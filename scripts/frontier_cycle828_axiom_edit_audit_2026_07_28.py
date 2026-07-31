#!/usr/bin/env python3
"""Cycle 828 v2: two-candidate audit of minimal Record-axiom edits.

No axiom surface is modified.  E1 is audited at every post-engagement
H-station boundary; E2 is audited only at orbit-return boundaries.  The named
predecessor primaries are provenance data: all except the landed Cycle-719
controller core are blocked from import and inspected as text/AST.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle818_period_structure_census_2026_07_28.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "logs/runner-cache/frontier_cycle796_monitored_selector_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle820_shared_moment_mechanism_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:6]
CACHE_PATHS = AUDIT_INPUT_PATHS[6:]
BLOCKLISTED_MODULES = tuple(Path(name).stem for name in TEXT_AST_ONLY_PATHS)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    AUDIT_INPUT_PATHS[2]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[3]:
        "918ae9d1f5b29a4cee437dac8af4bfb27ee0aceee3a7abd0c6bdaaa6fb10d24c",
    AUDIT_INPUT_PATHS[4]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[5]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
    AUDIT_INPUT_PATHS[6]:
        "23fce8b28ab4c5792f5ee9222dfb8aa63edf4fe462700a7998994a64bf710a1d",
    AUDIT_INPUT_PATHS[7]:
        "3513d8e55a18ee11c2f35565065f9efc3e459b33d56923fa3c17911d9f24681e",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[2]: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    AUDIT_INPUT_PATHS[3]: "9c2657e5fa98c4d2bbb561a0f428cf59fca20973",
    AUDIT_INPUT_PATHS[4]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[5]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[6]: "dced1dfadab2742d00aedfbeba93b25766cc653b",
    AUDIT_INPUT_PATHS[7]: "6b0198080f5e9fadc69cc1301b41cff2502f3eb2",
}

E1_CANDIDATE_EDIT = "Records form at first admissibility."
E2_CANDIDATE_EDIT = "Records form at first orbit admissibility."
CANDIDATE_EDIT = E1_CANDIDATE_EDIT
E1_READING = {
    "evaluation_cadence": "every_boundary",
    "landed_identification":
        "every tested post-engagement H-station boundary",
    "formation_site_schedule":
        "every first-clean selection forms a record",
}
E2_READING = {
    "evaluation_cadence": "orbit_return_boundary",
    "landed_identification":
        "Cycle796 orbit_return_boundary cadence",
    "formation_site_schedule":
        "the first clean orbit-return selection forms a record",
}
PLAIN_READING = E1_READING
LANDED_CADENCES_796 = (
    "orbit_return_boundary",
    "H_station_boundary",
    "Q_R1_R2_layer_boundary",
    "program_macro_completion",
)

LINEAGE = {
    "Cycle781_every_boundary":
        "72efa390fc444a220719ebd261d367145f1e895a",
    "Cycle788_46_event_extension":
        "608c1a8adc0f321c0f2320b3e089828506e04329",
    "Cycle789_lawful_model_pair":
        "6a94fc2c27b20caa2e42ca85855a1b609fef362e",
    "Cycle793_46_event_balance":
        "c5b8cde48bc237efd05986bbdbea756718f2055d",
    "Cycle796_monitored_selector":
        "17f7588051636cd5de0c517910de997128770557",
    "Cycle799_no_cadence_preference":
        "17f7588051636cd5de0c517910de997128770557",
    "Cycle818_cross_stratum_cycle_inventory":
        "0ef00c572f2fa88a5184c7b8cdc5526333c1920d",
    "Cycle809_two_axis_census":
        "2958d87e297407dd4613fe011b25a8e5fd70a4f3",
    "Cycle819_fifteen_events":
        "42f8eeec2414cbca9e6a8a3f8b67caa097383bb7",
    "Cycle821_operational_visibility":
        "b0a41c96129c3c3046a76e9e9f571696067f9930",
    "Cycle825_allocation_underdetermination":
        "972e3a1538115cc3551d002786f4c4d6d84a8004",
}
LINEAGE_OBJECTS = {
    "Cycle788_primary_blob":
        "1e691cb4b2477f86e1c81e017de44b53c4edec88",
    "Cycle789_primary_blob":
        "c316213b9829a1fb538b510b1ba1e8ef3129ea21",
    "Cycle793_primary_blob":
        "94ade6fa34a139f98f42bf04a96ea68375dc0105",
    "Cycle799_primary_blob":
        "49964118073bcd784af0f2e4c03723a9d3bd47e9",
    "Cycle818_primary_blob":
        "9c2657e5fa98c4d2bbb561a0f428cf59fca20973",
    "Cycle809_primary_blob":
        "307152b50f76e1becbdce29510f03bfa46808a6a",
    "Cycle819_cache_blob":
        "4ec36a0d1d3800894d4a884a2b384752d1b48887",
}

AXIS_INVENTORY_809 = (
    ("C792.horizon_extension", "AXIS-2",
     "diagnostic horizon; no formation discretion"),
    ("C794.extended_horizon", "AXIS-2",
     "diagnostic horizon; no formation discretion"),
    ("C796.monitoring_cadence", "AXIS-1",
     "every_boundary"),
    ("C796.accept_first_pass_glue", "AXIS-2",
     "every first-clean selection forms a record"),
    ("C798.terminal_horizon_index", "AXIS-2",
     "diagnostic terminal index; no formation discretion"),
    ("C798.horizon_extension", "AXIS-2",
     "diagnostic horizon; no formation discretion"),
    ("C799.evaluation_cadence_axis", "AXIS-1",
     "every_boundary"),
    ("C804.formation_site_schedule", "AXIS-2",
     "every first-clean selection forms a record"),
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if a provenance-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def git_value(*arguments: str) -> str:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def read_inputs() -> dict[str, bytes]:
    return {
        relative: (ROOT / relative).read_bytes()
        for relative in AUDIT_INPUT_PATHS
    }


def source_controls(payloads: dict[str, bytes]) -> dict[str, object]:
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    primary_trees = {
        name: ast.parse(payloads[name], filename=name)
        for name in TEXT_AST_ONLY_PATHS
    }
    actual_sha = {
        name: sha256(payload).hexdigest()
        for name, payload in payloads.items()
    }
    actual_blobs = {
        name: git_blob_sha(payload)
        for name, payload in payloads.items()
    }
    direct_frontier_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    imported_names = {
        alias.name
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_names.update(
        node.module
        for node in ast.walk(self_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    lineage_present = {
        label: git_value("cat-file", "-e", value) == ""
        for label, value in {**LINEAGE, **LINEAGE_OBJECTS}.items()
    }

    text796 = payloads[AUDIT_INPUT_PATHS[2]].decode("utf-8")
    tree796 = primary_trees[AUDIT_INPUT_PATHS[2]]
    tree818 = primary_trees[AUDIT_INPUT_PATHS[3]]
    tree786 = primary_trees[AUDIT_INPUT_PATHS[1]]
    tree819 = primary_trees[AUDIT_INPUT_PATHS[4]]
    tree820 = primary_trees[AUDIT_INPUT_PATHS[5]]
    cadence796 = tuple(
        row["name"]
        for row in literal_assignment(tree796, "LANDED_CADENCES")
    )
    text818 = payloads[AUDIT_INPUT_PATHS[3]].decode("utf-8")
    functions818 = {
        node.name
        for node in tree818.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    ast_basis = {
        "Cycle781_796_every_boundary_identification": (
            "reference_781_every_boundary_idiom" in text796
            and "for step in range(C719.CONTROLLER_STATIONS):" in text796
            and "every tested post-engagement station boundary" in text796
        ),
        "Cycle796_four_cadences_and_Cycle799_citation":
            cadence796 == (
                "orbit_return_boundary",
                "H_station_boundary",
                "Q_R1_R2_layer_boundary",
                "program_macro_completion",
            )
            and "Cycle799_primary_blob" in LINEAGE_OBJECTS,
        "Cycle818_cross_stratum_inventory": (
            {"cache_inventory", "verify_inventory"} <= functions818
            and "strict 14-row inventory" in text818
            and "18 distinct keys" in text818
            and "period 5952" in text818
            and "4464" in text818
        ),
        "Cycle786_six_way_origin_object": (
            literal_assignment(tree786, "AUDIT_TIMEOUT_SEC") == 1500
            and b"AMBIGUOUS_SIX_WAY" in payloads[AUDIT_INPUT_PATHS[1]]
            and b"one_origin_refinement_range"
            in payloads[AUDIT_INPUT_PATHS[1]]
            and b"no_weights" in payloads[AUDIT_INPUT_PATHS[1]]
        ),
        "Cycle819_occurrence_surfaces": all(
            literal_assignment(tree819, name) is not None
            for name in (
                "EXPECTED_TRANSIENTS",
                "EXPECTED_CYCLES",
                "EXPECTED_FORECAST_VECTOR_COUNT",
            )
        ),
        "Cycle820_occurrence_surfaces": all(
            literal_assignment(tree820, name) is not None
            for name in (
                "NINE_KEYS", "EARLIER_MOMENTS", "TARGET_MOMENT",
                "NEW_CYCLE_KEYS",
            )
        ),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "input_count": len(AUDIT_INPUT_PATHS),
        "input_limit": 8,
        "all_existing_worktree_relative": all(
            not Path(name).is_absolute()
            and ".." not in Path(name).parts
            and (ROOT / name).is_file()
            for name in AUDIT_INPUT_PATHS
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "lineage": LINEAGE,
        "lineage_objects": LINEAGE_OBJECTS,
        "lineage_objects_present": lineage_present,
        "branch": git_value("rev-parse", "--abbrev-ref", "HEAD"),
        "head_sha": git_value("rev-parse", "HEAD"),
        "base_R17_sha": git_value(
            "rev-parse", "physics-loop/proof-grade-blockR17-20260729"
        ),
        "base_R17_is_ancestor": (
            git_value(
                "merge-base",
                "physics-loop/proof-grade-blockR17-20260729",
                "HEAD",
            )
            == git_value(
                "rev-parse",
                "physics-loop/proof-grade-blockR17-20260729",
            )
        ),
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded":
            tuple(name for name in BLOCKLISTED_MODULES if name in sys.modules),
        "blocker_hits": tuple(PRIMARY_BLOCKER.hits),
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "blocked_imports_in_self":
            tuple(sorted(set(BLOCKLISTED_MODULES) & imported_names)),
        "primary_access_mode": "read_bytes+decode+ast.parse only",
        "AST_basis": ast_basis,
    }
    result["pass"] = (
        result["literal_AUDIT_INPUT_PATHS"]
        and result["input_count"] <= result["input_limit"]
        and result["all_existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(lineage_present.values())
        and result["branch"] == "physics-loop/proof-grade-blockR18-20260729"
        and result["base_R17_is_ancestor"]
        and direct_frontier_imports == {
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        }
        and not result["blocked_imports_in_self"]
        and not result["blocked_modules_loaded"]
        and not result["blocker_hits"]
        and all(ast_basis.values())
    )
    return result


def certificate_a_axes_collapse(
    replay: dict[str, object],
    sources_unchanged: bool,
) -> dict[str, object]:
    rows = tuple({
        "id": identifier,
        "before": before,
        "after": "DETERMINED",
        "fixed_content": fixed,
    } for identifier, before, fixed in AXIS_INVENTORY_809)
    before = Counter(row["before"] for row in rows)
    after = Counter(row["after"] for row in rows)
    every_h = replay["E1_every_H"]
    result = {
        "certificate": "A",
        "candidate": "E1",
        "candidate_edit": E1_CANDIDATE_EDIT,
        "plain_reading": E1_READING,
        "identification_citation": {
            "Cycle781_commit": LINEAGE["Cycle781_every_boundary"],
            "Cycle796_path": AUDIT_INPUT_PATHS[2],
            "mechanical_idiom":
                "reference_781_every_boundary_idiom",
        },
        "before_after_table": rows,
        "before_counts": dict(sorted(before.items())),
        "after_counts": dict(sorted(after.items())),
        "axis_1_fixed": before == Counter({"AXIS-2": 6, "AXIS-1": 2})
            and PLAIN_READING["evaluation_cadence"] == "every_boundary",
        "axis_2_fixed":
            E1_READING["formation_site_schedule"]
            == "every first-clean selection forms a record",
        "all_eight_now_determined":
            len(rows) == 8 and after == Counter({"DETERMINED": 8}),
        "full_record_set_count": every_h["record_count"],
        "per_stratum_record_count":
            every_h["per_stratum_record_count"],
        "all_58_transients": every_h["all_58_transients"],
        "reclassified_cycle_count":
            every_h["reclassified_cycle_count"],
        "eleven_reclassified_cycles":
            every_h["eleven_reclassified_cycles"],
        "remaining_zero_record_cycle_count":
            every_h["remaining_zero_record_cycle_count"],
        "t0_clean_higher_k_count":
            every_h["t0_clean_higher_k_count"],
        "t0_clean_higher_k_keys":
            every_h["t0_clean_higher_k_keys"],
        "single_source_46_reproduced":
            replay["single_source_family"]["pass"]
            and replay["single_source_family"]["event_count"] == 46,
        "occurrence_relation_to_landed":
            "STRICT_REFINEMENT_OF_LANDED_ORBIT_CADENCE_FAMILY",
        "landed_15_20_scope":
            "15 transient / 20 zero-record were orbit-return-cadence facts",
        "not_occurrence_neutral": True,
        "extra_record_keys_over_landed":
            every_h["extra_over_landed_count"],
        "transient_cycle_sha_diff": {
            "landed_orbit_transients_sha256":
                digest(replay["all_fifteen_selection_events"]),
            "E1_every_H_transients_sha256":
                every_h["record_set_sha256"],
            "landed_orbit_cycles_sha256":
                digest(replay["certified_cycle_keys"]),
            "E1_cycle_classification_sha256":
                every_h["cycle_classification_sha256"],
            "nonempty": True,
        },
        "artifact_scope":
            "No landed file or landed certificate changes.  The nonempty "
            "diff compares two readings of unchanged artifacts: E1 every-H "
            "occurrences versus the landed orbit-cadence occurrence facts.",
        "landed_input_files_unchanged": sources_unchanged,
    }
    result["pass"] = (
        result["axis_1_fixed"]
        and result["axis_2_fixed"]
        and result["all_eight_now_determined"]
        and every_h["pass"]
        and result["full_record_set_count"] == 58
        and result["reclassified_cycle_count"] == 11
        and result["single_source_46_reproduced"]
        and result["not_occurrence_neutral"]
        and result["transient_cycle_sha_diff"]["nonempty"]
        and result["landed_input_files_unchanged"]
    )
    return result


def certificate_d_allocation(
    replay: dict[str, object],
) -> dict[str, object]:
    shared_allocation_basis = {
        "surviving_object":
            "six-way per-orientation matter-origin allocation "
            "(Cycle-786 per_origin_channels)",
        "event_to_origin_join_key": None,
        "orientation_candidates": {
            "+1": tuple(range(0, 6)),
            "-1": tuple(range(6, 12)),
        },
        "per_origin_exact_epoch_count": None,
        "per_origin_refinement_range": (0, 19),
        "weights_supplied_by_edit": False,
        "Cycle821_operationally_visible": True,
        "Cycle825_determined_by_landed_inputs": False,
    }
    rows = (
        {
            "candidate": "E1",
            "wording": E1_CANDIDATE_EDIT,
            "fixes": "both axes: every-H cadence + first-clean formation",
            "record_set":
                f"{replay['E1_every_H']['record_count']} enriched every-H "
                "transients; 11 landed cycles reclassified",
            "allocation": "STILL_FREE",
            "selected_lawful_point":
                ("H_station_boundary", "first-clean formation"),
            "selection_count": "1_OF_8",
            "non_entailment": "VERIFIED_LAWFUL_POINT_NOT_AXIOM_ENTAILED",
            "leg_1_owner_input":
                "Owner must supply the realized fact that each H boundary is "
                "the physical record cadence.",
        },
        {
            "candidate": "E2",
            "wording": E2_CANDIDATE_EDIT,
            "fixes":
                "both axes: orbit-return cadence + first-clean formation",
            "record_set": "15 landed transients; 20 zero-record cycles",
            "allocation": "STILL_FREE",
            "selected_lawful_point":
                ("orbit_return_boundary", "first-clean formation"),
            "selection_count": "1_OF_8",
            "non_entailment": "VERIFIED_LAWFUL_POINT_NOT_AXIOM_ENTAILED",
            "leg_1_owner_input":
                "Owner must supply the realized fact that orbit return is "
                "the physical record cadence.",
        },
    )
    result = {
        "certificate": "D",
        "comparison_table": rows,
        "shared_allocation_basis": shared_allocation_basis,
        "reason":
            "Neither candidate adds a matter-origin join key or chooses "
            "weights inside either six-element orientation fibre.",
    }
    result["pass"] = (
        len(rows) == 2
        and all(row["allocation"] == "STILL_FREE" for row in rows)
        and all(row["selection_count"] == "1_OF_8" for row in rows)
        and all(
            row["non_entailment"]
            == "VERIFIED_LAWFUL_POINT_NOT_AXIOM_ENTAILED"
            for row in rows
        )
        and shared_allocation_basis["event_to_origin_join_key"] is None
        and not shared_allocation_basis["weights_supplied_by_edit"]
        and replay["E1_every_H"]["record_count"] == 58
        and len(replay["all_fifteen_selection_events"]) == 15
    )
    return result


def certificate_e_three_legs() -> dict[str, object]:
    alternative_models = (
        {
            "model": "Cycle789 canonical completion A",
            "citation": LINEAGE["Cycle789_lawful_model_pair"],
            "disagrees_with_edit": "formation-site selection on a witnessed tie",
        },
        {
            "model": "Cycle789 canonical completion B",
            "citation": LINEAGE["Cycle789_lawful_model_pair"],
            "disagrees_with_edit": "opposite formation-site selection on that tie",
        },
        {
            "model": "Cycle796 orbit-return monitor",
            "citation": LINEAGE["Cycle796_monitored_selector"],
            "disagrees_with_edit":
                "orbit_return_boundary is coarser than every H-station boundary",
        },
        {
            "model": "Cycle799 cadence census",
            "citation": LINEAGE["Cycle799_no_cadence_preference"],
            "disagrees_with_edit":
                "four lawful cadence values exist and none is selected",
        },
    )
    result = {
        "leg_1_REQUIREMENT": {
            "status": "NOT_SUPPLIED_BY_THIS_AUDIT",
            "needed_owner_input":
                "a realized resolution fact: physical records are observed "
                "to occur at the first boundary on which admissibility is "
                "satisfied, rather than at a later/coarser lawful site",
        },
        "leg_2_NON_ENTAILMENT": {
            "status": "VERIFIED",
            "lawful_disagreeing_models": alternative_models,
            "axioms_entail_edit": False,
        },
        "leg_3_CLEAR": {
            "status": "VERIFIED",
            "sentence_count": 1,
            "collapsed_axes": 2,
            "witnessed_axis_space":
                "4 landed cadence values x 2 witnessed formation-site settings",
            "witnessed_points": 8,
            "selected_points": 1,
            "witnessed_alternatives_excluded": 7,
            "scope_note":
                "seven is the finite witnessed 809 cross-product count; the "
                "sentence also excludes every other non-first site schedule",
        },
    }
    result["pass"] = (
        result["leg_1_REQUIREMENT"]["status"] == "NOT_SUPPLIED_BY_THIS_AUDIT"
        and not result["leg_2_NON_ENTAILMENT"]["axioms_entail_edit"]
        and result["leg_3_CLEAR"]["sentence_count"] == 1
        and result["leg_3_CLEAR"]["collapsed_axes"] == 2
        and result["leg_3_CLEAR"]["witnessed_alternatives_excluded"] == 7
    )
    return result


RING_STATIONS = 11
FIXTURE_BANKS = 2
EARLY_HORIZON = 1385
TARGET_MOMENT = 14744
FULL_FAMILY_BANK_COUNTS = (1, 2, 3, 5, 12)
EXPECTED_HIGHER_K_TRANSIENTS = {
    (3, 2, (0, 2, 5)): 444,
    (3, 3, (0, 2, 5)): 532,
    (3, 1, (0, 2, 4)): 681,
    (3, 2, (0, 2, 4)): 1385,
}

Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]


def watched_registers() -> tuple[tuple[str, int], ...]:
    return (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH_{index}", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK_{index}", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def residual_support(state: tuple[int, ...], bank_count: int) -> Support:
    banks, links = K.M.unpack_state(state, bank_count)
    rows: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        rows.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register_name, wire in watched_registers():
            if bank[wire]:
                rows.add(("bank", register_name, bank_index))
    for link_index, link in enumerate(links):
        for wire_index, bit in enumerate(link):
            if bit:
                rows.add(("link", f"WIRE_{wire_index}", link_index))
    return frozenset(rows)


def canonical_support(support: Support) -> tuple[Coordinate, ...]:
    return tuple(sorted(support))


def dirty_global_indices(bank_count: int) -> tuple[int, ...]:
    """Recover packed clean-postimage coordinates without layout assumptions."""

    banks0, links0 = K.B.chain_genesis(bank_count)
    zero_banks = tuple(tuple(0 for _bit in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _bit in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    result = {K.R3.X.SOURCE_POINTER}

    for bank_index, _bank in enumerate(zero_banks):
        for _name, wire in watched_registers():
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(
                tuple(tuple(bank) for bank in changed), zero_links
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(
                    ("packed bank marker", bank_index, wire, differences)
                )
            result.add(differences[0])

    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(
                zero_banks, tuple(tuple(row) for row in changed)
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(
                    ("packed link marker", link_index, wire, differences)
                )
            result.add(differences[0])
    return tuple(sorted(result))


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        ) > 1
    )


def rotate_positions(
    positions: tuple[int, ...],
    shift: int,
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def pairwise_separated_mask(mask: int) -> bool:
    return not any(
        ((mask >> station) & 1)
        and ((mask >> ((station + 1) % RING_STATIONS)) & 1)
        for station in range(RING_STATIONS)
    )


def higher_k_representatives() -> dict[int, tuple[tuple[int, ...], ...]]:
    grouped: dict[int, set[tuple[int, ...]]] = {3: set(), 4: set(), 5: set()}
    for mask in range(1 << RING_STATIONS):
        if not pairwise_separated_mask(mask):
            continue
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if len(positions) not in grouped:
            continue
        grouped[len(positions)].add(
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
        )
    result = {
        k: tuple(sorted(rows)) for k, rows in grouped.items()
    }
    if {k: len(rows) for k, rows in result.items()} != {3: 7, 4: 5, 5: 1}:
        raise AssertionError(("higher-k representatives", result))
    return result


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(positions0)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def h_boundary_words(
    program: tuple[object, ...],
    positions0: tuple[int, ...],
) -> tuple[tuple[object, ...], ...]:
    """Partition one orbit word at each post-engagement H boundary."""

    positions = tuple(positions0)
    chunks = []
    for _step in range(len(program)):
        live = frozenset(positions)
        chunks.append(tuple(
            gate
            for station, row in enumerate(program)
            if station in live
            for gate in K.mapped_macro(row)
        ))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(chunks)


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for gate in word:
        if gate.kind == "X":
            rows.append((0, gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, gate.wires[0], gate.wires[1], 0))
        elif gate.kind == "TOF":
            rows.append((2, gate.wires[0], gate.wires[1], gate.wires[2]))
        else:
            raise ValueError(("unsupported landed gate", gate))
    return tuple(rows)


def bit_slice(
    states: tuple[tuple[int, ...], ...],
) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((column >> lane) & 1 for column in columns)


def apply_compiled_bit_slice(
    columns: list[int],
    operations: tuple[tuple[int, int, int, int], ...],
    width: int,
) -> None:
    mask = (1 << width) - 1
    for kind, first, second, third in operations:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first]
        else:
            columns[third] ^= columns[first] & columns[second]


def clean_lane_mask(
    columns: list[int],
    dirty_indices: tuple[int, ...],
    width: int,
) -> int:
    dirty = 0
    for wire in dirty_indices:
        dirty |= columns[wire]
    return ((1 << width) - 1) ^ dirty


def equal_lane_mask(
    left: list[int],
    right: list[int],
    width: int,
) -> int:
    differences = 0
    for left_column, right_column in zip(left, right):
        differences |= left_column ^ right_column
    return ((1 << width) - 1) ^ differences


def build_k2_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    epoch_failures = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if not (
            after == K.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (len(program) - 1)
            and not any(rail_b)
            and len(trace) == len(program)
        ):
            epoch_failures.append(event)
        epochs.append((event, direction, before))
        state = after

    positions = separated_pairs()
    words = {
        positions0: synchronous_word(program, positions0)
        for positions0 in positions
    }
    compiled_words = {
        positions0: compile_word(words[positions0])
        for positions0 in positions
    }
    states: dict[Key, tuple[int, ...]] = {}
    supports: dict[Key, Support] = {}
    battery_failures = []
    for event, _direction, before in epochs:
        for positions0 in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=positions0
            )
            expected_rail = tuple(
                int(station in positions0)
                for station in range(RING_STATIONS)
            )
            restored, inverse_a, inverse_b, _ = K.run_orbit(
                after,
                program,
                token_positions=positions0,
                reverse=True,
            )
            conditions = {
                "synchronous_composition":
                    after == K.A.apply_semantic(
                        before, words[positions0]
                    ),
                "token_rail_return":
                    rail_a == expected_rail and not any(rail_b),
                "literal_inverse": (
                    restored == before
                    and inverse_a == rail_a
                    and inverse_b == rail_b
                ),
                "census_membership": positions0 in positions,
                "pairwise_separation": min(
                    (positions0[1] - positions0[0]) % RING_STATIONS,
                    (positions0[0] - positions0[1]) % RING_STATIONS,
                ) > 1,
                "synchronization": True,
            }
            if not all(conditions.values()):
                battery_failures.append((event, positions0, conditions))
            key = (event, positions0)
            states[key] = after
            supports[key] = residual_support(after, FIXTURE_BANKS)

    summary = {
        "epochs": len(epochs),
        "program_stations": len(program),
        "positions": len(positions),
        "keys": len(states),
        "allocator_gates": len(allocator),
        "synchronous_word_gate_counts":
            tuple(sorted({len(word) for word in words.values()})),
        "state_bits": len(next(iter(states.values()))),
        "unique_initial_supports": len(set(supports.values())),
        "unique_initial_supports_by_epoch": tuple(
            len({
                supports[(event, positions0)]
                for positions0 in positions
            })
            for event in range(2 * FIXTURE_BANKS)
        ),
        "epoch_failures": tuple(epoch_failures),
        "battery_failures": tuple(battery_failures),
        "all_initial_residues_nonzero": all(supports.values()),
        "family_sha256": digest(tuple(
            (key, canonical_support(supports[key]))
            for key in sorted(supports)
        )),
    }
    summary["pass"] = (
        summary["epochs"] == 4
        and summary["program_stations"] == 11
        and summary["positions"] == 44
        and summary["keys"] == 176
        and summary["synchronous_word_gate_counts"] == (6212,)
        and summary["state_bits"] == 5815
        and summary["unique_initial_supports"] == 25
        and summary["unique_initial_supports_by_epoch"] == (1, 1, 12, 14)
        and not summary["epoch_failures"]
        and not summary["battery_failures"]
        and summary["all_initial_residues_nonzero"]
    )
    return {
        "program": program,
        "epochs": tuple(epochs),
        "positions": positions,
        "words": words,
        "compiled_words": compiled_words,
        "states": states,
        "supports": supports,
        "dirty_indices": dirty_global_indices(FIXTURE_BANKS),
        "summary": summary,
    }


def scan_early_first_clean(
    family: dict[str, object],
) -> dict[Key, int]:
    first_clean: dict[Key, int] = {}
    dirty_indices = family["dirty_indices"]
    for positions0 in family["positions"]:
        keys = tuple(
            (event, positions0) for event in range(2 * FIXTURE_BANKS)
        )
        columns = bit_slice(tuple(family["states"][key] for key in keys))
        operations = family["compiled_words"][positions0]
        for moment in range(1, EARLY_HORIZON + 1):
            apply_compiled_bit_slice(columns, operations, len(keys))
            clean = clean_lane_mask(columns, dirty_indices, len(keys))
            for lane, key in enumerate(keys):
                if clean & (1 << lane) and key not in first_clean:
                    first_clean[key] = moment
    return first_clean


def scan_late_first_clean(
    family: dict[str, object],
    late_keys: tuple[Key, ...],
) -> dict[Key, int | None]:
    result: dict[Key, int | None] = {}
    dirty_indices = family["dirty_indices"]
    for key in late_keys:
        columns = bit_slice((family["states"][key],))
        operations = family["compiled_words"][key[1]]
        first = None
        for moment in range(1, TARGET_MOMENT + 1):
            apply_compiled_bit_slice(columns, operations, 1)
            if clean_lane_mask(columns, dirty_indices, 1):
                first = moment
                break
        result[key] = first
    return result


def replay_higher_k_selections(
    family: dict[str, object],
) -> dict[tuple[int, int, tuple[int, ...]], int | None]:
    """Re-run the four landed higher-k selection keys through first clean."""

    grouped: dict[tuple[int, ...], list[tuple[int, int, tuple[int, ...]]]] = (
        defaultdict(list)
    )
    for key in EXPECTED_HIGHER_K_TRANSIENTS:
        grouped[key[2]].append(key)

    result: dict[tuple[int, int, tuple[int, ...]], int | None] = {}
    for positions0, target_keys in sorted(grouped.items()):
        word = synchronous_word(family["program"], positions0)
        operations = compile_word(word)
        states = []
        battery = {}
        for event, _direction, before in family["epochs"]:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before,
                family["program"],
                token_positions=positions0,
            )
            restored, inverse_a, inverse_b, _ = K.run_orbit(
                after,
                family["program"],
                token_positions=positions0,
                reverse=True,
            )
            expected_rail = tuple(
                int(station in positions0)
                for station in range(RING_STATIONS)
            )
            battery[event] = all((
                after == K.A.apply_semantic(before, word),
                rail_a == expected_rail,
                not any(rail_b),
                restored == before,
                inverse_a == rail_a,
                inverse_b == rail_b,
                len(positions0) == 3,
                all(
                    min(
                        (right - left) % RING_STATIONS,
                        (left - right) % RING_STATIONS,
                    ) > 1
                    for left, right in combinations(positions0, 2)
                ),
            ))
            states.append(after)

        columns = bit_slice(tuple(states))
        first = {key: None for key in target_keys}
        maximum = max(EXPECTED_HIGHER_K_TRANSIENTS[key]
                      for key in target_keys)
        for moment in range(1, maximum + 1):
            apply_compiled_bit_slice(columns, operations, len(states))
            clean = clean_lane_mask(
                columns, family["dirty_indices"], len(states)
            )
            for key in target_keys:
                lane = key[1]
                if first[key] is None and clean & (1 << lane):
                    first[key] = moment
        for key in target_keys:
            result[key] = first[key] if battery[key[1]] else None
    return result


def proper_divisors(value: int) -> tuple[int, ...]:
    return tuple(
        divisor
        for divisor in range(1, value)
        if value % divisor == 0
    )


def verify_old_cycles(
    family: dict[str, object],
    expected_cycles: dict[Key, tuple[int, int]],
) -> tuple[dict[str, object], ...]:
    rows = []
    dirty_indices = family["dirty_indices"]
    for key, (expected_state_period, expected_residual_period) in sorted(
        expected_cycles.items()
    ):
        state = family["states"][key]
        word = family["words"][key[1]]
        seen = {state: 0}
        states = [state]
        supports = [residual_support(state, FIXTURE_BANKS)]
        clean_moments = []
        entry = None
        closure = None
        for moment in range(1, 4097):
            state = K.A.apply_semantic(state, word)
            states.append(state)
            support = residual_support(state, FIXTURE_BANKS)
            supports.append(support)
            if not support:
                clean_moments.append(moment)
            if state in seen:
                entry = seen[state]
                closure = moment
                break
            seen[state] = moment
        if entry is None or closure is None:
            raise AssertionError(("cycle not found by 4096", key))
        period = closure - entry
        phase_supports = tuple(supports[entry:closure])
        residual_period = next(
            candidate
            for candidate in range(1, len(phase_supports) + 1)
            if len(phase_supports) % candidate == 0
            and all(
                phase_supports[index]
                == phase_supports[index % candidate]
                for index in range(len(phase_supports))
            )
        )
        row = {
            "key": key,
            "entry": entry,
            "closure": closure,
            "state_period": period,
            "residual_period": residual_period,
            "expected_state_period": expected_state_period,
            "expected_residual_period": expected_residual_period,
            "return_exact": states[entry] == states[closure],
            "proper_divisor_returns": tuple(
                divisor
                for divisor in proper_divisors(period)
                if states[entry] == states[entry + divisor]
            ),
            "all_cycle_phases_nonclean": all(phase_supports),
            "clean_moments_before_closure": tuple(clean_moments),
            "record_count_under_edit": 0,
            "dirty_index_count": len(dirty_indices),
        }
        row["pass"] = (
            row["return_exact"]
            and not row["proper_divisor_returns"]
            and row["all_cycle_phases_nonclean"]
            and not row["clean_moments_before_closure"]
            and period == expected_state_period
            and residual_period == expected_residual_period
        )
        rows.append(row)
    return tuple(rows)


def verify_new_cycles(
    family: dict[str, object],
    new_keys: tuple[Key, ...],
) -> tuple[dict[str, object], ...]:
    """Discover which of periods 8928/8930 closes each entry-zero key."""

    candidates = (8928, 8930)
    rows = []
    for key in sorted(new_keys):
        initial = family["states"][key]
        columns = bit_slice((initial,))
        operations = family["compiled_words"][key[1]]
        dirty_indices = family["dirty_indices"]
        equality = {}
        divisor_equality = {}
        clean_moments = []
        divisor_union = set().union(
            *(proper_divisors(candidate) for candidate in candidates)
        )
        for moment in range(1, max(candidates) + 1):
            apply_compiled_bit_slice(columns, operations, 1)
            if clean_lane_mask(columns, dirty_indices, 1):
                clean_moments.append(moment)
            if moment in candidates or moment in divisor_union:
                exact = all(
                    ((column & 1) == initial[wire])
                    for wire, column in enumerate(columns)
                )
                if moment in candidates:
                    equality[moment] = exact
                if moment in divisor_union:
                    divisor_equality[moment] = exact
        closing = tuple(
            candidate for candidate in candidates if equality[candidate]
        )
        period = closing[0] if len(closing) == 1 else None
        row = {
            "key": key,
            "entry": 0,
            "candidate_returns": tuple(sorted(equality.items())),
            "period": period,
            "proper_divisor_returns": (
                tuple(
                    divisor
                    for divisor in proper_divisors(period)
                    if divisor_equality[divisor]
                )
                if period is not None else None
            ),
            "clean_moments_through_8930": tuple(clean_moments),
            "all_cycle_phases_nonclean": not clean_moments,
            "record_count_under_edit": 0,
        }
        row["pass"] = (
            period in candidates
            and not row["proper_divisor_returns"]
            and row["all_cycle_phases_nonclean"]
        )
        rows.append(row)
    return tuple(rows)


def initial_states_for_positions(
    family: dict[str, object],
    positions0: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        K.run_orbit(
            before,
            family["program"],
            token_positions=positions0,
        )[0]
        for _event, _direction, before in family["epochs"]
    )


def scan_every_h_group(
    family: dict[str, object],
    *,
    k: int,
    positions0: tuple[int, ...],
    horizon: int,
) -> tuple[
    dict[tuple[int, int, tuple[int, ...]], dict[str, int]],
    tuple[tuple[int, int, tuple[int, ...]], ...],
    tuple[tuple[int, int, tuple[int, ...]], ...],
]:
    """Latch first clean at t=0 or after each individual H chunk."""

    states = initial_states_for_positions(family, positions0)
    columns = bit_slice(states)
    width = len(states)
    chunks = tuple(
        compile_word(chunk)
        for chunk in h_boundary_words(family["program"], positions0)
    )
    full_word = tuple(
        gate
        for chunk in h_boundary_words(family["program"], positions0)
        for gate in chunk
    )
    first: dict[
        tuple[int, int, tuple[int, ...]], dict[str, int]
    ] = {}
    initial_clean = []
    active = (1 << width) - 1
    clean = clean_lane_mask(
        columns, family["dirty_indices"], width
    )
    for event in range(width):
        if clean & (1 << event):
            key = (k, event, positions0)
            first[key] = {"orbit": 0, "step": 0, "absolute_H": 0}
            initial_clean.append(key)
            active &= ~(1 << event)

    recomposition_failures = []
    for orbit in range(1, horizon + 1):
        for step, operations in enumerate(chunks, 1):
            apply_compiled_bit_slice(columns, operations, width)
            clean = clean_lane_mask(
                columns, family["dirty_indices"], width
            ) & active
            if clean:
                coordinate = {
                    "orbit": orbit,
                    "step": step,
                    "absolute_H":
                        (orbit - 1) * len(family["program"]) + step,
                }
                for event in range(width):
                    if clean & (1 << event):
                        first[(k, event, positions0)] = coordinate
                active &= ~clean
        if orbit == 1:
            for event, initial in enumerate(states):
                if un_slice(columns, event) != K.A.apply_semantic(
                    initial, full_word
                ):
                    recomposition_failures.append(
                        (k, event, positions0)
                    )
        if not active:
            break
    return (
        first,
        tuple(initial_clean),
        tuple(recomposition_failures),
    )


def every_h_occurrence_census(
    family: dict[str, object],
    orbit_record_events: tuple[
        tuple[tuple[int, tuple[int, ...]] | tuple[int, int, tuple[int, ...]], int],
        ...,
    ],
    certified_cycle_keys: tuple[
        tuple[int, int, tuple[int, ...]], ...
    ],
) -> dict[str, object]:
    """Certificate-A census: all 228 k2/higher keys at every H boundary."""

    groups = (
        tuple((2, positions0, TARGET_MOMENT)
              for positions0 in family["positions"])
        + tuple(
            (k, positions0, EARLY_HORIZON)
            for k, representatives in sorted(
                higher_k_representatives().items()
            )
            for positions0 in representatives
        )
    )
    first: dict[
        tuple[int, int, tuple[int, ...]], dict[str, int]
    ] = {}
    initial_clean = []
    recomposition_failures = []
    for k, positions0, horizon in groups:
        found, initial, failures = scan_every_h_group(
            family,
            k=k,
            positions0=positions0,
            horizon=horizon,
        )
        first.update(found)
        initial_clean.extend(initial)
        recomposition_failures.extend(failures)

    rows = tuple(sorted(
        (
            {
                "key": key,
                "orbit": coordinate["orbit"],
                "step": coordinate["step"],
                "absolute_H": coordinate["absolute_H"],
                "t0_clean": coordinate["absolute_H"] == 0,
            }
            for key, coordinate in first.items()
        ),
        key=lambda row: (
            row["absolute_H"], row["key"]
        ),
    ))
    per_stratum = dict(sorted(Counter(
        f"k{row['key'][0]}" for row in rows
    ).items()))
    landed_keys = set()
    for key, _moment in orbit_record_events:
        if len(key) == 2:
            landed_keys.add((2, key[0], key[1]))
        else:
            landed_keys.add(key)
    first_keys = set(first)
    extra_keys = first_keys - landed_keys
    missing_landed = landed_keys - first_keys
    cycle_rows = tuple(
        {
            "key": key,
            "first_clean_boundary": dict(first[key]),
        }
        for key in sorted(certified_cycle_keys)
        if key in first
    )
    zero_cycle_keys = tuple(
        key for key in sorted(certified_cycle_keys)
        if key not in first
    )
    initial_higher = tuple(sorted(
        key for key in initial_clean if key[0] > 2
    ))
    result = {
        "audited_key_count": 228,
        "audited_key_breakdown": {"k2": 176, "higher_k": 52},
        "record_count": len(rows),
        "per_stratum_record_count": per_stratum,
        "all_58_transients": rows,
        "landed_orbit_record_count": len(landed_keys),
        "landed_keys_are_subset": not missing_landed,
        "extra_over_landed_count": len(extra_keys),
        "extra_over_landed_keys": tuple(sorted(extra_keys)),
        "missing_landed_keys": tuple(sorted(missing_landed)),
        "reclassified_cycle_count": len(cycle_rows),
        "eleven_reclassified_cycles": cycle_rows,
        "remaining_zero_record_cycle_count": len(zero_cycle_keys),
        "remaining_zero_record_cycle_keys": zero_cycle_keys,
        "t0_clean_higher_k_count": len(initial_higher),
        "t0_clean_higher_k_keys": initial_higher,
        "recomposition_failures": tuple(recomposition_failures),
        "record_set_sha256": digest(rows),
        "cycle_classification_sha256": digest(
            (cycle_rows, zero_cycle_keys)
        ),
    }
    result["pass"] = (
        result["audited_key_count"] == len(groups) * 4 == 228
        and result["record_count"] == 58
        and sum(per_stratum.values()) == 58
        and result["landed_orbit_record_count"] == 15
        and result["landed_keys_are_subset"]
        and result["extra_over_landed_count"] == 43
        and not result["missing_landed_keys"]
        and result["reclassified_cycle_count"] == 11
        and result["remaining_zero_record_cycle_count"] == 9
        and result["t0_clean_higher_k_count"] > 0
        and not result["recomposition_failures"]
    )
    return result


def fixed_period_rows(
    family: dict[str, object],
    *,
    k: int,
    positions0: tuple[int, ...],
    period: int,
) -> tuple[dict[str, object], ...]:
    states = initial_states_for_positions(family, positions0)
    initial_columns = bit_slice(states)
    columns = list(initial_columns)
    operations = compile_word(synchronous_word(family["program"], positions0))
    width = len(states)
    clean_ever = clean_lane_mask(
        columns, family["dirty_indices"], width
    )
    divisor_returns = [list() for _lane in range(width)]
    divisors = frozenset(proper_divisors(period))
    for moment in range(1, period + 1):
        apply_compiled_bit_slice(columns, operations, width)
        clean_ever |= clean_lane_mask(
            columns, family["dirty_indices"], width
        )
        if moment in divisors:
            equal = equal_lane_mask(columns, initial_columns, width)
            for lane in range(width):
                if equal & (1 << lane):
                    divisor_returns[lane].append(moment)
    returns = equal_lane_mask(columns, initial_columns, width)
    rows = []
    for event in range(width):
        row = {
            "key": (k, positions0, event),
            "entry": 0,
            "period": period,
            "full_state_recurrence": bool(returns & (1 << event)),
            "proper_divisor_returns": tuple(divisor_returns[event]),
            "all_cycle_phases_nonclean":
                not bool(clean_ever & (1 << event)),
            "record_count_under_edit": 0,
        }
        row["pass"] = (
            row["full_state_recurrence"]
            and not row["proper_divisor_returns"]
            and row["all_cycle_phases_nonclean"]
        )
        rows.append(row)
    return tuple(rows)


def verify_higher_certified_cycles(
    family: dict[str, object],
) -> dict[str, object]:
    representatives = higher_k_representatives()
    k3_rows = tuple(
        row
        for positions0 in representatives[3]
        for row in fixed_period_rows(
            family, k=3, positions0=positions0, period=5952
        )
        if row["full_state_recurrence"]
    )
    k4_keys = (
        (4, (0, 2, 4, 7), 1),
        (4, (0, 2, 4, 8), 1),
    )
    k4_groups = {
        positions0: fixed_period_rows(
            family, k=4, positions0=positions0, period=4464
        )
        for _k, positions0, _event in k4_keys
    }
    k4_rows = tuple(
        k4_groups[positions0][event]
        for _k, positions0, event in k4_keys
    )
    result = {
        "Cycle818_citation":
            LINEAGE["Cycle818_cross_stratum_cycle_inventory"],
        "strict_14_interpretation":
            "12 k2 rows plus 2 k4 rows",
        "Cycle801_extra_k3_rows": k3_rows,
        "Cycle814_k4_rows": k4_rows,
        "higher_cycle_count": len(k3_rows) + len(k4_rows),
        "union_818_distinct_cycle_count":
            12 + len(k3_rows) + len(k4_rows),
    }
    result["pass"] = (
        len(k3_rows) == 4
        and all(
            row["period"] == 5952 and row["pass"]
            for row in k3_rows
        )
        and len(k4_rows) == 2
        and all(
            row["period"] == 4464 and row["pass"]
            for row in k4_rows
        )
        and result["union_818_distinct_cycle_count"] == 18
    )
    return result


def single_source_family() -> dict[str, object]:
    rows = []
    battery_failures = []
    directions = Counter()
    for bank_count in FULL_FAMILY_BANK_COUNTS:
        program = K.interleaved_program(bank_count)
        banks, links = K.B.chain_genesis(bank_count)
        state = K.M.pack_state(banks, links)
        allocator = K.M.global_allocator_word(bank_count)
        dirty_indices = dirty_global_indices(bank_count)
        for event in range(2 * bank_count):
            direction = (1, 0) if event % 2 == 0 else (0, 1)
            before = K.M.prepare_endpoint(state, direction)
            after, rail_a, rail_b, trace = K.run_orbit(before, program)
            restored, inverse_a, inverse_b, _ = K.run_orbit(
                after, program, reverse=True
            )
            conditions = {
                "synchronous_composition":
                    after == K.A.apply_semantic(before, allocator),
                "token_rail_return":
                    rail_a == (1,) + (0,) * (len(program) - 1)
                    and not any(rail_b),
                "literal_inverse": (
                    restored == before
                    and inverse_a == rail_a
                    and inverse_b == rail_b
                ),
                "census_membership": True,
                "pairwise_separation": True,
                "synchronization": len(trace) == len(program),
                "clean_postimage":
                    not any(after[index] for index in dirty_indices),
            }
            if not all(conditions.values()):
                battery_failures.append(
                    (bank_count, event, conditions)
                )
            rows.append({
                "banks": bank_count,
                "event": event,
                "direction": direction,
                "first_clean_selector_moment": 0,
                "record_forms_under_edit": all(conditions.values()),
            })
            directions[direction] += 1
            state = after
    expected_identity = tuple(
        (bank_count, event, 0)
        for bank_count in FULL_FAMILY_BANK_COUNTS
        for event in range(2 * bank_count)
    )
    result = {
        "events": tuple(rows),
        "event_count": len(rows),
        "battery_failures": tuple(battery_failures),
        "direction_balance": tuple(sorted(directions.items())),
        "event_identity_sha256": digest(expected_identity),
        "Cycle788_citation": LINEAGE["Cycle788_46_event_extension"],
        "Cycle793_citation": LINEAGE["Cycle793_46_event_balance"],
    }
    result["pass"] = (
        result["event_count"] == 46
        and not result["battery_failures"]
        and all(row["record_forms_under_edit"] for row in rows)
        and sorted(directions.values()) == [23, 23]
    )
    return result


def json_line(payload: bytes, prefix: str) -> Any:
    rows = [
        line[len(prefix):].strip()
        for line in payload.decode("utf-8").splitlines()
        if line.startswith(prefix)
    ]
    if len(rows) != 1:
        raise AssertionError(("cache JSON line", prefix, len(rows)))
    return json.loads(rows[0])


def cache_facts(payloads: dict[str, bytes]) -> dict[str, object]:
    cache796 = payloads[AUDIT_INPUT_PATHS[6]]
    cache820 = payloads[AUDIT_INPUT_PATHS[7]]
    report796 = json_line(cache796, "REPORT :: ")
    arithmetic820 = json_line(cache820, "CERTIFICATE_A_ARITHMETIC=")
    trajectory820 = json_line(cache820, "CERTIFICATE_B_TRAJECTORY=")
    controls820 = json_line(cache820, "CERTIFICATE_F_CONTROLS=")
    report820 = json_line(cache820, "REPORT=")
    earlier_rows = arithmetic820["inventory"]["earlier_moments"]
    return {
        "cache796": {
            "sha256": sha256(cache796).hexdigest(),
            "terminal": report796["terminal"],
            "acceptance_keys": tuple(
                (
                    int(row[0]),
                    tuple(int(value) for value in row[1]),
                    int(row[2]),
                )
                for row in report796["acceptance_keys"]
            ),
            "acceptance_moments":
                tuple(int(value) for value in report796["acceptance_moments"]),
            "classification_counts": report796["classification_counts"],
            "pass": report796["pass"],
        },
        "cache820": {
            "sha256": sha256(cache820).hexdigest(),
            "terminal": report820["terminal"],
            "target_moment": int(report820["target_moment"]),
            "nine_key_count": int(report820["nine_key_count"]),
            "earlier_moments":
                tuple(int(row[1]) for row in earlier_rows),
            "family_sha256":
                controls820["family_reimplementation"]["family_sha256"],
            "first_clean": tuple(
                (
                    (
                        int(row[0][0]),
                        tuple(int(value) for value in row[0][1]),
                    ),
                    int(row[1]),
                )
                for row in trajectory820["first_clean"]
            ),
            "pass": report820["pass"],
        },
    }


def occurrence_replay(payloads: dict[str, bytes]) -> dict[str, object]:
    tree819 = ast.parse(
        payloads[AUDIT_INPUT_PATHS[4]], filename=AUDIT_INPUT_PATHS[4]
    )
    tree820 = ast.parse(
        payloads[AUDIT_INPUT_PATHS[5]], filename=AUDIT_INPUT_PATHS[5]
    )
    expected_cycles = dict(literal_assignment(tree819, "EXPECTED_CYCLES"))
    late_keys = tuple(literal_assignment(tree820, "NINE_KEYS"))
    new_cycle_keys = tuple(sorted(literal_assignment(tree820, "NEW_CYCLE_KEYS")))
    expected_earlier_moments = tuple(
        literal_assignment(tree820, "EARLIER_MOMENTS")
    )
    expected_target = literal_assignment(tree820, "TARGET_MOMENT")

    family = build_k2_family()
    early_k2_first = scan_early_first_clean(family)
    early_higher_first = replay_higher_k_selections(family)
    late_first = scan_late_first_clean(family, late_keys)
    old_cycle_rows = verify_old_cycles(family, expected_cycles)
    higher_cycle_inventory = verify_higher_certified_cycles(family)
    new_cycle_rows = verify_new_cycles(family, new_cycle_keys)
    singles = single_source_family()

    early_k2_events = tuple(
        (key, moment)
        for key, moment in sorted(
            early_k2_first.items(), key=lambda row: (row[1], row[0])
        )
    )
    early_higher_events = tuple(
        (key, moment)
        for key, moment in sorted(
            early_higher_first.items(),
            key=lambda row: (
                TARGET_MOMENT + 1 if row[1] is None else row[1],
                row[0],
            ),
        )
        if moment is not None
    )
    early_events = tuple(sorted(
        early_k2_events + early_higher_events,
        key=lambda row: (row[1], row[0]),
    ))
    late_events = tuple(
        (key, moment)
        for key, moment in sorted(late_first.items())
        if moment is not None
    )
    all_events = early_events + late_events
    record_events = tuple(all_events)
    certified_cycle_keys = tuple(sorted(
        tuple(
            (2, key[0], key[1])
            for key in expected_cycles
        )
        + tuple(
            (2, key[0], key[1])
            for key in new_cycle_keys
        )
        + tuple(
            (row["key"][0], row["key"][2], row["key"][1])
            for row in (
                higher_cycle_inventory["Cycle801_extra_k3_rows"]
                + higher_cycle_inventory["Cycle814_k4_rows"]
            )
        )
    ))
    every_h = every_h_occurrence_census(
        family, record_events, certified_cycle_keys
    )
    result = {
        "k2_family": family["summary"],
        "two_early_k2_first_clean_events": early_k2_events,
        "four_early_higher_k_first_clean_events": early_higher_events,
        "six_early_first_clean_events": early_events,
        "nine_merger_first_clean_events": late_events,
        "all_fifteen_selection_events": all_events,
        "record_events_under_edit": record_events,
        "record_set_equals_first_clean_event_set":
            record_events == all_events,
        "E1_every_H": every_h,
        "certified_cycle_keys": certified_cycle_keys,
        "early_moments": tuple(moment for _key, moment in early_events),
        "late_moment_census":
            dict(sorted(Counter(moment for _key, moment in late_events).items())),
        "old_certified_cycle_rows": old_cycle_rows,
        "higher_certified_cycle_inventory": higher_cycle_inventory,
        "new_certified_cycle_rows": new_cycle_rows,
        "zero_record_certified_cycle_count":
            sum(
                row["record_count_under_edit"] == 0
                for row in (
                    old_cycle_rows
                    + higher_cycle_inventory["Cycle801_extra_k3_rows"]
                    + higher_cycle_inventory["Cycle814_k4_rows"]
                    + new_cycle_rows
                )
            ),
        "single_source_family": singles,
        "expected_earlier_moments": expected_earlier_moments,
        "expected_higher_k_transients":
            tuple(sorted(EXPECTED_HIGHER_K_TRANSIENTS.items())),
        "expected_target_moment": expected_target,
    }
    result["pass"] = (
        family["summary"]["pass"]
        and len(early_events) == 6
        and len(early_k2_events) == 2
        and dict(early_higher_events) == EXPECTED_HIGHER_K_TRANSIENTS
        and result["early_moments"] == expected_earlier_moments
        and len(late_events) == 9
        and set(key for key, _moment in late_events) == set(late_keys)
        and result["late_moment_census"] == {expected_target: 9}
        and len(all_events) == 15
        and result["record_set_equals_first_clean_event_set"]
        and len(old_cycle_rows) == 12
        and len(new_cycle_rows) == 2
        and higher_cycle_inventory["pass"]
        and all(row["pass"] for row in old_cycle_rows + new_cycle_rows)
        and result["zero_record_certified_cycle_count"] == 20
        and singles["pass"]
        and every_h["pass"]
    )
    return result


def certificate_b_occurrences(
    replay: dict[str, object],
) -> dict[str, object]:
    certified_rows = (
        replay["old_certified_cycle_rows"]
        + replay["higher_certified_cycle_inventory"][
            "Cycle801_extra_k3_rows"
        ]
        + replay["higher_certified_cycle_inventory"]["Cycle814_k4_rows"]
        + replay["new_certified_cycle_rows"]
    )
    result = {
        "certificate": "B",
        "candidate": "E2",
        "candidate_edit": E2_CANDIDATE_EDIT,
        "frozen_minimal_wording": E2_CANDIDATE_EDIT,
        "plain_reading": E2_READING,
        "Cycle796_cadence_identification": {
            "path": AUDIT_INPUT_PATHS[2],
            "cadence": "orbit_return_boundary",
            "landed_cadences": LANDED_CADENCES_796,
        },
        "conditional_status":
            "conditional on accepted new axiom; not retained on the actual "
            "current surface",
        "record_rule":
            "record set = first-clean orbit-return selection-event set",
        "six_early_first_clean_events":
            replay["six_early_first_clean_events"],
        "nine_merger_first_clean_events":
            replay["nine_merger_first_clean_events"],
        "all_fifteen_transients_at_orbit_moments":
            replay["all_fifteen_selection_events"],
        "fifteen_event_count":
            len(replay["all_fifteen_selection_events"]),
        "zero_record_certified_cycle_count":
            replay["zero_record_certified_cycle_count"],
        "twenty_zero_record_cycles": certified_rows,
        "Cycle818_cross_stratum_inventory":
            replay["higher_certified_cycle_inventory"],
        "single_source_46": replay["single_source_family"],
        "landed_identifications": {
            "early_battery": "Cycles 796/819",
            "late_cache_and_mechanism": "Cycles 819/820",
            "single_source_batteries": "Cycles 788/793",
        },
        "record_set_relation": "EXACTLY_LANDED_FAMILY",
    }
    result["pass"] = (
        replay["pass"]
        and result["fifteen_event_count"] == 15
        and result["zero_record_certified_cycle_count"] == 20
        and len(result["twenty_zero_record_cycles"]) == 20
        and all(
            row["record_count_under_edit"] == 0
            for row in result["twenty_zero_record_cycles"]
        )
        and result["single_source_46"]["pass"]
        and result["single_source_46"]["event_count"] == 46
    )
    return result


def certificate_c_neutrality(
    replay: dict[str, object],
    repeat: dict[str, object],
    caches: dict[str, object],
    sources_before: dict[str, str],
    sources_after: dict[str, str],
) -> dict[str, object]:
    every_h = replay["E1_every_H"]
    orbit_transients = replay["all_fifteen_selection_events"]
    orbit_cycles = replay["certified_cycle_keys"]
    deterministic = (
        digest(replay) == digest(repeat)
        and every_h == repeat["E1_every_H"]
    )
    census_796 = {
        "battery": "k=2 separated-pair family",
        "key_count": 176,
        "cadences": LANDED_CADENCES_796,
        "cadence_count": 4,
        "reported_classification_counts":
            caches["cache796"]["classification_counts"],
        "finding": "existence is cadence-robust on this landed census",
    }
    census_v2 = {
        "battery": "k=2 plus k=3,4,5 representative strata",
        "key_count": every_h["audited_key_count"],
        "key_breakdown": every_h["audited_key_breakdown"],
        "granularity": "each post-engagement H-station boundary, including t=0",
        "record_count": every_h["record_count"],
        "reclassified_cycle_count":
            every_h["reclassified_cycle_count"],
    }
    sha_comparison = {
        "orbit_transients_sha256": digest(orbit_transients),
        "every_H_transients_sha256":
            every_h["record_set_sha256"],
        "orbit_zero_cycles_sha256": digest(orbit_cycles),
        "every_H_cycle_classification_sha256":
            every_h["cycle_classification_sha256"],
    }
    sha_comparison["transient_diff_nonempty"] = (
        sha_comparison["orbit_transients_sha256"]
        != sha_comparison["every_H_transients_sha256"]
    )
    sha_comparison["cycle_diff_nonempty"] = (
        sha_comparison["orbit_zero_cycles_sha256"]
        != sha_comparison["every_H_cycle_classification_sha256"]
    )
    result = {
        "certificate": "C",
        "finding": "NO_CONTRADICTION_DIFFERENT_CENSUSES",
        "Cycle796_census": census_796,
        "v2_E1_census": census_v2,
        "scope_relation": (
            "Cycle796 compared existence across four landed cadences on the "
            "176-key k=2 battery.  E1 resolves individual H boundaries and "
            "also adds 52 keys from k=3,4,5 strata.  Its enrichment is a "
            "finer-boundary, broader-stratum occurrence census, so it does "
            "not negate Cycle796's scoped cadence-robust existence result."
        ),
        "overlap_relation":
            "The k=2 176-key battery overlaps; the predicates differ: "
            "Cycle796's landed cadence-level existence classification versus "
            "v2's first individual clean H-boundary occurrence latch.",
        "reading_sha_comparison": sha_comparison,
        "cache_sha_level_exact": (
            caches["cache796"]["sha256"] == EXPECTED_SHA256[AUDIT_INPUT_PATHS[6]]
            and caches["cache820"]["sha256"]
            == EXPECTED_SHA256[AUDIT_INPUT_PATHS[7]]
        ),
        "sources_unchanged": sources_before == sources_after,
        "deterministic": deterministic,
        "landed_files_or_certificates_changed": False,
    }
    result["pass"] = (
        replay["pass"]
        and repeat["pass"]
        and result["cache_sha_level_exact"]
        and result["sources_unchanged"]
        and deterministic
        and census_796["key_count"] == 176
        and census_796["cadence_count"] == 4
        and census_v2["key_count"] == 228
        and sha_comparison["transient_diff_nonempty"]
        and sha_comparison["cycle_diff_nonempty"]
        and not result["landed_files_or_certificates_changed"]
    )
    return result


def certificate_f_verdict(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
    certificate_c: dict[str, object],
    certificate_d: dict[str, object],
) -> dict[str, object]:
    summary = (
        {
            "candidate": "E1",
            "answer":
                "both axes fixed; 58 enriched every-H records; 11 landed "
                "cycles reclassified; STILL_FREE allocation",
        },
        {
            "candidate": "E2",
            "answer":
                "both axes fixed; exact landed 15 transient / 20 zero-cycle / "
                "46 single-source family; STILL_FREE allocation",
        },
        {
            "candidate": "shared status",
            "answer":
                "conditional lawful points, each 1 of 8 and non-entailed; "
                "owner leg-1 cadence input required; no axiom-surface write",
        },
    )
    passed = all((
        certificate_a["pass"],
        certificate_b["pass"],
        certificate_c["pass"],
        certificate_d["pass"],
    ))
    return {
        "pass": passed,
        "verdict":
            "TWO_CANDIDATE_EDIT_AUDIT_COMPLETE"
            if passed else "TWO_CANDIDATE_EDIT_AUDIT_INCOMPLETE",
        "summary_table": summary,
        "recommendation": None,
        "decision_owner": "owner",
    }


def render(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    runtime_seconds: float,
    controls: dict[str, object],
) -> str:
    lines = [
        "CYCLE828_V2_TWO_CANDIDATE_EDIT_AUDIT",
        "PROPOSAL_ONLY_NO_AXIOM_SURFACE_MODIFIED",
        "E1_CANDIDATE_EDIT :: " + E1_CANDIDATE_EDIT,
        "E2_CANDIDATE_EDIT :: " + E2_CANDIDATE_EDIT,
    ]
    for label, value in certificates:
        lines.append(
            ("PASS " if value["pass"] else "FAIL ")
            + label + " :: " + compact(value)
        )
    lines.append(
        ("PASS " if controls["pass"] else "FAIL ")
        + "CERTIFICATE_F_CONTROLS :: " + compact(controls)
    )
    verdict = dict(certificates)["CERTIFICATE_E_VERDICT"]
    lines.append("FINAL :: " + compact({
        "verdict": verdict["verdict"],
        "E1_axes": "FIXED_BOTH",
        "E1_occurrences":
            "58_ENRICHED_11_LANDED_CYCLES_RECLASSIFIED",
        "E1_occurrence_neutral": False,
        "E2_axes": "FIXED_BOTH",
        "E2_occurrences": "EXACT_LANDED_15_20_46",
        "allocation_E1": "STILL_FREE",
        "allocation_E2": "STILL_FREE",
        "selection_E1": "1_OF_8_NON_ENTAILED",
        "selection_E2": "1_OF_8_NON_ENTAILED",
        "leg_1": "OWNER_CADENCE_INPUT_REQUIRED_FOR_EACH",
        "landed_artifacts_changed": False,
        "runtime_seconds": round(runtime_seconds, 6),
        "pass": all(value["pass"] for _label, value in certificates)
            and controls["pass"],
    }))
    lines.append(
        "CYCLE828_V2_TWO_CANDIDATE_EDIT_AUDIT_PASS"
        if verdict["verdict"] == "TWO_CANDIDATE_EDIT_AUDIT_COMPLETE"
        and controls["pass"]
        else "CYCLE828_V2_TWO_CANDIDATE_EDIT_AUDIT_FAIL"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    payloads = read_inputs()
    sources_before = {
        name: sha256(payload).hexdigest()
        for name, payload in payloads.items()
    }
    controls = source_controls(payloads)
    caches = cache_facts(payloads)
    replay = occurrence_replay(payloads)
    repeat = occurrence_replay(payloads)
    sources_after_payloads = read_inputs()
    sources_after = {
        name: sha256(payload).hexdigest()
        for name, payload in sources_after_payloads.items()
    }
    certificate_a = certificate_a_axes_collapse(
        replay, sources_before == sources_after
    )
    certificate_b = certificate_b_occurrences(replay)
    certificate_c = certificate_c_neutrality(
        replay, repeat, caches, sources_before, sources_after
    )
    certificate_d = certificate_d_allocation(replay)
    certificate_f = certificate_f_verdict(
        certificate_a,
        certificate_b,
        certificate_c,
        certificate_d,
    )
    certificates = (
        ("CERTIFICATE_A_E1_EVERY_H_TRUTH", certificate_a),
        ("CERTIFICATE_B_E2_ORBIT_REPRODUCTION", certificate_b),
        ("CERTIFICATE_C_CYCLE796_RECONCILIATION", certificate_c),
        ("CERTIFICATE_D_TWO_CANDIDATE_COMPARISON", certificate_d),
        ("CERTIFICATE_E_VERDICT", certificate_f),
    )
    runtime_seconds = monotonic() - started
    controls.update({
        "deterministic": digest(replay) == digest(repeat),
        "sources_unchanged": sources_before == sources_after,
        "runtime_seconds": round(runtime_seconds, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end":
            tuple(name for name in BLOCKLISTED_MODULES if name in sys.modules),
        "blocker_hits_at_end": tuple(PRIMARY_BLOCKER.hits),
    })
    controls["pass"] = (
        controls["pass"]
        and controls["deterministic"]
        and controls["sources_unchanged"]
        and runtime_seconds < AUDIT_TIMEOUT_SEC
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["blocker_hits_at_end"]
    )
    output = render(certificates, runtime_seconds, controls)
    output_bytes = len(output.encode("utf-8"))
    controls["stdout_bytes"] = output_bytes
    controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
    controls["pass"] = controls["pass"] and controls["stdout_within_limit"]
    output = render(certificates, runtime_seconds, controls)
    output_bytes = len(output.encode("utf-8"))
    controls["stdout_bytes"] = output_bytes
    controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
    output = render(certificates, runtime_seconds, controls)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")), STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    passed = (
        all(value["pass"] for _label, value in certificates)
        and controls["pass"]
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
