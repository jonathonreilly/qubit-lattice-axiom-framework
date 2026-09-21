"""Bodies in BALANCE (they re-emit what they capture) against bodies that only capture.
A balanced body keeps a store of captured records; every tick each stored record tries once to leave: a random site of the body, a random
direction, and if the neighbouring site there is free gas it receives a record whose content follows the cosine law about the outward
normal (the time reverse of capture); the body's momentum changes by minus that content.
usage: inertial_balanced.py L rho0 sep ticks seed gamma R fill mode1 mode2      (mode = c: captures only; b: balanced)
Reports per body: captures and emissions per tick, force towards the other body (captured minus emitted momentum), and the wind coefficient."""
import sys, time
import numpy as np
from numba import njit
from inertial import tick_s, gas_s, rand_unit, seed_compiled, EK
from inertial_porous_bodies import reservoir, porous


@njit(cache=True)
def emit(occ, sx, sy, sz, solid, sites, bid, store, force, counts):
    left = store
    for _ in range(store):
        i = np.random.randint(0, sites.shape[0]); k = np.random.randint(0, 6)
        tx = sites[i, 0] + EK[k, 0]; ty = sites[i, 1] + EK[k, 1]; tz = sites[i, 2] + EK[k, 2]
        if solid[tx, ty, tz] != 0 or occ[tx, ty, tz]: continue
        u = np.random.random(); cn = np.sqrt(u); st = np.sqrt(1.0 - u); ph = 2.0 * np.pi * np.random.random()
        a = k // 2; sgn = 1.0 if k % 2 == 0 else -1.0
        v = np.zeros(3); v[a] = sgn * cn; v[(a + 1) % 3] = st * np.cos(ph); v[(a + 2) % 3] = st * np.sin(ph)
        occ[tx, ty, tz] = True; sx[tx, ty, tz] = v[0]; sy[tx, ty, tz] = v[1]; sz[tx, ty, tz] = v[2]
        force[bid, 0] -= v[0]; force[bid, 1] -= v[1]; force[bid, 2] -= v[2]; counts[bid] += 1.0; left -= 1
    return left


if __name__ == "__main__":
    L, rho0, sep, ticks, seed, gamma = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    R, fill, mode = int(sys.argv[7]), float(sys.argv[8]), (sys.argv[9], sys.argv[10])
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); c = L // 2; c1, c2 = (c - sep // 2, c, c), (c - sep // 2 + sep, c, c)
    n1 = porous(L, c1, R, fill, solid, 1, rng); n2 = porous(L, c2, R, fill, solid, 2, rng)
    sites = [np.argwhere(solid == b).astype(np.int64) for b in (1, 2)]
    occ, sx, sy, sz = gas_s(L, rho0, rng); occ[solid > 0] = False
    idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
    for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
    bsites = np.argwhere(edge).astype(np.int64)
    force = np.zeros((3, 3)); emitted = np.zeros(3); store = [0, 0]; seen = [0.0, 0.0]; warm = 1500; t0 = time.time(); marks = []
    for t in range(warm + ticks):
        if t == warm: force[:] = 0; emitted[:] = 0; seen = [0.0, 0.0]
        tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, True); reservoir(occ, sx, sy, sz, bsites, rho0)
        for b in (0, 1):
            new = force[0, b + 1] - seen[b]; seen[b] = force[0, b + 1]
            if mode[b] == "b":
                store[b] += int(round(new)); store[b] = emit(occ, sx, sy, sz, solid, sites[b], b + 1, store[b], force, emitted)
        if t >= warm and (t - warm + 1) % (ticks // 10) == 0: marks.append(force[1:, 0].copy())
    per = np.diff(np.vstack([np.zeros(2), np.array(marks)]), axis=0) / (ticks // 10)
    F1, F2 = per[:, 0], -per[:, 1]; q = [force[0, 1] / ticks, force[0, 2] / ticks]; em = [emitted[1] / ticks, emitted[2] / ticks]
    e = lambda v: v.std(ddof=1) / np.sqrt(len(v)); k0 = np.sqrt(3) / (4 * np.pi * rho0 * (1 - rho0))
    print(f"modes {mode[0]}{mode[1]} seed {seed} sep={sep} rho={rho0} gamma={gamma} | body1 ({n1} sites): captures {q[0]:.3f}, emits {em[0]:.3f}, net {q[0] - em[0]:+.3f}, store {store[0]}, F1={F1.mean():+.4f}+-{e(F1):.4f} | body2 ({n2} sites): captures {q[1]:.3f}, emits {em[1]:.3f}, net {q[1] - em[1]:+.3f}, store {store[1]}, F2={F2.mean():+.4f}+-{e(F2):.4f} | reference K0 Q1 Q2/r^2 with gross captures = {k0 * q[0] * q[1] / sep ** 2:.4f}; {(warm + ticks) / (time.time() - t0):.0f} ticks/s")
