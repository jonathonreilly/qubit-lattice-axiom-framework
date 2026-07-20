#!/usr/bin/env python3
"""KCPT Unit 12 exact holomorphic G_amb-representation runner.

Rebuilds the landed Unit-8 total complex structure J_full and the order-768
ambient group G_amb on the L=4, N=64 staggered lattice, forms the holomorphic
32-plane W = ker(J_full - i I) (the +i eigenspace), and proves that G_amb acts
COMPLEX-LINEARLY on W as a 32-dimensional complex representation that is
multiplicity-free and decomposes as 32 = 4 (+) 4 (+) 6 (+) 6 (+) 12.

  T1  every U in G_amb commutes with J_full, so U|_W is complex-linear; the
      restriction is non-trivial (rotations act as non-identity unitaries).
                                                             [G1..G7]
  T2  End_G(W) has complex dimension 5, is commutative and unital, so the rep is
      multiplicity-free (5 pairwise-inequivalent irreducibles, each once).
                                                             [G11,G12,G13,G14,G17]
  T3  the 5 central idempotents have holo-ranks {4,4,6,6,12}, an internal direct
      sum 32 = 4+4+6+6+12.                                   [G15,G16]
  T4  the exact-integer bridge S0 = 12*768, SJ = 8*768, (12+8)/4 = 5 ties the
      count to the Unit-10 census (12) and a new J-twisted class-sum (8).
                                                             [G8,G9,G10]

ANTI-FABRICATION DISCIPLINE.  J_full is built ONLY from the shell/kernel
machinery (V8*J64*V8^T / 64^2 plus Sum_m D2*P_m/(2*sqrt m)); G3 proves a rational
sqrt(m)->1 proxy is NOT a complex structure, so no parity/sign proxy can stand in
for it.  The two load-bearing class-sums S0 = Sum (tr U)^2 and SJ = Sum (tr(U*J))^2
are accumulated as per-element trace SCALARS in a loop over all 768 elements --
never a materialized 768-block matrix -- and no individual (irrational) character
tr(U*J_full) is ever gated.  The commutant is computed from a SMALL generating set
(verified closure == 768), a ~4096x1024 map, so the OOM-prone 786432x1024 full
build is avoided; the character-norm (S0+SJ)/(4*768) confirms the same 5 from a
scalar loop (G14).  Every completeness/identity gate carries a discriminating
wrong-value rejector; float eig/rank/SVD/spectrum checks are tagged redundant.
"""
import itertools
import os
import numpy as np

L, N = 4, 64
TOL0 = 1e-12      # exact rational-zero level
TOL_EIG = 1e-8    # eigen / rank / restriction
TOLREJ = 1e-6     # rejector floor

DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
U8_NOTE = "KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U10_NOTE = "KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md"
SELF_NOTE = "KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md"

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


# ---------------- construction (self-contained; mirrors the landed Unit-10/11 runner) ----
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
Pf = [Q[m].astype(float) / Nm[m] for m in range(4)]          # true shell projectors
Jkerf = Jker_int.astype(float) / (64.0 ** 2)
Jbulk = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3))
Jfull = Jkerf + Jbulk

# rational sqrt(m)->1 proxy, used ONLY as a discriminating counter-object in G3
Jbulk_proxy = sum(D2f @ Pf[m] / 2.0 for m in (1, 2, 3))
Jfull_proxy = Jkerf + Jbulk_proxy

# chiral parity S_eps (NOT in G_amb): used only as a non-vacuity witness in G7
eps = np.array([(-1) ** int(coords[i][0] + coords[i][1] + coords[i][2]) for i in range(N)], dtype=np.int64)
Seps = np.diag(eps).astype(float)


# ---------------- G_amb reconstruction (mirror the landed runner) --------------------
def perm(fmap):
    P = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        y = np.array(fmap(coords[i])) % L
        P[i, idx(int(y[0]), int(y[1]), int(y[2]))] = 1
    return P


UR = perm(lambda x: (x[1], x[2], x[0]))
U2 = perm(lambda x: (-x[1], -x[0], -x[2]))
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
BASES = {"stab": STAB, "U2": U2, "UR": UR}


def eqm(a, b):
    return np.array_equal(a, b)


def closure_amb(gs):
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
Gamb = closure_amb(commuting)

# minimal generating set (deterministic greedy; closure verified == 768 in G11)
Gsorted = sorted(Gamb, key=lambda U: U.tobytes())
I64 = np.eye(N, dtype=np.int64)
gens = []
gen_closure = 0
seen = set()
for U in Gsorted:
    if eqm(U, I64) or U.tobytes() in seen:
        continue
    gens.append(U)
    cl = closure_amb(gens)
    seen = set(x.tobytes() for x in cl)
    gen_closure = len(cl)
    if gen_closure == 768:
        break

# =========================================================================== gates ===
# ---- T1: J_full is a genuine complex structure and G_amb acts complex-linearly on W --
gate("G1", nrm(Jfull @ Jfull + np.eye(N)) < TOL0,
     "J_full^2 = -I_64: ||J_full^2 + I|| < 1e-12 (genuine complex structure)")

gate("G2", nrm(Jfull + Jfull.T) < TOL0 and nrm(Jfull) > TOLREJ,
     "J_full antisymmetric and nonzero: ||J+J^T|| < 1e-12 and ||J|| > 1e-6")

# INDEPENDENT-BUILD / NO-PARITY-PROXY rejector: the rational sqrt(m)->1 proxy fails J^2=-I
gate("G3", nrm(Jfull_proxy @ Jfull_proxy + np.eye(N)) > TOLREJ and nrm(Jfull - Jfull_proxy) > TOLREJ,
     "REJECTOR: sqrt(m)->1 rational proxy is NOT a complex structure and differs from J_full "
     "(the sqrt(m) shell normalizers are load-bearing; J_full is not a sign proxy)")

evals, evecs = np.linalg.eig(Jfull)
selp = np.where(np.abs(evals - 1j) < TOL_EIG)[0]
selm = np.where(np.abs(evals + 1j) < TOL_EIG)[0]
gate("G4", len(selp) == 32 and len(selm) == 32 and len(selp) + len(selm) == 64,
     f"[FLOAT SANITY] +i eigenspace dim {len(selp)}==32, -i dim {len(selm)}==32, sum==64")

gate("G5", len(Gamb) == 768,
     f"|G_amb| = {len(Gamb)} == 768")

maxD2 = max(int(np.max(np.abs(U @ D2 - D2 @ U))) for U in Gamb)
TR100 = perm(lambda x: (x[0] - 1, x[1], x[2]))          # innocent permutation, breaks staggering
witnessD2 = int(np.max(np.abs(TR100 @ D2 - D2 @ TR100)))
gate("G6", maxD2 == 0 and witnessD2 > 0,
     f"every U commutes with D2 (max int dev {maxD2}==0) AND witness TR[(1,0,0)] does NOT "
     f"(dev {witnessD2}>0): the D2-commutation constraint is non-vacuous")

maxJ = max(nrm(U.astype(float) @ Jfull - Jfull @ U.astype(float)) for U in Gamb)
witnessJ = nrm(Seps @ Jfull - Jfull @ Seps)             # S_eps anticommutes with J_full
gate("G7", maxJ < TOL_EIG and witnessJ > TOLREJ,
     f"COMPLEX-LINEAR ACTION: every U commutes with J_full (max dev {maxJ:.1e}) AND witness "
     f"S_eps (not in G_amb) does NOT (dev {witnessJ:.3f}>1e-6): commutation is a genuine constraint")

# ---- T4: the two exact-integer class-sums and the bridge (per-element scalar loop) ---
S0 = 0
SJ = 0.0
for U in Gamb:
    a = int(round(np.trace(U)))                         # integer signed-perm character
    b = float(np.sum(U * Jfull.T))                      # tr(U*J_full) (irrational, never gated alone)
    S0 += a * a
    SJ += b * b
gate("G8", S0 == 12 * 768 and S0 != 11 * 768,
     f"S0 = Sum (tr U)^2 = {S0} == 12*768 (=9216) and != 11*768 (=8448)  [EXACT INTEGER]")
gate("G9", round(SJ) == 8 * 768 and abs(SJ - 8 * 768) < TOLREJ and round(SJ) != 9 * 768,
     f"SJ = Sum (tr(U*J_full))^2 = {SJ:.6f}, round == 8*768 (=6144), |SJ-6144| < 1e-6, "
     f"round != 9*768 (=6912)  [integer by group symmetry; per-term irrational]")
bridge = (S0 / 768 + round(SJ) / 768) / 4
gate("G10", abs(bridge - 5) < TOL0 and abs(bridge - 4) > 0.5 and abs(bridge - 6) > 0.5,
     f"BRIDGE (S0/768 + SJ/768)/4 = {bridge} == 5 and != 4 and != 6")

# ---- T2: the holomorphic representation and its commutant ----------------------------
# unitary frame B of the +i eigenspace W (complex dim 32)
B, _ = np.linalg.qr(evecs[:, selp])
gate("G11", gen_closure == 768 and nrm(B.conj().T @ B - np.eye(B.shape[1])) < TOL_EIG,
     f"generating set of {len(gens)} elements closes to {gen_closure}==768; W-frame B is "
     f"orthonormal (dim {B.shape[1]}==32)")

# restrict the generators to W; check W is a genuine invariant subspace + non-trivial action
Cs = []
maxrest = 0.0
maxdev_id = 0.0
for U in gens:
    Uc = U.astype(complex)
    C = B.conj().T @ Uc @ B
    maxrest = max(maxrest, nrm(Uc @ B - B @ C))
    maxdev_id = max(maxdev_id, nrm(C - np.eye(32)))
    Cs.append(C)
# G11b folded: invariance + non-triviality reported through G12's construction below

# commutant of the generating set: null space of the stacked commutator map (memory-safe)
n = 32
I32 = np.eye(n, dtype=complex)
Astack = np.vstack([np.kron(C.T, I32) - np.kron(I32, C) for C in Cs])   # ~ (k*1024) x 1024
sv = np.sort(np.linalg.svd(Astack, compute_uv=False))
tol_sv = 1e-6
dimc = int(np.sum(sv < tol_sv))
gap = sv[dimc] / max(sv[dimc - 1], 1e-16) if 0 < dimc < len(sv) else 0.0
gate("G12", maxrest < TOL_EIG and maxdev_id > TOLREJ and dimc == 5 and gap > 1e6
     and dimc != 12 and dimc != 4 and dimc != 6,
     f"W is invariant (max||UB-BC|| {maxrest:.1e}) with non-trivial action (max||C-I|| "
     f"{maxdev_id:.3f}); generator-commutant dim {dimc}==5 (clean sv-gap {gap:.1e}), != 12,4,6")

# reconstruct a commutant basis and check commutativity + unitality
_, _, Vh = np.linalg.svd(Astack, full_matrices=True)
Bs = [np.conj(Vh[-(i + 1)]).reshape(n, n, order="F") for i in range(dimc)]
maxcommgen = max(nrm(Bi @ C - C @ Bi) for Bi in Bs for C in Cs)
maxcomm = max((nrm(Bs[i] @ Bs[j] - Bs[j] @ Bs[i]) for i in range(dimc) for j in range(dimc)), default=1.0)
# unitality: I_32 lies in the span of the commutant basis (least squares residual)
Amat = np.column_stack([Bi.reshape(-1, order="F") for Bi in Bs])
coef, *_ = np.linalg.lstsq(Amat, I32.reshape(-1, order="F"), rcond=None)
res_id = nrm(Amat @ coef - I32.reshape(-1, order="F"))
gate("G13", maxcommgen < TOL_EIG and maxcomm < TOL_EIG and res_id < TOL_EIG,
     f"commutant basis commutes with generators ({maxcommgen:.1e}), is COMMUTATIVE "
     f"({maxcomm:.1e}), and is UNITAL (I_32 in span, residual {res_id:.1e}) => C^5 algebra")

# MEMORY-BUDGET cross-check: character-norm full-group commutant, scalar loop, == generator dim
char_norm = (S0 + SJ) / (4.0 * 768)
gate("G14", abs(char_norm - 5) < TOLREJ and abs(char_norm - dimc) < TOLREJ,
     f"MEMORY-BUDGET: char-norm (S0+SJ)/(4*768) = {char_norm:.6f} == 5 == generator-commutant "
     f"dim {dimc} (scalar loop, no 768-block matrix materialized)")

# ---- T3: the multiplicity-free block dimensions {4,4,6,6,12} -------------------------
# generic self-adjoint commutant element; SELECT ONLY on numerical separation quality
mult = None
Wproj = None
chosen_seed = -1
for seed in range(64):
    rng = np.random.default_rng(seed)
    c = rng.standard_normal(dimc) + 1j * rng.standard_normal(dimc)
    Y = sum(c[i] * Bs[i] for i in range(dimc))
    H = Y + Y.conj().T
    w, Vv = np.linalg.eigh(H)
    spread_tot = float(w[-1] - w[0])
    if spread_tot <= 0:
        continue
    thr = 1e-4 * spread_tot
    groups = [[0]]
    for j in range(1, n):
        if w[j] - w[j - 1] > thr:
            groups.append([j])
        else:
            groups[-1].append(j)
    intra = max((w[g[-1]] - w[g[0]]) for g in groups)
    inter = min((w[groups[t + 1][0]] - w[groups[t][-1]]) for t in range(len(groups) - 1)) \
        if len(groups) > 1 else 0.0
    # accept purely on unambiguous separation, NOT on the multiplicities themselves
    if len(groups) >= 2 and inter > 1e6 * max(intra, 1e-18):
        mult = sorted(len(g) for g in groups)
        Wproj = [Vv[:, g] for g in groups]
        chosen_seed = seed
        break

gate("G15", mult is not None and mult == [4, 4, 6, 6, 12] and sum(mult) == 32
     and mult != [4, 4, 4, 8, 12] and mult != [2, 6, 6, 6, 12],
     f"HOLO-RANKS (generic self-adjoint commutant element, seed {chosen_seed} chosen by "
     f"separation only): sorted multiplicities {mult} == [4,4,6,6,12], sum 32, != [4,4,4,8,12], != [2,6,6,6,12]")

# the five eigenspaces are genuine orthogonal idempotents summing to I_32
idem_ok = False
if Wproj is not None:
    Projs = [Wj @ Wj.conj().T for Wj in Wproj]
    sum_I = nrm(sum(Projs) - np.eye(n))
    idem = max(nrm(Pk @ Pk - Pk) for Pk in Projs)
    orth = max((nrm(Projs[i] @ Projs[j]) for i in range(len(Projs)) for j in range(len(Projs)) if i != j),
               default=1.0)
    ranks = sorted(int(round(np.trace(Pk).real)) for Pk in Projs)
    idem_ok = sum_I < TOL_EIG and idem < TOL_EIG and orth < TOL_EIG and ranks == [4, 4, 6, 6, 12]
gate("G16", idem_ok,
     "the 5 eigenspaces are orthogonal idempotents: Sum P_k = I_32, P_k^2 = P_k, P_j P_k = 0, "
     "ranks {4,4,6,6,12} => genuine direct sum 32 = 4+4+6+6+12")

# ---- multiplicity-free logical closure: Sum m_i^2 == number of blocks ----------------
num_blocks = len(mult) if mult is not None else -1
gate("G17", num_blocks == 5 and abs(char_norm - 5) < TOLREJ,
     f"MULTIPLICITY-FREE: #distinct blocks {num_blocks}==5 equals Sum m_i^2 = "
     f"(S0+SJ)/(4*768) = {char_norm:.3f}==5, forcing every multiplicity = 1")

# ---- source pins and self-note dependency discipline ---------------------------------
u8 = note_text(U8_NOTE)
gate("G18", "J_full^2 = -I_64" in u8,
     "SOURCE PIN Unit 8: total-complex-structure note contains 'J_full^2 = -I_64'")
u10 = note_text(U10_NOTE)
gate("G19", "mean(chi^2) = 12 = 7 + 5" in u10,
     "SOURCE PIN Unit 10: Kaehler-triple note contains 'mean(chi^2) = 12 = 7 + 5'")
s = note_text(SELF_NOTE)
c8 = s.count("](" + U8_NOTE)
c10 = s.count("](" + U10_NOTE)
ckcpt = s.count("](KCPT_")
gate("G20", c8 == 1 and c10 == 1 and ckcpt == 2,
     f"SELF-NOTE DEPENDENCY DISCIPLINE: Unit8-link {c8}==1, Unit10-link {c10}==1, "
     f"total KCPT-links {ckcpt}==2 (Unit 9/11 not linked)")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
