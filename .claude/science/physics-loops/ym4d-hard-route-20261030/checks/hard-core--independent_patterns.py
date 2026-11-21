#!/usr/bin/env python3
"""Local patterns of a union of cells, for Text 3.2 and Lemma 7 of the library, parts/hard-core--independent.md.

A reader found that a critical Sobolev bound fails near two removed cells that touch along an edge, offset (1, 1, 1, 0): the
six cells around that edge form a ring with no plaquette across it, so a field of small energy can carry a holonomy
of order one around a unit loop, for the whole length of the edge. This script answers two questions by exhaustion or
by experiment. No float enters except in the rank over a prime field, which is exact.

Local complex. Around a face of the cell complex of codimension d there are 2^d cells, the vertices of the cube Q_d. For a
set S of kept cells, K(S) has vertices S, an edge for each pair of kept cells that are face adjacent, and a square for each
2-face of Q_d with all four vertices kept. It is what the lattice sees near that face: a link needs two face-adjacent cells,
and a plaquette four cells around a codimension-2 face.

Question 1 (exhaustion). For d = 2, 3, 4, which S have a component of K(S) with non-trivial H_1, over F_2 and F_3?
Pre-registered expectation, by hand on the octahedron for d = 3: exactly the complements of an antipodal pair of Q_3.
    PASS-Q3: exactly that. FAIL-Q3: anything else, and then the hand argument is wrong.
For d = 4 there is no expectation; the output is the list of classes, with the size of the smallest removed set.
A pattern with H_1 = 0 could still have non-trivial pi_1 in principle. The script checks simple connectivity by adding
squares to a spanning tree: it reports any pattern where this greedy elimination does not kill all generators.
    PASS-PI1: no such pattern, among those with H_1 = 0.

Question 2 (experiment). The closure of a set of removed cells: while some face of codimension 3 or 4 has a bad pattern,
remove all the cells around it. Is the closure bounded by a constant times the initial set? On a torus Z^4 of side N, with
removed sets drawn at random at several densities, and structured sets (diagonal chains and sheets), and a hill climb on the
ratio from the random sets.
    PASS-RATIO: ratio |closure| / |initial| at most 100 on every run, and max sup distance from the initial set at most 4.
    FAIL-RATIO: some ratio above 100 at low density, density being what would make the fill rule useless for Theorem 4.2.
    The experiment cannot prove a bound; it can only fail to break it. N small is a limitation.

Result, under a confirmed lock: PASS-Q3, PASS-PI1, 8652 bad patterns for d = 4 in 60 classes, the smallest removed set of size 3.
PASS-RATIO: worst ratio 22.44 (hill climb at side 7), distance at most 2 where computed. At densities above about 0.03 the closure
fills most of a small torus, so these ratios are capped by 1 / density.

Run under the numeric lock, nice, RSS checked against 2 GB.
"""
import itertools
import random
import resource
import sys

RSS_LIMIT_BYTES = 2 * 1024**3


def check_rss():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT_BYTES:
        print("ABORT rss")
        sys.exit(3)


def rank_mod_p(rows, ncols, p):
    rows = [r[:] for r in rows]
    rank = 0
    for col in range(ncols):
        piv = None
        for i in range(rank, len(rows)):
            if rows[i][col] % p:
                piv = i
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], p - 2, p)
        rows[rank] = [(x * inv) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % p:
                f = rows[i][col]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def complex_of(mask, d):
    """vertices, edges (a < b), squares as 4-cycles of edge indices with signs."""
    verts = [v for v in range(2**d) if mask >> v & 1]
    vset = set(verts)
    edges = {}
    for v in verts:
        for i in range(d):
            w = v ^ (1 << i)
            if w in vset and v < w:
                edges[(v, w)] = len(edges)
    squares = []
    for v in verts:
        for i, j in itertools.combinations(range(d), 2):
            if v >> i & 1 or v >> j & 1:
                continue
            a, b, c = v ^ (1 << i), v ^ (1 << j), v ^ (1 << i) ^ (1 << j)
            if a in vset and b in vset and c in vset:
                squares.append(((v, a), (a, c), (b, c), (v, b)))
    return verts, edges, squares


def components(verts, edges):
    par = {v: v for v in verts}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for (a, b) in edges:
        par[find(a)] = find(b)
    return len({find(v) for v in verts}), find


def h1_rank(mask, d, p):
    verts, edges, squares = complex_of(mask, d)
    if not verts:
        return 0
    ne = len(edges)
    ncomp, _ = components(verts, edges)
    rank_d1 = len(verts) - ncomp
    if not squares:
        return ne - rank_d1
    rows = []
    for sq in squares:
        row = [0] * ne
        (e1, e2, e3, e4) = sq
        row[edges[e1]] = 1
        row[edges[e2]] = 1
        row[edges[e3]] = p - 1
        row[edges[e4]] = p - 1
        rows.append(row)
    rank_d2 = rank_mod_p(rows, ne, p)
    return ne - rank_d1 - rank_d2


def pi1_trivial(mask, d):
    """Greedy: edges in a spanning forest are trivial; a square with three trivial edges makes the fourth trivial."""
    verts, edges, squares = complex_of(mask, d)
    if not verts:
        return True
    par = {v: v for v in verts}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    trivial = set()
    for e in edges:
        a, b = find(e[0]), find(e[1])
        if a != b:
            par[a] = b
            trivial.add(e)
    changed = True
    while changed:
        changed = False
        for sq in squares:
            unk = [e for e in sq if e not in trivial]
            if len(unk) == 1:
                trivial.add(unk[0])
                changed = True
    return len(trivial) == len(edges)


def bad_table(d):
    bad = set()
    pi_fail = []
    for mask in range(2 ** (2**d)):
        r2 = h1_rank(mask, d, 2)
        r3 = h1_rank(mask, d, 3)
        if r2 or r3:
            bad.add(mask)
        elif not pi1_trivial(mask, d):
            pi_fail.append(mask)
    return bad, pi_fail


def canon(mask, d):
    best = None
    size = 2**d
    for perm in itertools.permutations(range(d)):
        for flip in range(size):
            m = 0
            for v in range(size):
                if mask >> v & 1:
                    w = 0
                    for i in range(d):
                        if v >> perm[i] & 1:
                            w |= 1 << i
                    m |= 1 << (w ^ flip)
            if best is None or m < best:
                best = m
    return best


def closure(cells, N, bad3, bad4):
    """cells: set of removed cells in Z_N^4. Faces: edges (three transverse axes) and vertices."""
    cells = set(cells)
    passes = 0
    while True:
        add = set()
        cand_vertices = set()
        for c in cells:
            for sh in itertools.product((0, 1), repeat=4):
                cand_vertices.add(tuple((c[i] + sh[i]) % N for i in range(4)))
        for v in cand_vertices:
            around = [tuple((v[i] - 1 + b[i]) % N for i in range(4)) for b in itertools.product((0, 1), repeat=4)]
            mask = 0
            for k, b in enumerate(itertools.product((0, 1), repeat=4)):
                idx = b[0] | b[1] << 1 | b[2] << 2 | b[3] << 3
                if around[k] not in cells:
                    mask |= 1 << idx
            if mask in bad4:
                add.update(around)
                continue
            # edges along each axis through the cell column at v
            for axis in range(4):
                others = [i for i in range(4) if i != axis]
                for tcell in (v[axis], (v[axis] - 1) % N):
                    ar = []
                    m3 = 0
                    for b in itertools.product((0, 1), repeat=3):
                        c2 = [0] * 4
                        c2[axis] = tcell
                        for j, i in enumerate(others):
                            c2[i] = (v[i] - 1 + b[j]) % N
                        c2 = tuple(c2)
                        ar.append(c2)
                        idx = b[0] | b[1] << 1 | b[2] << 2
                        if c2 not in cells:
                            m3 |= 1 << idx
                    if m3 in bad3:
                        add.update(ar)
        add -= cells
        if not add:
            return cells, passes
        cells |= add
        passes += 1


def sup_dist(a, b, N):
    return max(min((a[i] - b[i]) % N, (b[i] - a[i]) % N) for i in range(4))


def max_distance(init, final, N):
    worst = 0
    init = list(init)
    for c in final:
        d = min(sup_dist(c, s, N) for s in init)
        worst = max(worst, d)
    return worst


def main():
    bad2, pi2 = bad_table(2)
    bad3, pi3 = bad_table(3)
    print(f"d=2 bad patterns: {len(bad2)}, pi1 unresolved: {len(pi2)}", flush=True)
    print(f"d=3 bad patterns: {len(bad3)}, pi1 unresolved: {len(pi3)}", flush=True)
    expected = set()
    for v in range(8):
        expected.add(255 ^ (1 << v) ^ (1 << (7 - v)))
    print("PASS-Q3" if bad3 == expected else f"FAIL-Q3 {sorted(bad3)}", flush=True)
    bad4, pi4 = bad_table(4)
    check_rss()
    print(f"d=4 bad patterns: {len(bad4)}, pi1 unresolved: {len(pi4)}", flush=True)
    print("PASS-PI1" if not (pi2 or pi3 or pi4) else "FAIL-PI1", flush=True)
    classes = {}
    for m in bad4:
        c = canon(m, 4)
        classes.setdefault(c, 0)
        classes[c] += 1
    sizes = sorted((16 - bin(c).count("1"), c, classes[c]) for c in classes)
    print(f"d=4 bad classes: {len(sizes)}; (removed count, rep, orbit): {sizes[:40]}", flush=True)

    # Question 2
    rnd = random.Random(20261031)
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    worst_ratio = 0.0
    worst_dist = 0
    all_cells = list(itertools.product(range(N), repeat=4))
    for p in (0.001, 0.003, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12):
        for trial in range(3):
            init = {c for c in all_cells if rnd.random() < p}
            if not init:
                continue
            final, passes = closure(init, N, bad3, bad4)
            ratio = len(final) / len(init)
            dist = max_distance(init, final, N) if len(final) < 5000 else -1
            print(f"p={p} n0={len(init)} n={len(final)} ratio={ratio:.2f} passes={passes} dist={dist}", flush=True)
            if p <= 0.03:
                worst_ratio = max(worst_ratio, ratio)
            worst_dist = max(worst_dist, dist)
            check_rss()
    # structured: diagonal chain and sheet, offset (1,1,1,0), and offset (1,1,1,1)
    sets = {
        "chain111": {(i, i, i, 0) for i in range(N - 1)},
        "sheet111": {(i, i, i, t) for i in range(N - 1) for t in range(N)},
        "chain1111": {(i, i, i, i) for i in range(N - 1)},
        "double": {(i, i, i, 0) for i in range(N - 1)} | {(i + 3, i, i, 0) for i in range(N - 1)},
        "lattice222": {c for c in all_cells if sum(c) % 3 == 0 and c[3] == 0},
    }
    for name, init in sets.items():
        final, passes = closure(init, N, bad3, bad4)
        ratio = len(final) / len(init)
        dist = max_distance(init, final, N) if len(final) < 5000 else -1
        print(f"{name} n0={len(init)} n={len(final)} ratio={ratio:.2f} passes={passes} dist={dist}", flush=True)
        worst_ratio = max(worst_ratio, ratio)
        worst_dist = max(worst_dist, dist)
    # hill climb on ratio, small torus, cells added one at a time
    best_overall = 0.0
    M = 7
    cells_small = list(itertools.product(range(M), repeat=4))
    for restart in range(4):
        cur = {rnd.choice(cells_small) for _ in range(6)}
        val = len(closure(cur, M, bad3, bad4)[0]) / len(cur)
        for it in range(250):
            c = rnd.choice(cells_small)
            new = set(cur)
            if c in new and len(new) > 2:
                new.remove(c)
            else:
                new.add(c)
            v2 = len(closure(new, M, bad3, bad4)[0]) / len(new)
            if v2 >= val:
                cur, val = new, v2
        print(f"climb restart={restart} n0={len(cur)} ratio={val:.2f}", flush=True)
        best_overall = max(best_overall, val)
        check_rss()
    worst_ratio = max(worst_ratio, best_overall)
    print(f"worst ratio {worst_ratio:.2f}, worst distance {worst_dist}")
    print("PASS-RATIO" if worst_ratio <= 100 and worst_dist <= 4 else ("FAIL-RATIO" if worst_ratio > 100 else "NEITHER-RATIO"))


if __name__ == "__main__":
    main()
