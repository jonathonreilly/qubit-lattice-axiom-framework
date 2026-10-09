"""K7a part 2, real space: 4D staggered linearized EH on a periodic Z^4 torus (L cells per side).

Half-unit coordinates X in Z_{2L}^4 (A-lattice spacing = 2 half-units).  Class of X = X mod 2
= subset S of {0..3}.  h_{mu nu} (mu<=nu) lives where X mod 2 = indicator({mu} xor {nu});
xi_mu where X mod 2 = indicator({mu}).  (partial_lam f)(Y) = f(Y+e_lam) - f(Y-e_lam)  (half-unit shifts;
symbol 2i sin(k/2) for k in A-units).

Checks (all exact integer arithmetic unless noted):
R1 every product in the action lands on a single class (assert by construction)
R2 Q D = 0 exactly (lattice linearized diffeo invariance)
R3 all 384 W(B4) elements about a vertex: P^T Q P = Q and P D = D P_xi
R4 spectrum: nullity(Q) = rank(D) + 10 (constants) -> no doublers / no extra zero modes; 6 nonzero
   eigenvalue branches; compare Bloch blocks of the real-space Q to the symbolic symbol K(s)
R5 cross-check with A25's real-space 3D operator V (stag2.py): spatial slice of Q at fixed t
"""
import itertools, sys, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

t0 = time.time()
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
N2 = 2 * L


def say(*a):
    print(*a); sys.stdout.flush()


def cls(mu, nu):
    b = [0, 0, 0, 0]
    b[mu] ^= 1; b[nu] ^= 1
    return tuple(b)


# site lists per class (positions are half-unit coordinate tuples); index maps
allX = np.array(list(itertools.product(range(N2), repeat=4)))
par = allX % 2
site_of_class = {}
for S in itertools.product((0, 1), repeat=4):
    m = np.all(par == np.array(S), axis=1)
    site_of_class[S] = allX[m]
index = {}                                     # (class, X tuple) -> local index
for S, arr in site_of_class.items():
    index[S] = {tuple(x): n for n, x in enumerate(arr)}
Ns = L ** 4
assert all(len(v) == Ns for v in site_of_class.values())


class Field:
    """a field = list of components, each (class); global index = comp * Ns + local"""
    def __init__(self, classes):
        self.classes = classes
        self.n = len(classes) * Ns


H_CLASSES = [cls(i, j) for (i, j) in PAIRS]                    # 10 comps
XI_CLASSES = [cls(m, m) if False else tuple(1 if k == m else 0 for k in range(4)) for m in range(4)]
hF, xF = Field(H_CLASSES), Field(XI_CLASSES)


def shift_op(S_in, lam, sgn):
    """matrix from field values on class S_in to values on class S_out = S_in xor {lam}:
       (T f)(Y) = f(Y + sgn*e_lam)"""
    S_out = list(S_in); S_out[lam] ^= 1; S_out = tuple(S_out)
    rows, cols = [], []
    for Y, r in index[S_out].items():
        Z = list(Y); Z[lam] = (Z[lam] + sgn) % N2
        rows.append(r); cols.append(index[S_in][tuple(Z)])
    return S_out, sp.csr_matrix((np.ones(Ns), (rows, cols)), shape=(Ns, Ns))


def ddiff(S_in, lam):
    S_out, Tp = shift_op(S_in, lam, +1)
    _, Tm = shift_op(S_in, lam, -1)
    return S_out, (Tp - Tm).tocsr()


def block(rows, ncomp_out, ncomp_in):
    """rows: dict (a,b)->sparse Ns x Ns -> bmat"""
    B = [[None] * ncomp_in for _ in range(ncomp_out)]
    for (a, b), M in rows.items():
        B[a][b] = M if B[a][b] is None else B[a][b] + M
    return sp.bmat(B, format='csr', dtype=float) if True else None


def compidx(mu, nu):
    return PAIRS.index((min(mu, nu), max(mu, nu)))


# ---- operators.  Output "derivative objects" are fields on explicit classes with bookkeeping.
# grad_{lam}(h_{mu nu}) for the FULL tensor (mu,nu all 16 ordered pairs): lives at class(mu,nu) xor lam
# We build, per object, a sparse matrix from h (10 comps) -> object (single class), and record its class.
objects = []        # list of (name, class, matrix 1-block Ns x 10Ns, weight)

def hmat_row(comp_terms):
    """comp_terms: list of (comp, coeff, op) with op a Ns x Ns sparse (already mapped to the same output class)."""
    B = [None] * 10
    for c, coeff, op in comp_terms:
        B[c] = coeff * op if B[c] is None else B[c] + coeff * op
    B = [sp.csr_matrix((Ns, Ns)) if b is None else b for b in B]
    return sp.hstack(B, format='csr')

ops_cache = {}
def dop(S_in, lam):
    key = (S_in, lam)
    if key not in ops_cache:
        ops_cache[key] = ddiff(S_in, lam)
    return ops_cache[key]

# F(h) = 1/4 [ sum_{lam,mu,nu}(d_lam h_mu nu)^2 - 2 sum_nu div_nu^2 + 2 sum_nu div_nu g_nu - sum_nu g_nu^2 ],
# div_nu = sum_mu d_mu h_{mu nu}, g_nu = d_nu tr h ; Hessian: (a.h)^2 -> 2 a^T a ; 2(a.h)(b.h) -> 2(a^T b + b^T a)
Qmat = sp.csr_matrix((10 * Ns, 10 * Ns))
for lam in range(4):
    for (mu, nu) in PAIRS:
        c = compidx(mu, nu)
        S_out, op = dop(H_CLASSES[c], lam)
        row = hmat_row([(c, 1.0, op)])
        mult = 1 if mu == nu else 2                   # off-diagonal appears twice in the tensor sum
        Qmat = Qmat + 0.25 * 2 * mult * (row.T @ row)
div_rows, tr_rows = [], []
for nu in range(4):
    terms = []; out_class = None
    for mu in range(4):
        c = compidx(mu, nu)
        S_out, op = dop(H_CLASSES[c], mu)
        if out_class is None: out_class = S_out
        assert S_out == out_class, 'R1 violated (divergence)'
        terms.append((c, 1.0, op))
    assert out_class == tuple(1 if k == nu else 0 for k in range(4))
    div_rows.append(hmat_row(terms))
    terms = []; oc2 = None
    for lam in range(4):
        c = compidx(lam, lam)
        S_out, op = dop(H_CLASSES[c], nu)
        if oc2 is None: oc2 = S_out
        assert S_out == oc2, 'R1 violated (trace gradient)'
        terms.append((c, 1.0, op))
    assert oc2 == out_class, 'R1 violated: div and trace gradient on different classes'
    tr_rows.append(hmat_row(terms))
for nu in range(4):
    dr, tr = div_rows[nu], tr_rows[nu]
    Qmat = Qmat + 0.25 * (-4 * (dr.T @ dr) + 2 * (dr.T @ tr + tr.T @ dr) - 2 * (tr.T @ tr))
Qmat = Qmat.tocsr()

# gauge generator D: xi -> h
Dmat_rows = {}
for (mu, nu) in PAIRS:
    c = compidx(mu, nu)
    # (D xi)_{mu nu} = d_mu xi_nu + d_nu xi_mu  (orthonormal coordinate scaling not used here: independent comps h_{mu nu})
    if mu == nu:
        S_out, op = dop(XI_CLASSES[mu], mu)
        assert S_out == H_CLASSES[c]
        Dmat_rows[(c, mu)] = 2.0 * op
    else:
        S1, op1 = dop(XI_CLASSES[nu], mu)
        S2, op2 = dop(XI_CLASSES[mu], nu)
        assert S1 == S2 == H_CLASSES[c], 'R1 violated (gauge)'
        Dmat_rows[(c, nu)] = op1
        Dmat_rows[(c, mu)] = op2
Dmat = block(Dmat_rows, 10, 4)
say(f'L={L}: sites/class = {Ns}, dim h = {10*Ns}, dim xi = {4*Ns}; R1: every term of every operator landed on a single class (asserted)')
say(f'R2 gauge invariance Q D = 0: max |Q D| = {abs(Qmat @ Dmat).max():.1e}')
say(f'   Q symmetric: {abs(Qmat - Qmat.T).max():.1e}')

# ---------------------------------------------------------------- R3 hypercubic group
def signed_perms(n):
    out = []
    for p in itertools.permutations(range(n)):
        for sg in itertools.product((1, -1), repeat=n):
            out.append((p, sg))
    return out
W4 = signed_perms(4)


def site_map(Sclass, p, sg):
    """local index permutation on a class: X -> X' with X'_{p[a]} = sg[a] * X_a (mod 2L); class S -> p(S)"""
    S_img = [0] * 4
    for a in range(4):
        S_img[p[a]] = Sclass[a]
    S_img = tuple(S_img)
    mp = np.empty(Ns, dtype=np.int64)
    for X, r in index[Sclass].items():
        Xn = [0] * 4
        for a in range(4):
            Xn[p[a]] = (sg[a] * X[a]) % N2
        mp[r] = index[S_img][tuple(Xn)]
    return S_img, mp


def tensor_action(p, sg):
    """Signed-permutation matrix P (10Ns x 10Ns) with (P h)_{comp'}(X') = s_mu s_nu h_comp(X), comp' = (p mu, p nu)."""
    rows, cols, vals = [], [], []
    for c, (mu, nu) in enumerate(PAIRS):
        S = H_CLASSES[c]
        S_img, mp = site_map(S, p, sg)
        c2 = compidx(p[mu], p[nu])
        assert H_CLASSES[c2] == S_img
        sgn = sg[mu] * sg[nu]
        rows.append(c2 * Ns + mp); cols.append(c * Ns + np.arange(Ns)); vals.append(np.full(Ns, float(sgn)))
    r = np.concatenate(rows); cc = np.concatenate(cols); v = np.concatenate(vals)
    return sp.csr_matrix((v, (r, cc)), shape=(10 * Ns, 10 * Ns))


def vector_action(p, sg):
    rows, cols, vals = [], [], []
    for m in range(4):
        S = XI_CLASSES[m]
        S_img, mp = site_map(S, p, sg)
        m2 = p[m]
        assert XI_CLASSES[m2] == S_img
        rows.append(m2 * Ns + mp); cols.append(m * Ns + np.arange(Ns)); vals.append(np.full(Ns, float(sg[m])))
    r = np.concatenate(rows); cc = np.concatenate(cols); v = np.concatenate(vals)
    return sp.csr_matrix((v, (r, cc)), shape=(4 * Ns, 4 * Ns))


worstQ = worstD = 0.0
for (p, sg) in W4:
    P = tensor_action(p, sg); Pv = vector_action(p, sg)
    worstQ = max(worstQ, abs(P.T @ Qmat @ P - Qmat).max())
    worstD = max(worstD, abs(P @ Dmat - Dmat @ Pv).max())
say(f'R3 W(B4) about a vertex, all {len(W4)} elements (tensor relabelling + coordinate map): max |P^T Q P - Q| = {worstQ:.1e}; max |P D - D P_xi| = {worstD:.1e}')

# ---------------------------------------------------------------- R4 spectrum
dimh = 10 * Ns
if dimh <= 7000:
    Qd = Qmat.toarray()
    w = np.linalg.eigvalsh(Qd)
    tol = 1e-9 * abs(w).max()
    nullity = int(np.sum(abs(w) < tol))
    Dd = Dmat.toarray()
    rankD = np.linalg.matrix_rank(Dd, tol=1e-9)
    say(f'R4 dim ker Q = {nullity};  rank D = {rankD};  ker Q - rank D = {nullity - rankD}  (expected 10 = the constant h at k=0; any more = doublers/extra modes)')
    say(f'   negative eigenvalues of Q: {int(np.sum(w < -tol))}  (Euclidean conformal-factor branch; expected = number of k != 0 modes = {Ns-1})')
    say(f'   positive eigenvalues: {int(np.sum(w > tol))} (expected 5 per k != 0 => {5*(Ns-1)})')

# ---------------------------------------------------------------- Bloch comparison with the symbol
import sympy as sps
# symbol K for independent coordinates h_{mu nu} (mu<=nu), tensor H_{mu nu}=H_{nu mu}=h
sy = sps.symbols('s1:5', real=True)
hh = sps.symbols('h0:10', real=True)
Hm = sps.zeros(4, 4)
for c, (i, j) in enumerate(PAIRS):
    Hm[i, j] = Hm[j, i] = hh[c]
sv = sps.Matrix(sy); s2 = sum(x ** 2 for x in sy); trH = Hm.trace(); Hs = Hm * sv
Qf = sps.Rational(1, 4) * (s2 * (Hm.T * Hm).trace() - 2 * (Hs.T * Hs)[0] + 2 * (sv.T * Hm * sv)[0] * trH - s2 * trH ** 2)
Ksym = sps.lambdify(sy, sps.hessian(sps.expand(Qf), hh), 'numpy')

# plane waves with TRUE positions x = X/2 (A-units), k in A-units
errB = 0.0
rng = np.random.default_rng(5)
ks = [2 * np.pi * np.array(n) / L for n in [(1, 0, 0, 0), (1, 1, 0, 0), (1, 2, 1, 3 % L), (2, 3 % L, 1, 1), (0, 0, 0, 1), (L // 2, L // 2, L // 2, L // 2)]]
for kk in ks:
    cols = []
    for c in range(10):
        v = np.zeros(10 * Ns, complex)
        for X, r in index[H_CLASSES[c]].items():
            v[c * Ns + r] = np.exp(1j * (np.array(X) / 2.0) @ kk)
        cols.append(v)
    Vv = np.array(cols).T
    Bk = (Vv.conj().T @ (Qmat @ Vv)) / Ns
    sn = 2 * np.sin(kk / 2)
    Ks = np.array(Ksym(*sn), float)
    errB = max(errB, abs(Bk - Ks).max())
say(f'R4b Bloch block (true-position phases) of the real-space Q vs symbolic symbol K(s): max |dev| = {errB:.1e}  (confirms half-shift convention and the Hessian bookkeeping)')

# ---------------------------------------------------------------- R5 cross-check with A25's 3D V (slice at fixed t)
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/test_K7a/ref')
import stag2
ops3 = stag2.build(L, 'stag')
V3 = ops3['Vp']                               # Hessian in independent coords (11,22,33,12,13,23) at spatial vertices
# our spatial block: take Q restricted to spatial comps (0..2 pairs), but with derivatives only along spatial directions.
# build the 3D-only energy by removing time-derivative pieces: compare the symbol-level via Bloch on the same grid instead
sp3 = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
idx_sp = [PAIRS.index(x) for x in sp3]
errV = 0.0
for kk in [2 * np.pi * np.array(n) / L for n in [(1, 0, 0), (1, 1, 0), (1, 2, 1), (2, 3 % L, 1)]]:
    k4 = np.array([kk[0], kk[1], kk[2], 0.0])
    s_ = 2 * np.sin(k4 / 2)
    Ks = np.array(Ksym(*s_), float)[np.ix_(idx_sp, idx_sp)]
    Vk = stag2.bloch(ops3['lat'], V3, stag2.H_OFF, stag2.H_OFF, kk[None, :])[0]
    # A25 potential V(h) = 1/2 h^T Vp h with the same normalization as 1/4 h:inc(h); ours: Q = 1/2 h^T K h
    errV = max(errV, abs(Vk - Ks).max())
say(f'R5 A25 real-space 3D V (stag2.build, L={L}) Bloch block vs spatial slice (s_4 = 0) of the 4D symbol: max |dev| = {errV:.1e}')
say(f'done in {time.time() - t0:.1f}s')
