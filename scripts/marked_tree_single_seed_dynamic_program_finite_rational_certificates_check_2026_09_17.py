#!/usr/bin/env python3
"""Finite single-seed dynamic programming, explicit marked-tree ratios and
four supplied polynomial point certificates. Complete finite fixtures and
exact arithmetic retained; broader negative certification is deferred.
No physical phase, optimum or real rounded threshold is established.
Stdout-only checks; no historical search or optimizer is executed.
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

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/MARKED_TREE_SINGLE_SEED_DYNAMIC_PROGRAM_AND_FINITE_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
INPUT_SHA256 = {'docs/MARKED_TREE_SINGLE_SEED_DYNAMIC_PROGRAM_AND_FINITE_RATIONAL_CERTIFICATES_BOUNDED_THEOREM_NOTE_2026-09-17.md': '10003c417a65f6d7b14bc50a7d7b191b777d08d11811fac448ebd3d774bf4448', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md': 'cc7e8423b3bb35f7f2cf4699d498556b98fbc55229eb8a5d9f52e1ba00a63f97'}
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "marked_tree_single_seed_dynamic_program_and_finite_rational_certificates_bounded_theorem_note_2026-09-17"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "forks_dropped_in_family": "B",
    "isolated_seed_cost_wrong": "B",
    "zb_mark_count_wrong": "C",
    "real_boundary_rounded": "E",
    "extremal_marks_wrong": "C",
    "family_bound_asserted": "C",
    "witness_tree_wrong": "D",
    "certificate_wrong": "E",
    "floor_wrong": "E",
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
# cheap trees of block 31's witnesses W2 and W3 found by the integer program (control); each: nodes, arrows (node, 1-predecessor), forks (sibling pair)
W2_TREE = dict(root=(3, 3, 6), E=7, A=11, S=2, F=1, ratio='4/11',
    arrows=[((0, 0, 1), (0, 0, 0)), ((0, 0, 2), (0, 0, 1)), ((0, 1, 0), (0, 0, 0)), ((0, 1, 1), (0, 0, 1)), ((0, 2, 1), (0, 1, 1)), ((0, 3, 1), (0, 2, 1)), ((1, 0, 0), (0, 0, 0)), ((1, 2, 1), (0, 2, 1)), ((2, 1, 3), (2, 0, 3)), ((2, 1, 4), (2, 1, 3)), ((2, 2, 1), (1, 2, 1)), ((2, 2, 2), (2, 2, 1)), ((2, 2, 4), (2, 1, 4)), ((2, 2, 5), (2, 2, 4)), ((2, 3, 5), (2, 2, 5)), ((2, 3, 6), (2, 3, 5)), ((3, 2, 2), (2, 2, 2)), ((3, 3, 6), (2, 3, 6))],
    forks=[((2, 1, 3), (2, 2, 2))])
W3_TREE = dict(root=(4, 4, 5), E=9, A=17, S=8, F=7, ratio='-12/17',
    arrows=[((1, 0, 0), (0, 0, 0)), ((1, 1, 5), (0, 1, 5)), ((1, 2, 8), (0, 2, 8)), ((2, 0, 0), (1, 0, 0)), ((2, 1, 0), (2, 0, 0)), ((2, 1, 5), (1, 1, 5)), ((2, 1, 6), (2, 1, 5)), ((2, 1, 7), (1, 1, 7)), ((2, 1, 8), (2, 1, 7)), ((2, 2, 0), (2, 1, 0)), ((2, 2, 1), (2, 2, 0)), ((2, 3, 1), (2, 2, 1)), ((2, 3, 2), (2, 3, 1)), ((2, 3, 3), (2, 3, 2)), ((3, 1, 6), (2, 1, 6)), ((3, 2, 0), (2, 2, 0)), ((3, 3, 3), (2, 3, 3)), ((3, 3, 4), (3, 3, 3)), ((3, 4, 4), (3, 3, 4)), ((3, 4, 5), (3, 4, 4)), ((4, 0, 5), (4, 0, 4)), ((4, 0, 6), (4, 0, 5)), ((4, 1, 6), (3, 1, 6)), ((4, 2, 6), (4, 1, 6)), ((4, 3, 6), (4, 2, 6)), ((4, 4, 5), (3, 4, 5))],
    forks=[((1, 1, 7), (2, 1, 6)), ((1, 2, 8), (2, 1, 8)), ((2, 1, 8), (3, 0, 8)), ((2, 3, 1), (2, 4, 0)), ((3, 1, 6), (4, 0, 6)), ((3, 2, 0), (4, 1, 0)), ((4, 3, 6), (4, 4, 5))])



# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "the context-only product-law note carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT,p).is_file() and hashlib.sha256(Path(ROOT,p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all three declared inputs match literal SHA-256 pins")


# ============================================================================================ family B — the reduction (T1)
def family_b(checks: Checks) -> None:
    eta_seed = {(0, 0, 0): 1}
    seed_cost, _, seed_nodes = single_seed_min(eta_seed, (0, 0, 0), Fraction(1))
    expected_seed = Fraction(1) if mut("isolated_seed_cost_wrong") else Fraction(0)
    checks.check("B3", seed_cost == expected_seed and tree_counts(eta_seed, seed_nodes) == (0, 0, 1), "isolated seed: zero cost and zero amplification; restricted positive-amplification ratio domain is empty")
    random.seed(32)
    sites = [(a, b, c) for a in range(3) for b in range(3) for c in range(4)]
    agree = tested = multi = forks_matter = 0
    ok = True
    while tested < 90 or multi < 25:
        zeta = {z: 1 for z in random.sample(sites, random.randint(1, 5))}
        eta = run_automaton(sites, zeta)
        ones = [z for z, v in eta.items() if v == 1]
        if len(ones) < 4 or len(ones) > 10:
            continue
        root = max(ones, key=level)
        if level(root) < 2:
            continue
        c = Fraction(random.choice([1, 2, 3]), random.choice([1, 2]))
        comp = component(eta, root)
        seeds_in = [z for z in comp if kinds(eta)[2][z] == "seed"]
        b = brute_min(eta, root, c, with_forks=not mut("forks_dropped_in_family"))
        if len(seeds_in) == 1:
            d, seeds, N = single_seed_min(eta, root, c)
            tested += 1
            if d == b and N is not None:
                agree += 1
            else:
                ok = False
        else:
            multi += 1
            b0 = brute_min(eta, root, c, with_forks=False)
            if b is not None and (b0 is None or b < b0):
                forks_matter += 1
            if b0 is not None and b is not None and b > b0:
                ok = False
        if tested > 400:
            break
    checks.check("B1", ok and agree == tested and tested >= 90, f"T1: on {tested} tiny realizations whose component holds one seed, the subset dynamic program equals the brute-force minimum over the full family (forks included) in every case ({agree})")
    checks.check("B2", forks_matter >= 10 and multi >= 25, f"T1: on {multi} tiny realizations with several seeds in the component, forks lower the minimum or are needed for any tree in {forks_matter} cases (the multi-seed part of the family is not vacuous; the single-seed reduction is used only where the component holds one seed)")


# ============================================================================================ family C — the extremal realizations (T2)
def realization(w, drop=None):
    root, (A_, B_, L_), marks = w
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    zeta = {z: 1 for z in marks if z != drop}
    return run_automaton(sites, zeta), root


def family_c(checks: Checks) -> None:
    mark_target = 108 if mut("zb_mark_count_wrong") else 36
    checks.check("C4", len(Z_B[2]) == len(set(Z_B[2])) == mark_target, "Z_B has exactly36 distinct marked sites; the original fixture bytes are retained")
    etaA, rootA = realization(Z_A, drop=(2, 1, 3) if mut("extremal_marks_wrong") else None)
    compA = component(etaA, rootA)
    v1, seedsA, N1 = single_seed_min(etaA, rootA, Fraction(1))
    v99, _, _ = single_seed_min(etaA, rootA, Fraction(99, 100))
    v101, _, _ = single_seed_min(etaA, rootA, Fraction(101, 100))
    okA = len(seedsA) == 1 and len(compA) == 42 and v1 == 0 and v99 == Fraction(3, 50) and v101 == Fraction(-1, 10)
    E, A, S = tree_counts(etaA, N1) if N1 else (None, None, None)
    # the exhibited optimal tree: arrows chosen inside N (any 1-predecessor in N; amplified: its single one)
    if N1:
        ones, npred, kind = kinds(etaA)
        arrows = [(z, [u for u in npred[z] if u in N1][0]) for z in N1 if kind[z] != "seed"]
        okA = okA and verify_tree(etaA, rootA, N1, arrows, []) and (E, A, S) == (6, 6, 1)
    checks.check("C1", okA, f"T2: realization Z_A (window 4x4x7, 20 marks, root (3,3,3)): the component of the root has 42 of the 46 ones and one seed; the exact minimum of E - 3(|S|-1) - c|A| over every tree of the family is 0 at c = 1, 3/50 at c = 99/100 and -1/10 at c = 101/100; the optimal tree has E = |A| = 6 and is verified: finite minimum at c=1 is zero")
    etaB, rootB = realization(Z_B)
    compB = component(etaB, rootB)
    w1, seedsB, NB = single_seed_min(etaB, rootB, Fraction(1))
    w99, _, _ = single_seed_min(etaB, rootB, Fraction(99, 100))
    target = Fraction(101, 100) if mut("family_bound_asserted") else Fraction(1)
    wt, _, _ = single_seed_min(etaB, rootB, target)
    okB = len(seedsB) == 1 and len(compB) == 60 and w1 == 0 and w99 == Fraction(2, 25) and wt >= 0
    EB, AB, SB = tree_counts(etaB, NB) if NB else (None, None, None)
    okB = okB and (EB, AB, SB) == (9, 9, 1)
    checks.check("C2", okB, f"T2: realization Z_B (window 5x5x8, root (4,4,4)): the component has 60 of the 69 ones and one seed; the minimum is 0 at c = 1 and 2/25 at c = 99/100; the optimal tree has E = |A| = 9")
    grid = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(99, 100), Fraction(1), Fraction(101, 100)]
    vals = [single_seed_min(etaA, rootA, c)[0] for c in grid]
    okC = all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1)) and vals[0] == 6 and vals[-2] == 0
    checks.check("C3", okC, f"T2: on Z_A the minimum is non-increasing in c along {[str(c) for c in grid]} with values {[str(v) for v in vals]}; the concavity proof is written in the note; these are finite rational values, with zero-credit minimum6")


# ============================================================================================ family D — block 31's witnesses have cheap trees (T3)
def family_d(checks: Checks) -> None:
    eta1, root1 = realization(W1)
    v34, seeds1, N34 = single_seed_min(eta1, root1, Fraction(3, 4))
    v74, _, _ = single_seed_min(eta1, root1, Fraction(74, 100))
    E, A, S = tree_counts(eta1, N34) if N34 else (None, None, None)
    ok1 = len(seeds1) == 1 and v34 == 0 and v74 > 0 and (E, A, S) == (6, 8, 1)
    checks.check("D1", ok1, "T3: W1 (the first supplied witness) has a single-seed component; the minimum is 0 at c = 3/4 and positive at 74/100, with an optimal tree E = 6, |A| = 8: the family's constant on W1 is exactly 3/4 against the construction's 8/5")
    eta2, root2 = realization(W2)
    forks2 = list(W2_TREE["forks"])
    if mut("witness_tree_wrong"):
        forks2 = forks2[:-1]
    nodes2 = {z for e in W2_TREE["arrows"] for z in e} | {z for e in forks2 for z in e} | {root2}
    ok2 = verify_tree(eta2, root2, nodes2, W2_TREE["arrows"], forks2)
    E2, A2, S2 = tree_counts(eta2, nodes2)
    ok2 = ok2 and (E2, A2, S2, len(forks2)) == (7, 11, 2, 1) and Fraction(E2 - 3 * (S2 - 1), A2) == Fraction(4, 11)
    checks.check("D2", ok2, "T3: W2 carries a verified tree of the family with E = 7, |A| = 11, |S| = 2, one fork: ratio 4/11 against the construction's 5/3")
    eta3, root3 = realization(W3)
    nodes3 = {z for e in W3_TREE["arrows"] for z in e} | {z for e in W3_TREE["forks"] for z in e} | {root3}
    ok3 = verify_tree(eta3, root3, nodes3, W3_TREE["arrows"], W3_TREE["forks"])
    E3_, A3, S3 = tree_counts(eta3, nodes3)
    ok3 = ok3 and (E3_, A3, S3, len(W3_TREE["forks"])) == (9, 17, 8, 7) and E3_ - 3 * (S3 - 1) == -12
    checks.check("D3", ok3, "T3: W3 carries a verified tree with E = 9, |A| = 17, |S| = 8, seven forks: E - 3(|S|-1) = -12, raw ratio -12/17, not clamped")


# ============================================================================================ family E — the stake and the floor (T4)
def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def family_e(checks: Checks) -> None:
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
    checks.check("E1", ok, "T4: for the supplied polynomial definitions, the rational triples at (453,1,2), (232,1,1), (905,2,4), (677,1,3) are exact super-solutions at (t + epsilon_2/t, epsilon_1/t^3) with epsilon_1 R-bar < 10^-5 (four points only; no parameter interval or physical conclusion)")
    t = sp.symbols("t", positive=True)
    top = sp.Rational(4, 729) if not mut("floor_wrong") else sp.Rational(5, 729)
    m1 = sp.maximum(t * (sp.Rational(4, 27) - t), t, sp.Interval(0, sp.Rational(4, 27)))
    ok2 = sp.simplify(m1 - top) == 0
    # for c >= 1 and 0 < t < 1: t^c <= t, so max_t t^c (4/27 - t) <= 4/729
    cs = sp.symbols("c", positive=True)
    ok2 = ok2 and sp.simplify((t ** cs).subs({t: sp.Rational(1, 2), cs: 1}) - sp.Rational(1, 2)) == 0 and all(Fraction(1, 2) ** k <= Fraction(1, 2) for k in (1, 2, 3))
    d3a = deviations(367, 1, 2)[2]
    d3b = deviations(368, 1, 2)[2]
    ok2 = ok2 and d3a > Fraction(4, 729) > d3b
    checks.check("E2", ok2, f"T4: scalar maximum4/729 and integer crossing367/368; d3 values {d3a}, {d3b}; conditional algebra, not a physical route theorem")
    real_p = Fraction(36799, 100)
    real_d3 = deviations(real_p, 1, 2)[2]
    polynomial = 4 * real_p ** 2 - 1450 * real_p - 7975
    scalar_ok = real_d3 < Fraction(4, 729) and polynomial > 0
    if mut("real_boundary_rounded"):
        scalar_ok = scalar_ok and real_p >= 368
    checks.check("E3", scalar_ok, "real p=36799/100 satisfies the exact necessary polynomial inequality; this is not a full recursion certificate")


# ============================================================================================ family F
FENCES = ('This note retains exact finite marked-tree minima, explicit witness ratios and four supplied polynomial certificates; no physical rule, order or coupling is selected.', 'The ratio statistic is defined only on its nonempty positive-amplification domain; zero-amplification costs remain defined and negative witness ratios are not clamped.', 'Formal negative certification and global construction conclusions remain deferred; finite checks and point certificates do not supply five closed attack families.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "optimal constant", "cannot be improved", "best possible",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 453."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Gács", "Swart", "Szabó", "Toninelli", "Bramson", "Gray", "Krylov", "Bogolyubov", "Choquet", "Peierls", "Dobrushin", "Steiner")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T4", phrase + "\n\n## Theorem T4", 1)
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
N5_LINES = ('per_element: executed — exact rational finite-subset costs, tree counts and the completed-square scalar maximum; full DP completeness is a written proof', 'per_site: executed — five fixed finite marked windows, component connectivity and predecessor/fork validation; Z_B contains36 distinct marks', 'per_mode: checked and not executed — no spectral decomposition is used; cost parameters and finite subsets are not spectral modes', 'per_block: executed — unchanged seeded tiny-fixture batch, exact finite minima, four supplied-recursion points and isolated-seed/real-scalar boundaries', 'lattice_wide: checked and not executed — no infinite lattice or global construction search; the written conditional implications have deferred formal negative certification')


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
