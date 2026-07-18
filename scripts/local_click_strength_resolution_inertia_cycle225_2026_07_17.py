#!/usr/bin/env python3
"""Cycle 225: fixed scalar-Kraus projector and resolution controls.

For a supplied position projector P, test the standard weak instrument
M0=Q+cos(g)P, M1=sin(g)P.  The normalized click state is independent of g:
weakening the coupling changes the branch weight, not the state conditional on
that sharp click.  Distinguish copying one pointer from interrogating matter
twice, then measure the resolution/inertia trade in the Cycle-222 packets.

The instrument, projector, coupling, squared-norm weights, candidate working
state, and conditioning are supplied.  No Record, occurrence, clock, gravity
law, or axiom conclusion is derived.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import conditional_flavor_mass_operator_compiler_cycle222_2026_07_17 as c222
import locking_cadence_record_kernel_discriminator_cycle223_2026_07_17 as c223
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import stationary_local_first_event_history_cycle224_2026_07_17 as c224


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCAL_CLICK_STRENGTH_RESOLUTION_INERTIA_CYCLE225_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "fixed scalar-kraus projector identity",
        "instrument-exact, not effect-generic",
        "copying a pointer is not a second interrogation",
        "spatial resolution and inertia preservation trade",
        "supplied compiled eigenlabel",
        "host-supplied many-site projectors",
        "squared-modulus weights are supplied",
        "occurrence remains supplied",
        "does not derive a record",
        "does not derive a clock",
        "global novelty has not been established",
        "n1",
        "n8",
        "audit unset",
        "no axiom conclusion",
        "draft pr #5389",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    forbidden = tuple(
        phrase
        for phrase in (
            "fewer click branches",
            "a record cannot be treated as a cost-free shadow",
            "mass is a persistent law-sector property",
        )
        if phrase in text
    )
    check(
        "note preserves the bounded fixed-instrument claim",
        not missing and not forbidden,
        {"missing": missing, "forbidden": forbidden},
    )


def projector_instrument(
    projector: np.ndarray, coupling: float
) -> tuple[np.ndarray, np.ndarray]:
    identity = np.eye(projector.shape[0], dtype=complex)
    complement = identity - projector
    return (
        complement + np.cos(coupling) * projector,
        np.sin(coupling) * projector,
    )


def exact_strength_controls() -> None:
    dimension = 18
    projector = np.diag(
        np.concatenate((np.ones(6), np.zeros(dimension - 6))).astype(complex)
    )
    rng = np.random.default_rng(22501)
    state = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    state /= np.linalg.norm(state)
    sharp = projector @ state
    sharp /= np.linalg.norm(sharp)
    support_weight = float(np.vdot(state, projector @ state).real)
    couplings = (-np.pi / 7, np.pi / 13, np.pi / 7, np.pi / 3, np.pi / 2)
    rows = []
    for coupling in couplings:
        no_click, click = projector_instrument(projector, coupling)
        click_branch = click @ state
        click_weight = float(np.vdot(click_branch, click_branch).real)
        conditioned = click_branch / np.sqrt(click_weight)
        rows.append(
            (
                coupling,
                np.linalg.norm(
                    no_click.conj().T @ no_click
                    + click.conj().T @ click
                    - np.eye(dimension)
                ),
                1 - abs(np.vdot(sharp, conditioned)) ** 2,
                abs(
                    click_weight
                    - np.sin(coupling) ** 2 * support_weight
                ),
                click_weight,
            )
        )

    no_click, click = projector_instrument(projector, 0.0)
    check(
        "the fixed scalar-Kraus projector identity holds for non-Clifford complex tests",
        max(row[1] for row in rows) < 3e-12
        and max(abs(row[2]) for row in rows) < 3e-12
        and max(row[3] for row in rows) < 3e-12,
        rows,
    )
    check(
        "zero coupling deletes the instrument back-action and click branch",
        np.linalg.norm(no_click - np.eye(dimension)) < 3e-12
        and np.linalg.norm(click) < 3e-12,
        {
            "no_click_identity": np.linalg.norm(no_click - np.eye(dimension)),
            "click_norm": np.linalg.norm(click),
        },
    )


def pointer_copy_and_reinterrogation_controls() -> None:
    dimension = 12
    projector = np.diag(
        np.concatenate((np.ones(4), np.zeros(dimension - 4))).astype(complex)
    )
    complement = np.eye(dimension) - projector
    rng = np.random.default_rng(22502)
    state = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    state /= np.linalg.norm(state)
    density = np.outer(state, state.conj())
    coupling = np.pi / 7
    cosine = np.cos(coupling)
    sine = np.sin(coupling)
    zero = np.array((1, 0), dtype=complex)
    one = np.array((0, 1), dtype=complex)
    rotated = cosine * zero + sine * one
    q_state = complement @ state
    p_state = projector @ state

    one_pointer = np.kron(q_state, zero) + np.kron(p_state, rotated)
    copied_pointer = np.kron(q_state, np.kron(zero, zero)) + np.kron(
        p_state,
        cosine * np.kron(zero, zero) + sine * np.kron(one, one),
    )
    two_interrogations = np.kron(q_state, np.kron(zero, zero)) + np.kron(
        p_state, np.kron(rotated, rotated)
    )

    one_reduced = c224.trace_pointer(
        np.outer(one_pointer, one_pointer.conj()), dimension
    )
    copied_reduced = c224.trace_pointer(
        np.outer(copied_pointer, copied_pointer.conj()), dimension
    )
    twice_reduced = c224.trace_pointer(
        np.outer(two_interrogations, two_interrogations.conj()), dimension
    )
    diagonal = (
        complement @ density @ complement + projector @ density @ projector
    )
    cross = complement @ density @ projector + projector @ density @ complement
    once_expected = diagonal + cosine * cross
    twice_expected = diagonal + cosine**2 * cross

    check(
        "copying one pointer preserves its reduced matter channel",
        np.linalg.norm(one_reduced - once_expected) < 3e-12
        and np.linalg.norm(copied_reduced - once_expected) < 3e-12
        and np.linalg.norm(one_reduced - copied_reduced) < 3e-12,
        {
            "one": np.linalg.norm(one_reduced - once_expected),
            "copied": np.linalg.norm(copied_reduced - once_expected),
        },
    )
    check(
        "two matter interrogations are not a redundant copy of one pointer",
        np.linalg.norm(twice_reduced - twice_expected) < 3e-12
        and np.linalg.norm(twice_reduced - copied_reduced) > 0.01,
        {
            "twice_formula": np.linalg.norm(twice_reduced - twice_expected),
            "copy_vs_twice": np.linalg.norm(twice_reduced - copied_reduced),
        },
    )


def weak_first_event_history(
    unitary: np.ndarray,
    detector_mask: np.ndarray,
    initial: np.ndarray,
    steps: int,
    coupling: float,
) -> tuple[tuple[np.ndarray, ...], np.ndarray]:
    no_click = 1 - (1 - np.cos(coupling)) * detector_mask
    click = np.sin(coupling) * detector_mask
    open_state = np.asarray(initial, dtype=complex).copy()
    clicks = []
    for _ in range(steps):
        evolved = unitary @ open_state
        clicks.append(click * evolved)
        open_state = no_click * evolved
    return tuple(clicks), open_state


def weak_causal_arrival_controls(
    blocks: tuple[c223.BlindBlock, ...]
) -> None:
    length = 31
    centre = length // 2
    distance = 6
    steps = 12
    detector = c224.site_mask(length, centre + distance)
    initial = np.zeros(6 * length, dtype=complex)
    initial[6 * centre] = 1
    couplings = (np.pi / 13, np.pi / 7, np.pi / 3, np.pi / 2)
    rows = []
    deletion_rows = []
    for block_row in blocks:
        unitary = c224.axis_walk(block_row.block, length)
        first_conditioned = []
        for coupling in couplings:
            clicks, survival = weak_first_event_history(
                unitary, detector, initial, steps, coupling
            )
            weights = np.asarray(
                [float(np.vdot(row, row).real) for row in clicks]
            )
            normalization = abs(
                float(np.sum(weights) + np.vdot(survival, survival).real) - 1
            )
            first = clicks[distance - 1] / np.sqrt(weights[distance - 1])
            first_conditioned.append(first)
            rows.append(
                (
                    block_row.c3_phase,
                    coupling,
                    float(np.max(np.abs(weights[: distance - 1]))),
                    float(weights[distance - 1]),
                    normalization,
                    float(np.sum(weights)),
                )
            )
        reference = first_conditioned[0]
        rows.append(
            (
                block_row.c3_phase,
                "conditioned_first_arrival_fidelity",
                min(abs(np.vdot(reference, row)) ** 2 for row in first_conditioned),
            )
        )
        deleted_clicks, deleted_survival = weak_first_event_history(
            unitary, detector, initial, steps, 0.0
        )
        deletion_rows.append(
            (
                block_row.c3_phase,
                max(np.linalg.norm(row) for row in deleted_clicks),
                np.linalg.norm(
                    deleted_survival
                    - np.linalg.matrix_power(unitary, steps) @ initial
                ),
            )
        )

    numeric_rows = [row for row in rows if len(row) == 6]
    fidelity_rows = [row for row in rows if len(row) == 3]
    sector_spreads = []
    for phase in sorted({row[0] for row in numeric_rows}):
        totals = [row[5] for row in numeric_rows if row[0] == phase]
        sector_spreads.append((phase, max(totals) - min(totals)))
    check(
        "weak coupling changes weight but not the normalized first-causal-support branch",
        max(row[2] for row in numeric_rows) < 3e-14
        and min(row[3] for row in numeric_rows) > 1e-7
        and max(row[4] for row in numeric_rows) < 3e-12
        and min(row[2] for row in fidelity_rows) > 1 - 3e-12
        and min(row[1] for row in sector_spreads) > 0.01,
        {"rows": rows, "within_sector_total_weight_spreads": sector_spreads},
    )
    check(
        "deleting the coupling restores uninterrupted candidate evolution",
        max(row[1] for row in deletion_rows) < 3e-14
        and max(row[2] for row in deletion_rows) < 3e-12,
        deletion_rows,
    )


@dataclass(frozen=True)
class PatchRow:
    scale_label: str
    c3_phase: float
    half_width: int
    click_weight: float
    fidelity: float
    band_weight: float
    dispersion_mass: float
    conditioned_force_response_estimator: float
    relative_mismatch: float
    normalized_even_contamination: float
    odd_acceleration: float
    force_sign_ok: bool
    health: bool


def patch_trade_rows(
    scale_label: str,
    compiled: c222.Compiled,
    half_widths: tuple[int, ...],
) -> tuple[PatchRow, ...]:
    length = 4096
    width = 0.006
    strength = 1e-6
    rows = []
    for block_row in c223.c3_blind_blocks(compiled.coin):
        positions, momenta, packet = c222.prepare_block_packet(
            block_row.block, length, width
        )
        evolved = c210.local_molecular_step(packet, block_row.block, axis=0)
        curvature = c222.block_curvature_tensor(block_row.block, step=0.003)
        dispersion = 1 / float(np.mean(np.diag(curvature)))
        for half_width in half_widths:
            mask = (np.abs(positions) <= half_width)[:, None]
            branch = mask * evolved
            click_weight = float(np.sum(np.abs(branch) ** 2))
            branch /= np.sqrt(click_weight)
            fidelity = float(abs(np.vdot(evolved, branch)) ** 2)
            band = c222.block_branch_probability(
                branch, momenta, block_row.block
            )
            positive = c224.forced_packet_response_from_seed(
                block_row.block,
                branch,
                positions,
                momenta,
                strength,
            )
            negative = c224.forced_packet_response_from_seed(
                block_row.block,
                branch,
                positions,
                momenta,
                -strength,
            )
            zero = c224.forced_packet_response_from_seed(
                block_row.block,
                branch,
                positions,
                momenta,
                0.0,
            )
            odd_acceleration = (positive[0] - negative[0]) / 2
            normalized_even_contamination = abs(
                positive[0] + negative[0] - 2 * zero[0]
            ) / max(abs(positive[0] - negative[0]), 1e-30)
            inertia = -strength / odd_acceleration
            health = (
                max(
                    abs(positive[2] - 1),
                    abs(negative[2] - 1),
                    abs(zero[2] - 1),
                )
                < 3e-10
                and max(positive[3], negative[3], zero[3]) < 2e-12
                and normalized_even_contamination < 1e-8
                and abs(odd_acceleration) > 1e-12
                and positive[0] * negative[0] < 0
                and np.isfinite(inertia)
                and inertia > 0
            )
            rows.append(
                PatchRow(
                    scale_label,
                    block_row.c3_phase,
                    half_width,
                    click_weight,
                    fidelity,
                    band,
                    dispersion,
                    inertia,
                    abs(inertia / dispersion - 1),
                    normalized_even_contamination,
                    odd_acceleration,
                    positive[0] * negative[0] < 0,
                    health,
                )
            )
    return tuple(rows)


def resolution_inertia_controls(
    reference: c222.Compiled,
    held_out: c222.Compiled,
) -> None:
    half_widths = (0, 16, 64, 128, 256, 512)
    rows = patch_trade_rows("reference", reference, half_widths) + patch_trade_rows(
        "held-out", held_out, half_widths
    )
    site = [row for row in rows if row.half_width == 0]
    earlier_widths = {
        width: [row for row in rows if row.half_width == width]
        for width in half_widths
        if width < 256
    }
    width_128 = [row for row in rows if row.half_width == 128]
    width_256 = [row for row in rows if row.half_width == 256]
    width_512 = [row for row in rows if row.half_width == 512]

    check(
        "conditioned site-projector branches fail the calibrated low-band inertia contract at both scales",
        min(row.relative_mismatch for row in site) > 0.05
        and max(row.band_weight for row in site) < 0.8
        and all(row.health for row in site),
        site,
    )
    check(
        "the sampled spatial resolution and inertia preservation trade is target-unfed",
        all(
            max(row.relative_mismatch for row in width_rows) > 0.01
            for width_rows in earlier_widths.values()
        )
        and max(row.relative_mismatch for row in width_256) < 0.01
        and min(row.click_weight for row in width_256) > 0.97
        and min(row.band_weight for row in width_256) > 0.999
        and max(row.relative_mismatch for row in width_512) < 0.001
        and min(row.click_weight for row in width_512) > 0.99998
        and max(abs(row.fidelity - row.click_weight) for row in rows) < 3e-12
        and all(row.health for row in rows),
        {
            "earlier_widths": earlier_widths,
            "width_256": width_256,
            "width_512": width_512,
        },
    )


def mass_and_axis_controls(
    reference: c222.Compiled,
    held_out: c222.Compiled,
) -> None:
    coin_commutators = []
    position_commutators = []
    axis_rows = []
    for scale_label, compiled in (
        ("reference", reference),
        ("held-out", held_out),
    ):
        mass_direction = np.kron(compiled.recovered_mass, np.eye(6))
        commutator = (
            mass_direction @ compiled.coin - compiled.coin @ mass_direction
        )
        coin_commutators.append(
            (
                scale_label,
                np.linalg.norm(commutator)
                / (
                    np.linalg.norm(mass_direction)
                    * np.linalg.norm(compiled.coin)
                ),
            )
        )
        lattice_sites = 3
        position = np.diag((1.0, 0.0, 0.0)).astype(complex)
        position_full = np.kron(position, np.eye(24))
        mass_full = np.kron(np.eye(lattice_sites), mass_direction)
        position_commutators.append(
            (
                scale_label,
                np.linalg.norm(position_full @ mass_full - mass_full @ position_full),
            )
        )
        for block_row in c223.c3_blind_blocks(compiled.coin):
            values = []
            for axis in range(3):
                positions, momenta, packet = c222.prepare_block_packet(
                    block_row.block, 1024, 0.012, axis=axis
                )
                evolved = c210.local_molecular_step(
                    packet, block_row.block, axis=axis
                )
                branch = (np.abs(positions) <= 64)[:, None] * evolved
                weight = float(np.sum(np.abs(branch) ** 2))
                branch /= np.sqrt(weight)
                band = c222.block_branch_probability(
                    branch, momenta, block_row.block, axis=axis
                )
                values.append((weight, band))
            axis_rows.append(
                (
                    scale_label,
                    block_row.c3_phase,
                    max(value[0] for value in values)
                    - min(value[0] for value in values),
                    max(value[1] for value in values)
                    - min(value[1] for value in values),
                )
            )

    check(
        "the compiled coin commutes with the supplied internal operator",
        max(row[1] for row in coin_commutators) < 3e-12,
        coin_commutators,
    )
    check(
        "host-supplied position projectors commute with the internal operator by tensor factor",
        max(row[1] for row in position_commutators) < 3e-12,
        position_commutators,
    )
    check(
        "co-oriented retained-weight and scalar-band controls agree on all three cubic axes",
        max(row[2] for row in axis_rows) < 3e-12
        and max(row[3] for row in axis_rows) < 1e-8,
        axis_rows,
    )


def predecessor_controls() -> None:
    predecessors = (
        ROOT
        / "scripts/stationary_local_first_event_history_cycle224_2026_07_17.py",
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "STATIONARY_LOCAL_FIRST_EVENT_HISTORY_CYCLE224_NOTE_2026-07-17.md",
        ROOT
        / "scripts/locking_cadence_record_kernel_discriminator_cycle223_2026_07_17.py",
        ROOT
        / "scripts/conditional_flavor_mass_operator_compiler_cycle222_2026_07_17.py",
    )
    check(
        "the mass cadence and stationary-arrival predecessors remain present",
        all(path.is_file() for path in predecessors),
        [path.name for path in predecessors],
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    reference = c222.compile_operator(c222.REFERENCE_SCALE)
    held_out = c222.compile_operator(c222.HELD_OUT_SCALE)
    blocks = c223.c3_blind_blocks(reference.coin)
    check(
        "reference and frozen held-out candidate laws are unitary",
        np.linalg.norm(reference.coin.conj().T @ reference.coin - np.eye(24))
        < 3e-12
        and np.linalg.norm(held_out.coin.conj().T @ held_out.coin - np.eye(24))
        < 3e-12,
        (reference.scale, held_out.scale),
    )
    exact_strength_controls()
    pointer_copy_and_reinterrogation_controls()
    weak_causal_arrival_controls(blocks)
    resolution_inertia_controls(reference, held_out)
    mass_and_axis_controls(reference, held_out)
    predecessor_controls()
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
