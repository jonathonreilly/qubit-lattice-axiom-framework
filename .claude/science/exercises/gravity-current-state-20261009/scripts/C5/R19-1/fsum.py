"""R19-1 f-sum measurement at the RK point (method fixed in METHOD_preregistered.md (a)).
f(k,eps) = (1/2V) sum_m <exp(-bU Delta_m/2) |sum_{s in p_m} e^{-ik.pos_s} c_s sigma_s|^2>, t = 1.
Accumulates the 6x6 slot-type matrix Mf[k] = sum_m r_m A_m(k)^* A_m(k)^T per configuration; f = c.Mf.c/(2V)."""
import numpy as np, numba as nb
from mc import *
@nb.njit(cache=True)
def fsum_meas(n, g, L, bU, S, GE, GN, PH, Mf):
    npat = S.shape[0]; nk = PH.shape[0]
    eidx = np.zeros((64, 4), dtype=np.int64); edel = np.zeros(64, dtype=np.int64)
    A = np.zeros((nk, 6), dtype=np.complex128)
    for a in range(npat):
        for bx in range(L):
            for by in range(L):
                for bz in range(L):
                    ne = 0
                    for kk in range(nk):
                        for t in range(6): A[kk, t] = 0
                    for b in range(S.shape[1]):
                        if S[a, b, 0] < 0: break
                        sx = (bx + S[a, b, 0]) % L; sy = (by + S[a, b, 1]) % L; sz = (bz + S[a, b, 2]) % L; t = S[a, b, 3]
                        dl = 1 - 2*n[t, sx, sy, sz]
                        for kk in range(nk): A[kk, t] += PH[kk, t, sx, sy, sz]*dl
                        for q in range(GN[t]):
                            ex = (sx + GE[t, q, 0]) % L; ey = (sy + GE[t, q, 1]) % L; ez = (sz + GE[t, q, 2]) % L; j = GE[t, q, 3]
                            found = -1
                            for r in range(ne):
                                if eidx[r, 0] == ex and eidx[r, 1] == ey and eidx[r, 2] == ez and eidx[r, 3] == j:
                                    found = r; break
                            if found < 0:
                                eidx[ne, 0] = ex; eidx[ne, 1] = ey; eidx[ne, 2] = ez; eidx[ne, 3] = j; edel[ne] = 0; found = ne; ne += 1
                            edel[found] += GE[t, q, 4]*dl
                    dE = 0.0
                    for r in range(ne):
                        g0 = g[eidx[r, 3], eidx[r, 0], eidx[r, 1], eidx[r, 2]]; g1 = g0 + edel[r]
                        dE += (g1*g1 - g0*g0)/4.0
                    rate = np.exp(-bU*dE/2.0)
                    for kk in range(nk):
                        for t1 in range(6):
                            c1 = np.conj(A[kk, t1])*rate
                            for t2 in range(6):
                                Mf[kk, t1, t2] += c1*A[kk, t2]
def phase_table(K, L):
    nk = len(K); PH = np.zeros((nk, 6, L, L, L), complex)
    xs = np.array(np.meshgrid(range(L), range(L), range(L), indexing='ij'), float)
    for kk in range(nk):
        for t in range(6):
            PH[kk, t] = np.exp(-1j*(K[kk][0]*(xs[0] + OFFS[t][0]) + K[kk][1]*(xs[1] + OFFS[t][1]) + K[kk][2]*(xs[2] + OFFS[t][2])))
    return PH
