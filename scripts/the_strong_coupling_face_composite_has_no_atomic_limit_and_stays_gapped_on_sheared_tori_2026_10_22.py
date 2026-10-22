#!/usr/bin/env python3
"""composite-band-3d: strong-coupling (g -> infinity) analysis of the far-rung cube-filtered pair square.
Question: in its symmetric phase, does the composite (three-fermion) band stay gapped at the zone faces X, M, R?
 A  exact: filter kernel and off-face span; sheared-torus reduction (the Gamma-X, Gamma-M, Gamma-R lines carry the exact
    3D filter cos^(2n)); overlapping terms do not commute (no atomic limit, composite moves at order g); mode-product identity
 B  exact identity + numerical optimisation: best mode-product states (Spin(10) and toy alike) break translations
 C  toy ED (supplied model: one SU(4)-singlet charge-4 quartic per cube, c1c2c3c4 + h.c., on the same filter; NOT Spin(10)):
    open cube clusters, sheared tori T_n (n = 1, 2, 3 -> X, M, R), face composite, propagator zero line with a free band
 D  why a strong-coupling cluster expansion cannot decide 3D (two-cube linked-cluster estimate vs exact 1D)
Self-contained (numpy/scipy/stdlib). Units: each filtered term normalised so a lone term (atom) has gap 1 (g' = g N^4)."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/THE_STRONG_COUPLING_FACE_COMPOSITE_HAS_NO_ATOMIC_LIMIT_AND_STAYS_GAPPED_ON_SHEARED_TORI_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 120
import itertools, os, time
from math import comb
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np, scipy.linalg as sl, scipy.sparse as sp, scipy.sparse.linalg as sla
T0 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ------------------------------------------------------------------ toy engine (four flavour copies of an n_m-mode Fock space)
class Flav:
    def __init__(s, nm):
        s.nm = nm; s.basis = {N: [m for m in range(1 << nm) if bin(m).count('1') == N] for N in range(nm + 1)}
        pos = {N: {m: i for i, m in enumerate(b)} for N, b in s.basis.items()}; s.ann = {}
        for N in range(1, nm + 1):
            mats = []
            for j in range(nm):
                r, c, v = [], [], []
                for i, m in enumerate(s.basis[N]):
                    if m >> j & 1: r.append(pos[N - 1][m ^ (1 << j)]); c.append(i); v.append((-1) ** bin(m & ((1 << j) - 1)).count('1'))
                mats.append(sp.csr_matrix((np.array(v, float), (r, c)), shape=(len(s.basis[N - 1]), len(s.basis[N]))))
            s.ann[N] = mats
    def dim(s, N): return len(s.basis[N]) if 0 <= N <= s.nm else 0
    def a(s, N, coef):
        out = None
        for cf, M in zip(coef, s.ann[N]):
            if abs(cf) > 1e-15: out = cf * M if out is None else out + cf * M
        return out.tocsr()
    def occ(s, N, w): return np.array([sum(w[j] for j in range(s.nm) if m >> j & 1) for m in s.basis[N]])
def kron_all(Ms):
    M = Ms[0]
    for m in Ms[1:]: M = sp.kron(M, m, format='csr')
    return M
class Model:   # H_int = -sum_x (C_x + C_x^+), C_x = c1(x)c2(x)c3(x)c4(x), c_f(x) = sum_j A[x,j] e_fj; class d: N_f = n + d_f
    def __init__(s, A): s.A = np.asarray(A); s.nt, s.nm = s.A.shape; s.F = Flav(s.nm); s.cls = {}
    def blocks(s, d):
        ns = list(range(-min(d), s.nm - max(d) + 1)); off = {}; o = 0
        for n in ns: off[n] = o; o += int(np.prod([s.F.dim(n + x) for x in d]))
        return ns, off, o
    def _pat(s, N):   # annihilation pattern N -> N-1 of one flavour: (row, col, JW sign, mode); one mode per entry
        pat = s.F.__dict__.setdefault('pat', {})
        if N not in pat:
            cs = [M.tocoo() for M in s.F.ann[N]]
            pat[N] = tuple(np.concatenate(z) for z in ([c.row for c in cs], [c.col for c in cs], [c.data for c in cs], [np.full(c.nnz, j) for j, c in enumerate(cs)]))
        return pat[N]
    def _asm(s, d, xs):   # H = -(C + C^+), C = sum_x C_x maps class block n -> n - 1; only C is stored (HOp applies H)
        xs = list(xs); T = np.einsum('xa,xb,xc,xd->abcd', *[s.A[xs]] * 4)   # T = sum_x prod_f A_x,j_f: kron entries are JW signs * T
        ns, off, D = s.blocks(d); sh = lambda f, a: a.reshape([-1 if g == f else 1 for g in range(4)])
        todo = [(n, [s._pat(n + df) for df in d]) for n in ns if n - 1 in off]
        nnz = sum(int(np.prod([len(p[0]) for p in P])) for _, P in todo)
        R = np.empty(nnz, np.int32); Cc = np.empty(nnz, np.int32); V = np.empty(nnz, T.dtype); o = 0
        for n, P in todo:
            Do = [s.F.dim(n + df - 1) for df in d]; Di = [s.F.dim(n + df) for df in d]; k = int(np.prod([len(p[0]) for p in P]))
            R[o:o + k] = sum(sh(f, P[f][0]) * int(np.prod(Do[f + 1:])) for f in range(4)).ravel() + off[n - 1]
            Cc[o:o + k] = sum(sh(f, P[f][1]) * int(np.prod(Di[f + 1:])) for f in range(4)).ravel() + off[n]
            sg = (-1) ** (2 * n + d[0] + d[2]) * sh(0, P[0][2]) * sh(1, P[1][2]) * sh(2, P[2][2]) * sh(3, P[3][2])
            V[o:o + k] = (sg * T[sh(0, P[0][3]), sh(1, P[1][3]), sh(2, P[2][3]), sh(3, P[3][3])]).ravel(); o += k; del sg
        C = sp.coo_matrix((V, (R, Cc)), shape=(D, D)); del R, Cc, V
        return HOp(C.tocsr())
    def H(s, d):
        if d not in s.cls: s.cls[d] = s._asm(d, range(s.nt))
        return s.cls[d]
    def term(s, d, x): return s._asm(d, [x])
    def diag(s, d, w):   # sum_f sum_j w_j (n_fj - 1/2), or momentum label with w = ks (integers) when mod is given
        ns, off, D = s.blocks(d); out = np.zeros(D)
        for n in ns:
            t = s.F.occ(n + d[0], w)
            for df in d[1:]: t = (t[:, None] + s.F.occ(n + df, w)[None, :]).ravel()
            out[off[n]:off[n] + len(t)] = t
        return out
    def _place(s, d_from, d_to, bl):
        _, offf, Df = s.blocks(d_from); _, offt, Dt = s.blocks(d_to); R, Cc, V = [], [], []
        for n, occ, M in bl:
            nt = occ[0] - d_to[0]
            if [nt + x for x in d_to] != list(occ) or nt not in offt: continue
            M = M.tocoo(); R.append(M.row + offt[nt]); Cc.append(M.col + offf[n]); V.append(M.data.astype(complex))
        return sp.csr_matrix((np.concatenate(V), (np.concatenate(R), np.concatenate(Cc))), shape=(Dt, Df))
    def e1(s, d_from, d_to, k, dag=False):   # annihilate / create flavour-1 mode k
        bl = []
        for n in s.blocks(d_from)[0]:
            N1 = n + d_from[0]
            if (not dag and N1 < 1) or (dag and N1 >= s.nm): continue
            M1 = s.F.ann[N1][k] if not dag else s.F.ann[N1 + 1][k].T.tocsr()
            bl.append((n, [N1 + (1 if dag else -1)] + [n + df for df in d_from[1:]],
                       kron_all([M1] + [sp.identity(s.F.dim(n + df), format='csr') for df in d_from[1:]])))
        return s._place(d_from, d_to, bl)
    def Dop(s, d_from, d_to, coefs):   # sum_x coefs_x D_x, D_x = c4^+ c3^+ c2^+(x): [e_1k, H_int] = sum_x conj(A_xk) D_x
        bl = []
        for n in s.blocks(d_from)[0]:
            occ = [n + d_from[0]] + [n + df + 1 for df in d_from[1:]]
            if max(occ) > s.nm: continue
            M = None
            for x, cf in enumerate(coefs):
                if abs(cf) < 1e-15: continue
                Mx = kron_all([sp.identity(s.F.dim(occ[0]), format='csr')] + [s.F.a(n + df + 1, np.conj(s.A[x])).T.tocsr() for df in d_from[1:]])
                M = cf * Mx if M is None else M + cf * Mx
            bl.append((n, occ, (-1) ** (2 * n + d_from[0] + d_from[2] + 1) * M))
        return s._place(d_from, d_to, bl)
class HOp:   # Hermitian H = -(C + C^+) + diag(d), applied from the stored half C (memory: one half, no summed copy)
    def __init__(s, C, d=None): s.C = C; s.d = d; s.shape = C.shape; s.dtype = np.result_type(C.dtype, np.float64)
    def __matmul__(s, x):
        y = -(s.C @ x) - (s.C.T @ x.conj()).conj()
        return y + s.d * x if s.d is not None else y
    def full(s): F = -(s.C + s.C.conj().T).tocsr(); return F + sp.diags(s.d) if s.d is not None else F
    def toarray(s): return s.full().toarray()
    def shift(s, d): return HOp(s.C, d)
    def sector(s, ii, d=None): return HOp(s.C[ii][:, ii].tocsr(), d)
def lowest(H, k=2):
    if H.shape[0] <= 2000: return sl.eigh(H.toarray(), subset_by_index=[0, k - 1], driver='evr', overwrite_a=True)   # O(n) workspace
    Lo = sla.LinearOperator(H.shape, matvec=lambda x: H @ x, dtype=H.dtype)
    e, v = sla.eigsh(Lo, k=k, which='SA', tol=1e-10, v0=np.ones(H.shape[0])); o = np.argsort(e); return e[o], v[:, o]
def poles(H, v, m=70):   # Lanczos with full reorthogonalisation; T_ij = <q_i|H|q_j> accumulated column by column
    nv = np.linalg.norm(v)
    if H.shape[0] <= 2000: e, U = sl.eigh(H.toarray(), driver='evr', overwrite_a=True); return e, np.abs(U.conj().T @ v) ** 2
    Q = [v / nv]; HQ = []
    for it in range(m + 1):
        w = H @ Q[-1]; HQ.append(np.array([np.vdot(q, w) for q in Q]))
        if it == m: break
        for _ in range(2):
            for q in Q: w = w - np.vdot(q, w) * q
        b = np.linalg.norm(w)
        if b < 1e-9: break
        Q.append(w / b)
    if len(HQ) < len(Q): w = H @ Q[-1]; HQ.append(np.array([np.vdot(q, w) for q in Q]))
    k = len(Q); T = np.zeros((k, k), complex)
    for j, col in enumerate(HQ): T[:j + 1, j] = col; T[j, :j] = np.conj(col[:j])
    e, U = np.linalg.eigh((T + T.conj().T) / 2); proj = np.array([np.vdot(q, v) for q in Q]); del Q, HQ
    return e, np.abs(U.conj().T @ proj) ** 2
def zeros_in(ep, wp, eh, wh, lo, hi, n=4001):
    ws = np.linspace(lo + 1e-4 * (hi - lo), hi - 1e-4 * (hi - lo), n)
    G = (wp / (ws[:, None] - ep)).sum(1) + (wh / (ws[:, None] + eh)).sum(1); return ws[np.nonzero(np.diff(np.sign(G)))[0]]
def gram_open(cubes):
    c = np.array(cubes); return np.array([[0.0 if np.abs(a - b).max() > 1 else np.prod([1.0 if x == 0 else 0.5 for x in np.abs(a - b)]) for b in c] for a in c])
def sqrt_psd(K): w, V = np.linalg.eigh(K); return (V * np.sqrt(np.clip(w, 0, None))) @ V.T
def sheared(L, n):   # torus Z^3/Lambda_n: s = x_1+..+x_n mod L, remaining directions identified; filter (1+e^iq)^n, face q = pi
    ms = [m for m in range(L) if 2 * m != L]
    return np.array([[np.exp(2j * np.pi * m * x / L) * (1 + np.exp(2j * np.pi * m / L)) ** n / np.sqrt(L * comb(2 * n, n)) for m in ms] for x in range(L)]), ms
Z, HO, PA = (0, 0, 0, 0), (0, 1, 1, 1), (1, 0, 0, 0)

# ================================================================== A
print('== A. exact structure of the g -> infinity problem')
def cube_matrix(Ls):   # columns: cube-average vectors (1/sqrt 8) on an L1 x L2 x L3 torus
    S = list(itertools.product(*[range(L) for L in Ls])); idx = {s: i for i, s in enumerate(S)}; C = np.zeros((len(S), len(S)))
    for y, s in enumerate(S):
        for c in itertools.product((0, 1), repeat=3): C[idx[tuple((a + b) % L for a, b, L in zip(s, c, Ls))], y] += 1
    return C / np.sqrt(8), S, idx
ranks = {}; kern_ok = True
for L in (4, 6):
    C, S, idx = cube_matrix((L, L, L)); K = C.T @ C; ranks[L] = np.linalg.matrix_rank(K, tol=1e-9)
    d = np.array(S); dd = np.minimum(d % L, (-d) % L)
    kern_ok &= np.allclose(K[0], np.where(dd.max(1) <= 1, 0.5 ** (dd == 1).sum(1), 0))
check('A1 THEOREM c_x = sqrt8 b~_x: {c_x, c_y^+} = prod_i (1, 1/2, 0)[|x_i - y_i|]; on L^3 they span exactly the (L-1)^3 '
      'off-face momenta: H_int lives there, face modes are free spectators', kern_ok and ranks == {4: 27, 6: 125}, 'rank ' + ', '.join(f'L={k}: {int(v)}' for k, v in ranks.items()) + ' = (L-1)^3')
ok = True; info = []
for n in (1, 2, 3):
    L = 6; Lam = np.array([[1, -1, 0], [0, 1, -1], [L, 0, 0]]) if n == 3 else (np.array([[1, -1, 0], [0, 0, 1], [L, 0, 0]]) if n == 2 else np.array([[L, 0, 0], [0, 1, 0], [0, 0, 1]]))
    w = np.zeros(L)
    for c in itertools.product((0, 1), repeat=3): w[sum(c[:n]) % L] += 1 / 8   # b~ on the quotient: class of x + c is s + c_1 + .. + c_n
    face = np.full(3, np.pi); face[n:] = 0
    ok &= abs(abs(np.linalg.det(Lam)) - L) < 1e-9 and np.allclose(np.exp(1j * Lam @ face), 1) and np.allclose(w[:n + 1], [comb(n, j) / 2 ** n for j in range(n + 1)])
    q = np.pi - 1e-3; ok &= abs(abs(np.sum(w * np.exp(1j * q * np.arange(L)))) / abs(np.cos(q / 2)) ** n - 1) < 1e-6
    info.append(f"n={n}: weights {np.round(w[:n + 1] * 2 ** n).astype(int).tolist()}/2^{n}")
check('A2 THEOREM sheared tori T_n = Z^3/Lambda_n (det L) carry only (q,0,0), (q,q,0), (q,q,q) (n = 1, 2, 3): the cube filter '
      'becomes ((1+e^iq)/2)^n, faces X, M, R at q = pi with the exact 3D zero order cos^(2n). '
      'Legitimate 3D tori, transverse size one cell (no transverse coordination)', ok, '; '.join(info))
# engine cross-check on the NN pair: union of class spectra = dense Fock spectrum (independent Jordan-Wigner build)
A2 = sqrt_psd(gram_open([(0, 0, 0), (1, 0, 0)])); nmod = 8; Df = 1 << nmod
def jw(p):
    r, c, v = [], [], []
    for st in range(Df):
        if st >> p & 1: r.append(st ^ (1 << p)); c.append(st); v.append((-1) ** bin(st & ((1 << p) - 1)).count('1'))
    return sp.csr_matrix((np.array(v, float), (r, c)), shape=(Df, Df))
ann = [jw(p) for p in range(nmod)]; Hd = sp.csr_matrix((Df, Df)); terms = []
for x in range(2):
    cf = [sum(A2[x, j] * ann[f * 2 + j] for j in range(2)) for f in range(4)]; Cx = cf[0] @ cf[1] @ cf[2] @ cf[3]; terms.append(-(Cx + Cx.T)); Hd = Hd + terms[-1]
ed = np.sort(np.linalg.eigvalsh(Hd.toarray())); M2 = Model(A2); allc = []
for d in itertools.product(range(3), repeat=4):
    if min(d) == 0 and M2.blocks(d)[2] > 0: allc += list(np.linalg.eigvalsh(M2.H(d).toarray()))
comm = {}
for dvec in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0)):
    Mx = Model(sqrt_psd(gram_open([(0, 0, 0), dvec]))); h0 = Mx.term(Z, 0).toarray(); h1 = Mx.term(Z, 1).toarray()
    comm[dvec] = (np.linalg.norm(h0 @ h1 - h1 @ h0, 2), lowest(Mx.H(Z), 1)[0][0] / 2)
c_dense = np.linalg.norm((terms[0] @ terms[1] - terms[1] @ terms[0]).toarray(), 2)
check('A3 THEOREM (toy, exact) overlapping filtered terms do not commute: ||[h_x, h_y]|| = 0.866, 0.484, 0.248 for overlaps 1/2, '
      '1/4, 1/8 (0 for disjoint cubes); a two-term cluster cannot reach 2 E_atom (energy per term -0.901, -0.970, -0.992). So the '
      'g -> infinity limit has no atomic form: the composite moves at order g via the overlap, not at t^n/g^(n-1). '
      'Engine = dense Jordan-Wigner spectrum (256 states)',
      np.allclose(np.sort(allc), ed, atol=1e-10) and abs(c_dense - comm[(1, 0, 0)][0]) < 1e-10
      and np.allclose([comm[k][0] for k in comm], [0.8660254, 0.4841229, 0.2480392, 0.0], atol=1e-6)
      and np.allclose([comm[k][1] for k in comm], [-0.90139, -0.97026, -0.99228, -1.0], atol=1e-4),
      'norms ' + ', '.join(f'{v[0]:.3f}' for v in comm.values()) + '; E/term ' + ', '.join(f'{v[1]:.3f}' for v in comm.values()))
Ar, msr = sheared(4, 1); Mr = Model(Ar); errs = 0.0
for j in range(len(msr)):
    lhs = Mr.e1(Z, HO, j) @ Mr.H(Z).full() - Mr.H(HO).full() @ Mr.e1(Z, HO, j); rhs = Mr.Dop(Z, HO, np.conj(Ar[:, j])); errs = max(errs, abs(lhs - rhs).max())
check('A4 THEOREM [e_k, H_int] = sum_x conj(A_xk) D_x (D_x three-fermion, A_xk ~ f(k) e^ikx): D(face) is nonzero and its '
      'propagator is exactly the kernel Sigma/|f|^2', errs < 1e-12, 'identity error below 1e-12 (T_1, L = 4)')

# ================================================================== B
print('== B. mode-product states: <h(c_y)> = e_atom * sum_m beta_m(y)^4 (exact for any charge-4-only quartic, Spin(10) included)')
rng = np.random.default_rng(3); U = np.linalg.qr(rng.normal(size=(2, 2)))[0]; beta = U.T @ A2.T   # modes e' = U^T e
psi = np.zeros(Df); psi[0] = 1.0
for m in range(2):
    cre = [sum(U[j, m] * ann[f * 2 + j] for j in range(2)).T for f in range(4)]
    Qd = cre[0] @ cre[1] @ cre[2] @ cre[3]; psi = (psi + Qd @ psi) / np.sqrt(2)
lhs = [psi @ (terms[x] @ psi) for x in range(2)]; rhs = [-np.sum(beta[:, x] ** 4) for x in range(2)]
def cubes1(L, dim):
    S = list(itertools.product(range(L), repeat=dim)); idx = {s: i for i, s in enumerate(S)}; C = np.zeros((len(S),) * 2)
    for y, s in enumerate(S):
        for c in itertools.product((0, 1), repeat=dim): C[idx[tuple((a + b) % L for a, b in zip(s, c))], y] += 1
    return C / np.sqrt(2 ** dim), S, idx
def hadamard(L, dim, S, idx):
    U = np.zeros((len(S),) * 2); col = 0
    for blk in itertools.product(range(0, L, 2), repeat=dim):
        for nn in itertools.product((0, 1), repeat=dim):
            for c in itertools.product((0, 1), repeat=dim): U[idx[tuple(b + x for b, x in zip(blk, c))], col] = (-1) ** int(np.dot(nn, c)) / np.sqrt(2 ** dim)
            col += 1
    return U
def gpa(U, C, it=300):
    for _ in range(it):
        G = C @ ((U.T @ C) ** 3).T; W, _, Vt = np.linalg.svd(G); U = W @ Vt
    return U
phi = lambda U, C: np.sum((U.T @ C) ** 4, 0)
prod = {}
for L, dim in ((8, 1), (4, 3)):
    C, S, idx = cubes1(L, dim); N = len(S); best = None
    for U0 in [np.eye(N), hadamard(L, dim, S, idx)] + [np.linalg.qr(rng.normal(size=(N, N)))[0] for _ in range(3)]:
        py = phi(gpa(U0, C), C)
        if best is None or py.mean() > best.mean(): best = py
    prod[dim] = (phi(np.eye(N), C).mean(), phi(hadamard(L, dim, S, idx), C).mean(), best.mean(), best.std())
check('B1 THEOREM + DIAGNOSTIC per-mode atomic singlets: cross-mode terms vanish by Z4, E/term = e_atom sum beta^4; site '
      'product 1/2^d, cube solid (5/4)^d/2^d; the best product (quartimax) is non-uniform: products favour translation '
      'breaking, more in 3D (best/site 2.9 vs 1.4)',
      np.allclose(lhs, rhs, atol=1e-12) and np.allclose([prod[1][0], prod[1][1], prod[3][0], prod[3][1]], [0.5, 0.625, 0.125, (5 / 4) ** 3 / 8])
      and prod[3][2] > prod[3][1] and prod[1][3] > 0.05 and prod[3][3] > 0.05,
      f"identity err below 1e-12; 1D ring 8: site {prod[1][0]:.3f}, solid {prod[1][1]:.3f}, best {prod[1][2]:.3f} "
      f"(std {prod[1][3]:.2f}); 3D 4^3: site {prod[3][0]:.3f}, solid {prod[3][1]:.3f}, best {prod[3][2]:.3f} (std {prod[3][3]:.2f})")

# ================================================================== C
print(f'== C. toy ED of H_int (g -> infinity, t = 0 unless stated)  [t = {time.time() - T0:.0f} s]')
clusters = {'line3': [(i, 0, 0) for i in range(3)], 'line5': [(i, 0, 0) for i in range(5)], 'plate2x2': [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)],
            'tripod4': [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)], 'tet4': [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)],
            'cube5': [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1)], 'star3d5': [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]}
rows = []; okC = True
for nm, cl in clusters.items():
    A = sqrt_psd(gram_open(cl)); M = Model(A); e, v = lowest(M.H(Z), 2); gs = v[:, 0]; M.cls.clear()
    Up = A.T; best = 0.0                     # best mode product on the cluster's own mode space (columns = cubes)
    for U0 in [np.eye(len(cl))] + [np.linalg.qr(rng.normal(size=(len(cl),) * 2))[0] for _ in range(3)]:
        best = max(best, phi(gpa(U0, Up, 200), Up).mean())
    sg = {'G': np.ones(len(cl))}
    for k_, P_ in (('X', (1, 0, 0)), ('M', (1, 1, 0)), ('R', (1, 1, 1))):
        s_ = np.array([(-1) ** int(np.dot(P_, c)) for c in cl], float)
        if len(set(s_)) > 1: sg[k_] = s_
    low = {}
    for k_, s_ in sg.items():
        ee, wt = poles(M.H(HO), M.Dop(Z, HO, s_.astype(complex)) @ gs); sel = wt > 0.02 * wt.sum(); low[k_] = ee[sel][0] - e[0]
    low['F'] = min(v for k_, v in low.items() if k_ != 'G')
    rows.append(f"{nm} {e[0] / len(cl):.3f}/{-best:.3f} {e[1] - e[0]:.2f} {low['G']:.2f} {low['F']:.2f}")
    okC &= e[1] - e[0] > 0.1 and -1.10 * best < e[0] / len(cl) < -1.002 * best and low['F'] < low['G']
check('C1 FINITE DIAGNOSTIC open clusters (<= 5 cubes, 1D-3D): unique ground state (gap > 0.1), exact E/term only 0.3-9% below '
      'the best mode product, and the face-signed composite lies below the uniform one (open clusters do not separate it from '
      'the soft near-face elementary)', okC, '; '.join(rows))
print('   format: E/term exact/best product; neutral gap; lowest composite pole, uniform and face-signed (-1)^(P.x)')
res = {}; c5 = None
for n in (1, 2, 3):   # one torus at a time; each Fock class is built, used for every mass, then freed
    for L in (4, 6):
        A, ms = sheared(L, n); M = Model(A); ks = [2 * np.pi * m / L for m in ms]; masses = (0.0, 0.25) if L == 6 else (0.0,)
        hks = {mass: [mass * (1 - np.cos(k)) / 2 for k in ks] for mass in masses}; st = {}
        mom0 = M.diag(Z, ms) % L; H0 = M._asm(Z, range(M.nt)); secs = [np.nonzero(mom0 == K)[0] for K in range(L)]
        blk = [H0.sector(ii) for ii in secs]; DZ = H0.shape[0]; del H0
        for mass in masses:   # ground state in fixed-momentum sectors
            dz = M.diag(Z, hks[mass]); lev = []
            for K, ii in enumerate(secs):
                Hs = blk[K].shift(dz[ii]) if mass else blk[K]; e, v = lowest(Hs, 2); lev += [(x, K, ii, v[:, j]) for j, x in enumerate(e)]
            lev.sort(key=lambda z: z[0]); E0, K0, ii, v0 = lev[0]; gs = np.zeros(DZ, complex); gs[ii] = v0
            st[mass] = dict(E0=E0, K0=K0, gap=lev[1][0] - E0, gs=gs)
        del blk, lev
        if n == 1 and L == 6:   # C5 on the 6-ring: one filtered term at a time, keep only h_x|GS>
            g6 = st[0.0]['gs']; u = []
            for x in range(L): hx = M.term(Z, x); u.append(hx @ g6); del hx
            ev = [np.vdot(g6, ux).real for ux in u]; c5 = (ev, [np.vdot(u[0], u[d]).real - ev[0] * ev[d] for d in (1, 2, 3)]); del u
        Hh = M._asm(HO, range(M.nt))
        for mass in masses:
            S = st[mass]; gs = S['gs']; E0 = S['E0']; Hm = Hh.shift(M.diag(HO, hks[mass])) if mass else Hh
            ee, wt = poles(Hm, M.Dop(Z, HO, np.exp(-1j * np.pi * np.arange(L)) / np.sqrt(L)) @ gs); ee = ee - E0; tot = wt.sum()
            S['r'] = dict(E0=E0 / L, K0=S['K0'], gap=S['gap'], Dlow=ee[wt > 0.02 * tot][0], Dmean=float(np.sum(ee * wt) / tot), Dw05=float(wt[ee < 0.5].sum() / tot), n2=tot)
            if L == 6: S['h'] = [poles(Hm, M.e1(Z, HO, j) @ gs) for j in range(len(ms))]
        del Hh, Hm
        if L == 6:
            Hp = M._asm(PA, range(M.nt))
            for mass in masses:
                S = st[mass]; gs = S['gs']; E0 = S['E0']; Hm = Hp.shift(M.diag(PA, hks[mass])) if mass else Hp; zl = []; eps = []
                for j in range(len(ms)):
                    ep, wp = poles(Hm, M.e1(Z, PA, j, dag=True) @ gs); eh, wh = S['h'][j]; ep = ep - E0; eh = eh - E0
                    a = wp > 1e-7; b = wh > 1e-7; zs = zeros_in(ep[a], wp[a], eh[b], wh[b], -eh[b].min(), ep[a].min())
                    zl.append(zs[0] if len(zs) else np.nan); eps.append(ep[a][np.argmax(wp[a])])
                S['r']['zero'] = zl; S['r']['eps'] = eps; S['r']['f2'] = [np.cos(k / 2) ** (2 * n) for k in ks]
            del Hp, Hm
        for mass in masses: res[n, L, mass] = st[mass]['r']
        del st, M
print(f'   [t = {time.time() - T0:.0f} s]')
for n, lab in ((1, 'X'), (2, 'M'), (3, 'R')):
    a, b, c = res[n, 4, 0.0], res[n, 6, 0.0], res[n, 6, 0.25]
    print(f"   T_{n} ({lab}): E0/term {a['E0']:.3f}, {b['E0']:.3f}; K0 {a['K0']},{b['K0']}; neutral gap L4 {a['gap']:.3f} L6 {b['gap']:.3f} (free band m=0.25: {c['gap']:.3f}); "
          f"D({lab}) lowest/mean L4 {a['Dlow']:.2f}/{a['Dmean']:.2f}, L6 {b['Dlow']:.2f}/{b['Dmean']:.2f}, m=0.25 {c['Dlow']:.2f}/{c['Dmean']:.2f}; "
          f"zero line q=0,pi/3,2pi/3 at m=0.25: {np.round(c['zero'][:3], 2).tolist()}")
check('C2 FINITE DIAGNOSTIC T_1, T_2, T_3 (L = 4, 6): D(face)|GS> has no weight below 0.5 and its lowest pole is 0.9-2.3 '
      '(atom units) at X, M and R, with and without a face-gapped free band: no flattening on these tori',
      all(r['Dw05'] < 1e-12 and r['Dlow'] > 0.85 for r in res.values()) and all(r['K0'] == 0 for r in res.values()),
      'weight below 0.5: below 1e-12 on every torus; D norm^2 at the face T_1..T_3 (L=6) '
      + ', '.join(f"{res[n, 6, 0.0]['n2']:.3f}" for n in (1, 2, 3)))
r1 = res[1, 6, 0.0]; ratio = np.array(r1['eps']) / np.array(r1['f2'])
soft = [res[n, 6, 0.0]['eps'][2] for n in (1, 2, 3)]
check('C3 FINITE DIAGNOSTIC t = 0 is singular at the faces: eps(q) ~ c|f(q)|^2 (c 1.4-1.6) vanishes there (near-face modes '
      'almost free, softer for higher n), T_3 neutral gap is near-face pairs, every t = 0 zero is pinned at w = 0 (PH x inversion). '
      'The shell g|f|^2 < t around each face is weakly coupled at any g',
      np.all((ratio > 1.3) & (ratio < 1.7)) and soft[0] > soft[1] > soft[2] and res[3, 6, 0.0]['gap'] < 0.05 < res[3, 6, 0.25]['gap']
      and all(abs(z) < 5e-3 for n in (1, 2, 3) for z in res[n, 6, 0.0]['zero']),
      f"eps/|f|^2 (T_1) {np.round(ratio, 2).tolist()}; eps(2pi/3) T_1..T_3 {np.round(soft, 3).tolist()}; T_3 gap t=0 {res[3, 6, 0.0]['gap']:.3f} -> {res[3, 6, 0.25]['gap']:.3f}")
zz = [res[n, 6, 0.25]['zero'] for n in (1, 2, 3)]
check('C4 FINITE DIAGNOSTIC free band h = 0.25(1 - cos q)/2: the zero leaves w = 0 and moves monotonically away toward the '
      'face (or leaves the window): it disperses into the gapped face composite on all three lines',
      all(abs(z[0]) < abs(z[1]) and (np.isnan(z[2]) or abs(z[2]) > abs(z[1])) for z in zz),
      '; '.join(f"T_{n}: {np.round(z[:3], 3).tolist()}" for n, z in zip((1, 2, 3), zz)))
ev, cc = c5   # computed in the torus loop from the T_1, L = 6 ground state (h_x Hermitian: <h_0 h_d> = <h_0 GS|h_d GS>)
check('C5 FINITE DIAGNOSTIC 6-ring T_1: unique K = 0 ground state, uniform <h_x>, connected <h_0 h_d> decays without period-2 '
      'alternation: no cube solid',
      np.allclose(ev, ev[0]) and abs(cc[2]) < abs(cc[0]) and res[1, 6, 0.0]['gap'] > 0.3, f"<h> {ev[0]:.3f}; C(d=1,2,3) {np.round(cc, 4).tolist()}")

# ================================================================== D
print('== D. can a strong-coupling cluster expansion decide 3D?')
pair = {}
for dvec in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
    Mx = Model(sqrt_psd(gram_open([(0, 0, 0), dvec]))); e, v = lowest(Mx.H(Z), 1); out = []
    for sgn in (1, -1):
        ee, wt = poles(Mx.H(HO), Mx.Dop(Z, HO, np.array([1, sgn], complex)) @ v[:, 0]); out.append(ee[wt > 0.02 * wt.sum()][0] - e[0])
    pair[dvec] = ((out[0] + out[1]) / 2 - 1.0, (out[0] - out[1]) / 2)
nb = [d for d in itertools.product((-1, 0, 1), repeat=3) if any(d)]
lc = lambda Q: 1.0 + sum(pair[tuple(sorted(np.abs(d), reverse=True))][0] + pair[tuple(sorted(np.abs(d), reverse=True))][1] * np.cos(np.dot(Q, d)) for d in nb)
P = {'G': (0, 0, 0), 'X': (np.pi, 0, 0), 'M': (np.pi, np.pi, 0), 'R': (np.pi,) * 3}; est = {k: lc(np.array(q, float)) for k, q in P.items()}
est1 = 1.0 + 2 * (pair[(1, 0, 0)][0] - pair[(1, 0, 0)][1])
check('D1 DIAGNOSTIC (negative for the method) two-cube linked-cluster band puts the 3D composite below zero at X, M, R, but '
      'in 1D it predicts ~0 where the exact ring gives 1.01: overlap 1/2 is not small, so 3D is not decided here', all(est[k] < 0 for k in 'XMR') and abs(est1) < 0.1 and res[1, 6, 0.0]['Dlow'] > 0.9,
      'est ' + ', '.join(f'{k} {v:+.2f}' for k, v in est.items()) + f'; 1D est {est1:+.2f} vs exact {res[1, 6, 0.0]["Dlow"]:.2f}')
print('supplied: toy content (4 modes, SU(4)-singlet quartic, not Spin(10)), sizes, tori T_n, free band h, atom units; '
      'Spin(10)-general: A1, A2, A4, B1 identity')
print('cited: collective-spin10 B2/B3/C4, filtered-smg-1d A3/C4/C5, zeros-ghosts')
print(f'elapsed {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
