#!/usr/bin/env python3
"""Cycle 793 independent adversarial check: attack per-bank balance.

The Cycle 793/788/786 primaries are text-only, runtime-blocklisted references.
All event states and selector trials below are reconstructed from the landed
Cycle 750/719 machinery.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_STDOUT_MAX_BYTES = 150 * 1024
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
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
ALL_BANKS = (1, 2, 3, 5, 12)
LANDED_BANKS = (2, 5, 12)
EXTENSION_BANKS = (1, 3)

PRIMARY_TEXT_PATHS = {
    "cycle793": (
        "scripts/frontier_cycle793_enlarged_orientation_census_2026_07_28.py"
    ),
    "cycle788": (
        "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py"
    ),
}
C788_CHECKER_TEXT_PATH = (
    "scripts/frontier_cycle788_extension_independent_check_2026_07_28.py"
)
C719_PACKET_CORE_TEXT_PATH = (
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py"
)
C786_REFERENCE_REF = "origin/physics-loop/proof-grade-blockR7-20260729"
C786_REFERENCE_COMMIT = "6a4d3a49f68808236403fe6310097459c2f7c07a"
C786_REFERENCE_PATH = (
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py"
)

BLOCKLISTED_MODULES = (
    "frontier_cycle793_enlarged_orientation_census_2026_07_28",
    "frontier_cycle788_selector_scope_extension_2026_07_28",
    "frontier_cycle786_ensemble_support_census_2026_07_28",
)

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
EXPECTED_TEXT_SHA256 = {
    "cycle793":
        "aff8222437aac85443df6770cd11bef136b7698f6be0d4a65caa7771f1bf31c5",
    "cycle788":
        "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    "cycle788_checker":
        "345ae7c423c529b080ce87647909472453f64119282aa41b8aa4ffbecbf4286e",
    "cycle786":
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    "cycle719_packet_core":
        "b8afe7e4697b0838715a079203930fb37bc7a6fc133e092f02a22141049aad8c",
}


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Reject any attempt to import a blocklisted primary."""

    def find_spec(self, fullname, path=None, target=None):
        if fullname in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import protected_recurrent_actual_history_selection_cycle335_2026_07_18 as H335
import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as O332
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(f"missing function {name}")


def source_tree(path: str) -> tuple[str, ast.Module]:
    source = (ROOT / path).read_text(encoding="utf-8")
    return source, ast.parse(source)


def source_anchors() -> dict[str, str]:
    return {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }


def text_references() -> tuple[dict[str, object], dict[str, ast.Module]]:
    sources = {}
    trees = {}
    for label, path in PRIMARY_TEXT_PATHS.items():
        source, tree = source_tree(path)
        sources[label] = source.encode("utf-8")
        trees[label] = tree
    checker_source, checker_tree = source_tree(C788_CHECKER_TEXT_PATH)
    sources["cycle788_checker"] = checker_source.encode("utf-8")
    trees["cycle788_checker"] = checker_tree
    packet_source, packet_tree = source_tree(C719_PACKET_CORE_TEXT_PATH)
    sources["cycle719_packet_core"] = packet_source.encode("utf-8")
    trees["cycle719_packet_core"] = packet_tree

    resolved = subprocess.run(
        ("git", "rev-parse", C786_REFERENCE_REF),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    c786_bytes = subprocess.run(
        ("git", "show", f"{C786_REFERENCE_COMMIT}:{C786_REFERENCE_PATH}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    sources["cycle786"] = c786_bytes
    trees["cycle786"] = ast.parse(c786_bytes.decode("utf-8"))
    anchors = {
        label: sha256(source).hexdigest()
        for label, source in sources.items()
    }
    return {
        "sha256": anchors,
        "expected_sha256": EXPECTED_TEXT_SHA256,
        "cycle786_reference_ref": C786_REFERENCE_REF,
        "cycle786_resolved_commit": resolved,
        "cycle786_pinned_commit": C786_REFERENCE_COMMIT,
        "cycle786_reference_path": C786_REFERENCE_PATH,
        "handling": "text_AST_only_never_imported",
    }, trees


def own_source_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    assignments: dict[str, ast.AST] = {}
    direct_landed_imports = []
    all_imports = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            for alias in node.names:
                all_imports.append(alias.name)
                if alias.name.startswith(
                    ("frontier_", "protected_", "physical_")
                ):
                    direct_landed_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            all_imports.append(node.module or "")
    audit = assignments.get("AUDIT_INPUT_PATHS")
    declared = assignments.get("DECLARED_INPUT_PATHS")
    expected_modules = [
        Path(path).stem for path in AUDIT_INPUT_PATHS
    ]
    return {
        "literal_AUDIT_INPUT_PATHS": (
            isinstance(audit, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in audit.elts
            )
            and tuple(ast.literal_eval(audit)) == AUDIT_INPUT_PATHS
        ),
        "DECLARED_INPUT_PATHS_alias": (
            isinstance(declared, ast.Name)
            and declared.id == "AUDIT_INPUT_PATHS"
        ),
        "all_audit_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "direct_landed_imports": direct_landed_imports,
        "direct_landed_imports_exact": (
            direct_landed_imports == expected_modules
        ),
        "blocklisted_primary_AST_imports": sorted(
            set(all_imports).intersection(BLOCKLISTED_MODULES)
        ),
    }


def exercise_runtime_blocklist() -> dict[str, object]:
    attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            __import__(module)
        except ImportError as exc:
            attempts[module] = {
                "blocked": str(exc) == f"BLOCKLIST forbids import of {module}",
                "message": str(exc),
            }
        else:
            attempts[module] = {
                "blocked": False,
                "message": "IMPORT_UNEXPECTEDLY_SUCCEEDED",
            }
    return {
        "finder_installed": PRIMARY_BLOCKER in sys.meta_path,
        "attempts": attempts,
        "none_loaded": all(
            module not in sys.modules for module in BLOCKLISTED_MODULES
        ),
    }


def orientation_counts(rows: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(int(row["orientation"]) for row in rows)
    return {
        "+1": counts[1],
        "-1": counts[-1],
        "other": sum(
            count
            for orientation, count in counts.items()
            if orientation not in (-1, 1)
        ),
        "total": len(rows),
    }


def per_bank_counts(
    rows: list[dict[str, object]],
) -> dict[int, dict[str, int]]:
    return {
        bank: orientation_counts(
            [row for row in rows if int(row["bank"]) == bank]
        )
        for bank in sorted({int(row["bank"]) for row in rows})
    }


def own_event_rows(bank_counts: tuple[int, ...]) -> list[dict[str, object]]:
    """Rebuild the epochs without calling Cycle 750's fixture helper."""
    rows = []
    for bank_count in bank_counts:
        program = K719.interleaved_program(bank_count)
        banks, links = K719.B.chain_genesis(bank_count)
        state = K719.M.pack_state(banks, links)
        allocator = K719.M.global_allocator_word(bank_count)
        for event in range(2 * bank_count):
            mode = (1, 0) if event % 2 == 0 else (0, 1)
            before = K719.M.prepare_endpoint(state, mode)
            expected = K719.A.apply_semantic(before, allocator)
            alternatives = tuple(range(len(program)))
            selected = S750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            after_banks, after_links = K719.M.unpack_state(
                expected, bank_count
            )
            chain, decode_order = K719.B.decode_local_graph(
                after_banks, after_links
            )
            cell = chain.cells[event]
            rows.append(
                {
                    "bank": bank_count,
                    "epoch": event,
                    "mode": list(mode),
                    "orientation": int(cell.orientation),
                    "cell_identity": int(cell.identity),
                    "cell_count": len(chain.cells),
                    "decode_node": list(decode_order[event]),
                    "selected": list(selected),
                    "program_stations": len(program),
                }
            )
            state = expected
    return rows


def derived_target_mode_rule(
    rows: list[dict[str, object]],
) -> dict[str, object]:
    observations: dict[str, set[int]] = {}
    for row in rows:
        key = compact(row["mode"])
        observations.setdefault(key, set()).add(int(row["orientation"]))
    rendered = {
        key: sorted(values) for key, values in sorted(observations.items())
    }
    rule = {
        key: values[0]
        for key, values in rendered.items()
        if len(values) == 1
    }
    return {
        "observation_sets": rendered,
        "single_valued": all(len(values) == 1 for values in rendered.values()),
        "rule": rule,
    }


def normalized_function(tree: ast.Module, name: str) -> str:
    return " ".join(ast.unparse(function_node(tree, name)).split())


def structural_mechanism(
    rows: list[dict[str, object]],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    _, selector_tree = source_tree(AUDIT_INPUT_PATHS[0])
    _, controller_tree = source_tree(AUDIT_INPUT_PATHS[3])
    fixture_text = normalized_function(selector_tree, "k_epoch_fixtures")
    held_text = normalized_function(controller_tree, "held_certificate")
    packet_fill_text = normalized_function(
        trees["cycle719_packet_core"], "fill_certificate"
    )
    decode_text = normalized_function(
        trees["cycle719_packet_core"], "decode_local_graph"
    )
    source_checks = {
        "fixture_has_exactly_2N_epochs":
            "for event in range(2 * bank_count):" in fixture_text,
        "fixture_alternates_target_mode_by_parity": (
            "direction = (1, 0) if event % 2 == 0 else (0, 1)"
            in fixture_text
        ),
        "fixture_appends_epoch_and_advances_state": (
            "rows.append((event, direction, program, before, expected))"
            in fixture_text
            and "state = expected" in fixture_text
        ),
        "controller_repeats_same_parity_pairing": (
            "for event in range(2 * bank_count):" in held_text
            and "direction = (1, 0) if event % 2 == 0 else (0, 1)"
            in held_text
        ),
        "controller_mode_to_orientation_rule": (
            "orientation=1 if direction == (1, 0) else -1"
            in held_text
        ),
        "packet_core_repeats_mode_to_orientation_rule": (
            "orientation = 1 if direction == (1, 0) else -1"
            in packet_fill_text
        ),
        "decoder_reads_packet_orientation": (
            "orientation=packet['orientation']" in decode_text.replace(" ", "")
        ),
        "decoder_numbers_graph_order_1to1": (
            "for identity, node in enumerate(order):" in decode_text
            and "identity=identity" in decode_text.replace(" ", "")
        ),
    }

    pairs_by_bank: dict[int, list[dict[str, object]]] = {}
    for bank in ALL_BANKS:
        bank_rows = sorted(
            (
                row for row in rows if int(row["bank"]) == bank
            ),
            key=lambda row: int(row["epoch"]),
        )
        pairs = []
        for pair_index in range(bank):
            left = bank_rows[2 * pair_index]
            right = bank_rows[2 * pair_index + 1]
            pairs.append(
                {
                    "pair": pair_index,
                    "epochs": [int(left["epoch"]), int(right["epoch"])],
                    "modes": [left["mode"], right["mode"]],
                    "orientations": [
                        int(left["orientation"]),
                        int(right["orientation"]),
                    ],
                    "identities": [
                        int(left["cell_identity"]),
                        int(right["cell_identity"]),
                    ],
                    "opposite": (
                        int(left["orientation"])
                        == -int(right["orientation"])
                    ),
                }
            )
        pairs_by_bank[bank] = pairs

    pair_checks = {
        "pair_count": sum(len(pairs) for pairs in pairs_by_bank.values()),
        "per_bank_pair_counts": {
            bank: len(pairs) for bank, pairs in pairs_by_bank.items()
        },
        "epoch_bijection_exact": all(
            row["epochs"] == [2 * row["pair"], 2 * row["pair"] + 1]
            for pairs in pairs_by_bank.values()
            for row in pairs
        ),
        "orientation_conjugates_exact": all(
            bool(row["opposite"])
            for pairs in pairs_by_bank.values()
            for row in pairs
        ),
        "identity_map_exact": all(
            row["identities"] == row["epochs"]
            for pairs in pairs_by_bank.values()
            for row in pairs
        ),
    }
    mechanism_found = (
        all(source_checks.values())
        and pair_checks["pair_count"] == sum(ALL_BANKS)
        and pair_checks["per_bank_pair_counts"]
        == {bank: bank for bank in ALL_BANKS}
        and all(
            (
                pair_checks["epoch_bijection_exact"],
                pair_checks["orientation_conjugates_exact"],
                pair_checks["identity_map_exact"],
            )
        )
    )
    verdict = (
        "STRUCTURALLY_FORCED_BY_2N_PARITY_CONJUGATE_EPOCH_PAIRS"
        if mechanism_found
        else "UNEXPLAINED"
    )
    return {
        "verdict": verdict,
        "finding": (
            "Each bank-N fixture creates exactly 2N epochs; epoch 2j uses "
            "target mode (1,0), epoch 2j+1 uses (0,1), and the decoded "
            "EventCells carry opposite orientations.  The map "
            "2j -> 2j+1 is a 1:1 constructor-level pairing, so per-bank "
            "balance is forced, not an emergent coincidence."
            if mechanism_found
            else "UNEXPLAINED: no constructor-level 1:1 opposite-orientation "
            "epoch pairing was established from the permitted landed modules."
        ),
        "module_evidence": {
            "fixture": {
                "path": AUDIT_INPUT_PATHS[0],
                "function": "k_epoch_fixtures",
                "lines": [
                    function_node(selector_tree, "k_epoch_fixtures").lineno,
                    function_node(selector_tree, "k_epoch_fixtures").end_lineno,
                ],
            },
            "controller": {
                "path": AUDIT_INPUT_PATHS[3],
                "function": "held_certificate",
                "lines": [
                    function_node(controller_tree, "held_certificate").lineno,
                    function_node(controller_tree, "held_certificate").end_lineno,
                ],
            },
            "packet_decoder": {
                "path": C719_PACKET_CORE_TEXT_PATH,
                "functions": ["fill_certificate", "decode_local_graph"],
            },
            "source_checks": source_checks,
        },
        "pair_checks": pair_checks,
        "pairs_by_bank": pairs_by_bank,
    }


def rotate_left(values: tuple, amount: int) -> tuple:
    amount %= len(values)
    return values[amount:] + values[:amount]


def q_order(stations: int, mode: str) -> tuple[int, ...] | None:
    if mode == "ascending":
        return None
    if mode == "descending":
        return tuple(reversed(range(stations)))
    if mode == "even_then_odd":
        return (
            tuple(range(0, stations, 2))
            + tuple(range(1, stations, 2))
        )
    raise ValueError(mode)


def advance_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(len(a)):
        a[station], b[station] = b[station], a[station]
    for station in range(len(a)):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    return tuple(a), tuple(b)


def retreat_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in reversed(range(len(a))):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    for station in reversed(range(len(a))):
        a[station], b[station] = b[station], a[station]
    return tuple(a), tuple(b)


def apply_live_macros(
    data: tuple[int, ...],
    program: tuple,
    a_tokens: tuple[int, ...],
    *,
    reverse: bool,
    order_mode: str,
) -> tuple[int, ...]:
    order = q_order(len(program), order_mode)
    if order is None:
        order = (
            tuple(reversed(range(len(program))))
            if reverse
            else tuple(range(len(program)))
        )
    output = data
    for station in order:
        if a_tokens[station]:
            word = K719.mapped_macro(program[station])
            if reverse:
                word = tuple(reversed(word))
            output = K719.A.apply_semantic(output, word)
    return output


def run_r_then_q_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    order_mode: str,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    stations = len(program)
    a = tuple(int(index == token_position) for index in range(stations))
    b = (0,) * stations
    output = data
    for _step in range(stations):
        if reverse:
            output = apply_live_macros(
                output,
                program,
                a,
                reverse=True,
                order_mode=order_mode,
            )
            a, b = retreat_rails(a, b)
        else:
            a, b = advance_rails(a, b)
            output = apply_live_macros(
                output,
                program,
                a,
                reverse=False,
                order_mode=order_mode,
            )
    return output, a, b


def run_varied_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    layer_order: str,
    order_mode: str,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    if layer_order == "Q_then_R":
        station_order = q_order(len(program), order_mode)
        orders = (
            None
            if station_order is None
            else (station_order,) * len(program)
        )
        output, a, b, _trace = K719.run_orbit(
            data,
            program,
            token_positions=(token_position,),
            reverse=reverse,
            q_orders=orders,
        )
        return output, a, b
    if layer_order == "R_then_Q":
        return run_r_then_q_orbit(
            data,
            program,
            token_position=token_position,
            reverse=reverse,
            order_mode=order_mode,
        )
    raise ValueError(layer_order)


def postimage_clean(after: tuple[int, ...], bank_count: int) -> bool:
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
    return not any(
        (
            after[K719.R3.X.SOURCE_POINTER],
            bank_dirty,
            any(any(link) for link in links),
        )
    )


def station_trial(
    program: tuple,
    before: tuple[int, ...],
    expected: tuple[int, ...],
    bank_count: int,
    position: int,
    *,
    layer_order: str,
    order_mode: str,
) -> tuple[dict[str, bool], tuple[int, ...]]:
    tokens = tuple(
        int(index == position) for index in range(len(program))
    )
    zeros = (0,) * len(program)
    after, rail_a, rail_b = run_varied_orbit(
        before,
        program,
        token_position=position,
        reverse=False,
        layer_order=layer_order,
        order_mode=order_mode,
    )
    restored, inverse_a, inverse_b = run_varied_orbit(
        after,
        program,
        token_position=position,
        reverse=True,
        layer_order=layer_order,
        order_mode=order_mode,
    )
    return {
        "composition": after == expected,
        "rail": rail_a == tokens and rail_b == zeros,
        "inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "postimage": postimage_clean(after, bank_count),
    }, after


def selecting_variations(stations: int) -> dict[str, list[dict[str, object]]]:
    """Literal reimplementation of the three SELECT supplies in Check 788."""
    source_rows = []
    for source_index in (0, 1, stations - 1):
        source_rows.append(
            {
                "choice": f"source_station_index={source_index}",
                "program_rotation": (-source_index) % stations,
                "layer_order": "Q_then_R",
                "order_mode": "ascending",
            }
        )
    orientation_rows = []
    for rotation in (0, 1, stations - 1):
        orientation_rows.append(
            {
                "choice": f"left_rotation={rotation}",
                "program_rotation": rotation,
                "layer_order": "Q_then_R",
                "order_mode": "ascending",
            }
        )
    order_rows = []
    for layer_order, order_mode in (
        ("Q_then_R", "ascending"),
        ("Q_then_R", "descending"),
        ("Q_then_R", "even_then_odd"),
        ("R_then_Q", "ascending"),
    ):
        order_rows.append(
            {
                "choice": (
                    f"layers={layer_order};Q_order={order_mode}"
                ),
                "program_rotation": 0,
                "layer_order": layer_order,
                "order_mode": order_mode,
            }
        )
    return {
        "inherited_1": source_rows,
        "inherited_2": orientation_rows,
        "inherited_3": order_rows,
    }


def varied_orientation_signature(
    bank_count: int,
    settings: dict[str, object],
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    program = rotate_left(
        base_program, int(settings["program_rotation"])
    )
    banks, links = K719.B.chain_genesis(bank_count)
    state = K719.M.pack_state(banks, links)
    allocator = K719.M.global_allocator_word(bank_count)
    selected_signature = []
    orientation_signature = []
    identity_signature = []
    event_failures = []
    for event in range(2 * bank_count):
        mode = (1, 0) if event % 2 == 0 else (0, 1)
        before = K719.M.prepare_endpoint(state, mode)
        expected = K719.A.apply_semantic(before, allocator)
        survivors = []
        for position in range(len(program)):
            criteria, after = station_trial(
                program,
                before,
                expected,
                bank_count,
                position,
                layer_order=str(settings["layer_order"]),
                order_mode=str(settings["order_mode"]),
            )
            if all(criteria.values()):
                survivors.append((position, after))
        selected_signature.append(
            [position for position, _after in survivors]
        )
        event_orientations = []
        event_identities = []
        for _position, after in survivors:
            after_banks, after_links = K719.M.unpack_state(
                after, bank_count
            )
            chain, _decode_order = K719.B.decode_local_graph(
                after_banks, after_links
            )
            event_orientations.append(int(chain.cells[event].orientation))
            event_identities.append(int(chain.cells[event].identity))
        orientation_signature.append(event_orientations)
        identity_signature.append(event_identities)
        if len(survivors) != 1:
            event_failures.append(
                {
                    "event": event,
                    "survivors": selected_signature[-1],
                }
            )
        state = expected
    return {
        "selected_signature": selected_signature,
        "orientation_signature": orientation_signature,
        "identity_signature": identity_signature,
        "event_failures": event_failures,
        "program_stations": len(program),
    }


def supply_sensitivity_probe(
    baseline_rows: list[dict[str, object]],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    checker_text = normalized_function(
        trees["cycle788_checker"], "run_supply_attack"
    )
    text_checks = {
        "source_station_choices_exact": (
            "for source_index in (0, 1, stations - 1):"
            in checker_text
            and "rotation = -source_index % stations" in checker_text
        ),
        "left_rotation_choices_exact": (
            "for rotation in (0, 1, stations - 1):" in checker_text
        ),
        "layer_and_Q_order_choices_exact": all(
            fragment in checker_text
            for fragment in (
                "('Q_then_R', 'ascending')",
                "('Q_then_R', 'descending')",
                "('Q_then_R', 'even_then_odd')",
                "('R_then_Q', 'ascending')",
            )
        ),
        "checker_classifies_by_distinct_survivor_signatures": (
            "'SELECTS' if len(signatures) > 1 else 'NEUTRAL'"
            in checker_text
        ),
    }
    baseline = {
        bank: [
            int(row["orientation"])
            for row in baseline_rows
            if int(row["bank"]) == bank
        ]
        for bank in EXTENSION_BANKS
    }
    rows = []
    flips = []
    supply_signatures: dict[int, dict[str, list[str]]] = {}
    for bank in EXTENSION_BANKS:
        stations = len(K719.interleaved_program(bank))
        supply_signatures[bank] = {}
        for supply_id, variations in selecting_variations(stations).items():
            supply_signatures[bank][supply_id] = []
            for settings in variations:
                result = varied_orientation_signature(bank, settings)
                selected_key = compact(result["selected_signature"])
                supply_signatures[bank][supply_id].append(selected_key)
                flat_orientations = [
                    values[0] for values in result["orientation_signature"]
                    if len(values) == 1
                ]
                changed = (
                    result["event_failures"]
                    or flat_orientations != baseline[bank]
                )
                row = {
                    "bank": bank,
                    "supply_id": supply_id,
                    "choice": settings["choice"],
                    "settings": {
                        key: settings[key]
                        for key in (
                            "program_rotation",
                            "layer_order",
                            "order_mode",
                        )
                    },
                    "selected_signature": result["selected_signature"],
                    "orientation_signature": result[
                        "orientation_signature"
                    ],
                    "identity_signature": result["identity_signature"],
                    "event_failures": result["event_failures"],
                    "orientation_changed": bool(changed),
                }
                rows.append(row)
                if changed:
                    flips.append(row)
    classifications = {
        bank: {
            supply_id: (
                "SELECTS"
                if len(set(signatures)) > 1
                else "NEUTRAL"
            )
            for supply_id, signatures in supplies.items()
        }
        for bank, supplies in supply_signatures.items()
    }
    exhausted = all(
        (
            len(rows) == len(EXTENSION_BANKS) * (3 + 3 + 4),
            all(text_checks.values()),
            all(
                verdict == "SELECTS"
                for supplies in classifications.values()
                for verdict in supplies.values()
            ),
            all(not row["event_failures"] for row in rows),
            all(
                identities
                == [event]
                for row in rows
                for event, identities in enumerate(
                    row["identity_signature"]
                )
            ),
        )
    )
    verdict = (
        "ORIENTATION_FLIPS_UNDER_SELECTING_SUPPLY_VARIATIONS"
        if flips
        else (
            "ORIENTATION_ROBUST_ACROSS_ALL_SELECTING_SUPPLY_VARIATIONS"
            if exhausted
            else "SUPPLY_PROBE_INCOMPLETE"
        )
    )
    finding = (
        "The new bank-1 and bank-3 EventCell orientations do not change "
        "under any inherited_1/inherited_2/inherited_3 selecting-supply "
        "variation.  Within this exhausted 788 variation set, the 4/4 "
        "new-event balance datum is supply-independent even though the "
        "surviving controller station changes."
        if verdict
        == "ORIENTATION_ROBUST_ACROSS_ALL_SELECTING_SUPPLY_VARIATIONS"
        else (
            "At least one new EventCell orientation flips under a selecting "
            "788 supply variation; the selecting-supply caveat sharpens."
            if flips
            else "The selecting-supply orientation probe was incomplete."
        )
    )
    return {
        "verdict": verdict,
        "finding": finding,
        "source_text_checks": text_checks,
        "classifications": classifications,
        "baseline_orientations": baseline,
        "variation_rows": rows,
        "variation_count": len(rows),
        "flip_count": len(flips),
        "flips": flips,
        "exhausted": exhausted,
    }


def main() -> int:
    reference, trees = text_references()
    own_audit = own_source_audit()
    blocklist = exercise_runtime_blocklist()
    input_anchors = source_anchors()

    rows = own_event_rows(ALL_BANKS)
    mode_rule = derived_target_mode_rule(rows)
    by_bank = per_bank_counts(rows)
    total = orientation_counts(rows)
    landed_rows = [
        row for row in rows if int(row["bank"]) in LANDED_BANKS
    ]
    extension_rows = [
        row for row in rows if int(row["bank"]) in EXTENSION_BANKS
    ]
    landed_counts = orientation_counts(landed_rows)
    extension_counts = orientation_counts(extension_rows)
    mechanism = structural_mechanism(rows, trees)
    supply = supply_sensitivity_probe(rows, trees)

    expected_by_bank = {
        1: {"+1": 1, "-1": 1, "other": 0, "total": 2},
        2: {"+1": 2, "-1": 2, "other": 0, "total": 4},
        3: {"+1": 3, "-1": 3, "other": 0, "total": 6},
        5: {"+1": 5, "-1": 5, "other": 0, "total": 10},
        12: {"+1": 12, "-1": 12, "other": 0, "total": 24},
    }
    expected_total = {"+1": 23, "-1": 23, "other": 0, "total": 46}
    recount_agreement = (
        by_bank == expected_by_bank and total == expected_total
    )
    certificate_a = all(
        (
            len(rows) == 46,
            Counter(int(row["bank"]) for row in rows)
            == {1: 2, 2: 4, 3: 6, 5: 10, 12: 24},
            recount_agreement,
            mode_rule["single_valued"],
            mode_rule["rule"] == {"[0,1]": -1, "[1,0]": 1},
            all(
                int(row["cell_count"]) == int(row["epoch"]) + 1
                for row in rows
            ),
            all(row["selected"] == [0] for row in rows),
        )
    )

    hunt_complete = (
        mechanism["verdict"]
        in {
            "STRUCTURALLY_FORCED_BY_2N_PARITY_CONJUGATE_EPOCH_PAIRS",
            "UNEXPLAINED",
        }
        and mechanism["pair_checks"]["pair_count"] == 23
        and set(mechanism["module_evidence"]["source_checks"])
        == {
            "fixture_has_exactly_2N_epochs",
            "fixture_alternates_target_mode_by_parity",
            "fixture_appends_epoch_and_advances_state",
            "controller_repeats_same_parity_pairing",
            "controller_mode_to_orientation_rule",
            "packet_core_repeats_mode_to_orientation_rule",
            "decoder_reads_packet_orientation",
            "decoder_numbers_graph_order_1to1",
        }
    )
    certificate_b = hunt_complete and (
        mechanism["verdict"] == "UNEXPLAINED"
        or all(mechanism["module_evidence"]["source_checks"].values())
    )

    certificate_c = (
        bool(supply["exhausted"])
        and supply["variation_count"] == 20
        and supply["verdict"]
        in {
            "ORIENTATION_ROBUST_ACROSS_ALL_SELECTING_SUPPLY_VARIATIONS",
            "ORIENTATION_FLIPS_UNDER_SELECTING_SUPPLY_VARIATIONS",
        }
    )

    landed_identity = {
        "rows": len(landed_rows),
        "identity_matches_epoch": sum(
            int(row["cell_identity"]) == int(row["epoch"])
            for row in landed_rows
        ),
        "orientation_counts": landed_counts,
        "by_bank": per_bank_counts(landed_rows),
    }
    certificate_d = all(
        (
            landed_identity["rows"] == 38,
            landed_identity["identity_matches_epoch"] == 38,
            landed_counts
            == {"+1": 19, "-1": 19, "other": 0, "total": 38},
            landed_identity["by_bank"]
            == {
                2: {"+1": 2, "-1": 2, "other": 0, "total": 4},
                5: {"+1": 5, "-1": 5, "other": 0, "total": 10},
                12: {
                    "+1": 12,
                    "-1": 12,
                    "other": 0,
                    "total": 24,
                },
            },
        )
    )

    repeat_rows = own_event_rows(ALL_BANKS)
    repeat_mechanism = structural_mechanism(repeat_rows, trees)
    repeat_supply = supply_sensitivity_probe(repeat_rows, trees)
    deterministic = all(
        (
            repeat_rows == rows,
            repeat_mechanism == mechanism,
            repeat_supply == supply,
            digest(repeat_rows) == digest(rows),
        )
    )
    elapsed = monotonic() - START

    reference_control = all(
        (
            reference["sha256"] == EXPECTED_TEXT_SHA256,
            reference["cycle786_resolved_commit"]
            == C786_REFERENCE_COMMIT,
            set(trees)
            == {
                "cycle793",
                "cycle788",
                "cycle788_checker",
                "cycle786",
                "cycle719_packet_core",
            },
        )
    )
    blocklist_control = all(
        (
            blocklist["finder_installed"],
            blocklist["none_loaded"],
            all(
                result["blocked"]
                for result in blocklist["attempts"].values()
            ),
            not own_audit["blocklisted_primary_AST_imports"],
        )
    )
    import_identity_control = all(
        (
            S750.H335 is H335,
            S750.O332 is O332,
            S750.K is K719,
            K719.B.__name__
            == "frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26",
        )
    )
    controls_base = all(
        (
            all(
                (
                    own_audit["literal_AUDIT_INPUT_PATHS"],
                    own_audit["DECLARED_INPUT_PATHS_alias"],
                    own_audit["all_audit_paths_exist"],
                    own_audit["direct_landed_imports_exact"],
                )
            ),
            input_anchors == EXPECTED_INPUT_SHA256,
            reference_control,
            blocklist_control,
            import_identity_control,
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
        )
    )

    recount_finding = (
        "Independent decoded-EventCell recount agrees: all 46 rows split "
        "23/23, with bank 1=1/1, bank 2=2/2, bank 3=3/3, bank 5=5/5, "
        "and bank 12=12/12."
        if recount_agreement
        else (
            "REFUTATION: the independent decoded-EventCell recount disagrees "
            f"with the claimed 23/23 per-bank census: {compact(by_bank)}."
        )
    )
    identity_finding = (
        "The independently reconstructed landed 38 rows have exact "
        "EventCell identity==epoch for all 38 and split 19/19."
        if certificate_d
        else (
            "REFUTATION: the landed-38 identity/orientation control is not "
            f"exact: {compact(landed_identity)}."
        )
    )

    base_lines = [
        "ANCHORS " + compact(input_anchors),
        "TEXT_REFERENCE_PROVENANCE " + compact(reference),
        "OWN_SOURCE_AUDIT " + compact(own_audit),
        "PRIMARY_BLOCKLIST " + compact(blocklist),
        "DERIVED_TARGET_MODE_RULE " + compact(mode_rule),
    ]
    for row in rows:
        base_lines.append("ORIENTATION_RECOUNT_ROW " + compact(row))
    for bank in ALL_BANKS:
        base_lines.append(
            "ORIENTATION_BY_BANK "
            + compact({"bank": bank, **by_bank[bank]})
        )
    base_lines.extend(
        [
            "ORIENTATION_TOTAL " + compact(total),
            "ORIENTATION_COMPOSITION "
            + compact(
                {
                    "landed_38": landed_counts,
                    "new_8": extension_counts,
                    "enlarged_46": total,
                }
            ),
            "FINDING_ORIENTATION_RECOUNT " + recount_finding,
            "STRUCTURAL_MODULE_EVIDENCE "
            + compact(mechanism["module_evidence"]),
        ]
    )
    for bank in ALL_BANKS:
        base_lines.append(
            "STRUCTURAL_EPOCH_PAIRS "
            + compact(
                {
                    "bank": bank,
                    "pairs": mechanism["pairs_by_bank"][bank],
                }
            )
        )
    base_lines.extend(
        [
            "STRUCTURAL_MECHANISM_VERDICT "
            + compact(
                {
                    "verdict": mechanism["verdict"],
                    "pair_checks": mechanism["pair_checks"],
                }
            ),
            "FINDING_STRUCTURAL_MECHANISM " + mechanism["finding"],
            "SUPPLY_VARIATION_SOURCE_CHECKS "
            + compact(supply["source_text_checks"]),
        ]
    )
    for row in supply["variation_rows"]:
        base_lines.append(
            "SUPPLY_SENSITIVITY_VARIATION " + compact(row)
        )
    base_lines.extend(
        [
            "SUPPLY_SENSITIVITY_VERDICT "
            + compact(
                {
                    "verdict": supply["verdict"],
                    "classifications": supply["classifications"],
                    "variation_count": supply["variation_count"],
                    "flip_count": supply["flip_count"],
                }
            ),
            "FINDING_SUPPLY_SENSITIVITY " + supply["finding"],
            "LANDED_IDENTITY_CONTROL " + compact(landed_identity),
            "FINDING_IDENTITY_CONTROL " + identity_finding,
            (
                "CERTIFICATE_A_PASS"
                if certificate_a
                else "CERTIFICATE_A_FAIL"
            )
            + " orientation recount all 46 rows + per-bank totals :: "
            + compact(
                {
                    "agreement": recount_agreement,
                    "by_bank": by_bank,
                    "total": total,
                    "rows_sha256": digest(rows),
                }
            ),
            (
                "CERTIFICATE_B_PASS"
                if certificate_b
                else "CERTIFICATE_B_FAIL"
            )
            + " structural-mechanism hunt :: "
            + compact(
                {
                    "hunt_complete": hunt_complete,
                    "verdict": mechanism["verdict"],
                    "pair_checks": mechanism["pair_checks"],
                    "source_checks": mechanism[
                        "module_evidence"
                    ]["source_checks"],
                }
            ),
            (
                "CERTIFICATE_C_PASS"
                if certificate_c
                else "CERTIFICATE_C_FAIL"
            )
            + " selecting-supply sensitivity probe :: "
            + compact(
                {
                    "verdict": supply["verdict"],
                    "exhausted": supply["exhausted"],
                    "variation_count": supply["variation_count"],
                    "flip_count": supply["flip_count"],
                    "rows_sha256": digest(supply["variation_rows"]),
                }
            ),
            (
                "CERTIFICATE_D_PASS"
                if certificate_d
                else "CERTIFICATE_D_FAIL"
            )
            + " landed 38 identity control :: "
            + compact(landed_identity),
        ]
    )

    def render(actual_stdout_bytes: int) -> tuple[str, bool]:
        certificate_e = (
            controls_base
            and actual_stdout_bytes < AUDIT_STDOUT_MAX_BYTES
        )
        certificates = {
            "A_orientation_recount": certificate_a,
            "B_structural_mechanism": certificate_b,
            "C_supply_sensitivity": certificate_c,
            "D_identity_control": certificate_d,
            "E_controls": certificate_e,
        }
        passed = all(certificates.values())
        status = (
            "NO_REFUTATION_FOUND"
            if passed and recount_agreement
            else (
                "PRIMARY_REFUTED"
                if not recount_agreement or not certificate_d
                else "CHECK_INCOMPLETE"
            )
        )
        control_detail = {
            "input_sha_anchors": input_anchors == EXPECTED_INPUT_SHA256,
            "text_sha_anchors": reference_control,
            "literal_input_tuple": own_audit[
                "literal_AUDIT_INPUT_PATHS"
            ],
            "exact_direct_landed_imports": own_audit[
                "direct_landed_imports_exact"
            ],
            "primary_blocklist": blocklist_control,
            "landed_import_identity": import_identity_control,
            "deterministic": deterministic,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "actual_stdout_bytes": actual_stdout_bytes,
            "stdout_limit_bytes": AUDIT_STDOUT_MAX_BYTES,
        }
        summary = {
            "cycle": 793,
            "checker": "independent_adversarial_per_bank_balance",
            "status": status,
            "pass": passed,
            "certificates": certificates,
            "recount_agreement": recount_agreement,
            "target_mode_rule": mode_rule["rule"],
            "per_bank": by_bank,
            "total": total,
            "mechanism_verdict": mechanism["verdict"],
            "supply_sensitivity_verdict": supply["verdict"],
            "landed_identity_control": landed_identity,
            "deterministic": deterministic,
            "runtime_seconds": round(elapsed, 6),
            "stdout_bytes": actual_stdout_bytes,
        }
        final_lines = base_lines + [
            (
                "CERTIFICATE_E_PASS"
                if certificate_e
                else "CERTIFICATE_E_FAIL"
            )
            + " sha anchors + primary blocklist + determinism + bounds :: "
            + compact(control_detail),
            "SUMMARY_JSON " + compact(summary),
            (
                "CYCLE793_BALANCE_INDEPENDENT_CHECK_PASS"
                if passed
                else "CYCLE793_BALANCE_INDEPENDENT_CHECK_FAIL"
            ),
        ]
        return "\n".join(final_lines) + "\n", passed

    measured = 0
    output = ""
    passed = False
    for _iteration in range(12):
        output, passed = render(measured)
        next_measured = len(output.encode("utf-8"))
        if next_measured == measured:
            break
        measured = next_measured
    output, passed = render(measured)
    if len(output.encode("utf-8")) != measured:
        output, passed = render(len(output.encode("utf-8")))
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
