#!/usr/bin/env python3
"""Numerical cross-checks, not proofs, for MANUSCRIPT_RG.md.

One process; set BLAS threads before importing numpy/scipy.  RSS is checked
explicitly rather than constrained with RLIMIT_AS.  No simulation of an RG
return or of a conditioned history is claimed.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import math
import platform
import resource
import sys
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import gammaincc, gamma, ive


def rss_bytes():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(rss if sys.platform == "darwin" else 1024 * rss)


def guard():
    value = rss_bytes()
    if value >= 1_000_000_000:
        raise RuntimeError(f"RSS limit exceeded: {value}")
    return value


def log_a_bessel(s):
    if s == 0:
        return 0.0
    return math.log(2) + math.log(float(ive(1, s))) - math.log(s)


def haar_integral(s, fn=lambda x: 1.0):
    # Independent direct Haar integral. Scaling theta prevents loss of the
    # narrow cap at large s.  1-cos(theta)=2*sin(theta/2)^2 is cancellation-safe.
    scale = math.sqrt(max(s, 1.0))
    upper = min(math.pi * scale, 16.0)
    def integrand(z):
        theta = z / scale
        x = 2 * s * math.sin(theta / 2) ** 2
        return 2 / math.pi * math.sin(theta) ** 2 * math.exp(-x) * fn(x) / scale
    value, error = quad(integrand, 0, upper, epsabs=1e-13 / scale ** 3,
                        epsrel=2e-11, limit=200)
    return value, error


def run():
    guard()
    scales = [0.0, 1e-6, 0.01, 0.1, 1.0, 3.0, 10.0, 100.0, 1e3, 1e5]
    rel_errors = []
    max_mgf_ratio = 0.0
    max_moment_ratio = 0.0
    checks = 0
    for s in scales:
        direct, err = haar_integral(s)
        analytic = math.exp(log_a_bessel(s))
        rel = abs(direct / analytic - 1)
        rel_errors.append(rel)
        assert rel < 2e-9, (s, direct, analytic, err)
        checks += 1
        for b in [0.0, 0.1, 0.5, 0.9]:
            ratio = math.exp(log_a_bessel((1-b)*s) - log_a_bessel(s))
            bound = (1-b) ** (-1.5)
            assert ratio <= bound * (1+2e-12), (s, b, ratio, bound)
            max_mgf_ratio = max(max_mgf_ratio, ratio / bound)
            checks += 1
        for power in [0.5, 1, 1.5, 2, 3, 6]:
            numer, _ = haar_integral(s, lambda x: x ** power)
            moment = numer / direct
            bound = gamma(power+1.5) / gamma(1.5)
            assert moment <= bound * (1+2e-9), (s, power, moment, bound)
            max_moment_ratio = max(max_moment_ratio, moment / bound)
            checks += 1
        guard()

    # Direct SU(2) Haar second moments test tangent/radial normalizer scores.
    # In S^3, E[v_1^2 | v_0] = (1-v_0^2)/3.
    fisher_rows = []
    for s in [0.1, 1, 10, 100, 1000]:
        a, _ = haar_integral(s)
        tangent, _ = haar_integral(s, lambda x: (1-(1-x/s)**2)/3)
        tangent /= a
        bessel_ratio = float(ive(2, s) / ive(1, s)) / s
        assert abs(tangent-bessel_ratio) < 2e-9, (s, tangent, bessel_ratio)
        fisher_rows.append((s, tangent, bessel_ratio))
        checks += 1

    # Conditioning check: at fixed mean I, fixing V=-I makes X=2t.
    # This explicitly is a point evaluation, NOT a positive-mass history.
    point_rows = [(t, 2*t, math.exp(0.1*2*t), 0.9**(-1.5))
                  for t in [1, 10, 100]]
    print(f"Python {platform.python_version()}; numpy {np.__version__}; scipy {scipy.__version__}")
    print(f"Checks: {checks}; all numerical inequalities satisfied on the declared grid.")
    print(f"Max Bessel/direct-Haar relative error: {max(rel_errors):.6g}")
    print(f"Max MGF/bound ratio (includes b=0 equality): {max_mgf_ratio:.12g}")
    print(f"Max fractional moment/Gamma bound ratio: {max_moment_ratio:.12g}")
    print("Tangent variance: (s, Haar quadrature, Bessel recurrence)")
    for row in fisher_rows:
        print(row)
    print("Pinned-output diagnostic: (t, X, exp(0.1 X), unconditional MGF bound)")
    for row in point_rows:
        print(row)
    print(f"Peak RSS bytes: {guard()}; limit: 1000000000; BLAS threads: 1")
    print("No all-history, retained-output, or regeneration estimate tested.")


if __name__ == "__main__":
    run()
