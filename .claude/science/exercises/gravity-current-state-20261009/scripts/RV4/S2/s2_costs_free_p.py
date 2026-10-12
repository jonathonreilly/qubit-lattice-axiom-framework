"""Costs of the free-p common zeros (fixed NN KG dispersion): (i) E∇E violation p - grad(Omega/2) = p - sin k (total momentum must equal
the total energy current, so the one-particle symbols must agree pointwise; improvements cannot change totals);
IR cubic coefficients p_x = kx + A kx^3 + B kx(ky^2[+kz^2]) + ...: the M^6 ln M (3D) / M^4 ln M-type IR log of mu_E ∝ (3A - B), of mu_T2 ∝ B.
(sin k: A = -1/6, B = 0)."""
import numpy as np
from s2_core import terms, grid, p_and_dp
for d in (2, 3):
    tl = terms(d, 4); L = 32; K = grid(d, L)
    for tag in ['M1.0', 'M0.3', 'both']:
        a = np.load(f's2_zero_d{d}_{tag}.npy')
        A = -sum(c*t[0]**3 for c, t in zip(a, tl))/6
        if d == 2: B = -sum(c*t[0]*t[1]**2 for c, t in zip(a, tl))/2
        else:      B = -sum(c*t[0]*(t[1]**2 + t[2]**2) for c, t in zip(a, tl))/4
        P = [0]*d
        for c, t in zip(a, tl):
            Pt, _ = p_and_dp(t, K); P = [x + c*y for x, y in zip(P, Pt)]
        dev = np.sqrt(np.mean((P[0] - np.sin(K[0]))**2)/np.mean(np.sin(K[0])**2))
        sep = sum(abs(c) for c, t in zip(a, tl) if any(t[1:]))
        print(f"d={d} zero[{tag:4s}]: A={A:+.5f} B={B:+.5f}  (3A-B)={3*A-B:+.5f}  | rms(p_x - sin kx)/rms(sin kx) = {dev:.4f}  | sum|non-separable coeffs| = {sep:.4f}")
