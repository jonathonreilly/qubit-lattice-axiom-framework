#!/usr/bin/env python3
"""Cycle 792: supplied extended-horizon test of the k=2 selector battery.

The Cycle-758 selector is reconstructed from its text-only reference and the
landed Cycle-736, Cycle-750, and Cycle-719 suppliers.  The landed acceptance
test observes the immediate postimage (horizon t=0).  This runner additionally
measures a SUPPLIED acceptance-law change: after the landed postimage, repeat
the same full landed controller orbit and test cleanliness at an explicit
horizon.  That horizon extension is not promoted to landed law here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
LANDED_POSTIMAGE_HORIZON = 0
CONTROL_HORIZON = 251
EXTENDED_HORIZON = 252
TARGET_EVENT = 3
TARGET_POSITIONS = (1, 10)
TARGET_KEY = (TARGET_EVENT, TARGET_POSITIONS)
STDOUT_LIMIT_BYTES = 150 * 1024

REFERENCE_PATH = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py"
)
REFERENCE_MODULE = (
    "frontier_cycle758_selector_multisource_2026_07_28"
)
REFERENCE_REQUESTED_REF = (
    "origin/physics-loop/toe-close-blockA5-20260729:"
    + REFERENCE_PATH
)
REFERENCE_SOURCE_COMMIT = (
    "7a120caef64c8aacccb4c350594b8e91cca2f9c2"
)
REFERENCE_GIT_BLOB_SHA1 = "4e23e03ecc5f92a0b8348bfa526eb5b2f2b09dd0"
M736_GIT_BLOB_SHA1 = "8ddd84104dc0729107cebfb0d0cd694fe78af1af"
EXPECTED_HORIZON_CENSUS_SHA256 = (
    "992e2e74126239826df5c9f170ef5267effaa855b579ebd9eb4c784a8d12ad39"
)

SUPPLIED_SCOPE_STATEMENT = (
    "the horizon extension is a SUPPLIED change to the acceptance law, "
    "not a landed law"
)
SUPPLIED_EXTENSION_DEFINITION = (
    "Starting from the landed immediate postimage, apply the same complete "
    "landed K.run_orbit with the same token positions once per horizon tick; "
    "only the clean_postimage observation horizon changes."
)
NO_ACTUALITY_STATEMENT = (
    "No actuality claim: the extension is supplied, and the "
    "horizon-extended postimage LAW remains the derivation target."
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_bytes(relative_path: str) -> bytes:
    return (ROOT / relative_path).read_bytes()


def file_sha256(relative_path: str) -> str:
    return sha256(file_bytes(relative_path)).hexdigest()


def git_blob_sha1(relative_path: str) -> str:
    payload = file_bytes(relative_path)
    framed = b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload
    return sha1(framed).hexdigest()


def state_sha256(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def configuration_families(
    positions_rows: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for positions in positions_rows:
        representative = min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        )
        grouped.setdefault(representative, set()).add(positions)
    return {
        representative: tuple(sorted(alternatives))
        for representative, alternatives in sorted(grouped.items())
    }


def landed_clean_postimage(
    state: tuple[int, ...], bank_count: int
) -> bool:
    """The Cycle-758/F750 terminal-postimage predicate, unchanged."""

    banks, links = K.M.unpack_state(state, bank_count)
    return not any(
        (
            state[K.R3.X.SOURCE_POINTER],
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


def expected_synchronization_trace(
    positions: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            rotate_positions(positions, step),
            rotate_positions(positions, step + 1),
            0,
        )
        for step in range(RING_STATIONS)
    )


def base_battery_evaluation(
    event: int,
    direction: tuple[int, int],
    program: tuple[object, ...],
    before: tuple[int, ...],
    positions: tuple[int, ...],
    k2_members: frozenset[tuple[int, ...]],
) -> dict[str, object]:
    """Reconstruct every landed non-horizon exclusion for one alternative."""

    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(value ^ value for value in tokens)
    composition_word = M736.synchronous_composition_word(
        program, positions
    )
    expected = K.A.apply_semantic(before, composition_word)
    after, rail_a, rail_b, trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    config = tuple(
        int(station in positions) for station in range(RING_STATIONS)
    )
    expected_trace = expected_synchronization_trace(positions)
    conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "census_membership": positions in k2_members,
        "pairwise_separation": M736.is_pairwise_separated(config),
        "synchronization": trace == expected_trace,
    }
    evidence = {
        "event": event,
        "direction": direction,
        "positions": positions,
        "configuration_mask": sum(1 << station for station in positions),
        "pairwise_circular_distances":
            M736.pairwise_circular_distances(
                positions, RING_STATIONS
            ),
        "composition_word_gates": len(composition_word),
        "composition_word_sha256": K.gate_digest(composition_word),
        "before_state_sha256": state_sha256(before),
        "expected_state_sha256": state_sha256(expected),
        "after_state_sha256": state_sha256(after),
        "restored_state_sha256": state_sha256(restored),
        "token_rail_a": tuple(
            station for station, value in enumerate(rail_a) if value
        ),
        "token_rail_b_weight": sum(rail_b),
        "inverse_rail_a": tuple(
            station for station, value in enumerate(inverse_a) if value
        ),
        "inverse_rail_b_weight": sum(inverse_b),
        "synchronization_steps": len(trace),
        "synchronization_trace_sha256": digest(trace),
        "inverse_trace_sha256": digest(inverse_trace),
        "landed_postimage_clean":
            landed_clean_postimage(after, FIXTURE_BANKS),
    }
    return {
        "key": (event, positions),
        "event": event,
        "direction": direction,
        "program": program,
        "before": before,
        "positions": positions,
        "tokens": tokens,
        "after": after,
        "conditions": conditions,
        "evidence": evidence,
    }


def horizon_trajectory(
    evaluation: dict[str, object], maximum_horizon: int
) -> dict[str, object]:
    """Apply the SUPPLIED repeated-orbit horizon extension."""

    if maximum_horizon < LANDED_POSTIMAGE_HORIZON:
        raise ValueError(maximum_horizon)
    state = evaluation["after"]
    program = evaluation["program"]
    positions = evaluation["positions"]
    tokens = evaluation["tokens"]
    zeros = tuple(0 for _value in tokens)
    statuses = {
        LANDED_POSTIMAGE_HORIZON:
            landed_clean_postimage(state, FIXTURE_BANKS)
    }
    first_clean = (
        LANDED_POSTIMAGE_HORIZON
        if statuses[LANDED_POSTIMAGE_HORIZON]
        else None
    )
    seen = {state: LANDED_POSTIMAGE_HORIZON}
    first_cycle = None
    horizon_transport_failures = 0
    for horizon in range(1, maximum_horizon + 1):
        state, rail_a, rail_b, _trace = K.run_orbit(
            state, program, token_positions=positions
        )
        horizon_transport_failures += (
            rail_a != tokens or rail_b != zeros
        )
        clean = landed_clean_postimage(state, FIXTURE_BANKS)
        if horizon in (CONTROL_HORIZON, EXTENDED_HORIZON):
            statuses[horizon] = clean
        if clean and first_clean is None:
            first_clean = horizon
        if state in seen and first_cycle is None:
            first_cycle = {
                "entry_horizon": seen[state],
                "return_horizon": horizon,
                "period": horizon - seen[state],
            }
        else:
            seen[state] = horizon
    return {
        "key": evaluation["key"],
        "first_clean_horizon": first_clean,
        "clean_at": statuses,
        "cycle": first_cycle,
        "horizon_transport_failures": horizon_transport_failures,
        "final_state_sha256": state_sha256(state),
    }


def selector_conditions(
    evaluation: dict[str, object],
    trajectory: dict[str, object],
    horizon: int,
) -> dict[str, bool]:
    conditions = dict(evaluation["conditions"])
    conditions["clean_postimage"] = bool(
        trajectory["clean_at"][horizon]
    )
    return conditions


def header_and_reference_audit() -> dict[str, object]:
    runner_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = {}
    imported_modules = {}
    for node in runner_tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
            for target in targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules[alias.asname or alias.name] = alias.name

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    literal_audit_tuple = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 3
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in audit_node.elts
        )
    )
    expected_imports = {
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "M736":
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "K":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    }
    reference_blob = git_blob_sha1(REFERENCE_PATH)
    source_anchors = {
        path: {
            "sha256": file_sha256(path),
            "git_blob_sha1": git_blob_sha1(path),
        }
        for path in AUDIT_INPUT_PATHS + (REFERENCE_PATH,)
    }
    supplier_imports = {
        alias: imported_modules.get(alias)
        for alias in ("F750", "M736", "K")
    }
    return {
        "pass": (
            literal_audit_tuple
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
            and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
            and supplier_imports == expected_imports
            and REFERENCE_MODULE not in imported_modules.values()
            and REFERENCE_MODULE not in sys.modules
            and reference_blob == REFERENCE_GIT_BLOB_SHA1
            and source_anchors[AUDIT_INPUT_PATHS[1]][
                "git_blob_sha1"
            ]
            == M736_GIT_BLOB_SHA1
        ),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_audit_tuple": literal_audit_tuple,
        "direct_supplier_imports": supplier_imports,
        "reference_blocklisted_from_imports": (
            REFERENCE_MODULE not in imported_modules.values()
            and REFERENCE_MODULE not in sys.modules
        ),
        "reference_requested_ref": REFERENCE_REQUESTED_REF,
        "requested_ref_resolution": (
            "The refreshed requested A5 ref ends at Cycle 754 and lacks the "
            "path; the exact landed Cycle-758 blob was resolved from its "
            "Cycle-758 commit without semantic substitution."
        ),
        "reference_source_commit": REFERENCE_SOURCE_COMMIT,
        "reference_git_blob_sha1": reference_blob,
        "reference_sha256": file_sha256(REFERENCE_PATH),
        "source_anchors": source_anchors,
    }


def family_selected_matrix(
    families: dict[
        tuple[int, ...], tuple[tuple[int, ...], ...]
    ],
    rows: dict[tuple[int, tuple[int, ...]], dict[str, object]],
    trajectories: dict[
        tuple[int, tuple[int, ...]], dict[str, object]
    ],
    horizon: int,
) -> dict[str, list[int]]:
    matrix = {}
    for representative, alternatives in families.items():
        counts = []
        for event in range(2 * FIXTURE_BANKS):
            counts.append(
                sum(
                    all(
                        selector_conditions(
                            rows[(event, positions)],
                            trajectories[(event, positions)],
                            horizon,
                        ).values()
                    )
                    for positions in alternatives
                )
            )
        matrix[",".join(map(str, representative))] = counts
    return matrix


def run_experiment() -> dict[str, object]:
    census = M736.configuration_census()
    configurations = census["configurations"]
    k2_positions = tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 2
    )
    k2_members = frozenset(k2_positions)
    families = configuration_families(k2_positions)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)

    rows = {}
    for event, direction, program, before, _single_expected in fixtures:
        for positions in k2_positions:
            evaluation = base_battery_evaluation(
                event,
                direction,
                program,
                before,
                positions,
                k2_members,
            )
            rows[(event, positions)] = evaluation

    trajectories = {
        key: horizon_trajectory(evaluation, EXTENDED_HORIZON)
        for key, evaluation in rows.items()
    }

    target_rerun = horizon_trajectory(
        rows[TARGET_KEY], EXTENDED_HORIZON
    )
    horizon_summary = tuple(
        {
            "event": key[0],
            "positions": key[1],
            "first_clean_horizon": trajectory[
                "first_clean_horizon"
            ],
            "clean_t251": trajectory["clean_at"][CONTROL_HORIZON],
            "clean_t252": trajectory["clean_at"][EXTENDED_HORIZON],
            "cycle": trajectory["cycle"],
            "horizon_transport_failures":
                trajectory["horizon_transport_failures"],
            "final_state_sha256": trajectory["final_state_sha256"],
        }
        for key, trajectory in sorted(trajectories.items())
    )
    horizon_census_sha256 = digest(horizon_summary)

    standard_failure_census: Counter[str] = Counter()
    all_non_horizon_conditions_pass = True
    standard_selected = []
    extended_selected = []
    for key, evaluation in rows.items():
        base_conditions = evaluation["conditions"]
        all_non_horizon_conditions_pass &= all(
            base_conditions.values()
        )
        for condition, passed in base_conditions.items():
            if not passed:
                standard_failure_census[condition] += 1
        standard_clean = trajectories[key]["clean_at"][
            LANDED_POSTIMAGE_HORIZON
        ]
        if not standard_clean:
            standard_failure_census["clean_postimage"] += 1
        if all(base_conditions.values()) and standard_clean:
            standard_selected.append(key)
        extended_clean = trajectories[key]["clean_at"][
            EXTENDED_HORIZON
        ]
        if all(base_conditions.values()) and extended_clean:
            extended_selected.append(key)

    control_positions = (
        TARGET_POSITIONS,
        (0, 2),
        (0, 3),
        (1, 3),
        (0, 4),
        (1, 4),
    )
    identity_controls = []
    for positions in control_positions:
        key = (TARGET_EVENT, positions)
        landed_conditions = selector_conditions(
            rows[key],
            trajectories[key],
            LANDED_POSTIMAGE_HORIZON,
        )
        identity_controls.append(
            {
                "event": TARGET_EVENT,
                "positions": positions,
                "selected": all(landed_conditions.values()),
                "conditions": landed_conditions,
                "firing_exclusions": tuple(
                    name
                    for name, passed in landed_conditions.items()
                    if not passed
                ),
            }
        )

    matrices = {
        f"t{LANDED_POSTIMAGE_HORIZON}":
            family_selected_matrix(
                families,
                rows,
                trajectories,
                LANDED_POSTIMAGE_HORIZON,
            ),
        f"t{CONTROL_HORIZON}":
            family_selected_matrix(
                families, rows, trajectories, CONTROL_HORIZON
            ),
        f"t{EXTENDED_HORIZON}":
            family_selected_matrix(
                families, rows, trajectories, EXTENDED_HORIZON
            ),
    }
    target_representative = next(
        representative
        for representative, alternatives in families.items()
        if TARGET_POSITIONS in alternatives
    )
    target_alternatives = families[target_representative]
    target_side_by_side = {}
    for horizon in (CONTROL_HORIZON, EXTENDED_HORIZON):
        selected = tuple(
            positions
            for positions in target_alternatives
            if all(
                selector_conditions(
                    rows[(TARGET_EVENT, positions)],
                    trajectories[(TARGET_EVENT, positions)],
                    horizon,
                ).values()
            )
        )
        target_side_by_side[f"t{horizon}"] = {
            "selected": selected,
            "selected_count": len(selected),
            "verdict": "SELECTED" if selected else "STILL_EXCLUDED",
        }

    survivor_certificates = []
    for key in extended_selected:
        evaluation = rows[key]
        trajectory = trajectories[key]
        conditions = selector_conditions(
            evaluation, trajectory, EXTENDED_HORIZON
        )
        survivor_certificates.append(
            {
                "event": key[0],
                "positions": key[1],
                "conditions": conditions,
                "evidence": evaluation["evidence"],
                "postimage_horizon_certificate": {
                    "landed_horizon":
                        LANDED_POSTIMAGE_HORIZON,
                    "landed_clean":
                        trajectory["clean_at"][
                            LANDED_POSTIMAGE_HORIZON
                        ],
                    "control_horizon": CONTROL_HORIZON,
                    "control_clean":
                        trajectory["clean_at"][CONTROL_HORIZON],
                    "extended_horizon": EXTENDED_HORIZON,
                    "extended_clean":
                        trajectory["clean_at"][EXTENDED_HORIZON],
                    "first_clean_horizon":
                        trajectory["first_clean_horizon"],
                    "final_state_sha256":
                        trajectory["final_state_sha256"],
                },
            }
        )

    cycle_controls = tuple(
        {
            "event": key[0],
            "positions": key[1],
            **trajectory["cycle"],
        }
        for key, trajectory in sorted(trajectories.items())
        if trajectory["cycle"] is not None
    )
    other_keys = tuple(
        key for key in sorted(rows) if key != TARGET_KEY
    )
    other_clean_at_252 = tuple(
        key
        for key in other_keys
        if trajectories[key]["clean_at"][EXTENDED_HORIZON]
    )
    first_clean_through_252 = tuple(
        (
            key,
            trajectory["first_clean_horizon"],
        )
        for key, trajectory in sorted(trajectories.items())
        if trajectory["first_clean_horizon"] is not None
    )

    expected_zero_matrix = {
        "0,2": [0, 0, 0, 0],
        "0,3": [0, 0, 0, 0],
        "0,4": [0, 0, 0, 0],
        "0,5": [0, 0, 0, 0],
    }
    expected_extended_matrix = {
        **expected_zero_matrix,
        "0,2": [0, 0, 0, 1],
    }
    battery_pass = (
        census["agreement"]
        and len(k2_positions) == M736.EXPECTED_COUNTS_BY_K[2] == 44
        and tuple(families) == ((0, 2), (0, 3), (0, 4), (0, 5))
        and all(len(alternatives) == RING_STATIONS
                for alternatives in families.values())
        and len(rows) == 176
        and all_non_horizon_conditions_pass
        and dict(standard_failure_census)
        == {"clean_postimage": 176}
        and not standard_selected
        and matrices["t0"] == expected_zero_matrix
        and all(
            not row["selected"]
            and row["firing_exclusions"] == ("clean_postimage",)
            for row in identity_controls
        )
    )
    extended_pass = (
        target_side_by_side["t251"]["selected"] == ()
        and target_side_by_side["t252"]["selected"]
        == (TARGET_POSITIONS,)
        and extended_selected == [TARGET_KEY]
        and matrices["t251"] == expected_zero_matrix
        and matrices["t252"] == expected_extended_matrix
        and len(survivor_certificates) == 1
        and all(
            survivor_certificates[0]["conditions"].values()
        )
        and trajectories[TARGET_KEY]["first_clean_horizon"]
        == EXTENDED_HORIZON
    )
    subset_control_pass = (
        len(other_keys) == 175
        and not other_clean_at_252
        and first_clean_through_252
        == ((TARGET_KEY, EXTENDED_HORIZON),)
        and len(cycle_controls) == 11
        and all(
            trajectory["horizon_transport_failures"] == 0
            for trajectory in trajectories.values()
        )
    )
    deterministic_pass = (
        target_rerun == trajectories[TARGET_KEY]
        and horizon_census_sha256
        == EXPECTED_HORIZON_CENSUS_SHA256
        and digest(k2_positions) == digest(tuple(k2_positions))
    )

    return {
        "battery_pass": battery_pass,
        "extended_pass": extended_pass,
        "subset_control_pass": subset_control_pass,
        "deterministic_pass": deterministic_pass,
        "k2_configuration_count": len(k2_positions),
        "k2_family_count": len(families),
        "k2_family_representatives": tuple(families),
        "k2_family_sizes": {
            ",".join(map(str, representative)): len(alternatives)
            for representative, alternatives in families.items()
        },
        "k2_evaluations": len(rows),
        "standard_failure_census":
            dict(sorted(standard_failure_census.items())),
        "standard_selected": tuple(standard_selected),
        "identity_controls": identity_controls,
        "selected_count_matrices": matrices,
        "target_family_representative": target_representative,
        "target_family_alternatives": target_alternatives,
        "target_side_by_side": target_side_by_side,
        "extended_selected": tuple(extended_selected),
        "survivor_certificates": survivor_certificates,
        "other_k2_evaluations": len(other_keys),
        "other_clean_at_t252": other_clean_at_252,
        "first_clean_through_t252": first_clean_through_252,
        "cycle_controls_count": len(cycle_controls),
        "cycle_controls": cycle_controls,
        "cycle790_named_control_scope": {
            "other_open_keys": 163,
            "certified_cycles": 11,
            "named_control_keys": 174,
            "verification_scope": (
                "All 175 non-target k=2 evaluations were checked; this "
                "strictly covers the supplied 163+11 named controls.  The "
                "Cycle-790 open/cycle key classification is context and is "
                "not re-derived here."
            ),
        },
        "horizon_census_sha256": horizon_census_sha256,
        "target_trajectory_deterministic_rerun":
            target_rerun == trajectories[TARGET_KEY],
    }


def main() -> int:
    started = monotonic()
    anchor = header_and_reference_audit()
    experiment = run_experiment()
    elapsed = monotonic() - started

    outcome = (
        "SELECTED"
        if experiment["extended_selected"]
        else "STILL_EXCLUDED"
    )
    if outcome == "SELECTED":
        survivor_set = tuple(
            key[1] for key in experiment["extended_selected"]
        )
        uniqueness = (
            "UNIQUE" if len(survivor_set) == 1 else "TIE"
        )
        new_firing_exclusion = None
    else:
        survivor_set = ()
        uniqueness = "NONE"
        target_certificate = next(
            certificate
            for certificate in experiment["survivor_certificates"]
            if certificate["positions"] == TARGET_POSITIONS
        )
        new_firing_exclusion = tuple(
            name
            for name, passed in target_certificate["conditions"].items()
            if not passed
        )

    boundary = {
        "scope_statement": SUPPLIED_SCOPE_STATEMENT,
        "extension_definition": SUPPLIED_EXTENSION_DEFINITION,
        "actuality_claim": False,
        "actuality_statement": NO_ACTUALITY_STATEMENT,
        "probability_or_weights_used": False,
        "axiom_update_triggered": False,
        "horizon_extended_postimage_law_landed": False,
        "horizon_extended_postimage_law_status":
            "derivation target",
    }
    boundaries_pass = (
        not boundary["actuality_claim"]
        and not boundary["probability_or_weights_used"]
        and not boundary["axiom_update_triggered"]
        and not boundary["horizon_extended_postimage_law_landed"]
        and SUPPLIED_SCOPE_STATEMENT
        == (
            "the horizon extension is a SUPPLIED change to the acceptance "
            "law, not a landed law"
        )
    )
    projected_upper_bound = len(
        compact((anchor, experiment, boundary)).encode("utf-8")
    ) + 16 * 1024
    bounds_pass = (
        elapsed < AUDIT_TIMEOUT_SEC
        and projected_upper_bound < STDOUT_LIMIT_BYTES
    )

    certificate_rows = (
        (
            "Certificate_A_anchors_and_758_reference_provenance",
            anchor["pass"],
            anchor,
        ),
        (
            "Certificate_B_faithful_battery_and_landed_identity",
            experiment["battery_pass"],
            {
                "landed_postimage_horizon":
                    LANDED_POSTIMAGE_HORIZON,
                "battery_conditions": (
                    "synchronous_composition",
                    "token_rail_return",
                    "literal_inverse",
                    "census_membership",
                    "pairwise_separation",
                    "synchronization",
                    "clean_postimage",
                ),
                "standard_failure_census":
                    experiment["standard_failure_census"],
                "selected_count_matrix_t0":
                    experiment["selected_count_matrices"]["t0"],
                "identity_controls":
                    experiment["identity_controls"],
            },
        ),
        (
            "Certificate_C_extended_horizon_t251_vs_t252",
            experiment["extended_pass"],
            {
                "outcome": outcome,
                "survivor_set": survivor_set,
                "uniqueness_or_tie": uniqueness,
                "new_firing_exclusion": new_firing_exclusion,
                "target_side_by_side":
                    experiment["target_side_by_side"],
                "selected_count_matrix_t251":
                    experiment["selected_count_matrices"]["t251"],
                "selected_count_matrix_t252":
                    experiment["selected_count_matrices"]["t252"],
                "survivor_certificates":
                    experiment["survivor_certificates"],
            },
        ),
        (
            "Certificate_D_k2_subset_t252_unique_discontinuity",
            experiment["subset_control_pass"],
            {
                "k2_evaluations": experiment["k2_evaluations"],
                "other_k2_evaluations":
                    experiment["other_k2_evaluations"],
                "other_clean_at_t252":
                    experiment["other_clean_at_t252"],
                "first_clean_through_t252":
                    experiment["first_clean_through_t252"],
                "cycle_controls_count":
                    experiment["cycle_controls_count"],
                "cycle_controls": experiment["cycle_controls"],
                "cycle790_named_control_scope":
                    experiment["cycle790_named_control_scope"],
                "horizon_census_sha256":
                    experiment["horizon_census_sha256"],
            },
        ),
        (
            "Certificate_E_boundaries_determinism_and_bounds",
            (
                boundaries_pass
                and experiment["deterministic_pass"]
                and bounds_pass
            ),
            {
                "boundaries": boundary,
                "deterministic_target_rerun":
                    experiment[
                        "target_trajectory_deterministic_rerun"
                    ],
                "frozen_horizon_census_sha256":
                    EXPECTED_HORIZON_CENSUS_SHA256,
                "observed_horizon_census_sha256":
                    experiment["horizon_census_sha256"],
                "runtime_seconds": round(elapsed, 6),
                "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
                "projected_stdout_upper_bound_bytes":
                    projected_upper_bound,
                "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            },
        ),
    )
    checks = {
        label: bool(passed)
        for label, passed, _detail in certificate_rows
    }
    scientific_payload = {
        "anchor": anchor,
        "experiment": experiment,
        "outcome": outcome,
        "survivor_set": survivor_set,
        "uniqueness_or_tie": uniqueness,
        "boundary": boundary,
        "checks": checks,
    }
    report = {
        **scientific_payload,
        "scientific_report_sha256": digest(scientific_payload),
        "runtime_seconds": round(elapsed, 6),
        "pass": all(checks.values()),
        "terminal": (
            "CYCLE792_EXTENDED_HORIZON_SELECTOR_PASS"
            if all(checks.values())
            else "CYCLE792_EXTENDED_HORIZON_SELECTOR_FAIL"
        ),
    }

    lines = [
        "SUPPLIED_CHANGE_LOUD: " + SUPPLIED_SCOPE_STATEMENT,
        "SUPPLIED_CHANGE_DEFINITION: " + SUPPLIED_EXTENSION_DEFINITION,
        "landed_postimage_horizon: "
        + str(LANDED_POSTIMAGE_HORIZON),
        "extended_postimage_horizon: " + str(EXTENDED_HORIZON),
    ]
    lines.extend(
        (
            ("PASS " if passed else "FAIL ")
            + label
            + " :: "
            + compact(detail)
        )
        for label, passed, detail in certificate_rows
    )
    lines.extend(
        (
            "outcome: " + outcome,
            "survivor_set: " + compact(survivor_set),
            "uniqueness_or_tie: " + uniqueness,
            "horizon_discontinuity_t251_vs_t252: "
            + compact(experiment["target_side_by_side"]),
            "first_multisource_selection_at_extended_horizon: "
            + ("true" if outcome == "SELECTED" else "false"),
            "actuality_claim: false",
            "probability_or_weights_used: false",
            "axiom_update_triggered: false",
            NO_ACTUALITY_STATEMENT,
            compact(report),
        )
    )
    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
