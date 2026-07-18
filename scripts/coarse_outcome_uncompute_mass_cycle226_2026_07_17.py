#!/usr/bin/env python3
"""Cycle 226: coarse outcome copying, fine-workspace uncompute, and mass.

Compare two supplied detector microarchitectures with the same coarse yes/no
output and the same position statistics.  One copies only a coarse patch bit
and coherently uncomputes its site-resolving workspace.  The other exports or
dephases the site label before uncompute.  The first preserves coherence inside
the coarse outcome fibre; the second does not.

Apply that exact distinction to the supplied Cycle-222 packets.  This is a
conditional channel/apparatus discriminator.  It does not derive an apparatus,
an occurring Record, Born frequency, a clock, gravity, or axiom language.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import conditional_flavor_mass_operator_compiler_cycle222_2026_07_17 as c222
import locking_cadence_record_kernel_discriminator_cycle223_2026_07_17 as c223
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COARSE_OUTCOME_UNCOMPUTE_MASS_CYCLE226_NOTE_2026-07-17.md"
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
        "same coarse outcome and position statistics",
        "coherently uncomputes the fine workspace",
        "archive-before-uncompute",
        "within-outcome coherence",
        "which-site information",
        "supplied detector microarchitecture",
        "does not derive a record",
        "occurrence remains supplied",
        "born frequency remains supplied",
        "does not derive a clock",
        "does not derive gravity",
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
            "a record must form only after uncompute",
            "uncompute causes occurrence",
            "mass is the record",
            "the axioms require",
        )
        if phrase in text
    )
    check(
        "note preserves the bounded coarse-versus-fine channel claim",
        not missing and not forbidden,
        {"missing": missing, "forbidden": forbidden},
    )


def reduced_matter_density(state: np.ndarray) -> np.ndarray:
    """Trace every factor after the first two matter axes."""
    matter_dimension = state.shape[0] * state.shape[1]
    matrix = state.reshape(matter_dimension, -1)
    return matrix @ matrix.conj().T


def coarse_and_site_densities(
    state: np.ndarray, patch: np.ndarray
) -> tuple[float, np.ndarray, np.ndarray]:
    """Return normalized coarse-projector and site-dephased yes densities."""
    branch = patch[:, None] * state
    weight = float(np.vdot(branch, branch).real)
    vector = branch.reshape(-1) / np.sqrt(weight)
    coarse = np.outer(vector, vector.conj())
    site = np.zeros_like(coarse)
    internal = state.shape[1]
    for position in np.flatnonzero(patch):
        value = state[position]
        block = np.outer(value, value.conj()) / weight
        start = position * internal
        site[start : start + internal, start : start + internal] = block
    return weight, coarse, site


def position_probabilities(density: np.ndarray, sites: int, internal: int) -> np.ndarray:
    probabilities = np.zeros(sites)
    for position in range(sites):
        start = position * internal
        probabilities[position] = float(
            np.trace(density[start : start + internal, start : start + internal]).real
        )
    return probabilities


def toggle_fine_workspace(state: np.ndarray, patch: np.ndarray) -> np.ndarray:
    """Controlled swap of workspace zero with the matter site's fine label."""
    output = state.copy()
    for position in np.flatnonzero(patch):
        output[position, :, 0, ...] = state[position, :, position + 1, ...]
        output[position, :, position + 1, ...] = state[position, :, 0, ...]
    return output


def copy_coarse_bit(state: np.ndarray, patch: np.ndarray) -> np.ndarray:
    """Controlled NOT on the final axis for the declared coarse matter fibre."""
    output = state.copy()
    for position in np.flatnonzero(patch):
        output[position, :, :, 0] = state[position, :, :, 1]
        output[position, :, :, 1] = state[position, :, :, 0]
    return output


def finite_uncompute_controls() -> None:
    sites = 7
    internal = 3
    workspace = sites + 1
    rng = np.random.default_rng(22601)
    matter = rng.normal(size=(sites, internal)) + 1j * rng.normal(
        size=(sites, internal)
    )
    matter /= np.linalg.norm(matter)
    patch = np.array((False, True, True, True, True, False, False))
    weight, coarse, site = coarse_and_site_densities(matter, patch)

    # Reversibly write the fine site label, copy only the coarse yes/no value,
    # and then erase the fine workspace using the still-present matter position.
    initial = np.zeros((sites, internal, workspace, 2), dtype=complex)
    initial[:, :, 0, 0] = matter
    computed = toggle_fine_workspace(initial, patch)
    copied = copy_coarse_bit(computed, patch)
    uncomputed = toggle_fine_workspace(copied, patch)

    expected = np.zeros_like(uncomputed)
    expected[:, :, 0, 0] = (~patch)[:, None] * matter
    expected[:, :, 0, 1] = patch[:, None] * matter
    yes_vector = uncomputed[:, :, 0, 1].reshape(-1) / np.sqrt(weight)
    yes_density = np.outer(yes_vector, yes_vector.conj())
    generic = rng.normal(size=initial.shape) + 1j * rng.normal(size=initial.shape)

    check(
        "copying the coarse output and coherently uncomputing the fine workspace restores its outcome fibre",
        np.linalg.norm(uncomputed - expected) < 3e-12
        and np.linalg.norm(yes_density - coarse) < 3e-12
        and abs(np.linalg.norm(copied) - 1) < 3e-12
        and abs(np.linalg.norm(uncomputed) - 1) < 3e-12
        and np.linalg.norm(
            toggle_fine_workspace(toggle_fine_workspace(generic, patch), patch)
            - generic
        )
        < 3e-12
        and np.linalg.norm(
            copy_coarse_bit(copy_coarse_bit(generic, patch), patch) - generic
        )
        < 3e-12,
        {
            "state_error": np.linalg.norm(uncomputed - expected),
            "yes_density_error": np.linalg.norm(yes_density - coarse),
        },
    )

    coarse_positions = position_probabilities(coarse, sites, internal)
    site_positions = position_probabilities(site, sites, internal)
    within_fibre_block = coarse[
        internal : 2 * internal, 2 * internal : 3 * internal
    ]
    archived_block = site[
        internal : 2 * internal, 2 * internal : 3 * internal
    ]
    # Copy the fine workspace label into an environment, then uncompute only
    # the local workspace.  Conditioning on coarse output one and tracing the
    # retained environment gives the site-dephased density exactly.
    archived = np.zeros(
        (sites, internal, workspace, 2, workspace), dtype=complex
    )
    for fine_label in range(workspace):
        archived[:, :, fine_label, :, fine_label] = copied[
            :, :, fine_label, :
        ]
    archived_uncomputed = toggle_fine_workspace(archived, patch)
    archived_yes = archived_uncomputed[:, :, :, 1, :] / np.sqrt(weight)
    archived_yes_density = reduced_matter_density(archived_yes)
    nonblank_workspace_norm = np.linalg.norm(
        archived_uncomputed[:, :, 1:, :, :]
    )
    check(
        "archive-before-uncompute leaves site dephasing despite the same coarse output statistics",
        abs(np.trace(site) - 1) < 3e-12
        and np.linalg.norm(coarse_positions - site_positions) < 3e-12
        and np.linalg.norm(within_fibre_block) > 0.01
        and np.linalg.norm(archived_block) < 3e-12
        and abs(np.trace(coarse @ coarse).real - 1) < 3e-12
        and np.trace(site @ site).real < 0.5
        and np.linalg.norm(archived_yes_density - site) < 3e-12
        and nonblank_workspace_norm < 3e-12,
        {
            "weight": weight,
            "position_error": np.linalg.norm(coarse_positions - site_positions),
            "coarse_purity": np.trace(coarse @ coarse).real,
            "archived_purity": np.trace(site @ site).real,
            "coherence_removed": np.linalg.norm(within_fibre_block),
            "explicit_archive_error": np.linalg.norm(archived_yes_density - site),
            "nonblank_workspace_norm": nonblank_workspace_norm,
        },
    )

    # A passive permutation of fine labels changes no reduced matter state.
    permutation = np.array((0, 4, 2, 7, 1, 6, 3, 5))
    relabeled = copied[:, :, permutation, :]
    check(
        "passive relabeling of the fine workspace leaves the reduced channel invariant",
        np.linalg.norm(
            reduced_matter_density(copied) - reduced_matter_density(relabeled)
        )
        < 3e-12,
        np.linalg.norm(
            reduced_matter_density(copied) - reduced_matter_density(relabeled)
        ),
    )

    # One or two copies of the already-coarse pointer induce the same reduced
    # matter channel; retaining the fine workspace induces a different channel.
    complement = (~patch)[:, None] * matter
    projected = patch[:, None] * matter
    one_coarse = np.zeros((sites, internal, 2), dtype=complex)
    one_coarse[:, :, 0] = complement
    one_coarse[:, :, 1] = projected
    two_coarse = np.zeros((sites, internal, 2, 2), dtype=complex)
    two_coarse[:, :, 0, 0] = complement
    two_coarse[:, :, 1, 1] = projected
    one_reduced = reduced_matter_density(one_coarse)
    two_reduced = reduced_matter_density(two_coarse)
    fine_reduced = reduced_matter_density(copied)
    check(
        "a redundant coarse copy is not an archived fine-site interrogation",
        np.linalg.norm(one_reduced - two_reduced) < 3e-12
        and np.linalg.norm(one_reduced - fine_reduced) > 0.01,
        {
            "one_vs_two_coarse": np.linalg.norm(one_reduced - two_reduced),
            "coarse_vs_fine": np.linalg.norm(one_reduced - fine_reduced),
        },
    )


def scalar_band_kernel(
    block: np.ndarray, momenta: np.ndarray, *, axis: int = 0
) -> np.ndarray:
    kernel = np.zeros((6, 6), dtype=complex)
    for momentum in momenta:
        vector_momentum = np.zeros(3)
        vector_momentum[axis] = momentum
        _, vector = c222.block_branch_eigenpair(block, vector_momentum)
        kernel += np.outer(vector, vector.conj()) / len(momenta)
    return kernel


@dataclass(frozen=True)
class FibreRow:
    scale_label: str
    c3_phase: float
    half_width: int
    branch_weight: float
    coarse_band_weight: float
    site_archived_band_weight: float
    site_archived_purity: float


def fibre_rows(
    scale_label: str,
    compiled: c222.Compiled,
    half_widths: tuple[int, ...],
) -> tuple[FibreRow, ...]:
    rows = []
    for block_row in c223.c3_blind_blocks(compiled.coin):
        positions, momenta, packet = c222.prepare_block_packet(
            block_row.block, 4096, 0.006
        )
        evolved = c210.local_molecular_step(packet, block_row.block, axis=0)
        kernel = scalar_band_kernel(block_row.block, momenta)
        for half_width in half_widths:
            branch = (np.abs(positions) <= half_width)[:, None] * evolved
            weight = float(np.vdot(branch, branch).real)
            coarse = branch / np.sqrt(weight)
            coarse_band = c222.block_branch_probability(
                coarse, momenta, block_row.block
            )
            site_band = float(
                sum(np.vdot(value, kernel @ value).real for value in branch)
                / weight
            )
            site_weights = np.sum(np.abs(branch) ** 2, axis=1)
            site_purity = float(np.sum(site_weights**2) / weight**2)
            rows.append(
                FibreRow(
                    scale_label,
                    block_row.c3_phase,
                    half_width,
                    weight,
                    coarse_band,
                    site_band,
                    site_purity,
                )
            )
    return tuple(rows)


def packet_fibre_controls(
    reference: c222.Compiled, held_out: c222.Compiled
) -> None:
    widths = (0, 16, 64, 128, 256, 512)
    rows = fibre_rows("reference", reference, widths) + fibre_rows(
        "held-out", held_out, widths
    )
    width_256 = [row for row in rows if row.half_width == 256]
    width_512 = [row for row in rows if row.half_width == 512]

    check(
        "coarse and site-resolving packet diagnostics share the declared patch weight and remain normalized",
        all(0 < row.branch_weight <= 1 + 3e-12 for row in rows)
        and all(0 < row.coarse_band_weight <= 1 + 3e-12 for row in rows)
        and all(0 < row.site_archived_band_weight <= 1 + 3e-12 for row in rows)
        and all(0 < row.site_archived_purity <= 1 + 3e-12 for row in rows),
        {
            "minimum_weight": min(row.branch_weight for row in rows),
            "maximum_weight": max(row.branch_weight for row in rows),
        },
    )
    check(
        "coarse width-256 outcomes preserve the scalar band while archived which-site information does not",
        min(row.branch_weight for row in width_256) > 0.97045
        and min(row.coarse_band_weight for row in width_256) > 0.999555
        and max(row.site_archived_band_weight for row in width_256) < 0.712081
        and max(row.site_archived_purity for row in width_256) < 0.002537,
        width_256,
    )
    check(
        "near-unit packet retention does not repair an archived site-resolving channel",
        min(row.branch_weight for row in width_512) > 0.999986
        and min(row.coarse_band_weight for row in width_512) > 0.9999996
        and max(row.site_archived_band_weight for row in width_512) < 0.712080
        and max(row.site_archived_purity for row in width_512) < 0.002394,
        width_512,
    )

    spans = []
    for scale_label in ("reference", "held-out"):
        for phase in sorted({row.c3_phase for row in rows}):
            selected = [
                row
                for row in rows
                if row.scale_label == scale_label and row.c3_phase == phase
            ]
            spans.append(
                (
                    scale_label,
                    phase,
                    max(row.coarse_band_weight for row in selected)
                    - min(row.coarse_band_weight for row in selected),
                    max(row.site_archived_band_weight for row in selected)
                    - min(row.site_archived_band_weight for row in selected),
                )
            )
    check(
        "broadening the coarse fibre repairs its band content but not a retained fine-site archive",
        min(row[2] for row in spans) > 0.28
        and max(row[3] for row in spans) < 5e-5,
        spans,
    )


def axis_controls(
    reference: c222.Compiled, held_out: c222.Compiled
) -> None:
    rows = []
    for scale_label, compiled in (
        ("reference", reference),
        ("held-out", held_out),
    ):
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
                weight = float(np.vdot(branch, branch).real)
                coarse_band = c222.block_branch_probability(
                    branch / np.sqrt(weight),
                    momenta,
                    block_row.block,
                    axis=axis,
                )
                kernel = scalar_band_kernel(
                    block_row.block, momenta, axis=axis
                )
                site_band = float(
                    sum(np.vdot(value, kernel @ value).real for value in branch)
                    / weight
                )
                values.append((weight, coarse_band, site_band))
            rows.append(
                (
                    scale_label,
                    block_row.c3_phase,
                    max(value[0] for value in values)
                    - min(value[0] for value in values),
                    max(value[1] for value in values)
                    - min(value[1] for value in values),
                    max(value[2] for value in values)
                    - min(value[2] for value in values),
                )
            )
    check(
        "co-oriented coarse and fine channel-projector diagnostics agree across cardinal axes",
        max(row[2] for row in rows) < 3e-12
        and max(row[3] for row in rows) < 1e-8
        and max(row[4] for row in rows) < 1e-6,
        rows,
    )


def predecessor_controls() -> None:
    predecessors = (
        ROOT
        / "scripts/local_click_strength_resolution_inertia_cycle225_2026_07_17.py",
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "LOCAL_CLICK_STRENGTH_RESOLUTION_INERTIA_CYCLE225_NOTE_2026-07-17.md",
    )
    check(
        "the resolution predecessor remains present",
        all(path.is_file() for path in predecessors),
        [path.name for path in predecessors],
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    reference = c222.compile_operator(c222.REFERENCE_SCALE)
    held_out = c222.compile_operator(c222.HELD_OUT_SCALE)
    check(
        "reference and frozen held-out candidate laws remain unitary",
        np.linalg.norm(reference.coin.conj().T @ reference.coin - np.eye(24))
        < 3e-12
        and np.linalg.norm(held_out.coin.conj().T @ held_out.coin - np.eye(24))
        < 3e-12,
        (reference.scale, held_out.scale),
    )
    finite_uncompute_controls()
    packet_fibre_controls(reference, held_out)
    axis_controls(reference, held_out)
    predecessor_controls()
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
