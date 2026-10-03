"""A17 check C3 (supplied 1D toy): the A5 Dirac step with a paced mass coin.

Step: R content shifts right, L content shifts left, then coin C(theta_x) = cos - i sin sigma_x at each site,
with theta_x = m * d(x,t).  Ideal: d = 1.  Only the coin (rest-energy phase) is paced here, to isolate the
rest-energy phase that dominates heavy matter; pacing the shift too is A14's question.
Dose fields (one shared field per realization):
  per-site events:  d = e/p,  e ~ Bernoulli(p) iid per site and tick;
  smoothed:         d = box_R(e) / (p (2R+1))   (periodic box of 2R+1 sites).
Part A: single branch, fidelity F = |<psi_ideal|psi_paced>|^2.  Second-order prediction (EXACT to O(m^2),
        cross-tick terms vanish in expectation):  E[1-F] = m^2 sum_t E[ <dd^2>_rho - (<dd s>)^2 ],
        dd = d - 1, rho = |psi|^2, s = psi^+ sigma_x psi on the ideal trajectory.
Part B: two branches at separation D in the SAME dose field (shared environment), recombined by translation.
        Per-run phase vs prediction -m sum_t [<d>_2 - <d>_1]; Var of the phase vs the box-kernel formula.
Part C: deterministic gradient d = N(x) = 1 + g (x - xc): relative phase (COW-like) and universal fall.
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import time
import numpy as np

t0 = time.time()
L = 4096
X = np.arange(L)
kk = 2 * np.pi * np.fft.fftfreq(L)


def packet(m, x0, sig):
    c, s = np.cos(m), np.sin(m)
    U = np.empty((L, 2, 2), complex)
    U[:, 0, 0] = c * np.exp(-1j * kk); U[:, 0, 1] = -1j * s * np.exp(1j * kk)
    U[:, 1, 0] = -1j * s * np.exp(-1j * kk); U[:, 1, 1] = c * np.exp(1j * kk)
    ev, vec = np.linalg.eig(U)
    pick = np.argmin(np.angle(ev), axis=1)               # e^{-i omega}, omega in (0, pi): positive branch
    v = vec[np.arange(L), :, pick]                        # (L, 2)
    v = v / np.linalg.norm(v, axis=1, keepdims=True)
    v = v * np.exp(-1j * np.angle(v[:, :1]))              # smooth gauge: first component real
    g = np.exp(-(kk ** 2) * sig ** 2) * np.exp(-1j * kk * x0)
    psi = np.fft.ifft((g[:, None] * v).T, axis=1)         # (2, L)
    return psi / np.linalg.norm(psi)


def step(psi, theta):
    """psi (..., 2, L); theta broadcastable to (..., L)."""
    a = np.roll(psi[..., 0, :], 1, axis=-1)
    b = np.roll(psi[..., 1, :], -1, axis=-1)
    c, s = np.cos(theta), np.sin(theta)
    out = np.empty_like(psi)
    out[..., 0, :] = c * a - 1j * s * b
    out[..., 1, :] = -1j * s * a + c * b
    return out


def boxfft(R):
    b = np.zeros(L); b[:R + 1] = 1; b[L - R:] = 1
    return np.fft.fft(b)


def dose(rng, nr, p, R, BF):
    e = (rng.random((nr, L)) < p).astype(float)
    if R == 0:
        return e / p
    return np.real(np.fft.ifft(np.fft.fft(e, axis=1) * BF, axis=1)) / (p * (2 * R + 1))


rng = np.random.default_rng(20261003)

print("== Part A: within-branch scrambling (m=0.01, p=0.25, T=200, sigma=30, 60 realizations) ==")
m, p, T, nr = 0.01, 0.25, 200, 60
psi0 = packet(m, L // 2, 30.0)
for R in (0, 3, 200):
    BF = boxfft(R) if R else None
    ps = np.repeat(psi0[None], nr, axis=0)
    pi = psi0.copy()
    pred = np.zeros(nr)
    for t in range(T):
        d = dose(rng, nr, p, R, BF)
        ps = step(ps, m * d)
        pi = step(pi, m)
        rho = (np.abs(pi) ** 2).sum(0)
        sx = 2 * np.real(np.conj(pi[0]) * pi[1])
        dd = d - 1.0
        pred += m ** 2 * ((dd ** 2) @ rho - (dd @ sx) ** 2)
    F = np.abs(np.einsum('cx,rcx->r', np.conj(pi), ps)) ** 2
    vd = (1 - p) / p / (2 * R + 1)
    print(f" R={R:3d}: E[1-F] = {np.mean(1-F):.5f} +- {np.std(1-F)/np.sqrt(nr):.5f}; E[-ln F] = {np.mean(-np.log(F)):.5f};"
          f" 2nd-order pred = {np.mean(pred):.5f};  naive m^2 T Var(d) = {m*m*T*vd:.5f}")

print("\n== Part B: two branches in one shared dose field (m=0.15, p=0.05, R=200, T=200, sigma=30, 600 runs) ==")
m, p, T, R, nr = 0.15, 0.05, 200, 200, 200
BF = boxfft(R)
x1 = 1000
for D in (600, 100):
    pa = packet(m, x1, 30.0); pb = packet(m, x1 + D, 30.0)
    s1 = 2 * np.real(np.conj(pa[0]) * pa[1]); s2 = 2 * np.real(np.conj(pb[0]) * pb[1])
    Ol, pl = [], []
    for batch in range(3):
        A = np.repeat(pa[None], nr, axis=0); B = np.repeat(pb[None], nr, axis=0)
        ph_pred = np.zeros(nr)
        for t in range(T):
            d = dose(rng, nr, p, R, BF)
            A = step(A, m * d); B = step(B, m * d)
            ph_pred += -m * (d @ s2 - d @ s1)
        Bback = np.roll(B, -D, axis=-1)
        Ol.append(np.einsum('rcx,rcx->r', np.conj(A), Bback)); pl.append(ph_pred)
        del A, B, Bback
    O = np.concatenate(Ol); ph_pred = np.concatenate(pl)
    ph = np.angle(O)
    vd = (1 - p) / p
    if D >= 2 * R + 1:
        var_th = m * m * 2 * T * vd / (2 * R + 1)
    else:
        var_th = m * m * T * 2 * D * vd / (2 * R + 1) ** 2
    print(f" D={D:3d}: mean|O| = {np.mean(np.abs(O)):.6f} (single run, ideal 1);  max|phase - predicted| = "
          f"{np.max(np.abs(np.angle(np.exp(1j*(ph-ph_pred))))):.2e} rad")
    box = np.zeros(L); box[:R + 1] = 1; box[L - R:] = 1
    kA = np.real(np.fft.ifft(np.fft.fft(s1) * np.fft.fft(box))); kB = np.real(np.fft.ifft(np.fft.fft(s2) * np.fft.fft(box)))
    var_pk = m * m * T * p * (1 - p) / (p * (2 * R + 1)) ** 2 * np.sum((kB - kA) ** 2)
    dev = np.angle(np.exp(1j * (ph - ph_pred)))
    print(f"        rms|phase - predicted| = {np.sqrt(np.mean(dev**2)):.2e} rad (phase sd {np.std(ph):.3f})")
    print(f"        Var(phase) = {np.var(ph):.4f} vs point-kernel formula {var_th:.4f}, packet-weighted exact {var_pk:.4f}"
          f" (s.e. ~{np.sqrt(2/(len(O)-1)):.2f} rel);  ensemble |E O| = {np.abs(np.mean(O)):.4f}"
          f" vs mean|O| * exp(-Var_pk/2) = {np.mean(np.abs(O))*np.exp(-var_pk/2):.4f}")

print("\n== Part C: deterministic gradient N(x) = 1 + g (x - xc), g = 1e-4, D = 600, T = 200 (no noise) ==")
g, T, D = 1e-4, 200, 600
xc = 2048
Nx = 1 + g * (X - xc)
for m in (0.05, 0.15):
    pa = packet(m, xc - D // 2, 30.0); pb = packet(m, xc + D // 2, 30.0)
    ca0 = (np.abs(pa) ** 2).sum(0) @ X
    A, B = pa.copy(), pb.copy()
    for t in range(T):
        A = step(A, m * Nx); B = step(B, m * Nx)
    O = np.vdot(A.ravel(), np.roll(B, -D, axis=-1).ravel())
    ca = (np.abs(A) ** 2).sum(0) @ X
    print(f" m={m}: arg O = {np.angle(O):+.4f} rad vs -m g D T = {-m*g*D*T:+.4f};  |O| = {abs(O):.6f};"
          f" centroid shift = {ca-ca0:+.3f} vs -(1/2) g T^2 m/tan(m) = {-0.5*g*T*T*m/np.tan(m):+.3f}")
print(f"\nelapsed {time.time()-t0:.1f} s")
