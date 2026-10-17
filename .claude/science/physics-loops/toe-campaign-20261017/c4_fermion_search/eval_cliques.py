"""For each maximal clique (3 axis qubits, ACTION): signed generators, torus L validity (no -1/±i), log2 dim."""
import sys, pickle, itertools, time
import numpy as np
sys.argv = [sys.argv[0]] + sys.argv[1:]
ACTION = sys.argv[1]; MAXSIZE = int(sys.argv[2]) if len(sys.argv) > 2 else 400
exec(open('analyze3q.py').read().split("d = pickle.load(open(f'surv3q_{ACTION}.pkl', 'rb'))")[0])
d = pickle.load(open(f'orb3q_{ACTION}.pkl', 'rb')); cl = pickle.load(open(f'cl3q_{ACTION}.pkl', 'rb'))
reps, elems = d['reps'], d['elems']
def dec(a): return [((int(a) >> (6*i)) & 63) for i in range(7)]
def signed_orbit(rep):
    out = {}
    for k in range(24):
        t, g = transform(np.array([rep], np.uint64), k); out[int(t[0])] = int(g[0])
    return out
MUL = {(1,2):(3,1),(2,1):(3,3),(2,3):(1,1),(3,2):(1,3),(3,1):(2,1),(1,3):(2,3)}
def torus(gens, L):
    n = 3 * L**3; idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    rows, ops = [], []
    for v in itertools.product(range(L), repeat=3):
        for code, sg in gens:
            x = np.zeros(2*n, np.uint8); op = {}
            for i, l in enumerate(dec(code)):
                if not l: continue
                p = [v[j] + STAR[i][j] for j in range(3)]
                for a in range(3):
                    lab = (l >> (2*a)) & 3
                    if not lab: continue
                    q = idx(p, a)
                    if q in op: return None   # torus too small (self-overlap)
                    op[q] = lab
                    if lab in (1, 2): x[q] ^= 1
                    if lab in (2, 3): x[n + q] ^= 1
            rows.append(x); ops.append((op, sg))
    r, N = c1.f2_rank_and_null(np.array(rows))
    bad = 0
    for c in N:
        cur, ph = {}, 0
        for k in np.nonzero(c)[0]:
            op, sg = ops[k]
            if sg < 0: ph += 2
            for q, P in op.items():
                Q = cur.get(q)
                if Q is None: cur[q] = P
                elif Q == P: del cur[q]
                else: cur[q], e = MUL[(Q, P)]; ph += e
        if cur or ph % 4: bad += 1
    return n - r, bad
res = []
order = sorted(range(len(cl)), key=lambda i: len(cl[i]))
for ci in order:
    c = cl[ci]
    if len(c) > MAXSIZE: continue
    gens = []
    for k in c:
        for code, sg in signed_orbit(reps[k]).items(): gens.append((code, sg))
    t0 = time.time()
    r4 = torus(gens, 4); r6 = torus(gens, 6) if r4 and r4[1] == 0 and r4[0] <= 64 else None
    print(ci, len(c), 'gens/site', len(gens), 'L4 (log2dim, bad relations):', r4, 'L6:', r6, f'{time.time()-t0:.1f}s', flush=True)
    res.append((ci, len(c), r4, r6))
pickle.dump(res, open(f'evalcl_{ACTION}.pkl', 'wb'))
