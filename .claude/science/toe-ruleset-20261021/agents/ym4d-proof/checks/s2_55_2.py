# s2_55_2 -- tower lemma and the N5' decomposition on exact finite chains (criteria: s2_55_2_criteria.md, written first).
from fractions import Fraction as Fr
import itertools

S0, S1n, S2n = range(4), range(3), range(2)

def chain_law(p, K0, K1):
    return {(u0, u1, u2): p[u0] * K0[u0][u1] * K1[u1][u2] for u0 in S0 for u1 in S1n for u2 in S2n}

def marg(q, idx):
    m = {}
    for k, w in q.items():
        key = tuple(k[i] for i in idx)
        m[key] = m.get(key, Fr(0)) + w
    return m

def cond_exp(q, f, idx):            # E[f(U0) | U_idx] as dict keyed by value of U_idx
    num, den = {}, {}
    for k, w in q.items():
        key = k[idx]
        num[key] = num.get(key, Fr(0)) + w * f[k[0]]
        den[key] = den.get(key, Fr(0)) + w
    return {key: num[key] / den[key] for key in num}

def E(q, g):                        # g: function of full tuple
    return sum(w * g(k) for k, w in q.items())

def check_chain(p, K0, K1, F, S, X, grid):
    q = chain_law(p, K0, K1)
    assert sum(q.values()) == 1
    EX = E(q, lambda k: X[k[0]])
    X1 = cond_exp(q, X, 1); X2 = cond_exp(q, X, 2)
    # tower: E[X|U2=v] = sum_u P(U1=u|U2=v) X1[u]
    m12 = marg(q, (1, 2)); m2 = marg(q, (2,))
    tower_id = all(X2[v] == sum(m12[(u, v)] / m2[(v,)] * X1[u] for u in S1n) for v in S2n)
    cs = list(grid) + [EX]
    tower_ineq = all(max(abs(X2[v] - c) for v in S2n) <= max(abs(X1[u] - c) for u in S1n) for c in cs)
    g1 = tower_id and tower_ineq
    # PB
    F1 = cond_exp(q, F, 1); Sx1 = cond_exp(q, S, 1); F2 = cond_exp(q, F, 2); Sx2 = cond_exp(q, S, 2)
    def ccov_given(level, fa, fb):   # E over U_level of Cov(fa(U0), fb(U0) | U_level)
        ea = cond_exp(q, fa, level); eb = cond_exp(q, fb, level)
        return E(q, lambda k: (fa[k[0]] - ea[k[level]]) * (fb[k[0]] - eb[k[level]]))
    lhs = ccov_given(2, F, S)
    # E Cov(F1,S1|U2): F1,S1 functions of U1; conditional law of U1 given U2 is the chain's
    def ccov_top():
        tot = Fr(0)
        for v in S2n:
            pv = m2[(v,)]
            w = {u: m12[(u, v)] / pv for u in S1n}
            mf = sum(w[u] * F1[u] for u in S1n); ms = sum(w[u] * Sx1[u] for u in S1n)
            tot += pv * sum(w[u] * (F1[u] - mf) * (Sx1[u] - ms) for u in S1n)
        return tot
    def abs_ccov_top():
        tot = Fr(0)
        for v in S2n:
            pv = m2[(v,)]
            w = {u: m12[(u, v)] / pv for u in S1n}
            mf = sum(w[u] * F1[u] for u in S1n); ms = sum(w[u] * Sx1[u] for u in S1n)
            tot += pv * abs(sum(w[u] * (F1[u] - mf) * (Sx1[u] - ms) for u in S1n))
        return tot
    pb1 = (lhs == ccov_given(1, F, S) + ccov_top())
    EF = E(q, lambda k: F[k[0]]); ES = E(q, lambda k: S[k[0]])
    cov = E(q, lambda k: (F[k[0]] - EF) * (S[k[0]] - ES))
    coarse = E(q, lambda k: (F2[k[2]] - EF) * (Sx2[k[2]] - ES))
    pb2 = (cov == lhs + coarse)
    g2 = pb1 and pb2
    # TOP and COARSE bounds, squared form
    A = abs_ccov_top()
    L2F1 = E(q, lambda k: (F1[k[1]] - EF) ** 2)
    g3 = all(A ** 2 <= L2F1 * max(abs(Sx1[u] - c) for u in S1n) ** 2 for c in cs)
    L2F2 = E(q, lambda k: (F2[k[2]] - EF) ** 2)
    g4 = all(coarse ** 2 <= L2F2 * max(abs(Sx2[v] - c) for v in S2n) ** 2 for c in cs)
    nonvac = (A > 0) and (max(abs(X2[v] - EX) for v in S2n) > 0)
    return g1, g2, g3, g4, nonvac

grid = [Fr(-2), Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 3), Fr(1), Fr(2)]
chains = [
    ([Fr(1, 4), Fr(1, 8), Fr(3, 8), Fr(1, 4)],
     [[Fr(1, 2), Fr(1, 3), Fr(1, 6)], [Fr(1, 5), Fr(3, 5), Fr(1, 5)], [Fr(1, 3), Fr(1, 3), Fr(1, 3)], [Fr(0), Fr(1, 4), Fr(3, 4)]],
     [[Fr(2, 3), Fr(1, 3)], [Fr(1, 4), Fr(3, 4)], [Fr(1, 2), Fr(1, 2)]],
     [Fr(1), Fr(-2), Fr(3), Fr(1, 2)], [Fr(2), Fr(1), Fr(-1), Fr(0)], [Fr(5), Fr(-1), Fr(2), Fr(-3)]),
    ([Fr(1, 10), Fr(2, 5), Fr(3, 10), Fr(1, 5)],
     [[Fr(1, 7), Fr(2, 7), Fr(4, 7)], [Fr(1, 2), Fr(1, 2), Fr(0)], [Fr(1, 9), Fr(4, 9), Fr(4, 9)], [Fr(3, 4), Fr(1, 8), Fr(1, 8)]],
     [[Fr(1, 3), Fr(2, 3)], [Fr(5, 6), Fr(1, 6)], [Fr(2, 5), Fr(3, 5)]],
     [Fr(-1), Fr(2), Fr(0), Fr(4)], [Fr(3), Fr(-1), Fr(1, 2), Fr(2)], [Fr(0), Fr(1), Fr(1), Fr(-2)]),
    ([Fr(1, 4)] * 4,
     [[Fr(1, 3)] * 3, [Fr(1, 2), Fr(1, 4), Fr(1, 4)], [Fr(1, 6), Fr(1, 6), Fr(2, 3)], [Fr(2, 5), Fr(2, 5), Fr(1, 5)]],
     [[Fr(9, 10), Fr(1, 10)], [Fr(1, 10), Fr(9, 10)], [Fr(1, 2), Fr(1, 2)]],
     [Fr(1), Fr(1), Fr(-1), Fr(-1)], [Fr(2), Fr(-2), Fr(2), Fr(-2)], [Fr(1), Fr(0), Fr(0), Fr(-1)]),
]
res = [check_chain(*ch, grid) for ch in chains]
G1 = all(r[0] for r in res); G2 = all(r[1] for r in res); G3 = all(r[2] for r in res); G4 = all(r[3] for r in res)
NV = any(r[4] for r in res)
# Y1: non-Markov control
p = [Fr(1, 4)] * 4
K0p = [Fr(1, 2), Fr(1, 4), Fr(1, 4)]                      # U1 independent of U0
Kp = [[Fr(9, 10), Fr(1, 10)], [Fr(1, 10), Fr(9, 10)], [Fr(9, 10), Fr(1, 10)], [Fr(1, 10), Fr(9, 10)]]   # U2 depends on U0
X = [Fr(1), Fr(-1), Fr(1), Fr(-1)]
q = {(u0, u1, u2): p[u0] * K0p[u1] * Kp[u0][u2] for u0 in S0 for u1 in S1n for u2 in S2n}
EX = sum(w * X[k[0]] for k, w in q.items())
X1 = cond_exp(q, X, 1); X2 = cond_exp(q, X, 2)
Y1 = (max(abs(X2[v] - EX) for v in S2n) > max(abs(X1[u] - EX) for u in S1n))
print('G1 TOWER', 'PASS' if G1 else 'FAIL'); print('G2 PB', 'PASS' if G2 else 'FAIL')
print('G3 TOP', 'PASS' if G3 else 'FAIL'); print('G4 COARSE', 'PASS' if G4 else 'FAIL')
print('non-vacuity', NV)
print('Y1 non-Markov control', 'FIRED' if Y1 else 'DID-NOT-FIRE', '| E[X|U1] =', X1, '| E[X|U2] =', X2, '| EX =', EX)
print('VERDICT:', 'PASS' if (G1 and G2 and G3 and G4 and NV and Y1) else 'FAIL')
