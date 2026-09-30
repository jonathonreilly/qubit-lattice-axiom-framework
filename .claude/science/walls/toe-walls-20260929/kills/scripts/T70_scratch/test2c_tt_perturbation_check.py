"""Test 2c (T70): independent check of the TT response of test2b by second-order perturbation theory
in momentum space (no supercell, no finite amplitude).

TT sector, site-centred (g_xx,g_yy) = (1 + a c, 1 - a c), N = 1, c = cos(kz):
  M = sqrt(g) = 1 - a^2 c^2/2 ;  D = wx*ax + wy*ay + wz*az + m^2 sqrt(g),
  wx = sqrt(g)/g_xx ~ 1 - a c + a^2 c^2/2 ;  wy ~ 1 + a c + a^2 c^2/2 ;  wz = sqrt(g) (bond midpoint) ~ 1 - a^2 c^2/2.
K = M^{-1/2} D M^{-1/2} = K0 + a K1 + a^2 K2 (zero-wave-vector part of K2 is enough at this order).
E = (1/2) Tr sqrt K :  E2 = a^2 [ sum_q K2_qq/(4 w_q) - (1/8) sum_{q,q'} |K1_{qq'}|^2 /(w_q w_q' (w_q + w_q')) ].
K1 connects q -> q +- k with amplitude (ay - ax)/2 ; K2_qq = (ax+ay)/2 (derived in the comment of the notebook: the m^2 and az pieces cancel).
"""
import numpy as np, sys

def A_tt(m, k, N=96):
    q = 2*np.pi*(np.arange(N)+0.5)/N
    qx, qy, qz = np.meshgrid(q, q, q, indexing='ij')
    ax, ay, az = 2-2*np.cos(qx), 2-2*np.cos(qy), 2-2*np.cos(qz)
    w = np.sqrt(m*m + ax + ay + az)
    # K2 diagonal: D2 avg + (1/4) D0 pieces
    #   D2: +ax/4 + ay/4 - az/4 - m^2/4 ; M-factors: +(1/4) D0 = (m^2+ax+ay+az)/4
    K2 = (ax+ay)/2
    term1 = np.mean(K2/(4*w))
    K1sq = ((ay-ax)/2)**2
    tot2 = 0.0
    for sgn in (+1, -1):
        wp = np.sqrt(m*m + ax + ay + 2-2*np.cos(qz+sgn*k))
        tot2 += np.mean(K1sq/(w*wp*(w+wp)))
    return term1 - tot2/8

if __name__ == "__main__":
    m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    # k -> 0 (uniform limit: cos-modulation gives A_uni/2)
    for p in (8, 12, 16, 24, 32, 48):
        k = 2*np.pi/p
        print(f"m={m} p={p} k={k:.4f}  A_cos(k) [perturbation theory] = {A_tt(m,k):.6f}")
