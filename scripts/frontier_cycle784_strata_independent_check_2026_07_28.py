#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-784 k=3/k=4 census.

The Cycle-784 primary is blocklisted: it is read only as text and parsed only
as an AST.  Enumeration, orbit reduction, selector evaluation, covariance,
tie functionals, and exclusion-mechanism counts are implemented here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle758_selector_multisource_2026_07_28 as F758


RING_STATIONS = 11
FIXTURE_BANKS = 2
TARGET_STRATA = (3, 4)
STDOUT_LIMIT_BYTES = 150 * 1024
PRIMARY_PATH = (
    "scripts/frontier_cycle784_full_strata_ties_2026_07_28.py"
)
PRIMARY_MODULE = Path(PRIMARY_PATH).stem

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    PRIMARY_PATH:
        "b532563da6aa8e84ae8aae2c4ad14c10a50d45d43c020ca2107fd48b79dc8a30",
}

EXPECTED_STRATA = {
    3: {
        "configuration_count": 77,
        "translation_family_count": 7,
        "family_epoch_count": 28,
        "outcome_counts": {
            "exact_tie": 7,
            "unique_survivor": 3,
            "zero_survivors": 18,
        },
        "covariance_failure_families": 5,
    },
    4: {
        "configuration_count": 55,
        "translation_family_count": 5,
        "family_epoch_count": 20,
        "outcome_counts": {
            "exact_tie": 0,
            "unique_survivor": 0,
            "zero_survivors": 20,
        },
        "covariance_failure_families": 0,
    },
}

FUNCTIONAL_SPECS = (
    (
        "first_Q_layer_physical_gate_count_minimum",
        "gate_count",
        "minimum",
    ),
    (
        "first_Q_layer_physical_gate_count_maximum",
        "gate_count",
        "maximum",
    ),
    (
        "initial_relay_station_occupancy_minimum",
        "relay_occupancy",
        "minimum",
    ),
    (
        "initial_handoff_station_occupancy_maximum",
        "handoff_occupancy",
        "maximum",
    ),
)
FROZEN_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))


def jsonable(value: object) -> object:
    if isinstance(value, dict):
        return {
            (
                ",".join(map(str, key))
                if isinstance(key, tuple)
                else str(key)
            ): jsonable(item)
            for key, item in value.items()
        }
    if isinstance(value, (tuple, list)):
        return [jsonable(item) for item in value]
    return value


def compact(value: object) -> str:
    return json.dumps(
        jsonable(value),
        sort_keys=True,
        separators=(",", ":"),
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def own_orbit(positions: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        sorted(
            {
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            }
        )
    )


def independent_positions(k: int) -> tuple[tuple[int, ...], ...]:
    """Brute-force Ind_k(C_11), without the landed census helper."""

    rows = []
    for positions in combinations(range(RING_STATIONS), k):
        occupied = set(positions)
        if all(
            (station + 1) % RING_STATIONS not in occupied
            for station in occupied
        ):
            rows.append(positions)
    return tuple(rows)


def independent_closed_form(k: int) -> int:
    numerator = RING_STATIONS * comb(RING_STATIONS - k, k)
    denominator = RING_STATIONS - k
    if numerator % denominator:
        raise AssertionError(("nonintegral independent-cycle count", k))
    return numerator // denominator


def own_families(
    positions_rows: tuple[tuple[int, ...], ...]
) -> dict[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    grouped: dict[
        tuple[int, ...], set[tuple[int, ...]]
    ] = {}
    for positions in positions_rows:
        representative = min(own_orbit(positions))
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(members))
        for representative, members in sorted(grouped.items())
    }


def positions_to_bits(
    positions: tuple[int, ...]
) -> tuple[int, ...]:
    occupied = set(positions)
    return tuple(
        int(station in occupied) for station in range(RING_STATIONS)
    )


def reduction_surface() -> dict[str, object]:
    strata = {}
    all_partition_checks = []
    for k in TARGET_STRATA:
        configurations = independent_positions(k)
        families = own_families(configurations)
        flattened = tuple(
            member
            for members in families.values()
            for member in members
        )
        membership = Counter(flattened)
        reroot_failures = []
        for representative, members in families.items():
            for member in members:
                if own_orbit(member) != members:
                    reroot_failures.append(
                        (representative, member, own_orbit(member))
                    )

        landed_bits = tuple(
            positions_to_bits(row) for row in configurations
        )
        landed_families = F758.configuration_families(landed_bits)[k]
        landed_match = landed_families == families
        partition_exact = (
            len(configurations) == independent_closed_form(k)
            and len(flattened) == len(configurations)
            and set(flattened) == set(configurations)
            and all(count == 1 for count in membership.values())
            and all(len(members) == RING_STATIONS
                    for members in families.values())
            and not reroot_failures
        )
        all_partition_checks.append(partition_exact)
        strata[str(k)] = {
            "configuration_count": len(configurations),
            "closed_form_count": independent_closed_form(k),
            "translation_family_count": len(families),
            "family_epoch_count": 4 * len(families),
            "family_sizes": tuple(map(len, families.values())),
            "representatives": tuple(families),
            "partition_exactly_once": partition_exact,
            "all_member_reroot_orbits_identical": not reroot_failures,
            "landed_reduction_crosscheck": landed_match,
        }
    return {
        "equivalence": (
            "same orbit under the cyclic translation action C11 on station "
            "sets; no configuration is replaced by a representative"
        ),
        "strata": strata,
        "partition_complete": all(all_partition_checks),
    }


def own_fixtures() -> tuple[
    tuple[int, tuple[int, int], tuple[object, ...], int, int], ...
]:
    """Rebuild the four Cycle-750 two-bank epochs from Cycle-719 primitives."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        expected = K.A.apply_semantic(
            before,
            K.M.global_allocator_word(FIXTURE_BANKS),
        )
        rows.append((event, direction, program, before, expected))
        state = expected
    return tuple(rows)


def own_synchronous_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Compose each occupied station macro over one orbit, independently."""

    moving = tuple(positions)
    word = []
    for _step in range(len(program)):
        live = set(moving)
        for station in range(len(program)):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        moving = tuple(
            (station + 1) % len(program) for station in moving
        )
    return tuple(word)


def postimage_residual(after: int) -> tuple[int, int, int]:
    banks, links = K.M.unpack_state(after, FIXTURE_BANKS)
    bank_work = sum(
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
    )
    link_work = sum(sum(link) for link in links)
    return (
        int(after[K.R3.X.SOURCE_POINTER]),
        int(bank_work),
        int(link_work),
    )


def evaluate_alternative(
    program: tuple[object, ...],
    before: int,
    positions: tuple[int, ...],
) -> dict[str, object]:
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = (0,) * len(program)
    composition_word = own_synchronous_word(program, positions)
    landed_word = M736.synchronous_composition_word(program, positions)
    expected = K.A.apply_semantic(before, composition_word)
    after, rail_a, rail_b, _trace = K.run_orbit(
        before,
        program,
        token_positions=positions,
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after,
        program,
        token_positions=positions,
        reverse=True,
    )
    residual = postimage_residual(after)
    conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": residual == (0, 0, 0),
    }
    return {
        "positions": positions,
        "conditions": conditions,
        "survivor": all(conditions.values()),
        "postimage_residual": residual,
        "own_word_matches_landed": composition_word == landed_word,
    }


def evaluate_family(
    program: tuple[object, ...],
    before: int,
    alternatives: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    evaluations = tuple(
        evaluate_alternative(program, before, alternative)
        for alternative in alternatives
    )
    return {
        "selected": tuple(
            row["positions"] for row in evaluations if row["survivor"]
        ),
        "evaluations": evaluations,
    }


def outcome_class(
    selected: tuple[tuple[int, ...], ...]
) -> str:
    if not selected:
        return "zero_survivors"
    if len(selected) == 1:
        return "unique_survivor"
    return "exact_tie"


def run_full_census() -> dict[str, object]:
    fixtures = own_fixtures()
    stratum_surfaces = {}
    all_rows = []
    all_covariance = []
    word_crosscheck_failures = 0

    for k in TARGET_STRATA:
        configurations = independent_positions(k)
        families = own_families(configurations)
        outcome_counts: Counter[str] = Counter()
        failed_conditions: Counter[str] = Counter()
        rows = []
        covariance_rows = []

        for representative, alternatives in families.items():
            base_selected = None
            for event, direction, program, before, _expected in fixtures:
                result = evaluate_family(program, before, alternatives)
                selected = result["selected"]
                if event == 0:
                    base_selected = selected
                classification = outcome_class(selected)
                outcome_counts[classification] += 1
                for evaluation in result["evaluations"]:
                    word_crosscheck_failures += (
                        not evaluation["own_word_matches_landed"]
                    )
                    for condition, passed in (
                        evaluation["conditions"].items()
                    ):
                        if not passed:
                            failed_conditions[condition] += 1
                row = {
                    "k": k,
                    "representative": representative,
                    "event": event,
                    "direction": direction,
                    "alternative_count": len(alternatives),
                    "outcome_class": classification,
                    "selected_count": len(selected),
                    "selected": selected,
                    "evaluations": result["evaluations"],
                }
                rows.append(row)
                all_rows.append(row)

            if base_selected is None:
                raise AssertionError(("missing event zero", representative))
            first = fixtures[0]
            failures = []
            membership_failures = 0
            for shift in range(RING_STATIONS):
                if shift == 0:
                    observed = base_selected
                else:
                    program = first[2]
                    rotated_program = (
                        program[shift:] + program[:shift]
                    )
                    rotated = evaluate_family(
                        rotated_program,
                        first[3],
                        alternatives,
                    )
                    observed = rotated["selected"]
                    for evaluation in rotated["evaluations"]:
                        word_crosscheck_failures += (
                            not evaluation["own_word_matches_landed"]
                        )
                expected = tuple(
                    sorted(
                        rotate_positions(alternative, -shift)
                        for alternative in base_selected
                    )
                )
                symmetric_difference = len(
                    set(observed) ^ set(expected)
                )
                membership_failures += symmetric_difference
                if observed != expected:
                    failures.append(
                        {
                            "shift": shift,
                            "observed": observed,
                            "expected": expected,
                            "membership_failures":
                                symmetric_difference,
                        }
                    )
            covariance_row = {
                "k": k,
                "representative": representative,
                "failure_count": len(failures),
                "membership_failure_count": membership_failures,
                "failures": tuple(failures),
            }
            covariance_rows.append(covariance_row)
            all_covariance.append(covariance_row)

        for name in (
            "unique_survivor",
            "exact_tie",
            "zero_survivors",
        ):
            outcome_counts[name] += 0
        covariance_failures = {
            row["representative"]: bool(row["failure_count"])
            for row in covariance_rows
        }
        public_rows = tuple(
            {
                key: value
                for key, value in row.items()
                if key != "evaluations"
            }
            | {
                "covariance_failure": (
                    covariance_failures[row["representative"]]
                    if row["event"] == 0
                    else None
                ),
                "adversarial_class": (
                    "covariance_failure"
                    if (
                        row["event"] == 0
                        and covariance_failures[row["representative"]]
                    )
                    else row["outcome_class"]
                ),
            }
            for row in rows
        )
        stratum_surfaces[str(k)] = {
            "configuration_count": len(configurations),
            "translation_family_count": len(families),
            "family_epoch_count": len(rows),
            "configuration_evaluations": sum(
                row["alternative_count"] for row in rows
            ),
            "outcome_counts": dict(sorted(outcome_counts.items())),
            "covariance_failure_family_count": sum(
                bool(row["failure_count"]) for row in covariance_rows
            ),
            "covariance_failure_shift_count": sum(
                row["failure_count"] for row in covariance_rows
            ),
            "covariance_membership_failure_count": sum(
                row["membership_failure_count"]
                for row in covariance_rows
            ),
            "failed_condition_census":
                dict(sorted(failed_conditions.items())),
            "rows": public_rows,
            "covariance": tuple(covariance_rows),
        }

    deterministic_surface = {
        "strata": stratum_surfaces,
        "word_crosscheck_failures": word_crosscheck_failures,
    }
    deterministic_surface["sha256"] = digest(deterministic_surface)
    return {
        **deterministic_surface,
        "_evaluation_rows": tuple(all_rows),
        "_covariance_rows": tuple(all_covariance),
    }


def family_battery_signature(
    alternatives: tuple[tuple[int, ...], ...],
    fixtures: tuple[
        tuple[int, tuple[int, int], tuple[object, ...], int, int], ...
    ],
) -> tuple[dict[str, object], ...]:
    rows = []
    for event, _direction, program, before, _expected in fixtures:
        selected = evaluate_family(
            program, before, alternatives
        )["selected"]
        rows.append(
            {
                "event": event,
                "outcome_class": outcome_class(selected),
                "selected": selected,
            }
        )
    return tuple(rows)


def sampled_reduction_battery_audit() -> dict[str, object]:
    """Actually rerun member-rooted families for one k=3 and one k=4 orbit."""

    fixtures = own_fixtures()
    sample_rows = []
    passed = True
    for k in TARGET_STRATA:
        families = own_families(independent_positions(k))
        representative = next(iter(families))
        members = families[representative]
        roots = (members[0], members[3], members[7])
        baseline = family_battery_signature(members, fixtures)
        root_rows = []
        for root in roots:
            rerooted = own_orbit(root)
            observed = family_battery_signature(rerooted, fixtures)
            exact = rerooted == members and observed == baseline
            passed &= exact
            root_rows.append(
                {
                    "root": root,
                    "rerooted_set_identical": rerooted == members,
                    "battery_signature_identical": observed == baseline,
                    "battery_signature": observed,
                }
            )
        sample_rows.append(
            {
                "k": k,
                "representative": representative,
                "members_in_family": len(members),
                "member_roots_actually_run": roots,
                "baseline_battery_signature": baseline,
                "root_checks": tuple(root_rows),
            }
        )
    return {
        "families_actually_rerun": len(sample_rows),
        "member_roots_per_family": 3,
        "rows": tuple(sample_rows),
        "pass": passed,
        "interpretation": (
            "Changing the representative regenerates the identical complete "
            "alternative set and therefore the identical four-epoch census. "
            "Program-translation covariance is tested separately and may "
            "fail without discarding any configuration."
        ),
    }


def alternative_features(
    alternative: tuple[int, ...],
    program: tuple[object, ...],
) -> dict[str, object]:
    roles = tuple(program[station][0] for station in alternative)
    return {
        "gate_count": sum(
            len(K.mapped_macro(program[station]))
            for station in alternative
        ),
        "relay_occupancy": sum(role == "relay" for role in roles),
        "handoff_occupancy": sum(
            role == "handoff" for role in roles
        ),
        "station_roles": roles,
    }


def own_unique_extremum(
    values: dict[tuple[int, ...], int],
    direction: str,
) -> dict[str, object]:
    extremal = (
        min(values.values())
        if direction == "minimum"
        else max(values.values())
    )
    winners = tuple(
        alternative
        for alternative, value in values.items()
        if value == extremal
    )
    return {
        "values": values,
        "extremal_value": extremal,
        "winners": winners,
        "selection": winners[0] if len(winners) == 1 else None,
        "refusal": len(winners) != 1,
    }


def build_tie_catalog(
    experiment: dict[str, object],
) -> tuple[dict[str, object], ...]:
    programs = {
        event: program
        for event, _direction, program, _before, _expected
        in own_fixtures()
    }
    ties = []
    for row in experiment["_evaluation_rows"]:
        if row["outcome_class"] != "exact_tie":
            continue
        alternatives = row["selected"]
        features = {
            alternative: alternative_features(
                alternative, programs[row["event"]]
            )
            for alternative in alternatives
        }
        functionals = {}
        for name, feature, direction in FUNCTIONAL_SPECS:
            values = {
                alternative: int(feature_row[feature])
                for alternative, feature_row in features.items()
            }
            functionals[name] = {
                "feature": feature,
                "direction": direction,
                **own_unique_extremum(values, direction),
            }
        decisive_selections = tuple(
            functional["selection"]
            for functional in functionals.values()
            if functional["selection"] is not None
        )
        selection_counts = Counter(decisive_selections)
        three_to_one = (
            len(decisive_selections) == 4
            and tuple(sorted(selection_counts.values())) == (1, 3)
        )
        ties.append(
            {
                "tie_id": (
                    f"k{row['k']}:"
                    f"{'-'.join(map(str, row['representative']))}:"
                    f"e{row['event']}"
                ),
                "k": row["k"],
                "representative": row["representative"],
                "event": row["event"],
                "alternatives": alternatives,
                "features": features,
                "functionals": functionals,
                "three_to_one_disagreement": three_to_one,
                "selection_multiplicities":
                    dict(sorted(selection_counts.items())),
                "occupancy_functional_refusal": (
                    functionals[
                        "initial_relay_station_occupancy_minimum"
                    ]["refusal"]
                    or functionals[
                        "initial_handoff_station_occupancy_maximum"
                    ]["refusal"]
                ),
                "selector_status": "OPEN",
            }
        )
    return tuple(ties)


def tie_aggregate(
    tie_catalog: tuple[dict[str, object], ...]
) -> dict[str, object]:
    decisive_counts = {}
    for name, _feature, _direction in FUNCTIONAL_SPECS:
        decisive_counts[name] = sum(
            not tie["functionals"][name]["refusal"]
            for tie in tie_catalog
        )

    frozen_rows = tuple(
        tie
        for tie in tie_catalog
        if tie["k"] == 3
        and tie["event"] == 0
        and tie["alternatives"] == FROZEN_TIE
    )
    frozen_values = ()
    frozen_selections = {}
    if len(frozen_rows) == 1:
        frozen = frozen_rows[0]
        gate_min = frozen["functionals"][
            "first_Q_layer_physical_gate_count_minimum"
        ]
        frozen_values = tuple(
            gate_min["values"][alternative]
            for alternative in FROZEN_TIE
        )
        frozen_selections = {
            name: frozen["functionals"][name]["selection"]
            for name, _feature, _direction in FUNCTIONAL_SPECS
        }

    return {
        "tie_count": len(tie_catalog),
        "decisive_counts": decisive_counts,
        "three_to_one_count": sum(
            tie["three_to_one_disagreement"] for tie in tie_catalog
        ),
        "three_to_one_tie_ids": tuple(
            tie["tie_id"]
            for tie in tie_catalog
            if tie["three_to_one_disagreement"]
        ),
        "occupancy_refusal_row_count": sum(
            tie["occupancy_functional_refusal"]
            for tie in tie_catalog
        ),
        "occupancy_refusal_tie_ids": tuple(
            tie["tie_id"]
            for tie in tie_catalog
            if tie["occupancy_functional_refusal"]
        ),
        "frozen_tie_occurrences": len(frozen_rows),
        "frozen_gate_values": frozen_values,
        "frozen_selections": frozen_selections,
    }


def failure_signature(
    evaluation: dict[str, object]
) -> tuple[str, ...]:
    return tuple(
        name
        for name, passed in evaluation["conditions"].items()
        if not passed
    )


def exclusion_mechanism_rows(
    rows: tuple[dict[str, object], ...],
) -> dict[str, object]:
    signatures: Counter[tuple[str, ...]] = Counter()
    failed_conditions: Counter[str] = Counter()
    residuals: Counter[tuple[int, int, int]] = Counter()
    survivors = 0
    evaluations = 0
    for row in rows:
        for evaluation in row["evaluations"]:
            evaluations += 1
            survivors += bool(evaluation["survivor"])
            signature = failure_signature(evaluation)
            signatures[signature] += 1
            for condition in signature:
                failed_conditions[condition] += 1
            residuals[evaluation["postimage_residual"]] += 1
    return {
        "evaluations": evaluations,
        "survivors": survivors,
        "failure_signature_census": dict(sorted(signatures.items())),
        "failed_condition_census":
            dict(sorted(failed_conditions.items())),
        "postimage_residual_census": dict(sorted(residuals.items())),
    }


def k4_over_exclusion_probe(
    experiment: dict[str, object],
) -> dict[str, object]:
    k4_rows = tuple(
        row for row in experiment["_evaluation_rows"] if row["k"] == 4
    )
    k4_mechanisms = exclusion_mechanism_rows(k4_rows)

    fixtures = own_fixtures()
    k2_families = own_families(independent_positions(2))
    k2_rows = []
    for representative, alternatives in k2_families.items():
        for event, direction, program, before, _expected in fixtures:
            result = evaluate_family(program, before, alternatives)
            k2_rows.append(
                {
                    "k": 2,
                    "representative": representative,
                    "event": event,
                    "direction": direction,
                    "evaluations": result["evaluations"],
                }
            )
    k2_mechanisms = exclusion_mechanism_rows(tuple(k2_rows))

    representatives = tuple(
        sorted({row["representative"] for row in k4_rows})
    )
    samples = []
    for index, representative in enumerate(representatives):
        event = index % len(fixtures)
        row = next(
            candidate
            for candidate in k4_rows
            if candidate["representative"] == representative
            and candidate["event"] == event
        )
        samples.append(
            {
                "representative": representative,
                "event": event,
                "alternative_traces": tuple(
                    {
                        "positions": evaluation["positions"],
                        "failed_exclusions":
                            failure_signature(evaluation),
                        "postimage_residual":
                            evaluation["postimage_residual"],
                    }
                    for evaluation in row["evaluations"]
                ),
            }
        )

    clean_only_signature = {("clean_postimage",)}
    k4_signatures = set(
        k4_mechanisms["failure_signature_census"]
    )
    k2_signatures = set(
        k2_mechanisms["failure_signature_census"]
    )
    return {
        "k4_full_mechanism_census": k4_mechanisms,
        "k2_758_mechanism_control": k2_mechanisms,
        "sampled_k4_family_epochs": tuple(samples),
        "sample_count": len(samples),
        "same_veto_as_k2": (
            k4_signatures == clean_only_signature
            and k2_signatures == clean_only_signature
        ),
        "mechanism": "clean_postimage_only",
    }


def primary_blocklist_and_anchor_control() -> dict[str, object]:
    path = ROOT / PRIMARY_PATH
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=PRIMARY_PATH)
    imported_names = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            imported_names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_names.add(node.module)
    source_hashes = {
        relative: file_sha256(relative)
        for relative in (*AUDIT_INPUT_PATHS, PRIMARY_PATH)
    }
    sha_matches = {
        relative: observed == EXPECTED_SHA256[relative]
        for relative, observed in source_hashes.items()
    }
    fixture_match = own_fixtures() == F750.k_epoch_fixtures(
        FIXTURE_BANKS
    )
    return {
        "source_sha256": source_hashes,
        "sha_anchor_matches": sha_matches,
        "all_sha_anchors_match": all(sha_matches.values()),
        "primary_ast_module": isinstance(tree, ast.Module),
        "primary_top_level_import_names": tuple(sorted(imported_names)),
        "primary_execution_mode": "text_and_AST_only",
        "primary_not_imported": PRIMARY_MODULE not in sys.modules,
        "own_fixtures_match_landed_750": fixture_match,
        "audit_input_paths_literal_value": AUDIT_INPUT_PATHS,
        "declared_is_audit_tuple": (
            DECLARED_INPUT_PATHS is AUDIT_INPUT_PATHS
        ),
    }


def stripped_experiment_surface(
    experiment: dict[str, object]
) -> dict[str, object]:
    return {
        key: value
        for key, value in experiment.items()
        if not key.startswith("_")
    }


def census_claim_matches(experiment: dict[str, object]) -> bool:
    for k in TARGET_STRATA:
        observed = experiment["strata"][str(k)]
        expected = EXPECTED_STRATA[k]
        if not (
            observed["configuration_count"]
            == expected["configuration_count"]
            and observed["translation_family_count"]
            == expected["translation_family_count"]
            and observed["family_epoch_count"]
            == expected["family_epoch_count"]
            and observed["outcome_counts"]
            == expected["outcome_counts"]
            and observed["covariance_failure_family_count"]
            == expected["covariance_failure_families"]
        ):
            return False
    return True


def main() -> int:
    started = monotonic()
    data_lines: list[str] = []

    anchors = primary_blocklist_and_anchor_control()
    reduction = reduction_surface()
    reduction_battery = sampled_reduction_battery_audit()
    data_lines.append("ANCHOR_BLOCKLIST_CONTROL " + compact(anchors))
    data_lines.append("REDUCTION_AUDIT " + compact(reduction))
    for row in reduction_battery["rows"]:
        data_lines.append(
            "REDUCTION_BATTERY_FAMILY " + compact(row)
        )

    reduction_matches_claim = all(
        (
            reduction["strata"][str(k)]["configuration_count"]
            == EXPECTED_STRATA[k]["configuration_count"]
            and reduction["strata"][str(k)][
                "translation_family_count"
            ]
            == EXPECTED_STRATA[k]["translation_family_count"]
            and reduction["strata"][str(k)]["family_epoch_count"]
            == EXPECTED_STRATA[k]["family_epoch_count"]
        )
        for k in TARGET_STRATA
    )
    certificate_reduction = (
        reduction["partition_complete"]
        and reduction_matches_claim
        and all(
            reduction["strata"][str(k)][
                "landed_reduction_crosscheck"
            ]
            for k in TARGET_STRATA
        )
        and reduction_battery["pass"]
    )

    experiment = run_full_census()
    second_experiment = run_full_census()
    deterministic = (
        experiment["sha256"] == second_experiment["sha256"]
        and stripped_experiment_surface(experiment)
        == stripped_experiment_surface(second_experiment)
    )
    for k in TARGET_STRATA:
        stratum = experiment["strata"][str(k)]
        data_lines.append(
            f"CENSUS_SUMMARY k={k} "
            + compact(
                {
                    key: value
                    for key, value in stratum.items()
                    if key not in {"rows", "covariance"}
                }
            )
        )
        for row in stratum["rows"]:
            data_lines.append(
                f"CENSUS_FAMILY_EPOCH k={k} " + compact(row)
            )
        for row in stratum["covariance"]:
            data_lines.append(
                f"COVARIANCE_FAMILY k={k} " + compact(row)
            )
    certificate_census = (
        census_claim_matches(experiment)
        and experiment["word_crosscheck_failures"] == 0
    )

    ties = build_tie_catalog(experiment)
    tie_summary = tie_aggregate(ties)
    for tie in ties:
        data_lines.append("TIE_FUNCTIONAL_ROW " + compact(tie))
    data_lines.append(
        "TIE_FUNCTIONAL_AGGREGATE " + compact(tie_summary)
    )
    expected_decisive = {
        "first_Q_layer_physical_gate_count_minimum": 7,
        "first_Q_layer_physical_gate_count_maximum": 7,
        "initial_relay_station_occupancy_minimum": 5,
        "initial_handoff_station_occupancy_maximum": 1,
    }
    frozen_expected_selections = {
        "first_Q_layer_physical_gate_count_minimum": (0, 7, 9),
        "first_Q_layer_physical_gate_count_maximum": (0, 2, 9),
        "initial_relay_station_occupancy_minimum": (0, 2, 9),
        "initial_handoff_station_occupancy_maximum": (0, 2, 9),
    }
    certificate_ties = (
        tie_summary["tie_count"] == 7
        and tie_summary["decisive_counts"] == expected_decisive
        and tie_summary["three_to_one_count"] == 1
        and tie_summary["occupancy_refusal_row_count"] == 6
        and tie_summary["frozen_tie_occurrences"] == 1
        and tie_summary["frozen_gate_values"] == (769, 1350, 610)
        and tie_summary["frozen_selections"]
        == frozen_expected_selections
        and all(tie["selector_status"] == "OPEN" for tie in ties)
    )

    mechanism = k4_over_exclusion_probe(experiment)
    data_lines.append(
        "K4_EXCLUSION_MECHANISM_CENSUS "
        + compact(mechanism["k4_full_mechanism_census"])
    )
    data_lines.append(
        "K2_CLEAN_POSTIMAGE_CONTROL "
        + compact(mechanism["k2_758_mechanism_control"])
    )
    for sample in mechanism["sampled_k4_family_epochs"]:
        data_lines.append(
            "K4_EXCLUSION_SAMPLE " + compact(sample)
        )
    certificate_k4 = (
        mechanism["same_veto_as_k2"]
        and mechanism["k4_full_mechanism_census"]["evaluations"]
        == 55 * 4
        and mechanism["k4_full_mechanism_census"]["survivors"] == 0
        and mechanism["k2_758_mechanism_control"]["evaluations"]
        == 44 * 4
        and mechanism["k2_758_mechanism_control"]["survivors"] == 0
        and mechanism["sample_count"] == 5
    )

    elapsed = monotonic() - started
    projected_stdout_ok = (
        len("\n".join(data_lines).encode("utf-8")) + 20_000
        < STDOUT_LIMIT_BYTES
    )
    certificate_controls = (
        anchors["all_sha_anchors_match"]
        and anchors["primary_ast_module"]
        and anchors["primary_execution_mode"] == "text_and_AST_only"
        and anchors["primary_not_imported"]
        and anchors["own_fixtures_match_landed_750"]
        and anchors["declared_is_audit_tuple"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_ok
    )

    certificates = (
        (
            "CERTIFICATE_1_THE_REDUCTION_AUDIT",
            certificate_reduction,
            {
                "equivalence": reduction["equivalence"],
                "k3": reduction["strata"]["3"],
                "k4": reduction["strata"]["4"],
                "battery_families_actually_rerun":
                    reduction_battery["families_actually_rerun"],
                "member_roots_per_family":
                    reduction_battery["member_roots_per_family"],
                "verdict": (
                    "LAWFUL_LOSSLESS_BATCHING"
                    if certificate_reduction
                    else "UNLAWFUL_OR_INCOMPLETE_REDUCTION"
                ),
            },
        ),
        (
            "CERTIFICATE_2_CENSUS_RECOUNT",
            certificate_census,
            {
                "k3": {
                    "outcomes":
                        experiment["strata"]["3"]["outcome_counts"],
                    "covariance_failure_families":
                        experiment["strata"]["3"][
                            "covariance_failure_family_count"
                        ],
                },
                "k4": {
                    "outcomes":
                        experiment["strata"]["4"]["outcome_counts"],
                    "covariance_failure_families":
                        experiment["strata"]["4"][
                            "covariance_failure_family_count"
                        ],
                },
                "class_flip": not census_claim_matches(experiment),
            },
        ),
        (
            "CERTIFICATE_3_TIE_CATALOG_FUNCTIONALS",
            certificate_ties,
            tie_summary,
        ),
        (
            "CERTIFICATE_4_K4_OVER_EXCLUSION_PROBE",
            certificate_k4,
            {
                "k4_evaluations":
                    mechanism["k4_full_mechanism_census"][
                        "evaluations"
                    ],
                "k4_failure_signatures":
                    mechanism["k4_full_mechanism_census"][
                        "failure_signature_census"
                    ],
                "same_veto_as_k2": mechanism["same_veto_as_k2"],
                "mechanism": mechanism["mechanism"],
            },
        ),
        (
            "CERTIFICATE_5_CONTROLS",
            certificate_controls,
            {
                "sha_anchors": anchors["all_sha_anchors_match"],
                "primary_text_AST_only":
                    anchors["primary_not_imported"],
                "deterministic": deterministic,
                "first_sha256": experiment["sha256"],
                "second_sha256": second_experiment["sha256"],
                "runtime_seconds": round(elapsed, 6),
                "runtime_under_1500s":
                    elapsed < AUDIT_TIMEOUT_SEC,
                "stdout_projected_under_150KB":
                    projected_stdout_ok,
                "ties_remain_open": all(
                    tie["selector_status"] == "OPEN" for tie in ties
                ),
                "probability_or_weights_used": False,
            },
        ),
    )

    if certificate_reduction:
        data_lines.append(
            "FINDING REDUCTION VERBATIM :: CONFIRMED: 77 configurations "
            "partition exactly once into 7 C11 translation families and "
            "55 partition exactly once into 5; four epochs give 28 and 20 "
            "family-epochs. The family unit retains all 11 configurations; "
            "member-rooted reruns on two families preserve the census."
        )
    else:
        data_lines.append(
            "!!! REFUTATION FINDING REDUCTION VERBATIM :: UNLAWFUL OR "
            "INCOMPLETE REDUCTION; THE CENSUS IS INVALID."
        )
    if certificate_census:
        data_lines.append(
            "FINDING CENSUS VERBATIM :: CONFIRMED: k=3 is 3 unique, 7 "
            "exact ties, 18 zero-survivor with 5 covariance-failing "
            "families; k=4 is 20/20 zero-survivor."
        )
    else:
        data_lines.append(
            "!!! REFUTATION FINDING CENSUS VERBATIM :: CLASS FLIP OR "
            "COVARIANCE-COUNT ERROR DETECTED."
        )
    if certificate_ties:
        data_lines.append(
            "FINDING DECISIVENESS VERBATIM :: CONFIRMED: gate-count min/max "
            "are decisive 7/7, relay-min 5/7, handoff-max 1/7; exactly one "
            "3-to-1 row and six occupancy-refusal rows; frozen values are "
            "769/1350/610."
        )
    else:
        data_lines.append(
            "!!! REFUTATION FINDING DECISIVENESS VERBATIM :: TIE CATALOG, "
            "FUNCTIONAL COUNT, RECURRENCE, REFUSAL, OR FROZEN CONTROL ERROR."
        )
    if certificate_k4:
        data_lines.append(
            "FINDING K4 MECHANISM VERBATIM :: CONFIRMED: every one of 220 "
            "k=4 alternatives is killed only by clean_postimage, the same "
            "sole veto observed in the exhaustive 176-case k=2 control."
        )
    else:
        data_lines.append(
            "!!! REFUTATION FINDING K4 MECHANISM VERBATIM :: A k=4 "
            "ALTERNATIVE SURVIVED OR AN EXCLUSION OTHER THAN THE CLAIMED "
            "CLEAN_POSTIMAGE MECHANISM WAS LOAD-BEARING."
        )

    for name, passed, detail in certificates:
        data_lines.append(
            f"{'PASS' if passed else 'FAIL'} {name} :: "
            + compact(detail)
        )
    passed = all(row[1] for row in certificates)
    terminal = {
        "terminal": (
            "CYCLE784_PRIMARY_CONFIRMED"
            if passed
            else "CYCLE784_PRIMARY_REFUTED"
        ),
        "pass": passed,
        "reduction_verdict": (
            "lawful_complete"
            if certificate_reduction
            else "unlawful_or_incomplete"
        ),
        "census_agreement": certificate_census,
        "decisiveness_agreement": certificate_ties,
        "k4_mechanism": (
            "clean_postimage_only"
            if certificate_k4
            else "mechanism_mismatch"
        ),
        "runtime_seconds": round(elapsed, 6),
    }
    data_lines.append("FINAL " + compact(terminal))
    output = "\n".join(data_lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout_limit", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
