#!/usr/bin/env python3
"""C10 check: staggered flat example, in the FULL phase space (phi, pi, u, Pi), a = pi + Delta phi, central Delta.
K_x = Pi_x + h_x;  flat <=> {K_x, K_y} = 0 identically.  Also: shift invariance and linear u-response."""
import sympy as sp
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
for L in (4, 6):
    f = sp.symbols(f"f0:{L}"); p = sp.symbols(f"p0:{L}"); u = sp.symbols(f"u0:{L}"); Pi = sp.symbols(f"Pi0:{L}")
    D = lambda i, j: {1: sp.Rational(1, 2), L - 1: -sp.Rational(1, 2)}.get((j - i) % L, 0)
    a = [p[x] + sum(D(x, y) * f[y] for y in range(L)) for x in range(L)]
    pairs = list(zip(f, p)) + list(zip(u, Pi))
    pb = lambda F, G: sp.expand(sum(sp.diff(F, q) * sp.diff(G, P) - sp.diff(F, P) * sp.diff(G, q) for q, P in pairs))
    for sgn, expect in [(-1, True), (1, False)]:
        h = [a[x]**2 / 4 if x % 2 == 1 else
             (a[x] + sgn * (u[(x + 1) % L] * a[(x + 1) % L] - u[(x - 1) % L] * a[(x - 1) % L]) / 2)**2 / 4 for x in range(L)]
        K = [Pi[x] + h[x] for x in range(L)]
        flat = all(pb(K[x], K[y]) == 0 for x in range(L) for y in range(x + 1, L))
        check(f"stag L={L} sign={sgn}: flat = {flat} (expected {expect})", flat == expect)
    h = [a[x]**2 / 4 if x % 2 == 1 else (a[x] - (u[(x + 1) % L] * a[(x + 1) % L] - u[(x - 1) % L] * a[(x - 1) % L]) / 2)**2 / 4 for x in range(L)]
    c = sp.Symbol("c")
    shift = all(sp.expand(h[x].subs({u[i]: u[i] + c for i in range(L)}, simultaneous=True) - h[x]) == 0 for x in range(L))
    check(f"stag L={L}: not shift invariant", not shift)
    # linear u-response at uniform a = A: even site -A^2 e_x/2, odd site 0; continuum a^2/(4g) gives -A^2 e/4
    A = sp.Symbol("A")
    sub = {p[x]: A for x in range(L)}; sub.update({f[x]: 0 for x in range(L)})
    e0 = (u[1] - u[L - 1]) / 2
    lin_even = sp.expand(sp.diff(h[0].subs(sub), u[1]) * u[1] + sp.diff(h[0].subs(sub), u[L - 1]) * u[L - 1]).subs({u[i]: 0 for i in range(L) if i not in (1, L - 1)})
    lin_even = sp.expand(sum(sp.diff(h[0].subs(sub), u[i]).subs({uu: 0 for uu in u}) * u[i] for i in range(L)))
    lin_odd = sp.expand(sum(sp.diff(h[1].subs(sub), u[i]).subs({uu: 0 for uu in u}) * u[i] for i in range(L)))
    check(f"stag L={L}: uniform-a linear response even site = -A^2 e/2, odd = 0 (continuum -A^2 e/4; matches only on the 2-site average)",
          sp.expand(lin_even + A**2 * e0 / 2) == 0 and lin_odd == 0, f"even={lin_even}, odd={lin_odd}")
print(f"TOTAL chk_stag: PASS={PASS} FAIL={FAIL}")
