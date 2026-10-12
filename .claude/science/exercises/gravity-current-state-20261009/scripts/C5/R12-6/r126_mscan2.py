"""C5 R12-6, script 7: memory-sliced rerun of the matched-curve (Wilson e / cochain photino) unrepaired partner total
(= transverse piece T, since the dressing cancels for matched curves; script 3) at smaller m and larger N.
Same formulas as r126_electron_loops.dE_photino(mode='T'), evaluated slice by slice in q_x.  Units 16 pi^2/e^2."""
import numpy as np, sys, time
sys.path.insert(0, '.')
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import r126_electron_loops as L
from r101_pairing import wilson_curve
A, B, e, U = L.A, L.B, L.e, L.U16
t0 = time.time()
def dE_T(cur, m, p, N):
    k1 = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    QY, QZ = np.meshgrid(k1, k1, indexing='ij')
    pv = np.array([p, 0.0, 0.0])
    ev, Ve = np.linalg.eigh(L.Mmat(cur, pv, m)); Ep = ev[-1]
    v = lambda kk: cur['S'](kk) ** 2 + cur['W'](kk) ** 2
    tot = 0.0
    for qx in k1:
        q = [np.full_like(QY, qx), QY, QZ]
        D = [np.exp(1j * q[j]) - 1 for j in range(3)]
        w = np.sqrt(sum(np.abs(Dj) ** 2 for Dj in D))
        ks = [pv[j] - q[j] for j in range(3)]
        eps = np.sqrt(m * m + v(ks[0]) + v(ks[1]) + v(ks[2]))
        dS = [cur['S'](np.array(pv[j])) - cur['S'](ks[j]) for j in range(3)]
        dW = [cur['W'](np.array(pv[j])) - cur['W'](ks[j]) for j in range(3)]
        for s in range(4, 8):
            u = Ve[:, s]
            R = [1j * e * (dS[j][..., None] * (A[j] @ u) + dW[j][..., None] * (B[j] @ u)) / np.conj(D[j])[..., None] for j in range(3)]
            trAA = sum(np.sum(np.abs(R[j]) ** 2, axis=-1) for j in range(3))
            Lv = sum(np.conj(D[j])[..., None] * R[j] for j in range(3))
            S = 0.5 * (trAA - np.sum(np.abs(Lv) ** 2, axis=-1) / w ** 2)
            tot += np.sum((S / (Ep - w - eps) + S / (Ep + w + eps)) / (2 * eps))
    return Ep, tot / (4 * N ** 3)
def dcl(cur, m, N, hstep=0.02):
    E0, d0 = dE_T(cur, m, 0.0, N); vals = []
    for hh in (hstep, 2 * hstep):
        Ep, d = dE_T(cur, m, hh, N); vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    return ((4 * vals[0] - vals[1]) / 3) / 2
cur = wilson_curve()
print('check vs script 3/5 (m=0.1, N=64: -9.008):  %+8.3f' % (U * dcl(cur, 0.1, 64)), flush=True)
for m, N in [(0.1, 128), (0.05, 128), (0.05, 160)]:
    print('m=%.3f N=%3d : matched-curve unrepaired partner total %+8.3f   [%.0fs]' % (m, N, U * dcl(cur, m, N), time.time() - t0), flush=True)
for m, N in [(0.2, 96), (0.025, 224), (0.025, 256)]:
    print('m=%.3f N=%3d : matched-curve unrepaired partner total %+8.3f   [%.0fs]' % (m, N, U * dcl(cur, m, N), time.time() - t0), flush=True)
