#!/usr/bin/env python3
"""2D schedule cycle on an L x L torus (L even), one item (qubit content) per site.

Sub-step with direction d: every A site a (x+y even) exchanges its whole content with
a+d, unless a or a+d is locked (record).  Locked sites never change.
The full cycle is the composition of the sub-steps; pi[s] = final site of the content
that started at s.  Everything is integer bookkeeping except angle sums (float, rounded
and checked against integers).
"""
import numpy as np, math

SCHED = [(1, 0), (0, 1), (-1, 0), (0, -1)]   # +x, +y, -x, -y  ("right-handed" schedule)


def coords(L):
    ys, xs = np.divmod(np.arange(L * L), L)
    return xs, ys


def substep_perm(L, locked, d):
    xs, ys = coords(L)
    perm = np.arange(L * L)
    a = np.nonzero((xs + ys) % 2 == 0)[0]
    b = ((ys[a] + d[1]) % L) * L + (xs[a] + d[0]) % L
    ok = ~(locked[a] | locked[b])
    perm[a[ok]] = b[ok]
    perm[b[ok]] = a[ok]
    return perm


def run_cycle(L, locked, sched=SCHED):
    pos = np.arange(L * L)
    path = [pos.copy()]
    for d in sched:
        pos = substep_perm(L, locked, d)[pos]
        path.append(pos.copy())
    return pos, np.array(path)          # pi, path[k, s] = site of item s after k sub-steps


def mi(v, L):                            # minimal-image displacement (float ok)
    return (v + L / 2.0) % L - L / 2.0


def rel(L, sites, c):
    xs, ys = coords(L)
    return mi(xs[sites] - c[0], L), mi(ys[sites] - c[1], L)


def wrap(a):
    return (a + math.pi) % (2 * math.pi) - math.pi


def rho_paths(L, path, c, R):
    """(1/2pi) * total angle swept around point c by all items' sub-step paths
    (ccw positive), items starting within radius R of c."""
    x0, y0 = rel(L, path[0], c)
    sel = np.nonzero(x0 ** 2 + y0 ** 2 < R * R)[0]
    tot = 0.0
    th_prev = None
    for k in range(path.shape[0]):
        x, y = rel(L, path[k, sel], c)
        th = np.arctan2(y, x)
        if th_prev is not None:
            dth = wrap(th - th_prev)
            assert np.all(np.abs(dth) < 0.75 * math.pi), "step too close to c"
            tot += dth.sum()
        th_prev = th
    return tot / (2 * math.pi)


def rho_straight(L, pi, c):
    """(1/2pi) * sum over moved items of the straight-chord angle s -> pi[s] around c.
    Returns (value, max |chord angle|) so ambiguity can be flagged."""
    mv = np.nonzero(pi != np.arange(L * L))[0]
    if len(mv) == 0:
        return 0.0, 0.0
    x0, y0 = rel(L, mv, c)
    x1, y1 = rel(L, pi[mv], c)
    d = wrap(np.arctan2(y1, x1) - np.arctan2(y0, x0))
    return d.sum() / (2 * math.pi), float(np.abs(d).max())


def ray_count(L, pi, c, u, eps=0.3):
    """Net clockwise crossings of the ray {c + eps*v + t*u, t>0} by straight moves
    s -> pi[s] (v = u rotated by +90 deg).  Rotate so that u -> (0,1)."""
    Q = {(0, 1): ((1, 0), (0, 1)), (1, 0): ((0, -1), (1, 0)),
         (0, -1): ((-1, 0), (0, -1)), (-1, 0): ((0, 1), (-1, 0))}[u]
    mv = np.nonzero(pi != np.arange(L * L))[0]
    if len(mv) == 0:
        return 0
    x0, y0 = rel(L, mv, c)
    x1, y1 = rel(L, pi[mv], c)
    X0, Y0 = Q[0][0] * x0 + Q[0][1] * y0, Q[1][0] * x0 + Q[1][1] * y0
    X1, Y1 = Q[0][0] * x1 + Q[0][1] * y1, Q[1][0] * x1 + Q[1][1] * y1
    # in rotated frame the ray is x = -eps (v rotated to (-1,0)), y > 0; use x = -eps
    xr = -eps
    cnt = 0
    for a0, b0, a1, b1 in zip(X0, Y0, X1, Y1):
        if (a0 - xr) * (a1 - xr) < 0:
            t = (xr - a0) / (a1 - a0)
            if b0 + t * (b1 - b0) > 0:
                cnt += 1 if a1 > a0 else -1      # +x in rotated frame = clockwise
    return cnt


def orbits(pi):
    n = len(pi)
    seen = np.zeros(n, bool)
    out = []
    for s in range(n):
        if seen[s] or pi[s] == s:
            seen[s] = True
            continue
        cyc = []
        t = s
        while not seen[t]:
            seen[t] = True
            cyc.append(t)
            t = pi[t]
        out.append(cyc)
    return out


def orbit_winding(L, path, cyc, c):
    """winding (ccw +) of one orbit of pi around c, from the items' actual sub-step paths"""
    tot = 0.0
    for s in cyc:
        x, y = rel(L, path[:, s], c)
        th = np.arctan2(y, x)
        tot += wrap(np.diff(th)).sum()
    return tot / (2 * math.pi)


def box(L, x0, y0, w, h):
    lk = np.zeros(L * L, bool)
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            lk[(y % L) * L + (x % L)] = True
    return lk


def cheb_dist_to_locked(L, locked):
    xs, ys = coords(L)
    lx, ly = xs[locked], ys[locked]
    d = np.full(L * L, 10 ** 9)
    for a, b in zip(lx, ly):
        dd = np.maximum(np.abs(mi(xs - a, L)), np.abs(mi(ys - b, L)))
        d = np.minimum(d, dd)
    return d
