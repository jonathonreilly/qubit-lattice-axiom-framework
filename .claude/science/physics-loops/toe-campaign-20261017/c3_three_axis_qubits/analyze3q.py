"""Sign consistency, compatibility and TQO/3D-mobility search for 3-axis-qubit survivors."""
import itertools, sys, pickle, time, subprocess
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/c2')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from module_tool import singular_script
ACTION = sys.argv[1]; LIM = int(sys.argv[2]) if len(sys.argv) > 2 else 200
O, STAR, SIDX = c1.O, c1.STAR, c1.SIDX
t0 = time.time()
def log(*a): print(f'[{time.time()-t0:7.1f}s]', *a, flush=True)
def perm_of(M): return [int(np.nonzero(M[:, a])[0][0]) for a in range(3)]
def labmap(Qm):
    m, sg = [0] * 4, [1] * 4
    for a in (1, 2, 3):
        col = Qm[:, a - 1]; b = int(np.nonzero(col)[0][0]); m[a], sg[a] = b + 1, int(col[b])
    return m, sg
SITE, SSG = [], []
for M in O:
    pm, (lm, ls) = perm_of(M), labmap(c1.Q(M, ACTION))
    t = np.zeros(64, np.uint64); g = np.ones(64, np.int8)
    for s in range(64):
        out, sg = 0, 1
        for a in range(3):
            l = (s >> (2 * a)) & 3; out |= lm[l] << (2 * pm[a]); sg *= ls[l]
        t[s], g[s] = out, sg
    SITE.append(t); SSG.append(g)
POS = [[SIDX[tuple(int(v) for v in M @ np.array(p))] for p in STAR] for M in O]
def sp1(a, b): return int(a != 0 and b != 0 and a != b)
SP = np.array([[sum(sp1((s1 >> (2*a)) & 3, (s2 >> (2*a)) & 3) for a in range(3)) % 2 for s2 in range(64)] for s1 in range(64)], np.uint8)
SH = []
for s in itertools.product(range(-2, 3), repeat=3):
    pr = [(i, j) for i in range(7) for j in range(7) if tuple(np.subtract(STAR[i], STAR[j])) == s]
    if pr: SH.append(pr)
def nib(a, i): return ((a >> np.uint64(6 * i)) & np.uint64(63)).astype(np.int64)
def transform(a, k):
    out = np.zeros_like(a); sg = np.ones(a.shape, np.int8)
    for i in range(7):
        nb = nib(a, i); out |= SITE[k][nb] << np.uint64(6 * POS[k][i]); sg *= SSG[k][nb]
    return out, sg
def commutes_all(a, b):
    ok = np.ones(a.shape, bool)
    for pr in SH:
        par = np.zeros(a.shape, np.uint8)
        for i, j in pr: par ^= SP[nib(a, i), nib(b, j)]
        ok &= par == 0
    return ok
d = pickle.load(open(f'surv3q_{ACTION}.pkl', 'rb')); reps = d['reps']
TR = np.stack([transform(reps, k)[0] for k in range(24)]); GR = np.stack([transform(reps, k)[1] for k in range(24)])
cons = np.ones(reps.size, bool)
for k in range(24):
    for l in range(k + 1, 24): cons &= (TR[k] != TR[l]) | (GR[k] == GR[l])
reps, TR = reps[cons], TR[:, cons]; n = reps.size; log('sign-consistent orbits', n)
elems = [np.unique(TR[:, i]) for i in range(n)]
allel = np.concatenate(elems); owner = np.concatenate([np.full(e.size, i) for i, e in enumerate(elems)])
adj = {}
for i in range(n):
    bad = set(owner[~commutes_all(np.full(allel.shape, reps[i], np.uint64), allel)].tolist())
    adj[i] = {j for j in range(n) if j != i and j not in bad}
log('edges', sum(len(v) for v in adj.values()) // 2)
def dec(a): return [((int(a) >> (6*i)) & 63) for i in range(7)]
def anti(p, l): return SP[p, l]
labsets = [set(l for e in elems[k] for l in dec(e)) - {0} for k in range(n)]
def commutant(labs): return frozenset(p for p in range(1, 64) if all(not anti(p, l) for l in labs))
comm = [commutant(labsets[k]) for k in range(n)]
# greedy: candidate unions = maximal cliques restricted to those whose union commutant is empty; test minimal ones of size <= 3
cands = [(k,) for k in range(n) if not comm[k]]
for i in range(n):
    if not comm[i]: continue
    for j in adj[i]:
        if j <= i or not comm[j]: continue
        cij = comm[i] & comm[j]
        if not cij: cands.append((i, j)); continue
        for k in adj[i] & adj[j]:
            if k <= j or not comm[k]: continue
            if not (cij & comm[k]): cands.append((i, j, k))
log('TQO-1 single-site candidate unions (size <= 3, minimal-ish):', len(cands))
pickle.dump({'reps': reps, 'elems': elems, 'adj': adj, 'cands': cands}, open(f'orb3q_{ACTION}.pkl', 'wb'))
R = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_check/runsing.sh'
L4 = 'IXYZ'
def show(e): return ' '.join(''.join(L4[(l >> (2*a)) & 3] for a in range(3)) for l in dec(e))
hits = 0
for c in cands[:LIM]:
    gens = []
    for k in c:
        for e in elems[k]:
            l = dec(e); gens.append({STAR[i]: tuple((l[i] >> (2*a)) & 3 for a in range(3)) for i in range(7) if l[i]})
    open('tmp3.sing', 'w').write(singular_script(gens, 3, 'c'))
    try:
        out = subprocess.run([R, 'tmp3.sing'], stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300).stdout
        mob = out.split('3D-mobile charge exists)?')[1].split()[0] if '3D-mobile' in out else '?'
    except subprocess.TimeoutExpired:
        mob = 'timeout'
    if mob != '0': hits += 1
    print(c, [len(elems[k]) for k in c], 'mobile3D =', mob, '|', ' / '.join(show(elems[k][0]) for k in c), flush=True)
log('done; nonzero/unknown', hits, 'of', min(LIM, len(cands)))
