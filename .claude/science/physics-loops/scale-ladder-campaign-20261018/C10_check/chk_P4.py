# P4a for general antisymmetric Delta (L=5, d1,d2) and central L=6, with g_x as independent symbols G_x
# and the chain rule d/du_y = sum_z Delta_zy d/dG_z; a = pi + Delta phi in full (phi,pi) phase space.  Plus L3.
import sympy as sp
PASS = FAIL = 0
def check(n, ok):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}", flush=True)
d1, d2 = sp.symbols("d1 d2")
for L, dd, lab in [(5, {1: d1, 4: -d1, 2: d2, 3: -d2}, "general antisym"), (6, {1: sp.Rational(1, 2), 5: -sp.Rational(1, 2)}, "central")]:
    Dl = sp.Matrix(L, L, lambda x, y: dd.get((y - x) % L, 0))
    f = sp.symbols(f"f0:{L}"); p = sp.symbols(f"p0:{L}"); G = sp.symbols(f"G0:{L}")
    a = [p[x] + sum(Dl[x, y] * f[y] for y in range(L)) for x in range(L)]
    pb = lambda F, H: sum(sp.diff(F, q) * sp.diff(H, P) - sp.diff(F, P) * sp.diff(H, q) for q, P in zip(f, p))
    du = lambda F, y: sum(Dl[z, y] * sp.diff(F, G[z]) for z in range(L))
    h = [a[x]**2 / (4 * G[x]) for x in range(L)]
    ok = True
    for x in range(L):
        for y in range(x + 1, L):
            F = du(h[x], y) - du(h[y], x) + pb(h[x], h[y])
            ok &= sp.expand((F + Dl[x, y] * (a[x] / G[x] - a[y] / G[y])**2 / 4) * 4 * G[x]**2 * G[y]**2) == 0
    check(f"P4a L={L} {lab}: F_xy = -D_xy (v_x - v_y)^2/4 (chain-rule encoding)", ok)
u = sp.symbols("u0:3"); Pi = sp.symbols("Pi0:3"); f = sp.symbols("f0:3"); p = sp.symbols("p0:3")
pairs = list(zip(f, p)) + list(zip(u, Pi))
pbf = lambda F, H: sp.expand(sum(sp.diff(F, q) * sp.diff(H, P) - sp.diff(F, P) * sp.diff(H, q) for q, P in pairs))
h = [u[0] * f[1]**2 + p[x] * u[(x + 1) % 3]**2 + f[x] * p[(x + 2) % 3] for x in range(3)]
K = [Pi[x] + h[x] for x in range(3)]
check("L3 Kuchar form: {K_x,K_y} independent of Pi", all(not pbf(K[x], K[y]).has(*Pi) for x in range(3) for y in range(3)))
print(f"TOTAL chk_P4: PASS={PASS} FAIL={FAIL}")
