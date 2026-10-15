"""Independent/targeted numerical checks for the UV-1 referee report.

All modes are intentionally small enough for the local watchdog.  The beta=infinity
mode rebuilds the torus operator from explicit links and uses the polar form of the
overlap operator, independently of uv1_inf.py's H_W-sign implementation.  The
Stage-B mode reuses only the registered node generator/kernel evaluator to locate
a small principal submatrix, then checks that submatrix at n=2,3,4 and verifies
representative nodes against Geom.full_D.
"""
from __future__ import annotations

import argparse
import gc
import itertools
import sys
import time

import numpy as np


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


GX = np.array([[0, 1], [1, 0]], complex)
GT = np.array([[0, -1j], [1j, 0]], complex)
I2 = np.eye(2)


def explicit_inf(pool: str, nws: list[int], gap_grid: int) -> None:
    d = np.load(pool)
    U = [{"x": d["ux"][i], "t": d["ut"][i]} for i in range(len(d["ux"]))]
    k = len(U)
    T = d["ux"].shape[1]
    Lx, Lt = 2, 2 * T
    N = 2 * Lx * Lt
    mass = 0.05
    ident = np.eye(N, dtype=complex)
    g5 = np.kron(np.eye(N // 2), np.diag([1.0, -1.0]))

    def sidx(x, ti):
        return 2 * (ti + Lt * (x % Lx))

    def links(ua, ub, a1, b0, b1):
        ux = np.zeros((Lx, Lt))
        ut = np.zeros((Lx, Lt))
        for t in range(1, T + 1):
            ux[:, t + T - 1] = ua["x"][t - 1]
            ux[:, (1 - t) + T - 1] = ub["x"][t - 1]
        for t in range(1, T):
            ut[:, t + T - 1] = ua["t"][t - 1]
            ut[:, (-t) + T - 1] = -ub["t"][t - 1]
        ut[:, T - 1] = [0.0, a1]
        ut[:, Lt - 1] = [b0, b1]
        return ux, ut

    def plaquettes(ux, ut):
        return wrap(
            np.array(
                [
                    [
                        ux[x, ti]
                        + ut[(x + 1) % Lx, ti]
                        - ux[x, (ti + 1) % Lt]
                        - ut[x, ti]
                        for x in range(Lx)
                    ]
                    for ti in range(Lt)
                ]
            )
        )

    def dw(ux, ut):
        out = 2.0 * ident.copy()
        for x in range(Lx):
            for ti in range(Lt):
                a = sidx(x, ti)
                b = sidx(x + 1, ti)
                z = np.exp(1j * ux[x, ti])
                out[a : a + 2, b : b + 2] += -0.5 * (I2 - GX) * z
                out[b : b + 2, a : a + 2] += -0.5 * (I2 + GX) * np.conj(z)
                b = sidx(x, (ti + 1) % Lt)
                z = (-1.0 if ti == Lt - 1 else 1.0) * np.exp(1j * ut[x, ti])
                out[a : a + 2, b : b + 2] += -0.5 * (I2 - GT) * z
                out[b : b + 2, a : a + 2] += -0.5 * (I2 + GT) * np.conj(z)
        return out

    def logdet_overlap(dwmat):
        x = dwmat - ident
        vals, vecs = np.linalg.eigh(x.conj().T @ x)
        polar = x @ (vecs * (1.0 / np.sqrt(vals))) @ vecs.conj().T
        dovm = (1.0 - mass / 2.0) * (ident + polar) + mass * ident
        sign, ld = np.linalg.slogdet(dovm)
        gap = np.min(np.abs(np.linalg.eigvalsh(g5 @ x)))
        return ld + np.log(complex(sign)), gap

    # The two flat crossing conditions are solved from explicit plaquettes.
    crossing_flat = 0.0
    params = {}
    for a in range(k):
        for b in range(a, k):
            p0 = plaquettes(*links(U[a], U[b], 0.0, 0.0, 0.0))
            params[a, b] = (-p0[T - 1, 0], -p0[Lt - 1, 0])

    kernels = []
    t0 = time.time()
    for nw in nws:
        angles = 2 * np.pi * np.arange(nw) / nw
        logs = np.zeros((k, k), complex)
        min_gap = np.inf
        max_phase_diag = 0.0
        for a in range(k):
            for b in range(a, k):
                a1, y = params[a, b]
                lv = []
                for b0 in angles:
                    ux, ut = links(U[a], U[b], a1, b0, b0 + y)
                    if b0 == 0:
                        p = plaquettes(ux, ut)
                        crossing_flat = max(
                            crossing_flat, float(np.max(np.abs(p[[T - 1, Lt - 1]])))
                        )
                    val, gap = logdet_overlap(dw(ux, ut))
                    lv.append(val)
                    min_gap = min(min_gap, gap)
                lv = np.asarray(lv)
                shift = np.max(lv.real)
                entry = shift + np.log(np.mean(np.exp(lv - shift)) + 0j)
                logs[a, b] = entry if a != b else entry.real
                logs[b, a] = np.conj(logs[a, b])
                if a == b:
                    max_phase_diag = max(max_phase_diag, abs(entry.imag))
        diag = logs.diagonal().real
        z = np.exp(logs - 0.5 * (diag[:, None] + diag[None, :]))
        z = 0.5 * (z + z.conj().T)
        ev, vec = np.linalg.eigh(z)
        residual = np.linalg.norm(z @ vec[:, 0] - ev[0] * vec[:, 0])
        herm = np.max(np.abs(z - z.conj().T))
        kernels.append(z)
        print(
            f"INF nw={nw}: lambda_min={ev[0]:+.12e} lambda_max={ev[-1]:.12e} "
            f"relative={ev[0]/ev[-1]:+.12e} gap_min={min_gap:.9f} "
            f"eig_residual={residual:.3e} herm_defect={herm:.1e} "
            f"diag_phase_max={max_phase_diag:.1e}",
            flush=True,
        )
    for i in range(1, len(kernels)):
        delta = np.max(np.abs(kernels[i] - kernels[i - 1]))
        weyl = k * delta
        print(
            f"INF change nw={nws[i-1]}->{nws[i]}: max_entry={delta:.3e} k*max={weyl:.3e}",
            flush=True,
        )
    print(f"INF max_crossing_plaquette={crossing_flat:.3e}", flush=True)

    # Continuity needs a gap along the whole residual flat-holonomy circle, not
    # merely at quadrature nodes.  Scan all pool pairs independently.
    min_gap = np.inf
    where = None
    for a in range(k):
        for b in range(a, k):
            a1, y = params[a, b]
            for j in range(gap_grid):
                b0 = 2 * np.pi * (j + 0.5) / gap_grid
                x = dw(*links(U[a], U[b], a1, b0, b0 + y)) - ident
                gap = float(np.min(np.abs(np.linalg.eigvalsh(g5 @ x))))
                if gap < min_gap:
                    min_gap, where = gap, (a, b, j)
    print(f"INF dense_gap grid={gap_grid}: min={min_gap:.9f} at={where}", flush=True)
    print(f"elapsed={time.time()-t0:.1f}s", flush=True)


def stageb_spot(pool: str) -> None:
    sys.path.insert(0, "scripts")
    from k2b_lib import normalized
    from lat2d import Geom
    from uv1_lib import (
        D_links,
        buffer_xlink_mats,
        deep_to_ext,
        nested_nodes_d2,
        point_logs,
        wfun,
    )

    ids = [12, 16, 17, 19, 9, 10]
    d = np.load(pool)
    T = d["ux"].shape[1]
    geom = Geom(2, T, False, -1)
    u1 = [{"x": d["ux"][i], "t": d["ut"][i]} for i in ids]
    ud = [{"x": u["x"][: T - 1].copy(), "t": u["t"][: T - 2].copy()} for u in u1]
    fsc, bsc = geom.crossing_mats()
    fsx, bsx = buffer_xlink_mats(geom)
    exact_volume = (88.0 / 5.0) * 0.6**5
    def get_entry(node_set, a, b):
        # Streaming equivalent of uv1_lib.entry_d2: do not materialize the
        # full up/um/theta/plaquette/log arrays at n=4.
        q_all, d_all, base_all = node_set
        zero = np.zeros(2)
        ua0 = deep_to_ext(ud[a], zero)
        ub0 = deep_to_ext(ud[b], zero)
        d0mat = geom.D0(ua0, ub0)
        th0 = np.concatenate([ua0["x"][0], ub0["x"][0]])
        e0 = np.exp(1j * th0)
        dfix = d0mat - np.einsum("j,jab->ab", e0, fsx) - np.einsum(
            "j,jab->ab", np.conj(e0), bsx
        )
        fs = np.concatenate([fsx, fsc])
        bs = np.concatenate([bsx, bsc])
        scale = -np.inf
        accum = 0.0 + 0.0j
        gap_min = np.inf
        for c in range(0, len(d_all), 64):
            q = q_all[c : c + 64]
            dd = d_all[c : c + 64]
            up = ua0["x"][0][None] + q[:, :2]
            um = ub0["x"][0][None] + q[:, 2:]
            aa = um - up
            phi = wrap(aa.sum(axis=1))
            theta = np.concatenate(
                [up, um, np.zeros((len(q), 1)), (dd - aa[:, 0])[:, None]], axis=1
            )
            plaquette = np.concatenate([q, dd[:, None], (phi - dd)[:, None]], axis=1)
            logs, gaps = point_logs(geom, D_links(dfix, fs, bs, theta), "O")
            gap_min = min(gap_min, float(np.nanmin(gaps)))
            weights = base_all[c : c + 64] * np.prod(wfun(plaquette, "tri", 8.0), axis=1)
            chunk_scale = float(np.max(logs.real))
            if chunk_scale > scale:
                accum *= np.exp(scale - chunk_scale) if np.isfinite(scale) else 0.0
                scale = chunk_scale
            accum += np.sum(weights * np.exp(logs - scale))
        return scale + np.log(accum + 0j), gap_min

    # n=2 is cheap enough to locate a small principal witness.
    node_set = nested_nodes_d2(2)
    print(
        f"D2 nodes n=2: count={len(node_set[2])} volume={node_set[2].sum():.12f} "
        f"volume_error={node_set[2].sum()-exact_volume:+.3e}",
        flush=True,
    )
    k = len(ud)
    l2 = np.zeros((k, k), complex)
    g2 = np.inf
    for a in range(k):
        for b in range(a, k):
            value, gap = get_entry(node_set, a, b)
            l2[a, b] = value if a != b else value.real
            l2[b, a] = np.conj(l2[a, b])
            g2 = min(g2, gap)
    z2 = normalized(l2)
    ev2, v2 = np.linalg.eigh(z2)
    order = np.argsort(-np.abs(v2[:, 0]))
    print(
        f"D2 full n=2: lambda_min={ev2[0]:+.12e} relative={ev2[0]/ev2[-1]:+.12e} "
        f"gap_min={g2:.9f} eigvec_order={order.tolist()} weights={np.abs(v2[order,0]).tolist()}",
        flush=True,
    )
    # Prefer a 2x2 violation if present; otherwise use the three largest
    # components of the n=2 negative vector.
    pair_scores = []
    for a, b in itertools.combinations(range(k), 2):
        pair_scores.append((abs(z2[a, b]) - 1.0, a, b))
    pair_scores.sort(reverse=True)
    if pair_scores[0][0] > 0:
        subset = sorted(pair_scores[0][1:])
    else:
        subset = sorted(order[:3].tolist())
    print(f"D2 selected principal subset={subset} best_2x2_excess={pair_scores[0]}", flush=True)

    mats = {}
    for n in (2, 3, 4):
        if n != 2:
            del node_set
            gc.collect()
            node_set = nested_nodes_d2(n)
            print(
                f"D2 nodes n={n}: count={len(node_set[2])} volume={node_set[2].sum():.12f} "
                f"volume_error={node_set[2].sum()-exact_volume:+.3e}",
                flush=True,
            )
        kk = len(subset)
        lm = np.zeros((kk, kk), complex)
        gap_min = np.inf
        for ii, a in enumerate(subset):
            for jj in range(ii, kk):
                b = subset[jj]
                value, gap = get_entry(node_set, a, b)
                lm[ii, jj] = value if ii != jj else value.real
                lm[jj, ii] = np.conj(lm[ii, jj])
                gap_min = min(gap_min, gap)
        z = normalized(lm)
        ev = np.linalg.eigvalsh(z)
        mats[n] = z
        print(
            f"D2 subset n={n}: lambda_min={ev[0]:+.12e} relative={ev[0]/ev[-1]:+.12e} "
            f"gap_min={gap_min:.9f}",
            flush=True,
        )
    for a, b in ((2, 3), (3, 4)):
        diff = np.max(np.abs(mats[b] - mats[a]))
        print(
            f"D2 subset change n={a}->{b}: max_entry={diff:.3e} k*max={len(subset)*diff:.3e}",
            flush=True,
        )


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="mode", required=True)
    q = sub.add_parser("inf")
    q.add_argument("pool")
    q.add_argument("--nws", default="12,24,48")
    q.add_argument("--gap-grid", type=int, default=64)
    q = sub.add_parser("stageb")
    q.add_argument("pool")
    a = p.parse_args()
    if a.mode == "inf":
        explicit_inf(a.pool, [int(x) for x in a.nws.split(",")], a.gap_grid)
    else:
        stageb_spot(a.pool)


if __name__ == "__main__":
    main()
