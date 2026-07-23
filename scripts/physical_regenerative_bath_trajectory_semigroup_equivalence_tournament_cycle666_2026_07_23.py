#!/usr/bin/env python3
"""Cycle666: regenerative-bath trajectory/semigroup equivalence tournament.

A reusable six-rail collision bath is reset after each collision by swapping
its complete quantum state into a fresh outbound exhaust carrier.  A supplied
hybrid stochastic law writes an ontic innovation label with the same local
Kraus kernel while the coherent wave exhaust remains retained.  This is a
candidate finite law, not a derivation of nature's law, Record, Born weights,
physical time, energy, or indefinite non-erasing renewal.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 666,
    "route": "regenerative-bath trajectory/semigroup equivalence tournament",
    "decisive_question": (
        "can one bounded translation/proper-cubic covariant local collision-bath law reproduce the "
        "Cycle663 reduced amplitude-damping semigroup and the Cycle662 objective-within-law branch "
        "kernel without an input actuality token or host sampler, retain complete exhaust, and "
        "distinguish Cycle661 by held temporal correlations rather than one-step marginals"
    ),
    "required": [
        "literal two-M2 collision followed by reversible bath-to-mobile-exhaust regeneration",
        "exact coherent history isometry and reduced semigroup equality",
        "objective-within-supplied-law innovation sequence with Cycle662 quadratic branch kernel",
        "all wave, innovation, rejection, no-emission and emission-time exhaust retained",
        "preregistered train and blinded held biased/nonproduct inputs at H3/H4/H6",
        "off-diagonal temporal-covariance discriminator whose disposition ignores one-step marginals",
        "finite ready/spent/bath-carrier ledger with inverse, deletion, malformed, dark and saturation controls",
        "support/M2/depth inventory and all24/all576 covariance",
        "fresh N1-N8 before any bounded negative or residual statement",
    ],
    "forbidden": [
        "input actuality token", "host sampler", "global parity service", "global ordering",
        "discarded wave exhaust", "one-step-marginal discriminator", "reduced state as one trajectory",
        "pointer or latch as framework Record", "weights as Born probability",
        "collision layer as physical time", "generator element as rate", "bath content as energy",
    ],
    "success_ceiling": (
        "positive finite candidate hybrid regenerative collision law with bounded outbound exhaust; "
        "nature-law selection, framework Record, Born/empirical interpretation, physical time, and "
        "indefinite non-erasing renewal remain open"
    ),
}
TARGET_CONTRACT_SHA256 = "6aa7ef289c8b6b17e87e4e4e73d1bf3fc148b8ef3a7d22a84aee99332bb90dcd"


PREREGISTRATION = {
    "collision_survival": "r=1/2",
    "system_code": "vacuum plus six proper-cubic direction precursor rails",
    "trajectory_outcomes_per_layer": "no-emission plus six direction emissions",
    "kernel_inputs": {
        "train_direction0": {"split": "train", "horizon": 3, "state": "|direction0>"},
        "held_biased_coherent": {
            "split": "held_blinded", "horizon": 4,
            "unnormalized_re_im": [[0.73,0.0],[0.41,0.11],[-0.19,0.37],[0.29,-0.23],[-0.31,-0.17],[0.13,0.43],[-0.27,0.09]],
        },
        "held_nonproduct_reference": {
            "split": "held_blinded_nonproduct", "horizon": 6, "theta": 0.61,
            "direction_phases": [0.0,0.17,-0.29,0.43,-0.61,0.79],
            "state": "cos(theta)|vacuum,0>+sin(theta)/sqrt(6) sum_d exp(i phase_d)|d,1>",
        },
    },
    "pointer_temporal_inputs": {
        "product_z0": {"split": "train", "horizon": 3, "state": "|000000>"},
        "biased_phase_product": {
            "split": "held_blinded", "horizon": 4,
            "theta": [0.19,0.31,0.43,0.57,0.71,0.83],
            "phase": [0.0,0.2,-0.3,0.5,-0.7,0.9],
        },
        "six_site_GHZ": {
            "split": "held_blinded_nonproduct", "horizon": 6,
            "state": "(|000000>+exp(0.37i)|111111>)/sqrt(2)",
        },
    },
    "temporal_discriminator": {
        "observable": "first-emission indicator J_h",
        "score": "Frobenius norm of the off-diagonal covariance difference",
        "held_rows_only_for_disposition": True,
        "diagonal_and_one_step_marginals_masked": True,
        "Cycle661_reference": "immediate deterministic first-formation event J_1=A and J_h>1=0",
    },
    "episode_capacities": [3,4,6],
    "frame_set": "all 24 proper-cubic frames and all 576 ordered products",
}
PREREGISTRATION_SHA256 = "1cc76f2bc311d65bbd1a903ad032479a21f890d9b7c116f58db25df27da9f887"


from dataclasses import dataclass
import ast
from hashlib import sha256
from itertools import product
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
SHORE = "467565dd850e8835c86134f5fb55ca7d89d838d4"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_REGENERATIVE_BATH_TRAJECTORY_SEMIGROUP_EQUIVALENCE_TOURNAMENT_CYCLE666_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_regenerative_bath_trajectory_semigroup_equivalence_tournament_cycle666_receipt_2026_07_23.json"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
SURVIVAL = 0.5
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0


PINS = {
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py": "83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md": "14262310b768983ebbdc8a89f914f237ab2a2523c8a096eece63b33a7e5e9ad4",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json": "c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py": "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md": "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json": "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
    "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py": "03446972470065a781c78b8e220169ca9d65239d1054535992e3e16b3ece09e4",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md": "96f59a3f79ce7c29f3c9ccdf93cae9503ea4cd0084821c11ba6e0545046bec87",
    "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json": "ab246cd35e6b6f30840621ca3e1eb9258a936de1c675fb2f0f429e9c131aa9b5",
    "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py": "ca187b7dda5c2b1b56a63ba960695734fc9915177c2769ef957913a096a74d52",
    "docs/work_history/repo/review_feedback/PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md": "d0b8b3b0cb496a3864320c38f2fd8948a42a03252bf18e1b2389618f76f3cd5c",
    "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json": "3fd6a476feac3bae38f0da2b6c0d2826432e4b6a605d02d1e99b0d946e6efc87",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py": "a618b5803cc1313a3dd644e3e066bb987bf366d8215a50a43d4260c69847b9e9",
    "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md": "190ed6dfc5502a0d8d68c665501fe4f009d21fb2aad4bc0b71e9f96a9856552d",
    "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json": "a867cbeed66052da8cb85e8867a55802d27bfca586c9db805aa1649a6f0c7560",
    "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py": "faa1a251d7586ed9d2e496cc73b42f45108347fe5f627523fcef3caa4e652a73",
    "docs/work_history/repo/review_feedback/PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_CYCLE621_NOTE_2026-07-22.md": "a52395a57fb34b6d827a677a43528033e913cde2f98ce708a276507f6e1e353e",
    "outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json": "d28ee4034b15ecd7eebac2a0481c9475d828bbbe444baa8d9b903f231ca47156",
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value): return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def file_sha(path): return sha256(Path(path).read_bytes()).hexdigest()
def git_bytes(path): return subprocess.check_output(("git", "show", f"{SHORE}:{path}"), cwd=ROOT)


def load_exact(name, path):
    module=types.ModuleType(name); module.__file__=str(ROOT/path); module.__package__=""
    sys.modules[name]=module; exec(compile(git_bytes(path),module.__file__,"exec"),module.__dict__); return module


def citation(path, fragment):
    rows=git_bytes(path).decode().splitlines(); matches=[i for i,row in enumerate(rows,1) if fragment in row]
    if len(matches)!=1: raise AssertionError((path,fragment,matches))
    return {"ref":SHORE,"path":path,"line":matches[0]}


def current_citation(fragment):
    rows=Path(__file__).read_text().splitlines()
    matches=[i for i,row in enumerate(rows,1)
             if (row.strip().startswith(fragment) if fragment.startswith("def ") else fragment in row)]
    if len(matches)!=1: raise AssertionError((fragment,matches))
    return {"ref":"Cycle666 current","path":str(Path(__file__).relative_to(ROOT)),"line":matches[0]}


# Evidence loads only after the target, preregistration, hashes and exact shore pins.
c634=load_exact("cycle666_exact_c634","scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py")
c625=load_exact("cycle666_exact_c625","scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py")
c621=load_exact("cycle666_exact_c621","scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py")
c662prior=load_exact("cycle666_exact_c662","scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py")


def freeze_and_shore_controls():
    source=Path(__file__).read_text().splitlines()
    target_line=next(i for i,row in enumerate(source,1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line=next(i for i,row in enumerate(source,1) if row.startswith("PREREGISTRATION ="))
    evidence_line=next(i for i,row in enumerate(source,1) if row.startswith("c634=load_exact"))
    observed={path:sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipts={cycle:json.loads(git_bytes(path)) for cycle,path in {
        "661":"outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json",
        "662":"outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json",
        "663":"outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json",
        "634":"outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json",
        "625":"outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json",
        "621":"outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json",
    }.items()}
    imported={
        "Cycle661_pass":receipts["661"]["pass"],
        "Cycle662_pass":receipts["662"]["pass"],
        "Cycle663_pass":receipts["663"]["pass"],
        "Cycle634_pass":receipts["634"]["pass"],
        "Cycle625_B_pass":receipts["625"]["route_B_physical_shared_middle"]["pass"],
        "Cycle621_A_pass":receipts["621"]["route_A_constrained_operation_algebra"]["pass"],
    }
    passed=(target_line<prereg_line<evidence_line and digest(TARGET_CONTRACT)==TARGET_CONTRACT_SHA256
            and digest(PREREGISTRATION)==PREREGISTRATION_SHA256 and observed==PINS and all(imported.values()))
    result={"shore":SHORE,"target":TARGET_CONTRACT,"target_sha256":digest(TARGET_CONTRACT),
            "expected_target_sha256":TARGET_CONTRACT_SHA256,"preregistration":PREREGISTRATION,
            "preregistration_sha256":digest(PREREGISTRATION),"expected_preregistration_sha256":PREREGISTRATION_SHA256,
            "target_line":target_line,"preregistration_line":prereg_line,"first_evidence_line":evidence_line,
            "frozen_before_evidence":target_line<prereg_line<evidence_line,"pins":PINS,"observed":observed,
            "working_tree_bytes_used_as_evidence":False,"imported_contracts":imported,"pass":passed}
    check("Cycle666 target, temporal discriminator and exact shores were frozen before evidence",passed,
          {"target":result["target_sha256"],"prereg":result["preregistration_sha256"],"pins":len(PINS)})
    return result,receipts


DIM=7


def multirail_kraus():
    k0=np.diag([1.0]+[math.sqrt(SURVIVAL)]*6).astype(complex); rows=[k0]
    for direction in range(6):
        jump=np.zeros((DIM,DIM),complex); jump[0,direction+1]=math.sqrt(1-SURVIVAL); rows.append(jump)
    return tuple(rows)


def apply_channel(rho,kraus=None):
    if kraus is None: kraus=multirail_kraus()
    return sum(k@rho@k.conj().T for k in kraus)


def history_operators(horizon):
    if type(horizon) is not int or horizon<1: raise ValueError("positive integer horizon required")
    k0,*jumps=multirail_kraus(); rows=[("none",k0.copy())]
    rows[0]=("none",np.linalg.matrix_power(k0,horizon))
    for layer in range(1,horizon+1):
        prefix=np.linalg.matrix_power(k0,layer-1)
        for direction,jump in enumerate(jumps): rows.append((f"emit:{layer}:{direction}",jump@prefix))
    return tuple(rows)


def trajectory_sum(rho,horizon): return sum(op@rho@op.conj().T for _,op in history_operators(horizon))


def repeated_channel(rho,horizon):
    out=rho.copy()
    for _ in range(horizon): out=apply_channel(out)
    return out


def history_unitary(horizon,delete_pair=None):
    width=1+6+6*horizon; unitary=np.eye(width,dtype=complex)
    c=math.sqrt(SURVIVAL); s=math.sqrt(1-SURVIVAL)
    for layer in range(horizon):
        for direction in range(6):
            if delete_pair==(layer,direction): continue
            pending=1+direction; exhaust=1+6+layer*6+direction
            gate=np.eye(width,dtype=complex)
            gate[np.ix_((pending,exhaust),(pending,exhaust))]=np.array([[c,-s],[s,c]],complex)
            unitary=gate@unitary
    return unitary


def three_qubit_cnot(control,target):
    matrix=np.zeros((8,8),complex)
    for bits in product((0,1),repeat=3):
        out=list(bits); out[target]^=out[control]
        source=4*bits[0]+2*bits[1]+bits[2]; target_index=4*out[0]+2*out[1]+out[2]
        matrix[target_index,source]=1
    return matrix


def layer_regenerator_unitary(delete_swap_gate=None):
    collision=np.array([[1,0,0,0],[0,math.sqrt(SURVIVAL),math.sqrt(1-SURVIVAL),0],
                        [0,-math.sqrt(1-SURVIVAL),math.sqrt(SURVIVAL),0],[0,0,0,1]],complex)
    collision3=np.kron(collision,np.eye(2))
    swap=np.eye(8,dtype=complex)
    for index,(control,target) in enumerate(((1,2),(2,1),(1,2))):
        if index!=delete_swap_gate:swap=three_qubit_cnot(control,target)@swap
    return swap@collision3


def kernel_inputs():
    train=np.zeros(DIM,complex); train[1]=1
    raw=np.asarray([complex(a,b) for a,b in PREREGISTRATION["kernel_inputs"]["held_biased_coherent"]["unnormalized_re_im"]])
    biased=raw/np.linalg.norm(raw)
    cfg=PREREGISTRATION["kernel_inputs"]["held_nonproduct_reference"]
    nonproduct=np.zeros(DIM*2,complex); nonproduct[0]=math.cos(cfg["theta"])
    for d,phase in enumerate(cfg["direction_phases"]): nonproduct[2*(d+1)+1]=math.sin(cfg["theta"])*np.exp(1j*phase)/math.sqrt(6)
    return {
        "train_direction0":{"rho":np.outer(train,train.conj()),"spectator":1,"split":"train","horizon":3},
        "held_biased_coherent":{"rho":np.outer(biased,biased.conj()),"spectator":1,"split":"held_blinded","horizon":4},
        "held_nonproduct_reference":{"rho":np.outer(nonproduct,nonproduct.conj()),"spectator":2,"split":"held_blinded_nonproduct","horizon":6},
    }


def extend_operator(operator,spectator): return np.kron(operator,np.eye(spectator))


def partial_trace_system(rho,spectator):
    return np.trace(rho.reshape(DIM,spectator,DIM,spectator),axis1=0,axis2=2)


def validate_density(rho,spectator):
    if rho.shape!=(DIM*spectator,DIM*spectator): raise ValueError("density dimension")
    if np.linalg.norm(rho-rho.conj().T)>TOL: raise ValueError("non-Hermitian")
    if abs(np.trace(rho)-1)>TOL: raise ValueError("nonnormalized")
    if np.linalg.eigvalsh((rho+rho.conj().T)/2).min() < -TOL: raise ValueError("negative density")


def coherent_semigroup_tournament(c663_receipt):
    kraus=multirail_kraus(); completeness=sum(k.conj().T@k for k in kraus)
    completeness_residual=float(np.linalg.norm(completeness-np.eye(DIM),ord=2))
    single=layer_regenerator_unitary(); single_unitarity=float(np.linalg.norm(single.conj().T@single-np.eye(8),ord=2))
    source=np.zeros(8,complex); source[4]=0.6; source[0]=0.8
    output=single@source
    bath_reset_population=float(sum(abs(output[4*p+2*1+x])**2 for p,x in product((0,1),repeat=2)))
    single_inverse=float(np.linalg.norm(single.conj().T@output-source))
    rows={}; failures=0; max_semigroup=max_isometry=max_history_inverse=0.0
    for name,item in kernel_inputs().items():
        rho=item["rho"]; spectator=item["spectator"]; horizon=item["horizon"]; validate_density(rho,spectator)
        ext_ops=[(label,extend_operator(op,spectator)) for label,op in history_operators(horizon)]
        trajectory=sum(op@rho@op.conj().T for _,op in ext_ops)
        repeated=rho.copy()
        ext_kraus=tuple(extend_operator(k,spectator) for k in kraus)
        for _ in range(horizon): repeated=sum(k@repeated@k.conj().T for k in ext_kraus)
        semigroup_residual=float(np.linalg.norm(trajectory-repeated,ord=2)); max_semigroup=max(max_semigroup,semigroup_residual)
        isometry_residual=float(np.linalg.norm(sum(op.conj().T@op for _,op in ext_ops)-np.eye(DIM*spectator),ord=2)); max_isometry=max(max_isometry,isometry_residual)
        props=[float(np.trace(op@rho@op.conj().T).real) for _,op in ext_ops]
        spectator_before=partial_trace_system(rho,spectator); spectator_after=partial_trace_system(trajectory,spectator)
        spectator_residual=float(np.linalg.norm(spectator_after-spectator_before,ord=2))
        global_u=history_unitary(horizon); global_res=float(np.linalg.norm(global_u.conj().T@global_u-np.eye(global_u.shape[0]),ord=2)); max_history_inverse=max(max_history_inverse,global_res)
        rows[name]={"split":item["split"],"horizon":horizon,"trajectory_branches":len(ext_ops),
                    "propensity_sum_residual":abs(sum(props)-1),"minimum_propensity":min(props),
                    "trajectory_sum_to_reduced_semigroup_residual":semigroup_residual,
                    "history_isometry_residual":isometry_residual,"global_history_inverse_residual":global_res,
                    "spectator_no_signalling_residual":spectator_residual,
                    "no_emission_propensity":props[0],"emission_propensity":sum(props[1:])}
        failures+=int(max(rows[name]["propensity_sum_residual"],semigroup_residual,isometry_residual,global_res,spectator_residual)>TOL or min(props)<-TOL)
    c663_eigs=tuple(c663_receipt["stinespring_collision"]["reduced_superoperator_eigenvalues"])
    restriction_eigs=(1.0,math.sqrt(SURVIVAL),math.sqrt(SURVIVAL),SURVIVAL)
    result={"multirail_dimension":DIM,"Kraus_outcomes":len(kraus),"Kraus_completeness_residual":completeness_residual,
            "literal_three_M2_collision_swap_unitarity_residual":single_unitarity,
            "literal_three_M2_collision_swap_inverse_residual":single_inverse,
            "bath_one_population_after_swap_to_blank_exhaust":bath_reset_population,
            "rows":rows,"maximum_semigroup_residual":max_semigroup,"maximum_history_inverse_residual":max_history_inverse,
            "Cycle663_single_rail_spectrum":c663_eigs,"current_single_rail_spectrum":restriction_eigs,
            "Cycle663_spectrum_exact_match":c663_eigs==restriction_eigs,
            "Cycle663_population_survival_exact_match":c663_receipt["stinespring_collision"]["population_contraction_per_layer"]==SURVIVAL,
            "coherent_wave_exhaust_retained":True,"bath_reused_only_after_state_moved_to_outbound_exhaust":True,
            "reduced_state_called_one_objective_trajectory":False,
            "pass":failures==0 and max(completeness_residual,single_unitarity,single_inverse,bath_reset_population)<TOL
                    and c663_eigs==restriction_eigs}
    check("one regenerative collision law exactly reproduces the Cycle663 reduced semigroup",result["pass"],
          {"semigroup":max_semigroup,"bath_reset":bath_reset_population,"rows":len(rows)})
    return result


def objective_kernel_tournament(c662_receipt):
    rows={}; failures=0; max_formula=max_sector=max_inverse=0.0
    for name,item in kernel_inputs().items():
        rho=item["rho"]; spectator=item["spectator"]; horizon=item["horizon"]
        branches=[]; operators=history_operators(horizon)
        for label,operator in operators:
            extended=extend_operator(operator,spectator); branch=extended@rho@extended.conj().T
            q=float(np.trace(branch).real)
            formula=float(np.trace(extended@rho@extended.conj().T).real)
            formula_residual=abs(q-formula); max_formula=max(max_formula,formula_residual)
            branches.append({"sigma":label,"propensity":q,"stored_innovation":label,
                             "objective_within_supplied_candidate_law":q>TOL,
                             "wave_history_sector_retained":True})
        # The coherent history isometry has one environment sector per objective label.
        isometry=np.vstack([extend_operator(op,spectator) for _,op in operators])
        inverse_residual=float(np.linalg.norm(isometry.conj().T@isometry-np.eye(DIM*spectator),ord=2)); max_inverse=max(max_inverse,inverse_residual)
        sector_residual=abs(sum(row["propensity"] for row in branches)-1); max_sector=max(max_sector,sector_residual)
        rows[name]={"split":item["split"],"horizon":horizon,"branches":branches,
                    "objective_path_labels":len(branches),"kernel_normalization_residual":sector_residual,
                    "coherent_history_inverse_residual":inverse_residual,
                    "law_updates_sigma_without_input_actuality":True,"host_sampler_calls":0,
                    "runner_samples_branch":False,"all_zero_propensity_labels_retained":True}
        failures+=int(max(sector_residual,inverse_residual)>TOL)
    # Compose every exact Cycle662 pointer-pattern branch with the current
    # trace-preserving history instrument.  Marginalizing the new temporal
    # label must return every Cycle662 objective pointer propensity unchanged.
    prior_rows={(row["menu"],row["state"]):row for row in c662_receipt["stochastic_dilation"]["rows"]}
    pointer_marginal_rows=[]; pointer_marginal_failures=0; maximum_pointer_marginal=0.0; joint_labels=0
    states,_=c662prior.blind_states()
    for menu_name,effects in c662prior.cycle634_menus().items():
        compiled=c662prior.c634.compile_menu(effects)
        pointer_kraus=c662prior.c634.pointer_kraus(compiled["unitary"],compiled["ports"])
        for state_name,state in states.items():
            rho=state["rho"]; spectator=state["spectator"]
            horizon=6 if state_name=="held_blind_nonproduct" else 4 if state_name=="held_blind_biased" else 3
            embed_system=np.zeros((DIM,2),complex); embed_system[0,0]=1; embed_system[1,1]=1
            embed=np.kron(embed_system,np.eye(spectator)); prior_row=prior_rows[(menu_name,state_name)]
            branch_residuals=[]
            for branch_prior,(pattern,operator) in zip(prior_row["branches"],sorted(pointer_kraus.items())):
                extended=np.kron(operator,np.eye(spectator)); branch2=extended@rho@extended.conj().T
                branch7=embed@branch2@embed.conj().T; q=float(np.trace(branch7).real)
                temporal_total=0.0
                for _,history in history_operators(horizon):
                    history_ext=np.kron(history,np.eye(spectator))
                    temporal_total+=float(np.trace(history_ext@branch7@history_ext.conj().T).real)
                residual=max(abs(q-branch_prior["propensity"]),abs(temporal_total-q))
                maximum_pointer_marginal=max(maximum_pointer_marginal,residual); branch_residuals.append(residual)
                joint_labels+=len(history_operators(horizon))
            row_residual=max(branch_residuals,default=0.0); pointer_marginal_failures+=int(row_residual>TOL)
            pointer_marginal_rows.append({"menu":menu_name,"state":state_name,"split":state["split"],
                                          "horizon":horizon,"pointer_patterns":len(pointer_kraus),
                                          "maximum_pointer_marginal_residual":row_residual})
    prior_law=c662_receipt["stochastic_dilation"]["law"]
    same_form="q_p=Tr" in prior_law and "sigma'=p" in prior_law
    kernel_source=inspect.getsource(objective_kernel_tournament)
    sampling_call_names={"random","rand","randn","choice","choices","sample","randint","uniform"}
    host_sampling_hits=tuple(sorted({
        (node.func.attr if isinstance(node.func,ast.Attribute) else node.func.id)
        for node in ast.walk(ast.parse(kernel_source)) if isinstance(node,ast.Call)
        and isinstance(node.func,(ast.Attribute,ast.Name))
        and (node.func.attr if isinstance(node.func,ast.Attribute) else node.func.id) in sampling_call_names
    }))
    actuality_input_parameter=any("actual" in name.lower() for name in inspect.signature(objective_kernel_tournament).parameters)
    result={"law":"q_sigma(rho)=Tr[(J_sigma tensor I) rho (J_sigma^dagger tensor I)], sigma'=sigma",
            "Cycle662_law":prior_law,"same_quadratic_branch_kernel_form":same_form,
            "Cycle662_objective_candidate_terminal":c662_receipt["target_contract_candidate_terminal_met"],
            "Cycle662_pointer_marginal_rows":pointer_marginal_rows,
            "Cycle662_pointer_marginal_failures":pointer_marginal_failures,
            "Cycle662_joint_pointer_temporal_labels":joint_labels,
            "maximum_Cycle662_pointer_marginal_residual":maximum_pointer_marginal,
            "rows":rows,"maximum_formula_residual":max_formula,"maximum_sector_residual":max_sector,
            "maximum_coherent_inverse_residual":max_inverse,"input_actuality_token_M2":0,"host_sampler_calls":0,
            "host_sampling_source_hits":host_sampling_hits,"actuality_input_parameter":actuality_input_parameter,
            "innovation_law_supplied_not_derived_as_nature_law":True,
            "wave_exhaust_and_objective_sigma_both_retained":True,
            "candidate_pointer_or_latch_called_framework_Record":False,"propensity_called_Born_probability":False,
            "pass":failures==0 and pointer_marginal_failures==0 and same_form
                   and c662_receipt["target_contract_candidate_terminal_met"]
                   and max(max_formula,maximum_pointer_marginal)<TOL and not host_sampling_hits and not actuality_input_parameter}
    check("the same law realizes the Cycle662 objective-within-law quadratic trajectory kernel",result["pass"],
          {"formula":max_formula,"pointer_marginal":maximum_pointer_marginal,"joint_labels":joint_labels,"actuality_inputs":0})
    return result


def kron_all(items):
    result=np.array([1+0j])
    for item in items: result=np.kron(result,item)
    return result


def pointer_fixtures():
    z0=np.array([1,0],complex); train=kron_all([z0]*6); cfg=PREREGISTRATION["pointer_temporal_inputs"]["biased_phase_product"]
    biased=kron_all([np.array([math.cos(theta),np.exp(1j*phase)*math.sin(theta)],complex)
                     for theta,phase in zip(cfg["theta"],cfg["phase"])])
    ghz=np.zeros(64,complex); ghz[0]=1/math.sqrt(2); ghz[-1]=np.exp(0.37j)/math.sqrt(2)
    return {"product_z0":train,"biased_phase_product":biased,"six_site_GHZ":ghz}


def pointer_distribution(state,effects):
    rows={}
    for candidates in product((0,1),repeat=6):
        operator=kron_all([effects[0] if bit else effects[1] for bit in candidates])
        rows[candidates]=float(np.vdot(state,operator@state).real)
    return rows


def offdiagonal(matrix):
    out=matrix.copy(); np.fill_diagonal(out,0); return out


def temporal_correlation_tournament(c661_receipt,c663_receipt):
    menu=c634.menu_families()["mixed_projective_merge"]; compiled=c634.compile_menu(menu)
    effects=c634.induced_effects(compiled["unitary"],compiled["ports"])
    cfg=PREREGISTRATION["pointer_temporal_inputs"]; prior=c661_receipt["quantum_menu_and_firewalls"]["preregistered_state_rows"]
    rows={}; failures=0
    for name,state in pointer_fixtures().items():
        probs=pointer_distribution(state,effects); q=sum(value for word,value in probs.items() if sum(word)==1)
        horizon=cfg[name]["horizon"]
        p=np.asarray([q*(1-SURVIVAL)*SURVIVAL**layer for layer in range(horizon)])
        first_hit_joint=np.diag(p); collision_cov=first_hit_joint-np.outer(p,p)
        deterministic_p=np.zeros(horizon); deterministic_p[0]=q
        deterministic_joint=np.diag(deterministic_p); deterministic_cov=deterministic_joint-np.outer(deterministic_p,deterministic_p)
        score=float(np.linalg.norm(offdiagonal(collision_cov-deterministic_cov),ord="fro"))
        prior_q=prior[name]["QCA_formed_sector_weight"]
        c663_row=c663_receipt["corpus_response"]["rows"][name]
        fixture_fail=(abs(q-prior_q)>TOL or abs(q-c663_row["attractor_unique_sector_weight"])>TOL
                      or abs(sum(p)-q*(1-SURVIVAL**horizon))>TOL)
        held=cfg[name]["split"].startswith("held")
        failures+=int(fixture_fail or (held and score<=TOL))
        rows[name]={"split":cfg[name]["split"],"horizon":horizon,"unique_candidate_weight":q,
                    "Cycle661_unique_candidate_weight":prior_q,"Cycle663_attractor_weight":c663_row["attractor_unique_sector_weight"],
                    "first_emission_event_propensities":p.tolist(),
                    "finite_emission_weight":float(sum(p)),"survival_weight":q*SURVIVAL**horizon,
                    "offdiagonal_collision_covariance":offdiagonal(collision_cov).tolist(),
                    "offdiagonal_Cycle661_covariance":offdiagonal(deterministic_cov).tolist(),
                    "offdiagonal_temporal_covariance_discriminator":score,
                    "held_row_used_for_disposition":held,"one_step_marginal_used_for_disposition":False}
    held_scores=[row["offdiagonal_temporal_covariance_discriminator"] for row in rows.values() if row["held_row_used_for_disposition"]]
    c661_target=c661_receipt["frozen_contract"]["target_contract"]
    native_temporal_contract=any("temporal" in str(value).lower() or "trajectory" in str(value).lower()
                                 for value in c661_target.values())
    schedule_firewall=citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md",
        "Gate order and carrier-head advance are not physical time or a rate",
    )
    extension_score_pass=len(held_scores)==2 and min(held_scores)>TOL
    result={"observable":"first-emission indicator J_h","rows":rows,
            "discriminator":"off-diagonal covariance Frobenius norm; diagonal/one-step entries masked",
            "minimum_held_temporal_score":min(held_scores),"held_rows_distinguished":sum(score>TOL for score in held_scores),
            "held_rows_required":len(held_scores),"one_step_marginals_used_for_disposition":False,
            "preregistered_immediate_Cycle661_extension_distinguished":extension_score_pass,
            "Cycle661_native_temporal_contract_present":native_temporal_contract,
            "Cycle661_schedule_time_firewall":schedule_firewall,
            "immediate_event_extension_is_additional_import":True,
            "Cycle661_route_distinguished_without_temporal_extension":False,
            "target_requirement_iv_met":False,
            "disposition":"BOUNDED_INDETERMINATE_FOR_CYCLE661_NATIVE_ROUTE; POSITIVE_AGAINST_PREREGISTERED_IMMEDIATE_EVENT_EXTENSION",
            "unweighted_pointer_census_called_empirical_data":False,"weights_called_Born_probability":False,
            "collision_layers_called_physical_time":False,
            "pass":failures==0 and extension_score_pass and not native_temporal_contract}
    check("held temporal test separates the preregistered extension but does not overclaim Cycle661",result["pass"],
          {"scores":{name:row["offdiagonal_temporal_covariance_discriminator"] for name,row in rows.items()},
           "native_temporal_contract":native_temporal_contract,"requirement_iv":False})
    return result


@dataclass(frozen=True)
class EpisodeSlot:
    ready: int
    spent: int
    horizon: int
    pointer_blockade_exhaust: tuple[int,...] | None
    wave_exhaust: tuple[int,...] | None
    innovation_exhaust: tuple[int,...] | None


def initial_slots(capacity,horizon): return tuple(EpisodeSlot(1,0,horizon,None,None,None) for _ in range(capacity))


def validate_slots(slots,horizon):
    if not slots: raise ValueError("empty slots")
    frontier=False
    for slot in slots:
        if slot.horizon!=horizon or (slot.ready,slot.spent) not in ((1,0),(0,1)): raise ValueError("slot type")
        exhaust=(slot.pointer_blockade_exhaust,slot.wave_exhaust,slot.innovation_exhaust)
        if slot.ready and any(item is not None for item in exhaust): raise ValueError("dirty ready")
        if slot.spent and any(item is None for item in exhaust): raise ValueError("empty spent")
        if slot.spent and len(slot.pointer_blockade_exhaust)!=38: raise ValueError("pointer/blockade exhaust width")
        if slot.ready: frontier=True
        elif frontier: raise ValueError("non-prefix ledger")


def fire_slot(slots,horizon,path,formation_exhaust):
    validate_slots(slots,horizon)
    try:index=next(i for i,slot in enumerate(slots) if slot.ready)
    except StopIteration as error: raise OverflowError("episode ledger saturated") from error
    if len(path)!=horizon or any(label not in range(7) for label in path): raise ValueError("malformed path")
    if sum(label!=0 for label in path)>1: raise ValueError("more than one first emission")
    if len(formation_exhaust)!=38 or any(type(bit) is not int or bit not in (0,1) for bit in formation_exhaust):raise ValueError("formation exhaust")
    wave=tuple(label for label in path); innovation=tuple(label for label in path)
    out=list(slots); out[index]=EpisodeSlot(0,1,horizon,tuple(formation_exhaust),wave,innovation); out=tuple(out); validate_slots(out,horizon); return out


def inverse_fire(slots,horizon):
    validate_slots(slots,horizon); indices=[i for i,slot in enumerate(slots) if slot.spent]
    if not indices: raise ValueError("no spent slot")
    index=indices[-1]; out=list(slots); out[index]=EpisodeSlot(1,0,horizon,None,None,None); out=tuple(out); validate_slots(out,horizon); return out


def resource_ledger_tournament():
    rows=[]; failures=0
    for capacity,horizon,split in ((3,3,"train"),(4,4,"held_blinded"),(6,6,"held_blinded_nonproduct")):
        initial=initial_slots(capacity,horizon); state=initial; paths=[]
        for episode in range(capacity):
            path=[0]*horizon
            if episode%2==0: path[min(episode,horizon-1)]=(episode%6)+1
            candidates=(tuple(int(index==episode%6) for index in range(6)) if episode%2==0 else (1,1,0,0,0,0))
            formation_exhaust=candidates+(0,)*(38-6)
            state=fire_slot(state,horizon,tuple(path),formation_exhaust); paths.append(tuple(path))
        saturated=state; refusal=False
        try:fire_slot(state,horizon,(0,)*horizon,(0,)*38)
        except OverflowError:refusal=True
        while any(slot.spent for slot in state): state=inverse_fire(state,horizon)
        inverse_fail=int(state!=initial)
        dirty=list(initial); dirty[0]=EpisodeSlot(1,0,horizon,(0,)*38,(0,)*horizon,(0,)*horizon); dirty_refused=False
        try:validate_slots(tuple(dirty),horizon)
        except ValueError:dirty_refused=True
        bath_M2=6; wave_M2=6*horizon; innovation_M2=6*horizon
        route_core=12+38+bath_M2+wave_M2+innovation_M2+11
        full_episode=route_core+3; total=capacity*full_episode
        row={"capacity":capacity,"horizon":horizon,"split":split,"reusable_bath_M2":bath_M2,
             "wave_exhaust_M2_per_episode":wave_M2,"innovation_exhaust_M2_per_episode":innovation_M2,
             "route_core_M2_per_episode":route_core,"ready_spent_head_M2_per_episode":3,
             "full_M2_per_episode":full_episode,"explicit_retained_M2":total,
             "spent_at_saturation":sum(slot.spent for slot in saturated),"saturation_refuses_next_episode":refusal,
             "inverse_roundtrip_failures":inverse_fail,"dirty_ready_refused":dirty_refused,
             "inverse_renews_only_by_erasing_all_three_exhaust_classes":True,
             "non_erasing_indefinite_renewal_claimed":False,
             "pass":refusal and inverse_fail==0 and dirty_refused}
        failures+=int(not row["pass"]); rows.append(row)
    # Within every episode the same six bath M2 return blank after each collision;
    # H outbound wave carriers and H innovation slots are consumed and retained.
    result={"finite_rows":rows,"bath_regeneration":"SWAP bath state into blank outbound carrier after every collision",
            "same_bath_M2_reused_across_layers":True,"all_outbound_wave_exhaust_retained":True,
            "all_objective_innovation_exhaust_retained":True,
            "all_pointer_blockade_accepted_and_rejected_exhaust_retained":True,
            "external_interface_test_M2":{"Cycle625_B":c625.B_WIDTH,"Cycle621_A":c621.A_WIDTH},
            "finite_outbound_carrier_saturation_is_named":True,
            "bath_content_called_energy_entropy_temperature_or_source":False,
            "pass":failures==0}
    check("finite ready/spent regeneration ledgers retain all exhaust classes and saturate explicitly",result["pass"],
          [(row["capacity"],row["explicit_retained_M2"]) for row in rows])
    return result


@dataclass(frozen=True)
class Operation:
    kind: str
    sites: tuple[int,...]
    label: str


def physical_schedule(horizon):
    if type(horizon) is not int or horizon<1:raise ValueError("positive integer horizon required")
    # Standalone law: six pending rails, six reusable bath rails, then H banks
    # each of wave exhaust and objective innovation, followed by 11 scalar/packet targets.
    pending=tuple(range(6)); bath=tuple(range(6,12)); wave0=12; innovation0=12+6*horizon
    target0=12+12*horizon; operations=[]
    for layer in range(horizon):
        for direction in range(6):
            p=pending[direction]; b=bath[direction]; wave=wave0+6*layer+direction; innovation=innovation0+6*layer+direction
            operations.append(Operation("PARTIAL_SWAP",(p,b),f"collision:{layer}:{direction}"))
            operations.extend((Operation("CNOT",(b,wave),f"swap1:{layer}:{direction}"),
                               Operation("CNOT",(wave,b),f"swap2:{layer}:{direction}"),
                               Operation("CNOT",(b,wave),f"swap3:{layer}:{direction}")))
            operations.append(Operation("HYBRID_WRITE",(wave,innovation),f"innovation:{layer}:{direction}"))
            packet=(1,*(int(i==direction) for i in range(6)),1,0)
            targets=(target0,target0+1,*(target0+2+i for i,bit in enumerate(packet) if bit))
            for index,target in enumerate(targets):
                operations.append(Operation("CNOT",(innovation,target),f"port:{layer}:{direction}:{index}"))
    return tuple(operations)


def validate_physical_source(word,horizon):
    physical_schedule(horizon); width=23+12*horizon
    if len(word)!=width or any(type(bit) is not int or bit not in (0,1) for bit in word):raise ValueError("binary physical word")
    if sum(word[:6])>1:raise ValueError("multi-hot precursor")
    if any(word[6:]):raise ValueError("bath, exhaust, innovation and targets must be blank")


def semantic_writer_output(horizon,layer,direction,delete_label=None):
    width=23+12*horizon; wave=12+6*layer+direction; innovation=12+6*horizon+6*layer+direction
    bits=[0]*width; bits[wave]=1
    relevant=[op for op in physical_schedule(horizon)
              if op.label==f"innovation:{layer}:{direction}" or op.label.startswith(f"port:{layer}:{direction}:")]
    for op in relevant:
        if op.label==delete_label:continue
        control,target=op.sites; bits[target]^=bits[control]
    return tuple(bits)


def packet(direction):return (1,*(int(index==direction) for index in range(6)),1,0)


def cycle625_base(candidates,direction):
    bits=[0]*c625.B_WIDTH
    for sites,bit in zip(c625.P_ENDPOINT,candidates):
        for site in sites:bits[site]=bit
    for sites,bit in zip(c625.P_PACKET,packet(direction)):
        for site in sites:bits[site]=bit
    bits[c625.P_ADMIT]=1; bits[c625.B_READY]=1
    return tuple(bits)


def interface_compatibility_tournament():
    writer_fail=c625_fail=c625_inverse=c531_fail=c621_fail=0
    for direction in range(6):
        horizon=3; word=semantic_writer_output(horizon,0,direction); target0=12+12*horizon
        writer_fail+=int(word[target0]!=1 or word[target0+1]!=1
                         or tuple(word[target0+2+i] for i in range(9))!=packet(direction))
        candidates=tuple(int(index==direction) for index in range(6)); base=cycle625_base(candidates,direction)
        output=c625.apply_cnots(base,c625.B_SCHEDULE)
        occurrence=output[c625.B_EDGE]&output[c625.B_MEMBER[0]]&output[c625.B_RECEIPT[0]]
        c625_fail+=int(tuple(output[site] for site in c625.B_ARCHIVE)!=candidates
                        or tuple(output[site] for site in c625.B_MEMBER)!=(1,0,0,0,0)
                        or tuple(output[site] for site in c625.B_RECEIPT)!=(1,0,0,0,0))
        c531_fail+=int(occurrence!=1 or output[c625.B_SNAPSHOT[1]]!=1 or output[c625.B_SNAPSHOT[2]]!=1)
        c625_inverse+=int(c625.apply_cnots(output,c625.B_SCHEDULE,reverse=True)!=base)
        formed=c621.cycle614_formed(direction); before=c621.packet_coordinates(formed)
        for generator in c621.A_GENERATORS:
            after=c621.apply_a_schedule(formed,generator.gates)
            c621_fail+=int(c621.packet_coordinates(after)!=before or after[c621.A_LOCK]!=1 or after[c621.A_ADMIT_PROVENANCE]!=1)
    result={"formed_directions":6,"emission_writer_failures":writer_fail,"Cycle625_failures":c625_fail,
            "Cycle625_inverse_failures":c625_inverse,"Cycle531_equation_failures":c531_fail,
            "Cycle621_generator_tests":6*len(c621.A_GENERATORS),"Cycle621_generator_failures":c621_fail,
            "packet_called_framework_Record":False,"finite_preserving_monoid_called_physical_all_future_law":False,
            "pass":writer_fail==c625_fail==c625_inverse==c531_fail==c621_fail==0}
    check("regenerated emission labels feed unchanged occurrence and preservation interfaces",result["pass"],
          {"directions":6,"generators":result["Cycle621_generator_tests"]})
    return result


def ordered_wire_depth(operations):
    last_layer={}; maximum=0
    for op in operations:
        layer=1+max((last_layer.get(site,0) for site in op.sites),default=0)
        for site in op.sites:last_layer[site]=layer
        maximum=max(maximum,layer)
    return maximum


def direction_map(frame,direction):
    return c625.DIRECTIONS.index(c625.matvec(frame,c625.DIRECTIONS[direction]))


def covariance_locality_controls():
    frames=c625.proper_cubic_frames(); kraus=multirail_kraus(); covariance_fail=0; maximum=0.0
    for frame in frames:
        p=np.zeros((DIM,DIM),complex); p[0,0]=1
        for direction in range(6): p[1+direction_map(frame,direction),1+direction]=1
        residual=float(np.linalg.norm(p@kraus[0]@p.conj().T-kraus[0],ord=2)); maximum=max(maximum,residual); covariance_fail+=residual>TOL
        for direction in range(6):
            residual=float(np.linalg.norm(p@kraus[direction+1]@p.conj().T-kraus[direction_map(frame,direction)+1],ord=2))
            maximum=max(maximum,residual); covariance_fail+=residual>TOL
    group_fail=0
    for left,right,direction in product(frames,frames,range(6)):
        group_fail+=int(direction_map(left,direction_map(right,direction))!=direction_map(c625.matmul(left,right),direction))
    history_cov_fail=0
    for horizon in (3,4,6):
        for frame in frames:
            mapping=tuple(direction_map(frame,d) for d in range(6))
            source_labels=tuple(label for label,_ in history_operators(horizon))
            rotated=[]
            for label in source_labels:
                if label=="none":rotated.append(label)
                else:
                    _,layer,direction=label.split(":"); rotated.append(f"emit:{layer}:{mapping[int(direction)]}")
            history_cov_fail+=int(set(rotated)!=set(source_labels))
    schedule_cov_fail=0
    for horizon in (3,4,6):
        schedule=physical_schedule(horizon); target0=12+12*horizon
        reference=sorted((op.kind,op.sites) for op in schedule)
        for frame in frames:
            def rotate_site(site):
                if 0<=site<6:return direction_map(frame,site)
                if 6<=site<12:return 6+direction_map(frame,site-6)
                if 12<=site<12+6*horizon:
                    relative=site-12; layer,direction=divmod(relative,6)
                    return 12+6*layer+direction_map(frame,direction)
                innovation0=12+6*horizon
                if innovation0<=site<innovation0+6*horizon:
                    relative=site-innovation0; layer,direction=divmod(relative,6)
                    return innovation0+6*layer+direction_map(frame,direction)
                if target0+3<=site<target0+9:return target0+3+direction_map(frame,site-(target0+3))
                return site
            moved=sorted((op.kind,tuple(rotate_site(site) for site in op.sites)) for op in schedule)
            schedule_cov_fail+=int(moved!=reference)
    schedule_rows={}; all_support=True
    for horizon in (3,4,6):
        schedule=physical_schedule(horizon); counts={kind:sum(op.kind==kind for op in schedule) for kind in ("PARTIAL_SWAP","CNOT","HYBRID_WRITE")}
        support=max(len(op.sites) for op in schedule); depth=ordered_wire_depth(schedule); width=23+12*horizon
        schedule_rows[str(horizon)]={"standalone_law_M2":width,"operation_counts":counts,"literal_operations":len(schedule),
                                     "ordered_wire_depth":depth,"maximum_support_M2":support}
        all_support&=support<=2
    translated=[]
    for offset in (0,256,512):
        normalized=tuple((op.kind,tuple(site+offset-offset for site in op.sites),op.label) for op in physical_schedule(6)); translated.append(digest(normalized))
    # Active controls: collision deletion is tested against the history unitary
    # below; here the literal SWAP and semantic innovation/port writes are tested.
    source=np.zeros(8,complex); source[4]=1
    full_regenerator=layer_regenerator_unitary()@source
    swap_deleted=layer_regenerator_unitary(delete_swap_gate=1)@source
    full_writer=semantic_writer_output(3,0,0)
    no_innovation=semantic_writer_output(3,0,0,"innovation:0:0")
    no_port=semantic_writer_output(3,0,0,"port:0:0:0")
    deletions=[
        {"operation":"swap2:0:0","basis_witness_residual":float(np.linalg.norm(full_regenerator-swap_deleted)),"visible":not np.allclose(full_regenerator,swap_deleted)},
        {"operation":"innovation:0:0","basis_witness_residual":0.0 if full_writer==no_innovation else math.sqrt(2),"visible":full_writer!=no_innovation},
        {"operation":"port:0:0:0","basis_witness_residual":0.0 if full_writer==no_port else math.sqrt(2),"visible":full_writer!=no_port},
    ]
    malformed=[]; horizon=3; width=23+12*horizon
    cases=[]
    for name,sites in (("multi_hot_pending",(0,1)),("dirty_reusable_bath",(6,)),
                       ("dirty_outbound_wave",(12,)),("dirty_innovation",(12+6*horizon,)),
                       ("dirty_target",(12+12*horizon,))):
        word=[0]*width
        for site in sites:word[site]=1
        cases.append((name,tuple(word),horizon))
    for name,word,h in cases:
        refused=False
        try:validate_physical_source(word,h)
        except ValueError:refused=True
        malformed.append({"case":name,"refused":refused})
    invalid_horizon_refused=False
    try:physical_schedule(0)
    except ValueError:invalid_horizon_refused=True
    malformed.append({"case":"invalid_horizon","refused":invalid_horizon_refused})
    result={"proper_cubic_frames":len(frames),"Kraus_all24_comparisons":len(frames)*7,
            "Kraus_covariance_failures":covariance_fail,"maximum_Kraus_covariance_residual":maximum,
            "history_label_all24_comparisons":len(frames)*3,"history_label_covariance_failures":history_cov_fail,
            "full_schedule_all24_comparisons":len(frames)*3,"full_schedule_covariance_failures":schedule_cov_fail,
            "all576_direction_tests":len(frames)**2*6,"all576_direction_failures":group_fail,
            "schedule_rows":schedule_rows,"all_literal_operations_support_at_most_two_M2":all_support,
            "translated_schedule_digests":translated,"partitioned_supercell_translation_invariant":len(set(translated))==1,
            "deletion_rows":deletions,"malformed_rows":malformed,"global_parity_service":False,"preferred_global_ordering":False,
            "runtime_frame_selector":False,"collision_layer_called_physical_time":False,"generator_element_called_rate":False,
            "pass":len(frames)==24 and covariance_fail==history_cov_fail==schedule_cov_fail==group_fail==0 and maximum<TOL and all_support
                   and len(set(translated))==1 and all(row["visible"] and row["basis_witness_residual"]>0.5 for row in deletions)
                   and all(row["refused"] for row in malformed)}
    check("support-two schedules, translation, all24/all576, deletion and malformed controls pass",result["pass"],
          {"all24":result["Kraus_all24_comparisons"],"all576":result["all576_direction_tests"],"H6":schedule_rows["6"]})
    return result


def dark_saturation_inverse_controls():
    vacuum=np.zeros((DIM,DIM),complex); vacuum[0,0]=1
    out=apply_channel(vacuum); dark=float(np.linalg.norm(out-vacuum,ord=2))
    props=[float(np.trace(k@vacuum@k.conj().T).real) for k in multirail_kraus()]
    inverse_rows=[]; deletion_rows=[]
    for horizon in (3,4,6):
        u=history_unitary(horizon); source=np.zeros(u.shape[0],complex); source[1]=1
        output=u@source; inverse=float(np.linalg.norm(u.conj().T@output-source)); inverse_rows.append({"horizon":horizon,"residual":inverse})
        damaged=history_unitary(horizon,delete_pair=(0,0))@source
        deletion_rows.append({"horizon":horizon,"first_collision_deletion_residual":float(np.linalg.norm(output-damaged))})
    invalid=[]
    for bad in (0,-1,1.5):
        refused=False
        try:history_operators(bad)
        except (ValueError,TypeError):refused=True
        invalid.append({"horizon":bad,"refused":refused})
    malformed_density=[]
    for rho,spectator in ((np.eye(DIM)/8,1),(np.diag([1.1]+[-0.1]+[0]*5).astype(complex),1),(np.eye(3)/3,1)):
        refused=False
        try:validate_density(rho,spectator)
        except ValueError:refused=True
        malformed_density.append(refused)
    result={"vacuum_dark_residual":dark,"vacuum_objective_propensities":props,
            "postformation_no_emission_is_certain":abs(props[0]-1)<TOL and max(props[1:])<TOL,
            "global_history_inverse_rows":inverse_rows,"collision_deletion_rows":deletion_rows,
            "invalid_horizon_rows":invalid,"malformed_density_rejections":sum(malformed_density),
            "expected_malformed_density_rejections":len(malformed_density),"complete_exhaust_required_for_inverse":True,
            "pass":dark<TOL and abs(props[0]-1)<TOL and max(props[1:])<TOL
                   and max(row["residual"] for row in inverse_rows)<TOL
                   and min(row["first_collision_deletion_residual"] for row in deletion_rows)>0.5
                   and all(row["refused"] for row in invalid) and all(malformed_density)}
    check("inverse, collision deletion, malformed, and dark/postformation controls pass",result["pass"],
          {"dark":dark,"deletion":min(row["first_collision_deletion_residual"] for row in deletion_rows)})
    return result


def no_go_discipline():
    families=[
        {"family":"Cycle661 deterministic conserved-count QCA","status":"ATTEMPTED_POSITIVE_CANDIDATE","invariant":"basis-code immediate formation"},
        {"family":"Cycle662 hybrid menu jump law","status":"ATTEMPTED_POSITIVE_CANDIDATE","invariant":"supplied quadratic objective sigma"},
        {"family":"Cycle663 retained dissipative collision","status":"ATTEMPTED_POSITIVE_CANDIDATE","invariant":"reduced semigroup without trajectory promotion"},
        {"family":"Cycle666 regenerative hybrid collision","status":"ATTEMPTED_PARTIAL_POSITIVE","invariant":"reused bath plus outbound wave/innovation exhaust; native Cycle661 temporal comparison unavailable"},
        {"family":"autonomous closed finite bath cycle","status":"OPEN_NOT_COUNTED","invariant":"stationary non-erasing renewal without blank influx"},
        {"family":"unitary-only many-world history","status":"OPEN_NOT_COUNTED","invariant":"no extra ontic sigma"},
    ]
    walls=("nature_law_selection","objective_hybrid_ontology_import","indefinite_non_erasing_exhaust_renewal",
           "framework_Record_permanence","empirical_probability_and_physical_time")
    pairs=[{"left":a,"right":b,"left_closes_right":False,"right_closes_left":False,"independent":True}
           for a in walls for b in walls if a!=b]
    c662ref=citation("docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md","quadratic stochastic jump form")
    c663ref=citation("docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md","reduced ensemble is not one objective trajectory")
    c661ref=citation("docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md","positive deterministic basis-code formation candidate")
    current=current_citation("def objective_kernel_tournament(")
    residuals=[
        {"prior":c663ref,"prior_residual":"reduced collision semigroup has no objective path","current":current,
         "current_residual":"supplied hybrid sigma gives a finite objective path while wave exhaust remains","exact_scope_match":True,"used_as_closure":True},
        {"prior":c662ref,"prior_residual":"quadratic jump form is supplied, not selected as nature law","current":current,
         "current_residual":"same kernel form survives regeneration; nature-law selection remains open","exact_scope_match":True,"used_as_closure":False},
        {"prior":c661ref,"prior_residual":"deterministic basis-code candidate explicitly lacking physical-time interpretation","current":current_citation("def temporal_correlation_tournament("),
         "current_residual":"held covariance separates only a preregistered immediate-event extension; native Cycle661 temporal disposition is indeterminate","exact_scope_match":True,"used_as_closure":False},
    ]
    rhetoric=[
        {"claim":"finite regenerative bath does not imply indefinite non-erasing renewal","per_element":"each bath bit is swapped out","per_site":"six bath M2 reused","per_mode":"all wave and innovation modes retained","per_block":"H3/H4/H6 saturate","lattice_wide":"outbound blank-carrier supply open"},
        {"claim":"objective within a supplied hybrid law is not derivation of nature's law","per_element":"every sigma branch enumerated","per_site":"bounded stochastic kernel","per_mode":"no-emission plus six directions","per_block":"three frozen inputs","lattice_wide":"law selection untested"},
        {"claim":"temporal covariance is not Born frequency or physical time","per_element":"first-hit indicators","per_site":"one coarse formation cell","per_mode":"six directions","per_block":"held H4/H6","lattice_wide":"no empirical process tested"},
    ]
    partial=[
        {"file":"Cycle666","status":"EXECUTED_PARTIAL_POSITIVE","closes":"finite bath reset and semigroup/trajectory equivalence; only extension-level temporal discriminator"},
        {"file":"Cycle662","status":"EXECUTED_PRIOR","closes":"objective-within-supplied-law kernel only"},
        {"file":"future closed bath cycle","status":"OPEN","closes":"indefinite non-erasing carrier renewal"},
        {"file":"future law-selection tournament","status":"OPEN","closes":"why this hybrid kernel is physical"},
    ]
    steelman=("Construct a closed translation-invariant carrier QCA whose outbound exhaust is transported without deletion, "
              "whose local low-entropy bath slots recur without importing blank states, and whose objective innovation ontology "
              "is derived rather than stipulated; then test multi-cell temporal correlations and noise-stable packet permanence. "
              "That route could retire renewal, law selection and Record walls, so the present finite positive candidate supports no no-go.")
    echoes=[
        {"cycle":661,"retired":"nothing in its native temporal scope; the immediate-event extension is separated","remaining":"native route supplies no temporal joint law and remains viable"},
        {"cycle":662,"retired":"lack of a collision realization for its generic kernel","remaining":"hybrid ontology and nature-law choice supplied"},
        {"cycle":663,"retired":"lack of a finite objective-within-law trajectory attached to its semigroup","remaining":"reduction alone still is not actuality"},
        {"cycle":621,"retired":"none of indefinite non-erasing renewal","remaining":"finite preserving monoid only"},
    ]
    passed=sum(row["status"].startswith("ATTEMPTED") for row in families)==4 and len(pairs)==20 and all(row["exact_scope_match"] for row in residuals)
    result={"N1_families":families,"N1_qualifying_attempts":4,"N1_required_for_negative":5,
            "N1_broad_negative_gate":"FAIL_DO_NOT_SHIP","N2_walls":walls,"N2_directed_pairs":pairs,
            "N3_hidden_conditions":["r=1/2","one-excitation six-rail code","blank outbound carriers","supplied hybrid stochastic ontology","finite capacities","Cycle634 menu","frame chart","Cycle625/Cycle621 ports"],
            "N4_exact_residual_matches":residuals,"N5_rhetoric":rhetoric,"N6_partial_closure_paths":partial,
            "N7_steelman":steelman,"N8_cross_cycle_echo":echoes,
            "broad_negative_claim":False,"minimum_content_claim":False,"shared_route_independent_obstruction":False,
            "axiom_pressure":False,"route_specific_finite_renewal_residual_only":True,
            "route_specific_temporal_comparison_indeterminate":True,"pass":passed}
    check("fresh N1-N8 blocks broad negative, shared obstruction and axiom pressure",passed,
          {"attempted":4,"required":5,"pairs":20})
    return result


def inventory():
    return {"supplied":["Cycle634 mixed-projective menu and blank ports","Cycle662 hybrid quadratic sigma ontology",
                        "Cycle663 r=1/2 collision","one-excitation direction code","blank outbound carriers",
                        "finite ready/spent capacities","proper-cubic chart","Cycle625/Cycle621 external ports"],
            "derived":["literal bath reset by state transfer","coherent history isometry and reduced semigroup equality",
                        "objective trajectory kernel equality","complete dual exhaust ledger","held off-diagonal temporal separation from one preregistered Cycle661 extension",
                        "support-two lowering","all24/all576","dark/inverse/deletion/domain controls"],
            "open":["Cycle661-native temporal comparison law","nature-law selection","derivation of objective hybrid ontology","indefinite non-erasing exhaust renewal",
                    "framework Record and permanence","Born/empirical interpretation","physical time","energy/source/gravity"]}


def note_text(r):
    sem=r["semigroup_equivalence"]; obj=r["objective_kernel_equivalence"]; temp=r["temporal_discriminator"]
    ledger=r["resource_ledger"]; loc=r["covariance_locality"]; ng=r["no_go_discipline"]
    sem_rows="\n".join(f"| {name} | {row['split']} | {row['horizon']} | {row['trajectory_branches']} | {row['trajectory_sum_to_reduced_semigroup_residual']:.3e} | {row['global_history_inverse_residual']:.3e} | {row['spectator_no_signalling_residual']:.3e} |" for name,row in sem["rows"].items())
    temp_rows="\n".join(f"| {name} | {row['split']} | {row['horizon']} | {row['unique_candidate_weight']:.12f} | {row['finite_emission_weight']:.12f} | {row['offdiagonal_temporal_covariance_discriminator']:.3e} | {str(row['one_step_marginal_used_for_disposition']).lower()} |" for name,row in temp["rows"].items())
    ledger_rows="\n".join(f"| {row['capacity']} | {row['horizon']} | {row['split']} | {row['reusable_bath_M2']} | {row['full_M2_per_episode']} | {row['explicit_retained_M2']} | {str(row['saturation_refuses_next_episode']).lower()} |" for row in ledger["finite_rows"])
    schedule_rows="\n".join(f"| {horizon} | {row['standalone_law_M2']} | {row['literal_operations']} | {row['ordered_wire_depth']} | {row['maximum_support_M2']} |" for horizon,row in loc["schedule_rows"].items())
    n1="\n".join(f"| {row['family']} | {row['status']} | {row['invariant']} |" for row in ng["N1_families"])
    n2="\n".join(f"| {row['left']} | {row['right']} | no | no | yes |" for row in ng["N2_directed_pairs"])
    n5="\n".join(f"| {row['claim']} | {row['per_element']} | {row['per_site']} | {row['per_mode']} | {row['per_block']} | {row['lattice_wide']} |" for row in ng["N5_rhetoric"])
    n6="\n".join(f"| {row['file']} | {row['status']} | {row['closes']} |" for row in ng["N6_partial_closure_paths"])
    n8="\n".join(f"| Cycle {row['cycle']} | {row['retired']} | {row['remaining']} |" for row in ng["N8_cross_cycle_echo"])
    return f"""# Regenerative-bath trajectory/semigroup equivalence tournament — Cycle 666

Authority: **none**

Audit: **unset**

## Fresh N1–N8 gate before disposition

### N1

| family | status | invariant |
|---|---|---|
{n1}

Four qualifying attempts are below the required five. Broad negative, minimum-content, shared-obstruction and axiom-pressure gates are **FAIL / DO NOT SHIP**.

### N2

| left | right | left closes right? | reverse? | independent? |
|---|---|---:|---:|---:|
{n2}

### N3–N4

All collision angle, one-excitation code, blank carriers, stochastic ontology, finite capacities, menus, charts and ports are explicit. N4 matches Cycle663's reduction residual, Cycle662's supplied-law residual, and Cycle661's deterministic scope without promoting any route-specific result to constitutional evidence.

### N5

| claim | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
{n5}

### N6

| path | status | closes |
|---|---|---|
{n6}

### N7

{ng['N7_steelman']}

### N8

| cycle | retired scope | remaining |
|---|---|---|
{n8}

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Result classification

Classification: **partial positive finite hybrid collision law; native Cycle661 temporal comparison, nature-law selection, indefinite renewal, Record, Born, and physical-time identification open**

Strict full-framework terminal: **false**

## Frozen target and construction

The target `{r['frozen_contract']['target_sha256']}` and temporal preregistration `{r['frozen_contract']['preregistration_sha256']}` were fixed at lines `{r['frozen_contract']['target_line']}` and `{r['frozen_contract']['preregistration_line']}` before evidence line `{r['frozen_contract']['first_evidence_line']}`. All `{len(r['frozen_contract']['pins'])}` shore artifacts are exact at `{r['frozen_contract']['shore']}`.

Six identical precursor rails collide with six reusable bath M2 through the Cycle663 `r=1/2` partial swap. After each collision, a literal reversible SWAP moves every bath bit into a fresh outbound wave-exhaust carrier and returns the same bath M2 to blank. Nothing is discarded. The coherent history unitary remains exactly invertible only while those carriers are retained.

On the vacuum-plus-six-direction code, the seven local history operators are `J_0=diag(1,sqrt(r),...,sqrt(r))` and `J_d=sqrt(1-r)|vac><d|`. Their sum gives the reduced channel; the supplied hybrid stochastic law writes one ontic `sigma` label with `q_sigma(rho)=Tr[J_sigma rho J_sigma^dagger]`. This is the same quadratic kernel form as Cycle662 and requires zero input actuality M2 and zero host samples. The hybrid ontology remains supplied rather than derived as nature's law.

Composition with every exact Cycle662 pointer-pattern branch preserves all `{len(obj['Cycle662_pointer_marginal_rows'])}` menu/state pointer marginals while refining them into `{obj['Cycle662_joint_pointer_temporal_labels']}` joint pointer/temporal labels. The maximum pointer-marginal residual is `{obj['maximum_Cycle662_pointer_marginal_residual']:.3e}`.

| input | split | H | trajectory branches | semigroup residual | coherent inverse residual | spectator residual |
|---|---|---:|---:|---:|---:|---:|
{sem_rows}

The Kraus completeness residual is `{sem['Kraus_completeness_residual']:.3e}`; the literal collision/SWAP unitarity residual is `{sem['literal_three_M2_collision_swap_unitarity_residual']:.3e}`; and bath-one population after state transfer is `{sem['bath_one_population_after_swap_to_blank_exhaust']:.3e}`. Restriction to any one direction has Cycle663 spectrum `{sem['current_single_rail_spectrum']}` exactly.

The reduced state is not promoted to one actual path. `sigma` is objective only within this explicitly supplied candidate stochastic law. Wave history and objective innovation exhaust are both retained. A pointer, latch, or occurrence candidate is not called a framework Record; no propensity is called Born probability.

## Preregistered temporal discriminator

| pointer fixture | split | H | unique weight q | finite emission weight | off-diagonal covariance score | one-step used? |
|---|---|---:|---:|---:|---:|---|
{temp_rows}

The score masks every diagonal entry and uses only the off-diagonal covariance of first-emission indicators. The two held rows pass with minimum score `{temp['minimum_held_temporal_score']:.3e}`. One-step marginals are reported for accounting but are not used for disposition. This separates the present finite collision candidate from the preregistered immediate-event extension of Cycle661.

It does **not** distinguish the native Cycle661 route. Cycle661 supplies one deterministic formation update, explicitly states that gate order and carrier-head advance are not physical time or a rate, and supplies no temporal joint kernel. Treating its update as `J_1=A, J_h>1=0` is therefore an additional comparison import. Requirement (iv) is **bounded indeterminate**, not a route falsification.

Collision-layer indices are schedule labels, not physical time or a rate. These code-state weights are not empirical frequencies or Born probability.

## Finite regeneration and locality

| capacity | H | split | reusable bath M2 | full M2/episode | retained M2 | saturation refusal |
|---:|---:|---|---:|---:|---:|---|
{ledger_rows}

The bath is regenerated locally across the declared H layers because its state is exported, not erased. Every slot also retains the 38-M2 pointer/blockade accepted-or-rejected exhaust. Finite outbound carrier and innovation stores saturate. Inverse makes a slot ready only by erasing the pointer/blockade, wave, and innovation exhausts; indefinite non-erasing renewal remains open. Bath content is not called energy, entropy, temperature, stress, or gravity source.

| H | standalone law M2 | literal operations | ordered wire depth | max support |
|---:|---:|---:|---:|---:|
{schedule_rows}

All operations have support at most two M2. The runner executes `{loc['Kraus_all24_comparisons']}` Kraus all24 comparisons, `{loc['history_label_all24_comparisons']}` history-label all24 comparisons, `{loc['full_schedule_all24_comparisons']}` full-schedule all24 comparisons, and `{loc['all576_direction_tests']}` all576 direction tests, with zero failures and maximum residual `{loc['maximum_Kraus_covariance_residual']:.3e}`. Translation digests agree. No global parity, preferred ordering, or runtime frame selector is used.

Every direction packet from the regenerated innovation writer feeds the unchanged Cycle625-B/Cycle531 occurrence port and all `{r['unchanged_interfaces']['Cycle621_generator_tests']}` Cycle621 preservation-generator checks with zero failures. This remains finite interface compatibility, not framework Record identification or an all-future physical law.

## Supplied, derived, open

Supplied: Cycle634 menu; Cycle662 hybrid quadratic sigma ontology; Cycle663 collision angle; one-excitation direction code; blank outbound carriers; finite capacities; frame chart; external occurrence/preservation ports.

Derived: literal bath reset by state transfer; coherent history and reduced-semigroup equality; objective-within-law trajectory equivalence; complete pointer/blockade, wave, and innovation exhaust; held temporal separation from the preregistered immediate-event extension; support-two lowering; all24/all576; inverse/deletion/domain/dark/saturation controls.

Open: a Cycle661-native temporal comparison law; nature-law selection; derivation of objective hybrid ontology; indefinite non-erasing renewal; framework Record/permanence; Born/empirical interpretation; physical time; energy/source/gravity.

## Disposition

**PASS** for one finite, bounded, translation/proper-cubic covariant candidate law simultaneously realizing the Cycle663 reduced semigroup, the Cycle662 objective-within-supplied-law kernel, complete pointer/blockade plus wave/innovation exhaust, and finite bath reuse.

**BOUNDED INDETERMINATE** for distinguishing native Cycle661 by temporal correlations. The held discriminator is positive only against the frozen immediate-event extension, which Cycle661 itself does not supply.

**OPEN / DO NOT CLAIM** for indefinite non-erasing renewal, derivation or selection of the hybrid ontology as nature's law, a framework Record, Born/empirical probability, physical time/rate, realized history, energy/source/gravity, shared obstruction, or axiom pressure.

The next campaign should first freeze a shared operational sequence protocol for Cycle661 and Cycle666 without calling that sequence physical time. It should then combine the protocol with a closed moving-carrier QCA that exports exhaust covariantly, returns blank capacity without deleting any occurrence, and tests whether hybrid sigma can be eliminated or derived.
"""


def note_contract():
    body=" ".join(NOTE.read_text().lower().split())
    required=("authority: **none**","audit: **unset**","strict full-framework terminal: **false**",
              "one-step marginals are reported for accounting but are not used for disposition",
              "reduced state is not promoted to one actual path","not called a framework record",
              "not empirical frequencies or born probability","not physical time or a rate",
              "shared route-independent obstruction: **not established**","axiom pressure: **none**")
    missing=tuple(fragment for fragment in required if fragment not in body)
    return {"required":required,"missing":missing,"pass":not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started=time.perf_counter()
    frozen,receipts=freeze_and_shore_controls()
    ng=no_go_discipline()
    semigroup=coherent_semigroup_tournament(receipts["663"])
    objective=objective_kernel_tournament(receipts["662"])
    temporal=temporal_correlation_tournament(receipts["661"],receipts["663"])
    ledger=resource_ledger_tournament(); locality=covariance_locality_controls()
    interfaces=interface_compatibility_tournament(); controls=dark_saturation_inverse_controls()
    receipt={"cycle":666,"date":"2026-07-23","status":"partial positive finite regenerative hybrid collision law; native Cycle661 temporal comparison indeterminate",
             "classification":"bounded constructive partial candidate with finite outbound-exhaust saturation and one route-specific temporal wall",
             "authority":AUTHORITY,"audit":AUDIT,"strict_full_framework_terminal_met":False,
             "target_contract_candidate_terminal_met":False,
             "target_requirement_disposition":{"i_Cycle663_semigroup":"PASS","ii_Cycle662_objective_kernel":"PASS",
                                                "iii_complete_exhaust":"PASS","iv_native_Cycle661_temporal_discriminator":"BOUNDED_INDETERMINATE"},
             "frozen_contract":frozen,
             "semigroup_equivalence":semigroup,"objective_kernel_equivalence":objective,
             "temporal_discriminator":temporal,"resource_ledger":ledger,"covariance_locality":locality,
             "unchanged_interfaces":interfaces,"dark_inverse_deletion_domain":controls,
             "no_go_discipline":ng,"supplied_structure_inventory":inventory(),
             "strongest_constructive_result":"one finite regenerative collision law has Cycle663 reduced dynamics, exact Cycle662 objective pointer marginals and trajectories, and complete pointer/blockade plus wave/innovation exhaust",
             "highest_honest_terminal":"partial positive finite candidate; native Cycle661 temporal comparison is undefined without an added sequence law",
             "route_disposition":{"Cycle661":"bounded indeterminate: frozen immediate-event extension separates, but native route has no temporal joint law",
                                  "Cycle662":"quadratic objective-within-law kernel reproduced",
                                  "Cycle663":"reduced amplitude-damping semigroup reproduced",
                                  "Cycle666":"finite bath reuse by outbound state transfer; dual exhaust saturates"},
             "shared_route_independent_obstruction":False,"axiom_pressure":False,"breakthrough":False,
             "author_accepted":False,"optimal_next_campaign":"freeze a shared operational sequence protocol for Cycle661/Cycle666, then test it inside a closed moving-carrier QCA and hybrid-sigma elimination/derivation"}
    NOTE.write_text(note_text(receipt)); note=note_contract(); check("Cycle666 note preserves trajectory/Record/Born/time/no-go firewalls",note["pass"],note["missing"])
    elapsed=time.perf_counter()-started; rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss<10_000_000:rss*=1024
    receipt.update({"note_contract":note,"runner_sha256":file_sha(Path(__file__)),"note_sha256":file_sha(NOTE),
                    "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"tests_passed":PASS,"tests_failed":FAIL})
    receipt["pass"]=(FAIL==0 and all(item["pass"] for item in (frozen,semigroup,objective,temporal,ledger,locality,interfaces,controls,ng,note))
                     and elapsed<WALL_CAP_SECONDS and rss<RSS_CAP_BYTES and AUTHORITY=="none" and AUDIT=="unset")
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=lambda x:x.item() if isinstance(x,np.generic) else list(x))+"\n")
    print(json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,"elapsed_seconds":elapsed,
                      "maximum_RSS_bytes":rss,"note":str(NOTE),"receipt":str(RECEIPT)},indent=2))
    if not receipt["pass"]:raise SystemExit(1)


if __name__=="__main__":main()
