"""A54 c4: spin-1/2 U(1) version.  On ice states only some flips are allowed, so the constraints on chi are
weaker than in the Z2 form.  Test: is there a bounded-range quadratic Q (B_lm for |x_l-x_m|^2 <= R2,
plus a linear part b) with Q(n') + Q(n) = log-sign of the dressed flip, for every edge of a BFS sample of the
ice graph?  (A certificate of 'no solution' on a sample is a certificate for the whole ice graph.)
Usage: c4_ice_local.py Lx,Ly,Lz R2a,R2b,... cap [uniform|random]"""
import signal, sys, time
signal.alarm(118)
from collections import deque
from a54lib import *

shape = tuple(int(t) for t in sys.argv[1].split(','))
R2s = [int(t) for t in sys.argv[2].split(',')]
cap = int(sys.argv[3]); rk = sys.argv[4] if len(sys.argv) > 4 else 'uniform'
kind = sys.argv[5] if len(sys.argv) > 5 else 'fermion'
tor, recs, hops, dcol, loops, dp, Ddp = setup(shape, 0, rk, seed=21)
n = tor.n; NP = len(dp)
if kind == 'boson':        # control: hops X_l Z^{B0 e_l}, B0 random symmetric local (range^2 4) -> local chi exists
    rngb = np.random.default_rng(5); B0 = [0] * n
    for l in range(n):
        for m in range(l + 1, n):
            if link_d2(tor, l, m) <= 4 and rngb.random() < 0.5:
                B0[l] |= 1 << m; B0[m] |= 1 << l
    dcol = B0
st0 = 0
for l in range(n):
    v, i, w, ip = tor.ends(l); a = i // 2
    if (-1) ** (sum(v[bb] // 2 for bb in range(3) if bb != a)) == -1: st0 |= 1 << l
lps = [[(l, SIGN[i]) for (l, v, i, w, ip) in lp] for lp in loops]
def flip(st, loop, dagger):
    seq = loop if not dagger else loop[::-1]; sign = 0
    for (l, s) in seq:
        e = -1 if (st >> l) & 1 else 1
        if s * e != (-1 if not dagger else 1): return None
        sign ^= popc(st & dcol[l]) & 1
        st ^= 1 << l
    return st, sign
t0 = time.time()
import random
random.seed(7)
E = []; nst = 0; mode = 'walk'
for walker in range(10):
    st = st0
    for step in range(cap):
        p = random.randrange(NP); dg = random.random() < 0.5
        r = flip(st, lps[p], dg)
        if r is not None:
            st = r[0]
        if step % 25 == 24:
            nst += 1
            for p2, loop in enumerate(lps):
                for dg2 in (False, True):
                    r2 = flip(st, loop, dg2)
                    if r2 is not None:
                        E.append((st, p2, r2[1]))
seen = range(nst); q = None
rank_of = {l: r for r, l in enumerate(sorted(range(n), key=lambda l: tor.links[l][::-1]))}
for R2 in R2s:
    t1 = time.time()
    nb = [[m for m in range(n) if m != l and link_d2(tor, l, m) <= R2] for l in range(n)]
    pairs = sorted((max(rank_of[l], rank_of[m]), min(rank_of[l], rank_of[m]), l, m)
                   for l in range(n) for m in nb[l] if l < m)
    var = {(l, m): k + 1 + n for k, (_, _, l, m) in enumerate(pairs)}     # b_l are unknowns 1..n
    nbm = [{m: var[(min(l, m), max(l, m))] for m in nb[l]} for l in range(n)]
    S = GF2()
    for (st, p, sg) in E:
        row = sg
        lp = bits_of(dp[p])
        for m in lp:
            row ^= 1 << (m + 1)                                  # b . dp
            for l, k in nbm[m].items():
                if (dp[p] >> l) & 1:
                    continue
                if (st >> l) & 1:
                    row ^= 1 << k                                # n_l * dp_m
        for i1 in range(4):
            for i2 in range(i1 + 1, 4):
                l, m = lp[i1], lp[i2]
                k = nbm[l].get(m)
                if k and (((st >> l) & 1) ^ ((st >> m) & 1) ^ 1):
                    row ^= 1 << k                                # (n_l + n_m + 1) for pairs inside the loop
        if row: S.add(row)
    print("  R2 <= %2d: unknowns %6d, rank %6d, inconsistent %6d -> %s (%.1f s)" % (
        R2, len(var) + n, S.rank(), S.incons, 'SOLVABLE on the sample' if S.incons == 0 else 'no solution', time.time() - t1))
    sys.stdout.flush()
print("done")
