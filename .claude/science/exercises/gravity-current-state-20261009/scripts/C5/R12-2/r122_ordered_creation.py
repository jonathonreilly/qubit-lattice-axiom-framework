"""R12-2: deterministic integrate-and-fire creation with low-discrepancy phases vs Poisson.
Each site carries a phase; phase advances at the creation rate (uniform here: Phi = int c dt / ln 2
per axis); when it crosses 1 the site inserts one neighbour along the column and both restart at 0.
Descendants of a site with initial phase phi after Phi: D = 2^floor(Phi + phi) (deterministic, monotone in phi).
Window count = sum over n consecutive initial sites. Compare: random phases, quasi-periodic phases
frac(i*alpha), and the Yule (Poisson) process with the same mean.
Koksma-Hlawka: |sum D(phi_i) - n int D| <= V(D) * n * Dstar_n,  V(D) = D(1)-D(0) = 2^floor(Phi) (2^1 - 1) ~ mean.
"""
import numpy as np
rng = np.random.default_rng(7)
alpha = (np.sqrt(5) - 1) / 2
n, nwin = 20000, 400
for Phi in (1.0, 3.3, 6.6):
    idx = np.arange(n * nwin)
    D = lambda ph: 2.0 ** np.floor(Phi + ph)
    rnd = D(rng.random(n * nwin)).reshape(nwin, n).sum(1)
    qp = D((idx * alpha) % 1.0).reshape(nwin, n).sum(1)
    mean = n * (2 ** Phi) / (2 * np.log(2)) * (2 - 1) if False else None
    # Yule with the same mean growth e^{Phi ln2}: negative binomial
    p = 2.0 ** (-Phi)
    yule = np.array([rng.geometric(p, size=n).sum() for _ in range(nwin)])
    print(f'Phi={Phi}: mean counts  random {rnd.mean():.1f}  quasi-periodic {qp.mean():.1f}  Yule {yule.mean():.1f}')
    print(f'          std across windows: random {rnd.std():.2f}  quasi-periodic {qp.std():.3f}  Yule {yule.std():.2f}'
          f'   (sqrt(mean) = {np.sqrt(qp.mean()):.1f}; KH bound V(D)*O(log n) ~ {2**np.floor(Phi)*np.log(n):.0f})')
