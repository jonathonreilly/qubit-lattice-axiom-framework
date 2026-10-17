"""Is the half-edge BKSF code of a D3 ordering invariant under a C4 (or any R) with an on-site Clifford?
Unknown on-site linear map S on a site's 12 bits (6 qubits: x6|z6). Condition: for every generator g, the image
(site permutation v -> Rv, then S on every site) commutes with every generator. Linear in S. Then test the
solution space for an invertible symplectic S."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_site_local_six_direction_qubit_realization_2026_10_17 as hf
bk, c1 = hf.bk, hf.c1
O = c1.O
L = 4
h = hf.Half(L); n = h.n; V = h.V
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
o0 = next(o for o in orders if sum(1 for M in O if H[bk.rot_order(M, o)] == H[o]) == 6)
C = h.code(o0)
def site_bits(vec, s):   # 12 bits of site s: x(6) | z(6)
    return np.concatenate([vec[6 * s:6 * s + 6], vec[n + 6 * s:n + 6 * s + 6]])
def sidx(v): return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)
def solve_space(A):
    """null space of A (rows: equations) over GF(2)"""
    r, N = c1.f2_rank_and_null(A.T)   # left null of A^T = right null of A
    return N
res = {}
for M in O:
    kd = bk.kind(M)
    if kd in res: continue
    # site map v -> Mv ; image of generator g: for each site s of g, new site s' = M s, bits S @ g_s
    # commutation of image(g) with generator h: sum over sites t of sym(S g_{M^-1 t}, h_t) = sum_t g^T S^T J h_t
    # unknown S entries S[i][j] (output i, input j): sym(S a, b) = (S a) . (J b) = sum_ij S_ij a_j (J b)_i
    J = np.zeros((12, 12), np.uint8); J[:6, 6:] = np.eye(6); J[6:, :6] = np.eye(6)
    Minv = np.round(np.linalg.inv(M)).astype(int)
    rows = []
    gens_near = [g for g in C if any(site_bits(g, sidx(v)).any() for v in [(0, 0, 0)])]
    for g in gens_near:
        gsites = [s for s in range(L ** 3) if site_bits(g, s).any()]
        # image sites
        img = {}
        for s in gsites:
            v = (s // (L * L), (s // L) % L, s % L)
            w = tuple(int(x) for x in M @ np.array(v)); img[sidx(w)] = site_bits(g, s)
        for hgen in C:
            tsites = [t for t in img if site_bits(hgen, t).any()]
            if not tsites: continue
            row = np.zeros(144, np.uint8)
            for t in tsites:
                a = img[t]; Jb = (J @ site_bits(hgen, t)) % 2
                row ^= (np.outer(Jb, a) % 2).astype(np.uint8).flatten()
            rows.append(row)
    A = np.unique(np.array(rows), axis=0)
    N = solve_space(A)
    # search the solution space for an invertible symplectic S
    dim = len(N)
    found = None
    if dim <= 20:
        for coeffs in itertools.product((0, 1), repeat=dim):
            if not any(coeffs): continue
            Svec = (np.array(coeffs) @ N) % 2
            S = Svec.reshape(12, 12)
            if ((S.T @ J @ S) % 2 == J).all():
                found = S; break
    res[kd] = (dim, found is not None)
    print(kd, 'solution space dim', dim, 'symplectic invertible S found:', found is not None, flush=True)
