"""Chunked search of C2-fixed star strings (axis C2 about z, or edge C2 about (1,1,0)) for three
axis qubits per site, ACTION labels; keep strings commuting with all translates of all rotated images."""
import itertools, sys, time, pickle
import numpy as np
sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('e3', 'enum3q.py')
ACTION, WHICH = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], ACTION]
src = open('enum3q.py').read().split('surv = []')[0]     # reuse tables and helpers only
exec(src)
k = find(np.diag([-1, -1, 1])) if WHICH == 'axis' else find(np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]))
g = POS[k]; orbits, seen = [], set()
for i in range(7):
    if i in seen: continue
    orb, j = [i], g[i]
    while j != i: orb.append(j); j = g[j]
    seen |= set(orb); orbits.append(orb)
def gpow(lbl, steps):
    for _ in range(steps): lbl = int(SITE[k][lbl])
    return lbl
opts = [np.array([l for l in range(64) if gpow(l, len(orb)) == l], np.uint64) for orb in orbits]
sizes = [o.size for o in opts]; N = int(np.prod(sizes)); log(f'{WHICH} C2: orbits {orbits}, options {sizes}, total {N}')
CH = 1 << 22; surv = []
for start in range(0, N, CH):
    idx = np.arange(start, min(N, start + CH), dtype=np.int64)
    out = np.zeros(idx.size, np.uint64); rem = idx.copy()
    for orb, o in zip(orbits, opts):
        d = rem % o.size; rem //= o.size
        cur = o[d]
        for i in orb:
            out |= cur << np.uint64(6 * i); cur = SITE[k][cur.astype(np.int64)]
    a = out[out != 0]
    a = a[commutes_all(a, a)]
    for kk in range(1, 24):
        if a.size == 0: break
        a = a[commutes_all(a, transform(a, kk))]
    surv.append(a)
    if (start // CH) % 32 == 0: log(f'chunk {start // CH}/{N // CH + 1}: survivors {sum(x.size for x in surv)}')
S = np.unique(np.concatenate(surv)); log('survivors', S.size)
pickle.dump(S, open(f'surv3q_c2{WHICH}_{ACTION}.pkl', 'wb'))
