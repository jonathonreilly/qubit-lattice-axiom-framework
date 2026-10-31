#!/usr/bin/env python3
"""Preregistered exact algebra/geometry checks; no physics simulation."""
from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import os
import re
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "checks/realrgb_check_result.json"
LOCK = ROOT / "checks/realrgb_check.lock"
THREADS = ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS")
report = {"kind": "exact finite regression, not Yang–Mills evidence",
          "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "criteria_sha256": hashlib.sha256(
              (ROOT / "checks/realrgb_criteria.md").read_bytes()).hexdigest(),
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "checks": [], "resources": [], "status": "NOT_RUN"}


class ResourceRefusal(RuntimeError):
    pass


def guard(label):
    if sys.platform != "darwin":
        raise ResourceRefusal("This registered free-memory check is for macOS.")
    mem = subprocess.run(["/usr/bin/memory_pressure", "-Q"], text=True,
                         capture_output=True, check=True)
    match = re.search(r"System-wide memory free percentage:\s*([0-9.]+)%",
                      mem.stdout)
    if not match:
        raise ResourceRefusal("Cannot determine system free-memory percentage.")
    sample = {"label": label, "load": list(os.getloadavg()),
              "free_percent": float(match.group(1)),
              "rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "nice": os.getpriority(os.PRIO_PROCESS, 0),
              "threads": {key: os.environ.get(key) for key in THREADS}}
    report["resources"].append(sample)
    good = (max(sample["load"]) < 8 and sample["free_percent"] >= 30
            and sample["rss_bytes"] < 1_000_000_000 and sample["nice"] >= 10
            and all(value == "1" for value in sample["threads"].values()))
    if not good:
        raise ResourceRefusal("Resource guard failed: " + json.dumps(sample))


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    r = [0] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    return trim(r)


def mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x * y
    return trim(r)


def scale(p, n):
    return trim([n * x for x in p])


def partitions(n):
    if n == 0:
        yield ()
    else:
        for pi in partitions(n - 1):
            yield pi + ((n,),)
            for i in range(len(pi)):
                yield pi[:i] + (pi[i] + (n,),) + pi[i + 1:]


def partition_polynomial(n, block_values, factor):
    total = [0]
    for pi in partitions(n):
        term = [factor(len(pi))]
        for block in pi:
            term = mul(term, block_values[len(block)])
        total = add(total, term)
    return total


def check(name, actual, expected):
    record = {"name": name, "actual": actual, "expected": expected,
              "passed": actual == expected}
    report["checks"].append(record)
    if actual != expected:
        raise AssertionError(name + ": " + repr(record))


def source_hashes():
    current = {}
    for line in (ROOT / "checks/realrgb_input_sha256.txt").read_text().splitlines():
        digest, rel = line.split(None, 1)
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if actual != digest:
            raise AssertionError("Source changed: " + rel)
        current[rel] = actual
    return current


def main():
    guard("startup")
    before = source_hashes()
    log_bounds = [[1]] + [[0, 1]] * 4
    moments = [partition_polynomial(n, log_bounds, lambda k: 1)
               for n in range(5)]
    expected_m = [[1], [0, 1], [0, 1, 1], [0, 1, 3, 1], [0, 1, 7, 6, 1]]
    check("Bell partitions", moments, expected_m)
    # Independent exponential differentiation recurrence.
    recurrence_m = [[1]]
    for n in range(1, 5):
        value = [0]
        for k in range(1, n + 1):
            value = add(value, scale(mul([0, 1], recurrence_m[n - k]),
                                     comb(n - 1, k - 1)))
        recurrence_m.append(value)
    check("Bell recurrence", recurrence_m, expected_m)
    guard("Bell")

    inverse = [[1]]
    for n in range(1, 5):
        value = [0]
        for k in range(1, n + 1):
            value = add(value, scale(mul(moments[k], inverse[n - k]), comb(n, k)))
        inverse.append(value)
    expected_i = [[1], [0, 1], [0, 1, 3], [0, 1, 9, 13], [0, 1, 21, 78, 75]]
    check("Reciprocal recurrence", inverse, expected_i)
    partition_i = [partition_polynomial(n, moments, factorial) for n in range(5)]
    check("Reciprocal partitions", partition_i, expected_i)
    guard("reciprocal")

    quotients = []
    for n in range(5):
        value = [0]
        for k in range(n + 1):
            value = add(value, scale(mul(moments[k], inverse[n - k]), comb(n, k)))
        quotients.append(value)
    expected_c = [[1], [0, 2], [0, 2, 6], [0, 2, 18, 26], [0, 2, 42, 156, 150]]
    check("Quotient Leibniz", quotients, expected_c)
    p4 = sum((Fraction(sum(p), factorial(n)) for n, p in enumerate(quotients)),
             Fraction(0))
    check("P4 at unit arguments", str(p4), "117/4")
    guard("quotient")

    logs = [partition_polynomial(n, moments, lambda k: factorial(k - 1))
            for n in range(1, 5)]
    expected_l = [[0, 1], [0, 1, 2], [0, 1, 6, 6], [0, 1, 14, 36, 26]]
    check("Logarithmic partitions", logs, expected_l)
    guard("logarithm")

    hole = {tuple(x % 7 for x in v) for v in product((-1, 0, 1), repeat=4)}
    hood = set(hole)
    for v in hole:
        for axis in range(4):
            for step in (-1, 1):
                w = list(v)
                w[axis] = (w[axis] + step) % 7
                hood.add(tuple(w))
    singleton = (2, 0, 0, 0)
    assert singleton not in hole and singleton in hood
    check("RD3 hole geometry", [len(hole), len(hood), len(hole | {singleton})],
          [81, 297, 82])
    guard("geometry")
    after = source_hashes()
    check("Source manifest preserved", after, before)
    guard("finished")
    report["status"] = "PASS"


owned_lock = False
exit_code = 0
try:
    lock_fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    owned_lock = True
    with os.fdopen(lock_fd, "w") as lock:
        lock.write(str(os.getpid()) + "\n")
    main()
except ResourceRefusal as error:
    report["status"] = "RESOURCE_GUARD_FAILED"
    report["error"] = str(error)
    exit_code = 2
except Exception as error:
    report["status"] = "FAILED"
    report["error"] = type(error).__name__ + ": " + str(error)
    exit_code = 1
finally:
    if owned_lock:
        LOCK.unlink()
    report["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "checks": len(report["checks"]),
                      "resource_samples": len(report["resources"]),
                      "error": report.get("error")}, indent=2))
sys.exit(exit_code)
