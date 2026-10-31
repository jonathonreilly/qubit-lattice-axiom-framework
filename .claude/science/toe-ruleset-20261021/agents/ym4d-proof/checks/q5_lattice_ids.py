"""q5: lattice identities for SQ.md section 15 (session 4): TPL, BIA, WB, NREFL, GARSIA.
Criteria: checks/q5_criteria.md (written before this script). SU(2) throughout."""
import itertools
import numpy as np

rng = np.random.default_rng(20261028 + 5)
N = 2
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
EB = [1j * s / np.sqrt(2) for s in SIG]          # orthonormal basis of su(2) for <A,B> = Re tr(A^dag B)
I2 = np.eye(2, dtype=complex)
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
TRIPLES = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
RES = {}


def expm_su2(X):
    # X anti-Hermitian traceless 2x2: exp via closed form
    a = np.sqrt(np.maximum(-np.real(np.einsum('...ij,...ji->...', X, X)) / 2, 0.0))
    a = a[..., None, None]
    with np.errstate(invalid='ignore', divide='ignore'):
        f = np.where(a > 1e-300, np.sin(a) / np.where(a > 1e-300, a, 1.0), 1.0)
    return np.cos(a) * I2 + f * X


def coords(X):
    return np.stack([np.real(np.einsum('ij,...ij->...', b.conj(), X)) for b in EB], axis=-1)


def from_coords(c):
    return np.einsum('...a,aij->...ij', c, np.array(EB))


def dag(U):
    return np.conj(np.swapaxes(U, -1, -2))


def mm(A, B):
    return np.einsum('...ij,...jk->...ik', A, B)


def adR(U):
    """rotation matrix of Ad_U in the basis EB: R_ab = Re tr(e_a^dag U e_b U^dag)"""
    out = np.zeros(U.shape[:-2] + (3, 3))
    for b in range(3):
        Y = mm(mm(U, EB[b]), dag(U))
        out[..., :, b] = coords(Y)
    return out


def rand_field(S, eta):
    U = []
    for mu in range(4):
        c = rng.normal(size=tuple(S) + (3,))
        c /= np.linalg.norm(c, axis=-1, keepdims=True)
        c *= np.sqrt(2) * rng.uniform(0.3, 1.0, size=tuple(S) + (1,))   # |X_b|_op = |c|/sqrt2 = uniform(0.3, 1)
        U.append(expm_su2(eta * from_coords(c)))
    return U


def haar_su2(shape):
    q = rng.normal(size=tuple(shape) + (4,))
    q /= np.linalg.norm(q, axis=-1, keepdims=True)
    a, b, c, d = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    M = np.empty(tuple(shape) + (2, 2), complex)
    M[..., 0, 0] = a + 1j * b; M[..., 0, 1] = c + 1j * d
    M[..., 1, 0] = -c + 1j * d; M[..., 1, 1] = a - 1j * b
    return M


def gauge(U, g):
    return [mm(mm(g, U[mu]), dag(np.roll(g, -1, axis=mu))) for mu in range(4)]


def sh(f, lam, axoff=0):
    """f(x + e_lam) on the torus"""
    return np.roll(f, -1, axis=axoff + lam)


def plaq(U, mu, nu):
    return mm(mm(U[mu], sh(U[nu], mu)), mm(dag(sh(U[mu], nu)), dag(U[nu])))


def pfield(W):
    A = (W - dag(W)) / 2
    tr = np.einsum('...ii->...', A) / N
    return A - tr[..., None, None] * I2


def opnorm1m(W):
    return np.linalg.norm(I2 - W, ord=2, axis=(-2, -1))


# ---------------- operators on coordinate fields with a leading batch axis ----------------
def build_ops(U, S):
    R = [adR(U[mu]) for mu in range(4)]          # shape S+(3,3)
    V = int(np.prod(S))

    def ad(lam, f):  # Ad_{U(x,lam)} f(x+e_lam); f has shape (B,)+S+(3,)
        return np.einsum('...ab,B...b->B...a', R[lam], sh(f, lam, 1))

    def D1(al):  # al: (B,)+S+(4,3) -> (B,)+S+(6,3)
        out = []
        for (mu, nu) in PAIRS:
            out.append(al[..., mu, :] + ad(mu, al[..., nu, :]) - ad(nu, al[..., mu, :]) - al[..., nu, :])
        return np.stack(out, axis=-2)

    def D2(u):  # u: (B,)+S+(6,3) -> (B,)+S+(4,3)
        idx = {p: i for i, p in enumerate(PAIRS)}
        out = []
        for (l, m, n) in TRIPLES:
            t = (ad(l, u[..., idx[(m, n)], :]) - u[..., idx[(m, n)], :]) \
                - (ad(m, u[..., idx[(l, n)], :]) - u[..., idx[(l, n)], :]) \
                + (ad(n, u[..., idx[(l, m)], :]) - u[..., idx[(l, m)], :])
            out.append(t)
        return np.stack(out, axis=-2)

    def nab(lam, u):  # (B,)+S+(6,3)
        return np.stack([ad(lam, u[..., i, :]) - u[..., i, :] for i in range(6)], axis=-2)

    def mat(op, din_shape):
        dim = V * int(np.prod(din_shape))
        E = np.eye(dim).reshape((dim,) + tuple(S) + tuple(din_shape))
        out = op(E)
        return out.reshape(dim, -1).T            # columns = images of basis vectors

    M1 = mat(D1, (4, 3))
    M2 = mat(D2, (6, 3))
    NN = sum(mat(lambda u, l=l: nab(l, u), (6, 3)).T @ mat(lambda u, l=l: nab(l, u), (6, 3)) for l in range(4))
    K = NN - M1 @ M1.T - M2.T @ M2
    return K, D2


def ufield(U):
    return np.stack([coords(pfield(plaq(U, mu, nu))) for (mu, nu) in PAIRS], axis=-2)


def etaP(U):
    return max(np.max(opnorm1m(plaq(U, mu, nu))) for (mu, nu) in PAIRS)


# ---------------- T1: 1D kernels ----------------
def T_n(u, n):
    return np.where((u >= 0) & (u <= 2 * n - 2), np.minimum(u + 1, 2 * n - 1 - u), 0)


def t1():
    L = 3
    ok = True
    for m in (1, 2, 3):
        Nc = 3                                    # coarse sites at level m (periodic)
        nf = Nc * L ** m                          # fine sites
        # level-wise integer kernels L*A (in-plane) and L*M (transverse), periodic
        comp_in = np.eye(nf, dtype=np.int64)
        comp_tr = np.eye(nf, dtype=np.int64)
        size = nf
        for lev in range(m):
            nc = size // L
            Ain = np.zeros((nc, size), dtype=np.int64)
            Atr = np.zeros((nc, size), dtype=np.int64)
            for X in range(nc):
                for s in range(size):
                    Ain[X, s] = T_n((s - L * X) % size, L)
                    Atr[X, s] = 1 if L * X <= s < L * X + L else 0
            comp_in = Ain @ comp_in
            comp_tr = Atr @ comp_tr
            size = nc
        target = np.array([[T_n((s - L ** m * X) % nf, L ** m) for s in range(nf)] for X in range(Nc)], dtype=np.int64)
        e1 = np.max(np.abs(comp_in - target))
        cs_in = comp_in.sum(axis=0)               # = L^m * (column sum of A^(m))
        cs_tr = comp_tr.sum(axis=0)
        mx_in = comp_in.max(); mx_tr = comp_tr.max()
        # transverse: M^(m)[X,s] = L^-m 1{...}; integer comp_tr = L^m M^(m) has entries 1 on the block, colsum 1.
        okm = (e1 == 0) and np.all(cs_in == L ** m) and np.all(cs_tr == 1) and mx_in == L ** m and mx_tr == 1
        print(f"T1 m={m}: compose==T_(L^m): {e1 == 0}; in-plane colsum(A^(m))={cs_in.min() / L ** m:.0f}..{cs_in.max() / L ** m:.0f}"
              f" (target 1), max entry={mx_in / L ** m:.0f} (target 1); transverse colsum={cs_tr.min()}/{L ** m}..{cs_tr.max()}/{L ** m}"
              f" (target L^-m), max entry=1/{L ** m}")
        ok &= okm
    RES['T1'] = ok


# ---------------- T2: dQ_str = Q_2 d ----------------
def t2():
    L = 3
    worst = 0.0
    for (mu, nu) in PAIRS:
        tr = [r for r in range(4) if r not in (mu, nu)]
        dims = [0] * 4
        dims[mu] = 2 * L; dims[nu] = 2 * L; dims[tr[0]] = L; dims[tr[1]] = L
        for _ in range(5):
            a = rng.normal(size=tuple(dims) + (4,))  # a[x, lam]; links leaving the region unused

            def Qstr(Y, d):
                # block Y (coarse coords, 4-vector), direction d: straight lines from the block face
                tot = 0.0
                others = [r for r in range(4) if r != d]
                for off in itertools.product(range(L), repeat=3):
                    x = [0] * 4
                    for r, o in zip(others, off):
                        x[r] = L * Y[r] + o
                    for i in range(L):
                        x[d] = L * Y[d] + i
                        tot += a[tuple(x) + (d,)]
                return tot / L ** 3
            e = lambda r: [1 if k == r else 0 for k in range(4)]
            z = [0, 0, 0, 0]
            lhs = Qstr(z, mu) + Qstr(e(mu), nu) - Qstr(e(nu), mu) - Qstr(z, nu)
            rhs = 0.0
            for x in itertools.product(*[range(n) for n in dims]):
                if x[mu] > 2 * L - 2 or x[nu] > 2 * L - 2:
                    continue
                xm = list(x); xm[mu] += 1
                xn = list(x); xn[nu] += 1
                da = a[x + (mu,)] + a[tuple(xm) + (nu,)] - a[tuple(xn) + (mu,)] - a[x + (nu,)]
                w = T_n(x[mu], L) * T_n(x[nu], L) / L ** 4
                rhs += w * da
            worst = max(worst, abs(lhs - rhs))
    print(f"T2: max |dQ_str a - Q_2 da| = {worst:.3e} (threshold 1e-12)")
    RES['T2'] = worst <= 1e-12


# ---------------- W1-W3, B1 ----------------
def b_ratio(U, D2):
    u = ufield(U)[None]
    Bc = D2(u)[0]                                   # S+(4,3)
    num = np.linalg.norm(Bc, axis=-1)               # |D2 u| per cube
    idx = {p: i for i, p in enumerate(PAIRS)}
    worst = 0.0
    sizes = {p: opnorm1m(plaq(U, *p)) for p in PAIRS}
    for t, (l, m, n) in enumerate(TRIPLES):
        faces = [sizes[(m, n)], np.roll(sizes[(m, n)], -1, axis=l), sizes[(l, n)], np.roll(sizes[(l, n)], -1, axis=m),
                 sizes[(l, m)], np.roll(sizes[(l, m)], -1, axis=n)]
        den = np.max(np.stack(faces), axis=0) ** 2
        worst = max(worst, np.max(num[..., t] / den))
    return worst


def tw():
    S = (3, 3, 3, 3)
    one = [np.broadcast_to(I2, S + (2, 2)).copy() for _ in range(4)]
    K, _ = build_ops(one, S)
    w1 = np.max(np.abs(K))
    print(f"W1: max|K| at U=1: {w1:.3e} (threshold 1e-12)")
    RES['W1'] = w1 <= 1e-12
    g = haar_su2(S)
    Upg = [mm(g, dag(np.roll(g, -1, axis=mu))) for mu in range(4)]
    K, _ = build_ops(Upg, S)
    w2 = np.max(np.abs(K))
    print(f"W2: max|K| on pure gauge: {w2:.3e} (threshold 1e-11)")
    RES['W2'] = w2 <= 1e-11
    RK, RB, inv_k, inv_b = [], [], 0.0, 0.0
    for eta in (0.04, 0.02, 0.01):
        U = rand_field(S, eta)
        K, D2 = build_ops(U, S)
        nk = np.max(np.abs(np.linalg.eigvalsh(K)))
        ep = etaP(U)
        RK.append(nk / ep)
        rb = b_ratio(U, D2)
        RB.append(rb)
        g = haar_su2(S)
        Ug = gauge(U, g)
        Kg, D2g = build_ops(Ug, S)
        nkg = np.max(np.abs(np.linalg.eigvalsh(Kg)))
        inv_k = max(inv_k, abs(nkg - nk) / nk)
        inv_b = max(inv_b, abs(b_ratio(Ug, D2g) - rb) / rb)
        print(f"  eta={eta}: eta_P={ep:.4e} ||K||_op={nk:.4e} R_K={nk / ep:.3f} R_B={rb:.3f}")
    print(f"W3: R_K max={max(RK):.3f} (<=200), max/min={max(RK) / min(RK):.3f} (<=2), gauge change={inv_k:.2e} (<=1e-9)")
    print(f"B1: R_B max={max(RB):.3f} (<=50), max/min={max(RB) / min(RB):.3f} (<=3), gauge change={inv_b:.2e} (<=1e-9)")
    RES['W3'] = max(RK) <= 200 and max(RK) / min(RK) <= 2 and inv_k <= 1e-9
    RES['B1'] = max(RB) <= 50 and max(RB) / min(RB) <= 3 and inv_b <= 1e-9


# ---------------- R1: nonlinear reflection ----------------
def grad_wilson(U, S, mask=None):
    """left gradient (coords) of sum_p s(U(p)), s = 1 - Re tr/N, at every link; mask[pair] = bool array of allowed bases"""
    G = [np.zeros(S + (3,)) for _ in range(4)]
    for (mu, nu) in PAIRS:
        U1 = U[mu]; U2 = sh(U[nu], mu); U3 = sh(U[mu], nu); U4 = U[nu]
        m = np.ones(S, bool) if mask is None else mask[(mu, nu)]
        mf = m[..., None]
        W1 = mm(mm(U1, U2), mm(dag(U3), dag(U4)))          # based at x, starts with U1
        W2 = mm(mm(U2, dag(U3)), mm(dag(U4), U1))          # based at x+e_mu, starts with U2
        W3 = mm(mm(dag(U4), U1), mm(U2, dag(U3)))          # based at x+e_nu, ends with U3^dag
        W4 = W1                                             # based at x, ends with U4^dag
        # d/dt s(e^{tX}W) = -Re tr(XW)/N ; d/dt s(W e^{-tX}) = +Re tr(WX)/N = +Re tr(XW)/N
        c1 = -np.stack([np.real(np.einsum('ij,...ji->...', b, W1)) for b in EB], -1) / N
        c2 = -np.stack([np.real(np.einsum('ij,...ji->...', b, W2)) for b in EB], -1) / N
        c3 = np.stack([np.real(np.einsum('ij,...ji->...', b, W3)) for b in EB], -1) / N
        c4 = np.stack([np.real(np.einsum('ij,...ji->...', b, W4)) for b in EB], -1) / N
        G[mu] += np.where(mf, c1, 0)
        G[nu] += np.roll(np.where(mf, c2, 0), 1, axis=mu)   # contribution lives at link (x+e_mu, nu)
        G[mu] += np.roll(np.where(mf, c3, 0), 1, axis=nu)   # at link (x+e_nu, mu)
        G[nu] += np.where(mf, c4, 0)
    return G


def r1():
    Sb = (4, 4, 2, 2)
    St = tuple(2 * s for s in Sb)
    Ub = rand_field(St, 0.05)                    # only box links (both ends in box) are used
    # box mask for plaquettes: base x with x_mu <= S_mu-2, x_nu <= S_nu-2, all coords in box
    inbox = np.ones(St, bool)
    for r in range(4):
        sl = [slice(None)] * 4; sl[r] = slice(Sb[r], None); inbox[tuple(sl)] = False
    mask = {}
    for (mu, nu) in PAIRS:
        m = inbox.copy()
        for r in (mu, nu):
            sl = [slice(None)] * 4; sl[r] = slice(Sb[r] - 1, None); m[tuple(sl)] = False
        mask[(mu, nu)] = m
    gb = grad_wilson(Ub, St, mask)
    # reflected torus field
    Ut = [np.empty(St + (2, 2), complex) for _ in range(4)]
    pre = [np.empty(St + (5,), int) for _ in range(4)]   # preimage box link (z, mu) and flag (0 crossing)
    for w in itertools.product(*[range(n) for n in St]):
        z, A = [], set()
        for r in range(4):
            if w[r] < Sb[r]:
                z.append(w[r])
            else:
                z.append(2 * Sb[r] - 1 - w[r]); A.add(r)
        for mu in range(4):
            if w[mu] == Sb[mu] - 1 or w[mu] == 2 * Sb[mu] - 1:
                Ut[mu][w] = I2; pre[mu][w] = (0, 0, 0, 0, 0)
            elif mu not in A:
                Ut[mu][w] = Ub[mu][tuple(z)]; pre[mu][w] = tuple(z) + (1,)
            else:
                zz = list(z); zz[mu] -= 1
                Ut[mu][w] = dag(Ub[mu][tuple(zz)]); pre[mu][w] = tuple(zz) + (1,)
    # (a) crossing plaquettes flat; (d) energy ratio
    worst_a = 0.0
    sum_t = 0.0
    for (mu, nu) in PAIRS:
        P = plaq(Ut, mu, nu)
        ut = coords(pfield(P)); sum_t += np.sum(ut ** 2)
        cross = np.zeros(St, bool)
        for r in (mu, nu):
            sl = [slice(None)] * 4; sl[r] = Sb[r] - 1; cross[tuple(sl)] = True
            sl[r] = 2 * Sb[r] - 1; cross[tuple(sl)] = True
        worst_a = max(worst_a, np.max(opnorm1m(P)[cross]))
    sum_b = 0.0
    for (mu, nu) in PAIRS:
        ub = coords(pfield(plaq(Ub, mu, nu)))
        sum_b += np.sum((ub ** 2)[mask[(mu, nu)]])
    gt = grad_wilson(Ut, St)
    worst_b, worst_c = 0.0, 0.0
    for mu in range(4):
        for w in itertools.product(*[range(n) for n in St]):
            p = pre[mu][w]
            if p[4] == 0:
                worst_c = max(worst_c, np.linalg.norm(gt[mu][w]))
                continue
            z = tuple(p[:4])
            worst_c = max(worst_c, abs(np.linalg.norm(gt[mu][w]) - np.linalg.norm(gb[mu][z])))
            inb = all(w[r] < Sb[r] for r in range(4)) and w[mu] + 1 < Sb[mu]
            if inb:
                worst_b = max(worst_b, np.linalg.norm(gt[mu][w] - gb[mu][w]))
    worst_d = abs(sum_t - 16 * sum_b) / (1 + sum_b)
    print(f"R1: (a) crossing plaquettes max||1-U||={worst_a:.2e}; (b) box-link gradient diff={worst_b:.2e}; "
          f"(c) |norm diff| all links={worst_c:.2e}; (d) energy ratio rel err={worst_d:.2e} (sum_box|u|^2={sum_b:.4e})")
    RES['R1'] = worst_a <= 1e-14 and worst_b <= 1e-13 and worst_c <= 1e-13 and worst_d <= 1e-12


# ---------------- G1: Garsia ----------------
def g1():
    D = 10
    nleaf = 3 ** D
    ok = True
    for kind in ('iid', 'tower', 'sparse'):
        a = []
        for t in range(D + 1):
            n = 3 ** t
            if kind == 'iid':
                v = rng.uniform(0, 1, n) * 0.1
            elif kind == 'tower':
                v = np.zeros(n); v[0] = 1.0           # heavy path: node 0 at every depth (ancestors of leaf 0)
            else:
                v = np.where(rng.uniform(size=n) < 0.02, 1.0, 0.0)
            a.append(v)
        # values at leaves: a_t at ancestor of leaf
        leaf_idx = np.arange(nleaf)
        A = np.zeros(nleaf)
        anc = []
        for t in range(D + 1):
            at = a[t][leaf_idx // 3 ** (D - t)]
            anc.append(at)
            A += at
        # beta = max over nodes of avg over its leaves of sum_{s>=t} a_s
        suffix = np.zeros(nleaf)
        beta = 0.0
        for t in range(D, -1, -1):
            suffix += anc[t]
            cond = suffix.reshape(3 ** t, -1).mean(axis=1)
            beta = max(beta, cond.max())
        for lb in (0.25, 0.5, 0.9):
            lam = lb / beta
            E = np.mean(np.exp(lam * A))
            bound = 1 / (1 - lb)
            print(f"G1 {kind}: beta={beta:.4f} lam*beta={lb}: E[e^(lam A)]={E:.6f} bound={bound:.6f}")
            ok &= E <= bound * (1 + 1e-12)
    RES['G1'] = ok


t1()
t2()
tw()
r1()
g1()
okall = all(RES[k] for k in ['T1', 'T2', 'W1', 'W2', 'W3', 'B1', 'R1', 'G1'])
for k in ['T1', 'T2', 'W1', 'W2', 'W3', 'B1', 'R1', 'G1']:
    print(f"{k}: {'PASS' if RES[k] else 'FAIL'}")
print("OVERALL:", "PASS" if okall else "FAIL")
