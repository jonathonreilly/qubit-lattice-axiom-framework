#!/usr/bin/env python3
"""W2: the blocked near covariance, two ways.

For the map (B-1) as n -> infinity, the plaquette (a,b) flux is the average of
F_ab against rho_ab = tri(x_a - 1/2) tri(x_b - 1/2) box(x_c) box(x_d), with
tri = box*box. Parallel plaquettes at offset z:

  P_infinity(z) = int R(w) M(z - w) dw,
  R = T4(w_a) T4(w_b) T2(w_c) T2(w_d), T2 = box*box, T4 = box*4,
  M(x) = (1/(pi^2 r^4)) (1 - 2 (x_a^2 + x_b^2) / r^2).

Position side: exact spline masses on sub-boxes and monotone bounds of the
kernel on each sub-box give an enclosure. Fourier side: (B-4) by Schwinger
parameter, 1/|p|^2 = int_0^inf exp(-t |p|^2) dt, so the 4d integral factorizes.
"""
import json, os, resource, sys
import numpy as np

LIM = 2 * 1024**3


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    if rss > LIM:
        sys.exit("rss limit")


def cdf_T2(x):
    """CDF of box*box on [-1,1]."""
    x = np.clip(x, -1.0, 1.0)
    return np.where(x < 0, 0.5 * (1 + x) ** 2, 1 - 0.5 * (1 - x) ** 2)


def cdf_T4(x):
    """CDF of box*4 (cubic B-spline) on [-2,2], by exact piecewise formula."""
    x = np.clip(x, -2.0, 2.0)

    def left(u):  # u in [0,2], integral from -2 to -2+u ... use symmetry below
        # density of cubic B-spline b(y): for y in [-2,-1]: (2+y)^3/6; [-1,0]: (4-6y^2-3y^3)/6
        v = u - 2.0  # v in [-2,0]
        a = (v + 2.0) ** 4 / 24.0
        # mass to -1 is 1/24
        m1 = 1.0 / 24.0
        b = m1 + ((4 * (v + 1)) - 2 * (v ** 3 + 1) - 0.75 * (v ** 4 - 1)) / 6.0
        return np.where(v < -1.0, a, b)

    return np.where(x < 0, left(x + 2.0), 1.0 - left(2.0 - x))


def enclosure(z, n=(48, 48, 24, 24)):
    z = np.asarray(z, float)
    edges = []
    masses = []
    for ax in range(4):
        half = 2.0 if ax < 2 else 1.0
        e = np.linspace(-half, half, n[ax] + 1)
        c = cdf_T4(e) if ax < 2 else cdf_T2(e)
        edges.append(e)
        masses.append(np.diff(c))
    # x = z - w, so box in x
    xlo = [z[ax] - edges[ax][1:] for ax in range(4)]
    xhi = [z[ax] - edges[ax][:-1] for ax in range(4)]
    # square ranges per axis
    lo2 = []
    hi2 = []
    for ax in range(4):
        a, b = xlo[ax], xhi[ax]
        l = np.where((a <= 0) & (b >= 0), 0.0, np.minimum(a * a, b * b))
        h = np.maximum(a * a, b * b)
        lo2.append(l)
        hi2.append(h)
    if (lo2[0].min() + lo2[1].min() + lo2[2].min() + lo2[3].min()) <= 0:
        raise ValueError("kernel singular on the support")
    lo_sum = hi_sum = 0.0
    # write M = (1/pi^2)( (c34)/r^6 - s/r^6 ), r^2 = s + c34, s = x1^2+x2^2, c34 = x3^2+x4^2
    # M pi^2 = (c34 - s) / r^6
    s_lo = lo2[0][:, None] + lo2[1][None, :]
    s_hi = hi2[0][:, None] + hi2[1][None, :]
    m12 = masses[0][:, None] * masses[1][None, :]
    c_lo = lo2[2][:, None] + lo2[3][None, :]
    c_hi = hi2[2][:, None] + hi2[3][None, :]
    m34 = masses[2][:, None] * masses[3][None, :]
    s_lo_f, s_hi_f, m12_f = s_lo.ravel(), s_hi.ravel(), m12.ravel()
    c_lo_f, c_hi_f, m34_f = c_lo.ravel(), c_hi.ravel(), m34.ravel()
    for i in range(c_lo_f.size):
        cl, ch, m = c_lo_f[i], c_hi_f[i], m34_f[i]
        # f(s,c) = (c - s)/(s+c)^3. d/ds = -(1/(s+c)^3) - 3 (c-s)/(s+c)^4 = (2 s - 4 c)/(s+c)^4
        # d/dc = (s + ... ): d/dc = 1/(s+c)^3 - 3 (c-s)/(s+c)^4 = (4 s - 2 c)/(s+c)^4
        # bound by rational corners of numerator and denominator separately
        num_lo = cl - s_hi_f
        num_hi = ch - s_lo_f
        r_lo = (s_lo_f + cl) ** 3
        r_hi = (s_hi_f + ch) ** 3
        up = np.where(num_hi >= 0, num_hi / r_lo, num_hi / r_hi)
        dn = np.where(num_lo >= 0, num_lo / r_hi, num_lo / r_lo)
        hi_sum += m * (m12_f * up).sum()
        lo_sum += m * (m12_f * dn).sum()
    guard()
    return lo_sum / np.pi**2, hi_sum / np.pi**2


def sinc2(u):
    """s(u) = 2 sin(u/2)/u."""
    u = np.asarray(u, float)
    out = np.ones_like(u)
    m = np.abs(u) > 1e-9
    out[m] = 2 * np.sin(u[m] / 2) / u[m]
    return out


def fourier(z, Lp=120.0, np1=8001, ts=None):
    """P_infinity(z) by Schwinger parameter.

    (p1^2+p2^2)/|p|^2 |rho|^2 e^{-i p.z}, integrated with exp(-t p^2).
    One-dim factors: A_i(t) = int dp/(2 pi) w_i(p) exp(-t p^2) cos(p z_i),
    with w = s^4 on in-plane axes, s^2 on the others, and B_i the same with p^2.
    """
    p = np.linspace(-Lp, Lp, np1)
    dp = p[1] - p[0]
    s = sinc2(p)
    if ts is None:
        # log grid with Gauss-Legendre per decade
        x, w = np.polynomial.legendre.leggauss(12)
        decades = np.arange(-6, 7)
        ts = []
        wt = []
        for dk in decades:
            a, b = 10.0**dk, 10.0 ** (dk + 1)
            tt = 0.5 * (b - a) * x + 0.5 * (b + a)
            ts.append(tt)
            wt.append(0.5 * (b - a) * w)
        ts = np.concatenate(ts)
        wt = np.concatenate(wt)
    w_in = s**6  # in-plane: (rho has s(p_a)^2 after the extra factor); |rho|^2 has s^4 ... see below
    # rho_ab(p) = prod_nu s(p_nu) * s(p_a) s(p_b); |rho|^2 = s(p_a)^4 s(p_b)^4 s(p_c)^2 s(p_d)^2
    w_in = s**4
    w_out = s**2
    total = 0.0
    for t, wg in zip(ts, wt):
        e = np.exp(-t * p**2)
        A = []
        B = []
        for ax in range(4):
            wa = w_in if ax < 2 else w_out
            c = np.cos(p * z[ax])
            A.append((wa * e * c).sum() * dp / (2 * np.pi))
            B.append((wa * e * c * p**2).sum() * dp / (2 * np.pi))
        total += wg * (B[0] * A[1] + A[0] * B[1]) * A[2] * A[3]
    return float(total)


def main():
    offsets = [
        (3, 3, 2, 2),
        (3, 3, 2, 3),
        (3, 3, 2, 4),
        (3, 3, 2, 6),
        (3, 3, 4, 4),
        (4, 4, 2, 2),
        (3, 3, 6, 6),
    ]
    out = []
    for z in offsets:
        lo, hi = enclosure(z, n=(112, 112, 56, 56) if z in [(3, 3, 2, 2), (3, 3, 2, 4)] else (48, 48, 24, 24))
        fo = fourier(z)
        mx = (1 - 2 * (z[0] ** 2 + z[1] ** 2) / sum(a * a for a in z)) / (np.pi**2 * sum(a * a for a in z) ** 2)
        rec = dict(z=z, lo=lo, hi=hi, fourier=fo, maxwell=mx, inside=bool(lo <= fo <= hi), width_rel=abs(hi - lo) / abs(0.5 * (hi + lo)))
        out.append(rec)
        print(rec, flush=True)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "near_flux.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
