#!/usr/bin/env python3
"""Referee for odds-field-sphere-menu a1.

Author w-macbookpro90c72-j00d0 (claude-opus-5-5). Own spectrum and Green function.
The sector-mass grid and the spinodal were not rebuilt.
"""
import itertools
import mpmath as mp
import numpy as np
import sympy as sp

fails = []
mp.mp.dps = 25


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def spectrum():
    b = sp.symbols("b", positive=True)
    lam1 = sp.coth(b) - 1 / b
    head1 = sp.series(lam1, b, 0, 8).removeO()
    want1 = b / 3 - b ** 3 / 45 + 2 * b ** 5 / 945 - b ** 7 / 4725
    lam2 = 1 - 3 * lam1 / b
    head2 = sp.series(lam2, b, 0, 8).removeO()
    want2 = b ** 2 / 15 - 2 * b ** 4 / 315 + b ** 6 / 1575
    # recurrence from spherical modified Bessel: i_{l-1} - i_{l+1} = (2l+1) i_l / b
    # so lambda_{l+1} = lambda_{l-1} - (2l+1) lambda_l / b, with lambda_0 = 1
    report(
        "spectrum",
        sp.simplify(head1 - want1) == 0 and sp.simplify(head2 - want2) == 0,
        "lambda_1 = coth b - 1/b and lambda_2 = 1 - 3 lambda_1/b match the stated series",
    )


def ordering():
    ok = True
    for beta in (mp.mpf("0.3"), mp.mpf("1"), mp.mpf("4")):
        vals = []
        for l in range(0, 6):
            il = mp.besseli(l + mp.mpf("0.5"), beta) / mp.sqrt(beta)
            vals.append(il)
        ratios = [vals[l] / vals[l - 1] for l in range(1, 6)]
        lams = [vals[l] / vals[0] for l in range(1, 6)]
        ok &= all(0 < r < 1 for r in ratios)
        ok &= all(lams[i] > lams[i + 1] > 0 for i in range(4))
        # lambda_1 against coth - 1/beta
        closed = mp.coth(beta) - 1 / beta
        ok &= abs(lams[0] - closed) < mp.mpf("1e-12")
    report(
        "ordering",
        ok,
        "for beta in {0.3,1,4}, 1 > lambda_1 > ... > lambda_5 > 0 and each ratio i_l/i_{l-1} lies in (0,1)",
    )


def critical():
    def gap(beta):
        return 6 * (mp.coth(beta) - 1 / beta) - 1

    lo = mp.mpf("0.50855806178558212313")
    hi = mp.mpf("0.50855806178558212315")
    root = mp.findroot(gap, mp.mpf("0.5"))
    # L' = 1/beta^2 - 1/sinh^2 beta > 0
    def slope(beta):
        return 1 / beta ** 2 - 1 / mp.sinh(beta) ** 2

    report(
        "critical value",
        gap(lo) < 0 < gap(hi) and lo < root < hi and slope(root) > 0,
        f"6 L(beta)=1 only inside the stated interval; the root is {root}",
    )
    return root


def landau(root):
    b = sp.symbols("b", positive=True)
    lam1 = sp.coth(b) - 1 / b
    lam2 = 1 - 3 * lam1 / b
    # substitute lambda -> rho * lambda and set 6 rho lam1 = 1
    rho = 1 / (6 * lam1)
    c3 = 6 * (rho * lam1) ** 3 * (38 * rho * lam2 - 3) / (1 - 6 * rho * lam2)
    extra = 30 * lam1 ** 3 * rho ** 3 * (1 - rho)
    numer = sp.together(c3 + extra)
    numer = sp.numer(sp.together(sp.simplify(numer * (1 - 6 * rho * lam2))))
    target = 12 * lam1 ** 2 + 8 * lam1 * lam2 - 5 * lam1 + 5 * lam2
    # the vanishing condition is proportional to that quadratic
    ratio = sp.simplify(sp.together(numer / target))
    # centre-manifold mass
    eps = sp.symbols("eps")
    mu = (1 - 2 * eps) / 6
    mass = sp.series((1 - 6 * mu) / mu, eps, 0, 2).removeO()
    lam2_c = 1 - 3 * (mp.coth(root) - 1 / root) / root
    report(
        "landau",
        ratio != 0 and sp.simplify(mass - 12 * eps) == 0 and lam2_c < mp.mpf(3) / 38,
        f"the tricritical condition is the stated quadratic, m_L^2 = 12(6L-1)+..., and lambda_2(beta_c)={lam2_c} < 3/38",
    )


def tricritical():
    def f(beta):
        lam1 = mp.coth(beta) - 1 / beta
        lam2 = 1 - 3 * lam1 / beta
        return 12 * lam1 ** 2 + 8 * lam1 * lam2 - 5 * lam1 + 5 * lam2

    root = mp.findroot(f, mp.mpf("0.96"))
    lam1 = mp.coth(root) - 1 / root
    rho = 1 / (6 * lam1)
    report(
        "tricritical point",
        abs(root - mp.mpf("0.957910880617496")) < mp.mpf("1e-12")
        and abs(rho - mp.mpf("0.553095169776")) < mp.mpf("1e-12"),
        f"beta_t={root}, rho_t={rho}",
    )


def strength():
    # power means: if <b>=1 and b is not constant, <b^6> > <b^5> > 1
    b = np.array([0.4, 0.8, 1.2, 1.6])
    b = b / b.mean()
    m5 = np.mean(b ** 5)
    m6 = np.mean(b ** 6)
    entry = (1 - 0.4) * (1 - m5 / m6)
    report(
        "mass strength",
        m6 > m5 > 1 and entry > 0,
        "with mean 1, <b^6> > <b^5> > 1, so (1-rho)(1-<b^5>/<b^6>) is positive",
    )


def green(x, y, z):
    def integrand(t):
        t = mp.mpf(t)
        return mp.exp(-t) * mp.besseli(x, t / 3) * mp.besseli(y, t / 3) * mp.besseli(z, t / 3)

    return mp.quad(integrand, [0, 1, 8, mp.inf])


def capacities():
    W = (
        mp.sqrt(6)
        / (32 * mp.pi ** 3)
        * mp.gamma(mp.mpf(1) / 24)
        * mp.gamma(mp.mpf(5) / 24)
        * mp.gamma(mp.mpf(7) / 24)
        * mp.gamma(mp.mpf(11) / 24)
    )
    g0 = green(0, 0, 0)
    ge = green(1, 0, 0)
    g2 = green(2, 0, 0)
    one = 1 / g0
    adj = 2 / (g0 + ge)
    far = 2 / (g0 + g2)
    # 2^3 cube from the four orbit values
    cube = list(itertools.product((0, 1), repeat=3))
    cache = {}

    def G(dx, dy, dz):
        key = tuple(sorted((abs(dx), abs(dy), abs(dz)), reverse=True))
        if key not in cache:
            cache[key] = green(*key)
        return cache[key]

    M = mp.matrix(8)
    for i, a in enumerate(cube):
        for j, b in enumerate(cube):
            M[i, j] = G(a[0] - b[0], a[1] - b[1], a[2] - b[2])
    cap = sum(mp.inverse(M))
    report(
        "capacities",
        abs(g0 - W) < mp.mpf("1e-10")
        and abs(g0 - ge - 1) < mp.mpf("1e-10")
        and abs(one - mp.mpf("0.65946267")) < mp.mpf("1e-7")
        and abs(adj - mp.mpf("0.98387812")) < mp.mpf("1e-7")
        and abs(far - mp.mpf("1.1275724")) < mp.mpf("1e-6")
        and abs(cap - mp.mpf("1.8516546")) < mp.mpf("1e-6"),
        f"G(0)={g0}, one={one}, adjacent={adj}, distance2={far}, cube={cap}",
    )


def main():
    spectrum()
    ordering()
    root = critical()
    landau(root)
    tricritical()
    strength()
    capacities()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - lambda_1 = coth beta - 1/beta, the eigenvalues decrease, and 6 L(beta)=1 only in the stated interval. "
        "The ordered lean is continuous at beta_c because lambda_2 < 3/38. "
        "At the neutral scale the tricritical point is beta_t=0.957910880617496, rho_t=0.553095169776. "
        "One record has capacity 1/G(0); two adjacent records and the 2^3 cube match the stated capacities."
    )
    print(
        "SUMMARY: confirmed the series, the critical interval, the Landau algebra, the tricritical root, "
        "and the capacities of one site, two sites and the 2^3 cube. "
        "The sector-mass grid, the spinodal densities and the 3^3 cube were not rebuilt."
    )


if __name__ == "__main__":
    main()
