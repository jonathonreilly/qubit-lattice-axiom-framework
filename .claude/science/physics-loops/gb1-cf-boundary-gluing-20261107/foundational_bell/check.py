#!/usr/bin/env python3
"""Exact four-record Bell test; standalone replay, not a physical Bell experiment."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import argparse
import hashlib
import json
import os
import resource
import sys
import time

P, Q = (F(1), F(0)), (F(0), F(1))
ZERO = (F(0), F(0))
T = (F(10), F(10))
OFFSETS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FRAME_ROOT = (-10, -10, -10)
IDENTITY_AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
START = time.monotonic()
COUNTS = Counter()


def guard():
    assert time.monotonic() - START < 50, "wall guard"
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    assert rss < 250 * 1024**2, "RSS guard"


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def scalar(n):
    return (F(n), F(n))


def center(j):
    return (20 * 2**j, 0, 0)


def bank_index(h):
    return 1 + sum(bit * 2**(len(h) - k - 1) for k, bit in enumerate(h))


def probability(j, h, r):
    if j < 4:
        return F(1, 2)
    x, y, a = h
    return (1 + r * (-1)**(a + x * y)) / 2


def decode(m):
    p = (sum(m) - 5) / 2
    projector = tuple(v - 2 - p for v in m)
    if 0 <= p <= 1 and sum(projector) == 1 and all(v*v == v for v in projector):
        return p, projector
    return None


def menu(records, site):
    values = [records[add(site, d)] for d in OFFSETS if add(site, d) in records]
    programs = [decode(v) for v in values if decode(v) is not None]
    if T in values and len(programs) == 1:
        p, projector = programs[0]
        result = {projector: p, tuple(1-v for v in projector): 1-p}
    elif values:
        result = {v: F(n, len(values)) for v, n in Counter(values).items()}
    else:
        result = {ZERO: F(1)}
    assert sum(result.values()) == 1 and min(result.values()) >= 0
    return {v: p for v, p in result.items() if p}


def preparation(r, fault):
    records = {}
    for j in range(1, 5):
        c = center(j)
        records[add(c, (1, 0, 0))] = T
        records[add(c, (2, 0, 0))] = T
        for h in product((0, 1), repeat=j-1):
            p = probability(j, h, r)
            value = (3+p, 2+p)
            l = bank_index(h)
            records[add(c, (-3*l, 3, 0))] = value
            records[add(c, (-3*l, 3, 1))] = value
    for v, displacements in [(20, [(0,0,0),(-1,0,0)]),
                             (21, [(1,0,0),(2,0,0)]),
                             (22, [(0,2,0),(1,2,0)]),
                             (23, [(0,0,3),(1,0,3)])]:
        for d in displacements:
            records[add(FRAME_ROOT, d)] = scalar(v)
    assert len(records) == 46
    if fault == "missing-buddy":
        del records[add(center(1), (-3, 3, 1))]
    return records


def coordinates(records):
    roots = [s for s, v in records.items() if v == scalar(20)
             and any(records.get(add(s, d)) == scalar(21) for d in OFFSETS)]
    assert len(roots) == 1, "frame root must be unique"
    root = roots[0]
    first = [d for d in OFFSETS if records.get(add(root, d)) == scalar(21)]
    assert len(first) == 1
    axes = [first[0]]
    for value, length in [(22, 2), (23, 3)]:
        sites = [s for s, v in records.items() if v == scalar(value)]
        nearest = min(sites, key=lambda s: dot(sub(s, root), sub(s, root)))
        delta = sub(nearest, root)
        assert all(v % length == 0 for v in delta)
        axes.append(tuple(v // length for v in delta))
    assert all(dot(axes[i], axes[j]) == int(i == j) for i in range(3) for j in range(3))
    canonical = {add(FRAME_ROOT, tuple(dot(sub(s, root), a) for a in axes)): v
                 for s, v in records.items()}
    return canonical, root, tuple(axes)


def to_world(c, root, axes):
    delta = sub(c, FRAME_ROOT)
    return add(root, tuple(sum(delta[i]*axes[i][k] for i in range(3)) for k in range(3)))


def transition(records, fault=None):
    canonical, root, axes = coordinates(records)
    assert sum(v == T for v in canonical.values()) == 8
    h = []
    for j in range(1, 5):
        c = center(j)
        if c in canonical:
            assert canonical[c] in (P, Q)
            h.append(int(canonical[c] == Q))
            continue
        selected = list(h)
        if fault == "ignore-first-setting" and j == 4:
            selected[0] = 0
        l = bank_index(selected)
        path = [add(c, (-3*l, y, 0)) for y in (2, 1, 0)]
        path += [add(c, (x, 0, 0)) for x in range(-3*l+1, 0)]
        for s in path:
            if s not in canonical:
                return to_world(s, root, axes), "program", tuple(h)
        return to_world(c, root, axes), "data", tuple(h)
    return None, "terminal", tuple(h)


def supported(records, sites):
    for s in sites:
        if s in records:
            assert menu(records, s).get(records[s], 0) > 0, ("old record lost support", s)
            COUNTS["support_checks"] += 1


def replay(r, fault):
    initial = preparation(r, fault)
    supported(initial, initial)
    work = [(initial, F(1))]
    terminal = defaultdict(F)
    snapshots = {"initial": initial}
    max_records = len(initial)
    states = appends = 0
    while work:
        guard()
        records, weight = work.pop()
        states += 1
        site, kind, history = transition(records, fault)
        if len(history) == 2 and "after-settings" not in snapshots:
            snapshots["after-settings"] = records
        if site is None:
            terminal[history] += weight
            snapshots["terminal"] = records
            supported(records, records)
            continue
        assert site not in records
        m = menu(records, site)
        if kind == "data":
            assert set(m) <= {P, Q}, "fixed first target must form a data content"
        else:
            assert len(m) == 1 and next(iter(m.values())) == 1, "routing is deterministic"
        for value, p in m.items():
            new = dict(records)
            new[site] = value
            supported(new, [site] + [add(site, d) for d in OFFSETS])
            assert all(new[s] == v for s, v in records.items()), "record permanence"
            appends += 1
            max_records = max(max_records, len(new))
            work.append((new, weight*p))
    assert sum(terminal.values()) == 1
    for x, y, a, b in product((0, 1), repeat=4):
        expected = (1+r*(-1)**(a+b+x*y))/16
        assert terminal[(x,y,a,b)] == expected, ("cylinder mismatch", r, x,y,a,b)
    correlators = []
    for x,y in product((0,1), repeat=2):
        setting_mass = sum(terminal[(x,y,a,b)] for a,b in product((0,1), repeat=2))
        assert setting_mass == F(1,4), "independent setting probabilities"
        for a in (0,1):
            assert sum(terminal[(x,y,a,b)] for b in (0,1))/setting_mass == F(1,2)
        for b in (0,1):
            assert sum(terminal[(x,y,a,b)] for a in (0,1))/setting_mass == F(1,2)
        correlators.append(sum((-1)**(a+b)*terminal[(x,y,a,b)] for a,b in product((0,1), repeat=2))/setting_mass)
    score = abs(sum(correlators[:3])-correlators[3])
    assert score == 4*abs(r)
    assert max_records <= 103
    return {"r":str(r), "S":str(score), "correlators":list(map(str,correlators)),
            "replayed_states":states, "appends":appends, "max_records":max_records,
            "positive_cylinders":sum(p>0 for p in terminal.values())}, snapshots


def rotations():
    for perm in permutations(range(3)):
        parity = (-1)**sum(perm[i] > perm[j] for i in range(3) for j in range(i+1,3))
        for signs in product((-1,1), repeat=3):
            if parity*signs[0]*signs[1]*signs[2] == 1:
                yield tuple(tuple(signs[i]*int(k==perm[i]) for k in range(3)) for i in range(3))


def covariance(snapshots):
    count = 0
    translation = (7, -13, 4)
    for axes in rotations():
        transform = lambda s: add(translation, tuple(sum(s[i]*axes[i][k] for i in range(3)) for k in range(3)))
        for records in snapshots.values():
            transformed = {transform(s):v for s,v in records.items()}
            s, kind, h = transition(records)
            q, kind2, h2 = transition(transformed)
            assert (kind,h) == (kind2,h2)
            assert q == (transform(s) if s is not None else None)
            if s is not None:
                assert menu(records,s) == menu(transformed,q)
            supported(transformed, transformed)
            count += 1
    assert count == 72
    return count


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def plus(a,b,sign=1):
    return [[x+sign*y for x,y in zip(row,other)] for row,other in zip(a,b)]


def scale(a,s):
    return [[s*x for x in row] for row in a]


def kron(a,b):
    return [[x*y for x in ar for y in br] for ar in a for br in b]


def standard_bounds():
    classical = []
    for a0,a1,b0,b1 in product((-1,1),repeat=4):
        classical.append(a0*b0+a0*b1+a1*b0-a1*b1)
    assert set(classical) == {-2,2}
    z,x,i = [[1,0],[0,-1]], [[0,1],[1,0]], [[1,0],[0,1]]
    bp,bm = plus(z,x),plus(z,x,-1)  # actual B operators divide these by sqrt2
    d = plus(plus(kron(z,bp),kron(z,bm)),plus(kron(x,bp),kron(x,bm),-1))
    comm_a = plus(matmul(z,x),matmul(x,z),-1)
    comm_b = scale(plus(matmul(bp,bm),matmul(bm,bp),-1),F(1,2))
    assert scale(matmul(d,d),F(1,2)) == plus(scale(kron(i,i),4),kron(comm_a,comm_b),-1)
    v = [[1],[0],[0],[1]]  # Phi+ is v/sqrt2
    assert matmul(d,v) == scale(v,4)  # C=D/sqrt2; expectation 2sqrt2
    scaled_correlators=[]
    for a,b in [(z,bp),(z,bm),(x,bp),(x,bm)]:
        value=matmul([[1,0,0,1]],matmul(kron(a,b),v))[0][0]/F(2)
        scaled_correlators.append(value)
    assert scaled_correlators == [1,1,1,-1]
    return {"local_vertices":16,"local_vertex_scores":sorted(set(classical)),
            "quantum_square_identity":"exact","quantum_S":"2sqrt2",
            "quantum_E_times_sqrt2":list(map(str,scaled_correlators))}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--fault",choices=["missing-buddy","ignore-first-setting"])
    args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(55,60))
    for name in ["OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS"]:
        assert os.environ.get(name) == "1", name
    rows=[]
    for r in map(F, [0,F(1,2),F(3,4),1,-1]):
        row,snapshots=replay(r,args.fault)
        rows.append(row)
        if r == F(3,4):
            covariance_checks=covariance(snapshots)
    result={"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "status":"ok","model":"four-event diagonal specialization of existing program theorem",
            "examples":rows,"support_checks":COUNTS["support_checks"],
            "spatial_covariance_snapshots":covariance_checks,"standard_comparators":standard_bounds(),
            "interpretation":"exact conditional model test; no physical spacelike implementation",
            "N5":{"per_element":"rational diagonal program decoding and binary probabilities checked",
                  "per_site":"complete six-neighbor menus and occupied-site support checked",
                  "per_mode":"checked and not executed: no propagating-mode claim",
                  "per_block":"four-record cylinders and standard 4x4 Bell algebra checked",
                  "lattice_wide":"checked and not executed: finite apparatus on Z3, not an infinite dynamics simulation"},
            "elapsed_seconds":time.monotonic()-START,
            "max_rss_host_units":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
