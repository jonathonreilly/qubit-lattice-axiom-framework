#!/usr/bin/env python3
"""Source-bound selective review checks, with exact constructions of added claims.

No primary helper is used in the exact checks. The final floating metric is
explicitly a source-bound reproduction of the primary relative-position gate.
Writes only RESULTS.json beside this file; preserves all prior sealed evidence.
"""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import platform
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INDEPENDENT = HERE.parent / "independent"
NOTE = "docs/MOBILE_RECORDS_EMPTY_START_MOTION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-21.md"
RUNNER = "scripts/mobile_records_empty_start_motion_response_2026_09_21.py"
SOURCES = {
    NOTE: "a8e9d26399a8c810a7bb919edaaa9e9a5554f18139e601c790c2b23c24177a74",
    RUNNER: "56aeb1083d9a66a5dba5ad68b625f539e67fbd9fa458e835ca4fae60ee697156",
}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def torus(side, dim):
    points = list(product(range(side), repeat=dim))
    neighbors = {}
    for x in points:
        near = set()
        for i in range(dim):
            for step in [-1, 1]:
                y = list(x)
                y[i] = (y[i] + step) % side
                near.add(tuple(y))
        neighbors[x] = near
    return points, neighbors


def relative(x, y, side):
    return tuple((b-a) % side for a, b in zip(x, y))


def clean(row):
    return {i: value for i, value in row.items() if value}


def relative_rows(points, neighbors, g):
    zero = points[0]
    rs = points[1:]
    weights = {r: g if r in neighbors[zero] else F(1) for r in rs}
    common = {r: F(len(neighbors[zero] & neighbors[r])) for r in rs}
    rows = {}
    for r in rs:
        row = {rp: 2*weights[rp]/(weights[r]+weights[rp])
               for rp in neighbors[r] if rp != zero}
        row[r] = -sum(row.values(), F(0))
        rows[r] = clean(row)
    return rows, weights, common


def check_exact_lumping(side, dim, g):
    points, neighbors = torus(side, dim)
    Hr, wr, cr = relative_rows(points, neighbors, g)
    checked = 0
    for x in points:
        for y in points:
            if x == y:
                continue
            r = relative(x, y, side)
            old_w = g if y in neighbors[x] else F(1)
            aggregate = defaultdict(F)
            for moved in [0, 1]:
                positions = (x, y)
                for destination in neighbors[positions[moved]]:
                    if destination == positions[1-moved]:
                        continue
                    new = list(positions)
                    new[moved] = destination
                    new_w = g if new[1] in neighbors[new[0]] else F(1)
                    rate = new_w/(old_w+new_w)
                    aggregate[relative(*new, side)] += rate
                    aggregate[r] -= rate
            assert clean(aggregate) == Hr[r]
            checked += 1
    # Counting identity for the inversion-even observable used in the theorem.
    physical = sum((g if y in neighbors[x] else F(1))*len(neighbors[x] & neighbors[y])**2
                   for x, y in combinations(points, 2))
    reduced = F(len(points), 2)*sum(wr[r]*cr[r]**2 for r in wr)
    assert physical == reduced
    return {"side": side, "dimension": dim, "g": str(g),
            "ordered_generator_rows": checked, "weighted_norm": str(physical)}


def general_menu():
    # Positive symmetric row-six, not invariant under the six-axis symmetry.
    u = (2, -1, -1, 0, 0, 0)
    q = (0, 0, 0, 1, -1, 0)
    return [[1+F(u[a]*u[b], 10)-F(q[a]*q[b], 5) for b in range(6)]
            for a in range(6)], u, q


def actual_hazard(state, neighbors, W):
    total = F(0)
    for x, sx in enumerate(state):
        if sx != -1:
            continue
        for a in range(6):
            rate = F(1)
            for y in neighbors[x]:
                if state[y] != -1:
                    rate *= W[a][state[y]]
            total += rate
    return total


def pair_content_power_check(side, dim):
    points, nb = torus(side, dim)
    ids = {x: i for i, x in enumerate(points)}
    neighbors = [{ids[y] for y in nb[x]} for x in points]
    n = len(points)
    W, _, _ = general_menu()
    states = []
    for x, y in combinations(range(n), 2):
        for a, b in product(range(6), repeat=2):
            state = [-1]*n
            state[x], state[y] = a, b
            states.append(tuple(state))
    index = {s: i for i, s in enumerate(states)}
    weights, hazard, H = [], [], []
    for state in states:
        occupied = [x for x, a in enumerate(state) if a != -1]
        x, y = occupied
        weights.append(W[state[x]][state[y]] if y in neighbors[x] else F(1))
        hazard.append(actual_hazard(state, neighbors, W))
    for i, state in enumerate(states):
        row = defaultdict(F)
        for x, a in enumerate(state):
            if a == -1:
                continue
            for y in neighbors[x]:
                if state[y] != -1:
                    continue
                target = list(state)
                target[x], target[y] = -1, a
                j = index[tuple(target)]
                rate = weights[j]/(weights[i]+weights[j])
                row[j] += rate
                row[i] -= rate
        H.append(clean(row))
    full = hazard[:]
    reduced = {}
    h = [[sum(W[a][z]*W[z][b] for z in range(6))-6
          for b in range(6)] for a in range(6)]
    for a, b in product(range(6), repeat=2):
        g = W[a][b]
        if g not in reduced:
            rows, wr, c = relative_rows(points, nb, g)
            reduced[g] = [rows, wr, c, c.copy()]
    results = []
    for order in range(1, 4):
        full = [sum(rate*full[j] for j, rate in row.items()) for row in H]
        actual = -sum(w*b*v for w, b, v in zip(weights, hazard, full))
        for g, (rows, wr, c, current) in reduced.items():
            reduced[g][3] = {r: sum(rate*current[rp] for rp, rate in row.items())
                             for r, row in rows.items()}
        prediction = F(0)
        for a, b in product(range(6), repeat=2):
            rows, wr, c, current = reduced[W[a][b]]
            prediction -= F(n, 2)*h[a][b]**2*sum(wr[r]*c[r]*current[r] for r in wr)
        assert actual == prediction
        results.append({"power": order, "full_minus_weighted_b_H_power_b": str(actual)})
    return {"side": side, "dimension": dim, "physical_content_states": len(states),
            "matrix_power_checks": results}


def birth_row(state, neighbors, W):
    row = defaultdict(F)
    for x, value in enumerate(state):
        if value != -1:
            continue
        for a in range(6):
            rate = F(1)
            for y in neighbors[x]:
                if state[y] != -1:
                    rate *= W[a][state[y]]
            target = list(state)
            target[x] = a
            row[tuple(target)] += rate
            row[state] -= rate
    return clean(row)


def initial_moment_checks():
    W, u, q = general_menu()
    assert all(sum(row) == 6 for row in W)
    assert min(map(min, W)) > 0
    checked = 0
    for n, edges in [(1, []), (3, [(0, 1), (1, 2)]),
                     (3, [(0, 1), (1, 2), (0, 2)]),
                     (4, [(0, 1), (2, 3)]), (4, [(0, 1), (0, 2), (0, 3)])]:
        nb = [{y if x == i else x for x, y in edges if i in (x, y)} for i in range(n)]
        first = birth_row(tuple([-1]*n), nb, W)
        second = defaultdict(F)
        for s, value in first.items():
            for t, rate in birth_row(s, nb, W).items():
                second[t] += value*rate
        for chi, theta in [(u, F(3, 5)), (q, F(-2, 5))]:
            assert all(sum(W[a][b]*chi[b] for b in range(6)) == theta*chi[a] for a in range(6))
            nu = sum(F(c*c, 6) for c in chi)
            field = lambda state, x: F(0) if state[x] == -1 else F(chi[state[x]])
            for x in range(n):
                assert sum(p*(s[x] != -1) for s, p in first.items()) == 6
                assert sum(p*(s[x] != -1) for s, p in second.items())/2 == -18
                assert sum(p*field(s, x)**2 for s, p in first.items()) == 6*nu
                assert sum(p*field(s, x)**2 for s, p in second.items())/2 == -18*nu
                checked += 4
                for y in range(x+1, n):
                    covariance = sum(p*field(s, x)*field(s, y) for s, p in second.items())/2
                    assert covariance == 6*nu*theta*(y in nb[x])
                    checked += 1
            spatial = list(range(1, n+1))
            diagonal = sum(c*c for c in spatial)
            numerator2 = sum(p*sum(spatial[x]*field(s, x) for x in range(n))**2
                             for s, p in second.items())/2
            denominator2 = -18*nu*diagonal
            adjacency = sum(spatial[x]*spatial[y] for x in range(n) for y in nb[x])
            assert (numerator2-denominator2)/(6*nu*diagonal) == theta*adjacency/diagonal
            checked += 1
    # Scope counterexample: an admissible matrix and a chosen scalar eigenmode
    # do not force all three six-axis coordinates to have its eigenvalue.
    rank_one = [[1+F(u[a]*u[b], 10) for b in range(6)] for a in range(6)]
    axes = [(1, -1, 0, 0, 0, 0), (0, 0, 1, -1, 0, 0), (0, 0, 0, 0, 1, -1)]
    vector_theta = sum(F(v[a])*rank_one[a][b]*v[b]
                       for v in axes for a, b in product(range(6), repeat=2))/6
    assert vector_theta == F(1, 6) != F(3, 5)
    return {"exact_scalar_moment_assertions": checked,
            "vector_scope_counterexample": {
                "W": "J + u u^T/10, u=(2,-1,-1,0,0,0)",
                "scalar_eigenfunction": "u", "scalar_theta": "3/5",
                "unit_vector_structure_effective_theta": str(vector_theta)}}


def main():
    assert all(digest(ROOT/path) == expected for path, expected in SOURCES.items())
    receipts = {}
    for subdir, name in [("", "SEAL.json"), ("", "POST_SEAL_GEOMETRY_REVIEW_SEAL.json"),
                         ("formation_intensity", "SEAL.json")]:
        base = INDEPENDENT/subdir
        seal = json.loads((base/name).read_text())
        for path, expected in seal["artifacts_sha256"].items():
            assert digest(base/path) == expected, (subdir, path)
        receipts[str(Path(subdir)/name)] = digest(base/name)
    exact = [check_exact_lumping(side, dim, g)
             for side, dim in [(2, 2), (3, 1), (4, 1), (6, 1), (3, 2), (4, 2), (3, 3)]
             for g in [F(1, 2), F(1), F(3, 2), F(7, 5)]]
    content_powers = [pair_content_power_check(side, dim) for side, dim in [(4, 1), (3, 2)]]
    moments = initial_moment_checks()
    # This portion reproduces, rather than independently derives, a primary
    # numerical claim. No module cache file is written.
    namespace = {"__name__": "reviewed_primary_runner", "__file__": str(ROOT/RUNNER)}
    exec(compile((ROOT/RUNNER).read_text(), str(ROOT/RUNNER), "exec"), namespace)
    discrepancies = []
    for side, dim in [(4, 1), (6, 1), (3, 2), (4, 2), (3, 3)]:
        for g in [.5, 1., 1.5]:
            H, w, c, Hr, wr, cr, n = namespace["position_matrices"](side, dim, g)
            full = namespace["spectral_coefficient"](H, w, c, 1.3, .7)/n
            reduced = namespace["spectral_coefficient"](Hr, wr, cr, 1.3, .7)/2
            discrepancy = float(abs(full-reduced))
            assert discrepancy < 1e-11*max(1., abs(full))
            discrepancies.append({"side": side, "dimension": dim, "g": g,
                                  "absolute_difference": discrepancy})
    result = {"reviewed_sources_sha256": SOURCES, "prior_seals_reverified": receipts,
              "exact_lumping_cases": exact,
              "exact_ordered_generator_rows_checked": sum(x["ordered_generator_rows"] for x in exact),
              "full_content_semigroup_power_checks": content_powers,
              "initial_moments": moments,
              "primary_relative_gate_reproduction": discrepancies,
              "primary_relative_gate_max_absolute_difference": max(x["absolute_difference"] for x in discrepancies),
              "python": platform.python_version(), "all_checks_passed": True}
    (HERE/"RESULTS.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
