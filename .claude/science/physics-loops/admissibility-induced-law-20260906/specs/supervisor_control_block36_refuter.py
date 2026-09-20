"""Refuting pass, block 36 (machinery disjoint from the chain's own sampler): single-site Metropolis sampling of the EQUILIBRIUM laws
that T1 and T2 name, compared with the stationary magnetization of the re-recording chains (which use an exact vMF heat bath).
 (a) seven-site stencil: Metropolis on the doubled graph Gamma (two layers; every edge joins the layers), observable |m_0| of one layer,
     against the synchronous chain s_{t+1}(x) ~ exp(beta s . sum of the 7 tick-t records).
 (b) six-site stencil (the axioms' nearest-neighbour rule): Metropolis on the static law exp(beta sum_<xy> s_x.s_y) on Z^3, observable the
     magnetization of the whole configuration, against the space-time checkerboard of the synchronous chain (class A at tick t, class B at
     tick t+1).
usage: refuter.py L beta sweeps seed"""
import numpy as np, sys, time
L = int(sys.argv[1]); beta = float(sys.argv[2]); sweeps = int(sys.argv[3]); seed = int(sys.argv[4]); rng = np.random.default_rng(seed)
shape = (L, L, L); e0 = np.array([0.0, 0.0, 1.0])
def nbr_sum(s, with_self):
    S = sum(np.roll(s, 1, axis=j) + np.roll(s, -1, axis=j) for j in range(3))
    return S + s if with_self else S
def vmf(V):
    kappa = np.linalg.norm(V, axis=-1); kappa = np.where(kappa < 1e-12, 1e-12, kappa); uu = V / kappa[..., None]
    U = rng.random(V.shape[:-1]); w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa, -1.0, 1.0); ph = rng.random(V.shape[:-1]) * 2 * np.pi
    a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    b1 = a - (a * uu).sum(-1)[..., None] * uu; b1 /= np.linalg.norm(b1, axis=-1)[..., None]; b2 = np.cross(uu, b1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * b1 + np.sin(ph)[..., None] * b2)
def metropolis(s, field, mask=None, step=0.6):
    prop = s + step * rng.normal(size=s.shape); prop /= np.linalg.norm(prop, axis=-1)[..., None]
    dE = beta * ((prop - s) * field).sum(-1); acc = np.log(rng.random(s.shape[:-1])) < dE
    if mask is not None: acc &= mask
    return np.where(acc[..., None], prop, s), acc.mean()
par = np.indices(shape).sum(0) % 2
t0 = time.time()
# (a) seven-site stencil
s = np.broadcast_to(e0, shape + (3,)).copy(); ms = []
for t in range(sweeps):
    s = vmf(beta * nbr_sum(s, True))
    if t >= sweeps // 2: ms.append(np.linalg.norm(s.reshape(-1, 3).mean(0)))
chain7 = np.mean(ms)
a0 = np.broadcast_to(e0, shape + (3,)).copy(); a1 = a0.copy(); ms = []
for t in range(sweeps):
    for _ in range(2):
        a0, _ = metropolis(a0, nbr_sum(a1, True)); a1, _ = metropolis(a1, nbr_sum(a0, True))
    if t >= sweeps // 2: ms.append(np.linalg.norm(a0.reshape(-1, 3).mean(0)))
eq7 = np.mean(ms)
print(f"(a) seven-site stencil, L={L}, beta={beta}: chain plateau |m_0| = {chain7:.4f}; Metropolis on the doubled graph, one layer: {eq7:.4f}; difference {chain7-eq7:+.4f}")
# (b) six-site stencil
s = np.broadcast_to(e0, shape + (3,)).copy(); ms = []
for t in range(sweeps):
    s_new = vmf(beta * nbr_sum(s, False))
    if t >= sweeps // 2:
        cb = np.where((par == t % 2)[..., None], s, s_new)      # class (t mod 2) at tick t, the other class at tick t+1
        ms.append(np.linalg.norm(cb.reshape(-1, 3).mean(0)))
    s = s_new
chain6 = np.mean(ms)
c = np.broadcast_to(e0, shape + (3,)).copy(); ms = []
for t in range(sweeps):
    for p_ in (0, 1):
        for _ in range(2): c, _ = metropolis(c, nbr_sum(c, False), mask=(par == p_))
    if t >= sweeps // 2: ms.append(np.linalg.norm(c.reshape(-1, 3).mean(0)))
eq6 = np.mean(ms)
print(f"(b) six-site stencil, L={L}, beta={beta}: space-time checkerboard of the synchronous chain |m| = {chain6:.4f}; Metropolis on the static law: {eq6:.4f}; difference {chain6-eq6:+.4f}   ({time.time()-t0:.0f}s)")
