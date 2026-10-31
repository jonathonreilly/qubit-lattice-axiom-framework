#!/usr/bin/env python3
"""Gate theorem-z-repaired: two exact checks, written before running.

N1 (sheet, non-abelian Stokes). Consumer: Lemma OC, whose Y_i has absolute radius, and the dense step of Prop 10.
 Field: SU(2) centre links on a 4-torus of side N. Links in direction 0 from x_0 = c to c + 1 with a <= x_1 < b are -1, all others +1.
 C1a. Every plaquette is exactly +1 or -1, and the -1 plaquettes are (0,1) plaquettes at x_1 = a - 1 and x_1 = b - 1 with x_0 = c: two sheets.
 C1b. Every rectangle in the (0,1) plane around one sheet and not the other has holonomy -1, at every radius tried.
 C1c. Stokes control: on random SU(2) link fields on an n x n patch with plaquette angles near t, the boundary holonomy angle is at most the sum of plaquette angles, 1000 trials, n = 2..6, no violation. Angle of g := arccos(tr g / 2), so d(1, -1) = pi.
 Reading fixed in advance: if C1a-c hold, any field equal to this one off a set whose section is a disc of n plaquettes has some plaquette angle in that disc at least pi/n. So a class field (angle <= T) needs n >= pi/T. Limits: this is a statement on existence of a fill, not on energy.

N3 (brick layers). Consumer: "Thickness at least t_0" and "in Sigma_{l+1}" in `library/quiet-boundary-rarity.md`, Sigma(E) := bricks not in E that touch E.
 Tiling: Lemma BG, d = 2, 3, 4, shifts v_{d-1} = t_0 (2^-(d-1), ..., 2^-1), t_0 = 8. E: one brick, and 40 random unions of bricks in a window of side 5 t_0.
 Thickness := min over cells z outside E u Sigma of the sup distance from z to E, minus 1 (cells of the layer on a straight path). Cells within t_0 of the window edge are not read.
 C3a. Control: Sigma_w(E) := bricks within sup distance t_0 of E has thickness at least t_0 - 1 in every case.
 Reading fixed in advance: thickness of touching-Sigma below t_0 - 1 in some case means the sentence fails as written; the value is reported, and t_0 >= 3 R_loc then gives room R_loc only if the value is at least t_0/3.
Limits: finite window; combinatorics only.
"""
import sys
import numpy as np
from scipy import ndimage

def angle(g):
    return float(np.arccos(np.clip(np.trace(g).real / 2, -1, 1)))

def su2(v):
    t = np.linalg.norm(v)
    s = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
    if t == 0:
        return np.eye(2, dtype=complex)
    n = v / t
    return np.cos(t) * np.eye(2) + 1j * np.sin(t) * sum(n[i] * s[i] for i in range(3))

def n1():
    N, c, a, b = 12, 5, 3, 8
    U = np.ones((4,) + (N,) * 4)
    idx = [slice(None)] * 4
    idx[0], idx[1] = c, slice(a, b)
    U[0][tuple(idx)] = -1
    minus = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            P = U[mu] * np.roll(U[nu], -1, axis=mu) * np.roll(U[mu], -1, axis=nu) * U[nu]
            assert set(np.unique(P)) <= {-1.0, 1.0}
            for x in np.argwhere(P == -1):
                minus.append((mu, nu, tuple(x)))
    planes = {(m[0], m[1]) for m in minus}
    x0s = {m[2][0] for m in minus}
    x1s = {m[2][1] for m in minus}
    ok_a = planes == {(0, 1)} and x0s == {c} and x1s == {a - 1, b - 1}
    print("C1a", ok_a, "planes", planes, "x0", x0s, "x1", x1s, "n(-1)", len(minus), "expected", 2 * N * N)
    # Rectangles about the sheet at x_1 = a - 1 in the plane x_2 = x_3 = 0.
    ok_b = True
    for r in range(1, 3):
        p0, p1 = c - r + 1, a - 1 - r + 1
        h = 1.0
        # bottom along direction 0, right along 1, top back along 0, left back along 1: only direction 0 links carry -1
        for t in range(2 * r):
            h *= U[0][(p0 + t) % N, p1 % N, 0, 0]
            h *= U[0][(p0 + t) % N, (p1 + 2 * r) % N, 0, 0]
        print(" rectangle half-side", r, "holonomy", h)
        ok_b = ok_b and h == -1
    print("C1b", ok_b)
    rng = np.random.default_rng(1)
    worst, bad = 0.0, 0
    for trial in range(1000):
        n = int(rng.integers(2, 7))
        t = 10 ** rng.uniform(-3, -0.3)
        H = [[su2(rng.normal(size=3) * t) for _ in range(n)] for _ in range(n + 1)]  # horizontal links
        V = [[su2(rng.normal(size=3) * t) for _ in range(n + 1)] for _ in range(n)]  # vertical links
        tot = 0.0
        for i in range(n):
            for j in range(n):
                P = H[i][j] @ V[i][j + 1] @ H[i + 1][j].conj().T @ V[i][j].conj().T
                tot += angle(P)
        W = np.eye(2, dtype=complex)
        for j in range(n):
            W = W @ H[0][j]
        for i in range(n):
            W = W @ V[i][n]
        for j in reversed(range(n)):
            W = W @ H[n][j].conj().T
        for i in reversed(range(n)):
            W = W @ V[i][0].conj().T
        hol = angle(W)
        worst = max(worst, hol / tot)
        bad += hol > tot + 1e-9
    print("C1c violations", bad, "largest hol/sum", worst)
    return ok_a and ok_b and bad == 0

def ids(d, t, shape):
    """Label of the Lemma BG brick of each cell, as one integer array."""
    grids = np.indices(shape, dtype=np.int64)
    x = [grids[i] - shape[i] // 2 for i in range(d)]
    lab = np.zeros(shape, dtype=np.int64)
    for k in range(d - 1, -1, -1):  # coordinate k is the layer coordinate of T_{k+1}
        m = np.floor_divide(x[k], t)
        lab = lab * 1009 + (m + 500)
        for i in range(k):
            shift = t // 2 ** (k - i)  # v_{k}: t 2^-(k), ..., t 2^-1 for i = 0, ..., k - 1
            x[i] = x[i] - m * shift
    return np.unique(lab, return_inverse=True)[1].reshape(shape)

def thickness(E, Sigma, t, d):
    dist = ndimage.distance_transform_cdt(~E, metric="chessboard")
    out = ~(E | Sigma)
    core = np.zeros(E.shape, bool)
    core[(slice(t, -t),) * d] = True
    return int(dist[out & core].min()) - 1

def layers(lab, E, t, d):
    st = ndimage.generate_binary_structure(d, d)
    grown = ndimage.binary_dilation(E, st)
    touch = np.isin(lab, np.unique(lab[grown & ~E]))
    wide = ndimage.distance_transform_cdt(~E, metric="chessboard") <= t
    within = np.isin(lab, np.unique(lab[wide & ~E]))
    return touch & ~E, within & ~E

def n3():
    t = 8
    rng = np.random.default_rng(2)
    good = True
    for d in (2, 3, 4):
        shape = (5 * t,) * d
        lab = ids(d, t, shape)
        n = lab.max() + 1
        ctr = lab[tuple(s // 2 for s in shape)]
        res_t, res_w = [], []
        for k in range(41):
            if k == 0:
                E = lab == ctr
            else:
                pick = rng.random(n) < 0.15
                E = pick[lab]
            s1, s2 = layers(lab, E, t, d)
            if (~(E | s1))[(slice(t, -t),) * d].any():
                res_t.append(thickness(E, s1, t, d))
            if (~(E | s2))[(slice(t, -t),) * d].any():
                res_w.append(thickness(E, s2, t, d))
        print("d", d, "t_0", t, "touching: min thickness", min(res_t), "; within t_0: min thickness", min(res_w), "cases", len(res_t), len(res_w))
        good = good and min(res_w) >= t - 1
    print("C3a control", good)
    return good

if __name__ == "__main__":
    print("N1 PASS" if n1() else "N1 FAIL")
    print("N3 control PASS" if n3() else "N3 control FAIL")
