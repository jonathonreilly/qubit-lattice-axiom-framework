"""Sign of mu_E for separable symbols u = sum g(k_i) with p = grad u (P = energy current).
Random cosine series g(k) = sum_n c_n (1 - cos nk), normalized to g ~ k^2/2, range r <= 4.
Record min/max of mu_E over samples, split by monotone (g' > 0 on (0,pi)) vs non-monotone bands."""
import numpy as np, warnings
warnings.filterwarnings('ignore')
rng = np.random.default_rng(1)
N = 64
k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
def mu_sep(m, c):
    n = np.arange(1, len(c)+1)
    K = np.outer(k, n)
    g0 = np.sum(c*(1-np.cos(K)), 1); g1 = np.sum(c*n*np.sin(K), 1); g2 = np.sum(c*n*n*np.cos(K), 1)
    GX, GY = np.meshgrid(g0, g0, indexing='ij'); D1X, D1Y = np.meshgrid(g1, g1, indexing='ij'); D2X, D2Y = np.meshgrid(g2, g2, indexing='ij')
    phi = D1X**2 - D1Y**2; psi = D2X - D2Y
    acc = 0.0
    for gz in g0:
        om2 = m*m + 2*(GX + GY + gz)
        if (om2 <= 0).any(): return np.nan
        acc += np.sum(phi*psi/np.sqrt(om2))
    return -acc/N**3/8
kk = np.linspace(1e-3, np.pi-1e-3, 400)
res = {True: [], False: []}
for trial in range(400):
    r = rng.integers(2, 5)
    c = rng.normal(size=r)*np.array([1, 0.5, 0.3, 0.2][:r])
    c = c/np.sum(c*np.arange(1, r+1)**2)          # g''(0) = sum c n^2 = 1
    n = np.arange(1, r+1)
    gp = np.sum(c*n*np.sin(np.outer(kk, n)), 1)
    g0 = np.sum(c*(1-np.cos(np.outer(np.linspace(-np.pi, np.pi, 801), n))), 1)
    if g0.min() < -1e-12: continue
    mono = bool((gp > 0).all())
    vals = [mu_sep(m, c) for m in (0.2, 1.0, 3.0)]
    if np.isnan(vals).any(): continue
    res[mono].append(vals)
for mono in (True, False):
    A = np.array(res[mono])
    if len(A) == 0: continue
    lines = [f'{"monotone" if mono else "non-monotone"} bands: {len(A)} samples']
    for j, m in enumerate((0.2, 1.0, 3.0)):
        lines.append(f'   m={m}: min muE = {A[:,j].min():+.4e}  max muE = {A[:,j].max():+.4e}  frac negative = {(A[:,j]<0).mean():.3f}')
    print('\n'.join(lines))
