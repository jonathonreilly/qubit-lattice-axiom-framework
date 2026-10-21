"""C4c-02: exact checks of the ingredients of the Vertex Lemma (NOTE.md Lemma V) and its
corollary, by routes independent of the proof text.

(a) one-site algebra (sympy, exact): commutants of sigma^z, sigma^+, {sigma^+,sigma^-}; a unitary
    whose one-site Schmidt span lies in span{1, sigma^+} has zero sigma^+ part.
(b) geometry (exhaustive on all 255 nonempty subsets of the unit cube, sampled on the 27-cell):
    for every vertex v of conv(S) there is t != 0 with S cap (S+t) = {v}; and the iterated
    single-overlap forcing rule.
(c) two-site U(1) gate g (sympy, exact, generic entries): [g_01, g_12] = 0 together with
    unitarity forces the |01>,|10> block to be diagonal (independent of (a),(b)).
(d) single commuting layer freeze (numerical sanity on a ring, non-U(1) example): support of
    alpha^n(X_0) for alpha = Ad prod exp(i th Z X Z) stays bounded.
"""
import itertools, random
import numpy as np
import sympy as sp
from c4c_common import check, total

# ---------- (a)
a, b, c, d = sp.symbols('a b c d')
Xg = sp.Matrix([[a, b], [c, d]])
sz = sp.Matrix([[1, 0], [0, -1]]); sp_ = sp.Matrix([[0, 0], [1, 0]]); sm = sp_.T  # |1>=magnon=index1
def comm_sol(*ops):
    eqs = []
    for o in ops:
        eqs += list(o * Xg - Xg * o)
    return sp.solve(eqs, [a, b, c, d], dict=True)
s1 = comm_sol(sz); s2 = comm_sol(sp_); s3 = comm_sol(sp_, sm)
print("commutant(sz):", s1, " commutant(s+):", s2, " commutant(s+,s-):", s3)
gen = lambda sl: [sp.simplify(Xg.subs(x)) for x in sl]
check("(a1) commutant of sigma^z = diagonal", len(s1) == 1 and gen(s1)[0][0, 1] == 0 and gen(s1)[0][1, 0] == 0)
G2 = gen(s2)[0]
check("(a2) commutant of sigma^+ = span{1, sigma^+} (lower-left entry free, diag equal)",
      len(s2) == 1 and G2[0, 1] == 0 and sp.simplify(G2[0, 0] - G2[1, 1]) == 0, str(G2))
G3 = gen(s3)[0]
check("(a3) commutant of {sigma^+, sigma^-} = scalars",
      len(s3) == 1 and G3[0, 1] == 0 and G3[1, 0] == 0 and sp.simplify(G3[0, 0] - G3[1, 1]) == 0, str(G3))
# unitary g = G1 (x) 1 + Gp (x) s+ on (rest) (x) site; check sigma^z coefficient of g^dag g
m = 2
G1 = sp.Matrix(m, m, sp.symbols('g0:4')); Gp = sp.Matrix(m, m, sp.symbols('p0:4'))
g = sp.kronecker_product(G1, sp.eye(2)) + sp.kronecker_product(Gp, sp_)
gg = (g.H * g)
# project onto rest (x) sigma^z: coefficient = (1/2) tr_site[(1 (x) sz) gg]
coef = sp.zeros(m, m)
for i in range(m):
    for j in range(m):
        coef[i, j] = sp.simplify((gg[2 * i, 2 * j] - gg[2 * i + 1, 2 * j + 1]) / 2)
expect = (Gp.H * Gp) / 2
check("(a4) sigma^z-coefficient of g^dag g equals +Gp^dag Gp/2 (so unitarity forces Gp=0)",
      sp.simplify(coef - expect) == sp.zeros(m, m) or sp.simplify(coef + expect) == sp.zeros(m, m),
      f"coef={coef}")

# ---------- (b)
def vertices(S):
    """exposed points of conv(S) for S subset Z^3 small: v is a vertex iff some linear functional
    has v as unique maximiser; test by LP-free check: v not in conv(S\\{v}) (scipy linprog)."""
    from scipy.optimize import linprog
    out = []
    for v in S:
        others = [s for s in S if s != v]
        if not others:
            out.append(v); continue
        A = np.array(others, float).T; A = np.vstack([A, np.ones(len(others))])
        bb = np.array(list(v) + [1.0])
        r = linprog(np.zeros(len(others)), A_eq=A, b_eq=bb, bounds=[(0, None)] * len(others))
        if not r.success:
            out.append(v)
    return out

def single_overlaps(S):
    Sset = set(S); res = {}
    for p in S:
        for q in S:
            t = tuple(np.subtract(p, q))
            if t == (0, 0, 0):
                continue
            ov = Sset & set(tuple(np.add(s, t)) for s in S)
            if len(ov) == 1:
                res.setdefault(next(iter(ov)), set()).add(t)
    return res

cube = list(itertools.product((0, 1), repeat=3))
bad = 0; allvert = 0
for k in range(1, 9):
    for S in itertools.combinations(cube, k):
        S = list(S)
        V = vertices(S)
        if len(V) == len(S):
            allvert += 1
        so = single_overlaps(S)
        if len(S) > 1 and any(v not in so for v in V):
            bad += 1
check("(b1) every subset of the unit cube is in convex position", allvert == 255, f"{allvert}/255")
check("(b2) every vertex of every cube subset (|S|>1) is a single-site overlap S cap (S+t)", bad == 0)

cell = list(itertools.product((-1, 0, 1), repeat=3))
random.seed(7)
nbad = 0; nforced_all = 0; samples = 300; unforced_hist = {}
for _ in range(samples):
    k = random.randint(2, 12)
    S = random.sample(cell, k)
    V = vertices(S); so = single_overlaps(S)
    if any(v not in so for v in V):
        nbad += 1
    forced = set(so.keys())
    for s, ts in so.items():
        for t in ts:
            forced.add(tuple(np.subtract(s, t)))
    nun = len(S) - len(forced)
    unforced_hist[nun] = unforced_hist.get(nun, 0) + 1
    if nun == 0:
        nforced_all += 1
check("(b3) sampled 27-cell supports: every conv-hull vertex is a single-site overlap",
      nbad == 0, f"{samples} samples")
print("     sampled supports: #sites NOT forced diagonal by single-overlap rule -> count:",
      dict(sorted(unforced_hist.items())))

# ---------- (c) two-site gate, generic symbols, chain 0-1-2
p00, p11, u11, u12, u21, u22 = sp.symbols('p00 p11 u11 u12 u21 u22')
g2 = sp.diag(p00, sp.Matrix([[u11, u12], [u21, u22]]), p11)   # basis 00,01,10,11
I2 = sp.eye(2)
gA = sp.kronecker_product(g2, I2); gB = sp.kronecker_product(I2, g2)
C = (gA * gB - gB * gA).applyfunc(sp.expand)
ent = set(e for e in C if e != 0)
print("     nonzero commutator entries:", ent)
# entries that are monomials u12*u21-type or u12*(...): show that each solution has u12=u21=0 or
# violates unitarity of the 2x2 block.
sols = sp.solve(list(ent), [u12, u21, u11, u22, p00, p11], dict=True)
print("     solutions:", sols)
def ok_sol(sl):
    U = sp.Matrix([[u11, u12], [u21, u22]]).subs(sl)
    P = [sp.sympify(p00).subs(sl), sp.sympify(p11).subs(sl)]
    offd = (U[0, 1] == 0 and U[1, 0] == 0)
    # a solution with an off-diagonal entry must kill p00 or p11 or a full 2x2 row -> non-unitary
    nonunitary = any(x == 0 for x in P) or U.det() == 0
    return offd or nonunitary
check("(c) two-site U(1) gate with commuting chain translates: block diagonal or non-unitary",
      all(ok_sol(sl) for sl in sols), f"{len(sols)} solution branches")

# ---------- (d) single commuting layer freeze sanity (ring L=10, ZXZ layer, th=0.37)
L = 10
X = np.array([[0, 1], [1, 0]], complex); Z = np.diag([1, -1]).astype(complex)
def op(dd):
    mm = np.array([[1]], complex)
    for i in range(L):
        mm = np.kron(mm, dd.get(i, np.eye(2)))
    return mm
th = 0.37
U = np.eye(2 ** L, dtype=complex)
for j in range(L):
    P = op({(j - 1) % L: Z, j: X, (j + 1) % L: Z})
    U = (np.cos(th) * np.eye(2 ** L) + 1j * np.sin(th) * P) @ U
A = op({0: X}); supp = []
An = A.copy()
def support(M):
    s = []
    T = M.reshape([2] * (2 * L))
    for i in range(L):
        Tm = np.moveaxis(T, [i, L + i], [0, 1]).reshape(2, 2, -1)
        # traceless part on site i
        r = Tm - np.einsum('aa...->...', Tm)[None, None] * np.eye(2)[:, :, None] / 2
        if np.abs(r).max() > 1e-9:
            s.append(i)
    return s
for n in range(1, 13):
    An = U @ An @ U.conj().T
    supp.append(len(support(An)))
print("     |supp alpha^n(X_0)|, n=1..12:", supp)
check("(d) single commuting layer: support bounded uniformly in n (<= |S-S| = 5)", max(supp) <= 5)
total()
