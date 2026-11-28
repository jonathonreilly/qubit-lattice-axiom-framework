# GUIDE only. Periodic parent functions with exactly one parent edge per plaquette,
# par in {-e_0} U {+-e_i, i=1..3}, and every parent path reaching a -e_0 site (descends in time).
import itertools, sys
P = [int(c) for c in sys.argv[1].split(',')]
D = 4
sites = list(itertools.product(*[range(p) for p in P])); idx = {s:i for i,s in enumerate(sites)}
def add(s, mu, sg):
    t = list(s); t[mu] = (t[mu] + sg) % P[mu]; return tuple(t)
dirs = [(0, -1)] + [(mu, sg) for mu in (1,2,3) for sg in (1,-1)]
plaq_lits = []
for s in sites:
    for mu in range(D):
        for nu in range(mu+1, D):
            es = [(s, mu), (add(s, nu, 1), mu), (s, nu), (add(s, mu, 1), nu)]
            plaq_lits.append([(idx[y], (m, 1)) for (y, m) in es] + [(idx[add(y, m, 1)], (m, -1)) for (y, m) in es])
site_plaqs = [sorted({k for k, L in enumerate(plaq_lits) for (i, d) in L if i == j}) for j in range(len(sites))]
assign = [None]*len(sites); sols = []
def ok(k):
    on = 0; unk = False
    for (i, d) in plaq_lits[k]:
        if assign[i] is None: unk = True
        elif assign[i] == d: on += 1
    return on <= 1 and (unk or on == 1)
def descends():
    for j in range(len(sites)):
        seen = set(); c = j
        while assign[c] != (0, -1):
            if c in seen: return False
            seen.add(c); d = assign[c]; c = idx[add(sites[c], d[0], d[1])]
    return True
def rec(n):
    if len(sols) >= 1: return
    if n == len(sites):
        if descends(): sols.append(list(assign))
        return
    for d in dirs:
        assign[n] = d
        y = sites[n]; j = idx[add(y, d[0], d[1])]
        if not (assign[j] == (d[0], -d[1])) and all(ok(k) for k in site_plaqs[n]):
            rec(n+1)
        assign[n] = None
rec(0)
print("period", P, "descending one-per-plaquette solutions:", len(sols))
for s in sols[:1]:
    print([ (sites[i], d) for i, d in enumerate(s)])
