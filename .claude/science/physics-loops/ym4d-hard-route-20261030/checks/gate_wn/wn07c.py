"""Criterion (written first): law U = exp(i A), A = a - (1/3) K_rho grad S3tilde(a), a Gaussian (Feynman), K_rho = G cut off at range rho.
Tree value: K_N = K_comp + 4 [ sumV(K J_1, E_2, E_3) + sumV(E_1, K J_2, E_3) + sumV(E_1, E_2, K J_3) ].
Rectangle sum Stk_N(rho) at D = 3, R = 8, T = 32.
Self-check: at rho = infinity Stk_N must equal Stk_W, to 1e-10 relative.
PREDICTION (reviewer): for rho << D, Stk_N is near -24 Flux (a strictly local quadratic map does not change the reading), and for rho >> R it is near Stk_W.
FAIL of the prediction if rho = 1 moves Stk_N by more than half the way from -24 Flux to Stk_W."""
import numpy as np
from wnlib import *
from wn02_rect import square, sigma, tau_path

import sys
T = int(sys.argv[1])
d = 4
D = int(sys.argv[2])
R = int(sys.argv[3])
c3 = T // 2
ys = square(c3, c3, D)
far = (R, 0, c3 + (D - 1) // 2, c3 + (D - 1) // 2)
near = [plaq(y, 0, 1) for y in ys]
l3 = plaq(far, 2, 3)
Jn = [current(p, T, d) for p in near]
J3 = current(l3, T, d)
En = [green(J, T, d) for J in Jn]
e = green(J3, T, d)
Pk = [np.sum(Jn[k] * En[(k + 1) % 4]) for k in range(4)]

# position-space G on the torus
kh = khat2(T, d)
kh[(0,) * d] = np.inf
G0 = np.fft.ifftn(1 / kh).real
coords = np.meshgrid(*[np.minimum(np.arange(T), T - np.arange(T)) for _ in range(d)], indexing="ij")
dist = np.sqrt(sum(c ** 2 for c in coords))


def kernel(rho):
    if np.isinf(rho):
        return 1 / kh
    chi = (dist <= rho).astype(float)
    return np.fft.fftn(G0 * chi).real


def apply(Khat, J):
    out = np.empty_like(J)
    for mu in range(d):
        out[mu] = np.fft.ifftn(np.fft.fftn(J[mu]) * Khat).real
    return out


kc = {}
flux = 0
for k in range(4):
    kp = (k + 1) % 4
    sig = sigma(k, ys, D)
    tau = tau_path(ys[k], far)
    paths = [near[k], lasso(sig, near[kp]), lasso(tau, l3)]
    kc[k] = K_comp(paths, [En[k], En[kp], e], T)
    flux += incr(e, sig, T).sum()
stk_comp = sum(kc[k] / Pk[k] for k in range(4))
print(f"-24 Flux {-24*flux:.5e}; Stk_comp {stk_comp:.5e}", flush=True)
stkW = sum((kc[k] + 12 * sumV(En[k], En[(k + 1) % 4], e, T, d)) / Pk[k] for k in range(4))
print(f"Stk_W {stkW:.5e}", flush=True)
for rho in (0, 1, 2, 3):
    Kh = kernel(rho)
    Et = [apply(Kh, J) for J in Jn]
    et = apply(Kh, J3)
    s = 0
    for k in range(4):
        kp = (k + 1) % 4
        add_ = 4 * (sumV(Et[k], En[kp], e, T, d) + sumV(En[k], Et[kp], e, T, d) + sumV(En[k], En[kp], et, T, d))
        s += (kc[k] + add_) / Pk[k]
    frac = (s - stk_comp) / (stkW - stk_comp)
    print(f"rho={rho}: Stk_N {s:.5e}; fraction of the way from -24 Flux to Stk_W {frac:.4f}", flush=True)
