#!/usr/bin/env python3
"""Exact certificates for a supplied coarse SU(2) code on native site qubits.

No giant tensor product is constructed. General phase separation and operator
extension require the accompanying proof. Mutations must exit unsuccessfully.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

AUDIT_TIMEOUT_SEC = 60
CHECKS = 0
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ORIGIN = (0, 0, 0)
SIGNS = (1, -1, -1, -1, 1)


def rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def bounds():
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise RuntimeError(f"{name}=1 required")
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    started = time.monotonic()

    def guard(_sig, _frame):
        if time.monotonic() - started > 60:
            raise TimeoutError("60-second wall limit")
        if rss() >= 270_000_000:
            raise MemoryError("270 MB RSS guard")

    signal.signal(signal.SIGALRM, guard)
    signal.setitimer(signal.ITIMER_REAL, 0.05, 0.05)
    print("BOUNDS cpu=60s wall=60s RSS_guard=270000000 poll=0.05s threads=1")
    return started


def eq(label, actual, expected):
    global CHECKS
    if actual != expected:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")
    CHECKS += 1


def clean(a):
    return {key: value for key, value in a.items() if value}


def mul(a, b):
    out = {}
    for (i, k), x in a.items():
        for (k2, j), y in b.items():
            if k == k2:
                out[i, j] = out.get((i, j), F(0)) + x * y
    return clean(out)


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
    return clean(out)


def outer(a, b):
    return {(i, j): F(x * y, 2) for i, x in a.items() for j, y in b.items()}


def reverse_bits(a):
    return int(f"{a:04b}"[::-1], 2)


def link_checks(fault):
    # Columns below have norm sqrt(2); J is these columns divided by sqrt(2).
    cols = [{8: 1, 1: 1}, {8: 1, 1: -1}, {4: 1, 2: -1},
            {12: 1, 3: -1}, {4: 1, 2: 1}]
    if fault == "reverse-sign":
        cols[3] = {12: 1, 3: 1}
    if fault == "include-quiescent":
        cols[0] = {0: 1, 15: 1}
    for i, a in enumerate(cols):
        for j, b in enumerate(cols):
            eq("orthonormal columns", sum(x * b.get(k, 0) for k, x in a.items()),
               2 * (i == j))
        reflected = {reverse_bits(k): x for k, x in a.items()}
        eq("geometric reversal", reflected, {k: SIGNS[i] * x for k, x in a.items()})
        eq("quiescent exclusion", a.get(0, 0), 0)
    units = {(i, j): outer(cols[i], cols[j]) for i in range(5) for j in range(5)}
    for i, j, k, ell in product(range(5), repeat=4):
        eq("corner matrix-unit product", mul(units[i, j], units[k, ell]),
           units[i, ell] if j == k else {})
    q = {}
    for i in range(5):
        q = add(q, units[i, i])
    eq("code projector", mul(q, q), q)
    eq("projector rank by trace", sum(x for (i, j), x in q.items() if i == j), F(5))
    eq("projector reversal", {(reverse_bits(i), reverse_bits(j)): x for (i, j), x in q.items()}, q)
    print("LINK " + json.dumps({"native_qubits": 4, "code_rank": 5,
                               "inversion_eigenvalues": SIGNS,
                               "matrix_unit_products": 5**4,
                               "quiescent_orthogonal": True}))


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(k, a):
    return tuple(k * x for x in a)


def residue(a):
    return tuple(x % 5 for x in a)


def interior(v, d):
    return tuple(plus(v, scale(t, d)) for t in range(1, 5))


def active_at(point, phase):
    return sum((x - p) % 5 != 0 for x, p in zip(point, phase)) == 1


def rotations():
    out = []
    for perm in permutations(range(3)):
        parity = (-1)**sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                out.append((perm, signs))
    return out


def rotate(r, v):
    perm, signs = r
    return tuple(signs[i] * v[perm[i]] for i in range(3))


def geometry_checks(fault):
    phases = set(product(range(5), repeat=3))
    if fault == "preferred-phase":
        phases = {ORIGIN}
    for a in AXES:
        eq("unit translation closure", {residue(plus(p, a)) for p in phases}, phases)
    rs = rotations()
    eq("proper rotation census", len(rs), 24)
    for r in rs:
        eq("rotation phase closure", {residue(rotate(r, p)) for p in phases}, phases)
        for direction in AXES:
            rd = rotate(r, direction)
            axis = next(i for i, x in enumerate(rd) if x)
            positive = rd[axis] > 0
            anchor = ORIGIN if positive else scale(-5, AXES[axis])
            actual = tuple(rotate(r, x) for x in interior(ORIGIN, direction))
            target = interior(anchor, AXES[axis])
            eq("oriented geometric code support", actual, target if positive else target[::-1])
    cells = set(product(range(5), repeat=3))
    eq("active qubits per coarse cell", sum(active_at(x, ORIGIN) for x in cells), 12)
    separation = []
    for q in sorted(phases - {ORIGIN}):
        witnesses = [i for i, d in enumerate(AXES)
                     if all(not active_at(x, ORIGIN) for x in interior(q, d))]
        if not witnesses:
            raise AssertionError(f"missing spectator-edge witness at phase {q}")
        separation.append({"phase": q, "axis": witnesses[0]})
    eq("all nontrivial phase differences", len(separation), 124)
    fine_size = 15
    allocated = []
    for z in product(range(3), repeat=3):
        v = scale(5, z)
        for d in AXES:
            allocated.extend(tuple(a % fine_size for a in x) for x in interior(v, d))
    eq("disjoint link allocation on 15-cubed torus", len(set(allocated)), len(allocated))
    eq("torus active count", len(allocated), 4 * 3 * 3**3)
    star = {x for d in AXES for sign in (-1, 1) for x in interior(ORIGIN, scale(sign, d))}
    eq("six disjoint detector blocks", len(star), 24)
    for r in rs:
        eq("detector geometric invariance", {rotate(r, x) for x in star}, star)
    # Independent coordinate formula for an anchored electric/plaquette seed.
    seed = set(star)
    for i in range(3):
        seed.update(interior(ORIGIN, AXES[i]))
        for j in range(i+1, 3):
            seed.update(interior(ORIGIN, AXES[j]))
            seed.update(interior(scale(5, AXES[i]), AXES[j]))
            seed.update(interior(scale(5, AXES[j]), AXES[i]))
    radius = max(sum(abs(a) for a in x) for x in seed)
    diameter = max(sum(abs(a-b) for a, b in zip(x, y)) for x in seed for y in seed)
    eq("seed l1 radius", radius, 9)
    if diameter > 18:
        raise AssertionError("support exceeds the proved diameter bound")
    print("GEOMETRY " + json.dumps({"phases": len(phases), "rotations": len(rs),
           "active_per_cell": 12, "spectators_per_cell": 113,
           "torus_native_qubits": fine_size**3, "torus_active_qubits": len(allocated),
           "detector_qubits": len(star), "seed_l1_radius": radius,
           "seed_l1_diameter": diameter}))
    print("PHASE_SEPARATION " + json.dumps(separation, separators=(",", ":")))


def gf2_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            key = row.bit_length() - 1
            if key not in pivots:
                pivots[key] = row
                break
            row ^= pivots[key]
    return len(pivots)


def graph_certificate(n, periodic):
    vertices = list(product(range(n), repeat=3))
    indexes = {v: i for i, v in enumerate(vertices)}
    edges = []
    for v in vertices:
        for axis in range(3):
            if periodic or v[axis]+1 < n:
                w = list(v)
                w[axis] = (w[axis]+1) % n
                edges.append((indexes[v], indexes[tuple(w)]))
    rows = [0] * len(vertices)
    for k, (v, w) in enumerate(edges):
        rows[v] ^= 1 << k
        rows[w] ^= 1 << k
    rank = gf2_rank(rows)
    eq("connected incidence rank", rank, len(vertices)-1)
    cycles = len(edges)-rank
    return {"n": n, "periodic": periodic, "V": len(vertices), "E": len(edges),
            "incidence_rank": rank, "physical_dimension_lower_bound": 1 << cycles,
            "same_site_count_qubit_dimension": 1 << len(vertices), "cycle_dimension": cycles}


def capacity_checks():
    # Multiplicity of spin zero by successive spin-half fusion, not a stored table.
    multiplicities = {0: 1}
    singlets = []
    for degree in range(7):
        if degree % 2 == 0:
            singlets.append(multiplicities.get(0, 0))
        nxt = {}
        for twice_j, count in multiplicities.items():
            for out in (twice_j-1, twice_j+1):
                if out >= 0:
                    nxt[out] = nxt.get(out, 0) + count
        multiplicities = nxt
    if not all(m > 0 for m in singlets):
        raise AssertionError("an even occupied degree has no invariant")
    print("EVEN_VERTEX_SINGLET_MULTIPLICITIES " + json.dumps(singlets))
    for periodic in (False, True):
        certificate = graph_certificate(3, periodic)
        if certificate["physical_dimension_lower_bound"] <= certificate["same_site_count_qubit_dimension"]:
            raise AssertionError("declared finite capacity witness did not separate")
        print("CAPACITY " + json.dumps(certificate, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inject-fault", choices=("reverse-sign", "include-quiescent", "preferred-phase"))
    args = parser.parse_args()
    started = bounds()
    print("SOURCE_SHA256 " + sha256(Path(__file__).read_bytes()).hexdigest())
    link_checks(args.inject_fault)
    geometry_checks(args.inject_fault)
    capacity_checks()
    print("per_element: exact four-qubit matrix units preserve all five link states and inversion.")
    print("per_site: one M2 factor per native site is used under supplied tensor composition.")
    print("per_mode: checked and not executed - no momentum, spectral, or continuum mode claim.")
    print("per_block: all 125 phase residues and all 24 proper rotations are exhausted exactly.")
    print("lattice_wide: finite certificates support the general local proof; no full infinite tensor matrix is built.")
    print(f"TOTAL: PASS={CHECKS} FAIL=0")
    print(json.dumps({"seconds": time.monotonic()-started, "peak_rss_bytes": rss()}))


if __name__ == "__main__":
    main()
