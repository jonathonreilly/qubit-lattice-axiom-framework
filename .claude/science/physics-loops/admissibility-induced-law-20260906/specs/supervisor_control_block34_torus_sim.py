"""the sphere formation law on periodic L x L level planes from the aligned plane: the ensemble mean of the projection m_z(t) over
several seeds, and the linearized Gaussian model on the same torus (theta_{t+1} = P theta_t + xi, per-component variance
sigma^2 = A(3 beta)/(3 beta)) with the proxy exp(-v_t) and the direction's projection; fitted late-time exponential rates
against the zero-mode rate sigma^2/L^2."""
import numpy as np, sys, time
def A(k): return 1.0 / np.tanh(k) - 1.0 / k
def run_sphere(beta, L, T, seed, every):
    rng = np.random.default_rng(seed)
    s = np.zeros((L, L, 3)); s[..., 2] = 1.0
    out = []
    for t in range(1, T + 1):
        S = s + np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1)
        norm = np.linalg.norm(S, axis=2); u = S / norm[..., None]; kappa = beta * norm
        U = rng.random((L, L)); w = 1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa
        w = np.clip(w, -1.0, 1.0); phi = rng.random((L, L)) * 2 * np.pi
        a = np.where((np.abs(u[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
        e1 = a - (a * u).sum(-1)[..., None] * u; e1 /= np.linalg.norm(e1, axis=2)[..., None]; e2 = np.cross(u, e1)
        r = np.sqrt(np.clip(1 - w * w, 0, 1))
        s = w[..., None] * u + r[..., None] * (np.cos(phi)[..., None] * e1 + np.sin(phi)[..., None] * e2)
        if t % every == 0:
            m = s.mean(axis=(0, 1)); out.append((t, m[2], np.linalg.norm(m)))
    return out
def run_linear(beta, L, T, seed, every):
    """Gaussian transverse field on the torus; the direction's projection is cos of the angle |theta_bar| of the plane average
    (small-angle proxy exp(-|theta_bar|^2/2 ... ) we record the plane-average variance and the proxy exp(-v_t) with v_t the site
    variance estimated across the plane."""
    rng = np.random.default_rng(seed); sig = np.sqrt(A(3 * beta) / (3 * beta))
    th = np.zeros((L, L, 2)); out = []
    for t in range(1, T + 1):
        th = (th + np.roll(th, 1, axis=0) + np.roll(th, 1, axis=1)) / 3.0 + sig * rng.standard_normal((L, L, 2))
        if t % every == 0:
            bar = th.mean(axis=(0, 1)); out.append((t, float((bar ** 2).sum()), float((th ** 2).sum(-1).mean())))
    return out
beta = float(sys.argv[1]); L = int(sys.argv[2]); T = int(sys.argv[3]); nseeds = int(sys.argv[4]); every = max(1, T // 400)
t0 = time.time()
acc = None
for sd in range(nseeds):
    res = run_sphere(beta, L, T, 100 + sd, every)
    arr = np.array([[r[1], r[2]] for r in res]); acc = arr if acc is None else acc + arr
acc /= nseeds; ts = np.array([r[0] for r in res])
lin = None
for sd in range(nseeds):
    res2 = run_linear(beta, L, T, 300 + sd, every)
    arr2 = np.array([[r[1], r[2]] for r in res2]); lin = arr2 if lin is None else lin + arr2
lin /= nseeds
rate_lin = A(3 * beta) / (3 * beta) / L ** 2
# early-window exponential fit of the ensemble-mean projection: from the first record until E[m_z] falls to 0.2 of its first value
mz = acc[:, 0]; first = mz[0]
idx = np.where(mz < 0.2 * first)[0]; end = idx[0] if len(idx) else len(mz)
win = slice(0, max(end, 6))
sl, ic = np.polyfit(ts[win], np.log(np.clip(mz[win], 1e-6, None)), 1); rate_nl = -sl
# the linear model's own projection proxy exp(-|theta_bar|^2/2 per component ...): fit exp(-Var) with Var = mean |theta_bar|^2/2
lv = lin[:, 0] / 2.0; sl2, _ = np.polyfit(ts[win], -lv[win], 1); rate_lin_meas = -sl2
print(f"beta={beta} L={L} T={T} seeds={nseeds} ({time.time()-t0:.0f}s): zero-mode rate sigma^2/L^2 = {rate_lin:.3e}; memory time L^2/sigma^2 = {1/rate_lin:.0f}; nonlinear fitted rate of E[m_z] over the early window (to 0.2 of the start, {int(end)} records) = {rate_nl:.3e} (ratio to sigma^2/L^2: {rate_nl/rate_lin:.2f}); linear model measured zero-mode rate {rate_lin_meas:.3e} (ratio {rate_lin_meas/rate_lin:.2f})")
for i in range(0, len(ts), max(1, len(ts) // 12)):
    print(f"  t={ts[i]:7d}  E[m_z]={acc[i,0]:.4f}  E|m|={acc[i,1]:.4f}  lin: |theta_bar|^2={lin[i,0]:.4f}  site var={lin[i,1]:.4f}")
