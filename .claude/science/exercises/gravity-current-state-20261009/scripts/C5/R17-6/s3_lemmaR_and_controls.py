# R17-6 s3.
# (i) Lemma R check: in a uniform state over a mod-2 coset n0 + C (C = ker G mod 2),
#     <(-1)^{u.n}> != 0 iff u in rowspace(G) mod 2 (= C^perp). Label pairs s,t are
#     correlated iff e_s + e_t in rowspace. Check on an L^3 torus (N0914 slots) that
#     no single slot and no pair of slots within the box lies in the rowspace,
#     so label two-point functions are on-site only (white noise, regular at k=0).
# (ii) Controls for Theorem Z's diagnostic on lattice Gaussians (same observable:
#     the E readout's static susceptibility chi_ab(k) and f-sum m1_ab(k)):
#     EH comparator (exact constraints, physical space = TT(qhat)) and an
#     unconstrained elastic Gaussian.
import itertools, numpy as np
L = 4
types = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]
def sid(x, t): return ((x[0] % L) * L * L + (x[1] % L) * L + (x[2] % L)) * 6 + t
nS = 6 * L ** 3
rows = []
for x in itertools.product(range(L), repeat=3):
    for j in range(3):
        r = np.zeros(nS, np.uint8)
        e = [0, 0, 0]; e[j] = 1
        r[sid([x[0] + e[0], x[1] + e[1], x[2] + e[2]], j)] ^= 1; r[sid(x, j)] ^= 1
        for i in range(3):
            if i == j: continue
            t = types.index(tuple(sorted((i, j))))
            ei = [0, 0, 0]; ei[i] = 1
            r[sid(x, t)] ^= 1; r[sid([x[0] - ei[0], x[1] - ei[1], x[2] - ei[2]], t)] ^= 1
        rows.append(r)
R = np.array(rows, np.uint8)
def gf2_rref(A):
    A = A.copy(); piv = []; r = 0
    for c in range(A.shape[1]):
        p = np.nonzero(A[r:, c])[0]
        if len(p) == 0: continue
        p = p[0] + r; A[[r, p]] = A[[p, r]]
        nz = np.nonzero(A[:, c])[0]; nz = nz[nz != r]; A[nz] ^= A[r]
        piv.append(c); r += 1
        if r == A.shape[0]: break
    return A[:r], piv
B, piv = gf2_rref(R)
print(f'(i) L={L}: {nS} slots, {R.shape[0]} Gauss rows, rank over F2 = {B.shape[0]}')
def in_rowspace(u):
    v = u.copy()
    for k, c in enumerate(piv):
        if v[c]: v ^= B[k]
    return not v.any()
ones = sum(in_rowspace(np.eye(nS, dtype=np.uint8)[s]) for s in range(nS))
print(f'    single slots in rowspace (frozen labels): {ones}')
pairs = 0; tested = 0
for s in range(nS):
    for t in range(s + 1, nS):
        u = np.zeros(nS, np.uint8); u[s] = 1; u[t] = 1; tested += 1
        if in_rowspace(u): pairs += 1
print(f'    slot pairs tested: {tested}; pairs in rowspace (correlated labels): {pairs}')
# minimum weight of rowspace elements, quick bound: each row has weight 6
print(f'    row weights: {sorted(set(R.sum(1)))}')
# (ii) controls
print('\n(ii) controls: chi_ab(k)/(1/J) for E readout, k = 1e-3 along z and along y, component xz')
def ptt(q):
    q = np.array(q, float); q /= np.linalg.norm(q); P = np.eye(3) - np.outer(q, q)
    basis = []
    for (i, j) in types:
        Bm = np.zeros((3, 3)); Bm[i, j] = Bm[j, i] = 1; basis.append(Bm / np.linalg.norm(Bm))
    def tt(T): return P @ T @ P - 0.5 * P * np.trace(P @ T)
    return np.array([[np.sum(b2 * tt(b1)) for b1 in basis] for b2 in basis])
k = 1e-3
for nm, kv in [('k || z', (0, 0, k)), ('k || y', (0, k, 0)), ('k || (1,1,0)', (k, k, 0))]:
    qh = 2 * np.sin(np.array(kv) / 2)
    chiEH = ptt(qh)        # EH comparator: physical E = TT(qhat), chi = P_TT / J
    chiEl = np.eye(6)      # elastic Gaussian: chi = 1/J on every component
    a = types.index((0, 2))
    print(f'   {nm:14s} EH: chi_xz,xz = {chiEH[a, a]:.3f}, rank(chi) = {np.linalg.matrix_rank(chiEH, 1e-9)}; elastic: chi_xz,xz = {chiEl[a, a]:.3f}, rank = 6')
print('   EH: chi(k) -> P_TT(khat)/J, direction-dependent at k -> 0 (pinch point): branch (B) of Theorem Z.')
print('   elastic: chi = I/J regular; m1 = g qhat^2 on all 6 -> six linear branches: branch (A), partners.')
