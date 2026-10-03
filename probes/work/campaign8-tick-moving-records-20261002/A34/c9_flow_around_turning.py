"""A34 c9: A37's untested 'turning' case -- what does flow-around (the only tidy push on the full grid) do to a
record whose stepping odds favour excitations?  (classical decohered toy, 2D; own code)

Lattice 64x64 torus, a gas of excitations at density 0.3 (at most one per site), one record. Each tick the record
steps to a neighbour y with odds proportional to (beta + (alpha - beta) * occupied(y)); alpha=1, beta=0.1
("odds favour excitations").  Post-step rules for the possibilities (A37's names):
  SW  : y's content goes to x (swap);
  PL1 : y's content goes to y+e, and y+e's content jumps back to x (capped line push);
  PSr : flow around with a random side f (perpendicular to e): y -> y+f -> x+f -> x;
  PSl : flow around, always the left side (2D handed rule; covariant under proper turns in 2D).
Excitations otherwise frozen (no smooth change), as in A37's 'frozen background' one-step rule.
Measured: distribution of the turn between consecutive steps (same / left / right / back), mean squared
displacement after 400 ticks, and net rotation (sum of signed quarter turns) per tick.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import signal
import numpy as np
signal.alarm(28)
rng = np.random.default_rng(17)
L, dens, alpha, beta, T, RUNS = 64, 0.3, 1.0, 0.1, 400, 150
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]          # index d; left of d is (d+1)%4, right is (d+3)%4

def run(rule):
    occ = (rng.random((L, L)) < dens)
    x = (0, 0); occ[x] = False                       # the record's site holds no possibility
    pos = np.array([0, 0]); prev = None
    turns = {"same": 0, "left": 0, "right": 0, "back": 0}; rot = 0
    for _ in range(T):
        w = []
        for d, (dx, dy) in enumerate(DIRS):
            y = ((x[0] + dx) % L, (x[1] + dy) % L)
            w.append(beta + (alpha - beta) * occ[y])
        w = np.array(w); d = int(rng.choice(4, p=w / w.sum()))
        e = DIRS[d]; y = ((x[0] + e[0]) % L, (x[1] + e[1]) % L)
        cy = occ[y]
        if rule == "SW":
            occ[x] = cy
        elif rule == "PL1":
            y2 = ((y[0] + e[0]) % L, (y[1] + e[1]) % L)
            occ[x] = occ[y2]; occ[y2] = cy
        else:
            fi = (d + 1) % 4 if (rule == "PSl" or rng.random() < 0.5) else (d + 3) % 4
            f = DIRS[fi]
            yf = ((y[0] + f[0]) % L, (y[1] + f[1]) % L); xf = ((x[0] + f[0]) % L, (x[1] + f[1]) % L)
            occ[x] = occ[xf]; occ[xf] = occ[yf]; occ[yf] = cy
        occ[y] = False
        if prev is not None:
            k = (d - prev) % 4
            name = ["same", "left", "back", "right"][k]
            turns[name] += 1
            rot += {0: 0, 1: 1, 2: 0, 3: -1}[k]
        prev = d; x = y; pos += np.array(e)
    return turns, float(pos @ pos), rot / T

for rule in ("SW", "PL1", "PSr", "PSl"):
    tot = {"same": 0, "left": 0, "right": 0, "back": 0}; msd = []; rots = []
    for _ in range(RUNS):
        t, m, r = run(rule)
        for k in tot:
            tot[k] += t[k]
        msd.append(m); rots.append(r)
    n = sum(tot.values())
    print(f"{rule:4s}: p(same) {tot['same']/n:.3f}  p(left) {tot['left']/n:.3f}  p(right) {tot['right']/n:.3f}  "
          f"p(back) {tot['back']/n:.3f}  | MSD after {T} ticks {np.mean(msd):8.1f}  | net quarter-turns per tick {np.mean(rots):+.3f}")
print("(random-walk reference: p = 0.25 each; MSD = 400 for unit steps)")
