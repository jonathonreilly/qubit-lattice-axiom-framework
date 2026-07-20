#!/usr/bin/env python3
"""Cycle 514 symbolic/per-axis diagnostic for the Route-C Q6 prefix.

This runner diagnoses the under-instrumented Cycle-513 axis gate.  Dry mode
binds the packaged Cycle-512/513 evidence and executes only local algebra,
geometry, authorization, and quarantine checks.  The separately gated mode
builds all three axial preparations only through the nine update-3
*pre-collision* product factors.  It performs no generic collision growth.

For matter, the gated diagnostic extends the Cycle-512 exact
Q(zeta_9)[z] contact-tag support through the third free word after applying
each update-2 I/D/X branch.  Collision and emitter sine/cosine factors are
named supplied nonzero premises.  They are not used as cancellation oracles,
and no claim is made about cancellations across the sum of structural
branches.  Machine-exact zeros and magnitude diagnostics never gate support.

All later surfaces--update-3 collision growth and mediator stream, joint
Schmidt analysis, inverse/order/orbit, depth five, response, deletion, train,
and held--remain false/open.

Authority: none.  Audit: unset.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
import os
from pathlib import Path
import resource
import sys
import time
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_route_c_q6_generic_factor_growth_preflight_cycle513_2026_07_20 as c513

c512 = c513.c512

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
CLI_MODES = ("dry-contract", "symbolic-axis-diagnostic")

CYCLE513_RUNNER = ROOT / "scripts/physical_route_c_q6_generic_factor_growth_preflight_cycle513_2026_07_20.py"
CYCLE513_DRY = ROOT / "outputs/physical_route_c_q6_generic_factor_growth_preflight_cycle513_2026_07_20.log"
CYCLE513_ATTEMPT1 = ROOT / "outputs/physical_route_c_q6_generic_factor_growth_scout_cycle513_attempt1_2026_07_20.log"
CYCLE513_RECEIPT = ROOT / "outputs/physical_route_c_q6_generic_factor_growth_scout_cycle513_attempt1_receipt_2026_07_20.json"
CYCLE513_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUTE_C_Q6_GENERIC_FACTOR_GROWTH_CYCLE513_ATTEMPT1_FAILURE_NOTE_2026-07-20.md"
CYCLE512_RUNNER = ROOT / "scripts/physical_route_c_q6_factorized_resource_scout_cycle512_2026_07_20.py"
CYCLE512_RAW = ROOT / "outputs/physical_route_c_q6_factorized_resource_scout_cycle512_2026_07_20.log"
CYCLE512_RECEIPT = ROOT / "outputs/physical_route_c_q6_factorized_resource_scout_cycle512_receipt_2026_07_20.json"
CYCLE512_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUTE_C_Q6_FACTORIZED_RESOURCE_SCOUT_CYCLE512_NOTE_2026-07-20.md"

STRICT_FILE_HASHES = {
    CYCLE513_RUNNER: "84ccd28c0ef428a851d0f9328ba7988c13a59ac1627d218e1ca9b9ee0b01a297",
    CYCLE513_DRY: "e6c92ffb2158230afcb755bc7ad987c25f0eefa83aa444eb4bcbd5c3566fb762",
    CYCLE513_ATTEMPT1: "e4ac928931cdd77445a690e767b64e56b70118f12a467e667c8c3e5fc35d5cd7",
    CYCLE513_RECEIPT: "fbae7dfced0ace45d490651dc4a36c5018743be91ac0792df8651d2f03a68fd3",
    CYCLE513_NOTE: "4330e0b21ba86f8d5a12703292f35fa1e8fa7fc5b9b007a3b63a208e21745b1f",
    CYCLE512_RUNNER: "d90525f7c25c92762851ac07b9ea58c28123c378fd0fdea6ce3ab565108834fe",
    CYCLE512_RAW: "203a24590329119b44ce13f2c3c39581f011457cd4db217e62c3f985ea840f67",
    CYCLE512_RECEIPT: "40de95deab66e3d32113d1f91cb14d9a1ac92e96fc7cae27b2ea87c56980b983",
    CYCLE512_NOTE: "f027e124f71450e3d24c9961b74c8445129621c52a1c2ea473a03ab7aef28506",
}

EXPECTED_CYCLE513_RECEIPT_SCHEMA = (
    "cycle513-route-c-q6-generic-factor-growth-attempt1-receipt-v1"
)
EXPECTED_CYCLE513_STATUS = (
    "factor-growth-scout-attempt1-failed-closed-axis1-compound-fixture-mismatch"
)
EXPECTED_CYCLE512_RECEIPT_SCHEMA = (
    "cycle512-route-c-q6-factorized-resource-scout-receipt-v1"
)
EXPECTED_CYCLE512_STATUS = (
    "update2-unpruned-packed-numerical-rank9-qualified-depth5-open"
)

SCOUT_AUTHORIZATION_ENV = c512.SCOUT_AUTHORIZATION_ENV
SCOUT_AUTHORIZATION_TOKEN = c512.SCOUT_AUTHORIZATION_TOKEN
RUNNER_INTEGRITY_ENV = "CYCLE514_ROUTE_C_Q6_SYMBOLIC_AXIS_DIAGNOSTIC_RUNNER_SHA256"
ALL_AUTHORIZATION_ENVIRONMENTS = c512.ALL_AUTHORIZATION_ENVIRONMENTS

RSS_LIMIT_BYTES = c512.RSS_LIMIT_BYTES
RSS_PREALLOC_ABORT_BYTES = c512.RSS_PREALLOC_ABORT_BYTES
WALL_LIMIT_SECONDS = c512.WALL_LIMIT_SECONDS
WALL_GRACE_SECONDS = c512.WALL_GRACE_SECONDS
FRAME_RESIDUAL_CEILING = 1e-11
SUPPORT_DIAGNOSTIC_CEILING = c512.SUPPORT_DIAGNOSTIC_CEILING
HISTORICAL_COUNTS = {
    "compact_DX_matter_support_only_upper": 581,
    "Cycle513_axis0_generic_descriptor_forecast": 461,
    "unpreserved_unreconciled_helper": 453,
}
EXPECTED_CANDIDATE_CELL_COUNTS = c513.EXPECTED_COMPACT_CANDIDATE_CELLS
EXPECTED_MATTER_FACTOR_COUNTS = {
    "II": (46425, 30207, 176286),
    "ID": (1800, 1620, 3456),
    "IX": (1800, 1620, 3456),
    "DI": (1800, 1620, 3456),
    "XI": (1800, 1620, 3456),
    "DD": (36, 36, 36),
    "DX": (36, 36, 36),
    "XD": (36, 36, 36),
    "XX": (36, 36, 36),
}
EXPECTED_MEDIATOR_FACTOR_SUPPORT = {
    label: (4096 if label == "II" else 1024 if label.count("I") == 1 else 256)
    for label in c512.EXPECTED_UPDATE2_FACTOR_LABELS
}
EXPECTED_MEDIATOR_BRANCH_SUPPORT = {
    label: (729 if label == "II" else 243 if label.count("I") == 1 else 81)
    for label in c512.EXPECTED_UPDATE2_FACTOR_LABELS
}
PREFIX_PREDICATE_NAMES = (
    "update1_collision_is_identity",
    "update2_active_cell_audit",
    "update2_factor_labels_match",
    "update2_factor_stored_supports_match",
    "stored_matter_support_updates0_1_2_II3_match",
    "stored_mediator_support_updates0_1_2_II3_match",
)
GEOMETRY_PREDICATE_NAMES = (
    "geometry:actual_union_equals_expected",
    "geometry:actual_union_has_14_cells",
    "geometry:actual_union_is_inside_fixed_shell",
    "geometry:all_omitted_cell_K_actions_vanish",
    "geometry:per_label_candidate_counts_match_historical_diagnostic",
)
AXIS_PREDICATE_NAMES = (
    *PREFIX_PREDICATE_NAMES,
    *GEOMETRY_PREDICATE_NAMES,
    "all_factor_exact_stored_and_finite_predicates",
)

MatterRay = c512.MatterRay
MediatorRay = c512.MediatorRay
ExactMatterTags = c512.ExactMatterTags
Factor = tuple[MatterRay, MediatorRay, str]
MediatorMonomial = tuple[int, int, int]
MediatorHistory = tuple[MediatorMonomial, tuple[str, ...]]
MediatorHistories = dict[c512.MediatorConfiguration, set[MediatorHistory]]


class ResourceWall(RuntimeError):
    """A technical execution cap, never a physical conclusion."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def resource_checkpoint(started: float, label: str, projected_bytes: int = 0) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_PREALLOC_ABORT_BYTES:
        raise ResourceWall(f"RSS preallocation guard reached at {label}: {rss}")
    if rss + projected_bytes >= RSS_PREALLOC_ABORT_BYTES:
        raise ResourceWall(
            f"projected allocation guard reached at {label}: "
            f"rss={rss}, projected={projected_bytes}"
        )
    if swap_count() != 0:
        raise ResourceWall(f"nonzero process swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "estimated_next_allocation_bytes": projected_bytes,
        "process_swap_count": swap_count(),
    }


def evidence_controls() -> dict:
    actual = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    failures = {
        str(path.relative_to(ROOT)): {
            "expected": expected,
            "actual": actual[str(path.relative_to(ROOT))],
        }
        for path, expected in STRICT_FILE_HASHES.items()
        if actual[str(path.relative_to(ROOT))] != expected
    }
    c513_receipt = json.loads(CYCLE513_RECEIPT.read_text(encoding="utf-8"))
    c512_receipt = json.loads(CYCLE512_RECEIPT.read_text(encoding="utf-8"))
    attempt = c513_receipt.get("authorized_attempt1", {})
    return {
        "strict_file_hashes": actual,
        "strict_hash_failures": failures,
        "Cycle513_receipt_schema": c513_receipt.get("schema"),
        "Cycle513_receipt_status": c513_receipt.get("status"),
        "Cycle513_receipt_pass": c513_receipt.get("pass"),
        "Cycle513_dry_tests": (
            c513_receipt.get("dry_contract", {}).get("tests_passed"),
            c513_receipt.get("dry_contract", {}).get("tests_total"),
        ),
        "Cycle513_attempt_exit_code": attempt.get("process_exit_code"),
        "Cycle513_attempt_error": attempt.get("error"),
        "Cycle513_single_invocation_consumed": attempt.get(
            "single_authorized_invocation_consumed"
        ),
        "Cycle513_old_invocation_reusable": c513_receipt.get("diagnosis", {}).get(
            "old_single_invocation_may_be_reused"
        ),
        "Cycle513_cause_proven": c513_receipt.get("diagnosis", {}).get(
            "cause_proven"
        ),
        "Cycle513_quarantine": c513_receipt.get("quarantine"),
        "Cycle512_receipt_schema": c512_receipt.get("schema"),
        "Cycle512_receipt_status": c512_receipt.get("status"),
        "Cycle512_receipt_pass": c512_receipt.get("pass"),
        "Cycle512_all_axis_rank9": c512_receipt.get("all_axis_Schmidt", {}).get(
            "pass"
        ),
    }


def frozen_contract_matches() -> bool:
    frozen = c512.c511.authorization_contract()["scout"]
    return (
        frozen["environment"] == SCOUT_AUTHORIZATION_ENV
        and frozen["exact_token"] == SCOUT_AUTHORIZATION_TOKEN
        and frozen["scope"]
        == "RouteC8 index0 intact L15 middle-beta resource sentinel only"
        and frozen["science_rows"] == 0
        and frozen["response_quarantined"] is True
        and frozen["selector"] is False
        and frozen["refit"] is False
        and frozen["resource_ceiling"]
        == {
            "wall_seconds": int(WALL_LIMIT_SECONDS),
            "RSS_bytes": RSS_LIMIT_BYTES,
            "swap_count": 0,
        }
    )


def authorization_inputs_allowed(
    present: tuple[str, ...],
    values: dict[str, str | None],
    integrity_present: bool,
    integrity_value: str | None,
    runner_sha: str,
    contract_matches: bool,
) -> bool:
    return (
        present == (SCOUT_AUTHORIZATION_ENV,)
        and values.get(SCOUT_AUTHORIZATION_ENV) == SCOUT_AUTHORIZATION_TOKEN
        and integrity_present
        and integrity_value == runner_sha
        and contract_matches
    )


def authorization_decision(mode: str) -> tuple[bool, dict]:
    present = tuple(name for name in ALL_AUTHORIZATION_ENVIRONMENTS if name in os.environ)
    values = {name: os.environ.get(name) for name in present}
    integrity_present = RUNNER_INTEGRITY_ENV in os.environ
    integrity_value = os.environ.get(RUNNER_INTEGRITY_ENV)
    runner_sha = file_sha(Path(__file__))
    contract_matches = frozen_contract_matches()
    common = {
        "mode": mode,
        "present_authorization_variables": present,
        "runner_integrity_variable_present": integrity_present,
        "presence_even_empty_rejected": True,
        "frozen_Cycle511_scout_contract_matches": contract_matches,
    }
    if mode == "dry-contract":
        return not present and not integrity_present, common
    allowed = authorization_inputs_allowed(
        present,
        values,
        integrity_present,
        integrity_value,
        runner_sha,
        contract_matches,
    )
    return allowed, {
        **common,
        "runner_integrity_sha256_match": integrity_value == runner_sha,
        "current_runner_sha256": runner_sha,
        "exact_frozen_Cycle511_scout_token_match": values.get(
            SCOUT_AUTHORIZATION_ENV
        )
        == SCOUT_AUTHORIZATION_TOKEN,
        "new_token_or_scope_introduced": False,
        "single_invocation": True,
        "scope": "RouteC8 index0 intact L15 middle-beta resource sentinel only",
        "implementation_scope": (
            "one hash-bound Cycle514 symbolic all-axis update3-pre-collision "
            "diagnostic invocation; no generic collision growth"
        ),
        "science_rows": 0,
        "response_quarantined": True,
        "held_rows": 0,
        "selector": False,
        "refit": False,
    }


def exact_copy_tag(tag: c512.ContactTag, sign: int = 1) -> c512.ContactTag:
    return {
        power: c512.cyclotomic_scale(value, sign) for power, value in tag.items()
    }


def exact_apply_branch_term(
    ray: ExactMatterTags,
    site: tuple[tuple[int, int, int], int, int, int, int],
    choice: str,
) -> ExactMatterTags:
    if choice == "I":
        return {pair: dict(tag) for pair, tag in ray.items()}
    cell, incoming, outgoing, _incoming_slot, _outgoing_slot = site
    old = c512.matter_mode(cell, incoming)
    new = c512.matter_mode(cell, outgoing)
    output: ExactMatterTags = {}
    for pair, tag in ray.items():
        if old not in pair or new in pair:
            continue
        target = pair
        if choice == "X":
            values = list(pair)
            values[values.index(old)] = new
            target = tuple(sorted(values))  # type: ignore[assignment]
        elif choice != "D":
            raise ValueError(f"unknown exact branch choice {choice}")
        c512.add_contact_tag(output, target, dict(tag))
    return output


def exact_axis_prefix_tags(axis: int) -> tuple[ExactMatterTags, dict]:
    matter0 = c512.exact_initial_matter_tags(axis)
    matter1, raw1 = c512.exact_forward_matter_tag_word(matter0)
    matter2, raw2 = c512.exact_forward_matter_tag_word(matter1)
    return matter2, {
        "raw_coin_contributions_updates1_2": (raw1, raw2),
        "stored_keys_updates0_1_2": (
            len(matter0),
            len(matter1),
            len(matter2),
        ),
        "exact_support_updates0_1_2": (
            c512.exact_tag_support(matter0),
            c512.exact_tag_support(matter1),
            c512.exact_tag_support(matter2),
        ),
    }


def exact_update3_branch_tags(
    matter2: ExactMatterTags,
    prefix_meta: dict,
    axis: int,
    choices: tuple[str, str],
) -> tuple[ExactMatterTags, dict]:
    branched = matter2
    scalar_factors = []
    for position, (choice, site) in enumerate(
        zip(choices, c512.FROZEN_UPDATE2_ACTIVE_SITES[axis])
    ):
        branched = exact_apply_branch_term(branched, site, choice)
        scalar_factors.append(
            {
                "site_index": position,
                "cell": site[0],
                "choice": choice,
                "factor": {
                    "I": "1",
                    "D": "cos(theta)-1",
                    "X": "i*sin(theta)",
                }[choice],
            }
        )
    matter3, raw3 = c512.exact_forward_matter_tag_word(branched)
    return matter3, {
        "raw_coin_contributions_updates1_2_3": (
            *prefix_meta["raw_coin_contributions_updates1_2"],
            raw3,
        ),
        "stored_keys_updates0_1_2_branch_3": (
            *prefix_meta["stored_keys_updates0_1_2"],
            len(branched),
            len(matter3),
        ),
        "exact_support_updates0_1_2_branch_3": (
            *prefix_meta["exact_support_updates0_1_2"],
            c512.exact_tag_support(branched),
            c512.exact_tag_support(matter3),
        ),
        "collision_scalar_word": tuple(scalar_factors),
        "collision_scalar_nonzero_status": "supplied nonzero premise; not proved by tag oracle",
        "cross_branch_cancellation_oracle": False,
    }


def advance_mediator_history(
    history: MediatorHistory,
    delta: MediatorMonomial,
    token: str,
) -> MediatorHistory:
    monomial, word = history
    return (
        tuple(monomial[index] + delta[index] for index in range(3)),
        word + (token,),
    )  # type: ignore[return-value]


def add_mediator_history(
    target: MediatorHistories,
    configuration: c512.MediatorConfiguration,
    history: MediatorHistory,
) -> None:
    target.setdefault(configuration, set()).add(history)


def named_emitter_histories(
    ray: MediatorHistories, update: int
) -> MediatorHistories:
    geometry = c512.c511.c509.ROUTE_C_TRAIN
    output = {configuration: set(histories) for configuration, histories in ray.items()}
    for emitter_index, (source, direction) in enumerate(
        zip(geometry.source_cells, geometry.inward_directions)
    ):
        parked = c512.mediator_mode(source, 0)
        active = c512.mediator_mode(source, 1 + direction)
        following: MediatorHistories = {}
        for configuration, histories in output.items():
            occupied_parked = parked in configuration
            occupied_active = active in configuration
            if occupied_parked == occupied_active:
                for history in histories:
                    add_mediator_history(
                        following,
                        configuration,
                        advance_mediator_history(
                            history, (0, 0, 0), f"E{update}.{emitter_index}:1"
                        ),
                    )
                continue
            old, new = (parked, active) if occupied_parked else (active, parked)
            moved = c512.canonical_mediator(
                new if value == old else value for value in configuration
            )
            for history in histories:
                add_mediator_history(
                    following,
                    configuration,
                    advance_mediator_history(
                        history, (1, 0, 0), f"E{update}.{emitter_index}:C"
                    ),
                )
                add_mediator_history(
                    following,
                    moved,
                    advance_mediator_history(
                        history, (0, 1, 0), f"E{update}.{emitter_index}:S"
                    ),
                )
        output = following
    return output


def named_mediator_stream(ray: MediatorHistories) -> MediatorHistories:
    output: MediatorHistories = {}
    for configuration, histories in ray.items():
        moved = c512.stream_mediator_configuration(configuration)
        for history in histories:
            add_mediator_history(output, moved, history)
    return output


def named_mediator_factor_term(
    ray: MediatorHistories,
    site: tuple[tuple[int, int, int], int, int, int, int],
    choice: str,
    position: int,
) -> MediatorHistories:
    cell, _incoming, _outgoing, incoming_slot, outgoing_slot = site
    old = c512.mediator_mode(cell, incoming_slot)
    new = c512.mediator_mode(cell, outgoing_slot)
    output: MediatorHistories = {}
    scalar_delta = {
        "I": (0, 0, 0),
        "D": (0, 0, 1),
        "X": (0, 1, 0),
    }[choice]
    for configuration, histories in ray.items():
        if choice == "I":
            target = configuration
        elif old not in configuration:
            continue
        elif choice == "D":
            target = configuration
        else:
            target = c512.canonical_mediator(
                new if value == old else value for value in configuration
            )
        for history in histories:
            add_mediator_history(
                output,
                target,
                advance_mediator_history(
                    history, scalar_delta, f"B{position}:{choice}"
                ),
            )
    return output


def named_mediator_factor_oracle(axis: int, label: str) -> tuple[set, dict]:
    initial_configuration = next(iter(c512.initial_mediator_ray()))
    ray: MediatorHistories = {
        initial_configuration: {((0, 0, 0), ("initial",))}
    }
    stage_counts = [("initial", len(ray))]
    ray = named_emitter_histories(ray, 1)
    stage_counts.append(("after_emitter1", len(ray)))
    ray = named_mediator_stream(ray)
    stage_counts.append(("after_stream1", len(ray)))
    ray = named_emitter_histories(ray, 2)
    stage_counts.append(("after_emitter2", len(ray)))
    for position, (choice, site) in enumerate(
        zip(label, c512.FROZEN_UPDATE2_ACTIVE_SITES[axis])
    ):
        ray = named_mediator_factor_term(ray, site, choice, position)
    stage_counts.append(("after_update2_branch", len(ray)))
    ray = named_mediator_stream(ray)
    stage_counts.append(("after_stream2", len(ray)))
    ray = named_emitter_histories(ray, 3)
    stage_counts.append(("after_emitter3_precollision", len(ray)))
    history_multiplicities = Counter(len(histories) for histories in ray.values())
    monomial_multiplicities = Counter(
        len({history[0] for history in histories}) for histories in ray.values()
    )
    expected_final = EXPECTED_MEDIATOR_FACTOR_SUPPORT[label]
    expected_branch = EXPECTED_MEDIATOR_BRANCH_SUPPORT[label]
    predicates = {
        "named_history_prefix_counts_match": tuple(count for _name, count in stage_counts[:4])
        == (1, 64, 64, 729),
        "named_history_branch_and_stream_counts_match": tuple(
            count for _name, count in stage_counts[4:6]
        )
        == (expected_branch, expected_branch),
        "named_history_final_support_matches": len(ray) == expected_final,
        "one_history_per_configuration": history_multiplicities == {1: len(ray)},
        "one_monomial_per_configuration": monomial_multiplicities == {1: len(ray)},
    }
    return set(ray), {
        "predicates": predicates,
        "stage_configuration_counts": tuple(stage_counts),
        "expected_branch_support": expected_branch,
        "expected_final_support": expected_final,
        "actual_final_support": len(ray),
        "history_multiplicity_histogram": dict(sorted(history_multiplicities.items())),
        "monomial_multiplicity_histogram": dict(
            sorted(monomial_multiplicities.items())
        ),
        "named_monomial_basis": (
            "C=cos(theta)",
            "S=i*sin(theta)",
            "D=cos(theta)-1",
        ),
        "C_S_D_nonzero": "supplied premise",
        "algebraic_relation_between_C_S_D_needed": False,
        "reason_no_relation_needed": "one named history and one monomial per configuration",
        "numerical_amplitudes_consulted": False,
        "cancellation_oracle": False,
    }


def build_update3_pre_collision_factors(
    axis: int,
    coin: np.ndarray,
    angle: float,
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    partial_rows: list[dict] | None = None,
) -> tuple[tuple[Factor, ...], dict]:
    matter0 = c512.initial_matter_ray(axis)
    mediator0 = c512.initial_mediator_ray()
    matter1 = c512.forward_matter_word(matter0, coin)
    mediator1_pre = c512.apply_emitters(mediator0, angle)
    update1_identity = c512.collision_is_identity_on_product(
        matter1, mediator1_pre, lookup
    )
    mediator1 = c512.apply_mediator_stream(mediator1_pre)
    matter2 = c512.forward_matter_word(matter1, coin)
    mediator2_pre = c512.apply_emitters(mediator1, angle)
    active = c512.update2_active_site_audit(
        axis, matter2, mediator2_pre, lookup, angle
    )

    factors = []
    update2_rows = []
    for choices in product(("I", "D", "X"), repeat=2):
        matter = matter2
        mediator = mediator2_pre
        for choice, site, local_row in zip(
            choices, c512.FROZEN_UPDATE2_ACTIVE_SITES[axis], active["local_rows"]
        ):
            coefficient = 1 + 0j
            if choice == "D":
                coefficient = local_row["diagonal_coefficient"] - 1
            elif choice == "X":
                coefficient = local_row["exchange_coefficient"]
            matter = c512.apply_matter_factor_term(matter, site, choice, coefficient)
            mediator = c512.apply_mediator_factor_term(mediator, site, choice)
        label = "".join(choices)
        mediator = c512.apply_mediator_stream(mediator)
        update2_rows.append((label, len(matter), len(mediator)))
        matter3 = c512.forward_matter_word(matter, coin)
        mediator3 = c512.apply_emitters(mediator, angle)
        factors.append((matter3, mediator3, label))
        if partial_rows is not None:
            partial_rows.append(
                {
                    "label": label,
                    "matter_stored_keys": len(matter3),
                    "mediator_stored_keys": len(mediator3),
                    "completed": True,
                }
            )

    predicates = {
        "update1_collision_is_identity": update1_identity,
        "update2_active_cell_audit": active["pass"],
        "update2_factor_labels_match": tuple(row[0] for row in update2_rows)
        == c512.EXPECTED_UPDATE2_FACTOR_LABELS,
        "update2_factor_stored_supports_match": tuple(
            (row[1], row[2]) for row in update2_rows
        )
        == c512.EXPECTED_UPDATE2_FACTOR_SUPPORTS,
        "stored_matter_support_updates0_1_2_II3_match": (
            len(matter0), len(matter1), len(matter2), len(factors[0][0])
        )
        == c512.DECLARED_STORED_MATTER_KEYS_BY_UPDATE[:4],
        "stored_mediator_support_updates0_1_2_II3_match": (
            len(mediator0), len(mediator1_pre), len(mediator2_pre), len(factors[0][1])
        )
        == c512.DECLARED_UNCOUPLED_MEDIATOR_KEYS_BY_UPDATE[:4],
    }
    return tuple(factors), {
        "predicates": predicates,
        "update2_factor_rows": tuple(update2_rows),
        "stored_matter_support_updates0_1_2_II3": (
            len(matter0), len(matter1), len(matter2), len(factors[0][0])
        ),
        "stored_mediator_support_updates0_1_2_II3": (
            len(mediator0), len(mediator1_pre), len(mediator2_pre), len(factors[0][1])
        ),
    }


def support_signature_sets(ray: dict, decoder: Callable) -> dict:
    masks: dict[tuple[int, int, int], set[int]] = defaultdict(set)
    occupied: Counter[tuple[int, int, int]] = Counter()
    for configuration in ray:
        local: dict[tuple[int, int, int], int] = defaultdict(int)
        for mode in configuration:
            cell, slot = decoder(mode)
            local[cell] |= 1 << slot
        for cell, mask in local.items():
            masks[cell].add(mask)
            occupied[cell] += 1
    for cell in tuple(masks):
        if occupied[cell] < len(ray):
            masks[cell].add(0)
    return masks


def expected_axis_touched(axis: int) -> set[tuple[int, int, int]]:
    shell = set(c513.shell_geometry())
    center = c512.c511.c509.ROUTE_C_TRAIN.probe_center
    return shell - {
        tuple(
            int(
                center[index]
                + 4 * c512.c511.c210.DIRECTIONS[direction, index]
            )
            for index in range(3)
        )
        for direction in range(6)
        if direction // 2 != axis
    }


def geometry_witness(
    factors: tuple[Factor, ...],
    lookup: Callable[[int, int], tuple[tuple[int, int, complex], ...]],
    axis: int,
    partial_rows: list[dict] | None = None,
) -> dict:
    shell = set(c513.shell_geometry())
    actual_union = set()
    per_label = []
    first_omitted_witness = None
    omitted_failures = 0
    all_cells = tuple(c512.linear_cell(index) for index in range(c512.CELL_COUNT))
    for matter, mediator, label in factors:
        matter_masks = support_signature_sets(matter, c512.decode_matter_mode)
        mediator_masks = support_signature_sets(mediator, c512.decode_mediator_mode)
        touched = set()
        for cell in set(matter_masks) & set(mediator_masks):
            for matter_mask in matter_masks[cell]:
                for mediator_mask in mediator_masks[cell]:
                    if lookup(matter_mask, mediator_mask) != (
                        (matter_mask, mediator_mask, 1 + 0j),
                    ):
                        touched.add(cell)
        actual_union.update(touched)
        matter_pairs = set()
        for pair in matter:
            occupied_cells = {
                c512.decode_matter_mode(mode)[0] for mode in pair
            } & touched
            matter_pairs.update(combinations(sorted(occupied_cells), 2))
        label_row = {
            "label": label,
            "actual_touched_cells": tuple(sorted(touched)),
            "actual_matter_cooccupied_pairs": tuple(sorted(matter_pairs)),
            "candidate_cell_count_C_j": len(touched),
            "matter_cooccupied_pair_count_P_j": len(matter_pairs),
            "historical_compact_DX_expression": 1
            + 2 * len(touched)
            + 4 * len(matter_pairs),
            "historical_count_is_gate": False,
        }
        per_label.append(label_row)
        if partial_rows is not None:
            partial_rows.append(label_row)
        for cell in all_cells:
            if cell in shell:
                continue
            for matter_mask in matter_masks.get(cell, {0}):
                for mediator_mask in mediator_masks.get(cell, {0}):
                    observed = lookup(matter_mask, mediator_mask)
                    if observed != (
                        (matter_mask, mediator_mask, 1 + 0j),
                    ):
                        omitted_failures += 1
                        if first_omitted_witness is None:
                            first_omitted_witness = {
                                "label": label,
                                "cell": cell,
                                "matter_mask": matter_mask,
                                "mediator_mask": mediator_mask,
                                "observed_local_lookup_rows": observed,
                            }
    expected = expected_axis_touched(axis)
    predicates = {
        "actual_union_equals_expected": actual_union == expected,
        "actual_union_has_14_cells": len(actual_union) == 14,
        "actual_union_is_inside_fixed_shell": actual_union <= shell,
        "all_omitted_cell_K_actions_vanish": omitted_failures == 0,
        "per_label_candidate_counts_match_historical_diagnostic": tuple(
            row["candidate_cell_count_C_j"] for row in per_label
        )
        == EXPECTED_CANDIDATE_CELL_COUNTS,
    }
    return {
        "predicates": predicates,
        "expected_touched_cells": tuple(sorted(expected)),
        "actual_touched_cells": tuple(sorted(actual_union)),
        "missing_expected_cells": tuple(sorted(expected - actual_union)),
        "unexpected_actual_cells": tuple(sorted(actual_union - expected)),
        "omitted_nonidentity_count": omitted_failures,
        "first_omitted_witness": first_omitted_witness,
        "per_label": tuple(per_label),
        "physical_selector": False,
        "scope": "nine declared update3 pre-collision product-factor supports",
    }


def factor_diagnostics(
    numerical_factors: tuple[Factor, ...],
    axis: int,
    partial_rows: list[dict] | None = None,
    partial_exact_by_label: dict[str, ExactMatterTags] | None = None,
) -> tuple[tuple[dict, ...], dict[str, ExactMatterTags]]:
    rows = [] if partial_rows is None else partial_rows
    exact_by_label = (
        {} if partial_exact_by_label is None else partial_exact_by_label
    )
    exact_prefix, exact_prefix_meta = exact_axis_prefix_tags(axis)
    for matter, mediator, label in numerical_factors:
        choices = (label[0], label[1])
        exact, exact_meta = exact_update3_branch_tags(
            exact_prefix, exact_prefix_meta, axis, choices
        )
        exact_by_label[label] = exact
        mediator_exact_keys, mediator_exact_meta = named_mediator_factor_oracle(
            axis, label
        )
        matter_diag = c512.unpruned_support_diagnostics(matter)
        mediator_diag = c512.unpruned_support_diagnostics(mediator)
        exact_keys = {key for key, tag in exact.items() if tag}
        machine_keys = {key for key, value in matter.items() if value != 0j}
        above_keys = {
            key for key, value in matter.items() if abs(value) > SUPPORT_DIAGNOSTIC_CEILING
        }
        expected_stored, expected_exact, expected_raw = EXPECTED_MATTER_FACTOR_COUNTS[
            label
        ]
        expected_mediator = EXPECTED_MEDIATOR_FACTOR_SUPPORT[label]
        predicates = {
            "exact_and_numerical_stored_key_sets_match": set(exact) == set(matter),
            "exact_support_is_subset_of_stored_keys": exact_keys <= set(matter),
            "matter_expected_counts_match_conditional_on_named_scalar_nonzero": (
                len(matter),
                len(exact_keys),
                exact_meta["raw_coin_contributions_updates1_2_3"][-1],
            )
            == (expected_stored, expected_exact, expected_raw),
            "mediator_named_history_keys_match_numerical_stored_keys": (
                mediator_exact_keys == set(mediator)
            ),
            "mediator_expected_support_matches_conditional_on_C_S_D_nonzero": (
                len(mediator_exact_keys) == len(mediator) == expected_mediator
            ),
            "mediator_named_history_predicates_pass": all(
                mediator_exact_meta["predicates"].values()
            ),
            "numerical_values_are_finite": matter_diag["nonfinite_value_count"] == 0
            and mediator_diag["nonfinite_value_count"] == 0,
        }
        rows.append(
            {
                "label": label,
                "predicates": predicates,
                "matter_stored_keys": len(matter),
                "matter_exact_symbolic_support": len(exact_keys),
                "matter_raw_coin_contributions_update3": exact_meta[
                    "raw_coin_contributions_updates1_2_3"
                ][-1],
                "matter_expected_stored_exact_raw": (
                    expected_stored,
                    expected_exact,
                    expected_raw,
                ),
                "matter_expected_count_gate_is_conditional_on_named_scalar_nonzero": True,
                "matter_machine_nonzero_values": len(machine_keys),
                "matter_machine_exact_zero_values": len(matter) - len(machine_keys),
                "matter_values_above_diagnostic_ceiling": len(above_keys),
                "matter_values_at_or_below_diagnostic_ceiling": matter_diag[
                    "values_at_or_below_diagnostic_ceiling"
                ],
                "matter_squared_norm_at_or_below_diagnostic_ceiling": matter_diag[
                    "squared_norm_at_or_below_diagnostic_ceiling"
                ],
                "exact_minus_machine_nonzero_count": len(exact_keys - machine_keys),
                "machine_nonzero_minus_exact_count": len(machine_keys - exact_keys),
                "exact_minus_above_ceiling_count": len(exact_keys - above_keys),
                "above_ceiling_minus_exact_count": len(above_keys - exact_keys),
                "machine_counts_are_gates": False,
                "diagnostic_ceiling_is_support_oracle": False,
                "mediator_stored_keys": len(mediator),
                "mediator_exact_named_history_support": len(mediator_exact_keys),
                "mediator_expected_support": expected_mediator,
                "mediator_machine_nonzero_values": mediator_diag[
                    "machine_nonzero_values"
                ],
                "mediator_values_at_or_below_diagnostic_ceiling": mediator_diag[
                    "values_at_or_below_diagnostic_ceiling"
                ],
                "exact_matter": exact_meta,
                "exact_mediator_named_history": mediator_exact_meta,
                "emitter_scalar_alphabet": (
                    "cos(theta)",
                    "i*sin(theta)",
                ),
                "emitter_scalar_nonzero_status": (
                    "supplied nonzero premise; mediator cancellation support not decided symbolically"
                ),
            }
        )
    return tuple(rows), exact_by_label


def transform_cell(
    cell: tuple[int, int, int], frame: np.ndarray
) -> tuple[int, int, int]:
    center = c512.c511.c509.ROUTE_C_TRAIN.probe_center
    return tuple(
        int(
            center[index]
            + sum(frame[index, j] * (cell[j] - center[j]) for j in range(3))
        )
        for index in range(3)
    )


def transform_matter_ray(ray: MatterRay, frame: np.ndarray) -> MatterRay:
    direction_map = c512.c510.direction_map(frame)
    output: MatterRay = {}
    for pair, amplitude in ray.items():
        moved = []
        for mode in pair:
            cell, direction = c512.decode_matter_mode(mode)
            moved.append(
                c512.matter_mode(transform_cell(cell, frame), direction_map[direction])
            )
        ordered = c512.canonical_pair(moved[0], moved[1])
        if ordered is None:
            raise RuntimeError("proper-cubic frame collapsed two CAR modes")
        target, sign = ordered
        c512.add_amplitude(output, target, sign * amplitude)
    return output


def transform_mediator_ray(ray: MediatorRay, frame: np.ndarray) -> MediatorRay:
    direction_map = c512.c510.direction_map(frame)
    output: MediatorRay = {}
    for configuration, amplitude in ray.items():
        moved = []
        for mode in configuration:
            cell, slot = c512.decode_mediator_mode(mode)
            moved_slot = 0 if slot == 0 else 1 + direction_map[slot - 1]
            moved.append(c512.mediator_mode(transform_cell(cell, frame), moved_slot))
        c512.add_amplitude(output, c512.canonical_mediator(moved), amplitude)
    return output


def transform_exact_tags(
    ray: ExactMatterTags, frame: np.ndarray
) -> ExactMatterTags:
    direction_map = c512.c510.direction_map(frame)
    output: ExactMatterTags = {}
    for pair, tag in ray.items():
        moved = []
        for mode in pair:
            cell, direction = c512.decode_matter_mode(mode)
            moved.append(
                c512.matter_mode(transform_cell(cell, frame), direction_map[direction])
            )
        ordered = c512.canonical_pair(moved[0], moved[1])
        if ordered is None:
            raise RuntimeError("proper-cubic exact tag frame collapsed two modes")
        target, sign = ordered
        c512.add_contact_tag(output, target, exact_copy_tag(tag, sign))
    return output


def scale_matter_ray(ray: MatterRay, sign: int) -> MatterRay:
    if sign not in (-1, 1):
        raise ValueError("CAR ray sign must be plus or minus one")
    return {pair: sign * amplitude for pair, amplitude in ray.items()}


def scale_exact_tags(ray: ExactMatterTags, sign: int) -> ExactMatterTags:
    if sign not in (-1, 1):
        raise ValueError("exact CAR tag sign must be plus or minus one")
    return {pair: exact_copy_tag(tag, sign) for pair, tag in ray.items()}


def packet_orientation_sign(frame: np.ndarray) -> tuple[int, dict]:
    direction_map = c512.c510.direction_map(frame)
    target_axis = direction_map[0] // 2
    # Mapping the prepared +axis ray to a negative target direction exchanges
    # its two packet roles exactly once.  Canonical exterior ordering therefore
    # contributes -1; positive target orientation contributes +1.  This is a
    # predetermined CAR sign, never a fitted phase.
    sign = 1 if direction_map[0] % 2 == 0 else -1
    transformed = transform_matter_ray(c512.initial_matter_ray(0), frame)
    target = c512.initial_matter_ray(target_axis)
    signed_residual = c512.ray_residual(
        transformed, scale_matter_ray(target, sign)
    )
    opposite_residual = c512.ray_residual(
        transformed, scale_matter_ray(target, -sign)
    )
    return sign, {
        "target_axis": target_axis,
        "mapped_positive_direction": direction_map[0],
        "predetermined_CAR_ray_sign": sign,
        "signed_initial_packet_residual": signed_residual,
        "opposite_sign_initial_packet_residual": opposite_residual,
        "phase_fitted": False,
    }


def transform_active_site(
    site: tuple[tuple[int, int, int], int, int, int, int],
    frame: np.ndarray,
) -> tuple[tuple[int, int, int], int, int, int, int]:
    cell, incoming, outgoing, incoming_slot, outgoing_slot = site
    direction_map = c512.c510.direction_map(frame)
    return (
        transform_cell(cell, frame),
        direction_map[incoming],
        direction_map[outgoing],
        1 + direction_map[incoming_slot - 1],
        1 + direction_map[outgoing_slot - 1],
    )


def transform_factor_label(
    label: str, frame: np.ndarray, target_axis: int
) -> tuple[str, tuple[int, int]]:
    target_sites = c512.FROZEN_UPDATE2_ACTIVE_SITES[target_axis]
    mapped_positions = []
    target_choices = ["", ""]
    for source_position, source_site in enumerate(
        c512.FROZEN_UPDATE2_ACTIVE_SITES[0]
    ):
        mapped_site = transform_active_site(source_site, frame)
        try:
            target_position = target_sites.index(mapped_site)
        except ValueError as error:
            raise RuntimeError(
                "proper-cubic frame did not map an active site into the target fixture"
            ) from error
        mapped_positions.append(target_position)
        target_choices[target_position] = label[source_position]
    if sorted(mapped_positions) != [0, 1] or not all(target_choices):
        raise RuntimeError("proper-cubic active-site map is not a permutation")
    return "".join(target_choices), tuple(mapped_positions)  # type: ignore[return-value]


def frame_comparison(
    axis_factors: dict[int, tuple[Factor, ...]],
    axis_exact_tags: dict[int, dict[str, ExactMatterTags]],
) -> dict:
    rows = []
    maximum_matter = 0.0
    maximum_mediator = 0.0
    exact_failures = 0
    frames = c512.c511.c210.proper_cubic_frames()
    source = axis_factors[0]
    target_by_axis = {
        axis: {label: (matter, mediator) for matter, mediator, label in factors}
        for axis, factors in axis_factors.items()
    }
    mapped_position_permutations = set()
    orientation_sign_counts = Counter()
    maximum_initial_packet_residual = 0.0
    for frame_index, frame in enumerate(frames):
        direction_map = c512.c510.direction_map(frame)
        target_axis = direction_map[0] // 2
        orientation_sign, orientation = packet_orientation_sign(frame)
        orientation_sign_counts[orientation_sign] += 1
        maximum_initial_packet_residual = max(
            maximum_initial_packet_residual,
            orientation["signed_initial_packet_residual"],
        )
        for source_matter, source_mediator, source_label in source:
            target_label, position_permutation = transform_factor_label(
                source_label, frame, target_axis
            )
            mapped_position_permutations.add(position_permutation)
            target_matter, target_mediator = target_by_axis[target_axis][target_label]
            matter_residual = c512.ray_residual(
                transform_matter_ray(source_matter, frame),
                scale_matter_ray(target_matter, orientation_sign),
            )
            mediator_residual = c512.ray_residual(
                transform_mediator_ray(source_mediator, frame), target_mediator
            )
            maximum_matter = max(maximum_matter, matter_residual)
            maximum_mediator = max(maximum_mediator, mediator_residual)
            source_exact = axis_exact_tags[0][source_label]
            target_exact = axis_exact_tags[target_axis][target_label]
            exact_match = transform_exact_tags(source_exact, frame) == scale_exact_tags(
                target_exact, orientation_sign
            )
            exact_failures += not exact_match
            rows.append(
                {
                    "frame_index": frame_index,
                    "source_axis": 0,
                    "target_axis": target_axis,
                    "source_label": source_label,
                    "target_label": target_label,
                    "active_site_position_permutation": position_permutation,
                    "predetermined_CAR_ray_sign": orientation_sign,
                    "signed_initial_packet_residual": orientation[
                        "signed_initial_packet_residual"
                    ],
                    "phase_fitted": False,
                    "frame": tuple(tuple(int(value) for value in row) for row in frame),
                    "direction_map": direction_map,
                    "matter_exterior_CAR_residual": matter_residual,
                    "mediator_hard_core_residual": mediator_residual,
                    "exact_matter_tag_match": exact_match,
                }
            )
    predicates = {
        "all_24_proper_cubic_frames_compared": len(frames) == 24
        and len(rows) == 24 * len(source),
        "both_active_site_orientation_permutations_observed": (
            mapped_position_permutations == {(0, 1), (1, 0)}
        ),
        "packet_orientation_sign_census_is_12_plus_12_minus": (
            orientation_sign_counts == {1: 12, -1: 12}
        ),
        "signed_initial_packet_frame_residual_below_ceiling": (
            maximum_initial_packet_residual <= FRAME_RESIDUAL_CEILING
        ),
        "matter_frame_residual_below_ceiling": maximum_matter
        <= FRAME_RESIDUAL_CEILING,
        "mediator_frame_residual_below_ceiling": maximum_mediator
        <= FRAME_RESIDUAL_CEILING,
        "exact_matter_tags_frame_match": exact_failures == 0,
    }
    return {
        "predicates": predicates,
        "rows": tuple(rows),
        "maximum_matter_exterior_CAR_residual": maximum_matter,
        "maximum_mediator_hard_core_residual": maximum_mediator,
        "exact_matter_tag_failures": exact_failures,
        "proper_cubic_frame_count": len(frames),
        "factor_state_comparison_count": len(rows),
        "active_site_position_permutations": tuple(
            sorted(mapped_position_permutations)
        ),
        "packet_orientation_sign_census": dict(sorted(orientation_sign_counts.items())),
        "maximum_signed_initial_packet_residual": maximum_initial_packet_residual,
        "ceiling": FRAME_RESIDUAL_CEILING,
        "CAR_signs_included": True,
        "physical_frame_reference_derived": True,
        "phase_fitted": False,
    }


def partial_retention_failure_fixture(fail_at: int = 3) -> dict:
    retained = []
    error = None
    try:
        for index, label in enumerate(c512.EXPECTED_UPDATE2_FACTOR_LABELS):
            if index == fail_at:
                raise RuntimeError(f"injected failure before {label}")
            retained.append({"index": index, "label": label, "completed": True})
    except RuntimeError as caught:
        error = str(caught)
    return {
        "fail_at": fail_at,
        "retained_rows": tuple(retained),
        "retained_count": len(retained),
        "error": error,
        "JSON_safe": True,
    }


def run_dry() -> tuple[dict, int]:
    tests = []

    def check(name: str, condition: bool, detail: object = None) -> None:
        tests.append({"name": name, "passed": bool(condition), "detail": detail})

    allowed, authorization = authorization_decision("dry-contract")
    if not allowed:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "mode": "dry-contract",
            "status": "authorization-rejected",
            "authorization": authorization,
            "global_amplitude_states_evolved": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
        }, 2

    evidence = evidence_controls()
    check("Cycle512 and Cycle513 packaged evidence hashes are exact", not evidence["strict_hash_failures"], evidence)
    check(
        "Cycle513 failed receipt is exact and its old invocation is consumed",
        evidence["Cycle513_receipt_schema"] == EXPECTED_CYCLE513_RECEIPT_SCHEMA
        and evidence["Cycle513_receipt_status"] == EXPECTED_CYCLE513_STATUS
        and evidence["Cycle513_receipt_pass"] is False
        and evidence["Cycle513_dry_tests"] == (9, 9)
        and evidence["Cycle513_attempt_exit_code"] == 1
        and evidence["Cycle513_attempt_error"]
        == "axis1 frozen prefix or geometry equivalence failed"
        and evidence["Cycle513_single_invocation_consumed"] is True
        and evidence["Cycle513_old_invocation_reusable"] is False
        and evidence["Cycle513_cause_proven"] is False,
        evidence,
    )
    check(
        "Cycle512 qualified update2 all-axis prefix remains exact",
        evidence["Cycle512_receipt_schema"] == EXPECTED_CYCLE512_RECEIPT_SCHEMA
        and evidence["Cycle512_receipt_status"] == EXPECTED_CYCLE512_STATUS
        and evidence["Cycle512_receipt_pass"] is True
        and evidence["Cycle512_all_axis_rank9"] is True,
        evidence,
    )
    angle = c512.c511.factor_coordinate_controls()[
        "train_and_matched_size_beta_-4pi_over_9"
    ]["emitter_and_collision_angle"]
    local = c513.local_block_certificate(angle)
    check("inherited exhaustive 2794-state local block certificate passes", local["pass"], local)
    geometry = c513.geometry_contract()
    check(
        "fixed shell is 18 cells and invariant under all 24 proper-cubic frames",
        geometry["support_equivalent_fixed_shell_cell_count"] == 18
        and geometry["proper_cubic_frame_failures"] == 0,
        geometry,
    )
    frames = c512.c511.c210.proper_cubic_frames()
    frame_site_rows = []
    for frame_index, frame in enumerate(frames):
        direction_map = c512.c510.direction_map(frame)
        target_axis = direction_map[0] // 2
        mapped_label, position_permutation = transform_factor_label(
            "DX", frame, target_axis
        )
        frame_site_rows.append(
            {
                "frame_index": frame_index,
                "target_axis": target_axis,
                "source_label": "DX",
                "mapped_label": mapped_label,
                "position_permutation": position_permutation,
                "orientation": packet_orientation_sign(frame)[1],
            }
        )
    check(
        "all 24 frame-local active-site maps are exact permutations",
        len(frame_site_rows) == 24
        and {row["target_axis"] for row in frame_site_rows} == {0, 1, 2}
        and {row["position_permutation"] for row in frame_site_rows}
        == {(0, 1), (1, 0)}
        and all(
            row["mapped_label"]
            == ("DX" if row["position_permutation"] == (0, 1) else "XD")
            for row in frame_site_rows
        ),
        frame_site_rows,
    )
    orientation_census = Counter(
        row["orientation"]["predetermined_CAR_ray_sign"]
        for row in frame_site_rows
    )
    check(
        "packet orientation supplies a predetermined 12 plus / 12 minus CAR sign fixture",
        orientation_census == {1: 12, -1: 12}
        and all(
            row["orientation"]["signed_initial_packet_residual"]
            <= FRAME_RESIDUAL_CEILING
            and row["orientation"]["phase_fitted"] is False
            for row in frame_site_rows
        ),
        {
            "orientation_sign_census": dict(sorted(orientation_census.items())),
            "maximum_signed_residual": max(
                row["orientation"]["signed_initial_packet_residual"]
                for row in frame_site_rows
            ),
            "phase_fitted": False,
        },
    )
    site = c512.FROZEN_UPDATE2_ACTIVE_SITES[0][0]
    old_mode = c512.matter_mode(site[0], site[1])
    new_mode = c512.matter_mode(site[0], site[2])
    spectator_mode = c512.matter_mode((7, 7, 7), 2)
    source_pair = tuple(sorted((old_mode, spectator_mode)))
    source_tag = {0: c512.cyclotomic_rational(Fraction(1))}
    source_ray = {source_pair: source_tag}
    expected_exchange_pair = tuple(sorted((new_mode, spectator_mode)))
    local_branch_rows = {
        choice: exact_apply_branch_term(source_ray, site, choice)
        for choice in ("I", "D", "X")
    }
    check(
        "exact local matter tag branch action covers I, D, and X with Pauli exclusion",
        local_branch_rows["I"] == source_ray
        and local_branch_rows["D"] == source_ray
        and local_branch_rows["X"] == {expected_exchange_pair: source_tag}
        and exact_apply_branch_term(
            {tuple(sorted((old_mode, new_mode))): source_tag}, site, "X"
        )
        == {},
        {
            "branch_stored_key_counts": {
                choice: len(ray) for choice, ray in local_branch_rows.items()
            },
            "I_D_source_key_preserved": (
                set(local_branch_rows["I"]) == set(local_branch_rows["D"])
                == {source_pair}
            ),
            "X_expected_key": expected_exchange_pair,
            "Pauli_blocked_X_key_count": len(
                exact_apply_branch_term(
                    {tuple(sorted((old_mode, new_mode))): source_tag}, site, "X"
                )
            ),
        },
    )
    partial_fixture = partial_retention_failure_fixture()
    check(
        "pure injected failure retains every completed caller-owned row",
        partial_fixture["retained_count"] == 3
        and tuple(
            row["label"] for row in partial_fixture["retained_rows"]
        )
        == c512.EXPECTED_UPDATE2_FACTOR_LABELS[:3]
        and partial_fixture["error"] == "injected failure before DI",
        partial_fixture,
    )
    check(
        "conditional exact matter and named-mediator support fixtures cover all nine labels",
        set(EXPECTED_MATTER_FACTOR_COUNTS)
        == set(EXPECTED_MEDIATOR_FACTOR_SUPPORT)
        == set(c512.EXPECTED_UPDATE2_FACTOR_LABELS)
        and EXPECTED_MATTER_FACTOR_COUNTS["II"] == (46425, 30207, 176286)
        and {EXPECTED_MATTER_FACTOR_COUNTS[label] for label in ("ID", "IX", "DI", "XI")}
        == {(1800, 1620, 3456)}
        and {EXPECTED_MATTER_FACTOR_COUNTS[label] for label in ("DD", "DX", "XD", "XX")}
        == {(36, 36, 36)}
        and EXPECTED_MEDIATOR_FACTOR_SUPPORT["II"] == 4096
        and {
            EXPECTED_MEDIATOR_FACTOR_SUPPORT[label]
            for label in ("ID", "IX", "DI", "XI")
        }
        == {1024}
        and {
            EXPECTED_MEDIATOR_FACTOR_SUPPORT[label]
            for label in ("DD", "DX", "XD", "XX")
        }
        == {256},
        {
            "matter": EXPECTED_MATTER_FACTOR_COUNTS,
            "mediator": EXPECTED_MEDIATOR_FACTOR_SUPPORT,
            "conditional_on_named_C_S_D_nonzero": True,
        },
    )
    check(
        "dry authorization is absent and Cycle514 reuses only the frozen scout contract",
        authorization["present_authorization_variables"] == ()
        and authorization["runner_integrity_variable_present"] is False
        and authorization["frozen_Cycle511_scout_contract_matches"],
        authorization,
    )
    runner_sha = file_sha(Path(__file__))
    cases = {
        "absent": authorization_inputs_allowed((), {}, False, None, runner_sha, True),
        "empty": authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: ""},
            True,
            runner_sha,
            runner_sha,
            True,
        ),
        "wrong_token": authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: "wrong"},
            True,
            runner_sha,
            runner_sha,
            True,
        ),
        "missing_integrity": authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            False,
            None,
            runner_sha,
            True,
        ),
        "wrong_integrity": authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            True,
            "wrong",
            runner_sha,
            True,
        ),
        "contract_mismatch": authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            True,
            runner_sha,
            runner_sha,
            False,
        ),
        "exact": authorization_inputs_allowed(
            (SCOUT_AUTHORIZATION_ENV,),
            {SCOUT_AUTHORIZATION_ENV: SCOUT_AUTHORIZATION_TOKEN},
            True,
            runner_sha,
            runner_sha,
            True,
        ),
    }
    check(
        "authorization matrix accepts only exact frozen token and Cycle514 integrity",
        cases["exact"]
        and not any(value for key, value in cases.items() if key != "exact"),
        cases,
    )
    historical = {
        "counts": HISTORICAL_COUNTS,
        "used_as_axis_gate": False,
        "used_as_resource_gate": False,
        "used_as_science_result": False,
    }
    check("461, 581, and 453 are historical diagnostics only", not any(historical[key] for key in historical if key != "counts"), historical)
    execution = {
        "large_global_allocations": 0,
        "global_amplitude_states_evolved": 0,
        "symbolic_axis_diagnostic_executed": False,
        "generic_collision_growth_executed": False,
        "science_rows_executed": 0,
        "response_rows_executed": 0,
        "held_rows_executed": 0,
        "deletion_variants_executed": 0,
        "selector": False,
        "refit": False,
    }
    check("dry mode evolves no global amplitude and exposes no later surface", not any(execution.values()), execution)
    passed = all(row["passed"] for row in tests)
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle514-symbolic-axis-diagnostic-contract-ready" if passed else "dry-contract-failed",
        "pass": passed,
        "tests_passed": sum(row["passed"] for row in tests),
        "tests_total": len(tests),
        "authorization": authorization,
        "evidence": evidence,
        "local_block_certificate": local,
        "geometry_contract": geometry,
        "historical_counts": historical,
        "execution": execution,
        "tests": tests,
    }, 0 if passed else 1


def run_symbolic_axis_diagnostic() -> tuple[dict, int]:
    allowed, authorization = authorization_decision("symbolic-axis-diagnostic")
    if not allowed:
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "mode": "symbolic-axis-diagnostic",
            "status": "authorization-rejected",
            "authorization": authorization,
            "diagnostic_invocations": 0,
            "generic_collision_growth_executed": False,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
        }, 2

    started = time.monotonic()
    checkpoints = []
    early_stage = "packaged-evidence"
    try:
        evidence = evidence_controls()
        if evidence["strict_hash_failures"]:
            raise RuntimeError(
                "packaged Cycle512/513 evidence changed after authorization"
            )
        early_stage = "coordinate-and-coin"
        angle = c512.c511.factor_coordinate_controls()[
            "train_and_matched_size_beta_-4pi_over_9"
        ]["emitter_and_collision_angle"]
        coin = c512.c511.c509.c219.common_species(c512.MIDDLE_BETA).coin
        early_stage = "local-collision-lookup"
        lookup, _controls = c512.local_collision_lookup(angle)
        early_stage = "initial-resource-checkpoint"
        checkpoints.append(
            resource_checkpoint(started, "after-evidence-and-local-lookup")
        )
    except Exception as error:
        is_resource = isinstance(error, (ResourceWall, MemoryError))
        return {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": "symbolic-axis-diagnostic",
            "status": (
                "symbolic-axis-precollision-diagnostic-resource-wall"
                if is_resource
                else "symbolic-axis-precollision-diagnostic-early-failure"
            ),
            "pass": False,
            "authorization": authorization,
            "diagnostic_invocations": 1,
            "single_invocation_consumed": True,
            "failure_stage": early_stage,
            "error_type": type(error).__name__,
            "error": str(error),
            "axis_rows": (),
            "partial_ledger_preserved": True,
            "generic_update3_collision_growth_executed": False,
            "post_collision_update3_mediator_stream_executed": False,
            "joint_species_Schmidt_core_constructed": False,
            "joint_species_Schmidt_rank_computed": False,
            "science_rows_executed": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
            "selector": False,
            "refit": False,
            "resource": {
                "elapsed_seconds": time.monotonic() - started,
                "maximum_RSS_bytes": rss_bytes(),
                "process_swap_count": swap_count(),
                "checkpoints": checkpoints,
            },
        }, 1

    axis_rows = [
        {
            "axis": axis,
            "completed": False,
            "pass": False,
            "stage": "not-started",
            "predicates": {name: None for name in AXIS_PREDICATE_NAMES},
            "prefix": None,
            "geometry": None,
            "numerical_factor_build_rows": [],
            "geometry_partial_rows": [],
            "factor_diagnostics": (),
            "machine_nonzero_count_used_as_gate": False,
            "historical_461_581_453_used_as_gate": False,
            "partial_ledger_preserved": True,
        }
        for axis in range(3)
    ]
    axis_factors: dict[int, tuple[Factor, ...]] = {}
    axis_exact_tags: dict[int, dict[str, ExactMatterTags]] = {}
    resource_wall = None
    for axis, axis_row in enumerate(axis_rows):
        try:
            axis_row["stage"] = "resource-start-check"
            checkpoints.append(
                resource_checkpoint(started, f"axis{axis}-start", 400_000_000)
            )
            axis_row["stage"] = "numerical-prefix"
            numerical_build_rows: list[dict] = axis_row[
                "numerical_factor_build_rows"
            ]
            factors, prefix = build_update3_pre_collision_factors(
                axis, coin, angle, lookup, numerical_build_rows
            )
            axis_row["prefix"] = prefix
            axis_row["predicates"].update(prefix["predicates"])
            axis_row["stage"] = "geometry"
            geometry_partial_rows: list[dict] = axis_row["geometry_partial_rows"]
            geometry = geometry_witness(
                factors, lookup, axis, geometry_partial_rows
            )
            axis_row["geometry"] = geometry
            axis_row["predicates"].update(
                {
                    f"geometry:{key}": value
                    for key, value in geometry["predicates"].items()
                }
            )
            axis_row["stage"] = "exact-factor-diagnostics"
            partial_factor_rows: list[dict] = []
            exact_tags: dict[str, ExactMatterTags] = {}
            axis_row["factor_diagnostics"] = partial_factor_rows
            factor_rows, exact_tags = factor_diagnostics(
                factors, axis, partial_factor_rows, exact_tags
            )
            axis_row["factor_diagnostics"] = factor_rows
            axis_row["predicates"][
                "all_factor_exact_stored_and_finite_predicates"
            ] = all(all(row["predicates"].values()) for row in factor_rows)
            axis_row["completed"] = True
            axis_row["pass"] = all(
                value is True for value in axis_row["predicates"].values()
            )
            axis_row["stage"] = "complete"
            axis_factors[axis] = factors
            axis_exact_tags[axis] = exact_tags
            checkpoints.append(resource_checkpoint(started, f"axis{axis}-complete"))
        except (ResourceWall, MemoryError) as error:
            resource_wall = f"{type(error).__name__}: {error}"
            axis_row["error_type"] = type(error).__name__
            axis_row["error"] = str(error)
            axis_row["failed_at_stage"] = axis_row["stage"]
            axis_row["stage"] = "resource-wall"
            for remaining in axis_rows[axis + 1 :]:
                remaining["stage"] = "not-attempted-after-resource-wall"
                remaining["error_type"] = "PriorResourceWall"
                remaining["error"] = resource_wall
            break
        except Exception as error:
            axis_row["error_type"] = type(error).__name__
            axis_row["error"] = str(error)
            axis_row["failed_at_stage"] = axis_row["stage"]
            axis_row["stage"] = "exception"
            continue

    frame = None
    if set(axis_factors) == {0, 1, 2}:
        try:
            frame = frame_comparison(axis_factors, axis_exact_tags)
        except Exception as error:
            frame = {
                "predicates": {"frame_comparison_completed": False},
                "error_type": type(error).__name__,
                "error": str(error),
            }
    all_axes_completed = len(axis_rows) == 3 and all(
        row.get("completed") is True for row in axis_rows
    )
    all_axis_predicates = all_axes_completed and all(
        row.get("pass") is True for row in axis_rows
    )
    frame_pass = frame is not None and all(frame.get("predicates", {}).values())
    passed = all_axis_predicates and frame_pass and resource_wall is None
    exact_completed_rows = sum(
        len(row.get("factor_diagnostics", ())) for row in axis_rows
    )
    status = (
        "symbolic-axis-precollision-diagnostic-complete-conditional"
        if passed
        else (
            "symbolic-axis-precollision-diagnostic-resource-wall"
            if resource_wall is not None
            else "symbolic-axis-precollision-diagnostic-witnessed-mismatch"
        )
    )
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "mode": "symbolic-axis-diagnostic",
        "status": status,
        "pass": passed,
        "authorization": authorization,
        "evidence": evidence,
        "axis_rows": tuple(axis_rows),
        "frame_transport": frame,
        "historical_counts": {
            "values": HISTORICAL_COUNTS,
            "historical_only": True,
            "used_as_gate": False,
        },
        "scalar_support_boundary": {
            "matter_exact_field": "Q(zeta_9)[z] with z the formal contact phase",
            "collision_factors": ("1", "cos(theta)-1", "i*sin(theta)"),
            "emitter_factors": ("cos(theta)", "i*sin(theta)"),
            "trigonometric_nonzero_is_supplied_premise": True,
            "trigonometric_interval_certificate_present": False,
            "cross_branch_cancellation_oracle_present": False,
            "mediator_exact_symbolic_cancellation_oracle_present": False,
            "mediator_named_monomial_history_oracle_present": exact_completed_rows
            > 0,
            "C_S_D_nonzero_is_supplied_premise": True,
            "algebraic_relation_between_C_S_D_needed": False,
            "conditional_result_only": True,
        },
        "resource": {
            "elapsed_seconds": time.monotonic() - started,
            "maximum_RSS_bytes": rss_bytes(),
            "process_swap_count": swap_count(),
            "checkpoints": checkpoints,
            "wall": resource_wall,
            "limits": {
                "RSS_bytes": RSS_LIMIT_BYTES,
                "preallocation_abort_bytes": RSS_PREALLOC_ABORT_BYTES,
                "wall_seconds": WALL_LIMIT_SECONDS,
                "swap_count": 0,
            },
        },
        "execution": {
            "diagnostic_invocations": 1,
            "single_invocation_consumed": True,
            "science_result": False,
            "completed_update3": False,
            "all_axis_growth": False,
            "physical_compiler_covariance_established": False,
            "all_three_axes_update3_pre_collision_built": all_axes_completed,
            "exact_branch_local_matter_tags_executed": exact_completed_rows > 0,
            "exact_branch_local_matter_tags_completed_rows": exact_completed_rows,
            "named_mediator_history_oracle_executed": exact_completed_rows > 0,
            "named_mediator_history_oracle_completed_rows": exact_completed_rows,
            "machine_nonzero_gate_used": False,
            "generic_update3_collision_growth_executed": False,
            "post_collision_update3_mediator_stream_executed": False,
            "joint_species_Schmidt_core_constructed": False,
            "joint_species_Schmidt_rank_computed": False,
            "forward_reverse_collision_cell_order_compared": False,
            "full_inverse_update3_executed": False,
            "state_orbit72_executed": False,
            "depth5_completed": False,
            "science_rows_executed": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
            "deletion_variants_executed": 0,
            "response_values_emitted": 0,
            "occupation_or_bond_fields_emitted": 0,
            "state_hashes_emitted": 0,
            "selector": False,
            "refit": False,
            "packed_joint_constructed": False,
            "dense_X_or_Y_constructed": False,
        },
        "open": {
            "generic_update3_collision_growth": True,
            "post_collision_update3_mediator_stream": True,
            "joint_species_Schmidt_core_and_rank": True,
            "forward_reverse_collision_cell_order": True,
            "full_inverse_update3": True,
            "state_orbit72": True,
            "depth5": True,
            "response": True,
            "deletion_train_held": True,
            "physical_parity_superselection_compiler": True,
        },
        "interpretation": (
            "diagnostics-only pre-collision prefix; a pass or mismatch is neither "
            "completed update3 science nor a substrate obstruction or axiom-pressure result"
        ),
    }, 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    try:
        payload, code = (
            run_dry()
            if args.mode == "dry-contract"
            else run_symbolic_axis_diagnostic()
        )
    except Exception as error:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "revision": REVISION,
            "mode": args.mode,
            "status": "fail-closed-exception",
            "error_type": type(error).__name__,
            "error": str(error),
            "diagnostic_invocations": 0,
            "generic_update3_collision_growth_executed": False,
            "post_collision_update3_mediator_stream_executed": False,
            "joint_species_Schmidt_core_constructed": False,
            "joint_species_Schmidt_rank_computed": False,
            "science_rows_executed": 0,
            "response_rows_executed": 0,
            "held_rows_executed": 0,
            "deletion_variants_executed": 0,
            "response_values_emitted": 0,
            "occupation_or_bond_fields_emitted": 0,
            "state_hashes_emitted": 0,
            "selector": False,
            "refit": False,
        }
        code = 1
    print(json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
