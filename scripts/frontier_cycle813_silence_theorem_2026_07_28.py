#!/usr/bin/env python3
"""Cycle 813: exact invariant-level test of the k>=4 silence.

Only the landed Cycle-719 controller core is executable science input.
Cycle-736/758/790/791/792/794/798 primaries are SHA-pinned text/AST
references and are blocked from import.  The runner independently reconstructs
the synchronous word, the clean-postimage predicate, the separated translation
families, and the exact Boolean gate interpreter.

The terminal is deliberately three-way.  A bounded-horizon silence is never
promoted to an all-time theorem unless a proven conserved necessary condition
excludes the key.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

LINEAGE_REFERENCES = (
    {
        "cycle": 736,
        "commit": "723d0c20cb15f8a40bb3c997339978764f61c6bf",
        "path":
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
        "blob": "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
        "sha256":
            "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    },
    {
        "cycle": 758,
        "commit": "7a120caef64c8aacccb4c350594b8e91cca2f9c2",
        "path":
            "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
        "blob": "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
        "sha256":
            "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    },
    {
        "cycle": 790,
        "commit": "935e46cac19230caf123c8810af367d7cd843469",
        "path":
            "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
        "blob": "c322bb975900b2611c3f42d19da347a1dd5bfc56",
        "sha256":
            "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    },
    {
        "cycle": 791,
        "commit": "6255426f36a48494de43ccc8bd3eb9592e584c00",
        "path":
            "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
        "blob": "f026960526f2f2a8d990a5a7856b02217ea798ce",
        "sha256":
            "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    },
    {
        "cycle": 792,
        "commit": "04499b425103ba4635900a56f7370123a59345a4",
        "path":
            "scripts/frontier_cycle792_extended_horizon_selector_2026_07_28.py",
        "blob": "63948b09c41dd02b14350084ec33f7df9ad83b47",
        "sha256":
            "7f7470b3d759c84ccc0c2c6559d62448340fb8a0b0915eb98d450635a72730df",
    },
    {
        "cycle": 794,
        "commit": "0f4bace05de9b2830ea0b9a3f8a99f42a56cc301",
        "path":
            "scripts/frontier_cycle794_second_selection_2026_07_28.py",
        "blob": "a6debf306793270a4cda61638b619d4ad55dea69",
        "sha256":
            "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
    },
    {
        "cycle": 798,
        "commit": "c9073485c5eb446d417434416c015da9e0a1cff5",
        "path":
            "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
        "blob": "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
        "sha256":
            "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    },
)

BLOCKLISTED_MODULES = tuple(
    Path(row["path"]).stem for row in LINEAGE_REFERENCES
)
EXPECTED_719_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)
EXPECTED_719_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only lineage primary is imported."""

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
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
EXPECTED_CONFIGURATION_COUNTS = {
    0: 1,
    1: 11,
    2: 44,
    3: 77,
    4: 55,
    5: 11,
}
EXPECTED_FAMILY_COUNTS = {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
EXPECTED_SILENT_FAMILY_REPRESENTATIVES = {
    4: (
        (0, 2, 4, 6),
        (0, 2, 4, 7),
        (0, 2, 4, 8),
        (0, 2, 5, 7),
        (0, 2, 5, 8),
    ),
    5: ((0, 2, 4, 6, 8),),
}
EXPECTED_IDENTITY_CONTROLS = (
    {
        "k": 2,
        "positions": (1, 10),
        "event": 3,
        "first_clean_t": 252,
    },
    {
        "k": 2,
        "positions": (0, 7),
        "event": 3,
        "first_clean_t": 371,
    },
    {
        "k": 3,
        "positions": (0, 2, 5),
        "event": 2,
        "first_clean_t": 444,
    },
    {
        "k": 3,
        "positions": (0, 2, 5),
        "event": 3,
        "first_clean_t": 532,
    },
    {
        "k": 3,
        "positions": (0, 2, 4),
        "event": 1,
        "first_clean_t": 681,
    },
    {
        "k": 3,
        "positions": (0, 2, 4),
        "event": 2,
        "first_clean_t": 1385,
    },
)
PROVEN_INVARIANT_NAMES = (
    "UNWRITTEN_LINK_VECTOR_ZERO",
    "UNWRITTEN_LINK_OCCUPANCY_ZERO",
    "UNWRITTEN_LINK_PARITY_EVEN",
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def git_reference_payload(commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def literal_audit_paths() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignment = next(
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    )
    return (
        isinstance(assignment.value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignment.value.elts
        )
        and tuple(ast.literal_eval(assignment.value)) == AUDIT_INPUT_PATHS
    )


def source_controls() -> dict[str, object]:
    audit_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        audit_rows.append(
            {
                "path": relative,
                "exists": path.is_file(),
                "sha256": sha256(payload).hexdigest(),
                "git_blob": git_blob_sha(payload),
            }
        )

    reference_rows = []
    for reference in LINEAGE_REFERENCES:
        payload = git_reference_payload(
            str(reference["commit"]), str(reference["path"])
        )
        tree = ast.parse(
            payload.decode("utf-8"), filename=str(reference["path"])
        )
        reference_rows.append(
            {
                "cycle": reference["cycle"],
                "commit": reference["commit"],
                "path": reference["path"],
                "sha256": sha256(payload).hexdigest(),
                "git_blob": git_blob_sha(payload),
                "expected_sha256": reference["sha256"],
                "expected_blob": reference["blob"],
                "top_level_function_count": sum(
                    isinstance(node, ast.FunctionDef) for node in tree.body
                ),
                "AST_TEXT_ONLY_BLOCKLISTED": True,
                "match": (
                    sha256(payload).hexdigest() == reference["sha256"]
                    and git_blob_sha(payload) == reference["blob"]
                ),
            }
        )

    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_audit_paths(),
        "existing_worktree_relative": all(
            (ROOT / relative).is_file()
            and not Path(relative).is_absolute()
            for relative in AUDIT_INPUT_PATHS
        ),
        "audit_rows": audit_rows,
        "lineage_reference_rows": reference_rows,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_runtime_modules": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_tuple"]
        and result["existing_worktree_relative"]
        and len(audit_rows) == 1
        and audit_rows[0]["sha256"] == EXPECTED_719_SHA256
        and audit_rows[0]["git_blob"] == EXPECTED_719_BLOB
        and len(reference_rows) == 7
        and all(row["match"] for row in reference_rows)
        and not result["blocked_runtime_modules"]
        and not result["firewall_hits"]
    )
    return result


def tuple_state_to_int(state: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(state))


def int_state_to_tuple(state: int, width: int) -> tuple[int, ...]:
    return tuple((state >> index) & 1 for index in range(width))


def one_changed_coordinate(
    left: tuple[int, ...], right: tuple[int, ...]
) -> int:
    changed = tuple(
        index
        for index, (left_bit, right_bit) in enumerate(zip(left, right))
        if left_bit != right_bit
    )
    if len(changed) != 1 or len(left) != len(right):
        raise AssertionError(("basis coordinate", len(changed)))
    return changed[0]


def watched_bank_registers() -> tuple[tuple[str, int], ...]:
    rows = [
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
    ]
    rows.extend(
        (f"FRESH_{index}", wire)
        for index, wire in enumerate(K.A.FRESH)
    )
    rows.extend(
        (f"ZERO_WORK_{index}", wire)
        for index, wire in enumerate(K.A.ZERO_WORK)
    )
    rows.append(("TOKEN_OK", K.A.TOKEN_OK))
    return tuple(rows)


def clean_postimage_reimplementation(
    state: tuple[int, ...], bank_count: int
) -> bool:
    """Exact Cycle-758 definition, reconstructed without importing it."""

    banks, links = K.M.unpack_state(state, bank_count)
    return not any(
        (
            state[K.R3.X.SOURCE_POINTER],
            any(
                bank[wire]
                for bank in banks
                for _name, wire in watched_bank_registers()
            ),
            any(any(link) for link in links),
        )
    )


def watched_coordinate_basis() -> dict[str, object]:
    """Recover the exact absolute-bit basis used by clean_postimage."""

    genesis_banks, genesis_links = K.B.chain_genesis(FIXTURE_BANKS)
    packed = K.M.pack_state(genesis_banks, genesis_links)
    banks, links = K.M.unpack_state(packed, FIXTURE_BANKS)
    labels: dict[int, tuple[str, object, int]] = {
        K.R3.X.SOURCE_POINTER: ("source", "SOURCE_POINTER", 0)
    }

    for bank_index in range(FIXTURE_BANKS):
        for name, wire in watched_bank_registers():
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(link) for link in links]
            changed_banks[bank_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(link) for link in changed_links),
            )
            absolute = one_changed_coordinate(packed, changed)
            if absolute in labels:
                raise AssertionError(("duplicate watched coordinate", absolute))
            labels[absolute] = ("bank", name, bank_index)

    for link_index, link in enumerate(links):
        for wire in range(len(link)):
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(item) for item in links]
            changed_links[link_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(item) for item in changed_links),
            )
            absolute = one_changed_coordinate(packed, changed)
            if absolute in labels:
                raise AssertionError(("duplicate watched coordinate", absolute))
            labels[absolute] = ("link", f"WIRE_{wire}", link_index)

    mask = sum(1 << coordinate for coordinate in labels)
    expected_count = (
        1
        + FIXTURE_BANKS * len(watched_bank_registers())
        + sum(len(link) for link in links)
    )
    return {
        "packed_genesis": packed,
        "state_width": len(packed),
        "labels": labels,
        "mask": mask,
        "watched_coordinate_count": len(labels),
        "expected_coordinate_count": expected_count,
        "bank_register_count_per_bank": len(watched_bank_registers()),
        "link_coordinate_count": sum(len(link) for link in links),
        "basis_complete": (
            len(labels) == expected_count == 477
            and len(set(labels)) == len(labels)
        ),
    }


def clean_from_mask(state: int, watched_mask: int) -> bool:
    return not bool(state & watched_mask)


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def pairwise_separated(positions: tuple[int, ...]) -> bool:
    occupied = frozenset(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in occupied
    )


def configuration_families() -> dict[
    int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
]:
    grouped: dict[
        int, dict[tuple[int, ...], set[tuple[int, ...]]]
    ] = {}
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if not pairwise_separated(positions):
            continue
        representative = (
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
            if positions
            else ()
        )
        grouped.setdefault(len(positions), {}).setdefault(
            representative, set()
        ).add(positions)
    return {
        k: {
            representative: tuple(sorted(alternatives))
            for representative, alternatives in sorted(rows.items())
        }
        for k, rows in sorted(grouped.items())
    }


def build_fixtures(
    program: tuple[object, ...],
) -> tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append((event, direction, before))
        state = K.A.apply_semantic(
            before, K.M.global_allocator_word(FIXTURE_BANKS)
        )
    return tuple(rows)


def gate_signature(gate: object) -> tuple[str, tuple[int, ...]]:
    kind = str(gate.kind)
    wires = tuple(int(wire) for wire in gate.wires)
    expected_arity = {"X": 1, "CNOT": 2, "TOF": 3}
    if kind not in expected_arity or len(wires) != expected_arity[kind]:
        raise AssertionError(("unsupported exact gate", kind, wires))
    if len(set(wires)) != len(wires):
        raise AssertionError(("non-distinct gate wires", kind, wires))
    return kind, wires


def synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Exact independent Cycle-736 synchronous composition."""

    positions = tuple(token_positions)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station in range(len(program)):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int], ...]:
    compiled = []
    for gate in word:
        _kind, wires = gate_signature(gate)
        control_mask = sum(1 << wire for wire in wires[:-1])
        target_mask = 1 << wires[-1]
        compiled.append((control_mask, target_mask))
    return tuple(compiled)


def apply_compiled_word(
    state: int, compiled: tuple[tuple[int, int], ...]
) -> int:
    result = state
    for control_mask, target_mask in compiled:
        if result & control_mask == control_mask:
            result ^= target_mask
    return result


def local_gate_rule_truth_table() -> dict[str, object]:
    """Exhaustively check the independent bit rule against landed semantics."""

    constructors = {
        "X": (K.A.x(0), 1),
        "CNOT": (K.A.cn(0, 1), 2),
        "TOF": (K.A.tof(0, 1, 2), 3),
    }
    rows = {}
    for name, (gate, width) in constructors.items():
        compiled = compile_word((gate,))
        failures = []
        non_target_failures = []
        target = gate_signature(gate)[1][-1]
        for value in range(1 << width):
            state = tuple((value >> index) & 1 for index in range(width))
            landed = K.A.apply_semantic(state, (gate,))
            independent_int = apply_compiled_word(value, compiled)
            independent = int_state_to_tuple(independent_int, width)
            if independent != landed:
                failures.append((state, landed, independent))
            if any(
                landed[index] != state[index]
                for index in range(width)
                if index != target
            ):
                non_target_failures.append((state, landed))
        rows[name] = {
            "truth_rows": 1 << width,
            "semantic_failures": failures,
            "non_target_failures": non_target_failures,
        }
    return {
        "rows": rows,
        "pass": all(
            not row["semantic_failures"]
            and not row["non_target_failures"]
            for row in rows.values()
        ),
    }


def silent_keys(
    families: dict[
        int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
    ],
) -> tuple[tuple[int, tuple[int, ...], int], ...]:
    return tuple(
        (k, representative, event)
        for k in (4, 5)
        for representative in families[k]
        for event in range(2 * FIXTURE_BANKS)
    )


def exact_word_and_invariant_basis(
    program: tuple[object, ...],
    watched: dict[str, object],
    evaluated_positions: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    base_counter = Counter(
        gate_signature(gate)
        for row in program
        for gate in K.mapped_macro(row)
    )
    rows = []
    common_unwritten: frozenset[int] | None = None
    for positions in evaluated_positions:
        word = synchronous_word(program, positions)
        signatures = tuple(gate_signature(gate) for gate in word)
        targets = frozenset(wires[-1] for _kind, wires in signatures)
        unwritten = frozenset(watched["labels"]) - targets
        if common_unwritten is None:
            common_unwritten = unwritten
        expected_counter = Counter(
            {
                signature: count * len(positions)
                for signature, count in base_counter.items()
            }
        )
        rows.append(
            {
                "positions": positions,
                "k": len(positions),
                "gate_count": len(word),
                "gate_multiset_is_k_copies":
                    Counter(signatures) == expected_counter,
                "unwritten_coordinates_equal_common":
                    unwritten == common_unwritten,
                "word_sha256": digest(signatures),
            }
        )

    if common_unwritten is None:
        raise AssertionError("no evaluated positions")
    labels = watched["labels"]
    unwritten_labels = tuple(
        labels[coordinate] for coordinate in sorted(common_unwritten)
    )
    local_link_wires = tuple(
        int(str(label[1]).removeprefix("WIRE_"))
        for label in unwritten_labels
        if label[0] == "link"
    )
    expected_local_link_wires = tuple(
        range(183, 191)
    ) + tuple(range(288, 382))
    unwritten_mask = sum(1 << coordinate for coordinate in common_unwritten)
    watched_mask = int(watched["mask"])
    return {
        "rows": rows,
        "unwritten_coordinates": tuple(sorted(common_unwritten)),
        "unwritten_labels": unwritten_labels,
        "unwritten_mask": unwritten_mask,
        "unwritten_count": len(common_unwritten),
        "written_watched_count":
            int(watched["watched_coordinate_count"]) - len(common_unwritten),
        "all_unwritten_are_links":
            all(label[0] == "link" for label in unwritten_labels),
        "exact_unwritten_link_ranges":
            local_link_wires == expected_local_link_wires,
        "clean_implication_by_mask_subset":
            unwritten_mask & ~watched_mask == 0,
        "gate_level_invariance": all(
            row["gate_multiset_is_k_copies"]
            and row["unwritten_coordinates_equal_common"]
            for row in rows
        ),
        "pass": (
            len(common_unwritten) == 102
            and all(label[0] == "link" for label in unwritten_labels)
            and local_link_wires == expected_local_link_wires
            and unwritten_mask & ~watched_mask == 0
            and all(
                row["gate_multiset_is_k_copies"]
                and row["unwritten_coordinates_equal_common"]
                for row in rows
            )
        ),
    }


def landed_initial_word_cross_checks(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    positions_rows: tuple[tuple[int, ...], ...],
    watched_mask: int,
) -> dict[str, object]:
    rows = []
    for positions in positions_rows:
        word = synchronous_word(program, positions)
        compiled = compile_word(word)
        expected_tokens = tuple(
            int(station in positions)
            for station in range(len(program))
        )
        for event, _direction, before in fixtures:
            independent = apply_compiled_word(
                tuple_state_to_int(before), compiled
            )
            landed, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=positions
            )
            independent_tuple = int_state_to_tuple(
                independent, len(before)
            )
            rows.append(
                {
                    "key": (len(positions), positions, event),
                    "independent_equals_landed":
                        independent_tuple == landed,
                    "rails_return":
                        rail_a == expected_tokens and not any(rail_b),
                    "clean_predicates_agree": (
                        clean_from_mask(independent, watched_mask)
                        == clean_postimage_reimplementation(
                            independent_tuple, FIXTURE_BANKS
                        )
                    ),
                }
            )
    return {
        "rows": rows,
        "pass": all(
            row["independent_equals_landed"]
            and row["rails_return"]
            and row["clean_predicates_agree"]
            for row in rows
        ),
    }


def identity_controls(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    watched: dict[str, object],
    invariant: dict[str, object],
) -> tuple[dict[str, object], ...]:
    fixture_by_event = {row[0]: row for row in fixtures}
    watched_mask = int(watched["mask"])
    unwritten_mask = int(invariant["unwritten_mask"])
    state_width = int(watched["state_width"])
    rows = []
    for control in EXPECTED_IDENTITY_CONTROLS:
        positions = tuple(control["positions"])
        event = int(control["event"])
        moment = int(control["first_clean_t"])
        _event, direction, before_tuple = fixture_by_event[event]
        state = tuple_state_to_int(before_tuple)
        initial_unwritten = state & unwritten_mask
        compiled = compile_word(synchronous_word(program, positions))
        t_minus_1_state = None
        invariant_preserved = True
        for horizon_t in range(moment + 1):
            state = apply_compiled_word(state, compiled)
            invariant_preserved &= (
                state & unwritten_mask
            ) == initial_unwritten
            if horizon_t == moment - 1:
                t_minus_1_state = state
        if t_minus_1_state is None:
            raise AssertionError(("invalid control moment", moment))
        final_tuple = int_state_to_tuple(state, state_width)
        before_clean = clean_from_mask(
            t_minus_1_state, watched_mask
        )
        at_clean = clean_from_mask(state, watched_mask)
        rows.append(
            {
                **control,
                "direction": direction,
                "t_minus_1_clean": before_clean,
                "t_clean": at_clean,
                "clean_definition_direct_agreement":
                    at_clean
                    == clean_postimage_reimplementation(
                        final_tuple, FIXTURE_BANKS
                    ),
                "invariant_preserved_every_orbit":
                    invariant_preserved,
                "invariant_values": {
                    PROVEN_INVARIANT_NAMES[0]:
                        state & unwritten_mask,
                    PROVEN_INVARIANT_NAMES[1]:
                        (state & unwritten_mask).bit_count(),
                    PROVEN_INVARIANT_NAMES[2]:
                        (state & unwritten_mask).bit_count() & 1,
                },
                "all_proven_necessary_conditions_hold":
                    not bool(state & unwritten_mask),
                "final_watched_weight":
                    (state & watched_mask).bit_count(),
                "pass": (
                    not before_clean
                    and at_clean
                    and clean_postimage_reimplementation(
                        final_tuple, FIXTURE_BANKS
                    )
                    and invariant_preserved
                    and not bool(state & unwritten_mask)
                ),
            }
        )
    return tuple(rows)


def evaluate_silent_keys(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    keys: tuple[tuple[int, tuple[int, ...], int], ...],
    watched: dict[str, object],
    invariant: dict[str, object],
) -> tuple[dict[str, object], ...]:
    fixture_by_event = {row[0]: row for row in fixtures}
    watched_mask = int(watched["mask"])
    unwritten_mask = int(invariant["unwritten_mask"])
    rows = []
    for k, positions, event in keys:
        _event, direction, before_tuple = fixture_by_event[event]
        before = tuple_state_to_int(before_tuple)
        compiled = compile_word(synchronous_word(program, positions))
        at_t0 = apply_compiled_word(before, compiled)
        initial_value = before & unwritten_mask
        t0_value = at_t0 & unwritten_mask
        condition_rows = {
            PROVEN_INVARIANT_NAMES[0]: {
                "required_value": 0,
                "conserved_value": initial_value,
                "status": (
                    "COMPATIBLE"
                    if initial_value == 0
                    else "VIOLATED-FOREVER"
                ),
            },
            PROVEN_INVARIANT_NAMES[1]: {
                "required_value": 0,
                "conserved_value": initial_value.bit_count(),
                "status": (
                    "COMPATIBLE"
                    if initial_value.bit_count() == 0
                    else "VIOLATED-FOREVER"
                ),
            },
            PROVEN_INVARIANT_NAMES[2]: {
                "required_value": 0,
                "conserved_value": initial_value.bit_count() & 1,
                "status": (
                    "COMPATIBLE"
                    if initial_value.bit_count() & 1 == 0
                    else "VIOLATED-FOREVER"
                ),
            },
            "DYNAMIC_WRITTEN_WATCHED_ZERO": {
                "required_value": 0,
                "value_at_t0":
                    (
                        at_t0
                        & (watched_mask & ~unwritten_mask)
                    ).bit_count(),
                "status": "UNDECIDED",
                "reason":
                    "375 cleanliness-watched coordinates are gate targets",
            },
        }
        violated = tuple(
            name
            for name in PROVEN_INVARIANT_NAMES
            if condition_rows[name]["status"] == "VIOLATED-FOREVER"
        )
        rows.append(
            {
                "key": (k, positions, event),
                "k": k,
                "positions": positions,
                "event": event,
                "direction": direction,
                "condition_rows": condition_rows,
                "invariant_preserved_at_t0":
                    initial_value == t0_value,
                "outcome": (
                    "VIOLATED-FOREVER" if violated else "COMPATIBLE"
                ),
                "violated_invariants": violated,
            }
        )
    return tuple(rows)


def discarded_candidate_context(
    watched_mask: int,
) -> tuple[dict[str, object], ...]:
    clean_state = 0
    adjacent_positions = (0, 1)
    return (
        {
            "candidate": "TOKEN_COUNT",
            "status": "DISCARDED_NOT_NECESSARY_FROM_CLEAN_POSTIMAGE",
            "machine_counterexample":
                clean_from_mask(clean_state, watched_mask)
                and len(adjacent_positions) == 2,
            "reason":
                "clean_postimage has no controller-rail/count argument",
        },
        {
            "candidate": "PAIRWISE_SEPARATION_AND_GAP_MULTISET",
            "status": "DISCARDED_NOT_NECESSARY_FROM_CLEAN_POSTIMAGE",
            "machine_counterexample":
                clean_from_mask(clean_state, watched_mask)
                and not pairwise_separated(adjacent_positions),
            "reason":
                "rail rotation conserves separation, but cleanliness does "
                "not inspect rails",
        },
        {
            "candidate": "DYNAMIC_WRITTEN_WATCHED_ZERO",
            "status": "UNDECIDED_TIME_DEPENDENT",
            "reason":
                "necessary by cleanliness but not conserved because these "
                "coordinates occur as X/CNOT/TOF targets",
        },
    )


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program = K.interleaved_program(FIXTURE_BANKS)
    fixtures = build_fixtures(program)
    families = configuration_families()
    keys = silent_keys(families)
    known_positions = tuple(
        sorted(
            {
                tuple(row["positions"])
                for row in EXPECTED_IDENTITY_CONTROLS
            }
        )
    )
    silent_positions = tuple(
        sorted({positions for _k, positions, _event in keys})
    )
    evaluated_positions = tuple(
        sorted(set(known_positions) | set(silent_positions))
    )
    watched = watched_coordinate_basis()
    gate_rules = local_gate_rule_truth_table()
    invariant = exact_word_and_invariant_basis(
        program, watched, evaluated_positions
    )
    cross_checks = landed_initial_word_cross_checks(
        program,
        fixtures,
        evaluated_positions,
        int(watched["mask"]),
    )
    identity_first = identity_controls(
        program, fixtures, watched, invariant
    )
    silent_first = evaluate_silent_keys(
        program, fixtures, keys, watched, invariant
    )
    identity_second = identity_controls(
        program, fixtures, watched, invariant
    )
    silent_second = evaluate_silent_keys(
        program, fixtures, keys, watched, invariant
    )
    first_digest = digest((identity_first, silent_first))
    second_digest = digest((identity_second, silent_second))

    configuration_counts = {
        k: sum(len(alternatives) for alternatives in rows.values())
        for k, rows in families.items()
    }
    family_counts = {k: len(rows) for k, rows in families.items()}
    catalog_pass = (
        configuration_counts == EXPECTED_CONFIGURATION_COUNTS
        and family_counts == EXPECTED_FAMILY_COUNTS
        and {
            k: tuple(families[k])
            for k in (4, 5)
        }
        == EXPECTED_SILENT_FAMILY_REPRESENTATIVES
        and len(keys) == 24
        and Counter(k for k, _positions, _event in keys)
        == Counter({4: 20, 5: 4})
    )
    necessity_proof = {
        "names": PROVEN_INVARIANT_NAMES,
        "logical_dependency":
            "UNWRITTEN_LINK_VECTOR_ZERO is the fundamental 102-bit "
            "invariant; occupancy-zero and parity-even are exact scalar "
            "corollaries, not independent generators.",
        "proof_chain": (
            "Every landed X/CNOT/TOF gate changes only its last (target) "
            "wire; the exhaustive local truth tables pass.",
            "The 102 listed cleanliness-watched link coordinates are absent "
            "from every gate target in every evaluated nonempty synchronous "
            "word, so their vector is gate-by-gate invariant.",
            "clean_postimage is exactly the zero test on all 477 watched "
            "coordinates; mask inclusion therefore proves clean implies "
            "zero vector, zero occupancy, and even/zero parity.",
        ),
        "watched_coordinate_count":
            watched["watched_coordinate_count"],
        "unwritten_count": invariant["unwritten_count"],
        "written_dynamic_count": invariant["written_watched_count"],
        "unwritten_labels": invariant["unwritten_labels"],
        "mask_subset_implication":
            invariant["clean_implication_by_mask_subset"],
        "gate_rule_truth_tables": gate_rules,
        "discarded_or_undecided_candidates":
            discarded_candidate_context(int(watched["mask"])),
    }
    certificate_a = (
        watched["basis_complete"]
        and gate_rules["pass"]
        and invariant["pass"]
        and cross_checks["pass"]
        and all(
            row["machine_counterexample"]
            for row in discarded_candidate_context(int(watched["mask"]))
            if "machine_counterexample" in row
        )
    )
    check(
        "CERTIFICATE_A_PROVEN_NECESSARY_INVARIANTS",
        certificate_a,
        necessity_proof,
    )

    certificate_b = (
        len(identity_first) == 6
        and identity_first == identity_second
        and tuple(
            (row["k"], row["first_clean_t"])
            for row in identity_first
        )
        == ((2, 252), (2, 371), (3, 444), (3, 532), (3, 681), (3, 1385))
        and all(row["pass"] for row in identity_first)
    )
    OUTPUT_LINES.append(
        "IDENTITY_CONTROL_ROWS " + compact(identity_first)
    )
    check(
        "CERTIFICATE_B_SIX_FIRST_CLEAN_IDENTITY_CONTROLS",
        certificate_b,
        {
            "control_count": len(identity_first),
            "moments": tuple(
                row["first_clean_t"] for row in identity_first
            ),
            "all_conditions_hold": all(
                row["all_proven_necessary_conditions_hold"]
                for row in identity_first
            ),
            "direct_t_minus_1_nonclean_and_t_clean": all(
                not row["t_minus_1_clean"] and row["t_clean"]
                for row in identity_first
            ),
        },
    )

    for row in silent_first:
        OUTPUT_LINES.append("SILENT_KEY_ROW " + compact(row))
    violated_rows = tuple(
        row
        for row in silent_first
        if row["outcome"] == "VIOLATED-FOREVER"
    )
    compatible_rows = tuple(
        row for row in silent_first if row["outcome"] == "COMPATIBLE"
    )
    certificate_c = (
        catalog_pass
        and len(silent_first) == 24
        and silent_first == silent_second
        and all(row["invariant_preserved_at_t0"] for row in silent_first)
        and len(violated_rows) + len(compatible_rows) == 24
        and all(
            row["condition_rows"]["DYNAMIC_WRITTEN_WATCHED_ZERO"][
                "status"
            ] == "UNDECIDED"
            for row in silent_first
        )
    )
    check(
        "CERTIFICATE_C_ALL_24_SILENT_KEYS",
        certificate_c,
        {
            "configuration_counts": configuration_counts,
            "family_counts": family_counts,
            "key_counts": dict(
                sorted(Counter(row["k"] for row in silent_first).items())
            ),
            "VIOLATED-FOREVER": len(violated_rows),
            "COMPATIBLE": len(compatible_rows),
            "UNDECIDED_time_dependent_condition_rows": len(silent_first),
        },
    )

    if len(violated_rows) == 24:
        verdict = "SILENCE_STRUCTURAL"
    elif violated_rows:
        verdict = "SILENCE_PARTIALLY_STRUCTURAL"
    else:
        verdict = "SILENCE_UNEXPLAINED_AT_THIS_LEVEL"
    certificate_d = (
        (
            verdict == "SILENCE_STRUCTURAL"
            and len(violated_rows) == 24
        )
        or (
            verdict == "SILENCE_PARTIALLY_STRUCTURAL"
            and 0 < len(violated_rows) < 24
        )
        or (
            verdict == "SILENCE_UNEXPLAINED_AT_THIS_LEVEL"
            and not violated_rows
        )
    )
    check(
        "CERTIFICATE_D_VERDICT",
        certificate_d,
        {
            "verdict": verdict,
            "VIOLATED-FOREVER": len(violated_rows),
            "COMPATIBLE": len(compatible_rows),
            "violated_key_invariant_rows": tuple(
                {
                    "key": row["key"],
                    "violated_invariants": row["violated_invariants"],
                }
                for row in violated_rows
            ),
            "sharpest_structure":
                "102/477 cleanliness coordinates form a gate-by-gate "
                "conserved link vector, but all 24 keys lie in its "
                "clean-compatible zero fiber; the remaining 375-coordinate "
                "projection is time-dependent.",
        },
    )

    elapsed = monotonic() - started
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 16 * 1024
    )
    deterministic = (
        identity_first == identity_second
        and silent_first == silent_second
        and first_digest == second_digest
    )
    certificate_e = (
        controls["pass"]
        and not IMPORT_FIREWALL.hits
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_SHA_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT",
        certificate_e,
        {
            "source_controls": controls,
            "deterministic": deterministic,
            "first_sha256": first_digest,
            "second_sha256": second_digest,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    passed = all(CHECKS.values())
    terminal = {
        "terminal": (
            "CYCLE813_SILENCE_THEOREM_PASS"
            if passed
            else "CYCLE813_SILENCE_THEOREM_HONEST_FAIL"
        ),
        "pass": passed,
        "proven_invariant_count": len(PROVEN_INVARIANT_NAMES),
        "proven_invariants": PROVEN_INVARIANT_NAMES,
        "identity_control_count": len(identity_first),
        "identity_moments": tuple(
            row["first_clean_t"] for row in identity_first
        ),
        "VIOLATED-FOREVER": len(violated_rows),
        "COMPATIBLE": len(compatible_rows),
        "UNDECIDED_time_dependent_condition_rows": len(silent_first),
        "verdict": verdict,
        "determinism_sha256": first_digest,
        "runtime_seconds": round(elapsed, 6),
    }
    output = "\n".join(OUTPUT_LINES) + "\nFINAL " + compact(terminal) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit")
    sys.stdout.write(output)
    return 0 if terminal["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
