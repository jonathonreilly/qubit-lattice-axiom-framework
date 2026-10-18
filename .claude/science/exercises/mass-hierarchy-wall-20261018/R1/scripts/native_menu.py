"""R1 Test A: native flavour-charge menu on the cubic lattice.

Group G  = O (24 proper cubic rotations).
Group G' = Z2^3 x| O (192), translations mod 2 acting on hw1 corners by signs.

For a generation rep V (L-handed) and one real spurion sigma along direction n,
compute the 'Krylov' filtration F_n = span{ h(n) : h equivariant poly map
sigma -> V, deg h <= n } and its jump degrees (the native FN exponents when the
R-handed partners are internal singlets).  Also: the LV order (first degree at
which an equivariant map sigma -> traceless-symmetric 2-tensors (E+T2, trivial
translation) is nonzero at n), the residual stabiliser of n and whether it acts
by scalars on V (CKM-block test), and bilinear (V_L x V_R) singular-value orders
with random O(1) coefficients.
"""
import itertools, sys
import numpy as np

np.set_printoptions(precision=4, suppress=True, linewidth=140)
TOL = 1e-9

# ---------- group elements ----------
def proper_rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3))
            for i, p in enumerate(perm):
                M[p, i] = signs[i]
            if round(np.linalg.det(M)) == 1:
                mats.append(M)
    return mats

ROT = proper_rotations()
assert len(ROT) == 24
TRANS = [np.array(t) for t in itertools.product([0, 1], repeat=3)]

def a2(R):
    return round(np.linalg.det(np.abs(R)))

B_E = np.array([[1, -1, 0], [1, 1, -2]], dtype=float).T
B_E[:, 0] /= np.sqrt(2); B_E[:, 1] /= np.sqrt(6)

# traceless symmetric basis (5)
TS = []
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    X = np.zeros((3, 3)); X[i, j] = X[j, i] = 1 / np.sqrt(2); TS.append(X)
X = np.diag([1, -1, 0]) / np.sqrt(2); TS.append(X)
X = np.diag([1, 1, -2]) / np.sqrt(6); TS.append(X)
TS = np.array(TS)

def rep_matrix(name, t, R):
    s = np.array([(-1) ** int(x) for x in t])
    P = np.abs(R)
    if name == 'A1': return np.eye(1)
    if name == 'A2': return np.array([[a2(R)]], float)
    if name == 'E': return B_E.T @ P @ B_E
    if name == 'T1': return R.copy()
    if name == 'T2': return a2(R) * R
    if name == 'triv3': return np.eye(3)
    if name == 'P': return P.copy()
    if name == 'P2': return a2(R) * P
    if name == 'S': return np.diag(s) @ P            # hw1-corner triplet / hw1 star
    if name == 'S2': return a2(R) * np.diag(s) @ P
    if name == 'C111': return np.array([[s.prod()]], float)
    if name == 'C111A2': return np.array([[s.prod() * a2(R)]], float)
    if name.startswith('D_'):  # sum of three 1-dim characters, e.g. D_A1_A1_A2
        return np.diag([rep_matrix(c, t, R)[0, 0] for c in name[2:].split('_')])
    if name == 'W':  # traceless symmetric tensors, trivial translation
        M = np.zeros((5, 5))
        for b in range(5):
            Y = R @ TS[b] @ R.T
            for a in range(5):
                M[a, b] = np.sum(TS[a] * Y)
        return M
    raise ValueError(name)

TRANSLATION_CHARGED = {'S', 'S2', 'C111', 'C111A2'}
def is_tc(name):
    return name in TRANSLATION_CHARGED or (name.startswith('D_') and 'C111' in name)

def group_for(names):
    if any(is_tc(n) for n in names):
        return [(t, R) for t in TRANS for R in ROT]
    return [(np.zeros(3, int), R) for R in ROT]

def check_hom(name, G):
    # verify homomorphism with law (t1,R1)(t2,R2) = (t1 + R1 t2 mod 2, R1 R2)
    rng = np.random.default_rng(0)
    for _ in range(60):
        i, j = rng.integers(len(G), size=2)
        (t1, R1), (t2, R2) = G[i], G[j]
        t = (t1 + np.abs(R1) @ t2) % 2
        lhs = rep_matrix(name, t, R1 @ R2)
        rhs = rep_matrix(name, t1, R1) @ rep_matrix(name, t2, R2)
        assert np.allclose(lhs, rhs), name

# ---------- monomials ----------
def monomials(d, k):
    return [c for c in itertools.combinations_with_replacement(range(d), k)]

def mono_val(vec, c):
    v = 1.0
    for i in c: v *= vec[i]
    return v

_CACHE = {}
def _reps(name, G):
    key = (name, len(G))
    if key not in _CACHE:
        _CACHE[key] = np.array([rep_matrix(name, t, R) for (t, R) in G])
    return _CACHE[key]

def equivariant_images(sig, V_L, V_R, n, k, G):
    """orthonormal basis of span{h(n)} over degree-k equivariant maps sigma -> V_L (x) V_R^T."""
    rs = _reps(sig, G); rl = _reps(V_L, G)
    rr = _reps(V_R, G) if V_R is not None else None
    d = rs.shape[1]
    gn = np.einsum('gij,j->gi', rs, n)
    vecs = []
    for c in monomials(d, k):
        mv = np.ones(len(G))
        for i in c: mv = mv * gn[:, i]
        if np.max(np.abs(mv)) < TOL: continue
        if rr is None:
            acc = np.einsum('g,gai->ai', mv, rl) / len(G)
            vecs.extend(list(acc))
        else:
            acc = np.einsum('g,gai,gbj->abij', mv, rl, rr) / len(G)
            dl, dr = rl.shape[1], rr.shape[1]
            vecs.extend(list(acc.reshape(dl * dr, dl * dr)))
    dl = rl.shape[1]; dr = rr.shape[1] if rr is not None else 1
    if not vecs: return np.zeros((0, dl * dr))
    A = np.array(vecs)
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    if s[0] < 1e-12: return np.zeros((0, dl * dr))
    r = int(np.sum(s > 1e-8 * s[0]))
    return vt[:r]

def krylov(sig, V, n, G, K=8):
    basis = np.zeros((0, 3)); jumps = []
    for k in range(K + 1):
        B = equivariant_images(sig, V, None, n, k, G)
        if B.shape[0]:
            M = np.vstack([basis, B])
            r = np.linalg.matrix_rank(M, tol=1e-8)
            while len(jumps) < r: jumps.append(k)
            u, s, vt = np.linalg.svd(M, full_matrices=False)
            basis = vt[:r]
        if len(jumps) >= 3: break
    while len(jumps) < 3: jumps.append(None)
    return jumps

def lv_order(sig, n, G, K=6):
    for k in range(1, K + 1):
        B = equivariant_images(sig, 'W', None, n, k, G)
        if B.shape[0]: return k
    return None

def stabiliser(sig, n, G):
    return [(t, R) for (t, R) in G if np.allclose(rep_matrix(sig, t, R) @ n, n)]

def acts_by_scalars(V, H):
    for (t, R) in H:
        M = rep_matrix(V, t, R)
        if not np.allclose(M, M[0, 0] * np.eye(M.shape[0])): return False
    return True

def isotypic_dims(V, H):
    # number of distinct H-characters (abelianised check via commutant dimension)
    chars = [np.trace(rep_matrix(V, t, R)) for (t, R) in H]
    return round(sum(abs(c) ** 2 for c in chars) / len(H))   # = sum m_i^2

def bilinear_orders(sig, VL, VR, n, G, K=7, seed=0):
    rng = np.random.default_rng(seed)
    mats = []
    for k in range(K + 1):
        B = equivariant_images(sig, VL, VR, n, k, G)
        for row in B:
            mats.append((k, (rng.normal() + 1j * rng.normal()) * row.reshape(3, 3)))
    def Y(eps):
        M = np.zeros((3, 3), complex)
        for k, X in mats: M = M + eps ** k * X
        return M
    e1, e2 = 1e-2, 1e-3
    s1 = np.linalg.svd(Y(e1), compute_uv=False)
    s2 = np.linalg.svd(Y(e2), compute_uv=False)
    out = []
    for a, b in zip(s1, s2):
        if a < 1e-13 or b < 1e-16:
            out.append('inf'); continue
        sl = np.log(b / a) / np.log(e2 / e1)
        out.append('inf' if sl > 7.5 else f'{round(sl * 2) / 2:g}')
    # degeneracy flag: two finite singular values equal to 1e-3 relative at eps=1e-3
    deg = any(abs(s2[i] - s2[i + 1]) < 1e-3 * s2[i] and s2[i + 1] > 1e-14 for i in range(2))
    return out + (['DEG'] if deg else [])

SPURIONS = {
    'A2': [('+', np.array([1.0]))],
    # E basis: e1 = (1,-1,0)/sqrt2, e2 = (1,1,-2)/sqrt6.  Michel (tetragonal) lines: e2 and its S3 images.
    'E': [('tetr-z', np.array([0.0, 1.0])), ('tetr-z(-)', np.array([0.0, -1.0])),
          ('gen0.37', np.array([np.sin(0.37), np.cos(0.37)]))],
    'T1': [('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / np.sqrt(2)),
           ('111', np.ones(3) / np.sqrt(3)), ('gen', np.array([0.83, 0.47, 0.30]))],
    'T2': [('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / np.sqrt(2)),
           ('111', np.ones(3) / np.sqrt(3)), ('gen', np.array([0.83, 0.47, 0.30]))],
    'S': [('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / np.sqrt(2)),
          ('111', np.ones(3) / np.sqrt(3)), ('gen', np.array([0.83, 0.47, 0.30]))],
    'S2': [('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / np.sqrt(2)),
           ('111', np.ones(3) / np.sqrt(3)), ('gen', np.array([0.83, 0.47, 0.30]))],
    'C111': [('+', np.array([1.0]))],
    'C111A2': [('+', np.array([1.0]))],
}
GENREPS_O = ['P', 'P2', 'T1', 'T2', 'D_A1_A1_A2', 'D_A1_A2_A2']
GENREPS_G2 = ['P', 'P2', 'T1', 'T2', 'S', 'S2', 'D_A1_A1_A2', 'D_A1_A2_A2', 'D_A1_C111_C111A2', 'D_A1_A2_C111', 'D_A1_A1_C111']

if __name__ == '__main__':
    Gfull = [(t, R) for t in TRANS for R in ROT]
    for nm in ['A2', 'E', 'T1', 'T2', 'P', 'P2', 'S', 'S2', 'C111', 'C111A2', 'W']:
        check_hom(nm, Gfull)
    print('homomorphism checks passed for all reps on Z2^3 x| O')
    # sanity: characters / irreducibility on O
    G0 = group_for(['E'])
    for nm in ['A2', 'E', 'T1', 'T2', 'P', 'W']:
        chars = [np.trace(rep_matrix(nm, t, R)) for (t, R) in G0]
        print(f'  <chi,chi>_O[{nm}] = {sum(c*c for c in chars)/24:.3f}')

    print('\n=== Krylov exponents (L in V, R internal singlets), LV order, residual ===')
    print('sigma   dir         V    exps          LVorder  |H|  H-scalar-on-V  sum m_i^2(V|H)')
    rows = []
    for sig, dirs in SPURIONS.items():
        reps = GENREPS_G2 if sig in TRANSLATION_CHARGED else GENREPS_O
        for dname, n in dirs:
            for V in reps:
                G = group_for([sig, V])
                ex = krylov(sig, V, n, G)
                lv = lv_order(sig, n, group_for([sig]))
                H = stabiliser(sig, n, G)
                sc = acts_by_scalars(V, H)
                iso = isotypic_dims(V, H)
                rows.append((sig, dname, V, ex, lv, len(H), sc, iso))
                print(f'{sig:7s} {dname:11s} {V:4s} {str(ex):14s} {str(lv):8s} {len(H):4d}  {str(sc):13s}  {iso}')
    sys.stdout.flush()

    print('\n=== bilinear singular-value orders (random O(1) coefficients, 2 seeds) ===')
    for sig, dirs in SPURIONS.items():
        reps = GENREPS_G2 if sig in TRANSLATION_CHARGED else GENREPS_O
        reps = reps + ['triv3']
        for dname, n in dirs:
            for VL in reps:
                for VR in reps:
                    if VL == 'triv3' and VR == 'triv3': continue
                    if VR == 'triv3' or VL == 'triv3':
                        pass
                    G = group_for([sig, VL, VR])
                    o0 = bilinear_orders(sig, VL, VR, n, G, seed=1)
                    o1 = bilinear_orders(sig, VL, VR, n, G, seed=2)
                    flag = '' if o0 == o1 else '  (seed-dependent)'
                    print(f'{sig:7s} {dname:11s} L={VL:5s} R={VR:5s} orders {o0}{flag}')
            sys.stdout.flush()
