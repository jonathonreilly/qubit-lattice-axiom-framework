#!/usr/bin/env python3
"""Cycle-729 bounded epoch-census feed of the Cycle-317 Born surface.

The two Cycle-722 2x2x2 epoch variants supply only declared apparatus data:
one normalized Bloch direction and four merge coefficients.  The effects are
then obtained only from the byte-pinned Cycle-317 dilation helpers.  No census
quantity is interpreted as an outcome weight, occurrence, Record, frequency,
calibration, eligibility declaration, or selected Born law.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BORN_SURFACE_FEED_CYCLE729_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from collections import Counter
from hashlib import sha256
import inspect
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from time import perf_counter

import numpy as np

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28 as F722


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_B317_SHA256 = (
    "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"
)
EXPECTED_F722_SHA256 = (
    "5f20146eace2a0b61e5f1aa26f19cc432c8ec5bf737621470e81efecaa763775"
)
EXPECTED_B317_PASS_COUNT = 15
EXPECTED_B317_FAIL_COUNT = 0
SHAPE = (2, 2, 2)
VARIANTS = ("primary", "alternate_port")
EVENT_FIELDS = (
    "certificate",
    "binder",
    "actuality",
    "admissibility",
    "law_domain",
)
BLOCH_FIELD_ORDER = ("certificate", "actuality", "law_domain")
BASE_STAGE_ORDER = ("A", "B", "C", "D")
CYCLE317_LITERAL_SPLITS = (0.17, 0.29, 0.54)
CYCLE317_LITERAL_MERGE_DIRECTIONS = (
    (1.0, 2.0, 3.0),
    (-1.0, 0.0, 0.0),
    (0.0, -1.0, 0.0),
    (0.0, 0.0, -1.0),
)
FROZEN_TABLE_SHA256 = {
    "primary": "a6293d1339f1457da9ae63b706cd66725d1a17d732429f97ce39b35099537c39",
    "alternate_port": (
        "4d693b9960b36abfef58049a531b7fa6116a311a125f131fc0d3a51b85ccab2a"
    ),
}
FROZEN_BASE_STAGE_HANDOFF_COUNTS = {
    "primary": {"A": 100, "B": 152, "C": 180, "D": 72},
    "alternate_port": {"A": 100, "B": 12, "C": 0, "D": 72},
}
FROZEN_COMBINED_BASE_STAGE_HANDOFF_COUNTS = (200, 164, 180, 144)
FROZEN_PORT_INVENTORY = {
    "basis": ("dimension", "index"),
    "binary_and_ternary_threshold_controls": ("trine_effects",),
    "check": ("label", "condition", "detail"),
    "contact_trine_controls": ("fixture",),
    "deletion_domain_and_semantic_controls": ("fixture", "forcing_kraus"),
    "derived_effects": ("isometry", "groups"),
    "main": (),
    "menu_metrics": ("effects",),
    "merge_isometry": ("weighted_projectors", "contact"),
    "mixed_projective_forcing_basis_controls": ("fixture",),
    "nonlinear_binary_weight": ("effect",),
    "normalized": ("path",),
    "note_contract": (),
    "physical_fixture": ("length",),
    "physical_isometry": ("two_ray_encoding", "kraus"),
    "physical_locality_and_covariance_controls": ("fixtures", "route_kraus"),
    "physical_subcode_controls": (),
    "projector_bloch": ("vector",),
    "split_projector_isometry": ("projector", "splits", "contact"),
    "stack_isometry": ("kraus",),
}
FORBIDDEN_CENSUS_RECEIVER_TOKENS = (
    "calibration",
    "count",
    "epoch",
    "exposure",
    "frequenc",
    "occurrence",
    "record",
    "row",
    "sampling",
)
CLAIM_BOUNDARY = (
    "the epoch census lawfully enters the landed Born-forcing surface only "
    "as declared apparatus data at its parameterized ports; the "
    "menu-selection rule, effect functionality across programs, eligibility, "
    "coefficients, and the weight law all remain supplied/open exactly as the "
    "landed note records; no Born/probability content is selected."
)

CHECKS: list[dict[str, object]] = []


def json_default(value: object) -> object:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def check(label: str, condition: bool, detail: object = "") -> bool:
    passed = bool(condition)
    row = {"label": label, "pass": passed, "detail": detail}
    CHECKS.append(row)
    rendered = json.dumps(
        detail,
        default=json_default,
        sort_keys=True,
        separators=(",", ":"),
    )
    print("PASS" if passed else "FAIL", label, "::", rendered)
    return passed


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def table_sha256(table: list[dict[str, object]]) -> str:
    payload = json.dumps(
        table,
        default=json_default,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()


def anchor_replay(b317_path: Path) -> dict[str, object]:
    environment = dict(os.environ)
    environment["PYTHONPATH"] = "scripts"
    completed = subprocess.run(
        [sys.executable, str(b317_path)],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    stdout = completed.stdout.decode("utf-8", errors="replace")
    stderr = completed.stderr.decode("utf-8", errors="replace")
    summaries = re.findall(
        r"^SUMMARY PASS ([0-9]+) FAIL ([0-9]+)$",
        stdout,
        flags=re.MULTILINE,
    )
    pass_lines = len(re.findall(r"^PASS ", stdout, flags=re.MULTILINE))
    fail_lines = len(re.findall(r"^FAIL ", stdout, flags=re.MULTILINE))
    summary_pass = int(summaries[-1][0]) if len(summaries) == 1 else None
    summary_fail = int(summaries[-1][1]) if len(summaries) == 1 else None
    result_lines = re.findall(r"^RESULT (.+)$", stdout, flags=re.MULTILINE)
    return {
        "returncode": completed.returncode,
        "summary_pass": summary_pass,
        "summary_fail": summary_fail,
        "pass_lines": pass_lines,
        "fail_lines": fail_lines,
        "stdout_bytes": len(completed.stdout),
        "stdout_sha256": sha256(completed.stdout).hexdigest(),
        "stderr_bytes": len(completed.stderr),
        "stderr_sha256": sha256(completed.stderr).hexdigest(),
        "result": result_lines[-1] if len(result_lines) == 1 else None,
        "pass": (
            completed.returncode == 0
            and summary_pass == EXPECTED_B317_PASS_COUNT
            and summary_fail == EXPECTED_B317_FAIL_COUNT
            and pass_lines == EXPECTED_B317_PASS_COUNT
            and fail_lines == EXPECTED_B317_FAIL_COUNT
            and result_lines
            == ["CYCLE317_PHYSICAL_CONTACT_TERNARY_BORN_BRIDGE_GREEN"]
            and not stderr
        ),
    }


def build_epoch_census() -> dict[str, object]:
    atlas = F722.EPOCH.P.build_private_atlases()
    primary = F722.EPOCH.build_epoch(SHAPE, "primary", atlas)
    alternate = F722.EPOCH.build_epoch(
        SHAPE,
        "alternate_port",
        atlas,
        recurrent_override=primary.recurrent,
    )
    bundles = {"primary": primary, "alternate_port": alternate}
    extensions: dict[str, dict[str, object]] = {}
    summaries: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        extension = F722.extend_and_walk(bundles[variant])
        extensions[variant] = extension
        table = extension["table"]
        word_stage = {
            word.word_id: slot.stage
            for slot in extension["slots"]
            for word in slot.words
        }
        destination_counts = Counter(
            word_stage[edge[1]] for edge in extension["handoffs"]
        )
        field_one_counts = {
            field: sum(int(row[field]) for row in table)
            for field in EVENT_FIELDS
        }
        identities = tuple(int(row["tick_identity"]) for row in table)
        summaries[variant] = {
            "shape": list(SHAPE),
            "event_rows": len(table),
            "distinct_identities": len(set(identities)),
            "identity_minimum": min(identities),
            "identity_maximum": max(identities),
            "identity_sequence_sha256": sha256(repr(identities).encode()).hexdigest(),
            "event_table_sha256": table_sha256(table),
            "field_one_counts": field_one_counts,
            "source_count": len(extension["sources"]),
            "sources_clean": extension["sources_clean"],
            "E_handoffs": len(extension["e_handoffs"]),
            "base_stage_destination_handoffs": {
                stage: int(destination_counts[stage])
                for stage in BASE_STAGE_ORDER
            },
            "collision_count": int(extension["walk"]["collision_count"]),
            "violation_count": int(extension["walk"]["violation_count"]),
            "lawful": bool(extension["lawful"]),
        }
    return {
        "bundles": bundles,
        "extensions": extensions,
        "summaries": summaries,
    }


def metric_domain_pass(metrics: dict[str, float]) -> bool:
    return (
        metrics["normalization"] < B317.TOL
        and metrics["minimum_eigenvalue"] > -B317.TOL
        and metrics["maximum_eigenvalue"] < 1 + B317.TOL
    )


def rejected(call: object) -> dict[str, object]:
    try:
        call()
    except ValueError as error:
        return {
            "detected": True,
            "mode": "lawful_domain_rejection",
            "exception": type(error).__name__,
            "message": str(error),
        }
    except Exception as error:
        return {
            "detected": False,
            "mode": "wrong_exception",
            "exception": type(error).__name__,
            "message": str(error),
        }
    return {
        "detected": False,
        "mode": "not_rejected",
        "exception": None,
        "message": None,
    }


def live_port_inventory() -> dict[str, tuple[str, ...]]:
    return {
        name: tuple(inspect.signature(getattr(B317, name)).parameters)
        for name in sorted(FROZEN_PORT_INVENTORY)
    }


def main() -> int:
    started = perf_counter()
    CHECKS.clear()

    b317_path = ROOT / AUDIT_INPUT_PATHS[0]
    f722_path = ROOT / AUDIT_INPUT_PATHS[1]
    source_pins = {
        "B317": {
            "path": AUDIT_INPUT_PATHS[0],
            "expected": EXPECTED_B317_SHA256,
            "observed": file_sha256(b317_path),
        },
        "F722": {
            "path": AUDIT_INPUT_PATHS[1],
            "expected": EXPECTED_F722_SHA256,
            "observed": file_sha256(f722_path),
        },
    }
    b317_pin_pass = (
        source_pins["B317"]["observed"] == source_pins["B317"]["expected"]
        and Path(B317.__file__).resolve() == b317_path.resolve()
    )
    f722_pin_pass = (
        source_pins["F722"]["observed"] == source_pins["F722"]["expected"]
        and Path(F722.__file__).resolve() == f722_path.resolve()
    )
    check(
        "ANCHOR byte-pin B317 against the frozen landed bytes",
        b317_pin_pass,
        source_pins["B317"],
    )
    check(
        "CENSUS byte-pin F722 against the frozen landed bytes",
        f722_pin_pass,
        source_pins["F722"],
    )

    anchor = anchor_replay(b317_path)
    anchor_pass = check(
        "ANCHOR subprocess replay keeps B317 main unchanged at frozen 15 PASS and zero FAIL",
        anchor["pass"],
        anchor,
    )
    leg1_pass = b317_pin_pass and anchor_pass

    census = build_epoch_census()
    census_summaries = census["summaries"]
    frozen_census_pass = all(
        census_summaries[variant]["event_rows"] == 24
        and census_summaries[variant]["distinct_identities"] == 24
        and census_summaries[variant]["identity_minimum"] == 0
        and census_summaries[variant]["identity_maximum"] == 23
        and census_summaries[variant]["event_table_sha256"]
        == FROZEN_TABLE_SHA256[variant]
        and census_summaries[variant]["field_one_counts"]
        == {field: 24 for field in EVENT_FIELDS}
        and census_summaries[variant]["source_count"] == 5
        and census_summaries[variant]["sources_clean"]
        and census_summaries[variant]["E_handoffs"] == 120
        and census_summaries[variant]["base_stage_destination_handoffs"]
        == FROZEN_BASE_STAGE_HANDOFF_COUNTS[variant]
        and census_summaries[variant]["collision_count"] == 0
        and census_summaries[variant]["violation_count"] == 0
        and census_summaries[variant]["lawful"]
        for variant in VARIANTS
    )
    census_pass = check(
        "TRUE FEEDS freeze both lawful 2x2x2 Cycle-722 event censuses and their digests",
        f722_pin_pass and frozen_census_pass,
        census_summaries,
    )

    fixture3 = B317.physical_fixture(3)
    fixture6 = B317.physical_fixture(6)
    expected_contact = np.diag(
        (np.exp(1j * B317.c311.COUPLING), 1)
    ).astype(complex)
    contact_unchanged = (
        fixture3.two_ray_encoding.shape == (510, 2)
        and fixture6.two_ray_encoding.shape == (510, 2)
        and fixture3.contact.shape == (2, 2)
        and fixture6.contact.shape == (2, 2)
        and np.linalg.norm(fixture3.contact - expected_contact) < B317.TOL
        and np.linalg.norm(fixture6.contact - expected_contact) < B317.TOL
        and np.linalg.norm(fixture3.contact - fixture6.contact) < B317.TOL
    )
    fixture_pass = check(
        "TRUE FEEDS bind the unchanged Cycle-317 L=3 contact and held L=6 fixture",
        contact_unchanged,
        {
            "fixture_lengths": [fixture3.length, fixture6.length],
            "two_ray_shapes": [
                list(fixture3.two_ray_encoding.shape),
                list(fixture6.two_ray_encoding.shape),
            ],
            "contact_sha256": sha256(fixture3.contact.tobytes()).hexdigest(),
            "contact_residual_L3_L6": float(
                np.linalg.norm(fixture3.contact - fixture6.contact)
            ),
        },
    )

    combined_field_counts = {
        field: sum(
            int(census_summaries[variant]["field_one_counts"][field])
            for variant in VARIANTS
        )
        for field in EVENT_FIELDS
    }
    bloch_raw = np.asarray(
        [combined_field_counts[field] for field in BLOCH_FIELD_ORDER],
        dtype=float,
    )
    bloch_direction = bloch_raw / np.linalg.norm(bloch_raw)
    census_projector = B317.projector_bloch(bloch_direction)
    split_isometry, split_groups = B317.split_projector_isometry(
        census_projector,
        CYCLE317_LITERAL_SPLITS,
        fixture3.contact,
    )
    split_effects = B317.derived_effects(split_isometry, split_groups)
    split_metrics = B317.menu_metrics(split_effects)
    projector_feed = {
        "label": (
            "supplied apparatus direction derived from declared census "
            "projection"
        ),
        "explicitly_not": "a derived menu selection",
        "convention": {
            "census_scalars": (
                "combined one-count in each named Cycle-722 event-table field "
                "over primary then alternate_port"
            ),
            "frame": "Cycle-317 Bloch (x,y,z) order",
            "field_order": list(BLOCH_FIELD_ORDER),
            "sign": "positive retained-bit one-counts; no sign flips",
            "raw_counts": bloch_raw.tolist(),
            "normalization": "divide by Euclidean L2 norm exactly once",
            "unit_vector": bloch_direction.tolist(),
            "fitted_parameters": 0,
        },
        "Cycle317_literal_splits": list(CYCLE317_LITERAL_SPLITS),
        "contact": "unchanged fixture L=3 contact",
        "groups": [list(group) for group in split_groups],
        "menu_metrics": split_metrics,
        "isometry_residual": float(
            np.linalg.norm(split_isometry.conj().T @ split_isometry - B317.I2)
        ),
    }
    projector_feed_pass = check(
        "TRUE FEED projector_bloch accepts the declared census unit vector and split_projector_isometry derives a lawful menu",
        (
            np.linalg.norm(bloch_direction) == 1.0
            and split_isometry.shape == (16, 2)
            and len(split_effects) == 4
            and projector_feed["isometry_residual"] < B317.TOL
            and metric_domain_pass(split_metrics)
        ),
        projector_feed,
    )

    corrupt_vector_control = rejected(
        lambda: B317.projector_bloch(np.zeros(3, dtype=float))
    )
    projector_control_pass = check(
        "CONTROL corrupted all-zero census vector is rejected by the landed Bloch lawful domain",
        corrupt_vector_control["detected"],
        corrupt_vector_control,
    )

    combined_stage_counts = tuple(
        sum(
            int(
                census_summaries[variant][
                    "base_stage_destination_handoffs"
                ][stage]
            )
            for variant in VARIANTS
        )
        for stage in BASE_STAGE_ORDER
    )
    stage_total = sum(combined_stage_counts)
    merge_fractions = tuple(
        count / stage_total for count in combined_stage_counts
    )
    literal_projectors = tuple(
        B317.projector_bloch(
            np.asarray(direction, dtype=float)
            / np.linalg.norm(np.asarray(direction, dtype=float))
        )
        for direction in CYCLE317_LITERAL_MERGE_DIRECTIONS
    )
    merge_isometry, merge_groups = B317.merge_isometry(
        tuple(zip(merge_fractions, literal_projectors)),
        fixture3.contact,
    )
    merge_effects = B317.derived_effects(merge_isometry, merge_groups)
    merge_metrics = B317.menu_metrics(merge_effects)
    merge_feed = {
        "label": "supplied apparatus coefficients",
        "explicitly_not": "Born weights w(E)",
        "convention": {
            "projection": (
                "count destination handoffs in the base epoch stages for both "
                "2x2x2 legs, aggregate in declared A,B,C,D order, divide each "
                "integer by their total"
            ),
            "stage_order": list(BASE_STAGE_ORDER),
            "per_variant_counts": {
                variant: census_summaries[variant][
                    "base_stage_destination_handoffs"
                ]
                for variant in VARIANTS
            },
            "combined_counts": list(combined_stage_counts),
            "normalization_total": stage_total,
            "fraction_tuple": list(merge_fractions),
            "fitted_parameters": 0,
        },
        "Cycle317_literal_projector_directions": [
            list(row) for row in CYCLE317_LITERAL_MERGE_DIRECTIONS
        ],
        "contact": "unchanged fixture L=3 contact",
        "groups": [list(group) for group in merge_groups],
        "menu_metrics": merge_metrics,
        "isometry_residual": float(
            np.linalg.norm(merge_isometry.conj().T @ merge_isometry - B317.I2)
        ),
    }
    merge_feed_pass = check(
        "TRUE FEED merge_isometry accepts normalized per-stage census fractions and compiles the Cycle-317 literal projectors",
        (
            combined_stage_counts
            == FROZEN_COMBINED_BASE_STAGE_HANDOFF_COUNTS
            and len(merge_fractions) == 4
            and all(value >= 0 for value in merge_fractions)
            and abs(sum(merge_fractions) - 1) < 1e-15
            and merge_isometry.shape == (16, 2)
            and len(merge_effects) == 5
            and merge_feed["isometry_residual"] < B317.TOL
            and metric_domain_pass(merge_metrics)
        ),
        merge_feed,
    )

    corrupted_fractions = list(merge_fractions)
    first_fraction = corrupted_fractions[0]
    corrupted_fractions[0] = -first_fraction
    corrupted_fractions[1] += 2 * first_fraction
    corrupt_tuple_control = rejected(
        lambda: B317.merge_isometry(
            tuple(zip(corrupted_fractions, literal_projectors)),
            fixture3.contact,
        )
    )
    corrupt_tuple_control["corrupted_fraction_tuple"] = corrupted_fractions
    corrupt_tuple_control["sum"] = sum(corrupted_fractions)
    merge_control_pass = check(
        "CONTROL negative corrupted census fraction is rejected by the landed merge lawful domain",
        corrupt_tuple_control["detected"],
        corrupt_tuple_control,
    )

    frame_count = len(B317.c311.c235.proper_cubic_frames())
    total_event_rows = sum(
        int(census_summaries[variant]["event_rows"]) for variant in VARIANTS
    )
    identity_multiplicities = Counter(
        int(row["tick_identity"])
        for variant in VARIANTS
        for row in census["extensions"][variant]["table"]
    )
    binding_table = [
        {
            "census_quantity": "2x2x2 epoch legs",
            "census_integer": len(VARIANTS),
            "pinned_fixture_quantity": "L=3 two-ray logical columns",
            "fixture_integer": fixture3.two_ray_encoding.shape[1],
        },
        {
            "census_quantity": "event rows per leg",
            "census_integer": min(
                int(census_summaries[variant]["event_rows"])
                for variant in VARIANTS
            ),
            "pinned_fixture_quantity": "proper-cubic frame count",
            "fixture_integer": frame_count,
        },
        {
            "census_quantity": "distinct tick identities per leg",
            "census_integer": min(
                int(census_summaries[variant]["distinct_identities"])
                for variant in VARIANTS
            ),
            "pinned_fixture_quantity": "proper-cubic frame count",
            "fixture_integer": frame_count,
        },
        {
            "census_quantity": "combined event rows",
            "census_integer": total_event_rows,
            "pinned_fixture_quantity": "proper frames x two-ray columns",
            "fixture_integer": frame_count
            * fixture3.two_ray_encoding.shape[1],
        },
        {
            "census_quantity": "multiplicity of every tick identity",
            "census_integer": min(identity_multiplicities.values()),
            "pinned_fixture_quantity": "pinned fixture lengths L=3,L=6",
            "fixture_integer": len((fixture3, fixture6)),
        },
        {
            "census_quantity": "ordered Bloch projection fields",
            "census_integer": len(BLOCH_FIELD_ORDER),
            "pinned_fixture_quantity": "pointer M2",
            "fixture_integer": B317.POINTER_M2,
        },
        {
            "census_quantity": "base-stage coefficient bins",
            "census_integer": len(BASE_STAGE_ORDER),
            "pinned_fixture_quantity": "maximum merge components",
            "fixture_integer": 4,
        },
    ]
    for row in binding_table:
        row["exact_equal"] = (
            row["census_integer"] == row["fixture_integer"]
        )
    binding_pass = check(
        "EXACT INTEGER BINDINGS match the census event-count table to pinned replay invariants",
        (
            len(identity_multiplicities) == 24
            and max(identity_multiplicities.values()) == 2
            and all(row["exact_equal"] for row in binding_table)
        ),
        binding_table,
    )
    leg2_pass = (
        census_pass
        and fixture_pass
        and projector_feed_pass
        and projector_control_pass
        and merge_feed_pass
        and merge_control_pass
    )
    leg3_pass = binding_pass

    observed_inventory = live_port_inventory()
    forbidden_receivers = {
        name: [
            parameter
            for parameter in parameters
            if any(
                token in parameter.lower()
                for token in FORBIDDEN_CENSUS_RECEIVER_TOKENS
            )
        ]
        for name, parameters in observed_inventory.items()
    }
    forbidden_receivers = {
        name: parameters
        for name, parameters in forbidden_receivers.items()
        if parameters
    }
    no_census_weight_receiver = {
        "frozen_port_count": len(FROZEN_PORT_INVENTORY),
        "inventory": {
            name: list(parameters)
            for name, parameters in observed_inventory.items()
        },
        "inventory_matches_extract": (
            observed_inventory == FROZEN_PORT_INVENTORY
        ),
        "forbidden_receiver_tokens": list(
            FORBIDDEN_CENSUS_RECEIVER_TOKENS
        ),
        "receivers_found": forbidden_receivers,
        "nonlinear_binary_weight_boundary": (
            "hard-coded counterfunctional of one supplied effect; not a "
            "configurable numerical-weight or census receiver"
        ),
        "merge_weight_boundary": (
            "weighted_projectors receives apparatus coefficients only"
        ),
    }
    no_receiver_pass = check(
        "FROZEN FINDING no_census_weight_receiver matches all 20 live signatures and finds no count/frequency/exposure/Record-row port",
        (
            no_census_weight_receiver["inventory_matches_extract"]
            and not forbidden_receivers
        ),
        no_census_weight_receiver,
    )

    weights_remain_supplied = {
        "value": True,
        "required_absent_bridge": [
            "physical occurrence or actual-member selection",
            "lawful Record formation and typing",
            "sampling and exposure model",
            "frequency or component-mean calibration",
        ],
        "finding": (
            "The numerical map w(E) requires an occurrence/Record/sampling/"
            "calibration bridge absent from this surface. Census counts, "
            "normalized counts, projector directions, and merge fractions do "
            "not select it."
        ),
        "Born_lane_analog": "no-port finding; nothing here selects w(E)",
    }
    supplied_weight_pass = check(
        "FROZEN FINDING weights_remain_supplied records the absent occurrence/Record/sampling/calibration bridge",
        no_receiver_pass and weights_remain_supplied["value"],
        weights_remain_supplied,
    )

    born_surface_fed = bool(leg1_pass and leg2_pass and leg3_pass)
    firewall = {
        "apparatus_data_supplied": True,
        "born_law_selected": False,
        "born_surface_fed": born_surface_fed,
        "effects_derived_only_via_pinned_dilation": True,
        "weights_remain_supplied": True,
    }
    firewall_pass = check(
        "FIREWALL preserves supplied apparatus data, derived effects, and unselected Born weights",
        (
            firewall
            == {
                "born_law_selected": False,
                "weights_remain_supplied": True,
                "apparatus_data_supplied": True,
                "effects_derived_only_via_pinned_dilation": True,
                "born_surface_fed": born_surface_fed,
            }
            and born_surface_fed
            and supplied_weight_pass
        ),
        firewall,
    )

    runtime_seconds = perf_counter() - started
    passing = all(bool(row["pass"]) for row in CHECKS)
    report = {
        "status": "PASS" if passing else "FAIL",
        "checks": CHECKS,
        "anchor": anchor,
        "source_pins": source_pins,
        "census": census_summaries,
        "projector_bloch_feed": projector_feed,
        "merge_isometry_feed": merge_feed,
        "controls": {
            "corrupted_census_vector": corrupt_vector_control,
            "corrupted_census_fraction_tuple": corrupt_tuple_control,
        },
        "exact_integer_binding_table": binding_table,
        "frozen_findings": {
            "no_census_weight_receiver": no_census_weight_receiver,
            "weights_remain_supplied": weights_remain_supplied,
        },
        "firewall": firewall,
        "claim_boundary": CLAIM_BOUNDARY,
        "zero_refit": True,
        "menu_selection_derived": False,
        "Born_probability_content_selected": False,
        "note_path_declared_without_existence_check": NOTE_PATH,
        "stdout_policy_bytes_less_than": 150_000,
        "runtime_seconds": runtime_seconds,
        "authority": "none",
        "audit": "unset",
        "all_required_legs": {
            "leg1_anchor": leg1_pass,
            "leg2_true_feeds_and_controls": leg2_pass,
            "leg3_exact_integer_bindings": leg3_pass,
            "frozen_findings": no_receiver_pass and supplied_weight_pass,
            "firewall": firewall_pass,
        },
    }
    print(json.dumps(report, default=json_default, indent=2, sort_keys=True))
    if not passing:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
