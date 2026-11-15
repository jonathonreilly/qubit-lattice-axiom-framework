#!/usr/bin/env python3
"""Guarded finite controls for HOLEPAY; no certificate of actual E15."""
from pathlib import Path
from fractions import Fraction
from itertools import product
from collections import defaultdict
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
REPORT = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "NOT RUN", "math_started": False, "checks": [], "resources": [],
    "criteria_sha256": hashlib.sha256((HERE / "holepay_criteria.md").read_bytes()).hexdigest(),
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "note_sha256": hashlib.sha256((HERE.parent / "HOLEPAY.md").read_bytes()).hexdigest(),
    "scope": "Finite regressions only; no actual history-uniform E15 check",
}


class Refusal(Exception):
    pass


def guard(label):
    names = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLAS_NUM_THREADS")
    row = {"label": label, "load": list(os.getloadavg()),
           "nice": os.getpriority(os.PRIO_PROCESS, 0),
           "rss_raw": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           "threads": {key: os.environ.get(key) for key in names}}
    REPORT["resources"].append(row)
    if sys.platform != "darwin":
        raise Refusal("Free-memory and RSS conventions verified only for macOS")
    row["rss_bytes"] = row["rss_raw"]
    mem = subprocess.run(["/usr/bin/memory_pressure", "-Q"],
                         capture_output=True, text=True, timeout=5)
    match = re.search(r"System-wide memory free percentage:\s*(\d+)%", mem.stdout)
    if mem.returncode != 0 or match is None:
        row["memory_probe"] = mem.stdout + mem.stderr
        raise Refusal("Cannot verify available memory")
    row["free_percent"] = int(match.group(1))
    if row["nice"] < 10:
        raise Refusal("Required nice priority unavailable; no unguarded fallback")
    if any(value != "1" for value in row["threads"].values()):
        raise Refusal("Single-thread settings are not all 1")
    if max(row["load"]) >= 8 or row["free_percent"] < 30 or row["rss_bytes"] >= 1_000_000_000:
        raise Refusal("Load, free-memory or RSS gate not met")


def check(name, ok, evidence):
    REPORT["checks"].append({"name": name, "status": "PASS" if ok else "FAIL", "evidence": evidence})


def components(vertices, adj):
    left, answer = set(vertices), []
    while left:
        todo = [min(left)]
        left.remove(todo[0])
        part = set(todo)
        while todo:
            point = todo.pop()
            new = (adj[point] & left)
            left -= new
            part |= new
            todo.extend(new)
        answer.append(frozenset(part))
    return answer


def subsets(n):
    return [frozenset(i for i in range(n) if bits & (1 << i)) for bits in range(1 << n)]


def saturation(x, active, adj):
    result = set(x)
    for hole in components(set(adj) - active, adj):
        if hole & x or any(adj[v] & x for v in hole):
            result |= hole
    return frozenset(result)


def growth(x, active, adj):
    result = set(x)
    while True:
        enlarged = result | {v for v in set(adj) - active if adj[v] & result}
        if enlarged == result:
            return frozenset(result)
        result = enlarged


def hole_size(x, active, adj):
    return sum(len(hole) for hole in components(set(adj) - active, adj)
               if hole & x or any(adj[v] & x for v in hole))


def root_sums(family, roots):
    return {v: sum((2 ** len(x)) * coefficient for x, coefficient in family.items() if v in x)
            for v in roots}


def full_norm(family, roots):
    return max(root_sums(family, roots).values(), default=0)


def fixed_graph_checks():
    nested_count = bound_count = 0
    all_ok = bounds_ok = True
    for cycle in (False, True):
        adj = {i: {j for j in range(6) if abs(i-j) == 1 or (cycle and abs(i-j) == 5)}
               for i in range(6)}
        sets = subsets(6)
        connected = [x for x in sets if x and len(components(x, adj)) == 1]
        for omega in sets:
            for active in sets:
                if not active <= omega:
                    continue
                for x in connected:
                    if not x & active:
                        continue
                    direct = saturation(x, active, adj)
                    composed = saturation(saturation(x, omega, adj), active, adj)
                    all_ok &= (direct == composed == growth(x, active, adj))
                    all_ok &= (direct & active == x & active)
                    nested_count += 1
            guard("nested graph masks")
        for active in sets:
            inputs = {x: Fraction(1) for x in connected if x & active}
            outputs = defaultdict(Fraction)
            for x in inputs:
                outputs[saturation(x, active, adj)] += Fraction(1, 4 ** hole_size(x, active, adj))
            bounds_ok &= full_norm(outputs, adj) <= 4 * full_norm(inputs, adj)
            bound_count += 1
    check("Nested saturation and growth identity", all_ok, {"instances": nested_count})
    check("Full-root weighted bound at exp(mu)=2, exp(tau)=4", bounds_ok, {"masks": bound_count})
    adj = {0: {1}, 1: {0, 2}, 2: {1}}
    active = frozenset({0, 2})
    inputs = {frozenset({0}): Fraction(1), frozenset({2}): Fraction(1)}
    outputs = defaultdict(Fraction)
    for x in inputs:
        outputs[saturation(x, active, adj)] += Fraction(1, 4 ** hole_size(x, active, adj))
    sums = root_sums(outputs, adj)
    correct = full_norm(outputs, adj)
    mutant = full_norm(outputs, active)
    check("Inactive-root witness", full_norm(inputs, adj) == 2 and list(sums.values()) == [1, 2, 1],
          {"input": str(full_norm(inputs, adj)), "output_roots": {str(k): str(v) for k, v in sums.items()}})
    check("Inactive-roots-omitted mutation rejected", correct == 2 and mutant != 2,
          {"baseline": str(correct), "mutation": str(mutant), "independent_expected_full_norm": "2"})


def collar(points, radius):
    offsets = tuple(product(range(-radius, radius + 1), repeat=4))
    return {tuple(v[i]+off[i] for i in range(4)) for v in points for off in offsets}


def project(points):
    return {tuple(coordinate // 3 for coordinate in point) for point in points}


def face_neighbours(point):
    return {tuple(value + (sign if i == axis else 0) for i, value in enumerate(point))
            for axis in range(4) for sign in (-1, 1)}


def geometry_checks():
    births = {0: {(0, 0, 0, 0), (12, 0, 0, 0)}, 1: {(1, 0, 0, 0)}}
    mask, cohorts, recorded = set(), [], []
    ok = True
    for step in range(5):
        new = births.get(step, set())
        mask = collar(project(mask | new), 1)
        cohorts = [(birth, seed, collar(project(current), 1)) for birth, seed, current in cohorts]
        cohorts += [(step, seed, collar(project({seed}), 1)) for seed in sorted(new)]
        union = set().union(*(item[2] for item in cohorts))
        cover = set()
        for birth, seed, current in cohorts:
            projected = {seed}
            for _ in range(step + 1 - birth):
                projected = project(projected)
            cover |= collar(projected, 2)
        adj = {v: face_neighbours(v) & mask for v in mask}
        count = len(components(mask, adj))
        ok &= mask == union and mask <= cover and len(mask) <= 625 * len(cohorts)
        recorded.append({"level": step+1, "vertices": len(mask), "births": len(cohorts), "components": count})
        guard("four-dimensional cohort geometry")
    ok &= recorded[0]["components"] == 2 and any(row["components"] == 1 for row in recorded[1:])
    check("Birth cover and merger", ok, recorded)


def set_partitions(items):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for parts in set_partitions(rest):
        yield ((first,),) + parts
        for i in range(len(parts)):
            yield parts[:i] + ((first,) + parts[i],) + parts[i+1:]


def algebra_checks():
    polynomial = [1]
    recorded = []
    ok = True
    for order in range(7):
        independent = [0] * (order+1)
        for partition in set_partitions(tuple(range(order))):
            independent[len(partition)] += 1
        ok &= polynomial == independent
        recorded.append(polynomial)
        # M_(r+1)(z) = z M_r(z) + z M'_r(z).
        next_polynomial = [0] * (len(polynomial)+1)
        for degree, coefficient in enumerate(polynomial):
            next_polynomial[degree+1] += coefficient
            next_polynomial[degree] += degree * coefficient
        polynomial = next_polynomial
    check("Exponential derivative partitions through order six", ok, recorded)
    cube = set(product(range(1, 4), repeat=4))
    boundary = set().union(*(face_neighbours(point) for point in cube)) - cube
    check("Cube boundary count", len(cube) == 81 and len(boundary) == 216,
          {"volume": len(cube), "external_face_boundary": len(boundary)})
    exponent = 10**4 - 8 * 10**3
    check("Boundary-only finite exponent witness", exponent == 2000 and exponent > 0,
          {"side": 10, "mu": 1, "b": 1, "log_norm_ratio": exponent})


def main():
    exit_code = 2
    try:
        with (HERE / "holepay_numeric.lock").open("a+") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            guard("pre-mathematics")
            REPORT["math_started"] = True
            fixed_graph_checks()
            guard("after fixed graphs")
            geometry_checks()
            guard("before algebra")
            algebra_checks()
            guard("completion")
            failed = sum(row["status"] == "FAIL" for row in REPORT["checks"])
            REPORT["status"] = "FAIL" if failed else "PASS"
            exit_code = 1 if failed else 0
    except (Refusal, BlockingIOError) as exc:
        REPORT["reason"] = str(exc)
        REPORT["status"] = "INCOMPLETE" if REPORT["math_started"] else "NOT RUN"
    except Exception as exc:
        REPORT["status"] = "ERROR"
        REPORT["reason"] = f"{type(exc).__name__}: {exc}"
        exit_code = 1
    finally:
        (HERE / "holepay_result.json").write_text(json.dumps(REPORT, indent=2) + "\n")
        print(json.dumps(REPORT, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
