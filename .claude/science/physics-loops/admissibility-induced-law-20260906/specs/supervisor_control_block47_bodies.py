"""Block 47 control (floating point; not the runner): two CAPTURING bodies of different size and porosity in the sphere-menu inertial gas.
usage: supervisor_control_block47_bodies.py L rho0 sep ticks seed gamma R1 f1 R2 f2     (a ball of radius R in which each site is solid with probability f)
A second body with fill 0 is absent (single-body runs).  Reports, per body: number of solid sites, captures per tick, force per tick towards the other body; and F r^2/(Q1 Q2)."""
import sys, time
import numpy as np
from numba import njit
from supervisor_control_block47_inertial import tick_s, gas_s, rand_unit, seed_compiled, EK

@njit(cache=True)
def reservoir(occ, sx, sy, sz, bsites, rho0):
    for i in range(bsites.shape[0]):
        x, y, z = bsites[i, 0], bsites[i, 1], bsites[i, 2]
        if np.random.random() < rho0:
            ux, uy, uz = rand_unit(); occ[x, y, z] = True; sx[x, y, z] = ux; sy[x, y, z] = uy; sz[x, y, z] = uz
        else: occ[x, y, z] = False

def porous(L, centre, radius, fill, solid, bid, rng):
    n = 0
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            for dz in range(-radius, radius + 1):
                if dx * dx + dy * dy + dz * dz <= radius * radius and rng.random() < fill:
                    solid[centre[0] + dx, centre[1] + dy, centre[2] + dz] = bid; n += 1
    return n

if __name__ == "__main__":
    L, rho0, sep, ticks, seed, gamma = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    R1, f1, R2, f2 = int(sys.argv[7]), float(sys.argv[8]), int(sys.argv[9]), float(sys.argv[10])
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); c = L // 2; c1, c2 = (c - sep // 2, c, c), (c - sep // 2 + sep, c, c)
    n1 = porous(L, c1, R1, f1, solid, 1, rng); n2 = porous(L, c2, R2, f2, solid, 2, rng)
    occ, sx, sy, sz = gas_s(L, rho0, rng); occ[solid > 0] = False
    idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
    for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
    bsites = np.argwhere(edge).astype(np.int64)
    force = np.zeros((3, 3)); warm = 2000; t0 = time.time(); marks = []
    for t in range(warm + ticks):
        if t == warm: force[:] = 0
        tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, True); reservoir(occ, sx, sy, sz, bsites, rho0)
        if t >= warm and (t - warm + 1) % (ticks // 10) == 0: marks.append(force[1:, 0].copy())
    per = np.diff(np.vstack([np.zeros(2), np.array(marks)]), axis=0) / (ticks // 10)
    F1, F2 = per[:, 0], -per[:, 1]; q1, q2 = force[0, 1] / ticks, force[0, 2] / ticks
    e = lambda v: v.std(ddof=1) / np.sqrt(len(v))
    fm = 0.5 * (F1.mean() + F2.mean())
    print(f"sep={sep} body1 (R={R1}, f={f1}, sites {n1}): Q={q1:.3f}, F={F1.mean():+.4f}+-{e(F1):.4f} | body2 (R={R2}, f={f2}, sites {n2}): Q={q2:.3f}, F={F2.mean():+.4f}+-{e(F2):.4f} | F r^2/(Q1 Q2) = {fm * sep * sep / (q1 * q2):.3f} (wind estimate sqrt3/(4 pi rho (1-rho)) = {np.sqrt(3) / (4 * np.pi * rho0 * (1 - rho0)):.3f}); {(warm + ticks) / (time.time() - t0):.0f} ticks/s")
