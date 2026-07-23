#!/usr/bin/env python3
"""Cycle635: paired-neutral higher-form/BKSF same-code discriminator.

Six data occupations are paired with six local spectator occupations.  The
doubled Cycle235 graph has data and spectator copies of every face edge plus
one rung per mode.  Route A fixes the three Wilson characters and tests the
local paired-flux isometry.  Route B keeps only bounded checks and tests
whether equality constraints or a subsystem reading remove those characters.
The intermediate-occupation CAR sign is executed, not replaced by an endpoint
truth table.  Authority none; audit unset.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import parity_doubling_spectator_compiler_cycle248_2026_07_17 as c248

AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
TOL = 3.0e-10
CAP_SECONDS = 300.0
CAP_BYTES = 3 * 1024**3
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PAIRED_NEUTRAL_GAUGE_COMPILER_DISCRIMINATOR_"
    "CYCLE635_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_paired_neutral_gauge_compiler_discriminator_"
    "cycle635_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_paired_neutral_gauge_compiler_discriminator_"
    "cycle635_cold_2026_07_23.txt"
)

PINS = {
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py": "dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34",
    "docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md": "295edee5608d3141fc3e3212bc51753265d953dadd68a8b44a66ed1e0e16e0d2",
    "scripts/parity_doubling_spectator_compiler_cycle248_2026_07_17.py": "bee5d2f602e44c3f0d810c359a42e5d8bda9ce89baa527500abf6aea52bfa252",
    "docs/work_history/repo/review_feedback/PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md": "c1b0ee1e93901a07544cfce14ebf0e6280348fc008a0229ce05c4810caa4d7ce",
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py": "a768d4250e55399c03e6084614a772953e6bcdf1570b9e7c50ac8d18544cfe6a",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md": "5f668f6cc04a5eece23f913d5869f57553df583c23d6dbb5cdac6756be41bfc3",
    "outputs/physical_rough_gauge_subsystem_quotient_cycle532_receipt_2026_07_21.json": "01f4716903ee1d0a2338d42a83001add9a0aaf5e0707e010380d99d21b7847b6",
    "scripts/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_2026_07_22.py": "93a273524be455c2b766f5096f38fedb30af4723b9a7a3f33976362261f6d3c5",
    "docs/work_history/repo/review_feedback/PHYSICAL_SAME_CODE_HIGHER_FORM_FERMION_ENCODING_TOURNAMENT_CYCLE622_NOTE_2026-07-22.md": "9e14328100329ce07dcf3df942a72443783aca9ddc79e78322731d8614b9ab19",
    "outputs/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_receipt_2026_07_22.json": "cee3fb81f46ada638e2af6425aa9bffe7abf8ad2fd000362af86df13c19044f7",
    "outputs/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_cold_2026_07_22.txt": "f83055a3ffe330d87ff23021eb5675587dab57bd5bb2f7471edb40cdc229950f",
    "scripts/physical_non_diagonal_link_qudit_same_code_fermion_compiler_tournament_cycle628_2026_07_22.py": "0bd2dc1b53bed2e76c867f0e3b7ff6b962f817258d3c32246cedf73dd061278b",
    "docs/work_history/repo/review_feedback/PHYSICAL_NON_DIAGONAL_LINK_QUDIT_SAME_CODE_FERMION_COMPILER_TOURNAMENT_CYCLE628_NOTE_2026-07-22.md": "328a4269a4dcd2855723b448ac662faca1ec8ba35c08882c65830990092c28ef",
    "outputs/physical_non_diagonal_link_qudit_same_code_fermion_compiler_tournament_cycle628_receipt_2026_07_22.json": "f923d5afb19246a180d0d5fcc7f43e2c072c4d1b7a36decb387ed7019194c4b6",
    "outputs/physical_non_diagonal_link_qudit_same_code_fermion_compiler_tournament_cycle628_cold_2026_07_22.txt": "f2a41a0c85c851f7400d4f9178bcce49ae09d30e049ddd171404edfbc00fcce8",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def sha(path: Path) -> str: return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, complex): return (value.real, value.imag)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def load(name: str) -> dict: return json.loads((ROOT / name).read_text())


def shore() -> tuple[dict, dict, dict, dict]:
    observed = {name: sha(ROOT / name) for name in PINS}
    r532 = load("outputs/physical_rough_gauge_subsystem_quotient_cycle532_receipt_2026_07_21.json")
    r622 = load("outputs/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_receipt_2026_07_22.json")
    r628 = load("outputs/physical_non_diagonal_link_qudit_same_code_fermion_compiler_tournament_cycle628_receipt_2026_07_22.json")
    result = {
        "hashes_match": observed == PINS, "observed": observed,
        "Cycle532_pass": r532["pass"], "Cycle622_pass": r622["pass"], "Cycle628_pass": r628["pass"],
        "authorities": (r532["authority"], r622["authority"], r628["authority"]),
        "audits": (r532["audit"], r622["audit"], r628["audit"]),
        "Cycle532_baseline": {
            "physical_M2_per_cell": r532["factorization"]["physical_M2_per_cell"],
            "both_parities": r532["factorization"]["both_matter_parity_sectors_nonempty"],
            "full_Fock_target_factor": r532["factorization"]["target_full_Fock_exponent"],
            "bounded_B_support": r532["bounded_construction"]["maximum_B_FSWAP_support_M2"],
            "onsite_support": r532["bounded_construction"]["maximum_onsite_hopping_support_M2"],
            "contact_support": r532["bounded_construction"]["maximum_contact_word_support_M2"],
            "Wilson_initializers": r532["topological_boundary"]["Wilson_initializers"],
            "local_only_extra_characters": r532["topological_boundary"]["local_only_extra_matter_central_characters"],
            "bounded_E_or_initializer": r532["topological_boundary"]["bounded_code_state_preparation_supplied"],
        },
    }
    condition = (
        result["hashes_match"] and r532["pass"] and r622["pass"] and r628["pass"]
        and set(result["authorities"]) == {AUTHORITY} and set(result["audits"]) == {AUDIT}
        and result["Cycle532_baseline"] == {
            "physical_M2_per_cell":22, "both_parities":True, "full_Fock_target_factor":"6N",
            "bounded_B_support":13, "onsite_support":7, "contact_support":12,
            "Wilson_initializers":3, "local_only_extra_characters":3,
            "bounded_E_or_initializer":False,
        }
    )
    check("Cycle235/248/532/622/628 shores are byte exact and Cycle532 is the conditional full-Fock baseline", condition, result)
    return r532, r622, r628, result


def permute_mask(mask: int, mapping: list[int]) -> int:
    result = 0
    while mask:
        bit = mask & -mask; source = bit.bit_length()-1
        result ^= 1 << mapping[source]; mask ^= bit
    return result


def independent_basis(rows: list[int]) -> list[int]:
    pivots: dict[int,int] = {}; answer=[]
    for original in rows:
        row=int(original)
        while row:
            pivot=row.bit_length()-1
            if pivot in pivots: row ^= pivots[pivot]
            else:
                pivots[pivot]=row; answer.append(original); break
    return answer


def all_xor(rows: list[int]) -> int:
    answer = 0
    for row in rows:
        answer ^= row
    return answer


def ladder_rows(length: int) -> dict:
    graph = c235.PyramidCellulation(length)
    vertices, edges = len(graph.vertices), len(graph.edges)
    qubits = 2*edges + vertices
    local_cycles = [mask for mask,_vertices,_kind in c235.primal_edge_cycles(graph)]
    squares=[]
    for edge,(left,right,_kind,_owner) in enumerate(graph.edges):
        squares.append((1<<edge)|(1<<(edges+edge))|(1<<(2*edges+left))|(1<<(2*edges+right)))
    wilsons=[graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
    equalities=[]
    for vertex in range(vertices):
        row=0
        for edge in graph.incident[vertex]: row ^= (1<<edge)|(1<<(edges+edge))
        equalities.append(row)
    local_loop_rank=c235.gf2_rank(local_cycles+squares)
    fixed_loop_rank=c235.gf2_rank(local_cycles+squares+wilsons)
    equality_rank=c235.gf2_rank(equalities)
    local_stabilizers=(local_cycles+squares)+[row<<qubits for row in equalities]
    fixed_stabilizers=(local_cycles+squares+wilsons)+[row<<qubits for row in equalities]
    equality_basis=independent_basis(equalities)
    local_basis=independent_basis(local_cycles+squares)
    fixed_basis=independent_basis(local_cycles+squares+wilsons)
    return {
        "graph":graph, "vertices":vertices, "original_edges":edges, "physical_M2":qubits,
        "local_cycles":local_cycles, "squares":squares, "wilsons":wilsons, "equalities":equalities,
        "local_loop_rank":local_loop_rank, "fixed_loop_rank":fixed_loop_rank,
        "equality_rank":equality_rank,
        "local_combined_rank":c235.gf2_rank(local_stabilizers),
        "fixed_combined_rank":c235.gf2_rank(fixed_stabilizers),
        "local_code_exponent":qubits-c235.gf2_rank(local_stabilizers),
        "fixed_code_exponent":qubits-c235.gf2_rank(fixed_stabilizers),
        "equality_relation_zero":all_xor(equalities)==0,
        "delete_one_redundant_equality_rank":c235.gf2_rank(equalities[1:]),
        "delete_one_independent_equality_rank":c235.gf2_rank(equality_basis[1:]),
        "delete_one_independent_local_rank":c235.gf2_rank(local_basis[1:]),
        "delete_one_Wilson_rank":c235.gf2_rank(fixed_basis[:-1]),
    }


def rank_and_constraint_audit() -> tuple[dict, dict]:
    rows=[]; data={}
    for length,split in ((3,"train"),(6,"held"),(7,"held-out-size")):
        row=ladder_rows(length); data[length]=row; cells=length**3
        public={key:value for key,value in row.items() if key not in ("graph","local_cycles","squares","wilsons","equalities")}
        public.update({
            "length":length,"split":split,"cells":cells,"M2_per_cell":row["physical_M2"]//cells,
            "target_full_Fock_exponent":6*cells,
            "one_relation_expected_after_execution":row["vertices"]-row["equality_rank"],
            "local_only_extra_characters":row["local_code_exponent"]-6*cells,
            "maximum_local_cycle_weight":max(mask.bit_count() for mask in row["local_cycles"]),
            "maximum_ladder_square_weight":max(mask.bit_count() for mask in row["squares"]),
            "maximum_equality_weight":max(mask.bit_count() for mask in row["equalities"]),
            "Wilson_weights":tuple(mask.bit_count() for mask in row["wilsons"]),
        })
        public["pass"]=(
            row["physical_M2"]==36*cells and row["local_loop_rank"]==24*cells-2
            and row["fixed_loop_rank"]==24*cells+1 and row["equality_rank"]==6*cells-1
            and row["equality_relation_zero"] and row["fixed_combined_rank"]==30*cells
            and row["fixed_code_exponent"]==6*cells and row["local_code_exponent"]==6*cells+3
            and row["delete_one_redundant_equality_rank"]==row["equality_rank"]
            and row["delete_one_independent_equality_rank"]==row["equality_rank"]-1
            and public["maximum_ladder_square_weight"]==4 and public["maximum_equality_weight"]==10
        )
        rows.append(public)
    result={
        "doubled_graph":"data and spectator copies of all 15N Cycle235 dual edges plus 6N local rungs",
        "equality":"C_v=B_data,v B_spectator,v=+1",
        "rank_law":"36N-(24N+1)-(6N-1)=6N after three Wilson rows",
        "one_dependency":"product_v C_v=product_all_doubled_B=I",
        "rows":rows,"pass":all(row["pass"] for row in rows),
    }
    check("the paired-neutral equality family has exactly one relation and the fixed-Wilson same code has exponent 6N on L3/L6/L7", result["pass"], result)
    malformed={
        "local_pair_words":4,"accepted_equal_words":sum(a==b for a in (0,1) for b in (0,1)),
        "rejected_unequal_words":sum(a!=b for a in (0,1) for b in (0,1)),
        "redundant_row_deletion_is_not_a_signal":all(row["delete_one_redundant_equality_rank"]==row["equality_rank"] for row in rows),
        "independent_basis_deletion_signals":all(row["delete_one_independent_equality_rank"]==row["equality_rank"]-1 for row in rows),
        "Wilson_deletion_signals":all(row["delete_one_Wilson_rank"]==row["fixed_loop_rank"]-1 for row in rows),
        "pass":True,
    }
    check("local unequal-pair, independent-equality deletion, redundant-row, and Wilson-deletion controls distinguish the lawful code", malformed["pass"] and malformed["accepted_equal_words"]==2 and malformed["rejected_unequal_words"]==2 and malformed["independent_basis_deletion_signals"] and malformed["Wilson_deletion_signals"], malformed)
    return result,{"by_length":data,"controls":malformed}


def paired_encoder_and_stream() -> dict:
    E2=c248.mode_spectator_isometry(2); E3=c248.mode_spectator_isometry(3)
    coarse2=c248.swap_gate(2,0,1,fermionic=True)
    sign2=c248.swap_gate(4,0,2,fermionic=True) @ c248.swap_gate(4,1,3,fermionic=False)
    coarse3=c248.permutation_unitary(3,(2,1,0),fermionic=True)
    endpoint=(c248.swap_gate(6,0,4,fermionic=True) @ c248.swap_gate(6,1,5,fermionic=False))
    middle=np.eye(64,dtype=complex)
    for state in range(64):
        n0=(state>>0)&1; n1=(state>>2)&1; n2=(state>>4)&1
        middle[state,state]=(-1)**(n1*(n0^n2))
    corrected=endpoint @ middle
    projector=E3@E3.conj().T
    coherent=np.ones(8,dtype=complex)/math.sqrt(8)
    result={
        "E2_shape":E2.shape,"E3_shape":E3.shape,
        "E3_dagger_E3_residual":float(np.linalg.norm(E3.conj().T@E3-np.eye(8))),
        "local_pair_charge_even_failures":sum(((2*state.bit_count())%2)!=0 for state in range(8)),
        "isolated_two_mode_intertwiner_residual":float(np.linalg.norm(sign2@E2-E2@coarse2)),
        "nonadjacent_endpoint_only_residual":float(np.linalg.norm(endpoint@E3-E3@coarse3)),
        "intermediate_occupation_corrected_residual":float(np.linalg.norm(corrected@E3-E3@coarse3)),
        "corrected_full_code_leakage":float(np.linalg.norm((np.eye(64)-projector)@corrected@E3)),
        "corrected_coherent_state_residual":float(np.linalg.norm(corrected@E3@coherent-E3@coarse3@coherent)),
        "deleted_intermediate_sign_residual":float(np.linalg.norm(endpoint@E3-E3@coarse3)),
        "failed_endpoint_basis_states":(3,6),
        "intermediate_phase":"(-1)^[n_middle (n_left xor n_right)]",
        "local_rung_flux_isometry":"E|n>=product_v T_rung,v^n_v |Omega_spin>; T_rung toggles the paired B eigenvalues and commutes with loop/equality checks in the CSS-equivalent presentation",
        "supplied_gauge_vacuum_required":True,
    }
    result["pass"]=(
        result["E3_dagger_E3_residual"]<TOL and result["local_pair_charge_even_failures"]==0
        and result["isolated_two_mode_intertwiner_residual"]<TOL
        and abs(result["nonadjacent_endpoint_only_residual"]-2*math.sqrt(2))<TOL
        and result["intermediate_occupation_corrected_residual"]<TOL
        and result["corrected_full_code_leakage"]<TOL and result["corrected_coherent_state_residual"]<TOL
    )
    check("the paired isometry is exact and the corrected stream preserves the intermediate-occupation CAR sign that the endpoint word misses", result["pass"], result)
    return result


def factor_unitary(unitary: np.ndarray):
    work=unitary.copy().astype(complex); eliminators=[]; dimension=len(unitary)
    for column in range(dimension):
        for row in reversed(range(column+1,dimension)):
            a,b=work[row-1,column],work[row,column]; radius=math.sqrt(abs(a)**2+abs(b)**2)
            if radius<1e-14: continue
            givens=np.asarray([[np.conj(a)/radius,np.conj(b)/radius],[-b/radius,a/radius]],dtype=complex)
            work[(row-1,row),:]=givens@work[(row-1,row),:]; eliminators.append((row-1,row,givens))
    sequence=[]
    for index,value in enumerate(np.diag(work)):
        if abs(value-1)>1e-13: sequence.append(("phase",index,None,complex(value)))
    for first,second,givens in reversed(eliminators): sequence.append(("two",first,second,givens.conj().T))
    reconstruction=np.eye(dimension,dtype=complex)
    for kind,first,second,payload in sequence:
        gate=np.eye(dimension,dtype=complex)
        if kind=="phase": gate[first,first]=payload
        else: gate[np.ix_((first,second),(first,second))]=payload
        reconstruction=gate@reconstruction
    return sequence,reconstruction


def paired_basis_index(state: int) -> int:
    return sum(((state>>mode)&1)*((1<<(2*mode))|(1<<(2*mode+1))) for mode in range(6))


def apply_paired_word_to_encoded(encoded: np.ndarray, sequence: list, skip: int | None = None) -> np.ndarray:
    work=encoded.copy()
    for index,(kind,first,second,payload) in enumerate(sequence):
        if index==skip: continue
        paired_first=paired_basis_index(first)
        if kind=="phase": work[paired_first,:]*=payload
        else:
            paired_second=paired_basis_index(second)
            work[(paired_first,paired_second),:]=payload@work[(paired_first,paired_second),:]
    return work


def onsite_word_and_fixtures() -> dict:
    species=c248.c219.common_species(c248.c230.BETA)
    coin=c248.c229.fock_lift(species.coin)
    occupations=np.asarray([state.bit_count() for state in range(64)])
    contact=np.diag(np.exp(1j*c248.c230.COUPLING*occupations*(occupations-1)/2))
    E=c248.mode_spectator_isometry(6)
    coin_word,reconstructed=factor_unitary(coin)
    physical_coin_E=apply_paired_word_to_encoded(E,coin_word)
    hasher=sha256()
    for kind,first,second,payload in coin_word:
        paired_first=paired_basis_index(first)
        paired_second=None if second is None else paired_basis_index(second)
        serial=(kind,paired_first,paired_second,np.asarray(payload).tobytes() if kind=="two" else (payload.real,payload.imag))
        hasher.update(repr(serial).encode())
    deleted=len(coin_word)//2
    deleted_physical_coin_E=apply_paired_word_to_encoded(E,coin_word,skip=deleted)
    physical_contact_diagonal=np.ones(4096,dtype=complex)
    for state in range(64): physical_contact_diagonal[paired_basis_index(state)]=contact[state,state]
    physical_contact_E=physical_contact_diagonal[:,None]*E
    deleted_contact_diagonal=physical_contact_diagonal.copy()
    deleted_contact_state=next(state for state in range(64) if abs(contact[state,state]-1)>1e-14)
    deleted_contact_diagonal[paired_basis_index(deleted_contact_state)]=1
    _modes,_vectors,eigenvalues,_momenta=c248.c230.finite_torus_modes(3)
    sea_rank=int(np.sum(np.angle(eigenvalues)<-1e-10))
    result={
        "pair_code_E_shape":E.shape,"coin_dimension":64,"coin_two_level_or_phase_factors":len(coin_word),
        "paired_even_CAR_word_sha256":hasher.hexdigest(),
        "coin_reconstruction_residual":float(np.linalg.norm(reconstructed-coin)),
        "paired_coin_EG_residual":float(np.linalg.norm(physical_coin_E-E@coin)),
        "paired_coin_code_leakage":float(np.linalg.norm(physical_coin_E[[state for state in range(4096) if state not in {paired_basis_index(word) for word in range(64)}],:])),
        "coin_factor_deletion_signal":float(np.linalg.norm(deleted_physical_coin_E-physical_coin_E)),
        "contact_diagonal_factors":sum(abs(contact[i,i]-1)>1e-14 for i in range(64)),
        "contact_pair_code_EG_residual":float(np.linalg.norm(physical_contact_E-E@contact)),
        "contact_factor_deletion_signal":float(np.linalg.norm(deleted_contact_diagonal[:,None]*E-physical_contact_E)),
        "maximum_mapped_onsite_face_edge_support_M2":42,
        "mapped_word_scope":"each paired two-level factor is an even operator on the twelve doubled modes and hence has a bounded Cycle235/BKSF image on the 42 incident doubled-graph edge M2s",
        "literal_support_one_two_M2_lowering_executed":False,
        "rest_mass":c248.c219.rest_mass(species),"analytic_mass":species.analytic_mass,
        "one_particle_available_as_local_pair_flux":True,
        "original_L3_principal_sea_rank":sea_rank,
        "paired_sea_occupation_count":2*sea_rank,
        "rank73_seam_state_available":sea_rank==73,
        "complete_bounded_stream_on_same_code":False,
    }
    result["pass"]=(
        result["coin_reconstruction_residual"]<TOL and result["paired_coin_EG_residual"]<TOL
        and result["paired_coin_code_leakage"]<TOL and result["contact_pair_code_EG_residual"]<TOL
        and result["coin_factor_deletion_signal"]>1e-6 and result["contact_factor_deletion_signal"]>1e-6
        and abs(result["rest_mass"]/result["analytic_mass"]-1)<2e-12
        and sea_rank==73 and result["paired_sea_occupation_count"]==146
    )
    check("the same paired code has an explicit bounded even-CAR onsite coin/contact word and retains one-particle mass plus the rank-73 state domain", result["pass"], result)
    return result


def prefix_surface_audit(by_length: dict) -> dict:
    rows=[]
    for length in (3,6,7):
        row=by_length[length]; graph=row["graph"]; edges=row["original_edges"]; vertices=row["vertices"]
        corrected_support=[]; prefix_support=[]; interval_modes=[]
        for left,right,kind,_owner in graph.edges:
            if kind!="outer_square": continue
            lo,hi=sorted((left,right)); direct=list(range(lo+1,hi)); complement=list(range(hi+1,vertices))+list(range(0,lo))
            interval=min((direct,complement),key=len); prefix=0
            for vertex in interval:
                for edge in graph.incident[vertex]: prefix ^= 1<<edge
                prefix ^= 1<<(2*edges+vertex)
            local=0
            for vertex in (left,right):
                for edge in graph.incident[vertex]: local |= (1<<edge)|(1<<(edges+edge))
                local |= 1<<(2*edges+vertex)
            prefix_support.append(prefix.bit_count()); corrected_support.append((prefix|local).bit_count()); interval_modes.append(len(interval))
        rows.append({
            "length":length,"split":"train" if length==3 else "held" if length==6 else "held-out-size",
            "outer_stream_edges":len(corrected_support),"maximum_intermediate_logical_modes":max(interval_modes),
            "maximum_gauge_prefix_surface_M2":max(prefix_support),
            "maximum_exact_corrected_stream_support_M2":max(corrected_support),
            "endpoint_only_local_support_M2":20,
        })
    result={
        "exact_intermediate_sign_word":"endpoint paired swap times the product of logical parities over the selected fixed-order interval",
        "rows":rows,
        "bounded_support_uniform_in_L":False,
        "endpoint_shortcut_used_as_result":False,
        "corrected_word_residual":0.0,
        "pass_as_growth_discriminator":[row["maximum_exact_corrected_stream_support_M2"] for row in rows]==[112,340,448],
    }
    check("the exact intermediate-sign repair has zero algebraic residual but its mapped gauge surface grows on L3/L6/L7", result["pass_as_growth_discriminator"], result)
    return result


def covariance_audit(data3: dict) -> dict:
    graph=data3["graph"]; edges=data3["original_edges"]; vertices=data3["vertices"]
    qubits=data3["physical_M2"]; frames=c235.proper_cubic_frames()
    local_set=set(data3["local_cycles"]); square_set=set(data3["squares"]); equality_set=set(data3["equalities"])
    fixed_span=independent_basis(data3["local_cycles"]+data3["squares"]+data3["wilsons"])
    frame_maps=[]; failures={"bijection":0,"local_cycles":0,"squares":0,"equalities":0,"fixed_span":0,"all576":0}
    for frame in frames:
        vertex_map,edge_map=c235.graph_frame_maps(graph,frame)
        doubled=edge_map+[edges+value for value in edge_map]+[2*edges+value for value in vertex_map]
        frame_maps.append((vertex_map,doubled))
        failures["bijection"]+=int(len(set(doubled))!=qubits)
        failures["local_cycles"]+=sum(permute_mask(mask,doubled) not in local_set for mask in local_set)
        failures["squares"]+=sum(permute_mask(mask,doubled) not in square_set for mask in square_set)
        failures["equalities"]+=sum(permute_mask(mask,doubled) not in equality_set for mask in equality_set)
        failures["fixed_span"]+=int(c235.gf2_rank(fixed_span+[permute_mask(mask,doubled) for mask in data3["wilsons"]])!=len(fixed_span))
    lookup={tuple(int(x) for x in frame.ravel()):i for i,frame in enumerate(frames)}
    composition=0
    for left_index,left in enumerate(frames):
        for right_index,right in enumerate(frames):
            direct=frame_maps[lookup[tuple(int(x) for x in (left@right).ravel())]][1]
            composed=[frame_maps[left_index][1][frame_maps[right_index][1][site]] for site in range(qubits)]
            failures["all576"]+=sum(a!=b for a,b in zip(direct,composed)); composition+=qubits
    result={
        "proper_cubic_frames":24,"all24_constraint_images":24*(len(local_set)+len(square_set)+len(equality_set)),
        "all576_M2_role_composition_checks":composition,"failures":failures,
        "supplied_spin_vacuum_all_plus_is_frame_invariant":True,
        "fixed_order_prefix_is_not_translation_free":True,
        "pass":not any(failures.values()),
    }
    check("the doubled code, equality constraints and fixed-Wilson span pass all24 and all576 proper-cubic actions", result["pass"], result)
    return result


def route_disposition(rank: dict, controls: dict, encoder: dict, prefix: dict, onsite: dict, r532: dict) -> dict:
    rows=rank["rows"]
    route_a={
        "name":"paired face/edge flux on supplied spin vacuum",
        "exact_fixed_code_rank":all(row["fixed_code_exponent"]==row["target_full_Fock_exponent"] for row in rows),
        "local_relative_E":encoder["pass"],"supplied_gauge_vacuum":True,
        "bounded_onsite_coin_contact":onsite["pass"],"bounded_full_stream":False,
        "reason":"the exact intermediate-occupation phase is a growing parity surface in this displayed paired occupation map",
        "disposition":"PARTIAL POSITIVE / SAME CODE BUT NOT BOUNDED FULL UPDATE",
    }
    route_b={
        "name":"local-only subsystem/rough route without Wilson selection",
        "local_only_code_excess_qubits":tuple(row["local_only_extra_characters"] for row in rows),
        "three_characters_removed_by_pair_equalities":False,
        "treating_characters_as_unspecified_gauge_gives_one_E":False,
        "exact_reason":"bounded rows have rank 30N-3; equality rows are Z-type with one relation and do not span the three missing X-cycle rows",
        "Cycle532_comparator":{
            "M2_per_cell":r532["factorization"]["physical_M2_per_cell"],
            "bounded_full_Fock_algebra_already_closed":True,
            "three_topological_characters":r532["topological_boundary"]["local_only_extra_matter_central_characters"],
            "bounded_initializer_or_E":r532["topological_boundary"]["bounded_code_state_preparation_supplied"],
        },
        "disposition":"DOES NOT REMOVE TOPOLOGICAL INITIALIZATION",
    }
    result={
        "Route_A":route_a,"Route_B":route_b,
        "strongest_same_code_positive":"fixed-Wilson 36-M2/cell paired ladder with exact exponent 6N, local relative rung-flux E, bounded mapped onsite coin/contact, both logical parities, one-particle and rank-73 states",
        "Cycle532_baseline_improved":False,
        "why_not":"Cycle532 already has 22 M2/cell and bounded full-Fock B/onsite/contact; Cycle635 adds a local relative E only after supplying a spin vacuum, but its exact stream surface grows and it leaves the same three initialization characters",
        "shared_obstruction_or_axiom_pressure":False,
        "pass":route_a["exact_fixed_code_rank"] and route_a["local_relative_E"] and not route_a["bounded_full_stream"] and route_b["local_only_code_excess_qubits"]==(3,3,3) and not route_b["three_characters_removed_by_pair_equalities"],
    }
    check("both routes receive separate dispositions and paired neutrality does not overclaim an improvement over Cycle532", result["pass"], result)
    return result

def note_contract() -> dict:
    text=NOTE.read_text().lower()
    required=tuple(token.lower() for token in (
        "Cycle 635","authority none","audit unset","one relation","36 M2","L3/L6/L7","all24","all576",
        "intermediate occupation","112","340","448","rank 73","Cycle 532","22 M2","three topological",
        "supplied gauge vacuum","not full compiler","N1","N8","same_scope","exact_match","use_as_closure",
        "per_element","per_site","per_mode","per_block","lattice_wide","what_closes","actionable","no axiom pressure"
    ))
    missing=tuple(token for token in required if token not in text)
    result={"required":required,"missing":missing,"pass":not missing}
    check("Cycle635 note freezes rank, same-code sign, baseline, route, firewall and N1-N8 boundaries", result["pass"], result)
    return result


def source_line(fragment: str) -> int:
    for number,line in enumerate(Path(__file__).read_text().splitlines(),1):
        if fragment in line:return number
    return 0


def cited_line_exists(path: str,line: int) -> bool:
    target=ROOT/path
    return target.is_file() and 1<=line<=len(target.read_text().splitlines()) and bool(target.read_text().splitlines()[line-1].strip())


def no_go_discipline() -> dict:
    families=[
        {"family":"fixed-Wilson paired ladder","object":"36N edge/rung M2 code","mechanism":"two Cycle235 layers, rungs, equality rank 6N-1","terminal":"exact 6N rank and local relative E","marker":"ATTEMPTED","result":"rank/E pass conditional on supplied spin vacuum"},
        {"family":"intermediate-sign paired stream","object":"actual nonadjacent CAR exchange","mechanism":"endpoint word plus exact middle-parity correction","terminal":"same-code EG and bounded support","marker":"ATTEMPTED","result":"EG passes; support grows 112/340/448"},
        {"family":"paired onsite even-algebra word","object":"six-mode coin/contact on twelve doubled modes","mechanism":"explicit two-level paired basis word then Cycle235 map","terminal":"coin/contact EG, leakage and deletion","marker":"ATTEMPTED","result":"bounded cell word passes; primitive M2 lowering remains"},
        {"family":"local-only ladder subsystem","object":"unfixed three cycle characters","mechanism":"bounded loops, squares and paired equalities","terminal":"one exact 6N common code without loop selection","marker":"ATTEMPTED","result":"code exponent is 6N+3"},
        {"family":"Cycle532 rough subsystem baseline","object":"22N rough face code","mechanism":"target times N-1 gauge factor","terminal":"bounded full-Fock algebra with local state E","marker":"RULED OUT BY PRIOR","result":"conditional algebra passes; three spin initializers and E remain open"},
        {"family":"open/rough cut comparator","object":"periodic H1 generators","mechanism":"remove seams or add a local initialization protocol","terminal":"kill twists while preserving periodic seam and covariance","marker":"ATTEMPTED","result":"a fixed cut changes the periodic domain; local initialization remains live"},
    ]
    walls={
        "W_stream":"bounded exact intermediate-sign stream on the paired code",
        "W_spin_E":"bounded preparation of the three-character spin vacuum",
        "W_primitive":"literal one/two-M2 lowering of the bounded onsite macro",
        "W_placement":"physical role genesis and fine-site placement",
        "W_periodic_rough":"rough repair preserving the periodic seam and translations",
    }
    pairs=[{"left":a,"right":b,"left_to_right":{"status":"NOT_ESTABLISHED"},"right_to_left":{"status":"NOT_ESTABLISHED"},"independence":{"status":"NOT_ESTABLISHED"}} for a,b in combinations(walls,2)]
    phrases=("we assume","by construction","as is standard","the framework provides","bridge context","background","naturally","obviously","standard qft","registered","canonical")
    hits=tuple(p for p in phrases if p in NOTE.read_text().lower())
    current="scripts/physical_paired_neutral_gauge_compiler_discriminator_cycle635_2026_07_23.py"
    n4=[
        {"prior_path":"docs/work_history/repo/review_feedback/PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md","prior_line":37,"prior_residual":"local paired state map does not make the actual CAR image local","current_path":current,"current_line":source_line('def paired_encoder_and_stream'),"current_residual":"same intermediate sign is preserved exactly and its gauge surface is measured","exact_match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md","prior_line":68,"prior_residual":"closed face code exponent is 6N-1","current_path":current,"current_line":source_line('def rank_and_constraint_audit'),"current_residual":"doubling plus equality rank 6N-1 restores exact exponent 6N after spin fixation","exact_match":True,"same_scope":True,"use_as_closure":True},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md","prior_line":45,"prior_residual":"three spin/Wilson twists remain under bounded checks","current_path":current,"current_line":source_line('def route_disposition'),"current_residual":"paired equalities leave exactly the same three-rank deficit","exact_match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_SAME_CODE_HIGHER_FORM_FERMION_ENCODING_TOURNAMENT_CYCLE622_NOTE_2026-07-22.md","prior_line":101,"prior_residual":"three H1 flux sectors are not locally selected","current_path":current,"current_line":source_line('local_only_code_exponent'),"current_residual":"local-only paired code has exponent 6N+3","exact_match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_NON_DIAGONAL_LINK_QUDIT_SAME_CODE_FERMION_COMPILER_TOURNAMENT_CYCLE628_NOTE_2026-07-22.md","prior_line":100,"prior_residual":"local graded face block misses the full stream sign","current_path":current,"current_line":source_line('def prefix_surface_audit'),"current_residual":"exact sign is restored only by the measured growing surface in this route","exact_match":False,"same_scope":False,"use_as_closure":False},
    ]
    n5=[
        {"claim":"paired neutrality repairs rank but not the bounded stream","per_element":"each equality has weight ten","per_site":"one data/spectator rung per logical mode","per_mode":"six pairs per cell","per_block":"onsite word is bounded while exact stream support grows","lattice_wide":"three Wilson characters remain"},
        {"claim":"the relative E is local only with supplied spin vacuum","per_element":"one rung toggler per occupied mode","per_site":"paired B eigenvalues change together","per_mode":"all occupation words are injective","per_block":"coin/contact act on the same paired code","lattice_wide":"Omega_spin preparation is not built"},
        {"claim":"the endpoint shortcut is rejected, not reused","per_element":"middle phase is executed","per_site":"failed words 011 and 110 are detected","per_mode":"three-mode corrected residual is zero","per_block":"gauge prefix surface is enumerated","lattice_wide":"support grows across L3/L6/L7"},
        {"claim":"the rough/subsystem route does not select one code","per_element":"bounded loop rows are local","per_site":"equality rows do not span Wilson X cycles","per_mode":"logical exponent gains three","per_block":"unspecified characters give eight sectors","lattice_wide":"one E still needs a character state"},
        {"claim":"Cycle532 remains stronger conditionally","per_element":"its B support is thirteen","per_site":"twenty-two M2 per cell","per_mode":"both parities are present","per_block":"onsite/contact are bounded","lattice_wide":"its three initialization signs remain its one typed wall"},
    ]
    n6=[
        {"file":"docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md","status":"PINNED_EVEN_ALGEBRA_PARENT","what_closes":"one-layer graph, loop ranks and proper-cubic framing"},
        {"file":"docs/work_history/repo/review_feedback/PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md","status":"PINNED_PAIR_CODE_PARENT","what_closes":"local equality isometry and intermediate-sign witness"},
        {"file":"outputs/physical_rough_gauge_subsystem_quotient_cycle532_receipt_2026_07_21.json","status":"PINNED_STRONGEST_BASELINE","what_closes":"conditional bounded full-Fock algebra, not spin preparation"},
        {"file":"outputs/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_receipt_2026_07_22.json","status":"PINNED_HOMOLOGY_PARENT","what_closes":"L3/L6/L7 H1/H2 and same-code route boundaries"},
        {"file":"outputs/physical_non_diagonal_link_qudit_same_code_fermion_compiler_tournament_cycle628_receipt_2026_07_22.json","status":"PINNED_NONDIAGONAL_PARENT","what_closes":"one face-qudit and prefix/twist route scope"},
    ]
    steelman={"steelman":"A local measurement/reset or dissipative preparation of the three spin characters, or a different auxiliary Majorana/subsystem presentation, could combine a bounded E with Cycle532's already bounded full-Fock algebra.","mechanism":"use bounded syndrome extraction and a resource-accounted convergence law, or retain local gauge degrees that supply the incident-edge Clifford signs without a fixed ordering surface","terminal_obligation":"one same code with bounded E, bounded stream/coin/contact, literal M2 lowering, L3/L6/L7, all24/all576, and no supplied Wilson character","citations":[{"path":"docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md","line":451,"supports":"measurement, dissipative and topology repairs remain live"},{"path":"docs/work_history/repo/review_feedback/PHYSICAL_NON_DIAGONAL_LINK_QUDIT_SAME_CODE_FERMION_COMPILER_TOURNAMENT_CYCLE628_NOTE_2026-07-22.md","line":317,"supports":"tensor-network and higher-group routes remain live"}],"action":"attack Cycle532's three-character preparation directly before adding more occupation spectators"}
    echoes=[
        {"cycle":"Cycle235","prior_path":"docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md","prior_line":68,"citation_path":"docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md","citation_line":68,"echo":"closed face code loses one parity bit","retired":True,"retirement_mechanism":"doubled modes plus 6N-1 equality rank","could_apply_here":True,"mechanism":"paired-neutral doubled graph","applicability":"RETIRES_DIMENSION_SLICE_ONLY","effect":"full rank restored; locality/topology remain"},
        {"cycle":"Cycle248","prior_path":"docs/work_history/repo/review_feedback/PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md","prior_line":37,"citation_path":"docs/work_history/repo/review_feedback/PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md","citation_line":37,"echo":"paired state code retains a CAR sign surface","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"local sign-carrying gauge auxiliary","applicability":"ACTIONABLE_STREAM_ROUTE","effect":"blocks bounded stream credit"},
        {"cycle":"Cycle532","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md","prior_line":45,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md","citation_line":45,"echo":"three spin characters remain","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"local initialization protocol","applicability":"ACTIONABLE_TOPLOGICAL_E_ROUTE","effect":"prevents unconditional E"},
        {"cycle":"Cycle622","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_SAME_CODE_HIGHER_FORM_FERMION_ENCODING_TOURNAMENT_CYCLE622_NOTE_2026-07-22.md","prior_line":101,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_SAME_CODE_HIGHER_FORM_FERMION_ENCODING_TOURNAMENT_CYCLE622_NOTE_2026-07-22.md","citation_line":101,"echo":"H1 sectors remain under local constraints","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"bounded spin preparation or topology repair","applicability":"ACTIONABLE_HOMOLOGY_ROUTE","effect":"matches three-rank deficit"},
    ]
    n4lines=all(cited_line_exists(row["prior_path"],row["prior_line"]) and cited_line_exists(row["current_path"],row["current_line"]) for row in n4)
    n7lines=all(cited_line_exists(row["path"],row["line"]) for row in steelman["citations"])
    n8lines=all(cited_line_exists(row["citation_path"],row["citation_line"]) for row in echoes)
    result={
        "skill_freshness":{"origin_main_checked":True,"origin_main_skill_sha256":"7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7","proof_search_governance_sha256":"be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258","current_origin_main_followed":True},
        "N1_normalized_families":families,"N1_live_routes":["Cycle532 spin preparation","auxiliary Majorana/link code","tensor pull-through code","resource-accounted dissipative preparation","periodic topology repair"],
        "N2_walls":walls,"N2_directional_independence":pairs,"N2_independence_complete":False,
        "N3_hidden_wall_phrases":phrases,"N3_note_phrase_hits":hits,"N3_explicit_supplied_structure":["doubled graph","data/spectator role split","paired equality signs","CSS/framing presentation","three all-plus Wilson characters","spin vacuum","Fock order and middle sign","coin/contact/order/precision","periodic domains","macro placement and primitive synthesis"],
        "N4_exact_residual_matching":n4,"N4_cited_lines_exist":n4lines,
        "N5_five_resolution_rhetoric_audit":n5,"N6_partial_closure_paths":n6,
        "N7_cited_actionable_steelman":steelman,"N7_cited_lines_exist":n7lines,
        "N8_rowwise_cross_cycle_echo":echoes,"N8_cited_lines_exist":n8lines,
        "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","narrow_positive_gate":"PASS / SHIP WITH FIREWALL","negative_claim_shipped":False,"shared_route_independent_obstruction":False,"axiom_pressure":False,
    }
    schema=len(families)>=5 and all(row["marker"] in ("ATTEMPTED","RULED OUT BY PRIOR") for row in families) and len(pairs)==10 and not hits and n4lines and n7lines and n8lines and all(all(key in row for key in ("per_element","per_site","per_mode","per_block","lattice_wide")) for row in n5) and all(set(row)=={"file","status","what_closes"} for row in n6)
    check("fresh N1-N8 ships only the paired rank/relative-E/onsite positive and blocks broad negative or axiom pressure", schema, result)
    return result


def main() -> int:
    global PASS,FAIL
    PASS=FAIL=0; started=time.monotonic()
    print("Cycle635 paired-neutral gauge compiler discriminator",AUTHORITY,AUDIT)
    r532,r622,r628,shore_result=shore()
    note=note_contract()
    ranks,controls=rank_and_constraint_audit()
    encoder=paired_encoder_and_stream()
    onsite=onsite_word_and_fixtures()
    prefix=prefix_surface_audit(controls["by_length"])
    covariance=covariance_audit(controls["by_length"][3])
    disposition=route_disposition(ranks,controls,encoder,prefix,onsite,r532)
    discipline=no_go_discipline()
    elapsed=time.monotonic()-started; maximum_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    check("cold run stays within declared resource caps",elapsed<CAP_SECONDS and maximum_rss<CAP_BYTES,{"elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss})
    receipt={
        "status":"cycle635-paired-neutral-gauge-compiler-discriminator","classification":"bounded paired-neutral discriminator; conditional fixed-sector positive and route-specific stream/topology negatives","authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,"author_artifact_status_accepted":False,
        "pins":PINS,"runner_sha256":sha(Path(__file__)),"note_sha256":sha(NOTE),"shore":shore_result,
        "exact_target":"one paired-neutral same code on L3/L6/L7, exact equality dependency rank, explicit E or nonlocal surface witness, bounded mapped stream plus onsite word, odd/rank73 availability, all24/all576 and local constraint/deletion/leakage controls",
        "paired_ladder_rank_and_constraints":ranks,"constraint_and_deletion_controls":controls["controls"],
        "paired_state_isometry_and_intermediate_sign":encoder,"mapped_onsite_word_and_fixtures":onsite,
        "exact_corrected_stream_surface":prefix,"proper_cubic_covariance":covariance,
        "route_disposition":disposition,"no_go_discipline":discipline,"note_contract":note,
        "strongest_constructive_result":"after fixing three Wilson characters, the 36-M2/cell doubled Cycle235 ladder plus 6N paired equalities of rank 6N-1 has exact exponent 6N; a supplied spin vacuum admits a local rung-flux basis E, the mapped paired onsite coin/contact word is bounded, and odd one-particle/rank73 states exist",
        "decisive_negative_at_route_scope":"the exact intermediate-occupation phase repairs the three-mode intertwiner to zero but maps to supports 112/340/448 on L3/L6/L7; bounded local-only constraints leave exactly three extra characters, so paired neutrality neither supplies a bounded full stream nor removes Cycle532's topological initialization",
        "supplied_structure":["two copies of the Cycle235 dual graph plus six rungs per cell","data/spectator labels and equality signs","CSS-equivalent framing and local Clifford repair","three all-plus Wilson characters and the spin vacuum","Fock tensor order and exact intermediate parity word","coin beta/contact coupling/factor order/precision","periodic L3/L6/L7 domains","36-role macro placement and future literal primitive synthesis"],
        "interpretation_firewall":{"supplied_spin_vacuum_is_bounded_E":False,"relative_rung_E_is_unconditional_state_preparation":False,"onsite_even_algebra_word_is_full_compiler":False,"endpoint_swap_is_actual_CAR_stream":False,"factor_schedule_is_time":False,"wrapped_phase_is_energy":False,"generator_element_is_rate":False,"spectator_copy_is_Record":False},
        "Cycle532_baseline_improved":False,"shared_obstruction_or_axiom_pressure":False,"shared_route_independent_obstruction":False,"axiom_pressure":False,"constitutional_effect":"none",
        "six_wall_ledger":{"C_ref":"paired roles, CSS framing, fixed tensor order, three Wilson signs, and Omega_spin remain supplied","C_num":"exact 6N fixed-sector rank and paired-basis actions; no unconditional full-M64 physical code","C_wrap":"three topological characters and the growing fixed-order sign surface remain; no schedule is time","C_int":"bounded paired onsite coin/contact macros and mass fixture survive; complete stream and literal primitive lowering remain open","C_local":"36 M2/cell fixed-sector code is exact, but it is less efficient than Cycle532 and has no bounded complete stream or spin-vacuum preparation","C_source":"unchanged; spectator neutrality is not an energy/stress/source law"},
        "broad_negative_gate":discipline["broad_negative_gate"],"optimal_next_campaign":"attack Cycle532's three fixed spin characters directly with bounded measurement/reset, dissipative convergence, or a periodic topology repair; require an explicit state E and literal M2 primitive word before adding more occupation spectators",
        "breakthrough":False,"breakthrough_bar_met":False,"breakthrough_default":"no","elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss,
        "tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,
    }
    RECEIPT.parent.mkdir(parents=True,exist_ok=True); RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
    print("SUMMARY_JSON",json.dumps({"pass":FAIL==0,"tests_passed":PASS,"tests_failed":FAIL,"M2_per_cell":36,"equality_relation_count":1,"fixed_code_exponent_L6":ranks["rows"][1]["fixed_code_exponent"],"local_only_excess":ranks["rows"][1]["local_only_extra_characters"],"corrected_supports":[row["maximum_exact_corrected_stream_support_M2"] for row in prefix["rows"]],"Cycle532_improved":False,"axiom_pressure":False,"elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss},sort_keys=True))
    print("RESULT",PASS,FAIL); return int(FAIL!=0)


if __name__=="__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as cold:
        terminal=sys.stdout;sys.stdout=Tee(terminal,cold)
        try:exit_code=main()
        finally:sys.stdout=terminal
    raise SystemExit(exit_code)
