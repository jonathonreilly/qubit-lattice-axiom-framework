#!/usr/bin/env python3
"""Cycle 790 adversarial checker: attack the reimplementation and t=252.

The Cycle-790 primary is read only as text/AST data and is never imported or
executed.  The exact Cycle-762 cleanliness test is extracted from its anchored
historical checker, while all continuation, recurrence hashing, horizon
classification, and event accounting are implemented independently here.

This finite checker does not decide whether residual support is physical
content or dirt.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


LINEAGE_COMMIT = "67b4ac37b875fb5e6f46aee8d2a1c42b00be5be5"
CYCLE762_PRIMARY_PATH = (
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py"
)
CYCLE762_CHECKER_PATH = (
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py"
)
PRIMARY_TEXT_PATH = (
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py"
)
PRIMARY_MODULE_NAME = (
    "frontier_cycle790_horizon_extension_2026_07_28"
)
IMPORT_BLOCKLIST = (PRIMARY_MODULE_NAME,)

EXPECTED_SHA256 = {
    CYCLE762_PRIMARY_PATH:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    CYCLE762_CHECKER_PATH:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    AUDIT_INPUT_PATHS[0]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_BLOBS = {
    CYCLE762_PRIMARY_PATH: "87ba84671c246fe3b7473980d395ea94443921fc",
    CYCLE762_CHECKER_PATH: "3eff0f787a12cacf504324209f578f0c1df91c90",
}

RING_STATIONS = 11
FIXTURE_BANKS = 2
HORIZONS = (64, 128, 256)
LANDED_ORBIT_LENGTH = 130
LANDED_BANK_COUNTS = (2, 5, 12)
HEADLINE_KEY = (3, (1, 10))
HEADLINE_TIME = 252
STDOUT_LIMIT_BYTES = 150 * 1024
PHYSICAL_SCOPE = "CONTENT_VS_DIRT_REMAINS_OPEN"

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []

Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(rows: object) -> str:
    return sha256(compact(rows).encode("utf-8")).hexdigest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label}")
    return passed


def data(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"DATA {label} {compact(value)}")


def git_output(*args: str, text: bool = False) -> bytes | str:
    completed = subprocess.run(
        ("git",) + args,
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=text,
    )
    return completed.stdout


def historical_bytes(path: str) -> tuple[bytes, str]:
    local = ROOT / path
    if local.is_file():
        return local.read_bytes(), "working_tree"
    payload = git_output("show", f"{LINEAGE_COMMIT}:{path}")
    if not isinstance(payload, bytes):
        raise AssertionError(("historical bytes were text", path))
    return payload, f"git:{LINEAGE_COMMIT}"


def historical_blob(path: str) -> str:
    result = git_output(
        "rev-parse", f"{LINEAGE_COMMIT}:{path}", text=True
    )
    if not isinstance(result, str):
        raise AssertionError(("blob id was bytes", path))
    return result.strip()


def canonical_support(row: Support) -> tuple[Coordinate, ...]:
    return tuple(sorted(row))


def framed_update(hasher: object, *parts: bytes) -> None:
    for part in parts:
        hasher.update(len(part).to_bytes(8, "big"))
        hasher.update(part)


def state_bytes(state: tuple[int, ...]) -> bytes:
    if any(bit not in (0, 1) for bit in state):
        raise AssertionError("nonbinary state")
    return bytes(state)


def support_bytes(row: Support) -> bytes:
    return compact(canonical_support(row)).encode("utf-8")


def literal_assignment(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(ast.literal_eval(node.value))
    if len(matches) != 1:
        raise AssertionError(("literal assignment", name, len(matches)))
    return matches[0]


def top_level_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def normalized_function(node: ast.FunctionDef) -> str:
    copied = deepcopy(node)
    if (
        copied.body
        and isinstance(copied.body[0], ast.Expr)
        and isinstance(copied.body[0].value, ast.Constant)
        and isinstance(copied.body[0].value.value, str)
    ):
        copied.body.pop(0)
    ast.fix_missing_locations(copied)
    return ast.dump(copied, include_attributes=False)


class BuildFamilyNormalizer(ast.NodeTransformer):
    """Remove only Cycle-790's non-dynamical build-family instrumentation."""

    REMOVED_KEYS = {
        "bank_register_widths",
        "link_register_widths",
        "runtime_seconds",
    }
    RENAMES = {"banks0": "banks", "links0": "links"}

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id in self.RENAMES:
            node.id = self.RENAMES[node.id]
        return node

    def visit_Assign(self, node: ast.Assign) -> ast.AST | None:
        if (
            len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "started"
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "monotonic"
        ):
            return None
        return self.generic_visit(node)

    def visit_Dict(self, node: ast.Dict) -> ast.AST:
        kept = [
            (key, value)
            for key, value in zip(node.keys, node.values)
            if not (
                isinstance(key, ast.Constant)
                and key.value in self.REMOVED_KEYS
            )
        ]
        node.keys = [key for key, _value in kept]
        node.values = [value for _key, value in kept]
        return self.generic_visit(node)


def normalized_build_family(node: ast.FunctionDef) -> str:
    copied = BuildFamilyNormalizer().visit(deepcopy(node))
    if not isinstance(copied, ast.FunctionDef):
        raise AssertionError("build_family normalizer removed function")
    return normalized_function(copied)


def source_and_blocklist_certificate() -> dict[str, object]:
    source_payloads = {}
    source_modes = {}
    actual_sha256 = {}
    for path in (CYCLE762_PRIMARY_PATH, CYCLE762_CHECKER_PATH):
        payload, mode = historical_bytes(path)
        source_payloads[path] = payload
        source_modes[path] = mode
        actual_sha256[path] = sha256(payload).hexdigest()
    for path in AUDIT_INPUT_PATHS:
        payload = (ROOT / path).read_bytes()
        source_payloads[path] = payload
        source_modes[path] = "working_tree_import"
        actual_sha256[path] = sha256(payload).hexdigest()

    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source, filename=Path(__file__).name)
    header = None
    header_literal = False
    for node in own_tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            header_literal = (
                isinstance(node.value, ast.Tuple)
                and all(
                    isinstance(element, ast.Constant)
                    and isinstance(element.value, str)
                    for element in node.value.elts
                )
            )
            if header_literal:
                header = ast.literal_eval(node.value)

    imported_modules = []
    for node in ast.walk(own_tree):
        if isinstance(node, ast.Import):
            imported_modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.append(node.module)
    blocklist_hits = tuple(
        name
        for name in imported_modules
        if any(
            name == blocked or name.startswith(blocked + ".")
            for blocked in IMPORT_BLOCKLIST
        )
    )
    expected_import_modules = {
        Path(path).stem for path in AUDIT_INPUT_PATHS
    }
    actual_landed_import_modules = {
        name for name in imported_modules
        if name.startswith("frontier_")
    }
    tracked_inputs = {}
    for path in AUDIT_INPUT_PATHS:
        completed = subprocess.run(
            ("git", "ls-files", "--error-unmatch", path),
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        tracked_inputs[path] = (
            completed.returncode == 0
            and completed.stdout.strip() == path
        )

    blob_ids = {
        path: historical_blob(path)
        for path in (CYCLE762_PRIMARY_PATH, CYCLE762_CHECKER_PATH)
    }
    import_locations = {
        AUDIT_INPUT_PATHS[0]: str(Path(M736.__file__).resolve()),
        AUDIT_INPUT_PATHS[1]: str(Path(K.__file__).resolve()),
    }
    expected_locations = {
        path: str((ROOT / path).resolve()) for path in AUDIT_INPUT_PATHS
    }
    primary_path = ROOT / PRIMARY_TEXT_PATH
    primary_source = primary_path.read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_source, filename=PRIMARY_TEXT_PATH)
    result = {
        "lineage_commit": LINEAGE_COMMIT,
        "cycle762_source_modes": {
            path: source_modes[path]
            for path in (CYCLE762_PRIMARY_PATH, CYCLE762_CHECKER_PATH)
        },
        "actual_sha256": actual_sha256,
        "expected_sha256": EXPECTED_SHA256,
        "cycle762_blob_ids": blob_ids,
        "expected_cycle762_blob_ids": EXPECTED_BLOBS,
        "tracked_import_paths": tracked_inputs,
        "import_locations": import_locations,
        "expected_import_locations": expected_locations,
        "AUDIT_INPUT_PATHS_is_literal_tuple": header_literal,
        "AUDIT_INPUT_PATHS_value": header,
        "landed_import_modules": tuple(sorted(actual_landed_import_modules)),
        "expected_landed_import_modules":
            tuple(sorted(expected_import_modules)),
        "primary_text_path": PRIMARY_TEXT_PATH,
        "primary_text_sha256":
            sha256(primary_source.encode("utf-8")).hexdigest(),
        "primary_parsed_as_AST": isinstance(primary_tree, ast.Module),
        "primary_blocklist": IMPORT_BLOCKLIST,
        "primary_import_hits": blocklist_hits,
        "primary_in_sys_modules": PRIMARY_MODULE_NAME in sys.modules,
        "physical_question": PHYSICAL_SCOPE,
    }
    result["pass"] = (
        actual_sha256 == EXPECTED_SHA256
        and blob_ids == EXPECTED_BLOBS
        and all(tracked_inputs.values())
        and import_locations == expected_locations
        and header_literal
        and header == AUDIT_INPUT_PATHS
        and actual_landed_import_modules == expected_import_modules
        and not blocklist_hits
        and PRIMARY_MODULE_NAME not in sys.modules
        and result["primary_parsed_as_AST"]
        and result["physical_question"] == PHYSICAL_SCOPE
    )
    return {
        "result": result,
        "cycle762_checker_source":
            source_payloads[CYCLE762_CHECKER_PATH].decode("utf-8"),
        "primary_source": primary_source,
    }


def extract_landed_machinery(
    checker_source: str,
) -> tuple[dict[str, object], dict[str, object]]:
    """Compile only exact selected functions from the landed Cycle-762 checker."""

    tree = ast.parse(checker_source, filename=CYCLE762_CHECKER_PATH)
    functions = top_level_functions(tree)
    selected_names = (
        "separated_k2_positions",
        "synchronous_word",
        "watched_bank_registers",
        "residual_support",
        "canonical_support",
        "build_family",
    )
    selected = [deepcopy(functions[name]) for name in selected_names]
    future = ast.ImportFrom(
        module="__future__",
        names=[ast.alias(name="annotations")],
        level=0,
    )
    isolated = ast.Module(body=[future, *selected], type_ignores=[])
    ast.fix_missing_locations(isolated)
    namespace: dict[str, object] = {
        "K": K,
        "M736": M736,
        "combinations": combinations,
        "monotonic": monotonic,
        "digest_rows": digest_rows,
        "RING_STATIONS": RING_STATIONS,
        "FIXTURE_BANKS": FIXTURE_BANKS,
    }
    exec(
        compile(isolated, CYCLE762_CHECKER_PATH, "exec"),
        namespace,
        namespace,
    )
    extracted = {name: namespace[name] for name in selected_names}
    audit = {
        "source_path": CYCLE762_CHECKER_PATH,
        "source_sha256":
            sha256(checker_source.encode("utf-8")).hexdigest(),
        "selected_functions": selected_names,
        "selected_AST_sha256": {
            name: sha256(
                ast.dump(functions[name], include_attributes=False).encode(
                    "utf-8"
                )
            ).hexdigest()
            for name in selected_names
        },
        "cycle790_primary_imported": PRIMARY_MODULE_NAME in sys.modules,
        "physical_question": PHYSICAL_SCOPE,
    }
    audit["pass"] = (
        audit["source_sha256"] == EXPECTED_SHA256[CYCLE762_CHECKER_PATH]
        and set(extracted) == set(selected_names)
        and PRIMARY_MODULE_NAME not in sys.modules
        and audit["physical_question"] == PHYSICAL_SCOPE
    )
    return extracted, audit


def reimplementation_ast_attack(
    checker_source: str,
    primary_source: str,
) -> dict[str, object]:
    landed_tree = ast.parse(
        checker_source, filename=CYCLE762_CHECKER_PATH
    )
    primary_tree = ast.parse(primary_source, filename=PRIMARY_TEXT_PATH)
    landed = top_level_functions(landed_tree)
    primary = top_level_functions(primary_tree)
    exact_core_names = (
        "separated_k2_positions",
        "synchronous_word",
        "watched_bank_registers",
        "residual_support",
        "canonical_support",
    )
    core_agreement = {
        name: normalized_function(landed[name])
        == normalized_function(primary[name])
        for name in exact_core_names
    }
    build_family_agrees = (
        normalized_function(landed["build_family"])
        == normalized_build_family(primary["build_family"])
    )
    expected_t64_digest = literal_assignment(
        primary_tree, "EXPECTED_T64_CLASSIFICATION_SHA256"
    )
    horizons = literal_assignment(primary_tree, "HORIZONS")
    lineage = literal_assignment(primary_tree, "LINEAGE_COMMIT")
    primary_imports = []
    for node in ast.walk(primary_tree):
        if isinstance(node, ast.Import):
            primary_imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            primary_imports.append(node.module)
    result = {
        "comparison":
            "normalized AST; docstrings removed, build_family timing/width "
            "instrumentation removed and banks0/links0 alpha-renamed",
        "exact_core_function_agreement": core_agreement,
        "build_family_dynamics_agree": build_family_agrees,
        "primary_expected_T64_classification_sha256":
            expected_t64_digest,
        "primary_horizons": horizons,
        "primary_lineage_commit": lineage,
        "primary_imports": tuple(primary_imports),
        "primary_imported": PRIMARY_MODULE_NAME in sys.modules,
        "physical_question": PHYSICAL_SCOPE,
    }
    result["static_pass"] = (
        all(core_agreement.values())
        and build_family_agrees
        and isinstance(expected_t64_digest, str)
        and len(expected_t64_digest) == 64
        and horizons == HORIZONS
        and lineage == LINEAGE_COMMIT
        and PRIMARY_MODULE_NAME not in sys.modules
        and result["physical_question"] == PHYSICAL_SCOPE
    )
    return result


def independent_residual_support(state: tuple[int, ...]) -> Support:
    """Second direct projection, independent of the AST-extracted landed test."""

    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    result: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        result.add(("source", "SOURCE_POINTER", 0))
    watched = (
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
    for bank_index, bank in enumerate(banks):
        for register, wire in watched:
            if bank[wire]:
                result.add(("bank", register, bank_index))
    for link_index, link in enumerate(links):
        for wire, content in enumerate(link):
            if content:
                result.add(("link", f"WIRE_{wire}", link_index))
    return frozenset(result)


def least_phase_period(phases: tuple[Support, ...]) -> int:
    for candidate in range(1, len(phases) + 1):
        if len(phases) % candidate:
            continue
        if all(
            phases[index] == phases[index % candidate]
            for index in range(len(phases))
        ):
            return candidate
    raise AssertionError(("no phase period", len(phases)))


def horizon_status(record: dict[str, object], horizon: int) -> str:
    first_clean = record["first_clean"]
    if first_clean is not None and first_clean <= horizon:
        return f"FIRST_CLEAN(t={first_clean})"
    closure = record["cycle_closure"]
    if closure is not None and closure <= horizon:
        return (
            f"CYCLE(period={record['residual_period']},"
            f"entry={record['cycle_start']},"
            f"state_period={record['state_period']},closure={closure})"
        )
    return f"OPEN(no_clean_or_certified_cycle_through_T={horizon})"


def snapshot(
    records: dict[Key, dict[str, object]], horizon: int
) -> dict[str, object]:
    clean = []
    cycles = []
    open_keys = []
    for key in sorted(records):
        record = records[key]
        first_clean = record["first_clean"]
        closure = record["cycle_closure"]
        if first_clean is not None and first_clean <= horizon:
            clean.append(key)
        elif closure is not None and closure <= horizon:
            cycles.append(key)
        else:
            open_keys.append(key)
    return {
        "horizon": horizon,
        "keys": len(records),
        "clean_count": len(clean),
        "first_clean_time_census": dict(
            sorted(Counter(records[key]["first_clean"] for key in clean).items())
        ),
        "cycle_count": len(cycles),
        "state_period_census": dict(
            sorted(Counter(records[key]["state_period"] for key in cycles).items())
        ),
        "residual_period_census": dict(
            sorted(
                Counter(
                    records[key]["residual_period"] for key in cycles
                ).items()
            )
        ),
        "open_count": len(open_keys),
        "open_minimum_weight_census": dict(
            sorted(
                Counter(
                    min(
                        map(
                            len,
                            records[key]["supports"][:horizon + 1],
                        )
                    )
                    for key in open_keys
                ).items()
            )
        ),
        "all_certified_cycles_forever_nonzero": all(
            records[key]["cycle_nonzero"] for key in cycles
        ),
        "clean_keys": tuple(clean),
        "cycle_keys": tuple(cycles),
        "open_keys": tuple(open_keys),
    }


def sweep_256(
    family: dict[str, object],
    landed_support: object,
) -> dict[str, object]:
    """Own exhaustive loop; SHA-256 hits are confirmed by exact state bytes."""

    records: dict[Key, dict[str, object]] = {}
    all_clean_hits = []
    collision_count = 0
    t64_projection_disagreements = 0
    all_projection_disagreements = 0
    first_projection_disagreements = []
    global_state_trace = sha256()
    global_support_trace = sha256()

    for key in sorted(family["states"]):
        state = family["states"][key]
        word = family["words"][key[1]]
        supports = []
        first_clean = None
        clean_times = []
        first_recurrence = None
        seen: dict[bytes, list[tuple[int, bytes]]] = {}
        exact_state_count = 0
        key_state_trace = sha256()
        key_support_trace = sha256()
        horizon_state_sha256 = {}
        horizon_support_sha256 = {}
        special_state_sha256 = {}

        for update in range(HORIZONS[-1] + 1):
            if update:
                state = K.A.apply_semantic(state, word)
            payload = state_bytes(state)
            state_hash = sha256(payload).digest()
            landed = landed_support(state)
            independent = independent_residual_support(state)
            if landed != independent:
                all_projection_disagreements += 1
                if update <= HORIZONS[0]:
                    t64_projection_disagreements += 1
                if len(first_projection_disagreements) < 10:
                    first_projection_disagreements.append(
                        {
                            "key": key,
                            "update": update,
                            "landed": canonical_support(landed),
                            "independent": canonical_support(independent),
                        }
                    )
            supports.append(landed)
            residual_payload = support_bytes(landed)
            row_key = compact(key).encode("utf-8")
            row_time = update.to_bytes(4, "big")
            framed_update(
                global_state_trace, row_key, row_time, payload
            )
            framed_update(
                global_support_trace,
                row_key,
                row_time,
                residual_payload,
            )
            framed_update(key_state_trace, row_time, payload)
            framed_update(key_support_trace, row_time, residual_payload)

            if not landed:
                clean_times.append(update)
                all_clean_hits.append((key, update))
                if first_clean is None:
                    first_clean = update

            bucket = seen.setdefault(state_hash, [])
            exact_match = next(
                (
                    prior_update
                    for prior_update, prior_payload in bucket
                    if prior_payload == payload
                ),
                None,
            )
            if exact_match is None:
                if bucket:
                    collision_count += 1
                bucket.append((update, payload))
                exact_state_count += 1
            elif first_recurrence is None:
                first_recurrence = (
                    exact_match,
                    update - exact_match,
                    update,
                    state_hash.hex(),
                )

            if update in HORIZONS:
                horizon_state_sha256[update] = sha256(payload).hexdigest()
                horizon_support_sha256[update] = sha256(
                    residual_payload
                ).hexdigest()
            if key == HEADLINE_KEY and update in {
                HEADLINE_TIME - 1,
                HEADLINE_TIME,
            }:
                special_state_sha256[update] = sha256(payload).hexdigest()

        if first_recurrence is None:
            cycle_start = state_period = cycle_closure = None
            residual_period = cycle_nonzero = residue_phases = None
            recurrence_state_sha256 = None
        else:
            cycle_start, state_period, cycle_closure, recurrence_state_sha256 = (
                first_recurrence
            )
            phases = tuple(supports[cycle_start:cycle_closure])
            residual_period = least_phase_period(phases)
            cycle_nonzero = all(phases)
            residue_phases = tuple(
                canonical_support(phase) for phase in phases
            )

        records[key] = {
            "first_clean": first_clean,
            "clean_times": tuple(clean_times),
            "cycle_start": cycle_start,
            "state_period": state_period,
            "residual_period": residual_period,
            "cycle_closure": cycle_closure,
            "cycle_nonzero": cycle_nonzero,
            "residue_phases": residue_phases,
            "recurrence_state_sha256": recurrence_state_sha256,
            "supports": tuple(supports),
            "exact_unique_states_through_T256": exact_state_count,
            "state_trace_sha256": key_state_trace.hexdigest(),
            "support_trace_sha256": key_support_trace.hexdigest(),
            "horizon_state_sha256": horizon_state_sha256,
            "horizon_support_sha256": horizon_support_sha256,
            "special_state_sha256": special_state_sha256,
        }

    snapshots = {
        horizon: snapshot(records, horizon) for horizon in HORIZONS
    }
    classifications = []
    t64_rows = []
    for key in sorted(records):
        record = records[key]
        residues = record["supports"][:HORIZONS[0] + 1]
        base = {
            "event": key[0],
            "positions": key[1],
            "minimum_residue_weight": min(map(len, residues)),
            "distinct_residues_through_64": len(set(residues)),
        }
        if (
            record["first_clean"] is not None
            and record["first_clean"] <= HORIZONS[0]
        ):
            classification = "reaches_zero"
            row = {
                **base,
                "classification": classification,
                "first_clean_update": record["first_clean"],
            }
        elif (
            record["cycle_closure"] is not None
            and record["cycle_closure"] <= HORIZONS[0]
        ):
            classification = "nonzero_limit_cycle"
            row = {
                **base,
                "classification": classification,
                "cycle_start": record["cycle_start"],
                "cycle_length": record["state_period"],
            }
        else:
            classification = "not_clean_or_closed_within_64"
            row = {**base, "classification": classification}
        classifications.append(row)
        t64_rows.append(
            {
                "event": key[0],
                "positions": key[1],
                "classification": classification,
                "clean_through_T64": (
                    record["first_clean"] is not None
                    and record["first_clean"] <= HORIZONS[0]
                ),
                "T64_state_sha256":
                    record["horizon_state_sha256"][HORIZONS[0]],
                "T64_residual_sha256":
                    record["horizon_support_sha256"][HORIZONS[0]],
                "minimum_residue_weight":
                    base["minimum_residue_weight"],
                "distinct_residues_through_64":
                    base["distinct_residues_through_64"],
            }
        )

    deterministic_rows = tuple(
        {
            "key": key,
            "first_clean": record["first_clean"],
            "clean_times": record["clean_times"],
            "cycle_start": record["cycle_start"],
            "state_period": record["state_period"],
            "residual_period": record["residual_period"],
            "cycle_closure": record["cycle_closure"],
            "cycle_nonzero": record["cycle_nonzero"],
            "residue_phases": record["residue_phases"],
            "recurrence_state_sha256":
                record["recurrence_state_sha256"],
            "exact_unique_states_through_T256":
                record["exact_unique_states_through_T256"],
            "state_trace_sha256": record["state_trace_sha256"],
            "support_trace_sha256": record["support_trace_sha256"],
            "horizon_state_sha256": record["horizon_state_sha256"],
            "horizon_support_sha256": record["horizon_support_sha256"],
            "special_state_sha256": record["special_state_sha256"],
        }
        for key, record in sorted(records.items())
    )
    public_snapshots = {
        horizon: {
            key: value
            for key, value in snapshots[horizon].items()
            if key not in {"clean_keys", "cycle_keys", "open_keys"}
        }
        for horizon in HORIZONS
    }
    deterministic_payload = {
        "snapshots": public_snapshots,
        "records": deterministic_rows,
        "all_clean_hits": tuple(all_clean_hits),
        "state_trace_sha256": global_state_trace.hexdigest(),
        "support_trace_sha256": global_support_trace.hexdigest(),
        "collision_count": collision_count,
        "all_projection_disagreements": all_projection_disagreements,
    }
    return {
        "records": records,
        "snapshots": snapshots,
        "public_snapshots": public_snapshots,
        "all_clean_hits": tuple(all_clean_hits),
        "hash_collision_count": collision_count,
        "t64_projection_disagreements": t64_projection_disagreements,
        "all_projection_disagreements": all_projection_disagreements,
        "first_projection_disagreements":
            tuple(first_projection_disagreements),
        "T64_classifications": tuple(classifications),
        "T64_classification_sha256": digest_rows(classifications),
        "T64_key_rows": tuple(t64_rows),
        "T64_key_rows_sha256": digest_rows(t64_rows),
        "state_trace_sha256": global_state_trace.hexdigest(),
        "support_trace_sha256": global_support_trace.hexdigest(),
        "deterministic_sha256": digest_rows(deterministic_payload),
    }


def fidelity_certificate(
    source_control: dict[str, object],
    extraction_audit: dict[str, object],
    static_attack: dict[str, object],
    family: dict[str, object],
    sweep: dict[str, object],
) -> dict[str, object]:
    t64 = sweep["snapshots"][64]
    expected_digest = static_attack[
        "primary_expected_T64_classification_sha256"
    ]
    expected_t64_snapshot = {
        "keys": 176,
        "clean_count": 0,
        "first_clean_time_census": {},
        "cycle_count": 11,
        "state_period_census": {2: 2, 3: 9},
        "residual_period_census": {2: 2, 3: 9},
        "open_count": 165,
        "open_minimum_weight_census":
            {1: 114, 2: 19, 3: 16, 4: 7, 5: 1, 6: 1, 7: 7},
        "all_certified_cycles_forever_nonzero": True,
    }
    observed_t64_snapshot = {
        key: t64[key] for key in expected_t64_snapshot
    }
    result = {
        "attack_target": "Cycle-790 reimplementation versus landed Cycle-762 test",
        "source_control_pass": source_control["pass"],
        "landed_extraction_pass": extraction_audit["pass"],
        "static_AST_attack": static_attack,
        "landed_family_pass": family["summary"]["pass"],
        "keys": len(sweep["T64_key_rows"]),
        "samples_per_key": HORIZONS[0] + 1,
        "landed_test_samples": len(sweep["T64_key_rows"]) * (HORIZONS[0] + 1),
        "T64_projection_disagreements":
            sweep["t64_projection_disagreements"],
        "first_projection_disagreements":
            sweep["first_projection_disagreements"],
        "T64_observed_snapshot": observed_t64_snapshot,
        "T64_expected_snapshot": expected_t64_snapshot,
        "T64_classification_sha256":
            sweep["T64_classification_sha256"],
        "primary_frozen_T64_classification_sha256": expected_digest,
        "T64_key_rows_sha256": sweep["T64_key_rows_sha256"],
        "full_T0_T256_state_trace_sha256":
            sweep["state_trace_sha256"],
        "full_T0_T256_landed_residual_trace_sha256":
            sweep["support_trace_sha256"],
        "byte_exact_basis": (
            "states serialized as one byte per binary wire; landed and "
            "independent residual supports serialized as canonical compact JSON"
        ),
        "primary_execution": "BLOCKLISTED_TEXT_AST_ONLY",
        "physical_question": PHYSICAL_SCOPE,
    }
    result["pass"] = (
        source_control["pass"]
        and extraction_audit["pass"]
        and static_attack["static_pass"]
        and family["summary"]["pass"]
        and result["keys"] == 176
        and result["landed_test_samples"] == 176 * 65
        and result["T64_projection_disagreements"] == 0
        and observed_t64_snapshot == expected_t64_snapshot
        and result["T64_classification_sha256"] == expected_digest
        and result["physical_question"] == PHYSICAL_SCOPE
    )
    result["finding"] = (
        "CONFIRMED_WITH_LANDED_TEST: Cycle-790's load-bearing "
        "reimplementation is semantically AST-identical to the landed "
        "Cycle-762 test and agrees on all 176 T=64 verdicts and 11,440 "
        "landed-test residual samples."
        if result["pass"]
        else
        "REFUTED_REIMPLEMENTATION_DIVERGENCE: Cycle-790 does not agree "
        "with the landed Cycle-762 T=64 test; the extension is invalid."
    )
    return result


def headline_event_certificate(sweep: dict[str, object]) -> dict[str, object]:
    records = sweep["records"]
    headline = records[HEADLINE_KEY]
    first_clean_rows = tuple(
        (key, record["first_clean"])
        for key, record in sorted(records.items())
        if record["first_clean"] is not None
        and record["first_clean"] <= HORIZONS[-1]
    )
    clean_configuration_counts = {
        horizon: sweep["snapshots"][horizon]["clean_count"]
        for horizon in HORIZONS
    }
    support_251 = canonical_support(
        headline["supports"][HEADLINE_TIME - 1]
    )
    support_252 = canonical_support(
        headline["supports"][HEADLINE_TIME]
    )
    result = {
        "headline_key": HEADLINE_KEY,
        "headline_first_clean": headline["first_clean"],
        "headline_clean_times_through_T256": headline["clean_times"],
        "headline_all_t_before_252_nonzero": all(
            headline["supports"][update]
            for update in range(HEADLINE_TIME)
        ),
        "headline_t252_clean": not headline["supports"][HEADLINE_TIME],
        "headline_t251_support": support_251,
        "headline_t252_support": support_252,
        "headline_t251_state_sha256":
            headline["special_state_sha256"][HEADLINE_TIME - 1],
        "headline_t252_state_sha256":
            headline["special_state_sha256"][HEADLINE_TIME],
        "headline_t252_residual_sha256":
            sha256(support_bytes(headline["supports"][HEADLINE_TIME])).hexdigest(),
        "first_clean_rows_through_T256": first_clean_rows,
        "all_clean_hits_through_T256": sweep["all_clean_hits"],
        "clean_configuration_counts": clean_configuration_counts,
        "projection_disagreements_through_T256":
            sweep["all_projection_disagreements"],
        "evolution":
            "own update loop using anchored K.A.apply_semantic and the "
            "AST-extracted landed Cycle-762 residual_support test",
        "physical_question": PHYSICAL_SCOPE,
    }
    result["pass"] = (
        result["headline_first_clean"] == HEADLINE_TIME
        and result["headline_all_t_before_252_nonzero"]
        and result["headline_t252_clean"]
        and first_clean_rows == ((HEADLINE_KEY, HEADLINE_TIME),)
        and clean_configuration_counts == {64: 0, 128: 0, 256: 1}
        and result["projection_disagreements_through_T256"] == 0
        and result["physical_question"] == PHYSICAL_SCOPE
    )
    result["finding"] = (
        "CONFIRMED_WITH_LANDED_TEST: epoch 3 positions (1,10) is nonclean "
        "for every t<252, clean at t=252, and is the sole configuration "
        "with a first clean time through T=256."
        if result["pass"]
        else
        "REFUTED_SPURIOUS_OR_MISSED_CLEAN_EVENT: the landed-test sweep "
        "does not support the claimed unique first clean event at t=252."
    )
    return result


def cycle_and_open_certificate(sweep: dict[str, object]) -> dict[str, object]:
    records = sweep["records"]
    cycle_keys = sweep["snapshots"][256]["cycle_keys"]
    open_keys = sweep["snapshots"][256]["open_keys"]
    cycle_rows = tuple(
        {
            "key": key,
            "cycle_start": records[key]["cycle_start"],
            "state_period": records[key]["state_period"],
            "residual_period": records[key]["residual_period"],
            "closure": records[key]["cycle_closure"],
            "recurrence_state_sha256":
                records[key]["recurrence_state_sha256"],
            "forever_nonzero_on_certified_cycle":
                records[key]["cycle_nonzero"],
        }
        for key in cycle_keys
    )
    spot_keys = tuple(
        sorted(
            open_keys,
            key=lambda key: sha256(
                compact(key).encode("utf-8")
            ).digest(),
        )[:10]
    )
    spot_rows = tuple(
        {
            "key": key,
            "no_clean_through_T256":
                records[key]["first_clean"] is None,
            "no_exact_state_recurrence_through_T256":
                records[key]["cycle_closure"] is None,
            "exact_unique_states_through_T256":
                records[key]["exact_unique_states_through_T256"],
            "all_257_landed_residues_nonzero":
                all(records[key]["supports"]),
            "state_trace_sha256": records[key]["state_trace_sha256"],
            "support_trace_sha256": records[key]["support_trace_sha256"],
        }
        for key in spot_keys
    )
    state_period_census = dict(
        sorted(Counter(row["state_period"] for row in cycle_rows).items())
    )
    residual_period_census = dict(
        sorted(Counter(row["residual_period"] for row in cycle_rows).items())
    )
    result = {
        "recurrence_method": (
            "SHA-256 of exact binary state bytes; every digest hit was "
            "confirmed by byte equality before recurrence certification"
        ),
        "hash_collision_count": sweep["hash_collision_count"],
        "cycle_count": len(cycle_keys),
        "state_period_census": state_period_census,
        "residual_period_census": residual_period_census,
        "cycle_rows": cycle_rows,
        "open_count": len(open_keys),
        "open_spot_selection":
            "10 lowest SHA-256 ranks of canonical open keys",
        "open_spot_rows": spot_rows,
        "physical_question": PHYSICAL_SCOPE,
    }
    result["pass"] = (
        result["hash_collision_count"] == 0
        and result["cycle_count"] == 11
        and state_period_census == {2: 2, 3: 9}
        and residual_period_census == {2: 2, 3: 9}
        and all(
            row["cycle_start"] == 0
            and row["state_period"] == row["residual_period"]
            and row["closure"] == row["state_period"]
            and row["forever_nonzero_on_certified_cycle"]
            for row in cycle_rows
        )
        and result["open_count"] == 164
        and len(spot_rows) == 10
        and all(
            row["no_clean_through_T256"]
            and row["no_exact_state_recurrence_through_T256"]
            and row["exact_unique_states_through_T256"] == 257
            and row["all_257_landed_residues_nonzero"]
            for row in spot_rows
        )
        and result["physical_question"] == PHYSICAL_SCOPE
    )
    return result


def integer_relation(period: int, constant: int) -> str:
    if period == constant:
        return "equal"
    if constant % period == 0:
        return "period_divides_constant"
    if period % constant == 0:
        return "period_is_multiple_of_constant"
    return "neither"


def divisibility_certificate(
    family: dict[str, object],
    cycle_certificate: dict[str, object],
) -> dict[str, object]:
    banks, _links = K.B.chain_genesis(FIXTURE_BANKS)
    constants = (
        ("orbit_length", LANDED_ORBIT_LENGTH),
        ("station_count", len(family["program"])),
        *tuple(
            (f"bank_count_{count}", count)
            for count in LANDED_BANK_COUNTS
        ),
        *tuple(
            (f"bank_{index}_register_width", len(bank))
            for index, bank in enumerate(banks)
        ),
    )
    rows = tuple(
        {
            "period": period,
            "keys": count,
            "relations": {
                label: {
                    "constant": constant,
                    "relation": integer_relation(period, constant),
                }
                for label, constant in constants
            },
        }
        for period, count in sorted(
            cycle_certificate["residual_period_census"].items()
        )
    )
    explicit_recount = {
        "2_divides_130": 130 % 2 == 0,
        "2_divides_12": 12 % 2 == 0,
        "3_divides_12": 12 % 3 == 0,
    }
    result = {
        "definition": "Pure integer divisibility data; no numerological inference",
        "period_basis":
            "least residual phase period on an exact full-state cycle",
        "structural_constants": dict(constants),
        "period_census": cycle_certificate["residual_period_census"],
        "explicit_recount": explicit_recount,
        "rows": rows,
        "physical_question": PHYSICAL_SCOPE,
    }
    result["pass"] = (
        result["period_census"] == {2: 2, 3: 9}
        and all(explicit_recount.values())
        and result["definition"]
        == "Pure integer divisibility data; no numerological inference"
        and result["physical_question"] == PHYSICAL_SCOPE
    )
    return result


def run() -> int:
    started = monotonic()

    source_packet = source_and_blocklist_certificate()
    source_control = source_packet["result"]
    check("A_SHA_ANCHORS_AUDIT_INPUTS_AND_PRIMARY_BLOCKLIST", source_control["pass"])
    data("A_CONTROLS", source_control)

    landed, extraction_audit = extract_landed_machinery(
        source_packet["cycle762_checker_source"]
    )
    static_attack = reimplementation_ast_attack(
        source_packet["cycle762_checker_source"],
        source_packet["primary_source"],
    )
    family = landed["build_family"]()
    first_sweep = sweep_256(family, landed["residual_support"])

    fidelity = fidelity_certificate(
        source_control,
        extraction_audit,
        static_attack,
        family,
        first_sweep,
    )
    check("B_REIMPLEMENTATION_FIDELITY_FULL_T64", fidelity["pass"])
    OUTPUT_LINES.append("FINDING B " + fidelity["finding"])
    data(
        "B_FIDELITY",
        {
            key: value
            for key, value in fidelity.items()
            if key != "static_AST_attack"
        },
    )
    data("B_STATIC_AST_ATTACK", static_attack)
    data("B_T64_ROWS", first_sweep["T64_key_rows"])

    event = headline_event_certificate(first_sweep)
    check("C_T252_FIRST_CLEAN_AND_T256_SWEEP", event["pass"])
    OUTPUT_LINES.append("FINDING C " + event["finding"])
    data("C_T252_AND_CLEAN_SWEEP", event)
    data("C_HORIZON_COUNTS", first_sweep["public_snapshots"])

    cycles = cycle_and_open_certificate(first_sweep)
    check("D_CYCLE_CENSUS_AND_10_OPEN_SPOTCHECKS", cycles["pass"])
    data(
        "D_CYCLE_CENSUS",
        {
            key: value
            for key, value in cycles.items()
            if key not in {"cycle_rows", "open_spot_rows"}
        },
    )
    data("D_CYCLE_ROWS", cycles["cycle_rows"])
    data("D_OPEN_SPOT_ROWS", cycles["open_spot_rows"])

    divisibility = divisibility_certificate(family, cycles)
    check("E_DIVISIBILITY_TABLE_RECOUNT_AS_DATA", divisibility["pass"])
    data("E_DIVISIBILITY", divisibility)

    replay_family = landed["build_family"]()
    replay = sweep_256(
        replay_family, landed["residual_support"]
    )
    family_deterministic = (
        replay_family["program"] == family["program"]
        and replay_family["positions"] == family["positions"]
        and replay_family["words"] == family["words"]
        and replay_family["states"] == family["states"]
        and replay_family["residues"] == family["residues"]
        and replay_family["summary"] == family["summary"]
    )
    sweep_deterministic = (
        replay["deterministic_sha256"]
        == first_sweep["deterministic_sha256"]
        and replay["state_trace_sha256"]
        == first_sweep["state_trace_sha256"]
        and replay["support_trace_sha256"]
        == first_sweep["support_trace_sha256"]
        and replay["T64_classification_sha256"]
        == first_sweep["T64_classification_sha256"]
        and replay["T64_key_rows"] == first_sweep["T64_key_rows"]
        and replay["public_snapshots"] == first_sweep["public_snapshots"]
        and replay["all_clean_hits"] == first_sweep["all_clean_hits"]
    )
    elapsed = monotonic() - started
    bounds = {
        "family_deterministic": family_deterministic,
        "sweep_deterministic": sweep_deterministic,
        "primary_deterministic_sha256":
            first_sweep["deterministic_sha256"],
        "replay_deterministic_sha256":
            replay["deterministic_sha256"],
        "primary_state_trace_sha256":
            first_sweep["state_trace_sha256"],
        "replay_state_trace_sha256":
            replay["state_trace_sha256"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "physical_question": PHYSICAL_SCOPE,
    }
    report_core = {
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "lineage_commit": LINEAGE_COMMIT,
        "machinery_basis":
            "EXACT_AST_EXTRACTED_LANDED_CYCLE762_TEST_PLUS_OWN_EVOLUTION",
        "certificate_A": source_control,
        "certificate_B": {
            key: value
            for key, value in fidelity.items()
            if key != "static_AST_attack"
        },
        "certificate_C": event,
        "certificate_D": {
            key: value
            for key, value in cycles.items()
            if key not in {"cycle_rows", "open_spot_rows"}
        },
        "certificate_E": divisibility,
        "determinism_and_bounds": bounds,
        "physical_question": PHYSICAL_SCOPE,
    }
    estimated = (
        "\n".join(
            OUTPUT_LINES
            + ["PASS F_DETERMINISM_RUNTIME_AND_STDOUT_BOUNDS"]
        )
        + "\n"
        + compact(
            {
                **report_core,
                "checks": {
                    **CHECKS,
                    "F_DETERMINISM_RUNTIME_AND_STDOUT_BOUNDS": True,
                },
            }
        )
        + "\n"
    )
    projected_stdout_bytes = len(estimated.encode("utf-8")) + 4096
    bounds["projected_stdout_bytes_with_safety_margin"] = (
        projected_stdout_bytes
    )
    bounds_pass = (
        family_deterministic
        and sweep_deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
        and PRIMARY_MODULE_NAME not in sys.modules
        and bounds["physical_question"] == PHYSICAL_SCOPE
    )
    check("F_DETERMINISM_RUNTIME_AND_STDOUT_BOUNDS", bounds_pass)
    data("F_DETERMINISM_AND_BOUNDS", bounds)

    scientific_names = (
        "B_REIMPLEMENTATION_FIDELITY_FULL_T64",
        "C_T252_FIRST_CLEAN_AND_T256_SWEEP",
        "D_CYCLE_CENSUS_AND_10_OPEN_SPOTCHECKS",
        "E_DIVISIBILITY_TABLE_RECOUNT_AS_DATA",
    )
    if CHECKS["A_SHA_ANCHORS_AUDIT_INPUTS_AND_PRIMARY_BLOCKLIST"] and any(
        not CHECKS[name] for name in scientific_names
    ):
        verdict = "REFUTED"
        terminal = "CYCLE790_HORIZON_INDEPENDENT_CHECK_REFUTED"
    elif all(CHECKS.values()):
        verdict = "CONFIRMED_WITH_LANDED_TEST"
        terminal = (
            "CYCLE790_HORIZON_INDEPENDENT_CHECK_"
            "CONFIRMED_WITH_LANDED_TEST"
        )
    else:
        verdict = "CHECKER_INCOMPLETE"
        terminal = "CYCLE790_HORIZON_INDEPENDENT_CHECK_HONEST_FAIL"

    report = {
        **report_core,
        "checks": dict(CHECKS),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "pass": all(CHECKS.values()),
        "verdict": verdict,
        "terminal": terminal,
    }
    report["report_sha256"] = digest_rows(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    actual_stdout_bytes = len(output.encode("utf-8"))
    if actual_stdout_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "verdict": "CHECKER_INCOMPLETE",
            "terminal": "CYCLE790_HORIZON_INDEPENDENT_CHECK_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": actual_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "physical_question": PHYSICAL_SCOPE,
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "checks": dict(CHECKS),
            "pass": False,
            "verdict": "CHECKER_INCOMPLETE",
            "terminal": "CYCLE790_HORIZON_INDEPENDENT_CHECK_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
            "primary_imported": PRIMARY_MODULE_NAME in sys.modules,
            "physical_question": PHYSICAL_SCOPE,
        }
        if OUTPUT_LINES:
            sys.stdout.write("\n".join(OUTPUT_LINES) + "\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
