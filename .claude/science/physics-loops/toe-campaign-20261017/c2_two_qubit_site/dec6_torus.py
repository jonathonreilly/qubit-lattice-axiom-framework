import sys, itertools, numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
# qubit index: 2*site + (0 spin, 1 flavour); generator at v: spin Chamon on nbrs, flavour X on nbrs
def run(L):
    n = 2 * L**3; idx = lambda p, q: 2 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + q
    rows = []
    for v in itertools.product(range(L), repeat=3):
        x = np.zeros(2 * n, np.uint8)
        for a in range(3):
            for s in (1, -1):
                p = list(v); p[a] += s
                lab = a + 1; i = idx(p, 0)
                if lab in (1, 2): x[i] ^= 1
                if lab in (2, 3): x[n + i] ^= 1
                x[idx(p, 1)] ^= 1    # flavour X
        rows.append(x)
    r, N = c1.f2_rank_and_null(np.array(rows))
    print(f'L={L}: qubits {n}, rank {r}, log2 code dim {n - r}, relations {len(N)}', flush=True)
for L in map(int, sys.argv[1:]): run(L)
