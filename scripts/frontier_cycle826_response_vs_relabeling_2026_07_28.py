#!/usr/bin/env python3
"""Cycle 826: response surface versus the Cycle-805 relabeling group.

The Cycle-805/808/821 primaries and the six landed W7 sources are SHA-pinned,
text/AST-only inputs.  This runner never imports or executes them.  It
reimplements the 27 primary-bank relabeling cases and the exact W7 response.

The central type check is deliberately explicit.  Cycle 805/808 moves
controller station, physical-track, Q-traversal, and sometimes layer-slot
labels while fixing bank, epoch, occurrence direction, orientation, and the
constructor data state.  W7 consumes a separate ordered six-column direction
family and its six allocation weights.  There is no source-side map from an
805 moved domain to either W7 object, so every induced W7 action is identity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
BASE_HEAD_SHA = "37c7afd1837dc68de4e9686910e74c18a7391c4b"
EXPECTED_BRANCH = "physics-loop/proof-grade-blockP14-20260729"

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle808_uniformity_from_relabeling_2026_07_28.py",
    "scripts/frontier_cycle821_orbit_observability_2026_07_28.py",
    "scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "scripts/frontier_cycle812_mixed_input_response_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[1]:
        "d3ccc94cf4d43da9fc8e737ca2706706cdffccb1e963bb8381d6db2350fefcea",
    AUDIT_INPUT_PATHS[2]:
        "36273e2f13c26803d7a28bb65a3efce0aab82c766e4dc039d8269f0d53973342",
    AUDIT_INPUT_PATHS[3]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[4]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[5]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[6]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[7]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    AUDIT_INPUT_PATHS[8]:
        "fe35718b8f5e84cfafed74026a5634e722da757782f04d536a756d7273d3ee9b",
}
EXPECTED_GIT_BLOB_SHA1 = {
    AUDIT_INPUT_PATHS[0]: "075659d59588f7895e91f50f9ef93a368fb1fb4e",
    AUDIT_INPUT_PATHS[1]: "a79ef29be8f8c4b50ed7fc98cd4879b4e3d34524",
    AUDIT_INPUT_PATHS[2]: "fff1b6267ebdafa88f267600988705549297957b",
    AUDIT_INPUT_PATHS[3]: "cee674584704dd7d351cb2ffa947c74bee47d06e",
    AUDIT_INPUT_PATHS[4]: "0070722d7a12d47658346b6c812edd05424ae592",
    AUDIT_INPUT_PATHS[5]: "52abfe3dd54b3969f51ca6816ec4830b42405106",
    AUDIT_INPUT_PATHS[6]: "6bde2222ddfdaf48e3806c0ac0a9c9d6431d945f",
    AUDIT_INPUT_PATHS[7]: "8366a5240d992376d0396a6fdc2c0b33247e8aba",
    AUDIT_INPUT_PATHS[8]: "39b5f24595f2271704bf68197103b62824a14cbf",
}

from dataclasses import dataclass
import ast
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import importlib.util
from itertools import combinations
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
STDOUT_BYTES = 0
CHECKS: dict[str, bool] = {}
PRIMARY_PATHS = AUDIT_INPUT_PATHS[:3]
W7_PATHS = AUDIT_INPUT_PATHS[3:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _SourceBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST text/AST-only source: {fullname}")
        return None


SOURCE_BLOCKER = _SourceBlocker()
sys.meta_path.insert(0, SOURCE_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(*parts: object) -> None:
    global STDOUT_BYTES
    line = " ".join(str(part) for part in parts)
    encoded = (line + "\n").encode("utf-8")
    STDOUT_BYTES += len(encoded)
    if STDOUT_BYTES >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit exceeded", STDOUT_BYTES))
    print(line)


def check(label: str, condition: bool, detail: object) -> bool:
    CHECKS[label] = bool(condition)
    emit(
        "CERTIFICATE",
        label,
        "PASS" if condition else "FAIL",
        compact(detail),
    )
    return bool(condition)


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = tuple(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(rows) != 1:
        raise AssertionError(("function multiplicity", name, len(rows)))
    return rows[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    rows = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            rows.append(node.value)
    if len(rows) != 1 or rows[0] is None:
        raise AssertionError(("assignment multiplicity", name, len(rows)))
    return ast.literal_eval(rows[0])


def literal_self_paths() -> tuple[str, ...]:
    tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    return tuple(literal_assignment(tree, "AUDIT_INPUT_PATHS"))


def subprocess_text(*command: str) -> str:
    return subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def source_controls(
    input_bytes: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    observed_sha256 = {
        path: sha256(data).hexdigest() for path, data in input_bytes.items()
    }
    observed_blobs = {
        path: git_blob_sha1(data) for path, data in input_bytes.items()
    }
    blocked_attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            importlib.util.find_spec(module)
        except ImportError as error:
            blocked_attempts[module] = str(error)
        else:
            blocked_attempts[module] = "NOT_BLOCKED"

    own_tree = ast.parse(Path(__file__).read_bytes(), filename=__file__)
    imported = {
        alias.name.rsplit(".", 1)[-1]
        for node in ast.walk(own_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        str(node.module).rsplit(".", 1)[-1]
        for node in ast.walk(own_tree)
        if isinstance(node, ast.ImportFrom)
    }
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", BASE_HEAD_SHA, "HEAD"),
        cwd=ROOT,
        check=False,
        capture_output=True,
    ).returncode == 0
    return {
        "head_sha": subprocess_text("git", "rev-parse", "HEAD"),
        "branch": subprocess_text("git", "branch", "--show-current"),
        "base_is_ancestor": base_is_ancestor,
        "literal_paths": literal_self_paths(),
        "paths_worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "parsed_source_count": len(trees),
        "sha256": observed_sha256,
        "git_blob_sha1": observed_blobs,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "git_blob_match": observed_blobs == EXPECTED_GIT_BLOB_SHA1,
        "blocked_attempts": blocked_attempts,
        "blocklist_pass": all(
            text.startswith("BLOCKLIST text/AST-only source:")
            for text in blocked_attempts.values()
        ),
        "none_loaded": all(
            module not in sys.modules for module in BLOCKLISTED_MODULES
        ),
        "no_blocklisted_AST_import": not (
            set(BLOCKLISTED_MODULES) & imported
        ),
    }


@dataclass(frozen=True)
class GeneratorSpec:
    name: str
    supply: str
    choice: str
    rotation: int
    layer_order: str
    order_mode: str


GENERATOR_SPECS = (
    GeneratorSpec(
        "I1_SOURCE_1", "inherited_1", "source_index=1",
        -1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I1_SOURCE_LAST", "inherited_1", "source_index=stations-1",
        1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I2_ROTATE_1", "inherited_2", "left_rotation=1",
        1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I2_ROTATE_LAST", "inherited_2", "left_rotation=stations-1",
        -1, "Q_then_R", "ascending",
    ),
    GeneratorSpec(
        "I3_Q_THEN_R_DESCENDING", "inherited_3",
        "layers=Q_then_R;Q_order=descending",
        0, "Q_then_R", "descending",
    ),
    GeneratorSpec(
        "I3_Q_THEN_R_EVEN_THEN_ODD", "inherited_3",
        "layers=Q_then_R;Q_order=even_then_odd",
        0, "Q_then_R", "even_then_odd",
    ),
    GeneratorSpec(
        "I3_R_THEN_Q_ASCENDING", "inherited_3",
        "layers=R_then_Q;Q_order=ascending",
        0, "R_then_Q", "ascending",
    ),
    GeneratorSpec(
        "I3_R_THEN_Q_DESCENDING", "inherited_3",
        "layers=R_then_Q;Q_order=descending",
        0, "R_then_Q", "descending",
    ),
    GeneratorSpec(
        "I3_R_THEN_Q_EVEN_THEN_ODD", "inherited_3",
        "layers=R_then_Q;Q_order=even_then_odd",
        0, "R_then_Q", "even_then_odd",
    ),
)
BANK_STATIONS = ((1, 3), (2, 11), (3, 19))


def q_positions(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        order = tuple(range(stations))
    elif mode == "descending":
        order = tuple(reversed(range(stations)))
    elif mode == "even_then_odd":
        order = (
            tuple(range(0, stations, 2))
            + tuple(range(1, stations, 2))
        )
    else:
        raise ValueError(mode)
    positions = [0] * stations
    for slot, station in enumerate(order):
        positions[station] = slot
    return tuple(positions)


def action_row(
    spec: GeneratorSpec,
    bank: int,
    stations: int,
) -> dict[str, object]:
    rotation = spec.rotation % stations
    phase = int(spec.layer_order == "R_then_Q")
    station_shift = (-spec.rotation - phase) % stations
    station_map = tuple(
        (station + station_shift) % stations
        for station in range(stations)
    )
    q_position = q_positions(stations, spec.order_mode)
    q_slots = tuple(
        q_position[(station - rotation) % stations]
        for station in range(stations)
    )
    return {
        "case": f"{spec.name}@bank={bank}",
        "generator": spec.name,
        "supply": spec.supply,
        "choice": spec.choice,
        "bank": bank,
        "stations": stations,
        "occurrence_action": {
            "station_shift": station_shift,
            "station_map": station_map,
            "physical_track_site_map": tuple(
                2 * ((site // 2 + station_shift) % stations) + site % 2
                for site in range(2 * stations)
            ),
            "q_traversal_slot_map": q_slots,
            "layer_slot_map": (phase, 1 ^ phase),
            "logical_bank": "FIXED",
            "epoch": "FIXED",
            "occurrence_direction": "FIXED",
            "orientation": "FIXED",
            "constructor_data_state": "IDENTITY",
        },
        "w7_input_action": "IDENTITY_NO_REACH",
        "w7_fixed_objects": (
            "six direction-column labels",
            "six allocation weights",
            "fixed response rows",
            "normalized diagonal LinkState weights",
        ),
        "reason": (
            "805/808 maps only station/track/Q/layer labels; no map targets "
            "a W7 direction column, allocation weight, response row, or "
            "LinkState coordinate"
        ),
    }


def main() -> int:
    input_bytes = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(data, filename=path)
        for path, data in input_bytes.items()
    }
    controls = source_controls(input_bytes, trees)
    actions = tuple(
        action_row(spec, bank, stations)
        for spec in GENERATOR_SPECS
        for bank, stations in BANK_STATIONS
    )
    emit("CYCLE", 826, "RESPONSE_VS_RELABELING")
    emit("HEAD_SHA", controls["head_sha"])
    emit("BRANCH", controls["branch"])
    for path in AUDIT_INPUT_PATHS:
        emit(
            "SOURCE_SHA",
            path,
            controls["sha256"][path],
            controls["git_blob_sha1"][path],
        )
    for action in actions:
        emit(
            "GENERATOR_ACTION",
            compact(
                {
                    "case": action["case"],
                    "choice": action["choice"],
                    "station_shift":
                        action["occurrence_action"]["station_shift"],
                    "layer_slot_map":
                        action["occurrence_action"]["layer_slot_map"],
                    "q_traversal_slot_map_sha256": digest(
                        action["occurrence_action"][
                            "q_traversal_slot_map"
                        ]
                    ),
                    "w7_input_action": action["w7_input_action"],
                    "reason": action["reason"],
                }
            ),
        )
    check(
        "SCAFFOLD_SOURCE_CONTROLS",
        (
            controls["literal_paths"] == AUDIT_INPUT_PATHS
            and controls["paths_worktree_relative"]
            and controls["all_paths_exist"]
            and controls["parsed_source_count"] == len(AUDIT_INPUT_PATHS)
            and controls["sha256_match"]
            and controls["git_blob_match"]
            and controls["blocklist_pass"]
            and controls["none_loaded"]
            and controls["no_blocklisted_AST_import"]
            and controls["branch"] == EXPECTED_BRANCH
            and controls["base_is_ancestor"]
            and len(actions) == 27
        ),
        controls,
    )
    elapsed = monotonic() - START
    emit("SCAFFOLD_ACTION_COUNT", len(actions))
    emit("RUNTIME_SECONDS", f"{elapsed:.6f}")
    emit("STDOUT_BYTES", STDOUT_BYTES)
    emit("PASS" if all(CHECKS.values()) else "FAIL")
    return 0 if all(CHECKS.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
