#!/usr/bin/env python3
"""Cycle 371: conditional Cycle-366 convergence-Record -> Cycle-351 corpus bridge.

The code space contains only post-CONSUME Cycle-366 convergence Records and
one supplied site/payload-bound 13-M2 Cycle-351 apparatus tag per Record.
Three precommit carriers and the reversible formed transcript are neither
Records nor corpus trials.  On that declared code space the exact finite maps

    E : ThresholdCommonState x explicit embedding -> tuple[CorpusAtom],
    D E = identity,
    O_common = O_Cycle351 E,
    W_proposal,common = W_proposal,Cycle351 E

are tested at L3/L6, N3/N6/N12, and all 24 proper-cubic frames.

Cycle 366 and its threshold value three are supplied, unselected candidate-law
content.  Its reversible X/CNOT/Toffoli calculation does not supply the
nonunitary CONSUME admission, the 13-M2 tag genesis, or a physical 30+13 NN
binding compiler.  Optional numerical weights are downstream proposal views;
they do not enter thresholding, commit, extraction, or E.  No rule, sampler,
actual member, frequency theorem, Born law, physical tag compiler, or no-go is
selected.  Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from hashlib import sha256
from inspect import getsource, signature
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_BORN_CORPUS_ADAPTER_"
    "CYCLE371_NOTE_2026-07-18.md"
)

import physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18 as c350
import physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18 as c366


Coord = c366.Coord
Word = c366.Word
LENGTHS = (3, 6)
TRAIN_SIZES = (3, 6)
HELD_SIZE = 12
SIZES = TRAIN_SIZES + (HELD_SIZE,)
TAG_M2 = c350.ATOM_M2 - c350.RECORD_M2
TAG_SOURCE = "Cycle-371 supplied convergence-site/payload-bound Cycle-351 apparatus tag"
AUTHORITY = "none"
AUDIT = "unset"
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
        check("the Cycle-371 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "post-consume logical record",
        "three precommit carriers are not records or three trials",
        "d e = identity",
        "all 24 proper-cubic frames",
        "train sizes n=3 and n=6",
        "held-out size n=12",
        "proposal weights never determine the threshold or commit",
        "physical tag-genesis compiler: none",
        "physical nearest-neighbor 30+13 binding compiler: none",
        "consume admission by existing framework law: none",
        "cycle 366 is not selected",
        "born rule is not selected",
        "actual-history sampler: none",
        "actual-member selector: none",
        "shared substrate obstruction: none established",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the post-commit code space, exact maps, supplied law content, and open physical residuals",
        not missing,
        missing,
    )
    return {"missing": missing}


@dataclass(frozen=True)
class RegisteredConvergenceTag:
    site: Coord
    payload: Word
    preparation: int
    program: int
    fine_pointer: int
    trial: int
    use: int
    pointer_event_registered: int = 1
    source: str = TAG_SOURCE


@dataclass(frozen=True)
class ThresholdCommonState:
    records: tuple[c366.ThresholdSiteContentRecord, ...]
    tags: tuple[RegisteredConvergenceTag, ...]


@dataclass(frozen=True)
class CorpusEmbedding:
    ordered_sites: tuple[Coord, ...]


@dataclass(frozen=True)
class ProposalWeightView:
    corpus_hash: str
    proposal_rule: str | None
    weights: tuple[float, ...] | None
    actual_history_sampler: None = None
    actual_member_selector: None = None


def valid_coord(site: Coord) -> bool:
    return (
        isinstance(site, tuple)
        and len(site) == 3
        and all(isinstance(value, int) and not isinstance(value, bool) for value in site)
    )


def validate_tag(tag: RegisteredConvergenceTag) -> None:
    if not isinstance(tag, RegisteredConvergenceTag):
        raise TypeError("bridge requires one RegisteredConvergenceTag")
    if (
        not valid_coord(tag.site)
        or not isinstance(tag.payload, tuple)
        or len(tag.payload) != c350.RECORD_M2
        or any(bit not in (0, 1) for bit in tag.payload)
        or not isinstance(tag.preparation, int)
        or isinstance(tag.preparation, bool)
        or not 0 <= tag.preparation < 4
        or not isinstance(tag.program, int)
        or isinstance(tag.program, bool)
        or not 0 <= tag.program < c350.c323.LAWFUL_PROGRAMS
        or not isinstance(tag.fine_pointer, int)
        or isinstance(tag.fine_pointer, bool)
        or not 0 <= tag.fine_pointer < c350.PROGRAM_FINE_LABELS[tag.program]
        or not isinstance(tag.trial, int)
        or isinstance(tag.trial, bool)
        or not 0 <= tag.trial < 16
        or tag.use not in (0, 1)
        or tag.pointer_event_registered != 1
        or tag.source != TAG_SOURCE
    ):
        raise ValueError("registered convergence tag is outside its exact 13-M2 domain")


def scheduled_tag(site: Coord, payload: Word, trial: int) -> RegisteredConvergenceTag:
    preparation, program, fine_pointer, use = c350.schedule_fields(trial)
    return RegisteredConvergenceTag(
        site, payload, preparation, program, fine_pointer, trial, use
    )


def tag_word(tag: RegisteredConvergenceTag) -> Word:
    validate_tag(tag)
    word = (
        c350.bits(tag.preparation, c350.PREPARATION_M2)
        + c350.bits(tag.program, c350.PROGRAM_M2)
        + c350.bits(tag.fine_pointer, c350.FINE_POINTER_M2)
        + c350.bits(tag.trial, c350.TRIAL_M2)
        + (tag.use,)
    )
    if len(word) != TAG_M2:
        raise RuntimeError("13-M2 tag inventory drifted")
    return word


def validate_common_state(
    fixture: c366.c364.c342.c338.RouteFixture,
    common: ThresholdCommonState,
) -> None:
    if not isinstance(common, ThresholdCommonState):
        raise TypeError("encoder requires one ThresholdCommonState")
    if not isinstance(common.records, tuple) or not common.records:
        raise ValueError("common code space requires post-CONSUME logical Records")
    if not isinstance(common.tags, tuple) or len(common.tags) != len(common.records):
        raise ValueError("every and only convergence Record requires one tag")
    if len({record.site for record in common.records}) != len(common.records):
        raise ValueError("convergence Record sites alias")
    if len({tag.site for tag in common.tags}) != len(common.tags):
        raise ValueError("registered tag sites alias")
    if len({tag.trial for tag in common.tags}) != len(common.tags):
        raise ValueError("registered trial fields alias")
    for trial, (record, tag) in enumerate(zip(common.records, common.tags)):
        validate_tag(tag)
        decoded = c366.c364.c342.decode_record_word(record.content)
        if (
            not isinstance(record, c366.ThresholdSiteContentRecord)
            or not valid_coord(record.site)
            or record.predecessors != ()
            or record.record_type != c366.RECORD_TYPE
            or record.law != c366.LAW_NAME
            or not record.permanent_under_candidate_law
            or not decoded.typed
            or not decoded.permanent
            or not c366.c364.c342.cylinder_is_lawful(fixture, decoded.cylinder)
            or tag.site != record.site
            or tag.payload != record.content
            or tag.trial != trial
            or (
                tag.preparation,
                tag.program,
                tag.fine_pointer,
                tag.use,
            )
            != c350.schedule_fields(trial)
        ):
            raise ValueError("common state is outside the post-CONSUME fixed-corpus code space")
    if not c366.c364.c342.valid_chain(
        fixture,
        tuple(c366.c364.c342.decode_record_word(record.content) for record in common.records),
    ):
        raise ValueError("convergence Record payloads are not one lawful Cycle-351 chain")


def extract_common_state(
    fixture: c366.c364.c342.c338.RouteFixture,
    physical: c366.BasisState,
    tags: tuple[RegisteredConvergenceTag, ...],
) -> ThresholdCommonState:
    """Extract only post-CONSUME Records; carrier/transcript registers are absent."""

    c366.validate_basis(physical)
    if c366.workspace_leakage(physical) != 0:
        raise ValueError("reversible workspace must be clean at common-state extraction")
    records = c366.logical_records(physical)
    if not records:
        raise ValueError("precommit or subthreshold carriers are not corpus Records")
    common = ThresholdCommonState(records, tags)
    validate_common_state(fixture, common)
    return common


def validate_embedding(common: ThresholdCommonState, embedding: CorpusEmbedding) -> None:
    if not isinstance(embedding, CorpusEmbedding) or not isinstance(embedding.ordered_sites, tuple):
        raise TypeError("bridge requires one explicit ordered-site embedding")
    if (
        embedding.ordered_sites != tuple(record.site for record in common.records)
        or len(set(embedding.ordered_sites)) != len(embedding.ordered_sites)
    ):
        raise ValueError("embedding must preserve the exact common-state order")


def encode_typed_corpus(
    fixture: c366.c364.c342.c338.RouteFixture,
    common: ThresholdCommonState,
    embedding: CorpusEmbedding,
) -> tuple[c350.CorpusAtom, ...]:
    """E: exact threshold-, weight-, and sampler-blind 30+13 encoder."""

    validate_common_state(fixture, common)
    validate_embedding(common, embedding)
    atoms = []
    for record, tag in zip(common.records, common.tags):
        atom = c350.CorpusAtom(
            c366.c364.c342.decode_record_word(record.content),
            tag.preparation,
            tag.program,
            tag.fine_pointer,
            tag.trial,
            tag.use,
        )
        word = c350.atom_word(atom)
        if word[: c350.RECORD_M2] != record.content or word[c350.RECORD_M2 :] != tag_word(tag):
            raise RuntimeError("30+13 field separation failed")
        atoms.append(atom)
    output = tuple(atoms)
    if not c350.validate_fixed_corpus(fixture, output):
        raise ValueError("encoded atoms do not inhabit Cycle-351's fixed-program corpus")
    return output


def decode_typed_corpus(
    fixture: c366.c364.c342.c338.RouteFixture,
    atoms: tuple[c350.CorpusAtom, ...],
    embedding: CorpusEmbedding,
) -> ThresholdCommonState:
    """D: exact code-space decoder using the supplied finite embedding."""

    if not isinstance(atoms, tuple) or len(atoms) != len(embedding.ordered_sites):
        raise ValueError("decoder input and embedding have different finite domains")
    if not c350.validate_fixed_corpus(fixture, atoms):
        raise ValueError("decoder requires a lawful Cycle-351 fixed-program corpus")
    records = tuple(
        c366.ThresholdSiteContentRecord(site, c366.c364.c342.record_word(atom.record), ())
        for site, atom in zip(embedding.ordered_sites, atoms)
    )
    tags = tuple(
        RegisteredConvergenceTag(
            site,
            record.content,
            atom.preparation,
            atom.program,
            atom.fine_pointer,
            atom.trial,
            atom.use,
        )
        for site, record, atom in zip(embedding.ordered_sites, records, atoms)
    )
    common = ThresholdCommonState(records, tags)
    validate_common_state(fixture, common)
    return common


def corpus_programs() -> tuple[c350.c321.Program, ...]:
    fixture = c350.c317.physical_fixture(3)
    return c350.c323.make_programs(fixture.contact)


def common_observables(
    common: ThresholdCommonState,
    embedding: CorpusEmbedding,
    programs: tuple[c350.c321.Program, ...],
) -> tuple[np.ndarray, ...]:
    validate_embedding(common, embedding)
    return tuple(
        programs[tag.program].fine_effects[tag.fine_pointer]
        for tag in common.tags
    )


def supplied_weight_rule(name: str):
    rules = {
        "supplied trace proposal": c350.born_trace_grade,
        "supplied nonlinear proposal": c350.nonlinear_grade,
    }
    if name not in rules:
        raise ValueError("weight proposal is outside the declared comparison menu")
    return rules[name]


def weight_view(
    atoms: tuple[c350.CorpusAtom, ...],
    programs: tuple[c350.c321.Program, ...],
    proposal_rule: str | None,
) -> ProposalWeightView:
    digest = c350.corpus_hash(atoms)
    if proposal_rule is None:
        return ProposalWeightView(digest, None, None)
    rule = supplied_weight_rule(proposal_rule)
    return ProposalWeightView(
        digest,
        proposal_rule,
        tuple(float(rule(c350.atom_effect(atom, programs), atom.preparation)) for atom in atoms),
    )


def common_weight_view(
    common: ThresholdCommonState,
    embedding: CorpusEmbedding,
    atoms: tuple[c350.CorpusAtom, ...],
    programs: tuple[c350.c321.Program, ...],
    proposal_rule: str,
) -> ProposalWeightView:
    rule = supplied_weight_rule(proposal_rule)
    observables = common_observables(common, embedding, programs)
    return ProposalWeightView(
        c350.corpus_hash(atoms),
        proposal_rule,
        tuple(
            float(rule(observable, tag.preparation))
            for observable, tag in zip(observables, common.tags)
        ),
    )


def build_physical_source(
    fixture: c366.c364.c342.c338.RouteFixture,
    size: int,
    multiplicity: int = c366.FORMATION_THRESHOLD,
) -> tuple[c366.BasisState, c366.BasisState, c366.BasisState]:
    if size not in SIZES and size != 1:
        raise ValueError("bridge fixture size is outside its declared finite domain")
    layout = c366.build_layout(size)
    words = c366.record_words(fixture, size)
    assignments = tuple(
        (
            event,
            c366.redundant_from_immediate(
                c366.immediate_proposal(layout.blocks[event], words[event], multiplicity),
                multiplicity,
            ),
        )
        for event in range(size)
    )
    prepared = c366.prepare(layout, assignments)
    if not prepared.admissible:
        raise RuntimeError(("threshold fixture rejected", prepared.reasons))
    calculated = c366.apply_layers(prepared.state, prepared.state.layout.layers[:-1])
    committed = c366.apply_layers(calculated, (prepared.state.layout.layers[-1],))
    return prepared.state, calculated, committed


def build_common(
    fixture: c366.c364.c342.c338.RouteFixture,
    size: int,
) -> tuple[c366.BasisState, c366.BasisState, c366.BasisState, ThresholdCommonState, CorpusEmbedding]:
    prepared, calculated, committed = build_physical_source(fixture, size)
    records = c366.logical_records(committed)
    tags = tuple(scheduled_tag(record.site, record.content, trial) for trial, record in enumerate(records))
    common = extract_common_state(fixture, committed, tags)
    embedding = CorpusEmbedding(tuple(record.site for record in common.records))
    return prepared, calculated, committed, common, embedding


def transform_basis_source(
    source: c366.BasisState,
    frame: np.ndarray,
    mapping,
) -> c366.BasisState:
    """Rotate physical coordinates and the Record-payload fields before step."""

    sites = tuple(
        replace(site, coord=c366.c362.c353.rotated(site.coord, frame))
        for site in source.layout.sites
    )
    blocks = tuple(
        replace(
            block,
            target_site=c366.c362.c353.rotated(block.target_site, frame),
            predecessors=tuple(c366.c362.c353.rotated(site, frame) for site in block.predecessors),
        )
        for block in source.layout.blocks
    )
    bits = list(source.bits)
    for block in source.layout.blocks:
        for replica in block.replicas:
            payload = tuple(source.bits[replica[lane]] for lane in c366.PAYLOAD_LANES)
            rotated = c366.c364.rotate_payload(payload, mapping)
            for lane, value in zip(c366.PAYLOAD_LANES, rotated):
                bits[replica[lane]] = value
    return c366.BasisState(replace(source.layout, sites=sites, blocks=blocks), tuple(bits))


def threshold_commit_and_trial_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    programs = corpus_programs()
    rows = []
    failures = 0
    for multiplicity in (1, 2, 3):
        prepared, calculated, committed = build_physical_source(fixture, 1, multiplicity)
        logical_before = c366.logical_records(calculated)
        logical_after = c366.logical_records(committed)
        atom_weights = {}
        if logical_after:
            record = logical_after[0]
            tag = scheduled_tag(record.site, record.content, 0)
            atom = c350.CorpusAtom(
                c366.c364.c342.decode_record_word(record.content),
                tag.preparation,
                tag.program,
                tag.fine_pointer,
                tag.trial,
                tag.use,
            )
            atom_weights = {
                name: float(supplied_weight_rule(name)(c350.atom_effect(atom, programs), atom.preparation))
                for name in ("supplied trace proposal", "supplied nonlinear proposal")
            }
        expected = int(multiplicity == c366.FORMATION_THRESHOLD)
        failures += int(
            len(logical_before) != 0
            or len(logical_after) != expected
            or c366.workspace_leakage(calculated) != 0
            or c366.workspace_leakage(committed) != 0
        )
        rows.append(
            {
                "precommit_carriers": multiplicity,
                "precommit_logical_Records": len(logical_before),
                "post_CONSUME_logical_Records": len(logical_after),
                "corpus_trials": len(logical_after),
                "downstream_proposal_views": atom_weights,
            }
        )
    signatures = {
        "prepare": tuple(signature(c366.prepare).parameters),
        "step": tuple(signature(c366.step).parameters),
        "extract": tuple(signature(extract_common_state).parameters),
        "E": tuple(signature(encode_typed_corpus).parameters),
    }
    executable_symbol_hits = {
        name: tuple(
            term
            for term in ("weight", "grade", "sampler")
            if any(
                term in symbol.lower()
                for symbol in function.__code__.co_names + function.__code__.co_varnames
            )
        )
        for name, function in (
            ("step", c366.step),
            ("extract", extract_common_state),
            ("E", encode_typed_corpus),
        )
    }
    detail = {
        "threshold": c366.FORMATION_THRESHOLD,
        "threshold_derived": False,
        "rows": rows,
        "interface_signatures": signatures,
        "weight_grade_sampler_executable_symbol_hits": executable_symbol_hits,
        "three_carriers_are_three_trials": False,
        "reversible_formed_transcript_is_Record": False,
        "CONSUME_admission_by_existing_framework_law": None,
    }
    check(
        "one/two/three carriers yield zero/zero/one post-CONSUME Record and downstream weights never determine threshold or commit",
        failures == 0
        and tuple(row["post_CONSUME_logical_Records"] for row in rows) == (0, 0, 1)
        and tuple(row["corpus_trials"] for row in rows) == (0, 0, 1)
        and all(not hits for hits in executable_symbol_hits.values())
        and signatures["step"] == ("state",)
        and signatures["extract"] == ("fixture", "physical", "tags")
        and signatures["E"] == ("fixture", "common", "embedding")
        and detail["CONSUME_admission_by_existing_framework_law"] is None,
        detail,
    )
    return {
        "failures": failures + sum(bool(hits) for hits in executable_symbol_hits.values()),
        **detail,
    }


def exact_maps_frame_controls() -> dict[str, object]:
    programs = corpus_programs()
    frames = c366.c362.c353.proper_cubic_frames()
    proposal_names = ("supplied trace proposal", "supplied nonlinear proposal")
    rows = []
    cases = held_cases = 0
    threshold_failures = common_covariance_failures = roundtrip_failures = field_leakage = 0
    record_mapping_failures = observable_failures = weight_failures = 0
    maximum_observable_residual = maximum_weight_residual = 0.0
    for length in LENGTHS:
        fixture = c366.c364.c342.c338.build_fixture(length)
        for size in SIZES:
            prepared, _calculated, _committed, base_common, _embedding = build_common(fixture, size)
            row_failures = 0
            for frame in frames:
                rotated_fixture, mapping, mapping_failures = c366.c364.c342.mapped_fixture(fixture, frame)
                record_mapping_failures += mapping_failures
                framed_source = transform_basis_source(prepared, frame, mapping)
                framed_calculated = c366.apply_layers(framed_source, framed_source.layout.layers[:-1])
                framed_committed = c366.apply_layers(framed_calculated, (framed_source.layout.layers[-1],))
                records = c366.logical_records(framed_committed)
                tags = tuple(scheduled_tag(record.site, record.content, trial) for trial, record in enumerate(records))
                common = extract_common_state(rotated_fixture, framed_committed, tags)
                expected_records = tuple(
                    replace(
                        record,
                        site=c366.c362.c353.rotated(record.site, frame),
                        content=c366.c364.rotate_payload(record.content, mapping),
                        predecessors=tuple(
                            c366.c362.c353.rotated(site, frame)
                            for site in record.predecessors
                        ),
                    )
                    for record in base_common.records
                )
                expected_common = ThresholdCommonState(
                    expected_records,
                    tuple(
                        scheduled_tag(record.site, record.content, trial)
                        for trial, record in enumerate(expected_records)
                    ),
                )
                common_covariance_failures += int(common != expected_common)
                embedding = CorpusEmbedding(tuple(record.site for record in common.records))
                atoms = encode_typed_corpus(rotated_fixture, common, embedding)
                decoded = decode_typed_corpus(rotated_fixture, atoms, embedding)
                roundtrip_failures += int(decoded != common)
                threshold_failures += int(
                    len(records) != size
                    or c366.logical_records(framed_calculated) != ()
                    or c366.workspace_leakage(framed_committed) != 0
                )
                common_effects = common_observables(common, embedding, programs)
                corpus_effects = tuple(c350.atom_effect(atom, programs) for atom in atoms)
                for record, tag, atom, left, right in zip(
                    common.records, common.tags, atoms, common_effects, corpus_effects
                ):
                    word = c350.atom_word(atom)
                    field_leakage += int(word[: c350.RECORD_M2] != record.content)
                    field_leakage += int(word[c350.RECORD_M2 :] != tag_word(tag))
                    residual = float(np.linalg.norm(left - right))
                    maximum_observable_residual = max(maximum_observable_residual, residual)
                    observable_failures += int(residual > 1e-12)
                for name in proposal_names:
                    left = common_weight_view(common, embedding, atoms, programs, name)
                    right = weight_view(atoms, programs, name)
                    weight_failures += int(left != right)
                    if left.weights is None or right.weights is None:
                        residual = float("inf")
                    else:
                        residual = max(abs(a - b) for a, b in zip(left.weights, right.weights))
                    maximum_weight_residual = max(maximum_weight_residual, residual)
                cases += 1
                held_cases += int(length == 6 and size == HELD_SIZE)
            row_failures += threshold_failures + roundtrip_failures + field_leakage
            rows.append(
                {
                    "L": length,
                    "N": size,
                    "train": size in TRAIN_SIZES,
                    "held": length == 6 and size == HELD_SIZE,
                    "frames": len(frames),
                    "post_CONSUME_Records_per_frame": size,
                }
            )
    total_failures = (
        threshold_failures
        + common_covariance_failures
        + roundtrip_failures
        + field_leakage
        + record_mapping_failures
        + observable_failures
        + weight_failures
    )
    detail = {
        "rows": rows,
        "L_by_N_by_frame_cases": cases,
        "held_L6_N12_frame_cases": held_cases,
        "proper_cubic_frames": len(frames),
        "threshold_or_commit_failures": threshold_failures,
        "common_state_covariance_failures": common_covariance_failures,
        "D_E_roundtrip_failures": roundtrip_failures,
        "30_plus_13_field_leakage": field_leakage,
        "Record_payload_mapping_failures": record_mapping_failures,
        "observable_intertwiner_failures": observable_failures,
        "proposal_weight_intertwiner_failures": weight_failures,
        "maximum_observable_residual": maximum_observable_residual,
        "maximum_proposal_weight_residual": maximum_weight_residual,
        "intertwiners": (
            "D E = identity on ThresholdCommonState",
            "O_common = O_Cycle351 E",
            "W_proposal,common = W_proposal,Cycle351 E",
        ),
    }
    check(
        "E/D and observable/proposal-weight views intertwine exactly at L3/L6 N3/N6/held-N12 in all 24 frames",
        cases == len(LENGTHS) * len(SIZES) * 24
        and held_cases == 24
        and total_failures == 0
        and maximum_observable_residual == maximum_weight_residual == 0.0,
        detail,
    )
    return {"failures": total_failures, **detail}


def deletion_splice_domain_leakage_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    prepared, calculated, committed, common, embedding = build_common(fixture, 6)
    atoms = encode_typed_corpus(fixture, common, embedding)
    programs = corpus_programs()
    before_hash = c350.corpus_hash(atoms)
    deleted_weights = weight_view(atoms, programs, None)
    trace_weights = weight_view(atoms, programs, "supplied trace proposal")
    nonlinear_weights = weight_view(atoms, programs, "supplied nonlinear proposal")
    after_hash = c350.corpus_hash(atoms)

    carrier_deleted_bits = list(prepared.bits)
    for offset in prepared.layout.blocks[0].replicas[2]:
        carrier_deleted_bits[offset] = 0
    carrier_deleted = replace(prepared, bits=tuple(carrier_deleted_bits))
    carrier_deleted_final = c366.step(carrier_deleted)

    carrier_corrupted_bits = list(prepared.bits)
    carrier_corrupted_bits[prepared.layout.blocks[0].replicas[2][0]] ^= 1
    carrier_corrupted = replace(prepared, bits=tuple(carrier_corrupted_bits))
    carrier_corrupted_final = c366.step(carrier_corrupted)

    deleted_atoms = atoms[:-1]
    spliced_atoms = list(atoms)
    spliced_atoms[0], spliced_atoms[1] = spliced_atoms[1], spliced_atoms[0]
    invalid_calls = (
        lambda: extract_common_state(fixture, calculated, ()),
        lambda: extract_common_state(fixture, carrier_deleted_final, common.tags),
        lambda: extract_common_state(fixture, carrier_corrupted_final, common.tags),
        lambda: validate_common_state(fixture, replace(common, tags=common.tags[:-1])),
        lambda: validate_common_state(
            fixture,
            replace(
                common,
                tags=(replace(common.tags[0], site=common.tags[1].site),) + common.tags[1:],
            ),
        ),
        lambda: validate_common_state(
            fixture,
            replace(
                common,
                tags=(replace(common.tags[0], payload=common.tags[1].payload),) + common.tags[1:],
            ),
        ),
        lambda: decode_typed_corpus(fixture, deleted_atoms, embedding),
        lambda: decode_typed_corpus(fixture, tuple(spliced_atoms), embedding),
        lambda: encode_typed_corpus(
            fixture, common, CorpusEmbedding(embedding.ordered_sites[:-1])
        ),
        lambda: validate_common_state(
            fixture,
            replace(
                common,
                tags=(replace(common.tags[0], pointer_event_registered=0),) + common.tags[1:],
            ),
        ),
        lambda: supplied_weight_rule("selected Born rule"),
    )
    rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            rejections += 1

    distinct_weight_delta = 0.0
    if trace_weights.weights is not None and nonlinear_weights.weights is not None:
        distinct_weight_delta = max(
            abs(left - right)
            for left, right in zip(trace_weights.weights, nonlinear_weights.weights)
        )
    common_surface = set(ThresholdCommonState.__dataclass_fields__)
    detail = {
        "precommit_logical_Records": len(c366.logical_records(calculated)),
        "post_CONSUME_logical_Records": len(c366.logical_records(committed)),
        "carrier_deletion_first_event_Record_absent": all(
            record.site != prepared.layout.blocks[0].target_site
            for record in c366.logical_records(carrier_deleted_final)
        ),
        "carrier_corruption_first_event_Record_absent": all(
            record.site != prepared.layout.blocks[0].target_site
            for record in c366.logical_records(carrier_corrupted_final)
        ),
        "domain_rejections": rejections,
        "domain_attempts": len(invalid_calls),
        "corpus_hash_before_weight_views": before_hash,
        "corpus_hash_after_weight_views": after_hash,
        "weight_deleted_weights": deleted_weights.weights,
        "trace_sampler": trace_weights.actual_history_sampler,
        "trace_actual_member": trace_weights.actual_member_selector,
        "nonlinear_sampler": nonlinear_weights.actual_history_sampler,
        "distinct_supplied_weight_maximum_delta": distinct_weight_delta,
        "common_state_fields": tuple(sorted(common_surface)),
        "carrier_registers_in_common_state": bool(common_surface.intersection({"replicas", "carriers"})),
        "reversible_transcript_in_common_state": bool(common_surface.intersection({"formed", "fresh", "workspace", "bits"})),
        "whole_43_M2_atom_is_Record": False,
        "Record_M2": c350.RECORD_M2,
        "tag_M2": TAG_M2,
        "atom_M2": c350.ATOM_M2,
        "Cycle350_form_atom_called": "form_atom" in getsource(encode_typed_corpus),
    }
    check(
        "CONSUME/carrier/tag/atom deletion and splice controls reject; 30+13 fields do not leak and weights leave the corpus immutable",
        detail["precommit_logical_Records"] == 0
        and detail["post_CONSUME_logical_Records"] == 6
        and detail["carrier_deletion_first_event_Record_absent"]
        and detail["carrier_corruption_first_event_Record_absent"]
        and rejections == len(invalid_calls)
        and before_hash == after_hash == deleted_weights.corpus_hash
        and deleted_weights.weights is None
        and trace_weights.actual_history_sampler is None
        and trace_weights.actual_member_selector is None
        and nonlinear_weights.actual_history_sampler is None
        and distinct_weight_delta > 1e-6
        and not detail["carrier_registers_in_common_state"]
        and not detail["reversible_transcript_in_common_state"]
        and detail["whole_43_M2_atom_is_Record"] is False
        and (detail["Record_M2"], detail["tag_M2"], detail["atom_M2"]) == (30, 13, 43)
        and not detail["Cycle350_form_atom_called"],
        detail,
    )
    return detail


def supplied_structure_and_residual_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded positive conditional Cycle-366 post-CONSUME Record to Cycle-351 corpus bridge",
        "common_state": "only post-CONSUME convergence Records plus one exact registered tag each",
        "three_precommit_carriers_are_Records": False,
        "three_precommit_carriers_are_three_trials": False,
        "reversible_formed_transcript_is_Record": False,
        "Cycle366_threshold": c366.FORMATION_THRESHOLD,
        "threshold_input": "supplied candidate-law content; not derived here",
        "Cycle366_candidate_law_selected": False,
        "reversible_threshold_calculation": "exact fixed connected-NN Boolean basis-state X/CNOT/Toffoli realization inherited from Cycle 366",
        "reversible_threshold_calculation_is_admitted_physical_M2_gate_compiler": False,
        "CONSUME_input": "one isolated supplied nonunitary fresh-token consume",
        "CONSUME_admission_by_existing_framework_law": None,
        "Cycle342_fixture": "supplied L3/L6 decoder and proper-cubic payload mapping",
        "typing_and_permanence": "validated in every 30-M2 convergence Record",
        "apparatus_tag_input": "supplied 13-M2 preparation/program/fine-pointer/trial/use word",
        "tag_binding_input": "supplied exact convergence-site/payload binding and pointer-event registration",
        "apparatus_fixture": "supplied Cycle-323/350 fixed six-program effect table and contact fixture",
        "embedding": "supplied ordered convergence-site list",
        "train_sizes": TRAIN_SIZES,
        "held_size": HELD_SIZE,
        "physical_tag_genesis_compiler": None,
        "physical_nearest_neighbor_30_plus_13_binding_compiler": None,
        "weight_inputs": (
            "optional supplied trace proposal functional",
            "optional supplied nonlinear comparison functional",
        ),
        "selected_weight_rule": None,
        "weight_input_to_threshold_or_commit": None,
        "weight_input_to_encoder_E": None,
        "proposal_weights_are_sampling_probabilities": False,
        "actual_history_sampler": None,
        "actual_member_selector": None,
        "Born_rule_selected": False,
        "Born_law_derived": False,
        "repeated_history_law": None,
        "frequency_theorem": None,
        "whole_43_M2_atom_is_Record": False,
        "implementation_or_law_incompleteness": (
            "CONSUME admission, threshold justification, tag genesis/binding compiler, unique numerical law, actual-history sampler, and frequency theorem remain open"
        ),
        "shared_substrate_obstruction": None,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the supplied threshold, commit, fixture, tag, embedding, apparatus, weight, and compiler residuals are explicit without selecting Cycle 366 or a Born rule",
        inventory["three_precommit_carriers_are_Records"] is False
        and inventory["three_precommit_carriers_are_three_trials"] is False
        and inventory["reversible_formed_transcript_is_Record"] is False
        and inventory["Cycle366_threshold"] == 3
        and inventory["Cycle366_candidate_law_selected"] is False
        and inventory["reversible_threshold_calculation_is_admitted_physical_M2_gate_compiler"] is False
        and inventory["CONSUME_admission_by_existing_framework_law"] is None
        and inventory["physical_tag_genesis_compiler"] is None
        and inventory["physical_nearest_neighbor_30_plus_13_binding_compiler"] is None
        and inventory["selected_weight_rule"] is None
        and inventory["weight_input_to_threshold_or_commit"] is None
        and inventory["weight_input_to_encoder_E"] is None
        and inventory["proposal_weights_are_sampling_probabilities"] is False
        and inventory["actual_history_sampler"] is None
        and inventory["actual_member_selector"] is None
        and inventory["Born_rule_selected"] is False
        and inventory["Born_law_derived"] is False
        and inventory["repeated_history_law"] is None
        and inventory["frequency_theorem"] is None
        and inventory["whole_43_M2_atom_is_Record"] is False
        and inventory["shared_substrate_obstruction"] is None
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def inherited_carrier_controls() -> dict[str, object]:
    with redirect_stdout(StringIO()):
        fixtures = c350.c323.physical_fixture_controls()
        programs = c350.c323.make_programs(fixtures[3].contact)
        carrier = c350.c323.FixedProgramCarrier(programs)
        covariance = c350.c323.covariance_controls(fixtures, carrier)
    detail = {
        "proper_cubic_frames": covariance["frames"],
        "carrier_branch_failures": covariance["branch_failures"],
        "maximum_one_use_carrier_residual": covariance["maximum_one_use_carrier_residual"],
        "maximum_two_use_carrier_residual": covariance["maximum_two_use_carrier_residual"],
        "fixed_apparatus_carrier_is_supplied": True,
    }
    check(
        "the inherited fixed apparatus carrier preserves its all-frame observable surface without becoming a Record, tag genesis law, or sampler",
        detail["proper_cubic_frames"] == 24
        and detail["carrier_branch_failures"] == 0
        and detail["maximum_one_use_carrier_residual"] < c350.TOL
        and detail["maximum_two_use_carrier_residual"] < c350.TOL
        and detail["fixed_apparatus_carrier_is_supplied"],
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 371: CONDITIONAL THRESHOLD-CONVERGENCE RECORD -> CYCLE-351 CORPUS BRIDGE")
    print("authority=none; audit=unset; Cycle366 and Born rule unselected")
    note = note_contract()
    threshold = threshold_commit_and_trial_controls()
    frames = exact_maps_frame_controls()
    attacks = deletion_splice_domain_leakage_controls()
    inventory = supplied_structure_and_residual_controls()
    carrier = inherited_carrier_controls()
    check(
        "Cycle 371 constructs an exact conditional post-CONSUME common-state bridge while leaving physical commit/tag compilation and actuality/statistics open",
        not note["missing"]
        and threshold["failures"] == 0
        and frames["failures"] == 0
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and inventory["CONSUME_admission_by_existing_framework_law"] is None
        and inventory["physical_tag_genesis_compiler"] is None
        and inventory["physical_nearest_neighbor_30_plus_13_binding_compiler"] is None
        and inventory["actual_history_sampler"] is None
        and carrier["carrier_branch_failures"] == 0,
        {
            "disposition": "bounded positive conditional common-state adapter",
            "strongest_positive": "post-CONSUME convergence Record exact 30+13 E/D plus observable/proposal-weight intertwiners",
            "open_physical_residual": "CONSUME admission and 13-M2 tag genesis/NN binding compiler",
            "selected_candidate_law": None,
            "selected_Born_rule": None,
            "shared_obstruction": None,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_BORN_CORPUS_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_BORN_CORPUS_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
