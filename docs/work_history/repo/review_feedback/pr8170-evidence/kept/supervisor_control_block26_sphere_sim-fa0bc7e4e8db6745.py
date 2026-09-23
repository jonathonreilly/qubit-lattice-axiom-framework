# Exploration: the unsoldered (sphere) formation law in level time on a periodic L x L level plane.
# New spin at x ~ exp(beta s . S), S = s_{x-e1} + s_{x-e2} + s_{x-e3}; in plane coordinates the three predecessors of (i,j) are
# (i,j) [the e1-predecessor, projected onto the plane through the bijection x -> (x2, x3)], (i-1,j), (i,j-1).
# Exact vMF sampling on S^2: cosine w = 1 + log(u + (1-u) e^{-2 kappa})/kappa, uniform azimuth.
import numpy as np, sys, time
def run(beta, L, T, seed=0, record_every=1):
    rng = np.random.default_rng(seed)
    s = np.zeros((L, L, 3)); s[..., 2] = 1.0   # aligned initial plane (pole)
    out = []
    for t in range(1, T + 1):
        S = s + np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1)
        norm = np.linalg.norm(S, axis=2); u = S / norm[..., None]; kappa = beta * norm
        U = rng.random((L, L)); w = 1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa
        w = np.clip(w, -1.0, 1.0)
        phi = rng.random((L, L)) * 2 * np.pi
        # orthonormal tangent frame at u
        a = np.where((np.abs(u[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
        e1 = a - (a * u).sum(-1)[..., None] * u; e1 /= np.linalg.norm(e1, axis=2)[..., None]
        e2 = np.cross(u, e1)
        r = np.sqrt(np.clip(1 - w * w, 0, 1))
        s = w[..., None] * u + r[..., None] * (np.cos(phi)[..., None] * e1 + np.sin(phi)[..., None] * e2)
        if t % record_every == 0:
            m = s.mean(axis=(0, 1)); out.append((t, np.linalg.norm(m), m[2]))
    return out
beta = float(sys.argv[1]); L = int(sys.argv[2]); T = int(sys.argv[3])
t0 = time.time(); res = run(beta, L, T, seed=1, record_every=max(1, T // 40))
print(f"beta={beta} L={L} T={T} ({time.time()-t0:.0f}s)")
for t, m, mz in res:
    print(f"  t={t:6d}  |m|={m:.5f}  m_z={mz:.5f}")
