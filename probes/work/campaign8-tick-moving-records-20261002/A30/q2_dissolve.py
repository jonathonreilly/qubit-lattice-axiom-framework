"""A30 q2_dissolve: lifetime of a leaking jam under Option R steps (supplied classical toy).

Quiet surroundings, record content r = -n, emptiness |n>: then SW with content weight
W = beta + (alpha-beta)|r><r| acts on quiet sites with weight beta, and the record sector is
EXACTLY a classical exclusion process (the possibilities stay |n>^(x)).  Claim rule CL:
each empty site with recorded neighbours claims each of them with prob p = c*beta/z (at most
one claim per site); a record claimed by several picks one claimant uniformly; then swap.
No formation (quiet weight), so record number is conserved.
Measured: t_half = first tick at which fewer than half of the records sit inside the
initial ball/disc.  Diffusive dissolution predicts t_half ~ C R^2 / p.
Usage: python3 q2_dissolve.py DIM   (2 or 3)
"""
import signal
import sys
import numpy as np

signal.alarm(55)
d = int(sys.argv[1]) if len(sys.argv) > 1 else 2
p = 0.2 if d == 2 else 0.15          # claim prob per recorded neighbour (p*z <= 1)
N = 128 if d == 2 else 48
z = 2 * d
rng = np.random.default_rng(7)
dirs = []
for a in range(d):
    for s in (1, -1):
        v = [0] * d; v[a] = s; dirs.append(tuple(v))


def shift(arr, v):
    return np.roll(arr, shift=tuple(-x for x in v), axis=tuple(range(d)))   # value at x+v


def tick(rec):
    empty = ~rec
    nb = [shift(rec, v) for v in dirs]                 # nb[i][x] = rec at x+dirs[i]
    u = rng.random(rec.shape)
    # an empty site claims its i-th recorded neighbour (in fixed order among recorded ones)
    # with prob p each: draw u, the claim index = floor(u/p) among its recorded neighbours.
    nrec = sum(b.astype(np.int64) for b in nb)
    k = np.floor(u / p).astype(np.int64)
    claims = empty & (k < nrec)
    # map k -> direction index
    cnt = np.zeros(rec.shape, dtype=np.int64)
    target_dir = -np.ones(rec.shape, dtype=np.int64)
    for i, b in enumerate(nb):
        hit = claims & b & (cnt == k)
        target_dir[hit] = i
        cnt += b
    # each claim gets a random priority; a record keeps the claimant with the largest priority
    pri = rng.random(rec.shape)
    best = np.full(rec.shape, -1.0)
    # for each direction i, claimant at y targets record at y+dirs[i]; record sees claimant at x-dirs[i]
    for i, v in enumerate(dirs):
        c_i = (target_dir == i)
        pr = np.where(c_i, pri, -1.0)
        pr_at_rec = shift(pr, tuple(-x for x in v))     # value at x - v  (claimant y = x - v)
        best = np.maximum(best, pr_at_rec)
    winners = np.zeros(rec.shape, dtype=bool)          # claimant sites that win
    for i, v in enumerate(dirs):
        c_i = (target_dir == i)
        best_at_target = shift(best, v)                 # best at y+v
        winners |= c_i & (pri == best_at_target)
    # perform moves: record at y+dirs[i] -> y
    new = rec.copy()
    for i, v in enumerate(dirs):
        w = winners & (target_dir == i)
        new[w] = True
        src = shift(w, tuple(-x for x in v))            # site x = y + v is the source if w at y
        new[src] = False
    assert new.sum() == rec.sum()
    return new


idx = np.indices((N,) * d)
c = N // 2
r2 = sum((ii - c) ** 2 for ii in idx)
radii = [3, 4, 6, 8, 12, 16] if d == 2 else [2, 3, 4, 6, 8]
print(f"d={d} N={N} claim prob p={p}: t_half vs R (records inside initial ball < half)")
for R in radii:
    ball = r2 <= R * R
    n0 = int(ball.sum())
    ths = []
    for seed in range(8):
        rng = np.random.default_rng(100 + seed)
        rec = ball.copy()
        tt = 0
        while True:
            rec = tick(rec)
            tt += 1
            inside = int((rec & ball).sum())
            if inside < n0 / 2 or tt > 20000:
                break
        ths.append(tt)
    m = np.mean(ths); se = np.std(ths, ddof=1) / np.sqrt(len(ths))
    print(f"R={R:3d} N0={n0:6d}  t_half={m:8.1f} +- {se:5.1f}  t_half*p/R^2={m*p/R**2:.3f} +- {se*p/R**2:.3f}  "
          f"t_half/N0^(2/d)={m/n0**(2/d):.3f}")
