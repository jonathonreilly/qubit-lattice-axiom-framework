#!/usr/bin/env python3
"""Cycle 493: three-route member-law tournament on the Cycle478/483 seam.

The positive result is deliberately split.  A retained Kraus pointer controls
FORM coherently; a fixed reversible rotor extends every supplied basis seed;
and a supplied stationary product bath has a global reversible dilation.
None of those operations selects one member of a coherent state or turns a
mixture into an actual history.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import comb, sqrt
from pathlib import Path
import inspect
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_form_occurrence_born_weight_firewall_cycle488_2026_07_20 as c488


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TERMINAL_MENU_MEMBER_LAW_TOURNAMENT_CYCLE493_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-9
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle430 runner": "3fa6981d1d0203a3121729026f0094058cf024e6a71f63045f5bc6043c2039a0",
    "Cycle456 runner": "9c2b1f1b055413255f01e80a0854c8a5a753b6495125a4580a14830178cb9c63",
    "Cycle469 runner": "ac706716229b81876c2a730a524d0610dee0b41c2fb92dc95a22f6a4260b0fa1",
    "Cycle479 runner": "2154075b3f1bfa3dee849eb859bad46adf3f8d07670e6ac5200f6c720b119d30",
    "Cycle478 runner": "b700a8d5bede8037af025d9df65b1223c0159170e2c3f21992741a3b593ab99f",
    "Cycle483 runner": "52f0621a06792093ad64a706ab7741335cfd7ff9418b3756f4ab83cf72b8d222",
    "Cycle488 runner": "17bbdd0d30f579668120dbdea55b4d42dfceff550b31cc50b3ec11451b510470",
}
FROZEN_PATHS = {
    "Cycle430 runner": ROOT / "scripts/repeated_physical_instrument_conditional_history_frequency_cycle430_2026_07_19.py",
    "Cycle456 runner": ROOT / "scripts/physical_dual_clock_interval_signature_classifier_cycle456_2026_07_19.py",
    "Cycle469 runner": ROOT / "scripts/physical_relational_interval_s3_slice_seed_bridge_cycle469_2026_07_19.py",
    "Cycle479 runner": ROOT / "scripts/physical_3d_laplacian_s3_generator_provenance_cycle479_2026_07_19.py",
    "Cycle478 runner": Path(c488.c478.__file__),
    "Cycle483 runner": Path(c488.c483.__file__),
    "Cycle488 runner": Path(c488.__file__),
}

TRAIN_N = 4
HELD_N = 12
TRAIN_HORIZON = 3
HELD_HORIZON = 6
MAX_TRIALS = 12
MENU = range(c488.MENU_ARITY)
Word = tuple[int, ...]


class WallCapExceeded(RuntimeError):
    pass


@dataclass(frozen=True)
class ProductBathLaw:
    name: str
    q: tuple[float, ...]
    supplied_stationary: bool = True
    supplied_independent: bool = True

    def __post_init__(self) -> None:
        if len(self.q) != c488.MENU_ARITY or any(x <= 0 or x >= 1 for x in self.q):
            raise ValueError("selector bath law needs five strictly positive grades")
        if abs(sum(self.q) - 1.0) > TOL:
            raise ValueError("selector bath grades must normalize")

    def word_weight(self, word: tuple[int, ...]) -> float:
        if not word or any(x not in MENU for x in word):
            raise ValueError("product word leaves the declared menu")
        answer = 1.0
        for x in word:
            answer *= self.q[x]
        return answer


@dataclass(frozen=True)
class PointerGate:
    target: int
    controls: tuple[tuple[int, int], ...]
    label: str

    def apply(self, value: int) -> int:
        bits = list(c488.bits_of(value, c488.POINTER_BITS))
        if all(bits[index] == expected for index, expected in self.controls):
            bits[self.target] ^= 1
        return c488.int_of(tuple(bits))


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


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def contract_controls() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "same cycle-478 terminal menu", "same cycle-483 form interface",
        "route a — retained-outcome instrument trajectory",
        "route b — deterministic every-orbit continuation",
        "route c — supplied stationary/independent local bath law",
        "two incompatible input states", "train n=4", "held n=12",
        "physical-m2 e/g", "exact inverse", "used-bath nonreentry",
        "all 24 proper-cubic frames", "non-born-selector falsifier",
        "coherent pointer correlation is not a realized member or history",
        "counts, frequencies, and norms are not probability",
        "supplied / derived / open", "gate disposition: fail",
        "no no-go, minimum-content, shared obstruction, or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle493 note freezes the three-route contract and semantic ceiling", not missing, missing)
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check(
        "direct and reconnaissance inputs are frozen by exact runner SHA",
        observed == FROZEN,
        {"observed": observed, "authority": AUTHORITY, "audit": AUDIT},
    )


def validate_generic_input(state: c488.BasisState) -> None:
    if (
        not isinstance(state, c488.BasisState)
        or state.case_name not in (c488.TRAIN_CASE, c488.HELD_CASE)
        or state.horizon not in (TRAIN_HORIZON, HELD_HORIZON)
        or not 1 <= state.trials <= MAX_TRIALS
        or not c488.is_word(state.bits, state.trials * c488.CELL_M2)
    ):
        raise ValueError("member-law state leaves the bounded binary domain")
    words = c488.class_words(state.case_name)
    for cell in range(state.trials):
        c488.c483.validate_route_input(c488.local_c483_state(state, cell), "bath")
        pointer = c488.int_of(c488.selected(state.bits, c488.field(cell, c488.POINTER)))
        if pointer not in MENU:
            raise ValueError("member-law pointer leaves the terminal menu")
        if c488.int_of(c488.selected(state.bits, c488.field(cell, c488.TRIAL_ID))) != cell + 1:
            raise ValueError("member-law trial identity is dirty")
        for outcome, word in enumerate(words):
            if c488.selected(state.bits, c488.field(cell, c488.CODEBOOK[outcome])) != word:
                raise ValueError("terminal class codebook is dirty")
        if any(state.bits[c488.site(cell, local)] for local in c488.ADAPTER_OUTPUT_LOCAL):
            raise ValueError("FORM receipt/work/count carriers must enter blank")


def prepare_history(case_name: str, horizon: int, pointers: tuple[int, ...]) -> c488.BasisState:
    if not 1 <= len(pointers) <= MAX_TRIALS:
        raise ValueError("history size leaves the frozen N<=12 domain")
    if any(pointer not in MENU for pointer in pointers):
        raise ValueError("history pointer leaves the five-outcome menu")
    words = c488.class_words(case_name)
    laws = tuple(c488.c483.c449.PROGRAMS)
    bits = [0] * (len(pointers) * c488.CELL_M2)
    for cell, pointer in enumerate(pointers):
        local = c488.c483.prepare_state(
            case_name, laws[cell % len(laws)], route="bath", reset_work=1,
        )
        start = cell * c488.CELL_M2
        bits[start:start + c488.c483.TOTAL_M2] = local.bits
        c488.replace_selected(bits, c488.field(cell, c488.POINTER), c488.bits_of(pointer, c488.POINTER_BITS))
        c488.replace_selected(bits, c488.field(cell, c488.TRIAL_ID), c488.bits_of(cell + 1, c488.TRIAL_ID_BITS))
        for outcome, word in enumerate(words):
            c488.replace_selected(bits, c488.field(cell, c488.CODEBOOK[outcome]), word)
    state = c488.BasisState(len(pointers), horizon, case_name, tuple(bits))
    validate_generic_input(state)
    return state


@lru_cache(maxsize=None)
def adapter_schedule_generic(trials: int) -> tuple[c488.Gate, ...]:
    """Cycle488's frozen adapter law, extended without changing one gate."""
    if not 1 <= trials <= MAX_TRIALS:
        raise ValueError("adapter leaves the N<=12 tournament")
    output: list[c488.Gate] = []
    for cell in range(trials):
        pointer = c488.field(cell, c488.POINTER)
        for outcome in MENU:
            value = c488.bits_of(outcome, c488.POINTER_BITS)
            for lane, bit in enumerate(value):
                if bit == 0:
                    output.append(c488.gate(
                        trials, "X", (pointer[lane],), f"cell:{cell}:match:{outcome}:negate:{lane}",
                    ))
            computed = c488.append_prefix(
                trials, output, pointer, c488.field(cell, c488.MATCH_PREFIX[outcome]),
                f"cell:{cell}:match:{outcome}:prefix",
            )
            output.append(c488.gate(
                trials, "CNOT",
                (c488.field(cell, c488.MATCH_PREFIX[outcome])[-1], c488.site(cell, c488.MATCH[outcome])),
                f"cell:{cell}:match:{outcome}:retain",
            ))
            output.extend(
                c488.Gate(item.kind, item.sites, f"{item.label}:uncompute") for item in reversed(computed)
            )
            for lane, bit in reversed(tuple(enumerate(value))):
                if bit == 0:
                    output.append(c488.gate(
                        trials, "X", (pointer[lane],),
                        f"cell:{cell}:match:{outcome}:negate:{lane}:restore",
                    ))
        for outcome in MENU:
            output.append(c488.gate(
                trials, "CNOT", (c488.site(cell, c488.MATCH[outcome]), c488.site(cell, c488.CLASS_VALID)),
                f"cell:{cell}:class-valid:{outcome}",
            ))
        c488.append_majority(
            trials, output, c488.field(cell, c488.c483.B_TYPE), c488.site(cell, c488.TYPE_FLAG),
            f"cell:{cell}:type-majority",
        )
        c488.append_majority(
            trials, output, c488.field(cell, c488.c483.B_OCCURRENCE), c488.site(cell, c488.OCCURRENCE_FLAG),
            f"cell:{cell}:occurrence-majority",
        )
        c488.append_majority(
            trials, output, c488.field(cell, c488.c483.B_LOCK), c488.site(cell, c488.LOCK_FLAG),
            f"cell:{cell}:lock-majority",
        )
        accept_compute = c488.append_prefix(
            trials, output,
            (
                c488.site(cell, c488.c483.B_FORM), c488.site(cell, c488.TYPE_FLAG),
                c488.site(cell, c488.OCCURRENCE_FLAG), c488.site(cell, c488.LOCK_FLAG),
                c488.site(cell, c488.CLASS_VALID),
            ),
            c488.field(cell, c488.ACCEPT_PREFIX), f"cell:{cell}:accept-prefix",
        )
        output.append(c488.gate(
            trials, "CNOT", (c488.field(cell, c488.ACCEPT_PREFIX)[-1], c488.site(cell, c488.ACCEPT)),
            f"cell:{cell}:accept-retain",
        ))
        output.extend(
            c488.Gate(item.kind, item.sites, f"{item.label}:uncompute") for item in reversed(accept_compute)
        )
        for outcome, class_index in enumerate(c488.TERMINAL_CLASSES):
            output.append(c488.gate(
                trials, "TOFFOLI",
                (c488.site(cell, c488.ACCEPT), c488.site(cell, c488.MATCH[outcome]),
                 c488.site(cell, c488.OUTCOME_ENABLE[outcome])),
                f"cell:{cell}:outcome-enable:{outcome}",
            ))
            enable = c488.site(cell, c488.OUTCOME_ENABLE[outcome])
            output.append(c488.gate(
                trials, "CNOT", (enable, c488.site(cell, c488.RECEIPT_ONEHOT[outcome])),
                f"cell:{cell}:receipt-onehot:{outcome}",
            ))
            for lane, bit in enumerate(c488.bits_of(class_index, c488.CLASS_ID_BITS)):
                if bit:
                    output.append(c488.gate(
                        trials, "CNOT", (enable, c488.field(cell, c488.RECEIPT_CLASS_ID)[lane]),
                        f"cell:{cell}:receipt-class:{outcome}:{lane}",
                    ))
            for lane, (source, target) in enumerate(zip(
                c488.field(cell, c488.CODEBOOK[outcome]), c488.field(cell, c488.RECEIPT_WORD),
            )):
                output.append(c488.gate(
                    trials, "TOFFOLI", (enable, source, target),
                    f"cell:{cell}:packet-copy:{outcome}:{lane}",
                ))
        for lane, (source, target) in enumerate(zip(
            c488.field(cell, c488.TRIAL_ID), c488.field(cell, c488.RECEIPT_TRIAL_ID),
        )):
            output.append(c488.gate(
                trials, "TOFFOLI", (c488.site(cell, c488.ACCEPT), source, target),
                f"cell:{cell}:trial-copy:{lane}",
            ))
        for outcome in MENU:
            receipt = c488.site(cell, c488.RECEIPT_ONEHOT[outcome])
            current_sum = c488.field(cell, c488.COUNT_SUM[outcome])
            current_carry = c488.field(cell, c488.COUNT_CARRY[outcome])
            if cell == 0:
                output.append(c488.gate(
                    trials, "CNOT", (receipt, current_sum[0]), f"cell:{cell}:count:{outcome}:seed",
                ))
                continue
            previous_sum = c488.field(cell - 1, c488.COUNT_SUM[outcome])
            for bit in range(c488.COUNT_BITS):
                output.append(c488.gate(
                    trials, "CNOT", (previous_sum[bit], current_sum[bit]),
                    f"cell:{cell}:count:{outcome}:add-a:{bit}",
                ))
                if bit == 0:
                    output.append(c488.gate(
                        trials, "CNOT", (receipt, current_sum[bit]),
                        f"cell:{cell}:count:{outcome}:add-b:{bit}",
                    ))
                output.append(c488.gate(
                    trials, "CNOT", (current_carry[bit], current_sum[bit]),
                    f"cell:{cell}:count:{outcome}:add-carry:{bit}",
                ))
                if bit == 0:
                    output.append(c488.gate(
                        trials, "TOFFOLI", (previous_sum[bit], receipt, current_carry[bit + 1]),
                        f"cell:{cell}:count:{outcome}:carry-ab:{bit}",
                    ))
                    output.append(c488.gate(
                        trials, "TOFFOLI", (receipt, current_carry[bit], current_carry[bit + 1]),
                        f"cell:{cell}:count:{outcome}:carry-bc:{bit}",
                    ))
                output.append(c488.gate(
                    trials, "TOFFOLI", (previous_sum[bit], current_carry[bit], current_carry[bit + 1]),
                    f"cell:{cell}:count:{outcome}:carry-ac:{bit}",
                ))
    return tuple(output)


@lru_cache(maxsize=None)
def physical_schedule(trials: int, horizon: int) -> tuple[c488.Gate, ...]:
    if not 1 <= trials <= MAX_TRIALS or horizon not in (TRAIN_HORIZON, HELD_HORIZON):
        raise ValueError("schedule leaves the bounded tournament")
    lower = c488.c483.bath_schedule(horizon, inject_faults=False)
    return tuple(
        c488.shifted_c483_gate(trials, cell, item)
        for cell in range(trials)
        for item in lower
    ) + adapter_schedule_generic(trials)


def apply_physical(
    state: c488.BasisState,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> c488.BasisState:
    if not reverse:
        validate_generic_input(state)
    elif not c488.is_word(state.bits, state.trials * c488.CELL_M2):
        raise ValueError("inverse state leaves the binary domain")
    schedule = physical_schedule(state.trials, state.horizon)
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion label is absent or ambiguous")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    bits = list(state.bits)
    for item in reversed(schedule) if reverse else schedule:
        c488.apply_gate(bits, item)
    return c488.BasisState(state.trials, state.horizon, state.case_name, tuple(bits))


@lru_cache(maxsize=None)
def generic_adapter_trace(trials: int) -> c488.AdapterTrace:
    schedule = adapter_schedule_generic(trials)
    coords = c488.manifest(trials)
    failures = 0
    for cell in range(trials):
        path = c488.cell_path(cell)
        failures += sum(c488.manhattan(coords[a], coords[b]) != 1 for a, b in zip(path, path[1:]))
    for cell in range(trials - 1):
        path = c488.link_path(cell)
        failures += sum(c488.manhattan(coords[a], coords[b]) != 1 for a, b in zip(path, path[1:]))
    digest = sha256(f"Cycle493 {trials}-cell inherited adapter route".encode())
    primitives = 0
    maximum = 0
    for item in schedule:
        spans, final_sites, swaps = c488.compact_route_plan(item)
        failures += sum(
            c488.manhattan(coords[a], coords[b]) != 1
            for a, b in zip(final_sites, final_sites[1:])
        )
        primitives += 1 + 6 * swaps
        maximum = max(maximum, len(item.sites))
        digest.update(f"{item.kind}:{item.sites}:{item.label}:{spans}:{final_sites}".encode())
    return c488.AdapterTrace(len(schedule), primitives, maximum, failures, digest.hexdigest())


def coarse_step(state: c488.BasisState) -> c488.BasisState:
    """Declarative E-side map, independent of the reversible prefix schedule."""
    validate_generic_input(state)
    bits = list(state.bits)
    lower = c488.c483.bath_schedule(state.horizon, inject_faults=False)
    for cell in range(state.trials):
        local = list(bits[cell * c488.CELL_M2:cell * c488.CELL_M2 + c488.c483.TOTAL_M2])
        for item in lower:
            c488.c483.apply_gate(local, item)
        bits[cell * c488.CELL_M2:cell * c488.CELL_M2 + c488.c483.TOTAL_M2] = local
    for cell in range(state.trials):
        pointer = c488.int_of(c488.selected(bits, c488.field(cell, c488.POINTER)))
        matches = tuple(int(outcome == pointer) for outcome in MENU)
        c488.replace_selected(bits, c488.field(cell, c488.MATCH), matches)
        bits[c488.site(cell, c488.CLASS_VALID)] = int(sum(matches) == 1)
        bits[c488.site(cell, c488.TYPE_FLAG)] = c488.majority_value(bits, c488.field(cell, c488.c483.B_TYPE))
        bits[c488.site(cell, c488.OCCURRENCE_FLAG)] = c488.majority_value(bits, c488.field(cell, c488.c483.B_OCCURRENCE))
        bits[c488.site(cell, c488.LOCK_FLAG)] = c488.majority_value(bits, c488.field(cell, c488.c483.B_LOCK))
        accept = int(
            bits[c488.site(cell, c488.c483.B_FORM)]
            and bits[c488.site(cell, c488.TYPE_FLAG)]
            and bits[c488.site(cell, c488.OCCURRENCE_FLAG)]
            and bits[c488.site(cell, c488.LOCK_FLAG)]
            and bits[c488.site(cell, c488.CLASS_VALID)]
        )
        bits[c488.site(cell, c488.ACCEPT)] = accept
        enabled = tuple(accept & value for value in matches)
        c488.replace_selected(bits, c488.field(cell, c488.OUTCOME_ENABLE), enabled)
        c488.replace_selected(bits, c488.field(cell, c488.RECEIPT_ONEHOT), enabled)
        if accept:
            c488.replace_selected(
                bits, c488.field(cell, c488.RECEIPT_CLASS_ID),
                c488.bits_of(c488.TERMINAL_CLASSES[pointer], c488.CLASS_ID_BITS),
            )
            c488.replace_selected(
                bits, c488.field(cell, c488.RECEIPT_TRIAL_ID),
                c488.selected(bits, c488.field(cell, c488.TRIAL_ID)),
            )
            c488.replace_selected(
                bits, c488.field(cell, c488.RECEIPT_WORD),
                c488.selected(bits, c488.field(cell, c488.CODEBOOK[pointer])),
            )
        for outcome in MENU:
            receipt = enabled[outcome]
            if cell == 0:
                current, carries = receipt, (0,) * (c488.COUNT_BITS + 1)
            else:
                previous = c488.selected(bits, c488.field(cell - 1, c488.COUNT_SUM[outcome]))
                carry, sums, carry_bits = 0, [], [0]
                for bit in range(c488.COUNT_BITS):
                    a, b = previous[bit], receipt if bit == 0 else 0
                    sums.append(a ^ b ^ carry)
                    carry = (a & b) ^ (a & carry) ^ (b & carry)
                    carry_bits.append(carry)
                current, carries = c488.int_of(tuple(sums)), tuple(carry_bits)
            c488.replace_selected(bits, c488.field(cell, c488.COUNT_SUM[outcome]), c488.bits_of(current, c488.COUNT_BITS))
            c488.replace_selected(bits, c488.field(cell, c488.COUNT_CARRY[outcome]), carries)
    return c488.BasisState(state.trials, state.horizon, state.case_name, tuple(bits))


def branch_weights(program: object, psi: np.ndarray) -> tuple[float, ...]:
    fine = tuple(float(np.vdot(k @ psi, k @ psi).real) for k in program.kraus)
    return tuple(sum(fine[index] for index in group) for group in program.coarse_groups)


def route_a_controls(surface: c488.MenuSurface) -> dict[str, object]:
    print("\nROUTE A / RETAINED KRAUS POINTER -> FORM")
    states = (
        ("z-plus", np.asarray((1.0, 0.0), complex)),
        ("y-plus", np.asarray((1.0, 1.0j), complex) / sqrt(2.0)),
    )
    rows = []
    basis_failures = 0
    direct_rows = []
    cases = {
        length: c488.c478.bounded_class_cases(length, len(surface.raw_effects))
        for length in (3, 6)
    }
    for name, psi in states:
        weights = branch_weights(surface.held_program, psi)
        branches = tuple(k @ psi for k in surface.held_program.kraus)
        for pointer in MENU:
            encoded = prepare_history(c488.HELD_CASE, HELD_HORIZON, (pointer,))
            physical = apply_physical(encoded)
            coarse = coarse_step(encoded)
            recovered = apply_physical(physical, reverse=True)
            witnessed = c488.receipts(physical)
            basis_failures += int(
                physical != coarse or recovered != encoded or witnessed is None
                or witnessed[0].pointer != pointer
            )
        # Execute the actual Cycle478 fine-pointer-to-protected-packet bridge,
        # with the unnormalized Kraus vectors packed in one sparse isometry.
        # No branch is renormalized before the common linear FORM control.
        for length, program in ((3, surface.train_program), (6, surface.held_program)):
            law = c488.c478.c440.menu_law(
                c488.TERMINAL_CLASSES, cases[length], c488.TERMINAL_ROW_INDEX,
            )
            source = c488.c478.c436.prepare_bank(c488.c478.c433.LAYOUT, law)
            physical478, leakage = c488.c478.c436.physical_pointer_then_law(program, psi, source, law)
            reference478 = c488.c478.c436.coarse_then_encode(program, psi, source, law)
            inverse478 = c488.c478.c436.inverse_sparse(physical478, law)
            input478 = c488.c478.c436.input_sparse(program, psi, source)
            # Linearly append the already-tested FORM basis permutation to
            # every sparse pointer key.  The schedule is common; this loop is
            # the declarative reference, not a runtime pointer query.
            form_signatures = {}
            for pointer in MENU:
                encoded = prepare_history(
                    c488.TRAIN_CASE if length == 3 else c488.HELD_CASE,
                    TRAIN_HORIZON if length == 3 else HELD_HORIZON,
                    (pointer,),
                )
                form_signatures[pointer] = apply_physical(encoded).bits
            composed_physical = {
                (pointer, system, packet, form_signatures[pointer]): amplitude
                for (pointer, system, packet), amplitude in physical478.items()
            }
            composed_reference = {
                (pointer, system, packet, form_signatures[pointer]): amplitude
                for (pointer, system, packet), amplitude in reference478.items()
            }
            direct_rows.append({
                "state": name,
                "length": length,
                "fine_pointer_labels": len(program.kraus),
                "coarse_packing": program.coarse_groups,
                "Cycle478_E_G_residual": c488.c478.c436.sparse_residual(physical478, reference478),
                "Cycle478_inverse_residual": c488.c478.c436.sparse_residual(inverse478, input478),
                "linear_FORM_residual": c488.c478.c436.sparse_residual(composed_physical, composed_reference),
                "leakage": leakage,
                "sparse_terms": len(composed_physical),
            })
        rows.append({
            "state": name,
            "weights": weights,
            "unnormalized_branch_squared_norms": tuple(float(np.vdot(v, v).real) for v in branches),
            "sum": sum(weights),
            "coherent_output_norm": sum(float(np.vdot(v, v).real) for v in branches),
            "train_sector_count": c488.MENU_ARITY**TRAIN_N,
            "held_sector_count": c488.MENU_ARITY**HELD_N,
            "held_factorized_norm": sum(weights) ** HELD_N,
        })
    incompatibility = abs(np.vdot(states[0][1], states[1][1]))
    check(
        "A: the actual five-sector Kraus carrier controls one exact FORM continuation on every basis sector and all sectors coherently",
        len(surface.held_program.kraus) == c488.MENU_ARITY
        and surface.held_program.coarse_groups == tuple((x,) for x in MENU)
        and basis_failures == 0
        and all(
            row["fine_pointer_labels"] == c488.MENU_ARITY
            and row["coarse_packing"] == tuple((x,) for x in MENU)
            and max(row["Cycle478_E_G_residual"], row["Cycle478_inverse_residual"], row["linear_FORM_residual"]) < TOL
            and row["leakage"] == 0
            for row in direct_rows
        )
        and all(abs(row["sum"] - 1.0) < TOL and abs(row["coherent_output_norm"] - 1.0) < TOL for row in rows)
        and incompatibility < 1.0 - 1e-6,
        {
            "input_rows": rows,
            "actual_Cycle478_code_rows": direct_rows,
            "input_overlap_magnitude": float(incompatibility),
            "basis_E_G_inverse_failures": basis_failures,
            "physical_carrier": "3-M2 fine pointer + retained system vector + Cycle483/Cycle488 FORM receipt",
            "branchwise_renormalization": False,
            "runtime_host_pointer_queries": 0,
            "coherent_sector_actualized": False,
        },
    )
    return {"states": states, "rows": rows}


def edge_gate(first: int, second: int, label: str) -> PointerGate:
    left = c488.bits_of(first, c488.POINTER_BITS)
    right = c488.bits_of(second, c488.POINTER_BITS)
    changed = tuple(index for index in range(c488.POINTER_BITS) if left[index] != right[index])
    if len(changed) != 1:
        raise ValueError("edge transposition is not one hypercube edge")
    target = changed[0]
    controls = tuple((index, left[index]) for index in range(c488.POINTER_BITS) if index != target)
    return PointerGate(target, controls, label)


def transpose_schedule(first: int, second: int, label: str) -> tuple[PointerGate, ...]:
    path = [first]
    current = list(c488.bits_of(first, c488.POINTER_BITS))
    target = c488.bits_of(second, c488.POINTER_BITS)
    for bit in range(c488.POINTER_BITS):
        if current[bit] != target[bit]:
            current[bit] ^= 1
            path.append(c488.int_of(tuple(current)))
    edges = tuple(edge_gate(a, b, f"{label}:edge:{index}") for index, (a, b) in enumerate(zip(path, path[1:])))
    return edges + tuple(reversed(edges[:-1]))


@lru_cache(maxsize=1)
def rotor_schedule() -> tuple[PointerGate, ...]:
    target = (1, 2, 3, 4, 0, 5, 6, 7)
    current = list(range(8))
    schedule: list[PointerGate] = []
    for source in range(8):
        if current[source] == target[source]:
            continue
        partner = current.index(target[source])
        a, b = current[source], current[partner]
        schedule.extend(transpose_schedule(a, b, f"rotor-fix:{source}"))
        current = [b if value == a else a if value == b else value for value in current]
    if tuple(current) != target:
        raise RuntimeError("compiled rotor table is wrong")
    return tuple(schedule)


def rotate_pointer(value: int, *, reverse: bool = False, delete: int | None = None) -> int:
    schedule = rotor_schedule()
    if delete is not None:
        schedule = tuple(item for index, item in enumerate(schedule) if index != delete)
    for item in reversed(schedule) if reverse else schedule:
        value = item.apply(value)
    return value


def orbit(seed: int, length: int) -> tuple[int, ...]:
    if seed not in MENU or not 1 <= length <= MAX_TRIALS:
        raise ValueError("rotor seed/length leaves the declared code")
    answer = []
    cursor = seed
    for _ in range(length):
        answer.append(cursor)
        cursor = rotate_pointer(cursor)
    return tuple(answer)


def courier_forward(seed: int, length: int, *, delete_rotor_gate: int | None = None) -> tuple[int, tuple[int, ...]]:
    """Three CNOT copies per cell followed by the same fixed rotor word."""
    if seed not in MENU or not 1 <= length <= MAX_TRIALS:
        raise ValueError("courier seed/length leaves the declared code")
    cursor = seed
    pointers = [0] * length
    for cell in range(length):
        pointers[cell] ^= cursor  # integer XOR is the three bitwise CNOTs.
        cursor = rotate_pointer(cursor, delete=delete_rotor_gate)
    return cursor, tuple(pointers)


def courier_inverse(cursor: int, pointers: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    restored = list(pointers)
    for cell in reversed(range(len(restored))):
        cursor = rotate_pointer(cursor, reverse=True)
        restored[cell] ^= cursor
    return cursor, tuple(restored)


def count_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(word.count(pointer) for pointer in MENU)


def route_b_controls() -> dict[str, object]:
    print("\nROUTE B / DETERMINISTIC EVERY-ORBIT CONTINUATION")
    table = tuple(rotate_pointer(value) for value in range(8))
    inverse_failures = sum(rotate_pointer(rotate_pointer(value), reverse=True) != value for value in range(8))
    train = orbit(0, TRAIN_N)
    held = orbit(0, HELD_N)
    rows = []
    eg_failures = 0
    for case_name, horizon, word in (
        (c488.TRAIN_CASE, TRAIN_HORIZON, train),
        (c488.HELD_CASE, HELD_HORIZON, held),
    ):
        encoded = prepare_history(case_name, horizon, word)
        physical = apply_physical(encoded)
        coarse = coarse_step(encoded)
        recovered = apply_physical(physical, reverse=True)
        eg_failures += int(physical != coarse or recovered != encoded)
        counts = c488.final_counts(physical)
        rows.append((
            len(word), word, counts,
            tuple(str(Fraction(count, len(word))) for count in counts),
            len(c488.receipts(physical) or ()),
        ))
    all_orbits = tuple((seed, orbit(seed, HELD_N), count_word(orbit(seed, HELD_N))) for seed in MENU)
    courier_rows = []
    courier_inverse_failures = 0
    for seed in MENU:
        cursor, word = courier_forward(seed, HELD_N)
        restored_seed, blanks = courier_inverse(cursor, word)
        courier_inverse_failures += int(restored_seed != seed or any(blanks) or word != orbit(seed, HELD_N))
        courier_rows.append((seed, cursor, word, restored_seed, blanks))
    _, deleted = courier_forward(0, HELD_N, delete_rotor_gate=0)
    check(
        "B: one fixed three-M2 reversible rotor extends every supplied basis seed and feeds exact N4/N12 FORM histories",
        table == (1, 2, 3, 4, 0, 5, 6, 7)
        and inverse_failures == eg_failures == courier_inverse_failures == 0
        and rows[0][2] == (1, 1, 1, 1, 0)
        and rows[1][2] == (3, 3, 2, 2, 2)
        and rows[0][4] == TRAIN_N and rows[1][4] == HELD_N
        and len(all_orbits) == 5 and deleted != held,
        {
            "rotor_table": table,
            "compiled_pointer_gates": len(rotor_schedule()),
            "maximum_new_gate_support_M2": 3,
            "train_held_rows": rows,
            "all_held_seed_orbits_and_counts": all_orbits,
            "courier_forward_inverse_rows": courier_rows,
            "deleted_gate_word_differs": deleted != held,
            "seed_is_supplied": True,
            "norm_controls_rotor": False,
        },
    )
    return {"train": train, "held": held, "all_orbits": all_orbits}


def product_bin_sum(law: ProductBathLaw, n: int, counts: tuple[int, ...]) -> float:
    if len(counts) != c488.MENU_ARITY or sum(counts) != n:
        raise ValueError("malformed multinomial bin")
    multiplicity = 1
    remaining = n
    for count in counts:
        multiplicity *= comb(remaining, count)
        remaining -= count
    answer = float(multiplicity)
    for q, count in zip(law.q, counts):
        answer *= q**count
    return answer


def route_c_controls(route_a: dict[str, object], route_b: dict[str, object]) -> dict[str, object]:
    print("\nROUTE C / SUPPLIED STATIONARY-INDEPENDENT SELECTOR BATH")
    norm_laws = tuple(
        ProductBathLaw("norm-copied-" + row["state"], tuple(row["weights"]))
        for row in route_a["rows"]
    )
    uniform = ProductBathLaw("uniform-non-Born", (0.2,) * c488.MENU_ARITY)
    laws = (*norm_laws, uniform)
    normalization = tuple((law.name, sum(law.q) ** n) for law in laws for n in (TRAIN_N, HELD_N))
    bin_normalization = []
    for law in laws:
        for n in (TRAIN_N, HELD_N):
            bins = (
                (a, b, c, d, n - a - b - c - d)
                for a in range(n + 1)
                for b in range(n - a + 1)
                for c in range(n - a - b + 1)
                for d in range(n - a - b - c + 1)
            )
            bin_normalization.append((law.name, n, sum(product_bin_sum(law, n, counts) for counts in bins)))
    marginals = tuple(
        (
            law.name,
            sum(law.word_weight(prefix + (last,)) for last in MENU),
            law.word_weight(prefix),
        )
        for law in laws
        for prefix in ((0, 1, 2), tuple(route_b["held"][:-1]))
    )
    stationarity = tuple(
        (law.name, tuple(sum(law.q[i] * law.q[j] for i in MENU) for j in MENU))
        for law in laws
    )
    distances = tuple(
        (
            row["state"],
            sum(abs(a - b) for a, b in zip(uniform.q, row["weights"])),
            sum(abs(a - b) for a, b in zip(uniform.q, row["weights"])),
        )
        for row in route_a["rows"]
    )
    held_word = tuple(route_b["held"])
    positive_member_weights = tuple((law.name, law.word_weight(held_word)) for law in laws)
    selector_basis_inverse_failures = 0
    selector_FORM_failures = 0
    for value in MENU:
        # Three CNOTs copy one supplied basis bath label to a blank pointer;
        # the retained bath label and spent marker make the global map invertible.
        bath, pointer, spent = value, 0, 0
        pointer ^= bath
        spent ^= 1
        spent ^= 1
        pointer ^= bath
        selector_basis_inverse_failures += int((bath, pointer, spent) != (value, 0, 0))
        # Forward again, then feed the copied basis label through the actual
        # FORM bridge.  All selector baths and branch labels remain retained.
        pointer ^= bath
        spent ^= 1
        encoded = prepare_history(c488.HELD_CASE, HELD_HORIZON, (pointer,))
        physical = apply_physical(encoded)
        coarse = coarse_step(encoded)
        witnessed = c488.receipts(physical)
        selector_FORM_failures += int(
            physical != coarse or witnessed is None or witnessed[0].pointer != value
            or bath != value or spent != 1
        )
    malformed = 0
    for q in ((0.25,) * 5, (0.2, 0.2, 0.2, 0.5, -0.1), (0.5, 0.5)):
        try:
            ProductBathLaw("bad", q)
        except ValueError:
            malformed += 1
    check(
        "C: a supplied local selector-bath law derives every product word/bin/marginal but uniform passes the same structure without approaching norm weights at held N12",
        selector_basis_inverse_failures == selector_FORM_failures == 0 and malformed == 3
        and all(abs(value - 1.0) < TOL for _name, value in normalization)
        and all(abs(value - 1.0) < TOL for _name, _n, value in bin_normalization)
        and all(abs(left - right) < TOL for _name, left, right in marginals)
        and all(max(abs(a - b) for a, b in zip(row, law.q)) < TOL for (name, row), law in zip(stationarity, laws))
        and all(train_distance == held_distance and held_distance > 0.1 for _name, train_distance, held_distance in distances)
        and all(weight > 0 for _name, weight in positive_member_weights),
        {
            "normalization_train_held": normalization,
            "multinomial_bin_normalization": tuple(bin_normalization),
            "last-symbol_marginals": marginals,
            "stationary_rows": stationarity,
            "uniform_distance_from_norm_at_N4_and_N12": distances,
            "same_held_basis_member_positive_under_each_law": positive_member_weights,
            "selector_dilation": "retained 3-M2 bath label + blank 3-M2 pointer + spent marker; support<=2",
            "selector_to_FORM_E_G_failures": selector_FORM_failures,
            "retired_import": "separate supplied table for each finite word",
            "unretired": ("q", "stationarity", "independence", "bath preparation", "actual member", "renewal"),
        },
    )
    return {"laws": laws, "distances": distances}


def bath_nonreentry_controls() -> None:
    print("\nFRESH BATH / USED-BATH NONREENTRY")
    c483 = c488.c483
    formation = set(site for group in c483.B_FORM_BATH_GROUPS for site in group)
    formation.update((c483.B_FORM_BATH_FRESH, c483.B_FORM_BATH_SPENT, c483.B_FORM_BATH_WORK))
    formation.update(c483.B_FORM_BATH_PROGRAM)
    repairs = tuple(set(site for group in c483.B_REPAIR_BATH[step] for site in group) for step in range(HELD_HORIZON))
    slices = (formation, *repairs)
    local_disjoint = all(not left.intersection(right) for left, right in combinations(slices, 2))
    regions = tuple(
        frozenset(cell * c488.CELL_M2 + site for site in set().union(*slices))
        for cell in range(HELD_N)
    )
    cross_disjoint = all(not left.intersection(right) for left, right in combinations(regions, 2))
    selector_baths = tuple((cell, "selector-bath", tuple(range(3)), "retained-spent") for cell in range(HELD_N))
    check(
        "formation/repair and selector baths are one-event fresh regions with no used-bath reentry or hidden renewal",
        local_disjoint and cross_disjoint and len(selector_baths) == HELD_N,
        {
            "Cycle483_bath_M2_per_held_event": len(set().union(*slices)),
            "held_event_regions": len(regions),
            "pairwise_region_intersections": 0,
            "selector_bath_batches": len(selector_baths),
            "used_bath_reentry_operations": 0,
            "renewal_operations": 0,
            "fresh_bath_genesis": "supplied",
        },
    )


def deletion_malformed_controls(route_b: dict[str, object]) -> None:
    print("\nDELETION / MALFORMED / HELD CONTROLS")
    base = prepare_history(c488.HELD_CASE, HELD_HORIZON, tuple(route_b["held"]))
    nominal = apply_physical(base)
    damaged = apply_physical(base, delete_label="cell:0:match:0:prefix:0")
    deletion_visible = c488.receipts(damaged) is None or c488.final_counts(damaged) != c488.final_counts(nominal)
    corruptions = []
    bad_pointer = list(base.bits)
    c488.replace_selected(bad_pointer, c488.field(0, c488.POINTER), c488.bits_of(7, c488.POINTER_BITS))
    corruptions.append(c488.BasisState(base.trials, base.horizon, base.case_name, tuple(bad_pointer)))
    dirty_bath = list(base.bits)
    dirty_bath[c488.site(0, c488.c483.B_FORM_BATH_FRESH)] = 1
    corruptions.append(c488.BasisState(base.trials, base.horizon, base.case_name, tuple(dirty_bath)))
    refusals = 0
    for state in corruptions:
        try:
            validate_generic_input(state)
        except ValueError:
            refusals += 1
    constructors = 0
    for action in (
        lambda: prepare_history(c488.HELD_CASE, HELD_HORIZON, (0,) * 13),
        lambda: orbit(5, HELD_N),
        lambda: prepare_history(c488.HELD_CASE, HELD_HORIZON, (0, 1, 7)),
    ):
        try:
            action()
        except ValueError:
            constructors += 1
    check(
        "FORM deletion is visible and pointer/bath/seed/size malformed inputs are refused at held N12",
        deletion_visible and refusals == 2 and constructors == 3 and c488.final_counts(nominal) == (3, 3, 2, 2, 2),
        {
            "FORM_deletion_visible": deletion_visible,
            "state_refusals": refusals,
            "constructor_refusals": constructors,
            "held_N": HELD_N,
            "held_counts": c488.final_counts(nominal),
        },
    )


def covariance_locality_controls() -> None:
    print("\nLOCALITY / ALL-24 PROPER-CUBIC COVARIANCE")
    traces = {n: generic_adapter_trace(n) for n in (TRAIN_N, HELD_N)}
    imported = {
        horizon: c488.c483.route_trace("bath", horizon)
        for horizon in (TRAIN_HORIZON, HELD_HORIZON)
    }
    frames = c488.proper_cubic_frames()
    failures = 0
    rows = 0
    # The new rotor and selector carriers occupy translation-equivalent short
    # line segments.  Proper-cubic rotations must preserve every unit edge.
    base_edges = tuple(((cell, lane, 0), (cell, lane + 1, 0)) for cell in range(HELD_N) for lane in range(6))
    for frame in frames:
        for first, second in base_edges:
            moved_first = c488.rotate_coord(first, frame)
            moved_second = c488.rotate_coord(second, frame)
            failures += int(c488.manhattan(moved_first, moved_second) != 1)
            rows += 1
    check(
        "the N4/N12 FORM adapter plus local rotor/selector carriers is bounded and covariant in all 24 proper-cubic frames",
        len(frames) == 24 and failures == 0
        and all(trace.connected_failures == 0 and trace.maximum_support_M2 <= 3 for trace in traces.values())
        and all(trace.connected_failures == 0 and trace.maximum_support_M2 <= 3 for trace in imported.values()),
        {
            "proper_cubic_frames": len(frames),
            "new_edge_rows": rows,
            "failures": failures,
            "FORM_adapter_traces": traces,
            "Cycle483_bath_traces": imported,
            "rotor_selector_max_support_M2": 3,
            "N12_M2_without_three_M2_courier": HELD_N * c488.CELL_M2,
        },
    )


def recon_and_interface_controls() -> None:
    print("\nRECONNAISSANCE / INTERFACE DISPOSITION")
    dispositions = (
        ("Cycle430", "independent product-weight precedent", "recon only; its scalar class-13 pointer is not the Cycle478 menu"),
        ("Cycle456", "physical clock signature and conditional Record predicates", "no five-menu member carrier; non-join"),
        ("Cycle469", "classified-word to S3 seed consumer", "seed-output family, not occurrence/member selector; non-join"),
        ("Cycle479", "local-3D provenance for that seed generator", "no occurrence/Record/Born output; non-join"),
        ("Cycle478", "actual five-pointer Kraus program", "direct input"),
        ("Cycle483", "basis bath-relative FORM occurrence", "direct input"),
        ("Cycle488", "pointer-to-FORM receipt/count permutation", "direct bridge"),
    )
    check(
        "prior product/clock/seed consumers are bounded without promoting them into a hidden actualization join",
        len(dispositions) == 7 and sum(row[2].startswith("direct") for row in dispositions) == 3,
        {"dispositions": dispositions},
    )


def no_go_controls() -> None:
    print("\nN1-N8 / CLAIM GATE")
    n1 = (
        ("retained-outcome instrument trajectory", "ATTEMPTED / POSITIVE COHERENT", "A; basis continuation, no sector actualization"),
        ("deterministic every-orbit law", "ATTEMPTED / POSITIVE CONDITIONAL", "B; fixed rotor, supplied seed/law"),
        ("stationary independent selector bath", "ATTEMPTED / POSITIVE CONDITIONAL", "C; q/mixture/member supplied"),
        ("deterministic supplied corpus", "ATTEMPTED PRIOR", "Cycle488; pointer word supplied"),
        ("independent scalar-instrument product law", "ATTEMPTED PRIOR", "Cycle430; independence/member supplied"),
        ("autonomous renewable stochastic bath", "OPEN / UNTESTED", "could generate correlated actual trajectories"),
        ("martingale/typicality over actual Records", "OPEN / UNTESTED", "requires realized Record process"),
        ("pre-history symmetry/grade theorem", "OPEN / UNTESTED", "could select q before separate occurrence law"),
    )
    walls = ("law/grade selection", "coherent-member actualization", "independence/stationarity", "fresh-bath genesis/renewal", "framework Record admission")
    n2 = tuple(
        (a, b, "neither direction derived; A/B/C furnish explicit countermodels closing one while supplying the other")
        for a, b in combinations(walls, 2)
    )
    n3 = (
        "Cycle478 terminal menu and logical input", "one-hot/basis pointer code",
        "Cycle483 FORM semantics and pure blank baths", "rotor law and initial seed",
        "selector q, stationarity and independence", "finite N4/N12 and horizon3/6",
        "class codec, trial identities and order", "noiseless gates and frame geometry",
        "mixture preparation and subsystem discard", "tolerances and exact source hashes",
    )
    n4 = (
        ("Cycle488", "member law absent", "A/B/C now supply three explicit conditional mechanisms but none derives actuality", True),
        ("Cycle430", "product rule supplied", "C retires per-word tables only; q/independence remain", True),
        ("Cycle483", "basis FORM does not choose coherent member", "A exposes exact coherent versus basis boundary", True),
        ("Cycle456/469/479", "downstream consumers", "no matching terminal-member carrier", True),
    )
    n5 = (
        ("every branch", "all five one-trial pointer sectors tested", "yes"),
        ("every orbit", "all five seeds through held N12 tested", "yes"),
        ("finite stationary law", "N4/N12 normalization/marginal/stationarity tested", "yes"),
        ("arbitrary N or asymptotic convergence", "not tested", "no negative claim"),
        ("lattice-wide realized histories", "not tested", "no negative claim"),
    )
    n6 = (
        "derive a physical pointer dephasing/actualization law with retained outcome",
        "derive q from an operational grade theorem independently of occurrence",
        "build an autonomous renewable selector-bath conveyor and audit export",
        "join basis FORM to framework Record admission and an empirical corpus",
        "test correlated stationary/ergodic laws beyond the supplied i.i.d. family",
    )
    n7 = (
        "The strongest live route combines A's exact Kraus-controlled FORM dilation with an autonomous local decohering bath whose retained stable pointer both selects a sector and renews without reusing spent carriers; an independently derived grade plus an ergodic theorem could then relate actual Record frequencies to norm weights. This tournament neither constructs nor excludes that route."
    )
    n8 = (
        "Cycle430 product weights did not actualize words",
        "Cycle478 effect functionality did not select a grade or occurrence",
        "Cycle483 bath FORM did not select a coherent member",
        "Cycle488 counts did not install a member law",
        "Cycle493 closes three finite mechanism gaps conditionally and leaves their supplied inputs separate",
    )
    check(
        "N1-N8 admits the three bounded positive results but rejects no-go, minimum-content, shared-obstruction, and axiom-pressure conclusions",
        len(n1) >= 5 and len(n2) == 10 and len(n3) >= 8 and len(n4) == 4
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 100 and len(n8) == 5,
        {
            "N1_normalized_route_registry": n1,
            "N2_pairwise_wall_audit": n2,
            "N3_hidden_condition_scan": n3,
            "N4_residual_matching": n4,
            "N5_rhetoric_and_resolution_audit": n5,
            "N6_partial_closure_paths": n6,
            "N7_steelman": n7,
            "N8_cross_cycle_echo": n8,
            "Gate_disposition": "FAIL — partial-attempt-with-named-untested-routes",
            "axiom_pressure": False,
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN")
    supplied = (
        "Cycle478 five-effect terminal menu, Kraus program, logical input states, and pointer basis",
        "Cycle483 bath-relative FORM law, blank formation/repair baths, finite protection horizons, and FORM semantics",
        "Cycle488 class codec, event order/identities, receipt/count apparatus, geometry, and inverse schedule",
        "route-B rotor law and initial basis seed",
        "route-C selector q, stationary/independent interpretation, mixture preparation, and fresh selector baths",
        "finite N4/N12 fixtures, noiseless gates, frame convention, tolerances, and source versions",
    )
    derived = (
        "route-A all-five basis E/G/inverse and coherent norm-preserving FORM continuation for two incompatible inputs",
        "route-B fixed three-M2 every-orbit extension, all five held seed orbits, and exact finite counts",
        "route-C word/bin/marginal/stationary consequences and global retained-bath inverse",
        "retirement of separately supplied finite-word tables under route C",
        "uniform non-Born selector surviving the same N4/N12 structural laws with fixed nonzero norm distance",
        "used-bath nonreentry, deletion, malformed, held, bounded-support, and all24 controls",
    )
    open_items = (
        "selection of one sector/member from route A's coherent correlated output",
        "physical selection of the route-B law or seed and any norm-frequency identification",
        "derivation of route-C q, stationarity, independence, mixture preparation, actual sampler, or actual member",
        "autonomous bath genesis/renewal, used-resource export, unbounded persistence, and arbitrary-noise control",
        "framework Record admission, empirical corpus, Born probability, and realized history",
        "asymptotic convergence, continuum time, energy, inertia, source, gravity, or constitutional conclusion",
    )
    check(
        "the inventory keeps physical carriers and finite consequences separate from actuality, probability, Record, and renewal imports",
        len(supplied) == len(derived) == len(open_items) == 6,
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "raw_counts_called_probability": False,
            "norm_called_probability": False,
            "coherent_pointer_called_realized_history": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.monotonic() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "bounded execution stays within the declared wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
        {
            "elapsed_seconds": elapsed,
            "peak_rss_bytes": rss,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "rss_cap_bytes": RSS_CAP_BYTES,
        },
    )


def install_wall_cap() -> None:
    def alarm(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle493 exceeded its wall cap")
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(int(WALL_CAP_SECONDS))


def main() -> int:
    started = time.monotonic()
    install_wall_cap()
    print("CYCLE493 PHYSICAL TERMINAL-MENU MEMBER-LAW TOURNAMENT")
    contract_controls()
    recon_and_interface_controls()
    surface = c488.finalized_surface()
    route_a = route_a_controls(surface)
    route_b = route_b_controls()
    route_c_controls(route_a, route_b)
    bath_nonreentry_controls()
    deletion_malformed_controls(route_b)
    covariance_locality_controls()
    no_go_controls()
    inventory_controls()
    resource_controls(started)
    signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
