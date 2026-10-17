"""Claim 4: Chamon rule on L^3 torus: code dimension and phases of all generator relations."""
import numpy as np, itertools, time, sys

def gf2_rank_kernel(M):
    """returns rank and a basis of the left kernel {v : v M = 0} over GF(2)."""
    M = M.copy() % 2; n, m = M.shape
    A = np.concatenate([M, np.eye(n, dtype=np.uint8)], axis=1).astype(np.uint8)
    r = 0
    for c in range(m):
        hits = np.nonzero(A[r:, c])[0]
        if len(hits) == 0: continue
        k = r + hits[0]; A[[r, k]] = A[[k, r]]
        rest = np.nonzero(A[:, c])[0]; rest = rest[rest != r]
        A[rest] ^= A[r]; r += 1
        if r == n: break
    return r, A[r:, m:]

def pauli_mul(p, q):
    """p=(phase k for i^k, x bits, z bits) with operator i^k X^x Z^z per site convention."""
    k1, x1, z1 = p; k2, x2, z2 = q
    # X^x1 Z^z1 X^x2 Z^z2 = (-1)^{z1.x2} X^{x1+x2} Z^{z1+z2}
    return ((k1 + k2 + 2 * int(np.dot(z1, x2) % 2)) % 4, x1 ^ x2, z1 ^ z2)

for L in [int(a) for a in sys.argv[1:]] or [4, 6]:
    t0 = time.time(); n = L ** 3
    idx = lambda p: ((p[0] % L) * L + p[1] % L) * L + p[2] % L
    gens = []
    for g in itertools.product(range(L), repeat=3):
        x = np.zeros(n, np.uint8); z = np.zeros(n, np.uint8); k = 0
        for s in (1, -1):
            x[idx((g[0] + s, g[1], g[2]))] ^= 1                      # X
            x[idx((g[0], g[1] + s, g[2]))] ^= 1; z[idx((g[0], g[1] + s, g[2]))] ^= 1; k += 1  # Y = i X Z
            z[idx((g[0], g[1], g[2] + s))] ^= 1                      # Z
        gens.append((k % 4, x, z))
    # Hermiticity check & commutation
    G = np.array([np.concatenate([x, z]) for _, x, z in gens])
    Xs, Zs = G[:, :n].astype(int), G[:, n:].astype(int)
    comm = (Xs @ Zs.T + Zs @ Xs.T) % 2
    rank, ker = gf2_rank_kernel(G)
    bad_phase = 0; sizes = []
    for v in ker:
        P = (0, np.zeros(n, np.uint8), np.zeros(n, np.uint8))
        for i in np.nonzero(v)[0]: P = pauli_mul(P, gens[i])
        assert not P[1].any() and not P[2].any()
        if P[0] != 0: bad_phase += 1
        sizes.append(int(v.sum()) % 2)
    print(f'L={L}: n={n}, all commute={not comm.any()}, rank={rank}, log2 dim k={n-rank} (4L={4*L}), '
          f'kernel dim={len(ker)}, relations with phase != +1: {bad_phase}, '
          f'odd-size relations in basis: {sum(sizes)}  ({time.time()-t0:.1f}s)')
