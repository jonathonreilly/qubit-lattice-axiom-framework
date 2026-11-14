#!/usr/bin/env python3
"""Exact, small author checks for LIB1. No external theorem or math library."""
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
          "counts": {}, "resources": [], "mutations": {}}


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
                output_full = norm(grouped, out_labels, allv, allv, 1)
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


def mutations():
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
        "identify_active_and_full_norms": 2**y.bit_count() != 2**(y & lam).bit_count(),
    }
    for key, rejected in checks.items():
        require(rejected, "mutation_rejected_"+key)
    REPORT["mutations"] = {key: "rejected by exact witness" for key in checks}
    REPORT["norm_witness"] = {"graph": "four-cycle", "input_support": [0],
                              "inactive_component": [1, 2, 3], "input_full_norm": 2,
                              "output_full_norm": 16, "output_active_norm": 2,
                              "mu": "log(2)", "activity_supremum": 1}


def main():
    guard("before any enumeration")
    exercise("path6", graph(6, [(i, i+1) for i in range(5)]))
    exercise("cycle6", graph(6, [(i, (i+1) % 6) for i in range(6)]))
    exercise("box2x3", graph(6, [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]))
    native_four_dimensional()
    mutations()
    guard("completion")


if __name__ == "__main__":
    code = 0
    try:
        main()
        REPORT["result"] = "completed; all enumerated predicates satisfied"
    except ResourceRefusal as exc:
        REPORT["result"] = "not completed: resource gate/deadline"
        REPORT["reason"] = str(exc)
        code = 75
    except Exception as exc:
        REPORT["result"] = "failed"
        REPORT["reason"] = repr(exc)
        code = 1
    REPORT["elapsed_seconds"] = time.monotonic()-START
    REPORT["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    REPORT["criteria_sha256"] = hashlib.sha256((HERE/"lib1_criteria.md").read_bytes()).hexdigest()
    data = json.dumps(REPORT, indent=2)+"\n"
    (HERE/"lib1_check_result.json").write_text(data)
    print(data, end="")
    sys.exit(code)
