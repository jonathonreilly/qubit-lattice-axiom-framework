#!/usr/bin/env python3
"""A15 task 3 (1D): event-paced local beats for the A10 cycle, one excitation, supplied toy.
Each round every site independently has a local record event with odds q (stand-in for A8's arrivals).
 E1 (wait): a pair fires when both sites name each other and both have had an event since their last firing;
     firing advances both counters (self-timed, event-gated).
 E2 (slip): an event advances the site's own counter; a pair acts when both name each other and at least one
     of them had an event this round (handshake H on rigid-but-irregular clocks).
Measured: spread <x^2> of the excitation (history-averaged weight), against rounds; ballistic ~ t^2, diffusive ~ t."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np

def sel(N, c):
    x = np.arange(N)
    right = (c % 2) == (x % 2)
    s = np.where(right, x + 1, x - 1) % N
    return s

def run(mode, q, th, N=401, R=160, runs=60, seed=7):
    rng = np.random.default_rng(seed)
    cth, sth = np.cos(th), np.sin(th)
    u = np.exp(1j * th) * np.array([[cth, -1j * sth], [-1j * sth, cth]])
    x = np.arange(N); x0 = N // 2
    msd = np.zeros(R)
    for _ in range(runs):
        psi = np.zeros(N, complex); psi[x0] = 1.0
        c = np.zeros(N, int)
        fresh = np.zeros(N, bool)
        for r in range(R):
            ev = rng.random(N) < q
            if mode == 'E2':
                c = c + ev
            s = sel(N, c)
            mutual = (s[s] == x)
            if mode == 'E1':
                fresh |= ev
                act = mutual & fresh & fresh[s]
            else:
                act = mutual & (ev | ev[s])
            a = x[act & (x < s) & ~((x == N - 1) & (s == 0))]
            b = s[a]
            pa, pb = psi[a].copy(), psi[b].copy()
            psi[a] = u[0, 0] * pa + u[0, 1] * pb
            psi[b] = u[1, 0] * pa + u[1, 1] * pb
            if mode == 'E1':
                fired = np.zeros(N, bool); fired[a] = True; fired[b] = True
                c = c + fired
                fresh &= ~fired
            msd[r] += np.sum(np.abs(psi) ** 2 * (x - x0) ** 2)
    return msd / runs

for th in (np.pi / 2, np.pi / 4):
    for q in (1.0, 0.5, 0.2):
        for mode in ('E1', 'E2'):
            m = run(mode, q, th)
            t1, t2 = 79, 159
            exp = np.log(m[t2] / m[t1]) / np.log((t2 + 1) / (t1 + 1))
            print("theta=%.3f q=%.1f %s: <x^2> at r=80: %8.1f, r=160: %8.1f, growth exponent %.2f (2 ballistic, 1 diffusive)"
                  % (th, q, mode, m[t1], m[t2], exp))
