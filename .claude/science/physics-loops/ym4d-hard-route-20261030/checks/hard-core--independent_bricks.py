#!/usr/bin/env python3
"""A region that is a union of tiles of a brick tiling has only good local patterns. Text 3.2, Lemma 3.2a.

Around a face of codimension d of the cell lattice there are 2^d cells, the vertices of Q_d. A partition of Q_d into subcubes
is a GUILLOTINE partition with distinct coordinates if it is the trivial one, or if some coordinate i splits Q_d into its two facets
and the facets carry guillotine partitions using coordinates that are pairwise disjoint from each other, and do not contain i.

Claims tested, by exhaustion, exact, for d = 2, 3, 4.
    (A) For every such partition and every union of its parts as the removed set, the kept set S is either empty or
        connected, with K(S) simply connected, and it is not a pattern of the bad table at d (the table of patterns.py, which is
        K(S) not simply connected, and at d = 4 also the antipodal pair of Text 3.2 below).
    (B) The same for the kept set intersected with every subcube of Q_d (a patch cut by a box).
    (C) The counts of parts: at most d + 1.
Criteria, written before the first run.
    PASS-A: no kept set of (A) is bad, and every one is connected.
    PASS-B: no kept set of (B) is bad, and every one is connected.
    PASS-C: every partition has at most d + 1 parts.
    FAIL otherwise, with the first failing partition printed. Then the proof in Text 3.2 is wrong.

(D) A construction test in d = 2, 3, where the whole lattice can be listed: two nested levels, cuts by the rule of Text 3.2 with
    a small residue table found by greedy colouring, L odd. Criterion PASS-D: at every vertex of the fine lattice, at most one cut piece
    in each coordinate touches it, every local partition is a guillotine one, and every tile of the coarse level is a
    union of tiles of the fine level. This only tests the bookkeeping of the construction, at small sizes; the proof is in the text.

Run under the numeric lock, nice, RSS checked against 2 GB.

First run, under a confirmed lock: PASS-A, PASS-B, PASS-C at d = 2, 3, 4 (7, 46, 485 partitions, 42, 590, 12882 unions, at most d + 1 parts).
FAIL-D as registered: the test cut the torus as an interval, so every box of a round had a wall at the seam x = 0, which is two walls in one coordinate at a vertex.
That is an error of the test, not of the rule: the rule cuts a circle. Fixed by closing the cuts up on the circle. Second run, under a confirmed lock: PASS-A, PASS-B, PASS-C unchanged, PASS-D (no non-guillotine vertex, at most d + 1 tiles at a vertex, nesting exact, at d = 2, L = 5, 7, and d = 3, L = 3).
"""
import importlib.util
import itertools
import pathlib
import random
import sys

HERE = pathlib.Path(__file__)
spec = importlib.util.spec_from_file_location("patterns", HERE.with_name("hard-core--independent_patterns.py"))
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)


def guillotine_partitions(coords):
    """All guillotine partitions of the cube on the coordinate list coords, as lists of parts.
    A part is a dict: coordinate -> fixed bit, for the coordinates that were cut on the way to it.
    Each tree uses each coordinate at most once in the whole tree."""
    coords = tuple(coords)
    yield [dict()]
    for i in coords:
        rest = [c for c in coords if c != i]
        # split the remaining coordinates between the two sides; a coordinate may go to neither
        for assignment in itertools.product((0, 1, 2), repeat=len(rest)):
            left = [c for c, a in zip(rest, assignment) if a == 0]
            right = [c for c, a in zip(rest, assignment) if a == 1]
            for pl in guillotine_partitions(left):
                for pr in guillotine_partitions(right):
                    parts = []
                    for p in pl:
                        q = dict(p)
                        q[i] = 0
                        parts.append(q)
                    for p in pr:
                        q = dict(p)
                        q[i] = 1
                        parts.append(q)
                    yield parts


def part_mask(part, d):
    m = 0
    for v in range(2**d):
        if all((v >> c & 1) == b for c, b in part.items()):
            m |= 1 << v
    return m


def connected(mask, d):
    if mask == 0:
        return True
    start = next(v for v in range(2**d) if mask >> v & 1)
    seen = 0
    stack = [start]
    while stack:
        x = stack.pop()
        if seen >> x & 1:
            continue
        seen |= 1 << x
        for i in range(d):
            y = x ^ (1 << i)
            if mask >> y & 1 and not seen >> y & 1:
                stack.append(y)
    return seen == mask


def subcube_masks(d):
    out = []
    for fixed in itertools.product((None, 0, 1), repeat=d):
        m = 0
        for v in range(2**d):
            if all(b is None or (v >> c & 1) == b for c, b in enumerate(fixed)):
                m |= 1 << v
        out.append(m)
    return out


def full_bad(d):
    bad, _ = pm.bad_table(d)
    bad = set(bad)
    if d == 4:
        # the antipodal pair removed with nothing else, Text 3.2
        full = 2**16 - 1
        for v in range(16):
            bad.add(full ^ (1 << v) ^ (1 << (15 - v)))
    return bad


def run_exact(d):
    bad = full_bad(d)
    subs = subcube_masks(d)
    seen_partitions = set()
    max_parts = 0
    n_sets = 0
    fail_a = fail_b = None
    for parts in guillotine_partitions(range(d)):
        masks = tuple(sorted(part_mask(p, d) for p in parts))
        if masks in seen_partitions:
            continue
        seen_partitions.add(masks)
        assert sum(bin(m).count("1") for m in masks) == 2**d
        max_parts = max(max_parts, len(masks))
        for r in range(2 ** len(masks)):
            kept = 0
            for j, m in enumerate(masks):
                if r >> j & 1:
                    kept |= m
            n_sets += 1
            if kept in bad or not connected(kept, d):
                fail_a = fail_a or (masks, kept)
            for s in subs:
                k2 = kept & s
                if k2 and (k2 in bad or not connected(k2, d)):
                    fail_b = fail_b or (masks, kept, s)
    pm.check_rss()
    print(f"d={d}: partitions={len(seen_partitions)}, unions={n_sets}, max parts={max_parts}", flush=True)
    print("PASS-A" if fail_a is None else f"FAIL-A {fail_a}")
    print("PASS-B" if fail_b is None else f"FAIL-B {fail_b}")
    print("PASS-C" if max_parts <= d + 1 else "FAIL-C")
    return fail_a is None and fail_b is None and max_parts <= d + 1


# ---------------------------------------------------------------- construction test, d = 2, 3


class Node:
    __slots__ = ("box", "depth", "residue", "children", "cuts")

    def __init__(self, box, depth):
        self.box = box  # list of (a, b), half-open in lattice units, torus coordinates unwrapped
        self.depth = depth  # the coordinate to be cut next; -1 for a leaf
        self.residue = None
        self.children = []
        self.cuts = []


def touches(b1, b2, side):
    """closed boxes on the torus of the given side per coordinate meet"""
    for (a1, e1), (a2, e2), n in zip(b1, b2, side):
        hit = False
        for shift in (-n, 0, n):
            if a1 <= e2 + shift and a2 + shift <= e1:
                hit = True
                break
        if not hit:
            return False
    return True


def build_level(parents, side, period, avoid_positions, rng):
    """Cut each parent box into tiles, coordinate d-1 first. Each node of one depth takes a residue differing from all touching nodes
    of that depth. avoid_positions: a list of (coordinate, position, box) of the coarser cut pieces."""
    d = len(side)
    current = [Node(list(p), d - 1) for p in parents]
    leaves = []
    for depth in range(d - 1, -1, -1):
        # greedy colouring of the touching graph of the nodes at this depth
        used = {}
        order = list(range(len(current)))
        for idx in order:
            forbidden = set()
            for jdx, res in used.items():
                if touches(current[idx].box, current[jdx].box, side):
                    forbidden.add(res)
            r = 0
            while r in forbidden:
                r += 1
            if r >= period:
                raise RuntimeError(f"period {period} too small at depth {depth}")
            used[idx] = r
            current[idx].residue = r
        nxt = []
        for node in current:
            a, b = node.box[depth]
            whole = (b - a == side[depth])  # the coordinate is still the whole circle: no seam, the cuts close up
            # cut positions strictly inside, by residue, deleting positions of touching coarser pieces
            cuts = [x for x in range(a + 1, b) if x % period == node.residue]
            if whole:
                cuts = [x for x in range(a, b) if x % period == node.residue]
            cuts2 = []
            for x in cuts:
                bad = False
                for (c, pos, cbox) in avoid_positions:
                    if c == depth and pos % side[depth] == x % side[depth] and touches(node.box, cbox, side):
                        bad = True
                        break
                if not bad:
                    cuts2.append(x)
            node.cuts = cuts2
            ends = [a] + cuts2 + [b]
            if whole:
                ends = cuts2 + [cuts2[0] + side[depth]]
            for i in range(len(ends) - 1):
                box = list(node.box)
                box[depth] = (ends[i], ends[i + 1])
                nxt.append(Node(box, depth - 1))
        current = nxt
    return [n.box for n in current]


def all_cut_pieces(leaves, side):
    """The faces of the leaves, by coordinate: returned as a dict (coordinate, position mod side) -> set of leaf indices with that wall."""
    pieces = {}
    for k, box in enumerate(leaves):
        for c, (a, b) in enumerate(box):
            for pos in (a, b):
                pieces.setdefault((c, pos % side[c]), set()).add(k)
    return pieces


def local_check(leaves, side):
    """At each lattice vertex: the cells around it, which tile each belongs to; the local partition must be a guillotine one with distinct coordinates."""
    d = len(side)
    owner = {}
    for k, box in enumerate(leaves):
        for x in itertools.product(*[range(a, b) for a, b in box]):
            owner[tuple(xi % n for xi, n in zip(x, side))] = k
    assert len(owner) == pm_prod(side), (len(owner), pm_prod(side))
    n_fail = 0
    worst = 0
    for x in itertools.product(*[range(n) for n in side]):
        cells = []
        for bits in range(2**d):
            y = tuple((xi - 1 + (bits >> c & 1)) % n for c, (xi, n) in enumerate(zip(x, side)))
            cells.append(owner[y])
        parts = {}
        for bits, o in enumerate(cells):
            parts.setdefault(o, 0)
            parts[o] |= 1 << bits
        worst = max(worst, len(parts))
        if not is_guillotine(sorted(parts.values()), list(range(d)), d):
            n_fail += 1
    return n_fail, worst


def pm_prod(side):
    p = 1
    for n in side:
        p *= n
    return p


def is_guillotine(masks, coords, d):
    """masks partition a subcube; decide whether it is a guillotine partition with distinct coordinates from the list coords"""
    if len(masks) == 1:
        return True
    union = 0
    for m in masks:
        union |= m
    for i in coords:
        left = [m for m in masks if all((v >> i & 1) == 0 for v in range(2**d) if m >> v & 1)]
        right = [m for m in masks if all((v >> i & 1) == 1 for v in range(2**d) if m >> v & 1)]
        if len(left) + len(right) != len(masks) or not left or not right:
            continue
        rest = [c for c in coords if c != i]
        # coordinates split between the sides: try all assignments
        for assignment in itertools.product((0, 1), repeat=len(rest)):
            cl = [c for c, a in zip(rest, assignment) if a == 0]
            cr = [c for c, a in zip(rest, assignment) if a == 1]
            if is_guillotine(left, cl, d) and is_guillotine(right, cr, d):
                return True
    return False


def run_construction(d, N1, L, period1, period0, seed):
    """Level 1: a torus of side N1 cut into tiles. Level 0: refine by L."""
    rng = random.Random(seed)
    side1 = tuple([N1] * d)
    torus1 = [[(0, N1)] * d]
    leaves1 = build_level(torus1, side1, period1, [], rng)
    # tiles of level 1 on the level-0 lattice
    side0 = tuple([N1 * L] * d)
    parents = [[(a * L, b * L) for a, b in box] for box in leaves1]
    avoid = []
    for box in parents:
        for c, (a, b) in enumerate(box):
            avoid.append((c, a, box))
            avoid.append((c, b, box))
    leaves0 = build_level(parents, side0, period0, avoid, rng)
    # nesting
    bad_nest = 0
    for box in parents:
        vol = pm_prod([b - a for a, b in box])
        inside = 0
        for f in leaves0:
            if all(a <= fa and fb <= b for (a, b), (fa, fb) in zip(box, f)):
                inside += pm_prod([fb - fa for fa, fb in f])
        if inside != vol:
            bad_nest += 1
    f1, w1 = local_check(leaves1, side1)
    f0, w0 = local_check(leaves0, side0)
    maxside = max(b - a for box in leaves0 for a, b in box)
    print(f"d={d}, N1={N1}, L={L}, periods {period1},{period0}: level 1 tiles {len(leaves1)}, level 0 tiles {len(leaves0)}, max side {maxside}; "
          f"non-guillotine vertices {f1}, {f0}; max parts {w1}, {w0}; bad nesting {bad_nest}", flush=True)
    return f1 == 0 and f0 == 0 and bad_nest == 0 and w0 <= d + 1 and w1 <= d + 1


def main():
    ok = True
    for d in (2, 3, 4):
        ok = run_exact(d) and ok
    pm.check_rss()
    ok2 = True
    for args in ((2, 24, 5, 8, 8, 1), (2, 24, 7, 8, 8, 2), (3, 24, 3, 12, 12, 3)):
        ok2 = run_construction(*args) and ok2
        pm.check_rss()
    print("PASS-D" if ok2 else "FAIL-D")
    print("ALL-EXACT-PASS" if ok else "EXACT-FAIL")


if __name__ == "__main__":
    main()
