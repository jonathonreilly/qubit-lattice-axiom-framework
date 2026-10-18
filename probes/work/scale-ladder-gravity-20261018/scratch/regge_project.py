"""Project the supplied 4D Kuhn-complex Regge Hessian's O(k^2) symbol onto the
K48 (S4 x inversion) gauge-invariant space, and test metric universality:
with edge lengths l_v^2 = v^T g0 v, is the leading symbol EH of g0?"""
import os, sys, numpy as np
REPO = '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0'
sys.path.insert(0, REPO + '/scripts'); sys.path.insert(0, os.path.dirname(__file__))
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4
import census as C

HC = R4.HCOMPS
U = np.ones(4)

def build(g0):
    a_terms, d_terms = [], []
    L2 = lambda v: float(v @ g0 @ v)
    for tri in R4.TRI_CLASSES:
        vts = [np.array(x) for x in tri]
        qvals, einfo = [], []
        for (i, j) in [(0, 1), (0, 2), (1, 2)]:
            cls, anc = R4.edge_class(tuple(vts[i]), tuple(vts[j]))
            v = np.array(R4.DIRS15[cls], float)
            qvals.append(L2(v)); einfo.append((cls, anc, np.sqrt(L2(v))))
        aout = R4.AREA(*qvals)
        at = [(cls, np.array(anc, float), 2 * ell * float(aout[1 + n])) for n, (cls, anc, ell) in enumerate(einfo)]
        dt = []
        for vs in R4.STARS[tri]:
            loc = {v: i for i, v in enumerate(vs)}
            hl = sorted([loc[tri[0]], loc[tri[1]], loc[tri[2]]])
            miss = tuple(sorted([i for i in range(5) if i not in hl]))
            qv, ed = [], []
            for (i, j) in R4.PAIRS5:
                cls, anc = R4.edge_class(vs[i], vs[j])
                v = np.array(R4.DIRS15[cls], float)
                qv.append(L2(v)); ed.append((cls, anc, np.sqrt(L2(v))))
            out = R4.THETA[miss](*qv)
            dt += [(cls, np.array(anc, float), -2 * ell * float(out[1 + n])) for n, (cls, anc, ell) in enumerate(ed)]
        for src, dst in ((at, a_terms), (dt, d_terms)):
            dst.append((np.array([t[0] for t in src], int), np.array([t[1] for t in src], float),
                        np.array([t[2] for t in src], float)))

    def row(term, k):
        cls, anc, coef = term
        r = np.zeros(15, complex); np.add.at(r, cls, coef * np.exp(1j * (anc @ k))); return r

    def Q(k):
        k = np.asarray(k, complex); M = np.zeros((15, 15), complex)
        for t in range(len(a_terms)):
            ap, am = row(a_terms[t], k), row(a_terms[t], -k)
            dp, dm = row(d_terms[t], k), row(d_terms[t], -k)
            M += 0.5 * (np.outer(am, dp) + np.outer(dm, ap))
        return M

    def Mmap(k):
        k = np.asarray(k, complex); Mm = np.zeros((15, 10), complex)
        for ci, v in enumerate(R4.DIRS15):
            vv = np.array(v, float); ell = np.sqrt(L2(vv)); z = (k @ vv) / 2
            ph = 1.0 if abs(z) < 1e-13 else (np.exp(2j * z) - 1) / (2j * z)
            for hj, (a, b) in enumerate(HC):
                Hm = np.zeros((4, 4)); Hm[a, b] += 1
                if a != b: Hm[b, a] += 1
                Mm[ci, hj] = ph * (vv @ Hm @ vv) / (2 * ell)
        return Mm

    return lambda k: Mmap(-np.asarray(k, complex)).T @ Q(k) @ Mmap(k), Q

def Q2_of(Qh, k, eps=(2e-3, 1e-3)):
    a = [Qh(e * k) / e**2 for e in eps]
    return (4 * a[1] - a[0]) / 3  # Richardson: removes O(k^4) relative term

def hfull(x):
    h = np.zeros((4, 4))
    for i, (a, b) in enumerate(HC): h[a, b] = h[b, a] = x[i]
    return h

def EH(h, k, g0):
    gi = np.linalg.inv(g0)
    hu = gi @ h @ gi             # raised
    k2 = k @ gi @ k
    trh = np.trace(gi @ h)
    kh = gi @ h @ gi @ k          # h^{mu nu} k_nu  (raised)
    return (k2 * np.trace(gi @ h @ gi @ h) - 2 * (k @ gi @ h @ gi @ h @ gi @ k)
            + 2 * (k @ gi @ h @ gi @ k) * trh - k2 * trh**2)

def fit_monomials(Ffun, B, nsamp=1400, seed=3):
    rng = np.random.default_rng(seed)
    A, y = [], []
    for _ in range(nsamp):
        x = rng.standard_normal(10); k = rng.standard_normal(4)
        h = hfull(x)
        A.append(C.evalF(B, C.field_vec(h, 2), k)); y.append(Ffun(x, h, k))
    A = np.array(A); y = np.array(y)
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return c, np.linalg.norm(A @ c - y) / np.linalg.norm(y)

if __name__ == '__main__':
    r = C.census(2, 2, 'K48'); B, W = r['basis']           # 550 x 2 gauge-invariant K48 basis
    W, _ = np.linalg.qr(W)
    for b in [0.0, 0.3, -0.15]:
        g0 = np.eye(4) + b * np.outer(U, U)
        Qh, _ = build(g0)
        cache = {}
        def FR(x, h, k):
            Q2 = Q2_of(Qh, k); Q2 = 0.5 * (Q2 + Q2.T)
            return float(np.real(x @ Q2 @ x))
        cR, resR = fit_monomials(FR, B, nsamp=700)
        cE, resE = fit_monomials(lambda x, h, k: EH(h, k, g0), B, nsamp=700)
        cE0, _ = fit_monomials(lambda x, h, k: EH(h, k, np.eye(4)), B, nsamp=700)
        def split(c):
            inside = W @ (W.T @ c); return np.linalg.norm(c - inside) / np.linalg.norm(c), W.T @ c
        oR, wR = split(cR); oE, wE = split(cE)
        lam, *_ = np.linalg.lstsq(cE[:, None], cR, rcond=None)
        print(f"b={b:+.2f}: fit residuals Regge {resR:.1e} EH {resE:.1e}; "
              f"Regge outside K48 gauge-inv span {oR:.1e}; EH_g0 outside {oE:.1e}")
        print(f"   Regge Q2 = {lam[0]:+.6f} * EH_g0 ; misfit {np.linalg.norm(cR - lam[0]*cE)/np.linalg.norm(cR):.1e};"
              f" misfit vs EH_delta {np.linalg.norm(cR - (cR@cE0)/(cE0@cE0)*cE0)/np.linalg.norm(cR):.1e}")
