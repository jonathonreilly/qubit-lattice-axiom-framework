"""the sphere formation law on a periodic L x L level plane at strong coupling: the equal-level transverse structure factor
S_0(k) = E|s_perp^(k)|^2 (per component, unitary DFT) and the cross-level correlation C_s(k) = E[s_perp^(k, t) conj s_perp^(k, t+s)]
accumulated over the last T - T0 levels, against the linearized kernel sigma^2 phi(k)^s / (1 - |phi(k)|^2), phi = (1 + e^{ik1} + e^{ik2})/3.
Transverse components: the two components orthogonal to the initial direction (the average direction stays near it: the memory time
3 beta L^2 / A(3 beta) is far beyond the run)."""
import numpy as np, sys, time
def A(k): return 1.0 / np.tanh(k) - 1.0 / k
beta = float(sys.argv[1]); L = int(sys.argv[2]); T = int(sys.argv[3]); T0 = int(sys.argv[4]); seed = int(sys.argv[5])
lags = [0, 1, 2, 4, 8, 16, 32, 64]; maxlag = max(lags)
rng = np.random.default_rng(seed); s = np.zeros((L, L, 3)); s[..., 2] = 1.0
k = 2 * np.pi * np.arange(L) / L; K1, K2 = np.meshgrid(k, k, indexing="ij")
phi = (1 + np.exp(1j * K1) + np.exp(1j * K2)) / 3.0; u = np.abs(phi) ** 2
sigma2 = A(3 * beta) / (3 * beta)
hist = []; acc = {l: np.zeros((L, L), dtype=complex) for l in lags}; n = {l: 0 for l in lags}; mabs = []
t0 = time.time()
for t in range(1, T + 1):
    S = s + np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1)
    norm = np.linalg.norm(S, axis=2); uu = S / norm[..., None]; kappa = beta * norm
    U = rng.random((L, L)); w = 1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa
    w = np.clip(w, -1.0, 1.0); ph = rng.random((L, L)) * 2 * np.pi
    a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    e1 = a - (a * uu).sum(-1)[..., None] * uu; e1 /= np.linalg.norm(e1, axis=2)[..., None]; e2 = np.cross(uu, e1)
    r = np.sqrt(np.clip(1 - w * w, 0, 1))
    s = w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * e1 + np.sin(ph)[..., None] * e2)
    if t > T0 - maxlag:
        # transverse field: the two components orthogonal to e_z; unitary DFT (divide by L)
        f = (np.fft.fft2(s[..., 0]) + 1j * 0) / L, np.fft.fft2(s[..., 1]) / L
        hist.append(f)
        if len(hist) > maxlag + 1: hist.pop(0)
        if t > T0:
            mabs.append(np.linalg.norm(s.mean(axis=(0, 1))))
            cur = hist[-1]
            for l in lags:
                if len(hist) > l:
                    past = hist[-1 - l]
                    # C_s(k) = E[ f(k, t-s) conj f(k, t) ] averaged over the two components
                    acc[l] += 0.5 * (past[0] * np.conj(cur[0]) + past[1] * np.conj(cur[1])); n[l] += 1
print(f"beta={beta} L={L} T={T} (levels {T0+1}..{T} accumulated; {time.time()-t0:.0f}s): sigma^2 = {sigma2:.5f}; mean |m| = {np.mean(mabs):.4f}")
S0 = (acc[0] / n[0]).real
mask = np.ones((L, L), dtype=bool); mask[0, 0] = False; lin = np.where(mask, sigma2 / np.where(mask, 1 - u, 1.0), 0.0)
ratio = S0[mask] / lin[mask]
kk = np.sqrt(K1 ** 2 + K2 ** 2)
print("equal-level structure factor S_0(k) / [sigma^2/(1-u(k))] by |k| shell (nonzero modes):")
for lo, hi in ((0, 0.3), (0.3, 0.6), (0.6, 1.0), (1.0, 1.5), (1.5, 2.2), (2.2, 3.2), (3.2, 5.0)):
    sel = mask & (kk >= lo) & (kk < hi)
    if sel.sum(): print(f"   |k| in [{lo},{hi}): mean ratio {np.mean(S0[sel]/lin[sel]):.4f} (n={sel.sum()})")
print("cross-level correlation C_s(k)/C_0(k) against phi(k)^s at three modes (modulus, phase):")
for (i, j) in ((1, 0), (2, 2), (4, 1), (8, 8)):
    line = f"   k=2pi({i},{j})/L: "
    for l in lags[1:]:
        c = (acc[l] / n[l])[i, j] / S0[i, j]; p = phi[i, j] ** l
        line += f" s={l}: {abs(c):.3f}/{abs(p):.3f} ph {np.angle(c):+.2f}/{np.angle(p):+.2f};"
    print(line)
# the structure function D(r) = E|theta_x - theta_{x+r}|^2 along the two lattice directions and the diagonal, from S_0 by inverse FFT
C0 = np.fft.ifft2(S0).real   # numpy's ifft2 divides by L^2: C0(r) = (1/L^2) sum_k S0(k) e^{ik.r}, the site covariance per component (unitary forward DFT)
print("structure function D(r) = 2 (C0(0) - C0(r)) along e1, e2, e1+e2 at r = 1, 2, 4, 8, 16, 32 (nonlinear law); linear: 2 sigma^2 (1/L^2) sum_k (1 - cos k.r)/(1-u)")
Dl = lambda rvec: 2 * sigma2 * ((1 - np.cos(K1 * rvec[0] + K2 * rvec[1]))[mask] / (1 - u[mask])).sum() / L**2
for rvec in ((1, 0), (2, 0), (4, 0), (8, 0), (16, 0), (32, 0), (1, 1), (4, 4), (16, 16)):
    d = 2 * (C0[0, 0] - C0[rvec[0] % L, rvec[1] % L])
    print(f"   r={rvec}: nonlinear {d:.4f}  linear {Dl(rvec):.4f}  ratio {d/Dl(rvec):.3f}")
