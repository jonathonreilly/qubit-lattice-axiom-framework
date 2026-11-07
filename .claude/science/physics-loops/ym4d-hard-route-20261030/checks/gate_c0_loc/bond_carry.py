#!/usr/bin/env python3
"""Kill test of (4.1b) and the row part of (3.4) of library/c0-loc.md; criteria in CRITERIA.md.
A run refutes or guides, never discharges."""
import importlib.util
import itertools
import pathlib

import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("pc", here.parent / "gate_lc_u" / "path_coarsening.py")
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)

L = 3
ID = np.array([1.0, 0, 0, 0])


def gauge(U, seed):
    """Random fine gauge transformation."""
    N = U.shape[1]
    rng = np.random.default_rng(seed)
    g = rng.normal(size=(N,) * 4 + (4,))
    g /= np.linalg.norm(g, axis=-1, keepdims=True)
    out = np.zeros_like(U)
    for mu in range(4):
        out[mu] = pc.qmul(pc.qmul(g, U[mu]), pc.qconj(np.roll(g, -1, axis=mu)))
    return out


def hol(V, start, steps):
    N = V.shape[1]
    h, _ = pc.walk(V, [np.array(int(start[i]) % N) for i in range(4)], steps)
    return h


def dist(a, b):
    return float(min(np.linalg.norm(a - b), np.linalg.norm(a + b)))


def centre(y):
    return tuple(3 * c + 1 for c in y)


def parent(q):
    return tuple(c // 3 for c in q)


def patch_E(th4_cells):
    """l^4 norm on the 3^4 window of level-(j+1) cells around each cell, plus the next along any mu."""
    acc = np.zeros_like(th4_cells)
    for sh in itertools.product((-2, -1, 0, 1, 2), repeat=4):
        acc += np.roll(th4_cells, sh, axis=(0, 1, 2, 3))
    return acc ** 0.25


def level_data(Vs):
    out = []
    for j in range(len(Vs) - 1):
        th = pc.plaq_angles(Vs[j])
        th4 = np.sum(th ** 4, axis=0)
        nc = th4.shape[0] // 3
        cells = th4.reshape(nc, 3, nc, 3, nc, 3, nc, 3).sum(axis=(1, 3, 5, 7))
        out.append(patch_E(cells))
    return out


def term(Vs, Ed, r, y, mu, rng):
    """One random kernel term of row (y, mu) at level r. Returns T, x0, B1 ratio, err sum, the
    chain data for the prediction, and delta_r."""
    N0 = Vs[0].shape[1]
    # descend: choose x_j, t_j
    ys = {r: tuple(y)}
    choice = {}
    for j in range(r - 1, -1, -1):
        d = tuple(int(c) for c in rng.integers(-1, 2, 4))
        t = int(rng.integers(0, L))
        x = tuple(centre(ys[j + 1])[i] + d[i] for i in range(4))
        tail = list(x)
        tail[mu] += t
        choice[j] = (d, t, x, tuple(tail))
        ys[j] = tuple(tail)
    # composite transport, top down: p_(r-1) ... p_0
    T = ID.copy()
    ps = {}
    for j in range(r - 1, -1, -1):
        d, t, x, tl = choice[j]
        steps = pc.contour_steps(d) + [(mu, 1)] * t
        ps[j] = hol(Vs[j], centre(ys[j + 1]), steps)
        T = pc.qmul(T, ps[j])
    # ascend with the flag
    q = {0: ys[0]}
    delta = {0: 0}
    errs = []
    ratio = 0.0
    gammas = []
    for j in range(r):
        qp = parent(q[j])
        dlt = qp[mu] - ys[j + 1][mu]
        assert dlt in (0, 1), (dlt, qp, ys[j + 1])
        for i in range(4):
            if i != mu:
                assert qp[i] == ys[j + 1][i]
        delta[j + 1] = dlt
        q[j + 1] = qp
        lhs = ps[j]
        if delta[j]:
            lhs = pc.qmul(lhs, hol(Vs[j], ys[j], [(mu, 1)]))
        c = tuple(q[j][i] - centre(qp)[i] for i in range(4))
        g = hol(Vs[j], centre(qp), pc.contour_steps(c))
        gammas.append(g)
        rhs = g
        if dlt:
            rhs = pc.qmul(hol(Vs[j + 1], ys[j + 1], [(mu, 1)]), g)
        e = dist(lhs, rhs)
        errs.append(e)
        nc = Ed[j].shape[0]
        Ebd = float(Ed[j][tuple(c % nc for c in ys[j + 1])])
        if Ebd > 0:
            ratio = max(ratio, e / (2 ** 14 * L ** 2 * Ebd))
    # prediction: V_r^delta_r Gamma_(r-1) ... Gamma_0
    chain = ID.copy()
    for g in reversed(gammas):
        chain = pc.qmul(chain, g)
    if delta[r]:
        pred = pc.qmul(hol(Vs[r], ys[r], [(mu, 1)]), chain)
    else:
        pred = chain
    x0 = tuple(c % N0 for c in ys[0])
    return T, x0, ratio, sum(errs), dist(T, pred), dist(T, chain), delta[r]


def run(kind, N, r, target, seed=11, rows=12, terms=120):
    U0 = pc.tuned_field(kind, N, target, seed)
    a = pc.a_of(U0)
    U = gauge(U0, seed + 1)
    Vs = pc.chain(U)
    Ed = level_data(Vs)
    rng = np.random.default_rng(seed + 2)
    z = tuple(int(c) for c in rng.integers(0, N, 4))
    J = pc.axis_frame(U, z)
    S = 0.0
    b1 = 0.0
    b2_ok = True
    b2_max = 0.0
    ctrl = []
    nc = Vs[r].shape[1]
    for _ in range(rows):
        y = tuple(int(c) for c in rng.integers(0, nc, 4))
        mu = int(rng.integers(0, 4))
        base = None
        for _ in range(terms):
            T, x0, ratio, es, e_comp, e_drop, dl = term(Vs, Ed, r, y, mu, rng)
            b1 = max(b1, ratio)
            b2_max = max(b2_max, e_comp)
            if e_comp > es + 1e-9:
                b2_ok = False
            if dl:
                ctrl.append((e_drop, e_comp))
            w = pc.qmul(T, pc.qconj(J[x0]))
            if base is None:
                base = w
            S = max(S, dist(w, base))
        pc.guard()
    drop = min(c[0] for c in ctrl) if ctrl else float("nan")
    comp = max(c[1] for c in ctrl) if ctrl else float("nan")
    row = dict(kind=kind, N=N, r=r, target=target, a=round(a, 6), S=S, S_over_a=S / a, b1=b1,
               b2_ok=b2_ok, b2_max=b2_max, n_carry=len(ctrl), drop_min=drop, comp_max=comp)
    print(row, flush=True)
    return row


def main():
    rows = []
    for kind in ("smooth", "tube", "noise"):
        for N, r in ((9, 1), (27, 1), (27, 2)):
            for t in (0.02, 0.01):
                rows.append(run(kind, N, r, t))

    def get(k, n, r, t):
        return next(x for x in rows if (x["kind"], x["N"], x["r"], x["target"]) == (k, n, r, t))

    fails = []
    for x in rows:
        if x["b1"] > 1:
            fails.append(("B1", x["kind"], x["N"], x["r"], x["b1"]))
        if not x["b2_ok"]:
            fails.append(("B2", x["kind"], x["N"], x["r"]))
        if x["n_carry"] == 0 or x["drop_min"] < 100 * x["comp_max"]:
            fails.append(("B5 void", x["kind"], x["N"], x["r"], x["drop_min"], x["comp_max"]))
    for k in ("smooth", "tube", "noise"):
        s1 = get(k, 9, 1, 0.01)["S_over_a"]
        s2 = get(k, 27, 2, 0.01)["S_over_a"]
        if s2 > 2 * s1:
            fails.append(("B3", k, s1, s2))
        s3 = get(k, 27, 2, 0.02)["S_over_a"]
        if abs(s3 - s2) > 0.25 * s2:
            fails.append(("B4", k, s3, s2))
    print("FAILS:", fails if fails else "none")
    print("VERDICT:", "FAIL" if fails else "PASS")


if __name__ == "__main__":
    main()
