# GUIDE only: decimated star-marginal sensitivity on S^3. Not a proof.
import numpy as np, sys
from scipy.special import ive
from scipy.optimize import minimize
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
beta = float(sys.argv[1]) if len(sys.argv) > 1 else 0.7
# quadrature on S^3: h=(cos e cos x1, cos e sin x1, sin e cos x2, sin e sin x2), weight sin e cos e
ne, nx = 28, 40
ge, we = np.polynomial.legendre.leggauss(ne)
eta = (ge + 1) * np.pi / 4; we = we * np.pi / 4 * np.sin(eta) * np.cos(eta)
xs = 2 * np.pi * np.arange(nx) / nx
E, X1, X2 = np.meshgrid(eta, xs, xs, indexing='ij')
W = (we[:, None, None] * np.ones_like(X1)).ravel(); W /= W.sum()
H = np.stack([np.cos(E)*np.cos(X1), np.cos(E)*np.sin(X1), np.sin(E)*np.cos(X2), np.sin(E)*np.sin(X2)], -1).reshape(-1, 4)
def logz(r):
    r = np.asarray(r, float); out = np.empty_like(r); s = r < 1e-4
    out[s] = r[s]**2 / 8
    rr = r[~s]; out[~s] = np.log(2 * ive(1, rr) / rr) + rr
    return out
def afun(k):
    k = np.asarray(k, float); out = np.empty_like(k); s = k < 1e-4
    out[s] = 0.25 - k[s]**2 / 96
    kk = k[~s]; out[~s] = ive(2, kk) / (kk * ive(1, kk))
    return out
def mvec(F):
    k = np.linalg.norm(F, axis=-1); return afun(k)[..., None] * F
def law(F0, Gs):
    lw = H @ F0
    for G in Gs: lw = lw + logz(np.linalg.norm(beta * H + G, axis=1))
    w = W * np.exp(lw - lw.max()); return w / w.sum()
def cov(w, A, B):
    ma = w @ A; mb = w @ B
    return (A * w[:, None]).T @ B - np.outer(ma, mb)
def L_of(F0, Gs):  # linear-test proxy for the decimated price
    w = law(F0, Gs); g = mvec(beta * H + Gs[0])
    return np.linalg.svd(cov(w, H, g), compute_uv=False)[0]
def tau_lin(F0, Gs):  # linear-test proxy for tau of the law
    w = law(F0, Gs); return np.linalg.eigvalsh(cov(w, H, H))[-1]
t = afun(np.array([beta]))[0] * beta
print(f"beta={beta}  t(beta)/4={t/4:.6f}  beta/16={beta/16:.6f}  zero-env L={L_of(np.zeros(4), [np.zeros(4)]*6):.6f}")
def unpack(p, n, f0):
    Gs = [p[4*i:4*i+4] for i in range(n)]
    F0 = p[4*n:4*n+4] if f0 else np.zeros(4)
    return F0, Gs
def clip(p, n, f0):
    q = p.copy()
    for i in range(n):
        v = q[4*i:4*i+4]; r = np.linalg.norm(v)
        if r > 5*beta: q[4*i:4*i+4] = v * 5*beta / r
    if f0:
        v = q[4*n:4*n+4]; r = np.linalg.norm(v)
        if r > 6*beta: q[4*n:4*n+4] = v * 6*beta / r
    return q
for (n, f0) in [(6, False), (5, True), (6, True)]:
    best = (0, None)
    for trial in range(int(sys.argv[3]) if len(sys.argv) > 3 else 12):
        p0 = rng.normal(size=4*n + (4 if f0 else 0)) * rng.uniform(0.05, 1.5) * beta
        f = lambda p: -L_of(*unpack(clip(p, n, f0), n, f0))
        res = minimize(f, p0, method='Powell', options={'maxfev': 1500, 'xtol': 1e-3, 'ftol': 1e-7})
        val = -res.fun
        if val > best[0]: best = (val, clip(res.x, n, f0))
    F0, Gs = unpack(best[1], n, f0)
    print(f"n={n} F0free={f0}: max L={best[0]:.6f} ratio to t/4 = {best[0]/(t/4):.4f}; |G|=",
          np.round([np.linalg.norm(G) for G in Gs], 3), "|F0|=", round(float(np.linalg.norm(F0)), 3))
# tau proxy: max over environments of top covariance eigenvalue for star-type laws
for n in [1, 5, 6]:
    best = (0, None)
    for trial in range(8):
        p0 = rng.normal(size=4*n + 4) * rng.uniform(0.05, 1.5) * beta
        f = lambda p: -tau_lin(*unpack(clip(p, n, True), n, True))
        res = minimize(f, p0, method='Powell', options={'maxfev': 1500, 'xtol': 1e-3, 'ftol': 1e-8})
        if -res.fun > best[0]: best = (-res.fun, clip(res.x, n, True))
    F0, Gs = unpack(best[1], n, True)
    print(f"tau proxy n={n}: max top-eig Cov = {best[0]:.6f} (1/4 = 0.25); |G|=", np.round([np.linalg.norm(G) for G in Gs],3), "|F0|=", round(float(np.linalg.norm(F0)),3))
