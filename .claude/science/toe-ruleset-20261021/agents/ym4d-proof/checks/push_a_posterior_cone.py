#!/usr/bin/env python3
"""Finite checks for a full-posterior conditional-excitation comparison.

The cone is computed from the actual paired contours. One-link quadratures
check the original conditional law, not the full posterior. No RG return,
posterior covariance decay or invariant reserve is numerically certified.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import sys
sys.dont_write_bytecode = True
import math
from collections import defaultdict
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from push_a_posterior_geometry import PATHS, L, guard, log_z


def cone_check():
    stencil = defaultdict(set)
    for mu, paths in enumerate(PATHS):
        for path in paths:
            for base, nu, _ in path:
                residue = tuple(x % L for x in base)
                cell = tuple((base[a] - residue[a]) // L for a in range(4))
                stencil[(residue, nu)].add((cell, mu))

    def advance(edges):
        result = set()
        for x, nu in edges:
            residue = tuple(a % L for a in x)
            cell = tuple((x[a] - residue[a]) // L for a in range(4))
            for shift, mu in stencil[(residue, nu)]:
                result.add((tuple(cell[a] - shift[a] for a in range(4)), mu))
        return result

    origin = (0,) * 4
    star = {(origin, mu) for mu in range(4)}
    star.update((tuple(-1 if a == mu else 0 for a in range(4)), mu)
                for mu in range(4))
    first = advance({(origin, 0)})
    assert first == star and advance(star) == star
    print(f"Exact integer reader sets: one root link -> {len(first)} links; "
          "the eight-link star maps to itself.")
    print("This proves the stencil closure by induction, not persistence of rough fields.")
    guard()


def kernel_check():
    count = 0
    for t in (0.1, 1.0, 10.0, 100.0):
        lower, upper = -t - log_z(t), t - log_z(t)
        for radius in (0.0, 0.1, 0.5, 1.0):
            s = t * radius
            normalizer = log_z(s) if s else 0.0
            for angle in (0.0, 0.3, math.pi / 2, math.pi):
                value = s * math.cos(angle) - normalizer
                assert lower - 1e-12 <= value <= upper + 1e-12
                count += 1
    print(f"Kernel endpoint-range finite checks: {count}; ratio bound exp(2t).")
    guard()


def excitation_check():
    # Actual six positive staples, or four positive and two negative:
    # H_D=6-radius*cos(theta), with minimum 6-radius.
    c_haar = 8 / (3 * math.pi**3)
    largest_log_ratio = -math.inf
    count = 0
    for radius in (2.0, 6.0):
        for u in (20.0, 100.0, 1000.0):
            denominator = quad(lambda a: math.exp(-u * radius * (1 - math.cos(a)))
                               * math.sin(a)**2, 0, math.pi,
                               epsabs=2e-14, epsrel=2e-12)[0]
            for threshold in (0.25, 0.5, 1.0):
                cutoff = math.acos(1 - threshold / radius)
                for reserve in (0.0, 0.25, 0.75):
                    gamma = 1 - reserve
                    tail = quad(lambda a: math.exp(-gamma * u *
                                (radius * (1 - math.cos(a)) - threshold))
                                * math.sin(a)**2, cutoff, math.pi,
                                epsabs=2e-14, epsrel=2e-12)[0]
                    log_actual = (-gamma * u * threshold
                                  + math.log(tail) - math.log(denominator))
                    delta = gamma * threshold / 12
                    log_bound = -math.log(c_haar * delta**3) - gamma * u * threshold / 2
                    largest_log_ratio = max(largest_log_ratio, log_actual - log_bound)
                    assert log_actual <= log_bound + 1e-10
                    # A literal original-action regulator retains its minimum term.
                    log_full = log_actual + reserve * u * (6 - radius)
                    assert log_full <= log_bound + 12 * reserve * u + 1e-10
                    count += 1
    print(f"Actual one-link original conditional moments checked: {count}; "
          f"maximum log(actual/bound)={largest_log_ratio:.12g}.")
    print("All 54 literal original-action regulator bounds retain the minimum-energy term.")
    print("These quadratures do not integrate a pinned coarse output or certify locality.")
    guard()


def frustrated_core_check():
    identity = np.eye(2, dtype=complex)
    sigma = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]],
                      [[1, 0], [0, -1]]], dtype=complex)
    origin = (0,) * 4
    negative = {tuple(-1 if a == nu else 0 for a in range(4)) for nu in (1, 2, 3)}

    def shift(x, mu, amount=1):
        out = list(x)
        out[mu] += amount
        return tuple(out)

    def field(x, mu, q):
        if mu != 0:
            return identity
        if x == origin:
            return q
        return -identity if x in negative else identity

    def plaquette(x, mu, nu, q):
        return (field(x, mu, q) @ field(shift(x, mu), nu, q)
                @ field(shift(x, nu), mu, q).conj().T
                @ field(x, nu, q).conj().T)

    rng = np.random.default_rng(20261030)
    max_error, min_rough = 0.0, math.inf
    for _ in range(40):
        components = rng.normal(size=4)
        components /= np.linalg.norm(components)
        q = components[0] * identity + 1j * np.einsum("a,aij->ij", components[1:], sigma)
        values = [1 - np.trace(plaquette(x, 0, nu, q)).real / 2
                  for nu in (1, 2, 3) for x in (origin, shift(origin, nu, -1))]
        max_error = max(max_error, abs(sum(values) - 6))
        min_rough = min(min_rough, max(values))
        assert abs(sum(values) - 6) < 1e-12 and max(values) >= 1 - 1e-12
    print(f"Actual six-plaquette frustrated core, 40 fields: energy-sum error "
          f"{max_error:.6g}; minimum sampled largest f_p={min_rough:.12g}.")
    print("Analytically its conditional excitation is zero for every core field; "
          "the open-neighborhood argument is in the manuscript.")
    guard()


def debit_check():
    u, kappa, readers = 100, Fraction(1, 1000), 8
    budget = Fraction(1, 2) * u * 12  # Upper bound on one link's retained energy.
    debit = 2 * kappa * u * readers
    first_excess = int(budget // debit) + 1
    assert first_excess * debit > budget >= (first_excess - 1) * debit
    print(f"Repeated-comparison test, prescribed constant couplings: budget={budget}, "
          f"debit/step={debit}, first excess={first_excess}.")
    print("Failure is of repeated debit accounting; the single-horizon bound "
          "does not multiply these costs. This is not a U2 counterexample.")


if __name__ == "__main__":
    cone_check()
    kernel_check()
    excitation_check()
    frustrated_core_check()
    debit_check()
    print(f"Peak RSS bytes: {guard()} (<1000000000); BLAS threads=1.")
    print("Counted U1--U4 progress: zero.")
