"""C5 s5: W3 of generic finite-range unitaries found by solving the unitarity equations directly.

No product or Clifford structure is imposed: coefficients A_n (n in {-r..r}^3, n x n complex) are
driven by Levenberg-Marquardt to U U^dag = 1 on an exact (4r+1)^3 grid (U U^dag - 1 has degree <= 2r,
so vanishing there means vanishing identically, up to the solver residual). A soft anchor pulls the
walk toward a random non-unitary Laurent matrix in the first stage so that solutions are moving
(non-constant); the anchor is then removed. W3 is evaluated with the exact grid N = 6r+2 using the
inverse U^{-1} by matrix inversion (not U^dag), plus a second grid for consistency.
"""
import itertools
import sys
import numpy as np
from scipy.optimize import least_squares
from w3lib import Checker, w3_from_fields

ck = Checker()
rng = np.random.default_rng(99)

def hops(r):
    return np.array(list(itertools.product(range(-r, r + 1), repeat=3)))

def run(n, r, seed_scale, anchor_w):
    H = hops(r); nh = len(H)
    Nu = 4 * r + 1
    ku = 2 * np.pi * np.array(list(itertools.product(range(Nu), repeat=3))) / Nu
    Cu = np.exp(1j * ku @ H.T)
    target = rng.normal(size=(nh, n, n)) + 1j * rng.normal(size=(nh, n, n))
    target *= seed_scale
    target[nh // 2] += np.eye(n)
    def unpack(p):
        return (p[:nh * n * n] + 1j * p[nh * n * n:]).reshape(nh, n, n)
    def res(p, aw):
        A = unpack(p)
        U = np.einsum('kn,nij->kij', Cu, A)
        R = (U @ np.conj(np.swapaxes(U, 1, 2)) - np.eye(n)).ravel()
        out = [R.real, R.imag]
        if aw > 0:
            D = (A - target).ravel() * aw
            out += [D.real, D.imag]
        return np.concatenate(out)
    p = np.concatenate([target.real.ravel(), target.imag.ravel()])
    for aw in (anchor_w, anchor_w / 10, 0.0):
        p = least_squares(res, p, args=(aw,), method='trf', max_nfev=400, xtol=1e-15, ftol=1e-15, gtol=1e-15).x
    A = unpack(p)
    K = rng.uniform(0, 2 * np.pi, (2000, 3))
    U = np.einsum('kn,nij->kij', np.exp(1j * K @ H.T), A)
    uerr = np.abs(U @ np.conj(np.swapaxes(U, 1, 2)) - np.eye(n)).max()
    # motion: spread of U(k) over the torus (0 for a constant walk)
    motion = np.linalg.norm(U - U.mean(0), axis=(1, 2)).max()
    ws = []
    for N in (6 * r + 2, 6 * r + 5):
        k = 2 * np.pi * np.arange(N) / N
        KK = np.array(list(itertools.product(k, k, k)))
        C = np.exp(1j * KK @ H.T)
        Ug = np.einsum('kn,nij->kij', C, A).reshape(N, N, N, n, n)
        dU = [np.einsum('kn,nij->kij', C * (1j * H[:, b])[None, :], A).reshape(N, N, N, n, n) for b in range(3)]
        ws.append(w3_from_fields(Ug, dU, unitary=False))
    # number of hop matrices with significant weight, and the k-dependence along all three axes
    sig = int((np.abs(A).reshape(nh, -1).max(1) > 1e-6).sum())
    return uerr, motion, ws, sig

for n, r, trials in ((2, 1, 4), (4, 1, 2)):   # run 1 (log s5_run1_stopped_in_r2_trial.log) stalled in the r=2 finite-difference solve; r=2 dropped
    for t in range(trials):
        uerr, motion, ws, sig = run(n, r, 0.15, 0.3)
        line = (f'n={n} r={r} trial {t}: unit.err {uerr:.1e}, motion {motion:.3f}, {sig} nonzero hops, '
                f'W3 = {ws[0].real:+.2e} (N={6*r+2}), {ws[1].real:+.2e} (N={6*r+5})')
        print(line, flush=True)
        if uerr < 1e-9 and motion > 0.1:
            ck.check(f'n={n} r={r} trial {t}: moving unitary walk (no structure imposed) has W3 = 0', abs(ws[0]) < 1e-6 and abs(ws[1]) < 1e-6)
        else:
            print('   (solver did not reach a moving unitary walk; no check recorded)')
sys.exit(ck.total())
