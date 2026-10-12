"""Whole-zone v_max (S17 rule) for the BQ laws used: R8-5 boxes at r = 1, the tuned L = 0 law, heavy-edge r = 32 (m = 0.1, 1)."""
import sys; sys.path.insert(0, '.')
import numpy as np
from r161_laws import BQLaw
from r85_box_qed_copy import deriv
k = (np.arange(96) + 0.5) * 2 * np.pi / 96 - np.pi; k1 = np.linspace(-np.pi, np.pi, 20001)
for lab, b1, b2, r in (('S1', 1.0, 2.0, 1.0), ('S2', 1.5, 2.5, 1.0), ('S3', 2.0, 3.0, 1.0), ('S5', 0.5, 1.5, 1.0), ('S7', 1.0, 3.0, 1.0), ('S8', 2.5, 3.1, 1.0),
                       ('tuned b1*=1.7514', 1.7513769123, 2.7513769123, 1.0), ('S3 r=32', 2.0, 3.0, 32.0)):
    out = []
    for m in (0.1, 1.0):
        law = BQLaw(b1, b2, r, m)
        S, W, dS, dW = law.S(k), law.W(k), deriv(law.S, k), deriv(law.W, k); best = 0.0
        for a in range(96):
            M = m + W[a] + W[:, None] + W[None, :]; E = np.sqrt(M ** 2 + S[a] ** 2 + S[:, None] ** 2 + S[None, :] ** 2)
            gx = (M * dW[a] + S[a] * dS[a]) / E; gy = (M * dW[:, None] + (S * dS)[:, None]) / E; gz = (M * dW[None, :] + (S * dS)[None, :]) / E
            best = max(best, np.sqrt(gx ** 2 + gy ** 2 + gz ** 2).max())
        S1, W1, dS1, dW1 = law.S(k1), law.W(k1), deriv(law.S, k1), deriv(law.W, k1)
        for n in (1, 2, 3):
            M = m + n * W1; E = np.sqrt(M ** 2 + n * S1 ** 2); best = max(best, np.max(np.sqrt(n) * np.abs(M * dW1 + S1 * dS1) / E))
        out.append(best)
    print('BQ %-18s (b1=%.4f, r=%.0f): v_max(m=0.1) = %.3f, v_max(m=1) = %.3f' % (lab, b1, r, *out), flush=True)
