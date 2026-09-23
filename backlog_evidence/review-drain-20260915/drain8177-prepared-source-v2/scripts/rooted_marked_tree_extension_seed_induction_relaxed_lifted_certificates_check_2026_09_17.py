#!/usr/bin/env python3
"""Finite rooted extension/seed instances, exact predecessor profiles and
relaxed lifted-tree polynomial certificates. The open induction residual
suffices for a finite unit budget; no converse or physical improvement is
proved. The count deliberately relaxes entering processed-child occupancy
and geometric collisions. Original finite fixtures and arithmetic retained.
Stdout only; historical solvers and searches are not executed.
"""

from __future__ import annotations

import hashlib
import random
import re
import sys
from fractions import Fraction
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ROOTED_MARKED_TREE_EXTENSION_SEED_INDUCTION_AND_RELAXED_LIFTED_TREE_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/SIX_AXIS_TWO_LEVEL_DOMINATION_EXTENDED_EXPLANATION_TREE_AND_FOUR_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md",
)
INPUT_SHA256 = {'docs/ROOTED_MARKED_TREE_EXTENSION_SEED_INDUCTION_AND_RELAXED_LIFTED_TREE_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-17.md': '24be34b472e47cafd59a15dd5125bfad54a1270fb4712002d9bf29d145029559', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md': 'cc7e8423b3bb35f7f2cf4699d498556b98fbc55229eb8a5d9f52e1ba00a63f97', 'docs/SIX_AXIS_TWO_LEVEL_DOMINATION_EXTENDED_EXPLANATION_TREE_AND_FOUR_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-16.md': '5642877329c141c39394936173c35c82c5cd18bb8f9a408c17fad0497cef647e'}
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "rooted_marked_tree_extension_seed_induction_and_relaxed_lifted_tree_certificates_bounded_theorem_note_2026-09-17"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "extension_lemma_wrong": "B",
    "seed_lemma_wrong": "B",
    "tightness_wrong": "C",
    "predecessor_profile_wrong": "C",
    "certificate_wrong": "D",
    "upfactor_wrong": "D",
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


# ============================================================================================ level time, the automaton, the family
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK_OFFSETS = [tuple(E3[a][i] - E3[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]


def level(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)]


def is_fork(u, v):
    return tuple(v[i] - u[i] for i in range(3)) in FORK_OFFSETS


def run_automaton(sites, zeta):
    """the one-sided two-level majority automaton from its noise marks: 1 if at least two 1-predecessors, else 1 iff marked."""
    eta = {}
    for z in sorted(sites, key=level):
        ps = [eta.get(p, 0) for p in preds(z)]
        eta[z] = 1 if (sum(ps) >= 2 or zeta.get(z, 0)) else 0
    return eta


def kinds(eta):
    ones = {z for z, v in eta.items() if v == 1}
    npred = {z: [p for p in preds(z) if p in ones] for z in ones}
    kind = {z: ("seed" if len(npred[z]) == 0 else "amp" if len(npred[z]) == 1 else "proc") for z in ones}
    return ones, npred, kind


def component(eta, root):
    """the component of the root in G restricted to 1-sites (arrows to 1-predecessors and from 1-successors, forks to 1-siblings)."""
    ones, npred, kind = kinds(eta)
    seen = {root}
    st = [root]
    while st:
        z = st.pop()
        nb = list(npred[z]) + [s for s in ones if z in preds(s)] + [tuple(z[i] + o[i] for i in range(3)) for o in FORK_OFFSETS]
        for w in nb:
            if w in ones and w not in seen:
                seen.add(w)
                st.append(w)
    return seen


def cost_of(kind_z, c):
    return Fraction(1) if kind_z == "proc" else -Fraction(c) if kind_z == "amp" else Fraction(0)


def single_seed_min(eta, root, c):
    """exact minimum of E - 3(|S| - 1) - c|A| over the family when the component of the root holds one seed; returns (value, seeds, node set)."""
    comp = component(eta, root)
    ones, npred, kind = kinds(eta)
    seeds = [z for z in comp if kind[z] == "seed"]
    if len(seeds) != 1:
        return None, seeds, None
    s = seeds[0]
    at = {}
    for z in comp:
        at.setdefault(level(z), []).append(z)
    Lmax, Ls, lr = max(at), level(s), level(root)
    nodes = sorted(at.get(Lmax, []))
    states = {}
    for mask in range(1 << len(nodes)):
        X = frozenset(nodes[i] for i in range(len(nodes)) if mask >> i & 1)
        if Lmax == lr and root not in X:
            continue
        states[X] = (sum(cost_of(kind[z], c) for z in X), None)
    hist = []
    for l in range(Lmax, Ls, -1):
        below = sorted(at.get(l - 1, []))
        nxt = {}
        for X, (val, bp) in states.items():
            need = [z for z in X if kind[z] != "seed"]
            for mask in range(1 << len(below)):
                Y = frozenset(below[i] for i in range(len(below)) if mask >> i & 1)
                if l - 1 == lr and root not in Y:
                    continue
                if any(not any(p in Y for p in npred[z]) for z in need):
                    continue
                v2 = val + sum(cost_of(kind[z], c) for z in Y)
                if Y not in nxt or v2 < nxt[Y][0]:
                    nxt[Y] = (v2, X)
        hist.append(states)
        states = nxt
    key = frozenset([s])
    if key not in states:
        return None, seeds, None
    best, bp = states[key]
    tree = [key]
    X = bp
    i = len(hist) - 1
    while X is not None and i >= 0:
        tree.append(X)
        X = hist[i][X][1]
        i -= 1
    return best, seeds, set().union(*tree)


def verify_tree(eta, root, nodes, arrows, forks):
    """a marked tree of the family: subtree of G through 1-sites containing the root; every non-seed node exactly one downward arrow
    to a 1-predecessor (an amplified node to its single one); forks between siblings; connected with |edges| = |nodes| - 1; F = |S| - 1."""
    ones, npred, kind = kinds(eta)
    ns = set(nodes)
    if root not in ns or not ns <= ones:
        return False
    adj = {z: set() for z in ns}
    down = {z: 0 for z in ns}
    for (z, u) in arrows:
        if z not in ns or u not in ns or u not in npred[z]:
            return False
        if kind[z] == "amp" and u != npred[z][0]:
            return False
        down[z] += 1
        adj[z].add(u)
        adj[u].add(z)
    for (u, v) in forks:
        if u not in ns or v not in ns or not is_fork(u, v):
            return False
        adj[u].add(v)
        adj[v].add(u)
    if any((kind[z] == "seed") != (down[z] == 0) or down[z] > 1 for z in ns):
        return False
    if len(arrows) + len(forks) != len(ns) - 1:
        return False
    seen = {root}
    st = [root]
    while st:
        a = st.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                st.append(b)
    S = sum(1 for z in ns if kind[z] == "seed")
    return seen == ns and len(forks) == S - 1


def tree_counts(eta, nodes):
    ones, npred, kind = kinds(eta)
    E = sum(1 for z in nodes if kind[z] == "proc")
    A = sum(1 for z in nodes if kind[z] == "amp")
    S = sum(1 for z in nodes if kind[z] == "seed")
    return E, A, S


def brute_min(eta, root, c, with_forks=True):
    """the full family enumerated on a tiny configuration: node sets, one arrow per non-seed node, forks joining the arborescences."""
    ones, npred, kind = kinds(eta)
    ones = sorted(ones)
    others = [z for z in ones if z != root]
    best = None
    for r in range(len(others) + 1):
        for sub in combinations(others, r):
            N = set(sub) | {root}
            nonseed = [z for z in N if kind[z] != "seed"]
            choices = [[u for u in npred[z] if u in N] for z in nonseed]
            if any(len(ch) == 0 for ch in choices):
                continue
            S = sum(1 for z in N if kind[z] == "seed")
            val = sum(cost_of(kind[z], c) for z in N) - 3 * (S - 1)
            if best is not None and val >= best:
                continue
            pairs = [(u, v) for u, v in combinations(sorted(N), 2) if is_fork(u, v)] if with_forks else []
            for arrows in product(*choices):
                parent = {z: z for z in N}

                def find(a):
                    while parent[a] != a:
                        a = parent[a]
                    return a

                for z, u in zip(nonseed, arrows):
                    parent[find(z)] = find(u)
                comps = {find(z) for z in N}
                qadj = {cc: set() for cc in comps}
                for (u, v) in pairs:
                    a, b = find(u), find(v)
                    if a != b:
                        qadj[a].add(b)
                        qadj[b].add(a)
                start = next(iter(comps))
                seen = {start}
                st = [start]
                while st:
                    a = st.pop()
                    for b in qadj[a]:
                        if b not in seen:
                            seen.add(b)
                            st.append(b)
                if seen == comps:
                    best = val
                    break
    return best


def cone(x, depth):
    pts = {x}
    frontier = {x}
    for _ in range(depth):
        nxt = set()
        for z in frontier:
            for j in range(3):
                nxt.add(tuple(z[i] - E3[j][i] for i in range(3)))
        pts |= nxt
        frontier = nxt
    return sorted(pts, key=level)


# ============================================================================================ data: the realizations
# Z_A: window 4x4x7, root (3,3,3); Z_B: window 5x5x8, root (4,4,4) — found by a hill-climb on the family's constant (controls)
Z_A = ((3, 3, 3), (4, 4, 7), [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 2), (1, 0, 5), (1, 2, 0), (1, 2, 5), (1, 3, 1), (2, 0, 0), (2, 1, 3), (2, 2, 3), (2, 3, 3), (3, 0, 1), (3, 0, 2), (3, 1, 0), (3, 1, 3), (3, 3, 5), (3, 3, 6)])
Z_B = ((4, 4, 4), (5, 5, 8), [(0, 0, 0), (0, 0, 1), (0, 0, 7), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 7), (0, 2, 7), (0, 4, 4), (1, 0, 0), (1, 0, 2), (1, 1, 2), (1, 2, 0), (1, 2, 2), (1, 3, 1), (1, 3, 7), (2, 0, 0), (2, 2, 0), (2, 2, 2), (2, 2, 3), (2, 2, 6), (2, 3, 3), (2, 3, 4), (2, 4, 2), (2, 4, 6), (3, 0, 1), (3, 0, 2), (3, 1, 2), (3, 2, 1), (3, 2, 7), (4, 0, 2), (4, 0, 6), (4, 1, 1), (4, 2, 1), (4, 4, 2), (4, 4, 4)])


# block 31's witnesses (PR #8175), restated as data
W1 = ((3, 3, 4), (4, 4, 7), [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 2), (1, 2, 0), (1, 3, 1), (2, 0, 0), (2, 2, 3), (2, 3, 4), (3, 0, 2)])
W2 = ((3, 3, 6), (4, 4, 7), [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 5), (0, 1, 0), (0, 1, 2), (0, 1, 3), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 5), (0, 2, 6), (0, 3, 1), (0, 3, 2), (0, 3, 5), (0, 3, 6), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 1), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 2), (2, 0, 3), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5), (2, 3, 1), (2, 3, 5), (2, 3, 6), (3, 0, 0), (3, 2, 2), (3, 3, 1), (3, 3, 2), (3, 3, 5)])
W3 = ((4, 4, 5), (5, 5, 9), [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 4), (0, 1, 0), (0, 1, 5), (0, 2, 3), (0, 2, 8), (0, 3, 1), (0, 3, 3), (0, 3, 4), (0, 4, 3), (0, 4, 4), (0, 4, 5), (0, 4, 6), (0, 4, 7), (1, 0, 0), (1, 0, 1), (1, 0, 4), (1, 1, 0), (1, 1, 1), (1, 1, 5), (1, 1, 7), (1, 2, 8), (1, 3, 8), (2, 0, 0), (2, 1, 1), (2, 1, 5), (2, 1, 6), (2, 1, 8), (2, 2, 0), (2, 2, 1), (2, 2, 6), (2, 2, 7), (2, 2, 8), (2, 3, 1), (2, 3, 2), (2, 3, 3), (2, 3, 8), (2, 4, 0), (2, 4, 2), (3, 0, 2), (3, 0, 8), (3, 1, 6), (3, 1, 7), (3, 2, 0), (3, 2, 2), (3, 2, 6), (3, 2, 7), (3, 2, 8), (3, 3, 1), (3, 3, 2), (3, 3, 4), (3, 3, 7), (3, 4, 3), (3, 4, 5), (4, 0, 2), (4, 0, 4), (4, 0, 5), (4, 0, 6), (4, 1, 0), (4, 1, 4), (4, 1, 6), (4, 1, 7), (4, 1, 8), (4, 2, 0), (4, 2, 2), (4, 2, 6), (4, 3, 0), (4, 3, 1), (4, 3, 6), (4, 4, 2), (4, 4, 6), (4, 4, 8)])

# ============================================================================================ rooted machinery
def single_seed_min_capped(eta, root, c, cap):
    """the single-seed program restricted to levels <= cap (rooted trees); returns (value, seeds)."""
    comp = component(eta, root)
    ones, npred, kind = kinds(eta)
    comp = {z for z in comp if level(z) <= cap}
    seeds = [z for z in comp if kind[z] == "seed"]
    if len(seeds) != 1:
        return None, seeds
    s = seeds[0]
    at = {}
    for z in comp:
        at.setdefault(level(z), []).append(z)
    Lmax, Ls, lr = max(at), level(s), level(root)
    nodes = sorted(at.get(Lmax, []))
    states = {}
    for mask in range(1 << len(nodes)):
        X = frozenset(nodes[i] for i in range(len(nodes)) if mask >> i & 1)
        if Lmax == lr and root not in X:
            continue
        states[X] = sum(cost_of(kind[z], c) for z in X)
    for l in range(Lmax, Ls, -1):
        below = sorted(at.get(l - 1, []))
        nxt = {}
        for X, val in states.items():
            need = [z for z in X if kind[z] != "seed"]
            for mask in range(1 << len(below)):
                Y = frozenset(below[i] for i in range(len(below)) if mask >> i & 1)
                if l - 1 == lr and root not in Y:
                    continue
                if any(not any(p in Y for p in npred[z]) for z in need):
                    continue
                v2 = val + sum(cost_of(kind[z], c) for z in Y)
                if Y not in nxt or v2 < nxt[Y]:
                    nxt[Y] = v2
        states = nxt
    key = frozenset([s])
    return (states.get(key), seeds)


def brute_rooted(eta, root, c, one_child=False):
    """exact minimum over ROOTED trees of the full family on a tiny realization (nodes at levels <= level(root); forks included);
    one_child: every node has at most one processed child (a node whose arrow points to it)."""
    ones, npred, kind = kinds(eta)
    ones = sorted(z for z in ones if level(z) <= level(root))
    others = [z for z in ones if z != root]
    best = None
    for r in range(len(others) + 1):
        for sub in combinations(others, r):
            N = set(sub) | {root}
            nonseed = [z for z in N if kind[z] != "seed"]
            choices = [[u for u in npred[z] if u in N] for z in nonseed]
            if any(len(ch) == 0 for ch in choices):
                continue
            S = sum(1 for z in N if kind[z] == "seed")
            val = sum(cost_of(kind[z], c) for z in N) - 3 * (S - 1)
            if best is not None and val >= best:
                continue
            pairs = [(u, v) for u, v in combinations(sorted(N), 2) if is_fork(u, v)]
            for arrows in product(*choices):
                if one_child:
                    pc = {}
                    for z, u in zip(nonseed, arrows):
                        if kind[z] == "proc":
                            pc[u] = pc.get(u, 0) + 1
                    if pc and max(pc.values()) > 1:
                        continue
                parent = {z: z for z in N}

                def find(a):
                    while parent[a] != a:
                        a = parent[a]
                    return a

                for z, u in zip(nonseed, arrows):
                    parent[find(z)] = find(u)
                comps = {find(z) for z in N}
                qadj = {cc: set() for cc in comps}
                for (u, v) in pairs:
                    a, b = find(u), find(v)
                    if a != b:
                        qadj[a].add(b)
                        qadj[b].add(a)
                start = next(iter(comps))
                seen = {start}
                st = [start]
                while st:
                    a = st.pop()
                    for b in qadj[a]:
                        if b not in seen:
                            seen.add(b)
                            st.append(b)
                if seen == comps:
                    best = val
                    break
    return best


def tiny_realizations(seed, count, shape=(3, 3, 5), lo=4, hi=10):
    random.seed(seed)
    sites = [(a, b, c) for a in range(shape[0]) for b in range(shape[1]) for c in range(shape[2])]
    out = []
    while len(out) < count:
        zeta = {z: 1 for z in random.sample(sites, random.randint(1, 6))}
        eta = run_automaton(sites, zeta)
        ones = [z for z, v in eta.items() if v == 1]
        if len(ones) < lo or len(ones) > hi:
            continue
        out.append(eta)
    return out


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts[:3]
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "the linked product-law parent carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT,p).is_file() and hashlib.sha256(Path(ROOT,p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all four proof/model source inputs match literal SHA-256 pins")


# ============================================================================================ family B — the rooted inequality's proven cases (T1)
def family_b(checks: Checks) -> None:
    etas = tiny_realizations(33, 140)
    ext_ok = seed_ok = ineq_ok = True
    n_ext = n_amp = n_seed1 = n_seed2 = n_sites = n_hard = 0
    ext_slack = 0 if not mut("extension_lemma_wrong") else 1
    seed_target = -1
    seed_target2 = -2 if not mut("seed_lemma_wrong") else -3
    for eta in etas:
        ones, npred, kind = kinds(eta)
        v = {z: brute_rooted(eta, z, Fraction(1)) for z in ones}
        for z in ones:
            n_sites += 1
            if kind[z] == "seed":
                ineq_ok = ineq_ok and v[z] <= 0      # {s} alone costs 0; sibling seeds joined by forks cost less
                continue
            for u in npred[z]:
                n_ext += 1
                ext_ok = ext_ok and v[z] <= 1 + v[u] - ext_slack
            if kind[z] == "amp":
                n_amp += 1
                ext_ok = ext_ok and v[z] <= -1 + v[npred[z][0]]
                ineq_ok = ineq_ok and v[z] <= -1
            else:
                ineq_ok = ineq_ok and v[z] <= 0
                seeds = [u for u in npred[z] if kind[u] == "seed"]
                if len(seeds) >= 2:
                    n_seed2 += 1
                    seed_ok = seed_ok and v[z] <= seed_target2
                elif len(seeds) == 1 and len(npred[z]) >= 2:
                    n_seed1 += 1
                    seed_ok = seed_ok and v[z] <= seed_target
                if not seeds and all(kind[u] == "proc" and v[u] == 0 for u in npred[z]):
                    n_hard += 1
    print(f"B-diagnostics: ext_ok={ext_ok} seed_ok={seed_ok} ineq_ok={ineq_ok} n_ext={n_ext} n_amp={n_amp} n_seed1={n_seed1} n_seed2={n_seed2} n_sites={n_sites} n_hard={n_hard}")
    checks.check("B1", ext_ok and n_ext >= 200 and n_amp >= 30, f"T1 (extension lemma, instances): on 140 tiny realizations, v(z) <= 1 + v(u) for every 1-predecessor u of every non-seed site ({n_ext} pairs) and v(z) <= -1 + v(u) at every amplified site ({n_amp}); exact rooted brute force")
    checks.check("B2", seed_ok and n_seed1 >= 12 and n_seed2 >= 10, f"T1 (seed lemma, instances): a processed site with one seed 1-predecessor and another 1-predecessor has v <= -1 ({n_seed1} cases), with two seed 1-predecessors v <= -2 ({n_seed2} cases)")
    checks.check("B3", ineq_ok and n_sites >= 600 and n_hard == 0, f"T1 (the rooted inequality, executed): v <= 0 at seeds, v <= -1 at amplified and v <= 0 at processed sites on all {n_sites} sites; processed sites whose 1-predecessors are all tight processed sites (the one case the lemmas leave open): {n_hard}")


# ============================================================================================ family C — the extremal realizations (T2)
def realization(w):
    root, (A_, B_, L_), marks = w
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    return run_automaton(sites, {z: 1 for z in marks}), root


def family_c(checks: Checks) -> None:
    ok = True
    report = []
    for name, Z in (("Z_A", Z_A), ("Z_B", Z_B)):
        eta, root = realization(Z)
        ones, npred, kind = kinds(eta)
        vr, seeds = single_seed_min_capped(eta, root, Fraction(1), level(root))
        target = Fraction(0) if not mut("tightness_wrong") else Fraction(-1)
        ok = ok and len(seeds) == 1 and vr == target
        pv = []
        for u in npred[root]:
            vu, _ = single_seed_min_capped(eta, u, Fraction(1), level(u))
            pv.append(vu)
        ok = ok and len(pv) == 3 and all(kind[u] == "proc" for u in npred[root]) and sorted(pv) == ([-1, -1, -1] if name == "Z_A" or mut("predecessor_profile_wrong") else [-1, -1, 0])
        pairs_min = max(min(a, b) for a, b in combinations(pv, 2))
        ok = ok and pairs_min <= -1
        report.append(f"{name}: v(root) = {vr}, the three processed 1-predecessors have v = {[str(x) for x in pv]}")
    checks.check("C1", ok, "T2: on Z_A and Z_B the root is tight (rooted value 0, exact single-seed program with a level cap) with exact processed-predecessor profiles ZA[-1,-1,-1], ZB[-1,-1,0]: neither tested root is a tight-sibling case; " + "; ".join(report))
    eta, root = realization(Z_B)
    ones, npred, kind = kinds(eta)
    z2 = (4, 4, 3)
    v2, _ = single_seed_min_capped(eta, z2, Fraction(1), level(z2))
    pv2 = [single_seed_min_capped(eta, u, Fraction(1), level(u))[0] for u in npred[z2]]
    checks.check("C2", v2 == 0 and sorted(pv2) == [-1, -1, -1], f"T2: Z_B's second tight site (4,4,3) has rooted value {v2} with 1-predecessors at {[str(x) for x in pv2]}; a tight site may be a predecessor of a tight site, in these tested profiles not all predecessors are tight; no universal absence asserted")


# ============================================================================================ family D — the one-processed-child count (T3)
def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def upf(n, xP, xA, U, restricted):
    if not restricted:
        return (1 + (xP + xA) * U) ** n
    return (1 + xA * U) ** n + n * xP * U * (1 + xA * U) ** (n - 1)


def rhs(xP, xA, y, D, U, Fv, restricted):
    x = xP + xA
    return (upf(2, xP, xA, U, restricted) * (1 + 3 * x * D) * (1 + y * Fv) ** 6,
            upf(3, xP, xA, U, restricted) * (1 + y * Fv) ** 6,
            upf(3, xP, xA, U, restricted) * (1 + 3 * x * D) * (1 + y * Fv) ** 5)


def family_d(checks: Checks) -> None:
    a, b, u = sp.symbols("a b u", positive=True)
    ok1 = True
    for n in (2, 3):
        # children: n successor positions, each empty, processed (weight a u) or amplified (weight b u); at most one processed
        total = 0
        for kinds_ in product(("empty", "P", "A"), repeat=n):
            if kinds_.count("P") > 1:
                continue
            term = 1
            for kk in kinds_:
                term *= {"empty": 1, "P": a * u, "A": b * u}[kk]
            total += term
        target = (1 + b * u) ** n + n * a * u * (1 + b * u) ** (n - 1)
        if mut("upfactor_wrong"):
            target = (1 + b * u) ** n + n * a * u * (1 + b * u) ** n
        ok1 = ok1 and sp.expand(total - target) == 0
    checks.check("D1", ok1, "T3: the remaining-slot up-factor of the relaxed upper count, (1 + x_A U)^n + n x_P U (1 + x_A U)^(n-1), is the sum over the successor configurations with at most one processed child, for n = 2 and 3 (symbolic)")
    certs = {
        (2, 2921, 1, 2): (Fraction(121, 1000), Fraction(38819515651721, 125000000000), Fraction(2614495936247, 1000000000000), Fraction(411275330287659, 1000000000000)),
        (2, 1464, 1, 1): (Fraction(121, 1000), Fraction(116365070741407, 500000000000), Fraction(652123939263, 250000000000), Fraction(3080327991177, 10000000000)),
        (2, 5841, 2, 4): (Fraction(61, 500), Fraction(151842195690607, 500000000000), Fraction(1303405077461, 500000000000), Fraction(12551068393373, 31250000000)),
        (2, 4380, 1, 3): (Fraction(121, 1000), Fraction(321841798858453, 1000000000000), Fraction(653785718103, 250000000000), Fraction(21312272709127, 50000000000)),
        (1, 405, 1, 2): (Fraction(91, 1000), Fraction(11697402025031, 1000000000000), Fraction(155146937439, 62500000000), Fraction(46962997959, 3125000000)),
        (1, 208, 1, 1): (Fraction(89, 1000), Fraction(10283263176051, 1000000000000), Fraction(152629090359, 62500000000), Fraction(2627739909739, 200000000000)),
        (1, 810, 2, 4): (Fraction(91, 1000), Fraction(11697402025031, 1000000000000), Fraction(155146937439, 62500000000), Fraction(46962997959, 3125000000)),
        (1, 605, 1, 3): (Fraction(93, 1000), Fraction(3032442310293, 250000000000), Fraction(2482877419491, 1000000000000), Fraction(7794092314937, 500000000000)),
    }
    ok2 = True
    for (c, pv, qv, rv), (t, Db, Ub, Fb) in certs.items():
        d1, d2, d3 = deviations(pv, qv, rv)
        e1, e2 = d1, max(d2, d3)
        if mut("certificate_wrong"):
            e2 = e2 * Fraction(11, 10)
        xP, xA, y = t, e2 / t ** c, e1 / t ** 3
        r = rhs(xP, xA, y, Db, Ub, Fb, True)
        Rbar = upf(3, xP, xA, Ub, True) * (1 + 3 * (xP + xA) * Db) * (1 + y * Fb) ** 6
        ok2 = ok2 and Db >= r[0] and Ub >= r[1] and Fb >= r[2] and min(Db, Ub, Fb) >= 1 and e1 * Rbar < Fraction(1, 10 ** 5)
    checks.check("D2", ok2, "T3: the rational triples are exact super-solutions of the relaxed upper recursion at (2921,1,2), (1464,1,1), (5841,2,4), (4380,1,3) with c = 2 and at (405,1,2), (208,1,1), (810,2,4), (605,1,3) with c = 1, each with epsilon_1 R-bar < 10^-5")
    # D3: the unrestricted recursion is the same code with the full up-factor, and block 30's certificate passes it
    t = Fraction(99, 1000)
    d1, d2, d3 = deviations(4165, 1, 2)
    e1, e2 = d1, max(d2, d3)
    Db, Ub, Fb = Fraction(56694252249173, 500000000000), Fraction(3279872914431, 1000000000000), Fraction(168429466648591, 1000000000000)
    r = rhs(t, e2 / t ** 2, e1 / t ** 3, Db, Ub, Fb, False)
    ok3 = Db >= r[0] and Ub >= r[1] and Fb >= r[2]
    r1 = rhs(t, e2 / t ** 2, e1 / t ** 3, Db, Ub, Fb, True)
    ok3 = ok3 and Db >= r1[0] and Ub >= r1[1] and Fb >= r1[2]
    checks.check("D3", ok3, "T3: with the full up-factor the same code is the linked full-slot polynomial and its certificate at (4165,1,2) passes it; the same triple also dominates the restricted recursion (the relaxed remaining-slot upper sum is termwise smaller)")


# ============================================================================================ family E — the restriction's admissibility on tiny realizations (T4)
def family_e(checks: Checks) -> None:
    etas = tiny_realizations(34, 60, shape=(3, 3, 5), lo=5, hi=10)
    same = differ = fits = 0
    ok = True
    for eta in etas:
        ones, npred, kind = kinds(eta)
        root = max(ones, key=level)
        for c in (Fraction(1), Fraction(2)):
            full = brute_min(eta, root, c)
            restr = brute_rooted(eta, root, c, one_child=True) if False else None
            # unrooted with the restriction: reuse brute_min's structure through a rooted call at the top site (all nodes are <= level(root))
            restr = brute_rooted(eta, root, c, one_child=True)
            if full is None:
                continue
            if restr == full:
                same += 1
            else:
                differ += 1
            if full <= 0:
                fits += 1
                ok = ok and restr is not None and restr <= 0
    checks.check("E1", ok and fits == 120 and same == 120 and differ == 0, f"T4 (executed): on 60 tiny realizations at c = 1 and 2, whenever a tree with the budget exists ({fits} cases) a tree with at most one processed child per node and the budget exists too; the restricted minimum equals the unrestricted one in {same} cases and differs in {differ}")


# ============================================================================================ family F
FENCES = ('This note proves finite rooted extension and seed lemmas, a sufficient induction conditional on an open tight-sibling statement, and a relaxed lifted-tree upper sum with eight rational point certificates.', 'The unrooted unit-budget converse and the local saturated-support characterization are not established; restricted admissibility and improved formation regions remain open.', 'Finite samples and historical floating solver observations do not complete formal negative certification; all original arguments and failures remain recoverable.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "optimal constant", "cannot be improved", "best possible",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 2921."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Gács", "Swart", "Szabó", "Toninelli", "Bramson", "Gray", "Krylov", "Bogolyubov", "Choquet", "Peierls", "Dobrushin", "Steiner")
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
N5_LINES = ('per_element: executed — extension and seed instances on140 tiny realizations by exact rooted enumeration and remaining-slot identity; universal statements use written proofs', 'per_site: executed — the fixed tiny sample and exact capped profiles ZA[-1,-1,-1], ZB[-1,-1,0], second tight site[-1,-1,-1]; no global absence claim', 'per_mode: checked and not executed — no spectral decomposition is present; finite parameter cases and rooted subsets are not spectral modes', 'per_block: executed — eight rational relaxed-upper-sum certificates, one full-slot comparison and120 equal minima/zero differences on60 fixed sampled realizations', 'lattice_wide: checked and not executed — no infinite simulation or universal restricted-admissibility test; finite-domain lemmas and relaxed injection have written proofs')


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
    family_e(checks)
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
