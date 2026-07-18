#!/usr/bin/env python3
"""Cycle 383: mixed-projective/refinement functionality Born bridge.

This runner joins the landed Cycle-321 coarse-effect/coarse-CP tournament to
Cycle-350/351's grade-blind 30+13 M2 registration grammar.  Explicit merge
maps quotient an unsplit scaled-ray outcome and its proportional two-piece
refinement to one registered coarse common state.  Resolution-indexed split
maps are sections, not a unique inverse: fine program/pointer labels remain
physically visible and must be supplied to reconstruct a presentation.

For the ray pair, effects, coarse CP maps, and system-only futures agree, so a
coarse-CP quotient is lawful.  For the axis pair, coarse effects agree but CP
maps and futures differ, so only an explicitly weaker effect quotient can
identify them.  Any deterministic numerical view whose only apparatus input
is the merged effect is representative-independent by exact input equality;
arbitrary nonlinear sums over visible fine components need not be.

The open PR-5479 comparator is not imported or treated as retained.  No coarse
equality is occurrence, Record identity, probability, a sampler, or a
frequency law.  Physical quotient selection, resolution/genesis, numerical-
view selection, actual history, and local tag compilation remain supplied or
open without no-go, minimum-content, obstruction, or axiom pressure.
Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from hashlib import sha256
from inspect import signature
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MIXED_PROJECTIVE_REFINEMENT_FUNCTIONALITY_BORN_BRIDGE_"
    "CYCLE383_NOTE_2026-07-18.md"
)

import physical_effect_equivalence_normalized_grade_cycle321_2026_07_18 as c321
import physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18 as c350


LENGTHS = (3, 6)
TRAIN_SIZES = (3, 6)
HELD_SIZE = 12
SIZES = TRAIN_SIZES + (HELD_SIZE,)
TAG_M2 = c350.ATOM_M2 - c350.RECORD_M2
TAG_SOURCE = "Cycle-383 supplied fine apparatus registration tag"
RESOLUTION_TO_PROGRAM = {
    "axis-left": 0,
    "axis-right": 1,
    "ray-unsplit": 2,
    "ray-refined": 3,
}
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8.0e-11
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
        check("the Cycle-383 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "landed cycle-321 coarse-cp refinement equivalence",
        "cycle-350/351 grade-blind 30+13 m2 registration",
        "merge map",
        "resolution-indexed split maps",
        "fine apparatus labels remain physically visible",
        "ray split/refinement pair",
        "axis same-effect separator",
        "effect-functional numerical view",
        "nonlinear fine-component sum separator",
        "all 24 proper-cubic frames",
        "held-out n=12",
        "fixed six-program carrier",
        "open pr #5479 is not imported",
        "coarse equality is not occurrence, record identity, or probability",
        "actual-history sampler: none",
        "frequency law: none",
        "shared substrate obstruction: none established",
        "no no-go, minimum-content theorem, or axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the lawful quotient, visible fine separators, registration boundary, and open functionality/genesis imports",
        not missing,
        missing,
    )
    return {"missing": missing}


MatrixKey = tuple[tuple[float, float], ...]


def matrix_key(matrix: np.ndarray) -> MatrixKey:
    array = np.asarray(matrix, dtype=complex)
    def canonical(value: float) -> float:
        rounded = round(float(value), 13)
        return 0.0 if rounded == 0.0 else rounded
    return tuple(
        (canonical(value.real), canonical(value.imag))
        for value in array.reshape(-1)
    )


def matrix_from_key(key: MatrixKey, shape: tuple[int, int]) -> np.ndarray:
    if len(key) != shape[0] * shape[1]:
        raise ValueError("matrix key has the wrong declared shape")
    return np.asarray([complex(real, imag) for real, imag in key]).reshape(shape)


@dataclass(frozen=True)
class FineTag:
    preparation: int
    program: int
    fine_pointer: int
    trial: int
    use: int
    pointer_event_registered: int = 1
    source: str = TAG_SOURCE


@dataclass(frozen=True)
class DecompositionAtom:
    record: c350.c342.CylinderRecord
    coarse_outcome: int
    fine_tags: tuple[FineTag, ...]


@dataclass(frozen=True)
class RegisteredPresentation:
    resolution: str
    atoms: tuple[DecompositionAtom, ...]


@dataclass(frozen=True)
class CoarseRegisteredAtom:
    record: c350.c342.CylinderRecord
    preparation: int
    trial: int
    use: int
    coarse_outcome: int
    effect: MatrixKey
    coarse_cp_choi: MatrixKey | None


@dataclass(frozen=True)
class CoarseRegisteredCorpus:
    quotient: str
    atoms: tuple[CoarseRegisteredAtom, ...]


@dataclass(frozen=True)
class NumericalView:
    corpus_hash: str
    functional: str | None
    values: tuple[float, ...] | None
    actual_history_sampler: None = None
    actual_member_selector: None = None


def validate_tag(tag: FineTag, programs: tuple[c321.Program, ...]) -> None:
    if not isinstance(tag, FineTag):
        raise TypeError("fine registration requires FineTag values")
    if (
        not isinstance(tag.preparation, int)
        or isinstance(tag.preparation, bool)
        or not 0 <= tag.preparation < 4
        or not isinstance(tag.program, int)
        or isinstance(tag.program, bool)
        or not 0 <= tag.program < len(programs)
        or not isinstance(tag.fine_pointer, int)
        or isinstance(tag.fine_pointer, bool)
        or not 0 <= tag.fine_pointer < len(programs[tag.program].kraus)
        or not isinstance(tag.trial, int)
        or isinstance(tag.trial, bool)
        or not 0 <= tag.trial < 16
        or tag.use not in (0, 1)
        or tag.pointer_event_registered != 1
        or tag.source != TAG_SOURCE
    ):
        raise ValueError("fine tag is outside the registered 13-M2 domain")


def tag_word(tag: FineTag, programs: tuple[c321.Program, ...]) -> tuple[int, ...]:
    validate_tag(tag, programs)
    word = (
        c350.bits(tag.preparation, c350.PREPARATION_M2)
        + c350.bits(tag.program, c350.PROGRAM_M2)
        + c350.bits(tag.fine_pointer, c350.FINE_POINTER_M2)
        + c350.bits(tag.trial, c350.TRIAL_M2)
        + (tag.use,)
    )
    if len(word) != TAG_M2:
        raise RuntimeError("fine registration tag inventory drifted")
    return word


def validate_presentation(
    fixture: c350.c338.RouteFixture,
    presentation: RegisteredPresentation,
    programs: tuple[c321.Program, ...],
) -> None:
    if not isinstance(presentation, RegisteredPresentation):
        raise TypeError("merge requires one RegisteredPresentation")
    if presentation.resolution not in RESOLUTION_TO_PROGRAM:
        raise ValueError("fine resolution is outside the declared menu")
    if not isinstance(presentation.atoms, tuple) or len(presentation.atoms) not in SIZES:
        raise ValueError("presentation size is outside train/held registration domain")
    program_index = RESOLUTION_TO_PROGRAM[presentation.resolution]
    program = programs[program_index]
    records = []
    for trial, atom in enumerate(presentation.atoms):
        if not isinstance(atom, DecompositionAtom) or not atom.fine_tags:
            raise TypeError("presentation requires decomposition atoms with visible fine tags")
        if not atom.record.typed or not atom.record.permanent:
            raise ValueError("every decomposition atom requires one typed permanent Record")
        if not 0 <= atom.coarse_outcome < len(program.coarse_groups):
            raise ValueError("coarse outcome is outside its program")
        pointers = tuple(tag.fine_pointer for tag in atom.fine_tags)
        if pointers != program.coarse_groups[atom.coarse_outcome]:
            raise ValueError("visible fine tags are not the complete declared coarse group")
        preparation, _scheduled_program, _pointer, use = c350.schedule_fields(trial)
        for tag in atom.fine_tags:
            validate_tag(tag, programs)
            if (
                tag.program != program_index
                or tag.preparation != preparation
                or tag.trial != trial
                or tag.use != use
            ):
                raise ValueError("fine tag disagrees with resolution or fixed registration fields")
        records.append(atom.record)
    if not c350.c342.valid_chain(fixture, tuple(records)):
        raise ValueError("presentation Records are outside the lawful Cycle-342 chain")


def build_presentation(
    fixture: c350.c338.RouteFixture,
    records: tuple[c350.c342.CylinderRecord, ...],
    resolution: str,
    programs: tuple[c321.Program, ...],
) -> RegisteredPresentation:
    if resolution not in RESOLUTION_TO_PROGRAM:
        raise ValueError("unknown supplied resolution")
    program_index = RESOLUTION_TO_PROGRAM[resolution]
    program = programs[program_index]
    atoms = []
    for trial, record in enumerate(records):
        preparation, _scheduled_program, _pointer, use = c350.schedule_fields(trial)
        outcome = trial % len(program.coarse_groups)
        tags = tuple(
            FineTag(preparation, program_index, pointer, trial, use)
            for pointer in program.coarse_groups[outcome]
        )
        atoms.append(DecompositionAtom(record, outcome, tags))
    presentation = RegisteredPresentation(resolution, tuple(atoms))
    validate_presentation(fixture, presentation, programs)
    return presentation


def presentation_records(
    fixture: c350.c338.RouteFixture,
    size: int,
    endpoint: int = 0,
) -> tuple[c350.c342.CylinderRecord, ...]:
    if size not in SIZES:
        raise ValueError("registration size is outside the finite campaign domain")
    cylinders = c350.c342.make_cylinder_chain(fixture, endpoint, size)
    return tuple(c350.c342.form_conditional_record(fixture, item) for item in cylinders)


def fine_registration_hash(
    presentation: RegisteredPresentation,
    programs: tuple[c321.Program, ...],
) -> str:
    payload = bytearray()
    payload.extend(presentation.resolution.encode("utf-8"))
    for atom in presentation.atoms:
        payload.extend(c350.c342.record_word(atom.record))
        payload.append(atom.coarse_outcome)
        payload.append(len(atom.fine_tags))
        for tag in atom.fine_tags:
            payload.extend(tag_word(tag, programs))
    return sha256(bytes(payload)).hexdigest()


def merge_presentation(
    fixture: c350.c338.RouteFixture,
    presentation: RegisteredPresentation,
    programs: tuple[c321.Program, ...],
    quotient: str,
) -> CoarseRegisteredCorpus:
    """E/Q: forget visible fine labels only under an explicit quotient level."""

    validate_presentation(fixture, presentation, programs)
    if quotient not in ("effect", "coarse_cp"):
        raise ValueError("quotient must be effect or coarse_cp")
    program = programs[RESOLUTION_TO_PROGRAM[presentation.resolution]]
    atoms = []
    for atom in presentation.atoms:
        pointers = tuple(tag.fine_pointer for tag in atom.fine_tags)
        effect = sum(
            (program.fine_effects[pointer] for pointer in pointers),
            start=np.zeros((2, 2), dtype=complex),
        )
        grouped = tuple(program.kraus[pointer] for pointer in pointers)
        tags = atom.fine_tags
        atoms.append(
            CoarseRegisteredAtom(
                atom.record,
                tags[0].preparation,
                tags[0].trial,
                tags[0].use,
                atom.coarse_outcome,
                matrix_key(effect),
                matrix_key(c321.choi(grouped)) if quotient == "coarse_cp" else None,
            )
        )
    common = CoarseRegisteredCorpus(quotient, tuple(atoms))
    validate_common(fixture, common)
    return common


def validate_common(
    fixture: c350.c338.RouteFixture,
    common: CoarseRegisteredCorpus,
) -> None:
    if not isinstance(common, CoarseRegisteredCorpus) or common.quotient not in ("effect", "coarse_cp"):
        raise TypeError("common state requires one declared quotient level")
    if not isinstance(common.atoms, tuple) or len(common.atoms) not in SIZES:
        raise ValueError("common corpus has the wrong finite size")
    records = []
    for trial, atom in enumerate(common.atoms):
        if not isinstance(atom, CoarseRegisteredAtom):
            raise TypeError("common corpus contains a non-coarse atom")
        preparation, _program, _pointer, use = c350.schedule_fields(trial)
        if (
            not atom.record.typed
            or not atom.record.permanent
            or atom.trial != trial
            or atom.preparation != preparation
            or atom.use != use
            or atom.coarse_outcome not in (0, 1, 2)
            or len(atom.effect) != 4
            or (common.quotient == "effect" and atom.coarse_cp_choi is not None)
            or (common.quotient == "coarse_cp" and (atom.coarse_cp_choi is None or len(atom.coarse_cp_choi) != 16))
        ):
            raise ValueError("coarse registered atom is outside its declared quotient code")
        records.append(atom.record)
    if not c350.c342.valid_chain(fixture, tuple(records)):
        raise ValueError("common corpus Record chain is unlawful")


def split_common(
    fixture: c350.c338.RouteFixture,
    common: CoarseRegisteredCorpus,
    resolution: str | None,
    programs: tuple[c321.Program, ...],
) -> RegisteredPresentation:
    """D_resolution: a supplied section; there is no resolution-free inverse."""

    validate_common(fixture, common)
    if resolution is None or resolution not in RESOLUTION_TO_PROGRAM:
        raise ValueError("fine reconstruction requires one supplied resolution")
    candidate = build_presentation(
        fixture,
        tuple(atom.record for atom in common.atoms),
        resolution,
        programs,
    )
    if merge_presentation(fixture, candidate, programs, common.quotient) != common:
        raise ValueError("supplied resolution is not a section of this quotient state")
    return candidate


def coarse_corpus_hash(common: CoarseRegisteredCorpus) -> str:
    payload = repr(common).encode("utf-8")
    return sha256(payload).hexdigest()


def supplied_functional(name: str):
    functions = {
        "trace-labelled": c350.born_trace_grade,
        "nonlinear comparison": c350.nonlinear_grade,
        "spectral maximum": lambda effect, _preparation: float(np.max(np.linalg.eigvalsh(effect))),
    }
    if name not in functions:
        raise ValueError("effect functional is outside the supplied comparison menu")
    return functions[name]


def effect_functional_view(
    common: CoarseRegisteredCorpus,
    name: str | None,
) -> NumericalView:
    digest = coarse_corpus_hash(common)
    if name is None:
        return NumericalView(digest, None, None)
    functional = supplied_functional(name)
    values = tuple(
        float(functional(matrix_from_key(atom.effect, (2, 2)), atom.preparation))
        for atom in common.atoms
    )
    return NumericalView(digest, name, values)


def fine_component_sum_view(
    presentation: RegisteredPresentation,
    programs: tuple[c321.Program, ...],
    name: str,
) -> tuple[float, ...]:
    functional = supplied_functional(name)
    program = programs[RESOLUTION_TO_PROGRAM[presentation.resolution]]
    return tuple(
        sum(
            float(functional(program.fine_effects[tag.fine_pointer], tag.preparation))
            for tag in atom.fine_tags
        )
        for atom in presentation.atoms
    )


def ray_quotient_section_controls() -> dict[str, object]:
    fixture = c350.c338.build_fixture(3)
    programs = c350.c323.make_programs(c350.c317.physical_fixture(3).contact)
    records = presentation_records(fixture, 6)
    unsplit = build_presentation(fixture, records, "ray-unsplit", programs)
    refined = build_presentation(fixture, records, "ray-refined", programs)
    left = merge_presentation(fixture, unsplit, programs, "coarse_cp")
    right = merge_presentation(fixture, refined, programs, "coarse_cp")
    left_section = split_common(fixture, left, "ray-unsplit", programs)
    right_section = split_common(fixture, left, "ray-refined", programs)
    effect_residual = max(
        np.linalg.norm(
            matrix_from_key(a.effect, (2, 2)) - matrix_from_key(b.effect, (2, 2))
        )
        for a, b in zip(left.atoms, right.atoms)
    )
    cp_residual = max(
        np.linalg.norm(
            matrix_from_key(a.coarse_cp_choi or (), (4, 4))
            - matrix_from_key(b.coarse_cp_choi or (), (4, 4))
        )
        for a, b in zip(left.atoms, right.atoms)
    )
    detail = {
        "coarse_common_states_equal": left == right,
        "merge_split_unsplit_identity": merge_presentation(fixture, left_section, programs, "coarse_cp") == left,
        "merge_split_refined_identity": merge_presentation(fixture, right_section, programs, "coarse_cp") == left,
        "split_merge_unsplit_identity": left_section == unsplit,
        "split_merge_refined_identity": right_section == refined,
        "coarse_effect_residual": float(effect_residual),
        "coarse_CP_Choi_residual": float(cp_residual),
        "fine_registration_hash_equal": fine_registration_hash(unsplit, programs) == fine_registration_hash(refined, programs),
        "fine_transcript_Choi_residual": float(
            np.linalg.norm(
                c321.transcript_choi(programs[2].fine_effects)
                - c321.transcript_choi(programs[3].fine_effects)
            )
        ),
        "fine_tag_words_unsplit": sum(len(atom.fine_tags) for atom in unsplit.atoms),
        "fine_tag_words_refined": sum(len(atom.fine_tags) for atom in refined.atoms),
        "resolution_free_inverse": None,
    }
    check(
        "the landed ray proportional refinement admits exact merge and resolution-indexed split sections while fine registrations remain visible",
        detail["coarse_common_states_equal"]
        and detail["merge_split_unsplit_identity"]
        and detail["merge_split_refined_identity"]
        and detail["split_merge_unsplit_identity"]
        and detail["split_merge_refined_identity"]
        and effect_residual == cp_residual == 0.0
        and not detail["fine_registration_hash_equal"]
        and detail["fine_transcript_Choi_residual"] > 0.3
        and detail["fine_tag_words_refined"] > detail["fine_tag_words_unsplit"]
        and detail["resolution_free_inverse"] is None,
        detail,
    )
    return detail


def effect_functionality_and_axis_separator_controls() -> dict[str, object]:
    fixture = c350.c338.build_fixture(3)
    programs = c350.c323.make_programs(c350.c317.physical_fixture(3).contact)
    records = presentation_records(fixture, 6)
    ray_left = build_presentation(fixture, records, "ray-unsplit", programs)
    ray_right = build_presentation(fixture, records, "ray-refined", programs)
    ray_common_left = merge_presentation(fixture, ray_left, programs, "coarse_cp")
    ray_common_right = merge_presentation(fixture, ray_right, programs, "coarse_cp")
    functionals = ("trace-labelled", "nonlinear comparison", "spectral maximum")
    view_rows = {
        name: effect_functional_view(ray_common_left, name) == effect_functional_view(ray_common_right, name)
        for name in functionals
    }
    nonlinear_left = fine_component_sum_view(ray_left, programs, "nonlinear comparison")
    nonlinear_right = fine_component_sum_view(ray_right, programs, "nonlinear comparison")
    trace_left = fine_component_sum_view(ray_left, programs, "trace-labelled")
    trace_right = fine_component_sum_view(ray_right, programs, "trace-labelled")
    nonlinear_delta = max(abs(a - b) for a, b in zip(nonlinear_left, nonlinear_right))
    trace_delta = max(abs(a - b) for a, b in zip(trace_left, trace_right))

    axis_left = build_presentation(fixture, records, "axis-left", programs)
    axis_right = build_presentation(fixture, records, "axis-right", programs)
    axis_effect_left = merge_presentation(fixture, axis_left, programs, "effect")
    axis_effect_right = merge_presentation(fixture, axis_right, programs, "effect")
    axis_cp_left = merge_presentation(fixture, axis_left, programs, "coarse_cp")
    axis_cp_right = merge_presentation(fixture, axis_right, programs, "coarse_cp")
    axis_cp_residual = max(
        np.linalg.norm(
            matrix_from_key(a.coarse_cp_choi or (), (4, 4))
            - matrix_from_key(b.coarse_cp_choi or (), (4, 4))
        )
        for a, b in zip(axis_cp_left.atoms, axis_cp_right.atoms)
    )
    axis_future = c321.future_process_witness(
        c321.grouped_kraus(programs[0], 0), c321.grouped_kraus(programs[1], 0)
    )
    detail = {
        "effect_functional_view_equal_by_name": view_rows,
        "effect_functional_parameters": tuple(signature(c350.born_trace_grade).parameters),
        "ray_nonlinear_fine_sum_maximum_delta": nonlinear_delta,
        "ray_trace_fine_sum_maximum_delta": trace_delta,
        "axis_effect_quotient_equal": axis_effect_left == axis_effect_right,
        "axis_coarse_CP_quotient_equal": axis_cp_left == axis_cp_right,
        "axis_coarse_CP_Choi_residual": float(axis_cp_residual),
        "axis_held_future_witness": float(axis_future),
        "selected_numerical_functional": None,
        "effect_functional_view_is_probability": False,
    }
    check(
        "effect-functional views factor through the merged effect, while nonlinear fine sums and same-effect process separators retain the premise boundary",
        all(view_rows.values())
        and detail["effect_functional_parameters"] == ("effect", "preparation")
        and nonlinear_delta > 1e-4
        and trace_delta < TOL
        and detail["axis_effect_quotient_equal"]
        and not detail["axis_coarse_CP_quotient_equal"]
        and axis_cp_residual > 0.4
        and axis_future > 0.1
        and detail["selected_numerical_functional"] is None
        and detail["effect_functional_view_is_probability"] is False,
        detail,
    )
    return detail


def rotate_record(
    record: c350.c342.CylinderRecord,
    mapping,
) -> c350.c342.CylinderRecord:
    cylinder = record.cylinder
    return c350.c342.CylinderRecord(
        c350.c338.FutureCylinder(
            endpoint=cylinder.endpoint,
            candidate=cylinder.candidate,
            phase=cylinder.phase,
            future_pre=int(mapping[cylinder.future_pre]),
            future_post=int(mapping[cylinder.future_post]),
        ),
        record.typed,
        record.permanent,
    )


def frame_size_held_controls() -> dict[str, object]:
    programs = c350.c323.make_programs(c350.c317.physical_fixture(3).contact)
    frames = c350.c311.c235.proper_cubic_frames()
    cases = held_cases = atom_cases = 0
    mapping_failures = quotient_failures = section_failures = 0
    view_failures = tag_visibility_failures = record_mapping_failures = 0
    rows = []
    for length in LENGTHS:
        fixture = c350.c338.build_fixture(length)
        base_records = {size: presentation_records(fixture, size) for size in SIZES}
        for size in SIZES:
            for frame in frames:
                rotated_fixture, mapping, failures = c350.c342.mapped_fixture(fixture, frame)
                mapping_failures += failures
                records = presentation_records(rotated_fixture, size)
                expected = tuple(rotate_record(record, mapping) for record in base_records[size])
                record_mapping_failures += int(
                    tuple(c350.c342.record_word(record) for record in records)
                    != tuple(c350.c342.record_word(record) for record in expected)
                )
                unsplit = build_presentation(rotated_fixture, records, "ray-unsplit", programs)
                refined = build_presentation(rotated_fixture, records, "ray-refined", programs)
                left = merge_presentation(rotated_fixture, unsplit, programs, "coarse_cp")
                right = merge_presentation(rotated_fixture, refined, programs, "coarse_cp")
                quotient_failures += int(left != right)
                section_failures += int(
                    split_common(rotated_fixture, left, "ray-unsplit", programs) != unsplit
                    or split_common(rotated_fixture, left, "ray-refined", programs) != refined
                )
                for name in ("trace-labelled", "nonlinear comparison", "spectral maximum"):
                    view_failures += int(
                        effect_functional_view(left, name) != effect_functional_view(right, name)
                    )
                tag_visibility_failures += int(
                    fine_registration_hash(unsplit, programs) == fine_registration_hash(refined, programs)
                )
                atom_cases += size
                cases += 1
                held_cases += int(length == 6 and size == HELD_SIZE)
            rows.append(
                {
                    "L": length,
                    "N": size,
                    "train": size in TRAIN_SIZES,
                    "held": length == 6 and size == HELD_SIZE,
                    "frames": len(frames),
                }
            )
    failures = (
        mapping_failures
        + quotient_failures
        + section_failures
        + view_failures
        + tag_visibility_failures
        + record_mapping_failures
    )
    detail = {
        "rows": rows,
        "L_by_N_by_frame_cases": cases,
        "registered_atom_cases": atom_cases,
        "held_L6_N12_frame_cases": held_cases,
        "proper_cubic_frames": len(frames),
        "payload_mapping_failures": mapping_failures + record_mapping_failures,
        "coarse_CP_quotient_failures": quotient_failures,
        "resolution_section_failures": section_failures,
        "effect_functional_view_failures": view_failures,
        "fine_tag_visibility_failures": tag_visibility_failures,
    }
    check(
        "ray quotient/sections and effect-functional views are exact at L3/L6 N3/N6/held-N12 in all 24 frames while fine tags remain visible",
        cases == len(LENGTHS) * len(SIZES) * 24
        and atom_cases == len(LENGTHS) * sum(SIZES) * 24
        and held_cases == 24
        and failures == 0,
        detail,
    )
    return {"failures": failures, **detail}


def fixed_carrier_controls() -> dict[str, object]:
    with redirect_stdout(StringIO()):
        c350.c323.PASS = c350.c323.FAIL = 0
        fixtures = c350.c323.physical_fixture_controls()
        programs = c350.c323.make_programs(fixtures[3].contact)
        carrier = c350.c323.FixedProgramCarrier(programs)
        ray, axis = c350.c323.two_use_equivalence_controls(programs)
        covariance = c350.c323.covariance_controls(fixtures, carrier)
        inherited_failures = c350.c323.FAIL
    detail = {
        "fixed_carrier_programs": len(programs),
        "proper_cubic_frames": covariance["frames"],
        "carrier_branch_failures": covariance["branch_failures"],
        "maximum_one_use_carrier_residual": covariance["maximum_one_use_carrier_residual"],
        "maximum_two_use_carrier_residual": covariance["maximum_two_use_carrier_residual"],
        "ray_two_use_coarse_effect_residual": ray["two_use_coarse_effect_residual"],
        "ray_two_use_coarse_CP_residual": ray["two_use_coarse_instrument_Choi_residual"],
        "ray_two_use_fine_transcript_residual": ray["two_use_fine_transcript_Choi_residual"],
        "axis_two_use_coarse_CP_residual": axis["two_use_coarse_instrument_Choi_residual"],
        "axis_two_use_future_witness": axis["two_use_held_future_witness"],
        "inherited_fixed_carrier_control_failures": inherited_failures,
    }
    check(
        "the fixed six-program carrier preserves the ray coarse-CP quotient and axis separator under all frames while fine transcripts remain visible",
        detail["fixed_carrier_programs"] == 6
        and detail["proper_cubic_frames"] == 24
        and detail["carrier_branch_failures"] == 0
        and detail["maximum_one_use_carrier_residual"] < c350.TOL
        and detail["maximum_two_use_carrier_residual"] < c350.TOL
        and detail["ray_two_use_coarse_effect_residual"] < TOL
        and detail["ray_two_use_coarse_CP_residual"] < TOL
        and detail["ray_two_use_fine_transcript_residual"] > 0.9
        and detail["axis_two_use_coarse_CP_residual"] > 0.2
        and detail["axis_two_use_future_witness"] > 0.3
        and inherited_failures == 0,
        detail,
    )
    return detail


def deletion_leakage_domain_and_record_separator_controls() -> dict[str, object]:
    fixture = c350.c338.build_fixture(3)
    programs = c350.c323.make_programs(c350.c317.physical_fixture(3).contact)
    records = presentation_records(fixture, 6)
    alternative_records = presentation_records(fixture, 6, endpoint=1)
    refined = build_presentation(fixture, records, "ray-refined", programs)
    common = merge_presentation(fixture, refined, programs, "coarse_cp")
    alternative = merge_presentation(
        fixture,
        build_presentation(fixture, alternative_records, "ray-refined", programs),
        programs,
        "coarse_cp",
    )
    before_hash = coarse_corpus_hash(common)
    deleted_view = effect_functional_view(common, None)
    after_hash = coarse_corpus_hash(common)

    split_deleted = replace(
        refined,
        atoms=(replace(refined.atoms[0], fine_tags=refined.atoms[0].fine_tags[:1]),)
        + refined.atoms[1:],
    )
    registration_deleted = replace(
        refined,
        atoms=(
            replace(
                refined.atoms[0],
                fine_tags=(replace(refined.atoms[0].fine_tags[0], pointer_event_registered=0),)
                + refined.atoms[0].fine_tags[1:],
            ),
        )
        + refined.atoms[1:],
    )
    pointer_spliced = replace(
        refined,
        atoms=(
            replace(
                refined.atoms[0],
                fine_tags=(replace(refined.atoms[0].fine_tags[0], fine_pointer=2),)
                + refined.atoms[0].fine_tags[1:],
            ),
        )
        + refined.atoms[1:],
    )
    tampered_common = replace(
        common,
        atoms=(replace(common.atoms[0], effect=((9.0, 0.0),) * 4),) + common.atoms[1:],
    )
    invalid_calls = (
        lambda: merge_presentation(fixture, split_deleted, programs, "coarse_cp"),
        lambda: merge_presentation(fixture, registration_deleted, programs, "coarse_cp"),
        lambda: merge_presentation(fixture, pointer_spliced, programs, "coarse_cp"),
        lambda: validate_presentation(fixture, replace(refined, atoms=refined.atoms[:-1]), programs),
        lambda: split_common(fixture, common, None, programs),
        lambda: split_common(fixture, tampered_common, "ray-refined", programs),
        lambda: split_common(fixture, common, "axis-left", programs),
        lambda: merge_presentation(fixture, refined, programs, "selected Born quotient"),
        lambda: supplied_functional("selected probability law"),
    )
    rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            rejections += 1

    common_fields = set(CoarseRegisteredAtom.__dataclass_fields__)
    detail = {
        "same_effect_different_Record_common_states_equal": common == alternative,
        "same_effect_different_Record_hashes_equal": coarse_corpus_hash(common) == coarse_corpus_hash(alternative),
        "coarse_hash_before_deleted_view": before_hash,
        "coarse_hash_after_deleted_view": after_hash,
        "deleted_numerical_view_values": deleted_view.values,
        "deleted_view_sampler": deleted_view.actual_history_sampler,
        "deleted_view_actual_member": deleted_view.actual_member_selector,
        "domain_rejections": rejections,
        "domain_attempts": len(invalid_calls),
        "common_atom_fields": tuple(sorted(common_fields)),
        "program_or_fine_pointer_in_common_atom": bool(common_fields.intersection({"program", "fine_pointer", "fine_tags"})),
        "Record_words_preserved_across_ray_presentations": tuple(
            c350.c342.record_word(atom.record) for atom in refined.atoms
        )
        == tuple(c350.c342.record_word(atom.record) for atom in split_common(fixture, common, "ray-unsplit", programs).atoms),
        "whole_expanded_presentation_atom_is_Record": False,
        "Record_M2": c350.RECORD_M2,
        "each_fine_tag_M2": TAG_M2,
    }
    check(
        "fine/tag/resolution deletion and malformed quotients reject; numerical-view deletion preserves the common state and equal effects never merge different Records",
        detail["same_effect_different_Record_common_states_equal"] is False
        and detail["same_effect_different_Record_hashes_equal"] is False
        and before_hash == after_hash == deleted_view.corpus_hash
        and deleted_view.values is None
        and deleted_view.actual_history_sampler is None
        and deleted_view.actual_member_selector is None
        and rejections == len(invalid_calls)
        and not detail["program_or_fine_pointer_in_common_atom"]
        and detail["Record_words_preserved_across_ray_presentations"]
        and detail["whole_expanded_presentation_atom_is_Record"] is False
        and (detail["Record_M2"], detail["each_fine_tag_M2"]) == (30, 13),
        detail,
    )
    return detail


def supplied_structure_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded conditional registered refinement/functionality quotient bridge",
        "retained_input": "landed Cycle-321 proportional ray refinement/coarse-CP equivalence",
        "open_PR_5479_comparator_imported": False,
        "open_PR_5479_treated_as_retained": False,
        "registration": "Cycle-350/351 grade-blind typed 30-M2 Record plus supplied 13-M2 fine apparatus tags",
        "fixed_carrier": "supplied Cycle-323 six-program three-M2 program carrier and fresh three-M2 pointers",
        "merge_map": "explicit representative -> coarse registered effect/optional CP quotient",
        "split_maps": "resolution-indexed supplied sections; no unique resolution-free inverse",
        "ray_quotient": "coarse CP, coarse effect, pointer-erased system future",
        "axis_quotient": "effect only; coarse CP and future remain distinct",
        "fine_labels_visible": True,
        "quotient_rule_selected_by_framework": False,
        "resolution_genesis": None,
        "physical_functionality_comparator": None,
        "physical_tag_genesis_and_binding_compiler": None,
        "effect_functional_views": "optional supplied deterministic functions of merged effect and preparation only",
        "selected_numerical_functional": None,
        "coarse_equality_is_occurrence": False,
        "coarse_equality_is_Record_identity": False,
        "coarse_equality_is_probability": False,
        "fine_component_is_occurrence": False,
        "actual_history_sampler": None,
        "actual_member_selector": None,
        "frequency_law": None,
        "Born_law_derived": False,
        "implementation_or_law_incompleteness": (
            "physical quotient selection/comparator, resolution genesis, tag compiler, numerical-view selection, actuality and frequency remain open"
        ),
        "shared_substrate_obstruction": None,
        "no_go": None,
        "minimum_content": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the supplied quotient/resolution/registration inventory is exact without importing the open comparator or promoting equality to actuality/statistics",
        inventory["open_PR_5479_comparator_imported"] is False
        and inventory["open_PR_5479_treated_as_retained"] is False
        and inventory["fine_labels_visible"]
        and inventory["quotient_rule_selected_by_framework"] is False
        and inventory["resolution_genesis"] is None
        and inventory["physical_functionality_comparator"] is None
        and inventory["physical_tag_genesis_and_binding_compiler"] is None
        and inventory["selected_numerical_functional"] is None
        and inventory["coarse_equality_is_occurrence"] is False
        and inventory["coarse_equality_is_Record_identity"] is False
        and inventory["coarse_equality_is_probability"] is False
        and inventory["fine_component_is_occurrence"] is False
        and inventory["actual_history_sampler"] is None
        and inventory["actual_member_selector"] is None
        and inventory["frequency_law"] is None
        and inventory["Born_law_derived"] is False
        and inventory["shared_substrate_obstruction"] is None
        and inventory["no_go"] is inventory["minimum_content"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 383: MIXED-PROJECTIVE / REFINEMENT-FUNCTIONALITY BORN BRIDGE")
    print("authority=none; audit=unset; open PR comparator unimported")
    note = note_contract()
    quotient = ray_quotient_section_controls()
    functionality = effect_functionality_and_axis_separator_controls()
    frames = frame_size_held_controls()
    carrier = fixed_carrier_controls()
    attacks = deletion_leakage_domain_and_record_separator_controls()
    inventory = supplied_structure_and_semantic_controls()
    check(
        "Cycle 383 constructs a finite registered coarse-CP refinement quotient and exact effect-functional factorization while leaving physical functionality/genesis open",
        not note["missing"]
        and quotient["coarse_common_states_equal"]
        and all(functionality["effect_functional_view_equal_by_name"].values())
        and frames["failures"] == 0
        and carrier["carrier_branch_failures"] == 0
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and inventory["physical_functionality_comparator"] is None
        and inventory["shared_substrate_obstruction"] is None,
        {
            "disposition": "bounded positive conditional registered refinement quotient",
            "strongest_positive": "ray coarse-CP common state plus resolution-indexed sections and representative-independent effect-functional views",
            "separator": "axis same-effect programs remain CP/future distinct; fine ray tags remain visible",
            "open_physical_residual": "quotient selection/comparator, resolution/tag genesis, numerical selection, actuality/frequency",
            "shared_obstruction": None,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_MIXED_PROJECTIVE_REFINEMENT_FUNCTIONALITY_BORN_BRIDGE_OPEN")
        return 1
    print("RESULT PHYSICAL_MIXED_PROJECTIVE_REFINEMENT_FUNCTIONALITY_BORN_BRIDGE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
