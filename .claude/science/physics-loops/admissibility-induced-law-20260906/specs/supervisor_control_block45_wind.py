"""Block 45 control (floating point; not the runner): the wind around ONE capturing body in the sphere-menu inertial gas: mean inward momentum per record in shells, against sqrt3 Q <1/r^2>/(4 pi (1 - rho)).
usage: supervisor_control_block45_wind.py L rho0 radius ticks seed gamma"""
import sys, time
import numpy as np
from numba import njit
from supervisor_control_block45_inertial import tick_s, gas_s, rand_unit, seed_compiled
from supervisor_control_block45_bodies import reservoir, porous

if __name__ == "__main__":
    L, rho0, radius, ticks, seed, gamma = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); c = L // 2
    porous(L, (c, c, c), radius, 1.0, solid, 1, rng)
    occ, sx, sy, sz = gas_s(L, rho0, rng); occ[solid > 0] = False
    idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
    for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
    bsites = np.argwhere(edge).astype(np.int64)
    rel = idx - c; rr = np.sqrt((rel ** 2).sum(axis=0)); rhat = np.where(rr > 0, rel / np.maximum(rr, 1e-9), 0.0)
    shells = [(6, 8), (8, 11), (11, 15), (15, 20), (20, 27), (27, 36)]
    masks = [(rr >= a) & (rr < b) & (solid == 0) for a, b in shells]
    g_in = np.zeros(len(shells)); dens = np.zeros(len(shells)); force = np.zeros((3, 3)); warm = 2000; every = 10; count = 0
    for t in range(warm + ticks):
        if t == warm: force[:] = 0
        tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, True); reservoir(occ, sx, sy, sz, bsites, rho0)
        if t >= warm and t % every == 0:
            radial = -(sx * rhat[0] + sy * rhat[1] + sz * rhat[2]) * occ          # inward component
            for i, m in enumerate(masks):
                g_in[i] += radial[m].sum() / m.sum(); dens[i] += occ[m].mean()
            count += 1
    q = force[0, 1] / ticks
    print(f"single capturing body R={radius}, side {L}, density {rho0}, gamma {gamma}: captures per tick Q = {q:.3f}")
    for i, (a, b) in enumerate(shells):
        rho = dens[i] / count; g = g_in[i] / count; rm = np.sqrt(rr[masks[i]] ** 2).mean(); r2 = (1.0 / rr[masks[i]] ** 2).mean()
        pred = np.sqrt(3) * q * r2 / (4 * np.pi * (1 - rho))
        print(f"   shell {a:2d}-{b:2d} (mean r {rm:5.1f}): density {rho:.4f}; inward momentum density {g:+.5f}; from the exact current sqrt3 Q <1/r^2>/(4 pi (1 - rho)) = {pred:.5f}; ratio {g / pred:.3f}")
