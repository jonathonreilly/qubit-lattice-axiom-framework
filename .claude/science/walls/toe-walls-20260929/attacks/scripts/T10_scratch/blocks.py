"""Test C: G-invariant partitions (block systems) of the octahedral rotation group O (24 proper cubic rotations)
acting on orbits of directions: 6 axes, 8 vertices, 12 edges, free orbit (24).
Every invariant equivalence relation is a join of minimal ones E(x0,y); we build all minimal ones then close under join."""
import itertools, json
import numpy as np

def cube_rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i, p in enumerate(perm):
                M[i, p] = signs[i]
            if round(np.linalg.det(M)) == 1:
                mats.append(M)
    return mats

G = cube_rotations()
assert len(G) == 24

def orbit(v):
    pts = []
    for M in G:
        w = tuple(int(x) for x in M @ np.array(v))
        if w not in pts: pts.append(w)
    return pts

def act(M, w): return tuple(int(x) for x in M @ np.array(w))

def closure(pts, pairs):
    idx = {p: i for i, p in enumerate(pts)}
    parent = list(range(len(pts)))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[ra] = rb; return True
        return False
    for (x, y) in pairs:
        for M in G:
            union(idx[act(M, x)], idx[act(M, y)])
    cl = {}
    for i in range(len(pts)): cl.setdefault(find(i), []).append(i)
    return frozenset(frozenset(c) for c in cl.values())

def join(p1, p2, n):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for part in list(p1) + list(p2):
        part = list(part)
        for a in part[1:]:
            ra, rb = find(part[0]), find(a)
            if ra != rb: parent[ra] = rb
    cl = {}
    for i in range(n): cl.setdefault(find(i), []).append(i)
    return frozenset(frozenset(c) for c in cl.values())

def all_invariant_partitions(pts):
    x0 = pts[0]
    mins = {closure(pts, [(x0, y)]) for y in pts[1:]}
    allp = set(mins)
    changed = True
    while changed:
        changed = False
        for a in list(allp):
            for b in list(mins):
                j = join(a, b, len(pts))
                if j not in allp: allp.add(j); changed = True
    allp.add(frozenset(frozenset([i]) for i in range(len(pts))))  # identity
    return allp

res = {}
for name, v in [("axes(6)", (1, 0, 0)), ("vertices(8)", (1, 1, 1)), ("edges(12)", (1, 1, 0)), ("free(24)", (1, 2, 3))]:
    pts = orbit(v)
    parts = all_invariant_partitions(pts)
    counts = sorted(len(p) for p in parts)
    two_block = [p for p in parts if len(p) == 2]
    res[name] = dict(orbit_size=len(pts), n_invariant_partitions=len(parts), block_counts=counts, two_block_partitions=len(two_block))
    print(name, res[name])
json.dump(res, open("blocks_results.json", "w"), indent=1)
