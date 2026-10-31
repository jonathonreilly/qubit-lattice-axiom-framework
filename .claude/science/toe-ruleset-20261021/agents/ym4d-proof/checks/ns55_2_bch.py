"""ns55_2 -- exact free-algebra structure of F(u,a,b) = log(e^u e^a e^{-u-b}) - a + b, truncated at degree 4.

Criteria: checks/ns55_2_criteria.md (written before this file). Exact Fractions only; letters 'u','a','b' (b = beta).
"""
from fractions import Fraction as Fr
from math import factorial

DMAX = 4


def add(P, Q, c=Fr(1)):
    R = dict(P)
    for w, v in Q.items():
        R[w] = R.get(w, Fr(0)) + c * v
        if R[w] == 0:
            del R[w]
    return R


def mul(P, Q):
    R = {}
    for w1, v1 in P.items():
        for w2, v2 in Q.items():
            w = w1 + w2
            if len(w) > DMAX:
                continue
            R[w] = R.get(w, Fr(0)) + v1 * v2
            if R[w] == 0:
                del R[w]
    return R


def scal(P, c):
    return {w: c * v for w, v in P.items() if c * v != 0}


ONE = {(): Fr(1)}


def exp_(X):
    R, term = dict(ONE), dict(ONE)
    for n in range(1, DMAX + 1):
        term = mul(term, X)
        R = add(R, term, Fr(1, factorial(n)))
    return R


def log_(M):                       # M = 1 + Y, Y without constant term
    Y = add(M, ONE, Fr(-1))
    assert () not in Y
    R, term = {}, dict(ONE)
    for n in range(1, DMAX + 1):
        term = mul(term, Y)
        R = add(R, term, Fr((-1) ** (n + 1), n))
    return R


def L_(letter):
    return {(letter,): Fr(1)}


u, a, b = L_('u'), L_('a'), L_('b')
neg = lambda P: scal(P, Fr(-1))

F = add(add(log_(mul(mul(exp_(u), exp_(a)), exp_(neg(add(u, b))))), a, Fr(-1)), b)
G = add(log_(mul(mul(exp_(u), exp_(a)), exp_(neg(add(u, b))))), a, Fr(-1))      # designed-FAIL control (+b omitted)

D1 = all(len(w) >= 2 for w in F)
D2 = all(('u' in w) or ('b' in w) for w in F)
D3 = all(len(set(w)) >= 2 for w in F)
deg2 = {w: v for w, v in F.items() if len(w) == 2}
target2 = {('u', 'a'): Fr(1), ('a', 'u'): Fr(-1),
           ('u', 'b'): Fr(-1, 2), ('b', 'u'): Fr(1, 2),
           ('a', 'b'): Fr(-1, 2), ('b', 'a'): Fr(1, 2)}
D4 = deg2 == target2
D5 = all(('a' in w and 'b' in w) for w in F if 'u' not in w)
D6_control_fails = not all(len(w) >= 2 for w in G)          # must be True (G has the degree-1 word ('b',))
X = add(u, a)
D7 = log_(mul(exp_(X), exp_(neg(X)))) == {}

print("number of words in F up to degree 4:", len(F))
print("degree-2 part of F:", {''.join(w): str(v) for w, v in sorted(deg2.items())})
print("degree-3 words of F without u:", {''.join(w): str(v) for w, v in sorted(F.items()) if len(w) == 3 and 'u' not in w})
print(f"D1={D1} D2={D2} D3={D3} D4={D4} D5={D5} D6(control G fails D1)={D6_control_fails} D7(exp/log sanity)={D7}")
print("OVERALL:", "PASS" if (D1 and D2 and D3 and D4 and D5 and D6_control_fails and D7) else "FAIL")
