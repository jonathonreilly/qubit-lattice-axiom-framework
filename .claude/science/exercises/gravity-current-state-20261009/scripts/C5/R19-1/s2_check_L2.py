"""R19-1 s2: recheck of the copied R18-1 engine + my f-sum estimator against exact L=2 enumeration (s1)."""
import numpy as np, subprocess, sys, pickle, itertools
sys.path.insert(0, '.')
from common import *
from mc import *
from fsum import fsum_meas, phase_table
L = 2; V = 8; G = G_matrix(L); P = pattern_vectors(L); B = f2_basis(P); d = B.shape[0]
states = np.array([(np.array(c) @ B) % 2 for c in itertools.product([0, 1], repeat=d)], dtype=np.int64)
gam = (G @ states.T)//2; Es = (gam**2).sum(0).astype(float)
S_, GE, GN = move_tables(L)
K = np.array([[0, 0, np.pi], [np.pi, np.pi, 0], [np.pi, np.pi, np.pi]]); PH = phase_table(K, L)
for bU in [0.0, 1.0, 2.0]:
    pi = np.exp(-bU*Es); pi /= pi.sum()
    # exact: average fsum_meas over the enumerated states (state vector -> n[t,x,y,z])
    Mex = np.zeros((3, 6, 6), complex)
    for i, s in enumerate(states):
        n = s.reshape(6, L, L, L).copy(); g = charges(n, L); Mf = np.zeros((3, 6, 6), complex)
        fsum_meas(n, g, L, bU, S_, GE, GN, PH, Mf); Mex += pi[i]*Mf
    Mex /= 2*V
    # MC
    n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); sweeps(n, g, L, bU, S_, GE, GN, 2000, 3)
    Mmc = np.zeros((3, 6, 6), complex); nm = 20000
    for it in range(nm):
        sweeps(n, g, L, bU, S_, GE, GN, 1, 50 + it, it % 2); Mf = np.zeros((3, 6, 6), complex)
        fsum_meas(n, g, L, bU, S_, GE, GN, PH, Mf); Mmc += Mf
    Mmc /= nm*2*V
    c = cvec(channel_pols(np.array([1., 1, 0]))['TT'][1])
    print("bU=%.1f: TT2 at k=(pi,pi,0): f exact-enum = %.5f (s1 quantum/classical value at bU=1: 1.24920), f MC = %.5f; max|Mex-Mmc| = %.4f"
          % (bU, np.real(c @ Mex[1] @ c), np.real(c @ Mmc[1] @ c), np.abs(Mex - Mmc).max()))
