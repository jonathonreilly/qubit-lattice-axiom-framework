#!/usr/bin/env python3
"""Exact checks: the six-axis formation threshold lifted by a two-level domination — seeds and amplified nodes in the explanation tree.

Scope. Supplied p >= q > 0, r > 0. T1: the three deviations' closed forms, their monotonicity in p, d_1 <= max(d_2, d_3), and the two-level coupling inequality
at every predecessor state.  T2: the extended construction (amplified sites inside clusters; an amplified pole's excuse is its single
predecessor; bad pairs; bad amplified poles kept) executed on every configuration of the depth-2 cone, every depth-3 configuration with
at most four noise sites and random cones, with the tree, the classification, the identity Span + 1 - b at every refinement,
forks = |S| - 1, refinements <= |S| - 1 + B, B <= |A| and E <= 3(|S| - 1) + 2|A|.  T3: the lift's slot structure on subtrees with
<= 4 edges (counts against the recursion's coefficients).  T4: the four super-solution certificates and the bounds.  T5: the ceiling
4/27 and 256/531441 symbolically, and d_3(4150) > 256/531441.  Exact arithmetic only (integers, Fractions and sympy); the exact arithmetic bodies are preserved; no float-scan or prose-count PASS is used.
"""

from __future__ import annotations

import random
import hashlib
import json
import re
import sys
from collections import deque
from fractions import Fraction
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_MEMORY_MB = 768
AUDIT_INPUT_PATHS = ('docs/SIX_AXIS_TWO_LEVEL_DOMINATION_EXTENDED_EXPLANATION_TREE_AND_FOUR_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md', 'docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md')
EXPECTED_INPUT_SHA256 = {'docs/SIX_AXIS_TWO_LEVEL_DOMINATION_EXTENDED_EXPLANATION_TREE_AND_FOUR_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md': '5642877329c141c39394936173c35c82c5cd18bb8f9a408c17fad0497cef647e', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md': 'cc7e8423b3bb35f7f2cf4699d498556b98fbc55229eb8a5d9f52e1ba00a63f97', 'docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md': '01b4ca057540b1f84b261f5b7ce4328540b7efa9ca845a95c14e9952a75006e2'}
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "six_axis_two_level_domination_extended_explanation_tree_and_four_rational_certificates_bounded_theorem_note_2026-09-16"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "deviation_closed_form_wrong": "B",
    "domination_state_wrong": "B",
    "spanning_identity_wrong": "C",
    "budget_amplified_dropped": "C",
    "bad_pairs_wrong": "C",
    "forks_identity_wrong": "C",
    "subtree_bound_wrong": "D",
    "certificate_wrong": "D",
    "ceiling_wrong": "E",
    "domination_domain_wrong": "B",
    "ceiling_endpoint_wrong": "E",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.results = []
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        self.results.append(dict(tag=tag, passed=bool(ok), detail=msg))
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


# ============================================================================================ the extended construction (T2)
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
            assert expected == sum(M(j, poles[j]) for j in range(3)) + 1 - bad + (1 if mut("spanning_identity_wrong") and bad > 0 else 0)
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


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01, single_noise = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four framework sentences used by the conditional model")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "block 01's note (on main) carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT, p).exists() and hashlib.sha256(Path(ROOT, p).read_bytes()).hexdigest() == EXPECTED_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all declared inputs exist and match exact pins, including the single-noise comparison parent")


# ============================================================================================ family B
def phi_of(v, w, p, q, r):
    if v == w:
        return p
    if v == (w ^ 1):
        return q
    return r


def conditional(a, triple, p, q, r):
    ws = [phi_of(v, triple[0], p, q, r) * phi_of(v, triple[1], p, q, r) * phi_of(v, triple[2], p, q, r) for v in range(6)]
    return ws[a] / sum(ws)


def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def family_b(checks: Checks) -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    if mut("deviation_closed_form_wrong"):
        d2 = 1 - p ** 2 * q / (p * q * (p + q) + 2 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    ok = True
    for (pv, qv, rv) in ((3, 1, 2), (10, 1, 2), (30, 1, 2), (7, 3, 5)):
        subs = {p: pv, q: qv, r: rv}
        c1 = conditional(0, (0, 0, 0), Fraction(pv), Fraction(qv), Fraction(rv))
        c2 = conditional(0, (0, 0, 1), Fraction(pv), Fraction(qv), Fraction(rv))
        c3 = conditional(0, (0, 0, 2), Fraction(pv), Fraction(qv), Fraction(rv))
        ok = ok and sp.Rational(1) - sp.Rational(c1.numerator, c1.denominator) == d1.subs(subs) and sp.Rational(1) - sp.Rational(c2.numerator, c2.denominator) == d2.subs(subs) and sp.Rational(1) - sp.Rational(c3.numerator, c3.denominator) == d3.subs(subs)
    derivatives = (
        -3*p**2*(q**3+4*r**3)/(p**3+q**3+4*r**3)**2,
        -(q**3*p**2+8*q*r**3*p)/(p*q*(p+q)+4*r**3)**2,
        -p*(r*p+2*q**2+2*r*q+4*r**2)/(p**2+q**2+r*(p+q)+2*r**2)**2,
    )
    der_ok = all(sp.simplify(sp.diff(d,p)-expected)==0 for d,expected in zip((d1,d2,d3),derivatives))
    checks.check("B1", ok and der_ok, "Three exact closed forms and all three explicit strictly negative derivative identities for positive weights")
    gap = p**2*(p-q)*(q**2*(p+q)+4*r**3)/((p**3+q**3+4*r**3)*(p*q*(p+q)+4*r**3))
    small = deviations(Fraction(1,10),1,1)
    domain_ok = sp.simplify(d2-d1-gap)==0 and small==(Fraction(5000,5001),Fraction(410,411),Fraction(410,411))
    domain_ok = domain_ok and (small[0] <= max(small[1:]) if mut("domination_domain_wrong") else small[0] > max(small[1:]))
    checks.check("B3", domain_ok, "Exact p>=q domination factorization and small-p counterexample to the withdrawn unrestricted domain")
    # d_1 <= max(d_2, d_3) and the two-level coupling inequality at every predecessor state, at the four lines' thresholds and at (11, 1, 2)
    ok2 = True
    for (pv, qv, rv) in ((4165, 1, 2), (2085, 1, 1), (8330, 2, 4), (6247, 1, 3), (11, 1, 2)):
        e1, e2 = deviations(pv, qv, rv)[0], max(deviations(pv, qv, rv)[1:])
        ok2 = ok2 and e1 <= e2
        for triple in product(range(6), repeat=3):
            n_a = sum(1 for v in triple if v == 0)
            dev = 1 - conditional(0, triple, Fraction(pv), Fraction(qv), Fraction(rv))
            if n_a == 3:
                ok2 = ok2 and dev <= e1
            elif n_a == 2:
                bound = e2 if not mut("domination_state_wrong") else e1
                ok2 = ok2 and dev <= bound
    checks.check("B2", ok2, "T1(b): at the four thresholds and at (11, 1, 2): d_1 <= max(d_2, d_3); a site whose three predecessors equal a dissents with probability at most epsilon_1 and one with exactly two equal to a with probability at most epsilon_2 (all 216 triples)")


# ============================================================================================ family C
def test_config(x, sites, zeta, stats):
    eta = run_automaton(sites, zeta)
    if eta[x] != 1:
        return True
    ex = Explainer(eta, zeta)
    try:
        nodes, edges, S, A, refs, bad = ex.explain(x)
    except AssertionError:
        return False
    ok = check_tree(nodes, edges, x, ex)
    downs = {v: 0 for v in nodes}
    E = Fk = Am = 0
    for e, kind in edges.items():
        a, b = tuple(e)
        if kind == "fork":
            Fk += 1
            continue
        upper = a if b in preds(a) else b
        downs[upper] += 1
        if kind == "arrow":
            E += 1
        else:
            Am += 1
    nS, nA = len(S), len(A)
    ok = ok and all(z in ex.noise for z in S) and all(z in ex.amp for z in A) and max(downs.values()) <= 1
    ok = ok and {v for v in nodes if downs[v] == 0} == S and Am == nA
    forks_target = nS - 1 if not mut("forks_identity_wrong") else nS
    ok = ok and Fk == forks_target and refs <= nS - 1 + bad
    ok = ok and (bad <= nA if not mut("bad_pairs_wrong") else bad == 0)
    slack = 2 if not mut("budget_amplified_dropped") else 0
    ok = ok and E <= 3 * (nS - 1) + slack * nA
    stats["cases"] += 1
    stats["withA"] += (nA > 0)
    if nA > 0:
        stats["worst"] = max(stats["worst"], Fraction(E - 3 * (nS - 1), nA))
    return ok


def family_c(checks: Checks) -> None:
    x = (0, 0, 0)
    # C1: increments of an amplified excuse
    k, j = 1, 1
    v = (2, -1, -1)
    w = sub(v, E[j])
    inc = [M(kk, w) - M(kk, v) for kk in range(3)]
    checks.check("C1", inc == [Fraction(1, 3), Fraction(-2, 3), Fraction(1, 3)], "T2.2: an amplified site's excuse (its single predecessor v - e_j) raises the charges k != j by 1/3 and lowers the charge j by 2/3, so a bad pair costs exactly one unit of span")
    stats = {"cases": 0, "withA": 0, "worst": Fraction(-100)}
    sites2 = cone(x, 2)
    ok1 = True
    for bits in product((0, 1), repeat=len(sites2)):
        zeta = {z: b for z, b in zip(sites2, bits) if b}
        ok1 = ok1 and test_config(x, sites2, zeta, stats)
    checks.check("C2", ok1 and stats["cases"] == 932, f"T2: on all 1024 noise configurations of the depth-2 cone ({stats['cases']} explained, {stats['withA']} with amplified nodes) the extended construction builds a tree through 1-sites with seeds without 1-predecessors and amplified nodes with exactly one, the identity Span + 1 - b holds at every refinement, forks = |S| - 1, refinements <= |S| - 1 + B, B <= |A| and E <= 3(|S| - 1) + 2|A|")
    stats3 = {"cases": 0, "withA": 0, "worst": Fraction(-100)}
    sites3 = cone(x, 3)
    ok2 = True
    for kk in range(1, 5):
        for combo in combinations(sites3, kk):
            ok2 = ok2 and test_config(x, sites3, {z: 1 for z in combo}, stats3)
    random.seed(30)
    stats4 = {"cases": 0, "withA": 0, "worst": Fraction(-100)}
    for trial in range(1200):
        depth = 3 + trial % 6
        dens = (10, 20, 35, 50)[trial % 4]
        sites = cone(x, depth)
        zeta = {z: 1 for z in sites if random.randrange(100) < dens}
        ok2 = ok2 and test_config(x, sites, zeta, stats4)
    checks.check("C3", ok2 and stats3["cases"] == 2321 and stats4["cases"] > 400, f"T2: every depth-3 configuration with at most four noise sites ({stats3['cases']} explained) and 1200 random cones of depth 3-8 ({stats4['cases']} explained, {stats4['withA']} with amplified nodes) pass the same checks")
    worst = max(stats["worst"], stats3["worst"], stats4["worst"])
    checks.check("C4", worst <= Fraction(2, 3), f"T2: the largest executed value of (E - 3(|S| - 1))/|A| over trees with amplified nodes is {worst} (the proved budget allows 2)")


# ============================================================================================ family D
TYPES = [("down", j) for j in range(3)] + [("up", j) for j in range(3)] + [("fork", (i, j)) for i in range(3) for j in range(3) if i != j]


def step(v, ty):
    kind, d = ty
    if kind == "down":
        return sub(v, E[d])
    if kind == "up":
        return add(v, E[d])
    return add(sub(v, E[d[1]]), E[d[0]])


def gf_coefficients(A, FM, up_slots=3):
    def pmul(P, Q):
        R = {}
        for (a1, f1), c1 in P.items():
            for (a2, f2), c2 in Q.items():
                if a1 + a2 <= A and f1 + f2 <= FM:
                    R[(a1 + a2, f1 + f2)] = R.get((a1 + a2, f1 + f2), 0) + c1 * c2
        return R

    def ppow(P, n):
        R = {(0, 0): 1}
        for _ in range(n):
            R = pmul(R, P)
        return R

    def one_plus(P, c, da, df):
        R = {(0, 0): 1}
        for (a, f), v in P.items():
            if a + da <= A and f + df <= FM:
                R[(a + da, f + df)] = R.get((a + da, f + df), 0) + c * v
        return R

    D = U = Fp = {(0, 0): 1}
    for _ in range(A + FM + 1):
        xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(Fp, 1, 0, 1)
        D, U, Fp = pmul(pmul(ppow(xU, 2), xD3), ppow(yF, 6)), pmul(ppow(xU, up_slots), ppow(yF, 6)), pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 5))
    xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(Fp, 1, 0, 1)
    return pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 6))


def exp_bounds(x: Fraction, terms=None):
    n = terms if terms is not None else 2 * (int(x) + 1) + 40
    lo = Fraction(0)
    term = Fraction(1)
    for k in range(n + 1):
        lo += term
        term = term * x / (k + 1)
    return lo, lo + term / (1 - x / (n + 2))


def family_d(checks: Checks) -> None:
    x = (0, 0, 0)
    trees = {frozenset()}
    counts = {(0, 0): 1}
    for _ in range(4):
        nxt = set()
        for T in trees:
            nodes = {x} | {c for (_p, c, _t) in T}
            downs = {v: 0 for v in nodes}
            for (p, c, ty) in T:
                if ty[0] == "down":
                    downs[p] += 1
                if ty[0] == "up":
                    downs[c] += 1
            for v in nodes:
                for ty in TYPES:
                    w = step(v, ty)
                    if w in nodes or (ty[0] == "down" and downs[v] >= 1):
                        continue
                    nxt.add(T | {(v, w, ty)})
        trees = nxt
        for T in trees:
            a = sum(1 for e in T if e[2][0] != "fork")
            counts[(a, len(T) - a)] = counts.get((a, len(T) - a), 0) + 1
    coeff = gf_coefficients(5, 5, up_slots=2 if mut("subtree_bound_wrong") else 3)
    within = all(c <= coeff.get(k, 0) for k, c in counts.items())
    checks.check("D1", sum(counts.values()) == 66103 and within, f"T3: the {sum(counts.values())} subtrees of G with at most four edges and at most one arrow to a predecessor per node, by (arrows, forks), are each at most the recursion's coefficient — the lift with both kinds of arrow in the arrow slots")
    certs = {
        (4165, 1, 2): (Fraction(99, 1000), Fraction(56694252249173, 500000000000), Fraction(3279872914431, 1000000000000), Fraction(168429466648591, 1000000000000)),
        (2085, 1, 1): (Fraction(49, 500), Fraction(88632394933177, 1000000000000), Fraction(3254100818939, 1000000000000), Fraction(131311435970231, 1000000000000)),
        (8330, 2, 4): (Fraction(99, 1000), Fraction(56694252249173, 500000000000), Fraction(3279872914431, 1000000000000), Fraction(168429466648591, 1000000000000)),
        (6247, 1, 3): (Fraction(99, 1000), Fraction(24445325573453, 250000000000), Fraction(3264868815393, 1000000000000), Fraction(9064364177089, 62500000000)),
    }
    ok = True
    bounds = {}
    for (pv, qv, rv), (t, Db, Ub, Fb) in certs.items():
        d1, d2, d3 = deviations(pv, qv, rv)
        e1, e2 = d1, max(d2, d3)
        if mut("certificate_wrong"):
            e2 = e2 * Fraction(11, 10)
        xx, yy = t + e2 / t ** 2, e1 / t ** 3
        rD = (1 + xx * Ub) ** 2 * (1 + 3 * xx * Db) * (1 + yy * Fb) ** 6
        rU = (1 + xx * Ub) ** 3 * (1 + yy * Fb) ** 6
        rF = (1 + xx * Ub) ** 3 * (1 + 3 * xx * Db) * (1 + yy * Fb) ** 5
        Rbar = (1 + xx * Ub) ** 3 * (1 + 3 * xx * Db) * (1 + yy * Fb) ** 6
        ok = ok and Db >= rD and Ub >= rU and Fb >= rF and min(Db, Ub, Fb) >= 1 and t <= 1 and xx < Fraction(4, 27)
        bounds[(pv, qv, rv)] = e1 * Rbar
        ok = ok and e1 * Rbar < Fraction(1, 10 ** 7)
    checks.check("D2", ok, "T3-T4: at (4165,1,2), (2085,1,1), (8330,2,4), (6247,1,3) with t = 99/1000, 49/500, 99/1000, 99/1000 the rational triples are super-solutions at (t + epsilon_2/t^2, epsilon_1/t^3) (three exact inequalities each, entries >= 1, x < 4/27), and epsilon_1 R-bar < 10^-7 at each")
    # D3: the previous thresholds' factor and the distinctness arithmetic
    old = {(1, 2): 285718, (1, 1): 142861, (2, 4): 571436, (1, 3): 428576}
    new = {(1, 2): 4165, (1, 1): 2085, (2, 4): 8330, (1, 3): 6247}
    ok3 = all(Fraction(old[k], new[k]) >= 68 for k in old) and all(b < Fraction(1, 2) for b in bounds.values())
    checks.check("D3", ok3, "T4: the certified couplings are at least 68 times below block 25's on every line, and the bounds are below 1/2 (the distinctness of the six laws)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    v, t = sp.symbols("v t", positive=True)
    top = sp.Rational(4, 27)
    if mut("ceiling_wrong"):
        top = sp.Rational(5, 27)
    m1 = sp.maximum((v - 1) / v ** 3, v, sp.Interval(1, sp.oo))
    m2 = sp.maximum(t ** 2 * (sp.Rational(4, 27) - t), t, sp.Interval(0, sp.Rational(4, 27)))
    ok = sp.simplify(m1 - top) == 0 and sp.simplify(m2 - sp.Rational(256, 531441)) == 0
    # the tangency point and the maximiser
    ok = ok and sp.simplify(((v - 1) / v ** 3).subs(v, sp.Rational(3, 2)) - sp.Rational(4, 27)) == 0 and sp.simplify((t ** 2 * (sp.Rational(4, 27) - t)).subs(t, sp.Rational(8, 81)) - sp.Rational(256, 531441)) == 0
    checks.check("E1", ok, "T5: max_{v >= 1} (v - 1)/v^3 = 4/27 (at v = 3/2), scalar U maximum only; full-domain endpoint separately checked; max_t t^2 (4/27 - t) = 256/531441 (at t = 8/81)")
    denominator = sp.simplify(1-3*((v-1)/v**3)*v**2)
    endpoint_slope = 3*Fraction(4,27)*Fraction(3,2)**2
    endpoint_constant = Fraction(3,2)**2
    endpoint_ok = sp.simplify(denominator-(3-2*v)/v)==0 and endpoint_slope==1 and endpoint_constant==Fraction(9,4)
    if mut("ceiling_endpoint_wrong"):
        endpoint_ok = endpoint_ok and endpoint_slope < 1
    checks.check("E3", endpoint_ok, "Full recursion denominator (3-2v)/v; at the endpoint D=9/4+D, so bounded scalar U alone is insufficient; deferred route-bound diagnostic")
    d3 = deviations(4150, 1, 2)[2]
    d3b = deviations(4165, 1, 2)[2]
    checks.check("E2", d3 > Fraction(256, 531441) > d3b, f"T5: d_3(4150, 1, 2) = {d3} exceeds 256/531441 while d_3(4165, 1, 2) = {d3b} is below it: the deferred necessary comparison is bracketed by these points; no optimal integer is asserted")


# Honest resolution statements; these lines are not counted as scientific checks.
N5_LINES = (
    "per_element: finite exact closed-form and derivative identities, factorization and amplified-excuse increments are checked",
    "per_site: finite all-216 predecessor triples at five weight triples; no sitewise physical or infinite-time threshold is measured",
    "per_mode: exact small cones and original 1200 seeded random cones, with finite 66103 lifted-tree enumeration; no exhaustive larger-cone claim",
    "per_block: four exact rational super-solutions and algebraic endpoint diagnostics; conditional positive certificates only",
    "lattice_wide: checked and not executed — written finite-localization, tree-bound and compactness proofs under supplied hypotheses",
)

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
    family_e(checks)
    for line in N5_LINES:
        print(line)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    result = dict(checks=checks.results, passed=checks.passed, failed=checks.failed,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}, mutation=ACTIVE_MUTATION)
    suffix = "--"+ACTIVE_MUTATION if ACTIVE_MUTATION else ""
    output = ROOT/"logs/runner-cache"/(Path(__file__).stem+suffix+".json")
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("x") as stream:
        json.dump(result,stream,indent=2)
        stream.write("\n")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
