#!/usr/bin/env python3
"""Exact center-flip geometry and finite checks of its posterior comparison.

No posterior integral is numerically evaluated. The probability comparison
uses Haar invariance and the analytic full-posterior disintegration in the
manuscript. A failure of a filled-volume estimate is not an RG counterexample.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import sys
sys.dont_write_bytecode = True
import itertools
import math
from collections import defaultdict
import numpy as np
from push_a_posterior_geometry import PATHS, L, guard


def move(x, direction, amount=1):
    y = list(x)
    y[direction] += amount
    return tuple(y)


def plaquette_edges(p):
    x, mu, nu = p
    return ((x, mu, 1), (move(x, mu), nu, 1),
            (move(x, nu), mu, -1), (x, nu, -1))


def flip_boundary(edges):
    boundary = set()
    for x, direction in edges:
        for other in range(4):
            if other == direction:
                continue
            mu, nu = sorted((direction, other))
            for base in (x, move(x, other, -1)):
                p = (base, mu, nu)
                if p in boundary:
                    boundary.remove(p)
                else:
                    boundary.add(p)
    return boundary


STENCIL = defaultdict(set)
for mu, paths in enumerate(PATHS):
    for path in paths:
        for p, nu, _ in path:
            residue = tuple(x % L for x in p)
            shift = tuple((p[a] - residue[a]) // L for a in range(4))
            STENCIL[(residue, nu)].add((shift, mu))


def advance(edges):
    result = set()
    for x, nu in edges:
        residue = tuple(a % L for a in x)
        cell = tuple((x[a] - residue[a]) // L for a in range(4))
        for shift, mu in STENCIL[(residue, nu)]:
            result.add((tuple(cell[a] - shift[a] for a in range(4)), mu))
    return result


def geometry_check():
    print("Exact center-sheet and actual-contour reader counts:")
    for j in (1, 2, 3):
        radius = L**j
        sheet = {((0,) + y, 0) for y in itertools.product(range(radius), repeat=3)}
        boundary = flip_boundary(sheet)
        assert len(sheet) == radius**3 and len(boundary) == 6 * radius**2
        readers = {(x, mu) for p in boundary for x, mu, _ in plaquette_edges(p)}
        assert len(readers) <= 4 * len(boundary)
        projected = {tuple((v + (L**(j+1)-1)//2) // L**(j+1) for v in x)
                     for x, _ in sheet | readers}
        assert projected == {(0, 0, 0, 0)}
        cone_s, cone_b = sheet, readers
        for _ in range(j + 1):
            cone_s, cone_b = advance(cone_s), advance(cone_b)
            guard()
        assert len(cone_s) <= 2500 and len(cone_b) <= 2500
        print(f"j={j}, R={radius}: changed links={len(sheet)}, "
              f"changed plaquettes={len(boundary)}, boundary readers={len(readers)}, "
              f"terminal cone sizes=({len(cone_s)},{len(cone_b)}), "
              f"Wilson action at twisted identity={2*len(boundary)}.")
    guard()


def matrix_check():
    identity = np.eye(2, dtype=complex)
    sigma = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]],
                      [[1, 0], [0, -1]]], dtype=complex)
    rng = np.random.default_rng(20261030)
    sheet = {((0,) + y, 0) for y in itertools.product(range(3), repeat=3)}
    boundary = flip_boundary(sheet)
    incident = {(base, *sorted((0, other)))
                for x, _ in sheet for other in (1, 2, 3)
                for base in (x, move(x, other, -1))}
    fields = {}
    for p in sorted(incident):
        for x, mu, _ in plaquette_edges(p):
            if (x, mu) not in fields:
                q = rng.normal(size=4)
                q /= np.linalg.norm(q)
                fields[(x, mu)] = q[0]*identity + 1j*np.einsum("a,aij->ij", q[1:], sigma)
    max_error = 0.0
    action_change = 0.0
    for p in sorted(incident):
        original, changed = identity.copy(), identity.copy()
        for x, mu, sign in plaquette_edges(p):
            u = fields[(x, mu)]
            v = -u if (x, mu) in sheet else u
            original = original @ (u if sign == 1 else u.conj().T)
            changed = changed @ (v if sign == 1 else v.conj().T)
        expected = -original if p in boundary else original
        max_error = max(max_error, float(np.max(np.abs(changed - expected))))
        f_original = 1 - np.trace(original).real/2
        f_changed = 1 - np.trace(changed).real/2
        action_change += f_changed - f_original
        assert abs(f_changed - ((2-f_original) if p in boundary else f_original)) < 1e-12
    assert max_error < 1e-12 and abs(action_change) <= 2*len(boundary) + 1e-12
    print(f"Random SU(2) matrix check on all {len(incident)} incident plaquettes: "
          f"maximum center-multiplication error={max_error:.6g}; "
          f"action change={action_change:.12g}; bound={2*len(boundary)}.")
    guard()


def gauge_repair_check():
    # The original field U_1=-I, U_2=U_3=U_4=I is a periodic pure gauge
    # on even tori. Resetting internal links to I flips the following set.
    for side in (2, 3, 5):
        inside = {((a,) + y, 0) for a in range(side-1)
                  for y in itertools.product(range(side), repeat=3)}
        boundary = flip_boundary(inside)
        assert len(boundary) == 6*(side-1)*side**2
        print(f"Pure-gauge identity-reset check: side={side}, original action=0, "
              f"repaired action={2*len(boundary)}.")
    guard()


def exponent_check():
    # Inspect only the explicit lower-bound exponent, not a probability.
    u, kappa, epsilon, filling_rate = 100.0, 1.0, 0.5, 0.1
    c_haar = 8/(3*math.pi**3)
    ball_radius = math.sqrt(epsilon/8)
    log_inv_mass = -math.log(c_haar*ball_radius**3)
    surface_constant = 300*u + 24*log_inv_mass
    terminal_constant = 10000*kappa*u
    print(f"Analytic exponent inputs: u_0=u_j={u}, kappa={kappa}, "
          f"epsilon={epsilon}, filling rate a={filling_rate}.")
    print("Filled-volume factor times the analytic probability lower bound:")
    for j in (9, 11, 13):
        radius = L**j
        exponent = filling_rate*radius**3 - surface_constant*radius**2 - terminal_constant
        if j == 13:
            assert exponent > 0
        print(f"R=3^{j}; log bound for exp(a R^3) pi(E_rough) >= {exponent:.12g}.")
    print("The all-R divergence is analytic; these values are not posterior measurements.")


if __name__ == "__main__":
    geometry_check()
    matrix_check()
    gauge_repair_check()
    exponent_check()
    print(f"Peak RSS bytes: {guard()} (<1000000000); BLAS threads=1.")
    print("No lower bound on the connected covariance or extracted RG remainder is claimed.")
    print("U1--U4 count remains four.")
