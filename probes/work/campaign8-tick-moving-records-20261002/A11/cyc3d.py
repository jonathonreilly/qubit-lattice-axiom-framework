#!/usr/bin/env python3
"""3D schedule cycles on an L^3 torus (L even), one item per site, A sites = x+y+z even.
Sub-step d: every A site exchanges content with a+d unless either site is locked."""
import numpy as np

X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
neg = lambda v: tuple(-c for c in v)
LAYER_Z = [X, Y, neg(X), neg(Y)]                                    # supplied axis z
C3CYC = [X, Y, neg(Z), neg(X), Y, Z, neg(X), neg(Y), Z, X, neg(Y), neg(Z)]  # supplied diagonal (111)


def coords3(L):
    s = np.arange(L ** 3)
    z, r = np.divmod(s, L * L)
    y, x = np.divmod(r, L)
    return x, y, z


def idx(L, x, y, z):
    return ((z % L) * L + (y % L)) * L + (x % L)


def substep(L, locked, d, xyz):
    x, y, z = xyz
    perm = np.arange(L ** 3)
    a = np.nonzero((x + y + z) % 2 == 0)[0]
    b = idx(L, x[a] + d[0], y[a] + d[1], z[a] + d[2])
    ok = ~(locked[a] | locked[b])
    perm[a[ok]] = b[ok]
    perm[b[ok]] = a[ok]
    return perm


def run3(L, locked, sched):
    xyz = coords3(L)
    pos = np.arange(L ** 3)
    path = [pos.copy()]
    for d in sched:
        pos = substep(L, locked, d, xyz)[pos]
        path.append(pos.copy())
    return pos, np.array(path)


def mi(v, L):
    return (v + L / 2.0) % L - L / 2.0


def cube(L, lo, s):
    x, y, z = coords3(L)
    return (x >= lo) & (x < lo + s) & (y >= lo) & (y < lo + s) & (z >= lo) & (z < lo + s)


def plane_flux(L, pi, axis, cval, cond):
    """net number of straight moves s->pi[s] crossing the plane r_axis = cval (+ direction counts +1),
    counted only if the crossing point satisfies cond(point) (point = 3-vector, absolute coords)."""
    xyz = np.array(coords3(L), dtype=float)
    mv = np.nonzero(pi != np.arange(L ** 3))[0]
    p0 = xyz[:, mv]
    dp = mi(xyz[:, pi[mv]] - p0, L)
    tot = 0
    for k in range(len(mv)):
        a0, da = p0[axis, k], dp[axis, k]
        if da == 0:
            continue
        # crossing of r_axis = cval (allowing for periodic wrap: shift cval into (a0-L/2, a0+L/2])
        cv = a0 + mi(cval - a0, L)
        t = (cv - a0) / da
        if 0 < t < 1:
            pt = p0[:, k] + t * dp[:, k]
            if cond(pt):
                tot += 1 if da > 0 else -1
    return tot


def loop_area_density(L, path):
    """mean over all items of the area vector (1/2) sum r_k x r_{k+1} of the closed bulk path
    (only meaningful with no locks, where every path is closed)."""
    x, y, z = coords3(L)
    P = np.stack([x[path], y[path], z[path]], axis=-1).astype(float)      # (K+1, N, 3)
    rel = mi(P - P[0][None], L)
    a = 0.5 * np.cross(rel[:-1], rel[1:]).sum(axis=0)                     # (N, 3)
    return a.mean(axis=0), np.abs(a - a.mean(axis=0)).max()
