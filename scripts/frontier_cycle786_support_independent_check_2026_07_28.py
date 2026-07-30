#!/usr/bin/env python3
"""Cycle 786 independent adversarial check of the claimed support ceiling.

This runner hunts for a landed selector-epoch -> specific-origin join.  It
reports a refutation if one exists and otherwise reports the complete landed
interface census supporting only the orientation partition.

Boundary: counts only; no weights, no rate law, no probability; any needed
convention must be declared, never silently used.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha256
from math import comb
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 1500
AUDIT_STDOUT_MAX_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

SELECTOR_MODULE_NAME = "frontier_cycle750_actual_selector_stretch_2026_07_28"
SELECTOR_LANDED_GIT_BLOB = "0a8f4562d28f12ed64130b3c3b23fccab677d333"
BLOCKLISTED_PRIMARY_PATH = (
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py"
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]: "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[1]: "ef9398b3f27dcbb540446d6c5c165c5803014cffa37da59071751810a7ac9978",
    AUDIT_INPUT_PATHS[2]: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[3]: "d5403ebbf51d8ecfaf621d5e0983d333b8df9a7d589145095b598c530ac15ab4",
}
BOUNDARY_VERBATIM = (
    "counts only; no weights, no rate law, no probability; any needed "
    "convention must be declared, never silently used."
)


import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719
import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def selector_source_bytes() -> tuple[bytes, str]:
    """Read Cycle 750 from its path or the immutable landed blob."""
    path = ROOT / AUDIT_INPUT_PATHS[0]
    if path.is_file():
        return path.read_bytes(), "worktree"
    completed = subprocess.run(
        ("git", "cat-file", "blob", SELECTOR_LANDED_GIT_BLOB),
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return completed.stdout, "landed_git_blob"


def load_selector() -> tuple[ModuleType, bytes, str]:
    source, locator = selector_source_bytes()
    module = ModuleType(SELECTOR_MODULE_NAME)
    module.__file__ = str(ROOT / AUDIT_INPUT_PATHS[0])
    module.__package__ = ""
    sys.modules[SELECTOR_MODULE_NAME] = module
    exec(compile(source, module.__file__, "exec"), module.__dict__)
    return module, source, locator


S750, S750_SOURCE, S750_SOURCE_LOCATOR = load_selector()


def literal_audit_tuple() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            continue
        return (
            isinstance(node.value, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in node.value.elts
            )
            and tuple(ast.literal_eval(node.value)) == AUDIT_INPUT_PATHS
        )
    return False


def input_sources() -> dict[str, bytes]:
    return {
        AUDIT_INPUT_PATHS[0]: S750_SOURCE,
        **{
            path: (ROOT / path).read_bytes()
            for path in AUDIT_INPUT_PATHS[1:]
        },
    }


def packet_write_code(projection: dict[str, object]) -> int:
    fields = (
        "endpoint",
        "carry",
        "binder",
        "valid",
        "actuality",
        "admissibility",
        "law_domain",
    )
    return sum(int(projection[field]) << bit for bit, field in enumerate(fields))


def one_hot_index(bits: tuple[int, ...]) -> int | None:
    if sum(map(int, bits)) != 1:
        return None
    return next(index for index, value in enumerate(bits) if value)


def branch_target(basis: int) -> int:
    matter = basis & ((1 << 12) - 1)
    if matter.bit_count() != 1:
        raise AssertionError(("non-one-hot matter branch", matter))
    return matter.bit_length() - 1


JOIN_TOKENS = (
    "alternative",
    "bank",
    "content",
    "direction",
    "event",
    "identity",
    "matter",
    "orientation",
    "origin",
    "pointer",
    "record",
    "selected",
    "site",
    "station",
    "target",
)


def ast_interface_census(path: str, source: bytes) -> dict[str, object]:
    """Inventory the complete top-level API and every join-shaped identifier."""
    tree = ast.parse(source, filename=path)
    functions = []
    relevant_signatures = []
    relevant_identifiers = set()
    direct_repo_imports = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            signature = {
                "name": node.name,
                "arguments": [argument.arg for argument in node.args.args],
            }
            functions.append(signature)
            signature_text = node.name + " " + " ".join(signature["arguments"])
            if any(token in signature_text.lower() for token in JOIN_TOKENS):
                relevant_signatures.append(signature)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith(("frontier_", "physical_")):
                    direct_repo_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith(("frontier_", "physical_")):
                direct_repo_imports.append(node.module)
    for node in ast.walk(tree):
        names = []
        if isinstance(node, ast.Name):
            names.append(node.id)
        elif isinstance(node, ast.Attribute):
            names.append(node.attr)
        elif isinstance(node, ast.arg):
            names.append(node.arg)
        for name in names:
            if any(token in name.lower() for token in JOIN_TOKENS):
                relevant_identifiers.add(name)
    return {
        "path": path,
        "source_bytes": len(source),
        "sha256": sha256(source).hexdigest(),
        "ast_nodes_examined": sum(1 for _node in ast.walk(tree)),
        "top_level_functions": functions,
        "join_relevant_function_signatures": relevant_signatures,
        "join_relevant_identifiers": sorted(relevant_identifiers),
        "direct_repo_imports": sorted(direct_repo_imports),
    }


def blocklist_census() -> dict[str, object]:
    """Parse blocklisted primaries as inert text and prove none was imported."""
    primary = ROOT / BLOCKLISTED_PRIMARY_PATH
    cycle785 = sorted((ROOT / "scripts").glob("*cycle785*.py"))
    paths = [primary, *cycle785]
    parsed = []
    parse_failures = []
    for path in paths:
        try:
            source = path.read_bytes()
            tree = ast.parse(source, filename=str(path))
            parsed.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": sha256(source).hexdigest(),
                    "ast_nodes": sum(1 for _node in ast.walk(tree)),
                    "execution": "BLOCKLISTED_TEXT_AST_ONLY",
                }
            )
        except (OSError, SyntaxError) as error:
            parse_failures.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "error": type(error).__name__,
                }
            )
    blocked_resolved = {path.resolve() for path in paths}
    loaded = []
    for name, module in tuple(sys.modules.items()):
        module_file = getattr(module, "__file__", None)
        if module_file and Path(module_file).resolve() in blocked_resolved:
            loaded.append(name)
    return {
        "required_cycle786_primary_present": primary.is_file(),
        "cycle785_copies_present": [
            path.relative_to(ROOT).as_posix() for path in cycle785
        ],
        "parsed_text_ast_only": parsed,
        "parse_failures": parse_failures,
        "loaded_blocklisted_modules": sorted(loaded),
        "audit_input_overlap": sorted(
            set(AUDIT_INPUT_PATHS)
            & {path.relative_to(ROOT).as_posix() for path in paths}
        ),
    }


def derive_origin_catalog() -> tuple[list[dict[str, object]], dict[str, object]]:
    """Independently derive support-only formation and one write per origin."""
    transitions, transition_certificate = C719.instrument_transition()
    layout = K719.M.R12.full_wire_layout()
    matter_sites = tuple(layout["wire_sites"][:12])
    catalog = []
    for origin in range(12):
        banks0, links0 = C719.B.chain_genesis(C719.BANKS)
        genesis_chain, _genesis_order = C719.B.decode_local_graph(banks0, links0)
        initial = C719.tuple_to_int(
            C719.M.pack_state(banks0, links0, matter=1 << origin)
        )
        branches = C719.C713.apply_sparse_word(
            {initial: 1.0 + 0.0j},
            C719.MATTER_WORD,
        )
        by_target = {branch_target(basis): basis for basis in branches}
        if not (len(branches) == len(by_target) == 6):
            raise AssertionError(("formation support not six targets", origin))

        support = []
        for branch_index, (target, orientation, _coefficient) in enumerate(
            transitions[origin]
        ):
            basis = by_target[int(target)]
            pointer = (basis >> C719.R3_SOURCE_POINTER()) & 1
            support.append(
                {
                    "branch_index": branch_index,
                    "target": int(target),
                    "orientation": int(orientation),
                    "source_pointer": int(pointer),
                }
            )
        record_rows = [row for row in support if row["source_pointer"]]
        if len(record_rows) != 1 or int(record_rows[0]["orientation"]) == 0:
            raise AssertionError(("record-shaped support not unique", origin))
        record = record_rows[0]
        record_target = int(record["target"])
        written, write_control = C719.sparse_controller_orbit(
            {by_target[record_target]: 1.0 + 0.0j},
            C719.PROGRAM,
        )
        if len(written) != 1:
            raise AssertionError(("write not classical", origin, len(written)))
        written_bits = C719.int_to_tuple(next(iter(written)))
        banks1, links1 = C719.M.unpack_state(written_bits, C719.BANKS)
        written_chain, written_order = C719.B.decode_local_graph(banks1, links1)
        projection = C719.A.packet_projection(banks1[0], 0)
        if projection is None:
            raise AssertionError(("missing record packet", origin))
        catalog.append(
            {
                "origin": origin,
                "origin_matter_site": list(matter_sites[origin]),
                "transition_support": support,
                "record_branch_index": int(record["branch_index"]),
                "record_target": record_target,
                "record_target_matter_site": list(matter_sites[record_target]),
                "record_orientation": int(record["orientation"]),
                "record_source_pointer": int(record["source_pointer"]),
                "write_pipeline": [
                    len(genesis_chain.cells),
                    int(record["source_pointer"]),
                    packet_write_code(projection),
                ],
                "postwrite_source_pointer": int(
                    written_bits[C719.R3_SOURCE_POINTER()]
                ),
                "written_event_cells": len(written_chain.cells),
                "written_decode_order": [
                    list(pair) for pair in written_order
                ],
                "write_control": write_control,
            }
        )
    signatures = {
        orientation: sorted(
            {
                compact(row["transition_support"])
                for row in catalog
                if row["record_orientation"] == orientation
            }
        )
        for orientation in (-1, 1)
    }
    evidence = {
        "transition_certificate": transition_certificate,
        "matter_origin_sites": [list(site) for site in matter_sites],
        "origins": len(catalog),
        "support_branches": sum(
            len(row["transition_support"]) for row in catalog
        ),
        "record_branches": sum(
            sum(
                int(branch["source_pointer"])
                for branch in row["transition_support"]
            )
            for row in catalog
        ),
        "distinct_support_signatures_by_orientation": {
            str(orientation): len(rows)
            for orientation, rows in signatures.items()
        },
        "support_signatures_by_orientation": signatures,
    }
    return catalog, evidence


def selector_epoch_rows(
    catalog: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Invoke the selector independently over every landed held fixture."""
    orientation_origins = {
        orientation: tuple(
            int(row["origin"])
            for row in catalog
            if row["record_orientation"] == orientation
        )
        for orientation in (-1, 1)
    }
    rows = []
    ordinal = 0
    for bank_count in (2, 5, 12):
        _held_program, track = K719.held_physical_program_and_track(bank_count)
        fixtures = S750.k_epoch_fixtures(bank_count)
        for event, direction, program, before, expected in fixtures:
            alternatives = tuple(range(len(program)))
            selected = S750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            banks, links = K719.M.unpack_state(expected, bank_count)
            chain, decode_order = K719.B.decode_local_graph(banks, links)
            cell = chain.cells[event]
            before_matter_mode = one_hot_index(tuple(map(int, before[:12])))
            after_matter_mode = one_hot_index(tuple(map(int, expected[:12])))
            selected_sites = [
                list(track[2 * position]) for position in selected
            ]
            rows.append(
                {
                    "epoch_ordinal": ordinal,
                    "fixture": f"banks{bank_count}_event{event}",
                    "banks": bank_count,
                    "event": event,
                    "direction": list(direction),
                    "alternative_count": len(alternatives),
                    "selected_alternatives": list(selected),
                    "selected_program_rows": [
                        [program[position][0], int(program[position][1])]
                        for position in selected
                    ],
                    "selected_station_sites": selected_sites,
                    "before_matter_mode": before_matter_mode,
                    "after_matter_mode": after_matter_mode,
                    "source_pointer_before": int(
                        before[C719.R3_SOURCE_POINTER()]
                    ),
                    "source_pointer_after": int(
                        expected[C719.R3_SOURCE_POINTER()]
                    ),
                    "event_cell": {
                        "identity": int(cell.identity),
                        "rotor": int(cell.rotor),
                        "carry": int(cell.carry),
                        "predecessor": cell.predecessor,
                        "binder": int(cell.binder),
                        "valid": int(cell.valid),
                        "orientation": int(cell.orientation),
                    },
                    "decode_order_tail": list(decode_order[-1]),
                    "origin_candidates": list(
                        orientation_origins[int(cell.orientation)]
                    ),
                }
            )
            ordinal += 1
    return rows


def direct_origin_probe_census(
    epochs: list[dict[str, object]],
    catalog: list[dict[str, object]],
) -> dict[str, object]:
    """Try every same-shaped selector field as a direct origin key."""
    origin_by_site = {
        tuple(row["origin_matter_site"]): int(row["origin"])
        for row in catalog
    }
    probes: dict[str, list[int | None]] = {
        "fixture_matter_mode_as_source_origin": [],
        "selected_alternative_as_source_origin": [],
        "selected_program_row_index_as_source_origin": [],
        "epoch_ordinal_as_source_origin": [],
        "bank_count_as_source_origin": [],
        "event_cell_identity_as_source_origin": [],
        "event_cell_rotor_as_source_origin": [],
        "event_cell_carry_as_source_origin": [],
        "event_cell_predecessor_as_source_origin": [],
        "event_cell_binder_as_source_origin": [],
        "event_cell_valid_as_source_origin": [],
        "decode_bank_index_as_source_origin": [],
        "decode_slot_index_as_source_origin": [],
        "direction_live_component_as_source_origin": [],
        "source_pointer_before_as_source_origin": [],
        "source_pointer_after_as_source_origin": [],
        "selected_station_site_as_origin_matter_site": [],
    }
    for row in epochs:
        selected = row["selected_alternatives"]
        program_rows = row["selected_program_rows"]
        station_sites = row["selected_station_sites"]
        probes["fixture_matter_mode_as_source_origin"].append(
            row["after_matter_mode"]
        )
        probes["selected_alternative_as_source_origin"].append(
            int(selected[0]) if len(selected) == 1 else None
        )
        probes["selected_program_row_index_as_source_origin"].append(
            int(program_rows[0][1]) if len(program_rows) == 1 else None
        )
        probes["epoch_ordinal_as_source_origin"].append(
            int(row["epoch_ordinal"])
        )
        probes["bank_count_as_source_origin"].append(int(row["banks"]))
        probes["event_cell_identity_as_source_origin"].append(
            int(row["event_cell"]["identity"])
        )
        probes["event_cell_rotor_as_source_origin"].append(
            int(row["event_cell"]["rotor"])
        )
        probes["event_cell_carry_as_source_origin"].append(
            int(row["event_cell"]["carry"])
        )
        predecessor = row["event_cell"]["predecessor"]
        probes["event_cell_predecessor_as_source_origin"].append(
            int(predecessor) if predecessor is not None else None
        )
        probes["event_cell_binder_as_source_origin"].append(
            int(row["event_cell"]["binder"])
        )
        probes["event_cell_valid_as_source_origin"].append(
            int(row["event_cell"]["valid"])
        )
        probes["decode_bank_index_as_source_origin"].append(
            int(row["decode_order_tail"][0])
        )
        probes["decode_slot_index_as_source_origin"].append(
            int(row["decode_order_tail"][1])
        )
        probes["direction_live_component_as_source_origin"].append(
            row["direction"].index(1)
        )
        probes["source_pointer_before_as_source_origin"].append(
            int(row["source_pointer_before"])
        )
        probes["source_pointer_after_as_source_origin"].append(
            int(row["source_pointer_after"])
        )
        probes["selected_station_site_as_origin_matter_site"].append(
            origin_by_site.get(tuple(station_sites[0]))
            if len(station_sites) == 1
            else None
        )
    rows = {}
    for name, values in probes.items():
        compatible = sum(
            value is not None and value in epoch["origin_candidates"]
            for value, epoch in zip(values, epochs)
        )
        rows[name] = {
            "values_present": sum(value is not None for value in values),
            "orientation_compatible_rows": compatible,
            "total_rows": len(epochs),
            "total_specific_origin_join": compatible == len(epochs),
            "distinct_values": sorted(
                {int(value) for value in values if value is not None}
            ),
        }
    return rows


def refinement_interface_census(
    epochs: list[dict[str, object]],
    catalog: list[dict[str, object]],
    ast_census: list[dict[str, object]],
) -> tuple[dict[str, object], list[int] | None, str | None]:
    """Intersect every landed typed join and attempt a specific-origin map."""
    matter_sites = {
        tuple(row["origin_matter_site"]) for row in catalog
    }
    selected_sites = {
        tuple(site)
        for epoch in epochs
        for site in epoch["selected_station_sites"]
    }
    target_join_sizes = []
    pointer_join_sizes = []
    combined_join_sizes = []
    target_join_matches_orientation = True
    for epoch in epochs:
        orientation_candidates = set(map(int, epoch["origin_candidates"]))
        target_candidates = {
            int(row["origin"])
            for row in catalog
            if row["record_target"] == epoch["after_matter_mode"]
        }
        pointer_candidates = {
            int(row["origin"])
            for row in catalog
            if row["record_source_pointer"] == epoch["source_pointer_before"]
            and row["postwrite_source_pointer"] == epoch["source_pointer_after"]
        }
        target_join_sizes.append(len(target_candidates))
        pointer_join_sizes.append(len(pointer_candidates))
        combined_join_sizes.append(
            len(orientation_candidates & target_candidates & pointer_candidates)
        )
        target_join_matches_orientation &= (
            target_candidates == orientation_candidates
        )

    direct_probes = direct_origin_probe_census(epochs, catalog)
    selected_alternative_orientations: dict[int, set[int]] = {}
    record_branch_matches = 0
    for epoch in epochs:
        for selected in epoch["selected_alternatives"]:
            selected_alternative_orientations.setdefault(
                int(selected), set()
            ).add(int(epoch["event_cell"]["orientation"]))
        expected_record_branch = next(
            int(row["record_branch_index"])
            for row in catalog
            if row["record_orientation"]
            == epoch["event_cell"]["orientation"]
        )
        record_branch_matches += (
            epoch["selected_alternatives"] == [expected_record_branch]
        )
    matter_route = direct_probes["fixture_matter_mode_as_source_origin"]
    site_route = direct_probes[
        "selected_station_site_as_origin_matter_site"
    ]
    exact_origins = None
    join_kind = None
    if matter_route["total_specific_origin_join"]:
        exact_origins = [
            int(epoch["after_matter_mode"]) for epoch in epochs
        ]
        join_kind = "fixture_matter_mode_is_source_origin"
    elif site_route["total_specific_origin_join"]:
        origin_by_site = {
            tuple(row["origin_matter_site"]): int(row["origin"])
            for row in catalog
        }
        exact_origins = [
            origin_by_site[tuple(epoch["selected_station_sites"][0])]
            for epoch in epochs
        ]
        join_kind = "selected_station_site_is_origin_matter_site"

    selector_ast = next(
        row for row in ast_census if row["path"] == AUDIT_INPUT_PATHS[0]
    )
    selector_origin_identifiers = [
        name
        for name in selector_ast["join_relevant_identifiers"]
        if "origin" in name.lower()
    ]
    interface = {
        "sources_exhaustively_ast_parsed": len(ast_census),
        "selector_origin_identifiers": selector_origin_identifiers,
        "selector_function": {
            "name": "enforcement_lineage_selector",
            "inputs": [
                "program",
                "before",
                "expected",
                "bank_count",
                "alternatives",
            ],
            "output_type": "tuple of controller program-station indices",
            "observed_values": sorted(
                {
                    tuple(epoch["selected_alternatives"])
                    for epoch in epochs
                }
            ),
            "orientations_by_bare_selected_index": {
                str(index): sorted(orientations)
                for index, orientations in selected_alternative_orientations.items()
            },
            "interpretation": (
                "The bare selected station index is 0 under both orientations. "
                "Orientation is determined only after retaining the epoch's "
                "fixture state and reading its landed EventCell/target mode."
            ),
        },
        "site_coordinates": {
            "selected_station_sites": [
                list(site) for site in sorted(selected_sites)
            ],
            "origin_matter_sites": [
                list(site) for site in sorted(matter_sites)
            ],
            "intersection": [
                list(site) for site in sorted(selected_sites & matter_sites)
            ],
            "result": (
                "NO JOIN: selected controller stations are disjoint from "
                "all twelve origin matter sites"
            ),
        },
        "pointer_values": {
            "selector_before": sorted(
                {epoch["source_pointer_before"] for epoch in epochs}
            ),
            "selector_after": sorted(
                {epoch["source_pointer_after"] for epoch in epochs}
            ),
            "formation_record_before": sorted(
                {row["record_source_pointer"] for row in catalog}
            ),
            "formation_record_after": sorted(
                {row["postwrite_source_pointer"] for row in catalog}
            ),
            "candidate_sizes_before_orientation": sorted(set(pointer_join_sizes)),
            "result": (
                "JOIN EXISTS BUT NOT FINER: 1->0 is common to all twelve "
                "record-shaped origin branches"
            ),
        },
        "matter_word_support": {
            "selector_fixture_modes": sorted(
                {epoch["after_matter_mode"] for epoch in epochs}
            ),
            "formation_record_targets": sorted(
                {row["record_target"] for row in catalog}
            ),
            "candidate_sizes": sorted(set(target_join_sizes)),
            "same_partition_as_orientation": target_join_matches_orientation,
            "result": (
                "JOIN EXISTS BUT NOT FINER: target mode 6 is shared by "
                "origins 0-5 and target mode 1 by origins 6-11"
            ),
        },
        "orientation": {
            "candidate_sizes": sorted(
                {len(epoch["origin_candidates"]) for epoch in epochs}
            ),
            "combined_typed_join_candidate_sizes": sorted(
                set(combined_join_sizes)
            ),
            "result": "JOIN EXISTS: exactly the two six-origin groups",
        },
        "station_and_event_indices": {
            "direct_equality_probes": direct_probes,
            "selected_station_index_equals_record_branch_index_rows": (
                record_branch_matches
            ),
            "selected_station_index_equals_record_branch_index_total": (
                record_branch_matches == len(epochs)
            ),
            "result": (
                "NO TOTAL JOIN: every numeric EventCell field, station/program "
                "index, fixture/event ordinal, direction component, pointer, "
                "and decoded bank/slot was tested by direct equality; no landed "
                "interface binds any of them to a one-hot source origin"
            ),
        },
        "R693": {
            "record_identities": len(R693.CONTENT),
            "contents": list(R693.CONTENT),
            "distinct_contents": len(set(R693.CONTENT)),
            "authority": R693.AUTHORITY,
            "result": (
                "NO ORIGIN JOIN: three record identities and two contents "
                "expose no selector epoch or twelve-origin key"
            ),
        },
        "specific_origin_join_kind": join_kind,
        "specific_origin_join_found": exact_origins is not None,
        "supplied_origin_refinement_convention": None,
    }
    return interface, exact_origins, join_kind


def weak_composition_audit(total: int, bins: int) -> dict[str, object]:
    """Enumerate all nonnegative allocations; do not assume a split rule."""
    possible_values = [set() for _index in range(bins)]
    vector_count = 0

    def visit(remaining: int, positions: int, prefix: tuple[int, ...]) -> None:
        nonlocal vector_count
        if positions == 1:
            vector = prefix + (remaining,)
            vector_count += 1
            for index, value in enumerate(vector):
                possible_values[index].add(value)
            return
        for value in range(remaining + 1):
            visit(remaining - value, positions - 1, prefix + (value,))

    visit(total, bins, ())
    return {
        "total_group_epochs": total,
        "origins_in_group": bins,
        "weak_compositions_enumerated": vector_count,
        "weak_compositions_closed_form": comb(total + bins - 1, bins - 1),
        "possible_values_by_origin": [
            sorted(values) for values in possible_values
        ],
        "per_origin_range": [
            min(values) for values in possible_values
        ][:1]
        + [max(possible_values[0])],
    }


def main() -> int:
    started = monotonic()
    sources = input_sources()
    observed_sha = {
        path: sha256(source).hexdigest()
        for path, source in sources.items()
    }
    ast_census = [
        ast_interface_census(path, sources[path])
        for path in AUDIT_INPUT_PATHS
    ]
    blocklist = blocklist_census()
    catalog, catalog_evidence = derive_origin_catalog()
    epochs = selector_epoch_rows(catalog)
    epochs_repeat = selector_epoch_rows(catalog)

    interface, exact_origins, join_kind = refinement_interface_census(
        epochs, catalog, ast_census
    )
    orientation_counts = Counter(
        int(epoch["event_cell"]["orientation"]) for epoch in epochs
    )
    formation_orientation_by_target = {
        int(row["record_target"]): int(row["record_orientation"])
        for row in catalog
    }
    independently_read_orientations = [
        formation_orientation_by_target[int(epoch["after_matter_mode"])]
        for epoch in epochs
    ]
    direction_orientations = [
        1 if epoch["direction"] == [1, 0] else -1
        for epoch in epochs
    ]
    unmapped_epochs = [
        epoch["fixture"]
        for epoch in epochs
        if len(epoch["origin_candidates"]) != 6
    ]
    recount_evidence = {
        "epochs": len(epochs),
        "fixture_counts_by_banks": {
            str(size): sum(epoch["banks"] == size for epoch in epochs)
            for size in (2, 5, 12)
        },
        "alternatives_exhausted": sum(
            int(epoch["alternative_count"]) for epoch in epochs
        ),
        "selected_alternatives": sorted(
            {tuple(epoch["selected_alternatives"]) for epoch in epochs}
        ),
        "event_cell_orientation_counts": {
            "+1": orientation_counts[1],
            "-1": orientation_counts[-1],
        },
        "matter_target_orientation_counts": {
            "+1": independently_read_orientations.count(1),
            "-1": independently_read_orientations.count(-1),
        },
        "direction_orientation_counts": {
            "+1": direction_orientations.count(1),
            "-1": direction_orientations.count(-1),
        },
        "three_readings_agree": all(
            int(epoch["event_cell"]["orientation"])
            == matter_orientation
            == direction_orientation
            for epoch, matter_orientation, direction_orientation in zip(
                epochs,
                independently_read_orientations,
                direction_orientations,
            )
        ),
        "unmapped_epochs": unmapped_epochs,
    }

    range_audit = weak_composition_audit(19, 6)
    expected_values = list(range(20))
    per_origin_table = [
        {
            "origin": int(row["origin"]),
            "orientation": int(row["record_orientation"]),
            "exact_epoch_count": (
                Counter(exact_origins)[int(row["origin"])]
                if exact_origins is not None
                else None
            ),
            "compatible_epoch_count": orientation_counts[
                int(row["record_orientation"])
            ],
            "orientation_only_refinement_range": [0, 19],
        }
        for row in catalog
    ]

    outcome_convention = (
        "DECLARED IDENTITY CONTROL ONLY: epoch_ordinal modulo "
        "len(R693.CONTENT); not an origin correspondence"
    )
    outcome_ids = [
        int(epoch["epoch_ordinal"]) % len(R693.CONTENT)
        for epoch in epochs
    ]
    outcome_counts = Counter(outcome_ids)
    origin_zero = catalog[0]
    identity_evidence = {
        "outcome_mapping_convention": outcome_convention,
        "outcome_census": [
            outcome_counts[index] for index in range(len(R693.CONTENT))
        ],
        "R693_record_identities": len(R693.CONTENT),
        "origin0_Cycle769_lineage_check": {
            "record_branch_index": origin_zero["record_branch_index"],
            "record_target": origin_zero["record_target"],
            "record_orientation": origin_zero["record_orientation"],
            "write_pipeline": origin_zero["write_pipeline"],
            "postwrite_source_pointer": origin_zero[
                "postwrite_source_pointer"
            ],
            "written_event_cells": origin_zero["written_event_cells"],
        },
    }

    if exact_origins is None:
        primary_status = "CONFIRMED_ORIENTATION_ONLY"
        refinement_finding = (
            "CONFIRMED_ORIENTATION_ONLY: no landed selector epoch or "
            "selected-alternative interface determines a specific one-hot "
            "matter origin; orientation and shared target modes 6/1 each "
            "leave six candidates."
        )
    else:
        primary_status = "REFUTED_CEILING"
        refinement_finding = (
            "REFUTED_CEILING: landed join "
            + str(join_kind)
            + " determines a specific origin for every epoch; the 12-bin "
            "table is printed."
        )

    refinement_pass = all(
        (
            len(ast_census) == len(AUDIT_INPUT_PATHS) == 4,
            interface["sources_exhaustively_ast_parsed"] == 4,
            interface["orientation"]["combined_typed_join_candidate_sizes"]
            == [6]
            if exact_origins is None
            else len(exact_origins) == len(epochs),
            (
                not interface["selector_origin_identifiers"]
                and interface["selector_function"][
                    "orientations_by_bare_selected_index"
                ] == {"0": [-1, 1]}
                and interface["station_and_event_indices"][
                    "selected_station_index_equals_record_branch_index_rows"
                ] == 19
                and not any(
                    row["total_specific_origin_join"]
                    for row in interface["station_and_event_indices"][
                        "direct_equality_probes"
                    ].values()
                )
            )
            if exact_origins is None
            else True,
            interface["supplied_origin_refinement_convention"] is None,
        )
    )
    recount_pass = all(
        (
            recount_evidence["epochs"] == 38,
            recount_evidence["fixture_counts_by_banks"]
            == {"2": 4, "5": 10, "12": 24},
            recount_evidence["alternatives_exhausted"] == 2578,
            recount_evidence["selected_alternatives"] == [(0,)],
            recount_evidence["event_cell_orientation_counts"]
            == {"+1": 19, "-1": 19},
            recount_evidence["matter_target_orientation_counts"]
            == {"+1": 19, "-1": 19},
            recount_evidence["direction_orientation_counts"]
            == {"+1": 19, "-1": 19},
            recount_evidence["three_readings_agree"],
            not unmapped_epochs,
        )
    )
    range_pass = all(
        (
            exact_origins is None,
            range_audit["weak_compositions_enumerated"] == 42_504,
            range_audit["weak_compositions_enumerated"]
            == range_audit["weak_compositions_closed_form"],
            all(
                values == expected_values
                for values in range_audit["possible_values_by_origin"]
            ),
            range_audit["per_origin_range"] == [0, 19],
            all(
                row["exact_epoch_count"] is None
                and row["compatible_epoch_count"] == 19
                and row["orientation_only_refinement_range"] == [0, 19]
                for row in per_origin_table
            ),
        )
    )
    identity_pass = all(
        (
            identity_evidence["outcome_census"] == [13, 13, 12],
            identity_evidence["R693_record_identities"] == 3,
            origin_zero["record_branch_index"] == 0,
            origin_zero["record_target"] == 6,
            origin_zero["record_orientation"] == 1,
            origin_zero["write_pipeline"] == [0, 1, 125],
            origin_zero["postwrite_source_pointer"] == 0,
            origin_zero["written_event_cells"] == 1,
        )
    )

    deterministic_evidence = {
        "epochs_equal_on_repeat": epochs_repeat == epochs,
        "epoch_rows_sha256": digest(epochs),
        "repeat_epoch_rows_sha256": digest(epochs_repeat),
        "catalog_rows_sha256": digest(catalog),
        "interface_sha256": digest(interface),
    }
    elapsed = monotonic() - started
    base_controls_pass = all(
        (
            literal_audit_tuple(),
            DECLARED_INPUT_PATHS is AUDIT_INPUT_PATHS,
            observed_sha == EXPECTED_SHA256,
            S750_SOURCE_LOCATOR in ("worktree", "landed_git_blob"),
            C719.K is K719,
            S750.K is K719,
            catalog_evidence["transition_certificate"]
            == {
                "source_modes": 12,
                "transition_entries": 72,
                "failures": 0,
                "endpoint_aux_cleanup_failures": 0,
            },
            catalog_evidence["origins"] == 12,
            catalog_evidence["support_branches"] == 72,
            catalog_evidence["record_branches"] == 12,
            catalog_evidence["distinct_support_signatures_by_orientation"]
            == {"-1": 1, "1": 1},
            blocklist["required_cycle786_primary_present"],
            not blocklist["parse_failures"],
            not blocklist["loaded_blocklisted_modules"],
            not blocklist["audit_input_overlap"],
            deterministic_evidence["epochs_equal_on_repeat"],
            elapsed < AUDIT_TIMEOUT_SEC,
            BOUNDARY_VERBATIM
            == (
                "counts only; no weights, no rate law, no probability; any "
                "needed convention must be declared, never silently used."
            ),
        )
    )

    lines = []
    lines.append("BOUNDARY_VERBATIM " + BOUNDARY_VERBATIM)
    lines.append("SHA_ANCHORS " + compact(observed_sha))
    lines.append(
        "SELECTOR_SOURCE "
        + compact(
            {
                "locator": S750_SOURCE_LOCATOR,
                "landed_git_blob": SELECTOR_LANDED_GIT_BLOB,
            }
        )
    )
    lines.append("BLOCKLIST_CENSUS " + compact(blocklist))
    for row in ast_census:
        lines.append("INTERFACE_AST_CENSUS " + compact(row))
    lines.append("FORMATION_CATALOG_EVIDENCE " + compact(catalog_evidence))
    for row in catalog:
        lines.append("FORMATION_ORIGIN " + compact(row))
    for row in epochs:
        lines.append("SELECTOR_EPOCH_INTERFACE " + compact(row))
    lines.append("REFINEMENT_INTERFACE_CENSUS " + compact(interface))
    for row in per_origin_table:
        lines.append("PER_ORIGIN_SUPPORT " + compact(row))
    lines.append("RECOUNT_EVIDENCE " + compact(recount_evidence))
    lines.append("REFINEMENT_RANGE_EVIDENCE " + compact(range_audit))
    lines.append("IDENTITY_EVIDENCE " + compact(identity_evidence))
    lines.append("DETERMINISM_EVIDENCE " + compact(deterministic_evidence))
    lines.append(
        ("CERTIFICATE_REFINEMENT_HUNT_PASS" if refinement_pass
         else "CERTIFICATE_REFINEMENT_HUNT_FAIL")
        + " :: "
        + refinement_finding
        + " "
        + compact(
            {
                "specific_origin_join_found": exact_origins is not None,
                "specific_origin_join_kind": join_kind,
                "per_origin_table_printed": True,
            }
        )
    )
    lines.append(
        ("CERTIFICATE_19_19_RECOUNT_PASS" if recount_pass
         else "CERTIFICATE_19_19_RECOUNT_FAIL")
        + " :: "
        + compact(recount_evidence)
    )
    lines.append(
        ("CERTIFICATE_REFINEMENT_RANGE_AUDIT_PASS" if range_pass
         else "CERTIFICATE_REFINEMENT_RANGE_AUDIT_FAIL")
        + " :: "
        + compact(range_audit)
    )
    lines.append(
        ("CERTIFICATE_IDENTITY_CONTROLS_PASS" if identity_pass
         else "CERTIFICATE_IDENTITY_CONTROLS_FAIL")
        + " :: "
        + compact(identity_evidence)
    )

    def render(actual_stdout_bytes: int) -> tuple[str, bool]:
        controls_pass = (
            base_controls_pass
            and actual_stdout_bytes < AUDIT_STDOUT_MAX_BYTES
        )
        control_evidence = {
            "literal_AUDIT_INPUT_PATHS": literal_audit_tuple(),
            "sha_anchors": observed_sha == EXPECTED_SHA256,
            "selector_source_locator": S750_SOURCE_LOCATOR,
            "controller_core_object_identity": C719.K is K719,
            "selector_core_object_identity": S750.K is K719,
            "blocklist_text_ast_only": (
                blocklist["required_cycle786_primary_present"]
                and not blocklist["parse_failures"]
                and not blocklist["loaded_blocklisted_modules"]
                and not blocklist["audit_input_overlap"]
            ),
            "cycle785_copies_checked": len(
                blocklist["cycle785_copies_present"]
            ),
            "deterministic": deterministic_evidence[
                "epochs_equal_on_repeat"
            ],
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "actual_stdout_bytes": actual_stdout_bytes,
            "stdout_limit_bytes": AUDIT_STDOUT_MAX_BYTES,
        }
        all_pass = all(
            (
                refinement_pass,
                recount_pass,
                range_pass,
                identity_pass,
                controls_pass,
            )
        )
        report = {
            "cycle": 786,
            "checker": "independent_adversarial",
            "pass": all_pass,
            "primary_status": primary_status,
            "refinement_hunt_finding": refinement_finding,
            "certificates": {
                "refinement_hunt": refinement_pass,
                "recount_19_19": recount_pass,
                "refinement_range": range_pass,
                "identity_controls": identity_pass,
                "controls": controls_pass,
            },
            "specific_origin_counts": (
                [
                    Counter(exact_origins)[origin]
                    for origin in range(12)
                ]
                if exact_origins is not None
                else None
            ),
            "orientation_counts": {"+1": 19, "-1": 19},
            "outcome_census": identity_evidence["outcome_census"],
            "runtime_seconds": round(elapsed, 6),
            "no_weights": True,
            "no_rate_law": True,
            "no_probability": True,
            "supplied_origin_refinement_convention": None,
        }
        report["report_sha256"] = digest(report)
        rendered_lines = lines + [
            (
                "CERTIFICATE_CONTROLS_PASS"
                if controls_pass
                else "CERTIFICATE_CONTROLS_FAIL"
            )
            + " :: "
            + compact(control_evidence),
            "SUMMARY_JSON " + compact(report),
            (
                "CYCLE786_SUPPORT_INDEPENDENT_CHECK_PASS"
                if all_pass
                else "CYCLE786_SUPPORT_INDEPENDENT_CHECK_INCOMPLETE"
            ),
        ]
        return "\n".join(rendered_lines) + "\n", controls_pass

    actual_stdout_bytes = 0
    output = ""
    controls_pass = False
    for _iteration in range(10):
        output, controls_pass = render(actual_stdout_bytes)
        new_size = len(output.encode("utf-8"))
        if new_size == actual_stdout_bytes:
            break
        actual_stdout_bytes = new_size
    output, controls_pass = render(actual_stdout_bytes)
    if len(output.encode("utf-8")) != actual_stdout_bytes:
        actual_stdout_bytes = len(output.encode("utf-8"))
        output, controls_pass = render(actual_stdout_bytes)

    sys.stdout.write(output)
    return 0 if all(
        (
            refinement_pass,
            recount_pass,
            range_pass,
            identity_pass,
            controls_pass,
            len(output.encode("utf-8")) < AUDIT_STDOUT_MAX_BYTES,
        )
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
