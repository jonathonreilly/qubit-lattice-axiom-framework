"""Probe library: the two-level noisy majority automaton in level time (blocks 25-33), its marked explanation trees, the exact
single-seed minimum, a brute-force enumerator of the counted family, and the recorded realizations.  Extracted from the block-32
runner (PR #8176); floats allowed here (probes are not runners)."""
from fractions import Fraction
from itertools import combinations, product
import random

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
