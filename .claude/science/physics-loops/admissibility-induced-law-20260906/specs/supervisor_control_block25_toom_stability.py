"""Control, block 25 (supervisor): the explanation-tree construction for the level automaton (module supervisor_control_block25_toom_core.py),
run exhaustively on the depth-2 backward cone, on every depth-3 configuration with at most four noise sites, on random cones of depth 3-6 and 7-10,
and on structured seeds; then the exact Peierls arithmetic, the least couplings p_0 and the subtree counts. The first draft of the core let two forks
sharing a point be adjacent in the cause graph; the very first depth-2 configuration then gave 5 edges for 2 noise nodes (the skipped cluster
held two uncounted noise sites); the bipartite cause graph fixed it (recorded in CHECKER_block25_findings.md)."""
import sys, os, random, time
from itertools import product, combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib; toom_core = importlib.import_module("supervisor_control_block25_toom_core"); globals().update({k: getattr(toom_core, k) for k in dir(toom_core) if not k.startswith("__")})
random.seed(25)
x = (0, 0, 0)
def test_config(depth, zeta, stats):
    sites = cone(x, depth)
    eta = run_automaton(sites, zeta)
    if eta[x] != 1:
        return
    ex = Explainer(eta, zeta)
    nodes, edges, noise_nodes, refs = ex.explain(x)
    n = len(noise_nodes)
    assert n >= 1
    assert check_tree(nodes, edges, x, ex), "tree check failed"
    assert noise_nodes <= ex.noise
    assert all(zeta.get(z, 0) == 1 for z in noise_nodes)
    ne = len(edges)
    assert ne <= 4 * (n - 1), ("edge bound violated", ne, n, refs)
    stats["cases"] += 1
    stats["max_ratio"] = max(stats["max_ratio"], ne / max(n - 1, 1))
    stats["max_edges"] = max(stats["max_edges"], ne)
    stats["max_n"] = max(stats["max_n"], n)
    stats["max_refs"] = max(stats["max_refs"], refs)
stats = {"cases": 0, "max_ratio": 0.0, "max_edges": 0, "max_n": 0, "max_refs": 0}
t0 = time.time()
sites2 = cone(x, 2)
for bits in product((0, 1), repeat=len(sites2)):
    zeta = {z: b for z, b in zip(sites2, bits) if b}
    test_config(2, zeta, stats)
print(f"depth 2 exhaustive (1024 configs): explained cases {stats['cases']}, max edges/(n-1) = {stats['max_ratio']:.3f}, max edges {stats['max_edges']}, max n {stats['max_n']} ({time.time()-t0:.1f}s)")
stats3 = {"cases": 0, "max_ratio": 0.0, "max_edges": 0, "max_n": 0, "max_refs": 0}
sites3 = cone(x, 3)
for k in range(1, 5):
    for combo in combinations(sites3, k):
        zeta = {z: 1 for z in combo}
        test_config(3, zeta, stats3)
print(f"depth 3, all configs with <= 4 noise sites: explained cases {stats3['cases']}, max ratio {stats3['max_ratio']:.3f}, max edges {stats3['max_edges']}, max n {stats3['max_n']} ({time.time()-t0:.1f}s)")
stats4 = {"cases": 0, "max_ratio": 0.0, "max_edges": 0, "max_n": 0, "max_refs": 0}
for trial in range(3000):
    depth = random.choice((3, 4, 5, 6))
    dens = random.choice((0.15, 0.3, 0.5))
    sites = cone(x, depth)
    zeta = {z: 1 for z in sites if random.random() < dens}
    test_config(depth, zeta, stats4)
print(f"random cones depth 3-6 (3000 trials): explained cases {stats4['cases']}, max ratio {stats4['max_ratio']:.3f}, max edges {stats4['max_edges']}, max n {stats4['max_n']}, max refinements {stats4['max_refs']} ({time.time()-t0:.1f}s)")
# structured seeds: a line of n+1 noise sites at level -n in the direction e1-e2 ; a triangle seed; a strip refreshed by one noise per level
stats5 = {"cases": 0, "max_ratio": 0.0, "max_edges": 0, "max_n": 0, "max_refs": 0}
for n in range(1, 9):
    zeta = {sub(x, (a, n - a, 0)): 1 for a in range(n + 1)}
    test_config(n, zeta, stats5)
for n in range(1, 7):
    zeta = {z: 1 for z in cone(x, n) if level(z) == -n}
    test_config(n, zeta, stats5)
for n in range(2, 9):
    zeta = {}
    for s in range(1, n + 1):
        zeta[sub(x, (0, s, 0))] = 1
        zeta[sub(x, (1, s - 1, 0))] = 1 if s == n else zeta.get(sub(x, (1, s - 1, 0)), 0)
    test_config(n, zeta, stats5)
print(f"structured seeds: explained cases {stats5['cases']}, max ratio {stats5['max_ratio']:.3f}, max edges {stats5['max_edges']}, max n {stats5['max_n']}")

# ---- deep stress ----
random.seed(2525)
x = (0, 0, 0)
worst = (0.0, None); cases = 0; t0 = time.time(); fails = 0
for trial in range(1500):
    depth = random.choice((7, 8, 9, 10))
    dens = random.choice((0.05, 0.1, 0.2, 0.35, 0.6))
    sites = cone(x, depth)
    zeta = {z: 1 for z in sites if random.random() < dens}
    eta = run_automaton(sites, zeta)
    if eta[x] != 1:
        continue
    ex = Explainer(eta, zeta)
    try:
        nodes, edges, noise_nodes, refs = ex.explain(x)
    except AssertionError as err:
        fails += 1; print("FAILURE:", err, "depth", depth, "dens", dens); continue
    n = len(noise_nodes); ne = len(edges)
    ok = check_tree(nodes, edges, x, ex) and noise_nodes <= ex.noise and ne <= 4 * (n - 1)
    if not ok:
        fails += 1; print("VIOLATION: edges", ne, "n", n, "depth", depth)
    cases += 1
    r = ne / max(n - 1, 1)
    if r > worst[0]: worst = (r, (depth, dens, n, ne, refs))
print(f"deep random cones (depth 7-10, 1500 trials): explained {cases}, failures {fails}, worst ratio {worst[0]:.3f} at (depth, dens, n, edges, refinements) = {worst[1]}, {time.time()-t0:.0f}s")
