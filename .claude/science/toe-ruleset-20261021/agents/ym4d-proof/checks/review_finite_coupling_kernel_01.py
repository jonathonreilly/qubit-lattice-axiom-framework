#!/usr/bin/env python3
"""Independent Fourier-determinant and geometry diagnostics; criteria precede code."""
from pathlib import Path
import collections
import functools
import itertools
import json
import os
import resource
import sys
import time

import mpmath as mp
import numpy as np
from scipy.linalg import expm
import sympy as sy

started = time.monotonic()
mp.mp.dps = 60
checks = []


def record(name, condition, **details):
    row = {"name": name, "pass": bool(condition), **details}
    checks.append(row)
    print(json.dumps(row), flush=True)


def finite_normalizer(t, scalar=1, lam=0, winding=64):
    """Return exp(-t S) Z(t,S,lambda) by Fourier projection, not grid quadrature."""
    t, scalar, lam = map(mp.mpf, (t, scalar, lam))
    p, q = t * (scalar + lam) / 6, t * (scalar - lam) / 6
    z = 2 * mp.sqrt(p * q)
    entries = [mp.exp(-z) * mp.besseli(j, z) for j in range(winding + 3)]
    ratio = (p / q) ** mp.mpf("1.5")
    terms = []
    for k in range(winding + 1):
        a = [[entries[abs(k + i - j)] for j in range(3)] for i in range(3)]
        det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
               - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
               + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
        terms.append(det if k == 0 else det * (ratio ** k + ratio ** (-k)))
    return mp.exp(3 * z - t * scalar) * mp.fsum(terms)


def error_log(t, scalar=1, lam=0, winding=64):
    amp = 27 * mp.sqrt(3) / mp.pi * mp.mpf(scalar) ** (-4)
    return mp.log(finite_normalizer(t, scalar, lam, winding) * mp.mpf(t) ** 4 / amp)


record("resource_child_settings", os.getpriority(os.PRIO_PROCESS, 0) >= 10,
       nice=os.getpriority(os.PRIO_PROCESS, 0), threads={key: os.environ.get(key) for key in
       ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")})

# Exact rational moments in an independent two-coordinate eigenvalue representation.
x, y = sy.symbols("x y")
vand = (x - y) ** 2 * (2 * x + y) ** 2 * (x + 2 * y) ** 2


@functools.lru_cache(None)
def moment(a, b):
    if a < 0 or b < 0 or (a + b) % 2:
        return 0
    if not (a or b):
        return 1
    if a:
        return 2 * (a - 1) * moment(a - 2, b) - b * moment(a - 1, b - 1)
    return 2 * (b - 1) * moment(0, b - 2)


def average(poly):
    return sum(coeff * moment(*powers) for powers, coeff in sy.Poly(poly, x, y).terms())


norm = average(vand)
fourth = average(vand * (x ** 4 + y ** 4 + (x + y) ** 4)) / norm
third_squared = average(vand * (x ** 3 + y ** 3 - (x + y) ** 3) ** 2) / norm
haar = -average(vand * ((x - y) ** 2 + (2 * x + y) ** 2 + (x + 2 * y) ** 2)) / (12 * norm)
record("exact_Weyl_moments", norm == 324 and fourth == 360 and third_squared == 1080,
       norm=str(norm), fourth=str(fourth), third_squared=str(third_squared),
       haar_correction=str(haar), quartic_correction=str(fourth / 72),
       cubic_lambda_squared_correction=str(-third_squared / 648))

discrepancies = []
for t in (32, 64, 128):
    a, b = finite_normalizer(t, winding=48), finite_normalizer(t, winding=64)
    rel = abs(a / b - 1)
    ee = error_log(t)
    discrepancy = abs(t * ee + 1)
    discrepancies.append(discrepancy)
    record("SU3_cutoff_%s" % t, rel < mp.mpf("1e-25"), relative=str(rel))
    record("SU3_first_correction_%s" % t, discrepancy < mp.mpf("0.15"),
           tE=str(t * ee), discrepancy=str(discrepancy))
    wrong = mp.log(b * mp.mpf(t) ** mp.mpf("1.5") / (27 * mp.sqrt(3) / mp.pi))
    record("control_wrong_dimension_%s" % t, abs(t * wrong + 1) >= mp.mpf("0.15"),
           wrong_discrepancy=str(abs(t * wrong + 1)))
record("SU3_first_correction_approaches", all(a > b for a, b in zip(discrepancies, discrepancies[1:])),
       discrepancies=list(map(str, discrepancies)))

e0 = error_log(128)
derivatives = []
for h in (mp.mpf("1e-5"), mp.mpf("5e-6")):
    d2 = (error_log(128, lam=h) + error_log(128, lam=-h) - 2 * e0) / h ** 2
    derivatives.append(d2)
record("SU3_scalar_constraint_derivative_resolution", abs(derivatives[0] - derivatives[1]) < mp.mpf("1e-6"),
       derivatives=list(map(str, derivatives)), difference=str(abs(derivatives[0] - derivatives[1])))
record("SU3_scalar_constraint_derivative", abs(128 * derivatives[1] + mp.mpf(10) / 3) < mp.mpf("0.25"),
       t_dlambda2_E=str(128 * derivatives[1]), discrepancy=str(abs(128 * derivatives[1] + mp.mpf(10) / 3)))
record("control_erase_scalar_constraint", abs(mp.mpf(10) / 3) >= mp.mpf("0.25"),
       mutated_t_dlambda2_E="0", discrepancy=str(mp.mpf(10) / 3))

# Geometry is built on lifted integer paths before reducing modulo the torus.
L, T, side = 3, 2, 6
perms = list(itertools.permutations(range(4)))
offsets = list(itertools.product((-1, 0, 1), repeat=4))


def axis_path(start, end, order):
    point = list(start)
    result = []
    for axis in order:
        while point[axis] != end[axis]:
            sign = 1 if end[axis] > point[axis] else -1
            base = point.copy()
            if sign < 0:
                base[axis] -= 1
            result.append((tuple(base), axis, sign))
            point[axis] += sign
    return result


def contours(axis):
    root = (0, 0, 0, 0)
    second = tuple(L if j == axis else 0 for j in range(4))
    for offset in offsets:
        endpoint = tuple(offset[j] + second[j] for j in range(4))
        for order in perms:
            first = axis_path(root, offset, order)
            middle = axis_path(offset, endpoint, (axis,))
            last = [(b, a, -sign) for b, a, sign in reversed(axis_path(second, endpoint, order))]
            yield first + middle + last


all_words = {axis: list(contours(axis)) for axis in range(4)}
reader_counts = collections.Counter()
for axis, words in all_words.items():
    support = {(base, direction) for word in words for base, direction, sign in word}
    vertices = set(offsets) | {tuple(v[j] + (L if j == axis else 0) for j in range(4)) for v in offsets}
    endpoint_ok = True
    support_ok = True
    for word in words:
        endpoint = [0] * 4
        for base, direction, sign in word:
            endpoint[direction] += sign
            far = list(base)
            far[direction] += 1
            support_ok &= base in vertices and tuple(far) in vertices
        endpoint_ok &= endpoint == [L if j == axis else 0 for j in range(4)]
    record("S4prime_axis_%s" % axis,
           len(words) == 24 * L ** 4 and max(map(len, words)) == 5 * L - 4 and
           endpoint_ok and support_ok and len(support) <= 8 * L ** 4,
           path_count=len(words), max_length=max(map(len, words)), reader_links=len(support),
           endpoints=endpoint_ok, lifted_brick=support_ok)
    for coarse in itertools.product(range(T), repeat=4):
        translated = {(tuple((base[j] + L * coarse[j]) % side for j in range(4)), direction)
                      for base, direction in support}
        reader_counts.update(translated)
record("S4prime_all_reader_incidence", max(reader_counts.values()) <= 8,
       max_readers=max(reader_counts.values()), distinct_fine_links=len(reader_counts))

pauli = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex),
         np.diag([1, -1]).astype(complex)]
coarse_holonomy = {}
for coarse in itertools.product(range(T), repeat=4):
    for axis in range(4):
        coeff = (0.43 + 0.09 * axis, -0.27 + 0.06 * sum(coarse), 0.18 + 0.04 * coarse[axis])
        coarse_holonomy[(coarse, axis)] = expm(1j * sum(c * p for c, p in zip(coeff, pauli)))


def baseline_link(base, axis):
    base = tuple(v % side for v in base)
    coarse = tuple(((v + 1) // L) % T for v in base)
    local = tuple((v + 1) % L - 1 for v in base)
    return coarse_holonomy[(coarse, axis)] if local[axis] == 1 else np.eye(2, dtype=complex)


anchor = (1, 0, 0, 0)
maximum_error = 0.0
for word in all_words[0]:
    product = np.eye(2, dtype=complex)
    for base, direction, sign in word:
        shifted = tuple(base[j] + L * anchor[j] for j in range(4))
        value = baseline_link(shifted, direction)
        product = product @ (value if sign == 1 else np.linalg.inv(value))
    maximum_error = max(maximum_error, float(np.linalg.norm(product - coarse_holonomy[(anchor, 0)])))
record("S4prime_wrapping_noncommuting_holonomy", maximum_error < 1e-12, max_HS_error=maximum_error)

result = {"precision_decimal_digits": mp.mp.dps, "checks": checks,
          "passed": sum(row["pass"] for row in checks), "total": len(checks),
          "elapsed_seconds": time.monotonic() - started,
          "maxrss_native": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          "scope": "finite diagnostics only; no numerical certification of conservative t0"}
out = Path(__file__).with_name("review_finite_coupling_kernel_01_results.json")
with out.open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(json.dumps({"passed": result["passed"], "total": result["total"], "elapsed_seconds": result["elapsed_seconds"]}), flush=True)
sys.exit(0 if result["passed"] == result["total"] else 1)
