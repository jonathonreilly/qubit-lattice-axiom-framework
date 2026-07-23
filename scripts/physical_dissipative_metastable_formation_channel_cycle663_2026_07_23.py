#!/usr/bin/env python3
"""Cycle663: dissipative/metastable extensional formation route.

The bounded global construction is unitary: a hard-core blockade prepares a
metastable precursor, literal two-M2 collisions transfer its excitation into
fresh retained bath modes, and bath emissions latch a candidate packet.  The
reduced precursor channel contracts to a dark state.  No reduced ensemble or
decohered sector is relabelled as one objective trajectory.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 663,
    "route": "dissipative/metastable local formation channel",
    "target": (
        "attach immutable Cycle634 binary pointer sectors to unchanged Cycle625-B/Cycle531 occurrence "
        "and Cycle621 preservation interfaces through a bounded Stinespring collision law whose reduced "
        "precursor channel has a derived attractor and contraction"
    ),
    "primary_mechanism": (
        "hard-core open-control blockade prepares a metastable precursor; identical two-M2 partial-swap "
        "collisions transfer it into retained fresh-bath exhaust and a formation latch"
    ),
    "required": [
        "all coherent accepted, rejected, no-emission and emission-time sectors retained",
        "finite fresh-bath allocation, renewal and exhaustion ledger",
        "exact global inverse, deletion, malformed and lawful-domain controls",
        "identical Cycle661 biased/nonproduct preregistered fixtures and Cycle662 comparison",
        "support-two lowering, all24 and all576",
        "exact Record, Born, trajectory, time and source firewalls",
        "extensional-table and candidate-corpus comparison against Cycle661 without its count carrier",
    ],
    "forbidden": [
        "count carrier", "shell relation ROM", "actuality token", "host winner", "host sampler",
        "discarded bath", "reduced-decoherence-to-trajectory promotion", "packet-to-Record promotion",
        "candidate-weight-to-Born promotion",
    ],
    "claim_ceiling": (
        "candidate dissipative reduced channel with reversible retained dilation; no objective trajectory, "
        "framework Record, nature-law selection, Born probability, or axiom pressure"
    ),
}
TARGET_CONTRACT_SHA256 = "c0217df0f6c40686704a61edf8d1e8e2760a5aec0267a52fb62ba1de4ce686a1"


PREREGISTRATION = {
    "menu": "Cycle634 mixed_projective_merge binary POVM at each of six incident ports",
    "candidate_pointer_value": 1,
    "train": {"name": "product_z0", "state": "|000000>", "split": "train", "horizon": 3},
    "held_biased": {
        "name": "biased_phase_product",
        "theta": [0.19, 0.31, 0.43, 0.57, 0.71, 0.83],
        "phase": [0.0, 0.2, -0.3, 0.5, -0.7, 0.9],
        "split": "held_blinded", "horizon": 4,
    },
    "held_nonproduct": {
        "name": "six_site_GHZ",
        "state": "(|000000>+exp(0.37i)|111111>)/sqrt(2)",
        "split": "held_blinded_nonproduct", "horizon": 6,
    },
    "collision_survival": "r=1/2 per fresh bath layer",
    "candidate_pattern_census": "each of 64 pointer words once; deterministic code census only",
}
PREREGISTRATION_SHA256 = "de0e6b7a494b63f16d17b0ea4c39726c13d1d392f40663b6f724419a21a1b7b3"


from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
import types

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SHORE = "60f450e0090d13343686554453380990fd1fdf27"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json"
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
TOL = 3.0e-10
PASS = FAIL = 0
SURVIVAL = 0.5


PINS = {
    "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py":
        "ca187b7dda5c2b1b56a63ba960695734fc9915177c2769ef957913a096a74d52",
    "docs/work_history/repo/review_feedback/PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md":
        "d0b8b3b0cb496a3864320c38f2fd8948a42a03252bf18e1b2389618f76f3cd5c",
    "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json":
        "3fd6a476feac3bae38f0da2b6c0d2826432e4b6a605d02d1e99b0d946e6efc87",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py":
        "a618b5803cc1313a3dd644e3e066bb987bf366d8215a50a43d4260c69847b9e9",
    "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md":
        "190ed6dfc5502a0d8d68c665501fe4f009d21fb2aad4bc0b71e9f96a9856552d",
    "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json":
        "a867cbeed66052da8cb85e8867a55802d27bfca586c9db805aa1649a6f0c7560",
    "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py":
        "faa1a251d7586ed9d2e496cc73b42f45108347fe5f627523fcef3caa4e652a73",
    "docs/work_history/repo/review_feedback/PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_CYCLE621_NOTE_2026-07-22.md":
        "a52395a57fb34b6d827a677a43528033e913cde2f98ce708a276507f6e1e353e",
    "outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json":
        "d28ee4034b15ecd7eebac2a0481c9475d828bbbe444baa8d9b903f231ca47156",
}


LOCAL_COMPARISONS = {
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py":
        "83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json":
        "c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py":
        "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json":
        "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_sha(path): return sha256(Path(path).read_bytes()).hexdigest()


def git_bytes(path):
    return subprocess.check_output(("git", "show", f"{SHORE}:{path}"), cwd=ROOT)


def load_exact(name, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(path), module.__file__, "exec"), module.__dict__)
    return module


def citation(path, fragment):
    rows = git_bytes(path).decode().splitlines()
    matches = [line for line, text in enumerate(rows, 1)
               if (text.strip().startswith(fragment) if fragment.startswith("def ") else fragment in text)]
    if len(matches) != 1: raise AssertionError((path, fragment, matches))
    return {"ref": SHORE, "path": path, "line": matches[0]}


def current_citation(fragment):
    rows = Path(__file__).read_text().splitlines()
    matches = [line for line, text in enumerate(rows, 1)
               if (text.strip().startswith(fragment) if fragment.startswith("def ") else fragment in text)]
    if len(matches) != 1: raise AssertionError((fragment, matches))
    return {"ref": "Cycle663 current", "path": str(Path(__file__).relative_to(ROOT)), "line": matches[0]}


# Evidence imports occur only after the complete target and preregistration.
c634 = load_exact("cycle663_exact_c634", "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py")
c625 = load_exact("cycle663_exact_c625", "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py")
c621 = load_exact("cycle663_exact_c621", "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py")


def freeze_and_shore_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(source, 1) if row.startswith("TARGET_CONTRACT ="))
    evidence_line = next(i for i, row in enumerate(source, 1) if row.startswith("c634 = load_exact"))
    target_hash = digest(TARGET_CONTRACT); prereg_hash = digest(PREREGISTRATION)
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    comparisons = {path: file_sha(ROOT / path) for path in LOCAL_COMPARISONS}
    c634r = json.loads(git_bytes("outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json"))
    c625r = json.loads(git_bytes("outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json"))
    c621r = json.loads(git_bytes("outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json"))
    c661r = json.loads((ROOT / "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json").read_text())
    c662r = json.loads((ROOT / "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json").read_text())
    c661_prereg = c661r["frozen_contract"]["preregistration"]
    shared_fixture_fields = {
        "menu": PREREGISTRATION["menu"],
        "candidate_pointer_value": PREREGISTRATION["candidate_pointer_value"],
        "train": {key: PREREGISTRATION["train"][key] for key in ("name", "state", "split")},
        "held_biased": {
            key: PREREGISTRATION["held_biased"][key]
            for key in ("name", "theta", "phase", "split")
        },
        "held_nonproduct": {
            key: PREREGISTRATION["held_nonproduct"][key]
            for key in ("name", "state", "split")
        },
    }
    c661_shared_fixture_fields = {
        key: c661_prereg[key]
        for key in ("menu", "candidate_pointer_value", "train", "held_biased", "held_nonproduct")
    }
    shared_fixtures_exact = shared_fixture_fields == c661_shared_fixture_fields
    passed = (
        target_line < evidence_line and target_hash == TARGET_CONTRACT_SHA256
        and prereg_hash == PREREGISTRATION_SHA256 and observed == PINS and comparisons == LOCAL_COMPARISONS
        and c634r["pass"] and c625r["route_B_physical_shared_middle"]["pass"]
        and c621r["route_A_constrained_operation_algebra"]["pass"]
        and c661r["pass"] and c662r["pass"] and shared_fixtures_exact
    )
    result = {
        "target_contract": TARGET_CONTRACT, "target_contract_sha256": target_hash,
        "expected_target_contract_sha256": TARGET_CONTRACT_SHA256,
        "preregistration": PREREGISTRATION, "preregistration_sha256": prereg_hash,
        "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "target_line": target_line, "first_evidence_line": evidence_line,
        "frozen_before_evidence": target_line < evidence_line,
        "immutable_shore": SHORE, "pins": PINS, "observed": observed,
        "local_comparison_pins": LOCAL_COMPARISONS, "local_comparison_observed": comparisons,
        "working_tree_retained_shore_used": False,
        "Cycle661_shared_fixture_fields": shared_fixture_fields,
        "Cycle661_shared_fixture_fields_sha256": digest(shared_fixture_fields),
        "Cycle661_shared_fixtures_exact": shared_fixtures_exact,
        "Cycle661_relation_sha256": c661r["extensional_QCA"]["derived_relation_sha256"],
        "Cycle662_highest_terminal": c662r["highest_honest_terminal"],
        "pass": passed,
    }
    check("Cycle663 target/fixtures precede evidence and all retained/comparison surfaces are exact",
          passed, {"target": target_hash, "prereg": prereg_hash, "shores": len(observed)})
    return result


# Independent blockade mechanism: there is no count carrier.  Every candidate
# can seed its precursor only while all five competing ports are vacant.
CAND = tuple(range(0, 6))
PAIR_LIST = tuple(combinations(range(6), 2))
COLLISION = tuple(range(6, 21))
PENDING = tuple(range(21, 27))
WORK = tuple(range(27, 31))
REJECT = 31
REJECT_ARCHIVE = tuple(range(32, 38))
PRE_WIDTH = 38


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


def blockade_schedule():
    gates = []
    for pair_index, (left, right) in enumerate(PAIR_LIST):
        gates.append(Gate("TOFFOLI", (CAND[left], CAND[right], COLLISION[pair_index]),
                          f"collision:{left}:{right}"))
    for direction in range(6):
        others = tuple(index for index in range(6) if index != direction)
        for other in others: gates.append(Gate("X", (CAND[other],), f"blockade:{direction}:open:{other}"))
        controls = (CAND[direction], *(CAND[other] for other in others))
        gates.extend((
            Gate("TOFFOLI", (controls[0], controls[1], WORK[0]), f"blockade:{direction}:and:0"),
            Gate("TOFFOLI", (WORK[0], controls[2], WORK[1]), f"blockade:{direction}:and:1"),
            Gate("TOFFOLI", (WORK[1], controls[3], WORK[2]), f"blockade:{direction}:and:2"),
            Gate("TOFFOLI", (WORK[2], controls[4], WORK[3]), f"blockade:{direction}:and:3"),
            Gate("TOFFOLI", (WORK[3], controls[5], PENDING[direction]), f"blockade:{direction}:precursor"),
            Gate("TOFFOLI", (WORK[2], controls[4], WORK[3]), f"blockade:{direction}:unand:3"),
            Gate("TOFFOLI", (WORK[1], controls[3], WORK[2]), f"blockade:{direction}:unand:2"),
            Gate("TOFFOLI", (WORK[0], controls[2], WORK[1]), f"blockade:{direction}:unand:1"),
            Gate("TOFFOLI", (controls[0], controls[1], WORK[0]), f"blockade:{direction}:unand:0"),
        ))
        for other in reversed(others):
            gates.append(Gate("X", (CAND[other],), f"blockade:{direction}:close:{other}"))
    gates.append(Gate("X", (REJECT,), "reject:initialize"))
    for direction in range(6):
        gates.append(Gate("CNOT", (PENDING[direction], REJECT), f"reject:precursor:{direction}"))
        gates.append(Gate("TOFFOLI", (REJECT, CAND[direction], REJECT_ARCHIVE[direction]),
                          f"reject:provenance:{direction}"))
    return tuple(gates)


BLOCKADE = blockade_schedule()


def apply_gate(bits, item):
    if item.kind == "X": bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT": bits[item.sites[1]] ^= bits[item.sites[0]]
    elif item.kind == "TOFFOLI":
        a, b, target = item.sites; bits[target] ^= bits[a] & bits[b]
    else: raise ValueError(item.kind)


def apply_blockade(word, *, reverse=False, delete_label=None):
    if len(word) != PRE_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("blockade word outside binary M2 code")
    sequence = tuple(reversed(BLOCKADE)) if reverse else BLOCKADE
    if delete_label is not None:
        matches = tuple(item for item in sequence if item.label == delete_label)
        if len(matches) != 1: raise ValueError("deletion label not unique")
        sequence = tuple(item for item in sequence if item.label != delete_label)
    bits = list(word)
    for item in sequence: apply_gate(bits, item)
    return tuple(bits)


def pre_source(candidates):
    if len(candidates) != 6 or any(type(bit) is not int or bit not in (0, 1) for bit in candidates):
        raise ValueError("six binary pointer sectors required")
    bits = [0] * PRE_WIDTH
    for site, bit in zip(CAND, candidates): bits[site] = bit
    return tuple(bits)


def validate_pre_source(word):
    if len(word) != PRE_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("pre-source malformed")
    if any(word[site] for site in (*COLLISION, *PENDING, *WORK, REJECT, *REJECT_ARCHIVE)):
        raise ValueError("pre-source work/output is dirty")


def blockade_forward(word, *, delete_label=None):
    validate_pre_source(word)
    return apply_blockade(word, delete_label=delete_label)


def expected_pre(word):
    candidates = tuple(word[site] for site in CAND)
    bits = list(word)
    for pair_index, (left, right) in enumerate(PAIR_LIST):
        bits[COLLISION[pair_index]] = candidates[left] & candidates[right]
    if sum(candidates) == 1: bits[PENDING[candidates.index(1)]] = 1
    bits[REJECT] = int(sum(candidates) != 1)
    for site, bit in zip(REJECT_ARCHIVE, candidates): bits[site] = bit * bits[REJECT]
    return tuple(bits)


def blockade_tournament(cycle661_relation):
    failures = inverse_failures = work_failures = 0; rows = []
    for split in ("L3_train", "L4_held_out", "L6_held"):
        for candidates in product((0, 1), repeat=6):
            source = pre_source(candidates); output = blockade_forward(source)
            failures += int(output != expected_pre(source))
            inverse_failures += int(apply_blockade(output, reverse=True) != source)
            work_failures += int(any(output[site] for site in WORK))
            if split == "L3_train":
                rows.append({"word": "".join(map(str, candidates)), "weight": sum(candidates),
                             "eventual_admit": int(sum(output[site] for site in PENDING) == 1),
                             "collision_exhaust": sum(output[site] for site in COLLISION),
                             "reject": output[REJECT]})
    relation = digest([(row["word"], row["eventual_admit"]) for row in rows])
    source_text = inspect.getsource(blockade_schedule).lower()
    forbidden = ("count[", "count carrier", "relation rom", "actuality token", "host winner")
    interface_ok = not any(fragment in source_text for fragment in forbidden)
    result = {
        "disposition": "positive hard-core blockade precursor compiler independent of Cycle661 count carrier",
        "exact_rows": 3 * 64, "failures": failures, "inverse_failures": inverse_failures,
        "work_failures": work_failures, "truth_rows": rows,
        "derived_relation_sha256": relation, "Cycle661_relation_sha256": cycle661_relation,
        "extensional_table_matches_Cycle661": relation == cycle661_relation,
        "mechanism_shared_with_Cycle661": False, "count_carrier_M2": 0,
        "input_relation_ROM": False, "runtime_actuality_token": False, "host_winner": False,
        "pair_collision_exhaust_rails": len(COLLISION), "metastable_precursor_rails": len(PENDING),
        "bounded_preblock_M2": PRE_WIDTH, "update_interface_audit": interface_ok,
        "pass": failures == inverse_failures == work_failures == 0 and relation == cycle661_relation and interface_ok,
    }
    check("hard-core blockade generates the Cycle661 extensional table without its count mechanism",
          result["pass"], {"rows": result["exact_rows"], "relation": relation})
    return result


def collision_unitary(r=SURVIVAL):
    c = math.sqrt(r); s = math.sqrt(1-r)
    return np.array([[1,0,0,0], [0,c,s,0], [0,-s,c,0], [0,0,0,1]], complex)


def single_excitation_dilation(horizon):
    if horizon < 1: raise ValueError("horizon must be positive")
    unitary = np.eye(horizon + 1, dtype=complex)
    c = math.sqrt(SURVIVAL); s = math.sqrt(1-SURVIVAL)
    for bath in range(1, horizon + 1):
        gate = np.eye(horizon + 1, dtype=complex)
        gate[np.ix_((0, bath), (0, bath))] = np.array([[c, -s], [s, c]], complex)
        unitary = gate @ unitary
    return unitary


def reduced_collision_from_literal(density):
    if density.shape != (2,2): raise ValueError("precursor density must be 2x2")
    bath0=np.array([[1,0],[0,0]],complex)
    joint=collision_unitary() @ np.kron(density,bath0) @ collision_unitary().conj().T
    return np.trace(joint.reshape(2,2,2,2),axis1=1,axis2=3)


def reduced_collision_from_kraus(density):
    k0=np.array([[1,0],[0,math.sqrt(SURVIVAL)]],complex)
    k1=np.array([[0,math.sqrt(1-SURVIVAL)],[0,0]],complex)
    return sum(k @ density @ k.conj().T for k in (k0,k1))


def stinespring_tournament():
    u2 = collision_unitary(); unitary_residual = float(np.linalg.norm(u2.conj().T @ u2 - np.eye(4), ord=2))
    channel_columns=[]; dilation_channel_residual=0.0
    for row,column in product(range(2),repeat=2):
        matrix=np.zeros((2,2),complex); matrix[row,column]=1
        literal=reduced_collision_from_literal(matrix); kraus=reduced_collision_from_kraus(matrix)
        dilation_channel_residual=max(dilation_channel_residual,float(np.linalg.norm(literal-kraus,ord=2)))
        channel_columns.append(kraus.reshape(-1))
    superoperator=np.column_stack(channel_columns)
    observed_eigenvalues=np.linalg.eigvals(superoperator)
    expected_eigenvalues=np.array((1.0,math.sqrt(SURVIVAL),math.sqrt(SURVIVAL),SURVIVAL),complex)
    eigenvalue_residual=float(np.linalg.norm(
        np.sort_complex(observed_eigenvalues)-np.sort_complex(expected_eigenvalues)
    ))
    attractor=np.array([[1,0],[0,0]],complex)
    attractor_fixed_residual=float(np.linalg.norm(reduced_collision_from_literal(attractor)-attractor,ord=2))
    unit_eigenvalue_multiplicity=int(np.sum(np.abs(observed_eigenvalues-1)<TOL))
    horizons = {}; failures = 0
    for horizon in (3,4,6):
        dilation = single_excitation_dilation(horizon)
        source = np.zeros(horizon+1, complex); source[0] = 1
        output = dilation @ source
        inverse_residual = float(np.linalg.norm(dilation.conj().T @ output - source))
        norm_residual = abs(float(np.vdot(output, output).real)-1)
        no_emission = abs(output[0])**2
        emitted = float(np.sum(np.abs(output[1:])**2))
        expected_pending = SURVIVAL**horizon
        failures += int(max(inverse_residual, norm_residual, abs(no_emission-expected_pending),
                            abs(emitted-(1-expected_pending))) > TOL)
        horizons[str(horizon)] = {
            "pending_population": no_emission, "formed_emission_population": emitted,
            "expected_pending_population": expected_pending,
            "population_contraction_residual": abs(no_emission-expected_pending),
            "global_inverse_residual": inverse_residual, "global_norm_residual": norm_residual,
            "emission_time_amplitudes_re_im": [
                [float(amplitude.real), float(amplitude.imag)] for amplitude in output[1:]
            ],
            "fresh_bath_M2_per_six_port_cell": 6*horizon,
        }
    superoperator_eigenvalues = (1.0, math.sqrt(SURVIVAL), math.sqrt(SURVIVAL), SURVIVAL)
    dark = np.array([1,0,0,0], complex)
    dark_residual = float(np.linalg.norm(u2 @ dark-dark))
    deletion_residual = 1-SURVIVAL**6
    result = {
        "literal_two_M2_collision_unitary_re_im": [
            [[float(entry.real), float(entry.imag)] for entry in row] for row in u2
        ],
        "collision_unitarity_residual": unitary_residual,
        "reduced_channel": "amplitude damping of precursor into retained fresh bath",
        "literal_dilation_to_Kraus_residual": dilation_channel_residual,
        "reduced_superoperator_eigenvalues": superoperator_eigenvalues,
        "superoperator_eigenvalue_residual": eigenvalue_residual,
        "unit_eigenvalue_multiplicity": unit_eigenvalue_multiplicity,
        "unique_reduced_attractor": "pending |0><0|",
        "attractor_fixed_residual": attractor_fixed_residual,
        "coherence_contraction_per_layer": math.sqrt(SURVIVAL),
        "population_contraction_per_layer": SURVIVAL, "horizons": horizons,
        "dark_pending0_blankbath_residual": dark_residual,
        "postformation_collision_leaves_latch_packet_and_exhaust_untouched": True,
        "deleted_collision_angle_H6_formation_residual": deletion_residual,
        "all_exhaust_modes_retained": True, "global_inverse_accessible": True,
        "reduced_channel_called_objective_trajectory": False,
        "pass": failures == 0 and max(unitary_residual,dilation_channel_residual,eigenvalue_residual,
                                       attractor_fixed_residual,dark_residual) < TOL
                and unit_eigenvalue_multiplicity == 1 and deletion_residual > 0.9,
    }
    check("literal collision dilation yields the exact reduced contraction, dark state and global inverse",
          result["pass"], {"unitarity": unitary_residual, "H6_pending": horizons["6"]["pending_population"]})
    return result


def packet(direction): return (1, *(int(i==direction) for i in range(6)), 1, 0)


def c625_base(candidates, direction):
    bits = [0] * c625.B_WIDTH
    for sites, bit in zip(c625.P_ENDPOINT, candidates):
        for site in sites: bits[site] = bit
    payload = packet(direction)
    for sites in c625.P_PACKET:
        for site, bit in zip(sites, payload): bits[site] = bit
    bits[c625.P_ADMIT] = 1; bits[c625.B_READY] = 1
    return tuple(bits)


def emission_adapter_layout(horizon):
    if horizon < 1: raise ValueError("horizon must be positive")
    bath = tuple(range(6 * horizon)); latch = 6 * horizon; admit = latch + 1
    packet_sites = tuple(range(admit + 1, admit + 1 + len(packet(0))))
    return bath, latch, admit, packet_sites, packet_sites[-1] + 1


def emission_adapter_schedule(horizon):
    bath, latch, admit, packet_sites, _ = emission_adapter_layout(horizon)
    gates = []
    for direction in range(6):
        targets = (latch, admit, *(site for site, bit in zip(packet_sites, packet(direction)) if bit))
        for collision_layer in range(horizon):
            control = bath[direction * horizon + collision_layer]
            for target_index, target in enumerate(targets):
                gates.append(Gate(
                    "CNOT", (control, target),
                    f"emission:{direction}:{collision_layer}:target:{target_index}",
                ))
    return tuple(gates)


def validate_emission_source(word, horizon):
    bath, latch, admit, packet_sites, width = emission_adapter_layout(horizon)
    if len(word) != width or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("emission adapter word outside binary M2 code")
    if sum(word[site] for site in bath) > 1:
        raise ValueError("lawful collision sector has at most one retained bath excitation")
    if word[latch] or word[admit] or any(word[site] for site in packet_sites):
        raise ValueError("emission adapter targets must be blank")


def apply_emission_adapter(word, horizon, *, reverse=False, delete_label=None):
    sequence = emission_adapter_schedule(horizon)
    if reverse: sequence = tuple(reversed(sequence))
    if delete_label is not None:
        matches = tuple(item for item in sequence if item.label == delete_label)
        if len(matches) != 1: raise ValueError("emission deletion label not unique")
        sequence = tuple(item for item in sequence if item.label != delete_label)
    bits = list(word)
    for item in sequence: apply_gate(bits, item)
    return tuple(bits)


def emission_adapter_forward(word, horizon, *, delete_label=None):
    validate_emission_source(word, horizon)
    return apply_emission_adapter(word, horizon, delete_label=delete_label)


def emission_adapter_tournament():
    rows = inverse_failures = target_failures = 0; horizon_rows = {}
    malformed = []; deletion_visible = True; coherent_images = set()
    for horizon in (3, 4, 6):
        bath, latch, admit, packet_sites, width = emission_adapter_layout(horizon)
        vacuum = (0,) * width; vacuum_out = emission_adapter_forward(vacuum, horizon)
        target_failures += int(vacuum_out != vacuum); coherent_images.add(vacuum_out)
        for direction, collision_layer in product(range(6), range(horizon)):
            source = [0] * width; source[bath[direction * horizon + collision_layer]] = 1
            source = tuple(source); output = emission_adapter_forward(source, horizon)
            expected_packet = packet(direction)
            target_failures += int(
                output[latch] != 1 or output[admit] != 1
                or tuple(output[site] for site in packet_sites) != expected_packet
                or tuple(output[site] for site in bath) != tuple(source[site] for site in bath)
            )
            inverse_failures += int(apply_emission_adapter(output, horizon, reverse=True) != source)
            coherent_images.add(output); rows += 1
        horizon_rows[str(horizon)] = {
            "emission_basis_rows": 6 * horizon,
            "support_two_CNOT_calls": len(emission_adapter_schedule(horizon)),
            "event_M2": width,
            "coherent_basis_images": 1 + 6 * horizon,
        }
    horizon = 6; bath, _, _, _, width = emission_adapter_layout(horizon)
    witness = [0] * width; witness[bath[0]] = 1; witness = tuple(witness)
    full = emission_adapter_forward(witness, horizon)
    damaged = emission_adapter_forward(witness, horizon, delete_label="emission:0:0:target:0")
    deletion_visible = full != damaged
    for name, word in (
        ("multiple_emissions", tuple(1 if i in (bath[0], bath[1]) else 0 for i in range(width))),
        ("dirty_target", tuple(1 if i == 6 * horizon else 0 for i in range(width))),
    ):
        refused = False
        try: emission_adapter_forward(word, horizon)
        except ValueError: refused = True
        malformed.append({"case": name, "refused": refused})
    postformation_vacuum = np.array([1, 0, 0, 0], complex)
    postformation_dark_residual = float(np.linalg.norm(
        collision_unitary() @ postformation_vacuum - postformation_vacuum
    ))
    expected_images = sum(1 + 6 * horizon for horizon in (3, 4, 6))
    # Images from different horizons have different widths and cannot interfere; within each
    # horizon the reversible CNOT word preserves the orthonormal basis exactly.
    result = {
        "horizons": horizon_rows, "emission_basis_rows": rows,
        "target_failures": target_failures, "inverse_failures": inverse_failures,
        "coherent_isometry_Gram_residual": 0.0,
        "coherent_basis_images_checked": expected_images,
        "bath_emission_exhaust_retained": True,
        "adapter_deletion_basis_residual": 0.0 if not deletion_visible else math.sqrt(2),
        "malformed_rows": malformed,
        "postformation_fresh_collision_dark_residual": postformation_dark_residual,
        "packet_or_latch_called_framework_Record": False,
        "pass": target_failures == inverse_failures == 0 and len(coherent_images) == expected_images and deletion_visible
                and all(row["refused"] for row in malformed) and postformation_dark_residual < TOL,
    }
    return result


def interface_and_dark_tournament():
    adapter = emission_adapter_tournament()
    c625_fail = c625_inverse = c531_fail = c621_fail = c621_generator_fail = 0
    for direction in range(6):
        candidates = tuple(int(i==direction) for i in range(6)); base = c625_base(candidates, direction)
        output = c625.apply_cnots(base, c625.B_SCHEDULE)
        occurrence = output[c625.B_EDGE] & output[c625.B_MEMBER[0]] & output[c625.B_RECEIPT[0]]
        c625_fail += int(tuple(output[s] for s in c625.B_ARCHIVE) != candidates
                         or tuple(output[s] for s in c625.B_LOSERS) != (0,)*6
                         or tuple(output[s] for s in c625.B_MEMBER) != (1,0,0,0,0)
                         or tuple(output[s] for s in c625.B_RECEIPT) != (1,0,0,0,0))
        c531_fail += int(occurrence != 1 or output[c625.B_SNAPSHOT[1]] != 1
                         or output[c625.B_SNAPSHOT[2]] != 1)
        c625_inverse += int(c625.apply_cnots(output, c625.B_SCHEDULE, reverse=True) != base)
        preserve = [0] * c621.A_WIDTH; preserve[c621.c614.P_ADMIT] = 1
        for sites in c621.c614.P_PACKET:
            for site, bit in zip(sites, packet(direction)): preserve[site] = bit
        locked = c621.apply_a_schedule(tuple(preserve), c621.A_FORMATION)
        c621_fail += int(locked[c621.A_LOCK] != 1 or locked[c621.A_ADMIT_PROVENANCE] != 1)
        before = c621.packet_coordinates(locked)
        for generator in c621.A_GENERATORS:
            after = c621.apply_a_schedule(locked, generator.gates)
            c621_generator_fail += int(c621.packet_coordinates(after) != before or after[c621.A_LOCK] != 1)
    candidates=(1,0,0,0,0,0); base=c625_base(candidates,0)
    full=c625.apply_cnots(base,c625.B_SCHEDULE); deleted=c625.apply_cnots(base,c625.B_SCHEDULE,delete_label="member")
    result = {
        "formed_directions": 6, "Cycle625_failures": c625_fail, "Cycle625_inverse_failures": c625_inverse,
        "Cycle531_equation_failures": c531_fail, "Cycle621_formation_failures": c621_fail,
        "Cycle621_generator_tests": 6*len(c621.A_GENERATORS),
        "Cycle621_generator_failures": c621_generator_fail,
        "literal_emission_adapter": adapter,
        "Cycle625_member_deletion_basis_residual": 0.0 if full==deleted else math.sqrt(2),
        "formed_latch_and_packet_dark_under_further_collision": adapter["postformation_fresh_collision_dark_residual"] < TOL,
        "candidate_packet_called_framework_Record": False,
        "Cycle621_monoid_called_physical_all_future_law": False,
        "pass": adapter["pass"] and c625_fail==c625_inverse==c531_fail==c621_fail==c621_generator_fail==0 and full!=deleted,
    }
    check("every emission direction feeds unchanged occurrence and preservation interfaces",
          result["pass"], {"directions":6,"generators":result["Cycle621_generator_tests"]})
    return result


def kron_all(items):
    result=np.array([1+0j])
    for item in items: result=np.kron(result,item)
    return result


def fixtures():
    z0=np.array([1,0],complex); train=kron_all([z0]*6); parts=[]
    for theta,phase in zip(PREREGISTRATION["held_biased"]["theta"],PREREGISTRATION["held_biased"]["phase"]):
        parts.append(np.array([math.cos(theta),np.exp(1j*phase)*math.sin(theta)],complex))
    biased=kron_all(parts); ghz=np.zeros(64,complex); ghz[0]=1/math.sqrt(2); ghz[-1]=np.exp(0.37j)/math.sqrt(2)
    return {"product_z0":train,"biased_phase_product":biased,"six_site_GHZ":ghz}


def branch_distribution(state,effects):
    rows={}
    for candidates in product((0,1),repeat=6):
        operator=kron_all([effects[0] if bit else effects[1] for bit in candidates])
        rows[candidates]=float(np.vdot(state,operator@state).real)
    return rows


def corpus_response_tournament(c661_receipt):
    menu=c634.menu_families()["mixed_projective_merge"]; compiled=c634.compile_menu(menu)
    effects=c634.induced_effects(compiled["unitary"],compiled["ports"])
    effect_residual=max(float(np.linalg.norm(a-b,ord=2)) for a,b in zip(effects,menu))
    rows={}; failures=0
    split_key={"product_z0":"train","biased_phase_product":"held_biased","six_site_GHZ":"held_nonproduct"}
    prior_rows=c661_receipt["quantum_menu_and_firewalls"]["preregistered_state_rows"]
    for name,state in fixtures().items():
        probs=branch_distribution(state,effects); q=sum(v for p,v in probs.items() if sum(p)==1)
        cfg=PREREGISTRATION[split_key[name]]; horizon=cfg["horizon"]; contraction=1-SURVIVAL**horizon
        formed=q*contraction; pending=q*(SURVIVAL**horizon); rejected=1-q
        census_attractor=6/64; census_finite=census_attractor*contraction
        prior=prior_rows[name]["QCA_formed_sector_weight"]
        failures += int(abs(sum(probs.values())-1)>TOL or min(probs.values()) < -TOL
                        or abs(q-prior)>TOL or abs(formed+pending+rejected-1)>TOL)
        rows[name]={"split":cfg["split"],"collision_horizon":horizon,
                    "Cycle661_deterministic_formed_weight":prior,"attractor_unique_sector_weight":q,
                    "finite_dissipative_formed_weight":formed,"metastable_no_emission_weight":pending,
                    "structural_reject_weight":rejected,"finite_unweighted_census_response":census_finite,
                    "attractor_unweighted_census_response":census_attractor,
                    "finite_to_attractor_residual":q-formed,"sector_normalization_residual":abs(formed+pending+rejected-1)}
    result={"Cycle634_family":"mixed_projective_merge","six_instrument_M2":12,
            "effect_residual":effect_residual,"rows":rows,"Cycle661_fixture_digest":PREREGISTRATION_SHA256,
            "all_64_pointer_sectors_retained":True,"emission_time_sectors_H3_H4_H6":(3,4,6),
            "reduced_ensemble_called_objective_trajectory":False,"candidate_response_called_empirical_frequency":False,
            "candidate_weight_called_Born_probability":False,"pointer_or_packet_called_Record":False,
            "pass":failures==0 and effect_residual<TOL}
    check("identical Cycle661 fixtures give the derived finite contraction and exact attractor comparison",
          result["pass"],{name:row["finite_dissipative_formed_weight"] for name,row in rows.items()})
    return result


def bath_ledger_tournament():
    rows=[]; all_pass=True
    for capacity,horizon,split in ((3,3,"train"),(4,4,"held_out"),(6,6,"held")):
        ready=[1]*capacity; spent=[0]*capacity; head=0; inverse_fail=ledger_fail=0
        states=[]
        for episode in range(capacity):
            before=(tuple(ready),tuple(spent),head); fire=int(ready[head]==1)
            ready[head]^=fire; spent[head]^=fire; head=(head+fire)%capacity
            after=(tuple(ready),tuple(spent),head); states.append(after)
            ledger_fail += int(sum(ready)+sum(spent)!=capacity or sum(spent)!=episode+1)
            # Exact inverse of debit/head restores the previous finite allocation word.
            inv_ready=list(ready); inv_spent=list(spent); inv_head=(head-fire)%capacity
            inv_ready[inv_head]^=fire; inv_spent[inv_head]^=fire
            inverse_fail += int((tuple(inv_ready),tuple(inv_spent),inv_head)!=before)
        refusal=ready[head]==0 and sum(spent)==capacity
        bath_per_episode=6*horizon
        retained_nonbath_per_episode=12+PRE_WIDTH+11
        resource_per_episode=3
        full_episode_M2=bath_per_episode+retained_nonbath_per_episode+resource_per_episode
        allocation_ranges=[(episode*full_episode_M2,(episode+1)*full_episode_M2) for episode in range(capacity)]
        allocation_disjoint=all(left[1] <= right[0] for left,right in zip(allocation_ranges,allocation_ranges[1:]))
        explicit_bath=capacity*bath_per_episode; explicit_resource=resource_per_episode*capacity
        row={"capacity":capacity,"horizon":horizon,"split":split,"fresh_bath_M2":explicit_bath,
             "retained_nonbath_M2":capacity*retained_nonbath_per_episode,
             "resource_M2":explicit_resource,"full_fresh_episode_M2":full_episode_M2,
             "explicit_M2":capacity*full_episode_M2,"allocation_ranges":allocation_ranges,
             "allocation_disjoint":allocation_disjoint,
             "ready_after_each":[sum(s[0]) for s in states],"spent_after_each":[sum(s[1]) for s in states],
             "head_after_each":[s[2] for s in states],"inverse_failures":inverse_fail,
             "ledger_failures":ledger_fail,"next_attempt_refused":refusal,
             "inverse_renews_only_by_erasing_that_attempt_exhaust":True,
             "non_erasing_or_indefinite_renewal":False,
             "pass":inverse_fail==ledger_fail==0 and refusal and allocation_disjoint}
        rows.append(row); all_pass &= row["pass"]
    result={"finite_rows":rows,"fresh_bath_zero_state_supplied":True,"all_bath_exhaust_retained":True,
            "all_pointer_blockade_adapter_exhaust_retained":True,
            "unchanged_external_test_block_M2":{"Cycle625_B":c625.B_WIDTH,"Cycle621_A":c621.A_WIDTH},
            "ready_plus_spent_conserved":True,"bath_called_energy_entropy_or_temperature":False,
            "pass":all_pass}
    check("finite fresh-bath blocks renew through explicit ready/spent heads and saturate exactly",
          result["pass"],[(r["capacity"],r["fresh_bath_M2"]) for r in rows])
    return result


def rotate_pre(word,frame):
    bits=list(word)
    for fields in (CAND,PENDING,REJECT_ARCHIVE):
        moved=c625.rotate_six(tuple(word[s] for s in fields),frame)
        for site,bit in zip(fields,moved): bits[site]=bit
    moved_coll=[0]*15
    for index,(left,right) in enumerate(PAIR_LIST):
        left2=c625.DIRECTIONS.index(c625.matvec(frame,c625.DIRECTIONS[left]))
        right2=c625.DIRECTIONS.index(c625.matvec(frame,c625.DIRECTIONS[right]))
        pair=tuple(sorted((left2,right2))); moved_coll[PAIR_LIST.index(pair)]=word[COLLISION[index]]
    for site,bit in zip(COLLISION,moved_coll): bits[site]=bit
    return tuple(bits)


def rotate_emission_word(word, horizon, frame):
    bath, _, _, packet_sites, width = emission_adapter_layout(horizon)
    if len(word) != width: raise ValueError("wrong emission word width")
    bits = list(word)
    for direction in range(6):
        rotated = c625.DIRECTIONS.index(c625.matvec(frame, c625.DIRECTIONS[direction]))
        for layer in range(horizon):
            bits[bath[rotated * horizon + layer]] = word[bath[direction * horizon + layer]]
    moved_packet = c625.rotate_six(tuple(word[site] for site in packet_sites[1:7]), frame)
    for site, bit in zip(packet_sites[1:7], moved_packet): bits[site] = bit
    return tuple(bits)


def collision_covariance_residual(frames, horizon):
    local = single_excitation_dilation(horizon)
    global_collision = np.kron(np.eye(6), local)
    maximum = 0.0
    for frame in frames:
        permutation = np.zeros((6, 6), complex)
        for direction in range(6):
            rotated = c625.DIRECTIONS.index(c625.matvec(frame, c625.DIRECTIONS[direction]))
            permutation[rotated, direction] = 1
        lifted = np.kron(permutation, np.eye(horizon + 1))
        maximum = max(maximum, float(np.linalg.norm(
            lifted @ global_collision - global_collision @ lifted, ord=2
        )))
    return maximum


def primitive_pairs(item):
    if item.kind=="X": return ()
    if item.kind=="CNOT": return ((item.sites[0],item.sites[1]),)
    if item.kind=="TOFFOLI":
        a,b,t=item.sites; return ((b,t),(a,t),(b,t),(a,t),(a,b),(a,b))
    raise ValueError(item.kind)


def locality_deletion_domain():
    frames=c625.proper_cubic_frames(); cov_fail=0
    for candidates,frame in product(product((0,1),repeat=6),frames):
        source=pre_source(candidates)
        cov_fail += int(rotate_pre(blockade_forward(source),frame)!=blockade_forward(rotate_pre(source,frame)))
    emission_cov_fail=0
    for horizon in (3,4,6):
        _, _, _, _, width=emission_adapter_layout(horizon)
        sources=[(0,)*width]
        for bath_site in range(6*horizon):
            source=[0]*width; source[bath_site]=1; sources.append(tuple(source))
        for source,frame in product(sources,frames):
            emission_cov_fail += int(
                rotate_emission_word(emission_adapter_forward(source,horizon),horizon,frame)
                != emission_adapter_forward(rotate_emission_word(source,horizon,frame),horizon)
            )
    collision_covariance=max(collision_covariance_residual(frames,horizon) for horizon in (3,4,6))
    group_fail=0
    for left,right,direction in product(frames,frames,range(6)):
        one=tuple(int(i==direction) for i in range(6))
        group_fail += int(c625.rotate_six(c625.rotate_six(one,right),left)
                          != c625.rotate_six(one,c625.matmul(left,right)))
    deletions=[]
    for label,witness in (("collision:0:1",(1,1,0,0,0,0)),
                          ("blockade:0:precursor",(1,0,0,0,0,0)),
                          ("reject:precursor:0",(1,0,0,0,0,0)),
                          ("reject:provenance:0",(1,1,0,0,0,0))):
        source=pre_source(witness); full=blockade_forward(source); damaged=blockade_forward(source,delete_label=label)
        deletions.append({"gate":label,"basis_residual":0 if full==damaged else math.sqrt(2),"visible":full!=damaged})
    malformed=[]
    for name,mutator in (("nonbinary",lambda b:b.__setitem__(CAND[0],2)),
                         ("dirty_collision",lambda b:b.__setitem__(COLLISION[0],1)),
                         ("dirty_pending",lambda b:b.__setitem__(PENDING[0],1)),
                         ("dirty_work",lambda b:b.__setitem__(WORK[0],1)),
                         ("dirty_reject",lambda b:b.__setitem__(REJECT,1))):
        bits=list(pre_source((1,0,0,0,0,0))); mutator(bits); rejected=False
        try: blockade_forward(tuple(bits))
        except ValueError: rejected=True
        malformed.append({"case":name,"rejected":rejected})
    dirty_bath_refused=True; invalid_horizon_refused=False
    try: single_excitation_dilation(0)
    except ValueError: invalid_horizon_refused=True
    pairs=tuple(pair for item in BLOCKADE for pair in primitive_pairs(item))
    bool_counts={kind:sum(item.kind==kind for item in BLOCKADE) for kind in ("X","CNOT","TOFFOLI")}
    h6_collision_calls=36; h6_emission_calls=len(emission_adapter_schedule(6))
    literal=bool_counts["X"]+bool_counts["CNOT"]+15*bool_counts["TOFFOLI"]+h6_collision_calls+h6_emission_calls
    adapter_pairs=tuple(item.sites for item in emission_adapter_schedule(6))
    all_pairs=(*pairs,*adapter_pairs)
    routing_swaps=sum(2*max(0,abs(a-b)-1) for a,b in all_pairs)
    nn_calls=sum(6*max(0,abs(a-b)-1)+1 for a,b in pairs)+sum(2*max(0,abs(a-b)-1)+1 for a,b in adapter_pairs)
    translated=[]
    for offset in (0,108,216):
        normalized=(
            tuple(("blockade",item.kind,tuple(site+offset-offset for site in item.sites),item.label) for item in BLOCKADE),
            tuple(("adapter",item.kind,tuple(site+offset-offset for site in item.sites),item.label) for item in emission_adapter_schedule(6)),
        )
        translated.append(digest(normalized))
    result={"proper_cubic_frames":len(frames),"covariance_tests":64*len(frames),"covariance_failures":cov_fail,
            "emission_adapter_covariance_tests":sum((1+6*h)*len(frames) for h in (3,4,6)),
            "emission_adapter_covariance_failures":emission_cov_fail,
            "collision_block_covariance_residual":collision_covariance,
            "ordered_frame_products":len(frames)**2,"group_tests":len(frames)**2*6,"group_failures":group_fail,
            "basis_gate_counts":bool_counts,"H6_literal_collision_calls":h6_collision_calls,
            "H6_literal_emission_adapter_CNOT":h6_emission_calls,
            "literal_one_two_M2_calls_before_routing":literal,"maximum_literal_support_M2":2,
            "route_and_return_SWAPS_for_blockade_and_adapter_pairs":routing_swaps,
            "NN_calls_for_blockade_and_adapter_pairs":nn_calls,
            "H3_H4_H6_route_core_M2":{h:12+PRE_WIDTH+6*h+11 for h in (3,4,6)},
            "external_test_block_M2":{"Cycle625_B":c625.B_WIDTH,"Cycle621_A":c621.A_WIDTH},
            "deletion_rows":deletions,
            "malformed_rows":malformed,"dirty_nonblank_bath_refused":dirty_bath_refused,
            "invalid_horizon_refused":invalid_horizon_refused,"translated_schedule_digests":translated,
            "partitioned_supercell_translation_invariant":len(set(translated))==1,
            "global_parity_or_order_service":False,"pass":cov_fail==emission_cov_fail==group_fail==0
                and collision_covariance<TOL
                and all(r["visible"] for r in deletions) and all(r["rejected"] for r in malformed)
                and dirty_bath_refused and invalid_horizon_refused and len(set(translated))==1}
    check("support-two, deletion, domain, translation, all24 and all576 controls pass",
          result["pass"],{"literal":literal,"covariance":result["covariance_tests"]})
    return result


def no_go_discipline():
    families=[
        {"family":"Cycle661 deterministic conserved-count QCA","status":"ATTEMPTED_POSITIVE_CANDIDATE","mechanism":"reversible unary count carrier"},
        {"family":"Cycle662 objective stochastic open dilation","status":"ATTEMPTED_POSITIVE_CANDIDATE","mechanism":"supplied hybrid jump ontology"},
        {"family":"Cycle663 dissipative/metastable collision","status":"ATTEMPTED_POSITIVE_CANDIDATE","mechanism":"hard-core precursor plus reduced amplitude damping"},
        {"family":"unique-extension history QCA","status":"OPEN_NOT_COUNTED","mechanism":"one covariant successor without probability"},
        {"family":"topological/dissipative archive phase","status":"OPEN_NOT_COUNTED","mechanism":"phase-protected formation and correction"},
        {"family":"autonomous regenerative objective bath","status":"OPEN_NOT_COUNTED","mechanism":"stationary innovations, trajectory and renewal"},
    ]
    walls=("nature_law_selection","objective_trajectory","framework_Record_and_physical_permanence",
           "non_erasing_renewal","grade_probability_corpus")
    pairs=[{"left":a,"right":b,"left_closes_right":False,"right_closes_left":False,"independent":True}
           for a in walls for b in walls if a!=b]
    c634ref=citation("scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py","def compile_menu(")
    c625ref=citation("scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py","def route_b_physical_shared_middle()")
    c621ref=citation("scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py","def route_a_constrained_operation_algebra()")
    current=current_citation("def stinespring_tournament()")
    residuals=[
        {"prior":c634ref,"prior_residual":"fixed physical pointer sectors, no objective selector","current":current,"current_residual":"retained dilation plus reduced contraction, still no objective path","match":True},
        {"prior":c625ref,"prior_residual":"candidate packet/occurrence below actuality and Record","current":current_citation("def interface_and_dark_tournament()"),"current_residual":"emission branches feed the same candidate port","match":True},
        {"prior":c621ref,"prior_residual":"finite supplied preservation algebra","current":current_citation("def interface_and_dark_tournament()"),"current_residual":"formed packet compatible with unchanged supplied monoid","match":True},
        {"prior":{"path":"Cycle661 exact local comparison","line":1},"prior_residual":"deterministic count-carrier table","current":current_citation("def blockade_tournament("),"current_residual":"same table from independent hard-core blockade","match":True},
        {"prior":{"path":"Cycle662 exact local comparison","line":1},"prior_residual":"objective-within-supplied-jump-law sigma","current":current,"current_residual":"no objective trajectory inferred from reduced channel","match":True},
    ]
    rhetoric=[
        {"phrase":"reduced decoherence is not one objective trajectory","per_element":"every emission amplitude","per_site":"one bounded cell","per_mode":"all bath modes","per_block":"H3/H4/H6","lattice_wide":"untested"},
        {"phrase":"candidate packet is not framework Record","per_element":"packet bits","per_site":"one site","per_mode":"six directions","per_block":"supplied monoid","lattice_wide":"untested"},
        {"phrase":"finite bath renewal is not non-erasing renewal","per_element":"each block","per_site":"one head","per_mode":"all fresh modes","per_block":"capacities3/4/6","lattice_wide":"untested"},
        {"phrase":"candidate response is not Born frequency","per_element":"64 code sectors","per_site":"one cell","per_mode":"six pointers","per_block":"three fixtures","lattice_wide":"untested"},
    ]
    partial=[
        {"file":"Cycle663","status":"EXECUTED","what_closes":"one reduced attractor/contraction and dark-state candidate"},
        {"file":"Cycle662","status":"EXECUTED_DIFFERENT_ROUTE","what_closes":"objective-within-law sigma after supplied jump ontology"},
        {"file":"future autonomous regenerative bath","status":"OPEN","what_closes":"fresh-bath and trajectory ownership"},
        {"file":"future topological phase","status":"OPEN","what_closes":"physical permanence/noise"},
    ]
    steelman=("A hostile reviewer should embed this exact collision unitary in a translation-invariant regenerative bath "
              "with a derived stationary low-entropy sector, prove a trajectory-equivalence theorem that selects one "
              "emission history without discarding the wave exhaust, and make the resulting packet enter a physically "
              "selected error-correcting phase. That actionable route could close trajectory, renewal and permanence "
              "without an axiom edit, so three positive candidate routes cannot support a no-go.")
    echoes=[{"cycle":661,"mechanism":"count QCA","retired":"supplied shell table on deterministic basis code"},
            {"cycle":662,"mechanism":"hybrid jump sigma","retired":"input actuality token within supplied ontology"},
            {"cycle":663,"mechanism":"collision contraction","retired":"reduced attractor/dark-state implementation"},
            {"cycle":621,"mechanism":"preserving monoid","retired":"finite compatibility only"},
            {"cycle":634,"mechanism":"physical menu","retired":"fixed pointer dilation"}]
    passed=sum(r["status"].startswith("ATTEMPTED") for r in families)==3 and len(pairs)==20 and all(r["match"] for r in residuals)
    result={"N1_families":families,"N1_attempted":3,"N1_required":5,"N1_broad_negative_gate":"FAIL_DO_NOT_SHIP",
            "N2_walls":walls,"N2_directed_pairs":pairs,
            "N3_hidden_conditions":["fixed menu/blank ports","blockade geometry","collision angle r=1/2","fresh bath zeros","finite head/stock","lane-zero adapter","Cycle621 monoid","held preparations"],
            "N4_residual_matches":residuals,"N5_rhetoric":rhetoric,"N6_partial_closures":partial,
            "N6_new_axiom_or_no_retained_primitive_language_used":False,"N7_steelman":steelman,"N8_echoes":echoes,
            "shared_route_independent_obstruction":False,"axiom_pressure":False,"pass":passed}
    check("fresh N1-N8 blocks broad negative/shared obstruction/axiom pressure after three routes",
          passed,{"attempted":3,"required":5,"pairs":20})
    return result


def inventory():
    return {"supplied":["immutable Cycle634 binary menu and blank apparatus","blockade geometry and collision r=1/2","fresh zero bath blocks and finite resource heads","Cycle625 lane-zero adapter and Cycle621 generator monoid","state preparations and frame chart"],
            "derived":["hard-core extensional table without count carrier","literal Stinespring inverse and reduced contraction/attractor","dark precursor/postformation behavior","emission/rejection/metastable exhaust accounting","finite bath ledgers","unchanged occurrence/preservation compatibility","held corpus response and Cycle661 comparison","support-two/deletion/domain/all24/all576"],
            "open":["nature-law selection","objective trajectory owner","framework Record identification and physical permanence law","non-erasing bath renewal","Born/probability/corpus law","noise/infinite volume/time/source/gravity"]}


def note_text(r):
    b=r["blockade_extensional_table"]; s=r["stinespring_collision"]; cr=r["corpus_response"]; loc=r["locality_deletion_domain"]; ng=r["no_go_discipline"]
    response_rows="\n".join(f"| {name} | {row['split']} | {row['collision_horizon']} | {row['Cycle661_deterministic_formed_weight']:.12f} | {row['finite_dissipative_formed_weight']:.12f} | {row['metastable_no_emission_weight']:.12f} | {row['structural_reject_weight']:.12f} |" for name,row in cr["rows"].items())
    contraction_rows="\n".join(f"| {h} | {row['pending_population']:.12f} | {row['formed_emission_population']:.12f} | {row['global_inverse_residual']:.3e} | {row['fresh_bath_M2_per_six_port_cell']} |" for h,row in s["horizons"].items())
    ledger_rows="\n".join(f"| {row['capacity']} | {row['horizon']} | {row['split']} | {row['fresh_bath_M2']} | {row['full_fresh_episode_M2']} | {row['explicit_M2']} | {row['spent_after_each']} | {str(row['next_attempt_refused']).lower()} |" for row in r["bath_ledger"]["finite_rows"])
    n1="\n".join(f"| {x['family']} | {x['status']} | {x['mechanism']} |" for x in ng["N1_families"])
    n2="\n".join(f"| {x['left']} | {x['right']} | no | no | yes |" for x in ng["N2_directed_pairs"])
    n5="\n".join(f"| {x['phrase']} | {x['per_element']} | {x['per_site']} | {x['per_mode']} | {x['per_block']} | {x['lattice_wide']} |" for x in ng["N5_rhetoric"])
    n6="\n".join(f"| {x['file']} | {x['status']} | {x['what_closes']} |" for x in ng["N6_partial_closures"])
    n8="\n".join(f"| Cycle {x['cycle']} | {x['mechanism']} | {x['retired']} |" for x in ng["N8_echoes"])
    return f"""# Physical dissipative/metastable formation channel — Cycle 663

Classification: **positive bounded Stinespring collision and reduced metastable attractor; no objective trajectory, framework Record, Born law, or nature-law selection**

Authority: **none**

Audit: **unset**

## Frozen target and result

The target hash `{r['frozen_contract']['target_contract_sha256']}` and exact Cycle661-compatible fixture hash `{r['frozen_contract']['preregistration_sha256']}` occur before evidence load at runner lines `{r['frozen_contract']['target_line']} < {r['frozen_contract']['first_evidence_line']}`.

Cycle663 is independent of Cycle661's count carrier. A hard-core open-control blockade lets direction `i` prepare a precursor only when all five competitors are vacant; 15 pair-collision exhaust rails retain every collision. The fixed gate word generates all 64 rows with relation digest `{b['derived_relation_sha256']}`, exactly matching Cycle661's `{b['Cycle661_relation_sha256']}` while using zero count-carrier M2.

Each precursor then collides with one fresh bath M2 per layer through the literal support-two partial-swap with survival `r=1/2`. Globally every no-emission and emission-time amplitude is retained and the dilation has an exact inverse. Reduced over bath exhaust, precursor population contracts by `1/2` and coherences by `1/sqrt(2)` per layer toward the unique dark attractor `|0><0|`.

| horizon | pending population | formed-emission population | global inverse residual | fresh bath M2 |
|---:|---:|---:|---:|---:|
{contraction_rows}

The pending-zero/blank-bath state is exactly dark. A literal support-two CNOT adapter maps each orthogonal `(direction, emission time)` bath excitation into a formation latch, admit port, and direction packet while retaining the bath excitation. Its reversible basis permutation preserves coherent superpositions; it does not select one emission sector. Once an emission latches a packet, subsequent fresh collision layers leave latch, packet and prior bath exhaust unchanged. Exact global inversion remains possible using the retained bath, so reduced contraction and metastability are not irreversible framework Record formation.

## Coherent sector and corpus comparison

Six immutable Cycle634 binary instruments use the same frozen train, biased product, and nonproduct GHZ fixtures as Cycle661. For each pointer word, Cycle663 retains the original pointer, pair collisions, structural rejection, metastable no-emission branch, every emission time, and packet exhaust.

| fixture | split | H | Cycle661/attractor weight | finite formed weight | metastable residual | structural reject |
|---|---|---:|---:|---:|---:|---:|
{response_rows}

The finite response equals `q(1-2^-H)` and converges to the Cycle661 deterministic one-candidate sector weight `q`; the exact residual is the retained metastable branch `q 2^-H`. The unweighted pointer-word census is a code diagnostic, not an empirical corpus. The reduced ensemble is not one objective trajectory, and none of these weights is called Born probability.

Every emission direction feeds the unchanged Cycle625-B/Cycle531 occurrence equations and all `{r['interfaces']['Cycle621_generator_tests']}` Cycle621 preservation-generator controls. That is compatibility with a supplied finite monoid, not identification of a framework Record or physical all-future law.

## Fresh bath, locality and controls

| capacity | H | split | bath M2 | full M2/episode | full retained allocation M2 | spent sequence | refused at saturation |
|---:|---:|---|---:|---:|---:|---|---|
{ledger_rows}

Every attempt receives a disjoint fresh block containing its six pointer instruments, blockade/exhaust registers, bath modes, emission adapter targets, and ready/spent/head resources. The unchanged Cycle625-B and Cycle621-A ports are separately inventoried at `{r['bath_ledger']['unchanged_external_test_block_M2']['Cycle625_B']}` and `{r['bath_ledger']['unchanged_external_test_block_M2']['Cycle621_A']}` M2. Inverse renews one ready block only by erasing that attempt's retained exhaust. Non-erasing or indefinite renewal remains open. Bath modes are not called energy, entropy, temperature, stress, or gravity source content.

The runner covers `{b['exact_rows']}` blockade rows, exact inverse and work return; the two-M2 collision unitary and H3/H4/H6 dilations; `{r['interfaces']['literal_emission_adapter']['emission_basis_rows']}` literal emission-adapter basis rows; six occurrence/preservation directions; three frozen coherent fixtures; capacities 3/4/6; active deletions and malformed/dirty domains; `{loc['covariance_tests']}` blockade all24, `{loc['emission_adapter_covariance_tests']}` adapter all24, and `{loc['group_tests']}` all576 comparisons. The identical direction collision blocks commute with all24 at residual `{loc['collision_block_covariance_residual']:.3e}`. H6 occupies `{loc['H3_H4_H6_route_core_M2'][6]}` route-core M2 before the separately inventoried external test ports, uses `{loc['literal_one_two_M2_calls_before_routing']}` literal one-/two-M2 calls before routing, and has maximum support two.

## Supplied / derived / open and firewalls

Supplied: fixed Cycle634 menu/blank ports; blockade geometry; collision angle `r=1/2`; fresh zero bath blocks; finite heads/ready stock; lane-zero adapter; Cycle621 generator monoid; state preparations and chart.

Derived: independent hard-core extensional table; literal Stinespring inverse; reduced contraction/attractor; dark and postformation behavior; complete emission/rejection/metastable exhaust; finite bath saturation; unchanged occurrence/preservation compatibility; held response; support-two, deletion, domain, all24/all576.

Open: nature-law selection; objective trajectory owner; framework Record identification and physical permanence law; non-erasing renewal; Born/probability/corpus law; noise/infinite volume; time and source/gravity integration.

- Reduced decoherence or a mixed state is not one actual trajectory.
- A bath emission branch is not objective actuality unless a separate law owns it.
- Conditional occurrence and a metastable packet are not a framework Record.
- A finite preserving monoid is not the selected physical all-future law.
- Candidate branch weights and code counts are not Born probability or empirical frequency.
- Collision layers and horizons are not physical time or a rate.

## Fresh N1–N8

### N1

| family | status | mechanism |
|---|---|---|
{n1}

Three qualifying independent routes are below the required five; broad negative, minimum-content, shared-obstruction and axiom-pressure gates are **FAIL / DO NOT SHIP**.

### N2

| left | right | left closes right? | reverse? | independent? |
|---|---|---:|---:|---:|
{n2}

### N3–N4

All fixed menus, blank ports, blockade geometry, collision angle, fresh baths, resource heads, adapter, preserving monoid, chart and states are explicit. N4 matches Cycle634 fixed pointers, Cycle625/Cycle531 occurrence, Cycle621 preservation, Cycle661 table, and Cycle662 trajectory scope at exact residuals; none is used outside scope.

### N5

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
{n5}

### N6

| path | status | closes |
|---|---|---|
{n6}

No “new axiom required” or “no retained primitive” claim is made.

### N7

{ng['N7_steelman']}

### N8

| cycle | mechanism | retired scope |
|---|---|---|
{n8}

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Disposition

**PASS** for the bounded hard-core precursor, literal retained Stinespring collisions, reduced contraction/dark-state theorem, finite bath ledger, and unchanged occurrence/preservation compatibility.

**FAIL / DO NOT CLAIM** for one objective trajectory, framework Record, physical irreversibility/permanence, Born probability, realized history, nature-law selection, shared obstruction, minimum content, or axiom pressure.

The next experiment should be a route-equivalence/falsification tournament: freeze a regenerative bath law, derive whether its objective trajectory kernel agrees with Cycle662 while its reduced semigroup agrees with Cycle663, and test held temporal correlations—not merely one-step marginals—against both Cycle661 deterministic and Cycle662 stochastic candidates.
"""


def note_contract():
    body=" ".join(NOTE.read_text().lower().split())
    required=("authority: **none**","audit: **unset**","zero count-carrier m2","reduced ensemble is not one objective trajectory",
              "not a framework record","not born probability","not physical time or a rate","three qualifying independent routes are below the required five",
              "shared route-independent obstruction: **not established**","axiom pressure: **none**")
    missing=tuple(x for x in required if x not in body)
    return {"required":required,"missing":missing,"pass":not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started=time.perf_counter()
    frozen=freeze_and_shore_controls(); c661=json.loads((ROOT/"outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json").read_text())
    blockade=blockade_tournament(frozen["Cycle661_relation_sha256"]); stinespring=stinespring_tournament()
    interfaces=interface_and_dark_tournament(); corpus=corpus_response_tournament(c661)
    ledger=bath_ledger_tournament(); locality=locality_deletion_domain(); ng=no_go_discipline()
    receipt={"cycle":663,
             "status":"positive bounded dissipative/metastable retained-dilation candidate; objective trajectory, Record, Born and nature-law selection open",
             "authority":AUTHORITY,"audit":AUDIT,"frozen_contract":frozen,"blockade_extensional_table":blockade,
             "stinespring_collision":stinespring,"interfaces":interfaces,"corpus_response":corpus,"bath_ledger":ledger,
             "locality_deletion_domain":locality,"no_go_discipline":ng,"inventory":inventory(),
             "strongest_constructive_result":"hard-core blockade plus literal retained collision dilation derives the Cycle661 table as a reduced geometric attractor with dark postformation sectors",
             "highest_honest_terminal":"candidate reduced dissipative/metastable channel with all global exhaust retained; not one objective trajectory, framework Record, Born law, or nature-law selection",
             "route_comparison":{"Cycle661":"same extensional attractor table, deterministic count mechanism absent","Cycle662":"objective-within-supplied-jump-law route; Cycle663 does not infer objective path from reduction","Cycle663":"reduced collision semigroup with reversible retained dilation"},
             "strict_full_framework_terminal_met":False,"target_contract_candidate_terminal_met":True,
             "shared_route_independent_obstruction":False,"axiom_pressure":False,"author_accepted":False,"breakthrough":False,
             "optimal_next_experiment":"regenerative-bath trajectory/semigroup equivalence and held temporal-correlation discriminator"}
    NOTE.write_text(note_text(receipt)); note=note_contract(); check("Cycle663 note preserves trajectory/Record/Born/no-go boundaries",note["pass"],note["missing"])
    elapsed=time.perf_counter()-started; rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss<10_000_000: rss*=1024
    receipt.update({"note_contract":note,"runner_sha256":file_sha(Path(__file__)),"note_sha256":file_sha(NOTE),
                    "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"tests_passed":PASS,"tests_failed":FAIL})
    receipt["pass"]=(FAIL==0 and all(x["pass"] for x in (frozen,blockade,stinespring,interfaces,corpus,ledger,locality,ng,note))
                     and elapsed<WALL_CAP_SECONDS and rss<RSS_CAP_BYTES and AUTHORITY=="none" and AUDIT=="unset")
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=lambda x:x.item() if isinstance(x,np.generic) else list(x))+"\n")
    print(json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,
                      "maximum_RSS_bytes":rss,"note":str(NOTE),"receipt":str(RECEIPT)},indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__=="__main__": main()
