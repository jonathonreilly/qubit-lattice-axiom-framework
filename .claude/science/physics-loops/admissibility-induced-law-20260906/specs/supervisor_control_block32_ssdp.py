"""Single-usable-seed exact DP (integers / Fractions only).
Component: the connected component of the root in G restricted to 1-sites (arrows to 1-predecessors, forks between 1-siblings);
every tree of the family containing the root lies inside it.  If the component holds exactly one seed, every tree is one
arborescence (each non-seed node's arrow chain ends at that seed), there are no forks, and a node set N is the node set of a tree
iff root in N and every non-seed node of N has a 1-predecessor in N (an amplified node: its single one).
min cost = min over such N of  #proc(N) - c #amp(N)  (the seed contributes -3 + 3 = 0)."""
import sys, os
from fractions import Fraction as Fr
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK_OFFSETS = [tuple(E3[a][i] - E3[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]
def level(z): return z[0] + z[1] + z[2]
def preds(z): return [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)]

def component(eta, root):
    ones = {z for z, v in eta.items() if v == 1}
    seen = {root}; st = [root]
    while st:
        z = st.pop()
        nb = [p for p in preds(z) if p in ones] + [s for s in ones if z in preds(s)] + [tuple(z[i] + o[i] for i in range(3)) for o in FORK_OFFSETS]
        for w in nb:
            if w in ones and w not in seen:
                seen.add(w); st.append(w)
    return seen

def single_seed_min(eta, root, c, want_tree=False):
    comp = component(eta, root)
    npred = {z: [p for p in preds(z) if eta.get(p, 0) == 1] for z in comp}
    kind = {z: ("seed" if len(npred[z]) == 0 else "amp" if len(npred[z]) == 1 else "proc") for z in comp}
    seeds = [z for z in comp if kind[z] == "seed"]
    if len(seeds) != 1:
        return None, seeds, None
    s = seeds[0]
    cost = {z: (Fr(1) if kind[z] == "proc" else -Fr(c) if kind[z] == "amp" else Fr(0)) for z in comp}
    at = {}
    for z in comp: at.setdefault(level(z), []).append(z)
    Lmax, Ls, lr = max(at), level(s), level(root)
    # states: frozenset X_l -> (min cost of nodes at levels >= l, backpointer)
    states = {frozenset(): (Fr(0), None)}
    hist = []
    for l in range(Lmax, Ls, -1):
        nodes = sorted(at.get(l, [])); below = sorted(at.get(l - 1, []))
        nxt = {}
        # enumerate X_l consistent with the state's requirements: for a state at level l+1 (X_{l+1}), X_l must cover it
        # here we do it forward: states hold X_l; transition to X_{l-1}
        # first fill X_l states from the previous level's requirements
        if l == Lmax:
            cand = {}
            for mask in range(1 << len(nodes)):
                X = frozenset(nodes[i] for i in range(len(nodes)) if mask >> i & 1)
                if l == lr and root not in X: continue
                cand[X] = (sum(cost[z] for z in X), None)
            states = cand
        for X, (val, bp) in states.items():
            need = [z for z in X if kind[z] != "seed"]
            for mask in range(1 << len(below)):
                Y = frozenset(below[i] for i in range(len(below)) if mask >> i & 1)
                if l - 1 == lr and root not in Y: continue
                if any(not any(p in Y for p in npred[z]) for z in need): continue
                v2 = val + sum(cost[z] for z in Y)
                if Y not in nxt or v2 < nxt[Y][0]: nxt[Y] = (v2, X)
        hist.append(states)
        states = nxt
    # at the seed's level: X must be exactly {s}
    key = frozenset([s])
    if key not in states: return None, seeds, None
    best, bp = states[key]
    tree = None
    if want_tree:
        tree = [key]; X = bp; i = len(hist) - 1
        while X is not None and i >= 0:
            tree.append(X); X = hist[i][X][1]; i -= 1
        tree = sorted(set().union(*tree), key=level, reverse=True)
    return best, seeds, tree

if __name__ == "__main__":
    import ast, re, time, importlib
    sys.path.insert(0, sys.argv[1])
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from supervisor_control_block32_mintree import run_automaton
    m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_minimal_marked_tree_family_constant_at_least_one_exact_certificates_and_the_tree_route_floor_2026_09_17")
    cases = {}
    cases["Z_A"] = m.Z_A
    cases["Z_B"] = m.Z_B
    cases["W1"] = m.W1; cases["W2"] = m.W2; cases["W3"] = m.W3
    for name, (root, W, zeta) in cases.items():
        sites = [(a, b, cc) for a in range(W[0]) for b in range(W[1]) for cc in range(W[2])]
        eta = run_automaton(sites, {z: 1 for z in zeta})
        t0 = time.time()
        comp = component(eta, root)
        v1, seeds, tree = single_seed_min(eta, root, Fr(1), want_tree=True)
        if v1 is None:
            print(f"{name}: component {len(comp)} nodes, seeds in component {len(seeds)} -> multi-seed (subset DP not applicable)"); continue
        vp = single_seed_min(eta, root, Fr(101, 100))[0]; vm = single_seed_min(eta, root, Fr(99, 100))[0]
        npred = {z: [p for p in preds(z) if eta.get(p, 0) == 1] for z in comp}
        E = sum(1 for z in tree if len(npred[z]) >= 2); A = sum(1 for z in tree if len(npred[z]) == 1)
        print(f"{name}: component {len(comp)} of {sum(eta.values())} ones, one seed {seeds[0]}; exact min cost at c=1: {v1} (c=1.01: {vp}; c=0.99: {vm}); optimal tree E={E} |A|={A} -> c* = {Fr(E, A) if A else None}; {time.time()-t0:.2f}s")
