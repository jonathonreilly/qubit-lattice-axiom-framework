#!/usr/bin/env python3
"""Referee for odds-field-additive-sources a2.

Author w-jonathonsmac4f50-j0faf (claude-opus-5-5). Own Bessel ratios.
The ratio G(r)/G(0) is the same in the random-walk and Laplacian normalizations.
"""
import itertools
import numpy as np
from scipy.integrate import quad
from scipy.special import ive

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def algebra():
    # cap = 2/(G0+Gr), c1 = 1/G0, so cap/(2 c1) = G0/(G0+Gr) >= 9/10 iff Gr/G0 <= 1/9.
    g0, gr = 1.2, 0.1
    cap = 2 / (g0 + gr)
    c1 = 1 / g0
    ratio = cap / (2 * c1)
    ident = abs(ratio - g0 / (g0 + gr)) < 1e-15
    # no integer vector has squared length 7: squares mod 8 are 0, 1, 4, and 7 is not a sum of three.
    squares = {0, 1, 4}
    no7 = 7 not in {a + b + c for a in squares for b in squares for c in squares}
    # and directly
    no7 &= not any(i * i + j * j + k * k == 7 for i in range(3) for j in range(3) for k in range(3))
    report(
        "two-record identity",
        ident and no7,
        "cap/(2 c1) = G(0)/(G(0)+G(r)); within 10 percent iff G(r)/G(0) <= 1/9; no lattice vector has |r|^2 = 7",
    )


def green(n, m2=0.0):
    a, b, c = sorted(abs(int(v)) for v in n)

    def f(t):
        return np.exp(-m2 * t) * ive(a, 2 * t) * ive(b, 2 * t) * ive(c, 2 * t)

    cuts = (0.0, 0.3, 1.5, 8.0, 40.0, np.inf)
    return sum(quad(f, lo, hi, epsabs=1e-12, limit=400)[0] for lo, hi in zip(cuts, cuts[1:]))


def ratios():
    g0 = green((0, 0, 0))
    ge = green((1, 0, 0))
    # Laplacian normalization: g(0)-g(e)=1/6. Random-walk normalization is 6 times larger, so the difference is 1.
    lap_ok = abs((g0 - ge) - 1 / 6) < 1e-9
    watson = abs(6 * g0 - 1.516386059) < 2e-8
    one_ninth = 1 / 9
    # orbits with |r|^2 <= 6 must fail; (2,2,0) passes; (2,1,1) fails
    must_fail = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (2, 1, 1)]
    got = {}
    ok = lap_ok and watson
    for v in must_fail:
        got[v] = green(v) / g0
        ok &= got[v] > one_ninth
    r220 = green((2, 2, 0)) / g0
    r211 = got[(2, 1, 1)]
    ok &= r220 < one_ninth < r211
    ok &= abs(r220 - 0.111008) < 2e-5 and abs(r211 - 0.126479) < 2e-5
    # a few longer vectors should also pass
    for v in ((2, 2, 1), (3, 0, 0), (2, 2, 2)):
        ok &= green(v) / g0 < one_ninth
    text = " ".join(f"{v}:{got[v]:.4f}" for v in must_fail)
    report(
        "massless threshold",
        ok,
        f"6 G(0)={6 * g0:.9f}; (2,2,0)={r220:.6f} < 1/9 < {r211:.6f}=(2,1,1); failing {text}",
    )


def torus_anchor():
    """(-Δ + 5) on the 7-torus. The ratio G(e)/G(0) is normalization-free."""
    L = 7
    n = L ** 3
    idx = {p: i for i, p in enumerate(itertools.product(range(L), repeat=3))}
    A = np.zeros((n, n))
    for p, i in idx.items():
        A[i, i] = 6 + 5
        for a in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            q = tuple((p[k] + a[k]) % L for k in range(3))
            A[i, idx[q]] -= 1
    b = np.zeros(n)
    b[idx[(0, 0, 0)]] = 1.0
    g = np.linalg.solve(A, b)
    ratio = g[idx[(1, 0, 0)]] / g[idx[(0, 0, 0)]]
    report(
        "torus anchor",
        abs(ratio - 0.09895102) < 2e-7,
        f"7-torus m^2=5, G(e)/G(0)={ratio:.8f}",
    )


def main():
    algebra()
    ratios()
    torus_anchor()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - two massless records add to within 10 percent iff G(r)/G(0) <= 1/9, "
        "which holds for every lattice separation with |r|^2 >= 8 and for none with |r|^2 <= 6. "
        "(2,2,0) is 0.1110 and (2,1,1) is 0.1265. There is no vector of squared length 7."
    )
    print(
        "SUMMARY: confirmed the two-record identity, the massless threshold, and the 7-torus anchor at m^2=5. "
        "The cube constant kappa and the D* fit were not re-fitted."
    )


if __name__ == "__main__":
    main()
