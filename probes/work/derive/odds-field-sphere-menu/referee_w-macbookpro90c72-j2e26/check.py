#!/usr/bin/env python3
"""Independent referee: odds-field sphere menu a2. Own arithmetic."""
from fractions import Fraction as F
import itertools
import sympy as sp


def lambda1_identity():
    b = sp.symbols("beta", positive=True)
    Z = sp.integrate(sp.exp(b * sp.symbols("t")), (sp.symbols("t"), -1, 1)) / 2
    t = sp.symbols("t")
    lam1 = sp.integrate(sp.exp(b * t) * t, (t, -1, 1)) / 2 / (sp.sinh(b) / b)
    ok_z = sp.simplify(Z - sp.sinh(b) / b) == 0
    ok_l = sp.simplify((lam1 - (sp.coth(b) - 1 / b)).rewrite(sp.exp)) == 0
    return bool(ok_z and ok_l)


def assoc_poles():
    tt = sp.symbols("tt")
    return all(sp.simplify(sp.assoc_legendre(l, 1, tt).subs(tt, s)) == 0 for l in range(1, 8) for s in (1, -1))


def capacity(n, body):
    sites = list(itertools.product(range(n), repeat=3))
    S = set(body)
    free = [s for s in sites if s not in S]
    ix = {s: i for i, s in enumerate(free)}

    def nbrs(s):
        out = []
        for a in range(3):
            for d in (1, -1):
                q = list(s)
                q[a] += d
                out.append(tuple(q))
        return out

    N = len(free)
    A = [[F(0)] * N for _ in range(N)]
    b = [F(0)] * N
    for s in free:
        i = ix[s]
        A[i][i] = F(6)
        for q in nbrs(s):
            if q in ix:
                A[i][ix[q]] -= 1
            elif q in S:
                b[i] += 1
    # gaussian
    M = [row[:] + [bi] for row, bi in zip(A, b)]
    for c in range(N):
        piv = next(r for r in range(c, N) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(N):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    u = {free[r]: M[r][N] for r in range(N)}

    def val(q):
        if q in S:
            return F(1)
        return u.get(q, F(0))

    return sum(1 - F(1, 6) * sum(val(q) for q in nbrs(s)) for s in S)


def main():
    print("lambda1", lambda1_identity())
    print("P_l^1 poles", assoc_poles())
    c1 = capacity(5, [(2, 2, 2)])
    c2 = capacity(5, [(2, 2, 2), (3, 2, 2)])
    print(f"cap1 {c1} cap2adj {c2} subadditive {c2 < 2 * c1}")
    if lambda1_identity() and assoc_poles() and c1 == F(99, 136) and c2 < 2 * c1:
        print(
            "HIT: confirmed - lambda_1 = coth beta - 1/beta, P_l^1(+-1)=0 for l<=7, "
            "and one record on a 5^3 box has capacity 99/136, two adjacent records strictly less than twice that"
        )
        print(
            "SUMMARY: confirmed the exact Funk-Hecke dipole, the aligned-record vanishing, "
            "and the non-additive capacity; the numeric ordered-field spectrum was not rebuilt"
        )
    else:
        print(f"SUMMARY: fails at a finite claim cap1={c1}")


if __name__ == "__main__":
    main()
