#!/usr/bin/env python3
"""C10 check, Model P (lattice PFT) and the Kuchar/recombination lemmas.  New code.
Full phase space (phi_x, pi_x; u+_x, Pi+_x; u-_x, Pi-_x); no reduced a-bracket is assumed."""
import sympy as sp, itertools
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

def make(L, dd):
    Dl = sp.Matrix(L, L, lambda x, y: dd.get((y - x) % L, 0))
    f = sp.symbols(f"f0:{L}"); p = sp.symbols(f"p0:{L}")
    u = sp.symbols(f"u0:{L}"); Pi = sp.symbols(f"Pi0:{L}"); v = sp.symbols(f"v0:{L}"); Pv = sp.symbols(f"Pv0:{L}")
    pairs = list(zip(f, p)) + list(zip(u, Pi)) + list(zip(v, Pv))
    def pb(F, G):
        return sp.expand(sum(sp.diff(F, q) * sp.diff(G, P) - sp.diff(F, P) * sp.diff(G, q) for q, P in pairs))
    Df = [sum(Dl[x, y] * f[y] for y in range(L)) for x in range(L)]
    gp = [1 + sum(Dl[x, y] * u[y] for y in range(L)) for x in range(L)]
    gm = [1 + sum(Dl[x, y] * v[y] for y in range(L)) for x in range(L)]
    a = [p[x] + Df[x] for x in range(L)]; b = [p[x] - Df[x] for x in range(L)]
    Cp = [sp.expand(Pi[x] * gp[x] + a[x]**2 / 4) for x in range(L)]
    Cm = [sp.expand(Pv[x] * gm[x] - b[x]**2 / 4) for x in range(L)]
    return dict(Dl=Dl, f=f, p=p, u=u, Pi=Pi, v=v, Pv=Pv, pb=pb, a=a, b=b, gp=gp, gm=gm, Cp=Cp, Cm=Cm)

d1, d2 = sp.symbols("d1 d2")
CEN5 = {1: sp.Rational(1, 2), 4: -sp.Rational(1, 2)}
FWD5 = {1: 1, 0: -1}
AS5 = {1: d1, 4: -d1, 2: d2, 3: -d2}

# ---- (b1) on-shell anomaly for antisymmetric Delta (central L=5, general antisym L=5, central L=6)
for L, dd, lab in [(5, CEN5, "central"), (5, AS5, "general antisym"), (6, {1: sp.Rational(1, 2), 5: -sp.Rational(1, 2)}, "central")]:
    M = make(L, dd); Dl = M["Dl"]
    onsh = {M["Pi"][x]: -M["a"][x]**2 / (4 * M["gp"][x]) for x in range(L)}
    onsh.update({M["Pv"][x]: M["b"][x]**2 / (4 * M["gm"][x]) for x in range(L)})
    ok = True
    for x in range(L):
        for y in range(L):
            w = M["pb"](M["Cp"][x], M["Cp"][y]).subs(onsh)
            pred = -Dl[x, y] * (M["a"][x] * M["gp"][y] - M["a"][y] * M["gp"][x])**2 / (4 * M["gp"][x] * M["gp"][y])
            ok &= sp.cancel(sp.together(w - pred)) == 0
            ok &= M["pb"](M["Cp"][x], M["Cm"][y]) == 0
    check(f"P-anom L={L} {lab}: on shell {{C+x,C+y}} = -D_xy (a_x g_y - a_y g_x)^2/(4 g_x g_y); {{C+,C-}} = 0", ok)
# forward: {C+x,C-y} = -S_xy a_x b_y / 4 (strong)
L = 5; M = make(L, FWD5); Dl = M["Dl"]; S = Dl + Dl.T
ok = all(sp.expand(M["pb"](M["Cp"][x], M["Cm"][y]) + S[x, y] * M["a"][x] * M["b"][y] / 4) == 0 for x in range(L) for y in range(L))
check("P-anom L=5 forward: {C+x,C-y} = -S_xy a_x b_y/4 strongly", ok)

# ---- (b2) rational non-vanishing points: reconstruct the C10 log's point (values r/7, r cycling 1,-2,3,5,-1,4,2
#      over phi, pi, u+, u- in that order; Pi+- fixed on shell)
for L, dd, lab, expect, extra in [(5, FWD5, "forward", sp.Rational(3, 784), {}),
                                  (5, CEN5, "central", sp.Rational(34583, 570752), {}),
                                  (5, AS5, "range-2 (d1=2/3,d2=-1/12)", sp.Rational(2591839, 24618825), {d1: sp.Rational(2, 3), d2: -sp.Rational(1, 12)})]:
    M = make(L, dd)
    cyc = itertools.cycle([1, -2, 3, 5, -1, 4, 2])
    vals = {s: sp.Rational(next(cyc), 7) for s in list(M["f"]) + list(M["p"]) + list(M["u"]) + list(M["v"])}
    vals.update(extra)
    gpv = [sp.sympify(g).subs(vals) for g in M["gp"]]; gmv = [sp.sympify(g).subs(vals) for g in M["gm"]]
    av = [sp.sympify(t).subs(vals) for t in M["a"]]; bv = [sp.sympify(t).subs(vals) for t in M["b"]]
    vals.update({M["Pi"][x]: -av[x]**2 / (4 * gpv[x]) for x in range(L)})
    vals.update({M["Pv"][x]: bv[x]**2 / (4 * gmv[x]) for x in range(L)})
    on = all(c.subs(vals) == 0 for c in M["Cp"] + M["Cm"]) and all(g != 0 for g in gpv + gmv)
    H = [M["Cp"][x] - M["Cm"][x] for x in range(L)]
    hb = M["pb"](H[0], H[1]).subs(vals)
    check(f"P-point L=5 {lab}: point on Sigma (g != 0), {{H_0,H_1}} = {hb}", on and hb == expect, f"expected {expect}")
    if lab == "forward":
        # decompose: on-shell {C+0,C+1}, {C-0,C-1}, cross terms
        cpp = M["pb"](M["Cp"][0], M["Cp"][1]).subs(vals); cmm = M["pb"](M["Cm"][0], M["Cm"][1]).subs(vals)
        cx = (M["pb"](M["Cp"][0], M["Cm"][1]) + M["pb"](M["Cm"][0], M["Cp"][1])).subs(vals)
        print(f"      forward point: {{C+0,C+1}}={cpp}  {{C-0,C-1}}={cmm}  -({{C+0,C-1}}+{{C-0,C+1}})={-cx}  g+={gpv} a={av}")
# a simpler independent point for the forward difference: look for a small-integer point where only the cross term acts
L = 5; M = make(L, FWD5)
vals = {s: 0 for s in list(M["f"]) + list(M["u"]) + list(M["v"])}
vals.update({M["p"][x]: [1, 2, 0, 0, 0][x] for x in range(L)})
av = [sp.sympify(t).subs(vals) for t in M["a"]]; bv = [sp.sympify(t).subs(vals) for t in M["b"]]
vals.update({M["Pi"][x]: -av[x]**2 / 4 for x in range(L)}); vals.update({M["Pv"][x]: bv[x]**2 / 4 for x in range(L)})
H = [M["Cp"][x] - M["Cm"][x] for x in range(L)]
hb = M["pb"](H[0], H[1]).subs(vals)
check("P-point L=5 forward, own point (u=v=0, phi=0, pi=(1,2,0,0,0)): {H_0,H_1} != 0", hb != 0 and all(c.subs(vals) == 0 for c in M["Cp"] + M["Cm"]), f"= {hb}")

# ---- (b3) L4 recombination identity with a non-trivial abelian K (matter + u-gradient):
#      K_x = Pi_x + f_x^2 + dW/du_x,  W = sum u_x^2 u_{x+1};  C_x = g_x K_x
for L, dd, lab in [(5, CEN5, "central"), (5, FWD5, "forward"), (4, {r: sp.Symbol(f"c{r}") for r in range(4)}, "generic circulant")]:
    M = make(L, dd); Dl = M["Dl"]; u = M["u"]
    W = sum(u[x]**2 * u[(x + 1) % L] for x in range(L))
    K = [M["Pi"][x] + M["f"][x]**2 + sp.diff(W, u[x]) for x in range(L)]
    okab = all(M["pb"](K[x], K[y]) == 0 for x in range(L) for y in range(L))
    C = [sp.expand(M["gp"][x] * K[x]) for x in range(L)]
    ok = all(sp.expand(M["pb"](C[x], C[y]) - (Dl[x, y] * M["gp"][y] * K[x] - Dl[y, x] * M["gp"][x] * K[y])) == 0 for x in range(L) for y in range(L))
    check(f"L4 L={L} {lab}: K abelian and {{g_x K_x, g_y K_y}} = D_xy g_y K_x - D_yx g_x K_y", okab and ok)
# zeroth-order constants at g=1 in Fourier: c(m,n) = lam_n - lam_m (exact cyclotomic check, L=5..8, central & forward)
w = sp.Symbol("w")
okF = True
for L in range(5, 9):
    Phi = sp.cyclotomic_poly(L, w)
    for dd in [{1: sp.Rational(1, 2), L - 1: -sp.Rational(1, 2)}, {1: 1, 0: -1}]:
        lam = lambda n: sum(c * w**((n * r) % L) for r, c in dd.items())
        for m_ in range(L):
            for n_ in range(L):
                # {C_m, C_n} = sum_{x,y} w^{mx+ny} (D_xy C_x - D_yx C_y); coefficient of C_0 (x=0 term of first, y=0 of second)
                coef = sum(w**((n_ * y) % L) * dd.get(y % L, 0) for y in range(L)) - sum(w**((m_ * x) % L) * dd.get(x % L, 0) for x in range(L))
                okF &= sp.rem(sp.expand(coef - (lam(n_) - lam(m_))), Phi, w) == 0
        okF &= sp.rem(sp.expand(lam(1)), Phi, w) != 0 and sp.rem(sp.expand(lam(1) - lam(L - 1)), Phi, w) != 0
check("L4 Fourier: c(m,n) = lam_n - lam_m, Lambda_n = lam_n, (S) holds (central, forward, L=5-8)", okF)

# ---- (b4) P4a curvature, in the full phase space: K_x = Pi_x + a_x^2/(4 g_x), F_xy = {K_x,K_y}
for L, dd, lab in [(5, CEN5, "central"), (5, AS5, "general antisym"), (6, {1: sp.Rational(1, 2), 5: -sp.Rational(1, 2)}, "central")]:
    M = make(L, dd); Dl = M["Dl"]
    K = [M["Pi"][x] + M["a"][x]**2 / (4 * M["gp"][x]) for x in range(L)]
    vv = [M["a"][x] / M["gp"][x] for x in range(L)]
    ok = all(sp.cancel(sp.together(M["pb"](K[x], K[y]) + Dl[x, y] * (vv[x] - vv[y])**2 / 4)) == 0 for x in range(L) for y in range(L))
    check(f"P4a L={L} {lab}: F_xy = {{K_x,K_y}} = -D_xy (v_x - v_y)^2/4, v = a/g", ok)
# L3 numerical illustration: {K_x,K_y} for K = Pi + h(u, matter) has no Pi-dependence (generic h)
L = 3; M = make(L, CEN5 if False else {1: sp.Rational(1, 2), 2: -sp.Rational(1, 2)})
h = [M["u"][0] * M["f"][1]**2 + M["p"][x] * M["u"][(x + 1) % 3]**2 + M["f"][x] * M["p"][(x + 2) % 3] for x in range(3)]
K = [M["Pi"][x] + h[x] for x in range(3)]
check("L3 Kuchar form: {K_x,K_y} independent of Pi (so weak = strong vanishing)",
      all(not M["pb"](K[x], K[y]).has(*M["Pi"]) for x in range(3) for y in range(3)))
print(f"TOTAL chk_P: PASS={PASS} FAIL={FAIL}")
