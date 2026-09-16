"""Refuting pass, block 26 (independent machinery).
Modes: fast - the control's sampler against the exact moments by Monte Carlo, P_k by FFT convolution against the exact sums, the linear
recursion on a torus against the exact variance; sphere - the sphere formation law with an independently coded sampler (inversion written
the other way, tangent frame by a Rodrigues rotation of a pole sample); linear - the linear model against its exact prediction.
Usage: python3 <this> <mode> <beta> <L> <T> <seed>."""
# Refuting-pass simulations (independent code): (a) sphere formation law with a differently coded vMF sampler (inversion written the other
# way, tangent frame by a Rodrigues rotation of a pole sample); (b) the linear Gaussian model theta_x = avg + N(0, A(3b)/(3b) I_2) with
# its exact prediction v_t = sigma^2 sum_{k<t} P_k; (c) finite-size series at beta = 6 (L = 64, 128).
import numpy as np, sys, time
from math import factorial
mode = sys.argv[1]; beta = float(sys.argv[2]); L = int(sys.argv[3]); T = int(sys.argv[4]); seed = int(sys.argv[5])
rng = np.random.default_rng(seed); rec = max(1, T // 40)
def A(x): return 1 / np.tanh(x) - 1 / x
t0 = time.time()
if mode == "fast":
    print("refuter fast checks")
    # (i) the control's sampler (inversion of the cosine law, uniform azimuth) against E[w] = A(kappa), E[w^2] = 1 - 2A/kappa
    for kap in (1.0, 3.0, 9.0, 18.0, 36.0):
        n = 2_000_000; U = rng.random(n); w = 1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap
        print(f"  kappa={kap:5.1f}: mean w = {w.mean():.5f} vs A = {A(kap):.5f}; mean w^2 = {(w*w).mean():.5f} vs 1 - 2A/kappa = {1 - 2*A(kap)/kap:.5f}")
    # (ii) P_k by FFT convolution of the step law on a 1024 x 1024 torus (no wrap for k < 1024)
    from math import factorial
    def Pk_exact(k):
        tot = 0
        for a in range(k + 1):
            for b in range(k + 1 - a):
                mlt = factorial(k) // (factorial(a) * factorial(b) * factorial(k - a - b)); tot += mlt * mlt
        return tot / 9 ** k
    N = 1024; step = np.zeros((N, N)); step[0, 0] = step[-1, 0] = step[0, -1] = 1 / 3
    Fs = np.fft.fft2(step); c0 = 3 * np.sqrt(3) / (4 * np.pi)
    for k in (1, 2, 3, 10, 50, 150, 300, 600):
        pk = np.real(np.fft.ifft2(Fs ** k)); Pk = float((pk * pk).sum())
        ex = Pk_exact(k) if k <= 150 else float("nan")
        print(f"  k={k:4d}: P_k(FFT) = {Pk:.10f}  exact = {ex:.10f}  k P_k = {k*Pk:.5f}  (c0 = {c0:.5f})")
    # (iii) the linear recursion on a 128 x 128 torus for 40 levels, 400 independent noise realisations, against sigma^2 sum_{k<t} P_k
    sig2 = A(18) / 18; Lt = 128; reps = 400; acc = np.zeros(41)
    for r_ in range(reps):
        th = np.zeros((Lt, Lt, 2))
        for t in range(1, 41):
            th = (th + np.roll(th, 1, 0) + np.roll(th, 1, 1)) / 3 + rng.normal(0, np.sqrt(sig2), (Lt, Lt, 2))
            acc[t] += (th * th).sum(-1).mean() / 2
    acc /= reps
    for t in (1, 2, 5, 10, 20, 40):
        cum = sig2 * sum(Pk_exact(k) for k in range(t))
        print(f"  t={t:3d}: v_t(sim) = {acc[t]:.5f}  exact sigma^2 sum_(k<t) P_k = {cum:.5f}")
if mode == "sphere":
    s = np.zeros((L, L, 3)); s[..., 2] = 1
    print(f"refuter sphere beta={beta} L={L} T={T} seed={seed}")
    for t in range(1, T + 1):
        Sv = s + np.roll(s, 1, 0) + np.roll(s, 1, 1); n = np.sqrt((Sv * Sv).sum(-1)); u = Sv / n[..., None]; kap = beta * n
        U = rng.random((L, L)); w = 1 + np.log1p(-U * (1 - np.exp(-2 * kap))) / kap
        w = np.clip(w, -1, 1); ph = 2 * np.pi * rng.random((L, L)); r = np.sqrt(1 - w * w)
        v = np.stack([r * np.cos(ph), r * np.sin(ph), w], -1)          # sample around the pole
        # Rodrigues rotation taking the pole to u: axis k = z x u, angle with cos = u_z
        kx, ky = -u[..., 1], u[..., 0]; kn = np.sqrt(kx * kx + ky * ky); c = u[..., 2]
        safe = kn > 1e-12; kx = np.where(safe, kx / np.where(safe, kn, 1), 0); ky = np.where(safe, ky / np.where(safe, kn, 1), 0)
        sn = np.sqrt(np.clip(1 - c * c, 0, 1))
        K = np.stack([kx, ky, np.zeros_like(kx)], -1)
        kv = np.cross(K, v); kdv = (K * v).sum(-1)
        s_new = v * c[..., None] + kv * sn[..., None] + K * (kdv * (1 - c))[..., None]
        s = np.where(safe[..., None], s_new, np.where((c > 0)[..., None], v, -v))
        if t % rec == 0:
            m = s.mean((0, 1)); print(f"  t={t:6d}  |m|={np.linalg.norm(m):.5f}  m_z={m[2]:.5f}")
elif mode == "linear":
    sig2 = A(3 * beta) / (3 * beta)
    th = np.zeros((L, L, 2)); P = []
    # exact P_k (floats) for the prediction
    def Pk(k):
        tot = 0
        for a in range(k + 1):
            for b in range(k + 1 - a):
                mlt = factorial(k) // (factorial(a) * factorial(b) * factorial(k - a - b)); tot += mlt * mlt
        return tot / 9 ** k
    pred = {}
    print(f"refuter linear beta={beta} sigma^2={sig2:.6f} L={L} T={T} seed={seed}")
    for t in range(1, T + 1):
        th = (th + np.roll(th, 1, 0) + np.roll(th, 1, 1)) / 3 + rng.normal(0, np.sqrt(sig2), (L, L, 2))
        if t % rec == 0:
            v = (th * th).sum(-1).mean() / 2
            print(f"  t={t:6d}  v_t(sim)={v:.5f}  exp(-v)={np.exp(-v):.5f}")
    # prediction at a few t (sum of P_k up to t-1 via quadrature for speed)
    n = 2048; g = np.linspace(-np.pi, np.pi, n, endpoint=False); T1, T2 = np.meshgrid(g, g, indexing="ij")
    u = (3 + 2 * np.cos(T1) + 2 * np.cos(T2) + 2 * np.cos(T1 - T2)) / 9
    acc = 0.0; uk = np.ones_like(u)
    for k in range(0, T):
        acc += uk.mean(); uk = uk * u
        if (k + 1) % rec == 0: print(f"  prediction v_{k+1} = sigma^2 sum_(k'<{k+1}) P_k' = {sig2 * acc:.5f}")
print(f"({time.time()-t0:.0f}s)")
