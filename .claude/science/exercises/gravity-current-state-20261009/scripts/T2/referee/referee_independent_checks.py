#!/usr/bin/env python3
"""Independent controls for the T2 referee report.

These checks deliberately avoid the perfect-action Schwinger/Hankel code under
review.  They test (i) the pole-mixture moment inequality and (ii) the temporal
box-blocking obstruction to an unshifted Hausdorff moment sequence.
"""

import numpy as np


def pole_moment_control(samples=100_000, seed=20261009):
    """Return the smallest E[r]E[r^-2]/E[r^-1] in a random mixture scan."""
    rng = np.random.default_rng(seed)
    minimum = np.inf
    for _ in range(samples):
        count = rng.integers(2, 9)
        weights = rng.dirichlet(np.ones(count))
        ranges = 10.0 ** rng.uniform(-6.0, 6.0, count)
        ratio = (
            np.dot(weights, ranges)
            * np.dot(weights, ranges ** -2)
            / np.dot(weights, ranges ** -1)
        )
        minimum = min(minimum, ratio)
    return minimum


def sinc2(x):
    """(sin(x/2)/(x/2))^2, matching the block-window convention."""
    return np.sinc(x / (2.0 * np.pi)) ** 2


def blocked_alias_mass_cutoff(k=(0.41, 0.73, 1.07), mass=0.3, cut=8):
    """Necessary zero-moment mass for aliases along one spatial direction.

    For one continuum energy E, unit-time box blocking gives
      G_n = A(E) exp(-n E), n >= 1,
      A(E) = (cosh(E)-1)/E^3.
    A positive unshifted Hausdorff representation must therefore contain mass
    A(E) at lambda=exp(-E).  The spatial sinc weights fall only polynomially,
    so this necessary mass diverges as the alias cutoff grows.
    """
    k = np.asarray(k, float)
    fixed_weight = sinc2(k[1]) * sinc2(k[2])
    required = 0.0
    actual_g0 = 0.0
    for ell in range(-cut, cut + 1):
        p0 = k[0] + 2.0 * np.pi * ell
        weight = fixed_weight * sinc2(p0)
        energy = np.sqrt(mass * mass + p0 * p0 + k[1] ** 2 + k[2] ** 2)
        required += weight * (np.cosh(energy) - 1.0) / energy ** 3
        actual_g0 += weight * (energy - 1.0 + np.exp(-energy)) / energy ** 3
    return required, actual_g0


if __name__ == "__main__":
    print("pole-mixture minimum ratio:", f"{pole_moment_control():.12f}")
    print("alias cutoff | required unshifted mass | actual same-cell G0")
    for cutoff in range(1, 9):
        required, actual = blocked_alias_mass_cutoff(cut=cutoff)
        print(f"{cutoff:12d}   {required: .8e}   {actual: .8e}")
