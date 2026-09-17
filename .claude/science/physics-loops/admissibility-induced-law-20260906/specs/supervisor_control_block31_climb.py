"""hill-climb the ratio (E - 3(|S|-1))/|A| over noise sets zeta in a small window; random restarts."""
import sys, random
sys.path.insert(0, sys.argv[1]); seed = int(sys.argv[2]); secs = float(sys.argv[3])
from supervisor_control_block31_core import Explainer, level, preds, check_tree, run_automaton
from fractions import Fraction as F
import time
random.seed(seed)
A_, B_, L_ = 4, 4, 7
sites = [(a,b,c) for a in range(A_) for b in range(B_) for c in range(L_)]
def score(zeta):
    eta = run_automaton(sites, zeta)
    ones = [z for z, v in eta.items() if v == 1]
    if not ones or len(ones) > 60: return F(-10), None
    ex = Explainer(eta, zeta)
    best = (F(-10), None)
    for root in ones:
        try:
            nodes, edges, seeds, amps, nref, bad = ex.explain(root)
        except AssertionError:
            return F(-100), ("ASSERT", root)
        E = sum(1 for e, k in edges.items() if k == "arrow"); A = len(amps); Sn = len(seeds)
        if A == 0: continue
        r = F(E - 3*(Sn-1), A)
        if r > best[0]: best = (r, (root, E, A, Sn, nref, bad, sorted(zeta)))
    return best
t0 = time.time(); overall = (F(-10), None); restarts = 0
while time.time() - t0 < secs:
    zeta = {z: 1 for z in random.sample(sites, random.randint(2, 6))}
    cur = score(zeta); restarts += 1
    for it in range(400):
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
                print(f"seed {seed}: new best ratio {sc[0]} = {float(sc[0]):.3f}: root={sc[1][0]} E={sc[1][1]} |A|={sc[1][2]} |S|={sc[1][3]} refinements={sc[1][4]} bad={sc[1][5]} zeta={sc[1][6]}", flush=True)
print(f"seed {seed}: done, restarts={restarts}, best={overall[0]}")
