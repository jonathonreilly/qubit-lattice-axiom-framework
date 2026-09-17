"""hill-climb over noise sets to MAXIMIZE c*(config) = max over top roots of min_T (E - 3(|S|-1))/|A| (the family-level constant)."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from supervisor_control_block32_mintree import MinTree, run_automaton, level
from fractions import Fraction as Fr
seed = int(sys.argv[1]); secs = float(sys.argv[2]); A_, B_, L_ = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
random.seed(seed)
sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
def score(zeta):
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if not ones or len(ones) > 70: return Fr(-10), None
    roots = sorted(ones, key=level, reverse=True)[:3]
    best = (Fr(-10), None)
    for root in roots:
        if level(root) < 4: continue
        mt = MinTree(eta, root)
        cs, r, r0 = mt.cstar()
        if cs is None: continue
        if r0["E"] - 3 * (r0["S"] - 1) <= 0: cs = min(cs, Fr(0))     # a tree without amplification already fits block 25's budget
        if cs > best[0]: best = (cs, (root, r["E"], r["A"], r["S"], r["F"], len(ones)))
    return best
t0 = time.time(); overall = (Fr(-10), None); restarts = 0
W1 = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 2), (1, 2, 0), (1, 3, 1), (2, 0, 0), (2, 2, 3), (2, 3, 4), (3, 0, 2)]
while time.time() - t0 < secs:
    if restarts == 0 and seed % 2 == 1 and A_ >= 4 and L_ >= 7:
        zeta = {z: 1 for z in W1}
    else:
        zeta = {z: 1 for z in random.sample(sites, random.randint(2, 7))}
    cur = score(zeta); restarts += 1
    for it in range(300):
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
                print(f"seed {seed} {A_}x{B_}x{L_}: c* {sc[0]} = {float(sc[0]):.3f}: root={sc[1][0]} minimal tree (E,|A|,|S|,F)=({sc[1][1]},{sc[1][2]},{sc[1][3]},{sc[1][4]}) ones={sc[1][5]} zeta={sorted(zeta)}", flush=True)
print(f"seed {seed}: done restarts={restarts} best={overall[0]}")
