"""Independent check: build the joint law as a literal product of nearest-neighbour bond weights over the FULL
configuration space (no hand enumeration of consistent configurations), for K = 1, 2, 3 rungs."""
from fractions import Fraction as Fr
from itertools import product

def gibbs(K, s, t):
    A_states = list(product((0, 1), repeat=2))          # alpha = (tau, a)
    B_states = list(product((0, 1), repeat=2))          # beta  = (tau', b)
    rails = list(product((0, 1), repeat=2 * K))         # (g1_1..g1_K, g2_1..g2_K)
    law = {}
    for A in A_states:
        for R in rails:
            g1, g2 = R[:K], R[K:]
            for B in B_states:
                w = 1
                # site weights with the setting neighbours
                w *= 1 if A[0] == s else 0                       # s - A bond
                w *= 1 if B[0] == t else 0                       # B - t bond
                # A - rail bonds
                w *= 1 if g1[0] == A[1] else 0                   # A - g1_1
                w *= 1 if g2[0] == (A[1] ^ 1 ^ A[0]) else 0      # A - g2_1
                # rail copy bonds
                for k in range(K - 1):
                    w *= 1 if g1[k + 1] == g1[k] else 0
                    w *= 1 if g2[k + 1] == g2[k] else 0
                # rail - B bonds
                w *= 1 if (B[0] == 1 or B[1] == g1[-1]) else 0   # g1_K - B
                w *= 1 if (B[0] == 0 or B[1] == (g2[-1] ^ 1)) else 0   # g2_K - B
                if w: law[(A, R, B)] = Fr(w)
    Z = sum(law.values())
    return {k: v / Z for k, v in law.items()}, Z

for K in (1, 2, 3):
    E = {}; margs = {}
    for s in (0, 1):
        for t in (0, 1):
            law, Z = gibbs(K, s, t)
            E[(s, t)] = sum(p * (1 - 2 * k[0][1]) * (1 - 2 * k[2][1]) for k, p in law.items())
            # all single-site marginals
            for name, f in (("A", lambda k: k[0]), ("B", lambda k: k[2])) + tuple(
                    (f"r{i}", (lambda i: lambda k: k[1][i])(i)) for i in range(2 * K)):
                m = {}
                for k, p in law.items(): m[f(k)] = m.get(f(k), 0) + p
                margs[(name, s, t)] = m
    S = E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]
    names = sorted({n for (n, _, _) in margs})
    dep = {}
    for n in names:
        ds = any(margs[(n, 0, t)] != margs[(n, 1, t)] for t in (0, 1))
        dt = any(margs[(n, s, 0)] != margs[(n, s, 1)] for s in (0, 1))
        dep[n] = (ds, dt)
    print(f"K={K}: Z(s,t)={[str(gibbs(K,s,t)[1]) for s in (0,1) for t in (0,1)]}  CHSH={S}  marginal-dependence (on s, on t): {dep}")
