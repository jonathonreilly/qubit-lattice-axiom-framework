#!/usr/bin/env python3
"""Check actual-contour geometry used in the full-posterior route test.

This evaluates specified flat configurations, not posterior integrals or
their typical mass. Full posterior normalizers cancel in the analytic cross
ratio; this script does not compute those normalizers or prove RG return.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import cmath
import itertools
import math
import resource
import sys
sys.dont_write_bytecode = True
from scipy.integrate import quad
from scipy.special import ive

L = 3
HALF = (L - 1) // 2


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else 1024 * rss)
    if rss >= 1_000_000_000:
        raise RuntimeError(f"RSS limit exceeded: {rss}")
    return rss


def walk(start, target, order):
    current = list(start)
    edges = []
    for mu in order:
        while current[mu] != target[mu]:
            sign = 1 if current[mu] < target[mu] else -1
            base = current.copy()
            if sign < 0:
                base[mu] -= 1
            edges.append((tuple(base), mu, sign))
            current[mu] += sign
    assert tuple(current) == tuple(target)
    return edges


def paired_paths(mu):
    root = (0,) * 4
    other = tuple(L if a == mu else 0 for a in range(4))
    for order in itertools.permutations(range(4)):
        for y in itertools.product(range(-HALF, HALF + 1), repeat=4):
            shifted = tuple(y[a] + other[a] for a in range(4))
            yield (walk(root, y, order)
                   + walk(y, shifted, (mu,))
                   + walk(shifted, other, tuple(reversed(order))))


PATHS = [list(paired_paths(mu)) for mu in range(4)]
assert all(len(paths) == 24 * L**4 for paths in PATHS)
assert max(map(len, itertools.chain.from_iterable(PATHS))) == 5 * L - 4


def mean_for_constant(mu, fine_angle):
    # SU(2) diagonal entries exp(+/- i fine_angle) in direction zero.
    values = []
    for path in PATHS[mu]:
        value = 1 + 0j
        for _, direction, sign in path:
            if direction == 0:
                value *= cmath.exp(1j * sign * fine_angle)
        values.append(value)
    target = cmath.exp(1j * L * fine_angle) if mu == 0 else 1 + 0j
    return sum(values) / len(values), max(abs(value - target) for value in values)


def coarse_checkerboard(x):
    return (-1) ** sum((a + HALF) // L for a in x)


def gauge_mean(mu):
    values = []
    for path in PATHS[mu]:
        value = 1
        for base, direction, _ in path:
            end = list(base)
            end[direction] += 1
            # Central +/- I is its own inverse, including reversed edges.
            value *= coarse_checkerboard(base) * coarse_checkerboard(end)
        values.append(value)
    assert set(values) == {-1}
    return sum(values) / len(values)


def log_z(t):
    integral = quad(lambda a: math.exp(t * (math.cos(a) - 1))
                    * math.sin(a)**2, 0, math.pi,
                    epsabs=2e-14, epsrel=2e-13)[0]
    value = t + math.log(2 * integral / math.pi)
    comparison = t + math.log(2 * ive(1, t) / t)
    assert abs(value - comparison) < 2e-12
    return value


def log_kernel(t, output, mean, normalizer):
    return t * (output.conjugate() * mean).real - normalizer


def main():
    print("Scope: exact-contour configuration checks; no posterior quadrature.")
    print(f"L={L}; paired paths per orientation={24 * L**4}; BLAS threads=1.")
    assert all(gauge_mean(mu) == -1 for mu in range(4))
    maximum_path_error = 0.0
    maximum_ratio_error = 0.0
    alpha = 0.15
    coarse_volume = 2**4
    for j in (0, 1, 3, 7):
        # A flat prefix U_l,0=exp(i alpha/L^(j+1-l) sigma_3).
        # Every earlier step matches the next field; all Wilson plaquettes
        # are identity. Their common density factors cancel before rounding.
        for level in range(j + 1):
            angle = alpha / L**(j + 1 - level)
            for mu in range(4):
                mean, error = mean_for_constant(mu, angle)
                expected = cmath.exp(1j * L * angle) if mu == 0 else 1
                assert abs(mean - expected) < 1e-12
                maximum_path_error = max(maximum_path_error, error)
        t = 100 - j
        normalizer = log_z(t)
        q = cmath.exp(1j * alpha)
        # Four terminal kernel values, retaining their input normalizers.
        cross_ratio = coarse_volume * (
            log_kernel(t, 1, 1, normalizer)
            + log_kernel(t, q, q, normalizer)
            - log_kernel(t, 1, q, normalizer)
            - log_kernel(t, q, 1, normalizer))
        expected = 2 * t * coarse_volume * (1 - math.cos(alpha))
        maximum_ratio_error = max(maximum_ratio_error, abs(cross_ratio - expected))
        assert abs(cross_ratio - expected) < 1e-10
        # Checkerboard pair has every coarse mean +/- I.
        links = 4 * coarse_volume
        diameter = links * (
            log_kernel(t, 1, 1, normalizer)
            + log_kernel(t, -1, -1, normalizer)
            - log_kernel(t, 1, -1, normalizer)
            - log_kernel(t, -1, 1, normalizer))
        assert abs(diameter - 4 * t * links) < 1e-10
        h = math.sqrt(2 / t)  # kappa=1, comparable current/next weights.
        print(f"depth={j}; flat cross-ratio log={cross_ratio:.12g}; "
              f"diameter={diameter:.12g}; weighted score oscillation={2*t*h:.12g}")
        guard()
    assert 2 * math.cos(2 * alpha) != 2  # Distinct terminal holonomy traces.
    print(f"Maximum individual path error: {maximum_path_error:.6g}.")
    print(f"Maximum four-kernel cross-ratio error: {maximum_ratio_error:.6g}.")
    print("The analytic variance identity is not numerically checked here.")
    print("No TV/covariance lower bound, U1--U4 closure or counterexample is inferred.")
    print(f"Peak RSS bytes: {guard()} (<1000000000).")


if __name__ == "__main__":
    main()
