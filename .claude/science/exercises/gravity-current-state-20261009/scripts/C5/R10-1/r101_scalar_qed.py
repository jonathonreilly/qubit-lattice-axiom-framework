"""R10-1 check 2: scalar QED (charged complex scalar, Peierls/Ward-forced vertex) photon speed shift.

Separable band eps^2 = m^2 + sum_j u(k_j) (R9-9 profiles G, L, NN). Transverse photon (q along x, current y):
vertex = u'(k_y) exactly for q_y = 0 (Peierls, axis paths); seagull = u''(k_y) (q-independent at q_y = 0).
Normalization as R8-5 (per e^2, mean over the BZ grid, times 16 pi^2):
   P_E = (1/16) < u'(k_y)^2 / eps^5 >        (= (1/4)<(d_y eps)^2/eps^3>; continuum ratio to Dirac 1:4)
   P_M = [chi(0) - chi(q)]/q^2,  chi(q) = < u'(k_y)^2 /(2 eps eps' (eps + eps')) >,  eps' = eps(k + q xhat)
   dc_gamma = (P_M - P_E)/2.
Claimed identity (Theorem T', proved in the report): dc_gamma = (1/32) < u'(k_y)^2 A_xx / eps^5 >,
A_xx = u''(k_x)/2 - 1.  Direct P_M uses exact shifts of the k_x grid (q = 2 pi n/N) and Richardson in q^2.
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r99_profiles_copy import profile

U = 16 * np.pi ** 2

def run(name, m, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    u, up, upp = profile(name, k)
    A = upp / 2 - 1
    KX, KY, KZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    e2 = m * m + u[KX] + u[KY] + u[KZ]
    eps = np.sqrt(e2)
    w = up[KY] ** 2
    PE = np.mean(w / eps ** 5) / 16
    mom = np.mean(w * A[KX] / eps ** 5) / 32
    chi0 = np.mean(w / (4 * eps ** 3))
    PMs = []
    for n in (1, 2, 4):
        q = 2 * np.pi * n / N
        ep = np.sqrt(m * m + u[(KX + n) % N] + u[KY] + u[KZ])
        chiq = np.mean(w / (2 * eps * ep * (eps + ep)))
        PMs.append(((chi0 - chiq) / q ** 2, q))
    # Richardson in q^2 using n = 1, 2 and 2, 4
    r1 = (4 * PMs[0][0] - PMs[1][0]) / 3; r2 = (4 * PMs[1][0] - PMs[2][0]) / 3
    PM = (16 * r1 - r2) / 15
    return dict(PE=PE, PM=PM, direct=(PM - PE) / 2, mom=mom)

if __name__ == '__main__':
    t0 = time.time()
    print('scalar QED photon: direct (P_M - P_E)/2 vs moment (1/32)<u_y\'^2 A_xx/eps^5>, both x 16 pi^2')
    print('profile | m | N | P_E | P_M | direct | moment | direct - moment | sign of A on zone')
    for name in ('G', 'L', 'NN'):
        kk = (np.arange(4096) + 0.5) * 2 * np.pi / 4096 - np.pi
        _, _, uppk = profile(name, kk)
        Ak = uppk / 2 - 1
        for m, N in [(1.0, 64), (1.0, 96), (0.3, 96), (0.3, 128), (0.05, 128)]:
            r = run(name, m, N)
            print('%-3s | %.2f | %3d | %+.5f | %+.5f | %+.6f | %+.6f | %+.1e | A in [%.2f, %.2f]' % (
                name, m, N, r['PE'] * U, r['PM'] * U, r['direct'] * U, r['mom'] * U,
                (r['direct'] - r['mom']) * U, Ak.min(), Ak.max()), flush=True)
    print('elapsed %.1fs' % (time.time() - t0))
