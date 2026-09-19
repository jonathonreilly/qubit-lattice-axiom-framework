#!/usr/bin/env python3
"""beyond-the-union-bound, attempt 3 (worker w-jonathonsmac4f50-jae8a, model claude-opus-5).

Count the refinement histories of block 30's construction instead of its explanation trees.

A refinement moves the three poles of a cluster down one level (27 move patterns, a bad charge
weighted r = eps2/sigma), then hangs a minimal Steiner tree of clusters and forks. Block 30's potential
gives #refinements <= #forks + #bad, and |S| = #forks + 1 holds for every history. So

    P(eta'_x = 1) <= eps1 * Z,   Z = 1 + mu Z / (1 - c Z)^3,   mu = sigma (2 + eps2/sigma)^3,  c = 6 eps1 / sigma,

for every sigma in (0, 1] at which a super-solution exists. Exact arithmetic throughout.

Sections
  A  deviations, their monotonicity in p, block 30's two-level coupling inequality at the certificate points
  B  block 30's construction (its runner's code, copied verbatim, one recording line added): every refinement's
     terminals are moves of the poles, the potential and the seed count, and the reconstruction of every seed
     and bad site from the abstract history alone (all configurations of the depth-2 and depth-3 cones, and random cones)
  C  the recursion counts exactly the abstract histories (series coefficients against a direct enumeration of
     the grammar), and every realized history lies in the grammar
  D  domination on complete small cones: the exact P(eta'_x = 1) <= the union over realized histories <= eps1 Zbar,
     and each history's configurations weigh at most eps1^|S| eps2^B
  E  exact certificates on four lines, and comparisons with the tree route's ceilings
  F  this route's own ceiling (27 eps2 < 1 at eps1 -> 0) and a numerical scan below the certificates

The construction code in section B is copied from
scripts/admissibility_rule_six_axis_formation_threshold_two_level_domination_seeds_and_amplified_nodes_2026_09_16.py
on the block 30 branch (PR #8174, commit cc7662e14ebf17010a0c60fdb8e7e634b176ce99), lines 87-377, with its
mutation hook replaced by 0 and one line that records each refinement.
"""
from __future__ import annotations

import math
import random
import sys
from collections import deque
from fractions import Fraction
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

PASSES = 0
FAILS = 0


def check(tag, ok, msg):
    global PASSES, FAILS
    if ok:
        PASSES += 1
        print(f"PASS: {tag} {msg}")
    else:
        FAILS += 1
        print(f"FAIL: {tag} {msg}")


# ============================================================================================ A: deviations
def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def eps_pair(p, q, r):
    d1, d2, d3 = deviations(p, q, r)
    return d1, max(d2, d3)


def phi_of(v, w, p, q, r):
    # menu {+-e_1, +-e_2, +-e_3} encoded 0..5 with v ^ 1 the antipode
    if v == w:
        return p
    if v == (w ^ 1):
        return q
    return r


def conditional(a, triple, p, q, r):
    ws = [phi_of(v, triple[0], p, q, r) * phi_of(v, triple[1], p, q, r) * phi_of(v, triple[2], p, q, r) for v in range(6)]
    return ws[a] / sum(ws)


LINES = [(84, 1, 2), (44, 1, 1), (168, 2, 4), (125, 1, 3)]


def section_a():
    p, q, r = sp.symbols("p q r", positive=True)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    # the p-derivatives against explicit negative expressions
    K1 = q ** 3 + 4 * r ** 3
    D2 = p * q * (p + q) + 4 * r ** 3
    c0 = r * q ** 2 + r ** 2 * q + 2 * r ** 3
    D3 = r * p ** 2 + r ** 2 * p + c0
    ok1 = sp.simplify(sp.diff(d1, p) + 3 * p ** 2 * K1 / (p ** 3 + K1) ** 2) == 0
    ok2 = sp.simplify(sp.diff(d2, p) + (q ** 3 * p ** 2 + 8 * q * r ** 3 * p) / D2 ** 2) == 0
    ok3 = sp.simplify(sp.diff(d3, p) + (r ** 3 * p ** 2 + 2 * r * p * c0) / D3 ** 2) == 0
    check("A1", ok1 and ok2 and ok3,
          "d_1, d_2, d_3 are strictly decreasing in p > 0 at fixed q, r > 0: their p-derivatives have numerators "
          "-3p^2(q^3 + 4r^3), -(q^3 p^2 + 8 q r^3 p), -(r^3 p^2 + 2 r p (r q^2 + r^2 q + 2 r^3)) over squares")
    ok = True
    for (pv, qv, rv) in LINES + [(11, 1, 2)]:
        P, Q, R = Fraction(pv), Fraction(qv), Fraction(rv)
        c1 = conditional(0, (0, 0, 0), P, Q, R)
        c2 = conditional(0, (0, 0, 1), P, Q, R)
        c3 = conditional(0, (0, 0, 2), P, Q, R)
        dd = deviations(pv, qv, rv)
        ok = ok and (1 - c1, 1 - c2, 1 - c3) == dd
        e1, e2 = eps_pair(pv, qv, rv)
        ok = ok and e1 <= e2
        for triple in product(range(6), repeat=3):
            n_a = sum(1 for v in triple if v == 0)
            dev = 1 - conditional(0, triple, P, Q, R)
            if n_a == 3:
                ok = ok and dev <= e1
            elif n_a == 2:
                ok = ok and dev <= e2
    check("A2", ok,
          "at the four certificate points and at (11, 1, 2): the closed forms equal 1 - K(a|a,a,a), 1 - K(a|a,a,-a), "
          "1 - K(a|a,a,b); d_1 <= max(d_2, d_3); every predecessor triple with three a's dissents with probability "
          "<= eps_1 and every triple with exactly two a's with probability <= eps_2 (all 216 triples): block 30's "
          "two-level coupling inequality")


# ============================================================================================ B: block 30's construction (copied)
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
        self.records = []
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
            assert expected == sum(M(j, poles[j]) for j in range(3)) + 1 - bad + 0
            self.records.append({'K': K, 'poles': tuple(poles), 'u': tuple(u), 'bad': bad, 'fam': list(fam), 'tree_nodes': set(tree_nodes), 'tnbr': {i: set(tnbr[i]) for i in tree_nodes}, 'term': list(term), 'pole_of': dict(pole_of)})
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



# ============================================================================================ B: the abstract history
def vec_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vec_sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


ZERO = (0, 0, 0)


def history(ex, root):
    """The abstract refinement history of the construction's run at root.

    Encoding: a cluster is ('seed',) or ('ref', d, tree) with d = (d_0, d_1, d_2) the moves (u_k = v_k - e_{d_k});
    tree = ('cl', here, cluster-encoding, kids) is the minimal Steiner tree of the refinement rooted at the cluster
    holding charge 0, 'here' the charges whose terminal lies in that cluster, and kids a sorted tuple of
    (charges beyond the fork, displacement m(f, Y) - m(f, X) of the fork, subtree)."""
    nodes, edges, S, A, refs, bad_total = ex.explain(root)
    recs = {rec['K']: rec for rec in ex.records}
    info = {'R': len(ex.records), 'B': 0, 'F': 0, 'seeds': [], 'bad_sites': [], 'ok': len(recs) == len(ex.records),
            'moves_ok': True, 'pole_rule_ok': True}

    def enc_cluster(K, poles):
        if K not in recs:
            info['ok'] = info['ok'] and len(K) == 1 and all(v == next(iter(K)) for v in poles)
            info['seeds'].append(next(iter(K)))
            return ('seed',)
        rec = recs[K]
        info['ok'] = info['ok'] and rec['poles'] == tuple(poles)
        u = rec['u']
        d = []
        for k in range(3):
            diff = vec_sub(poles[k], u[k])
            info['moves_ok'] = info['moves_ok'] and diff in E
            d.append(E.index(diff) if diff in E else 0)
        badk = [k for k in range(3) if d[k] == k]
        # a move d_k = k happens exactly when (v_k, k) is a bad pair
        info['moves_ok'] = info['moves_ok'] and len(badk) == rec['bad'] and all(ex.is_bad(poles[k], k) for k in badk) \
            and all(not ex.is_bad(poles[k], k) for k in range(3) if k not in badk)
        for k in badk:
            info['bad_sites'].append(poles[k])
        info['B'] += len(badk)
        fam, tn, tnbr, term, pole_of = rec['fam'], rec['tree_nodes'], rec['tnbr'], rec['term'], rec['pole_of']
        info['F'] += sum(1 for i in tn if fam[i][0] == 'fork')

        def next_toward(i, target):
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
                        prev[b] = a
                        dq.append(b)
            raise AssertionError

        for i in tn:        # block 25's pole rule (T3): u_k in C_k, else the meeting point toward C_k
            for k in range(3):
                want = u[k] if i == term[k] else min(fam[i][1] & fam[next_toward(i, term[k])][1])
                info['pole_rule_ok'] = info['pole_rule_ok'] and pole_of[i][k] == want

        def sub_charges(i, parent):
            out = {k for k in range(3) if term[k] == i}
            for j in tnbr[i]:
                if j != parent:
                    out |= sub_charges(j, i)
            return out

        def ser(i, parent):
            here = tuple(sorted(k for k in range(3) if term[k] == i))
            info['ok'] = info['ok'] and fam[i][0] == 'cluster'
            kids = []
            for f in tnbr[i]:
                if f == parent:
                    continue
                info['ok'] = info['ok'] and fam[f][0] == 'fork' and len(tnbr[f]) == 2
                (Y,) = [y for y in tnbr[f] if y != i]
                mX = min(fam[i][1] & fam[f][1])
                mY = min(fam[Y][1] & fam[f][1])
                kids.append((tuple(sorted(sub_charges(Y, f))), vec_sub(mY, mX), ser(Y, f)))
            kids.sort()
            return ('cl', here, enc_cluster(fam[i][1], pole_of[i]), tuple(kids))

        return ('ref', tuple(d), ser(term[0], None))

    enc = enc_cluster(frozenset([root]), (root, root, root))
    info['S'] = len(info['seeds'])
    info['Sset'] = set(S)
    return enc, info


REL_MEMO = {}


def rel(enc):
    """offsets of a cluster's three poles from its charge-0 pole, computed from the encoding alone (bottom-up)"""
    if enc[0] == 'seed':
        return (ZERO, ZERO, ZERO)
    key = id(enc)
    if key in REL_MEMO and REL_MEMO[key][0] is enc:
        return REL_MEMO[key][1]
    d, tree = enc[1], enc[2]
    upos = place_tree(tree, 0, ZERO, None, None)
    v = [vec_add(upos[k], E[d[k]]) for k in range(3)]
    out = tuple(vec_sub(v[k], v[0]) for k in range(3))
    REL_MEMO[key] = (enc, out)
    return out


def place_tree(node, anchor_charge, anchor_pos, seeds, bads):
    """place a Steiner-tree serialization with the root cluster's pole of anchor_charge at anchor_pos; returns the terminals"""
    _, here, cenc, kids = node
    ro = rel(cenc)
    base = vec_sub(anchor_pos, ro[anchor_charge])
    poles = [vec_add(base, ro[k]) for k in range(3)]
    upos = {k: poles[k] for k in here}
    if seeds is not None:
        place_cluster(cenc, poles, seeds, bads)
    for beyond, disp, sub in kids:
        mX = poles[beyond[0]]
        if not all(poles[k] == mX for k in beyond):
            raise ValueError("charges beyond a fork do not share their pole")
        back = [k for k in range(3) if k not in beyond][0]
        upos.update(place_tree(sub, back, vec_add(mX, disp), seeds, bads))
    return upos


def place_cluster(enc, poles, seeds, bads):
    if enc[0] == 'seed':
        if not poles[0] == poles[1] == poles[2]:
            raise ValueError("seed with distinct poles")
        seeds.append(poles[0])
        return
    d, tree = enc[1], enc[2]
    for k in range(3):
        if d[k] == k:
            bads.append(poles[k])
    upos = place_tree(tree, 0, vec_sub(poles[0], E[d[0]]), seeds, bads)
    for k in range(3):
        if vec_sub(poles[k], E[d[k]]) != upos[k]:
            raise ValueError("terminal mismatch")


def reconstruct(enc, root):
    seeds, bads = [], []
    place_cluster(enc, (root, root, root), seeds, bads)
    return seeds, bads


FORK_SET = set(FORK_OFFSETS)


def validate_cluster(enc):
    """membership in the grammar counted by the recursion; returns (R, B, F)"""
    if enc == ('seed',):
        return (0, 0, 0)
    tag, d, tree = enc
    assert tag == 'ref' and len(d) == 3 and all(x in (0, 1, 2) for x in d)
    b = sum(1 for k in range(3) if d[k] == k)
    R, B, F_ = validate_tree(tree, (0, 1, 2), root=True)
    return (R + 1, B + b, F_)


def validate_tree(tree, charges, root=False):
    tag, here, enc, kids = tree
    assert tag == 'cl' and tuple(sorted(here)) == here and set(here) <= set(charges)
    if root:
        assert 0 in here
    R, B, F_ = validate_cluster(enc)
    rest = set(charges) - set(here)
    seen = set()
    assert tuple(sorted(kids)) == kids
    for beyond, disp, sub in kids:
        assert beyond and tuple(sorted(beyond)) == beyond and not (set(beyond) & seen) and set(beyond) <= rest
        seen |= set(beyond)
        assert disp in FORK_SET
        r1, b1, f1 = validate_tree(sub, beyond)
        R += r1
        B += b1
        F_ += f1 + 1
    assert seen == rest
    return (R, B, F_)


def examine(eta, x, zeta=None):
    """run the construction at x, extract and validate the history; returns (enc, S, B, R, F, ok)"""
    if zeta is None:
        zeta = {z: 1 for z, v in eta.items() if v and sum(eta.get(pp, 0) for pp in preds(z)) < 2}
    try:
        ex = Explainer(eta, zeta)
        enc, info = history(ex, x)
    except AssertionError:
        return None, 0, 0, 0, 0, False
    ok = info['ok'] and info['moves_ok'] and info['pole_rule_ok']
    try:
        R, B, F_ = validate_cluster(enc)
        ok = ok and (R, B, F_) == (info['R'], info['B'], info['F'])
    except AssertionError:
        return enc, info['S'], info['B'], info['R'], info['F'], False
    ok = ok and info['S'] == F_ + 1 and R <= F_ + B
    try:
        seeds, bads = reconstruct(enc, x)
    except ValueError:
        return enc, info['S'], B, R, F_, False
    ok = ok and sorted(seeds) == sorted(info['seeds']) and sorted(bads) == sorted(info['bad_sites'])
    ok = ok and set(seeds) == info['Sset'] and len(set(seeds)) == len(seeds) and len(set(bads)) == len(bads)
    ok = ok and not (set(seeds) & set(bads)) and all(z in ex.noise for z in seeds) and all(z in ex.amp for z in bads)
    return enc, info['S'], B, R, F_, ok


def eta_configs(x, depth):
    """every configuration of eta' on the cone (outside = 0) with its exponent vector
    (#0-pred ones, #0-pred zeros, #1-pred ones, #1-pred zeros); sites with >= 2 one-predecessors are forced"""
    sites = sorted(cone(x, depth), key=level)
    idx = {z: i for i, z in enumerate(sites)}
    pidx = [[idx.get(pp) for pp in preds(z)] for z in sites]
    n = len(sites)
    vals = [0] * n

    def rec(i, a1, a0, b1, b0):
        if i == n:
            yield dict(zip(sites, vals)), (a1, a0, b1, b0)
            return
        c = sum(vals[j] for j in pidx[i] if j is not None)
        if c >= 2:
            vals[i] = 1
            yield from rec(i + 1, a1, a0, b1, b0)
        elif c == 1:
            vals[i] = 1
            yield from rec(i + 1, a1, a0, b1 + 1, b0)
            vals[i] = 0
            yield from rec(i + 1, a1, a0, b1, b0 + 1)
        else:
            vals[i] = 1
            yield from rec(i + 1, a1 + 1, a0, b1, b0)
            vals[i] = 0
            yield from rec(i + 1, a1, a0 + 1, b1, b0)
        vals[i] = 0

    return rec(0, 0, 0, 0, 0)


def section_b():
    x = (0, 0, 0)
    results = {}
    for depth in (2, 3):
        per_h = {}
        n_conf = n_x = 0
        ok = True
        for eta, expo in eta_configs(x, depth):
            n_conf += 1
            if eta[x] != 1:
                continue
            n_x += 1
            enc, S, B, R, F_, good = examine(eta, x)
            ok = ok and good
            if enc is None:
                continue
            per_h.setdefault(enc, [S, B, R, F_, []])[4].append(expo)
        results[depth] = per_h
        check(f"B{depth - 1}", ok and len(per_h) > 0,
              f"depth-{depth} cone, all {n_conf} configurations of eta' ({n_x} with eta'_x = 1, {len(per_h)} distinct "
              "histories): every refinement's terminals are moves u_k = v_k - e_(d_k) with d_k = k exactly at the bad "
              "pairs; block 25's pole rule holds; every history lies in the grammar with |S| = #forks + 1 and "
              "#refinements <= #forks + #bad; the seeds and bad sites rebuilt from the abstract history alone equal "
              "the realized ones, and are distinct seed sites and amplified sites")
    random.seed(20260918)
    ok = True
    n_expl = 0
    deepest = 0
    for trial in range(1500):
        depth = 3 + trial % 6
        dens = (10, 20, 35, 50)[trial % 4]
        sites = cone(x, depth)
        zeta = {z: 1 for z in sites if random.randrange(100) < dens}
        eta = run_automaton(sites, zeta)
        if eta[x] != 1:
            continue
        n_expl += 1
        enc, S, B, R, F_, good = examine(eta, x, zeta)
        deepest = max(deepest, R)
        ok = ok and good
    check("B3", ok and n_expl > 500,
          f"1500 random cones of depth 3-8 (seed 20260918; {n_expl} with eta'_x = 1, up to {deepest} refinements): "
          "the same checks")
    return results


# ============================================================================================ C: the recursion counts the grammar
def _addc(c, key, v):
    c[key] = c.get(key, 0) + v


def smul(a, b, RM, FM):
    out = {}
    for (r1, b1, f1), v1 in a.items():
        for (r2, b2, f2), v2 in b.items():
            if r1 + r2 <= RM and f1 + f2 <= FM:
                _addc(out, (r1 + r2, b1 + b2, f1 + f2), v1 * v2)
    return out


def sadd(a, b):
    out = dict(a)
    for k, v in b.items():
        _addc(out, k, v)
    return out


def series_Z(RM, FM):
    """coefficients of Z = 1 + s (2 + r)^3 Z / (1 - 6 f Z)^3 in (s, r, f), truncated at s^RM, f^FM"""
    one = {(0, 0, 0): 1}
    Z = dict(one)
    mv = {}
    for d in product(range(3), repeat=3):
        _addc(mv, (1, sum(1 for k in range(3) if d[k] == k), 0), 1)
    for _ in range(RM + FM + 2):
        X = {(k[0], k[1], k[2] + 1): 6 * v for k, v in Z.items() if k[2] + 1 <= FM}
        inv = dict(one)
        P = dict(one)
        for j in range(1, FM + 1):
            P = smul(P, X, RM, FM)
            inv = sadd(inv, P)
        G = smul(Z, smul(inv, smul(inv, inv, RM, FM), RM, FM), RM, FM)
        Z = sadd(one, smul(mv, G, RM, FM))
    return Z


def enum_cluster(RM, FM):
    yield (('seed',), 0, 0, 0)
    if RM < 1:
        return
    for d in product(range(3), repeat=3):
        b = sum(1 for k in range(3) if d[k] == k)
        for tree, R, B, F_ in enum_root_tree(RM - 1, FM):
            yield (('ref', d, tree), R + 1, B + b, F_)


def enum_root_tree(RM, FM):
    for H0 in ((0, 1, 2), (0, 1), (0, 2), (0,)):
        rest = tuple(k for k in (1, 2) if k not in H0)
        groupings = [()] if not rest else ([(rest,)] + ([((1,), (2,))] if rest == (1, 2) else []))
        for grp in groupings:
            for enc0, R0, B0, F0 in enum_cluster(RM, FM):
                yield from _hang(('cl', H0, enc0), list(grp), [], RM - R0, FM - F0, R0, B0, F0)


def _hang(part, grp, kids, RM, FM, R, B, F_):
    if not grp:
        yield (part + (tuple(sorted(kids)),), R, B, F_)
        return
    beyond = grp[0]
    if FM < 1:
        return
    for disp in FORK_OFFSETS:
        for sub, R1, B1, F1 in enum_subtree(beyond, RM, FM - 1):
            yield from _hang(part, grp[1:], kids + [(beyond, disp, sub)], RM - R1, FM - 1 - F1, R + R1, B + B1, F_ + 1 + F1)


def enum_subtree(charges, RM, FM):
    ch = tuple(charges)
    if len(ch) == 1:
        opts = [(ch, ()), ((), (ch,))]
    else:
        a, b = ch
        opts = [(ch, ()), ((a,), ((b,),)), ((b,), ((a,),)), ((), (ch,)), ((), ((a,), (b,)))]
    for Hy, grp in opts:
        for encY, R0, B0, F0 in enum_cluster(RM, FM):
            yield from _hang(('cl', Hy, encY), list(grp), [], RM - R0, FM - F0, R0, B0, F0)


def section_c(results):
    for RM, FM in ((2, 2), (3, 1)):
        Zs = series_Z(RM, FM)
        cnt = {}
        total = 0
        ok_member = True
        for enc, R, B, F_ in enum_cluster(RM, FM):
            _addc(cnt, (R, B, F_), 1)
            total += 1
            if total % 97 == 0:
                ok_member = ok_member and validate_cluster(enc) == (R, B, F_)
        keys = set(Zs) | set(cnt)
        mism = [k for k in keys if Zs.get(k, 0) != cnt.get(k, 0)]
        check(f"C{1 if RM == 2 else 2}", not mism and ok_member,
              f"the series of Z = 1 + s(2 + r)^3 Z/(1 - 6fZ)^3 up to s^{RM}, f^{FM} ({len(keys)} coefficients) equals the "
              f"count of the grammar's histories by (refinements, bad charges, forks) ({total} histories enumerated "
              "directly); sampled enumerated histories pass the membership test")
    # realized histories: counts per (R, B, F) never exceed the coefficient
    Zs = series_Z(6, 3)
    ok = True
    ratios = {}
    for depth in (2, 3):
        cnt = {}
        for enc, (S, B, R, F_, lst) in results[depth].items():
            _addc(cnt, (R, B, F_), 1)
        for k, v in cnt.items():
            if k[0] <= 6 and k[2] <= 3:
                ok = ok and v <= Zs.get(k, 0)
                ratios[k] = max(ratios.get(k, 0), Fraction(v, Zs[k]))
    top = sorted(ratios.items(), key=lambda kv: -kv[1])[:3]
    check("C3", ok,
          "the distinct realized histories of the depth-2 and depth-3 cones, counted by (refinements, bad charges, forks), "
          "never exceed the recursion's coefficient; the three largest ratios: "
          + ", ".join(f"{k}: {v}" for k, v in top))


# ============================================================================================ D: domination on complete cones
def exact_dp(x, depth, e1, e2):
    """independent level-by-level computation of P(eta'_x = 1) on the cone (outside = 0)"""
    levels = {}
    for z in cone(x, depth):
        levels.setdefault(level(z), []).append(z)
    dist = {(): Fraction(1)}
    prev_sites = []
    for L in sorted(levels):
        cur = sorted(levels[L])
        new = {}
        for state, pr in dist.items():
            on = {z for z, v in zip(prev_sites, state) if v}
            ps = []
            for z in cur:
                c = sum(1 for pp in preds(z) if pp in on)
                ps.append(Fraction(1) if c >= 2 else (e2 if c == 1 else e1))
            for bits in product((0, 1), repeat=len(cur)):
                w = pr
                for bb, pz in zip(bits, ps):
                    w *= pz if bb else (1 - pz)
                    if w == 0:
                        break
                if w:
                    new[bits] = new.get(bits, 0) + w
        dist = new
        prev_sites = cur
    return sum(pr for st, pr in dist.items() if st[0] == 1)


def section_d(results, certs):
    x = (0, 0, 0)
    pts = [(Fraction(1, 10), Fraction(1, 5)), (Fraction(1, 3), Fraction(1, 2)), (Fraction(1, 100), Fraction(1, 20))]
    pts += [(eps_pair(*ln)[0], eps_pair(*ln)[1]) for ln in LINES[:2]]
    for depth in (2, 3):
        per_h = results[depth]
        lines = []
        ok = True
        for i, (e1, e2) in enumerate(pts):
            Pex = Fraction(0)
            UB = Fraction(0)
            for enc, (S, B, R, F_, lst) in per_h.items():
                s = sum(e1 ** a1 * (1 - e1) ** a0 * e2 ** b1 * (1 - e2) ** b0 for (a1, a0, b1, b0) in lst)
                w = e1 ** S * e2 ** B
                ok = ok and s <= w
                Pex += s
                UB += w
            Pdp = exact_dp(x, depth, e1, e2)
            ok = ok and Pex == Pdp and Pex <= UB
            if i >= 3:
                sigma, Zb = certs[LINES[i - 3]]
                ok = ok and UB <= e1 * Zb
                lines.append(f"at {LINES[i - 3]} P = {float(Pex):.4g} <= union {float(UB):.4g} <= eps1*Zbar = {float(e1 * Zb):.4g}")
            else:
                lines.append(f"at (eps1, eps2) = ({e1}, {e2}) P = {float(Pex):.4g} <= union {float(UB):.4g}")
        check(f"D{depth - 1}", ok,
              f"depth-{depth} cone: the exact P(eta'_x = 1) (configuration sum = independent level DP) is at most the "
              "sum over realized histories of eps1^|S| eps2^B, each history's configurations weigh at most its "
              "eps1^|S| eps2^B, and at the certificate points the union is at most eps1*Zbar: " + "; ".join(lines))


# ============================================================================================ E: certificates
CERTS = {
    (84, 1, 2): (Fraction(161, 5000), Fraction(5119922891, 1000000000)),
    (44, 1, 1): (Fraction(313, 10000), Fraction(230312929, 50000000)),
    (168, 2, 4): (Fraction(161, 5000), Fraction(5119922891, 1000000000)),
    (125, 1, 3): (Fraction(13, 400), Fraction(655476451, 125000000)),
}


def mu_c(sigma, e1, e2):
    return sigma * (2 + e2 / sigma) ** 3, 6 * e1 / sigma


def section_e():
    rows = []
    ok = True
    for ln in LINES:
        sigma, Zb = CERTS[ln]
        e1, e2 = eps_pair(*ln)
        mu, c = mu_c(sigma, e1, e2)
        good = 0 < sigma <= 1 and Zb >= 1 and c * Zb < 1 and Zb >= 1 + mu * Zb / (1 - c * Zb) ** 3
        ok = ok and good
        rows.append(f"{ln}: sigma = {sigma}, Zbar = {Zb} ({float(Zb):.6f}), mu = {float(mu):.4f}, cZbar = {float(c * Zb):.4f}, "
                    f"bound eps1*Zbar = {float(e1 * Zb):.3e}")
    check("E1", ok,
          "exact super-solutions: 0 < sigma <= 1, c Zbar < 1 and Zbar >= 1 + mu Zbar/(1 - c Zbar)^3 with "
          "mu = sigma(2 + eps2/sigma)^3, c = 6 eps1/sigma, eps1 = d_1, eps2 = max(d_2, d_3); " + "; ".join(rows) +
          ". By A1 the deviations decrease in p, mu and c decrease, and the same Zbar serves every larger p on each line")
    # comparisons with the tree route
    old = {(84, 1, 2): 4165, (44, 1, 1): 2085, (168, 2, 4): 8330, (125, 1, 3): 6247}
    ok = True
    for ln in LINES:
        e1, e2 = eps_pair(*ln)
        ok = ok and e2 > Fraction(256, 531441) and e2 > Fraction(4, 729)
    d3_4150 = deviations(4150, 1, 2)[2]
    d3_367 = deviations(367, 1, 2)[2]
    ok = ok and d3_4150 > Fraction(256, 531441) and d3_367 > Fraction(4, 729)
    check("E2", ok,
          "at every certificate point eps2 > 4/729 > 256/531441, so the tree recursion (domain ending at x = 4/27) "
          "cannot reach these points with either budget c = 2 (ceiling 256/531441, p > 4150 on (p,1,2)) or c = 1 "
          "(ceiling 4/729, p > 367); block 30's thresholds " + ", ".join(f"{old[ln]} on {ln[1:]}" for ln in LINES) +
          " become " + ", ".join(f"{ln[0]}" for ln in LINES))


# ============================================================================================ F: this route's ceiling
def fixed_point_float(mu, c):
    Z = 1.0
    for _ in range(100000):
        if c * Z >= 1:
            return None
        Zn = 1 + mu * Z / (1 - c * Z) ** 3
        if Zn > 1e9:
            return None
        if abs(Zn - Z) < 1e-14:
            return Zn
        Z = Zn
    return None


def section_f():
    s, e = sp.symbols("sigma epsilon", positive=True)
    ident = sp.expand((2 * s + e) ** 3 - 27 * e * s ** 2 - (s - e) ** 2 * (8 * s + e)) == 0
    d3_57, d3_58 = deviations(57, 1, 2)[2], deviations(58, 1, 2)[2]
    d2_58 = deviations(58, 1, 2)[1]
    ok = ident and d3_57 > Fraction(1, 27) >= d3_58 and d2_58 < d3_58
    check("F1", ok,
          "sigma(2 + eps/sigma)^3 - 27 eps = (sigma - eps)^2 (8 sigma + eps)/sigma^2 >= 0, so min over sigma of mu is "
          "27 eps2 (at sigma = eps2) and at eps1 -> 0 the recursion's domain is eps2 < 1/27 (was 256/531441, a factor "
          f"{float(Fraction(531441, 256) / 27):.1f}); on (p,1,2) eps2 = d_3 and d_3(57) = {d3_57} > 1/27 >= d_3(58) = {d3_58}: "
          "the route's ceiling at eps1 -> 0 is p >= 58")
    notes = []
    for ln in LINES:
        p0 = ln[0] - 1
        e1, e2 = eps_pair(p0, ln[1], ln[2])
        found = False
        for i in range(50, 400):
            sigma = i / 10000
            mu = sigma * (2 + float(e2) / sigma) ** 3
            c = 6 * float(e1) / sigma
            if fixed_point_float(mu, c) is not None:
                found = True
                break
        notes.append(f"{(p0,) + ln[1:]}: {'found' if found else 'none'}")
    print("INFO: F2 (numerical, not a claim) fixed point of the recursion for sigma = i/10000, i = 50..399, one step "
          "below each certificate: " + "; ".join(notes))


def main():
    try:
        return run_all()
    except Exception as exc:  # a crash is reported, never silent
        print(f"FAIL: X unexpected exception {type(exc).__name__}: {exc}")
        print("SUMMARY: ROUTE FAILS AT an unexpected exception in check.py")
        return 1


def run_all():
    section_a()
    results = section_b()
    section_c(results)
    certs = {ln: CERTS[ln] for ln in LINES}
    section_d(results, certs)
    section_e()
    section_f()
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    if FAILS == 0:
        print("SUMMARY: PARTIAL counting the construction's refinement histories instead of its explanation trees gives "
              "P(eta'_x = 1) <= eps1 Zbar for any super-solution of Z = 1 + mu Z/(1 - cZ)^3, mu = sigma(2 + eps2/sigma)^3, "
              "c = 6 eps1/sigma (conditional on block 30's T1-T2 and block 25's T3); exact certificates: the formation "
              "law keeps its plane for p >= 84 on (p,1,2), 44 on (p,1,1), 168 on (p,2,4), 125 on (p,1,3) (block 30: "
              "4165, 2085, 8330, 6247; tree-route ceilings p > 4150 and p > 367); this route's own ceiling at eps1 -> 0 "
              "is eps2 < 1/27 (p >= 58 on (p,1,2)); the located strength 10.5-11 is not reached")
        print("HIT: new exact partial result: the refinement-history count Z = 1 + sigma(2 + eps2/sigma)^3 Z/(1 - 6 eps1 Z/sigma)^3 "
              "replaces the explanation-tree count and its 4/27 ceiling; exact certificates give P(v_x != a) <= eps1 Zbar "
              "< 3e-4 for p >= 84 on (p,1,2) (was 4165), 44 on (p,1,1), 168 on (p,2,4), 125 on (p,1,3)")
    else:
        print("SUMMARY: ROUTE FAILS AT a failed check (see FAIL lines)")
    return 0 if FAILS == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
