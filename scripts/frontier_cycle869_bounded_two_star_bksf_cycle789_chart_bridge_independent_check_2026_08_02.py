#!/usr/bin/env python3
"""Independent structural reconstruction of the Cycle869 bounded bridge.

This verifier does not import or execute the Cycle869 primary runner and does
not read a primary receipt.  It independently rebuilds the literal route and
resource census, signed seam equality, two-star cleanup/ranks/shared addresses,
primary/held Gram discriminator, landed edge-gauge boundary, and 24/576 signed
transport diagrams from the pinned landed modules.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle708_physical_endpoint_cube_core_2026_07_26 as G
import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as EG
import frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27 as R


AUDIT_TIMEOUT_SEC = 900
PRIMARY_RUNNER = (
    "scripts/frontier_cycle869_bounded_two_star_bksf_cycle789_"
    "chart_bridge_2026_08_02.py"
)
TARGET_SPEC = (
    "docs/work_history/repo/review_feedback/BOUNDED_TWO_STAR_BKSF_"
    "CYCLE789_TARGET_CHART_BRIDGE_"
    "CYCLE869_TARGET_SPEC_2026-08-02.md"
)
TARGET_SHA256 = "2220b3f4a35fa1ad80a9069c0c2436bd7418fc5c9896b0bc62974340fa0b05e9"
PACKAGE_BASE_COMMIT = "1900b64260f39f075c59f2e353079c44e8ede031"
EXPECTED_PRIMARY_RUNNER_SHA256 = (
    "61425733dddbfda2ff056639d47bc77a9608b9994382282689bbcc79104c0a2a"
)
EXPECTED_LOADED_HELPER_COUNT = 45
EXPECTED_LOADED_HELPER_CLOSURE_SHA256 = (
    "41bb2d352bea3d43677b574fbf6cc111800590a344366ec4a60e1e708d233530"
)
PINNED_DIRECT_IMPORTS = {
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py":
        "102f8bc31e60fd4a452a1cfab176129f922665e10b564f0421dc26ffb11ee152",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py":
        "3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py":
        "5d49d85ddbc4daddfc0b24737dc569eaa9f32a050f5fccf48f048fe0fdd74b40",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py":
        "d74fb32e21879b2a843eae822c8e71b950729d9dc295eaf336911f174cceee3a",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py":
        "f2fc664a1d14a2d62562ff58395840a0174d4cc75239ef2c1589c6e0f65ed982",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py":
        "6a309f6449d155244b1dbee581cbe169937db5fe815c4dcc3e93929274a79004",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py":
        "dee1557eca4b88af75c469413290801577415cdf4ebfa3d970ceaa5ea15a2a8b",
}
AUDIT_INPUT_PATHS = (PRIMARY_RUNNER, TARGET_SPEC, *tuple(PINNED_DIRECT_IMPORTS))
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


def digest(path: Path) -> str:
    value = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def loaded_helper_closure() -> dict[str, object]:
    """Pin every repo-local Python helper loaded by this verifier."""

    runner = Path(__file__).resolve()
    rows: dict[str, str] = {}
    for module in tuple(sys.modules.values()):
        raw = getattr(module, "__file__", None)
        if not raw:
            continue
        try:
            path = Path(raw).resolve()
            relative = path.relative_to(ROOT)
        except (OSError, ValueError):
            continue
        if (
            relative.parts
            and relative.parts[0] == "scripts"
            and path.suffix == ".py"
            and path != runner
        ):
            rows[relative.as_posix()] = digest(path)
    ordered = tuple(sorted(rows.items()))
    observed = sha256(json.dumps(
        ordered, separators=(",", ":")
    ).encode()).hexdigest()
    return {
        "expected_loaded_helper_count": EXPECTED_LOADED_HELPER_COUNT,
        "loaded_helper_count": len(ordered),
        "expected_closure_sha256": EXPECTED_LOADED_HELPER_CLOSURE_SHA256,
        "observed_closure_sha256": observed,
        "runner_path_excluded": str(runner.relative_to(ROOT)),
        "inventory": tuple(
            {"path": path, "sha256": digest_value}
            for path, digest_value in ordered
        ),
        "match": (
            len(ordered) == EXPECTED_LOADED_HELPER_COUNT
            and observed == EXPECTED_LOADED_HELPER_CLOSURE_SHA256
        ),
    }


def package_base_commit_certificate() -> dict[str, object]:
    metadata = subprocess.run(
        ("git", "-C", str(ROOT), "rev-parse", "--git-dir"),
        check=False,
        capture_output=True,
        text=True,
    ).returncode == 0
    exists = False
    if metadata:
        exists = subprocess.run(
            (
                "git", "-C", str(ROOT), "cat-file", "-e",
                f"{PACKAGE_BASE_COMMIT}^{{commit}}",
            ),
            check=False,
            capture_output=True,
            text=True,
        ).returncode == 0
    return {
        "named_package_base_commit": PACKAGE_BASE_COMMIT,
        "repository_has_git_metadata": metadata,
        "commit_object_exists": exists if metadata else None,
        "pass": not metadata or exists,
    }


def anti(left, right) -> int:
    return ((left.x & right.z).bit_count() + (left.z & right.x).bit_count()) & 1


def rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def controlled_matrix(letter: str):
    identity = np.eye(2, dtype=complex)
    target = {
        "X": P.c707.c655.X,
        "Y": np.asarray(((0, -1j), (1j, 0)), dtype=complex),
        "Z": np.diag((1, -1)).astype(complex),
    }[letter]
    p0 = np.diag((1, 0)).astype(complex)
    p1 = np.diag((0, 1)).astype(complex)
    return np.kron(identity, p0) + np.kron(target, p1)


def character_word(row, sites, ancilla):
    axes, sign = P.c707.pauli_axes(row, sites)
    word = [P.c707.Instruction("verify_H", (ancilla,), P.c707.c655.H)]
    if sign == -1:
        word.append(P.c707.Instruction(
            "verify_sign_Z", (ancilla,), np.diag((1, -1)).astype(complex)
        ))
    word.extend(
        P.c707.Instruction(
            f"verify_CP_{axis}", (ancilla, site), controlled_matrix(axis)
        )
        for site, axis in axes
    )
    word.append(P.c707.Instruction("verify_H", (ancilla,), P.c707.c655.H))
    return tuple(word)


def inverse_word(word):
    return tuple(
        P.c707.Instruction(
            "verify_inverse_" + row.kind,
            row.sites,
            row.matrix.conj().T,
        )
        for row in reversed(word)
    )


def replay_returned_route(word, routed) -> dict[str, int]:
    """Independently replay physical route swaps and logical operands."""

    touched = {site for gate in routed for site in gate.sites}
    labels = {site: site for site in touched}
    expected_index = 0
    swap_gates = nn_failures = operand_failures = 0
    kind_failures = matrix_failures = swap_matrix_failures = 0
    for gate in routed:
        if len(gate.sites) == 2:
            left, right = gate.sites
            nn_failures += sum(
                abs(a - b) for a, b in zip(left, right)
            ) != 1
        if gate.kind == "route_swap":
            left, right = gate.sites
            labels[left], labels[right] = labels[right], labels[left]
            swap_gates += 1
            swap_matrix_failures += int(np.linalg.norm(
                gate.matrix - P.c707.c655.SWAP
            ) > 1.0e-12)
            continue
        expected = word[expected_index]
        expected_index += 1
        operand_failures += tuple(
            labels[site] for site in gate.sites
        ) != expected.sites
        kind_failures += gate.kind != expected.kind
        matrix_failures += int(np.linalg.norm(
            gate.matrix - expected.matrix
        ) > 1.0e-12)
    return {
        "replayed_route_swap_gates": swap_gates,
        "replayed_non_swap_gates": expected_index,
        "replayed_NN_failures": nn_failures,
        "replayed_operand_failures": operand_failures,
        "replayed_kind_failures": kind_failures,
        "replayed_matrix_failures": matrix_failures,
        "replayed_swap_matrix_failures": swap_matrix_failures,
        "replayed_label_return_failures": sum(
            site != label for site, label in labels.items()
        ),
    }


def literal_reconstruction() -> dict[str, object]:
    cells = ((0, 0, 0), (1, 0, 0))
    eq, graph, site_map, gauges, sites, collisions = P.placement_bundle(cells)
    source_open = R.source_fswap_terms(eq, (0, 0, 0), 0)[2]
    source = C.natural(eq, source_open)
    bounded = eq.forward(source_open)
    factors = C.seam_factors(eq, (0, 0, 0), 0)
    physical_factors = tuple(
        P.physical_lift(row, eq, graph, site_map, gauges)[0]
        for row in factors
    )
    _local, _support, e_word = P.compile_factor_rows(
        physical_factors, C.ROTATION_SIGNS, sites
    )
    source_physical = P.physical_lift(
        source, eq, graph, site_map, gauges
    )[0]
    midpoint = next(iter(gauges.values()))
    ancilla = (midpoint[0], midpoint[1], midpoint[2] + 1)
    character = character_word(source_physical, sites, ancilla)
    word = inverse_word(e_word) + character + e_word
    routed, route = P.c707.route_word(word)
    replay = replay_returned_route(word, routed)
    expected_route_swaps = sum(
        2 * max(0, sum(
            abs(a - b) for a, b in zip(*instruction.sites)
        ) - 1)
        for instruction in word if len(instruction.sites) == 2
    )
    touched = set(route["touched_coordinates"])
    declared = set(sites) | {ancilla}
    return {
        "abstract_exact": C.apply_images(
            C.seam_images(eq, (0, 0, 0), 0), source, eq.qubits
        ) == bounded,
        "code_M2": len(sites),
        "ancilla_M2": int(ancilla not in sites),
        "declared_M2": len(declared),
        "routed_locations": len(touched),
        "touched_declared": len(touched & declared),
        "transit_only": len(touched - declared),
        "untouched_declared": len(declared - touched),
        "placement_collisions": collisions,
        "primitive_counts": (len(e_word), len(character), len(e_word)),
        "routed_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "delete_first_swap_detected": route[
            "delete_first_swap_detected_macros"
        ],
        "expected_route_swap_gates": expected_route_swaps,
        **replay,
    }


def overlap_reconstruction() -> dict[str, object]:
    cells = G.box_cells((2, 2, 2))
    eq = G.build_equivalence(cells).equivalence
    keys = tuple(C.seam_key(label) for label in eq.rail_labels)
    pair = C.cleanup_edges(eq)[0]
    a = C.seam_images(eq, *keys[pair[0]])
    b = C.seam_images(eq, *keys[pair[1]])
    ab = C.compose(b, a, eq.qubits)
    ba = C.compose(a, b, eq.qubits)
    cleanup = C.cleanup_images(eq, (pair,))
    stabilizers = eq.target_w[len(eq.target_logical_z):]

    left_cells = G.box_cells((2, 2, 2))
    right_cells = tuple((x + 1, y, z) for x, y, z in left_cells)
    left_view = P.placement_bundle(left_cells, origin=(-8, 0, 0))
    right_view = P.placement_bundle(right_cells, origin=(8, 0, 0))
    left_map = P.address_placement(*left_view[:4])
    right_map = P.address_placement(*right_view[:4])
    shared = set(left_map) & set(right_map)
    kinds = Counter(key[0] for key in shared)
    shared_sites = {site for key in shared for site in left_map[key]}
    return {
        "raw": C.mismatch_counts(ab, ba),
        "repaired_AB": C.mismatch_counts(
            C.compose(cleanup, ab, eq.qubits), ba
        ),
        "repaired_BA": C.mismatch_counts(
            C.compose(cleanup, ba, eq.qubits), ab
        ),
        "stabilizer_rank": rank(
            row.x | (row.z << eq.qubits) for row in stabilizers
        ),
        "deleted_rank": rank(
            row.x | (row.z << eq.qubits) for row in stabilizers[1:]
        ),
        "shared_addresses": len(shared),
        "shared_kinds": dict(kinds),
        "shared_failures": sum(
            left_map[key] != right_map[key] for key in shared
        ),
        "shared_M2": len(shared_sites),
    }


def candidate(eq, fixture, tag):
    if tag[0] == "onsite_Z":
        cell, mode = tag[1:3]
        return eq.target_logical_z[6 * cell + mode]
    if tag[0] == "onsite_XX":
        cell, mode = tag[1:3]
        return eq.target_logical_x[6 * cell + mode] @ eq.target_logical_x[
            6 * cell + mode + 1
        ]
    _left, _right, owner, axis, _lm, _rm = fixture.edges[tag[1]]
    return eq.forward(
        R.source_fswap_terms(eq, tuple(owner), int(axis))[2]
    )


def gram_reconstruction(shape):
    fixture = M.CompanionFixture.build(shape)
    eq = G.build_equivalence(fixture.cells).equivalence
    _graph, tags = B.P.direct_graph_basis(fixture)
    targets = B.EB.target_rows(fixture, tags)
    rows = tuple(candidate(eq, fixture, tag) for tag in tags)
    failures = sum(
        anti(rows[left], rows[right]) != anti(targets[left], targets[right])
        for right in range(len(rows)) for left in range(right)
    )
    return len(rows), len(rows) * (len(rows) - 1) // 2, failures


def edge_gauge_reconstruction(shape):
    fixture = EG.CellEdgeGauge.build(shape)
    common = EG.diagonal_common_e(fixture)
    local = EG.constraint_and_update_certificate(fixture)
    failures = sum((
        common["logical_leakage_failures"],
        common["stabilizer_commutator_failures"],
        common["transformed_logical_term_failures"],
        common["transformed_coordinate_failures"],
        common["transformed_phase_failures"],
    ))
    return failures, local["shared_edge_register_use_minimum"], local[
        "shared_edge_register_use_maximum"
    ]


def character_covariance() -> dict[str, int]:
    source = C.F.build_equivalence(((0, 0, 0), (1, 0, 0)))
    source_row = R.source_fswap_terms(source, (0, 0, 0), 0)[2]
    bounded = source.forward(source_row)
    frames = C.F.base.proper_cubic_frames()
    frame_failures = 0
    for frame in frames:
        cells = tuple(
            tuple(int(value) for value in frame @ C.F.np.asarray(cell))
            for cell in source.cells
        )
        target = C.F.build_equivalence(cells)
        ot = C.F.graph_transform_data(source.open_graph, target.open_graph, frame)
        pt = C.F.graph_transform_data(source.patch_graph, target.patch_graph, frame)
        moved_source = C.F.transform_graph_pauli(
            source_row, ot[2], ot[3], ot[4], ot[5]
        )
        moved_bounded = C.F.transform_augmented_pauli(
            bounded, source, target, pt, ot[0]
        )
        frame_failures += moved_bounded != target.forward(moved_source)

    product_failures = 0
    for left in frames:
        for right in frames:
            direct = left @ right
            mid_cells = tuple(
                tuple(int(value) for value in right @ C.F.np.asarray(cell))
                for cell in source.cells
            )
            final_cells = tuple(
                tuple(int(value) for value in left @ C.F.np.asarray(cell))
                for cell in mid_cells
            )
            mid = C.F.build_equivalence(mid_cells)
            final = C.F.build_equivalence(final_cells)
            ot1 = C.F.graph_transform_data(source.open_graph, mid.open_graph, right)
            ot2 = C.F.graph_transform_data(mid.open_graph, final.open_graph, left)
            otd = C.F.graph_transform_data(source.open_graph, final.open_graph, direct)
            pt1 = C.F.graph_transform_data(source.patch_graph, mid.patch_graph, right)
            pt2 = C.F.graph_transform_data(mid.patch_graph, final.patch_graph, left)
            ptd = C.F.graph_transform_data(source.patch_graph, final.patch_graph, direct)
            mid_source = C.F.transform_graph_pauli(
                source_row, ot1[2], ot1[3], ot1[4], ot1[5]
            )
            seq_source = C.F.transform_graph_pauli(
                mid_source, ot2[2], ot2[3], ot2[4], ot2[5]
            )
            dir_source = C.F.transform_graph_pauli(
                source_row, otd[2], otd[3], otd[4], otd[5]
            )
            mid_bounded = C.F.transform_augmented_pauli(
                bounded, source, mid, pt1, ot1[0]
            )
            seq_bounded = C.F.transform_augmented_pauli(
                mid_bounded, mid, final, pt2, ot2[0]
            )
            dir_bounded = C.F.transform_augmented_pauli(
                bounded, source, final, ptd, otd[0]
            )
            product_failures += seq_source != dir_source
            product_failures += seq_bounded != dir_bounded
            product_failures += final.forward(seq_source) != seq_bounded
    return {
        "frames": len(frames),
        "frame_failures": frame_failures,
        "products": len(frames) ** 2,
        "product_failures": product_failures,
    }


def main() -> None:
    pin_rows = tuple({
        "path": relative,
        "expected_sha256": expected,
        "observed_sha256": (
            digest(ROOT / relative) if (ROOT / relative).is_file() else None
        ),
    } for relative, expected in PINNED_DIRECT_IMPORTS.items())
    pin_rows = tuple({
        **row,
        "match": row["observed_sha256"] == row["expected_sha256"],
    } for row in pin_rows)
    literal = literal_reconstruction()
    overlap = overlap_reconstruction()
    primary = gram_reconstruction((3, 2, 2))
    held = gram_reconstruction((5, 3, 2))
    gauges = tuple(
        edge_gauge_reconstruction(shape)
        for shape in ((3, 2, 2), (5, 3, 2))
    )
    covariance = character_covariance()
    factor_frames = C.frame_transport_certificate()
    factor_products = C.frame_product_certificate()
    closure = loaded_helper_closure()
    base = package_base_commit_certificate()
    primary_runner_sha256 = digest(ROOT / PRIMARY_RUNNER)
    checks = {
        "target_primary_and_direct_import_pins_match": (
            digest(ROOT / TARGET_SPEC) == TARGET_SHA256
            and (ROOT / PRIMARY_RUNNER).is_file()
            and primary_runner_sha256 == EXPECTED_PRIMARY_RUNNER_SHA256
            and all(row["match"] for row in pin_rows)
            and closure["match"]
            and base["pass"]
        ),
        "literal_resource_and_route_reconstructed": (
            literal["abstract_exact"]
            and (literal["code_M2"], literal["ancilla_M2"], literal["declared_M2"])
            == (39, 1, 40)
            and (literal["routed_locations"], literal["touched_declared"],
                 literal["transit_only"], literal["untouched_declared"])
            == (155, 20, 135, 20)
            and literal["primitive_counts"] == (74, 15, 74)
            and literal["routed_gates"] == 3327
            and literal["maximum_route_distance"] == 24
            and literal["non_NN_failures"] == 0
            and literal["operand_order_failures"] == 0
            and literal["route_return_failures"] == 0
            and literal["delete_first_swap_detected"] == 111
            and literal["replayed_route_swap_gates"]
            == literal["expected_route_swap_gates"] == 3164
            and literal["replayed_non_swap_gates"] == sum(
                literal["primitive_counts"]
            ) == 163
            and literal["replayed_NN_failures"] == 0
            and literal["replayed_operand_failures"] == 0
            and literal["replayed_kind_failures"] == 0
            and literal["replayed_matrix_failures"] == 0
            and literal["replayed_swap_matrix_failures"] == 0
            and literal["replayed_label_return_failures"] == 0
        ),
        "overlap_rank_and_shared_addresses_reconstructed": (
            overlap["raw"]["exact"] == 2
            and not any(overlap["repaired_AB"].values())
            and not any(overlap["repaired_BA"].values())
            and (overlap["stabilizer_rank"], overlap["deleted_rank"])
            == (120, 119)
            and overlap["shared_addresses"] == 80
            and overlap["shared_kinds"] == {"edge": 76, "rail": 4}
            and overlap["shared_failures"] == 0
            and overlap["shared_M2"] == 84
        ),
        "primary_held_Gram_reconstructed": (
            primary == (152, 11476, 22)
            and held == (389, 75466, 76)
        ),
        "edge_gauge_boundary_reconstructed": all(
            failures == 0 and minimum == maximum == 1
            for failures, minimum, maximum in gauges
        ),
        "signed_24_576_reconstructed": (
            covariance == {
                "frames": 24, "frame_failures": 0,
                "products": 576, "product_failures": 0,
            }
            and factor_frames["signed_exact_failures"] == 0
            and factor_frames["signed_phase_only_failures"] == 0
            and factor_products["signed_factor_diagram_failures"] == 0
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "direct_import_pins": pin_rows,
        "primary_runner_expected_sha256": EXPECTED_PRIMARY_RUNNER_SHA256,
        "primary_runner_observed_sha256": primary_runner_sha256,
        "loaded_helper_closure": closure,
        "package_base_commit": base,
        "literal": literal,
        "overlap": overlap,
        "primary_Gram": primary,
        "held_Gram": held,
        "edge_gauge": gauges,
        "covariance": covariance,
        "scope": (
            "independent structural reconstruction; the primary runner separately "
            "executes the 20-site dense state/tableau comparison"
        ),
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print(
        "CYCLE869_BOUNDED_TWO_STAR_BKSF_CHART_BRIDGE_INDEPENDENT_PASS"
        if report["status"] == "PASS"
        else "CYCLE869_BOUNDED_TWO_STAR_BKSF_CHART_BRIDGE_INDEPENDENT_FAIL"
    )
    raise SystemExit(0 if report["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
