"""BLEAK-1 main computation: one-graviton-loop speed row of a massless scalar on Z^4 (a = 1, G in lattice units).

Sigma(p) = -32 pi G p_a p_b int_k D_k(U^a, U^b)/shat(k)^2 + O(p^4)   (m = 0; derivation in REPORT.md sec. 3)
dZ_a = -32 pi G I_a,  I_a = int_BZ d^4k/(2pi)^4 D_k(U^a,U^a)/shat^2   (= mean over the BZ)
delta c = (dZ_s - dZ_4)/2 = -16 pi G (I_1 - I_4).
U^a is identical for K2 and D2 (D2's extra vertex is O(p1^2)), so cases C1 = M1 and C0 = M2 at this order;
the D2 identity is checked separately at finite p in b1_finite_p.py.
Integrands are even in each k_mu (b1_checks.out (iv)), so the integral is taken over [0,pi]^4 with M = N/2 midpoints per axis.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from b1_core import shat, U_alpha, kernel_parts, iter_chunks

def integrals(M):
    acc = {key: 0.0 for key in ('GR1', 'GR4', 'TT1', 'TT4', 'inst1', 'inst4', 'GR2')}
    cnt = 0
    for k in iter_chunks(M, chunk=1 << 15):   # 2^15 after the 443 MB run with 2^17
        S2 = np.sum(shat(k) ** 2, 0)
        for a, tag in ((0, '1'), (3, '4'), (1, '2')):
            U = U_alpha(k, a)
            WTT, Wi, WGR = kernel_parts(U, U, k)
            acc['GR' + tag] += np.sum(WGR / S2)
            if tag != '2':
                acc['TT' + tag] += np.sum(WTT / S2)
                acc['inst' + tag] += np.sum(Wi / S2)
        cnt += k.shape[1]
    return {key: v / cnt for key, v in acc.items()}

if __name__ == '__main__':
    Ms = [int(x) for x in sys.argv[1:]] or [6, 8, 12, 16, 24, 32, 48]
    rows = []
    print("M(=N/2)  I_GR(1)        I_GR(4)        I_GR(2)        I_TT(1)        I_TT(4)        I_inst(1)      I_inst(4)      sec")
    for M in Ms:
        t0 = time.time()
        r = integrals(M)
        rows.append((M, r))
        print("%4d  %14.10f %14.10f %14.10f %14.10f %14.10f %14.10f %14.10f %6.1f" % (
            M, r['GR1'], r['GR4'], r['GR2'], r['TT1'], r['TT4'], r['inst1'], r['inst4'], time.time() - t0), flush=True)
    print("\nper grid: covariant (C0=M2) row  I_GR(1)-I_GR(4);   foliated (C1=M1) row  I_fol(1)-I_fol(4), I_fol = I_TT + I_inst")
    for M, r in rows:
        dGR = r['GR1'] - r['GR4']
        f1 = r['TT1'] + r['inst1']; f4 = r['TT4'] + r['inst4']
        print("  N=%4d  dI_GR = %+.3e   I_fol(1)=%.8f I_fol(4)=%.8f  dI_fol = %+.8f   delta c(fol) = -16 pi dI = %+.6f" % (
            2 * M, dGR, f1, f4, f1 - f4, -16 * np.pi * (f1 - f4)))
    np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'b1_row_raw_%s.npy' % '_'.join(map(str, Ms))),
            np.array([[M, r['GR1'], r['GR4'], r['GR2'], r['TT1'], r['TT4'], r['inst1'], r['inst4']] for M, r in rows]))
