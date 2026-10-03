"""C7: the window as a concrete local, causal instrument (quasi-free, exact many-body).
Field: 1D Dirac step on a ring (N sites x 2). Register: one fermion slot d at site x, phase e^{-i Omega}
per tick; after each tick's step, a number-conserving swap of angle g*w(t) between (x,R) and d.
At the window's end the formation instrument acts on the register only: P(form) = <n_d>.
Vacuum: lower band filled, register empty. Excitation: vacuum + one particle in psi = P_+ w_hat (normalised),
the best-matched upper-band packet. Everything is a single-particle unitary V, so <n_d> = (V C V^+)_dd."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np

N, Om = 160, np.pi / 2
x = N // 2


def build(m):
    cm, sm = np.cos(m), np.sin(m)
    S = np.zeros((2 * N, 2 * N), complex)
    for xx in range(N):
        S[2 * ((xx + 1) % N), 2 * xx] = 1
        S[2 * ((xx - 1) % N) + 1, 2 * xx + 1] = 1
    U = np.kron(np.eye(N), np.array([[cm, -1j * sm], [-1j * sm, cm]])) @ S
    lam, V = np.linalg.eig(U)
    V, _ = np.linalg.qr(V)
    th = -np.angle(lam)
    if m == 0:            # massless: degenerate eigenvalues; define bands by the R/L momentum directly
        k = 2 * np.pi * np.arange(N) / N
        k = np.where(k > np.pi, k - 2 * np.pi, k)
        cols = []
        for kk in k:
            pw = np.exp(1j * kk * np.arange(N)) / np.sqrt(N)
            vR = np.zeros(2 * N, complex); vR[0::2] = pw          # R mover, theta = k
            vL = np.zeros(2 * N, complex); vL[1::2] = pw          # L mover, theta = -k
            if -np.pi < kk < 0: cols.append(vR)
            if 0 < kk < np.pi: cols.append(vL)
            if kk == 0 or kk == np.pi:                             # half-weight zero modes: fill one of each pair
                cols.append(vR if kk == np.pi else vL)
        Vl = np.array(cols).T
    else:
        Vl = V[:, th < 0]
    return U, Vl


def cheb_taps(T, x0):
    n = T - 1; Mf = 4 * T
    nu = 2 * np.pi * np.arange(Mf) / Mf
    y = x0 * np.cos(nu / 2)
    W = np.exp(1j * nu * n / 2) * np.where(np.abs(y) <= 1, np.cos(n * np.arccos(np.clip(y, -1, 1))),
                                            np.sign(y) ** n * np.cosh(n * np.arccosh(np.maximum(np.abs(y), 1))))
    taps = (np.fft.fft(W) / Mf).real[:T]                      # w_t = (1/M) sum_j W(nu_j) e^{-i nu_j t}
    return taps / taps.max()


def respond(U, Vl, w, g, m):
    D = 2 * N + 1                                          # last index = register slot
    Vtot = np.eye(D, dtype=complex)
    Ufull = np.eye(D, dtype=complex); Ufull[:2 * N, :2 * N] = U; Ufull[-1, -1] = np.exp(-1j * Om)
    a = 2 * x
    for t in range(len(w)):
        th = g * w[t]
        R = np.eye(D, dtype=complex)
        R[a, a] = R[-1, -1] = np.cos(th); R[a, -1] = -np.sin(th); R[-1, a] = np.sin(th)
        Vtot = R @ Ufull @ Vtot
    Cvac = np.zeros((D, D), complex); Cvac[:2 * N, :2 * N] = Vl @ Vl.conj().T
    n_vac = (Vtot @ Cvac @ Vtot.conj().T)[-1, -1].real
    # matched excitation: psi = P_+ w_hat, w_hat = sum_t w_t e^{+i Om (T-1-t)} U^{-(t+1)} e_{x,R}
    T = len(w)
    wh = np.zeros(2 * N, complex); cur = np.zeros(2 * N, complex); cur[a] = 1
    Ui = U.conj().T
    for t in range(T):
        cur = Ui @ cur
        wh += w[t] * np.exp(1j * Om * (T - 1 - t)) * cur
    Pm = Vl @ Vl.conj().T
    eps_mode = np.vdot(wh, Pm @ wh).real / np.vdot(wh, wh).real
    psi = wh - Pm @ wh; psi /= np.linalg.norm(psi)
    p = np.zeros(D, complex); p[:2 * N] = psi
    n_exc = n_vac + abs((Vtot @ p)[-1]) ** 2
    return n_vac, n_exc, eps_mode


for m in (0.0, 0.3):
    U, Vl = build(m)
    print(f"--- m={m}: filled modes {Vl.shape[1]} / {2*N}; orthonormal err {np.abs(Vl.conj().T@Vl-np.eye(Vl.shape[1])).max():.1e}")
    for T in (16, 32, 48):
        th_e = np.pi / 2 + m
        for name, w in (("hann", np.sin(np.pi * (np.arange(T) + 1) / (T + 1)) ** 2),
                        ("cheb", cheb_taps(T, 1 / np.cos(th_e / 2)))):
            for g in (0.02, 0.4):
                nv, ne, em = respond(U, Vl, w, g, m)
                print(f"T={T:3d} {name}: g={g:<5} P(form|vac)={nv:.3e}  P(form|1 particle)={ne:.3e}  "
                      f"ratio={nv/(ne-nv):.3e}  single-mode eps={em:.3e}")
