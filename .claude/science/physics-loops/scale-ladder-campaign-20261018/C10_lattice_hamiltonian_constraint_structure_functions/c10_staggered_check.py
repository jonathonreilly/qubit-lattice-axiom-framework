#!/usr/bin/env python3
"""C10 side check: an exactly flat range-1 Kuchar density that is only 2Z-covariant (staggered gauge).
Central Delta, chiral bracket {a_x,a_y} = 2 Delta_xy.  Odd sites: h_x = a_x^2/4.  Even sites: the odd-site
gauge flow conjugates a_x -> a_x - (u_{x+1} a_{x+1} - u_{x-1} a_{x-1})/2 (exact: odd a's commute at distance 2).
Checks F_xy = d_{u_y} h_x - d_{u_x} h_y + {h_x,h_y} = 0 identically.  Control: the opposite sign is not flat."""
import sympy as sp
PASS = FAIL = 0
for L in (4, 6, 8):
    a = sp.symbols(f"a0:{L}"); u = sp.symbols(f"u0:{L}")
    D = lambda i, j: {1: sp.Rational(1, 2), L - 1: -sp.Rational(1, 2)}.get((j - i) % L, 0)
    pa = lambda F, G: sp.expand(sum(2 * D(i, j) * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L)))
    for eps, expect in [(-1, True), (1, False)]:
        h = [a[x]**2 / 4 if x % 2 else (a[x] + eps * (u[(x + 1) % L] * a[(x + 1) % L] - u[(x - 1) % L] * a[(x - 1) % L]) / 2)**2 / 4 for x in range(L)]
        ok = all(sp.expand(sp.diff(h[x], u[y]) - sp.diff(h[y], u[x]) + pa(h[x], h[y])) == 0 for x in range(L) for y in range(L))
        good = ok == expect
        PASS += good; FAIL += (not good)
        print(f"[{'PASS' if good else 'FAIL'}] L={L} eps={eps}: staggered h flat = {ok} (expected {expect})")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
