"""Block 52 control (floating point; not the runner): the wind of ONE capturing body by lattice direction under the BIASED-WALK clause
(a record of content s hops to x + e with probability (1 + s.e)/6 per attempt; supervisor_control_block52_biased.py).
A porous ball (radius R, fill f) captures at the centre of an open box with a reservoir at the walls; the inward momentum density times r^2 over
the capture rate is averaged over the sites with r in [rmin, rmax] within 15 degrees of an axis, of a face diagonal, of a body diagonal.
Isotropic closure for this clause: g = 3 J/(1 - rho), that is 3/(4 pi (1 - rho)) per unit capture.
usage: supervisor_control_block52_wind_by_direction.py L rho0 gamma ticks seed R fill rmin rmax"""
import sys, time, os
import numpy as np
from scipy.special import gammaln
from numba import njit
from supervisor_control_block52_inertial import gas_s, rand_unit, seed_compiled
from supervisor_control_block52_biased import tick_b as tick_s


@njit(cache=True)
def reservoir(occ, sx, sy, sz, bsites, rho0):
    for i in range(bsites.shape[0]):
        x, y, z = bsites[i, 0], bsites[i, 1], bsites[i, 2]
        if np.random.random() < rho0:
            ux, uy, uz = rand_unit(); occ[x, y, z] = True; sx[x, y, z] = ux; sy[x, y, z] = uy; sz[x, y, z] = uz
        else: occ[x, y, z] = False

GRID = 300
TABLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shadow_table.npz")


def build_table(nmax):
    g = (np.arange(GRID) + 0.5) / GRID
    w1, w2 = np.meshgrid(g, g, indexing="ij"); w3 = 1 - w1 - w2; keep = w3 > 0
    w = np.stack([w1[keep], w2[keep], w3[keep]]); logw = np.log(w); t2 = (w ** 2).sum(axis=0) ** -2.0
    tab = np.zeros((nmax + 1, nmax + 1, nmax + 1, 3))
    for x in np.ndindex(nmax + 1, nmax + 1, nmax + 1):
        n = sum(x)
        if n == 0: continue
        ax = np.array(x, float)
        logh = gammaln(n + 1) - gammaln(ax + 1).sum() + (ax[:, None] * logw).sum(axis=0)
        vec = (np.exp(logh) * t2 * w).sum(axis=1) / GRID ** 2
        tab[x] = vec * (ax > 0) * 2 ** int((ax == 0).sum())
    return tab


if __name__ == "__main__":
    L, rho0, gamma, ticks, seed = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    R, fill, rmin, rmax = int(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9])
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); c = L // 2; body = []
    for d in np.ndindex(2 * R + 1, 2 * R + 1, 2 * R + 1):
        dd = np.array(d) - R
        if (dd ** 2).sum() <= R * R and rng.random() < fill:
            solid[c + dd[0], c + dd[1], c + dd[2]] = 1; body.append(dd)
    body = np.array(body)
    occ, sx, sy, sz = gas_s(L, rho0, rng); occ[solid > 0] = False
    idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
    for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
    bsites = np.argwhere(edge).astype(np.int64)
    force = np.zeros((3, 3)); warm = 400; G = np.zeros((3, L, L, L)); t0 = time.time()
    for t in range(warm + ticks):
        if t == warm: force[:] = 0
        tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, True); reservoir(occ, sx, sy, sz, bsites, rho0)
        if t >= warm:
            G[0] += occ * sx; G[1] += occ * sy; G[2] += occ * sz
    G /= ticks; Q = force[0, 1] / ticks
    rel = np.stack([idx[a] - c for a in range(3)]).astype(float); r = np.sqrt((rel ** 2).sum(axis=0)); r[c, c, c] = 1.0
    rhat = rel / r; shell = (r >= rmin) & (r <= rmax)
    classes = {"axis": [(1, 0, 0), (0, 1, 0), (0, 0, 1)], "face diagonal": [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)],
               "body diagonal": [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]}
    cos15 = np.cos(np.radians(15.0)); out = []
    for name, dirs in classes.items():
        sel = np.zeros((L, L, L), bool)
        for d in dirs:
            u = np.array(d, float); u /= np.linalg.norm(u); sel |= np.abs(rhat[0] * u[0] + rhat[1] * u[1] + rhat[2] * u[2]) > cos15
        sel &= shell & (solid == 0)
        inward = -(G[0] * rhat[0] + G[1] * rhat[1] + G[2] * rhat[2])[sel] * r[sel] ** 2
        out.append((name, int(sel.sum()), inward.mean() / Q, 0.0))
    coll = 3.0 / (4 * np.pi * (1 - rho0))                     # g = 3 J/(1 - rho) for the biased walk (mean displacement s/3)
    txt = " | ".join(f"{n}: sites {k}, measured {m:.4f}" for n, k, m, p in out)
    print(f"seed {seed} rho={rho0} gamma={gamma} body sites {len(body)} Q={Q:.3f} (kinetic {rho0 * len(body):.3f}); inward wind r^2/Q: {txt} | isotropic closure {coll:.4f} | {(warm + ticks) / (time.time() - t0):.0f} ticks/s")
