#!/usr/bin/env python3
"""Cycle 376: migrating Cycle-365 Record -> grade-blind Cycle-351 corpus.

One physical 43-M2 corpus block is rooted next to each immutable Cycle-365
root-endpoint site.  Its first 30 M2 contain the component's lawful Record
word and its remaining 13 M2 contain the supplied preparation, program,
fine-pointer, trial and use tag.  The endpoint coordinate is geometry, not a
value-valued ID in the block.  Binding is checked only against the active
root carrier or first source-origin bond in the endpoint's bounded local
neighbourhood; the adapter never walks or scans the worldline component.

The exact finite maps are A (physical source and rooted blocks to a common
state), E (common state to Cycle-351-compatible atoms), and D (atoms plus the
explicit physical embedding back to the common state).  On the declared code
space A is invariant under one- and two-step Cycle-365 history recodings,
D E A = A, and the corpus, trial/use addresses, hash, observables, and both
supplied proposal-weight views are invariant.  A cleared endpoint carrier
reused at its second physical root slot adds exactly one new atom/address.

No grade or sampler enters formation, A, E, or D.  The trace-labelled and
nonlinear weights are downstream supplied proposal views only.  The sampler
and member selector are None.  Cycle 365 remains unselected; no Born law,
frequency theorem, no-go, or axiom pressure is claimed.  Authority is none
and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from inspect import getsource, signature
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MIGRATING_RECORD_BORN_CORPUS_ADAPTER_"
    "CYCLE376_NOTE_2026-07-18.md"
)

import physical_migrating_invariant_fact_record_formation_candidate_cycle365_2026_07_18 as c365
import physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18 as c350


Coord = c365.Coord
Word = c365.Word
LENGTHS = (3, 6)
TRAIN_SIZES = (6, 12)
HELD_SIZE = 18
SIZES = TRAIN_SIZES + (HELD_SIZE,)
TAG_BITS = c350.ATOM_M2 - c350.RECORD_M2
ATOM_BITS = c350.ATOM_M2
BLOCK_SOURCE = "Cycle-376 supplied physical endpoint-rooted Cycle-351 corpus block"
COMMON_SOURCE = "Cycle-376 endpoint-rooted grade-blind corpus common state"
EMBEDDING_SOURCE = "Cycle-376 explicit ordered physical root/block embedding"
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


def is_bit(value: object) -> bool:
    return value in (0, 1) and (
        isinstance(value, bool)
        or isinstance(value, int) and not isinstance(value, bool)
    )


def distance(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def integer(word: Word) -> int:
    if any(not is_bit(item) for item in word):
        raise ValueError("an M2 word must be binary")
    return sum(int(item) << index for index, item in enumerate(word))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


@dataclass(frozen=True)
class TagRegistration:
    preparation: int
    program: int
    fine_pointer: int
    trial: int
    use: int
    pointer_event_registered: int = 1
    source: str = BLOCK_SOURCE


@dataclass(frozen=True)
class EndpointCorpusBlock:
    root_endpoint: Coord
    sites: tuple[Coord, ...]
    word: Word
    pointer_event_registered: int = 1
    source: str = BLOCK_SOURCE


@dataclass(frozen=True)
class TaggedWorldlineState:
    source: c365.BasisState
    blocks: tuple[EndpointCorpusBlock, ...] = ()


@dataclass(frozen=True)
class FormationTagAnswer:
    state: TaggedWorldlineState
    formed: c365.InvariantFactRecord | None
    status: str
    tag_conditions: tuple[tuple[str, bool], ...]


@dataclass(frozen=True)
class BoundCorpusAtom:
    root_endpoint: Coord
    sites: tuple[Coord, ...]
    word: Word


@dataclass(frozen=True)
class CommonCorpusState:
    atoms: tuple[BoundCorpusAtom, ...]
    source: str = COMMON_SOURCE


@dataclass(frozen=True)
class CorpusEmbedding:
    ordered_roots: tuple[Coord, ...]
    block_sites: tuple[tuple[Coord, ...], ...]
    source: str = EMBEDDING_SOURCE


@dataclass(frozen=True)
class ProposalWeightView:
    corpus_hash: str
    proposal_rule: str | None
    weights: tuple[float, ...] | None
    actual_history_sampler: None = None
    actual_member_selector: None = None


@dataclass(frozen=True)
class SourceFixture:
    initial: TaggedWorldlineState
    migrated: TaggedWorldlineState
    history: TaggedWorldlineState
    embedding: CorpusEmbedding
    first_migration_statuses: tuple[str, ...]
    second_migration_statuses: tuple[str, ...]


def canonical_blocks(
    blocks: tuple[EndpointCorpusBlock, ...],
) -> tuple[EndpointCorpusBlock, ...]:
    return tuple(sorted(blocks, key=lambda item: item.root_endpoint))


def schedule_fields(ordinal: int) -> tuple[int, int, int, int, int]:
    """Use the Cycle-351 2+3+3+4+1 widths through 32 addresses.

    Trial/use is the explicit five-bit corpus address.  This extends the
    existing finite atom schema to held N=18; it does not change any field
    width or claim that use is time.
    """

    if not isinstance(ordinal, int) or isinstance(ordinal, bool) or not 0 <= ordinal < 32:
        raise ValueError("the finite Cycle-376 corpus address is outside five M2")
    program = ordinal % c350.c323.LAWFUL_PROGRAMS
    fine_pointer = (ordinal // c350.c323.LAWFUL_PROGRAMS + program) % (
        c350.PROGRAM_FINE_LABELS[program]
    )
    return (
        ordinal % 4,
        program,
        fine_pointer,
        ordinal % 16,
        ordinal // 16,
    )


def scheduled_registration(ordinal: int) -> TagRegistration:
    return TagRegistration(*schedule_fields(ordinal))


def validate_registration(registration: TagRegistration) -> None:
    if not isinstance(registration, TagRegistration):
        raise TypeError("formation needs one explicit TagRegistration")
    if registration.source != BLOCK_SOURCE:
        raise ValueError("the endpoint tag has the wrong supplied source")
    if registration.pointer_event_registered not in (0, 1):
        raise ValueError("pointer-event registration is outside its predicate domain")
    values = (
        registration.preparation,
        registration.program,
        registration.fine_pointer,
        registration.trial,
        registration.use,
    )
    if any(not isinstance(item, int) or isinstance(item, bool) for item in values):
        raise ValueError("tag fields must be finite integer labels")
    if (
        not 0 <= registration.preparation < 4
        or not 0 <= registration.program < c350.c323.LAWFUL_PROGRAMS
        or not 0 <= registration.fine_pointer < c350.PROGRAM_FINE_LABELS[registration.program]
        or not 0 <= registration.trial < 16
        or registration.use not in (0, 1)
    ):
        raise ValueError("tag fields are outside the 13-M2 Cycle-351 domain")


def registration_word(registration: TagRegistration) -> Word:
    validate_registration(registration)
    word = (
        c350.bits(registration.preparation, c350.PREPARATION_M2)
        + c350.bits(registration.program, c350.PROGRAM_M2)
        + c350.bits(registration.fine_pointer, c350.FINE_POINTER_M2)
        + c350.bits(registration.trial, c350.TRIAL_M2)
        + (registration.use,)
    )
    if len(word) != TAG_BITS:
        raise RuntimeError("the Cycle-351 apparatus-tag width drifted")
    return word


def atom_from_word(word: Word) -> c350.CorpusAtom:
    if not isinstance(word, tuple) or len(word) != ATOM_BITS or any(not is_bit(item) for item in word):
        raise ValueError("a rooted corpus block needs one binary 43-M2 word")
    record = c365.c342.decode_record_word(word[: c365.RECORD_BITS])
    cursor = c365.RECORD_BITS

    def take(width: int) -> int:
        nonlocal cursor
        output = integer(word[cursor : cursor + width])
        cursor += width
        return output

    atom = c350.CorpusAtom(
        record,
        take(c350.PREPARATION_M2),
        take(c350.PROGRAM_M2),
        take(c350.FINE_POINTER_M2),
        take(c350.TRIAL_M2),
        take(c350.USE_M2),
    )
    if cursor != ATOM_BITS or c350.atom_word(atom) != word:
        raise ValueError("the 43-M2 corpus block did not decode exactly")
    return atom


def atom_word(payload: Word, registration: TagRegistration) -> Word:
    if (
        not isinstance(payload, tuple)
        or len(payload) != c365.RECORD_BITS
        or any(not is_bit(item) for item in payload)
    ):
        raise ValueError("the endpoint block needs one complete 30-M2 Record word")
    word = payload + registration_word(registration)
    atom_from_word(word)
    return word


def frame_matrix(layout: c365.Layout) -> np.ndarray:
    matrix = np.asarray(layout.frame, dtype=int).reshape(3, 3)
    if not c365.proper_frame(matrix):
        raise ValueError("the source layout lost its proper-cubic frame")
    return matrix


def endpoint_block_sites(source: c365.BasisState, root_endpoint: Coord) -> tuple[Coord, ...]:
    if root_endpoint not in {site.coord for site in source.layout.sites}:
        raise ValueError("a corpus block must anchor at an installed physical endpoint")
    axis = c365.c362.c353.rotated((0, 0, 1), frame_matrix(source.layout))
    return tuple(
        tuple(root_endpoint[index] + step * axis[index] for index in range(3))
        for step in range(1, ATOM_BITS + 1)
    )


def physical_root_table(source: c365.BasisState) -> dict[Coord, tuple[int, int]]:
    """Read only the fixed endpoint marker sites, never the component graph."""

    roots: dict[Coord, tuple[int, int]] = {}
    for carrier in range(source.layout.size):
        view = c365.carrier_view(source, carrier)
        for slot, marker in enumerate(view.endpoint_markers):
            if not marker:
                continue
            site = source.layout.carriers[carrier].sites[c365.CARRIER_ENDPOINT_LANES[slot]]
            coord = source.layout.sites[site].coord
            if coord in roots:
                raise ValueError("two physical root slots alias one endpoint coordinate")
            roots[coord] = (carrier, slot)
    return roots


def root_attachment_content(source: c365.BasisState, carrier: int, slot: int) -> Word:
    """Bind at radius one: root carrier or its first source-origin bond only."""

    attachments: list[Word] = []
    view = c365.carrier_view(source, carrier)
    if view.present and view.root_origin and view.root_slot == slot:
        attachments.append(view.content)
    for bond_index in (carrier - 1, carrier):
        if not 0 <= bond_index < source.layout.size - 1:
            continue
        bond = c365.bond_view(source, bond_index)
        if not bond.used or not bond.source_origin or bond.root_slot != slot:
            continue
        bond_source, _destination = c365.bond_endpoints(bond_index, bond)
        if bond_source == carrier:
            attachments.append(bond.content)
    if len(attachments) != 1:
        raise ValueError("a physical root endpoint needs exactly one local component attachment")
    return attachments[0]


def block_map(state: TaggedWorldlineState) -> dict[Coord, EndpointCorpusBlock]:
    return {item.root_endpoint: item for item in state.blocks}


def validate_tagged_state(state: TaggedWorldlineState) -> None:
    if not isinstance(state, TaggedWorldlineState):
        raise TypeError("the adapter needs one TaggedWorldlineState")
    c365.validate_state(state.source)
    if c365.local_constraint_failures(state.source):
        raise ValueError("the Cycle-365 source is outside its locally constrained code space")
    if not isinstance(state.blocks, tuple) or state.blocks != canonical_blocks(state.blocks):
        raise ValueError("endpoint blocks must be an immutable canonical tuple")
    roots = physical_root_table(state.source)
    blocks = block_map(state)
    if len(blocks) != len(state.blocks) or set(blocks) != set(roots):
        raise ValueError("every and only physical root endpoints need one corpus block")
    source_coords = {site.coord for site in state.source.layout.sites}
    installed_block_coords: set[Coord] = set()
    addresses = set()
    for root, block in blocks.items():
        if block.source != BLOCK_SOURCE or block.pointer_event_registered != 1:
            raise ValueError("endpoint block lacks the supplied registration predicate")
        if block.sites != endpoint_block_sites(state.source, root):
            raise ValueError("the 43-M2 block is not physically rooted at its endpoint")
        if any(site in source_coords or site in installed_block_coords for site in block.sites):
            raise ValueError("endpoint corpus blocks overlap the source or one another")
        if distance(root, block.sites[0]) != 1 or any(
            distance(left, right) != 1 for left, right in zip(block.sites, block.sites[1:])
        ):
            raise ValueError("the endpoint corpus block is not a connected NN path")
        installed_block_coords.update(block.sites)
        carrier, slot = roots[root]
        if block.word[: c365.RECORD_BITS] != root_attachment_content(state.source, carrier, slot):
            raise ValueError("the root-local component content and corpus block disagree")
        atom = atom_from_word(block.word)
        if (
            not atom.record.typed
            or not atom.record.permanent
            or not c365.c342.cylinder_is_lawful(state.source.layout.fixture, atom.record.cylinder)
        ):
            raise ValueError("the endpoint block does not contain a lawful typed Record word")
        address = (atom.trial, atom.use)
        if address in addresses:
            raise ValueError("two endpoint blocks alias one trial/use address")
        addresses.add(address)


def make_endpoint_block(
    source: c365.BasisState,
    root_endpoint: Coord,
    payload: Word,
    registration: TagRegistration,
) -> EndpointCorpusBlock:
    return EndpointCorpusBlock(
        root_endpoint,
        endpoint_block_sites(source, root_endpoint),
        atom_word(payload, registration),
        registration.pointer_event_registered,
        registration.source,
    )


def apply_registered_formation(
    state: TaggedWorldlineState,
    proposal: c365.FormationProposal,
    seed: c365.IdentitySeed,
    registration: TagRegistration,
) -> FormationTagAnswer:
    """Atomic Cycle-365 formation plus local endpoint-block registration."""

    validate_tagged_state(state)
    validate_registration(registration)
    formation = c365.apply_formation(state.source, proposal, seed)
    target = state.source.layout.anchors.index(proposal.site)
    endpoint_site = state.source.layout.carriers[target].sites[
        c365.CARRIER_ENDPOINT_LANES[seed.local_root_slot]
    ]
    root = state.source.layout.sites[endpoint_site].coord
    expected = scheduled_registration(len(state.blocks))
    existing_addresses = {
        (atom_from_word(block.word).trial, atom_from_word(block.word).use)
        for block in state.blocks
    }
    conditions = (
        ("formation_succeeded", formation.status == "formed"),
        ("pointer_event_registered", registration.pointer_event_registered == 1),
        ("scheduled_grade_blind_fields", registration == expected),
        ("fresh_physical_root", root not in block_map(state)),
        ("fresh_trial_use_address", (registration.trial, registration.use) not in existing_addresses),
    )
    failed = tuple(name for name, value in conditions if not value)
    if failed:
        return FormationTagAnswer(state, None, "blocked:" + ",".join(failed), conditions)
    block = make_endpoint_block(formation.state, root, proposal.payload, registration)
    output = TaggedWorldlineState(
        formation.state,
        canonical_blocks(state.blocks + (block,)),
    )
    validate_tagged_state(output)
    return FormationTagAnswer(output, formation.formed, "formed-with-endpoint-corpus-block", conditions)


def embedding_for(state: TaggedWorldlineState, ordered_roots: tuple[Coord, ...]) -> CorpusEmbedding:
    blocks = block_map(state)
    if set(ordered_roots) != set(blocks) or len(ordered_roots) != len(blocks):
        raise ValueError("the embedding must name every rooted block exactly once")
    return CorpusEmbedding(
        ordered_roots,
        tuple(blocks[root].sites for root in ordered_roots),
    )


def validate_embedding(state: TaggedWorldlineState, embedding: CorpusEmbedding) -> None:
    if not isinstance(embedding, CorpusEmbedding):
        raise TypeError("A needs one explicit CorpusEmbedding")
    if embedding.source != EMBEDDING_SOURCE:
        raise ValueError("the corpus embedding has the wrong supplied source")
    if (
        not isinstance(embedding.ordered_roots, tuple)
        or not embedding.ordered_roots
        or len(set(embedding.ordered_roots)) != len(embedding.ordered_roots)
        or any(not c365.valid_coord(item) for item in embedding.ordered_roots)
        or not isinstance(embedding.block_sites, tuple)
        or len(embedding.block_sites) != len(embedding.ordered_roots)
    ):
        raise ValueError("the ordered endpoint/block embedding is outside its finite domain")
    blocks = block_map(state)
    if set(embedding.ordered_roots) != set(blocks):
        raise ValueError("the embedding omits or adds a physical endpoint block")
    if any(blocks[root].sites != sites for root, sites in zip(embedding.ordered_roots, embedding.block_sites)):
        raise ValueError("the embedding splices a block away from its root endpoint")


def validate_common(
    fixture: c365.c342.c338.RouteFixture,
    common: CommonCorpusState,
) -> None:
    if not isinstance(common, CommonCorpusState) or common.source != COMMON_SOURCE:
        raise TypeError("E/D need one Cycle-376 CommonCorpusState")
    if not isinstance(common.atoms, tuple) or not 1 <= len(common.atoms) <= 32:
        raise ValueError("the common corpus has the wrong finite cardinality")
    roots = tuple(item.root_endpoint for item in common.atoms)
    if len(set(roots)) != len(roots) or any(not c365.valid_coord(item) for item in roots):
        raise ValueError("common atoms need unique physical root endpoints")
    all_sites: set[Coord] = set()
    decoded = []
    addresses = []
    for ordinal, bound in enumerate(common.atoms):
        if (
            not isinstance(bound.sites, tuple)
            or len(bound.sites) != ATOM_BITS
            or distance(bound.root_endpoint, bound.sites[0]) != 1
            or any(distance(left, right) != 1 for left, right in zip(bound.sites, bound.sites[1:]))
            or any(site in all_sites for site in bound.sites)
        ):
            raise ValueError("common block geometry is not a disjoint rooted NN path")
        all_sites.update(bound.sites)
        atom = atom_from_word(bound.word)
        fields = (atom.preparation, atom.program, atom.fine_pointer, atom.trial, atom.use)
        if fields != schedule_fields(ordinal):
            raise ValueError("the common atom does not match its supplied finite address schedule")
        if (
            not atom.record.typed
            or not atom.record.permanent
            or not c365.c342.cylinder_is_lawful(fixture, atom.record.cylinder)
        ):
            raise ValueError("the common atom Record field is not fixture-lawful")
        decoded.append(atom.record)
        addresses.append((atom.trial, atom.use))
    if len(set(addresses)) != len(addresses):
        raise ValueError("common atoms contain a trial/use alias")
    if not c365.c342.valid_chain(fixture, tuple(decoded)):
        raise ValueError("common Record fields do not form the supplied lawful chain")


def adapt_common_state(
    state: TaggedWorldlineState,
    embedding: CorpusEmbedding,
) -> CommonCorpusState:
    """A: read the rooted blocks, never traverse the worldline graph."""

    validate_tagged_state(state)
    validate_embedding(state, embedding)
    blocks = block_map(state)
    common = CommonCorpusState(tuple(
        BoundCorpusAtom(root, blocks[root].sites, blocks[root].word)
        for root in embedding.ordered_roots
    ))
    validate_common(state.source.layout.fixture, common)
    return common


def encode_typed_corpus(
    fixture: c365.c342.c338.RouteFixture,
    common: CommonCorpusState,
) -> tuple[c350.CorpusAtom, ...]:
    """E: exact grade-, weight-, and sampler-blind corpus encoder."""

    validate_common(fixture, common)
    return tuple(atom_from_word(item.word) for item in common.atoms)


def decode_typed_corpus(
    fixture: c365.c342.c338.RouteFixture,
    atoms: tuple[c350.CorpusAtom, ...],
    embedding: CorpusEmbedding,
) -> CommonCorpusState:
    """D: exact decoder using the same explicit physical block embedding."""

    if (
        not isinstance(atoms, tuple)
        or not isinstance(embedding, CorpusEmbedding)
        or embedding.source != EMBEDDING_SOURCE
        or len(atoms) != len(embedding.ordered_roots)
        or len(atoms) != len(embedding.block_sites)
    ):
        raise ValueError("D received mismatched atoms and physical embedding")
    common = CommonCorpusState(tuple(
        BoundCorpusAtom(root, sites, c350.atom_word(atom))
        for root, sites, atom in zip(embedding.ordered_roots, embedding.block_sites, atoms)
    ))
    validate_common(fixture, common)
    return common


def corpus_hash(atoms: tuple[c350.CorpusAtom, ...]) -> str:
    return sha256(bytes(bit for atom in atoms for bit in c350.atom_word(atom))).hexdigest()


def corpus_programs() -> tuple[c350.c321.Program, ...]:
    fixture = c350.c317.physical_fixture(3)
    return c350.c323.make_programs(fixture.contact)


def common_observables(
    common: CommonCorpusState,
    programs: tuple[c350.c321.Program, ...],
) -> tuple[np.ndarray, ...]:
    return tuple(c350.atom_effect(atom_from_word(item.word), programs) for item in common.atoms)


def supplied_weight_rule(name: str):
    rules = {
        "supplied trace proposal": c350.born_trace_grade,
        "supplied nonlinear proposal": c350.nonlinear_grade,
    }
    if name not in rules:
        raise ValueError("weight proposal is outside the two-view comparison menu")
    return rules[name]


def weight_view(
    atoms: tuple[c350.CorpusAtom, ...],
    programs: tuple[c350.c321.Program, ...],
    proposal_rule: str | None,
) -> ProposalWeightView:
    digest = corpus_hash(atoms)
    if proposal_rule is None:
        return ProposalWeightView(digest, None, None)
    rule = supplied_weight_rule(proposal_rule)
    weights = tuple(float(rule(c350.atom_effect(atom, programs), atom.preparation)) for atom in atoms)
    return ProposalWeightView(digest, proposal_rule, weights)


def common_weight_view(
    common: CommonCorpusState,
    programs: tuple[c350.c321.Program, ...],
    proposal_rule: str,
) -> ProposalWeightView:
    rule = supplied_weight_rule(proposal_rule)
    atoms = tuple(atom_from_word(item.word) for item in common.atoms)
    observables = common_observables(common, programs)
    weights = tuple(float(rule(observable, atom.preparation)) for observable, atom in zip(observables, atoms))
    return ProposalWeightView(corpus_hash(atoms), proposal_rule, weights)


def build_source_fixture(
    fixture: c365.c342.c338.RouteFixture,
    count: int,
) -> SourceFixture:
    if count not in SIZES:
        raise ValueError("source count is outside the N6/N12/held-N18 domain")
    layout = c365.build_layout(fixture, 3 * count, np.eye(3, dtype=int))
    payloads = c365.words(fixture, count)
    state = TaggedWorldlineState(c365.blank_state(layout))
    ordered_roots = []
    for ordinal, payload in enumerate(payloads):
        carrier = 3 * ordinal
        answer = apply_registered_formation(
            state,
            c365.proposal(layout, carrier, payload),
            c365.IdentitySeed(0),
            scheduled_registration(ordinal),
        )
        if answer.status != "formed-with-endpoint-corpus-block":
            raise RuntimeError(("rooted corpus fixture failed", ordinal, answer.status))
        state = answer.state
        endpoint_site = layout.carriers[carrier].sites[c365.CARRIER_ENDPOINT_LANES[0]]
        ordered_roots.append(layout.sites[endpoint_site].coord)
    initial = state
    first_requests = tuple(
        c365.RecodingRequest(
            3 * ordinal,
            3 * ordinal + 1,
            c365.proposal(layout, 3 * ordinal + 1, payload, (3 * ordinal,)),
        )
        for ordinal, payload in enumerate(payloads)
    )
    first = c365.apply_recoding_batch(initial.source, first_requests)
    migrated = TaggedWorldlineState(first.state, initial.blocks)
    validate_tagged_state(migrated)
    second_requests = tuple(
        c365.RecodingRequest(
            3 * ordinal + 1,
            3 * ordinal + 2,
            c365.proposal(layout, 3 * ordinal + 2, payload, (3 * ordinal + 1,)),
        )
        for ordinal, payload in enumerate(payloads)
    )
    second = c365.apply_recoding_batch(migrated.source, second_requests)
    history = TaggedWorldlineState(second.state, initial.blocks)
    validate_tagged_state(history)
    return SourceFixture(
        initial,
        migrated,
        history,
        embedding_for(initial, tuple(ordered_roots)),
        first.statuses,
        second.statuses,
    )


def transform_coord(coord: Coord, frame: np.ndarray) -> Coord:
    return c365.c362.c353.rotated(coord, frame)


def transform_tagged_state(
    state: TaggedWorldlineState,
    frame: np.ndarray,
) -> TaggedWorldlineState:
    layout = c365.build_layout(state.source.layout.fixture, state.source.layout.size, frame)
    blocks = canonical_blocks(tuple(
        replace(
            block,
            root_endpoint=transform_coord(block.root_endpoint, frame),
            sites=tuple(transform_coord(site, frame) for site in block.sites),
        )
        for block in state.blocks
    ))
    output = TaggedWorldlineState(c365.BasisState(layout, state.source.bits), blocks)
    validate_tagged_state(output)
    return output


def transform_embedding(embedding: CorpusEmbedding, frame: np.ndarray) -> CorpusEmbedding:
    return CorpusEmbedding(
        tuple(transform_coord(root, frame) for root in embedding.ordered_roots),
        tuple(tuple(transform_coord(site, frame) for site in sites) for sites in embedding.block_sites),
    )


def transform_fixture(source: SourceFixture, frame: np.ndarray) -> SourceFixture:
    return SourceFixture(
        transform_tagged_state(source.initial, frame),
        transform_tagged_state(source.migrated, frame),
        transform_tagged_state(source.history, frame),
        transform_embedding(source.embedding, frame),
        source.first_migration_statuses,
        source.second_migration_statuses,
    )


def transform_common(common: CommonCorpusState, frame: np.ndarray) -> CommonCorpusState:
    return CommonCorpusState(tuple(
        BoundCorpusAtom(
            transform_coord(item.root_endpoint, frame),
            tuple(transform_coord(site, frame) for site in item.sites),
            item.word,
        )
        for item in common.atoms
    ))


def root_marker_count(state: c365.BasisState) -> int:
    return sum(
        sum(c365.carrier_view(state, carrier).endpoint_markers)
        for carrier in range(state.layout.size)
    )


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-376 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "physical endpoint-rooted component identity",
        "no transported id",
        "no host-side worldline scan",
        "migration and history recoding leave the corpus, trial/use addresses, and hash invariant",
        "endpoint-carrier reuse adds exactly one distinct atom and trial/use address",
        "train sizes n=6 and n=12",
        "held-out size n=18",
        "all 24 proper-cubic spatial frames",
        "sampler and actual-member selector are none",
        "no born-law claim",
        "the whole 43-m2 block is not an additional record",
        "law/interface incompleteness, not an obstruction",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the endpoint binding, migration invariant, finite domain, and Born firewall",
        not missing,
        missing,
    )
    return {"missing": missing}


def migration_frame_intertwiner_controls() -> dict[str, object]:
    programs = corpus_programs()
    frames = c365.c362.c353.proper_cubic_frames()
    cases = atom_cases = held_cases = held_atoms = 0
    source_constraint_failures = local_binding_failures = 0
    migration_common_failures = migration_corpus_failures = migration_hash_failures = 0
    trial_address_failures = covariance_failures = roundtrip_failures = 0
    field_leakage = observable_failures = weight_failures = geometry_failures = 0
    history_cardinality_failures = 0
    maximum_observable_residual = maximum_weight_residual = 0.0
    rows = []
    proposal_names = ("supplied trace proposal", "supplied nonlinear proposal")
    for length in LENGTHS:
        fixture = c365.c342.c338.build_fixture(length)
        base_sources = {count: build_source_fixture(fixture, count) for count in SIZES}
        base_common = {
            count: adapt_common_state(item.history, item.embedding)
            for count, item in base_sources.items()
        }
        base_hashes = {
            count: corpus_hash(encode_typed_corpus(fixture, common))
            for count, common in base_common.items()
        }
        for frame in frames:
            for count in SIZES:
                source = transform_fixture(base_sources[count], frame)
                phases = (source.initial, source.migrated, source.history)
                source_constraint_failures += sum(c365.local_constraint_failures(item.source) for item in phases)
                try:
                    for item in phases:
                        validate_tagged_state(item)
                except (TypeError, ValueError):
                    local_binding_failures += 1
                    continue
                commons = tuple(adapt_common_state(item, source.embedding) for item in phases)
                corpora = tuple(encode_typed_corpus(fixture, common) for common in commons)
                hashes = tuple(corpus_hash(atoms) for atoms in corpora)
                addresses = tuple(tuple((atom.trial, atom.use) for atom in atoms) for atoms in corpora)
                migration_common_failures += int(not commons[0] == commons[1] == commons[2])
                migration_corpus_failures += int(not corpora[0] == corpora[1] == corpora[2])
                migration_hash_failures += int(not hashes[0] == hashes[1] == hashes[2] == base_hashes[count])
                trial_address_failures += int(not addresses[0] == addresses[1] == addresses[2])
                expected = transform_common(base_common[count], frame)
                covariance_failures += int(commons[2] != expected)
                roundtrip_failures += int(decode_typed_corpus(fixture, corpora[2], source.embedding) != commons[2])
                for bound, atom in zip(commons[2].atoms, corpora[2]):
                    word = c350.atom_word(atom)
                    field_leakage += int(word != bound.word)
                    atom_cases += 1
                    held_atoms += int(length == 6 and count == HELD_SIZE)
                common_effects = common_observables(commons[2], programs)
                corpus_effects = tuple(c350.atom_effect(atom, programs) for atom in corpora[2])
                for left, right in zip(common_effects, corpus_effects):
                    residual = float(np.linalg.norm(left - right))
                    maximum_observable_residual = max(maximum_observable_residual, residual)
                    observable_failures += int(residual > 1e-12)
                for name in proposal_names:
                    common_view = common_weight_view(commons[2], programs, name)
                    corpus_view = weight_view(corpora[2], programs, name)
                    if common_view.weights is None or corpus_view.weights is None:
                        maximum_weight_residual = float("inf")
                    else:
                        residual = max(abs(left - right) for left, right in zip(common_view.weights, corpus_view.weights))
                        maximum_weight_residual = max(maximum_weight_residual, residual)
                    weight_failures += int(common_view != corpus_view)
                base_layout = base_sources[count].history.source.layout
                geometry_failures += sum(
                    transform_coord(site.coord, frame) != rotated.coord
                    for site, rotated in zip(base_layout.sites, source.history.source.layout.sites)
                )
                facts = tuple(len(c365.occupied_fact_nodes(item.source)) for item in phases)
                history_cardinality_failures += int(
                    facts != (count, 2 * count, 3 * count)
                    or any(root_marker_count(item.source) != count for item in phases)
                    or any(len(common.atoms) != count for common in commons)
                )
                cases += 1
                held_cases += int(length == 6 and count == HELD_SIZE)
                if np.array_equal(frame, np.eye(3, dtype=int)):
                    rows.append({
                        "L": length,
                        "N": count,
                        "held": length == 6 and count == HELD_SIZE,
                        "fact_nodes_initial_migrated_history": facts,
                        "rooted_corpus_atoms": len(corpora[2]),
                        "unique_trial_use_addresses": len(set(addresses[2])),
                        "hash": hashes[2],
                        "source_M2": len(source.history.source.layout.sites),
                        "rooted_block_M2": count * ATOM_BITS,
                    })
    detail = {
        "rows": rows,
        "L_by_N_by_frame_cases": cases,
        "L_by_N_by_frame_atom_cases": atom_cases,
        "proper_cubic_frames": len(frames),
        "held_L6_N18_cases": held_cases,
        "held_L6_N18_atom_cases": held_atoms,
        "Cycle365_source_constraint_failures": source_constraint_failures,
        "root_local_binding_failures": local_binding_failures,
        "migration_common_state_failures": migration_common_failures,
        "migration_corpus_failures": migration_corpus_failures,
        "migration_hash_failures": migration_hash_failures,
        "migration_trial_use_address_failures": trial_address_failures,
        "proper_cubic_covariance_failures": covariance_failures,
        "D_E_A_roundtrip_failures": roundtrip_failures,
        "30_plus_13_field_leakage": field_leakage,
        "observable_intertwiner_failures": observable_failures,
        "proposal_weight_intertwiner_failures": weight_failures,
        "physical_geometry_failures": geometry_failures,
        "history_double_count_failures": history_cardinality_failures,
        "maximum_observable_residual": maximum_observable_residual,
        "maximum_proposal_weight_residual": maximum_weight_residual,
        "intertwiners": (
            "A(initial)=A(migrated)=A(two-segment history)",
            "D E A=A",
            "O_common=O_Cycle351 E",
            "W_trace,common=W_trace,Cycle351 E",
            "W_nonlinear,common=W_nonlinear,Cycle351 E",
        ),
    }
    check(
        "A/E/D, corpus/trial/hash invariance, observables, and both weight views are exact at L3/L6 N6/N12/held-N18 in all 24 frames",
        len(frames) == 24
        and cases == len(LENGTHS) * len(SIZES) * len(frames)
        and atom_cases == len(LENGTHS) * sum(SIZES) * len(frames)
        and held_cases == 24
        and held_atoms == HELD_SIZE * 24
        and source_constraint_failures
        == local_binding_failures
        == migration_common_failures
        == migration_corpus_failures
        == migration_hash_failures
        == trial_address_failures
        == covariance_failures
        == roundtrip_failures
        == field_leakage
        == observable_failures
        == weight_failures
        == geometry_failures
        == history_cardinality_failures
        == 0
        and maximum_observable_residual == maximum_weight_residual == 0.0,
        detail,
    )
    return detail


def endpoint_carrier_reuse_controls() -> dict[str, object]:
    fixture = c365.c342.c338.build_fixture(3)
    source = build_source_fixture(fixture, 6)
    before_common = adapt_common_state(source.history, source.embedding)
    before_atoms = encode_typed_corpus(fixture, before_common)
    before_addresses = tuple((atom.trial, atom.use) for atom in before_atoms)
    before_hash = corpus_hash(before_atoms)
    new_payload = c365.words(fixture, 7)[-1]
    answer = apply_registered_formation(
        source.history,
        c365.proposal(source.history.source.layout, 0, new_payload),
        c365.IdentitySeed(1),
        scheduled_registration(6),
    )
    root_site = source.history.source.layout.carriers[0].sites[c365.CARRIER_ENDPOINT_LANES[1]]
    new_root = source.history.source.layout.sites[root_site].coord
    extended_embedding = embedding_for(
        answer.state,
        source.embedding.ordered_roots + (new_root,),
    )
    after_common = adapt_common_state(answer.state, extended_embedding)
    after_atoms = encode_typed_corpus(fixture, after_common)
    after_addresses = tuple((atom.trial, atom.use) for atom in after_atoms)
    new_atoms = tuple(atom for atom in after_atoms if atom not in before_atoms)
    new_addresses = set(after_addresses) - set(before_addresses)
    detail = {
        "cleared_endpoint_carrier_blank_before_reuse": c365.carrier_blank(source.history.source, 0),
        "reuse_status": answer.status,
        "Cycle365_constraints_after_reuse": c365.local_constraint_failures(answer.state.source),
        "root_endpoints_before_after": (root_marker_count(source.history.source), root_marker_count(answer.state.source)),
        "worldline_fact_nodes_before_after": (
            len(c365.occupied_fact_nodes(source.history.source)),
            len(c365.occupied_fact_nodes(answer.state.source)),
        ),
        "corpus_atoms_before_after": (len(before_atoms), len(after_atoms)),
        "prior_atoms_preserved_exactly": after_atoms[:-1] == before_atoms,
        "distinct_new_atoms": len(new_atoms),
        "distinct_new_trial_use_addresses": len(new_addresses),
        "new_address": tuple(sorted(new_addresses)),
        "hash_changed_by_exact_append": before_hash != corpus_hash(after_atoms),
        "old_root_ID_transported_to_reused_carrier": False,
    }
    check(
        "reuse of the cleared physical endpoint carrier at its second root slot adds exactly one distinct atom and trial/use address",
        detail["cleared_endpoint_carrier_blank_before_reuse"]
        and detail["reuse_status"] == "formed-with-endpoint-corpus-block"
        and detail["Cycle365_constraints_after_reuse"] == 0
        and detail["root_endpoints_before_after"] == (6, 7)
        and detail["worldline_fact_nodes_before_after"] == (18, 19)
        and detail["corpus_atoms_before_after"] == (6, 7)
        and detail["prior_atoms_preserved_exactly"]
        and detail["distinct_new_atoms"] == 1
        and detail["distinct_new_trial_use_addresses"] == 1
        and detail["hash_changed_by_exact_append"]
        and not detail["old_root_ID_transported_to_reused_carrier"],
        detail,
    )
    return detail


def mutate_source_bit(state: TaggedWorldlineState, site: int, value: int) -> TaggedWorldlineState:
    bits = list(state.source.bits)
    bits[site] = value
    return replace(state, source=replace(state.source, bits=tuple(bits)))


def rejected(callable_) -> bool:
    try:
        callable_()
    except (TypeError, ValueError, RuntimeError):
        return True
    return False


def deletion_leakage_domain_sampler_controls() -> dict[str, object]:
    fixture = c365.c342.c338.build_fixture(3)
    source = build_source_fixture(fixture, 6)
    state = source.history
    common = adapt_common_state(state, source.embedding)
    atoms = encode_typed_corpus(fixture, common)
    programs = corpus_programs()
    digest = corpus_hash(atoms)
    deleted_grade = weight_view(atoms, programs, None)
    trace_view = weight_view(atoms, programs, "supplied trace proposal")
    nonlinear_view = weight_view(atoms, programs, "supplied nonlinear proposal")

    root_marker_site = state.source.layout.carriers[0].sites[c365.CARRIER_ENDPOINT_LANES[0]]
    deleted_root_marker = mutate_source_bit(state, root_marker_site, 0)
    first_history_bond = state.source.layout.bonds[0]
    deleted_bond_used = mutate_source_bit(state, first_history_bond.sites[c365.BOND_USED_LANE], 0)
    content_lane = next(index for index, bit in enumerate(state.blocks[0].word[: c365.RECORD_BITS]) if bit)
    corrupted_word = list(state.blocks[0].word)
    corrupted_word[content_lane] ^= 1
    corrupted_block = replace(state.blocks[0], word=tuple(corrupted_word))
    corrupted_state = replace(state, blocks=canonical_blocks((corrupted_block,) + state.blocks[1:]))
    spliced_geometry = replace(state.blocks[0], sites=state.blocks[1].sites)
    spliced_state = replace(state, blocks=canonical_blocks((spliced_geometry,) + state.blocks[1:]))
    unregistered = replace(state.blocks[0], pointer_event_registered=0)
    unregistered_state = replace(state, blocks=canonical_blocks((unregistered,) + state.blocks[1:]))
    wrong_source = replace(state.blocks[0], source="host-side tag")
    wrong_source_state = replace(state, blocks=canonical_blocks((wrong_source,) + state.blocks[1:]))
    leaked_word = replace(state.blocks[0], word=state.blocks[0].word[:-1] + (2,))
    leaked_state = replace(state, blocks=canonical_blocks((leaked_word,) + state.blocks[1:]))
    alias_atom = replace(atoms[1], trial=atoms[0].trial, use=atoms[0].use)
    alias_block = replace(state.blocks[1], word=c350.atom_word(alias_atom))
    alias_state = replace(state, blocks=canonical_blocks((state.blocks[0], alias_block) + state.blocks[2:]))
    swapped_atoms = list(atoms)
    swapped_atoms[0], swapped_atoms[1] = swapped_atoms[1], swapped_atoms[0]
    wrong_sites = list(source.embedding.block_sites)
    wrong_sites[0] = wrong_sites[1]

    invalid_calls = (
        lambda: validate_tagged_state(replace(state, blocks=state.blocks[:-1])),
        lambda: validate_tagged_state(deleted_root_marker),
        lambda: validate_tagged_state(deleted_bond_used),
        lambda: validate_tagged_state(corrupted_state),
        lambda: validate_tagged_state(spliced_state),
        lambda: validate_tagged_state(unregistered_state),
        lambda: validate_tagged_state(wrong_source_state),
        lambda: validate_tagged_state(leaked_state),
        lambda: validate_tagged_state(alias_state),
        lambda: adapt_common_state(state, replace(source.embedding, ordered_roots=source.embedding.ordered_roots[:-1], block_sites=source.embedding.block_sites[:-1])),
        lambda: adapt_common_state(state, replace(source.embedding, block_sites=tuple(wrong_sites))),
        lambda: decode_typed_corpus(fixture, atoms[:-1], source.embedding),
        lambda: decode_typed_corpus(fixture, tuple(swapped_atoms), source.embedding),
        lambda: supplied_weight_rule("selected Born law"),
        lambda: apply_registered_formation(
            TaggedWorldlineState(c365.blank_state(c365.build_layout(fixture, 3, np.eye(3, dtype=int)))),
            c365.proposal(c365.build_layout(fixture, 3, np.eye(3, dtype=int)), 0, c365.words(fixture, 1)[0]),
            c365.IdentitySeed(0),
            replace(scheduled_registration(0), source="host-side tag"),
        ),
    )
    rejections = sum(rejected(call) for call in invalid_calls)
    distinct_rule_delta = 0.0
    if trace_view.weights is not None and nonlinear_view.weights is not None:
        distinct_rule_delta = max(abs(left - right) for left, right in zip(trace_view.weights, nonlinear_view.weights))
    binding_source = "\n".join((
        getsource(root_attachment_content),
        getsource(physical_root_table),
        getsource(adapt_common_state),
    ))
    forbidden_scan_terms = (
        "read_candidate_records",
        "quotient_adjacency",
        "frontier",
        "breadth_first",
        "networkx",
    )
    detail = {
        "domain_rejections": rejections,
        "domain_attempts": len(invalid_calls),
        "root_marker_deletion_rejected": rejected(lambda: validate_tagged_state(deleted_root_marker)),
        "history_bond_deletion_rejected": rejected(lambda: validate_tagged_state(deleted_bond_used)),
        "block_payload_corruption_rejected": rejected(lambda: validate_tagged_state(corrupted_state)),
        "block_geometry_splice_rejected": rejected(lambda: validate_tagged_state(spliced_state)),
        "binary_leakage_rejected": rejected(lambda: validate_tagged_state(leaked_state)),
        "host_worldline_scan_terms_present": tuple(term for term in forbidden_scan_terms if term in binding_source),
        "root_binding_maximum_bonds_examined": 2,
        "root_coordinate_encoded_in_43_M2_word": False,
        "corpus_hash_before_after_grade_deletion": (digest, deleted_grade.corpus_hash),
        "grade_deleted_weights": deleted_grade.weights,
        "trace_sampler": trace_view.actual_history_sampler,
        "trace_actual_member_selector": trace_view.actual_member_selector,
        "nonlinear_sampler": nonlinear_view.actual_history_sampler,
        "distinct_supplied_rule_maximum_delta": distinct_rule_delta,
        "selected_weight_rule": None,
        "actual_history_sampler_input": None,
        "actual_member_selector": None,
        "A_parameters": tuple(signature(adapt_common_state).parameters),
        "E_parameters": tuple(signature(encode_typed_corpus).parameters),
        "formation_adapter_parameters": tuple(signature(apply_registered_formation).parameters),
    }
    check(
        "deletion, splice, leakage, malformed-domain, grade-deletion, and sampler controls are visible without a host worldline scan",
        rejections == len(invalid_calls)
        and detail["root_marker_deletion_rejected"]
        and detail["history_bond_deletion_rejected"]
        and detail["block_payload_corruption_rejected"]
        and detail["block_geometry_splice_rejected"]
        and detail["binary_leakage_rejected"]
        and not detail["host_worldline_scan_terms_present"]
        and detail["root_binding_maximum_bonds_examined"] == 2
        and not detail["root_coordinate_encoded_in_43_M2_word"]
        and digest == deleted_grade.corpus_hash
        and deleted_grade.weights is None
        and trace_view.actual_history_sampler is None
        and trace_view.actual_member_selector is None
        and nonlinear_view.actual_history_sampler is None
        and distinct_rule_delta > 1e-6
        and detail["selected_weight_rule"] is None
        and detail["actual_history_sampler_input"] is None
        and detail["actual_member_selector"] is None
        and detail["A_parameters"] == ("state", "embedding")
        and detail["E_parameters"] == ("fixture", "common")
        and detail["formation_adapter_parameters"] == ("state", "proposal", "seed", "registration"),
        detail,
    )
    return detail


def supplied_structure_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "exact bounded migrating Cycle-365 component to grade-blind Cycle-351 corpus common-state adapter",
        "Cycle365_candidate_selected": False,
        "source_Record": "one code-valid physical endpoint-rooted Cycle-365 worldline quotient component",
        "active_carrier_is_additional_Record": False,
        "history_bond_is_additional_Record": False,
        "root_marker_is_additional_Record": False,
        "whole_43_M2_block_is_additional_Record": False,
        "physical_block": "one connected 43-M2 path adjacent to the immutable physical root endpoint",
        "Record_field_M2": c365.RECORD_BITS,
        "apparatus_tag_M2": TAG_BITS,
        "atom_M2": ATOM_BITS,
        "tag_fields": "supplied preparation/program/fine-pointer/trial/use basis word",
        "held_trial_address": "four-bit trial plus one-bit use gives 32 supplied addresses; use is not time",
        "tag_binding": "30-bit block field equals the root carrier or first source-origin bond content at radius one",
        "transported_value_valued_identity": False,
        "host_side_worldline_component_scan": False,
        "explicit_ordered_root_block_embedding": True,
        "common_projection_A": "rooted physical blocks in supplied order, invariant under history recoding",
        "encoder_E": "common rooted blocks to 30+13 M2 Cycle-351-compatible atoms",
        "decoder_D": "atoms plus the supplied physical root/block embedding to common state",
        "intertwiners": (
            "A(initial)=A(migrated)=A(two-segment history)",
            "D E A=A",
            "O_common=O_Cycle351 E",
            "two supplied W_proposal views intertwine",
        ),
        "weight_inputs": ("supplied trace proposal", "supplied nonlinear proposal"),
        "weight_input_to_formation_A_E_or_D": None,
        "selected_weight_rule": None,
        "proposal_weights_are_sampling_probabilities": False,
        "sampler_input": None,
        "actual_history_sampler": None,
        "actual_member_selector": None,
        "frequency_theorem": None,
        "Born_law_derived": False,
        "physical_tag_genesis_law": None,
        "supplied_structure": (
            "unselected Cycle-365 formation and recoding hypothesis",
            "finite 3N-carrier source capacity and two supplied recoding batches",
            "one supplied 43-M2 rooted block and registration predicate per component",
            "supplied trial/use address schedule and ordered root/block embedding",
            "Cycle-342 L3/L6 fixture, proper-cubic frame, and payload decoder",
            "Cycle-323/350 six-program observable table and two comparison functionals",
        ),
        "implementation_or_law_incompleteness": "autonomous rooted block/tag genesis, selected numerical rule, actual-history sampler, and frequency theorem remain open",
        "shared_substrate_obstruction": False,
        "no_go": None,
        "axiom_pressure": None,
        "trial_or_use_is_time": False,
        "count_is_probability": False,
        "phase_is_energy": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the physical identity, supplied blocks/embedding, weight views, and actuality/statistics boundary are explicit",
        inventory["Cycle365_candidate_selected"] is False
        and not inventory["active_carrier_is_additional_Record"]
        and not inventory["history_bond_is_additional_Record"]
        and not inventory["whole_43_M2_block_is_additional_Record"]
        and inventory["Record_field_M2"] == 30
        and inventory["apparatus_tag_M2"] == 13
        and inventory["atom_M2"] == 43
        and not inventory["transported_value_valued_identity"]
        and not inventory["host_side_worldline_component_scan"]
        and inventory["weight_input_to_formation_A_E_or_D"] is None
        and inventory["selected_weight_rule"] is None
        and not inventory["proposal_weights_are_sampling_probabilities"]
        and inventory["sampler_input"] is None
        and inventory["actual_history_sampler"] is None
        and inventory["actual_member_selector"] is None
        and inventory["frequency_theorem"] is None
        and not inventory["Born_law_derived"]
        and inventory["physical_tag_genesis_law"] is None
        and not inventory["shared_substrate_obstruction"]
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and not inventory["trial_or_use_is_time"]
        and not inventory["count_is_probability"]
        and not inventory["phase_is_energy"]
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 376: MIGRATING RECORD -> ENDPOINT-ROOTED GRADE-BLIND CORPUS")
    print("authority=none; audit=unset; sampler/member selector=None; no Born-law claim")
    note = note_contract()
    intertwiners = migration_frame_intertwiner_controls()
    reuse = endpoint_carrier_reuse_controls()
    attacks = deletion_leakage_domain_sampler_controls()
    inventory = supplied_structure_and_semantic_controls()
    check(
        "Cycle 376 gives an exact bounded migration-invariant endpoint-rooted corpus adapter while leaving tag genesis, actuality, and statistics open",
        not note["missing"]
        and intertwiners["migration_common_state_failures"] == 0
        and intertwiners["migration_hash_failures"] == 0
        and intertwiners["D_E_A_roundtrip_failures"] == 0
        and intertwiners["proposal_weight_intertwiner_failures"] == 0
        and reuse["corpus_atoms_before_after"] == (6, 7)
        and attacks["actual_history_sampler_input"] is None
        and inventory["shared_substrate_obstruction"] is False,
        {
            "disposition": "bounded positive exact migrating-component/common-corpus adapter",
            "strongest_positive": "physical endpoint-rooted 30+13 M2 atoms remain exact under two history recodings and one lawful carrier reuse adds exactly one",
            "missing": "autonomous rooted tag/block genesis, selected numerical law, actual-history sampler, frequency theorem",
            "obstruction": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_MIGRATING_RECORD_BORN_CORPUS_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_MIGRATING_RECORD_BORN_CORPUS_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
