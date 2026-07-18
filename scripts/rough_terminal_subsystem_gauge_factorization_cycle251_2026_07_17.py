#!/usr/bin/env python3
"""Cycle 251: resolve the rough-terminal multiplicity as a local commutant.

The Cycle-247 rough code carries the exact mapped matter even-CAR algebra but
has N-1 excess logical qubits.  This runner computes its full Pauli
commutant, identifies a bounded auxiliary even-CAR_N generator family whose
total parity is locked to matter parity, and tests sectorwise factorization,
local selector attempts, covariance, held-out size, deletion, and the fixed
Cycle-230 free-plus-contact fixture.

The positive result is deliberately narrower than a bounded physical encoder:
the auxiliary algebra is locally generated and is a full matrix factor after
fixing total parity, but no bounded parity-sector identification or bounded
state-preparation circuit E is constructed.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import local_rough_puncture_odd_sector_cycle247_2026_07_17 as c247
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md"
)
MARKER_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_NOTE_2026-07-17.md"
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "auxiliary even-car",
        "parity-locked",
        "sectorwise factorization",
        "not a canonical onsite gauge",
        "bounded state-preparation circuit",
        "coarse-cell unit translations",
        "not homogeneous one-site translation",
        "period-16 physical role marker",
        "held-out l=6",
        "fixed free-plus-contact",
        "mass fixture",
        "contact and seam",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "time firewall",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves scope, supplies, N1-N8, and time firewall", not missing, missing)

    marker = normalized(MARKER_NOTE)
    marker_required = (
        "spacing-16 marker",
        "all 4096 translated marker sectors",
        "marker-sector initial/boundary/realized-state selection",
    )
    marker_missing = tuple(phrase for phrase in marker_required if phrase not in marker)
    check(
        "the inherited period-16 physical role marker remains an explicit supplied structure",
        not marker_missing,
        marker_missing,
    )


def rank(paulis: list[c235.Pauli], qubits: int) -> int:
    return c235.gf2_rank(row.symplectic(qubits) for row in paulis)


def gram_rank(paulis: list[c235.Pauli]) -> int:
    rows = []
    for left in paulis:
        row = 0
        for index, right in enumerate(paulis):
            if not left.commutes(right):
                row ^= 1 << index
        rows.append(row)
    return c235.gf2_rank(rows)


def product_paulis(paulis: list[c235.Pauli]) -> c235.Pauli:
    result = c235.Pauli()
    for pauli in paulis:
        result = result @ pauli
    return result


def gauge_z(graph: c247.PunctureGraph, cell: tuple[int, int, int]) -> c235.Pauli:
    """Auxiliary cell parity: product of the six puncture-spoke Z factors."""
    z = 0
    for direction in range(6):
        z ^= 1 << graph.spoke_lookup[(cell, direction)]
    return c235.Pauli(z=z)


def gauge_x_oriented(
    graph: c247.PunctureGraph, source: int, target: int
) -> c235.Pauli:
    """Auxiliary hop along an oriented coarse stream edge."""
    left_cell = graph.base.vertices[source][0]
    right_cell = graph.base.vertices[target][0]
    middle = graph.A(source, target) @ c235.Pauli(
        x=(1 << graph.terminal_lookup[(left_cell, 0)])
        ^ (1 << graph.terminal_lookup[(right_cell, 0)])
    )
    return (
        graph.A(graph.sink_index[left_cell], source)
        @ middle
        @ graph.A(target, graph.sink_index[right_cell])
    )


def gauge_x(graph: c247.PunctureGraph, base_edge: int) -> c235.Pauli:
    source, target, kind, _ = graph.base.edges[base_edge]
    if kind != "outer_square":
        raise ValueError((base_edge, kind))
    return gauge_x_oriented(graph, source, target)


def gauge_family(
    graph: c247.PunctureGraph,
) -> tuple[list[c235.Pauli], list[c235.Pauli], list[int]]:
    z_rows = [gauge_z(graph, cell) for cell in graph.cells]
    stream_edges = [
        edge
        for edge, row in enumerate(graph.base.edges)
        if row[2] == "outer_square"
    ]
    x_rows = [gauge_x(graph, edge) for edge in stream_edges]
    return z_rows, x_rows, stream_edges


def matter_family(graph: c247.PunctureGraph) -> list[c235.Pauli]:
    return [graph.B(vertex) for vertex in range(graph.matter_count)] + [
        graph.mapped_matter_A(edge) for edge in range(len(graph.base.edges))
    ]


def commutant_and_auxiliary_car_controls() -> None:
    print("\nFULL PAULI COMMUTANT / AUXILIARY EVEN-CAR")
    rows = []
    for length in (3, 4, 5, 6):
        graph = c247.PunctureGraph(length, terminals=1)
        n = length**3
        stabilizers = c247.code_rows(graph)
        matter = matter_family(graph)
        gauge_b, gauge_a, stream_edges = gauge_family(graph)
        gauge = gauge_b + gauge_a
        s_rank = rank(stabilizers, graph.qubits)
        sm_rank = rank(stabilizers + matter, graph.qubits)
        sg_rank = rank(stabilizers + gauge, graph.qubits)
        smg_rank = rank(stabilizers + matter + gauge, graph.qubits)
        matter_increment = sm_rank - s_rank
        gauge_increment = sg_rank - s_rank
        intersection = matter_increment + gauge_increment - (smg_rank - s_rank)
        centralizer_quotient = 2 * graph.qubits - sm_rank - s_rank

        stabilizer_leakage = sum(
            not generator.commutes(stabilizer)
            for generator in gauge
            for stabilizer in stabilizers
        )
        matter_leakage = sum(
            not generator.commutes(target)
            for generator in gauge
            for target in matter
        )
        squares = sum((generator @ generator) != c235.Pauli() for generator in gauge)

        endpoint_failures = edge_failures = 0
        for stream_index, base_edge in enumerate(stream_edges):
            source, target, _, _ = graph.base.edges[base_edge]
            endpoint_cells = {
                graph.base.vertices[source][0],
                graph.base.vertices[target][0],
            }
            for cell_index, cell in enumerate(graph.cells):
                actual = not gauge_a[stream_index].commutes(gauge_b[cell_index])
                endpoint_failures += actual != (cell in endpoint_cells)
            for other_index in range(stream_index + 1, len(stream_edges)):
                other_source, other_target, _, _ = graph.base.edges[
                    stream_edges[other_index]
                ]
                other_cells = {
                    graph.base.vertices[other_source][0],
                    graph.base.vertices[other_target][0],
                }
                expected = len(endpoint_cells & other_cells) == 1
                actual = not gauge_a[stream_index].commutes(gauge_a[other_index])
                edge_failures += actual != expected

        matter_parity = product_paulis(
            [graph.B(vertex) for vertex in range(graph.matter_count)]
        )
        gauge_parity = product_paulis(gauge_b)
        rows.append(
            {
                "L": length,
                "N": n,
                "stabilizer_rank": s_rank,
                "code_exponent": graph.qubits - s_rank,
                "matter_quotient_dimension": matter_increment,
                "matter_symplectic_rank": gram_rank(matter),
                "commutant_quotient_dimension": centralizer_quotient,
                "explicit_gauge_dimension": gauge_increment,
                "explicit_gauge_symplectic_rank": gram_rank(gauge),
                "matter_gauge_intersection": intersection,
                "P_g_equals_P_m": gauge_parity == matter_parity,
                "stabilizer_leakage": stabilizer_leakage,
                "matter_leakage": matter_leakage,
                "auxiliary_CAR_endpoint_failures": endpoint_failures,
                "auxiliary_CAR_edge_failures": edge_failures,
                "nonhermitian_generators": squares,
                "max_gauge_B_weight": max((row.x | row.z).bit_count() for row in gauge_b),
                "max_gauge_A_weight": max((row.x | row.z).bit_count() for row in gauge_a),
            }
        )

    check(
        "the bounded auxiliary generators obey exact even-CAR incidence and commute with the full mapped matter algebra",
        all(
            row["stabilizer_leakage"] == 0
            and row["matter_leakage"] == 0
            and row["auxiliary_CAR_endpoint_failures"] == 0
            and row["auxiliary_CAR_edge_failures"] == 0
            and row["nonhermitian_generators"] == 0
            and row["max_gauge_B_weight"] == 6
            and row["max_gauge_A_weight"] <= 18
            for row in rows
        ),
        rows,
    )
    check(
        "the explicit auxiliary even-CAR algebra exhausts the full Pauli commutant modulo stabilizers through held-out L=6",
        all(
            row["stabilizer_rank"] == 15 * row["N"] + 1
            and row["code_exponent"] == 7 * row["N"] - 1
            and row["matter_quotient_dimension"] == 12 * row["N"] - 1
            and row["matter_symplectic_rank"] == 12 * row["N"] - 2
            and row["commutant_quotient_dimension"]
            == row["explicit_gauge_dimension"]
            == 2 * row["N"] - 1
            and row["explicit_gauge_symplectic_rank"] == 2 * row["N"] - 2
            and row["matter_gauge_intersection"] == 1
            and row["P_g_equals_P_m"]
            for row in rows
        ),
        rows,
    )


def coarse_spanning_tree(graph: c247.PunctureGraph) -> tuple[tuple[int, int, int], list[int]]:
    adjacency = {cell: [] for cell in graph.cells}
    for edge, (source, target, kind, _) in enumerate(graph.base.edges):
        if kind != "outer_square":
            continue
        left = graph.base.vertices[source][0]
        right = graph.base.vertices[target][0]
        adjacency[left].append((right, edge))
        adjacency[right].append((left, edge))
    root = (0, 0, 0)
    seen = {root}
    queue = deque([root])
    edges = []
    while queue:
        cell = queue.popleft()
        for target, edge in adjacency[cell]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
                edges.append(edge)
    if len(seen) != len(graph.cells):
        raise RuntimeError("coarse graph disconnected")
    return root, edges


def symplectic_gram_schmidt(paulis: list[c235.Pauli]) -> list[c235.Pauli]:
    remaining = list(paulis)
    canonical = []
    while remaining:
        left = remaining.pop(0)
        partner = next(
            (index for index, right in enumerate(remaining) if not left.commutes(right)),
            None,
        )
        if partner is None:
            raise RuntimeError("degenerate input to symplectic Gram-Schmidt")
        right = remaining.pop(partner)
        repaired = []
        for row in remaining:
            if not row.commutes(right):
                row = row @ left
            if not row.commutes(left):
                row = row @ right
            repaired.append(row)
        canonical.extend((left, right))
        remaining = repaired
    return canonical


def sectorwise_factorization_controls() -> None:
    print("\nSECTORWISE FACTORIZATION / BOUNDED-ENCODER FIREWALL")
    rows = []
    for length in (3, 4, 5, 6):
        graph = c247.PunctureGraph(length, terminals=1)
        n = length**3
        stabilizers = c247.code_rows(graph)
        root, tree_edges = coarse_spanning_tree(graph)
        raw_factor = [gauge_z(graph, cell) for cell in graph.cells if cell != root] + [
            gauge_x(graph, edge) for edge in tree_edges
        ]
        canonical = symplectic_gram_schmidt(raw_factor)
        rows.append(
            {
                "L": length,
                "N": n,
                "raw_factor_count": len(raw_factor),
                "raw_factor_increment": rank(stabilizers + raw_factor, graph.qubits)
                - rank(stabilizers, graph.qubits),
                "raw_factor_gram_rank": gram_rank(raw_factor),
                "raw_max_weight": max((row.x | row.z).bit_count() for row in raw_factor),
                "canonical_max_weight": max(
                    (row.x | row.z).bit_count() for row in canonical
                ),
                "fixed_parity_code_exponent": graph.qubits
                - rank(stabilizers, graph.qubits)
                - 1,
                "matter_sector_plus_auxiliary_exponent": (6 * n - 1) + (n - 1),
            }
        )

    check(
        "after fixing shared parity, a root/tree choice gives the complete nondegenerate auxiliary matrix factor sectorwise",
        all(
            row["raw_factor_count"]
            == row["raw_factor_increment"]
            == row["raw_factor_gram_rank"]
            == 2 * row["N"] - 2
            and row["raw_max_weight"] <= 18
            and row["fixed_parity_code_exponent"]
            == row["matter_sector_plus_auxiliary_exponent"]
            == 7 * row["N"] - 2
            for row in rows
        ),
        rows,
    )
    check(
        "the tested root/tree canonicalization grows to extensive support and therefore does not furnish a bounded full-Fock tensor encoder",
        [row["canonical_max_weight"] for row in rows] == [162, 385, 750, 1296],
        rows,
    )


def selector_controls() -> None:
    print("\nLOCAL COMMUTING SELECTOR ATTEMPTS")
    rows = []
    for length in (3, 4, 5, 6):
        graph = c247.PunctureGraph(length, terminals=1)
        n = length**3
        stabilizers = c247.code_rows(graph)
        matter = matter_family(graph)
        root = (0, 0, 0)
        marked = [gauge_z(graph, cell) for cell in graph.cells if cell != root]
        equalities = []
        for cell in graph.cells:
            for axis in range(3):
                target = list(cell)
                target[axis] = (target[axis] + 1) % length
                equalities.append(gauge_z(graph, cell) @ gauge_z(graph, tuple(target)))
        matter_parity = product_paulis(
            [graph.B(vertex) for vertex in range(graph.matter_count)]
        )
        s_rank = rank(stabilizers, graph.qubits)
        marked_rank = rank(stabilizers + marked, graph.qubits)
        equality_rank = rank(stabilizers + equalities, graph.qubits)
        rows.append(
            {
                "L": length,
                "N": n,
                "marked_increment": marked_rank - s_rank,
                "marked_code_exponent": graph.qubits - marked_rank,
                "marked_matter_dimension": rank(stabilizers + marked + matter, graph.qubits)
                - marked_rank,
                "marked_parity_fixed": rank(
                    stabilizers + marked + [matter_parity], graph.qubits
                )
                == marked_rank,
                "marked_translation_covariant": False,
                "marked_rotation_covariant": True,
                "equality_increment": equality_rank - s_rank,
                "equality_code_exponent": graph.qubits - equality_rank,
                "equality_matter_dimension": rank(
                    stabilizers + equalities + matter, graph.qubits
                )
                - equality_rank,
                "equality_parity_fixed": rank(
                    stabilizers + equalities + [matter_parity], graph.qubits
                )
                == equality_rank,
                "equality_translation_covariant": True,
                "equality_rotation_covariant": True,
                "selector_leakage": sum(
                    not selector.commutes(generator)
                    for selector in marked + equalities
                    for generator in matter
                ),
            }
        )

    check(
        "a marked-root bounded selector rank-matches and keeps both parities but breaks coarse-cell translations",
        all(
            row["marked_increment"] == row["N"] - 1
            and row["marked_code_exponent"] == 6 * row["N"]
            and row["marked_matter_dimension"] == 12 * row["N"] - 1
            and not row["marked_parity_fixed"]
            and row["marked_rotation_covariant"]
            and not row["marked_translation_covariant"]
            and row["selector_leakage"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "covariant local parity equalities rank-match but have an exact even-volume parity defect",
        all(
            row["equality_increment"] == row["N"] - 1
            and row["equality_code_exponent"] == 6 * row["N"]
            and row["equality_translation_covariant"]
            and row["equality_rotation_covariant"]
            and row["equality_parity_fixed"] == (row["N"] % 2 == 0)
            and row["equality_matter_dimension"]
            == 12 * row["N"] - (2 if row["N"] % 2 == 0 else 1)
            for row in rows
        ),
        rows,
    )


def graph_translation_maps(
    graph: c247.PunctureGraph, displacement: tuple[int, int, int]
) -> tuple[list[int], list[int]]:
    vertex_map = []
    for vertex in range(graph.matter_count):
        cell, direction = graph.base.vertices[vertex]
        target_cell = tuple(
            (cell[axis] + displacement[axis]) % graph.length for axis in range(3)
        )
        vertex_map.append(graph.base.vertex_index[(target_cell, direction)])
    for cell in graph.cells:
        target_cell = tuple(
            (cell[axis] + displacement[axis]) % graph.length for axis in range(3)
        )
        vertex_map.append(graph.sink_index[target_cell])
    edge_map = []
    for row in graph.edges:
        if row.v is None:
            target_cell = tuple(
                (row.owner[axis] + displacement[axis]) % graph.length
                for axis in range(3)
            )
            edge_map.append(graph.terminal_lookup[(target_cell, row.label)])
        else:
            edge_map.append(graph.edge_between(vertex_map[row.u], vertex_map[row.v]))
    return vertex_map, edge_map


def equality_selectors(graph: c247.PunctureGraph) -> set[c235.Pauli]:
    rows = set()
    for cell in graph.cells:
        for axis in range(3):
            target = list(cell)
            target[axis] = (target[axis] + 1) % graph.length
            rows.add(gauge_z(graph, cell) @ gauge_z(graph, tuple(target)))
    return rows


def covariance_controls() -> None:
    print("\nPROPER-CUBIC / COARSE-TRANSLATION COVARIANCE")
    graph = c247.PunctureGraph(3, terminals=1)
    z_failures = x_failures = equality_frame_failures = marked_frame_failures = 0
    equality_family = equality_selectors(graph)
    marked_family = {
        gauge_z(graph, cell) for cell in graph.cells if cell != (0, 0, 0)
    }
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c247.graph_frame_maps(graph, frame)
        toggles, pairs = c247.order_gauge(graph, vertex_map, edge_map)
        flips = 0
        for source_edge, row in enumerate(graph.edges):
            if row.v is None:
                continue
            transformed = c247.permute_pauli(graph.A(row.u, row.v), edge_map)
            target = graph.A(vertex_map[row.u], vertex_map[row.v])
            ordered = c235.apply_gauge(transformed, toggles, pairs)
            if ordered.x != target.x or ordered.z != target.z:
                x_failures += 1
            elif (ordered.phase - target.phase) % 4 == 2:
                flips ^= 1 << edge_map[source_edge]

        for cell in graph.cells:
            target_cell = tuple(
                int(value % graph.length) for value in frame @ np.asarray(cell)
            )
            transformed = c235.apply_gauge(
                c247.permute_pauli(gauge_z(graph, cell), edge_map),
                toggles,
                pairs,
                flips,
            )
            z_failures += transformed != gauge_z(graph, target_cell)

        for source, target, kind, _ in graph.base.edges:
            if kind != "outer_square":
                continue
            transformed = c235.apply_gauge(
                c247.permute_pauli(gauge_x_oriented(graph, source, target), edge_map),
                toggles,
                pairs,
                flips,
            )
            expected = gauge_x_oriented(graph, vertex_map[source], vertex_map[target])
            x_failures += transformed != expected

        transformed_equalities = {
            c235.apply_gauge(
                c247.permute_pauli(row, edge_map), toggles, pairs, flips
            )
            for row in equality_family
        }
        equality_frame_failures += transformed_equalities != equality_family
        transformed_marked = {
            c235.apply_gauge(
                c247.permute_pauli(row, edge_map), toggles, pairs, flips
            )
            for row in marked_family
        }
        marked_frame_failures += transformed_marked != marked_family

    translation_failures = equality_translation_failures = 0
    marked_translation_preserved = 0
    for axis in range(3):
        displacement = tuple(1 if index == axis else 0 for index in range(3))
        vertex_map, edge_map = graph_translation_maps(graph, displacement)
        toggles, pairs = c247.order_gauge(graph, vertex_map, edge_map)
        flips = 0
        for source_edge, row in enumerate(graph.edges):
            if row.v is None:
                continue
            transformed = c247.permute_pauli(graph.A(row.u, row.v), edge_map)
            target = graph.A(vertex_map[row.u], vertex_map[row.v])
            ordered = c235.apply_gauge(transformed, toggles, pairs)
            if ordered.x != target.x or ordered.z != target.z:
                translation_failures += 1
            elif (ordered.phase - target.phase) % 4 == 2:
                flips ^= 1 << edge_map[source_edge]
        for cell in graph.cells:
            target_cell = tuple(
                (cell[index] + displacement[index]) % graph.length
                for index in range(3)
            )
            translation_failures += c235.apply_gauge(
                c247.permute_pauli(gauge_z(graph, cell), edge_map),
                toggles,
                pairs,
                flips,
            ) != gauge_z(graph, target_cell)
        for source, target, kind, _ in graph.base.edges:
            if kind == "outer_square":
                translation_failures += c235.apply_gauge(
                    c247.permute_pauli(
                        gauge_x_oriented(graph, source, target), edge_map
                    ),
                    toggles,
                    pairs,
                    flips,
                ) != gauge_x_oriented(graph, vertex_map[source], vertex_map[target])
        transformed_equalities = {
            c235.apply_gauge(
                c247.permute_pauli(row, edge_map), toggles, pairs, flips
            )
            for row in equality_family
        }
        equality_translation_failures += transformed_equalities != equality_family
        transformed_marked = {
            c235.apply_gauge(
                c247.permute_pauli(row, edge_map), toggles, pairs, flips
            )
            for row in marked_family
        }
        marked_translation_preserved += transformed_marked == marked_family

    check(
        "the complete local auxiliary even-CAR family is covariant under all 24 frames and coarse-cell unit translations",
        len(c235.proper_cubic_frames()) == 24
        and z_failures == x_failures == translation_failures == 0
        and equality_frame_failures == equality_translation_failures == 0
        and marked_frame_failures == marked_translation_preserved == 0,
        {
            "frames": len(c235.proper_cubic_frames()),
            "gauge_B_failures": z_failures,
            "gauge_A_failures": x_failures,
            "translation_family_failures": translation_failures,
            "equality_frame_failures": equality_frame_failures,
            "equality_translation_failures": equality_translation_failures,
            "marked_frame_failures": marked_frame_failures,
            "marked_nonzero_translations_preserved": marked_translation_preserved,
            "translation_scope": "supplied puncture macro-cell roles",
            "homogeneous_one_site_M2_translation": False,
        },
    )


def fixed_update_and_fixture_controls() -> None:
    print("\nFIXED FREE-PLUS-CONTACT UPDATE / FIXTURES")
    species = c219.common_species(c230.BETA)
    one_particle, onsite_coin, stream, _, _ = c230.spatial_layers(3, species.coin)
    local_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
    )
    _, modes, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))

    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = float(1 / np.mean(np.diag(curvature)))
    forced = c210.force_response(species, 2e-5)

    minus_root = 1.5783929737448452
    seam_length = 416
    lower_index = int(np.floor(minus_root * seam_length / (2 * np.pi)))
    lower = 2 * np.pi * lower_index / seam_length
    upper = 2 * np.pi * (lower_index + 1) / seam_length
    seam, phase_cost, _ = c230.seam_block(lower, upper, -1)
    singulars = np.linalg.svd(seam, compute_uv=False)

    rng = np.random.default_rng(251)
    state = rng.normal(size=seam.shape[1]) + 1j * rng.normal(size=seam.shape[1])
    state /= np.linalg.norm(state)
    spectator = rng.normal(size=2) + 1j * rng.normal(size=2)
    spectator /= np.linalg.norm(spectator)
    spectator_residual = np.linalg.norm(
        np.kron(seam, np.eye(2)) @ np.kron(state, spectator)
        - np.kron(seam @ state, spectator)
    )

    graph = c247.PunctureGraph(3, terminals=1)
    gauge = list(gauge_family(graph)[0] + gauge_family(graph)[1])
    matter = matter_family(graph)
    gauge_update_commutators = sum(
        not auxiliary.commutes(generator)
        for auxiliary in gauge
        for generator in matter
    )

    check(
        "one fixed onsite-coin then stream then onsite-contact word remains unitary, even, and identity on the one-particle contact sector",
        np.linalg.norm(one_particle.conj().T @ one_particle - np.eye(162)) < 2e-14
        and np.linalg.norm(onsite_coin.conj().T @ onsite_coin - np.eye(162)) < 2e-14
        and np.linalg.norm(stream.conj().T @ stream - np.eye(162)) < 2e-14
        and np.linalg.norm(local_coin.conj().T @ local_coin - np.eye(64)) < 2e-14
        and np.linalg.norm(contact.conj().T @ contact - np.eye(64)) < 2e-14
        and np.max(np.abs(np.diag(contact)[number <= 1] - 1)) < 2e-15,
        {"beta": c230.BETA, "contact_coupling": c230.COUPLING},
    )
    check(
        "the local matter word commutes with the complete auxiliary algebra, so the fixed even update is spectator-independent sectorwise",
        gauge_update_commutators == 0 and spectator_residual < 2e-15,
        {
            "generator_commutator_failures": gauge_update_commutators,
            "explicit_spectator_residual": spectator_residual,
            "scope": "sectorwise algebraic intertwining, not bounded preparation E",
        },
    )
    check(
        "the one-particle mass fixture, L=3 sea rank, and Cycle-230 seam block are reproduced",
        abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(forced.measured_mass / species.analytic_mass - 1) < 0.007
        and sea_rank == 73
        and np.linalg.norm(modes.conj().T @ modes - np.eye(162)) < 2e-13
        and abs(float(np.angle(np.exp(1j * phase_cost)))) < 0.005
        and np.linalg.norm(
            singulars - np.asarray([1.0, 0.99988849, 0.99988849, 0.99988849])
        )
        < 2e-8,
        {
            "analytic_mass": species.analytic_mass,
            "rest_mass": c219.rest_mass(species),
            "dispersion_mass": dispersion_mass,
            "forced_mass": forced.measured_mass,
            "sea_rank": sea_rank,
            "seam_wrapped_phase": float(np.angle(np.exp(1j * phase_cost))),
            "seam_singulars": singulars,
        },
    )


def deletion_controls() -> None:
    print("\nDELETION / LAWFUL-DOMAIN CONTROLS")
    graph = c247.PunctureGraph(3, terminals=1)
    stabilizers = c247.code_rows(graph)
    root, tree_edges = coarse_spanning_tree(graph)
    factor = [gauge_z(graph, cell) for cell in graph.cells if cell != root] + [
        gauge_x(graph, edge) for edge in tree_edges
    ]
    full_increment = rank(stabilizers + factor, graph.qubits) - rank(
        stabilizers, graph.qubits
    )
    deleted_increment = rank(stabilizers + factor[1:], graph.qubits) - rank(
        stabilizers, graph.qubits
    )

    stream_edge = next(
        edge for edge, row in enumerate(graph.base.edges) if row[2] == "outer_square"
    )
    source, target, _, _ = graph.base.edges[stream_edge]
    bare = graph.A(source, target)
    constraints = [graph.cell_constraint(cell) for cell in graph.cells]
    bare_leakage = sum(not bare.commutes(row) for row in constraints)
    dressed_leakage = sum(
        not graph.mapped_matter_A(stream_edge).commutes(row) for row in constraints
    )

    full_rank = rank(stabilizers, graph.qubits)
    deleted_constraint_rank = rank(stabilizers[:-1], graph.qubits)
    check(
        "deleting one independent auxiliary factor generator loses one quotient direction",
        full_increment == 52 and deleted_increment == 51,
        {"full_increment": full_increment, "deleted_increment": deleted_increment},
    )
    check(
        "rough dressing deletion gives exactly two local constraint violations while the full stream has zero leakage",
        bare_leakage == 2 and dressed_leakage == 0,
        {"bare_stream_leakage": bare_leakage, "dressed_stream_leakage": dressed_leakage},
    )
    check(
        "deleting one independent local code constraint adds exactly one physical logical direction",
        deleted_constraint_rank == full_rank - 1,
        {"full_rank": full_rank, "deleted_rank": deleted_constraint_rank},
    )


def main() -> int:
    note_contract()
    commutant_and_auxiliary_car_controls()
    sectorwise_factorization_controls()
    selector_controls()
    covariance_controls()
    fixed_update_and_fixture_controls()
    deletion_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
