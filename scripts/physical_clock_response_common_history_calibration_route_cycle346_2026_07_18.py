#!/usr/bin/env python3
"""Cycle 346 Route 3: conditional clock/response common-key normalization.

Join one conditional typed permanent Cycle-342 cylinder endpoint to the
Cycle-313 physical source/mediator response in one bounded computational-basis
control register.  A reversible equality/coincidence gate writes a handshake
bit only when the complete cylinder key, spatial placement, named clock,
Record typing/permanence, installed response instrument, and supplied response
event all agree.  Only that joint witness may form and append a calibration
Record.

The construction is conditional.  Clock placement/name, response-instrument
preparation and outcome, the handshake truth table, Record semantics, and the
calibration convention remain supplied.  The bounded register width is not a
nearest-neighbour support certificate.  The calibrated scalar is response per
named Record count, not a physical rate.  Kappa, wrapped phase, a generator
element, occupation, and circuit/update count are not called energy, rate, or
time.  Numerical response and calibration floats remain external to the
82-M2 common key; an explicit control below shows that changing those floats
can leave the key unchanged while changing the host-side diagnostic.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_m2_source_response_common_seam_cycle313_2026_07_18 as c313
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


AUTHORITY = "none"
AUDIT = "unset"
CLOCK_NAME = "Cycle342 complete-cylinder Record chain"
CLOCK_ENDPOINT = 0
ROUTE_LENGTHS = (3, 6)
COORD_BITS = 3
HISTORY_BITS = c342.c338.CYLINDER_BITS
COMMON_CODE_BITS = (
    c342.RECORD_BITS
    + HISTORY_BITS
    + 2 * 3 * COORD_BITS
    + 1  # L=3/L=6 selector
    + 1  # response instrument installed
    + 1  # supplied response event occurred
    + 1  # n=1/n=2 selector
    + 1  # named clock present
    + 1  # common-history handshake
)
TOLERANCE = 3e-12

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


def bits(value: int, width: int) -> tuple[int, ...]:
    if value < 0 or value >= 1 << width:
        raise ValueError("integer does not fit the declared M2 basis register")
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def coordinate_word(cell: tuple[int, int, int]) -> tuple[int, ...]:
    if len(cell) != 3:
        raise ValueError("a physical placement needs three coordinates")
    return tuple(bit for value in cell for bit in bits(value, COORD_BITS))


def validate_route_fixture(
    length: int, source: tuple[int, int, int], matter_number: int
) -> None:
    if length not in ROUTE_LENGTHS:
        raise ValueError("the calibration route is declared only at L=3 and held L=6")
    c313.validate_fixture(length, source, matter_number)


def neighbour_event_projector(
    length: int, source: tuple[int, int, int]
) -> sparse.csr_matrix:
    """Project onto the six streamed directional M2 adjacent to one source."""

    validate_route_fixture(length, source, 1)
    diagonal = np.zeros(1 + 6 * length**3, dtype=float)
    for direction, displacement in enumerate(c313.c210.DIRECTIONS):
        target = c313.shifted(source, displacement, length)
        diagonal[1 + 6 * c313.site_index(target, length) + direction] = 1
    return sparse.diags(diagonal.astype(complex), format="csr")


def physical_response_metrics(
    length: int, source: tuple[int, int, int], matter_number: int
) -> dict[str, object]:
    validate_route_fixture(length, source, matter_number)
    *_, update = c313.one_source_layers(length, source, matter_number)
    initial = np.zeros(update.shape[0], dtype=complex)
    initial[0] = 1
    output = update @ initial
    event = neighbour_event_projector(length, source)
    complement = sparse.eye(event.shape[0], dtype=complex, format="csr") - event
    weight = float(np.real(np.vdot(output, event @ output)))
    predicted = float(np.sin(c313.THETA * matter_number) ** 2)
    return {
        "length": length,
        "source": source,
        "matter_number": matter_number,
        "event_weight": weight,
        "predicted_sin2_response": predicted,
        "prediction_residual": abs(weight - predicted),
        "instrument_projector_residual": float(
            sparse_linalg.norm(event @ event - event)
        ),
        "instrument_completeness_residual": float(
            sparse_linalg.norm(event + complement - sparse.eye(event.shape[0]))
        ),
        "output_norm_residual": abs(float(np.vdot(output, output).real) - 1),
        "event_rank_on_Q1_code": int(round(float(event.diagonal().real.sum()))),
    }


@dataclass(frozen=True)
class ResponseEvent:
    length: int
    source: tuple[int, int, int]
    history_key: tuple[int, ...]
    matter_number: int
    instrument_installed: bool
    event_occurs: bool
    response_weight: float | None
    predicted_weight: float | None


@dataclass(frozen=True)
class CommonHistoryCode:
    clock: c342.CylinderRecord
    clock_cell: tuple[int, int, int]
    response: ResponseEvent
    clock_name: str | None
    handshake: int


@dataclass(frozen=True)
class CalibrationRecord:
    common: CommonHistoryCode
    typed: bool
    permanent: bool


@dataclass(frozen=True)
class CalibrationBook:
    records: tuple[CalibrationRecord, ...]
    capacity: int


def validate_response_event(event: ResponseEvent) -> None:
    validate_route_fixture(event.length, event.source, event.matter_number)
    if len(event.history_key) != HISTORY_BITS or any(
        bit not in (0, 1) for bit in event.history_key
    ):
        raise ValueError("the response instrument needs one complete cylinder key")
    if not isinstance(event.instrument_installed, bool) or not isinstance(
        event.event_occurs, bool
    ):
        raise ValueError("instrument and event predicates are basis bits")
    if event.instrument_installed:
        if event.response_weight is None or event.predicted_weight is None:
            raise ValueError("an installed instrument needs its physical response statistic")
        if not (
            np.isfinite(event.response_weight)
            and np.isfinite(event.predicted_weight)
            and 0 <= event.response_weight <= 1
            and 0 <= event.predicted_weight <= 1
        ):
            raise ValueError("response weights must be finite unit-interval scalars")
    elif event.response_weight is not None or event.predicted_weight is not None:
        raise ValueError("a deleted response instrument exposes no numerical response")


def response_event(
    length: int,
    source: tuple[int, int, int],
    matter_number: int,
    history_key: tuple[int, ...],
    *,
    instrument_installed: bool = True,
    event_occurs: bool = True,
) -> ResponseEvent:
    metrics = (
        physical_response_metrics(length, source, matter_number)
        if instrument_installed
        else None
    )
    event = ResponseEvent(
        length=length,
        source=source,
        history_key=history_key,
        matter_number=matter_number,
        instrument_installed=instrument_installed,
        event_occurs=event_occurs,
        response_weight=None if metrics is None else float(metrics["event_weight"]),
        predicted_weight=None
        if metrics is None
        else float(metrics["predicted_sin2_response"]),
    )
    validate_response_event(event)
    return event


def validate_common_code(fixture: c342.c338.RouteFixture, code: CommonHistoryCode) -> None:
    if code.handshake not in (0, 1):
        raise ValueError("the handshake is one M2 basis bit")
    if code.clock_name not in (None, CLOCK_NAME):
        raise ValueError("the route accepts only its declared named clock")
    validate_response_event(code.response)
    if code.response.length != fixture.length:
        raise ValueError("clock and response must inhabit the same finite fixture")
    if len(code.clock_cell) != 3 or any(
        value < 0 or value >= fixture.length for value in code.clock_cell
    ):
        raise ValueError("the clock placement is outside the common finite code")
    c342.decode_record_word(c342.record_word(code.clock))


def common_code_word(code: CommonHistoryCode) -> tuple[int, ...]:
    word = (
        c342.record_word(code.clock)
        + code.response.history_key
        + coordinate_word(code.clock_cell)
        + coordinate_word(code.response.source)
        + (int(code.response.length == 6),)
        + (int(code.response.instrument_installed),)
        + (int(code.response.event_occurs),)
        + (code.response.matter_number - 1,)
        + (int(code.clock_name == CLOCK_NAME),)
        + (code.handshake,)
    )
    if len(word) != COMMON_CODE_BITS or any(bit not in (0, 1) for bit in word):
        raise RuntimeError("common-history product-register inventory drifted")
    return word


def coincidence_predicate(
    fixture: c342.c338.RouteFixture, code: CommonHistoryCode
) -> bool:
    validate_common_code(fixture, code)
    return bool(
        c342.cylinder_is_lawful(fixture, code.clock.cylinder)
        and code.clock.typed
        and code.clock.permanent
        and code.clock_name == CLOCK_NAME
        and code.clock.cylinder.endpoint == CLOCK_ENDPOINT
        and code.response.instrument_installed
        and code.response.event_occurs
        and code.clock_cell == code.response.source
        and c342.c338.cylinder_word(code.clock.cylinder) == code.response.history_key
    )


def handshake_gate(
    fixture: c342.c338.RouteFixture, code: CommonHistoryCode
) -> CommonHistoryCode:
    """One reversible XOR gate on the joint clock/response basis register."""

    predicate = int(coincidence_predicate(fixture, code))
    return replace(code, handshake=code.handshake ^ predicate)


def form_calibration_record(
    fixture: c342.c338.RouteFixture, common: object
) -> CalibrationRecord | None:
    if not isinstance(common, CommonHistoryCode):
        raise TypeError("separate/tensored outputs are not a common-history witness")
    validate_common_code(fixture, common)
    if common.handshake != 1 or not coincidence_predicate(fixture, common):
        return None
    return CalibrationRecord(common=common, typed=True, permanent=True)


def append_calibration(
    book: CalibrationBook, record: CalibrationRecord | None
) -> CalibrationBook:
    if record is None or not record.typed or not record.permanent:
        raise ValueError("only a handshaken typed permanent calibration Record appends")
    encoded = common_code_word(record.common)
    if any(common_code_word(item.common) == encoded for item in book.records):
        raise ValueError(
            "one common-event control word cannot be counted twice without a new event identity"
        )
    if len(book.records) >= book.capacity:
        raise ValueError("the supplied finite calibration page is exhausted")
    return CalibrationBook(book.records + (record,), book.capacity)


def erase_calibration(_book: CalibrationBook, _index: int) -> CalibrationBook:
    raise ValueError("the declared post-Record domain is append-only")


def calibration_count(book: CalibrationBook) -> int | None:
    if not book.records:
        return None
    return c342.cycle22_commit_count(
        tuple(record.common.clock for record in book.records),
        named_chain=CLOCK_NAME,
    )


def calibrated_response_per_count(
    book: CalibrationBook, calibration_constant: float | None
) -> float | None:
    if calibration_constant is None:
        return None
    if not np.isfinite(calibration_constant) or calibration_constant <= 0:
        raise ValueError("the supplied calibration constant must be positive and finite")
    count = calibration_count(book)
    if count is None or count <= 0:
        return None
    if any(
        record.common.handshake != 1
        or not record.typed
        or not record.permanent
        or record.common.response.response_weight is None
        for record in book.records
    ):
        return None
    response = sum(
        float(record.common.response.response_weight) for record in book.records
    )
    return calibration_constant * response / count


def common_candidate(
    fixture: c342.c338.RouteFixture,
    matter_number: int,
    *,
    source: tuple[int, int, int] = c313.SOURCE,
    endpoint: int = CLOCK_ENDPOINT,
    occurrence: bool = True,
    commit: bool = True,
    typing: bool = True,
    permanence: bool = True,
    fibre_certified: bool = True,
    instrument_installed: bool = True,
    response_occurs: bool = True,
    clock_name: str | None = CLOCK_NAME,
    response_history_key: tuple[int, ...] | None = None,
    clock_cell: tuple[int, int, int] | None = None,
) -> CommonHistoryCode:
    cylinder = c342.make_cylinder_chain(fixture, endpoint, 1)[0]
    clock = c342.form_conditional_record(
        fixture,
        cylinder,
        occurrence=occurrence,
        commit=commit,
        typing=typing,
        permanence=permanence,
        fibre_certified=fibre_certified,
    )
    key = c342.c338.cylinder_word(cylinder)
    event = response_event(
        fixture.length,
        source,
        matter_number,
        key if response_history_key is None else response_history_key,
        instrument_installed=instrument_installed,
        event_occurs=response_occurs,
    )
    code = CommonHistoryCode(
        clock=clock,
        clock_cell=source if clock_cell is None else clock_cell,
        response=event,
        clock_name=clock_name,
        handshake=0,
    )
    validate_common_code(fixture, code)
    return code


def handshaken_book(
    fixture: c342.c338.RouteFixture,
    matter_number: int,
    *,
    source: tuple[int, int, int] = c313.SOURCE,
) -> tuple[CommonHistoryCode, CalibrationRecord, CalibrationBook]:
    blank = common_candidate(fixture, matter_number, source=source)
    joined = handshake_gate(fixture, blank)
    record = form_calibration_record(fixture, joined)
    if record is None:
        raise RuntimeError("the lawful common-history fixture did not handshake")
    book = append_calibration(CalibrationBook((), 1), record)
    return joined, record, book


def product_code_and_handshake_controls(
    fixtures: dict[int, c342.c338.RouteFixture]
) -> dict[str, object]:
    fixture = fixtures[3]
    blank = common_candidate(fixture, 1)
    joined = handshake_gate(fixture, blank)
    restored = handshake_gate(fixture, joined)
    record = form_calibration_record(fixture, joined)
    book = append_calibration(CalibrationBook((), 1), record)

    tensor_rejected = False
    try:
        form_calibration_record(fixture, (blank.clock, blank.response))
    except TypeError:
        tensor_rejected = True
    host_aligned_rejected = False
    try:
        form_calibration_record(fixture, (0, 0, blank.clock, blank.response))
    except TypeError:
        host_aligned_rejected = True
    occupied_rejected = False
    try:
        append_calibration(book, record)
    except ValueError:
        occupied_rejected = True
    duplicate_event_rejected = False
    try:
        first = append_calibration(CalibrationBook((), 2), record)
        append_calibration(first, record)
    except ValueError:
        duplicate_event_rejected = True
    erase_rejected = False
    try:
        erase_calibration(book, 0)
    except ValueError:
        erase_rejected = True

    detail = {
        "common_product_register_M2_width": len(common_code_word(joined)),
        "clock_Record_M2_width": c342.RECORD_BITS,
        "response_history_key_M2_width": HISTORY_BITS,
        "handshake_bit": joined.handshake,
        "exact_XOR_inverse": restored == blank,
        "named_Record_count": calibration_count(book),
        "separate_tensor_outputs_rejected": tensor_rejected,
        "equal_host_indices_rejected": host_aligned_rejected,
        "second_append_without_capacity_rejected": occupied_rejected,
        "duplicate_common_event_rejected_with_spare_capacity": duplicate_event_rejected,
        "post_Record_erase_rejected": erase_rejected,
        "host_update_index_in_common_code": None,
        "nearest_neighbour_handshake_support_M2": None,
        "register_width_is_nearest_neighbour_support": False,
    }
    check(
        "one bounded common-key equality gate conditionally forms an append-only control Record and refuses duplicate event words",
        record is not None
        and record.typed
        and record.permanent
        and detail["common_product_register_M2_width"] == COMMON_CODE_BITS == 82
        and detail["handshake_bit"] == 1
        and detail["exact_XOR_inverse"]
        and detail["named_Record_count"] == 1
        and tensor_rejected
        and host_aligned_rejected
        and occupied_rejected
        and duplicate_event_rejected
        and erase_rejected
        and detail["nearest_neighbour_handshake_support_M2"] is None
        and not detail["register_width_is_nearest_neighbour_support"],
        detail,
    )
    return detail


def calibration_training_and_held_controls(
    fixtures: dict[int, c342.c338.RouteFixture]
) -> dict[str, object]:
    train_joined, train_record, train_book = handshaken_book(fixtures[3], 1)
    training_response = float(train_record.common.response.response_weight)
    calibration_constant = 1.0 / training_response
    training_value = calibrated_response_per_count(train_book, calibration_constant)

    held_rows = []
    for length, matter_number, hold in (
        (3, 2, "held matter number"),
        (6, 2, "held matter number and held size"),
    ):
        joined, record, book = handshaken_book(fixtures[length], matter_number)
        value = calibrated_response_per_count(book, calibration_constant)
        held_rows.append(
            {
                "L": length,
                "matter_number": matter_number,
                "hold": hold,
                "handshake": joined.handshake,
                "Record_count": calibration_count(book),
                "raw_physical_response": record.common.response.response_weight,
                "predicted_response": record.common.response.predicted_weight,
                "calibrated_response_per_named_count": value,
                "evaluated_only_after_handshake": joined.handshake == 1,
            }
        )
    predicted_ratio = float(
        np.sin(2 * c313.THETA) ** 2 / np.sin(c313.THETA) ** 2
    )
    detail = {
        "training": {
            "L": 3,
            "matter_number": 1,
            "handshake": train_joined.handshake,
            "Record_count": calibration_count(train_book),
            "raw_physical_response": training_response,
            "supplied_calibration_target": 1.0,
            "fitted_calibration_constant": calibration_constant,
            "calibrated_response_per_named_count": training_value,
        },
        "held": held_rows,
        "predicted_n2_over_n1_response": predicted_ratio,
        "maximum_raw_response_residual": max(
            abs(float(row["raw_physical_response"]) - float(row["predicted_response"]))
            for row in held_rows
        ),
        "held_size_residual": abs(
            float(held_rows[0]["calibrated_response_per_named_count"])
            - float(held_rows[1]["calibrated_response_per_named_count"])
        ),
        "physical_rate": None,
        "physical_time": None,
    }
    check(
        "the n=1 handshaken Record fixes one supplied normalization convention and re-evaluates the inherited held n=2 and L=6 response only after their own handshakes",
        train_joined.handshake == 1
        and calibration_count(train_book) == 1
        and abs(float(training_value) - 1.0) < 2e-15
        and all(row["handshake"] == 1 for row in held_rows)
        and all(row["Record_count"] == 1 for row in held_rows)
        and all(row["evaluated_only_after_handshake"] for row in held_rows)
        and detail["maximum_raw_response_residual"] < 2e-14
        and abs(
            float(held_rows[0]["calibrated_response_per_named_count"])
            - predicted_ratio
        )
        < 2e-14
        and detail["held_size_residual"] < 2e-14
        and detail["physical_rate"] is None
        and detail["physical_time"] is None,
        detail,
    )
    return detail


def deletion_and_rescaling_controls(
    fixtures: dict[int, c342.c338.RouteFixture], calibration_constant: float
) -> dict[str, object]:
    fixture = fixtures[3]
    base = common_candidate(fixture, 1)
    joined = handshake_gate(fixture, base)
    record = form_calibration_record(fixture, joined)
    if record is None:
        raise RuntimeError("base deletion fixture did not form")
    book = append_calibration(CalibrationBook((), 1), record)

    def attempted_record(code: CommonHistoryCode, apply_handshake: bool = True):
        candidate = handshake_gate(fixture, code) if apply_handshake else code
        return form_calibration_record(fixture, candidate)

    bad_key = (1 - base.response.history_key[0],) + base.response.history_key[1:]
    attacks = {
        "handshake": attempted_record(base, apply_handshake=False),
        "response_instrument": attempted_record(
            common_candidate(fixture, 1, instrument_installed=False)
        ),
        "clock_name": attempted_record(common_candidate(fixture, 1, clock_name=None)),
        "clock_endpoint": attempted_record(
            common_candidate(fixture, 1, endpoint=(CLOCK_ENDPOINT + 1) % 3)
        ),
        "typing": attempted_record(common_candidate(fixture, 1, typing=False)),
        "permanence": attempted_record(common_candidate(fixture, 1, permanence=False)),
        "response_event": attempted_record(
            common_candidate(fixture, 1, response_occurs=False)
        ),
        "history_key": attempted_record(
            common_candidate(fixture, 1, response_history_key=bad_key)
        ),
        "spatial_coincidence": attempted_record(
            common_candidate(fixture, 1, clock_cell=(1, 0, 0))
        ),
    }
    deleted_outputs = {
        name: None
        if attacked is None
        else calibrated_response_per_count(
            append_calibration(CalibrationBook((), 1), attacked),
            calibration_constant,
        )
        for name, attacked in attacks.items()
    }
    deleted_outputs["calibration_constant"] = calibrated_response_per_count(book, None)

    base_word = common_code_word(record.common)
    base_count = calibration_count(book)
    base_value = calibrated_response_per_count(book, calibration_constant)
    rescaled_value = calibrated_response_per_count(book, 2 * calibration_constant)
    altered_common = replace(
        record.common,
        response=replace(
            record.common.response,
            response_weight=0.5,
            predicted_weight=0.5,
        ),
    )
    validate_common_code(fixture, altered_common)
    altered_record = CalibrationRecord(
        common=altered_common, typed=True, permanent=True
    )
    altered_book = append_calibration(CalibrationBook((), 1), altered_record)
    altered_value = calibrated_response_per_count(
        altered_book, calibration_constant
    )
    detail = {
        "deleted_records": {name: attacked is None for name, attacked in attacks.items()},
        "deleted_outputs": deleted_outputs,
        "all_deleted_outputs_undefined_never_zero": all(
            value is None for value in deleted_outputs.values()
        ),
        "base_Record_count": base_count,
        "rescaled_Record_count": calibration_count(book),
        "history_word_unchanged_under_rescaling": common_code_word(record.common)
        == base_word,
        "base_calibrated_response": base_value,
        "twice_calibration_constant_response": rescaled_value,
        "rescaling_changes_only_numerical_calibration": abs(
            float(rescaled_value) - 2 * float(base_value)
        )
        < 2e-14,
        "response_floats_encoded_in_common_word": False,
        "same_common_word_after_response_float_retarget": common_code_word(
            altered_common
        )
        == base_word,
        "handshake_unchanged_after_response_float_retarget": altered_common.handshake
        == record.common.handshake
        == 1,
        "numerical_output_changes_after_unencoded_float_retarget": abs(
            float(altered_value) - float(base_value)
        )
        > 0.1,
        "altered_unencoded_response_output": altered_value,
        "numerical_response_registration_open": True,
        "rate_after_each_deletion": None,
    }
    check(
        "handshake instrument name typing permanence calibration and common-key deletions make response-per-count undefined, while rescaling leaves count/history fixed and changes only the numerical result",
        all(attacked is None for attacked in attacks.values())
        and detail["all_deleted_outputs_undefined_never_zero"]
        and base_count == detail["rescaled_Record_count"] == 1
        and detail["history_word_unchanged_under_rescaling"]
        and detail["rescaling_changes_only_numerical_calibration"]
        and not detail["response_floats_encoded_in_common_word"]
        and detail["same_common_word_after_response_float_retarget"]
        and detail["handshake_unchanged_after_response_float_retarget"]
        and detail["numerical_output_changes_after_unencoded_float_retarget"]
        and detail["numerical_response_registration_open"]
        and detail["rate_after_each_deletion"] is None,
        detail,
    )
    return detail


def covariance_translation_and_held_controls(
    fixtures: dict[int, c342.c338.RouteFixture]
) -> dict[str, object]:
    length = 3
    fixture = fixtures[length]
    base_source = c313.SOURCE
    frames = c313.c210.proper_cubic_frames()
    frame_update_residuals = []
    frame_instrument_residuals = []
    frame_response_residuals = []
    translation_update_residuals = []
    translation_instrument_residuals = []
    translation_response_residuals = []
    clock_mapping_failures = common_failures = 0

    for matter_number in (1, 2):
        *_, base_update = c313.one_source_layers(length, base_source, matter_number)
        base_event = neighbour_event_projector(length, base_source)
        base_weight = physical_response_metrics(length, base_source, matter_number)[
            "event_weight"
        ]
        for frame in frames:
            representation = c313.field_family_representation(length, frame=frame)
            target_source = tuple(
                int(value % length) for value in frame @ np.asarray(base_source)
            )
            *_, target_update = c313.one_source_layers(
                length, target_source, matter_number
            )
            target_event = neighbour_event_projector(length, target_source)
            frame_update_residuals.append(
                float(
                    sparse_linalg.norm(
                        representation @ base_update - target_update @ representation
                    )
                )
            )
            frame_instrument_residuals.append(
                float(
                    sparse_linalg.norm(
                        representation @ base_event - target_event @ representation
                    )
                )
            )
            target_weight = physical_response_metrics(
                length, target_source, matter_number
            )["event_weight"]
            frame_response_residuals.append(abs(float(target_weight) - float(base_weight)))

            rotated, _mapping, failures = c342.mapped_fixture(fixture, frame)
            clock_mapping_failures += failures
            candidate = common_candidate(
                rotated, matter_number, source=target_source, clock_cell=target_source
            )
            joined = handshake_gate(rotated, candidate)
            common_failures += int(form_calibration_record(rotated, joined) is None)

        for translation in product(range(length), repeat=3):
            representation = c313.field_family_representation(
                length, translation=translation
            )
            target_source = tuple(
                (base_source[axis] + translation[axis]) % length for axis in range(3)
            )
            *_, target_update = c313.one_source_layers(
                length, target_source, matter_number
            )
            target_event = neighbour_event_projector(length, target_source)
            translation_update_residuals.append(
                float(
                    sparse_linalg.norm(
                        representation @ base_update - target_update @ representation
                    )
                )
            )
            translation_instrument_residuals.append(
                float(
                    sparse_linalg.norm(
                        representation @ base_event - target_event @ representation
                    )
                )
            )
            target_weight = physical_response_metrics(
                length, target_source, matter_number
            )["event_weight"]
            translation_response_residuals.append(
                abs(float(target_weight) - float(base_weight))
            )
            candidate = common_candidate(
                fixture, matter_number, source=target_source, clock_cell=target_source
            )
            joined = handshake_gate(fixture, candidate)
            common_failures += int(form_calibration_record(fixture, joined) is None)

    held_rows = []
    for matter_number in (1, 2):
        metrics = physical_response_metrics(6, c313.SOURCE, matter_number)
        joined, _record, book = handshaken_book(fixtures[6], matter_number)
        held_rows.append(
            {
                "L": 6,
                "matter_number": matter_number,
                "response_residual": metrics["prediction_residual"],
                "instrument_rank": metrics["event_rank_on_Q1_code"],
                "handshake": joined.handshake,
                "Record_count": calibration_count(book),
            }
        )

    detail = {
        "proper_cubic_frame_cases": len(frame_update_residuals),
        "L3_translation_cases": len(translation_update_residuals),
        "maximum_frame_update_residual": max(frame_update_residuals),
        "maximum_frame_instrument_residual": max(frame_instrument_residuals),
        "maximum_frame_response_residual": max(frame_response_residuals),
        "maximum_translation_update_residual": max(translation_update_residuals),
        "maximum_translation_instrument_residual": max(
            translation_instrument_residuals
        ),
        "maximum_translation_response_residual": max(translation_response_residuals),
        "clock_mapping_failures": clock_mapping_failures,
        "common_history_failures": common_failures,
        "held_L6": held_rows,
        "proper_cubic_covariance_is_spatial": True,
    }
    check(
        "the common-history handshake carries the Cycle-313 update and six-M2 response instrument through all frames/translations and held L6",
        detail["proper_cubic_frame_cases"] == 48
        and detail["L3_translation_cases"] == 54
        and max(
            detail["maximum_frame_update_residual"],
            detail["maximum_frame_instrument_residual"],
            detail["maximum_frame_response_residual"],
            detail["maximum_translation_update_residual"],
            detail["maximum_translation_instrument_residual"],
            detail["maximum_translation_response_residual"],
        )
        < TOLERANCE
        and clock_mapping_failures == common_failures == 0
        and all(row["response_residual"] < 2e-14 for row in held_rows)
        and all(row["instrument_rank"] == 6 for row in held_rows)
        and all(row["handshake"] == row["Record_count"] == 1 for row in held_rows)
        and detail["proper_cubic_covariance_is_spatial"],
        detail,
    )
    return detail


def mass_contact_source_and_deletion_firewalls(
    fixture: c342.c338.RouteFixture,
) -> dict[str, object]:
    species = c313.c219.common_species(c313.BETA)
    encoding = c313.c306.constrained_encoding()
    _, _logical, physical = c313.c306.old_and_new_operators(c313.BETA)
    scalar = np.zeros(c313.c306.c304.LOGICAL_DIMENSION, dtype=complex)
    scalar[:6] = c313.c210.UNIFORM
    encoded = encoding @ scalar
    eigenvalue = np.vdot(encoded, physical["coin"] @ encoded)
    physical_mass = float(np.angle(eigenvalue)) / c313.c219.C_SQUARED
    contact_zero = c313.c306.lift_physical(c313.c306.c304.physical_contact(0.0))
    contact_firewall = float(
        np.linalg.norm((physical["contact"] - contact_zero) @ encoding[:, :12])
    )
    _logical_number, physical_number = c313.matter_number_operators()
    contact_number_commutator = float(
        np.linalg.norm(
            physical["contact"] @ physical_number
            - physical_number @ physical["contact"]
        )
    )

    length = 3
    initial = np.zeros(1 + 6 * length**3, dtype=complex)
    initial[0] = 1
    coin = c313.field_coin(length)
    stream = c313.field_stream(length)
    zero_coupling = stream @ c313.field_vertex(length, c313.SOURCE, 0.0) @ coin
    zero_response_norm = float(np.linalg.norm(zero_coupling @ initial - initial))
    lawful = c313.one_source_layers(length, c313.SOURCE, 1)[-1] @ initial
    lawful_event_weight = float(
        np.real(
            np.vdot(
                lawful,
                neighbour_event_projector(length, c313.SOURCE) @ lawful,
            )
        )
    )
    no_stream = c313.field_vertex(length, c313.SOURCE, c313.THETA) @ coin
    no_stream_state = no_stream @ initial
    no_stream_neighbor_weight = float(
        np.real(
            np.vdot(
                no_stream_state,
                neighbour_event_projector(length, c313.SOURCE) @ no_stream_state,
            )
        )
    )
    operators = c313.reservoir.reservoir_field_operators()
    lowering = np.asarray(((0, 1), (0, 0)), dtype=complex)
    emission_only = np.kron(lowering, operators["creation"])
    nonconjugate_gate = np.eye(128, dtype=complex) - 1j * c313.THETA * emission_only
    emission_only_unitarity_residual = float(
        np.linalg.norm(
            nonconjugate_gate.conj().T @ nonconjugate_gate - np.eye(128)
        )
    )
    matter_number_control_deletion_residual = float(
        np.linalg.norm(
            c313.dressed.local_vertex_block(2 * c313.THETA)
            - c313.dressed.local_vertex_block(c313.THETA)
        )
    )
    source_deleted = common_candidate(
        fixture, 1, instrument_installed=False, response_occurs=False
    )
    source_deleted_record = form_calibration_record(
        fixture, handshake_gate(fixture, source_deleted)
    )

    detail = {
        "physical_rest_mass": physical_mass,
        "Cycle219_rest_mass_fixture": c313.c219.rest_mass(species),
        "one_particle_contact_firewall": contact_firewall,
        "contact_number_commutator": contact_number_commutator,
        "zero_coupling_response_norm": zero_response_norm,
        "lawful_streamed_six_neighbour_response": lawful_event_weight,
        "six_neighbour_response_if_stream_deleted": no_stream_neighbor_weight,
        "emission_only_nonconjugate_unitarity_residual": emission_only_unitarity_residual,
        "matter_number_control_deletion_residual": matter_number_control_deletion_residual,
        "calibration_Record_after_source_or_instrument_deletion": source_deleted_record,
        "calibrated_output_after_source_or_instrument_deletion": None,
        "inherited_physical_support": {
            "matter_M2_per_cell": 23,
            "mediator_M2_per_cell": 6,
            "reservoir_M2_per_active_source": 1,
            "maximum_matter_patch_plus_source_vertex_M2": 51,
            "field_coin_support_M2": 6,
            "field_stream_support_M2": 2,
        },
        "source_is_gravity_source": False,
        "occupation_is_energy": False,
    }
    check(
        "the calibration route preserves the Cycle-219 mass, Cycle-230 contact, and Cycle-313 source/stream deletion firewalls without renaming occupation as energy or a gravity source",
        abs(physical_mass - c313.c219.rest_mass(species)) < 4e-13
        and contact_firewall == 0
        and contact_number_commutator < c313.TOLERANCE
        and zero_response_norm < 1e-14
        and lawful_event_weight > 0.1
        and no_stream_neighbor_weight < 1e-15
        and emission_only_unitarity_residual > 0.1
        and matter_number_control_deletion_residual > 0.4
        and source_deleted_record is None
        and detail["calibrated_output_after_source_or_instrument_deletion"] is None
        and not detail["source_is_gravity_source"]
        and not detail["occupation_is_energy"],
        detail,
    )
    return detail


def lawful_domain_and_inventory_controls(
    fixture: c342.c338.RouteFixture,
) -> dict[str, object]:
    base = common_candidate(fixture, 1)
    invalid = (
        lambda: validate_route_fixture(4, c313.SOURCE, 1),
        lambda: validate_route_fixture(3, (3, 0, 0), 1),
        lambda: response_event(3, c313.SOURCE, 3, base.response.history_key),
        lambda: response_event(3, c313.SOURCE, 1, (0,) * (HISTORY_BITS - 1)),
        lambda: validate_common_code(fixture, replace(base, handshake=2)),
        lambda: validate_common_code(fixture, replace(base, clock_name="host clock")),
        lambda: calibrated_response_per_count(CalibrationBook((), 1), 0.0),
    )
    rejected = 0
    for call in invalid:
        try:
            call()
        except (TypeError, ValueError):
            rejected += 1

    inventory = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "upstream_clock": "Cycle342 conditional typed permanent complete-cylinder endpoint and Cycle22 named count",
        "upstream_response": "Cycle313 physical n=1/n=2 fixed-seam source/mediator common code",
        "supplied_clock_semantics": "occurrence, commit, fibre certificate, Record typing, permanence, endpoint 0, clock name, and spatial placement",
        "supplied_response_structure": "Q=1 reservoir preparation, n sector, source cell, six-M2 occupation instrument, and actual event predicate",
        "supplied_common_structure": "second complete-cylinder key, co-location, and the reversible equality/coincidence truth table",
        "supplied_calibration": "n=1 target convention and fitted positive calibration constant",
        "derived": "conditional Boolean common-key handshake, duplicate-event guard, append-only control Record, and externally evaluated response expectation per supplied named count",
        "not_derived": "autonomous preparation/instrument/outcome, universal calibration, NN handshake synthesis, interval, rate, time, energy, stress, gravity source or response",
        "common_product_register_M2_width": COMMON_CODE_BITS,
        "response_and_calibration_floats_encoded_in_common_word": False,
        "common_register_width_is_NN_support": False,
        "nearest_neighbour_handshake_support_M2": None,
        "kappa_is_energy": False,
        "wrapped_phase_is_energy": False,
        "generator_element_is_rate": False,
        "occupation_is_energy": False,
        "circuit_or_update_count_is_time": False,
        "calibrated_response_per_count_is_physical_rate": False,
        "physical_interval": None,
        "physical_rate": None,
        "physical_time": None,
        "negative_claim": None,
        "axiom_pressure": False,
    }
    check(
        "the lawful domain rejects malformed common codes and inventories every supplied semantic, preparation, instrument, calibration, and support boundary",
        rejected == len(invalid)
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset"
        and inventory["common_product_register_M2_width"] == 82
        and not inventory["response_and_calibration_floats_encoded_in_common_word"]
        and not inventory["common_register_width_is_NN_support"]
        and inventory["nearest_neighbour_handshake_support_M2"] is None
        and not inventory["kappa_is_energy"]
        and not inventory["wrapped_phase_is_energy"]
        and not inventory["generator_element_is_rate"]
        and not inventory["occupation_is_energy"]
        and not inventory["circuit_or_update_count_is_time"]
        and not inventory["calibrated_response_per_count_is_physical_rate"]
        and inventory["physical_interval"] is inventory["physical_rate"] is inventory["physical_time"] is None
        and inventory["negative_claim"] is None
        and not inventory["axiom_pressure"],
        {"lawful_domain_rejections": rejected, "inventory": inventory},
    )
    return {"lawful_domain_rejections": rejected, "inventory": inventory}


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 346 ROUTE 3: PHYSICAL CLOCK/RESPONSE COMMON-HISTORY CALIBRATION")
    print("authority=none; audit=unset")
    fixtures = {length: c342.c338.build_fixture(length) for length in ROUTE_LENGTHS}
    handshake = product_code_and_handshake_controls(fixtures)
    calibration = calibration_training_and_held_controls(fixtures)
    calibration_constant = float(
        calibration["training"]["fitted_calibration_constant"]
    )
    deletions = deletion_and_rescaling_controls(fixtures, calibration_constant)
    covariance = covariance_translation_and_held_controls(fixtures)
    firewalls = mass_contact_source_and_deletion_firewalls(fixtures[3])
    inventory = lawful_domain_and_inventory_controls(fixtures[3])
    check(
        "Route 3 conditionally gates one Cycle342 Record endpoint and one supplied Cycle313 response packet by a common key before host-side normalization, without promoting the result to physical time/rate",
        handshake["handshake_bit"] == 1
        and calibration["held"][-1]["L"] == 6
        and deletions["all_deleted_outputs_undefined_never_zero"]
        and covariance["common_history_failures"] == 0
        and firewalls["calibrated_output_after_source_or_instrument_deletion"] is None
        and inventory["inventory"]["physical_rate"] is None
        and inventory["inventory"]["physical_time"] is None,
        {
            "strongest_positive": "bounded Boolean common-key coincidence and conditional host-side response-expectation normalization",
            "conditional_on": "clock/response preparation, event, typing/permanence, handshake law, and calibration convention",
            "route_specific_open": "independent event provenance, encoded numerical response, nearest-neighbour handshake synthesis, and autonomous instrument/calibration law",
            "shared_obstruction": None,
            "axiom_pressure": False,
        },
    )
    print("DATA handshake", handshake)
    print("DATA calibration", calibration)
    print("DATA deletions", deletions)
    print("DATA covariance", covariance)
    print("DATA firewalls", firewalls)
    print("DATA inventory", inventory)
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_CLOCK_RESPONSE_COMMON_HISTORY_CALIBRATION_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_CLOCK_RESPONSE_COMMON_HISTORY_CALIBRATION_ROUTE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
