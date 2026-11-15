"""bb6n: nonabelian box-Coulomb normal forms and the Karcher-glued slice (lane B session 6), d = 2, SU(2).

Criteria: checks/bb6n_criteria.md (written before this script).
SU(2) = unit quaternions (w, x, y, z); exp(v) = (cos|v|, sin|v| v/|v|); |log| = geodesic distance.
"""
import time

import numpy as np

T0 = time.time()
rng = np.random.default_rng(6262)
n, Tc = 3, 5
M = n * Tc           # fine torus side 15
HW = 2 * n           # box half-width (fine)
S = 2 * HW + 1       # box side 13
TAU = 0.1
TOL = 1e-12
MAXIT = 40000


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


def haar(shape):
    q = rng.standard_normal(shape + (4,))
    return q / np.linalg.norm(q, axis=-1, keepdims=True)


def gauge(U, g):
    """U^g(z, a) = g(z) U(z, a) g(z + e_a)^{-1} on the fine torus (U: (M, M, 2, 4))."""
    out = np.empty_like(U)
    for a in range(2):
        out[:, :, a] = qmul(qmul(g, U[:, :, a]), qinv(np.roll(g, -1, axis=a)))
    return out


# qlog is the principal SU(2) log (angle in [0, pi]); links stay near 1 (asserted in box_w).

def box_extract(U, c):
    idx = (np.arange(-HW, HW + 1) + c[:, None]) % M  # (2, S)
    Ub = U[np.ix_(idx[0], idx[1])]                   # (S, S, 2, 4)
    return Ub, idx


VALID = np.ones((S, S, 2), bool)
VALID[S - 1, :, 0] = False
VALID[:, S - 1, 1] = False
CENTER = (HW, HW)


def box_w(Ub, g):
    w = np.zeros(Ub.shape[:3] + (3,))
    for a in range(2):
        gy = np.roll(g, -1, axis=a)
        W = qmul(qmul(g, Ub[:, :, a]), qinv(gy))
        assert (W[..., 0][VALID[:, :, a]] > 0).all()
        w[:, :, a] = qlog(W)
    w[~VALID] = 0.0
    return w


def box_div(w):
    """D(z) = sum_a [w(z, a) - w(z - e_a, a)] (out minus in; Neumann: invalid links are 0) = -(d*w)(z)."""
    return sum(w[:, :, a] - np.roll(w[:, :, a], 1, axis=a) for a in range(2))


def normal_form(Ub, g0):
    g = g0.copy()
    for it in range(MAXIT):
        w = box_w(Ub, g)
        Dz = box_div(w)
        err = np.abs(Dz).max()
        if err < TOL:
            break
        g = qmul(qexp(-TAU * Dz), g)
    # Phi(c g) = Phi(g) for constants c: normalise the critical point so that g(c_X) = 1
    g = qmul(np.broadcast_to(qinv(g[CENTER]), g.shape), g)
    return g, err, it


def qdist(p, q):
    return np.linalg.norm(qlog(qmul(p, qinv(q))), axis=-1)


out = []
A = rng.standard_normal((M, M, 2, 3))
A *= 0.3 / (n * np.linalg.norm(A, axis=-1).max())
U = qexp(A)


def curv_size(U):
    pl = qmul(qmul(U[:, :, 0], np.roll(U[:, :, 1], -1, axis=0)), qmul(qinv(np.roll(U[:, :, 0], -1, axis=1)), qinv(U[:, :, 1])))
    return n * n * np.linalg.norm(qlog(pl), axis=-1).max()


out.append(f"setup: d = 2, SU(2), n = {n}, coarse side {Tc}, fine side {M}, box side {S}; n max|A| = 0.300, eps_f(U) = {curv_size(U):.4f}")

# N1, N2: one box (root X = (0, 0))
c0 = np.array([0, 0])
Ub, idx = box_extract(U, c0)
ident = np.zeros((S, S, 4)); ident[..., 0] = 1.0
gref, err, it = normal_form(Ub, ident)
wref = box_w(Ub, gref)
N1 = err <= 1e-9
out.append(f"N1 critical equation: max|d*w| = {err:.2e} after {it} steps: {'PASS' if N1 else 'FAIL'}; n max|w| = {n * np.linalg.norm(wref, axis=-1).max():.4f}")
dmax = 0.0
for trial in range(4):
    eta = rng.standard_normal((S, S, 3))
    eta *= 0.5 / np.linalg.norm(eta, axis=-1).max()
    eta[CENTER] = 0.0
    g, err2, it2 = normal_form(Ub, qexp(eta))
    dmax = max(dmax, qdist(g, gref).max())
N2 = dmax <= 1e-7
out.append(f"N2 uniqueness from 4 random starts (|eta| <= 0.5): max distance {dmax:.2e}: {'PASS' if N2 else 'FAIL'}")

# N3: covariance under a Haar-random h
h = haar((M, M))
Uh = gauge(U, h)
Uhb, _ = box_extract(Uh, c0)
hb = h[np.ix_(idx[0], idx[1])]
hc = hb[CENTER]
target = qmul(qmul(np.broadcast_to(hc, hb.shape), gref), qinv(hb))
eta = rng.standard_normal((S, S, 3)); eta *= 0.3 / np.linalg.norm(eta, axis=-1).max(); eta[CENTER] = 0.0
g0 = qmul(qexp(eta), qmul(np.broadcast_to(hc, hb.shape), qinv(hb)))
gh, err3, it3 = normal_form(Uhb, g0)
d3 = qdist(gh, target).max()
N3 = d3 <= 1e-7 and err3 <= 1e-9
out.append(f"N3 covariance g(U^h) = h(c) g(U) h^-1: max distance {d3:.2e} (max|d*w| {err3:.1e}, {it3} steps): {'PASS' if N3 else 'FAIL'}")


# KΠ on the torus
def sig5(t):
    t = np.minimum(np.abs(t), 1.0)
    return 1 - 10 * t ** 3 + 15 * t ** 4 - 6 * t ** 5


def tdist(z, c):
    d = (z - c) % M
    return np.minimum(d, M - d)


roots = [np.array([3 * X0, 3 * X1]) for X0 in range(Tc) for X1 in range(Tc)]
zz = np.indices((M, M)).transpose(1, 2, 0)  # (M, M, 2)


def all_normal_forms(U, starts=None):
    """Return list of (gX on the full torus where defined: dict mapping fine site -> quaternion arrays) as (S,S,4) + idx."""
    res = []
    for i, c in enumerate(roots):
        Ub, idx = box_extract(U, c)
        g0 = ident if starts is None else starts[i]
        g, err, it = normal_form(Ub, g0)
        res.append((g, idx, err))
    return res


def chi_and_local(c, idx_unused=None):
    d = tdist(zz, c)                      # (M, M, 2)
    chi = sig5(d[..., 0] / n) * sig5(d[..., 1] / n)
    return chi


CHI = [chi_and_local(c) for c in roots]


def local_value(g, c, z):
    """value of box normal form g (box of root c) at fine site z (torus), z within HW of c."""
    u = ((z - c + HW) % M)
    return g[u[0], u[1]]


def karcher(points, weights, iters=200):
    m = points[np.argmax(weights)].copy()
    for _ in range(iters):
        step = sum(wt * qlog(qmul(qinv(m), p)) for p, wt in zip(points, weights))
        m = qmul(m, qexp(step))
        if np.linalg.norm(step) < 1e-15:
            break
    return m


def glue(nfs, mode="karcher", left=None):
    """G(z) from normal forms; left: optional per-root left factors (for the ĥ formula)."""
    G = np.zeros((M, M, 4))
    for z0 in range(M):
        for z1 in range(M):
            z = np.array([z0, z1])
            pts, wts = [], []
            for i, c in enumerate(roots):
                wgt = CHI[i][z0, z1]
                if wgt > 0:
                    p = local_value(nfs[i][0], c, z)
                    if left is not None:
                        p = qmul(left[i], p)
                    pts.append(p); wts.append(wgt)
            wts = np.array(wts) / sum(wts)
            if mode == "karcher":
                G[z0, z1] = karcher(pts, wts)
            else:
                G[z0, z1] = qexp(sum(wt * qlog(p) for p, wt in zip(pts, wts)))
    return G


ts = time.time()
nfU = all_normal_forms(U)
G = glue(nfU)
PiU = gauge(U, G)
rootdev = max(np.linalg.norm(qlog(G[c[0], c[1]])) for c in roots)
N4a = rootdev <= 1e-12
nfPi = all_normal_forms(PiU)
GPi = glue(nfPi)
idem = np.linalg.norm(qlog(GPi), axis=-1).max()
N4b = idem <= 1e-7
# covariance
h = haar((M, M))
zeta = rng.standard_normal((len(roots), 3)); zeta *= 0.2 / np.linalg.norm(zeta, axis=-1).max()
for i, c in enumerate(roots):
    h[c[0], c[1]] = qexp(zeta[i])
Uh = gauge(U, h)
starts = []
for i, c in enumerate(roots):
    _, idx = box_extract(U, c)
    hb = h[np.ix_(idx[0], idx[1])]
    hc = hb[HW, HW]
    eta = rng.standard_normal((S, S, 3)); eta *= 0.3 / np.linalg.norm(eta, axis=-1).max(); eta[CENTER] = 0.0
    starts.append(qmul(qexp(eta), qmul(np.broadcast_to(hc, hb.shape), qinv(hb))))
nfUh = all_normal_forms(Uh, starts)
Gh = glue(nfUh)
PiUh = gauge(Uh, Gh)
hroot = [h[c[0], c[1]] for c in roots]
hhat = qmul(glue(nfU, left=hroot), qinv(G))
PiU_hhat = gauge(PiU, hhat)
covdev = qdist(PiUh, PiU_hhat).max()
hroot_dev = max(qdist(hhat[c[0], c[1]], h[c[0], c[1]]) for c in roots)
N4c = covdev <= 1e-7 and hroot_dev <= 1e-12
maxerr = max(e for _, _, e in nfU + nfPi + nfUh)
out.append(f"N4 KΠ (25 boxes x 3 configurations, max|d*w| over all {maxerr:.1e}, {time.time() - ts:.1f} s):")
out.append(f"  (a) max |log G(U)(c_Y)| = {rootdev:.2e}: {'PASS' if N4a else 'FAIL'}")
out.append(f"  (b) idempotence max |log G(Pi(U))| = {idem:.2e}: {'PASS' if N4b else 'FAIL'}")
out.append(f"  (c) covariance max dist(Pi(U^h), Pi(U)^hhat) = {covdev:.2e}, max dist(hhat(c_Y), h(c_Y)) = {hroot_dev:.2e}: "
           f"{'PASS' if N4c else 'FAIL'}")
# N5: exponential-coordinate gluing
Ge = glue(nfU, mode="exp")
Geh = glue(nfUh, mode="exp")
hhat_e = qmul(qmul(Geh, h), qinv(Ge))
dev5 = qdist(hhat_e, hhat).max()
N5 = dev5 >= 1e-4
out.append(f"N5 control (exp-coordinate gluing): max dist(true extension, Karcher root-value formula) = {dev5:.3e} "
           f"(must be >= 1e-4): {'PASS' if N5 else 'FAIL'}")
# N6 informational
wsz = max(n * np.linalg.norm(box_w(box_extract(U, c)[0], nfU[i][0]), axis=-1).max() for i, c in enumerate(roots))
out.append(f"N6 informational: max over boxes n max|w| = {wsz:.4f}; eps_f(U) = {curv_size(U):.4f}; "
           f"Karcher extension at U: max|log hhat| = {np.linalg.norm(qlog(hhat), axis=-1).max():.4f}")
allp = N1 and N2 and N3 and N4a and N4b and N4c and N5
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (N1-N5)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
