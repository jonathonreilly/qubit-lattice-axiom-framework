#!/usr/bin/env python3
"""Independent check of the sharp one-site TV bound and the 49/25 window."""
from fractions import Fraction as F
import sympy as sp


def main():
    m, M, H = sp.symbols("m M H", positive=True)
    # E[(h-H)+] <= (H-m)(M-H)/(M-m) for a two-point law; TV = that / H
    tv = (H - m) * (M - H) / ((M - m) * H)
    crit = sp.diff(tv, H)
    Hstar = sp.simplify(sp.solve(crit, H)[0])
    best = sp.simplify(tv.subs(H, Hstar))
    sharp = (sp.sqrt(M) - sp.sqrt(m)) / (sp.sqrt(M) + sp.sqrt(m))
    ok = sp.simplify(Hstar - sp.sqrt(M * m)) == 0 and sp.simplify(best - sharp) == 0
    # tanh(log(R)/4) = (sqrt(R)-1)/(sqrt(R)+1)
    R = sp.symbols("R", positive=True)
    tanh = (sp.sqrt(R) - 1) / (sp.sqrt(R) + 1)
    # 6 tanh < 1 iff sqrt(R) < 7/5 iff R < 49/25
    bound = sp.simplify(sp.solve(6 * tanh - 1, R)[0])
    ok &= bound == sp.Rational(49, 25)
    # attained 1/5 at M/m = 9/4
    att = sharp.subs({M: sp.Rational(9, 4), m: 1})
    ok &= sp.simplify(att - sp.Rational(1, 5)) == 0
    # a1's (M-m)/(M+m) is strictly larger for R=9/4
    loose = (F(9, 4) - 1) / (F(9, 4) + 1)
    ok &= loose > F(1, 5)
    # content-less: ratios are cw and 1/(cw), unique iff 25/49 < cw < 49/25
    axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    pqr = { (3, 1, 2): (3, 1, 2) }

    def omega(a, b, p, q, r):
        if a == b:
            return p
        if a == tuple(-x for x in b):
            return q
        return r

    def spread(p, q, r):
        worst = F(1)
        for u, v in itertools.product(axes, repeat=2):
            hs = [F(omega(a, v, p, q, r), omega(a, u, p, q, r)) for a in axes]
            worst = max(worst, max(hs) / min(hs))
        return worst

    import itertools
    r312 = spread(3, 1, 2)
    no_cert = r312 > F(49, 25)
    print(f"identity {ok} loose {loose} > 1/5, (3,1,2) content spread {r312} exceeds 49/25 {no_cert}")
    print(f"Hstar formula ok, 6 tanh boundary {bound}")
    if ok and no_cert:
        print(
            "HIT: confirmed - sup TV = (sqrt(M)-sqrt(m))/(sqrt(M)+sqrt(m)) = tanh(log(R)/4), "
            "attained (1/5 at R=9/4); 6 tanh < 1 iff R < 49/25; (3,1,2) content ratios already exceed that"
        )
        print(
            "SUMMARY: confirmed the sharp one-site bound and the 49/25 uniqueness window; "
            "the chessboard/Peierls constants above were not recomputed"
        )
    else:
        print("SUMMARY: fails at the sharp TV identity or the window")


if __name__ == "__main__":
    main()
