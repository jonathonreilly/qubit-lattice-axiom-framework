"""Independent spot checks for the lane-RG G1/G2 referee pass.

This deliberately does not call the supplied samplers or optimizers.  It checks
the closed-form binomial extremum, the on-shell equality witness, the claimed
fixed-window Green-function constants by nonsingular high-precision
quadrature, the static Lindhard sign, and the readout-Q arithmetic.  It also
evaluates the momentum-only witness used for the minimax-product rate on the
actual TB/KG energy shells.
"""

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 50


def f_binom(k, r):
    return ((1.0 + np.cos(k)) / 2.0) ** r


def eps_tb(k):
    return -2.0 * np.sum(np.cos(k), axis=-1)


def eps_kg(k, mass=1.0):
    return np.sqrt(mass * mass + np.sum(4.0 * np.sin(k / 2.0) ** 2, axis=-1))


print("BINOMIAL CLOSED FORM")
for r in (1, 2, 4, 8):
    # For winding +1 in one coordinate, s_in=s and s_out=s-2pi.
    # Log-concavity makes equal sharing optimal within each pair.
    ss = np.linspace(0.0, 2.0 * np.pi, 200_001)
    vals = (
        f_binom(ss / 2.0, r) ** 2
        * f_binom((ss - 2.0 * np.pi) / 2.0, r) ** 2
    )
    numeric = float(vals.max())
    exact = 16.0 ** (-r)
    print(f"r={r:2d} numeric={numeric:.16e} exact={exact:.16e} ratio={numeric/exact:.12f}")


print("\nON-SHELL EQUALITY WITNESS")
for name, eps in (("TB", eps_tb), ("KG(m=1)", eps_kg)):
    k1 = np.array([np.pi / 2.0, 0.0])
    k2 = np.array([np.pi / 2.0, 0.0])
    k3 = np.array([-np.pi / 2.0, 0.0])
    k4 = np.array([-np.pi / 2.0, 0.0])
    energy_residual = float(eps(k1) + eps(k2) - eps(k3) - eps(k4))
    winding = (k1 + k2 - k3 - k4) / (2.0 * np.pi)
    product_r1 = float(np.prod([f_binom(k[0], 1) for k in (k1, k2, k3, k4)]))
    print(
        f"{name}: dE={energy_residual:.3e} winding={winding.tolist()} "
        f"product(r=1)={product_r1:.16e}"
    )


def green_rate(kappa):
    """Independent nonsingular quadrature for E=[-1,0] U [a,1]."""
    a = mp.cos(kappa)
    den0 = lambda th: mp.sqrt(1.0 - a * a * mp.sin(th) ** 4)
    i0 = 2.0 * mp.quad(lambda th: 1.0 / den0(th), [0, mp.pi / 2])
    i1 = 2.0 * a * mp.quad(lambda th: mp.sin(th) ** 2 / den0(th), [0, mp.pi / 2])
    c = i1 / i0
    g = mp.quad(
        lambda th: 2.0
        * c ** 1.5
        * mp.cos(th) ** 3
        / mp.sqrt(
            (1.0 + c * mp.sin(th) ** 2)
            * (1.0 - c * mp.sin(th) ** 2)
            * (a - c * mp.sin(th) ** 2)
        ),
        [0, mp.pi / 2],
    )
    return float(g), float(c)


print("\nFIXED-WINDOW GREEN RATES")
for kappa in (np.pi / 6.0, np.pi / 4.0, np.pi / 3.0):
    g, c = green_rate(kappa)
    print(f"kappa/pi={kappa/np.pi:.6f} g1={g:.8f} critical_x={c:.8f}")


print("\nMINIMAX REPORT WITNESS IS NOT GENERICALLY ON SHELL")
for kappa in (np.pi / 6.0, np.pi / 4.0, np.pi / 3.0):
    k1 = np.array([kappa, 0.0])
    k2 = np.array([np.pi, 0.0])
    k3 = np.array([-(np.pi - kappa) / 2.0, 0.0])
    k4 = k3.copy()
    wind = (k1 + k2 - k3 - k4) / (2.0 * np.pi)
    dtb = float(eps_tb(k1) + eps_tb(k2) - eps_tb(k3) - eps_tb(k4))
    dkg = float(eps_kg(k1) + eps_kg(k2) - eps_kg(k3) - eps_kg(k4))
    print(
        f"kappa/pi={kappa/np.pi:.6f} winding={wind.tolist()} "
        f"TB_dE={dtb:.8f} KG_dE={dkg:.8f}"
    )


print("\nSTATIC LINDHARD SIGN CHECK")
grid_n = 160
grid = (np.arange(grid_n) + 0.5) * 2.0 * np.pi / grid_n - np.pi
kx, ky = np.meshgrid(grid, grid, indexing="ij")
ek = -2.0 * (np.cos(kx) + np.cos(ky))
mu, temp = -1.0, 0.02
fk = 1.0 / (1.0 + np.exp(np.clip((ek - mu) / temp, -700.0, 700.0)))
for qx, qy in ((0.1, 0.2), (0.7, -1.1), (np.pi, 0.0), (np.pi, np.pi)):
    ekq = -2.0 * (np.cos(kx + qx) + np.cos(ky + qy))
    fkq = 1.0 / (1.0 + np.exp(np.clip((ekq - mu) / temp, -700.0, 700.0)))
    de = ekq - ek
    ratio = np.empty_like(de)
    small = np.abs(de) < 1.0e-10
    ratio[small] = fk[small] * (1.0 - fk[small]) / temp
    ratio[~small] = (fk[~small] - fkq[~small]) / de[~small]
    print(
        f"q=({qx:.6f},{qy:.6f}) min_term={ratio.min():.3e} "
        f"chi0={ratio.mean():.9f} negative_terms={np.count_nonzero(ratio < -1e-13)}"
    )


print("\nREADOUT-Q ARITHMETIC FOR AMPLITUDE 1e-100")
target = 100.0 * math.log(10.0)
rates = {
    "binomial": 4.0 * math.log(2.0),
    "Chebyshev achieved": 3.100,
    "fixed kappa=pi/4 checked": 0.48,
    "fixed kappa=pi/4 asymptotic g1": green_rate(np.pi / 4.0)[0],
    "fixed kappa=pi/3 asymptotic g1": green_rate(np.pi / 3.0)[0],
}
for label, rate in rates.items():
    print(f"{label}: rate={rate:.9f} n={target/rate:.3f}")
