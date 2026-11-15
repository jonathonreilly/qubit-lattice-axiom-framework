"""c35: N5 at small-field backgrounds, the random-walk expansion, level-0 constants (PROOF.md [S19]).
Criteria: checks/c35_criteria.md (written first). Usage: python3 c35_n5bg.py A|B|C."""
import sys, itertools, time, resource
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

# ----------------------------------------------------------------------------------------------------------------------
# geometry


class Geo:
    def __init__(self, d, L, T):
        self.d, self.L, self.T = d, L, T
        self.n = n = T * L
        self.ns = n ** d
        self.nl = self.ns * d
        self.strides = n ** np.arange(d)
        self.coords = np.array(list(itertools.product(range(n), repeat=d)))[:, ::-1]  # coords[s] with s = sum x_mu n^mu
        assert (self.coords @ self.strides == np.arange(self.ns)).all()
        self.blocks = [tuple(X) for X in itertools.product(range(T), repeat=d)]
        self.nb = len(self.blocks)
        self.h = (L - 1) // 2
        self.orders = list(itertools.permutations(range(d)))

    def sid(self, x):
        return int(sum((int(xi) % self.n) * int(s) for xi, s in zip(x, self.strides)))

    def lid(self, x, mu):
        return self.sid(x) * self.d + mu

    def centre(self, X):
        return tuple(self.L * Xi + self.h for Xi in X)

    def block_sites(self, X):
        return [tuple(self.L * Xi + yi for Xi, yi in zip(X, y)) for y in itertools.product(range(self.L), repeat=self.d)]

    def block_of_site(self, s):
        return tuple(self.coords[s] // self.L)

    def tdist(self, s1, s2):
        dx = np.abs(self.coords[s1] - self.coords[s2]) % self.n
        return np.minimum(dx, self.n - dx).sum(-1)


def axial_steps(c, y, order):
    """steps (x_base, mu, sign) of the complete-axial path c -> y moving in the coordinates `order` (unwrapped)."""
    x = list(c); out = []
    for mu in order:
        while x[mu] != y[mu]:
            if y[mu] > x[mu]:
                out.append((tuple(x), mu, +1)); x[mu] += 1
            else:
                xb = list(x); xb[mu] -= 1; out.append((tuple(xb), mu, -1)); x[mu] -= 1
    return out


def contour_steps(G, X, mu, order, y):
    """S4' contour of coarse link (X, mu): P^order(c_X -> y), L straight steps, reverse of P^order(c_Y -> y + L e_mu)."""
    cX = G.centre(X)
    Y = list(X); Y[mu] += 1; cY = G.centre(Y)
    st = axial_steps(cX, y, order)
    z = list(y)
    for _ in range(G.L):
        st.append((tuple(z), mu, +1)); z[mu] += 1
    back = axial_steps(cY, tuple(z), order)
    st += [(xb, nu, -s) for (xb, nu, s) in reversed(back)]
    return st


# ----------------------------------------------------------------------------------------------------------------------
# SU(2) helpers (basis tau_a = i sigma_a / sqrt 2, orthonormal for -tr XY)

SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
TAU = 1j * SIG / np.sqrt(2)


def su2_exp(x):
    """x: (..., 3) real coefficients -> exp(sum x_a tau_a) as (..., 2, 2)."""
    x = np.asarray(x, float)
    th = np.linalg.norm(x, axis=-1) / np.sqrt(2)
    with np.errstate(invalid="ignore", divide="ignore"):
        nh = np.where(th[..., None] > 0, x / (np.sqrt(2) * np.where(th > 0, th, 1)[..., None]), 0.0)
    nsig = np.einsum("...a,aij->...ij", nh, SIG)
    return np.cos(th)[..., None, None] * np.eye(2) + 1j * np.sin(th)[..., None, None] * nsig


def Ad(V):
    """V: (..., 2, 2) -> (..., 3, 3), Ad(V)_{ab} = -tr(tau_a V tau_b V^dag)."""
    Vd = np.conj(np.swapaxes(V, -1, -2))
    M = np.einsum("aij,...jk,bkl,...li->...ab", TAU, V, TAU, Vd)
    return -M.real


def dag(V):
    return np.conj(np.swapaxes(V, -1, -2))


def su2_logn(V):
    """HS norm of the principal log of V in SU(2)."""
    c = np.clip(np.real(np.trace(V, axis1=-2, axis2=-1)) / 2, -1, 1)
    return np.sqrt(2) * np.arccos(c)


# ----------------------------------------------------------------------------------------------------------------------
# non-abelian (q = 3) dense/sparse objects at a background U (array (nl, 2, 2))


def path_coefs(G, steps, AdU):
    """coefficients of l_P(A) = sum_j Ad(T_{j-1}) a~_j: list of (link index, 3x3), and Ad(T_P)."""
    Tm = np.eye(3); out = []
    for (xb, mu, s) in steps:
        b = G.lid(xb, mu)
        if s > 0:
            out.append((b, Tm.copy())); Tm = Tm @ AdU[b]
        else:
            Tm = Tm @ AdU[b].T; out.append((b, -Tm.copy()))
    return out, Tm


def build_na(G, U):
    d, L = G.d, G.L
    AdU = Ad(U)
    q = 3
    norm = 1.0 / (len(G.orders) * L ** d)
    h = np.zeros((q * G.nb, q * G.nl)); M = np.zeros((q * G.nb, q * G.ns))
    for iX, X in enumerate(G.blocks):
        cX = G.centre(X)
        for y in G.block_sites(X):
            for o in G.orders:
                co, Tp = path_coefs(G, axial_steps(cX, y, o), AdU)
                for (b, C) in co:
                    h[q * iX:q * iX + q, q * b:q * b + q] += norm * C
                sy = G.sid(y)
                M[q * iX:q * iX + q, q * sy:q * sy + q] += norm * Tp
    nc = G.nb * d
    Q = np.zeros((q * nc, q * G.nl))
    for iX, X in enumerate(G.blocks):
        for mu in range(d):
            ic = iX * d + mu
            for y in G.block_sites(X):
                for o in G.orders:
                    co, _ = path_coefs(G, contour_steps(G, X, mu, o, y), AdU)
                    for (b, C) in co:
                        Q[q * ic:q * ic + q, q * b:q * b + q] += norm * C
    # D_U: sites -> links
    rows, cols, vals = [], [], []
    for s in range(G.ns):
        x = G.coords[s]
        for mu in range(d):
            b = s * d + mu
            xp = x.copy(); xp[mu] += 1; sp_ = G.sid(xp)
            for a in range(q):
                for c in range(q):
                    rows.append(q * b + a); cols.append(q * sp_ + c); vals.append(AdU[b][a, c])
                rows.append(q * b + a); cols.append(q * s + a); vals.append(-1.0)
    D = sp.csr_matrix((vals, (rows, cols)), shape=(q * G.nl, q * G.ns))
    lam_mask = np.ones(q * G.ns)
    for X in G.blocks:
        sc = G.sid(G.centre(X)); lam_mask[q * sc:q * sc + q] = 0
    HW = wilson_hessian(G, U)
    return dict(h=h, M=M, Q=Q, D=D, mask=lam_mask, HW=HW, q=q)


def wilson_hessian(G, U):
    """exact Hessian of A -> sum_p Re tr(1 - (e^A U)_p) at A = 0 (left trivialisation), sparse (3 nl)^2."""
    d = G.d; q = 3
    rows, cols, vals = [], [], []
    I2 = np.eye(2, dtype=complex)
    for s in range(G.ns):
        x = G.coords[s]
        for mu in range(d):
            for nu in range(mu + 1, d):
                xm = x.copy(); xm[mu] += 1; xn = x.copy(); xn[nu] += 1
                b = [s * d + mu, G.sid(xm) * d + nu, G.sid(xn) * d + mu, s * d + nu]
                sg = [1, 1, -1, -1]
                c = [U[b[0]], U[b[1]] @ dag(U[b[2]]), dag(U[b[3]]), I2]
                H = hess_plaq(c, sg)
                for j in range(4):
                    for l in range(4):
                        blk = H[j, l]
                        for a in range(q):
                            for bb in range(q):
                                rows.append(q * b[j] + a); cols.append(q * b[l] + bb); vals.append(blk[a, bb])
    return sp.csr_matrix((vals, (rows, cols)), shape=(q * G.nl, q * G.nl))


def cprod(c, i, j):
    """product c[i] c[i+1] ... c[j-1] cyclically (indices mod 4), empty -> identity."""
    P = np.eye(2, dtype=complex); k = i
    while k != j:
        P = P @ c[k % 4]; k = (k + 1) % 4
    return P


def hess_plaq(c, sg):
    """slots 0..3 (exponentials e^{sg_j A_j}), constant c[j] between slot j and slot j+1 (c[3] wraps)."""
    H = np.zeros((4, 4, 3, 3))
    for j in range(4):
        Z = c[j] @ cprod(c, (j + 1) % 4, j)  # full cyclic product starting at c[j]
        for a in range(3):
            for bb in range(3):
                H[j, j, a, bb] = -np.real(0.5 * np.trace((TAU[a] @ TAU[bb] + TAU[bb] @ TAU[a]) @ Z))
        for l in range(j + 1, 4):
            Xm = cprod(c, j, l); Ym = cprod(c, l, j)
            for a in range(3):
                for bb in range(3):
                    v = -np.real(sg[j] * sg[l] * np.trace(TAU[a] @ Xm @ TAU[bb] @ Ym))
                    H[j, l, a, bb] = v; H[l, j, bb, a] = v
    return H


def plaq_action(Us, sg_unused=None):
    P = Us[0] @ Us[1] @ dag(Us[2]) @ dag(Us[3])
    return np.real(np.trace(np.eye(2) - P))


class OpNA:
    def __init__(self, G, U, kappa=1.0):
        self.G = G; o = build_na(G, U); self.__dict__.update(o)
        self.kappa = kappa
        self.Sh = np.linalg.inv(self.h @ self.h.T)
        Mm = self.M * self.mask[None, :]
        self.Mm = Mm; self.SM = np.linalg.inv(Mm @ Mm.T)
        self.N = self.q * G.nl

    def Pi(self, v):
        return v - self.h.T @ (self.Sh @ (self.h @ v))

    def Pres(self, f):
        f = f * self.mask[:, None] if f.ndim == 2 else f * self.mask
        return f - self.Mm.T @ (self.SM @ (self.Mm @ f))

    def O(self, v):
        return self.HW @ v + self.kappa * (self.Q.T @ (self.Q @ v)) + self.D @ self.Pres(self.D.T @ v)

    def Ot(self, v):
        w = self.Pi(v)
        return self.Pi(self.O(w)) + v - w

    def lin(self):
        return spl.LinearOperator((self.N, self.N), matvec=self.Ot, dtype=float)


def lam_min(op, N, seed=0):
    v0 = np.random.default_rng(seed).standard_normal(N)
    ev = spl.eigsh(op, k=1, which="SA", tol=1e-11, v0=v0, ncv=60, maxiter=200000, return_eigenvectors=False)
    return float(ev[0])


def solve_cols(op, B, x0=None):
    X = np.zeros_like(B); res = []
    for j in range(B.shape[1]):
        x, info = spl.minres(op, B[:, j], rtol=1e-12, maxiter=100000)
        X[:, j] = x
        res.append(np.linalg.norm(op @ x - B[:, j]) / np.linalg.norm(B[:, j]))
    return X, max(res)


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20


# ----------------------------------------------------------------------------------------------------------------------
# Part A


def part_A():
    t0 = time.time()
    G = Geo(4, 3, 2)
    rng = np.random.default_rng(0)
    a = rng.standard_normal((G.nl, 3)); a /= np.linalg.norm(a, axis=1).max()
    b0 = G.lid((0, 0, 0, 0), 1)
    E = np.zeros((3 * G.nl, 3)); E[3 * b0:3 * b0 + 3, :] = np.eye(3)
    dist = G.tdist(np.arange(G.ns), np.full(G.ns, b0 // 4))
    ldist = np.repeat(dist, 4)  # per link (base point distance)
    ok = {}

    def profile(Ccol):
        blk = Ccol.reshape(G.nl, 3, 3)
        nrm = np.linalg.norm(blk, ord=2, axis=(1, 2))
        return np.array([nrm[ldist == r].max() for r in range(ldist.max() + 1)]), nrm

    # A0
    U3 = su2_exp(0.3 * a)
    s = G.sid((1, 2, 0, 1)); errs = []
    for (mu, nu) in ((0, 1), (1, 3), (2, 3)):
        x = G.coords[s]; xm = x.copy(); xm[mu] += 1; xn = x.copy(); xn[nu] += 1
        bl = [s * 4 + mu, G.sid(xm) * 4 + nu, G.sid(xn) * 4 + mu, s * 4 + nu]
        c = [U3[bl[0]], U3[bl[1]] @ dag(U3[bl[2]]), dag(U3[bl[3]]), np.eye(2, dtype=complex)]
        H = hess_plaq(c, [1, 1, -1, -1]).transpose(0, 2, 1, 3).reshape(12, 12)
        f = lambda A: plaq_action([su2_exp(A[3 * j:3 * j + 3]) @ U3[bl[j]] for j in range(4)])
        hfd = np.zeros((12, 12)); e = 1e-4
        for i in range(12):
            for j in range(12):
                ei = np.zeros(12); ei[i] = e; ej = np.zeros(12); ej[j] = e
                hfd[i, j] = (f(ei + ej) - f(ei - ej) - f(-ei + ej) + f(-ei - ej)) / (4 * e * e)
        errs.append(np.abs(hfd - H).max() / np.abs(H).max())
    opA = OpNA(G, U3)
    lamv = rng.standard_normal(3 * G.ns) * opA.mask
    lhs = opA.h @ (opA.D @ lamv)
    cvals = np.concatenate([lamv[3 * G.sid(G.centre(X)):3 * G.sid(G.centre(X)) + 3] for X in G.blocks])
    rhs = opA.M @ lamv - cvals
    e2 = np.linalg.norm(lhs - rhs) / np.linalg.norm(rhs)
    v = rng.standard_normal(opA.N); w = rng.standard_normal(opA.N)
    e3 = abs(v @ opA.Ot(w) - w @ opA.Ot(v)) / abs(v @ opA.Ot(w))
    ok["A0"] = max(errs) <= 1e-5 and e2 <= 1e-12 and e3 <= 1e-12
    print(f"A0: Hessian FD rel err {max(errs):.2e}; NA-FP(i) rel err {e2:.2e}; symmetry {e3:.2e}  ({time.time()-t0:.0f} s)")
    del opA
    # backgrounds
    ts = [0.0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3]
    res = {}
    for t in ts:
        U = su2_exp(t * a)
        op = OpNA(G, U); L_ = op.lin()
        lm = lam_min(L_, op.N)
        X, rr = solve_cols(L_, E)
        Ccol = X - (E - op.Pi(E))
        p, _ = profile(Ccol)
        # curvature
        curv = 0.0
        for s_ in range(0, G.ns, 1):
            x = G.coords[s_]
            for mu in range(4):
                for nu in range(mu + 1, 4):
                    xm = x.copy(); xm[mu] += 1; xn = x.copy(); xn[nu] += 1
                    Up = U[s_ * 4 + mu] @ U[G.sid(xm) * 4 + nu] @ dag(U[G.sid(xn) * 4 + mu]) @ dag(U[s_ * 4 + nu])
                    curv = max(curv, float(su2_logn(Up)))
        res[t] = dict(op=op, lm=lm, C=Ccol, p=p, curv=curv, rr=rr)
        print(f"  t={t}: lambda_min {lm:.6e}; max|log U_p| {curv:.4f}; MINRES rel res {rr:.1e}; p(0..12) "
              + " ".join(f"{x:.2e}" for x in p) + f"  ({time.time()-t0:.0f} s, RSS {rss_mb():.0f} MB)")
        if t not in (0.0, 0.1):
            del res[t]["op"]
    # A1 gauge covariance at t = 0.1
    U = su2_exp(0.1 * a)
    gq = rng.standard_normal((G.ns, 4)); gq /= np.linalg.norm(gq, axis=1)[:, None]
    g = np.zeros((G.ns, 2, 2), complex)
    g[:, 0, 0] = gq[:, 0] + 1j * gq[:, 3]; g[:, 0, 1] = gq[:, 2] + 1j * gq[:, 1]
    g[:, 1, 0] = -gq[:, 2] + 1j * gq[:, 1]; g[:, 1, 1] = gq[:, 0] - 1j * gq[:, 3]
    gU = np.zeros_like(U)
    for s_ in range(G.ns):
        x = G.coords[s_]
        for mu in range(4):
            xp = x.copy(); xp[mu] += 1
            gU[s_ * 4 + mu] = g[s_] @ U[s_ * 4 + mu] @ dag(g[G.sid(xp)])
    Adg = Ad(g)

    def Rg(V):
        V3 = V.reshape(G.nl, 3, -1)
        return np.einsum("lab,lbk->lak", Adg[np.arange(G.nl) // 4], V3).reshape(3 * G.nl, -1)
    opg = OpNA(G, gU); Lg = opg.lin()
    lmg = lam_min(Lg, opg.N)
    Xg, _ = solve_cols(Lg, Rg(E))
    Cg = Xg - (Rg(E) - opg.Pi(Rg(E)))
    rel = np.linalg.norm(Cg - Rg(res[0.1]["C"])) / np.linalg.norm(res[0.1]["C"])
    rel_l = abs(lmg - res[0.1]["lm"]) / abs(res[0.1]["lm"])
    ok["A1"] = rel <= 1e-7 and rel_l <= 1e-7
    print(f"A1: ||C(gU)R_g e - R_g C(U) e||/||C e|| = {rel:.2e}; lambda_min rel diff {rel_l:.2e}")
    del opg
    # A2 abelian lambda_min at trivial background
    Gab = G
    opab = AbOp(Gab, kappa=1.0)
    lab = lam_min(opab.lin(), Gab.nl)
    rel2 = abs(lab - res[0.0]["lm"]) / lab
    ok["A2"] = res[0.0]["lm"] > 0 and rel2 <= 1e-7
    print(f"A2: lambda_min SU(2) trivial {res[0.0]['lm']:.8e}, abelian {lab:.8e}, rel diff {rel2:.2e}")
    # A3
    C0 = res[0.0]["C"]; p0 = res[0.0]["p"]
    def dprof(t):
        dlt = (res[t]["C"] - C0).reshape(G.nl, 3, 3)
        nrm = np.linalg.norm(dlt, ord=2, axis=(1, 2))
        return np.array([nrm[ldist == r].max() for r in range(ldist.max() + 1)])
    d1, d3 = dprof(0.001), dprof(0.003)
    sel = d1 >= 1e-6 * p0[0]
    ratios = d3[sel] / d1[sel]
    ok["A3"] = bool(sel.any()) and bool(((ratios >= 2) & (ratios <= 4.5)).all())
    print("A3: Delta_0.003/Delta_0.001 at r = " + " ".join(f"{r}:{x:.3f}" for r, x in zip(np.where(sel)[0], ratios)))
    # A4
    rr_ = np.arange(1, 9)
    slope = {t: np.polyfit(rr_, np.log(res[t]["p"][1:9]), 1)[0] for t in (0.0, 0.001, 0.003, 0.01)}
    ok["A4"] = slope[0.0] < 0 and all(slope[t] <= 0.8 * slope[0.0] for t in (0.001, 0.003, 0.01))
    print("A4: slopes " + " ".join(f"t={t}:{s:.4f}" for t, s in slope.items()))
    # A5 informational
    op0 = res[0.0]["op"]
    for t in (0.01, 0.1):
        opt = res[t]["op"] if "op" in res[t] else OpNA(G, su2_exp(t * a))
        x = rng.standard_normal(op0.N)
        for _ in range(60):
            y = opt.Ot(x) - op0.Ot(x); y = opt.Ot(y) - op0.Ot(y); nx = np.linalg.norm(y); x = y / nx
        print(f"A5: t={t}: ||O~(U_t) - O~(1)||_op ~ {np.sqrt(nx):.4e}, /t = {np.sqrt(nx)/t:.3f}")
    print("A5: lambda_min(t): " + " ".join(f"{t}:{res[t]['lm']:.4e}" for t in ts))
    print("A5: slopes for t >= 0.03: " + " ".join(f"{t}:{np.polyfit(rr_, np.log(res[t]['p'][1:9]), 1)[0]:.4f}" for t in (0.03, 0.1, 0.3)))
    for k, v_ in ok.items():
        print(k, "PASS" if v_ else "FAIL")
    print("Part A:", "PASS" if all(ok.values()) else "FAIL", f"(time {time.time()-t0:.0f} s, peak RSS {rss_mb():.0f} MB)")


# ----------------------------------------------------------------------------------------------------------------------
# abelian sparse objects at the trivial background (one colour)


class AbOp:
    def __init__(self, G, kappa=1.0, a_ww=1.0):
        d, L = G.d, G.L
        self.G = G; self.kappa = kappa; self.a_ww = a_ww
        norm = Fraction(1, len(G.orders) * L ** d)
        # slice template (block at origin)
        c0 = G.centre((0,) * d)
        wt = {}
        for y in itertools.product(range(L), repeat=d):
            for o in G.orders:
                for (xb, mu, s) in axial_steps(c0, y, o):
                    wt[(xb, mu)] = wt.get((xb, mu), 0) + s
        self.w_exact = {k: v * norm for k, v in wt.items() if v != 0}
        wkeys = list(self.w_exact)
        wv = np.array([float(self.w_exact[k]) for k in wkeys])
        rows, cols, vals = [], [], []
        for iX, X in enumerate(G.blocks):
            for k, (xb, mu) in enumerate(wkeys):
                rows.append(iX); cols.append(G.lid(tuple(L * Xi + xi for Xi, xi in zip(X, xb)), mu)); vals.append(wv[k])
        self.W = sp.csr_matrix((vals, (rows, cols)), shape=(G.nb, G.nl))
        self.w2 = float(sum(v * v for v in self.w_exact.values()))
        # Q template per direction
        qt = []
        for mu in range(d):
            acc = {}
            for y in G.block_sites((0,) * d):
                for o in G.orders:
                    for (xb, nu, s) in contour_steps(G, (0,) * d, mu, o, y):
                        acc[(xb, nu)] = acc.get((xb, nu), 0) + s
            qt.append({k: float(v * norm) for k, v in acc.items() if v != 0})
        rows, cols, vals = [], [], []
        for iX, X in enumerate(G.blocks):
            for mu in range(d):
                for (xb, nu), v in qt[mu].items():
                    rows.append(iX * d + mu); cols.append(G.lid(tuple(L * Xi + xi for Xi, xi in zip(X, xb)), nu)); vals.append(v)
        self.Q = sp.csr_matrix((vals, (rows, cols)), shape=(G.nb * d, G.nl))
        # d0 (sites -> links), d1 (links -> plaquettes)
        s_all = np.arange(G.ns)
        r0, c0_, v0 = [], [], []
        for mu in range(d):
            xp = G.coords.copy(); xp[:, mu] = (xp[:, mu] + 1) % G.n
            spn = xp @ G.strides
            r0 += list(s_all * d + mu) * 2; c0_ += list(spn) + list(s_all); v0 += [1.0] * G.ns + [-1.0] * G.ns
        self.d0 = sp.csr_matrix((v0, (r0, c0_)), shape=(G.nl, G.ns))
        r1, c1, v1 = [], [], []; ip = 0
        for mu in range(d):
            for nu in range(mu + 1, d):
                xm = G.coords.copy(); xm[:, mu] = (xm[:, mu] + 1) % G.n
                xn = G.coords.copy(); xn[:, nu] = (xn[:, nu] + 1) % G.n
                pid = ip * G.ns + s_all
                for lk, sg in ((s_all * d + mu, 1.0), ((xm @ G.strides) * d + nu, 1.0), ((xn @ G.strides) * d + mu, -1.0), (s_all * d + nu, -1.0)):
                    r1 += list(pid); c1 += list(lk); v1 += [sg] * G.ns
                ip += 1
        self.d1 = sp.csr_matrix((v1, (r1, c1)), shape=(ip * G.ns, G.nl))
        self.dd = (self.d1.T @ self.d1).tocsr()
        # P_res: per block, project out delta_c and 1_B
        bs = np.array([[G.sid(x) for x in G.block_sites(X)] for X in G.blocks])
        cc = np.array([G.sid(G.centre(X)) for X in G.blocks])
        self.bs, self.cc = bs, cc
        self.N = G.nl

    def Pres(self, f):
        g = f.copy()
        # e1 = delta_c
        if f.ndim == 1:
            g[self.cc] = 0.0
            m = g[self.bs].sum(1)  # (nb,)
            nB = self.bs.shape[1] - 1
            for k in range(self.bs.shape[1]):
                g[self.bs[:, k]] -= m / nB
            g[self.cc] = 0.0
        else:
            g[self.cc] = 0.0
            m = g[self.bs].sum(1)
            nB = self.bs.shape[1] - 1
            for k in range(self.bs.shape[1]):
                g[self.bs[:, k]] -= m / nB
            g[self.cc] = 0.0
        return g

    def Pi(self, v):
        return v - self.W.T @ (self.W @ v) / self.w2

    def O(self, v):
        return self.a_ww * (self.dd @ v) + self.kappa * (self.Q.T @ (self.Q @ v)) + self.d0 @ self.Pres(self.d0.T @ v)

    def Ot(self, v):
        w = self.Pi(v)
        return self.Pi(self.O(w)) + v - w

    def lin(self):
        return spl.LinearOperator((self.N, self.N), matvec=self.Ot, matmat=self.Ot, dtype=float)


# ----------------------------------------------------------------------------------------------------------------------
# Part B


def part_B():
    t0 = time.time()
    G = Geo(2, 3, 12)
    op = AbOp(G, kappa=1.0)
    N = G.nl
    K = op.Ot(np.eye(N))
    K = (K + K.T) / 2  # symmetric to rounding
    ev, V = np.linalg.eigh(K)
    ok = {"B0": ev[0] > 0}
    print(f"B0: lambda_min {ev[0]:.6e}, lambda_max {ev[-1]:.4f}  ({time.time()-t0:.0f} s)")
    Kinv = (V / ev) @ V.T
    blk_of_link = np.array([tuple(G.coords[b // 2] // 3) for b in range(N)])
    qs = {}; ok1 = ok2 = ok3 = ok5 = True
    store = {}
    for R in (1, 2, 3):
        nbx = G.T // R
        box_of_link = (blk_of_link // R) @ np.array([1, nbx])
        P = np.zeros((N, N)); Rm = np.zeros((N, N)); Gs = {}; Oms = {}; S = X = None
        for bx in range(nbx * nbx):
            bc = np.array([bx % nbx, bx // nbx]) * R  # lower corner block of the box (coord order: x0 + nbx*x1)
            # blocks within l_inf distance <= R of the box [bc, bc+R-1]
            def dist1(z, lo):
                dz = (z - lo) % G.T
                inside = dz <= R - 1
                return np.where(inside, 0, np.minimum(dz - (R - 1), G.T - dz))
            dmax = np.maximum(dist1(blk_of_link[:, 0], bc[0]), dist1(blk_of_link[:, 1], bc[1]))
            Om = np.where(dmax <= R)[0]
            Oc = np.where(dmax > R)[0]
            cols = np.where(box_of_link == bx)[0]
            Gb = np.linalg.inv(K[np.ix_(Om, Om)])
            pos = np.searchsorted(Om, cols)
            P[np.ix_(Om, cols)] = Gb[:, pos]
            Rm[np.ix_(Oc, cols)] = -(K[np.ix_(Oc, Om)] @ Gb[:, pos])
            Gs[bx] = (Om, Gb); Oms[bx] = (Om, Oc, cols, pos)
        e1 = np.abs(K @ P - (np.eye(N) - Rm)).max()
        ok1 &= e1 <= 1e-10
        q = np.abs(Rm).sum(1).max(); qs[R] = q
        NP = np.abs(P).sum(1).max(); MR = np.abs(Rm).max()
        line = f"R={R}: B1 err {e1:.2e}; q = {q:.4e}; N0(|P|) = {NP:.4f}; M0(|R|) = {MR:.3e}"
        if q < 1:
            S = P.copy(); X = P.copy(); n = 0; worst = 0.0; errs = []
            while True:
                bnd = NP * MR * q ** n / (1 - q)
                en = np.abs(Kinv - S).max(); errs.append(en)
                worst = max(worst, en / ((1 + 1e-9) * bnd + 1e-12))
                if bnd < 1e-13 or n >= 200:
                    break
                X = X @ Rm; S += X; n += 1
            ok2 &= worst <= 1
            ok3 &= errs[-1] <= 1e-10
            line += f"; n_max {n}; max e_n/bound {worst:.3e}; e_n " + " ".join(f"{e:.1e}" for e in errs[:8]) + f" ... {errs[-1]:.1e}"
            # B5
            rng = np.random.default_rng(0)
            Y = rng.permutation(nbx * nbx)[: (nbx * nbx) // 2]
            sv = np.zeros(nbx * nbx, complex); sv[Y] = 0.5 + 0.5j
            Rs = Rm * sv[box_of_link][None, :]
            Cs = P @ np.linalg.inv(np.eye(N) - Rs)
            w5 = 0.0
            for bx in range(nbx * nbx):
                if bx in set(Y):
                    continue
                Om, Oc, cols, pos = Oms[bx]
                ref = np.zeros((N, len(cols))); ref[Om, :] = Gs[bx][1][:, pos]
                w5 = max(w5, np.abs(Cs[:, cols] - ref).max())
            ok5 &= w5 <= 1e-12
            line += f"; B5 decoupling err {w5:.1e}"
            del Cs, Rs
        print(line + f"  ({time.time()-t0:.0f} s, RSS {rss_mb():.0f} MB)")
        if R == 2:
            store = dict(Oms=Oms, box_of_link=box_of_link, nbx=nbx)
        del P, Rm, S, X
    ok["B1"] = ok1; ok["B2"] = ok2; ok["B3"] = ok3; ok["B5"] = ok5
    ok["B4"] = qs[3] < qs[2] < qs[1] and qs[3] < 1
    # B6 square root at R = 2
    del Kinv
    lam0 = np.sqrt(ev[0] * ev[-1])
    xg, wg = np.polynomial.legendre.leggauss(200)
    th = (xg + 1) * np.pi / 4; wth = wg * np.pi / 4
    Ksq = (V / np.sqrt(ev)) @ V.T
    fq = np.zeros_like(ev); quad_walk = np.zeros((N, N))
    Oms = store["Oms"]; nbx = store["nbx"]
    for k in range(len(th)):
        u2 = lam0 * np.tan(th[k]) ** 2
        jac = np.sqrt(lam0) / np.cos(th[k]) ** 2
        Kt = K + u2 * np.eye(N)
        fq += (2 / np.pi) * wth[k] * jac / (ev + u2)
        P = np.zeros((N, N)); Rm = np.zeros((N, N))
        for bx, (Om, Oc, cols, pos) in Oms.items():
            Gb = np.linalg.inv(Kt[np.ix_(Om, Om)])
            P[np.ix_(Om, cols)] = Gb[:, pos]
            Rm[np.ix_(Oc, cols)] = -(K[np.ix_(Oc, Om)] @ Gb[:, pos])
        q = np.abs(Rm).sum(1).max(); NP = np.abs(P).sum(1).max(); MR = np.abs(Rm).max()
        # partial sum sum_{j < 2^m} R^j by doubling, m minimal with tail bound < 1e-14
        m = 0
        while NP * MR * q ** (2 ** m - 1) / (1 - q) >= 1e-14:
            m += 1
        S = np.eye(N); Rp = Rm.copy()
        for _ in range(m):
            S = S + S @ Rp
            Rp = Rp @ Rp
        quad_walk += (2 / np.pi) * wth[k] * jac * (P @ S)
        del P, Rm, S, Rp, Kt
    quad_exact = (V * fq) @ V.T
    r6a = np.abs(quad_exact - Ksq).max() / np.abs(Ksq).max()
    r6b = np.abs(quad_walk - quad_exact).max() / np.abs(quad_exact).max()
    ok["B6"] = r6a <= 1e-6 and r6b <= 1e-10
    print(f"B6: quadrature vs eig {r6a:.2e}; walk-quadrature vs resolvent-quadrature {r6b:.2e}  ({time.time()-t0:.0f} s)")
    # B7 informational: proven eps_R with the measured constants
    Dist = G.tdist(np.repeat(np.arange(G.ns), 2)[:, None], np.repeat(np.arange(G.ns), 2)[None, :])
    Ka = np.abs(K)
    for mm in (0.05, 0.1, 0.2):
        Dm_ = (Ka * (np.exp(mm * Dist) - 1)).sum(1).max(); Sm = (Ka * np.exp(mm * Dist)).sum(1).max()
        line = f"B7: m={mm}: D_m(|K|) = {Dm_:.3f} (CT needs <= gamma/2 = {ev[0]/2:.4f}); S_m = {Sm:.2f}"
        for R in (1, 2, 3):
            a_ = mm / 2
            epsR = (2 * Sm / ev[0]) * 2 * (1 / np.tanh(a_ / 4)) ** 2 * np.exp(-a_ * R * 3 / 2)  # d = 2: 2 coth^2
            line += f"; eps_R(R={R}) = {epsR:.2e} vs q = {qs[R]:.2e}"
        print(line)
    for k, v_ in ok.items():
        print(k, "PASS" if v_ else "FAIL")
    print("Part B:", "PASS" if all(ok.values()) else "FAIL", f"(time {time.time()-t0:.0f} s, peak RSS {rss_mb():.0f} MB)")


# ----------------------------------------------------------------------------------------------------------------------
# Part C


def part_C():
    t0 = time.time(); ok = {}
    L, d, kap = 3, 4, 1.0
    pL = 5 * L - 4
    c1 = 1 / 3.5e6
    gam0 = c1 * min(0.5, kap / 2) / L ** 2
    G = Geo(4, 3, 3)
    op = AbOp(G, kappa=kap)
    wv = list(op.w_exact.values())
    w2 = sum(v * v for v in wv); l1 = sum(abs(v) for v in wv); mx = max(abs(v) for v in wv)
    nu_w = mx * l1 / w2
    # float rows of 1 - Pi in block 0
    blk0 = [b for b in range(G.nl) if G.block_of_site(b // 4) == (0, 0, 0, 0)]
    E = np.zeros((G.nl, len(blk0))); E[blk0, np.arange(len(blk0))] = 1
    onemPi = E - op.Pi(E)
    nuf = np.abs(onemPi).sum(0).max()
    ok["C1"] = float(nu_w) <= 128 * L * L / (L - 1) and abs(nuf - float(nu_w)) <= 1e-12 * float(nu_w)
    print(f"C1: ||w||^2 = {w2} = {float(w2):.6f}; sum|w| = {l1} = {float(l1):.6f}; max|w| = {mx}; nu_w = {nu_w} = "
          f"{float(nu_w):.6f} (N5-sl bound n_Pi - 1 <= {128*L*L/(L-1):.0f}); float rows {nuf:.12f}")
    # C2 rows of O~_0
    Ocols = op.Ot(E)  # (nl, 324): column b of O~ = row b by symmetry
    # symmetry check on the torus: O~(b', b) for b' also in block 0 vs O~(b, b')
    sub = Ocols[blk0, :]
    esym = np.abs(sub - sub.T).max()
    # ranges and Z^4 distances
    bsite = np.arange(G.nl) // 4
    Bk = G.coords[bsite] // L
    shift = np.where(Bk == 2, -1, Bk)
    lift = G.coords[bsite] - np.where(Bk == 2, G.n, 0)
    x0 = G.coords[np.array(blk0) // 4]
    nz = np.abs(Ocols) > 0
    rng_ok = True  # range <= 1 block is automatic on T = 3 up to aliasing; check zero entries are exact zeros elsewhere
    Dz = np.abs(lift[:, None, :] - x0[None, :, :]).sum(-1)  # (nl, 324)
    A = np.abs(Ocols)

    def Dnum(m):
        return float((A * (np.exp(m * Dz) - 1)).sum(0).max() * (1 + 1e-9))
    Dcol = {m: (A * (np.exp(m * Dz) - 1)).sum(0) for m in (1e-3, 0.1)}

    def Nnum(m):
        return float((A * np.exp(m * Dz)).sum(0).max() * (1 + 1e-9))
    nPi = 1 + 128 * L * L / (L - 1)
    SO = 24 + 16 * kap * pL + 32

    def EO(m):
        return 24 * (np.exp(2 * m) - 1) + (np.exp(m * pL) - 1) * (16 * kap * pL + 32)

    def Dfrak(m):
        dP = (np.exp(4 * m * (L - 1)) - 1) * (nPi - 1); pm = nPi + dP
        return dP * (1 + (SO + EO(m)) * pm + nPi * SO) + nPi * EO(m) * pm
    c2 = all(Dnum(m) <= Dfrak(m) for m in (1e-12, 1e-9, 1e-6, 1e-3))

    def bisect(f, target, lo=0.0, hi=1.0):
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid) <= target:
                lo = mid
            else:
                hi = mid
        return lo
    mnum = bisect(Dnum, gam0 / 2); mfr = bisect(Dfrak, gam0 / 2)
    m4num = bisect(Dnum, gam0 / 4)
    print(f"C2: symmetry {esym:.1e}; N^num(0) = {Nnum(0):.4f}; sum|O~|d = {float((A*Dz).sum(0).max()):.4f}; "
          + " ".join(f"m={m:g}: D^num {Dnum(m):.3e} vs Dfrak {Dfrak(m):.3e};" for m in (1e-12, 1e-9, 1e-6, 1e-3)))
    print(f"C2: gamma_0 = {gam0:.4e}; m_cov^num = {mnum:.4e} (D^num <= gamma_0/2); N5-triv m_cov(i=0) = {mfr:.4e}; "
          f"ratio {mnum/mfr:.3e}; m_4^num (<= gamma_0/4) = {m4num:.4e}  ({time.time()-t0:.0f} s, RSS {rss_mb():.0f} MB)")
    # C3 Bloch
    bloc = {b: k for k, b in enumerate(blk0)}
    loc_of = np.zeros(G.nl, int)
    for b in range(G.nl):
        s_ = b // 4; mu = b % 4
        xl = tuple(G.coords[s_] % L); loc_of[b] = bloc[G.lid(xl, mu)]
    shifts = list(itertools.product((-1, 0, 1), repeat=4))
    sidx = {s: i for i, s in enumerate(shifts)}
    sh_of = np.array([sidx[tuple(r)] for r in shift])
    nloc = len(blk0)

    def build_As(cols):
        As = np.zeros((81, nloc, nloc))
        for j in range(G.nl):
            As[sh_of[j], :, loc_of[j]] += cols[j, :]
        return As  # As[s][b, b'] = O~(b, b' + s L)
    As = build_As(Ocols)
    S_arr = np.array(shifts, float)

    def bloch(As_, K):
        ph = np.exp(1j * (S_arr @ K))
        return np.tensordot(ph, As_, axes=(0, 0))
    # validation on T = 3 grid
    rng = np.random.default_rng(0); vmax = 0.0
    for _ in range(3):
        K = 2 * np.pi * rng.integers(0, 3, 4) / 3
        Mk = bloch(As, K); Mk = (Mk + Mk.conj().T) / 2
        ewk, vk = np.linalg.eigh(Mk)
        v = vk[:, 0]
        ext = v[loc_of] * np.exp(1j * (shift @ K))
        r_ = op.Ot(ext.real) + 1j * op.Ot(ext.imag) - ewk[0] * ext
        vmax = max(vmax, np.linalg.norm(r_) / np.linalg.norm(ext))
    # grid minimum
    def grid_min(As_):
        best = (np.inf, None)
        g = np.arange(8) * 2 * np.pi / 8
        for K in itertools.product(range(8), repeat=4):
            if tuple((-np.array(K)) % 8) < K:
                continue
            Kv = g[list(K)]
            Mk = bloch(As_, Kv); Mk = (Mk + Mk.conj().T) / 2
            lmn = np.linalg.eigvalsh(Mk)[0]
            if lmn < best[0]:
                best = (lmn, K)
        return best
    gm, Km = grid_min(As)
    print(f"C3: Bloch validation residual {vmax:.1e}; gamma_meas = {gm:.6e} at K = (2pi/8){Km}; proven gamma_0 = {gam0:.3e}; "
          f"ratio {gm/gam0:.3e}  ({time.time()-t0:.0f} s)")
    cE = 0.004069
    opLB = AbOp(G, kappa=kap, a_ww=2 * cE)
    AsLB = build_As(opLB.Ot(E))
    gLB, KLB = grid_min(AsLB)
    print(f"C3: gamma_meas^LB (2c_E d*d) = {gLB:.6e} at K = (2pi/8){KLB}; proven gamma_i = 1.29e-10; ratio {gLB/1.29e-10:.3e}"
          f"  ({time.time()-t0:.0f} s)")
    ok["C3"] = vmax <= 1e-10 and gm >= gam0 and gLB >= 1.29e-10
    del As, AsLB, Ocols, A, Dz
    # C4 decay on T = 5
    G5 = Geo(4, 3, 5)
    op5 = AbOp(G5, kappa=kap)
    b0 = G5.lid((0, 0, 0, 0), 1)
    e = np.zeros(G5.nl); e[b0] = 1
    x, info = spl.cg(op5.lin(), e, rtol=1e-12, maxiter=200000)
    rr = np.linalg.norm(op5.Ot(x) - e)
    Ccol = x - (e - op5.Pi(e))
    dist5 = np.repeat(G5.tdist(np.arange(G5.ns), np.full(G5.ns, 0)), 4)
    p = np.array([np.abs(Ccol[dist5 == r]).max() for r in range(dist5.max() + 1)])
    rr_ = np.arange(4, 21)
    mmeas = -np.polyfit(rr_, np.log(p[4:21]), 1)[0]
    ok["C4"] = mmeas >= mnum
    # C2 range/aliasing validation on T = 5: 6 rows of block 0 vanish outside shifts in {-1,0,1}^4 and reproduce the T = 3 D-values
    bsite5 = np.arange(G5.nl) // 4
    Bk5 = G5.coords[bsite5] // L
    sh5 = np.where(Bk5 >= 3, Bk5 - 5, Bk5)
    near = (np.abs(sh5) <= 1).all(1)
    lift5 = G5.coords[bsite5] - np.where(Bk5 >= 3, G5.n, 0)
    worst_out = 0.0; worst_D = 0.0
    for k in range(0, len(blk0), 54):
        b3 = blk0[k]; xb = tuple(G.coords[b3 // 4]); mu = b3 % 4
        b5 = G5.lid(xb, mu)
        e5 = np.zeros(G5.nl); e5[b5] = 1
        col = op5.Ot(e5)
        worst_out = max(worst_out, np.abs(col[~near]).max())
        dz5 = np.abs(lift5 - np.array(xb)).sum(1)
        for m in (1e-3, 0.1):
            v5 = (np.abs(col) * (np.exp(m * dz5) - 1)).sum(); v3 = Dcol[m][k]
            worst_D = max(worst_D, abs(v5 - v3) / v3)
    rng_ok = worst_out <= 1e-14 and worst_D <= 1e-12
    ok["C2"] = c2 and esym <= 1e-12 and rng_ok
    print(f"C2 (validation on T = 5): max |entry| outside the 1-block range {worst_out:.1e}; D-value T5 vs T3 rel diff {worst_D:.1e}")
    print(f"C4: CG info {info}, residual {rr:.1e}; m_meas = {mmeas:.4f} vs m_cov^num = {mnum:.3e}; p(r) = "
          + " ".join(f"{v:.2e}" for v in p) + f"  ({time.time()-t0:.0f} s, RSS {rss_mb():.0f} MB)")
    for k, v_ in ok.items():
        print(k, "PASS" if v_ else "FAIL")
    print("Part C:", "PASS" if all(ok.values()) else "FAIL", f"(time {time.time()-t0:.0f} s, peak RSS {rss_mb():.0f} MB)")


if __name__ == "__main__":
    {"A": part_A, "B": part_B, "C": part_C}[sys.argv[1]]()
