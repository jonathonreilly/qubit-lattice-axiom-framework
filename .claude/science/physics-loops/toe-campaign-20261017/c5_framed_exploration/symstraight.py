import sys, itertools, time
from collections import Counter
from legs import *
exec(open('symframed.py').read().split("def run(name, maxk):")[0].split("exec(open('framed.py')")[0] + "\n".join(open('symframed.py').read().split("def run(name, maxk):")[0].split("\n")[6:]))
def classify(S):
    if not commute([plaq(c, S) for c in range(3)]): return 'noncommuting'
    P = [as_vec(plaq(c, S)) for c in range(3)]; Av = as_vec(A)
    for a in range(3):
        u = as_vec(U((0,0,0), a, S))
        for c in range(3):
            for s in itertools.product(range(-3, 4), repeat=3):
                if anti(u, shift(P[c], s)): return 'U not pure hopping'
        hits = [s for s in itertools.product(range(-3, 4), repeat=3) if anti(u, shift(Av, s))]
        if sorted(hits) != sorted([(0,0,0), E[a]]): return 'U not pure hopping'
    signs = set()
    for trip in itertools.combinations(range(6), 3):
        L = [leg(S, d, 3)[0] for d in trip]
        signs.add((-1) ** (anti(L[0], L[1]) + anti(L[1], L[2]) + anti(L[0], L[2])))
    return 'fermion' if signs == {-1} else ('boson' if signs == {1} else 'mixed')
for name in sys.argv[2:]:
    H = SUB[name]; t0 = time.time(); cnt = Counter(); ex = {}
    for S in framings(H, int(sys.argv[1])):
        k = classify(S); cnt[k] += 1; ex.setdefault(k, S)
    print(name, len(H), dict(cnt), f'[{time.time()-t0:.0f}s]', '| fermion example:', ex.get('fermion'), '| mixed example:', ex.get('mixed'), flush=True)
