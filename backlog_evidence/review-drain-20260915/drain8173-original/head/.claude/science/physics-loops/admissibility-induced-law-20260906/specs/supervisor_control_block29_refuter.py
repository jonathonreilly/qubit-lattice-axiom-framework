"""Refuting pass, block 29 (independent machinery): (a) the normalization from the REAL-SPACE transverse correlation: fit T(r) = c G_L(r)/beta
with the torus Green function G_L computed by FFT (a different estimator from the structure factor); (b) a Metropolis single-site sampler
(a different chain) at beta = 1.5 on 16^3 measuring beta E(k) S_perp(k); (c) the transverse sum rule in a field: beta h N <(m^1)^2> against
<m^3> at h = 0.05, 0.1 on 16^3, beta = 1.5 (heat bath with the field added to the neighbour sum)."""
import numpy as np, time
rng = np.random.default_rng(37)
L = 16; N = L**3; idx = np.indices((L, L, L)).sum(0) % 2
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
def nbsum(s): return sum(np.roll(s, sh, ax) for ax in range(3) for sh in (1, -1))
# torus Green function along an axis: G_L(r) = (1/N) sum_{k != 0} e^{i k.r} / E(k)
kx = 2 * np.pi * np.fft.fftfreq(L) * L / L; K1, K2, K3 = np.meshgrid(kx, kx, kx, indexing="ij")
E = 2 * (3 - np.cos(K1) - np.cos(K2) - np.cos(K3)); invE = np.where(E > 1e-12, 1 / np.where(E > 1e-12, E, 1), 0.0)
G = np.real(np.fft.ifftn(invE))   # G_L(r) with G_L(0) = (1/N) sum_{k!=0} 1/E(k)
print(f"(a) torus Green function G_L(r) along e_1 (L=16): {' '.join(f'{G[r,0,0]:.4f}' for r in range(6))}")
for beta in (1.0, 1.5, 2.0):
    s = np.zeros((L, L, L, 3)); s[..., 2] = 1; Tr = np.zeros(L // 2 + 1); ms = []; cnt = 0; t0 = time.time()
    for sw in range(3000):
        for par in (0, 1):
            s = np.where((idx == par)[..., None], vmf(beta * nbsum(s)), s)
        if sw >= 1000 and sw % 2 == 0:
            M = s.mean((0, 1, 2)); m = np.linalg.norm(M); u = M / m; sp = s - (s @ u)[..., None] * u; ms.append(m)
            for r in range(L // 2 + 1): Tr[r] += (sp * np.roll(sp, r, 0)).sum(-1).mean() / 2
            cnt += 1
    Tr /= cnt
    # fit c from r = 1..4 (r = 0 carries the local, non-Green part): c = beta * T(r) / G_L(r)
    cs = [beta * Tr[r] / G[r, 0, 0] for r in range(1, 5)]
    print(f"  beta={beta}: m = {np.mean(ms):.4f}; T(r) r=0..5: {' '.join(f'{Tr[r]:.4f}' for r in range(6))}; c from T(r)/(G_L(r)/beta), r=1..4: {' '.join(f'{c:.3f}' for c in cs)}   ({time.time()-t0:.0f}s)")
print("(b) Metropolis single-site chain at beta = 1.5 on 16^3: beta E(k) S_perp(k) for n = 1..6")
beta = 1.5; s = np.zeros((L, L, L, 3)); s[..., 2] = 1; ks = np.arange(1, 7); Ek = 2 * (1 - np.cos(2 * np.pi * ks / L)); Sk = np.zeros(len(ks)); cnt = 0; t0 = time.time()
for sw in range(4000):
    for par in (0, 1):
        g = rng.normal(size=(L, L, L, 3)); prop = s + 0.6 * g; prop /= np.linalg.norm(prop, axis=-1)[..., None]
        V = nbsum(s); dE = beta * ((prop - s) * V).sum(-1)
        acc = (rng.random((L, L, L)) < np.exp(np.minimum(0, dE))) & (idx == par)
        s = np.where(acc[..., None], prop, s)
    if sw >= 1500 and sw % 2 == 0:
        M = s.mean((0, 1, 2)); u = M / np.linalg.norm(M); sp = s - (s @ u)[..., None] * u
        F = np.fft.fftn(sp, axes=(0, 1, 2)); Sk += (np.abs(F[ks, 0, 0, :]) ** 2).sum(-1) / N / 2; cnt += 1
Sk /= cnt
print(f"  {' '.join(f'{beta*Ek[i]*Sk[i]:.3f}' for i in range(len(ks)))}   ({time.time()-t0:.0f}s)")
print("(c) the transverse sum rule in a field h e_3 at beta = 1.5 on 16^3: beta h N <(m^1)^2> against <m^3>")
for h in (0.05, 0.1, 0.2):
    s = np.zeros((L, L, L, 3)); s[..., 2] = 1; m1sq = []; m3 = []; t0 = time.time()
    for sw in range(3000):
        for par in (0, 1):
            V = nbsum(s) + np.array([0, 0, h]); s = np.where((idx == par)[..., None], vmf(beta * V), s)
        if sw >= 1000:
            M = s.mean((0, 1, 2)); m1sq.append(M[0] ** 2); m3.append(M[2])
    print(f"  h={h}: beta h N <(m^1)^2> = {beta*h*N*np.mean(m1sq):.4f}  <m^3> = {np.mean(m3):.4f}   ({time.time()-t0:.0f}s)")
