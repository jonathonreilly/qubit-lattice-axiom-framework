"""Refuting pass, block 37: (a) the family constant at the witness by an integer program (machinery disjoint from the level-subset
dynamic program of the runner); (b) the rooted values of the three predecessors with the level cap; (c) a local search around the
witness for realizations with a larger constant.  usage: control_b37.py seconds seed"""
import sys, time, random
from itertools import product
from fractions import Fraction
sys.path.insert(0, ".")
import supervisor_control_block37_family as m
from supervisor_control_block37_mintree import MinTree
from supervisor_control_block37_rooted import rooted
M = [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,2,1),(1,0,2),(2,1,0),(1,1,3),(1,3,1),(3,1,1)]
def realize(marks, hi=5):
    sites = list(product(range(-1, hi + 1), repeat=3)); return m.run_automaton(sites, {z: 1 for z in marks})
eta = realize(M); root = (3, 3, 3)
cs, tree, r0 = MinTree(eta, root).cstar(); print(f"(a) integer program: c*(eta, 333) = {cs}; optimal tree E={tree['E']} A={tree['A']} S={tree['S']}")
for u in ((2,3,3),(3,2,3),(3,3,2)):
    v, info = rooted(eta, u, 1.0); print(f"(b) rooted value with the level cap, c = 1, at {u}: {v}  (E={info['E']} A={info['A']} S={info['S']})")
v, info = rooted(eta, root, 1.0); print(f"(b) rooted value at 333: {v}")
secs = float(sys.argv[1]); rng = random.Random(int(sys.argv[2])); t0 = time.time()
def best_constant(marks):
    e = realize(marks); ones, npred, kind = m.kinds(e); best = (Fraction(0), None)
    tops = sorted((z for z in ones if kind[z] == "proc"), key=m.level)[-3:]
    for z in tops:
        try: c, tr, _ = MinTree(e, z).cstar()
        except Exception: continue
        if c is not None and c > best[0]: best = (c, z)
    return best
cur = list(M); cur_val = best_constant(cur); top = cur_val; tried = 0
box = list(product(range(0, 5), repeat=3))
while time.time() - t0 < secs:
    cand = list(cur); move = rng.random()
    if move < 0.4 and len(cand) > 4: cand.pop(rng.randrange(len(cand)))
    elif move < 0.8: cand.append(rng.choice(box))
    else: cand[rng.randrange(len(cand))] = rng.choice(box)
    cand = sorted(set(cand)); val = best_constant(cand); tried += 1
    if val[0] >= cur_val[0]: cur, cur_val = cand, val
    if val[0] > top[0]: top = val; print(f"   new best {val[0]} = {float(val[0]):.4f} at {val[1]} with marks {cand}", flush=True)
print(f"(c) local search: {tried} realizations tried in {time.time()-t0:.0f}s; largest constant found {top[0]} at {top[1]}")
