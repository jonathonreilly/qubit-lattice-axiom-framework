"""structural search for tight sibling predecessors / rooted violations: moves = single toggles, and 'duplication' moves that copy a
random sub-block of marks translated by a sibling offset (e_i - e_j) or a predecessor offset, so that a break-even support is placed
next to itself. Objective: (number of processed sites with all 1-predecessors tight, max rooted value over processed sites,
number of tight sites)."""
import sys, os, os, random, time, ast
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rooted import rooted, m, run_automaton, level, preds
seed = int(sys.argv[1]); secs = float(sys.argv[2]); A_, B_, L_ = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); start = sys.argv[6]
random.seed(seed); sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
OFFS = [(1, -1, 0), (-1, 1, 0), (1, 0, -1), (-1, 0, 1), (0, 1, -1), (0, -1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
def score(zeta):
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 6 or len(ones) > 110: return (-99, -99, -99), None
    _, npred, kind = m.kinds(eta); vc = {}
    def v(z):
        if z not in vc: vc[z] = rooted(eta, z)[0]
        return vc[z]
    hard = 0; vmax = -99; tight = 0; detail = None
    for z in ones:
        if kind[z] != "proc": continue
        vz = v(z)
        if vz == 0: tight += 1
        vmax = max(vmax, vz)
        ps = npred[z]
        if all(kind[u] == "proc" and v(u) == 0 for u in ps):
            hard += 1; detail = (z, [(u, v(u)) for u in ps], vz)
    return (hard, vmax, tight), detail
Z = {"A": m.Z_A, "B": m.Z_B}[start]
zeta = {z: 1 for z in Z[2]}; t0 = time.time(); cur = score(zeta); overall = cur
print(f"seed {seed} {A_}x{B_}x{L_} from Z_{start}: start {cur[0]}", flush=True)
while time.time() - t0 < secs:
    new = dict(zeta); r = random.random()
    if r < 0.5:
        for _ in range(random.choice((1, 1, 2))):
            z = random.choice(sites)
            if z in new: del new[z]
            else: new[z] = 1
    else:   # duplication: copy the marks in a random level band translated by a random offset
        off = random.choice(OFFS); lo = random.randint(0, L_ + A_ + B_ - 3); hi = lo + random.randint(1, 4)
        for z in list(zeta):
            if lo <= level(z) <= hi:
                w = (z[0] + off[0], z[1] + off[1], z[2] + off[2])
                if 0 <= w[0] < A_ and 0 <= w[1] < B_ and 0 <= w[2] < L_: new[w] = 1
    if not new: continue
    sc = score(new)
    if sc[0] >= cur[0]:
        zeta, cur = new, sc
        if sc[0] > overall[0]:
            overall = sc
            print(f"seed {seed}: (hard, vmax, tight) = {sc[0]}; detail {sc[1]}; zeta={sorted(zeta)}", flush=True)
    elif random.random() < 0.03:
        zeta, cur = new, sc
print(f"seed {seed}: done best={overall[0]}")
