# GUIDE recheck for vg_lens.py: the case (m, b, c) = (1, 3, 3) and (1, 6, 3) by eigenvalue log-determinants
# (symmetric positive definite matrices), against slogdet; prints any FP warnings as errors.
import warnings, numpy as np, sys
sys.path.insert(0, '.')
warnings.simplefilter('error')
import vg_lens as V
def logdet_eig(A):
    w = np.linalg.eigvalsh(0.5 * (A + A.T)); assert w.min() > 0, w.min(); return np.sum(np.log(w))
for (m, b, c) in [(1.0, 3, 3), (1.0, 6, 3), (0.5, 8, 4)]:
    hL = b + 1
    WL = V.W_of(V.lap_K((hL, c, c), m)); Ws = V.W_of(V.lap_K((b, c, c), m))
    keep = [p for p in range(hL) if p != 1]
    kept = np.arange(hL * c * c).reshape(hL, c, c)[keep].ravel()
    WM = 0.5 * np.linalg.inv(np.linalg.inv(2 * WL)[np.ix_(kept, kept)])
    lo_eig = 0.5 * (logdet_eig(Ws) + logdet_eig(WM)) - logdet_eig(0.5 * (Ws + WM))
    try:
        lo_sl = V.overlap2(b, c, m, [1]); note = ''
    except Exception as ex:
        lo_sl = float('nan'); note = 'slogdet path raised: %r' % ex
    print(m, b, c, 'eig:', -lo_eig, 'slogdet:', -lo_sl, note)
