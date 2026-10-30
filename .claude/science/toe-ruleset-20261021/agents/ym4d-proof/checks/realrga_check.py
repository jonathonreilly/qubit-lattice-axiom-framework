#!/usr/bin/env python3
"""Exact finite diagnostics; not a gauge estimate or an independent review."""
from fractions import Fraction as F
from itertools import product, combinations
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

HERE = Path(__file__).resolve().parent
REPORT = {"status": "NOT RUN", "checks": {}, "resources": [],
          "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "criteria_sha256": hashlib.sha256((HERE / "realrga_criteria.md").read_bytes()).hexdigest(),
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


class Refusal(Exception):
    pass


def guard(where):
    if sys.platform != "darwin":
        raise Refusal("Unverified memory gate on non-macOS host")
    cp = subprocess.run(["/usr/bin/memory_pressure", "-Q"], capture_output=True,
                        text=True, timeout=5)
    m = re.search(r"System-wide memory free percentage:\s*(\d+)%", cp.stdout)
    if cp.returncode or not m:
        raise Refusal("Cannot verify free memory: " + cp.stdout + cp.stderr)
    names = ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLAS_NUM_THREADS"]
    row = {"where": where, "rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           "load": os.getloadavg(), "free_percent": int(m.group(1)),
           "nice": os.getpriority(os.PRIO_PROCESS, 0),
           "threads": {n: os.environ.get(n) for n in names}}
    REPORT["resources"].append(row)
    if row["rss_bytes"] >= 1_000_000_000 or max(row["load"]) >= 8 or row["free_percent"] < 30:
        raise Refusal("Resource threshold not met")
    if row["nice"] < 10 or any(v != "1" for v in row["threads"].values()):
        raise Refusal("Niceness or thread guard not satisfied")


def add(a, b):
    return {m: a.get(m, F(0)) + b.get(m, F(0)) for m in set(a) | set(b)}


def scale(a, x):
    return {m: v*x for m, v in a.items()}


def mul(a, b):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            if not m & n:
                out[m | n] = out.get(m | n, F(0)) + x*y
    return out


def logjet(a):
    assert a.get(0) == 1
    v = add(a, {0: F(-1)})
    out, power = {}, {0: F(1)}
    for n in range(1, 5):
        power = mul(power, v)
        out = add(out, scale(power, F((-1)**(n+1), n)))
    return out


def expjet(a):
    assert a.get(0, 0) == 0
    out, power = {0: F(1)}, {0: F(1)}
    for n in range(1, 5):
        power = mul(power, a)
        out = add(out, scale(power, F(1, factorial(n))))
    return out


def mgf(p):
    return {m: (F(1) if m == 0 else p) for m in range(16)}


def require(ok, name, details=None):
    REPORT["checks"][name] = {"pass": bool(ok), "details": details}
    if not ok:
        raise AssertionError(name)


def checks():
    p = F(1, 3)
    expected = [0, p, p*(1-p), p*(1-p)*(1-2*p), p*(1-p)*(1-6*p*(1-p))]
    jets = logjet(mgf(p))
    require(all(jets[m] == expected[m.bit_count()] for m in range(1, 16)),
            "all_15_Bernoulli_jets", {str(i): str(expected[i]) for i in range(1, 5)})
    require(p != p*(1-p) == F(2, 9), "normalization_omission_detected")
    guard("after normalization")
    conditional = [logjet(mgf(F(1, 4))), logjet(mgf(F(3, 4)))]
    assembled = logjet(scale(add(*(expjet(j) for j in conditional)), F(1, 2)))
    direct = logjet(mgf(F(1, 2)))
    require(all(assembled[m] == direct[m] for m in range(1, 16)) and direct[15] == F(-1, 8),
            "conditional_outer_all_15_jets", {"fourth": str(direct[15])})
    dropped = [{m: v for m, v in j.items() if m.bit_count() != 3} for j in conditional]
    wrong = logjet(scale(add(*(expjet(j) for j in dropped)), F(1, 2)))
    require(wrong[15] != direct[15], "omitted_triples_detected", {"mutant_fourth": str(wrong[15])})
    guard("before Mayer")
    weights = [F(1, 8), F(-1, 9), F(1, 10)]
    # Direct polynomial-log coefficients, from multiplication of ordinary powers.
    zminus1 = {1: sum(weights), 2: F(1, 80)}
    power, directlog = {0: F(1)}, {}
    for k in range(1, 5):
        tmp = {}
        for i, a in power.items():
            for j, b in zminus1.items():
                if i+j <= 4:
                    tmp[i+j] = tmp.get(i+j, F(0)) + a*b
        power = tmp
        for n, value in power.items():
            directlog[n] = directlog.get(n, F(0)) + F((-1)**(k+1), k)*value
    graphlog, no_repeats = {}, {}
    for n in range(1, 5):
        total, wrong_total = F(0), F(0)
        for labels in product(range(3), repeat=n):
            edges = [(i, j) for i, j in combinations(range(n), 2)
                     if labels[i] == labels[j] or abs(labels[i]-labels[j]) == 1]
            coefficient = 0
            for mask in range(1 << len(edges)):
                chosen = [e for i, e in enumerate(edges) if mask >> i & 1]
                reached = {0}
                for _ in range(n):
                    for a, b in chosen:
                        if a in reached or b in reached:
                            reached.update((a, b))
                if len(reached) == n:
                    coefficient += (-1)**len(chosen)
            contribution = F(coefficient, factorial(n))
            for label in labels:
                contribution *= weights[label]
            total += contribution
            if len(set(labels)) == n:
                wrong_total += contribution
        graphlog[n], no_repeats[n] = total, wrong_total
        guard("Mayer order " + str(n))
    require(graphlog == directlog, "Mayer_graph_vs_direct_log",
            {str(n): str(v) for n, v in graphlog.items()})
    require(no_repeats != directlog, "omitted_repeated_labels_detected")


code = 2
try:
    with (HERE / "realrga_numeric.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as e:
            raise Refusal("Numerical lane lock occupied") from e
        guard("preflight")
        checks()
        guard("completed")
        REPORT["status"], code = "PASS", 0
except Refusal as e:
    REPORT["reason"] = str(e)
except Exception as e:
    REPORT["status"], REPORT["reason"], code = "FAIL", repr(e), 1
finally:
    output = json.dumps(REPORT, indent=2) + "\n"
    (HERE / "realrga_result.json").write_text(output)
    print(output, end="")
sys.exit(code)
