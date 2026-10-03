#!/usr/bin/env python3
"""A15 task 3/4 (2D): self-timed (handshake-wait) local beats for the A11 4-sub-step swap cycle, supplied toy.

Each site keeps a counter c (pair events it took part in); its next partner is fixed by j = c + phi (mod 4) as in
a11walls.py. A pair fires when both sites name each other, then both counters advance. No global clock: we draw
the history in as-soon-as-possible rounds (firing order does not change the history).
Initial offsets phi: (i) vertical strip at offset k; (ii) square island at offset k; (iii) a 4-site waiting cycle
(phase vortex) on one plaquette. Reported: deadlock (round with no firing), number of permanently stuck sites,
growth of the stuck region, and whether the beat becomes uniform ((c+phi) mod 4 the same everywhere)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np

D = np.array([(1, 0), (0, 1), (-1, 0), (0, -1)])

def run(L, phi, rounds, track=False):
    X, Y = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    sgn = np.where((X + Y) % 2 == 0, 1, -1)
    c = np.zeros((L, L), int)
    last_fire = -np.ones((L, L), int)
    fires_per_round = []
    stuck_hist = []
    for r in range(rounds):
        j = (c + phi) % 4
        px = (X + sgn * D[j, 0]) % L
        py = (Y + sgn * D[j, 1]) % L
        back_x = px[px, py]; back_y = py[px, py]
        ready = (back_x == X) & (back_y == Y)
        c[ready] += 1
        last_fire[ready] = r
        fires_per_round.append(int(ready.sum()))
        if track:
            stuck_hist.append(int((last_fire < r - 8).sum()) if r > 8 else 0)
    jf = (c + phi) % 4
    return c, last_fire, fires_per_round, jf, stuck_hist

def report(name, L, phi, rounds=400):
    c, lf, fpr, jf, sh = run(L, phi, rounds, track=True)
    never_after = int((lf < rounds - 20).sum())
    uniform = len(set(jf.ravel().tolist())) == 1
    late_rate = np.mean(fpr[-40:]) / (L * L)
    print("%-34s deadlock=%s  stuck sites at end=%4d/%d  late firing fraction=%.3f  uniform beat=%s  counters %d..%d"
          % (name, fpr[-1] == 0, never_after, L * L, late_rate, uniform, c.min(), c.max()))
    return sh

if __name__ == '__main__':
    L = 16
    print("== self-timed A11, torus L=16, 400 rounds ==")
    report("uniform (k=0)", L, np.zeros((L, L), int))
    for k in (1, 2, 3):
        phi = np.zeros((L, L), int); phi[4:12, :] = k
        report("vertical strip x in [4,12), k=%d" % k, L, phi)
        phi = np.zeros((L, L), int); phi[:, 4:12] = k
        report("horizontal strip y in [4,12), k=%d" % k, L, phi)
    L = 24
    for s in (1, 2, 4):
        for k in (1, 2, 3):
            phi = np.zeros((L, L), int); c0 = L // 2 - s // 2; phi[c0:c0 + s, c0:c0 + s] = k
            report("island s=%d k=%d (L=24)" % (s, k), L, phi)
    # phase vortex: plaquette a=(x0,y0) A-site phase 0, b=(x0+1,y0) phase 3, c=(x0+1,y0+1) phase 2, d=(x0,y0+1) phase 1
    L = 32
    phi = np.zeros((L, L), int); x0 = y0 = 16
    phi[x0 + 1, y0] = 3; phi[x0 + 1, y0 + 1] = 2; phi[x0, y0 + 1] = 1
    sh = report("vortex plaquette (L=32)", L, phi, rounds=200)
    print("   stuck-region size vs round (sites not fired for 8 rounds):", {r: sh[r] for r in (10, 20, 40, 60, 80, 100, 150, 199)})
    # radius of the stuck region: compare with light-cone growth
    c, lf, fpr, jf, _ = run(L, phi, 120)
    stuck = lf < 100
    xs, ys = np.where(stuck)
    if xs.size:
        dist = np.maximum(np.abs(((xs - x0 + L // 2) % L) - L // 2), np.abs(((ys - y0 + L // 2) % L) - L // 2))
        print("   at round 120: stuck sites=%d, max Chebyshev distance from vortex=%d" % (stuck.sum(), dist.max()))
