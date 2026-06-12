#!/usr/bin/env python3
"""Class-A exact verification for the adequate-family source note

    docs/CONDITIONAL_LAW_PREFIX_LADDER_NO_FINITE_K_EXHAUSTION_BOUNDED_THEOREM_NOTE_2026-06-12.md

The theorem-grade claim is no exhaustion through each seed's adequate-family
range; higher-k entries are reported with inadequacy flags rather than counted
as null-clearing verdicts.

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_conditional_law_prefix_ladder_persistence_2026_06_12.py
"""
from __future__ import annotations

import sys

import numpy as np
from scipy.linalg import expm


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    if detail:
        print(f"[{tag}] {name}: {detail}")
    else:
        print(f"[{tag}] {name}")


NC = 3
L_RING = 3
NM = L_RING * NC
DIM = 2 ** NM
K_OCC = 5
EPS = 0.6
TAU = 0.35
SEEDS = (4242, 99, 7)
DEPTH_CAP = 12
CAP_STABILITY_PROBE = 11
PREFIX_KS = tuple(range(2, 9))
NULL_DRAWS = 300
NULL_SEED = 7777
RANK_TOL = 1.0e-8
NO_PRUNE_TOL = 1.0e-14
WEIGHT_TOL = 1.0e-10
CLEAR_TOL = 1.0e-12
ANCHOR_SEED = 4242
ANCHOR_ROW = 9
ANCHOR_K = 3
ANCHOR_PREFIX3 = 0.557
ANCHOR_PREFIX3_TOL = 2.0e-3
ANCHOR_NULL95 = 0.469
ANCHOR_NULL95_TOL = 5.0e-3

# The pinned script used `if n >= 5` with zero-based loop variable n while storing
# rows as n + 1. Mirroring it exactly makes the eligible stored rows row >= 6.
SELECTOR_MIN_ROW = 6

EXPECTED_EMPTY_FULL_LABEL_PAIRS = {(99, 8)}
MIN_ACTIVE_FAMILY_SIZE = 8

EXPECTED_ADEQUATE_CLEAR_SETS = {
    4242: {2, 3, 4, 5, 6},
    99: {2, 3, 4},
    7: {2, 3, 4, 5, 6, 7},
}
EXPECTED_ADEQUATE_KMAX = {4242: 6, 99: 4, 7: 7}
EXPECTED_FAMILY_INADEQUATE_SETS = {
    4242: {7, 8},
    99: {5, 6, 7, 8},
    7: {8},
}


def build() -> dict[str, object]:
    bits = np.array(
        [[(idx >> (NM - 1 - j)) & 1 for j in range(NM)] for idx in range(DIM)],
        dtype=np.uint8,
    )
    shifts = np.array([1 << (NM - 1 - j) for j in range(NM)], dtype=np.int64)
    signs = np.empty((NM, DIM), dtype=np.int8)
    for j in range(NM):
        if j == 0:
            parity = np.zeros(DIM, dtype=np.uint8)
        else:
            parity = bits[:, :j].sum(axis=1) & 1
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
    for x in range(L_RING):
        for c in range(NC):
            left = x * NC + c
            right = ((x + 1) % L_RING) * NC + c
            for i, j in ((left, right), (right, left)):
                rows, cols, coeff = one_body_map(i, j)
                hamiltonian[rows, cols] += -coeff

    u_step = expm((-1j * TAU) * hamiltonian)
    n0_diag = bits[:, :NC].sum(axis=1).astype(float)
    nt = (n0_diag - n0_diag.mean()) / max(abs(n0_diag - n0_diag.mean()))
    kp_diag = np.sqrt((1.0 + EPS * nt) / 2.0).astype(complex)
    km_diag = np.sqrt((1.0 - EPS * nt) / 2.0).astype(complex)
    ops = [one_body_map(i, NC + j) for i in range(3) for j in range(3)]
    return {
        "bits": bits,
        "creation": [creation_map(j) for j in range(NM)],
        "U": u_step,
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
    psi[env["vac_idx"]] = 1.0
    for k in range(pmat.shape[1]):
        new = np.zeros(DIM, dtype=complex)
        for m in range(NM):
            new += pmat[m, k] * apply_creation(env, m, psi)
        psi = new
    return psi / np.linalg.norm(psi)


def dets_of(env: dict[str, object], states: np.ndarray) -> tuple[np.ndarray, float]:
    bcount = states.shape[0]
    mats = np.empty((bcount, 9), dtype=complex)
    for k, (rows, cols, coeff) in enumerate(env["OPS"]):
        mats[:, k] = np.einsum(
            "bt,t,bt->b",
            states[:, rows].conj(),
            coeff,
            states[:, cols],
            optimize=True,
        )
    mats = mats.reshape(bcount, 3, 3)
    singular = np.linalg.svd(mats, compute_uv=False)
    u, _, vh = np.linalg.svd(mats)
    polar = u @ vh
    return np.linalg.det(polar), float(np.min(singular[:, -1]))


def prefix_info(
    theta: np.ndarray,
    weights: np.ndarray,
    kpref: int,
    labels: np.ndarray | None = None,
) -> dict[str, object]:
    branches = len(weights)
    label_count = 2 ** kpref
    if labels is None:
        labels = np.arange(branches) % label_count
    counts = np.bincount(labels, minlength=label_count)
    within = []
    family_weights = []
    for value in range(label_count):
        mask = labels == value
        wsum = weights[mask].sum()
        if wsum < 1.0e-12:
            continue
        z = np.sum(weights[mask] * np.exp(1j * theta[mask])) / wsum
        within.append(abs(complex(z)))
        family_weights.append(wsum)
    if not within:
        stat = float("nan")
    else:
        stat = float(np.average(within, weights=family_weights))
    active_counts = counts[counts > 0]
    return {
        "stat": stat,
        "branches": branches,
        "label_count": label_count,
        "active_label_count": int(len(active_counts)),
        "empty_label_count": int(np.sum(counts == 0)),
        "min_count": int(counts.min()) if len(counts) else 0,
        "max_count": int(counts.max()) if len(counts) else 0,
        "min_active_count": int(active_counts.min()) if len(active_counts) else 0,
        "max_active_count": int(active_counts.max()) if len(active_counts) else 0,
    }


def prefix(theta: np.ndarray, weights: np.ndarray, kpref: int, labels: np.ndarray | None = None) -> float:
    return float(prefix_info(theta, weights, kpref, labels=labels)["stat"])


def null_p95(theta: np.ndarray, weights: np.ndarray, kpref: int) -> float:
    rng = np.random.default_rng(NULL_SEED)
    branches = len(weights)
    base = np.arange(branches) % (2 ** kpref)
    vals = [
        prefix(theta, weights, kpref, labels=base[rng.permutation(branches)])
        for _ in range(NULL_DRAWS)
    ]
    return float(np.quantile(np.array(vals), 0.95))


def scan(
    env: dict[str, object],
    seed: int,
    depth: int,
) -> tuple[tuple[int, float, np.ndarray, np.ndarray], dict[int, tuple[float, np.ndarray, np.ndarray]], float, float, float]:
    rng = np.random.default_rng(seed)
    pmat = np.linalg.qr(
        rng.normal(size=(NM, K_OCC)) + 1j * rng.normal(size=(NM, K_OCC))
    )[0]
    psi0 = slater(env, pmat)

    single_family = psi0[None, :].copy()
    baseline = []
    det_prev = None
    for n in range(depth):
        single_family = single_family @ env["U"].T
        dets, _ = dets_of(env, single_family)
        if det_prev is not None:
            baseline.append(float(np.angle(dets[0] / det_prev[0])))
        det_prev = dets

    states = psi0[None, :].copy()
    weights = np.array([1.0])
    det_prev = None
    theta = np.zeros(1)
    worst_sv = np.inf
    min_norm = np.inf
    max_weight_error = 0.0
    most = None
    rows: dict[int, tuple[float, np.ndarray, np.ndarray]] = {}
    for n in range(depth):
        states = states @ env["U"].T
        new = np.vstack([states * env["kp"][None, :], states * env["km"][None, :]])
        norms = np.einsum("bi,bi->b", new.conj(), new).real
        min_norm = min(min_norm, float(norms.min()))
        if float(norms.min()) <= 0.0:
            raise RuntimeError(f"zero norm branch at seed={seed} depth_step={n + 1}")
        weights = np.concatenate([weights, weights]) * norms
        max_weight_error = max(max_weight_error, abs(float(weights.sum()) - 1.0))
        states = (new.T / np.sqrt(norms)).T
        dets, sv_min = dets_of(env, states)
        worst_sv = min(worst_sv, sv_min)
        if det_prev is not None:
            parent = det_prev[np.arange(len(dets)) % len(det_prev)]
            theta = theta[np.arange(len(dets)) % len(theta)] + np.angle(
                np.exp(1j * (np.angle(dets / parent) - baseline[n - 1]))
            )
            z = weights.sum()
            g1 = abs(complex(np.sum(weights * np.exp(1j * theta)) / z))
            row = n + 1
            rows[row] = (g1, theta.copy(), weights.copy())
            if n >= 5 and (most is None or g1 < most[1]):
                most = (row, g1, theta.copy(), weights.copy())
        det_prev = dets
    if most is None:
        raise RuntimeError("selector had no eligible rows")
    return most, rows, worst_sv, min_norm, max_weight_error


def select_most_for_cap(rows: dict[int, tuple[float, np.ndarray, np.ndarray]], cap: int) -> int:
    candidates = [
        (row, data[0])
        for row, data in rows.items()
        if SELECTOR_MIN_ROW <= row <= cap
    ]
    if not candidates:
        raise RuntimeError(f"no selector candidates for cap={cap}")
    return min(candidates, key=lambda item: item[1])[0]


def ladder_for_row(
    rows: dict[int, tuple[float, np.ndarray, np.ndarray]],
    row: int,
) -> dict[int, dict[str, object]]:
    _, theta, weights = rows[row]
    ladder = {}
    for kpref in PREFIX_KS:
        info = prefix_info(theta, weights, kpref)
        n95 = null_p95(theta, weights, kpref)
        stat = float(info["stat"])
        gap = stat - n95
        required_active_family_count = 2 ** (kpref - 1)
        gap_clears = gap > CLEAR_TOL
        family_size_adequate = info["min_active_count"] >= MIN_ACTIVE_FAMILY_SIZE
        family_count_adequate = info["active_label_count"] >= required_active_family_count
        family_adequate = family_size_adequate and family_count_adequate
        theorem_clears = gap_clears and family_adequate
        if theorem_clears:
            status = "clears (adequate)"
        elif not family_adequate:
            status = "reported (family-inadequate)"
        else:
            status = "does_not_clear (adequate)"
        info.update(
            {
                "null95": n95,
                "gap": gap,
                "gap_clears": gap_clears,
                "required_active_family_count": required_active_family_count,
                "family_size_adequate": family_size_adequate,
                "family_count_adequate": family_count_adequate,
                "family_adequate": family_adequate,
                "theorem_clears": theorem_clears,
                "status": status,
                "well_defined": np.isfinite(stat) and np.isfinite(n95) and -1.0e-12 <= stat <= 1.0 + 1.0e-12,
            }
        )
        ladder[kpref] = info
    return ladder


def print_ladder(seed: int, row: int, g1: float, ladder: dict[int, dict[str, object]]) -> None:
    print(f"X3b ADEQUACY-ANNOTATED k-LADDER seed={seed} selected_row={row} global_g1={g1:.12f}")
    for kpref in PREFIX_KS:
        entry = ladder[kpref]
        cautions = []
        if not entry["family_size_adequate"]:
            cautions.append(f"min_active_family<{MIN_ACTIVE_FAMILY_SIZE}")
        if not entry["family_count_adequate"]:
            cautions.append(f"active_family_count<{entry['required_active_family_count']}")
        if entry["empty_label_count"] > 0:
            cautions.append("EMPTY-LABELS")
        details = []
        if seed == 99 and kpref == 7:
            details.append(
                "singleton-degenerate: one branch per active family; "
                "non-clearance is power-limited, not a measured difference"
            )
        caution = " " + ",".join(cautions) if cautions else ""
        detail = " detail=" + "; ".join(details) if details else ""
        print(
            f"  k={kpref} stat={entry['stat']:.12f} null95={entry['null95']:.12f} "
            f"gap={entry['gap']:+.12f} gap_clears={entry['gap_clears']} "
            f"theorem_clears={entry['theorem_clears']} status=\"{entry['status']}\" "
            f"labels={entry['label_count']} active={entry['active_label_count']} "
            f"required_active={entry['required_active_family_count']} "
            f"branches={entry['branches']} min_active={entry['min_active_count']} "
            f"max_active={entry['max_active_count']} empty={entry['empty_label_count']}"
            f"{caution}{detail}"
        )


def main() -> None:
    print(
        "SCOPE: fixed period L=3, depth-stable events selected by the pinned "
        "argmin global |E[exp(i Theta)]| over original n>=5 rows, prefix ladder "
        "k=2..8; adequate-grade claim is no exhaustion through the adequate-family "
        "range; higher-k entries are reported with inadequacy flags; "
        "Born cap + named instruments inherited; "
        "trajectories realized-state data. Statuses pipeline-derived; audit lane grades."
    )
    print(
        "MACHINERY: K_occ=5, eps=0.6, tau=0.35, dense L=3 Fock dimension 512, "
        "diagonal Kraus pair, named OPS, baseline subtraction, null rng 7777 "
        "with 300 draws."
    )
    env = build()

    scans = {}
    for seed in SEEDS:
        most, rows, worst_sv, min_norm, max_weight_error = scan(env, seed, DEPTH_CAP)
        selected_row = select_most_for_cap(rows, DEPTH_CAP)
        selected_g1 = rows[selected_row][0]
        ladder = ladder_for_row(rows, selected_row)
        scans[seed] = {
            "most": most,
            "rows": rows,
            "worst_sv": worst_sv,
            "min_norm": min_norm,
            "max_weight_error": max_weight_error,
            "selected_row": selected_row,
            "selected_g1": selected_g1,
            "ladder": ladder,
        }

    anchor_theta = scans[ANCHOR_SEED]["rows"][ANCHOR_ROW][1]
    anchor_weights = scans[ANCHOR_SEED]["rows"][ANCHOR_ROW][2]
    anchor_p3 = prefix(anchor_theta, anchor_weights, ANCHOR_K)
    anchor_n95 = null_p95(anchor_theta, anchor_weights, ANCHOR_K)
    check(
        "X3a anchor prefix-3 reproduction",
        abs(anchor_p3 - ANCHOR_PREFIX3) <= ANCHOR_PREFIX3_TOL,
        f"seed=4242 row=9 prefix-3={anchor_p3:.12f} target={ANCHOR_PREFIX3:.3f} tol={ANCHOR_PREFIX3_TOL:.1e}",
    )
    check(
        "X3a anchor null p95 reproduction",
        abs(anchor_n95 - ANCHOR_NULL95) <= ANCHOR_NULL95_TOL,
        f"seed=4242 row=9 null95={anchor_n95:.12f} target={ANCHOR_NULL95:.3f} tol={ANCHOR_NULL95_TOL:.1e}",
    )
    for seed in SEEDS:
        rec = scans[seed]
        check(
            f"X3a rank/no-prune/weight gates seed {seed}",
            rec["worst_sv"] > RANK_TOL
            and rec["min_norm"] > NO_PRUNE_TOL
            and rec["max_weight_error"] <= WEIGHT_TOL,
            (
                f"worst_sv={rec['worst_sv']:.12e} rank_tol>{RANK_TOL:.1e}; "
                f"min_norm={rec['min_norm']:.12e} no_prune_tol>{NO_PRUNE_TOL:.1e}; "
                f"max_abs(sum_w-1)={rec['max_weight_error']:.12e} weight_tol<={WEIGHT_TOL:.1e}"
            ),
        )

    for seed in SEEDS:
        print_ladder(
            seed,
            scans[seed]["selected_row"],
            scans[seed]["selected_g1"],
            scans[seed]["ladder"],
        )

    bad_well_defined = []
    empty_full_label_pairs = set()
    family_inadequate_pairs = []
    for seed in SEEDS:
        for kpref, entry in scans[seed]["ladder"].items():
            if not entry["well_defined"] or entry["active_label_count"] <= 0:
                bad_well_defined.append((seed, kpref))
            if entry["empty_label_count"] > 0:
                empty_full_label_pairs.add((seed, kpref))
            if not entry["family_adequate"]:
                family_inadequate_pairs.append(
                    f"seed={seed}/k={kpref}/min_active={entry['min_active_count']}/"
                    f"active={entry['active_label_count']}/required_active={entry['required_active_family_count']}/"
                    f"empty={entry['empty_label_count']}"
                )
    check(
        "X3c every landed ladder statistic is finite and has at least one realized family",
        not bad_well_defined,
        "bad_entries="
        + repr(bad_well_defined)
        + "; family_inadequate_flags="
        + "; ".join(family_inadequate_pairs),
    )
    check(
        "X3c literal full-label coverage exposes exactly the seed-99 k=8 empty-sector obstruction",
        empty_full_label_pairs == EXPECTED_EMPTY_FULL_LABEL_PAIRS,
        f"empty_full_label_pairs={sorted(empty_full_label_pairs)}; expected={sorted(EXPECTED_EMPTY_FULL_LABEL_PAIRS)}",
    )

    observed_adequate_sets = {}
    observed_theorem_clear_sets = {}
    observed_family_inadequate_sets = {}
    observed_adequate_kmax = {}
    for seed in SEEDS:
        adequate_set = {
            kpref for kpref, entry in scans[seed]["ladder"].items() if entry["family_adequate"]
        }
        theorem_clear_set = {
            kpref for kpref, entry in scans[seed]["ladder"].items() if entry["theorem_clears"]
        }
        family_inadequate_set = {
            kpref for kpref, entry in scans[seed]["ladder"].items() if not entry["family_adequate"]
        }
        observed_adequate_sets[seed] = adequate_set
        observed_theorem_clear_sets[seed] = theorem_clear_set
        observed_family_inadequate_sets[seed] = family_inadequate_set
        observed_adequate_kmax[seed] = max(adequate_set) if adequate_set else None
        adequate_not_clear = sorted(adequate_set - theorem_clear_set)
        print(
            f"X3d ADEQUATE VERDICT seed={seed} adequate_k_max={observed_adequate_kmax[seed]} "
            f"adequate={sorted(adequate_set)} theorem_clears={sorted(theorem_clear_set)} "
            f"adequate_does_not_clear={adequate_not_clear} "
            f"reported_family_inadequate={sorted(family_inadequate_set)}"
        )
    check(
        "X3d adequate-grade verdict is no exhaustion through each seed's adequate-family range and all higher-k entries are reported family-inadequate",
        observed_adequate_sets == EXPECTED_ADEQUATE_CLEAR_SETS
        and observed_theorem_clear_sets == EXPECTED_ADEQUATE_CLEAR_SETS
        and observed_adequate_kmax == EXPECTED_ADEQUATE_KMAX
        and observed_family_inadequate_sets == EXPECTED_FAMILY_INADEQUATE_SETS,
        (
            "observed_adequate_sets={"
            + ", ".join(f"{s}:{sorted(observed_adequate_sets[s])}" for s in SEEDS)
            + "}; "
            "observed_theorem_clear_sets={"
            + ", ".join(f"{s}:{sorted(observed_theorem_clear_sets[s])}" for s in SEEDS)
            + "}; "
            "observed_family_inadequate_sets={"
            + ", ".join(f"{s}:{sorted(observed_family_inadequate_sets[s])}" for s in SEEDS)
            + "}; "
            f"observed_adequate_kmax={observed_adequate_kmax}; "
            f"expected_adequate_kmax={EXPECTED_ADEQUATE_KMAX}"
        ),
    )

    stability_details = []
    stability_ok = True
    for seed in SEEDS:
        rows = scans[seed]["rows"]
        row11 = select_most_for_cap(rows, CAP_STABILITY_PROBE)
        row12 = select_most_for_cap(rows, DEPTH_CAP)
        ladder11 = ladder_for_row(rows, row11)
        ladder12 = scans[seed]["ladder"] if row12 == scans[seed]["selected_row"] else ladder_for_row(rows, row12)
        diffs = []
        for kpref in PREFIX_KS:
            diffs.append(abs(ladder11[kpref]["stat"] - ladder12[kpref]["stat"]))
            diffs.append(abs(ladder11[kpref]["null95"] - ladder12[kpref]["null95"]))
        max_diff = max(diffs)
        same_event = row11 == row12
        stability_ok = stability_ok and same_event and max_diff <= 1.0e-9
        stability_details.append(
            f"seed={seed}:cap11_row={row11},cap12_row={row12},max_ladder_diff={max_diff:.3e}"
        )
    check(
        "X3e cap-11 vs cap-12 depth-stability of the selected event and k-ladder",
        stability_ok,
        "; ".join(stability_details),
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        sys.exit(1)


if __name__ == "__main__":
    main()
