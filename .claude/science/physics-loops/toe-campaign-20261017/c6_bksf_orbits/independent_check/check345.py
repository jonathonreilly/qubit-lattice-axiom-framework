"""Claims (3), (4), (5)."""
import time, random, pickle
from collections import Counter, defaultdict
from core import *

t0 = time.time()
lat = Lattice(4)
key_of = {}
canon = {}
for order in ORDERS:
    Bs, Ss = lat.gens(rank_of_order(order))
    k = rref(Bs + Ss)
    key_of[order] = k
classes = defaultdict(list)
for o, k in key_of.items():
    classes[k].append(o)
print('L=4 distinct stabilizer groups:', len(classes), 'class sizes', Counter(len(v) for v in classes.values()), f'{time.time()-t0:.1f}s')
cls_id = {k: i for i, k in enumerate(classes)}
code_of = {o: cls_id[k] for o, k in key_of.items()}

# L=6 sample: the partition must agree on random pairs + one full class
t0 = time.time()
lat6 = Lattice(6)
random.seed(1)
sample = random.sample(ORDERS, 40)
k6 = {}
for o in sample:
    Bs, Ss = lat6.gens(rank_of_order(o))
    k6[o] = rref(Bs + Ss)
agree = all((k6[a] == k6[b]) == (code_of[a] == code_of[b]) for a in sample for b in sample)
# also: all 12 members of one class equal at L=6, and reps of distinct classes distinct
c0 = list(classes.values())[0]
k6c = {rref(sum(lat6.gens(rank_of_order(o)), [])) for o in c0}
print('L=6 sample partition agrees with L=4:', agree, '; one L=4 class gives', len(k6c), 'L=6 group(s);',
      'distinct L=6 groups in sample', len(set(k6.values())), 'vs L=4', len({code_of[o] for o in sample}), f'{time.time()-t0:.1f}s')

# Claim 4: rotation action. Verify R(code(sigma)) == code(R sigma) by explicit qubit permutation for all 60 reps x 24 rotations
t0 = time.time()
reps = {cid: classes[k][0] for k, cid in cls_id.items()}
perms = [qubit_perm(lat, M) for M in ROTS]
mismatch = 0
act = {}
for cid, o in reps.items():
    basis = list(key_of[o])
    for ri, M in enumerate(ROTS):
        img = rref([apply_perm(lat, p, perms[ri]) for p in basis])
        if img not in cls_id:
            mismatch += 1; continue
        act[(ri, cid)] = cls_id[img]
        if cls_id[img] != code_of[rot_order(M, o)]:
            mismatch += 1
print('rotation action: explicit-permutation vs rotated-ordering mismatches:', mismatch, f'{time.time()-t0:.1f}s')
# also check rotated ordering consistent for ALL 720 orders (well-defined on classes)
wd = all(code_of[rot_order(M, o)] == act[(ri, code_of[o])] for o in ORDERS for ri, M in enumerate(ROTS))
print('action well-defined on all 720 orders:', wd)

seen = set(); orbits = []
for c in range(60):
    if c in seen: continue
    orb = {act[(ri, c)] for ri in range(24)}
    seen |= orb; orbits.append(sorted(orb))
print('orbit sizes:', sorted(Counter(len(o) for o in orbits).items()), '-> codes per size', {s: s * m for s, m in Counter(len(o) for o in orbits).items()})
inv = [c for c in range(60) if all(act[(ri, c)] == c for ri in range(24))]
print('O-invariant codes:', inv)


def classify(M):
    tr = int(np.trace(M))
    if tr == 3: return 'id'
    w, V = np.linalg.eig(M.astype(float))
    ax = np.real(V[:, np.argmin(abs(w - 1))]); ax = ax / np.max(abs(ax))
    ax = tuple(int(round(x)) for x in ax)
    nz = sum(1 for x in ax if x)
    kind = {1: 'face-axis', 2: 'face-diag(edge)-axis', 3: 'body-diag'}[nz]
    order = {0: 3, -1: 2, 1: 4}[tr]
    return f'C{order}/{kind}{ax}'

stabs = Counter()
for c in range(60):
    st = [ri for ri in range(24) if act[(ri, c)] == c]
    stabs[len(st)] += 1
    if len(st) == 6 and c == [x for x in range(60) if sum(act[(r, x)] == x for r in range(24)) == 6][0]:
        print('example order-6 stabilizer elements:', [classify(ROTS[ri]) for ri in st])
print('stabilizer orders histogram:', dict(stabs))
# check every order-6 stabilizer is D3 of the stated type; and describe order-2/order-4 stabilizers
types = Counter()
for c in range(60):
    st = [ri for ri in range(24) if act[(ri, c)] == c]
    sig = tuple(sorted(Counter(classify(ROTS[ri]).split('(')[0] for ri in st).items()))
    types[(len(st), sig)] += 1
for k, v in types.items():
    print('stab order', k[0], 'element types', k[1], 'count', v)
# D3 non-abelian check
for c in range(60):
    st = [ROTS[ri] for ri in range(24) if act[(ri, c)] == c]
    if len(st) == 6:
        nonab = any(not np.array_equal(a @ b, b @ a) for a in st for b in st)
        assert nonab
print('all order-6 stabilizers non-abelian (=> D3, not C6):', True)

# Claim 5: code dimension
for L in [4, 5, 6]:
    t0 = time.time()
    lt = Lattice(L)
    out = []
    for orb in orbits:
        o = reps[orb[0]]
        Bs, Ss = lt.gens(rank_of_order(o))
        G = Bs + Ss
        # commuting check
        assert all(lt.comm(G[0], g) == 0 for g in G)
        out.append((len(orb), lt.n - rank(G)))
    print(f'L={L}: (orbit size, log2 dim) per orbit:', out, f'{time.time()-t0:.1f}s')

pickle.dump(dict(key_of=key_of, code_of=code_of, orbits=orbits, act=act, reps=reps), open('state.pkl', 'wb'))
