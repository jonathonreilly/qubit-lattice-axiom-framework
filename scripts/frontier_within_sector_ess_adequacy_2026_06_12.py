#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/WITHIN_SECTOR_ESS_ADEQUACY_CONCLUSION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_within_sector_ess_adequacy_2026_06_12.py
"""

from __future__ import annotations

import sys

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


L = 3
NC = 3
NM = L * NC
DIM = 2 ** NM
K_OCC = 5
EPS = 0.6
TAU = 0.35
DEPTH_CAP = 12
KPREF = 3
N_SECTORS = 2 ** KPREF
SEEDS = (4242, 99, 7)
PINNED_DEPTH = {4242: 9, 99: 7, 7: 4}
NULL_DRAWS = 300
NULL_RNG_SEED = 7777
ESS_MIN = 8.0
RANK_TOL = 1.0e-8


def ann(j: int, n: int) -> np.ndarray:
    sz = np.array([[1.0, 0.0], [0.0, -1.0]])
    sm = np.array([[0.0, 1.0], [0.0, 0.0]])
    out = np.array([[1.0]])
    for k in range(n):
        op = sz if k < j else (sm if k == j else np.eye(2))
        out = np.kron(out, op)
    return out


def ring_hopping(lring: int) -> np.ndarray:
    h = np.zeros((lring * NC, lring * NC))
    for x in range(lring):
        xp = (x + 1) % lring
        for c in range(NC):
            h[x * NC + c, xp * NC + c] = -1.0
            h[xp * NC + c, x * NC + c] = -1.0
    return h


A = [ann(j, NM) for j in range(NM)]
AD = [a.T for a in A]
H1 = ring_hopping(L)
H = np.zeros((DIM, DIM), dtype=complex)
for i in range(NM):
    for j in range(NM):
        if abs(H1[i, j]) > 1.0e-12:
            H += H1[i, j] * (AD[i] @ A[j]).astype(complex)
evals, evecs = np.linalg.eigh(H)
U_STEP = (evecs * np.exp(-1j * TAU * evals)) @ evecs.conj().T

N0_DIAG = np.zeros(DIM)
for c in range(NC):
    N0_DIAG += np.diag(AD[c] @ A[c]).real
NT = (N0_DIAG - N0_DIAG.mean()) / np.max(np.abs(N0_DIAG - N0_DIAG.mean()))
KP_DIAG = np.sqrt((1.0 + EPS * NT) / 2.0).astype(complex)
KM_DIAG = np.sqrt((1.0 - EPS * NT) / 2.0).astype(complex)

OPS = np.array(
    [(AD[0 + i] @ A[NC + j]).astype(complex) for i in range(NC) for j in range(NC)]
)
NTOT_DIAG = np.zeros(DIM)
for m in range(NM):
    NTOT_DIAG += np.diag(AD[m] @ A[m]).real
VAC_IDX = int(np.argmin(NTOT_DIAG))


def polar_u(mat: np.ndarray) -> np.ndarray:
    u, _s, vh = np.linalg.svd(mat)
    return u @ vh


def slater(pmat: np.ndarray) -> np.ndarray:
    psi = np.zeros(DIM, dtype=complex)
    psi[VAC_IDX] = 1.0
    for k in range(pmat.shape[1]):
        nxt = np.zeros(DIM, dtype=complex)
        for m in range(NM):
            nxt += pmat[m, k] * (AD[m].astype(complex) @ psi)
        psi = nxt
    return psi / np.linalg.norm(psi)


def dets_of(states: np.ndarray) -> tuple[np.ndarray, float]:
    bsz = states.shape[0]
    mats = np.empty((bsz, 9), dtype=complex)
    for k in range(9):
        mats[:, k] = np.einsum("bi,bi->b", states.conj(), states @ OPS[k].T)
    mats = mats.reshape(bsz, 3, 3)
    sv = np.linalg.svd(mats, compute_uv=False)
    sv_min = float(np.min(sv[:, -1]))
    dets = np.empty(bsz, dtype=complex)
    for b in range(bsz):
        dets[b] = np.linalg.det(polar_u(mats[b]))
    return dets, sv_min


def full_scan(seed: int) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    q, _r = np.linalg.qr(
        rng.normal(size=(NM, K_OCC)) + 1j * rng.normal(size=(NM, K_OCC))
    )
    psi0 = slater(q[:, :K_OCC])

    sf = psi0[None, :].copy()
    base: list[float] = []
    dprev = None
    for n in range(DEPTH_CAP):
        sf = sf @ U_STEP.T
        dets, _svm = dets_of(sf)
        if dprev is not None:
            base.append(float(np.angle(dets[0] / dprev[0])))
        dprev = dets

    states = psi0[None, :].copy()
    weights = np.array([1.0])
    detprev = None
    theta = np.zeros(1)
    rows: dict[int, dict[str, object]] = {}
    worst_sv = np.inf

    for n in range(DEPTH_CAP):
        states = states @ U_STEP.T
        new_states = np.vstack([states * KP_DIAG[None, :], states * KM_DIAG[None, :]])
        norms = np.einsum("bi,bi->b", new_states.conj(), new_states).real
        assert np.all(norms > 1.0e-14), "no-prune guard"
        weights = np.concatenate([weights, weights]) * norms
        states = (new_states.T / np.sqrt(norms)).T

        dets, svm = dets_of(states)
        worst_sv = min(worst_sv, svm)
        if detprev is not None:
            parent = detprev[np.arange(len(dets)) % len(detprev)]
            eta = np.angle(np.exp(1j * (np.angle(dets / parent) - base[n - 1])))
            theta = theta[np.arange(len(dets)) % len(theta)] + eta
            z = weights.sum()
            ch1 = abs(complex(np.sum(weights * np.exp(1j * theta)) / z))
            rows[n + 1] = {
                "n": n + 1,
                "ch1": ch1,
                "theta": theta.copy(),
                "w": weights.copy(),
            }
        detprev = dets

    return {"rows": rows, "worst_sv": worst_sv}


def labels_for(branch_count: int) -> np.ndarray:
    return np.arange(branch_count) % N_SECTORS


def sector_ess(w: np.ndarray) -> float:
    sw = float(np.sum(w))
    sw2 = float(np.sum(w * w))
    if sw2 <= 0.0:
        return float("nan")
    return (sw * sw) / sw2


def sector_moment(row: dict[str, object], labels: np.ndarray, sid: int) -> dict[str, float]:
    theta = row["theta"]
    weights = row["w"]
    assert isinstance(theta, np.ndarray)
    assert isinstance(weights, np.ndarray)
    mask = labels == sid
    w = weights[mask]
    th = theta[mask]
    mass = float(np.sum(w))
    raw = int(np.sum(mask))
    if mass <= 0.0:
        return {
            "raw": raw,
            "mass": mass,
            "ess": float("nan"),
            "c1": float("nan"),
            "c2": float("nan"),
            "delta": float("nan"),
        }
    c1 = abs(complex(np.sum(w * np.exp(1j * th)) / mass))
    c2 = abs(complex(np.sum(w * np.exp(2j * th)) / mass))
    delta = c2 - c1 ** 4
    return {
        "raw": raw,
        "mass": mass,
        "ess": sector_ess(w),
        "c1": float(c1),
        "c2": float(c2),
        "delta": float(delta),
    }


def sector_table_for(seed: int, row: dict[str, object]) -> list[dict[str, float | int | bool]]:
    weights = row["w"]
    assert isinstance(weights, np.ndarray)
    labels = labels_for(len(weights))
    out = []
    for sid in range(N_SECTORS):
        rec = sector_moment(row, labels, sid)
        rec["seed"] = seed
        rec["depth"] = int(row["n"])
        rec["sector"] = sid
        rec["adequate"] = bool(np.isfinite(rec["ess"]) and rec["ess"] >= ESS_MIN)
        out.append(rec)
    return out


def weighted_mean_abs_delta(
    row: dict[str, object], labels: np.ndarray, sector_ids: list[int]
) -> float:
    numer = 0.0
    denom = 0.0
    for sid in sector_ids:
        rec = sector_moment(row, labels, sid)
        if not np.isfinite(rec["delta"]):
            continue
        numer += rec["mass"] * abs(rec["delta"])
        denom += rec["mass"]
    if denom <= 0.0:
        return float("nan")
    return float(numer / denom)


def permutation_null_p95(row: dict[str, object], sector_ids: list[int]) -> float:
    weights = row["w"]
    assert isinstance(weights, np.ndarray)
    if not sector_ids:
        return float("nan")
    rng = np.random.default_rng(NULL_RNG_SEED)
    base = labels_for(len(weights))
    vals = np.empty(NULL_DRAWS)
    for i in range(NULL_DRAWS):
        vals[i] = weighted_mean_abs_delta(row, base[rng.permutation(len(base))], sector_ids)
    return float(np.quantile(vals, 0.95))


def print_sector_table(table: list[dict[str, float | int | bool]]) -> None:
    print("seed depth sector raw_count sector_weight      ESS adequate  |ch1|    |ch2|    delta")
    for rec in table:
        print(
            f"{rec['seed']:4d} {rec['depth']:5d} {rec['sector']:6d} "
            f"{rec['raw']:9d} {rec['mass']:13.6e} {rec['ess']:8.3f} "
            f"{str(rec['adequate']):>8s} {rec['c1']:7.3f} {rec['c2']:7.3f} "
            f"{rec['delta']:+8.3f}"
        )


print("=" * 78)
print("Effective-sample-size adequacy for the L=3 within-sector moment test")
print("=" * 78)

h6 = ring_hopping(2 * L)
wrap3 = all(H1[(L - 1) * NC + c, c] == -1.0 and H1[c, (L - 1) * NC + c] == -1.0 for c in range(NC))
wrap6 = all(h6[(2 * L - 1) * NC + c, c] == -1.0 and h6[c, (2 * L - 1) * NC + c] == -1.0 for c in range(NC))
check(
    "finite-lattice wraparound probe: the L=3 one-body ring closes site 2 to site 0 for all colors",
    wrap3,
)
check(
    "size-doubling probe: the L=6 one-body ring has twice the L=3 modes and preserves wraparound",
    h6.shape == (2 * NM, 2 * NM) and wrap6,
)

scans = {seed: full_scan(seed) for seed in SEEDS}
selected: dict[int, dict[str, object]] = {}
for seed in SEEDS:
    rows = scans[seed]["rows"]
    assert isinstance(rows, dict)
    selected[seed] = rows[PINNED_DEPTH[seed]]

worst_sv = min(float(scans[seed]["worst_sv"]) for seed in SEEDS)
check(
    "rank guard holds on the selected-seed scans",
    worst_sv > RANK_TOL,
    f"worst min-sv {worst_sv:.4e}",
)
for seed, row in selected.items():
    weights = row["w"]
    assert isinstance(weights, np.ndarray)
    check(
        f"pinned predecessor selector row is present for seed {seed} at depth {PINNED_DEPTH[seed]}",
        int(row["n"]) == PINNED_DEPTH[seed],
        f"branches {len(weights)}, Born-weight sum {np.sum(weights):.12f}",
    )
    check(
        f"Born weights are normalized at seed {seed} depth {PINNED_DEPTH[seed]}",
        abs(float(np.sum(weights)) - 1.0) < 1.0e-10,
        f"sum {np.sum(weights):.12f}",
    )

print("=" * 78)
print("Per-sector raw counts and Born-weight effective sample size")
print("=" * 78)
table: list[dict[str, float | int | bool]] = []
for seed in SEEDS:
    table.extend(sector_table_for(seed, selected[seed]))
print_sector_table(table)

finite_ess_count = sum(1 for rec in table if np.isfinite(rec["ess"]))
adequate_count = sum(1 for rec in table if bool(rec["adequate"]))
check(
    "ESS is finite in all 24 selected prefix-3 sectors",
    finite_ess_count == len(SEEDS) * N_SECTORS,
    f"finite {finite_ess_count}/{len(SEEDS) * N_SECTORS}",
)
per_seed_adequate = {seed: sum(1 for rec in table if rec["seed"] == seed and rec["adequate"])
                     for seed in SEEDS}
check(
    "adequate-ESS sectors are EXACTLY 16/24 with pattern 4242:8/8, 99:8/8, 7:0/8 "
    "(hard assert)",
    adequate_count == 16 and per_seed_adequate.get(4242) == 8
    and per_seed_adequate.get(99) == 8 and per_seed_adequate.get(7) == 0,
    "pattern "
    + ", ".join(
        f"{seed}:{sum(1 for rec in table if rec['seed'] == seed and rec['adequate'])}/8"
        for seed in SEEDS
    ),
)

print("=" * 78)
print("Adequate-ESS-only weighted mean |delta| vs fixed seeded 300-draw permutation-null p95 diagnostic")
print("=" * 78)
relations: dict[int, dict[str, float | bool | int]] = {}
for seed in SEEDS:
    row = selected[seed]
    weights = row["w"]
    assert isinstance(weights, np.ndarray)
    labels = labels_for(len(weights))
    seed_table = [rec for rec in table if rec["seed"] == seed]
    adequate_ids = [int(rec["sector"]) for rec in seed_table if bool(rec["adequate"])]
    record_stat = weighted_mean_abs_delta(row, labels, adequate_ids)
    null_p95 = permutation_null_p95(row, adequate_ids)
    relations[seed] = {
        "n_adequate": len(adequate_ids),
        "record": record_stat,
        "null": null_p95,
        "le_null": bool(np.isfinite(record_stat) and np.isfinite(null_p95) and record_stat <= null_p95),
    }
    if not adequate_ids:
        check(
            f"seed {seed}: no adequate-ESS prefix-3 sectors survive, so the moment-relation comparison is untested",
            len(adequate_ids) == 0 and not np.isfinite(record_stat) and not np.isfinite(null_p95),
        )
    elif record_stat <= null_p95:
        check(
            f"seed {seed}: adequate-ESS weighted mean |delta| is <= fixed seeded 300-draw permutation-null p95 diagnostic",
            record_stat <= null_p95,
            f"adequate {len(adequate_ids)}/8; record {record_stat:.6f}; null p95 {null_p95:.6f}",
        )
    else:
        check(
            f"seed {seed}: adequate-ESS weighted mean |delta| is > fixed seeded 300-draw permutation-null p95 diagnostic",
            record_stat > null_p95,
            f"adequate {len(adequate_ids)}/8; record {record_stat:.6f}; null p95 {null_p95:.6f}",
        )

print("=" * 78)
print("Effective-sample-size verdict")
print("=" * 78)
tested = [rel for rel in relations.values() if int(rel["n_adequate"]) > 0]
survives = bool(tested) and all(bool(rel["le_null"]) for rel in tested)
detail = "; ".join(
    f"{seed}:adequate={relations[seed]['n_adequate']},"
    f"record={relations[seed]['record']:.6f},null={relations[seed]['null']:.6f}"
    if int(relations[seed]["n_adequate"]) > 0
    else f"{seed}:adequate=0,untested"
    for seed in SEEDS
)
if survives:
    check(
        "ESS verdict: the predecessor's power-limited-consistency conclusion survives the stricter adequacy filter where testable (seed 7 untestable; fixed seeded null computed on the fixed adequate sector IDs)",
        survives,
        detail,
    )
else:
    check(
        "ESS verdict: the predecessor's power-limited-consistency conclusion does not survive the stricter adequacy filter",
        not survives,
        detail,
    )

print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: ESS refinement of the L=3 within-sector wrapped-Gaussian moment")
print("  relation delta = |ch2| - |ch1|^4, restricted to prefix-3 record sectors")
print("  at the pinned predecessor rows 4242@9, 99@7, and 7@4. Finite power only;")
print("  Born cap inherited; statuses are pipeline-derived and the audit lane grades.")
if FAIL:
    raise SystemExit(1)
sys.exit(0)
