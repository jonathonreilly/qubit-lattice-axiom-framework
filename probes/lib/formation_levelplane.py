"""formation_levelplane.py dim menu beta L T T0 seed

The formation law in level order on the event lattice Z^(dim+1): the record at x is drawn given its dim+1 recorded predecessors
(the same plane site one level down and its dim backward neighbours), with weight exp(beta s.S), S the sum of the predecessors'
records; read as a synchronous automaton on the periodic level plane (Z/L)^dim.  dim = 2 is the campaign's law on Z^3 (blocks 26,
34, 35).  dim = 3 is the 3+1 event lattice: three-dimensional level planes, where the plane walk is transient.
menu: sphere (unit vectors, density prop. to exp(beta s.S)); linear (the Gaussian gain-one model with the sphere's transverse
variance sigma^2 = A(n beta)/(n beta), n = dim + 1: the estimator's calibration, expected ratios 1); axes6, corners8, edges12,
fib<N> (finite menus of unit vectors with the same weight).  Start: every record equal to the menu's first vector (sphere: e_z).
Prints the memory table (levels, |m|, projection on the initial direction), then for sphere and linear the equal-level transverse
structure factor against sigma^2/(1 - |phi(k)|^2), phi = (1 + sum_j e^{i k_j})/n, by |k| shell, and the structure function D(r)."""
import numpy as np, sys, time
def A(k): return 1.0 / np.tanh(k) - 1.0 / k
dim = int(sys.argv[1]); menu = sys.argv[2]; beta = float(sys.argv[3]); L = int(sys.argv[4]); T = int(sys.argv[5]); T0 = int(sys.argv[6]); seed = int(sys.argv[7])
n = dim + 1; shape = (L,) * dim; N = L ** dim; rng = np.random.default_rng(seed); sigma2 = A(n * beta) / (n * beta)
def menu_vectors(name):
    if name == "axes6": M = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    elif name == "corners8": M = [(a, b, c) for c in (1, -1) for a in (1, -1) for b in (1, -1)]
    elif name == "edges12": M = [v for v in [(a, b, 0) for a in (1, -1) for b in (1, -1)] + [(a, 0, b) for a in (1, -1) for b in (1, -1)] + [(0, a, b) for a in (1, -1) for b in (1, -1)]]
    elif name.startswith("fib"):
        K = int(name[3:]); i = np.arange(K) + 0.5; z = 1 - 2 * i / K; ph = np.pi * (1 + 5 ** 0.5) * i
        M = np.stack([np.sqrt(1 - z * z) * np.cos(ph), np.sqrt(1 - z * z) * np.sin(ph), z], axis=1)
    else: raise SystemExit("unknown menu " + name)
    M = np.array(M, dtype=float); return M / np.linalg.norm(M, axis=1)[:, None]
grids = np.meshgrid(*([2 * np.pi * np.arange(L) / L] * dim), indexing="ij")
phi = (1 + sum(np.exp(1j * g) for g in grids)) / n; u = np.abs(phi) ** 2; kk = np.sqrt(sum(np.minimum(g, 2 * np.pi - g) ** 2 for g in grids))
mask = np.ones(shape, dtype=bool); mask[(0,) * dim] = False
discrete = menu not in ("sphere", "linear")
if menu == "linear": theta = np.zeros(shape + (2,))
else:
    M = menu_vectors(menu) if discrete else None
    e0 = M[0] if discrete else np.array([0.0, 0.0, 1.0]); s = np.broadcast_to(e0, shape + (3,)).copy()
    ref = np.array([1.0, 0, 0]) if abs(e0[0]) < 0.9 else np.array([0, 1.0, 0]); t1 = ref - (ref @ e0) * e0; t1 /= np.linalg.norm(t1); t2 = np.cross(e0, t1)
marks = sorted(set(int(round(x)) for x in np.geomspace(1, T, 25))); acc = np.zeros(shape); cnt = 0; tail = []; t0 = time.time()
print(f"dim={dim} (event lattice Z^{dim+1}) menu={menu} beta={beta} L={L} T={T} T0={T0} seed={seed}; predecessors n={n}; sigma^2={sigma2:.6f}")
print("memory table: level, |m|, m.e0")
for t in range(1, T + 1):
    if menu == "linear":
        theta = (theta + sum(np.roll(theta, 1, axis=j) for j in range(dim))) / n + rng.normal(0.0, np.sqrt(sigma2), shape + (2,))
        fx, fy = theta[..., 0], theta[..., 1]
    else:
        S = s + sum(np.roll(s, 1, axis=j) for j in range(dim))
        if discrete:
            idx = np.argmax(beta * (S @ M.T) + rng.gumbel(size=shape + (len(M),)), axis=-1); s = M[idx]
        else:
            norm = np.linalg.norm(S, axis=-1); norm = np.where(norm < 1e-12, 1e-12, norm); uu = S / norm[..., None]; kappa = beta * norm
            U = rng.random(shape); w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa, -1.0, 1.0); ph = rng.random(shape) * 2 * np.pi
            a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
            b1 = a - (a * uu).sum(-1)[..., None] * uu; b1 /= np.linalg.norm(b1, axis=-1)[..., None]; b2 = np.cross(uu, b1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
            s = w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * b1 + np.sin(ph)[..., None] * b2)
        m = s.reshape(-1, 3).mean(axis=0)
        if t in marks: print(f"   {t:7d}  {np.linalg.norm(m):.4f}  {m @ e0:+.4f}", flush=True)
        if t > 0.75 * T: tail.append(np.linalg.norm(m))
        fx, fy = s @ t1, s @ t2
    if t > T0 and not discrete:
        acc += 0.5 * (np.abs(np.fft.fftn(fx)) ** 2 + np.abs(np.fft.fftn(fy)) ** 2) / N; cnt += 1
plateau = float(np.mean(tail)) if tail else float("nan"); lowk = float("nan")
if not discrete and cnt:
    S0 = acc / cnt; lin = np.where(mask, sigma2 / np.where(mask, 1 - u, 1.0), 0.0)
    print("equal-level transverse structure factor S_0(k) / [sigma^2/(1-|phi|^2)] by |k| shell:")
    for lo, hi in ((0, 0.3), (0.3, 0.6), (0.6, 1.0), (1.0, 1.5), (1.5, 2.2), (2.2, 3.2), (3.2, 6.0)):
        sel = mask & (kk >= lo) & (kk < hi)
        if sel.sum():
            val = float(np.mean(S0[sel] / lin[sel])); print(f"   |k| in [{lo},{hi}): {val:.4f} (n={int(sel.sum())})")
            if np.isnan(lowk): lowk = val
    C0 = np.fft.ifftn(np.where(mask, S0, 0.0)).real; Cl = np.fft.ifftn(lin).real
    print("site covariance without the zero mode along e_1: r, measured C(r), linear C(r), ratio" + (", r*linear C(r) (the 1/r law of a three-dimensional plane)" if dim == 3 else ""))
    for r in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32):
        if r <= L // 2:
            ix = (r,) + (0,) * (dim - 1); print(f"   {r:3d}  {C0[ix]:+.6f}  {Cl[ix]:+.6f}  {C0[ix]/Cl[ix] if abs(Cl[ix]) > 1e-12 else float('nan'):.3f}" + (f"  {r*Cl[ix]:+.5f}" if dim == 3 else ""))
print(f"SUMMARY: dim={dim} menu={menu} beta={beta} L={L} T={T} plateau_|m|={plateau:.4f} lowk_ratio={lowk:.4f} seconds={time.time()-t0:.0f}")
