#!/usr/bin/env python3
"""J:attack:PR8168 - block 25 (PR #8168), attack pattern (e) SAMPLED EVIDENCE: T4's explanation tree (edges <= 4(n - 1), forks = n - 1,
arrows <= 3(n - 1), at most one arrow to a predecessor per node, the marked nodes exactly the noise sites, the spanning identity at every
refinement) rests on a proof plus executions that were exhaustive only at depths 2-3 and random at depths 3-7 ('the largest ratio
observed is below 3').  Here the refinement procedure of T4 is re-implemented from the note's text (clusters of the arrow graph, the cause
graph with one fork per adjacent pair, T3's minimal subtree through shortest paths and its poles, the excuses, the kept poles and their
arrows), and instead of more random cones an adversarial search is run: hill-climbing over noise configurations in backward cones of depth
4-12 that maximizes edges/(n - 1), arrows/(n - 1) and the number of refinements, with every asserted property checked on every visited
configuration; plus the exhaustive depth-2 cone (1024 configurations) as a calibration of the implementation.
HIT if some configuration makes the procedure fail, breaks one of the asserted properties, or exceeds edges <= 4(n - 1) / arrows <= 3(n - 1).
"""
import random
import sys
import time
from collections import deque
from fractions import Fraction as F

random.seed(8168)
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def tau(z):
    return z[0] + z[1] + z[2]


def M3(z, k):                                   # 3 M_k(z) = 3 z_k - tau(z), an integer
    return 3 * z[k] - tau(z)


FORKS = [add(E[i], (-E[j][0], -E[j][1], -E[j][2])) for i in range(3) for j in range(3) if i != j]


class Failure(Exception):
    pass


def run(x, D, noise):
    """Compute eta on the relevant region and run T4's refinement; return the counts or raise Failure."""
    lo = tuple(c - D for c in x)
    # the region: y >= lo componentwise, 1 <= level <= tau(x); eta vanishes elsewhere below tau(x)
    eta, noise_site = {}, set()
    levels = {}
    T = tau(x)
    for s in range(T - D + 1, T + 1):
        pts = []
        base = s - tau(lo)
        for a in range(base + 1):
            for b in range(base - a + 1):
                y = (lo[0] + a, lo[1] + b, lo[2] + base - a - b)
                pts.append(y)
        levels[s] = pts
        for y in pts:
            ones = sum(eta.get(sub(y, e), 0) for e in E)
            z = 1 if y in noise else 0
            v = 1 if (ones >= 2 or z) else 0
            if v:
                eta[y] = 1
                if ones < 2:
                    noise_site.add(y)
    if not eta.get(x):
        return None
    ones = set(eta)

    def one_preds(y):
        return [(j, sub(y, E[j])) for j in range(3) if sub(y, E[j]) in ones]

    # clusters: union-find over the arrow graph, level by level
    parent = {}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    cluster_of = {}
    for s in sorted(levels):
        for y in levels[s]:
            if y in ones:
                parent[y] = y
        for y in levels[s]:
            if y in ones and y not in noise_site:
                for _, w in one_preds(y):
                    ra, rb = find(y), find(w)
                    if ra != rb:
                        parent[ra] = rb
        comp = {}
        for y in levels[s]:
            if y in ones:
                comp.setdefault(find(y), set()).add(y)
        for c in comp.values():
            fc = frozenset(c)
            for y in c:
                cluster_of[y] = fc

    def excuse(v, k):
        pr = one_preds(v)
        W = [p for p in pr][:2]                    # the two 1-predecessors with the smallest indices
        cand = [(j, w) for j, w in W if j != k]
        return min(cand)[1]

    # refinement
    U = [(frozenset([x]), (x, x, x))]
    processed, arrows, forks = set(), [], []
    edges_at = {}                                    # point -> number of incident edges
    seen_clusters = {frozenset([x])}
    refinements = 0
    while True:
        idx = next((i for i, (K, v) in enumerate(U) if any(p not in noise_site for p in K)), None)
        if idx is None:
            break
        K, v = U.pop(idx)
        if any(p in noise_site for p in K):
            raise Failure("a cluster with a non-noise pole contains a noise site")
        s = tau(next(iter(K)))
        u = tuple(excuse(v[k], k) for k in range(3))
        span_K = sum(M3(v[k], k) for k in range(3))
        span_u = sum(M3(u[k], k) for k in range(3))
        if span_u != span_K + 3:
            raise Failure(f"excuse lemma: 3 Span(u) = {span_u} vs 3 Span(K) + 3 = {span_K + 3}")
        VK = []
        for p in K:
            for _, w in one_preds(p):
                c = cluster_of[w]
                if c not in VK:
                    VK.append(c)
        cid = {c: i for i, c in enumerate(VK)}
        for k in range(3):
            if cluster_of[u[k]] not in cid:
                raise Failure("an excuse outside V_K")
        # one fork per adjacent pair
        fork_list, pair_seen = [], set()
        for c in VK:
            for p in sorted(c):
                for f in FORKS:
                    q = add(p, f)
                    if q in ones and q in cluster_of and cluster_of[q] in cid and cluster_of[q] != c:
                        pr = tuple(sorted((cid[c], cid[cluster_of[q]])))
                        if pr not in pair_seen:
                            pair_seen.add(pr)
                            fork_list.append((cid[c], cid[cluster_of[q]], p, q))
        # bipartite graph B
        adj = {("C", i): [] for i in range(len(VK))}
        for j, (a, b, p, q) in enumerate(fork_list):
            adj[("F", j)] = [("C", a), ("C", b)]
            adj[("C", a)].append(("F", j))
            adj[("C", b)].append(("F", j))
        Ck = [("C", cid[cluster_of[u[k]]]) for k in range(3)]

        def bfs(src_set, target):
            prev = {n: None for n in src_set}
            dq = deque(src_set)
            while dq:
                n = dq.popleft()
                if n == target:
                    path = [n]
                    while prev[path[-1]] is not None:
                        path.append(prev[path[-1]])
                    return path[::-1]
                for m in adj[n]:
                    if m not in prev:
                        prev[m] = n
                        dq.append(m)
            return None

        p12 = bfs([Ck[0]], Ck[1])
        if p12 is None:
            raise Failure("cause graph disconnected (T1)")
        p3 = bfs(list(p12), Ck[2])
        if p3 is None:
            raise Failure("cause graph disconnected (T1)")
        tnodes = set(p12) | set(p3)
        tedges = set()
        for path in (p12, p3):
            for a, b in zip(path, path[1:]):
                tedges.add(frozenset((a, b)))
        terminals = set(Ck)
        changed = True
        while changed:
            changed = False
            for n in list(tnodes):
                deg = sum(1 for e in tedges if n in e)
                if deg <= 1 and n not in terminals and len(tnodes) > 1:
                    tnodes.remove(n)
                    tedges = {e for e in tedges if n not in e}
                    changed = True
        tadj = {n: [m for e in tedges if n in e for m in e if m != n] for n in tnodes}

        def pts_of(n):
            return VK[n[1]] if n[0] == "C" else frozenset(fork_list[n[1]][2:])

        def meet(a, b):
            common = pts_of(a) & pts_of(b)
            if len(common) != 1:
                raise Failure("adjacent tree nodes do not meet in one point")
            return next(iter(common))

        def next_toward(a, target):
            if a == target:
                return None
            prev = {a: None}
            dq = deque([a])
            while dq:
                n = dq.popleft()
                if n == target:
                    break
                for m in tadj[n]:
                    if m not in prev:
                        prev[m] = n
                        dq.append(m)
            n = target
            while prev[n] != a:
                n = prev[n]
            return n

        poles = {}
        for X in tnodes:
            Xp = set(u[k] for k in range(3) if X == Ck[k]) | {meet(X, Y) for Y in tadj[X]}
            if X[0] == "F":
                Xp = set(pts_of(X))
            pol = []
            for k in range(3):
                if u[k] in Xp:
                    pol.append(u[k])
                else:
                    pol.append(meet(X, next_toward(X, Ck[k])))
            if not all(pp in pts_of(X) for pp in pol) or not Xp <= set(pol):
                raise Failure("T3: a point of X' is not a pole, or a pole outside X")
            poles[X] = tuple(pol)
        tot = sum(M3(poles[X][k], k) for X in tnodes for k in range(3))
        if tot != span_u:
            raise Failure(f"spanning identity: 3 sum Span(X) = {tot} vs 3 sum M_k(u_k) = {span_u}")
        # kept poles, arrows
        kept = [w for w in dict.fromkeys(v) if edges_at.get(w, 0) > 0] or [v[0]]
        for X in tnodes:
            if X[0] == "C":
                if VK[X[1]] in seen_clusters:
                    raise Failure("a cluster added twice")
                seen_clusters.add(VK[X[1]])
                U.append((VK[X[1]], poles[X]))
            else:
                a_, b_ = fork_list[X[1]][2:]
                forks.append((a_, b_))
                edges_at[a_] = edges_at.get(a_, 0) + 1
                edges_at[b_] = edges_at.get(b_, 0) + 1
        for w in kept:
            k = min(k for k in range(3) if v[k] == w)
            arrows.append((w, u[k]))
            edges_at[w] = edges_at.get(w, 0) + 1
            edges_at[u[k]] = edges_at.get(u[k], 0) + 1
            if w in processed:
                raise Failure("a point processed twice")
            processed.add(w)
        refinements += 1
    # the final tree
    marked = set()
    for K, v in U:
        if len(K) != 1 or next(iter(K)) not in noise_site:
            raise Failure("an unprocessed cluster that is not a noise singleton")
        marked.add(next(iter(K)))
    nodes = processed | marked | {x}
    all_edges = [frozenset(e) for e in arrows] + [frozenset(e) for e in forks]
    endpoints = set().union(*all_edges) if all_edges else set()
    if not endpoints <= nodes:
        raise Failure("an edge endpoint that is neither processed nor marked")
    if len(set(all_edges)) != len(all_edges) or len(all_edges) != len(nodes) - 1:
        raise Failure(f"not a tree: {len(all_edges)} edges on {len(nodes)} nodes")
    nb = {n: [] for n in nodes}
    for e in all_edges:
        a_, b_ = tuple(e)
        nb[a_].append(b_)
        nb[b_].append(a_)
    seen, dq = {x}, deque([x])
    while dq:
        n = dq.popleft()
        for m in nb[n]:
            if m not in seen:
                seen.add(m)
                dq.append(m)
    if seen != nodes:
        raise Failure("not connected")
    down = {n: sum(1 for (w, uu) in arrows if w == n) for n in nodes}
    if any(c > 1 for c in down.values()):
        raise Failure("a node with two arrows to predecessors")
    if {n for n in nodes if down[n] == 0} != marked or not marked <= noise_site:
        raise Failure("the nodes without an arrow to a predecessor are not exactly the noise nodes")
    if any(eta.get(n) != 1 for n in nodes):
        raise Failure("a node that is not a 1-site")
    n = len(marked)
    if len(forks) != n - 1 or len(arrows) > 3 * (n - 1):
        raise Failure(f"counts: n = {n}, forks = {len(forks)}, arrows = {len(arrows)}")
    return n, len(arrows), len(forks), refinements


def cone(x, D):
    out = []
    for k1 in range(D):
        for k2 in range(D - k1):
            for k3 in range(D - k1 - k2):
                out.append((x[0] - k1, x[1] - k2, x[2] - k3))
    return out


def main():
    t0 = time.time()
    hits = []
    stats = {"configs": 0, "trees": 0, "best_edge_ratio": F(0), "best_arrow_ratio": F(0), "best_ref": 0}
    best_cfg = None

    def evaluate(x, D, noise):
        stats["configs"] += 1
        try:
            r = run(x, D, noise)
        except Failure as e:
            hits.append(f"depth {D}, {len(noise)} noise sites {sorted(noise)[:12]}: {e}")
            return None
        if r is None:
            return None
        n, a, f, ref = r
        stats["trees"] += 1
        if n >= 2:
            er, ar = F(a + f, n - 1), F(a, n - 1)
            if er > stats["best_edge_ratio"]:
                stats["best_edge_ratio"] = er
            if ar > stats["best_arrow_ratio"]:
                stats["best_arrow_ratio"] = ar
            stats["best_ref"] = max(stats["best_ref"], ref)
            return er, ar, ref
        return F(0), F(0), ref

    # calibration: the exhaustive depth-2 cone
    x2 = (1, 1, 1)                                   # level 3: the depth-2 backward cone covers levels 1-3 (10 sites)
    base2 = cone(x2, 3)
    assert len(base2) == 10
    for mask in range(1 << len(base2)):
        evaluate(x2, 3, {base2[i] for i in range(len(base2)) if mask >> i & 1})
    print(f"[calibration] depth-2 backward cone: {1 << len(base2)} configurations, {stats['trees']} with eta_x = 1, largest edges/(n-1) "
          f"{float(stats['best_edge_ratio']):.4f}, arrows/(n-1) {float(stats['best_arrow_ratio']):.4f}; failures {len(hits)}  ({time.time() - t0:.0f}s)")
    # adversarial hill-climbing
    for D in (4, 5, 6, 7, 8, 9, 10, 11, 12):
        x = (D, 0, 0)
        sites = cone(x, D)
        for restart in range(12 if D <= 6 else (8 if D <= 9 else 5)):
            cur = set(random.sample(sites, max(2, len(sites) // 6)))
            val = evaluate(x, D, cur)
            curv = (val[0], val[1], val[2]) if val else (F(-1), F(-1), -1)
            obj_i = restart % 3
            for step in range(300 if D <= 6 else (200 if D <= 9 else 150)):
                cand = set(cur)
                for _ in range(random.choice((1, 1, 2, 3))):
                    y = random.choice(sites)
                    cand.symmetric_difference_update({y})
                val = evaluate(x, D, cand)
                if val is None:
                    continue
                if val[obj_i] >= curv[obj_i]:
                    cur, curv = cand, val
            if len(hits) > 5:
                break
        print(f"[adversarial] depth {D}: {stats['configs']} configurations so far; largest edges/(n-1) {float(stats['best_edge_ratio']):.4f}, "
              f"arrows/(n-1) {float(stats['best_arrow_ratio']):.4f}, most refinements {stats['best_ref']}; failures {len(hits)}  ({time.time() - t0:.0f}s)")
    over = stats["best_edge_ratio"] > 4 or stats["best_arrow_ratio"] > 3
    if over:
        hits.append(f"bound exceeded: edges/(n-1) {stats['best_edge_ratio']}, arrows/(n-1) {stats['best_arrow_ratio']}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits[:8]:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (e) SAMPLED EVIDENCE - T4's refinement procedure re-implemented from the note and driven by hill-climbing "
          f"over noise configurations in backward cones of depth 4-12 (plus the exhaustive depth-2 cone): {stats['configs']} configurations, "
          f"{stats['trees']} with eta_x = 1; largest edges/(n-1) = {float(stats['best_edge_ratio']):.4f} (bound 4; the note observed below 3), "
          f"largest arrows/(n-1) = {float(stats['best_arrow_ratio']):.4f} (bound 3), most refinements {stats['best_ref']}; {len(hits)} failures "
          f"of the procedure or of its asserted properties; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
