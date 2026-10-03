#!/usr/bin/env python3
"""A18: one-site staggered phase mass with A10's PLAIN 1D word (even, odd) vs the TIME-SYMMETRIC word.
Check cos(omega) = cos(mu) cos^2(theta) - sin^2(theta) cos(K + mu) for the plain word (hand derivation),
and locate the upper-band minimum for both words (supplied toy)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
def G(th): return np.array([[np.cos(th), -1j*np.sin(th)], [-1j*np.sin(th), np.cos(th)]])
def O(th, K): return np.array([[np.cos(th), -1j*np.sin(th)*np.exp(-1j*K)], [-1j*np.sin(th)*np.exp(1j*K), np.cos(th)]])
def Mh(mu): return np.diag([np.exp(-0.5j*mu), np.exp(0.5j*mu)])
th, mu = 0.3, 0.05
Ks = np.pi + np.linspace(-0.2, 0.2, 40001)
err, up_plain, up_sym = 0.0, [], []
for K in Ks:
    Up = Mh(mu) @ O(th, K) @ G(th) @ Mh(mu)
    Us = Mh(mu) @ G(th/2) @ O(th, K) @ G(th/2) @ Mh(mu)
    w = -np.angle(np.linalg.eigvals(Up)); up_plain.append(w.max())
    err = max(err, abs(np.cos(w[0]) - (np.cos(mu)*np.cos(th)**2 - np.sin(th)**2*np.cos(K + mu))))
    up_sym.append((-np.angle(np.linalg.eigvals(Us))).max())
i, j = np.argmin(up_plain), np.argmin(up_sym)
print("plain word: max |cos(omega) - formula| = %.2e; band minimum at K - pi = %+.5f (formula: -mu = %+.5f), omega_min = %.6f"
      % (err, Ks[i] - np.pi, -mu, up_plain[i]))
print("time-symmetric word: band minimum at K - pi = %+.5f, omega_min = %.6f (= mu)" % (Ks[j] - np.pi, up_sym[j]))
