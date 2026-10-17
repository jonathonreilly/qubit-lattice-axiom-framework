import sys, pickle, re, itertools
import numpy as np
sys.path.insert(0, '../c4'); sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
from stats import t_junction
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
ACTION = sys.argv[1]; LOG = sys.argv[2]
d = pickle.load(open(f'orb3q_{ACTION}.pkl', 'rb')); cl = pickle.load(open(f'cl3q_{ACTION}.pkl', 'rb'))
STAR = c1.STAR
def dec(a): return [((int(a) >> (6*i)) & 63) for i in range(7)]
def rank(orbs, L):
    n = 3 * L**3; idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    rows = []
    for v in itertools.product(range(L), repeat=3):
        for k in orbs:
            for e in d['elems'][k]:
                x = np.zeros(2*n, np.uint8)
                for i, l in enumerate(dec(e)):
                    if not l: continue
                    p = [v[j] + STAR[i][j] for j in range(3)]
                    for a in range(3):
                        lab = (l >> (2*a)) & 3
                        if lab in (1, 2): x[idx(p, a)] ^= 1
                        if lab in (2, 3): x[n + idx(p, a)] ^= 1
                rows.append(x)
    return c1.f2_rank_and_null(np.array(rows))[0]
hits = []
for line in open(LOG):
    m = re.match(r'(\d+) (\d+) gens/site (\d+) L4 \(log2dim, bad relations\): \((\d+), (\d+)\) L6: \((\d+), (\d+)\)', line)
    if m:
        ci, sz, g, d4, b4, d6, b6 = map(int, m.groups())
        if b4 == 0 and b6 == 0 and d4 == d6 and d4 > 0: hits.append(ci)
L = 'IXYZ'
for ci in hits:
    orbs = sorted(cl[ci]); target = (rank(orbs, 4), rank(orbs, 6))
    for k in sorted(orbs, key=lambda k: -len(d['elems'][k])):
        trial = [o for o in orbs if o != k]
        if trial and (rank(trial, 4), rank(trial, 6)) == target: orbs = trial
    gens, names = [], []
    for k in orbs:
        for e in d['elems'][k]:
            l = dec(e); gens.append({STAR[i]: tuple((l[i] >> (2*a)) & 3 for a in range(3)) for i in range(7) if l[i]})
            names.append(' '.join(''.join(L[(x >> (2*a)) & 3] for a in range(3)) for x in l))
    out = []
    for r_ in range(1, len(gens) + 1):
        for sub in itertools.combinations(range(len(gens)), r_):
            pat = [((0,0,0), j) for j in sub]
            r = t_junction(gens, 3, pat, [(2,0,0),(0,2,0),(0,0,2)], R=3)
            if r[0] is not None: out.append((sub, r[0]))
    signs = sorted(set(o[1] for o in out))
    print(ci, 'minimal orbits', orbs, len(gens), 'gens; mobile charge patterns at origin:', len(out), 'exchange signs found:', signs, '|', names[0], flush=True)
