"""T09 Test 3b: 1D Kac telegraph (nonnegative persistent walk) vs Dirac quantum walk (Feynman checkerboard).
Two-stream walker, right/left movers, per-tick amplitude: straight a, reversal b.
  T(k) = diag(e^{ik}, e^{-ik}) [[a, b],[b, a]]     lambda^2 - 2 a cos k lambda + (a^2 - b^2) = 0
Nonnegative stochastic: a = 1-p, b = p.   Unitary Dirac walk: a = cos th, b = i sin th  (b imaginary).
Checks: (i) strict front (support within |x| <= t) for both; (ii) stochastic branch damped for every k != 0
with rate ~ D k^2 (telegraph -> diffusion), never undamped on an open set unless p in {0,1};
(iii) the continuation b -> i*b maps the damped branch to the unimodular one: what moved is the phase of b."""
import numpy as np

def eig(a, b, k):
    return np.roots([1, -2 * a * np.cos(k), a * a - b * b])

print('(ii) stochastic telegraph: max |lambda| over k in [0.05, pi-0.05] for several reversal probabilities p')
for p in (0.01, 0.1, 0.3, 0.5, 0.9):
    ks = np.linspace(0.05, np.pi - 0.05, 400)
    mx = max(max(abs(eig(1 - p, p, k))) for k in ks)
    # small-k: |lambda| ~ 1 - D k^2 ; D = (1-p)/(2p) for the persistent walk (velocity 1)
    k = 0.05
    lam = max(abs(eig(1 - p, p, k)))
    print(f'  p={p:4.2f}: max|lam| = {mx:.6f}; at k=0.05 |lam|={lam:.6f}, (1-|lam|)/k^2 = {(1 - lam) / k ** 2:.4f}  [D=(1-p)/(2p)={(1 - p) / (2 * p):.4f}]')

print('\n(iii) same algebra, b -> i sin(th) with a = cos(th): unitary Dirac walk')
for th in (0.1, 0.5, 1.0):
    a, b = np.cos(th), 1j * np.sin(th)
    ks = np.linspace(-np.pi, np.pi, 401)
    mods = [abs(eig(a, b, k)) for k in ks]
    om = [np.arccos(np.clip(np.cos(th) * np.cos(k), -1, 1)) for k in ks]
    err = max(abs(np.sort(np.angle(eig(a, b, k)))[1] - w) for k, w in zip(ks, om))
    print(f'  theta={th}: max| |lam|-1 | = {max(abs(np.array(mods) - 1).ravel()):.2e}; dispersion cos(w)=cos(th)cos(k) err {err:.2e}; gap w(0)={om[200]:.4f}')

print('\n(iii-b) stochastic branch at small k: lambda = e^{-lam*} ...   telegraph relation lambda^2-2(1-p)cos k lambda+(1-2p)=0')
print('   what "continuation p -> i eps" does: a^2-b^2 = 1 only if b^2 = a^2-1 <0 (b imaginary) for |a|<1:')
for a in (0.3, 0.8, 0.99):
    print(f'   a={a}: b^2 = {a * a - 1:.4f} -> b = {np.sqrt(complex(a * a - 1)):.4f}; real b would give det {a * a:.2f}-b^2 != 1 unless b=0')

print('\n(i) strict front: exact n-step kernel support (stochastic p=0.3 and unitary th=0.5), n=20')
def kernel(a, b, n):
    N = 2 * n + 3
    psi = np.zeros((2, N), complex); c = n + 1
    psi[0, c] = 1  # start moving right (weight 1)
    for _ in range(n):
        new = np.zeros_like(psi)
        # coin then shift
        r = a * psi[0] + b * psi[1]; l = b * psi[0] + a * psi[1]
        new[0, 1:] = r[:-1]; new[1, :-1] = l[1:]
        psi = new
    return np.abs(psi).sum(axis=0), c
for (a, b, lab) in ((0.7, 0.3, 'stochastic p=0.3'), (np.cos(0.5), 1j * np.sin(0.5), 'unitary th=0.5')):
    w, c = kernel(a, b, 20)
    idx = np.nonzero(w > 1e-15)[0]
    print(f'  {lab}: support x in [{idx.min() - c}, {idx.max() - c}] after 20 ticks; front speed = {(idx.max() - c) / 20:.2f}; mass sum = {w.sum():.4f}')
