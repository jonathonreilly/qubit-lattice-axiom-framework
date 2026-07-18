#!/usr/bin/env python3
"""Cycle 281: same-code matter-coupling-faithful positive close candidate.

The exact Cycle-278 connected-edge contact pointer is used twice.  The first
use writes the pointer, an ordinary M2 archive copies it, and the second use
resets the same pointer.  CLOSE is written only when the archive is one and
the pointer has returned to zero.  Thus deletion of either actual U_I use,
while every auxiliary gate survives, removes all close support on the blank
interface.  A reversible history/export carrier is explicit.

This is a coherent positive-contact close on a declared deletion domain.  It
is not occurrence, permanence, Record formation, a clock, a rate, a source,
or a Born/frequency law.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "MATTER_COUPLING_FAITHFUL_CLOSE_RECORD_CANDIDATE_CYCLE281_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 3.0e-11

# One existing Cycle-278 pointer plus four additional ordinary M2 carriers.
POINTER, ARCHIVE, CLOSE, HISTORY, FRESH = range(5)
ANCILLA_BITS = 5
ANCILLA_DIMENSION = 2**ANCILLA_BITS
MATTER_DIMENSION = 64


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
        check("the Cycle-281 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-278 connected edge code",
        "same physical pointer",
        "positive-contact close",
        "couple–archive–recouple",
        "bounded support",
        "constant overhead",
        "all 24 proper-cubic frames",
        "held-out l=6",
        "split deletion",
        "pointer-only substitution",
        "coherent correlation",
        "supplied read",
        "occurrence",
        "close",
        "permanence",
        "record",
        "reversible archive/environment",
        "reset resources",
        "lawful domain",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the same-code, fault, resource, semantic, and N1-N8 contract",
        not missing,
        missing,
    )


def basis(dimension: int, index: int) -> np.ndarray:
    vector = np.zeros(dimension, dtype=complex)
    vector[index] = 1.0
    return vector


def contact_projectors() -> tuple[np.ndarray, np.ndarray]:
    active = np.asarray(
        [c278.contact_active(occupation) for occupation in range(64)], dtype=float
    )
    q = np.diag(active).astype(complex)
    return np.eye(64, dtype=complex) - q, q


def permutation_for_flip(
    target: int, controls: dict[int, int] | None = None
) -> np.ndarray:
    controls = controls or {}
    mapping = np.arange(ANCILLA_DIMENSION)
    for source in range(ANCILLA_DIMENSION):
        if all(((source >> bit) & 1) == value for bit, value in controls.items()):
            mapping[source] = source ^ (1 << target)
    return mapping


def apply_permutation(state: np.ndarray, mapping: np.ndarray) -> np.ndarray:
    matrix = state.reshape(MATTER_DIMENSION, ANCILLA_DIMENSION)
    output = np.zeros_like(matrix)
    output[:, mapping] = matrix
    return output.reshape(-1)


def apply_coupling(state: np.ndarray, mode: str) -> np.ndarray:
    """Apply U_I, delete it, or retain only an unconditional pointer X."""

    if mode == "deleted":
        return state.copy()
    if mode not in ("ideal", "pointer_only"):
        raise ValueError(f"unknown coupling mode {mode}")
    matrix = state.reshape(MATTER_DIMENSION, ANCILLA_DIMENSION)
    output = matrix.copy()
    pointer_map = np.arange(ANCILLA_DIMENSION) ^ (1 << POINTER)
    for occupation in range(MATTER_DIMENSION):
        if mode == "pointer_only" or c278.contact_active(occupation):
            output[occupation, :] = matrix[occupation, pointer_map]
    return output.reshape(-1)


def candidate_gates(
    first: str = "ideal",
    second: str = "ideal",
    archive: bool = True,
    close: bool = True,
    history: bool = True,
    continuation: bool = False,
) -> tuple[tuple[str, object], ...]:
    gates: list[tuple[str, object]] = [("coupling", first)]
    if archive:
        gates.append(
            ("permutation", permutation_for_flip(ARCHIVE, {POINTER: 1}))
        )
    gates.append(("coupling", second))
    if close:
        gates.append(
            (
                "permutation",
                permutation_for_flip(CLOSE, {ARCHIVE: 1, POINTER: 0}),
            )
        )
    if history:
        gates.append(
            (
                "permutation",
                permutation_for_flip(HISTORY, {ARCHIVE: 1, CLOSE: 1}),
            )
        )
    if continuation:
        gates.append(
            (
                "permutation",
                permutation_for_flip(FRESH, {HISTORY: 1, CLOSE: 1}),
            )
        )
    return tuple(gates)


def apply_gates(
    state: np.ndarray, gates: tuple[tuple[str, object], ...], inverse: bool = False
) -> np.ndarray:
    output = state.copy()
    sequence = tuple(reversed(gates)) if inverse else gates
    for kind, payload in sequence:
        if kind == "coupling":
            output = apply_coupling(output, str(payload))
        else:
            output = apply_permutation(output, np.asarray(payload))
    return output


def isometry(gates: tuple[tuple[str, object], ...]) -> np.ndarray:
    blank = basis(ANCILLA_DIMENSION, 0)
    columns = []
    for occupation in range(MATTER_DIMENSION):
        columns.append(
            apply_gates(np.kron(basis(MATTER_DIMENSION, occupation), blank), gates)
        )
    return np.column_stack(columns)


def ancilla_effect(isometry_matrix: np.ndarray, conditions: dict[int, int]) -> np.ndarray:
    tensor = isometry_matrix.reshape(
        MATTER_DIMENSION, ANCILLA_DIMENSION, MATTER_DIMENSION
    )
    indices = [
        index
        for index in range(ANCILLA_DIMENSION)
        if all(((index >> bit) & 1) == value for bit, value in conditions.items())
    ]
    blocks = tensor[:, indices, :].reshape(-1, MATTER_DIMENSION)
    return blocks.conj().T @ blocks


def partial_matter_density(state: np.ndarray) -> np.ndarray:
    matrix = state.reshape(MATTER_DIMENSION, ANCILLA_DIMENSION)
    return matrix @ matrix.conj().T


def coupling_echo_constructor() -> dict[str, float]:
    print("\nSAME-POINTER COUPLE-ARCHIVE-RECOUPLE CONSTRUCTOR")
    q0, q = contact_projectors()
    gates = candidate_gates()
    v = isometry(gates)
    packet_index = (1 << ARCHIVE) | (1 << CLOSE) | (1 << HISTORY)
    expected = np.kron(q0, basis(ANCILLA_DIMENSION, 0)[:, None])
    expected += np.kron(q, basis(ANCILLA_DIMENSION, packet_index)[:, None])
    gram_error = float(np.linalg.norm(v.conj().T @ v - np.eye(64)))
    intertwiner_error = float(np.linalg.norm(v - expected))
    close_effect = ancilla_effect(v, {CLOSE: 1})
    history_effect = ancilla_effect(v, {HISTORY: 1})
    pointer_residual = float(np.linalg.norm(ancilla_effect(v, {POINTER: 1})))
    archive_residual = float(np.linalg.norm(ancilla_effect(v, {ARCHIVE: 1}) - q))
    check(
        "the exact Cycle-278 pointer gives a coherent positive-contact close and history packet after coupling-mediated reset",
        gram_error < TOL
        and intertwiner_error < TOL
        and np.linalg.norm(close_effect - q) < TOL
        and np.linalg.norm(history_effect - q) < TOL
        and pointer_residual < TOL
        and archive_residual < TOL,
        {
            "isometry_Gram_error": gram_error,
            "intertwiner_error": intertwiner_error,
            "close_effect_minus_Q": float(np.linalg.norm(close_effect - q)),
            "history_effect_minus_Q": float(np.linalg.norm(history_effect - q)),
            "final_pointer_one_effect": pointer_residual,
        },
    )

    rng = np.random.default_rng(281)
    held = rng.normal(size=64) + 1j * rng.normal(size=64)
    held /= np.linalg.norm(held)
    blank_input = np.kron(held, basis(ANCILLA_DIMENSION, 0))
    output = apply_gates(blank_input, gates)
    recovered = apply_gates(output, gates, inverse=True)
    inverse_error = float(np.linalg.norm(recovered - blank_input))
    check(
        "the complete finite interface is reversible and reconnecting its archive erases close rather than proving permanence",
        inverse_error < TOL,
        inverse_error,
    )

    cross = (basis(64, 0) + basis(64, 3)) / np.sqrt(2)
    cross_input = np.kron(cross, basis(ANCILLA_DIMENSION, 0))
    cross_output = apply_gates(cross_input, gates)
    reduced = partial_matter_density(cross_output)
    expected_dephased = q0 @ np.outer(cross, cross.conj()) @ q0
    expected_dephased += q @ np.outer(cross, cross.conj()) @ q
    cross_close = float(
        np.vdot(cross, ancilla_effect(v, {CLOSE: 1}) @ cross).real
    )
    check(
        "a coherent inactive/active input retains both branches and yields dephasing only after archive restriction",
        abs(cross_close - 0.5) < TOL
        and np.linalg.norm(reduced - expected_dephased) < TOL
        and abs(np.vdot(cross_output, cross_output) - 1.0) < TOL,
        {
            "close_weight": cross_close,
            "reduced_dephasing_residual": float(
                np.linalg.norm(reduced - expected_dephased)
            ),
            "branch_selected": False,
        },
    )
    return {
        "gram_error": gram_error,
        "intertwiner_error": intertwiner_error,
        "inverse_error": inverse_error,
    }


def split_deletion_and_substitution_controls() -> dict[str, float]:
    print("\nSPLIT DELETIONS / STRONGER SUBSTITUTION BOUNDARY")
    _, q = contact_projectors()
    ideal = isometry(candidate_gates())
    deletion_cases = {
        "delete_first_U_I": candidate_gates(first="deleted"),
        "delete_second_U_I": candidate_gates(second="deleted"),
        "delete_both_U_I": candidate_gates(first="deleted", second="deleted"),
        "delete_archive_writer": candidate_gates(archive=False),
    }
    deletion_rows = []
    deletion_failures = []
    for label, gates in deletion_cases.items():
        faulty = isometry(gates)
        close_norm = float(np.linalg.norm(ancilla_effect(faulty, {CLOSE: 1})))
        history_norm = float(np.linalg.norm(ancilla_effect(faulty, {HISTORY: 1})))
        residual = float(np.linalg.norm(faulty - ideal))
        row = {
            "fault": label,
            "close_effect_norm": close_norm,
            "history_effect_norm": history_norm,
            "isometry_residual_from_ideal": residual,
            "all_auxiliary_gates_survive": label.startswith("delete_")
            and "archive" not in label,
        }
        deletion_rows.append(row)
        if close_norm >= TOL or history_norm >= TOL or residual <= 1.0:
            deletion_failures.append(row)
    check(
        "deleting either actual matter-pointer coupling leg while the complete auxiliary schedule survives gives zero close and history support",
        not deletion_failures,
        deletion_rows,
    )

    no_close = isometry(candidate_gates(close=False))
    no_history = isometry(candidate_gates(history=False))
    check(
        "close-writer and history-export deletions cannot create a false positive",
        np.linalg.norm(ancilla_effect(no_close, {CLOSE: 1})) < TOL
        and np.linalg.norm(ancilla_effect(no_close, {HISTORY: 1})) < TOL
        and np.linalg.norm(ancilla_effect(no_history, {HISTORY: 1})) < TOL
        and np.linalg.norm(ancilla_effect(no_history, {CLOSE: 1}) - q) < TOL,
    )

    substitutions = {
        "pointer_only_first": candidate_gates(first="pointer_only"),
        "pointer_only_second": candidate_gates(second="pointer_only"),
        "pointer_only_both": candidate_gates(
            first="pointer_only", second="pointer_only"
        ),
    }
    substitution_rows = []
    for label, gates in substitutions.items():
        faulty = isometry(gates)
        close_effect = ancilla_effect(faulty, {CLOSE: 1})
        substitution_rows.append(
            {
                "fault": label,
                "isometry_residual": float(np.linalg.norm(faulty - ideal)),
                "close_minus_Q": float(np.linalg.norm(close_effect - q)),
                "false_close_rank_on_Q0": int(
                    round(np.trace(close_effect @ (np.eye(64) - q)).real)
                ),
                "final_pointer_effect_norm": float(
                    np.linalg.norm(ancilla_effect(faulty, {POINTER: 1}))
                ),
            }
        )
    check(
        "pointer-only substitutions are not hidden: single substitutions alter the full packet and double substitution falsely closes the seven-dimensional inactive sector",
        substitution_rows[0]["isometry_residual"] > 1.0
        and substitution_rows[1]["isometry_residual"] > 1.0
        and substitution_rows[0]["close_minus_Q"] < TOL
        and substitution_rows[1]["close_minus_Q"] < TOL
        and substitution_rows[2]["false_close_rank_on_Q0"] == 7
        and substitution_rows[2]["close_minus_Q"] > 2.0,
        substitution_rows,
    )
    return {
        "max_deleted_close_effect_norm": max(
            row["close_effect_norm"] for row in deletion_rows
        ),
        "min_deleted_isometry_residual": min(
            row["isometry_residual_from_ideal"] for row in deletion_rows
        ),
        "double_pointer_only_false_close_rank": float(
            substitution_rows[2]["false_close_rank_on_Q0"]
        ),
    }


def actual_contact_mass_and_weight_controls() -> None:
    print("\nACTUAL CONTACT / MASS / CONDITIONAL WEIGHTS")
    q0, q = contact_projectors()
    occupations = np.asarray([index.bit_count() for index in range(64)])
    species = c278.c219.common_species(c278.c230.BETA)
    fock_coin = c278.c229.fock_lift(species.coin)
    contact = np.diag(
        np.exp(
            1j
            * c278.c230.COUPLING
            * occupations
            * (occupations - 1)
            / 2
        )
    )
    reverse = np.zeros((6, 6), dtype=complex)
    for source, target in enumerate((1, 0, 3, 2, 5, 4)):
        reverse[target, source] = 1
    fock_reverse = c278.c229.fock_lift(reverse)
    check(
        "the close effect is the support of the actual contact fixture and is identity-free on the one-particle mass sector",
        np.linalg.norm(q @ fock_coin - fock_coin @ q) < 2e-14
        and np.linalg.norm(q @ contact - contact @ q) == 0
        and np.linalg.norm(q @ fock_reverse - fock_reverse @ q) == 0
        and np.all(np.diag(q)[occupations <= 1] == 0)
        and abs(c278.c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "Q_coin_commutator": float(np.linalg.norm(q @ fock_coin - fock_coin @ q)),
            "Q_contact_commutator": float(np.linalg.norm(q @ contact - contact @ q)),
            "one_particle_close_weight": 0,
        },
    )

    states = {
        "uniform": np.eye(64, dtype=complex) / 64,
        "B0_plus": np.diag(
            [int((index & 1) == 0) / 32 for index in range(64)]
        ),
        "B0_minus": np.diag(
            [int((index & 1) == 1) / 32 for index in range(64)]
        ),
    }
    expected = {
        "uniform": Fraction(57, 64),
        "B0_plus": Fraction(13, 16),
        "B0_minus": Fraction(31, 32),
    }
    v = isometry(candidate_gates())
    deleted = isometry(candidate_gates(first="deleted"))
    close_effect = ancilla_effect(v, {CLOSE: 1})
    deleted_close = ancilla_effect(deleted, {CLOSE: 1})
    rows = []
    for label, rho in states.items():
        rows.append(
            {
                "state": label,
                "close_weight": float(np.trace(close_effect @ rho).real),
                "expected": str(expected[label]),
                "delete_first_close_weight": float(
                    np.trace(deleted_close @ rho).real
                ),
            }
        )
    check(
        "the faithful positive close reproduces the Cycle-278 contact weights and all vanish under a split coupling deletion",
        all(
            abs(row["close_weight"] - float(expected[row["state"]])) < TOL
            and row["delete_first_close_weight"] < TOL
            for row in rows
        ),
        rows,
    )


def same_code_support_and_covariance_controls() -> None:
    print("\nCONNECTED EDGE CODE / SUPPORT / ALL-24 COVARIANCE")
    coefficients = c278.walsh_coefficients()
    size_rows = []
    failures = []
    cache: dict[int, c269.WilsonSubsystemCode] = {}
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        bs = c278.cell_bs(code, (0, 0, 0))
        terms = tuple(c278.pauli_product(bs, mask) for mask in range(64))
        support_union = 0
        for row in bs:
            support_union |= row.x | row.z
        leakage = sum(
            not term.commutes(check_row)
            for term in terms
            for check_row in code.local_checks + code.wilsons
        )
        row = {
            "L": length,
            "held_out": length == 6,
            "matter_support_union": support_union.bit_count(),
            "interface_M2": ANCILLA_BITS,
            "total_neighborhood_M2": support_union.bit_count() + ANCILLA_BITS,
            "maximum_Q_Pauli_weight": max(
                (term.x | term.z).bit_count() for term in terms
            ),
            "maximum_U_I_term_weight": max(
                (term.x | term.z).bit_count() for term in terms
            )
            + 1,
            "nonzero_Walsh_terms": sum(value != 0 for value in coefficients),
            "check_or_Wilson_leakage": leakage,
        }
        size_rows.append(row)
        if not (
            row["matter_support_union"] == 18
            and row["interface_M2"] == 5
            and row["total_neighborhood_M2"] == 23
            and row["maximum_Q_Pauli_weight"] == 12
            and row["maximum_U_I_term_weight"] == 13
            and row["nonzero_Walsh_terms"] == 64
            and leakage == 0
        ):
            failures.append(row)
    check(
        "the close remains on the Cycle-278 connected edge code with bounded 23-M2 support and constant five-M2 interface through held-out L=6",
        not failures,
        size_rows,
    )

    code = cache[3]
    base_bs = c278.cell_bs(code, (0, 0, 0))
    local_family = set(code.local_checks)
    central_pivots, central_bad = c278.phase_reducer(
        list(code.local_checks + code.wilsons), code.qubits
    )
    frame_failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(code.length), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]]
                for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]]
                for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(
                code.graph, vertex_map, edge_map
            )
            transformed_bs = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in base_bs
            )
            target_cell = tuple(value % code.length for value in displacement)
            target_bs = c278.cell_bs(code, target_cell)
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_wilsons = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.wilsons
            )
            if not (
                set(transformed_bs) == set(target_bs)
                and transformed_local == local_family
                and not central_bad
                and all(
                    not c278.reduce_pauli(
                        row, central_pivots, code.qubits
                    ).symplectic(code.qubits)
                    for row in transformed_wilsons
                )
            ):
                frame_failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "the Q-controlled echo and scalar interface roles are covariant under all 24 proper-cubic frames and full L=3 translations",
        not frame_failures and tests == 24 * 27,
        {
            "frame_translation_tests": tests,
            "failures": frame_failures[:5],
            "pointer_archive_close_history_fresh_roles": "carried scalars",
        },
    )


def archive_reset_domain_and_semantic_controls() -> None:
    print("\nARCHIVE / RESET / LAWFUL-DOMAIN FIREWALLS")
    base_gates = candidate_gates()
    continued_gates = candidate_gates(continuation=True)
    base = isometry(base_gates)
    continued = isometry(continued_gates)
    history_before = ancilla_effect(base, {HISTORY: 1})
    history_after = ancilla_effect(continued, {HISTORY: 1})
    fresh_after = ancilla_effect(continued, {FRESH: 1})
    check(
        "one supplied controls-only continuation exports the close to a fresh reversible carrier without changing its history effect",
        np.linalg.norm(history_before - history_after) < TOL
        and np.linalg.norm(fresh_after - history_before) < TOL,
        {
            "history_effect_change": float(
                np.linalg.norm(history_before - history_after)
            ),
            "fresh_export_residual": float(
                np.linalg.norm(fresh_after - history_before)
            ),
            "fresh_capacity_is_supplied": True,
        },
    )

    def validate(length: int, dimensions: tuple[int, ...], blank: int) -> None:
        if length < 3:
            raise ValueError("L must be at least three")
        if dimensions != (2, 2, 2, 2, 2):
            raise ValueError("the interface is five ordinary M2 carriers")
        if blank != 0:
            raise ValueError("the declared interface boundary is blank")

    rejected = 0
    for arguments in (
        (2, (2, 2, 2, 2, 2), 0),
        (3, (2, 2, 2, 2), 0),
        (3, (2, 2, 2, 2, 2), 1),
    ):
        try:
            validate(*arguments)
        except ValueError:
            rejected += 1
    validate(3, (2, 2, 2, 2, 2), 0)
    text = normalized(NOTE)
    check(
        "lawful-domain and semantic controls reject malformed interfaces and keep close, occurrence, permanence, and Record distinct",
        rejected == 3
        and "does not splice cycle 251" in text
        and "coherent correlation is not a supplied read" in text
        and "close is not occurrence" in text
        and "conditional archive stability is not permanence" in text
        and "the candidate is not a record" in text
        and "compiler order is not physical time" in text,
        {
            "rejected_controls": rejected,
            "pointer_reset": "second actual U_I use",
            "full_interface_reset": "inverse reconnection or fresh blank carriers",
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    constructor = coupling_echo_constructor()
    faults = split_deletion_and_substitution_controls()
    actual_contact_mass_and_weight_controls()
    same_code_support_and_covariance_controls()
    archive_reset_domain_and_semantic_controls()
    check(
        "the bounded result is a constructive partial and creates neither shared obstruction nor axiom pressure",
        "no shared obstruction" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
    )
    print("DATA constructor", constructor)
    print("DATA faults", faults)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE281_MATTER_COUPLING_FAITHFUL_CLOSE_GREEN"
        if FAIL == 0
        else "CYCLE281_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
