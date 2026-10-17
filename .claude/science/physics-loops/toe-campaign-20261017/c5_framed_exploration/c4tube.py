import sys, json, itertools
from tubestats import t_junction_tube
STAR = [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def dec(a): return [((int(a) >> (6*i)) & 63) for i in range(7)]
rules = json.load(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/toe-campaign-20261017/c4_fermion_search/unsoldered_bounded_rules.json'))
LEGSETS = [[(4,0,0),(0,4,0),(0,0,4)], [(-4,0,0),(0,-4,0),(0,0,-4)], [(4,0,0),(-4,0,0),(0,4,0)]]
for i, rule in enumerate(rules):
    codes = [c for orb in rule['strings'] for c in orb]
    gens = [{STAR[k]: tuple((l[k] >> (2*a)) & 3 for a in range(3)) for k in range(7) if l[k]} for l in map(dec, codes)]
    res = {}
    for r_ in range(1, len(gens) + 1):
        for sub in itertools.combinations(range(len(gens)), r_):
            pat = [((0,0,0), j) for j in sub]
            signs = [t_junction_tube(gens, 3, pat, legs, R=5)[0] for legs in LEGSETS]
            if all(s is not None for s in signs): res[sub] = signs
    print(i, rule['clique'], 'tube-mobile patterns:', len(res), 'signs:', sorted(set(s for v in res.values() for s in v)), flush=True)
