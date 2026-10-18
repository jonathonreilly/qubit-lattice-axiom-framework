"""Canonical symmetric triangulations of B4-invariant periodic point sets in R^4.

Delaunay cells of the periodic set; every non-simplicial face (cell, facet, 2-face) is coned from its
circumcentre ('pulling' from circumcentres), which is choice-free and keeps every symmetry of the set.
Returns base simplices as (cell, type) vertex lists with fractional offsets per type, ready for regge_generic.Complex.
"""
import itertools, numpy as np
from fractions import Fraction
from scipy.spatial import Delaunay, ConvexHull

TOL = 1e-8
E4 = np.eye(4)

def orbit_offsets(which):
    """which: subset of {1,2,3,4}: half-integer orbits with that many 1/2 coordinates."""
    offs = [np.zeros(4)]
    for r in sorted(which):
        for S in itertools.combinations(range(4), r):
            v = np.zeros(4); v[list(S)] = 0.5; offs.append(v)
    return offs

def patch(offs, lo=-2, hi=3):
    pts = []
    for b in itertools.product(range(lo, hi), repeat=4):
        for o in offs: pts.append(np.array(b, float) + o)
    return np.array(pts)

def circumcenter(P):
    """centre of the sphere through the points P (m x 4), within their affine hull."""
    p0 = P[0]; A = P[1:] - p0
    # x = p0 + A^T y ; |x - p_i|^2 equal  ->  2 A A^T y = |A_i|^2
    G = A @ A.T; b = 0.5 * np.einsum('ij,ij->i', A, A)
    y = np.linalg.lstsq(G, b, rcond=None)[0]
    return p0 + A.T @ y

def local_frame(P):
    c = P.mean(axis=0); u, s, vt = np.linalg.svd(P - c)
    d = int((s > TOL).sum()); return c, vt[:d]

def facets(P):
    """facets of the convex polytope with vertex set P (points spanning their affine hull)."""
    c, B = local_frame(P); X = (P - c) @ B.T; d = B.shape[0]
    if d == 1:
        i, j = np.argmin(X[:, 0]), np.argmax(X[:, 0]); return [P[[i]], P[[j]]]
    hull = ConvexHull(X)
    groups = {}
    for eq in hull.equations:
        key = tuple(np.round(eq / np.linalg.norm(eq[:-1]), 7))
        groups[key] = eq
    out = []
    for eq in groups.values():
        on = np.abs(X @ eq[:-1] + eq[-1]) < 1e-7
        out.append(P[on])
    return out

def subdivide(P):
    """symmetric triangulation of the polytope conv(P) (P cospherical vertex set) -> list of point arrays."""
    c, B = local_frame(P); d = B.shape[0]
    if len(P) == d + 1: return [P]
    cc = circumcenter(P)
    out = []
    for F in facets(P):
        for s in subdivide(F):
            t = np.vstack([s, cc])
            if np.linalg.matrix_rank(t[1:] - t[0], tol=1e-9) == len(t) - 1: out.append(t)   # drop flat cones
    return out

def delaunay_cells(offs):
    pts = patch(offs)
    tri = Delaunay(pts, qhull_options='Qbb Qc Qz Q12 Qt')
    cells = {}
    for simp in tri.simplices:
        P = pts[simp]
        if abs(np.linalg.det(P[1:] - P[0])) < 1e-9: continue           # flat sliver from Qt
        cc = circumcenter(P); r = np.linalg.norm(P[0] - cc)
        if np.any(cc < -0.01) or np.any(cc > 1.01): continue      # keep cells whose centre is near the base cell
        key = tuple(np.round(cc, 6))
        if key in cells: continue
        # all patch points on that sphere = the Delaunay cell
        on = np.abs(np.linalg.norm(pts - cc, axis=1) - r) < 1e-6
        cells[key] = (cc, pts[on])
    # one representative per translation class: circumcentre in [0,1)^4
    reps = {}
    for key, (cc, P) in cells.items():
        f = np.mod(np.round(cc, 6), 1.0); f[np.abs(f - 1) < 1e-9] = 0
        k2 = tuple(np.round(f, 6))
        if k2 not in reps: reps[k2] = (cc, P - (cc - f))
    return list(reps.values())

def build(which):
    offs = orbit_offsets(which)
    cells = delaunay_cells(offs)
    simps = []
    for cc, P in cells:
        simps += subdivide(P)
    # vertex types by fractional position
    types = {}
    def vid(x):
        f = np.mod(np.round(x * 840) / 840, 1.0); key = tuple(np.round(f, 6))
        if key not in types: types[key] = len(types)
        b = tuple(int(v) for v in np.round(x - np.array(key)))
        return (b, types[key])
    base = [[vid(x) for x in s] for s in simps]
    OFF = [np.array(k) for k, _ in sorted(types.items(), key=lambda kv: kv[1])]
    vol = sum(abs(np.linalg.det(s[1:] - s[0])) / 24 for s in simps)
    return OFF, base, vol, len(cells), [len(P) for _, P in cells]
