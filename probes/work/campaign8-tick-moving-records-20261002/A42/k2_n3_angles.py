"""A42 check k2: step N3 for two neighbour support axes at angle g.

x and z = x+e_a+e_b share m1 = x+e_a and m2 = x+e_b.
T_x is a unital *-subalgebra of span{1,A_m1} (x) span{1,B_m2},
T_z is a unital *-subalgebra of span{1,B_m1} (x) span{1,A_m2},
with A = sz and B = cos(g) sz + sin(g) sx.  Each is spanned by block sums of the
four atoms P^A_i (x) P^B_j (a set partition, 15 of them).  Both must have
nontrivial support on both sites (the branch assumption).

Exact part: with t = tan(g/2) (Weierstrass), every commutator entry is a
rational function of t; a pair commutes at angle g iff all numerators vanish at
t.  The gcd of the numerators gives the exact set of angles for each pair.
Numeric part: direct numpy test at sample angles.
"""
import sys, itertools, numpy as np, sympy as sp

def partitions(lst):
    if not lst:
        yield []
        return
    first, rest = lst[0], lst[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p

ATOMS = [(i, j) for i in range(2) for j in range(2)]
PARTS = list(partitions(ATOMS)); assert len(PARTS) == 15
def nontrivial_both(part):
    s1 = any(((1 - i, j) not in blk) for blk in part for (i, j) in blk)
    s2 = any(((i, 1 - j) not in blk) for blk in part for (i, j) in blk)
    return s1 and s2
good = [p for p in PARTS if nontrivial_both(p)]
print('partitions with nontrivial support on both sites:', len(good), flush=True)

# ---- numeric ----
def proj(M):
    return [(np.eye(2) + M) / 2, (np.eye(2) - M) / 2]
def blocks(part, P1, P2):
    return [sum(np.kron(P1[i], P2[j]) for (i, j) in blk) for blk in part]
def survivors(gv):
    A = np.diag([1., -1.]); B = np.cos(gv) * A + np.sin(gv) * np.array([[0., 1.], [1., 0.]])
    PA, PB = proj(A), proj(B)
    out = []
    for p in good:
        Tx = blocks(p, PA, PB)
        for q in good:
            Tz = blocks(q, PB, PA)
            if all(np.abs(X @ Y - Y @ X).max() < 1e-12 for X in Tx for Y in Tz):
                out.append((p, q))
    return out
for name, gv in [('parallel g=0', 0.0), ('perpendicular g=pi/2', np.pi / 2), ('g=pi/3', np.pi / 3),
                 ('g=2pi/3 (axis d-branch, cos=-1/2)', 2 * np.pi / 3), ('g=acos(1/3)', np.arccos(1 / 3)),
                 ('g=1 rad', 1.0), ('g=pi/4', np.pi / 4), ('g=0.123', 0.123)]:
    sv = survivors(gv)
    print(f'{name:36s} commuting pairs: {len(sv)}', flush=True)
    if 0 < len(sv) <= 2:
        for p, q in sv:
            print('    T_x blocks', p, '| T_z blocks', q)

# ---- exact (Weierstrass) ----
t = sp.symbols('t')
c = (1 - t**2) / (1 + t**2); s = 2 * t / (1 + t**2)
A = sp.Matrix([[1, 0], [0, -1]]); B = c * A + s * sp.Matrix([[0, 1], [1, 0]])
I2 = sp.eye(2)
PA = [(I2 + A) / 2, (I2 - A) / 2]; PB = [(I2 + B) / 2, (I2 - B) / 2]
kron = sp.kronecker_product
def sblocks(part, P1, P2):
    return [sum((kron(P1[i], P2[j]) for (i, j) in blk), sp.zeros(4, 4)) for blk in part]
SBx = {i: sblocks(p, PA, PB) for i, p in enumerate(good)}
SBz = {i: sblocks(p, PB, PA) for i, p in enumerate(good)}
results = {}
for i in range(len(good)):
    for j in range(len(good)):
        G = None
        for X in SBx[i]:
            for Y in SBz[j]:
                for e in (X * Y - Y * X):
                    num = sp.numer(sp.together(e))
                    num = sp.expand(num)
                    if num == 0:
                        continue
                    P = sp.Poly(num, t)
                    G = P if G is None else sp.gcd(G, P)
        if G is None:
            key = 'all angles'
        else:
            roots = sorted({sp.nsimplify(r) for r in sp.real_roots(G)} if G.degree() > 0 else set(), key=float)
            key = tuple(roots) if roots else 'no angle'
        results.setdefault(key, []).append((i, j))
print('exact angle sets (t = tan(g/2); t=0 parallel, t=1 perpendicular) -> number of pairs:')
for k, v in results.items():
    print('   ', k, '->', len(v), 'pairs')
# note t = infinity (g = pi, antiparallel = parallel as a line) is not a root of a polynomial; it is the same line as g = 0
