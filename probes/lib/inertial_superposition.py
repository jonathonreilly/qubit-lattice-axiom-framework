"""Two capturing bodies; is the mean momentum density the superposition of two potential flows,
g(x) = sqrt3/(4 pi (1 - rho)) * sum_a Q_a (x_a - x)/|x - x_a|^3 ?   usage: inertial_superposition.py L rho0 radius sep ticks seed gamma"""
import sys
import numpy as np
from inertial import tick_s, gas_s, seed_compiled
from inertial_porous_bodies import reservoir, porous

if __name__ == "__main__":
    L, rho0, radius, sep, ticks, seed, gamma = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), float(sys.argv[7])
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); c = L // 2; c1, c2 = np.array((c - sep // 2, c, c)), np.array((c - sep // 2 + sep, c, c))
    porous(L, tuple(c1), radius, 1.0, solid, 1, rng); porous(L, tuple(c2), radius, 1.0, solid, 2, rng)
    occ, sx, sy, sz = gas_s(L, rho0, rng); occ[solid > 0] = False
    idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
    for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
    bsites = np.argwhere(edge).astype(np.int64)
    force = np.zeros((3, 3)); warm = 2000; every = 4; n = 0
    gsum = np.zeros((3, L, L, L)); dsum = np.zeros((L, L, L))
    for t in range(warm + ticks):
        if t == warm: force[:] = 0
        tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, True); reservoir(occ, sx, sy, sz, bsites, rho0)
        if t >= warm and t % every == 0:
            gsum[0] += sx * occ; gsum[1] += sy * occ; gsum[2] += sz * occ; dsum += occ; n += 1
    g = gsum / n; rho = dsum.sum() / n / (solid == 0).sum(); q1, q2 = force[0, 1] / ticks, force[0, 2] / ticks
    pos = idx.astype(float)
    pred = np.zeros_like(g)
    for ca, q in ((c1, q1), (c2, q2)):
        d = ca[:, None, None, None] - pos; r3 = (d ** 2).sum(axis=0) ** 1.5; r3[r3 == 0] = np.inf
        pred += np.sqrt(3) * q / (4 * np.pi * (1 - rho)) * d / r3
    r1 = np.sqrt(((pos - c1[:, None, None, None]) ** 2).sum(axis=0)); r2 = np.sqrt(((pos - c2[:, None, None, None]) ** 2).sum(axis=0))
    print(f"two capturing bodies R={radius} at separation {sep}, side {L}, density {rho:.3f}: Q = ({q1:.2f}, {q2:.2f}); {n} samples")
    for lo, hi in ((6, 9), (9, 13), (13, 18)):
        m = (np.minimum(r1, r2) >= lo) & (np.minimum(r1, r2) < hi) & ~edge & (solid == 0)
        num = (g[:, m] * pred[:, m]).sum(); den = (pred[:, m] ** 2).sum()
        resid = np.sqrt(((g[:, m] - pred[:, m]) ** 2).sum() / m.sum() / 3)
        noise = np.sqrt(rho / 3 / n)                                  # standard error of a mean momentum component at one site
        print(f"   sites with nearest body at {lo}-{hi}: {m.sum()} sites; best scalar fit g = a * prediction: a = {num / den:.3f}; rms residual per component {resid:.4f} (sampling noise {noise:.4f}); rms predicted field {np.sqrt(den / m.sum() / 3):.4f}")
    # the plane midway between the bodies: the component along the joining axis should vanish, the in-plane field should point to the axis
    mid = c - sep // 2 + sep // 2
    print(f"   midplane x = {mid}: mean |g_x| = {np.abs(g[0, mid, 8:-8, 8:-8]).mean():.4f} (noise {np.sqrt(rho / 3 / n) * 0.8:.4f}); predicted g_x = {np.abs(pred[0, mid, 8:-8, 8:-8]).mean():.4f}")
