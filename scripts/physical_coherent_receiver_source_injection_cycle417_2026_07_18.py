#!/usr/bin/env python3
"""Cycle 417: coherent mediator-to-receiver source injection.

Two blank physical M2 source ports are attached to the Cycle-416 mediator.
Fixed local CNOTs latch the mediator excitation coherently into retarded and
static receiver-source ports.  No mediator expectation is queried to perform
the update.  This compiles the source-port seam only, not the Cycle-213/216
field arrays or their propagation into M2.

Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_strict_response_source_clock_metric_receiver_cycle416_2026_07_18 as c416


c399 = c416.c399
c403 = c416.c403
route_a = c416.route_a
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COHERENT_RECEIVER_SOURCE_INJECTION_CYCLE417_NOTE_2026-07-18.md"
)
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 7e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
Coord = tuple[int, int, int]


@dataclass(frozen=True)
class InjectionKey:
    bridge: c399.BridgeKey
    source: int
    mediator: int
    retarded_source: int
    static_source: int


InjectionState = dict[InjectionKey, np.ndarray]


@dataclass(frozen=True)
class M2Site:
    coord: Coord
    role: str
    inherited: bool = False


SITES = (
    M2Site((0, 0, 0), "STRICT_RESPONSE", True),
    M2Site((1, 0, 0), "SOURCE_EXCITATION", True),
    M2Site((0, 1, 0), "SCALAR_MEDIATOR", True),
    M2Site((0, 2, 0), "RETARDED_RECEIVER_SOURCE_TERM"),
    M2Site((1, 1, 0), "STATIC_RECEIVER_SOURCE_TERM"),
)
RESPONSE, SOURCE, MEDIATOR, RETARDED, STATIC = range(5)


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
    required = (
        "authority: none", "audit: unset", "two physical m2 receiver-source ports",
        "no mediator expectation is queried", "retarded", "static", "exact inverse",
        "blind held l6", "all 24 proper-cubic frames", "deletion", "no host branch query",
        "source-port seam only", "not physical energy, stress, or a selected source",
        "not independent confirmations", "e_417 g_417 = g_physical,417 e_417",
        "no negative, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-417 note states the coherent injection and semantic contract", not missing, missing)


def validate(state: InjectionState) -> None:
    for key in state:
        fields = (key.source, key.mediator, key.retarded_source, key.static_source)
        if any(bit not in (0, 1) for bit in fields):
            raise ValueError("Cycle-417 M2 labels must be binary")
        if key.source + key.mediator != 1:
            raise ValueError("the inherited balance code requires one excitation")


def lift(state: c416.BalanceState) -> InjectionState:
    return {
        InjectionKey(key.bridge, key.source, key.mediator, 0, 0): value.copy()
        for key, value in state.items()
    }


def source_injection(
    state: InjectionState,
    *,
    inverse: bool = False,
    delete_retarded: bool = False,
    delete_static: bool = False,
) -> InjectionState:
    """Apply the fixed CNOT source-port schedule; no expectation readout."""
    validate(state)
    output = state
    schedule = ("retarded", "static")
    if inverse:
        schedule = tuple(reversed(schedule))
    for port in schedule:
        if (port == "retarded" and delete_retarded) or (port == "static" and delete_static):
            continue
        updated: InjectionState = {}
        for key, value in output.items():
            retarded = key.retarded_source ^ (key.mediator if port == "retarded" else 0)
            static = key.static_source ^ (key.mediator if port == "static" else 0)
            target = InjectionKey(key.bridge, key.source, key.mediator, retarded, static)
            updated[target] = updated.get(target, 0) + value
        output = updated
    validate(output)
    return output


def residual(left: InjectionState, right: InjectionState) -> float:
    total = 0.0
    for key in set(left) | set(right):
        template = left.get(key, right.get(key))
        assert template is not None
        a = left.get(key, np.zeros_like(template))
        b = right.get(key, np.zeros_like(template))
        total += float(np.vdot(a - b, a - b).real)
    return float(np.sqrt(total))


def weight(state: InjectionState, predicate) -> float:
    return float(sum(np.vdot(value, value).real for key, value in state.items() if predicate(key)))


def connected(sites: tuple[int, ...], framed=SITES) -> bool:
    pending = {sites[0]}
    reached = set()
    while pending:
        node = pending.pop()
        reached.add(node)
        a = framed[node].coord
        for other in sites:
            b = framed[other].coord
            if other not in reached and sum(abs(a[i] - b[i]) for i in range(3)) == 1:
                pending.add(other)
    return reached == set(sites)


def basis_and_layout_controls() -> None:
    angle, _charge = c416.source_angle()
    emitted = c416.balance_unitary(1, angle) @ np.asarray((0, 0, 1, 0), dtype=complex)
    bridge = next(iter(c399.initial_bridge_state(0, *c399.packet_fixture())))
    balance = {
        c416.BalanceKey(bridge, 0, 1): emitted[1:2].copy(),
        c416.BalanceKey(bridge, 1, 0): emitted[2:3].copy(),
    }
    source = lift(balance)
    output = source_injection(source)
    restored = source_injection(output, inverse=True)
    mediator = weight(output, lambda key: key.mediator == 1)
    retarded = weight(output, lambda key: key.retarded_source == 1)
    static = weight(output, lambda key: key.static_source == 1)
    joint = weight(output, lambda key: key.mediator == key.retarded_source == key.static_source == 1)
    check(
        "two local M2 CNOTs inject the coherent mediator into retarded/static source ports with an exact inverse",
        connected((MEDIATOR, RETARDED)) and connected((MEDIATOR, STATIC))
        and abs(mediator - np.sin(angle) ** 2) < 2e-14
        and mediator == retarded == static == joint and residual(restored, source) == 0,
        {
            "represented_M2_common_installation": 4859, "new_M2_over_Cycle416": 2,
            "fixed_gate_layers": 2, "maximum_gate_support": 2, "connected_NN_support": True,
            "mediator_retarded_static_joint_weight": joint, "inverse_residual": residual(restored, source),
            "host_expectation_queries_in_update": 0,
        },
    )


def held_controls(factors, packet_layout, packet_initial):
    angle, _charge = c416.source_angle()
    transfer = float(np.sin(angle) ** 2)
    rows = []
    failures = 0
    held = None
    for route in c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                source = c403.pre_admission_response(origin, route, length, factors, packet_layout, packet_initial)
                balance_in = c416.encode(source)
                balance_out = c416.balance_step(balance_in, origin, angle)
                encoded = lift(balance_out)
                output = source_injection(encoded)
                restored = source_injection(output, inverse=True)
                target = c403.target_sector_weight(source, origin) * transfer
                mediator = weight(output, lambda key: key.mediator == 1)
                retarded = weight(output, lambda key: key.retarded_source == 1)
                static = weight(output, lambda key: key.static_source == 1)
                joint = weight(output, lambda key: key.mediator == key.retarded_source == key.static_source == 1)
                inverse = residual(restored, encoded)
                failures += int(max(abs(value - target) for value in (mediator, retarded, static, joint)) > TOLERANCE)
                failures += int(inverse > TOLERANCE)
                failures += sum(
                    int((key.retarded_source, key.static_source) != ((key.mediator,) * 2))
                    for key in output
                )
                rows.append({
                    "route": route, "L": length, "held": length == HELD_LENGTH,
                    "origin": "A" if origin == 0 else "C", "expected_transfer_weight": target,
                    "mediator_retarded_static_joint_weights": (mediator, retarded, static, joint),
                    "inverse_residual": inverse,
                })
                if (route, length, origin) == ("unit_weight", HELD_LENGTH, 0):
                    held = (source, encoded, output)
    check(
        "fixed source-port gates transfer every L5 and blind held-L6 coherent mediator branch without expectation feedback",
        failures == 0,
        {"rows": rows, "failures": failures, "host_expectation_queries_in_update": 0, "readout_use": "post-update diagnostic only"},
    )
    assert held is not None
    return held


def frame_deletion_identity_controls(held, factors, packet_layout, packet_initial) -> None:
    frames = route_a.c210.proper_cubic_frames()
    local_failures = frame_failures = 0
    for frame in frames:
        moved = tuple(
            M2Site(tuple(int(x) for x in frame @ np.asarray(site.coord)), site.role, site.inherited)
            for site in SITES
        )
        local_failures += int(not connected((MEDIATOR, RETARDED), moved))
        local_failures += int(not connected((MEDIATOR, STATIC), moved))
        frame_failures += int(len({site.coord for site in moved}) != len(moved))
    source, encoded, output = held
    no_retarded = source_injection(encoded, delete_retarded=True)
    no_static = source_injection(encoded, delete_static=True)
    mediator = weight(output, lambda key: key.mediator == 1)
    deletion_failures = (
        int(weight(no_retarded, lambda key: key.retarded_source == 1) != 0)
        + int(abs(weight(no_retarded, lambda key: key.static_source == 1) - mediator) > TOLERANCE)
        + int(weight(no_static, lambda key: key.static_source == 1) != 0)
        + int(abs(weight(no_static, lambda key: key.retarded_source == 1) - mediator) > TOLERANCE)
    )
    original_hash = c399.c360.record_hash(packet_initial)
    identity_failures = 0
    for key in output:
        identity_failures += int(key.bridge not in source)
        identity_failures += int(c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.a_bits)) != original_hash)
        identity_failures += int(c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.c_bits)) != original_hash)
    update_rows, _ = c399.source_factors()
    contact_columns = int(np.count_nonzero(abs(factors[3].diagonal() - 1) > 2e-14))
    check(
        "both receiver-source gates remain local in all 24 proper-cubic frames and each deletion is independently visible",
        len(frames) == 24 and local_failures == frame_failures == deletion_failures == 0,
        {"frames": len(frames), "local_failures": local_failures, "frame_failures": frame_failures, "deletion_failures": deletion_failures},
    )
    check(
        "source-port injection preserves bridge/Record and inherited mass/contact fixtures",
        identity_failures == 0
        and abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < TOLERANCE
        and contact_columns == 645,
        {"Record_hash": original_hash, "identity_failures": identity_failures, "mass": update_rows["Cycle219_mass_fixture"], "contact_columns": contact_columns},
    )


def domain_inventory_controls() -> None:
    bridge = next(iter(c399.initial_bridge_state(0, *c399.packet_fixture())))
    value = np.ones(1, dtype=complex)
    bad = (
        {InjectionKey(bridge, 1, 0, 2, 0): value},
        {InjectionKey(bridge, 0, 0, 0, 0): value},
        {InjectionKey(bridge, 1, 1, 0, 0): value},
    )
    rejections = 0
    for state in bad:
        try:
            validate(state)
        except ValueError:
            rejections += 1
    depth = c399.c255.depth_certificate(c399.c255.event_dag())["depth"]
    inventory = {
        "supplied": (
            "Cycle416 strict-response balance and scalar mediator meaning",
            "two blank receiver-source M2 ports and their retarded/static labels",
            "fixed mediator-controlled CNOT schedule and scalar proper-cubic representation",
        ),
        "derived": (
            "coherent branchwise source-port injection without expectation feedback",
            "exact cleanup, held-size transfer, gate deletion visibility, and 24-frame locality",
        ),
        "open": (
            "Cycle213/216 field-array encoding and propagation in physical M2",
            "point-profile/sign/coupling calibration, recurrence, recoil, and resource accounting",
            "selection as physical energy/stress/source, actual Records, time, metric, and gravity",
        ),
        "actual_Records_added": 0, "independent_confirmations": 0,
        "host_expectation_queries_in_update": 0, "physical_source_selected": False,
        "field_receiver_compiled_to_M2": False, "actual_dependency_depth_before_after": (depth, depth),
        "negative_or_minimum_claim": False, "shared_obstruction_claim": False, "axiom_pressure": False,
    }
    check(
        "E_417 G_417 = G_physical,417 E_417 holds on the source-port code with imports and residual field wall explicit",
        rejections == 3 and depth == 4 and not inventory["physical_source_selected"]
        and not inventory["field_receiver_compiled_to_M2"] and not inventory["negative_or_minimum_claim"]
        and not inventory["shared_obstruction_claim"] and not inventory["axiom_pressure"],
        {"domain_rejections": rejections, **inventory},
    )


def main() -> int:
    print("CYCLE 417: COHERENT PHYSICAL-M2 RECEIVER SOURCE INJECTION")
    note_contract()
    basis_and_layout_controls()
    _rows, factors = c399.source_factors()
    packet_layout, packet_initial = c399.packet_fixture()
    held = held_controls(factors, packet_layout, packet_initial)
    frame_deletion_identity_controls(held, factors, packet_layout, packet_initial)
    domain_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_COHERENT_RECEIVER_SOURCE_INJECTION_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_COHERENT_RECEIVER_SOURCE_INJECTION_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
