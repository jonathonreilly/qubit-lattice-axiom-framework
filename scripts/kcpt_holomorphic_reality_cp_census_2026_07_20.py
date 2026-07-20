#!/usr/bin/env python3
"""KCPT Unit 13 holomorphic reality / CP census (Frobenius-Schur) runner.

Rebuilds, from the bare L=4, N=64 staggered-lattice site construction (no import
of any other runner), the antisymmetric integer adjacency D2, the corner-wave
kernel frame V8, the bulk operator M = D2 @ D2 with Hamming-shell projectors,
the Unit-8 total complex structure J_full = J_ker + J_bulk, the chiral parity
S_eps = diag((-1)^{x1+x2+x3}), the order-768 ambient group G_amb, and the
holomorphic / anti-holomorphic 32-planes W = ker(J_full - iI), H_- = ker(J_full + iI).

It censuses the reality (Frobenius-Schur) type of the Unit-12 decomposition
32 = 4 (+) 4 (+) 6 (+) 6 (+) 12 and shows the Unit-9 chiral parity S_eps realizes
the complex-conjugation / geometric-CP structure:

  T1  Frobenius-Schur indicators of the 5 holomorphic constituents are (0,0,0,0,+1):
      the rank-12 constituent is the UNIQUE real (self-conjugate) piece; the two 4's
      and two 6's are complex-type; the conjugates of the 20 complex modes are NOT
      in W -- they live in the anti-holomorphic plane H_-.        [G3,G8,G9,G14,G15,G16]
  T2  exact-integer bridge FS_W = (1/|G|) Sum_g chi_W(g^2) = +1 pinned to two class-sums
      A = Sum_g tr(U_g^2) = 2*768 = 1536 and B = Sum_g tr(U_g^2 J_full) = 0,
      via (A - iB)/2 = 768 = |G|*FS_W.                            [G10,G11,G12,G17]
  T3  geometric CP realization / why B = 0: S_eps anticommutes with D2, normalizes
      G_amb by sigma(g) = S_eps g S_eps, and EVERY square U_g^2 centralizes S_eps
      (C_{G_amb}(S_eps) has index 2, so all 768 squares land in it); with the landed
      Unit-9 identity S_eps J_full S_eps = -J_full this forces each term individually,
      tr(U_g^2 J_full) = tr(U_g^2 S_eps J_full S_eps) = -tr(U_g^2 J_full) = 0, so B = 0
      term-by-term; the same S_eps carries W -> H_- unitarily.    [G4,G5,G6,G7,G8,G9,G11]

ANTI-FABRICATION DISCIPLINE.  J_full is built ONLY from the shell/kernel machinery
(V8*J64*V8^T / 64^2 plus Sum_{m in 1,2,3} D2*Q_m/(2*sqrt m)); G2 proves a rational
sqrt(m)->1 proxy is NOT a complex structure and differs from J_full, so no
parity/sign proxy stands in for it.  The two load-bearing invariants A = Sum tr(U^2)
and B = Sum tr(U^2 J_full) are accumulated from the REAL integer / field-valued
traces of the actual 768 group elements, NEVER from their targets; A carries the
wrong-value rejectors A != 768 and A != 2304, the bridge carries FS_W != 0 and != 2,
and B = 0 is verified STRUCTURALLY term-by-term (each tr(U^2 J_full) individually
zero by the S_eps sign reversal, not a global fluke), discriminated by the S_eps-
COMMUTING insertion I whose per-term traces do NOT vanish (Sum_g tr(U^2 . I) = A =
1536, per-term max 64) -- the vanishing is specific to J anticommuting with S_eps.
No individual (mixed rational/irrational) character is ever gated equal to
a target -- only the summed exact class-sums A, B and the integer FS indicators.  The
commutant is computed from a MINIMAL generating set (verified closure == 768), so the
kron stack is Sum over ~7 generators of a 1024x1024 map, NOT over all 768 (which would
OOM the 8 GB machine).  Every completeness / identity gate carries a discriminating
wrong-value rejector; float eig / rank / SVD / spectrum checks are tagged [FLOAT].
"""
import itertools
import os
import numpy as np

L, N = 4, 64
TOL0 = 1e-12      # exact rational-zero level
TOL_F = 1e-9      # [FLOAT] identity level (spec-stated)
TOL_EIG = 1e-8    # eigen / rank / restriction selection
TOLREJ = 1e-6     # rejector / residual floor

DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))
U9_NOTE = "KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U12_NOTE = "KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md"
SELF_NOTE = "KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md"
U8_NOTE = "KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U10_NOTE = "KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md"
U11_NOTE = "KCPT_CHIRAL_PARITY_LAGRANGIAN_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-19.md"

# PRESERVE VERBATIM source-pin substrings (grepped from the on-disk parent notes):
PIN_U9 = "S_eps J_full S_eps = -J_full"
PIN_U12 = "4 + 4 + 6 + 6 + 12 = 32"

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


# ---------------- construction (self-contained; per spec CONSTRUCTION block) ----------
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


# ---------------- G_amb reconstruction (dressed-symmetry scan + closure) ---------------
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
Gamb_set = {U.tobytes() for U in Gamb}

# deterministic greedy minimal generating set (commutant of a generating set == of the group)
Gsorted = sorted(Gamb, key=lambda U: U.tobytes())
gens = []
gen_closure = 0
seen = set()
for U in Gsorted:
    if eqm(U, I64i) or U.tobytes() in seen:
        continue
    gens.append(U)
    cl = closure_amb(gens)
    seen = {x.tobytes() for x in cl}
    gen_closure = len(cl)
    if gen_closure == 768:
        break

# ---------------- holomorphic / anti-holomorphic frames --------------------------------
evals, evecs = np.linalg.eig(Jfull)
selp = np.where(np.abs(evals - 1j) < TOL_EIG)[0]
selm = np.where(np.abs(evals + 1j) < TOL_EIG)[0]
Bh, _ = np.linalg.qr(evecs[:, selp])       # holo 64 x 32
Bm, _ = np.linalg.qr(evecs[:, selm])       # anti-holo 64 x 32
n = 32
I32 = np.eye(n, dtype=complex)

# ---------------- per-element pass: restrictions, class-sums A,B, sigma images ----------
Cs = {}                # holo restriction B^H U B for every U in G_amb
g2keys = []            # bytes of U^2 (in G_amb, group is closed)
sigma_img = []         # S_eps U S_eps for every U
A_int = 0              # A = Sum_g tr(U_g^2)   (exact integer)
B_val = 0.0            # B = Sum_g tr(U_g^2 J_full)   (float; predict 0)
maxbI = 0              # max_g |tr(U_g^2 . I)|        (S_eps-COMMUTING insertion I: nonzero)
maxbJ_term = 0.0       # max_g |tr(U_g^2 . J_full)|   (S_eps-ANTICOMMUTING insertion J: zero)
for U in Gamb:
    key = U.tobytes()
    Cs[key] = Bh.conj().T @ U.astype(complex) @ Bh
    U2 = U @ U
    g2keys.append(U2.tobytes())
    tI = int(np.trace(U2))                     # tr(U_g^2 . I)  [I commutes with S_eps]
    A_int += tI
    maxbI = max(maxbI, abs(tI))
    t = float(np.sum(U2 * Jfull.T))            # tr(U_g^2 . J_full)  [J anticommutes with S_eps]
    B_val += t
    maxbJ_term = max(maxbJ_term, abs(t))
    sigma_img.append(Seps_int @ U @ Seps_int)

# ---------------- commutant from the generating set (memory-safe kron stack) ------------
Cgens = [Cs[g.tobytes()] for g in gens]
Astack = np.vstack([np.kron(C.T, I32) - np.kron(I32, C) for C in Cgens])
Ucv, sv, Vh = np.linalg.svd(Astack, full_matrices=False)
del Ucv, Astack
sv_asc = np.sort(sv)
dimc = int(np.sum(sv_asc < 1e-6))
gap = sv_asc[dimc] / max(sv_asc[dimc - 1], 1e-16) if 0 < dimc < len(sv_asc) else 0.0
Bs = [np.conj(Vh[-(i + 1)]).reshape(n, n, order="F") for i in range(dimc)]

# ---------------- split W into the 5 constituents (generic self-adjoint commutant elt) --
# accept a seed ONLY on five-cluster SEPARATION QUALITY, never on the block ranks.
Projs = None
ranks = None
chosen_seed = -1
for seed in range(128):
    rng = np.random.default_rng(seed)
    c = rng.standard_normal(dimc) + 1j * rng.standard_normal(dimc)
    Y = sum(c[i] * Bs[i] for i in range(dimc))
    H = Y + Y.conj().T
    w, Vv = np.linalg.eigh(H)
    spread = float(w[-1] - w[0])
    if spread <= 0:
        continue
    thr = 1e-4 * spread
    groups = [[0]]
    for j in range(1, n):
        if w[j] - w[j - 1] > thr:
            groups.append([j])
        else:
            groups[-1].append(j)
    intra = max((w[g[-1]] - w[g[0]]) for g in groups)
    inter = min((w[groups[t + 1][0]] - w[groups[t][-1]]) for t in range(len(groups) - 1)) \
        if len(groups) > 1 else 0.0
    if len(groups) >= 2 and inter > 1e6 * max(intra, 1e-18):
        Wproj = [Vv[:, g] for g in groups]
        Pk = [Wj @ Wj.conj().T for Wj in Wproj]
        rk = [int(round(np.trace(P).real)) for P in Pk]
        order = np.argsort(rk)
        Projs = [Pk[i] for i in order]
        ranks = [rk[i] for i in order]
        chosen_seed = seed
        break

# ---------------- per-constituent Frobenius-Schur indicators + characters ---------------
FS = None
imchi = None
if Projs is not None:
    FS = []
    imchi = []
    for Pk in Projs:
        acc = 0.0
        maxim = 0.0
        for gi in range(len(Gamb)):
            Cg = Cs[Gamb[gi].tobytes()]
            maxim = max(maxim, abs(np.trace(Pk @ Cg).imag))
            Cg2 = Cs[g2keys[gi]]
            acc += np.trace(Pk @ Cg2).real
        FS.append(acc / len(Gamb))
        imchi.append(maxim)

# =============================================================================== gates ==
# ---- group / structure sanity --------------------------------------------------------
maxD2 = max(int(np.max(np.abs(U @ D2 - D2 @ U))) for U in Gamb)
TR100 = perm(lambda x: (x[0] - 1, x[1], x[2]))            # innocent shift; breaks staggering
witnessD2 = int(np.max(np.abs(TR100 @ D2 - D2 @ TR100)))
maxJcomm = max(nrm(U.astype(float) @ Jfull - Jfull @ U.astype(float)) for U in Gamb)
gate("G1", len(Gamb) == 768 and maxD2 == 0 and witnessD2 > 0 and maxJcomm < TOL_F,
     f"|G_amb|={len(Gamb)}==768; every U commutes with D2 (max int dev {maxD2}==0, witness "
     f"TR[(1,0,0)] dev {witnessD2}>0 non-vacuous); [FLOAT] every U commutes with J_full "
     f"(max {maxJcomm:.1e}<1e-9): complex-linear action")

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

# ---- S_eps geometric-CP realization (the Unit-9 thread) ------------------------------
SD2S = Seps_int @ D2 @ Seps_int
gate("G4", eqm(SD2S, -D2) and not eqm(SD2S, D2) and nrm(D2) > 0,
     "EXACT: S_eps D2 S_eps == -D2 (S_eps anticommutes with the adjacency); != +D2 (D2 nonzero)")

sig_bytes = [W.tobytes() for W in sigma_img]
in_amb = all(sb in Gamb_set for sb in sig_bytes)
sig_commute = max(int(np.max(np.abs(W @ D2 - D2 @ W))) for W in sigma_img)
bijection = len(set(sig_bytes)) == 768 and set(sig_bytes) == Gamb_set
n_moved = sum(1 for gi in range(len(Gamb)) if not eqm(sigma_img[gi], Gamb[gi]))
seps_not_in = Seps_int.tobytes() not in Gamb_set
gate("G5", in_amb and sig_commute == 0 and bijection and n_moved > 0 and seps_not_in,
     f"S_eps normalizes G_amb: every W=S_eps U S_eps commutes with D2 (dev {sig_commute}==0) and lies "
     f"in G_amb; sigma is a BIJECTION of the 768 (|image|=={len(set(sig_bytes))}); REJECTOR sigma moves "
     f"{n_moved}>0 elements and S_eps not in G_amb ({seps_not_in})")

sq_central = all(eqm(Seps_int @ (Gamb[gi] @ Gamb[gi]) @ Seps_int, Gamb[gi] @ Gamb[gi])
                 for gi in range(len(Gamb)))
seps_inv = eqm(Seps_int @ Seps_int, I64i)
gate("G6", sq_central and seps_inv and 0 < n_moved < 768,
     f"EXACT: every square U_g^2 centralizes S_eps (S_eps U_g^2 S_eps == U_g^2 for all 768; "
     f"S_eps^2==I: {seps_inv}); DISCRIMINATOR: only {768 - n_moved} of 768 group elements centralize "
     f"S_eps -- {n_moved} do NOT (0<{n_moved}<768), so the squares land specifically in C(S_eps), "
     f"not because S_eps is central")

sjs = nrm(Seps @ Jfull @ Seps + Jfull)
sjs_plus = nrm(Seps @ Jfull @ Seps - Jfull)
gate("G7", sjs < TOL_F and sjs_plus > TOLREJ,
     f"[FLOAT] landed Unit-9 identity S_eps J_full S_eps == -J_full (||.+J||={sjs:.1e}<1e-9); "
     f"REJECTOR != +J_full (||.-J||={sjs_plus:.3f}>1e-6): the sign reversal is real")

T = Bm.conj().T @ Seps.astype(complex) @ Bh
Trank = int(np.linalg.matrix_rank(T, tol=TOL_EIG))
Tuni = nrm(T.conj().T @ T - np.eye(32))
gate("G8", Trank == 32 and Tuni < TOL_F,
     f"[FLOAT] S_eps carries W -> H_-: T=Bm^H S_eps B is 32x32 rank {Trank}==32 and unitary "
     f"(||T^H T - I||={Tuni:.1e}<1e-9)")

maxconj = 0.0
for U in Gamb:
    Uc = U.astype(complex)
    maxconj = max(maxconj, abs(np.trace(Bm.conj().T @ Uc @ Bm) - np.conj(np.trace(Bh.conj().T @ Uc @ Bh))))
gate("G9", maxconj < TOL_F,
     f"[FLOAT] anti-holo restriction == conj(holo restriction) over ALL 768: "
     f"max|tr(Bm^H U Bm) - conj(tr(B^H U B))|={maxconj:.1e}<1e-9 (H_- is the complex conjugate of W)")

# ---- exact-integer bridge (load-bearing) ---------------------------------------------
gate("G10", A_int == 1536 and A_int == 2 * 768 and A_int != 768 and A_int != 2304,
     f"A = Sum_g tr(U_g^2) = {A_int} == 1536 == 2*768 [EXACT INTEGER: U^2 signed perm]; "
     f"REJECTORS A != 768, A != 2304")

gate("G11", abs(B_val) < TOL_F and maxbJ_term < TOL_F and A_int == 1536 and maxbI == 64,
     f"[FLOAT] B = Sum_g tr(U_g^2 J_full) = {B_val:.2e} (|B|<1e-9), and EACH term individually zero "
     f"(max_g|tr(U_g^2 J_full)|={maxbJ_term:.1e}<1e-9): forced by G6 (U_g^2 centralizes S_eps) + G7 "
     f"(S_eps J S_eps=-J) -> tr(U_g^2 J)=tr(U_g^2 S_eps J S_eps)=-tr(U_g^2 J)=0. DISCRIMINATOR: the "
     f"S_eps-COMMUTING insertion I gives Sum_g tr(U_g^2 . I)=A={A_int}!=0, per-term max {maxbI}==64>0, "
     f"so the vanishing is specific to J anticommuting with S_eps, not an all-traces-zero artifact")

FS_W = ((A_int - 1j * B_val) / 2).real / len(Gamb)
half = (A_int - 1j * B_val) / 2
gate("G12", abs(FS_W - 1) < TOL_F and abs(FS_W) > 0.5 and abs(FS_W - 2) > 0.5,
     f"FS_W = ((A - iB)/2).real/|G| = {FS_W:.6f} == 1; REJECTORS != 0, != 2. "
     f"(A - iB)/2 = {half:.4f} == 768 == |G|*FS_W = {len(Gamb) * int(round(FS_W))}")

gate("G13", 1 < len(gens) <= 10 and gen_closure == 768 and dimc == 5,
     f"MEMORY-BUDGET: commutant from MINIMAL generating set ({len(gens)} gens, 1<..<=10, closure "
     f"{gen_closure}==768); generator-commutant dim {dimc}==5 (OOM-avoiding kron over ~7 gens, not 768)")

# ---- per-constituent reality census --------------------------------------------------
idem_sumI = nrm(sum(Projs) - np.eye(n)) if Projs is not None else 1.0
idem_sq = max(nrm(P @ P - P) for P in Projs) if Projs is not None else 1.0
idem_orth = max((nrm(Projs[i] @ Projs[j]) for i in range(len(Projs)) for j in range(len(Projs)) if i != j),
                default=1.0) if Projs is not None else 1.0
gate("G14", dimc == 5 and gap > 1e6 and Projs is not None and idem_sumI < TOL_EIG and idem_sq < TOL_EIG
     and idem_orth < TOL_EIG and ranks == [4, 4, 6, 6, 12] and sum(ranks) == 32
     and ranks != [4, 4, 4, 8, 12] and ranks != [2, 6, 6, 6, 12],
     f"commutant dim {dimc}==5 (clean sv-gap {gap:.1e}>1e6); 5 idempotents orthogonal (Sum P=I "
     f"{idem_sumI:.1e}, P^2=P {idem_sq:.1e}, P_iP_j=0 {idem_orth:.1e}), sorted ranks {ranks}==[4,4,6,6,12] "
     f"sum {sum(ranks) if ranks else -1}; REJECTORS != [4,4,4,8,12], != [2,6,6,6,12]")

FS_round = sorted(int(round(x)) for x in FS) if FS is not None else []
FS_res = max(abs(x - round(x)) for x in FS) if FS is not None else 1.0
plus_one_idx = [k for k in range(len(FS))if round(FS[k]) == 1] if FS is not None else []
plus_is_12 = len(plus_one_idx) == 1 and ranks[plus_one_idx[0]] == 12 if FS is not None else False
gate("G15", FS is not None and FS_res < TOLREJ and FS_round == [0, 0, 0, 0, 1] and sum(FS_round) == 1
     and plus_is_12 and FS_round != [0, 0, 0, 0, 0] and FS_round != [1, 1, 1, 1, 1]
     and FS_round != [0, 0, 0, 1, 1],
     f"[FLOAT] per-constituent FS_k round to integers (residual {FS_res:.1e}<1e-6), sorted {FS_round}"
     f"==[0,0,0,0,1], sum {sum(FS_round)}==1; the unique +1 is the rank-{ranks[plus_one_idx[0]] if plus_one_idx else '?'} "
     f"constituent; REJECTORS != [0,0,0,0,0], != [1,1,1,1,1], != [0,0,0,1,1]")

im12 = [imchi[k] for k in range(len(ranks)) if ranks[k] == 12] if imchi is not None else []
im_other = [imchi[k] for k in range(len(ranks)) if ranks[k] != 12] if imchi is not None else []
gate("G16", imchi is not None and len(im12) == 1 and im12[0] < TOLREJ
     and len(im_other) == 4 and all(v > 1e-3 for v in im_other),
     f"[FLOAT] rank-12 constituent self-conjugate (max|Im chi_12|={im12[0]:.1e}<1e-6); the four "
     f"rank-4/6 constituents NOT self-conjugate (min max|Im chi|={min(im_other):.3f}>1e-3): a real 12 "
     f"vs four genuinely complex modes")

sum_FSk = int(round(sum(FS))) if FS is not None else -99
gate("G17", sum_FSk == 1 and sum_FSk == int(round(FS_W)),
     f"CONSISTENCY: Sum_k FS_k = {sum_FSk} == FS_W = {int(round(FS_W))} (both == 1): "
     f"per-constituent census agrees with the exact-integer bridge")

# ---- source pins + self-note dependency discipline -----------------------------------
gate("G18", PIN_U9 in note_text(U9_NOTE),
     f"SOURCE PIN Unit 9: common-sign-orbit note contains `{PIN_U9}`")
gate("G19", PIN_U12 in note_text(U12_NOTE),
     f"SOURCE PIN Unit 12: holomorphic-rep note contains `{PIN_U12}`")

s = note_text(SELF_NOTE)
c12 = s.count("](" + U12_NOTE)
c9 = s.count("](" + U9_NOTE)
ckcpt = s.count("](KCPT_")
c8 = s.count("](" + U8_NOTE)
c10 = s.count("](" + U10_NOTE)
c11 = s.count("](" + U11_NOTE)
gate("G20", ckcpt == 2 and c12 == 1 and c9 == 1 and c8 == 0 and c10 == 0 and c11 == 0,
     f"SELF-NOTE DEPENDENCY DISCIPLINE: total KCPT-links {ckcpt}==2 (Unit12 {c12}==1, Unit9 {c9}==1); "
     f"Unit8/10/11 linked {c8}/{c10}/{c11} == 0/0/0 (backticked only, never `](...)`)")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
raise SystemExit(1 if FAIL else 0)
