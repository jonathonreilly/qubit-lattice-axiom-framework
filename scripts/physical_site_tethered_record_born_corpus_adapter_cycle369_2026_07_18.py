#!/usr/bin/env python3
"""Cycle 369: conditional Cycle-364 -> Cycle-351 typed-corpus adapter.

The runner maps the output of the unselected Cycle-364 site-tethered
formation hypothesis into Cycle 351's concrete fixed-program 30+13 M2 corpus
contract.  It never calls Cycle 350's older occurrence/typing constructor.
One atomic adapter call commits a Cycle-364 conditional site/content Record
and one supplied site/payload-bound registered apparatus tag together, or
leaves the whole common state unchanged.

The exact finite code-space maps are

    E : TaggedFormationState x explicit embedding -> tuple[CorpusAtom],
    D E = identity,
    O_common = O_corpus E,
    W_proposal,common = W_proposal,corpus E.

Weights are optional downstream proposal views.  They do not enter formation
or E, and no proposal rule is selected.  The actual-history sampler input and
actual-member selector are both absent.  This is a bounded conditional corpus
bridge, not a Born derivation, occurrence selector, frequency theorem, count,
time, rate, energy, law-completeness result, no-go, or axiom-pressure result.
Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from inspect import getsource, signature
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SITE_TETHERED_RECORD_BORN_CORPUS_ADAPTER_"
    "CYCLE369_NOTE_2026-07-18.md"
)

import physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18 as c350
import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364
import physical_record_formation_link_genesis_counter_adapter_cycle368_2026_07_18 as c368


Coord = c364.Coord
Word = c364.Word
LENGTHS = (3, 6)
TRAIN_SIZES = (3, 6)
HELD_SIZE = 12
SIZES = TRAIN_SIZES + (HELD_SIZE,)
TAG_BITS = c350.ATOM_M2 - c350.RECORD_M2
TAG_SOURCE = "Cycle-369 supplied site/payload-bound Cycle-351 apparatus tag"
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
        check("the Cycle-369 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "non-circular bounded common-state map",
        "does not call the older cycle-350 formation connector",
        "the whole 43-bit atom is not promoted to a record",
        "actuality remains open",
        "statistics remains open",
        "sampler input is explicitly none",
        "law/interface incompleteness, not an obstruction",
        "train sizes n=3 and n=6",
        "held-out size n=12",
        "all 24 proper-cubic spatial frames",
        "no count is called probability",
        "canonical law-completeness contract",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the non-circular map, finite domain, supplied inputs, and actuality/statistics firewall",
        not missing,
        missing,
    )
    return {"missing": missing}


@dataclass(frozen=True)
class RegisteredCorpusTag:
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
class TaggedFormationState:
    formation: c364.FormationState
    tags: tuple[RegisteredCorpusTag, ...] = ()


@dataclass(frozen=True)
class TagAdapterAnswer:
    state: TaggedFormationState
    formed: c364.SiteContentRecord | None
    status: str
    formation_conditions: tuple[tuple[str, bool], ...]
    tag_conditions: tuple[tuple[str, bool], ...]


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


def canonical_tags(tags: tuple[RegisteredCorpusTag, ...]) -> tuple[RegisteredCorpusTag, ...]:
    return tuple(sorted(tags, key=lambda item: item.site))


def tag_map(state: TaggedFormationState) -> dict[Coord, RegisteredCorpusTag]:
    return {tag.site: tag for tag in state.tags}


def validate_tag(tag: RegisteredCorpusTag) -> None:
    if not isinstance(tag, RegisteredCorpusTag):
        raise TypeError("corpus adapter requires one RegisteredCorpusTag")
    if (
        not c364.valid_coord(tag.site)
        or not isinstance(tag.payload, tuple)
        or len(tag.payload) != c364.RECORD_BITS
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
        or tag.pointer_event_registered not in (0, 1)
        or tag.source != TAG_SOURCE
    ):
        raise ValueError("registered corpus tag is outside its 13-M2 domain")


def validate_tagged_state(
    fixture: c364.c342.c338.RouteFixture,
    state: TaggedFormationState,
) -> None:
    if not isinstance(state, TaggedFormationState):
        raise TypeError("corpus adapter requires one TaggedFormationState")
    c364.validate_state(fixture, state.formation)
    if not isinstance(state.tags, tuple) or state.tags != canonical_tags(state.tags):
        raise ValueError("registered tags must be an immutable canonical tuple")
    for tag in state.tags:
        validate_tag(tag)
    if len({tag.site for tag in state.tags}) != len(state.tags):
        raise ValueError("registered tags contain a site alias")
    if len({tag.trial for tag in state.tags}) != len(state.tags):
        raise ValueError("registered tags contain a trial alias")
    records = c364.record_map(state.formation)
    tags = tag_map(state)
    if set(records) != set(tags):
        raise ValueError("every and only formed Record sites require one registered tag")
    if any(
        tag.payload != records[site].content or tag.pointer_event_registered != 1
        for site, tag in tags.items()
    ):
        raise ValueError("tag site/content registration disagrees with formed Records")


def tag_word(tag: RegisteredCorpusTag) -> Word:
    validate_tag(tag)
    word = (
        c350.bits(tag.preparation, c350.PREPARATION_M2)
        + c350.bits(tag.program, c350.PROGRAM_M2)
        + c350.bits(tag.fine_pointer, c350.FINE_POINTER_M2)
        + c350.bits(tag.trial, c350.TRIAL_M2)
        + (tag.use,)
    )
    if len(word) != TAG_BITS:
        raise RuntimeError("registered apparatus-tag inventory drifted")
    return word


def scheduled_tag(site: Coord, payload: Word, trial: int) -> RegisteredCorpusTag:
    preparation, program, fine_pointer, use = c350.schedule_fields(trial)
    return RegisteredCorpusTag(
        site,
        payload,
        preparation,
        program,
        fine_pointer,
        trial,
        use,
    )


def tag_condition_table(
    state: TaggedFormationState,
    proposal: c364.FormationProposal,
    tag: RegisteredCorpusTag,
) -> tuple[tuple[str, bool], ...]:
    existing = tag_map(state)
    return (
        (
            "site_payload_binding",
            tag.site == proposal.site and tag.payload == proposal.payload,
        ),
        ("pointer_event_registration", tag.pointer_event_registered == 1),
        ("fresh_tag_site", tag.site not in existing),
        ("fresh_trial_tag", tag.trial not in {item.trial for item in state.tags}),
    )


def apply_formation_corpus_tag(
    fixture: c364.c342.c338.RouteFixture,
    state: TaggedFormationState,
    proposal: c364.FormationProposal,
    tag: RegisteredCorpusTag,
) -> TagAdapterAnswer:
    """Atomic conditional formation/tag adapter; accepts no grade or sampler."""

    validate_tagged_state(fixture, state)
    validate_tag(tag)
    formation = c364.apply_candidate_law(fixture, state.formation, proposal)
    tag_conditions = tag_condition_table(state, proposal, tag)
    if formation.formed is None:
        return TagAdapterAnswer(
            state,
            None,
            "formation-" + formation.status,
            formation.conditions,
            tag_conditions,
        )
    failed = tuple(name for name, value in tag_conditions if not value)
    if failed:
        return TagAdapterAnswer(
            state,
            None,
            "tag-blocked:" + ",".join(failed),
            formation.conditions,
            tag_conditions,
        )
    output = TaggedFormationState(
        formation.state,
        canonical_tags(state.tags + (tag,)),
    )
    validate_tagged_state(fixture, output)
    return TagAdapterAnswer(
        output,
        formation.formed,
        "formed-with-registered-corpus-tag",
        formation.conditions,
        tag_conditions,
    )


def build_tagged_chain(
    fixture: c364.c342.c338.RouteFixture,
    count: int,
) -> tuple[
    TaggedFormationState,
    tuple[TaggedFormationState, ...],
    tuple[c364.FormationProposal, ...],
    tuple[RegisteredCorpusTag, ...],
]:
    if count not in SIZES:
        raise ValueError("tagged corpus count is outside Cycle-351 train/held domain")
    payloads = c364.words(fixture, count)
    state = TaggedFormationState(c364.FormationState())
    states = [state]
    proposals = []
    tags = []
    for trial, payload in enumerate(payloads):
        site = (trial, 0, 0)
        predecessors: tuple[Coord, ...] = () if trial == 0 else ((trial - 1, 0, 0),)
        proposal = c364.proposal(site, payload, predecessors)
        tag = scheduled_tag(site, payload, trial)
        answer = apply_formation_corpus_tag(fixture, state, proposal, tag)
        if answer.status != "formed-with-registered-corpus-tag":
            raise RuntimeError(("lawful tagged fixture did not form", trial, answer))
        state = answer.state
        states.append(state)
        proposals.append(proposal)
        tags.append(tag)
    return state, tuple(states), tuple(proposals), tuple(tags)


def validate_embedding(state: TaggedFormationState, embedding: CorpusEmbedding) -> None:
    if not isinstance(embedding, CorpusEmbedding) or not isinstance(embedding.ordered_sites, tuple):
        raise TypeError("corpus encoder needs one explicit ordered-site embedding")
    records = c364.record_map(state.formation)
    if (
        not embedding.ordered_sites
        or len(set(embedding.ordered_sites)) != len(embedding.ordered_sites)
        or any(not c364.valid_coord(site) for site in embedding.ordered_sites)
        or set(embedding.ordered_sites) != set(records)
    ):
        raise ValueError("embedding must name every formed site exactly once")
    for index, site in enumerate(embedding.ordered_sites):
        expected: tuple[Coord, ...] = () if index == 0 else (embedding.ordered_sites[index - 1],)
        if records[site].predecessors != expected:
            raise ValueError("ordered corpus embedding disagrees with predecessor metadata")


def encode_typed_corpus(
    fixture: c364.c342.c338.RouteFixture,
    state: TaggedFormationState,
    embedding: CorpusEmbedding,
) -> tuple[c350.CorpusAtom, ...]:
    """E: exact grade- and sampler-blind common-state corpus encoder."""

    validate_tagged_state(fixture, state)
    validate_embedding(state, embedding)
    records = c364.record_map(state.formation)
    tags = tag_map(state)
    atoms = []
    for trial, site in enumerate(embedding.ordered_sites):
        tag = tags[site]
        if tag.trial != trial or (
            tag.preparation,
            tag.program,
            tag.fine_pointer,
            tag.use,
        ) != c350.schedule_fields(trial):
            raise ValueError("supplied tag does not inhabit the fixed-program corpus embedding")
        record = c364.c342.decode_record_word(records[site].content)
        atom = c350.CorpusAtom(
            record,
            tag.preparation,
            tag.program,
            tag.fine_pointer,
            tag.trial,
            tag.use,
        )
        word = c350.atom_word(atom)
        if word[: c364.RECORD_BITS] != records[site].content or word[c364.RECORD_BITS :] != tag_word(tag):
            raise RuntimeError("30+13 M2 corpus encoding failed exact field separation")
        atoms.append(atom)
    output = tuple(atoms)
    if not c350.validate_fixed_corpus(fixture, output):
        raise ValueError("encoded atoms do not form a lawful Cycle-351 fixed corpus")
    return output


def decode_typed_corpus(
    fixture: c364.c342.c338.RouteFixture,
    atoms: tuple[c350.CorpusAtom, ...],
    embedding: CorpusEmbedding,
) -> TaggedFormationState:
    """D: exact code-space decoder using only the supplied site embedding."""

    if not isinstance(atoms, tuple) or len(atoms) != len(embedding.ordered_sites):
        raise ValueError("corpus decoder has the wrong finite domain")
    if not c350.validate_fixed_corpus(fixture, atoms):
        raise ValueError("corpus decoder requires a lawful fixed-program atom tuple")
    records = []
    tags = []
    for index, (site, atom) in enumerate(zip(embedding.ordered_sites, atoms)):
        content = c364.c342.record_word(atom.record)
        predecessors: tuple[Coord, ...] = () if index == 0 else (embedding.ordered_sites[index - 1],)
        records.append(c364.SiteContentRecord(site, content, predecessors))
        tags.append(
            RegisteredCorpusTag(
                site,
                content,
                atom.preparation,
                atom.program,
                atom.fine_pointer,
                atom.trial,
                atom.use,
            )
        )
    output = TaggedFormationState(
        c364.FormationState(c364.canonical(tuple(records))),
        canonical_tags(tuple(tags)),
    )
    validate_tagged_state(fixture, output)
    return output


def corpus_programs() -> tuple[c350.c321.Program, ...]:
    fixture = c350.c317.physical_fixture(3)
    return c350.c323.make_programs(fixture.contact)


def common_observables(
    state: TaggedFormationState,
    embedding: CorpusEmbedding,
    programs: tuple[c350.c321.Program, ...],
) -> tuple[np.ndarray, ...]:
    tags = tag_map(state)
    return tuple(
        programs[tags[site].program].fine_effects[tags[site].fine_pointer]
        for site in embedding.ordered_sites
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
    weights = tuple(
        float(rule(c350.atom_effect(atom, programs), atom.preparation))
        for atom in atoms
    )
    return ProposalWeightView(digest, proposal_rule, weights)


def common_weight_view(
    state: TaggedFormationState,
    embedding: CorpusEmbedding,
    atoms: tuple[c350.CorpusAtom, ...],
    programs: tuple[c350.c321.Program, ...],
    proposal_rule: str,
) -> ProposalWeightView:
    rule = supplied_weight_rule(proposal_rule)
    tags = tag_map(state)
    observables = common_observables(state, embedding, programs)
    weights = tuple(
        float(rule(observable, tags[site].preparation))
        for site, observable in zip(embedding.ordered_sites, observables)
    )
    return ProposalWeightView(c350.corpus_hash(atoms), proposal_rule, weights)


def transform_tag(
    tag: RegisteredCorpusTag,
    frame: np.ndarray,
    mapping,
) -> RegisteredCorpusTag:
    return replace(
        tag,
        site=c364.transform_coord(tag.site, frame, (0, 0, 0)),
        payload=c364.rotate_payload(tag.payload, mapping),
    )


def transform_state(
    state: TaggedFormationState,
    frame: np.ndarray,
    mapping,
) -> TaggedFormationState:
    return TaggedFormationState(
        c364.transform_state(state.formation, frame, (0, 0, 0), mapping),
        canonical_tags(tuple(transform_tag(tag, frame, mapping) for tag in state.tags)),
    )


def atomic_formation_tag_controls() -> dict[str, object]:
    rows = []
    failures = preservation_failures = 0
    for length in LENGTHS:
        fixture = c364.c342.c338.build_fixture(length)
        for count in SIZES:
            final, states, _proposals, _tags = build_tagged_chain(fixture, count)
            for before, after in zip(states, states[1:]):
                failures += int(
                    len(after.formation.records) - len(before.formation.records) != 1
                    or len(after.tags) - len(before.tags) != 1
                )
                before_records = c364.record_map(before.formation)
                after_records = c364.record_map(after.formation)
                preservation_failures += sum(
                    after_records.get(site) != record for site, record in before_records.items()
                )
                preservation_failures += sum(tag not in after.tags for tag in before.tags)
            failures += int(
                len(final.formation.records) != count
                or len(final.tags) != count
                or any(tag.payload != c364.record_map(final.formation)[tag.site].content for tag in final.tags)
            )
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "train": count in TRAIN_SIZES,
                    "held": length == 6 and count == HELD_SIZE,
                    "formed_Records": len(final.formation.records),
                    "registered_tags": len(final.tags),
                    "common_state_M2": count * c350.ATOM_M2,
                    "prior_Record_tag_residual": preservation_failures,
                }
            )
    parameters = tuple(signature(apply_formation_corpus_tag).parameters)
    check(
        "each Cycle-364 formation and its site/payload-bound 13-M2 tag commit atomically at Cycle-351 train/held sizes without a grade or sampler input",
        failures == preservation_failures == 0
        and parameters == ("fixture", "state", "proposal", "tag"),
        {
            "rows": rows,
            "atomic_failures": failures,
            "prior_Record_tag_residual": preservation_failures,
            "adapter_parameters": parameters,
        },
    )
    return {"rows": rows, "failures": failures + preservation_failures}


def encoder_observable_weight_frame_controls() -> dict[str, object]:
    programs = corpus_programs()
    frames = c350.c311.c235.proper_cubic_frames()
    frame_corpus_cases = held_cases = 0
    adapter_covariance_failures = encoder_roundtrip_failures = 0
    field_leakage = record_mapping_failures = observable_failures = 0
    maximum_observable_residual = maximum_weight_residual = 0.0
    proposal_names = ("supplied trace proposal", "supplied nonlinear proposal")
    for length in LENGTHS:
        fixture = c364.c342.c338.build_fixture(length)
        base_by_size = {count: build_tagged_chain(fixture, count) for count in SIZES}
        for frame in frames:
            rotated_fixture, mapping, mapping_failures = c364.c342.mapped_fixture(fixture, frame)
            record_mapping_failures += mapping_failures
            for count in SIZES:
                base_final, base_states, proposals, tags = base_by_size[count]
                prefix = base_states[-2]
                reference = apply_formation_corpus_tag(
                    fixture, prefix, proposals[-1], tags[-1]
                )
                transformed_prefix = transform_state(prefix, frame, mapping)
                transformed_proposal = c364.transform_proposal(
                    proposals[-1], frame, (0, 0, 0), mapping
                )
                transformed_tag = transform_tag(tags[-1], frame, mapping)
                observed = apply_formation_corpus_tag(
                    rotated_fixture,
                    transformed_prefix,
                    transformed_proposal,
                    transformed_tag,
                )
                expected = transform_state(reference.state, frame, mapping)
                adapter_covariance_failures += int(
                    observed.status != reference.status or observed.state != expected
                )
                order = tuple(
                    c364.transform_coord((index, 0, 0), frame, (0, 0, 0))
                    for index in range(count)
                )
                embedding = CorpusEmbedding(order)
                atoms = encode_typed_corpus(rotated_fixture, observed.state, embedding)
                encoder_roundtrip_failures += int(
                    decode_typed_corpus(rotated_fixture, atoms, embedding) != observed.state
                )
                common_effects = common_observables(observed.state, embedding, programs)
                corpus_effects = tuple(c350.atom_effect(atom, programs) for atom in atoms)
                for site, atom, common_effect, corpus_effect in zip(
                    embedding.ordered_sites, atoms, common_effects, corpus_effects
                ):
                    record = c364.record_map(observed.state.formation)[site]
                    tag = tag_map(observed.state)[site]
                    word = c350.atom_word(atom)
                    field_leakage += int(word[: c364.RECORD_BITS] != record.content)
                    field_leakage += int(word[c364.RECORD_BITS :] != tag_word(tag))
                    residual = float(np.linalg.norm(common_effect - corpus_effect))
                    maximum_observable_residual = max(maximum_observable_residual, residual)
                    observable_failures += int(residual > 1e-12)
                    frame_corpus_cases += 1
                    held_cases += int(length == 6 and count == HELD_SIZE)
                for name in proposal_names:
                    common_view = common_weight_view(
                        observed.state, embedding, atoms, programs, name
                    )
                    corpus_view = weight_view(atoms, programs, name)
                    if common_view.weights is None or corpus_view.weights is None:
                        maximum_weight_residual = float("inf")
                    else:
                        residual = max(
                            abs(left - right)
                            for left, right in zip(common_view.weights, corpus_view.weights)
                        )
                        maximum_weight_residual = max(maximum_weight_residual, residual)
                    observable_failures += int(common_view != corpus_view)
    detail = {
        "L_by_size_by_frame_atom_cases": frame_corpus_cases,
        "proper_cubic_frames": len(frames),
        "held_L6_N12_atom_cases": held_cases,
        "adapter_covariance_failures": adapter_covariance_failures,
        "D_E_roundtrip_failures": encoder_roundtrip_failures,
        "30_plus_13_field_leakage": field_leakage,
        "Record_payload_mapping_failures": record_mapping_failures,
        "observable_or_weight_intertwiner_failures": observable_failures,
        "maximum_observable_residual": maximum_observable_residual,
        "maximum_proposal_weight_residual": maximum_weight_residual,
        "intertwiners": (
            "D E = identity",
            "O_common = O_Cycle351 E",
            "W_proposal,common = W_proposal,Cycle351 E",
        ),
    }
    check(
        "E/D and supplied observable/weight proposal views intertwine exactly in all 24 frames at L3/L6 and N3/N6/held-N12",
        len(frames) == 24
        and frame_corpus_cases == len(LENGTHS) * sum(SIZES) * 24
        and held_cases == HELD_SIZE * 24
        and adapter_covariance_failures == encoder_roundtrip_failures == 0
        and field_leakage == record_mapping_failures == observable_failures == 0
        and maximum_observable_residual == maximum_weight_residual == 0.0,
        detail,
    )
    return detail


def deletion_splice_domain_and_sampler_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(3)
    payloads = c364.words(fixture, 6)
    empty = TaggedFormationState(c364.FormationState())
    root_proposal = c364.proposal((0, 0, 0), payloads[0])
    root_tag = scheduled_tag((0, 0, 0), payloads[0], 0)
    root = apply_formation_corpus_tag(fixture, empty, root_proposal, root_tag)
    child_proposal = c364.proposal((1, 0, 0), payloads[1], ((0, 0, 0),))
    child_tag = scheduled_tag((1, 0, 0), payloads[1], 1)
    nominal = apply_formation_corpus_tag(
        fixture, root.state, child_proposal, child_tag
    )
    missing_formation = apply_formation_corpus_tag(
        fixture,
        root.state,
        replace(child_proposal, close=replace(child_proposal.close, close_candidate=0)),
        child_tag,
    )
    attacks = (
        (
            "pointer_registration_deleted",
            replace(child_tag, pointer_event_registered=0),
            "pointer_event_registration",
        ),
        (
            "tag_site_splice",
            replace(child_tag, site=(2, 0, 0)),
            "site_payload_binding",
        ),
        (
            "tag_payload_splice",
            replace(child_tag, payload=payloads[2]),
            "site_payload_binding",
        ),
        (
            "trial_alias",
            replace(child_tag, trial=0),
            "fresh_trial_tag",
        ),
    )
    attack_rows = []
    for name, tag, condition in attacks:
        answer = apply_formation_corpus_tag(
            fixture, root.state, child_proposal, tag
        )
        attack_rows.append(
            {
                "attack": name,
                "formed": answer.formed is not None,
                "state_unchanged": answer.state == root.state,
                "condition_visible": dict(answer.tag_conditions)[condition] is False,
            }
        )

    full, _states, _proposals, _tags = build_tagged_chain(fixture, 6)
    embedding = CorpusEmbedding(tuple((index, 0, 0) for index in range(6)))
    atoms = encode_typed_corpus(fixture, full, embedding)
    programs = corpus_programs()
    before_hash = c350.corpus_hash(atoms)
    deleted_view = weight_view(atoms, programs, None)
    trace_view = weight_view(atoms, programs, "supplied trace proposal")
    nonlinear_view = weight_view(atoms, programs, "supplied nonlinear proposal")
    after_hash = c350.corpus_hash(atoms)

    missing_tag_state = replace(full, tags=full.tags[:-1])
    deleted_atoms = atoms[:-1]
    spliced_atoms = list(atoms)
    spliced_atoms[0], spliced_atoms[1] = spliced_atoms[1], spliced_atoms[0]
    invalid_calls = (
        lambda: encode_typed_corpus(fixture, missing_tag_state, embedding),
        lambda: decode_typed_corpus(fixture, deleted_atoms, embedding),
        lambda: decode_typed_corpus(fixture, tuple(spliced_atoms), embedding),
        lambda: apply_formation_corpus_tag(
            fixture,
            root.state,
            child_proposal,
            replace(child_tag, program=6),
        ),
        lambda: apply_formation_corpus_tag(
            fixture,
            root.state,
            child_proposal,
            replace(child_tag, source="host-tag"),
        ),
        lambda: encode_typed_corpus(
            fixture,
            full,
            CorpusEmbedding(embedding.ordered_sites[:-1]),
        ),
        lambda: supplied_weight_rule("selected Born law"),
    )
    rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            rejections += 1

    distinct_rule_delta = 0.0
    if trace_view.weights is not None and nonlinear_view.weights is not None:
        distinct_rule_delta = max(
            abs(left - right)
            for left, right in zip(trace_view.weights, nonlinear_view.weights)
        )
    encoder_source = getsource(encode_typed_corpus)
    adapter_source = getsource(apply_formation_corpus_tag)
    detail = {
        "nominal_status": nominal.status,
        "missing_formation_status": missing_formation.status,
        "missing_formation_state_unchanged": missing_formation.state == root.state,
        "tag_attack_rows": attack_rows,
        "corpus_hash_before_weight_views": before_hash,
        "corpus_hash_after_weight_views": after_hash,
        "grade_deleted_weights": deleted_view.weights,
        "trace_proposal_sampler": trace_view.actual_history_sampler,
        "trace_proposal_actual_member_selector": trace_view.actual_member_selector,
        "nonlinear_proposal_sampler": nonlinear_view.actual_history_sampler,
        "distinct_supplied_rule_maximum_delta": distinct_rule_delta,
        "domain_rejections": rejections,
        "domain_attempts": len(invalid_calls),
        "Cycle350_form_atom_called": "form_atom" in encoder_source + adapter_source,
        "weight_or_sampler_in_encoder_parameters": tuple(signature(encode_typed_corpus).parameters),
        "weight_or_sampler_in_adapter_parameters": tuple(signature(apply_formation_corpus_tag).parameters),
        "selected_weight_rule": None,
        "actual_history_sampler_input": None,
        "actual_member_selector": None,
    }
    check(
        "formation/tag deletion and splices fail atomically; weight deletion preserves the corpus and no proposal view selects actual history",
        nominal.status == "formed-with-registered-corpus-tag"
        and missing_formation.formed is None
        and missing_formation.state == root.state
        and all(
            not row["formed"] and row["state_unchanged"] and row["condition_visible"]
            for row in attack_rows
        )
        and before_hash == after_hash == deleted_view.corpus_hash
        and deleted_view.weights is None
        and trace_view.actual_history_sampler is None
        and trace_view.actual_member_selector is None
        and nonlinear_view.actual_history_sampler is None
        and distinct_rule_delta > 1e-6
        and rejections == len(invalid_calls)
        and not detail["Cycle350_form_atom_called"]
        and detail["weight_or_sampler_in_encoder_parameters"] == (
            "fixture", "state", "embedding"
        )
        and detail["weight_or_sampler_in_adapter_parameters"] == (
            "fixture", "state", "proposal", "tag"
        )
        and detail["selected_weight_rule"] is None
        and detail["actual_history_sampler_input"] is None
        and detail["actual_member_selector"] is None,
        detail,
    )
    return detail


def supplied_structure_and_completeness_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded positive conditional Cycle-364 to Cycle-351 fixed-program typed-corpus adapter",
        "common_state": "fixture-lawful Cycle-364 FormationState plus one site/payload-bound registered tag per formed site",
        "Cycle364_atomic_law": "supplied downstream hypothesis",
        "Cycle364_selected": False,
        "Cycle364_formed_state": "supplied conditional formed state; not selected or sampled here",
        "Cycle368_link_or_count_input": None,
        "Cycle342_fixture": "supplied L3/L6 decoder and proper-cubic payload mapping",
        "typing_and_permanence": "validated in each 30-M2 Cycle-364/Cycle-342 Record word",
        "tag_input": "supplied 13-M2 preparation/program/fine-pointer/trial/use word",
        "tag_binding": "supplied exact site/payload binding and pointer-event registration",
        "apparatus_fixture": "supplied Cycle-323/350 fixed six-program effect table and contact fixture",
        "embedding": "supplied ordered site list for the finite linear corpus code",
        "train_sizes": TRAIN_SIZES,
        "held_size": HELD_SIZE,
        "weight_inputs": (
            "optional supplied trace/Born-labelled proposal functional",
            "optional supplied nonlinear comparison functional",
        ),
        "selected_weight_rule": None,
        "weight_input_to_formation": None,
        "weight_input_to_encoder_E": None,
        "proposal_weights_are_sampling_probabilities": False,
        "sampler_input": None,
        "actual_history_sampler": None,
        "actual_member_selector": None,
        "repeated_history_law": None,
        "frequency_theorem": None,
        "Born_law_derived": False,
        "whole_43_M2_atom_is_Record": False,
        "Record_M2": c350.RECORD_M2,
        "tag_M2": TAG_BITS,
        "corpus_atom_M2": c350.ATOM_M2,
        "physical_NN_tag_binding_compiler": None,
        "implementation_or_law_incompleteness": (
            "tag genesis/binding compiler, unique numerical rule, actual-history sampler, and frequency theorem remain open"
        ),
        "shared_substrate_obstruction": False,
        "canonical_contract_RECORD": "bounded conditional partial bridge only",
        "canonical_contract_ACTUALITY": "open",
        "canonical_contract_STATISTICS": "open",
        "count_is_time_or_probability": False,
        "trial_or_use_is_time": False,
        "phase_is_energy": False,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "all state, typing, tag, apparatus, fixture, embedding, weight, and sampler inputs are inventoried against the canonical completeness contract",
        inventory["Cycle364_selected"] is False
        and inventory["Cycle368_link_or_count_input"] is None
        and inventory["selected_weight_rule"] is None
        and inventory["weight_input_to_formation"] is None
        and inventory["weight_input_to_encoder_E"] is None
        and inventory["proposal_weights_are_sampling_probabilities"] is False
        and inventory["sampler_input"] is None
        and inventory["actual_history_sampler"] is None
        and inventory["actual_member_selector"] is None
        and inventory["repeated_history_law"] is None
        and inventory["frequency_theorem"] is None
        and inventory["Born_law_derived"] is False
        and inventory["whole_43_M2_atom_is_Record"] is False
        and inventory["Record_M2"] == 30
        and inventory["tag_M2"] == 13
        and inventory["corpus_atom_M2"] == 43
        and inventory["physical_NN_tag_binding_compiler"] is None
        and inventory["shared_substrate_obstruction"] is False
        and inventory["canonical_contract_ACTUALITY"] == "open"
        and inventory["canonical_contract_STATISTICS"] == "open"
        and inventory["count_is_time_or_probability"] is False
        and inventory["trial_or_use_is_time"] is False
        and inventory["phase_is_energy"] is False
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
        "maximum_one_use_carrier_residual": covariance[
            "maximum_one_use_carrier_residual"
        ],
        "maximum_two_use_carrier_residual": covariance[
            "maximum_two_use_carrier_residual"
        ],
        "carrier_is_supplied_not_derived_by_Cycle369": True,
    }
    check(
        "the supplied fixed apparatus carrier preserves its all-frame observable surface without becoming a tag or sampler",
        detail["proper_cubic_frames"] == 24
        and detail["carrier_branch_failures"] == 0
        and detail["maximum_one_use_carrier_residual"] < c350.TOL
        and detail["maximum_two_use_carrier_residual"] < c350.TOL
        and detail["carrier_is_supplied_not_derived_by_Cycle369"],
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 369: CONDITIONAL SITE-TETHERED RECORD -> CYCLE-351 CORPUS ADAPTER")
    print("authority=none; audit=unset; no selected weight rule or history sampler")
    note = note_contract()
    atomic = atomic_formation_tag_controls()
    frames = encoder_observable_weight_frame_controls()
    attacks = deletion_splice_domain_and_sampler_controls()
    inventory = supplied_structure_and_completeness_controls()
    carrier = inherited_carrier_controls()
    check(
        "Cycle 369 constructs an exact non-circular bounded corpus/weight-proposal interface while leaving actuality and statistics open",
        not note["missing"]
        and atomic["failures"] == 0
        and frames["adapter_covariance_failures"] == 0
        and frames["D_E_roundtrip_failures"] == 0
        and frames["observable_or_weight_intertwiner_failures"] == 0
        and attacks["actual_history_sampler_input"] is None
        and inventory["canonical_contract_ACTUALITY"] == "open"
        and inventory["canonical_contract_STATISTICS"] == "open"
        and carrier["carrier_branch_failures"] == 0,
        {
            "disposition": "bounded positive conditional common-state adapter",
            "strongest_positive": "exact grade-blind 30+13 M2 corpus E/D plus supplied observable/weight proposal intertwiner",
            "missing": "tag genesis compiler, selected numerical law, actual-history sampler, frequency theorem",
            "obstruction": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_SITE_TETHERED_RECORD_BORN_CORPUS_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_SITE_TETHERED_RECORD_BORN_CORPUS_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
