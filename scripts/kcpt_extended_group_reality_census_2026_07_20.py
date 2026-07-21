#!/usr/bin/env python3
"""KCPT Unit 15 -- H-level Frobenius-Schur reality census of the six CP-completed constituents.

Self-contained (no import of any other runner). Rebuilds from the bare L=4, N=64
staggered-lattice site construction the antisymmetric integer adjacency D2, the
corner-wave kernel frame V8/J64, the ambient-invariant total complex structure
J_full = J_ker + J_bulk = V8 J64 V8^T / 64^2 + Sum_{m in 1,2,3} D2 Q_m/(2 sqrt m),
the chiral parity S_eps = diag((-1)^{x1+x2+x3}), the order-768 ambient group G_amb,
its order-1536 extension H = <G_amb, S_eps> (G_amb index 2, disjoint coset
S_eps*G_amb), the five holomorphic G_amb-idempotents PW (ranks 4,4,6,6,12) of the
Unit-12 census and their S_eps-images PHm in the anti-holomorphic plane H_-, and the
split ZhalfW of the CP-completed real-12 24-block into a 12^+ and a 12^-.

It forms the SIX Unit-14 constituents

    P6 = [ PW[0]+PHm[0], PW[1]+PHm[1], PW[2]+PHm[2], PW[3]+PHm[3],   (8, 8, 12, 12)
           ZhalfW[0] ZhalfW[0]^H, ZhalfW[1] ZhalfW[1]^H ]           (12^+, 12^-)

and certifies, TWO independent ways, the H-level reality (Frobenius-Schur) census

    FS_H = (+1, +1, +1, +1, +1, +1)   -- every constituent REAL / orthogonal type.

Physics: the CP-completion REALIFIES the census. Unit 13's (0, 0, 0, 0, +1) over the
holomorphic ranks (4,4,6,6,12) becomes (+1 x 6) over (8,8,12,12,12,12) once the
anti-holomorphic S_eps-partners are adjoined -- each complex-type G_amb piece (FS 0)
fuses with its S_eps-conjugate into a single self-dual real induced H-rep (+1); the
already-real 12 stays +1 in BOTH split halves.

METHOD A (group-sum Frobenius-Schur): FS_i = (1/|H|) Sum_{h in H} chi_i(h^2)
    = tr(P_i . T),  T = (1/|H|) Sum_{h in H} h@h  (valid: each P_i commutes with R(h)).
METHOD B (invariant symmetric bilinear form): every h in H is a REAL orthogonal signed
    permutation, so B(u,v) = u^T v (NO conjugation) is H-invariant. On a Hermitian
    orthobasis Z_i (64 x r) of constituent i, B restricts to G_i = Z_i^T Z_i (complex
    SYMMETRIC); min singular value > 0 <=> nondegenerate <=> real/orthogonal (+1).

ANTI-FABRICATION DISCIPLINE. J_full is rebuilt ONLY from the shell/kernel machinery;
G-CONSTRUCT proves a rational sqrt(m)->1 proxy is NOT a complex structure (fails
J^2 = -I, residual ~0.6) so no parity/sign proxy stands in for it. The FS indicators
are accumulated from the REAL group sum T = mean_H h@h and from REAL symmetric-form
singular values -- NEVER from the ranks or the expected +1. The BUILT-IN discriminator:
J_full is real antisymmetric, so its +-i eigenspaces W and H_- are each TOTALLY
B-isotropic (u^T v = 0), hence the symmetric form VANISHES on any holomorphic-only
block PW[k] (min-sv ~ 0, a LIVE rejector gate) and is NONDEGENERATE (min-sv = 1) only
after the S_eps CP-doubling PW[k]+PHm[k]. For the four complex-type blocks, the +1
type is CAUSED by the CP-completion; the real rank-12 instead splits into two +1
extensions. Every h in H is a signed permutation so the full character tr(h) is
integral and every constituent character chi_i(h) = tr(P_i h) is real.  The
12^+/- half-characters can still take the Unit-14 irrational values +/-2*sqrt(2);
this census decides reality by gate STRUCTURE (group sum + form nondegeneracy),
never by gating an individual irrational character value.
"""
import itertools
import os
import numpy as np

# The three landed notes this runner reads, repo-relative (Unit 14 primary, Unit 13
# before-census, and this note for dependency-discipline checks). Plain literal tuple,
# statically ast-parseable by the runner-cache input fingerprint, matching the Unit-14
# runner's declaration mechanism.
AUDIT_INPUT_PATHS = (
    "docs/KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md",
    "docs/KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md",
    "docs/KCPT_EXTENDED_GROUP_REALITY_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md",
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
SELF_NOTE = "KCPT_EXTENDED_GROUP_REALITY_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U9_NOTE = "KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U10_NOTE = "KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md"

# PRESERVE VERBATIM source-pin substrings (grepped from the on-disk parent notes):
PIN_U14 = "C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻"
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

# rational sqrt(m)->1 proxy: a discriminating counter-object ONLY (anti-proxy rejector)
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

# ---------------- exact-integer class-sums (chi(h) = tr(h) in Z for signed perms) -------
SG = sum(int(np.trace(g)) ** 2 for g in Gamb)     # = |G_amb| * dim End_{G_amb}(C^64)
SH = sum(int(np.trace(h)) ** 2 for h in Hgrp)     # = |H|     * dim End_H(C^64)
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

# ==================== SIX Unit-14 constituents and the two FS methods ===================
# four CP-doubled blocks (8,8,12,12) + the two halves of the split real 12 (12^+, 12^-)
P6 = [PW[0] + PHm[0], PW[1] + PHm[1], PW[2] + PHm[2], PW[3] + PHm[3],
      ZhalfW[0] @ ZhalfW[0].conj().T,
      ZhalfW[1] @ ZhalfW[1].conj().T]
ranks6 = sorted(int(round(np.trace(P).real)) for P in P6)

# --- METHOD A: group-sum FS over H,  T = (1/|H|) Sum_{h in H} h@h ---
TH = np.zeros((N, N), dtype=float)
for h in Hgrp:
    hf = h.astype(float)
    TH += hf @ hf
TH /= len(Hgrp)
FS_group = [complex(np.trace(P @ TH)) for P in P6]      # each ~ +1 + 0j


# --- METHOD B: invariant symmetric bilinear form min singular value ---
def form_minsv(P):
    r = int(round(np.trace(P).real))
    if r <= 0:
        return 0.0
    _w, V = np.linalg.eigh((P + P.conj().T) / 2.0)
    Z = V[:, -r:]                                # 64 x r, Z^H Z = I
    G = Z.T @ Z                                  # complex SYMMETRIC (NO conjugation) = restricted B
    s = np.linalg.svd(G, compute_uv=False)
    return float(s.min())


form_cp = [form_minsv(P) for P in P6]                  # CP-completed: each ~ 1.0
form_wonly = [form_minsv(PW[k]) for k in range(4)]     # holomorphic-only complex-type: each ~ 0

# --- real-character check: chi_i(h) = tr(P_i h) real over all h in H ---
char_imax = []
for P in P6:
    m = 0.0
    for h in Hgrp:
        val = complex(np.sum(P * h.astype(float).T))   # tr(P h)
        if abs(val.imag) > m:
            m = abs(val.imag)
    char_imax.append(m)

# --- BEFORE census over G_amb on the FIVE holomorphic PW (reproduces Unit 13) ---
TG = np.zeros((N, N), dtype=float)
for g in Gamb:
    gf = g.astype(float)
    TG += gf @ gf
TG /= len(Gamb)
FS_G = [float(np.trace(PW[k] @ TG).real) for k in range(5)]   # [0,0,0,0,1]

# ==================================== gates =====================================
# ---- G-CONSTRUCT: independent J_full rebuild + anti-proxy + S_eps sign reversals ------
group_structure_ok = (
    len(Gamb) == 768
    and len(Hgrp) == 1536
    and Gamb_set <= Hset
    and len(coset) == 768
    and not ({x.tobytes() for x in coset} & Gamb_set)
    and ({x.tobytes() for x in coset} | Gamb_set) == Hset
)
gate("G-CONSTRUCT-GROUP", group_structure_ok,
     f"reconstructed group structure: |G_amb|={len(Gamb)}==768, |H|={len(Hgrp)}==1536; "
     f"G_amb subset H, and the {len(coset)}-element S_eps*G_amb coset is disjoint and completes H; "
     f"REJECTORS |H| != 768, != 3072")

j2 = nrm(Jfull @ Jfull + np.eye(N))
janti = nrm(Jfull + Jfull.T)
gate("G-CONSTRUCT-J2", j2 < TOL_F and janti < TOL_F,
     f"[FLOAT] independent rebuild J_full^2 = -I_64 (||J^2+I||={j2:.1e}<1e-9, well within spec's "
     f"<0.13), antisymmetric (||J+J^T||={janti:.1e}<1e-9): shell/kernel machinery, no sign proxy")

proxy2 = nrm(Jfull_proxy @ Jfull_proxy + np.eye(N))
proxydiff = nrm(Jfull - Jfull_proxy)
gate("G-CONSTRUCT-PROXY", proxy2 > 0.1 and proxydiff > TOLREJ,
     f"ANTI-PROXY REJECTOR: the sqrt(m)->1 rational stand-in (/2.0 for /(2 sqrt m)) FAILS J^2=-I "
     f"(||J_proxy^2+I||={proxy2:.3f}~0.6, >0.1) and differs from J_full ({proxydiff:.3f}>1e-6): "
     f"the shell normalizers are load-bearing")

SD2S = Seps_int @ D2 @ Seps_int
sjs = nrm(Seps @ Jfull @ Seps + Jfull)
sjs_plus = nrm(Seps @ Jfull @ Seps - Jfull)
gate("G-CONSTRUCT-SEPS", sjs < TOL_F and sjs_plus > TOLREJ and eqm(SD2S, -D2) and not eqm(SD2S, D2),
     f"S_eps J_full S_eps = -J_full [FLOAT] (||.+J||={sjs:.1e}<1e-9), REJECTOR != +J_full "
     f"(||.-J||={sjs_plus:.3f}>1e-6); and EXACT integer S_eps D2 S_eps = -D2 (!= +D2): S_eps carries "
     f"W <-> H_-")

# ---- G-DECOMP: the six P6 are an idempotent tiling with the split ranks ---------------
idem = max(nrm(P @ P - P) for P in P6)
gate("G-DECOMP-IDEM", idem < TOL_EIG,
     f"[FLOAT] all six P6 idempotent: max||P^2-P||={idem:.1e}<1e-8")

sumdev = nrm(sum(P6) - np.eye(N))
gate("G-DECOMP-COMPLETE", sumdev < TOL_EIG,
     f"[FLOAT] the six P6 tile the identity: ||Sum P6 - I_64||={sumdev:.1e}<1e-8")

gate("G-DECOMP-RANKS",
     ranks6 == [8, 8, 12, 12, 12, 12] and sum(ranks6) == 64
     and ranks6 != [8, 8, 12, 12, 24] and ranks6 != [4, 4, 6, 6, 12, 32],
     f"integer ranks sorted {ranks6}==[8,8,12,12,12,12] summing to {sum(ranks6)}==64; REJECTORS "
     f"!=[8,8,12,12,24] (unsplit real-12) and !=[4,4,6,6,12,32] (holomorphic-only, no CP-completion)")

# ---- G-FSGROUP: commutation precondition, then Method-A group-sum indicators ----------
comm = 0.0
for P in P6:
    for g in gens_H:
        gc = g.astype(complex)
        comm = max(comm, nrm(P @ gc - gc @ P))
gate("G-FSGROUP-COMM", comm < TOL_EIG,
     f"PRECONDITION (else the FS group-sum is void): every P_i commutes with every H generator, "
     f"max||[P_i, R(gen_H)]||={comm:.1e}<1e-8")

fs_re_ok = all(abs(z.real - 1.0) < TOLREJ for z in FS_group)
fs_im_ok = all(abs(z.imag) < TOLREJ for z in FS_group)
gate("G-FSGROUP-FS", comm < TOL_EIG and fs_re_ok and fs_im_ok,
     f"METHOD A group-sum FS_i = tr(P_i . T), T = mean_H h@h: FS_group.real = "
     f"{[round(z.real, 4) for z in FS_group]} all == +1.0 (|.-1|<1e-6), max|Im| "
     f"{max(abs(z.imag) for z in FS_group):.1e}<1e-6 -- all six REAL/orthogonal type")

# ---- G-FSFORM: Method-B symmetric-form nondegeneracy + the built-in W-only rejector ----
cp_ok = all(mn > TOLREJ for mn in form_cp)
gate("G-FSFORM-CP", cp_ok,
     f"METHOD B symmetric-form min-sv (CP-completed) = {[round(mn, 4) for mn in form_cp]} all >1e-6 "
     f"(~1.0): B(u,v)=u^T v nondegenerate on every CP-completed block -> +1")

wonly_ok = all(mn < TOLREJ for mn in form_wonly)
gate("G-FSFORM-WONLY", wonly_ok and cp_ok,
     f"BUILT-IN W-ONLY REJECTOR (W totally B-isotropic): form min-sv on holomorphic-only PW[k] "
     f"(k=0..3, complex-type) = {['%.1e' % mn for mn in form_wonly]} all <1e-6, while CP-completed "
     f"all >1e-6 -- reality is CAUSED by the S_eps CP-doubling, not assumed")

# ---- G-AGREE: the two methods agree; none complex-type, none symplectic ---------------
methodA = [round(z.real) for z in FS_group]
methodB = [1 if mn > TOLREJ else 0 for mn in form_cp]
agree = methodA == [1, 1, 1, 1, 1, 1] and methodB == [1, 1, 1, 1, 1, 1]
none_complex = all(abs(abs(z) - 1.0) < TOLREJ for z in FS_group)
none_symp = all(z.real > 0.5 for z in FS_group)
gate("G-AGREE", agree and none_complex and none_symp,
     f"methods A and B AGREE on all six (A={methodA}, B={methodB}, both all +1); no constituent "
     f"complex-type (all |FS_group|=1: min {min(abs(z) for z in FS_group):.4f}) and none symplectic "
     f"(no -1: min Re {min(z.real for z in FS_group):.4f}>0)")

# ---- G-REALCHAR: characters are real over all of H (independent of the h^2 sum) -------
gate("G-REALCHAR", all(m < TOL_F for m in char_imax),
     f"chi_i(h) = tr(P_i h) REAL over all {len(Hgrp)} h in H: max_h|Im chi_i(h)| over the six "
     f"constituents = {max(char_imax):.1e}<1e-9 -- self-dual directly; the FS/form gates "
     f"distinguish orthogonal from quaternionic type")

# ---- G-REALIFY: tie Unit 13 (before) to this unit (after) -- the CP-completion realifies
FS_G_round = sorted(int(round(x)) for x in FS_G)
gate("G-REALIFY-BEFORE",
     FS_G_round == [0, 0, 0, 0, 1] and round(sum(FS_G)) == 1,
     f"BEFORE census over G_amb on the FIVE holomorphic PW (ranks 4,4,6,6,12): FS_G sorted "
     f"{FS_G_round}==[0,0,0,0,1] (four complex-type 0 + one real +1), sum {round(sum(FS_G))}==1 "
     f"[reproduces Unit-13 (0, 0, 0, 0, +1)]")

FS_H_re = [z.real for z in FS_group]
flip_ok = all(round(FS_G[k]) == 0 and round(FS_H_re[k]) == 1 for k in range(4))
stay_ok = round(FS_G[4]) == 1 and round(FS_H_re[4]) == 1 and round(FS_H_re[5]) == 1
gate("G-REALIFY-AFTER",
     round(sum(FS_H_re)) == 6 and flip_ok and stay_ok,
     f"AFTER census over H: sum(FS_H)={round(sum(FS_H_re))}==6 vs sum(FS_G)={round(sum(FS_G))}==1 -- "
     f"CP-completion REALIFIES. The four complex-type W-blocks FLIP 0->+1 ({flip_ok}); the unique "
     f"real 12 STAYS +1 in BOTH split halves ({stay_ok})")

# ---- G-COUNT: exact-integer six-constituent count pins to the Unit-14 splitting fact --
gate("G-COUNT", cH == 6 and cH != 5 and cH != 7 and SH % len(Hgrp) == 0,
     f"c_H = (Sum_{{h in H}} tr(h)^2)/|H| = {SH}/{len(Hgrp)} = {cH}==6 [EXACT INTEGER signed-perm "
     f"traces] -- six distinct H-constituents; REJECTORS c_H != 5 (unsplit) / != 7")

# ---- source pins + self-note dependency discipline ------------------------------------
gate("G-PIN-U14", PIN_U14 in note_text(U14_NOTE),
     f"SOURCE PIN Unit 14: CP-completion note contains `{PIN_U14}` (the six-constituent "
     f"decomposition being censused)")
gate("G-PIN-U13", PIN_U13 in note_text(U13_NOTE),
     f"SOURCE PIN Unit 13: reality/CP-census note contains `{PIN_U13}` (the before-census)")

s = note_text(SELF_NOTE)
ckcpt = s.count("](KCPT_")
c14 = s.count("](" + U14_NOTE)
c13 = s.count("](" + U13_NOTE)
c9 = s.count("](" + U9_NOTE)
c10 = s.count("](" + U10_NOTE)
gate("G-PIN-SELF",
     ckcpt == 2 and c14 == 1 and c13 == 1 and c9 == 0 and c10 == 0,
     f"SELF-NOTE DEPENDENCY DISCIPLINE: total KCPT-links {ckcpt}==2 (Unit14 {c14}==1, Unit13 {c13}==1); "
     f"Unit9 {c9}==0 and Unit10 {c10}==0 markdown links (backticked names only)")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
