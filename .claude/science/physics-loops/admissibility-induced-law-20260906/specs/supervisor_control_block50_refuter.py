"""Block 50 refuting pass (supervisor-run; machinery disjoint from the runner: forward flux accounting over the FULL sectors, symbolic weights,
and a continuous-time simulation; the runner uses the predecessor map on configurations with one record at the origin).
W1  two-record sector, all 12636 configurations: push the flux pi(C) rate(C -> C') forward along every event; inflow equals outflow everywhere
    for the global and for the local clock; every configuration has as many events in as out.
W2  three-record sector, all 631800 configurations: the same; global clock balanced everywhere; local clock violated at 9 x 3168 configurations
    (the runner fixes one record at the origin, which counts every configuration three times among 27 translates), largest defect 3.
W3  symbolic weights (p, q, r, c): the local-clock defect of the witness configuration is (c r - 1) + (c p - 1); it is zero for sampled
    two-record configurations identically in the weights.
W4  continuous-time simulation of two records with local clocks (floating point): time spent in adjacent configurations of equal, opposite and
    orthogonal contents, per REACHABLE configuration, over the time spent per non-adjacent configuration: 3, 1, 2 within sampling error.
    Without re-drawing, two records on a common line whose contents lie along it never leave it: those configurations form closed classes and
    are not reached from a generic start (2 of the 6 equal and 2 of the 6 opposite content pairs on each bond).
W5  the neutral scale: c_0 r = 1 exactly when p + q = 2 r (so orthogonal pairs are neutral at (3, 1, 2)), symbolically."""
import random
import sys
from itertools import combinations, product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[5]
E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SITES = list(product(range(3), repeat=3))
IDX = {x: i for i, x in enumerate(SITES)}
NB = [[IDX[tuple((x[i] + d[i]) % 3 for i in range(3))] for d in E] for x in SITES]
ADJ = [[False] * 27 for _ in range(27)]
for a in range(27):
    for b in NB[a]:
        ADJ[a][b] = True
results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def om(a, b, w):
    return w[0] if a == b else (w[1] if a == (b ^ 1) else w[2])


def total_weight(pos, con, w):
    val = 1
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            if ADJ[pos[i]][pos[j]]:
                val = val * om(con[i], con[j], w)
    return val


def own_weight(pos, con, k, w):
    val = 1
    for j in range(len(pos)):
        if j != k and ADJ[pos[k]][pos[j]]:
            val = val * om(con[k], con[j], w)
    return val


def event(pos, con, k):
    """The event of record k: returns the successor as (positions, contents), both sorted by position."""
    target = NB[pos[k]][con[k]]
    pos2, con2 = list(pos), list(con)
    if target in pos:
        j = pos.index(target)
        con2[k], con2[j] = con[j], con[k]
    else:
        pos2[k] = target
    order = sorted(range(len(pos2)), key=lambda i: pos2[i])
    return tuple(pos2[i] for i in order), tuple(con2[i] for i in order)


def balance(nrec, w, clock):
    inflow, outflow, indeg = {}, {}, {}
    for pos in combinations(range(27), nrec):
        for con in product(range(6), repeat=nrec):
            pi = total_weight(pos, con, w)
            c_key = (pos, con)
            for k in range(nrec):
                flux = 1 if clock == "global" else pi // own_weight(pos, con, k, w)       # pi_x divides pi: the flux pi/pi_x is the weight of the pairs that do not touch x
                nxt = event(pos, con, k)
                inflow[nxt] = inflow.get(nxt, 0) + flux
                indeg[nxt] = indeg.get(nxt, 0) + 1
                outflow[c_key] = outflow.get(c_key, 0) + flux
    bad = [c for c in outflow if inflow.get(c, 0) != outflow[c]]
    deg_ok = all(indeg.get(c, 0) == nrec for c in outflow)
    largest = max((abs(outflow[c] - inflow.get(c, 0)) for c in bad), default=0)
    return len(outflow), len(bad), largest, deg_ok


W = (3, 1, 2)
n, bad_g, _, deg = balance(2, W, "global")
_, bad_l, _, _ = balance(2, W, "local")
report("W1", n == 12636 and bad_g == 0 and bad_l == 0 and deg, f"two records, all {n} configurations, forward flux accounting: global clock violated at {bad_g}, local clock at {bad_l}; every configuration has two events in and two out")
n, bad_g, _, deg = balance(3, W, "global")
_, bad_l, largest, _ = balance(3, W, "local")
report("W2", n == 631800 and bad_g == 0 and bad_l == 9 * 3168 and largest == 3 and deg, f"three records, all {n} configurations: global clock violated at {bad_g}; local clock at {bad_l} = 9 x 3168 (the runner's 3168 are configurations with a record at the origin: each configuration has three such translates, and 27 translates in all), largest defect {largest}; three events in and three out everywhere")

# ------------------------------------------------------------------------------------------------ W3
p, q, r, c = sp.symbols("p q r c", positive=True)
WS = (c * p, c * q, c * r)


def sym_defect(posl, conl):
    nrec = len(posl)
    pi = sp.Integer(1) * total_weight(posl, conl, WS)                    # sympy numbers throughout: an int over an int would be a float
    out = sum(pi / own_weight(posl, conl, k, WS) for k in range(nrec))
    inn = 0
    for k in range(nrec):                                               # predecessor of record k
        behind = NB[posl[k]][conl[k] ^ 1]
        pos2, con2 = list(posl), list(conl)
        if behind in posl:
            j = posl.index(behind)
            con2[j], con2[k] = conl[k], conl[j]
            act = j
        else:
            pos2[k] = behind
            act = k
        inn += sp.Integer(1) * total_weight(pos2, con2, WS) / own_weight(pos2, con2, act, WS)
    return sp.simplify(out - inn)


witness = sym_defect([IDX[(0, 0, 0)], IDX[(0, 0, 1)], IDX[(0, 1, 0)]], [2, 4, 2])
rng = random.Random(50)
two_ok = True
for _ in range(60):
    a, b = rng.sample(range(27), 2)
    two_ok = two_ok and sym_defect([a, b], [rng.randrange(6), rng.randrange(6)]) == 0
report("W3", sp.simplify(witness - ((c * r - 1) + (c * p - 1))) == 0 and two_ok, f"symbolic weights: the local-clock defect of the witness configuration is {witness}; sixty sampled two-record configurations have defect zero identically in p, q, r, c")

# ------------------------------------------------------------------------------------------------ W4
rng = random.Random(4)
pos, con = [0, 13], [rng.randrange(6), rng.randrange(6)]
time_in = {"equal": 0.0, "opposite": 0.0, "orthogonal": 0.0, "far": 0.0}
t_total = 0.0
for step in range(600000):
    adjacent = ADJ[pos[0]][pos[1]]
    wpair = om(con[0], con[1], W) if adjacent else 1
    rate = 2.0 / wpair                                                  # each of the two records runs at 1/pi_x, and pi_x = wpair for both
    dt = rng.expovariate(rate)
    kind = "far" if not adjacent else ("equal" if con[0] == con[1] else ("opposite" if con[0] == (con[1] ^ 1) else "orthogonal"))
    time_in[kind] += dt
    t_total += dt
    k = rng.randrange(2)
    target = NB[pos[k]][con[k]]
    if target == pos[1 - k]:
        con[0], con[1] = con[1], con[0]
    else:
        pos[k] = target
    if step % 7 == 0:                                                   # uniform re-draw of both contents now and then, so that every content class is visited
        if not ADJ[pos[0]][pos[1]]:
            con = [rng.randrange(6), rng.randrange(6)]
# numbers of configurations per kind (ordered pairs of sites): adjacent site pairs 27 x 6, non-adjacent 27 x 20; contents 6 equal, 6 opposite, 24 orthogonal, 36 any
per_conf = {"equal": time_in["equal"] / (162 * 4), "opposite": time_in["opposite"] / (162 * 4), "orthogonal": time_in["orthogonal"] / (162 * 24), "far": time_in["far"] / (540 * 36)}
ratios = {k: per_conf[k] / per_conf["far"] for k in ("equal", "opposite", "orthogonal")}
ok = abs(ratios["equal"] - 3) < 0.15 and abs(ratios["opposite"] - 1) < 0.08 and abs(ratios["orthogonal"] - 2) < 0.1
report("W4", ok, f"simulation of two records with local clocks (600000 events): time per reachable configuration (contents not both along the bond) over the non-adjacent value: equal {ratios['equal']:.3f}, opposite {ratios['opposite']:.3f}, orthogonal {ratios['orthogonal']:.3f} (the rule's 3, 1, 2)")

# ------------------------------------------------------------------------------------------------ W5
c0 = 6 / (p + q + 4 * r)
report("W5", sp.simplify((c0 * r - 1).subs(q, 2 * r - p)) == 0 and sp.simplify((c0 * p + c0 * q + 4 * c0 * r) / 6 - 1) == 0, "symbolic: the mean pair weight at c_0 = 6/(p + q + 4r) is one; c_0 r = 1 exactly when p + q = 2r, so at (3, 1, 2) orthogonal pairs are neutral at the neutral scale")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
