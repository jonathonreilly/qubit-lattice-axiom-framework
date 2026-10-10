"""Independent L=8 classical phi^4 autocorrelation audit.

This repeats the worker's Hamiltonian and velocity-Verlet evolution, but keeps
each trajectory's numerator and denominator separately.  The ensemble
autocorrelation is the ratio of ensemble sums, not the mean of the
single-trajectory ratios used for the reported error bars.
"""

import numpy as np


L = 8
M2 = 0.5
TEMP = 1.0
DT = 0.02
NTRAJ = 24
TEQ = 40.0
TMAX = 150.0
TAIL_START = 75.0


def force(phi, lam):
    lap = sum(np.roll(phi, 1, axis) + np.roll(phi, -1, axis) - 2 * phi
              for axis in range(3))
    return lap - M2 * phi - lam * phi**3


def current(phi, pi):
    return np.array([
        -0.5 * np.sum((np.roll(phi, -1, axis) - phi)
                      * (pi + np.roll(pi, -1, axis)))
        for axis in range(3)
    ])


def energy(phi, pi, lam):
    gradient = sum(0.5 * (np.roll(phi, -1, axis) - phi)**2
                   for axis in range(3))
    return np.sum(0.5 * pi**2 + 0.5 * M2 * phi**2
                  + 0.25 * lam * phi**4 + gradient)


def one_trajectory(rng, lam):
    k = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    omega2 = M2 + 4 * (np.sin(kx / 2)**2 + np.sin(ky / 2)**2
                       + np.sin(kz / 2)**2)
    phi_k = np.fft.fftn(rng.normal(size=(L, L, L))) * np.sqrt(TEMP / omega2)
    phi = np.fft.ifftn(phi_k).real
    pi = rng.normal(size=(L, L, L)) * np.sqrt(TEMP)
    accel = force(phi, lam)

    for _ in range(round(TEQ / DT)):
        pi += 0.5 * DT * accel
        phi += DT * pi
        accel = force(phi, lam)
        pi += 0.5 * DT * accel

    e0 = energy(phi, pi, lam)
    j0 = current(phi, pi)
    denom = float(j0 @ j0)
    numerators = []
    max_drift = 0.0
    tail_index = round(TAIL_START / DT)
    for step in range(round(TMAX / DT)):
        if step >= tail_index:
            numerators.append(float(current(phi, pi) @ j0))
        pi += 0.5 * DT * accel
        phi += DT * pi
        accel = force(phi, lam)
        pi += 0.5 * DT * accel
    max_drift = abs(energy(phi, pi, lam) - e0) / abs(e0)
    return float(np.mean(numerators)), denom, max_drift


def jackknife_ratio(numerators, denominators):
    total_a = np.sum(numerators)
    total_b = np.sum(denominators)
    estimates = (total_a - numerators) / (total_b - denominators)
    mean = np.mean(estimates)
    error = np.sqrt((len(estimates) - 1) * np.mean((estimates - mean)**2))
    return total_a / total_b, error


for lam in (0.0, 0.5, 2.0, 4.0):
    generator = np.random.default_rng(20261010 + round(10 * lam))
    rows = [one_trajectory(generator, lam) for _ in range(NTRAJ)]
    nums = np.array([row[0] for row in rows])
    dens = np.array([row[1] for row in rows])
    pooled, pooled_se = jackknife_ratio(nums, dens)
    mean_of_ratios = np.mean(nums / dens)
    mor_se = np.std(nums / dens, ddof=1) / np.sqrt(NTRAJ)
    print(
        f"lambda={lam:.1f}: pooled tail C={pooled:+.4f} +/- {pooled_se:.4f}; "
        f"mean-of-ratios={mean_of_ratios:+.4f} +/- {mor_se:.4f}; "
        f"max drift={max(row[2] for row in rows):.2e}; "
        f"J0^2 range=[{dens.min():.3g},{dens.max():.3g}]"
    )

# Use the worker's seed and lambda ordering so the second and fourth rows use
# exactly the same initial-condition stream as l3_phi4_stats.py.
print("worker-seed replay with the correct pooled estimator:")
generator = np.random.default_rng(1)
for lam in (0.0, 2.0, 4.0):
    rows = [one_trajectory(generator, lam) for _ in range(NTRAJ)]
    nums = np.array([row[0] for row in rows])
    dens = np.array([row[1] for row in rows])
    pooled, pooled_se = jackknife_ratio(nums, dens)
    mean_of_ratios = np.mean(nums / dens)
    mor_se = np.std(nums / dens, ddof=1) / np.sqrt(NTRAJ)
    print(
        f"lambda={lam:.1f}: pooled tail C={pooled:+.4f} +/- {pooled_se:.4f}; "
        f"mean-of-ratios={mean_of_ratios:+.4f} +/- {mor_se:.4f}"
    )
