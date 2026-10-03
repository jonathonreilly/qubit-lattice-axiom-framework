"""C7c: designed register schedule (massless 1D): efficiency for the packet matched to the dressed window."""
import numpy as np
src = open("c7_register.py").read().split("for m in (0.0, 0.3):")[0]
g = {}; exec(src, g)
N, Om, x = g["N"], g["Om"], g["x"]
U, Vl = g["build"](0.0)
D = 2 * N + 1; a = 2 * x
Pm = Vl @ Vl.conj().T
for T in (16, 24, 32):
    for Q in (0.5, 0.9, 0.99):
        tgt = g["cheb_taps"](T, np.sqrt(2.0)); tgt = tgt / np.linalg.norm(tgt) * np.sqrt(Q)
        th = np.empty(T); C = 1.0
        for t in range(T - 1, -1, -1):
            th[t] = np.arcsin(tgt[t] / C); C *= np.cos(th[t])
        Ufull = np.eye(D, dtype=complex); Ufull[:2 * N, :2 * N] = U; Ufull[-1, -1] = np.exp(-1j * Om)
        V = np.eye(D, dtype=complex)
        for t in range(T):
            Rm = np.eye(D, dtype=complex)
            Rm[a, a] = Rm[-1, -1] = np.cos(th[t]); Rm[a, -1] = -np.sin(th[t]); Rm[-1, a] = np.sin(th[t])
            V = Rm @ Ufull @ V
        Cv = np.zeros((D, D), complex); Cv[:2 * N, :2 * N] = Pm
        nv = (V @ Cv @ V.conj().T)[-1, -1].real
        wh = np.zeros(2 * N, complex); cur = np.zeros(2 * N, complex); cur[a] = 1
        for t in range(T):
            cur = U.conj().T @ cur
            wh += tgt[t] * np.exp(1j * Om * (T - 1 - t)) * cur
        eps_t = np.vdot(wh, Pm @ wh).real / np.vdot(wh, wh).real
        psi = wh - Pm @ wh; psi /= np.linalg.norm(psi)
        p = np.zeros(D, complex); p[:2 * N] = psi
        ne = nv + abs((V @ p)[-1]) ** 2
        print(f"T={T:3d} Q={Q:<5}: P(form|vac)={nv:.3e} (Q*eps_target={Q*eps_t:.3e})  "
              f"P(form|matched particle)={ne:.4f} (Q(1-eps)={Q*(1-eps_t):.4f})")
