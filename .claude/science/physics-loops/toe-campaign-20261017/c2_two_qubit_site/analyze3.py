"""Vectorized orbit sign-consistency and compatibility for two-qubit-site survivors."""
import itertools, sys, pickle, time
import numpy as np
sys.argv = [sys.argv[0]] + sys.argv[1:]
ACTION, FACTION = sys.argv[1], sys.argv[2]
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
O, STAR, SIDX = c1.O, c1.STAR, c1.SIDX
t0 = time.time()
def log(*a): print(f'[{time.time()-t0:7.1f}s]', *a, flush=True)
def sp1(a, b): return int(a != 0 and b != 0 and a != b)
SP = np.array([[sp1(l1 >> 2, l2 >> 2) ^ sp1(l1 & 3, l2 & 3) for l2 in range(16)] for l1 in range(16)], np.uint8)
def lab(Qm):
    m, sg = np.zeros(4, int), np.ones(4, int)
    for a in (1, 2, 3):
        col = Qm[:, a - 1]; b = int(np.nonzero(col)[0][0]); m[a] = b + 1; sg[a] = int(col[b])
    return m, sg
RT = []
for M in O:
    pos = [SIDX[tuple(int(v) for v in M @ np.array(p))] for p in STAR]
    (ms, ss), (mf, sf) = lab(c1.Q(M, ACTION)), lab(c1.Q(M, FACTION))
    lm = np.array([4 * ms[l >> 2] + mf[l & 3] for l in range(16)], np.uint32)
    lsg = np.array([ss[l >> 2] * sf[l & 3] for l in range(16)], np.int8)
    RT.append((pos, lm, lsg))
SH = []
for s in itertools.product(range(-2, 3), repeat=3):
    pr = [(i, j) for i in range(7) for j in range(7) if tuple(np.subtract(STAR[i], STAR[j])) == s]
    if pr: SH.append(pr)
def nib(a, i): return (a >> (4 * i)) & 15
def transform(a, k):
    pos, lm, lsg = RT[k]; out = np.zeros_like(a); sg = np.ones(a.shape, np.int8)
    for i in range(7):
        nb = nib(a, i); out |= lm[nb] << (4 * pos[i]); sg *= lsg[nb]
    return out, sg
def commutes_all(a, b):
    ok = np.ones(a.shape, bool)
    for pr in SH:
        par = np.zeros(a.shape, np.uint8)
        for i, j in pr: par ^= SP[nib(a, i), nib(b, j)]
        ok &= par == 0
    return ok
S = np.unique(pickle.load(open(f'surv_{ACTION}_{FACTION}.pkl', 'rb')).astype(np.uint32))
T = np.stack([transform(S, k)[0] for k in range(24)])       # 24 x n images
G = np.stack([transform(S, k)[1] for k in range(24)])
rep = T.min(axis=0)
reps, inv = np.unique(rep, return_inverse=True)
log('strings', S.size, 'orbits', reps.size)
# sign consistency: for each representative, images under O with signs must agree on repeated strings
R = reps
TR = np.stack([transform(R, k)[0] for k in range(24)]); GR = np.stack([transform(R, k)[1] for k in range(24)])
cons = np.ones(R.size, bool)
for k in range(24):
    for l in range(k + 1, 24):
        same = TR[k] == TR[l]
        cons &= ~same | (GR[k] == GR[l])
R, TR = R[cons], TR[:, cons]
log('sign-consistent orbits', R.size)
n = R.size
orbit_elems = [np.unique(TR[:, i]) for i in range(n)]
adj = {i: set() for i in range(n)}
allel = np.concatenate(orbit_elems); owner = np.concatenate([np.full(e.size, i) for i, e in enumerate(orbit_elems)])
for i in range(n):
    ok = commutes_all(np.full(allel.shape, R[i], np.uint32), allel)
    bad = set(owner[~ok].tolist())
    for j in range(n):
        if j != i and j not in bad: adj[i].add(j)
log('compatibility edges', sum(len(v) for v in adj.values()) // 2)
pickle.dump({'reps': R, 'elems': orbit_elems, 'adj': adj}, open(f'orb3_{ACTION}_{FACTION}.pkl', 'wb'))
L = 'IXYZ'
def show(a): return ' '.join(L[(int(a) >> (4 * i + 2)) & 3] + L[(int(a) >> (4 * i)) & 3] for i in range(7))
labs_s = [set(((int(e) >> (4 * i + 2)) & 3) for e in orbit_elems[k] for i in range(7)) - {0} for k in range(n)]
labs_f = [set(((int(e) >> (4 * i)) & 3) for e in orbit_elems[k] for i in range(7)) - {0} for k in range(n)]
from collections import Counter
print(Counter((len(labs_s[k]), len(labs_f[k])) for k in range(n)))
if n < 3000:
    cl = c1.maximal_cliques(n, adj); log('maximal cliques', len(cl), sorted(len(c) for c in cl)[-10:])
    pickle.dump(cl, open(f'cl3_{ACTION}_{FACTION}.pkl', 'wb'))
