"""Finite exact probability checks; criteria: n5b_criteria.md.

No Yang--Mills simulation or analytic estimate is performed.
Constructive-method attribution in the associated note: Balaban and Dimock.
"""

from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import os
import re
import resource
import subprocess
import sys
import time

START = time.monotonic()
LIMIT = 1_000_000_000
FAILURES = []
THREADS = (
    "BLAS", "BLAS_NUM_THREADS", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS",
)


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    if rss >= LIMIT or time.monotonic() - START >= 60:
        raise RuntimeError("Resource limit reached; computation stopped")
    return rss


def record(label, passed, detail=""):
    guard()
    print(label, "PASS" if passed else "FAIL", detail, flush=True)
    if not passed:
        FAILURES.append(label)


def mean(law, f):
    return sum((p * f(x) for x, p in law), Q(0))


def covariance(law, f, g):
    return mean(law, lambda x: f(x) * g(x)) - mean(law, f) * mean(law, g)


def conditional_image(law, f, coordinate):
    masses, sums = {}, {}
    for x, p in law:
        u = x[coordinate]
        masses[u] = masses.get(u, Q(0)) + p
        sums[u] = sums.get(u, Q(0)) + p * f(x)
    return {u: sums[u] / mass for u, mass in masses.items()}


def conditional_covariances(law, f, g, coordinate):
    """Compute from separately normalized conditional laws, not telescoping."""
    groups = {}
    for x, p in law:
        groups.setdefault(x[coordinate], []).append((x, p))
    out = {}
    for u, group in groups.items():
        mass = sum((p for _, p in group), Q(0))
        normalized = [(x, p / mass) for x, p in group]
        out[u] = covariance(normalized, f, g)
    return out


def tests():
    initial = [Q(1, 2), Q(1, 3), Q(1, 6)]
    transitions = [
        [[Q(x, 8) for x in row] for row in [(5, 2, 1), (1, 5, 2), (2, 1, 5)]],
        [[Q(x, 6) for x in row] for row in [(3, 1, 2), (2, 3, 1), (1, 2, 3)]],
        [[Q(x, 8) for x in row] for row in [(4, 3, 1), (1, 4, 3), (3, 1, 4)]],
    ]
    law = []
    for x in product(range(3), repeat=4):
        p = initial[x[0]]
        for i, kernel in enumerate(transitions):
            p *= kernel[x[i]][x[i + 1]]
        law.append((x, p))
    record("C1-positive-normalized-chain", all(p > 0 for _, p in law)
           and sum(p for _, p in law) == 1
           and all(sum(row) == 1 for kernel in transitions for row in kernel))
    f = lambda x: Q([-2, 1, 4][x[0]])
    s = lambda x: Q([3, -1, 2][x[0]])
    fi = [conditional_image(law, f, i) for i in range(4)]
    si = [conditional_image(law, s, i) for i in range(4)]
    total = covariance(law, f, s)
    increments = []
    for i in range(3):
        f_i = lambda x, i=i: fi[i][x[i]]
        s_i = lambda x, i=i: si[i][x[i]]
        cc = conditional_covariances(law, f_i, s_i, i + 1)
        increments.append(mean(law, lambda x, i=i, cc=cc: cc[x[i + 1]]))
        record(f"C1-tower-{i}",
               conditional_image(law, f_i, i + 1) == fi[i + 1]
               and conditional_image(law, s_i, i + 1) == si[i + 1])
    nonzero = False
    omitted_detected = False
    for k in (1, 2, 3):
        f_k = lambda x, k=k: fi[k][x[k]]
        s_k = lambda x, k=k: si[k][x[k]]
        terminal = covariance(law, f_k, s_k)
        prefix = sum(increments[:k], Q(0))
        record(f"C1-cut-{k}", total == prefix + terminal,
               f"total={total}; terminal={terminal}")
        radius = (max(si[k].values()) - min(si[k].values())) / 2
        variance = covariance(law, f_k, f_k)
        record(f"C1-bound-{k}", terminal ** 2 <= variance * radius ** 2)
        nonzero |= terminal != 0
        omitted_detected |= terminal != 0 and total != prefix
    record("C1-nonzero-terminal", nonzero)
    record("X1-omitted-terminal-detected", omitted_detected)

    non_markov = [((x, y, x), Q(1, 4)) for x, y in product((-1, 1), repeat=2)]
    f0 = lambda x: Q(x[0])
    at1 = conditional_image(non_markov, f0, 1)
    direct = conditional_image(non_markov, f0, 2)
    through1 = conditional_image(non_markov, lambda x: at1[x[1]], 2)
    record("X2-non-Markov-tower-detected", direct != through1,
           f"direct={direct}; through_U1={through1}")

    signs = [(x, Q(1, 8)) for x in product((-1, 1), repeat=3)]
    f2 = lambda x: Q(x[0] + x[1])
    s2 = lambda x: Q(x[0]) + Q(x[2], 3)
    cc = conditional_covariances(signs, f2, s2, 0)
    total2 = covariance(signs, f2, s2)
    record("C2-zero-conditional", all(v == 0 for v in cc.values()))
    record("C2-unit-total", total2 == 1, f"covariance={total2}")
    s_at_x = conditional_image(signs, s2, 0)
    fake_radius = max(abs(value - value) for value in s_at_x.values())
    record("X3-field-dependent-center-detected", fake_radius == 0 and total2 != 0)

    for n in (2, 4, 8, 16, 32):
        probability = Q(1, n * n)
        bernoulli = [((0,), 1 - probability), ((1,), probability)]
        f3 = lambda x, n=n: Q(n * x[0])
        bad = lambda x, n=n: Q(n * x[0])
        good = lambda x: Q(x[0])
        cov_bad = covariance(bernoulli, f3, bad)
        cov_good = covariance(bernoulli, f3, good)
        variance = covariance(bernoulli, f3, f3)
        budget_bad = mean(bernoulli, lambda x: bad(x) ** 2 * x[0])
        budget_good = mean(bernoulli, lambda x: good(x) ** 2 * x[0])
        record(f"C3-amplitude-{n}", cov_bad == 1 - probability
               and cov_bad >= Q(3, 4) and cov_good == (1 - probability) / n
               and cov_good <= Q(1, n),
               f"P_bad={probability}; cov_bad={cov_bad}; cov_good={cov_good}")
        record(f"C3-tail-bound-{n}", cov_bad ** 2 <= variance * budget_bad
               and cov_good ** 2 <= variance * budget_good)


def main():
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    print("priority=", priority, flush=True)
    if priority < 10:
        print("NOT RUN: required nice priority was not established", flush=True)
        return 2
    if any(os.environ.get(name) != "1" for name in THREADS):
        print("NOT RUN: missing single-thread environment", flush=True)
        return 2
    if sys.platform != "darwin":
        print("NOT RUN: preregistered memory_pressure guard requires Darwin", flush=True)
        return 2
    load = os.getloadavg()[0]
    pressure = subprocess.run(["/usr/bin/memory_pressure"], check=True,
                              text=True, capture_output=True, timeout=10).stdout
    match = re.search(r"System-wide memory free percentage:\s*(\d+)%", pressure)
    free = int(match.group(1)) if match else None
    print(f"load1={load}; memory_free_percent={free}", flush=True)
    if load >= 8 or free is None or free < 30:
        print("NOT RUN: resource guard failed", flush=True)
        return 2
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    # Darwin rejected attempts to set either an RSS soft or hard ceiling.
    # The preregistered resource check is measured RSS in guard(), exercised
    # before computation and at every criterion. No inherited cap is raised.
    print(f"inherited_rss_limit={resource.getrlimit(resource.RLIMIT_RSS)}; "
          f"monitored_rss_limit={LIMIT}", flush=True)
    lock = Path(__file__).with_name("n5b_numeric.lock")
    try:
        lock.mkdir()
    except FileExistsError:
        print("NOT RUN: numeric lock occupied", flush=True)
        return 2
    try:
        guard()
        tests()
        print(f"peak_rss_bytes={guard()}; elapsed_seconds={time.monotonic()-START:.6f}")
        print("VERDICT:", "FAIL" if FAILURES else "PASS", flush=True)
        return 1 if FAILURES else 0
    finally:
        lock.rmdir()


if __name__ == "__main__":
    sys.exit(main())
