"""BLEAK-1 independent check: direct one-loop Sigma(p) at finite p with the FULL vertices (K2 and D2), both kernels.

Sigma(p) = -32 pi G int_k D_k(V(-p, p-k), V(p, k-p)) G(p-k), m = 0, a = 1, G = 1.
Substitute k = p + k' (k' on the midpoint grid of [-pi,pi]^4, which avoids k' = 0 and the bridge's q = 0 line for p along
e_1 or e_4). Then V(-p, p-k) = V(-p, -k'), V(p, k-p) = V(p, k'), G(p-k) = G(k'), kernel at k = k' + p.
Report Z_a(delta) = Sigma(delta e_a)/delta^2 and the row (Z_1 - Z_4)/2, to compare with the closed form:
  covariant: Z_1 = Z_4 = -32 pi I_GR;  foliated: Z_a = -32 pi I_inst(a); row = pi/6 = 0.5236 (foliated), 0 (covariant).
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from b1_core import shat, vertex, kernel_parts, iter_chunks

def sigma(pvec, N):
    p = np.asarray(pvec, float)[:, None]
    acc = np.zeros(4)   # [K2-GR, K2-fol, D2-GR, D2-fol]
    n = 0
    for kp in iter_chunks(N, chunk=1 << 15, lo=-np.pi, hi=np.pi):
        k = kp + p
        Gk = 1.0 / np.sum(shat(kp) ** 2, 0)
        pm = np.broadcast_to(-p, kp.shape); pp = np.broadcast_to(p, kp.shape)
        for j, d2 in enumerate((False, True)):
            Va = vertex(pm, -kp, 0.0, d2); Vb = vertex(pp, kp, 0.0, d2)
            WTT, Wi, WGR = kernel_parts(Va, Vb, k)
            acc[2 * j] += np.sum(WGR * Gk); acc[2 * j + 1] += np.sum((WTT + Wi) * Gk)
        n += kp.shape[1]
    return -32 * np.pi * acc / n

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    deltas = [float(x) for x in sys.argv[2:]] or [0.2, 0.1]
    print("N = %d (full BZ midpoint, N^4 = %d points)" % (N, N ** 4))
    print("Sigma(0) (all four cases):", sigma([0, 0, 0, 0], max(8, N // 4)))
    tags = ['K2-GR (C0)', 'K2-fol (C1)', 'D2-GR (M2)', 'D2-fol (M1)']
    for d in deltas:
        t0 = time.time()
        s1 = sigma([d, 0, 0, 0], N); s4 = sigma([0, 0, 0, d], N)
        print("delta = %.3f  (%.0f s)" % (d, time.time() - t0))
        for i, t in enumerate(tags):
            Z1, Z4 = s1[i] / d ** 2, s4[i] / d ** 2
            print("   %-12s Z_s = %+.6f  Z_4 = %+.6f  row (Z_s - Z_4)/2 = %+.6f" % (t, Z1, Z4, 0.5 * (Z1 - Z4)), flush=True)
    print("closed form: foliated row pi/6 = %.6f ; covariant row 0 ; Z_GR = -32 pi * 0.046216 = %.4f ;"
          " foliated Z_s = -32 pi * 0.0223451 = %.4f, Z_4 = -32 pi * 0.0327617 = %.4f" % (
              np.pi / 6, -32 * np.pi * 0.046216, -32 * np.pi * 0.0223451, -32 * np.pi * 0.0327617))
