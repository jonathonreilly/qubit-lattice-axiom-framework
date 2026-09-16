"""Finite challenges for positive Wilson mixtures, not a gauge-phase computation.

The radial finite-volume heat equation checks the Hartman-Watson transform
through a different implementation from Bessel order formulas. Cube sums
challenge the partition tilt and dilution comparison on an actual incidence
matrix, using a finite two-point mixing law, not sampled Hartman-Watson tails.
"""
AUDIT_TIMEOUT_SEC = 180
from hashlib import sha256
from itertools import product, combinations
from pathlib import Path
import json
import math
import time

import mpmath as mp
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import ive, i0e


def radial_kernel(a, nu, resolution):
    # Symmetric finite-volume discretization of radial planar Brownian motion,
    # including the centrifugal killing nu^2/(2 r^2). Cell resolution is chosen
    # so the observation radius is exactly 1; no interpolation is used.
    h = 1.0 / (resolution + 0.5)
    size = math.ceil(8.0 / h)
    r = (np.arange(size) + 0.5) * h
    upper = np.arange(1, size + 1) * h
    lower = np.arange(size) * h
    diag = -(upper + lower) / (2 * h * h * r) - nu * nu / (2 * r * r)
    off = upper[:-1] / (2 * h * h * np.sqrt(r[:-1] * r[1:]))
    duration = 1.0 / a
    eigenvalues, vectors = eigh_tridiagonal(
        diag, off, select="v", select_range=(-100 / duration, 0),
        check_finite=False, lapack_driver="stebz")
    value = np.sum(np.exp(duration * eigenvalues) * vectors[resolution] ** 2)
    assert abs(r[resolution] - 1.0) < 2e-15
    return float(value), len(eigenvalues)


def heat_checks():
    rows = []
    for a in [1.0, 3.0, 12.0]:
        # The nu=1/2 radial solution is singular in derivative at r=0. The
        # preserved first attempt and diagnostic show first-order convergence
        # there; increase resolution without weakening its error criterion.
        for resolution in [64, 128, 256, 512, 1024]:
            base, _ = radial_kernel(a, 0.0, resolution)
            for nu in [0.5, 1.0, 2.0]:
                killed, modes = radial_kernel(a, nu, resolution)
                ratio = killed / base
                expected = float(ive(nu, a) / i0e(a))
                error = abs(ratio - expected)
                rows.append(dict(a=a, nu=nu, resolution=resolution,
                                 heat_ratio=ratio, bessel_ratio=expected,
                                 absolute_error=error, modes=modes))
                if resolution == 1024:
                    assert error < 8e-5, rows[-1]
    return rows


def cube_matrix():
    vertices = list(product(range(2), repeat=3))
    edges = [(x, j) for x in vertices for j in range(3) if x[j] == 0]
    index = {e: k for k, e in enumerate(edges)}
    faces = [(x, i, j) for x in vertices for i in range(3)
             for j in range(i + 1, 3) if x[i] == x[j] == 0]
    c = np.zeros((len(faces), len(edges)), dtype=int)
    for p, (x, i, j) in enumerate(faces):
        xi = tuple(x[k] + (k == i) for k in range(3))
        xj = tuple(x[k] + (k == j) for k in range(3))
        for e, sign in [((x, i), 1), ((xi, j), 1), ((xj, i), -1), ((x, j), -1)]:
            c[p, index[e]] = sign
    cycles = [np.array(z) for z in product([-1, 1], repeat=6)
              if np.all(c.T @ np.array(z) == 0)]
    assert c.shape == (6, 12) and np.linalg.matrix_rank(c) == 5
    assert len(cycles) == 2 and np.array_equal(cycles[0], -cycles[1])
    return c, cycles[0]


def cube_partition(variances, z, filling=None, deleted=None):
    k = np.arange(-80, 81, dtype=float)
    q = k[:, None] * z[None, :]
    if filling is not None:
        q = q + filling[None, :]
    allowed = np.ones(len(k), dtype=bool)
    if deleted is not None:
        allowed = np.all(q[:, deleted] == 0, axis=1)
    exponents = -0.5 * np.sum(variances[None, :] * q * q, axis=1)
    return float(np.exp(exponents[allowed]).sum())


def mixture_checks():
    c, z = cube_matrix()
    masks = np.array(list(product([False, True], repeat=6)))
    fillings = [np.eye(6, dtype=int)[0], np.eye(6, dtype=int)[0] + np.eye(6, dtype=int)[1]]
    assert all(np.any(c.T @ n) for n in fillings)
    rows = []
    for p in [0.01, 0.2, 0.5]:
        prior = p ** masks.sum(axis=1) * (1 - p) ** (6 - masks.sum(axis=1))
        variances = np.where(masks, 2.3, 0.08)
        partitions = np.array([cube_partition(t, z) for t in variances])
        posterior = prior * partitions / (prior @ partitions)
        inverted = prior / partitions
        inverted /= inverted.sum()
        assert abs(prior.sum() - 1) < 1e-14
        assert abs(posterior.sum() - 1) < 1e-14
        largest_ratio = 0.0
        for size in range(1, 7):
            for subset in combinations(range(6), size):
                event = masks[:, subset].all(axis=1)
                actual = float(posterior[event].sum())
                independent = p ** size
                largest_ratio = max(largest_ratio, actual / independent)
                assert actual <= independent + 2e-14
        # Deliberately invert the partition tilt: this must expose the direction
        # error rather than pass the domination bound by an accidental equality.
        inverse_bad = float(inverted[masks[:, 0]].sum())
        assert inverse_bad > p + 1e-5
        for filling in fillings:
            loop = np.array([cube_partition(t, z, filling) / partition
                             for t, partition in zip(variances, partitions)])
            diluted = np.array([
                cube_partition(np.full(6, 0.08), z, filling, mask)
                / cube_partition(np.full(6, 0.08), z, deleted=mask)
                for mask in masks])
            assert np.all(loop >= diluted - 2e-13)
            exact_mixture = float(posterior @ loop)
            unweighted_mixture = float(prior @ loop)
            diluted_lower = float(prior @ diluted)
            assert exact_mixture >= unweighted_mixture - 2e-13
            assert unweighted_mixture >= diluted_lower - 2e-13
            rows.append(dict(prior_bad_probability=p, filling=filling.tolist(),
                             largest_joint_bad_ratio=largest_ratio,
                             coupled_bad_probability=float(posterior[masks[:, 0]].sum()),
                             inverted_tilt_bad_probability=inverse_bad,
                             exact_mixture_loop=exact_mixture,
                             prior_average_loop=unweighted_mixture,
                             diluted_lower_bound=diluted_lower))
    return rows


def convolution_checks():
    size = 4096
    angle = 2 * np.pi * np.arange(size) / size
    frequency = np.fft.fftfreq(size, d=1 / size).astype(int)
    rows = []
    for variance in [0.2, 0.8, 2.0]:
        target = np.sqrt(2 * np.pi / variance) * sum(
            np.exp(-(angle - 2 * np.pi * k) ** 2 / (2 * variance)) for k in range(-6, 8))
        for steps in [4, 16, 64, 256]:
            beta = steps / variance
            density = np.exp(beta * (np.cos(angle) - 1)) / i0e(beta)
            coefficients = np.fft.fft(density) / size
            convolved = np.fft.ifft(coefficients ** steps).real * size
            analytic = (ive(abs(frequency), beta) / i0e(beta)) ** steps
            fft_error = float(np.max(abs(coefficients ** steps - analytic)))
            gaussian_error = float(np.max(abs(convolved - target)))
            assert fft_error < 2e-11
            n = np.arange(1, 81)
            ratio = ive(n, beta) / i0e(beta)
            envelope = np.exp(-n * n / (2 * (beta + n)))
            assert np.all(ratio <= envelope + 5e-14)
            rows.append(dict(variance=variance, steps=steps,
                             fft_bessel_error=fft_error,
                             uniform_villain_error=gaussian_error))
        assert rows[-1]["uniform_villain_error"] < 0.02
    return rows


def cusp_checks():
    mp.mp.dps = 100
    rows = []
    for a in map(mp.mpf, ["0.7", "3", "10"]):
        coefficient = mp.besselk(0, a) / mp.besseli(0, a)
        for power in [8, 16, 32, 48]:
            lam = mp.mpf(10) ** -power
            quotient = (1 - mp.besseli(mp.sqrt(lam), a) / mp.besseli(0, a)) / mp.sqrt(2 * lam)
            rel = abs(quotient / coefficient - 1)
            if power == 48:
                assert rel < mp.mpf("1e-14")
            rows.append(dict(a=str(a), lambda_power=-power,
                             sqrt_lambda_quotient=mp.nstr(quotient, 24),
                             exact_cusp_coefficient=mp.nstr(coefficient, 24),
                             relative_error=mp.nstr(rel, 12)))
    return rows


def main():
    start = time.monotonic()
    result = {"source_sha256": sha256(Path(__file__).read_bytes()).hexdigest()}
    # Each returned group includes all tested resolutions and controls.
    result["radial_heat"] = heat_checks()
    result["cube_mixture"] = mixture_checks()
    result["circle_convolution"] = convolution_checks()
    result["infinite_mean_cusp"] = cusp_checks()
    result["epsilon_bounds"] = {str(a): min(1.0, math.pi * math.exp(0.5) * math.sqrt(a) * math.exp(-a / 2)
                                          + 4 * math.exp(-((math.sqrt(3) - 1) / 2) ** 2 * a))
                                 for a in [10, 50, 100, 200, 400]}
    result["elapsed_seconds"] = time.monotonic() - start
    result["scope"] = "finite heat-kernel, character, and two-point-mixing challenges; no phase certification"
    result["status"] = "PASS"
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
