import sys, pickle, itertools
sys.argv=['x','full']
exec(open('eval_cliques.py').read().split("res = []")[0].replace("cl = pickle.load(open(f'cl3q_{ACTION}.pkl', 'rb'))", "cl = []"))
adj = d['adj']; out = pickle.load(open('outsiders.pkl','rb'))
nodes = set(out)
for k in out: nodes |= adj[k]
nodes = sorted(nodes); print('subgraph nodes', len(nodes), flush=True)
loc = {v:i for i,v in enumerate(nodes)}
sadj = {loc[v]: {loc[w] for w in adj[v] if w in loc} for v in nodes}
cls = c1.maximal_cliques(len(nodes), sadj)
cls = [sorted(nodes[i] for i in c) for c in cls]
cls = [c for c in cls if any(k in out for k in c)]
print('maximal cliques containing an outsider:', len(cls), 'sizes', sorted(len(c) for c in cls), flush=True)
for c in cls:
    gens = []
    for k in c:
        for code, sg in signed_orbit(reps[k]).items(): gens.append((code, sg))
    r4 = torus(gens, 4); r6 = torus(gens, 6) if r4 else None
    print(len(c), 'orbits', len(gens), 'gens/site | L4 (3L^3-rank, bad relations)', r4, '| L6', r6, flush=True)
pickle.dump(cls, open('outsider_cls.pkl','wb'))
