#!/usr/bin/env python3
"""Exact checks: the three-dimensional formation law's ordered phase — stability of the noisy level automaton with an explicit
noise threshold, and six invariant laws.

Scope.  T0: the closed forms of the rule's three-predecessor conditional, the monotonicity of the noise map in p, the noise map as
the exact maximum over the 216 triples with two entries a, the domination inequality.  T2: the increments of M_k, the fork size, the
excuse identity.  T4: the explanation-tree construction (clusters, cause graph, spanning lemma, refinement) executed exhaustively on
the depth-2 backward cone, on every depth-3 configuration with at most four noise sites, on random deeper cones (integer
randomness) and on line and triangle seeds, with the tree property, the marks, the spanning identity and edges <= 4(n - 1) checked.
T4 (refined): at most one arrow to a predecessor at each node, the marks read off the tree, forks = n - 1, arrows <= 3(n - 1).  T5: the
subtrees of G with at most four edges and at most one arrow to a predecessor per node, counted by (arrows, forks), their lifts to the
typed regular tree (pairwise distinct) and the exact coefficients of the generating-function recursion; the rational super-solution
certificate at (t, s) = (91/1000, 1000/107653).  T6-T7: the bound (391/100) epsilon at epsilon_0 = 7/10^6, the thresholds p_0, the
Cesaro identity on a finite chain, the distinctness arithmetic.  Exact arithmetic only (integers, Fractions and sympy); the runner
scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
from collections import deque
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_of_the_noisy_level_automaton_explicit_threshold_six_invariant_laws_bounded_theorem_note_2026-09-16"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "kernel_closed_form_wrong": "B",
    "monotonicity_wrong": "B",
    "noise_map_max_wrong": "B",
    "domination_inequality_wrong": "B",
    "increment_wrong": "C",
    "fork_size_wrong": "C",
    "edge_bound_claimed_tighter": "D",
    "spanning_identity_wrong": "D",
    "subtree_bound_wrong": "D",
    "certificate_wrong": "E",
    "threshold_p0_wrong": "E",
    "claim_transition_located_injected": "F",
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
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


# ============================================================================================ the automaton and the construction
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK_OFFSETS = [tuple(E3[a][i] - E3[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def level(z):
    return z[0] + z[1] + z[2]


def Mfun(k, z):
    return Fraction(z[k]) - Fraction(level(z), 3)


def preds(z):
    return [sub(z, E3[j]) for j in range(3)]


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
    eta = {}
    for z in sorted(sites, key=level):
        ps = [eta.get(p, 0) for p in preds(z)]
        maj = 1 if sum(ps) >= 2 else 0
        eta[z] = 1 if (maj or zeta.get(z, 0)) else 0
    return eta


class Explainer:
    def __init__(self, eta, zeta, spanning_offset=Fraction(0)):
        self.eta = eta
        self.zeta = zeta
        self.spanning_offset = spanning_offset
        self.ones = {z for z, v in eta.items() if v == 1}
        self.noise = {z for z in self.ones if zeta.get(z, 0) == 1 and sum(eta.get(p, 0) for p in preds(z)) < 2}
        self.exc = {}
        for z in self.ones:
            if z in self.noise:
                continue
            idx = [j for j in range(3) if eta.get(preds(z)[j], 0) == 1]
            assert len(idx) >= 2
            self.exc[z] = (idx[0], idx[1])
        self._cluster_cache = {}

    def excuse_k(self, v, k):
        i, j = self.exc[v]
        a = min(t for t in (i, j) if t != k)
        return preds(v)[a]

    def arrows_down(self, z):
        if z in self.noise or z not in self.ones:
            return []
        return [p for p in preds(z) if p in self.ones]

    def clusters_at(self, s):
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
        edges = {}
        processed = set()
        unproc = [(frozenset([root]), (root, root, root))]
        refinements = 0
        identity_ok = True
        if root in self.noise:
            return {root}, edges, {root}, 0, True

        def incident(pt):
            return any(pt in e for e in edges)

        while True:
            active = [(K, poles) for (K, poles) in unproc if not all(v in self.noise for v in poles)]
            if not active:
                break
            K, poles = active[0]
            unproc.remove((K, poles))
            assert all(v not in self.noise for v in poles)
            s = level(next(iter(K)))
            u = [self.excuse_k(poles[j], j) for j in range(3)]
            cl = self.clusters_at(s - 1)
            V_K = []
            for z in K:
                for p in self.arrows_down(z):
                    c = cl[p]
                    if c not in V_K:
                        V_K.append(c)
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
            n = len(fam)
            adj = {i: set() for i in range(n)}
            for i, j in combinations(range(n), 2):
                if fam[i][0] != fam[j][0] and (fam[i][1] & fam[j][1]):
                    adj[i].add(j); adj[j].add(i)
            term = []
            for j in range(3):
                ti = [i for i in range(n) if fam[i][0] == "cluster" and u[j] in fam[i][1]]
                assert len(ti) == 1
                term.append(ti[0])

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

            def inter_point(i, j):
                common = fam[i][1] & fam[j][1]
                assert len(common) == 1
                return next(iter(common))

            reduced = {}
            for i in tree_nodes:
                pts = set()
                for j in range(3):
                    if term[j] == i:
                        pts.add(u[j])
                for nb in tnbr[i]:
                    pts.add(inter_point(i, nb))
                reduced[i] = pts

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
                            prev[b] = a; dq.append(b)
                raise AssertionError

            pole_of = {}
            for i in tree_nodes:
                pl = []
                for j in range(3):
                    if u[j] in reduced[i]:
                        pl.append(u[j])
                    else:
                        pl.append(inter_point(i, next_toward(i, term[j])))
                pole_of[i] = tuple(pl)
            total = sum(Mfun(j, pole_of[i][j]) for i in tree_nodes for j in range(3))
            expected = sum(Mfun(j, u[j]) for j in range(3)) + self.spanning_offset
            identity_ok = identity_ok and (total == expected) and (expected - self.spanning_offset == sum(Mfun(j, poles[j]) for j in range(3)) + 1)
            for i in tree_nodes:
                if fam[i][0] == "cluster":
                    unproc.append((fam[i][1], pole_of[i]))
                else:
                    a, b = tuple(fam[i][1])
                    edges[frozenset([a, b])] = "fork"
            kept = {}
            for j in range(3):
                v = poles[j]
                if incident(v) and v not in kept:
                    kept[v] = j
            if not kept:
                kept[poles[0]] = 0
            for v, j in kept.items():
                edges[frozenset([v, u[j]])] = "arrow"
                processed.add(v)
            refinements += 1
        noise_nodes = set()
        for (K, poles) in unproc:
            assert len(K) == 1 and all(v in self.noise for v in poles)
            noise_nodes |= set(K)
        nodes = set(processed) | noise_nodes
        for e in edges:
            nodes |= set(e)
        return nodes, edges, noise_nodes, refinements, identity_ok


def check_tree(nodes, edges, root, ex):
    ok = root in nodes and len(edges) == len(nodes) - 1
    nb = {v: set() for v in nodes}
    for e, kind in edges.items():
        a, b = tuple(e)
        nb[a].add(b); nb[b].add(a)
        ok = ok and ((b in preds(a) or a in preds(b)) if kind == "arrow" else is_fork(a, b))
    seen = {root}; dq = deque([root])
    while dq:
        a = dq.popleft()
        for b in nb[a]:
            if b not in seen:
                seen.add(b); dq.append(b)
    return ok and seen == nodes and all(z in ex.ones for z in nodes)


def test_config(x, sites, zeta, stats, ratio_bound):
    eta = run_automaton(sites, zeta)
    if eta[x] != 1:
        return True
    ex = Explainer(eta, zeta)
    nodes, edges, noise_nodes, refs, ident = ex.explain(x)
    n = len(noise_nodes)
    ok = n >= 1 and check_tree(nodes, edges, x, ex) and noise_nodes <= ex.noise and all(zeta.get(z, 0) == 1 for z in noise_nodes)
    ok = ok and ident and len(edges) <= ratio_bound * (n - 1)
    downs = {v: 0 for v in nodes}
    arrows = forks = 0
    for e, kind in edges.items():
        if kind == "arrow":
            p, c = tuple(e)
            downs[p if c in preds(p) else c] += 1
            arrows += 1
        else:
            forks += 1
    ok = ok and max(downs.values()) <= 1 and {v for v in nodes if downs[v] == 0} == noise_nodes and forks == n - 1 and arrows <= 3 * (n - 1)
    stats["cases"] += 1
    stats["max_ratio"] = max(stats["max_ratio"], Fraction(len(edges), max(n - 1, 1)))
    return ok


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, b01 = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3,
                 "the three declared inputs exist (this note, the axiom memo, block 01's note on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the four axiom sentences used are present verbatim in the axiom memo")
    f1 = normalize_text(b01)
    checks.check("A3", BLOCK01_CLAIM_ID in f1 and BLOCK01_FRAGMENT in f1, "block 01's claim id and its section on the static law of a product rule are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
MENU = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi_of(v, w, p, q, r):
    if v == w:
        return p
    if tuple(-c for c in v) == w:
        return q
    return r


def conditional(a, triple, p, q, r):
    num = 1
    for w in triple:
        num = num * phi_of(a, w, p, q, r)
    den = 0
    for v in MENU:
        t = 1
        for w in triple:
            t = t * phi_of(v, w, p, q, r)
        den += t
    return Fraction(num, den)


def deviations(p, q, r):
    d1 = 1 - Fraction(p ** 3, p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - Fraction(p ** 2 * q, p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - Fraction(p ** 2 * r, r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def family_b(checks: Checks) -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    a = (1, 0, 0); b = (0, 1, 0); ma = (-1, 0, 0)

    def K(v, triple):
        num = 1
        for w in triple:
            num = num * phi_of(v, w, p, q, r)
        den = sum(sp.prod([phi_of(vv, w, p, q, r) for w in triple]) for vv in MENU)
        return num / den

    f1 = sp.simplify(K(a, (a, a, a)) - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)) == 0
    target_b = p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    if mut("kernel_closed_form_wrong"):
        target_b = p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 4 * r ** 3)
    f2 = sp.simplify(K(a, (a, a, b)) - target_b) == 0
    f3 = sp.simplify(K(a, (a, a, ma)) - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)) == 0
    checks.check("B1", f1 and f2 and f3, "T0(a): the three-predecessor conditional of block 01's rule at the unanimous, orthogonal 2:1 and antipodal 2:1 patterns has the stated closed forms, symbolically")
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = (p * q ** 2 + 4 * r ** 3) / (q * p ** 2 + q ** 2 * p + 4 * r ** 3)
    C = r * q ** 2 + r ** 2 * q + 2 * r ** 3
    d3 = (r ** 2 * p + C) / (r * p ** 2 + r ** 2 * p + C)
    n1 = sp.factor(sp.simplify(sp.diff(d1, p) * (p ** 3 + q ** 3 + 4 * r ** 3) ** 2))
    n2 = sp.expand(sp.simplify(sp.diff(d2, p) * (q * p ** 2 + q ** 2 * p + 4 * r ** 3) ** 2))
    n3 = sp.expand(sp.simplify(sp.diff(d3, p) * (r * p ** 2 + r ** 2 * p + C) ** 2))
    t2 = -q ** 3 * p ** 2 - 8 * q * r ** 3 * p
    if mut("monotonicity_wrong"):
        t2 = -q ** 3 * p ** 2 + 8 * q * r ** 3 * p
    mono = sp.simplify(n1 + 3 * p ** 2 * (q ** 3 + 4 * r ** 3)) == 0 and sp.simplify(n2 - t2) == 0 and sp.simplify(n3 - (-r ** 3 * p ** 2 - 2 * r * C * p)) == 0
    checks.check("B2", mono, "T0(b): the numerators of the three deviations' derivatives in p are -3p^2(q^3 + 4r^3), -q^3 p^2 - 8 q r^3 p and -r^3 p^2 - 2 r C p, all negative: epsilon is strictly decreasing in p")
    ok3 = True
    for (pp, qq, rr) in ((3, 1, 2), (10, 1, 2), (30, 1, 2)):
        worst = Fraction(0)
        for triple in product(MENU, repeat=3):
            if sum(1 for w in triple if w == a) >= 2:
                worst = max(worst, 1 - conditional(a, triple, pp, qq, rr))
        formula = max(deviations(pp, qq, rr))
        if mut("noise_map_max_wrong"):
            formula = max(deviations(pp, qq, rr)[:2])
        ok3 = ok3 and worst == formula
    checks.check("B3", ok3, "T0(a): epsilon(p, q, r) as the exact maximum over all triples with at least two entries a equals max(d1, d2, d3) at (3,1,2), (10,1,2) and (30,1,2) (the antipodal deviation attains it at p = 3, 10, the orthogonal one at p = 30)")
    ok4 = True
    for (pp, qq, rr) in ((3, 1, 2), (10, 1, 2), (5, 2, 4)):
        eps = max(deviations(pp, qq, rr))
        bound = eps
        if mut("domination_inequality_wrong"):
            bound = eps / 2
        for triple in product(MENU, repeat=3):
            if sum(1 for w in triple if w == a) >= 2:
                ok4 = ok4 and (1 - conditional(a, triple, pp, qq, rr)) <= bound
    checks.check("B4", ok4, "T0(c): at every triple with at least two entries a, 1 - K(a | triple) <= epsilon(p, q, r), at three couplings (the coupling's per-site inequality)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    x = (2, -1, 3)
    ok = True
    for k in range(3):
        for j in range(3):
            inc = Mfun(k, sub(x, E3[j])) - Mfun(k, x)
            target = Fraction(1, 3) - (1 if j == k else 0)
            if mut("increment_wrong"):
                target = Fraction(1, 3) - (2 if j == k else 0)
            ok = ok and inc == target
    ok = ok and all(sum(Mfun(k, z) for k in range(3)) == 0 for z in cone((0, 0, 0), 3))
    pairs_ok = all(any(j != k for j in pair) for pair in combinations(range(3), 2) for k in range(3))
    checks.check("C1", ok and pairs_ok, "T2(a): M_k(x - e_j) - M_k(x) = 1/3 - delta_jk; sum_k M_k = 0 on the depth-3 cone; every pair of indices contains one differing from each k")
    w = (0, 0, 0)
    ok2 = True
    for off in FORK_OFFSETS:
        w2 = add(w, off)
        size = sum(max(Mfun(k, w), Mfun(k, w2)) for k in range(3))
        target = Fraction(1)
        if mut("fork_size_wrong"):
            target = Fraction(2)
        ok2 = ok2 and size == target
        for poles in product((w, w2), repeat=3):
            ok2 = ok2 and sum(Mfun(k, poles[k]) for k in range(3)) <= 1
    checks.check("C2", ok2, "T2(b): every fork pair has Size = 1 and every assignment of its two points as poles has Span <= 1")


# ------------------------------------------------------------------------------------------- the typed tree (T5)
TYPES = [("down", j) for j in range(3)] + [("up", j) for j in range(3)] + [("fork", (i, j)) for i in range(3) for j in range(3) if i != j]


def step(v, ty):
    kind, d = ty
    if kind == "down":
        return sub(v, E3[d])
    if kind == "up":
        return add(v, E3[d])
    return add(sub(v, E3[d[1]]), E3[d[0]])


def reverse(ty):
    kind, d = ty
    if kind == "down":
        return ("up", d)
    if kind == "up":
        return ("down", d)
    return ("fork", (d[1], d[0]))


def gf_coefficients(A, FM, up_slots=3):
    """Exact coefficients [t^a s^f] of the recursion D = (1+tU)^2 (1+3tD)(1+sF)^6, U = (1+tU)^{up_slots} (1+sF)^6,
    F = (1+tU)^3 (1+3tD)(1+sF)^5, R = (1+tU)^3 (1+3tD)(1+sF)^6, truncated at a <= A, f <= FM (heights up to A + FM + 1)."""

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

    D = U = F = {(0, 0): 1}
    for _ in range(A + FM + 1):
        xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(F, 1, 0, 1)
        D, U, F = pmul(pmul(ppow(xU, 2), xD3), ppow(yF, 6)), pmul(ppow(xU, up_slots), ppow(yF, 6)), pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 5))
    xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(F, 1, 0, 1)
    return pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 6))


def enumerate_typed_tree(kmax):
    """Admissible rooted subtrees of the typed tree with at most kmax edges, counted by (arrows, forks); vertices are type words."""
    trees = {frozenset([()])}
    counts = {}
    for _ in range(kmax):
        nxt = set()
        for T in trees:
            downs = {w: 0 for w in T}
            for w in T:
                if w and w[-1][0] == "down":
                    downs[w[:-1]] += 1
                if w and w[-1][0] == "up":
                    downs[w] += 1
            for w in T:
                last = w[-1] if w else None
                for ty in TYPES:
                    if (last is not None and ty == reverse(last)) or (ty[0] == "down" and downs[w] >= 1):
                        continue
                    nw = w + (ty,)
                    if nw not in T:
                        nxt.add(T | {nw})
        trees = nxt
        for T in trees:
            a = sum(1 for w in T if w and w[-1][0] != "fork")
            counts[(a, len(T) - 1 - a)] = counts.get((a, len(T) - 1 - a), 0) + 1
    return counts


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    x = (0, 0, 0)
    ratio_bound = 4
    if mut("edge_bound_claimed_tighter"):
        ratio_bound = 2
    stats = {"cases": 0, "max_ratio": Fraction(0)}
    sites2 = cone(x, 2)
    ok1 = True
    for bits in product((0, 1), repeat=len(sites2)):
        zeta = {z: b for z, b in zip(sites2, bits) if b}
        ok1 = ok1 and test_config(x, sites2, zeta, stats, ratio_bound)
    checks.check("D1", ok1 and stats["cases"] == 932, f"T4: on all 1024 noise configurations of the depth-2 backward cone ({stats['cases']} with a one at x) the refinement builds a tree of arrows and forks through 1-sites rooted at x, its marked nodes are noise sites, the spanning identity holds at every refinement, edges <= 4(n-1) (largest ratio {stats['max_ratio']}), every node has at most one arrow to a predecessor, the nodes without one are exactly the noise nodes, forks = n-1 and arrows <= 3(n-1)")
    stats3 = {"cases": 0, "max_ratio": Fraction(0)}
    sites3 = cone(x, 3)
    ok2 = True
    for k in range(1, 5):
        for combo in combinations(sites3, k):
            ok2 = ok2 and test_config(x, sites3, {z: 1 for z in combo}, stats3, ratio_bound)
    random.seed(25)
    stats4 = {"cases": 0, "max_ratio": Fraction(0)}
    for trial in range(1200):
        depth = 3 + trial % 5
        dens = (15, 30, 50)[trial % 3]
        sites = cone(x, depth)
        zeta = {z: 1 for z in sites if random.randrange(100) < dens}
        ok2 = ok2 and test_config(x, sites, zeta, stats4, ratio_bound)
    checks.check("D2", ok2 and stats3["cases"] == 2321 and stats4["cases"] > 400, f"T4: every depth-3 configuration with at most four noise sites ({stats3['cases']} explained) and 1200 random cones of depth 3-7 ({stats4['cases']} explained) pass the same checks (largest ratios {stats3['max_ratio']}, {stats4['max_ratio']})")
    stats5 = {"cases": 0, "max_ratio": Fraction(0)}
    ok3 = True
    for n in range(1, 9):
        zeta = {sub(x, (a, n - a, 0)): 1 for a in range(n + 1)}
        ok3 = ok3 and test_config(x, cone(x, n), zeta, stats5, ratio_bound)
    for n in range(1, 7):
        zeta = {z: 1 for z in cone(x, n) if level(z) == -n}
        ok3 = ok3 and test_config(x, cone(x, n), zeta, stats5, ratio_bound)
    # the spanning identity itself, with a deliberately wrong expectation under mutation
    eta = run_automaton(cone(x, 4), {z: 1 for z in cone(x, 4) if level(z) == -4})
    ex = Explainer(eta, {z: 1 for z in cone(x, 4) if level(z) == -4}, spanning_offset=Fraction(1) if mut("spanning_identity_wrong") else Fraction(0))
    _, _, _, _, ident = ex.explain(x)
    checks.check("D3", ok3 and stats5["cases"] == 14 and ident, f"T4: line seeds (n + 1 noise sites n levels down, n <= 8) and triangle seeds (n <= 6) are explained with the bound (largest ratio {stats5['max_ratio']}); the spanning identity sum_X Span(X) = sum_k M_k(u_k) holds at every refinement of the depth-4 triangle seed")

    # T5: the subtrees of G containing the origin with at most one arrow to a predecessor at each node, by (arrows, forks); their lifts
    trees = {frozenset()}
    counts = {(0, 0): 1}
    lifts = set()
    inj = True
    for _ in range(4):
        nxt = set()
        for T in trees:
            nodes = {x} | {c for (_p, c, _ty) in T}
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
            parent = {c: (p, ty) for (p, c, ty) in T}
            words = set()
            for v in list(parent) + [x]:
                w = []
                while v in parent:
                    p, ty = parent[v]
                    w.append(ty)
                    v = p
                words.add(tuple(reversed(w)))
            key = frozenset(words)
            inj = inj and key not in lifts
            lifts.add(key)
    total = sum(counts.values())
    coeff = gf_coefficients(5, 5, up_slots=2 if mut("subtree_bound_wrong") else 3)
    within = all(c <= coeff.get(k, 0) for k, c in counts.items())
    equal_small = all(c == coeff.get(k, 0) for k, c in counts.items() if sum(k) <= 2)
    strict_four = all(c < coeff.get(k, 0) for k, c in counts.items() if sum(k) == 4)
    direct = enumerate_typed_tree(3)
    agree = all(direct.get(k, 0) == coeff.get(k, 0) for k in set(direct) | {k for k in coeff if 1 <= sum(k) <= 3})
    checks.check("D4", total == 66103 and inj and within and equal_small and strict_four and agree, f"T5: the subtrees of G containing the origin with at most four edges and at most one arrow to a predecessor at each node number {total}; their lifts to the typed tree are pairwise distinct; by (arrows, forks) each count is at most the recursion's coefficient (equal for at most two edges, below it for every pair with four edges); the coefficients with at most three edges agree with a direct enumeration of admissible subtrees of the typed tree")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    t = Fraction(91, 1000)
    s = Fraction(1000, 107653)
    if mut("certificate_wrong"):
        s = Fraction(1, 100)
    Db, Ub, Fb = Fraction(3290957526219, 10 ** 12), Fraction(514547476033, 25 * 10 ** 10), Fraction(943741493637, 25 * 10 ** 10)
    rD = (1 + t * Ub) ** 2 * (1 + 3 * t * Db) * (1 + s * Fb) ** 6
    rU = (1 + t * Ub) ** 3 * (1 + s * Fb) ** 6
    rF = (1 + t * Ub) ** 3 * (1 + 3 * t * Db) * (1 + s * Fb) ** 5
    Rbar = (1 + t * Ub) ** 3 * (1 + 3 * t * Db) * (1 + s * Fb) ** 6
    eps0 = t ** 3 * s
    cert = Db >= rD and Ub >= rU and Fb >= rF and min(Db, Ub, Fb) >= 1 and t <= 1
    partial = sum((c * t ** a * s ** f for (a, f), c in gf_coefficients(5, 5).items()), Fraction(0))
    checks.check("E1", cert and Rbar < Fraction(391, 100) and eps0 == Fraction(7, 10 ** 6) and eps0 * Rbar <= Fraction(3, 10 ** 5) and Fraction(391, 100) * eps0 == Fraction(2737, 10 ** 8) and partial <= Rbar, "T5-T6: at (t, s) = (91/1000, 1000/107653) the rational triple (D-bar, U-bar, F-bar) is a super-solution of the recursion (three exact inequalities; entries >= 1; t <= 1), R-bar = (1 + t U-bar)^3 (1 + 3 t D-bar)(1 + s F-bar)^6 < 391/100, t^3 s = 7/10^6 = epsilon_0, epsilon_0 R-bar <= 3/10^5 ((391/100) epsilon_0 = 2737/10^8), and the recursion's partial sum over at most five edges stays below R-bar")
    eps0 = Fraction(7, 10 ** 6)

    def least_p(q, r):
        lo, hi = 1, 10 ** 12
        while lo < hi:
            mid = (lo + hi) // 2
            if max(deviations(mid, q, r)) <= eps0:
                hi = mid
            else:
                lo = mid + 1
        return lo

    p0 = {(1, 2): 285718, (1, 1): 142861, (2, 4): 571436, (1, 3): 428576}
    if mut("threshold_p0_wrong"):
        p0[(1, 2)] = 285717
    ok2 = all(least_p(q, r) == v and max(deviations(v, q, r)) <= eps0 < max(deviations(v - 1, q, r)) for (q, r), v in p0.items())
    checks.check("E2", ok2, "T7(b): the least integers p with epsilon(p, q, r) <= epsilon_0 = 7/10^6 are 285718 at (1,2), 142861 at (1,1), 571436 at (2,4), 428576 at (1,3), each with epsilon(p_0 - 1) > epsilon_0")
    delta = Fraction(3, 10 ** 5)
    Pm = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4)], [sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3)], [sp.Rational(1, 6), sp.Rational(1, 6), sp.Rational(2, 3)]])
    lam = sp.Matrix([[1, 0, 0]])
    f = sp.Matrix([1, -1, sp.Rational(1, 2)])
    T = 12
    laws = [lam * Pm ** t for t in range(1, T + 2)]
    cesaro = sum(laws[:T], sp.zeros(1, 3)) / T
    lhs = (cesaro * Pm * f)[0] - (cesaro * f)[0]
    rhs = ((laws[T] - laws[0]) * f)[0] / T
    checks.check("E3", sp.simplify(lhs - rhs) == 0 and abs(rhs) <= sp.Rational(2, T) and (1 - delta) > delta, "T7(c): on a three-state chain the Cesaro average satisfies mu_T(Pf) - mu_T(f) = (lambda_{T+1}(f) - lambda_1(f))/T, bounded by 2||f||/T; and 1 - delta > delta for the distinctness")


# ============================================================================================ family F
FENCES = (
    "This note proves, for the noisy majority automaton of the three-dimensional formation law in level time, that the density of ones from the all-zero level is at most `(391/100)ε` for `ε ≤ 7/10⁶`, and hence that the formation law of the six-axis product rule started from a constant plane keeps every later site within `3/10⁵` of that value whenever `ε(p, q, r) ≤ 7/10⁶`, with at least six distinct invariant laws; it does not locate the true threshold, does not treat couplings between block 08's uniqueness region and this one, does not treat other menus or orders, does not select a reading, rule or coupling as physical, and adopts no clause.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at",
)
CLAIM_INJECTIONS = {"claim_transition_located_injected": "Hence the ordered phase begins at p = p_0."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Gács", "Swart", "Szabó", "Toninelli", "Bramson", "Gray", "Krylov", "Bogolyubov", "Choquet", "Peierls", "Dobrushin", "Mermin", "Wagner")  # authors; Feller, Bernoulli, Markov name standard objects
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F3", not bad and len(scan) > 150, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem T4"):
            body = body + " (Toom's construction)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record; Feller, Bernoulli and Markov name standard objects ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the kernel's closed forms; the increments 1/3 - delta_jk; the fork size; the derivatives of the deviations",
    "per_site: executed — the coupling inequality at all 216 triples with two entries a; the exact least couplings p_0 at four weight pairs",
    "per_mode: executed — the refinement on all 1024 depth-2 and all 2321 explained depth-3 configurations with at most four noise sites, on 1200 random cones and on structured seeds; the 66103 trees with at most four edges against the recursion's coefficients",
    "per_block: executed — the super-solution certificate at (91/1000, 1000/107653); the bound (391/100) epsilon <= 3/10^5 at epsilon_0 = 7/10^6; the Cesaro identity on a finite chain",
    "lattice_wide: T4-T7 proved for every epsilon <= 7/10^6 and every coupling with epsilon(p, q, r) <= epsilon_0; the true threshold not claimed",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


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
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the three-dimensional formation law's ordered phase — the noisy level automaton's explanation trees executed exhaustively on small cones, the subtree count, the series bound, the coupling thresholds, the six invariant laws; exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
