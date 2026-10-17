import sys, itertools, numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
E = [(1,0,0),(0,1,0),(0,0,1)]
def run(L):
    n = 3 * L**3; idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
    rows = []
    for v in itertools.product(range(L), repeat=3):
        x = np.zeros(2*n, np.uint8)
        for a in range(3):
            for s in (1,-1):
                p = [v[i] + s*E[a][i] for i in range(3)]; x[idx(p, a)] ^= 1
        rows.append(x)
        for c in range(3):
            a, b = [k for k in range(3) if k != c]; z = np.zeros(2*n, np.uint8)
            for s in (1,-1):
                z[n + idx([v[i] + s*E[a][i] for i in range(3)], b)] ^= 1
                z[n + idx([v[i] + s*E[b][i] for i in range(3)], a)] ^= 1
            rows.append(z)
    r, N = c1.f2_rank_and_null(np.array(rows))
    # single-site free local variables: single-site Paulis commuting with all generators
    print(f'L={L}: qubits {n}, rank {r}, log2 code dim {n-r}', flush=True)
for L in map(int, sys.argv[1:]): run(L)
