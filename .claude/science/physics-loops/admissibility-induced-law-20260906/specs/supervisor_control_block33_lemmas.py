import sys, os, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
from supervisor_control_block33_tight import rooted, m, run_automaton, level, preds
random.seed(int(sys.argv[2])); sites = [(a, b, c) for a in range(4) for b in range(4) for c in range(7)]
cases = []
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B), ("W1", m.W1)):
    root, (A_, B_, L_), marks = Z
    st = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    cases.append((name, run_automaton(st, {z: 1 for z in marks})))
n = 0
while n < int(sys.argv[3]):
    zeta = {z: 1 for z in random.sample(sites, random.randint(3, 16))}
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 12 or len(ones) > 60: continue
    cases.append((f"rand{n}", eta)); n += 1
tight_nodes = []; tab = {}; L1 = L2 = L3 = 0; L1v = L2v = L3v = 0; total_proc = 0
for name, eta in cases:
    ones, npred, kind = m.kinds(eta)
    vc = {}
    def v(z):
        if z not in vc: vc[z] = rooted(eta, z)[0]
        return vc[z]
    for z in ones:
        if kind[z] != "proc": continue
        total_proc += 1
        ps = npred[z]; ks = tuple(sorted(kind[u] for u in ps)); vz = v(z)
        pv = [v(u) for u in ps if kind[u] == "proc"]
        key = (ks, vz); tab[key] = tab.get(key, 0) + 1
        if vz == 0: tight_nodes.append((name, z, [(u, kind[u], v(u)) for u in ps]))
        # L1: a processed node with a seed 1-predecessor has v <= -1
        if "seed" in ks:
            L1 += 1; L1v += (vz > -1)
        # L2: a processed node with >= 3 one-predecessors has v <= -1
        if len(ps) >= 3:
            L2 += 1; L2v += (vz > -1)
        # L3: a processed node with two processed 1-preds (no seed, no amp) has some pred with v <= -1, or v(z) <= -1 anyway
        if ks == ("proc", "proc"):
            L3 += 1; L3v += (min(pv) > -1 and vz > -1)
print(f"{len(cases)} realizations, {total_proc} processed nodes")
print("tight processed nodes (v = 0):", tight_nodes)
print(f"L1 (seed pred => v <= -1): {L1} cases, violations {L1v}")
print(f"L2 (>= 3 one-preds => v <= -1): {L2} cases, violations {L2v}")
print(f"L3 (two processed preds, no seed/amp: some pred v <= -1 or v(z) <= -1): {L3} cases, violations {L3v}")
print("table (pred kinds, v(z)) -> count:")
for k in sorted(tab, key=lambda kv: (kv[0], kv[1])): print("   ", k, tab[k])
