"""A17 check C1 (exact arithmetic on Z^3, supplied carrier model).

Carriers: independent walkers (or SSEP) with generator kappa*Delta_lat at density u.
Pace at x: N(x,t) = sum_y w(y-x) eta_y(t), normalised so E N = 1  (sum w = 1/u).
Zero-frequency noise:  S_N(0) = 2u(1-u) <w, G_kappa w> = [2(1-u)/(u kappa)] * e,
   e = <nu, G nu>,  nu = u*w (sum nu = 1),  G = (-Delta_lat)^{-1}  (G(0) = Watson/6).
Floor (Cauchy-Schwarz in the G_KK inner product):  e >= 1/Cap(K),  Cap(K) = 1^T G_KK^{-1} 1.
Checks:
  (a) G validation (Watson/6, discrete Laplacian residual);
  (b) uniform-ball e_unif and floor e_opt = 1/Cap for R = 0..6; trend 4 pi R e -> 1.2 and 1 (continuum);
  (c) two balls at separation D: e_self - e_cross(D); exact identity e_self - e_cross(1) = 1/(6|K|);
      far field e_cross(D) -> G(D).
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import time
import itertools
import numpy as np
from scipy.special import ive

t0 = time.time()
TMAX = 2.0e5
s = np.linspace(np.log(1e-9), np.log(TMAX), 9001)
tg = np.exp(s)
ds = s[1] - s[0]
wq = np.full(s.size, ds); wq[0] *= 0.5; wq[-1] *= 0.5
wq = wq * tg                       # dt = t ds
AMAX = 21
IV = np.array([ive(a, 2 * tg) for a in range(AMAX + 1)])   # (AMAX+1, nt)
PREF = (4 * np.pi) ** -1.5


def G_triples(trip):
    """trip: (n,3) nonneg ints -> G values (vectorised trapezoid in log t + asymptotic tail)."""
    out = np.empty(len(trip))
    for i0 in range(0, len(trip), 400):
        tr = trip[i0:i0 + 400]
        prod = IV[tr[:, 0]] * IV[tr[:, 1]] * IV[tr[:, 2]]
        val = prod @ wq
        sfac = (4 * tr[:, 0] ** 2 - 1) + (4 * tr[:, 1] ** 2 - 1) + (4 * tr[:, 2] ** 2 - 1)
        tail = PREF * (2 * TMAX ** -0.5 - (sfac / 16.0) * (2.0 / 3.0) * TMAX ** -1.5)
        out[i0:i0 + 400] = val + tail
    return out


# table of G over all sorted triples 0 <= a <= b <= c <= AMAX
trips = np.array([t for t in itertools.combinations_with_replacement(range(AMAX + 1), 3)])
Gt = G_triples(trips)
GT = np.zeros((AMAX + 1,) * 3)
for (a, b, c), v in zip(trips, Gt):
    for p in set(itertools.permutations((a, b, c))):
        GT[p] = v


def Gof(d):
    d = np.abs(d)
    return GT[d[..., 0], d[..., 1], d[..., 2]]


W = 1.516386059151978
print("== (a) Green function validation ==")
print(f"G(0) = {GT[0,0,0]:.12f}  Watson/6 = {W/6:.12f}  diff = {GT[0,0,0]-W/6:.1e}")
res = []
for x in [(0, 0, 0), (1, 0, 0), (2, 1, 0), (3, 2, 1), (6, 4, 2), (9, 0, 0)]:
    x = np.array(x)
    lap = -6 * Gof(x)
    for dd in range(3):
        for sg in (1, -1):
            y = x.copy(); y[dd] += sg
            lap += Gof(y)
    res.append(lap + (1.0 if not x.any() else 0.0))
print("  -Delta G - delta residuals:", " ".join(f"{r:.1e}" for r in res))
print(f"  4 pi r G at (20,0,0): {4*np.pi*20*GT[20,0,0]:.5f}  (-> 1)")


def ball(R):
    rng = range(-R, R + 1)
    return np.array([(i, j, k) for i in rng for j in rng for k in rng if i * i + j * j + k * k <= R * R])


print("\n== (b) uniform-ball pace noise vs capacity floor (e = S_N(0) * u kappa / (2(1-u))) ==")
print(" R  |K|   R_eff   e_unif      e_floor=1/Cap  ratio  4piR_eff*e_unif  4piR_eff*e_floor  e_unif/G(0)")
for R in range(0, 7):
    K = ball(R)
    D = K[:, None, :] - K[None, :, :]
    GKK = Gof(D)
    n = len(K)
    e_unif = GKK.sum() / n ** 2
    cap = np.linalg.solve(GKK, np.ones(n)).sum()
    e_opt = 1.0 / cap
    Reff = (3 * n / (4 * np.pi)) ** (1 / 3)
    print(f" {R}  {n:4d}  {Reff:5.2f}  {e_unif:.6f}   {e_opt:.6f}     {e_unif/e_opt:.4f}   {4*np.pi*Reff*e_unif:.4f}"
          f"          {4*np.pi*Reff*e_opt:.4f}          {e_unif/GT[0,0,0]:.4f}")

print("\n== (c) two uniform balls (R=3) at separation D along x: shared-environment correlation ==")
K = ball(3); n = len(K)
D0 = K[:, None, :] - K[None, :, :]
e_self = Gof(D0).sum() / n ** 2
print(f" |K| = {n}, e_self = {e_self:.6f}")
print("  D   e_cross     (e_self-e_cross)/e_self   G(D)       note")
for Dx in [1, 2, 3, 4, 6, 8, 12, 15]:
    sh = np.array([Dx, 0, 0])
    e_cross = Gof(D0 - sh).sum() / n ** 2
    note = ""
    if Dx == 1:
        note = f"identity: e_self-e_cross(1) = {e_self-e_cross:.3e} vs 1/(6|K|) = {1/(6*n):.3e}"
    print(f" {Dx:3d}  {e_cross:.6f}   {(e_self-e_cross)/e_self:.4f}                  {GT[Dx,0,0]:.6f}  {note}")
print(f"\nelapsed {time.time()-t0:.1f} s")
