#!/usr/bin/env python3
"""Narrow exact check of the piecewise-polynomial correlation used in the proof."""
import sympy as s
for n in [16, 20, 32, 64, 2048]:
    t = [s.Rational(n//2-2*abs(x-n//2), n//2) for x in range(n)]
    y = [t[(x-n//4) % n] for x in range(n)]
    for j in range(min(n//4, 5)+1):
        f = sum(t[x]*y[(x+j) % n] for x in range(n))/n
        expected = (s.Rational(2, n)+s.Rational(32, 3*n**3))*j-s.Rational(32*j**3, 3*n**3)
        assert f == expected, (n, j, f, expected)
        print(f'N={n}, shift={j}, correlation={f}')
print('All selected exact piecewise-correlation controls passed.')
