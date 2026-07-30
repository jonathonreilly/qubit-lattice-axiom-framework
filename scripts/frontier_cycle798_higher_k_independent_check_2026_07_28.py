#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-798 higher-k claim.

Only the landed Cycle-719 controller core is executable science input.  The
Cycle-798 primary and every later lineage/reference source are blocklisted and
read only as text or top-level AST.  Dynamics, the separated-configuration
census, translation families, gate interpretation, cycle hashing, and the
monitored-selector recount are implemented here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

BLOCKLIST_TEXT_PATHS = (
    "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle784_full_strata_ties_2026_07_28.py",
    "scripts/frontier_cycle794_second_selection_2026_07_28.py",
)

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

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

GIT_TEXT_REFERENCES = {
    "cycle759_primary": {
        "module":
            "frontier_cycle759_multisource_postimage_law_2026_07_28",
        "path":
            "scripts/frontier_cycle759_multisource_postimage_law_2026_07_28.py",
        "git_blob_sha1": "e18482f01677b769d4e3d4b3945d7169d4696491",
        "sha256":
            "59c92f46aec9249e6dd46c8a8423223ffaa8c1b54cdc8a33ee402373b19292f0",
    },
    "cycle787_primary": {
        "module":
            "frontier_cycle787_k5_stratum_unified_veto_2026_07_28",
        "path":
            "scripts/frontier_cycle787_k5_stratum_unified_veto_2026_07_28.py",
        "git_blob_sha1": "1f432d2b869b8b611ae728fe55a8d5fa685e9d29",
        "sha256":
            "177c24792478009a76376c06105594181587cf7d318d562060cafec40088707c",
    },
}

BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in BLOCKLIST_TEXT_PATHS
) + tuple(
    row["module"] for row in GIT_TEXT_REFERENCES.values()
)


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if later code tries to execute a text-only reference."""

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
TARGET_STRATA = (3, 4, 5)
SCAN_HORIZON_T = 2048
CLAIMED_TRANSIENT_MOMENTS = (444, 532, 681, 1385)
CLAIMED_FIRST_KEY = (3, (0, 2, 5), 2)
EXPECTED_K2_TRANSIENTS = (
    (3, (1, 10), 252),
    (3, (0, 7), 371),
)
EXPECTED_CONFIGURATION_COUNTS = {
    0: 1,
    1: 11,
    2: 44,
    3: 77,
    4: 55,
    5: 11,
}
EXPECTED_FAMILY_COUNTS = {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
EXPECTED_CLASS_COUNTS = {
    3: {"exact_tie": 7, "unique_survivor": 3, "zero_survivors": 18},
    4: {"exact_tie": 0, "unique_survivor": 0, "zero_survivors": 20},
    5: {"exact_tie": 0, "unique_survivor": 0, "zero_survivors": 4},
}
EXPECTED_ZERO_COUNTS = {3: 18, 4: 20, 5: 4}
EXPANDED_EXCLUSIONS = (
    "census_membership",
    "pairwise_separation",
    "synchronization",
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
PRIMARY_EXCLUSIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
SELECTION_HORIZONS = tuple(range(443, 451))

EXPECTED_DISK_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    BLOCKLIST_TEXT_PATHS[0]:
        "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    BLOCKLIST_TEXT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    BLOCKLIST_TEXT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    BLOCKLIST_TEXT_PATHS[3]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    BLOCKLIST_TEXT_PATHS[4]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    BLOCKLIST_TEXT_PATHS[5]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    BLOCKLIST_TEXT_PATHS[6]:
        "b532563da6aa8e84ae8aae2c4ad14c10a50d45d43c020ca2107fd48b79dc8a30",
    BLOCKLIST_TEXT_PATHS[7]:
        "5fcb9f015b7690df833a3b3d1dc7bdc81162e066f1f25d34d420d8779c563582",
}
EXPECTED_DISK_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    BLOCKLIST_TEXT_PATHS[0]: "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
    BLOCKLIST_TEXT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    BLOCKLIST_TEXT_PATHS[2]: "0a8f4562d28f12ed64130b3c3b23fccab677d333",
    BLOCKLIST_TEXT_PATHS[3]: "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0",
    BLOCKLIST_TEXT_PATHS[4]: "87ba84671c246fe3b7473980d395ea94443921fc",
    BLOCKLIST_TEXT_PATHS[5]: "3eff0f787a12cacf504324209f578f0c1df91c90",
    BLOCKLIST_TEXT_PATHS[6]: "b718499f3b6fd1498b9c99e8b87926dcc057f385",
    BLOCKLIST_TEXT_PATHS[7]: "a6debf306793270a4cda61638b619d4ad55dea69",
}

CHECKS: dict[str, bool] = {}
FINDINGS: list[str] = []
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    framed = f"blob {len(payload)}\0".encode("ascii") + payload
    return sha1(framed).hexdigest()


def check(
    label: str,
    condition: bool,
    detail: object,
    finding: str | None = None,
) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    if not passed and finding is not None:
        FINDINGS.append(finding)
        OUTPUT_LINES.append("REFUTES_PRIMARY FINDING_VERBATIM :: " + finding)
    return passed


def fixed_git_blob(blob_sha1: str) -> bytes:
    completed = subprocess.run(
        ("git", "cat-file", "blob", blob_sha1),
        cwd=ROOT,
        check=False,
        capture_output=True,
        timeout=60,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            (
                "unavailable immutable Git text reference",
                blob_sha1,
                completed.stderr.decode("utf-8", errors="replace")[:500],
            )
        )
    if git_blob_sha(completed.stdout) != blob_sha1:
        raise AssertionError(("Git blob framing mismatch", blob_sha1))
    return completed.stdout


def literal_assignment(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        value: ast.AST | None = None
        targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            value = node.value
            targets = tuple(node.targets)
        elif isinstance(node, ast.AnnAssign):
            value = node.value
            targets = (node.target,)
        if value is not None and any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(ast.literal_eval(value))
    if len(matches) != 1:
        raise AssertionError(("literal assignment", name, len(matches)))
    return matches[0]


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("named function", name, len(matches)))
    return matches[0]


def local_literal_assignment(
    tree: ast.Module,
    function_name: str,
    assignment_name: str,
) -> object:
    function = named_function(tree, function_name)
    matches = [
        ast.literal_eval(node.value)
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == assignment_name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        raise AssertionError(
            (
                "local literal assignment",
                function_name,
                assignment_name,
                len(matches),
            )
        )
    return matches[0]


def function_arguments(function: ast.FunctionDef) -> tuple[str, ...]:
    return tuple(argument.arg for argument in function.args.args)


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=str(Path(__file__)),
    )
    disk_rows: dict[str, object] = {}
    trees: dict[str, ast.Module] = {}
    for relative in (*AUDIT_INPUT_PATHS, *BLOCKLIST_TEXT_PATHS):
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        observed_sha = sha256(payload).hexdigest()
        observed_blob = git_blob_sha(payload)
        disk_rows[relative] = {
            "exists": path.is_file(),
            "sha256": observed_sha,
            "expected_sha256": EXPECTED_DISK_SHA256[relative],
            "git_blob_sha1": observed_blob,
            "expected_git_blob_sha1": EXPECTED_DISK_GIT_BLOBS[relative],
            "match": (
                path.is_file()
                and observed_sha == EXPECTED_DISK_SHA256[relative]
                and observed_blob == EXPECTED_DISK_GIT_BLOBS[relative]
            ),
            "execution_mode": (
                "LANDED_IMPORT"
                if relative in AUDIT_INPUT_PATHS
                else "TEXT_ONLY_BLOCKLISTED"
            ),
        }
        if relative in BLOCKLIST_TEXT_PATHS and path.is_file():
            trees[relative] = ast.parse(
                payload.decode("utf-8"), filename=relative
            )

    git_rows = {}
    for label, reference in GIT_TEXT_REFERENCES.items():
        payload = fixed_git_blob(reference["git_blob_sha1"])
        observed_sha = sha256(payload).hexdigest()
        git_rows[label] = {
            **reference,
            "observed_sha256": observed_sha,
            "observed_git_blob_sha1": git_blob_sha(payload),
            "match": (
                observed_sha == reference["sha256"]
                and git_blob_sha(payload) == reference["git_blob_sha1"]
            ),
            "execution_mode": "IMMUTABLE_GIT_BLOB_TEXT_ONLY_BLOCKLISTED",
        }
        trees[reference["path"]] = ast.parse(
            payload.decode("utf-8"), filename=reference["path"]
        )

    assignments: dict[str, ast.AST] = {}
    direct_imports = []
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            direct_imports.extend(alias.name for alias in node.names)
    input_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    literal_inputs = (
        isinstance(input_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in input_node.elts
        )
        and tuple(ast.literal_eval(input_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
    )
    science_imports = tuple(
        name for name in direct_imports if name.startswith("frontier_cycle")
    )
    forbidden_dynamic_calls = tuple(
        ast.unparse(node)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"exec", "eval", "compile", "__import__"}
    )
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal_exact": literal_inputs,
        "direct_science_imports": science_imports,
        "direct_science_imports_exact": science_imports
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        ),
        "blocklist_text_paths": BLOCKLIST_TEXT_PATHS,
        "blocklisted_modules": BLOCKLISTED_MODULES,
        "blocked_runtime_modules": tuple(
            module for module in BLOCKLISTED_MODULES if module in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "forbidden_dynamic_calls": forbidden_dynamic_calls,
        "disk_rows": disk_rows,
        "git_text_rows": git_rows,
    }
    report["pass"] = (
        literal_inputs
        and report["direct_science_imports_exact"]
        and not report["blocked_runtime_modules"]
        and not report["firewall_hits"]
        and not forbidden_dynamic_calls
        and all(row["match"] for row in disk_rows.values())
        and all(row["match"] for row in git_rows.values())
    )
    return report, trees


Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def pairwise_separated(positions: tuple[int, ...]) -> bool:
    occupied = set(positions)
    return all(
        (station + 1) % RING_STATIONS not in occupied
        for station in occupied
    )


def independent_configuration_census(
) -> dict[int, tuple[tuple[int, ...], ...]]:
    grouped: dict[int, list[tuple[int, ...]]] = {
        k: [] for k in range(6)
    }
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if pairwise_separated(positions):
            grouped[len(positions)].append(positions)
    return {
        k: tuple(sorted(positions))
        for k, positions in grouped.items()
    }


def independent_translation_families(
    configurations: dict[int, tuple[tuple[int, ...], ...]],
) -> dict[
    int,
    dict[tuple[int, ...], tuple[tuple[int, ...], ...]],
]:
    result = {}
    for k, positions_rows in configurations.items():
        grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
        for positions in positions_rows:
            representative = (
                min(
                    rotate_positions(positions, shift)
                    for shift in range(RING_STATIONS)
                )
                if positions
                else ()
            )
            grouped.setdefault(representative, set()).add(positions)
        result[k] = {
            representative: tuple(sorted(members))
            for representative, members in sorted(grouped.items())
        }
    return result


def independent_gate_word(
    bits: tuple[int, ...],
    gates: tuple[object, ...],
) -> tuple[int, ...]:
    """Second implementation of the landed X/CNOT/Toffoli semantics."""

    state = list(bits)
    for gate in gates:
        if gate.kind == "X":
            state[gate.wires[0]] ^= 1
        elif gate.kind == "CNOT":
            control, target = gate.wires
            state[target] ^= state[control]
        elif gate.kind == "TOF":
            left, right, target = gate.wires
            state[target] ^= state[left] & state[right]
        else:
            raise AssertionError(("unknown landed gate", gate))
    return tuple(state)


def synchronous_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Fresh expansion of the simultaneous Q layers over one orbit."""

    live = tuple(positions)
    gates = []
    for _step in range(len(program)):
        occupied = set(live)
        for station, row in enumerate(program):
            if station in occupied:
                gates.extend(K.mapped_macro(row))
        live = tuple(
            (position + 1) % len(program) for position in live
        )
    if tuple(sorted(live)) != tuple(sorted(positions)):
        raise AssertionError(("scheduler did not close", positions, live))
    return tuple(gates)


def expected_forward_trace(
    positions: tuple[int, ...],
    stations: int,
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            tuple(
                sorted(
                    (position + step) % stations
                    for position in positions
                )
            ),
            tuple(
                sorted(
                    (position + step + 1) % stations
                    for position in positions
                )
            ),
            0,
        )
        for step in range(stations)
    )


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


def watched_bank_registers_759() -> tuple[tuple[str, int], ...]:
    return (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH[{index}]", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK[{index}]", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def residual_support(state: tuple[int, ...]) -> Support:
    """Own exact support projection of the postimage-cleanliness registers."""

    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    result: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        result.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register, wire in watched_bank_registers():
            if bank[wire]:
                result.add(("bank", register, bank_index))
    for link_index, link in enumerate(links):
        for wire, content in enumerate(link):
            if content:
                result.add(("link", f"WIRE_{wire}", link_index))
    return frozenset(result)


def postimage_residual(
    after: int, bank_count: int
) -> tuple[tuple[str, str, int, int], ...]:
    """Exact content-bearing Cycle-759 projection, independently transcribed."""

    banks, links = K.M.unpack_state(after, bank_count)
    residual = []
    source_content = after[K.R3.X.SOURCE_POINTER]
    if source_content:
        residual.append(
            (
                "source",
                "SOURCE_POINTER",
                K.R3.X.SOURCE_POINTER,
                source_content,
            )
        )
    for bank_index, bank in enumerate(banks):
        for register, wire in watched_bank_registers_759():
            content = bank[wire]
            if content:
                residual.append(
                    (
                        f"bank[{bank_index}]",
                        register,
                        wire,
                        content,
                    )
                )
    for link_index, link in enumerate(links):
        for wire, content in enumerate(link):
            if content:
                residual.append(
                    (
                        f"link[{link_index}]",
                        f"WIRE[{wire}]",
                        wire,
                        content,
                    )
                )
    return tuple(residual)


def landed_clean_postimage(after: int, bank_count: int) -> bool:
    """Direct reconstruction of the landed Cycle-758 Boolean predicate."""

    banks, links = K.M.unpack_state(after, bank_count)
    return not any(
        (
            after[K.R3.X.SOURCE_POINTER],
            any(
                bank[wire]
                for bank in banks
                for wire in (
                    K.A.POINTER,
                    K.A.U_TO_V,
                    K.A.V_TO_U,
                    K.A.DIRECTION_OK,
                    *K.A.FRESH,
                    *K.A.ZERO_WORK,
                    K.A.TOKEN_OK,
                )
            ),
            any(any(link) for link in links),
        )
    )


def attribute_tokens(function: ast.FunctionDef) -> tuple[str, ...]:
    return tuple(
        sorted(
            {
                ast.unparse(node)
                for node in ast.walk(function)
                if isinstance(node, ast.Attribute)
            }
        )
    )


def residual_definition_audit(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    path758 = BLOCKLIST_TEXT_PATHS[3]
    path762 = BLOCKLIST_TEXT_PATHS[4]
    path762_independent = BLOCKLIST_TEXT_PATHS[5]
    path798 = BLOCKLIST_TEXT_PATHS[0]
    path759 = GIT_TEXT_REFERENCES["cycle759_primary"]["path"]

    clean758 = named_function(trees[path758], "clean_postimage")
    residual759 = named_function(trees[path759], "postimage_residual")
    clean759 = named_function(trees[path759], "clean_postimage")
    residual762 = named_function(
        trees[path762_independent], "residual_support"
    )
    extract762 = named_function(
        trees[path762], "extract_cycle759_projection"
    )
    main798_source = ast.unparse(named_function(trees[path798], "main"))

    forbidden_input_names = {"k", "positions", "token_positions"}
    residual759_names = {
        node.id
        for node in ast.walk(residual759)
        if isinstance(node, ast.Name)
    }
    clean758_names = {
        node.id
        for node in ast.walk(clean758)
        if isinstance(node, ast.Name)
    }
    residual762_names = {
        node.id
        for node in ast.walk(residual762)
        if isinstance(node, ast.Name)
    }
    declared758 = literal_assignment(
        trees[path758], "DECLARED_HIGH_K_FAMILY_REPRESENTATIVES"
    )
    declared759 = literal_assignment(
        trees[path759], "DECLARED_HIGH_K_FAMILY_REPRESENTATIVES"
    )
    supplied_choice_tokens = (
        "'name': 'terminal_horizon_index'",
        "'name': 'higher_k_family_epoch_scan_key'",
        "'name': 'horizon_extension'",
        "'name': 'monitored_selector_composition'",
        "'name': 'reference_disk_transport'",
        "'status': 'SUPPLIED'",
    )
    extract_source = ast.unparse(extract762)
    clean759_source = ast.unparse(clean759)
    result = {
        "landed_758_clean_arguments": function_arguments(clean758),
        "landed_759_residual_arguments": function_arguments(residual759),
        "landed_759_clean_arguments": function_arguments(clean759),
        "independent_762_residual_arguments":
            function_arguments(residual762),
        "landed_758_has_no_k_or_positions_input": not (
            forbidden_input_names & clean758_names
        ),
        "landed_759_has_no_k_or_positions_input": not (
            forbidden_input_names & residual759_names
        ),
        "independent_762_has_no_k_or_positions_input": not (
            forbidden_input_names & residual762_names
        ),
        "cycle758_declared_high_k_representatives": declared758,
        "cycle759_declared_high_k_representatives": declared759,
        "high_k_declarations_agree": declared758 == declared759
        == {
            3: ((0, 2, 4),),
            4: ((0, 2, 4, 6),),
            5: ((0, 2, 4, 6, 8),),
        },
        "cycle762_extracts_only_projection_functions": all(
            token in extract_source
            for token in (
                "names = ('watched_bank_registers', 'postimage_residual')",
                "selected = tuple((functions[name] for name in names))",
                "expected_roots",
            )
        ),
        "cycle762_primary_names_cycle759_path": literal_assignment(
            trees[path762], "PRIMARY_DATA_PATH"
        )
        == path759,
        "cycle759_clean_is_not_residual": (
            "return not postimage_residual(after, bank_count)"
            in clean759_source
        ),
        "wire_surface_agrees": (
            {
                token
                for token in attribute_tokens(residual759)
                if token.startswith("K.")
            }
            <= {
                token
                for token in attribute_tokens(clean758)
                if token.startswith("K.")
            }
            | {
                "K.M.unpack_state",
                "K.R3.X.SOURCE_POINTER",
            }
        ),
        "cycle798_all_supplied_choices_declared": all(
            token in main798_source for token in supplied_choice_tokens
        ),
        "scope": (
            "The predicate is k/source-position agnostic at the fixed "
            "two-bank fixture; it is not claimed to be bank-count agnostic. "
            "Cycle 758/759 already apply the same landed projection to "
            "declared k=3,4,5 translation families."
        ),
        "SUPPLIED_generalization": False,
        "silent_generalization": False,
    }
    result["pass"] = (
        result["landed_758_clean_arguments"] == ("after", "bank_count")
        and result["landed_759_residual_arguments"]
        == ("after", "bank_count")
        and result["landed_759_clean_arguments"]
        == ("after", "bank_count")
        and result["independent_762_residual_arguments"] == ("state",)
        and result["landed_758_has_no_k_or_positions_input"]
        and result["landed_759_has_no_k_or_positions_input"]
        and result["independent_762_has_no_k_or_positions_input"]
        and result["high_k_declarations_agree"]
        and result["cycle762_extracts_only_projection_functions"]
        and result["cycle762_primary_names_cycle759_path"]
        and result["cycle759_clean_is_not_residual"]
        and result["wire_surface_agrees"]
        and result["cycle798_all_supplied_choices_declared"]
        and not result["silent_generalization"]
    )
    return result


def independent_epoch_fixtures(
) -> tuple[tuple[int, tuple[int, int], tuple[object, ...], Any], ...]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append((event, direction, program, before))
        state = independent_gate_word(before, allocator)
    return tuple(rows)


def trace_initial_alternative(
    program: tuple[object, ...],
    before: Any,
    positions: tuple[int, ...],
    census_set: frozenset[tuple[int, ...]],
) -> dict[str, object]:
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    blank = (0,) * len(program)
    word = synchronous_word(program, positions)
    expected = independent_gate_word(before, word)
    after, rail_a, rail_b, trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    clean = landed_clean_postimage(after, FIXTURE_BANKS)
    support = residual_support(after)
    content_residual = postimage_residual(after, FIXTURE_BANKS)
    conditions = {
        "census_membership": positions in census_set,
        "pairwise_separation": pairwise_separated(positions),
        "synchronization":
            trace == expected_forward_trace(positions, len(program)),
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == blank,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": clean,
    }
    failed = tuple(
        name for name in EXPANDED_EXCLUSIONS if not conditions[name]
    )
    return {
        "positions": positions,
        "conditions": conditions,
        "failed_exclusions": failed,
        "selected": not failed,
        "clean_equals_empty_762_support": clean == (not support),
        "clean_equals_empty_759_content": clean == (not content_residual),
        "residual_weight": len(support),
    }


def outcome_class(selected: tuple[tuple[int, ...], ...]) -> str:
    if not selected:
        return "zero_survivors"
    if len(selected) == 1:
        return "unique_survivor"
    return "exact_tie"


def build_catalog() -> dict[str, object]:
    configurations = independent_configuration_census()
    families = independent_translation_families(configurations)
    fixtures = independent_epoch_fixtures()
    census_set = frozenset(
        positions
        for positions_rows in configurations.values()
        for positions in positions_rows
    )
    class_counts: dict[int, Counter[str]] = {
        k: Counter() for k in TARGET_STRATA
    }
    rows = []
    zero_rows = []
    expanded_failures: Counter[str] = Counter()
    residual_equivalence_failures = 0

    for k in TARGET_STRATA:
        for representative, alternatives in families[k].items():
            for event, direction, program, before in fixtures:
                evaluations = tuple(
                    trace_initial_alternative(
                        program, before, positions, census_set
                    )
                    for positions in alternatives
                )
                selected = tuple(
                    row["positions"]
                    for row in evaluations
                    if row["selected"]
                )
                classification = outcome_class(selected)
                class_counts[k][classification] += 1
                residual_equivalence_failures += sum(
                    not row["clean_equals_empty_762_support"]
                    or not row["clean_equals_empty_759_content"]
                    for row in evaluations
                )
                row = {
                    "k": k,
                    "representative": representative,
                    "event": event,
                    "direction": direction,
                    "alternative_count": len(alternatives),
                    "outcome_class": classification,
                    "selected": selected,
                }
                rows.append(row)
                if classification == "zero_survivors":
                    for evaluation in evaluations:
                        expanded_failures.update(
                            evaluation["failed_exclusions"]
                        )
                    zero_rows.append(
                        {
                            **row,
                            "all_alternatives_failed_only_clean": all(
                                evaluation["failed_exclusions"]
                                == ("clean_postimage",)
                                for evaluation in evaluations
                            ),
                            "initial_residual_weights": tuple(
                                evaluation["residual_weight"]
                                for evaluation in evaluations
                            ),
                        }
                    )

    configuration_counts = {
        k: len(configurations[k]) for k in range(6)
    }
    family_counts = {k: len(families[k]) for k in range(6)}
    normalized_class_counts = {
        k: {
            name: class_counts[k][name]
            for name in (
                "exact_tie",
                "unique_survivor",
                "zero_survivors",
            )
        }
        for k in TARGET_STRATA
    }
    zero_counts = dict(sorted(Counter(row["k"] for row in zero_rows).items()))
    public_surface = {
        "configuration_counts": configuration_counts,
        "family_counts": family_counts,
        "class_counts": normalized_class_counts,
        "zero_counts": zero_counts,
        "zero_keys": tuple(
            (row["k"], row["representative"], row["event"])
            for row in zero_rows
        ),
    }
    result = {
        "configurations": configurations,
        "families": families,
        "fixtures": fixtures,
        "rows": tuple(rows),
        "zero_rows": tuple(zero_rows),
        **public_surface,
        "expanded_failure_census":
            dict(sorted(expanded_failures.items())),
        "residual_equivalence_failures":
            residual_equivalence_failures,
        "catalog_sha256": digest(public_surface),
    }
    result["pass"] = (
        configuration_counts == EXPECTED_CONFIGURATION_COUNTS
        and family_counts == EXPECTED_FAMILY_COUNTS
        and normalized_class_counts == EXPECTED_CLASS_COUNTS
        and zero_counts == EXPECTED_ZERO_COUNTS
        and len(zero_rows) == 42
        and sum(row["alternative_count"] for row in zero_rows) == 42 * 11
        and result["expanded_failure_census"]
        == {"clean_postimage": 42 * 11}
        and residual_equivalence_failures == 0
        and all(
            row["all_alternatives_failed_only_clean"]
            and min(row["initial_residual_weights"]) > 0
            for row in zero_rows
        )
    )
    return result


def exact_controller_state_key(
    state: tuple[int, ...],
    positions: tuple[int, ...],
) -> bytes:
    tokens = tuple(
        int(station in positions) for station in range(RING_STATIONS)
    )
    blank = (0,) * RING_STATIONS
    packed = np.packbits(
        np.asarray(state, dtype=np.uint8), bitorder="little"
    ).tobytes()
    return (
        len(state).to_bytes(4, "little")
        + packed
        + bytes(tokens)
        + bytes(blank)
    )


def scan_key(
    event: int,
    direction: tuple[int, int],
    program: tuple[object, ...],
    before: Any,
    positions: tuple[int, ...],
    horizon_t: int,
) -> dict[str, object]:
    word = synchronous_word(program, positions)
    state = before
    seen: dict[bytes, int] = {}
    trace_sha = sha256()
    first_clean_t = None
    cycle_start_t = None
    cycle_period = None
    minimum_weight = None
    residual_equivalence_failures = 0
    nonclean_prefix_count = 0
    initial_composition_exact = False
    initial_rails_exact = False
    initial_synchronization_exact = False
    first_state_sha = None
    last_t = -1

    for horizon_index in range(horizon_t + 1):
        state = independent_gate_word(state, word)
        last_t = horizon_index
        clean = landed_clean_postimage(state, FIXTURE_BANKS)
        support = residual_support(state)
        content_residual = postimage_residual(state, FIXTURE_BANKS)
        residual_equivalence_failures += (
            clean != (not support)
            or clean != (not content_residual)
        )
        weight = len(support)
        minimum_weight = (
            weight
            if minimum_weight is None
            else min(minimum_weight, weight)
        )
        key = exact_controller_state_key(state, positions)
        trace_sha.update(horizon_index.to_bytes(4, "little"))
        trace_sha.update(len(key).to_bytes(4, "little"))
        trace_sha.update(key)
        trace_sha.update(weight.to_bytes(4, "little"))

        if horizon_index == 0:
            first_state_sha = sha256(key).hexdigest()
            direct, rail_a, rail_b, trace = K.run_orbit(
                before, program, token_positions=positions
            )
            expected_tokens = tuple(
                int(station in positions)
                for station in range(len(program))
            )
            initial_composition_exact = direct == state
            initial_rails_exact = (
                rail_a == expected_tokens and not any(rail_b)
            )
            initial_synchronization_exact = (
                trace
                == expected_forward_trace(positions, len(program))
            )

        if clean:
            first_clean_t = horizon_index
            break
        nonclean_prefix_count += 1
        if key in seen:
            cycle_start_t = seen[key]
            cycle_period = horizon_index - seen[key]
            break
        seen[key] = horizon_index

    if first_clean_t is not None:
        classification = "TRANSIENT_CLEAN"
    elif cycle_period is not None:
        classification = "CYCLE_CERTIFIED_NONZERO"
    else:
        classification = "OPEN"
    return {
        "event": event,
        "direction": direction,
        "positions": positions,
        "horizon_t": horizon_t,
        "classification": classification,
        "first_clean_t": first_clean_t,
        "nonclean_prefix_count": nonclean_prefix_count,
        "cycle_start_t": cycle_start_t,
        "cycle_period": cycle_period,
        "open_through_t":
            horizon_t if classification == "OPEN" else None,
        "last_evaluated_t": last_t,
        "minimum_residual_weight": minimum_weight,
        "initial_composition_exact": initial_composition_exact,
        "initial_rails_exact": initial_rails_exact,
        "initial_synchronization_exact":
            initial_synchronization_exact,
        "residual_equivalence_failures":
            residual_equivalence_failures,
        "initial_full_controller_state_sha256": first_state_sha,
        "trace_full_state_sha256": trace_sha.hexdigest(),
        "cycle_hash_granularity": (
            "exact np.packbits of all 5815 landed data bits plus both "
            "11-site controller rails at every complete-orbit boundary"
        ),
    }


def scan_catalog(
    catalog: dict[str, object],
    horizon_t: int,
) -> tuple[dict[str, object], ...]:
    fixture_by_event = {
        row[0]: row for row in catalog["fixtures"]
    }
    rows = []
    for zero_row in catalog["zero_rows"]:
        event = zero_row["event"]
        _event, direction, program, before = fixture_by_event[event]
        rows.append(
            {
                "k": zero_row["k"],
                "key": (
                    zero_row["k"],
                    zero_row["representative"],
                    event,
                ),
                **scan_key(
                    event,
                    direction,
                    program,
                    before,
                    zero_row["representative"],
                    horizon_t,
                ),
            }
        )
    return tuple(rows)


def direct_moment_check(
    fixture: tuple[int, tuple[int, int], tuple[object, ...], Any],
    positions: tuple[int, ...],
    moment: int,
) -> dict[str, object]:
    event, direction, program, before = fixture
    state = before
    pre_clean = None
    at_clean = None
    rails_exact = True
    synchronization_exact = True
    for horizon_index in range(moment + 1):
        state, rail_a, rail_b, trace = K.run_orbit(
            state, program, token_positions=positions
        )
        tokens = tuple(
            int(station in positions) for station in range(len(program))
        )
        rails_exact &= rail_a == tokens and not any(rail_b)
        synchronization_exact &= (
            trace == expected_forward_trace(positions, len(program))
        )
        if horizon_index == moment - 1:
            pre_clean = landed_clean_postimage(state, FIXTURE_BANKS)
        if horizon_index == moment:
            at_clean = landed_clean_postimage(state, FIXTURE_BANKS)
    return {
        "event": event,
        "direction": direction,
        "positions": positions,
        "moment": moment,
        "t_minus_1_clean": pre_clean,
        "t_clean": at_clean,
        "rails_exact_all_orbits": rails_exact,
        "synchronization_exact_all_orbits": synchronization_exact,
        "pass": (
            pre_clean is False
            and at_clean is True
            and rails_exact
            and synchronization_exact
        ),
    }


def reference_catalog_audit(
    trees: dict[str, ast.Module],
    catalog: dict[str, object],
) -> dict[str, object]:
    path784 = BLOCKLIST_TEXT_PATHS[6]
    path798 = BLOCKLIST_TEXT_PATHS[0]
    path787 = GIT_TEXT_REFERENCES["cycle787_primary"]["path"]
    tree784 = trees[path784]
    tree787 = trees[path787]
    tree798 = trees[path798]

    expected_identity787 = literal_assignment(
        tree787, "EXPECTED_IDENTITY"
    )
    zero_epochs787 = local_literal_assignment(
        tree787, "main", "expected_zero_family_epochs"
    )
    k5_expected = {
        "exact_tie": 0,
        "unique_survivor": 0,
        "zero_survivors": 4,
    }
    k5_literal_present = False
    for node in ast.walk(named_function(tree787, "main")):
        if not isinstance(node, ast.Dict):
            continue
        try:
            value = ast.literal_eval(node)
        except (ValueError, TypeError):
            continue
        if value == k5_expected:
            k5_literal_present = True
            break
    reference_classes = {
        3: {
            name: expected_identity787[3][name]
            for name in (
                "exact_tie",
                "unique_survivor",
                "zero_survivors",
            )
        },
        4: {
            name: expected_identity787[4][name]
            for name in (
                "exact_tie",
                "unique_survivor",
                "zero_survivors",
            )
        },
        5: k5_expected,
    }
    result = {
        "cycle784_configuration_counts": literal_assignment(
            tree784, "EXPECTED_COUNTS_BY_K"
        ),
        "cycle784_family_counts": literal_assignment(
            tree784, "EXPECTED_FAMILY_COUNTS_BY_K"
        ),
        "cycle787_configuration_counts": literal_assignment(
            tree787, "EXPECTED_CONFIGURATION_COUNTS"
        ),
        "cycle787_family_counts": literal_assignment(
            tree787, "EXPECTED_FAMILY_COUNTS"
        ),
        "cycle787_identity_k3_k4": expected_identity787,
        "cycle787_zero_family_epochs": zero_epochs787,
        "cycle787_k5_class_literal_present": k5_literal_present,
        "cycle798_class_counts": literal_assignment(
            tree798, "EXPECTED_CLASS_COUNTS"
        ),
        "cycle798_zero_counts": literal_assignment(
            tree798, "EXPECTED_ZERO_FAMILY_EPOCHS"
        ),
        "cycle798_k2_controls": literal_assignment(
            tree798, "EXPECTED_K2_TRANSIENTS"
        ),
        "reference_class_counts": reference_classes,
        "observed_class_counts": catalog["class_counts"],
    }
    result["pass"] = (
        result["cycle784_configuration_counts"] == {3: 77, 4: 55}
        and result["cycle784_family_counts"] == {3: 7, 4: 5}
        and result["cycle787_configuration_counts"]
        == EXPECTED_CONFIGURATION_COUNTS
        and result["cycle787_family_counts"] == EXPECTED_FAMILY_COUNTS
        and {
            int(k): v for k, v in zero_epochs787.items() if int(k) >= 3
        }
        == EXPECTED_ZERO_COUNTS
        and k5_literal_present
        and reference_classes == EXPECTED_CLASS_COUNTS
        and result["cycle798_class_counts"] == EXPECTED_CLASS_COUNTS
        and result["cycle798_zero_counts"] == EXPECTED_ZERO_COUNTS
        and result["cycle798_k2_controls"] == EXPECTED_K2_TRANSIENTS
        and catalog["class_counts"] == reference_classes
    )
    return result


def monitored_selection_window(
    catalog: dict[str, object],
) -> dict[str, object]:
    k, representative, event = CLAIMED_FIRST_KEY
    alternatives = catalog["families"][k][representative]
    fixture = next(
        row for row in catalog["fixtures"] if row[0] == event
    )
    _event, direction, program, before = fixture
    census_set = frozenset(catalog["configurations"][k])
    snapshots: dict[int, list[dict[str, object]]] = {
        horizon: [] for horizon in SELECTION_HORIZONS
    }

    for positions in alternatives:
        tokens = tuple(
            int(station in positions) for station in range(len(program))
        )
        blank = (0,) * len(program)
        word = synchronous_word(program, positions)
        inverse_word = tuple(reversed(word))
        direct_state = before
        independent_state = before
        composition_prefix_exact = True
        synchronization_prefix_exact = True
        rail_prefix_exact = True
        for horizon_index in range(max(SELECTION_HORIZONS) + 1):
            direct_state, rail_a, rail_b, trace = K.run_orbit(
                direct_state,
                program,
                token_positions=positions,
            )
            independent_state = independent_gate_word(
                independent_state, word
            )
            composition_prefix_exact &= (
                direct_state == independent_state
            )
            synchronization_prefix_exact &= (
                trace
                == expected_forward_trace(positions, len(program))
            )
            rail_prefix_exact &= (
                rail_a == tokens and rail_b == blank
            )
            if horizon_index not in snapshots:
                continue

            restored = direct_state
            for _orbit in range(horizon_index + 1):
                restored = independent_gate_word(
                    restored, inverse_word
                )
            clean = landed_clean_postimage(
                direct_state, FIXTURE_BANKS
            )
            support = residual_support(direct_state)
            content = postimage_residual(
                direct_state, FIXTURE_BANKS
            )
            conditions = {
                "census_membership": positions in census_set,
                "pairwise_separation":
                    pairwise_separated(positions),
                "synchronization":
                    synchronization_prefix_exact,
                "synchronous_composition":
                    composition_prefix_exact,
                "token_rail_return": rail_prefix_exact,
                "literal_inverse": restored == before,
                "clean_postimage": clean,
            }
            failed = tuple(
                name
                for name in EXPANDED_EXCLUSIONS
                if not conditions[name]
            )
            snapshots[horizon_index].append(
                {
                    "positions": positions,
                    "conditions": conditions,
                    "failed_exclusions": failed,
                    "selected": not failed,
                    "residual_weight": len(support),
                    "clean_equals_empty_762_support":
                        clean == (not support),
                    "clean_equals_empty_759_content":
                        clean == (not content),
                    "full_state_sha256": sha256(
                        exact_controller_state_key(
                            direct_state, positions
                        )
                    ).hexdigest(),
                }
            )

    horizons = {}
    for horizon, raw_rows in sorted(snapshots.items()):
        rows = tuple(raw_rows)
        survivors = tuple(
            row["positions"] for row in rows if row["selected"]
        )
        horizons[horizon] = {
            "horizon_t_SUPPLIED": horizon,
            "complete_orbits_applied": horizon + 1,
            "rows": rows,
            "survivors": survivors,
            "survivor_count": len(survivors),
            "all_residual_equivalences_exact": all(
                row["clean_equals_empty_762_support"]
                and row["clean_equals_empty_759_content"]
                for row in rows
            ),
        }

    t444 = horizons[444]
    exclusion_recount = {
        exclusion: {
            "pass_count": sum(
                row["conditions"][exclusion]
                for row in t444["rows"]
            ),
            "fail_count": sum(
                not row["conditions"][exclusion]
                for row in t444["rows"]
            ),
            "passing_positions": tuple(
                row["positions"]
                for row in t444["rows"]
                if row["conditions"][exclusion]
            ),
            "failing_positions": tuple(
                row["positions"]
                for row in t444["rows"]
                if not row["conditions"][exclusion]
            ),
        }
        for exclusion in EXPANDED_EXCLUSIONS
    }
    return {
        "key": CLAIMED_FIRST_KEY,
        "direction": direction,
        "alternative_count": len(alternatives),
        "horizons": horizons,
        "t444_exclusion_recount": exclusion_recount,
        "t443_veto": horizons[443]["survivor_count"] == 0,
        "t444_unique_representative": (
            t444["survivors"] == (representative,)
        ),
        "window_445_450": {
            horizon: {
                "survivors": horizons[horizon]["survivors"],
                "survivor_count": horizons[horizon][
                    "survivor_count"
                ],
            }
            for horizon in range(445, 451)
        },
        "pass": (
            len(alternatives) == 11
            and horizons[443]["survivor_count"] == 0
            and t444["survivors"] == (representative,)
            and all(
                horizons[horizon][
                    "all_residual_equivalences_exact"
                ]
                for horizon in SELECTION_HORIZONS
            )
            and all(
                all(
                    row["conditions"][exclusion]
                    for row in t444["rows"]
                )
                for exclusion in EXPANDED_EXCLUSIONS
                if exclusion != "clean_postimage"
            )
            and exclusion_recount["clean_postimage"]["pass_count"] == 1
            and exclusion_recount["clean_postimage"][
                "passing_positions"
            ] == (representative,)
        ),
    }


def classification_counts(
    rows: tuple[dict[str, object], ...],
) -> dict[int, dict[str, int]]:
    return {
        k: {
            name: sum(
                row["k"] == k and row["classification"] == name
                for row in rows
            )
            for name in (
                "TRANSIENT_CLEAN",
                "CYCLE_CERTIFIED_NONZERO",
                "OPEN",
            )
        }
        for k in TARGET_STRATA
    }


def public_catalog(catalog: dict[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in catalog.items()
        if key
        not in {
            "configurations",
            "families",
            "fixtures",
            "rows",
            "zero_rows",
        }
    }


def main() -> int:
    started = monotonic()

    controls, trees = source_controls()
    basis = residual_definition_audit(trees)
    catalog = build_catalog()
    reference_identity = reference_catalog_audit(trees, catalog)
    OUTPUT_LINES.append(
        "AUDIT_INPUT_PATHS_LITERAL " + repr(AUDIT_INPUT_PATHS)
    )
    OUTPUT_LINES.append("SOURCE_CONTROLS " + compact(controls))
    OUTPUT_LINES.append(
        "RESIDUAL_DEFINITION_AUDIT " + compact(basis)
    )
    OUTPUT_LINES.append(
        "CATALOG_SUMMARY " + compact(public_catalog(catalog))
    )
    OUTPUT_LINES.append(
        "REFERENCE_CATALOG_IDENTITY " + compact(reference_identity)
    )
    for row in catalog["zero_rows"]:
        OUTPUT_LINES.append(
            "CATALOG_ZERO_ROW "
            + compact(
                {
                    key: value
                    for key, value in row.items()
                    if key != "initial_residual_weights"
                }
            )
        )

    check(
        "CERTIFICATE_2_RESIDUAL_DEFINITION_LANDED_K_AGNOSTIC",
        basis["pass"],
        basis,
        (
            "SILENT_GENERALIZATION: the Cycle-798 cleanliness basis is not "
            "genuinely landed/k-agnostic or one of its supplied extensions "
            "is undeclared."
        ),
    )

    fixture_by_event = {
        row[0]: row for row in catalog["fixtures"]
    }
    k2_rows = []
    k2_direct_rows = []
    for event, positions, expected_t in EXPECTED_K2_TRANSIENTS:
        fixture = fixture_by_event[event]
        _event, direction, program, before = fixture
        row = scan_key(
            event,
            direction,
            program,
            before,
            positions,
            expected_t,
        )
        k2_rows.append(
            {"expected_first_clean_t": expected_t, **row}
        )
        k2_direct_rows.append(
            direct_moment_check(fixture, positions, expected_t)
        )
    k2_pass = (
        all(
            row["classification"] == "TRANSIENT_CLEAN"
            and row["first_clean_t"]
            == row["expected_first_clean_t"]
            and row["nonclean_prefix_count"]
            == row["expected_first_clean_t"]
            and row["minimum_residual_weight"] == 0
            and row["residual_equivalence_failures"] == 0
            and row["initial_composition_exact"]
            and row["initial_rails_exact"]
            and row["initial_synchronization_exact"]
            for row in k2_rows
        )
        and all(row["pass"] for row in k2_direct_rows)
    )
    OUTPUT_LINES.append(
        "K2_IDENTITY_CONTROLS "
        + compact(
            {
                "independent_scans": k2_rows,
                "direct_controller_recounts": k2_direct_rows,
            }
        )
    )

    first_scan = scan_catalog(catalog, SCAN_HORIZON_T)
    second_scan = scan_catalog(catalog, SCAN_HORIZON_T)
    first_scan_sha = digest(first_scan)
    second_scan_sha = digest(second_scan)
    deterministic = (
        first_scan == second_scan
        and first_scan_sha == second_scan_sha
    )
    for row in first_scan:
        OUTPUT_LINES.append("SCAN_ROW " + compact(row))

    counts = classification_counts(first_scan)
    transients = tuple(
        sorted(
            (
                row
                for row in first_scan
                if row["classification"] == "TRANSIENT_CLEAN"
            ),
            key=lambda row: (row["first_clean_t"], row["key"]),
        )
    )
    cycles = tuple(
        row
        for row in first_scan
        if row["classification"] == "CYCLE_CERTIFIED_NONZERO"
    )
    moments = tuple(row["first_clean_t"] for row in transients)
    transient_keys = tuple(row["key"] for row in transients)
    direct_transient_rows = tuple(
        direct_moment_check(
            fixture_by_event[row["event"]],
            row["positions"],
            row["first_clean_t"],
        )
        for row in transients
    )
    OUTPUT_LINES.append(
        "FOUR_MOMENT_DIRECT_RECOUNTS "
        + compact(direct_transient_rows)
    )
    expected_scan_counts = {
        3: {
            "TRANSIENT_CLEAN": 4,
            "CYCLE_CERTIFIED_NONZERO": 0,
            "OPEN": 14,
        },
        4: {
            "TRANSIENT_CLEAN": 0,
            "CYCLE_CERTIFIED_NONZERO": 0,
            "OPEN": 20,
        },
        5: {
            "TRANSIENT_CLEAN": 0,
            "CYCLE_CERTIFIED_NONZERO": 0,
            "OPEN": 4,
        },
    }
    scan_pass = (
        len(first_scan) == 42
        and moments == CLAIMED_TRANSIENT_MOMENTS
        and transient_keys[0] == CLAIMED_FIRST_KEY
        and not cycles
        and counts == expected_scan_counts
        and all(
            row["nonclean_prefix_count"] == row["first_clean_t"]
            and row["minimum_residual_weight"] == 0
            for row in transients
        )
        and all(row["pass"] for row in direct_transient_rows)
        and all(
            row["initial_composition_exact"]
            and row["initial_rails_exact"]
            and row["initial_synchronization_exact"]
            and row["residual_equivalence_failures"] == 0
            and (
                row["last_evaluated_t"] == SCAN_HORIZON_T
                if row["classification"] == "OPEN"
                else True
            )
            for row in first_scan
        )
    )
    check(
        "CERTIFICATE_1_FOUR_MOMENTS_AND_FULL_42_KEY_SWEEP",
        scan_pass,
        {
            "keys": len(first_scan),
            "horizon_t": SCAN_HORIZON_T,
            "moments": moments,
            "transient_keys": transient_keys,
            "classification_counts": counts,
            "cycle_certifications": tuple(
                {
                    "key": row["key"],
                    "cycle_start_t": row["cycle_start_t"],
                    "cycle_period": row["cycle_period"],
                }
                for row in cycles
            ),
            "scan_sha256": first_scan_sha,
            "direct_transient_recounts": direct_transient_rows,
        },
        (
            "MISSED_OR_SPURIOUS_SWEEP_OUTCOME: the exact full-state 42-key "
            "re-sweep disagrees with the four claimed moments, the zero-cycle "
            "claim, or the 14/20/4 open census."
        ),
    )

    selection = monitored_selection_window(catalog)
    OUTPUT_LINES.append(
        "T444_SELECTION_RECOUNT "
        + compact(
            {
                key: value
                for key, value in selection.items()
                if key != "horizons"
            }
        )
    )
    for horizon, row in selection["horizons"].items():
        OUTPUT_LINES.append(
            "SELECTION_WINDOW_ROW "
            + compact(
                {
                    "horizon_t_SUPPLIED": horizon,
                    "complete_orbits_applied":
                        row["complete_orbits_applied"],
                    "survivors": row["survivors"],
                    "survivor_count": row["survivor_count"],
                    "rows": row["rows"],
                }
            )
        )
    for exclusion in EXPANDED_EXCLUSIONS:
        row = selection["t444_exclusion_recount"][exclusion]
        expected = (
            row["pass_count"] == 1
            and row["passing_positions"] == ((0, 2, 5),)
            if exclusion == "clean_postimage"
            else row["pass_count"] == 11
            and row["fail_count"] == 0
        )
        check(
            "CERTIFICATE_3_EXCLUSION_" + exclusion.upper(),
            expected,
            row,
            (
                "T444_EXCLUSION_RECOUNT_MISMATCH: exclusion "
                f"{exclusion} does not have the required complete-family "
                "truth table at t=444."
            ),
        )
    check(
        "CERTIFICATE_3_T444_UNIQUE_SELECTION_T443_VETO_AND_WINDOW",
        selection["pass"],
        {
            "key": selection["key"],
            "t443_survivors":
                selection["horizons"][443]["survivors"],
            "t444_survivors":
                selection["horizons"][444]["survivors"],
            "window_445_450": selection["window_445_450"],
        },
        (
            "NON_UNIQUE_SELECTION: the complete 11-member (0,2,5) family "
            "does not veto at t=443 and select exactly (0,2,5) at t=444."
        ),
    )

    catalog_identity_pass = (
        catalog["pass"]
        and reference_identity["pass"]
        and k2_pass
    )
    check(
        "CERTIFICATE_4_CATALOG_784_787_IDENTITY_AND_K2_CONTROLS",
        catalog_identity_pass,
        {
            "catalog_pass": catalog["pass"],
            "reference_identity_pass": reference_identity["pass"],
            "configuration_counts": catalog["configuration_counts"],
            "family_counts": catalog["family_counts"],
            "class_counts": catalog["class_counts"],
            "zero_counts": catalog["zero_counts"],
            "catalog_sha256": catalog["catalog_sha256"],
            "k2_controls_pass": k2_pass,
            "k2_first_clean_t": tuple(
                row["first_clean_t"] for row in k2_rows
            ),
        },
        (
            "CATALOG_OR_CONTROL_IDENTITY_MISMATCH: the independent catalog "
            "does not reproduce the Cycle-784/787 18/20/4 zero classes or "
            "the k=2 252/371 first-clean controls."
        ),
    )

    elapsed = monotonic() - started
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 24 * 1024
    )
    certificate_5 = (
        controls["pass"]
        and deterministic
        and first_scan_sha == second_scan_sha
        and k2_pass
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_5_SHA_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT",
        certificate_5,
        {
            "source_controls_pass": controls["pass"],
            "blocked_runtime_modules":
                controls["blocked_runtime_modules"],
            "firewall_hits": controls["firewall_hits"],
            "deterministic": deterministic,
            "first_scan_sha256": first_scan_sha,
            "second_scan_sha256": second_scan_sha,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
        (
            "CONTROL_FAILURE: a SHA anchor, import blocklist, determinism, "
            "runtime, or stdout bound failed."
        ),
    )

    passed = all(CHECKS.values()) and not FINDINGS
    OUTPUT_LINES.append("FINDINGS_VERBATIM " + compact(tuple(FINDINGS)))
    terminal = {
        "terminal": (
            "CYCLE798_HIGHER_K_INDEPENDENT_CHECK_PASS"
            if passed
            else "CYCLE798_HIGHER_K_INDEPENDENT_CHECK_REFUTES_PRIMARY"
        ),
        "pass": passed,
        "four_moments_verified": moments,
        "classification_counts": counts,
        "t443_survivors": selection["horizons"][443]["survivors"],
        "t444_survivors": selection["horizons"][444]["survivors"],
        "window_445_450": selection["window_445_450"],
        "determinism_sha256": first_scan_sha,
        "runtime_seconds": round(elapsed, 6),
        "findings": tuple(FINDINGS),
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    stdout_bytes = len(output.encode("utf-8"))
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", stdout_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
