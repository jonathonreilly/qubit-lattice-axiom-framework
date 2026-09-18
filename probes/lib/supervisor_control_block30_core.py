"""Core: the level automaton (three-predecessor majority with one-sided noise) and the explanation-tree construction
(clusters, cause graph, spanning lemma, refinement) in Z^3 level time. Exact rationals for the functionals M_k = z_k - tau/3."""
from fractions import Fraction as F
from itertools import product, combinations
from collections import deque

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK_OFFSETS = [tuple(E[a][i] - E[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def level(z):
    return z[0] + z[1] + z[2]


def M(k, z):
    return F(z[k]) - F(level(z), 3)


def preds(z):
    return [sub(z, E[j]) for j in range(3)]


def is_fork(u, v):
    return sub(u, v) in FORK_OFFSETS


def cone(x, depth):
    out = []
    for d1 in range(depth + 1):
        for d2 in range(depth + 1 - d1):
            for d3 in range(depth + 1 - d1 - d2):
                out.append(sub(x, (d1, d2, d3)))
    return out


def run_automaton(sites, zeta):
    """sites: list of space-time points closed under predecessors within the window (points outside are 0)."""
    eta = {}
    for z in sorted(sites, key=level):
        ps = [eta.get(p, 0) for p in preds(z)]
        maj = 1 if sum(ps) >= 2 else 0
        eta[z] = 1 if (maj or zeta.get(z, 0)) else 0
    return eta


class Explainer:
    def __init__(self, eta, zeta):
        self.eta = eta
        self.zeta = zeta
        self.ones = {z for z, v in eta.items() if v == 1}
        npred = {z: sum(eta.get(p, 0) for p in preds(z)) for z in self.ones}
        self.noise = {z for z in self.ones if npred[z] == 0}          # S-nodes: seeds (no 1-predecessor)
        self.amp = {z for z in self.ones if npred[z] == 1}            # A-nodes: amplified (exactly one 1-predecessor)
        assert all(zeta.get(z, 0) == 1 for z in self.noise | self.amp)
        self.amp_dir = {z: [j for j in range(3) if eta.get(preds(z)[j], 0) == 1][0] for z in self.amp}
        # excuse pairs for processed ones: lexicographically first pair of indices among 1-predecessors
        self.exc = {}
        for z in self.ones:
            if z in self.noise or z in self.amp:
                continue
            idx = [j for j in range(3) if eta.get(preds(z)[j], 0) == 1]
            assert len(idx) >= 2, (z, idx)
            self.exc[z] = (idx[0], idx[1])
        self._cluster_cache = {}

    def excuse_k(self, v, k):
        """excuse of pole v for charge k: a processed pole's winning-pair member with index != k; an A-pole's single 1-predecessor."""
        if v in self.amp:
            w = preds(v)[self.amp_dir[v]]
            assert M(k, w) - M(k, v) == (F(1, 3) if self.amp_dir[v] != k else F(-2, 3))
            return w
        i, j = self.exc[v]
        cand = [a for a in (i, j) if a != k]
        a = min(cand)
        w = preds(v)[a]
        assert M(k, w) - M(k, v) == F(1, 3)
        return w

    def is_bad(self, v, k):
        return v in self.amp and self.amp_dir[v] == k

    def arrows_down(self, z):
        """arrows of the extended arrow graph: a processed or amplified 1-site to its 1-predecessors (all of them; one for an A-node)."""
        if z in self.noise or z not in self.ones:
            return []
        return [p for p in preds(z) if p in self.ones]

    def clusters_at(self, s):
        """clusters at level s: components of the arrow graph on 1-sites with levels <= s, restricted to level s."""
        if s in self._cluster_cache:
            return self._cluster_cache[s]
        pts = [z for z in self.ones if level(z) <= s]
        parent = {z: z for z in pts}

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        for z in pts:
            for p in self.arrows_down(z):
                ra, rb = find(z), find(p)
                if ra != rb:
                    parent[ra] = rb
        comp = {}
        for z in pts:
            if level(z) == s:
                comp.setdefault(find(z), set()).add(z)
        cl = {}
        for members in comp.values():
            fs = frozenset(members)
            for z in members:
                cl[z] = fs
        self._cluster_cache[s] = cl
        return cl

    def explain(self, root):
        """Build the extended explanation tree of a 1-site root. Returns (nodes, edges, seed_nodes, amp_nodes, n_refinements, bad_total).
        edges: frozenset -> 'arrow' (excuse), 'amp' (amplification arrow), 'fork'."""
        assert root in self.ones
        edges = {}
        processed = set()
        amp_nodes = set()
        unproc = [(frozenset([root]), (root, root, root))]
        refinements = 0
        bad_total = 0
        if root in self.noise:
            return {root}, edges, {root}, set(), 0, 0

        def incident(pt):
            return any(pt in e for e in edges)

        while True:
            active = [(K, poles) for (K, poles) in unproc if not all(v in self.noise for v in poles)]
            if not active:
                break
            K, poles = active[0]
            unproc.remove((K, poles))
            assert all(v not in self.noise for v in poles), "cluster with mixed noise poles"
            s = level(next(iter(K)))
            u = [self.excuse_k(poles[j], j) for j in range(3)]
            bad = sum(1 for j in range(3) if self.is_bad(poles[j], j))
            bad_total += bad
            cl = self.clusters_at(s - 1)
            V_K = []
            for z in K:
                for p in self.arrows_down(z):
                    c = cl[p]
                    if c not in V_K:
                        V_K.append(c)
            # fork edges between distinct clusters of V_K (one representative fork each)
            fam = [("cluster", c) for c in V_K]
            for a, b in combinations(range(len(V_K)), 2):
                found = None
                for w in sorted(V_K[a]):
                    for off in FORK_OFFSETS:
                        w2 = add(w, off)
                        if w2 in V_K[b]:
                            found = frozenset([w, w2])
                            break
                    if found:
                        break
                if found:
                    fam.append(("fork", found))
            # intersection graph on fam
            n = len(fam)
            adj = {i: set() for i in range(n)}
            for i, j in combinations(range(n), 2):
                if fam[i][0] != fam[j][0] and (fam[i][1] & fam[j][1]):   # bipartite: clusters adjacent to the forks that touch them
                    adj[i].add(j); adj[j].add(i)
            term = []
            for j in range(3):
                ti = [i for i in range(n) if fam[i][0] == "cluster" and u[j] in fam[i][1]]
                assert len(ti) == 1, (u[j], ti)
                term.append(ti[0])
            # minimal tree connecting the three terminals: shortest paths then prune
            def bfs_path(src, dsts):
                prev = {src: None}
                dq = deque([src])
                while dq:
                    a = dq.popleft()
                    if a in dsts:
                        path = []
                        while a is not None:
                            path.append(a); a = prev[a]
                        return path[::-1]
                    for b in adj[a]:
                        if b not in prev:
                            prev[b] = a; dq.append(b)
                raise AssertionError("cause graph not connected")
            p12 = bfs_path(term[0], {term[1]})
            tree_nodes = set(p12)
            p3 = bfs_path(term[2], tree_nodes)
            tree_nodes |= set(p3)
            tedges = set()
            for path in (p12, p3):
                for a, b in zip(path, path[1:]):
                    tedges.add(frozenset([a, b]))
            # prune non-terminal leaves
            changed = True
            while changed:
                changed = False
                for i in list(tree_nodes):
                    deg = sum(1 for e in tedges if i in e)
                    if deg <= 1 and i not in term:
                        tree_nodes.discard(i)
                        tedges = {e for e in tedges if i not in e}
                        changed = True
            tnbr = {i: set() for i in tree_nodes}
            for e in tedges:
                a, b = tuple(e)
                tnbr[a].add(b); tnbr[b].add(a)
            # reduced point sets and pole assignment
            def inter_point(i, j):
                return min(fam[i][1] & fam[j][1])
            reduced = {}
            for i in tree_nodes:
                pts = set()
                for j in range(3):
                    if term[j] == i:
                        pts.add(u[j])
                for nb in tnbr[i]:
                    pts.add(inter_point(i, nb))
                reduced[i] = pts
            # direction from i toward terminal term[j] within the tree
            def next_toward(i, target):
                if i == target:
                    return None
                prev = {i: None}
                dq = deque([i])
                while dq:
                    a = dq.popleft()
                    if a == target:
                        b = a
                        while prev[b] != i:
                            b = prev[b]
                        return b
                    for b in tnbr[a]:
                        if b not in prev:
                            prev[b] = a; dq.append(b)
                raise AssertionError
            pole_of = {}
            for i in tree_nodes:
                pl = []
                for j in range(3):
                    if u[j] in reduced[i]:
                        pl.append(u[j])
                    else:
                        nb = next_toward(i, term[j])
                        pl.append(inter_point(i, nb))
                pole_of[i] = tuple(pl)
                assert all(pt in reduced[i] for pt in pl)
            total = sum(M(j, pole_of[i][j]) for i in tree_nodes for j in range(3))
            expected = sum(M(j, u[j]) for j in range(3))
            assert total == expected, ("spanning lemma failed", total, expected)
            assert expected == sum(M(j, poles[j]) for j in range(3)) + 1 - bad
            # new clusters and forks
            for i in tree_nodes:
                if fam[i][0] == "cluster":
                    unproc.append((fam[i][1], pole_of[i]))
                else:
                    a, b = tuple(fam[i][1])
                    edges[frozenset([a, b])] = "fork"
            # kept poles: incident ones, bad A-poles (forced), or the first pole if none
            kept = {}
            for j in range(3):
                v = poles[j]
                if (incident(v) or self.is_bad(v, j)) and v not in kept:
                    kept[v] = j
            if not kept:
                kept[poles[0]] = 0
            for v, j in kept.items():
                if v in self.amp:
                    edges[frozenset([v, preds(v)[self.amp_dir[v]]])] = "amp"
                    amp_nodes.add(v)
                else:
                    edges[frozenset([v, u[j]])] = "arrow"
                    processed.add(v)
            refinements += 1
        noise_nodes = set()
        for (K, poles) in unproc:
            assert len(K) == 1 and all(v in self.noise for v in poles)
            noise_nodes |= set(K)
        nodes = set(processed) | amp_nodes | noise_nodes
        for e in edges:
            nodes |= set(e)
        return nodes, edges, noise_nodes, amp_nodes, refinements, bad_total


def check_tree(nodes, edges, root, explainer):
    """the point graph must be a tree, contain the root, use only arrows/forks of G, noise nodes are noise sites."""
    ok = root in nodes
    ok = ok and len(edges) == len(nodes) - 1
    # connectivity
    nb = {v: set() for v in nodes}
    for e, kind in edges.items():
        a, b = tuple(e)
        nb[a].add(b); nb[b].add(a)
        if kind in ("arrow", "amp"):
            ok = ok and (b in preds(a) or a in preds(b))
        else:
            ok = ok and is_fork(a, b)
    seen = {root}; dq = deque([root])
    while dq:
        a = dq.popleft()
        for b in nb[a]:
            if b not in seen:
                seen.add(b); dq.append(b)
    ok = ok and seen == nodes
    ok = ok and all(z in explainer.ones for z in nodes)
    return ok
