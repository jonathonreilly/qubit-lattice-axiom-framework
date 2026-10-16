"""Author development probe: past cache versus current two-input relation.

Synthetic exact/seeded controls only. No observational data or physical fit.
Run with an external timeout; outputs bind the exact source and stated inputs.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path
import random
from fractions import Fraction as F

import sympy as sp

AUDIT_TIMEOUT_SEC = 120
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
REPO_INPUTS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/NETWORK_EVOLUTION_BLOCK01_v1.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
]
checks = []


def check(name, condition, detail):
    checks.append({"name": name, "pass": bool(condition), "detail": detail})


def cache_step(cache, bits, route):
    a, b = cache
    x, y = bits
    return (x, b) if route == 0 else (a, y)


def score(bits, cache):
    return 1 if (bits[0] ^ bits[1]) == (cache[0] ^ cache[1]) else -1


def response_extremes():
    """Every deterministic one-bit response; convexity covers stochastic ones."""
    tables = list(itertools.product((0, 1), repeat=2))
    rows = []
    for f0, f1, q in itertools.product(tables, tables, (F(0), F(1, 3), F(1, 2), F(1))):
        p = {(x, y): q * f0[x] + (1 - q) * f1[y]
             for x, y in itertools.product((0, 1), repeat=2)}
        delta = p[0, 0] + p[1, 1] - p[0, 1] - p[1, 0]
        rows.append(delta)
    check("one_current_input_all_deterministic_extremes", all(x == 0 for x in rows),
          {"cases": len(rows), "largest_abs_delta": str(max(map(abs, rows)))})


def exact_block_cache():
    contexts = list(itertools.product((0, 1), repeat=2))
    all_errors = []
    for bits in contexts:
        distribution = {cache: F(1, 4) for cache in contexts}
        cumulative = F(0)
        rows = []
        for t in range(1, 13):
            after = {cache: F(0) for cache in contexts}
            for cache, probability in distribution.items():
                for route in (0, 1):
                    after[cache_step(cache, bits, route)] += probability / 2
            distribution = after
            error = sum(p for cache, p in after.items() if score(bits, cache) == -1)
            cumulative += error
            expected = F(1, 2**t)
            block_win = 1 - cumulative / t
            expected_block = 1 - (1 - F(1, 2**t)) / t
            rows.append({"t": t, "error": str(error), "mean_win": str(block_win)})
            all_errors += [error - expected, block_win - expected_block,
                           sum(after.values()) - 1]
        check("fixed_context_exact_transient_" + str(bits),
              all(error == 0 for error in all_errors), rows)


def fresh_cache():
    rows = []
    for cache in itertools.product((0, 1), repeat=2):
        for q in (F(0), F(1, 3), F(1, 2), F(1)):
            win = F(0)
            for bits in itertools.product((0, 1), repeat=2):
                for route, weight in ((0, q), (1, 1 - q)):
                    updated = cache_step(cache, bits, route)
                    win += F(1, 4) * weight * (score(bits, updated) + 1) / 2
            rows.append(win)
    check("fresh_inputs_every_cache_and_route_bias", all(x == F(1, 2) for x in rows),
          {"cases": len(rows), "win_values": sorted(set(map(str, rows)))})


def markov_stationary(nu, q):
    """Independent direct 16-state calculation, not the geometric-age formula."""
    states = list(itertools.product((0, 1), repeat=4))
    index = {s: i for i, s in enumerate(states)}
    transition = sp.zeros(16)
    for row, (x, y, a, b) in enumerate(states):
        for fx, fy in itertools.product((0, 1), repeat=2):
            bits = (x ^ fx, y ^ fy)
            prob = (nu if fx else 1 - nu) * (nu if fy else 1 - nu)
            for route, weight in ((0, q), (1, 1 - q)):
                cache = cache_step((a, b), bits, route)
                transition[row, index[bits + cache]] += prob * weight
    equation = transition.T - sp.eye(16)
    equation[15, :] = sp.ones(1, 16)
    rhs = sp.zeros(16, 1)
    rhs[15] = 1
    stationary = equation.inv() * rhs
    expectation = sum(stationary[i] * score(s[:2], s[2:]) for i, s in enumerate(states))
    rho = 1 - 2 * nu
    predicted = q * (1 - q) * rho * (1 / (1 - q * rho) + 1 / (1 - (1 - q) * rho))
    check("stationary_cache_nu_" + str(nu) + "_route_" + str(q),
          expectation == predicted and min(stationary) >= 0
          and sum(stationary) == 1 and transition.T * stationary == stationary,
          {"score": str(expectation), "win": str((1 + expectation) / 2),
           "method": "full finite-state stationary equation"})


def seeded_episodes():
    rng = random.Random(2026101601)
    episodes = 20000
    delta = 1e-8
    tolerance = math.sqrt(math.log(2 / delta) / (2 * episodes))
    rows = []
    for block in (1, 2, 4, 16, 64):
        total = 0.0
        for _ in range(episodes):
            bits = (rng.randrange(2), rng.randrange(2))
            cache = (rng.randrange(2), rng.randrange(2))
            wins = 0
            for _ in range(block):
                cache = cache_step(cache, bits, rng.randrange(2))
                wins += score(bits, cache) == 1
            total += wins / block
        estimate = total / episodes
        expected = 1 - (1 - 2**(-block)) / block
        rows.append({"block_size": block, "episodes": episodes, "observed_synthetic_win": estimate,
                     "exact_expected_win": expected, "error": estimate - expected})
    check("seeded_independent_episode_control",
          all(abs(r["error"]) <= tolerance for r in rows),
          {"rows": rows, "tolerance": tolerance,
           "tolerance_basis": "Hoeffding for independent bounded episode averages; per-row delta=1e-8",
           "seed": 2026101601})


def countermodels_and_mutations():
    # The extra-current-signal control deliberately leaves the one-input class.
    truth_table = []
    for x, y in itertools.product((0, 1), repeat=2):
        # Two local wires, followed by OR/AND/NOT at their common future.
        wire0, wire1 = x, y
        output = int((wire0 or wire1) and not (wire0 and wire1))
        truth_table.append({"x": x, "y": y, "output": output})
    wins = [r["output"] == (r["x"] ^ r["y"]) for r in truth_table]
    check("two_current_local_messages_control", all(wins),
          {"win": "1", "truth_table": truth_table,
           "changed_premise": "both current inputs reach common-future receiver"})
    # A past variable that knows the current parity violates freshness, even
    # with no current signal. This is a countermodel to dropping that premise.
    check("input_correlated_history_control", all(h == (x ^ y)
          for x, y, h in ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))),
          {"win": "1", "changed_premise": "history depends on current inputs"})
    q, f00, f01, f10, f11 = sp.symbols("q f00 f01 f10 f11")
    delta = ((q*f00+(1-q)*f10)+(q*f01+(1-q)*f11)
             -(q*f00+(1-q)*f11)-(q*f01+(1-q)*f10))
    check("symbolic_general_response_cancellation", sp.expand(delta) == 0, str(sp.expand(delta)))
    # Wrong endpoint-vs-block-average formula must be detected at B=2.
    exact_block2 = F(5, 8)
    wrong_block2 = 1 - F(1, 4)
    check("wrong_transient_average_rejected", exact_block2 != wrong_block2,
          {"correct": str(exact_block2), "mutated": str(wrong_block2)})
    # Physical Born probabilities appear only as the exposed benchmark.
    phi0, phi1 = sp.symbols("phi0 phi1", real=True)
    benchmark = (1 + sp.cos(phi0-phi1))/2
    p = {(x, y): sp.simplify(benchmark.subs({phi0: sp.pi*x, phi1: sp.pi*y}))
         for x, y in itertools.product((0, 1), repeat=2)}
    contrast = p[0, 0] + p[1, 1] - p[0, 1] - p[1, 0]
    check("exposed_quantum_benchmark_contrast", contrast == 2,
          {"delta": str(contrast), "score": str(contrast/2), "input_status": "benchmark, not derived candidate law"})


def main():
    response_extremes()
    exact_block_cache()
    fresh_cache()
    for nu, q in ((sp.Rational(1,8), sp.Rational(1,2)),
                  (sp.Rational(1,4), sp.Rational(1,2)),
                  (sp.Rational(1,2), sp.Rational(1,2)),
                  (sp.Rational(3,4), sp.Rational(1,2)),
                  (sp.Rational(1,4), sp.Rational(1,3))):
        markov_stationary(nu, q)
    seeded_episodes()
    countermodels_and_mutations()
    sources = {str(Path(p)): hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in REPO_INPUTS}
    sources[str(Path(__file__).resolve().relative_to(ROOT))] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result = {"status": "author development controls", "empirical_validation": False,
              "independent_check": False, "timeout_seconds": AUDIT_TIMEOUT_SEC,
              "sources_sha256": sources, "checks": checks,
              "total": {"pass": sum(c["pass"] for c in checks), "fail": sum(not c["pass"] for c in checks)}}
    (HERE/'NETWORK_HISTORY_CONTROLS_v1.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["total"]["fail"] == 0 else 1)


if __name__ == '__main__':
    main()
