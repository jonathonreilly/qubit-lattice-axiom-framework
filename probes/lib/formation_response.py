"""formation_response.py dim beta L T T0 h seed      (dim = 3 backward past, 3s symmetric light-cone past; also 2, 2s)

The potential around a persistent source under the formation reading.  Two copies of the sphere formation law run with the SAME
random numbers; in the second a field h along a transverse direction acts on the record at ONE site at every level (weight
exp(beta s.S + h s.t1) there).  Output: the mean transverse displacement of the second copy relative to the first, averaged over
levels T0 < t <= T, along e_1 and along the body diagonal, against the linear prediction
    delta(x) = (h / (n beta)) * [ (1 - P)^-1 delta_0 ](x),   P the predecessor average, symbol phi(k), zero mode removed.
For the light-cone past phi = 1 - E(k)/7, so (1 - P)^-1 = 7/E(k): the lattice Green function, a 1/r potential.  For the backward
past the response lives in the forward cone.  Common random numbers make the difference a low-noise estimate."""
import numpy as np, sys, time
sym = sys.argv[1].endswith("s"); dim = int(sys.argv[1].rstrip("s")); beta = float(sys.argv[2]); L = int(sys.argv[3]); T = int(sys.argv[4]); T0 = int(sys.argv[5]); h = float(sys.argv[6]); seed = int(sys.argv[7])
n = (2 * dim + 1) if sym else (dim + 1); shape = (L,) * dim; rng = np.random.default_rng(seed)
e0 = np.array([0.0, 0.0, 1.0]); t1 = np.array([1.0, 0.0, 0.0]); origin = (0,) * dim
def step(s, U, ph, field):
    S = s + sum(np.roll(s, 1, axis=j) + (np.roll(s, -1, axis=j) if sym else 0) for j in range(dim))
    V = beta * S
    if field: V[origin] = V[origin] + h * t1
    kappa = np.linalg.norm(V, axis=-1); kappa = np.where(kappa < 1e-12, 1e-12, kappa); uu = V / kappa[..., None]
    w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa, -1.0, 1.0)
    a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    b1 = a - (a * uu).sum(-1)[..., None] * uu; b1 /= np.linalg.norm(b1, axis=-1)[..., None]; b2 = np.cross(uu, b1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * b1 + np.sin(ph)[..., None] * b2)
s0 = np.broadcast_to(e0, shape + (3,)).copy(); s1 = s0.copy(); acc = np.zeros(shape); cnt = 0; t_start = time.time()
for t in range(1, T + 1):
    U = rng.random(shape); ph = rng.random(shape) * 2 * np.pi
    s0 = step(s0, U, ph, False); s1 = step(s1, U, ph, True)
    if t > T0: acc += (s1 - s0) @ t1; cnt += 1
resp = acc / cnt; resp -= resp.mean()
grids = np.meshgrid(*([2 * np.pi * np.arange(L) / L] * dim), indexing="ij")
phi = ((1 + sum(2 * np.cos(g) for g in grids)) / n + 0j) if sym else (1 + sum(np.exp(-1j * g) for g in grids)) / n
mask = np.ones(shape, dtype=bool); mask[origin] = False
lin = np.fft.ifftn(np.where(mask, 1.0 / np.where(mask, 1 - phi, 1.0), 0.0)).real * h / (n * beta)
m = float(np.linalg.norm(s0.reshape(-1, 3).mean(axis=0)))
print(f"dim={sys.argv[1]} beta={beta} L={L} T={T} T0={T0} h={h} seed={seed}; n={n}; |m| of the unperturbed copy at the end = {m:.4f}")
print("along e_1: r, measured displacement, linear prediction, ratio" + (", r * measured (a 1/r potential gives a plateau)" if dim == 3 else ""))
ratios = []
for r in (1, 2, 3, 4, 6, 8, 12, 16):
    if r <= L // 2:
        ix = (r,) + (0,) * (dim - 1); q = resp[ix] / lin[ix] if abs(lin[ix]) > 1e-15 else float("nan"); ratios.append(q)
        print(f"   {r:3d}  {resp[ix]:+.6f}  {lin[ix]:+.6f}  {q:.3f}" + (f"  {r*resp[ix]:+.6f}" if dim == 3 else ""))
print("along the body diagonal, forward (+) and backward (-): r, measured +, measured -, linear +, linear -")
for r in (1, 2, 3, 4, 6, 8):
    if r <= L // 2:
        ip = (r,) * dim; im = tuple((-r) % L for _ in range(dim)); print(f"   {r:3d}  {resp[ip]:+.6f}  {resp[im]:+.6f}  {lin[ip]:+.6f}  {lin[im]:+.6f}")
near = [q for q in ratios[:4] if q == q]
print(f"SUMMARY: dim={sys.argv[1]} beta={beta} L={L} h={h} mean_ratio_r1to4={np.mean(near) if near else float('nan'):.4f} forward_backward_asymmetry_r2={(resp[(2,)*dim]-resp[tuple((-2)%L for _ in range(dim))]):+.6f} seconds={time.time()-t_start:.0f}")
