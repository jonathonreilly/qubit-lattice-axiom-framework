#!/usr/bin/env python3
import numpy as np, math, time
from cyc2d import *

t0 = time.time()
rng = np.random.default_rng(7)
MIRROR = [(-d[0], d[1]) for d in SCHED]                       # image of SCHED under x -> -x
shifts = lambda s: [s[k:] + s[:k] for k in range(len(s))]
REV = [d for d in reversed(SCHED)]                            # schedule of the inverse cycle

# 1. bulk identity -------------------------------------------------------------------------
L = 16
none = np.zeros(L * L, bool)
ok = all(np.array_equal(run_cycle(L, none, s)[0], np.arange(L * L)) for s in shifts(SCHED) + shifts(MIRROR))
print("[1] bulk identity (all 4 phases, both hands), L=16 torus:", ok)

# 2. straight walls: locked band rows 0..3, free rows 4..15 -----------------------------------
lk = np.zeros(L * L, bool); lk[:4 * L] = True
pi, path = run_cycle(L, lk)
xs, ys = coords(L)
mv = np.nonzero(pi != np.arange(L * L))[0]
summ = {}
for s in mv:
    key = (int(ys[s]), int((xs[s] + ys[s]) % 2), int(mi(xs[pi[s]] - xs[s], L)), int(mi(ys[pi[s]] - ys[s], L)))
    summ[key] = summ.get(key, 0) + 1
print("[2] wall band: (row, parity A=0/B=1, dx, dy): count ->", summ)

# 3. square islands ---------------------------------------------------------------------------
L = 24
print("[3] islands s x s on L=24 torus (right-handed schedule; rho ccw-positive, rays cw-positive)")
for s in range(1, 7):
    lk = box(L, 10, 10, s, s)
    c = (10 + (s - 1) / 2.0, 10 + (s - 1) / 2.0)
    pi, path = run_cycle(L, lk)
    mvs = np.nonzero(pi != np.arange(L * L))[0]
    dist = cheb_dist_to_locked(L, lk)
    orb = orbits(pi)
    wind = [round(orbit_winding(L, path, o, c), 9) for o in orb]
    rA = rho_paths(L, path, c, 10.5)
    rS, mx = rho_straight(L, pi, c)
    rays = [ray_count(L, pi, c, u) for u in [(0, 1), (1, 0), (0, -1), (-1, 0)]] if s >= 2 else "n/a"
    per = 4 * s + 4                                              # free sites ringing the island (Chebyshev)
    lens = sorted(len(o) for o in orb)
    print(f"  s={s}: moved={len(mvs)} maxdist={int(dist[mvs].max()) if len(mvs) else 0} "
          f"orbits(len)={lens} windings={wind} rho_paths={rA:+.9f} rho_straight={rS:+.6f} "
          f"(max chord angle {mx/math.pi:.2f} pi) rays={rays}")

# 4./5. hand and phase -------------------------------------------------------------------------
lk = box(L, 10, 10, 4, 4); c = (11.5, 11.5)
res = []
for name, sch in [("R", SCHED), ("mirror", MIRROR)]:
    for k, s in enumerate(shifts(sch)):
        pi, path = run_cycle(L, lk, s)
        res.append((name, k, round(rho_straight(L, pi, c)[0], 9),
                    [ray_count(L, pi, c, u) for u in [(0, 1), (1, 0), (0, -1), (-1, 0)]]))
print("[4/5] 4x4 island, rho_straight and cw ray counts per schedule phase:", res)
print("      mirror schedule is a cyclic shift of the reversed (inverse) schedule:", MIRROR in shifts(REV),
      "| mirror is a cyclic shift of SCHED:", MIRROR in shifts(SCHED))

# 6. covariance up to cyclic relabelling (exact equality of permutations) -------------------
L = 16
xs, ys = coords(L)
Rm = lambda x, y: ((-y) % L, x % L)                              # 90 deg about site (0,0)
Tm = lambda x, y: ((x + 1) % L, y % L)                           # odd translation
Mm = lambda x, y: ((-x) % L, y % L)
def mapsite(f):
    X, Y = f(xs, ys); return Y * L + X
ok_R = ok_T = ok_M = True
comm = 0; ntr = 40
for trial in range(ntr):
    J = rng.random(L * L) < rng.choice([0.05, 0.15, 0.3])
    p0 = run_cycle(L, J, SCHED)[0]
    for f, k, sch, tag in [(Rm, 1, SCHED, "R"), (Tm, 2, SCHED, "T"), (Mm, 0, MIRROR, "M")]:
        g = mapsite(f)
        J2 = np.zeros_like(J); J2[g] = J
        p1 = run_cycle(L, J2, shifts(sch)[k])[0]
        good = np.array_equal(p1[g], g[p0])
        if tag == "R": ok_R &= good
        if tag == "T": ok_T &= good
        if tag == "M": ok_M &= good
    ps = [run_cycle(L, J, s)[0] for s in shifts(SCHED)]
    allc = all(np.array_equal(ps[a][ps[b]], ps[b][ps[a]]) for a in range(4) for b in range(a + 1, 4))
    comm += allc
print(f"[6] {ntr} random lock patterns: R(90)pi R^-1 = pi(shift 1): {ok_R}; T(odd)pi T^-1 = pi(shift 2): {ok_T}; "
      f"mirror image = mirror schedule: {ok_M}; four phase-shifted full cycles pairwise commute in {comm}/{ntr}")
print(f"time {time.time()-t0:.1f}s")
