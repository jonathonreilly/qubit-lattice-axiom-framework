"""A17 check C2 (supplied toy, Monte Carlo vs exact formula).

Independent lazy walkers (stay 1/2, else one of 6 neighbours; kappa = 1/12) on an L^3 torus,
uniform (stationary) start, density u = Nw/V.  One shared walker history per replica.
Pace kernels (normalised so E N = 1):
  ball(R) at c0, R = 0..3;  branch differences ball(2)@c0 - ball(2)@(c0 + D e_x), D = 1, 3, 6, 10;
  a causal moving-average window W = 100 applied to ball(2)  (time smoothing).
Exact: Var(sum_{t<T} N) = (u/V) sum_{k != 0} |w_hat(k)|^2 f_T(lambda_k),
       lambda_k = 1/2 + (1/6) sum_a cos k_a,  f_T(l) = T(1+l)/(1-l) - 2l(1-l^T)/(1-l)^2.
Compares MC variance across replicas (s.e. ~ sqrt(2/M)) with the exact value.
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import sys
import time
import numpy as np

t0 = time.time()
L, u_target, M, T, Wwin = 20, 0.05, 500, 1200, 100
V = L ** 3
Nw = int(round(u_target * V)); u = Nw / V
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 20261003)
c0 = np.array([10, 10, 10])
X, Y, Z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")


def dist2(c):
    d = [np.minimum((A - ci) % L, (ci - A) % L) for A, ci in zip((X, Y, Z), c)]
    return d[0] ** 2 + d[1] ** 2 + d[2] ** 2


def ballw(R, c):
    m = (dist2(c) <= R * R).astype(float)
    return m / (u * m.sum())


kern, names = [], []
for R in range(4):
    kern.append(ballw(R, c0)); names.append(f"ball R={R}")
for D in (1, 3, 6, 10):
    kern.append(ballw(2, c0) - ballw(2, c0 + np.array([D, 0, 0]))); names.append(f"diff R=2, D={D}")
Wm = np.array([k.ravel() for k in kern])            # (nk, V)
nk = len(kern)

# exact variances on the torus
kx = 2 * np.pi * np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(kx, kx, kx, indexing="ij")
lam = 0.5 + (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 6.0
lam_nz = lam.ravel()[1:]


def fT(l, T):
    return T * (1 + l) / (1 - l) - 2 * l * (1 - l ** T) / (1 - l) ** 2


exact, slope = [], []
for k in kern:
    wh2 = np.abs(np.fft.fftn(k)).ravel()[1:] ** 2
    exact.append(u / V * np.sum(wh2 * fT(lam_nz, T)))
    slope.append(u / V * np.sum(wh2 * (1 + lam_nz) / (1 - lam_nz)))
# windowed sum weights: sum over t = W-1..T-1 of (1/W) sum_{s=t-W+1}^{t} N(s)  ->  sum_s c_s N(s)
cs = np.array([sum(1 for t in range(max(Wwin - 1, s), min(s + Wwin, T))) for s in range(T)], float) / Wwin
wh2b = np.abs(np.fft.fftn(kern[2])).ravel()[1:] ** 2
# exact windowed variance: sum_{s,s'} c_s c_s' (u/V) sum_k |w|^2 lam^{|s-s'|}  (direct over lags)
lagsum = np.zeros(T)
for tau in range(T):
    lagsum[tau] = np.dot(cs[:T - tau], cs[tau:])
lam_pow = np.ones_like(lam_nz); exact_win = 0.0
for tau in range(T):
    term = u / V * np.sum(wh2b * lam_pow)
    exact_win += lagsum[tau] * term * (1 if tau == 0 else 2)
    lam_pow = lam_pow * lam_nz

pos = rng.integers(0, L, size=(M, Nw, 3)).astype(np.int16)
acc = np.zeros((nk, M)); accw = np.zeros(M)
for t in range(T):
    flat = (pos[..., 0].astype(np.int32) * L + pos[..., 1]) * L + pos[..., 2]
    Nt = Wm[:, flat].sum(axis=2)                     # (nk, M)
    acc += Nt
    accw += cs[t] * Nt[2]
    d = rng.integers(0, 12, size=(M, Nw))
    mv = d >= 6
    ax = (d - 6) // 2
    sg = np.where((d - 6) % 2 == 0, 1, -1).astype(np.int16)
    for a in range(3):
        sel = mv & (ax == a)
        pos[..., a] = (pos[..., a] + np.where(sel, sg, 0)) % L

se = np.sqrt(2.0 / (M - 1))
print(f"L={L}, Nw={Nw} (u={u:.4f}), replicas M={M}, T={T}; relative s.e. of a variance ~ {se:.3f}")
print(" kernel             Var_MC/T    Var_exact/T   ratio    asymptotic slope   naive 1/|K| scaling")
v0 = None
for i in range(nk):
    vmc = acc[i].var(ddof=1)
    extra = ""
    if i < 4:
        if i == 0:
            v0 = exact[0]
        sizes = [1, 7, 33, 123]
        extra = f"   exact/exact(R=0) = {exact[i]/v0:.4f} vs 1/|K| = {1/sizes[i]:.4f}"
    print(f" {names[i]:17s}  {vmc/T:9.4f}   {exact[i]/T:9.4f}    {vmc/exact[i]:.3f}    {slope[i]:9.4f}{extra}")
print(f" windowed W={Wwin} (ball R=2): Var_MC = {accw.var(ddof=1):.1f}, exact {exact_win:.1f}; "
      f"windowed/raw exact = {exact_win/exact[2]:.4f} vs total-weight ratio {cs.sum()/T:.4f} (1/W would be {1/Wwin:.4f})")
print(f"elapsed {time.time()-t0:.1f} s")
