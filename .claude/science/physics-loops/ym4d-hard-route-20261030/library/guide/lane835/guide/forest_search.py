# GUIDE only: search periodic parent functions par: (Z/P)^4 -> {+-e_mu} such that every
# plaquette of Z^4 contains exactly one parent edge {y, y+par(y)}. Optional constraint:
# par(y) has time component <= 0 and paths strictly descend in time within bounded steps.
import itertools, sys
P = [int(c) for c in sys.argv[1].split(',')] if len(sys.argv) > 1 else [2,2,2,2]
D = 4
sites = list(itertools.product(*[range(p) for p in P]))
idx = {s:i for i,s in enumerate(sites)}
def add(s, mu, sgn):
    t = list(s); t[mu] = (t[mu] + sgn) % P[mu]; return tuple(t)
dirs = [(mu, sg) for mu in range(D) for sg in (1, -1)]
# edge {y, y+e_mu} is a parent edge iff par(y)=(mu,+1) or par(y+e_mu)=(mu,-1)
plaqs = []
for s in sites:
    for mu in range(D):
        for nu in range(mu+1, D):
            # edges as (base site, direction)
            plaqs.append([(s, mu), (add(s, nu, 1), mu), (s, nu), (add(s, mu, 1), nu)])
# each edge (y,mu) is "on" via var (idx y, (mu,+1)) or (idx y+e_mu, (mu,-1))
def edge_lits(e):
    y, mu = e
    return [(idx[y], (mu, 1)), (idx[add(y, mu, 1)], (mu, -1))]
plaq_lits = [[l for e in p for l in edge_lits(e)] for p in plaqs]
site_plaqs = [[] for _ in sites]
for k, lits in enumerate(plaq_lits):
    for (i, d) in lits:
        if k not in site_plaqs[i]: site_plaqs[i].append(k)
allowed = dirs if (len(sys.argv) < 3) else [d for d in dirs if not (d[0] == 0 and d[1] == 1)]
assign = [None]*len(sites)
order = list(range(len(sites)))
count = [0]
sols = []
def plaq_ok(k):
    on = 0; unknown = False
    for (i, d) in plaq_lits[k]:
        if assign[i] is None: unknown = True
        elif assign[i] == d: on += 1
    if on > 1: return False
    if not unknown and on != 1: return False
    return True
def no2cycle(i):
    d = assign[i]; y = sites[i]; j = idx[add(y, d[0], d[1])]
    return not (assign[j] is not None and assign[j] == (d[0], -d[1]))
def rec(n):
    if len(sols) >= 3: return
    if n == len(order):
        sols.append(list(assign)); return
    i = order[n]
    for d in allowed:
        assign[i] = d
        if no2cycle(i) and all(plaq_ok(k) for k in site_plaqs[i]):
            rec(n+1)
        assign[i] = None
rec(0)
print("period", P, "time-monotone" if len(sys.argv) >= 3 else "any", "solutions found:", len(sols))
for s in sols[:1]:
    for i, d in enumerate(s): print(sites[i], d)
