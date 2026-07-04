"""Composite link under two named record instruments: pointer/erased split,
exact slaving, instrument footprint.

Route R-B of the gauge-link dynamics frontier (bounded-by-design). The
formation rule/process is not supplied by the axioms
(record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06,
post-append narrowed scope), so every record instrument here is a
NAMED ADMISSION, not a derivation. Two flanking admissions are named:

  I-A: per-site occupation-basis dephasing instrument -- Lueders projectors
       onto joint eigenspaces of (n_{x,1}, n_{x,2}, n_{x,3}) in the SUPPLIED
       per-site C^3 color basis (8 projectors/site). The finest per-site
       occupancy readout; it NAMES a color frame at each site.
  I-B: per-site total-occupation Lueders instrument -- projectors onto
       eigenspaces of N_x = sum_i n_{x,i} (4 projectors/site). The coarsest
       non-trivial per-site occupancy readout; color-blind (commutes with all
       local color-frame rotations), so it names NO frame.

Both are applied at partial strength lam in [0,1]:
  rho -> (1-lam) rho + lam sum_P P rho P,  interleaved with exact Hamiltonian
steps e^{-iH tau} of the block-01 model H's (uniform quadratic NN hopping,
free / frozen-generic-SU(3)-background).

Measured exactly (finite-dimensional algebra; PASS/FAIL):
  A. Fock-level anchor (2 sites x 3 colors, dim 64, Jordan-Wigner): the exact
     one-body transformation rules of both instruments on arbitrary
     (non-Gaussian) states; channel covariance split (I-B commutes with local
     color rotations, I-A does not).
  B. Pointer/erased split: the composite-link carrier M(x,y) is ERASED content
     under both instruments; surviving on-site content is instrument-dependent
     (I-A: named-frame occupations; I-B: the full Ad-covariant local color
     density). tr M(x,x) survives both.
  C. Single-edge interleaved model is EXACTLY SOLVABLE (H^2 = 1): exact mode
     decomposition -- the s-parallel cross mode (s = -i(V M(y,y) - M(x,x) V))
     is exactly invariant (V s^dag V = -s), slaved coefficient
     alpha = eta sin(tau)cos(tau)/(1 - eta cos(2tau)) exact (eta = (1-lam)^2),
     all s-orthogonal cross modes contract by eta cos(2tau) per step, the
     slaved link U_eff = polar(s) is CONSTANT along the pointer relaxation,
     and the pointer sector is closed (autonomous in registered data) at
     leading order:
     Delta M(x,x) = -sin^2(tau) (M(x,x) - V M(y,y) V^dag) + O(eta) feedback.
  D. 4-cycle (chords present): the slaving holds at leading order in tau and
     the chord channel is damped OUT of the slaved direction (records localize
     the slaved link); lam=0 contrast is order-1.
  E. The block-01 non-autonomy exhibit under records: the hidden-Q channel is
     damped -- the two trajectories with identical U_eff(0)/local densities
     converge instead of separating; the slaved link differs order-1 between
     I-A and I-B (the admission's footprint, exhibited).

Memory-safe: largest objects are 64x64 (Fock anchor); all dynamics 6x6/12x12.
Prints "TOTAL: PASS=N FAIL=0" on success.
"""
from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260609)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    msg = f"[{tag}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def info(name: str, detail: str) -> None:
    print(f"[INFO] {name}: {detail}")


# ----------------------------------------------------------------------
# shared helpers (3x3 color blocks; conventions of the block-01 runner)
# ----------------------------------------------------------------------

def crand(*shape):
    return RNG.standard_normal(shape) + 1j * RNG.standard_normal(shape)


def haar_su3():
    z = crand(3, 3)
    q, r = np.linalg.qr(z)
    q = q @ np.diag(np.exp(-1j * np.angle(np.diag(r))))
    return q / np.linalg.det(q) ** (1.0 / 3.0)


def polar_uq(m):
    """m = u q, q = (m^dag m)^{1/2} PD Hermitian, u unitary (m invertible)."""
    w, v = np.linalg.eigh(m.conj().T @ m)
    q = v @ np.diag(np.sqrt(w)) @ v.conj().T
    u = m @ v @ np.diag(1.0 / np.sqrt(w)) @ v.conj().T
    return u, q


def block(mat, x, y):
    return mat[3 * x: 3 * x + 3, 3 * y: 3 * y + 3]


# ======================================================================
# Part A: Fock-level anchor for the one-body instrument rules
# (2 sites x 3 colors = 6 modes, dim 64, Jordan-Wigner)
# ======================================================================
print("== Part A: Fock-level anchor (instrument rules are exact one-body maps) ==")

N_MODES = 6
DIM_F = 2 ** N_MODES
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SM = np.array([[0, 1], [0, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def jw_annihilator(m):
    ops = [SZ] * m + [SM] + [I2] * (N_MODES - m - 1)
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


A_OPS = [jw_annihilator(m) for m in range(N_MODES)]
AD_OPS = [a.conj().T for a in A_OPS]
NUM_OPS = [AD_OPS[m] @ A_OPS[m] for m in range(N_MODES)]

car_dev = 0.0
for m in range(N_MODES):
    for n in range(N_MODES):
        anti = A_OPS[m] @ AD_OPS[n] + AD_OPS[n] @ A_OPS[m]
        car_dev = max(car_dev, np.abs(anti - (1.0 if m == n else 0.0) * np.eye(DIM_F)).max())
        anti2 = A_OPS[m] @ A_OPS[n] + A_OPS[n] @ A_OPS[m]
        car_dev = max(car_dev, np.abs(anti2).max())
check("A1: CAR algebra exact (Jordan-Wigner, 6 modes)", car_dev < 1e-13,
      f"max dev = {car_dev:.2e}")


def one_body_of(rho_f):
    """C[m,n] = tr(rho a^dag_n a_m); M(x,y) = C[3x:3x+3, 3y:3y+3]."""
    c = np.zeros((N_MODES, N_MODES), complex)
    for m in range(N_MODES):
        for n in range(N_MODES):
            c[m, n] = np.trace(rho_f @ AD_OPS[n] @ A_OPS[m])
    return c


def fock_quadratic(h1):
    out = np.zeros((DIM_F, DIM_F), complex)
    for m in range(N_MODES):
        for n in range(N_MODES):
            out += h1[m, n] * AD_OPS[m] @ A_OPS[n]
    return out


def unitary_of(h, t):
    w, v = np.linalg.eigh(h)
    return v @ np.diag(np.exp(-1j * w * t)) @ v.conj().T


# random NON-Gaussian Fock state (tests the rules beyond Gaussian states)
GF = crand(DIM_F, DIM_F)
RHO_F = GF @ GF.conj().T
RHO_F /= np.trace(RHO_F).real

h1_test = crand(6, 6)
h1_test = (h1_test + h1_test.conj().T) / 2
EF = unitary_of(fock_quadratic(h1_test), 0.37)
e1 = unitary_of(h1_test, 0.37)
cl_dev = np.abs(one_body_of(EF @ RHO_F @ EF.conj().T)
                - e1 @ one_body_of(RHO_F) @ e1.conj().T).max()
check("A2: one-body data evolves autonomously under quadratic H (non-Gaussian state)",
      cl_dev < 1e-12, f"max dev = {cl_dev:.2e}")


def projectors_ia(site):
    out = []
    for b in range(8):
        p = np.eye(DIM_F, dtype=complex)
        for i in range(3):
            nm = NUM_OPS[3 * site + i]
            p = p @ (nm if (b >> i) & 1 else np.eye(DIM_F) - nm)
        out.append(p)
    return out


def projectors_ib(site):
    nx = sum(NUM_OPS[3 * site + i] for i in range(3))
    out = []
    for k in range(4):
        p = np.eye(DIM_F, dtype=complex)
        for j in range(4):
            if j != k:
                p = p @ (nx - j * np.eye(DIM_F)) / (k - j)
        out.append(p)
    return out


PROJ_IA = [projectors_ia(0), projectors_ia(1)]
PROJ_IB = [projectors_ib(0), projectors_ib(1)]

for tag, plists in (("A3: I-A", PROJ_IA), ("A4: I-B", PROJ_IB)):
    dev = 0.0
    for pl in plists:
        dev = max(dev, np.abs(sum(pl) - np.eye(DIM_F)).max())
        for p in pl:
            dev = max(dev, np.abs(p @ p - p).max(), np.abs(p - p.conj().T).max())
    check(f"{tag} projector family: orthogonal resolution of identity (both sites)",
          dev < 1e-12, f"max dev = {dev:.2e}")


def lueders(rho_f, projs):
    return sum(p @ rho_f @ p for p in projs)


def partial_site(rho_f, projs, lam):
    return (1 - lam) * rho_f + lam * lueders(rho_f, projs)


def apply_instrument(rho_f, proj_pair, lam):
    return partial_site(partial_site(rho_f, proj_pair[0], lam), proj_pair[1], lam)


C0F = one_body_of(RHO_F)
XX0, XY0, YY0 = C0F[:3, :3], C0F[:3, 3:], C0F[3:, 3:]

dev_a = 0.0
for lam in (1.0, 0.4):
    c1 = one_body_of(apply_instrument(RHO_F, PROJ_IA, lam))
    dev_a = max(dev_a,
                np.abs(c1[:3, :3] - ((1 - lam) * XX0 + lam * np.diag(np.diag(XX0)))).max(),
                np.abs(c1[3:, 3:] - ((1 - lam) * YY0 + lam * np.diag(np.diag(YY0)))).max(),
                np.abs(c1[:3, 3:] - (1 - lam) ** 2 * XY0).max())
check("A5: I-A one-body rule exact: M(x,x)->(1-lam)M+lam diag, M(x,y)->(1-lam)^2 M",
      dev_a < 1e-12, f"max dev (lam=1, 0.4) = {dev_a:.2e}")

dev_b = 0.0
for lam in (1.0, 0.4):
    c1 = one_body_of(apply_instrument(RHO_F, PROJ_IB, lam))
    dev_b = max(dev_b,
                np.abs(c1[:3, :3] - XX0).max(),
                np.abs(c1[3:, 3:] - YY0).max(),
                np.abs(c1[:3, 3:] - (1 - lam) ** 2 * XY0).max())
check("A6: I-B one-body rule exact: M(x,x) preserved FULLY, M(x,y)->(1-lam)^2 M",
      dev_b < 1e-12, f"max dev (lam=1, 0.4) = {dev_b:.2e}")

ord_dev = np.abs(partial_site(partial_site(RHO_F, PROJ_IB[0], 0.6), PROJ_IB[1], 0.6)
                 - partial_site(partial_site(RHO_F, PROJ_IB[1], 0.6), PROJ_IB[0], 0.6)).max()
check("A7: site-composition order-independence of the instrument (Fock level)",
      ord_dev < 1e-13, f"max dev = {ord_dev:.2e}")


def gamma_local(g, site):
    """Fock representation of the local color rotation (g at site, 1 elsewhere)."""
    w, v = np.linalg.eig(g)
    hg = v @ np.diag(np.log(w) / 1j) @ np.linalg.inv(v)
    hg = (hg + hg.conj().T) / 2
    u1 = np.zeros((6, 6), complex)
    u1[3 * site:3 * site + 3, 3 * site:3 * site + 3] = hg
    hf = fock_quadratic(u1)
    wf, vf = np.linalg.eigh(hf)
    return vf @ np.diag(np.exp(1j * wf)) @ vf.conj().T


G_TEST = haar_su3()
GAM = gamma_local(G_TEST, 0)
g1full = np.eye(6, dtype=complex)
g1full[:3, :3] = G_TEST
int_dev = 0.0
for m in range(N_MODES):
    lhs = GAM @ AD_OPS[m] @ GAM.conj().T
    rhs = sum(g1full[n, m] * AD_OPS[n] for n in range(N_MODES))
    int_dev = max(int_dev, np.abs(lhs - rhs).max())
check("A8: Fock rep intertwines the one-body rotation (setup)", int_dev < 1e-12,
      f"max dev = {int_dev:.2e}")

ROT_F = GAM @ RHO_F @ GAM.conj().T
cov_b = np.abs(lueders(ROT_F, PROJ_IB[0])
               - GAM @ lueders(RHO_F, PROJ_IB[0]) @ GAM.conj().T).max()
cov_a = np.abs(lueders(ROT_F, PROJ_IA[0])
               - GAM @ lueders(RHO_F, PROJ_IA[0]) @ GAM.conj().T).max()
check("A9: I-B channel commutes with local color rotations (color-blind, exact)",
      cov_b < 1e-12, f"max dev = {cov_b:.2e}")
check("A10: I-A channel does NOT commute with local color rotations (frame-naming teeth)",
      cov_a > 1e-4, f"violation = {cov_a:.3e} (vs I-B {cov_b:.2e})")

tr_dev = 0.0
for projs in (PROJ_IA, PROJ_IB):
    c1 = one_body_of(apply_instrument(RHO_F, projs, 0.7))
    tr_dev = max(tr_dev, abs(np.trace(c1[:3, :3]) - np.trace(XX0)),
                 abs(np.trace(c1[3:, 3:]) - np.trace(YY0)))
check("A11: tr M(x,x) exactly conserved by both instruments", tr_dev < 1e-12,
      f"max dev = {tr_dev:.2e}")

# ======================================================================
# Part B: pointer / erased split at the one-body level
# (rules anchored by Part A; from here all dynamics is one-body, exact)
# ======================================================================
print()
print("== Part B: pointer vs erased content of the composite-link carrier ==")


def dmap_ia(c, lam, n_sites):
    out = np.zeros_like(c)
    for x in range(n_sites):
        for y in range(n_sites):
            b = block(c, x, y)
            if x == y:
                out[3 * x:3 * x + 3, 3 * y:3 * y + 3] = \
                    (1 - lam) * b + lam * np.diag(np.diag(b))
            else:
                out[3 * x:3 * x + 3, 3 * y:3 * y + 3] = (1 - lam) ** 2 * b
    return out


def dmap_ib(c, lam, n_sites):
    out = c.copy()
    for x in range(n_sites):
        for y in range(n_sites):
            if x != y:
                out[3 * x:3 * x + 3, 3 * y:3 * y + 3] *= (1 - lam) ** 2
    return out


modes6 = np.linalg.qr(crand(6, 4))[0][:, :4]
C6 = modes6 @ modes6.conj().T

ca1 = dmap_ia(C6, 1.0, 2)
check("B1: I-A at lam=1: pointer = named-frame occupations; on-site coherences "
      "AND the link carrier M(x,y) erased",
      np.abs(ca1[:3, 3:]).max() < 1e-15
      and np.abs(ca1[:3, :3] - np.diag(np.diag(C6[:3, :3]))).max() < 1e-15)
cb1 = dmap_ib(C6, 1.0, 2)
check("B2: I-B at lam=1: pointer = FULL local color densities M(x,x); "
      "the link carrier M(x,y) erased",
      np.abs(cb1[:3, 3:]).max() < 1e-15
      and np.abs(cb1[:3, :3] - C6[:3, :3]).max() < 1e-15)
check("B3: lam=1 maps idempotent (pointer projections)",
      np.abs(dmap_ia(ca1, 1.0, 2) - ca1).max() < 1e-15
      and np.abs(dmap_ib(cb1, 1.0, 2) - cb1).max() < 1e-15)

spec0 = np.sort(np.linalg.eigvalsh(C6[:3, :3]))
spec_a = np.sort(np.linalg.eigvalsh(dmap_ia(C6, 0.7, 2)[:3, :3]))
spec_b = np.sort(np.linalg.eigvalsh(dmap_ib(C6, 0.7, 2)[:3, :3]))
check("B4: spec M(x,x) preserved by I-B, changed by I-A (registered local color "
      "content is instrument-dependent)",
      np.abs(spec_b - spec0).max() < 1e-13 and np.abs(spec_a - spec0).max() > 1e-3,
      f"I-B dev = {np.abs(spec_b - spec0).max():.2e}, I-A dev = {np.abs(spec_a - spec0).max():.3f}")

# pointer-content covariance class: I-B registered content is Ad-covariant
gx = haar_su3()
m_loc = C6[:3, :3]
spec_rot = np.sort(np.linalg.eigvalsh(gx @ m_loc @ gx.conj().T))
diag_rot = np.sort(np.abs(np.diag(gx @ m_loc @ gx.conj().T)))
diag_orig = np.sort(np.abs(np.diag(m_loc)))
check("B5: I-B pointer content Ad-covariant (spec invariant under local rotation); "
      "I-A pointer content frame-dependent (occupation vector not stable)",
      np.abs(spec_rot - spec0).max() < 1e-13 and np.abs(diag_rot - diag_orig).max() > 1e-3,
      f"spec dev = {np.abs(spec_rot - spec0).max():.2e}, "
      f"diag change = {np.abs(diag_rot - diag_orig).max():.3f}")

# ======================================================================
# Part C: single-edge interleaved model -- exact mode decomposition
# ======================================================================
print()
print("== Part C: single edge is exactly solvable; exact slaving structure ==")

V_BG = haar_su3()
H_EDGE = np.zeros((6, 6), complex)
H_EDGE[:3, 3:] = V_BG
H_EDGE[3:, :3] = V_BG.conj().T

dev_h2 = np.abs(H_EDGE @ H_EDGE - np.eye(6)).max()
TAU = 0.05
E_TAU = np.cos(TAU) * np.eye(6) - 1j * np.sin(TAU) * H_EDGE
W_E, V_E = np.linalg.eigh(H_EDGE)
E_REF = V_E @ np.diag(np.exp(-1j * W_E * TAU)) @ V_E.conj().T
check("C1: H_edge^2 = 1 and e^{-iH tau} = cos(tau) - i sin(tau) H exactly",
      dev_h2 < 1e-13 and np.abs(E_TAU - E_REF).max() < 1e-13,
      f"H^2 dev = {dev_h2:.2e}, expm dev = {np.abs(E_TAU - E_REF).max():.2e}")


def edge_step(c, lam, tau, which="IB"):
    e = np.cos(tau) * np.eye(6) - 1j * np.sin(tau) * H_EDGE
    c = e @ c @ e.conj().T
    return dmap_ib(c, lam, 2) if which == "IB" else dmap_ia(c, lam, 2)


def s_of(c):
    return -1j * (V_BG @ c[3:, 3:] - c[:3, :3] @ V_BG)


LAM_C = 0.9
ETA_C = (1 - LAM_C) ** 2

rho_t = C6.copy()
ct, st_ = np.cos(TAU), np.sin(TAU)
rp = E_TAU @ rho_t @ E_TAU.conj().T
p1, p2, mblk = rho_t[:3, :3], rho_t[3:, 3:], rho_t[:3, 3:]
sv = s_of(rho_t)
p1_pred = ct * ct * p1 + st_ * st_ * V_BG @ p2 @ V_BG.conj().T \
    - 1j * st_ * ct * (V_BG @ mblk.conj().T - mblk @ V_BG.conj().T)
m_pred = ct * ct * mblk + st_ * ct * sv + st_ * st_ * V_BG @ mblk.conj().T @ V_BG
check("C2: exact one-step block identities (pointer flow + cross-mode map)",
      np.abs(rp[:3, :3] - p1_pred).max() < 1e-13
      and np.abs(rp[:3, 3:] - m_pred).max() < 1e-13,
      f"P1 dev = {np.abs(rp[:3, :3] - p1_pred).max():.2e}, "
      f"m dev = {np.abs(rp[:3, 3:] - m_pred).max():.2e}")

dev_vs = 0.0
for _ in range(5):
    ar, br = crand(3, 3), crand(3, 3)
    pa, pb = ar @ ar.conj().T, br @ br.conj().T
    svr = -1j * (V_BG @ pb - pa @ V_BG)
    dev_vs = max(dev_vs, np.abs(V_BG @ svr.conj().T @ V_BG + svr).max())
check("C3: V s^dag V = -s for every Hermitian density pair (s-mode is exactly "
      "self-conjugate under the step)", dev_vs < 1e-12, f"max dev = {dev_vs:.2e}")

alpha = ETA_C * st_ * ct / (1 - ETA_C * np.cos(2 * TAU))
mstar = alpha * sv
fp_dev = np.abs(mstar - ETA_C * (ct * ct * mstar + st_ * ct * sv
                                 + st_ * st_ * V_BG @ mstar.conj().T @ V_BG)).max()
check("C4: slaved coefficient EXACT: alpha = eta sc/(1 - eta cos 2tau) is the "
      "s-mode fixed point (frozen pointer data)", fp_dev < 1e-15,
      f"fixed-point dev = {fp_dev:.2e}, alpha = {alpha:.4e}")

cburn = C6.copy()
for _ in range(800):
    cburn = edge_step(cburn, LAM_C, TAU, "IB")
m_b = cburn[:3, 3:]
s_b = s_of(cburn)
sig_b = np.linalg.svd(m_b, compute_uv=False)
u_m, _ = polar_uq(m_b)
u_s, _ = polar_uq(s_b)
check("C5: record-dominated slaving: U_eff = polar(s) on the slow manifold "
      "(s = -i(V M(y,y) - M(x,x) V), pointer data only)",
      np.linalg.norm(u_m - u_s) < 1e-9 and sig_b[2] / sig_b[0] > 0.05,
      f"|U_eff - polar(s)|_F = {np.linalg.norm(u_m - u_s):.2e}, "
      f"sig3/sig1 = {sig_b[2]/sig_b[0]:.3f}")

pert = crand(3, 3)
pert -= (np.vdot(s_b, pert) / np.vdot(s_b, s_b)) * s_b
pert *= 1e-6 / np.linalg.norm(pert)
cpert = cburn.copy()
cpert[:3, 3:] += pert
cpert[3:, :3] += pert.conj().T
d_after = edge_step(cpert, LAM_C, TAU, "IB")[:3, 3:] - edge_step(cburn, LAM_C, TAU, "IB")[:3, 3:]
contr = np.linalg.norm(d_after) / np.linalg.norm(pert)
check("C6: every s-orthogonal cross mode contracts at the exact instrument rate "
      "~ eta per step (hidden-data channel damping)",
      0.9 * ETA_C < contr < 1.01 * ETA_C,
      f"contraction = {contr:.6f}, eta = {ETA_C:.6f}")

u_ref = u_m
cdrift = cburn.copy()
max_u_drift = 0.0
max_step_rel = 0.0
s_start = np.linalg.norm(s_of(cdrift))
for _ in range(2000):
    s_prev = s_of(cdrift)
    cdrift = edge_step(cdrift, LAM_C, TAU, "IB")
    s_next = s_of(cdrift)
    max_step_rel = max(max_step_rel,
                       np.linalg.norm(s_next - np.cos(2 * TAU) * s_prev)
                       / np.linalg.norm(s_prev))
    mm = cdrift[:3, 3:]
    if np.linalg.svd(mm, compute_uv=False)[2] > 1e-12:
        uu, _ = polar_uq(mm)
        max_u_drift = max(max_u_drift, np.linalg.norm(uu - u_ref))
s_end = np.linalg.norm(s_of(cdrift))
check("C7: the slaved link is CONSTANT along the pointer relaxation "
      "(registered link direction frozen)", max_u_drift < 1e-6,
      f"max drift over 2000 steps = {max_u_drift:.2e}")
ratio_pred = np.cos(2 * TAU) ** 2000
ratio_meas = s_end / s_start
check("C8: source contracts along itself: s' = cos(2 tau) s + O(eta) feedback "
      "per step; |s| tracks cos(2 tau)^n over 2000 steps within the "
      "accumulated O(eta) window",
      max_step_rel < 5 * ETA_C / (1 - ETA_C)
      and 0.5 * ratio_pred < ratio_meas < 1.5 * ratio_pred,
      f"per-step rel dev = {max_step_rel:.2e} (bound {5*ETA_C/(1-ETA_C):.2e}); "
      f"2000-step ratio = {ratio_meas:.3e} vs cos(2tau)^2000 = {ratio_pred:.3e}")

rel_errs = []
cflow = cburn.copy()
for _ in range(50):
    p1c, p2c = cflow[:3, :3].copy(), cflow[3:, 3:].copy()
    cn = edge_step(cflow, LAM_C, TAU, "IB")
    dp1 = cn[:3, :3] - p1c
    pred = -np.sin(TAU) ** 2 * (p1c - V_BG @ p2c @ V_BG.conj().T)
    rel_errs.append(np.linalg.norm(dp1 - pred) / np.linalg.norm(dp1))
check("C9: pointer-sector flow is closed (autonomous in registered data) at "
      "leading order: Delta M(x,x) = -sin^2(tau)(M(x,x) - V M(y,y) V^dag) "
      "+ O(eta) feedback",
      max(rel_errs) < 0.05, f"max rel err = {max(rel_errs):.4f} "
      f"(eta/(1-eta) = {ETA_C/(1-ETA_C):.4f})")

cflow = C6.copy()
for _ in range(100):
    cflow = edge_step(cflow, LAM_C, TAU, "IA")
rel_errs_a = []
for _ in range(50):
    n1 = np.diag(cflow[:3, :3]).copy()
    n2 = np.diag(cflow[3:, 3:]).copy()
    cn = edge_step(cflow, LAM_C, TAU, "IA")
    dn1 = np.diag(cn[:3, :3]) - n1
    pred = np.diag(-np.sin(TAU) ** 2 * (np.diag(n1) - V_BG @ np.diag(n2) @ V_BG.conj().T))
    rel_errs_a.append(np.linalg.norm(dn1 - pred) / np.linalg.norm(dn1))
    cflow = cn
check("C10: I-A analogue is closed on ITS pointer content (named-frame occupations)",
      max(rel_errs_a) < 0.05, f"max rel err = {max(rel_errs_a):.4f}")

c_nor = C6.copy()
for _ in range(800):
    c_nor = edge_step(c_nor, 0.0, TAU, "IB")
u_nor, _ = polar_uq(c_nor[:3, 3:])
u_snor, _ = polar_uq(s_of(c_nor))
check("C11: lam=0 contrast: WITHOUT records the link is NOT slaved to pointer "
      "data (order-1 deviation)", np.linalg.norm(u_nor - u_snor) > 0.3,
      f"|U_eff - polar(s)|_F = {np.linalg.norm(u_nor - u_snor):.3f}")

# free-H variant (V = 1): same exact structure, slaving holds
H_SAVE = H_EDGE.copy()
V_SAVE = V_BG.copy()
H_EDGE = np.zeros((6, 6), complex)
H_EDGE[:3, 3:] = np.eye(3)
H_EDGE[3:, :3] = np.eye(3)
V_BG = np.eye(3, dtype=complex)
cfree = C6.copy()
for _ in range(800):
    cfree = edge_step(cfree, LAM_C, TAU, "IB")
m_f = cfree[:3, 3:]
s_f = s_of(cfree)
sig_f = np.linalg.svd(m_f, compute_uv=False)
ok_free = sig_f[2] > 1e-12
if ok_free:
    u_mf, _ = polar_uq(m_f)
    u_sf, _ = polar_uq(s_f)
    dev_free = np.linalg.norm(u_mf - u_sf)
else:
    dev_free = np.inf
check("C12: free hopping (V = 1): same exact slaving U_eff = polar(s)",
      ok_free and dev_free < 1e-9, f"|U_eff - polar(s)|_F = {dev_free:.2e}")
H_EDGE = H_SAVE
V_BG = V_SAVE

# ======================================================================
# Part D: 4-cycle (chords present) -- leading-order slaving, localization,
# covariance of the instrumented trajectory
# ======================================================================
print()
print("== Part D: 4-cycle slaving, chord localization, covariance split ==")

N_SITES = 4
DIM = 12
EDGES = [(0, 1), (1, 2), (2, 3), (3, 0)]
LINKS = [haar_su3() for _ in EDGES]
H4 = np.zeros((DIM, DIM), complex)
for k, (x, y) in enumerate(EDGES):
    H4[3 * x:3 * x + 3, 3 * y:3 * y + 3] = LINKS[k]
    H4[3 * y:3 * y + 3, 3 * x:3 * x + 3] = LINKS[k].conj().T
W4, V4 = np.linalg.eigh(H4)
LINK_OF = {}
for k, (x, y) in enumerate(EDGES):
    LINK_OF[(x, y)] = LINKS[k]
    LINK_OF[(y, x)] = LINKS[k].conj().T
NBR = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}


def cycle_step(c, lam, tau, which="IB"):
    e = V4 @ np.diag(np.exp(-1j * W4 * tau)) @ V4.conj().T
    c = e @ c @ e.conj().T
    return dmap_ib(c, lam, N_SITES) if which == "IB" else dmap_ia(c, lam, N_SITES)


def s_local(c, x, y):
    v_xy = LINK_OF[(x, y)]
    return -1j * (v_xy @ block(c, y, y) - block(c, x, x) @ v_xy)


def s_chordful(c, x, y):
    s = s_local(c, x, y)
    for z in NBR[x]:
        if z != y:
            s += -1j * (LINK_OF[(x, z)] @ block(c, z, y))
    for z in NBR[y]:
        if z != x:
            s -= -1j * (block(c, x, z) @ LINK_OF[(z, y)])
    return s


modes12 = np.linalg.qr(crand(DIM, 4))[0][:, :4]
C12 = modes12 @ modes12.conj().T

devs = {}
for tau in (0.02, 0.01):
    c = C12.copy()
    for _ in range(int(12.0 / tau)):
        c = cycle_step(c, 0.9, tau, "IB")
    dev_loc, dev_split, sig_min = 0.0, 0.0, np.inf
    for (x, y) in EDGES:
        m = block(c, x, y)
        sl = s_local(c, x, y)
        sc = s_chordful(c, x, y)
        u_m, _ = polar_uq(m)
        u_l, _ = polar_uq(sl)
        u_c, _ = polar_uq(sc)
        dev_loc = max(dev_loc, np.linalg.norm(u_m - u_l))
        dev_split = max(dev_split, np.linalg.norm(u_c - u_l))
        sig = np.linalg.svd(m, compute_uv=False)
        sig_min = min(sig_min, sig[2] / sig[0])
    devs[tau] = (dev_loc, dev_split, sig_min)
check("D1: 4-cycle slaving at leading order: U_eff = polar(s_local) on every "
      "edge (lam=0.9, tau=0.02)", devs[0.02][0] < 2.5e-3,
      f"max dev = {devs[0.02][0]:.2e}")
check("D2: deviation is higher-order: shrinks by >= 3x under tau halving",
      devs[0.01][0] < devs[0.02][0] / 3.0,
      f"tau=0.02: {devs[0.02][0]:.2e} -> tau=0.01: {devs[0.01][0]:.2e}")
check("D3: chord channel damped OUT of the slaved direction: "
      "polar(s_chordful) = polar(s_local) far below the leading deviation",
      devs[0.02][1] < 1e-4 and devs[0.01][1] < 1e-4,
      f"chord-vs-local: {devs[0.02][1]:.2e} (tau=0.02), {devs[0.01][1]:.2e} (tau=0.01)")
check("D4: slaved link well-defined at this configuration: min sig3/sig1 after "
      "burn-in bounded away from degeneracy (> 0.05)",
      min(devs[0.02][2], devs[0.01][2]) > 0.05,
      f"min sig3/sig1 = {min(devs[0.02][2], devs[0.01][2]):.3f} (seed-specific margin)")

c = C12.copy()
for _ in range(600):
    c = cycle_step(c, 0.0, 0.02, "IB")
dev0 = max(np.linalg.norm(polar_uq(block(c, x, y))[0] - polar_uq(s_local(c, x, y))[0])
           for (x, y) in EDGES)
check("D5: lam=0 baseline on the 4-cycle: order-1 (records absent, no slaving)",
      dev0 > 0.5, f"max dev = {dev0:.3f}")

# covariance of the instrumented trajectory (2-site, exact contrast)
gs_pair = [haar_su3(), haar_su3()]
GD = np.zeros((6, 6), complex)
GD[:3, :3] = gs_pair[0]
GD[3:, 3:] = gs_pair[1]
V_ROT = gs_pair[0] @ V_BG @ gs_pair[1].conj().T
H_ROT = np.zeros((6, 6), complex)
H_ROT[:3, 3:] = V_ROT
H_ROT[3:, :3] = V_ROT.conj().T


def edge_step_rot(c, lam, tau, which="IB"):
    e = np.cos(tau) * np.eye(6) - 1j * np.sin(tau) * H_ROT
    c = e @ c @ e.conj().T
    return dmap_ib(c, lam, 2) if which == "IB" else dmap_ia(c, lam, 2)


for which, expect_exact, tag in (("IB", True, "D6"), ("IA", False, "D7")):
    cb = C6.copy()
    cr = GD @ C6 @ GD.conj().T
    dev_cov = 0.0
    for _ in range(60):
        cb = edge_step(cb, 0.6, TAU, which)
        cr = edge_step_rot(cr, 0.6, TAU, which)
        sb = np.linalg.svd(cb[:3, 3:], compute_uv=False)
        if sb[2] > 1e-10:
            ub, _ = polar_uq(cb[:3, 3:])
            ur, _ = polar_uq(cr[:3, 3:])
            dev_cov = max(dev_cov, np.abs(ur - gs_pair[0] @ ub @ gs_pair[1].conj().T).max())
    if expect_exact:
        check(f"{tag}: joint local covariance of the INSTRUMENTED link trajectory "
              "is exact under I-B (color-blind instrument)", dev_cov < 1e-10,
              f"max dev = {dev_cov:.2e}")
    else:
        check(f"{tag}: joint local covariance FAILS under I-A "
              "(the named frame breaks it -- admission footprint)", dev_cov > 0.1,
              f"max violation = {dev_cov:.3f}")

# ======================================================================
# Part E: the block-01 non-autonomy exhibit under records
# ======================================================================
print()
print("== Part E: the hidden-Q non-autonomy channel under records ==")

g1m, g2m = crand(3, 3), crand(3, 3)
rho_a = np.block([[g1m @ g1m.conj().T, g1m @ g2m.conj().T],
                  [g2m @ g1m.conj().T, g2m @ g2m.conj().T]])
rho_a = rho_a + 0.10 * (np.trace(rho_a).real / 6.0) * np.eye(6)
rho_a = rho_a / (1.3 * np.linalg.eigvalsh(rho_a).max())
p1p, p2p = rho_a[:3, :3].copy(), rho_a[3:, 3:].copy()
m_a = rho_a[:3, 3:].copy()
u0, q_a = polar_uq(m_a)
d_raw = crand(3, 3)
delta0 = d_raw @ d_raw.conj().T
delta0 *= 0.5 * np.linalg.norm(q_a) / np.linalg.norm(delta0)
rho_b = None
q_b = None
for back in range(12):
    cand_q = q_a + delta0 / (2.0 ** back)
    cand = np.block([[p1p, u0 @ cand_q], [(u0 @ cand_q).conj().T, p2p]])
    ev = np.linalg.eigvalsh(cand)
    if ev.min() > 1e-6 and ev.max() <= 1.0:
        q_b = cand_q
        rho_b = cand
        break
assert rho_b is not None, "exhibit backoff failed"

u_b0, _ = polar_uq(rho_b[:3, 3:])
eigs_a = np.linalg.eigvalsh(rho_a)
eigs_b = np.linalg.eigvalsh(rho_b)
check("E1: exhibit pair valid: same U_eff(0), same local densities, "
      "different positive parts, both physical",
      np.abs(u_b0 - u0).max() < 1e-12
      and np.abs(rho_b[:3, :3] - p1p).max() < 1e-15
      and np.linalg.norm(q_a - q_b) > 0.01
      and eigs_a.min() > 0 and eigs_a.max() <= 1 + 1e-12
      and eigs_b.min() > 0 and eigs_b.max() <= 1 + 1e-12,
      f"|Q_A - Q_B|_F = {np.linalg.norm(q_a - q_b):.4f}")

TAU_E = 0.05
seps_by_lam = {}
for lam in (0.0, 0.3, 0.7, 0.95):
    ca, cb = rho_a.copy(), rho_b.copy()
    seps = []
    for _ in range(int(2.0 / TAU_E)):
        ca = edge_step(ca, lam, TAU_E, "IB")
        cb = edge_step(cb, lam, TAU_E, "IB")
        sa = np.linalg.svd(ca[:3, 3:], compute_uv=False)
        sb = np.linalg.svd(cb[:3, 3:], compute_uv=False)
        if sa[2] > 1e-10 and sb[2] > 1e-10:
            ua, _ = polar_uq(ca[:3, 3:])
            ub, _ = polar_uq(cb[:3, 3:])
            seps.append(np.linalg.norm(ua - ub))
    seps_by_lam[lam] = (max(seps), seps[-1])
    info(f"E exhibit separation lam={lam}",
         f"max_t |U_A - U_B|_F = {max(seps):.4f}, final = {seps[-1]:.4f}")

check("E2: lam=0 reproduces the block-01 non-autonomy (trajectories with "
      "identical U_eff(0)/local densities separate; >10x the record-dominated case)",
      seps_by_lam[0.0][0] > 0.2
      and seps_by_lam[0.0][0] > 10 * seps_by_lam[0.95][0],
      f"max sep = {seps_by_lam[0.0][0]:.3f} vs lam=0.95 max {seps_by_lam[0.95][0]:.3f}")
mono = (seps_by_lam[0.0][0] > seps_by_lam[0.3][0] > seps_by_lam[0.7][0]
        >= seps_by_lam[0.95][0])
check("E3: separation suppressed MONOTONICALLY with record strength",
      mono, " > ".join(f"{seps_by_lam[l][0]:.3f}" for l in (0.0, 0.3, 0.7, 0.95)))
check("E4: record-dominated regime: the two trajectories CONVERGE "
      "(hidden-Q channel damped; final sep < 5% of lam=0 max)",
      seps_by_lam[0.95][1] < 0.05 * seps_by_lam[0.0][0],
      f"final sep at lam=0.95 = {seps_by_lam[0.95][1]:.4f}")

c_ia = C6.copy()
c_ib = C6.copy()
for _ in range(800):
    c_ia = edge_step(c_ia, LAM_C, TAU, "IA")
    c_ib = edge_step(c_ib, LAM_C, TAU, "IB")
u_ia, _ = polar_uq(c_ia[:3, 3:])
u_ib, _ = polar_uq(c_ib[:3, 3:])
foot = np.linalg.norm(u_ia - u_ib)
check("E5: instrument footprint: the slaved links of I-A and I-B from the SAME "
      "initial state differ at order 1 (the admission is visible in the result)",
      foot > 0.3, f"|U_slaved(I-A) - U_slaved(I-B)|_F = {foot:.3f}")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
