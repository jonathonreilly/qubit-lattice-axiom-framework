"""Pure-gauge RP of one crossing plane in the 2D U(1) proxy (K2c section 2 setting).
Gauge-invariant kernel on boundary Wilson lines: K(W_a,W_b) = sum_n c_n^Lx e^{in(W_b-W_a)}.
RP <=> c_n^Lx >= 0 for all n (Bochner).  Eigenvalues on N equally spaced Wilson lines:
lambda_j = N * sum_{n = j mod N} c_n^Lx  (exact aliasing identity, as K2c V1).
Weights (both supported in |theta| < delta, i.e. strictly admissible):
  hard:     f = 1(|theta|<delta),                 c_n = sin(n delta)/(n pi)
  triangle: f = (1_{delta/2} * 1_{delta/2})/norm, c_n = 2pi*(sin(n delta/2)/(n pi))^2 / delta  (>= 0)
"""
import numpy as np
delta, N, nmax = 0.6, 64, 200000
n = np.arange(-nmax, nmax + 1)
def c_hard(n):
    out = np.empty(n.shape); nz = n != 0
    out[nz] = np.sin(n[nz]*delta)/(n[nz]*np.pi); out[~nz] = delta/np.pi; return out
def c_tri(n):
    out = np.empty(n.shape); nz = n != 0
    out[nz] = 2*np.pi*(np.sin(n[nz]*delta/2)/(n[nz]*np.pi))**2/delta; out[~nz] = 2*np.pi*(delta/(2*np.pi))**2/delta; return out
# support check of the triangle weight on a grid
th = np.linspace(-np.pi, np.pi, 4001)
tri = np.clip(delta - np.abs(th), 0, None)  # autocorrelation of two boxes of half-width delta/2
print(f"triangle weight support max |theta| with f>0: {np.max(np.abs(th[tri>0])):.4f} (delta = {delta})")
for name, cf in (("hard", c_hard), ("triangle", c_tri)):
    c = cf(n)
    print(f"{name}: min c_n = {c.min():+.3e}  (# negative coefficients in |n|<=50: {int(np.sum(c[np.abs(n)<=50] < 0))})")
    for Lx in (1, 2, 3, 4, 5):
        cl = c**Lx
        lam = np.array([N*cl[(n - j) % N == 0].sum() for j in range(N)])
        print(f"   Lx={Lx}: lambda_min/lambda_max = {lam.min()/lam.max():+.3e}")
