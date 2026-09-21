"""Block 44 control (floating point; not the runner): two bodies in the sphere-menu inertial gas.  usage: inertial_bodies.py L rho0 radius separation Q ticks seed gamma [absorb] [single]
Force per tick on each body along the joining axis, positive = towards the other body; absorbing bodies also report captures per tick.
The committed output was produced before the compiled generator was seeded; re-runs agree with it within the quoted errors, not digit for digit."""
import sys, time
import numpy as np
from numba import njit
from inertial import tick_s, gas_s, rand_unit, seed_compiled, EK

@njit(cache=True)
def emit(occ, sx, sy, sz, sites, dirs, q_whole, q_frac, force, b):
    n = q_whole + (1 if np.random.random() < q_frac else 0)
    for _ in range(n):
        for _try in range(40):
            i = np.random.randint(0, sites.shape[0]); x, y, z = sites[i, 0], sites[i, 1], sites[i, 2]
            if not occ[x, y, z]:
                ux, uy, uz = rand_unit(); k = dirs[i]
                if ux * EK[k, 0] + uy * EK[k, 1] + uz * EK[k, 2] < 0: ux, uy, uz = -ux, -uy, -uz
                occ[x, y, z] = True; sx[x, y, z] = ux; sy[x, y, z] = uy; sz[x, y, z] = uz
                force[b, 0] -= ux; force[b, 1] -= uy; force[b, 2] -= uz
                break

@njit(cache=True)
def reservoir(occ, sx, sy, sz, bsites, rho0):
    for i in range(bsites.shape[0]):
        x, y, z = bsites[i, 0], bsites[i, 1], bsites[i, 2]
        if np.random.random() < rho0:
            ux, uy, uz = rand_unit(); occ[x, y, z] = True; sx[x, y, z] = ux; sy[x, y, z] = uy; sz[x, y, z] = uz
        else: occ[x, y, z] = False

def body(L, centre, radius, solid, bid):
    sites, dirs = [], []; rng = range(-radius - 1, radius + 2)
    for dx in rng:
        for dy in rng:
            for dz in rng:
                if dx * dx + dy * dy + dz * dz <= radius * radius: solid[centre[0] + dx, centre[1] + dy, centre[2] + dz] = bid
    for dx in rng:
        for dy in rng:
            for dz in rng:
                s = (centre[0] + dx, centre[1] + dy, centre[2] + dz)
                if solid[s] == bid:
                    for k in range(6):
                        t = (s[0] + EK[k, 0], s[1] + EK[k, 1], s[2] + EK[k, 2])
                        if solid[t] == 0: sites.append(t); dirs.append(k)
    return np.array(sites, np.int64), np.array(dirs, np.int64)

if __name__ == "__main__":
    absorb = "absorb" in sys.argv; single = "single" in sys.argv
    L, rho0, radius, sep, q, ticks, seed, gamma = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), float(sys.argv[8])
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); c = L // 2; c1, c2 = (c - sep // 2, c, c), (c - sep // 2 + sep, c, c)
    s1, d1 = body(L, c1, radius, solid, 1); s2, d2 = (s1, d1) if single else body(L, c2, radius, solid, 2)
    occ, sx, sy, sz = gas_s(L, rho0, rng); occ[solid > 0] = False
    idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
    for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
    bsites = np.argwhere(edge).astype(np.int64)
    force = np.zeros((3, 3)); warm = 2000; t0 = time.time(); marks = []
    for t in range(warm + ticks):
        if t == warm: force[:] = 0
        if q > 0:
            emit(occ, sx, sy, sz, s1, d1, int(q), q - int(q), force, 1)
            if not single: emit(occ, sx, sy, sz, s2, d2, int(q), q - int(q), force, 2)
        tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, absorb); reservoir(occ, sx, sy, sz, bsites, rho0)
        if t >= warm and (t - warm + 1) % (ticks // 10) == 0: marks.append(force[1:, 0].copy())
    per = np.diff(np.vstack([np.zeros(2), np.array(marks)]), axis=0) / (ticks // 10)
    f1, f2 = per[:, 0], -per[:, 1]; f = f1 if single else 0.5 * (f1 + f2)
    tag = ("ABSORB" if absorb else ("EMIT" if q > 0 else "REFLECT")) + (" SINGLE" if single else " PAIR")
    print(f"{tag} L={L} sep={sep} Q={q} rho0={rho0} R={radius} gamma={gamma}: force towards the other body per tick = {f.mean():+.4f} +- {f.std(ddof=1) / np.sqrt(len(f)):.4f}" + (f"; captures per tick per body {force[0, 1] / ticks:.3f}" if absorb else "") + f"; mean density {occ[solid == 0].mean():.3f}; {(warm + ticks) / (time.time() - t0):.0f} ticks/s")
