"""perturbation climb on c* from a given starting noise set (argv: seed secs A B L 'zeta-literal' root-literal); moves: toggle 1-2 sites."""
import sys, os, random, time, ast
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from supervisor_control_block32_mintree import MinTree, run_automaton, level
from fractions import Fraction as Fr
seed = int(sys.argv[1]); secs = float(sys.argv[2]); A_, B_, L_ = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
zeta0 = ast.literal_eval(sys.argv[6]); root0 = ast.literal_eval(sys.argv[7])
random.seed(seed)
sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
def score(zeta):
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if not ones or len(ones) > 90: return Fr(-10), None
    roots = sorted(ones, key=level, reverse=True)[:4]
    best = (Fr(-10), None)
    for root in roots:
        if level(root) < 4: continue
        mt = MinTree(eta, root); cs, r, r0 = mt.cstar()
        if cs is None: continue
        if r0["E"] - 3 * (r0["S"] - 1) <= 0: cs = min(cs, Fr(0))
        if cs > best[0]: best = (cs, (root, r["E"], r["A"], r["S"], r["F"], len(ones)))
    return best
t0 = time.time(); zeta = {z: 1 for z in zeta0}; cur = score(zeta); overall = cur
print(f"seed {seed} {A_}x{B_}x{L_}: start c* {cur[0]}", flush=True)
while time.time() - t0 < secs:
    new = dict(zeta)
    for _ in range(random.choice((1, 1, 2))):
        z = random.choice(sites)
        if z in new: del new[z]
        else: new[z] = 1
    if not new: continue
    sc = score(new)
    if sc[0] >= cur[0]:
        zeta, cur = new, sc
        if sc[0] > overall[0]:
            overall = sc
            print(f"seed {seed} {A_}x{B_}x{L_}: c* {sc[0]} = {float(sc[0]):.3f}: root={sc[1][0]} minimal tree (E,|A|,|S|,F)=({sc[1][1]},{sc[1][2]},{sc[1][3]},{sc[1][4]}) ones={sc[1][5]} zeta={sorted(zeta)}", flush=True)
    elif random.random() < 0.02:   # occasional downhill step to escape plateaus
        zeta, cur = new, sc
print(f"seed {seed}: done best={overall[0]}")
