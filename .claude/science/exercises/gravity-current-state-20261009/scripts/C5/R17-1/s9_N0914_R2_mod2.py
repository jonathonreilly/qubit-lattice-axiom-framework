"""R17-1 s9 (written before running). N0914's own g-term at N = 2 (N0914:133-157).
Build the R2 rows from the doubled-position rule (N0914:135-140): R2_ij = 2 eps_iab eps_jcd D_a D_c h_bd,
h_bb = q_bb (diagonal, doubled position 2x), h_bd = q_bd/2 off diagonal (doubled position 2x+e_b+e_d),
D_a f(P) = f(P+e_a) - f(P-e_a) in doubled coordinates. Check: integer G R2^T = 0 (N0914:146), then reduce mod 2:
expectation (hand derivation): diagonal rows vanish mod 2; off-diagonal row R2_xy mod 2 = product of the two
cubes sharing that xy face (weight 10). Report the as-is-lift zeroth moment M0 of the mod-2 pattern."""
import numpy as np, itertools
from fractions import Fraction as F
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
TIDX = {t: n for n, t in enumerate(TYPES)}
E3 = np.eye(3, dtype=int)
def lc(i, j, k): return int(np.linalg.det(np.array([E3[i], E3[j], E3[k]])))
def slot_at(P, b, d):
    """doubled position P of component (b,d) -> (base x, type); None if parity wrong"""
    b, d = min(b, d), max(b, d); P = np.array(P)
    off = E3[b] + E3[d] if b != d else np.zeros(3, int)
    Q = P - off
    if np.any(Q % 2): return None
    return (tuple(Q // 2), TIDX[(b, d)])
def R2_row(i, j, P):
    row = {}
    for a, b, c, d in itertools.product(range(3), repeat=4):
        e = lc(i, a, b)*lc(j, c, d)
        if e == 0: continue
        for sa, sc in itertools.product([1, -1], repeat=2):
            Q = np.array(P) + sa*E3[a] + sc*E3[c]
            s = slot_at(Q, b, d)
            if s is None: continue
            coef = F(2*e*sa*sc) * (F(1, 2) if b != d else F(1))
            row[s] = row.get(s, F(0)) + coef
    return {s: v for s, v in row.items() if v != 0}
def G_entries(x, t):
    i, j = TYPES[t]; x = np.array(x); out = []
    if i == j: out += [((tuple(x - E3[j]), j), 1), ((tuple(x), j), -1)]
    else: out += [((tuple(x), j), 1), ((tuple(x + E3[i]), j), -1), ((tuple(x), i), 1), ((tuple(x + E3[j]), i), -1)]
    return out
def Gof(supp):
    chk = {}
    for (x, t), v in supp.items():
        for g, c in G_entries(x, t): chk[g] = chk.get(g, 0) + c*v
    return {g: v for g, v in chk.items() if v != 0}
for (i, j), P in [((0,0), (4,4,4)), ((0,1), (5,5,4)), ((1,2), (4,5,5)), ((0,2), (5,4,5))]:
    row = R2_row(i, j, P)
    assert all(v.denominator == 1 for v in row.values())
    row = {s: int(v) for s, v in row.items()}
    g = Gof(row)
    m2 = {s: v % 2 for s, v in row.items() if v % 2}
    print("R2_%s%s at doubled %s: weight %d, max|coef| %d, l1 %d, integer G R2 = 0: %s ; mod-2 weight %d ; mod-2 types %s"
          % ("xyz"[i], "xyz"[j], P, len(row), max(abs(v) for v in row.values()), sum(abs(v) for v in row.values()),
             len(g) == 0, len(m2), sorted(set(TYPES[t] for (x, t) in m2))))
    if m2:
        # compare with the two cubes sharing the face at P (face (i,j) at base (P - e_i - e_j)/2)
        base = (np.array(P) - E3[i] - E3[j])//2; k = 3 - i - j
        def cube(x):
            x = np.array(x); fs = set()
            for (a, b) in [(0,1),(1,2),(0,2)]:
                c = 3 - a - b
                fs.add((tuple(x), TIDX[(a, b)])); fs.add((tuple(x + E3[c]), TIDX[(a, b)]))
            return fs
        pair = cube(base) ^ cube(base - E3[k])
        print("    mod-2 pattern == cube(x) xor cube(x - e_k): %s ; G(mod-2 pattern) = 0 mod 2: %s ; M0 of 0/1 lift (xy,yz,xz counts) = %s"
              % (set(m2.keys()) == pair, all(v % 2 == 0 for v in Gof(m2).values()),
                 [sum(1 for (x, t) in m2 if t == tt) for tt in (3, 4, 5)]))
