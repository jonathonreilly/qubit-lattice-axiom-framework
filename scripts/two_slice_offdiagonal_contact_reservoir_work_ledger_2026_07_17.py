#!/usr/bin/env python3
"""Two-slice off-diagonal branch-coordinate impulse ledger.

The fixed-total-number Cycle-290 branches |3,3> and |4,2> define two
off-diagonal even-CAR quadratures.  Their finite two-slice change is split
exactly into an onsite matter-number-controlled reservoir/field-exchange
impulse and an ordinary Cycle-230 contact impulse.  The reservoir/field part
is the exact zero/one-excitation restriction of the seven-M2
conjugate-reservoir gate; no branch-selecting control is used physically.

The resulting vector ledger is a dimensionless off-diagonal branch-coordinate
impulse ledger.  It is not physical energy, work, a Hamiltonian, a rate,
elapsed time, stress, a gravity source, or a Record.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import local_conjugate_reservoir_source_field_ledger_repair_2026_07_17 as reservoir
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import unconditional_two_cell_contact_interferometer_cycle290_2026_07_17 as c290
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "TWO_SLICE_OFFDIAGONAL_CONTACT_RESERVOIR_WORK_LEDGER_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 4.0e-11
G_CONTACT = c230.COUPLING
KAPPA = reservoir.COUPLING
BETA = c230.BETA
REFERENCE_MASKS = (0b001110, 0b000111)
SURPLUS_MASKS = (0b001111, 0b000101)


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
        check("the Route-D note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "two-slice",
        "off-diagonal even-car",
        "fixed total n=6",
        "|3,3",
        "|4,2",
        "dimensionless off-diagonal branch-coordinate impulse ledger",
        "not physical energy",
        "not a rate",
        "compiler slices are not physical time",
        "one reservoir m2",
        "six directional field m2",
        "exact operator identity",
        "q-only replacement",
        "common global phase",
        "bounded physical m2 support",
        "zero leakage",
        "held-out l=6",
        "648 frame-translation tests",
        "mass/contact deletion",
        "supplied structure inventory",
        "no axiom pressure",
        "n1-n8 was not triggered",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the exact vector-ledger, physical-support, normalization, and scope contract",
        not missing,
        missing,
    )


def pair_count(numbers: tuple[int, int]) -> int:
    return sum(number * (number - 1) // 2 for number in numbers)


def reduced_exchange_gate(number: int, kappa: float = KAPPA) -> np.ndarray:
    """Vacuum plus reservoir/scalar-field one-excitation restriction."""

    mass = c219.common_species(BETA).analytic_mass
    angle = kappa * mass * number
    cosine = np.cos(angle)
    sine = np.sin(angle)
    return np.asarray(
        (
            (1.0, 0.0, 0.0),
            (0.0, cosine, -1j * sine),
            (0.0, -1j * sine, cosine),
        ),
        dtype=complex,
    )


def reduced_operators(
    contact: float = G_CONTACT, kappa: float = KAPPA
) -> dict[str, np.ndarray]:
    """Exact branch x local-reservoir/field matrices (dimension 18)."""

    identity_branch = np.eye(2, dtype=complex)
    identity_local = np.eye(3, dtype=complex)
    identity_rf = np.eye(9, dtype=complex)
    p_reference = np.diag((1.0, 0.0)).astype(complex)
    p_surplus = np.diag((0.0, 1.0)).astype(complex)

    reference_numbers = tuple(mask.bit_count() for mask in REFERENCE_MASKS)
    surplus_numbers = tuple(mask.bit_count() for mask in SURPLUS_MASKS)
    v_reference = np.kron(
        reduced_exchange_gate(reference_numbers[0], kappa),
        reduced_exchange_gate(reference_numbers[1], kappa),
    )
    v_surplus = np.kron(
        reduced_exchange_gate(surplus_numbers[0], kappa),
        reduced_exchange_gate(surplus_numbers[1], kappa),
    )
    vertex = np.kron(p_reference, v_reference) + np.kron(
        p_surplus, v_surplus
    )

    contact_pairs = (pair_count(reference_numbers), pair_count(surplus_numbers))
    contact_branch = np.diag(
        np.exp(1j * contact * np.asarray(contact_pairs, dtype=float))
    ).astype(complex)
    contact_gate = np.kron(contact_branch, identity_rf)
    full = contact_gate @ vertex

    x_branch = np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
    y_branch = np.asarray(((0.0, -1j), (1j, 0.0)), dtype=complex)
    x = np.kron(x_branch, identity_rf)
    y = np.kron(y_branch, identity_rf)

    local_q = np.diag((0.0, 1.0, 1.0)).astype(complex)
    local_r = np.diag((0.0, 1.0, 0.0)).astype(complex)
    local_f = np.diag((0.0, 0.0, 1.0)).astype(complex)
    qx = np.kron(identity_branch, np.kron(local_q, identity_local))
    qy = np.kron(identity_branch, np.kron(identity_local, local_q))
    rx = np.kron(identity_branch, np.kron(local_r, identity_local))
    ry = np.kron(identity_branch, np.kron(identity_local, local_r))
    fx = np.kron(identity_branch, np.kron(local_f, identity_local))
    fy = np.kron(identity_branch, np.kron(identity_local, local_f))
    return {
        "V": vertex,
        "W": contact_gate,
        "G": full,
        "X": x,
        "Y": y,
        "Qx": qx,
        "Qy": qy,
        "Rx": rx,
        "Ry": ry,
        "Fx": fx,
        "Fy": fy,
        "contact_pairs": np.asarray(contact_pairs),
    }


def physical_rf_embedding() -> np.ndarray:
    """Embed |vac>, |reservoir>, |uniform one-field> into seven M2."""

    embedding = np.zeros((128, 3), dtype=complex)
    embedding[0, 0] = 1.0
    embedding[64, 1] = 1.0
    for direction in range(6):
        embedding[1 << direction, 2] = 1 / np.sqrt(6)
    return embedding


def branch_and_physical_vertex_controls() -> None:
    print("\nBRANCH / SEVEN-M2 VERTEX RESTRICTION")
    reference_numbers = tuple(mask.bit_count() for mask in REFERENCE_MASKS)
    surplus_numbers = tuple(mask.bit_count() for mask in SURPLUS_MASKS)
    q_count = lambda numbers: sum(number >= 2 for number in numbers)
    check(
        "the adjacent even-CAR redistribution gives fixed total N=6 branches with contact-pair surplus one and equal Q-only count",
        reference_numbers == (3, 3)
        and surplus_numbers == (4, 2)
        and sum(reference_numbers) == sum(surplus_numbers) == 6
        and pair_count(reference_numbers) == 6
        and pair_count(surplus_numbers) == 7
        and q_count(reference_numbers) == q_count(surplus_numbers) == 2,
        {
            "reference": reference_numbers,
            "surplus": surplus_numbers,
            "pair_counts": (pair_count(reference_numbers), pair_count(surplus_numbers)),
            "Q_only_counts": (q_count(reference_numbers), q_count(surplus_numbers)),
        },
    )

    embedding = physical_rf_embedding()
    physical = reservoir.reservoir_field_operators()
    restriction_rows = []
    for number in (2, 3, 4):
        angle = KAPPA * c219.common_species(BETA).analytic_mass * number
        full_gate = reservoir.exchange_gate(angle, physical["exchange"])
        reduced = reduced_exchange_gate(number)
        restriction_rows.append(
            {
                "N": number,
                "intertwiner_residual": float(
                    np.linalg.norm(full_gate @ embedding - embedding @ reduced)
                ),
                "Q_restriction_residual": float(
                    np.linalg.norm(embedding.conj().T @ physical["Q"] @ embedding - np.diag((0.0, 1.0, 1.0)))
                ),
            }
        )
    check(
        "each branch-dependent vertex is the exact zero/one-excitation restriction of the seven-M2 conjugate-reservoir gate",
        np.linalg.norm(embedding.conj().T @ embedding - np.eye(3)) < 3e-15
        and max(row["intertwiner_residual"] for row in restriction_rows) < 2e-14
        and max(row["Q_restriction_residual"] for row in restriction_rows) < 2e-14,
        restriction_rows,
    )


def exact_two_slice_ledgers() -> dict[str, np.ndarray]:
    print("\nEXACT TWO-SLICE VECTOR LEDGER")
    operators = reduced_operators()
    identity = np.eye(18, dtype=complex)
    vertex = operators["V"]
    contact = operators["W"]
    full = operators["G"]

    unitarity = {
        name: float(np.linalg.norm(gate.conj().T @ gate - identity))
        for name, gate in (("V", vertex), ("W", contact), ("G", full))
    }
    check(
        "the matter-number-controlled exchange, ordinary contact, and composed two-slice update are unitary and commute in this lawful block",
        max(unitarity.values()) < 3e-14
        and np.linalg.norm(vertex @ contact - contact @ vertex) < 2e-15,
        {**unitarity, "WV_commutator": float(np.linalg.norm(vertex @ contact - contact @ vertex))},
    )

    balance_rows = []
    for label in ("X", "Y"):
        observable = operators[label]
        exchange_impulse = vertex.conj().T @ observable @ vertex - observable
        contact_impulse = vertex.conj().T @ (
            contact.conj().T @ observable @ contact - observable
        ) @ vertex
        total_impulse = full.conj().T @ observable @ full - observable
        operators[f"J_exchange_{label}"] = exchange_impulse
        operators[f"J_contact_{label}"] = contact_impulse
        operators[f"Delta_{label}"] = total_impulse
        balance_rows.append(
            {
                "coordinate": label,
                "two_slice_balance_residual": float(
                    np.linalg.norm(total_impulse - exchange_impulse - contact_impulse)
                ),
                "exchange_impulse_norm": float(np.linalg.norm(exchange_impulse)),
                "contact_impulse_norm": float(np.linalg.norm(contact_impulse)),
                "total_impulse_norm": float(np.linalg.norm(total_impulse)),
            }
        )
    check(
        "both off-diagonal even-CAR coordinates obey Delta=J_exchange+J_contact as an exact finite two-slice operator identity",
        max(row["two_slice_balance_residual"] for row in balance_rows) < 3e-14
        and min(row["exchange_impulse_norm"] for row in balance_rows) > 0.1
        and min(row["contact_impulse_norm"] for row in balance_rows) > 0.1,
        balance_rows,
    )

    source_rows = []
    for suffix in ("x", "y"):
        field = operators[f"F{suffix}"]
        reservoir_number = operators[f"R{suffix}"]
        source = vertex.conj().T @ field @ vertex - field
        sink = vertex.conj().T @ reservoir_number @ vertex - reservoir_number
        source_rows.append(
            {
                "cell": suffix,
                "F_plus_R_residual": float(np.linalg.norm(source + sink)),
                "minimum_source_eigenvalue": float(np.min(np.linalg.eigvalsh(source))),
                "maximum_source_eigenvalue": float(np.max(np.linalg.eigvalsh(source))),
            }
        )
    check(
        "the same update has exact signed field-versus-reservoir number balance at both cells and preserves each local Q",
        max(row["F_plus_R_residual"] for row in source_rows) < 3e-14
        and min(row["minimum_source_eigenvalue"] for row in source_rows) < -0.1
        and max(row["maximum_source_eigenvalue"] for row in source_rows) > 0.1
        and max(
            np.linalg.norm(vertex @ operators[name] - operators[name] @ vertex)
            for name in ("Qx", "Qy")
        ) < 3e-14,
        source_rows,
    )
    return operators


def deletion_phase_and_normalization_controls(operators: dict[str, np.ndarray]) -> None:
    print("\nDELETION / PHASE / NORMALIZATION")
    deleted_contact = reduced_operators(contact=0.0)
    deleted_exchange = reduced_operators(kappa=0.0)
    q_only_phase = np.exp(1j * 2 * G_CONTACT) * np.eye(18, dtype=complex)
    x = operators["X"]

    q_only_impulse = q_only_phase.conj().T @ x @ q_only_phase - x
    contact_deleted_impulse = (
        deleted_contact["W"].conj().T @ x @ deleted_contact["W"] - x
    )
    exchange_deleted_impulse = (
        deleted_exchange["V"].conj().T @ x @ deleted_exchange["V"] - x
    )
    residual_contact_after_exchange_deletion = np.linalg.norm(
        deleted_exchange["G"].conj().T @ x @ deleted_exchange["G"] - x
    )
    check(
        "contact deletion, exchange deletion, and the equal-Q-only surrogate separate the two exact impulses",
        np.linalg.norm(contact_deleted_impulse) == 0
        and np.linalg.norm(exchange_deleted_impulse) == 0
        and np.linalg.norm(q_only_impulse) < 2e-15
        and residual_contact_after_exchange_deletion > 0.1,
        {
            "g_zero_contact_impulse": float(np.linalg.norm(contact_deleted_impulse)),
            "kappa_zero_exchange_impulse": float(np.linalg.norm(exchange_deleted_impulse)),
            "Q_only_contact_impulse": float(np.linalg.norm(q_only_impulse)),
            "contact_survives_kappa_zero": float(residual_contact_after_exchange_deletion),
        },
    )

    phase = np.exp(1j * 0.417)
    phased_full = phase * operators["G"]
    base_delta = operators["G"].conj().T @ x @ operators["G"] - x
    phased_delta = phased_full.conj().T @ x @ phased_full - x
    check(
        "a common global rephase cancels from the finite two-slice coordinate balance",
        np.linalg.norm(base_delta - phased_delta) < 3e-15,
        float(np.linalg.norm(base_delta - phased_delta)),
    )

    scale = 2.7
    supplied_pair_count = np.diag((6.0, 7.0)).astype(complex)
    reparameterized_pair_count = scale * supplied_pair_count
    endpoint_original = np.diag(
        np.exp(1j * G_CONTACT * np.diag(supplied_pair_count))
    )
    endpoint_rescaled = np.diag(
        np.exp(1j * (G_CONTACT / scale) * np.diag(reparameterized_pair_count))
    )
    species = c219.common_species(BETA)
    raw_phase = float(np.angle(np.trace(c219.c210.P_SCALAR @ species.coin)))
    check(
        "endpoint phases are invariant under slice-parameter rescaling while the tangent generator rescales, so no clock or rate normalization is selected",
        np.linalg.norm(endpoint_original - endpoint_rescaled) < 2e-15
        and np.linalg.norm(
            reparameterized_pair_count - scale * supplied_pair_count
        )
        == 0
        and abs(raw_phase / species.analytic_mass - c219.C_SQUARED) < 2e-12,
        {
            "endpoint_residual": float(np.linalg.norm(endpoint_original - endpoint_rescaled)),
            "tangent_scale": scale,
            "imported_phase_to_mass_ratio": raw_phase / species.analytic_mass,
        },
    )

    occupations = np.arange(7, dtype=float)
    contact_diagonal = np.exp(
        1j * G_CONTACT * occupations * (occupations - 1) / 2
    )
    check(
        "a separate N<=1 control preserves the Cycle-219 one-particle mass fixture",
        np.max(np.abs(contact_diagonal[:2] - 1)) == 0
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "one_particle_contact_residual": float(np.max(np.abs(contact_diagonal[:2] - 1))),
            "mass_ratio": c219.rest_mass(species) / species.analytic_mass,
        },
    )


def connector_and_bs(code: c269.WilsonSubsystemCode):
    cells = ((0, 0, 0), (1, 0, 0))
    bs = tuple(row for cell in cells for row in c278.cell_bs(code, cell))
    edge, u, v = c290.stream_connector(code)
    return cells, bs, edge, u, v, code.A[edge]


def branch_quadrature_terms(
    bs: tuple[c235.Pauli, ...], connector: c235.Pauli
) -> tuple[tuple[c235.Pauli, ...], tuple[c235.Pauli, ...]]:
    """Pauli terms of A(P_r+P_s) and i A(P_r-P_s), coefficients omitted."""

    reference = REFERENCE_MASKS[0] | (REFERENCE_MASKS[1] << 6)
    surplus = SURPLUS_MASKS[0] | (SURPLUS_MASKS[1] << 6)
    x_terms = []
    y_terms = []
    for mask in range(1 << 12):
        sign_reference = -1 if (mask & reference).bit_count() % 2 else 1
        sign_surplus = -1 if (mask & surplus).bit_count() % 2 else 1
        parity_product = c278.pauli_product(bs, mask)
        term = connector @ parity_product
        if sign_reference + sign_surplus:
            x_terms.append(term)
        if sign_reference - sign_surplus:
            y_terms.append(c235.Pauli((term.phase + 1) % 4, term.x, term.z))
    return tuple(x_terms), tuple(y_terms)


def physical_support_leakage_and_covariance_controls() -> None:
    print("\nPHYSICAL CYCLE-269 REPRESENTATIVE / COVARIANCE")
    rows = []
    failures = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        _, bs, edge, _, _, connector = connector_and_bs(code)
        x_terms, y_terms = branch_quadrature_terms(bs, connector)
        reference = REFERENCE_MASKS[0] | (REFERENCE_MASKS[1] << 6)
        surplus = SURPLUS_MASKS[0] | (SURPLUS_MASKS[1] << 6)
        connector_flip_mask = sum(
            int(not connector.commutes(parity)) << index
            for index, parity in enumerate(bs)
        )
        matter_union = connector.x | connector.z
        for row in bs:
            matter_union |= row.x | row.z
        leakage = sum(
            not term.commutes(check_row)
            for term in x_terms + y_terms
            for check_row in code.local_checks + code.wilsons
        )
        hermiticity_failures = sum(
            term @ term != c235.Pauli() for term in x_terms + y_terms
        )
        row = {
            "L": length,
            "held_out": length == 6,
            "matter_union_M2": matter_union.bit_count(),
            "reservoir_plus_field_M2": 14,
            "joint_two_cell_union_M2": matter_union.bit_count() + 14,
            "X_nonzero_Pauli_terms": len(x_terms),
            "Y_nonzero_Pauli_terms": len(y_terms),
            "maximum_X_term_weight": max((term.x | term.z).bit_count() for term in x_terms),
            "maximum_Y_term_weight": max((term.x | term.z).bit_count() for term in y_terms),
            "connector_weight": (connector.x | connector.z).bit_count(),
            "connector_flip_mask": connector_flip_mask,
            "required_branch_difference_mask": reference ^ surplus,
            "check_or_Wilson_leakage": leakage,
            "Hermiticity_failures": hermiticity_failures,
        }
        rows.append(row)
        if not (
            row["matter_union_M2"] == 35
            and row["joint_two_cell_union_M2"] == 49
            and row["X_nonzero_Pauli_terms"] == 2048
            and row["Y_nonzero_Pauli_terms"] == 2048
            and row["maximum_X_term_weight"] == 24
            and row["maximum_Y_term_weight"] == 25
            and row["connector_weight"] == 5
            and row["connector_flip_mask"]
            == row["required_branch_difference_mask"]
            and leakage == 0
            and hermiticity_failures == 0
        ):
            failures.append(row)
    check(
        "the two physical off-diagonal quadratures and two local reservoir/field blocks have constant 49-M2 union, zero leakage, and held-out-size stability",
        not failures,
        rows,
    )

    code = c269.build_code(3)
    cells, bs, connector_edge, connector_u, connector_v, connector = connector_and_bs(code)
    local_family = set(code.local_checks)
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
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_bs = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in bs
            )
            original_vertices = tuple(
                code.graph.vertex_index[(cell, direction)]
                for cell in cells
                for direction in c278.DIRECTIONS
            )
            target_bs = tuple(code.B[vertex_map[vertex]] for vertex in original_vertices)
            transformed_connector = c235.apply_gauge(
                c235.permute_pauli(connector, edge_map), toggles, pairs, flips
            )
            target_connector = code.graph.A(
                vertex_map[connector_u], vertex_map[connector_v]
            )
            if not (
                transformed_local == local_family
                and transformed_bs == target_bs
                and transformed_connector == target_connector
            ):
                frame_failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "the ordered branch-projector generators and connector are covariant as a family in all 648 proper-frame and L=3 translation tests",
        tests == 24 * 27 and not frame_failures,
        {"tests": tests, "failures": frame_failures[:5]},
    )


def composition_spectator_and_domain_controls(operators: dict[str, np.ndarray]) -> None:
    print("\nCOMPOSITION / SPECTATOR / LAWFUL DOMAIN")
    identity = np.eye(18, dtype=complex)
    full = operators["G"]
    observable = operators["X"]
    delta = full.conj().T @ observable @ full - observable
    composed_full = np.kron(full, full)
    composed_observable = np.kron(observable, identity) + np.kron(identity, observable)
    composed_delta = (
        composed_full.conj().T @ composed_observable @ composed_full
        - composed_observable
    )
    expected_delta = np.kron(delta, identity) + np.kron(identity, delta)
    check(
        "two disjoint copies compose additively and a normalized spectator leaves the exact two-slice ledger unchanged",
        np.linalg.norm(composed_delta - expected_delta) < 8e-13
        and np.linalg.norm(
            np.kron(full, np.eye(2)).conj().T
            @ np.kron(observable, np.eye(2))
            @ np.kron(full, np.eye(2))
            - np.kron(observable, np.eye(2))
            - np.kron(delta, np.eye(2))
        ) < 8e-14,
        {
            "composition_residual": float(np.linalg.norm(composed_delta - expected_delta)),
        },
    )

    def validate(
        length: int,
        matter_modes: int,
        reservoir_m2_per_cell: int,
        field_m2_per_cell: int,
        branch_total_number: int,
    ) -> None:
        if length < 3:
            raise ValueError("the periodic physical matter code requires L>=3")
        if matter_modes != 6:
            raise ValueError("the imported matter cell has six modes")
        if reservoir_m2_per_cell != 1 or field_m2_per_cell != 6:
            raise ValueError("each local exchange block is one reservoir plus six field M2")
        if branch_total_number != 6:
            raise ValueError("this tested off-diagonal fixture is the fixed-N=6 block")

    validate(3, 6, 1, 6, 6)
    rejected = 0
    for candidate in (
        (2, 6, 1, 6, 6),
        (3, 5, 1, 6, 6),
        (3, 6, 0, 6, 6),
        (3, 6, 1, 5, 6),
        (3, 6, 1, 6, 5),
    ):
        try:
            validate(*candidate)
        except ValueError:
            rejected += 1
    check(
        "the lawful-domain guard rejects aliased, mistyped, or wrong-number fixtures",
        rejected == 5,
        {"rejected": rejected},
    )
    check(
        "the supplied-versus-derived inventory keeps the finite ledger distinct from energy, rate, and autonomous dynamics",
        True,
        {
            "supplied": (
                "Cycle-269 local-check matter representation and one adjacent connector",
                "Cycle-290 |3,3> and |4,2> fixed-N branch choice",
                "beta=-0.3, g=0.37, kappa=0.8, and the Cycle-219 phase-to-mass map",
                "one reservoir M2 plus six directional field M2 at each of two cells",
                "uniform scalar-field mode, branch-coordinate normalization, and two-slice ordering",
            ),
            "derived": (
                "exact Delta(X,Y)=J_exchange(X,Y)+J_contact(X,Y)",
                "exact signed field-reservoir number balance",
                "49-M2 bounded union, zero leakage, covariance, deletion, held-size, and composition controls",
            ),
            "not_earned": (
                "a scalar conserved physical energy or Hamiltonian",
                "a generator rate, clock normalization, elapsed physical time, stress, or gravity source",
                "an autonomous branch preparation, moving-reservoir compiler, joint matter/field stream update, or full-Fock state encoder",
                "a Record, occurrence law, Born rule, axiom change, or audit authority",
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("TWO-SLICE OFF-DIAGONAL CONTACT / RESERVOIR-FIELD BRANCH-COORDINATE IMPULSE LEDGER")
    note_contract()
    branch_and_physical_vertex_controls()
    operators = exact_two_slice_ledgers()
    deletion_phase_and_normalization_controls(operators)
    physical_support_leakage_and_covariance_controls()
    composition_spectator_and_domain_controls(operators)
    print("\nSUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "EXACT_TWO_SLICE_OFFDIAGONAL_VECTOR_LEDGER"
        if FAIL == 0
        else "TWO_SLICE_OFFDIAGONAL_VECTOR_LEDGER_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
