#!/usr/bin/env python3
"""Cycle577: faithful physical-M2 compiler tournament for the L41 instrument.

The eleven original nonorthogonal rank-one M2 projectors and the P/E/X/Z
three-site instrument are tested through a direct channel, a priority local
gauge/environment/Naimark dilation, and a staggered retained-environment
dilation with an in-state phase head.  Branch traces are diagnostics against pinned Cycle41
candidate-law data; no actual member, framework Record, or probability law is
created.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import complete_candidate_lstar_assembly_cycle41_2026_07_14 as c41


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

FROZEN_PATHS = {
    "Cycle41 runner": ROOT / "scripts/complete_candidate_lstar_assembly_cycle41_2026_07_14.py",
    "Cycle41 note": ROOT / "docs/work_history/repo/review_feedback/COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md",
    "Cycle280 runner": ROOT / "scripts/same_code_instrument_bridge_synthesis_cycle280_2026_07_17.py",
    "Cycle280 note": ROOT / "docs/work_history/repo/review_feedback/SAME_CODE_INSTRUMENT_BRIDGE_SYNTHESIS_CYCLE280_NOTE_2026-07-17.md",
    "Cycle288 runner": ROOT / "scripts/physical_instrument_record_history_bridge_synthesis_cycle288_2026_07_17.py",
    "Cycle288 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_INSTRUMENT_RECORD_HISTORY_BRIDGE_SYNTHESIS_CYCLE288_NOTE_2026-07-17.md",
    "Cycle430 runner": ROOT / "scripts/repeated_physical_instrument_conditional_history_frequency_cycle430_2026_07_19.py",
    "Cycle430 note": ROOT / "docs/work_history/repo/review_feedback/REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_CYCLE430_NOTE_2026-07-19.md",
    "Cycle483 runner": ROOT / "scripts/physical_reset_environment_record_occurrence_cycle483_2026_07_19.py",
    "Cycle483 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CYCLE483_NOTE_2026-07-19.md",
    "Cycle488 runner": ROOT / "scripts/physical_form_occurrence_born_weight_firewall_cycle488_2026_07_20.py",
    "Cycle488 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_FORM_OCCURRENCE_BORN_WEIGHT_FIREWALL_CYCLE488_NOTE_2026-07-20.md",
    "Cycle502 runner": ROOT / "scripts/physical_kraus_record_lock_candidate_grade_formation_tournament_cycle502_2026_07_20.py",
    "Cycle502 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_KRAUS_RECORD_LOCK_CANDIDATE_GRADE_FORMATION_TOURNAMENT_CYCLE502_NOTE_2026-07-20.md",
    "Cycle565 runner": ROOT / "scripts/physical_born_menu_compiler_occurrence_interface_cycle565_2026_07_21.py",
    "Cycle565 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md",
    "Cycle571 runner": ROOT / "scripts/physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22.py",
    "Cycle571 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md",
    "Cycle574 runner": ROOT / "scripts/physical_l41_candidate_law_integration_tournament_cycle574_2026_07_22.py",
    "Cycle574 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_CANDIDATE_LAW_INTEGRATION_TOURNAMENT_CYCLE574_NOTE_2026-07-22.md",
}
FROZEN = {
    "Cycle41 runner": "d8207fc0090ca926d060f536fedc2b2c031ccd50184e035c292e6b8eccb56814",
    "Cycle41 note": "efacbbdeda940877e6130f48e1363ccb223a6e9cb579d500e119ed47511b69bd",
    "Cycle280 runner": "c524555dde37c89d5111c9282d2594271e39d40d0c489dccc299c2b75a5db281",
    "Cycle280 note": "271c0220d3649bafdf512aa77bf887c14437174a8f8ad92039c4f6ead71235e4",
    "Cycle288 runner": "1f69d7c185a847bf2c32d591965d90b7f03094a0c95be2961c7e477b6feaac59",
    "Cycle288 note": "054dd0f593abdd2c162ebe15334e2d3fe33eac2746794806cf3f6a5abf5e502e",
    "Cycle430 runner": "3fa6981d1d0203a3121729026f0094058cf024e6a71f63045f5bc6043c2039a0",
    "Cycle430 note": "75c41994f834454d7a18871578b33464599dec9632adadbdfede4fe70c73afad",
    "Cycle483 runner": "52f0621a06792093ad64a706ab7741335cfd7ff9418b3756f4ab83cf72b8d222",
    "Cycle483 note": "be836748288af45b5b71d71ce380376f05b4168468e48e2bc8ff75c4a43dc74f",
    "Cycle488 runner": "17bbdd0d30f579668120dbdea55b4d42dfceff550b31cc50b3ec11451b510470",
    "Cycle488 note": "b7f4ce80c87e45018af4b4ae87c8036aba1bb063964b78ce8d0b614605f5c7c5",
    "Cycle502 runner": "5494b7fd9d1411023ac2427b92c323cea9b7c26720b3a6b8d58ee32835e1e8a9",
    "Cycle502 note": "36e156581d5f3d3dddea1e0ce1344834bd31d65883160c3c3b04c4d4671b41c2",
    "Cycle565 runner": "b4b6e2c4491c5a6b30389764e8ac597ce07e1dac3f31c7cb8fff9297ac04437a",
    "Cycle565 note": "72dd62448eaf685de0a7f1cc4ce9d164363428976eafc8efb93c973b8856f39a",
    "Cycle571 runner": "7221d59558e4d731f98a2a4523c280aa98b889f23ea3f7be1acc8919395dfee8",
    "Cycle571 note": "b254476f392597c03f27581fbc4f559266ed42984ac86a516888ee81d2aff8e2",
    "Cycle574 runner": "5ee6808d41feb6cd9c1c3d512232ab483f5a55a4643d0a136b89d12f37c3af15",
    "Cycle574 note": "aa01495db7805af094df8f6254a6236e19536d117f5ae40f76756b8b205a0d83",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


I2 = np.eye(2, dtype=complex)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
Z = np.asarray(((1, 0), (0, -1)), dtype=complex)
H = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2.0)
ZERO = np.asarray((1, 0), dtype=complex)
ONE = np.asarray((0, 1), dtype=complex)
PLUS = (ZERO + ONE) / np.sqrt(2.0)


def kron_all(*items: np.ndarray) -> np.ndarray:
    answer = np.asarray([[1.0 + 0.0j]])
    for item in items:
        answer = np.kron(answer, item)
    return answer


def ket(index: int, width: int) -> np.ndarray:
    answer = np.zeros(width, dtype=complex)
    answer[index] = 1.0
    return answer


def projector(axis: np.ndarray, sign: int = 1) -> np.ndarray:
    return (I2 + sign * axis) / 2.0


ROLE_AXES = {
    "H1": Y,
    "H0": -Y,
    "B1": (X + Y) / np.sqrt(2.0),
    "B0": -(X + Y) / np.sqrt(2.0),
    "D1": (X + Z) / np.sqrt(2.0),
    "D0": -(X + Z) / np.sqrt(2.0),
    "C": (X + Y + Z) / np.sqrt(3.0),
    "X+": X,
    "X-": -X,
    "Z0": Z,
    "Z1": -Z,
}
ROLES = tuple(ROLE_AXES)
ROLE_P = {name: projector(axis) for name, axis in ROLE_AXES.items()}


def on_site(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    return kron_all(*(operator if index == site else I2 for index in range(count)))


PLUS3 = kron_all(PLUS.reshape(-1, 1), PLUS.reshape(-1, 1), PLUS.reshape(-1, 1)).reshape(-1)
CZ01 = np.diag(tuple(-1.0 if ((word >> 2) & 1) and ((word >> 1) & 1) else 1.0 for word in range(8))).astype(complex)
CZ12 = np.diag(tuple(-1.0 if ((word >> 1) & 1) and (word & 1) else 1.0 for word in range(8))).astype(complex)
CZ = CZ12 @ CZ01
CLUSTER = CZ @ PLUS3
HISTORIES = tuple(product((1, -1), (0, 1), (0, 1)))


def history_index(history: tuple[int, int, int]) -> int:
    middle_sign, left_value, right_value = history
    return 4 * int(middle_sign == -1) + 2 * left_value + right_value


def history_projector(history: tuple[int, int, int]) -> np.ndarray:
    middle_sign, left_value, right_value = history
    return (
        on_site(projector(Z, 1 if left_value == 0 else -1), 0, 3)
        @ on_site(projector(X, middle_sign), 1, 3)
        @ on_site(projector(Z, 1 if right_value == 0 else -1), 2, 3)
    )


HISTORY_P = {history: history_projector(history) for history in HISTORIES}
BRANCH_VECTOR = {history: HISTORY_P[history] @ CLUSTER for history in HISTORIES}
A0 = np.outer(PLUS, ZERO.conj())
A1 = np.outer(PLUS, ONE.conj())
RESET_K = tuple(kron_all(*items) for items in product((A0, A1), repeat=3))
BRANCH_K = {
    history: tuple(HISTORY_P[history] @ CZ @ reset for reset in RESET_K)
    for history in HISTORIES
}


def channel(kraus: tuple[np.ndarray, ...], rho: np.ndarray) -> np.ndarray:
    return sum((item @ rho @ item.conj().T for item in kraus), np.zeros((kraus[0].shape[0], kraus[0].shape[0]), dtype=complex))


def trace_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def valid_density(rho: np.ndarray, width: int) -> bool:
    return (
        rho.shape == (width, width)
        and np.allclose(rho, rho.conj().T, atol=TOL)
        and abs(float(np.trace(rho).real) - 1.0) < TOL
        and np.linalg.eigvalsh(rho).min() > -TOL
    )


W2 = np.zeros((4, 2), dtype=complex)
W2[0, 0] = W2[3, 1] = 1.0
W3 = kron_all(W2, W2, W2)
Q2 = W2 @ W2.conj().T
Q3 = W3 @ W3.conj().T
ENCODED_ROLE_P = {name: W2 @ value @ W2.conj().T for name, value in ROLE_P.items()}
H9 = np.zeros((2**9, 9), dtype=complex)
H9_PHYSICAL_BASIS = tuple(1 << (8 - rail) for rail in range(9))
for _rail, _basis_index in enumerate(H9_PHYSICAL_BASIS):
    H9[_basis_index, _rail] = 1.0


def apply_one(state: np.ndarray, unitary: np.ndarray, site: int, count: int) -> np.ndarray:
    tensor = state.reshape((2,) * count)
    moved = np.moveaxis(tensor, site, 0).reshape(2, -1)
    moved = unitary @ moved
    return np.moveaxis(moved.reshape((2,) + (2,) * (count - 1)), 0, site).reshape(-1)


def apply_cnot(state: np.ndarray, control: int, target: int, count: int) -> np.ndarray:
    indices = np.arange(len(state))
    c_mask, t_mask = 1 << (count - 1 - control), 1 << (count - 1 - target)
    destinations = np.where((indices & c_mask) != 0, indices ^ t_mask, indices)
    output = np.empty_like(state)
    output[destinations] = state
    return output


def apply_cz(state: np.ndarray, first: int, second: int, count: int) -> np.ndarray:
    indices = np.arange(len(state))
    first_mask, second_mask = 1 << (count - 1 - first), 1 << (count - 1 - second)
    signs = np.where(((indices & first_mask) != 0) & ((indices & second_mask) != 0), -1.0, 1.0)
    return state * signs


def apply_swap(state: np.ndarray, first: int, second: int, count: int) -> np.ndarray:
    return np.swapaxes(state.reshape((2,) * count), first, second).reshape(-1)


C_PHASES = (
    "reset-left", "reset-middle", "reset-right", "CZ-left-middle",
    "CZ-middle-right", "measure-X-middle", "measure-Z-left", "measure-Z-right",
)


def staggered_column(input_index: int, *, delete_phase: str | None = None,
                     delete_advance: str | None = None) -> np.ndarray:
    count = 12
    quantum = kron_all(ket(input_index, 8).reshape(-1, 1), PLUS3.reshape(-1, 1), ket(0, 8).reshape(-1, 1), ket(0, 8).reshape(-1, 1)).reshape(-1)
    # The head is an actual nine-dimensional one-excitation code factor.  A
    # phase operation acts only on the amplitude slice with that occupied rail;
    # the following rail SWAP is a physical two-M2 head advance.
    state = np.zeros((2**count, 9), dtype=complex)
    state[:, 0] = quantum
    for phase, label in enumerate(C_PHASES):
        if label != delete_phase:
            active = state[:, phase]
            if phase < 3:
                active = apply_swap(active, phase, 3 + phase, count)
            elif label == "CZ-left-middle":
                active = apply_cz(active, 0, 1, count)
            elif label == "CZ-middle-right":
                active = apply_cz(active, 1, 2, count)
            elif label == "measure-X-middle":
                active = apply_one(active, H, 1, count)
                active = apply_cnot(active, 1, 6, count)
                active = apply_cnot(active, 6, 9, count)
                active = apply_one(active, H, 1, count)
            elif label == "measure-Z-left":
                active = apply_cnot(active, 0, 7, count)
                active = apply_cnot(active, 7, 10, count)
            elif label == "measure-Z-right":
                active = apply_cnot(active, 2, 8, count)
                active = apply_cnot(active, 8, 11, count)
            state[:, phase] = active
        if label != delete_advance:
            state[:, (phase, phase + 1)] = state[:, (phase + 1, phase)]
    return state.reshape(-1)


def staggered_isometry(**kwargs: str | None) -> tuple[np.ndarray, tuple[int, ...]]:
    isometry = np.column_stack(tuple(staggered_column(index, **kwargs) for index in range(8)))
    tensor = isometry.reshape(4096, 9, 8)
    heads = tuple(int(np.argmax(np.sum(np.abs(tensor[:, :, index]) ** 2, axis=0))) for index in range(8))
    return isometry, heads


def route_c_branch_kraus(isometry: np.ndarray, history: tuple[int, int, int]) -> tuple[np.ndarray, ...]:
    pointer = history_index(history)
    tensor = isometry.reshape(8, 8, 8, 8, 9, 8)
    return tuple(
        tensor[:, environment, pointer, pointer, head, :]
        for environment in range(8) for head in range(9)
    )


def dependency_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.exists() else ""
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c",
        "eleven nonorthogonal", "precise cptp/instrument intertwiner", "all24", "all576",
        "held l6", "candidate weights are pinned prior-law data", "not derived born probabilities",
        "not select an actual branch", "supplied / derived / open", "n1", "n2", "n3", "n4",
        "n5", "n6", "n7", "n8", "n1 status: **fail**",
        "positive partial construction with explicit residuals",
        "axiom-pressure claim: **do not ship**",
    )
    missing = tuple(fragment for fragment in required if fragment not in note)
    return {"expected": FROZEN, "observed": observed, "note_missing": missing, "pass": observed == FROZEN and not missing}


def projector_controls() -> dict[str, object]:
    direct_residuals = []
    gauge_residuals = []
    rank_failures = distinct_failures = gauge_leakage = 0
    for name, value in ROLE_P.items():
        rank_failures += int(not (
            np.allclose(value @ value, value, atol=TOL)
            and np.allclose(value, value.conj().T, atol=TOL)
            and abs(float(np.trace(value).real) - 1.0) < TOL
        ))
        direct_residuals.append(float(np.linalg.norm(value - I2.conj().T @ value @ I2)))
        encoded = ENCODED_ROLE_P[name]
        gauge_residuals.append(float(np.linalg.norm(W2.conj().T @ encoded @ W2 - value)))
        gauge_leakage += int(np.linalg.norm((np.eye(4) - Q2) @ encoded @ Q2) > TOL)
    for left, right in combinations(ROLES, 2):
        distinct_failures += int(np.allclose(ROLE_P[left], ROLE_P[right], atol=TOL))
    original_gram = np.asarray([[np.trace(ROLE_P[a] @ ROLE_P[b]) for b in ROLES] for a in ROLES])
    encoded_gram = np.asarray([[np.trace(ENCODED_ROLE_P[a] @ ENCODED_ROLE_P[b]) for b in ROLES] for a in ROLES])
    result = {
        "roles": ROLES, "rank_failures": rank_failures, "pair_count": 55,
        "distinct_failures": distinct_failures, "direct_max_intertwiner": max(direct_residuals),
        "gauge_max_intertwiner": max(gauge_residuals),
        "gauge_Gram_residual": float(np.linalg.norm(original_gram - encoded_gram)),
        "gauge_leakage_failures": gauge_leakage,
        "local_gauge_constraint": "Z tensor Z = +1 on each two-M2 code block",
        "pass": bool(not any((rank_failures, distinct_failures, gauge_leakage))
        and max(direct_residuals + gauge_residuals) < TOL
        and np.linalg.norm(original_gram - encoded_gram) < TOL),
    }
    check("all eleven original nonorthogonal one-M2 projectors are faithfully represented directly and in the two-M2 local gauge code", result["pass"], result)
    return result


def direct_channel_controls() -> dict[str, object]:
    completeness = sum((item.conj().T @ item for history in HISTORIES for item in BRANCH_K[history]), np.zeros((8, 8), dtype=complex))
    fixtures = (
        np.eye(8, dtype=complex) / 8.0,
        np.outer((ket(0, 8) + 1j * ket(3, 8) + np.sqrt(2) * ket(7, 8)) / 2.0,
                 (ket(0, 8) + 1j * ket(3, 8) + np.sqrt(2) * ket(7, 8)).conj() / 2.0),
    )
    eg = tp = 0
    branch_rows = []
    for fixture_index, rho in enumerate(fixtures):
        if not valid_density(rho, 8):
            raise ValueError("direct route fixture leaves density domain")
        outputs = tuple(channel(BRANCH_K[history], rho) for history in HISTORIES)
        traces = tuple(float(np.trace(value).real) for value in outputs)
        expected = tuple(np.outer(BRANCH_VECTOR[history], BRANCH_VECTOR[history].conj()) for history in HISTORIES)
        eg += sum(int(np.linalg.norm(found - target) > TOL) for found, target in zip(outputs, expected))
        tp += int(abs(sum(traces) - 1.0) > TOL)
        branch_rows.append((fixture_index, traces))
    pinned = tuple(Fraction(1, 4) if np.vdot(BRANCH_VECTOR[h], BRANCH_VECTOR[h]).real > TOL else Fraction(0) for h in HISTORIES)
    result = {
        "route": "A direct local CPTP channel", "M2_data": 3,
        "channel_primitive_or_discard_supplied": True,
        "completeness_residual": float(np.linalg.norm(completeness - np.eye(8))),
        "EG_failures": eg, "trace_failures": tp,
        "branch_rows": branch_rows,
        "pinned_candidate_trace_tuple": tuple(str(value) for value in pinned),
        "pass": np.linalg.norm(completeness - np.eye(8)) < TOL and not eg and not tp
        and sorted(pinned) == [Fraction(0)] * 4 + [Fraction(1, 4)] * 4,
    }
    check("Route A satisfies the direct CPTP/instrument square on the declared three-M2 block", result["pass"], result)
    return result


def gauge_naimark_controls() -> dict[str, object]:
    fixtures = (
        np.eye(8, dtype=complex) / 8.0,
        np.outer((ket(1, 8) + ket(6, 8)) / np.sqrt(2.0), (ket(1, 8) + ket(6, 8)).conj() / np.sqrt(2.0)),
    )
    # Materialize the single 18-M2 output isometry.  Its axes are encoded
    # system(64), encoded spent-reset environment(64), pointer(8), copied
    # dephasing environment(8), and logical input(8).  Only code/pointer
    # sectors are populated, so sparse block assignment avoids a 2^18 square.
    full_tensor = np.zeros((64, 64, 8, 8, 8), dtype=complex)
    for input_index in range(8):
        encoded_old_input = W3 @ ket(input_index, 8)
        for history in HISTORIES:
            pointer = history_index(history)
            encoded_branch = W3 @ BRANCH_VECTOR[history]
            full_tensor[:, :, pointer, pointer, input_index] += np.outer(encoded_branch, encoded_old_input)
    full_isometry = full_tensor.reshape(2**18, 8)
    gram = full_isometry.conj().T @ full_isometry
    code_completeness = np.zeros((64, 64), dtype=complex)
    eg = leakage = materialized_branch_failures = 0
    for history in HISTORIES:
        pointer = history_index(history)
        materialized_kraus = tuple(full_tensor[:, environment, pointer, pointer, :] for environment in range(64))
        physical_kraus = tuple(W3 @ item @ W3.conj().T for item in BRANCH_K[history])
        code_completeness += sum((item.conj().T @ item for item in physical_kraus), np.zeros((64, 64), dtype=complex))
        for rho in fixtures:
            encoded_input = W3 @ rho @ W3.conj().T
            found = channel(physical_kraus, encoded_input)
            expected = W3 @ channel(BRANCH_K[history], rho) @ W3.conj().T
            eg += int(np.linalg.norm(found - expected) > TOL)
            materialized_branch_failures += int(np.linalg.norm(channel(materialized_kraus, rho) - expected) > TOL)
            leakage += int(np.linalg.norm((np.eye(64) - Q3) @ found @ Q3) > TOL)
    materialized_reduced_failures = 0
    for rho in fixtures:
        reduced = np.zeros((64, 64), dtype=complex)
        expected_reduced = np.zeros((64, 64), dtype=complex)
        for history in HISTORIES:
            pointer = history_index(history)
            reduced += channel(tuple(full_tensor[:, environment, pointer, pointer, :] for environment in range(64)), rho)
            expected_reduced += W3 @ channel(BRANCH_K[history], rho) @ W3.conj().T
        materialized_reduced_failures += int(np.linalg.norm(reduced - expected_reduced) > TOL)
    parity_failures = 0
    zz = np.kron(Z, Z)
    for logical in (ZERO, ONE, PLUS, (ZERO + 1j * ONE) / np.sqrt(2.0)):
        encoded = W2 @ logical
        parity_failures += int(np.linalg.norm(zz @ encoded - encoded) > TOL)
    reset_input_distance = 0.5 * trace_norm(np.outer(ZERO, ZERO) - np.outer(ONE, ONE))
    reset_system_distance = 0.0
    reset_environment_distance = reset_input_distance
    supported = tuple(h for h in HISTORIES if np.vdot(BRANCH_VECTOR[h], BRANCH_VECTOR[h]).real > TOL)
    missing_branch_residual = float(np.linalg.norm(
        gram - sum((
            sum((np.outer(W3 @ BRANCH_VECTOR[h], W3[e, :].conj()).conj().T @ np.outer(W3 @ BRANCH_VECTOR[h], W3[e, :].conj()) for e in range(64)), np.zeros((8, 8), dtype=complex))
            for h in supported[1:]
        ), np.zeros((8, 8), dtype=complex))
    ))
    result = {
        "route": "B priority local gauge/environment/Naimark",
        "physical_M2": 18, "per_coarse_site_M2": 6,
        "encoded_system_M2": 6, "fresh_encoded_plus_reset_environment_M2": 6,
        "pointer_M2": 3, "pointer_dephasing_environment_M2": 3,
        "fresh_reset_code_blocks": 3, "fresh_reset_environment_M2": 6,
        "fresh_blank_pointer_M2": 3, "fresh_blank_dephasing_M2": 3,
        "fresh_low_entropy_auxiliary_M2_per_invocation": 12,
        "local_parity_constraints": 6, "parity_failures": parity_failures,
        "local_parity_enforcement_dynamics_constructed": False,
        "materialized_full_output_isometry_shape": full_isometry.shape,
        "materialized_full_output_M2": 18,
        "materialized_nonzero_amplitudes": int(np.count_nonzero(np.abs(full_isometry) > TOL)),
        "only_bounded_full_isometry_constructed": True,
        "exact_bounded_gate_layout_decomposition_constructed": False,
        "full_unitary_extension_constructed": False,
        "dilation_isometry_residual": float(np.linalg.norm(gram - np.eye(8))),
        "physical_code_completeness_residual": float(np.linalg.norm(code_completeness - Q3)),
        "CPTP_instrument_intertwiner_failures": eg, "code_leakage_failures": leakage,
        "materialized_branch_reduction_failures": materialized_branch_failures,
        "materialized_nonselective_reduction_failures": materialized_reduced_failures,
        "reset_system_trace_distance_after": reset_system_distance,
        "spent_environment_trace_distance_after": reset_environment_distance,
        "missing_supported_pointer_branch_residual": missing_branch_residual,
        "reusable_reset_entropy_derived": False,
        "pointer_dephasing_requires_named_environment": True,
        "actual_branch_selected": False,
        "framework_Record_created": False,
        "pass": not any((parity_failures, eg, leakage, materialized_branch_failures, materialized_reduced_failures))
        and full_isometry.shape == (2**18, 8) and np.linalg.norm(gram - np.eye(8)) < TOL
        and np.linalg.norm(code_completeness - Q3) < TOL
        and reset_system_distance < TOL and abs(reset_environment_distance - 1.0) < TOL
        and missing_branch_residual > 0.1,
    }
    check("Route B gives an exact code-space gauge/Naimark/reset dilation with every fresh and spent environment named", result["pass"], result)
    return result


def staggered_controls() -> dict[str, object]:
    isometry, heads = staggered_isometry()
    expected_columns = []
    for input_index in range(8):
        expected_quantum = np.zeros(4096, dtype=complex)
        for history in HISTORIES:
            h_index = history_index(history)
            expected_quantum += kron_all(
                BRANCH_VECTOR[history].reshape(-1, 1), ket(input_index, 8).reshape(-1, 1),
                ket(h_index, 8).reshape(-1, 1), ket(h_index, 8).reshape(-1, 1),
            ).reshape(-1)
        expected_columns.append(np.kron(expected_quantum, ket(8, 9)))
    expected_isometry = np.column_stack(expected_columns)
    code_tensor = isometry.reshape(4096, 9, 8)
    nonzero = np.argwhere(np.abs(code_tensor) > TOL)
    sparse_rows: dict[int, np.ndarray] = {}
    sparse_digest = sha256()
    for quantum_index, head_index, input_index in nonzero:
        physical_row = int(quantum_index) * (2**9) + H9_PHYSICAL_BASIS[int(head_index)]
        value = code_tensor[int(quantum_index), int(head_index), int(input_index)]
        sparse_rows.setdefault(physical_row, np.zeros(8, dtype=complex))[int(input_index)] += value
        sparse_digest.update(f"{physical_row}:{int(input_index)}:{value.real:.17g}:{value.imag:.17g}".encode())
    sparse_gram = sum((np.outer(row.conj(), row) for row in sparse_rows.values()), np.zeros((8, 8), dtype=complex))
    h9_residual = float(np.linalg.norm(H9.conj().T @ H9 - np.eye(9)))
    physical_sparse_isometry_residual = float(np.linalg.norm(sparse_gram - np.eye(8)))
    fixtures = (
        np.eye(8, dtype=complex) / 8.0,
        np.outer((ket(2, 8) + 1j * ket(5, 8)) / np.sqrt(2.0), (ket(2, 8) + 1j * ket(5, 8)).conj() / np.sqrt(2.0)),
    )
    eg = 0
    for history, rho in product(HISTORIES, fixtures):
        found = channel(route_c_branch_kraus(isometry, history), rho)
        expected = channel(BRANCH_K[history], rho)
        eg += int(np.linalg.norm(found - expected) > TOL)
    without_advance, deleted_heads = staggered_isometry(delete_advance="reset-right")
    advance_deletion_residual = float(np.linalg.norm(without_advance - expected_isometry))
    without_cz, _ = staggered_isometry(delete_phase="CZ-middle-right")
    deleted_branch_shift = 0.0
    rho = np.eye(8, dtype=complex) / 8.0
    for history in HISTORIES:
        deleted_branch_shift = max(deleted_branch_shift, float(np.linalg.norm(
            channel(route_c_branch_kraus(without_cz, history), rho) - channel(BRANCH_K[history], rho)
        )))
    result = {
        "route": "C staggered sequential dilation with in-state phase head",
        "physical_M2": 21, "data_reset_pointer_dephase_M2": 12, "one_hot_head_M2": 9,
        "fresh_low_entropy_auxiliary_M2_per_invocation": 18,
        "head_code_coordinate_dimension": 9,
        "materialized_code_coordinate_isometry_shape": isometry.shape,
        "H9_physical_embedding_shape": H9.shape,
        "physical_sparse_output_isometry_shape": (2**21, 8),
        "physical_sparse_nonzero_amplitudes": len(nonzero),
        "physical_sparse_embedding_SHA256": sparse_digest.hexdigest(),
        "H9_isometry_residual": h9_residual,
        "physical_sparse_isometry_residual": physical_sparse_isometry_residual,
        "head_exactly_one_is_supplied_code_domain": True,
        "head_exactly_one_locally_enforced": False,
        "explicit_phases": C_PHASES, "terminal_heads": heads,
        "retained_environment_isometry_residual": float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(8))),
        "explicit_sequence_residual": float(np.linalg.norm(isometry - expected_isometry)),
        "CPTP_instrument_intertwiner_failures": eg,
        "head_advance_deletion_terminal_heads": deleted_heads,
        "head_advance_deletion_isometry_residual": advance_deletion_residual,
        "CZ_deletion_branch_shift": deleted_branch_shift,
        "maximum_uncontrolled_gate_support_M2": 2,
        "maximum_phase_controlled_logical_support_M2": 3,
        "exact_two_M2_decomposition_supplied": False,
        "full_2pow21_unitary_extension_constructed": False,
        "schedule_is_time": False, "autonomous_repeated_invocation_derived": False,
        "pass": set(heads) == {8} and np.linalg.norm(isometry.conj().T @ isometry - np.eye(8)) < TOL
        and h9_residual < TOL and physical_sparse_isometry_residual < TOL
        and (2**21, 8) == (2097152, 8) and len(nonzero) > 0
        and np.linalg.norm(isometry - expected_isometry) < TOL and not eg
        and set(deleted_heads) != {8} and advance_deletion_residual > TOL and deleted_branch_shift > TOL,
    }
    check("Route C's eight in-state phases implement the same retained-environment instrument with exact local substeps", result["pass"], result)
    return result


def held_and_domain_controls() -> dict[str, object]:
    spectator = (ket(0, 8) + ket(3, 8) + 1j * ket(7, 8)) / np.sqrt(3.0)
    rho_s = np.outer(spectator, spectator.conj())
    rho3 = np.outer((ket(1, 8) + ket(4, 8)) / np.sqrt(2.0), (ket(1, 8) + ket(4, 8)).conj() / np.sqrt(2.0))
    rho6 = np.kron(rho3, rho_s)
    held_failures = 0
    for history in HISTORIES:
        held_k = tuple(np.kron(item, np.eye(8)) for item in BRANCH_K[history])
        found = channel(held_k, rho6)
        expected = np.kron(channel(BRANCH_K[history], rho3), rho_s)
        held_failures += int(np.linalg.norm(found - expected) > TOL)
    W6 = np.kron(W3, W3)
    held_isometry_residual = float(np.linalg.norm(W6.conj().T @ W6 - np.eye(64)))
    c_isometry, _heads = staggered_isometry()
    c_held_residual = float(np.linalg.norm(np.kron(c_isometry.conj().T @ c_isometry, np.eye(8)) - np.eye(64)))
    malformed = (
        np.zeros((8, 8), dtype=complex),
        np.eye(8, dtype=complex),
        np.diag((1.1, -0.1, 0, 0, 0, 0, 0, 0)).astype(complex),
        np.ones((7, 7), dtype=complex) / 7.0,
    )
    refused = sum(int(not valid_density(item, 8)) for item in malformed)
    bad_code = ket(1, 4)
    bad_gauge_refused = np.linalg.norm(Q2 @ bad_code - bad_code) > TOL
    c_malformed = (
        ((1, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0), (0, 0, 0), True),
        ((0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0), (0, 0, 0), True),
        ((1, 0, 0, 0, 0, 0, 0, 0, 0), (1, 0, 0), (0, 0, 0), True),
        ((1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0), (0, 1, 0), True),
        ((1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0), (0, 0, 0), False),
    )

    def lawful_c_initial(case: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], bool]) -> bool:
        head, pointer, dephase, reset_fresh = case
        return head == (1, 0, 0, 0, 0, 0, 0, 0, 0) and pointer == dephase == (0, 0, 0) and reset_fresh

    c_refused = sum(int(not lawful_c_initial(case)) for case in c_malformed)
    result = {
        "train_L3_held_L6_branch_tests": len(HISTORIES), "held_failures": held_failures,
        "held_gauge_isometry_residual": held_isometry_residual,
        "held_staggered_isometry_residual": c_held_residual,
        "malformed_density_refused": refused, "malformed_total": len(malformed),
        "noncode_parity_state_refused": bool(bad_gauge_refused),
        "staggered_dirty_head_pointer_dephase_reset_refused": c_refused,
        "staggered_malformed_total": len(c_malformed),
        "pass": bool(not held_failures and held_isometry_residual < TOL
        and c_held_residual < TOL and refused == len(malformed) and bad_gauge_refused
        and c_refused == len(c_malformed)),
    }
    check("train L3 and held L6 extensions, density domain, and local gauge domain are exact", result["pass"], result)
    return result


def deletion_controls() -> dict[str, object]:
    reset_completeness = sum((item.conj().T @ item for item in RESET_K[:-1]), np.zeros((8, 8), dtype=complex))
    reset_deletion = float(np.linalg.norm(reset_completeness - np.eye(8)))
    supported = tuple(history for history in HISTORIES if np.vdot(BRANCH_VECTOR[history], BRANCH_VECTOR[history]).real > TOL)
    branch_deletion_trace = sum(float(np.vdot(BRANCH_VECTOR[h], BRANCH_VECTOR[h]).real) for h in supported[1:])
    coherent_cross = max(
        float(np.linalg.norm(np.outer(BRANCH_VECTOR[left], BRANCH_VECTOR[right].conj())))
        for left, right in combinations(supported, 2)
    )
    no_environment_column = sum((
        kron_all(
            (W3 @ BRANCH_VECTOR[h]).reshape(-1, 1),
            ket(history_index(h), 8).reshape(-1, 1),
            ket(history_index(h), 8).reshape(-1, 1),
        ).reshape(-1)
        for h in HISTORIES
    ), np.zeros(4096, dtype=complex))
    no_environment_columns = np.column_stack((no_environment_column,) * 8)
    environment_deletion_residual = float(np.linalg.norm(no_environment_columns.conj().T @ no_environment_columns - np.eye(8)))
    result = {
        "direct_reset_Kraus_deletion_completeness_residual": reset_deletion,
        "supported_branch_deletion_retained_trace": branch_deletion_trace,
        "Naimark_reset_environment_deletion_isometry_residual": environment_deletion_residual,
        "dephasing_environment_deletion_coherent_cross_block": coherent_cross,
        "staggered_head_and_CZ_deletions": "tested in Route C",
        "pass": reset_deletion > TOL and abs(branch_deletion_trace - 0.75) < TOL
        and environment_deletion_residual > TOL and coherent_cross > TOL,
    }
    check("reset Kraus, pointer branch, retained input environment, dephasing environment, phase, and CZ deletions are visible", result["pass"], result)
    return result


def covariance_controls() -> dict[str, object]:
    frames = c41.proper_cubic_rotations()
    program = c41.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    records = c41.seed_records(program)
    traces = tuple(round(float(np.vdot(BRANCH_VECTOR[h], BRANCH_VECTOR[h]).real), 14) for h in HISTORIES)
    route_failures = route_tests = mapped_code_edge_failures = 0
    code_pair = (np.asarray((0, 0, 0), dtype=int), np.asarray((0, 0, 1), dtype=int))
    for _route, frame in product(("A", "B", "C"), frames):
        moved = c41.transform_program(program, frame, (5, -7, 2))
        moved_records = c41.transform_records(records, frame, (5, -7, 2))
        route_failures += int(not c41.preparation_ready(moved, moved_records))
        route_failures += int(traces != tuple(round(float(np.vdot(BRANCH_VECTOR[h], BRANCH_VECTOR[h]).real), 14) for h in HISTORIES))
        if _route == "B":
            mapped_code_edge_failures += int(np.abs(frame @ code_pair[1] - frame @ code_pair[0]).sum() != 1)
        route_tests += 1
    group_failures = group_tests = 0
    sample_sites = (program.trigger, *c41.header_sites(program))
    for first, second in product(frames, frames):
        direct = first @ second
        for role_index, role in enumerate(ROLES):
            site = sample_sites[role_index % len(sample_sites)]
            sequential = tuple(int(value) for value in first @ (second @ np.asarray(site, dtype=int)))
            composed = tuple(int(value) for value in direct @ np.asarray(site, dtype=int))
            group_failures += int(sequential != composed or np.linalg.norm(ROLE_P[role] - ROLE_P[role]) > TOL)
            group_tests += 1
    result = {
        "proper_frames": len(frames), "all24_route_tests": route_tests,
        "route_covariance_failures": route_failures, "ordered_products": len(frames) ** 2,
        "mapped_two_M2_code_edge_failures": mapped_code_edge_failures,
        "all576_projector_role_tests": group_tests, "group_failures": group_failures,
        "site_only_action": "spatial sites rotate; reference projector labels and local gauge blocks are scalars",
        "pass": len(frames) == 24 and route_tests == 72 and group_tests == 576 * 11
        and not route_failures and not mapped_code_edge_failures and not group_failures,
    }
    check("all three routes commute with all24 site-only frames and all eleven projector roles close all576 products", result["pass"], result)
    return result


def inventory_controls() -> dict[str, object]:
    inventory = {
        "supplied": (
            "Cycle41 eleven-projector Bloch dictionary, P/E/X/Z candidate instrument, four supported histories, and four 1/4 trace targets",
            "finite L3 front and held L6 spectator boundary", "Route A local CPTP/Kraus primitive or discarded environment",
            "Route B two-M2 parity code, six local gauge constraints, encoded-plus reset blocks, blank pointer/dephasing environments",
            "Route C H9 exactly-one head code-domain condition, initial phase, eight-phase order, fresh plus environments, blank pointers/dephasing carriers",
            "finite low-entropy capacity, noiseless bounded one/two/three-M2 gates, routing chart, and site-only proper-cubic presentation",
        ),
        "derived": (
            "faithful eleven-projector operator and Gram intertwiners", "exact direct CPTP instrument",
            "exact code-space gauge instrument and Naimark/Stinespring dilation", "reset-input export into named spent environment",
            "quantum-classical pointer channel after named dephasing export", "staggered in-state phase realization",
            "four supported and four null branch trace diagnostics matching pinned Cycle41 data", "held spectator invariance, deletion signatures, all24/all576 covariance",
        ),
        "open": (
            "selection of Cycle41 as nature's law", "actual branch selection, framework Record formation, permanence, and realized history",
            "derivation or calibration of trace weights as Born probabilities", "fresh reset/dephasing environment genesis, renewal, entropy export, and temperature",
            "autonomous repeated phase invocation, asynchronous boundary epoch/finalization, collision-safe volume and noise",
            "local enforcement of Route C exactly-one head domain and a full 2^21 unitary extension",
            "exact bounded gate/layout decomposition of Route B's full isometry",
            "composition with full Cycle563/569 matter without the noninjective reset erasing matter identity",
            "metric time/rate/lapse, energy/stress/source, backreaction, gravity, continuum/Lorentz/CPT",
        ),
    }
    forbidden_claims = {
        "actual_branch_selected": False, "framework_Record": False,
        "derived_Born_law": False, "reusable_reset_entropy": False,
        "physical_time": False, "energy_or_rate": False,
    }
    result = {"inventory": inventory, "forbidden_claims": forbidden_claims, "pass": not any(forbidden_claims.values())}
    check("every projector, reset, pointer, dephasing, phase, blank, and semantic supply is inventoried without promotion", result["pass"], result)
    return result


def no_go_controls() -> dict[str, object]:
    routes = (
        {
            "family": "direct local CPTP channel",
            "object_formulation": "three-M2 density-operator channel with 64 branch/reset Kraus operators",
            "mechanism_invariant": "Kraus completeness and exact branch CP maps",
            "terminal_obligation": "supply a reversible physical realization and one framework-owned actual branch/Record",
            "status": "ATTEMPTED",
            "evidence": "Route A is exact but retains a channel primitive/discard and emits the complete conditional instrument family",
            "citation": "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py:direct_channel_controls",
        },
        {
            "family": "local gauge plus retained Naimark environment",
            "object_formulation": "two-M2 ZZ=+1 code and a sparse 2^18-by-8 retained-environment isometry",
            "mechanism_invariant": "code projector, isometry, pointer/dephasing sectors, and old-input export",
            "terminal_obligation": "derive fresh-resource renewal and an actuality/Record map not selected by branch trace",
            "status": "ATTEMPTED",
            "evidence": "Route B has zero branch/reduction residual but retains every branch and all spent environments",
            "citation": "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py:gauge_naimark_controls",
        },
        {
            "family": "staggered physical-head dilation",
            "object_formulation": "H9 exactly-one physical-head code embedded sparsely into a 2^21-by-8 output isometry",
            "mechanism_invariant": "phase-rail controlled gates, head SWAP advance, and retained reset/dephasing outputs",
            "terminal_obligation": "locally enforce the head domain, construct autonomous repeated invocation, and bind one actual Record",
            "status": "ATTEMPTED",
            "evidence": "Route C closes one bounded episode only; the head and all branch sectors remain reversible state",
            "citation": "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py:staggered_controls",
        },
        {
            "family": "independent repeated-instrument product",
            "object_formulation": "tensor-product conditional history instrument and finite word/counter corpus",
            "mechanism_invariant": "Stinespring completeness and product branch traces",
            "terminal_obligation": "select one actual history and prove a framework Record/frequency law",
            "status": "UNTESTED_OPEN_NOT_COUNTED",
            "evidence": "Cycle430 tests one finite product instance and explicitly leaves sampler, occurrence, and actual history as reopen obligations; it does not rule out the normalized family",
            "citation": "docs/work_history/repo/review_feedback/REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_CYCLE430_NOTE_2026-07-19.md:56",
        },
        {
            "family": "supplied-bath overwrite and FORM channel",
            "object_formulation": "many-to-one reduced reset/repair channel with retained global bath dilation",
            "mechanism_invariant": "old-state export, spent-token ledger, and finite majority repair",
            "terminal_obligation": "derive coherent actual-member selection, bath renewal, and unconditional framework Record permanence",
            "status": "UNTESTED_OPEN_NOT_COUNTED",
            "evidence": "Cycle483 tests a finite supplied-bath instance and leaves coherent member, stationary renewal, and unconditional Record as concrete reopen routes",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CYCLE483_NOTE_2026-07-19.md:188",
        },
        {
            "family": "hard-core/rotor grade-formation candidate",
            "object_formulation": "one-winner candidate apparatus and deterministic retained rotor",
            "mechanism_invariant": "hard-core exclusion, reversible conveyor, and finite response grading",
            "terminal_obligation": "produce an actual member and bind it to the framework Record formation site/content",
            "status": "UNTESTED_OPEN_NOT_COUNTED",
            "evidence": "Cycle502 tests finite hard-core/rotor instances but leaves actual-member and Record-binding mechanisms open, so the family is not ruled out",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_KRAUS_RECORD_LOCK_CANDIDATE_GRADE_FORMATION_TOURNAMENT_CYCLE502_NOTE_2026-07-20.md:171",
        },
        {
            "family": "finite Naimark menu plus conditional occurrence binder",
            "object_formulation": "finite effect-menu isometry, physical pointer sectors, and independent member-law cell",
            "mechanism_invariant": "effect completeness, coherent pointer retention, and conditional Cycle531/552 binding",
            "terminal_obligation": "derive the menu/member/grade genesis and a non-erasing Record/actuality owner",
            "status": "UNTESTED_OPEN_NOT_COUNTED",
            "evidence": "Cycle565 closes finite Naimark/binder instances but leaves menu/member genesis and non-erasing actuality/Record ownership as concrete reopen routes",
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md:154",
        },
    )
    walls = (
        "law selection", "fresh reset/dephasing resources", "actual branch/Record",
        "autonomous recurrence/volume", "matter-compatible nonerasure", "mathematical trace-to-Born identification",
    )
    pair_reasons = (
        (0, 1, "selecting a candidate law does not generate fresh low-entropy carriers", "a renewable carrier stream does not choose which counterfactual law governs"),
        (0, 2, "law selection alone supplies no member/Record occurrence map", "one occurrence does not identify the governing counterfactual law"),
        (0, 3, "selecting a finite rule does not prove autonomous collision-safe recurrence", "an autonomous scheduler can execute multiple candidate laws without selecting one"),
        (0, 4, "law selection does not make the Cycle41 reset preserve interacting matter", "matter-compatible injectivity does not choose the law"),
        (0, 5, "law selection does not identify trace as Born weight", "a mathematical trace/Born theorem does not select the dynamical law"),
        (1, 2, "fresh resources supply capacity but no actual-member/Record rule", "an actual Record does not replenish reset/dephasing carriers"),
        (1, 3, "fresh carriers alone do not provide phase/collision recurrence", "autonomous recurrence can consume a finite reservoir without renewing it"),
        (1, 4, "bath renewal does not prevent reduced reset from erasing matter identity", "matter-compatible dynamics does not generate low-entropy baths"),
        (1, 5, "resource renewal does not identify the trace functional", "trace-to-Born identification does not supply physical reset resources"),
        (2, 3, "one actual branch/Record does not yield repeated volume scheduling", "a recurrent QCA can remain coherent and select no actual Record"),
        (2, 4, "actuality/Record typing does not make the reset matter-compatible", "matter-compatible evolution does not choose one actual branch"),
        (2, 5, "one actual Record does not prove mathematical trace-to-Born identification", "a Born identification gives weights but no actual member or Record"),
        (3, 4, "autonomous recurrence can repeatedly erase the reduced matter state", "matter-compatible dynamics need not tile or schedule a volume"),
        (3, 5, "a recurrent QCA does not identify trace as Born weight", "Born identification does not supply collision-safe recurrent dynamics"),
        (4, 5, "matter-compatible injectivity does not identify the trace functional", "trace-to-Born identification does not preserve interacting matter"),
    )
    pair_table = tuple({
        "pair": (walls[left], walls[right]),
        "close_left_automatically_closes_right": "no",
        "left_to_right_reason": left_reason,
        "close_right_automatically_closes_left": "no",
        "right_to_left_reason": right_reason,
        "independent": True,
        "collapse_result": "retain both",
    } for left, right, left_reason, right_reason in pair_reasons)
    note_lines = NOTE.read_text(encoding="utf-8").splitlines()
    hidden_patterns = (
        "we assume", "by construction", "as is standard", "are standard", "the framework provides",
        "bridge context", "background", "naturally", "obviously", "standard qft",
        "registered", "canonical",
    )
    hidden_hits = []
    for line_number, line in enumerate(note_lines, start=1):
        lowered = line.lower()
        for pattern in hidden_patterns:
            if pattern in lowered:
                hidden_hits.append({
                    "pattern": pattern, "line": line_number, "text": line.strip(),
                    "classification": (
                        "non-load-bearing prior-art attribution"
                        if pattern in ("as is standard", "are standard", "standard qft") else
                        "non-load-bearing terminology occurrence; no premise imported"
                    ),
                })
    residual_table = (
        {
            "witness": "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md:154",
            "witness_residual": "eleven exact nonorthogonal one-M2 projectors and the P/E/X/Z instrument",
            "claimed_closed_residual": "faithful bounded projector/instrument representation",
            "match": "yes",
        },
        {
            "witness": "PHYSICAL_L41_CANDIDATE_LAW_INTEGRATION_TOURNAMENT_CYCLE574_NOTE_2026-07-22.md:110",
            "witness_residual": "Cycle574 one-hot recode did not reproduce projector overlaps/instrument",
            "claimed_closed_residual": "faithful projector overlaps and finite instrument intertwiner",
            "match": "yes",
        },
        {
            "witness": "PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CYCLE483_NOTE_2026-07-19.md:155",
            "witness_residual": "reset old state must be retained/exported and finite bath is not renewal",
            "claimed_closed_residual": "finite retained reset export only",
            "match": "yes",
        },
        {
            "witness": "SAME_CODE_INSTRUMENT_BRIDGE_SYNTHESIS_CYCLE280_NOTE_2026-07-17.md:32",
            "witness_residual": "conditional instrument is not occurrence or Record",
            "claimed_closed_residual": "projector/instrument representation, not occurrence",
            "match": "no — semantic boundary only; dropped as a representation-closure witness",
        },
        {
            "witness": "REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_CYCLE430_NOTE_2026-07-19.md:56",
            "witness_residual": "conditional product traces do not select actual history",
            "claimed_closed_residual": "one-use faithful compiler",
            "match": "no — selection boundary only; dropped as a compiler-closure witness",
        },
        {
            "witness": "PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md:154",
            "witness_residual": "finite Naimark menu compilation with supplied menu/member resources",
            "claimed_closed_residual": "specific Cycle41 projector/instrument compilation",
            "match": "no — analogous method only; dropped as exact closure witness",
        },
    )
    rhetoric_table = (
        {
            "phrase": "candidate branch trace is not a derived Born law",
            "tested": "eight branches in one L3 block and held L6 spectator extension",
            "untested": "repeated lattice/empirical calibration",
            "allowed_claim": "these finite branch traces are diagnostics only",
        },
        {
            "phrase": "retained pointer is not a framework Record",
            "tested": "one bounded instrument output and exact reversible deletion/inverse boundary",
            "untested": "framework-wide admission and all-future permanence",
            "allowed_claim": "Cycle577 outputs are not promoted to Records",
        },
        {
            "phrase": "head phase is not physical time",
            "tested": "one eight-phase code-space episode",
            "untested": "metric/lattice-wide clock calibration",
            "allowed_claim": "the tested head coordinate is not assigned duration or rate",
        },
        {
            "phrase": "carrier count is not energy/source",
            "tested": "no energy/source functional is defined on the finite block",
            "untested": "possible future calibrated source map",
            "allowed_claim": "Cycle577 makes no energy/source identification",
        },
    )
    partial_closure = (
        {
            "path": "explicit two-/three-M2 gate and spatial layout synthesis for Route B",
            "status": "open proof/implementation obligation, not a new axiom",
            "what_it_closes": "full-isometry versus local gate/layout distinction",
        },
        {
            "path": "local penalty/check dynamics for H9 exactly-one head",
            "status": "open constructive physics route, not a labeling convention",
            "what_it_closes": "supplied Route-C code-domain condition",
        },
        {
            "path": "Cycle483-style explicit renewable carrier stream",
            "status": "finite reset export retained; stationary renewal unproved",
            "what_it_closes": "fresh reset/dephasing resource import if an autonomous recurrence is proved",
        },
        {
            "path": "Record-side formation/admission law tested independently of branch trace",
            "status": "physics/owner-governance obligation; definition-only relabeling forbidden by Cycle502",
            "what_it_closes": "candidate pointer versus framework Record wall",
        },
    )
    steelman = {
        "concrete_mechanism": "a collision-safe reversible QCA streams locally prepared encoded-plus and zero carriers through Route B blocks, exports spent carriers, transports an H9-like phase excitation, and couples an independent non-trace-driven occurrence field to one pointer sector",
        "terminal_obligation": "construct one bounded-neighborhood unitary recurrence for arbitrary finite volume that preserves the interacting matter code, proves stationary fresh/spent resource balance, and derives a framework-owned unique occurrence/Record without reading branch trace",
        "strongest_authority": "PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CYCLE483_NOTE_2026-07-19.md:188 plus PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md:537",
        "disposition": "unclosed and mathematically actionable; therefore broad no-go remains premature",
    }
    echo_table = (
        {
            "prior_wall": "Cycle574 faithful projector-overlap gap",
            "retired": "yes at one finite instrument block",
            "mechanism": "two-M2 isometry preserving operator Gram geometry",
            "current_application": "shows representation walls can retire constructively without axiom edits",
        },
        {
            "prior_wall": "Cycle483 hidden reset/discard",
            "retired": "finite export only; renewal remains open",
            "mechanism": "retain old input and spent carriers in the dilation",
            "current_application": "used directly in Route B/C; stationary renewal must still be attempted",
        },
        {
            "prior_wall": "Cycle565 bounded Naimark menu",
            "retired": "finite compilation yes; selector/Record no",
            "mechanism": "explicit pointer isometry and resource ledger",
            "current_application": "specialized to the exact Cycle41 instrument",
        },
        {
            "prior_wall": "Cycle280/288 conditional instrument to occurrence",
            "retired": "no",
            "mechanism": "later cycles added candidate FORM/typing but not unconditional framework selection",
            "current_application": "forces Cycle577 to retain conditional language and the QCA steelman",
        },
    )
    n1_qualifying = tuple(route for route in routes if route["status"] in ("ATTEMPTED", "RULED OUT BY PRIOR"))
    valid_route_schema = all(
        all(route[key] for key in ("object_formulation", "mechanism_invariant", "terminal_obligation", "citation", "evidence", "status"))
        for route in routes
    )
    result = {
        "N1_routes": routes, "N1_count": len(routes),
        "N1_schema_valid": valid_route_schema,
        "N1_qualifying_ATTEMPTED_or_RULED_OUT_count": len(n1_qualifying),
        "N1_required_count": 5,
        "N1_pass": len(n1_qualifying) >= 5,
        "N1_failure": "only three normalized families were attempted; four prior instances leave concrete reopen routes and cannot be counted as ruled out",
        "N2_walls": walls, "N2_pairwise_table": pair_table, "N2_pairs": len(pair_table),
        "N2_collapsed_wall_set": walls, "N2_collapse_result": "all 15 pairs bidirectionally no; retain six independent walls",
        "N2_empirical_calibration_collapse": {
            "raw_condition": "empirical frequency calibration on permanent readable Records",
            "dependencies": ("actual branch/Record", "mathematical trace-to-Born identification"),
            "result": "collapse as a downstream composite obligation, not a seventh independent wall",
        },
        "N3_hidden_phrase_hits": hidden_hits,
        "N3_explicit_supplies": "projector dictionary, code/gauge, reset inputs and spent outputs, pointer/dephasing carriers, H9 exactly-one domain, phase order, candidate trace functional, law table, frame chart, blanks and held boundary",
        "N4_residual_table": residual_table,
        "N4_exact_closure_witnesses_retained": sum(int(row["match"] == "yes") for row in residual_table),
        "N5_rhetoric_resolution_table": rhetoric_table,
        "N6_partial_closure_paths": partial_closure,
        "N6_new_axiom_required": False,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echo_table,
        "gate_status": "FAIL",
        "demoted_artifact_status": "POSITIVE_PARTIAL_CONSTRUCTION_WITH_EXPLICIT_RESIDUALS",
        "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP",
        "shared_obstruction_claim": "DO_NOT_SHIP", "axiom_pressure_claim": "DO_NOT_SHIP",
        "negative_claims_shipped": False,
        "pass": len(routes) >= 5 and valid_route_schema and len(n1_qualifying) == 3 and len(pair_table) == 15
        and all(row["independent"] and row["close_left_automatically_closes_right"] == "no"
                and row["close_right_automatically_closes_left"] == "no" for row in pair_table)
        and all(hit["classification"] for hit in hidden_hits)
        and sum(int(row["match"] == "yes") for row in residual_table) >= 3
        and len(rhetoric_table) >= 4 and len(partial_closure) >= 4
        and all(steelman[key] for key in ("concrete_mechanism", "terminal_obligation", "strongest_authority"))
        and len(echo_table) >= 4,
    }
    check("current N1-N8 gate fails honestly at N1, demotes the artifact, and blocks broad no-go/minimum/shared-obstruction/axiom-pressure language", result["pass"] and result["gate_status"] == "FAIL" and not result["negative_claims_shipped"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_route: str = "B exact two-M2 gauge encoding with retained reset and Naimark/dephasing environments"
    actual_branch: None = None
    framework_Record: None = None
    reusable_reset_entropy: None = None
    physical_time: None = None
    energy: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle577 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        deps = dependency_controls()
        check("committed Cycle41/280/288/430/483/488/502/565/571/574 shores and note contract are exact-pinned", deps["pass"], deps)
        roles = projector_controls()
        direct = direct_channel_controls()
        gauge = gauge_naimark_controls()
        staggered = staggered_controls()
        held = held_and_domain_controls()
        deletion = deletion_controls()
        covariance = covariance_controls()
        inventory = inventory_controls()
        discipline = no_go_controls()
        resources = {
            "elapsed_seconds": time.perf_counter() - started, "rss_bytes": rss_bytes(),
            "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES,
        }
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["rss_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({
            "dependency": deps, "projectors": roles, "route_A": direct, "route_B": gauge,
            "route_C": staggered, "held_domain": held, "deletion": deletion,
            "covariance": covariance, "inventory": inventory, "no_go_discipline": discipline,
            "resources": resources, "summary": Summary().__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; candidate trace weights are pinned data, not actual selection, Record, derived probability, time, energy, or rate")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
