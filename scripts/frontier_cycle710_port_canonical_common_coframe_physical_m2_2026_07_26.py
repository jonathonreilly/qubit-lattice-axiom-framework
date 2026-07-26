#!/usr/bin/env python3
"""Primary fail-closed runner for the bounded Cycle710 port compiler."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle710_port_canonical_order_gauge_core_2026_07_26 as C
import frontier_cycle710_port_canonical_physical_core_2026_07_26 as P


PASS = 0
FAIL = 0
NOTE_PATH = (
    "docs/PORT_CANONICAL_COMMON_COFRAME_PHYSICAL_M2_COMPILER_"
    "CYCLE710_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
ACTIVE_SOURCE_PATHS = (
    "scripts/frontier_cycle710_port_canonical_common_coframe_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle710_port_canonical_order_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle710_port_canonical_physical_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_"
    "CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    *ACTIVE_SOURCE_PATHS,
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
EXPECTED_DEPENDENCIES = {
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py":
        "64f73efb404f2acacb1a4e5e392aa8c6ac139eafb3e5f05380af9a3b3cc91826",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py":
        "5d49d85ddbc4daddfc0b24737dc569eaa9f32a050f5fccf48f048fe0fdd74b40",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py":
        "d74fb32e21879b2a843eae822c8e71b950729d9dc295eaf336911f174cceee3a",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py":
        "3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py":
        "71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py":
        "b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
}


def check(label: str, condition: bool, detail: object) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def json_ready(value):
    if isinstance(value, dict):
        return {
            key if isinstance(key, (str, int, float, bool)) else repr(key): json_ready(item)
            for key, item in value.items()
        }
    if isinstance(value, (tuple, list)):
        return [json_ready(item) for item in value]
    return value


def dependency_controls() -> dict[str, object]:
    actual = {
        name: sha256((ROOT / name).read_bytes()).hexdigest()
        for name in EXPECTED_DEPENDENCIES
    }
    return {
        "expected": EXPECTED_DEPENDENCIES,
        "actual": actual,
        "mismatches": {
            name: digest for name, digest in actual.items()
            if digest != EXPECTED_DEPENDENCIES[name]
        },
        "baseline_commit": "922b9b12a6f58cfd12afe829df914a3bf970d249",
    }


def replay_cycle709() -> dict[str, object]:
    runner = ROOT / "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py"
    completed = subprocess.run(
        [sys.executable, str(runner)], cwd=ROOT, text=True,
        capture_output=True, check=False,
    )
    lines = completed.stdout.splitlines()
    summary_line = next(
        (line for line in reversed(lines) if line.startswith("SUMMARY_JSON ")),
        "",
    )
    summary = json.loads(summary_line.removeprefix("SUMMARY_JSON ")) if summary_line else {}
    return {
        "returncode": completed.returncode,
        "terminal_present": (
            "CYCLE709_LOCAL_SEAM_PHYSICAL_M2_BOUNDED_COMPILER_PASS" in lines
        ),
        "pass_lines": sum(line.startswith("PASS ") for line in lines),
        "fail_lines": sum(line.startswith("FAIL ") for line in lines),
        "stdout_sha256": sha256(completed.stdout.encode()).hexdigest(),
        "stderr": completed.stderr,
        "mass_contact": summary.get("mass_contact_regression", {}),
        "physical_primary": summary.get("physical_primary", {}),
    }


def shuffled_aggregate(rows) -> dict[str, object]:
    semantic = sum(
        field for row in rows
        for family in row["semantic_failures"].values()
        for field in family.values()
    )
    locality = sum(
        gauge["graph_A_failures"] + gauge["pair_shared_vertex_failures"]
        + gauge["pair_cell_diameter_gt_two"]
        for row in rows for gauge in (row["open_gauge"], row["patch_gauge"])
    )
    span_failures = sum(
        row["code_span"]["declared_stabilizer_rank"]
        != row["code_span"]["actual_stabilizer_rank"]
        or row["code_span"]["union_stabilizer_rank"]
        != row["code_span"]["actual_stabilizer_rank"]
        or row["code_span"]["declared_semantic_rank"]
        != row["code_span"]["full_centralizer_dimension"]
        or row["code_span"]["semantic_stabilizer_commutator_failures"]
        or row["code_span"]["ambient_mismatch_outside_or_nonhermitian"]
        for row in rows
    )
    return {
        "fixtures": len(rows),
        "semantic_failure_sum": semantic,
        "locality_failure_sum": locality,
        "centralizer_span_failures": span_failures,
        "transition_term_sum": sum(
            row["open_gauge"]["Z_terms"] + row["open_gauge"]["CZ_terms"]
            + row["patch_gauge"]["Z_terms"] + row["patch_gauge"]["CZ_terms"]
            for row in rows
        ),
        "rank_table": tuple(
            (
                row["shape"],
                row["code_span"]["actual_stabilizer_rank"],
                row["code_span"]["full_centralizer_dimension"],
            )
            for row in rows[::4]
        ),
    }


def main() -> int:
    dependencies = dependency_controls()
    check(
        "the landed Cycle219/230/706-709 sources are pinned to main@922b9b12a6",
        not dependencies["mismatches"], dependencies,
    )

    upstream = replay_cycle709()
    check(
        "the complete landed Cycle709 physical compiler and mass/contact harness replays unchanged",
        upstream["returncode"] == 0 and upstream["terminal_present"]
        and upstream["pass_lines"] == 22 and upstream["fail_lines"] == 0
        and upstream["mass_contact"].get("one_particle_mass_residual", 1) < 3e-12
        and upstream["mass_contact"].get("contact_double_occupation_phase_residual", 1) < 3e-12,
        upstream,
    )

    legacy = C.legacy_local_match_campaign()
    check(
        "radius-one port rules exactly reproduce the landed presentation on five sizes",
        legacy == {
            "fixtures": 10,
            "incident_order_failures": 0,
            "oriented_A_failures": 0,
        }, legacy,
    )

    shuffles = shuffled_aggregate(C.port_shuffled_campaign())
    check(
        "twenty shuffled target paths need zero order gauge and cover the full signed-code centralizer",
        shuffles["fixtures"] == 20
        and shuffles["semantic_failure_sum"] == 0
        and shuffles["locality_failure_sum"] == 0
        and shuffles["centralizer_span_failures"] == 0
        and shuffles["transition_term_sum"] == 0,
        shuffles,
    )

    frames = C.port_frame_campaign()
    check(
        "all 24 proper-cubic frames and 576 products close with bounded local factors",
        frames["proper_cubic_frames"] == 24
        and frames["ordered_frame_products"] == 576
        and not any(frames[key] for key in (
            "semantic_failure_sum", "open_product_failures",
            "patch_product_failures", "inverse_failures", "locality_failures",
        )), frames,
    )

    overlap = C.port_independent_overlap_campaign()
    check(
        "independent target enumerations agree on all shared overlapping-cube registers",
        overlap["shared_augmented_addresses"] == 80
        and overlap["shared_patch_edge_addresses"] == 76
        and overlap["shared_rail_addresses"] == 4
        and overlap["independent_order_transition_terms"] == 0
        and overlap["graph_A_failures"] == 0,
        overlap,
    )

    restrictions = C.common_coframe_restriction_campaign()
    check(
        "one common coframe restricts exactly from 3x2x2 to both overlapping cubes",
        restrictions["checks"] == 96
        and restrictions["failure_checks"] == 0
        and restrictions["maximum_difference"] == 0,
        restrictions,
    )

    features = C.feature_factoring_campaign()
    check(
        "all presentation choices factor through local ports plus the finite coframe",
        all(
            not row["Z_feature_collisions"]
            and not row["pair_feature_collisions"]
            and not row["legacy_local_pair_order_collisions"]
            and not row["legacy_local_phase_collisions"]
            for row in features.values()
        ), features,
    )

    falsifier = C.independent_coframe_falsifier()
    check(
        "independent-coframe equality fails on the retained 108/88 and 46/42 discriminator",
        falsifier["semantic_failure_sum"] == 0
        and falsifier["same_physical_cube"] == {
            "open_term_difference": 108,
            "patch_term_difference": 88,
        }
        and falsifier["overlap_open"]["term_difference"] == 46
        and falsifier["overlap_patch"]["term_difference"] == 42,
        falsifier,
    )

    encoded = P.repetition_isometry_certificate()
    check(
        "local physical Z/CZ gates exactly intertwine the repetition encoding and preserve its constraints",
        encoded["maximum_intertwiner_residual"] < 3e-12
        and encoded["maximum_leakage_residual"] < 3e-12
        and encoded["maximum_stabilizer_commutator"] < 3e-12
        and encoded["number_commutator"] < 3e-12
        and encoded["minimum_active_deletion_residual"] > 1,
        encoded,
    )

    physical = P.common_coframe_physical_campaign()
    check(
        "the full pre-address/base/post-address compiler is physically routed in all 24 common coframes",
        physical["proper_cubic_frames"] == 24
        and physical["logical_intertwiner_failures"] == 0
        and physical["address_permutation_failures"] == 0
        and physical["identity_landed_word_failures"] == 0
        and physical["non_NN_failures"] == 0
        and physical["operand_order_failures"] == 0
        and physical["route_return_failures"] == 0
        and physical["minimum_active_gauge_deletion_failures"] > 0,
        physical,
    )

    no_go = {
        "N1_normalized_routes": 6,
        "N1_unexhausted_routes": 4,
        "N2_collapsed_residual": "independent-coframe mismatch equals the overlap-transition obligation",
        "N3_hidden_imports_promoted": (
            "common coframe", "prepared source/repetition sector",
            "serial route work and controller",
        ),
        "N4_residual_match": "Cycle709 target order is retired; independent coframe equality is distinct",
        "N5_tested_resolution": "edge/pair/cube/two-cube/five-box/24-frame/576-product",
        "N6_live_partial_closures": (
            "overlap transition cocycle", "local coframe gauge field",
            "sparse tag constraints", "staggered transport",
        ),
        "N7_steelman": "XOR the two local diagonal chart gauges and test its triple-overlap cocycle",
        "N8_echo": "Cycles706-709 repeatedly retired apparent nonlocality constructively",
        "gate_for_broad_negative": "FAIL",
        "disposition": "positive bounded theorem plus conditional falsifier only",
    }
    check(
        "N1-N8 rejects any no-go, minimum, shared-obstruction, or axiom-pressure claim",
        no_go["N1_normalized_routes"] >= 5
        and no_go["N1_unexhausted_routes"] > 0
        and no_go["gate_for_broad_negative"] == "FAIL",
        no_go,
    )

    note = (ROOT / NOTE_PATH).read_text()
    check(
        "the theorem note keeps authority none, audit unset, and the supplied/derived/open boundary explicit",
        "**Authority:** none" in note and "**Audit:** unset" in note
        and "## Supplied, derived, and open structure" in note
        and "time law." in note
        and "axiom-pressure" in note
        and "common coframe" in note,
        {"note": NOTE_PATH},
    )

    summary = {
        "authority": "none",
        "audit": "unset",
        "claim_type": "bounded_theorem",
        "claim_scope": (
            "enumeration-independent port-canonical physical-M2 compiler on open boxes "
            "with one supplied common coframe"
        ),
        "pass": PASS,
        "fail": FAIL,
        "dependencies": dependencies,
        "upstream_cycle709": upstream,
        "legacy_local_match": legacy,
        "shuffles": shuffles,
        "frames": frames,
        "overlap": overlap,
        "common_coframe_restrictions": restrictions,
        "feature_factoring": features,
        "independent_coframe_falsifier": falsifier,
        "encoded_gates": encoded,
        "physical_common_coframes": physical,
        "no_go_discipline": no_go,
        "inventory": C.supplied_inventory(),
        "terminal": "CYCLE710_PORT_CANONICAL_COMMON_COFRAME_PHYSICAL_M2_COMPILER_PASS",
    }
    print("SUMMARY_JSON", json.dumps(json_ready(summary), sort_keys=True))
    if FAIL:
        return 1
    print("CYCLE710_PORT_CANONICAL_COMMON_COFRAME_PHYSICAL_M2_COMPILER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
