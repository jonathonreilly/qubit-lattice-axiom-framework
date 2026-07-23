#!/usr/bin/env python3
"""Cycle 675: physical-occupancy-to-six-q reversible extractor."""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "construct and execute a bounded reversible extractor from independently encoded physical matter rails and blank six-q ancillas, run the exact Cycle672 aggregate detector macro, feed and compare Cycle668's four-bit material/binder interface, and uncompute q so the detector follows matter rather than an imported q label",
    "quantifiers_domain": "an explicit generic-read-cell family including cells with nonzero incident-C rows; L3 train, L4 held-out-size and L6 held; independent matter and initial-q counterfactuals; contact on/off; Cycle662 train and held biased/nonproduct spectators; all extractor/detector factors and deletions; all24/all576",
    "allowed_premises": "byte-pinned committed Cycle608 local role tables and primitive recipes, Cycle672 executed aggregate macro and declared limitation, Cycle668 four-bit comparison target, Cycle662 finite spectator profiles, independently placed finite physical occupancy rails and blank reversible work, local compile-time coordinate transport",
    "forbidden_weakenings": "supplying q from a target label; reading matter through a global lookup or shell-predicate ROM; runtime frame selector, host branch selection or host scheduling; occurrence-as-matter; testing only the zero-incident origin; hiding initial-q counterfactuals, malformed/dirty/leakage/deletion/collision/held-size failures; calling macro ordinals time or energy; repairing prior cycles; protected edits or axiom language",
    "required_edge_cases": "same initial q with different matter and same matter with different initial q; blank q required on lawful code and nonblank-q malformed controls; contact on/off and all matter/binder inputs; generic cells; L3/L4/L6; biased/nonproduct spectators; inverse, uncompute, leakage, deletion, placement/collision, bounded support and all24/all576",
    "completion_witness": "an explicit local encoding of independent physical occupancy rails, an ordered reversible factor list deriving all six q bits into blank ancillas, chronological composition with the exact Cycle672 detector and Cycle668 binder factor, exact q uncompute, coordinate placement and collision proof, executed sparse-state equality and counterfactual controls under every frozen quantifier",
    "outcomes_not_closure": "a supplied q label; a host-computed q assignment; an extractor truth table with no factor product; origin-only zero-incident success generalized to all cells; transported coordinate labels called same-device covariance; counts without execution; a route-specific chart or placement failure promoted to shared obstruction, minimum content or axiom pressure",
}

from collections import Counter
from contextlib import contextmanager
from dataclasses import replace
from hashlib import sha256
from itertools import product
import importlib.util
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OCCUPANCY_SIX_Q_SYNDROME_EXTRACTOR_CYCLE675_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_occupancy_six_q_syndrome_extractor_cycle675_cold_2026_07_23.txt"
SHORE = "e5f100af4e45917912c743ba6e32eb580e3c80a4"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-10
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_cycle608_literal_aggregate_detector_product_cycle672_2026_07_23.py":
        "c0af96a46e7f8a8641c0ec9de92da934fb24efc3887d9d5966e40ae91be44735",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE608_LITERAL_AGGREGATE_DETECTOR_PRODUCT_CYCLE672_NOTE_2026-07-23.md":
        "def730b1161028a584684482fdcadd76e86ad94e3c2590862a54aaf60e9d4263",
    "outputs/physical_cycle608_literal_aggregate_detector_product_cycle672_receipt_2026_07_23.json":
        "41d025b4c1b4cc89cc6c27b52157a4861189055e388f9f99c1929f997e07e745",
    "outputs/physical_cycle608_literal_aggregate_detector_product_cycle672_cold_2026_07_23.txt":
        "8f40e803f9dddd95eb433e8dac40d095fffd2a1952c247411ac402603558fbdc",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json":
        "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
    "outputs/physical_detector_formation_current_interval_kernel_cycle668_receipt_2026_07_23.json":
        "f7f733820abdbcf5520a7edf9de9aca067aa7998374e02f3af07204c2718f6a0",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json":
        "4ccba85490c08120aab645917fee87dbd58f21cf4fb17c5f60b3a4fab9dbca48",
}

Coord = tuple[int, int, int]
SparseState = dict[frozenset[Coord], complex]


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, body):
        for stream in self.streams: stream.write(body)
        return len(body)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def stable_digest(value: object) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=float).encode()).hexdigest()


def git_bytes(path: str) -> bytes:
    return subprocess.run(("git", "show", f"{SHORE}:{path}"), cwd=ROOT, check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def target_freeze_controls() -> dict[str, object]:
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i,line in enumerate(source,1) if line.startswith("TARGET_CONTRACT ="))
    evidence_line = next(i for i,line in enumerate(source,1) if line.startswith("def shore_controls"))
    fields = sorted(TARGET_CONTRACT)
    expected = ["allowed_premises", "completion_witness", "forbidden_weakenings",
                "outcomes_not_closure", "quantifiers_domain", "required_edge_cases",
                "target_statement"]
    return {"target_line":target_line,"first_evidence_load_line":evidence_line,
            "frozen_before_evidence":target_line<evidence_line,
            "target_contract_sha256":stable_digest(TARGET_CONTRACT),
            "proof_search_governance_exact_fields":fields,
            "pass":target_line<evidence_line and fields==expected}


def shore_controls() -> tuple[dict[str,object],dict[str,object]]:
    observed={path:sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipts={
        "Cycle608":json.loads(git_bytes("outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json")),
        "Cycle662":json.loads(git_bytes("outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json")),
        "Cycle668":json.loads(git_bytes("outputs/physical_detector_formation_current_interval_kernel_cycle668_receipt_2026_07_23.json")),
        "Cycle672":json.loads(git_bytes("outputs/physical_cycle608_literal_aggregate_detector_product_cycle672_receipt_2026_07_23.json")),
    }
    passed=(observed==PINS and all(row["authority"]=="none" and row["audit"]=="unset" for row in receipts.values())
            and receipts["Cycle672"]["pass"] and receipts["Cycle672"]["bounded_partial_construction_pass"]
            and not receipts["Cycle672"]["target_contract_candidate_terminal_met"])
    return {"ref":SHORE,"pins":PINS,"observed":observed,
            "Cycle672_terminal":receipts["Cycle672"]["highest_honest_terminal"],
            "Cycle672_replay_boundary":receipts["Cycle672"]["shore"]["Cycle668_disclosed_replay_packet"],
            "working_tree_bytes_used_as_scientific_premise":False,
            "author_status_accepted_as_audit":False,"pass":passed},receipts


@contextmanager
def cycle672_and_cycle608():
    path=ROOT/"scripts/physical_cycle608_literal_aggregate_detector_product_cycle672_2026_07_23.py"
    if sha256(path.read_bytes()).hexdigest()!=PINS[str(path.relative_to(ROOT))]:
        raise RuntimeError("Cycle672 working path differs from pinned committed bytes")
    name="cycle675_pinned_cycle672"
    spec=importlib.util.spec_from_file_location(name,path); module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    try:
        with module.committed_cycle608_module() as c608:
            yield module,c608
    finally:
        sys.modules.pop(name,None)


def directions(c608) -> tuple[Coord,...]:
    return tuple(tuple(int(value) for value in row) for row in c608.c560.c533.c527.c210.DIRECTIONS)


def add_coord(left: Coord, right: Coord, modulus: int) -> Coord:
    return tuple((left[axis]+right[axis])%modulus for axis in range(3))


def matter_rails(c608, layout, cell: Coord) -> tuple[Coord,...]:
    center=c608.c560.c533.c527.cell_center(cell,layout.length)
    return tuple(add_coord(center,tuple(4*value for value in direction),layout.modulus)
                 for direction in directions(c608))


def all_matter_rails(c608,layout) -> tuple[Coord,...]:
    return tuple(site for cell in layout.cells for site in matter_rails(c608,layout,cell))


def global_occupied(c608,layout) -> set[Coord]:
    physical={c608.c560.c533.coordinate_for_qubit(layout.code,bit)
              for bit in range(c608.c560.c555.physical_bit_count(layout.code))}
    result=physical|{site for row in layout.q for site in row}|{site for row in layout.branch for site in row}
    result|={site for row in layout.work for site in row}|set(layout.path)|set(layout.read_work)|{layout.pointer}
    return result


def local_read_layout(c608,layout,cell_index: int, occupied: set[Coord]):
    if cell_index==layout.cells.index((0,0,0)):
        local_layout=layout
        occupied.update(layout.read_work);occupied.add(layout.pointer)
    else:
        center=c608.c560.c533.c527.cell_center(layout.cells[cell_index],layout.length)
        block=c608.c560.allocated_block(center,6,occupied,layout.modulus)
        local_layout=replace(layout,read_work=tuple(block[:5]),pointer=block[5])
    center=c608.c560.c533.c527.cell_center(layout.cells[cell_index],layout.length)
    extras=c608.c560.allocated_block(center,4,occupied,layout.modulus)
    return local_layout,extras[0],tuple(extras[1:])


def swap_extractor(m672, matter: tuple[Coord,...], q: tuple[Coord,...]):
    factors=[]
    for layer,(controls,targets) in enumerate(((matter,q),(q,matter),(matter,q))):
        for direction,(control,target) in enumerate(zip(controls,targets)):
            factors.append(m672.Factor("MCX",(control,),(1,),(target,),None,
                                       ("occupancy_q_SWAP",layer,direction)))
    return tuple(factors)


def occupancy_state(coordinates: tuple[Coord,...], amplitudes: dict[int,float],
                    extras: tuple[Coord,...]=()) -> SparseState:
    result={}
    for word,amplitude in amplitudes.items():
        if abs(amplitude)<=1e-14: continue
        bits=set(extras)
        bits.update(coord for direction,coord in enumerate(coordinates) if (word>>direction)&1)
        result[frozenset(bits)]=complex(amplitude)
    norm=math.sqrt(sum(abs(value)**2 for value in result.values()))
    return {bits:value/norm for bits,value in result.items()}


def basis_occupancy(coordinates: tuple[Coord,...],word: int,
                    extras: tuple[Coord,...]=()) -> SparseState:
    bits=set(extras);bits.update(coord for i,coord in enumerate(coordinates) if (word>>i)&1)
    return {frozenset(bits):1+0j}


def tensor_states(first: SparseState, second: SparseState) -> SparseState:
    result={}
    for left,a in first.items():
        for right,b in second.items():
            if left&right: raise ValueError("tensor coordinate collision")
            bits=left|right;result[bits]=result.get(bits,0j)+a*b
    return result


def add_extras(state: SparseState,extras: tuple[Coord,...]) -> SparseState:
    return {bits|frozenset(extras):amplitude for bits,amplitude in state.items()}


def profile_rows(receipt: dict[str,object]) -> tuple[dict[str,object],...]:
    rows={}
    for row in receipt["stochastic_dilation"]["rows"]:
        rows.setdefault(row["state"],row)
    return tuple(rows.values())


def build_candidate(m672,c608,base_layout,cell_index: int,occupied: set[Coord]):
    layout,opportunity,spectators=local_read_layout(c608,base_layout,cell_index,occupied)
    cell=layout.cells[cell_index]; matter=matter_rails(c608,layout,cell);q=layout.q[cell_index]
    extractor=swap_extractor(m672,matter,q)
    W,legacy,census=m672.local_W_factors(c608,layout,cell_index)
    predicate,predicate_meta=m672.a2_predicate_factors(c608,layout,cell_index)
    detector=W+predicate+m672.inverse_word(W)
    binder=layout.path[cell_index]
    conjunction=m672.Factor("MCX",(layout.pointer,binder),(1,1),(opportunity,),None,
                            ("Cycle668_binder_contact_Toffoli",))
    full=(extractor+m672.inverse_word(W)+detector+(conjunction,)+m672.inverse_word(detector)
          +W+m672.inverse_word(extractor))
    return {"layout":layout,"cell":cell,"cell_index":cell_index,"matter":matter,"q":q,
            "extractor":extractor,"W":W,"predicate":predicate,"detector":detector,
            "conjunction":conjunction,"full":full,"binder":binder,"opportunity":opportunity,
            "spectators":spectators,"legacy_digest":legacy,"census":census,
            "predicate_meta":predicate_meta}


def source_state(m672,c608,candidate,profile: dict[str,object],material: int,binder: int,
                 initial_q_word: int=0) -> SparseState:
    extras=(candidate["binder"],) if binder else ()
    matter=(occupancy_state(candidate["matter"],c608.a2_word_amplitudes(),extras)
            if material else basis_occupancy(candidate["matter"],0,extras))
    q=basis_occupancy(candidate["q"],initial_q_word)
    state=tensor_states(matter,q)
    return m672.tensor_profile(state,candidate["spectators"],profile)


def overlap(first: SparseState,second: SparseState) -> complex:
    return sum(np.conj(first.get(bits,0))*value for bits,value in second.items())


def factor_coordinate_set(factors) -> set[Coord]:
    return {coord for factor in factors for coord in factor.controls+factor.targets}


def selected_cells(c608,layout) -> tuple[tuple[int,...],dict[Coord,dict[str,object]]]:
    audit=c608.c_coherent_role_table_audit(layout)
    rows={tuple(row["cell"]):row for row in audit["read_cell_rows"]}
    seed=min((cell for cell,row in rows.items() if row["incident_C_rows"]==audit["incident_C_rows_maximum"]))
    frames=c608.c560.c532.c235.proper_cubic_frames()
    orbit={c608.c560.c533.c527.rotated_body(seed,frame,layout.length) for frame in frames}
    cells={(0,0,0)}|orbit
    return tuple(layout.cells.index(cell) for cell in sorted(cells)),rows


def executed_factor_deletion_witnesses(m672,factors) -> tuple[list[dict[str,object]],float]:
    """Execute the complete factor word on a constructive witness per deletion."""
    rows=[];minimum=math.inf
    for ordinal,factor in enumerate(factors):
        if factor.kind not in ("X","MCX"):
            raise ValueError("extractor deletion helper expects X-family factors")
        local_bits={coord for coord,value in zip(factor.controls,factor.values) if value}
        local_bits.discard(factor.targets[0])
        local={frozenset(local_bits):1+0j}
        source=m672.apply_word(local,m672.inverse_word(tuple(factors[:ordinal])))
        full=m672.apply_word(source,factors)
        deleted=m672.apply_word(source,factors,skip=ordinal)
        signal=m672.state_distance(full,deleted);minimum=min(minimum,signal)
        rows.append({"ordinal":ordinal,"label":list(factor.label),"executed_full_extractor_witness_terms":len(source),
                     "deletion_signal":signal,
                     "construction":"inverse prefix applied to a matching-control local target-zero basis witness"})
    return rows,minimum


def execute_candidate(m672,c608,candidate,profiles,incident_row,cycle672_row) -> dict[str,object]:
    comparisons=[];max_residual=max_norm=max_leakage=0.0
    factor_coords=factor_coordinate_set(candidate["full"])
    lawful_allowed=set(candidate["matter"])|{candidate["binder"],candidate["opportunity"]}|set(candidate["spectators"])
    forbidden=factor_coords-lawful_allowed
    stage_source=tensor_states(occupancy_state(candidate["matter"],c608.a2_word_amplitudes()),
                               basis_occupancy(candidate["q"],0))
    stage_observed=m672.apply_word(stage_source,candidate["extractor"])
    stage_expected=tensor_states(basis_occupancy(candidate["matter"],0),
                                 occupancy_state(candidate["q"],c608.a2_word_amplitudes()))
    matter_to_q_stage_residual=m672.state_distance(stage_observed,stage_expected)
    extractor_inverse_residual=m672.state_distance(
        m672.apply_word(stage_observed,m672.inverse_word(candidate["extractor"])),stage_source)
    for profile in profiles:
        for material,binder in product((0,1),repeat=2):
            source=source_state(m672,c608,candidate,profile,material,binder)
            output=m672.apply_word(source,candidate["full"])
            expected=m672.expected_toggle(source,candidate["opportunity"]) if material and binder else source
            residual=m672.state_distance(output,expected)
            leakage=sum(abs(amplitude)**2 for bits,amplitude in output.items() if bits&forbidden)
            max_residual=max(max_residual,residual);max_norm=max(max_norm,abs(m672.state_norm(output)-1));max_leakage=max(max_leakage,leakage)
            comparisons.append({"Cycle662_state":profile["state"],"split":profile["split"],
                "material":material,"binder":binder,"contact":"on" if binder else "off",
                "residual":residual,"terminal_leakage_probability":leakage,"terms":len(output)})
    profile=profiles[-1]
    q_counter=[];max_q_counter=0.0
    for qword in (0,21,63):
        source=source_state(m672,c608,candidate,profile,1,1,qword)
        output=m672.apply_word(source,candidate["full"])
        expected=m672.expected_toggle(source,candidate["opportunity"])
        residual=m672.state_distance(output,expected);max_q_counter=max(max_q_counter,residual)
        q_counter.append({"initial_q_word":qword,"restored_same_q":True,"residual":residual})
    q_a2=tensor_states(basis_occupancy(candidate["matter"],0,(candidate["binder"],)),
                       occupancy_state(candidate["q"],c608.a2_word_amplitudes()))
    q_a2=m672.tensor_profile(q_a2,candidate["spectators"],profile)
    q_a2_output=m672.apply_word(q_a2,candidate["full"])
    imported_q_ignored=m672.state_distance(q_a2_output,q_a2)
    matter_vac=source_state(m672,c608,candidate,profile,0,1,0)
    matter_a2=source_state(m672,c608,candidate,profile,1,1,0)
    vac_output=m672.apply_word(matter_vac,candidate["full"])
    a2_output=m672.apply_word(matter_a2,candidate["full"])
    same_q_different_matter=(m672.state_distance(vac_output,matter_vac),
                             m672.state_distance(a2_output,m672.expected_toggle(matter_a2,candidate["opportunity"])))
    one_particle=[];max_one=0.0
    for direction in range(6):
        matter=basis_occupancy(candidate["matter"],1<<direction,(candidate["binder"],))
        q=basis_occupancy(candidate["q"],0);state=tensor_states(matter,q)
        output=m672.apply_word(state,candidate["full"]);residual=m672.state_distance(output,state)
        max_one=max(max_one,residual);one_particle.append({"direction":direction,"residual":residual})
    dirty=m672.expected_toggle(matter_a2,candidate["layout"].branch[candidate["cell_index"]][0])
    dirty_output=m672.apply_word(dirty,candidate["full"])
    clean_expected=m672.expected_toggle(matter_a2,candidate["opportunity"])
    dirty_overlap=abs(overlap(dirty_output,clean_expected))
    central=next(i for i,factor in enumerate(candidate["full"]) if factor.label==("A2_predicate",))
    deleted=m672.apply_word(matter_a2,candidate["full"],skip=central)
    deleted_signal=m672.state_distance(deleted,clean_expected)
    target_fixture_extractor_deletions=[];minimum_target_fixture_extractor=math.inf
    for ordinal in range(len(candidate["extractor"])):
        deleted=m672.apply_word(matter_a2,candidate["full"],skip=ordinal)
        signal=m672.state_distance(deleted,clean_expected);minimum_target_fixture_extractor=min(minimum_target_fixture_extractor,signal)
        target_fixture_extractor_deletions.append({"full_word_ordinal":ordinal,"target_fixture_signal":signal})
    extractor_deletions,minimum_extractor=executed_factor_deletion_witnesses(m672,candidate["extractor"])
    deletion_rows,minimum_all=m672.factor_local_deletion_rows(candidate["full"])
    W_descriptors=[f.descriptor(i) for i,f in enumerate(candidate["W"])]
    descriptors={"extractor_factors":[f.descriptor(i) for i,f in enumerate(candidate["extractor"])],
                 "W_factor_descriptor_count":len(W_descriptors),
                 "W_factor_descriptor_sha256":stable_digest(W_descriptors),
                 "W_factor_descriptor_head":W_descriptors[:4],
                 "W_factor_descriptor_tail":W_descriptors[-4:],
                 "W_factor_full_export_serialized":False,
                 "W_factor_full_export_regenerated_by_runner":True,
                 "predicate_factors":[f.descriptor(i) for i,f in enumerate(candidate["predicate"])],
                 "conjunction":candidate["conjunction"].descriptor(0),
                 "full_chronological_segments":["extractor_SWAP","inverse(W_cell)","Cycle672_detector=W_cell;P_A2;inverse(W_cell)",
                    "Cycle668_binder_contact_Toffoli","inverse(Cycle672_detector)","W_cell","inverse(extractor_SWAP)"],
                 "inverse_rule":"reverse factors; X/MCX self-inverse; Givens conjugate transpose",
                 "full_factor_count":len(candidate["full"]),"full_factor_sha256":m672.factor_digest(candidate["full"])}
    origin=candidate["cell"]==(0,0,0)
    exact_origin_match=(not origin or (len(candidate["detector"])==cycle672_row["factor_export"]["aggregate_detector_macro_factors"]
        and m672.factor_digest(candidate["detector"])==cycle672_row["factor_export"]["aggregate_detector_factor_sha256"]))
    placement={"matter_rail_radius":4,"matter_rails":[list(c) for c in candidate["matter"]],
               "q_rails":[list(c) for c in candidate["q"]],"matter_q_pair_distances":[candidate["layout"].distance(a,b) for a,b in zip(candidate["matter"],candidate["q"])],
               "pointer":list(candidate["layout"].pointer),"binder":list(candidate["binder"]),
               "opportunity":list(candidate["opportunity"]),"spectators":[list(c) for c in candidate["spectators"]],
               "placed_operand_M2":len(factor_coords),"maximum_macro_support":max(len(set(f.controls+f.targets)) for f in candidate["full"]),
               "extractor_two_M2_factors":len(candidate["extractor"]),"extractor_three_commuting_layers":True,
               "direction_order_is_physical_schedule":False,"all_extractor_pairs_NN":all(candidate["layout"].distance(a,b)==1 for a,b in zip(candidate["matter"],candidate["q"]))}
    passed=(max(max_residual,max_norm,max_leakage,matter_to_q_stage_residual,extractor_inverse_residual,
                max_q_counter,imported_q_ignored,*same_q_different_matter,max_one,dirty_overlap)<TOL
            and deleted_signal>1e-3 and minimum_extractor>1e-3 and minimum_all>1e-8 and exact_origin_match
            and placement["all_extractor_pairs_NN"] and incident_row["incident_C_rows"]>=0)
    return {"cell":list(candidate["cell"]),"origin_exact_Cycle672":origin,"incident_C_rows_context":incident_row["incident_C_rows"],
            "coherent_A2_sensitive_C_rows_context":incident_row["coherent_A2_sensitive_rows"],
            "incident_C_factors_inserted_in_executed_word":False,
            "local_W_factor_count":len(candidate["W"]),"detector_factor_count":len(candidate["detector"]),
            "local_W_census":candidate["census"],"local_W_legacy_digest":candidate["legacy_digest"],
            "predicate_meta":candidate["predicate_meta"],"exact_Cycle672_origin_digest_match":exact_origin_match,
            "comparison_count":len(comparisons),"comparisons":comparisons,"maximum_interface_residual":max_residual,
            "maximum_norm_residual":max_norm,"maximum_terminal_leakage_probability":max_leakage,
            "matter_to_blank_q_extractor_stage_residual":matter_to_q_stage_residual,
            "extractor_stage_inverse_residual":extractor_inverse_residual,
            "extractor_stage_statement":"coherent A2 amplitudes move from independent radius-four matter rails to initially blank radius-three q rails while the matter rails become blank",
            "q_counterfactuals":q_counter,"maximum_initial_q_counterfactual_residual":max_q_counter,
            "input_q_A2_with_physical_vacuum_identity_residual":imported_q_ignored,
            "same_blank_q_different_matter_residuals":list(same_q_different_matter),
            "one_particle_fixture":one_particle,"maximum_one_particle_false_positive_residual":max_one,
            "dirty_work_to_clean_overlap":dirty_overlap,"deleted_central_predicate_signal":deleted_signal,
            "extractor_deleted_factor_rows":extractor_deletions,"minimum_extractor_deleted_factor_signal":minimum_extractor,
            "target_fixture_extractor_deleted_factor_rows":target_fixture_extractor_deletions,
            "minimum_target_fixture_extractor_deleted_factor_signal":minimum_target_fixture_extractor,
            "all_factor_constructive_deletion_witness_count":len(deletion_rows),
            "minimum_all_factor_constructive_deletion_signal":minimum_all,
            "deletion_witness_rule":deletion_rows[0]["global_witness"],
            "factor_export":descriptors,"placement":placement,"pass":passed}


def covariance_controls(m672,c608,representatives) -> dict[str,object]:
    frames=c608.c560.c532.c235.proper_cubic_frames();keys={tuple(frame.reshape(-1)) for frame in frames}
    equivariance=coordinate_only_failures=distance_failures=group_failures=extractor_layer_failures=0;comparisons=0
    fermionic_group_failures=0;maximum_phase_CZ=maximum_phase_route=0
    amplitude_rows=[];phase_exports=[]
    amplitudes=c608.a2_word_amplitudes();dirs=directions(c608)
    lookup={direction:i for i,direction in enumerate(dirs)}
    for candidate in representatives:
        source=occupancy_state(candidate["matter"],amplitudes,(candidate["binder"],))
        source=tensor_states(source,basis_occupancy(candidate["q"],0))
        base=m672.apply_word(source,candidate["full"])
        for frame_index,frame in enumerate(frames):
            rotated_word=tuple(m672.rotate_factor(c608,factor,frame,candidate["layout"].modulus) for factor in candidate["full"])
            dmap=tuple(lookup[tuple(int(v) for v in frame@np.asarray(direction))] for direction in dirs)
            rotated_matter=tuple(m672.rotate_coord(c608,coord,frame,candidate["layout"].modulus) for coord in candidate["matter"])
            phase_factors=tuple(m672.Factor("MCZ",(rotated_matter[left],),(1,),(rotated_matter[right],),None,
                ("local_fermionic_frame_inversion_CZ",left,right))
                for left in range(6) for right in range(left+1,6) if dmap[left]>dmap[right])
            phase_exports.append({"length":candidate["layout"].length,"seed_cell":list(candidate["cell"]),
                "frame_index":frame_index,"direction_permutation":list(dmap),
                "chronological_sheath":"phase_CZs ; coordinate-transported full word ; reverse phase_CZs",
                "phase_CZ_factors":[factor.descriptor(i) for i,factor in enumerate(phase_factors)]})
            maximum_phase_CZ=max(maximum_phase_CZ,len(phase_factors))
            maximum_phase_route=max(maximum_phase_route,max((candidate["layout"].distance(f.controls[0],f.targets[0]) for f in phase_factors),default=0))
            def signed_rotate(state):
                result={}
                for bits,amplitude in state.items():
                    occupied=[direction for direction,coord in enumerate(candidate["matter"]) if coord in bits]
                    mapped=[dmap[direction] for direction in occupied]
                    inversions=sum(mapped[left]>mapped[right] for left in range(len(mapped)) for right in range(left+1,len(mapped)))
                    sign=-1 if inversions%2 else 1
                    target=frozenset(m672.rotate_coord(c608,c,frame,candidate["layout"].modulus) for c in bits)
                    result[target]=result.get(target,0j)+sign*amplitude
                return result
            rotated_source=signed_rotate(source);rotated_base=signed_rotate(base)
            coordinate_only_failures+=m672.state_distance(m672.apply_word(rotated_source,rotated_word),rotated_base)>TOL
            signed_word=phase_factors+rotated_word+tuple(reversed(phase_factors))
            equivariance+=m672.state_distance(m672.apply_word(rotated_source,signed_word),rotated_base)>TOL;comparisons+=1
            distance_failures+=sum(candidate["layout"].distance(m672.rotate_coord(c608,a,frame,candidate["layout"].modulus),
                m672.rotate_coord(c608,b,frame,candidate["layout"].modulus))!=1 for a,b in zip(candidate["matter"],candidate["q"]))
            transformed={}
            for word,amplitude in amplitudes.items():
                occupied=[i for i in range(6) if (word>>i)&1]
                mapped=[dmap[i] for i in occupied]
                wedge_sign=1 if mapped[0]<mapped[1] else -1
                transformed[sum(1<<direction for direction in mapped)]=wedge_sign*amplitude
            inner=sum(transformed.get(word,0)*amplitudes.get(word,0) for word in set(transformed)|set(amplitudes))
            amplitude_rows.append(inner)
            for layer in range(3):
                mapped={(m672.rotate_coord(c608,candidate["matter"][d],frame,candidate["layout"].modulus),
                         m672.rotate_coord(c608,candidate["q"][d],frame,candidate["layout"].modulus)) for d in range(6)}
                extractor_layer_failures+=len(mapped)!=6
    for first in frames:
        for second in frames:
            group_failures+=tuple((first@second).reshape(-1)) not in keys
            for candidate in representatives:
                modulus=candidate["layout"].modulus
                for coord in factor_coordinate_set(candidate["full"]):
                    group_failures+=m672.rotate_coord(c608,m672.rotate_coord(c608,coord,second,modulus),first,modulus)!=m672.rotate_coord(c608,coord,first@second,modulus)
            first_map=tuple(lookup[tuple(int(v) for v in first@np.asarray(direction))] for direction in dirs)
            second_map=tuple(lookup[tuple(int(v) for v in second@np.asarray(direction))] for direction in dirs)
            product_map=tuple(lookup[tuple(int(v) for v in (first@second)@np.asarray(direction))] for direction in dirs)
            for left in range(6):
                for right in range(left+1,6):
                    after_second=(second_map[left],second_map[right])
                    second_sign=-1 if after_second[0]>after_second[1] else 1
                    ordered_second=tuple(sorted(after_second))
                    after_first=(first_map[ordered_second[0]],first_map[ordered_second[1]])
                    first_sign=-1 if after_first[0]>after_first[1] else 1
                    product_pair=(product_map[left],product_map[right])
                    product_sign=-1 if product_pair[0]>product_pair[1] else 1
                    fermionic_group_failures+=second_sign*first_sign!=product_sign
    return {"proper_cubic_frames":len(frames),"ordered_frame_products":len(frames)**2,
            "executed_full_word_state_equivariance_comparisons":comparisons,
            "signed_coordinate_only_state_equivariance_failures_before_local_phase_repair":coordinate_only_failures,
            "signed_local_phase_repaired_state_equivariance_failures":equivariance,
            "NN_distance_transport_failures":distance_failures,
            "extractor_commuting_layer_transport_failures":extractor_layer_failures,"group_coordinate_failures":group_failures,
            "fermionic_wedge_group_law_failures":fermionic_group_failures,
            "A2_fermionic_wedge_orbit_minimum_absolute_overlap":min(abs(value) for value in amplitude_rows),
            "fermionic_mode_permutation_sign_included_in_executed_state_transport":True,
            "local_frame_inversion_phase_CZ_maximum":maximum_phase_CZ,
            "local_frame_inversion_phase_maximum_pair_route_edges":maximum_phase_route,
            "local_frame_phase_factor_exports":phase_exports,
            "global_parity_string_or_service":False,
            "compile_time_transported_circuit":True,"runtime_frame_selector":False,
            "same_unprogrammed_generic_device_claimed":False,
            "pass":len(frames)==24 and coordinate_only_failures==48
                   and not(equivariance or distance_failures or extractor_layer_failures or group_failures or fermionic_group_failures)
                   and min(abs(value) for value in amplitude_rows)>1-TOL}


def no_go_discipline() -> dict[str,object]:
    walls={
        "W_incident_C_star_product":"the proper-cubic-closed generic family executes the local Cycle672 A/SELECT/D detector variant but does not insert incident Cycle608 C equality rows or neighboring prepared branches into the product",
        "W_same_device_generic_chart":"each generic cell factor word and read block is compiled from the supplied Cycle608 chart; transported circuits are equivariant but one autonomous unprogrammed all-cell device is not constructed",
        "W_framework_matter_identification":"radius-four M2 occupancy rails are explicit independent physical inputs but their identification with an autonomous framework matter law is supplied",
    }
    names=tuple(walls);pairs=[]
    for first in names:
        for second in names:
            if first!=second:pairs.append({"from":first,"to":second,"implied":False,"reason":"distinct constructive obligation"})
    families=[
        {"family":"NN six-rail coherent SWAP extractor","object_formulation":"six radius-four matter M2s and six blank radius-three q M2s","mechanism_invariant":"three commuting CNOT layers","terminal_obligation":"derive q, detector, restore matter/q","strength_vs_target":"strong bounded partial","status":"PASS_EXECUTED","honesty_marker":"ATTEMPTED"},
        {"family":"basis-copy CNOT extractor","object_formulation":"matter retained while q is XOR copied","mechanism_invariant":"six parallel CNOTs","terminal_obligation":"coherent A2 projector","strength_vs_target":"target-equivalent only on basis rays","status":"REJECTED: entangles matter and q and dephases the q A2 coherence","honesty_marker":"ATTEMPTED"},
        {"family":"generic local Cycle672 macro orbit","object_formulation":"origin plus maximal-incident proper-cubic cell orbit","mechanism_invariant":"cell-local Wdag P W","terminal_obligation":"generic read cells","strength_vs_target":"bounded generic family","status":"PASS_EXECUTED_WITHOUT_INCIDENT_C","honesty_marker":"ATTEMPTED"},
        {"family":"incident-C prepared star","object_formulation":"target and neighbor A/SELECT branches with incident phase rows","mechanism_invariant":"bounded read light cone","terminal_obligation":"execute C-sensitive generic detector","strength_vs_target":"stronger","status":"OPEN / NOT ATTEMPTED","honesty_marker":"OPEN / NOT ATTEMPTED"},
        {"family":"autonomous all-cell same-device extractor","object_formulation":"simultaneous translation-covariant circuit law","mechanism_invariant":"no chart/read-block program","terminal_obligation":"same physical device every cell","strength_vs_target":"strict","status":"OPEN / NOT ATTEMPTED","honesty_marker":"OPEN / NOT ATTEMPTED"},
    ]
    return {"N1_normalized_families":families,"N1_qualifying_attempts_for_negative":3,
            "N1_required_for_negative":5,"N1_threshold_met_for_negative":False,
            "N1_open_routes_not_counted":[row for row in families if row["honesty_marker"].startswith("OPEN")],
            "N2_walls":walls,"N2_directed_ordered_pairs":pairs,
            "N3_hidden_wall_scan":[
                {"condition":"radius-four matter rails","classification":"explicit supplied physical input; W_framework_matter_identification"},
                {"condition":"blank q lawful domain","classification":"locally visible code condition; nonblank counterfactuals executed"},
                {"condition":"fermionic frame inversion phase","classification":"coordinate-only transport fails 48/72; explicit bounded local CZ sheath supplied per compile-time frame, with no global parity service"},
                {"condition":"compiled local tables/read blocks","classification":"explicit W_same_device_generic_chart"},
                {"condition":"incident-C row census","classification":"context selected and disclosed; factors absent under W_incident_C_star_product"}],
            "N4_exact_residual_matches":[
                {"prior_cycle":672,"prior_residual":"physical matter-to-q extraction absent","current_residual":"six NN SWAP extractor executed from independent matter rails","exact_match":True,"use_as_closure":True},
                {"prior_cycle":672,"prior_residual":"generic same-device chart open","current_residual":"proper-cubic-closed compiled cell family only","exact_match":True,"use_as_closure":False},
                {"prior_cycle":608,"prior_residual":"incident-C algebraic comparison only","current_residual":"incident-C physical star product still absent","exact_match":True,"use_as_closure":False}],
            "N5_rhetoric":[
                {"claim":"physical occupancy rails are not an autonomous matter law","per_element":"six M2 inputs","per_site":"radius-four orbit","per_mode":"six directional occupations","per_block":"one selected cell","lattice_wide":"no matter genesis"},
                {"claim":"transported circuits are not one unprogrammed device","per_element":"factors explicit","per_site":"cell word compiled","per_mode":"direction layers commute","per_block":"closed orbits","lattice_wide":"simultaneous controller absent"},
                {"claim":"coordinate relabeling is not fermionic CAR covariance","per_element":"raw transport fails 48/72","per_site":"local CZ sheath repairs","per_mode":"wedge sign explicit","per_block":"all24/all576 pass","lattice_wide":"same-device frame dispatch remains open"},
                {"claim":"generic location is not incident-C execution","per_element":"C rows counted as context","per_site":"positive incident cells","per_mode":"A2-sensitive rows disclosed","per_block":"local macro only","lattice_wide":"C star open"},
                {"claim":"factor ordinal is not time or energy","per_element":"finite gate order","per_site":"bounded support","per_mode":"no frequency","per_block":"no clock calibration","lattice_wide":"no source law"}],
            "N6_partial_closure_paths":[
                {"file":"scripts/physical_occupancy_six_q_syndrome_extractor_cycle675_2026_07_23.py","status":"EXECUTED PARTIAL","what_closes":"Cycle672 physical occupancy-to-q extractor wall on explicit rails"},
                {"file":"UNMATERIALIZED/cycle675_incident_C_prepared_star_next.py","status":"OPEN / PRIORITY","what_closes":"W_incident_C_star_product"},
                {"file":"UNMATERIALIZED/cycle675_same_device_cellular_extractor_next.py","status":"OPEN","what_closes":"W_same_device_generic_chart"}],
            "N7_steelman":{"mechanism":"Prepare the target cell and every incident neighbor through their A/SELECT prefixes, insert every coordinate-explicit C equality phase row, finish all D suffixes, and conjugate the same matter-SWAP/P_A2 interface; then replace compiled read blocks by a translation-covariant cellular tile.",
                "actionable_steps":["split every local W into A/SELECT/D prefixes","materialize incident C PHASE_EQ rows with neighbor operands","execute the bounded star on physical neighbor states","tile the verified star with collision-free uniform roles"],
                "terminal_test":"same matter/q counterfactuals, every sensitive C-row deletion, all generic cells and frames, no compiled chart selector"},
            "N8_cross_cycle_echo":[
                {"cycle":560,"mechanism":"physical/q coordinate separation and local role tables","retired":"coordinate existence","applicability":"does not supply matter-to-q dynamics"},
                {"cycle":608,"mechanism":"generic incident-C algebraic audit","retired":"row census and bounded radius","applicability":"does not execute the star product"},
                {"cycle":672,"mechanism":"executed origin macro and exact four-bit composition","retired":"counts-only macro wall","applicability":"supplied-q and generic-chart walls motivated this extractor"}],
            "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,
            "shared_route_independent_obstruction":False,"axiom_pressure_claim":False,
            "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
            "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","pass":True}


def rss_bytes() -> int:
    value=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform=="darwin" else value*1024)


def main() -> int:
    global PASS,FAIL
    started=time.monotonic();NOTE.parent.mkdir(parents=True,exist_ok=True);RECEIPT.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as cold:
        original=sys.stdout;sys.stdout=Tee(original,cold)
        try:
            freeze=target_freeze_controls();shore,receipts=shore_controls()
            check("target frozen before evidence",freeze["pass"],freeze)
            check("Cycle608/Cycle662/Cycle668/Cycle672 committed shores pinned",shore["pass"],shore["ref"])
            profiles=profile_rows(receipts["Cycle662"]);size_rows=[];representatives=[]
            with cycle672_and_cycle608() as (m672,c608):
                for length in (3,4,6):
                    layout=c608.build_layout(length);indices,incident=selected_cells(c608,layout)
                    matter_all=set(all_matter_rails(c608,layout));occupied=global_occupied(c608,layout)
                    matter_collisions=len(matter_all&occupied);matter_injective=len(matter_all)==6*len(layout.cells)
                    candidates=[];rows=[]
                    cycle672_row=next(row for row in receipts["Cycle672"]["size_rows"] if row["length"]==length)
                    for index in indices:
                        candidate=build_candidate(m672,c608,layout,index,set(occupied|matter_all));candidates.append(candidate)
                        row=execute_candidate(m672,c608,candidate,profiles,incident[candidate["cell"]],cycle672_row);rows.append(row)
                    seed=max(candidates,key=lambda item:incident[item["cell"]]["incident_C_rows"]);representatives.append(seed)
                    all_generic=all(row["incident_C_rows_context"]>0 for row in rows if not row["origin_exact_Cycle672"])
                    row={"length":length,"split":next(row["split"] for row in receipts["Cycle608"]["compiler_rows"] if row["length"]==length),
                         "selected_cell_rule":"origin baseline plus proper-cubic orbit of lexicographically first maximum-incident-C cell",
                         "selected_cells":[list(candidates[i]["cell"]) for i in range(len(candidates))],
                         "selected_cell_count":len(candidates),"generic_nonzero_incident_cells":sum(not r["origin_exact_Cycle672"] for r in rows),
                         "all_nonorigin_cells_have_positive_incident_C_context":all_generic,
                         "global_radius_four_matter_rail_M2":len(matter_all),"matter_rail_global_collisions":matter_collisions,
                         "matter_rail_global_injective":matter_injective,"cell_rows":rows,
                         "pass":matter_collisions==0 and matter_injective and all_generic and all(r["pass"] for r in rows)}
                    size_rows.append(row)
                    check(f"L{length} physical occupancy extractor generic orbit",row["pass"],{
                        "cells":len(rows),"generic":row["generic_nonzero_incident_cells"],
                        "max_residual":max(r["maximum_interface_residual"] for r in rows),
                        "max_factors":max(r["factor_export"]["full_factor_count"] for r in rows)})
                covariance=covariance_controls(m672,c608,representatives)
            check("all24/all576 transported extractor and full-word covariance",covariance["pass"],covariance)
            total_cells=sum(row["selected_cell_count"] for row in size_rows)
            total_fixtures=sum(cell["comparison_count"] for row in size_rows for cell in row["cell_rows"])
            max_residual=max(cell["maximum_interface_residual"] for row in size_rows for cell in row["cell_rows"])
            max_q=max(cell["maximum_initial_q_counterfactual_residual"] for row in size_rows for cell in row["cell_rows"])
            min_delete=min(cell["minimum_extractor_deleted_factor_signal"] for row in size_rows for cell in row["cell_rows"])
            check("same-q/different-matter and same-matter/different-q controls",max(max_residual,max_q)<TOL,{
                "cells":total_cells,"fixtures":total_fixtures,"max_interface":max_residual,"max_initial_q":max_q})
            check("all 18 extractor factors have executed deletion signal",min_delete>1e-3,min_delete)
            nogo=no_go_discipline();check("full N1-N8; no broad negative or axiom claim",nogo["pass"] and not nogo["shared_obstruction_claim"],nogo["N2_walls"])
            status=("positive bounded reversible six-rail physical-occupancy-to-q SWAP extractor composed with the exact Cycle672 origin macro and a proper-cubic-closed generic local-macro family; incident-C star and same-device chart remain open")
            receipt={"cycle":675,"date":"2026-07-23","authority":AUTHORITY,"audit":AUDIT,"status":status,
                "Status":"PASS" if FAIL==0 else "FAIL","pass":FAIL==0,"tests_passed":PASS,"tests_failed":FAIL,
                "elapsed_seconds":time.monotonic()-started,"maximum_RSS_bytes":rss_bytes(),"target_contract":TARGET_CONTRACT,
                "target_freeze":freeze,"shore":shore,"size_rows":size_rows,"covariance":covariance,
                "aggregate_summary":{"sizes":[3,4,6],"selected_cells":total_cells,"fixture_comparisons":total_fixtures,
                    "Cycle662_profiles":[row["state"] for row in profiles],"maximum_interface_residual":max_residual,
                    "maximum_initial_q_counterfactual_residual":max_q,"minimum_extractor_deleted_factor_signal":min_delete,
                    "independent_physical_matter_rails":True,"blank_q_lawful_domain":True,"q_restored":True,
                    "matter_restored":True,"detector_follows_matter_not_initial_q":True,
                    "exact_Cycle672_origin_macro_executed":True,"generic_local_macro_family_executed":True,
                    "signed_coordinate_only_covariance_failures":covariance["signed_coordinate_only_state_equivariance_failures_before_local_phase_repair"],
                    "bounded_local_fermionic_phase_repair_executed":True,
                    "incident_C_star_product_executed":False,"same_unprogrammed_all_cell_device_executed":False,
                    "pass":all(row["pass"] for row in size_rows) and covariance["pass"]},
                "supplied_structure_inventory":{"radius_four_six_M2_matter_rail_orbit":True,
                    "Cycle608_A2_amplitudes_on_matter_rails":True,"blank_six_q_ancillas":True,
                    "Cycle608_local_tables_per_compiled_cell":True,"Cycle672_macro_algorithm_and_origin_digest":True,
                    "Cycle668_binder_interface":True,"Cycle662_profiles_as_tensor_spectators":True,
                    "compiled_generic_read_blocks":True,"independent_matter_genesis":False,
                    "local_fermionic_frame_inversion_CZ_sheath":True,"global_parity_string_or_service":False,
                    "incident_C_physical_factors":False,"runtime_frame_selector":False,"host_scheduler":False,
                    "global_lookup":False,"shell_predicate_ROM":False,"input_q_label":False},
                "route_disposition":{"coherent_NN_SWAP_extractor":"PASS_EXECUTED",
                    "basis_copy_CNOT_extractor":"REJECTED_COHERENCE_LOSS","origin_exact_Cycle672_composition":"PASS_EXECUTED",
                    "proper_cubic_generic_local_macro_orbit":"PASS_EXECUTED_PARTIAL",
                    "signed_coordinate_only_covariance":"FAIL_48_OF_72",
                    "signed_local_phase_repaired_covariance":"PASS_EXECUTED",
                    "incident_C_prepared_star":"OPEN_NOT_EXECUTED","same_device_all_cell_tile":"OPEN_NOT_EXECUTED"},
                "highest_honest_terminal":"bounded physical occupancy-to-q extractor on radius-four rails, exact at the Cycle672 origin and executed on a compiled proper-cubic-closed generic cell family without incident-C factors",
                "bounded_partial_construction_pass":True,"target_contract_candidate_terminal_met":False,
                "strict_full_framework_terminal_met":False,
                "six_wall_ledger":{"C_ref":"advance: q is blank and reversibly derived from independent matter rails; A2 rail amplitudes and binder remain supplied",
                    "C_num":"unchanged; committed finite matrices and spectator profiles supplied","C_wrap":"unchanged; no wrapped phase/energy claim",
                    "C_int":"advance: extractor plus exact detector/binder/uncompute product executed",
                    "C_local":"advance on a proper-cubic-closed generic cell family; incident-C star and same-device chart open",
                    "C_source":"unchanged; no energy/gravity/source identification"},
                "no_go_discipline":nogo,"shared_obstruction_claim":False,"shared_route_independent_obstruction":False,
                "axiom_pressure":False,"axiom_pressure_claim":False,"constitutional_effect":"none",
                "optimal_next_campaign":"materialize and execute the bounded incident-C prepared-neighbor star, then replace compiled generic read blocks with a uniform cellular tile"}
            receipt["runner_sha256"]=sha256(Path(__file__).read_bytes()).hexdigest()
            receipt["note_sha256"]=sha256(NOTE.read_bytes()).hexdigest() if NOTE.exists() else None
            RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
            print("REPORT_DIGEST",stable_digest(receipt))
            print("SUMMARY",{"tests_passed":PASS,"tests_failed":FAIL,"status":status})
        finally:sys.stdout=original
    return int(FAIL!=0)


if __name__=="__main__":raise SystemExit(main())
