import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from supervisor_control_block32_mintree import MinTree, run_automaton, level, preds, FORK_OFFSETS
from supervisor_control_block32_treedp import min_tree_cost
def brute(eta, root, c):
    ones = [z for z, v in eta.items() if v == 1]
    npred = {z: [p for p in preds(z) if eta.get(p, 0) == 1] for z in ones}
    kind = {z: ("seed" if len(npred[z]) == 0 else "amp" if len(npred[z]) == 1 else "proc") for z in ones}
    cost = {z: (Fr(1) if kind[z] == "proc" else -Fr(c) if kind[z] == "amp" else Fr(-3)) for z in ones}
    best = None; bt = None
    others = [z for z in ones if z != root]
    for r in range(len(others) + 1):
        for sub in itertools.combinations(others, r):
            N = set(sub) | {root}
            nonseed = [z for z in N if kind[z] != "seed"]
            choices = [[u for u in npred[z] if u in N] for z in nonseed]
            if any(len(ch) == 0 for ch in choices): continue
            pairs = [(u, v) for u, v in itertools.combinations(sorted(N), 2) if tuple(v[i] - u[i] for i in range(3)) in FORK_OFFSETS]
            S = sum(1 for z in N if kind[z] == "seed")
            val = sum(cost[z] for z in N) + 3   # cost = E - 3(S-1) - cA  -> sum(cost) = E - 3S - cA ; add 3
            if best is not None and val >= best: continue
            found = False
            for arrows in itertools.product(*choices):
                # arborescence components
                parent = {z: z for z in N}
                def find(a):
                    while parent[a] != a: a = parent[a]
                    return a
                for z, u in zip(nonseed, arrows):
                    parent[find(z)] = find(u)
                comps = {find(z) for z in N}
                if len(comps) != S: continue   # arrows acyclic automatically (levels decrease); components = seeds
                # need S-1 forks connecting components without cycles: spanning tree of the quotient multigraph exists iff quotient connected
                qadj = {cpt: set() for cpt in comps}
                for (u, v) in pairs:
                    a, b = find(u), find(v)
                    if a != b: qadj[a].add(b); qadj[b].add(a)
                start = next(iter(comps)); seen = {start}; st = [start]
                while st:
                    a = st.pop()
                    for b in qadj[a]:
                        if b not in seen: seen.add(b); st.append(b)
                if seen == comps:
                    found = True; break
            if found:
                best = val; bt = (sorted(N), S)
    return best, bt
random.seed(5)
sites = [(a, b, c) for a in range(3) for b in range(3) for c in range(4)]
mism = 0; tested = 0
for trial in range(400):
    zeta = {z: 1 for z in random.sample(sites, random.randint(1, 5))}
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 4 or len(ones) > 11: continue
    root = max(ones, key=level)
    if level(root) < 2: continue
    c = Fr(random.choice([1, 2, 3]), random.choice([1, 2]))
    b, bt = brute(eta, root, c)
    d = min_tree_cost(eta, root, c)
    mt = MinTree(eta, root); r = mt.solve(float(c))
    mv = None if r is None else Fr(r["E"] - 3 * (r["S"] - 1)) - c * r["A"]
    tested += 1
    if not (b == d == mv):
        mism += 1
        if mism <= 4:
            print(f"MISMATCH c={c}: brute={b} dp={d} milp={mv}; ones={sorted(ones)}; root={root}; brute tree={bt}; milp tree nodes={None if r is None else sorted(r['nodes'])}")
print(f"tested {tested} tiny configurations: mismatches {mism}")
