#!/usr/bin/env python3
"""Exact LIB1 checks plus actual B1 mutations; one sequential invocation."""
# [R-fix 2026-10-29 B1] Frozen v1 is preserved; criteria are in lib1_criteria_v2.md.
import datetime
from fractions import Fraction
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
START = time.monotonic()
REPORT = {"kind": "finite author check; not an independent proof review",
          "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "counts": {}, "resources": [], "wrong_output_contrasts": {},
          "norm_witnesses": {}}


class ResourceRefusal(Exception):
    pass


def guard(where):
    if sys.platform != "darwin":
        raise ResourceRefusal("This receipt requires the specified macOS memory gate")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on Darwin
    loads = os.getloadavg()
    cp = subprocess.run(["/usr/bin/memory_pressure", "-Q"], capture_output=True,
                        text=True, timeout=5)
    match = re.search(r"System-wide memory free percentage:\s*(\d+)%", cp.stdout)
    if cp.returncode or not match:
        raise ResourceRefusal("Cannot verify memory free percentage: " + cp.stdout + cp.stderr)
    free = int(match.group(1))
    niceness = os.getpriority(os.PRIO_PROCESS, 0)
    names = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
    threads = {key: os.environ.get(key) for key in names}
    row = {"where": where, "max_rss_bytes": rss, "load_averages": loads,
           "memory_free_percent": free, "nice": niceness,
           "thread_environment": threads, "elapsed_seconds": time.monotonic()-START}
    REPORT["resources"].append(row)
    if rss >= 2_000_000_000 or max(loads) >= 20 or free < 50:
        raise ResourceRefusal("Resource threshold not met: " + json.dumps(row))
    if niceness < 10 or any(v != "1" for v in threads.values()):
        raise ResourceRefusal("Niceness or thread environment not as pre-stated")
    if time.monotonic()-START > 60:
        raise ResourceRefusal("60-second deadline reached")


def require(condition, name):
    if not condition:
        raise AssertionError(name)
    REPORT["counts"][name] = REPORT["counts"].get(name, 0) + 1


def vertices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask ^= bit


def components(mask, adj):
    out = []
    while mask:
        seed = mask & -mask
        comp, frontier = seed, seed
        while frontier:
            nbr = 0
            for v in vertices(frontier):
                nbr |= adj[v]
            frontier = nbr & mask & ~comp
            comp |= frontier
        out.append(comp)
        mask &= ~comp
    return out


def connected(mask, adj):
    return bool(mask) and len(components(mask, adj)) == 1


def touches(x, h, adj):
    return bool(x & h) or any(adj[v] & h for v in vertices(x))


def saturated(x, holes):
    return all(not (x & h) or (x & h) == h for h in holes)


def fill(x, holes, adj):
    y = x
    for h in holes:
        if touches(x, h, adj):
            y |= h
    return y


def reference_fill(x, inactive, adj):
    """Independent implementation: iterative one-vertex growth, no hole list."""
    y = x
    while True:
        nxt = y
        for v in vertices(inactive & ~y):
            if adj[v] & y:
                nxt |= 1 << v
        if nxt == y:
            return y
        y = nxt


def graph(n, edges):
    adj = [0]*n
    for i, j in edges:
        if i != j:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def steiner_table(adj):
    """Exact optimization over connected supersets, not a tree-walk bound."""
    total = 1 << len(adj)
    cs = [c for c in range(1, total) if connected(c, adj)]
    return {s: min(c.bit_count()-1 for c in cs if c & s == s)
            for s in range(1, total)}


def submasks(mask):
    s = mask
    while True:
        yield s
        if not s:
            break
        s = (s-1) & mask


def norm(coeff, labels, roots, active, weight_power):
    best = Fraction(0)
    for v in vertices(roots):
        value = sum((coeff[x]*(1 << (weight_power*(labels[x] & active).bit_count()))
                     for x in coeff if labels[x] & (1 << v)), Fraction(0))
        best = max(best, value)
    return best


def full_output_norm(grouped, out_labels, allv, lam):
    """Shared by every bounded-hole inequality and both exact witnesses."""
    return norm(grouped, out_labels, allv, allv, 1)


def exercise(name, adj):
    guard(name+": start")
    n, allv = len(adj), (1 << len(adj))-1
    ts = steiner_table(adj)
    supports = [x for x in range(1, allv+1) if connected(x, adj)]
    cases = 0
    for omega in range(allv+1):
        old_holes = components(allv ^ omega, adj)
        polys = [x for x in supports if x & omega and saturated(x, old_holes)]
        old_len = {x: ts[x & omega] for x in polys}
        coeff = {x: Fraction(1, 1 << (20*old_len[x])) for x in polys}
        labels = {x: x for x in polys}
        old_active_norm = norm(coeff, labels, omega, omega, 1)
        for v in vertices(omega):
            count = sum((Fraction(1, 1 << (16*old_len[x]))
                         for x in polys if x & (1 << v)), Fraction(0))
            require(count <= 1024, "rooted_entropy_bound")
        for lam in submasks(omega):
            cases += 1
            if cases % 250 == 0:
                guard(name+": nested pair "+str(cases))
            holes = components(allv ^ lam, adj)
            grouped, polynomial = {}, {}
            inactive = {x: Fraction((-1)**x.bit_count(), x+1)
                        for x in polys if not x & lam}
            for x in polys:
                if not x & lam:
                    continue
                y = fill(x, holes, adj)
                require(y == reference_fill(x, allv ^ lam, adj), "two_closure_algorithms")
                require(connected(y, adj) and saturated(y, holes), "new_polymer_class")
                require(x & y == x and y & lam == x & lam, "containment_and_active_identity")
                require(ts[y & lam] <= old_len[x], "ambient_tree_monotonicity")
                grouped[y] = grouped.get(y, Fraction(0)) + coeff[x]
                terms = polynomial.setdefault(y, {})
                terms[x] = terms.get(x, Fraction(0)) + Fraction((-1)**x.bit_count(), x+1)
                require(x & y == x, "all_original_monomial_sources_retained")
            recombined = dict(inactive)
            for terms in polynomial.values():
                for monomial, value in terms.items():
                    recombined[monomial] = recombined.get(monomial, Fraction(0)) + value
            original = {x: Fraction((-1)**x.bit_count(), x+1) for x in polys}
            require(recombined == original, "polynomial_identity_with_inactive_remainder")
            for y, value in grouped.items():
                require(value <= Fraction(1024, 1 << (4*ts[y & lam])), "pointwise_decay_bound")
            out_labels = {y: y for y in grouped}
            out_active_norm = norm(grouped, out_labels, lam, lam, 1)
            require(out_active_norm <= old_active_norm, "active_norm_contraction")
            if holes:
                m = max(h.bit_count() for h in holes)
                input_strong = norm(coeff, labels, allv, allv, 1+8*m)
                output_full = full_output_norm(grouped, out_labels, allv, lam)
                require(output_full <= 9*m*input_strong, "bounded_hole_full_norm")
            else:
                require(grouped == coeff, "no_hole_identity")
    REPORT.setdefault("graphs", []).append({"name": name, "vertices": n,
                                           "nested_active_pairs": cases,
                                           "connected_supports": len(supports)})
    guard(name+": end")


def native_four_dimensional():
    coords = list(itertools.product(range(2), repeat=4))
    index = {x: i for i, x in enumerate(coords)}
    edges = []
    for x in coords:
        for axis in range(4):
            y = list(x); y[axis] ^= 1
            edges.append((index[x], index[tuple(y)]))
    adj = graph(16, edges)
    allv = (1 << 16)-1
    supports = [1 << i for i in range(16)]
    supports += sorted({(1 << i) | (1 << j) for i, j in edges})
    removed = [0] + [1 << i for i in range(16)]
    removed += [(1 << i) | (1 << j) for i, j in itertools.combinations(range(16), 2)]
    count = 0
    for inactive in removed:
        lam = allv ^ inactive
        holes = components(inactive, adj)
        for x in supports:
            if not x & lam:
                continue
            y = fill(x, holes, adj)
            require(y == reference_fill(x, inactive, adj), "native_4d_closure")
            require(connected(y, adj) and saturated(y, holes)
                    and y & lam == x & lam and x & y == x, "native_4d_geometry")
            # Active subset is a singleton or the same adjacent pair.
            require((y & lam).bit_count()-1 <= x.bit_count()-1, "native_4d_tree")
            count += 1
    REPORT["native_4d"] = {"vertices": 16, "degree": max(x.bit_count() for x in adj),
                            "active_sets": len(removed), "support_instances": count}
    guard("native 4d end")


def wrong_output_contrasts():
    """Inherited v1 comparisons: static contrasts, not actual mutant runs."""
    adj = graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    allv, lam = 15, 1
    holes = components(allv ^ lam, adj)
    x, y = 1, fill(1, holes, adj)
    require(y == 15, "mutation_setup_full_hole")
    bad_fill = x
    for h in holes:
        if x & h:
            bad_fill |= h
    checks = {
        "drop_inactive_remainder": ({1: Fraction(1), 2: Fraction(1, 3)} != {1: Fraction(1)}),
        "erase_inactive_source": ({3: Fraction(1, 7)} != {3 & lam: Fraction(1, 7)}),
        "fill_intersected_only": bad_fill != y,
    }
    for key, distinguished in checks.items():
        require(distinguished, "static_contrast_"+key)
    REPORT["wrong_output_contrasts"] = {
        key: "distinguished static wrong output; no implementation mutant run in v2"
        for key in checks}


def exact_norm_witnesses():
    guard("exact norm witnesses: start")
    adj = graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    allv, lam = 15, 1
    holes = components(allv ^ lam, adj)
    y = fill(1, holes, adj)
    require(y == 15, "four_cycle_witness_support")
    input_full = norm({1: Fraction(1)}, {1: 1}, allv, allv, 1)
    grouped, out_labels = {y: Fraction(1)}, {y: y}
    output_full = full_output_norm(grouped, out_labels, allv, lam)
    output_active = norm(grouped, out_labels, lam, lam, 1)
    REPORT["norm_witnesses"]["four_cycle"] = {
        "input_supports": [[0]], "output_supports": [[0, 1, 2, 3]],
        "active_vertices": [0], "activity_suprema": [1], "mu": "log(2)",
        "computed": {"input_full": str(input_full), "output_full": str(output_full),
                     "output_active": str(output_active)},
        "expected": {"input_full": "2", "output_full": "16", "output_active": "2"},
        "independent_derivation": "Input 2^1; full rooted sums (16,16,16,16) from 2^4; active 2^1."}
    require(input_full == 2, "four_cycle_input_full_norm_exact")
    require(output_full == 16, "four_cycle_full_output_norm_exact")
    require(output_active == 2, "four_cycle_active_output_norm_exact")

    adj = graph(3, [(0, 1), (1, 2)])
    allv, lam = 7, 5
    holes = components(allv ^ lam, adj)
    inputs = {1: Fraction(1), 4: Fraction(1)}
    grouped = {}
    for x, coefficient in inputs.items():
        y = fill(x, holes, adj)
        grouped[y] = grouped.get(y, Fraction(0)) + coefficient
    require(grouped == {3: Fraction(1), 6: Fraction(1)}, "overlap_witness_supports")
    out_labels = {y: y for y in grouped}
    input_full = norm(inputs, {x: x for x in inputs}, allv, allv, 1)
    output_full = full_output_norm(grouped, out_labels, allv, lam)
    output_active = norm(grouped, out_labels, lam, lam, 1)
    REPORT["norm_witnesses"]["overlap_path"] = {
        "input_supports": [[0], [2]], "output_supports": [[0, 1], [1, 2]],
        "active_vertices": [0, 2], "inactive_maximizing_root": 1,
        "activity_suprema": [1, 1], "mu": "log(2)",
        "computed": {"input_full": str(input_full), "output_full": str(output_full),
                     "output_active": str(output_active)},
        "expected": {"input_full": "2", "output_full": "8", "output_active": "2"},
        "independent_derivation": "Each full support weighs 2^2=4; rooted sums (4,8,4); input and active maxima 2."}
    require(input_full == 2, "overlap_input_full_norm_exact")
    require(output_full == 8, "overlap_full_output_norm_exact")
    require(output_active == 2, "overlap_active_output_norm_exact")
    guard("exact norm witnesses: end")


def main():
    guard("before any enumeration")
    exercise("path6", graph(6, [(i, i+1) for i in range(5)]))
    exercise("cycle6", graph(6, [(i, (i+1) % 6) for i in range(6)]))
    exercise("box2x3", graph(6, [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]))
    native_four_dimensional()
    wrong_output_contrasts()
    exact_norm_witnesses()
    guard("completion")


def capture_trial(namespace, label, compiled_source, original_hash, criteria_hash, mutation):
    """Run a baseline or actual compiled mutant once; retain failures honestly."""
    report = namespace["REPORT"]
    report.update({"trial": label, "source_mutation": mutation,
                   "script_sha256": original_hash, "criteria_sha256": criteria_hash,
                   "compiled_source_sha256": hashlib.sha256(compiled_source.encode()).hexdigest(),
                   "trial_started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()})
    try:
        namespace["main"]()
        report.update({"result": "completed; all enumerated predicates satisfied", "exit_classification": 0})
    except namespace["ResourceRefusal"] as exc:
        report.update({"result": "not completed: resource gate/deadline", "reason": str(exc),
                       "failure_type": "ResourceRefusal", "exit_classification": 75})
    except AssertionError as exc:
        report.update({"result": "assertion failed", "reason": str(exc),
                       "failure_type": "AssertionError", "exit_classification": 1})
    except Exception as exc:
        report.update({"result": "failed unexpectedly", "reason": repr(exc),
                       "failure_type": type(exc).__name__, "exit_classification": 1})
    try:
        namespace["guard"]("trial outcome: "+label)
        report["outcome_resource_gate_passed"] = True
    except Exception as exc:
        report["prior_outcome"] = {key: report[key] for key in
                                   ("result", "reason", "failure_type", "exit_classification") if key in report}
        report.update({"result": "not completed: outcome resource gate", "reason": repr(exc),
                       "failure_type": "ResourceRefusal", "exit_classification": 75,
                       "outcome_resource_gate_passed": False})
    report["elapsed_seconds_from_suite_start"] = time.monotonic()-START
    return report


def run_suite():
    source = Path(__file__).read_text()
    original_hash = hashlib.sha256(source.encode()).hexdigest()
    criteria_hash = hashlib.sha256((HERE/"lib1_criteria_v2.md").read_bytes()).hexdigest()
    labels = ("baseline", "active_for_full", "inactive_roots")
    paths = {label: HERE/("lib1_check_v2_"+label+"_result.json") for label in labels}
    suite_path = HERE/"lib1_check_v2_result.json"
    for path in (*paths.values(), suite_path):
        if path.exists():
            raise FileExistsError("Refusing to overwrite "+str(path))
    original_line = "    return "+"norm(grouped, out_labels, allv, allv, 1)"
    if source.count(original_line) != 1:
        raise RuntimeError("Expected exactly one shared full-output return anchor")
    trials = {"baseline": capture_trial(globals(), "baseline", source,
                                        original_hash, criteria_hash, None)}
    substitutions = (
        ("active_for_full", "lam", "lam", "four_cycle_full_output_norm_exact", "four_cycle", "2"),
        ("inactive_roots", "lam", "allv", "overlap_full_output_norm_exact", "overlap_path", "4"),
    )
    checks = {"baseline_completed": trials["baseline"]["exit_classification"] == 0}
    for label, roots, active, required_assertion, witness, required_wrong_value in substitutions:
        if not checks["baseline_completed"]:
            trials[label] = {"trial": label, "result": "not run: baseline did not complete"}
            checks[label+"_rejected_at_required_assertion"] = False
            continue
        replacement = f"    return norm(grouped, out_labels, {roots}, {active}, 1)"
        modified = source.replace(original_line, replacement, 1)
        changes = [(a, b) for a, b in zip(source.splitlines(), modified.splitlines()) if a != b]
        if changes != [(original_line, replacement)]:
            raise RuntimeError("Mutation changed more than the specified return")
        namespace = {"__file__": str(Path(__file__).resolve()), "__name__": "lib1_b1_"+label}
        exec(compile(modified, str(Path(__file__).resolve())+"::"+label, "exec"), namespace)
        namespace["START"] = START  # One shared deadline, not a fresh budget per mutant.
        mutation = {"before": original_line.strip(), "after": replacement.strip(),
                    "changed_lines": 1, "required_assertion": required_assertion}
        trial = capture_trial(namespace, label, modified, original_hash, criteria_hash, mutation)
        trials[label] = trial
        checks[label+"_rejected_at_required_assertion"] = (
            trial.get("failure_type") == "AssertionError"
            and trial.get("reason") == required_assertion
            and trial.get("exit_classification") == 1
            and trial.get("outcome_resource_gate_passed") is True
            and trial["counts"].get("bounded_hole_full_norm") == 2184
            and trial.get("norm_witnesses", {}).get(witness, {}).get("computed", {}).get("output_full")
                == required_wrong_value)
    try:
        guard("entire sequential suite completion")
        checks["suite_resource_gate_passed"] = True
    except ResourceRefusal as exc:
        checks["suite_resource_gate_passed"] = False
        suite_resource_reason = str(exc)
    all_satisfied = all(checks.values())
    resource_refusal = (not checks["suite_resource_gate_passed"] or
                        any(r.get("exit_classification") == 75 for r in trials.values()))
    code = 0 if all_satisfied else (75 if resource_refusal else 1)
    suite = {"fix": "[R-fix 2026-10-29 B1]", "kind": "same-author finite repair checks; not independent review",
             "result": "completed; B1 baseline and actual mutation criteria satisfied" if all_satisfied
                       else "not completed: resource gate/deadline" if resource_refusal
                       else "failed: B1 acceptance criteria not satisfied",
             "exit_code": code, "acceptance": checks, "trials": trials,
             "trial_output_paths": {label: str(path) for label, path in paths.items()},
             "script_sha256": original_hash, "criteria_sha256": criteria_hash,
             "elapsed_seconds": time.monotonic()-START,
             "execution": "one invocation; baseline once, each compiled mutant once; sequential; no pools"}
    if not checks["suite_resource_gate_passed"]:
        suite["resource_reason"] = suite_resource_reason
    for label, path in paths.items():
        with path.open("x") as stream:
            stream.write(json.dumps(trials[label], indent=2)+"\n")
    data = json.dumps(suite, indent=2)+"\n"
    with suite_path.open("x") as stream:
        stream.write(data)
    print(data, end="")
    return code


if __name__ == "__main__":
    sys.exit(run_suite())
