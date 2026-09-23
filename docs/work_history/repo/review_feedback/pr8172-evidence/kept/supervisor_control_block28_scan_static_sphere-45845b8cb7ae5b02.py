# Sphere static law (weight e^{beta s.s'}) on a periodic L^3 lattice: heat-bath checkerboard sweeps with the exact conditional
# (exponential-overlap law with concentration beta |sum of 6 neighbours|); |magnetization| over the last half, aligned start.
import numpy as np, sys, time
L, sweeps = int(sys.argv[1]), int(sys.argv[2]); betas = [float(x) for x in sys.argv[3:]]
rng = np.random.default_rng(3)
idx = np.indices((L, L, L)).sum(0) % 2
def vmf(V):
    n = np.linalg.norm(V, axis=-1); kap = np.maximum(n, 1e-12); u = V / kap[..., None]
    U = rng.random(n.shape); w = np.clip(1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap, -1, 1); ph = 2 * np.pi * rng.random(n.shape)
    a = np.where((np.abs(u[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    e1 = a - (a * u).sum(-1)[..., None] * u; e1 /= np.linalg.norm(e1, axis=-1)[..., None]; e2 = np.cross(u, e1)
    rr = np.sqrt(np.clip(1 - w * w, 0, 1))
    s = w[..., None] * u + rr[..., None] * (np.cos(ph)[..., None] * e1 + np.sin(ph)[..., None] * e2)
    zero = n <= 1e-12
    if zero.any():
        g = rng.normal(size=s[zero].shape); s[zero] = g / np.linalg.norm(g, axis=-1)[..., None]
    return s
print(f"sphere static law, L={L}, sweeps={sweeps}; |m| over the last half, aligned start")
for beta in betas:
    s = np.zeros((L, L, L, 3)); s[..., 2] = 1; ms = []; t0 = time.time()
    for sw in range(sweeps):
        for par in (0, 1):
            V = np.zeros_like(s)
            for ax in range(3):
                for sh in (1, -1):
                    V = V + np.roll(s, sh, ax)
            new = vmf(beta * V)
            s = np.where((idx == par)[..., None], new, s)
        if sw >= sweeps // 2: ms.append(np.linalg.norm(s.mean((0, 1, 2))))
    print(f"  beta={beta:5.3f}: |m| = {np.mean(ms):.4f}   ({time.time()-t0:.0f}s)")
