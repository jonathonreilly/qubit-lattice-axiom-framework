#!/usr/bin/env python3
"""Kill test of lc-u.md Section 5; criteria in CRITERIA.md. A run refutes or guides, never discharges."""
import itertools
import resource
import sys

import numpy as np

L = 3
RSS_LIMIT = 2 * 1024 ** 3


def guard():
    # ru_maxrss is in bytes on darwin
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT:
        sys.exit("RSS above 2 GB, stopping")


def qmul(a, b):
    w = a[..., 0] * b[..., 0] - np.sum(a[..., 1:] * b[..., 1:], axis=-1)
    v = (a[..., 0, None] * b[..., 1:] + b[..., 0, None] * a[..., 1:]
         + np.cross(a[..., 1:], b[..., 1:]))
    return np.concatenate([w[..., None], v], axis=-1)


def qconj(a):
    return np.concatenate([a[..., :1], -a[..., 1:]], axis=-1)


def qlog(a):
    n = np.linalg.norm(a[..., 1:], axis=-1)
    th = np.arctan2(n, a[..., 0])
    f = np.where(n > 1e-14, th / np.maximum(n, 1e-300), 1.0)
    return a[..., 1:] * f[..., None]


def qexp(v):
    th = np.linalg.norm(v, axis=-1)
    f = np.where(th > 1e-14, np.sin(th) / np.maximum(th, 1e-300), 1.0)
    return np.concatenate([np.cos(th)[..., None], v * f[..., None]], axis=-1)


def walk(U, pos, steps):
    """Holonomy along steps from pos, an index tuple of arrays, with periodic wrap."""
    N = U.shape[1]
    pos = [p.copy() for p in pos]
    h = np.zeros(pos[0].shape + (4,))
    h[..., 0] = 1.0
    for mu, sg in steps:
        if sg > 0:
            h = qmul(h, U[mu][tuple(pos)])
            pos[mu] = (pos[mu] + 1) % N
        else:
            pos[mu] = (pos[mu] - 1) % N
            h = qmul(h, qconj(U[mu][tuple(pos)]))
    return h, pos


def contour_steps(delta):
    s = []
    for mu in range(4):
        s += [(mu, 1 if delta[mu] > 0 else -1)] * abs(delta[mu])
    return s


def rev(steps):
    return [(mu, -sg) for mu, sg in reversed(steps)]


DELTAS = list(itertools.product((-1, 0, 1), repeat=4))


def block_map(U):
    N = U.shape[1]
    Nc = N // L
    k = np.indices((Nc,) * 4)
    y = [3 * k[i] + 1 for i in range(4)]
    out = np.zeros((4,) + (Nc,) * 4 + (4,))
    for mu in range(4):
        om0, _ = walk(U, y, [(mu, 1)] * L)
        acc = np.zeros((Nc,) * 4 + (3,))
        for d in DELTAS:
            cs = contour_steps(d)
            steps = cs + [(mu, 1)] * L + rev(cs)
            om, _ = walk(U, y, steps)
            acc += qlog(qmul(om, qconj(om0)))
        out[mu] = qmul(qexp(acc / len(DELTAS)), om0)
        guard()
    return out


def plaq_angles(U):
    N = U.shape[1]
    idx = np.indices((N,) * 4)
    res = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            h, _ = walk(U, [idx[i] for i in range(4)], [(mu, 1), (nu, 1), (mu, -1), (nu, -1)])
            res.append(np.linalg.norm(qlog(h), axis=-1))
    return np.stack(res)  # shape (6, N, N, N, N)


def field(kind, N, amp, rng):
    x = np.indices((N,) * 4) / N
    A = np.zeros((4,) + (N,) * 4 + (3,))
    if kind == "smooth":
        for mu in range(4):
            for _ in range(4):
                m = rng.integers(-2, 3, 4)
                ph = rng.uniform(0, 2 * np.pi)
                n = rng.normal(size=3)
                A[mu] += (np.cos(2 * np.pi * np.tensordot(m, x, axes=(0, 0)) + ph)[..., None]
                          * n / np.linalg.norm(n))
    elif kind == "tube":
        c = (N // 2, N // 2, N // 2, N // 2)
        idx = np.indices((N,) * 4)
        r3 = np.sqrt(sum((idx[i] - c[i]) ** 2 for i in (0, 1, 2)))
        r2 = np.sqrt(sum((idx[i] - c[i]) ** 2 for i in (0, 1, 3)))
        A[3] += np.maximum(0, 1 - r3 / 2.0)[..., None] * np.array([0, 0, 1.0])
        A[2] += np.maximum(0, 1 - r2 / 2.0)[..., None] * np.array([1.0, 0, 0])
    elif kind == "noise":
        A = rng.normal(size=A.shape)
    else:
        raise ValueError(kind)
    return qexp(amp * A / N)


def a_of(U):
    N = U.shape[1]
    return N * np.sum(plaq_angles(U) ** 4) ** 0.25


def tuned_field(kind, N, target, seed):
    amp = 1.0
    for _ in range(6):
        U = field(kind, N, amp, np.random.default_rng(seed))
        amp *= target / a_of(U)
    return field(kind, N, amp, np.random.default_rng(seed))


def chain(U):
    Vs = [U]
    while Vs[-1].shape[1] > L:
        Vs.append(block_map(Vs[-1]))
    return Vs


def parent(i):
    return i // 3


def transport_to_all(Vs, order=(0, 1, 2, 3)):
    """C[j]: hierarchical transport from the top root to each level-j site. Root is the centre of level m-1."""
    m = len(Vs)
    top = Vs[-1].shape[1]  # L
    C = np.zeros((top,) * 4 + (4,))
    k0 = (1, 1, 1, 1)  # centre of the top block, index in level m-1
    # level m-1: one contour from the root
    idx = np.indices((top,) * 4)
    for d in DELTAS:
        cs = []
        for mu in order:
            cs += [(mu, 1 if d[mu] > 0 else -1)] * abs(d[mu])
        site = tuple(k0[i] + d[i] for i in range(4))
        h, _ = walk(Vs[-1], [np.array(k0[i]) for i in range(4)], cs)
        C[site] = h
    for j in range(m - 2, -1, -1):
        Nj = Vs[j].shape[1]
        next_C = np.zeros((Nj,) * 4 + (4,))
        k = np.indices((Nj // L,) * 4)
        for d in DELTAS:
            cs = []
            for mu in order:
                cs += [(mu, 1 if d[mu] > 0 else -1)] * abs(d[mu])
            y = [3 * k[i] + 1 for i in range(4)]
            h, _ = walk(Vs[j], y, cs)
            sel = tuple(3 * k[i] + 1 + d[i] for i in range(4))
            next_C[sel] = qmul(C[tuple(k[i] for i in range(4))], h)
        C = next_C
        guard()
    return C


def axis_frame(U, z):
    """hol(z to x) by axis-ordered path, axes 0, 1, 2, 3 in turn, no wrap, for all x."""
    N = U.shape[1]
    h = np.zeros((N,) * 4 + (4,))
    h[tuple(z)] = (1, 0, 0, 0)
    filled = [z[0:1]]
    # sweep each axis in turn from the plane already filled
    for mu in range(4):
        sl = [slice(None)] * 4
        for i in range(mu + 1, 4):
            sl[i] = z[i]
        for t in range(z[mu] + 1, N):
            s_to = list(sl); s_to[mu] = t
            s_fr = list(sl); s_fr[mu] = t - 1
            h[tuple(s_to)] = qmul(h[tuple(s_fr)], U[mu][tuple(s_fr)])
        for t in range(z[mu] - 1, -1, -1):
            s_to = list(sl); s_to[mu] = t
            s_fr = list(sl); s_fr[mu] = t + 1
            h[tuple(s_to)] = qmul(h[tuple(s_fr)], qconj(U[mu][tuple(s_to)]))
    return h


def path_steps(p, q):
    s = []
    for mu in range(4):
        dlt = int(q[mu]) - int(p[mu])
        s += [(mu, 1 if dlt > 0 else -1)] * abs(dlt)
    return s


def hol_points(V, pts):
    h = np.array([1.0, 0, 0, 0])
    for a, b in zip(pts[:-1], pts[1:]):
        hh, _ = walk(V, [np.array(int(a[i])) for i in range(4)], path_steps(a, b))
        h = qmul(h, hh)
    return h


def anc(p):
    return tuple(int(c) // 3 for c in p)


def cell_max_along(theta_cells, pts):
    """Sum over level-(j+1) cells met by the path of the largest level-j angle in the two-block patch."""
    total = 0.0
    n = theta_cells.shape[0]
    for a, b in zip(pts[:-1], pts[1:]):
        for mu in range(4):
            lo, hi = sorted((int(a[mu]), int(b[mu])))
            for t in range(lo // 3, hi // 3 + 1):
                c = [int(a[i]) // 3 if i > mu else int(b[i]) // 3 for i in range(4)]
                c[mu] = t
                w = [((c[i] + e) % n for e in (-1, 0, 1)) for i in range(4)]
                total += max(theta_cells[g] for g in itertools.product(*[list(u) for u in w]))
    return total


def main():
    rows = []
    for kind, N, target in [(k, n, t) for k in ("smooth", "tube", "noise")
                            for n in (9, 27) for t in (0.02, 0.01)]:
        U = tuned_field(kind, N, target, 11)
        a = a_of(U)
        Vs = chain(U)
        m = len(Vs)
        s = [L ** j / N for j in range(m)]
        Es = [np.sum(plaq_angles(V) ** 4) ** 0.25 for V in Vs]
        ratios = [Es[j] / (s[j] * a) for j in range(m)]
        C = transport_to_all(Vs)
        root = tuple([N // 2] * 4)
        worst = 0.0
        k4_ratio = 0.0
        k4_sum_ok = True
        rng = np.random.default_rng(5)
        zs = [tuple(rng.integers(0, N, 4)) for _ in range(5)] + [root]
        for z in zs:
            J = axis_frame(U, z)
            O = hol_points(U, [root, z])
            T = np.linalg.norm(C - qmul(O, J), axis=-1)
            T = np.minimum(T, np.linalg.norm(C + qmul(O, J), axis=-1))
            worst = max(worst, float(T.max()))
            # level by level at the worst x
            xw = np.unravel_index(int(np.argmax(T)), T.shape)
            p = [root, z, tuple(int(c) for c in xw)]
            Tp = float(T[xw])
            errs = []
            for j in range(m - 1):
                hj = hol_points(Vs[j], p)
                q = [anc(c) for c in p]
                hk = hol_points(Vs[j + 1], q)
                x_, y_ = p[2], q[2]
                d = tuple(int(x_[i]) - (3 * y_[i] + 1) for i in range(4))
                g, _ = walk(Vs[j], [np.array(3 * y_[i] + 1) for i in range(4)], contour_steps(d))
                e = float(min(np.linalg.norm(hj - qmul(hk, g)), np.linalg.norm(hj + qmul(hk, g))))
                errs.append(e)
                th = plaq_angles(Vs[j]).max(axis=0)
                nc = th.shape[0] // 3
                cells = th.reshape(nc, 3, nc, 3, nc, 3, nc, 3).max(axis=(1, 3, 5, 7))
                bound = (L ** 2) * cell_max_along(cells, p)
                if bound > 0:
                    k4_ratio = max(k4_ratio, e / bound)
                p = q
            # top level: path inside one block against the contour from the root
            q = p
            ht = hol_points(Vs[m - 1], q)
            d = tuple(int(q[2][i]) - 1 for i in range(4))
            gt, _ = walk(Vs[m - 1], [np.array(1)] * 4, contour_steps(d))
            errs.append(float(min(np.linalg.norm(ht - gt), np.linalg.norm(ht + gt))))
            if sum(errs) + 1e-12 < Tp:
                k4_sum_ok = False
            guard()
        row = dict(kind=kind, N=N, target=target, a=a, T=worst, T_over_a=worst / a,
                   ratios=[round(float(r), 4) for r in ratios], k4=k4_ratio, k4_sum_ok=k4_sum_ok)
        rows.append(row)
        print(row, flush=True)
    # criteria
    def get(k, n, t):
        return next(r for r in rows if r["kind"] == k and r["N"] == n and r["target"] == t)
    fails = []
    for r in rows:
        if r["target"] == 0.01 and max(r["ratios"]) > 1.25:
            fails.append(("K1", r["kind"], r["N"], max(r["ratios"])))
        if r["k4"] > 2 ** 12:
            fails.append(("K4 bound", r["kind"], r["N"], r["k4"]))
        if not r["k4_sum_ok"]:
            fails.append(("K4 sum", r["kind"], r["N"]))
    for k in ("smooth", "tube", "noise"):
        a2, a1 = get(k, 27, 0.02)["T_over_a"], get(k, 27, 0.01)["T_over_a"]
        if abs(a2 - a1) > 0.25 * a1:
            fails.append(("K2", k, a2, a1))
        d2, d3 = get(k, 9, 0.01)["T_over_a"], get(k, 27, 0.01)["T_over_a"]
        if d3 > 2 * d2:
            fails.append(("K3", k, d2, d3))
    print("FAILS:", fails if fails else "none")
    print("VERDICT:", "FAIL" if fails else "PASS", "(K5 not coded in this run)")


if __name__ == "__main__":
    main()
