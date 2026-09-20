#!/usr/bin/env python3
"""Independent exact enumeration plus absorption-law calculation.

No primary-agent code or output is imported. Fractions are used for all finite
sums; a separate symbolic killed-generator solve checks the target limit.
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import platform
import subprocess

import numpy as np
import scipy
import sympy as sp

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
EDGES = ((0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5))
NB = tuple(tuple(v if u == x else u for u, v in EDGES if x in (u, v))
           for x in range(6))
EMPTY = -1


def packed(x):
    if isinstance(x, F):
        return {"exact": str(x), "decimal": float(x)}
    if isinstance(x, dict):
        return {str(k): packed(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [packed(v) for v in x]
    return x


def all_states(n):
    for occupied in combinations(range(6), n):
        for values in product(range(6), repeat=n):
            s = [EMPTY] * 6
            for x, a in zip(occupied, values):
                s[x] = a
            yield tuple(s)


STATES = [tuple(all_states(n)) for n in range(4)]


def count_key(s):
    return tuple(s.count(a) for a in range(6))


def topological_hops(s):
    for x, y in EDGES:
        if (s[x] == EMPTY) != (s[y] == EMPTY):
            if s[x] == EMPTY:
                x, y = y, x
            t = list(s)
            t[y], t[x] = t[x], EMPTY
            yield tuple(t), x, y


def components(states):
    unseen = set(states)
    answer = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        todo, found = deque([seed]), [seed]
        while todo:
            s = todo.popleft()
            for t, _, _ in topological_hops(s):
                if t in unseen:
                    unseen.remove(t)
                    todo.append(t)
                    found.append(t)
        answer.append(tuple(sorted(found)))
    return answer


COMPONENTS = [components(states) for states in STATES]
GROUPS = []
CONNECTIVITY = []
for n, (states, parts) in enumerate(zip(STATES, COMPONENTS)):
    grouped = defaultdict(list)
    for s in states:
        grouped[count_key(s)].append(s)
    assert len(parts) == len(grouped)
    assert all(set(c) == set(grouped[count_key(c[0])]) for c in parts)
    GROUPS.append(dict(grouped))
    sizes = defaultdict(int)
    for c in parts:
        sizes[len(c)] += 1
    CONNECTIVITY.append({"n": n, "states": len(states),
                         "components": len(parts), "size_histogram": sizes})


class Model:
    def __init__(self, constant=None):
        self.constant = constant

    def w(self, a, b):
        if self.constant is not None:
            return self.constant
        return F(3, 2) if a == b else F(1, 2) if b == (a ^ 1) else F(1)

    @lru_cache(None)
    def weight(self, s):
        value = F(1)
        for u, v in EDGES:
            if s[u] != EMPTY and s[v] != EMPTY:
                value *= self.w(s[u], s[v])
        return value

    @lru_cache(None)
    def births(self, s):
        result = []
        for x in range(6):
            if s[x] != EMPTY:
                continue
            for a in range(6):
                rate = F(1)
                for y in NB[x]:
                    if s[y] != EMPTY:
                        rate *= self.w(a, s[y])
                t = list(s)
                t[x] = a
                t = tuple(t)
                assert self.weight(s) * rate == self.weight(t)
                result.append((t, rate, x, a))
        return tuple(result)

    def motion(self, s):
        for t, x, y in topological_hops(s):
            a, source, destination = s[x], F(1), F(1)
            for v in NB[x]:
                if v != y and s[v] != EMPTY:
                    source *= self.w(a, s[v])
            for v in NB[y]:
                if v != x and s[v] != EMPTY:
                    destination *= self.w(a, s[v])
            yield t, destination / (source + destination)

    @lru_cache(None)
    def hazard(self, s):
        return sum((r for _, r, _, _ in self.births(s)), F(0))


def identical(s):
    return len({a for a in s if a != EMPTY}) == 1


def tv(a, b):
    return sum((abs(a.get(s, F(0)) - b.get(s, F(0)))
                for s in set(a) | set(b)), F(0)) / 2


def static_level(model, n):
    partition = sum((model.weight(s) for s in STATES[n]), F(0))
    return partition, {s: model.weight(s) / partition for s in STATES[n]}


def grow(model, mode):
    """mode=rare pools only proved components; frozen uses singleton components."""
    alpha = {STATES[0][0]: F(1)}
    levels = []
    for n in range(3):
        following = defaultdict(F)
        if mode == "rare":
            mass = defaultdict(F)
            for s, p in alpha.items():
                mass[count_key(s)] += p
            for key, prob in mass.items():
                c = GROUPS[n][key]
                denominator = sum((model.weight(s) * model.hazard(s) for s in c), F(0))
                for s in c:
                    for t, r, _, _ in model.births(s):
                        following[t] += prob * model.weight(s) * r / denominator
        elif mode == "frozen":
            for s, prob in alpha.items():
                for t, r, _, _ in model.births(s):
                    following[t] += prob * r / model.hazard(s)
        else:
            raise ValueError(mode)
        alpha = dict(following)
        assert sum(alpha.values(), F(0)) == 1
        partition, static = static_level(model, n + 1)
        levels.append({"n": n + 1, "mass": sum(alpha.values(), F(0)),
                       "all_identical": sum((p for s, p in alpha.items() if identical(s)), F(0)),
                       "static_partition": partition,
                       "static_all_identical": sum((p for s, p in static.items() if identical(s)), F(0)),
                       "total_variation_from_static": tv(alpha, static)})
    return levels, alpha


MODEL = Model()
DB_COUNTS = []
for n, states in enumerate(STATES):
    checked = 0
    for s in states:
        for t, rate in MODEL.motion(s):
            reverse = dict(MODEL.motion(t))[s]
            assert MODEL.weight(s) * rate == MODEL.weight(t) * reverse
            checked += 1
    DB_COUNTS.append({"n": n, "directed_hops_checked_exactly": checked})

rare, rare_dist = grow(MODEL, "rare")
frozen, frozen_dist = grow(MODEL, "frozen")
constant_controls = {}
for scalar in (F(1), F(2)):
    const_model = Model(scalar)
    rc, _ = grow(const_model, "rare")
    fc, _ = grow(const_model, "frozen")
    # Contents are i.i.d. uniform for constant weights, regardless of placement.
    assert rc[-1]["all_identical"] == fc[-1]["all_identical"] == F(1, 6**2)
    assert rc[-1]["static_all_identical"] == F(1, 6**2)
    constant_controls[str(scalar)] = {"rare": rc, "no_motion": fc}

# A separate exact absorption calculation on the 15 placements of two zeroes.
pair_states = GROUPS[2][(2, 0, 0, 0, 0, 0)]
pair_index = {s: i for i, s in enumerate(pair_states)}
q = [[F(0) for _ in pair_states] for _ in pair_states]
for s, i in pair_index.items():
    for t, rate in MODEL.motion(s):
        q[i][pair_index[t]] += rate
        q[i][i] -= rate
b = [MODEL.hazard(s) for s in pair_states]
l = [sum((r for _, r, _, a in MODEL.births(s) if a == 0), F(0)) for s in pair_states]
z = sum((MODEL.weight(s) for s in pair_states), F(0))
pi = [MODEL.weight(s) / z for s in pair_states]
mean_b = sum((p * bb for p, bb in zip(pi, b)), F(0))
pre_rare = [p * bb / mean_b for p, bb in zip(pi, b)]
pre_bias = sum((abs(p - r) for p, r in zip(pi, pre_rare)), F(0)) / 2

# Graph automorphisms are enumerated, not assumed, to lump the 15-state solve.
edge_set = {frozenset(e) for e in EDGES}
automorphisms = [p for p in permutations(range(6))
                 if {frozenset((p[u], p[v])) for u, v in EDGES} == edge_set]


def permuted(s, p):
    t = [EMPTY] * 6
    for i, a in enumerate(s):
        t[p[i]] = a
    return tuple(t)


orbits = {}
for s in pair_states:
    key = min(permuted(s, p) for p in automorphisms)
    orbits.setdefault(key, []).append(s)
orbits = list(orbits.values())
orbit_index = {s: i for i, orb in enumerate(orbits) for s in orb}
qbar, bbar, lbar, pibar = [], [], [], []
for orb in orbits:
    rows = []
    for s in orb:
        row = [F(0)] * len(orbits)
        for t, j in pair_index.items():
            row[orbit_index[t]] += q[pair_index[s]][j]
        rows.append(row)
    assert all(row == rows[0] for row in rows)
    assert len({b[pair_index[s]] for s in orb}) == 1
    assert len({l[pair_index[s]] for s in orb}) == 1
    qbar.append(rows[0])
    bbar.append(b[pair_index[orb[0]]])
    lbar.append(l[pair_index[orb[0]]])
    pibar.append(sum((pi[pair_index[s]] for s in orb), F(0)))

epsilon = sp.Symbol("epsilon", positive=True)
a_symbolic = epsilon * sp.diag(*bbar) - sp.Matrix(qbar)
h_symbolic = a_symbolic.inv(method="DM") * (epsilon * sp.Matrix(lbar))
assert all(sp.cancel(x) == 0 for x in a_symbolic * h_symbolic - epsilon * sp.Matrix(lbar))
two_identical = rare[1]["all_identical"]
p_symbolic = sp.cancel(sp.Rational(two_identical) * (sp.Matrix([pibar]) * h_symbolic)[0])
limit_slow = F(sp.limit(p_symbolic, epsilon, 0))
limit_fast = F(sp.limit(p_symbolic, epsilon, sp.oo))
assert limit_slow == rare[-1]["all_identical"]
assert limit_fast == frozen[-1]["all_identical"]

q_float = np.array(q, dtype=float)
b_float = np.array(b, dtype=float)
l_float = np.array(l, dtype=float)
pi_float = np.array(pi, dtype=float)
finite = []
for eps in (1e-6, 1e-4, 0.01, 0.1, 1.0, 10.0, 100.0, 1e4, 1e6):
    a_float = eps * np.diag(b_float) - q_float
    h = np.linalg.solve(a_float, eps * l_float)
    visit_scaled = np.linalg.solve(a_float.T, eps * pi_float)
    pre = visit_scaled * b_float
    probability = float(two_identical) * float(pi_float @ h)
    symbolic_value = float(p_symbolic.subs(epsilon, sp.Rational(str(eps))))
    assert abs(probability - symbolic_value) < 1e-10
    assert abs(float(pre.sum()) - 1) < 1e-10
    finite.append({"epsilon": eps, "probability": probability,
                   "symbolic_probability": symbolic_value,
                   "max_harmonic_residual": float(np.max(abs(a_float @ h - eps * l_float))),
                   "prebirth_mass": float(pre.sum()),
                   "prebirth_tv_from_stationary": float(np.sum(abs(pre - pi_float)) / 2)})

# Constant-hazard control: arbitrary positive motion plus independent hazard 1
# leaves a stationary initial distribution stationary at the killing event.
unit_hazard_error = 0.0
for eps in (0.001, 0.1, 1.0, 10.0):
    law = np.linalg.solve((eps * np.eye(len(pi)) - q_float).T, eps * pi_float)
    unit_hazard_error = max(unit_hazard_error, float(np.max(abs(law - pi_float))))
assert unit_hazard_error < 1e-10

# Adversarial extension: content counts fail for five distinct contents / one hole.
one_hole_states = tuple(permutations((EMPTY, 0, 1, 2, 3, 4)))
one_hole_parts = components(one_hole_states)
assert len({count_key(s) for s in one_hole_states}) == 1

# The naive unweighted pre-event law gives E_pi[L/B], not E_pi[L]/E_pi[B].
naive = two_identical * sum((p * ll / bb for p, ll, bb in zip(pi, l, b)), F(0))
assert naive != limit_slow
assert naive == limit_fast

# Deliberately wrong candidate laws must fail against the independent
# absorption calculation; catches do not grant a scientific verdict.
rejected_candidates = []
for name, candidate in (("omit_prebirth_hazard_bias", naive),
                        ("pool_all_content_counts_as_one_component", rare[-1]["static_all_identical"])):
    try:
        assert candidate == limit_slow
    except AssertionError:
        rejected_candidates.append(name)
    else:
        raise AssertionError(f"candidate was not rejected: {name}")

triple_edge_profile = defaultdict(int)
triple_partition = defaultdict(F)
for occupied in combinations(range(6), 3):
    edge_number = sum(u in occupied and v in occupied for u, v in EDGES)
    triple_edge_profile[edge_number] += 1
for s in STATES[3]:
    occupied = tuple(i for i, a in enumerate(s) if a != EMPTY)
    triple_partition[occupied] += MODEL.weight(s)
assert set(triple_partition.values()) == {F(6**3)}

summary = {
    "connectivity": CONNECTIVITY,
    "detailed_balance": DB_COUNTS,
    "rare_birth_levels": rare,
    "no_motion_levels": frozen,
    "constant_weight_controls": constant_controls,
    "exact_comparison": {
        "rare": limit_slow, "static": rare[-1]["static_all_identical"],
        "static_minus_rare": rare[-1]["static_all_identical"] - limit_slow,
        "rare_div_static": limit_slow / rare[-1]["static_all_identical"],
        "no_motion": limit_fast, "naive_unbiased_prebirth": naive},
    "identical_pair": {
        "partition": z, "mean_total_birth_rate_without_epsilon": mean_b,
        "prebirth_tv_from_stationary_limit": pre_bias,
        "stationary_weighted_birth_hazard_sum": z * mean_b,
        "stationary_weighted_identical_birth_sum": z * sum((p * ll for p, ll in zip(pi, l)), F(0)),
        "automorphism_count": len(automorphisms),
        "orbit_sizes": [len(orb) for orb in orbits],
        "orbits_occupied_sites": [[tuple(i for i, a in enumerate(s) if a != EMPTY) for s in orb] for orb in orbits],
        "quotient_generator": qbar, "quotient_hazards": bbar,
        "quotient_identical_birth_rates": lbar,
        "quotient_stationary": pibar,
        "finite_epsilon_probability": str(p_symbolic)},
    "finite_epsilon": finite,
    "constant_hazard_control_max_absolute_error": unit_hazard_error,
    "rejected_candidate_laws": rejected_candidates,
    "three_site_induced_edge_profile": triple_edge_profile,
    "three_site_content_partition_per_occupied_set": sorted(set(triple_partition.values())),
    "one_hole_five_distinct": {"states": len(one_hole_states),
                                "components": len(one_hole_parts),
                                "component_sizes": [len(c) for c in one_hole_parts]},
}
(OUT / "results.json").write_text(json.dumps(packed(summary), indent=2) + "\n")

source_note = Path("/Users/jonreilly/Documents/Codex/physics-sync-2026-09-20/sources/pr-8530/docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md")
source_paths = [source_note, ROOT / "AGENTS.md", ROOT / "docs/ai_methodology/SCIENCE_WORKFLOW.md",
                ROOT / "docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md",
                Path("/Users/jonreilly/.codex/skills/workhorse/SKILL.md"), Path(__file__).resolve()]
sha256 = lambda data: hashlib.sha256(data).hexdigest()
git = lambda *args: subprocess.check_output(["git", *args], cwd=ROOT).strip().decode()
manifest = {"head": git("rev-parse", "HEAD"), "origin_main": git("rev-parse", "origin/main"),
            "origin_ai_execution": git("rev-parse", "origin/ai/execution"),
            "supplied_original_pr_head": "1c1a56df6c979401f94ff7191a5b18a1236f1b74",
            "sha256": {str(path): sha256(path.read_bytes()) for path in source_paths},
            "planning_AGENTS_sha256": sha256(subprocess.check_output(["git", "show", "origin/ai/execution:AGENTS.md"], cwd=ROOT)),
            "python": platform.python_version(), "numpy": np.__version__,
            "scipy": scipy.__version__, "sympy": sp.__version__}
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps(packed({"exact_comparison": summary["exact_comparison"],
                        "connectivity": CONNECTIVITY, "detailed_balance": DB_COUNTS,
                        "finite_epsilon_probability": str(p_symbolic),
                        "finite_epsilon": finite,
                        "one_hole_five_distinct": summary["one_hole_five_distinct"]}), indent=2))
