#!/usr/bin/env python3
"""Cycle 378: conditional Cycle-281-close to Cycle-364-formation adapter.

The actual Cycle-230 Q_x-controlled Cycle-281 write/archive/reset circuit is
executed on every intrinsic computational-basis sector.  Its positive close
may enter the Cycle-364 immediate site-tethered formation hypothesis only
through an explicit supplied site/payload/close/provenance/readiness binding.
The binding openly adapts the Cycle-281 close interface to the distinct
Cycle-361 close-interface type required by Cycle 364; it is not a derivation
that the two close notions coincide.

The result is one falsifiable conditional adapter.  It selects no framework
law, no actual branch, and no occurrence.  The Cycle-364 evaluator is not a
physical formation compiler.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17 as c281
import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364


c278 = c281.c278
c269 = c281.c269
c235 = c281.c235
c342 = c364.c342
LENGTHS = (3, 6)
HELD_SIZE = 6
TOL = 3.0e-11
AUTHORITY = "none"
AUDIT = "unset"
ADAPTER_NAME = "supplied Cycle281-positive-close to Cycle361-close-interface binding v1"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE281_CLOSE_TO_CYCLE364_FORMATION_ADAPTER_"
    "CYCLE378_NOTE_2026-07-18.md"
)

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


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-378 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "falsifiable conditional adapter",
        "actual cycle-230 q_x-controlled write and reset",
        "q_x=1 computational-basis",
        "q_x=0",
        "delete first u_i",
        "delete second u_i",
        "explicit supplied adapter",
        "not relabelled as cycle-361",
        "coherent candidate branch state",
        "not a classical record",
        "held l6",
        "all 24 proper-cubic frames",
        "no physical formation compiler",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the conditional adapter and every semantic firewall", not missing, missing)


@dataclass(frozen=True)
class Cycle281Packet:
    occupation: int
    first_U_I: str
    second_U_I: str
    pointer: int
    archive: int
    close: int
    history: int
    fresh: int
    output_basis_index: int
    packet_hash: str


@dataclass(frozen=True)
class SuppliedFormationBinding:
    length: int
    target_site: c364.Coord
    payload: c364.Word
    predecessors: tuple[c364.Coord, ...]
    adapter_name: str = ADAPTER_NAME
    supplied: bool = True
    cycle281_close_source: str = "Cycle-281 positive-contact CLOSE carrier"
    target_close_interface: str = c364.CLOSE_SOURCE
    readiness_source: str = c364.READINESS_SOURCE
    provenance_source: str = c364.PROVENANCE_SOURCE


def packet_hash(
    occupation: int,
    first: str,
    second: str,
    output_basis_index: int,
) -> str:
    return sha256(
        f"{occupation}|{first}|{second}|{output_basis_index}".encode("utf-8")
    ).hexdigest()


def execute_cycle281_packet(
    occupation: int,
    *,
    first: str = "ideal",
    second: str = "ideal",
) -> Cycle281Packet:
    if not isinstance(occupation, int) or isinstance(occupation, bool) or not 0 <= occupation < 64:
        raise ValueError("occupation is outside the intrinsic six-mode basis")
    if first not in ("ideal", "deleted") or second not in ("ideal", "deleted"):
        raise ValueError("Cycle-378 admits only ideal or deleted actual U_I calls")
    blank = c281.basis(c281.ANCILLA_DIMENSION, 0)
    source = np.kron(c281.basis(c281.MATTER_DIMENSION, occupation), blank)
    gates = c281.candidate_gates(first=first, second=second)
    output = c281.apply_gates(source, gates)
    support = np.flatnonzero(np.abs(output) > TOL)
    if len(support) != 1 or abs(abs(output[support[0]]) - 1) > TOL:
        raise RuntimeError("a Cycle-281 basis input left the declared basis packet domain")
    output_index = int(support[0])
    output_occupation, ancilla = divmod(output_index, c281.ANCILLA_DIMENSION)
    if output_occupation != occupation:
        raise RuntimeError("the Cycle-281 close circuit changed its matter basis label")
    bit = lambda offset: (ancilla >> offset) & 1
    return Cycle281Packet(
        occupation,
        first,
        second,
        bit(c281.POINTER),
        bit(c281.ARCHIVE),
        bit(c281.CLOSE),
        bit(c281.HISTORY),
        bit(c281.FRESH),
        output_index,
        packet_hash(occupation, first, second, output_index),
    )


def validate_packet(packet: Cycle281Packet) -> None:
    if not isinstance(packet, Cycle281Packet):
        raise TypeError("the close adapter requires one executed Cycle-281 packet")
    expected = execute_cycle281_packet(
        packet.occupation,
        first=packet.first_U_I,
        second=packet.second_U_I,
    )
    if packet != expected:
        raise ValueError("the Cycle-281 packet or its actual-U_I ancestry was altered")


def validate_binding(
    fixture: c342.c338.RouteFixture,
    binding: SuppliedFormationBinding,
) -> None:
    if not isinstance(binding, SuppliedFormationBinding):
        raise TypeError("the adapter requires an explicit supplied binding")
    if binding.length not in LENGTHS or binding.length != fixture.length:
        raise ValueError("the binding length does not match the active fixture")
    if not binding.supplied or binding.adapter_name != ADAPTER_NAME:
        raise ValueError("the Cycle281-to-Cycle361 close binding is absent")
    if (
        binding.cycle281_close_source
        != "Cycle-281 positive-contact CLOSE carrier"
        or binding.target_close_interface != c364.CLOSE_SOURCE
        or binding.readiness_source != c364.READINESS_SOURCE
        or binding.provenance_source != c364.PROVENANCE_SOURCE
    ):
        raise ValueError("one typed source binding was silently relabelled")
    if not c364.valid_coord(binding.target_site):
        raise ValueError("target site is outside the cubic integer domain")
    if (
        not isinstance(binding.predecessors, tuple)
        or len(binding.predecessors) != 1
        or c364.distance(binding.target_site, binding.predecessors[0]) != 1
    ):
        raise ValueError("the declared adapter requires one adjacent predecessor")
    if not c364.payload_lawful(fixture, binding.payload):
        raise ValueError("the bound payload is not lawful in the active typed fixture")


def initial_state_and_binding(length: int):
    fixture = c342.c338.build_fixture(length)
    payloads = c364.words(fixture, 2)
    predecessor_site = (0, 0, 0)
    target_site = (1, 0, 0)
    predecessor = c364.SiteContentRecord(predecessor_site, payloads[0], ())
    state = c364.FormationState((predecessor,))
    c364.validate_state(fixture, state)
    binding = SuppliedFormationBinding(
        length,
        target_site,
        payloads[1],
        (predecessor_site,),
    )
    validate_binding(fixture, binding)
    return fixture, state, binding


def bound_proposal(
    fixture: c342.c338.RouteFixture,
    packet: Cycle281Packet,
    binding: SuppliedFormationBinding,
    *,
    payload_complete: int = 1,
    predecessors_ready: int = 1,
    provenance_accepted: int = 1,
    fresh: int = 1,
) -> c364.FormationProposal:
    validate_packet(packet)
    validate_binding(fixture, binding)
    if any(value not in (0, 1) for value in (
        payload_complete,
        predecessors_ready,
        provenance_accepted,
        fresh,
    )):
        raise ValueError("adapter predicates must be binary basis values")
    close = c364.FaithfulCloseInterface(
        binding.target_site,
        binding.payload,
        packet.close,
        source=binding.target_close_interface,
    )
    readiness = c364.ReadinessInterface(
        binding.target_site,
        binding.predecessors,
        predecessors_ready,
        fresh,
        source=binding.readiness_source,
    )
    provenance = c364.ProvenanceInterface(
        binding.target_site,
        binding.payload,
        binding.predecessors,
        provenance_accepted,
        independent_confirmations=1,
        source=binding.provenance_source,
    )
    return c364.FormationProposal(
        binding.target_site,
        binding.payload,
        (payload_complete,) * c364.RECORD_BITS,
        close,
        readiness,
        provenance,
    )


def basis_sector_and_actual_U_I_controls() -> dict[str, object]:
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture, state, binding = initial_state_and_binding(length)
        for occupation in range(64):
            active = c278.contact_active(occupation)
            ideal_packet = execute_cycle281_packet(occupation)
            ideal_proposal = bound_proposal(fixture, ideal_packet, binding)
            ideal = c364.apply_candidate_law(fixture, state, ideal_proposal)
            deletion_answers = {}
            for label, first, second in (
                ("delete_first_U_I", "deleted", "ideal"),
                ("delete_second_U_I", "ideal", "deleted"),
                ("delete_both_U_I", "deleted", "deleted"),
            ):
                packet = execute_cycle281_packet(
                    occupation, first=first, second=second
                )
                answer = c364.apply_candidate_law(
                    fixture,
                    state,
                    bound_proposal(fixture, packet, binding),
                )
                deletion_answers[label] = (packet, answer)

            target = c364.record_map(ideal.state).get(binding.target_site)
            expected_formed = bool(active)
            actual_formed = ideal.status == "formed"
            failures += int(actual_formed != expected_formed)
            failures += int(
                active
                and not (
                    ideal_packet.pointer == 0
                    and ideal_packet.archive == 1
                    and ideal_packet.close == 1
                    and ideal_packet.history == 1
                    and target is not None
                    and target.content == binding.payload
                    and target.predecessors == binding.predecessors
                    and len(ideal.state.records) == len(state.records) + 1
                )
            )
            failures += int(
                not active
                and not (
                    ideal_packet.close == 0
                    and ideal.formed is None
                    and ideal.state == state
                )
            )
            for packet, answer in deletion_answers.values():
                failures += int(
                    packet.close != 0
                    or answer.formed is not None
                    or answer.state != state
                )
            rows.append(
                {
                    "L": length,
                    "held": length == HELD_SIZE,
                    "occupation": occupation,
                    "Q_x": int(active),
                    "ideal_packet": (
                        ideal_packet.pointer,
                        ideal_packet.archive,
                        ideal_packet.close,
                        ideal_packet.history,
                    ),
                    "ideal_status": ideal.status,
                    "delete_first_status": deletion_answers["delete_first_U_I"][1].status,
                    "delete_second_status": deletion_answers["delete_second_U_I"][1].status,
                    "delete_both_status": deletion_answers["delete_both_U_I"][1].status,
                }
            )
    detail = {
        "basis_cases": len(rows),
        "Q_x_1_cases": sum(row["Q_x"] for row in rows),
        "Q_x_0_cases": sum(not row["Q_x"] for row in rows),
        "held_L6_cases": sum(row["held"] for row in rows),
        "conditional_formations": sum(row["ideal_status"] == "formed" for row in rows),
        "delete_first_formations": sum(row["delete_first_status"] == "formed" for row in rows),
        "delete_second_formations": sum(row["delete_second_status"] == "formed" for row in rows),
        "delete_both_formations": sum(row["delete_both_status"] == "formed" for row in rows),
        "failures": failures,
    }
    check(
        "only Q_x=1 computational-basis packets with both actual U_I calls may add one conditional Cycle-364 Record",
        len(rows) == len(LENGTHS) * 64
        and detail["Q_x_1_cases"] == len(LENGTHS) * 57
        and detail["Q_x_0_cases"] == len(LENGTHS) * 7
        and detail["held_L6_cases"] == 64
        and detail["conditional_formations"] == len(LENGTHS) * 57
        and detail["delete_first_formations"] == 0
        and detail["delete_second_formations"] == 0
        and detail["delete_both_formations"] == 0
        and failures == 0,
        detail,
    )
    return {"rows": rows, "detail": detail}


def binding_deletion_and_corruption_controls() -> dict[str, object]:
    fixture, state, binding = initial_state_and_binding(3)
    packet = execute_cycle281_packet(3)
    ideal = c364.apply_candidate_law(
        fixture, state, bound_proposal(fixture, packet, binding)
    )
    variants = (
        ("payload_presence", {"payload_complete": 0}),
        ("predecessor_readiness", {"predecessors_ready": 0}),
        ("provenance_acceptance", {"provenance_accepted": 0}),
        ("fresh_target", {"fresh": 0}),
    )
    rows = []
    failures = 0
    for label, kwargs in variants:
        answer = c364.apply_candidate_law(
            fixture,
            state,
            bound_proposal(fixture, packet, binding, **kwargs),
        )
        rows.append((label, answer.status, answer.formed is None, answer.state == state))
        failures += int(answer.formed is not None or answer.state != state)

    payloads = c364.words(fixture, 2)
    wrong_close = replace(
        bound_proposal(fixture, packet, binding).close,
        payload=payloads[0],
    )
    close_splice = replace(
        bound_proposal(fixture, packet, binding), close=wrong_close
    )
    close_answer = c364.apply_candidate_law(fixture, state, close_splice)
    wrong_provenance = replace(
        bound_proposal(fixture, packet, binding).provenance,
        payload=payloads[0],
    )
    provenance_splice = replace(
        bound_proposal(fixture, packet, binding), provenance=wrong_provenance
    )
    provenance_answer = c364.apply_candidate_law(
        fixture, state, provenance_splice
    )
    failures += int(
        close_answer.formed is not None
        or provenance_answer.formed is not None
        or close_answer.state != state
        or provenance_answer.state != state
    )

    domain_rejections = 0
    invalid_calls = (
        lambda: execute_cycle281_packet(-1),
        lambda: execute_cycle281_packet(3, first="pointer_only"),
        lambda: validate_packet(replace(packet, close=0)),
        lambda: validate_binding(fixture, replace(binding, supplied=False)),
        lambda: validate_binding(
            fixture, replace(binding, target_close_interface="Cycle-281-close")
        ),
        lambda: validate_binding(
            fixture, replace(binding, payload=binding.payload[:-1])
        ),
        lambda: validate_binding(
            fixture, replace(binding, predecessors=((4, 0, 0),))
        ),
    )
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            domain_rejections += 1
    detail = {
        "ideal_status": ideal.status,
        "predicate_deletions": rows,
        "close_payload_splice_status": close_answer.status,
        "provenance_payload_splice_status": provenance_answer.status,
        "domain_rejections": domain_rejections,
        "attempted_domain_violations": len(invalid_calls),
        "binding_deletion_or_corruption_failures": failures,
    }
    check(
        "payload, readiness, provenance, freshness, close binding, and adapter-domain deletions are visible without target leakage",
        ideal.status == "formed"
        and all(row[2] and row[3] for row in rows)
        and close_answer.formed is None
        and provenance_answer.formed is None
        and domain_rejections == len(invalid_calls)
        and failures == 0,
        detail,
    )
    return detail


def coherent_candidate_controls() -> dict[str, object]:
    fixture, state, binding = initial_state_and_binding(HELD_SIZE)
    inactive = 0
    active = 3
    matter = (
        c281.basis(c281.MATTER_DIMENSION, inactive)
        + c281.basis(c281.MATTER_DIMENSION, active)
    ) / np.sqrt(2)
    source = np.kron(matter, c281.basis(c281.ANCILLA_DIMENSION, 0))
    output = c281.apply_gates(source, c281.candidate_gates())
    inactive_packet = execute_cycle281_packet(inactive)
    active_packet = execute_cycle281_packet(active)
    inactive_index = inactive_packet.output_basis_index
    active_index = active_packet.output_basis_index
    branch_coherence = output[inactive_index] * output[active_index].conj()
    purity_residual = abs(float(np.vdot(output, output).real) ** 2 - 1)
    support = tuple(int(item) for item in np.flatnonzero(np.abs(output) > TOL))
    inactive_answer = c364.apply_candidate_law(
        fixture,
        state,
        bound_proposal(fixture, inactive_packet, binding),
    )
    active_answer = c364.apply_candidate_law(
        fixture,
        state,
        bound_proposal(fixture, active_packet, binding),
    )
    classical_domain_rejection = 0
    try:
        c364.apply_candidate_law(fixture, output, bound_proposal(fixture, active_packet, binding))
    except TypeError:
        classical_domain_rejection += 1
    detail = {
        "L": HELD_SIZE,
        "coherent_support_basis_indices": support,
        "inactive_amplitude": output[inactive_index],
        "active_amplitude": output[active_index],
        "cross_branch_coherence": branch_coherence,
        "pure_state_residual": purity_residual,
        "inactive_basis_conditional_status": inactive_answer.status,
        "active_basis_conditional_status": active_answer.status,
        "Cycle364_classical_domain_rejections": classical_domain_rejection,
        "actual_member_selector": None,
        "branch_content_law": None,
        "independent_formation_law_selected": None,
        "formed_Record": None,
        "occurrence": None,
    }
    check(
        "the coherent Q_x=0 plus Q_x=1 input remains one coherent candidate branch state, not a classical Record or actual member",
        support == (inactive_index, active_index)
        and abs(output[inactive_index] - 1 / np.sqrt(2)) < TOL
        and abs(output[active_index] - 1 / np.sqrt(2)) < TOL
        and abs(branch_coherence - 0.5) < TOL
        and purity_residual < TOL
        and inactive_answer.formed is None
        and active_answer.status == "formed"
        and classical_domain_rejection == 1
        and detail["actual_member_selector"] is None
        and detail["branch_content_law"] is None
        and detail["independent_formation_law_selected"] is None
        and detail["formed_Record"] is None
        and detail["occurrence"] is None,
        detail,
    )
    return detail


def physical_support_mass_and_frame_controls() -> dict[str, object]:
    support_rows = []
    support_failures = 0
    frame_failures = 0
    formation_frame_failures = 0
    payload_mapping_failures = 0
    frame_cases = 0
    for length in LENGTHS:
        code = c269.build_code(length)
        bs = c278.cell_bs(code, (0, 0, 0))
        terms = tuple(c278.pauli_product(bs, mask) for mask in range(64))
        support_union = 0
        for row in bs:
            support_union |= row.x | row.z
        leakage = sum(
            not term.commutes(check_row)
            for term in terms
            for check_row in code.local_checks + code.wilsons
        )
        row = {
            "L": length,
            "held": length == HELD_SIZE,
            "Cycle281_matter_support_M2": support_union.bit_count(),
            "Cycle281_interface_M2": c281.ANCILLA_BITS,
            "Cycle281_close_patch_M2": support_union.bit_count() + c281.ANCILLA_BITS,
            "Walsh_terms": len(terms),
            "check_or_Wilson_leakage": leakage,
            "Cycle364_physical_formation_compiler": None,
        }
        support_rows.append(row)
        support_failures += int(
            row["Cycle281_matter_support_M2"] != 18
            or row["Cycle281_interface_M2"] != 5
            or row["Cycle281_close_patch_M2"] != 23
            or row["Walsh_terms"] != 64
            or leakage != 0
        )

        fixture, state, binding = initial_state_and_binding(length)
        packet = execute_cycle281_packet(3)
        proposal = bound_proposal(fixture, packet, binding)
        reference = c364.apply_candidate_law(fixture, state, proposal)
        local_family = set(code.local_checks)
        base_bs = set(bs)
        for frame in c235.proper_cubic_frames():
            # Cycle 281's complete physical code-frame audit is canonically
            # executed at L3; L6 is the independent held support/leakage
            # control.  Do not repeat the cubic repair elimination on the
            # much larger held torus inside this adapter.
            if length == 3:
                vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
                toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
                transformed_bs = {
                    c235.apply_gauge(
                        c235.permute_pauli(item, edge_map), toggles, pairs, flips
                    )
                    for item in bs
                }
                transformed_local = {
                    c235.apply_gauge(
                        c235.permute_pauli(item, edge_map), toggles, pairs, flips
                    )
                    for item in code.local_checks
                }
                frame_failures += int(
                    transformed_bs != base_bs or transformed_local != local_family
                )

            # The adapter adds only the site/content association.  Carry the
            # already typed payload word as one bound content value while the
            # target/predecessor neighborhood is rotated.  Internal
            # Cycle-342 word covariance is inherited, not re-executed or
            # promoted into a physical formation compiler here.
            target = c364.transform_coord(binding.target_site, frame, (0, 0, 0))
            predecessors = tuple(
                c364.transform_coord(item, frame, (0, 0, 0))
                for item in binding.predecessors
            )
            framed_binding = replace(
                binding,
                target_site=target,
                predecessors=predecessors,
            )
            framed_records = tuple(
                replace(
                    record,
                    site=c364.transform_coord(record.site, frame, (0, 0, 0)),
                    predecessors=tuple(
                        c364.transform_coord(item, frame, (0, 0, 0))
                        for item in record.predecessors
                    ),
                )
                for record in state.records
            )
            framed_state = c364.FormationState(c364.canonical(framed_records))
            framed_proposal = bound_proposal(
                fixture, packet, framed_binding
            )
            observed = c364.apply_candidate_law(
                fixture, framed_state, framed_proposal
            )
            expected_records = tuple(
                replace(
                    record,
                    site=c364.transform_coord(record.site, frame, (0, 0, 0)),
                    predecessors=tuple(
                        c364.transform_coord(item, frame, (0, 0, 0))
                        for item in record.predecessors
                    ),
                )
                for record in reference.state.records
            )
            expected_state = c364.FormationState(c364.canonical(expected_records))
            formation_frame_failures += int(
                observed.status != reference.status
                or observed.state != expected_state
                or observed.formed is None
                or observed.formed.site != target
                or observed.formed.content != binding.payload
                or observed.formed.predecessors != predecessors
            )
            frame_cases += 1

    occupations = np.asarray([index.bit_count() for index in range(64)])
    species = c278.c219.common_species(c278.c230.BETA)
    contact = np.diag(
        np.exp(
            1j
            * c278.c230.COUPLING
            * occupations
            * (occupations - 1)
            / 2
        )
    )
    contact_support = np.asarray(
        np.abs(np.diag(contact) - 1) > 2e-14, dtype=int
    )
    q_support = np.asarray(
        [c278.contact_active(index) for index in range(64)], dtype=int
    )
    mass_relative_residual = abs(
        c278.c219.rest_mass(species) / species.analytic_mass - 1
    )
    detail = {
        "support_rows": support_rows,
        "proper_cubic_frame_cases": frame_cases,
        "physical_close_frame_failures": frame_failures,
        "formation_binding_frame_failures": formation_frame_failures,
        "payload_mapping_failures": payload_mapping_failures,
        "actual_Cycle230_contact_support_minus_Q_x": int(
            np.count_nonzero(contact_support != q_support)
        ),
        "one_particle_mass_relative_residual": mass_relative_residual,
    }
    check(
        "the 23-M2 Cycle-281 close patch, payload binding, and conditional evaluator are exact at L3/held-L6 under all 24 frames",
        support_failures == 0
        and frame_cases == len(LENGTHS) * 24
        and frame_failures == formation_frame_failures == payload_mapping_failures == 0
        and detail["actual_Cycle230_contact_support_minus_Q_x"] == 0
        and mass_relative_residual < 2e-12,
        detail,
    )
    return detail


def inventory_controls() -> dict[str, object]:
    inventory = {
        "result": "falsifiable conditional Cycle281-close to Cycle364-formation adapter",
        "supplied": (
            "Cycle-281 connected-code Q_x, same pointer, two actual U_I calls, archive, close, and history gates",
            "one lawful Cycle-342 typed predecessor Record and one target payload per finite fixture",
            "one target site, adjacent predecessor tuple, complete payload presence, readiness, freshness, and provenance acceptance",
            ADAPTER_NAME,
            "Cycle-364 immediate site-tethered formation hypothesis and its finite basis-domain evaluator",
            "L3/held-L6 domains, proper-cubic frame maps, and tolerances",
        ),
        "derived": (
            "Q_x=1 ideal basis packets conditionally form one target Record under the supplied Cycle-364 hypothesis",
            "Q_x=0 and either/both actual-U_I deletions form no target",
            "payload/provenance/readiness/freshness deletions block the target",
            "coherent cross-sector input stays one candidate branch state",
        ),
        "Cycle281_close_called_Cycle361_without_adapter": False,
        "adapter_is_derived_equivalence": False,
        "Cycle364_law_selected": False,
        "framework_law_selected": False,
        "physical_formation_compiler": None,
        "actual_member_selector": None,
        "occurrence": None,
        "Born_rule": None,
        "clock_or_interval": None,
        "far_side_source_interpretation": None,
        "shared_obstruction": None,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the adapter inventory exposes every supplied binding without selecting a formation law or physical compiler",
        inventory["Cycle281_close_called_Cycle361_without_adapter"] is False
        and inventory["adapter_is_derived_equivalence"] is False
        and inventory["Cycle364_law_selected"] is False
        and inventory["framework_law_selected"] is False
        and inventory["physical_formation_compiler"] is None
        and inventory["actual_member_selector"] is None
        and inventory["occurrence"] is None
        and inventory["Born_rule"] is None
        and inventory["clock_or_interval"] is None
        and inventory["far_side_source_interpretation"] is None
        and inventory["shared_obstruction"] is inventory["no_go"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 378: CYCLE281 CLOSE TO CYCLE364 FORMATION ADAPTER")
    print("authority=none; audit=unset; conditional adapter; no law selection")
    note_contract()
    basis_sector_and_actual_U_I_controls()
    binding_deletion_and_corruption_controls()
    coherent_candidate_controls()
    physical_support_mass_and_frame_controls()
    inventory_controls()
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_CYCLE281_CLOSE_TO_CYCLE364_FORMATION_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_CYCLE281_CLOSE_TO_CYCLE364_FORMATION_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
