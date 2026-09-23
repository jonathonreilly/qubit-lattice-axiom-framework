#!/usr/bin/env python3
"""Exact finite marked-automaton witness counts, local charge accounting and
rational polynomial certificates. Global negative certification and a sharp
constant two are deferred; no physical threshold is obtained. All three exact
witness fixtures and the original seeded300-cone sample are retained. This
primary runs no historical hill-climb or annealing search and writes stdout.
"""

from __future__ import annotations

import hashlib
import random
import re
import sys
from collections import deque
from fractions import Fraction
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/EXTENDED_EXPLANATION_TREE_FINITE_WITNESS_COUNTS_AND_RATIONAL_RECURSION_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
INPUT_SHA256 = {'docs/EXTENDED_EXPLANATION_TREE_FINITE_WITNESS_COUNTS_AND_RATIONAL_RECURSION_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'a0c558c7d98c573f32a148724c3c3629c3aeca818d286f1df2024f870dc6f072', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md': 'cc7e8423b3bb35f7f2cf4699d498556b98fbc55229eb8a5d9f52e1ba00a63f97'}
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "extended_explanation_tree_finite_witness_counts_and_rational_recursion_certificates_bounded_theorem_note_2026-09-16"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "rise_identity_wrong": "B",
    "period_arithmetic_wrong": "B",
    "period_counts_wrong": "B",
    "witness_marks_wrong": "C",
    "sharper_budget_asserted": "C",
    "witness_ratio_wrong": "C",
    "certificate_wrong": "D",
    "ceiling_c1_wrong": "D",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


# ============================================================================================ the extended construction of block 30 (re-embedded, with a per-refinement log)
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
        self.log = []
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
            a_i = e_i = 0
            for v, j in kept.items():
                if v in self.amp:
                    edges[frozenset([v, preds(v)[self.amp_dir[v]]])] = "amp"
                    amp_nodes.add(v); a_i += 1
                else:
                    edges[frozenset([v, u[j]])] = "arrow"
                    processed.add(v); e_i += 1
            nforks = sum(1 for i in tree_nodes if fam[i][0] == "fork")
            fork_span = sum(sum(M(jj, pole_of[i][jj]) for jj in range(3)) for i in tree_nodes if fam[i][0] == "fork")
            rise = 1 - bad + nforks - fork_span
            self.log.append((bad, len(kept), a_i, e_i, nforks, rise, len(set(poles))))
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


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "the pinned context-only product-law note carries its identity and product-form heading")
    checks.check("A4", all(Path(ROOT, p).is_file() and hashlib.sha256(Path(ROOT, p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all three declared source/context inputs match literal SHA-256 pins")


# ============================================================================================ the witnesses (T2)
# noise marks (the one-sided automaton's flips); the rule fills the rest.  W1 is self-contained: its marks are exactly the tree's seed and amplified nodes.
W1 = ((3, 3, 4), (4, 4, 7), [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 2), (1, 2, 0), (1, 3, 1), (2, 0, 0), (2, 2, 3), (2, 3, 4), (3, 0, 2)])
W2 = ((3, 3, 6), (4, 4, 7), [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 5), (0, 1, 0), (0, 1, 2), (0, 1, 3), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 5), (0, 2, 6), (0, 3, 1), (0, 3, 2), (0, 3, 5), (0, 3, 6), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 1), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 2), (2, 0, 3), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5), (2, 3, 1), (2, 3, 5), (2, 3, 6), (3, 0, 0), (3, 2, 2), (3, 3, 1), (3, 3, 2), (3, 3, 5)])
W3 = ((4, 4, 5), (5, 5, 9), [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 4), (0, 1, 0), (0, 1, 5), (0, 2, 3), (0, 2, 8), (0, 3, 1), (0, 3, 3), (0, 3, 4), (0, 4, 3), (0, 4, 4), (0, 4, 5), (0, 4, 6), (0, 4, 7), (1, 0, 0), (1, 0, 1), (1, 0, 4), (1, 1, 0), (1, 1, 1), (1, 1, 5), (1, 1, 7), (1, 2, 8), (1, 3, 8), (2, 0, 0), (2, 1, 1), (2, 1, 5), (2, 1, 6), (2, 1, 8), (2, 2, 0), (2, 2, 1), (2, 2, 6), (2, 2, 7), (2, 2, 8), (2, 3, 1), (2, 3, 2), (2, 3, 3), (2, 3, 8), (2, 4, 0), (2, 4, 2), (3, 0, 2), (3, 0, 8), (3, 1, 6), (3, 1, 7), (3, 2, 0), (3, 2, 2), (3, 2, 6), (3, 2, 7), (3, 2, 8), (3, 3, 1), (3, 3, 2), (3, 3, 4), (3, 3, 7), (3, 4, 3), (3, 4, 5), (4, 0, 2), (4, 0, 4), (4, 0, 5), (4, 0, 6), (4, 1, 0), (4, 1, 4), (4, 1, 6), (4, 1, 7), (4, 1, 8), (4, 2, 0), (4, 2, 2), (4, 2, 6), (4, 3, 0), (4, 3, 1), (4, 3, 6), (4, 4, 2), (4, 4, 6), (4, 4, 8)])


def run_witness(w, drop=None):
    root, (A_, B_, L_), marks = w
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    zeta = {z: 1 for z in marks if z != drop}
    eta = run_automaton(sites, zeta)
    if eta.get(root, 0) != 1:
        return None
    ex = Explainer(eta, zeta)
    nodes, edges, S, A, refs, bad = ex.explain(root)
    ok = check_tree(nodes, edges, root, ex)
    # independent recount of the tree's marks and arrows
    npred = {v: sum(eta.get(p, 0) for p in preds(v)) for v in nodes}
    E_ = Fk = Am = 0
    for e, kind in edges.items():
        a, b = tuple(e)
        if kind == "fork":
            Fk += 1
            continue
        upper = a if b in preds(a) else b
        lower = b if upper == a else a
        if kind == "arrow":
            E_ += 1
            ok = ok and npred[upper] >= 2 and eta.get(lower, 0) == 1
        else:
            Am += 1
            ok = ok and npred[upper] == 1 and eta.get(lower, 0) == 1 and lower == preds(upper)[ex.amp_dir[upper]]
    ok = ok and all(npred[s] == 0 for s in S) and all(npred[a] == 1 for a in A) and Am == len(A)
    return dict(ok=ok, E=E_, A=len(A), S=len(S), F=Fk, refs=refs, bad=bad, log=list(ex.log), ones=len(ex.ones), nodes=len(nodes))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    j = 1
    v = (2, -1, -1)
    w = sub(v, E[j])
    inc = [M(kk, w) - M(kk, v) for kk in range(3)]
    checks.check("B1", inc == [Fraction(1, 3), Fraction(-2, 3), Fraction(1, 3)], "T1: an amplified site's excuse (its single predecessor v - e_j) raises the charges k != j by 1/3 and lowers the charge j by 2/3: a bad pair costs one unit of span")
    ok = True
    for w_ in (W1, W2, W3):
        r = run_witness(w_)
        ok = ok and r is not None and r["ok"]
        rises = [entry[5] for entry in r["log"]]
        forks_target = r["F"] + (1 if mut("rise_identity_wrong") else 0)
        ok = ok and sum(rises) == forks_target
        ok = ok and all((entry[4] > 0 or entry[5] == 1 - entry[0]) and entry[5] <= 1 - entry[0] + entry[4] for entry in r["log"])
        ok = ok and sum(entry[3] for entry in r["log"]) == r["E"] and sum(entry[2] for entry in r["log"]) == r["A"] and sum(entry[0] for entry in r["log"]) == r["bad"]
        ok = ok and all(entry[0] <= entry[2] and entry[2] + entry[3] == entry[1] <= 3 for entry in r["log"])
    checks.check("B2", ok, "T1: on the three witnesses the rise of the potential at a fork-free refinement is 1 - b and at most 1 - b + (forks created) otherwise, the rises sum to the number of forks, the excuse arrows and amplified nodes sum to E and |A| over the refinements, b <= a and e + a = kept <= 3 at every refinement")
    # B3: the two-level period, from the identities and as realised in the witnesses' logs
    period_e = 3 if mut("period_arithmetic_wrong") else 4
    ok3 = True
    pairs_total = 0
    per_witness_pairs = []
    expected_pairs = (2, 2, 0) if mut("period_counts_wrong") else (2, 1, 1)
    for w_ in (W1, W2, W3):
        log = run_witness(w_)["log"]
        pairs = 0
        for i in range(len(log) - 1):
            a_, b_ = log[i], log[i + 1]
            if a_[:6] == (0, 3, 0, 3, 0, 1) and b_[:6] == (2, 3, 2, 1, 0, -1):
                pairs += 1
                ok3 = ok3 and a_[3] + b_[3] == period_e and a_[2] + b_[2] == 2 and a_[5] + b_[5] == 0
        pairs_total += pairs
        per_witness_pairs.append(pairs)
    checks.check("B3", ok3 and tuple(per_witness_pairs) == expected_pairs and pairs_total == 4, f"T1: a fork-free refinement with three processed poles (rise 1, three excuse arrows) followed by one with two bad poles and one processed pole (rise -1, one excuse arrow, two amplified nodes) is rise-neutral with four excuse arrows per two amplified nodes — the period of ratio 2; the exact per-witness counts are {tuple(per_witness_pairs)}, total {pairs_total}; no global sharpness follows")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    slack = 1 if mut("sharper_budget_asserted") else 2
    r1 = run_witness(W1, drop=(2, 0, 0) if mut("witness_marks_wrong") else None)
    ok1 = r1 is not None and r1["ok"] and (r1["E"], r1["A"], r1["S"], r1["F"], r1["refs"], r1["bad"]) == (16, 10, 1, 0, 10, 10)
    ok1 = ok1 and r1["E"] <= 3 * (r1["S"] - 1) + slack * r1["A"] and r1["E"] - 3 * (r1["S"] - 1) - r1["A"] == 6 and Fraction(r1["E"] - 3 * (r1["S"] - 1), r1["A"]) == Fraction(8, 5)
    checks.check("C1", ok1, "T2: witness W1 (window 4x4x7, root (3,3,4), 11 noise marks = the tree's seed and ten amplified nodes): the tree is valid with E = 16, |A| = 10, |S| = 1, no fork, 10 refinements, 10 bad pairs; the comparison expression with coefficient two 3(|S|-1) + 2|A| = 20 holds; the arithmetic difference E-[3(|S|-1)+|A|] equals6: the ratio is 8/5")
    r2 = run_witness(W2)
    target = Fraction(4, 3) if mut("witness_ratio_wrong") else Fraction(5, 3)
    ok2 = r2 is not None and r2["ok"] and (r2["E"], r2["A"], r2["S"], r2["F"]) == (20, 12, 1, 0) and Fraction(r2["E"] - 3 * (r2["S"] - 1), r2["A"]) == target and r2["E"] <= 3 * (r2["S"] - 1) + 2 * r2["A"]
    r3 = run_witness(W3)
    ok3 = r3 is not None and r3["ok"] and (r3["E"], r3["A"], r3["S"]) == (23, 12, 2) and Fraction(r3["E"] - 3 * (r3["S"] - 1), r3["A"]) == target and r3["E"] <= 3 * (r3["S"] - 1) + 2 * r3["A"]
    checks.check("C2", ok2 and ok3, "T2: witnesses W2 (window 4x4x7, root (3,3,6): E = 20, |A| = 12, |S| = 1) and W3 (window 5x5x9, root (4,4,5): E = 23, |A| = 12, |S| = 2, one fork) are valid trees with ratio 5/3, within the comparison expression with coefficient two")
    # C3: the local patterns that defeat a per-refinement proof (on the unmutated W1)
    r1u = run_witness(W1)
    log = r1u["log"]
    two_e = sum(1 for en in log if en[0] >= 1 and en[3] == 2 and en[5] == 0)
    two_bad = sum(1 for en in log if en[0] == 2 and en[3] == 1 and en[5] == -1)
    checks.check("C3", two_e >= 1 and two_bad >= 1 and all(en[3] > 3 * en[5] + en[2] for en in log if (en[0] >= 1 and en[3] == 2 and en[5] == 0) or (en[0] == 2 and en[3] == 1 and en[5] == -1)), f"T2: W1 contains {two_e} refinement(s) with a bad pole, two excuse arrows and rise 0, and {two_bad} with two bad poles, one excuse arrow and rise -1; at each, e > 3 rise + a, these are exact local arithmetic comparisons; formal negative certification remains deferred")
    # C4: uniform sampling's blind spot
    random.seed(31)
    worst = Fraction(-100)
    cases = 0
    x = (0, 0, 0)
    for trial in range(300):
        depth = 3 + trial % 6
        dens = (10, 20, 35, 50)[trial % 4]
        sites = cone(x, depth)
        zeta = {z: 1 for z in sites if random.randrange(100) < dens}
        eta = run_automaton(sites, zeta)
        if eta[x] != 1:
            continue
        ex = Explainer(eta, zeta)
        nodes, edges, S, A, refs, bad = ex.explain(x)
        cases += 1
        if A:
            E_ = sum(1 for e, k in edges.items() if k == "arrow")
            worst = max(worst, Fraction(E_ - 3 * (len(S) - 1), len(A)))
    checks.check("C4", cases > 100 and worst <= 1 < Fraction(8, 5), f"T2: 300 uniformly random cones of depth 3-8 ({cases} explained) never exceed the ratio 1 (worst {worst}), while the witnesses reach 8/5 and 5/3: this fixed seeded sample is not a global upper bound")
    # C5: the witnesses' refinements all fork-free except W3's single fork; bad = |A| in W1 and W2 (every amplified node kept is a bad pole)
    checks.check("C5", r1u["bad"] == r1u["A"] and r2["bad"] == r2["A"] and r3["F"] == 1 and r1u["nodes"] == 27 and r2["nodes"] == 33, "T2: in W1 and W2 every amplified node of the tree is a bad pole (b = |A|), W1 has 27 nodes and W2 33, and W3 carries exactly one fork (its two seeds)")


# ============================================================================================ family D
def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def family_d(checks: Checks) -> None:
    certs = {
        (453, 1, 2): (Fraction(77, 1000), Fraction(530590310409, 62500000000), Fraction(2581678475343, 1000000000000), Fraction(11343276538931, 1000000000000)),
        (232, 1, 1): (Fraction(19, 250), Fraction(3177134369, 390625000), Fraction(2565214474763, 1000000000000), Fraction(10810979357851, 1000000000000)),
        (905, 2, 4): (Fraction(39, 500), Fraction(8819680764063, 1000000000000), Fraction(2607018650019, 1000000000000), Fraction(2955282963089, 250000000000)),
        (677, 1, 3): (Fraction(77, 1000), Fraction(8860200884553, 1000000000000), Fraction(1306536163573, 500000000000), Fraction(5937627036121, 500000000000)),
    }
    ok = True
    for (pv, qv, rv), (t, Db, Ub, Fb) in certs.items():
        d1, d2, d3 = deviations(pv, qv, rv)
        e1, e2 = d1, max(d2, d3)
        if mut("certificate_wrong"):
            e2 = e2 * Fraction(11, 10)
        xx, yy = t + e2 / t, e1 / t ** 3
        rD = (1 + xx * Ub) ** 2 * (1 + 3 * xx * Db) * (1 + yy * Fb) ** 6
        rU = (1 + xx * Ub) ** 3 * (1 + yy * Fb) ** 6
        rF = (1 + xx * Ub) ** 3 * (1 + 3 * xx * Db) * (1 + yy * Fb) ** 5
        Rbar = (1 + xx * Ub) ** 3 * (1 + 3 * xx * Db) * (1 + yy * Fb) ** 6
        ok = ok and Db >= rD and Ub >= rU and Fb >= rF and min(Db, Ub, Fb) >= 1 and xx < Fraction(4, 27) and e1 * Rbar < Fraction(1, 10 ** 5)
    checks.check("D1", ok, "T3: at the declared algebraic weight epsilon_2/t the rational triples at (453,1,2), (232,1,1), (905,2,4), (677,1,3) with t = 77/1000, 19/250, 39/500, 77/1000 are exact super-solutions at (t + epsilon_2/t, epsilon_1/t^3) with epsilon_1 R-bar < 10^-5: pure polynomial inequalities, not a formation region")
    t = sp.symbols("t", positive=True)
    top = sp.Rational(4, 729) if not mut("ceiling_c1_wrong") else sp.Rational(5, 729)
    m = sp.maximum(t * (sp.Rational(4, 27) - t), t, sp.Interval(0, sp.Rational(4, 27)))
    ok2 = sp.simplify(m - top) == 0 and sp.simplify((t * (sp.Rational(4, 27) - t)).subs(t, sp.Rational(2, 27)) - sp.Rational(4, 729)) == 0
    d3a = deviations(367, 1, 2)[2]
    d3b = deviations(368, 1, 2)[2]
    ok2 = ok2 and d3a > Fraction(4, 729) > d3b
    checks.check("D2", ok2, f"T3: the declared scalar expression has maximum max_t t (4/27 - t) = 4/729 at t = 2/27, crossed on (p, 1, 2) between p = 367 and 368 (d_3(367) = {d3a}, d_3(368) = {d3b}); this algebra does not establish any universal construction budget or formation region")
    ratios = [Fraction(4165, 453), Fraction(2085, 232), Fraction(8330, 905), Fraction(6247, 677)]
    checks.check("D3", all(r > 8 for r in ratios) and all(r < 10 for r in ratios), "T3 (the stake): the four historical comparison numbers differ by a factor between 8 and 10 (4165 -> 453, 2085 -> 232, 8330 -> 905, 6247 -> 677); none of it is claimed")


# ============================================================================================ family F
FENCES = ('This note retains exact finite construction counts, local charge identities and rational polynomial certificates for explicitly declared objects; no physical rule, order or coupling is selected.', 'A local ratio-two period does not establish a sharp global constant; the universal upper budget is not imported from an open handoff.', 'Formal negative certification is deferred in the readable recovery argument; finite witness validity is not a claim of five closed attack families.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "optimal", "cannot be improved", "best possible",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 4165."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Gács", "Swart", "Szabó", "Toninelli", "Bramson", "Gray", "Krylov", "Bogolyubov", "Choquet", "Peierls", "Dobrushin")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T2", "## Theorem T2 (after Toom)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in sec:
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if nm in sections[0]]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = ('per_element: executed — exact rational charge increments and local rise/count identities on every refinement of the three specified witnesses', 'per_site: executed — three marked windows of112,112,225sites, tree connectivity and live-predecessor edge types; unchanged finite fixtures', 'per_mode: checked and not executed — no spectral decomposition is present; witness classes and seeded cones are finite configurations, not modes', 'per_block: executed — exact witness period counts2,1,1, the fixed seeded300-cone sample, four rational certificates and scalar completed-square maximum', 'lattice_wide: checked and not executed — no exhaustive input search, infinite lattice simulation, sharp global budget or formal negative certification')


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


# ============================================================================================ main
def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
