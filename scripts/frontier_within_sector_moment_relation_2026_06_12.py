#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/WITHIN_SECTOR_MOMENT_RELATION_WRAPPED_GAUSSIAN_CONSISTENT_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_within_sector_moment_relation_2026_06_12.py
"""

from __future__ import annotations

import sys

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


NC = 3
LRING = 3
K_OCC = 5
EPS = 0.6
TAU = 0.35
RANK_TOL = 1.0e-8
NO_PRUNE_TOL = 1.0e-14
WEIGHT_SUM_TOL = 1.0e-10
ANCHOR_TOL = 5.0e-3
KPREF = 3
N_SECTORS = 2 ** KPREF
DEPTH_CAP = 12
SEEDS = (4242, 99, 7)
NULL_SEED = 7777
NULL_DRAWS = 300
CONTROL_DRAWS = 100
DELTA_SCALE = 0.05


def build_l3() -> dict[str, object]:
    nm = LRING * NC
    dim = 2 ** nm
    sz = np.array([[1.0, 0.0], [0.0, -1.0]])
    sm = np.array([[0.0, 1.0], [0.0, 0.0]])
    i2 = np.eye(2)

    def ann(j: int) -> np.ndarray:
        out = np.array([[1.0]])
        for k in range(nm):
            one = sz if k < j else (sm if k == j else i2)
            out = np.kron(out, one)
        return out.astype(complex)

    a_ops = [ann(j) for j in range(nm)]
    ad_ops = [a.T for a in a_ops]
    h = np.zeros((nm, nm))
    for x in range(LRING):
        for c in range(NC):
            h[x * NC + c, ((x + 1) % LRING) * NC + c] = -1.0
            h[((x + 1) % LRING) * NC + c, x * NC + c] = -1.0

    h_fock = np.zeros((dim, dim), dtype=complex)
    for i in range(nm):
        for j in range(nm):
            if abs(h[i, j]) > 1.0e-12:
                h_fock += h[i, j] * (ad_ops[i] @ a_ops[j])
    evals, evecs = np.linalg.eigh(h_fock)
    u_step = (evecs * np.exp((-1j * TAU) * evals)) @ evecs.conj().T

    n0_diag = sum(np.diag(ad_ops[c] @ a_ops[c]).real for c in range(NC))
    nt = (n0_diag - n0_diag.mean()) / max(abs(n0_diag - n0_diag.mean()))
    kp_diag = np.sqrt((1.0 + EPS * nt) / 2.0).astype(complex)
    km_diag = np.sqrt((1.0 - EPS * nt) / 2.0).astype(complex)
    ops = [(ad_ops[i] @ a_ops[NC + j]).astype(complex) for i in range(3) for j in range(3)]

    ntot_diag = sum(np.diag(ad_ops[m] @ a_ops[m]).real for m in range(nm))
    vac_idx = int(np.argmin(ntot_diag))
    return {
        "NM": nm,
        "DIM": dim,
        "AD": ad_ops,
        "U": u_step,
        "kp": kp_diag,
        "km": km_diag,
        "OPS": ops,
        "vac_idx": vac_idx,
    }


def polar_u(mat: np.ndarray) -> np.ndarray:
    u, _, vh = np.linalg.svd(mat)
    return u @ vh


def slater(env: dict[str, object], p: np.ndarray) -> np.ndarray:
    dim = int(env["DIM"])
    vac = np.zeros(dim)
    vac[int(env["vac_idx"])] = 1.0
    psi = vac.astype(complex)
    ad_ops = env["AD"]
    nm = int(env["NM"])
    for k in range(p.shape[1]):
        psi = sum(ad_ops[m] @ (p[m, k] * psi) for m in range(nm))
    return psi / np.linalg.norm(psi)


def dets_of(env: dict[str, object], states: np.ndarray) -> tuple[np.ndarray, float]:
    b = states.shape[0]
    ops = env["OPS"]
    moments = np.empty((b, 9), complex)
    for k in range(9):
        applied = (ops[k] @ states.T).T
        moments[:, k] = np.einsum("bi,bi->b", states.conj(), applied)
    mats = moments.reshape(b, 3, 3)
    sv = np.linalg.svd(mats, compute_uv=False)
    sv_min = float(np.min(sv[:, -1]))
    return np.array([np.linalg.det(polar_u(m)) for m in mats]), sv_min


def prefix(Theta: np.ndarray, w: np.ndarray, kpref: int, lbl=None) -> float:
    b = len(w)
    if lbl is None:
        lbl = np.arange(b) % (2 ** kpref)
    within: list[float] = []
    wts: list[float] = []
    for v in range(2 ** kpref):
        mask = lbl == v
        weight = float(w[mask].sum())
        if weight < 1.0e-12:
            continue
        moment = np.sum(w[mask] * np.exp(1j * Theta[mask])) / weight
        within.append(abs(complex(moment)))
        wts.append(weight)
    return float(np.average(within, weights=wts))


def null_p95(Theta: np.ndarray, w: np.ndarray, kpref: int, n_draws: int = NULL_DRAWS,
             seed: int = NULL_SEED) -> float:
    rng = np.random.default_rng(seed)
    b = len(w)
    base = np.arange(b) % (2 ** kpref)
    vals = [prefix(Theta, w, kpref, lbl=base[rng.permutation(b)]) for _ in range(n_draws)]
    return float(np.quantile(np.array(vals), 0.95))


def scan(env: dict[str, object], seed: int, depth: int, k_occ: int) -> tuple[tuple[int, float, np.ndarray, np.ndarray], dict[int, tuple[float, np.ndarray, np.ndarray]], dict[str, float]]:
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(
        rng.normal(size=(int(env["NM"]), k_occ)) + 1j * rng.normal(size=(int(env["NM"]), k_occ))
    )
    psi0 = slater(env, q)

    sf = psi0[None, :].copy()
    baseline = []
    dprev = None
    for n in range(depth):
        sf = sf @ env["U"].T
        d, _ = dets_of(env, sf)
        if dprev is not None:
            baseline.append(float(np.angle(d[0] / dprev[0])))
        dprev = d

    states = psi0[None, :].copy()
    weights = np.array([1.0])
    detprev = None
    Theta = np.zeros(1)
    worst_sv = np.inf
    min_branch_norm = np.inf
    max_weight_sum_dev = 0.0
    most = None
    rows: dict[int, tuple[float, np.ndarray, np.ndarray]] = {}
    for n in range(depth):
        states = states @ env["U"].T
        new = np.vstack([states * env["kp"][None, :], states * env["km"][None, :]])
        norms = np.einsum("bi,bi->b", new.conj(), new).real
        min_branch_norm = min(min_branch_norm, float(np.min(norms)))
        weights = np.concatenate([weights, weights]) * norms
        max_weight_sum_dev = max(max_weight_sum_dev, abs(float(weights.sum()) - 1.0))
        states = (new.T / np.sqrt(norms)).T
        d, svm = dets_of(env, states)
        worst_sv = min(worst_sv, svm)
        if detprev is not None:
            par = detprev[np.arange(len(d)) % len(detprev)]
            Theta = Theta[np.arange(len(d)) % len(Theta)] + np.angle(
                np.exp(1j * (np.angle(d / par) - baseline[n - 1]))
            )
            z = weights.sum()
            g1 = abs(complex(np.sum(weights * np.exp(1j * Theta)) / z))
            rows[n + 1] = (g1, Theta.copy(), weights.copy())
            if n >= 5 and (most is None or g1 < most[1]):
                most = (n + 1, g1, Theta.copy(), weights.copy())
        detprev = d

    if most is None:
        raise RuntimeError("argmin selector n>=5 produced no event")
    stats = {
        "worst_sv": float(worst_sv),
        "min_branch_norm": float(min_branch_norm),
        "max_weight_sum_dev": float(max_weight_sum_dev),
    }
    return most, rows, stats


def sector_moments(Theta: np.ndarray, w: np.ndarray, labels: np.ndarray) -> list[dict[str, float]]:
    out: list[dict[str, float]] = []
    for sector in range(N_SECTORS):
        mask = labels == sector
        ws = w[mask]
        th = Theta[mask]
        weight = float(ws.sum())
        m1_raw = np.sum(ws * np.exp(1j * th)) / weight
        mean = float(np.angle(m1_raw))
        z1 = np.sum(ws * np.exp(1j * (th - mean))) / weight
        z2 = np.sum(ws * np.exp(2j * (th - mean))) / weight
        r1 = float(abs(complex(z1)))
        r2 = float(abs(complex(z2)))
        r1_fourth = float(r1 ** 4)
        delta = float(r2 - r1_fourth)
        out.append({
            "sector": float(sector),
            "size": float(int(mask.sum())),
            "weight": weight,
            "mean": mean,
            "R1": r1,
            "R2": r2,
            "R1_4": r1_fourth,
            "delta": delta,
        })
    return out


def mean_abs_delta_for_labels(Theta: np.ndarray, w: np.ndarray, labels: np.ndarray) -> float:
    rows = sector_moments(Theta, w, labels)
    sector_weights = np.array([r["weight"] for r in rows])
    abs_delta = np.array([abs(r["delta"]) for r in rows])
    return float(np.average(abs_delta, weights=sector_weights))


def delta_null_p95(Theta: np.ndarray, w: np.ndarray, n_draws: int = CONTROL_DRAWS,
                   seed: int = NULL_SEED) -> float:
    rng = np.random.default_rng(seed)
    b = len(w)
    base = np.arange(b) % N_SECTORS
    vals = [
        mean_abs_delta_for_labels(Theta, w, base[rng.permutation(b)])
        for _ in range(n_draws)
    ]
    return float(np.quantile(np.array(vals), 0.95))


def print_header(title: str) -> None:
    print("=" * 78)
    print(title)
    print("=" * 78)


def main() -> int:
    print_header("Y3 within-sector remainder moment table")
    print(
        "PIN: L=3, K_occ=5, eps=0.6, tau=0.35, seeds=4242/99/7, "
        "depth cap=12, k=3 sectors"
    )
    env = build_l3()
    check(
        "dense L=3 build has the pinned 9-mode / 512-state Fock shape",
        int(env["NM"]) == 9 and int(env["DIM"]) == 512,
        f"NM={env['NM']}, DIM={env['DIM']}",
    )

    most_by_seed: dict[int, tuple[int, float, np.ndarray, np.ndarray]] = {}
    moment_rows: list[dict[str, float]] = []
    all_deltas: list[float] = []
    all_abs_deltas: list[float] = []
    all_sector_weights: list[float] = []
    control_relations: list[tuple[int, float, float, str]] = []

    print_header("Y3a machinery gates")
    for seed in SEEDS:
        most, rows, stats = scan(env, seed, DEPTH_CAP, K_OCC)
        most_by_seed[seed] = most
        depth, g1, Theta, w = most
        check(
            f"seed {seed}: rank guard stays above {RANK_TOL:g}",
            stats["worst_sv"] > RANK_TOL,
            f"worst min-sv={stats['worst_sv']:.6g}",
        )
        check(
            f"seed {seed}: no-prune guard keeps every branch norm above {NO_PRUNE_TOL:g}",
            stats["min_branch_norm"] > NO_PRUNE_TOL,
            f"min branch norm={stats['min_branch_norm']:.6g}",
        )
        check(
            f"seed {seed}: Born weights remain normalized within {WEIGHT_SUM_TOL:g}",
            stats["max_weight_sum_dev"] < WEIGHT_SUM_TOL,
            f"max |sum(w)-1|={stats['max_weight_sum_dev']:.3e}",
        )
        labels = np.arange(len(w)) % N_SECTORS
        sizes = np.array([int(np.sum(labels == sector)) for sector in range(N_SECTORS)])
        check(
            f"seed {seed}: k=3 sector adequacy has min family size >= 8 at selected depth",
            int(np.min(sizes)) >= 8,
            f"selected depth={depth}, global R1={g1:.6f}, sector sizes={sizes.tolist()}",
        )

    _, rows4242, _ = scan(env, 4242, 11, K_OCC)
    _, Th_anchor, w_anchor = rows4242[9]
    p2_anchor = prefix(Th_anchor, w_anchor, 2)
    p3_anchor = prefix(Th_anchor, w_anchor, 3)
    p4_anchor = prefix(Th_anchor, w_anchor, 4)
    null_anchor = null_p95(Th_anchor, w_anchor, 3)
    check(
        "anchor reproduction: seed 4242/depth 9 profile and null match landed rounded values",
        abs(p2_anchor - 0.557) < ANCHOR_TOL
        and abs(p3_anchor - 0.557) < ANCHOR_TOL
        and abs(null_anchor - 0.469) < ANCHOR_TOL,
        f"profile={p2_anchor:.6f}/{p3_anchor:.6f}/{p4_anchor:.6f}; "
        f"null p95={null_anchor:.6f}; tol={ANCHOR_TOL:g}",
    )

    print_header("Y3b moment table: seed sector R1 |z2| R1^4 delta")
    print(f"{'seed':>6} {'depth':>5} {'sector':>6} {'size':>5} {'weight':>12} "
          f"{'R1':>12} {'|z2|':>12} {'R1^4':>12} {'delta':>13}")
    for seed in SEEDS:
        depth, g1, Theta, w = most_by_seed[seed]
        labels = np.arange(len(w)) % N_SECTORS
        rows = sector_moments(Theta, w, labels)
        sector_weights = np.array([r["weight"] for r in rows])
        deltas = np.array([r["delta"] for r in rows])
        abs_deltas = np.abs(deltas)
        weighted_delta = float(np.average(deltas, weights=sector_weights))
        weighted_abs_delta = float(np.average(abs_deltas, weights=sector_weights))
        for row in rows:
            print(
                f"{seed:6d} {depth:5d} {int(row['sector']):6d} {int(row['size']):5d} "
                f"{row['weight']:12.6e} {row['R1']:12.6f} {row['R2']:12.6f} "
                f"{row['R1_4']:12.6f} {row['delta']:+13.6f}"
            )
            out = {"seed": float(seed), "depth": float(depth), **row}
            moment_rows.append(out)
        all_deltas.extend(float(v) for v in deltas)
        all_abs_deltas.extend(float(v) for v in abs_deltas)
        all_sector_weights.extend(float(v) for v in sector_weights)
        print(
            f"seed {seed}: selected depth={depth}, global R1={g1:.6f}, "
            f"weighted mean delta={weighted_delta:+.6f}, "
            f"weighted mean |delta|={weighted_abs_delta:.6f}"
        )

        record_mean_abs = mean_abs_delta_for_labels(Theta, w, labels)
        null95 = delta_null_p95(Theta, w)
        relation = "record <= null_p95"
        relation_condition = record_mean_abs <= null95
        control_relations.append((seed, record_mean_abs, null95, relation))
        check(
            f"seed {seed}: permutation control relation for weighted mean |delta| is {relation}",
            relation_condition,
            f"record={record_mean_abs:.6f}, null p95={null95:.6f}, draws={CONTROL_DRAWS}, seed={NULL_SEED}",
        )

    deltas_arr = np.array(all_deltas)
    abs_deltas_arr = np.array(all_abs_deltas)
    sector_weights_arr = np.array(all_sector_weights)
    check(
        "all 24 sector deltas are finite computed moment-relation deviations",
        np.isfinite(deltas_arr).all() and deltas_arr.size == len(SEEDS) * N_SECTORS,
        f"finite={int(np.isfinite(deltas_arr).sum())}/{len(SEEDS) * N_SECTORS}",
    )

    print_header("Y3c verdict: measured delta pattern")
    large_count = int(np.sum(abs_deltas_arr > DELTA_SCALE))
    total_count = int(abs_deltas_arr.size)
    weighted_mean_delta = float(np.average(deltas_arr, weights=sector_weights_arr))
    weighted_mean_abs_delta = float(np.average(abs_deltas_arr, weights=sector_weights_arr))
    check(
        f"Y3c the measured pattern: raw |delta| > {DELTA_SCALE:g} on a MAJORITY of "
        "sectors (sizeable raw deviations) while the weighted mean stays below the "
        "permutation null at every seed -- no structure resolvable BEYOND "
        "relabeling noise at these family sizes (power-limited consistency)",
        large_count > total_count / 2,
        f"large={large_count}/{total_count}, weighted mean delta={weighted_mean_delta:+.6f}, "
        f"weighted mean |delta|={weighted_mean_abs_delta:.6f}",
    )

    print_header("Y3d permutation-control summary")
    for seed, record_mean_abs, null95, relation in control_relations:
        print(
            f"seed {seed}: weighted mean |delta|={record_mean_abs:.6f}, "
            f"permuted-label null p95={null95:.6f}, relation={relation}"
        )

    print_header("SCOPE")
    print(
        "First distributional characterization of the within-sector remainder at the "
        "L=3 depth-stable most-spread events; k=3 adequate sectors only; Born cap "
        "and named instruments inherited; trajectories are realized-state data; "
        "audit lane grades statuses."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
