#!/usr/bin/env python3
"""A15: probe self-timed defects. (a) A10 2D word: a plaquette with offsets (0,2,0,2) = a 4-site waiting cycle;
(b) random phase fields: deadlock frequency for A10 2D/3D and A11 2D; (c) fate of a single out-of-phase site
(A10 2D, L=32): size of the set whose beat differs from the majority, vs round."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from selftimed_words import make, selftimed
import selftimed2d as a11

W2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
W3 = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
# (a) waiting cycle on one plaquette, A10 2D word
L = 16; coords, _ = make(W2, L, 2); n = L * L
phi = np.zeros(n, int)
idx = lambda x, y: x * L + y
x0 = y0 = 8          # a=(8,8) xe names b=(9,8); b ye names c=(9,9); c xe names d=(8,9); d ye names a
phi[idx(x0 + 1, y0)] = 2; phi[idx(x0, y0 + 1)] = 2
c, last, fpr = selftimed(W2, L, 2, phi, 300)
print("(a) A10 2D, plaquette offsets (0,2,0,2): deadlock=%s, stuck=%d/%d, first round with zero firings=%s"
      % (fpr[-1] == 0, int((last < 288).sum()), n, next((r for r, f in enumerate(fpr) if f == 0), None)))
# (b) random phase fields
rng = np.random.default_rng(20261002)
for name, word, d, L in (("A10 2D", W2, 2, 16), ("A10 3D", W3, 3, 8)):
    p = len(word); n = L ** d
    dl = 0
    for trial in range(40):
        phi = rng.integers(0, p, n)
        c, last, fpr = selftimed(word, L, d, phi, 200)
        dl += fpr[-1] == 0
    print("(b) %s random offsets: deadlocked in %d/40 runs (200 rounds)" % (name, dl))
    # sparse randomness: each site out of phase with probability 0.02
    dl = 0
    for trial in range(40):
        phi = np.where(rng.random(n) < 0.02, rng.integers(1, p, n), 0)
        c, last, fpr = selftimed(word, L, d, phi, 200)
        dl += fpr[-1] == 0
    print("    %s sparse offsets (2%% of sites): deadlocked in %d/40 runs" % (name, dl))
dl = 0
for trial in range(40):
    phi = rng.integers(0, 4, (16, 16))
    c, lf, fpr, jf, _ = a11.run(16, phi, 200)
    dl += fpr[-1] == 0
print("(b) A11 2D random offsets: deadlocked in %d/40 runs" % dl)
# (c) single out-of-phase site, A10 2D, L=32: spread of the mismatch set
L = 32; n = L * L; coords, part = make(W2, L, 2)
for k in (1, 2, 3):
    phi = np.zeros(n, int); phi[idx(16, 16) if False else 16 * L + 16] = k
    sizes = {}
    c = np.zeros(n, int); ar = np.arange(n)
    for r in range(121):
        j = (c + phi) % 4
        sel = part[j, ar]
        ready = sel[sel] == ar
        c[ready] += 1
        if r in (0, 5, 10, 20, 40, 80, 120):
            beat = (c + phi) % 4
            vals, cnts = np.unique(beat, return_counts=True)
            maj = vals[np.argmax(cnts)]
            off = np.where(beat != maj)[0]
            if off.size:
                dx = np.abs(((coords[off, 0] - 16 + L // 2) % L) - L // 2); dy = np.abs(((coords[off, 1] - 16 + L // 2) % L) - L // 2)
                sizes[r] = (int(off.size), int(max(dx.max(), dy.max())))
            else:
                sizes[r] = (0, 0)
    print("(c) A10 2D single site offset %d: (number off-beat, max distance) by round:" % k, sizes)
