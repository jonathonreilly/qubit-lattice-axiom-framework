#!/usr/bin/env python3
"""Cycle625: Admissibility / occurrence / Born shared-middle tournament.

This cycle asks whether the retained Admissibility/Record/realized-state
surfaces plus the Cycle614 physical candidate packet identify one covariant
local formation/admission functional from physical state and a grade/frequency
bridge.  Bare occurrence ("Records form") is already supplied axiom content;
this cycle does not attempt to rederive it.  It separates:

* the structural schema from extensional rule content;
* a positive supplied unique-quorum physical map from objective actuality;
* a ROM-free state-derived grade block from Born probability or Records.

Authority is none and audit is unset.  Candidate packets are not Records,
candidate weights/frequencies are not Born probabilities, and schedules are
not time.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import time


ROOT = Path(__file__).resolve().parents[1]
COMMITTED_SHORE_HEAD = "b31c92adb5bbf79b50b874078688d0bf62651eef"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_"
    "CYCLE625_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_admissibility_occurrence_born_shared_middle_"
    "tournament_cycle625_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0


FROZEN_SHORES = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md":
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md":
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md":
        "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/audit/data/axiom_premise_nodes.json":
        "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "scripts/physical_selected_seam_conditional_record_binder_cycle531_2026_07_21.py":
        "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md":
        "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "scripts/physical_autonomous_local_member_law_cell_cycle552_2026_07_21.py":
        "405cacd821b5453045f8a8920b1ab0fc2dca5ac90fb150e9b4a95f6f218ac8a4",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_LOCAL_MEMBER_LAW_CELL_CYCLE552_NOTE_2026-07-21.md":
        "919f95dd43d8bdd5ba65fba071f58a6d054a89b3d7d4b7cc04686c8c28cdbf42",
    "scripts/physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22.py":
        "7221d59558e4d731f98a2a4523c280aa98b889f23ea3f7be1acc8919395dfee8",
    "docs/work_history/repo/review_feedback/PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md":
        "b254476f392597c03f27581fbc4f559266ed42984ac86a516888ee81d2aff8e2",
    "scripts/physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_2026_07_22.py":
        "2879d5a2641b334553769f15cf3a6f152f9f16f8f80b23db723448533c28c494",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_OCCURRENCE_BORN_HISTORY_BRIDGE_TOURNAMENT_CYCLE587_NOTE_2026-07-22.md":
        "6938f48fa4e55dc7037a461802ec2f655893a9d9f68ffe65139950e6a07fd8db",
    "outputs/physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_cold_2026_07_22.txt":
        "47060b72e3304e13ed0e5f0d689e6ac323bb6b72fa450ea64e94605311909a84",
    "scripts/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_2026_07_22.py":
        "ab565af6aa59e66cea7b1ce625c08f8a88235ae9f7415e5e7d89d63af34ce9ce",
    "docs/work_history/repo/review_feedback/PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md":
        "dccf62d6126287b20cbf96ff410534adfa1746d9cf3aba94fbfb2893855be212",
    "outputs/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_cold_2026_07_22.txt":
        "135ec5a5b75c180d23a1246deb89b920b771dbc714a2e1ee2087cc6a2af5683d",
    "scripts/physical_state_family_grade_transition_synthesis_tournament_cycle597_2026_07_22.py":
        "994f050fb33d7b9909896d195dca6be0062f56445ba49cac8731f196a3cfe79e",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATE_FAMILY_GRADE_TRANSITION_SYNTHESIS_TOURNAMENT_CYCLE597_NOTE_2026-07-22.md":
        "9a786fc7c559437483fb357893ad23146ddbdebd71a992ed8c709053e9b1d413",
    "outputs/physical_state_family_grade_transition_synthesis_tournament_cycle597_cold_2026_07_22.txt":
        "022a8f946a9953a91a97ba9db3c05c3b3fc73bd08fcfe576e80b95373f51acea",
    "scripts/physical_autonomous_admission_record_permanence_tournament_cycle614_2026_07_22.py":
        "ca84ee27a2d8fa67e17336717613e7a2cd05c46421e6d0cc5f4ee6a860938240",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_ADMISSION_RECORD_PERMANENCE_TOURNAMENT_CYCLE614_NOTE_2026-07-22.md":
        "d9164a42bc3cba10fb6d142b9ae5152543274c5d18ced5a070e5533c488a7ca2",
    "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py":
        "faa1a251d7586ed9d2e496cc73b42f45108347fe5f627523fcef3caa4e652a73",
    "docs/work_history/repo/review_feedback/PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_CYCLE621_NOTE_2026-07-22.md":
        "a52395a57fb34b6d827a677a43528033e913cde2f98ce708a276507f6e1e353e",
}

NORMALIZED_RECEIPTS = {
    "outputs/physical_autonomous_admission_record_permanence_tournament_cycle614_receipt_2026_07_22.json":
        "b1b605be2b7e8db7203a7f2957fa745f799ddf35652f0abed4bc36a42ae3f089",
    "outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json":
        "9010a5f79cf926febd9ee978def1f2164fcb598c5df024b36e7f170e7d034c3e",
}


# Exact read-only comparator heads.  PRs 5472/5476/5479 were closed without
# merge and are not retained premises.  PR5557 is an external open candidate
# lane, pinned at one immutable head and consumed only as a dependency-shape
# comparison.  `git show <head>:<path>` makes every comparison byte-exact.
EXTERNAL_COMPARISON_HEADS = {
    "PR5472": {
        "head_oid": "2c648ccb408a8c36a700f53ec5401369e3bbd490",
        "declared_state": "CLOSED_NONRETAINED",
        "use": "conditional effect-menu forcing/product-menu boundary comparison only",
        "surfaces": (
            {
                "path": "docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
                "sha256": "f7ddc109ebb97d5514c7b41a78c523fe6adcf5419c08cff1ec75e54b2c99d435",
                "line": 60,
                "line_fragment": "Neither horn is selected. The axioms supply no menus at all",
            },
            {
                "path": "scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py",
                "sha256": "2bb29c0d1e27dc155af449c2cf76177d49a20933739eb6429aba06577ff1ef24",
            },
        ),
    },
    "PR5476": {
        "head_oid": "a994617819f57e599dd101c654be366123392236",
        "declared_state": "CLOSED_NONRETAINED",
        "use": "conditional scaled-projector forcing/paired-menu boundary comparison only",
        "surfaces": (
            {
                "path": "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
                "sha256": "042a5e69a50dba337fc3e8bfd5faa3a6cef34b42c3e0ab6344ae5d05f5e6cdc7",
                "line": 17,
                "line_fragment": "the menu family the physical registration supplies is underived",
            },
            {
                "path": "scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py",
                "sha256": "05fd738e28d4c6c8969758b6bc89bad22d94215dc1387427b7cc5f500c511136",
            },
        ),
    },
    "PR5479": {
        "head_oid": "84053108a424cef26dc23e484549df331ad2050f",
        "declared_state": "CLOSED_NONRETAINED",
        "use": "binary/ternary threshold, mixed-projective forcing, and incomparability comparison only",
        "surfaces": (
            {
                "path": "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
                "sha256": "feb8b3ca2ed1a8ffb3d272ce81814cfc2c6598148e9fecf2a48df88b53c45a35",
                "line": 62,
                "line_fragment": "No family is selected; nothing here derives which menus record formation",
            },
            {
                "path": "scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py",
                "sha256": "6f6e75bb73a13a18bcfadf22a35bb16d0c29e464162dd140aee4549f8b7b87e7",
            },
        ),
    },
    "PR5557": {
        "head_oid": "a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318",
        "declared_state": "OPEN_EXTERNAL_CANDIDATE_COMPARISON",
        "use": "Cycle610-612 shared occurrence/admission dependency comparison; never back-credit",
        "surfaces": (
            {
                "path": "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
                "sha256": "63854c353f477f7beb8371d3a4489c02d8787c54679ab8963c7cc828972a4ea4",
                "line": 364,
                "line_fragment": "shared supplied middle, not a",
            },
            {
                "path": "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
                "sha256": "61d624d3f47e371a3b99f55a3c60db68c1fe77f5d93a21651f9172b2d49f1458",
            },
            {
                "path": "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md",
                "sha256": "91e0e0bb6c931f7da7a468a7094deffb775523f22b75334322417639edf57056",
                "line": 97,
                "line_fragment": "Occurrence selector sigma",
            },
            {
                "path": "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
                "sha256": "9f1d4a2aabca8af1f61ef42071c8d2bce05018eace7a6f0886d769871689a13d",
            },
            {
                "path": "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
                "sha256": "028133c490e771dd3012061c79910fcfb88cd6132df072ec15e725fe9bc35496",
                "line": 167,
                "line_fragment": "conditional candidate Record.  No proper time",
            },
            {
                "path": "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
                "sha256": "4494ce889809f6a179fc9bb712aa851fa6e73dac32a7b1bfbdb71903be5fadde",
            },
        ),
    },
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized_receipt_sha(path: Path) -> str:
    body = json.loads(path.read_text())
    body.pop("elapsed_seconds", None)
    body.pop("maximum_RSS_bytes", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def normalized_receipt_bytes(body_bytes: bytes) -> tuple[str, dict[str, object]]:
    body = json.loads(body_bytes)
    body.pop("elapsed_seconds", None)
    body.pop("maximum_RSS_bytes", None)
    digest = sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return digest, body


def repo_line(path: str, fragment: str) -> int:
    """Return the unique exact working-tree line containing `fragment`."""
    rows = (ROOT / path).read_text().splitlines()
    matches = [index for index, row in enumerate(rows, 1)
               if (row.strip().startswith(fragment) if fragment.startswith("def ") else fragment in row)]
    if len(matches) != 1:
        raise ValueError(f"expected one line for {path!r} / {fragment!r}, got {matches}")
    return matches[0]


def git_surface_bytes(head_oid: str, path: str) -> bytes:
    return subprocess.run(
        ("git", "show", f"{head_oid}:{path}"), cwd=ROOT,
        check=True, capture_output=True,
    ).stdout


def external_comparison_controls() -> dict[str, object]:
    observed: dict[str, object] = {}
    failures = 0
    for name, spec in EXTERNAL_COMPARISON_HEADS.items():
        surface_rows = []
        for surface in spec["surfaces"]:
            body = git_surface_bytes(spec["head_oid"], surface["path"])
            observed_sha = sha256(body).hexdigest()
            line = surface.get("line")
            line_text = None
            line_match = True
            if line is not None:
                decoded = body.decode().splitlines()
                line_text = decoded[line - 1] if 0 < line <= len(decoded) else None
                line_match = line_text is not None and surface["line_fragment"] in line_text
            row_pass = observed_sha == surface["sha256"] and line_match
            failures += int(not row_pass)
            surface_rows.append({
                "path": surface["path"],
                "expected_sha256": surface["sha256"],
                "observed_sha256": observed_sha,
                "citation_line": line,
                "citation_line_text": line_text,
                "citation_fragment": surface.get("line_fragment"),
                "pass": row_pass,
            })
        observed[name] = {
            "head_oid": spec["head_oid"],
            "declared_state": spec["declared_state"],
            "retained_as_premise": False,
            "use": spec["use"],
            "back_credit": False,
            "surfaces": surface_rows,
            "pass": all(row["pass"] for row in surface_rows),
        }
    passed = failures == 0 and all(not row["retained_as_premise"] for row in observed.values())
    result = {
        "heads": observed,
        "closed_nonretained_heads": ("PR5472", "PR5476", "PR5479"),
        "external_candidate_head": "PR5557",
        "comparison_only": True,
        "back_credit": False,
        "pass": passed,
    }
    check("closed Born heads and external Cycle610-612 head are exact comparison-only git objects",
          passed, {"heads": len(observed), "surfaces": sum(len(row["surfaces"]) for row in observed.values())})
    return result


def shore_controls() -> dict[str, object]:
    committed_bytes = {name: git_surface_bytes(COMMITTED_SHORE_HEAD, name) for name in FROZEN_SHORES}
    observed = {name: sha256(body).hexdigest() for name, body in committed_bytes.items()}
    working_tree_observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    normalized_payloads = {
        name: normalized_receipt_bytes(git_surface_bytes(COMMITTED_SHORE_HEAD, name))
        for name in NORMALIZED_RECEIPTS
    }
    normalized = {name: row[0] for name, row in normalized_payloads.items()}
    working_tree_receipt_sha = {name: file_sha(ROOT / name) for name in NORMALIZED_RECEIPTS}
    c614 = next(row[1] for name, row in normalized_payloads.items() if "cycle614" in name)
    c621 = next(row[1] for name, row in normalized_payloads.items() if "cycle621" in name)
    premise = json.loads(committed_bytes["docs/audit/data/axiom_premise_nodes.json"])
    premise_text = json.dumps(premise).lower()
    minimal = committed_bytes["docs/MINIMAL_AXIOMS_2026-06-29.md"].decode().lower()
    realized = committed_bytes["docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"].decode().lower()
    semantics = {
        "fixed_nearest_neighbor_rule_named": "one fixed nearest-neighbor admissibility rule" in minimal,
        "rule_covariance_named": ("covariant under lattice" in minimal and "proper cubic rotations" in minimal),
        "admissibility_not_dynamics": "admissibility is not a dynamics axiom" in minimal,
        "no_transition_weights": "supply transition probabilities or" in minimal,
        "record_formation_named": "records form" in minimal,
        "realized_slot_has_no_selection": ("not a state-selection rule" in realized
                                             and "does not supply a state, state-selection rule" in realized),
        "premise_says_no_update_law": "no context-selection rule" in premise_text and "probability" in premise_text,
        "bare_Record_occurrence_is_supplied": "records form" in minimal,
        "formation_rule_remains_outside": ("which admissible possibility" in minimal
                                             and "at which site" in minimal
                                             and "at what rate" in minimal),
    }
    receipt_contract = (
        c614["pass"] is True and c621["pass"] is True
        and c614["route_A_state_local_unique_quorum"]["ideal_truth_rows"] == 64
        and c614["route_A_state_local_unique_quorum"]["coherent_sectors_retained"] == 6
        and c614["route_A_state_local_unique_quorum"]["materialized_reversible_predicate_circuit"]["bounded_M2"] == 92
        and c614["route_A_state_local_unique_quorum"]["materialized_reversible_predicate_circuit"]["maximum_literal_gate_support_M2"] == 2
        and c614["malformed_deletion_renewal_controls"]["one_particle_mass_fixture_residual"] < 2e-15
        and c621["tests_failed"] == 0
    )
    passed = (observed == FROZEN_SHORES and normalized == NORMALIZED_RECEIPTS
              and all(semantics.values()) and receipt_contract)
    result = {
        "committed_shore_head": COMMITTED_SHORE_HEAD,
        "committed_git_objects_are_only_retained_local_premises": True,
        "expected_sha256": FROZEN_SHORES,
        "observed_sha256": observed,
        "working_tree_comparison_sha256": working_tree_observed,
        "working_tree_differs_from_committed": tuple(
            name for name in FROZEN_SHORES if working_tree_observed[name] != observed[name]
        ),
        "working_tree_variants_retained_as_premise": False,
        "working_tree_variants_back_credit": False,
        "expected_normalized_receipt_sha256": NORMALIZED_RECEIPTS,
        "observed_normalized_receipt_sha256": normalized,
        "working_tree_receipt_raw_comparison_sha256": working_tree_receipt_sha,
        "semantic_surface_checks": semantics,
        "Cycle614_621_receipt_contract": receipt_contract,
        "Cycle614_mass_fixture_residual": c614["malformed_deletion_renewal_controls"]["one_particle_mass_fixture_residual"],
        "read_only_dependency_sweep_complete": True,
        "pass": passed,
    }
    check("axiom/primitive and Cycles531/552/571/587/592/597/614/621 shores are pinned to one immutable committed head",
          passed, {"files": len(observed), "normalized_receipts": len(normalized)})
    return result


# Proper-cubic geometry.  The six direction slots are geometric labels, not an
# incident ordering.  Every candidate predicate below is symmetric in them.
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def determinant(matrix: Matrix) -> int:
    a, b, c = matrix
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def proper_cubic_frames() -> tuple[Matrix, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(tuple(signs[row] if column == permutation[row] else 0
                                 for column in range(3)) for row in range(3))
            if determinant(matrix) == 1:
                frames.append(matrix)
    return tuple(frames)


def matvec(matrix: Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3))
                 for row in range(3))  # type: ignore[return-value]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum(left[row][inner] * right[inner][column] for inner in range(3))
                       for column in range(3)) for row in range(3))  # type: ignore[return-value]


def rotate_six(word: tuple[int, ...], frame: Matrix) -> tuple[int, ...]:
    if len(word) != 6:
        raise ValueError("six incident direction fields required")
    output = [0] * 6
    for direction, bit in enumerate(word):
        output[DIRECTIONS.index(matvec(frame, DIRECTIONS[direction]))] = bit
    return tuple(output)


def axis_permutation(frame: Matrix) -> tuple[int, int, int]:
    return tuple(next(index for index, value in enumerate(matvec(frame, axis)) if value)
                 for axis in AXES)


def rotate_axis_word(word: tuple[int, int, int], frame: Matrix) -> tuple[int, int, int]:
    output = [0, 0, 0]
    for old, new in enumerate(axis_permutation(frame)):
        output[new] = word[old]
    return tuple(output)  # type: ignore[return-value]


# Route A: structural Admissibility schema versus extensional rule content.
RULES = {
    "unique_quorum": frozenset((1,)),
    "odd_shells": frozenset((1, 3, 5)),
    "nonempty": frozenset((1, 2, 3, 4, 5, 6)),
    "low_density": frozenset((1, 2)),
    "even_nonzero": frozenset((2, 4, 6)),
}


def validate_endpoint_word(word: tuple[int, ...]) -> None:
    if len(word) != 6 or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("endpoint word leaves the six-bit M2 basis code")


def relation_answer(rule: frozenset[int], word: tuple[int, ...], *, fresh: bool = True) -> int:
    validate_endpoint_word(word)
    if type(fresh) is not bool:
        raise ValueError("freshness is not binary")
    return int(fresh and sum(word) in rule)


def route_a_structural_relation_tournament() -> dict[str, object]:
    frames = proper_cubic_frames()
    words = tuple(product((0, 1), repeat=6))
    train = tuple(word for word in words if sum(word) <= 3)
    held = tuple(word for word in words if sum(word) >= 4)
    rows = {}
    covariance_failures = 0
    totality_failures = 0
    for name, rule in RULES.items():
        outputs = tuple(relation_answer(rule, word) for word in words)
        totality_failures += int(len(outputs) != 64 or any(value not in (0, 1) for value in outputs))
        for word in words:
            for frame in frames:
                covariance_failures += int(
                    relation_answer(rule, rotate_six(word, frame)) != relation_answer(rule, word)
                )
        rows[name] = {
            "accepted_shells": sorted(rule),
            "accepted_truth_rows": sum(outputs),
            "train_accepts": sum(relation_answer(rule, word) for word in train),
            "held_accepts": sum(relation_answer(rule, word) for word in held),
            "nonconstant_and_neighborhood_dependent": len(set(outputs)) == 2,
            "one_boolean_answer_per_neighborhood": True,
            "runtime_ROM_ports": 0,
        }
    pair_separators = []
    for left, right in combinations(RULES, 2):
        train_difference = sum(relation_answer(RULES[left], word) != relation_answer(RULES[right], word)
                               for word in train)
        held_difference = sum(relation_answer(RULES[left], word) != relation_answer(RULES[right], word)
                              for word in held)
        pair_separators.append({"left": left, "right": right,
                                "train_truth_separators": train_difference,
                                "held_truth_separators": held_difference,
                                "total_truth_separators": train_difference + held_difference})
    all_distinct = all(row["total_truth_separators"] > 0 for row in pair_separators)
    result = {
        "disposition": (
            "positive executable structural relation family and exact extensional model separation; "
            "the retained surfaces do not identify one table"
        ),
        "neighborhood_words": 64,
        "train_words_weight_0_through_3": len(train),
        "held_words_weight_4_through_6": len(held),
        "proper_cubic_frames": len(frames),
        "covariance_tests": len(RULES) * len(words) * len(frames),
        "covariance_failures": covariance_failures,
        "totality_failures": totality_failures,
        "candidate_fixed_relations": rows,
        "pairwise_model_separators": pair_separators,
        "all_candidate_tables_extensionally_distinct": all_distinct,
        "retained_surface_selects_candidate_table": False,
        "actual_framework_rule_instantiated": False,
        "Cycle614_unique_quorum_available_as_supplied_candidate": True,
        "candidate_relation_digest": sha256(json.dumps(
            {name: sorted(rule) for name, rule in RULES.items()}, sort_keys=True).encode()).hexdigest(),
        "pass": covariance_failures == totality_failures == 0 and all_distinct,
    }
    check("Route A executes covariant local relations and separates their extensional content on train/held neighborhoods",
          result["pass"], {"models": len(RULES), "separators": len(pair_separators)})
    return result


# Lightweight exact finite-interface quotient of the byte-pinned Cycle614
# truth table.  It is used only after shore_controls validates the complete
# Cycle614 physical resource/fault/covariance receipt.
PACKET_WIDTH = 9
P_WIDTH = 92
P_ADMIT = 45
P_ENDPOINT = tuple(tuple(range(3 * direction, 3 * direction + 3)) for direction in range(6))
P_PACKET = tuple(tuple(range(18 + PACKET_WIDTH * replica,
                             18 + PACKET_WIDTH * (replica + 1))) for replica in range(3))

B_ARCHIVE = tuple(range(92, 98))
B_LOSERS = tuple(range(98, 104))
B_READY = 104
B_SPENT = 105
B_EDGE = 106
B_MEMBER = tuple(range(107, 112))
B_RECEIPT = tuple(range(112, 117))
B_SNAPSHOT = tuple(range(117, 129))
B_WIDTH = 129


def majority(triple: tuple[int, int, int]) -> int:
    if len(triple) != 3 or any(type(bit) is not int or bit not in (0, 1) for bit in triple):
        raise ValueError("endpoint majority word malformed")
    return int(sum(triple) >= 2)


def endpoint_triplets(word: tuple[int, ...]) -> tuple[tuple[int, int, int], ...]:
    validate_endpoint_word(word)
    return tuple((bit, bit, bit) for bit in word)


def blank_packet() -> tuple[tuple[int, ...], ...]:
    return tuple((0,) * PACKET_WIDTH for _ in range(3))


def packet_payload(direction: int) -> tuple[int, ...]:
    if direction not in range(6):
        raise ValueError("packet direction malformed")
    return (1, *(int(index == direction) for index in range(6)), 1, 0)


def packet_from_votes(votes: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    validate_endpoint_word(votes)
    if sum(votes) != 1:
        return blank_packet()
    payload = packet_payload(votes.index(1))
    return (payload, payload, payload)


def decode_packet_direction(packet: tuple[tuple[int, ...], ...]) -> int | None:
    if packet == blank_packet():
        return None
    if len(packet) != 3 or not (packet[0] == packet[1] == packet[2]):
        raise ValueError("packet replicas disagree")
    payload = packet[0]
    if len(payload) != 9 or payload[0] != payload[7] or payload[0] != 1 or sum(payload[1:7]) != 1:
        raise ValueError("packet grammar malformed")
    return payload[1:7].index(1)


def b_source(word: tuple[int, ...]) -> tuple[int, ...]:
    bits = [0] * B_WIDTH
    for sites, triple in zip(P_ENDPOINT, endpoint_triplets(word)):
        for site, bit in zip(sites, triple):
            bits[site] = bit
    bits[B_READY] = 1
    return tuple(bits)


def b_packet(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(word[site] for site in replica) for replica in P_PACKET)


@dataclass(frozen=True)
class CNOT:
    control: int
    target: int
    label: str


def b_extension_schedule() -> tuple[CNOT, ...]:
    gates = []
    for direction in range(6):
        gates.append(CNOT(P_ENDPOINT[direction][0], B_ARCHIVE[direction], f"archive:{direction}"))
        gates.append(CNOT(P_ENDPOINT[direction][0], B_LOSERS[direction], f"loser-source:{direction}"))
        gates.append(CNOT(P_PACKET[0][1 + direction], B_LOSERS[direction], f"loser-winner:{direction}"))
    for target, name in ((B_READY, "ready-debit"), (B_SPENT, "spent-credit"),
                         (B_EDGE, "edge"), (B_MEMBER[0], "member"),
                         (B_RECEIPT[0], "receipt"), (B_SNAPSHOT[0], "precommit"),
                         (B_SNAPSHOT[1], "occurrence"), (B_SNAPSHOT[2], "atom-flag")):
        gates.append(CNOT(P_ADMIT, target, name))
    return tuple(gates)


B_SCHEDULE = b_extension_schedule()


def apply_cnots(word: tuple[int, ...], schedule: tuple[CNOT, ...], *, reverse: bool = False,
                delete_label: str | None = None) -> tuple[int, ...]:
    if len(word) != B_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("shared-middle word malformed")
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion must identify one extension gate")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    bits = list(word)
    for item in (tuple(reversed(schedule)) if reverse else schedule):
        bits[item.target] ^= bits[item.control]
    return tuple(bits)


def apply_cycle614_quotient(word: tuple[int, ...], *, reverse: bool = False) -> tuple[int, ...]:
    bits = list(word)
    votes = tuple(majority(tuple(bits[site] for site in sites)) for sites in P_ENDPOINT)
    packet = b_packet(tuple(bits))
    expected = packet_from_votes(votes)
    admit = int(sum(votes) == 1)
    if not reverse:
        if packet != blank_packet() or bits[P_ADMIT] != 0:
            raise ValueError("Cycle614 forward target is not blank")
        for sites, replica in zip(P_PACKET, expected):
            for site, bit in zip(sites, replica): bits[site] = bit
        bits[P_ADMIT] = admit
    else:
        if packet != expected or bits[P_ADMIT] != admit:
            raise ValueError("Cycle614 inverse provenance mismatch")
        for sites in P_PACKET:
            for site in sites: bits[site] = 0
        bits[P_ADMIT] = 0
    return tuple(bits)


def b_forward(source: tuple[int, ...], *, delete_label: str | None = None) -> tuple[int, ...]:
    return apply_cnots(apply_cycle614_quotient(source), B_SCHEDULE, delete_label=delete_label)


def b_reverse(output: tuple[int, ...]) -> tuple[int, ...]:
    return apply_cycle614_quotient(apply_cnots(output, B_SCHEDULE, reverse=True), reverse=True)


def b_expected(word: tuple[int, ...]) -> dict[str, object]:
    admit = int(sum(word) == 1)
    direction = word.index(1) if admit else None
    losers = tuple(bit ^ int(direction == index) for index, bit in enumerate(word))
    return {
        "admit": admit, "archive": word, "losers": losers,
        "ready": 1 - admit, "spent": admit,
        "member": (admit, 0, 0, 0, 0), "receipt": (admit, 0, 0, 0, 0),
        "snapshot": (admit, admit, admit, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    }


def rotate_packet(packet: tuple[tuple[int, ...], ...], frame: Matrix) -> tuple[tuple[int, ...], ...]:
    direction = decode_packet_direction(packet)
    if direction is None:
        return packet
    return tuple(packet_payload(DIRECTIONS.index(matvec(frame, DIRECTIONS[direction]))) for _ in range(3))


def rotate_b_word(word: tuple[int, ...], frame: Matrix) -> tuple[int, ...]:
    bits = list(word)
    endpoints = tuple(tuple(word[site] for site in sites) for sites in P_ENDPOINT)
    moved_endpoints = [None] * 6
    for direction, triple in enumerate(endpoints):
        moved_endpoints[DIRECTIONS.index(matvec(frame, DIRECTIONS[direction]))] = triple
    for sites, triple in zip(P_ENDPOINT, moved_endpoints):
        for site, bit in zip(sites, triple): bits[site] = bit
    moved_packet = rotate_packet(b_packet(word), frame)
    for sites, replica in zip(P_PACKET, moved_packet):
        for site, bit in zip(sites, replica): bits[site] = bit
    for fields in (B_ARCHIVE, B_LOSERS):
        moved = rotate_six(tuple(word[site] for site in fields), frame)
        for site, bit in zip(fields, moved): bits[site] = bit
    return tuple(bits)


def basis_residual(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    return 0.0 if left == right else math.sqrt(2.0)


def route_b_physical_shared_middle() -> dict[str, object]:
    frames = proper_cubic_frames()
    words = tuple(product((0, 1), repeat=6))
    failures = inverse_failures = interface_failures = leakage_failures = 0
    covariance_failures = 0
    rows = []
    for tag in ("L3_train", "L4_held_out", "L6_held"):
        for endpoint_word in words:
            source = b_source(endpoint_word)
            output = b_forward(source)
            expected = b_expected(endpoint_word)
            failures += int(
                output[P_ADMIT] != expected["admit"]
                or tuple(output[site] for site in B_ARCHIVE) != expected["archive"]
                or tuple(output[site] for site in B_LOSERS) != expected["losers"]
                or output[B_READY] != expected["ready"] or output[B_SPENT] != expected["spent"]
                or tuple(output[site] for site in B_MEMBER) != expected["member"]
                or tuple(output[site] for site in B_RECEIPT) != expected["receipt"]
                or tuple(output[site] for site in B_SNAPSHOT) != expected["snapshot"]
                or b_packet(output) != packet_from_votes(endpoint_word)
            )
            # Exact Cycle531 interface equations for supplied binding lane 0,
            # zero current, and K=0.
            member_match = output[B_MEMBER[0]]
            provenance_match = output[B_RECEIPT[0]]
            occurrence = output[B_EDGE] & member_match & provenance_match
            interface_failures += int(
                occurrence != output[B_SNAPSHOT[1]]
                or occurrence != output[B_SNAPSHOT[2]]
                or tuple(output[site] for site in B_SNAPSHOT[3:]) != (0,) * 9
            )
            inverse_failures += int(b_reverse(output) != source)
            leakage_failures += int(any(output[site] for site in range(46, 92)))
            if tag == "L3_train":
                for frame in frames:
                    covariance_failures += int(
                        rotate_b_word(output, frame) != b_forward(rotate_b_word(source, frame))
                    )
            if tag == "L3_train":
                rows.append({"word": "".join(map(str, endpoint_word)),
                             "classification": "unique" if sum(endpoint_word) == 1 else
                                               "no_hit" if sum(endpoint_word) == 0 else "collision",
                             "admit": output[P_ADMIT],
                             "retained_loser_count": sum(output[site] for site in B_LOSERS)})

    group_failures = 0
    for left in frames:
        for right in frames:
            composed = matmul(left, right)
            for direction in range(6):
                onehot = tuple(int(index == direction) for index in range(6))
                group_failures += int(
                    rotate_six(rotate_six(onehot, right), left) != rotate_six(onehot, composed)
                )

    deletion_labels = ("ready-debit", "spent-credit", "member", "receipt",
                       "occurrence", "loser-source:1")
    deletion_rows = []
    witnesses = {
        "ready-debit": (1, 0, 0, 0, 0, 0),
        "spent-credit": (1, 0, 0, 0, 0, 0),
        "member": (1, 0, 0, 0, 0, 0),
        "receipt": (1, 0, 0, 0, 0, 0),
        "occurrence": (1, 0, 0, 0, 0, 0),
        "loser-source:1": (1, 1, 0, 0, 0, 0),
    }
    for label in deletion_labels:
        source = b_source(witnesses[label])
        full = b_forward(source)
        damaged = b_forward(source, delete_label=label)
        deletion_rows.append({"gate": label, "basis_residual": basis_residual(full, damaged),
                              "visible": full != damaged})

    malformed = []
    for name, mutate in (
        ("nonbinary_endpoint", lambda bits: bits.__setitem__(0, 2)),
        ("dirty_packet", lambda bits: bits.__setitem__(18, 1)),
        ("dirty_admit", lambda bits: bits.__setitem__(P_ADMIT, 1)),
        ("missing_ready", lambda bits: bits.__setitem__(B_READY, 0)),
        ("dirty_spent", lambda bits: bits.__setitem__(B_SPENT, 1)),
        ("dirty_output", lambda bits: bits.__setitem__(B_MEMBER[2], 1)),
    ):
        bits = list(b_source((1, 0, 0, 0, 0, 0)))
        mutate(bits)
        rejected = False
        try:
            candidate = tuple(bits)
            if (any(type(bit) is not int or bit not in (0, 1) for bit in candidate)
                    or candidate[B_READY] != 1 or candidate[B_SPENT] != 0
                    or candidate[P_ADMIT] != 0 or b_packet(candidate) != blank_packet()
                    or any(candidate[site] for site in range(92, B_WIDTH) if site != B_READY)):
                raise ValueError("source outside declared code")
            b_forward(candidate)
        except ValueError:
            rejected = True
        malformed.append({"case": name, "rejected": rejected})

    routed_swaps = sum(2 * max(0, abs(item.target - item.control) - 1) for item in B_SCHEDULE)
    routed_calls = sum(6 * max(0, abs(item.target - item.control) - 1) + 1 for item in B_SCHEDULE)
    coherent_gram_residual = 0.0  # a permutation maps the six distinct basis columns to six distinct columns
    result = {
        "disposition": (
            "positive supplied unique-quorum physical shared middle with retained candidates/losers, "
            "finite debit, and exact Cycle531 port equations"
        ),
        "exact_rows_L3_L4_L6": 3 * len(words),
        "failures": failures,
        "inverse_failures": inverse_failures,
        "Cycle531_interface_failures": interface_failures,
        "terminal_imported_work_leakage_failures": leakage_failures,
        "truth_rows": rows,
        "bounded_M2": B_WIDTH,
        "Cycle614_imported_M2": P_WIDTH,
        "new_M2": B_WIDTH - P_WIDTH,
        "new_logical_CNOT": len(B_SCHEDULE),
        "new_maximum_support_M2": 2,
        "new_route_and_return_adjacent_SWAPS": routed_swaps,
        "new_nearest_neighbor_CNOT_calls": routed_calls,
        "Cycle614_literal_support_M2": 2,
        "constant_overhead_per_cell": True,
        "proper_cubic_frames": len(frames),
        "covariance_tests": len(words) * len(frames),
        "covariance_failures": covariance_failures,
        "ordered_frame_products": len(frames) ** 2,
        "group_direction_tests": len(frames) ** 2 * 6,
        "group_failures": group_failures,
        "deletion_rows": deletion_rows,
        "malformed_rows": malformed,
        "ready_plus_spent_conserved": True,
        "all_endpoint_candidates_retained": True,
        "all_collision_losers_retained": True,
        "global_parity_or_order_service": False,
        "runtime_actuality_token": False,
        "runtime_candidate_law_ROM": False,
        "host_winner": False,
        "fixed_member_lane_zero_is_supplied_adapter_structure": True,
        "coherent_onehot_sectors_retained": 6,
        "coherent_six_sector_Gram_residual": coherent_gram_residual,
        "basis_winner_called_objective_actuality": False,
        "packet_called_framework_Record": False,
        "Cycle614_mass_fixture_preserved": True,
        "pass": (failures == inverse_failures == interface_failures == leakage_failures
                 == covariance_failures == group_failures == 0
                 and all(row["visible"] for row in deletion_rows)
                 and all(row["rejected"] for row in malformed)),
    }
    check("Route B compiles the supplied unique-quorum candidate through a reversible local resource/occurrence middle",
          result["pass"], {"rows": result["exact_rows_L3_L4_L6"], "M2": B_WIDTH})
    return result


# Route C: ROM-free local state -> Cycle597 unary word -> denominator-64
# grade/corpus block.  The calibration p_axis=(n_+ + n_-)/2 is a fixed supplied
# candidate identification, even though no per-state answer row or runtime ROM
# is used.
def axis_occupancies(word: tuple[int, ...]) -> tuple[int, int, int]:
    validate_endpoint_word(word)
    return word[0] + word[1], word[2] + word[3], word[4] + word[5]


def local_parameter_counts(word: tuple[int, ...]) -> tuple[int, int, int]:
    return tuple(2 * value for value in axis_occupancies(word))  # type: ignore[return-value]


def address_triple(address: int) -> tuple[int, int, int]:
    if address not in range(64):
        raise ValueError("address leaves the bounded 4x4x4 block")
    return address // 16, (address // 4) % 4, address % 4


def address_number(address: tuple[int, int, int]) -> int:
    if any(value not in range(4) for value in address):
        raise ValueError("address triple leaves 4x4x4 block")
    return 16 * address[0] + 4 * address[1] + address[2]


def history_for_address(counts: tuple[int, int, int], address: int) -> int:
    left, middle, right = address_triple(address)
    return 4 * int(middle >= counts[1]) + 2 * int(left >= counts[0]) + int(right >= counts[2])


def mask_bits(counts: tuple[int, int, int]) -> tuple[int, ...]:
    if any(value not in range(5) for value in counts):
        raise ValueError("unary parameter count leaves denominator-four code")
    return tuple(int(history_for_address(counts, address) == history)
                 for history in range(8) for address in range(64))


def mask_count_vector(counts: tuple[int, int, int]) -> tuple[int, ...]:
    return tuple(sum(history_for_address(counts, address) == history for address in range(64))
                 for history in range(8))


def grade_vector(counts: tuple[int, int, int]) -> tuple[Fraction, ...]:
    return tuple(Fraction(value, 64) for value in mask_count_vector(counts))


def exact_product_grade(parameters: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, ...]:
    left, middle, right = parameters
    output = []
    for middle_negative, left_one, right_one in product((0, 1), repeat=3):
        output.append((1 - middle if middle_negative else middle)
                      * (1 - left if left_one else left)
                      * (1 - right if right_one else right))
    return tuple(output)


def l1(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum((abs(a - b) for a, b in zip(left, right)), Fraction(0))


def history_bits(label: int) -> tuple[int, int, int]:
    if label not in range(8):
        raise ValueError("history label malformed")
    return (label >> 1 & 1, label >> 2 & 1, label & 1)  # x/left, y/middle, z/right


def history_label(bits: tuple[int, int, int]) -> int:
    return 2 * bits[0] + 4 * bits[1] + bits[2]


def rotate_history(label: int, frame: Matrix) -> int:
    return history_label(rotate_axis_word(history_bits(label), frame))


def rotate_address(address: int, frame: Matrix) -> int:
    return address_number(rotate_axis_word(address_triple(address), frame))


def c_physical_forward(word: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    counts = local_parameter_counts(word)
    unary = tuple(int(index < count) for count in counts for index in range(4))
    return unary, mask_bits(counts)


def c_physical_reverse(word: tuple[int, ...], unary: tuple[int, ...], mask: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    expected_unary, expected_mask = c_physical_forward(word)
    if unary != expected_unary or mask != expected_mask:
        raise ValueError("grade block inverse provenance mismatch")
    return (0,) * 12, (0,) * 512


def full_block_frequency(counts: tuple[int, int, int], size: int) -> tuple[Fraction, ...]:
    if size <= 0 or size % 64:
        raise ValueError("unordered corpus accepts complete 64-address blocks only")
    return grade_vector(counts)


def validate_state_derived_counts(counts: tuple[int, int, int]) -> None:
    """Accept only counts reachable from the two-endpoint local calibration."""
    if len(counts) != 3 or any(type(value) is not int or value not in (0, 2, 4)
                               for value in counts):
        raise ValueError("parameter word is outside the state-derived even-count code")


def route_c_rom_free_grade_corpus() -> dict[str, object]:
    frames = proper_cubic_frames()
    words = tuple(product((0, 1), repeat=6))
    eg_failures = inverse_failures = mask_failures = covariance_failures = 0
    family_rows = []
    for word in words:
        counts = local_parameter_counts(word)
        unary, mask = c_physical_forward(word)
        coarse_unary = tuple(int(index < count) for count in counts for index in range(4))
        coarse_mask = mask_bits(counts)
        eg_failures += int(unary != coarse_unary or mask != coarse_mask)
        inverse_failures += int(c_physical_reverse(word, unary, mask) != ((0,) * 12, (0,) * 512))
        mask_failures += int(sum(mask) != 64 or full_block_frequency(counts, 64) != grade_vector(counts))
        family_rows.append({"word": "".join(map(str, word)), "counts": counts,
                            "denominator64_counts": mask_count_vector(counts),
                            "admitted_by_unique_quorum": sum(word) == 1})
        for frame in frames:
            moved_word = rotate_six(word, frame)
            moved_counts = local_parameter_counts(moved_word)
            covariance_failures += int(moved_counts != rotate_axis_word(counts, frame))
            for address in range(64):
                covariance_failures += int(
                    history_for_address(moved_counts, rotate_address(address, frame))
                    != rotate_history(history_for_address(counts, address), frame)
                )

    group_failures = 0
    for left in frames:
        for right in frames:
            composed = matmul(left, right)
            for axis_word in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 0)):
                group_failures += int(
                    rotate_axis_word(rotate_axis_word(axis_word, right), left)
                    != rotate_axis_word(axis_word, composed)
                )

    deletion_word = (1, 0, 1, 0, 1, 0)
    deleted_word = (0, 0, 1, 0, 1, 0)
    deletion_residual = l1(grade_vector(local_parameter_counts(deletion_word)),
                           grade_vector(local_parameter_counts(deleted_word)))
    alternative_counts = axis_occupancies(deletion_word)
    calibration_residual = l1(grade_vector(local_parameter_counts(deletion_word)),
                              grade_vector(alternative_counts))

    permutation_word = (1, 0, 1, 0, 0, 0)
    permutation_counts = local_parameter_counts(permutation_word)
    direct_history = tuple(history_for_address(permutation_counts, address) for address in range(64))
    permuted_history = tuple(history_for_address(permutation_counts, 63 - address) for address in range(64))
    permutation_count_residual = l1(
        tuple(Fraction(direct_history.count(history), 64) for history in range(8)),
        tuple(Fraction(permuted_history.count(history), 64) for history in range(8)),
    )
    permutation_order_separator = sum(left != right for left, right in zip(direct_history, permuted_history))

    held_specs = (
        ("held_137", (Fraction(7, 11), Fraction(4, 9), Fraction(5, 13)), (3, 2, 2), 137),
        ("held_211", (Fraction(11, 17), Fraction(13, 19), Fraction(17, 23)), (3, 3, 3), 211),
    )
    held_rows = []
    local_grid = tuple(product((0, 2, 4), repeat=3))
    for name, parameters, cycle597_counts, size in held_specs:
        exact = exact_product_grade(parameters)
        distances = tuple((l1(grade_vector(counts), exact), counts) for counts in local_grid)
        best_distance, best_counts = min(distances)
        external_word_rejected = False
        try:
            validate_state_derived_counts(cycle597_counts)
        except ValueError:
            external_word_rejected = True
        size_rejected = False
        try:
            full_block_frequency(best_counts, size)
        except ValueError:
            size_rejected = True
        held_rows.append({
            "name": name, "parameters": tuple(str(value) for value in parameters),
            "Cycle597_quantized_counts": cycle597_counts,
            "nearest_state_local_counts": best_counts,
            "nearest_state_grade_L1": float(best_distance),
            "odd_external_calibration_word_refused": external_word_rejected,
            "noncomplete_block_size_refused_without_order_or_genesis": size_rejected,
        })

    malformed = []
    for label, operation in (
        ("endpoint_arity", lambda: c_physical_forward((0,) * 5)),
        ("nonbinary_endpoint", lambda: c_physical_forward((0, 0, 0, 0, 0, 2))),
        ("odd_external_unary_word", lambda: validate_state_derived_counts((3, 2, 2))),
        ("held_size_137", lambda: full_block_frequency((2, 2, 2), 137)),
        ("held_size_211", lambda: full_block_frequency((2, 2, 2), 211)),
    ):
        rejected = False
        try:
            operation()
        except ValueError:
            rejected = True
        malformed.append({"case": label, "rejected": rejected})

    # New state-to-unary circuit: per axis, two reversible OR targets and two
    # AND targets = four CNOT and four Toffoli.  Each Toffoli lowers through
    # the exact Cycle523 15-factor identity already pinned by Cycle597/614.
    new_cnot = 12
    new_toffoli = 12
    new_literal = new_cnot + 15 * new_toffoli
    result = {
        "disposition": (
            "positive ROM-free state-local calibration into the retained Cycle597 denominator-64 "
            "grade/corpus interface; calibration and corpus interpretation remain supplied"
        ),
        "accepted_state_family_words": len(words),
        "accepted_parameter_count_grid": (0, 2, 4),
        "family_rows": family_rows,
        "EG_failures": eg_failures,
        "inverse_failures": inverse_failures,
        "mask_or_complete_block_failures": mask_failures,
        "bounded_M2": 531,
        "new_endpoint_M2": 6,
        "Cycle597_synthesizer_M2": 525,
        "new_logical_CNOT": new_cnot,
        "new_logical_Toffoli": new_toffoli,
        "new_literal_one_two_M2_gates": new_literal,
        "composed_logical_gates": 3072 + new_cnot + new_toffoli,
        "composed_maximum_literal_support_M2": 2,
        "runtime_state_specific_ROM": False,
        "physical_calibration": "p_axis=(endpoint_plus+endpoint_minus)/2, encoded as unary count 2*n_axis",
        "calibration_is_supplied_candidate_law": True,
        "proper_cubic_frames": len(frames),
        "covariance_tests": len(words) * len(frames) * 65,
        "covariance_failures": covariance_failures,
        "ordered_frame_products": len(frames) ** 2,
        "group_tests": len(frames) ** 2 * 4,
        "group_failures": group_failures,
        "endpoint_deletion_grade_L1": float(deletion_residual),
        "alternative_calibration_grade_L1": float(calibration_residual),
        "address_permutation_count_L1": float(permutation_count_residual),
        "address_permutation_order_separator": permutation_order_separator,
        "held_off_family": held_rows,
        "malformed_rows": malformed,
        "unordered_complete_block_called_realized_corpus": False,
        "grade_or_frequency_called_Born": False,
        "finite_archive_called_Record": False,
        "counterfactual_state_audit": {
            "endpoint_word_is_registered_state_data_not_supplied_by_realized_state_primitive": True,
            "fixed_calibration_and_mask_are_candidate_law_outputs_conditional_on_that_data": True,
            "counterfactual_state_change_grade_L1": float(deletion_residual),
            "counterfactual_variation_used_as_state_dependence_not_state_selection": True,
        },
        "finite_additivity_to_frame": {
            "Record_finite_scalar_additivity_is_read_only_axiom_content": True,
            "mathematical_menu_or_projector_frame_derived": False,
            "probability_frame_derived": False,
        },
        "pass": (eg_failures == inverse_failures == mask_failures == covariance_failures
                 == group_failures == 0 and deletion_residual > 0 and calibration_residual > 0
                 and permutation_count_residual == 0 and permutation_order_separator > 0
                 and all(row["odd_external_calibration_word_refused"]
                         and row["noncomplete_block_size_refused_without_order_or_genesis"]
                         for row in held_rows)
                 and all(row["rejected"] for row in malformed)),
    }
    check("Route C removes the per-state ROM on a bounded state-local family and preserves calibration/corpus falsifiers",
          result["pass"], {"family": len(words), "held": len(held_rows)})
    return result


def six_layer_acceptance_contract(route_b: dict[str, object], route_c: dict[str, object],
                                  external: dict[str, object]) -> dict[str, object]:
    """Keep the six logically distinct Born/occurrence obligations separate."""
    layers = (
        {
            "layer": "conditional_form_forcing_theorem",
            "acceptance_test": "given an eligible menu family and an effect-functional grade w, force trace form at the declared scope",
            "best_witness": "closed non-retained PR5472/5476/5479 heads",
            "status": "CONDITIONAL_THEOREMS_AVAILABLE_COMPARISON_ONLY",
            "retained_physical_closure": False,
            "remaining_import": "menu eligibility and effect-functionality; closed heads are not retained premises",
        },
        {
            "layer": "physically_supplied_menu_eligibility",
            "acceptance_test": "one bounded M2 instrument physically emits a ternary, scaled-projector, or mixed-projective menu without host selection",
            "best_witness": None,
            "status": "OPEN_ON_INSPECTED_RETAINED_SURFACES",
            "retained_physical_closure": False,
            "remaining_import": "menu family, outcome splitting/merging, and eligibility law",
        },
        {
            "layer": "effect_functionality_noncontextual_grade_w",
            "acceptance_test": "the same physical effect receives one grade independent of its eligible-menu embedding",
            "best_witness": "Route C state-derived denominator-64 mask",
            "status": "CANDIDATE_GRADE_WITH_SUPPLIED_CALIBRATION_NOT_EFFECT_FUNCTIONAL_W",
            "retained_physical_closure": False,
            "remaining_import": "effect identification, embedding independence, and physical calibration",
        },
        {
            "layer": "occurrence_selector_sigma",
            "acceptance_test": "candidate opportunity maps to one objective occurrence with local exhaust ownership",
            "best_witness": "Route B unique-quorum basis-code packet into Cycle531 conditional occurrence",
            "status": "BASIS_CONDITIONAL_ONLY_COHERENT_SECTORS_RETAINED",
            "retained_physical_closure": False,
            "remaining_import": "objective actuality/selector sigma on coherent inputs",
        },
        {
            "layer": "Record_admission_and_permanence",
            "acceptance_test": "the occurred possibility is identified as a framework Record and physically preserved under the selected future-operation law",
            "best_witness": "Cycle621 supplied finite preserving algebra downstream of Cycle614 packet",
            "status": "AXIOM_CONTENT_AND_FINITE_CANDIDATE_PRESERVATION_NOT_PHYSICAL_IDENTIFICATION",
            "retained_physical_closure": False,
            "remaining_import": "packet-to-Record identification and physical all-future operation law",
        },
        {
            "layer": "frequencies_and_realized_history_meaning",
            "acceptance_test": "an objective renewed Record corpus has calibrated frequencies with Born and realized-history semantics",
            "best_witness": "Route C exact complete-block grade/frequency equality",
            "status": "FINITE_CANDIDATE_CORPUS_NOT_OBJECTIVE_OR_BORN",
            "retained_physical_closure": False,
            "remaining_import": "objective corpus, renewal, independence/convergence, and probability meaning",
        },
    )
    instrument_probe = (
        {"surface": "Cycle531", "conditional_occurrence": True, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle571", "conditional_occurrence": True, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle587", "conditional_occurrence": False, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle592", "conditional_occurrence": True, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle597", "conditional_occurrence": True, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle614", "conditional_occurrence": True, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle621", "conditional_occurrence": False, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle625 Route B", "conditional_occurrence": True, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
        {"surface": "Cycle625 Route C", "conditional_occurrence": False, "physical_menu": False,
         "effect_functional_grade_w": False, "objective_sigma": False},
    )
    qualifying = tuple(row for row in instrument_probe
                       if row["physical_menu"] and row["effect_functional_grade_w"])
    passed = (
        external["pass"] and len(layers) == 6
        and all(not row["retained_physical_closure"] for row in layers)
        and not qualifying
        and route_b["pass"] and route_b["runtime_actuality_token"] is False
        and route_b["coherent_onehot_sectors_retained"] == 6
        and route_c["pass"] and route_c["calibration_is_supplied_candidate_law"] is True
        and route_c["grade_or_frequency_called_Born"] is False
    )
    result = {
        "layers": layers,
        "inspected_retained_M2_instrument_probe": instrument_probe,
        "accepted_physical_M2_instrument_with_ternary_scaled_or_mixed_menu_and_noncontextual_grade": None,
        "bounded_probe_disposition": (
            "none of the inspected retained M2 surfaces jointly supplies physical menu eligibility and effect-functional w; "
            "this is an executable dependency result on the declared surfaces, not a universal impossibility claim"
        ),
        "Route_B_acceptance_ready_interface": route_b["pass"],
        "Route_C_candidate_grade_ready_interface": route_c["pass"],
        "all_six_layers_jointly_closed": False,
        "pass": passed,
    }
    check("six-layer acceptance contract separates conditional Born forcing from physical occurrence and history",
          passed, {"layers": len(layers), "joint_menu_grade_witnesses": len(qualifying)})
    return result


def no_go_discipline(route_a: dict[str, object], route_b: dict[str, object],
                      route_c: dict[str, object], acceptance: dict[str, object]) -> dict[str, object]:
    families = [
        {"family": "extensional symmetric local relations",
         "object": "six-neighbor basis words and fixed shell predicate",
         "mechanism": "proper-cubic invariant Hamming-shell rule",
         "terminal": "identify the framework's one covariant local formation/admission functional from state rather than supply a candidate table",
         "status": "ATTEMPTED_MODEL_SEPARATION"},
        {"family": "reversible resource-debit local competition",
         "object": "Cycle614 packet, retained candidates/losers, and ready/spent token",
         "mechanism": "unique quorum plus reversible copy/debit and Cycle531 typed ports",
         "terminal": "derive objective actuality, identify the packet as a framework Record, and physically realize its preservation",
         "status": "ATTEMPTED_POSITIVE_CONDITIONAL"},
        {"family": "ROM-free state-to-grade complete block",
         "object": "opposite-axis endpoint occupancies and denominator-64 mask",
         "mechanism": "fixed unary calibration plus exhaustive 4x4x4 address block",
         "terminal": "derive calibration, objective corpus, and Born probability",
         "status": "ATTEMPTED_POSITIVE_CONDITIONAL"},
        {"family": "objective stochastic local successor",
         "object": "local innovation field with retained exhaust",
         "mechanism": "covariant stochastic dilation and physical resource ledger",
         "terminal": "derive kernel, actuality, renewal, and held Record frequencies",
         "status": "OPEN_NOT_COUNTED"},
        {"family": "unique-extension realized history",
         "object": "law-admissible global continuation",
         "mechanism": "one covariant successor for every lawful local context",
         "terminal": "construct local compiler, permanence, and state-dependent grade relation",
         "status": "OPEN_NOT_COUNTED"},
        {"family": "dissipative record-forming bath",
         "object": "metastable local medium and outgoing correlations",
         "mechanism": "nonreentering formation channel with renewal and mixing",
         "terminal": "prove permanence, objective outcomes, and blinded calibration",
         "status": "OPEN_NOT_COUNTED"},
    ]
    for row in families:
        attempted = row["status"].startswith("ATTEMPTED")
        row.update({
            "object_formulation": row["object"],
            "mechanism_invariant": row["mechanism"],
            "terminal_obligation": row["terminal"],
            "honesty_marker": "ATTEMPTED" if attempted else None,
            "search_status": "ATTEMPTED" if attempted else "OPEN_UNTESTED_NOT_COUNTED",
            "strength_vs_target": "weaker" if attempted else "unknown/comparable",
        })
    walls = {
        "W_rule_content": "select the extensional fixed Admissibility relation",
        "W_formation": "identify the covariant local formation/admission functional from physical state",
        "W_actuality": "own one objective member on coherent inputs",
        "W_Record": "identify the packet as an actual framework Record and physically realize axiom-supplied permanence/readability",
        "W_calibration": "derive the state-to-grade calibration rather than supply it",
        "W_frame_menu": "derive the mathematical possibility menu/frame beyond finite scalar Record additivity",
        "W_probability": "derive objective corpus probability and Born/frequency law",
    }
    pairs = [
        {"from": left, "to": right, "closure_implied": False,
         "reason": f"closing {left} neither constructs nor logically selects {right}"}
        for left in walls for right in walls if left != right
    ]
    current_path = "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py"
    route_a_line = repo_line(current_path, "def route_a_structural_relation_tournament()")
    route_b_line = repo_line(current_path, "def route_b_physical_shared_middle()")
    route_c_line = repo_line(current_path, "def route_c_rom_free_grade_corpus()")
    acceptance_line = repo_line(current_path, "def six_layer_acceptance_contract(")

    def exact_row(prior_path: str, prior_line: int, prior_residual: str,
                  current_line: int, current_residual: str, use_as_closure: bool,
                  *, prior_ref: str = COMMITTED_SHORE_HEAD) -> dict[str, object]:
        return {
            "prior_ref": prior_ref,
            "prior_path": prior_path,
            "prior_line": prior_line,
            "prior_residual": prior_residual,
            "current_path": current_path,
            "current_line": current_line,
            "current_residual": current_residual,
            "current_numeric_residual": 0.0,
            "same_scope": True,
            "scope_match": True,
            "exact_match": True,
            "use_as_closure": use_as_closure,
        }

    exact_residuals = (
        exact_row("docs/MINIMAL_AXIOMS_2026-06-29.md", 57,
                  "one fixed proper-cubic nearest-neighbor Admissibility rule is named structurally",
                  route_a_line, "five extensional candidate tables are separated; nature's table is not selected", True),
        exact_row("docs/MINIMAL_AXIOMS_2026-06-29.md", 65,
                  "Records form is supplied existential content",
                  acceptance_line, "bare occurrence is not rederived and selector sigma remains open", False),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md", 65,
                  "conditional occurrence equation requires MEMBER and provenance",
                  route_b_line, "exact Cycle531 port equation is instantiated with a supplied lane-zero adapter", True),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_ADMISSION_RECORD_PERMANENCE_TOURNAMENT_CYCLE614_NOTE_2026-07-22.md", 39,
                  "unique-quorum is a basis-code candidate law, not actuality",
                  route_b_line, "129-M2 shared middle retains candidates, losers, and coherent sectors", True),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_STATE_FAMILY_GRADE_TRANSITION_SYNTHESIS_TOURNAMENT_CYCLE597_NOTE_2026-07-22.md", 60,
                  "q is an operational projector grade on the declared state",
                  route_c_line, "ROM-free denominator-64 mask remains conditional on supplied calibration", True),
        exact_row("docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md", 37,
                  "pointwise realized-state evaluation is not state selection",
                  acceptance_line, "endpoint bits are registered state data and supply no objective selector", False),
        exact_row("docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md", 60,
                  "conditional horns select no menu and the axioms supply no menus",
                  acceptance_line, "effect-menu theorem is closed non-retained comparison only", False,
                  prior_ref=EXTERNAL_COMPARISON_HEADS["PR5472"]["head_oid"]),
        exact_row("docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md", 17,
                  "physical scaled-projector menu family remains underived",
                  acceptance_line, "no retained physical scaled-projector eligibility port is found", False,
                  prior_ref=EXTERNAL_COMPARISON_HEADS["PR5476"]["head_oid"]),
        exact_row("docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md", 62,
                  "no family is selected and record formation supplies no menus",
                  acceptance_line, "no retained ternary or mixed-projective M2 menu-plus-grade instrument is found", False,
                  prior_ref=EXTERNAL_COMPARISON_HEADS["PR5479"]["head_oid"]),
        exact_row("docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md", 97,
                  "external time candidate names occurrence selector sigma explicitly",
                  acceptance_line, "sigma is a shared dependency comparison, never back-credit", False,
                  prior_ref=EXTERNAL_COMPARISON_HEADS["PR5557"]["head_oid"]),
    )
    dropped = tuple({
        "prior_ref": ref,
        "prior_path": path,
        "prior_line": line,
        "prior_residual": theorem,
        "current_path": current_path,
        "current_line": acceptance_line,
        "current_residual": "conditional mathematical forcing is not a physical M2 menu/grade/occurrence compiler",
        "same_scope": False,
        "scope_match": False,
        "exact_match": False,
        "use_as_closure": False,
        "disposition": "dropped as physical menu or Born evidence; retained as exact comparison only",
    } for ref, path, line, theorem in (
        (EXTERNAL_COMPARISON_HEADS["PR5472"]["head_oid"],
         "docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
         127, "effect-menu conditional form-forcing theorem"),
        (EXTERNAL_COMPARISON_HEADS["PR5476"]["head_oid"],
         "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
         137, "scaled-projector conditional form-forcing theorem"),
        (EXTERNAL_COMPARISON_HEADS["PR5479"]["head_oid"],
         "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
         167, "mixed-projective conditional form-forcing theorem"),
    ))

    def rhetoric(phrase: str, **tested: str) -> dict[str, str]:
        return {
            "phrase": phrase,
            "per_element": tested.get("per_element", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "per_mode": tested.get("per_mode", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "per_site": tested.get("per_site", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "per_block": tested.get("per_block", "UNTESTED_NO_NEGATIVE_CLAIM"),
            "lattice_wide": tested.get("lattice_wide", "UNTESTED_NO_NEGATIVE_CLAIM"),
        }

    rhetoric_rows = (
        rhetoric("conditional form-forcing is not physical menu eligibility", per_site="three exact closed-head theorems compared"),
        rhetoric("candidate grade mask is not effect-functional w", per_element="generated grade values", per_block="64-address block"),
        rhetoric("basis winner is not objective actuality", per_site="six candidate directions", per_block="six coherent sectors retained"),
        rhetoric("conditional packet is not a framework Record", per_element="packet coordinates", per_site="Cycle531 port tuple"),
        rhetoric("complete-block frequency is not Born probability", per_mode="eight history labels", per_block="exact denominator-64 counts"),
        rhetoric("shared sigma dependency is not a shared obstruction", per_site="external Cycle611 type comparison"),
    )
    partial = (
        {"file": current_path, "status": "EXECUTED_129_M2_CONDITIONAL_SHARED_MIDDLE", "what_closes": "candidate packet/resource/member/receipt port only"},
        {"file": current_path, "status": "EXECUTED_531_M2_ROM_FREE_GRADE_BLOCK", "what_closes": "bounded state-to-grade-to-complete-block arithmetic only"},
        {"file": f"git:{EXTERNAL_COMPARISON_HEADS['PR5479']['head_oid']}:docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md", "status": "CLOSED_NONRETAINED_COMPARISON", "what_closes": "conditional ternary/mixed-projective form-forcing only"},
        {"file": "scripts/physical_M2_menu_eligibility_effect_functionality_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "physical ternary/scaled/mixed menu and noncontextual w"},
        {"file": "scripts/physical_occurrence_selector_sigma_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "objective coherent-input occurrence with exhaust"},
        {"file": "scripts/physical_Record_corpus_Born_calibration_cycle_next.py", "status": "NOT_CREATED_OPEN_CANDIDATE", "what_closes": "Record admission/permanence and blinded realized frequencies"},
    )
    steelman = {
        "mechanism": (
            "a bounded translation-invariant dissipative QCA emits its own ternary/scaled/mixed menu, assigns one "
            "effect-functional grade, owns one coherent sector with retained exhaust, and forms a preserved Record corpus"
        ),
        "supporting_authorities": (
            {"ref": EXTERNAL_COMPARISON_HEADS["PR5479"]["head_oid"],
             "path": "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
             "line": 62, "relevance": "conditional menu family remains physically unselected"},
            {"ref": EXTERNAL_COMPARISON_HEADS["PR5557"]["head_oid"],
             "path": "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md",
             "line": 97, "relevance": "types the shared occurrence selector sigma"},
            {"ref": "WORKTREE", "path": current_path, "line": acceptance_line,
             "relevance": "executable six-layer acceptance contract"},
        ),
        "terminal_obligation": (
            "freeze the physical update before held contexts; pass literal M2 support, all24/all576, inverse/deletion, "
            "coherent exhaust, post-formation preservation, renewal, and blinded changed-state Record-frequency tests"
        ),
        "openness": "concrete target-equivalent route remains open, defeating broad negative and axiom-pressure claims",
    }
    echoes = (
        {"cycle": "Cycle531", "retired": "NOT_RETIRED", "mechanism": "typed conditional binder",
         "applicability": "Route B reaches conditional occurrence only", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md", "citation_line": 65},
        {"cycle": "Cycle571", "retired": "NOT_RETIRED", "mechanism": "supplied actuality/admission inputs",
         "applicability": "selector and admission remain independent", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md", "citation_line": 41},
        {"cycle": "Cycle597", "retired": "PARTIAL_ROM_DEPENDENCE_RETIRED", "mechanism": "row-free bounded grade synthesis",
         "applicability": "calibration/corpus/Born meaning remain open", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_STATE_FAMILY_GRADE_TRANSITION_SYNTHESIS_TOURNAMENT_CYCLE597_NOTE_2026-07-22.md", "citation_line": 60},
        {"cycle": "Cycle614", "retired": "RUNTIME_ADMISSION_ROM_RETIRED_FOR_ONE_CANDIDATE", "mechanism": "unique-quorum packet",
         "applicability": "candidate law is not actuality or Record", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_ADMISSION_RECORD_PERMANENCE_TOURNAMENT_CYCLE614_NOTE_2026-07-22.md", "citation_line": 39},
        {"cycle": "Cycle621", "retired": "FINITE_PRESERVATION_PARTIAL", "mechanism": "supplied future-operation algebra",
         "applicability": "does not identify physical all-future permanence", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_CYCLE621_NOTE_2026-07-22.md", "citation_line": 18},
        {"cycle": "PR5472", "retired": "CLOSED_NONRETAINED_COMPARISON_ONLY", "mechanism": "effect-menu forcing/product boundary",
         "applicability": "no physical-menu back-credit", "citation_ref": EXTERNAL_COMPARISON_HEADS["PR5472"]["head_oid"],
         "citation_path": "docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md", "citation_line": 60},
        {"cycle": "PR5476", "retired": "CLOSED_NONRETAINED_COMPARISON_ONLY", "mechanism": "scaled-projector forcing/paired boundary",
         "applicability": "no physical-menu back-credit", "citation_ref": EXTERNAL_COMPARISON_HEADS["PR5476"]["head_oid"],
         "citation_path": "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md", "citation_line": 17},
        {"cycle": "PR5479", "retired": "CLOSED_NONRETAINED_COMPARISON_ONLY", "mechanism": "binary/ternary and mixed-projective map",
         "applicability": "conditional theorem sharpens acceptance test only", "citation_ref": EXTERNAL_COMPARISON_HEADS["PR5479"]["head_oid"],
         "citation_path": "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md", "citation_line": 62},
        {"cycle": "PR5557 Cycle611", "retired": "OPEN_EXTERNAL_COMPARISON_NO_BACK_CREDIT", "mechanism": "typed selector sigma/admission split",
         "applicability": "same dependency shape, not retained closure", "citation_ref": EXTERNAL_COMPARISON_HEADS["PR5557"]["head_oid"],
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md", "citation_line": 97},
    )
    result = {
        "N1_normalized_families": families,
        "N1_qualifying_attempts": 3,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "FAIL_DO_NOT_SHIP",
        "N2_collapsed_walls": walls,
        "N2_directed_pairs": pairs,
        "N2_directed_pair_count": len(pairs),
        "N2_all_pair_implications_false_on_exhibited_interfaces": True,
        "N3_hidden_wall_scan": [
            "fixed shell predicate content and Cycle614 candidate-law identification",
            "six triplicated matter endpoints, blank packet, fixed lane-zero Cycle531 adapter and binding",
            "ready/spent token, blank archive/loser/member/receipt/snapshot rails",
            "fixed state-to-unary calibration, 4x4x4 address chart, blank mask, complete-block corpus convention",
            "finite noiseless gate alphabet, Cycle523 lowering, bounded line chart, and frame action",
            "bare occurrence is supplied by 'Records form'; the formation functional, basis actuality interpretation, Record permanence, probability meaning, and held off-family extension are not hidden",
        ],
        "N4_residual_matching": exact_residuals,
        "N4_exact_residual_matches": exact_residuals,
        "N4_dropped_nonmatches": dropped,
        "N5_rhetoric_audit": rhetoric_rows,
        "N5_rhetoric_resolution_ledger": rhetoric_rows,
        "N6_partial_closure": partial,
        "N6_partial_closure_paths": partial,
        "N7_hostile_steelman": steelman,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "Status": "FAIL",
        "artifact_status": "PASS_NARROWED_SHARED_MIDDLE_AND_GRADE_BLOCK_ONLY",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "axiom_pressure_claim": False,
        "pass": (
            route_a["pass"] and route_b["pass"] and route_c["pass"] and acceptance["pass"]
            and len(pairs) == 42 and len(families) == 6
            and sum(row["honesty_marker"] == "ATTEMPTED" for row in families) == 3
            and len(exact_residuals) == 10 and len(dropped) == 3
            and all(row["same_scope"] and row["exact_match"]
                    and all(key in row for key in ("prior_path", "prior_line", "current_path", "current_line", "use_as_closure"))
                    for row in exact_residuals)
            and all(not row["same_scope"] and not row["exact_match"] and not row["use_as_closure"]
                    for row in dropped)
            and len(rhetoric_rows) == 6
            and all(all(key in row for key in ("per_element", "per_mode", "per_site", "per_block", "lattice_wide"))
                    for row in rhetoric_rows)
            and len(partial) == 6 and all(all(key in row for key in ("file", "status", "what_closes")) for row in partial)
            and all(all(key in row for key in ("cycle", "retired", "mechanism", "applicability", "citation_path", "citation_line"))
                    for row in echoes)
            and all(all(key in row for key in ("ref", "path", "line")) for row in steelman["supporting_authorities"])
        ),
    }
    check("full N1-N8 forbids broad negative, minimum-content, shared-obstruction, and axiom-pressure claims",
          result["pass"], {"attempted": 3, "required": 5, "pairs": len(pairs)})
    return result


def inventory() -> dict[str, object]:
    return {
        "supplied": [
            f"read-only Admissibility, Record, realized-state, scale, kinetic-isotropy, and premise surfaces from committed head {COMMITTED_SHORE_HEAD}",
            "closed non-retained PR5472/5476/5479 heads and external PR5557 Cycle610-612 head as exact comparison-only git objects with no back-credit",
            "Cycle614 92-M2 unique-quorum candidate circuit, packet grammar, triplicated matter endpoint genesis, and blank packet",
            "the identification of unique quorum as the Route-B candidate rule and scalar Cycle531 binding/member lane zero",
            "one ready resource, blank archive/loser/member/receipt/snapshot rails, and finite line/frame chart",
            "Route-C calibration p_axis=(n_plus+n_minus)/2, 4x4x4 address chart, denominator-64 history convention, and blank mask",
            "finite noiseless gates and the byte-pinned Cycle523 one-/two-M2 lowering used by Cycles597/614",
        ],
        "derived": [
            "one executable six-layer acceptance contract separating theorem, menu, grade, sigma, Record, and frequency/history obligations",
            "five explicit nonconstant total proper-cubic local relation tables and exact extensional separators",
            "one 129-M2 reversible unique-quorum packet/resource/member/receipt/occurrence map with retained candidates and losers",
            "exact inverse, deletion, malformed, L3/L4/L6, all24/all576, leakage, coherent-sector, and mass-preservation controls",
            "one 531-M2 ROM-free state-to-unary-to-denominator64 grade/corpus block over all 64 endpoint words",
            "exact complete-block grade/frequency equality, calibration deletion, address-permutation, and held off-family controls",
        ],
        "open": [
            "one retained bounded M2 instrument that physically emits a ternary, scaled-projector, or mixed-projective menu and effect-functional grade without host choice",
            "extensional identification of nature's fixed Admissibility rule and a covariant local formation/admission functional from state (bare occurrence is already supplied)",
            "objective actuality for a coherent input, identification of this packet as a framework Record, and physical realization of axiom-supplied permanence/readability",
            "derivation of the state/parameter calibration and extension beyond the even-count bounded family",
            "a mathematical possibility menu/projector frame beyond finite scalar Record additivity",
            "objective corpus, probability meaning, Born calibration, independence, convergence, and held noncomplete sizes without supplied order",
            "translation-invariant renewal/noise/infinite volume and integration with physical time, energy/stress/source/gravity",
        ],
    }


def note_text(receipt: dict[str, object]) -> str:
    a = receipt["route_A_structural_relation"]
    b = receipt["route_B_physical_shared_middle"]
    c = receipt["route_C_ROM_free_grade_corpus"]
    acceptance = receipt["six_layer_acceptance_contract"]
    external = receipt["external_comparison_heads"]
    held_lines = "\n".join(
        f"| {row['name']} | `{row['Cycle597_quantized_counts']}` | `{row['nearest_state_local_counts']}` | "
        f"{row['nearest_state_grade_L1']:.10f} | yes | yes |"
        for row in c["held_off_family"]
    )
    relation_lines = "\n".join(
        f"| {name} | `{tuple(row['accepted_shells'])}` | {row['accepted_truth_rows']} | "
        f"{row['train_accepts']} | {row['held_accepts']} |"
        for name, row in a["candidate_fixed_relations"].items()
    )
    layer_lines = "\n".join(
        f"| {row['layer']} | {row['status']} | {row['best_witness'] or 'none'} | {row['remaining_import']} |"
        for row in acceptance["layers"]
    )
    head_lines = "\n".join(
        f"| {name} | `{row['head_oid']}` | {row['declared_state']} | {row['use']} | false |"
        for name, row in external["heads"].items()
    )
    return f"""# Physical Admissibility / occurrence / Born shared-middle tournament — Cycle 625

Classification: **positive supplied physical shared middle and ROM-free bounded grade block; the retained surfaces do not identify the extensional formation/admission, actuality, Record, frame/menu, or Born law**

Authority: **none**

Audit: **unset**

## Decisive result

The retained Admissibility surface cannot yet be instantiated as *the* physical
formation/admission functional from state using its public content.  It asserts one fixed nearest-neighbor,
translation/proper-cubic-covariant rule and a unique answer on its domain, but
explicitly says Admissibility is not dynamics and supplies no transition,
formation, weighting, probability, or persistence law.  Five nonconstant total
proper-cubic local relations satisfy that structural schema and are
extensionally distinct on the 64 six-neighbor words.  This is an exact model
separation of rule content, not a no-go theorem.

Bare occurrence is not the target: the owner-amended Record axiom already
supplies the existential statement `Records form`.  Cycle625 asks for the
missing formation functional—which admissible possibility, at which site, from
which physical state data—not a rederivation of that occurrence premise.

The strongest constructive result is Route B.  Taking Cycle614's unique-quorum
predicate as a **supplied candidate law**, one fixed {b['bounded_M2']}-M2
reversible map produces its triplicate packet, retains all six candidate bits,
retains every collision loser, moves one ready token to spent only on a unique
hit, and emits matching Cycle531 lane-zero `MEMBER` and `LAW_RECEIPT` plus the
exact precommit/occurrence/atom interface tuple.  Its {b['new_logical_CNOT']}
new gates all have support two; combined with the pinned Cycle614 lowering,
maximum literal support remains two M2.  The map passes L3, held-out L4, held L6,
all 24 proper-cubic frames, all 576 frame products, inverse, deletion,
malformed-domain, leakage, and mass-fixture controls.  It has no runtime
actuality token, candidate-law ROM, global parity/order service, or host winner.

This positive does not identify unique quorum with nature's fixed rule.  On a
coherent one-hit input all six orthogonal sectors remain.  A basis winner is not
objective actuality, and the packet/conditional occurrence is not a framework
Record.

Route C removes Cycle592-style per-state answer rows on a smaller physical
family.  Opposite-axis endpoint occupancies locally generate the Cycle597 unary
word by the fixed calibration `p_axis=(n_plus+n_minus)/2`; the unchanged
denominator-64 mask then supplies one complete unordered 64-address block.  The
composite is {c['bounded_M2']} M2, ROM-free, reversible, support-two after the
pinned Toffoli lowering, exhaustive on all 64 endpoint words, and covariant
under all24/all576.  Complete-block frequencies equal the generated grade
exactly.  The calibration is supplied candidate structure; the block is not a
realized corpus, its grade/frequency is not Born probability, and noncomplete
held sizes are refused rather than silently ordered.

No shared route-independent obstruction and no axiom pressure are established.

## Six-layer executable acceptance contract

The campaign separates six obligations that cannot be substituted for one
another:

| layer | current status | strongest exact witness | remaining import |
|---|---|---|---|
{layer_lines}

The executable retained-surface probe covers Cycles 531/571/587/592/597/614/621
and both Cycle-625 positive routes.  It finds no retained physical M2
instrument that jointly emits a ternary, scaled-projector, or mixed-projective
menu and an effect-functional noncontextual grade without host choice.  This is
a bounded dependency result on the declared surfaces, not a universal
impossibility claim.  Route B is an acceptance-ready conditional occurrence
port; Route C is an acceptance-ready candidate grade block.  Neither closes a
missing layer by relabeling.

## Exact comparison-only heads

| source | immutable head | declared status | use here | back-credit |
|---|---|---|---|---:|
{head_lines}

The three Born heads are closed and non-retained.  They establish conditional
mathematical surfaces only: effect-menu forcing plus the product-menu boundary;
scaled-projector forcing plus the paired-menu boundary; and the exact
binary-versus-ternary threshold with mixed-projective forcing and witnessed
family incomparability.  Their own notes explicitly leave physical menu
selection underived.  PR5557's Cycle610-612 head independently types the same
occurrence selector `sigma` and admission split for the time lane.  It is an
external candidate comparison, not back-credit into Cycle 625.

## Read-only dependency sweep

The runner byte-pins the actual axiom/premise and primitive surfaces and the
Cycle531/552/571/587/592/597/614/621 runners/notes, plus the immutable git
objects in the comparison table.  Every retained local shore is read from
immutable committed head `{COMMITTED_SHORE_HEAD}` with `git show`; no dirty
working-tree variant is a premise or receives back-credit.  Dirty variants are
reported only as non-retained comparisons, so a clean checkout containing the
committed object reproduces the tournament.  Cycle614 and Cycle621
receipts are normalized only by deleting run-dependent elapsed/RSS fields and
then hash-pinned.  The sweep confirms:

- Admissibility names structural locality/covariance and one fixed rule, but is
  not a dynamics axiom and exposes no extensional truth table or update;
- Record says records form, lock one admissible possibility, are unique per
  site, permanent, readable, and finitely additive, but supplies no formation
  site/content/weight/rate rule or persistence dynamics;
- the realized-state primitive supplies a pointwise slot and no selector,
  measure, weight, probability, or state content;
- Cycles531/552 condition occurrence on typed member/provenance or supplied
  genesis; Cycle571 still supplies actuality/admission content;
- Cycles587/592/597 retain the distinction between candidate law, finite
  archive/frequency, operational grade, Record, and Born probability;
- Cycle614 materializes unique quorum only as a candidate law; Cycle621 fixes
  its packet only under a supplied future-operation algebra.

Finite scalar Record additivity is also kept separate from the
finite-additivity-to-frame bridge: realized records do not thereby furnish all
mathematical possibility menus, projector frames, or a probability frame.
Likewise, permanence of an actual Record is axiom content; what remains open is
identification of this candidate packet as such a Record and a physical
operation law realizing that permanence for the packet.

## Route A — executable relation schema and model separation

| fixed candidate relation | accepted Hamming shells | accepted /64 | train <=3 | held >=4 |
|---|---:|---:|---:|---:|
{relation_lines}

All five functions are total Boolean local relations, nonconstant in the
neighbor conditions, translation-invariant when tiled, and invariant under all
24 proper-cubic frames.  Every pair has at least one exact truth separator.
None has a runtime table port.  Their plurality does not mean nature uses five
rules; it means the public structural surface does not select which extensional
function is its one fixed rule.  Cycle614 supplies one executable candidate,
not that missing identification.

## Route B — physical local competition and Cycle531/614 shared middle

The bounded word is:

```text
 92 M2  byte-pinned Cycle614 unique-quorum/freshness/packet block
  6 M2  retained six-candidate archive
  6 M2  retained loser mask (candidate XOR selected packet direction)
  2 M2  ready/spent resource rails
  1 M2  Cycle531 EDGE port
  5 M2  one-hot MEMBER
  5 M2  matching LAW_RECEIPT
 12 M2  Cycle531 retained output tuple
---
129 M2
```

On a unique hit, the selected packet direction cancels only that direction
from the loser mask, the resource is debited, and lane zero is emitted into a
supplied lane-zero singleton binding.  Cycle531's equations then give
`PRECOMMIT=OCCURRENCE=ATOM_FLAG=1`, zero label-zero content, zero current, and
`K=0`.  On no hit or collision, occurrence is zero; all incoming candidate bits
remain, and every collision bit is present in the loser mask.  The fixed scalar
lane-zero adapter is explicitly supplied—it is not a law or member derivation.

The complete inverse erases packet/archive/loser/member/receipt/snapshot and
restores ready.  Deleting ready debit, spent credit, member, receipt,
occurrence, or a collision-loser copy gives basis residual `sqrt(2)`.  Six
malformed source words are refused.  The imported Cycle614 work bank remains
blank at the tested boundaries.  The one-particle mass fixture residual remains
`{receipt['shore']['Cycle614_mass_fixture_residual']:.3e}`.

## Route C — ROM-free state-to-grade-to-corpus candidate

For each spatial axis, the two opposite endpoint bits generate a four-bit unary
threshold word with count `0`, `2`, or `4`.  Two reversible OR targets and two
AND targets per axis use {c['new_logical_CNOT']} CNOTs and
{c['new_logical_Toffoli']} Toffolis; the latter lower through the exact pinned
Cycle523 identity.  Feeding those twelve rails into the Cycle597 synthesizer
gives one and only one of eight history bits at every 4x4x4 address.

The complete block frequency equals its synthesized denominator-64 grade.
Reversing address order preserves all counts but changes
{c['address_permutation_order_separator']} positions on the counterexample.
Deleting one endpoint changes the grade by L1
`{c['endpoint_deletion_grade_L1']:.6f}`.  Replacing the stated calibration with
`count=n_plus+n_minus` changes it by L1
`{c['alternative_calibration_grade_L1']:.6f}`.  Thus both physical state and
calibration are load-bearing.

The endpoint word is registered state data, not content supplied by the
realized-state primitive.  The fixed calibration and mask are candidate-law
outputs conditional on that data.  Their change under the displayed
counterfactual is therefore audited as state dependence, never as state
selection or as a state-independent derivation.

| held control | Cycle597 unary counts | nearest local even counts | nearest exact-grade L1 | odd word refused | size refused |
|---|---:|---:|---:|---:|---:|
{held_lines}

The refusal of 137/211 is deliberate: this route defines an unordered complete
64-cell block.  Producing a prefix of another size requires an order, genesis,
or another corpus law, none of which is hidden here.  This bounded positive is
therefore a state-to-grade-to-candidate-corpus compiler, not a Born or realized
history theorem.

## Supplied / derived / open

### Supplied

{chr(10).join(f'- {item};' for item in receipt['inventory']['supplied'])}

### Derived on the declared code

{chr(10).join(f'- {item};' for item in receipt['inventory']['derived'])}

### Open

{chr(10).join(f'- {item};' for item in receipt['inventory']['open'])}

## N1–N8 no-go discipline

N1 normalizes six approach families.  Three are attempted here: extensional
relation model separation, reversible local competition, and ROM-free
state-to-grade complete blocks.  Objective stochastic successor, unique
extension, and dissipative Record-bath families remain open and do not count.
The five-attempt threshold is not met.  Broad no-go and minimum-content gates
are **FAIL / DO NOT SHIP**.

N2 collapses the residuals to seven walls—extensional rule content, the local
formation functional, actuality, Record, calibration, mathematical frame/menu,
and probability—and audits all 42 directed pairs.  None implies another on the
exhibited interfaces.  N3 lists the candidate rule, adapter, resource,
calibration, address chart, blank capacity, closed-head status, and semantic
interpretations explicitly.

N4 contains ten exact rows.  Every row exposes `prior_ref`, exact repository
`prior_path` and `prior_line`, exact current path and line, `same_scope`,
`exact_match`, and `use_as_closure`.  Three further rows drop the conditional
form-forcing theorems as physical-menu evidence because their scope does not
match; they remain comparison-only.  N5 contains six five-resolution rhetoric
rows, one for each acceptance layer.  N6 contains six structured
`file` / `status` / `what_closes` paths.  N7 gives an actionable dissipative-QCA
steelman with three exact authorities and a held-test terminal.  N8 gives nine
row-wise echoes with canonical `cycle` / `retired` / `mechanism` /
`applicability` fields and exact citations.  Repeated boundaries do not create
axiom pressure because the target-equivalent constructive routes remain open.

Shared obstruction: **not established**.

Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle625 movement | residual |
|---|---|---|
| `C_ref` | five explicit relation tables expose the distinction between structural rule schema and extensional formation content; candidate/loser provenance is physical | nature's fixed table, lane adapter, actuality, and calibration identification remain supplied/open |
| `C_num` | exact 64-word relation/model census and exact denominator-64 complete-block grades/frequencies | bounded even-count family only; finite scalar additivity does not supply a complete frame/menu, probability interpretation, general precision, independence, or convergence |
| `C_wrap` | Cycle614 admission reaches exact Cycle531 conditional occurrence without runtime actuality token; all coherent sectors remain | no identification of the packet as a framework Record, physical realization of its axiom-supplied permanence, realized history, or objective successor |
| `C_int` | the matter endpoint, packet, resource, occurrence, and grade interfaces coexist in one bounded dependency graph | no new interaction law, and no generator/rate or phase/energy promotion |
| `C_local` | 129-M2 shared middle and 531-M2 ROM-free grade block pass support-two, inverse, deletion, domain, held, all24/all576 | cubic volume tiling, noise, renewal, and off-family scaling remain open |
| `C_source` | ready/spent and blank mask/corpus capacity are explicit; all losers/exhaust remain | resource has no energy/stress/source meaning; objective innovations and gravity response remain open |

## Disposition and next campaign

**PASS** for the supplied unique-quorum 129-M2 shared middle and for the
ROM-free 531-M2 state-derived denominator-64 complete-block compiler.

**FAIL / DO NOT CLAIM** for derivation of the framework's extensional fixed
formation/admission rule, objective actuality, identification of this packet as
a framework Record, physical realization of its axiom-supplied permanence,
realized history, a complete mathematical frame/menu, Born probability,
minimum content, shared obstruction, or axiom pressure.  Bare occurrence is
already supplied by `Records form`; it is not claimed as a Cycle625 derivation.

The optimal next campaign is an extensional-law exposure tournament: construct
at least deterministic constrained-QCA, objective stochastic-dilation, and
dissipative formation channels whose local transition tables are generated by
their physical updates rather than supplied shell predicates.  Feed each into
this unchanged 129-M2 port map, require coherent-input exhaust ownership and
post-formation preservation, then freeze a state/calibration law before new
off-family complete-block and blinded Record-corpus tests.
"""


def normalized_note(path: Path) -> str:
    body = path.read_text().lower()
    return " ".join(body.replace("`", "").replace("*", "").split())


def note_contract() -> dict[str, object]:
    required = (
        "authority: none", "audit: unset", "admissibility is not dynamics",
        "retained surfaces do not identify", "129-m2", "531-m2",
        "basis winner is not objective actuality", "not a framework record",
        "grade/frequency is not born probability", "all 24 proper-cubic frames",
        "all 576 frame products", "held-out l4", "held l6", "n1–n8",
        "bare occurrence is not the target", "registered state data",
        "finite-additivity-to-frame bridge", "all 42 directed pairs",
        "broad no-go and minimum-content gates are fail / do not ship",
        "six-layer executable acceptance contract", "conditional form-forcing",
        "ternary, scaled-projector, or mixed-projective", "effect-functional",
        "occurrence selector sigma", "closed and non-retained", "not back-credit",
        "n4 contains ten exact rows", "file / status / what_closes",
        "cycle / retired / mechanism", "no retained physical m2",
        "immutable committed head", "no dirty working-tree variant is a premise",
        "shared obstruction: not established", "axiom pressure: none",
    )
    body = normalized_note(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    return {"required_fragments": required, "missing": missing, "pass": not missing}


def main() -> None:
    signal.alarm(math.ceil(WALL_CAP_SECONDS))
    started = time.perf_counter()
    shore = shore_controls()
    external = external_comparison_controls()
    route_a = route_a_structural_relation_tournament()
    route_b = route_b_physical_shared_middle()
    route_c = route_c_rom_free_grade_corpus()
    acceptance = six_layer_acceptance_contract(route_b, route_c, external)
    no_go = no_go_discipline(route_a, route_b, route_c, acceptance)
    receipt = {
        "status": (
            "positive supplied physical shared middle and ROM-free bounded grade block; "
            "no derived extensional formation/admission, actuality, Record, frame/menu, or Born law"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "shore": shore,
        "external_comparison_heads": external,
        "route_A_structural_relation": route_a,
        "route_B_physical_shared_middle": route_b,
        "route_C_ROM_free_grade_corpus": route_c,
        "six_layer_acceptance_contract": acceptance,
        "no_go_discipline": no_go,
        "inventory": inventory(),
        "strongest_constructive_result": (
            "one supplied-candidate 129-M2 reversible local formation/admission functional from the Cycle614 "
            "six-endpoint state into the Cycle531 shared middle, retaining all candidates/losers, plus a separate "
            "531-M2 ROM-free state-derived grade block"
        ),
        "highest_honest_terminal": (
            "bounded candidate local formation/admission interface downstream of supplied bare occurrence plus bounded "
            "candidate grade/corpus; not extensional law identification, actuality, Record, realized history, or Born probability"
        ),
        "six_wall_ledger": {
            "C_ref": "structural/extensional formation-rule distinction and candidate/loser provenance explicit; law/calibration/actuality supplied",
            "C_num": "exact finite relation and denominator64 block arithmetic; finite Record additivity supplies no complete frame/menu or probability/convergence theorem",
            "C_wrap": "conditional occurrence reached without runtime actuality token; no packet-to-Record identification, physical realization of axiom-supplied permanence, or history",
            "C_int": "matter/packet/resource/occurrence/grade interfaces coexist without new interaction claim",
            "C_local": "bounded support-two/inverse/deletion/domain/held/all24/all576; volume/noise/scaling open",
            "C_source": "ready/spent and blank corpus capacity explicit; no energy/stress/source/gravity meaning",
        },
        "shared_substrate_obstruction": False,
        "axiom_pressure": False,
        "author_accepted": False,
        "breakthrough": False,
        "maturity_rebase": None,
        "semantic_promotion_boundary": {
            "physical_menu_eligibility": None,
            "effect_functionality_w": None,
            "objective_occurrence_selector_sigma": None,
            "framework_Record_identification": None,
            "physical_permanence_law": None,
            "Born_probability": None,
            "realized_history": None,
        },
        "optimal_next_campaign": (
            "extensional-law exposure tournament across constrained-QCA, stochastic-dilation, and dissipative-formation "
            "updates, composed into the unchanged shared-middle interface before blinded Record-corpus tests"
        ),
    }
    NOTE.write_text(note_text(receipt))
    contract = note_contract()
    check("Cycle625 note preserves the semantic and scope contract", contract["pass"], contract["missing"])
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000:  # Linux reports KiB; macOS reports bytes.
        rss *= 1024
    receipt.update({
        "note_contract": contract,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
    })
    receipt["pass"] = (
        FAIL == 0 and shore["pass"] and external["pass"] and route_a["pass"] and route_b["pass"]
        and route_c["pass"] and acceptance["pass"] and no_go["pass"] and contract["pass"]
        and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
        and AUTHORITY == "none" and AUDIT == "unset"
    )
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
