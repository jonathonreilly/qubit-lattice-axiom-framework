"""seeded climb: maximize over processed 1-sites z the minimum cost at c = 1 over trees containing z — unrooted (the family; > 0 means c* > 1)
and rooted (> 0 refutes the induction hypothesis H3)."""
import sys, os, os, random, time, ast
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
from supervisor_control_block33_tight import rooted, m, run_automaton, level, preds
from supervisor_control_block33_mintree import MinTree
seed = int(sys.argv[2]); secs = float(sys.argv[3]); A_, B_, L_ = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]); start = sys.argv[7]
random.seed(seed); sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
def score(zeta):
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 6 or len(ones) > 80: return (-99, -99), None
    _, npred, kind = m.kinds(eta)
    best = ((-99, -99), None)
    for z in ones:
        if kind[z] != "proc" or level(z) < 3: continue
        mt = MinTree(eta, z); r = mt.solve(1.0)
        if r is None: continue
        un = r["E"] - 3 * (r["S"] - 1) - r["A"]
        ro = rooted(eta, z)[0]
        key = (un, ro)
        if key > best[0]: best = (key, (z, un, ro, (r["E"], r["A"], r["S"], r["F"])))
    return best
Z = {"A": m.Z_A, "B": m.Z_B}[start]
zeta = {z: 1 for z in Z[2]}
t0 = time.time(); cur = score(zeta); overall = cur
print(f"seed {seed} {A_}x{B_}x{L_} from Z_{start}: start (unrooted, rooted) max cost = {cur[0]} at {cur[1]}", flush=True)
while time.time() - t0 < secs:
    new = dict(zeta)
    for _ in range(random.choice((1, 1, 2, 3))):
        z = random.choice(sites)
        if z in new: del new[z]
        else: new[z] = 1
    if not new: continue
    sc = score(new)
    if sc[0] >= cur[0]:
        zeta, cur = new, sc
        if sc[0] > overall[0]:
            overall = sc
            print(f"seed {seed}: (unrooted, rooted) max cost = {sc[0]} at {sc[1]}; ones? zeta={sorted(zeta)}", flush=True)
    elif random.random() < 0.03:
        zeta, cur = new, sc
print(f"seed {seed}: done best={overall[0]}")
