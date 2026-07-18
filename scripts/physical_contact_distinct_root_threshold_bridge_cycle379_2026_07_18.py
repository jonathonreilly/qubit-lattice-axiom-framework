#!/usr/bin/env python3
"""Cycle 379: Cycle-281 contact confirmations -> Cycle-366 threshold bridge.

Three carrier copies do not establish three independent confirmations.  This
runner adds an explicit bounded radius-16 reference predicate over three
supplied one-hot provenance-root markers.  One positive Cycle-281 close fanned into
three spatial carriers retains one root marker and is rejected.  Three
distinct declared roots, each with an exact deletion-faithful positive-contact
close and the same lawful 30-M2 payload, may enter Cycle 366's otherwise
root-blind threshold calculation and isolated CONSUME candidate.

The root markers and their physical independence are supplied.  Their genesis,
autonomous enforcement, and the Cycle-281-close-to-Cycle-366-interface map are
not compiled here.  Cycle 366, threshold three, and CONSUME remain unselected;
CONSUME admission is absent.  Q=0 and coherent Q0+Q1 inputs do not supply a
deterministic positive confirmation, and no branch or Record is selected.
There is no no-go, minimum-content result, shared obstruction, or axiom
pressure.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from io import StringIO
from contextlib import redirect_stdout
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTACT_DISTINCT_ROOT_THRESHOLD_BRIDGE_"
    "CYCLE379_NOTE_2026-07-18.md"
)

import matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17 as c281
import physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18 as c366


Coord = c366.Coord
Word = c366.Word
LENGTHS = (3, 6)
ROOT_LABEL_WIDTH = 3
ROOTS_REQUIRED = c366.FORMATION_THRESHOLD
ROOT_MARKER_M2 = ROOTS_REQUIRED * ROOT_LABEL_WIDTH
ROOT_CONSTRAINT_MAX_L1 = 16
CONFIRMATION_SOURCE = "Cycle-379 supplied Cycle-281 positive-contact confirmation/root binding"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-11
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-379 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-281 positive-contact close",
        "three spatial copies of one close are not three independent confirmations",
        "nine-m2 marker inventory with a bounded radius-16 reference constraint",
        "root-marker genesis: supplied",
        "physical independence: supplied",
        "deleting either u_i",
        "q=0 separator",
        "coherent q0+q1 separator",
        "no actual branch is selected",
        "all 24 proper-cubic frames",
        "l=3 and l=6",
        "threshold three remains unselected",
        "consume admission by existing framework law: none",
        "shared substrate obstruction: none established",
        "no no-go, minimum-content theorem, or axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the contact/root/threshold bridge, independence boundary, separators, and residuals",
        not missing,
        missing,
    )
    return {"missing": missing}


@dataclass(frozen=True)
class MatterInput:
    label: str
    amplitudes: tuple[tuple[int, complex], ...]


@dataclass(frozen=True)
class ProvenanceRoot:
    root_site: Coord
    marker: tuple[int, ...]
    marker_anchor: Coord
    source: str = CONFIRMATION_SOURCE


@dataclass(frozen=True)
class ContactConfirmation:
    carrier_site: Coord
    root: ProvenanceRoot
    payload: Word
    matter: MatterInput
    first_U_I: str = "ideal"
    second_U_I: str = "ideal"
    archive_writer: bool = True
    close_writer: bool = True
    history_writer: bool = True
    source: str = CONFIRMATION_SOURCE


@dataclass(frozen=True)
class CloseDiagnostic:
    close_weight: float
    history_weight: float
    pointer_one_weight: float
    archive_weight: float
    normalized: bool
    deterministic_positive: bool
    actual_branch_selector: None = None


@dataclass(frozen=True)
class BridgeAnswer:
    status: str
    conditions: tuple[tuple[str, bool], ...]
    diagnostics: tuple[CloseDiagnostic, ...]
    prepared: c366.BasisState
    calculated: c366.BasisState
    committed: c366.BasisState
    records: tuple[c366.ThresholdSiteContentRecord, ...]


def q0_input() -> MatterInput:
    return MatterInput("Q=0 basis", ((0, 1.0 + 0.0j),))


def q1_input() -> MatterInput:
    return MatterInput("Q=1 basis", ((3, 1.0 + 0.0j),))


def coherent_input() -> MatterInput:
    amplitude = complex(1 / np.sqrt(2))
    return MatterInput("coherent Q0+Q1", ((0, amplitude), (3, amplitude)))


def matter_vector(item: MatterInput) -> np.ndarray:
    if not isinstance(item, MatterInput) or not item.amplitudes:
        raise TypeError("confirmation needs one explicit MatterInput")
    vector = np.zeros(c281.MATTER_DIMENSION, dtype=complex)
    seen = set()
    for occupation, amplitude in item.amplitudes:
        if (
            not isinstance(occupation, int)
            or isinstance(occupation, bool)
            or not 0 <= occupation < c281.MATTER_DIMENSION
            or occupation in seen
            or not np.isfinite(amplitude.real)
            or not np.isfinite(amplitude.imag)
        ):
            raise ValueError("matter input is outside the 64-dimensional supplied domain")
        vector[occupation] = amplitude
        seen.add(occupation)
    if abs(np.vdot(vector, vector).real - 1.0) > TOL:
        raise ValueError("matter input must be normalized")
    return vector


def validate_root(root: ProvenanceRoot) -> None:
    if not isinstance(root, ProvenanceRoot):
        raise TypeError("confirmation requires one ProvenanceRoot")
    if (
        not c366.c364.valid_coord(root.root_site)
        or not c366.c364.valid_coord(root.marker_anchor)
        or not isinstance(root.marker, tuple)
        or len(root.marker) != ROOT_LABEL_WIDTH
        or any(bit not in (0, 1) for bit in root.marker)
        or sum(root.marker) != 1
        or root.source != CONFIRMATION_SOURCE
    ):
        raise ValueError("provenance root is outside the supplied one-hot marker domain")


def validate_confirmation(item: ContactConfirmation) -> None:
    if not isinstance(item, ContactConfirmation):
        raise TypeError("bridge requires ContactConfirmation values")
    validate_root(item.root)
    matter_vector(item.matter)
    if (
        not c366.c364.valid_coord(item.carrier_site)
        or not isinstance(item.payload, tuple)
        or len(item.payload) != c366.c364.RECORD_BITS
        or any(bit not in (0, 1) for bit in item.payload)
        or item.first_U_I not in ("ideal", "deleted", "pointer_only")
        or item.second_U_I not in ("ideal", "deleted", "pointer_only")
        or not all(
            isinstance(value, bool)
            for value in (item.archive_writer, item.close_writer, item.history_writer)
        )
        or item.source != CONFIRMATION_SOURCE
    ):
        raise ValueError("contact confirmation is outside its exact finite domain")


def bit_weight(state: np.ndarray, bit: int, value: int = 1) -> float:
    matrix = state.reshape(c281.MATTER_DIMENSION, c281.ANCILLA_DIMENSION)
    indices = tuple(
        index
        for index in range(c281.ANCILLA_DIMENSION)
        if ((index >> bit) & 1) == value
    )
    return float(np.sum(np.abs(matrix[:, indices]) ** 2).real)


def close_diagnostic(item: ContactConfirmation) -> CloseDiagnostic:
    validate_confirmation(item)
    vector = matter_vector(item.matter)
    blank = c281.basis(c281.ANCILLA_DIMENSION, 0)
    gates = c281.candidate_gates(
        first=item.first_U_I,
        second=item.second_U_I,
        archive=item.archive_writer,
        close=item.close_writer,
        history=item.history_writer,
    )
    output = c281.apply_gates(np.kron(vector, blank), gates)
    norm = float(np.vdot(output, output).real)
    close_weight = bit_weight(output, c281.CLOSE)
    history_weight = bit_weight(output, c281.HISTORY)
    pointer_weight = bit_weight(output, c281.POINTER)
    archive_weight = bit_weight(output, c281.ARCHIVE)
    deterministic = (
        abs(norm - 1.0) < TOL
        and abs(close_weight - 1.0) < TOL
        and abs(history_weight - 1.0) < TOL
        and pointer_weight < TOL
        and abs(archive_weight - 1.0) < TOL
    )
    return CloseDiagnostic(
        close_weight,
        history_weight,
        pointer_weight,
        archive_weight,
        abs(norm - 1.0) < TOL,
        deterministic,
    )


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def distinct_root_conditions(
    target: Coord,
    confirmations: tuple[ContactConfirmation, ...],
) -> tuple[tuple[str, bool], ...]:
    roots = tuple(item.root for item in confirmations)
    return (
        ("exactly_three_confirmations", len(confirmations) == ROOTS_REQUIRED),
        ("one_hot_root_markers", all(sum(root.marker) == 1 for root in roots)),
        ("distinct_root_markers", len({root.marker for root in roots}) == ROOTS_REQUIRED),
        ("distinct_root_sites", len({root.root_site for root in roots}) == ROOTS_REQUIRED),
        ("distinct_carrier_sites", len({item.carrier_site for item in confirmations}) == ROOTS_REQUIRED),
        (
            "bounded_local_root_sidecar",
            all(
                l1(target, site) <= ROOT_CONSTRAINT_MAX_L1
                for item in confirmations
                for site in (item.carrier_site, item.root.root_site, item.root.marker_anchor)
            ),
        ),
        (
            "root_marker_carrier_binding",
            all(l1(item.root.marker_anchor, item.carrier_site) == 1 for item in confirmations),
        ),
    )


def confirmation_set(
    target: Coord,
    payload: Word,
    matter: MatterInput | None = None,
) -> tuple[ContactConfirmation, ...]:
    matter = q1_input() if matter is None else matter
    offsets = ((0, 0, 5), (0, 0, 9), (0, 0, 13))
    marker_offsets = ((0, 0, 4), (0, 0, 8), (0, 0, 12))
    root_offsets = ((1, 0, 4), (0, 1, 8), (-1, 0, 12))
    labels = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    add = lambda left, right: tuple(a + b for a, b in zip(left, right))
    return tuple(
        ContactConfirmation(
            add(target, carrier_offset),
            ProvenanceRoot(
                add(target, root_offset),
                label,
                add(target, marker_offset),
            ),
            payload,
            matter,
        )
        for carrier_offset, marker_offset, root_offset, label in zip(
            offsets, marker_offsets, root_offsets, labels
        )
    )


def copied_confirmation_set(
    target: Coord,
    payload: Word,
) -> tuple[ContactConfirmation, ...]:
    distinct = confirmation_set(target, payload)
    source_root = distinct[0].root
    return tuple(replace(item, root=source_root) for item in distinct)


def bridge_to_threshold(
    fixture: c366.c364.c342.c338.RouteFixture,
    layout: c366.Layout,
    payload: Word,
    confirmations: tuple[ContactConfirmation, ...],
) -> BridgeAnswer:
    if not isinstance(confirmations, tuple):
        raise TypeError("confirmations must be an immutable tuple")
    if len(confirmations) != ROOTS_REQUIRED:
        raise ValueError("bridge domain requires exactly three declared confirmations")
    for item in confirmations:
        validate_confirmation(item)
    if not c366.c364.payload_lawful(fixture, payload):
        raise ValueError("threshold payload is outside the active Cycle-342 fixture")
    target = layout.blocks[0].target_site
    root_conditions = distinct_root_conditions(target, confirmations)
    payload_conditions = (
        ("common_payload_binding", all(item.payload == payload for item in confirmations)),
        ("successful_Cycle281_positive_close", False),
    )
    diagnostics = tuple(close_diagnostic(item) for item in confirmations)
    payload_conditions = (
        payload_conditions[0],
        ("successful_Cycle281_positive_close", all(item.deterministic_positive for item in diagnostics)),
    )
    conditions = root_conditions + payload_conditions
    admitted = all(value for _name, value in conditions)
    assignments: tuple[tuple[int, c366.RedundantProposal], ...] = ()
    if admitted:
        base = c366.immediate_proposal(
            layout.blocks[0], payload, c366.FORMATION_THRESHOLD
        )
        proposal = c366.RedundantProposal(
            base.site,
            base.payload,
            base.readiness,
            tuple(c366.interface_replica(base) for _item in confirmations),
        )
        assignments = ((0, proposal),)
    prepared = c366.prepare(layout, assignments)
    if not prepared.admissible:
        raise RuntimeError(("bridge produced inadmissible threshold source", prepared.reasons))
    calculated = c366.apply_layers(prepared.state, prepared.state.layout.layers[:-1])
    committed = c366.apply_layers(calculated, (prepared.state.layout.layers[-1],))
    records = c366.logical_records(committed)
    status = "admitted-distinct-contact-confirmations" if admitted else "rejected:" + ",".join(
        name for name, value in conditions if not value
    )
    return BridgeAnswer(status, conditions, diagnostics, prepared.state, calculated, committed, records)


def rotate_coord(site: Coord, frame: np.ndarray) -> Coord:
    return c366.c362.c353.rotated(site, frame)


def rotate_layout(layout: c366.Layout, frame: np.ndarray) -> c366.Layout:
    return replace(
        layout,
        sites=tuple(replace(site, coord=rotate_coord(site.coord, frame)) for site in layout.sites),
        blocks=tuple(
            replace(
                block,
                target_site=rotate_coord(block.target_site, frame),
                predecessors=tuple(rotate_coord(site, frame) for site in block.predecessors),
            )
            for block in layout.blocks
        ),
    )


def rotate_confirmation(
    item: ContactConfirmation,
    frame: np.ndarray,
    mapping,
) -> ContactConfirmation:
    return replace(
        item,
        carrier_site=rotate_coord(item.carrier_site, frame),
        root=replace(
            item.root,
            root_site=rotate_coord(item.root.root_site, frame),
            marker_anchor=rotate_coord(item.root.marker_anchor, frame),
        ),
        payload=c366.c364.rotate_payload(item.payload, mapping),
    )


def copy_vs_distinct_root_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    layout = c366.build_layout(1)
    payload = c366.record_words(fixture, 1)[0]
    distinct = bridge_to_threshold(
        fixture, layout, payload, confirmation_set(layout.blocks[0].target_site, payload)
    )
    copies = bridge_to_threshold(
        fixture, layout, payload, copied_confirmation_set(layout.blocks[0].target_site, payload)
    )

    base = c366.immediate_proposal(layout.blocks[0], payload, 3)
    bypass = c366.step(
        c366.prepare(
            layout,
            ((0, c366.RedundantProposal(base.site, base.payload, base.readiness, tuple(c366.interface_replica(base) for _ in range(3)))),),
        ).state
    )
    detail = {
        "distinct_declared_roots_status": distinct.status,
        "distinct_declared_roots_formed": len(distinct.records),
        "one_root_fanned_to_three_carriers_status": copies.status,
        "one_root_fanned_to_three_carriers_formed": len(copies.records),
        "copy_distinct_root_marker_condition": dict(copies.conditions)["distinct_root_markers"],
        "copy_distinct_root_site_condition": dict(copies.conditions)["distinct_root_sites"],
        "Cycle366_direct_bypass_with_three_identical_replicas_formed": len(c366.logical_records(bypass)),
        "Cycle366_existing_interface_enforces_root_independence": False,
        "root_marker_storage_M2": ROOT_MARKER_M2,
        "reference_constraint_complete_support_M2": None,
        "root_constraint_maximum_L1": ROOT_CONSTRAINT_MAX_L1,
        "physical_root_independence_derived": False,
    }
    check(
        "three distinct declared contact roots pass while one close fanned into three spatial carriers is rejected before the root-blind Cycle-366 interface",
        detail["distinct_declared_roots_formed"] == 1
        and detail["one_root_fanned_to_three_carriers_formed"] == 0
        and detail["copy_distinct_root_marker_condition"] is False
        and detail["copy_distinct_root_site_condition"] is False
        and detail["Cycle366_direct_bypass_with_three_identical_replicas_formed"] == 1
        and detail["Cycle366_existing_interface_enforces_root_independence"] is False
        and detail["root_marker_storage_M2"] == 9
        and detail["reference_constraint_complete_support_M2"] is None
        and detail["physical_root_independence_derived"] is False,
        detail,
    )
    return detail


def coupling_deletion_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    layout = c366.build_layout(1)
    payload = c366.record_words(fixture, 1)[0]
    base = confirmation_set(layout.blocks[0].target_site, payload)
    rows = []
    failures = 0
    for root_index in range(ROOTS_REQUIRED):
        for leg in ("first_U_I", "second_U_I"):
            attacked = list(base)
            attacked[root_index] = replace(attacked[root_index], **{leg: "deleted"})
            answer = bridge_to_threshold(fixture, layout, payload, tuple(attacked))
            diagnostic = answer.diagnostics[root_index]
            failures += int(
                len(answer.records) != 0
                or diagnostic.close_weight >= TOL
                or diagnostic.history_weight >= TOL
                or dict(answer.conditions)["successful_Cycle281_positive_close"] is not False
            )
            rows.append(
                {
                    "required_confirmation": root_index,
                    "deleted_leg": leg,
                    "close_weight": diagnostic.close_weight,
                    "history_weight": diagnostic.history_weight,
                    "formed_Records": len(answer.records),
                }
            )
    check(
        "deleting either actual U_I in any required confirmation gives zero close/history support and suppresses threshold formation",
        len(rows) == 6 and failures == 0,
        rows,
    )
    return {"rows": rows, "failures": failures}


def q_sector_separator_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    layout = c366.build_layout(1)
    payload = c366.record_words(fixture, 1)[0]
    rows = []
    failures = 0
    for matter in (q0_input(), coherent_input()):
        confirmations = confirmation_set(layout.blocks[0].target_site, payload, matter)
        answer = bridge_to_threshold(fixture, layout, payload, confirmations)
        weights = tuple(item.close_weight for item in answer.diagnostics)
        expected = 0.0 if matter.label == "Q=0 basis" else 0.5
        failures += int(
            len(answer.records) != 0
            or any(abs(value - expected) > TOL for value in weights)
            or any(item.deterministic_positive for item in answer.diagnostics)
            or any(item.actual_branch_selector is not None for item in answer.diagnostics)
        )
        rows.append(
            {
                "matter_input": matter.label,
                "close_weights": weights,
                "actual_branch_selector": None,
                "independent_positive_branch_content_supplied": False,
                "formed_Records": len(answer.records),
            }
        )
    mixed = list(confirmation_set(layout.blocks[0].target_site, payload))
    mixed[2] = replace(mixed[2], matter=q0_input())
    mixed_answer = bridge_to_threshold(fixture, layout, payload, tuple(mixed))
    failures += int(len(mixed_answer.records) != 0)
    check(
        "Q=0 and coherent Q0+Q1 inputs do not supply three actual positive branches or any Record",
        failures == 0,
        {"rows": rows, "two_Q1_plus_one_Q0_formed": len(mixed_answer.records)},
    )
    return {"rows": rows, "failures": failures}


def frame_support_and_covariance_controls() -> dict[str, object]:
    frames = c366.c362.c353.proper_cubic_frames()
    cases = formation_failures = copy_false_positives = 0
    covariance_failures = nn_failures = constraint_failures = mapping_failures = 0
    rows = []
    for length in LENGTHS:
        fixture = c366.c364.c342.c338.build_fixture(length)
        layout = c366.build_layout(1)
        payload = c366.record_words(fixture, 1)[0]
        base_confirmations = confirmation_set(layout.blocks[0].target_site, payload)
        for frame in frames:
            rotated_fixture, mapping, failures = c366.c364.c342.mapped_fixture(fixture, frame)
            mapping_failures += failures
            framed_layout = rotate_layout(layout, frame)
            framed_payload = c366.c364.rotate_payload(payload, mapping)
            framed_confirmations = tuple(
                rotate_confirmation(item, frame, mapping) for item in base_confirmations
            )
            answer = bridge_to_threshold(
                rotated_fixture, framed_layout, framed_payload, framed_confirmations
            )
            expected_site = rotate_coord(layout.blocks[0].target_site, frame)
            formation_failures += int(
                len(answer.records) != 1
                or answer.records[0].site != expected_site
                or answer.records[0].content != framed_payload
            )
            covariance_failures += int(
                tuple(close_diagnostic(item) for item in framed_confirmations)
                != tuple(close_diagnostic(item) for item in base_confirmations)
            )
            copied = tuple(replace(item, root=framed_confirmations[0].root) for item in framed_confirmations)
            copy_answer = bridge_to_threshold(
                rotated_fixture, framed_layout, framed_payload, copied
            )
            copy_false_positives += len(copy_answer.records)
            constraint_failures += int(
                not all(value for _name, value in distinct_root_conditions(expected_site, framed_confirmations))
                or dict(copy_answer.conditions)["distinct_root_markers"] is not False
            )
            nn_failures += sum(
                not c366.support_connected_nn(gate, framed_layout.sites)
                for layer in framed_layout.layers
                for gate in layer.gates
            )
            cases += 1
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "frames": len(frames),
                "Cycle281_matter_support_M2": 18,
                "Cycle281_interface_M2": 5,
                "Cycle281_total_neighborhood_M2": 23,
                "root_marker_storage_M2": ROOT_MARKER_M2,
                "reference_constraint_complete_support_M2": None,
                "root_constraint_maximum_L1": ROOT_CONSTRAINT_MAX_L1,
            }
        )
    failures = (
        formation_failures
        + copy_false_positives
        + covariance_failures
        + nn_failures
        + constraint_failures
        + mapping_failures
    )
    detail = {
        "rows": rows,
        "L_by_frame_cases": cases,
        "proper_cubic_frames": len(frames),
        "formation_failures": formation_failures,
        "copy_false_positives": copy_false_positives,
        "contact_diagnostic_covariance_failures": covariance_failures,
        "Cycle366_connected_NN_failures": nn_failures,
        "root_constraint_covariance_failures": constraint_failures,
        "payload_mapping_failures": mapping_failures,
        "Cycle281_NN_interface_compiler": None,
        "root_constraint_NN_enforcement_compiler": None,
    }
    check(
        "distinct-root contact confirmations form covariantly at L3/L6 in all 24 frames while copies remain dark and the constructed threshold circuit stays NN",
        cases == len(LENGTHS) * 24 and failures == 0,
        detail,
    )
    return {"failures": failures, **detail}


def deletion_leakage_and_domain_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    layout = c366.build_layout(1)
    payload = c366.record_words(fixture, 2)
    nominal = confirmation_set(layout.blocks[0].target_site, payload[0])

    marker_deleted = list(nominal)
    marker_deleted[0] = replace(
        marker_deleted[0], root=replace(marker_deleted[0].root, marker=(0, 0, 0))
    )
    root_alias = list(nominal)
    root_alias[1] = replace(
        root_alias[1],
        root=replace(root_alias[1].root, root_site=root_alias[0].root.root_site),
    )
    carrier_alias = list(nominal)
    carrier_alias[1] = replace(carrier_alias[1], carrier_site=carrier_alias[0].carrier_site)
    payload_splice = list(nominal)
    payload_splice[2] = replace(payload_splice[2], payload=payload[1])
    history_deleted = list(nominal)
    history_deleted[1] = replace(history_deleted[1], history_writer=False)
    source_splice = list(nominal)
    source_splice[1] = replace(source_splice[1], source="host-close")
    far_root = list(nominal)
    far_root[2] = replace(
        far_root[2],
        root=replace(far_root[2].root, root_site=(999, 999, 999)),
    )
    invalid_calls = (
        lambda: bridge_to_threshold(fixture, layout, payload[0], tuple(marker_deleted)),
        lambda: bridge_to_threshold(fixture, layout, payload[0], nominal[:2]),
        lambda: bridge_to_threshold(fixture, layout, payload[0], tuple(source_splice)),
        lambda: bridge_to_threshold(
            fixture,
            layout,
            payload[0],
            (replace(nominal[0], matter=MatterInput("bad", ((0, 0.5 + 0j),))),) + nominal[1:],
        ),
    )
    rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            rejections += 1

    rejected_rows = []
    for label, attacked in (
        ("root_site_alias", tuple(root_alias)),
        ("carrier_alias", tuple(carrier_alias)),
        ("payload_splice", tuple(payload_splice)),
        ("history_writer_deleted", tuple(history_deleted)),
        ("far_root", tuple(far_root)),
    ):
        answer = bridge_to_threshold(fixture, layout, payload[0], attacked)
        rejected_rows.append((label, len(answer.records), answer.status))

    answer = bridge_to_threshold(fixture, layout, payload[0], nominal)
    common_fields = set(BridgeAnswer.__dataclass_fields__)
    detail = {
        "rejected_attack_rows": rejected_rows,
        "domain_rejections": rejections,
        "domain_attempts": len(invalid_calls),
        "nominal_workspace_leakage": c366.workspace_leakage(answer.committed),
        "precommit_logical_Records": len(c366.logical_records(answer.calculated)),
        "post_CONSUME_logical_Records": len(answer.records),
        "confirmation_carriers_typed_as_Records": 0,
        "root_markers_typed_as_Records": 0,
        "actual_branch_selector": None,
        "BridgeAnswer_fields": tuple(sorted(common_fields)),
    }
    check(
        "root/carrier aliases, marker/history deletion, payload/source splices, far roots, malformed matter, and transcript leakage are visible",
        all(records == 0 for _label, records, _status in rejected_rows)
        and rejections == len(invalid_calls)
        and detail["nominal_workspace_leakage"] == 0
        and detail["precommit_logical_Records"] == 0
        and detail["post_CONSUME_logical_Records"] == 1
        and detail["confirmation_carriers_typed_as_Records"] == 0
        and detail["root_markers_typed_as_Records"] == 0
        and detail["actual_branch_selector"] is None,
        detail,
    )
    return detail


def mass_contact_and_supplied_structure_controls() -> dict[str, object]:
    q0, q = c281.contact_projectors()
    occupations = np.asarray([index.bit_count() for index in range(64)])
    species = c281.c278.c219.common_species(c281.c278.c230.BETA)
    fock_coin = c281.c278.c229.fock_lift(species.coin)
    contact = np.diag(
        np.exp(
            1j
            * c281.c278.c230.COUPLING
            * occupations
            * (occupations - 1)
            / 2
        )
    )
    mass_residual = abs(c281.c278.c219.rest_mass(species) / species.analytic_mass - 1)
    with redirect_stdout(StringIO()):
        inherited = c366.inherited_physics_controls()
    inventory = {
        "result": "bounded conditional Cycle-281 distinct-root positive-contact confirmation to Cycle-366 threshold bridge",
        "Cycle281_close": "actual same-pointer couple-archive-recouple positive-contact close",
        "Cycle281_positive_close_selected_as_occurrence": False,
        "Cycle281_payload_binding": "supplied exact binding between each contact confirmation and one lawful 30-M2 candidate payload",
        "root_markers": "three supplied one-hot three-M2 labels",
        "root_marker_storage_M2": ROOT_MARKER_M2,
        "reference_constraint_complete_support_M2": None,
        "root_marker_genesis": "supplied",
        "physical_independence": "supplied; distinct labels/sites are not a derivation of dynamical independence",
        "root_constraint_autonomous_enforcement": None,
        "Cycle281_interface_NN_compiler": None,
        "Cycle281_to_Cycle366_bridge_compiler": None,
        "Cycle366_existing_independence_enforcement": False,
        "Cycle366_selected": False,
        "threshold_three_selected": False,
        "threshold_three_derived": False,
        "CONSUME_selected": False,
        "CONSUME_admission_by_existing_framework_law": None,
        "actual_branch_selector": None,
        "Q0_negative_close": None,
        "coherent_branch_actualization": None,
        "shared_substrate_obstruction": None,
        "no_go": None,
        "minimum_content": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    contact_detail = {
        "Q_coin_commutator": float(np.linalg.norm(q @ fock_coin - fock_coin @ q)),
        "Q_contact_commutator": float(np.linalg.norm(q @ contact - contact @ q)),
        "Q0_plus_Q_identity_residual": float(np.linalg.norm(q0 + q - np.eye(64))),
        "one_particle_Q_weight": float(np.max(np.diag(q).real[occupations <= 1])),
        "mass_relative_residual": mass_residual,
        "Cycle366_inherited_physics_failures": inherited["failures"],
        "inventory": inventory,
    }
    check(
        "the bridge preserves the Cycle-281 contact/mass and Cycle-366 seam fixtures while inventorying root genesis and physical independence as supplied",
        max(
            contact_detail["Q_coin_commutator"],
            contact_detail["Q_contact_commutator"],
            contact_detail["Q0_plus_Q_identity_residual"],
            contact_detail["one_particle_Q_weight"],
        ) < TOL
        and mass_residual < 2e-12
        and inherited["failures"] == 0
        and inventory["Cycle281_positive_close_selected_as_occurrence"] is False
        and inventory["root_marker_genesis"] == "supplied"
        and inventory["root_marker_storage_M2"] == 9
        and inventory["reference_constraint_complete_support_M2"] is None
        and inventory["physical_independence"].startswith("supplied")
        and inventory["root_constraint_autonomous_enforcement"] is None
        and inventory["Cycle281_interface_NN_compiler"] is None
        and inventory["Cycle281_to_Cycle366_bridge_compiler"] is None
        and inventory["Cycle366_existing_independence_enforcement"] is False
        and inventory["Cycle366_selected"] is False
        and inventory["threshold_three_selected"] is False
        and inventory["CONSUME_admission_by_existing_framework_law"] is None
        and inventory["actual_branch_selector"] is None
        and inventory["shared_substrate_obstruction"] is None
        and inventory["no_go"] is inventory["minimum_content"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        contact_detail,
    )
    return contact_detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 379: CYCLE-281 DISTINCT-ROOT CONTACT CONFIRMATIONS -> CYCLE-366 THRESHOLD")
    print("authority=none; audit=unset; threshold/CONSUME/root independence unselected")
    note = note_contract()
    roots = copy_vs_distinct_root_controls()
    deletions = coupling_deletion_controls()
    separators = q_sector_separator_controls()
    frames = frame_support_and_covariance_controls()
    attacks = deletion_leakage_and_domain_controls()
    physics = mass_contact_and_supplied_structure_controls()
    check(
        "Cycle 379 gives a bounded constructive contact-confirmation bridge without promoting copied closes or supplied root markers to physical independence",
        not note["missing"]
        and roots["distinct_declared_roots_formed"] == 1
        and roots["one_root_fanned_to_three_carriers_formed"] == 0
        and deletions["failures"] == 0
        and separators["failures"] == 0
        and frames["failures"] == 0
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and physics["inventory"]["CONSUME_admission_by_existing_framework_law"] is None
        and physics["inventory"]["shared_substrate_obstruction"] is None,
        {
            "disposition": "bounded positive conditional distinct-root contact-confirmation bridge",
            "strongest_positive": "three declared distinct Cycle281 positive closes pass; three copies of one close remain dark",
            "open_physical_residual": "root-marker genesis, physical independence/enforcement, bridge compiler, CONSUME admission",
            "selected_threshold": None,
            "shared_obstruction": None,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_CONTACT_DISTINCT_ROOT_THRESHOLD_BRIDGE_OPEN")
        return 1
    print("RESULT PHYSICAL_CONTACT_DISTINCT_ROOT_THRESHOLD_BRIDGE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
