#!/usr/bin/env python3
"""Preregistered finite bookkeeping diagnostic; no gauge integration."""
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import resource
import sys

HERE = Path(__file__).resolve().parent
THREADS = (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
)


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def guard():
    sample = {
        "nice": os.getpriority(os.PRIO_PROCESS, 0),
        "load": list(os.getloadavg()),
        "rss_bytes": peak_rss_bytes(),
        "threads": {name: os.environ.get(name) for name in THREADS},
        "memory": "not measured before priority/thread/load/RSS acceptance",
    }
    errors = []
    if sample["nice"] < 10:
        errors.append("actual nice < 10; requested priority was not applied")
    if any(value != "1" for value in sample["threads"].values()):
        errors.append("a required thread variable is not one")
    if max(sample["load"]) >= 8:
        errors.append("load average >= 8")
    if sample["rss_bytes"] >= 1_000_000_000:
        errors.append("peak RSS >= 1 GB")
    if errors:
        return sample, errors
    try:
        import psutil
        memory = psutil.virtual_memory()
        sample["memory"] = {
            "available_fraction": memory.available / memory.total,
            "free_fraction": memory.free / memory.total,
        }
        if min(sample["memory"].values()) < 0.30:
            errors.append("available or free memory < 30%")
    except ImportError:
        errors.append("psutil unavailable; memory guard cannot be verified")
    return sample, errors


def diagnostic():
    from fractions import Fraction as Q

    def subsets(mask):
        sub = mask
        while True:
            yield sub
            if sub == 0:
                break
            sub = (sub - 1) & mask

    def product_jet(left, right):
        return [sum((left[sub] * right[mask ^ sub]
                     for sub in subsets(mask)), Q(0)) for mask in range(16)]

    masses = (Q(2), Q(3))
    kernels = ((Q(1, 4), Q(3, 4)), (Q(2, 3), Q(1, 3)))
    exponentials = []
    for point in range(2):
        entries = []
        for mask in range(16):
            coefficient = Q(1)
            for label in range(4):
                if mask & (1 << label):
                    coefficient *= -Q((label + 1) * (point + 1), 5)
            entries.append(coefficient)
        exponentials.append(entries)
    mass = [sum(masses[x] * exponentials[x][mask] for x in range(2))
            for mask in range(16)]
    direct = [sum(masses[x] * exponentials[x][mask] * kernels[x][1]
                  for x in range(2)) for mask in range(16)]
    inverse = [Q(0)] * 16
    inverse[0] = 1 / mass[0]
    for mask in range(1, 16):
        inverse[mask] = -sum(mass[sub] * inverse[mask ^ sub]
                             for sub in subsets(mask) if sub) / mass[0]
    normalized = [Q(0)] * 16
    for point in range(2):
        probability = product_jet(
            [masses[point] * value for value in exponentials[point]], inverse
        )
        for mask in range(16):
            normalized[mask] += probability[mask] * kernels[point][1]
    rebuilt = product_jet(mass, normalized)
    mutation = [mass[0] * coefficient for coefficient in normalized]
    equal = all(a == b for a, b in zip(direct, rebuilt))
    differing = [mask for mask in range(1, 16) if mutation[mask] != direct[mask]]
    return {
        "name": "four original labels and endpoint mass",
        "status": "PASS" if equal and differing else "FAIL",
        "equal_subset_count": sum(a == b for a, b in zip(direct, rebuilt)),
        "frozen_mass_mutation_differing_masks": differing,
        "direct": [str(x) for x in direct],
        "rebuilt": [str(x) for x in rebuilt],
        "frozen_mass_mutation": [str(x) for x in mutation],
        "scope": "finite rational bookkeeping only; no gauge-model estimate",
    }


receipt = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "NOT RUN",
    "checks": [],
    "criteria_sha256": hashlib.sha256(
        (HERE / "matcha_criteria.md").read_bytes()).hexdigest(),
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
lock = None
try:
    lock = (HERE / "matcha_numeric.lock").open("a+")
    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    sample, errors = guard()
    receipt["preflight"] = sample
    if errors:
        receipt["reason"] = errors
    else:
        receipt["checks"] = [diagnostic()]
        after, errors = guard()
        receipt["postflight"] = after
        receipt["status"] = "FAIL" if errors or any(
            item["status"] != "PASS" for item in receipt["checks"]) else "PASS"
        if errors:
            receipt["reason"] = errors
except Exception as exc:
    receipt["reason"] = [type(exc).__name__ + ": " + str(exc)]
finally:
    if lock is not None:
        lock.close()
    rendered = json.dumps(receipt, indent=2)
    (HERE / "matcha_result.json").write_text(rendered + "\n")
    print(rendered)
sys.exit(0 if receipt["status"] == "PASS" else 2)
