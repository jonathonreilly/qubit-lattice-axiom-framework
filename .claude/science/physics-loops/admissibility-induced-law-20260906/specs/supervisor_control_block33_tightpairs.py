"""climb to find TIGHT SIBLING PAIRS: a processed z with two processed 1-preds w1, w2 both with rooted value 0.
objective = max over processed z with >= 2 processed 1-preds of min(v(w1), v(w2)) over pairs (values <= 0; 0 means tight-tight).
also records max over processed z of v(z) (H3 violations would be > 0)."""
import sys, os, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
from supervisor_control_block33_tight import rooted, m, run_automaton, level, preds
from itertools import combinations
seed = int(sys.argv[2]); secs = float(sys.argv[3]); A_, B_, L_ = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
random.seed(seed); sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
def score(zeta):
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 6 or len(ones) > 60: return -99, None
    _, npred, kind = m.kinds(eta); vc = {}
    def v(z):
        if z not in vc: vc[z] = rooted(eta, z)[0]
        return vc[z]
    best = (-99, None); hviol = None
    for z in ones:
        if kind[z] != "proc": continue
        pw = [u for u in npred[z] if kind[u] == "proc"]
        if len(pw) >= 2:
            for w1, w2 in combinations(pw, 2):
                val = min(v(w1), v(w2))
                if val > best[0]: best = (val, (z, w1, v(w1), w2, v(w2), v(z)))
        vz = v(z)
        if vz > 0: hviol = (z, vz)
    return best[0], (best[1], hviol, len(ones))
t0 = time.time(); overall = (-99, None); restarts = 0
while time.time() - t0 < secs:
    zeta = {z: 1 for z in random.sample(sites, random.randint(2, 8))}; cur = score(zeta); restarts += 1
    for it in range(250):
        if time.time() - t0 > secs: break
        z = random.choice(sites); new = dict(zeta)
        if z in new: del new[z]
        else: new[z] = 1
        if not new: continue
        sc = score(new)
        if sc[0] >= cur[0]:
            zeta, cur = new, sc
            if sc[0] > overall[0] or (sc[1] and sc[1][1]):
                overall = sc
                print(f"seed {seed}: max over sibling processed pred pairs of min(v) = {sc[0]}: detail {sc[1][0]}; H3 violation: {sc[1][1]}; ones={sc[1][2]}; zeta={sorted(zeta)}", flush=True)
print(f"seed {seed}: done restarts={restarts} best={overall[0]}")
