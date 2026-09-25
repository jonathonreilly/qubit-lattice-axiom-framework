"""Seeded Monte Carlo evidence (numerical, not exact) for ATTEMPT.md section 5.

Model (PR8178's nonlinear sphere law, as in the canonical note on main): on the periodic
L x L plane, S_x = s_x + s_{x-e1} + s_{x-e2}, and given level t the spins of level t+1 are
independent with density proportional to exp(beta s.S_x) on the unit sphere.
n(t) = M(t)/|M(t)|, M = plane average.  sigma^2 = A(3 beta)/(3 beta), tau_L = L^2/sigma^2.

Measured, in the stationary regime (burn-in from the aligned plane):
  x1      = 1 - E n(t+1).n(t)                       (one-level direction decorrelation)
  lam(l)  = -log E[n(t+l).n(t)] / l                 (l=1 is -log(1-x1))
  lam1    = log(C(l1)/C(l2))/(l2-l1)                (slope estimator of the memory rate)
  1/E|M|^2
Errors: jackknife over 20 blocks of independent chains.
Run: OMP_NUM_THREADS=1 nice -n 19 python3 mc_evidence.py   (about 20 minutes, one core)
"""
import numpy as np, math, time

def A(k):
    return 1.0 / np.tanh(k) - 1.0 / k

def step(s, beta, rng):
    S = s + np.roll(s, 1, axis=1) + np.roll(s, 1, axis=2)      # axes: chain, x1, x2, component
    r = np.linalg.norm(S, axis=-1); u = S / r[..., None]; kap = beta * r
    U = rng.random(r.shape)
    w = 1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kap)) / kap   # cosine to the mean direction
    w = np.clip(w, -1.0, 1.0); ph = rng.random(r.shape) * 2 * np.pi
    a = np.zeros_like(u); small = np.abs(u[..., 0]) < 0.9
    a[..., 0] = small; a[..., 1] = ~small
    e1 = a - (a * u).sum(-1)[..., None] * u; e1 /= np.linalg.norm(e1, axis=-1)[..., None]
    e2 = np.cross(u, e1); q = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[..., None] * u + q[..., None] * (np.cos(ph)[..., None] * e1 + np.sin(ph)[..., None] * e2)

def run(beta, L, C, T, burn, lags, seed):
    rng = np.random.default_rng(seed); s = np.zeros((C, L, L, 3)); s[..., 2] = 1.0
    for _ in range(burn):
        s = step(s, beta, rng)
    lmax = max(lags); buf = np.zeros((lmax + 1, C, 3)); acc = np.zeros((len(lags), C)); cnt = 0
    m2 = np.zeros(C)
    for t in range(T):
        s = step(s, beta, rng); M = s.mean(axis=(1, 2)); m = np.linalg.norm(M, axis=-1); n = M / m[:, None]
        buf[t % (lmax + 1)] = n; m2 += m * m
        if t >= lmax:
            for i, l in enumerate(lags):
                acc[i] += 1 - (n * buf[(t - l) % (lmax + 1)]).sum(-1)
            cnt += 1
    return acc / cnt, T / m2.mean()

def jack(f, C, nb=20):
    idx = np.arange(C); bl = np.array_split(idx, nb)
    v = f(idx); jk = np.array([f(np.setdiff1d(idx, b)) for b in bl])
    return v, math.sqrt((nb - 1) / nb * ((jk - jk.mean()) ** 2).sum())

SSTAR = {2: 27 / 32, 3: 11 / 9, 4: 189 / 128, 16: 2.6442710025856253}   # exact for 2,3,4 (check.py)

def main():
    t0 = time.time(); out = []
    # (a) one-level decorrelation x1 at several beta: coefficient (x1*tau - 1)/sigma^2
    grid = [(2, 20000, 3000, 360, [20, 40, 80, 160]), (3, 10000, 3000, 560, [20, 40, 80]),
            (4, 10000, 3000, 840, [20, 40, 80]), (16, 2000, 4000, 600, [48, 96])]
    print("(a) one-level decorrelation; coef = (x1*tau_L - 1)/sigma^2 ; pred1 = S*+2-1/L^2 ; 2S* = first-order coef of 1/E|M|^2")
    for L, C, T, burn, betas in grid:
        pts = []
        for b in betas:
            x, im2 = run(b, L, C, T, burn, [1], 1000 * L + b)
            s2 = A(3 * b) / (3 * b); tau = L * L / s2
            c, se = jack(lambda i: (x[0, i].mean() * tau - 1) / s2, C)
            pts.append((s2, c, se))
            print(f"  L={L:2d} beta={b:4d} sigma2={s2:.6f} x1*tau={x[0].mean()*tau:.6f} coef={c:.4f}+-{se:.4f} 1/E|M|^2={im2:.6f} (1/E|M|^2-1)/sigma2={(im2-1)/s2:.4f}")
        X = np.array([p[0] for p in pts]); Y = np.array([p[1] for p in pts]); Wt = 1 / np.array([p[2] for p in pts]) ** 2
        Am = np.vstack([np.ones_like(X), X]).T; cov = np.linalg.inv(Am.T @ (Wt[:, None] * Am)); beta_hat = cov @ (Am.T @ (Wt * Y))
        pred = SSTAR[L] + 2 - 1 / L ** 2
        print(f"  L={L:2d} weighted linear fit in sigma^2: intercept {beta_hat[0]:.4f}+-{math.sqrt(cov[0,0]):.4f} slope {beta_hat[1]:.1f} ; pred1 {pred:.4f} ; 2S* {2*SSTAR[L]:.4f}")
        out.append((L, beta_hat[0], math.sqrt(cov[0, 0]), pred, 2 * SSTAR[L]))
    # (b) memory rate by the slope estimator at beta=20, L=2,3,4, against x1 and 1/E|M|^2
    print("(b) memory rate lam1 (slope of -log C between lags l1<l2) at beta=20")
    for L, C, T in [(2, 20000, 10000), (3, 10000, 20000), (4, 8000, 20000)]:
        b = 20; s2 = A(3 * b) / (3 * b); lam0 = s2 / L ** 2
        l2 = max(4, int(round(0.3 / lam0))); l1 = max(2, l2 // 8); lags = sorted(set([1, 2, l1, l2]))
        x, im2 = run(b, L, C, T, 40 * L * L + 200, lags, 2000 + L)
        i1, i2 = lags.index(l1), lags.index(l2)
        lam, se = jack(lambda i: math.log((1 - x[i1, i].mean()) / (1 - x[i2, i].mean())) / (l2 - l1) / lam0, C)
        x1t = x[0].mean() / lam0
        print(f"  L={L} lags {l1},{l2}: lam1*tau={lam:.5f}+-{se:.5f} x1*tau={x1t:.5f} -log(1-x1)*tau={-math.log(1-x[0].mean())/lam0:.5f} 1/E|M|^2={im2:.5f} "
              f"(lam1*tau-1/E|M|^2)/se={(lam-im2)/se:.1f} ; first-order lam1*tau={1+s2*(SSTAR[L]+2-1/(2*L*L)):.5f}")
    # (c) lag structure at L=16, beta=12 (the historical table's regime)
    b = 12; L = 16; C = 1000; lags = [1, 4, 16, 64]
    x, im2 = run(b, L, C, 4000, 400, lags, 16012)
    s2 = A(3 * b) / (3 * b); tau = L * L / s2
    print(f"(c) L=16 beta=12: 1/E|M|^2={im2:.5f}; first-order lam1*tau={1+s2*(SSTAR[16]+2-1/512):.5f}")
    for i, l in enumerate(lags):
        v, se = jack(lambda j: -math.log(1 - x[i, j].mean()) / l * tau, C)
        print(f"  lag {l:3d}: -log C(l)/l * tau = {v:.5f}+-{se:.5f}")
    print(f"total {time.time()-t0:.0f}s")

if __name__ == "__main__":
    main()
