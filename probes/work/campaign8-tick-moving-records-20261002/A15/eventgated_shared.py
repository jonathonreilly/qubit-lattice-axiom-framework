#!/usr/bin/env python3
"""A15: E3 = one shared beat (no phase mismatch); on each sub-step a pair in the current layer applies its gate
only if a record event occurred at one of its two sites (odds q each), else nothing. History-averaged spread of one
excitation (A10 1D cycle). Compare growth exponents with E1/E2 (eventpaced1d.py)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
def run(q, th, N=401, R=320, runs=60, seed=11):
    rng = np.random.default_rng(seed)
    c, s = np.cos(th), np.sin(th)
    x = np.arange(N); x0 = N // 2
    msd = np.zeros(R)
    for _ in range(runs):
        psi = np.zeros(N, complex); psi[x0] = 1
        for t in range(R):
            A = np.arange(t % 2, N - 1, 2); B = A + 1
            ev = rng.random(N) < q
            act = ev[A] | ev[B]
            A, B = A[act], B[act]
            pa, pb = psi[A].copy(), psi[B].copy()
            ph = np.exp(1j * th)
            psi[A] = ph * (c * pa - 1j * s * pb)
            psi[B] = ph * (-1j * s * pa + c * pb)
            msd[t] += np.sum(np.abs(psi) ** 2 * (x - x0) ** 2)
    return msd / runs
for th in (np.pi / 2, np.pi / 4, 0.2):
    for q in (1.0, 0.5, 0.2):
        m = run(q, th)
        e1 = np.log(m[79] / m[39]) / np.log(2); e2 = np.log(m[319] / m[159]) / np.log(2)
        print("theta=%.3f q=%.1f: <x^2>(80)=%8.1f <x^2>(320)=%9.1f; exponent 40->80: %.2f, 160->320: %.2f" % (th, q, m[79], m[319], e1, e2))
