#!/usr/bin/env python3
"""Cycle-718 physical spatial-packet to Cycle-704/610/612 interval adapter.

The input is one literal 39-M2 packet/handshake bundle emitted by the routed
Cycle713 spatial ACK bridge.  A reversible bit-level adapter writes a fresh
Cycle704 34-bit payload, six-bit identity, predecessor/head, K16 rotor/carry,
and six-bit next-address state.  Selection of a new blank output cell for each
append remains explicit host-side bank work and is not hidden as an M2 law.

No count, rotor, address, or circuit ordinal is called time.  The reversible
packet is not called a Record.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path
import random
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
import frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26 as R


A = R.A
AUDIT_TIMEOUT_SEC = R.AUDIT_TIMEOUT_SEC
NOTE_PATH = R.NOTE_PATH
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/infinite_reversible_record_export_qca_cycle11_2026_07_14.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TOL = 5.0e-10
BANK = C704.C610.BANK_SIZE
SENTINEL = C714.SENTINEL_NONE


@dataclass(frozen=True)
class Layout:
    source: tuple[int, ...]
    payload: tuple[int, ...]
    identity: tuple[int, ...]
    head: tuple[int, ...]
    address: tuple[int, ...]
    rotor: tuple[int, ...]
    packet_fresh: int
    exhausted: int
    capacity: int
    new: int
    ack: int
    commit: int
    fail: int
    work: tuple[int, ...]
    n: int


def make_layout() -> Layout:
    cursor = 0

    def take(count):
        nonlocal cursor
        output = tuple(range(cursor, cursor + count))
        cursor += count
        return output

    source = take(R.RAIL_WIDTH)
    payload = take(34)
    identity = take(6)
    head = take(6)
    address = take(6)
    rotor = take(4)
    packet_fresh, exhausted, capacity, new, ack, commit, fail = take(7)
    work = take(56)
    return Layout(
        source, payload, identity, head, address, rotor,
        packet_fresh, exhausted, capacity, new, ack, commit, fail,
        work, cursor,
    )


L = make_layout()
SRC = R.rail_fields(L.source)
PRED = L.payload[:6]
RB = L.payload[6:10]
RA = L.payload[10:14]
CARRY = L.payload[14]
PDELTA = L.payload[15:27]
PEND, PBIND, PVALID, PORIENT, PACT, PADM, PLAW = L.payload[27:34]


def swap(left, right):
    return (A.cn(left, right), A.cn(right, left), A.cn(left, right))


def capacity_word():
    # 0 <= address < 24 iff bit5=0 and either bit4=0 or (bit4=1,bit3=0).
    return (
        *R.zero_controlled((), (L.address[5], L.address[4]), L.capacity, L.work),
        *R.zero_controlled((L.address[4],), (L.address[5], L.address[3]), L.capacity, L.work),
    )


def adapter_word(omit: str | None = None):
    output = []
    cap = capacity_word()
    output.extend(cap)
    positives = (
        SRC["endpoint"], SRC["binder"], SRC["valid"],
        SRC["actual"], SRC["admiss"], SRC["law"],
        SRC["fresh"], SRC["start"], SRC["cleanup"],
    )
    target_blank = (*L.payload, *L.identity, L.packet_fresh)
    if omit != "complete_blank_NEW":
        output.extend(R.zero_controlled(
            positives + (L.capacity,), target_blank, L.new, L.work
        ))
    # A capacity failure gets a reversible finite-bank receipt.  This is a
    # one-attempt output; replay without moving the input packet is off-domain.
    output.extend(R.zero_controlled(
        positives, target_blank + (L.capacity,), L.fail, L.work
    ))
    output.extend(swap(L.fail, L.exhausted))
    output.extend(reversed(cap))

    if omit != "append_ACK":
        output.append(A.cn(L.new, L.ack))
    ack = L.ack
    for source, target in zip(L.head, PRED):
        output.append(A.tof(ack, source, target))
    for source, target in zip(L.rotor, RB):
        output.append(A.tof(ack, source, target))
    if omit != "carry":
        output.extend(A.mcx((ack, *L.rotor), CARRY, L.work))
    # Controlled K16 increment, high bits first.
    output.extend(A.mcx((ack, L.rotor[0], L.rotor[1], L.rotor[2]), L.rotor[3], L.work))
    output.extend(A.mcx((ack, L.rotor[0], L.rotor[1]), L.rotor[2], L.work))
    output.extend((A.tof(ack, L.rotor[0], L.rotor[1]), A.cn(ack, L.rotor[0])))
    for source, target in zip(L.rotor, RA):
        output.append(A.tof(ack, source, target))
    for source, target in zip(SRC["delta"], PDELTA):
        output.append(A.tof(ack, source, target))
    for source, target in (
        (SRC["endpoint"], PEND),
        (SRC["binder"], PBIND),
        (SRC["valid"], PVALID),
        (SRC["orientation"], PORIENT),
        (SRC["actual"], PACT),
        (SRC["admiss"], PADM),
        (SRC["law"], PLAW),
    ):
        output.append(A.tof(ack, source, target))
    for source, target in zip(L.address, L.identity):
        output.append(A.tof(ack, source, target))

    # The old head is retained in PRED, so HEAD <- ADDRESS is reversible.
    for source, target in zip(PRED, L.head):
        output.append(A.tof(ack, source, target))
    for source, target in zip(L.address, L.head):
        output.append(A.tof(ack, source, target))
    # Controlled K64 address increment, again high bits first.
    for bit in reversed(range(1, 6)):
        output.extend(A.mcx((ack, *L.address[:bit]), L.address[bit], L.work))
    output.append(A.cn(ack, L.address[0]))

    # ACK returns clean.  NEW itself remains as the packet-local append
    # receipt; the inverse consumes it only after restoring the source and
    # target blank.  No dirty payload bit is later reused as an authorizer.
    output.append(A.cn(L.new, L.ack))
    # Consume only the NEW bit created by this invocation; an independently
    # dirty packet-fresh target must not consume the source freshness.
    if omit != "source_freshness":
        output.append(A.cn(L.new, SRC["fresh"]))
    if omit != "fresh_transfer":
        output.append(A.cn(L.new, L.packet_fresh))
    return tuple(output)


def set_integer(bits, wires, value):
    for index, wire in enumerate(wires):
        bits[wire] = (value >> index) & 1


def integer(bits, wires):
    return sum(bits[wire] << index for index, wire in enumerate(wires))


def source_bundle(orientation=1, *, missing: str | None = None):
    bundle = list(R.expected_packet(orientation, 1, 2, 0, 0))
    if missing is not None:
        field = R.rail_fields(tuple(range(R.RAIL_WIDTH)))[missing]
        if not isinstance(field, int):
            raise ValueError(missing)
        bundle[field] = 0
    return tuple(bundle)


def initial(source, *, head=SENTINEL, address=0, rotor=14, dirty_target=None):
    bits = [0] * L.n
    for wire, value in zip(L.source, source):
        bits[wire] = value
    set_integer(bits, L.head, head)
    set_integer(bits, L.address, address)
    set_integer(bits, L.rotor, rotor)
    if dirty_target is not None:
        bits[L.payload[dirty_target]] = 1
    return tuple(bits)


def decode_packet(bits):
    predecessor = integer(bits, PRED)
    return C704.IntervalPacket(
        identity=integer(bits, L.identity),
        predecessor=None if predecessor == SENTINEL else predecessor,
        rotor_before=integer(bits, RB),
        rotor=integer(bits, RA),
        carry=bits[CARRY],
        delta_mask=integer(bits, PDELTA),
        endpoint=bits[PEND],
        binder=bits[PBIND],
        valid=bits[PVALID],
        orientation=1 if bits[PORIENT] else -1,
        actuality=bits[PACT],
        admissibility=bits[PADM],
        law_domain=bits[PLAW],
    )


def direct_source_projection_ceiling():
    # The spatial bridge's original one-bit identity/frontier was intentionally
    # not claimed as a Cycle610 address.  Quantify that mismatch before adding
    # the six-bit sidecar rather than silently relabeling it.
    head, identity = 1, 0
    mismatches = []
    for address in range(4):
        packet = R.expected_packet(1, head, (2 + address) % 16, identity, 0)
        fields = R.rail_fields(tuple(range(R.RAIL_WIDTH)))
        observed_pred = sum(packet[wire] << bit for bit, wire in enumerate(fields["pred"]))
        observed_identity = packet[fields["identity_tag"]]
        expected_pred = None if address == 0 else address - 1
        mismatches.append({
            "address": address,
            "observed_one_bit_identity": observed_identity,
            "observed_predecessor_word": observed_pred,
            "expected_identity": address,
            "expected_predecessor": expected_pred,
            "matches": observed_identity == address and (
                (observed_pred == SENTINEL if expected_pred is None else observed_pred == expected_pred)
            ),
        })
        head, identity = identity, head
    return {
        "rows": mismatches,
        "mismatch_count": sum(not row["matches"] for row in mismatches),
        "verdict": "direct raw spatial predecessor/identity is not the Cycle610 chain address",
    }


def semantic_certificate():
    word = adapter_word()
    inverse = tuple(reversed(word))
    packets = []
    cycle610 = C704.C610.EventChain(bank=BANK)
    head, address, rotor = SENTINEL, 0, 14
    append_failures = projection_failures = inverse_failures = replay_failures = 0
    carry_failures = work_failures = freshness_failures = 0
    same_cell_reapplication_maximum_hamming = 0
    statuses = []
    for step in range(BANK):
        before = initial(
            source_bundle(1 if step % 2 == 0 else -1),
            head=head, address=address, rotor=rotor,
        )
        after = A.apply_semantic(before, word)
        packet = decode_packet(after)
        packets.append(packet)
        expected_predecessor = None if step == 0 else step - 1
        append_failures += any((
            packet.identity != step,
            packet.predecessor != expected_predecessor,
            packet.rotor_before != rotor,
            packet.rotor != (rotor + 1) % 16,
            packet.carry != int(rotor == 15),
            packet.delta_mask != 66,
            not (packet.endpoint == packet.binder == packet.valid),
            packet.actuality != packet.admissibility,
            packet.admissibility != packet.law_domain,
        ))
        carry_failures += packet.carry != int(rotor == 15)
        freshness_failures += not after[L.packet_fresh] or after[SRC["fresh"]]
        work_failures += any(after[wire] for wire in (*L.work, L.capacity, L.ack, L.commit, L.fail))
        work_failures += after[L.new] != 1
        restored = A.apply_semantic(after, inverse)
        inverse_failures += restored != before
        replay_failures += A.apply_semantic(restored, word) != after
        reapplied = A.apply_semantic(after, word)
        same_cell_reapplication_maximum_hamming = max(
            same_cell_reapplication_maximum_hamming,
            sum(left != right for left, right in zip(after, reapplied)),
        )
        status = cycle610.admit(
            tick_id=step, orientation=packet.orientation,
            certificate=packet.endpoint, binder=packet.binder,
            actuality=packet.actuality, admissibility=packet.admissibility,
            law_domain=packet.law_domain,
        )
        statuses.append(status)
        expected_cell = cycle610.cells[-1]
        projected = C704.C610.EventCell(
            identity=packet.identity, rotor=packet.rotor, carry=packet.carry,
            predecessor=packet.predecessor, binder=packet.binder,
            valid=packet.valid, orientation=packet.orientation,
        )
        projection_failures += asdict(projected) != asdict(expected_cell)
        head = integer(after, L.head)
        address = integer(after, L.address)
        rotor = integer(after, L.rotor)

    exhausted_before = initial(source_bundle(), head=head, address=address, rotor=rotor)
    exhausted_after = A.apply_semantic(exhausted_before, word)
    physical_exhausted = exhausted_after[L.exhausted] == 1 and not exhausted_after[PVALID]
    exhausted_inverse = A.apply_semantic(exhausted_after, inverse) == exhausted_before
    exhausted_replay = A.apply_semantic(
        A.apply_semantic(exhausted_after, inverse), word
    ) == exhausted_after
    cycle610_exhausted = cycle610.admit(
        tick_id=address, orientation=1, certificate=1, binder=1,
        actuality=1, admissibility=1, law_domain=1,
    )

    controls = {}
    blank = (0,) * R.RAIL_WIDTH
    no_op = initial(blank, head=7, address=3, rotor=5)
    controls["no_opportunity"] = A.apply_semantic(no_op, word) == no_op
    for field in (
        "endpoint", "binder", "valid", "actual", "admiss", "law",
        "fresh", "start", "cleanup",
    ):
        before = initial(source_bundle(missing=field), head=7, address=3, rotor=5)
        controls["refused_" + field] = A.apply_semantic(before, word) == before
    dirty_target_failures = 0
    for dirty_target in range(34):
        dirty = initial(
            source_bundle(), head=7, address=3, rotor=5,
            dirty_target=dirty_target,
        )
        dirty_target_failures += A.apply_semantic(dirty, word) != dirty
    # The six identity bits and packet-fresh sideband are also in NEW's
    # complete-blank predicate.
    for dirty_wire in (*L.identity, L.packet_fresh):
        dirty = list(initial(source_bundle(), head=7, address=3, rotor=5))
        dirty[dirty_wire] = 1
        dirty = tuple(dirty)
        dirty_target_failures += A.apply_semantic(dirty, word) != dirty
    controls["all_41_dirty_target_bits_refused"] = dirty_target_failures == 0
    rng_dirty = random.Random(0xD17)
    dirty_combination_rows = dirty_combination_failures = 0
    target_surface = (*L.payload, *L.identity, L.packet_fresh)
    for _ in range(256):
        dirty = list(initial(source_bundle(), head=7, address=3, rotor=5))
        for wire in rng_dirty.sample(
            target_surface, rng_dirty.randrange(1, min(20, len(target_surface)) + 1)
        ):
            dirty[wire] = 1
        dirty = tuple(dirty)
        dirty_combination_failures += A.apply_semantic(dirty, word) != dirty
        dirty_combination_rows += 1

    capacity_rows = capacity_failures = capacity_inverse_failures = 0
    for probe_address in range(64):
        before = initial(
            source_bundle(), head=7, address=probe_address, rotor=5
        )
        after = A.apply_semantic(before, word)
        admitted = probe_address < BANK
        capacity_failures += any((
            bool(after[PVALID]) != admitted,
            bool(after[L.exhausted]) == admitted,
            integer(after, L.address) != (
                (probe_address + 1) % 64 if admitted else probe_address
            ),
            any(after[wire] for wire in (*L.work, L.capacity, L.ack, L.commit, L.fail)),
            after[L.new] != int(admitted),
        ))
        capacity_inverse_failures += A.apply_semantic(after, inverse) != before
        capacity_rows += 1

    # The interval decoder consumes only the physical packet projections.
    projected_chain = C704.C610.EventChain(bank=BANK)
    projected_chain.cells = [
        C704.C610.EventCell(
            identity=packet.identity, rotor=packet.rotor, carry=packet.carry,
            predecessor=packet.predecessor, binder=packet.binder,
            valid=packet.valid, orientation=packet.orientation,
        ) for packet in packets
    ]
    projected_chain.admitted_ticks = {packet.identity for packet in packets}
    d_ab = projected_chain.interval(2, 11)
    d_bc = projected_chain.interval(11, 23)
    d_ac = projected_chain.interval(2, 23)

    rng = random.Random(0x610704)
    arbitrary_inverse_failures = 0
    for _ in range(64):
        before = tuple(rng.getrandbits(1) for _ in range(L.n))
        arbitrary_inverse_failures += A.apply_semantic(
            A.apply_semantic(before, word), inverse
        ) != before

    reference = A.apply_semantic(initial(source_bundle(), head=7, address=3, rotor=15), word)
    deletions = {}
    for omit in ("complete_blank_NEW", "append_ACK", "carry", "fresh_transfer", "source_freshness"):
        damaged = A.apply_semantic(
            initial(source_bundle(), head=7, address=3, rotor=15),
            adapter_word(omit=omit),
        )
        deletions[omit] = sum(a != b for a, b in zip(reference, damaged))
    return {
        "bank_cells": BANK,
        "statuses": tuple(statuses),
        "append_failures": append_failures,
        "Cycle610_projection_failures": projection_failures,
        "inverse_failures": inverse_failures,
        "replay_failures": replay_failures,
        "same_cell_reapplication_maximum_hamming": same_cell_reapplication_maximum_hamming,
        "carry_failures": carry_failures,
        "freshness_transfer_failures": freshness_failures,
        "work_return_failures": work_failures,
        "final_head": head,
        "final_next_address": address,
        "final_rotor": rotor,
        "physical_exhausted_receipt": physical_exhausted,
        "exhausted_inverse_exact": exhausted_inverse,
        "exhausted_replay_exact": exhausted_replay,
        "Cycle610_exhaustion_status": cycle610_exhausted,
        "controls": controls,
        "dirty_target_rows": 41,
        "dirty_target_failures": dirty_target_failures,
        "dirty_combination_rows": dirty_combination_rows,
        "dirty_combination_failures": dirty_combination_failures,
        "capacity_address_rows": capacity_rows,
        "capacity_address_failures": capacity_failures,
        "capacity_inverse_failures": capacity_inverse_failures,
        "intervals": {"d_ab": d_ab, "d_bc": d_bc, "d_ac": d_ac},
        "additivity_closed": d_ab is not None and d_bc is not None and d_ac == d_ab + d_bc,
        "reversal_closed": projected_chain.interval(11, 2) == -d_ab,
        "arbitrary_inverse_rows": 64,
        "arbitrary_inverse_failures": arbitrary_inverse_failures,
        "deletion_hamming": deletions,
        "all_deletions_detected": all(deletions.values()),
        "host_selected_new_blank_output_cell_each_append": True,
        "duplicate_membership_table_physical": False,
    }


def physical_layout():
    source_layout = R.physical_layout(13)
    source_sites = source_layout["rails_a"][0][1]
    # Keep the sidecar in one explicit bounded block outside the already assigned
    # Cycle-713 rail chart.  A nearest-shell placement was rejected because 58
    # transient router coordinates crossed live rail sites even though its
    # endpoints were disjoint.
    candidates = tuple(
        (52, -20 + y, -20 + z)
        for z in range(17)
        for y in range(7)
    )
    sites = tuple(source_sites) + candidates[:L.n - R.RAIL_WIDTH]
    if len(sites) != L.n or len(set(sites)) != L.n:
        raise AssertionError("adapter placement")
    if set(sites[R.RAIL_WIDTH:]) & set(source_layout["assigned_sites"]):
        raise AssertionError("adapter overlaps assigned spatial rail")
    return source_layout, sites


def physical_route_certificate():
    source_layout, sites = physical_layout()
    primitives = A.expanded(adapter_word())
    matrices = {"X": A.X, "H": A.H, "T": A.T, "TD": A.TD, "CNOT": A.CNOT}
    word = tuple(
        R.C712.c707.Instruction(
            "interval_adapter_" + kind,
            tuple(sites[wire] for wire in wires), matrices[kind],
        ) for kind, wires in primitives
    )
    routed, route = R.C712.c707.route_word(word)
    inverse_word = tuple(
        R.C712.c707.Instruction(
            "interval_adapter_inverse_" + kind,
            tuple(sites[wire] for wire in wires), matrices[kind],
        ) for kind, wires in A.expanded(tuple(reversed(adapter_word())))
    )
    inverse_routed, inverse_route = R.C712.c707.route_word(inverse_word)
    frames = R.C712.C709.F.base.proper_cubic_frames()
    coordinate_failures = NN_failures = product_failures = 0
    permutations = []
    for frame in frames:
        matrix = R.C712.C709.F.base.c210.direction_permutation(frame)
        permutations.append(tuple(
            next(target for target in range(6) if abs(matrix[target, source]) > 0.5)
            for source in range(6)
        ))
        inverse = frame.T
        for instruction in word:
            moved = tuple(tuple(int(v) for v in frame @ np.asarray(site)) for site in instruction.sites)
            restored = tuple(tuple(int(v) for v in inverse @ np.asarray(site)) for site in moved)
            coordinate_failures += restored != instruction.sites
        for gate in routed:
            if len(gate.sites) == 2:
                moved = tuple(tuple(int(v) for v in frame @ np.asarray(site)) for site in gate.sites)
                NN_failures += sum(abs(a - b) for a, b in zip(*moved)) != 1
    for li, left in enumerate(frames):
        for ri, right in enumerate(frames):
            index = next(i for i, frame in enumerate(frames) if np.array_equal(frame, left @ right))
            product_failures += tuple(
                permutations[li][permutations[ri][mode]] for mode in range(6)
            ) != permutations[index]
    assigned = set(sites)
    source_assigned = set(source_layout["assigned_sites"])
    input_bundle = set(source_layout["rails_a"][0][1])
    other_spatial = source_assigned - input_bundle
    touched = set(route["touched_coordinates"]) | set(inverse_route["touched_coordinates"])
    return {
        "input_bundle_M2": R.RAIL_WIDTH,
        "new_adapter_M2": L.n - R.RAIL_WIDTH,
        "assigned_adapter_M2": L.n,
        "semantic_gates": len(adapter_word()),
        "expanded_primitives": len(word),
        "routed_gates": len(routed),
        "inverse_routed_gates": len(inverse_routed),
        "maximum_route_distance": max(route["maximum_route_distance"], inverse_route["maximum_route_distance"]),
        "non_NN_failures": route["non_NN_failures"] + inverse_route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"] + inverse_route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"] + inverse_route["route_return_failures"],
        "deletion_detected_macros": route["delete_first_swap_detected_macros"],
        "routed_word_sha256": route["word_sha256"],
        "inverse_routed_word_sha256": inverse_route["word_sha256"],
        "touched_M2": len(touched),
        "blank_route_work_M2": len(touched - assigned),
        "adapter_placement_collisions": len(set(sites[R.RAIL_WIDTH:]) & source_assigned),
        "spatial_assigned_route_collisions": len(touched & other_spatial),
        "spatial_source_bundle_coordinates": source_sites_digest(source_layout["rails_a"][0][1]),
        "source_is_post_shift_station_one": True,
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "coordinate_restore_failures": coordinate_failures,
        "routed_NN_frame_failures": NN_failures,
        "direction_product_failures": product_failures,
    }


def source_sites_digest(sites):
    return sha256(json.dumps(sites, sort_keys=True).encode()).hexdigest()


def main():
    provenance = C714.provenance_certificate(AUDIT_INPUT_PATHS, __file__)
    direct = direct_source_projection_ceiling()
    semantic = semantic_certificate()
    route = physical_route_certificate()
    joint = C704.joint_order_controls()
    unchanged_host = C704.packet_interface_controls()
    checks = {
        "source_closure": provenance["baseline_is_ancestor"]
        and provenance["declared_path_failures"] == 0
        and provenance["duplicate_declared_paths"] == 0
        and not provenance["missing_transitive_scripts"]
        and not provenance["missing_dynamic_scripts"]
        and not provenance["untracked_inputs"],
        "direct_projection_boundary_exposed": direct["mismatch_count"] == 4,
        "bit_level_interval_adapter": all((
            semantic["statuses"] == ("admitted",) * BANK,
            semantic["append_failures"] == 0,
            semantic["Cycle610_projection_failures"] == 0,
            semantic["inverse_failures"] == 0,
            semantic["replay_failures"] == 0,
            semantic["carry_failures"] == 0,
            semantic["freshness_transfer_failures"] == 0,
            semantic["work_return_failures"] == 0,
            semantic["physical_exhausted_receipt"],
            semantic["exhausted_inverse_exact"],
            semantic["exhausted_replay_exact"],
            semantic["Cycle610_exhaustion_status"] == "exhausted",
            all(semantic["controls"].values()),
            semantic["dirty_target_rows"] == 41,
            semantic["dirty_target_failures"] == 0,
            semantic["dirty_combination_rows"] == 256,
            semantic["dirty_combination_failures"] == 0,
            semantic["capacity_address_rows"] == 64,
            semantic["capacity_address_failures"] == 0,
            semantic["capacity_inverse_failures"] == 0,
            semantic["additivity_closed"],
            semantic["reversal_closed"],
            semantic["arbitrary_inverse_failures"] == 0,
            semantic["all_deletions_detected"],
        )),
        "literal_M2_route": all((
            route["non_NN_failures"] == 0,
            route["operand_order_failures"] == 0,
            route["route_return_failures"] == 0,
            route["adapter_placement_collisions"] == 0,
            route["spatial_assigned_route_collisions"] == 0,
            route["deletion_detected_macros"] > 0,
            route["proper_cubic_frames"] == 24,
            route["ordered_frame_products"] == 576,
            route["coordinate_restore_failures"] == 0,
            route["routed_NN_frame_failures"] == 0,
            route["direction_product_failures"] == 0,
        )),
        "unchanged_Cycle612_JointOrder": all((
            joint["consistent_statuses"] == ("admitted", "admitted"),
            joint["consistent_acyclic"],
            joint["inverted_first"] == "admitted",
            joint["inverted_refusal"] == "refused_inverted",
            joint["forced_cycle_detected"],
            joint["no_endpoint_status"] == "no_opportunity",
            joint["JointOrder_class_module"] == C704.C612.JointOrder.__module__,
        )),
        "unchanged_Cycle704_host_control": all((
            unchanged_host["projection_failures"] == 0,
            unchanged_host["interval_failures"] == 0,
            unchanged_host["additivity_closed"],
            unchanged_host["reversal_closed"],
        )),
    }
    report = {
        "cycle": 718,
        "authority": "none",
        "audit": "unset",
        "status": "bounded_conditional_construction",
        "claim_type": "bounded_theorem",
        "declared_inputs": AUDIT_INPUT_PATHS,
        "provenance": provenance,
        "checks": checks,
        "pass": all(checks.values()),
        "direct_spatial_projection_boundary": direct,
        "bit_level_adapter": semantic,
        "physical_route": route,
        "unchanged_Cycle612_JointOrder": joint,
        "unchanged_Cycle704_host_control": unchanged_host,
        "imports": {
            "spatial_ACK_runner_sha256": sha256(Path(R.__file__).read_bytes()).hexdigest(),
            "Cycle704_runner_sha256": sha256(Path(C704.__file__).read_bytes()).hexdigest(),
            "Cycle714_fixed_packet_runner_sha256": sha256(Path(C714.__file__).read_bytes()).hexdigest(),
            "Cycle610_class_module": C704.C610.EventChain.__module__,
            "Cycle612_class_module": C704.C612.JointOrder.__module__,
        },
        "supplied": [
            "one acknowledged literal Cycle713 spatial packet at post-shift station one",
            "one host-selected blank output packet cell per append",
            "empty-head sentinel 63, initial address 0, initial K16 rotor 14, and clean work",
            "actuality, admissibility, law, binder, and finite capacity 24",
            "offline gate word, physical chart, and blank route workspace",
        ],
        "derived": [
            "literal 34-bit Cycle704 payload plus six-bit identity projection",
            "bit-level predecessor/head, K16 rotor/carry, K64 next-address, and freshness transfer",
            "exact append inverse/replay, no-op/refusal/exhaustion controls, and interval additivity/reversal",
            "unchanged Cycle612 consistent/refused/forced-cycle outcomes",
            "nearest-neighbor route from the actual post-shift spatial packet coordinates",
        ],
        "open": [
            "physical blank-cell selection and 24-cell duplicate-membership enforcement",
            "same-cell literal reapplication is active and therefore requires the disclosed moving selector",
            "autonomous blank/fresh/work genesis and renewal after exhaustion",
            "objective occurrence/admission and inaccessible inverse",
            "empirical interval unit, physical time, Record permanence, Born, and source/gravity meaning",
        ],
        "boundary": (
            "The local field update and direct Cycle704/610/612 projection are literal M2.  Repeated bank "
            "collection still uses host selection of a new blank output cell, disclosed separately; applying "
            "the one-cell factor again to its retained output is not a lawful recurrent update.  The "
            "integer interval is not called time and the reversible packet is not a Record."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE718_CYCLE612_INTERVAL_BRIDGE_PASS" if report["pass"] else "CYCLE718_CYCLE612_INTERVAL_BRIDGE_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
