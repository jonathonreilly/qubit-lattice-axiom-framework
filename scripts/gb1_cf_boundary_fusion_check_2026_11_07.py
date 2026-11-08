#!/usr/bin/env python3
"""Exact, sparse SU(2) coefficient/fusion certificate for the specified graph.

No workflow, specification, primary runner, or expected-result file is read.
Run under a fresh lab_ops numeric lease; AUDIT_TIMEOUT_SEC may override 85s.
Scientific arithmetic is integer or Fraction arithmetic throughout.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, prod
import os
from pathlib import Path
import platform
import resource
import signal
import sys
import time


ZERO = None
LINK_BASIS = [ZERO] + list(product(range(2), repeat=2))
AUDIT_TIMEOUT_SEC = 85
MEMORY_BYTES = 300_000_000
RSS_GUARD_BYTES = 270_000_000
CHECKS = 0


def peak_rss_bytes():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def set_bounds():
    timeout = int(os.environ.get("AUDIT_TIMEOUT_SEC", AUDIT_TIMEOUT_SEC))
    if not 1 <= timeout <= 90:
        raise ValueError("AUDIT_TIMEOUT_SEC must be in [1, 90]")
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise ValueError(f"{name}=1 is required")
    resource.setrlimit(resource.RLIMIT_CPU, (timeout, timeout))
    memory_limits = []
    for name in ("RLIMIT_DATA", "RLIMIT_AS"):
        try:
            resource.setrlimit(getattr(resource, name), (MEMORY_BYTES, MEMORY_BYTES))
            memory_limits.append(f"{name}={MEMORY_BYTES}")
        except (ValueError, OSError) as error:
            # macOS can reject AS/RSS limits; preflight requires an RSS watcher.
            memory_limits.append(f"{name}=unavailable({error})")
    started = time.monotonic()

    def guard(_sig, _frame):
        if time.monotonic() - started >= timeout:
            raise TimeoutError("wall-clock budget exceeded")
        if peak_rss_bytes() >= RSS_GUARD_BYTES:
            raise MemoryError("RSS safety guard exceeded")

    signal.signal(signal.SIGALRM, guard)
    signal.setitimer(signal.ITIMER_REAL, 0.05, 0.05)
    print(f"BOUNDS wall={timeout}s cpu={timeout}s {' '.join(memory_limits)} "
          f"RSS_guard={RSS_GUARD_BYTES} poll_seconds=0.05 threads=1")
    return started


def clean(d):
    return {k: v for k, v in d.items() if v}


def equal(label, actual, expected):
    global CHECKS
    if actual != expected:
        raise AssertionError(f"{label}: actual={actual!r} expected={expected!r}")
    CHECKS += 1


def reject(label, faulty, independent):
    try:
        equal(label, faulty, independent)
    except AssertionError:
        print(f"FAULT_REJECTED {label}: faulty={faulty} independent={independent}")
        return
    raise AssertionError(f"Fault survived: {label}")


def epsilon(a, b):
    return (a == 0 and b == 1) - (a == 1 and b == 0)


def split_at(vector, position):
    out = Counter()
    for key, coefficient in vector.items():
        token = key[position]
        pairs = [(ZERO, ZERO)] if token is ZERO else [
            ((token[0], k), (k, token[1])) for k in range(2)]
        for pair in pairs:
            out[key[:position] + pair + key[position + 1:]] += coefficient
    return clean(out)


def multiply_entry(vector, position, a, b):
    # The basis is {1, D_ab}, with norms 1 and 1/2, respectively.
    # P(D_ab D_cd) = epsilon_ac epsilon_bd / 2; no five-state matrix is built.
    out = Counter()
    for key, coefficient in vector.items():
        token = key[position]
        if token is ZERO:
            new, factor = (a, b), Fraction(1)
        else:
            new = ZERO
            factor = Fraction(epsilon(a, token[0]) * epsilon(b, token[1]), 2)
        out[key[:position] + (new,) + key[position + 1:]] += coefficient * factor
    return clean(out)


def path_entry(vector, a, b):
    # Tensor positions are [g2, g1], consistent with g2 g1.
    out = Counter()
    for k in range(2):
        term = multiply_entry(multiply_entry(vector, 1, k, b), 0, a, k)
        for key, value in term.items():
            out[key] += value
    return clean(out)


def inner(left, right):
    return sum((value * right.get(key, 0) * Fraction(1, 2) **
                sum(token is not ZERO for token in key)
                for key, value in left.items()), Fraction(0))


def electric(vector, position):
    return clean({key: value * (Fraction(3, 4) if key[position] is not ZERO else 0)
                  for key, value in vector.items()})


def cut_checks():
    vectors = [{(token,): Fraction(1)} for token in LINK_BASIS]
    for left in vectors:
        for right in vectors:
            equal("weighted Haar isometry", inner(split_at(left, 0), split_at(right, 0)),
                  inner(left, right))
    for vector in vectors:
        cut = split_at(vector, 0)
        equal("subdivision associativity", split_at(cut, 0), split_at(cut, 1))
        for a, b in product(range(2), repeat=2):
            equal("compressed holonomy intertwining", path_entry(cut, a, b),
                  split_at(multiply_entry(vector, 0, a, b), 0))
        for position in (0, 1):
            equal("each sublink Casimir", electric(cut, position),
                  split_at(electric(vector, 0), 0))
    # A genuine nonzero coefficient witnesses doubled unweighted energy.
    witness = split_at({((0, 0),): Fraction(1)}, 0)
    e_coarse = split_at(electric({((0, 0),): Fraction(1)}, 0), 0)
    fine_sum = {k: electric(witness, 0)[k] + electric(witness, 1)[k] for k in witness}
    equal("sum of two Casimirs", fine_sum, {k: 2 * v for k, v in e_coarse.items()})
    reject("unweighted fine energy equals coarse energy", fine_sum, e_coarse)
    print("CUT coefficient-basis Gram comparisons=25 holonomy entries=20 "
          "associativity inputs=5 per-link Casimir inputs=10")
    print("CUT range: j2=j1 in {0,1/2}, unique internal contraction, endpoint dimension=5")


VERTICES = tuple((x, y) for y in range(3) for x in range(3))
EDGES = tuple((v, w) for y in range(3) for x in range(3)
              for v in [(x, y)] for w in [(x + 1, y), (x, y + 1)]
              if w in VERTICES)
BOUNDARY = ((1, 0), (1, 1), (1, 2))
LEFT = tuple(e for e in EDGES if e[0][0] == 0)
MIDDLE = tuple(e for e in EDGES if e[0][0] == e[1][0] == 1)
RIGHT = tuple(e for e in EDGES if e not in LEFT and e not in MIDDLE)
REGION_A = LEFT + MIDDLE
REGION_B = RIGHT
LEFT_INTERIOR = tuple((0, y) for y in range(3))
RIGHT_INTERIOR = tuple((2, y) for y in range(3))


def half_fusion(n):
    reps = {0: 1}
    for _ in range(n):
        new = Counter()
        for q, multiplicity in reps.items():
            new[q + 1] += multiplicity
            if q:
                new[q - 1] += multiplicity
        reps = dict(new)
    return reps


def occupancy_decomposition(edges, projected, kept=(), clip_invariants=False):
    projected, kept = set(projected), tuple(kept)
    vertices = set(v for edge in edges for v in edge)
    out, records = Counter(), []
    for mask in range(1 << len(edges)):
        degrees = Counter(v for i, edge in enumerate(edges) if mask >> i & 1 for v in edge)
        factors = [half_fusion(degrees[v]).get(0, 0) for v in projected]
        if clip_invariants:
            factors = [min(1, value) for value in factors]
        multiplier = prod(factors)
        if not multiplier:
            continue
        multiplier *= 2 ** sum(degrees[v] for v in vertices - projected - set(kept))
        choices = [tuple(half_fusion(degrees[v]).items()) for v in kept]
        for selected in product(*choices):
            out[tuple(q for q, _ in selected)] += multiplier * prod(m for _, m in selected)
        records.append((mask, tuple(degrees[v] for v in kept), multiplier))
    return dict(out), records


def weight_character(edges, projected, kept=()):
    """Independent edge-weight enumeration and signed Haar constant terms.

    Each edge contributes 1+(z_u+z_u^-1)(z_v+z_v^-1).
    Integrate a closed projected variable with CT[(1-z^2) f], so powers
    0 and -2 have weights +1 and -1. Untracked vertices are evaluated at 1.
    """
    projected, kept = set(projected), tuple(kept)
    tracked = tuple(sorted(projected | set(kept)))
    index = {v: i for i, v in enumerate(tracked)}
    last = {v: max(i for i, e in enumerate(edges) if v in e) for v in projected}
    polynomial, peak = {(0,) * len(tracked): 1}, 1
    for i, (u, v) in enumerate(edges):
        expanded = Counter()
        for key, coefficient in polynomial.items():
            for a, b in ((0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                new = list(key)
                if u in index:
                    new[index[u]] += a
                if v in index:
                    new[index[v]] += b
                expanded[tuple(new)] += coefficient
        peak = max(peak, len(expanded))
        closed = [index[v] for v in projected if last[v] == i]
        reduced = Counter()
        for key, coefficient in expanded.items():
            new, factor = list(key), 1
            for p in closed:
                if key[p] == -2:
                    factor *= -1
                elif key[p] != 0:
                    factor = 0
                new[p] = 0
            reduced[tuple(new)] += factor * coefficient
        polynomial = clean(reduced)
    output = Counter()
    for key, value in polynomial.items():
        output[tuple(key[index[v]] for v in kept)] += value
    return clean(output), peak


def weight_to_irreps(weights, maxima):
    result = {}
    for q in product(*(range(n + 1) for n in maxima)):
        m = sum((-1) ** sum(bits) * weights.get(tuple(a + 2 * b for a, b in zip(q, bits)), 0)
                for bits in product((0, 1), repeat=len(q)))
        if m < 0:
            raise AssertionError(f"negative irrep multiplicity {q}: {m}")
        if m:
            result[q] = m
    return result


def dimension(reps):
    return sum(m * prod(q + 1 for q in label) for label, m in reps.items())


def tensor(left, right):
    out = Counter()
    for p, m in left.items():
        for q, n in right.items():
            for label in product(*(range(abs(a - b), a + b + 1, 2) for a, b in zip(p, q))):
                out[label] += m * n
    return dict(out)


def glue(left, right):
    return sum(m * right.get(q, 0) for q, m in left.items())


def show_reps(name, reps):
    print(f"REGION {name} dimension={dimension(reps)} sectors={len(reps)} "
          f"multiplicity_sum={sum(reps.values())}")
    for label, multiplicity in sorted(reps.items()):
        print(f"  q={label} multiplicity={multiplicity} "
              f"irrep_dimension={prod(q + 1 for q in label)}")


def face_cycle_masks():
    faces = []
    for x, y in product(range(2), repeat=2):
        boundary = {((x, y), (x + 1, y)), ((x, y + 1), (x + 1, y + 1)),
                    ((x, y), (x, y + 1)), ((x + 1, y), (x + 1, y + 1))}
        faces.append(sum(1 << i for i, edge in enumerate(EDGES) if edge in boundary))
    cycles = set()
    for choice in product((0, 1), repeat=len(faces)):
        mask = 0
        for include, face in zip(choice, faces):
            if include:
                mask ^= face
        cycles.add(mask)
    return cycles


def graph_checks(inject_fault):
    equal("edge partition", set(LEFT) | set(MIDDLE) | set(RIGHT), set(EDGES))
    equal("disjoint partition", len(LEFT) + len(MIDDLE) + len(RIGHT), len(EDGES))
    print("EDGES " + repr(list(enumerate(EDGES))))
    regions = {}
    for name, edges, interior in (("A", REGION_A, LEFT_INTERIOR),
                                  ("B", REGION_B, RIGHT_INTERIOR),
                                  ("L", LEFT, LEFT_INTERIOR),
                                  ("M", MIDDLE, ()), ("R", RIGHT, RIGHT_INTERIOR)):
        reps, records = occupancy_decomposition(edges, interior, BOUNDARY)
        weights, peak = weight_character(edges, interior, BOUNDARY)
        maxima = [sum(v in edge for edge in edges) for v in BOUNDARY]
        equal(f"{name} independent character decomposition", reps, weight_to_irreps(weights, maxima))
        equal(f"{name} character dimension", dimension(reps), sum(weights.values()))
        regions[name] = reps
        show_reps(name, reps)
        print(f"  OCCUPANCIES region={name} local_edge_order={edges}")
        print(f"  admissible_masks_degrees_multiplier={records} weight_frontier_peak={peak}")
    a, b, left, middle, right = (regions[k] for k in ("A", "B", "L", "M", "R"))
    equal("A=L tensor M", a, tensor(left, middle))
    equal("B=R", b, right)
    lm_r = tensor(tensor(left, middle), right)
    l_mr = tensor(left, tensor(middle, right))
    lr_m = tensor(tensor(left, right), middle)
    equal("full boundary associativity", lm_r, l_mr)
    equal("alternate boundary grouping", lm_r, lr_m)
    glued = glue(a, b)
    equal("singlet multiplicity by tensor decomposition", lm_r.get((0, 0, 0), 0), glued)
    full, records = occupancy_decomposition(EDGES, VERTICES)
    haar, peak = weight_character(EDGES, VERTICES)
    equal("all-vertex occupancy versus independent Haar weights", full, haar)
    equal("regional gluing versus all-vertex count", glued, full[()])
    cycles = face_cycle_masks()
    equal("complete even subgraphs from face basis", cycles, {mask for mask, _, _ in records})
    print(f"GLUING contributions={[(q, a[q] * m) for q, m in sorted(b.items())]}")
    print(f"FULL singlets={full[()]} Haar_frontier_peak={peak} even_subgraphs={len(cycles)}")
    for mask, _, multiplicity in records:
        selected = [i for i in range(len(EDGES)) if mask >> i & 1]
        center_degree = sum((1, 1) in EDGES[i] for i in selected)
        print(f"  FULL_CERT occupied_edges={selected} center_degree={center_degree} "
              f"invariant_multiplicity={multiplicity}")
    open_count, _ = occupancy_decomposition(EDGES, {(1, 1)})
    open_haar, peak = weight_character(EDGES, {(1, 1)})
    equal("open-boundary occupancy versus Haar", open_count, open_haar)
    star = sum(comb(4, n) * 2 ** n * (comb(n, n // 2) -
               (comb(n, n // 2 - 1) if n else 0)) for n in (0, 2, 4))
    equal("open-boundary star factorization", open_count[()], star * 5 ** 8)
    print(f"OPEN center_star_singlets={star} untouched_edges=8 dimension={open_count[()]} "
          f"Haar_frontier_peak={peak}")
    premature = a.get((0, 0, 0), 0) * b.get((0, 0, 0), 0)
    clipped, _ = occupancy_decomposition(EDGES, VERTICES, clip_invariants=True)
    lr = tensor(left, right)
    truncated = glue({q: m for q, m in lr.items() if max(q) <= 1}, middle)
    reject("prematurely project all regional boundary flux", premature, full[()])
    reject("discard local four-end invariant multiplicity", clipped[()], haar[()])
    reject("drop spin-one intermediate boundary channel in LR grouping", truncated, full[()])
    for bits in product((0, 1), repeat=3):
        retained = sum(a.get(q, 0) * m for q, m in b.items()
                       if all(not early or q[i] == 0 for i, early in enumerate(bits)))
        print(f"EARLY_PROJECT boundary_subset={bits} final_count={retained}")
    print(f"GROUPINGS LM_R={glue(a, right)} L_MR={glue(left, tensor(middle, right))} "
          f"LR_M={glue(lr, middle)} premature_each="
          f"{[tensor(x, y).get((0, 0, 0), 0) * z.get((0, 0, 0), 0) for x, y, z in [(left, middle, right), (middle, right, left), (left, right, middle)]]}")
    show_reps("LR", lr)
    if inject_fault == "drop-flux":
        equal("injected boundary fault must fail closed", premature, full[()])
    elif inject_fault == "drop-multiplicity":
        equal("injected multiplicity fault must fail closed", clipped[()], haar[()])
    elif inject_fault == "truncate-intermediate":
        equal("injected intermediate-spin fault must fail closed", truncated, full[()])


def main():
    started = set_bounds()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inject-fault", choices=("drop-flux", "drop-multiplicity", "truncate-intermediate"))
    args = parser.parse_args()
    print(f"SOURCE_SHA256 {sha256(Path(__file__).read_bytes()).hexdigest()}")
    print(f"RUNTIME Python={platform.python_version()} platform={platform.system()} "
          "arithmetic=integer/Fraction model_effort=inherited_not_exposed")
    print("HALF_FUSION " + repr({n: half_fusion(n) for n in range(5)}))
    cut_checks()
    graph_checks(args.inject_fault)
    print(f"TOTAL exact_equalities={CHECKS} failures=0")
    print(f"RESOURCES elapsed_seconds={time.monotonic() - started:.6f} peak_rss_bytes={peak_rss_bytes()}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, MemoryError, TimeoutError, ValueError, OSError) as error:
        print(f"CERTIFICATE_REJECTED {type(error).__name__}: {error}", file=sys.stderr)
        sys.exit(1)
