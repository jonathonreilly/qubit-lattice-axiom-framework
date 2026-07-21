#!/usr/bin/env python3
"""KCPT Unit 17 - Dirac-radius grading of End_H(C^64): P = D2 @ J_full is the negative
Dirac-radius operator -|D2| = -sqrt(-D2^2), an H-invariant real-symmetric element of the
c_H = 6 commutant, block-scalar on the six Unit-14 CP-completed constituents with
eigenvalue lambda_i = -2 sqrt(m_i) (the staggered-Dirac shell radii {0, -2, -2sqrt2, -2sqrt3}).

Rebuilds, from the bare L=4, N=64 staggered-lattice site construction (no import of any
other runner), the antisymmetric integer adjacency D2, the corner-wave kernel frame V8,
the bulk operator M = D2 @ D2 with Hamming-shell projectors, the Unit-8 total complex
structure J_full = J_ker + J_bulk, the chiral parity S_eps = diag((-1)^{x1+x2+x3}), the
order-768 ambient group G_amb, its order-1536 extension H = <G_amb, S_eps>, the
holomorphic / anti-holomorphic 32-planes W, H_-, the five holomorphic G_amb-idempotents
{4,4,6,6,12} (Unit 12), and the SIX CP-completed H-constituents
C^64 = 8 + 8 + 12 + 12 + 12^+ + 12^- (Unit 14).  It then forms P := D2 @ J_full and:

  T1  P is real-symmetric (D2 and J_full commute) and H-INVARIANT: [P,h]=0 for ALL 1536
      h in H, i.e. P in End_H(C^64).  Neither factor is H-invariant on its own -- both D2
      and J_full are chi_sgn-ODD (S_eps D2 S_eps=-D2, S_eps J_full S_eps=-J_full, Unit 9);
      their product is chi_sgn-EVEN, hence commutes with the S_eps coset as well as G_amb.
  T2  CLOSED FORM: P == -|D2| = -sqrt(-D2^2), reproduced independently from the M=D2^2
      shell spectrum.  Hence P is block-scalar on the six Unit-14 constituents with
      lambda_i = -2 sqrt(m_i), m_i the D2^2-shell radius of that constituent; the full
      P-spectrum is {0 (x8), -2 (x24), -2sqrt2 (x24), -2sqrt3 (x8)} matching the [8,24,24,8]
      shell dims of an independent eigh(M).
  T3  THE COMPUTED SHELL ASSIGNMENT: the CP-split pair {12^+,12^-} (the unique rank-12
      W-source that splits) BOTH sit at m=1 (lambda=-2) -- RADIUS-DEGENERATE; the two
      induced 12's (rank-6 W-source) BOTH sit at m=2 (lambda=-2sqrt2); the two induced 8's
      (rank-4 W-source) occupy the two EXTREME shells {m=0 (kernel), m=3 (top)}.  So the
      Dirac radius does NOT separate 12^+ from 12^- -- CP grading and radius grading are
      independent quantum numbers.
  T4  ANTI-FABRICATION contrast: neither D2 nor J_full alone is block-scalar / H-invariant
      (max_h ||[D2,h]|| >= 1, max_h ||[J_full,h]|| >= 0.5); D2 has a nonzero chi_sgn
      off-block Z_{12+}^H D2 Z_{12-} >= 1 whereas P's is zero.  A rational sqrt(m)->1 proxy
      for J_full fails J^2=-I and yields the WRONG integer spectrum -2m (not -2sqrt m).

ANTI-FABRICATION DISCIPLINE.  J_full is built ONLY from the shell/kernel machinery
(V8*J64*V8^T / 64^2 plus Sum_{m in 1,2,3} D2*Q_m/(2*sqrt m)); G2 proves the sqrt(m)->1
proxy is NOT a complex structure AND that P_proxy = D2*J_full_proxy has integer eigenvalues
-2m in {0,-2,-4,-6}, DIFFERENT from P's irrational -2sqrt m -- so no parity/sign/integer
proxy can fake the spectrum.  Every lambda_i is checked against m_i recomputed INDEPENDENTLY
from Z_i^H M Z_i (integer M=D2^2), and the closed form P=-sqrt(-M) is reproduced from a
separate eigh(M); the +-2sqrt2, +-2sqrt3 values cannot arise from the integer proxy.  The
commutant dimensions c_G, c_H are accumulated from the REAL integer traces of the ACTUAL
768 / 1536 group elements (never their targets); the shell assignment is grouped by
W-source rank (seed-robust: the multiset of shells per source-rank is basis-independent),
never by the seed-dependent constituent label order.
"""
import itertools
import os
import numpy as np

# Every note this runner reads (two parents + this unit's own note), repo-relative.
AUDIT_INPUT_PATHS = (
    "docs/KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md",
    "docs/KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md",
    "docs/KCPT_DIRAC_RADIUS_GRADING_OF_END_H_BOUNDED_THEOREM_NOTE_2026-07-20.md",   # self-note
)

L, N = 4, 64
TOL0 = 1e-12
TOL_F = 1e-9
TOL_EIG = 1e-8
TOLREJ = 1e-6
TOL_COMM = 1e-6

DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
U14_NOTE = "KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U9_NOTE = "KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md"
SELF_NOTE = "KCPT_DIRAC_RADIUS_GRADING_OF_END_H_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U8_NOTE = "KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U10_NOTE = "KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U11_NOTE = "KCPT_CHIRAL_PARITY_LAGRANGIAN_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U12_NOTE = "KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U13_NOTE = "KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md"

# PRESERVE VERBATIM source-pin substrings (grepped from the on-disk parent notes):
PIN_U14 = "9216 / 1536 = 6"
PIN_U9 = "S_eps J_full S_eps = -J_full"

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


# ---------------- construction (VERBATIM object-identical to the Unit-14 runner) ---------
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
Jker_int = V8 @ J64 @ V8.T

M = D2 @ D2
lam = [0, -4, -8, -12]
Fac = [M - lam[m] * np.eye(N, dtype=np.int64) for m in range(4)]
Q = []
for m in range(4):
    P0 = np.eye(N, dtype=np.int64)
    for mp in range(4):
        if mp != m:
            P0 = P0 @ Fac[mp]
    Q.append(P0)
Nm = []
for m in range(4):
    v = 1
    for mp in range(4):
        if mp != m:
            v *= (lam[m] - lam[mp])
    Nm.append(v)

D2f = D2.astype(float)
Pf = [Q[m].astype(float) / Nm[m] for m in range(4)]
Jkerf = Jker_int.astype(float) / (64.0 ** 2)
Jbulk = sum(D2f @ Pf[m] / (2.0 * np.sqrt(m)) for m in (1, 2, 3))
Jfull = Jkerf + Jbulk

# rational sqrt(m)->1 proxy: a discriminating counter-object ONLY (anti-proxy rejector)
Jbulk_proxy = sum(D2f @ Pf[m] / 2.0 for m in (1, 2, 3))
Jfull_proxy = Jkerf + Jbulk_proxy

eps = np.array([(-1) ** int(coords[i][0] + coords[i][1] + coords[i][2]) for i in range(N)], dtype=np.int64)
Seps_int = np.diag(eps)
Seps = Seps_int.astype(float)
I64i = np.eye(N, dtype=np.int64)


def perm(fmap):
    P0 = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        y = np.array(fmap(coords[i])) % L
        P0[i, idx(int(y[0]), int(y[1]), int(y[2]))] = 1
    return P0


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
Gamb_set = {U.tobytes() for U in Gamb}

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

gens_H = gens_G + [Seps_int]
Hgrp = closure_grp(gens_H)
gen_closure_H = len(Hgrp)
Hset = {h.tobytes() for h in Hgrp}
coset = [Seps_int @ g for g in Gamb]
coset_bytes = [c.tobytes() for c in coset]
gamb_in_H = all(g.tobytes() in Hset for g in Gamb)
coset_in_H = all(cb in Hset for cb in coset_bytes)
coset_disjoint = all(cb not in Gamb_set for cb in coset_bytes)

# exact-integer commutant discriminators (chi(h) = tr(h) in Z for signed perms)
SG = sum(int(np.trace(g)) ** 2 for g in Gamb)
SH = sum(int(np.trace(h)) ** 2 for h in Hgrp)
Scoset = sum(int(np.trace(c)) ** 2 for c in coset)
maxtr_coset = max(abs(int(np.trace(c))) for c in coset)
cG = SG // len(Gamb)
cH = SH // len(Hgrp)

# holomorphic / anti-holomorphic frames
evals, evecs = np.linalg.eig(Jfull)
selp = np.where(np.abs(evals - 1j) < TOL_EIG)[0]
selm = np.where(np.abs(evals + 1j) < TOL_EIG)[0]
Bh, _ = np.linalg.qr(evecs[:, selp])
Bm, _ = np.linalg.qr(evecs[:, selm])
PiW = Bh @ Bh.conj().T
PiHm = Bm @ Bm.conj().T


def commutant_dim(mats, r):
    Ir = np.eye(r, dtype=complex)
    A = np.vstack([np.kron(m.T, Ir) - np.kron(Ir, m) for m in mats])
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < TOL_COMM))


def commutant_basis(mats, r, d):
    Ir = np.eye(r, dtype=complex)
    A = np.vstack([np.kron(m.T, Ir) - np.kron(Ir, m) for m in mats])
    Uc, s, Vh = np.linalg.svd(A, full_matrices=False)
    del Uc, A
    return [np.conj(Vh[-(i + 1)]).reshape(r, r, order="F") for i in range(d)]


def split_block(Z, basis_mats, r, d):
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


# 5 holomorphic G_amb-idempotents on W (Unit-12 census)
Cgens = [Bh.conj().T @ g.astype(complex) @ Bh for g in gens_G]
dimcW = commutant_dim(Cgens, 32)
BsW = commutant_basis(Cgens, 32, dimcW)
subZW, ranksW, seedW = split_block(Bh, BsW, 32, dimcW)
order = list(np.argsort(ranksW))
subZW = [subZW[i] for i in order]
ranksW = [ranksW[i] for i in order]
PW = [z @ z.conj().T for z in subZW]
PHm = [Seps.astype(complex) @ p @ Seps.astype(complex) for p in PW]

# the SIX CP-completed H-constituents (Unit 14): tag, 64xd orthobasis Z, W-source rank,
# is_split flag (True for the two halves of the unique rank-12 real block).
gens_Hc = [g.astype(complex) for g in gens_H]
constituents = []  # (tag, Z, wrank, is_split)
for k in range(len(PW)):
    wrank = ranksW[k]
    block = PW[k] + PHm[k]
    r = int(round(np.trace(block).real))
    ww, VV = np.linalg.eigh((block + block.conj().T) / 2)
    Z = VV[:, -r:]
    matsH = [Z.conj().T @ g @ Z for g in gens_Hc]
    d = commutant_dim(matsH, r)
    if d == 1:
        constituents.append((f"ind{r}(W{wrank})", Z, wrank, False))
    else:
        BsB = commutant_basis(matsH, r, d)
        subZb, subr, seedb = split_block(Z, BsB, r, d)
        ordb = list(np.argsort(subr))
        subZb = [subZb[i] for i in ordb]
        for h_i, zz in enumerate(subZb):
            constituents.append((f"split12_{'+' if h_i == 0 else '-'}(W{wrank})", zz, wrank, True))

# ============================ P = D2 @ J_full analysis ================================
P = D2f @ Jfull
Pc = P.astype(complex)
Mc = M.astype(float).astype(complex)
D2c = D2f.astype(complex)

# T1 structure
symdev = nrm(P - P.T)
commdev = nrm(P - Jfull @ D2f)
commP = max(nrm(P @ g.astype(float) - g.astype(float) @ P) for g in Hgrp)
commD2 = max(nrm(D2f @ g.astype(float) - g.astype(float) @ D2f) for g in Hgrp)
commJ = max(nrm(Jfull @ g.astype(float) - g.astype(float) @ Jfull) for g in Hgrp)
SepsD2 = Seps_int @ D2 @ Seps_int
sMs = nrm(Seps @ M.astype(float) @ Seps - M.astype(float))

# T2 closed form  P == -|D2| == -sqrt(-M),  reproduced from an INDEPENDENT eigh(M).
# |D2| = sqrt(-M) is the operator square root of the positive-semidefinite -M; the kernel
# of M (M-eigenvalue exactly 0) maps to 0 by definition -- snapping it kills the spurious
# sqrt(~1e-14 eigh-noise)~1e-7 kernel contribution WITHOUT touching the {-4,-8,-12} shells.
wM, VM = np.linalg.eigh(M.astype(float))
sqrt_negM = np.sqrt(np.maximum(-wM, 0.0))
sqrt_negM[np.abs(wM) < 1e-6] = 0.0
absD2 = VM @ np.diag(sqrt_negM) @ VM.T   # sqrt(-M) = |D2|
Pclosed = -absD2
closed_dev = nrm(P - Pclosed)
# independent M-shell dims (m from eigenvalue -4m), sorted by m
shell_dims = {}
for w in wM:
    m = int(round(-w / 4))
    shell_dims[m] = shell_dims.get(m, 0) + 1
shell_dims_sorted = [shell_dims.get(m, 0) for m in range(4)]

# full P-spectrum multiset -> shell dims from P itself
wP = np.linalg.eigvalsh((P + P.T) / 2)
Pshell = {}
for w in wP:
    m = int(round((w / -2.0) ** 2))   # w = -2 sqrt(m)  =>  m = (w/-2)^2
    Pshell[m] = Pshell.get(m, 0) + 1
Pshell_sorted = [Pshell.get(m, 0) for m in range(4)]

# per-constituent block-scalar census
census = []  # (tag, d, wrank, is_split, lam_i, m_i, scalres, mres, d2_scalres)
for tag, Z, wrank, is_split in constituents:
    d = Z.shape[1]
    blk = Z.conj().T @ Pc @ Z
    lam_i = complex(np.trace(blk) / d)
    scalres = nrm(blk - lam_i * np.eye(d))
    mblk = Z.conj().T @ Mc @ Z
    mval = complex(np.trace(mblk) / d)
    m_i = int(round(-mval.real / 4))
    mres = nrm(mblk - mval * np.eye(d))
    d2blk = Z.conj().T @ D2c @ Z
    d2lam = complex(np.trace(d2blk) / d)
    d2scalres = nrm(d2blk - d2lam * np.eye(d))
    census.append((tag, d, wrank, is_split, lam_i.real, m_i, scalres, mres, d2scalres))

max_scalres = max(c[6] for c in census)
max_mres = max(c[7] for c in census)
lam_matches = all(abs(c[4] - (-2.0 * np.sqrt(c[5]))) < TOL_F for c in census)

# off-block census (P block-diagonal; D2 has off-blocks incl. the chi_sgn 12+<->12-)
maxoffP = 0.0
maxoffD2 = 0.0
d2_pm = None
for i in range(len(constituents)):
    for j in range(len(constituents)):
        if i == j:
            continue
        Zi = constituents[i][1]
        Zj = constituents[j][1]
        maxoffP = max(maxoffP, nrm(Zi.conj().T @ Pc @ Zj))
        maxoffD2 = max(maxoffD2, nrm(Zi.conj().T @ D2c @ Zj))
        if constituents[i][0].startswith("split12_+") and constituents[j][0].startswith("split12_-"):
            d2_pm = nrm(Zi.conj().T @ D2c @ Zj)

# proxy P: integer spectrum -2m (NOT -2 sqrt m)
Pproxy = (D2f @ Jfull_proxy)
proxy_census = []
for tag, Z, wrank, is_split in constituents:
    d = Z.shape[1]
    blk = Z.conj().T @ (Pproxy.astype(complex)) @ Z
    proxy_census.append(complex(np.trace(blk) / d).real)

# shell assignment grouped by W-source rank (seed-robust multisets)
m_split = sorted(c[5] for c in census if c[3])            # the CP pair (rank-12 source)
m_ind12 = sorted(c[5] for c in census if (not c[3]) and c[2] == 6)   # induced 12's (rank-6)
m_ind8 = sorted(c[5] for c in census if (not c[3]) and c[2] == 4)    # induced 8's (rank-4)

# ============================================================================== gates ==
gate("G1", len(Gamb) == 768 and gen_closure_H == 1536 and gen_closure_H == 2 * 768
     and gamb_in_H and coset_in_H and coset_disjoint,
     f"|G_amb|={len(Gamb)}==768; |H|={gen_closure_H}==1536==2*768; G_amb subset H ({gamb_in_H}), "
     f"coset S_eps*G_amb subset H ({coset_in_H}) and DISJOINT ({coset_disjoint}: index 2)")

j2 = nrm(Jfull @ Jfull + np.eye(N))
janti = nrm(Jfull + Jfull.T)
proxy2 = nrm(Jfull_proxy @ Jfull_proxy + np.eye(N))
proxydiff = nrm(Jfull - Jfull_proxy)
gate("G2", j2 < TOL_F and janti < TOL_F and proxy2 > TOLREJ and proxydiff > TOLREJ,
     f"[FLOAT] J_full^2=-I (||J^2+I||={j2:.1e}<1e-9), antisym (||J+J^T||={janti:.1e}); ANTI-PROXY: "
     f"sqrt(m)->1 proxy fails J^2=-I (||.||={proxy2:.3f}>1e-6) and differs from J_full "
     f"({proxydiff:.3f}>1e-6) -- shell sqrt(m) normalizers load-bearing, J_full no sign proxy")

gate("G3", symdev < TOL_F and commdev < TOL_F and nrm(P) > 1.0
     and nrm(P - D2f) > TOLREJ and nrm(P - Jfull) > TOLREJ,
     f"[FLOAT] P := D2*J_full is real-symmetric (||P-P^T||={symdev:.1e}<1e-9) because D2 and "
     f"J_full COMMUTE (||P-J_full*D2||={commdev:.1e}<1e-9); P nonzero (||P||={nrm(P):.3f}>1) and "
     f"P != D2, P != J_full (genuine product)")

gate("G4", commP < TOL_F,
     f"[FLOAT] THE THEOREM: max_{{h in H}} ||[P,h]|| = {commP:.1e}<1e-9 over ALL {len(Hgrp)} "
     f"elements -- P in End_H(C^64), the c_H=6 commutant")

gate("G5", commD2 > 1.0 and commJ > 0.5 and eqm(SepsD2, -D2) and sMs < TOL_F,
     f"ANTI-FAB CONTRAST: neither factor is H-invariant -- max_h ||[D2,h]||={commD2:.3f}>1 and "
     f"max_h ||[J_full,h]||={commJ:.3f}>0.5; both chi_sgn-ODD (S_eps D2 S_eps==-D2 exact: "
     f"{eqm(SepsD2, -D2)}), product chi_sgn-EVEN; S_eps preserves D2^2-shells "
     f"(||S_eps M S_eps - M||={sMs:.1e}). P's H-invariance is a genuine odd*odd=even effect")

gate("G6", cG == 12 and cH == 6 and Scoset == 0 and maxtr_coset == 0,
     f"exact-integer commutant pins (Unit-14 reproduced): c_G={cG}==12, c_H={cH}==6 "
     f"[Sum tr^2 = {SG}/{len(Gamb)}, {SH}/{len(Hgrp)}]; coset traceless (Sum tr^2={Scoset}==0, "
     f"max|tr|={maxtr_coset}==0). c_H=6 = the number of constituents P is block-scalar on")

Hdims = sorted(c[1] for c in census)
n_split = sum(1 for c in census if c[3])
n_ind = sum(1 for c in census if not c[3])
one_rank12_splits = all(c[2] == 12 for c in census if c[3]) and n_split == 2
gate("G7", Hdims == [8, 8, 12, 12, 12, 12] and len(census) == 6 and len(census) == cH
     and n_split == 2 and n_ind == 4 and one_rank12_splits,
     f"the SIX Unit-14 constituents rebuilt object-identically: dims (sorted) {Hdims}=="
     f"[8,8,12,12,12,12], count {len(census)}==6==c_H; exactly {n_split}==2 are the CP-split pair "
     f"(both from the unique rank-12 W-source: {one_rank12_splits}), {n_ind}==4 induced")

gate("G8", closed_dev < TOL_F and shell_dims_sorted == [8, 24, 24, 8]
     and Pshell_sorted == [8, 24, 24, 8],
     f"[FLOAT] CLOSED FORM P == -|D2| == -sqrt(-D2^2): ||P - (-sqrt(-M))||={closed_dev:.1e}<1e-9 "
     f"(|D2| reproduced from an INDEPENDENT eigh(M)); M-shell dims (m=0..3) "
     f"{shell_dims_sorted}==[8,24,24,8] and P's own spectrum tiles the same shells "
     f"{Pshell_sorted}==[8,24,24,8]")

gate("G9", max_scalres < TOL_F and max_mres < TOL0 * 1e3 and lam_matches and maxoffP < 1e-9,
     f"[FLOAT] BLOCK-SCALAR CENSUS: on every constituent Z_i^H P Z_i = lambda_i I "
     f"(max ||blk-lam I||={max_scalres:.1e}<1e-9), and lambda_i == -2 sqrt(m_i) with m_i from an "
     f"INDEPENDENT Z_i^H M Z_i (={ [c[5] for c in census] }, scalar dev {max_mres:.1e}); P "
     f"block-diagonal (max off-block |Z_i^H P Z_j|={maxoffP:.1e}<1e-9)")

# THE computed shell assignment (seed-robust multisets grouped by W-source rank)
gate("G10", m_split == [1, 1] and m_ind12 == [2, 2] and set(m_ind8) == {0, 3},
     f"THE COMPUTED ASSIGNMENT: CP-split pair {{12+,12-}} both at m={m_split}==[1,1] "
     f"(RADIUS-DEGENERATE, lambda=-2); induced 12's at m={m_ind12}==[2,2] (lambda=-2sqrt2); "
     f"induced 8's at the extreme shells m(set)={sorted(set(m_ind8))}=={{0,3}} (kernel + top). "
     f"Dirac radius does NOT separate 12+ from 12- -- CP grading independent of radius grading")

proxy_int = all(abs(v - round(v)) < 1e-6 for v in proxy_census)
proxy_vals = sorted(set(round(v) for v in proxy_census))
d2_offblock = d2_pm is not None and d2_pm > 1.0
gate("G11", d2_offblock and max(c[8] for c in census) > 1.0 and proxy_int
     and proxy_vals != [0, -2, -3, -4] and set(proxy_vals) <= {0, -2, -4, -6},
     f"ANTI-FAB: D2 alone has a NONZERO chi_sgn off-block |Z_12+^H D2 Z_12-|={d2_pm:.3f}>1 and is "
     f"NOT block-scalar (max D2-alone |blk-scal|={max(c[8] for c in census):.3f}>1), so P's "
     f"block-diagonality is NOT inherited from D2; the sqrt(m)->1 proxy gives INTEGER block values "
     f"-2m {proxy_vals} (in {{0,-2,-4,-6}}), NOT the irrational -2sqrt m -- no integer proxy fakes it")

# ---- source pins + self-note dependency discipline -----------------------------------
gate("G-PIN-U14", PIN_U14 in note_text(U14_NOTE),
     f"SOURCE PIN Unit 14: CP-completion note contains `{PIN_U14}` (c_H=6, the six constituents "
     f"P is block-scalar on)")
gate("G-PIN-U9", PIN_U9 in note_text(U9_NOTE),
     f"SOURCE PIN Unit 9: common-sign-orbit note contains `{PIN_U9}` (with S_eps D2 S_eps=-D2, the "
     f"two sign reversals that make P chi_sgn-even -> H-invariant)")

s = note_text(SELF_NOTE)
ckcpt = s.count("](KCPT_")
c14 = s.count("](" + U14_NOTE)
c9 = s.count("](" + U9_NOTE)
c8 = s.count("](" + U8_NOTE)
c10 = s.count("](" + U10_NOTE)
c11 = s.count("](" + U11_NOTE)
c12 = s.count("](" + U12_NOTE)
c13 = s.count("](" + U13_NOTE)
gate("G-PIN-SELF", ckcpt == 2 and c14 == 1 and c9 == 1
     and c8 == 0 and c10 == 0 and c11 == 0 and c12 == 0 and c13 == 0,
     f"SELF-NOTE DEPENDENCY DISCIPLINE: total KCPT-links {ckcpt}==2 (Unit14 {c14}==1, Unit9 {c9}==1); "
     f"Units 8/10/11/12/13 linked {c8}/{c10}/{c11}/{c12}/{c13}==0 (backticked only, never `](...)`)")

gate("G-MEM", gen_closure_G == 768 and gen_closure_H == 1536
     and 1 < len(gens_G) <= 16 and 1 < len(gens_H) <= 20,
     f"MEMORY-BUDGET: greedy generating sets close exactly -- G_amb {len(gens_G)} gens -> "
     f"{gen_closure_G}==768, H {len(gens_H)} gens -> {gen_closure_H}==1536; commutant kron stacks use "
     f"these generators, never a per-element stack over 768/1536 (OOM-avoiding)")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
