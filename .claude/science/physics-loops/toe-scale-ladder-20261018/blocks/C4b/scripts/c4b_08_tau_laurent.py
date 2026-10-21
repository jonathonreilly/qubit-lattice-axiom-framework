"""C4b-08: second route for the load-bearing E1 certificate: tau = tr(M_C M_K) computed in the
Laurent ring F2[x^+-,y^+-,z^+-] from the transvection formula M_P = 1 + v v^dag Lambda
(C4 NOTE, Theorem 1b), with v = (p_X; p_Z), dagger = transpose + antipode, Lambda = [[0,1],[1,0]].
Different implementation from c4b_05 (which iterated Pauli strings on sites).  Trace is cyclic,
so the composition order does not matter.  Also: symplecticity M^dag Lambda M = Lambda, det = 1.
Expected (from c4b_05, disclosed): tau = orbit sum of (4,2,0), 24 monomials.
"""
from collections import Counter
from c4b_common import check, total


def padd(*ps):
    c = Counter()
    for p in ps:
        for m in p:
            c[m] ^= 1
    return frozenset(m for m, v in c.items() if v)


def pmul(p, q):
    c = Counter()
    for a in p:
        for b in q:
            c[(a[0] + b[0], a[1] + b[1], a[2] + b[2])] ^= 1
    return frozenset(m for m, v in c.items() if v)


def anti(p):
    return frozenset((-a, -b, -c) for a, b, c in p)


ONE = frozenset({(0, 0, 0)})
ZERO = frozenset()


def string_polys(P):
    px = frozenset(r for r, L in P.items() if L in 'XY')
    pz = frozenset(r for r, L in P.items() if L in 'ZY')
    return px, pz


def M_of(P):
    px, pz = string_polys(P)
    # v v^dag Lambda : v = (px, pz)^T ; v^dag Lambda = (pz*, px*)
    return [[padd(ONE, pmul(px, anti(pz))), pmul(px, anti(px))],
            [pmul(pz, anti(pz)), padd(ONE, pmul(pz, anti(px)))]]


def mmul(A, B):
    return [[padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def dag(A):
    return [[anti(A[j][i]) for j in range(2)] for i in range(2)]


LAM = [[ZERO, ONE], [ONE, ZERO]]
C = {}
for a, L in zip(range(3), 'XYZ'):
    for s in (1, -1):
        v = [0, 0, 0]; v[a] = s; C[tuple(v)] = L
K = {}
for a, L in zip(range(3), 'XYZ'):
    o = [b for b in range(3) if b != a]
    for s1 in (1, -1):
        for s2 in (1, -1):
            v = [0, 0, 0]; v[o[0]] = s1; v[o[1]] = s2; K[tuple(v)] = L

MC, MK = M_of(C), M_of(K)
for name, M in [('C', MC), ('K', MK)]:
    ok = mmul(mmul(dag(M), LAM), M) == LAM
    check(f"M_{name} symplectic (M^dag Lambda M = Lambda)", ok)
    tr = padd(M[0][0], M[1][1])
    check(f"tr M_{name} = 0 (involution, as in C4)", tr == ZERO)
M = mmul(MC, MK)
check("M_C M_K symplectic", mmul(mmul(dag(M), LAM), M) == LAM)
det = padd(pmul(M[0][0], M[1][1]), pmul(M[0][1], M[1][0]))
check("det(M_C M_K) = 1", det == ONE)
tau = padd(M[0][0], M[1][1])
import itertools
orbit = set()
for p in itertools.permutations((4, 2, 0)):
    for s in itertools.product((1, -1), repeat=3):
        orbit.add(tuple(a * b for a, b in zip(p, s)))
print(f"tau has {len(tau)} monomials: {sorted(tau)}")
check("tau = orbit sum of (4,2,0) (24 monomials), nonconstant", set(tau) == orbit and len(tau) == 24)
total()
