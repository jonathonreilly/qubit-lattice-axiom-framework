"""Independent numerical/symmetry checks for the C4/RW/W1 referee.

This deliberately does not load the worker's NPZ products.  It checks:
  * the E-channel centroid/full-flow Hessians by scrambled Sobol integration;
  * the nearest-neighbour bond O(lambda') coefficient by a direct momentum sum;
  * the dressing-space ranks for the full 48-element cubic group and for the
    24-element proper-rotation group actually supplied by the Lattice axiom;
  * the three fixed coefficients in the strained-normal-ordering completion.
"""

from __future__ import annotations

import argparse
import itertools
import numpy as np
from scipy.stats import qmc


def signed_permutation_group(proper_only: bool) -> list[np.ndarray]:
    group = []
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            r = np.zeros((3, 3), dtype=int)
            for i in range(3):
                r[i, p[i]] = signs[i]
            if not proper_only or round(np.linalg.det(r)) == 1:
                group.append(r)
    return group


def canon(points):
    points = sorted(tuple(int(x) for x in point) for point in points)
    origin = points[0]
    return tuple(sorted(tuple(x - y for x, y in zip(point, origin)) for point in points))


def act(r, monomial):
    return canon([tuple(r @ np.asarray(point)) for point in monomial])


def monomials(rng: int):
    ball = [p for p in itertools.product(range(-rng, rng + 1), repeat=3)
            if sum(map(abs, p)) <= rng]
    answer = set()
    for item in itertools.combinations_with_replacement(ball, 4):
        if all(sum(abs(a - b) for a, b in zip(p, q)) <= rng
               for p, q in itertools.combinations(item, 2)):
            answer.add(canon(item))
    return sorted(answer)


def orbit_partition(items, group):
    seen = set()
    answer = []
    for item in items:
        if item in seen:
            continue
        orbit = sorted(set(act(r, item) for r in group))
        seen.update(orbit)
        answer.append(orbit)
    return answer


def channel_rank(rng: int, channel: str, proper_only: bool) -> int:
    group = signed_permutation_group(proper_only)
    items = monomials(rng)
    item_index = {item: i for i, item in enumerate(items)}
    orbits = orbit_partition(items, group)
    hhat = (np.diag([1.0, -1.0, 0.0]) if channel == "E" else
            np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]]))
    seeds = []
    for i in range(3):
        for j in range(i, 3):
            tensor = np.zeros((3, 3))
            tensor[i, j] = tensor[j, i] = 1.0
            seeds.append(tensor)
    rows = []
    for orbit in orbits:
        representative = orbit[0]
        for seed in seeds:
            row = np.zeros(len(items))
            for r in group:
                coefficient = np.sum((r @ seed @ r.T) * hhat)
                if abs(coefficient) > 1e-12:
                    row[item_index[act(r, representative)]] += coefficient
            if np.max(np.abs(row)) > 1e-12:
                rows.append(row)
    return 0 if not rows else int(np.linalg.matrix_rank(np.asarray(rows), tol=1e-10))


def phi(k, strain):
    return 2.0 * np.arctan2(np.exp(strain) * np.sin(k / 2.0), np.cos(k / 2.0))


def jac(k, strain):
    return np.exp(strain) / (np.cos(k / 2.0) ** 2
                             + np.exp(2.0 * strain) * np.sin(k / 2.0) ** 2)


def weight(momentum, eps, mass=1.0):
    strains = (eps, -eps, 0.0)
    mapped = np.stack([phi(momentum[..., i], strains[i]) for i in range(3)], axis=-1)
    determinant = np.prod(np.stack([jac(momentum[..., i], strains[i])
                                    for i in range(3)], axis=-1), axis=-1)
    omega = np.sqrt(mass * mass + np.sum(4.0 * np.sin(mapped / 2.0) ** 2, axis=-1))
    return np.prod(determinant / (2.0 * omega), axis=-1) / np.sum(omega, axis=-1)


def centroid_integrands(kappa, eps):
    strains = (eps, -eps, 0.0)
    shifted = np.empty_like(kappa)
    vertex = np.ones(kappa.shape[0])
    for axis, strain in enumerate(strains):
        total = np.zeros(kappa.shape[0])
        for _ in range(9):
            points = kappa[..., axis] + total[:, None] / 4.0
            residual = np.sum(phi(points, strain), axis=1)
            residual = (residual + np.pi) % (2.0 * np.pi) - np.pi
            derivative = np.mean(jac(points, strain), axis=1)
            total -= residual / derivative
        points = kappa[..., axis] + total[:, None] / 4.0
        shifted[..., axis] = points
        vertex /= np.mean(jac(points, strain), axis=1)
    laboratory_weight = weight(kappa, eps)
    shifted_weight = weight(shifted, eps)
    return np.stack((laboratory_weight,
                     laboratory_weight * vertex * vertex,
                     shifted_weight * vertex), axis=1)


def richardson_hessian(values, step=0.04):
    second_large = (values[step] + values[-step] - 2.0 * values[0.0]) / step**2
    half = step / 2.0
    second_small = (values[half] + values[-half] - 2.0 * values[0.0]) / half**2
    return (4.0 * second_small - second_large) / 3.0


def sobol_centroid(repeats: int, power: int):
    step = 0.04
    epsilons = (-step, -step / 2.0, 0.0, step / 2.0, step)
    estimates = []
    for seed in range(repeats):
        points = qmc.Sobol(9, scramble=True, seed=4100 + seed).random_base2(power)
        first_three = (2.0 * points.reshape(-1, 3, 3) - 1.0) * np.pi
        fourth = -np.sum(first_three, axis=1, keepdims=True)
        kappa = np.concatenate((first_three, fourth), axis=1)
        values = {eps: np.mean(centroid_integrands(kappa, eps), axis=0)
                  for eps in epsilons}
        estimates.append(richardson_hessian(values, step))
    estimates = np.asarray(estimates)
    return np.mean(estimates, axis=0), np.std(estimates, axis=0, ddof=1) / np.sqrt(repeats)


def bond_first_order(size=64, mass=1.0):
    k = 2.0 * np.pi * np.fft.fftfreq(size)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    omega = np.sqrt(mass * mass + 4.0 * (np.sin(kx / 2.0) ** 2
                                        + np.sin(ky / 2.0) ** 2
                                        + np.sin(kz / 2.0) ** 2))
    jacobian_dot = np.cos(kx) - np.cos(ky)
    omega_dot = (np.sin(kx) ** 2 - np.sin(ky) ** 2) / omega
    propagator_dot = jacobian_dot / (2.0 * omega) - omega_dot / (2.0 * omega**2)
    position = np.fft.ifftn(propagator_dot).real
    derivatives = np.array((position[1, 0, 0], position[0, 1, 0], position[0, 0, 1]))
    return derivatives, float(derivatives @ derivatives)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sobol-power", type=int, default=16)
    parser.add_argument("--sobol-repeats", type=int, default=8)
    args = parser.parse_args()

    print("dressing coefficient-space ranks")
    for proper_only in (False, True):
        label = "proper-24" if proper_only else "full-48"
        for rng in (1, 2):
            print(label, "range", rng,
                  "E", channel_rank(rng, "E", proper_only),
                  "T2", channel_rank(rng, "T2", proper_only))

    derivatives, coefficient = bond_first_order()
    print("bond Gdot(ex,ey,ez)", derivatives)
    print("bond mu1/lambda_prime", coefficient)
    print("strained-normal-ordering Hessian coefficients", (1, -2, 1),
          "sum", sum((1, -2, 1)))

    means, errors = sobol_centroid(args.sobol_repeats, args.sobol_power)
    names = ("L2", "centroid-local", "full-flow")
    for name, mean, error in zip(names, means, errors):
        print(name, "H", mean, "+/-", error, "mu/lambda^2", -mean / 24.0)


if __name__ == "__main__":
    main()
