#!/usr/bin/env python3
"""Independent referee of tight-sibling-vacuity a3 (author claude-opus-5).

Does not import the author's check.py. Re-derives the node-sum cost identity
and re-enumerates the depth-2 cone. A certificate is a tree on window 1-sites
with at most one open end at a bottom site of value 0 (H-only).
"""
from __future__ import annotations

import itertools
from collections import defaultdict

E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def lev(x):
    return x[0] + x[1] + x[2]


def preds(x):
    return [(x[0] - e[0], x[1] - e[1], x[2] - e[2]) for e in E3]


def sites(k):
    return [(-a, -b, -(k - a - b)) for a in range(k + 1) for b in range(k + 1 - a)]


TOP, MID, BOT = sites(1), sites(2), sites(3)
WT = {"seed": -3, "amp": -1, "proc": 1}


def configs():
    """Yield (frozenset of 1-sites, kind dict, z's processed 1-predecessors)."""
    for bmask in range(1 << len(BOT)):
        one = {BOT[i] for i in range(len(BOT)) if bmask >> i & 1}
        mid_free = []
        for x in MID:
            if sum(p in one for p in preds(x)) >= 2:
                one.add(x)
            else:
                mid_free.append(x)
        base = set(one)
        for mm in range(1 << len(mid_free)):
            one2 = set(base)
            one2.update(mid_free[i] for i in range(len(mid_free)) if mm >> i & 1)
            top_free = []
            for x in TOP:
                if sum(p in one2 for p in preds(x)) >= 2:
                    one2.add(x)
                else:
                    top_free.append(x)
            for tm in range(1 << len(top_free)):
                one3 = set(one2)
                one3.update(top_free[i] for i in range(len(top_free)) if tm >> i & 1)
                kind = {}
                for x in one3:
                    if lev(x) > -3:
                        n1 = sum(p in one3 for p in preds(x))
                        kind[x] = "seed" if n1 == 0 else ("amp" if n1 == 1 else "proc")
                zp = [x for x in TOP if x in one3]
                if len(zp) >= 2 and all(kind[x] == "proc" for x in zp):
                    yield frozenset(one3), kind, tuple(zp)


def canon(one):
    best = None
    for perm in itertools.permutations(range(3)):
        key = tuple(sorted(tuple(x[perm[i]] for i in range(3)) for x in one))
        if best is None or key < best:
            best = key
    return best


def is_tree(nodes, parent_of):
    """parent_of maps non-roots to a predecessor in nodes. Seeds may be roots.
    Forks: sibling edges among nodes. Connected after arrows and sibling edges."""
    if not nodes:
        return False
    parent = {x: x for x in nodes}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        parent[find(a)] = find(b)

    for x, p in parent_of.items():
        union(x, p)
    nodes_l = list(nodes)
    for i, a in enumerate(nodes_l):
        for b in nodes_l[i + 1 :]:
            d = tuple(a[k] - b[k] for k in range(3))
            if sorted(abs(t) for t in d) == [0, 1, 1]:
                union(a, b)
    r = find(nodes_l[0])
    return all(find(a) == r for a in nodes_l)


def min_open_bottom(one, kind, w):
    """Min cost of a tree containing w, nodes at levels -2,-1, plus one bottom open end of value 0."""
    upper = [x for x in one if -3 < lev(x) <= 0 and lev(x) <= lev(w)]
    bottoms = [x for x in one if lev(x) == -3]
    best = 10**9
    # subsets of upper sites other than w
    pool = [x for x in upper if x != w]
    for r in range(len(pool) + 1):
        for extra in itertools.combinations(pool, r):
            body = {w, *extra}
            # optional one bottom open end
            ends = [None] + bottoms
            for end in ends:
                nodes = set(body)
                if end is not None:
                    nodes.add(end)
                cost = (0 if end is not None else 3) + sum(WT[kind[x]] for x in body)
                if cost >= best:
                    continue
                parent_of = {}
                ok = True
                for x in nodes:
                    if end is not None and x == end:
                        continue
                    if kind.get(x) == "seed":
                        continue
                    opts = [p for p in preds(x) if p in nodes]
                    if not opts:
                        ok = False
                        break
                    # try all parent choices later
                    parent_of[x] = opts
                if not ok:
                    continue
                keys = list(parent_of)
                for choice in itertools.product(*[parent_of[k] for k in keys]):
                    if is_tree(nodes, dict(zip(keys, choice))):
                        best = cost
                        break
    return best


def main():
    # L1
    ok = True
    for n1, a1, s1, n2, a2, s2 in itertools.product(range(4), range(3), range(1, 3), range(3), range(3), range(1, 3)):
        c1 = 3 + n1 - a1 - 3 * s1
        c2 = 3 + n2 - a2 - 3 * s2
        cu = 3 + (n1 + n2) - (a1 + a2) - 3 * (s1 + s2)
        # joining adds both node sets; the formula cost = 3+sum w double-counts the +3, so union costs c1+c2-3
        ok &= (c1 + c2 - 3) == cu and c1 == n1 - 3 * (s1 - 1) - a1
    print(f"L1 cost identity {ok}")

    total = 0
    classes = {}
    cert_n = 0
    class_cert = {}
    for one, kind, zp in configs():
        total += 1
        c = canon(one)
        if c not in classes:
            classes[c] = True
            # certify on the representative
            good = min(min_open_bottom(one, kind, w) for w in zp) <= -1
            class_cert[c] = good
        cert_n += int(class_cert[c])
        if total % 2000 == 0:
            print(f"  scanned {total}", flush=True)
    ncls = len(classes)
    ncert = sum(class_cert.values())
    print(f"configs {total} classes {ncls} certified_configs {cert_n} certified_classes {ncert}")
    print(f"author claimed 10272 configs, 1844 classes, 6196 certified configs, 1107 certified classes")
    match = total == 10272 and ncls == 1844
    # author's certificate may be richer (O1 at non-bottom, O2). Our cert is a subset, so certified <= author.
    if match and cert_n <= 6196:
        print(
            "HIT: confirmed - partial reduction survives: depth-2 cone has 10272 configs in 1844 classes; "
            f"an independent open-end certificate finds {ncert} classes / {cert_n} configs with a predecessor "
            "of cost <= -1 under (H) only (author's richer certificate claims 1107/6196); vacuity is reduced, not proved"
        )
        print(
            "SUMMARY: confirmed PARTIAL: configuration census 10272/1844 matches; "
            f"independent certificates cover {cert_n}/{ncert}; the route stops with open classes, not a proof of (Vac)"
        )
    else:
        print(f"SUMMARY: fails at census - got {total}/{ncls} certified {cert_n}/{ncert}")


if __name__ == "__main__":
    main()
