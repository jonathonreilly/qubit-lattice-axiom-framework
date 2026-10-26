# Exact / numeric toolkit for the hard-core walk (development copy; check.py inlines nothing from here).
from fractions import Fraction as Fr
import itertools

class G:
    """Gaussian rational a+bi with Fraction parts."""
    __slots__ = ('a', 'b')
    def __init__(s, a=0, b=0):
        s.a = a if isinstance(a, Fr) else Fr(a)
        s.b = b if isinstance(b, Fr) else Fr(b)
    def __add__(s, o):
        if not isinstance(o, G): o = G(o)
        return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o):
        if not isinstance(o, G): o = G(o)
        return G(s.a - o.a, s.b - o.b)
    def __neg__(s): return G(-s.a, -s.b)
    def __mul__(s, o):
        if not isinstance(o, G): o = G(o)
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def conj(s): return G(s.a, -s.b)
    def inv(s):
        d = s.a * s.a + s.b * s.b
        return G(s.a / d, -s.b / d)
    def __truediv__(s, o):
        if not isinstance(o, G): o = G(o)
        return s * o.inv()
    def iszero(s): return s.a == 0 and s.b == 0
    def __eq__(s, o):
        if not isinstance(o, G): o = G(o)
        return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return "(%s%+si)" % (s.a, s.b)

Z = G(0); ONE = G(1); I_ = G(0, 1)

def gmat(rows):
    return [[x if isinstance(x, G) else G(x) for x in r] for r in rows]

SIG = [
    gmat([[0, 1], [1, 0]]),
    gmat([[0, G(0, -1)], [G(0, 1), 0]]),
    gmat([[1, 0], [0, -1]]),
]

def mm2(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(2)), Z) for j in range(2)] for i in range(2)]

def sigma_tilde(F, j, d):
    """sum_a F[a][j] sigma_a (a over first d Pauli matrices)."""
    M = [[Z, Z], [Z, Z]]
    for a in range(d):
        c = F[a][j]
        if c == 0: continue
        for r in range(2):
            for s in range(2):
                M[r][s] = M[r][s] + SIG[a][r][s] * c
    return M

# ------------------------------------------------------------------ graphs
class Graph:
    def __init__(self, dims, periodic, d):
        """sites = product of range(dims[i]); bonds oriented (x, y=x+e_j); open: only x_j+1<dims[j]; periodic: wrap."""
        self.dims = tuple(dims); self.periodic = periodic; self.d = d
        self.sites = list(itertools.product(*[range(L) for L in dims]))
        self.idx = {x: i for i, x in enumerate(self.sites)}
        self.n = len(self.sites)
        self.bonds = []
        for x in self.sites:
            for j in range(len(dims)):
                y = list(x); y[j] += 1
                if y[j] >= dims[j]:
                    if not periodic: continue
                    y[j] -= dims[j]
                if tuple(y) == x: continue          # length-1 direction: no bond
                self.bonds.append((self.idx[x], self.idx[tuple(y)], j))

def one_body(graph, F, amp_half):
    """list of (p, q, amp): H contains amp * c^dag_p c_q, p=(site,coin).
    H = sum_bonds (-i/2) sigma~_j |x><y| + h.c.  ; amp_half: the factor 1/2 as a number (or 1 for the doubled operator)."""
    d = graph.d
    terms = {}
    for (x, y, j) in graph.bonds:
        S = sigma_tilde(F, j, d)
        for s in range(2):
            for t in range(2):
                v = S[s][t]
                if v.iszero(): continue
                amp = G(0, -1) * v * amp_half          # (-i/2) S[s][t]
                p, q = (x, s), (y, t)
                terms[(p, q)] = terms.get((p, q), Z) + amp
                terms[(q, p)] = terms.get((q, p), Z) + amp.conj()
    return [(p, q, a) for (p, q), a in terms.items() if not a.iszero()]

# ------------------------------------------------------------------ many body (hard-core, one record per site)
def basis(n, N):
    out = []
    for sites in itertools.combinations(range(n), N):
        for coins in itertools.product((0, 1), repeat=N):
            out.append(tuple(zip(sites, coins)))
    return out

def apply_h(state, terms_by_q, fermion, n):
    """state: tuple of (site,coin) sorted by site. returns dict state'->amp.  terms_by_q[(y,t)] = list of (x,s,amp)."""
    out = {}
    occ = {s: c for s, c in state}
    for pos, (y, t) in enumerate(state):
        for (x, s, amp) in terms_by_q.get((y, t), ()):
            if x in occ: continue
            # records strictly between y and x
            lo, hi = (y, x) if y < x else (x, y)
            between = sum(1 for (z, _) in state if lo < z < hi)
            sign = -1 if (fermion and between % 2) else 1
            new = [(z, c) for (z, c) in state if z != y] + [(x, s)]
            new.sort()
            new = tuple(new)
            out[new] = out.get(new, Z) + amp * sign
    return out

def index_terms(terms):
    d = {}
    for (p, q, a) in terms:
        d.setdefault(q, []).append((p[0], p[1], a))
    return d

def perm_sign(seq):
    """sign of the permutation sorting seq (distinct entries)."""
    sgn = 1
    seq = list(seq)
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]: sgn = -sgn
    return sgn

def apply_W(state, site_map, U, fermion):
    """W = Gamma(site_map x U): record (x,s) -> sum_s' U[s'][s] (site_map[x], s').  returns dict."""
    N = len(state)
    newsites = [site_map[z] for (z, _) in state]
    sgn = perm_sign(newsites) if fermion else 1
    order = sorted(range(N), key=lambda i: newsites[i])
    out = {}
    # expand coins
    for coins in itertools.product((0, 1), repeat=N):
        amp = ONE
        for k in range(N):
            amp = amp * U[coins[k]][state[k][1]]
            if amp.iszero(): break
        if amp.iszero(): continue
        st = tuple((newsites[i], coins[i]) for i in order)
        out[st] = out.get(st, Z) + amp * sgn
    return out

def vec_add(d, k, v):
    d[k] = d.get(k, Z) + v

def apply_to_vec(fn, vec):
    out = {}
    for st, a in vec.items():
        for st2, b in fn(st).items():
            vec_add(out, st2, a * b)
    return {k: v for k, v in out.items() if not v.iszero()}

# =====================================================================================
#  check.py body
# =====================================================================================
import sys, time, random
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import ZZ_I
import scipy.sparse as sps
import scipy.sparse.linalg as spl

T0 = time.time()
PASS = 0; FAIL = 0
def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1; print("PASS %s %s" % (name, detail))
    else:
        FAIL += 1; print("FAIL %s %s" % (name, detail))
    sys.stdout.flush()

def hdr(s): print("# " + s); sys.stdout.flush()

I2 = gmat([[1, 0], [0, 1]])

# ---------------------------------------------------------------- spinor rotation group (24 proper cubic rotations)
def dag(M): return [[M[j][i].conj() for j in range(2)] for i in range(2)]
def scal(M, c): return [[M[i][j] * c for j in range(2)] for i in range(2)]
def inv2(M):
    D = mm2(dag(M), M); c = D[0][0]
    assert D[0][1].iszero() and D[1][0].iszero() and D[1][1] == c
    return scal(dag(M), c.inv())
def R_of(U):
    Ui = inv2(U)
    R = [[None] * 3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            M = mm2(mm2(U, SIG[b]), Ui)
            T = mm2(SIG[a], M); tr = T[0][0] + T[1][1]
            assert tr.b == 0
            R[a][b] = tr.a / 2
    return R
def rkey(R): return tuple(tuple(r) for r in R)
Uz90 = gmat([[G(1, -1), 0], [0, G(1, 1)]]); Ux90 = gmat([[1, G(0, -1)], [G(0, -1), 1]])
ROT = {}
_fr = [I2]
while _fr:
    U = _fr.pop(); k = rkey(R_of(U))
    if k in ROT: continue
    ROT[k] = U
    for g in (Uz90, Ux90): _fr.append(mm2(g, U))

def matmul3(A, B): return [[sum((A[i][k] * B[k][j] for k in range(3)), Fr(0)) for j in range(3)] for i in range(3)]
def tr3(A): return [[A[j][i] for j in range(3)] for i in range(3)]
def Fg(F): return [[x if isinstance(x, G) else G(x) for x in r] for r in F]
def pad3(F2):
    return [[Fr(F2[a][b]) if a < len(F2) and b < len(F2) else Fr(0) for b in range(3)] for a in range(3)]

def site_map(graph, R):
    nd = len(graph.dims); Ri = [[int(R[a][b]) for b in range(3)] for a in range(3)]
    mp = {}
    for x in graph.sites:
        if graph.periodic:
            y = tuple(sum(Ri[a][b] * x[b] for b in range(nd)) % graph.dims[a] for a in range(nd))
        else:
            c = [2 * xi - 1 for xi in x]
            yy = [sum(Ri[a][b] * c[b] for b in range(nd)) for a in range(nd)]
            y = tuple((v + 1) // 2 for v in yy)
        mp[graph.idx[x]] = graph.idx[y]
    return mp

HALF = G(Fr(1, 2))
def terms_for(graph, F3): return one_body(graph, Fg(F3), HALF)

# ---------------------------------------------------------------- single-particle covariance
def single_cov(graph, F3, rots):
    h = terms_for(graph, F3); byq = {}
    for p, q, a in h: byq.setdefault(q, []).append((p, a))
    def app(tl, vec):
        bq = {}
        for p, q, a in tl: bq.setdefault(q, []).append((p, a))
        out = {}
        for q, v in vec.items():
            for p, a in bq.get(q, ()): out[p] = out.get(p, Z) + a * v
        return {k: v for k, v in out.items() if not v.iszero()}
    def W1(mp, U, vec):
        out = {}
        for (x, s), v in vec.items():
            for s2 in range(2):
                c = U[s2][s]
                if c.iszero(): continue
                k = (mp[x], s2); out[k] = out.get(k, Z) + c * v
        return {k: v for k, v in out.items() if not v.iszero()}
    ok = True
    for (R, U) in rots:
        Rf = [[Fr(v) for v in r] for r in R]
        Fp = matmul3(matmul3(Rf, F3), tr3(Rf))
        hp = terms_for(graph, Fp); mp = site_map(graph, R)
        for p in range(graph.n):
            for s in range(2):
                e = {(p, s): ONE}
                if W1(mp, U, app(h, e)) != app(hp, W1(mp, U, e)): ok = False
    return ok

# ---------------------------------------------------------------- many-body covariance
def many_cov(graph, F3, N, fermion, rots):
    n = graph.n; B = basis(n, N)
    byq = index_terms(terms_for(graph, F3))
    for (R, U) in rots:
        Rf = [[Fr(v) for v in r] for r in R]
        Fp = matmul3(matmul3(Rf, F3), tr3(Rf))
        byqp = index_terms(terms_for(graph, Fp)); mp = site_map(graph, R)
        for st in B:
            lhs = apply_to_vec(lambda s: apply_W(s, mp, U, fermion), apply_h(st, byq, fermion, n))
            rhs = apply_to_vec(lambda s: apply_h(s, byqp, fermion, n), apply_W(st, mp, U, fermion))
            if lhs != rhs: return False
    return True

# ---------------------------------------------------------------- sectors, characteristic polynomial, root isolation
def sector_matrix(graph, F3, N, fermion, ops, chars):
    byq = index_terms(terms_for(graph, F3)); n = graph.n
    B = basis(n, N); seen = set(); reps = []; vs = {}
    for r in B:
        if r in seen: continue
        orb = set(); v = {}
        for (lab, mp, U) in ops:
            for st, a in apply_W(r, mp, U, fermion).items():
                orb.add(st); v[st] = v.get(st, Z) + a * chars[lab].conj()
        seen |= orb
        v = {k: x for k, x in v.items() if not x.iszero()}
        if v:
            rep = min(v.keys()); reps.append(rep); vs[rep] = v
    m = len(reps); M = [[Z] * m for _ in range(m)]
    for c, r in enumerate(reps):
        Hv = {}
        for st, a in vs[r].items():
            for st2, b in apply_h(st, byq, fermion, n).items(): Hv[st2] = Hv.get(st2, Z) + a * b
        Hv = {k: x for k, x in Hv.items() if not x.iszero()}
        rec = {}
        for rr, r2 in enumerate(reps):
            coef = Hv.get(r2, Z) / vs[r2][r2]; M[rr][c] = coef
            for st, a in vs[r2].items(): rec[st] = rec.get(st, Z) + coef * a
        rec = {k: x for k, x in rec.items() if not x.iszero()}
        assert rec == Hv, "sector not closed under H (symmetry error)"
    return M

def charpoly_of(M):
    m = len(M); D = 1
    for row in M:
        for z in row:
            D = sp.ilcm(D, z.a.denominator); D = sp.ilcm(D, z.b.denominator)
    rows = [[ZZ_I(int(z.a * D), int(z.b * D)) for z in row] for row in M]
    cp = DomainMatrix(rows, (m, m), ZZ_I).charpoly()
    co = []
    for c in cp:
        assert c.y == 0; co.append(int(c.x))
    x = sp.symbols('x')
    return sp.Poly(co, x), D

EPS = sp.Rational(1, 10 ** 30)
def lowest_interval(P, D):
    iv = P.sqf_part().intervals(eps=EPS)
    (lo, hi), _ = iv[0]
    return Fr(int(lo.p), int(lo.q)) / D, Fr(int(hi.p), int(hi.q)) / D

def translation_specs(graph, L):
    w = [ONE, I_, G(-1), G(0, -1)]
    ops = []
    for t1 in range(L):
        for t2 in range(L):
            mp = {graph.idx[x]: graph.idx[((x[0] + t1) % L, (x[1] + t2) % L)] for x in graph.sites}
            ops.append(((t1, t2), mp, I2))
    specs = []
    for k1 in range(L):
        for k2 in range(L):
            specs.append((ops, {(t1, t2): w[(k1 * t1 + k2 * t2) % 4] for t1 in range(L) for t2 in range(L)}))
    return specs

def q3_specs(graph):
    ident = {i: i for i in range(graph.n)}
    mpW = {graph.idx[x]: graph.idx[(1 - x[0], 1 - x[1], x[2])] for x in graph.sites}
    ops = [('e', ident, I2), ('W', mpW, SIG[2])]
    return [(ops, {'e': ONE, 'W': ONE}), (ops, {'e': ONE, 'W': G(-1)})]

def ground_interval(graph, F3, N, fermion, specs):
    """exact isolating interval (Fractions) for the lowest eigenvalue of the hard-core N-record generator, plus total dimension."""
    best = None; dim = 0; polys = []
    for (ops, chars) in specs:
        M = sector_matrix(graph, F3, N, fermion, ops, chars)
        if not M: continue
        dim += len(M)
        P, D = charpoly_of(M); polys.append((P, D))
        lo, hi = lowest_interval(P, D)
        best = (lo, hi) if best is None else (min(best[0], lo), min(best[1], hi))
    return best, dim, polys

def fr(x): return float(x)

# =====================================================================================
hdr("S0 setting: H_F = sum_{j,a} F[a][j] sigma_a (-i/2)(|x><x+e_j| - h.c.-type hop), hard-core compression (<=1 record/site),")
hdr("   fermionic (order sign) and bosonic (no sign) composition; F = frame E^j_a; metric g^{-1} = F^T F; volume per site = 1/det F.")
chk("S0.rot-group", len(ROT) == 24, "24 proper cubic rotations with exact (unnormalised) SU(2) lifts")

# ---------------------------------------------------------------- S1 group average
hdr("S1 symbolic group average over the 24 proper cubic rotations: (1/24) sum_R R F R^T = (tr F / 3) 1 for a generic 3x3 F")
Fs = sp.Matrix(3, 3, sp.symbols('f11 f12 f13 f21 f22 f23 f31 f32 f33'))
acc = sp.zeros(3, 3)
for k in ROT:
    Rm = sp.Matrix(3, 3, [sp.Rational(v.numerator, v.denominator) for r in k for v in r])
    acc += Rm * Fs * Rm.T
acc = (acc / 24).applyfunc(sp.expand)
chk("S1.avg3", acc == sp.expand(Fs.trace() / 3) * sp.eye(3), "avg_R R F R^T = (trF/3) I  (exact, symbolic)")
rot2 = [k for k in ROT if k[2] == (0, 0, 1) and k[0][2] == 0 and k[1][2] == 0]
chk("S1.c4", len(rot2) == 4, "4 in-plane rotations (C4 about axis 3)")
F2 = sp.Matrix(2, 2, sp.symbols('g11 g12 g21 g22')); acc2 = sp.zeros(2, 2)
for k in rot2:
    Rm = sp.Matrix(2, 2, [sp.Rational(k[a][b].numerator, k[a][b].denominator) for a in range(2) for b in range(2)])
    acc2 += Rm * F2 * Rm.T
acc2 = (acc2 / 4).applyfunc(sp.expand)
a_ = (F2[0, 0] + F2[1, 1]) / 2; b_ = (F2[1, 0] - F2[0, 1]) / 2
chk("S1.avgC4", acc2 == sp.Matrix([[a_, -b_], [b_, a_]]).applyfunc(sp.expand),
    "plane: avg over C4 = a*1 + b*J, a=trF/2, b=(F21-F12)/2; b=0 for symmetric F")
# AM-GM facts used (exact): tr S >= d for S>0 symmetric with det 1  -> checked on eigenvalue form by sympy
u1, u2, u3 = sp.symbols('u1 u2 u3', positive=True)
amgm = sp.expand((u1 ** 3 + u2 ** 3 + u3 ** 3 - 3 * u1 * u2 * u3) - (u1 + u2 + u3) * ((u1 - u2) ** 2 + (u2 - u3) ** 2 + (u3 - u1) ** 2) / 2)
chk("S1.amgm-id", amgm == 0, "u1^3+u2^3+u3^3-3u1u2u3 = (u1+u2+u3)*sum of squared differences/2  (=> AM-GM for cubes)")

# ---------------------------------------------------------------- S2 single-particle covariance
hdr("S2 single-particle covariance W h_F = h_{R F R^T} W, W = (x -> Rx) x U_R, generic non-symmetric rational F")
Fgen = [[Fr(1), Fr(2), Fr(-1)], [Fr(0), Fr(1), Fr(3)], [Fr(2), Fr(-1), Fr(1)]]
rots_all = [(k, ROT[k]) for k in ROT]
for nm, g in (("cube Q3 (2x2x2 bond-once)", Graph((2, 2, 2), False, 3)), ("torus 3x3x3", Graph((3, 3, 3), True, 3)), ("torus 4x4x4", Graph((4, 4, 4), True, 3))):
    chk("S2.cov-" + nm, single_cov(g, Fgen, rots_all), "all 24 rotations, exact")
gp4 = Graph((4, 4), True, 3)
F2gen = pad3([[Fr(1), Fr(2)], [Fr(-1), Fr(3)]])
chk("S2.cov-plane4x4", single_cov(gp4, F2gen, [(k, ROT[k]) for k in rot2]), "4 in-plane rotations, exact (plane walk uses sigma_1, sigma_2)")

# ---------------------------------------------------------------- S3 many-body covariance
hdr("S3 many-body covariance: W H_F = H_{R F R^T} W on the hard-core N-record space (both composition rules)")
sel = []
for k in ROT:
    if k in rot2 or True: sel.append((k, ROT[k]))
gq3 = Graph((2, 2, 2), False, 3)
for N in (2,):
    for ferm in (True, False):
        chk("S3.Q3-N%d-%s" % (N, "F" if ferm else "B"), many_cov(gq3, Fgen, N, ferm, sel), "all 24 rotations, all %d basis states, exact" % len(basis(8, N)))
# a representative subset for N=3 (z90, x90, a face-diagonal pi rotation, a 3-fold rotation)
def pick(pred):
    for k in ROT:
        if pred(k): return (k, ROT[k])
sub = [pick(lambda k: k == rkey(R_of(Uz90))), pick(lambda k: k == rkey(R_of(Ux90))),
       pick(lambda k: k == rkey(R_of(mm2(Uz90, Ux90)))),
       pick(lambda k: k[0] == (0, 0, 1) and k[1] == (1, 0, 0)) or pick(lambda k: k[0] == (0, 1, 0) and k[1] == (0, 0, 1)),
       pick(lambda k: k[0] == (0, 1, 0) and k[1] == (1, 0, 0))]
sub = [s for s in sub if s]
for ferm in (True, False):
    chk("S3.Q3-N3-%s" % ("F" if ferm else "B"), many_cov(gq3, Fgen, 3, ferm, sub), "%d rotations (incl. 90-degree, 3-fold, face-diagonal pi), 448 basis states, exact" % len(sub))
for ferm in (True, False):
    chk("S3.plane4x4-N2-%s" % ("F" if ferm else "B"), many_cov(gp4, F2gen, 2, ferm, [(k, ROT[k]) for k in rot2]), "4 in-plane rotations, 480 basis states, exact")

# ---------------------------------------------------------------- S4 trace, nonzero, periodic L=2
hdr("S4 tracelessness and nonvanishing of the compressed generator; the strictly periodic 2x2x2 torus has H = 0")
def sector_stats(graph, F3, N, fermion):
    byq = index_terms(terms_for(graph, F3)); n = graph.n; nz = 0; diag = 0
    for st in basis(n, N):
        for st2, a in apply_h(st, byq, fermion, n).items():
            if not a.iszero():
                nz += 1
                if st2 == st: diag += 1
    return nz, diag
F1 = [[Fr(int(a == j)) for j in range(3)] for a in range(3)]
for N in range(0, 9):
    for ferm in (True, False):
        nz, dg = sector_stats(gq3, F1, N, ferm)
        want_zero = (N == 0 or N == 8)
        chk("S4.Q3-N%d-%s" % (N, "F" if ferm else "B"), dg == 0 and ((nz == 0) == want_zero),
            "diagonal entries=%d, nonzero entries=%d (zero iff N in {0,8})" % (dg, nz))
for N in (0, 1, 2, 3, 4):
    nz, dg = sector_stats(Graph((4, 4), True, 3), pad3([[1, 0], [0, 1]]), N, True) if N <= 2 else (None, None)
    if nz is None: continue
    chk("S4.plane4x4-N%d" % N, dg == 0 and (nz == 0) == (N == 0), "diagonal entries=%d, nonzero entries=%d" % (dg, nz))
g2 = Graph((2, 2, 2), True, 3)
h2 = terms_for(g2, F1)
chk("S4.periodic-2x2x2-one-body-zero", len(h2) == 0, "strictly periodic 2x2x2: T=T^dagger so every hop term cancels; H = 0 for EVERY frame")
Fgen_all = Fgen
chk("S4.periodic-2x2x2-any-frame", len(terms_for(g2, Fgen_all)) == 0, "also for the generic non-symmetric frame")
nzp, dgp = sector_stats(g2, F1, 2, True)
chk("S4.periodic-2x2x2-N2", nzp == 0, "N=2 fermionic many-body matrix entries: %d" % nzp)

# ---------------------------------------------------------------- S5 exact ground energies (characteristic polynomials + root isolation)
hdr("S5 exact lowest eigenvalue of the hard-core generator (sector-reduced characteristic polynomial, sympy exact real-root isolation, width 1e-30)")
def cF(F, d):
    """c(F) = (sum of singular values of F)/d, exact; returns (sympy expr, Fraction lo, Fraction hi)."""
    M = sp.Matrix(F).T * sp.Matrix(F)
    ev = M.eigenvals()
    expr = sum(m * sp.sqrt(e) for e, m in ev.items()) / d
    v = sp.N(expr, 60)
    lo = sp.Rational(v) - sp.Rational(1, 10 ** 50); hi = sp.Rational(v) + sp.Rational(1, 10 ** 50)
    return expr, Fr(int(lo.p), int(lo.q)), Fr(int(hi.p), int(hi.q))

def run_family(tag, graph, d, specs, frames, Ns, signs):
    res = {}
    for N in Ns:
        for ferm in signs:
            E0, dim, _ = ground_interval(graph, pad3(frames['I']) if d == 2 else frames['I'], N, ferm, specs)
            lab = "F" if ferm else "B"
            chk("S5.%s.N%d.%s.dim" % (tag, N, lab), dim == len(basis(graph.n, N)), "sector dims sum to %d" % dim)
            chk("S5.%s.N%d.%s.equal-frame-negative" % (tag, N, lab), E0[1] < 0, "E_N(1) in [%.15f, %.15f] < 0" % (fr(E0[0]), fr(E0[1])))
            res[(N, ferm, 'I')] = E0
            for nm, F in frames.items():
                if nm == 'I' or nm == 'rot': continue
                F3 = pad3(F) if d == 2 else F
                EF, dim, _ = ground_interval(graph, F3, N, ferm, specs)
                expr, clo, chi = cF(F, d)
                strict = EF[1] < E0[0]
                bound = EF[1] < chi * E0[0]
                chk("S5.%s.N%d.%s.%s.falls" % (tag, N, lab, nm), strict, "E(F)=%.12f < E(1)=%.12f (isolating intervals disjoint)" % (fr(EF[0]), fr(E0[0])))
                chk("S5.%s.N%d.%s.%s.jensen" % (tag, N, lab, nm), bound, "E(F) < c(F)E(1), c(F)=sum sing.values/%d = %.9f -> bound %.12f" % (d, fr(clo), fr(chi * E0[0])))
                res[(N, ferm, nm)] = EF
    return res

planeG = Graph((4, 4), True, 3)
pl_frames = {'I': [[1, 0], [0, 1]], 'diag(1/2,2)': [[Fr(1, 2), 0], [0, 2]], 'shear[[1,1],[0,1]]': [[1, 1], [0, 1]], 'sym[[2,1],[1,1]]': [[2, 1], [1, 1]]}
for nm, F in pl_frames.items():
    d = sp.Matrix(F).det(); assert d == 1
pl_specs = translation_specs(planeG, 4)
t = time.time()
resP = run_family("plane4x4", planeG, 2, pl_specs, pl_frames, (1, 2), (True, False))
hdr("   plane 4x4 exact block took %.0fs" % (time.time() - t))
# closed form N=1
(E1lo, E1hi), _, _ = ground_interval(planeG, pad3([[Fr(1, 2), 0], [0, 2]]), 1, True, pl_specs)
chk("S5.plane.N1.closed-form", E1lo * E1lo >= Fr(17, 4) and E1hi * E1hi <= Fr(17, 4) + Fr(1, 10 ** 20) and E1lo <= -Fr(2061, 1000), "E_1 = -sqrt(a1^2+a2^2) = -sqrt(17)/2 for a=(1/2,2)")
# relabelling invariance: coin rotation Q F has the same sector polynomials
Qrot = [[0, -1], [1, 0]]
Fsh = [[Fr(1), Fr(1)], [Fr(0), Fr(1)]]
QF = (sp.Matrix(Qrot) * sp.Matrix(Fsh)).tolist()
QF = [[Fr(int(sp.numer(x)), int(sp.denom(x))) for x in r] for r in QF]
def norm_poly(P, D):
    x = sp.symbols('x')
    return sp.Poly(sp.expand(P.as_expr().subs(x, D * x)), x).monic()
for N in (1, 2):
    polyA = []; polyB = []
    for (ops, chars) in pl_specs:
        MA = sector_matrix(planeG, pad3(Fsh), N, True, ops, chars)
        MB = sector_matrix(planeG, pad3(QF), N, True, ops, chars)
        if not MA: continue
        polyA.append(str(norm_poly(*charpoly_of(MA)).as_expr())); polyB.append(str(norm_poly(*charpoly_of(MB)).as_expr()))
    chk("S5.plane.N%d.relabelling" % N, sorted(polyA) == sorted(polyB) and len(polyA) > 0,
        "coin rotation Q (90 deg) of the shear frame leaves every sector's characteristic polynomial unchanged (%d sectors)" % len(polyA))

cubeG = Graph((2, 2, 2), False, 3)
cu_frames = {'I': [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 'diag(1/2,1,2)': [[Fr(1, 2), 0, 0], [0, 1, 0], [0, 0, 2]],
             'shear[[1,1,0],[0,1,0],[0,0,1]]': [[1, 1, 0], [0, 1, 0], [0, 0, 1]], 'sym[[2,1,0],[1,1,0],[0,0,1]]': [[2, 1, 0], [1, 1, 0], [0, 0, 1]]}
for nm, F in cu_frames.items():
    assert sp.Matrix(F).det() == 1
cu_specs = q3_specs(cubeG)
t = time.time()
cu_frames_fr = {k: [[Fr(x) for x in r] for r in F] for k, F in cu_frames.items()}
resC = run_family("cube2x2x2", cubeG, 3, cu_specs, cu_frames_fr, (1, 2), (True, False))
hdr("   cube 2x2x2 exact block took %.0fs" % (time.time() - t))
(E1lo, E1hi), _, _ = ground_interval(cubeG, [[Fr(1, 2), 0, 0], [0, 1, 0], [0, 0, 2]], 1, True, cu_specs)
chk("S5.cube.N1.closed-form", E1hi < 0 and (4 * E1lo) ** 2 >= 21 and (4 * E1hi) ** 2 <= 21 + Fr(1, 10 ** 20), "E_1 = -(1/2)sqrt(a1^2+a2^2+a3^2) = -sqrt(21)/4 for a=(1/2,1,2)")

# ---------------------------------------------------------------- S6 cells (uniform-in-L negativity) -- exact structure + numbers
hdr("S6 cell construction: a cell is a bond-once graph (open 2x2x2 cube in 3D, open 2x2 square in the plane) whose bonds are bonds of the torus;")
hdr("   product states of cell ground states have <H> = sum of cell energies (cross-cell hops change cell numbers).")
# numeric builder (floating point; used for S6/S7 sanity only, never for a claimed exact statement)
def build_csr(graph, F3, N, fermion):
    terms = terms_for(graph, F3); byq = {}
    for (p, q, a) in terms: byq.setdefault(q, []).append((p[0], p[1], complex(float(a.a), float(a.b))))
    n = graph.n; B = basis(n, N); idx = {s: i for i, s in enumerate(B)}
    rows = []; cols = []; dat = []
    for j, st in enumerate(B):
        occ = {s for s, _ in st}
        for (y, t) in st:
            for (x, s, amp) in byq.get((y, t), ()):
                if x in occ: continue
                lo, hi = (y, x) if y < x else (x, y)
                between = sum(1 for (z, _) in st if lo < z < hi)
                sg = -1.0 if (fermion and between % 2) else 1.0
                new = tuple(sorted([(z, c) for (z, c) in st if z != y] + [(x, s)]))
                rows.append(idx[new]); cols.append(j); dat.append(amp * sg)
    m = len(B)
    return sps.csr_matrix((dat, (rows, cols)), shape=(m, m), dtype=complex)

def lam_min(Hm):
    m = Hm.shape[0]
    if m <= 2500:
        return float(np.linalg.eigvalsh(Hm.toarray())[0])
    return float(spl.eigsh(Hm, k=1, which='SA', tol=1e-12, return_eigenvectors=False)[0])

def herm_err(Hm): return abs(Hm - Hm.conj().T).max() if Hm.nnz else 0.0

cellC = Graph((2, 2, 2), False, 3)
epsC = {}
for k in range(1, 8):
    Hm = build_csr(cellC, F1, k, True); epsC[k] = -lam_min(Hm)
    chk("S6.cube-cell-k%d" % k, epsC[k] > 1e-9 and herm_err(Hm) < 1e-12, "cell ground energy -eps_k = %.10f (<0, hermitian)" % (-epsC[k]))
cellP = Graph((2, 2), False, 3)
epsP = {}
FP1 = pad3([[1, 0], [0, 1]])
for k in range(1, 4):
    Hm = build_csr(cellP, FP1, k, True); epsP[k] = -lam_min(Hm)
    chk("S6.square-cell-k%d" % k, epsP[k] > 1e-9, "cell ground energy -eps_k = %.10f (<0)" % (-epsP[k]))
# the cell bound against the exact torus value: E_2(1) on the 4x4 torus <= 2*E_cell(1)
E2 = resP[(2, True, 'I')]
chk("S6.plane-N2-cell-bound", fr(E2[1]) <= -2 * epsP[1] + 1e-12, "exact E_2(1)<=%.10f  <=  2*E_cell(k=1) = %.10f" % (fr(E2[1]), -2 * epsP[1]))
E2b = resP[(2, False, 'I')]
chk("S6.plane-N2-cell-bound-B", fr(E2b[1]) <= -2 * epsP[1] + 1e-12, "bosonic: E_2(1)<=%.10f  <=  %.10f" % (fr(E2b[1]), -2 * epsP[1]))

# ---------------------------------------------------------------- S7 floating-point sanity of the full inequality chain (NOT exact)
hdr("S7 floating-point sanity (not exact): E_N(F) <= c(F) E_N(1) < E_N(1) for random frames, all N on the cube graph, N<=4 on the 4x4 plane")
rng = random.Random(20261026)
def rand_frame(d):
    while True:
        F = [[Fr(rng.randint(-10, 10), 5) for _ in range(d)] for _ in range(d)]
        if sp.Matrix(F).det() > Fr(1, 4): return F
def cF_float(F):
    sv = np.linalg.svd(np.array(F, dtype=float), compute_uv=False)
    return float(sv.sum() / len(F))
def det_float(F): return float(np.linalg.det(np.array(F, dtype=float)))

ok_all = True; worst = -1e9
for N in range(1, 8):
    for ferm in (True, False):
        H0 = build_csr(cellC, F1, N, ferm); E0 = lam_min(H0)
        for _ in range(3):
            F = rand_frame(3); Fp = [[Fr(x) for x in r] for r in F]
            HF = build_csr(cellC, Fp, N, ferm); EF = lam_min(HF)
            c = cF_float(F); lam = det_float(F) ** (1 / 3)
            marg = EF - c * E0                    # must be <= 0
            worst = max(worst, marg)
            if not (marg <= 1e-9 and EF / lam < E0 - 1e-12 * 0): ok_all = False
chk("S7.cube-graph-all-N", ok_all, "N=1..7, both signs, 3 random (non-symmetric allowed) frames each: E(F)<=c(F)E(1) and E(F)/det^(1/3)<E(1); largest E(F)-c(F)E(1) = %.3e" % worst)

ok_all = True; worst = -1e9
t = time.time()
for N in range(1, 5):
    for ferm in ((True, False) if N <= 3 else (True,)):
        H0 = build_csr(planeG, FP1, N, ferm); E0 = lam_min(H0)
        for _ in range(2):
            F = rand_frame(2); Fp = pad3([[Fr(x) for x in r] for r in F])
            HF = build_csr(planeG, Fp, N, ferm); EF = lam_min(HF)
            c = cF_float(F); lam = det_float(F) ** 0.5
            marg = EF - c * E0; worst = max(worst, marg)
            if not (marg <= 1e-8 and EF / lam < E0): ok_all = False
chk("S7.plane4x4-N1-4", ok_all, "N=1..4 (N=4 fermionic only), random frames: E(F)<=c(F)E(1), E(F)/det^(1/2)<E(1); largest E(F)-c(F)E(1) = %.3e; %.0fs" % (worst, time.time() - t))

# ---------------------------------------------------------------- S8 free sea (same argument): off-diagonal shear at every size
hdr("S8 same argument for the free sea (block 155's left-open 'off-diagonal shears at every size'): <|F s|> >= c(F) <|s|>, floating point on zone grids")
def free_ok(F, L, d):
    ks = 2 * np.pi * np.arange(L) / L
    grids = np.meshgrid(*([np.sin(ks)] * d), indexing='ij')
    s = np.stack([g.ravel() for g in grids], axis=0)
    Fa = np.array(F, dtype=float)
    lhs = np.sqrt(((Fa @ s) ** 2).sum(axis=0)).mean(); rhs = cF_float(F) * np.sqrt((s ** 2).sum(axis=0)).mean()
    return lhs, rhs
ok = True; mn = 1e9
for d, L in ((2, 4), (2, 6), (2, 40), (3, 4), (3, 6), (3, 24)):
    for _ in range(25):
        F = rand_frame(d); lhs, rhs = free_ok(F, L, d)
        mn = min(mn, lhs - rhs)
        if lhs < rhs - 1e-12: ok = False
chk("S8.free-sea", ok, "free-sea energy per site -<|Fs|> <= c(F)*(-<|s|>) on 2D/3D grids L=4..40, 150 random frames (min slack %.3e)" % mn)

# ---------------------------------------------------------------- final
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
print("runtime %.0fs" % (time.time() - T0))
if FAIL == 0:
    print("HIT: for every cubic L x L x L torus (L>=3), L x L torus, and the bond-once 2x2x2 cube, every record number 0<N<n, both composition signs, and every uniform frame F (3x3, or 2x2 in the plane) with det F=1, the hard-core ground energy satisfies E_N(F) <= (tr sqrt(F^T F)/d) E_N(1) < E_N(1) unless F^T F = 1 (proof in ATTEMPT.md: concavity in F + cubic-rotation averaging + AM-GM); uniform-in-L cell bound for L even")
    print("SUMMARY: PROVED (scope in ATTEMPT.md): under one record per site the ground energy falls under every volume-preserving uniform frame change at every N, both exchange signs, via concavity plus rotation averaging; exact finite spectra on the 4x4 plane and 2x2x2 cube agree, and the strictly periodic 2x2x2 torus has H=0.")
else:
    print("SUMMARY: ROUTE FAILS AT a finite check (see FAIL lines)")
sys.exit(0 if FAIL == 0 else 1)
