#!/usr/bin/env python3
"""Prospective MIXGFF rational controls. Execution is NOT claimed.

Run only by the guarded command in mixgff_guard_status.txt. No third-party
packages, pools, sampling, quadrature, or continuum/YM numerical claims.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
from pathlib import Path
import datetime
import fcntl
import hashlib
import json
import os
import re
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
THREADS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
LIMIT = 800 * 1024 ** 2
RECORDS = []


def record(name, passed, evidence):
    RECORDS.append({"name": name, "passed": bool(passed), "evidence": evidence})


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def guard(start):
    require(time.monotonic() - start < 60, "60 second time guard")
    require(os.getpriority(os.PRIO_PROCESS, 0) >= 10, "nice guard")
    require(all(os.environ.get(k) == "1" for k in THREADS), "thread guard")
    native = subprocess.check_output(["/usr/bin/memory_pressure", "-Q"], text=True)
    match = re.search(r"free percentage:\s*(\d+)%", native)
    require(match is not None, "native memory diagnostic unavailable")
    free = int(match.group(1))
    load = os.getloadavg()[0]
    scale = 1 if sys.platform == "darwin" else 1024
    # One sequential diagnostic child at a time; this conservative sum uses
    # both self and completed-child peaks rather than only final live RSS.
    rss = scale * (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                   + resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    require(load < 8 and free >= 30 and rss < LIMIT, "load/memory guard")
    return {"load1": load, "free_percent": free,
            "combined_peak_bound_bytes": rss,
            "nice": os.getpriority(os.PRIO_PROCESS, 0)}


def partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for partition in partitions(rest):
        yield [[first]] + partition
        for j in range(len(partition)):
            yield partition[:j] + [[first] + partition[j]] + partition[j + 1:]


def gaussian_moment(items, mu, cov):
    if not items:
        return Q(1)
    i, *rest = items
    total = mu[i] * gaussian_moment(rest, mu, cov)
    for k, j in enumerate(rest):
        total += cov[i][j] * gaussian_moment(rest[:k] + rest[k + 1:], mu, cov)
    return total


def mixture_cumulant(components):
    total = Q(0)
    for partition in partitions(list(range(4))):
        value = Q((-1) ** (len(partition) - 1) * factorial(len(partition) - 1))
        for block in partition:
            value *= sum(w * gaussian_moment(block, mu, cov)
                         for w, mu, cov in components)
        total += value
    return total


def mixture_checks():
    vectors = ((1, 2, 3, 4), (4, 1, 2, 3))
    covs = [[[Q(int(i == j) + v[i] * v[j]) for j in range(4)]
             for i in range(4)] for v in vectors]
    weights = (Q(1, 3), Q(2, 3))
    for means in ((0, 0, 0, 0), (1, 2, 3, 4)):
        mu = list(map(Q, means))
        components = [(w, mu, c) for w, c in zip(weights, covs)]
        direct = mixture_cumulant(components)
        expected = Q(0)
        for i, j, k, ell in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)):
            expected += (sum(w * c[i][j] * c[k][ell] for w, c in zip(weights, covs))
                         - sum(w * c[i][j] for w, c in zip(weights, covs))
                         * sum(w * c[k][ell] for w, c in zip(weights, covs)))
        record("mixture_partition_identity_" + str(means), direct == expected,
               {"partition": str(direct), "covariance_sum": str(expected)})
    ones = [[Q(1)] * 4 for _ in range(4)]
    shifted = mixture_cumulant([(Q(1, 2), [Q(1)] * 4, ones),
                                (Q(1, 2), [Q(-1)] * 4, ones)])
    scaled = mixture_cumulant([(Q(1, 2), [Q(0)] * 4, [[Q(v)] * 4 for _ in range(4)])
                               for v in (0, 2)])
    record("random_shift_minus_two", shifted == -2, str(shifted))
    record("variance_mixture_three", scaled == 3, str(scaled))


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


PAIRS = list(combinations(range(4), 2))
CYCLES = ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3))


def curvature_by_minors(z):
    s = sum(v * v for v in z)
    h = [[Q(int(i == j)) - 2 * z[i] * z[j] / s for j in range(4)] for i in range(4)]
    jmat = [[h[a][c] * h[b][d] - h[a][d] * h[b][c]
             for c, d in PAIRS] for a, b in PAIRS]
    return s, jmat, [[v / s ** 2 for v in row] for row in jmat]


def curvature_by_hessian(z):
    s = sum(v * v for v in z)
    d2 = [[-Q(int(i == j), 2) / s ** 2 + 2 * z[i] * z[j] / s ** 3
           for j in range(4)] for i in range(4)]
    return [[-int(b == d) * d2[a][c] + int(b == c) * d2[a][d]
             + int(a == d) * d2[b][c] - int(a == c) * d2[b][d]
             for c, d in PAIRS] for a, b in PAIRS]


def geometry_data(points, name):
    matrices, lengths = {}, {}
    agree = True
    for i, j in combinations(range(4), 2):
        z = [Q(points[i][k] - points[j][k]) for k in range(4)]
        s, jmat, g = curvature_by_minors(z)
        agree = agree and g == curvature_by_hessian(z)
        matrices[i, j] = matrices[j, i] = jmat
        lengths[i, j] = lengths[j, i] = s
    record("hessian_versus_minors_" + name, agree, "all six distinct edges")
    traces, weights = [], []
    for cycle in CYCLES:
        product = eye(6)
        weight = Q(1)
        for i, j in zip(cycle, cycle[1:] + cycle[:1]):
            product = mm(product, matrices[i, j])
            weight /= lengths[i, j] ** 2
        traces.append(trace(product))
        weights.append(weight)
    return traces, weights


def geometry_checks():
    geom_a = ((0, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), (3, 0, 0, 0))
    geom_b = ((0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (2, 1, 0, 0))
    ta, wa = geometry_data(geom_a, "A")
    tb, wb = geometry_data(geom_b, "B")
    record("collinear_traces", ta == [6, 6, 6], list(map(str, ta)))
    record("noncollinear_traces", tb == [Q(26, 5), Q(2), Q(22, 5)], list(map(str, tb)))
    record("noncollinear_weights", wb == [Q(1, 1600), Q(1, 64), Q(1, 400)],
           list(map(str, wb)))
    average_a = sum(t * w for t, w in zip(ta, wa)) / sum(wa)
    average_b = sum(t * w for t, w in zip(tb, wb)) / sum(wb)
    record("weighted_B_trace", average_b == Q(182, 75), str(average_b))
    gap = (average_a - average_b) / 9
    record("free_ratio_gap", gap == Q(268, 675) and gap > 0, str(gap))
    identity_mutation = [Q(6)] * 3
    # Mutate the connected numerator only; the denominator is fixed by C2.
    drop_cycle_average = sum(t * w for t, w in zip(tb[:2], wb[:2])) / sum(wb)
    record("detect_identity_numerator", identity_mutation != tb,
           "identity removes the angular trace variation")
    record("detect_dropped_cycle", drop_cycle_average != average_b,
           {"mutant": str(drop_cycle_average), "complete": str(average_b)})


def pairings(legs):
    if not legs:
        yield []
        return
    first, *rest = legs
    for k, other in enumerate(rest):
        for tail in pairings(rest[:k] + rest[k + 1:]):
            yield [(first, other)] + tail


def connected_graph_classes(n):
    graphs = Counter()
    for pairing in pairings(list(range(2 * n))):
        edges = [tuple(sorted((a // 2, b // 2))) for a, b in pairing]
        if any(a == b for a, b in edges):
            continue
        reached = {0}
        for _ in range(n):
            for a, b in edges:
                if a in reached or b in reached:
                    reached.update((a, b))
        if len(reached) == n:
            graphs[tuple(sorted(edges))] += 1
    return graphs


def pairing_checks():
    g3, g4 = connected_graph_classes(3), connected_graph_classes(4)
    record("connected_pairings_n3", sum(g3.values()) == 8, sum(g3.values()))
    record("connected_pairings_n4", sum(g4.values()) == 48, sum(g4.values()))
    record("three_cycles_multiplicity_16", len(g4) == 3 and set(g4.values()) == {16},
           sorted(g4.values()))
    record("detect_factor_8", all(v != 8 for v in g4.values()) and bool(g4),
           sorted(g4.values()))
    a, power = [[Q(1), Q(0)], [Q(0), Q(-1)]], eye(2)
    powers = {}
    for k in range(1, 9):
        power = mm(power, a)
        powers[k] = trace(power)
    record("balanced_quadratic_powers", all(v == (0 if k % 2 else 2)
                                           for k, v in powers.items()),
           {k: str(v) for k, v in powers.items()})
    ratio = 4 * powers[4] / powers[2] ** 2
    record("quadratic_ratio_two", ratio == 2, str(ratio))


def main():
    receipt_path, result_path = HERE / "mixgff_run.json", HERE / "mixgff_results.json"
    require(not receipt_path.exists() and not result_path.exists(),
            "Existing run evidence must be preserved; no implicit overwrite")
    receipt = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "status": "BLOCKED", "checks_executed": False, "guards": [],
               "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "criteria_sha256": hashlib.sha256((HERE / "mixgff_criteria.md").read_bytes()).hexdigest()}
    start = time.monotonic()
    try:
        # Check niceness before even starting a diagnostic subprocess.
        require(os.getpriority(os.PRIO_PROCESS, 0) >= 10, "nice guard unavailable")
        require(all(os.environ.get(k) == "1" for k in THREADS), "thread guard")
        resource.setrlimit(resource.RLIMIT_AS, (LIMIT, LIMIT))
        resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
        with (HERE / "mixgff_numeric.lock").open("a+") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            receipt["lock"] = str(lock.name)
            receipt["guards"].append(guard(start))
            receipt["checks_executed"] = True
            for group in (mixture_checks, geometry_checks, pairing_checks):
                group()
                receipt["guards"].append(guard(start))
            receipt["status"] = "PASS" if all(r["passed"] for r in RECORDS) else "FAIL"
            result = {"scope": "finite algebra only; no YM estimates", "records": RECORDS}
            with result_path.open("x") as out:
                json.dump(result, out, indent=2)
                out.write("\n")
    except Exception as exc:
        receipt["failure"] = repr(exc)
        receipt["status"] = "INCOMPLETE" if receipt["checks_executed"] else "BLOCKED"
        receipt["partial_records"] = RECORDS
    receipt["elapsed_seconds"] = time.monotonic() - start
    with receipt_path.open("x") as out:
        json.dump(receipt, out, indent=2)
        out.write("\n")
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
