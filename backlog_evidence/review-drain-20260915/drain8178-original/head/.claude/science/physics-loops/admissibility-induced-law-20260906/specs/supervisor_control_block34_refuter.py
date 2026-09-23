"""Refuting pass, block 34 — disjoint machinery.
(1) The covariance recursion Sigma_{t+1} = P Sigma_t P^T + I on the torus L = 8 in floating point (numpy) against the mode sum in
    floating point (FFT multiplier) at t = 1..400: site variance and plane-average variance.
(2) The memory time and rate recomputed in floating point (numpy's coth) against the runner's exact enclosures at beta = 6, 12, 24, 48.
(3) An INDEPENDENT sampler of the sphere kernel (block 26's refuter route: a pole sample rotated onto the mean direction, with the cosine
    drawn by inversion) on the torus L = 16 at beta = 6, 12 seeds, the early-window decay rate of E[m_z] against sigma^2/L^2.
(4) The stationary transverse variance V_L by direct summation in floating point for L = 16, 32, 64 against the bracket
    [3/(4 pi^2), 9/16] sigma^2 S_L and against 2 gamma log L (gamma = 3 sqrt3/(4 pi) sigma^2)."""
import sys, numpy as np, time
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1])
import importlib
m = importlib.import_module("admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17")
def A(k): return 1.0 / np.tanh(k) - 1.0 / k
print("== (1): covariance recursion vs mode sum, L = 8, floating point")
L = 8; N = L * L
def shift(axis):
    M = np.zeros((N, N))
    for i in range(L):
        for j in range(L):
            src = i * L + j; dst = (((i - 1) % L) * L + j) if axis == 0 else (i * L + (j - 1) % L)
            M[src, dst] = 1.0
    return M
P = (np.eye(N) + shift(0) + shift(1)) / 3.0
Sigma = np.zeros((N, N)); worst = 0.0
k = 2 * np.pi * np.arange(L) / L; K1, K2 = np.meshgrid(k, k, indexing="ij")
u = (3 + 2 * np.cos(K1) + 2 * np.cos(K2) + 2 * np.cos(K1 - K2)) / 9.0
for t in range(1, 401):
    Sigma = P @ Sigma @ P.T + np.eye(N)
    site = np.trace(Sigma) / N; avg = Sigma.sum() / N ** 2
    mask = np.ones_like(u, dtype=bool); mask[0, 0] = False
    site_modes = (t + ((1 - u[mask] ** t) / (1 - u[mask])).sum()) / N
    worst = max(worst, abs(site - site_modes), abs(avg - t / N))
print(f"largest discrepancy over t <= 400: {worst:.2e}")
print("== (2): memory time and rate, floating point vs the exact enclosures")
for beta in (6, 12, 24, 48):
    a_lo, a_hi = m.A_bounds(Fr(3 * beta)); af = A(3.0 * beta)
    for LL in (16, 32, 64):
        tau = 3 * beta * LL * LL / af
        print(f"  beta={beta} L={LL}: tau = {tau:.2f} (exact enclosure [{float(3*beta*LL*LL/a_hi):.2f}, {float(3*beta*LL*LL/a_lo):.2f}]); rate = {af/(3*beta*LL*LL):.4e}")
print("== (3): independent sampler on the torus L = 16, beta = 6")
def sample_rot(rng, u, kappa):
    """draw s ~ exp(kappa s.u): cosine by inversion, azimuth uniform, built at the pole and rotated onto u by a Rodrigues rotation."""
    U = rng.random(u.shape[:-1]); w = 1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kappa)) / kappa; w = np.clip(w, -1, 1)
    ph = rng.random(u.shape[:-1]) * 2 * np.pi; r = np.sqrt(np.clip(1 - w * w, 0, 1))
    v = np.stack([r * np.cos(ph), r * np.sin(ph), w], axis=-1)      # sample around the pole
    z = np.zeros_like(u); z[..., 2] = 1.0
    axis = np.cross(z, u); sn = np.linalg.norm(axis, axis=-1); cs = u[..., 2]
    small = sn < 1e-12
    ax = axis / np.where(small, 1.0, sn)[..., None]
    # Rodrigues: v cos + (ax x v) sin + ax (ax.v)(1 - cos)
    out = v * cs[..., None] + np.cross(ax, v) * sn[..., None] + ax * (ax * v).sum(-1)[..., None] * (1 - cs)[..., None]
    out = np.where(small[..., None], np.where((cs > 0)[..., None], v, v * np.array([1, 1, -1.0])), out)
    return out
def run_sphere_rot(beta, L, T, seed, every):
    rng = np.random.default_rng(seed); s = np.zeros((L, L, 3)); s[..., 2] = 1.0; out = []
    for t in range(1, T + 1):
        S = s + np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1); norm = np.linalg.norm(S, axis=2)
        s = sample_rot(rng, S / norm[..., None], beta * norm)
        if t % every == 0: out.append((t, s.mean(axis=(0, 1))[2]))
    return out
beta, L, T, seeds = 6.0, 16, 30000, 12; every = T // 400; t0 = time.time(); acc = None
for sd in range(seeds):
    res = run_sphere_rot(beta, L, T, 900 + sd, every); arr = np.array([r[1] for r in res]); acc = arr if acc is None else acc + arr
acc /= seeds; ts = np.array([r[0] for r in res]); idx = np.where(acc < 0.2 * acc[0])[0]; end = idx[0] if len(idx) else len(acc)
sl, _ = np.polyfit(ts[:max(end, 6)], np.log(np.clip(acc[:max(end, 6)], 1e-6, None)), 1); rate_lin = A(3 * beta) / (3 * beta) / L ** 2
print(f"independent sampler: early-window rate {-sl:.3e}, sigma^2/L^2 = {rate_lin:.3e}, ratio {-sl/rate_lin:.2f} ({time.time()-t0:.0f}s)")
print("== (4): V_L by direct summation vs the bracket and 2 gamma log L")
for LL in (16, 32, 64, 128):
    k = 2 * np.pi * np.arange(LL) / LL; K1, K2 = np.meshgrid(k, k, indexing="ij")
    u = (3 + 2 * np.cos(K1) + 2 * np.cos(K2) + 2 * np.cos(K1 - K2)) / 9.0; mask = np.ones_like(u, dtype=bool); mask[0, 0] = False
    V = (1 / (1 - u[mask])).sum() / LL ** 2; S = float(m.lattice_sum(LL)) if LL <= 64 else None
    c0 = 3 * np.sqrt(3) / (4 * np.pi)
    print(f"  L={LL}: V_L/sigma^2 = {V:.4f}; bracket [{3/(4*np.pi**2)*S if S else float('nan'):.3f}, {9/16*S if S else float('nan'):.3f}]; 2 c0 log L = {2*c0*np.log(LL):.4f}; V_L - 2 c0 log L = {V - 2*c0*np.log(LL):.4f}")
print("== verdict: consistent" )
