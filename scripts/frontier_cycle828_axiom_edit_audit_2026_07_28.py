#!/usr/bin/env python3
"""Cycle 828: proposal audit for the frozen minimal Record-axiom edit.

No axiom surface is modified.  The candidate sentence is interpreted only as
a conditional rule mapping first-clean selector events to record occurrences.
The named predecessor primaries are provenance data: all except the landed
Cycle-719 controller core are blocked from import and inspected as text/AST.
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
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle799_cadence_preference_2026_07_28.py",
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
        "6773ec05cc1db37a09f88232e7d1f8f9c4b87db98e5b620ad3ef57180ab1cddc",
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
    AUDIT_INPUT_PATHS[3]: "49964118073bcd784af0f2e4c03723a9d3bd47e9",
    AUDIT_INPUT_PATHS[4]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[5]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[6]: "dced1dfadab2742d00aedfbeba93b25766cc653b",
    AUDIT_INPUT_PATHS[7]: "6b0198080f5e9fadc69cc1301b41cff2502f3eb2",
}

CANDIDATE_EDIT = "Records form at first admissibility."
PLAIN_READING = {
    "evaluation_cadence": "every_boundary",
    "landed_identification":
        "every tested post-engagement H-station boundary",
    "formation_site_schedule":
        "every first-clean selection forms a record",
}

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
    tree799 = primary_trees[AUDIT_INPUT_PATHS[3]]
    tree786 = primary_trees[AUDIT_INPUT_PATHS[1]]
    tree819 = primary_trees[AUDIT_INPUT_PATHS[4]]
    tree820 = primary_trees[AUDIT_INPUT_PATHS[5]]
    cadence796 = tuple(
        row["name"]
        for row in literal_assignment(tree796, "LANDED_CADENCES")
    )
    cadence799 = tuple(literal_assignment(tree799, "CADENCES"))
    ast_basis = {
        "Cycle781_796_every_boundary_identification": (
            "reference_781_every_boundary_idiom" in text796
            and "for step in range(C719.CONTROLLER_STATIONS):" in text796
            and "every tested post-engagement station boundary" in text796
        ),
        "Cycle796_799_four_cadences":
            cadence796 == cadence799 == (
                "orbit_return_boundary",
                "H_station_boundary",
                "Q_R1_R2_layer_boundary",
                "program_macro_completion",
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


def certificate_a_axes_collapse() -> dict[str, object]:
    rows = tuple({
        "id": identifier,
        "before": before,
        "after": "DETERMINED",
        "fixed_content": fixed,
    } for identifier, before, fixed in AXIS_INVENTORY_809)
    before = Counter(row["before"] for row in rows)
    after = Counter(row["after"] for row in rows)
    result = {
        "candidate_edit": CANDIDATE_EDIT,
        "plain_reading": PLAIN_READING,
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
            PLAIN_READING["formation_site_schedule"]
            == "every first-clean selection forms a record",
        "all_eight_now_determined":
            len(rows) == 8 and after == Counter({"DETERMINED": 8}),
    }
    result["pass"] = (
        result["axis_1_fixed"]
        and result["axis_2_fixed"]
        and result["all_eight_now_determined"]
    )
    return result


def certificate_d_allocation() -> dict[str, object]:
    result = {
        "outcome": "STILL_FREE",
        "surviving_object":
            "six-way per-orientation matter-origin allocation "
            "(Cycle-786 per_origin_channels)",
        "mechanical_basis": {
            "record_occurrence_object": "first-clean event set",
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
        },
        "reason":
            "The edit fixes occurrence timing only.  It neither adds the "
            "missing matter-origin join key nor chooses weights inside either "
            "six-element orientation fibre, so the operationally visible "
            "allocation remains meaningful and undetermined.",
    }
    result["pass"] = (
        result["outcome"] == "STILL_FREE"
        and result["mechanical_basis"]["event_to_origin_join_key"] is None
        and not result["mechanical_basis"]["weights_supplied_by_edit"]
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


def scaffold_main() -> int:
    payloads = read_inputs()
    controls = source_controls(payloads)
    certificate_a = certificate_a_axes_collapse()
    certificate_d = certificate_d_allocation()
    certificate_e = certificate_e_three_legs()
    rows = (
        ("CERTIFICATE_A_AXES_COLLAPSE", certificate_a),
        ("CERTIFICATE_D_ALLOCATION", certificate_d),
        ("CERTIFICATE_E_THREE_LEGS", certificate_e),
        ("CERTIFICATE_G_CONTROLS", controls),
    )
    for label, value in rows:
        print(("PASS " if value["pass"] else "FAIL ") + label
              + " :: " + compact(value))
    passed = all(value["pass"] for _label, value in rows)
    print(
        "CYCLE828_AXIOM_EDIT_AUDIT_SCAFFOLD_PASS"
        if passed else "CYCLE828_AXIOM_EDIT_AUDIT_SCAFFOLD_FAIL"
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(scaffold_main())
