#!/usr/bin/env python3
"""Cycle 640: physical-M2 endpoint / interval packet interface.

This runner constructs a bounded coherent contact-echo candidate pointer, a
reversible duplicate-safe endpoint certificate, and a reversible local
predecessor/rotor packet matching the immutable Cycle610-612 acceptance
contract from PR #5557.  The packet is a candidate interface.  Its counts are
not time; its pointer/certificate/cells are not occurrences, Records, or
histories.  Actuality, admissibility, and law-domain remain explicit ports.

The current physical shores are Cycle632's fixed-sector E/G and Cycle634's
bounded fixed-menu instrument.  Neither is silently widened to the same-
species Cycle583 A2 stream.  Cycle639's committed local 64x15 wedge2/A2 host
is not consumed as a premise; seam-complete stream/tick composition remains
conditional.

Authority none.  Audit unset.  Constitutional effect none.
"""

from __future__ import annotations

import json
import math
import resource
import signal
import subprocess
import time
from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_M2_ENDPOINT_INTERVAL_PACKET_INTERFACE_CYCLE640_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_m2_endpoint_interval_packet_interface_"
    "cycle640_receipt_2026_07_23.json"
)

PR5557_HEAD = "a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318"
COMMITTED_SHORE_HEAD = "ab87e466684e77b10cefbc799addc4701f8b8e0d"
CYCLE639_COMMITTED_HEAD = "e2719c0f7fceccc3a61e7b4a11049bc1e616550a"
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 120.0
RSS_CAP_BYTES = 1_000_000_000
TOL = 1.0e-12
CONTACT_PHASE = 0.37
IDENTITY_BITS = 6

PR5557_SHA256 = {
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md": "63854c353f477f7beb8371d3a4489c02d8787c54679ab8963c7cc828972a4ea4",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md": "91e0e0bb6c931f7da7a468a7094deffb775523f22b75334322417639edf57056",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md": "028133c490e771dd3012061c79910fcfb88cd6132df072ec15e725fe9bc35496",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py": "61d624d3f47e371a3b99f55a3c60db68c1fe77f5d93a21651f9172b2d49f1458",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py": "9f1d4a2aabca8af1f61ef42071c8d2bce05018eace7a6f0886d769871689a13d",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py": "4494ce889809f6a179fc9bb712aa851fa6e73dac32a7b1bfbdb71903be5fadde",
    "scripts/physical_minus_channel_certification_addendum_cycle612_2026_07_22.py": "5eee5e2b510c92f72dfd9a40ed1633c3257962cb39faf615ad4a9af7f3b4e711",
    "outputs/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_receipt_2026_07_22.json": "0816073d1861bb8b36238ec4948c387801a75442c797baf4a52e335cf6d30ccc",
    "outputs/physical_autonomous_bound_branch_preparation_tournament_cycle611_receipt_2026_07_22.json": "fe9ce56e115d064f82cb3483afc9ea51c6bd76bbdc8a737b8e7bb279119efe6b",
    "outputs/physical_tick_echo_association_causal_order_tournament_cycle612_receipt_2026_07_22.json": "6da06e7c1147b28e74b0f1469fb466018a20f524167e628189e80e5348165cd6",
    "outputs/physical_minus_channel_certification_addendum_cycle612_receipt_2026_07_22.json": "c768c814412b259938f804f18581956d354c680e35c497eeb636fd5d6cae0c10",
}

CURRENT_SHORE_SHA256 = {
    "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_SECTOR_HELD_L6_LITERAL_EG_PRODUCT_TOURNAMENT_CYCLE632_NOTE_2026-07-23.md": "d9ab97e1f46ad9ea7757b5de0d89b080bb101263190dee353263ab7b6ce1e4f2",
    "scripts/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_2026_07_23.py": "3b8e32baf616f64769b45bb6258d7f9f13814c6e7df99a4cea063706a25b597f",
    "outputs/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_receipt_2026_07_23.json": "36f87c42c5cdbd97da5d66f25a2be2a63ad016130087ef56dc4da32d700215ff",
    "docs/work_history/repo/review_feedback/PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md": "d0b8b3b0cb496a3864320c38f2fd8948a42a03252bf18e1b2389618f76f3cd5c",
    "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py": "ca187b7dda5c2b1b56a63ba960695734fc9915177c2769ef957913a096a74d52",
    "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json": "3fd6a476feac3bae38f0da2b6c0d2826432e4b6a605d02d1e99b0d946e6efc87",
}

# Execution evidence from a detached worktree at PR5557_HEAD on 2026-07-23.
# The source runners were byte-pinned above and executed without edits.  Their
# generated receipt digests are run-specific because elapsed time is retained.
UNCHANGED_HARNESS_EXTERNAL_RUN = {
    "execution_ref": PR5557_HEAD,
    "execution_mode": "detached isolated git worktree; source runners unchanged",
    "Cycle610": {
        "runner_sha256": PR5557_SHA256["scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py"],
        "exit_code": 1, "pass_count": 33, "fail_count": 3,
        "generated_receipt_sha256": "ae91bb0e28b91e0db1e89ee1777df393919431da48f038ec799cdd3053ffd93e",
    },
    "Cycle611": {
        "runner_sha256": PR5557_SHA256["scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py"],
        "exit_code": 1, "pass_count": 9, "fail_count": 2,
        "generated_receipt_sha256": "9cc4eabf8824341e5ac5810b2a27833ca5d997052b3294f2e852909c9cd50801",
    },
    "Cycle612_main": {
        "runner_sha256": PR5557_SHA256["scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py"],
        "exit_code": 1, "pass_count": 6, "fail_count": 1,
        "generated_receipt_sha256": "2a00ba531299feb4cfd415b00a8cbef88dcf112d047114f10443bb4cf83c0267",
    },
    "Cycle612_minus_addendum": {
        "runner_sha256": PR5557_SHA256["scripts/physical_minus_channel_certification_addendum_cycle612_2026_07_22.py"],
        "exit_code": 0, "pass_count": 5, "fail_count": 0,
        "generated_receipt_sha256": "bed186c69ace4878753efdeba861388713e092cbcf1952694a8409fe33d01662",
    },
    "outcomes_match_immutable_contract": True,
}

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


def digest(data: bytes) -> str:
    return sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    return digest(path.read_bytes())


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{ref}:{path}"], cwd=ROOT, check=True,
        stdout=subprocess.PIPE,
    ).stdout


def git_json(ref: str, path: str) -> dict[str, object]:
    return json.loads(git_bytes(ref, path))


def git_line(ref: str, path: str, fragment: str) -> int:
    for index, line in enumerate(git_bytes(ref, path).decode().splitlines(), start=1):
        if fragment in line:
            return index
    raise AssertionError((ref, path, fragment))


def repo_line(path: str, fragment: str) -> int:
    for index, line in enumerate((ROOT / path).read_text().splitlines(), start=1):
        if fragment in line:
            return index
    raise AssertionError((path, fragment))


def immutable_shores() -> dict[str, object]:
    observed_pr = {path: digest(git_bytes(PR5557_HEAD, path)) for path in PR5557_SHA256}
    observed_current = {
        path: digest(git_bytes(COMMITTED_SHORE_HEAD, path))
        for path in CURRENT_SHORE_SHA256
    }
    c610 = git_json(
        PR5557_HEAD,
        "outputs/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_receipt_2026_07_22.json",
    )
    c611 = git_json(
        PR5557_HEAD,
        "outputs/physical_autonomous_bound_branch_preparation_tournament_cycle611_receipt_2026_07_22.json",
    )
    c612 = git_json(
        PR5557_HEAD,
        "outputs/physical_tick_echo_association_causal_order_tournament_cycle612_receipt_2026_07_22.json",
    )
    c612a = git_json(
        PR5557_HEAD,
        "outputs/physical_minus_channel_certification_addendum_cycle612_receipt_2026_07_22.json",
    )
    c632 = git_json(
        COMMITTED_SHORE_HEAD,
        "outputs/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_receipt_2026_07_23.json",
    )
    c634 = git_json(
        COMMITTED_SHORE_HEAD,
        "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json",
    )
    semantics = {
        "Cycle610_expected_preregistered_exit_one": (
            c610["pass"] is False and c610["pass_count"] == 33 and c610["fail_count"] == 3
        ),
        "Cycle610_interval_contract": c610["route_b"]["sample_intervals"] == {
            "d_ab": 9, "d_bc": 12, "d_ac": 21,
        } and c610["route_b"]["carries"] == 2,
        "Cycle611_expected_preregistered_exit_one": (
            c611["pass"] is False and c611["pass_count"] == 9 and c611["fail_count"] == 2
        ),
        "Cycle612_expected_preregistered_exit_one": (
            c612["pass"] is False and c612["pass_count"] == 6 and c612["fail_count"] == 1
        ),
        "Cycle612_addendum_positive": (
            c612a["pass"] is True and c612a["pass_count"] == 5 and c612a["fail_count"] == 0
        ),
        "Cycle612_minus_channel_load_bearing": (
            c612a["channel_selection"]["pa_state"] == "minus"
            and c612a["channel_selection"]["contact_off"] == "none"
        ),
        "Cycle632_fixed_sector_only": (
            c632["pass"] is True
            and c632["literal_local_numeric_coin_intertwiner"]["full_local_M64_compiled"] is False
            and c632["fixed_sector_physical_intertwiner"]["factorwise_E_Gcoarse_equals_Gphysical_E"] is True
        ),
        "Cycle634_pointer_candidate_only": (
            c634["pass"] is True
            and c634["six_layer_contract"]["pointer_port_is_occurrence"] is False
            and c634["six_layer_contract"]["pointer_port_is_Record"] is False
        ),
    }
    passed = (
        observed_pr == PR5557_SHA256
        and observed_current == CURRENT_SHORE_SHA256
        and all(semantics.values())
    )
    result = {
        "PR5557_head": PR5557_HEAD,
        "current_committed_shore_head": COMMITTED_SHORE_HEAD,
        "expected_PR5557_sha256": PR5557_SHA256,
        "observed_PR5557_sha256": observed_pr,
        "expected_current_sha256": CURRENT_SHORE_SHA256,
        "observed_current_sha256": observed_current,
        "semantic_acceptance_contract": semantics,
        "working_tree_bytes_used_as_premise": False,
        "Cycle639_committed_local_wedge2_A2_host_consumed_as_premise": False,
        "pass": passed,
    }
    check("PR5557 Cycle610-612 and committed Cycle632/634 shores are immutable",
          passed, {"files": len(observed_pr) + len(observed_current),
                   "semantic_rows": len(semantics)})
    return result


# ---------------------------------------------------------------------------
# Physical two-path contact echo and Cycle634-compatible binary effect.
# ---------------------------------------------------------------------------

I2 = np.eye(2, dtype=complex)
P0 = np.diag([1.0, 0.0]).astype(complex)
P1 = np.diag([0.0, 1.0]).astype(complex)
H = np.asarray([[1, 1], [1, -1]], complex) / math.sqrt(2.0)


def hermitian_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.conj().T) / 2)
    return (vectors * np.sqrt(np.clip(values, 0.0, None))) @ vectors.conj().T


def binary_dilation(effect: np.ndarray) -> np.ndarray:
    root_e = hermitian_sqrt(effect)
    root_c = hermitian_sqrt(I2 - effect)
    return (
        np.kron(root_c, P0) - np.kron(root_e, np.asarray([[0, 1], [0, 0]], complex))
        + np.kron(root_e, np.asarray([[0, 0], [1, 0]], complex)) + np.kron(root_c, P1)
    )


def pointer_kraus(unitary: np.ndarray, pointer: int) -> np.ndarray:
    tensor = unitary.reshape(2, 2, 2, 2)
    return tensor[:, pointer, :, 0]


def contact_echo_instrument() -> dict[str, object]:
    matter_phase = np.diag([1.0, np.exp(1j * CONTACT_PHASE)])
    controlled = np.kron(I2, P0) + np.kron(matter_phase, P1)
    h_pointer = np.kron(I2, H)
    echo = h_pointer @ controlled @ h_pointer
    k1 = pointer_kraus(echo, 1)
    effect = k1.conj().T @ k1
    expected = np.diag([0.0, math.sin(CONTACT_PHASE / 2) ** 2])
    canonical = binary_dilation(expected)
    canonical_effect = pointer_kraus(canonical, 1).conj().T @ pointer_kraus(canonical, 1)

    contact_off = h_pointer @ np.eye(4) @ h_pointer
    off_effect = pointer_kraus(contact_off, 1).conj().T @ pointer_kraus(contact_off, 1)
    deletion_rows = []
    for label, candidate in (
        ("delete_first_H", h_pointer @ controlled),
        ("delete_controlled_contact", h_pointer @ h_pointer),
        ("delete_final_H", controlled @ h_pointer),
    ):
        deleted_k1 = pointer_kraus(candidate, 1)
        deleted_effect = deleted_k1.conj().T @ deleted_k1
        deletion_rows.append({
            "deletion": label,
            "effect_difference": float(np.linalg.norm(deleted_effect - effect, ord=2)),
        })
    inverse = float(np.linalg.norm(echo.conj().T @ echo - np.eye(4), ord=2))
    effect_residual = float(np.linalg.norm(effect - expected, ord=2))
    cycle634_residual = float(np.linalg.norm(canonical_effect - effect, ord=2))
    off_residual = float(np.linalg.norm(off_effect, ord=2))
    passed = (
        inverse < TOL and effect_residual < TOL and cycle634_residual < TOL
        and off_residual < TOL
        and all(row["effect_difference"] > 1.0e-3 for row in deletion_rows)
    )
    result = {
        "matter_input": "one supplied local contact-eigenflag M2; extraction from the committed Cycle639 64x15 local A2 payload is not consumed",
        "contact_phase": CONTACT_PHASE,
        "pointer_one_effect": effect.real.tolist(),
        "pointer_one_probability_on_contact_flag_one": float(expected[1, 1]),
        "contact_off_pointer_one_effect_residual": off_residual,
        "contact_deletion_kills_candidate_pointer": off_residual < TOL,
        "echo_unitary_inverse_residual": inverse,
        "direct_effect_residual": effect_residual,
        "Cycle634_positive_root_binary_effect_residual": cycle634_residual,
        "system_plus_pointer_M2": 2,
        "maximum_native_echo_gate_support_M2": 2,
        "pointer_is_coherent_candidate_not_occurrence": True,
        "deletion_rows": deletion_rows,
        "pass": passed,
    }
    check("a bounded coherent contact echo gives a Cycle634-compatible candidate pointer and contact deletion kills it",
          passed, {"on": float(expected[1, 1]), "off": off_residual,
                   "effect": cycle634_residual})
    return result


# ---------------------------------------------------------------------------
# Reversible bounded-support Boolean gates.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Gate:
    label: str
    kind: str
    controls: tuple[tuple[str, int], ...]
    targets: tuple[str, ...]

    @property
    def support(self) -> int:
        return len(self.controls) + len(self.targets)

    def apply(self, state: dict[str, int]) -> None:
        if not all(state.get(name, 0) == value for name, value in self.controls):
            return
        if self.kind == "toggle":
            state[self.targets[0]] = state.get(self.targets[0], 0) ^ 1
        elif self.kind == "swap":
            left, right = self.targets
            state[left], state[right] = state.get(right, 0), state.get(left, 0)
        else:
            raise ValueError(self.kind)


def toggle(label: str, target: str, *controls: tuple[str, int]) -> Gate:
    return Gate(label, "toggle", tuple(controls), (target,))


def fredkin(label: str, left: str, right: str, control: tuple[str, int]) -> Gate:
    return Gate(label, "swap", (control,), (left, right))


def apply_circuit(state: dict[str, int], gates: list[Gate],
                  reverse: bool = False, delete_label: str | None = None) -> None:
    iterable = reversed(gates) if reverse else gates
    for gate in iterable:
        if gate.label != delete_label:
            gate.apply(state)


def and_ladder(prefix: str, controls: list[tuple[str, int]]) -> tuple[list[Gate], str, list[str]]:
    assert len(controls) >= 2
    work = [f"{prefix}_and_{i}" for i in range(len(controls) - 1)]
    gates = [toggle(f"{prefix}_and_compute_0", work[0], controls[0], controls[1])]
    for index, control in enumerate(controls[2:], start=1):
        gates.append(toggle(f"{prefix}_and_compute_{index}", work[index],
                            (work[index - 1], 1), control))
    return gates, work[-1], work


def endpoint_circuit(prefix: str, claimed: str, input_prefix: str) -> tuple[list[Gate], dict[str, str], list[str]]:
    names = {
        "contact": f"{input_prefix}_contact_pointer",
        "crossing": f"{input_prefix}_crossing",
        "channel_ok": f"{input_prefix}_channel_certified",
        "convention_ok": f"{input_prefix}_convention_certified",
        "orientation": f"{input_prefix}_orientation",
        "channel": f"{input_prefix}_channel_sign",
        "convention": f"{input_prefix}_tick_convention",
        "certificate": f"{prefix}_certificate",
        "out_orientation": f"{prefix}_orientation",
        "out_channel": f"{prefix}_channel_sign",
        "out_convention": f"{prefix}_tick_convention",
        "token": f"{prefix}_token",
    }
    controls = [
        (names["contact"], 1), (names["crossing"], 1),
        (names["channel_ok"], 1), (names["convention_ok"], 1),
        (claimed, 0),
    ]
    compute, enable, work = and_ladder(f"{prefix}_endpoint", controls)
    uncompute = [
        Gate(g.label.replace("compute", "uncompute"), g.kind, g.controls, g.targets)
        for g in reversed(compute)
    ]
    gates = compute + [
        toggle(f"{prefix}_certificate_emit", names["certificate"], (enable, 1)),
        toggle(f"{prefix}_orientation_copy", names["out_orientation"],
               (names["certificate"], 1), (names["orientation"], 1)),
        toggle(f"{prefix}_channel_copy", names["out_channel"],
               (names["certificate"], 1), (names["channel"], 1)),
        toggle(f"{prefix}_convention_copy", names["out_convention"],
               (names["certificate"], 1), (names["convention"], 1)),
        toggle(f"{prefix}_token_emit", names["token"], (names["certificate"], 1)),
    ] + uncompute + [
        toggle(f"{prefix}_claim_latch", claimed, (names["certificate"], 1)),
    ]
    return gates, names, work


def endpoint_predicate_tournament() -> dict[str, object]:
    failures = 0
    rows = 0
    gates, names, work = endpoint_circuit("p0", "claimed", "in")
    for values in product((0, 1), repeat=8):
        contact, crossing, channel_ok, convention_ok, claimed, orient, channel, conv = values
        state = {
            names["contact"]: contact, names["crossing"]: crossing,
            names["channel_ok"]: channel_ok, names["convention_ok"]: convention_ok,
            "claimed": claimed, names["orientation"]: orient,
            names["channel"]: channel, names["convention"]: conv,
        }
        original = dict(state)
        apply_circuit(state, gates)
        expected = contact & crossing & channel_ok & convention_ok & (1 - claimed)
        good = (
            state.get(names["certificate"], 0) == expected
            and state.get(names["token"], 0) == expected
            and state.get(names["out_orientation"], 0) == expected * orient
            and state.get(names["out_channel"], 0) == expected * channel
            and state.get(names["out_convention"], 0) == expected * conv
            and state.get("claimed", 0) == (claimed ^ expected)
            and all(state.get(bit, 0) == 0 for bit in work)
        )
        restored = dict(state)
        apply_circuit(restored, gates, reverse=True)
        good &= all(restored.get(key, 0) == value for key, value in original.items())
        good &= all(restored.get(key, 0) == 0 for key in set(restored) - set(original))
        failures += int(not good)
        rows += 1

    duplicate_state = {
        "in_contact_pointer": 1, "in_crossing": 1,
        "in_channel_certified": 1, "in_convention_certified": 1,
        "in_orientation": 1, "in_channel_sign": 1, "in_tick_convention": 1,
        "claimed": 0,
    }
    apply_circuit(duplicate_state, gates)
    gates2, names2, work2 = endpoint_circuit("p1", "claimed", "in")
    apply_circuit(duplicate_state, gates2)
    duplicate_refused = (
        duplicate_state.get("p0_certificate", 0) == 1
        and duplicate_state.get("p1_certificate", 0) == 0
        and duplicate_state["claimed"] == 1
        and all(duplicate_state.get(bit, 0) == 0 for bit in work + work2)
    )

    baseline = {
        "in_contact_pointer": 1, "in_crossing": 1,
        "in_channel_certified": 1, "in_convention_certified": 1,
        "in_orientation": 1, "in_channel_sign": 1, "in_tick_convention": 1,
        "claimed": 0,
    }
    expected = dict(baseline)
    apply_circuit(expected, gates)
    deletion_labels = [
        "p0_endpoint_and_compute_0", "p0_certificate_emit", "p0_orientation_copy",
        "p0_channel_copy", "p0_convention_copy", "p0_token_emit",
        "p0_endpoint_and_uncompute_0", "p0_claim_latch",
    ]
    deletion_rows = []
    for label in deletion_labels:
        damaged = dict(baseline)
        apply_circuit(damaged, gates, delete_label=label)
        keys = set(expected) | set(damaged)
        hamming = sum(expected.get(key, 0) != damaged.get(key, 0) for key in keys)
        full_inverse = dict(damaged)
        apply_circuit(full_inverse, gates, reverse=True)
        inverse_hamming = sum(
            full_inverse.get(key, 0) != baseline.get(key, 0)
            for key in set(full_inverse) | set(baseline)
        )
        deletion_rows.append({"deleted_gate": label, "output_hamming": hamming,
                              "full_inverse_visible_hamming": inverse_hamming})
    deletion_pass = all(row["output_hamming"] > 0 and row["full_inverse_visible_hamming"] > 0
                        for row in deletion_rows)
    resources = {
        "local_contact_eigenflag_M2": 1,
        "echo_pointer_M2": 1,
        "endpoint_boolean_input_M2_including_pointer": 8,
        "endpoint_output_M2": 5,
        "endpoint_work_M2": len(work),
        "total_distinct_local_M2": 1 + 8 + 5 + len(work),
        "gate_count": len(gates),
        "maximum_gate_support_M2": max(g.support for g in gates),
    }
    passed = failures == 0 and duplicate_refused and deletion_pass and resources["maximum_gate_support_M2"] <= 3
    result = {
        "predicate": "contact_pointer AND crossing AND channel_certified AND convention_certified AND NOT claimed",
        "truth_table_rows": rows,
        "truth_table_failures": failures,
        "duplicate_second_certificate_refused": duplicate_refused,
        "channel_sign_port": "one retained M2 copied into a valid certificate; 0=plus, 1=minus",
        "tick_convention_port": "one retained M2 copied into a valid certificate; 0=T1, 1=T2",
        "crossing_orientation_port": "one retained M2; invariant under spatial proper-cubic frames",
        "channel_or_convention_selected_by_host_at_runtime": False,
        "channel_certification_and_convention_certificate_supplied": True,
        "line_agnostic_hardware": True,
        "second_A2_line_or_root_used": False,
        "work_returned_blank": True,
        "deletion_rows": deletion_rows,
        "resources": resources,
        "pass": passed,
    }
    check("the endpoint predicate is bounded, oriented, duplicate-safe, channel/convention explicit, and deletion-sensitive",
          passed, {"truth_rows": rows, "failures": failures,
                   "duplicate_refused": duplicate_refused,
                   "max_support": resources["maximum_gate_support_M2"]})
    return result


# ---------------------------------------------------------------------------
# Reversible local predecessor / rotor / carry packet.
# ---------------------------------------------------------------------------

CELL_FIELDS = {
    "identity": IDENTITY_BITS,
    "predecessor": IDENTITY_BITS,
    "rotor": 4,
    "carry": 1,
    "binder": 1,
    "valid": 1,
    "orientation": 1,
    "channel": 1,
    "convention": 1,
    "head": 1,
}


def bit_name(prefix: str, field: str, index: int = 0) -> str:
    width = CELL_FIELDS.get(field, 1)
    return f"{prefix}_{field}_{index}" if width > 1 else f"{prefix}_{field}"


def set_integer(state: dict[str, int], prefix: str, field: str, value: int) -> None:
    for index in range(CELL_FIELDS[field]):
        state[bit_name(prefix, field, index)] = (value >> index) & 1


def get_integer(state: dict[str, int], prefix: str, field: str) -> int:
    return sum(state.get(bit_name(prefix, field, index), 0) << index
               for index in range(CELL_FIELDS[field]))


def packet_bit(prefix: str, field: str, index: int = 0) -> str:
    width = IDENTITY_BITS if field == "identity" else 1
    return f"{prefix}_{field}_{index}" if width > 1 else f"{prefix}_{field}"


def packet_circuit(src: str, tgt: str, pkt: str, port: str,
                   prefix: str) -> tuple[list[Gate], list[str]]:
    controls = [
        (packet_bit(pkt, "token"), 1),
        (bit_name(src, "head"), 1),
        (bit_name(src, "valid"), 1),
        (f"{port}_binder", 1),
        (f"{port}_actuality", 1),
        (f"{port}_admissibility", 1),
        (f"{port}_law_domain", 1),
    ]
    compute, enable, enable_work = and_ladder(f"{prefix}_admit", controls)
    uncompute = [
        Gate(g.label.replace("compute", "uncompute"), g.kind, g.controls, g.targets)
        for g in reversed(compute)
    ]
    body: list[Gate] = []
    for index in range(IDENTITY_BITS):
        body.append(toggle(f"{prefix}_identity_copy_{index}",
                           bit_name(tgt, "identity", index),
                           (enable, 1), (packet_bit(pkt, "identity", index), 1)))
        body.append(toggle(f"{prefix}_predecessor_copy_{index}",
                           bit_name(tgt, "predecessor", index),
                           (enable, 1), (bit_name(src, "identity", index), 1)))
    for index in range(4):
        body.append(toggle(f"{prefix}_rotor_copy_{index}", bit_name(tgt, "rotor", index),
                           (enable, 1), (bit_name(src, "rotor", index), 1)))
    body.append(toggle(f"{prefix}_rotor_increment_bit0", bit_name(tgt, "rotor", 0),
                       (enable, 1)))
    body.append(toggle(f"{prefix}_rotor_increment_bit1", bit_name(tgt, "rotor", 1),
                       (enable, 1), (bit_name(src, "rotor", 0), 1)))
    increment_work: list[str] = []
    for target_index in (2, 3):
        lower = [(bit_name(src, "rotor", i), 1) for i in range(target_index)]
        ladder, lower_enable, lower_work = and_ladder(
            f"{prefix}_inc{target_index}", lower)
        body.extend(ladder)
        body.append(toggle(f"{prefix}_rotor_increment_bit{target_index}",
                           bit_name(tgt, "rotor", target_index),
                           (enable, 1), (lower_enable, 1)))
        body.extend([
            Gate(g.label.replace("compute", "uncompute"), g.kind, g.controls, g.targets)
            for g in reversed(ladder)
        ])
        increment_work.extend(lower_work)
    carry_ladder, carry_enable, carry_work = and_ladder(
        f"{prefix}_carry", [(bit_name(src, "rotor", i), 1) for i in range(4)]
    )
    body.extend(carry_ladder)
    body.append(toggle(f"{prefix}_carry_set", bit_name(tgt, "carry"),
                       (enable, 1), (carry_enable, 1)))
    body.extend([
        Gate(g.label.replace("compute", "uncompute"), g.kind, g.controls, g.targets)
        for g in reversed(carry_ladder)
    ])
    body.extend([
        toggle(f"{prefix}_binder_copy", bit_name(tgt, "binder"), (enable, 1)),
        toggle(f"{prefix}_orientation_copy", bit_name(tgt, "orientation"),
               (enable, 1), (packet_bit(pkt, "orientation"), 1)),
        toggle(f"{prefix}_channel_copy", bit_name(tgt, "channel"),
               (enable, 1), (packet_bit(pkt, "channel_sign"), 1)),
        toggle(f"{prefix}_convention_copy", bit_name(tgt, "convention"),
               (enable, 1), (packet_bit(pkt, "tick_convention"), 1)),
        toggle(f"{prefix}_valid_set", bit_name(tgt, "valid"), (enable, 1)),
    ])
    tail = [
        toggle(f"{prefix}_token_consume", packet_bit(pkt, "token"),
               (bit_name(tgt, "valid"), 1)),
        fredkin(f"{prefix}_head_move", bit_name(src, "head"), bit_name(tgt, "head"),
                (bit_name(tgt, "valid"), 1)),
    ]
    return compute + body + uncompute + tail, enable_work + increment_work + carry_work


def blank_cell(state: dict[str, int], prefix: str) -> bool:
    return all(state.get(bit_name(prefix, field, index), 0) == 0
               for field, width in CELL_FIELDS.items() for index in range(width))


def initialize_source(state: dict[str, int], prefix: str, identity: int, rotor: int) -> None:
    set_integer(state, prefix, "identity", identity)
    set_integer(state, prefix, "rotor", rotor)
    state[bit_name(prefix, "valid")] = 1
    state[bit_name(prefix, "binder")] = 1
    state[bit_name(prefix, "head")] = 1


def initialize_packet(state: dict[str, int], prefix: str, identity: int,
                      orientation: int, channel: int, convention: int) -> None:
    for index in range(IDENTITY_BITS):
        state[packet_bit(prefix, "identity", index)] = (identity >> index) & 1
    state[packet_bit(prefix, "token")] = 1
    state[packet_bit(prefix, "orientation")] = orientation
    state[packet_bit(prefix, "channel_sign")] = channel
    state[packet_bit(prefix, "tick_convention")] = convention


def initialize_ports(state: dict[str, int], prefix: str, values: tuple[int, int, int, int]) -> None:
    for name, value in zip(("binder", "actuality", "admissibility", "law_domain"), values):
        state[f"{prefix}_{name}"] = value


def cell_dict(state: dict[str, int], prefix: str) -> dict[str, int]:
    return {
        field: (get_integer(state, prefix, field) if width > 1
                else state.get(bit_name(prefix, field), 0))
        for field, width in CELL_FIELDS.items()
    }


def decode_interval(cells: list[dict[str, int]], start: int, end: int) -> int | None:
    if start == end:
        return 0 if any(cell["identity"] == start and cell["valid"] for cell in cells) else None
    if start > end:
        reverse = decode_interval(cells, end, start)
        return None if reverse is None else -reverse
    by_id = {cell["identity"]: cell for cell in cells if cell["valid"]}
    if start not in by_id or end not in by_id or len(by_id) != sum(c["valid"] for c in cells):
        return None
    path = []
    current = by_id[end]
    visited = set()
    while current["identity"] != start:
        if current["identity"] in visited or not current["binder"]:
            return None
        visited.add(current["identity"])
        predecessor = current["predecessor"]
        if predecessor not in by_id:
            return None
        previous = by_id[predecessor]
        if current["rotor"] != (previous["rotor"] + 1) % 16:
            return None
        if current["carry"] != int(previous["rotor"] == 15):
            return None
        path.append(current)
        current = previous
    carries = sum(cell["carry"] for cell in path)
    return 16 * carries + by_id[end]["rotor"] - by_id[start]["rotor"]


def packet_unit_tournament() -> dict[str, object]:
    failures = 0
    cases = 0
    gates, work = packet_circuit("src", "tgt", "pkt", "port", "u")
    for rotor in range(16):
        for ports in product((0, 1), repeat=4):
            for token, orient, channel, conv in product((0, 1), repeat=4):
                state: dict[str, int] = {}
                initialize_source(state, "src", 21, rotor)
                initialize_packet(state, "pkt", 22, orient, channel, conv)
                state[packet_bit("pkt", "token")] = token
                initialize_ports(state, "port", ports)
                original = dict(state)
                apply_circuit(state, gates)
                enabled = token and all(ports)
                target = cell_dict(state, "tgt")
                good = all(state.get(bit, 0) == 0 for bit in work)
                if enabled:
                    good &= (
                        target["identity"] == 22 and target["predecessor"] == 21
                        and target["rotor"] == (rotor + 1) % 16
                        and target["carry"] == int(rotor == 15)
                        and target["valid"] == 1 and target["binder"] == 1
                        and target["orientation"] == orient
                        and target["channel"] == channel
                        and target["convention"] == conv
                        and target["head"] == 1
                        and state[bit_name("src", "head")] == 0
                        and state[packet_bit("pkt", "token")] == 0
                    )
                else:
                    good &= blank_cell(state, "tgt")
                    good &= state[bit_name("src", "head")] == 1
                    good &= state[packet_bit("pkt", "token")] == token
                restored = dict(state)
                apply_circuit(restored, gates, reverse=True)
                good &= all(restored.get(key, 0) == value for key, value in original.items())
                good &= all(restored.get(key, 0) == 0 for key in set(restored) - set(original))
                failures += int(not good)
                cases += 1

    dirty_rows = []
    for field, width in CELL_FIELDS.items():
        for index in range(width):
            malformed = {bit_name("tgt", field, index): 1}
            dirty_rows.append({"bit": bit_name("tgt", field, index),
                               "declared_blank_code_refuses": not blank_cell(malformed, "tgt")})

    baseline: dict[str, int] = {}
    initialize_source(baseline, "src", 21, 15)
    initialize_packet(baseline, "pkt", 22, 1, 1, 1)
    initialize_ports(baseline, "port", (1, 1, 1, 1))
    expected = dict(baseline)
    apply_circuit(expected, gates)
    deletion_labels = [
        "u_predecessor_copy_0", "u_rotor_increment_bit0", "u_carry_set",
        "u_binder_copy", "u_orientation_copy", "u_valid_set",
        "u_admit_and_uncompute_0", "u_token_consume", "u_head_move",
    ]
    deletion_rows = []
    for label in deletion_labels:
        damaged = dict(baseline)
        apply_circuit(damaged, gates, delete_label=label)
        hamming = sum(
            expected.get(key, 0) != damaged.get(key, 0)
            for key in set(expected) | set(damaged)
        )
        inverse = dict(damaged)
        apply_circuit(inverse, gates, reverse=True)
        inverse_hamming = sum(
            inverse.get(key, 0) != baseline.get(key, 0)
            for key in set(inverse) | set(baseline)
        )
        deletion_rows.append({"deleted_gate": label, "output_hamming": hamming,
                              "full_inverse_visible_hamming": inverse_hamming})

    binder_deleted = dict(baseline)
    binder_deleted["port_binder"] = 0
    apply_circuit(binder_deleted, gates)
    binder_kill = blank_cell(binder_deleted, "tgt") and binder_deleted[packet_bit("pkt", "token")] == 1
    port_rows = []
    for port_name in ("actuality", "admissibility", "law_domain"):
        state = dict(baseline)
        state[f"port_{port_name}"] = 0
        apply_circuit(state, gates)
        port_rows.append({"deleted_port": port_name,
                          "admission_refused": blank_cell(state, "tgt")})

    once = dict(baseline)
    apply_circuit(once, gates)
    # The consumed packet is offered to a fresh target from the new local head.
    second_gates, second_work = packet_circuit("tgt", "tgt2", "pkt", "port", "u2")
    apply_circuit(once, second_gates)
    exactly_once = blank_cell(once, "tgt2") and once[packet_bit("pkt", "token")] == 0

    counts = {kind: sum(g.kind == kind for g in gates) for kind in ("toggle", "swap")}
    resources = {
        "cell_M2": sum(CELL_FIELDS.values()),
        "packet_M2": IDENTITY_BITS + 4,
        "explicit_admission_port_M2": 4,
        "two_cell_packet_and_work_neighborhood_M2": (
            2 * sum(CELL_FIELDS.values()) + IDENTITY_BITS + 4 + 4 + len(set(work))
        ),
        "gate_count": len(gates),
        "gate_counts": counts,
        "maximum_gate_support_M2": max(g.support for g in gates),
        "work_M2": len(set(work)),
        "identity_width_bits": IDENTITY_BITS,
        "declared_maximum_identity": 2**IDENTITY_BITS - 1,
    }
    passed = (
        failures == 0 and all(row["declared_blank_code_refuses"] for row in dirty_rows)
        and all(row["output_hamming"] > 0 and row["full_inverse_visible_hamming"] > 0
                for row in deletion_rows)
        and binder_kill and all(row["admission_refused"] for row in port_rows)
        and exactly_once and resources["maximum_gate_support_M2"] <= 3
    )
    result = {
        "basis_cases_exhausted": cases,
        "basis_case_failures": failures,
        "update": "one-use packet token AND local source head/valid AND binder/actuality/admissibility/law-domain; copy identity/predecessor/metadata; increment K16; K15->K0 carry; consume token; move head",
        "predecessor_source": "identity copied from the adjacent cell carrying the unique local head marker",
        "exactly_once": exactly_once,
        "binder_deletion_blocks_opportunity": binder_kill,
        "explicit_port_deletions": port_rows,
        "target_blank_local_input_constraints": dirty_rows,
        "blank_target_genesis_supplied_not_autonomous": True,
        "deletion_rows": deletion_rows,
        "resources": resources,
        "second_attempt_work_blank": all(once.get(bit, 0) == 0 for bit in second_work),
        "pass": passed,
    }
    check("the local packet is reversible, exactly-once, K15->K0 carry exact, binder/port/deletion sensitive, and head-local",
          passed, {"cases": cases, "failures": failures, "once": exactly_once,
                   "max_support": resources["maximum_gate_support_M2"]})
    return result


def build_chain(length: int) -> dict[str, object]:
    event_count = 24 + length
    state: dict[str, int] = {}
    initialize_source(state, "root", 63, 14)
    source = "root"
    all_work: list[str] = []
    for identity in range(event_count):
        target = f"c{identity}"
        packet = f"p{identity}"
        endpoint_input = f"e{identity}"
        claimed = f"e{identity}_claimed"
        state.update({
            f"{endpoint_input}_contact_pointer": 1,
            f"{endpoint_input}_crossing": 1,
            f"{endpoint_input}_channel_certified": 1,
            f"{endpoint_input}_convention_certified": 1,
            f"{endpoint_input}_orientation": identity & 1,
            f"{endpoint_input}_channel_sign": (identity // 2) & 1,
            f"{endpoint_input}_tick_convention": (identity // 4) & 1,
            claimed: 0,
        })
        endpoint_gates, endpoint_names, endpoint_work = endpoint_circuit(
            packet, claimed, endpoint_input
        )
        for index in range(IDENTITY_BITS):
            state[packet_bit(packet, "identity", index)] = (identity >> index) & 1
        apply_circuit(state, endpoint_gates)
        port = f"a{identity}"
        initialize_ports(state, port, (1, 1, 1, 1))
        gates, work = packet_circuit(source, target, packet, port, f"link{identity}")
        apply_circuit(state, gates)
        all_work.extend(endpoint_work + work)
        source = target
    cells = [cell_dict(state, f"c{i}") for i in range(event_count)]
    d_ab = decode_interval(cells, 2, 11)
    d_bc = decode_interval(cells, 11, 23)
    d_ac = decode_interval(cells, 2, 23)
    missing = [dict(cell) for cell in cells if cell["identity"] != 10]
    binder_broken = [dict(cell) for cell in cells]
    binder_broken[10]["binder"] = 0
    rotor_broken = [dict(cell) for cell in cells]
    rotor_broken[10]["rotor"] ^= 1
    carry_broken = [dict(cell) for cell in cells]
    carry_broken[17]["carry"] = 0
    passed = (
        d_ab == 9 and d_bc == 12 and d_ac == 21
        and decode_interval(cells, 11, 2) == -9
        and sum(cell["carry"] for cell in cells[:24]) == 2
        and decode_interval(missing, 2, 23) is None
        and decode_interval(binder_broken, 2, 23) is None
        and decode_interval(rotor_broken, 2, 23) is None
        and decode_interval(carry_broken, 2, 23) is None
        and sum(cell["head"] for cell in cells) == 1 and cells[-1]["head"] == 1
        and all(state.get(bit, 0) == 0 for bit in all_work)
    )
    return {
        "length": length,
        "split": {3: "construction", 6: "train", 7: "held-out-no-refit"}[length],
        "events": event_count,
        "intervals": {"d_ab": d_ab, "d_bc": d_bc, "d_ac": d_ac},
        "orientation_reverse": decode_interval(cells, 11, 2),
        "carries_first_24": sum(cell["carry"] for cell in cells[:24]),
        "lineage_gap_is_undefined": decode_interval(missing, 2, 23) is None,
        "binder_gap_is_undefined": decode_interval(binder_broken, 2, 23) is None,
        "rotor_deletion_is_undefined": decode_interval(rotor_broken, 2, 23) is None,
        "carry_deletion_is_undefined": decode_interval(carry_broken, 2, 23) is None,
        "unique_terminal_local_head": sum(cell["head"] for cell in cells) == 1 and cells[-1]["head"] == 1,
        "decoder_inputs_update_ordinal": False,
        "work_returned_blank": all(state.get(bit, 0) == 0 for bit in all_work),
        "pass": passed,
    }


def chain_and_cycle610_adapter() -> dict[str, object]:
    rows = [build_chain(length) for length in (3, 6, 7)]
    exact = all(row["pass"] for row in rows)
    result = {
        "rows": rows,
        "Cycle610_sample_interval_match": exact and all(
            row["intervals"] == {"d_ab": 9, "d_bc": 12, "d_ac": 21}
            and row["carries_first_24"] == 2 for row in rows
        ),
        "Cycle610_status_semantics": {
            "duplicate": "one-use packet token produces no target cell",
            "binder_deleted": "no target cell",
            "actuality_or_admissibility_or_law_domain_deleted": "no target cell",
            "lineage_gap": None,
        },
        "full_Cycle610_tick_word_composed_to_physical_stream": False,
        "reason": "Cycle640 consumes a certified crossing packet interface; the same-species A2 seam-complete physical stream and detector crossing circuit are not yet committed shores",
        "pass": exact,
    }
    check("L3/L6/L7 packets reproduce the Cycle610 9+12=21/two-carry acceptance row and return undefined on gaps",
          result["pass"] and result["Cycle610_sample_interval_match"],
          {"sizes": len(rows), "held": rows[-1]["pass"]})
    return result


# ---------------------------------------------------------------------------
# Proper-cubic schedule-label covariance.
# ---------------------------------------------------------------------------

def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        base = np.eye(3, dtype=int)[:, order]
        for signs in product((-1, 1), repeat=3):
            frame = base @ np.diag(signs)
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    unique = {tuple(frame.reshape(-1)): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


def signed_axis(frame: np.ndarray, axis: int, sign: int) -> tuple[int, int]:
    image = sign * (frame @ np.eye(3, dtype=int)[:, axis])
    target = int(np.flatnonzero(image)[0])
    return target, int(image[target])


def covariance_controls(endpoint: dict[str, object], packet: dict[str, object]) -> dict[str, object]:
    frames = proper_cubic_frames()
    failures = 0
    rows = []
    labels = tuple((axis, sign, orientation, channel, convention)
                   for axis in range(3) for sign in (-1, 1)
                   for orientation, channel, convention in product((0, 1), repeat=3))
    for length in (3, 6, 7):
        bijection_failures = 0
        group_failures = 0
        for frame in frames:
            mapped = []
            for axis, sign, orientation, channel, convention in labels:
                target_axis, target_sign = signed_axis(frame, axis, sign)
                mapped.append((target_axis, target_sign, orientation, channel, convention))
            bijection_failures += int(len(set(mapped)) != len(labels))
        for left in frames:
            for right in frames:
                for axis, sign, orientation, channel, convention in labels:
                    mid_axis, mid_sign = signed_axis(right, axis, sign)
                    composed_axis, composed_sign = signed_axis(left, mid_axis, mid_sign)
                    direct_axis, direct_sign = signed_axis(left @ right, axis, sign)
                    if (composed_axis, composed_sign, orientation, channel, convention) != (
                        direct_axis, direct_sign, orientation, channel, convention
                    ):
                        group_failures += 1
                        break
        failures += bijection_failures + group_failures
        rows.append({
            "length": length,
            "split": {3: "construction", 6: "train", 7: "held-out-no-refit"}[length],
            "oriented_apparatus_labels": len(labels),
            "all24_bijection_failures": bijection_failures,
            "all576_group_failures": group_failures,
            "endpoint_M2_per_local_packet": endpoint["resources"]["total_distinct_local_M2"],
            "interval_cell_M2": packet["resources"]["cell_M2"],
            "constant_overhead_per_event_cell": True,
        })
    passed = len(frames) == 24 and failures == 0
    result = {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "spatial_ray_transported": True,
        "crossing_orientation_channel_and_convention_are_spatial_scalars": True,
        "runtime_frame_selector": False,
        "reference_ray_and_bank_direction_supplied": True,
        "rows": rows,
        "pass": passed,
    }
    check("the endpoint/packet label family closes under all24/all576 at L3/L6/L7",
          passed, {"frames": len(frames), "failures": failures})
    return result


def no_go_discipline(shores: dict[str, object], echo: dict[str, object],
                      endpoint: dict[str, object], packet: dict[str, object],
                      adapter: dict[str, object]) -> dict[str, object]:
    families = [
        {"family": "coherent contact echo", "object_formulation": "contact eigenflag plus path-pointer M2",
         "mechanism_invariant": "Hadamard-controlled-contact-Hadamard gives zero pointer-one effect when contact is deleted",
         "terminal_obligation": "matter-caused candidate pointer", "strength_vs_target": "weaker",
         "honesty_marker": "ATTEMPTED", "status": "POSITIVE_CANDIDATE_POINTER"},
        {"family": "fixed-menu positive-root instrument", "object_formulation": "binary qubit effect on a cubic-star pointer",
         "mechanism_invariant": "Cycle634 dilation realizes the echo effect", "terminal_obligation": "physical pointer effect",
         "strength_vs_target": "weaker", "honesty_marker": "ATTEMPTED", "status": "POSITIVE_EFFECT_ONLY"},
        {"family": "claimed-latch endpoint transducer", "object_formulation": "reversible Boolean certificate cell",
         "mechanism_invariant": "one claimed bit suppresses repeat emission", "terminal_obligation": "duplicate-safe oriented packet",
         "strength_vs_target": "weaker", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
        {"family": "one-use predecessor rotor packet", "object_formulation": "two adjacent interval cells plus one packet token",
         "mechanism_invariant": "token consumption, local head move, K16 recurrence", "terminal_obligation": "reversible interval cell",
         "strength_vs_target": "target-equivalent for packet layer", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
        {"family": "retained-state lineage decoder", "object_formulation": "predecessor graph and rotor/carry validation",
         "mechanism_invariant": "any missing or inconsistent edge returns undefined", "terminal_obligation": "additive interval word",
         "strength_vs_target": "target-equivalent for decoder", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
        {"family": "immutable Cycle610 semantic adapter", "object_formulation": "L3/L6/L7 local packet chains",
         "mechanism_invariant": "9+12=21 and two K16 carries without ordinal decoder input", "terminal_obligation": "acceptance-row equality",
         "strength_vs_target": "weaker than full tick composition", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
    ]
    open_routes = [
        {"family": "seam-complete same-species A2 detector composition", "object_formulation": "physical wedge2 stream plus CT-1 detector",
         "mechanism_invariant": "future Cycle639 successor stream host and local crossing extractor", "terminal_obligation": "unchanged Cycle610-612 end-to-end physical harness",
         "strength_vs_target": "target-equivalent", "status": "OPEN_UNTESTED_NOT_FAILURE"},
    ]
    walls = {
        "W_stream": "committed seam-complete physical same-species A2 stream host",
        "W_crossing": "physical CT-1 crossing/channel/convention certificate generator over that stream",
        "W_actuality": "actuality/admissibility/law-domain values rather than explicit supplied ports",
        "W_genesis": "autonomous blank bank, root-head, identity, schedule, and renewal genesis",
    }
    pairs = []
    for source in walls:
        for target in walls:
            if source != target:
                pairs.append({"from": source, "to": target, "closure_implied": False,
                              "reason": "the source object does not construct the target typed interface"})

    c610_note = "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md"
    c612_note = "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md"
    c632_note = "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_SECTOR_HELD_L6_LITERAL_EG_PRODUCT_TOURNAMENT_CYCLE632_NOTE_2026-07-23.md"
    c634_note = "docs/work_history/repo/review_feedback/PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md"
    c639_note = "docs/work_history/repo/review_feedback/PHYSICAL_SAME_SPECIES_TWO_CARRIER_PATH_SIGN_COMPILER_CYCLE639_NOTE_2026-07-23.md"
    current = "scripts/physical_m2_endpoint_interval_packet_interface_cycle640_2026_07_23.py"
    echo_line = repo_line(current, "def contact_echo_instrument()")
    endpoint_line = repo_line(current, "def endpoint_predicate_tournament()")
    packet_line = repo_line(current, "def packet_unit_tournament()")
    adapter_line = repo_line(current, "def chain_and_cycle610_adapter()")
    residual_rows = [
        {"prior_ref": PR5557_HEAD, "prior_path": c610_note,
         "prior_line": git_line(PR5557_HEAD, c610_note, "`9 + 12 = 21`"),
         "prior_residual": {"d_ab": 9, "d_bc": 12, "d_ac": 21, "carries": 2},
         "current_path": current, "current_line": adapter_line, "current_residual": {"d_ab": 9, "d_bc": 12, "d_ac": 21, "carries": 2},
         "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": PR5557_HEAD, "prior_path": c610_note,
         "prior_line": git_line(PR5557_HEAD, c610_note, "returns undefined (never zero)"),
         "prior_residual": "lineage gap -> undefined", "current_path": current, "current_line": adapter_line,
         "current_residual": "lineage gap -> undefined", "same_scope": True,
         "exact_match": True, "use_as_closure": True},
        {"prior_ref": PR5557_HEAD, "prior_path": c610_note,
         "prior_line": git_line(PR5557_HEAD, c610_note, "refuses duplicates"),
         "prior_residual": "duplicate refused", "current_path": current, "current_line": endpoint_line,
         "current_residual": "consumed one-use packet produces no second cell", "same_scope": True,
         "exact_match": True, "use_as_closure": True},
        {"prior_ref": PR5557_HEAD, "prior_path": c612_note,
         "prior_line": git_line(PR5557_HEAD, c612_note, "deletion kills it"),
         "prior_residual": 0.0, "current_path": current, "current_line": echo_line,
         "current_residual": echo["contact_off_pointer_one_effect_residual"], "same_scope": True,
         "exact_match": echo["contact_off_pointer_one_effect_residual"] < TOL, "use_as_closure": True},
        {"prior_ref": PR5557_HEAD, "prior_path": c612_note,
         "prior_line": git_line(PR5557_HEAD, c612_note, "binder deletion blocks"),
         "prior_residual": "no opportunity", "current_path": current, "current_line": packet_line,
         "current_residual": "blank target and unspent token", "same_scope": True,
         "exact_match": packet["binder_deletion_blocks_opportunity"], "use_as_closure": True},
        {"prior_ref": PR5557_HEAD, "prior_path": c612_note,
         "prior_line": git_line(PR5557_HEAD, c612_note, "actuality, admissibility, and law-domain"),
         "prior_residual": "three explicit ports", "current_path": current, "current_line": packet_line,
         "current_residual": "three explicit retained control M2", "same_scope": True,
         "exact_match": all(row["admission_refused"] for row in packet["explicit_port_deletions"]),
         "use_as_closure": True},
        {"prior_ref": COMMITTED_SHORE_HEAD, "prior_path": c632_note,
         "prior_line": git_line(COMMITTED_SHORE_HEAD, c632_note, "exact symbolic residual zero"),
         "prior_residual": "fixed-sector factorwise EG zero", "current_path": current, "current_line": repo_line(current, "def immutable_shores()"),
         "current_residual": "comparison-only physical update host; same-species A2 not back-credited",
         "same_scope": False, "exact_match": False, "use_as_closure": False,
         "disposition": "dropped as full Cycle610 A2 stream evidence"},
        {"prior_ref": COMMITTED_SHORE_HEAD, "prior_path": c634_note,
         "prior_line": git_line(COMMITTED_SHORE_HEAD, c634_note, "basis states are not Records"),
         "prior_residual": "pointer is candidate only", "current_path": current, "current_line": echo_line,
         "current_residual": "contact echo pointer is candidate only", "same_scope": True,
         "exact_match": True, "use_as_closure": True},
    ]

    def rhetoric(phrase: str, **values: str) -> dict[str, str]:
        return {"phrase": phrase,
                "per_element": values.get("per_element", "UNTESTED_NO_BROADER_NEGATIVE"),
                "per_site": values.get("per_site", "UNTESTED_NO_BROADER_NEGATIVE"),
                "per_mode": values.get("per_mode", "UNTESTED_NO_BROADER_NEGATIVE"),
                "per_block": values.get("per_block", "UNTESTED_NO_BROADER_NEGATIVE"),
                "lattice_wide": values.get("lattice_wide", "UNTESTED_NO_BROADER_NEGATIVE")}

    rhetoric_rows = [
        rhetoric("a coherent contact pointer is not an occurrence", per_site="two-M2 echo", per_block="endpoint truth table"),
        rhetoric("a packet count is not time", per_element="one K16 increment", per_block="9+12=21 packet chain", lattice_wide="withheld"),
        rhetoric("a pointer or packet cell is not a Record", per_site="retained reversible cell", per_block="inverse-visible chain"),
        rhetoric("Cycle632 fixed-sector EG is not the same-species A2 stream", per_block="scope mismatch exact", lattice_wide="withheld"),
        rhetoric("all24/all576 is not Lorentz covariance", per_site="ray labels", per_block="finite packet family", lattice_wide="withheld"),
        rhetoric("undefined on a tested lineage gap is not an unbounded causal theorem", per_block="L3/L6/L7 chains", lattice_wide="withheld"),
    ]
    partial = [
        {"file": current, "status": "EXECUTED_CONTACT_ECHO", "what_closes": "contact-caused coherent candidate pointer"},
        {"file": current, "status": "EXECUTED_ENDPOINT_TRANSDUCER", "what_closes": "duplicate-safe oriented channel/convention packet"},
        {"file": current, "status": "EXECUTED_INTERVAL_PACKET", "what_closes": "reversible exactly-once predecessor/rotor/carry update"},
        {"file": current, "status": "EXECUTED_LINEAGE_DECODER", "what_closes": "finite additive and undefined-gap semantics"},
        {"file": c632_note, "status": "COMMITTED_FIXED_SECTOR_COMPARISON_ONLY", "what_closes": "physical E/G grammar only, not A2 stream"},
        {"file": c634_note, "status": "COMMITTED_FIXED_MENU_APPARATUS", "what_closes": "binary candidate pointer effect only"},
    ]
    steelman = {
        "argument": "Once a Cycle639 successor lands a seam-complete same-species wedge2 stream, compile the Cycle610 two-channel detector and phase-crossing comparator into bounded pointer M2s, drive Cycle640's already exact channel/convention endpoint port, and rerun the immutable 610-612 harness. This is a concrete unclosed construction, so the present stream/tick gap is implementation evidence, not an obstruction.",
        "mechanism": "seam-complete local A2 E/G plus a reversible crossing comparator feeding the existing endpoint circuit",
        "terminal_obligation": "unchanged Cycle610-612 end-to-end physical composition with contact deletion, held L7, and returned work",
        "supporting_authorities": [
            {"ref": PR5557_HEAD, "path": c612_note,
             "line": git_line(PR5557_HEAD, c612_note, "Interface contract for the physical-M2 side")},
            {"ref": COMMITTED_SHORE_HEAD, "path": c634_note,
             "line": git_line(COMMITTED_SHORE_HEAD, c634_note, "positive bounded fixed-menu M2 instrument compiler")},
        ],
    }
    echoes = [
        {"cycle": 610, "retired": "candidate interval semantics", "mechanism": "EventChain K16/predecessor grammar", "applicability": "exact packet acceptance target", "citation_ref": PR5557_HEAD, "citation_path": c610_note, "citation_line": git_line(PR5557_HEAD, c610_note, "Route B — event-chain relational interval")},
        {"cycle": 611, "retired": "plus-channel diagnosis only", "mechanism": "preparation/certification separation", "applicability": "channel sign remains explicit", "citation_ref": PR5557_HEAD, "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md", "citation_line": 18},
        {"cycle": 612, "retired": "physical-M2 interface acceptance contract", "mechanism": "typed endpoint/interval/admission clauses", "applicability": "direct", "citation_ref": PR5557_HEAD, "citation_path": c612_note, "citation_line": git_line(PR5557_HEAD, c612_note, "Interface contract for the physical-M2 side")},
        {"cycle": 632, "retired": "fixed-sector physical E/G only", "mechanism": "factorwise routed product", "applicability": "grammar comparator; A2 scope mismatch", "citation_ref": COMMITTED_SHORE_HEAD, "citation_path": c632_note, "citation_line": 9},
        {"cycle": 634, "retired": "fixed-menu physical candidate pointer", "mechanism": "positive-root binary dilation", "applicability": "contact echo effect comparator", "citation_ref": COMMITTED_SHORE_HEAD, "citation_path": c634_note, "citation_line": 11},
        {"cycle": 639, "retired": "committed local onsite A2 payload only", "mechanism": "64x15 local wedge2 E", "applicability": "not consumed; seam stream still open", "citation_ref": CYCLE639_COMMITTED_HEAD, "citation_path": c639_note, "citation_line": git_line(CYCLE639_COMMITTED_HEAD, c639_note, "First, a positive local theorem")},
    ]
    passed = (
        len(families) == 6 and all(row["honesty_marker"] == "ATTEMPTED" for row in families)
        and len(open_routes) == 1 and all("honesty_marker" not in row for row in open_routes)
        and len(pairs) == 12 and len(residual_rows) == 8
        and all(all(key in row for key in ("prior_ref", "prior_path", "prior_line", "prior_residual", "current_path", "current_line", "current_residual", "same_scope", "exact_match", "use_as_closure")) for row in residual_rows)
        and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in rhetoric_rows)
        and len(partial) == 6 and all(all(key in row for key in ("file", "status", "what_closes")) for row in partial)
        and len(echoes) == 6 and all(row["citation_ref"] and row["citation_path"] and row["citation_line"] for row in echoes)
        and shores["pass"] and echo["pass"] and endpoint["pass"]
        and packet["pass"] and adapter["pass"]
    )
    result = {
        "N1_normalized_families": families,
        "N1_open_routes_not_counted": open_routes,
        "N1_qualifying_attempts": 6,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "WITHHELD_BECAUSE_TARGET_EQUIVALENT_STREAM_ROUTE_IS_OPEN",
        "N2_collapsed_walls": walls,
        "N2_directed_pairs": pairs,
        "N2_directed_pair_count": len(pairs),
        "N3_hidden_wall_scan": [
            "contact eigenflag, crossing bit, channel/convention certification and labels are supplied",
            "actuality, admissibility, law-domain, binder, identity, blank bank, root head, and schedule are supplied",
            "Cycle632 is fixed-sector comparison only; no same-species A2 back-credit",
            "Cycle634 pointer is coherent candidate only; no occurrence or Record back-credit",
            "Cycle639 local A2 hosting is committed but not consumed; the unlanded positive +0.30 line is not used",
            "finite L3/L6/L7 and six-bit identity domain only; no infinite or renewal claim",
        ],
        "N4_residual_matching": residual_rows,
        "N4_exact_matches": [row for row in residual_rows if row["same_scope"]],
        "N4_exact_residual_matches": [row for row in residual_rows if row["same_scope"]],
        "N4_dropped_nonmatches": [row for row in residual_rows if not row["same_scope"]],
        "N5_rhetoric_resolution_ledger": rhetoric_rows,
        "N6_partial_closure_paths": partial,
        "N7_hostile_steelman": steelman,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "Status": "PASS",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "axiom_pressure_claim": False,
        "pass": passed,
    }
    check("full current N1-N8 permits scoped packet results only and withholds shared/no-go/axiom claims",
          passed, {"families": len(families), "attempted": 6,
                   "walls": len(walls), "pairs": len(pairs)})
    return result


def inventory() -> dict[str, object]:
    return {
        "supplied": [
            f"immutable PR5557 Cycle610-612 contracts at {PR5557_HEAD}",
            f"committed Cycle632/634 shores at {COMMITTED_SHORE_HEAD}",
            "one local contact eigenflag and its contact phase",
            "crossing bit, crossing orientation, channel sign, channel certificate, T1/T2 convention, convention certificate",
            "six-bit candidate identity and one claimed latch per crossing cell",
            "one-use packet token, root cell rotor K14/head, blank target-cell bank, nearest-neighbor bank direction, serialized local schedule",
            "binder, actuality, admissibility, and law-domain port values",
        ],
        "derived": [
            "two-M2 coherent contact echo and exact contact-off kill",
            "bounded-support-three reversible endpoint predicate with duplicate refusal and copied orientation/channel/convention",
            "bounded-support-three reversible predecessor/K16/carry packet with token consumption and local head move",
            "L3/L6/L7 9+12=21/two-carry acceptance equality, inverse/deletion/malformed, undefined-gap, all24/all576 controls",
        ],
        "open": [
            "committed seam-complete physical same-species A2 stream and local extraction of the contact eigenflag",
            "physical CT-1 crossing/channel/convention certificate generator over that stream",
            "actuality/admissibility/law-domain value law and occurrence",
            "autonomous identity, bank, root-head, schedule, reset, renewal, and permanence",
            "unbounded causal order, empirical duration unit, continuum/Lorentz/proper-time interpretation",
        ],
    }


def note_text(receipt: dict[str, object]) -> str:
    echo = receipt["contact_echo_instrument"]
    endpoint = receipt["endpoint_predicate"]
    packet = receipt["interval_packet_unit"]
    adapter = receipt["cycle610_semantic_adapter"]
    covariance = receipt["covariance_controls"]
    external = receipt["unchanged_harness_external_run"]
    rows = "\n".join(
        f"| L{row['length']} | {row['split']} | {row['events']} | "
        f"{row['intervals']['d_ab']} | {row['intervals']['d_bc']} | "
        f"{row['intervals']['d_ac']} | {row['carries_first_24']} | yes |"
        for row in adapter["rows"]
    )
    deletion_rows = "\n".join(
        f"| `{row['deleted_gate']}` | {row['output_hamming']} | {row['full_inverse_visible_hamming']} |"
        for row in packet["deletion_rows"]
    )
    return f"""# Physical-M2 endpoint / interval packet interface — Cycle 640

Classification: **positive bounded physical candidate-packet interface; full same-species A2 stream/tick composition and actuality remain conditional/open**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough bar met: **false**

## Result up front

Cycle 640 constructs the physical-M2-side interface requested verbatim by the
immutable Cycle610-612 acceptance contract from PR #5557.

First, a two-path contact echo uses one local contact-eigenflag M2 and one
pointer M2.  `H`, controlled contact phase, `H` induces pointer-one effect
`diag(0,sin^2(g/2))`.  At `g={CONTACT_PHASE}` its contact-flag-one weight is
`{echo['pointer_one_probability_on_contact_flag_one']:.15f}`.  Deleting contact
sets the complete pointer-one effect to zero with residual
`{echo['contact_off_pointer_one_effect_residual']:.3e}`.  The induced effect
matches the Cycle634 positive-root binary instrument at residual
`{echo['Cycle634_positive_root_binary_effect_residual']:.3e}`.  This pointer is
a coherent candidate sector, not an occurrence.  Contact deletion kills only
this candidate pointer; it does not establish an actual endpoint.

Second, a reversible endpoint transducer computes

```text
contact_pointer AND crossing AND channel_certified
AND convention_certified AND NOT claimed.
```

It exhausts all `{endpoint['truth_table_rows']}` basis inputs with zero failures,
returns all `{endpoint['resources']['endpoint_work_M2']}` work M2 blank, latches
the crossing as claimed, and refuses a second certificate from the same
crossing cell.  Every certificate carries three explicit ports: crossing
orientation, channel sign (`plus/minus`), and convention (`T1/T2`).  The logic
is line-agnostic: no spectral root is hardwired, so a future lawful two-line
domain changes the port values/certificates rather than this hardware.

Third, a local reversible packet consumes one one-use endpoint token only when
the adjacent source cell carries the head and all four controls are one:
`binder`, `actuality`, `admissibility`, and `law_domain`.  It copies the packet
identity, copies predecessor identity from the local head cell, increments the
four-bit rotor once, writes carry exactly on `K15 -> K0`, copies the three
endpoint ports, consumes the token, and moves the head to the new cell.  All
runtime gates have support at most three M2.  The target blank-cell code is a
set of `{len(packet['target_blank_local_input_constraints'])}` local support-one
constraints; blank genesis is supplied.

| size | role | admitted cells | Delta(A,B) | Delta(B,C) | Delta(A,C) | carries/first24 | gaps undefined |
|---|---|---:|---:|---:|---:|---:|---:|
{rows}

This exactly reproduces Cycle610's `9 + 12 = 21` and two-carry acceptance row
at construction L3, train L6, and held-out L7 without refit.  Reverse endpoint
order returns `-9`.  Missing predecessor, deleted binder, wrong rotor, or
deleted carry returns **undefined**, never zero.  The decoder reads retained
cell state only; no update ordinal enters it.

## Deletion, inverse, malformed, and exactly-once controls

The interval unit exhausts `{packet['basis_cases_exhausted']}` declared basis
cases with `{packet['basis_case_failures']}` failures, including every rotor and
every combination of the four admission ports.  Applying the reverse gate list
restores the source, packet, ports, head, and blank target exactly.  After a
successful append the packet token is zero, so presenting it to another fresh
target appends nothing.

| deleted gate | output Hamming signal | signal after full inverse |
|---|---:|---:|
{deletion_rows}

Deleting binder, actuality, admissibility, or law-domain blocks admission.
Every single dirty target-cell M2 is refused by the declared local blank code.
The endpoint runner separately deletes contact, endpoint conjunction,
certificate, metadata, token, uncompute, and claimed-latch gates; every
deletion is output- and inverse-visible.

## Proper-cubic and resource controls

All `{covariance['proper_cubic_frames']}` proper-cubic frames and
`{covariance['ordered_frame_products']}` ordered products pass at L3/L6/L7.
The spatial apparatus ray is transported.  Crossing orientation, channel sign,
and T1/T2 convention are spatial scalars.  There is no runtime frame selector.
The reference ray and local bank direction are supplied.

The endpoint neighborhood uses `{endpoint['resources']['total_distinct_local_M2']}`
M2 including the contact eigenflag, echo/certificate ports, and work.  One
retained interval cell uses `{packet['resources']['cell_M2']}` M2; the complete
two-cell update neighborhood including packet, four explicit ports, and work
uses `{packet['resources']['two_cell_packet_and_work_neighborhood_M2']}` M2.
These are constants on the declared six-bit-identity domain.  The schedule is
a supplied compiler serialization, not a physical time law or autonomous bank
genesis.

## Exact shore and composition boundary

Cycle632 supplies an exact fixed-sector physical E/G grammar but explicitly
does not compile same-species multiparticle A2.  Cycle634 supplies the bounded
candidate-pointer instrument but explicitly supplies no occurrence or Record.
Cycle639's committed local `64 x 15` wedge2/A2 host is not
consumed as a premise here; its seam-complete stream remains open.  The
unlanded finite-L9 positive A2 line near `+0.30` is not used.

Therefore Cycle640 composes exactly with the Cycle610 **packet semantics** but
does not claim the full Cycle610 detector word has been run over a committed
physical same-species A2 stream.

## Unchanged Cycle610-612 harness rerun

The four PR #5557 source runners were executed unchanged in an isolated
detached worktree at `{external['execution_ref']}`.  They reproduced their
preregistered dispositions exactly: Cycle610 `{external['Cycle610']['pass_count']}`
PASS / `{external['Cycle610']['fail_count']}` FAIL (exit 1), Cycle611
`{external['Cycle611']['pass_count']}` / `{external['Cycle611']['fail_count']}`
(exit 1), Cycle612 main `{external['Cycle612_main']['pass_count']}` /
`{external['Cycle612_main']['fail_count']}` (exit 1), and the Cycle612 minus
addendum `{external['Cycle612_minus_addendum']['pass_count']}` /
`{external['Cycle612_minus_addendum']['fail_count']}` (exit 0).  Those expected
FAIL rows remain FAIL; none is repaired or reclassified.  This is a contract
reproduction, not an end-to-end composition with the Cycle640 packet.

## Supplied / derived / open

Supplied: immutable shores; local contact eigenflag and phase; crossing,
orientation, channel/sign/certification, T1/T2/certification; six-bit identity;
claimed latch; one-use token; root `K14` head; blank bank; local bank direction
and serialized schedule; binder, actuality, admissibility, and law-domain.

Derived: exact two-M2 contact echo and contact-off kill; reversible bounded
endpoint predicate; reversible exactly-once predecessor/K16/carry packet;
local head movement; explicit-port refusal; inverse/deletion/malformed and
undefined-gap controls; exact Cycle610 interval-row equality; all24/all576.

Open: committed seam-complete physical same-species A2 stream; physical CT-1
crossing/channel/convention certificates; laws supplying actuality,
admissibility, and law-domain; autonomous identity/bank/head/schedule/reset and
renewal; permanence, empirical duration unit, unbounded causal order,
continuum/Lorentz/proper-time interpretation.

## N1-N8 no-go discipline

N1 normalizes six attempted families and lists the target-equivalent
seam-complete A2 detector composition separately as open and not counted as a
failure.  N2 retains four directional walls and all 12 directed pairs.  N3
lists every flag, seed, selector, schedule, bank, port, and scope boundary.  N4
has seven exact same-scope rows and one dropped Cycle632 scope mismatch.  N5
has six complete five-resolution rows.  N6 has six structured partial-closure
paths.  N7 gives the actionable Cycle639-stream plus physical crossing-comparator
steelman.  N8 has six row-wise echoes.  Status: **PASS** for scoped discipline.

Broad no-go: **withheld**.  Shared route-independent obstruction: **not
established**.  Minimum content: **not claimed**.  Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle640 movement | residual |
|---|---|---|
| `C_ref` | one-use endpoint identity, predecessor, and local head provenance are retained | identity/root/bank/reference-ray genesis and renewal supplied |
| `C_num` | exact K16 carry, `9+12=21`, inverse/deletion/malformed/held rows | packet counts are not time; they have no empirical unit |
| `C_wrap` | rotor/carry and lineage gaps are locally explicit | cells are reversible candidates, not Records or histories; permanence absent |
| `C_int` | contact echo makes candidate pointer matter-caused and deletion kills exactly | committed seam-complete A2 stream and physical CT-1 crossing detector open |
| `C_local` | bounded support <=3, constant packet neighborhood, all24/all576 | schedule/bank/head genesis and infinite deployment open |
| `C_source` | pointer/work/bank/port resources are fully counted | actuality/admissibility/law-domain and resource renewal supplied; no gravity/source meaning |

## Disposition

**PASS** for the bounded coherent contact candidate, duplicate-safe endpoint,
reversible exactly-once predecessor/interval packet, explicit admission ports,
and exact Cycle610 packet-semantic adapter.

**DO NOT CLAIM** a realized event, Record, history, time/rate/proper-time law,
full physical Cycle610 clock, seam-complete same-species A2 E/G, autonomous
bank/schedule/renewal, shared obstruction, minimum content, or axiom pressure.

Strongest honest terminal: a literal bounded physical-M2 candidate-packet
interface satisfying the Cycle612 endpoint/interval clauses, ready to accept a
future certified CT-1 crossing bit without hardware redesign.
"""


def normalized_note(path: Path) -> str:
    return " ".join(path.read_text().lower().split())


def note_contract() -> dict[str, object]:
    body = normalized_note(NOTE)
    required = (
        "authority: **none**", "audit: **unset**",
        "author artifact status accepted: **false**",
        "breakthrough bar met: **false**",
        "counts are not time", "not an occurrence", "not records or histories",
        "actuality", "admissibility", "law-domain", "t1/t2", "channel sign",
        "contact deletion", "undefined", "all24/all576",
        "shared route-independent obstruction: **not established**",
        "axiom pressure: **none**",
    )
    missing = [fragment for fragment in required if fragment not in body]
    return {"required_fragments": required, "missing": missing, "pass": not missing}


def main() -> None:
    signal.alarm(math.ceil(WALL_CAP_SECONDS))
    started = time.perf_counter()
    shores = immutable_shores()
    echo = contact_echo_instrument()
    endpoint = endpoint_predicate_tournament()
    packet = packet_unit_tournament()
    adapter = chain_and_cycle610_adapter()
    covariance = covariance_controls(endpoint, packet)
    no_go = no_go_discipline(shores, echo, endpoint, packet, adapter)
    receipt: dict[str, object] = {
        "status": "positive bounded physical-M2 candidate endpoint/interval packet; full A2 stream/tick and actuality open",
        "classification": "positive bounded support-three physical candidate-packet interface; seam-complete A2 stream, elementary support-two lowering, tick law, and actuality remain open",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "breakthrough": False,
        "breakthrough_bar_met": False,
        "immutable_shores": shores,
        "contact_echo_instrument": echo,
        "endpoint_predicate": endpoint,
        "interval_packet_unit": packet,
        "cycle610_semantic_adapter": adapter,
        "covariance_controls": covariance,
        "no_go_discipline": no_go,
        "inventory": inventory(),
        "route_disposition": {
            "contact_echo": "PASS_COHERENT_CANDIDATE_CONTACT_OFF_KILL",
            "endpoint_predicate": "PASS_DUPLICATE_SAFE_ORIENTED_CHANNEL_CONVENTION_EXPLICIT",
            "interval_packet": "PASS_REVERSIBLE_EXACTLY_ONCE_K16_LOCAL_HEAD",
            "Cycle610_packet_semantics": "PASS_EXACT_9_PLUS_12_EQUALS_21",
            "full_Cycle610_physical_tick_composition": "OPEN_CONDITIONAL_ON_COMMITTED_A2_STREAM_AND_CROSSING_DETECTOR",
            "actual_occurrence_Record_history": "OPEN_EXPLICIT_PORTS_ONLY",
        },
        "route_by_route_disposition": {
            "contact_echo": "PASS_COHERENT_CANDIDATE_CONTACT_OFF_KILL",
            "endpoint_predicate": "PASS_DUPLICATE_SAFE_ORIENTED_CHANNEL_CONVENTION_EXPLICIT",
            "interval_packet": "PASS_REVERSIBLE_EXACTLY_ONCE_K16_LOCAL_HEAD",
            "Cycle610_packet_semantics": "PASS_EXACT_9_PLUS_12_EQUALS_21",
            "full_Cycle610_physical_tick_composition": "OPEN_CONDITIONAL_ON_SEAM_COMPLETE_A2_STREAM_AND_CROSSING_DETECTOR",
            "actual_occurrence_Record_history": "OPEN_EXPLICIT_PORTS_ONLY",
        },
        "strongest_constructive_result": "a bounded support-three reversible physical-M2 candidate endpoint and predecessor/K16 interval packet with exact contact-off kill, duplicate refusal, explicit channel/T1-T2 and actuality/admissibility/law-domain ports, L3/L6/L7 and all24/all576 controls",
        "highest_honest_terminal": "Cycle612 physical-side candidate packet interface, not a full physical CT-1 clock and not time/occurrence/Record/history",
        "six_wall_ledger": {
            "C_ref": "one-use identity/predecessor/head provenance; root/bank/reference genesis supplied",
            "C_num": "exact K16 and 9+12=21; count has no empirical unit and is not time",
            "C_wrap": "rotor/carry/gap explicit; reversible cells not Records/histories",
            "C_int": "contact echo candidate with exact deletion kill; seam-complete A2 stream/crossing detector open",
            "C_local": "support<=3, constant neighborhood, all24/all576; serialized schedule and infinite deployment open",
            "C_source": "all pointer/work/bank/ports counted; port values and renewal supplied, no gravity/source meaning",
        },
        "shared_substrate_obstruction": False,
        "shared_route_independent_obstruction": False,
        "minimum_content_claim": False,
        "axiom_pressure": False,
        "full_Cycle610_612_harness_composition": False,
        "unchanged_harness_external_run": UNCHANGED_HARNESS_EXTERNAL_RUN,
        "optimal_next_campaign": "after a Cycle639 successor lands a seam-complete same-species A2 stream, compile the CT-1 two-channel crossing/channel/convention certificate into bounded M2s and feed this unchanged packet interface through the immutable Cycle610-612 harness",
    }
    NOTE.write_text(note_text(receipt))
    contract = note_contract()
    check("Cycle640 note preserves packet/time/occurrence/Record and no-go firewalls",
          contract["pass"], contract["missing"])
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000:
        rss *= 1024
    receipt.update({
        "note_contract": contract,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
    })
    receipt["pass"] = (
        FAIL == 0 and shores["pass"] and echo["pass"] and endpoint["pass"]
        and packet["pass"] and adapter["pass"] and covariance["pass"]
        and no_go["pass"] and contract["pass"]
        and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
        and AUTHORITY == "none" and AUDIT == "unset"
    )
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS,
                      "tests_failed": FAIL, "elapsed_seconds": elapsed,
                      "maximum_RSS_bytes": rss, "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
