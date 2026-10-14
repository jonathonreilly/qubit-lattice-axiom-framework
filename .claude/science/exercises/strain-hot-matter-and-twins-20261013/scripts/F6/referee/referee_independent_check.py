"""Independent F6 checks using analytic t-jets at t=0.

This deliberately does not call f6_lib's finite-t RK4 flows or its finite-
difference Hessian routines.  It uses only the archived band symbols and a
moderate composite Gauss-Legendre grid, processed one z slab at a time.
"""

import os
import sys
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "arch"))
sys.path.insert(0, os.path.join(HERE, "scripts"))

from r1934_lib import panels
from sublum import SymG, dsstep
from dirac import D1


BS = 2.526103698
BF = 0.909103708
RW = 0.555604226
BG = 2.9435


# Jets contain (value, first derivative, second derivative) with respect to t.
def jadd(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def jscale(a, c):
    return c * a[0], c * a[1], c * a[2]


def jmul(a, b):
    return (
        a[0] * b[0],
        a[1] * b[0] + a[0] * b[1],
        a[2] * b[0] + 2.0 * a[1] * b[1] + a[0] * b[2],
    )


def jpow(a, power):
    v = a[0]
    return (
        v**power,
        power * v ** (power - 1.0) * a[1],
        power * (power - 1.0) * v ** (power - 2.0) * a[1] ** 2
        + power * v ** (power - 1.0) * a[2],
    )


def jinv(a):
    return jpow(a, -1.0)


def jdiv(a, b):
    return jmul(a, jinv(b))


def jconst(v):
    z = np.zeros_like(v)
    return v, z, z


def sumj(items):
    out = items[0]
    for item in items[1:]:
        out = jadd(out, item)
    return out


def grid_gauge(n, hmax, mph):
    breaks = [BS, BG]
    breaks += [BG + i * (np.pi - BG) / mph for i in range(1, mph)]
    breaks += [BS + i * (np.pi - BS) / 6 for i in range(1, 6)]
    return panels(breaks, n, hmax)


def symg_flow_jets(law, x, sign, squared):
    """Jet of h(phi_t(x)) or h(phi_t(x))^2 for the SF time-1 map.

    phi'(0)=sign*p/2 and phi''(0)=p*p'/4, where p=h*h'.
    """
    h = law.h(x)
    hp = law.dh(x)
    hpp = -dsstep((x - law.b) / law.w) / law.w
    p = h * hp
    pp = hp * hp + h * hpp
    a = sign * p / 2.0
    b = p * pp / 4.0 if sign else np.zeros_like(x)
    if squared:
        g = h * h
        gp = 2.0 * p
        gpp = 2.0 * pp
        return g, gp * a, gpp * a * a + gp * b
    return h, hp * a, hpp * a * a + hp * b


def gauge_hessian(n, hmax, mph):
    x, w = grid_gauge(n, hmax, mph)
    scalar, photon = SymG(BS), SymG(BG)
    gs_1d = [symg_flow_jets(scalar, x, s, True) for s in (1, -1, 0)]
    dg_1d = [symg_flow_jets(photon, x, s, False) for s in (1, -1, 0)]
    total0 = 0.0
    total2 = 0.0
    quartic0 = 0.0
    quartic2 = 0.0
    for iz in range(len(x)):
        gs = [
            tuple(v[:, None, None] for v in gs_1d[0]),
            tuple(v[None, :, None] for v in gs_1d[1]),
            tuple(v[iz] for v in gs_1d[2]),
        ]
        dg = [
            tuple(v[:, None, None] for v in dg_1d[0]),
            tuple(v[None, :, None] for v in dg_1d[1]),
            tuple(v[iz] for v in dg_1d[2]),
        ]
        d2 = [jmul(d, d) for d in dg]
        k = sumj(gs)
        om = jpow(sumj(d2), 0.5)
        energy = jpow(k, 0.5)
        at = sumj([jdiv(gs[j], d2[j]) for j in range(3)])
        bt = sumj([jdiv(jmul(gs[j], gs[j]), d2[j]) for j in range(3)])
        tad = jscale(jdiv(at, om), 0.5)
        temp = jscale(jdiv(energy, jmul(om, jadd(om, energy))), 0.5)
        exch = jscale(jdiv(bt, jmul(jmul(om, energy), jadd(om, energy))), 0.5)
        integrand = jadd(jadd(tad, temp), jscale(exch, -1.0))
        scalar_prop = jscale(jpow(k, -0.5), 0.5)
        ww = w[:, None, None] * w[None, :, None] * w[iz]
        total0 += float(np.sum(ww * integrand[0]))
        total2 += float(np.sum(ww * integrand[2]))
        quartic0 += float(np.sum(ww * scalar_prop[0]))
        quartic2 += float(np.sum(ww * scalar_prop[2]))
    return len(x), total0, total2, quartic0, quartic2


def d2w_analytic(law, x):
    z = (x - law.b) / law.A.w
    st = np.clip(np.where(z <= 0, 0.0, np.where(z >= 1, 1.0, 0.0)), 0, 1)
    interior = (z > 0) & (z < 1)
    if np.any(interior):
        # Import the exact smooth step only where its ratio is nonsingular.
        from sublum import sstep

        st = st.astype(float)
        st[interior] = sstep(z[interior])
    dst = dsstep(z) / law.A.w
    # In the flat tails both numerator and denominator underflow.  The exact
    # C-infinity limit is zero, so evaluate the ratio only off those tails.
    core = interior & (st > 1e-14) & (st < 1.0 - 1e-14)
    ans = np.zeros_like(x)
    den = np.sqrt(st[core] * (1.0 - st[core]))
    ans[core] = law.r * dst[core] * (1.0 - 2.0 * st[core]) / den
    return ans


def composed_jet(value, first_k, second_k, phi1, phi2):
    return value, first_k * phi1, second_k * phi1**2 + first_k * phi2


def yukawa_hessian(n, hmax):
    x, w = panels([BF, np.pi - BF], n, hmax)
    law = D1(BF, RW)
    s = law.S(x)
    sp = law.dS(x)
    spp = law.d2S(x)
    W = law.W(x)
    Wp = law.dW(x)
    Wpp = d2w_analytic(law, x)
    total0 = 0.0
    total2 = 0.0
    condensate0 = 0.0
    condensate2 = 0.0
    for iz in range(len(x)):
        sx = s[:, None, None]
        sy = s[None, :, None]
        sz = s[iz]
        spx = sp[:, None, None]
        spy = sp[None, :, None]
        sppx = spp[:, None, None]
        sppy = spp[None, :, None]
        wx = W[:, None, None]
        wy = W[None, :, None]
        wz = W[iz]
        wpx = Wp[:, None, None]
        wpy = Wp[None, :, None]
        wppx = Wpp[:, None, None]
        wppy = Wpp[None, :, None]

        # The B1 flow uses m_flow=0.01, while the propagator itself is critical.
        mflow = 0.01 + wx + wy + wz
        px = sx * spx + mflow * wpx
        py = sy * spy + mflow * wpy
        hxx = spx**2 + sx * sppx + wpx**2 + mflow * wppx
        hyy = spy**2 + sy * sppy + wpy**2 + mflow * wppy
        hxy = wpx * wpy
        phix1 = px / 2.0
        phiy1 = -py / 2.0
        phix2 = (hxx * px - hxy * py) / 4.0
        phiy2 = (-hxy * px + hyy * py) / 4.0

        jsx = composed_jet(sx, spx, sppx, phix1, phix2)
        jsy = composed_jet(sy, spy, sppy, phiy1, phiy2)
        jsz = jconst(np.asarray(sz + 0.0 * px))
        jwx = composed_jet(wx, wpx, wppx, phix1, phix2)
        jwy = composed_jet(wy, wpy, wppy, phiy1, phiy2)
        jwz = jconst(np.asarray(wz + 0.0 * px))
        c2 = sumj([jmul(jsx, jsx), jmul(jsy, jsy), jmul(jsz, jsz)])
        mass = sumj([jwx, jwy, jwz])
        e2 = jadd(c2, jmul(mass, mass))
        integrand = jscale(jmul(c2, jpow(e2, -1.5)), -1.0)
        condensate = jscale(jmul(mass, jpow(e2, -0.5)), -2.0)
        ww = w[:, None, None] * w[None, :, None] * w[iz]
        total0 += float(np.sum(ww * integrand[0]))
        total2 += float(np.sum(ww * integrand[2]))
        condensate0 += float(np.sum(ww * condensate[0]))
        condensate2 += float(np.sum(ww * condensate[2]))
    return len(x), total0, total2, condensate0, condensate2


def nanograv_and_conversion():
    A = 2.4e-15
    fmax = 50.0
    # Exact power-law integral for one of five orthonormal traceless components.
    def variance(years):
        fmin = 1.0 / years
        integral_hc2 = A * A * 0.75 * (fmin ** (-4.0 / 3.0) - fmax ** (-4.0 / 3.0))
        return (2.0 / 5.0) * integral_hc2

    def ls_slope(years, window, nf=8000, nu=500):
        """RMS least-squares slope of Q_E by a one-lag covariance integral.

        For Q_E=(a^2+b^2)/2 with two independent equal-variance Gaussian
        components, Cov[Q_E(t),Q_E(s)]=C(t-s)^2.  Reducing the double time
        integral to lag u gives I(u)=T^3/12-T^2*u/4+u^3/6.
        """
        logf = np.linspace(np.log(1.0 / years), np.log(fmax), nf)
        f = np.exp(logf)
        hc2 = A * A * f ** (-4.0 / 3.0)
        dx = logf[1] - logf[0]
        freq_w = np.full(nf, dx)
        freq_w[[0, -1]] *= 0.5
        corr_w = (2.0 / 5.0) * hc2 * freq_w
        ug, uw = np.polynomial.legendre.leggauss(nu)
        u = 0.5 * window * (ug + 1.0)
        uw = 0.5 * window * uw
        corr = np.array([np.dot(corr_w, np.cos(2.0 * np.pi * f * lag)) for lag in u])
        overlap_moment = window**3 / 12.0 - window**2 * u / 4.0 + u**3 / 6.0
        variance_beta = (144.0 / window**6) * 2.0 * np.dot(uw, overlap_moment * corr**2)
        return np.sqrt(variance_beta)

    cH = 3.6811e-3
    MP, mH, fN = 1.22089e19, 125.1, 0.30
    kv = cH * MP**2 / (2.0 * mH**2)
    min_slope = ls_slope(16.0, 10.0)
    clock_rate = (1.0 - fN) * kv * min_slope
    return (
        variance(16.0),
        variance(30.0),
        min_slope,
        ls_slope(30.0, 10.0),
        kv,
        clock_rate,
        clock_rate / 3.6e-17,
    )


def main():
    print("Independent analytic-flow Hessians (one process; z-slab integration)")
    finest_gauge = None
    finest_quartic = None
    for cfg in [(6, 0.25, 6), (7, 0.20, 8)]:
        nodes, sig0, hess, gs0, gsh = gauge_hessian(*cfg)
        finest_gauge, finest_quartic = hess, gsh
        print(f"U1 n={cfg[0]} hmax={cfg[1]} mph={cfg[2]} nodes={nodes}: Sigma0={sig0:+.10f} Hess={hess:+.9e}; Gs0={gs0:+.10f} Gs_Hess={gsh:+.9e}")
    finest_c2 = None
    finest_yukawa = None
    for cfg in [(6, 0.25), (7, 0.20)]:
        nodes, y0, hess, c0, c2 = yukawa_hessian(*cfg)
        finest_yukawa, finest_c2 = hess, c2
        print(f"Yukawa B1 n={cfg[0]} hmax={cfg[1]} nodes={nodes}: Y0={y0:+.10f} Hess={hess:+.9e}; C0={c0:+.10f} C_Hess={c2:+.9e}")
    total = (0.75 * 0.26 + 0.25 * 0.21) * finest_gauge + 3.0 * 0.38**2 * finest_yukawa + 6.0 * (-0.013) * finest_quartic
    print(f"main c_H from independent finest-grid pieces: {total:+.9e}")
    v16, v30, slope16, slope30, kv, rate, ratio = nanograv_and_conversion()
    print(f"NANOGrav per-Eg-component variance: fmin=1/16 {v16:.9e}; fmin=1/30 {v30:.9e}")
    print(f"NANOGrav 10-yr LS slope rms: fmin=1/16 {slope16:.9e}/yr; fmin=1/30 {slope30:.9e}/yr")
    print(f"main |delta v/v| coefficient={kv:.9e}; conservative clock rate={rate:.9e}/yr; exceedance={ratio:.9e}")
    tadpole = 0.5 * (0.38 / np.sqrt(2.0)) * 3.0 * abs(finest_c2) * 1.22089e19**3 / (125.1**2 * 246.22)
    print(f"B1 tadpole |delta v/v| coefficient at y_t=0.38: {tadpole:.9e}")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes; Linux reports KiB. This packet runs on macOS.
    print(f"peak_rss_raw={rss}")


if __name__ == "__main__":
    main()
