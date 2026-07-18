#!/usr/bin/env python3
"""Training-frozen branch and scalar-observable test after Cycle 298.

Use only L=3,4 to select one nonzero-axis-momentum eigenpair family, freeze a
contact-block fingerprint template, a dimensionless eigenphase trend, and one
proper-cubic three-orbit coefficient vector.  Apply that rule without held-size
coefficient or comparator adaptation at declared held L=5,6.  Eigenphases are
reported only as dimensionless spectral data.  A failed held observable is one
route-specific result, not a no-go or axiom-pressure claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs

import carried_relative_extended_green_branch_hunt_2026_07_17 as c298


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "CARRIED_RELATIVE_FROZEN_BRANCH_OBSERVABLE_CYCLE300_NOTE_2026-07-17.md"
)

TRAINING_SIZES = (3, 4)
HELD_SIZES = (5, 6)
SIZES = TRAINING_SIZES + HELD_SIZES
MOMENTUM_INDEX = c298.K_AXIS
BRANCH_PAIR_PHASE_WIDTH = 0.12
HELD_TRACK_PHASE_WIDTH = 0.05
FINGERPRINT_WEIGHT_MINIMUM = 1e-4
FIXED_GREEN_OVERLAP_MINIMUM = 0.50
FIXED_CONTACT_MAXIMUM = 0.60
FIXED_PROJECTION_WEIGHT_MINIMUM = 1e-6
DUPLICATE_EIGENVALUE_TOLERANCE = 1e-8
TOLERANCE = 4e-10

PASS = 0
FAIL = 0


@dataclass
class BranchCandidate:
    length: int
    target_fraction: float
    eigenvalue: complex
    state: np.ndarray
    eigen_residual: float
    local_gap: float
    shift: float
    pole_margin: float


@dataclass
class ProjectionAnalysis:
    coefficients: np.ndarray
    profile: np.ndarray
    weight: float
    contact_fraction: float
    green_overlap: float
    green_residual: float


@dataclass
class FrozenRule:
    training_rows: tuple[BranchCandidate, BranchCandidate]
    fingerprint_template: np.ndarray
    projection_coefficients: np.ndarray
    phase_intercept: float
    phase_inverse_length_slope: float
    training_pair_score: float
    training_pair_score_gap: float


@dataclass
class SelectedRow:
    candidate: BranchCandidate
    predicted_phase_fraction: float
    phase_fraction: float
    phase_distance: float
    fingerprint_overlap: float
    combined_score: float
    combined_score_gap: float
    alternative_trackers_agree: bool
    fixed_profile: np.ndarray
    fixed_projection_weight: float
    fixed_contact_fraction: float
    fixed_green_overlap: float
    fixed_green_residual: float
    adaptive_projection_weight: float
    adaptive_contact_fraction: float
    adaptive_green_overlap: float
    adaptive_green_residual: float


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-300 frozen-rule note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "training l=3,4",
        "declared held-size l=5,6",
        "fixed axis momentum",
        "contact-block fingerprint",
        "dimensionless spectral data",
        "fixed proper-cubic scalar coefficient vector",
        "no held-size coefficient adaptation",
        "held candidate pool has no adaptive projection",
        "three branch trackers",
        "branch crossings",
        "all 24 proper-cubic frames",
        "basis-spanning",
        "theta=0",
        "fixed-versus-adaptive residual",
        "supplied structure inventory",
        "not physical energy",
        "not a rate",
        "not mass",
        "not gravity",
        "no broad no-go",
        "no axiom pressure",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "gate status: fail for the candidate broad negative; do not ship it",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the frozen prediction and no-go boundary", not missing, missing)


def phase_fraction(candidate: BranchCandidate) -> float:
    return float(-np.angle(candidate.eigenvalue) / c298.pole_phase(candidate.length))


def contact_fingerprint(candidate: BranchCandidate) -> tuple[np.ndarray, float]:
    vector = candidate.state[:42].copy()
    weight = float(np.vdot(vector, vector).real)
    if weight <= 0:
        raise ValueError("contact fingerprint has zero weight")
    return vector / np.sqrt(weight), weight


def align_to(reference: np.ndarray, vector: np.ndarray) -> np.ndarray:
    overlap = np.vdot(reference, vector)
    if abs(overlap) < 1e-14:
        raise ValueError("cannot phase-align orthogonal training features")
    return vector * np.conj(overlap / abs(overlap))


def enumerate_spectral_window(
    length: int, target_fraction: float
) -> list[BranchCandidate]:
    """Return forward-phase, below-pole eigenpairs without scalar projection."""

    update = c298.carried_update(length, MOMENTUM_INDEX)
    target_phase = target_fraction * c298.pole_phase(length)
    eigenvalues, eigenvectors = eigs(
        update,
        k=c298.EIGENPAIRS_PER_WINDOW,
        sigma=np.exp(-1j * target_phase),
        which="LM",
        v0=c298.deterministic_start(update.shape[0]),
        tol=2e-11,
        maxiter=50000,
        ncv=max(48, 2 * c298.EIGENPAIRS_PER_WINDOW + 8),
    )
    pole = c298.first_nonzero_laplacian(length)
    rows = []
    for index, eigenvalue in enumerate(eigenvalues):
        phase = float(-np.angle(eigenvalue))
        if phase <= 0:
            continue
        shift = float(6 * (1 - np.cos(phase)))
        pole_margin = pole - shift
        if pole_margin <= c298.POLE_MARGIN_FRACTION * pole:
            continue
        state = eigenvectors[:, index]
        state /= np.linalg.norm(state)
        other = np.delete(eigenvalues, index)
        rows.append(
            BranchCandidate(
                length=length,
                target_fraction=target_fraction,
                eigenvalue=complex(eigenvalue),
                state=state,
                eigen_residual=float(
                    np.linalg.norm(update @ state - eigenvalue * state)
                ),
                local_gap=float(np.min(abs(other - eigenvalue))),
                shift=shift,
                pole_margin=pole_margin,
            )
        )
    return rows


def candidate_pool(length: int) -> tuple[list[BranchCandidate], dict[str, int]]:
    rows: list[BranchCandidate] = []
    raw = forward_below_pole = duplicates = 0
    for target_fraction in c298.K_AXIS_TARGET_FRACTIONS:
        window = enumerate_spectral_window(length, target_fraction)
        raw += c298.EIGENPAIRS_PER_WINDOW
        forward_below_pole += len(window)
        for candidate in window:
            if any(
                abs(candidate.eigenvalue - prior.eigenvalue)
                < DUPLICATE_EIGENVALUE_TOLERANCE
                for prior in rows
            ):
                duplicates += 1
                continue
            if (
                candidate.eigen_residual < 2e-8
                and candidate.local_gap > c298.SIMPLE_EIGENVALUE_GAP
                and candidate.pole_margin
                > c298.POLE_MARGIN_FRACTION
                * c298.first_nonzero_laplacian(length)
            ):
                rows.append(candidate)
    return rows, {
        "raw_eigenpairs": raw,
        "forward_below_pole_with_window_duplicates": forward_below_pole,
        "deduplicated_lawful_simple_spectral_candidates": len(rows),
        "duplicate_window_hits": duplicates,
        "held_adaptive_projection_used_for_pool": False,
    }


def pool_controls() -> dict[int, list[BranchCandidate]]:
    print("\nFIXED AXIS-SHELL CANDIDATE POOLS")
    pools = {}
    details = {}
    for length in SIZES:
        rows, counts = candidate_pool(length)
        pools[length] = rows
        details[length] = counts
    check(
        "the declared axis-shell windows return deduplicated simple candidates on every training and held size",
        all(pools[length] for length in SIZES)
        and all(details[length]["raw_eigenpairs"] == 72 for length in SIZES)
        and all(
            details[length]["held_adaptive_projection_used_for_pool"] is False
            for length in SIZES
        ),
        details,
    )
    return pools


def training_pair_score(
    left: BranchCandidate,
    right: BranchCandidate,
    left_analysis: ProjectionAnalysis,
    right_analysis: ProjectionAnalysis,
) -> tuple[float, float, float, float]:
    left_fingerprint, left_weight = contact_fingerprint(left)
    right_fingerprint, right_weight = contact_fingerprint(right)
    fingerprint_overlap = float(abs(np.vdot(left_fingerprint, right_fingerprint)))
    fraction_distance = abs(phase_fraction(left) - phase_fraction(right))
    score = float(
        fingerprint_overlap
        * np.exp(-fraction_distance / BRANCH_PAIR_PHASE_WIDTH)
        * np.sqrt(left_analysis.green_overlap * right_analysis.green_overlap)
    )
    return score, fingerprint_overlap, left_weight, right_weight


def adaptive_analysis(candidate: BranchCandidate) -> ProjectionAnalysis | None:
    projected = c298.adaptive_scalar_projection(
        candidate.state, candidate.length, comparator(candidate)
    )
    if projected is None:
        return None
    (
        _fixed_metrics,
        coefficients,
        profile,
        weight,
        contact,
        overlap,
        residual,
    ) = projected
    return ProjectionAnalysis(
        coefficients=coefficients,
        profile=profile,
        weight=weight,
        contact_fraction=contact,
        green_overlap=overlap,
        green_residual=residual,
    )


def freeze_training_rule(pools: dict[int, list[BranchCandidate]]) -> FrozenRule:
    print("\nTRAINING-ONLY BRANCH / OBSERVABLE FREEZE")
    scored = []
    training_analyses = {
        id(candidate): adaptive_analysis(candidate)
        for length in TRAINING_SIZES
        for candidate in pools[length]
    }
    for left in pools[3]:
        left_fingerprint, left_weight = contact_fingerprint(left)
        left_analysis = training_analyses[id(left)]
        if (
            left_analysis is None
            or left_weight < FINGERPRINT_WEIGHT_MINIMUM
            or left_analysis.contact_fraction > FIXED_CONTACT_MAXIMUM
            or left_analysis.green_overlap < FIXED_GREEN_OVERLAP_MINIMUM
        ):
            continue
        for right in pools[4]:
            right_fingerprint, right_weight = contact_fingerprint(right)
            right_analysis = training_analyses[id(right)]
            if (
                right_analysis is None
                or right_weight < FINGERPRINT_WEIGHT_MINIMUM
                or right_analysis.contact_fraction > FIXED_CONTACT_MAXIMUM
                or right_analysis.green_overlap < FIXED_GREEN_OVERLAP_MINIMUM
            ):
                continue
            score, overlap, _left_weight, _right_weight = training_pair_score(
                left, right, left_analysis, right_analysis
            )
            scored.append(
                (score, overlap, left, right, left_analysis, right_analysis)
            )
    scored.sort(key=lambda row: row[0], reverse=True)
    if len(scored) < 2:
        raise RuntimeError("training branch tournament has fewer than two candidates")
    (
        score,
        fingerprint_overlap,
        left,
        right,
        left_analysis,
        right_analysis,
    ) = scored[0]

    left_fingerprint, left_weight = contact_fingerprint(left)
    right_fingerprint, right_weight = contact_fingerprint(right)
    right_fingerprint = align_to(left_fingerprint, right_fingerprint)
    template = left_fingerprint + right_fingerprint
    template /= np.linalg.norm(template)

    left_coefficients = left_analysis.coefficients.copy()
    right_coefficients = align_to(
        left_coefficients, right_analysis.coefficients.copy()
    )
    coefficients = left_coefficients + right_coefficients
    coefficients /= np.linalg.norm(coefficients)

    left_fraction = phase_fraction(left)
    right_fraction = phase_fraction(right)
    inverse_length_slope = (left_fraction - right_fraction) / (1 / 3 - 1 / 4)
    intercept = left_fraction - inverse_length_slope / 3
    rule = FrozenRule(
        training_rows=(left, right),
        fingerprint_template=template,
        projection_coefficients=coefficients,
        phase_intercept=float(intercept),
        phase_inverse_length_slope=float(inverse_length_slope),
        training_pair_score=score,
        training_pair_score_gap=score - scored[1][0],
    )
    check(
        "L=3,4 alone freeze one separated branch pair, contact template, phase trend, and scalar coefficient vector",
        fingerprint_overlap > 0.85
        and rule.training_pair_score_gap > 0.02
        and abs(np.linalg.norm(coefficients) - 1) < 1e-12,
        {
            "training_pair_score": score,
            "runner_up_score": scored[1][0],
            "score_gap": rule.training_pair_score_gap,
            "fingerprint_overlap": fingerprint_overlap,
            "phase_fractions": (left_fraction, right_fraction),
            "dimensionless_eigenphases": (
                float(-np.angle(left.eigenvalue)),
                float(-np.angle(right.eigenvalue)),
            ),
            "fingerprint_weights": (left_weight, right_weight),
            "fixed_coefficients_same_opposite_perpendicular": tuple(
                complex(value) for value in coefficients
            ),
            "phase_fraction_fit": {
                "intercept": rule.phase_intercept,
                "inverse_length_slope": rule.phase_inverse_length_slope,
            },
        },
    )
    return rule


def comparator(candidate: BranchCandidate) -> np.ndarray:
    target = c298.base.fixed.shifted_green_profile(
        candidate.length, candidate.shift
    ).astype(complex)
    return target - np.mean(target)


def fixed_observable_metrics(
    candidate: BranchCandidate, coefficients: np.ndarray
) -> tuple[np.ndarray, float, float, float, float]:
    profile = c298.scalar_orbit_profiles(candidate.state, candidate.length) @ coefficients
    target = comparator(candidate)
    weight = float(np.vdot(profile, profile).real)
    contact = float(abs(profile[0]) ** 2 / weight)
    overlap = float(
        abs(np.vdot(profile, target))
        / (np.linalg.norm(profile) * np.linalg.norm(target))
    )
    residual = float(np.sqrt(max(0.0, 2 - 2 * overlap)))
    return profile, weight, contact, overlap, residual


def select_with_frozen_rule(
    length: int, pool: list[BranchCandidate], rule: FrozenRule
) -> SelectedRow:
    predicted = (
        rule.phase_intercept + rule.phase_inverse_length_slope / length
    )
    scored = []
    for candidate in pool:
        fingerprint, _weight = contact_fingerprint(candidate)
        fingerprint_overlap = float(
            abs(np.vdot(rule.fingerprint_template, fingerprint))
        )
        fraction = phase_fraction(candidate)
        distance = abs(fraction - predicted)
        combined = float(
            fingerprint_overlap * np.exp(-distance / HELD_TRACK_PHASE_WIDTH)
        )
        scored.append((combined, fingerprint_overlap, distance, fraction, candidate))
    scored.sort(key=lambda row: row[0], reverse=True)
    combined, fingerprint_overlap, distance, fraction, candidate = scored[0]
    fingerprint_choice = max(scored, key=lambda row: row[1])[4]
    phase_choice = min(scored, key=lambda row: row[2])[4]
    profile, weight, contact, overlap, residual = fixed_observable_metrics(
        candidate, rule.projection_coefficients
    )
    adaptive = adaptive_analysis(candidate)
    if adaptive is None:
        raise RuntimeError("selected spectral candidate has no evaluable scalar span")
    return SelectedRow(
        candidate=candidate,
        predicted_phase_fraction=float(predicted),
        phase_fraction=fraction,
        phase_distance=distance,
        fingerprint_overlap=fingerprint_overlap,
        combined_score=combined,
        combined_score_gap=combined - scored[1][0],
        alternative_trackers_agree=(
            abs(fingerprint_choice.eigenvalue - candidate.eigenvalue)
            < DUPLICATE_EIGENVALUE_TOLERANCE
            and abs(phase_choice.eigenvalue - candidate.eigenvalue)
            < DUPLICATE_EIGENVALUE_TOLERANCE
        ),
        fixed_profile=profile,
        fixed_projection_weight=weight,
        fixed_contact_fraction=contact,
        fixed_green_overlap=overlap,
        fixed_green_residual=residual,
        adaptive_projection_weight=adaptive.weight,
        adaptive_contact_fraction=adaptive.contact_fraction,
        adaptive_green_overlap=adaptive.green_overlap,
        adaptive_green_residual=adaptive.green_residual,
    )


def branch_and_prediction_controls(
    pools: dict[int, list[BranchCandidate]], rule: FrozenRule
) -> dict[int, SelectedRow]:
    print("\nFROZEN BRANCH TRACKING / HELD PREDICTION")
    selected = {
        length: select_with_frozen_rule(length, pools[length], rule)
        for length in SIZES
    }
    details = {}
    for length, row in selected.items():
        candidate = row.candidate
        details[length] = {
            "domain": "training" if length in TRAINING_SIZES else "declared held-size",
            "K_index": MOMENTUM_INDEX,
            "target_window_fraction": candidate.target_fraction,
            "dimensionless_eigenphase": float(-np.angle(candidate.eigenvalue)),
            "phase_fraction_of_first_pole": row.phase_fraction,
            "training_predicted_phase_fraction": row.predicted_phase_fraction,
            "phase_fraction_residual": row.phase_distance,
            "contact_fingerprint_overlap": row.fingerprint_overlap,
            "combined_tracker_score": row.combined_score,
            "combined_tracker_score_gap": row.combined_score_gap,
            "phase_fingerprint_combined_trackers_agree": row.alternative_trackers_agree,
            "returned_window_local_eigenvalue_gap": candidate.local_gap,
            "fixed_projection_weight": row.fixed_projection_weight,
            "fixed_contact_fraction": row.fixed_contact_fraction,
            "fixed_green_overlap": row.fixed_green_overlap,
            "fixed_green_residual": row.fixed_green_residual,
            "same_eigenstate_adaptive_overlap": row.adaptive_green_overlap,
            "same_eigenstate_adaptive_residual": row.adaptive_green_residual,
            "same_eigenstate_adaptive_contact": row.adaptive_contact_fraction,
        }
    check(
        "phase-only, fingerprint-only, and combined frozen trackers agree on a separated held branch candidate",
        all(
            selected[length].alternative_trackers_agree
            and selected[length].combined_score_gap > 0.1
            and selected[length].fingerprint_overlap > 0.85
            and selected[length].candidate.local_gap > 1e-4
            for length in HELD_SIZES
        ),
        {length: details[length] for length in HELD_SIZES},
    )

    training_pass = all(
        selected[length].fixed_green_overlap >= FIXED_GREEN_OVERLAP_MINIMUM
        and selected[length].fixed_contact_fraction <= FIXED_CONTACT_MAXIMUM
        and selected[length].fixed_projection_weight
        >= FIXED_PROJECTION_WEIGHT_MINIMUM
        for length in TRAINING_SIZES
    )
    held_passes = {
        length: (
            selected[length].fixed_green_overlap >= FIXED_GREEN_OVERLAP_MINIMUM
            and selected[length].fixed_contact_fraction <= FIXED_CONTACT_MAXIMUM
            and selected[length].fixed_projection_weight
            >= FIXED_PROJECTION_WEIGHT_MINIMUM
        )
        for length in HELD_SIZES
    }
    check(
        "the training-fitted scalar observable passes training and is honestly rejected by both declared held-size overlap gates",
        training_pass and held_passes == {5: False, 6: False},
        {"held_passes": held_passes, "rows": details},
    )
    check(
        "the fixed-versus-adaptive residual comparison is evaluated on the same tracked eigenstate with no held coefficient refit",
        all(
            selected[length].adaptive_green_residual
            <= selected[length].fixed_green_residual + TOLERANCE
            for length in SIZES
        ),
        {
            length: {
                "fixed_overlap": selected[length].fixed_green_overlap,
                "fixed_residual": selected[length].fixed_green_residual,
                "adaptive_overlap": selected[length].adaptive_green_overlap,
                "adaptive_residual": selected[length].adaptive_green_residual,
            }
            for length in SIZES
        },
    )
    return selected


def covariance_controls(
    selected: dict[int, SelectedRow], rule: FrozenRule
) -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE")
    frames = c298.base.c210.proper_cubic_frames()
    operator_residuals = []
    held_state_residuals = []
    held_profile_residuals = []
    held_fingerprint_residuals = []
    held_tracker_overlap_residuals = []

    training = selected[3].candidate
    training_update = c298.carried_update(3, MOMENTUM_INDEX)
    for frame in frames:
        representation = c298.base.frame_permutation(3, frame)
        rotated_index = tuple(int(value) for value in frame @ np.asarray(MOMENTUM_INDEX))
        rotated_update = c298.carried_update(3, rotated_index)
        operator_residuals.append(
            float(
                sparse.linalg.norm(
                    rotated_update @ representation
                    - representation @ training_update
                )
            )
        )

    for length in HELD_SIZES:
        row = selected[length]
        candidate = row.candidate
        fingerprint, _weight = contact_fingerprint(candidate)
        for frame in frames:
            representation = c298.base.frame_permutation(length, frame)
            rotated_index = tuple(
                int(value) for value in frame @ np.asarray(MOMENTUM_INDEX)
            )
            rotated_state = representation @ candidate.state
            rotated_update = c298.carried_update(length, rotated_index)
            held_state_residuals.append(
                float(
                    np.linalg.norm(
                        rotated_update @ rotated_state
                        - candidate.eigenvalue * rotated_state
                    )
                )
            )
            rotated_profile = (
                c298.scalar_orbit_profiles(rotated_state, length)
                @ rule.projection_coefficients
            )
            expected_profile = c298.spatial_frame_profile(
                row.fixed_profile, length, frame
            )
            held_profile_residuals.append(
                float(np.linalg.norm(rotated_profile - expected_profile))
            )
            contact_representation = representation[:42, :42]
            rotated_fingerprint = rotated_state[:42]
            rotated_fingerprint /= np.linalg.norm(rotated_fingerprint)
            expected_fingerprint = contact_representation @ fingerprint
            held_fingerprint_residuals.append(
                float(np.linalg.norm(rotated_fingerprint - expected_fingerprint))
            )
            rotated_template = (
                contact_representation @ rule.fingerprint_template
            )
            rotated_overlap = float(
                abs(np.vdot(rotated_template, rotated_fingerprint))
            )
            held_tracker_overlap_residuals.append(
                abs(rotated_overlap - row.fingerprint_overlap)
            )
    check(
        "the fixed axis-shell rule, selected held eigenstates, contact fingerprint, and frozen scalar observable are covariant under all 24 proper-cubic frames",
        len(frames) == 24
        and max(operator_residuals) < 4e-12
        and max(held_state_residuals) < 4e-10
        and max(held_profile_residuals) < 4e-9
        and max(held_fingerprint_residuals) < 4e-9
        and max(held_tracker_overlap_residuals) < 4e-12,
        {
            "proper_frames": len(frames),
            "L3_max_operator_frobenius_residual": max(operator_residuals),
            "held_frame_state_tests": len(held_state_residuals),
            "held_max_eigenstate_residual": max(held_state_residuals),
            "held_max_fixed_profile_residual": max(held_profile_residuals),
            "held_max_fingerprint_residual": max(held_fingerprint_residuals),
            "held_max_tracker_overlap_residual": max(
                held_tracker_overlap_residuals
            ),
        },
    )


def domain_deletion_controls(selected: dict[int, SelectedRow]) -> None:
    print("\nLAWFUL DOMAIN / NONZERO-K LIFT / COUPLING ENDPOINT")
    length = 3
    update = c298.carried_update(length, MOMENTUM_INDEX)
    full_update = c298.base.full_periodic_update(length)
    lift = c298.momentum_lift_isometry(length, MOMENTUM_INDEX)
    identity = sparse.eye(update.shape[0], dtype=complex, format="csr")
    unitarity = float(sparse.linalg.norm(update.conj().T @ update - identity))
    isometry = float(sparse.linalg.norm(lift.conj().T @ lift - identity))
    intertwiner = float(sparse.linalg.norm(full_update @ lift - lift @ update))
    k_zero_regression = float(
        sparse.linalg.norm(
            c298.carried_update(length, c298.K_ZERO)
            - c298.base.carried_relative_update(length)
        )
    )
    invalid_length = invalid_momentum = False
    try:
        c298.momentum_lift_isometry(2, MOMENTUM_INDEX)
    except ValueError:
        invalid_length = True
    try:
        c298.momentum(4, (1.0, 0.5, 0.0))  # type: ignore[arg-type]
    except ValueError:
        invalid_momentum = True
    endpoint_residuals = {
        length: float(
            np.linalg.norm(
                c298.carried_update(
                    length, MOMENTUM_INDEX, angle=0.0
                )
                @ row.candidate.state
                - row.candidate.eigenvalue * row.candidate.state
            )
        )
        for length, row in selected.items()
    }
    check(
        "the relative-sector basis-spanning nonzero-K lift is lawful and exactly matches the predecessor at K=0",
        unitarity < 4e-13
        and isometry < 4e-13
        and intertwiner < 4e-12
        and k_zero_regression < 4e-13
        and invalid_length
        and invalid_momentum,
        {
            "relative_dimension": update.shape[0],
            "full_Q1_dimension": full_update.shape[0],
            "unitarity_residual": unitarity,
            "isometry_residual": isometry,
            "intertwiner_residual": intertwiner,
            "K0_predecessor_residual": k_zero_regression,
            "L2_rejected": invalid_length,
            "fractional_momentum_rejected": invalid_momentum,
            "domain": "one-matter Q=N_e+N_f=1 sector",
        },
    )
    check(
        "the tracked finite-coupling eigenpairs are not retained unchanged at the theta=0 deletion endpoint",
        all(value > 1e-3 for value in endpoint_residuals.values()),
        {
            "theta_zero_old_eigenpair_residuals": endpoint_residuals,
            "scope": "coupling dependence of these eigenpairs, not deletion of the update or a mass/energy claim",
        },
    )


def inventory_controls(rule: FrozenRule) -> None:
    print("\nSUPPLIED STRUCTURE INVENTORY")
    inventory = {
        "predecessor": "Cycle-298 carried relative update and candidate-window machinery",
        "training_sizes": TRAINING_SIZES,
        "declared_held_sizes": HELD_SIZES,
        "fixed_momentum_index": MOMENTUM_INDEX,
        "target_windows": c298.K_AXIS_TARGET_FRACTIONS,
        "eigenpairs_per_window": c298.EIGENPAIRS_PER_WINDOW,
        "held_candidate_pool": "phase, pole, eigen-residual, local-gap, and eigenvalue-deduplication only; no adaptive projection",
        "training_pair_score": "contact-fingerprint overlap times exp(-phase-fraction distance/0.12) times geometric-mean adaptive training overlap",
        "contact_fingerprint": "normalized first 42 relative-block amplitudes (six excited plus 36 contact-pair amplitudes)",
        "held_primary_tracker": "fingerprint overlap times exp(-phase-fraction residual/0.05)",
        "alternate_trackers": ("fingerprint only", "phase trend only"),
        "phase_trend": "two-training-point affine fit in 1/L of eigenphase/first-pole-phase",
        "fixed_scalar_orbits": c298.ORBIT_NAMES,
        "fixed_scalar_coefficients": tuple(
            complex(value) for value in rule.projection_coefficients
        ),
        "fixed_green_overlap_minimum": FIXED_GREEN_OVERLAP_MINIMUM,
        "fixed_contact_maximum": FIXED_CONTACT_MAXIMUM,
        "fixed_projection_weight_minimum": FIXED_PROJECTION_WEIGHT_MINIMUM,
        "branch_pair_phase_width": BRANCH_PAIR_PHASE_WIDTH,
        "held_track_phase_width": HELD_TRACK_PHASE_WIDTH,
        "fingerprint_weight_minimum": FINGERPRINT_WEIGHT_MINIMUM,
        "comparator": "per-eigenpair residual-matched shifted-Green shape; evaluation only on held sizes",
        "held_adaptation": False,
        "authority": "none",
        "audit": "unset",
    }
    check(
        "the runner prints every supplied branch, observable, window, threshold, and held-adaptation choice",
        inventory["held_adaptation"] is False
        and len(rule.projection_coefficients) == 3
        and len(c298.K_AXIS_TARGET_FRACTIONS) == 9,
        inventory,
    )


def main() -> int:
    print("CYCLE 300: TRAINING-FROZEN CARRIED BRANCH / OBSERVABLE")
    print("authority=none; audit=unset")
    note_contract()
    pools = pool_controls()
    rule = freeze_training_rule(pools)
    selected = branch_and_prediction_controls(pools, rule)
    covariance_controls(selected, rule)
    domain_deletion_controls(selected)
    inventory_controls(rule)
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
