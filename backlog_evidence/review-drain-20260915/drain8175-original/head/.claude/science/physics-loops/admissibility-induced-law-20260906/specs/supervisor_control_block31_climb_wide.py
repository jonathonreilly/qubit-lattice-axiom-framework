import sys, random, time
sys.path.insert(0, sys.argv[1]); seed = int(sys.argv[2]); secs = float(sys.argv[3]); A_, B_, L_ = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
from supervisor_control_block31_core import Explainer, level, preds, check_tree, run_automaton
from fractions import Fraction as F
random.seed(seed)
sites = [(a,b,c) for a in range(A_) for b in range(B_) for c in range(L_)]
def score(zeta):
    eta = run_automaton(sites, zeta)
    ones = [z for z, v in eta.items() if v == 1]
    if not ones or len(ones) > 110: return F(-10), None
    ex = Explainer(eta, zeta)
    best = (F(-10), None)
    for root in ones:
        if level(root) < L_ // 2: continue
        try: nodes, edges, seeds, amps, nref, bad = ex.explain(root)
        except AssertionError: return F(-100), ("ASSERT", root)
        E = sum(1 for e, k in edges.items() if k == "arrow"); A = len(amps); Sn = len(seeds)
        if A == 0: continue
        r = F(E - 3*(Sn-1), A)
        if r > best[0]: best = (r, (root, E, A, Sn, nref, bad, sorted(zeta)))
    return best
t0 = time.time(); overall = (F(-10), None)
while time.time() - t0 < secs:
    zeta = {z: 1 for z in random.sample(sites, random.randint(3, 8))}
    cur = score(zeta)
    for it in range(600):
        if time.time() - t0 > secs: break
        z = random.choice(sites); new = dict(zeta)
        if z in new: del new[z]
        else: new[z] = 1
        if not new: continue
        sc = score(new)
        if sc[0] >= cur[0]:
            zeta, cur = new, sc
            if sc[0] > overall[0]:
                overall = sc
                print(f"seed {seed} window {A_}x{B_}x{L_}: ratio {sc[0]} = {float(sc[0]):.3f}: root={sc[1][0]} E={sc[1][1]} |A|={sc[1][2]} |S|={sc[1][3]} refinements={sc[1][4]} bad={sc[1][5]} zeta={sc[1][6]}", flush=True)
print(f"seed {seed}: done best={overall[0]}")
