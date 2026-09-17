"""Exact minimum of cost(T) = (#processed) - c (#amplified) - 3 (#seeds - 1) over ALL marked trees of the counted family containing x,
by a dynamic program over levels (integers / Fractions only).  State after level l: (X_l, partition of X_l into components of the
partial tree above).  Transitions: one downward arrow per non-seed node of X_l (amplified: forced), extra top nodes at level l-1,
forks at level l-1 as coarsenings of the partition along sibling pairs; cycles rejected; a component without a foot is rejected
unless it is the whole tree (termination: one component, all of whose nodes at the current level are seeds)."""
import sys, os
from fractions import Fraction as Fr
from itertools import product, combinations
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORK_OFFSETS = [tuple(E3[a][i] - E3[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]
def level(z): return z[0] + z[1] + z[2]
def preds(z): return [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)]

def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p

def coarsenings(blocks, fork_pairs):
    """all partitions coarser than `blocks` whose merged blocks are connected through fork_pairs (pairs of nodes)."""
    n = len(blocks)
    blk_of = {}
    for i, b in enumerate(blocks):
        for v in b: blk_of[v] = i
    adj = {i: set() for i in range(n)}
    for (u, v) in fork_pairs:
        i, j = blk_of.get(u), blk_of.get(v)
        if i is None or j is None or i == j: continue
        adj[i].add(j); adj[j].add(i)
    out = []
    for p in set_partitions(range(n)):
        ok = True
        for grp in p:
            # grp must be connected in adj
            seen = {grp[0]}; st = [grp[0]]; gs = set(grp)
            while st:
                a = st.pop()
                for b in adj[a]:
                    if b in gs and b not in seen: seen.add(b); st.append(b)
            if seen != gs: ok = False; break
        if ok:
            out.append([sorted(sum((blocks[i] for i in grp), [])) for grp in p])
    return out

def min_tree_cost(eta, root, c, cost_seed=-3, verbose=False):
    ones = [z for z, v in eta.items() if v == 1]
    ones_at = {}
    for z in ones: ones_at.setdefault(level(z), []).append(z)
    npred = {z: [p for p in preds(z) if eta.get(p, 0) == 1] for z in ones}
    kind = {z: ("seed" if len(npred[z]) == 0 else "amp" if len(npred[z]) == 1 else "proc") for z in ones}
    cost = {z: (Fr(1) if kind[z] == "proc" else -Fr(c) if kind[z] == "amp" else Fr(cost_seed)) for z in ones}
    Lmax, Lmin = max(ones_at), min(ones_at)
    lr = level(root)
    # states: dict (frozenset X, frozenset of frozenset blocks) -> min cost of the partial tree (all nodes at levels >= l)
    states = {}
    best = None
    # start: at level Lmax, any X (subset of ones at Lmax); partition = each node alone? forks at that level may join them: use coarsenings
    def init_level(l):
        out = {}
        nodes = ones_at.get(l, [])
        pairs = [(u, v) for u, v in combinations(nodes, 2) if tuple(v[i] - u[i] for i in range(3)) in FORK_OFFSETS]
        for r in range(len(nodes) + 1):
            for X in combinations(nodes, r):
                if l == lr and root not in X: continue
                blocks = [[z] for z in X]
                for P in coarsenings(blocks, pairs):
                    key = (frozenset(X), frozenset(frozenset(b) for b in P))
                    val = sum(cost[z] for z in X)
                    if key not in out or val < out[key]: out[key] = val
        return out
    states = init_level(Lmax)
    for l in range(Lmax, Lmin - 1, -1):
        # termination check at level l
        for (X, P), val in states.items():
            if len(P) == 1 and all(kind[z] == "seed" for z in X) and (l <= lr):
                # complete tree (root at a level >= l: ensured since root forced at lr and l <= lr)
                if best is None or val < best: best = val
            if len(P) == 0 and l > lr:
                pass
        if l == Lmin: break
        nxt = {}
        below = ones_at.get(l - 1, [])
        pairs_below = [(u, v) for u, v in combinations(below, 2) if tuple(v[i] - u[i] for i in range(3)) in FORK_OFFSETS]
        for (X, P), val in states.items():
            X = sorted(X); P = [sorted(b) for b in P]
            nonseed = [z for z in X if kind[z] != "seed"]
            # a component all of whose level-l nodes are seeds has no foot below: invalid to continue (it was checked for termination)
            if any(all(kind[z] == "seed" for z in b) for b in P) and len(P) > 0:
                continue
            choices = [npred[z] for z in nonseed]
            for arrows in product(*choices):
                # graph on components + targets
                comp_of = {}
                for i, b in enumerate(P):
                    for z in b: comp_of[z] = i
                # cycle check: two nodes of one component to the same target, handled by union-find on (comp i) and (target u)
                parent = {}
                def find(a):
                    while parent[a] != a:
                        parent[a] = parent[parent[a]]; a = parent[a]
                    return a
                def union(a, b):
                    ra, rb = find(a), find(b)
                    if ra == rb: return False
                    parent[ra] = rb; return True
                for i in range(len(P)): parent[("c", i)] = ("c", i)
                targets = set()
                ok = True
                for z, u in zip(nonseed, arrows):
                    if ("t", u) not in parent: parent[("t", u)] = ("t", u)
                    targets.add(u)
                    if not union(("c", comp_of[z]), ("t", u)): ok = False; break
                if not ok: continue
                free = [y for y in below if y not in targets]
                base_blocks = {}
                for u in targets:
                    base_blocks.setdefault(find(("t", u)), []).append(u)
                base_blocks = [sorted(b) for b in base_blocks.values()]
                for r in range(len(free) + 1):
                    for Y in combinations(free, r):
                        if l - 1 == lr and root not in targets and root not in Y: continue
                        blocks = base_blocks + [[y] for y in Y]
                        Xn = sorted(targets | set(Y))
                        for Pn in coarsenings(blocks, pairs_below):
                            key = (frozenset(Xn), frozenset(frozenset(b) for b in Pn))
                            v2 = val + sum(cost[z] for z in Xn)
                            if key not in nxt or v2 < nxt[key]: nxt[key] = v2
        states = nxt
        if verbose: print(f"level {l-1}: {len(states)} states")
    return None if best is None else best + 3   # cost = E - 3(|S| - 1) - c|A| = sum of node costs + 3

if __name__ == "__main__":
    import importlib, time
    sys.path.insert(0, sys.argv[1])
    m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_minimal_marked_tree_family_constant_at_least_one_exact_certificates_and_the_tree_route_floor_2026_09_17")
    root, (A_, B_, L_), marks = m.W1
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    eta = m.run_automaton(sites, {z: 1 for z in marks})
    for c in (Fr(1), Fr(3, 4), Fr(1, 2), Fr(0)):
        t0 = time.time(); v = min_tree_cost(eta, root, c, verbose=(c == 1))
        print(f"W1: c = {c}: exact min cost over all trees = {v}   ({time.time()-t0:.1f}s)   [MILP: c* = 3/4 with (E,|A|,|S|,F) = (6,8,1,0): cost at c = 6 - 8c]")
