#!/usr/bin/env python3
"""Finite supplied-scale partitions and piecewise-constant log integrals.
No physical beta coefficients, mass matching, or YT pipeline are derived.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/POSITIVE_SCALE_THRESHOLD_ITINERARY_THEOREM_NOTE_2026-10-24.md']

from bisect import bisect_right
from math import isfinite, log, isclose, nextafter


def positive(value):
    if not isfinite(value) or value <= 0:
        raise ValueError('scales must be finite and strictly positive')


def itinerary(start, end, thresholds):
    """Return (start,end,regime) triples; ascending distinct thresholds required.

    Regime j is the open interval with j thresholds below its interior.
    Exact endpoint thresholds use the adjacent segment's interior regime.
    Endpoint labels themselves follow right-continuous regime assignment.
    """
    positive(start)
    positive(end)
    thresholds = tuple(thresholds)
    for x in thresholds:
        positive(x)
    if any(a >= b for a, b in zip(thresholds, thresholds[1:])):
        raise ValueError('thresholds must be strictly ascending and distinct')
    if start == end:
        return []
    lo, hi = min(start, end), max(start, end)
    inner = [x for x in thresholds if lo < x < hi]
    if start > end:
        inner.reverse()
    points = [start, *inner, end]
    # bisect_right at the lower boundary equals the regime of every
    # interior point. Avoid rounding a floating midpoint onto a boundary.
    return [(a, b, bisect_right(thresholds, min(a, b)))
            for a, b in zip(points, points[1:])]


def integrate(start, end, thresholds, coefficients):
    """Supplied piecewise-constant coefficient integrated against d log(mu)."""
    thresholds = tuple(thresholds)
    coefficients = tuple(coefficients)
    segments = itinerary(start, end, thresholds)
    if len(coefficients) != len(thresholds) + 1 or not all(isfinite(x) for x in coefficients):
        raise ValueError('one finite coefficient per open regime required')
    return sum(coefficients[j] * (log(b) - log(a)) for a, b, j in segments)


def main():
    failed = 0
    def check(label, ok):
        nonlocal failed
        failed += not bool(ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label}")

    cases = [
        (1, 8, [], [(1, 8, 0)]),
        (1, 8, [2], [(1, 2, 0), (2, 8, 1)]),
        (1, 8, [2, 4], [(1, 2, 0), (2, 4, 1), (4, 8, 2)]),
        (2, 4, [1, 2, 4, 8], [(2, 4, 2)]),
        (4, 2, [1, 2, 4, 8], [(4, 2, 2)]),
        (2, 2, [1, 2, 4], []),
        (2, 4, [1, 8], [(2, 4, 1)]),
    ]
    for a, b, ts, expected in cases:
        seg = itinerary(a, b, ts)
        check(f'exact fixture {a}->{b}, {ts}', seg == expected)
        check('reversal preserves interior labels', itinerary(b, a, ts) ==
              [(y, x, j) for x, y, j in reversed(seg)])
        check('adjacency and endpoint coverage', (a == b and not seg) or
              (seg[0][0] == a and seg[-1][1] == b and
               all(x[1] == y[0] for x, y in zip(seg, seg[1:]))))
    adjacent = nextafter(1.0, 2.0)
    check('adjacent floats: no rounded-midpoint regime error',
          itinerary(1.0, adjacent, [1.0, adjacent]) == [(1.0, adjacent, 1)])
    check('constant coefficient integral', isclose(integrate(1, 8, [2, 4], [3, 3, 3]),
                                                   3*log(8), rel_tol=1e-14))
    exact = (2+3+5)*log(2)
    check('analytic dyadic piecewise integral', isclose(integrate(1, 8, [2, 4], [2, 3, 5]), exact, rel_tol=1e-14))
    check('integral orientation', isclose(integrate(8, 1, [2, 4], [2, 3, 5]), -exact, rel_tol=1e-14))
    check('empty oriented integral', integrate(2, 2, [2], [3, 5]) == 0)
    for args in [(0, 1, []), (-1, 2, []), (float('nan'), 1, []),
                 (1, float('inf'), []), (1, 2, [0]), (1, 2, [float('nan')]),
                 (1, 2, [float('inf')]), (1, 2, [2, 2]), (1, 2, [3, 2])]:
        try:
            itinerary(*args)
        except ValueError:
            check(f'invalid input rejected {args}', True)
        else:
            check(f'invalid input rejected {args}', False)
    for coeffs in [[], [1], [1, float('nan')], [1, float('inf')]]:
        try:
            integrate(1, 4, [2], coeffs)
        except ValueError:
            check(f'invalid coefficients rejected {coeffs}', True)
        else:
            check(f'invalid coefficients rejected {coeffs}', False)

    # Historical diagnostic data, not physical masses or coefficients derived here.
    v, mt, mb, mc, mz = 246.28, 172.69, 4.18, 1.27, 91.1876
    b = lambda nf: 11-2*nf/3
    wrong = sum(b(nf)*log(lo/hi) for hi, lo, nf in
                [(v, mt, 6), (mt, mb, 5), (mb, mc, 4), (mc, mz, 3)])
    corrected = integrate(v, mz, [mc, mb, mt], [b(3), b(4), b(5), b(6)])
    check('historical route clips below-endpoint thresholds',
          itinerary(v, mz, [mc, mb, mt]) == [(v, mt, 3), (mt, mz, 2)])
    check('historical wrong itinerary remains discriminating',
          isclose(wrong-corrected, 4.904339799227147, rel_tol=1e-12))
    print(f'Historical supplied-data integral: wrong={wrong:.15g}; clipped={corrected:.15g}; delta={wrong-corrected:.15g}')
    print(f'Total FAIL: {failed}; no physical model or full YT result certified')
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
