#!/usr/bin/env python3
"""Cycle 791 independent adversarial resolution checker.

Both Cycle-790 and Cycle-791 primaries are blocklisted: this checker reads
their bytes only for SHA/AST controls and never imports or executes them.
Dynamics are rebuilt from the landed Cycle-736/719 modules.  The cleanliness
projection is reimplemented from the SHA-pinned Cycle-762 pair, and recurrence
discovery uses BLAKE2b plus exact state re-evolution rather than either
primary's SHA-256/checkpoint path.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter
from hashlib import blake2b, sha256
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PINNED_TEXT_PATHS = (
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
)
BLOCKLIST_TEXT_PATHS = (
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
    "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
)
BLOCKLIST_MODULES = (
    "frontier_cycle790_horizon_extension_2026_07_28",
    "frontier_cycle791_open_keys_resolution_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PINNED_TEXT_PATHS[0]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    PINNED_TEXT_PATHS[1]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    BLOCKLIST_TEXT_PATHS[0]:
        "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    BLOCKLIST_TEXT_PATHS[1]:
        "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
}

RING_STATIONS = 11
FIXTURE_BANKS = 2
BASELINE_HORIZON = 256
FINAL_HORIZON = 1024
FAMILY_SIZE = 176
STDOUT_LIMIT_BYTES = 150 * 1024

EXPECTED_T252_KEY = (3, (1, 10))
EXPECTED_T371_KEY = (3, (0, 7))
EXPECTED_PERIOD288_KEY = (2, (0, 9))
EXPECTED_PRIOR_CYCLES = {
    (3, (0, 5)): 2,
    (3, (0, 6)): 2,
    (3, (1, 6)): 3,
    (3, (1, 7)): 3,
    (3, (2, 7)): 3,
    (3, (2, 8)): 3,
    (3, (3, 8)): 3,
    (3, (3, 9)): 3,
    (3, (4, 9)): 3,
    (3, (4, 10)): 3,
    (3, (5, 10)): 3,
}
EXPECTED_KEYSET_SHA256 = {
    "family": "788e673e0a8f8f46931dd549dbdff0010a21d82f98c3363859e8da2e160bf756",
    "clean": "ab0b2a632f6deee4329f02df4834ff3ecc8cd4d885f59459f7dee46fd5dc5bed",
    "cycles": "f7fd5f12d3705e30d5dacbf45013d2c4bec743f6e8b72d85df60a6aa8c51b2ae",
    "open": "fe07a7b4ffdc2587b01db029d5afe4550d0987eb32fa8873f3afd917d916d947",
}

Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(rows: object) -> str:
    return sha256(compact(rows).encode("utf-8")).hexdigest()


def keyset_bytes(keys: object) -> bytes:
    return compact(tuple(sorted(keys))).encode("utf-8")


def literal_tuple_assignment(path: Path, name: str) -> tuple[str, ...] | None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    matches: list[ast.AST] = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
    if (
        len(matches) != 1
        or not isinstance(matches[0], ast.Tuple)
        or not all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in matches[0].elts
        )
    ):
        return None
    return ast.literal_eval(matches[0])


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def text_anchor_and_blocklist_certificate() -> dict[str, object]:
    """Authenticate allowed inputs and prove both primaries stayed text-only."""

    paths = AUDIT_INPUT_PATHS + PINNED_TEXT_PATHS + BLOCKLIST_TEXT_PATHS
    payloads = {path: (ROOT / path).read_bytes() for path in paths}
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    checker_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    landed_imports = {
        node.names[0].name
        for node in checker_tree.body
        if isinstance(node, ast.Import)
        and len(node.names) == 1
        and node.names[0].name.startswith("frontier_cycle")
    }
    expected_landed_imports = {
        Path(path).stem for path in AUDIT_INPUT_PATHS
    }
    imported_any_blocklisted = any(
        name in sys.modules for name in BLOCKLIST_MODULES
    )
    checker_imports_blocklisted = any(
        isinstance(node, (ast.Import, ast.ImportFrom))
        and (
            any(
                alias.name in BLOCKLIST_MODULES
                for alias in getattr(node, "names", ())
            )
            or getattr(node, "module", None) in BLOCKLIST_MODULES
        )
        for node in checker_tree.body
    )
    pinned_requirements = {
        PINNED_TEXT_PATHS[0]: {
            "held_two_bank_epochs",
            "k2_positions",
            "continuation_census",
        },
        PINNED_TEXT_PATHS[1]: {
            "separated_k2_positions",
            "synchronous_word",
            "watched_bank_registers",
            "residual_support",
            "build_family",
            "asymptotic_census",
        },
    }
    primary_requirements = {
        BLOCKLIST_TEXT_PATHS[0]: {
            "build_family",
            "cycle_census",
            "residual_support",
            "minimal_phase_period",
        },
        BLOCKLIST_TEXT_PATHS[1]: {
            "build_identity_and_checkpoints",
            "advance_one_key",
            "resolution_sweep",
            "run",
        },
    }
    pinned_ast_ok = all(
        required <= function_names(trees[path])
        for path, required in pinned_requirements.items()
    )
    blocklisted_ast_ok = all(
        required <= function_names(trees[path])
        for path, required in primary_requirements.items()
    )
    audit_tuple = literal_tuple_assignment(
        Path(__file__), "AUDIT_INPUT_PATHS"
    )
    passed = (
        all((ROOT / path).is_file() for path in paths)
        and actual_sha == EXPECTED_SHA256
        and audit_tuple == AUDIT_INPUT_PATHS
        and landed_imports == expected_landed_imports
        and pinned_ast_ok
        and blocklisted_ast_ok
        and not imported_any_blocklisted
        and not checker_imports_blocklisted
    )
    return {
        "pass": passed,
        "input_sha256": actual_sha,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal_exact": audit_tuple == AUDIT_INPUT_PATHS,
        "direct_landed_imports": tuple(sorted(landed_imports)),
        "pinned_762_pair_AST_only": pinned_ast_ok,
        "blocklisted_790_791_AST_only": blocklisted_ast_ok,
        "blocklisted_modules_imported": imported_any_blocklisted,
        "checker_imports_blocklisted": checker_imports_blocklisted,
    }


def separated_pairs() -> tuple[tuple[int, int], ...]:
    """Enumerate C_11 two-site independent sets without Cycle-790/791."""

    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        )
        > 1
    )


def independently_composed_word(
    program: tuple[object, ...],
    initial_positions: tuple[int, int],
) -> tuple[object, ...]:
    """Compose a full synchronous orbit from the closed motion formula."""

    stations = len(program)
    word: list[object] = []
    for step in range(stations):
        live = {
            (initial + step) % stations
            for initial in initial_positions
        }
        for station in range(stations):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
    return tuple(word)


def watched_bank_registers() -> tuple[tuple[str, int], ...]:
    """Literal register family pinned by the Cycle-762 checker text."""

    fixed = (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
    )
    fresh = tuple(
        (f"FRESH_{index}", wire)
        for index, wire in enumerate(K.A.FRESH)
    )
    zero_work = tuple(
        (f"ZERO_WORK_{index}", wire)
        for index, wire in enumerate(K.A.ZERO_WORK)
    )
    return fixed + fresh + zero_work + (("TOKEN_OK", K.A.TOKEN_OK),)


def landed_residual_support(state: tuple[int, ...]) -> Support:
    """Reimplement the exact landed Cycle-762 postimage-cleanliness test."""

    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    support: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        support.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register, wire in watched_bank_registers():
            if bank[wire]:
                support.add(("bank", register, bank_index))
    for link_index, link in enumerate(links):
        for wire, value in enumerate(link):
            if value:
                support.add(("link", f"WIRE_{wire}", link_index))
    return frozenset(support)


def canonical_support(support: Support) -> tuple[Coordinate, ...]:
    return tuple(sorted(support))


def build_family_independently() -> dict[str, object]:
    """Build all four epochs and 176 two-source states from landed machinery."""

    started = monotonic()
    program = K.interleaved_program(FIXTURE_BANKS)
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks0, links0)
    allocator_word = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs: list[tuple[int, tuple[int, int], tuple[int, ...]]] = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += after != K.A.apply_semantic(
            before, allocator_word
        )
        epoch_failures += (
            rail_a != (1,) + (0,) * (len(program) - 1)
        )
        epoch_failures += any(rail_b)
        epoch_failures += len(trace) != len(program)
        epochs.append((event, direction, before))
        state = after

    positions = separated_pairs()
    m736_positions = {
        M736.occupied_sites(configuration)
        for configuration in M736.configuration_census()["configurations"]
        if sum(configuration) == 2
    }
    words = {
        pair: independently_composed_word(program, pair)
        for pair in positions
    }
    word_disagreements = sum(
        words[pair]
        != M736.synchronous_composition_word(program, pair)
        for pair in positions
    )

    states: dict[Key, tuple[int, ...]] = {}
    residues: dict[Key, Support] = {}
    composition_failures = 0
    rail_failures = 0
    inverse_failures = 0
    for event, _direction, before in epochs:
        for pair in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=pair
            )
            restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
                after, program, token_positions=pair, reverse=True
            )
            expected_rail = tuple(
                int(station in pair)
                for station in range(len(program))
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[pair])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            inverse_failures += (
                restored != before
                or inverse_a != rail_a
                or inverse_b != rail_b
            )
            key = (event, pair)
            states[key] = after
            residues[key] = landed_residual_support(after)

    per_epoch_signatures = tuple(
        len(
            {
                residues[(event, pair)]
                for pair in positions
            }
        )
        for event in range(2 * FIXTURE_BANKS)
    )
    initial_residual_rows = tuple(
        (key, canonical_support(residues[key]))
        for key in sorted(residues)
    )
    state_rows = tuple(
        (
            key,
            blake2b(
                bytes(states[key]),
                digest_size=32,
                person=b"C791-family",
            ).hexdigest(),
        )
        for key in sorted(states)
    )
    summary = {
        "epochs": len(epochs),
        "directions": tuple(row[1] for row in epochs),
        "program_stations": len(program),
        "positions": len(positions),
        "M736_position_set_agrees": set(positions) == m736_positions,
        "M736_expected_k2_count": M736.EXPECTED_COUNTS_BY_K[2],
        "synchronous_word_disagreements": word_disagreements,
        "keys": len(states),
        "unique_initial_residual_signatures": len(set(residues.values())),
        "unique_initial_signatures_by_epoch": per_epoch_signatures,
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_return_failures": rail_failures,
        "literal_inverse_failures": inverse_failures,
        "all_initial_residuals_nonzero": all(residues.values()),
        "family_keyset_sha256": sha256(
            keyset_bytes(states)
        ).hexdigest(),
        "initial_residual_sha256": digest_rows(initial_residual_rows),
        "initial_state_blake2b_rows_sha256": digest_rows(state_rows),
        "runtime_seconds": round(monotonic() - started, 6),
    }
    summary["pass"] = (
        summary["epochs"] == 4
        and summary["directions"]
        == ((1, 0), (0, 1), (1, 0), (0, 1))
        and summary["program_stations"] == RING_STATIONS
        and summary["positions"]
        == summary["M736_expected_k2_count"]
        == 44
        and summary["M736_position_set_agrees"]
        and summary["synchronous_word_disagreements"] == 0
        and summary["keys"] == FAMILY_SIZE
        and summary["unique_initial_residual_signatures"] == 25
        and summary["unique_initial_signatures_by_epoch"]
        == (1, 1, 12, 14)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_return_failures"] == 0
        and summary["literal_inverse_failures"] == 0
        and summary["all_initial_residuals_nonzero"]
        and summary["family_keyset_sha256"]
        == EXPECTED_KEYSET_SHA256["family"]
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "initial_residues": residues,
        "summary": summary,
    }


def recurrence_hash(state: tuple[int, ...]) -> bytes:
    """Independent recurrence hash; exact equality is still mandatory."""

    return blake2b(
        bytes(state),
        digest_size=32,
        person=b"C791-adversary",
    ).digest()


def re_evolve(
    initial_state: tuple[int, ...],
    word: tuple[object, ...],
    update: int,
) -> tuple[int, ...]:
    state = initial_state
    for _step in range(update):
        state = K.A.apply_semantic(state, word)
    return state


def least_phase_period(phases: tuple[int, ...]) -> int:
    length = len(phases)
    for candidate in range(1, length + 1):
        if length % candidate:
            continue
        if all(
            phases[index] == phases[index % candidate]
            for index in range(length)
        ):
            return candidate
    raise AssertionError(("no residual phase period", length))


def sweep_all_keys(family: dict[str, object]) -> dict[str, object]:
    """Evolve all keys from t=0; stop only at clean or exact recurrence."""

    started = monotonic()
    support_to_id: dict[Support, int] = {frozenset(): 0}
    support_weights: list[int] = [0]

    def support_id(support: Support) -> int:
        existing = support_to_id.get(support)
        if existing is not None:
            return existing
        identifier = len(support_to_id)
        support_to_id[support] = identifier
        support_weights.append(len(support))
        return identifier

    records: dict[Key, dict[str, object]] = {}
    total_hash_observations = 0
    total_hash_collisions = 0
    total_exact_repeats = 0

    for key in sorted(family["states"]):
        initial_state = family["states"][key]
        word = family["words"][key[1]]
        initial_support = landed_residual_support(initial_state)
        phase_ids = [support_id(initial_support)]
        initial_digest = recurrence_hash(initial_state)
        seen: dict[bytes, list[int]] = {initial_digest: [0]}
        state = initial_state
        first_clean = 0 if not initial_support else None
        cycle_entry = None
        state_period = None
        residual_period = None
        cycle_closure = None
        cycle_nonzero = None
        exact_cycle_equality = None
        hash_collisions = 0
        exact_repeats = 0
        trajectory = sha256()
        trajectory.update(initial_digest)
        trajectory.update(compact(canonical_support(initial_support)).encode())
        evolved_through = 0

        for update in range(1, FINAL_HORIZON + 1):
            if first_clean is not None or cycle_closure is not None:
                break
            state = K.A.apply_semantic(state, word)
            support = landed_residual_support(state)
            phase_ids.append(support_id(support))
            digest = recurrence_hash(state)
            total_hash_observations += 1
            evolved_through = update
            trajectory.update(update.to_bytes(2, "big"))
            trajectory.update(digest)
            trajectory.update(compact(canonical_support(support)).encode())

            if not support:
                first_clean = update
                break

            exact_entry = None
            for candidate_entry in seen.get(digest, ()):
                candidate_state = re_evolve(
                    initial_state, word, candidate_entry
                )
                if candidate_state == state:
                    exact_entry = candidate_entry
                    break
                hash_collisions += 1
                total_hash_collisions += 1
            if exact_entry is not None:
                cycle_entry = exact_entry
                state_period = update - exact_entry
                cycle_closure = update
                phases = tuple(phase_ids[exact_entry:update])
                residual_period = least_phase_period(phases)
                cycle_nonzero = all(
                    support_weights[phase] > 0 for phase in phases
                )
                exact_cycle_equality = (
                    re_evolve(initial_state, word, exact_entry) == state
                )
                exact_repeats += 1
                total_exact_repeats += 1
                break
            seen.setdefault(digest, []).append(update)

        records[key] = {
            "first_clean": first_clean,
            "cycle_entry": cycle_entry,
            "state_period": state_period,
            "residual_period": residual_period,
            "cycle_closure": cycle_closure,
            "cycle_nonzero": cycle_nonzero,
            "exact_cycle_equality": exact_cycle_equality,
            "evolved_through": evolved_through,
            "phase_ids": tuple(phase_ids),
            "minimum_residual_weight": min(
                support_weights[phase] for phase in phase_ids
            ),
            "hash_algorithm":
                "BLAKE2b-256(person=C791-adversary)+exact_re-evolution",
            "hash_observations": evolved_through + 1,
            "distinct_hash_buckets": len(seen),
            "hash_collisions": hash_collisions,
            "exact_repeats": exact_repeats,
            "trajectory_sha256": trajectory.hexdigest(),
        }

    deterministic_rows = tuple(
        {
            "key": key,
            **{
                field: records[key][field]
                for field in (
                    "first_clean",
                    "cycle_entry",
                    "state_period",
                    "residual_period",
                    "cycle_closure",
                    "cycle_nonzero",
                    "exact_cycle_equality",
                    "evolved_through",
                    "minimum_residual_weight",
                    "hash_observations",
                    "distinct_hash_buckets",
                    "hash_collisions",
                    "exact_repeats",
                    "trajectory_sha256",
                )
            },
        }
        for key in sorted(records)
    )
    return {
        "records": records,
        "support_signature_count": len(support_to_id),
        "hash_observations": total_hash_observations + len(records),
        "hash_collisions": total_hash_collisions,
        "exact_repeats": total_exact_repeats,
        "deterministic_sha256": digest_rows(deterministic_rows),
        "runtime_seconds": round(monotonic() - started, 6),
    }


def partition_at(
    records: dict[Key, dict[str, object]],
    horizon: int,
) -> dict[str, tuple[Key, ...]]:
    clean: list[Key] = []
    cycles: list[Key] = []
    open_keys: list[Key] = []
    for key in sorted(records):
        record = records[key]
        if (
            record["first_clean"] is not None
            and record["first_clean"] <= horizon
        ):
            clean.append(key)
        elif (
            record["cycle_closure"] is not None
            and record["cycle_closure"] <= horizon
        ):
            cycles.append(key)
        else:
            open_keys.append(key)
    return {
        "clean": tuple(clean),
        "cycles": tuple(cycles),
        "open": tuple(open_keys),
    }


def render_output(
    certificates: dict[str, bool],
    findings: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {label}"
        for label, passed in certificates.items()
    ]
    lines.extend(
        f"FINDING {label} {compact(value)}"
        for label, value in findings.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: dict[str, bool],
    findings: dict[str, object],
    report: dict[str, object],
) -> str:
    for _attempt in range(12):
        output = render_output(certificates, findings, report)
        size = len(output.encode("utf-8"))
        if report["controls"]["stdout_bytes"] == size:
            return output
        report["controls"]["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    certificates: dict[str, bool] = {}
    findings: dict[str, object] = {}

    anchors = text_anchor_and_blocklist_certificate()
    certificates[
        "A_CONTROLS_SHA_ANCHORS_PRIMARY_BLOCKLIST"
    ] = bool(anchors["pass"])
    findings["A_ANCHORS_AND_BLOCKLIST"] = anchors

    family = build_family_independently()
    primary = sweep_all_keys(family)
    records = primary["records"]
    t256 = partition_at(records, BASELINE_HORIZON)
    t1024 = partition_at(records, FINAL_HORIZON)

    t371 = records[EXPECTED_T371_KEY]
    t371_nonclean_prefix = (
        len(t371["phase_ids"]) == 372
        and all(phase != 0 for phase in t371["phase_ids"][:371])
    )
    t371_clean_exact = t371["phase_ids"][371] == 0
    t371_pass = (
        t371["first_clean"] == 371
        and t371["cycle_closure"] is None
        and t371["evolved_through"] == 371
        and t371_nonclean_prefix
        and t371_clean_exact
    )
    certificates[
        "B_T371_EVENT_LANDED_CLEANLINESS"
    ] = t371_pass
    findings["B_T371_EVENT"] = {
        "finding_verbatim":
            "key (3,(0,7)) is nonclean at every t<371 and clean exactly at t=371",
        "key": EXPECTED_T371_KEY,
        "nonclean_at_every_t_lt_371": t371_nonclean_prefix,
        "clean_exactly_at_t_371": t371_clean_exact,
        "first_clean": t371["first_clean"],
        "observed_updates": len(t371["phase_ids"]),
    }

    period288 = records[EXPECTED_PERIOD288_KEY]
    period288_phases = period288["phase_ids"][
        period288["cycle_entry"]:period288["cycle_closure"]
    ]
    period288_pass = (
        period288["first_clean"] is None
        and period288["cycle_entry"] == 0
        and period288["state_period"] == 288
        and period288["residual_period"] == 6
        and period288["cycle_closure"] == 288
        and period288["cycle_nonzero"] is True
        and period288["exact_cycle_equality"] is True
        and period288["exact_repeats"] == 1
        and len(period288_phases) == 288
        and all(phase != 0 for phase in period288_phases)
        and period288["phase_ids"][288] == period288["phase_ids"][0]
        and least_phase_period(tuple(period288_phases)) == 6
    )
    certificates[
        "C_PERIOD288_CYCLE_INDEPENDENT_HASH"
    ] = period288_pass
    findings["C_PERIOD288_CYCLE"] = {
        "finding_verbatim":
            "key (2,(0,9)) has entry 0, state period 288, residual period 6, and a forever-nonzero residual",
        "key": EXPECTED_PERIOD288_KEY,
        "entry": period288["cycle_entry"],
        "closure": period288["cycle_closure"],
        "state_period": period288["state_period"],
        "residual_period": period288["residual_period"],
        "forever_nonzero_residual": period288["cycle_nonzero"],
        "exact_state_equality_confirmed":
            period288["exact_cycle_equality"],
        "hash_algorithm": period288["hash_algorithm"],
    }

    expected_baseline_terminals = (
        {EXPECTED_T252_KEY} | set(EXPECTED_PRIOR_CYCLES)
    )
    expected_open_by_formula = tuple(
        key
        for key in sorted(family["states"])
        if key not in expected_baseline_terminals
    )
    new_clean = tuple(
        key for key in t1024["clean"] if key not in set(t256["clean"])
    )
    new_cycles = tuple(
        key for key in t1024["cycles"] if key not in set(t256["cycles"])
    )
    baseline_coverage = all(
        (
            records[key]["first_clean"] is not None
            and records[key]["first_clean"] <= FINAL_HORIZON
        )
        or (
            records[key]["cycle_closure"] is not None
            and records[key]["cycle_closure"] <= FINAL_HORIZON
            and records[key]["exact_cycle_equality"] is True
        )
        or records[key]["evolved_through"] == FINAL_HORIZON
        for key in t256["open"]
    )
    final_open_hash_unique = all(
        records[key]["first_clean"] is None
        and records[key]["cycle_closure"] is None
        and records[key]["evolved_through"] == FINAL_HORIZON
        and records[key]["hash_observations"] == FINAL_HORIZON + 1
        and records[key]["distinct_hash_buckets"] == FINAL_HORIZON + 1
        and records[key]["minimum_residual_weight"] > 0
        for key in t1024["open"]
    )
    every_cycle_exact = all(
        records[key]["exact_cycle_equality"] is True
        and records[key]["cycle_nonzero"] is True
        for key in t1024["cycles"]
    )
    every_clean_first_hit_exact = all(
        records[key]["phase_ids"][records[key]["first_clean"]] == 0
        and all(
            phase != 0
            for phase in records[key]["phase_ids"][
                :records[key]["first_clean"]
            ]
        )
        for key in t1024["clean"]
    )
    sweep_pass = (
        len(t256["open"]) == 164
        and t256["open"] == expected_open_by_formula
        and new_clean == (EXPECTED_T371_KEY,)
        and new_cycles == (EXPECTED_PERIOD288_KEY,)
        and len(t1024["open"]) == 162
        and baseline_coverage
        and final_open_hash_unique
        and every_cycle_exact
        and every_clean_first_hit_exact
        and primary["hash_collisions"] == 0
        and primary["exact_repeats"] == 12
    )
    certificates[
        "D_MISSED_EVENT_SWEEP_ALL_164"
    ] = sweep_pass
    findings["D_MISSED_EVENT_SWEEP"] = {
        "finding_verbatim":
            "all 164 Cycle-790-open keys covered through T=1024 or an exact terminal certificate; exactly one new clean, exactly one new certified cycle, and 162 remain open",
        "baseline_open_keys": len(t256["open"]),
        "coverage": "164/164" if baseline_coverage else "INCOMPLETE",
        "new_clean_events": tuple(
            {
                "key": key,
                "first_clean": records[key]["first_clean"],
            }
            for key in new_clean
        ),
        "new_cycle_events": tuple(
            {
                "key": key,
                "entry": records[key]["cycle_entry"],
                "state_period": records[key]["state_period"],
                "residual_period": records[key]["residual_period"],
            }
            for key in new_cycles
        ),
        "open_at_1024": len(t1024["open"]),
        "open_keys_all_nonzero_and_hash_unique_through_1024":
            final_open_hash_unique,
        "all_cycles_exact_and_forever_nonzero": every_cycle_exact,
        "all_clean_events_are_first_zero_hits":
            every_clean_first_hit_exact,
        "state_hash_observations": primary["hash_observations"],
        "digest_collisions": primary["hash_collisions"],
        "exact_recurrences": primary["exact_repeats"],
    }

    expected_cycle_keys = tuple(sorted(EXPECTED_PRIOR_CYCLES))
    t256_keyset_sha = {
        label: sha256(keyset_bytes(t256[label])).hexdigest()
        for label in ("clean", "cycles", "open")
    }
    prior_cycle_controls = all(
        records[key]["cycle_entry"] == 0
        and records[key]["cycle_closure"] == period
        and records[key]["state_period"] == period
        and records[key]["residual_period"] == period
        and records[key]["cycle_nonzero"] is True
        and records[key]["exact_cycle_equality"] is True
        for key, period in EXPECTED_PRIOR_CYCLES.items()
    )
    clean_time_census = dict(
        sorted(Counter(
            records[key]["first_clean"] for key in t1024["clean"]
        ).items())
    )
    state_period_census = dict(
        sorted(Counter(
            records[key]["state_period"] for key in t1024["cycles"]
        ).items())
    )
    residual_period_census = dict(
        sorted(Counter(
            records[key]["residual_period"] for key in t1024["cycles"]
        ).items())
    )
    fractions = {
        "clean": f"{len(t1024['clean'])}/{FAMILY_SIZE}",
        "certified_cycles": f"{len(t1024['cycles'])}/{FAMILY_SIZE}",
        "open": f"{len(t1024['open'])}/{FAMILY_SIZE}",
    }
    identity_pass = (
        family["summary"]["pass"]
        and len(family["states"]) == FAMILY_SIZE
        and t256["clean"] == (EXPECTED_T252_KEY,)
        and records[EXPECTED_T252_KEY]["first_clean"] == 252
        and all(
            phase != 0
            for phase in records[EXPECTED_T252_KEY]["phase_ids"][:252]
        )
        and records[EXPECTED_T252_KEY]["phase_ids"][252] == 0
        and t256["cycles"] == expected_cycle_keys
        and prior_cycle_controls
        and t256["open"] == expected_open_by_formula
        and t256_keyset_sha == {
            label: EXPECTED_KEYSET_SHA256[label]
            for label in ("clean", "cycles", "open")
        }
        and clean_time_census == {252: 1, 371: 1}
        and state_period_census == {2: 2, 3: 9, 288: 1}
        and residual_period_census == {2: 2, 3: 9, 6: 1}
        and fractions == {
            "clean": "2/176",
            "certified_cycles": "12/176",
            "open": "162/176",
        }
    )
    certificates[
        "E_FRACTIONS_AND_CYCLE790_IDENTITY"
    ] = identity_pass
    findings["E_IDENTITY_AND_FRACTIONS"] = {
        "finding_verbatim":
            "Cycle-790 identity is exact: t=252 clean event, 11 prior cycles, and byte-identical 164-key open set; T=1024 fractions are clean 2/176, certified cycles 12/176, open 162/176",
        "T256": {
            "clean": len(t256["clean"]),
            "clean_key_and_time":
                (EXPECTED_T252_KEY, records[EXPECTED_T252_KEY]["first_clean"]),
            "certified_cycles": len(t256["cycles"]),
            "open": len(t256["open"]),
            "keyset_sha256": t256_keyset_sha,
            "expected_keyset_sha256": {
                label: EXPECTED_KEYSET_SHA256[label]
                for label in ("clean", "cycles", "open")
            },
            "prior_cycles_exact": prior_cycle_controls,
        },
        "T1024": {
            "first_clean_time_census": clean_time_census,
            "state_period_census": state_period_census,
            "residual_period_census": residual_period_census,
            "fractions": fractions,
        },
        "family": family["summary"],
    }

    replay_family = build_family_independently()
    replay = sweep_all_keys(replay_family)
    replay_t256 = partition_at(replay["records"], BASELINE_HORIZON)
    replay_t1024 = partition_at(replay["records"], FINAL_HORIZON)
    deterministic = (
        replay_family["summary"]["pass"]
        and replay_family["summary"]["initial_residual_sha256"]
        == family["summary"]["initial_residual_sha256"]
        and replay_family["summary"]["initial_state_blake2b_rows_sha256"]
        == family["summary"]["initial_state_blake2b_rows_sha256"]
        and replay_family["summary"]["family_keyset_sha256"]
        == family["summary"]["family_keyset_sha256"]
        and replay["deterministic_sha256"]
        == primary["deterministic_sha256"]
        and replay_t256 == t256
        and replay_t1024 == t1024
        and replay["hash_collisions"] == primary["hash_collisions"] == 0
        and replay["exact_repeats"] == primary["exact_repeats"] == 12
    )
    elapsed = monotonic() - started
    controls_base = (
        deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not any(name in sys.modules for name in BLOCKLIST_MODULES)
    )
    certificates[
        "F_DETERMINISM_RUNTIME_STDOUT"
    ] = controls_base
    findings["F_CONTROLS"] = {
        "deterministic": deterministic,
        "primary_deterministic_sha256":
            primary["deterministic_sha256"],
        "replay_deterministic_sha256":
            replay["deterministic_sha256"],
        "primary_sweep_seconds": primary["runtime_seconds"],
        "replay_sweep_seconds": replay["runtime_seconds"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocklisted_modules_imported_after_sweeps":
            tuple(
                name for name in BLOCKLIST_MODULES if name in sys.modules
            ),
    }

    scientific_labels = (
        "B_T371_EVENT_LANDED_CLEANLINESS",
        "C_PERIOD288_CYCLE_INDEPENDENT_HASH",
        "D_MISSED_EVENT_SWEEP_ALL_164",
        "E_FRACTIONS_AND_CYCLE790_IDENTITY",
    )
    scientific_pass = all(
        certificates[label] for label in scientific_labels
    )
    overall_pass = all(certificates.values())
    terminal = (
        "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
        if overall_pass
        else (
            "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_REFUTES_PRIMARY"
            if not scientific_pass
            else "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL"
        )
    )
    report = {
        "cycle": 791,
        "role": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "certificates": certificates,
        "scientific_pass": scientific_pass,
        "pass": overall_pass,
        "terminal": terminal,
        "controls": {
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "deterministic": deterministic,
        },
    }
    output = stable_render(certificates, findings, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    certificates[
        "F_DETERMINISM_RUNTIME_STDOUT"
    ] = controls_base and stdout_ok
    findings["F_CONTROLS"]["stdout_bytes"] = len(
        output.encode("utf-8")
    )
    findings["F_CONTROLS"]["stdout_under_150KB"] = stdout_ok
    overall_pass = all(certificates.values())
    scientific_pass = all(
        certificates[label] for label in scientific_labels
    )
    report["certificates"] = certificates
    report["scientific_pass"] = scientific_pass
    report["pass"] = overall_pass
    report["terminal"] = (
        "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
        if overall_pass
        else (
            "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_REFUTES_PRIMARY"
            if not scientific_pass
            else "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL"
        )
    )
    report["controls"]["stdout_under_150KB"] = stdout_ok
    output = stable_render(certificates, findings, report)
    for _attempt in range(12):
        exact_stdout_bytes = len(output.encode("utf-8"))
        if (
            findings["F_CONTROLS"]["stdout_bytes"]
            == exact_stdout_bytes
            and report["controls"]["stdout_bytes"]
            == exact_stdout_bytes
        ):
            break
        findings["F_CONTROLS"]["stdout_bytes"] = exact_stdout_bytes
        report["controls"]["stdout_bytes"] = exact_stdout_bytes
        output = stable_render(certificates, findings, report)
    else:
        raise AssertionError("reported stdout byte count did not converge")
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal":
                "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        sys.stdout.write("FAIL F_DETERMINISM_RUNTIME_STDOUT\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if overall_pass else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "pass": False,
            "terminal":
                "CYCLE791_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write("FAIL UNCAUGHT_CHECKER_EXCEPTION\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
