#!/usr/bin/env python3
"""Finite author checks of GH, not a Wilson-law calculation."""
from fractions import Fraction as F
from itertools import product
from math import log
import json
import os
import resource
import signal
import sys

LIMIT = 2 * 1024**3
address_space_cap = "2 GiB"
try:
    resource.setrlimit(resource.RLIMIT_AS, (LIMIT, LIMIT))
except (ValueError, OSError) as error:
    address_space_cap = "unavailable: " + str(error)


def check_rss():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else 1024 * peak
    if peak_bytes > LIMIT:
        raise SystemExit("RSS exceeded 2 GiB")
    return peak_bytes


signal.signal(signal.SIGALRM, lambda *_: check_rss())
signal.setitimer(signal.ITIMER_REAL, 0.01, 0.01)
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    assert os.environ.get(name) == "1", name
check_rss()

# P_i[parent state][child state], deliberately not deterministic.
P = [
    [[F(3, 4), F(1, 4)], [F(1, 5), F(4, 5)]],
    [[F(2, 3), F(1, 3)], [F(3, 7), F(4, 7)]],
    [[F(5, 8), F(3, 8)], [F(1, 6), F(5, 6)]],
]
t = [F(2), F(-3, 2), F(5, 3)]
S = [None, [F(1, 4), F(-1, 3)], [F(-2, 5), F(3, 8)],
     [F(1, 7), F(-3, 11)]]
bad = [None, [False, True], [True, False], [False, True]]
nu = [F(2, 5), F(3, 5)]
values = [[F(-2), F(3)]]
b = [None]
envelope = [list(map(abs, values[0]))]
for j in range(3):
    values.append([S[j+1][w] + t[j] * sum(P[j][w][v] * values[j][v]
                   for v in range(2)) for w in range(2)])
    b.append(max(abs(values[j+1][w]) for w in range(2) if not bad[j+1][w]))
    envelope.append([b[j+1] if not bad[j+1][w] else abs(S[j+1][w]) +
                     abs(t[j]) * sum(P[j][w][v] * envelope[j][v]
                                     for v in range(2)) for w in range(2)])
    assert all(abs(values[j+1][w]) <= envelope[j+1][w] for w in range(2))

trajectories = []
for states in product(range(2), repeat=4):
    weight = nu[states[3]]
    for j in range(3):
        weight *= P[j][states[j+1]][states[j]]
    trajectories.append((states, weight))
assert sum(weight for _, weight in trajectories) == 1

term_vectors = []
term_q_integrals = []
for i, kind in [(0, "bottom")] + [(i, kind) for i in range(1, 4)
                                  for kind in ("good", "source")]:
    c = F(1)
    for j in range(i, 3):
        c *= abs(t[j])
    term = [F(0), F(0)]
    q_integrals = {q: [F(0), F(0)] for q in (2, 4)}
    for states, weight in trajectories:
        check_rss()
        if not all(bad[l][states[l]] for l in range(i+1, 4)):
            continue
        if kind == "bottom":
            payload = abs(values[0][states[0]])
        elif kind == "good":
            if bad[i][states[i]]:
                continue
            payload = b[i]
        else:
            if not bad[i][states[i]]:
                continue
            payload = abs(S[i][states[i]])
        w = states[3]
        term[w] += c * payload * weight / nu[w]
        for q in (2, 4):
            q_integrals[q][w] += (c * payload)**q * weight
    term_vectors.append(term)
    term_q_integrals.append(q_integrals)

assert all(sum(term[w] for term in term_vectors) == envelope[3][w]
           for w in range(2))
checks = 0
for event in ([True, False], [False, True], [True, True]):
    for term, integrals in zip(term_vectors, term_q_integrals):
        for q in (2, 4):
            lhs = sum(nu[w] * term[w]**q for w in range(2) if event[w])
            rhs = sum(integrals[q][w] for w in range(2) if event[w])
            assert lhs <= rhs
            checks += 1

p = F(1, 2**80)
branching = 16
fourth_moments = [p * branching**(4*j) for j in range(4)]
ratios = [fourth_moments[j+1]/fourth_moments[j] for j in range(3)]
assert ratios == [F(branching**4)] * 3

radius = []
for d in (0, 1000):
    log_R = 2 * (log(1000) + d * log(5/4))
    log_exp_lambda_over_5 = (100 + d/100) / 5
    radius.append({"depth": d, "log_R": log_R,
                   "lambda_over_5": log_exp_lambda_over_5,
                   "R_exceeds_unfloored_M": log_R > log_exp_lambda_over_5})
assert not radius[0]["R_exceeds_unfloored_M"]
assert radius[1]["R_exceeds_unfloored_M"]

print(json.dumps({
    "scope": "finite author diagnostics; not a proof of the Wilson estimates",
    "history_expansion_exact": True,
    "pointwise_domination_exact": True,
    "individual_term_jensen_checks_exact": checks,
    "top_generated_values": list(map(str, values[3])),
    "top_positive_envelope": list(map(str, envelope[3])),
    "copy_fourth_moment_ratios": list(map(str, ratios)),
    "copy_norm_ratio": branching,
    "radius_diagnostics": radius,
    "address_space_cap": address_space_cap,
    "rss_limit_bytes": LIMIT,
    "rss_limit_enforcement": "periodic signal and per-trajectory self-check",
    "peak_rss_bytes": check_rss(),
}, indent=2))
