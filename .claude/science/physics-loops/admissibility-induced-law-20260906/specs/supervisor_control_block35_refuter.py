"""Refuting pass, block 35 — disjoint machinery.
(1) The cross-level covariance Sigma_{t,t+s} = Sigma_t (P^s)^T iterated in floating point on the torus L = 8 for 300 levels; for every
    nonzero mode the ratio (Fourier-projected cross covariance)/(variance) against phi(k)^s, s = 1..16.
(2) The small-k forms numerically: (1 - u(k))/(k^T M k) -> 1 and phi(k)'s phase vs (k1 + k2)/3 as k -> 0.
(3) The nonlinear law re-measured at beta = 12 on a 128 x 128 plane in the frame that rotates with the plane average (transverse
    components orthogonal to m^_t) against the fixed frame of the control: the normalization by |k| shell.
(4) The comparator: the mixed second derivative of log E(k) evaluated numerically at random points (never zero)."""
import sys, os, numpy as np, time
sys.path.insert(0, sys.argv[1])
import importlib
m = importlib.import_module("admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18")
print("== (1): cross-level covariances on L = 8 (floating point) vs phi(k)^s")
L = 8; N = L * L
def shift(axis):
    M = np.zeros((N, N))
    for i in range(L):
        for j in range(L):
            src = i * L + j; dst = (((i - 1) % L) * L + j) if axis == 0 else (i * L + (j - 1) % L); M[src, dst] = 1.0
    return M
P = (np.eye(N) + shift(0) + shift(1)) / 3.0
Sigma = np.zeros((N, N))
for t in range(300): Sigma = P @ Sigma @ P.T + np.eye(N)
k = 2 * np.pi * np.arange(L) / L
worst = 0.0
for n1 in range(L):
    for n2 in range(L):
        if n1 == 0 and n2 == 0: continue
        e = np.array([np.exp(1j * (k[n1] * i + k[n2] * j)) for i in range(L) for j in range(L)]) / L
        var = np.real(np.conj(e) @ Sigma @ e)
        phi = (1 + np.exp(1j * k[n1]) + np.exp(1j * k[n2])) / 3
        for s in range(1, 17):
            cross = np.conj(e) @ Sigma @ np.linalg.matrix_power(P, s).T @ e
            worst = max(worst, abs(cross / var - phi ** s))
print(f"largest |cross/var - phi^s| over all nonzero modes and s <= 16: {worst:.2e}")
print("== (2): small-k forms")
Mm = np.array([[2, -1], [-1, 2]]) / 9.0
for eps in (0.3, 0.1, 0.03, 0.01):
    kk = np.array([eps * 0.7, eps * 1.3]); u = abs((1 + np.exp(1j * kk[0]) + np.exp(1j * kk[1])) / 3) ** 2
    phase = np.angle((1 + np.exp(1j * kk[0]) + np.exp(1j * kk[1])) / 3)
    print(f"  eps={eps}: (1-u)/(k^T M k) = {(1-u)/(kk @ Mm @ kk):.5f}; arg phi / ((k1+k2)/3) = {phase/((kk[0]+kk[1])/3):.5f}")
print("== (3): rotating-frame measurement at beta = 12, L = 128")
def A(x): return 1.0 / np.tanh(x) - 1.0 / x
beta, L, T, T0 = 12.0, 128, 3000, 1500; rng = np.random.default_rng(11); s = np.zeros((L, L, 3)); s[..., 2] = 1.0
kx = 2 * np.pi * np.arange(L) / L; K1, K2 = np.meshgrid(kx, kx, indexing="ij"); u = np.abs((1 + np.exp(1j * K1) + np.exp(1j * K2)) / 3) ** 2
mask = np.ones((L, L), dtype=bool); mask[0, 0] = False; lin = np.where(mask, A(3 * beta) / (3 * beta) / np.where(mask, 1 - u, 1.0), 0.0)
acc = np.zeros((L, L)); n = 0; t0 = time.time()
for t in range(1, T + 1):
    S = s + np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1); norm = np.linalg.norm(S, axis=2); uu = S / norm[..., None]; kappa = beta * norm
    U = rng.random((L, L)); w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa, -1, 1); ph = rng.random((L, L)) * 2 * np.pi
    a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    e1 = a - (a * uu).sum(-1)[..., None] * uu; e1 /= np.linalg.norm(e1, axis=2)[..., None]; e2 = np.cross(uu, e1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
    s = w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * e1 + np.sin(ph)[..., None] * e2)
    if t > T0:
        mh = s.mean(axis=(0, 1)); mh /= np.linalg.norm(mh)
        f1 = np.array([1.0, 0, 0]) - mh[0] * mh; f1 /= np.linalg.norm(f1); f2 = np.cross(mh, f1)
        c1 = np.fft.fft2(s @ f1) / L; c2 = np.fft.fft2(s @ f2) / L
        acc += 0.5 * (np.abs(c1) ** 2 + np.abs(c2) ** 2); n += 1
S0 = acc / n; kk = np.sqrt(K1 ** 2 + K2 ** 2)
for lo, hi in ((0, 0.3), (0.6, 1.0), (1.5, 2.2), (3.2, 5.0)):
    sel = mask & (kk >= lo) & (kk < hi)
    print(f"  |k| in [{lo},{hi}): rotating-frame ratio {np.mean(S0[sel]/lin[sel]):.4f} (control, fixed frame at L=256: 0.898 / 0.934 / 0.936 / 0.938)")
print(f"  ({time.time()-t0:.0f}s)")
print("== (4): the comparator's mixed derivative of log E at random points")
rng = np.random.default_rng(3); vals = []
for _ in range(5):
    k1, k2, k3 = rng.uniform(0.2, 2.8, 3); h = 1e-4
    E = lambda a, b, c: 2 * (1 - np.cos(a)) + 2 * (1 - np.cos(b)) + 2 * (1 - np.cos(c))
    d = (np.log(E(k1 + h, k2, k3 + h)) - np.log(E(k1 + h, k2, k3 - h)) - np.log(E(k1 - h, k2, k3 + h)) + np.log(E(k1 - h, k2, k3 - h))) / (4 * h * h)
    vals.append(d)
print("  d^2 log E / dk1 dk3 at five random points:", ", ".join(f"{v:.4f}" for v in vals))
print("== verdict: consistent" if worst < 1e-8 else "== verdict: INCONSISTENCY in (1)")
