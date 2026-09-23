# Sphere static law (weight e^{beta s.s'}) on a periodic L^3 lattice, heat-bath checkerboard sweeps from an aligned start.
# Measures: m = |mean s|; the transverse structure factor S_perp(k) = (1/N) E|sum_x s_perp(x) e^{-ik.x}|^2 per transverse component,
# for k = (2 pi n/L, 0, 0), n = 1..L/2, with s_perp the components orthogonal to the instantaneous plane average; and the real-space
# transverse correlation T(r) = E[s_perp(0).s_perp(r e_1)]/2 along an axis.  Compare beta E(k) S_perp(k) with the bounds (M^2/3)^2 .. 1
# (block 19) and with m^2; E(k) = 2 sum_j (1 - cos k_j).
import numpy as np, sys, time
L, sweeps, therm = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); betas = [float(x) for x in sys.argv[4:]]
rng = np.random.default_rng(29); idx = np.indices((L, L, L)).sum(0) % 2
def vmf(V):
    n = np.linalg.norm(V, axis=-1); kap = np.maximum(n, 1e-12); u = V / kap[..., None]
    U = rng.random(n.shape); w = np.clip(1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap, -1, 1); ph = 2 * np.pi * rng.random(n.shape)
    a = np.where((np.abs(u[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    e1 = a - (a * u).sum(-1)[..., None] * u; e1 /= np.linalg.norm(e1, axis=-1)[..., None]; e2 = np.cross(u, e1)
    rr = np.sqrt(np.clip(1 - w * w, 0, 1)); s = w[..., None] * u + rr[..., None] * (np.cos(ph)[..., None] * e1 + np.sin(ph)[..., None] * e2)
    zero = n <= 1e-12
    if zero.any():
        g = rng.normal(size=s[zero].shape); s[zero] = g / np.linalg.norm(g, axis=-1)[..., None]
    return s
ks = np.arange(1, L // 2 + 1); E = 2 * (1 - np.cos(2 * np.pi * ks / L))
print(f"sphere static law, L={L}, sweeps={sweeps} (thermalisation {therm}); k = 2 pi n/L along e_1; E(k) = 2(1 - cos k)")
for beta in betas:
    s = np.zeros((L, L, L, 3)); s[..., 2] = 1; ms = []; Sk = np.zeros(len(ks)); Tr = np.zeros(L // 2 + 1); cnt = 0; t0 = time.time()
    for sw in range(sweeps):
        for par in (0, 1):
            V = sum(np.roll(s, sh, ax) for ax in range(3) for sh in (1, -1))
            s = np.where((idx == par)[..., None], vmf(beta * V), s)
        if sw >= therm and sw % 2 == 0:
            M = s.mean((0, 1, 2)); m = np.linalg.norm(M); ms.append(m); u = M / m
            sp = s - (s @ u)[..., None] * u                      # transverse components (two of them)
            F = np.fft.fftn(sp, axes=(0, 1, 2))                  # shape L,L,L,3
            Sk += (np.abs(F[ks, 0, 0, :]) ** 2).sum(-1) / (L ** 3) / 2     # per transverse component
            for r in range(L // 2 + 1):
                Tr[r] += (sp * np.roll(sp, r, 0)).sum(-1).mean() / 2
            cnt += 1
    Sk /= cnt; Tr /= cnt; m = np.mean(ms)
    print(f"  beta={beta:4.2f}: m = {m:.4f}, m^2 = {m*m:.4f}, (m^2/3)^2 = {(m*m/3)**2:.4f}   ({time.time()-t0:.0f}s)")
    print("    n  beta E(k) S_perp(k):", " ".join(f"{beta*E[i]*Sk[i]:.3f}" for i in range(min(8, len(ks)))))
    print("    T(r) r=0..8:", " ".join(f"{Tr[r]:.4f}" for r in range(min(9, L // 2 + 1))))
