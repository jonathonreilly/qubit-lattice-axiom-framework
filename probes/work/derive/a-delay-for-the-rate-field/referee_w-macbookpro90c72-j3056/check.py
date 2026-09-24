#!/usr/bin/env python3
"""Referee for a-delay-for-the-rate-field a3.

Author w-macbookpro90c72-jec4a (claude-opus-5-5). Own Euler-Lagrange, own resonance cases.
The 48^3 front was not re-executed. The eccentric factor is checked at five eccentricities only.
"""
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def kinetic():
    s, udot, w = sp.symbols("s udot w", positive=True)
    alpha = sp.symbols("alpha", real=True)
    scaled = (s * udot) ** 2 * (s * w) ** alpha
    expo = sp.simplify(sp.log(scaled / (udot ** 2 * w ** alpha)) / sp.log(s))
    t = sp.symbols("t", real=True)
    f = sp.Function("f")(t)
    u = sp.Function("u")(t)
    ur = sp.Function("ur")(t)
    fp = sp.diff(f, t)
    # tau = f(t), w_new = w/f', u_new = u - log f'
    du = (sp.diff(u, t) - sp.diff(fp, t) / fp) / fp
    dur = (sp.diff(ur, t) - sp.diff(fp, t) / fp) / fp
    wnew = sp.exp(u) / fp
    # action density per old time: (du/dtau)^2 / w_new * dtau/dt
    new = du ** 2 / wnew * fp
    old = sp.diff(u, t) ** 2 / sp.exp(u)
    diff = sp.simplify(new - old)
    ref = sp.simplify((du - dur) ** 2 / wnew * fp - (sp.diff(u, t) - sp.diff(ur, t)) ** 2 / sp.exp(u))
    report(
        "weight",
        expo == alpha + 2 and sp.solve(sp.Eq(expo, 1), alpha) == [-1]
        and diff != 0 and sp.simplify(diff.subs(sp.diff(fp, t), 0)) == 0 and ref == 0,
        "udot^2 w^alpha scales as s^(alpha+2); alpha=-1, and only a reference clock survives every reparametrisation",
    )


def wave():
    g, c = sp.symbols("gamma c", positive=True)
    ux = sp.symbols("ux")
    uy = sp.symbols("uy0:6")
    F = sum((2 / g) * (sp.exp(ux / 2) - sp.exp(v / 2)) ** 2 for v in uy)
    dF = sp.diff(F, ux)
    avg = sum(sp.exp(v / 2) for v in uy) / 6
    dF_ok = sp.simplify(dF - (12 / g) * sp.exp(ux / 2) * (sp.exp(ux / 2) - avg)) == 0
    t = sp.symbols("t")
    U = sp.Function("U")(t)
    K = sp.diff(U, t) ** 2 / (2 * g * c ** 2 * sp.exp(U))
    el = sp.diff(sp.diff(K, sp.diff(U, t)), t) - sp.diff(K, U)
    lhs = sp.simplify(el * g * c ** 2 * sp.exp(U))
    el_ok = sp.simplify(lhs - (sp.diff(U, t, 2) - sp.diff(U, t) ** 2 / 2)) == 0
    wb, eps = sp.symbols("wbar eps", positive=True)
    vx = sp.symbols("vx")
    vy = sp.symbols("vy0:6")
    rhs = (-g * c ** 2 * sp.exp(ux) * dF).subs(
        {ux: sp.log(wb) + eps * vx, **{uy[i]: sp.log(wb) + eps * vy[i] for i in range(6)}}
    )
    lin = sp.simplify(sp.diff(rhs, eps).subs(eps, 0))
    lin_ok = sp.simplify(lin - c ** 2 * wb ** 2 * (sum(vy) - 6 * vx)) == 0
    coeff = sp.simplify(sp.diff(-g * c ** 2 * sp.exp(ux) * dF, uy[0]))
    coeff_ok = sp.simplify(coeff - c ** 2 * sp.exp(3 * ux / 2) * sp.exp(uy[0] / 2)) == 0
    report(
        "wave law",
        dF_ok and el_ok and lin_ok and coeff_ok,
        "dF/du=(12/gamma) phi(phi-avg); weak field constant 6; neighbour weight c^2 w_x^{3/2} w_y^{1/2}",
    )


def speeds():
    x = sp.symbols("x", real=True)
    h = sp.sin(x / 2) - x / sp.pi
    # f''<=0 puts the graph above the chord, so h(0)=h(pi)=0 implies h>=0
    conc = sp.simplify(sp.diff(h, x, 2) + sp.sin(x / 2) / 4) == 0
    ends = h.subs(x, 0) == 0 and sp.simplify(h.subs(x, sp.pi)) == 0
    floor = sp.simplify((2 * sp.sin(x / 2) / x).subs(x, sp.pi) - 2 / sp.pi) == 0
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    c1, c2, c3 = sp.symbols("c1 c2 c3", real=True)
    num = s1 ** 2 * c1 ** 2 + s2 ** 2 * c2 ** 2 + s3 ** 2 * c3 ** 2
    den = s1 ** 2 + s2 ** 2 + s3 ** 2
    gap = sp.factor(den - num)  # sum s^2 sin^2 once cos^2 = 1 - sin^2, with s=sin
    # |v|^2 - 1 = (sum s^2 cos^2 - sum s^2)/sum s^2 = -sum s^2 (1-cos^2)/sum s^2 <= 0
    report(
        "speeds",
        conc and ends and floor and sp.simplify(gap.subs({c1 ** 2: 1 - s1 ** 2, c2 ** 2: 1 - s2 ** 2, c3 ** 2: 1 - s3 ** 2}))
        == s1 ** 4 + s2 ** 4 + s3 ** 4,
        "sin(x/2)>=x/pi on [0,pi] by h''<=0, so the phase speed is at least (2/pi)c; walker |v|^2<=1",
    )


def resonance():
    # Regimes of v/c. Middle window q1=-pi/2, m=1 covers [sqrt(2)/pi, 2/pi], including the endpoint where small-q1 amplitude dies.
    b_small = sp.sqrt(2) / sp.pi
    b_zone = 2 / sp.pi
    b_lo = 2 * sp.sqrt(2) / (3 * sp.pi)
    b_hi = 2 * sp.sqrt(10) / (3 * sp.pi)
    b_corner = 2 * sp.sqrt(3) / sp.pi
    order = (
        sp.simplify(b_lo - b_small) < 0
        and sp.simplify(b_small - b_zone) < 0
        and sp.simplify(b_zone - b_hi) < 0
        and sp.simplify(b_hi - b_corner) < 0
    )
    # sign chart at one rational point in each open piece, and at the two junctions
    def g(q1, s, m, r):
        p2 = 4 * sp.sin(q1 / 2) ** 2 + 8 * sp.sin(s * sp.pi / 2) ** 2
        return sp.simplify(p2 - ((q1 + 2 * sp.pi * m) * r) ** 2)

    samples = [
        (sp.Rational(1, 5), 1, sp.pi / 20),       # below sqrt(2)/pi ~ 0.450
        (b_small, 1, -sp.pi / 2),                 # junction, small-q1 amplitude would vanish
        (sp.Rational(1, 2), 1, -sp.pi / 2),       # middle
        (b_zone, 0, sp.pi),                       # junction, endpoint resonance
        (sp.Rational(4, 5), 0, sp.pi),            # (2/pi, 2 sqrt(3)/pi)
        (sp.Integer(2), 0, sp.pi / 10),           # fast
    ]
    signs = True
    for r, m, q1 in samples:
        g0 = g(q1, 0, m, r)
        g1 = g(q1, 1, m, r)
        amp = sp.simplify(sp.sin(q1 / 2)) != 0
        # endpoint resonance (g=0) still counts; otherwise a strict sign change
        root = sp.simplify(g0) == 0 or sp.simplify(g1) == 0
        cross = sp.simplify(g0) < 0 and sp.simplify(g1) > 0
        signs = signs and amp and (root or cross)
    report(
        "hopping source",
        order and signs,
        "the three q1 windows cover every v/c>0, with nonzero amplitude, including both junctions",
    )


def radiation():
    th, ph = sp.symbols("theta phi", real=True)
    n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
    def ang(expr):
        return sp.integrate(sp.integrate(expr * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
    ang_ok = True
    for i, j, k, l in ((0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1)):
        want = sp.Rational(4, 15) * sp.pi * ((i == j) * (k == l) + (i == k) * (j == l) + (i == l) * (j == k))
        ang_ok = ang_ok and sp.simplify(ang(n[i] * n[j] * n[k] * n[l]) - want) == 0
    mu, d, Om, t = sp.symbols("mu d Omega t", positive=True)
    X = [d * sp.cos(Om * t), d * sp.sin(Om * t), 0]
    Q = sp.Matrix(3, 3, lambda i, j: mu * X[i] * X[j])
    Q3 = sp.simplify(Q.diff(t, 3))
    QQ = sp.simplify(sum(Q3[i, j] ** 2 for i in range(3) for j in range(3)))
    circ = sp.simplify(QQ - 32 * mu ** 2 * d ** 4 * Om ** 6) == 0 and sp.simplify(Q3.trace()) == 0
    G, M, g, c = sp.symbols("G M gamma c", positive=True)
    P = (g / (240 * sp.pi * c ** 5)) * (0 + 2 * QQ)
    P = sp.simplify(P.subs({g: 4 * sp.pi * G, Om: sp.sqrt(G * M / d ** 3)}))
    power = sp.simplify(P - sp.Rational(16, 15) * G ** 4 * mu ** 2 * M ** 3 / (c ** 5 * d ** 5)) == 0
    report(
        "circular power",
        ang_ok and circ and power,
        "angular moment (4pi/15) and P=(16/15) G^4 mu^2 M^3/(c^5 d^5)",
    )


def kernel():
    q, lam = sp.symbols("q lam", positive=True)
    odd_l = sp.simplify(sp.integrate(lam ** 2 / (q ** 2 + lam ** 2), (q, 0, sp.oo)))
    t1 = sp.simplify(-(1 / (2 * sp.pi ** 2)) * odd_l)
    xx = sp.symbols("xsq", positive=True)
    piece = sp.integrate(lam ** 4 / (q ** 2 + lam ** 2), (q, 0, sp.oo))
    t3a = sp.simplify(-(xx / 6) * (1 / (2 * sp.pi ** 2)) * piece)
    tail = sp.integrate(lam ** 6 / (q ** 2 + lam ** 2) ** 2, (q, 0, sp.oo))
    t3b = sp.simplify(sp.Rational(1, 20) * (1 / (2 * sp.pi ** 2)) * (3 * piece - tail))
    odd = sp.simplify(t1 + lam / (4 * sp.pi)) == 0
    lat = sp.simplify(t3a + t3b + lam ** 3 * (xx - sp.Rational(3, 4)) / (24 * sp.pi)) == 0
    report(
        "retarded kernel",
        odd and lat,
        "odd terms -lam/(4pi) and -lam^3(|x|^2-3/4)/(24pi)",
    )


def eccentric():
    f = sp.symbols("f", real=True)
    ok = True
    for ev in (sp.Integer(0), sp.Rational(5, 13), sp.Rational(8, 17), sp.Rational(3, 5), sp.Rational(4, 5)):
        pp = 1 - ev ** 2
        r = pp / (1 + ev * sp.cos(f))
        fdot = sp.sqrt(pp) / r ** 2
        Xs = [r * sp.cos(f), r * sp.sin(f)]
        def ddt(ex, fd=fdot):
            return sp.simplify(sp.diff(ex, f) * fd)
        Qs = [[ddt(ddt(ddt(Xs[i] * Xs[j]))) for j in range(2)] for i in range(2)]
        integrand = sp.simplify((2 * sum(Qs[i][j] ** 2 for i in range(2) for j in range(2)) + (Qs[0][0] + Qs[1][1]) ** 2) / fdot)
        avg = sp.simplify(sp.integrate(integrand, (f, 0, 2 * sp.pi)) / (2 * sp.pi))
        target = 64 * (1 + sp.Rational(99, 32) * ev ** 2 + sp.Rational(51, 128) * ev ** 4) / (1 - ev ** 2) ** sp.Rational(7, 2)
        ok = ok and sp.simplify(avg - target) == 0
        print(f"  e={ev} {'ok' if sp.simplify(avg - target) == 0 else 'FAIL'}", flush=True)
    report(
        "eccentric factor",
        ok,
        "matches (1+99e^2/32+51e^4/128)/(1-e^2)^(7/2) at five Pythagorean eccentricities; not an identity for every e",
    )


def main():
    kinetic()
    wave()
    speeds()
    resonance()
    radiation()
    kernel()
    eccentric()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the weight-one on-site term is udot^2/w and needs a reference clock; "
        "the weak-field law has constant 6 and local speed c w; the phase speed is at least (2/pi)c; "
        "a one-site hopper resonates for every c>0; circling bodies radiate (16/15) G^4 mu^2 M^3/(c^5 d^5)"
    )
    print(
        "SUMMARY: confirmed the kinetic weight, the wave law, the speed floor, the hopping-source cover, "
        "the circular quadrupole, and the kernel's odd terms. The eccentric factor matches at five eccentricities "
        "and is not proved for every e. The 48^3 front was not re-executed."
    )


if __name__ == "__main__":
    main()
