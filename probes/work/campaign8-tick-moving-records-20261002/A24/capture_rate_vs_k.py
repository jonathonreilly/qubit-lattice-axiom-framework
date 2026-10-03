#!/usr/bin/env python3
"""A24 S4b: per-record energy of a rate-f formation instrument on the capture trap, vs the emitted quantum's momentum.
Prediction (stationary capture, small f):  E_inj / record = c sum_t dE_bin(t) / p_cap -> (f/2) cot k_e
  = (1/2) f x (emitted quantum's dwell time on the capture bond 1/v_e) x (its depth below band centre 2 J_C cos k_e).
Same network as S4 (capture_trap.py); the trap depth V sets k_e through E_probe + V = -2 J_C cos k_e."""
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm

LB, LC, JB, JC, g, j0 = 300, 400, 1.0, 1.0, 1.0, 200
q, wq, x_s = 0.3, 12.0, 130


def build(V):
    N = LB + LC
    H = np.zeros((N, N))
    for x in range(LB - 1):
        H[x, x + 1] = H[x + 1, x] = -JB
    for z in range(LC - 1):
        H[LB + z, LB + z + 1] = H[LB + z + 1, LB + z] = -JC
    for z in range(LC):
        H[LB + z, LB + z] = -V
    H[LB, j0] = H[j0, LB] = g
    return H


x = np.arange(LB)
for V in (0.2, 0.6, 1.0, 1.5, 1.9):
    H = build(V); Hs = sp.csr_matrix(H); N = H.shape[0]
    psi0 = np.zeros(N, complex); psi0[:LB] = np.exp(-(x - x_s) ** 2 / (4 * wq ** 2) + 1j * q * x); psi0 /= np.linalg.norm(psi0)
    E0 = np.vdot(psi0, Hs @ psi0).real
    ke = np.arccos(-(E0 + V) / (2 * JC))
    U1 = expm(-1j * H)
    P = np.zeros(N); P[LB:] = 1.0
    out = []
    for f in (0.01, 0.003):
        c = 1 - np.sqrt(1 - f); Kn = 1 - c * P
        psi = psi0.copy(); inj = 0.0; rec = 0.0
        for t in range(360):
            psi = U1 @ psi
            vf = np.sqrt(f) * P * psi; vn = Kn * psi
            inj += np.vdot(vf, Hs @ vf).real + np.vdot(vn, Hs @ vn).real - np.vdot(psi, Hs @ psi).real
            rec += np.vdot(vf, vf).real
            psi = vn
        tot = rec + np.sum(P * np.abs(psi) ** 2)
        out.append((f, inj / tot / f, tot))
    print(f"V={V}: emitted k_e={ke:.4f} (v_e={2*JC*np.sin(ke):.3f}); predicted (inj/record)/f = cot(k_e)/2 = {0.5/np.tan(ke):+.4f}; "
          + "; ".join(f"f={f}: {r:+.4f} (P(capture) {p:.3f})" for f, r, p in out))
