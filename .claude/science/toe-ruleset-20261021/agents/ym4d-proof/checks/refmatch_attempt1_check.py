#!/usr/bin/env python3
"""Finite REFMATCH diagnostics; refuse before mathematics if a guard fails."""
import cmath
import fcntl
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys

HERE = Path(__file__).resolve().parent
THREADS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS")
receipt = {"status": "NOT RUN", "checks": [], "resources": [],
           "criteria_sha256": hashlib.sha256((HERE / "refmatch_criteria.md").read_bytes()).hexdigest(),
           "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def guard():
    import psutil
    sample = {"nice": os.getpriority(os.PRIO_PROCESS, 0),
              "load": list(os.getloadavg()),
              "threads": {key: os.environ.get(key) for key in THREADS}}
    vm = psutil.virtual_memory()
    sample["available_fraction"] = vm.available / vm.total
    if sys.platform == "darwin":
        result = subprocess.run(["memory_pressure"], capture_output=True, text=True, check=True)
        line = next(s for s in result.stdout.splitlines()
                    if "System-wide memory free percentage:" in s)
        sample["free_fraction"] = float(line.rsplit(":", 1)[1].strip().strip("%")) / 100
    else:
        sample["free_fraction"] = vm.available / vm.total
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    sample["peak_rss_bytes"] = rss if sys.platform == "darwin" else rss * 1024
    receipt["resources"].append(sample)
    failures = []
    if sample["nice"] < 10:
        failures.append("nice < 10")
    if max(sample["load"]) >= 8:
        failures.append("load >= 8")
    if min(sample["free_fraction"], sample["available_fraction"]) < .30:
        failures.append("free/available memory < 30%")
    if sample["peak_rss_bytes"] >= 1_000_000_000:
        failures.append("peak RSS >= 1 GB")
    if any(value != "1" for value in sample["threads"].values()):
        failures.append("thread setting is not one")
    if failures:
        raise RuntimeError("; ".join(failures))


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(a, b):
    return [x * b for x in a]


def mul(a, b):
    return [sum(a[j] * b[i-j] for j in range(i+1)) for i in range(len(a))]


def inv(a):
    b = [1 / a[0]]
    for i in range(1, len(a)):
        b.append(-sum(a[j] * b[i-j] for j in range(1, i+1)) / a[0])
    return b


def affine(a, b):
    return [F(a), F(b), F(0), F(0), F(0)]


def check_three_signs():
    one = affine(1, 0)
    means = [affine("1/5", "1/8"), affine("-1/7", "1/9"), affine("1/6", "-1/10")]
    a, b = affine("1/32", "1/64"), affine("1/48", "-1/96")
    numerator, denominator = affine(0, 0), affine(0, 0)
    for state in itertools.product((-1, 1), repeat=3):
        weight = one
        for x, mean in zip(state, means):
            weight = mul(weight, scale(add(one, scale(mean, x)), F(1, 2)))
        weight = mul(weight, add(one, scale(a, state[0] * state[1])))
        weight = mul(weight, add(one, scale(b, state[1] * state[2])))
        denominator = add(denominator, weight)
        if state[0] == 1:
            numerator = add(numerator, weight)
    direct = mul(numerator, inv(denominator))
    m1, m2, m3 = means
    z_all = add(add(add(one, mul(a, mul(m1, m2))), mul(b, mul(m2, m3))),
                mul(mul(a, b), mul(m1, m3)))
    z_pin = add(add(add(one, mul(a, m2)), mul(b, mul(m2, m3))), mul(mul(a, b), m3))
    eliminated = mul(mul(scale(add(one, m1), F(1, 2)), z_pin), inv(z_all))
    frozen = scale(numerator, 1 / denominator[0])
    assert direct == eliminated
    assert any(x != y for x, y in zip(direct[1:], frozen[1:]))
    return {"name": "normalized_three_signs", "status": "PASS",
            "taylor_coefficients": list(map(str, direct)),
            "frozen_denominator_coefficients": list(map(str, frozen))}


def check_su2():
    comparisons = []
    for u in (2, 8, 32):
        h, t = math.sqrt(2 / u), u
        m = [sum(cmath.exp(2j * math.pi * r / 3) * (1.5j * h * r)**k
                 for r in range(3)) / (3 * math.factorial(k)) for k in range(5)]
        assert abs(m[0]) <= 1e-14
        m[0] = 0  # exact root-of-unity identity, checked above to roundoff
        q = mul(m, [z.conjugate() for z in m])
        one = [1, 0, 0, 0, 0]
        # Haar moments independently derived in the note: E x0^2=1/4, E x0^4=1/8.
        z = add(add(one, scale(q, t*t / 8)), scale(mul(q, q), t**4 / 192))
        v = add(z, scale(one, -1))
        power, logjet = one, [0] * 5
        for degree in range(1, 5):
            power = mul(power, v)
            logjet = add(logjet, scale(power, (-1)**(degree+1) / degree))
        actual = [2 * logjet[2], 24 * logjet[4]]
        expected = [3 * u / 8, -81 / 16 - 9 * u*u / 64]
        for x, y in zip(actual, expected):
            assert abs(x-y) <= 1e-10 * max(1, abs(y)), (u, x, y)
        comparisons.append({"u": u, "second": actual[0].real, "fourth": actual[1].real})
    return {"name": "su2_contour_fourth_jet_regression", "status": "PASS", "cases": comparisons}


def partitions(n):
    if n == 0:
        yield []
        return
    for old in partitions(n-1):
        yield old + [[n-1]]
        for index in range(len(old)):
            yield [block + [n-1] if i == index else block[:] for i, block in enumerate(old)]


def check_polynomials():
    size = 7
    one = [1] + [0] * (size-1)
    zero = [0] * size
    variable = [0, 1] + [0] * (size-2)
    M, I, L, C = [one], [one], [zero], [one]
    for n in range(1, size):
        moment = zero[:]
        for part in partitions(n):
            moment[len(part)] += 1
        M.append(moment)
        inverse, logarithm = zero[:], zero[:]
        for part in partitions(n):
            weight = one
            for block in part:
                weight = mul(weight, M[len(block)])
            inverse = add(inverse, scale(weight, math.factorial(len(part))))
            logarithm = add(logarithm, scale(weight, math.factorial(len(part)-1)))
        I.append(inverse)
        L.append(logarithm)
        density = zero[:]
        for k in range(n+1):
            density = add(density, scale(mul(M[k], I[n-k]), math.comb(n, k)))
        C.append(density)
    Mr, Ir, Lr = [one], [one], [zero]
    for n in range(1, size):
        moment = zero[:]
        for k in range(n):
            moment = add(moment, scale(mul(variable, Mr[k]), math.comb(n-1, k)))
        Mr.append(moment)
        inverse, logarithm = zero[:], zero[:]
        for k in range(1, n+1):
            inverse = add(inverse, scale(mul(Mr[k], Ir[n-k]), math.comb(n, k)))
            logarithm = add(logarithm, scale(mul(Mr[k], Ir[n-k]), math.comb(n-1, k-1)))
        Ir.append(inverse)
        Lr.append(logarithm)
    Cr = []
    for n in range(size):
        density = zero[:]
        for k in range(n+1):
            density = add(density, scale(mul(Mr[k], Ir[n-k]), math.comb(n, k)))
        Cr.append(density)
    assert M == Mr and I == Ir and L == Lr and C == Cr
    expected = [[0, 2], [0, 2, 6], [0, 2, 18, 26], [0, 2, 42, 156, 150]]
    assert all(C[n] == row + [0] * (size-len(row)) for n, row in enumerate(expected, 1))
    return {"name": "partition_vs_recurrence_polynomials", "status": "PASS", "C_0_through_6": C}


lock = None
try:
    lock = (HERE / "refmatch_numeric.lock").open("a+")
    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    guard()
    for check in (check_three_signs, check_su2, check_polynomials):
        guard()
        try:
            receipt["checks"].append(check())
        except Exception as exc:
            receipt["checks"].append({"name": check.__name__, "status": "FAIL", "reason": repr(exc)})
    guard()
    receipt["status"] = "FAIL" if any(x["status"] == "FAIL" for x in receipt["checks"]) else "PASS"
except Exception as exc:
    receipt["status"] = "PARTIAL" if receipt["checks"] else "NOT RUN"
    receipt["reason"] = repr(exc)
finally:
    if lock is not None:
        lock.close()
    result = json.dumps(receipt, indent=2) + "\n"
    (HERE / "refmatch_result.json").write_text(result)
    print(result, end="")
sys.exit(0 if receipt["status"] == "PASS" else 2)
