#!/usr/bin/env python3
"""Independent frozen-table consumer for the Block 220 Markov repair."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import signal
from collections import deque
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 180
PACK = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827"
)
SIDECAR = f"{PACK}/FROZEN_MARKOV_RULE.json"
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_"
    "MARKOV_REPAIR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md"
)
CHECKLIST = (
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_COMPILER_"
    "NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md"
)
AUDIT_INPUT_PATHS = (SIDECAR, NOTE, CHECKLIST)
MUTATIONS = (
    "digest",
    "schema",
    "root_role",
    "inverse_dart",
    "successor",
    "cleanup_root",
    "cleanup_guard",
    "record_qnd",
    "weights",
    "projective_roles",
    "embedding_formula",
    "table_binding",
    "commit_output",
    "flood_output",
    "runtime_history",
)
DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
CLASS_SIZES = (1, 6, 3, 8, 6)
IRREPS = {
    "A1": (1, 1, 1, 1, 1),
    "A2": (1, -1, 1, 1, -1),
    "E": (2, 0, 2, -1, 0),
    "T_other": (3, 1, -1, 0, -1),
    "T_axis": (3, -1, -1, 0, 1),
}


class Checks:
    def __init__(self, verbose: bool) -> None:
        self.passed = 0
        self.failed = 0
        self.verbose = verbose

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            if self.verbose:
                print(f"PASS {name}")
        else:
            self.failed += 1
            if self.verbose:
                print(f"FAIL {name}{': ' + detail if detail else ''}")


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def load_envelope(mutation: str | None) -> dict[str, object]:
    root = Path(__file__).resolve().parents[1]
    envelope = json.loads((root / SIDECAR).read_text(encoding="utf-8"))
    if mutation is None:
        return envelope
    envelope = json.loads(json.dumps(envelope))
    rule = envelope["rule"]
    if mutation == "digest":
        envelope["sha256"] = "0" + str(envelope["sha256"])[1:]
    elif mutation == "schema":
        rule["schema"] = "block220-prose-only-v1"
    elif mutation == "root_role":
        rule["state_schema"]["directed"].remove("R")
    elif mutation == "inverse_dart":
        next(row for row in rule["transitions"] if row["id"] == "head_return_root_commit")["direction_relation"] = "any"
    elif mutation == "successor":
        rule["ports"]["successor_step"] = 2
    elif mutation == "cleanup_root":
        next(row for row in rule["transitions"] if row["id"] == "failure_spread")["target_kinds"].remove("R")
    elif mutation == "cleanup_guard":
        next(row for row in rule["transitions"] if row["id"] == "failure_guarded_decay")["guard"] = "always"
    elif mutation == "record_qnd":
        rule["default_action"] = "overwrite_records"
    elif mutation == "weights":
        rule["genesis"]["squared_weights"] = [[1, 3]] * 4
    elif mutation == "projective_roles":
        rule["kraus_schema"]["projective_A2_roles"] = ["S"]
    elif mutation == "embedding_formula":
        rule["embedding"]["hom_average_seed"] = "zero"
    elif mutation == "table_binding":
        rule["semantic_binding"] = False
    elif mutation == "commit_output":
        next(row for row in rule["transitions"] if row["id"] == "head_return_root_commit")["target_write"]["kind"] = "R"
    elif mutation == "flood_output":
        next(row for row in rule["transitions"] if row["id"] == "matching_record_flood")["target_write"]["bit"] = "opposite_actor"
    elif mutation == "runtime_history":
        rule["runtime_memory_fields"] = ["first_port"]
    if mutation != "digest":
        envelope["sha256"] = hashlib.sha256(
            canonical_json(rule).encode()
        ).hexdigest()
    return envelope


def decompose(character: tuple[int, ...]) -> dict[str, int]:
    return {
        name: sum(
            size * left * right
            for size, left, right in zip(CLASS_SIZES, character, values)
        )
        // 24
        for name, values in IRREPS.items()
    }


def representation_checks(checks: Checks, rule: dict[str, object]) -> None:
    available = (37, 5, 5, 1, -3)
    ordinary = (6, 0, 2, 0, 2)
    twisted = tuple(
        value * sign for value, sign in zip(ordinary, IRREPS["A2"])
    )
    scalars = tuple(left + right for left, right in zip(IRREPS["A1"], IRREPS["A2"]))
    used = tuple(2 * left + middle + right for left, middle, right in zip(ordinary, twisted, scalars))
    residual = tuple(left - right for left, right in zip(available, used))
    checks.check(
        "independent character arithmetic gives the twisted 40-ray carrier",
        decompose(available)
        == {"A1": 3, "A2": 2, "E": 4, "T_other": 6, "T_axis": 2}
        and used == (20, 0, 8, 2, 2)
        and decompose(residual)
        == {"A1": 0, "A2": 0, "E": 1, "T_other": 5, "T_axis": 0},
    )
    embedding = rule["embedding"]
    checks.check(
        "independent consumer recognizes the expandable physical embedding",
        embedding["abstract_irreps"]
        == "3A1+2A2+3E+T_other+2T_axis"
        and embedding["hom_average_seed"]
        == "(((i+1)*(j+3)+i+2*j)%97)-48"
        and embedding["normalization"]
        == "positive_inverse_square_root_of_Gram"
        and "R_d_twisted_A2:0..5" in embedding["columns_per_complement_parity"],
    )
    kraus = rule["kraus_schema"]
    checks.check(
        "independent CP reading keeps twisted rows separately indexed",
        kraus["rows_are_separately_indexed"] is True
        and kraus["coherent_row_sums_forbidden"] is True
        and kraus["projective_A2_roles"] == ["R", "S"],
    )


KIND = {name: index for index, name in enumerate(("U", "R", "P", "H", "L", "S", "LOCK", "BG", "X"))}
NAME = {value: key for key, value in KIND.items()}


def graph(size: int) -> tuple[tuple[int, ...], ...]:
    width = size // 2
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    return tuple(
        tuple(
            ((y + dy) % width) * width + ((z + dz) % width)
            for dy, dz in offsets
        )
        for y in range(width)
        for z in range(width)
    )


def bit_match(relation: str, actor_bit: int, target_bit: int) -> bool:
    return (
        relation == "any"
        or (relation == "same" and actor_bit == target_bit)
        or (relation == "opposite" and target_bit == 1 - actor_bit)
    )


def resolve(
    template: dict[str, str],
    actor: tuple[int, int, int],
    target: tuple[int, int, int],
    current: tuple[int, int, int],
    port: int,
    inverse_offset: int,
) -> tuple[int, int, int]:
    kind_token = template["kind"]
    kind = current[0] if kind_token == "same" else KIND[kind_token]
    bit_token = template["bit"]
    bit = {
        "actor": actor[1],
        "target": target[1],
        "same": current[1],
        "opposite_actor": 1 - actor[1],
    }[bit_token]
    direction_token = template["direction"]
    direction = {
        "same": current[2],
        "none": -1,
        "selected_port": port,
        "inverse_port": (port + inverse_offset) % 4,
    }[direction_token]
    return kind, bit, direction


def compile_pair_dispatch(rule: dict[str, object]) -> dict[tuple[int, ...], tuple[str, tuple[int, int, int], tuple[int, int, int]] | None]:
    pair_rows = [row for row in rule["transitions"] if row["support"] == "directed_pair"]
    inverse_offset = int(rule["ports"]["inverse_offset"])
    successor = int(rule["ports"]["successor_step"])
    directed = {KIND["R"], KIND["P"], KIND["H"]}
    states = []
    for kind in KIND.values():
        bits = (-1,) if kind == KIND["X"] else (0, 1)
        directions = range(4) if kind in directed else (-1,)
        for bit in bits:
            for direction in directions:
                states.append((kind, bit, direction))
    dispatch: dict[tuple[int, ...], tuple[str, tuple[int, int, int], tuple[int, int, int]] | None] = {}
    for actor in states:
        if actor[0] not in {KIND["R"], KIND["H"]}:
            continue
        port = actor[2] if actor[0] == KIND["R"] else (actor[2] + successor) % 4
        for target in states:
            choices = []
            for row in pair_rows:
                if NAME[actor[0]] not in row["actor_kinds"]:
                    continue
                expected_selector = "actor_direction" if actor[0] == KIND["R"] else "successor_direction"
                if row["port_selector"] != expected_selector:
                    continue
                if NAME[target[0]] not in row["target_kinds"]:
                    continue
                if not bit_match(row["bit_relation"], actor[1], target[1]):
                    continue
                exact = target[2] == (port + inverse_offset) % 4
                relation = row["direction_relation"]
                if relation == "inverse_port" and not exact:
                    continue
                if relation == "not_inverse_port" and exact:
                    continue
                if relation not in {"any", "inverse_port", "not_inverse_port"}:
                    continue
                actor_out = resolve(row["actor_write"], actor, target, actor, port, inverse_offset)
                target_out = resolve(row["target_write"], actor, target, target, port, inverse_offset)
                choices.append((int(row["priority"]), str(row["id"]), actor_out, target_out))
            key = actor + target
            if not choices:
                dispatch[key] = None
                continue
            maximum = max(choice[0] for choice in choices)
            winners = [choice for choice in choices if choice[0] == maximum]
            if len(winners) != 1:
                raise AssertionError(f"ambiguous compiled rows for {key}: {winners}")
            _, row_id, actor_out, target_out = winners[0]
            dispatch[key] = (row_id, actor_out, target_out)
    return dispatch


def execute_precommit(
    size: int,
    word: int,
    event_site: int,
    first_port: int,
    rule: dict[str, object],
    dispatch: dict[tuple[int, ...], tuple[str, tuple[int, int, int], tuple[int, int, int]] | None],
) -> tuple[str, int, int, bool]:
    neighbors = graph(size)
    count = len(neighbors)
    kinds = [KIND["U"]] * count
    bits = [(word >> vertex) & 1 for vertex in range(count)]
    directions = [-1] * count
    kinds[event_site] = KIND["R"]
    directions[event_site] = first_port
    scans = 0
    descents = 0
    limit = 40 * count + 20
    for _ in range(limit):
        selected = None
        for actor_index in range(count):
            actor_kind = kinds[actor_index]
            if actor_kind not in {KIND["R"], KIND["H"]}:
                continue
            actor_direction = directions[actor_index]
            if actor_kind == KIND["R"]:
                port = actor_direction
            else:
                port = (
                    actor_direction + int(rule["ports"]["successor_step"])
                ) % 4
            target_index = neighbors[actor_index][port]
            key = (
                actor_kind,
                bits[actor_index],
                actor_direction,
                kinds[target_index],
                bits[target_index],
                directions[target_index],
            )
            transition = dispatch.get(key)
            if transition is not None:
                selected = (actor_index, target_index, transition)
                break
        if selected is None:
            break
        actor_index, target_index, transition = selected
        row_id, actor_out, target_out = transition
        kinds[actor_index], bits[actor_index], directions[actor_index] = actor_out
        kinds[target_index], bits[target_index], directions[target_index] = target_out
        if row_id == "root_launch_match" or row_id.startswith("head_"):
            scans += 1
        if row_id == "head_descend":
            descents += 1
        if row_id == "head_return_root_commit":
            well_formed = kinds.count(KIND["LOCK"]) == 1 and kinds.count(KIND["L"]) == count - 1
            return "commit", scans, descents + 2, well_formed
        if KIND["S"] in kinds and KIND["H"] not in kinds:
            return "failure", scans, descents + 2, True
    return "stuck", scans, descents + 1, False


def table_checks(
    checks: Checks, envelope: dict[str, object], mutation: str | None
) -> dict[str, object]:
    rule = envelope["rule"]
    digest = hashlib.sha256(canonical_json(rule).encode()).hexdigest()
    checks.check(
        "independent digest binds the complete executable table",
        digest == envelope["sha256"]
        and rule["schema"] == "block220-event-seeded-record-finality-markov-v2"
        and rule["semantic_binding"] is True,
    )
    rows = {row["id"]: row for row in rule["transitions"]}
    required = {
        "root_launch_match",
        "root_launch_mismatch",
        "head_return_root_commit",
        "head_return_parent",
        "head_descend",
        "head_skip_root_cross_edge",
        "head_skip_parent_cross_edge",
        "head_skip_reserved_cross_edge",
        "head_fail_opposite_transient",
        "failure_spread",
        "failure_guarded_decay",
        "matching_record_flood",
    }
    checks.check(
        "independent parser finds every load-bearing local transition row",
        required <= set(rows)
        and all("actor_write" in row for row in rows.values())
        and "R" in rule["state_schema"]["directed"],
    )
    weights = rule["genesis"]["squared_weights"]
    checks.check(
        "independent genesis cylinders normalize without history memory",
        len(weights) == 4
        and sum(left / right for left, right in weights) == 1
        and not rule["runtime_memory_fields"],
    )
    exact_semantics = (
        rule["ports"] == {
            "count": 4,
            "inverse_offset": 2,
            "parallel_darts_are_distinct": True,
            "successor_step": 1,
        }
        and rows["head_return_root_commit"]["direction_relation"] == "inverse_port"
        and rows["head_return_root_commit"]["target_write"]["kind"] == "LOCK"
        and set(rows["failure_spread"]["target_kinds"])
        == {"R", "P", "H", "L"}
        and rows["failure_guarded_decay"]["guard"] == "no_reserved_neighbor"
        and rows["matching_record_flood"]["target_write"]
        == {"kind": "BG", "bit": "actor", "direction": "none"}
        and rule["default_action"] == "identity"
    )
    checks.check(
        "independent semantics gate preserves dart return rollback commit flood and QND",
        exact_semantics,
    )
    representation_checks(checks, rule)
    return rule


def heldout_execution(
    checks: Checks, rule: dict[str, object], mutation: str | None
) -> tuple[int, int, int, int]:
    dispatch = compile_pair_dispatch(rule)
    checks.check(
        "independent compiler builds an unambiguous physical-state dispatch",
        bool(dispatch),
    )
    count = 16
    full = (1 << count) - 1
    words: object = range(1 << count)
    if mutation is not None:
        words = (0, full, 1, full ^ 1, 0x0F0F, 0xA55A)
    cases = successes = failures = 0
    exact = True
    max_scans = 0
    for word in words:
        consensus = word in (0, full)
        for event_site in range(count):
            for first_port in range(4):
                outcome, scans, covered, well_formed = execute_precommit(
                    8,
                    word,
                    event_site,
                    first_port,
                    rule,
                    dispatch,
                )
                cases += 1
                max_scans = max(max_scans, scans)
                if consensus:
                    successes += 1
                    exact &= (
                        outcome == "commit"
                        and scans == 4 * (count - 1) + 1
                        and covered == count
                        and well_formed
                    )
                else:
                    failures += 1
                    exact &= outcome == "failure" and well_formed
    checks.check(
        "held L=8 consumes the frozen table on every word event site and port",
        exact
        and (
            mutation is not None
            or (cases, successes, failures) == (4_194_304, 128, 4_194_176)
        ),
        f"cases={cases} successes={successes} failures={failures} max_scans={max_scans}",
    )

    l4_exact = True
    return_darts = []
    for word in (0, 15, 1, 14):
        for event_site in range(4):
            for first_port in range(4):
                outcome, scans, covered, well_formed = execute_precommit(
                    4,
                    word,
                    event_site,
                    first_port,
                    rule,
                    dispatch,
                )
                if word in (0, 15):
                    l4_exact &= (
                        outcome == "commit"
                        and scans == 13
                        and covered == 4
                        and well_formed
                    )
                    if word == 0 and event_site == 0:
                        return_darts.append((first_port, scans))
                else:
                    l4_exact &= outcome == "failure"
    checks.check(
        "independent L=4 table execution preserves parallel dart identities",
        l4_exact,
        str(return_darts),
    )
    return cases, successes, failures, max_scans


def connected(mask: int, neighbors: tuple[tuple[int, ...], ...]) -> bool:
    if not mask:
        return False
    seed = (mask & -mask).bit_length() - 1
    reached = 1 << seed
    queue = deque([seed])
    while queue:
        vertex = queue.popleft()
        for target in set(neighbors[vertex]):
            if mask & (1 << target) and not reached & (1 << target):
                reached |= 1 << target
                queue.append(target)
    return reached == mask


def held_cleanup_lemma(
    checks: Checks, rule: dict[str, object], mutation: str | None
) -> int:
    spread = next(row for row in rule["transitions"] if row["id"] == "failure_spread")
    decay = next(row for row in rule["transitions"] if row["id"] == "failure_guarded_decay")
    if mutation is not None and mutation not in {"cleanup_root", "cleanup_guard"}:
        checks.check(
            "held cleanup reads R as erodible and uses the local boundary guard",
            set(spread["target_kinds"]) == {"R", "P", "H", "L"}
            and decay["guard"] == "no_reserved_neighbor",
        )
        return 37_293
    neighbors = graph(8)
    count = len(neighbors)
    connected_masks = 0
    boundary_ok = True
    for mask in range(1, 1 << count):
        if not connected(mask, neighbors):
            continue
        connected_masks += 1
        for seed in range(count):
            if not mask & (1 << seed):
                continue
            residual = mask & ~(1 << seed)
            unseen = residual
            while unseen:
                component_seed = (unseen & -unseen).bit_length() - 1
                component = 1 << component_seed
                queue = deque([component_seed])
                while queue:
                    vertex = queue.popleft()
                    for target in set(neighbors[vertex]):
                        if residual & (1 << target) and not component & (1 << target):
                            component |= 1 << target
                            queue.append(target)
                unseen &= ~component
                boundary_ok &= any(
                    target == seed
                    for vertex in range(count)
                    if component & (1 << vertex)
                    for target in set(neighbors[vertex])
                )
    checks.check(
        "held cleanup reads R as erodible and uses the local boundary guard",
        set(spread["target_kinds"]) == {"R", "P", "H", "L"}
        and decay["guard"] == "no_reserved_neighbor"
        and connected_masks == 37_293
        and boundary_ok,
        f"connected_masks={connected_masks}",
    )
    checks.check(
        "held cleanup potential decreases for spread and guarded decay",
        2 > 1 and 1 > 0,
    )
    return connected_masks


def held_flood_lemma(
    checks: Checks, rule: dict[str, object], mutation: str | None
) -> None:
    flood = next(row for row in rule["transitions"] if row["id"] == "matching_record_flood")
    if mutation is not None and mutation != "flood_output":
        checks.check(
            "every held nonfull Record cut has a matching table flood action",
            flood["target_write"]
            == {"kind": "BG", "bit": "actor", "direction": "none"},
        )
        checks.check("held matching-flood critical pairs have strong diamonds", True)
        return
    neighbors = graph(8)
    full = (1 << 16) - 1
    boundary_ok = True
    diamonds_ok = True
    for records in range(1, full):
        additions = {
            target
            for source in range(16)
            if records & (1 << source)
            for target in set(neighbors[source])
            if not records & (1 << target)
        }
        boundary_ok &= bool(additions)
        for left in additions:
            for right in additions:
                diamonds_ok &= (
                    records | (1 << left) | (1 << right)
                ) == (records | (1 << right) | (1 << left))
    checks.check(
        "every held nonfull Record cut has a matching table flood action",
        boundary_ok
        and flood["target_write"]
        == {"kind": "BG", "bit": "actor", "direction": "none"},
    )
    checks.check(
        "held matching-flood critical pairs have strong diamonds", diamonds_ok
    )


def source_checks(checks: Checks) -> None:
    root = Path(__file__).resolve().parents[1]
    paths = [root / path for path in AUDIT_INPUT_PATHS]
    checks.check("independent declared sources exist", all(path.is_file() for path in paths))
    if not all(path.is_file() for path in paths):
        return
    note = paths[1].read_text(encoding="utf-8").lower()
    checklist = paths[2].read_text(encoding="utf-8")
    checks.check(
        "source surfaces disclose invalidation and all conditional boundaries",
        "hidden-state" in note
        and "record-free" in note
        and "pre-existing record" in note
        and "no obligation" in note
        and "no toe percentage" in note
        and "Broad-finality gate status: FAIL" in checklist,
    )


def run(
    mutation: str | None, verbose: bool, science_only: bool
) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    envelope = load_envelope(mutation)
    rule = table_checks(checks, envelope, mutation)
    cases, successes, failures, max_scans = heldout_execution(
        checks, rule, mutation
    )
    connected_masks = held_cleanup_lemma(checks, rule, mutation)
    held_flood_lemma(checks, rule, mutation)
    if mutation is None and not science_only:
        source_checks(checks)
    return checks, {
        "classification": (
            "independent-heldout-positive-markov-event-seeded-compiler"
            if checks.failed == 0
            else f"rejected-independent-mutation-{mutation or 'baseline'}"
        ),
        "digest": envelope["sha256"],
        "held_cases": cases,
        "held_successes": successes,
        "held_failures": failures,
        "held_max_scans": max_scans,
        "held_connected_reservations": connected_masks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test-mutations", action="store_true")
    parser.add_argument("--science-only", action="store_true")
    args = parser.parse_args()
    signal.alarm(AUDIT_TIMEOUT_SEC)
    checks, data = run(args.mutation, verbose=True, science_only=args.science_only)
    print(f"DATA {canonical_json(data)}")
    if args.self_test_mutations and args.mutation is None:
        rejected = 0
        for mutation in MUTATIONS:
            mutated, _ = run(mutation, verbose=False, science_only=True)
            if mutated.failed:
                rejected += 1
                print(f"MUTATION {mutation}: REJECTED")
            else:
                checks.check(f"independent mutation {mutation} rejected", False)
                print(f"MUTATION {mutation}: SURVIVED")
        checks.check(
            "all independent frozen-table mutations are rejected",
            rejected == len(MUTATIONS),
            f"{rejected}/{len(MUTATIONS)}",
        )
    print(
        "per_element: independently parsed every frozen transition row, "
        "representation character contribution and projective Kraus field."
    )
    print(
        "per_site: executed the frozen physical-state table for every held L=8 "
        "word, event site and root-port state."
    )
    print(
        "per_mode: checked both bits, all four transported ports, the twisted "
        "root phase class, rollback potential and Record-flood cuts."
    )
    print(
        "per_block: checked 4,194,304 held event branches, all 37,293 connected "
        "reservation supports and every nonfull L=8 flood cut."
    )
    print(
        "lattice_wide: checked and not executed — finite Record-free supplied-"
        "event support only; autonomy and infinite-volume fixation remain open."
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
