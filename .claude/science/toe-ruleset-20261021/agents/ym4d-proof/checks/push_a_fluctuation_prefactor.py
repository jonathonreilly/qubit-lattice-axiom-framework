#!/usr/bin/env python3
"""Checks for a bare Gaussian prefactor and its failed uncut extension.

No nonlinear stationary point, full density, history sum or RG return is
computed here. The contour quartic is in the actual leading action.
The determinant test uses one zero-momentum, one-colour Bloch fibre,
not the full matrix on a finite compatible torus.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import sys
sys.dont_write_bytecode = True
import cmath
import math
from collections import Counter, defaultdict
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.special import ive
from push_a_resolvent_paths import PATHS, FREE, SITES, actual_matrices, guard


def normalizer_check():
    largest = 0.0
    largest_bound_ratio = 0.0
    for t in (12.0, 30.0, 100.0, 1000.0, 1000000.0):
        for angle in np.linspace(0, 2*math.pi, 9)[:-1]:
            r = 1+0.25*cmath.exp(1j*angle)
            s = t*r
            # Scaled Bessel computation, retaining its complex phase.
            value = 2*ive(1, s)*cmath.exp(abs(s.real)-s)/s
            leading = math.sqrt(2/math.pi)*s**(-1.5)
            relative = value/leading
            stop = min(2*t, 160.0)
            def integrand(y):
                return (cmath.exp(-r*y)*math.sqrt(y)*
                        math.sqrt(max(0.0, 1-y/(2*t))))
            re = quad(lambda y: integrand(y).real, 0, stop,
                      epsabs=2e-11, epsrel=2e-11, limit=150)[0]
            im = quad(lambda y: integrand(y).imag, 0, stop,
                      epsabs=2e-11, epsrel=2e-11, limit=150)[0]
            independent = r**1.5*(re+1j*im)/math.gamma(1.5)
            # The omitted tail for stop=160 has |r|<=1.25, Re r>=.75.
            tail = (1.25**1.5/math.gamma(1.5) *
                    math.exp(-0.75*160)*(160/0.75+1/0.75**2))
            error = abs(relative-independent)
            assert error <= 2e-10+tail
            assert abs(relative-1) <= 6/t
            largest = max(largest, error)
            largest_bound_ratio = max(largest_bound_ratio, abs(relative-1)/(6/t))
            guard()
    print("Complex normalizer: 40 scaled-Bessel/direct-Haar comparisons.")
    print(f"Maximum absolute relative-factor discrepancy {largest:.12g}; largest fraction of 6/t bound {largest_bound_ratio:.12g}.")
    print("These samples check the formula; the sector-integral estimate proves zero-freeness.")


def determinant_check():
    w, q, _ = actual_matrices((0, 0, 0, 0))
    h = (w+q.conj().T@q).real
    cov = np.linalg.inv(h)
    # Declared matrix-algebra test, not a claimed nonlinear background Hessian.
    diagonal = 0.7+0.3*np.cos(np.arange(len(FREE)))
    diagonal *= 0.2/max(np.sum(abs(cov)*diagonal[None, :], axis=1))
    e = np.diag(diagonal)
    ce = cov@e
    row = float(np.max(np.sum(abs(ce), axis=1)))
    assert row <= 0.2000000001
    direct = 0.5*(np.linalg.slogdet(h+e)[1]-np.linalg.slogdet(h)[1])
    power = np.eye(len(FREE))
    partial = 0.0
    inverse = np.zeros_like(h)
    power_inverse = np.eye(len(FREE))
    for n in range(1, 13):
        power = power@ce
        partial += 0.5*((-1)**(n+1))*np.trace(power)/n
        inverse += power_inverse@cov
        power_inverse = -power_inverse@ce
        error_bound = len(FREE)*row**(n+1)/(2*(n+1)*(1-row))
        assert abs(direct-partial) <= error_bound+2e-12
    inverse_error = np.max(np.sum(abs(inverse-np.linalg.inv(h+e)), axis=1))
    inverse_bound = row**12*np.max(np.sum(abs(cov), axis=1))/(1-row)
    assert inverse_error <= inverse_bound+1e-10
    print(f"Actual flat 244-coordinate H with declared diagonal test E: row norm {row:.12g}.")
    print(f"12-term log-determinant absolute error {abs(direct-partial):.12g}, last tail bound {error_bound:.12g}.")
    print(f"12-term inverse row error {inverse_error:.12g}, tail bound {inverse_bound:.12g}.")
    print("This is a signed matrix-series check, not a numerical check of TB7 or a spatial support theorem.")
    guard()


def actual_quartic_check():
    picked = ((0, 0, 0, 0), 1)
    assert 4*SITES.index(picked[0])+picked[1] in FREE
    histograms = []
    fourth = -Fraction(1, 4)
    second = Fraction(3)
    for mu, paths in enumerate(PATHS):
        counts = defaultdict(Counter)
        for path in paths:
            row = Counter()
            for x, direction, sign in path:
                if direction == picked[1] and all(x[a] % 3 == 0 for a in range(4)):
                    row[tuple(-x[a]//3 for a in range(4))] += sign
            for block, n in row.items():
                counts[block][n] += 1
        for block, cnt in sorted(counts.items()):
            cnt[0] += len(paths)-sum(cnt.values())
            nonzero = [(n, multiplicity) for n, multiplicity in cnt.items() if n]
            assert len(nonzero) == 1 and abs(nonzero[0][0]) == 1
            sign, multiplicity = nonzero[0]
            p = Fraction(multiplicity, len(paths))
            second += p*p/2
            fourth -= p*p*(1+3*(1-p)**2)/24
            histograms.append((block, mu, sign, multiplicity, p))
    assert sorted(row[3] for row in histograms) == [6]*6+[18, 54]
    assert fourth == -Fraction(918869623, 3673320192)
    print("Actual single free link ((0,0,0,0), direction 1), zero-based directions, kappa=1:")
    for block, mu, sign, multiplicity, p in histograms:
        print(f"  coarse base {block}, direction {mu}: {multiplicity}/1944 paths have exponent {sign}; others zero; p={p}.")
    print(f"Exact leading-action quadratic coefficient {second}; quartic coefficient {fourth} = {float(fourth):.12g}.")
    # Finite-angle evaluation of the enumerated path means, using extended
    # precision for the quartic correction. This reuses the histograms;
    # it is an algebra check, not independent evidence for their counts.
    def direct_action(angle):
        a = np.longdouble(angle)
        result = 12*np.sin(a/2)**2
        for _, _, sign, multiplicity, _ in histograms:
            p = np.longdouble(multiplicity)/np.longdouble(1944)
            m0 = 1-2*p*np.sin(a/2)**2
            m3 = sign*p*np.sin(a)
            radius = np.sqrt(m0*m0+m3*m3)
            result += m3*m3/(radius+m0)
        return result
    largest = 0.0
    for a in (0.1, 0.05, 0.025):
        aa = np.longdouble(a)
        coeff = (direct_action(a)-np.longdouble(second.numerator)/second.denominator*aa**2)/aa**4
        err = abs(float(coeff)-float(fourth))
        assert err < 0.009*a*a
        largest = max(largest, err)
        print(f"  a={a}: finite-action quartic quotient {float(coeff):.12g}, discrepancy {err:.12g}.")
    print("The homogeneous quartic is negative on an open cone; the uncut quartic Gaussian replacement diverges for every u>0.")
    print("This tests a replacement of the leading action, not the actual compact integral or the all-history target.")
    guard()


if __name__ == "__main__":
    guard()
    normalizer_check()
    determinant_check()
    actual_quartic_check()
    print(f"Peak RSS bytes: {guard()}; ceiling 1000000000; BLAS threads 1.")
