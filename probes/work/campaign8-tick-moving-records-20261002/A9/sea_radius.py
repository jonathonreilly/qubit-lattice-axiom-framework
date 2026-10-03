"""Approximate quietness in the half-filled staggered sea at the cost of reach (supplied toy).
Formation weight F = occupation of one normalised local mode w_R: the upper-band part of the
centre site, P_+ e_0, cut to a ball of radius R. Vacuum rate eps(R) = <w_R| P_- |w_R>.
3D massless staggered fermions, antiperiodic L^3 torus, P_+ = (1 + H|H|^-1)/2 applied by FFT."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
L = 64
x = np.arange(L)
X1, X2, X3 = np.meshgrid(x, x, x, indexing="ij")
eta = [np.ones((L, L, L)), (-1.0) ** X1, (-1.0) ** (X1 + X2)]
k = np.pi * (2 * x + 1) / L                       # antiperiodic momenta
s2 = np.sin(k) ** 2
Einv = 1.0 / np.sqrt(s2[:, None, None] + s2[None, :, None] + s2[None, None, :])
tw = np.exp(-1j * np.pi * x / L)
TW = tw[:, None, None] * tw[None, :, None] * tw[None, None, :]

def absH_inv(v):           # convolution with |H|^-1 under antiperiodic boundaries
    u = np.fft.ifftn(Einv * np.fft.fftn(v * TW))
    return u / TW

def shift(v, mu, d):       # (shift v)(x) = v(x + d e_mu) with antiperiodic sign on wrap
    out = np.roll(v, -d, axis=mu)
    idx = [slice(None)] * 3
    idx[mu] = slice(L - 1, L) if d == 1 else slice(0, 1)
    out[tuple(idx)] *= -1
    return out

def H(v):
    out = np.zeros_like(v)
    for mu in range(3):
        out += 0.5j * eta[mu] * (shift(v, mu, -1) - shift(v, mu, 1))
    return out

def Pplus(v):
    return 0.5 * (v + H(absH_inv(v)))

rng = np.random.default_rng(3)
r = rng.normal(size=(L, L, L)) + 1j * rng.normal(size=(L, L, L))
pr = Pplus(r)
print(f"sanity: ||P+P+ r - P+ r|| / ||P+ r|| = {np.linalg.norm(Pplus(pr) - pr) / np.linalg.norm(pr):.1e}; "
      f"tr-weight of P+ at a site = {Pplus(np.eye(1, L**3, (L//2)*(L*L+L+1)).reshape(L, L, L))[L//2, L//2, L//2].real:.4f}")
c = L // 2
e0 = np.zeros((L, L, L), complex); e0[c, c, c] = 1
w = Pplus(e0)
dist = np.sqrt((X1 - c) ** 2 + (X2 - c) ** 2 + (X3 - c) ** 2)
prev = None
for R in (0, 1, 2, 3, 4, 6, 8, 12, 16):
    wR = np.where(dist <= R + 1e-9, w, 0)
    wR /= np.linalg.norm(wR)
    eps = 1 - np.vdot(wR, Pplus(wR)).real
    slope = "" if prev is None or prev[0] == 0 else f"  local slope d ln eps / d ln R = {np.log(eps/prev[1])/np.log(R/prev[0]):+.2f}"
    print(f"R={R:2d}: sites in ball {int((dist <= R + 1e-9).sum()):6d}; vacuum rate eps(R) = {eps:.3e}{slope}")
    prev = (R, eps)
