"""D1 whole-zone v_max with analytic s', W' (no finite differences): axis lines n = 1, 2, 3 (k,..,k) and a 96^3 grid."""
import sys; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law
for b in (1.4, 1.2, 1.0):
    out = []
    for m in (0.1, 0.3, 1.0):
        law = D1Law(b, 1 / np.sqrt(3), m)
        k1 = np.linspace(-np.pi, np.pi, 200001); S1, dS1 = law.S(k1), law.A.ds(k1); W1, dW1 = law.W(k1), law.dW(k1)
        best = 0.0; where = None
        for n in (1, 2, 3):
            M = m + n * W1; E = np.sqrt(M ** 2 + n * S1 ** 2); v = np.sqrt(n) * np.abs(M * dW1 + S1 * dS1) / E
            if v.max() > best: best, where = v.max(), (n, k1[np.argmax(v)])
        k = (np.arange(96) + 0.5) * 2 * np.pi / 96 - np.pi
        S, dS, W, dW = law.S(k), law.A.ds(k), law.W(k), law.dW(k); g = 0.0
        for a in range(96):
            M = m + W[a] + W[:, None] + W[None, :]; E = np.sqrt(M ** 2 + S[a] ** 2 + S[:, None] ** 2 + S[None, :] ** 2)
            gx = (M * dW[a] + S[a] * dS[a]) / E; gy = (M * dW[:, None] + (S * dS)[:, None]) / E; gz = (M * dW[None, :] + (S * dS)[None, :]) / E
            g = max(g, np.sqrt(gx ** 2 + gy ** 2 + gz ** 2).max())
        out.append('m=%.1f: lines %.6f (n=%d, k=%.4f), grid %.6f' % (m, best, where[0], where[1], g))
    print('D1(b=%.1f, 1/sqrt3): ' % b + ' | '.join(out), flush=True)
