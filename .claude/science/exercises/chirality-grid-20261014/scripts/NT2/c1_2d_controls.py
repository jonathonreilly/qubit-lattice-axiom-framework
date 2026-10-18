"""C1: 2D-proxy controls rebuilt here (real space, not K2c's alias sum): one crossing row of Lx links, periodic,
kernel g_Lx(dW) = (B_{2 delta})^{*Lx}(dW) (Lx-fold box convolution; no wrap since Lx delta < pi for Lx <= 4).
Pool: N = 64 equally spaced Wilson lines (K2c V1). Compare min/max with K2c: Lx=2 +1.382e-3, Lx=3 -8.949e-3, Lx=4 +3.316e-7."""
import numpy as np, itertools
d = 0.6; N = 64
def boxn(x, n, w):
    tot = np.zeros_like(x)
    for eps in itertools.product((1, -1), repeat=n):
        s = x + 0.5 * w * sum(eps)
        tot += np.prod(eps) * np.where(s > 0, s, 0.0) ** (n - 1)
    import math
    return tot / math.factorial(n - 1)
W = 2 * np.pi * np.arange(N) / N
dW = (W[:, None] - W[None, :] + np.pi) % (2 * np.pi) - np.pi
for Lx in (2, 3, 4):
    K = boxn(dW, Lx, 2 * d); ev = np.linalg.eigvalsh(K)
    print(f"Lx={Lx}: lam_min/lam_max {ev[0]/ev[-1]:+.4e}  (#neg {(ev < -1e-12 * ev[-1]).sum()})")
