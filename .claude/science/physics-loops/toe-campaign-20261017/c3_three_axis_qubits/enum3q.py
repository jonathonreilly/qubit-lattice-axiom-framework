"""Three axis-labelled qubits per site, labels soldered (ACTION) or fixed (trivial).
O acts: positions by R, qubit index a -> perm_R(a), Pauli labels on each qubit by Q(R).
Search strings on the star with a nontrivial stabilizer (fixed by a C2 axis, C2 edge or C3 rotation),
keep those commuting with every translate of every rotated image; then orbits."""
import itertools, sys, time, pickle
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
ACTION = sys.argv[1]
O, STAR, SIDX = c1.O, c1.STAR, c1.SIDX
t0 = time.time()
def log(*a): print(f'[{time.time()-t0:7.1f}s]', *a, flush=True)
def perm_of(M): return [int(np.nonzero(M[:, a])[0][0]) for a in range(3)]   # axis a -> perm[a]
def labmap(Qm):
    m = [0] * 4
    for a in (1, 2, 3): m[a] = int(np.nonzero(Qm[:, a - 1])[0][0]) + 1
    return m
# site label: 6 bits, qubit a (axis) occupies bits 2a..2a+1, value 0..3 = I X Y Z
SITE = []   # per group element: 64-entry map
for M in O:
    pm, lm = perm_of(M), labmap(c1.Q(M, ACTION))
    t = np.zeros(64, np.uint64)
    for s in range(64):
        out = 0
        for a in range(3):
            l = (s >> (2 * a)) & 3
            out |= lm[l] << (2 * pm[a])
        t[s] = out
    SITE.append(t)
POS = [[SIDX[tuple(int(v) for v in M @ np.array(p))] for p in STAR] for M in O]
def sp1(a, b): return int(a != 0 and b != 0 and a != b)
SP = np.array([[sum(sp1((s1 >> (2*a)) & 3, (s2 >> (2*a)) & 3) for a in range(3)) % 2 for s2 in range(64)] for s1 in range(64)], np.uint8)
SH = []
for s in itertools.product(range(-2, 3), repeat=3):
    pr = [(i, j) for i in range(7) for j in range(7) if tuple(np.subtract(STAR[i], STAR[j])) == s]
    if pr: SH.append(pr)
def nib(a, i): return ((a >> np.uint64(6 * i)) & np.uint64(63)).astype(np.int64)
def transform(a, k):
    out = np.zeros_like(a)
    for i in range(7): out |= SITE[k][nib(a, i)] << np.uint64(6 * POS[k][i])
    return out
def commutes_all(a, b):
    ok = np.ones(a.shape, bool)
    for pr in SH:
        par = np.zeros(a.shape, np.uint8)
        for i, j in pr: par ^= SP[nib(a, i), nib(b, j)]
        ok &= par == 0
    return ok
def key(M): return tuple(M.ravel())
def find(Mt): return next(k for k, M in enumerate(O) if np.array_equal(M, Mt))
gC4z = find(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])); gC3 = find(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))
def invariant_strings(k):
    """All strings fixed (labels mod sign) by group element k: choose labels on orbit reps of <g>."""
    g = POS[k]; orbits, seen = [], set()
    for i in range(7):
        if i in seen: continue
        orb = [i]; j = g[i]
        while j != i: orb.append(j); j = g[j]
        seen |= set(orb); orbits.append(orb)
    def gpow(lbl, steps):
        for _ in range(steps): lbl = int(SITE[k][lbl])
        return lbl
    choices = []
    for orb in orbits:
        opts = []
        for l in range(64):
            if gpow(l, len(orb)) != l: continue   # consistency around the orbit (returns to itself)
            opts.append(l)
        choices.append((orb, opts))
    total = np.prod([len(o) for _, o in choices]); log(f'element {k}: {len(orbits)} position orbits, {total} invariant strings')
    arrs = [np.array(o, np.uint64) for _, o in choices]
    grids = np.meshgrid(*arrs, indexing='ij')
    out = np.zeros(grids[0].shape, np.uint64)
    for (orb, _), G in zip(choices, grids):
        cur = G.copy()
        for step, i in enumerate(orb):
            out |= cur << np.uint64(6 * i)
            cur = SITE[k][cur.astype(np.int64)]
    return out.ravel()
surv = []
for k in (gC4z, gC3):
    S = invariant_strings(k); S = S[S != 0]
    CH = 1 << 21
    for st in range(0, S.size, CH):
        a = S[st:st + CH]
        a = a[commutes_all(a, a)]
        for kk in range(1, 24):
            if a.size == 0: break
            a = a[commutes_all(a, transform(a, kk))]
        surv.append(a)
    log('cumulative survivors', sum(x.size for x in surv))
S = np.unique(np.concatenate(surv)); log('survivors', S.size)
T = np.stack([transform(S, k) for k in range(24)]); reps = np.unique(T.min(axis=0)); log('orbits', reps.size)
pickle.dump({'S': S, 'reps': reps}, open(f'surv3q_{ACTION}.pkl', 'wb'))
