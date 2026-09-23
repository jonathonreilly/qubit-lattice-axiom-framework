import sys, os, random
sys.path.insert(0, sys.argv[1])
import supervisor_control_block33_core30 as core
random.seed(int(sys.argv[2])); N = int(sys.argv[3])

def make_explainer(eta, zeta, modified):
    ex = core.Explainer(eta, zeta)
    state = {"cur": {}, "forced": 0, "avoided": 0}
    orig = ex.excuse_k
    def excuse_k(v, k):
        if k == 0: state["cur"] = {}
        if v in ex.amp:
            u = core.preds(v)[ex.amp_dir[v]]; state["cur"][k] = (v, u); return u
        a, b = ex.exc[v]
        opts = [core.preds(v)[i] for i in (a, b) if i != k]
        taken = {uu for kk, (vv, uu) in state["cur"].items() if vv != v}
        if modified and len(opts) == 2:
            free = [u for u in opts if u not in taken]
            if free and free[0] != opts[0]: state["avoided"] += 1
            u = (free or opts)[0]
        else:
            u = opts[0]
            if modified and u in taken: state["forced"] += 1
        state["cur"][k] = (v, u); return u
    ex.excuse_k = excuse_k
    ex._state = state
    return ex

def run(eta, zeta, x, modified):
    ex = make_explainer(eta, zeta, modified)
    try: nodes, edges, seeds, amps, nref, bad = ex.explain(x)
    except AssertionError: return None
    kids = {}
    for e, k in edges.items():
        a, b = tuple(e)
        if k == "fork": continue
        upper = a if b in core.preds(a) else b; lower = b if upper == a else a
        kids.setdefault(lower, []).append(upper)
    dbl = [(u, ks) for u, ks in kids.items() if sum(1 for w in ks if w not in ex.amp and w not in ex.noise) >= 2]
    return dbl, ex._state["forced"], ex._state["avoided"], ex

x = (0, 0, 0); trees = 0; d0 = d1 = forced = avoided = 0; shown = 0
for trial in range(N):
    depth = 3 + trial % 6; dens = (10, 20, 35, 50)[trial % 4]
    sites = core.cone(x, depth); zeta = {z: 1 for z in sites if random.randrange(100) < dens}
    eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    r0 = run(eta, zeta, x, False); r1 = run(eta, zeta, x, True)
    if r0 is None or r1 is None: continue
    trees += 1; d0 += len(r0[0]); d1 += len(r1[0]); forced += r1[1]; avoided += r1[2]
    if r1[0] and shown < 3:
        shown += 1; ex = r1[3]
        for u, ks in r1[0]:
            procs = [w for w in ks if w not in ex.amp and w not in ex.noise]
            print(f"  modified rule still double at {u} (kind {'amp' if u in ex.amp else 'seed' if u in ex.noise else 'proc'}): processed children {procs}; their winning pairs {[ex.exc[w] for w in procs]}; zeta={sorted(zeta)}")
print(f"seed {sys.argv[2]}: {trees} trees; double-processed-child nodes: block 30's rule {d0}, modified rule {d1}; forced shared excuses {forced}; avoided by the modified rule {avoided}")
