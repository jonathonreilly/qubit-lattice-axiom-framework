#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/WITHIN_SECTOR_K2_THREE_SEED_MIXED_EVENT_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_within_sector_k2_mixed_event_evidence_2026_06_12.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


L, NM = 3, 9
RANK_TOL = 1e-8
DEPTH_CAP = 12
SEEDS = (4242, 99, 7)
SELECTED_DEPTH = {4242: 9, 99: 7, 7: 4}
ADEQUATE_ESS = 8.0
NULL_DRAWS = 300
NULL_SEED = 7777
EPS = 0.6


def ann(j: int, n: int) -> np.ndarray:
    sz = np.array([[1, 0], [0, -1]], float)
    sm = np.array([[0, 1], [0, 0]], float)
    ops = [sz] * j + [sm] + [np.eye(2)] * (n - j - 1)
    out = np.array([[1.0]])
    for op in ops:
        out = np.kron(out, op)
    return out


A9 = [ann(j, NM) for j in range(NM)]
AD9 = [a.T for a in A9]

h9 = np.zeros((NM, NM))
for x in range(L):
    for c in range(3):
        a = 3 * x + c
        b = 3 * ((x + 1) % L) + c
        h9[a, b] = h9[b, a] = -1.0

H = sum(
    h9[i, j] * (AD9[i] @ A9[j]).astype(complex)
    for i in range(NM)
    for j in range(NM)
)
N_site0 = sum(AD9[c] @ A9[c] for c in range(3))
OPS = np.array([(AD9[i] @ A9[3 + j]).astype(complex) for i in range(3) for j in range(3)])
U_step = expm(-1j * H * 0.35)


def polar_u(M: np.ndarray) -> np.ndarray:
    U, _s, Vh = np.linalg.svd(M)
    return U @ Vh


def kraus_pair(Nop: np.ndarray, eps: float) -> tuple[np.ndarray, np.ndarray]:
    w, V = np.linalg.eigh(Nop)
    centered = w - w.mean()
    Nt = centered / max(abs(centered))
    Kp = (V @ np.diag(np.sqrt((1 + eps * Nt) / 2)) @ V.T).astype(complex)
    Km = (V @ np.diag(np.sqrt((1 - eps * Nt) / 2)) @ V.T).astype(complex)
    return Kp, Km


KB = kraus_pair(N_site0, EPS)


def slater(P: np.ndarray) -> np.ndarray:
    vac = np.zeros(2**NM)
    vac[int(np.argmin(np.diag(sum(AD9[m] @ A9[m] for m in range(NM)).real)))] = 1.0
    psi = vac.astype(complex)
    for k in range(P.shape[1]):
        psi = sum(P[m, k] * AD9[m].astype(complex) for m in range(NM)) @ psi
    return psi / np.linalg.norm(psi)


def dets_of(states: np.ndarray) -> tuple[np.ndarray, float]:
    B = states.shape[0]
    M = np.empty((B, 9), complex)
    for k in range(9):
        M[:, k] = np.einsum("bi,bi->b", states.conj(), states @ OPS[k].T)
    M = M.reshape(B, 3, 3)
    sv_min = float(np.min(np.linalg.svd(M, compute_uv=False)[:, -1]))
    return np.array([np.linalg.det(polar_u(m)) for m in M]), sv_min


def full_scan(seed: int) -> dict[str, object]:
    """Exact Born tree through DEPTH_CAP, following the landed runner ordering."""
    rng = np.random.default_rng(seed)
    psi0 = slater(np.linalg.qr(rng.normal(size=(NM, 5)) + 1j * rng.normal(size=(NM, 5)))[0])

    sf = psi0[None, :].copy()
    base = []
    dprev = None
    for n in range(DEPTH_CAP):
        sf = sf @ U_step.T
        d, _ = dets_of(sf)
        if dprev is not None:
            base.append(float(np.angle(d[0] / dprev[0])))
        dprev = d

    states = psi0[None, :].copy()
    weights = np.array([1.0])
    detprev = None
    Theta = np.zeros(1)
    out: dict[str, object] = {"rows": [], "worst_sv": np.inf, "min_norm": np.inf}
    for n in range(DEPTH_CAP):
        states = states @ U_step.T
        new = np.vstack([states @ KB[0].T, states @ KB[1].T])
        norms = np.einsum("bi,bi->b", new.conj(), new).real
        out["min_norm"] = min(float(out["min_norm"]), float(np.min(norms)))
        assert (norms > 1e-14).all(), "no-prune guard"
        weights = np.concatenate([weights, weights]) * norms
        states = (new.T / np.sqrt(norms)).T

        d, svm = dets_of(states)
        out["worst_sv"] = min(float(out["worst_sv"]), svm)
        if detprev is not None:
            parent = detprev[np.arange(len(d)) % len(detprev)]
            dth = np.angle(d / parent)
            eta = np.angle(np.exp(1j * (dth - base[n - 1])))
            Theta = Theta[np.arange(len(d)) % len(Theta)] + eta
            Z = weights.sum()
            chT = [
                complex(np.sum(weights * np.exp(1j * k * Theta)) / Z)
                for k in (1, 2, 3)
            ]
            out["rows"].append(
                {
                    "n": n + 1,
                    "chT": [abs(c) for c in chT],
                    "Theta": Theta.copy(),
                    "w": weights.copy(),
                }
            )
        detprev = d
    return out


@dataclass(frozen=True)
class Sector:
    label: int
    branches: int
    weight: float
    ess: float
    ch1: float
    ch2: float
    delta: float
    adequate: bool


@dataclass(frozen=True)
class PrefixStats:
    prefix_k: int
    sectors: tuple[Sector, ...]
    adequate: tuple[Sector, ...]
    adequate_weight: float
    weighted_delta: float


def prefix_labels(B: int, prefix_k: int) -> np.ndarray:
    return np.arange(B) % (2**prefix_k)


def sector_ess(w: np.ndarray) -> float:
    z = float(np.sum(w))
    if z <= 0.0:
        return 0.0
    return z * z / float(np.sum(w * w))


def moment_delta(theta: np.ndarray, w: np.ndarray) -> tuple[float, float, float]:
    z = float(np.sum(w))
    ch1 = abs(complex(np.sum(w * np.exp(1j * theta)) / z))
    ch2 = abs(complex(np.sum(w * np.exp(2j * theta)) / z))
    delta = abs(ch2 - ch1**4)
    return float(ch1), float(ch2), float(delta)


def prefix_stats(row: dict[str, object], prefix_k: int, labels: np.ndarray | None = None) -> PrefixStats:
    theta = np.asarray(row["Theta"])
    w = np.asarray(row["w"])
    B = len(w)
    if labels is None:
        labels = prefix_labels(B, prefix_k)

    sectors = []
    for label in range(2**prefix_k):
        mask = labels == label
        branches = int(np.count_nonzero(mask))
        weight = float(np.sum(w[mask]))
        if branches == 0 or weight <= 0.0:
            ess = ch1 = ch2 = delta = 0.0
        else:
            ess = sector_ess(w[mask])
            ch1, ch2, delta = moment_delta(theta[mask], w[mask])
        sectors.append(
            Sector(
                label=label,
                branches=branches,
                weight=weight,
                ess=ess,
                ch1=ch1,
                ch2=ch2,
                delta=delta,
                adequate=ess >= ADEQUATE_ESS,
            )
        )

    adequate = tuple(s for s in sectors if s.adequate)
    adequate_weight = float(sum(s.weight for s in adequate))
    if adequate_weight > 0.0:
        weighted_delta = float(sum(s.weight * s.delta for s in adequate) / adequate_weight)
    else:
        weighted_delta = math.nan
    return PrefixStats(
        prefix_k=prefix_k,
        sectors=tuple(sectors),
        adequate=adequate,
        adequate_weight=adequate_weight,
        weighted_delta=weighted_delta,
    )


def permutation_null(
    row: dict[str, object],
    prefix_k: int,
    n_draws: int = NULL_DRAWS,
    seed: int = NULL_SEED,
) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    B = len(np.asarray(row["w"]))
    labels0 = prefix_labels(B, prefix_k)
    vals = []
    adequate_counts = []
    min_esses = []
    for _ in range(n_draws):
        labels = labels0[rng.permutation(B)]
        st = prefix_stats(row, prefix_k, labels=labels)
        adequate_counts.append(len(st.adequate))
        min_esses.append(min(s.ess for s in st.sectors))
        if not math.isnan(st.weighted_delta):
            vals.append(st.weighted_delta)
    arr = np.array(vals, dtype=float)
    if len(arr) == 0:
        return {
            "n_finite": 0,
            "median": math.nan,
            "p95": math.nan,
            "max": math.nan,
            "adequate_counts": tuple(adequate_counts),
            "min_ess_min": float(min(min_esses)) if min_esses else math.nan,
        }
    return {
        "n_finite": int(len(arr)),
        "median": float(np.quantile(arr, 0.50)),
        "p95": float(np.quantile(arr, 0.95)),
        "max": float(np.max(arr)),
        "adequate_counts": tuple(adequate_counts),
        "min_ess_min": float(min(min_esses)),
    }


def row_for(scan: dict[str, object], depth: int) -> dict[str, object]:
    return next(r for r in scan["rows"] if r["n"] == depth)


def ess_vector(stats: PrefixStats) -> str:
    return "[" + ", ".join(f"{s.ess:.3f}" for s in stats.sectors) + "]"


def delta_vector(stats: PrefixStats) -> str:
    return "[" + ", ".join(f"{s.delta:.3f}" for s in stats.sectors) + "]"


def adequacy_pattern(stats: PrefixStats) -> str:
    return "".join("A" if s.adequate else "u" for s in stats.sectors)


def nontrivial_prefix_testable(row: dict[str, object]) -> bool:
    B = len(np.asarray(row["w"]))
    max_prefix = int(math.log2(B))
    for prefix_k in range(1, max_prefix + 1):
        st = prefix_stats(row, prefix_k)
        if len(st.adequate) == len(st.sectors):
            return True
    return False


def print_prefix_table(seed: int, depth: int, row: dict[str, object], prefix_k: int) -> PrefixStats:
    st = prefix_stats(row, prefix_k)
    print(
        f"seed {seed} depth {depth} prefix-k={prefix_k}: "
        f"B={len(row['w'])}, sectors={len(st.sectors)}, ESS={ess_vector(st)}, "
        f"adequacy={adequacy_pattern(st)}, |delta|={delta_vector(st)}, "
        f"adequate-weighted |delta|={st.weighted_delta:.6f}"
    )
    return st


def compare_record_to_null(seed: int, depth: int, row: dict[str, object], prefix_k: int) -> tuple[PrefixStats, dict[str, object]]:
    st = print_prefix_table(seed, depth, row, prefix_k)
    null = permutation_null(row, prefix_k)
    print(
        f"seed {seed} depth {depth} prefix-k={prefix_k}: permutation null "
        f"draws={NULL_DRAWS}, finite={null['n_finite']}, "
        f"median={null['median']:.6f}, p95={null['p95']:.6f}, max={null['max']:.6f}"
    )
    if math.isnan(st.weighted_delta) or math.isnan(float(null["p95"])):
        check(
            f"V4 record-vs-null absence: seed {seed} depth {depth} prefix-k={prefix_k} has no adequate-sector weighted |delta| comparison",
            math.isnan(st.weighted_delta) or math.isnan(float(null["p95"])),
            f"adequate sectors {len(st.adequate)}/{len(st.sectors)}, null finite {null['n_finite']}",
        )
    elif st.weighted_delta > float(null["p95"]):
        check(
            f"V4 record-vs-null TRUE RELATION: seed {seed} depth {depth} prefix-k={prefix_k} adequate-sector weighted |delta| EXCEEDS permutation-null p95",
            st.weighted_delta > float(null["p95"]),
            f"record {st.weighted_delta:.6f} vs null p95 {float(null['p95']):.6f}",
        )
    else:
        check(
            f"V4 record-vs-null TRUE RELATION: seed {seed} depth {depth} prefix-k={prefix_k} adequate-sector weighted |delta| DOES NOT EXCEED permutation-null p95",
            st.weighted_delta <= float(null["p95"]),
            f"record {st.weighted_delta:.6f} vs null p95 {float(null['p95']):.6f}",
        )
    return st, null


def second_smallest_g1_row_with_min_branches(scan: dict[str, object], min_branches: int) -> dict[str, object]:
    candidates = [
        r for r in scan["rows"]
        if len(np.asarray(r["w"])) >= min_branches
    ]
    candidates.sort(key=lambda r: (float(r["chT"][0]), int(r["n"])))
    if len(candidates) < 2:
        raise RuntimeError("fewer than two seed-7 rows meet the requested branch floor")
    return candidates[1]


RES = {seed: full_scan(seed) for seed in SEEDS}

print("=" * 78)
print("Part 1  pinned L=3 tree, wraparound, and size guards")
print("=" * 78)
check(
    "L=3 finite-lattice wraparound is active in every color channel: site 2 connects back to site 0 and the hopping matrix is Hermitian",
    all(h9[3 * (L - 1) + c, c] == -1.0 and h9[c, 3 * (L - 1) + c] == -1.0 for c in range(3))
    and np.allclose(h9, h9.T),
    f"nonzero directed entries {int(np.count_nonzero(h9))}",
)
check(
    "depth cap 12 exact Born tree has the expected branch count B=2^n on every scanned row for seeds 4242/99/7",
    all(len(row["w"]) == 2 ** int(row["n"]) for seed in SEEDS for row in RES[seed]["rows"]),
    "; ".join(
        f"seed {seed}: max depth {max(int(r['n']) for r in RES[seed]['rows'])}, "
        f"max B {max(len(r['w']) for r in RES[seed]['rows'])}"
        for seed in SEEDS
    ),
)
check(
    "rank guard holds on every branch through depth cap 12 for the selected three seeds",
    min(float(RES[seed]["worst_sv"]) for seed in SEEDS) > RANK_TOL,
    f"worst min-sv {min(float(RES[seed]['worst_sv']) for seed in SEEDS):.4f}",
)
check(
    "Born no-prune guard holds through depth cap 12 for the selected three seeds",
    min(float(RES[seed]["min_norm"]) for seed in SEEDS) > 1e-14,
    f"minimum daughter norm {min(float(RES[seed]['min_norm']) for seed in SEEDS):.6e}",
)

print("=" * 78)
print("Part 2  V4a k=2 ESS adequacy on the landed selected events")
print("=" * 78)
selected_rows = {seed: row_for(RES[seed], SELECTED_DEPTH[seed]) for seed in SEEDS}
selected_k2 = {
    seed: print_prefix_table(seed, SELECTED_DEPTH[seed], selected_rows[seed], 2)
    for seed in SEEDS
}

all_four_adequate = {
    seed: len(selected_k2[seed].adequate) == len(selected_k2[seed].sectors)
    for seed in SEEDS
}
untestable_seed7_any_prefix = not nontrivial_prefix_testable(selected_rows[7])

if all_four_adequate[4242] and all_four_adequate[99] and not all_four_adequate[7]:
    check(
        "V4a TRUE ADEQUACY PATTERN: seeds 4242 and 99 are k=2 ESS-adequate in all four selected-event sectors, while seed 7 is not k=2 testable",
        all_four_adequate[4242] and all_four_adequate[99] and not all_four_adequate[7],
        "patterns "
        + ", ".join(f"seed {seed}: {adequacy_pattern(selected_k2[seed])}" for seed in SEEDS),
    )
else:
    check(
        "V4a TRUE ADEQUACY PATTERN: selected-event k=2 adequacy pattern is "
        + ", ".join(f"seed {seed}={adequacy_pattern(selected_k2[seed])}" for seed in SEEDS),
        all(
            adequacy_pattern(selected_k2[seed]) == "".join("A" if s.adequate else "u" for s in selected_k2[seed].sectors)
            for seed in SEEDS
        ),
        "A=ESS>=8, u=ESS<8",
    )

if not all_four_adequate[7] and untestable_seed7_any_prefix:
    check(
        "V4a TRUE SEED-7 DATUM: the landed seed 7 depth-4 event is too weight-concentrated for ANY nontrivial prefix test at ESS >= 8",
        not all_four_adequate[7] and untestable_seed7_any_prefix,
        f"k=2 ESS {ess_vector(selected_k2[7])}; B={len(selected_rows[7]['w'])}",
    )
elif not all_four_adequate[7]:
    check(
        "V4a TRUE SEED-7 DATUM: the landed seed 7 depth-4 event is not k=2 adequate, but some coarser nontrivial prefix is adequate",
        not all_four_adequate[7] and not untestable_seed7_any_prefix,
        f"k=2 ESS {ess_vector(selected_k2[7])}; B={len(selected_rows[7]['w'])}",
    )
else:
    check(
        "V4a TRUE SEED-7 DATUM: the landed seed 7 depth-4 event is k=2 ESS-adequate in all four sectors",
        all_four_adequate[7],
        f"k=2 ESS {ess_vector(selected_k2[7])}; B={len(selected_rows[7]['w'])}",
    )

print("=" * 78)
print("Part 3  V4b record-vs-null on k=2 testable selected events")
print("=" * 78)
testable_selected = [seed for seed in SEEDS if all_four_adequate[seed]]
check(
    "V4b selected-event testable-seed set is exactly the seeds with all four k=2 sectors at ESS >= 8",
    testable_selected == [seed for seed in SEEDS if len(selected_k2[seed].adequate) == 4],
    f"testable seeds {testable_selected}",
)
for seed in testable_selected:
    compare_record_to_null(seed, SELECTED_DEPTH[seed], selected_rows[seed], 2)

print("=" * 78)
print("Part 4  V4c seed 7 next-most-spread adequate-event probe")
print("=" * 78)
if not all_four_adequate[7]:
    probe = second_smallest_g1_row_with_min_branches(RES[7], min_branches=64)
    probe_depth = int(probe["n"])
    probe_B = len(probe["w"])
    sorted_seed7 = sorted(
        [r for r in RES[7]["rows"] if len(r["w"]) >= 64],
        key=lambda r: (float(r["chT"][0]), int(r["n"])),
    )
    check(
        "V4c selector TRUE TARGET: seed 7 probe is the second-smallest global |chi_1| row among rows with at least 64 branches under depth cap 12",
        probe is sorted_seed7[1],
        f"depth {probe_depth}, B={probe_B}, global |chi_1|={float(probe['chT'][0]):.6f}; "
        f"smallest depth {int(sorted_seed7[0]['n'])} |chi_1|={float(sorted_seed7[0]['chT'][0]):.6f}",
    )
    probe_stats = {}
    for prefix_k in (2, 3):
        st, _null = compare_record_to_null(7, probe_depth, probe, prefix_k)
        probe_stats[prefix_k] = st

    adequate_prefixes = [
        k for k, st in probe_stats.items()
        if len(st.adequate) == len(st.sectors)
    ]
    if adequate_prefixes:
        check(
            "V4c TRUE OUTCOME: seed 7's next-most-spread row supplies an adequate within-sector datum",
            len(adequate_prefixes) > 0,
            "adequate prefixes " + ", ".join(f"k={k}" for k in adequate_prefixes),
        )
    else:
        check(
            "V4c TRUE OUTCOME: seed 7's next-most-spread row still supplies no all-sector adequate within-sector datum at k=2 or k=3",
            len(adequate_prefixes) == 0,
            "; ".join(f"k={k} pattern {adequacy_pattern(st)}" for k, st in probe_stats.items()),
        )
else:
    check(
        "V4c not triggered: seed 7 selected event is already k=2 ESS-adequate in all sectors",
        all_four_adequate[7],
        "no next-most-spread fallback probe required",
    )

print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: finite L=3, depth cap 12, selected seeds 4242/99/7, landed selector")
print("  depths 9/7/4.  The ESS adequacy pattern is computed before gating; the")
print("  moment-relation statistic is the adequate-sector weighted | |chi_2| -")
print("  |chi_1|^4 | deviation.  Permutation controls use 300 deterministic label")
print("  draws with rng 7777 and preserve prefix-sector cardinalities.  Seed 7's")
print("  selected event is escalated to the requested next-most-spread row only if")
print("  its landed selected event is not k=2 adequate.  Finite power; branch")
print("  weights are explicit Kraus/Born weights; statuses pipeline-derived.")
print("  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
