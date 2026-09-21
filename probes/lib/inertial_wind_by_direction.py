"""The wind of ONE transparent capturing body, by lattice direction, with and without scattering.
A porous ball (radius R, fill f) captures at the centre of an open box with a reservoir at the walls.  The mean momentum density g(x) is
accumulated over the run; its radial component times r^2, divided by the capture rate Q, is averaged over the sites with r in [rmin, rmax]
that lie within 15 degrees of an axis, of a face diagonal, of a body diagonal.
Prediction without collisions (first order in the density; exact multinomial shadow of every site of the body):
    g(x) = -(rho/(4 pi)) sum_a m I(x - a),   I(x) = integral over the simplex of w (w.w)^(-2) h(x, w) dw   (s |s|_1^3 = w (w.w)^(-2)),
to be compared with the collisional wind of block 45, sqrt3 Q/(4 pi r^2 (1 - rho)), the same in every direction.
usage: inertial_wind_by_direction.py L rho0 gamma ticks seed R fill rmin rmax   (writes nothing; prints one line)"""
import sys, time, os
import numpy as np
from scipy.special import gammaln
from inertial import tick_s, gas_s, seed_compiled
from inertial_porous_bodies import reservoir

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
    nmax = int(rmax + R + 2)
    if os.path.exists(TABLE) and np.load(TABLE)["tab"].shape[0] >= nmax + 1: tab = np.load(TABLE)["tab"]
    else:
        tab = build_table(nmax); np.savez(TABLE, tab=tab)
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
        pts = np.argwhere(sel) - c; pred = np.zeros(len(pts))
        for i, x in enumerate(pts):
            v = np.zeros(3)
            for a in body:
                dxyz = x - a; ad = np.abs(dxyz)
                if ad.max() < tab.shape[0]: v += tab[ad[0], ad[1], ad[2]] * np.sign(dxyz)
            xr = x / np.linalg.norm(x); pred[i] = (rho0 / (4 * np.pi)) * float(v @ xr) * float(x @ x)
        out.append((name, int(sel.sum()), inward.mean() / Q, pred.mean() / (np.sqrt(3) / 2 * rho0 * len(body))))
    coll = np.sqrt(3) / (4 * np.pi * (1 - rho0))
    txt = " | ".join(f"{n}: sites {k}, measured {m:.4f}, collisionless prediction {p:.4f}" for n, k, m, p in out)
    print(f"seed {seed} rho={rho0} gamma={gamma} body sites {len(body)} Q={Q:.3f} (kinetic {np.sqrt(3) / 2 * rho0 * len(body):.3f}); inward wind r^2/Q: {txt} | collisional value {coll:.4f} | {(warm + ticks) / (time.time() - t0):.0f} ticks/s")
