#!/usr/bin/env python3
"""KCPT Unit 14 CP-completion under the extended group H = <G_amb, S_eps> (order 1536).

Rebuilds, from the bare L=4, N=64 staggered-lattice site construction (no import of
any other runner), the antisymmetric integer adjacency D2, the corner-wave kernel
frame V8, the bulk operator M = D2 @ D2 with Hamming-shell projectors, the Unit-8
total complex structure J_full = J_ker + J_bulk, the chiral parity
S_eps = diag((-1)^{x1+x2+x3}), the order-768 ambient group G_amb, its holomorphic /
anti-holomorphic 32-planes W = ker(J_full - iI) and H_- = ker(J_full + iI), and the
five holomorphic G_amb-idempotents {4,4,6,6,12} of the Unit-12 census.

It adjoins S_eps to G_amb to form the order-1536 group H = <G_amb, S_eps> in which
G_amb is index 2, and decomposes the complexified full carrier
V_R (x) C ~= C^64 = W (+) H_- under H:

  T1  C^64 = 8 (+) 8 (+) 12 (+) 12 (+) 12^+ (+) 12^- : six multiplicity-free
      constituents. The four COMPLEX-type G_amb constituents (two 4's, two 6's,
      Unit 13) CP-DOUBLE with their S_eps-images in H_- into two irreducible 8's
      and two irreducible 12's; the UNIQUE REAL 12 (Unit 13) is the ONLY one that
      does NOT fuse -- its 24-dim H-module (the real 12 of W TOGETHER with its
      S_eps-image in H_-) is H-reducible and SPLITS into a CP-even 12^+ and a
      CP-odd 12^-.                                               [G6,G10,G11,G12]
  T2  exact-integer discriminator: c_G = dim End_{G_amb}(C^64) = 12 and
      c_H = dim End_H(C^64) = 6, from the REAL integer signed-permutation traces
      chi(h) = tr(h) in Z of the actual 768 / 1536 elements. c_H = 6 (six pieces)
      rather than 5 (a single unsplit 24) IS the statement that the real 12 splits;
      every element of the coset S_eps*G_amb is traceless (Sum_coset tr^2 = 0), the
      W <-> H_- signature inside the separately verified index-2 extension. [G7,G8,G9]
  T3  the 12^+/12^- split, THREE complementary checks: (1) the 24-block's H-commutant
      dim = 2 (two inequivalent H-irreps); (2) its G_amb-commutant dim = 4 = M_2
      (two copies of the SAME self-conjugate real 12 under G_amb alone -- the split
      is created by the coset, not by G_amb); (3) a coset element carries opposite
      half-characters chi_{12^-} = -chi_{12^+} on the full coset (equal on every
      G_amb element) -- the
      sign character chi_sgn of H/G_amb = Z/2, so 12^- = 12^+ (x) chi_sgn. [G13,G14,G15]

ANTI-FABRICATION DISCIPLINE.  J_full is built ONLY from the shell/kernel machinery
(V8*J64*V8^T / 64^2 plus Sum_{m in 1,2,3} D2*Q_m/(2*sqrt m)); G2 proves a rational
sqrt(m)->1 proxy is NOT a complex structure and differs from J_full, so no
parity/sign proxy stands in for it.  The commutant dimensions c_G, c_H and the
coset trace-sum are accumulated from the REAL integer traces of the ACTUAL 768 /
1536 group elements, NEVER from their targets; each carries wrong-value rejectors
(c_G != 10/11/13, c_H != 5/7, coset non-vacuity + G_amb NOT all-traceless).  The
12^+/12^- split is checked THREE complementary ways -- an H-commutant dim, a
G_amb-commutant dim, and a full-group opposite-coset half-character comparison --
each a real computed quantity able to fail on its own.  Every completeness / identity gate
carries a discriminating rejector.  In the full 64-rep every h in H is a signed
permutation so tr(h) in Z is an INTEGER (coset elements traceless, tr = 0);
irrationality (+-2*sqrt(2) in Q(sqrt 2)) appears ONLY on the 24-block-RESTRICTED
half-characters chi_{12+-} and is NEVER gated to a numeric value -- G15 gates only
the opposite-SIGN structure.  The commutants are computed from small deterministic
greedy generating sets (verified closure == 768 / == 1536), so the kron stacks use
those sets, NOT all 768/1536 elements (which would OOM the 8 GB machine).
"""
import itertools
import os
import numpy as np

# Every note this runner reads (three parents + this unit's own note), repo-relative.
# Plain literal tuple, statically ast-parseable by the runner-cache input fingerprint.
AUDIT_INPUT_PATHS = (
    "docs/KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md",
    "docs/KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md",
    "docs/KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md",
    "docs/KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md",   # self-note
)

L, N = 4, 64
TOL0 = 1e-12      # exact rational-zero level
TOL_F = 1e-9      # [FLOAT] identity level (spec-stated)
TOL_EIG = 1e-8    # eigen / rank / restriction selection
TOLREJ = 1e-6     # rejector / residual floor
TOL_COMM = 1e-6   # commutant singular-value null threshold

DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
U9_NOTE = "KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U12_NOTE = "KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U13_NOTE = "KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md"
SELF_NOTE = "KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U8_NOTE = "KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U10_NOTE = "KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U11_NOTE = "KCPT_CHIRAL_PARITY_LAGRANGIAN_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-19.md"

# PRESERVE VERBATIM source-pin substrings (grepped from the on-disk parent notes):
PIN_U9 = "S_eps J_full S_eps = -J_full"
PIN_U12 = "4 + 4 + 6 + 6 + 12 = 32"
PIN_U13 = "FS = (0, 0, 0, 0, +1)"

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


# ---------------- construction (self-contained; per spec CONSTRUCTION block) ------------
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

# rational sqrt(m)->1 proxy: a discriminating counter-object ONLY (G2 anti-proxy rejector)
Jbulk_proxy = sum(D2f @ Pf[m] / 2.0 for m in (1, 2, 3))
Jfull_proxy = Jkerf + Jbulk_proxy

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
Gamb_set = {U.tobytes() for U in Gamb}

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
Hgrp = closure_grp(gens_H)
gen_closure_H = len(Hgrp)
Hset = {h.tobytes() for h in Hgrp}
coset = [Seps_int @ g for g in Gamb]             # the nontrivial coset S_eps * G_amb
coset_bytes = [c.tobytes() for c in coset]
gamb_in_H = all(g.tobytes() in Hset for g in Gamb)
coset_in_H = all(cb in Hset for cb in coset_bytes)
coset_disjoint = all(cb not in Gamb_set for cb in coset_bytes)

# ---------------- exact-integer class-sums (chi(h) = tr(h) in Z for signed perms) -------
SG = sum(int(np.trace(g)) ** 2 for g in Gamb)     # = |G_amb| * dim End_{G_amb}(C^64)
SH = sum(int(np.trace(h)) ** 2 for h in Hgrp)     # = |H|     * dim End_H(C^64)
Scoset = sum(int(np.trace(c)) ** 2 for c in coset)
maxtr_coset = max(abs(int(np.trace(c))) for c in coset)
maxtr_G = max(abs(int(np.trace(g))) for g in Gamb)
cG = SG // len(Gamb)
cH = SH // len(Hgrp)

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

# ---------------- H-decomposition: restrict each block PW_k+PHm_k to H, split if reducible
gensHc = [g.astype(complex) for g in gens_H]
gensGc = [g.astype(complex) for g in gens_G]
Hdims = []
block_dk = []
block_wrank = []
block_uni = []
split_subranks = None
ZhalfW = None
dG24 = None
ov = {"Wp": None, "Hmp": None, "Wm": None, "Hmm": None}
coset_best = None
gamb_gap = None
coset_opp_gap = None
half_char_imag = None
for k in range(len(PW)):
    wrank = ranksW[k]
    block = PW[k] + PHm[k]
    r = int(round(np.trace(block).real))                         # 2 * wrank
    ww, VV = np.linalg.eigh((block + block.conj().T) / 2)
    Z = VV[:, -r:]                                               # 64 x r orthobasis of the block
    matsH = [Z.conj().T @ g @ Z for g in gensHc]
    uni = max(nrm(m.conj().T @ m - np.eye(r)) for m in matsH)    # block H-invariant iff restr. unitary
    d = commutant_dim(matsH, r)
    block_dk.append(d)
    block_wrank.append(wrank)
    block_uni.append(uni)
    if d == 1:
        Hdims.append(r)
        continue
    # reducible block: split into its d H-irreps
    BsB = commutant_basis(matsH, r, d)
    subZb, subr, seedb = split_block(Z, BsB, r, d)
    if subZb is None:
        continue
    ordb = list(np.argsort(subr))
    subZb = [subZb[i] for i in ordb]
    subr = [subr[i] for i in ordb]
    split_subranks = subr[:]
    Hdims.extend(subr)
    ZhalfW = subZb                                               # two 64 x 12 half-bases
    # proof 2 (G14): G_amb-restricted commutant of the SAME 24-block
    matsG = [Z.conj().T @ g @ Z for g in gensGc]
    dG24 = commutant_dim(matsG, r)
    # proof 1 (G13): CP-mixing -- each 12-half meets W and H_- evenly (6 + 6)
    Pip = ZhalfW[0] @ ZhalfW[0].conj().T
    Pim = ZhalfW[1] @ ZhalfW[1].conj().T
    ov["Wp"] = float(np.trace(Pip @ PiW).real)
    ov["Hmp"] = float(np.trace(Pip @ PiHm).real)
    ov["Wm"] = float(np.trace(Pim @ PiW).real)
    ov["Hmm"] = float(np.trace(Pim @ PiHm).real)
    # character cross-check (G15): equal on ALL of G_amb, opposite on ALL of the
    # coset, and real.  The accepted condition never keys on the observed +-2*sqrt(2).
    def half_chars(x):
        xc = x.astype(complex)
        return (np.trace(ZhalfW[0].conj().T @ xc @ ZhalfW[0]),
                np.trace(ZhalfW[1].conj().T @ xc @ ZhalfW[1]))

    gchars = [half_chars(g) for g in Gamb]
    cchars = [half_chars(c) for c in coset]
    gamb_gap = max(abs(ta - tb) for ta, tb in gchars)
    coset_opp_gap = max(abs(ta + tb) for ta, tb in cchars)
    half_char_imag = max(abs(z.imag) for pair in gchars + cchars for z in pair)
    coset_best = max(cchars, key=lambda pair: abs(pair[0]))
    if abs(coset_best[0]) <= 1.0:
        coset_best = None

Hdims_sorted = sorted(Hdims)

# =============================================================================== gates ==
# ---- group / structure sanity --------------------------------------------------------
maxD2 = max(int(np.max(np.abs(U @ D2 - D2 @ U))) for U in Gamb)
TR100 = perm(lambda x: (x[0] - 1, x[1], x[2]))            # innocent shift; breaks staggering
witnessD2 = int(np.max(np.abs(TR100 @ D2 - D2 @ TR100)))
maxJcomm = max(nrm(U.astype(float) @ Jfull - Jfull @ U.astype(float)) for U in Gamb)
gate("G1", len(Gamb) == 768 and maxD2 == 0 and witnessD2 > 0 and maxJcomm < TOL_F,
     f"|G_amb|={len(Gamb)}==768; every U commutes with D2 (max int dev {maxD2}==0, witness "
     f"TR[(1,0,0)] dev {witnessD2}>0 non-vacuous); [FLOAT] every U commutes with J_full "
     f"(max {maxJcomm:.1e}<1e-9): complex-linear G_amb action")

j2 = nrm(Jfull @ Jfull + np.eye(N))
janti = nrm(Jfull + Jfull.T)
proxy2 = nrm(Jfull_proxy @ Jfull_proxy + np.eye(N))
proxydiff = nrm(Jfull - Jfull_proxy)
gate("G2", j2 < TOL_F and janti < TOL_F and proxy2 > TOLREJ and proxydiff > TOLREJ,
     f"[FLOAT] J_full^2=-I (||J^2+I||={j2:.1e}<1e-9), antisym (||J+J^T||={janti:.1e}); "
     f"ANTI-PROXY REJECTOR: sqrt(m)->1 proxy fails J^2=-I (||.||={proxy2:.3f}>1e-6) and differs "
     f"from J_full ({proxydiff:.3f}>1e-6) -- shell normalizers load-bearing, J_full no sign proxy")

gate("G3", len(selp) == 32 and len(selm) == 32 and len(selp) + len(selm) == 64,
     f"[FLOAT] +i eigenspace dim {len(selp)}==32 (holo W) and -i dim {len(selm)}==32 (anti-holo H_-), "
     f"sum {len(selp) + len(selm)}==64")

# ---- S_eps index-2 CP engine (the Unit-9 thread) -------------------------------------
SD2S = Seps_int @ D2 @ Seps_int
gate("G4", eqm(SD2S, -D2) and not eqm(SD2S, D2) and nrm(D2) > 0,
     "EXACT: S_eps D2 S_eps == -D2 (S_eps anticommutes with the adjacency; every nearest-neighbor "
     "hop flips site parity); != +D2, D2 nonzero")

sjs = nrm(Seps @ Jfull @ Seps + Jfull)
sjs_plus = nrm(Seps @ Jfull @ Seps - Jfull)
gate("G5", sjs < TOL_F and sjs_plus > TOLREJ,
     f"[FLOAT] landed Unit-9 identity S_eps J_full S_eps == -J_full (||.+J||={sjs:.1e}<1e-9); "
     f"REJECTOR != +J_full (||.-J||={sjs_plus:.3f}>1e-6): S_eps conjugates +i- to -i-eigenvectors, "
     f"carrying W -> H_- (pinned by source-grep at G-PIN-U9)")

gate("G6", gen_closure_H == 1536 and gen_closure_H == 2 * 768 and gamb_in_H and coset_in_H
     and coset_disjoint and gen_closure_H != 768 and gen_closure_H != 3072,
     f"|H|={gen_closure_H}==1536==2*768; G_amb subset H ({gamb_in_H}); the coset S_eps*G_amb subset H "
     f"({coset_in_H}) and DISJOINT from G_amb ({coset_disjoint}: index 2); REJECTORS |H|!=768 "
     f"(S_eps genuinely extends, S_eps not in G_amb) and |H|!=3072")

# ---- exact-integer commutant / traceless-coset discriminators ------------------------
gate("G7", SG == 9216 and SG % 768 == 0 and cG == 12 and cG != 10 and cG != 11 and cG != 13,
     f"c_G = (Sum_{{g in G_amb}} tr(g)^2)/|G_amb| = {SG}/{len(Gamb)} = {cG}==12 [EXACT INTEGER traces]; "
     f"Sum tr^2 {SG}==9216, Sum % 768 == 0 ({SG % 768 == 0}); REJECTORS c_G != 10/11/13")

gate("G8", SH == 9216 and SH % 1536 == 0 and cH == 6 and cH != 5 and cH != 7,
     f"c_H = (Sum_{{h in H}} tr(h)^2)/|H| = {SH}/{len(Hgrp)} = {cH}==6 [EXACT INTEGER traces]; "
     f"Sum tr^2 {SH}==9216, Sum % 1536 == 0 ({SH % 1536 == 0}); REJECTORS c_H != 5 (a single unsplit "
     f"24) / != 7. THE DISCRIMINATOR:  c_H = 6  <=>  real 12 splits")

gate("G9", Scoset == 0 and maxtr_coset == 0 and len(coset) == 768 and SG > 0 and maxtr_G == 64,
     f"coset traceless: Sum_{{c in S_eps*G_amb}} tr(c)^2 = {Scoset}==0 and max|tr(c)|={maxtr_coset}==0 "
     f"[EXACT INTEGER: coset carries W <-> H_-, zero diagonal]; NON-VACUITY len(coset)={len(coset)}==768 "
     f"and G_amb NOT all-traceless (Sum_G tr^2={SG}>0, max|tr(g)|={maxtr_G}==64): tracelessness is "
     f"coset-specific")

# ---- full H-decomposition (lift 5 W-idempotents, pair with S_eps-images, restrict to H)
sumPW = sum(PW) if PW else np.zeros((N, N), dtype=complex)
sumPHm = sum(PHm) if PHm else np.zeros((N, N), dtype=complex)
s1 = nrm(sumPW - PiW)
s2 = nrm(sumPHm - PiHm)
s3 = max((nrm(Seps.astype(complex) @ PW[k] @ Seps.astype(complex) - PHm[k]) for k in range(len(PW))),
         default=1.0)
s4 = max((nrm(PiHm @ PHm[k] @ PiHm - PHm[k]) for k in range(len(PHm))), default=1.0)
gate("G10", len(PW) == 5 and s1 < 1e-8 and s2 < 1e-8 and s3 < 1e-8 and s4 < 1e-8,
     f"[FLOAT] tiling: Sum_k PW_k == Pi_W=B B^H (||.||={s1:.1e}<1e-8) and Sum_k PHm_k == Pi_{{H_-}}=Bm Bm^H "
     f"(||.||={s2:.1e}<1e-8; S_eps maps W onto H_-), PHm_k=S_eps PW_k S_eps ({s3:.1e}) each supported in "
     f"H_- (||Pi_{{H_-}} PHm_k Pi_{{H_-}} - PHm_k||={s4:.1e}<1e-8)")

all_uni = (max(block_uni) < 1e-8) if block_uni else False
split_blocks = [k for k in range(len(block_dk)) if block_dk[k] == 2]
complex_blocks = [k for k in range(len(block_dk)) if block_dk[k] == 1]
split_is_rank12 = len(split_blocks) == 1 and block_wrank[split_blocks[0]] == 12
complex_ok = len(complex_blocks) == 4 and all(block_wrank[k] in (4, 6) for k in complex_blocks)
sum_dk = sum(block_dk)
no_high = all(d < 3 for d in block_dk) if block_dk else False
not_all_one = any(d != 1 for d in block_dk)
gate("G11", all_uni and split_is_rank12 and complex_ok and sum_dk == 6 and sum_dk == cH
     and no_high and not_all_one,
     f"[FLOAT] each block PW_k+PHm_k H-invariant (restr-unitary dev max "
     f"{max(block_uni) if block_uni else -1:.1e}<1e-8); H-commutant dims per block = "
     f"{[block_dk[k] for k in range(len(block_dk))]} paired to W-ranks "
     f"{block_wrank}: dim 2 is EXACTLY the rank-12 block ({split_is_rank12}), the other four dim 1; "
     f"Sum_k d_k={sum_dk}==6==c_H; REJECTOR not-all-1 ({not_all_one}, real 12 splits) and no d_k>=3")

gate("G12", Hdims_sorted == [8, 8, 12, 12, 12, 12] and sum(Hdims_sorted) == 64
     and len(Hdims_sorted) == 6 and len(Hdims_sorted) == cH
     and Hdims_sorted != [8, 8, 12, 12, 24] and Hdims_sorted != [4, 4, 6, 6, 12, 32],
     f"FULL H-decomposition dims (sorted) {Hdims_sorted}==[8,8,12,12,12,12], sum {sum(Hdims_sorted)}==64, "
     f"count {len(Hdims_sorted)}==6==c_H. MULT-FREE COROLLARY: count==6 with c_H==6 forces Sum_i m_i^2=6 "
     f"over 6 terms => every m_i==1 (the two 8's inequivalent, the four 12's pairwise inequivalent; a "
     f"repeated irrep would push c_H>=8). REJECTORS != [8,8,12,12,24] (c_H=5 non-split) / != [4,4,6,6,12,32]")

# ---- 12^+/12^- split -- three complementary checks -----------------------------------
overlaps = [ov["Wp"], ov["Hmp"], ov["Wm"], ov["Hmm"]]
mix_ok = all(o is not None and abs(o - 6.0) < 1e-6 for o in overlaps)
not_trivial = all(o is not None and abs(o) > 1.0 and abs(o - 12.0) > 1.0 for o in overlaps)
rank12_dk2 = split_is_rank12 and block_dk[split_blocks[0]] == 2 if split_blocks else False
gate("G13", rank12_dk2 and split_subranks == [12, 12] and mix_ok and not_trivial,
     f"PROOF 1 (H-commutant): the real-12 block's H-commutant dim == 2 (two inequivalent H-irreps), "
     f"sub-idempotents 12^+,12^- of equal rank {split_subranks}==[12,12]. CP-MIXING [FLOAT]: each half "
     f"meets W and H_- evenly -- tr(Pi_12+ Pi_W)={ov['Wp']:.4f}, tr(Pi_12+ Pi_H-)={ov['Hmp']:.4f}, "
     f"tr(Pi_12- Pi_W)={ov['Wm']:.4f}, tr(Pi_12- Pi_H-)={ov['Hmm']:.4f} all ==6 (<1e-6); REJECTOR "
     f"neither overlap 0 nor 12 (split is CP-diagonal, not a W/H_- relabelling)")

gate("G14", dG24 == 4 and dG24 != 2 and dG24 != 1,
     f"PROOF 2 (G_amb-commutant = M_2): the SAME 24-block's G_amb-restricted commutant dim = {dG24}==4=M_2 "
     f"-- under G_amb ALONE the 24 is two copies of ONE irrep (the self-conjugate real 12). REJECTORS "
     f"!= 2 (two distinct G_amb-irreps) / != 1. G_amb-commutant 4 (M_2, same content) vs "
     f"H-commutant 2 (split by the coset)")

chi_a, chi_b = coset_best if coset_best is not None else (0.0j, 0.0j)
opp = abs(chi_a + chi_b) < 1e-6
distinct = abs(chi_a - chi_b) > 1e-3
gamb_equal = gamb_gap is not None and gamb_gap < 1e-6
coset_all_opposite = coset_opp_gap is not None and coset_opp_gap < 1e-6
characters_real = half_char_imag is not None and half_char_imag < 1e-6
gate("G15", coset_best is not None and opp and distinct and gamb_equal and coset_all_opposite
     and characters_real,
     f"CHARACTER CROSS-CHECK (opposite coset character = chi_sgn): all 768 G_amb character pairs are "
     f"EQUAL (max complex gap {gamb_gap:.1e}<1e-6); all 768 coset pairs are OPPOSITE (max complex sum "
     f"{coset_opp_gap:.1e}<1e-6); all half-characters are REAL (max |Im| {half_char_imag:.1e}<1e-6). "
     f"One nonzero coset witness has (chi_a,chi_b)=({chi_a.real:+.4f},{chi_b.real:+.4f}) with "
     f"|chi_a-chi_b|={abs(chi_a - chi_b):.3f}>1e-3 -- hence 12^- = 12^+ (x) chi_sgn. "
     f"[observed value +-2*sqrt(2), NOT gated -- only equality/opposition, nonzero distinction, and reality]")

# ---- memory-budget gate (build discipline) -------------------------------------------
gate("G-MEM", gen_closure_G == 768 and gen_closure_H == 1536
     and 1 < len(gens_G) <= 16 and 1 < len(gens_H) <= 20,
     f"MEMORY-BUDGET: small deterministic greedy generating sets close exactly -- G_amb "
     f"{len(gens_G)} gens -> {gen_closure_G}==768, H {len(gens_H)} gens -> {gen_closure_H}==1536 "
     f"(1<len<=16/20, actual printed, never called minimal); commutant kron stacks use these "
     f"generators, never a per-element stack over 768/1536 (OOM-avoiding, peak < ~3 GB)")

# ---- source pins + self-note dependency discipline -----------------------------------
gate("G-PIN-U9", PIN_U9 in note_text(U9_NOTE),
     f"SOURCE PIN Unit 9: common-sign-orbit note contains `{PIN_U9}` (the sign reversal used by G5/G9)")
gate("G-PIN-U12", PIN_U12 in note_text(U12_NOTE),
     f"SOURCE PIN Unit 12: holomorphic-rep note contains `{PIN_U12}` (the decomposition that CP-completes)")
gate("G-PIN-U13", PIN_U13 in note_text(U13_NOTE),
     f"SOURCE PIN Unit 13: reality/CP-census note contains `{PIN_U13}` (rank-12 the unique self-conjugate)")

s = note_text(SELF_NOTE)
ckcpt = s.count("](KCPT_")
c12 = s.count("](" + U12_NOTE)
c13 = s.count("](" + U13_NOTE)
c9 = s.count("](" + U9_NOTE)
c8 = s.count("](" + U8_NOTE)
c10 = s.count("](" + U10_NOTE)
c11 = s.count("](" + U11_NOTE)
gate("G-PIN-SELF", ckcpt == 3 and c12 == 1 and c13 == 1 and c9 == 1 and c8 == 0 and c10 == 0 and c11 == 0,
     f"SELF-NOTE DEPENDENCY DISCIPLINE: total KCPT-links {ckcpt}==3 (Unit12 {c12}==1, Unit13 {c13}==1, "
     f"Unit9 {c9}==1); Unit8/10/11 linked {c8}/{c10}/{c11}==0/0/0 (backticked only, never `](...)`)")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
