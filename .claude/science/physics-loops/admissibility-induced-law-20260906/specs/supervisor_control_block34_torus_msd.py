"""the angular diffusion of the plane-average direction on the torus: MSD(l) = E|m^_{t+l} - m^_t|^2 averaged along trajectories after
a transient, for the nonlinear sphere law (D_1 = MSD/(2 l) per transverse component) against the linearized zero mode's exact
2 sigma^2 l / L^2; the linear Gaussian model with the same estimator as a calibration."""
import numpy as np, sys, time
def A(k): return 1.0 / np.tanh(k) - 1.0 / k
def run_sphere(beta, L, T, seed, every):
    rng = np.random.default_rng(seed); s = np.zeros((L, L, 3)); s[..., 2] = 1.0; out = []
    for t in range(1, T + 1):
        S = s + np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1)
        norm = np.linalg.norm(S, axis=2); u = S / norm[..., None]; kappa = beta * norm
        U = rng.random((L, L)); w = 1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa
        w = np.clip(w, -1.0, 1.0); phi = rng.random((L, L)) * 2 * np.pi
        a = np.where((np.abs(u[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
        e1 = a - (a * u).sum(-1)[..., None] * u; e1 /= np.linalg.norm(e1, axis=2)[..., None]; e2 = np.cross(u, e1)
        r = np.sqrt(np.clip(1 - w * w, 0, 1))
        s = w[..., None] * u + r[..., None] * (np.cos(phi)[..., None] * e1 + np.sin(phi)[..., None] * e2)
        if t % every == 0: out.append(s.mean(axis=(0, 1)))
    return np.array(out)
def run_linear(beta, L, T, seed, every):
    rng = np.random.default_rng(seed); sig = np.sqrt(A(3 * beta) / (3 * beta)); th = np.zeros((L, L, 2)); out = []
    for t in range(1, T + 1):
        th = (th + np.roll(th, 1, axis=0) + np.roll(th, 1, axis=1)) / 3.0 + sig * rng.standard_normal((L, L, 2))
        if t % every == 0: out.append(th.mean(axis=(0, 1)))
    return np.array(out)
beta = float(sys.argv[1]); L = int(sys.argv[2]); T = int(sys.argv[3]); nseeds = int(sys.argv[4]); every = 25
t0 = time.time(); D_nl = {}; D_lin = {}; lags = [1, 2, 4, 8, 16, 40]     # in units of 'every' levels
skip = max(5, (T // every) // 5)      # discard the first fifth as the transient
msd_nl = {l: [] for l in lags}; msd_lin = {l: [] for l in lags}; mabs = []
for sd in range(nseeds):
    m = run_sphere(beta, L, T, 500 + sd, every); mh = m / np.linalg.norm(m, axis=1)[:, None]; mabs.append(np.linalg.norm(m[skip:], axis=1).mean())
    th = run_linear(beta, L, T, 700 + sd, every)
    for l in lags:
        d = mh[skip + l:] - mh[skip:-l]; msd_nl[l].append((d ** 2).sum(1).mean())
        d2 = th[skip + l:] - th[skip:-l]; msd_lin[l].append((d2 ** 2).sum(1).mean())
rate = A(3 * beta) / (3 * beta) / L ** 2
print(f"beta={beta} L={L} T={T} seeds={nseeds} ({time.time()-t0:.0f}s): sigma^2/L^2 = {rate:.4e}; memory time {1/rate:.0f}; mean |m| in the stationary regime {np.mean(mabs):.4f}")
for l in lags:
    lag = l * every; a = np.mean(msd_nl[l]); b = np.mean(msd_lin[l]); ea = np.std(msd_nl[l]) / np.sqrt(nseeds); eb = np.std(msd_lin[l]) / np.sqrt(nseeds)
    print(f"  lag {lag:5d}: nonlinear MSD {a:.4e} -> D_1 = {a/(2*lag):.4e} (ratio to sigma^2/L^2: {a/(2*lag)/rate:.3f} +- {ea/(2*lag)/rate:.3f}); linear model MSD {b:.4e} (ratio {b/(2*lag)/rate:.3f} +- {eb/(2*lag)/rate:.3f})")
