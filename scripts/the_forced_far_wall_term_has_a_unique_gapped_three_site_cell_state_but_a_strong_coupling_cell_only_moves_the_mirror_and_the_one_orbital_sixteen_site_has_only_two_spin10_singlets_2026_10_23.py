AUDIT_INPUT_PATHS = ('docs/THE_FORCED_FAR_WALL_TERM_HAS_A_UNIQUE_GAPPED_THREE_SITE_CELL_STATE_BUT_A_STRONG_COUPLING_CELL_ONLY_MOVES_THE_MIRROR_AND_THE_ONE_ORBITAL_SIXTEEN_SITE_HAS_ONLY_TWO_SPIN10_SINGLETS_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""smg-strong-coupling: strong-coupling cells for the forced 3-4-5-0 far-wall term, bosonization of the same terms, and the
one-site test for the 16 of Spin(10).
 A  3450 cells: site, two-site, three- and four-site complete-graph cells; commutation; stability ingredients; relocation.
 B  3451 contrast: LSM filling, odd-cell doublet, even-cell spectra.
 C  bosonization (sympy): Haldane criterion data, free-point dimensions, the equal-velocity Luttinger threshold.
 D  one site of the 16 (2^16 Fock space): Spin(10) singlets, Casimir identity, the 10 and 120 channels, the 15, the 8,
    and the SU(3) x SU(2) x U(1)_Y x U(1)_B-L site.
Labels: [T] exact, [F] finite diagnostic. Supplied: charges, bond/pair forms, cells, naive hop, m sz stand-in, Luttinger
family, one orbital per weight, SM-group couplings. Cited, not rederived: Yarotsky 2006 (CMP 261, 799), Kennedy-Tasaki
1992, Bravyi-Hastings-Michalakis 2010, Haldane 1995, LSM/Oshikawa, Wang-Wen, Tong, Razamat-Tong,
Butt-Catterall-Hasenfratz, You-He-Xu-Vishwanath."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
from collections import Counter
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, sympy as sy

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))
def lowest(H, k):
    return np.sort(sla.eigsh(H.tocsr(), k=k, which='SA', tol=1e-12, return_eigenvectors=False, v0=rng.standard_normal(H.shape[0])))
def lowvec(H, k):
    e, v = sla.eigsh(H.tocsr(), k=k, which='SA', tol=1e-12, v0=rng.standard_normal(H.shape[0])); o = np.argsort(e); return e[o], v[:, o]

def ann(n):
    """sparse Jordan-Wigner annihilators on n modes"""
    dim = 1 << n; st = np.arange(dim); out = []
    for j in range(n):
        src = st[(st >> j) & 1 == 1]; dst = src ^ (1 << j)
        sg = 1 - 2 * (np.bitwise_count(src & ((1 << j) - 1)).astype(np.int64) & 1)
        out.append(sp.csr_matrix((sg.astype(float), (dst, src)), shape=(dim, dim)))
    return out

L1 = (1, -2, 1, 2); L2 = (2, 1, -2, 1); T51 = ((2, 0, -1, -1), (1, 0, -1, 2), (1, -2, 1, 0))
QA = (3, 4, 5, 0); QB = (2, 1, 2, -1); Q51 = (3, 4, 5, 1); SF = (1, 1, -1, -1)
CACHE = {}
def ops(ns):
    if ns not in CACHE:
        c = ann(4 * ns); CACHE[ns] = (c, [x.T.tocsr() for x in c])
    return CACHE[ns]
def cell(ns, terms, pairs):
    """forced terms on the listed site pairs (x, y): p = +-1 bond average (psi_x + psi_y)/2, p = +-2 pair psi_x psi_y"""
    c, cd = ops(ns); dim = 1 << (4 * ns); I = sp.identity(dim, format='csr'); H = sp.csr_matrix((dim, dim))
    C = lambda f, s: c[f * ns + s]; D = lambda f, s: cd[f * ns + s]
    for (x, y) in pairs:
        for l in terms:
            O = I
            for f in range(4):
                F = {1: (C(f, x) + C(f, y)) / 2, -1: (D(f, x) + D(f, y)) / 2, 2: C(f, x) @ C(f, y), -2: D(f, y) @ D(f, x)}.get(l[f])
                if F is not None: O = O @ F
            H = H + O + O.T
    N = [sum((cd[f * ns + s] @ c[f * ns + s]).diagonal() for s in range(ns)) for f in range(4)]
    return H.tocsr(), N
def hop(ns, pairs):
    c, cd = ops(ns); dim = 1 << (4 * ns); H = sp.csr_matrix((dim, dim), dtype=complex)
    for (x, y) in pairs:
        for f in range(4):
            A = cd[f * ns + x] @ c[f * ns + y]; H = H + SF[f] * 0.5j * (A - A.T)
    return H.tocsr()
K = lambda ns: list(itertools.combinations(range(ns), 2))

# ------------------------------------------------------------------ A
print("== A. 3450: the forced terms l1 = (1,-2,1,2), l2 = (2,1,-2,1) on cells (units of g)")
H1, _ = cell(1, (L1, L2), [(0, 0)])
check("A1 [T] one site: |l_f| = 2 needs two modes of one flavour (Pauli), so the term vanishes and all 16 states are degenerate",
      abs(H1).sum() == 0 and max(max(abs(x) for x in l) for l in (L1, L2)) == 2)
e2 = np.linalg.eigvalsh(cell(2, (L1, L2), K(2))[0].toarray())
d2 = int(np.sum(abs(e2 - e2[0]) < 1e-9))
check("A2 [F] two-site cell: ground state degenerate (the terms connect only pairs of configurations)", d2 > 1, f"{d2}-fold at {e2[0]:.3f}")
H3, N3 = cell(3, (L1, L2), K(3)); e3, v3 = lowvec(H3, 6); g3 = v3[:, 0]
qa = sum(q * (n - 1.5) for q, n in zip(QA, N3)); qb = sum(q * (n - 1.5) for q, n in zip(QB, N3))
mom = [abs(float(np.sum(abs(g3)**2 * x))) for x in (qa, qa**2, qb, qb**2)]
D0 = e3[1] - e3[0]
check("A3 [F] three-site complete-graph cell: unique ground state E0 = -1, E1 = -sqrt3/2, so Delta_0 = 1 - sqrt3/2; neutral "
      "(Q_A = Q_B = 0 from half filling, zero variance); a unique state is automatically symmetric",
      abs(e3[0] + 1) < 1e-9 and abs(e3[1] + np.sqrt(3) / 2) < 1e-9 and max(mom) < 1e-9, f"Delta_0 = {D0:.4f}, E1 x{int(np.sum(abs(e3-e3[1])<1e-9))}")
H4, N4 = cell(4, (L1, L2), K(4)); e4 = lowest(H4, 3)
check("A4 [F] four-site complete-graph cell: unique ground state, gap > 1e-2", e4[1] - e4[0] > 1e-2, f"gap {e4[1]-e4[0]:.4f}")
h01, _ = cell(3, (L1, L2), [(0, 1)]); h12, _ = cell(3, (L1, L2), [(1, 2)]); Cm = (h01 @ h12 - h12 @ h01).tocsr()
cn = np.sqrt(lowest(-(Cm.T @ Cm), 1)[0] * -1)
eo = lowest(h01 + h12, 3)
check("A5 [T]/[F] overlapping bond terms do not commute, and the open three-site chain is frustrated (E0 > 2 e_bond = -1) "
      "and degenerate: a uniform rule is not a sum of commuting or frustration-free blocks; a cell tiling is needed",
      cn > 0.1 and eo[0] > -0.9 and eo[1] - eo[0] < 1e-9, f"||[h01,h12]|| {cn:.3f}, E0 {eo[0]:.3f} x2")
hb = np.linalg.eigvalsh(hop(2, [(0, 1)]).toarray()); nb = max(abs(hb))
Hh = hop(3, [(0, 1), (1, 2)])
gap = lambda t: (lambda e: e[1] - e[0])(lowest(H3 + t * Hh, 2))
ok_small = all(gap(t) >= D0 / 2 for t in (0.02, 0.05, 0.1))
lo, hi = 0.1, 0.5
for _ in range(14):
    mid = (lo + hi) / 2; lo, hi = (mid, hi) if gap(mid) > 1e-4 else (lo, mid)
kap = 3 * nb / D0
check("A6 [F] stability ingredients: naive hop norm ||h_b|| = 2 per bond, z = 3 bonds per cell, so Yarotsky's hypothesis reads "
      "t/g < kappa_0 Delta_0/(z ||h_b||) = kappa_0/44.8 (kappa_0 not computed); one cell with its two hops keeps a unique "
      "state with gap >= Delta_0/2 for t/g <= 0.1, first crossing t_c/g in (0.1, 0.5)",
      abs(nb - 2) < 1e-9 and ok_small and 0.1 < hi < 0.5, f"z||h_b||/Delta_0 = {kap:.1f}, t_c/g = {hi:.3f}")
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex)
def slab(k, Ls, m):
    H = np.zeros((2 * Ls, 2 * Ls), complex); T = -(SZ + 1j * SY) / 2
    for s in range(Ls):
        H[2*s:2*s+2, 2*s:2*s+2] = np.sin(k) * SX + (1 - np.cos(k)) * SZ + (m * SZ if s == Ls - 1 else 0)
        if s + 1 < Ls: H[2*s+2:2*s+4, 2*s:2*s+2] = T; H[2*s:2*s+2, 2*s+2:2*s+4] = T.conj().T
    return H
k8 = np.pi / 8; ee, vv = np.linalg.eigh(slab(k8, 12, 20.0)); i8 = np.argmin(abs(ee - np.sin(k8)))
wl, wn = np.sum(abs(vv[-2:, i8])**2), np.sum(abs(vv[-4:-2, i8])**2)
check("A7 [F] relocation: free slab (Ls = 12) with the far layer gapped (m sz, m = 20): the far-wall branch keeps E = sin k "
      "and moves one layer in, so a gapped far-layer product does not gap the mirror (stability hypotheses fail for the slab)",
      abs(ee[i8] - np.sin(k8)) < 1e-6 and wl < 0.01 and wn > 0.9, f"k = pi/8: |dE| {abs(ee[i8]-np.sin(k8)):.1e}, w_far {wl:.4f}, w_next {wn:.3f}")

# ------------------------------------------------------------------ B
print("== B. 3451 contrast (fewest-change symmetric terms, Q51 kept)")
fill = lambda q: sum(q) / 2
check("B1 [T] at the particle-hole point Q51 per site = 13/2 (LSM: no unique gapped symmetric state with one-site translation); "
      "3450: Q_A, Q_B per site = 6, 2; sum q = q^T K q mod 2, so the lattice sees the anomaly mod 2 only",
      fill(Q51) == 6.5 and (fill(QA), fill(QB)) == (6, 2) and
      all((sum(q) - (q[0]**2 + q[1]**2 - q[2]**2 - q[3]**2)) % 2 == 0 for q in (QA, QB, Q51)))
def sectors(ns):
    H, N = cell(ns, T51, K(ns)); Q = sum(q * (n - ns / 2) for q, n in zip(Q51, N)); out = {}
    for val in np.unique(Q):
        idx = np.nonzero(Q == val)[0]; h = H[idx][:, idx]
        out[val] = np.linalg.eigvalsh(h.toarray())[:2] if len(idx) < 1200 else lowest(h, 2)
    return out
s3 = sectors(3); b3 = sorted(s3, key=lambda q: s3[q][0])
check("B2 [T]+[F] three-site cell: Q51 in Z + 1/2 on odd cells, particle-hole pairs +-Q51: ground state an exact doublet at "
      "Q51 = +-1/2", set(b3[:2]) == {0.5, -0.5} and abs(s3[0.5][0] - s3[-0.5][0]) < 1e-9 and s3[b3[2]][0] - s3[0.5][0] > 1e-6,
      f"E {s3[0.5][0]:.5f}, next sector {s3[b3[2]][0]:.5f}")
e2b = np.linalg.eigvalsh(cell(2, T51, K(2))[0].toarray()); d2b = int(np.sum(abs(e2b - e2b[0]) < 1e-9))
s4 = sectors(4); b4 = sorted(s4, key=lambda q: s4[q][0])
check("B3 [F] (recorded result) two-site cell many-fold; four-site cell a Q51 = +-2 doublet with Q51 = 0 higher (even cells: "
      "no kinematic obstruction, the doublet is dynamical): no unique 3451 cell up to four sites",
      d2b > 2 and set(b4[:2]) == {2.0, -2.0} and s4[0.0][0] - s4[2.0][0] > 1e-3,
      f"K2 {d2b}-fold; K4 E(+-2) {s4[2.0][0]:.4f}, E(0) {s4[0.0][0]:.4f}")

# ------------------------------------------------------------------ C
print("== C. bosonization: K = diag(1,1,-1,-1), charges (3,4,5,0), (2,1,2,-1)")
Ks = sy.diag(1, 1, -1, -1); l1 = sy.Matrix(L1); l2 = sy.Matrix(L2)
minors = [L1[i] * L2[j] - L1[j] * L2[i] for i in range(4) for j in range(i + 1, 4)]
check("C1 [T] l1, l2 K-null, mutually null, neutral under both charges, primitive (gcd of minors 1): Haldane's criterion "
      "(supplied) - the two cosines gap all four modes with a unique pinned minimum",
      (l1.T * Ks.inv() * l1)[0] == 0 and (l2.T * Ks.inv() * l2)[0] == 0 and (l1.T * Ks.inv() * l2)[0] == 0 and
      all(sum(a * b for a, b in zip(l, q)) == 0 for l in (L1, L2) for q in (QA, QB)) and np.gcd.reduce(np.abs(minors)) == 1)
check("C2 [T] free-point dimensions Delta = |l|^2/2 = 5, 5 (> 2): both irrelevant", (l1.dot(l1) / 2, l2.dot(l2) / 2) == (5, 5))
x = sy.symbols('x', real=True); O = sy.Matrix([[-sy.Rational(3, 5), -sy.Rational(4, 5)], [sy.Rational(4, 5), -sy.Rational(3, 5)]])
a1, b1, a2, b2 = l1[:2, 0], l1[2:, 0], l2[:2, 0], l2[2:, 0]
I2 = sy.eye(2); V = (sy.BlockMatrix([[I2, x * O.T], [x * O, I2]]).as_explicit()) / sy.sqrt(1 - x**2)
Vi = sy.simplify(V.inv()); dims = [sy.simplify((l.T * Vi * l)[0] / 2) for l in (l1, l2)]
target = 5 * sy.sqrt((1 - x) / (1 + x))
xs = sy.solve(sy.Eq(25 * (1 - x) / (1 + x), 4), x)
def num_dim(lv, xv):
    Vn = np.array(V.subs(x, xv).evalf(), dtype=float); eta = np.diag([1., 1, -1, -1])
    w, U = np.linalg.eigh(Vn); W = U @ np.diag(np.sqrt(w)) @ U.T; S, Uu = np.linalg.eigh(W @ eta @ W)
    Lam = np.linalg.inv(W) @ Uu @ np.diag(np.sqrt(abs(S)))
    return 0.5 * np.sum((Lam.T @ np.array(lv, float))**2)
numok = all(abs(num_dim(l, xv) - float(target.subs(x, xv))) < 1e-9 for l in (L1, L2) for xv in (0.3, 0.8))
check("C3 [T] b = O a with O a rotation; equal-velocity Luttinger family V(x) (V eta V = eta): Delta_1 = Delta_2 = "
      "5 sqrt((1-x)/(1+x)); both relevant iff 21/29 < x < 1 (numerical O(2,2) diagonalisation agrees)",
      O * a1 == b1 and O * a2 == b2 and sy.simplify(V * sy.diag(1, 1, -1, -1) * V - sy.diag(1, 1, -1, -1)) == sy.zeros(4) and
      all(sy.simplify(d**2 - target**2) == 0 and float(d.subs(x, 0.5)) > 0 for d in dims) and xs == [sy.Rational(21, 29)] and numok, "threshold x = 21/29 = 0.724")

# ------------------------------------------------------------------ D
print("== D. one site carrying the 16 (one orbital per weight, 2^16 states)")
b = ann(5); bd = [y.T.toarray() for y in b]; bb = [y.toarray() for y in b]
G = []
for k in range(5): G += [bb[k] + bd[k], 1j * (bb[k] - bd[k])]
ev = [s for s in range(32) if bin(s).count('1') % 2 == 0]
Sig = [(-0.25j * (G[a] @ G[c] - G[c] @ G[a]))[np.ix_(ev, ev)] for a, c in itertools.combinations(range(10), 2)]
cas16 = sum(S @ S for S in Sig)
check("D1 [T] 16 of Spin(10) from five oscillators: 45 Hermitian generators, Casimir 45/4", len(Sig) == 45 and
      max(np.abs(S - S.conj().T).max() for S in Sig) < 1e-14 and np.abs(cas16 - 45 / 4 * np.eye(16)).max() < 1e-12)
def psign(p):
    s = 1; p = list(p)
    for i in range(len(p)):
        while p[i] != i: j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s
W5 = [(np.array(p), np.array(f), psign(p)) for p in itertools.permutations(range(5)) for f in itertools.product((1, -1), repeat=5) if np.prod(f) == 1]
rho5 = np.array([8, 6, 4, 2, 0])
w16 = [np.array(v) for v in itertools.product((1, -1), repeat=5) if np.prod(v) == 1]     # doubled weights
def mult(cnt, lam): return sum(sg * cnt.get(tuple((lam + rho5)[p] * f - rho5), 0) for p, f, sg in W5)
st16 = np.arange(1 << 16); bits16 = ((st16[:, None] >> np.arange(16)) & 1); N16 = bits16.sum(1); WT = bits16 @ np.array(w16)
sing = [mult(Counter(map(tuple, WT[N16 == n])), np.zeros(5, int)) for n in range(17)]
check("D2 [T] Weyl character formula (|W(D5)| = 1920): Lambda^*(16) holds exactly two Spin(10) singlets, |0> and |F>",
      sing == [1] + [0] * 15 + [1], f"singlets by n: {''.join(map(str, sing))}")
c16 = ann(16); cd16 = [y.T.tocsr() for y in c16]
# basis order of the 16 = oscillator states ev; their Cartan weights must match w16 ordering for D2 (weights only) - D3 is basis-free
vr = rng.standard_normal(1 << 16) + 1j * rng.standard_normal(1 << 16); C2v = np.zeros_like(vr)
for S in Sig:
    T = sp.csr_matrix((1 << 16, 1 << 16), dtype=complex)
    for i, j in zip(*np.nonzero(np.abs(S) > 1e-14)): T = T + S[i, j] * (cd16[i] @ c16[j])
    C2v += T @ (T @ vr)
err = np.abs(C2v - 0.75 * N16 * (16 - N16) * vr).max() / np.abs(vr).max()
check("D3 [T] Casimir C2 = (3/4) N (16 - N) on the whole Fock space (Lambda^2(16) = 120 irreducible => the only number-"
      "conserving 4-fermion invariant is sum n_i n_j): every such term, incl. the 120 channel, is a function of N", err < 1e-9, f"err {err:.1e}")
pA = Counter(tuple(w16[i] + w16[j]) for i in range(16) for j in range(i + 1, 16))
pS = Counter(tuple(w16[i] + w16[j]) for i in range(16) for j in range(i, 16))
l10, l120 = np.array([2, 0, 0, 0, 0]), np.array([2, 2, 2, 0, 0])
check("D4 [T] the 10 is in Sym^2(16), not Lambda^2(16): psi^T C Gamma^a psi = 0 identically on one orbital (the suggested "
      "g sum_a |psi C Gamma^a psi|^2 is zero); Lambda^2(16) = 120", (mult(pA, l10), mult(pS, l10), mult(pA, l120)) == (0, 1, 1)
      and len(list(itertools.combinations(range(16), 2))) == 120)
Psi = c16[15]
for j in range(14, -1, -1): Psi = Psi @ c16[j]
HD5 = sp.diags((N16 * (16 - N16)).astype(float)) - (Psi + Psi.T)
e5, v5 = lowvec(HD5, 3); g5 = v5[:, 0]
check("D5 [T] unique Spin(10)-invariant site states lie in span{|0>,|F>}; particle-hole swaps them and only the 16-fermion "
      "term mixes them: N(16-N) - (Psi16 + h.c.) has the unique state (|0> +- |F>)/sqrt2 at -1, gap 2; no term of degree < 16 does",
      abs(e5[0] + 1) < 1e-9 and abs(e5[1] - e5[0] - 2) < 1e-9 and abs(abs(g5[0])**2 + abs(g5[-1])**2 - 1) < 1e-9)
c15 = ann(15); Cph = sp.identity(1 << 15, format='csr')
for y in c15: Cph = Cph @ (y + y.T)
Par = sp.diags(1.0 - 2 * (np.bitwise_count(np.arange(1 << 15)).astype(np.int64) & 1))
check("D6 [T] 15 modes (no nu^c): prod (c_i + c_i^+) anticommutes with fermion parity, so every level of a particle-hole-"
      "symmetric site is >= 2-fold for ANY interaction", abs(Cph @ Par + Par @ Cph).max() < 1e-12 and abs(Cph @ Par).max() > 0.5)
def sing_prod(modes, sun, nu1):
    M = len(modes); Wm = np.array(modes); s_ = np.arange(1 << M); bt = ((s_[:, None] >> np.arange(M)) & 1); Nn = bt.sum(1); Wt = bt @ Wm
    offs = np.cumsum([0] + sun)[:-1]; off = sum(sun); keep = np.all(Wt[:, off:off + nu1] == 0, axis=1)
    can = lambda v: tuple(np.concatenate([v[o:o + n] - v[o + n - 1] for o, n in zip(offs, sun)]))
    rho = np.concatenate([np.arange(n - 1, -1, -1) for n in sun])
    Ws = [[(np.array(p), psign(p)) for p in itertools.permutations(range(n))] for n in sun]; out = []
    for n in range(M + 1):
        cnt = Counter(can(v) for v in Wt[(Nn == n) & keep][:, :off]); tot = 0
        for combo in itertools.product(*Ws):
            y = np.concatenate([rho[o:o + nn][p] for (p, _), o, nn in zip(combo, offs, sun)]) - rho
            tot += np.prod([sgn for _, sgn in combo]) * cnt.get(can(y), 0)
        out.append(int(tot))
    return out
e_ = lambda n, i, s=1: np.eye(n, dtype=int)[i] * s
z3, z2 = np.zeros(3, int), np.zeros(2, int)
SM = ([np.concatenate([e_(3, c), e_(2, s), [1, 1]]) for c in range(3) for s in range(2)] +
      [np.concatenate([e_(3, c, -1), z2, [-4, -1]]) for c in range(3)] + [np.concatenate([e_(3, c, -1), z2, [2, -1]]) for c in range(3)] +
      [np.concatenate([z3, e_(2, s), [-3, -3]]) for s in range(2)] + [np.concatenate([z3, z2, [6, 3]]), np.concatenate([z3, z2, [0, 3]])])
QL = SM[:6] + SM[12:14]; P42 = [np.concatenate([e_(4, c), e_(2, s)]) for c in range(4) for s in range(2)]
sQL, s42, s16 = sing_prod(QL, [3, 2], 2), sing_prod(P42, [4, 2], 0), sing_prod(SM, [3, 2], 2)
check("D7 [T] 8 modes: Q + L (SU(3) x SU(2) x U(1)_Y x U(1)_B-L) and (4,2) (SU(4) x SU(2)) have singlets only at n = 0, 8: "
      "no unique state below degree 8, the same pattern as the Spin(10) 16", sQL == s42 == [1] + [0] * 7 + [1])
# D8: SM-group site, the six singlet charge-4 terms
kind = ['Q'] * 6 + ['u'] * 3 + ['d'] * 3 + ['L'] * 2 + ['e', 'n']
col = [c for c in range(3) for s in range(2)] + [0, 1, 2, 0, 1, 2] + [None] * 4
iso = [s for c in range(3) for s in range(2)] + [None] * 6 + [0, 1, None, None]
def raise_ops():
    out = []
    for (i, j) in ((0, 1), (1, 2)):
        R = sp.csr_matrix((1 << 16, 1 << 16))
        for a in range(16):
            if kind[a] == 'Q' and col[a] == j:
                bq = [m for m in range(16) if kind[m] == 'Q' and col[m] == i and iso[m] == iso[a]][0]; R = R + cd16[bq] @ c16[a]
            if kind[a] in 'ud' and col[a] == i:
                bq = [m for m in range(16) if kind[m] == kind[a] and col[m] == j][0]; R = R - cd16[bq] @ c16[a]
        out.append(R.tocsr())
    R = sp.csr_matrix((1 << 16, 1 << 16))
    for a in range(16):
        if kind[a] in 'QL' and iso[a] == 1:
            bq = [m for m in range(16) if kind[m] == kind[a] and col[m] == col[a] and iso[m] == 0][0]; R = R + cd16[bq] @ c16[a]
    return out + [R.tocsr()]
Rs = raise_ops(); Wsm = bits16 @ np.array(SM)
wz = np.all(np.stack([Wsm[:, 0] - Wsm[:, 2], Wsm[:, 1] - Wsm[:, 2], Wsm[:, 3] - Wsm[:, 4], Wsm[:, 5], Wsm[:, 6]], 1) == 0, axis=1)
sel = np.nonzero((N16 == 4) & wz)[0]
Pm = sp.csr_matrix((np.ones(len(sel)), (sel, np.arange(len(sel)))), shape=(1 << 16, len(sel)))
A = sp.vstack([R @ Pm for R in Rs]).tocsr(); A = A[np.unique(A.nonzero()[0])].toarray()
_, sv, vt = np.linalg.svd(A); Om = vt[int(np.sum(sv > 1e-9)):]
Ops = []
for w in Om:
    O = sp.csr_matrix((1 << 16, 1 << 16))
    for cf, s_ in zip(w, sel):
        if abs(cf) > 1e-12:
            oc = [j for j in range(16) if s_ >> j & 1]; O = O + cf * (c16[oc[3]] @ c16[oc[2]] @ c16[oc[1]] @ c16[oc[0]])
    Ops.append(O.tocsr())
H8 = -sum(O + O.T for O in Ops); e8, v8 = lowvec(H8, 3); g8 = v8[:, 0]
lad = max(np.linalg.norm(R @ g8) for R in Rs + [R.T.tocsr() for R in Rs])
check("D8 [F] SU(3) x SU(2) x U(1)_Y x U(1)_B-L on the one-orbital 16: singlets 1,6,8,6,1 at n = 0,4,8,12,16; its six singlet "
      "charge-4 terms with equal real couplings give a unique particle-hole-symmetric singlet ground state with a gap",
      s16 == [1, 0, 0, 0, 6, 0, 0, 0, 8, 0, 0, 0, 6, 0, 0, 0, 1] and len(Ops) == 6 and e8[1] - e8[0] > 0.05 and lad < 1e-8
      and abs(np.sum(abs(g8)**2 * (N16 % 4 != 0))) < 1e-12 and np.sum(abs(g8)**2 * (Wsm[:, 5]**2 + Wsm[:, 6]**2)) < 1e-9, f"gap {e8[1]-e8[0]:.3f} g, ladder residual {lad:.0e}")

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1 << 20)
print(f"Supplied: charges, bond/pair forms, cells, naive hop, m sz stand-in, Luttinger family, one orbital, SM couplings. "
      f"elapsed {time.time()-T0:.1f}s, peak RSS {rss:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
