#!/usr/bin/env python3
"""Exact finite MATCHB controls; enforce resource gates before mathematics."""
from fractions import Fraction as F
import fcntl
import hashlib
import itertools
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
THREADS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS")
receipt = {"status": "NOT RUN", "checks": [], "resources": [],
           "criteria_sha256": hashlib.sha256((HERE / "matchb_criteria.md").read_bytes()).hexdigest(),
           "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "proof_sha256": hashlib.sha256((ROOT / "MATCHB.md").read_bytes()).hexdigest()}


def guard():
    sample = {"nice": os.getpriority(os.PRIO_PROCESS, 0),
              "load": list(os.getloadavg()),
              "threads": {key: os.environ.get(key) for key in THREADS},
              "memory_status": "NOT MEASURED"}
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    sample["peak_rss_bytes"] = rss if sys.platform == "darwin" else rss * 1024
    receipt["resources"].append(sample)
    failures = []
    if sample["nice"] < 10:
        failures.append("nice < 10")
    if max(sample["load"]) >= 8:
        failures.append("load >= 8")
    if sample["peak_rss_bytes"] >= 1_000_000_000:
        failures.append("peak RSS >= 1 GB")
    if any(value != "1" for value in sample["threads"].values()):
        failures.append("thread setting not one")
    if failures:
        raise RuntimeError("; ".join(failures))
    if sys.platform == "darwin":
        result = subprocess.run(["memory_pressure"], capture_output=True, text=True, check=True)
        line = next(s for s in result.stdout.splitlines()
                    if "System-wide memory free percentage:" in s)
        sample["free_fraction"] = float(line.rsplit(":", 1)[1].strip().strip("%")) / 100
        vmstat = subprocess.run(["vm_stat"], capture_output=True, text=True, check=True).stdout
        page_size = int(re.search(r"page size of (\d+) bytes", vmstat).group(1))
        pages = {name: int(value) for name, value in
                 re.findall(r"^(Pages [^:]+):\s+(\d+)\.", vmstat, re.MULTILINE)}
        physical_bytes = int(subprocess.run(["sysctl", "-n", "hw.memsize"],
                             capture_output=True, text=True, check=True).stdout)
        # Conservative native availability measure; no credit for compressed,
        # purgeable or speculative pages. The registered 30% gate is unchanged.
        available_pages = max(0, pages["Pages free"] - pages["Pages speculative"])
        available_pages += pages["Pages inactive"]
        sample["available_fraction"] = available_pages * page_size / physical_bytes
        sample["available_pages"] = available_pages
        sample["physical_bytes"] = physical_bytes
        sample["page_size"] = page_size
        sample["memory_method"] = "memory_pressure plus (free-speculative+inactive) pages / physical memory"
    else:
        import psutil
        vm = psutil.virtual_memory()
        sample["available_fraction"] = vm.available / vm.total
        sample["free_fraction"] = vm.available / vm.total
        sample["memory_method"] = "psutil available / total"
    sample["memory_status"] = "MEASURED"
    if min(sample["free_fraction"], sample["available_fraction"]) < .30:
        raise RuntimeError("free/available memory < 30%")


def chain_weight(state, t):
    result = F(1, 2 ** len(state))
    for left, right in zip(state, state[1:]):
        result *= 1 + t * left * right
    return result


def check_dependence():
    states = list(itertools.product((-1, 1), repeat=4))
    weights = {x: chain_weight(x, F(1, 2)) for x in states}
    assert sum(weights.values()) == 1
    means = [sum(w * x[i] for x, w in weights.items()) for i in range(4)]
    assert means == [0] * 4
    correlation = sum(w * x[0] * x[3] for x, w in weights.items())
    assert correlation == F(1, 8)
    joint = sum(w * F(x[0], 8) * F(x[3], 8) for x, w in weights.items())
    separate = means[0] * means[3] / 64
    assert joint - separate == F(1, 512)
    assert joint != separate
    return {"name": "chain_dependence", "status": "PASS",
            "correlation": str(correlation), "factorization_defect": str(joint - separate),
            "product_of_marginals_mutation": "REJECTED"}


ORDER = 4


def poly(value, slope=0):
    return [F(value), F(slope)] + [F(0)] * (ORDER - 1)


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(a, q):
    return [x * q for x in a]


def mul(a, b):
    return [sum(a[j] * b[i-j] for j in range(i+1)) for i in range(ORDER+1)]


def inv(a):
    result = [1 / a[0]]
    for i in range(1, ORDER+1):
        result.append(-sum(a[j] * result[i-j] for j in range(1, i+1)) / a[0])
    return result


def direct_tilted(t, a, b, freeze_denominator=False):
    numerator, denominator = poly(0), poly(0)
    for x in itertools.product((-1, 1), repeat=4):
        weight = poly(F(1, 16))
        for left, right in zip(x, x[1:]):
            weight = mul(weight, add(poly(1), scale(t, left * right)))
        weight = mul(weight, add(poly(1), scale(a, x[0])))
        weight = mul(weight, add(poly(1), scale(b, x[3])))
        denominator = add(denominator, weight)
        if x[0] == 1:
            numerator = add(numerator, weight)
    divisor = poly(denominator[0]) if freeze_denominator else denominator
    return mul(numerator, inv(divisor)), denominator


def check_marginal():
    t, a, b = poly(F(1, 2), F(1, 13)), poly(F(1, 5), F(1, 7)), poly(F(1, 6), -F(1, 11))
    direct, z = direct_tilted(t, a, b)
    rho = mul(mul(t, t), t)
    expected_z = add(poly(1), mul(mul(a, b), rho))
    conditional = mul(scale(mul(add(poly(1), a), add(poly(1), mul(b, rho))), F(1, 2)), inv(expected_z))
    frozen_z, unused = direct_tilted(t, a, b, True)
    frozen_reference, unused = direct_tilted(poly(F(1, 2)), a, b)
    assert z == expected_z
    assert direct == conditional
    assert direct[1:] != frozen_z[1:]
    assert direct[1:] != frozen_reference[1:]
    return {"name": "nonproduct_marginal_jets", "status": "PASS",
            "taylor_coefficients": list(map(str, direct)),
            "frozen_denominator_coefficients": list(map(str, frozen_z)),
            "frozen_reference_coefficients": list(map(str, frozen_reference)),
            "omission_mutations": ["frozen denominator REJECTED", "frozen reference REJECTED"]}


def partitions(items):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for partition in partitions(rest):
        yield ((first,),) + partition
        for index in range(len(partition)):
            yield partition[:index] + ((first,) + partition[index],) + partition[index+1:]


def product(values):
    result = F(1)
    for value in values:
        result *= value
    return result


def factorial(n):
    result = 1
    for k in range(2, n+1):
        result *= k
    return result


def check_cumulant_gas():
    labels = tuple(range(4))
    states = list(itertools.product((-1, 1), repeat=4))
    weights = {x: chain_weight(x, F(1, 2)) for x in states}
    subsets = [tuple(i for i in labels if mask & (1 << i)) for mask in range(1 << 4)]
    moments = {B: sum(w * product(F(x[i], 10) for i in B) for x, w in weights.items()) for B in subsets}
    cumulants = {}
    for B in subsets[1:]:
        cumulants[B] = sum((-1) ** (len(pi)-1) * factorial(len(pi)-1)
                           * product(moments[tuple(sorted(A))] for A in pi)
                           for pi in partitions(B))

    def gas(remaining, singletons_only=False):
        if not remaining:
            return F(1)
        first = min(remaining)
        total = gas(remaining - {first}, singletons_only)
        for B, value in cumulants.items():
            if first in B and set(B) <= remaining and (not singletons_only or len(B) == 1):
                total += value * gas(remaining - set(B), singletons_only)
        return total

    direct = sum(w * product(1 + F(x[i], 10) for i in labels) for x, w in weights.items())
    actual = gas(set(labels))
    mutant = gas(set(labels), True)
    assert actual == direct
    assert mutant != direct
    return {"name": "label_disjoint_cumulant_gas", "status": "PASS",
            "direct_and_gas": str(direct), "singleton_only_mutant": str(mutant),
            "higher_cumulants_omission": "REJECTED", "cumulant_types": len(cumulants)}


def check_regeneration():
    t, s = F(1, 2), F(2, 3)
    matrix = {(a, b): F(0) for a, b in itertools.product((-1, 1), repeat=2)}
    total = F(0)
    for z in itertools.product((-1, 1), repeat=3):
        for x in itertools.product((-1, 1), repeat=3):
            weight = chain_weight(z, t) * product((1+s*x[i]*z[i])/2 for i in range(3))
            total += weight
            if x[1] == 1:
                matrix[x[0], x[2]] += weight
    assert total == 1
    event_mass = sum(matrix.values())
    mean_left = sum(a * w for (a, b), w in matrix.items()) / event_mass
    mean_right = sum(b * w for (a, b), w in matrix.items()) / event_mass
    mean_pair = sum(a * b * w for (a, b), w in matrix.items()) / event_mass
    covariance = mean_pair - mean_left * mean_right
    determinant = matrix[-1, -1] * matrix[1, 1] - matrix[-1, 1] * matrix[1, -1]
    expected = s*s*t*t*(1-s*s)/16
    assert covariance == F(5, 81)
    assert determinant == expected and determinant > 0
    return {"name": "noisy_chain_regeneration", "status": "PASS",
            "conditional_covariance": str(covariance), "endpoint_determinant": str(determinant),
            "conditional_independence_inference": "REJECTED", "joint_states": 64}


def main():
    started = time.monotonic()
    lock = (HERE / "matchb_numeric.lock").open("a+")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        guard()
        for check in (check_dependence, check_marginal, check_cumulant_gas, check_regeneration):
            guard()
            try:
                receipt["checks"].append(check())
            except AssertionError as exc:
                receipt["checks"].append({"name": check.__name__, "status": "FAIL", "error": repr(exc)})
                raise
        guard()
        receipt["status"] = "PASS"
    except AssertionError as exc:
        receipt["status"] = "FAIL"
        receipt["error"] = repr(exc)
    except Exception as exc:
        receipt["status"] = "PARTIAL" if receipt["checks"] else "NOT RUN"
        receipt["error"] = repr(exc)
    finally:
        receipt["seconds"] = time.monotonic() - started
        receipt["scope"] = "Finite rational diagnostics only; not actual gauge-history bounds or regeneration."
        encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
        (HERE / "matchb_result.json").write_text(encoded)
        print(encoded, end="")
        lock.close()
    return 0 if receipt["status"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
