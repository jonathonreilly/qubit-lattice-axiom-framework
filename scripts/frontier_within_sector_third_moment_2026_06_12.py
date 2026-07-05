#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/WITHIN_SECTOR_THIRD_MOMENT_CONSISTENT_ALL_SEEDS_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_within_sector_third_moment_2026_06_12.py
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import sys

import numpy as np
from scipy.linalg import expm


NC = 3
L_RING = 3
NM = L_RING * NC
DIM = 2 ** NM
K_OCC = 5
EPS = 0.6
TAU = 0.35
DEPTH_CAP = 12
SELECTOR_MIN_ROW = 6
KPREF = 3
N_SECTORS = 2 ** KPREF
NULL_DRAWS = 300
NULL_RNG_SEED = 7777
NULL_Q = 0.95
ESS_MIN = 8.0
RANK_TOL = 1.0e-8
NO_PRUNE_TOL = 1.0e-14
WEIGHT_SUM_TOL = 1.0e-10
ANCHOR_SEED = 4242
ANCHOR_ROW = 9
ANCHOR_PREFIX3_TARGET = 0.557
ANCHOR_PREFIX3_TOL = 2.0e-3
ANCHOR_NULL95_TARGET = 0.469
ANCHOR_NULL95_TOL = 5.0e-3
PROBE_SEED = 7
PROBE_MIN_BRANCHES = 64
PROBE_EXPECTED_ROW = 11
LANDED_SEEDS = (4242, 99)
ALL_SEEDS = (4242, 99, PROBE_SEED)
EXPECTED_LANDED_ROWS = {4242: 9, 99: 7}
EXPECTED_ADEQUATE_SECTORS = {4242: 8, 99: 8, PROBE_SEED: 8}
EXPECTED_DELTA2_LE_NULL = {4242: True, 99: True, PROBE_SEED: True}
EXPECTED_DELTA3_LE_NULL = {4242: True, 99: True, PROBE_SEED: True}
ANTI_FABRICATION_DELTA2_FLOOR = 1.0e-6


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag}: {name}{suffix}")


def wrap_angle(x: np.ndarray | float) -> np.ndarray | float:
    return np.angle(np.exp(1j * x))


@dataclass(frozen=True)
class TreeRow:
    depth: int
    global_r1: float
    theta: np.ndarray
    weights: np.ndarray


@dataclass(frozen=True)
class ScanResult:
    seed: int
    rows: dict[int, TreeRow]
    most: TreeRow
    worst_sv: float
    min_branch_norm: float
    max_weight_sum_dev: float


@dataclass(frozen=True)
class EventSpec:
    seed: int
    label: str
    depth: int
    disclosure: str


@dataclass(frozen=True)
class SectorRow:
    seed: int
    label: str
    depth: int
    sector: int
    branches: int
    sector_weight: float
    ess: float
    theta_mean: float
    r1: float
    abs_z2: float
    abs_z3: float
    delta2: float
    delta3: float
    adequate: bool


@dataclass(frozen=True)
class EventResult:
    spec: EventSpec
    rows: tuple[SectorRow, ...]
    adequate_rows: tuple[SectorRow, ...]
    weighted_abs_delta2: float
    weighted_abs_delta3: float
    null_delta2: np.ndarray
    null_delta3: np.ndarray
    p95_delta2: float
    p95_delta3: float
    delta2_le_null: bool
    delta3_le_null: bool


def build_env() -> dict[str, object]:
    bits = np.array(
        [[(idx >> (NM - 1 - j)) & 1 for j in range(NM)] for idx in range(DIM)],
        dtype=np.uint8,
    )
    shifts = np.array([1 << (NM - 1 - j) for j in range(NM)], dtype=np.int64)
    signs = np.empty((NM, DIM), dtype=np.int8)
    for j in range(NM):
        parity = np.zeros(DIM, dtype=np.uint8) if j == 0 else bits[:, :j].sum(axis=1) & 1
        signs[j] = np.where(parity, -1, 1)

    def creation_map(j: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        cols = np.flatnonzero(bits[:, j] == 0)
        rows = cols + shifts[j]
        coeff = signs[j, cols].astype(complex)
        return rows, cols, coeff

    def one_body_map(i: int, j: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        if i == j:
            cols = np.flatnonzero(bits[:, j] == 1)
            return cols, cols, np.ones(len(cols), dtype=complex)
        cols = np.flatnonzero((bits[:, j] == 1) & (bits[:, i] == 0))
        mid = cols - shifts[j]
        rows = mid + shifts[i]
        coeff = (signs[j, cols] * signs[i, mid]).astype(complex)
        return rows, cols, coeff

    hamiltonian = np.zeros((DIM, DIM), dtype=complex)
    h_one = np.zeros((NM, NM), dtype=float)
    for x in range(L_RING):
        for c in range(NC):
            left = x * NC + c
            right = ((x + 1) % L_RING) * NC + c
            h_one[left, right] = -1.0
            h_one[right, left] = -1.0
            for i, j in ((left, right), (right, left)):
                rows, cols, coeff = one_body_map(i, j)
                hamiltonian[rows, cols] += -coeff

    n0_diag = bits[:, :NC].sum(axis=1).astype(float)
    nt = (n0_diag - n0_diag.mean()) / max(abs(n0_diag - n0_diag.mean()))
    kp_diag = np.sqrt((1.0 + EPS * nt) / 2.0).astype(complex)
    km_diag = np.sqrt((1.0 - EPS * nt) / 2.0).astype(complex)
    ops = [one_body_map(i, NC + j) for i in range(NC) for j in range(NC)]
    return {
        "bits": bits,
        "creation": [creation_map(j) for j in range(NM)],
        "h_one": h_one,
        "U": expm((-1j * TAU) * hamiltonian),
        "kp": kp_diag,
        "km": km_diag,
        "OPS": ops,
        "vac_idx": 0,
    }


def apply_creation(env: dict[str, object], mode: int, vec: np.ndarray) -> np.ndarray:
    rows, cols, coeff = env["creation"][mode]
    out = np.zeros_like(vec)
    out[rows] = coeff * vec[cols]
    return out


def slater(env: dict[str, object], pmat: np.ndarray) -> np.ndarray:
    psi = np.zeros(DIM, dtype=complex)
    psi[int(env["vac_idx"])] = 1.0
    for k in range(pmat.shape[1]):
        new = np.zeros(DIM, dtype=complex)
        for m in range(NM):
            new += pmat[m, k] * apply_creation(env, m, psi)
        psi = new
    return psi / np.linalg.norm(psi)


def dets_of(env: dict[str, object], states: np.ndarray) -> tuple[np.ndarray, float]:
    branch_count = states.shape[0]
    mats = np.empty((branch_count, 9), dtype=complex)
    for k, (rows, cols, coeff) in enumerate(env["OPS"]):
        mats[:, k] = np.einsum(
            "bt,t,bt->b",
            states[:, rows].conj(),
            coeff,
            states[:, cols],
            optimize=True,
        )
    mats = mats.reshape(branch_count, 3, 3)
    singular = np.linalg.svd(mats, compute_uv=False)
    u, _, vh = np.linalg.svd(mats)
    polar = u @ vh
    return np.linalg.det(polar), float(np.min(singular[:, -1]))


def scan(env: dict[str, object], seed: int, depth: int = DEPTH_CAP) -> ScanResult:
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(
        rng.normal(size=(NM, K_OCC)) + 1j * rng.normal(size=(NM, K_OCC))
    )
    psi0 = slater(env, q[:, :K_OCC])

    single_family = psi0[None, :].copy()
    baseline: list[float] = []
    det_prev = None
    for n in range(depth):
        single_family = single_family @ env["U"].T
        dets, _ = dets_of(env, single_family)
        if det_prev is not None:
            baseline.append(float(np.angle(dets[0] / det_prev[0])))
        det_prev = dets

    states = psi0[None, :].copy()
    weights = np.array([1.0], dtype=float)
    det_prev = None
    theta = np.zeros(1, dtype=float)
    worst_sv = math.inf
    min_branch_norm = math.inf
    max_weight_sum_dev = 0.0
    most: TreeRow | None = None
    rows: dict[int, TreeRow] = {}
    for n in range(depth):
        states = states @ env["U"].T
        new_states = np.vstack([states * env["kp"][None, :], states * env["km"][None, :]])
        norms = np.einsum("bi,bi->b", new_states.conj(), new_states).real
        min_branch_norm = min(min_branch_norm, float(np.min(norms)))
        if not np.all(norms > NO_PRUNE_TOL):
            raise RuntimeError(f"no-prune guard failed at seed={seed} step={n + 1}")
        weights = np.concatenate([weights, weights]) * norms
        max_weight_sum_dev = max(max_weight_sum_dev, abs(float(np.sum(weights)) - 1.0))
        states = (new_states.T / np.sqrt(norms)).T
        dets, sv_min = dets_of(env, states)
        worst_sv = min(worst_sv, sv_min)
        if det_prev is not None:
            parent = det_prev[np.arange(len(dets)) % len(det_prev)]
            theta = theta[np.arange(len(dets)) % len(theta)] + np.angle(
                np.exp(1j * (np.angle(dets / parent) - baseline[n - 1]))
            )
            row_depth = n + 1
            z = float(np.sum(weights))
            global_r1 = abs(complex(np.sum(weights * np.exp(1j * theta)) / z))
            row = TreeRow(row_depth, float(global_r1), theta.copy(), weights.copy())
            rows[row_depth] = row
            if row_depth >= SELECTOR_MIN_ROW and (most is None or row.global_r1 < most.global_r1):
                most = row
        det_prev = dets

    if most is None:
        raise RuntimeError("most-spread selector found no eligible row")
    return ScanResult(
        seed=seed,
        rows=rows,
        most=most,
        worst_sv=float(worst_sv),
        min_branch_norm=float(min_branch_norm),
        max_weight_sum_dev=float(max_weight_sum_dev),
    )


def select_most_for_cap(rows: dict[int, TreeRow], cap: int) -> TreeRow:
    candidates = [row for depth, row in rows.items() if SELECTOR_MIN_ROW <= depth <= cap]
    if not candidates:
        raise RuntimeError(f"no selector candidates for cap={cap}")
    return min(candidates, key=lambda row: (row.global_r1, row.depth))


def seed7_probe_row(rows: dict[int, TreeRow]) -> TreeRow:
    candidates = [
        row for row in rows.values()
        if len(row.weights) >= PROBE_MIN_BRANCHES
    ]
    if len(candidates) < 2:
        raise RuntimeError("seed-7 probe selector has fewer than two candidates")
    candidates.sort(key=lambda row: (row.global_r1, row.depth))
    return candidates[1]


def prefix_labels(branch_count: int, kpref: int = KPREF) -> np.ndarray:
    return np.arange(branch_count) % (2 ** kpref)


def prefix_stat(theta: np.ndarray, weights: np.ndarray, kpref: int, labels: np.ndarray | None = None) -> float:
    if labels is None:
        labels = prefix_labels(len(weights), kpref)
    within: list[float] = []
    family_weights: list[float] = []
    for label in range(2 ** kpref):
        mask = labels == label
        wsum = float(np.sum(weights[mask]))
        if wsum < 1.0e-12:
            continue
        z = np.sum(weights[mask] * np.exp(1j * theta[mask])) / wsum
        within.append(abs(complex(z)))
        family_weights.append(wsum)
    return float(np.average(within, weights=family_weights))


def prefix_null_p95(theta: np.ndarray, weights: np.ndarray, kpref: int = KPREF) -> float:
    rng = np.random.default_rng(NULL_RNG_SEED)
    base = prefix_labels(len(weights), kpref)
    vals = np.empty(NULL_DRAWS, dtype=float)
    for i in range(NULL_DRAWS):
        vals[i] = prefix_stat(theta, weights, kpref, labels=base[rng.permutation(len(base))])
    return float(np.quantile(vals, NULL_Q))


def effective_sample_size(weights: np.ndarray) -> float:
    total = float(np.sum(weights))
    return total * total / float(np.sum(weights * weights))


def compute_sector_rows(spec: EventSpec, row: TreeRow) -> tuple[SectorRow, ...]:
    labels = prefix_labels(len(row.weights), KPREF)
    out: list[SectorRow] = []
    for sector in range(N_SECTORS):
        mask = labels == sector
        theta_s = row.theta[mask]
        weights_s = row.weights[mask]
        sector_weight = float(np.sum(weights_s))
        ess = effective_sample_size(weights_s)
        theta_mean = float(np.angle(np.sum(weights_s * np.exp(1j * theta_s)) / sector_weight))
        centered = wrap_angle(theta_s - theta_mean)
        z1 = np.sum(weights_s * np.exp(1j * centered)) / sector_weight
        z2 = np.sum(weights_s * np.exp(2j * centered)) / sector_weight
        z3 = np.sum(weights_s * np.exp(3j * centered)) / sector_weight
        r1 = float(abs(complex(z1)))
        abs_z2 = float(abs(complex(z2)))
        abs_z3 = float(abs(complex(z3)))
        out.append(
            SectorRow(
                seed=spec.seed,
                label=spec.label,
                depth=spec.depth,
                sector=sector,
                branches=int(np.count_nonzero(mask)),
                sector_weight=sector_weight,
                ess=ess,
                theta_mean=theta_mean,
                r1=r1,
                abs_z2=abs_z2,
                abs_z3=abs_z3,
                delta2=float(abs_z2 - r1 ** 4),
                delta3=float(abs_z3 - r1 ** 9),
                adequate=ess >= ESS_MIN,
            )
        )
    return tuple(out)


def weighted_abs(rows: tuple[SectorRow, ...], attr: str) -> float:
    if not rows:
        return math.nan
    weights = np.array([row.sector_weight for row in rows], dtype=float)
    values = np.array([abs(float(getattr(row, attr))) for row in rows], dtype=float)
    return float(np.sum(weights * values) / np.sum(weights))


def moment_stat_for_labels(
    theta: np.ndarray,
    weights: np.ndarray,
    labels: np.ndarray,
    sector_ids: tuple[int, ...],
) -> tuple[float, float]:
    rows: list[tuple[float, float, float]] = []
    for sector in sector_ids:
        mask = labels == sector
        theta_s = theta[mask]
        weights_s = weights[mask]
        sector_weight = float(np.sum(weights_s))
        theta_mean = float(np.angle(np.sum(weights_s * np.exp(1j * theta_s)) / sector_weight))
        centered = wrap_angle(theta_s - theta_mean)
        z1 = np.sum(weights_s * np.exp(1j * centered)) / sector_weight
        z2 = np.sum(weights_s * np.exp(2j * centered)) / sector_weight
        z3 = np.sum(weights_s * np.exp(3j * centered)) / sector_weight
        r1 = abs(complex(z1))
        delta2 = abs(complex(z2)) - r1 ** 4
        delta3 = abs(complex(z3)) - r1 ** 9
        rows.append((sector_weight, abs(float(delta2)), abs(float(delta3))))
    row_weights = np.array([item[0] for item in rows], dtype=float)
    delta2_values = np.array([item[1] for item in rows], dtype=float)
    delta3_values = np.array([item[2] for item in rows], dtype=float)
    return (
        float(np.sum(row_weights * delta2_values) / np.sum(row_weights)),
        float(np.sum(row_weights * delta3_values) / np.sum(row_weights)),
    )


def permutation_nulls(row: TreeRow, sector_ids: tuple[int, ...]) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(NULL_RNG_SEED)
    base = prefix_labels(len(row.weights), KPREF)
    null_delta2 = np.empty(NULL_DRAWS, dtype=float)
    null_delta3 = np.empty(NULL_DRAWS, dtype=float)
    for i in range(NULL_DRAWS):
        labels = base[rng.permutation(len(base))]
        null_delta2[i], null_delta3[i] = moment_stat_for_labels(
            row.theta, row.weights, labels, sector_ids
        )
    return null_delta2, null_delta3


def analyze_event(spec: EventSpec, row: TreeRow) -> EventResult:
    rows = compute_sector_rows(spec, row)
    adequate_rows = tuple(row for row in rows if row.adequate)
    sector_ids = tuple(row.sector for row in adequate_rows)
    observed_delta2 = weighted_abs(adequate_rows, "delta2")
    observed_delta3 = weighted_abs(adequate_rows, "delta3")
    null_delta2, null_delta3 = permutation_nulls(row, sector_ids)
    p95_delta2 = float(np.quantile(null_delta2, NULL_Q))
    p95_delta3 = float(np.quantile(null_delta3, NULL_Q))
    return EventResult(
        spec=spec,
        rows=rows,
        adequate_rows=adequate_rows,
        weighted_abs_delta2=observed_delta2,
        weighted_abs_delta3=observed_delta3,
        null_delta2=null_delta2,
        null_delta3=null_delta3,
        p95_delta2=p95_delta2,
        p95_delta3=p95_delta3,
        delta2_le_null=bool(observed_delta2 <= p95_delta2),
        delta3_le_null=bool(observed_delta3 <= p95_delta3),
    )


def print_header() -> None:
    print("# U3 exact Born-tree moment program")
    print(
        "constants: "
        f"L={L_RING} NC={NC} K_occ={K_OCC} eps={EPS} tau={TAU} "
        f"depth_cap={DEPTH_CAP} prefix_k={KPREF} ESS_min={ESS_MIN} "
        f"null_rng={NULL_RNG_SEED} null_draws={NULL_DRAWS}"
    )
    print(
        "tree: Slater initial state, U_step ring hopping, diagonal Kraus pair, "
        "OPS bilinears, baseline det-phase subtraction, composed centered Theta, Born weights"
    )


def print_table(results: tuple[EventResult, ...]) -> None:
    print(
        "TABLE seed label depth sector branches sector_weight ESS theta_mean "
        "R1 abs_z2 abs_z3 delta2 delta3 adequate"
    )
    for result in results:
        for row in result.rows:
            print(
                f"ROW seed={row.seed} label={row.label} depth={row.depth} "
                f"sector={row.sector} branches={row.branches} "
                f"sector_weight={row.sector_weight:.12e} ESS={row.ess:.6f} "
                f"theta_mean={row.theta_mean:.12f} R1={row.r1:.12f} "
                f"abs_z2={row.abs_z2:.12f} abs_z3={row.abs_z3:.12f} "
                f"delta2={row.delta2:+.12e} delta3={row.delta3:+.12e} "
                f"adequate={row.adequate}"
            )
    print("SUMMARY seed label depth adequate weighted_abs_delta2 p95_delta2 weighted_abs_delta3 p95_delta3")
    for result in results:
        print(
            f"SUMMARY seed={result.spec.seed} label={result.spec.label} depth={result.spec.depth} "
            f"adequate={len(result.adequate_rows)} "
            f"weighted_abs_delta2={result.weighted_abs_delta2:.12e} "
            f"p95_delta2={result.p95_delta2:.12e} "
            f"weighted_abs_delta3={result.weighted_abs_delta3:.12e} "
            f"p95_delta3={result.p95_delta3:.12e}"
        )


def relation_detail(observed: float, p95: float) -> str:
    relation = "<=" if observed <= p95 else ">"
    return f"record={observed:.12e} {relation} null_p95={p95:.12e}"


def main() -> int:
    env = build_env()
    print_header()

    scan4242 = scan(env, ANCHOR_SEED, DEPTH_CAP)
    anchor_row = scan4242.rows[ANCHOR_ROW]
    anchor_prefix3 = prefix_stat(anchor_row.theta, anchor_row.weights, KPREF)
    anchor_null95 = prefix_null_p95(anchor_row.theta, anchor_row.weights, KPREF)
    anchor_ok = (
        abs(anchor_prefix3 - ANCHOR_PREFIX3_TARGET) <= ANCHOR_PREFIX3_TOL
        and abs(anchor_null95 - ANCHOR_NULL95_TARGET) <= ANCHOR_NULL95_TOL
    )
    check(
        "ANCHOR FIRST: landed seed 4242 depth-9 prefix-3 and null p95 reproduce",
        anchor_ok,
        f"prefix3={anchor_prefix3:.12f} target={ANCHOR_PREFIX3_TARGET:.3f} "
        f"tol={ANCHOR_PREFIX3_TOL:.1e}; null_p95={anchor_null95:.12f} "
        f"target={ANCHOR_NULL95_TARGET:.3f} tol={ANCHOR_NULL95_TOL:.1e}",
    )

    scans: dict[int, ScanResult] = {ANCHOR_SEED: scan4242}
    for seed in (99, PROBE_SEED):
        scans[seed] = scan(env, seed, DEPTH_CAP)

    landed_specs: list[EventSpec] = []
    for seed in LANDED_SEEDS:
        selected = select_most_for_cap(scans[seed].rows, DEPTH_CAP)
        landed_specs.append(
            EventSpec(
                seed=seed,
                label="landed",
                depth=selected.depth,
                disclosure=f"depth-stable most-spread event for seed {seed}",
            )
        )
    probe = seed7_probe_row(scans[PROBE_SEED].rows)
    specs = tuple(
        landed_specs
        + [
            EventSpec(
                seed=PROBE_SEED,
                label="probe",
                depth=probe.depth,
                disclosure="disclosed post-hoc probe: second-smallest global R1 row with >=64 branches",
            )
        ]
    )
    rows_by_seed = {
        4242: scans[4242].rows[specs[0].depth],
        99: scans[99].rows[specs[1].depth],
        PROBE_SEED: probe,
    }
    results = tuple(analyze_event(spec, rows_by_seed[spec.seed]) for spec in specs)
    print_table(results)

    h_one = env["h_one"]
    wraparound_ok = all(
        h_one[(L_RING - 1) * NC + c, c] == -1.0
        and h_one[c, (L_RING - 1) * NC + c] == -1.0
        for c in range(NC)
    )
    check(
        "finite L=3 ring wraparound is active in every color channel",
        anchor_ok and wraparound_ok,
        f"nonzero one-body entries={int(np.count_nonzero(h_one))}",
    )
    check(
        "exact Born tree respects the depth cap and branch count B=2^depth",
        anchor_ok
        and all(result.spec.depth <= DEPTH_CAP for result in results)
        and all(len(rows_by_seed[result.spec.seed].weights) == 2 ** result.spec.depth for result in results),
        "; ".join(
            f"seed {result.spec.seed}: depth={result.spec.depth}, branches={len(rows_by_seed[result.spec.seed].weights)}"
            for result in results
        ),
    )
    check(
        "rank, no-prune, and Born-weight normalization guards hold through depth cap",
        anchor_ok
        and all(scan_result.worst_sv > RANK_TOL for scan_result in scans.values())
        and all(scan_result.min_branch_norm > NO_PRUNE_TOL for scan_result in scans.values())
        and all(scan_result.max_weight_sum_dev <= WEIGHT_SUM_TOL for scan_result in scans.values()),
        "; ".join(
            f"seed {seed}: worst_sv={scans[seed].worst_sv:.6e}, "
            f"min_norm={scans[seed].min_branch_norm:.6e}, "
            f"max_weight_error={scans[seed].max_weight_sum_dev:.3e}"
            for seed in ALL_SEEDS
        ),
    )
    check(
        "landed seeds use the depth-stable most-spread rows 4242@9 and 99@7",
        anchor_ok
        and {result.spec.seed: result.spec.depth for result in results if result.spec.seed in LANDED_SEEDS}
        == EXPECTED_LANDED_ROWS
        and all(
            select_most_for_cap(scans[seed].rows, 11).depth == select_most_for_cap(scans[seed].rows, 12).depth
            for seed in LANDED_SEEDS
        ),
        "; ".join(
            f"seed {seed}: cap11={select_most_for_cap(scans[seed].rows, 11).depth}, "
            f"cap12={select_most_for_cap(scans[seed].rows, 12).depth}"
            for seed in LANDED_SEEDS
        ),
    )
    seed7_candidates = [
        row for row in scans[PROBE_SEED].rows.values()
        if len(row.weights) >= PROBE_MIN_BRANCHES
    ]
    seed7_candidates.sort(key=lambda row: (row.global_r1, row.depth))
    check(
        "seed-7 probe row is depth 11 and is the second-smallest global R1 row with >=64 branches",
        anchor_ok and probe.depth == PROBE_EXPECTED_ROW and probe is seed7_candidates[1],
        f"probe_depth={probe.depth}, branches={len(probe.weights)}, global_R1={probe.global_r1:.12f}; "
        f"smallest_depth={seed7_candidates[0].depth}, smallest_global_R1={seed7_candidates[0].global_r1:.12f}",
    )
    check(
        "ESS adequacy: every testable event has all eight prefix-3 sectors at ESS >= 8",
        anchor_ok
        and {result.spec.seed: len(result.adequate_rows) for result in results} == EXPECTED_ADEQUATE_SECTORS,
        "; ".join(
            f"seed {result.spec.seed}: adequate={len(result.adequate_rows)}/8, "
            f"min_ESS={min(row.ess for row in result.rows):.6f}"
            for result in results
        ),
    )

    for result in results:
        delta2_relation_holds = result.delta2_le_null  # direct: record <= null p95
        delta3_relation_holds = result.delta3_le_null  # direct: record <= null p95
        label2 = "<=" if EXPECTED_DELTA2_LE_NULL[result.spec.seed] else ">"
        label3 = "<=" if EXPECTED_DELTA3_LE_NULL[result.spec.seed] else ">"
        check(
            f"U3 record-vs-null TRUE relation seed {result.spec.seed}: weighted mean |delta2| {label2} own permutation p95",
            anchor_ok and delta2_relation_holds,
            relation_detail(result.weighted_abs_delta2, result.p95_delta2),
        )
        check(
            f"U3 record-vs-null TRUE relation seed {result.spec.seed}: weighted mean |delta3| {label3} own permutation p95",
            anchor_ok and delta3_relation_holds,
            relation_detail(result.weighted_abs_delta3, result.p95_delta3),
        )

    delta2_nonzero = all(result.weighted_abs_delta2 > ANTI_FABRICATION_DELTA2_FLOOR for result in results)
    delta3_nonzero = all(result.weighted_abs_delta3 > ANTI_FABRICATION_DELTA2_FLOOR for result in results)
    check(
        "anti-fabrication (ALL): every seed's tree-data weighted mean |delta2| AND |delta3| is nonzero at the floor",
        anchor_ok and delta2_nonzero and delta3_nonzero,
        "; ".join(
            f"seed {result.spec.seed}: weighted_abs_delta2={result.weighted_abs_delta2:.12e}"
            for result in results
        ),
    )
    check(
        "joint U3 measured pattern is exactly the computed record-vs-null relation set for both moments",
        anchor_ok
        and all(result.delta2_le_null == EXPECTED_DELTA2_LE_NULL[result.spec.seed] for result in results)
        and all(result.delta3_le_null == EXPECTED_DELTA3_LE_NULL[result.spec.seed] for result in results),
        "delta2 "
        + ", ".join(f"{seed}:{'<=' if EXPECTED_DELTA2_LE_NULL[seed] else '>'}" for seed in ALL_SEEDS)
        + "; delta3 "
        + ", ".join(f"{seed}:{'<=' if EXPECTED_DELTA3_LE_NULL[seed] else '>'}" for seed in ALL_SEEDS),
    )

    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
