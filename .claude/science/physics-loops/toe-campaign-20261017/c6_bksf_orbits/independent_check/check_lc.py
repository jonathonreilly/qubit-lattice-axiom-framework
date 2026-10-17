"""Local-Clifford (on-site) equivalence test among the 60 codes.
Invariant: f_C(S) = dim(C cap P_S) (# independent stabilizers supported inside qubit set S).
Any per-qubit Clifford (site-dependent allowed) preserves supports, so C ~LC C' => f_C = f_C' for all S.
If the f-vectors of all 60 codes are pairwise distinct, no two distinct codes are LC-equivalent,
hence no rotation maps a code to itself up to LC beyond its genuine stabilizer, and no orbits merge.
Also: explicit search over translation-invariant per-orientation Cliffords (6^3=216) as a cross-check,
and full O_h (incl. improper) invariance check."""
import time, random, pickle, itertools
from collections import Counter
from core import *

st = pickle.load(open('state.pkl', 'rb'))
key_of, code_of, orbits, reps, act = st['key_of'], st['code_of'], st['orbits'], st['reps'], st['act']
lat = Lattice(4)
n = lat.n
FULL = (1 << (2 * n)) - 1
bases = {c: list(key_of[o]) for c, o in reps.items()}
orb_of = {c: i for i, orb in enumerate(orbits) for c in orb}


def qmask(qs):
    m = 0
    for q in qs:
        m |= (1 << q) | (1 << (n + q))
    return m


def star_edges(V):
    s = set()
    for v in V:
        for d in range(6):
            s.add(lat.edge_at(v, d))
    return s

random.seed(7)
clusters = []
nbr = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
for _ in range(40):
    V = {(0, 0, 0)}
    size = random.randint(2, 4)
    while len(V) < size:
        v = random.choice(sorted(V)); d = random.choice(nbr)
        V.add(tuple(v[i] + d[i] for i in range(3)))
    clusters.append(sorted(V))
# plus all rotated images of the first few clusters (so rotation-related tests are included)
extra = []
for V in clusters[:6]:
    for M in ROTS:
        extra.append(sorted(tuple(int(t) for t in M @ np.array(v)) for v in V))
clusters += extra
Smasks = [qmask(star_edges(V)) for V in clusters]

t0 = time.time()
sig = {}
for c in range(60):
    B = bases[c]; r = len(B)
    sig[c] = tuple(r - rank([b & (FULL ^ m) for b in B]) for m in Smasks)
groups = Counter(sig.values())
print('regions tested:', len(Smasks), '; distinct LC-invariant signatures among 60 codes:', len(groups), f'{time.time()-t0:.1f}s')
coll = [[c for c in range(60) if sig[c] == s] for s, k in groups.items() if k > 1]
print('colliding sets (code ids):', coll)
print('nontrivial f values seen:', sorted(set(x for s in sig.values() for x in s)))

# explicit translation-invariant per-orientation Clifford search (216) for every ordered pair in collisions,
# and also for each code vs. all rotated images (sanity: should only match the genuine stabilizer)
GL2 = [np.array(m).reshape(2, 2) for m in itertools.product([0, 1], repeat=4)
       if (m[0] * m[3] + m[1] * m[2]) % 2 == 1]
assert len(GL2) == 6
omask = [sum(1 << lat.eid(v, a) for v in lat.verts()) for a in range(3)]


def apply_cliff(p, gs):
    x = p & ((1 << n) - 1); z = p >> n
    nx = nz = 0
    for a in range(3):
        xa, za = x & omask[a], z & omask[a]
        g = gs[a]
        nx |= (xa if g[0, 0] else 0) ^ (za if g[0, 1] else 0)
        nz |= (xa if g[1, 0] else 0) ^ (za if g[1, 1] else 0)
    return nx | (nz << n)

keys = {c: key_of[reps[c]] for c in range(60)}
inv_key = {k: c for c, k in keys.items()}
t0 = time.time()
lc_hits = []
for c in range(60):
    for gs in itertools.product(GL2, repeat=3):
        if all(np.array_equal(g, np.eye(2, dtype=int)) for g in gs):
            continue
        img = rref([apply_cliff(b, gs) for b in bases[c]])
        if img in inv_key:
            lc_hits.append((c, inv_key[img], [g.tolist() for g in gs]))
print('nontrivial translation-invariant per-orientation Clifford maps code->some BKSF code:', lc_hits[:10], len(lc_hits), f'{time.time()-t0:.1f}s')

# improper rotations: does any of the 48 O_h elements fix a code? (reflections map BKSF codes to BKSF codes)
IMP = [-M for M in ROTS]
perms = [qubit_perm(lat, M) for M in IMP]
fixed_by_improper = Counter()
for c in range(60):
    k = 0
    for ri, M in enumerate(IMP):
        img = rref([apply_perm(lat, p, perms[ri]) for p in bases[c]])
        assert img in inv_key
        assert inv_key[img] == code_of[rot_order(M, reps[c])]
        if inv_key[img] == c:
            k += 1
    fixed_by_improper[k] += 1
print('histogram of #improper O_h elements fixing a code:', dict(fixed_by_improper))

# full-class distinctness at L=6
t0 = time.time()
lat6 = Lattice(6)
k6 = {rref(sum(lat6.gens(rank_of_order(reps[c])), [])) for c in range(60)}
print('L=6: 60 class reps give', len(k6), 'distinct groups', f'{time.time()-t0:.1f}s')
