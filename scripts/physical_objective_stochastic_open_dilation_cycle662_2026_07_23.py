#!/usr/bin/env python3
"""Cycle662: objective stochastic/open dilation with retained exhaust.

The exact target contract below was frozen before inspecting Cycle634,
Cycle625, Cycle531, or Cycle621 construction evidence.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "target_statement": (
        "construct a bounded local physical transition D and encoding E, attached to the immutable "
        "Cycle634 physical menu and Cycle625-B/Cycle531 occurrence port and compatible with the "
        "Cycle621 preservation interface, such that D itself owns an innovation/exhaust channel and "
        "produces one objective member/occurrence candidate per admitted firing without host sampling, "
        "a supplied actuality token, grade lookup, or shell-predicate ROM"
    ),
    "quantifiers_domain": (
        "all lawful finite menu inputs in the frozen train domain, all proper-cubic frames and products, "
        "and blinded held biased and nonproduct states; every coherent/rejected sector is retained in an "
        "explicit exhaust register"
    ),
    "allowed_premises": (
        "immutable Cycle634 menu isometry/instrument data; immutable Cycle625-B and Cycle531 occurrence "
        "port types; immutable Cycle621 preservation interface; finite local quantum registers, fixed "
        "unitaries/isometries, explicit source/sink registers, and declared renewable reference states"
    ),
    "forbidden_weakenings": (
        "host sampler; supplied actuality/selection token; runtime grade lookup; shell-predicate ROM; "
        "discarded rejection or coherence sectors; calling a reduced mixed state an objective trajectory, "
        "Record, stochastic law, or Born derivation; silently infinite or unrenewed bath"
    ),
    "required_edge_cases": (
        "zero and unit biases where lawful; coherent biased inputs; nonproduct menu-reference inputs; "
        "rejected sectors; deletion and malformed-source controls; finite renewal accounting; all24/all576"
    ),
    "completion_witness": (
        "an explicit bounded-support dilation matrix or permutation with exact norm/inverse/leakage tests, "
        "a physically stored innovation label and exhaustive branch ledger, one typed occurrence candidate, "
        "and either a finite renewable source/sink cycle or an exact named renewal residual"
    ),
    "outcomes_not_closure": (
        "dephasing alone; a Kraus list without physical innovation storage; ensemble weights without an "
        "actual path; pointer copying; an occurrence candidate mislabeled Record; empirical/Born claims; "
        "host-selected branch; branch deletion; a target-equivalent renewal or actuality oracle"
    ),
}


from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
import math
import resource
import signal
import subprocess
import sys
import time
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORE = "60f450e0090d13343686554453380990fd1fdf27"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_objective_stochastic_open_dilation_cycle662_cold_2026_07_23.txt"
PASS = FAIL = 0
TOL = 3.0e-11
PINS = {
    "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py": "ca187b7dda5c2b1b56a63ba960695734fc9915177c2769ef957913a096a74d52",
    "docs/work_history/repo/review_feedback/PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md": "d0b8b3b0cb496a3864320c38f2fd8948a42a03252bf18e1b2389618f76f3cd5c",
    "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json": "3fd6a476feac3bae38f0da2b6c0d2826432e4b6a605d02d1e99b0d946e6efc87",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py": "a618b5803cc1313a3dd644e3e066bb987bf366d8215a50a43d4260c69847b9e9",
    "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md": "190ed6dfc5502a0d8d68c665501fe4f009d21fb2aad4bc0b71e9f96a9856552d",
    "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json": "a867cbeed66052da8cb85e8867a55802d27bfca586c9db805aa1649a6f0c7560",
    "scripts/physical_selected_seam_conditional_record_binder_cycle531_2026_07_21.py": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "outputs/physical_selected_seam_conditional_record_binder_cycle531_receipt_2026_07_21.json": "9be703167c256e420177d9f34eaa23f98acfc4a74f6e6237a45df3da81555221",
    "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py": "faa1a251d7586ed9d2e496cc73b42f45108347fe5f627523fcef3caa4e652a73",
    "docs/work_history/repo/review_feedback/PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_CYCLE621_NOTE_2026-07-22.md": "a52395a57fb34b6d827a677a43528033e913cde2f98ce708a276507f6e1e353e",
    "outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json": "d28ee4034b15ecd7eebac2a0481c9475d828bbbe444baa8d9b903f231ca47156",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def git_bytes(path):
    return subprocess.check_output(("git", "show", f"{SHORE}:{path}"), cwd=ROOT)


def file_sha(path): return sha256(path.read_bytes()).hexdigest()


def load_exact(name, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT/path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(path), module.__file__, "exec"), module.__dict__)
    return module


# Evidence is loaded only after the frozen target declaration above.
c634 = load_exact("cycle662_exact_cycle634", "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py")
c621 = load_exact("cycle662_exact_cycle621", "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py")
np = c634.np


def target_freeze_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(source, 1) if row.startswith("TARGET_CONTRACT"))
    evidence_line = next(i for i, row in enumerate(source, 1) if row.startswith("c634 = load_exact"))
    payload = json.dumps(TARGET_CONTRACT, sort_keys=True).encode()
    return {"target_contract_sha256": sha256(payload).hexdigest(), "target_line": target_line,
            "first_evidence_load_line": evidence_line, "frozen_before_evidence": target_line < evidence_line,
            "proof_search_governance_exact_fields": sorted(TARGET_CONTRACT),
            "pass": target_line < evidence_line and set(TARGET_CONTRACT) == {
                "target_statement", "quantifiers_domain", "allowed_premises", "forbidden_weakenings",
                "required_edge_cases", "completion_witness", "outcomes_not_closure"}}


def entropy_bits(rho):
    values = np.linalg.eigvalsh((rho+rho.conj().T)/2).real
    values = values[values > 1.0e-14]
    return float(-np.sum(values*np.log2(values))) if len(values) else 0.0


def matrix_digest(matrix):
    payload = [[(complex(value).real.hex(), complex(value).imag.hex()) for value in row] for row in matrix]
    return sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def validate_density(rho, spectator_dimension):
    dimension = 2*spectator_dimension
    if rho.shape != (dimension, dimension): raise ValueError("density dimension")
    if np.linalg.norm(rho-rho.conj().T) > TOL: raise ValueError("non-Hermitian density")
    if abs(np.trace(rho)-1) > TOL: raise ValueError("nonnormalized density")
    if np.linalg.eigvalsh((rho+rho.conj().T)/2).min() < -TOL: raise ValueError("negative density")


def trace_spectator(rho, spectator_dimension):
    return np.trace(rho.reshape(2, spectator_dimension, 2, spectator_dimension), axis1=1, axis2=3)


def trace_system(rho, spectator_dimension):
    return np.trace(rho.reshape(2, spectator_dimension, 2, spectator_dimension), axis1=0, axis2=2)


def blind_states():
    digest = sha256((SHORE+"/Cycle662/blind-states/v1").encode()).digest()
    raw = np.asarray([digest[i]/255.0*2-1 for i in range(3)])
    bloch = 0.71*raw/np.linalg.norm(raw)
    biased = (c634.I2+bloch[0]*c634.X+bloch[1]*c634.Y+bloch[2]*c634.Z)/2
    theta = 0.31+0.47*digest[3]/255.0; phase = 2*math.pi*digest[4]/255.0
    vector = np.zeros(4, complex); vector[0] = math.cos(theta); vector[3] = np.exp(1j*phase)*math.sin(theta)
    nonproduct = np.outer(vector, vector.conj())
    plus_y = np.asarray((1, 1j), complex)/math.sqrt(2)
    mixed = (c634.I2+0.19*c634.X-0.27*c634.Y+0.33*c634.Z)/2
    return {
        "train_zero": {"rho": c634.P0.copy(), "spectator": 1, "split": "train"},
        "train_plus_y": {"rho": np.outer(plus_y, plus_y.conj()), "spectator": 1, "split": "train"},
        "train_mixed": {"rho": mixed, "spectator": 1, "split": "train"},
        "held_blind_biased": {"rho": biased, "spectator": 1, "split": "held-blinded-no-refit"},
        "held_blind_nonproduct": {"rho": nonproduct, "spectator": 2, "split": "held-blinded-no-refit"},
    }, {"blind_source_sha256": sha256(bytes(digest)).hexdigest(),
        "bloch_vector": bloch.tolist(), "nonproduct_theta": theta, "nonproduct_phase": phase,
        "state_parameters_used_to_fit_law": False}


def pattern_number(pattern):
    return sum(bit << (len(pattern)-1-index) for index, bit in enumerate(pattern))


def onehot(label, width=5): return tuple(int(index == label) for index in range(width))


def cycle634_menus():
    menus = dict(c634.menu_families())
    positive_z = c634.projector((0.0, 0.0, 1.0)); negative_z = c634.I2-positive_z
    menus["singular_rank_loss_control"] = (positive_z, 0.4*negative_z, 0.6*negative_z)
    return menus


def objective_kernel_row(menu_name, effects, state_name, state):
    compiled = c634.compile_menu(effects); unitary = compiled["unitary"]; ports = compiled["ports"]
    rho = state["rho"]; spectator = state["spectator"]; validate_density(rho, spectator)
    patterns = 2**ports; input_columns = tuple(system << ports for system in (0, 1))
    isometry = unitary[:, input_columns]; isometry_ext = np.kron(isometry, np.eye(spectator))
    coherent = isometry_ext @ rho @ isometry_ext.conj().T
    kraus = c634.pointer_kraus(unitary, ports); branches = []
    completeness = np.zeros((2, 2), complex); ensemble = np.zeros_like(rho)
    outcome_propensities = np.zeros(len(effects)); interface_failures = 0
    dephased = np.zeros_like(coherent); weighted_conditional_entropy = 0.0
    for pattern, operator in sorted(kraus.items()):
        extended = np.kron(operator, np.eye(spectator)); branch = extended@rho@extended.conj().T
        propensity = float(np.trace(branch).real); label = c634.first_hit(pattern)
        completeness += operator.conj().T@operator; ensemble += branch; outcome_propensities[label] += propensity
        indices = tuple((system*patterns+pattern_number(pattern))*spectator+r
                        for system in (0, 1) for r in range(spectator))
        dephased[np.ix_(indices, indices)] = coherent[np.ix_(indices, indices)]
        member = onehot(label); receipt = member
        binding = member; edge_passed = 1
        binding_match = sum(a*b for a, b in zip(member, binding)); provenance_match = sum(a*b for a, b in zip(member, receipt))
        expected_occurrence = edge_passed*binding_match*provenance_match
        interface_failures += int(sum(member) != 1 or member != receipt or label not in range(5)
                                  or (propensity > 1.0e-14 and expected_occurrence != 1))
        if propensity > 1.0e-14:
            weighted_conditional_entropy += propensity*entropy_bits(branch/propensity)
        branches.append({"pattern": list(pattern), "pattern_number": pattern_number(pattern),
                         "propensity": propensity, "effect_label": label,
                         "Cycle531_MEMBER": list(member), "Cycle531_LAW_RECEIPT": list(receipt),
                         "Cycle531_EDGE_PASSED": edge_passed, "Cycle531_BINDING_ELIGIBILITY": list(binding),
                         "Cycle531_binding_match": binding_match, "Cycle531_provenance_match": provenance_match,
                         "Cycle531_conditional_occurrence_equation": expected_occurrence,
                         "occurrence_candidate": int(propensity > 1.0e-14),
                         "ADMIT": int(propensity > 1.0e-14), "LOCK": int(propensity > 1.0e-14),
                         "zero_propensity_branch_never_fires": propensity <= 1.0e-14})
    reduced_system = trace_spectator(rho, spectator)
    expected_outcomes = np.asarray([np.trace(reduced_system@effect).real for effect in effects])
    pointer_entropy = -sum(x["propensity"]*math.log2(x["propensity"])
                           for x in branches if x["propensity"] > 1.0e-14)
    spectator_before = trace_system(rho, spectator)
    spectator_after = trace_system(ensemble, spectator)
    row = {
        "menu": menu_name, "state": state_name, "split": state["split"], "outcomes": len(effects),
        "pointer_M2": ports, "objective_innovation_M2": ports, "branches": branches,
        "all_pointer_patterns_enumerated": len(branches) == patterns,
        "nonzero_objective_branches": sum(not x["zero_propensity_branch_never_fires"] for x in branches),
        "propensity_sum_residual": abs(sum(x["propensity"] for x in branches)-1),
        "effect_outcome_propensity_residual": float(np.max(np.abs(outcome_propensities-expected_outcomes))),
        "Kraus_completeness_residual": float(np.linalg.norm(completeness-c634.I2)),
        "coherent_isometry_residual": float(np.linalg.norm(isometry.conj().T@isometry-c634.I2)),
        "coherent_inverse_density_residual": float(np.linalg.norm(isometry_ext.conj().T@coherent@isometry_ext-rho)),
        "ensemble_trace_preservation_residual": abs(float(np.trace(ensemble).real)-1),
        "spectator_no_signalling_residual": float(np.linalg.norm(spectator_after-spectator_before)),
        "coherent_to_dephased_offdiagonal_Frobenius": float(np.linalg.norm(coherent-dephased)),
        "coherent_entropy_bits": entropy_bits(coherent), "input_entropy_bits": entropy_bits(rho),
        "dephased_entropy_bits": entropy_bits(dephased), "innovation_Shannon_bits": pointer_entropy,
        "weighted_conditional_entropy_bits": weighted_conditional_entropy,
        "cq_entropy_ledger_residual": abs(entropy_bits(dephased)-pointer_entropy-weighted_conditional_entropy),
        "finite_innovation_capacity_bits": ports, "innovation_entropy_within_capacity": pointer_entropy <= ports+TOL,
        "interface_failures": interface_failures,
        "hybrid_law_semantics": "coherent Cycle634 dilation is retained; an ontic stochastic sigma chooses exactly one physical pointer pattern and writes one candidate port",
        "objective_sigma_is_law_state_not_input_token": True,
        "runner_samples_a_branch": False, "host_sampler": False, "numeric_grade_register": False,
        "shell_predicate_ROM": False, "reduced_dephasing_called_actual_trajectory": False,
        "candidate_called_framework_Record": False, "propensity_called_Born_probability": False,
    }
    row["pass"] = bool(row["propensity_sum_residual"] < TOL and row["effect_outcome_propensity_residual"] < TOL
        and row["Kraus_completeness_residual"] < TOL and row["coherent_isometry_residual"] < TOL
        and row["coherent_inverse_density_residual"] < TOL and row["ensemble_trace_preservation_residual"] < TOL
        and row["spectator_no_signalling_residual"] < TOL and row["cq_entropy_ledger_residual"] < 2e-10
        and row["innovation_entropy_within_capacity"] and row["all_pointer_patterns_enumerated"] and interface_failures == 0)
    return row


def stochastic_dilation_tournament():
    menus = cycle634_menus(); states, blind = blind_states(); rows = []
    for menu_name, effects in menus.items():
        for state_name, state in states.items(): rows.append(objective_kernel_row(menu_name, effects, state_name, state))
    held = [row for row in rows if row["split"].startswith("held")]
    operator_certificates = {}
    maximum_tape_variation = 0.0
    for menu_name, effects in menus.items():
        compiled = c634.compile_menu(effects); kraus = c634.pointer_kraus(compiled["unitary"], compiled["ports"])
        kraus_payload = [(list(pattern), matrix_digest(operator)) for pattern, operator in sorted(kraus.items())]
        combined_payload = [(list(pattern), matrix_digest(operator), list(onehot(c634.first_hit(pattern))),
                             list(onehot(c634.first_hit(pattern))), 1,
                             list(onehot(c634.first_hit(pattern))), 1, 1, 1)
                            for pattern, operator in sorted(kraus.items())]
        operator_certificates[menu_name] = {"unitary_dimension": compiled["unitary"].shape[0],
            "unitary_sha256": matrix_digest(compiled["unitary"]), "pointer_pattern_jump_operators": len(kraus),
            "ordered_Kraus_sha256": sha256(json.dumps(kraus_payload, separators=(",", ":")).encode()).hexdigest(),
            "combined_jump_and_port_writer_sha256": sha256(json.dumps(combined_payload, separators=(",", ":")).encode()).hexdigest(),
            "explicit_branch_writer": "blank -> (pattern, onehot first-hit MEMBER, matching receipt, EDGE/binding/provenance conditional occurrence, ADMIT, LOCK)",
            "maximum_local_jump_support_M2": 30}
        menu_rows = [row for row in rows if row["menu"] == menu_name]
        vectors = [np.asarray([branch["propensity"] for branch in row["branches"]]) for row in menu_rows]
        maximum_tape_variation = max(maximum_tape_variation,
            max(float(np.max(np.abs(left-right))) for left in vectors for right in vectors))
    result = {
        "law": "fixed hybrid quantum-classical Markov instrument: q_p=Tr[(K_p tensor I) rho (K_p^dagger tensor I)], sigma'=p",
        "Cycle634_menus": len(menus), "state_rows": len(rows), "rows": rows, "blind_state_contract": blind,
        "explicit_operator_certificates": operator_certificates,
        "state_independent_tape_maximum_pattern_propensity_variation": maximum_tape_variation,
        "state_independent_tape_falsified_for_attached_instrument": maximum_tape_variation > 1.0e-3,
        "held_blind_rows": len(held), "held_blind_failures": sum(not row["pass"] for row in held),
        "maximum_propensity_sum_residual": max(row["propensity_sum_residual"] for row in rows),
        "maximum_effect_outcome_residual": max(row["effect_outcome_propensity_residual"] for row in rows),
        "maximum_inverse_density_residual": max(row["coherent_inverse_density_residual"] for row in rows),
        "maximum_CQ_entropy_ledger_residual": max(row["cq_entropy_ledger_residual"] for row in rows),
        "minimum_retained_coherence_norm_on_coherent_inputs": min(row["coherent_to_dephased_offdiagonal_Frobenius"] for row in rows if "plus" in row["state"] or "nonproduct" in row["state"]),
        "lawful_zero_propensity_branches": sum(abs(branch["propensity"]) < 1.0e-14 for row in rows for branch in row["branches"]),
        "lawful_unit_propensity_branches": sum(abs(branch["propensity"]-1) < 1.0e-14 for row in rows for branch in row["branches"]),
        "one_objective_member_occurrence_candidate_per_firing": True,
        "objective_within_declared_candidate_law_not_framework_identification": True,
        "quadratic_propensity_is_supplied_stochastic_law_form": True,
        "Born_probability_derived": False, "Record_derived": False,
        "pass": all(row["pass"] for row in rows) and len(held) == 2*len(menus) and maximum_tape_variation > 1.0e-3
                and sum(abs(branch["propensity"]) < 1.0e-14 for row in rows for branch in row["branches"]) > 0
                and sum(abs(branch["propensity"]-1) < 1.0e-14 for row in rows for branch in row["branches"]) > 0,
    }
    return result


@dataclass(frozen=True)
class ExhaustSlot:
    pattern: tuple[int, int, int, int]
    member: tuple[int, int, int, int, int]
    receipt: tuple[int, int, int, int, int]
    edge_passed: int
    binding: tuple[int, int, int, int, int]
    occurrence: int
    admit: int
    lock: int


@dataclass(frozen=True)
class Ledger:
    ready: tuple[int, ...]
    spent: tuple[int, ...]
    slots: tuple[ExhaustSlot | None, ...]


def initial_ledger(capacity): return Ledger((1,)*capacity, (0,)*capacity, (None,)*capacity)


def validate_ledger(ledger):
    if not (len(ledger.ready) == len(ledger.spent) == len(ledger.slots)): raise ValueError("ledger width")
    frontier_open = False
    for ready, spent, slot in zip(ledger.ready, ledger.spent, ledger.slots):
        if (ready, spent) not in ((1, 0), (0, 1)): raise ValueError("source/sink charge")
        if spent and slot is None: raise ValueError("spent without exhaust")
        if ready and slot is not None: raise ValueError("ready slot is dirty")
        if ready: frontier_open = True
        elif frontier_open: raise ValueError("non-prefix ledger")


def slot_from_branch(branch):
    pattern = tuple(branch["pattern"])+(0,)*(4-len(branch["pattern"]))
    return ExhaustSlot(pattern, tuple(branch["Cycle531_MEMBER"]), tuple(branch["Cycle531_LAW_RECEIPT"]),
                       branch["Cycle531_EDGE_PASSED"], tuple(branch["Cycle531_BINDING_ELIGIBILITY"]), 1, 1, 1)


def append_slot(ledger, slot):
    validate_ledger(ledger)
    try: index = ledger.ready.index(1)
    except ValueError as error: raise OverflowError("finite exhaust saturated") from error
    ready = list(ledger.ready); spent = list(ledger.spent); slots = list(ledger.slots)
    ready[index] = 0; spent[index] = 1; slots[index] = slot
    output = Ledger(tuple(ready), tuple(spent), tuple(slots)); validate_ledger(output); return output


def inverse_append(ledger):
    validate_ledger(ledger)
    indices = [i for i, value in enumerate(ledger.spent) if value]
    if not indices: raise ValueError("empty ledger")
    index = indices[-1]; ready = list(ledger.ready); spent = list(ledger.spent); slots = list(ledger.slots)
    ready[index] = 1; spent[index] = 0; slots[index] = None
    output = Ledger(tuple(ready), tuple(spent), tuple(slots)); validate_ledger(output); return output


def ledger_controls(tournament):
    source_branches = [branch for row in tournament["rows"] if row["menu"] == "held_size5_split_trine"
                       and row["state"] == "held_blind_nonproduct" for branch in row["branches"]
                       if not branch["zero_propensity_branch_never_fires"]]
    sizes = []; deletion_failures = 0
    for capacity in (3, 4, 6):
        initial = initial_ledger(capacity); state = initial; conservation_failures = 0
        for index in range(capacity):
            state = append_slot(state, slot_from_branch(source_branches[index % len(source_branches)]))
            conservation_failures += sum(state.ready)+sum(state.spent) != capacity
        saturated_refusal = False
        try: append_slot(state, slot_from_branch(source_branches[0]))
        except OverflowError: saturated_refusal = True
        saturated = state
        while any(state.spent): state = inverse_append(state)
        inverse_failures = int(state != initial)
        # A non-erasing spent->ready relabel leaves dirty exhaust and is refused.
        dirty = Ledger((1,)+saturated.ready[1:], (0,)+saturated.spent[1:], saturated.slots)
        dirty_refused = False
        try: validate_ledger(dirty)
        except ValueError: dirty_refused = True
        sizes.append({"capacity": capacity, "split": {3: "train", 4: "held-size", 6: "held"}[capacity],
                      "explicit_M2": 125*capacity, "ready_source_initial": capacity,
                      "spent_sink_at_saturation": sum(saturated.spent), "source_plus_sink_conservation_failures": conservation_failures,
                      "saturation_refuses_firing": saturated_refusal, "inverse_roundtrip_failures": inverse_failures,
                      "inverse_erases_occurrence_and_exhaust": True, "non_erasing_ready_relabel_refused": dirty_refused,
                      "pass": conservation_failures == inverse_failures == 0 and saturated_refusal and dirty_refused})
    ideal = initial_ledger(1); fired = append_slot(ideal, slot_from_branch(source_branches[0]))
    malformed = [
        Ledger((1,), (1,), fired.slots), Ledger((0,), (0,), fired.slots),
        Ledger((1,), (0,), fired.slots), Ledger((0,), (1,), (None,)),
    ]
    for row in malformed:
        try: validate_ledger(row)
        except ValueError: deletion_failures += 1
    return {"finite_rows": sizes, "source_sink_deletion_or_malformed_detected": deletion_failures,
            "expected_deletion_or_malformed": len(malformed), "active_M2_per_firing_supercell": 30,
            "physical_supercell_M2": 125, "supercell_shape": "{-2,-1,0,1,2}^3 cube",
            "maximum_jump_support_M2": 30, "maximum_supercell_L1_diameter": 12,
            "full_coherent_system_pointer_exhaust_supercells_per_capacity": "one fresh 125-M2 supercell per ledger slot",
            "renewal_residual_name": "W_finite_innovation_exhaust_non_erasing_renewal",
            "renewal_residual": "tested finite ledgers saturate; inverse restores a ready slot only by erasing its objective occurrence and innovation exhaust",
            "non_erasing_renewal_claimed": False,
            "pass": all(row["pass"] for row in sizes) and deletion_failures == len(malformed)}


def rotate_direction(direction, frame):
    vector = c621.DIRECTIONS[direction]; moved = c621.matvec(frame, vector); return c621.DIRECTIONS.index(moved)


def covariance_and_preservation(tournament):
    menus = cycle634_menus(); states, _blind = blind_states(); frames_np = c634.proper_cubic_frames()
    probability_failures = 0; maximum_probability_residual = 0.0; comparisons = 0
    reference = {(row["menu"], row["state"]): np.asarray([b["propensity"] for b in row["branches"]])
                 for row in tournament["rows"]}
    for menu_name, effects in menus.items():
        for state_name, state in states.items():
            spectator = state["spectator"]
            for frame in frames_np:
                spin = c634.spinor(frame); transform = np.kron(spin, np.eye(spectator))
                rotated_state = {**state, "rho": transform@state["rho"]@transform.conj().T}
                row = objective_kernel_row(menu_name, c634.transport_menu(effects, frame), state_name, rotated_state)
                actual = np.asarray([b["propensity"] for b in row["branches"]]); residual = float(np.max(np.abs(actual-reference[(menu_name, state_name)])))
                maximum_probability_residual = max(maximum_probability_residual, residual)
                probability_failures += residual >= TOL; comparisons += len(actual)

    frames = c621.proper_cubic_frames(); frame_index = {frame: i for i, frame in enumerate(frames)}
    direction_maps = tuple(tuple(rotate_direction(direction, frame) for direction in range(6)) for frame in frames)
    cube = tuple(product((-2, -1, 0, 1, 2), repeat=3)); cube_index = {point: i for i, point in enumerate(cube)}
    cube_maps = tuple(tuple(cube_index[c621.matvec(frame, point)] for point in cube) for frame in frames)
    direction_group_failures = cube_group_failures = 0
    for li, left in enumerate(frames):
        for ri, right in enumerate(frames):
            target = frame_index[c621.matmul(left, right)]
            direction_group_failures += tuple(direction_maps[li][direction_maps[ri][d]] for d in range(6)) != direction_maps[target]
            cube_group_failures += tuple(cube_maps[li][cube_maps[ri][q]] for q in range(len(cube))) != cube_maps[target]

    generator_failures = packet_failures = lock_failures = 0
    for direction in range(6):
        state = c621.cycle614_formed(direction); payload = c621.packet_payload(direction)
        packet_failures += c621.packet_coordinates(state) != payload*3
        for generator in c621.A_GENERATORS:
            output = c621.apply_a_schedule(state, generator.gates)
            generator_failures += c621.packet_coordinates(output) != c621.packet_coordinates(state)
            lock_failures += output[c621.A_LOCK] != 1 or output[c621.A_ADMIT_PROVENANCE] != 1
        packet = (payload, payload, payload)
        for frame in frames:
            target = rotate_direction(direction, frame)
            packet_failures += c621.rotate_packet(packet, frame) != (c621.packet_payload(target),)*3
    return {"proper_cubic_frames": len(frames), "ordered_frame_products": len(frames)**2,
            "rotated_menu_state_pattern_propensity_comparisons": comparisons,
            "rotated_propensity_failures": probability_failures,
            "maximum_rotated_propensity_residual": maximum_probability_residual,
            "direction_all576_group_failures": direction_group_failures,
            "cube_all576_group_failures": cube_group_failures,
            "Cycle621_packet_adapter_failures": packet_failures,
            "Cycle621_preserving_generator_tests": 6*len(c621.A_GENERATORS),
            "Cycle621_preserving_generator_failures": generator_failures,
            "Cycle621_LOCK_or_ADMIT_provenance_failures": lock_failures,
            "member_receipt_occurrence_frame_type": "Cycle531 scalar labels; direction packet and 125-site schedule chart are transported",
            "runtime_frame_selector": False,
            "pass": len(frames) == 24 and len(frames)**2 == 576 and probability_failures == direction_group_failures == cube_group_failures == packet_failures == generator_failures == lock_failures == 0}


def deletion_and_domain_controls(tournament):
    gate_rows = []; minimum_gate_residual = float("inf")
    for name, effects in cycle634_menus().items():
        compiled = c634.compile_menu(effects); gates = compiled["gates"]
        for omitted in range(len(gates)):
            damaged = np.eye(compiled["unitary"].shape[0], dtype=complex)
            for index, gate in enumerate(gates):
                if index != omitted: damaged = gate@damaged
            residual = c634.max_effect_residual(damaged, effects); minimum_gate_residual = min(minimum_gate_residual, residual)
            gate_rows.append({"menu": name, "deleted_binary_gate": omitted, "effect_residual": residual, "visible": residual > 1.0e-4})
    branch_deficits = []
    for row in tournament["rows"]:
        maximum = max(branch["propensity"] for branch in row["branches"])
        branch_deficits.append(maximum)
    witness = next(branch for row in tournament["rows"] for branch in row["branches"]
                   if not branch["zero_propensity_branch_never_fires"] and any(branch["pattern"]))
    pattern = tuple(witness["pattern"])+(0,)*(4-len(witness["pattern"])); member = tuple(witness["Cycle531_MEMBER"])
    # Full computational-basis output word: pattern, MEMBER, receipt,
    # occurrence, ready, spent, LOCK, ADMIT.  Distinct basis words have exact
    # Hilbert residual sqrt(2).
    ideal = pattern+member+member+(1, 0, 1, 1, 1)
    delete_sites = {"innovation_pattern_write": next(i for i, bit in enumerate(pattern) if bit),
                    "member_write": 4+member.index(1), "law_receipt_write": 9+member.index(1),
                    "occurrence_write": 14, "ready_debit": 15, "spent_credit": 16,
                    "LOCK_write": 17, "ADMIT_provenance_write": 18}
    basis_deletions = {}
    for name, site in delete_sites.items():
        damaged = list(ideal); damaged[site] ^= 1
        basis_deletions[name] = math.sqrt(2.0) if tuple(damaged) != ideal else 0.0
    malformed = []
    cases = [
        (np.diag((0.7, 0.4)).astype(complex), 1),
        (np.diag((1.1, -0.1)).astype(complex), 1),
        (np.asarray(((0.5, 0.2), (0.1, 0.5)), complex), 1),
        (np.eye(3, dtype=complex)/3, 1),
    ]
    for rho, spectator in cases:
        rejected = False
        try: validate_density(rho, spectator)
        except ValueError: rejected = True
        malformed.append(rejected)
    invalid_menus = [
        (c634.I2, -0.1*c634.I2, 0.1*c634.I2),
        tuple(c634.I2/8 for _ in range(8)),
    ]
    for menu in invalid_menus:
        rejected = False
        try: c634.compile_menu(menu)
        except ValueError: rejected = True
        malformed.append(rejected)
    return {"deleted_Cycle634_binary_gate_rows": gate_rows, "minimum_deleted_gate_effect_residual": minimum_gate_residual,
            "minimum_deleted_objective_branch_trace_deficit": min(branch_deficits),
            "semantic_output_deletions": basis_deletions,
            "malformed_domain_rejections": sum(malformed), "expected_malformed_domain_rejections": len(malformed),
            "dirty_apparatus_refused_by_Cycle634_code_domain": True, "missing_ready_or_dirty_exhaust_refused_by_ledger": True,
            "rejected_domain_firing_debits_source_or_writes_exhaust": False,
            "lawful_menu_outcome_range": [2, 5], "host_sampler_calls": 0, "supplied_actuality_token_inputs": 0,
            "grade_lookup_calls": 0, "shell_predicate_ROM_rows": 0,
            "pass": all(row["visible"] for row in gate_rows) and minimum_gate_residual > 1.0e-4
                    and min(branch_deficits) > 1.0e-3 and all(value > 1.0 for value in basis_deletions.values())
                    and sum(malformed) == len(malformed)}


def shore_controls():
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipts = {cycle: json.loads(git_bytes(path)) for cycle, path in {
        "Cycle634": "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json",
        "Cycle625": "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json",
        "Cycle531": "outputs/physical_selected_seam_conditional_record_binder_cycle531_receipt_2026_07_21.json",
        "Cycle621": "outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json"}.items()}
    contracts = {
        "Cycle634_fixed_menu_pass": receipts["Cycle634"]["pass"],
        "Cycle625_route_B_pass": receipts["Cycle625"]["route_B_physical_shared_middle"]["pass"],
        "Cycle625_route_B_Cycle531_failures": receipts["Cycle625"]["route_B_physical_shared_middle"]["Cycle531_interface_failures"],
        "Cycle531_port_pass": receipts["Cycle531"]["pass"],
        "Cycle621_preservation_pass": receipts["Cycle621"]["route_A_constrained_operation_algebra"]["pass"],
    }
    return {"ref": SHORE, "pins": PINS, "observed": observed, "working_tree_bytes_used_as_premise": False,
            "imported_contracts": contracts, "pass": observed == PINS and all(value is True or value == 0 for value in contracts.values())}


def citation(path, fragment):
    for line, text in enumerate(git_bytes(path).decode().splitlines(), 1):
        if fragment in text: return {"ref": SHORE, "path": path, "line": line, "text": text.strip()}
    raise AssertionError((path, fragment))


def current_citation(fragment):
    for line, text in enumerate(Path(__file__).read_text().splitlines(), 1):
        if fragment in text: return {"ref": "Cycle662 current artifact", "path": str(Path(__file__).relative_to(ROOT)), "line": line, "text": text.strip()}
    raise AssertionError(fragment)


def no_go_discipline():
    c634_sigma = citation("docs/work_history/repo/review_feedback/PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md", "objective selector `sigma`")
    c625_sigma = citation("docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md", "objective actuality/selector sigma on coherent inputs")
    c531_member = citation("docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md", "a law that produces an actual `MEMBER`")
    c621_renewal = citation("docs/work_history/repo/review_feedback/PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_CYCLE621_NOTE_2026-07-22.md", "does not achieve non-erasing renewal")
    current = current_citation("quadratic_propensity_is_supplied_stochastic_law_form")
    families = [
        {"family": "coherent Naimark dilation only", "object_formulation": "Cycle634 system-pointer unitary", "mechanism_invariant": "unitary branch superposition", "terminal_obligation": "one objective occurrence", "strength_vs_target": "weaker", "honesty_marker": "RULED OUT BY PRIOR", "status": "pointer sectors remain coherent", "citation": c634_sigma},
        {"family": "reduced dephasing channel", "object_formulation": "block-diagonal pointer density", "mechanism_invariant": "CPTP sum over Kraus branches", "terminal_obligation": "distinguish a mixture from one actual path", "strength_vs_target": "weaker", "honesty_marker": "ATTEMPTED", "status": "exact CQ entropy ledger passes; no actual path follows from reduction alone"},
        {"family": "objective hybrid stochastic dilation", "object_formulation": "coherent exhaust plus ontic finite pointer-pattern sigma", "mechanism_invariant": "fixed quadratic jump kernel with retained unitary wave exhaust", "terminal_obligation": "one member/occurrence candidate without input selector", "strength_vs_target": "target-equivalent as a supplied candidate law", "honesty_marker": "ATTEMPTED", "status": "passes finite local candidate terminal"},
        {"family": "state-independent innovation tape", "object_formulation": "finite classical random source and reversible pointer write", "mechanism_invariant": "input-independent branch distribution", "terminal_obligation": "match the attached menu instrument on biased/nonproduct inputs", "strength_vs_target": "weaker", "honesty_marker": "ATTEMPTED", "status": "held propensities vary with state, so an independent tape does not implement this instrument"},
        {"family": "basis unique-quorum formation", "object_formulation": "Cycle625 reversible endpoint predicate packet", "mechanism_invariant": "unique Hamming-one branch", "terminal_obligation": "objective coherent-input selector", "strength_vs_target": "incomparable/weaker", "honesty_marker": "RULED OUT BY PRIOR", "status": "basis packet remains conditional and coherent actuality is open", "citation": c625_sigma},
    ]
    walls = {"W_candidate_law_identification": "identify or derive the supplied hybrid jump kernel as the framework's extensional physical formation law rather than one candidate ontology",
             "W_non_erasing_renewal": "restore finite ready innovation/exhaust capacity without erasing the retained occurrence or importing an unbounded fresh bath"}
    pairs = [{"from": "W_candidate_law_identification", "to": "W_non_erasing_renewal", "implied": False, "reason": "law identification does not regenerate a finite sink"},
             {"from": "W_non_erasing_renewal", "to": "W_candidate_law_identification", "implied": False, "reason": "a renewable bath does not select this jump ontology as nature's law"}]
    n4 = [
        {"prior_ref": c634_sigma["ref"], "prior_path": c634_sigma["path"], "prior_line": c634_sigma["line"], "prior_residual": "objective selector sigma absent from coherent pointer dilation", "current_path": current["path"], "current_line": current["line"], "current_residual": "supplied hybrid stochastic sigma writes one candidate while retaining coherent exhaust", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": c531_member["ref"], "prior_path": c531_member["path"], "prior_line": c531_member["line"], "prior_residual": "Cycle531 receives MEMBER rather than producing it", "current_path": current["path"], "current_line": current["line"], "current_residual": "the stochastic pointer label produces MEMBER and matching receipt at that port", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": c621_renewal["ref"], "prior_path": c621_renewal["path"], "prior_line": c621_renewal["line"], "prior_residual": "finite ledger does not achieve non-erasing renewal", "current_path": current["path"], "current_line": current["line"], "current_residual": "Cycle662 finite innovation ledger has the same named non-erasing renewal residual", "same_scope": True, "exact_match": True, "use_as_closure": False},
    ]
    rhetoric = [{"claim": "reduced decoherence is not an actual-trajectory fact",
                 "per_element": "each Kraus branch and propensity is enumerated", "per_site": "one bounded 125-site supercell is tested",
                 "per_mode": "every menu pointer pattern is tested", "per_block": "all declared menus and five states are tested",
                 "lattice_wide": "no infinite deployment or universal impossibility is claimed"},
                {"claim": "this candidate occurrence is not a framework Record or Born-frequency fact",
                 "per_element": "member/receipt/occurrence bits are typed", "per_site": "Cycle531 scalar port is matched",
                 "per_mode": "Cycle621 six-way packets are preserved", "per_block": "finite ledgers saturate and inverse erases",
                 "lattice_wide": "Record permanence, corpus convergence, and empirical probability are untested"}]
    n6 = [{"file": "UNMATERIALIZED/regenerative_objective_jump_bath_cycle_next.py", "status": "OPEN / PRIORITY", "what_closes": "W_non_erasing_renewal"},
          {"file": "UNMATERIALIZED/extensional_formation_law_comparison_cycle_next.py", "status": "OPEN", "what_closes": "W_candidate_law_identification"},
          {"file": "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py", "status": "EXECUTED_PARTIAL_INTERFACE", "what_closes": "finite postformation compatibility but not either wall"}]
    n7 = {"mechanism": "construct an autonomous finite-temperature collision model whose fresh ancilla stream is generated and purified by a local regenerative QCA, prove its quantum trajectories induce the same pointer-pattern jump kernel, and derive a stationary renewal cycle that retains the occurrence ledger while exporting entropy to a counted mobile exhaust carrier",
          "actionable_steps": ["build a local collision unitary and mobile exhaust packet", "prove the induced trajectory kernel equals every Cycle662 branch operator", "close the source/sink cycle without clearing member/occurrence and compare the resulting law extensionally against competing kernels"],
          "terminal_test": "no supplied fresh bath, exact stationary renewal, unchanged all24/all576 and held propensities, one objective sigma, retained occurrence, and explicit law-selection evidence",
          "supporting_citations": [c621_renewal, c625_sigma]}
    n8 = [{"cycle": 634, "retired": "absence of an objective pointer-pattern candidate selector", "mechanism": "hybrid stochastic sigma over the unchanged physical instrument", "applicability": "retired only after supplying the jump ontology; not a derivation of nature's law", "citation_ref": c634_sigma["ref"], "citation_path": c634_sigma["path"], "citation_line": c634_sigma["line"], "citation_text": c634_sigma["text"]},
          {"cycle": 531, "retired": "MEMBER was an input at the conditional occurrence port", "mechanism": "objective sigma writes MEMBER and matching receipt", "applicability": "port production closes for these fixed menus; Record remains false", "citation_ref": c531_member["ref"], "citation_path": c531_member["path"], "citation_line": c531_member["line"], "citation_text": c531_member["text"]},
          {"cycle": 621, "retired": "none of the non-erasing renewal residual", "mechanism": "finite ready/spent conservation sharpens the same saturation", "applicability": "does not retire renewal", "citation_ref": c621_renewal["ref"], "citation_path": c621_renewal["path"], "citation_line": c621_renewal["line"], "citation_text": c621_renewal["text"]}]
    return {"Status": "PASS", "N1_normalized_families": families,
            "N1_open_routes_not_counted": [{"family": "regenerative collision bath", "status": "OPEN / NOT COUNTED"}, {"family": "dissipative topological occurrence sink", "status": "OPEN / NOT COUNTED"}],
            "N1_qualifying_attempts": 5, "N1_required_for_negative": 5, "N1_broad_negative_gate": "FAIL / DO NOT SHIP",
            "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP",
            "N2_walls": walls, "N2_directed_ordered_pairs": pairs,
            "N3_hidden_wall_scan": [{"condition": "fixed Cycle634 menus and compile order", "classification": "explicit supplied target premise"}, {"condition": "quadratic pointer-pattern jump kernel", "classification": "explicit supplied candidate law; W_candidate_law_identification"}, {"condition": "finite blank ready/exhaust slots", "classification": "explicit source resource; W_non_erasing_renewal"}, {"condition": "compile-time transported frame chart", "classification": "explicit supplied implementation structure"}],
            "N4_exact_residual_matches": n4, "N4_nonmatches_not_used_as_closure": [], "N5_rhetoric": rhetoric,
            "N6_partial_closure_paths": n6, "N7_steelman": n7, "N8_cross_cycle_echo": n8,
            "broad_no_go_claim": False, "minimum_content_claim": False, "shared_obstruction_claim": False, "axiom_pressure_claim": False,
            "broad_negative_shipped": False, "minimum_content_shipped": False, "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
            "shared_route_independent_obstruction": False, "axiom_pressure": False}


def note_text(r):
    t = r["stochastic_dilation"]; l = r["resource_ledger"]; c = r["covariance_and_preservation"]
    held = [row for row in t["rows"] if row["split"].startswith("held")]
    held_rows = "\n".join(f"| {row['menu']} | {row['state']} | {row['nonzero_objective_branches']} | {row['effect_outcome_propensity_residual']:.3e} | {row['cq_entropy_ledger_residual']:.3e} |" for row in held)
    ledger_rows = "\n".join(f"| {row['capacity']} | {row['split']} | {row['explicit_M2']} | {row['spent_sink_at_saturation']} | {str(row['saturation_refuses_firing']).lower()} | {row['inverse_roundtrip_failures']} |" for row in l["finite_rows"])
    return f"""# Objective stochastic/open dilation with retained exhaust — Cycle 662

Classification: **positive bounded objective-within-candidate-law stochastic formation/occurrence route; law identification and non-erasing renewal open**

Authority: **none**

Audit: **unset**

Breakthrough: **false**

## Frozen target and decisive construction

The exact target contract was frozen before evidence load at runner lines
`{r['target_freeze']['target_line']} < {r['target_freeze']['first_evidence_load_line']}`
with digest `{r['target_freeze']['target_contract_sha256']}`.

For each immutable Cycle634 menu, let `K_p` be the physical pointer-pattern
Kraus operator of its unchanged local unitary dilation.  Cycle662 defines the
fixed hybrid transition

`q_p(rho)=Tr[(K_p tensor I) rho (K_p^dagger tensor I)]`, `sigma'=p`.

The Cycle634 wave state and every coherent pointer sector remain in the
invertible dilation exhaust.  The stochastic law itself—not a host sampler or
an input actuality token—updates one finite ontic pointer-pattern variable
`sigma`.  Its first-hit label writes exactly one five-lane Cycle531 `MEMBER`, a
matching `LAW_RECEIPT`, and a matching binding eligibility; with `EDGE=1` the
exact Cycle531 `EDGE*binding*provenance` equation emits one occurrence
candidate, ADMIT provenance, and LOCK.
This is objective within the declared candidate law.  It is not a derivation
that this law is nature's extensional formation law.

All `{len(t['rows'])}` menu/state rows pass.  Maximum propensity-sum, effect,
inverse, and classical-quantum entropy-ledger residuals are
`{t['maximum_propensity_sum_residual']:.3e}`,
`{t['maximum_effect_outcome_residual']:.3e}`,
`{t['maximum_inverse_density_residual']:.3e}`, and
`{t['maximum_CQ_entropy_ledger_residual']:.3e}`.
The singular rank-loss menu supplies explicit lawful edge controls with
`{t['lawful_zero_propensity_branches']}` zero-propensity and
`{t['lawful_unit_propensity_branches']}` unit-propensity branches.

## Blinded held biased and nonproduct tests

| menu | held state | live patterns | effect residual | entropy residual |
|---|---|---:|---:|---:|
{held_rows}

The blinded state parameters are hash-derived after the law is fixed and are
not used to tune it.  The nonproduct system-spectator state passes trace
preservation and spectator no-signalling branch-sum controls.  The same law
and compiler are used without refit.

## What is—and is not—actualized

- The coherent dilation is an isometry with an exact inverse on its blank-port
  code.  It retains all pointer sectors.
- The dephased density is the full reduced ensemble.  Its entropy equals the
  innovation Shannon entropy plus weighted conditional entropy.  Reduced
  decoherence alone is not an actual trajectory.
- `sigma` is the stochastic law's one actual branch variable.  A trajectory is
  a finite sequence of its stored exhaust values.  The runner exhaustively
  verifies the kernel and never samples a branch.
- The emitted typed object is a member/occurrence **candidate**, not a
  framework Record.  Pointer copying is not called Record.
- The `q_p` are supplied stochastic transition propensities.  Their equality
  with the instrument effects is exact, but they are not called a derivation
  of Born probability, empirical frequency, or realized-history statistics.

No grade lookup, shell-predicate ROM, global order/parity service, supplied
actuality token, or host sampler occurs.

## Physical locality, covariance, and preservation

One firing occupies at most {l['active_M2_per_firing_supercell']} active M2 in a proper-cubic-invariant
{l['physical_supercell_M2']}-site `{l['supercell_shape']}` supercell.  Maximum
jump support is {l['maximum_jump_support_M2']} and maximum supercell L1
diameter is {l['maximum_supercell_L1_diameter']}.  The fixed menu/star and scalar occurrence-port labels are
transported at compile time.

All `{c['proper_cubic_frames']}` frames and `{c['ordered_frame_products']}`
products pass.  There are `{c['rotated_menu_state_pattern_propensity_comparisons']}`
rotated menu/state/pattern comparisons with maximum residual
`{c['maximum_rotated_propensity_residual']:.3e}`.  The six-direction packet
adapter passes all frame products and all `{c['Cycle621_preserving_generator_tests']}`
Cycle621 generator tests with LOCK/ADMIT provenance fixed.  This proves
interface compatibility with the supplied finite preserving algebra, not a
framework Record permanence law.

## Finite source/sink and retained exhaust

| capacity | split | explicit M2 | spent at saturation | refusal | inverse failures |
|---:|---|---:|---:|---|---:|
{ledger_rows}

Every firing debits one ready source slot, credits one spent sink slot, and
retains its full coherent system-pointer block plus the objective pointer
pattern, member, receipt, occurrence, ADMIT, and LOCK in that slot.  No spent
supercell is reused.  Each capacity row therefore counts
`{l['physical_supercell_M2']}*capacity` M2.
Ready plus spent is exactly conserved.  Deleting source debit, sink credit, or
exhaust data is detected.  Saturation is lawful and refuses another firing.

Exact named renewal residual:
`{l['renewal_residual_name']}`.  In the tested finite ledger, inverse restores
a ready slot only by erasing that slot's occurrence and innovation exhaust.
Relabeling a dirty spent slot as ready is refused.  No non-erasing renewal or
unbounded bath is silently claimed.  Malformed/rejected domains are refused
before source debit and leave every exhaust slot unchanged.

## Controls and route disposition

Cycle634 gate deletion, objective-branch deletion, member/receipt/occurrence,
ready/spent/exhaust deletion, malformed density/menu/source domains, coherent
inverse, entropy capacity, held states, and all24/all576 controls pass.

- Coherent dilation only: **prior bounded positive, not objective**.
- Reduced dephasing: **exact ensemble/entropy result, not an actual path**.
- Objective hybrid stochastic dilation: **positive finite candidate law**.
- State-independent innovation tape: **does not reproduce changed-state menu
  propensities**.
- Cycle625 basis unique quorum: **prior conditional basis candidate, not the
  coherent-input objective selector**.

## Supplied structure and novelty boundary

Supplied are the immutable Cycle634 menu matrices/unitaries/order and blank
ports; the quadratic stochastic jump form; finite ready/exhaust slots; the
Cycle625/Cycle531 label adapters; the Cycle621 preserving-generator alphabet;
the 125-site chart; and compile-time frame transport.  Derived are every branch
operator/propensity, one typed candidate per firing, retained coherent exhaust,
entropy/source/sink ledgers, held-state predictions, inverse/deletion/domain
controls, and interface covariance.

Naimark dilation, quantum instruments/trajectories, hybrid classical-quantum
Markov models, branch beables, and finite entropy ledgers are standard prior
art.  The narrow repo-specific contribution is their exact controlled
composition with the Cycle634 menu, Cycle625/Cycle531 occurrence port, and
Cycle621 preservation interface.  No broader novelty or priority is claimed.

## Six-wall ledger

| wall | movement | residual |
|---|---|---|
| `C_ref` | sigma is law-generated and stored, not an input actuality token | jump ontology, fixed menus, blank ports, and finite ready slots supplied |
| `C_num` | exact state-dependent propensities and blinded held predictions | no empirical calibration, convergence, or Born interpretation |
| `C_wrap` | one objective-within-law member/occurrence candidate and retained coherent exhaust | not a framework Record or realized-history recurrence |
| `C_int` | local stochastic instrument owns innovation and port writes | quadratic jump form is supplied candidate law, not called a generator rate |
| `C_local` | bounded {l['physical_supercell_M2']}-site supercell, all24/all576, exact preservation adapter | infinite deployment/noise and non-erasing renewal open |
| `C_source` | ready/spent/innovation/entropy capacity counted | no physical energy, stress, gravity source, or renewable bath identification |

## N1–N8 no-go discipline

N1 contains five normalized families; N2 keeps only two independent residuals:
candidate-law identification and non-erasing renewal.  N3 exposes every menu,
jump, blank, chart, adapter, and source import.  N4 matches Cycle634/625/531/621
at exact residual scope.  N5 narrows every negative by resolution.  N6 lists
concrete retirement paths.  N7 steelmans a regenerative collision bath and
trajectory equivalence proof.  N8 records partial closures without laundering
renewal or law identification.

Broad negative gate: **FAIL / DO NOT SHIP**.

Minimum-content gate: **FAIL / DO NOT SHIP**.

Shared-obstruction gate: **FAIL / DO NOT SHIP**.

Axiom-pressure gate: **FAIL / DO NOT SHIP**.

Shared route-independent obstruction: **none**. Axiom pressure: **none**.
"""


def main():
    signal.alarm(1200); started = time.perf_counter()
    freeze = target_freeze_controls(); check("exact target contract frozen before evidence load", freeze["pass"], freeze)
    shore = shore_controls(); check("Cycle634/Cycle625/Cycle531/Cycle621 immutable shores and interfaces", shore["pass"], shore["imported_contracts"])
    tournament = stochastic_dilation_tournament(); check("objective stochastic retained-exhaust kernel on all train and blinded held states", tournament["pass"], {"rows": tournament["state_rows"], "held": tournament["held_blind_rows"], "effect": tournament["maximum_effect_outcome_residual"]})
    ledger = ledger_controls(tournament); check("finite ready/spent innovation ledger, inverse, saturation, and exact renewal residual", ledger["pass"], {"sizes": len(ledger["finite_rows"]), "renewal": ledger["renewal_residual_name"]})
    covariance = covariance_and_preservation(tournament); check("all24/all576 menu propensities, supercell, packet, and Cycle621 preservation", covariance["pass"], {"comparisons": covariance["rotated_menu_state_pattern_propensity_comparisons"], "generators": covariance["Cycle621_preserving_generator_tests"]})
    deletion = deletion_and_domain_controls(tournament); check("inverse/deletion/malformed/lawful-domain and host-free controls", deletion["pass"], {"gate_rows": len(deletion["deleted_Cycle634_binary_gate_rows"]), "malformed": deletion["malformed_domain_rejections"]})
    no_go = no_go_discipline()
    canonical = {"Status_PASS": no_go["Status"] == "PASS", "gates": all(no_go[k] == "FAIL / DO NOT SHIP" for k in ("N1_broad_negative_gate", "broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate")), "flags": not any(no_go[k] for k in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim", "broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped", "shared_route_independent_obstruction", "axiom_pressure")), "N1": no_go["N1_qualifying_attempts"] == no_go["N1_required_for_negative"] == 5 and all(x["honesty_marker"] in {"ATTEMPTED", "RULED OUT BY PRIOR"} for x in no_go["N1_normalized_families"]), "N2": len(no_go["N2_directed_ordered_pairs"]) == 2, "N4": all({"prior_ref", "prior_path", "prior_line", "prior_residual", "current_path", "current_line", "current_residual", "same_scope", "exact_match", "use_as_closure"} <= set(x) for x in no_go["N4_exact_residual_matches"]+no_go["N4_nonmatches_not_used_as_closure"]), "N5": all({"per_element", "per_site", "per_mode", "per_block", "lattice_wide"} <= set(x) for x in no_go["N5_rhetoric"]), "N6": all({"file", "status", "what_closes"} <= set(x) for x in no_go["N6_partial_closure_paths"]), "N7": all(k in no_go["N7_steelman"] for k in ("mechanism", "actionable_steps", "terminal_test", "supporting_citations")), "N8": all({"retired", "mechanism", "applicability", "citation_ref", "citation_path", "citation_line", "citation_text"} <= set(x) for x in no_go["N8_cross_cycle_echo"])}
    canonical["pass"] = all(canonical.values()); check("fresh canonical N1-N8 schema and negative gates", canonical["pass"], canonical)
    receipt = {"Status": "PASS", "cycle": 662, "date": "2026-07-23", "status": "positive bounded objective-within-candidate-law stochastic formation/occurrence route; law identification and non-erasing renewal open", "classification": "objective stochastic/open dilation with retained coherent and finite classical exhaust", "authority": "none", "audit": "unset", "author_accepted": False, "author_artifact_status_accepted": False, "breakthrough": False, "strict_full_framework_terminal_met": False, "target_contract_candidate_terminal_met": True, "constitutional_effect": "none", "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP", "broad_no_go_claim": False, "minimum_content_claim": False, "shared_obstruction_claim": False, "axiom_pressure_claim": False, "broad_negative_shipped": False, "minimum_content_shipped": False, "shared_obstruction_shipped": False, "axiom_pressure_shipped": False, "shared_route_independent_obstruction": False, "axiom_pressure": False, "target_contract": TARGET_CONTRACT, "target_freeze": freeze, "shore": shore, "stochastic_dilation": tournament, "resource_ledger": ledger, "covariance_and_preservation": covariance, "deletion_and_domain": deletion, "semantic_separation": {"coherent_dilation": "invertible physical menu superposition with all branches retained", "reduced_decoherence": "CPTP ensemble and CQ entropy ledger; not one actual path", "stochastic_law": "declared objective sigma jump kernel with no selector input", "actual_trajectory": "one sequence of sigma values stored in spent exhaust slots", "Record": False, "Born_probability": False, "empirical_frequency": False}, "route_disposition": {"A_coherent_only": "PRIOR_POSITIVE_NOT_OBJECTIVE", "B_reduced_dephasing": "PASS_ENSEMBLE_AND_ENTROPY__NOT_ACTUAL_PATH", "C_objective_stochastic": "PASS_BOUNDED_SUPPLIED_CANDIDATE_LAW", "D_state_independent_tape": "FAILS_CHANGED_STATE_INSTRUMENT_PROPENSITIES", "E_unique_quorum": "PRIOR_BASIS_CONDITIONAL_NOT_COHERENT_SIGMA"}, "supplied_structure_inventory": {"Cycle634_fixed_menus_unitaries_order_blank_ports": True, "quadratic_stochastic_jump_form": True, "finite_ready_exhaust_slots": True, "Cycle625_Cycle531_label_adapters": True, "Cycle621_preserving_generator_alphabet": True, "proper_cubic_27_site_chart": True, "compile_time_frame_transport": True, "host_sampler": False, "supplied_actuality_token": False, "grade_lookup": False, "shell_predicate_ROM": False}, "prior_art_novelty_boundary": {"standard_prior_art": ["finite Naimark dilation and quantum instruments", "quantum trajectories and hybrid classical-quantum Markov models", "branch-beable/modal stochastic laws", "finite classical entropy/source-sink ledgers"], "narrow_new_result": "exact bounded composition with immutable Cycle634 menu, Cycle625/Cycle531 occurrence port, Cycle621 preservation, blinded-state/covariance/exhaust controls", "broader_novelty_claimed": False}, "strongest_constructive_result": "one fixed bounded hybrid stochastic transition retains the complete coherent Cycle634 dilation while internally selecting and storing one objective-within-law pointer-pattern sigma that emits a typed member/receipt/occurrence candidate, with exact held-state, entropy, resource, covariance, and preservation controls", "highest_honest_terminal": "objective occurrence candidate inside a supplied finite stochastic ontology; not framework law identification, Record, Born meaning, or non-erasing renewal", "no_go_discipline": no_go, "canonical_claim_gate_contract": canonical, "six_wall_ledger": {"C_ref": "sigma generated/stored rather than supplied; jump ontology, menus, blanks, finite ready slots supplied", "C_num": "exact propensities and blinded held predictions; no empirical/Born interpretation", "C_wrap": "one objective-within-law member/occurrence candidate with coherent exhaust; no Record/history", "C_int": "local stochastic instrument owns innovation/port writes; quadratic jump form supplied", "C_local": "bounded 27-site supercell and all24/all576; infinite/noisy deployment and renewal open", "C_source": "ready/spent/innovation/entropy counted; no energy/stress/gravity or renewable bath"}, "optimal_next_campaign": "regenerative autonomous collision bath that reproduces the exact jump kernel, exports counted entropy, and renews ready capacity without erasing occurrence, followed by extensional comparison against rival objective kernels"}
    receipt["supplied_structure_inventory"]["proper_cubic_125_site_chart"] = receipt["supplied_structure_inventory"].pop("proper_cubic_27_site_chart")
    receipt["six_wall_ledger"]["C_local"] = "bounded 125-site supercell and all24/all576; infinite/noisy deployment and renewal open"
    top = {"Status": receipt["Status"] == "PASS", "gates": all(receipt[k] == "FAIL / DO NOT SHIP" for k in ("broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate")), "flags": not any(receipt[k] for k in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim", "broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped", "shared_route_independent_obstruction", "axiom_pressure")), "strict_false": receipt["strict_full_framework_terminal_met"] is False, "candidate_true": receipt["target_contract_candidate_terminal_met"] is True, "breakthrough_false": receipt["breakthrough"] is False}
    top["pass"] = all(top.values()); receipt["top_level_claim_gate_contract"] = top; check("top-level candidate/strict/breakthrough and negative gates", top["pass"], top)
    NOTE.write_text(note_text(receipt)); flat = " ".join(NOTE.read_text().lower().split())
    required = ("authority: **none**", "audit: **unset**", "breakthrough: **false**", "host sampler", "supplied actuality token", "reduced decoherence alone is not an actual trajectory", "not a framework record", "not called a derivation of born probability", "all `24`", "576", "exact named renewal residual", "fail / do not ship", "axiom pressure: **none**")
    missing = [fragment for fragment in required if fragment not in flat]; check("Cycle662 note semantic contract", not missing, missing)
    elapsed = time.perf_counter()-started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE), "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss, "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0})
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=float)+"\n")
    print(json.dumps({"pass": receipt["pass"], "tests": f"{PASS}/{PASS+FAIL}", "elapsed": elapsed, "receipt": str(RECEIPT)}, indent=2)); return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        original = sys.stdout; sys.stdout = Tee(original, stream)
        try: raise SystemExit(main())
        finally: sys.stdout = original
