#!/usr/bin/env python3
"""Finite MIXSMALL controls, never a certificate of the open RG estimates."""
from pathlib import Path
from math import comb, factorial, pi, sin, sqrt
from itertools import permutations, product
import cmath
import datetime
import fcntl
import hashlib
import json
import os
import re
import resource
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REPORT = {"status": "NOT RUN", "checks": [], "resources": [],
          "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "criteria_sha256": hashlib.sha256((HERE / "mixsmall_criteria.md").read_bytes()).hexdigest(),
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


class Refusal(Exception):
    pass


def guard(label):
    names = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLAS_NUM_THREADS")
    row = {"label": label, "load": list(os.getloadavg()),
           "nice": os.getpriority(os.PRIO_PROCESS, 0),
           "rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           "threads": {k: os.environ.get(k) for k in names}}
    REPORT["resources"].append(row)
    if sys.platform != "darwin":
        raise Refusal("No verified free-memory/RSS convention on this platform")
    result = subprocess.run(["/usr/bin/memory_pressure", "-Q"],
                            capture_output=True, text=True, timeout=5)
    match = re.search(r"System-wide memory free percentage:\s*(\d+)%", result.stdout)
    if result.returncode or not match:
        row["memory_probe"] = result.stdout + result.stderr
        raise Refusal("Free memory could not be verified")
    row["free_percent"] = int(match.group(1))
    if row["nice"] < 10:
        raise Refusal("nice guard not met; no mathematical controls executed")
    if any(value != "1" for value in row["threads"].values()):
        raise Refusal("Single-thread guard not met")
    if max(row["load"]) >= 8 or row["free_percent"] < 30 or row["rss_bytes"] >= 1_000_000_000:
        raise Refusal("Resource threshold not met")


def check(name, condition, evidence):
    REPORT["checks"].append({"name": name, "status": "PASS" if condition else "FAIL",
                             "evidence": evidence})


def integer_partitions(n, least=1):
    if n == 0:
        yield ()
    for first in range(least, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def partition_sum(n, values, factor):
    total = 0
    for sizes in integer_partitions(n):
        count_denominator = 1
        term = factor(len(sizes))
        for size in sizes:
            count_denominator *= factorial(size)
            term *= values[size]
        for size in set(sizes):
            count_denominator *= factorial(sizes.count(size))
        total += factorial(n) // count_denominator * term
    return total


def algebra():
    scores = [0] + [r + 2 for r in range(1, 11)]
    exponential = [1]
    for n in range(10):
        exponential.append(sum(comb(n, r) * scores[r + 1] * exponential[n - r]
                               for r in range(n + 1)))
    independent = [partition_sum(n, scores, lambda k: 1) for n in range(11)]
    check("Bell recurrence versus integer partitions through 10", exponential == independent,
          {"recurrence": exponential, "partitions": independent})
    reciprocal = [1]
    for n in range(1, 11):
        reciprocal.append(-sum(comb(n, r) * exponential[r] * reciprocal[n - r]
                               for r in range(1, n + 1)))
    independent_inverse = [partition_sum(n, exponential, lambda k: (-1)**k * factorial(k))
                           for n in range(11)]
    check("Signed reciprocal derivative identity", reciprocal == independent_inverse,
          {"recurrence": reciprocal, "partitions": independent_inverse})
    observed = []
    expected = []
    for B in (0, 1, 2, 3, 7):
        M = [partition_sum(n, [0] + [B] * 4, lambda k: 1) for n in range(5)]
        I = [partition_sum(n, M, factorial) for n in range(5)]
        C = [sum(comb(n, r) * M[r] * I[n - r] for r in range(n + 1)) for n in range(5)]
        observed.append(C)
        expected.append([1, 2*B, 2*B+6*B**2, 2*B+18*B**2+26*B**3,
                         2*B+42*B**2+156*B**3+150*B**4])
    check("REALRGB fourth-order quotient polynomial controls", observed == expected,
          {"observed": observed, "expected": expected})


def path_phase(start, end, order, L, h):
    point = list(start)
    phase = velocity = 0.0
    for axis in order:
        while point[axis] != end[axis]:
            sign = 1 if end[axis] > point[axis] else -1
            if sign == -1:
                point[axis] -= 1
            if axis == 0:
                phase += sign * 2*pi/L**2 * point[1]
                velocity += sign * h * (point[1] % L) / (L-1)
            if sign == 1:
                point[axis] += 1
    return phase, velocity


def contours():
    L, u, kappa = 3, 10.0, 1.0
    h, t = sqrt(2/u), kappa*u
    root = ((L-1)//2,) * 4
    shifted_root = (root[0]+L,) + root[1:]
    sums = [0j, 0j, 0j]
    count = 0
    for order in permutations(range(4)):
        for y in product(range(L), repeat=4):
            endpoint = (y[0]+L,) + y[1:]
            a, da = path_phase(root, y, order, L, h)
            b, db = path_phase(y, endpoint, (0,), L, h)
            c, dc = path_phase(shifted_root, endpoint, order, L, h)
            phase, velocity = a+b-c, da+db-dc
            value = cmath.exp(1j*phase)
            sums[0] += value
            sums[1] += 1j*velocity*value
            sums[2] -= velocity**2*value
            count += 1
    actual = [z/count for z in sums]
    expected = [sum((1j*L*h*r/(L-1))**m * cmath.exp(2j*pi*r/L)
                    for r in range(L))/L for m in range(3)]
    errors = [abs(a-b) for a, b in zip(actual, expected)]
    check("Actual paired-contour zero mean and derivatives",
          count == 24*L**4 and abs(actual[0]) < 1e-12 and max(errors) < 1e-11,
          {"count": count, "mean_modulus": abs(actual[0]), "derivative_errors": errors})
    normalizer_second = t**2 * abs(actual[1])**2 / 4
    exact_second = kappa**2 * u * L**2 / (8*(L-1)**2*sin(pi/L)**2)
    check("SU2 normalizer second derivative and omission mutation",
          abs(normalizer_second-exact_second) < 1e-11 and normalizer_second > 1e-8,
          {"computed": normalizer_second, "closed_form": exact_second,
           "omission_error": normalizer_second})
    wrong_derivative = sums[1] / (24*L**3)
    check("Wrong path-divisor mutation detected", abs(wrong_derivative-expected[1]) > 1e-11,
          {"mutation_error": abs(wrong_derivative-expected[1])})


def geometry():
    hole = set(product((-1, 0, 1), repeat=4))
    closed = set(hole)
    for vertex in hole:
        for axis in range(4):
            for sign in (-1, 1):
                adjacent = list(vertex)
                adjacent[axis] += sign
                closed.add(tuple(adjacent))
    check("81-block hole boundaries", len(closed) == 297 and len(closed-hole) == 216,
          {"hole": len(hole), "closed": len(closed), "external_boundary": len(closed-hole)})


try:
    with (HERE / "mixsmall_numeric.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise Refusal("Lane numeric lock occupied") from error
        guard("before mathematics")
        algebra()
        guard("after algebra")
        contours()
        guard("after contours")
        geometry()
        guard("after geometry")
        REPORT["status"] = "PASS" if all(c["status"] == "PASS" for c in REPORT["checks"]) else "FAIL"
except Refusal as error:
    REPORT["status"] = "NOT RUN" if not REPORT["checks"] else "INCOMPLETE"
    REPORT["reason"] = str(error)
except Exception as error:
    REPORT["status"] = "ERROR"
    REPORT["reason"] = repr(error)
finally:
    encoded = json.dumps(REPORT, indent=2) + "\n"
    (HERE / "mixsmall_result.json").write_text(encoded)
    print(encoded, end="")
sys.exit(0 if REPORT["status"] == "PASS" else 2)
