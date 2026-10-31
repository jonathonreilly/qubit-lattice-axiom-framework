#!/usr/bin/env python3
"""Checks for the actual-posterior replica-exchange route.

Matrix evaluations use the actual paired contours on compatible pure-gauge
prefixes. Haar quadrature concerns the gauge-orbit occupation majorant, not
the finite-coupling full posterior. The manuscript proves the limiting-law
statement; this script neither samples that posterior nor bounds (A).
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import sys
sys.dont_write_bytecode = True
from collections import Counter
from fractions import Fraction
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ive
from push_a_posterior_geometry import PATHS, L, guard


IDENTITY = np.eye(2, dtype=complex)
SIGMA = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]],
                  [[1, 0], [0, -1]]], dtype=complex)
ROOT = (0, 0, 0, 0)
EDGE = (ROOT, 0)


def move(x, mu):
    y = list(x)
    y[mu] += 1
    return tuple(y)


def random_su2(rng):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    return q[0]*IDENTITY + 1j*np.einsum("a,aij->ij", q[1:], SIGMA)


class GaugePrefix:
    def __init__(self, depth, seed):
        self.depth = depth
        self.spacing = L**(depth+1)
        self.side = 6*self.spacing
        self.rng = np.random.default_rng(seed)
        self.gauges = {}
        self.links = {}

    def gauge(self, level, x):
        original = tuple((L**level*a) % self.side for a in x)
        if all(a % self.spacing == 0 for a in original):
            return IDENTITY
        if original not in self.gauges:
            self.gauges[original] = random_su2(self.rng)
        return self.gauges[original]

    def link(self, level, x, mu):
        key = (level, x, mu)
        if key not in self.links:
            self.links[key] = self.gauge(level, x) @ self.gauge(level, move(x, mu)).conj().T
        return self.links[key]


def mean(prefix, level, mu, replacement=None):
    total = np.zeros((2, 2), dtype=complex)
    maximum_path_error = 0.0
    target = prefix.link(level+1, ROOT, mu)
    for path in PATHS[mu]:
        value = IDENTITY.copy()
        for x, direction, sign in path:
            u = prefix.link(level, x, direction)
            if replacement is not None and (x, direction) == EDGE:
                u = replacement
            value = value @ (u if sign == 1 else u.conj().T)
        total += value
        if replacement is None:
            maximum_path_error = max(maximum_path_error, float(np.max(abs(value-target))))
    return total/len(PATHS[mu]), maximum_path_error


def plaquette(prefix, level, replacement=None):
    edges = ((ROOT, 0, 1), (move(ROOT, 0), 1, 1),
             (move(ROOT, 1), 0, -1), (ROOT, 1, -1))
    value = IDENTITY.copy()
    for x, mu, sign in edges:
        u = prefix.link(level, x, mu)
        if replacement is not None and (x, mu) == EDGE:
            u = replacement
        value = value @ (u if sign == 1 else u.conj().T)
    return value


def log_z(s):
    if s < 1e-7:
        return math.log1p(s*s/8)
    return s + math.log(2*ive(1, s)/s)


def log_kernel(t, output, m):
    # A real quaternion matrix M has M*M=r^2 I.
    r = math.sqrt(max(0.0, np.trace(m.conj().T @ m).real/2))
    return t*np.trace(output.conj().T @ m).real/2 - log_z(t*r)


def prefix_checks():
    counts = Counter(sum(sign for x, mu, sign in path if (x, mu) == EDGE)
                     for path in PATHS[0])
    assert counts == {0: 1656, 1: 288}
    alpha = Fraction(counts[1], len(PATHS[0]))
    assert alpha == Fraction(4, 27)
    print(f"Exact last-kernel edge multiplicity: {dict(sorted(counts.items()))}; alpha={alpha}.")
    max_path_error = max_wilson_error = max_kernel_error = max_mean_error = 0.0
    for depth in (1, 2, 4):
        first = GaugePrefix(depth, 20261030 + 100*depth)
        second = GaugePrefix(depth, 20261031 + 100*depth)
        original_first = first.link(0, ROOT, 0)
        original_second = second.link(0, ROOT, 0)
        original_energy = 0.0
        changed_energy = 0.0
        for prefix, replacement in ((first, original_second), (second, original_first)):
            original_energy += 1 - np.trace(plaquette(prefix, 0)).real/2
            changed_energy += 1 - np.trace(plaquette(prefix, 0, replacement)).real/2
        expected = 2*(1 - np.trace(original_second @ original_first.conj().T).real/2)
        max_wilson_error = max(max_wilson_error, abs(changed_energy-original_energy-expected))
        assert abs(original_energy) < 1e-12
        assert abs(changed_energy-original_energy-expected) < 1e-12
        print(f"depth={depth}: original plaquette-pair action={original_energy:.3g}; "
              f"single-edge exchange action increase={changed_energy-original_energy:.12g}.")
        for level in range(depth):
            m1, err1 = mean(first, level, 0)
            m2, err2 = mean(second, level, 0)
            v1, v2 = first.link(level+1, ROOT, 0), second.link(level+1, ROOT, 0)
            max_path_error = max(max_path_error, err1, err2)
            coefficient = 2*(1 - np.trace(v1.conj().T @ v2).real/2)
            assert coefficient > 1e-6
            for t in (1.0, 10.0, 100.0):
                log_ratio = (log_kernel(t, v2, m1) + log_kernel(t, v1, m2)
                             - log_kernel(t, v1, m1) - log_kernel(t, v2, m2))
                max_kernel_error = max(max_kernel_error, abs(log_ratio+t*coefficient))
                assert abs(log_ratio+t*coefficient) < 2e-10
            print(f"  internal kernel level={level}: exchange log ratio/t={-coefficient:.12g}; "
                  "input normalizers retained and cancel for this output-only exchange.")
        # At the last level both output roots are fixed by the terminal identity.
        for prefix in (first, second):
            m, error = mean(prefix, depth, 0)
            assert np.max(abs(m-IDENTITY)) < 1e-12
            max_path_error = max(max_path_error, error)
        u1, u2 = first.link(depth, ROOT, 0), second.link(depth, ROOT, 0)
        mixed1, _ = mean(first, depth, 0, u2)
        mixed2, _ = mean(second, depth, 0, u1)
        q = u2 @ u1.conj().T
        expected1 = (1-float(alpha))*IDENTITY + float(alpha)*q
        expected2 = (1-float(alpha))*IDENTITY + float(alpha)*q.conj().T
        max_mean_error = max(max_mean_error, float(np.max(abs(mixed1-expected1))),
                             float(np.max(abs(mixed2-expected2))))
        assert max_mean_error < 2e-12
        a = np.trace(expected1).real/2
        r = math.sqrt(np.trace(expected1.conj().T @ expected1).real/2)
        assert r-a > 1e-8
        print(f"  last kernel: a={a:.12g}, r={r:.12g}, positive mixed gap={r-a:.12g}.")
        for t in (1.0, 10.0, 100.0, 1000.0):
            observed = (log_kernel(t, IDENTITY, mixed1) + log_kernel(t, IDENTITY, mixed2)
                        - 2*log_kernel(t, IDENTITY, IDENTITY))
            expected_log = 2*t*(a-1) + 2*(log_z(t)-log_z(t*r))
            max_kernel_error = max(max_kernel_error, abs(observed-expected_log))
            assert abs(observed-expected_log) < 2e-9
            # The changed mean lengths force a normalizer term; it is nonzero.
            normalizer_term = 2*(log_z(t)-log_z(t*r))
            assert normalizer_term > 0
            print(f"    t={t:g}: log pair-kernel ratio={observed:.12g}; "
                  f"normalizer contribution={normalizer_term:.12g}.")
        guard()
    print(f"Maximum errors: individual contour={max_path_error:.6g}, "
          f"Wilson exchange={max_wilson_error:.6g}, "
          f"mixed mean={max_mean_error:.6g}, kernel log ratio={max_kernel_error:.6g}.")


def orbit_quadrature():
    largest_error = 0.0
    print("Haar gauge-orbit empty-edge majorant; not a finite-u posterior expectation:")
    for coupling in (0.1, 1.0, 10.0, 100.0, 1000.0):
        integral = 2/math.pi * quad(
            lambda angle: math.exp(-2*coupling*(1-math.cos(angle)))*math.sin(angle)**2,
            0, math.pi, epsabs=1e-13, epsrel=1e-11)[0]
        bessel = ive(1, 2*coupling)/coupling
        error = abs(integral-bessel)
        largest_error = max(largest_error, error)
        assert error < 1e-12
        print(f"  coupling={coupling:g}: integral={integral:.12g}; scaled Bessel={bessel:.12g}.")
    print(f"Maximum independent Haar/Bessel absolute discrepancy={largest_error:.6g}.")


def orbit_pair_identity():
    # A two-point exchange orbit is the exact algebra behind RX1, not a
    # quadrature or approximation to the full posterior.
    largest_error = 0.0
    for delta in (-40.0, -2.0, 0.0, 0.3, 12.0, 40.0):
        p = 1/(1+math.exp(-delta))
        odd_values = (1.7, -1.7)
        lhs = p*odd_values[0] + (1-p)*odd_values[1]
        rhs = (p*odd_values[0]*math.tanh(delta/2)
               + (1-p)*odd_values[1]*math.tanh(-delta/2))
        largest_error = max(largest_error, abs(lhs-rhs))
        assert abs(lhs-rhs) < 1e-14
    print(f"Two-point swap-orbit tanh identity maximum discrepancy={largest_error:.6g}.")


if __name__ == "__main__":
    print("Scope: actual-contour matrix checks and gauge-orbit Haar quadrature; BLAS threads=1.")
    prefix_checks()
    orbit_quadrature()
    orbit_pair_identity()
    print(f"Peak RSS bytes: {guard()} (<1000000000).")
    print("No finite-coupling full-posterior simulation, covariance estimate, or induction closure.")
    print("U1--U4 count remains four; counted progress is zero.")
