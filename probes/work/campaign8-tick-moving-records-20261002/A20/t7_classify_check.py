"""Cross-check the classification on all enumerated covariant Clifford solutions:
  z-symbol -> w-polynomials (greedy Dickson elimination) -> N0 = adj(P)(M-1)P / Delta^2
  verify: N0 polynomial (remainder 0), S3-symmetric entries, tr N0 = Delta * det N0, det N0 (0 => involution).
"""
import itertools
import sympy as sp
from cliff_lines import affine_solutions
from cliff_enum import check
from cliff_poly import from_vecs
from wsym import W, P2, to_z, permute

w1, w2, w3 = W


def z_to_w(S):
    S = set(S); acc = P2(0)
    while S:
        v = max(tuple(sorted([abs(c) for c in u], reverse=False)) and tuple(abs(c) for c in u) for u in S)
        mon = P2(w1 ** v[0] * w2 ** v[1] * w3 ** v[2])
        acc = acc + mon
        for u in to_z(mon):
            S ^= {u}
    return acc


u0 = (w1 + w2, w2 + w3)
P = [[u0[0], u0[0] ** 2], [u0[1], u0[1] ** 2]]
adjP = [[P[1][1], P[0][1]], [P[1][0], P[0][0]]]
Delta = sp.expand(P[0][0] * P[1][1] + P[0][1] * P[1][0])


def N0_of(Mw):
    K = [[Mw[i][j].as_expr() + (1 if i == j else 0) for j in range(2)] for i in range(2)]
    T = [[sp.expand(sum(adjP[i][k] * K[k][l] * P[l][j] for k in range(2) for l in range(2))) for j in range(2)] for i in range(2)]
    N = [[None] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            q, r = sp.div(T[i][j], sp.expand(Delta ** 2), *W, modulus=2)
            N[i][j] = (P2(q), P2(r))
    return N


def symmetric(p):
    return all((permute(p, s) - p).is_zero or (permute(p, s).as_expr() - p.as_expr()) == 0
               for s in [(1, 0, 2), (1, 2, 0)])


for shape, r in [("cube", 2), ("oct", 3)]:
    pts, idx, Bs, L3, part, hom = affine_solutions(shape, r)
    L33 = (L3.astype(int) @ L3) % 2
    for s in itertools.product([0, 1], repeat=len(hom)):
        coeff = part.astype(int).copy()
        for si, hv in zip(s, hom):
            if si:
                coeff = (coeff + hv) % 2
        f = (coeff @ Bs.astype(int)) % 2
        h = (L33 @ f) % 2
        if not all(check(f, h, pts, r)):
            continue
        Mz = from_vecs(f, h, pts)
        Mw = [[z_to_w(Mz[i][j]) for j in range(2)] for i in range(2)]
        # round trip
        rt = all(to_z(Mw[i][j]) == Mz[i][j] for i in range(2) for j in range(2))
        N = N0_of(Mw)
        rem0 = all(N[i][j][1].is_zero for i in range(2) for j in range(2))
        Nq = [[N[i][j][0] for j in range(2)] for i in range(2)]
        sym = all(symmetric(Nq[i][j]) for i in range(2) for j in range(2))
        trN = (Nq[0][0] + Nq[1][1]).as_expr()
        detN = (Nq[0][0] * Nq[1][1] + Nq[0][1] * Nq[1][0]).as_expr()
        cond = sp.Poly(sp.expand(trN - Delta * detN), *W, modulus=2).is_zero
        print(f"{shape} r={r} s={s}: roundtrip={rt} N0 polynomial={rem0} symmetric={sym} "
              f"trN0=Delta*detN0: {cond}  detN0={sp.Poly(detN, *W, modulus=2).as_expr()}  N0={[[str(Nq[i][j].as_expr()) for j in range(2)] for i in range(2)]}")
