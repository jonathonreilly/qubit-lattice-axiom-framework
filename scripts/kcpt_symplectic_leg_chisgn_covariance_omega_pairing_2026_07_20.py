#!/usr/bin/env python3
"""KCPT Unit 16 -- symplectic-leg chi_sgn-covariance of omega = -J_full under
H = <G_amb, S_eps>, and the omega-pairing census of the six CP-completed constituents.

Self-contained (no import of any other runner). Rebuilds from the bare L=4, N=64
staggered-lattice site construction the antisymmetric integer adjacency D2, the
corner-wave kernel frame V8/J64, the ambient-invariant total complex structure
J_full = J_ker + J_bulk = V8 J64 V8^T / 64^2 + Sum_{m in 1,2,3} D2 Q_m/(2 sqrt m),
the chiral parity S_eps = diag((-1)^{x1+x2+x3}), the order-768 ambient group G_amb,
its order-1536 extension H = <G_amb, S_eps> (G_amb index 2, disjoint coset
S_eps*G_amb), the five holomorphic G_amb-idempotents PW (ranks 4,4,6,6,12) and their
S_eps-images PHm in the anti-holomorphic plane H_-, and the split ZhalfW of the
CP-completed real-12 24-block into a 12^+ and a 12^-. It forms the SIX Unit-14
constituents C^64 = 8 (+) 8 (+) 12 (+) 12 (+) 12^+ (+) 12^-.

omega := -J_full is the symplectic leg of the Unit-10 Kahler triple (metric g = I,
J_full^T g = -J_full). This unit certifies:

  T1  chi_sgn-COVARIANCE of omega under H:  h^T omega h = chi_sgn(h) * omega for every
      h in H -- omega is PRESERVED on the 768 G_amb elements (+omega, the Unit-10 fact)
      and SIGN-REVERSED on the 768 S_eps-coset elements (-omega). The generator identity
      S_eps^T omega S_eps = -omega follows from Unit 9's S_eps J_full S_eps = -J_full
      with omega = -J_full and S_eps diagonal. The rebuilt floating matrices give
      bit-for-bit zero deviation on all 1536 elements after the group/coset coverage is gated;
      each check carries a live wrong-sign rejector 2*max|omega| = 0.748 exceeding
      max|omega| = 0.3739.                              [G-OMEGA-INV / COSET / SEPS]
  T2  omega-PAIRING census Omega_ij = Z_i^T omega Z_j (transpose, no conjugation) of the
      six constituents: the four induced blocks {8, 8, 12, 12} self-pair nondegenerately
      (ranks 8, 8, 12, 12); 12^+ and 12^- are each omega-ISOTROPIC; the cross
      12^+ <-> 12^- is nondegenerate rank 12; every other pair vanishes. Accounting
      40 + 2*12 = 64; the assembled Gram is antisymmetric and rank 64.        [G-PAIR-*]
      Selection rule (the Schur explanation, consistent with T1 + T2, NOT an independent
      claim): omega(V_i, V_j) != 0 <=> V_j ~= V_i^* (x) chi_sgn. The induced blocks are
      chi_sgn-invariant and self-pair; 12^- = 12^+ (x) chi_sgn forces the 12^+ self-block
      to zero and canonically pairs the chiral backbone 12^+ <-> 12^-.
  T3  SYMMETRIC-vs-ANTISYMMETRIC contrast on 12^+: the invariant SYMMETRIC form has
      all singular values equal to the structural target 1 (also consistent with the
      Unit-15 census), so 12^+ is nondegenerate
      under it, while the ANTISYMMETRIC omega self-block on the SAME 12^+ vanishes -- the
      isotropy is omega's antisymmetry twisted by chi_sgn (12^+ (x) chi_sgn = 12^- != 12^+),
      not a subspace degeneracy.                              [G-CONTRAST-SYMVSANTI]

ANTI-FABRICATION DISCIPLINE. J_full is rebuilt ONLY from the shell/kernel machinery and
omega = -J_full is taken directly from it, never a parity/sign proxy. The covariance
deviations are REAL max-abs entrywise norms of u^T omega u -/+ omega over the ACTUAL 768
G_amb and 768 coset elements, NEVER computed from a target; each covariance gate carries a
live wrong-sign rejector (a wrong-sign deviation is 2*max|omega| > max|omega|). The pairing
pattern is read from REAL SVD numeric ranks of Z_i^T omega Z_j and REAL Frobenius norms of
the blocks against a fixed floor -- a spurious pairing or a collapsed self-block FAILS. The
T3 contrast gates the symmetric-form singular spectrum directly against the structural
target 1 while the antisymmetric self-block VANISHES, so a
computation using the wrong (symmetric) form gets nondegeneracy everywhere and FAILS.
Every constituent is represented by a Hermitian-orthonormal basis of its complexification,
and every h in H is a real signed permutation; the bilinear blocks therefore use transpose,
not conjugate transpose. No irrational value is gated; the census is decided by rank / zero
STRUCTURE and explicit wrong-sign or wrong-value rejectors.
"""
import itertools
import os
import numpy as np

# Every note this runner reads, repo-relative: the two parents (Unit 14 six-constituent
# decomposition, Unit 10 symplectic leg) plus this unit's own note. Plain literal tuple,
# statically ast-parseable by the runner-cache input fingerprint, matching the Unit-14
# runner's declaration mechanism.
AUDIT_INPUT_PATHS = (
    "docs/KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md",              # U14
    "docs/KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md",  # U10
    "docs/KCPT_SYMPLECTIC_LEG_CHISGN_COVARIANCE_OMEGA_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-20.md",     # self-note
)

L, N = 4, 64
TOL0 = 1e-12      # exact rational-zero level
TOL_F = 1e-9      # [FLOAT] identity level
TOL_EIG = 1e-8    # eigen / rank / restriction selection
TOLREJ = 1e-6     # rejector / residual floor
TOL_COMM = 1e-6   # commutant singular-value null threshold

DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
U14_NOTE = "KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U13_NOTE = "KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U15_NOTE = "KCPT_EXTENDED_GROUP_REALITY_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md"
SELF_NOTE = "KCPT_SYMPLECTIC_LEG_CHISGN_COVARIANCE_OMEGA_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U9_NOTE = "KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U10_NOTE = "KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md"

# PRESERVE VERBATIM source-pin substrings (grepped from the on-disk parent notes):
PIN_U14 = "C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻"
PIN_U10_A = "J_full^T g = -J_full"
PIN_U10_B = "U^T omega U = omega"

PASS = FAIL = 0


def gate(tag, cond, desc):
    global PASS, FAIL
    ok = bool(cond)
    PASS, FAIL = PASS + (1 if ok else 0), FAIL + (0 if ok else 1)
    print(f"{'PASS' if ok else 'FAIL'} {tag} - {desc}")
    return ok


def note_text(basename):
    try:
        with open(os.path.join(DOCS, basename), encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def nrm(X):
    return float(np.max(np.abs(X)))


def eqm(a, b):
    return np.array_equal(a, b)


# ---------------- construction (self-contained; verbatim Unit-14 backbone) --------------
def idx(a, b, c):
    return (a * L + b) * L + c


coords = np.zeros((N, 3), dtype=np.int64)
for a in range(L):
    for b in range(L):
        for c in range(L):
            coords[idx(a, b, c)] = (a, b, c)


def eta_mu(mu, x):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** int(x[0])
    return (-1) ** int(x[0] + x[1])


e = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
D2 = np.zeros((N, N), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for mu in range(3):
        D2[i, idx(*((x + e[mu]) % L))] += eta_mu(mu, x)
        D2[i, idx(*((x - e[mu]) % L))] -= eta_mu(mu, x)

SUBSETS = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
sidx = {frozenset(S): k for k, S in enumerate(SUBSETS)}
V8 = np.zeros((N, 8), dtype=np.int64)
for i in range(N):
    x = coords[i]
    for k, S in enumerate(SUBSETS):
        V8[i, k] = (-1) ** int(sum(x[j] for j in S))


def sgn_subset(S):
    Sset = frozenset(S)
    return ((-1) ** len(Sset & frozenset({0, 2}))) * (1 if 1 in Sset else -1)


J64 = np.zeros((8, 8), dtype=np.int64)
for k, S in enumerate(SUBSETS):
    T = frozenset(S) ^ frozenset({1})
    J64[sidx[T], k] = 64 * sgn_subset(S)
Jker_int = V8 @ J64 @ V8.T                       # == 64^2 * J_ker

M = D2 @ D2
lam = [0, -4, -8, -12]
Fac = [M - lam[m] * np.eye(N, dtype=np.int64) for m in range(4)]
Q = []
for m in range(4):
    P = np.eye(N, dtype=np.int64)
    for mp in range(4):
        if mp != m:
            P = P @ Fac[mp]
    Q.append(P)
Nm = []
for m in range(4):
    v = 1
    for mp in range(4):
        if mp != m:
            v *= (lam[m] - lam[mp])
    Nm.append(v)                                 # (384, -128, 128, -384)

# total complex structure from the shell/kernel machinery (NO parity/sign proxy)
D2f = D2.astype(float)
Pf = [Q[m].astype(float) / Nm[m] for m in range(4)]
Jkerf = Jker_int.astype(float) / (64.0 ** 2)
Jbulk = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3))
Jfull = Jkerf + Jbulk

# chiral parity S_eps (the Unit-9 involution); integer form for exact identities
eps = np.array([(-1) ** int(coords[i][0] + coords[i][1] + coords[i][2]) for i in range(N)], dtype=np.int64)
Seps_int = np.diag(eps)
Seps = Seps_int.astype(float)
I64i = np.eye(N, dtype=np.int64)


# ---------------- G_amb reconstruction (dressed-symmetry scan + closure) ----------------
def perm(fmap):
    P = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        y = np.array(fmap(coords[i])) % L
        P[i, idx(int(y[0]), int(y[1]), int(y[2]))] = 1
    return P


UR = perm(lambda x: (x[1], x[2], x[0]))
U2m = perm(lambda x: (-x[1], -x[0], -x[2]))
STAB = np.eye(N, dtype=np.int64)
TR = {t: perm(lambda x, t=t: (x[0] - t[0], x[1] - t[1], x[2] - t[2]))
      for t in itertools.product(range(L), repeat=3)}


def signfield(bits):
    a1, a2, a3, b12, b13, b23 = bits
    d = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x1, x2, x3 = coords[i]
        expo = a1 * x1 + a2 * x2 + a3 * x3 + b12 * x1 * x2 + b13 * x1 * x3 + b23 * x2 * x3
        d[i] = (-1) ** int(expo)
    return d


ALLBITS = list(itertools.product([0, 1], repeat=6))
SF = {bits: signfield(bits) for bits in ALLBITS}
BASES = {"stab": STAB, "U2": U2m, "UR": UR}


def closure_grp(gs):
    gs = [g0.copy() for g0 in gs]
    elts = {g0.tobytes(): g0 for g0 in gs}
    frontier = list(elts.values())
    while frontier:
        nf = []
        for xg in frontier:
            for g0 in gs:
                p = xg @ g0
                key = p.tobytes()
                if key not in elts:
                    elts[key] = p
                    nf.append(p)
        frontier = nf
    return list(elts.values())


commuting = []
for name, base in BASES.items():
    for bits in ALLBITS:
        dd = np.diag(SF[bits])
        for t in itertools.product(range(L), repeat=3):
            U = dd @ base @ TR[t]
            if eqm(U @ D2, D2 @ U):
                commuting.append(U.copy())
Gamb = closure_grp(commuting)

# small deterministic greedy generating set of G_amb (commutant of a generating set ==
# commutant of the group); closure certified == 768, so kron stacks use these, not 768.
Gsorted = sorted(Gamb, key=lambda U: U.tobytes())
gens_G = []
seenG = {I64i.tobytes()}
gen_closure_G = 0
for U in Gsorted:
    if eqm(U, I64i) or U.tobytes() in seenG:
        continue
    gens_G.append(U)
    cl = closure_grp(gens_G)
    seenG = {x.tobytes() for x in cl}
    gen_closure_G = len(cl)
    if gen_closure_G == 768:
        break

# ---------------- extend by S_eps: H = <G_amb, S_eps>, order 1536 -----------------------
gens_H = gens_G + [Seps_int]
coset = [Seps_int @ g for g in Gamb]             # the nontrivial coset S_eps * G_amb
Gamb_keys = {g.tobytes() for g in Gamb}
coset_keys = {c.tobytes() for c in coset}
gamb_complete = len(Gamb) == 768 and len(Gamb_keys) == 768
extension_complete = (
    gamb_complete
    and len(coset) == 768
    and len(coset_keys) == 768
    and Gamb_keys.isdisjoint(coset_keys)
    and all((Seps_int @ g @ Seps_int).tobytes() in Gamb_keys for g in Gamb)
)

# ---------------- holomorphic / anti-holomorphic frames --------------------------------
evals, evecs = np.linalg.eig(Jfull)
selp = np.where(np.abs(evals - 1j) < TOL_EIG)[0]
selm = np.where(np.abs(evals + 1j) < TOL_EIG)[0]
Bh, _ = np.linalg.qr(evecs[:, selp])       # holo W, 64 x 32
Bm, _ = np.linalg.qr(evecs[:, selm])       # anti-holo H_-, 64 x 32
PiW = Bh @ Bh.conj().T
PiHm = Bm @ Bm.conj().T


# ---------------- commutant helpers (memory-safe: kron stacks over GENERATORS only) -----
def commutant_dim(mats, r):
    Ir = np.eye(r, dtype=complex)
    A = np.vstack([np.kron(m.T, Ir) - np.kron(Ir, m) for m in mats])
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < TOL_COMM))


def commutant_basis(mats, r, d):
    Ir = np.eye(r, dtype=complex)
    A = np.vstack([np.kron(m.T, Ir) - np.kron(Ir, m) for m in mats])
    Uc, s, Vh = np.linalg.svd(A, full_matrices=False)   # full_matrices=False: no huge U -> OOM-safe
    del Uc, A
    return [np.conj(Vh[-(i + 1)]).reshape(r, r, order="F") for i in range(d)]


def split_block(Z, basis_mats, r, d):
    """Split the r-dim block with orthobasis columns Z (64 x r) into d H-irreps via a
    GENERIC self-adjoint commutant element.  A seed is accepted ONLY on clean d-cluster
    eigenvalue separation (inter-cluster gap > 1e6 * intra), NEVER by any target rank.
    Returns (sub-bases in 64-space, per-cluster ranks, seed) or (None, None, -1)."""
    for seed in range(128):
        rng = np.random.default_rng(seed)
        cc = rng.standard_normal(len(basis_mats)) + 1j * rng.standard_normal(len(basis_mats))
        Y = sum(cc[i] * basis_mats[i] for i in range(len(basis_mats)))
        Hs = Y + Y.conj().T
        ww, VV = np.linalg.eigh(Hs)
        spread = float(ww[-1] - ww[0])
        if spread <= 0:
            continue
        thr = 1e-4 * spread
        grp = [[0]]
        for j in range(1, r):
            if ww[j] - ww[j - 1] > thr:
                grp.append([j])
            else:
                grp[-1].append(j)
        intra = max((ww[g[-1]] - ww[g[0]]) for g in grp)
        inter = min((ww[grp[t + 1][0]] - ww[grp[t][-1]]) for t in range(len(grp) - 1)) \
            if len(grp) > 1 else 0.0
        if len(grp) == d and inter > 1e6 * max(intra, 1e-18):
            return [Z @ VV[:, g] for g in grp], [len(g) for g in grp], seed
    return None, None, -1


# ---------------- 5 holomorphic G_amb-idempotents on W (Unit-12 census) -----------------
Cgens = [Bh.conj().T @ g.astype(complex) @ Bh for g in gens_G]   # 32x32 restrictions
dimcW = commutant_dim(Cgens, 32)                                  # expect 5
BsW = commutant_basis(Cgens, 32, dimcW)
subZW, ranksW, seedW = split_block(Bh, BsW, 32, dimcW)
if subZW is not None:
    order = list(np.argsort(ranksW))
    subZW = [subZW[i] for i in order]
    ranksW = [ranksW[i] for i in order]
    PW = [z @ z.conj().T for z in subZW]                          # 64x64, in W; ranks 4,4,6,6,12
    PHm = [Seps.astype(complex) @ p @ Seps.astype(complex) for p in PW]   # S_eps-images in H_-
else:
    PW = PHm = []

# ============ split the reducible rank-12 CP-completed 24-block into 12^+ / 12^- ========
gensHc = [g.astype(complex) for g in gens_H]
k12 = int(np.argmax(ranksW)) if ranksW else 0    # the rank-12 W-block (ranksW sorted -> idx 4)
block12 = PW[k12] + PHm[k12]
r24 = int(round(np.trace(block12).real))         # 24
_w24, V24 = np.linalg.eigh((block12 + block12.conj().T) / 2.0)
Z24 = V24[:, -r24:]                              # 64 x 24 orthobasis of the CP-completed block
matsH24 = [Z24.conj().T @ g @ Z24 for g in gensHc]
dH24 = commutant_dim(matsH24, r24)               # expect 2 (two inequivalent H-irreps)
if dH24 == 2:
    BsB24 = commutant_basis(matsH24, r24, dH24)
    subZ24, subr24, _seed24 = split_block(Z24, BsB24, r24, dH24)
else:
    subZ24, subr24 = None, None
if subZ24 is not None:
    ordb = list(np.argsort(subr24))
    ZhalfW = [subZ24[i] for i in ordb]           # two 64 x 12 half-bases (12^+, 12^-)
else:
    ZhalfW = [np.zeros((N, 12), dtype=complex), np.zeros((N, 12), dtype=complex)]

# ==================== SIX Unit-14 constituents + the symmetric-form contrast anchor =====
# four CP-doubled blocks (8,8,12,12) + the two halves of the split real 12 (12^+, 12^-)
P6 = [PW[0] + PHm[0], PW[1] + PHm[1], PW[2] + PHm[2], PW[3] + PHm[3],
      ZhalfW[0] @ ZhalfW[0].conj().T,
      ZhalfW[1] @ ZhalfW[1].conj().T]
ranks6 = [int(np.linalg.matrix_rank(P, tol=TOL_EIG)) for P in P6]

# ==================================== gates

print("\n=== Unit 16: symplectic-leg chi_sgn-covariance of omega=-J_full + omega-pairing census ===")

# omega = -J_full : the Unit-10 symplectic leg (matrix form J_full^T g = -J_full, disclosed metric g = I).
omega = -Jfull
maxabs_w = float(np.max(np.abs(omega)))     # rejector threshold: a wrong-sign deviation must exceed one max entry
FZ = 1e-7                                    # "is zero" on a Frobenius norm (omega entries are O(1))


def numrank(M, rel=1e-8):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    if s.size == 0 or float(s[0]) < 1e-12:
        return 0
    return int(np.sum(s > rel * s[0]))


def orthobasis(P):
    _w, V = np.linalg.eigh((P + P.conj().T) / 2.0)
    r = int(round(np.trace(P).real))
    return V[:, -r:]


def cov_dev(u, sign):
    """||u^T omega u - sign*omega|| ; nrm is max-abs entrywise so correct-sign dev is exactly 0."""
    uf = u.astype(float)
    return nrm(uf.T @ omega @ uf - sign * omega)


Z6 = [orthobasis(P) for P in P6]
labels6 = ["8_a", "8_b", "12_a", "12_b", "12+", "12-"]
decomp_sum = nrm(sum(P6) - np.eye(N))
decomp_herm = max(nrm(P - P.conj().T) for P in P6)
decomp_idem = max(nrm(P @ P - P) for P in P6)
decomp_orth = max(
    nrm(P6[i] @ P6[j])
    for i in range(len(P6))
    for j in range(len(P6))
    if i != j
)
decomp_hinv = max(nrm(g @ P - P @ g) for g in gensHc for P in P6)

# ---- inherited-construction sanity (build on a verified base, not a fabricated one) ----
gate("G-CONSTRUCT-J2", nrm(Jfull @ Jfull + np.eye(N)) < TOL_F,
     "inherited J_full^2 = -I (Unit 8 total complex structure)")
gate("G-DECOMP-COMPLETE",
     decomp_sum < TOL_F and decomp_herm < TOL_F and decomp_idem < TOL_F
     and decomp_orth < TOL_F and decomp_hinv < TOL_F,
     f"six Unit-14 constituent projectors are Hermitian/idempotent/orthogonal/H-invariant "
     f"and resolve I_64 (residuals {decomp_herm:.1e}/{decomp_idem:.1e}/"
     f"{decomp_orth:.1e}/{decomp_hinv:.1e}/{decomp_sum:.1e})")
gate("G-DECOMP-RANKS", ranks6 == [8, 8, 12, 12, 12, 12],
     f"constituent ranks {ranks6} == [8, 8, 12, 12, 12, 12]")

# ---- T1: omega is antisymmetric & nondegenerate ----
gate("G-OMEGA-DEF", nrm(omega + omega.T) < TOL_F and numrank(omega) == 64,
     f"omega = -J_full antisymmetric (||w+w^T|| = {nrm(omega + omega.T):.1e}) and full rank {numrank(omega)} == 64")

# ---- T1: chi_sgn = +1 on all 768 G_amb (invariant); wrong-sign rejector live ----
inv_max = max(cov_dev(g, +1) for g in Gamb)
inv_wrong = max(cov_dev(g, -1) for g in Gamb)
gate("G-OMEGA-INV", gamb_complete and inv_max < TOL_F and inv_wrong > maxabs_w,
     f"|G_amb|={len(Gamb_keys)}==768 and g^T w g = +w on every element (max dev {inv_max:.1e}); "
     f"wrong-sign rejector {inv_wrong:.3f} > max|w| {maxabs_w:.3f}")

# ---- T1: chi_sgn = -1 on all 768 S_eps-coset (negated); wrong-sign rejector live ----
cos_neg = max(cov_dev(c, -1) for c in coset)
cos_wrong = max(cov_dev(c, +1) for c in coset)
gate("G-OMEGA-COSET", extension_complete and cos_neg < TOL_F and cos_wrong > maxabs_w,
     f"768-element disjoint normalized S_eps-coset gives |H|={len(Gamb_keys | coset_keys)}==1536 "
     f"and c^T w c = -w on every coset element (max dev {cos_neg:.1e}); "
     f"wrong-sign rejector {cos_wrong:.3f} > max|w| {maxabs_w:.3f}")

# ---- T1: S_eps carries the negation (the Unit-9 covariance input S_eps J_full S_eps = -J_full, in omega form) ----
seps_neg = cov_dev(Seps_int, -1)
seps_pos = cov_dev(Seps_int, +1)
gate("G-OMEGA-SEPS", seps_neg < TOL_F and seps_pos > maxabs_w,
     f"S_eps^T w S_eps = -w (dev {seps_neg:.1e}); wrong-sign rejector {seps_pos:.3f} > max|w| {maxabs_w:.3f}")

# ---- T2: build the pairwise bilinear omega-blocks Omega_ij = Z_i^T omega Z_j (transpose, no conjugation) ----
n6 = len(P6)
frob = [[float(np.linalg.norm(Z6[i].T @ omega @ Z6[j])) for j in range(n6)] for i in range(n6)]
rk = [[numrank(Z6[i].T @ omega @ Z6[j]) for j in range(n6)] for i in range(n6)]
r6 = [Z6[i].shape[1] for i in range(n6)]

# ---- T2: four induced self-blocks nondegenerate (ranks 8, 8, 12, 12) ----
gate("G-PAIR-INDUCED", all(frob[i][i] > FZ and rk[i][i] == r6[i] for i in range(4)),
     f"induced self-blocks nondegenerate, ranks {[rk[i][i] for i in range(4)]} == {[r6[i] for i in range(4)]}")

# ---- T2: 12+ and 12- each individually omega-isotropic ----
gate("G-PAIR-ISOTROPIC", frob[4][4] < FZ and frob[5][5] < FZ,
     f"omega vanishes within 12+ (||{frob[4][4]:.1e}||) and within 12- (||{frob[5][5]:.1e}||)")

# ---- T2: canonical chiral cross-pairing 12+ <-> 12- full rank 12 ----
gate("G-PAIR-CROSS", frob[4][5] > FZ and rk[4][5] == 12 and rk[5][4] == 12,
     f"12+ <-> 12- cross-pairing nondegenerate, rank {rk[4][5]} == 12")

# ---- T2: every other pair vanishes ----
allowed = {(4, 5), (5, 4)} | {(i, i) for i in range(4)}
offmax = max(frob[i][j] for i in range(n6) for j in range(n6) if (i, j) not in allowed)
gate("G-PAIR-OFFDIAG", offmax < FZ,
     f"all remaining pairs vanish (max off-block ||{offmax:.1e}||)")

# ---- T2: assembled omega nondegenerate on all C^64, antisymmetric, rank 64 ----
Zc = np.concatenate(Z6, axis=1)
unit = nrm(Zc.conj().T @ Zc - np.eye(N))
Gform = Zc.T @ omega @ Zc
grank = numrank(Gform)
self_ranks = sum(rk[i][i] for i in range(4))
total_form_rank = self_ranks + 2 * rk[4][5]
gate("G-PAIR-RANK",
     unit < TOL_EIG and nrm(Gform + Gform.T) < TOL_F and grank == 64 and total_form_rank == 64,
     f"assembled G antisymmetric, rank {grank} == 64; accounting {self_ranks} + 2*{rk[4][5]} = {total_form_rank} == 64")

# ---- anti-fabrication spine: on 12+ ALONE, the SYMMETRIC form is nondegenerate but omega is isotropic ----
# same basis Z6[4]: symmetric u^T v has unit singular spectrum while the
# antisymmetric u^T omega v vanishes. Proves the isotropy is omega's antisymmetry x chi_sgn
# (12+ (x) chi_sgn = 12- != 12+), NOT a subspace degeneracy. A fabricator using the wrong (symmetric)
# form gets nondegenerate everywhere and FAILS this contrast.
sym4_svals = np.linalg.svd(Z6[4].T @ Z6[4], compute_uv=False)
sym4_unit_dev = float(np.max(np.abs(sym4_svals - 1.0)))
asym4 = frob[4][4]
gate("G-CONTRAST-SYMVSANTI",
     sym4_unit_dev < TOL0 and asym4 < FZ,
     f"12+: all 12 symmetric-form singular values equal 1 (max dev {sym4_unit_dev:.1e}); "
     f"omega self ||{asym4:.1e}|| isotropic")

# ---- source-pin gates ----
gate("G-PIN-U14", PIN_U14 in note_text(U14_NOTE),
     f"Unit-14 six-constituent pin present in {U14_NOTE}")
gate("G-PIN-U10",
     PIN_U10_A in note_text(U10_NOTE) and PIN_U10_B in note_text(U10_NOTE),
     f"Unit-10 symplectic-leg pins present: {PIN_U10_A!r} and {PIN_U10_B!r}")

# ---- link discipline: exactly two dependency edges (Unit 14 + Unit 10); U9/U13/U15 backticked only ----
s = note_text(SELF_NOTE)
ckcpt = s.count("](KCPT_")
c14 = s.count(f"]({U14_NOTE})")
c10 = s.count(f"]({U10_NOTE})")
c9 = s.count(f"]({U9_NOTE})")
c13 = s.count(f"]({U13_NOTE})")
c15 = s.count(f"]({U15_NOTE})")
gate("G-PIN-SELF",
     ckcpt == 2 and c14 == 1 and c10 == 1 and c9 == 0 and c13 == 0 and c15 == 0,
     f"self-note dep edges: total {ckcpt}==2, U14 {c14}==1, U10 {c10}==1, U9/U13/U15 = {c9}/{c13}/{c15}==0")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
