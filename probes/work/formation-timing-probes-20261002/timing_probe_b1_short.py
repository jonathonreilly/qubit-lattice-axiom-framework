#!/usr/bin/env python3
"""PROBE B1' (exact): the same distance test as B1, but from a preparation whose shared possibilities link each site to
one partner only (equal mixture of the two singlet-pair coverings of the ring).  This preparation changes from the
start, so both schedules end at the same moment g:
   at once:   nothing forms until g, then sites 0 and d form together;
   0 early:   site 0 forms at 0, the change runs for g with 0 locked (pushing), then d forms at g.
Fixed z menus.  usage: python3 timing_probe_b1_short.py"""
import numpy as np
from scipy.sparse.linalg import expm_multiply
from timing_probes import Ring, Z, tv, corr


def covering_state(N, shift):
    pairs = [((2 * k + shift) % N, (2 * k + 1 + shift) % N) for k in range(N // 2)]
    psi = np.zeros(2 ** N, dtype=complex)
    for idx in range(2 ** N):
        c = [(idx >> (N - 1 - j)) & 1 for j in range(N)]
        amp = 1.0
        for a, b in pairs:
            if c[a] == c[b]:
                amp = 0.0
                break
            amp *= (1 if c[a] == 0 else -1) / np.sqrt(2)
        psi[idx] = amp
    return psi / np.linalg.norm(psi)


def joint_times(R, prep, i, k, ti, tk, push=True):
    P = {}
    if ti == tk:
        v0 = expm_multiply(-1j * ti * R.H0, prep) if ti > 0 else prep
        for a in (1, -1):
            v = R.project(v0, i, Z, a)
            for b in (1, -1):
                w = R.project(v, k, Z, b)
                P[(a, b)] = float(np.vdot(w, w).real)
        return P
    (x, tx), (y, ty) = sorted([(i, ti), (k, tk)], key=lambda z: z[1])
    v0 = expm_multiply(-1j * tx * R.H0, prep) if tx > 0 else prep
    for a in (1, -1):
        v = R.project(v0, x, Z, a)
        pa = float(np.vdot(v, v).real)
        v = R.evolve(v / np.sqrt(pa), {x: a * Z}, ty - tx, push)
        for b in (1, -1):
            w = R.project(v, y, Z, b)
            P[(a, b) if x == i else (b, a)] = pa * float(np.vdot(w, w).real)
    return P


def avg(Ps):
    return {key: float(np.mean([P[key] for P in Ps])) for key in Ps[0]}


if __name__ == "__main__":
    N = 12
    R = Ring(N)
    preps = [covering_state(N, 0), covering_state(N, 1)]
    print("=== PROBE B1' (exact): timing vs distance from a preparation with partner-only links, N = %d ring ===" % N)
    for d in range(1, 7):
        line = "d=%d" % d
        for g in (0.05, 0.1, 0.2, 0.3, 0.5, 1.0):
            Ponce = avg([joint_times(R, s, 0, d, g, g) for s in preps])
            Pearly = avg([joint_times(R, s, 0, d, 0.0, g) for s in preps])
            line += "  g=%.2f: TV %.5f (corr once %+.3f, early %+.3f)" % (g, tv(Pearly, Ponce), corr(Ponce), corr(Pearly))
        print(line, flush=True)
