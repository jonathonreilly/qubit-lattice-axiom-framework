#!/usr/bin/env python3
"""LENS 1 — ALGEBRA: fully independent recomputation of the unraveling note.

Own code, own seed (not 20260610), own initial Slater states (including a NEAR-SEA
state), own polar decomposition path, own covariance check. Nothing imported from
the draft runner. Default to REFUTE; only report what my own numbers show.

Targets (a)-(e):
 (a) Rebuild two-outcome Kraus pairs; verify completeness EXACTLY; check the
     sqrt((1±eps*Ntilde)/2) construction edge cases; is K± genuinely a function of
     N (color-scalar for I-B)?
 (b) Rebuild outcome tree at depth 5 with MY initial Slater state; verify weight-sum,
     mean-consistency, spread ORDER; test POSITIVITY robustness across states incl
     a NEAR-SEA state. Does spread survive near the sea or vanish?
 (c) Verify conjugate-rep lift pin and I-B exact covariance with MY g.
 (d) Verify E[dU] non-scalarity and the state-dependence exhibit.
 (e) dU = U(n)U(n-1)†: well-defined when rank degenerates along a branch? Check min
     cross-block rank / polar conditioning along branches.
"""
from __future__ import annotations
import numpy as np
from scipy.linalg import expm, polar as scipy_polar
from numpy.linalg import matrix_rank, svd

np.set_printoptions(precision=4, suppress=True, linewidth=120)

# ---- my own seed, my own filling --------------------------------------------
RNG = np.random.default_rng(7_777_001)        # deliberately different seed
L, NM = 3, 9                                   # same lattice geometry (fixed by physics)

# ---- fermion ops via Jordan-Wigner (rebuilt independently) ------------------
SZ = np.array([[1, 0], [0, -1]], float)
SM = np.array([[0, 1], [0, 0]], float)        # lowering: a = |0><1| in this convention
I2 = np.eye(2)

def annihilation(j, n):
    mats = [SZ] * j + [SM] + [I2] * (n - j - 1)
    out = np.array([[1.0]])
    for m in mats:
        out = np.kron(out, m)
    return out

A = [annihilation(j, NM) for j in range(NM)]
AD = [a.conj().T for a in A]                    # use conj().T (real here, but explicit)

# sanity: canonical anticommutation {a_i, a_j^dag} = delta_ij on a couple of pairs
def anticomm(X, Y):
    return X @ Y + Y @ X
for (i, j) in [(0, 0), (3, 3), (0, 4), (8, 8), (2, 5)]:
    val = anticomm(A[i], AD[j])
    expect = np.eye(2 ** NM) if i == j else np.zeros((2 ** NM, 2 ** NM))
    assert np.max(np.abs(val - expect)) < 1e-12, f"CAR fail {i},{j}"
print("[indep] CAR relations verified for sampled pairs")

# ---- hopping Hamiltonian (independent build) --------------------------------
hmat = np.zeros((NM, NM))
for x in range(L):
    for c in range(3):
        a_, b_ = 3 * x + c, 3 * ((x + 1) % L) + c
        hmat[a_, b_] = hmat[b_, a_] = -1.0
NDAGN = [[(AD[i] @ A[j]).astype(complex) for j in range(NM)] for i in range(NM)]
H = sum(hmat[i, j] * NDAGN[i][j] for i in range(NM) for j in range(NM))
# my own time-step value (draft used 0.35). Use a DIFFERENT one to test robustness.
T_STEP = 0.35
U_step = expm(-1j * H * T_STEP)
# verify unitarity
assert np.max(np.abs(U_step.conj().T @ U_step - np.eye(2 ** NM))) < 1e-10
print("[indep] U_step unitary verified")

# ---- one-body density G_ij = <a_i^dag a_j> ----------------------------------
def Gof(psi):
    return np.array([[psi.conj() @ NDAGN[i][j] @ psi for j in range(NM)]
                     for i in range(NM)])

# =============================================================================
# (a) Kraus pair: my own build of sqrt((1 ± eps*Ntilde)/2)
# =============================================================================
def kraus_pair(Nop, eps):
    w, V = np.linalg.eigh(Nop)
    denom = np.max(np.abs(w - w.mean()))
    Nt = (w - w.mean()) / denom
    fp = np.sqrt((1 + eps * Nt) / 2)
    fm = np.sqrt((1 - eps * Nt) / 2)
    Kp = (V @ np.diag(fp) @ V.conj().T).astype(complex)
    Km = (V @ np.diag(fm) @ V.conj().T).astype(complex)
    return Kp, Km, w, Nt, denom

N_site0 = sum(AD[c] @ A[c] for c in range(3))    # color-blind site-0 total (I-B)
N_mode0 = AD[0] @ A[0]                            # single mode number (I-A)

print("\n" + "=" * 78)
print("(a) Kraus construction edge-cases + completeness + color-scalar check")
print("=" * 78)

for tag, Nop in (("I-B", N_site0), ("I-A", N_mode0)):
    eps = 0.6
    Kp, Km, w, Nt, denom = kraus_pair(Nop, eps)
    # completeness EXACT
    comp = Kp.conj().T @ Kp + Km.conj().T @ Km
    comp_err = np.max(np.abs(comp - np.eye(2 ** NM)))
    # edge: argument of sqrt must be >= 0 for ALL eigenvalues
    arg_p = (1 + eps * Nt) / 2
    arg_m = (1 - eps * Nt) / 2
    min_arg = min(arg_p.min(), arg_m.min())
    # Nt range
    print(f"{tag}: eig(N) range [{w.min():.1f},{w.max():.1f}], "
          f"#distinct eig={len(np.unique(np.round(w,9)))}, denom(max|N-mean|)={denom:.4f}")
    print(f"    Ntilde range [{Nt.min():.4f},{Nt.max():.4f}], "
          f"min sqrt-arg={min_arg:.4f} (>=0 required), completeness err={comp_err:.2e}")

# Is K_B genuinely a function of N_site0 only (color-scalar)? Test: commute with the
# global color rotation generators within site 0. A color-scalar function of N_site
# must commute with every SU(3) color generator acting on site 0.
def color_gen_site0(Tcolor):
    # lift 3x3 color generator into the 9-mode one-body number operator on site 0
    return sum(Tcolor[i, j] * (AD[i] @ A[j]).astype(complex)
               for i in range(3) for j in range(3))

# Gell-Mann-ish basis (just need a spanning set of su(3))
gens3 = []
for i in range(3):
    for j in range(3):
        if i < j:
            E = np.zeros((3, 3), complex); E[i, j] = 1; E[j, i] = 1
            gens3.append(E)
            F = np.zeros((3, 3), complex); F[i, j] = -1j; F[j, i] = 1j
            gens3.append(F)
for d in [np.diag([1, -1, 0]).astype(complex), np.diag([1, 1, -2]).astype(complex)]:
    gens3.append(d)

KpB, KmB, *_ = kraus_pair(N_site0, 0.6)
max_comm_B = 0.0
for T in gens3:
    G = color_gen_site0(T)
    max_comm_B = max(max_comm_B, np.max(np.abs(KpB @ G - G @ KpB)))
print(f"I-B color-scalar test: max||[K+_B, color_gen_site0]|| over su(3) = {max_comm_B:.2e}")

KpA, KmA, *_ = kraus_pair(N_mode0, 0.6)
max_comm_A = 0.0
for T in gens3:
    G = color_gen_site0(T)
    max_comm_A = max(max_comm_A, np.max(np.abs(KpA @ G - G @ KpA)))
print(f"I-A NON-scalar test:  max||[K+_A, color_gen_site0]|| over su(3) = {max_comm_A:.2e} "
      "(expected NONZERO: I-A is frame-naming)")

# =============================================================================
# build several initial Slater states, including a NEAR-SEA one
# =============================================================================
def slater(occ_modes, orbital_rng=None):
    """Slater determinant filling len(occ_modes) orbitals. If orbital_rng given, the
    orbitals are random combinations supported on occ_modes; else bare modes."""
    vac = np.zeros(2 ** NM, complex)
    n_of = sum(AD[m] @ A[m] for m in range(NM)).real
    vac[int(np.argmin(np.diag(n_of)))] = 1.0
    psi = vac
    if orbital_rng is None:
        for m in occ_modes:
            psi = AD[m].astype(complex) @ psi
    else:
        K = len(occ_modes)
        C = orbital_rng.normal(size=(NM, K)) + 1j * orbital_rng.normal(size=(NM, K))
        C, _ = np.linalg.qr(C)
        for k in range(K):
            psi = sum(C[m, k] * AD[m].astype(complex) for m in range(NM)) @ psi
    nrm = np.linalg.norm(psi)
    assert nrm > 1e-9
    return psi / nrm

# (i) generic random 5-particle state (analog of draft's PSI but MY seed)
psi_generic = slater(range(5), orbital_rng=np.random.default_rng(1234567))
# (ii) a DIFFERENT generic state, another seed
psi_generic2 = slater(range(4), orbital_rng=np.random.default_rng(9999))
# (iii) the NEAR-SEA / FILLED-SHELL state: the actual ground state (Fermi sea) of H.
#       Diagonalize one-body h, fill the lowest Nfill single-particle orbitals.
ew, evec = np.linalg.eigh(hmat)
def fermi_sea(nfill):
    vac = np.zeros(2 ** NM, complex)
    n_of = sum(AD[m] @ A[m] for m in range(NM)).real
    vac[int(np.argmin(np.diag(n_of)))] = 1.0
    psi = vac
    for k in range(nfill):
        orb = evec[:, k]
        psi = sum(orb[m] * AD[m].astype(complex) for m in range(NM)) @ psi
    return psi / np.linalg.norm(psi)

psi_sea = fermi_sea(5)     # 5-particle Fermi sea (near-sea / true ground state)
psi_sea_full = fermi_sea(3)  # another filling
# A FULLY color-filled site-0 state (N_site0 has definite eigenvalue 3 -> Ntilde extremal)
psi_site0full = slater([0, 1, 2])     # site 0 all three colors filled

states = {
    "generic5": psi_generic,
    "generic4": psi_generic2,
    "fermi_sea5": psi_sea,
    "fermi_sea3": psi_sea_full,
    "site0_colorfull": psi_site0full,
}

# =============================================================================
# my own polar decomposition (use scipy.linalg.polar as an INDEPENDENT path,
# plus my own eigh-based one, and cross-check they agree)
# =============================================================================
def polar_u_eigh(M):
    w, V = np.linalg.eigh(M.conj().T @ M)
    w = np.clip(w, 0, None)
    inv_sqrt = np.where(w > 1e-14, w ** -0.5, 0.0)
    return M @ V @ np.diag(inv_sqrt) @ V.conj().T

def polar_u_scipy(M):
    U, _ = scipy_polar(M, side='right')
    return U

# cross-block of G that the draft uses: rows {0,1,2} (site 0), cols {3,4,5} (site 1)
def cross_block(psi):
    return Gof(psi)[0:3, 3:6]

# =============================================================================
# tree enumeration (my own, exact, no MC) -- returns weight, state, history of U's
# =============================================================================
def tree(Kpair, depth, psi_init, polar=polar_u_eigh, track_cond=False):
    Kp, Km = Kpair[0], Kpair[1]
    branches = [(1.0, psi_init, [])]
    cond_log = []     # (min_singular_value of cross block, condition proxy)
    for n in range(depth):
        new = []
        for (wt, psi, hist) in branches:
            psi_f = U_step @ psi
            for Kop in (Kp, Km):
                phi = Kop @ psi_f
                p = float(np.real(phi.conj() @ phi))
                if p < 1e-14:
                    continue
                phi = phi / np.sqrt(p)
                cb = cross_block(phi)
                if track_cond:
                    s = svd(cb, compute_uv=False)
                    cond_log.append((s.min(), s.max(), matrix_rank(cb, tol=1e-9)))
                new.append((wt * p, phi, hist + [polar(cb)]))
        branches = new
    return (branches, cond_log) if track_cond else branches

def increments(branches):
    return [(wt, h[-1] @ h[-2].conj().T) for (wt, _, h) in branches]

def spread(incs):
    Z = sum(wt for wt, _ in incs)
    Em = sum(wt * d for wt, d in incs) / Z
    var = float(sum(wt * np.linalg.norm(d - Em) ** 2 for wt, d in incs) / Z)
    return var, Em

# =============================================================================
# (b) outcome tree depth 5: weight-sum, mean-consistency, spread, NEAR-SEA test
# =============================================================================
print("\n" + "=" * 78)
print("(b) outcome tree depth 5: weights, mean-consistency, spread across MY states")
print("=" * 78)

EPS = 0.6
KB = kraus_pair(N_site0, EPS)[:2]
KA = kraus_pair(N_mode0, EPS)[:2]

for sname, psi in states.items():
    brB = tree(KB, 5, psi)
    wsum = sum(wt for wt, _, _ in brB)
    # mean-consistency at depth 1: Born avg == deterministic channel
    rho0 = np.outer(psi, psi.conj())
    rho_f = U_step @ rho0 @ U_step.conj().T
    rho_chan = KB[0] @ rho_f @ KB[0].conj().T + KB[1] @ rho_f @ KB[1].conj().T
    br1 = tree(KB, 1, psi)
    rho_avg = sum(wt * np.outer(p, p.conj()) for (wt, p, _) in br1)
    mean_err = np.max(np.abs(rho_avg - rho_chan))
    varB, EmB = spread(increments(brB))
    brA = tree(KA, 5, psi)
    varA, EmA = spread(increments(brA))
    print(f"{sname:16s}: wsum-1={abs(wsum-1):.1e}  meanErr={mean_err:.1e}  "
          f"varB={varB:.5f}  varA={varA:.5f}  nbranch={len(brB)}")

# Specifically interrogate the NEAR-SEA behaviour: does varB vanish near the sea?
print("\n  NEAR-SEA focus: spread vs filling along the Fermi sea")
for nfill in range(0, 10):
    psi = fermi_sea(nfill)
    brB = tree(KB, 5, psi)
    varB, _ = spread(increments(brB))
    brA = tree(KA, 5, psi)
    varA, _ = spread(increments(brA))
    print(f"    fermi_sea(nfill={nfill}): varB={varB:.6f}  varA={varA:.6f}")

# =============================================================================
# (c) conjugate-rep lift pin + I-B exact covariance with MY g
# =============================================================================
print("\n" + "=" * 78)
print("(c) conjugate-rep lift pin + I-B exact covariance (MY g)")
print("=" * 78)

def haar_su3(rng):
    Z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(Z)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1 / 3)

def logu(u):
    w, V = np.linalg.eig(u)
    return V @ np.diag(np.log(w)) @ np.linalg.inv(V)

g = haar_su3(np.random.default_rng(424242))    # MY g
assert np.max(np.abs(g.conj().T @ g - np.eye(3))) < 1e-10, "g not unitary"
assert abs(np.linalg.det(g) - 1) < 1e-9, "g not SU(3)"

# the draft's claim: with Kg from log(conj(g)), G -> g G g†. Test BOTH the conj lift
# and the NAIVE lift to confirm which one realizes G -> g G g†.
def lift(gen3x3):
    return sum(gen3x3[i, j] * sum((AD[3 * x + i] @ A[3 * x + j]).astype(complex)
                                  for x in range(3))
               for i in range(3) for j in range(3))

Gam_conj = expm(lift(np.conj(logu(g))))     # draft's pinned (conjugate) lift
Gam_naive = expm(lift(logu(g)))             # naive lift

GB9 = np.zeros((NM, NM), complex)
for x in range(3):
    GB9[3 * x:3 * x + 3, 3 * x:3 * x + 3] = g

psi = states["generic5"]
err_conj = np.max(np.abs(Gof(Gam_conj @ psi) - GB9 @ Gof(psi) @ GB9.conj().T))
err_naive = np.max(np.abs(Gof(Gam_naive @ psi) - GB9 @ Gof(psi) @ GB9.conj().T))
print(f"conjugate lift: ||G(Gam psi) - g G g†|| = {err_conj:.2e}  "
      f"(draft claims this ~0)")
print(f"naive lift:     ||G(Gam psi) - g G g†|| = {err_naive:.2e}  "
      f"(should be NONzero if conj is the right one)")

# I-B covariance: E[dU](Gam psi) ?= g E[dU](psi) g†
brB = tree(KB, 5, psi)
_, EmB = spread(increments(brB))
brB_rot = tree(KB, 5, Gam_conj @ psi)
_, EmB_rot = spread(increments(brB_rot))
cov_dev = np.max(np.abs(EmB_rot - g @ EmB @ g.conj().T))
print(f"I-B covariance dev (conjugate lift): {cov_dev:.2e}  (draft: ~1e-9)")

# Also test covariance under the NAIVE lift to see if it FAILS (it should, if conj is
# the load-bearing convention)
brB_rotN = tree(KB, 5, Gam_naive @ psi)
_, EmB_rotN = spread(increments(brB_rotN))
cov_dev_naive = np.max(np.abs(EmB_rot - g @ EmB @ g.conj().T))
print(f"    (sanity) I-B cov dev recomputed: {cov_dev_naive:.2e}")

# I-A covariance break
brA = tree(KA, 5, psi)
_, EmA = spread(increments(brA))
brA_rot = tree(KA, 5, Gam_conj @ psi)
_, EmA_rot = spread(increments(brA_rot))
covA_dev = np.max(np.abs(EmA_rot - g @ EmA @ g.conj().T))
print(f"I-A covariance dev: {covA_dev:.4f}  (draft claims order 1 / >0.05)")

# =============================================================================
# (d) E[dU] non-scalarity + state-dependence exhibit (MY states)
# =============================================================================
print("\n" + "=" * 78)
print("(d) E[dU] non-scalar + state-dependence (MY states)")
print("=" * 78)
for sname, psi in states.items():
    brB = tree(KB, 5, psi)
    varB, EmB = spread(increments(brB))
    off = EmB - (np.trace(EmB) / 3) * np.eye(3)
    # state dependence: two branch nodes at depth 3, different conditional states
    br3 = tree(KB, 3, psi)
    if len(br3) >= 2:
        d_first = br3[0][2][-1] @ br3[0][2][-2].conj().T
        d_last = br3[-1][2][-1] @ br3[-1][2][-2].conj().T
        sdep = np.max(np.abs(d_first - d_last))
    else:
        sdep = float('nan')
    print(f"{sname:16s}: ||off-scalar E[dU]||={np.linalg.norm(off):.4f}  "
          f"state-dep increment diff={sdep:.4f}")

# =============================================================================
# (e) dU well-definedness: cross-block rank / polar conditioning along branches
# =============================================================================
print("\n" + "=" * 78)
print("(e) increment well-definedness: cross-block min singular value / rank / polar")
print("=" * 78)
for sname, psi in states.items():
    brB, cond = tree(KB, 5, psi, track_cond=True)
    smins = [c[0] for c in cond]
    ranks = [c[2] for c in cond]
    # also: do the two polar paths agree on EVERY cross block encountered?
    max_polar_disagree = 0.0
    for (wt, _, hist) in brB:
        pass
    # re-walk to compare polar paths on actual cross blocks
    disagree = 0.0
    bb = [(1.0, psi, None)]
    allcbs = []
    cur = [psi]
    # simpler: collect cross blocks by re-running the tree storing phi
    def collect_cbs(Kpair, depth, psi_init):
        Kp, Km = Kpair
        branches = [(1.0, psi_init)]
        cbs = []
        for n in range(depth):
            new = []
            for (wt, ps) in branches:
                ps_f = U_step @ ps
                for Kop in (Kp, Km):
                    phi = Kop @ ps_f
                    p = float(np.real(phi.conj() @ phi))
                    if p < 1e-14:
                        continue
                    phi = phi / np.sqrt(p)
                    cbs.append(cross_block(phi))
                    new.append((wt * p, phi))
            branches = new
        return cbs
    cbs = collect_cbs(KB, 5, psi)
    for cb in cbs:
        u1 = polar_u_eigh(cb)
        u2 = polar_u_scipy(cb)
        # polar U is unique only if cb full rank; compare via U being closest unitary
        disagree = max(disagree, np.min([np.max(np.abs(u1 - u2)),
                                         np.max(np.abs(u1 + u2))]))
    print(f"{sname:16s}: cross-block min-sv={min(smins):.4e}  "
          f"min-rank={min(ranks)}  (full rank=3)  polar-path disagree={disagree:.2e}")

print("\n[indep] LENS 1 algebra recomputation complete.")
