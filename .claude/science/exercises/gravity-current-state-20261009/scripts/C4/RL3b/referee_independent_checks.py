"""Independent numerical checks for the RL3b referee.

This deliberately does not import the worker's momentum quadrature.  It uses
Gauss--Legendre integration in s=tau**2, a separate polar grid in the lower
w half-plane, and only the shared operator coefficients/core definition.
"""

import numpy as np
from scipy.special import kv

from rl2_core_copy import OPS, fvals


def ih_direct(C, ns=600, ntheta=32, nr=601, rmax=5000.0):
    # Direct Gauss--Legendre rule in s, rather than the worker's logarithmic
    # trapezoid.  f is negligible well before s=24 for these six-layer rows.
    sx, sw = np.polynomial.legendre.leggauss(ns)
    s = 12.0 * (sx + 1.0)
    sw = 12.0 * sw
    sf = sw * s * fvals(C, s)

    tx, tw = np.polynomial.legendre.leggauss(ntheta)
    theta = 0.5 * np.pi * (tx + 1.0)
    tw = 0.5 * np.pi * tw

    logr = np.linspace(np.log(1.0e-3), np.log(rmax), nr)
    radius = np.exp(logr)
    dlogr = logr[1] - logr[0]
    total = 0.0
    angular_tail = 0.0

    for angle, weight in zip(theta, tw):
        w = radius * np.exp(-1j * angle)
        radial = np.empty(nr)
        for lo in range(0, nr, 50):
            hi = min(lo + 50, nr)
            y = np.sqrt(w[lo:hi, None] * s[None, :])
            ftilde = 2.0 * np.pi * ((kv(1, y) / y) @ sf)
            phi = ftilde / (1.0 - ftilde)
            radial[lo:hi] = radius[lo:hi] ** 3 * np.abs(phi) ** 2
        total += weight * np.sin(angle) * np.trapezoid(radial, dx=dlogr)
        # Phi(w) = 8*pi*f(0)/w**2 + O(|w|**-5/2) at large |w|.
        angular_tail += (
            weight * np.sin(angle) * (8.0 * np.pi * C[0]) ** 2 / rmax
        )

    return (total + angular_tail) / (16.0 * np.pi**4)


def translation(kh, source_extent=1.0e4):
    planck = 1.616255e-35
    distance = 1.0e9 * 3.0856776e16
    ell = 1.0e-19
    tau = np.sqrt(2.0 * distance * source_extent + source_extent**2)
    nsd = kh * planck**2 * tau / (2.0 * ell**3)
    ell_needed = (kh * planck**2 * tau / 2.0) ** (1.0 / 3.0)
    kcrit = 2.0 * ell**3 / (planck**2 * tau)
    return tau, nsd, ell_needed, kcrit


if __name__ == "__main__":
    reported = np.array([0.595189, 0.639705, 0.842548])
    independent = np.array([ih_direct(C) for C in OPS])
    print("I_h independent:", " ".join(f"{x:.9f}" for x in independent))
    print("I_h minus report:", " ".join(f"{x:+.3e}" for x in independent - reported))
    kh = np.sqrt(4.0 * np.pi * independent)
    print("k_h independent:", " ".join(f"{x:.6f}" for x in kh))
    for i, k in enumerate(kh):
        tau, nsd, ell_needed, kcrit = translation(k)
        print(
            f"op{i}: tau={tau:.6e} nsd={nsd:.3f} "
            f"ell_needed={ell_needed:.6e} kcrit={kcrit:.8f}"
        )
