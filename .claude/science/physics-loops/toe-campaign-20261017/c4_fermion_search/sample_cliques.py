"""Random greedy maximal commuting orbit sets (soldered, extended class); evaluate validity and code dims."""
import sys, pickle, itertools, time, random
import numpy as np
sys.argv = [sys.argv[0], 'full'] + sys.argv[1:]
NS = int(sys.argv[2]); SEED = int(sys.argv[3])
exec(open('eval_cliques.py').read().split("res = []")[0].replace("cl = pickle.load(open(f'cl3q_{ACTION}.pkl', 'rb'))", "cl = []"))
adj = d['adj']; n = len(reps)
rng = random.Random(SEED)
seen = set(); found = []
t0 = time.time()
for it in range(NS):
    order = list(range(n)); rng.shuffle(order)
    C = []; cand = set(range(n))
    for v in order:
        if v in cand:
            C.append(v); cand &= adj[v]
    key = frozenset(C)
    if key in seen: continue
    seen.add(key)
    gens = []
    for k in C:
        for code, sg in signed_orbit(reps[k]).items(): gens.append((code, sg))
    if len(gens) > 400: print(it, len(C), 'gens', len(gens), 'skipped (large)', flush=True); continue
    r4 = torus(gens, 4)
    r6 = torus(gens, 6) if r4 and r4[1] == 0 and 0 < r4[0] <= 64 else None
    print(it, len(C), 'gens/site', len(gens), 'L4', r4, 'L6', r6, f'{time.time()-t0:.0f}s', flush=True)
    if r6 and r6[1] == 0 and r6[0] == r4[0]: found.append(sorted(C))
pickle.dump(found, open(f'sample_found_{SEED}.pkl', 'wb'))
print('bounded nonzero candidates:', len(found))
