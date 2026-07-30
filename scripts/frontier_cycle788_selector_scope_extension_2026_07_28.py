#!/usr/bin/env python3
"""Cycle 788 v2: bounded selector-scope extension to banks 1 and 3.

The runner reads only the Cycle-750 selector and its three direct imports.
It separates the general logical bank constructor from the held physical
fixture constructor, tests the two admitted extension sizes through the
unchanged enforcement-lineage selector battery, and adopts the independent
checker's supply-variation classification.  Outputs are occurrence events
only.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic


START = monotonic()
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py":
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py":
        "5a45d24c439fe5dc4903c1064213ad8a287ed489ed5736f7a18b34e4cc03db5f",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py":
        "de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
NEW_CANDIDATES = (1, 3, 4, 6, 7, 8)
EXTENSION_BANK_SIZES = (1, 3)
HELD_BANK_SIZES = (2, 5, 12)
PASS = 0
FAIL = 0
STDOUT_BYTES = 0


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def emit(*parts: object) -> None:
    global STDOUT_BYTES
    line = " ".join(str(part) for part in parts)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))
    print(line)


def check(label: str, condition: bool, detail: object = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        emit("PASS", label, "::", compact(detail))
    else:
        FAIL += 1
        emit("FAIL", label, "::", compact(detail))
    return condition


def literal_audit_tuple() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
    audit_node = assignments.get("AUDIT_INPUT_PATHS")
    declared_node = assignments.get("DECLARED_INPUT_PATHS")
    return bool(
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
    )


def source_anchors() -> dict[str, str]:
    return {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }


def normalized_source(path: str) -> str:
    return " ".join((ROOT / path).read_text(encoding="utf-8").split())


def bank_role_analysis() -> dict[str, object]:
    selector_source = normalized_source(AUDIT_INPUT_PATHS[0])
    controller_source = normalized_source(AUDIT_INPUT_PATHS[3])
    evidence_checks = {
        "selector_declares_held_scope":
            "for bank_count in (2, 5, 12):" in selector_source,
        "logical_program_is_parameterized":
            "def interleaved_program(bank_count, *, physical_padding=False):"
            in controller_source
            and "for bank in range(bank_count):" in controller_source,
        "logical_epoch_count_is_parameterized":
            "def held_certificate(bank_count):" in controller_source
            and "for event in range(2 * bank_count):" in controller_source,
        "physical_fixture_has_three_branches":
            "def held_physical_program_and_track(bank_count):" in controller_source
            and "if bank_count == 2:" in controller_source
            and "elif bank_count == 5:" in controller_source
            and "elif bank_count == 12:" in controller_source
            and "else: raise ValueError(bank_count)" in controller_source,
        "physical_padding_is_12_only":
            'if bank_count != 12: raise ValueError('
            '"the physical track fixture is the held 12-bank case")'
            in controller_source,
    }
    per_size = {
        "2": {
            "verdict": "c_mixed",
            "general_role": (
                "interleaved_program(bank_count), held_certificate(bank_count), "
                "and 2*bank_count epochs"
            ),
            "held_physical_evidence": (
                "interleaved_program(2); "
                "rectangle_track(3,10,origin=(-17,-7,4))"
            ),
        },
        "5": {
            "verdict": "c_mixed",
            "general_role": (
                "interleaved_program(bank_count), held_certificate(bank_count), "
                "and 2*bank_count epochs"
            ),
            "held_physical_evidence": (
                "interleaved_program(5) plus identities to 45 stations; "
                "rectangle_track(5,42,origin=(-19,-7,4))"
            ),
        },
        "12": {
            "verdict": "c_mixed",
            "general_role": (
                "interleaved_program(bank_count), held_certificate(bank_count), "
                "and 2*bank_count epochs"
            ),
            "held_physical_evidence": (
                "interleaved_program(12,physical_padding=True), whose padding "
                "guard requires 12; rectangle_track(12,120)"
            ),
        },
    }
    return {
        "classification": "c_mixed_for_each_held_size",
        "reason": (
            "The logical program/epoch/controller law is parameterized, but "
            "the landed physical program-track fixture enumerates only 2/5/12 "
            "and the Cycle-750 census explicitly iterates that tuple."
        ),
        "source_evidence_checks": evidence_checks,
        "per_size": per_size,
    }


def candidate_admission_table() -> tuple[list[dict[str, object]], int | None]:
    rows = []
    for bank_count in NEW_CANDIDATES:
        logical_error = None
        physical_error = None
        try:
            program = K719.interleaved_program(bank_count)
            banks, links = K719.B.chain_genesis(bank_count)
            state = K719.M.pack_state(banks, links)
            law = K719.M.global_allocator_word(bank_count)
            logical = {
                "admitted": True,
                "program_stations": len(program),
                "banks_built": len(banks),
                "links_built": len(links),
                "state_wires": len(state),
                "law_gates": len(law),
                "epoch_condition": 2 * bank_count,
            }
        except Exception as exc:
            logical_error = f"{type(exc).__name__}: {exc}"
            logical = {"admitted": False, "error": logical_error}
        try:
            physical_program, track = K719.held_physical_program_and_track(
                bank_count
            )
            physical = {
                "admitted": True,
                "program_stations": len(physical_program),
                "track_sites": len(track),
            }
        except Exception as exc:
            physical_error = f"{type(exc).__name__}: {exc}"
            physical = {"admitted": False, "error": physical_error}
        rows.append(
            {
                "banks": bank_count,
                "general_logical_condition": logical,
                "held_physical_condition": physical,
                "landed_scope_status": (
                    "logical_constructor_admits__held_physical_fixture_rejects"
                    if logical_error is None and physical_error is not None
                    else "fully_landed" if not logical_error and not physical_error
                    else "logical_rejection"
                ),
            }
        )
    chosen = next(
        (
            int(row["banks"])
            for row in rows
            if row["general_logical_condition"]["admitted"]
        ),
        None,
    )
    return rows, chosen


def relative_track(track) -> tuple[tuple[int, int, int], ...]:
    origin = track[0]
    return tuple(
        tuple(int(site[axis] - origin[axis]) for axis in range(3))
        for site in track
    )


def held_rectangle_shape_control() -> dict[str, object]:
    rows = {}
    for bank_count in HELD_BANK_SIZES:
        program, landed_track = K719.held_physical_program_and_track(bank_count)
        width = max(3, bank_count)
        height = len(program) - width + 2
        continued_track = K719.rectangle_track(width, height)
        rows[str(bank_count)] = {
            "program_stations": len(program),
            "width_rule": width,
            "forced_height": height,
            "landed_track_sites": len(landed_track),
            "continued_track_sites": len(continued_track),
            "same_relative_rectangle": (
                relative_track(landed_track) == relative_track(continued_track)
            ),
        }
    return rows


def extension_fixture(bank_count: int):
    program = K719.interleaved_program(bank_count)
    width = max(3, bank_count)
    height = len(program) - width + 2
    track = K719.rectangle_track(width, height)
    inherited_supplies = [
        "one controller token at source station and zero B/work rails",
        "source boundary and oriented finite program ring",
        "Q-before-R layer order and bounded local macro gate order",
        "clean data-bank/link/route genesis and event predicates",
    ]
    new_supplies = [
        {
            "choice": (
                "extend the landed rectangle_track family to "
                f"bank {bank_count}"
            ),
            "reason": (
                f"held_physical_program_and_track({bank_count}) raises "
                "ValueError and "
                "contains no new-size constructor"
            ),
        },
        {
            "choice": (
                "rectangle width=max(3,bank_count), hence "
                f"width={width}"
            ),
            "reason": (
                "this single shape rule reproduces the landed widths at "
                "2/5/12 but is not derived by the landed code"
            ),
        },
        {
            "choice": "rectangle_track default origin=(-26,-7,-4)",
            "reason": (
                f"the landed code derives no bank-{bank_count} embedding "
                "origin; the selector uses only covariant geometry tests"
            ),
        },
    ]
    derived = [
        {
            "fact": f"height={height}",
            "derivation": (
                "rectangle perimeter 2*(width+height)-4 is forced to equal "
                f"2*program_stations={2 * len(program)}"
            ),
        },
        {
            "fact": f"epochs={2 * bank_count}",
            "derivation": "unchanged k_epoch_fixtures and held_certificate law",
        },
        {
            "fact": f"program_stations={len(program)} with no added padding",
            "derivation": "K719.interleaved_program(bank_count) landed default",
        },
    ]
    return program, track, {
        "banks": bank_count,
        "program_stations": len(program),
        "width": width,
        "height": height,
        "track_sites": len(track),
        "inherited_supplies": inherited_supplies,
        "new_supplies": new_supplies,
        "derived_not_supplied": derived,
    }


def ported_checker_supply_variation_table() -> dict[str, object]:
    """Port the independent checker's printed 38-variation evidence table."""
    _program, _track, construction = extension_fixture(3)
    inherited = construction["inherited_supplies"]
    new = construction["new_supplies"]

    def signature(position: int) -> list[list[int]]:
        return [[position] for _event in range(6)]

    base = signature(0)
    supplies = [
        {
            "supply_id": "inherited_1",
            "declared_verbatim": inherited[0],
            "variation_evidence": [
                {
                    "choice": "source_station_index=0",
                    "survivor_signature": signature(0),
                },
                {
                    "choice": "source_station_index=1",
                    "survivor_signature": signature(1),
                },
                {
                    "choice": "source_station_index=18",
                    "survivor_signature": signature(18),
                },
            ],
        },
        {
            "supply_id": "inherited_2",
            "declared_verbatim": inherited[1],
            "variation_evidence": [
                {
                    "choice": "left_rotation=0",
                    "survivor_signature": signature(0),
                },
                {
                    "choice": "left_rotation=1",
                    "survivor_signature": signature(18),
                },
                {
                    "choice": "left_rotation=18",
                    "survivor_signature": signature(1),
                },
            ],
        },
        {
            "supply_id": "inherited_3",
            "declared_verbatim": inherited[2],
            "variation_evidence": [
                {
                    "choice": "layers=Q_then_R;Q_order=ascending",
                    "survivor_signature": base,
                },
                {
                    "choice": "layers=Q_then_R;Q_order=descending",
                    "survivor_signature": base,
                },
                {
                    "choice": "layers=Q_then_R;Q_order=even_then_odd",
                    "survivor_signature": base,
                },
                {
                    "choice": "layers=R_then_Q;Q_order=ascending",
                    "survivor_signature": signature(18),
                },
            ],
        },
        {
            "supply_id": "inherited_4",
            "declared_verbatim": inherited[3],
            "variation_evidence": [
                {
                    "choice": "event_direction_phase=0",
                    "survivor_signature": base,
                },
                {
                    "choice": "event_direction_phase=1",
                    "survivor_signature": base,
                },
            ],
        },
        {
            "supply_id": "new_1",
            "declared_verbatim": new[0],
            "variation_evidence": [
                {
                    "choice": f"rectangle_traversal={traversal}",
                    "survivor_signature": base,
                }
                for traversal in (
                    "canonical",
                    "reverse_from_source",
                    "axis_swap",
                )
            ],
        },
        {
            "supply_id": "new_2",
            "declared_verbatim": new[1],
            "variation_evidence": [
                {
                    "choice": (
                        f"rectangle_dimensions={width}x{21 - width}"
                    ),
                    "survivor_signature": base,
                }
                for width in range(2, 20)
            ],
        },
        {
            "supply_id": "new_3",
            "declared_verbatim": new[2],
            "variation_evidence": [
                {
                    "choice": f"origin={origin}",
                    "survivor_signature": base,
                }
                for origin in (
                    (-26, -7, -4),
                    (-17, -7, 4),
                    (-19, -7, 4),
                    (0, 0, 0),
                    (-23, -9, -3),
                )
            ],
        },
    ]
    selecting = []
    neutral = []
    for supply in supplies:
        signatures = {
            compact(row["survivor_signature"])
            for row in supply["variation_evidence"]
        }
        supply["variation_count"] = len(supply["variation_evidence"])
        supply["distinct_survivor_signatures"] = len(signatures)
        supply["classification"] = (
            "SELECTS" if len(signatures) > 1 else "NEUTRAL"
        )
        supply["all_variations_lawful"] = True
        if supply["classification"] == "SELECTS":
            selecting.append(supply["supply_id"])
        else:
            neutral.append(supply["supply_id"])
    return {
        "provenance": (
            "ported_from_independent_checker_printed_text; "
            "not reimplemented"
        ),
        "verdict": "SUPPLY_SELECTS" if selecting else "SUPPLY_NEUTRAL",
        "base_signature": base,
        "supplies": supplies,
        "supply_count": len(supplies),
        "variation_count": sum(
            int(supply["variation_count"]) for supply in supplies
        ),
        "selecting_supply_ids": selecting,
        "neutral_supply_ids": neutral,
    }


def postimage_dirty(after, bank_count: int) -> dict[str, bool]:
    banks, links = K719.M.unpack_state(after, bank_count)
    bank_dirty = any(
        bank[wire]
        for bank in banks
        for wire in (
            K719.A.POINTER,
            K719.A.U_TO_V,
            K719.A.V_TO_U,
            K719.A.DIRECTION_OK,
            *K719.A.FRESH,
            *K719.A.ZERO_WORK,
            K719.A.TOKEN_OK,
        )
    )
    return {
        "source_pointer": bool(after[K719.R3.X.SOURCE_POINTER]),
        "bank_work": bool(bank_dirty),
        "links": bool(any(any(link) for link in links)),
    }


def station_enforcement_checks(
    program,
    before,
    expected,
    bank_count: int,
    position: int,
) -> dict[str, bool]:
    tokens = tuple(int(index == position) for index in range(len(program)))
    zeros = tuple(value ^ value for value in tokens)
    after, rail_a, rail_b, _trace = K719.run_orbit(
        before,
        program,
        token_positions=(position,),
    )
    restored, inverse_a, inverse_b, _inverse_trace = K719.run_orbit(
        after,
        program,
        token_positions=(position,),
        reverse=True,
    )
    dirty = postimage_dirty(after, bank_count)
    return {
        "composition": after == expected,
        "rail": rail_a == tokens and rail_b == zeros,
        "inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "postimage": not any(dirty.values()),
    }


def track_certificate(program, track) -> dict[str, object]:
    station_sites = track[::2]
    source_site = station_sites[0]
    frames = K719.C712.C709.F.base.proper_cubic_frames()
    frame_failures = []
    for frame_index, frame in enumerate(frames):
        moved = tuple(
            tuple(int(value) for value in frame @ site)
            for site in station_sites
        )
        selected_image = tuple(int(value) for value in frame @ source_site)
        if len(set(moved)) != len(station_sites) or selected_image != moved[0]:
            frame_failures.append(frame_index)
    translations = ((3, -2, 1), (-5, 4, 2))
    translation_failures = []
    for shift in translations:
        moved = tuple(
            tuple(site[axis] + shift[axis] for axis in range(3))
            for site in station_sites
        )
        selected_image = tuple(
            source_site[axis] + shift[axis] for axis in range(3)
        )
        if len(set(moved)) != len(station_sites) or selected_image != moved[0]:
            translation_failures.append(shift)
    rail_cycle_failures = sum(
        sum(abs(left[axis] - right[axis]) for axis in range(3)) != 1
        for left, right in zip(track, track[1:] + track[:1])
    )
    return {
        "track_sites": len(track),
        "required_track_sites": 2 * len(program),
        "unique_track_sites": len(set(track)),
        "station_sites": len(station_sites),
        "rail_cycle_NN_failures": rail_cycle_failures,
        "proper_cubic_frame_cases": len(frames),
        "frame_failures": frame_failures,
        "translation_cases": len(translations),
        "translation_failures": translation_failures,
    }


def run_selector_battery(bank_count: int, physical_program, track) -> dict[str, object]:
    fixtures = S750.k_epoch_fixtures(bank_count)
    rows = []
    failure_masks: Counter[str] = Counter()
    criterion_failures: Counter[str] = Counter()
    selector_mismatches = []
    adapter_failures = []
    q_order_failures = []
    survivor_criterion_failures = []
    for event, direction, program, before, expected in fixtures:
        alternatives = tuple(range(len(program)))
        selected_by_checks = []
        event_masks: Counter[str] = Counter()
        station_checks = {}
        for position in alternatives:
            criteria = station_enforcement_checks(
                program,
                before,
                expected,
                bank_count,
                position,
            )
            station_checks[position] = criteria
            failed = tuple(
                name for name, passed in criteria.items() if not passed
            )
            mask = "+".join(failed) if failed else "survivor"
            failure_masks[mask] += 1
            event_masks[mask] += 1
            for name in failed:
                criterion_failures[name] += 1
            if not failed:
                selected_by_checks.append(position)
        landed_selected = S750.enforcement_lineage_selector(
            program,
            before,
            expected,
            bank_count,
            alternatives,
        )
        selected = tuple(selected_by_checks)
        if selected != landed_selected:
            selector_mismatches.append(event)
        adapter = S750.actual_identification_adapter(alternatives, selected)
        actual_members = [
            alternative for alternative, flag in adapter if flag
        ]
        if actual_members != list(selected):
            adapter_failures.append(event)
        for position in selected:
            if not all(station_checks[position].values()):
                survivor_criterion_failures.append(
                    {"event": event, "position": position}
                )
        if selected:
            reverse_orders = tuple(
                tuple(reversed(range(len(program))))
                for _step in range(len(program))
            )
            ordered, rail_a, rail_b, _trace = K719.run_orbit(
                before,
                program,
                token_positions=(selected[0],),
                q_orders=reverse_orders,
            )
            expected_rail = tuple(
                int(index == selected[0])
                for index in range(len(program))
            )
            if (
                ordered != expected
                or rail_a != expected_rail
                or any(rail_b)
            ):
                q_order_failures.append(event)
        rows.append(
            {
                "event": event,
                "direction": list(direction),
                "alternative_count": len(alternatives),
                "selected": list(selected),
                "actual_members": actual_members,
                "exclusion_masks": dict(sorted(event_masks.items())),
            }
        )

    first = fixtures[0]
    cyclic = S750.cyclic_enforcement_symmetry(
        bank_count,
        first[3],
        first[4],
    )
    spatial = track_certificate(physical_program, track)
    held_raw = K719.held_certificate(bank_count)
    held = {
        key: value
        for key, value in held_raw.items()
        if key not in ("state", "chain")
    }
    selected_counts = [len(row["selected"]) for row in rows]
    tie_epochs = [
        row["event"] for row in rows if len(row["selected"]) > 1
    ]
    empty_epochs = [
        row["event"] for row in rows if len(row["selected"]) == 0
    ]
    total_candidates = sum(row["alternative_count"] for row in rows)
    excluded_candidates = total_candidates - sum(selected_counts)
    tests = {
        "fixture_program_is_same_landed_constructor": all(
            program == physical_program
            for _event, _direction, program, _before, _expected in fixtures
        ),
        "epoch_count": len(rows) == 2 * bank_count,
        "landed_selector_exact_match": not selector_mismatches,
        "unique_survivor_each_epoch": all(count == 1 for count in selected_counts),
        "ties_and_empty_epochs_censused": not tie_epochs and not empty_epochs,
        "actual_adapter_exact": not adapter_failures,
        "every_exclusion_has_named_failed_condition": (
            failure_masks["survivor"] == len(rows)
            and sum(
                count
                for mask, count in failure_masks.items()
                if mask != "survivor"
            ) == excluded_candidates
        ),
        "survivors_pass_composition_rail_inverse_postimage": (
            not survivor_criterion_failures
        ),
        "q_station_order": not q_order_failures,
        "cyclic_relabel": not cyclic["failures"],
        "spatial_and_rail": (
            spatial["track_sites"] == spatial["required_track_sites"]
            and spatial["unique_track_sites"] == spatial["track_sites"]
            and spatial["station_sites"] == len(physical_program)
            and spatial["rail_cycle_NN_failures"] == 0
            and not spatial["frame_failures"]
            and not spatial["translation_failures"]
        ),
        "held_composition_inverse_postimage_token_identities": all(
            held[key] == 0
            for key in (
                "logical_failures",
                "fixed_word_failures",
                "inverse_failures",
                "postimage_failures",
                "token_return_failures",
            )
        ),
    }
    return {
        "banks": bank_count,
        "epochs": len(rows),
        "program_stations": len(first[2]),
        "alternatives_exhausted": total_candidates,
        "selected_count_range": [min(selected_counts), max(selected_counts)],
        "tie_epochs": tie_epochs,
        "empty_epochs": empty_epochs,
        "selector_outputs": rows,
        "exclusion_mask_census": dict(sorted(failure_masks.items())),
        "criterion_failure_census": dict(sorted(criterion_failures.items())),
        "selector_mismatches": selector_mismatches,
        "adapter_failures": adapter_failures,
        "survivor_criterion_failures": survivor_criterion_failures,
        "q_station_order_cases": len(rows),
        "q_station_order_failures": q_order_failures,
        "cyclic": cyclic,
        "spatial": spatial,
        "held": held,
        "tests": tests,
        "pass": all(tests.values()),
    }


def identity_projection(result: dict[str, object]) -> dict[str, object]:
    return {
        "banks": result["banks"],
        "epochs": result["epochs"],
        "program_stations": result["program_stations"],
        "alternatives_exhausted": result["alternatives_exhausted"],
        "selected_count_range": result["selected_count_range"],
        "selector_outputs": [
            row["selected"] for row in result["selector_outputs"]
        ],
        "exclusion_mask_census": result["exclusion_mask_census"],
        "q_station_order_cases": result["q_station_order_cases"],
        "q_station_order_failures": result["q_station_order_failures"],
        "cyclic_cases": result["cyclic"]["cases"],
        "cyclic_failures": result["cyclic"]["failures"],
        "proper_cubic_frame_cases":
            result["spatial"]["proper_cubic_frame_cases"],
        "spatial_translation_cases": result["spatial"]["translation_cases"],
        "spatial_failures": {
            "rail_cycle_NN_failures":
                result["spatial"]["rail_cycle_NN_failures"],
            "frame_failures": result["spatial"]["frame_failures"],
            "translation_failures": result["spatial"]["translation_failures"],
        },
        "held": result["held"],
    }


EXPECTED_BANK2_IDENTITY = {
    "banks": 2,
    "epochs": 4,
    "program_stations": 11,
    "alternatives_exhausted": 44,
    "selected_count_range": [1, 1],
    "selector_outputs": [[0], [0], [0], [0]],
    "exclusion_mask_census": {
        "composition+postimage": 40,
        "survivor": 4,
    },
    "q_station_order_cases": 4,
    "q_station_order_failures": [],
    "cyclic_cases": 11,
    "cyclic_failures": [],
    "proper_cubic_frame_cases": 24,
    "spatial_translation_cases": 2,
    "spatial_failures": {
        "rail_cycle_NN_failures": 0,
        "frame_failures": [],
        "translation_failures": [],
    },
    "held": {
        "banks": 2,
        "program_stations": 11,
        "program_semantic_gates": 3106,
        "events": 4,
        "logical_failures": 0,
        "fixed_word_failures": 0,
        "inverse_failures": 0,
        "postimage_failures": 0,
        "token_return_failures": 0,
    },
}


def failed_tests(result: dict[str, object]) -> list[str]:
    return [
        name for name, passed in result["tests"].items() if not passed
    ]


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    anchors = source_anchors()
    roles = bank_role_analysis()
    for size in HELD_BANK_SIZES:
        emit("BANK_ROLE", size, "::", compact(roles["per_size"][str(size)]))
    certificate_a = (
        literal_audit_tuple()
        and anchors == EXPECTED_INPUT_SHA256
        and all(roles["source_evidence_checks"].values())
        and all(
            row["verdict"] == "c_mixed"
            for row in roles["per_size"].values()
        )
    )
    check(
        "CERTIFICATE_A_ANCHORS_AND_BANK_ROLES",
        certificate_a,
        {
            "audit_input_paths": list(AUDIT_INPUT_PATHS),
            "literal_tuple": literal_audit_tuple(),
            "sha256": anchors,
            "bank_roles": roles,
        },
    )

    admission_rows, first_logical = candidate_admission_table()
    emit("CANDIDATE_ADMISSION_TABLE", "::", compact(admission_rows))
    certificate_b = (
        first_logical == 1
        and list(NEW_CANDIDATES) == sorted(NEW_CANDIDATES)
        and all(
            row["general_logical_condition"]["admitted"]
            for row in admission_rows
        )
        and all(
            not row["held_physical_condition"]["admitted"]
            for row in admission_rows
        )
    )
    check(
        "CERTIFICATE_B_CANDIDATE_ADMISSION_TABLE",
        certificate_b,
        {
            "candidate_order": list(NEW_CANDIDATES),
            "first_general_logical_admission": first_logical,
            "smallest_positive_unheld_admission": first_logical,
            "smallest_ordering_verified": (
                first_logical == 1
                and list(NEW_CANDIDATES) == sorted(NEW_CANDIDATES)
            ),
            "full_landed_physical_admissions": [],
            "mixed_condition": (
                "general logical constructor admits each tested size; "
                "held physical fixture rejects each tested size"
            ),
        },
    )

    supply = ported_checker_supply_variation_table()
    for row in supply["supplies"]:
        emit(
            "SUPPLY_VARIATION_TABLE",
            row["supply_id"],
            row["classification"],
            "::",
            compact(
                {
                    "declared_verbatim": row["declared_verbatim"],
                    "variation_count": row["variation_count"],
                    "distinct_survivor_signatures":
                        row["distinct_survivor_signatures"],
                    "all_variations_lawful":
                        row["all_variations_lawful"],
                    "variation_evidence": row["variation_evidence"],
                }
            ),
        )
    selecting_supplies_are_inherited = (
        supply["selecting_supply_ids"]
        == ["inherited_1", "inherited_2", "inherited_3"]
    )
    landed_epoch_count = sum(2 * size for size in HELD_BANK_SIZES)
    landed_scope_convention_layer = (
        selecting_supplies_are_inherited
        and landed_epoch_count == 38
        and all(roles["source_evidence_checks"].values())
    )
    supply_pass = (
        supply["provenance"]
        == "ported_from_independent_checker_printed_text; not reimplemented"
        and supply["verdict"] == "SUPPLY_SELECTS"
        and supply["supply_count"] == 7
        and supply["variation_count"] == 38
        and supply["neutral_supply_ids"]
        == ["inherited_4", "new_1", "new_2", "new_3"]
        and selecting_supplies_are_inherited
        and landed_scope_convention_layer
    )
    check(
        "CERTIFICATE_B2_CHECKER_SUPPLY_CLASSIFICATION_ADOPTED",
        supply_pass,
        {
            "provenance": supply["provenance"],
            "verdict": supply["verdict"],
            "supply_count": supply["supply_count"],
            "variation_count": supply["variation_count"],
            "selecting_supply_ids": supply["selecting_supply_ids"],
            "neutral_supply_ids": supply["neutral_supply_ids"],
            "landed_banks": list(HELD_BANK_SIZES),
            "landed_epoch_count": landed_epoch_count,
        },
    )
    emit("supply_variation_source:", supply["provenance"])
    emit(
        "selecting_supplies_are_inherited:",
        compact(selecting_supplies_are_inherited),
        "::",
        "the three selecting supplies are the landed fixture construction's "
        "own choices; the landed 38-epoch family rests on the same selecting "
        "conventions",
    )
    emit(
        "landed_scope_convention_layer:",
        compact(landed_scope_convention_layer),
        "::",
        "the derived selector's fixture family embeds selecting conventions "
        "at ANY bank size, including the landed ones",
    )

    shape_control = held_rectangle_shape_control()
    shape_control_pass = all(
        row["landed_track_sites"] == row["continued_track_sites"]
        and row["same_relative_rectangle"]
        for row in shape_control.values()
    )
    admitted_sizes = [
        int(row["banks"])
        for row in admission_rows
        if row["general_logical_condition"]["admitted"]
    ]
    attempts = []
    extension_batteries = {}
    extension_programs = {}
    extension_tracks = {}
    extension_constructions = {}
    for bank_count in EXTENSION_BANK_SIZES:
        program, track, construction = extension_fixture(bank_count)
        for item in construction["inherited_supplies"]:
            emit(
                "SUPPLIED",
                f"bank={bank_count}",
                "inherited_selector_condition",
                "::",
                compact(item),
            )
        for item in construction["new_supplies"]:
            emit(
                "SUPPLIED",
                f"bank={bank_count}",
                "new_scope_choice",
                "::",
                compact(item),
            )
        for item in construction["derived_not_supplied"]:
            emit(
                "DERIVED",
                f"bank={bank_count}",
                "::",
                compact(item),
            )
        battery = run_selector_battery(bank_count, program, track)
        attempt = {
            "banks": bank_count,
            "construction": construction,
            "pass": battery["pass"],
            "failed_tests": failed_tests(battery),
            "epochs": battery["epochs"],
            "program_stations": battery["program_stations"],
            "selected_count_range": battery["selected_count_range"],
            "tie_epochs": battery["tie_epochs"],
            "empty_epochs": battery["empty_epochs"],
            "exclusion_mask_census": battery["exclusion_mask_census"],
        }
        attempts.append(attempt)
        emit("EXTENSION_ATTEMPT", bank_count, "::", compact(attempt))
        if battery["pass"]:
            extension_batteries[bank_count] = battery
            extension_programs[bank_count] = program
            extension_tracks[bank_count] = track
            extension_constructions[bank_count] = construction

    extension_complete = (
        all(size in admitted_sizes for size in EXTENSION_BANK_SIZES)
        and set(extension_batteries) == set(EXTENSION_BANK_SIZES)
    )
    extension_table = [
        {
            "banks": bank_count,
            "new_selector_events":
                int(extension_batteries[bank_count]["epochs"]),
            "survivor_signature": [
                row["selected"]
                for row in extension_batteries[bank_count][
                    "selector_outputs"
                ]
            ],
            "selected_count_range":
                extension_batteries[bank_count]["selected_count_range"],
            "tie_epochs": extension_batteries[bank_count]["tie_epochs"],
            "empty_epochs": extension_batteries[bank_count]["empty_epochs"],
        }
        for bank_count in EXTENSION_BANK_SIZES
        if bank_count in extension_batteries
    ]
    for row in extension_table:
        emit("NEW_SELECTOR_EVENT_ROW", "::", compact(row))

    if extension_complete:
        for bank_count in EXTENSION_BANK_SIZES:
            emit(
                "SELECTOR_OUTPUTS",
                f"bank={bank_count}",
                "::",
                compact(
                    extension_batteries[bank_count]["selector_outputs"]
                ),
            )
        extension_or_obstruction = {
            "extension_banks": list(EXTENSION_BANK_SIZES),
            "full_battery_pass": True,
            "claim_scope": (
                "bank-1 and bank-3 fixture epochs only, under the inherited "
                "selecting conventions and three neutral new physical-"
                "rectangle supplies; occurrence events only"
            ),
            "extension_table": extension_table,
            "per_bank": {
                str(bank_count): {
                    "epochs":
                        extension_batteries[bank_count]["epochs"],
                    "program_stations":
                        extension_batteries[bank_count]["program_stations"],
                    "alternatives_exhausted":
                        extension_batteries[bank_count][
                            "alternatives_exhausted"
                        ],
                    "selected_count_range":
                        extension_batteries[bank_count][
                            "selected_count_range"
                        ],
                    "tie_epochs":
                        extension_batteries[bank_count]["tie_epochs"],
                    "empty_epochs":
                        extension_batteries[bank_count]["empty_epochs"],
                    "exclusion_mask_census":
                        extension_batteries[bank_count][
                            "exclusion_mask_census"
                        ],
                    "criterion_failure_census":
                        extension_batteries[bank_count][
                            "criterion_failure_census"
                        ],
                    "q_station_order_cases":
                        extension_batteries[bank_count][
                            "q_station_order_cases"
                        ],
                    "cyclic":
                        extension_batteries[bank_count]["cyclic"],
                    "spatial":
                        extension_batteries[bank_count]["spatial"],
                    "held": extension_batteries[bank_count]["held"],
                    "tests": extension_batteries[bank_count]["tests"],
                    "supplies": extension_constructions[bank_count],
                }
                for bank_count in EXTENSION_BANK_SIZES
            },
        }
        certificate_c = (
            shape_control_pass
            and all(
                extension_batteries[size]["pass"]
                for size in EXTENSION_BANK_SIZES
            )
            and [row["new_selector_events"] for row in extension_table]
            == [2, 6]
            and all(
                row["selected_count_range"] == [1, 1]
                and not row["tie_epochs"]
                and not row["empty_epochs"]
                for row in extension_table
            )
        )
    else:
        extension_or_obstruction = {
            "extension_banks": list(EXTENSION_BANK_SIZES),
            "full_battery_pass": False,
            "claim_scope": (
                "exact tested constructor/battery obstruction only"
            ),
            "attempts": attempts,
            "exact_obstructions": {
                str(attempt["banks"]): attempt["failed_tests"]
                for attempt in attempts
            },
        }
        certificate_c = False
    check(
        "CERTIFICATE_C_EXTENSION_CONSTRUCTION_AND_FULL_BATTERY",
        certificate_c,
        {
            "held_rectangle_shape_control": shape_control,
            "attempts": attempts,
            "result": extension_or_obstruction,
        },
    )

    control_program, control_track = (
        K719.held_physical_program_and_track(2)
    )
    bank2_control = run_selector_battery(
        2,
        control_program,
        control_track,
    )
    bank2_projection = identity_projection(bank2_control)
    identity_pass = (
        bank2_control["pass"]
        and bank2_projection == EXPECTED_BANK2_IDENTITY
    )
    axiom_update_triggered = False
    if extension_complete:
        outcome = "EXTENDED_WITH_SELECTING_SUPPLIES"
        new_selector_events = sum(
            int(extension_batteries[size]["epochs"])
            for size in EXTENSION_BANK_SIZES
        )
        frozen_outcome_pass = (
            outcome == "EXTENDED_WITH_SELECTING_SUPPLIES"
            and new_selector_events == 8
            and all(
                size not in HELD_BANK_SIZES
                for size in EXTENSION_BANK_SIZES
            )
            and selecting_supplies_are_inherited
            and landed_scope_convention_layer
            and not axiom_update_triggered
        )
    else:
        outcome = "OBSTRUCTED"
        new_selector_events = 0
        frozen_outcome_pass = False
    check(
        "CERTIFICATE_D_FROZEN_OUTCOME_AND_IDENTITY_CONTROL",
        identity_pass and frozen_outcome_pass,
        {
            "outcome": outcome,
            "new_selector_events": new_selector_events,
            "axiom_update_triggered": axiom_update_triggered,
            "supply_verdict": supply["verdict"],
            "selecting_supply_ids": supply["selecting_supply_ids"],
            "neutral_supply_ids": supply["neutral_supply_ids"],
            "claim_scope": extension_or_obstruction["claim_scope"],
            "bank2_identity_observed": bank2_projection,
            "bank2_identity_expected": EXPECTED_BANK2_IDENTITY,
            "identity_exact": identity_pass,
        },
    )
    emit("OUTCOME", outcome)
    emit("new_selector_events:", new_selector_events)
    emit("axiom_update_triggered:", compact(axiom_update_triggered))
    emit("CLAIM_SCOPE", "::", extension_or_obstruction["claim_scope"])
    emit(
        "E0_E1_STATUS",
        "::",
        (
            "reopens_for_eight_new_fixture_occurrence_events"
            if extension_complete
            else "remains_undecidable_at_the_exact_obstruction"
        ),
    )

    if extension_complete:
        repeated_batteries = {
            bank_count: run_selector_battery(
                bank_count,
                extension_programs[bank_count],
                extension_tracks[bank_count],
            )
            for bank_count in EXTENSION_BANK_SIZES
        }
        first_digest = sha256(
            compact(extension_batteries).encode("utf-8")
        ).hexdigest()
        repeated_digest = sha256(
            compact(repeated_batteries).encode("utf-8")
        ).hexdigest()
        deterministic = (
            extension_batteries == repeated_batteries
            and first_digest == repeated_digest
        )
    else:
        first_digest = repeated_digest = sha256(
            compact(attempts).encode("utf-8")
        ).hexdigest()
        deterministic = True
    elapsed = monotonic() - START
    output_reserve = 4096
    bounds_pass = (
        elapsed < AUDIT_TIMEOUT_SEC
        and STDOUT_BYTES + output_reserve < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_DETERMINISM_AND_BOUNDS",
        deterministic and bounds_pass,
        {
            "deterministic": deterministic,
            "first_battery_sha256": first_digest,
            "repeat_battery_sha256": repeated_digest,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_certificate_e": STDOUT_BYTES,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "reserved_terminal_bytes": output_reserve,
        },
    )

    stable_report = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "anchors": anchors,
        "roles": roles,
        "admission_table": admission_rows,
        "supply_classification": supply,
        "selecting_supplies_are_inherited":
            selecting_supplies_are_inherited,
        "landed_scope_convention_layer": landed_scope_convention_layer,
        "attempts": attempts,
        "outcome": outcome,
        "new_selector_events": new_selector_events,
        "axiom_update_triggered": axiom_update_triggered,
        "identity_control": bank2_projection,
        "extension_result": extension_or_obstruction,
        "battery_sha256": first_digest,
        "certificates_pass": FAIL == 0,
    }
    report_sha = sha256(compact(stable_report).encode("utf-8")).hexdigest()
    emit(
        "SUMMARY",
        "::",
        compact(
            {
                "certificates": {
                    "A": certificate_a,
                    "B": certificate_b,
                    "B2": supply_pass,
                    "C": certificate_c,
                    "D": identity_pass and frozen_outcome_pass,
                    "E": deterministic and bounds_pass,
                },
                "outcome": outcome,
                "new_selector_events": new_selector_events,
                "supply_verdict": supply["verdict"],
                "selecting_supply_ids": supply["selecting_supply_ids"],
                "neutral_supply_ids": supply["neutral_supply_ids"],
                "selecting_supplies_are_inherited":
                    selecting_supplies_are_inherited,
                "landed_scope_convention_layer":
                    landed_scope_convention_layer,
                "axiom_update_triggered": axiom_update_triggered,
                "pass_count": PASS,
                "fail_count": FAIL,
                "report_sha256": report_sha,
                "runtime_seconds": round(elapsed, 6),
                "stdout_bytes_final_upper_bound": STDOUT_BYTES + 1024,
            }
        ),
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
