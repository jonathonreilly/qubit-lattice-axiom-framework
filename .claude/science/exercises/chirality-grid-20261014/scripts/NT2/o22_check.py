"""O22 checks: (1) PPoly tabulation of T*Psi vs exact piecewise integration; (2) Nystrom convergence in n;
(3) unsmoothed limit sanity: rho small vs a direct high-n Nystrom of the point kernel at a few Delta;
(4) reduction check by Monte Carlo: x uniform in [-d,d]^12, density of the 4 plaquette sums (curl) near targets, ratios
compared with h (point kernel via high-n Nystrom)."""
import numpy as np, time, resource
from o22lib import *
d = 0.6; rho = 0.1
f, fex = make_TPsi(d, rho)
xs = np.linspace(-2.7, 2.7, 997); print("PPoly vs exact max diff:", np.abs(f(xs) - fex(xs)).max(), " max value", fex(xs).max())
rng = np.random.default_rng(3)
D = rng.uniform(-0.9, 0.9, (3, 4))
for n in (32, 64, 96):
    y, w = np.polynomial.legendre.leggauss(n); y = d * y; w = d * w
    print(f"n={n}:", [f"{h_smooth(Dk, f, y, w):.14e}" for Dk in D])
# point kernel by direct Nystrom (kinks: slow convergence) for the MC comparison
Tpt = lambda x: np.maximum(2 * d - np.abs(x), 0.0)
def h_point(Dl, n):
    y, w = np.polynomial.legendre.leggauss(n); y = d * y; w = d * w; sw = np.sqrt(w)
    Ms = [sw[:, None] * Tpt(Dl[p] + y[:, None] - y[None, :]) * sw[None, :] for p in range(4)]
    return np.trace(Ms[0] @ Ms[1] @ Ms[2] @ Ms[3])
targets = np.array([[0, 0, 0, 0], [0.5, -0.5, 0.5, -0.5], [0.8, 0.0, -0.4, 0.3], [1.0, 1.0, 0.0, -0.5]])
print("RSS before point h", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20, flush=True)
hp = np.array([h_point(t, 400) for t in targets]); print("point h (n=400):", hp, " n=200:", np.array([h_point(t, 200) for t in targets]))
print("RSS after point h", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20, flush=True)
# MC: plaquette p = S_p + e_{p-1} - e_p, S_p = sum of two outer links (signs irrelevant: symmetric)
eta = 0.06; cnt = np.zeros(len(targets)); N = 0
for chunk in range(160):
    x = rng.uniform(-d, d, (250_000, 12))
    S = x[:, 0:4] + x[:, 4:8]; e = x[:, 8:12]
    Phi = S + np.roll(e, 1, axis=1) - e
    for t in range(len(targets)):
        cnt[t] += np.all(np.abs(Phi - targets[t]) < eta, axis=1).sum()
    N += 250_000
    if chunk == 0: print('RSS after first MC chunk', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20, flush=True)
r_mc = cnt / cnt[0]; r_h = hp / hp[0]
print("MC counts:", cnt, "\nratios MC :", np.round(r_mc, 4), "\nratios h  :", np.round(r_h, 4), "\n(MC window eta=0.06 biases ratios at O(eta^2); stat error ~", np.round(np.sqrt(cnt) / cnt[0], 4), ")")
print("RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20)
