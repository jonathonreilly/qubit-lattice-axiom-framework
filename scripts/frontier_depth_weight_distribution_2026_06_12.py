#!/usr/bin/env python3
"""Finite-dimensional verification for det-phase tone weights.

Source draft:
    docs/HARMONIC_DEPTH_WEIGHT_DISTRIBUTION_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md

Scope: exact L=3 realized-state data.  The audit lane grades.

Run:
    python3 scripts/frontier_depth_weight_distribution_2026_06_12.py
"""
from __future__ import annotations

import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "docs" / "HARMONIC_DEPTH_WEIGHT_DISTRIBUTION_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md"
CACHE = REPO / "logs" / "runner-cache" / "frontier_depth_weight_distribution_2026_06_12.txt"

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
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


@dataclass(frozen=True)
class StateSpec:
    label: str
    k_occ: int
    seed: int


@dataclass(frozen=True)
class ToneWeight:
    gap: float
    weight: float
    share: float


@dataclass(frozen=True)
class StateAnalysis:
    spec: StateSpec
    capture4_w64: float
    rank_w128: int
    gap_count: int
    tone_weights: tuple[ToneWeight, ...]
    participation_ratio: float
    entropy: float
    exp_entropy: float
    center_share: float
    max_tone_weight: float
    gap_second_moment: float
    null_tone_weights: tuple[ToneWeight, ...]
    null_gap_count: int
    null_center_share: float
    null_gap_second_moment: float


L = 3
NC = 3
DIM = L * NC
TAU = 0.35
T_STEPS = 256
CAPTURE_WINDOW = 64
RANK_WINDOW = 128
RANK_REL_FLOOR = 1.0e-6
COUPLING_FLOOR = 1.0e-8

ANCHOR_CAPTURE_TOL = 1.0e-2
WEIGHT_TOL = 5.0e-12
METRIC_TOL = 5.0e-12

STATES = (
    StateSpec("K=3", 3, 391),
    StateSpec("K=4", 4, 99),
    StateSpec("K=5(seed=99)", 5, 99),
    StateSpec("K=6", 6, 466),
)

ANCHOR_CAPTURE4_W64 = (
    (3, 0.898),
    (4, 0.778),
    (6, 0.995),
)
FROZEN_CAPTURE4_W64 = (
    (3, 0.8981300885645052),
    (4, 0.7776195573427411),
    (5, 0.8991555454934871),
    (6, 0.9949365168913127),
)
FROZEN_RANK_W128 = (
    (3, 71),
    (4, 84),
    (5, 36),
    (6, 35),
)
FROZEN_GAP_COUNTS = (
    (3, 3),
    (4, 3),
    (5, 3),
    (6, 3),
)
FROZEN_TONE_WEIGHTS = (
    (3, ((-3.0, 0.37098525695055695), (0.0, 2.544541431436687), (3.0, 0.370985256950557))),
    (4, ((-3.0, 0.47768736255509264), (0.0, 3.088920133342336), (3.0, 0.47768736255509264))),
    (5, ((-3.0, 0.38734384700391267), (0.0, 3.8916132079458117), (3.0, 0.38734384700391267))),
    (6, ((-3.0, 0.2298062233414999), (0.0, 4.683222031818805), (3.0, 0.2298062233414999))),
)
FROZEN_PR = (
    (3, 1.6001835299148852),
    (4, 1.6359923319826128),
    (5, 1.4098254062809743),
    (6, 1.2001324062162435),
)
FROZEN_ENTROPY = (
    (3, 0.6905914723328893),
    (4, 0.7104332065111594),
    (5, 0.5645895003314196),
    (6, 0.36302280300593776),
)
FROZEN_CENTER_SHARE = (
    (3, 0.7742376944791992),
    (4, 0.7637722375475505),
    (5, 0.833982481994788),
    (6, 0.9106305192974259),
)
FROZEN_NULL_CENTER_SHARE = (
    (3, 0.11288115276040041),
    (4, 0.11811388122622478),
    (5, 0.08300875900260604),
    (6, 0.04468474035128705),
)
FROZEN_GAP_SECOND_MOMENT = (
    (3, 2.0318607496872074),
    (4, 2.126049862072046),
    (5, 1.4941576620469088),
    (6, 0.8043253263231669),
)
FROZEN_NULL_GAP_SECOND_MOMENT = (
    (3, 7.984069625156396),
    (4, 7.936975068963978),
    (5, 8.252921168976547),
    (6, 8.597837336838417),
)
FROZEN_NULL_GAP_SECOND_DELTA = (
    (3, 5.952208875469188),
    (4, 5.810925206891932),
    (5, 6.758763506929638),
    (6, 7.79351201051525),
)

EXPECTED_CAPTURE_DESCENDING = (6, 5, 3, 4)
EXPECTED_PR_ASCENDING = (6, 5, 3, 4)
EXPECTED_ENTROPY_ASCENDING = (6, 5, 3, 4)
EXPECTED_CENTER_DESCENDING = (6, 5, 3, 4)
EXPECTED_NULL_CENTER_DESCENDING = (4, 3, 5, 6)

# Fixed cyclic null on sorted tones [-3, 0, +3]:
# new[-3] = old[0], new[0] = old[+3], new[+3] = old[-3].
NULL_PERMUTATION = (1, 2, 0)


def lattice_hamiltonian(n_sites: int) -> np.ndarray:
    """Color-diagonal nearest-neighbor hopping on a periodic n-site ring."""
    h = np.zeros((n_sites * NC, n_sites * NC), dtype=complex)
    for x in range(n_sites):
        y = (x + 1) % n_sites
        for c in range(NC):
            h[NC * x + c, NC * y + c] = -1.0
            h[NC * y + c, NC * x + c] = -1.0
    return h


def polar_u(m: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(m.conj().T @ m)
    if float(np.min(w)) <= 1.0e-14:
        raise FloatingPointError(f"polar block singular: min eig={float(np.min(w)):.3e}")
    return m @ v @ np.diag(w**-0.5) @ v.conj().T


def state_modes(dim: int, k_occ: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(dim, k_occ)) + 1j * rng.normal(size=(dim, k_occ))
    q, r = np.linalg.qr(z)
    phases = np.exp(-1j * np.angle(np.diag(r)))
    q = q @ np.diag(phases)
    return q[:, :k_occ]


def phase_increment_sequence(
    spec: StateSpec,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    q = state_modes(DIM, spec.k_occ, spec.seed)
    rho0 = q @ q.conj().T
    phases = []
    for t in range(T_STEPS + 1):
        u = evecs @ np.diag(np.exp(-1j * TAU * evals * t)) @ evecs.conj().T
        rho_t = u @ rho0 @ u.conj().T
        block_01 = rho_t[0:NC, NC : 2 * NC]
        phases.append(float(np.angle(np.linalg.det(polar_u(block_01)))))
    raw = np.diff(np.unwrap(np.array(phases)))
    centered = raw - float(np.mean(raw))
    return rho0, centered


def trajectory_hankel(x: np.ndarray, window: int) -> np.ndarray:
    if len(x) < window:
        raise ValueError("sequence shorter than Hankel window")
    return np.column_stack([x[i : i + window] for i in range(len(x) - window + 1)])


def hankel_svals(x: np.ndarray, window: int) -> np.ndarray:
    return np.linalg.svd(trajectory_hankel(x, window), compute_uv=False)


def sv_capture(svals: np.ndarray, order: int) -> float:
    total = float(np.sum(svals * svals))
    kept = float(np.sum(svals[:order] * svals[:order]))
    return kept / total


def hankel_rank(svals: np.ndarray) -> int:
    floor = RANK_REL_FLOOR * float(svals[0])
    return int(np.sum(svals >= floor))


def site01_projector(n_sites: int) -> np.ndarray:
    p = np.zeros((n_sites * NC, n_sites * NC), dtype=complex)
    p[0:NC, 0:NC] = np.eye(NC)
    p[NC : 2 * NC, NC : 2 * NC] = np.eye(NC)
    return p


def coupled_tone_weights(
    rho0: np.ndarray,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> tuple[ToneWeight, ...]:
    """Aggregate coupled spectral-pair amplitudes by distinct gap.

    This mirrors the landed coupled-gap inventory.  For eigenbasis V and
    site-0/1 projector P, each propagating pair contributes amplitude
    |(V^* rho0 V)_{ab}| |(V^* P V)_{ba}| to the tone g = lambda_a-lambda_b.
    """
    occ = evecs.conj().T @ rho0 @ evecs
    p01 = evecs.conj().T @ site01_projector(L) @ evecs
    weights: dict[float, float] = {}
    for a in range(len(evals)):
        for b in range(len(evals)):
            weight = abs(occ[a, b]) * abs(p01[b, a])
            if weight > COUPLING_FLOOR:
                gap = round(float(evals[a] - evals[b]), 12)
                weights[gap] = weights.get(gap, 0.0) + float(weight)
    total = sum(weights.values())
    return tuple(
        ToneWeight(gap=gap, weight=weights[gap], share=weights[gap] / total)
        for gap in sorted(weights)
    )


def participation_ratio(tone_weights: tuple[ToneWeight, ...]) -> float:
    weights = np.array([tone.weight for tone in tone_weights], dtype=float)
    total = float(np.sum(weights))
    return total * total / float(np.sum(weights * weights))


def entropy(tone_weights: tuple[ToneWeight, ...]) -> float:
    shares = np.array([tone.share for tone in tone_weights], dtype=float)
    return -float(np.sum(shares * np.log(shares)))


def gap_second_moment(tone_weights: tuple[ToneWeight, ...]) -> float:
    return float(sum(tone.share * tone.gap * tone.gap for tone in tone_weights))


def support_gap_count(tone_weights: tuple[ToneWeight, ...]) -> int:
    return sum(1 for tone in tone_weights if tone.weight > COUPLING_FLOOR)


def cyclic_null(tone_weights: tuple[ToneWeight, ...]) -> tuple[ToneWeight, ...]:
    if len(tone_weights) != len(NULL_PERMUTATION):
        raise ValueError("null permutation length does not match tone table")
    gaps = [tone.gap for tone in tone_weights]
    weights = [tone_weights[idx].weight for idx in NULL_PERMUTATION]
    total = sum(weights)
    return tuple(
        ToneWeight(gap=gap, weight=weight, share=weight / total)
        for gap, weight in zip(gaps, weights)
    )


def center_share(tone_weights: tuple[ToneWeight, ...]) -> float:
    for tone in tone_weights:
        if tone.gap == 0.0:
            return tone.share
    raise ValueError("zero tone missing")


def analyze_state(
    spec: StateSpec,
    evals: np.ndarray,
    evecs: np.ndarray,
) -> StateAnalysis:
    rho0, increments = phase_increment_sequence(spec, evals, evecs)
    svals_w64 = hankel_svals(increments, CAPTURE_WINDOW)
    svals_w128 = hankel_svals(increments, RANK_WINDOW)
    tones = coupled_tone_weights(rho0, evals, evecs)
    null_tones = cyclic_null(tones)
    ent = entropy(tones)
    return StateAnalysis(
        spec=spec,
        capture4_w64=sv_capture(svals_w64, 4),
        rank_w128=hankel_rank(svals_w128),
        gap_count=support_gap_count(tones),
        tone_weights=tones,
        participation_ratio=participation_ratio(tones),
        entropy=ent,
        exp_entropy=math.exp(ent),
        center_share=center_share(tones),
        max_tone_weight=max(tone.weight for tone in tones),
        gap_second_moment=gap_second_moment(tones),
        null_tone_weights=null_tones,
        null_gap_count=support_gap_count(null_tones),
        null_center_share=center_share(null_tones),
        null_gap_second_moment=gap_second_moment(null_tones),
    )


def record_for(records: tuple[StateAnalysis, ...], k_occ: int) -> StateAnalysis:
    for record in records:
        if record.spec.k_occ == k_occ:
            return record
    raise KeyError(k_occ)


def ordered_by(
    records: tuple[StateAnalysis, ...],
    attr_name: str,
    reverse: bool,
) -> tuple[int, ...]:
    return tuple(
        record.spec.k_occ
        for record in sorted(records, key=lambda item: getattr(item, attr_name), reverse=reverse)
    )


def close_tuple(
    observed: tuple[tuple[int, float], ...],
    frozen: tuple[tuple[int, float], ...],
    tol: float,
) -> bool:
    if len(observed) != len(frozen):
        return False
    return all(
        observed_k == frozen_k and abs(observed_value - frozen_value) <= tol
        for (observed_k, observed_value), (frozen_k, frozen_value) in zip(observed, frozen)
    )


def tone_weights_close(
    records: tuple[StateAnalysis, ...],
    frozen: tuple[tuple[int, tuple[tuple[float, float], ...]], ...],
) -> bool:
    if len(records) != len(frozen):
        return False
    gates = []
    for record, (frozen_k, frozen_tones) in zip(records, frozen):
        if len(record.tone_weights) != len(frozen_tones):
            return False
        gates.append(record.spec.k_occ == frozen_k)
        for tone, (frozen_gap, frozen_weight) in zip(record.tone_weights, frozen_tones):
            gates.append(tone.gap == frozen_gap)
            gates.append(abs(tone.weight - frozen_weight) <= WEIGHT_TOL)
    return all(gates)


def frozen_detail(rows: tuple[tuple[int, float], ...]) -> str:
    return ", ".join(f"K{k}:{value:.12g}" for k, value in rows)


def main() -> int:
    print("=" * 78)
    print("Depth weight distribution runner: L=3 det-phase coupled tones")
    print("=" * 78)
    print(f"constants: L={L}, NC={NC}, tau={TAU}, T={T_STEPS}")
    print(
        f"Hankel capture window={CAPTURE_WINDOW}, rank window={RANK_WINDOW}, "
        f"rank relative threshold={RANK_REL_FLOOR:.1e}, coupling floor={COUPLING_FLOOR:.1e}"
    )
    print()

    h = lattice_hamiltonian(L)
    evals, evecs = np.linalg.eigh(h)
    records = tuple(analyze_state(spec, evals, evecs) for spec in STATES)

    print("S0 anchors")
    print("-" * 78)
    for k_occ, expected_capture in ANCHOR_CAPTURE4_W64:
        record = record_for(records, k_occ)
        check(
            f"ANCHOR: K={k_occ} capture@order4/window64 reproduces {expected_capture:.3f}",
            abs(record.capture4_w64 - expected_capture) <= ANCHOR_CAPTURE_TOL,
            f"observed={record.capture4_w64:.12f}, tol={ANCHOR_CAPTURE_TOL:.1e}",
        )

    observed_capture4 = tuple((record.spec.k_occ, record.capture4_w64) for record in records)
    check(
        "ANCHOR: capture@order4/window64 frozen table is reproduced",
        close_tuple(observed_capture4, FROZEN_CAPTURE4_W64, METRIC_TOL),
        frozen_detail(observed_capture4),
    )

    observed_ranks = tuple((record.spec.k_occ, record.rank_w128) for record in records)
    check(
        "ANCHOR: trajectory ranks at window=128 threshold=1e-6 reproduce 71/84/36/35",
        observed_ranks == FROZEN_RANK_W128,
        str(observed_ranks),
    )

    observed_gap_counts = tuple((record.spec.k_occ, record.gap_count) for record in records)
    check(
        "ANCHOR: coupled spectral gap count is exactly 3 for every state",
        observed_gap_counts == FROZEN_GAP_COUNTS,
        str(observed_gap_counts),
    )

    check(
        "anti-fabrication: every state has max tone weight above 1e-8",
        min(record.max_tone_weight for record in records) > COUPLING_FLOOR,
        ", ".join(f"K{record.spec.k_occ}:{record.max_tone_weight:.12g}" for record in records),
    )

    print()
    print("S1 tone-weight tables")
    print("-" * 78)
    for record in records:
        print(
            f"  {record.spec.label:12s} seed={record.spec.seed:3d} "
            f"capture4_w64={record.capture4_w64:.16g} rank_w128={record.rank_w128:d} "
            f"gap_count={record.gap_count:d}"
        )
        for tone in record.tone_weights:
            print(
                f"    g={tone.gap:+.1f}  "
                f"w={tone.weight:.16g}  share={tone.share:.16g}"
            )
        print(
            f"    PR={record.participation_ratio:.16g}  "
            f"entropy={record.entropy:.16g}  exp_entropy={record.exp_entropy:.16g}  "
            f"center_share={record.center_share:.16g}  gap2={record.gap_second_moment:.16g}"
        )

    check(
        "S1: frozen tone-weight table is reproduced exactly within 5e-12",
        tone_weights_close(records, FROZEN_TONE_WEIGHTS),
        "weights by K in sorted gap order (-3,0,+3)",
    )

    print()
    print("S2 concentration gates")
    print("-" * 78)
    observed_pr = tuple((record.spec.k_occ, record.participation_ratio) for record in records)
    observed_entropy = tuple((record.spec.k_occ, record.entropy) for record in records)
    observed_center = tuple((record.spec.k_occ, record.center_share) for record in records)
    check(
        "S2: frozen participation-ratio table is reproduced",
        close_tuple(observed_pr, FROZEN_PR, METRIC_TOL),
        frozen_detail(observed_pr),
    )
    check(
        "S2: frozen entropy table is reproduced",
        close_tuple(observed_entropy, FROZEN_ENTROPY, METRIC_TOL),
        frozen_detail(observed_entropy),
    )
    check(
        "S2: frozen center-share table is reproduced",
        close_tuple(observed_center, FROZEN_CENTER_SHARE, METRIC_TOL),
        frozen_detail(observed_center),
    )

    capture_order = ordered_by(records, "capture4_w64", reverse=True)
    pr_order = ordered_by(records, "participation_ratio", reverse=False)
    entropy_order = ordered_by(records, "entropy", reverse=False)
    center_order = ordered_by(records, "center_share", reverse=True)
    check(
        "S2: lower PR means stronger concentration; order is K6<K5<K3<K4",
        pr_order == EXPECTED_PR_ASCENDING,
        f"PR order={pr_order}",
    )
    check(
        "S2: entropy gives the same concentration order K6<K5<K3<K4",
        entropy_order == EXPECTED_ENTROPY_ASCENDING,
        f"entropy order={entropy_order}",
    )
    check(
        "S2: center-tone share ranks K6,K5,K3,K4",
        center_order == EXPECTED_CENTER_DESCENDING,
        f"center order={center_order}",
    )
    check(
        "S2: capture-at-order-4 is monotone with inverse PR over the four realized states",
        capture_order == EXPECTED_CAPTURE_DESCENDING and pr_order == EXPECTED_PR_ASCENDING,
        f"capture order={capture_order}, PR order={pr_order}",
    )

    print()
    print("S3 cyclic permutation null")
    print("-" * 78)
    observed_null_center = tuple((record.spec.k_occ, record.null_center_share) for record in records)
    observed_null_gap_counts = tuple((record.spec.k_occ, record.null_gap_count) for record in records)
    observed_gap2 = tuple((record.spec.k_occ, record.gap_second_moment) for record in records)
    observed_null_gap2 = tuple((record.spec.k_occ, record.null_gap_second_moment) for record in records)
    observed_null_gap2_delta = tuple(
        (
            record.spec.k_occ,
            abs(record.null_gap_second_moment - record.gap_second_moment),
        )
        for record in records
    )
    for record in records:
        print(
            f"  K={record.spec.k_occ}: cyclic-null center_share={record.null_center_share:.16g} "
            f"gap2={record.null_gap_second_moment:.16g} "
            f"delta_gap2={abs(record.null_gap_second_moment - record.gap_second_moment):.16g}"
        )

    check(
        "S3: cyclic shuffle preserves the fixed three-tone support",
        observed_null_gap_counts == FROZEN_GAP_COUNTS,
        str(observed_null_gap_counts),
    )
    check(
        "S3: cyclic-null center-share table is frozen and reproduced",
        close_tuple(observed_null_center, FROZEN_NULL_CENTER_SHARE, METRIC_TOL),
        frozen_detail(observed_null_center),
    )
    check(
        "S3: real gap-second-moment table is frozen and reproduced",
        close_tuple(observed_gap2, FROZEN_GAP_SECOND_MOMENT, METRIC_TOL),
        frozen_detail(observed_gap2),
    )
    check(
        "S3: cyclic-null gap-second-moment table is frozen and reproduced",
        close_tuple(observed_null_gap2, FROZEN_NULL_GAP_SECOND_MOMENT, METRIC_TOL),
        frozen_detail(observed_null_gap2),
    )
    check(
        "S3: cyclic shuffle changes the depth-relevant gap-second-moment by frozen nonzero deltas",
        close_tuple(observed_null_gap2_delta, FROZEN_NULL_GAP_SECOND_DELTA, METRIC_TOL),
        frozen_detail(observed_null_gap2_delta),
    )
    null_center_order = ordered_by(records, "null_center_share", reverse=True)
    check(
        "S3: cyclic-null center order is K4,K3,K5,K6, not the capture order",
        null_center_order == EXPECTED_NULL_CENTER_DESCENDING
        and null_center_order != EXPECTED_CAPTURE_DESCENDING,
        f"null center order={null_center_order}, capture order={capture_order}",
    )

    print()
    print("S4 note hygiene")
    print("-" * 78)
    note = NOTE.read_text(encoding="utf-8")
    note_norm = " ".join(note.split())
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note)
    expected_links = [
        (
            "`DET_PHASE_HARMONIC_DEPTH_STATE_DEPENDENT_BOUNDED_THEOREM_NOTE_2026-06-12.md`",
            "DET_PHASE_HARMONIC_DEPTH_STATE_DEPENDENT_BOUNDED_THEOREM_NOTE_2026-06-12.md",
        ),
        (
            "`HARMONIC_DEPTH_HANKEL_RANK_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md`",
            "HARMONIC_DEPTH_HANKEL_RANK_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md",
        ),
        (
            "`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`",
            "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        ),
    ]
    check(
        "S4: canonical claim type and status-authority front matter are present",
        "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane" in note
        and "**No-promotion statement:**" in note
        and "**Type:**" not in note
        and "draft source note" not in note.lower(),
    )
    check(
        "S4: dependency links are exactly the depth anchors plus realized-state primitive",
        links == expected_links,
        f"links={links}",
    )
    check(
        "S4: realized-state primitive boundary is not widened",
        "pointwise evaluation on supplied law-admissible realized states only" in note_norm
        and "no state selection, typicality, weighting, or averaging rule is imported" in note_norm,
    )
    check(
        "S4: causal/generative interpretation remains outside this runner",
        "Any broader causal or generative interpretation remains the named follow-on" in note,
    )
    check(
        "S4: note, runner, and cache are the touched files in this spec path set",
        _touched_spec_files_ok(),
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("SCOPE: exact finite one-body L=3 gauge-link system, realized seeds only.")
    print("CLAIM TESTED: coupled-gap count is identical (3 each), while the tone-weight")
    print("  distribution is ordered by concentration: K6 is most concentrated, K3/K4")
    print("  are least concentrated, and inverse PR is monotone with order-4 capture.")
    return 0 if FAIL == 0 else 1


def _touched_spec_files_ok() -> bool:
    import subprocess

    status = subprocess.run(
        [
            "git",
            "status",
            "--short",
            "--",
            str(NOTE.relative_to(REPO)),
            str(Path(__file__).relative_to(REPO)),
            str(CACHE.relative_to(REPO)),
        ],
        cwd=REPO,
        check=False,
        text=True,
        capture_output=True,
    )
    touched = [line for line in status.stdout.splitlines() if line.strip()]
    allowed = {"??", " A", "A ", "AM", " M"}
    return len(touched) == 3 and all(line[:2] in allowed for line in touched)


if __name__ == "__main__":
    sys.exit(main())
