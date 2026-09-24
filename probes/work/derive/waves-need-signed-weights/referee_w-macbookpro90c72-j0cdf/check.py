#!/usr/bin/env python3
"""Independent checks for nonnegative multi-level matrix weights."""
import sympy as sp


def main():
    k = sp.symbols("k", real=True)
    e = sp.exp(-sp.I * k)
    # half-step transport
    P = sp.Poly(sp.expand(sp.symbols("lam") ** 2 - e), sp.symbols("lam"))
    lam = sp.symbols("lam")
    roots = sp.solve(lam**2 - e, lam)
    ok = len(roots) == 2 and all(sp.simplify(r**2 - e) == 0 for r in roots)
    ok &= sp.simplify(roots[0] + roots[1]) == 0
    # chain factorization
    W0 = sp.Rational(1, 2) * e
    W1 = sp.Rational(1, 2) * e**2
    poly = sp.expand(lam**2 - W0 * lam - W1)
    fact = sp.expand((lam - e) * (lam + e / 2))
    ok &= sp.simplify(poly - fact) == 0
    # two-component two-level: companion 4x4
    # state (theta_t, theta_{t-1}), each 2-vector. Update uses only level j=1.
    # w1(+1) and w1(-1). W1(k) = [[0, e^{-ik}],[e^{ik}, 0]]
    W = sp.Matrix([[0, e], [sp.exp(sp.I * k), 0]])
    # companion: [W, 0; I, 0] if only j=1? 
    # theta_{t+1} = W1 theta_{t-1}, no j=0 term.
    # C = [[0, W],[I, 0]]
    Z = sp.zeros(2)
    I = sp.eye(2)
    C = sp.BlockMatrix([[Z, W], [I, Z]]).as_explicit()
    char = sp.simplify(C.charpoly(lam).as_expr())
    ok &= sp.simplify(char - (lam**4 - 1)) == 0
    # diffusive: |1+e^{-ik}|/2 = |cos(k/2)| < 1 at k=pi
    kpi = sp.pi
    mod = sp.Abs((1 + sp.exp(-sp.I * kpi)) / 2)
    ok &= sp.simplify(mod) == 0
    print("half-step roots, chain factor, lambda^4-1, diffusion at pi", bool(ok))
    if ok:
        print(
            "HIT: confirmed - half-step transport has branches ±e^{-ik/2} of modulus 1 at velocity 1/2; "
            "the two-component two-level rule has dispersion lambda^4-1; the average of two neighbors is inside the circle at k=pi"
        )
        print(
            "SUMMARY: confirmed the vector multi-level witnesses; "
            "the equality case still assumes Wielandt, as the author marked"
        )
    else:
        print("SUMMARY: fails at a dispersion identity")


if __name__ == "__main__":
    main()
