"""bb7k: the cut-off iterated gluing G^off (Construction KΠ-off, BFT_B §21.0) on spread data, d = 2, SU(2) (lane B session 7).

Criteria: checks/bb7k_criteria.md (written before this script). Setting and normal-form descent as checks/bb6n_nf.py.
"""
import time

import numpy as np

T0 = time.time()
rng = np.random.default_rng(7575)
n, Tc = 3, 5
M = n * Tc
HW = 2 * n
S = 2 * HW + 1
TAU = 0.1
TOL = 1e-12
MAXIT = 40000
R1, R2 = 1.0, 2.0


def qmul(p, q):
    w1, x1, y1, z1 = np.moveaxis(p, -1, 0)
    w2, x2, y2, z2 = np.moveaxis(q, -1, 0)
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=-1)


def qinv(q):
    return q * np.array([1.0, -1.0, -1.0, -1.0])


def qexp(v):
    th = np.linalg.norm(v, axis=-1, keepdims=True)
    sinc = np.where(th > 1e-15, np.sin(th) / np.where(th > 1e-15, th, 1.0), 1.0)
    return np.concatenate([np.cos(th), sinc * v], axis=-1)


def qlog(q):
    vn = np.linalg.norm(q[..., 1:], axis=-1, keepdims=True)
    th = np.arctan2(vn, q[..., :1])
    fac = np.where(vn > 1e-15, th / np.where(vn > 1e-15, vn, 1.0), 1.0)
    return fac * q[..., 1:]


def qdist(p, q):
    return np.linalg.norm(qlog(qmul(p, qinv(q))), axis=-1)


def haar(shape):
    q = rng.standard_normal(shape + (4,))
    return q / np.linalg.norm(q, axis=-1, keepdims=True)


def gauge(U, g):
    out = np.empty_like(U)
    for a in range(2):
        out[:, :, a] = qmul(qmul(g, U[:, :, a]), qinv(np.roll(g, -1, axis=a)))
    return out


def box_extract(U, c):
    idx = (np.arange(-HW, HW + 1) + c[:, None]) % M
    return U[np.ix_(idx[0], idx[1])], idx


VALID = np.ones((S, S, 2), bool)
VALID[S - 1, :, 0] = False
VALID[:, S - 1, 1] = False
CENTER = (HW, HW)
ident = np.zeros((S, S, 4)); ident[..., 0] = 1.0


def box_w(Ub, g):
    w = np.zeros(Ub.shape[:3] + (3,))
    for a in range(2):
        W = qmul(qmul(g, Ub[:, :, a]), qinv(np.roll(g, -1, axis=a)))
        assert (W[..., 0][VALID[:, :, a]] > 0).all()
        w[:, :, a] = qlog(W)
    w[~VALID] = 0.0
    return w


def box_div(w):
    return sum(w[:, :, a] - np.roll(w[:, :, a], 1, axis=a) for a in range(2))


def normal_form(Ub, g0):
    g = g0.copy()
    err = np.inf
    for it in range(MAXIT):
        Dz = box_div(box_w(Ub, g))
        err = np.abs(Dz).max()
        if err < TOL:
            break
        g = qmul(qexp(-TAU * Dz), g)
    g = qmul(np.broadcast_to(qinv(g[CENTER]), g.shape), g)
    return g, err


roots = [np.array([n * X0, n * X1]) for X0 in range(Tc) for X1 in range(Tc)]
RIDX = {(X0, X1): i for i, (X0, X1) in enumerate([(a, b) for a in range(Tc) for b in range(Tc)])}


def nf_all(U, starts=None):
    res = []
    for i, c in enumerate(roots):
        Ub, _ = box_extract(U, c)
        g, err = normal_form(Ub, ident if starts is None else starts[i])
        res.append((g, err))
    return res


def boxed(gfull, c):
    """restrict a full-torus gauge to the box of root c."""
    idx = (np.arange(-HW, HW + 1) + c[:, None]) % M
    return gfull[np.ix_(idx[0], idx[1])]


def transported(nf, left, right_full):
    """normal forms of U^k from those of U: g_X(U^k) = k(c_X) g_X(U) k^{-1} (NF-cov)."""
    res = []
    for i, c in enumerate(roots):
        kb = boxed(right_full, c)
        res.append((qmul(qmul(np.broadcast_to(left[i], kb.shape), nf[i][0]), qinv(kb)), 0.0))
    return res


def perturbed(gb, amp=0.3):
    eta = rng.standard_normal((S, S, 3)); eta *= amp / np.linalg.norm(eta, axis=-1).max(); eta[CENTER] = 0.0
    return qmul(qexp(eta), gb)


def sig5(t):
    return 1 - 10 * t ** 3 + 15 * t ** 4 - 6 * t ** 5


def psi(d):
    if d <= R1:
        return 1.0
    if d >= R2:
        return 0.0
    x = (R2 - d) / (R2 - R1)
    a, b = np.exp(-1.0 / x), np.exp(-1.0 / (1.0 - x))
    return a / (a + b)


def m_w(a, b, w, cut=True):
    if w == 0.0:
        return a
    if w == 1.0:
        return b
    v = qlog(qmul(qinv(a), b))
    d = np.linalg.norm(v)
    ps = psi(d) if cut else 1.0
    return qmul(a, qexp(w * ps * v))


def corner_points(nfs, z, X):
    """points p_eps = g_{X+eps}(z) for eps in {0,1}^2 (X = lower corner)."""
    P = {}
    for e0 in (0, 1):
        for e1 in (0, 1):
            Y = ((X[0] + e0) % Tc, (X[1] + e1) % Tc)
            i = RIDX[Y]
            c = roots[i]
            u = (np.array(z) - c + HW) % M
            P[(e0, e1)] = nfs[i][0][u[0], u[1]]
    return P


def glue_site(nfs, z, X, t, cut=True, left=None):
    P = corner_points(nfs, z, X)
    if left is not None:
        for e, p in P.items():
            Y = ((X[0] + e[0]) % Tc, (X[1] + e[1]) % Tc)
            P[e] = qmul(left[RIDX[Y]], p)
    w0, w1 = 1 - sig5(t[0]), 1 - sig5(t[1])
    Q0 = m_w(P[(0, 0)], P[(1, 0)], w0, cut)
    Q1 = m_w(P[(0, 1)], P[(1, 1)], w0, cut)
    return m_w(Q0, Q1, w1, cut)


def glue(nfs, cut=True, left=None):
    G = np.zeros((M, M, 4))
    for z0 in range(M):
        for z1 in range(M):
            X = (z0 // n, z1 // n)
            t = ((z0 - n * X[0]) / n, (z1 - n * X[1]) / n)
            G[z0, z1] = glue_site(nfs, (z0, z1), X, t, cut, left)
    return G


def spread_at(nfs, z):
    X = (z[0] // n, z[1] // n)
    P = list(corner_points(nfs, z, X).values())
    return max(float(qdist(p, q)) for p in P for q in P)


def karcher(points, weights, start, iters=200):
    m = start.copy()
    for it in range(iters):
        step = sum(wt * qlog(qmul(qinv(m), p)) for p, wt in zip(points, weights))
        m = qmul(m, qexp(step))
        if np.linalg.norm(step) < 1e-13:
            return m, True
    return m, False


out = []
A = rng.standard_normal((M, M, 2, 3))
A *= 0.3 / (n * np.linalg.norm(A, axis=-1).max())
U0 = qexp(A)
nf0 = nf_all(U0)
h = haar((M, M))
Us = gauge(U0, h)
hroot = [h[c[0], c[1]] for c in roots]
starts = [perturbed(qmul(qmul(np.broadcast_to(hroot[i], (S, S, 4)), nf0[i][0]), qinv(boxed(h, c))))
          for i, c in enumerate(roots)]
nfs = nf_all(Us, starts)
errs = [e for _, e in nf0 + nfs]
sp = [spread_at(nfs, (z0, z1)) for z0 in range(M) for z1 in range(M)]
sp0 = [spread_at(nf0, (z0, z1)) for z0 in range(M) for z1 in range(M)]
out.append(f"setup: d = 2, SU(2), n = {n}, coarse side {Tc}; U0 n max|A| = 0.3; descents max|d*w| = {max(errs):.1e}; "
           f"corner spread: U0 max {max(sp0):.3f}, U_s min/median/max {min(sp):.3f}/{np.median(sp):.3f}/{max(sp):.3f}")

Gs = glue(nfs)
PiS = gauge(Us, Gs)
k1 = max(float(np.linalg.norm(qlog(Gs[c[0], c[1]]))) for c in roots)
K1 = k1 <= 1e-12
out.append(f"K1 root values max|log G^off(U_s)(c_Y)| = {k1:.1e}: {'PASS' if K1 else 'FAIL'}")

# K2 face consistency: sites with t_nu = 0 recomputed from the lower neighbour cell with t_nu = 1
k2 = 0.0
for z0 in range(M):
    for z1 in range(M):
        X = (z0 // n, z1 // n)
        t = ((z0 - n * X[0]) / n, (z1 - n * X[1]) / n)
        for nu in (0, 1):
            if t[nu] == 0.0:
                Xn = list(X); Xn[nu] = (Xn[nu] - 1) % Tc
                tn = list(t); tn[nu] = 1.0
                # sigma_5(1) = 0, so w = 1 on the upper corner
                P = corner_points(nfs, (z0, z1), tuple(Xn))
                w0, w1 = 1 - sig5(tn[0]), 1 - sig5(tn[1])
                Q0 = m_w(P[(0, 0)], P[(1, 0)], w0)
                Q1 = m_w(P[(0, 1)], P[(1, 1)], w0)
                val = m_w(Q0, Q1, w1)
                k2 = max(k2, float(qdist(val, Gs[z0, z1])))
K2 = k2 <= 1e-12
out.append(f"K2 face consistency max distance = {k2:.1e}: {'PASS' if K2 else 'FAIL'}")

# K3 G_0 invariance (descent)
g0 = haar((M, M))
for c in roots:
    g0[c[0], c[1]] = np.array([1.0, 0, 0, 0])
Ug = gauge(Us, g0)
st3 = [perturbed(qmul(nfs[i][0], qinv(boxed(g0, c)))) for i, c in enumerate(roots)]
nfg = nf_all(Ug, st3)
Pig = gauge(Ug, glue(nfg))
k3 = float(qdist(Pig, PiS).max())
K3 = k3 <= 1e-8
out.append(f"K3 G_0-invariance max link distance = {k3:.1e} (descents max|d*w| {max(e for _, e in nfg):.1e}): {'PASS' if K3 else 'FAIL'}")

# K4 constant covariance (NF-cov transport)
cst = haar(())
cfull = np.broadcast_to(cst, (M, M, 4)).copy()
nfc = transported(nfs, [cst] * len(roots), cfull)
Pic = gauge(gauge(Us, cfull), glue(nfc))
k4 = float(qdist(Pic, gauge(PiS, cfull)).max())
K4 = k4 <= 1e-8
out.append(f"K4 constant covariance max link distance = {k4:.1e}: {'PASS' if K4 else 'FAIL'}")

# K5 idempotence (descent)
st5 = [perturbed(qmul(nfs[i][0], qinv(boxed(Gs, c)))) for i, c in enumerate(roots)]
nfp = nf_all(PiS, st5)
k5 = float(np.linalg.norm(qlog(glue(nfp)), axis=-1).max())
K5 = k5 <= 1e-8
out.append(f"K5 idempotence max|log G^off(Pi^off(U_s))| = {k5:.1e} (descents max|d*w| {max(e for _, e in nfp):.1e}): "
           f"{'PASS' if K5 else 'FAIL'}")

# K6 root-value covariance for a Haar level-0 gauge k (NF-cov transport)
kg = haar((M, M))
kroot = [kg[c[0], c[1]] for c in roots]
nfk = transported(nf0, kroot, kg)
G0 = glue(nf0)
Pi0 = gauge(U0, G0)
Pik = gauge(gauge(U0, kg), glue(nfk))
hhat = qmul(glue(nf0, left=kroot), qinv(G0))
k6 = float(qdist(Pik, gauge(Pi0, hhat)).max())
k6r = max(float(qdist(hhat[c[0], c[1]], kg[c[0], c[1]])) for c in roots)
K6 = k6 <= 1e-8 and k6r <= 1e-12
out.append(f"K6 root-value covariance max link distance = {k6:.1e}, max d(hhat(c_Y), k(c_Y)) = {k6r:.1e}: {'PASS' if K6 else 'FAIL'}")

# K7 continuity along a gauge path
zeta = rng.standard_normal((len(roots), 3))
zeta /= np.linalg.norm(zeta, axis=-1, keepdims=True)
zeta *= rng.uniform(0, 2.5, (len(roots), 1))
prevG, prevr = None, None
step_out, step_in, zone = 0.0, 0.0, []
for s in range(41):
    t = s / 40
    hr = [qexp(t * zeta[i]) for i in range(len(roots))]
    Gh = glue(nf0, left=hr)          # = G^off(U0^{h_t}) h_t (right equivariance)
    if prevG is not None:
        step_out = max(step_out, float(qdist(Gh, prevG).max()))
        step_in = max(step_in, max(float(qdist(hr[i], prevr[i])) for i in range(len(roots))))
    nz = 0
    for z0 in range(M):
        for z1 in range(M):
            X = (z0 // n, z1 // n)
            P = corner_points(nf0, (z0, z1), X)
            P = {e: qmul(hr[RIDX[((X[0] + e[0]) % Tc, (X[1] + e[1]) % Tc)]], p) for e, p in P.items()}
            dd = max(float(qdist(p, q)) for p in P.values() for q in P.values())
            nz += dd > R1
    zone.append(nz / M ** 2)
    prevG, prevr = Gh, hr
K7 = step_out <= 20 * step_in
out.append(f"K7 continuity: max output step {step_out:.4f} vs max root step {step_in:.4f} (ratio {step_out / step_in:.2f} <= 20): "
           f"{'PASS' if K7 else 'FAIL'}; fraction of sites with spread > r_1 along the path: start {zone[0]:.2f}, "
           f"middle {zone[20]:.2f}, end {zone[-1]:.2f}")

# K8 clustered data: G^off = m^geo exactly on U0
Ggeo = glue(nf0, cut=False)
k8 = float(qdist(G0, Ggeo).max())
K8 = k8 <= 1e-14
# informational: Karcher gluing on U0
Gk = np.zeros((M, M, 4))
for z0 in range(M):
    for z1 in range(M):
        X = (z0 // n, z1 // n)
        t = ((z0 - n * X[0]) / n, (z1 - n * X[1]) / n)
        P = corner_points(nf0, (z0, z1), X)
        wts = [sig5(t[0]) if e[0] == 0 else 1 - sig5(t[0]) for e in P]
        wts = [w * (sig5(t[1]) if e[1] == 0 else 1 - sig5(t[1])) for w, e in zip(wts, P)]
        Gk[z0, z1], _ = karcher(list(P.values()), wts, P[(0, 0)])
out.append(f"K8 clustered data: max d(G^off, m^geo) = {k8:.1e}: {'PASS' if K8 else 'FAIL'}; informational max d(m^geo, Karcher) = "
           f"{float(qdist(Ggeo, Gk).max()):.2e}")

# K9 informational: frame representative
hh = qmul(glue(nf0, left=hroot), qinv(G0))
back = gauge(PiS, qinv(hh))
out.append(f"K9 informational: max d(Pi^off(U_s)^(hhat^-1), Pi^off(U0)) = {float(qdist(back, Pi0).max()):.1e}; "
           f"n max|log| links: Pi^off(U0) {n * float(np.linalg.norm(qlog(Pi0), axis=-1).max()):.4f}, "
           f"Pi^off(U_s) {n * float(np.linalg.norm(qlog(PiS), axis=-1).max()):.4f}")

# K10 control: Karcher on spread data from two starts
k10, nonconv = 0.0, 0
for z0 in range(M):
    for z1 in range(M):
        X = (z0 // n, z1 // n)
        t = ((z0 - n * X[0]) / n, (z1 - n * X[1]) / n)
        P = corner_points(nfs, (z0, z1), X)
        keys = list(P)
        wts = np.array([(sig5(t[0]) if e[0] == 0 else 1 - sig5(t[0])) * (sig5(t[1]) if e[1] == 0 else 1 - sig5(t[1]))
                        for e in keys])
        if (wts > 0).sum() < 2:
            continue
        pts = [P[e] for e in keys]
        pos = [i for i in range(4) if wts[i] > 0]
        ia = max(pos, key=lambda i: wts[i]); ib = min(pos, key=lambda i: wts[i])
        ma, ca = karcher(pts, wts, pts[ia])
        mb, cb = karcher(pts, wts, pts[ib])
        nonconv += (not ca) + (not cb)
        k10 = max(k10, float(qdist(ma, mb)))
K10 = k10 >= 0.1 or nonconv > 0
out.append(f"K10 control (Karcher on spread data): max disagreement between two starts = {k10:.3f}, non-converged runs = {nonconv}: "
           f"{'PASS' if K10 else 'FAIL'}")
allp = K1 and K2 and K3 and K4 and K5 and K6 and K7 and K8 and K10
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (K1-K8, K10)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
