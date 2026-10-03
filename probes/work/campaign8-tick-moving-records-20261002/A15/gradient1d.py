#!/usr/bin/env python3
"""A15 task 2: smooth rate gradient under rigid local clocks + handshake (supplied 1D toy, A10 cycle, one excitation).
Site x advances its sub-step counter c(x) = floor(r(x) T) on a fine global time grid (dT); a pair acts once when it
becomes agreed (both name each other and one of them just advanced). r = 1 for x < a, falls linearly to 1/2 on
[a, b], r = 1/2 for x > b. Compared with a sharp commensurate 2:1 step (same as rate1d.py H-rate) and with no step.
Reported: transmitted weight past b of a packet sent from x < a, and the number of disagreeing bonds ('walls')
inside [a, b] at several times."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from seam1d import ublock, packet, branch

def run(profile, th=np.pi / 4, K0=np.pi - 0.4, N=900, a=400, b=500, dT=0.05, Tend=None):
    u = ublock(th)
    x = np.arange(N)
    if profile == 'flat':
        r = np.ones(N)
    elif profile == 'sharp':
        r = np.where(x < a, 1.0, 0.5)
    else:
        r = np.where(x < a, 1.0, np.where(x > b, 0.5, 1.0 - 0.5 * (x - a) / (b - a)))
    vg, _, _ = branch(K0, u, +1)
    psi = packet(N, a // 2 - 60, K0, 12.0, u, +1).astype(complex)
    psi[a:] = 0; psi /= np.linalg.norm(psi)
    if Tend is None:
        Tend = 2 * (60 + 60 + 50) / vg + 200
    nsteps = int(Tend / dT)
    c = np.zeros(N, int)
    walls = {}
    for n in range(1, nsteps + 1):
        T = n * dT
        cn = np.floor(r * T + 1e-9).astype(int)
        adv = cn != c
        c = cn
        if not adv.any():
            continue
        right = ((c - 1) % 2) == (x % 2)      # the sub-step just begun is c-1 (first one: even layer)
        s = np.where(right, x + 1, x - 1)
        s = np.clip(s, 0, N - 1)
        mutual = (s[s] == x) & (s != x)
        act = mutual & (adv | adv[s]) & (x < s)
        A = x[act]; B = s[act]
        pa, pb = psi[A].copy(), psi[B].copy()
        psi[A] = u[0, 0] * pa + u[0, 1] * pb
        psi[B] = u[1, 0] * pa + u[1, 1] * pb
        for tw in (20, 100, 300):
            if abs(T - tw) < dT / 2:
                walls[tw] = int(np.sum((c[a:b] % 2) != (c[a + 1:b + 1] % 2)))
    p = np.abs(psi) ** 2
    return p[b:].sum(), p[a:b].sum(), p[:a].sum(), walls, Tend

for prof in ('flat', 'sharp', 'smooth'):
    for th, K0 in ((np.pi / 2, np.pi / 2), (np.pi / 4, np.pi - 0.4)):
        tr, mid, rf, walls, Tend = run(prof, th, K0)
        print("%-6s theta=%.3f: past b %.4f | inside [a,b] %.4f | before a %.4f | disagreeing bonds in [a,b] at T=20,100,300: %s (T_end=%.0f)"
              % (prof, th, tr, mid, rf, walls, Tend))
