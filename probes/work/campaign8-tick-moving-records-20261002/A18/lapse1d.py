#!/usr/bin/env python3
"""A18 lapse1d: 1D A10 brickwork of partial swaps, one excitation, with the candidate package's paces
(supplied toy, nothing adopted).
  * one shared beat; cycle = [mass half] [even bonds, theta/2] [odd bonds] [even bonds, theta/2] [mass half] (time-symmetric, A10 S9)
  * bond (j, j+1) gate on the one-excitation block, vacuum-relative offset removed:  exp(-i theta_b sigma_x)
        theta_b = theta0 * w_b,  w_b = N_j N_{j+1}  (AND/product, P2)  or  (N_j + N_{j+1})/2  (OR)
  * one-site staggered phase mass (P3): phase exp(-i (mu/2) N_j (-1)^j) before and after the bonds
  * two-site mass (A10 B-type, for contrast): theta0e != theta0o, both scaled by w_b
Cells c hold sites (2c, 2c+1); cone at cell momentum K* = pi.
Parts: b = Bloch facts; m = massless delay through a smooth lapse bump (AND vs OR, two doses);
       s = reflection at smooth vs sharp lapse changes (massless and massive); f = free fall in a lapse gradient.
"""
import os, sys, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np

PARTS = sys.argv[1] if len(sys.argv) > 1 else "bmsf"


def bloch(K, the, tho, mN):
    """cycle matrix U(K) on (A,B) of a cell for uniform angles and mass phase mN = mu*N"""
    ce, se, co, so = np.cos(the / 2), np.sin(the / 2), np.cos(tho), np.sin(tho)
    Eh = np.array([[ce, -1j * se], [-1j * se, ce]])          # even bonds, half angle
    O = np.array([[co, -1j * so * np.exp(-1j * K)], [-1j * so * np.exp(1j * K), co]])
    Mh = np.diag([np.exp(-0.5j * mN), np.exp(0.5j * mN)])
    return Mh @ Eh @ O @ Eh @ Mh                               # time-symmetric block (A10 S9)


def bands(K, the, tho, mN):
    w, v = np.linalg.eig(bloch(K, the, tho, mN))
    om = -np.angle(w)
    i = np.argmax(om)                     # upper band (omega > 0)
    vec = v[:, i] * np.exp(-1j * np.angle(v[0, i]))   # gauge: A component real positive
    return om[i], vec / np.linalg.norm(vec)


def packet(Nc, c0, K0, sig, the, tho, mN):
    Ks = 2 * np.pi * np.arange(Nc) / Nc
    dK = np.angle(np.exp(1j * (Ks - K0)))
    g = np.exp(-0.5 * (dK * sig) ** 2) * np.exp(-1j * Ks * c0)
    keep = np.abs(g) > 1e-12
    A = np.zeros(Nc, complex); B = np.zeros(Nc, complex)
    cs = np.arange(Nc)
    for K, gk in zip(Ks[keep], g[keep]):
        _, vec = bands(K, the, tho, mN)
        ph = np.exp(1j * K * cs)
        A += gk * vec[0] * ph; B += gk * vec[1] * ph
    psi = np.empty(2 * Nc, complex); psi[0::2] = A; psi[1::2] = B
    return psi / np.linalg.norm(psi)


def angles(Nsite, theta0e, theta0o, rule):
    Nn = np.roll(Nsite, -1)
    w = Nsite * Nn if rule == "AND" else 0.5 * (Nsite + Nn)
    thE = theta0e * w[0::2]          # bond (2c, 2c+1)
    thO = theta0o * w[1::2]          # bond (2c+1, 2c+2)
    return thE, thO


def make_stepper(Nsite, theta0e, theta0o, mu, rule):
    thE, thO = angles(Nsite, theta0e, theta0o, rule)
    cE, sE, cO, sO = np.cos(thE / 2), np.sin(thE / 2), np.cos(thO), np.sin(thO)
    eps = np.where(np.arange(Nsite.size) % 2 == 0, 1.0, -1.0)
    mh = np.exp(-0.5j * mu * Nsite * eps)

    def step(psi):                     # mass half, even half-angle, odd, even half-angle, mass half
        psi = psi * mh
        a, b = psi[0::2], psi[1::2]
        a, b = cE * a - 1j * sE * b, -1j * sE * a + cE * b
        a2 = np.roll(a, -1)
        b, a2 = cO * b - 1j * sO * a2, -1j * sO * b + cO * a2
        a = np.roll(a2, 1)
        a, b = cE * a - 1j * sE * b, -1j * sE * a + cE * b
        out = np.empty_like(psi); out[0::2] = a; out[1::2] = b
        return out * mh
    return step


def cellprob(psi):
    p = np.abs(psi) ** 2
    return p[0::2] + p[1::2]


def arrival(Nsite, theta0, rule, q0, c0, cd, sig, Tmax, Nc):
    step = make_stepper(Nsite, theta0, theta0, 0.0, rule)
    psi = packet(Nc, c0, np.pi + q0, sig, theta0, theta0, 0.0)
    prev = 0.0
    for t in range(1, Tmax + 1):
        psi = step(psi)
        if t % 4 == 0:
            f = cellprob(psi)[cd:].sum()
            if f >= 0.5 > prev:
                return t - 4 + 4 * (0.5 - prev) / (f - prev), psi
            prev = f
    return np.nan, psi


def eik_delay(Ncell_profile, theta0, rule, q0):
    """exact-dispersion eikonal delay: omega conserved, local K, local group velocity (cells/cycle)"""
    om0, _ = bands(np.pi + q0, theta0, theta0, 0.0)
    Ns = np.repeat(Ncell_profile, 2)
    thE, thO = angles(Ns, theta0, theta0, rule)
    cosK = (np.cos(thE) * np.cos(thO) - np.cos(om0)) / (np.sin(thE) * np.sin(thO))
    K = 2 * np.pi - np.arccos(np.clip(cosK, -1, 1))          # K in (pi, 2pi): right mover branch
    v = -np.sin(thE) * np.sin(thO) * np.sin(K) / np.sin(om0)
    vinf = -np.sin(theta0) ** 2 * np.sin(np.pi + q0) / np.sin(om0)
    return np.sum(1 / v - 1 / vinf)


if "b" in PARTS:
    print("(b) Bloch facts at the cone K* = pi")
    for mu in (0.05, 0.2):
        for N in (1.0, 0.9, 0.8):
            om, _ = bands(np.pi, 0.3 * N * N, 0.3 * N * N, mu * N)
            print("   one-site mass mu=%.2f, N=%.2f: rest quasi-energy %.10f, /(mu N) = %.12f" % (mu, N, om, om / (mu * N)))
    for N in (1.0, 0.9, 0.8):
        om, _ = bands(np.pi, 0.275 * N * N, 0.325 * N * N, 0.0)
        print("   two-site mass (0.275/0.325), N=%.2f: rest quasi-energy %.10f, /(0.05 N^2) = %.12f" % (N, om, om / (0.05 * N * N)))
    for mu in (0.05, 0.2):
        Ks = np.pi + np.linspace(-0.3, 0.3, 6001)
        oms = np.array([bands(K, 0.3, 0.3, mu)[0] for K in Ks])
        i = np.argmin(oms)
        print("   one-site mass mu=%.2f, theta=0.3: upper-band minimum at K - pi = %+.5f, omega_min = %.8f" % (mu, Ks[i] - np.pi, oms[i]))
    for th0 in (0.01, 0.2, 0.6, np.pi / 4, np.pi / 2):
        dU = 1e-6
        v = lambda U: np.sin(th0 * np.exp(-2 * U))       # cone speed, cells/cycle, AND with N = e^{-U}
        gam = (np.log(v(0)) - np.log(v(dU))) / dU - 1    # n - 1 = (1 + gamma) U
        print("   theta0=%.4f: cone speed sin(theta0 N^2); light gamma_eff = %.6f ; 2 th cot th - 1 = %.6f"
              % (th0, gam, 2 * th0 / np.tan(th0) - 1))

if "m" in PARTS:
    print("(m) massless delay through a smooth lapse bump N = exp(-U), U = 0.1 exp(-((c-1500)/80)^2)")
    Nc, c0, cd, sig, q0 = 3000, 500, 2300, 50.0, 0.12
    cells = np.arange(Nc)
    U = 0.1 * np.exp(-((cells - 1500) / 80.0) ** 2)
    Ncell = np.exp(-U)
    Nsite = np.repeat(Ncell, 2)
    for theta0 in (0.2, 0.6):
        res = {}
        for rule in ("AND", "OR"):
            Tmax = int(2 * (cd - c0) / np.sin(theta0)) + 400
            t1, psi1 = arrival(Nsite, theta0, rule, q0, c0, cd, sig, Tmax, Nc)
            t0, _ = arrival(np.ones(2 * Nc), theta0, rule, q0, c0, cd, sig, Tmax, Nc)
            p = cellprob(psi1)
            refl = p[:1300].sum()
            pred = eik_delay(Ncell, theta0, rule, q0)
            vinf = np.sin(theta0)                               # cone speed (cells/cycle)
            small = np.sum((Ncell ** (-2 if rule == "AND" else -1)) - 1) / vinf
            res[rule] = t1 - t0
            print("   theta0=%.1f %-3s: delay %.2f cycles; exact-dispersion eikonal %.2f; small-dose (n=N^-%d) %.2f; "
                  "measured/small-dose %.4f; reflected weight %.1e; norm %.12f"
                  % (theta0, rule, t1 - t0, pred, 2 if rule == "AND" else 1, small, (t1 - t0) / small, refl, np.sum(p)))
        print("   theta0=%.1f: delay ratio AND/OR = %.4f ; theta0 cot theta0 = %.4f" %
              (theta0, res["AND"] / res["OR"], theta0 / np.tan(theta0)))

if "s" in PARTS:
    print("(s) reflection at lapse changes (AND rule): smooth Gaussian bump/dip vs sharp step")
    Nc, c0, sig = 2400, 500, 50.0
    cells = np.arange(Nc)
    for label, mu, q0, Ustep in (("massless", 0.0, 0.12, 0.1), ("massive mu=0.05", 0.05, 0.15, 0.05)):
        theta0 = 0.3
        for shape in ("smooth", "ramp20", "sharp"):
            if shape == "smooth":
                U = Ustep * np.exp(-((cells - 1200) / 60.0) ** 2)
            elif shape == "ramp20":
                U = Ustep * np.clip((cells - 1190) / 20.0, 0, 1)
            else:
                U = Ustep * (cells >= 1200)
            Nsite = np.repeat(np.exp(-U), 2)
            step = make_stepper(Nsite, theta0, theta0, mu, "AND")
            psi = packet(Nc, c0, np.pi + q0, sig, theta0, theta0, mu)
            om0, _ = bands(np.pi + q0, theta0, theta0, mu)
            vg = (bands(np.pi + q0 + 1e-5, theta0, theta0, mu)[0] - bands(np.pi + q0 - 1e-5, theta0, theta0, mu)[0]) / 2e-5
            T = int(1100 / vg)
            for t in range(T):
                psi = step(psi)
            p = cellprob(psi)
            print("   %-16s %-7s: transmitted (c>1260) %.8f  reflected (c<1100) %.2e  (group vel %.4f, %d cycles)"
                  % (label, shape, p[1260:].sum(), p[:1100].sum(), vg, T))

if "f" in PARTS:
    print("(f) free fall from rest in a linear lapse gradient N = 1 - g (c - c0), g = 1e-4 per cell (AND rule)")
    Nc, c0, g, T = 2000, 1000, 1e-4, 1500
    sig = float(os.environ.get("A18_SIG", "40"))
    print("   packet width sigma = %.0f cells" % sig)
    cells = np.arange(Nc)
    Nsite = np.repeat(1 - g * (cells - c0), 2)
    theta0 = 0.3
    clight2 = np.sin(theta0) ** 2                     # massless cone speed^2 at N = 1 (cells/cycle)^2
    a_metric = clight2 * g                            # geodesic of -N^2 dt^2 + N^-2 dx^2: a = -c^2 N^3 dN/dx
    for label, the0, tho0, mu in (("one-site mass mu=0.05", theta0, theta0, 0.05),
                                  ("one-site mass mu=0.02", theta0, theta0, 0.02),
                                  ("two-site mass 0.275/0.325", 0.275, 0.325, 0.0)):
        step = make_stepper(Nsite, the0, tho0, mu, "AND")
        psi = packet(Nc, c0, np.pi, sig, the0, tho0, mu)
        ts, xs = [], []
        for t in range(T + 1):
            if t % 10 == 0:
                p = cellprob(psi); ts.append(t); xs.append(np.sum(cells * p))
            psi = step(psi)
        coef = np.polyfit(np.array(ts, float), np.array(xs), 2)
        a_meas = 2 * coef[0]
        # semiclassical prediction from the exact uniform-medium dispersion: a = -(d omega/dN)(dN/dc)(d2 omega/dK2)
        dN, dK = 1e-5, 1e-3
        om = lambda K, N: bands(K, the0 * N * N, tho0 * N * N, mu * N)[0]
        domdN = (om(np.pi, 1 + dN) - om(np.pi, 1 - dN)) / (2 * dN)
        d2 = (om(np.pi + dK, 1) - 2 * om(np.pi, 1) + om(np.pi - dK, 1)) / dK ** 2
        a_sc = domdN * g * d2
        print("   %-26s a_meas = %.4e  semiclassical %.4e  (ratio %.4f);  a_meas / a_metric(light) = %.4f"
              % (label, a_meas, a_sc, a_meas / a_sc, a_meas / a_metric))
