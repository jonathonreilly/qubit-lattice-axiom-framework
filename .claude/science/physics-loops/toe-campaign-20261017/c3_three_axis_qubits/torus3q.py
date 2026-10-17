"""Torus code dimension for a 3-qubit-per-site rule given as orbit index list in orb3q_<ACTION>.pkl."""
import sys, itertools, pickle, numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
ACTION = sys.argv[1]; orbs = [int(v) for v in sys.argv[2].split(',')]; Ls = [int(v) for v in sys.argv[3:]]
d = pickle.load(open(f'orb3q_{ACTION}.pkl', 'rb')); elems = d['elems']
STAR = c1.STAR
def dec(a): return [((int(a) >> (6*i)) & 63) for i in range(7)]
gens = [dec(e) for k in orbs for e in elems[k]]
for L in Ls:
    n = 3 * L**3; idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    rows = []
    for v in itertools.product(range(L), repeat=3):
        for g in gens:
            x = np.zeros(2*n, np.uint8)
            for i, l in enumerate(g):
                if not l: continue
                p = [v[j] + STAR[i][j] for j in range(3)]
                for a in range(3):
                    lab = (l >> (2*a)) & 3
                    if lab in (1, 2): x[idx(p, a)] ^= 1
                    if lab in (2, 3): x[n + idx(p, a)] ^= 1
            rows.append(x)
    r, N = c1.f2_rank_and_null(np.array(rows))
    print(f'orbits {orbs} L={L}: generators/site {len(gens)}, qubits {n}, rank {r}, log2 code dim {n-r}', flush=True)
