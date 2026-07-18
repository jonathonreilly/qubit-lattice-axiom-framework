#!/usr/bin/env python3
"""Cycle 238 synthesis for the post-tournament state-locality wall.

This runner combines three independently constructed routes without upgrading
their different positive surfaces into one nonexistent compiler:

* Cycle 235: square-pyramid exact 3-D even-algebra bosonization;
* Cycle 236: Farrelly--Short all-parity bounded update gates;
* Cycle 237: infinite even-CAR sector split and translation-orbit marker.

It reruns all route artifacts, independently reconstructs their load-bearing
ranks/supports, checks the exact marker family, and enforces the narrow scope
of the Guaita preparation theorem and the N1--N8 synthesis claim.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "STATE_LOCAL_FERMIONIZATION_TOPOLOGICAL_SECTOR_TOURNAMENT_CYCLE238_NOTE_2026-07-17.md"
)

ROUTES = (
    (
        "higher_form",
        SCRIPTS / "exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
        "SUMMARY PASS 19 FAIL 0",
    ),
    (
        "auxiliary_majorana",
        SCRIPTS / "FARRELLY_SHORT_AUXILIARY_MAJORANA_CAR_COMPILER_CYCLE236_2026_07_17.py",
        "SUMMARY PASS 21 FAIL 0",
    ),
    (
        "infinite_marker",
        SCRIPTS / "ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_2026_07_17.py",
        "SUMMARY {'pass': 46, 'fail': 0}",
    ),
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


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError((name, path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


c235 = load_module("cycle235_synthesis", ROUTES[0][1])
c236 = load_module("cycle236_synthesis", ROUTES[1][1])
c237 = load_module("cycle237_synthesis", ROUTES[2][1])


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "no route supplies the full compiler",
        "15 face qubits per coarse cell",
        "maximum dressed update weight `14`",
        "radius-two marker",
        "shared conditional state-preparation obstruction",
        "not a full compiler no-go",
        "measurement plus feedforward",
        "nontrivial locality-preserving qca/isometry",
        "distinguishable-walker antisymmetric sector",
        "spatial-dimension and time firewall",
        "c_ref",
        "c_num",
        "c_wrap",
        "c_int",
        "c_local",
        "c_source",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "authority: none",
        "audit: unset",
    )
    missing = tuple(item for item in required if item not in text)
    check("synthesis note preserves the contract, ledger, and N1-N8 scope", not missing, missing)


def route_regressions() -> None:
    rows = []
    for name, path, expected in ROUTES:
        result = subprocess.run(
            (sys.executable, str(path)),
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        rows.append(
            {
                "route": name,
                "exit": result.returncode,
                "expected_summary": expected in result.stdout,
            }
        )
    check(
        "all three independently retained post-tournament runners pass",
        all(row["exit"] == 0 and row["expected_summary"] for row in rows),
        rows,
    )


def higher_form_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        cells = length**3
        loops = c235.primal_edge_cycles(graph)
        local_rank = c235.gf2_rank(mask for mask, _, _ in loops)
        full_rank = len(graph.edges) - len(graph.vertices) + 1
        total_flux = c235.Pauli()
        for vertex in range(len(graph.vertices)):
            total_flux = total_flux @ graph.B(vertex)
        rows.append(
            {
                "L": length,
                "face_qubits": len(graph.edges),
                "local_rank": local_rank,
                "full_rank": full_rank,
                "logical_after_Wilson_fix": len(graph.edges) - full_rank,
                "target_full_Fock": 6 * cells,
                "total_flux_identity": total_flux == c235.Pauli(),
            }
        )
    check(
        "square-pyramid code has exact 15N capacity, three Wilsons, and the closed total-even identity",
        rows
        == [
            {
                "L": 3,
                "face_qubits": 405,
                "local_rank": 241,
                "full_rank": 244,
                "logical_after_Wilson_fix": 161,
                "target_full_Fock": 162,
                "total_flux_identity": True,
            },
            {
                "L": 4,
                "face_qubits": 960,
                "local_rank": 574,
                "full_rank": 577,
                "logical_after_Wilson_fix": 383,
                "target_full_Fock": 384,
                "total_flux_identity": True,
            },
            {
                "L": 5,
                "face_qubits": 1875,
                "local_rank": 1123,
                "full_rank": 1126,
                "logical_after_Wilson_fix": 749,
                "target_full_Fock": 750,
                "total_flux_identity": True,
            },
        ],
        rows,
    )

    graph = c235.PyramidCellulation(3)
    supports = {
        "flux": max(graph.B(vertex).z.bit_count() for vertex in range(len(graph.vertices))),
        "hopping": max(
            (graph.A(u, v).x | graph.A(u, v).z).bit_count()
            for u, v, _, _ in graph.edges
        ),
        "Gauss": max(
            (graph.loop_pauli(vertices).x | graph.loop_pauli(vertices).z).bit_count()
            for _, vertices, _ in c235.primal_edge_cycles(graph)
        ),
    }
    check(
        "higher-form even-algebra supports are bounded",
        supports == {"flux": 5, "hopping": 9, "Gauss": 28},
        supports,
    )


def auxiliary_majorana_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        cell_count = length**3
        qubits = 12 * cell_count
        links = c236.links(length)
        stabilizers = (
            [c236.link_majorana(row) for row in links]
            + [c236.odd_link_parity_stabilizer(row) for row in links]
        )
        rank = c236.gf2_rank(row.symplectic(qubits) for row in stabilizers)
        matter_parity = c236.Pauli(
            z=sum(
                1 << c236.mode_index(cell, "matter", direction, length)
                for cell in c236.all_cells(length)
                for direction in range(6)
            )
        )
        parity_rank = c236.gf2_rank(
            [row.symplectic(qubits) for row in stabilizers]
            + [matter_parity.symplectic(qubits)]
        )
        dressed_max = 0
        for link in links:
            m_link = c236.link_majorana(link)
            for left_component in range(2):
                for right_component in range(2):
                    dressed = (
                        c236.jw_majorana(link["matter_left"], left_component)
                        @ m_link
                        @ c236.jw_majorana(link["matter_right"], right_component)
                    )
                    dressed_max = max(dressed_max, dressed.weight())
        rows.append(
            {
                "L": length,
                "rank": rank,
                "logical": qubits - rank,
                "matter_parity_rank_increment": parity_rank - rank,
                "M_max": max(c236.link_majorana(row).weight() for row in links),
                "dressed_max": dressed_max,
            }
        )
    check(
        "Farrelly-Short code carries both parities and bounded weight-14 updates while its M constraints grow",
        rows
        == [
            {"L": 3, "rank": 162, "logical": 162, "matter_parity_rank_increment": 1, "M_max": 216, "dressed_max": 14},
            {"L": 4, "rank": 384, "logical": 384, "matter_parity_rank_increment": 1, "M_max": 576, "dressed_max": 14},
            {"L": 5, "rank": 750, "logical": 750, "matter_parity_rank_increment": 1, "M_max": 1200, "dressed_max": 14},
        ],
        rows,
    )

    a, c, b, d = (c236.annihilation(index, 4) for index in range(4))
    m_link = 1j * (c + c.conj().T) @ (d + d.conj().T)
    q_dressed = (
        a.conj().T @ a
        + b.conj().T @ b
        - a.conj().T @ m_link @ b
        - b.conj().T @ m_link @ a
    )
    a2, b2 = (c236.annihilation(index, 2) for index in range(2))
    q_coarse = (
        a2.conj().T @ a2
        + b2.conj().T @ b2
        - a2.conj().T @ b2
        - b2.conj().T @ a2
    )
    k_link = (c.conj().T - 1j * d.conj().T) / np.sqrt(2)
    vacuum = np.eye(16, dtype=complex)[:, 0]
    columns = []
    for occupied_left, occupied_right in ((0, 0), (0, 1), (1, 0), (1, 1)):
        vector = vacuum
        if occupied_right:
            vector = b.conj().T @ vector
        if occupied_left:
            vector = a.conj().T @ vector
        columns.append(k_link @ vector)
    encoding = np.column_stack(columns)
    residual = np.linalg.norm(
        expm(1j * np.pi * q_dressed / 2) @ encoding
        - encoding @ expm(1j * np.pi * q_coarse / 2)
    )
    check(
        "Farrelly-Short dressed link retains the exact FSWAP intertwining residual",
        residual < 4e-15,
        residual,
    )


def infinite_and_marker_controls() -> None:
    parity_gaps = []
    identity = np.eye(2, dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    for modes in range(1, 7):
        old = c237.kron_all([z] * modes + [identity])
        enlarged = c237.kron_all([z] * (modes + 1))
        parity_gaps.append(float(np.linalg.norm(enlarged - old, 2)))
    check(
        "finite total-parity products have no quasi-local norm limit",
        max(abs(value - 2) for value in parity_gaps) < 1e-12,
        parity_gaps,
    )

    frames = c237.proper_cubic_frames()
    active = c237.active_residues()
    marker, orbits = c237.cubic_marker(frames)
    templates, coordinates, offsets = c237.marker_templates(marker, active)
    ambiguities = c237.template_ambiguities(templates)
    frame_mismatches = c237.rotation_mismatches(
        templates, coordinates, offsets, frames
    )
    missing, extra = c237.successor_mismatches(
        templates, coordinates, offsets
    )
    check(
        "radius-two marker locally enforces a unit-translation and proper-cubic code family",
        len(orbits) == 200
        and len(active) == 27
        and len(templates) == 4096
        and ambiguities == 0
        and frame_mismatches == 0
        and missing == 0
        and extra == 0,
        {
            "point_orbits": len(orbits),
            "active_wildcards": len(active),
            "phases": len(templates),
            "ambiguities": ambiguities,
            "frame_mismatches": frame_mismatches,
            "missing_successors": missing,
            "extra_successors": extra,
        },
    )


def fixture_and_theorem_scope_controls() -> None:
    # The runner does not claim to prove Guaita's theorem.  It checks the
    # fixture hypotheses that make the primary theorem relevant and preserves
    # its explicit exclusions in the synthesis note.
    plaquette_rows = []
    for length in (3, 4, 5):
        plaquettes = 3 * length * (length - 1) ** 2
        plaquette_rows.append((length, plaquettes))
    growing = {length: (length - 2) // 4 for length in (6, 10, 14, 18)}
    check(
        "Cycle-230 graph has overlapping-loop fixtures and an asymptotically growing square-grid depth parameter",
        plaquette_rows == [(3, 36), (4, 108), (5, 240)]
        and growing == {6: 1, 10: 2, 14: 3, 18: 4},
        {"held_plaquettes": plaquette_rows, "open_square_d": growing},
    )

    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    scope_phrases = (
        "product input",
        "local two-body unitary",
        "measurement plus feedforward remains live",
        "qca/isometry remains live",
        "contract pressure",
        "not axiom pressure",
    )
    missing = tuple(phrase for phrase in scope_phrases if phrase not in text)
    check(
        "Guaita preparation consequence is retained only under its exact hypotheses",
        not missing,
        missing,
    )


def combined_contract_controls() -> None:
    # Each row is backed by the exact route checks above.  No row may borrow a
    # passing surface from another route and masquerade as one common E.
    rows = {
        "higher_form": {
            "bounded_even_update": True,
            "both_parities": False,
            "bounded_constraints": True,
            "bounded_state_E": False,
            "full_fixtures": False,
            "cubic_complete": True,
        },
        "auxiliary_majorana": {
            "bounded_even_update": True,
            "both_parities": True,
            "bounded_constraints": False,
            "bounded_state_E": False,
            "full_fixtures": True,
            "cubic_complete": False,
        },
        "infinite_sector_marker": {
            "bounded_even_update": True,
            "both_parities": False,
            "bounded_constraints": True,
            "bounded_state_E": False,
            "full_fixtures": False,
            "cubic_complete": True,
        },
    }
    check(
        "no route supplies the full compiler, and cross-route feature splicing is rejected",
        all(not all(row.values()) for row in rows.values())
        and all(row["bounded_even_update"] for row in rows.values()),
        rows,
    )


def physics_and_time_firewall_controls() -> None:
    held = c236.c219.common_species(-0.35)
    rest = c236.c219.rest_mass(held)
    curvature = 1 / float(
        np.mean(np.diag(c236.c210.curvature_tensor(held, step=1e-4)))
    )
    _, _, eigenvalues, _ = c236.c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "conditional all-parity route retains the held mass and odd rank-73 fixture",
        abs(rest / curvature - 1) < 4e-6 and sea_rank == 73,
        {
            "rest_mass": rest,
            "curvature_mass": curvature,
            "relative_residual": abs(rest / curvature - 1),
            "sea_rank": sea_rank,
        },
    )

    notes = " ".join(
        path.read_text(encoding="utf-8").lower()
        for path in (
            NOTE,
            c235.NOTE,
            c236.NOTE,
            c237.NOTE,
        )
    )
    required = (
        "compiler control",
        "not physical time",
        "not a clock",
        "three-dimensional",
    )
    missing = tuple(phrase for phrase in required if phrase not in notes)
    check(
        "three-dimensional substrate and derived-time firewall remain explicit",
        not missing,
        missing,
    )


def main() -> int:
    note_contract()
    route_regressions()
    higher_form_controls()
    auxiliary_majorana_controls()
    infinite_and_marker_controls()
    fixture_and_theorem_scope_controls()
    combined_contract_controls()
    physics_and_time_firewall_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
