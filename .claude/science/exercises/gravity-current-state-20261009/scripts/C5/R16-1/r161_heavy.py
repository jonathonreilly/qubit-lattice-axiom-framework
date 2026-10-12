"""R16-1 heavy-electron linear coefficient for Wilson-box electrons (Theorem W of the report).
Static limit (m -> infinity, p in the box, along x): the on-shell energy shift tends to
   dE0(p) = const + < Omega(q ; W(p - q_x)) >_q,
   Omega(q; u) = u [D^2 - t (1 - A')] / (2 t Wg D (D + u)),   t = d(q_x)^2, Wg = sqrt(t + d_y^2 + d_z^2 + lam^2),
   D = Wg + W(q_y) + W(q_z),  A' = W(q_y)^2/d_y^2 + W(q_z)^2/d_z^2,
and dc_e(m) = L m + O(1) with   L = (1/2) d^2/dp^2 <Omega(q; W(p-q_x))> |_{p=0}
                                  = (1/2) < [d^2/dq_x^2 Omega(q; u)]_{u = W(q_x)} >   (photon-slot derivative).
Both forms are computed (independent quadratures: p-difference vs photon-slot difference).
Units: printed x 16 pi^2 (e^2/16pi^2 per unit lattice mass).
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
U = 16 * np.pi ** 2

def _gl(a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def Omega(law, qx_ph, u, dy2, dz2, Wy, Wz, lam):
    t = law.d(qx_ph) ** 2
    Wg = np.sqrt(t + dy2 + dz2 + lam ** 2)
    D = Wg + Wy + Wz
    Ap = Wy ** 2 / dy2 + Wz ** 2 / dz2
    return u * (D ** 2 - t * (1 - Ap)) / (2 * t * Wg * D * (D + u))

def perp_grid(law, Np):
    q = (np.arange(Np) + 0.5) * 2 * np.pi / Np - np.pi
    QY, QZ = np.meshgrid(q, q, indexing='ij')
    return (law.d(QY) ** 2)[None], (law.d(QZ) ** 2)[None], np.maximum(law.W(QY), 0)[None], np.maximum(law.W(QZ), 0)[None]

def L_photon_slot(law, lam, Np=64, nx=400, h=1e-3, chunk=50):
    """(1/2)< d^2_qx Omega(q;u)|_{u=W(q_x)} >, q_x over supp W = [b, pi] (x2 by evenness)."""
    b = getattr(law, 'b', None) or law.b1
    xs, ws = [], []
    # split [b, pi] into panels (Gevrey transitions are flat but steep)
    edges = np.linspace(b, np.pi, 41)
    for a0, a1 in zip(edges[:-1], edges[1:]):
        x, w = _gl(a0, a1, nx // 40); xs.append(x); ws.append(w)
    qx = np.concatenate(xs); wx = np.concatenate(ws)
    dy2, dz2, Wy, Wz = perp_grid(law, Np)
    tot = 0.0
    for i0 in range(0, len(qx), chunk):
        q = qx[i0:i0 + chunk][:, None, None]; u = np.maximum(law.W(q), 0)
        f = lambda s: Omega(law, q + s, u, dy2, dz2, Wy, Wz, lam)
        d2 = (-f(2 * h) + 16 * f(h) - 30 * f(0) + 16 * f(-h) - f(-2 * h)) / (12 * h * h)
        tot += np.sum(wx[i0:i0 + chunk][:, None, None] * d2.mean(axis=(1, 2), keepdims=True)[:, :, :] ) if False else np.sum(wx[i0:i0 + chunk] * d2.mean(axis=(1, 2)))
    avg = 2 * tot / (2 * np.pi)          # x2: q_x in [-pi,-b] by evenness; /(2 pi): <.> over q_x
    return 0.5 * avg

def L_p_difference(law, lam, Np=64, nx=400, hp=(0.02, 0.01), chunk=50):
    """(1/2) d^2/dp^2 < Omega(q; W(p - q_x)) > by central differences in p (Richardson), q_x over both signs."""
    b = getattr(law, 'b', None) or law.b1
    lo = max(b - 0.06, 0.05)
    xs, ws = [], []
    edges = np.linspace(lo, np.pi, 41)
    for a0, a1 in zip(edges[:-1], edges[1:]):
        x, w = _gl(a0, a1, nx // 40); xs.append(x); ws.append(w)
    qx = np.concatenate(xs); wx = np.concatenate(ws)
    qx = np.concatenate([qx, -qx]); wx = np.concatenate([wx, wx])
    dy2, dz2, Wy, Wz = perp_grid(law, Np)
    def avg(p):
        tot = 0.0
        for i0 in range(0, len(qx), chunk):
            q = qx[i0:i0 + chunk][:, None, None]; u = np.maximum(law.W(p - q), 0)
            tot += np.sum(wx[i0:i0 + chunk] * Omega(law, q, u, dy2, dz2, Wy, Wz, lam).mean(axis=(1, 2)))
        return tot / (2 * np.pi)
    a0 = avg(0.0)
    D = [(avg(h) + avg(-h) - 2 * a0) / h ** 2 for h in hp]
    return 0.5 * (4 * D[1] - D[0]) / 3, a0

def H3_check(law, n=200001):
    k = np.linspace(-np.pi, np.pi, n)
    W = np.maximum(law.W(k), 0); d = np.abs(law.d(k))
    rho = np.where(d > 1e-12, W / np.maximum(d, 1e-300), 0.0)
    return rho.max(), W.min()
