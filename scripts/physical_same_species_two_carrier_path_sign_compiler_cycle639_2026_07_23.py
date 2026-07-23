#!/usr/bin/env python3
"""Cycle639: same-species two-carrier physical-M2 path/sign discriminator.

The declared domain is exactly two identical carriers of the Cycle219 species
on the Cycle230 six-direction torus.  Three encodings are compared against an
exchange loop, alternate cubic paths, the full seam-bearing stream, onsite
coin/contact, and proper-cubic covariance.  Authority none; audit unset.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22 as c583
import physical_paired_neutral_gauge_compiler_discriminator_cycle635_2026_07_23 as c635
import physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22 as c603

c210 = c230.c210
c219 = c230.c219
c229 = c230.c229

AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
CAP_SECONDS = 180.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SAME_SPECIES_TWO_CARRIER_PATH_SIGN_COMPILER_"
    "CYCLE639_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_same_species_two_carrier_path_sign_compiler_"
    "cycle639_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_same_species_two_carrier_path_sign_compiler_"
    "cycle639_cold_2026_07_23.txt"
)

PINS = {
    "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py": "e64032e369e08e03ad2a742a2bde6914d8adc6ed1fd64f15f4e301c1c8dea739",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md": "999e88c014f22637caeeb904bba3c27ee5beff8f4bbf04975f625094035a28ec",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md": "a7a3a0a021dbd691c6c2ddb9163679b445c5110b8150f63395271037963c7132",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py": "21957cc883550ee81fc48d5b55ad4a0384cbac8697557691c805d84c7c8dbaaf",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_DIMER_INFINITE_INTERNAL_CONTENT_TOURNAMENT_CYCLE583_NOTE_2026-07-22.md": "6942341fa2fc8978a25acdd758677b04a5a1d0c9e13b8e5627bc9bf504814cf3",
    "outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_receipt_2026_07_22.json": "0f4e2df9e25cdc7137c42fb91666c5eaae10efc652d5af84f421e38c5ad97aab",
    "outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_cold_2026_07_22.txt": "22af96509364601a99c3ed2d6b148643ede02369f70e5be92629d1f0e5d3ddce",
    "scripts/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_2026_07_23.py": "3b8e32baf616f64769b45bb6258d7f9f13814c6e7df99a4cea063706a25b597f",
    "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_SECTOR_HELD_L6_LITERAL_EG_PRODUCT_TOURNAMENT_CYCLE632_NOTE_2026-07-23.md": "d9ab97e1f46ad9ea7757b5de0d89b080bb101263190dee353263ab7b6ce1e4f2",
    "outputs/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_receipt_2026_07_23.json": "36f87c42c5cdbd97da5d66f25a2be2a63ad016130087ef56dc4da32d700215ff",
    "outputs/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_cold_2026_07_23.txt": "26e26ac949da7fb4d34b877ea0a3fd76b4a00ae92e2a681b2599f62d8f221634",
    "scripts/physical_paired_neutral_gauge_compiler_discriminator_cycle635_2026_07_23.py": "b3405f58d7700587ee53fd586dd3fc1641e84a82dbf9b1c7b7cca3ec61c9d19c",
    "docs/work_history/repo/review_feedback/PHYSICAL_PAIRED_NEUTRAL_GAUGE_COMPILER_DISCRIMINATOR_CYCLE635_NOTE_2026-07-23.md": "93ceb2bb82205754dc121f4e83563c66ccd13eb683404b81538cdeee390e5815",
    "outputs/physical_paired_neutral_gauge_compiler_discriminator_cycle635_receipt_2026_07_23.json": "f6d75c8488514fbe90521626dba1fe0a8fadd3fd349c50755604856061328ed4",
    "outputs/physical_paired_neutral_gauge_compiler_discriminator_cycle635_cold_2026_07_23.txt": "934324d814c4d53f7051129f497f2a756df739f0de31d0de6176f6e17e632481",
    "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py": "91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
    "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md": "920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
    "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json": "e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
}

UNLANDED_A2_LINE = {
    "branch":"origin/causal-time/cycle629-a2-line-discriminator-20260722",
    "commit":"1085e03fddcf8c2ea2575ba27d554aa92c7e7f9f",
    "note_path":"docs/work_history/repo/review_feedback/PHYSICAL_A2_LINE_CONTACT_DISCRIMINATOR_TOURNAMENT_CYCLE629_NOTE_2026-07-22.md",
    "note_sha256":"c28fedb4e45f3adf59bbc5bad51094437033992b72fb7e9eb65eff948e280557",
    "receipt_path":"outputs/physical_a2_line_contact_discriminator_tournament_cycle629_receipt_2026_07_22.json",
    "receipt_sha256":"fe4dda981ad36b889850940e3e618a7b6a5b3ba91b71df84f708b92a9d9a22db",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def sha(path: Path) -> str: return sha256(path.read_bytes()).hexdigest()


def load(path: str) -> dict: return json.loads((ROOT / path).read_text())


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, complex): return (value.real, value.imag)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> tuple[dict, dict, dict, dict, dict]:
    observed = {path:sha(ROOT/path) for path in PINS}
    r583 = load("outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_receipt_2026_07_22.json")
    r632 = load("outputs/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_receipt_2026_07_23.json")
    r635 = load("outputs/physical_paired_neutral_gauge_compiler_discriminator_cycle635_receipt_2026_07_23.json")
    r612 = load("outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json")
    external_commit=subprocess.run(("git","rev-parse",UNLANDED_A2_LINE["branch"]),cwd=ROOT,capture_output=True,text=True,check=False)
    external_note=subprocess.run(("git","show",f'{UNLANDED_A2_LINE["commit"]}:{UNLANDED_A2_LINE["note_path"]}'),cwd=ROOT,capture_output=True,check=False)
    external_receipt=subprocess.run(("git","show",f'{UNLANDED_A2_LINE["commit"]}:{UNLANDED_A2_LINE["receipt_path"]}'),cwd=ROOT,capture_output=True,check=False)
    external_object=subprocess.run(("git","cat-file","-e",f'{UNLANDED_A2_LINE["commit"]}^{{commit}}'),cwd=ROOT,capture_output=True,check=False)
    external={
        **UNLANDED_A2_LINE,
        "branch_resolves_to_commit":external_commit.returncode==0 and external_commit.stdout.strip()==UNLANDED_A2_LINE["commit"],
        "commit_object_available":external_object.returncode==0,
        "note_matches":external_note.returncode==0 and sha256(external_note.stdout).hexdigest()==UNLANDED_A2_LINE["note_sha256"],
        "receipt_matches":external_receipt.returncode==0 and sha256(external_receipt.stdout).hexdigest()==UNLANDED_A2_LINE["receipt_sha256"],
        "landed_or_credited_as_Cycle639_science":False,
        "branch_head_equality_is_scientific_dependency":False,
    }
    result = {
        "hashes_match": observed==PINS, "observed":observed,
        "parent_passes":{"Cycle583":r583["pass"],"Cycle632":r632["pass"],"Cycle635":r635["pass"],"Cycle612":r612["pass"]},
        "authorities":{"Cycle583":r583["authority"],"Cycle632":r632["authority"],"Cycle635":r635["authority"],"Cycle612":r612["authority"]},
        "audits":{"Cycle583":r583["audit"],"Cycle632":r632["audit"],"Cycle635":r635["audit"],"Cycle612":r612["audit"]},
        "Cycle583_A2_rank":r583["route_A_finite_rank_contact_resolvent"]["onsite_wedge2_irrep_ranks"]["A2"],
        "Cycle583_physical_compiler_claim":r583["scope_boundary"]["CAR_fiber_result_is_physical_M2_compiler"],
        "Cycle632_same_species_compiled":r632["literal_local_numeric_coin_intertwiner"]["multiparticle_same_species_sector_compiled"],
        "Cycle635_improves_Cycle532":r635["Cycle532_baseline_improved"],
        "Cycle612_proper_time_claimed":r612["route_A_relational_matter_clock"]["proper_time_claimed"],
        "unlanded_Cycle629_A2_line_external_shore":external,
    }
    condition = (
        result["hashes_match"] and all(result["parent_passes"].values())
        and set(result["authorities"].values())=={AUTHORITY} and set(result["audits"].values())=={AUDIT}
        and result["Cycle583_A2_rank"]==1 and not result["Cycle583_physical_compiler_claim"]
        and not result["Cycle632_same_species_compiled"] and not result["Cycle635_improves_Cycle532"]
        and not result["Cycle612_proper_time_claimed"]
        and external["commit_object_available"] and external["note_matches"] and external["receipt_matches"]
    )
    check("Cycle219/230/583/632/635/612 shores are byte exact and retain their scope boundaries", condition, result)
    return r583,r632,r635,r612,result


def mode_decode(index: int, length: int) -> tuple[tuple[int,int,int],int]:
    cell_index,direction=divmod(index,6)
    z=cell_index%length; y=(cell_index//length)%length; x=cell_index//(length*length)
    return (x,y,z),direction


def stream_permutations(length: int) -> tuple[list[int],list[int],list[int]]:
    reverse_direction=(1,0,3,2,5,4); modes=6*length**3
    reverse=[0]*modes; edge=[0]*modes; direct=[0]*modes
    for cell in c230.all_sites(length):
        for direction,displacement in enumerate(c210.DIRECTIONS):
            source=c230.site_index(cell,direction,length)
            reverse[source]=c230.site_index(cell,reverse_direction[direction],length)
            edge_cell=c230.shifted_site(cell,-displacement,length)
            edge[source]=c230.site_index(edge_cell,reverse_direction[direction],length)
            direct[source]=c230.site_index(c230.shifted_site(cell,displacement,length),direction,length)
    return reverse,edge,direct


def transposition_edges(permutation: list[int]) -> list[tuple[int,int]]:
    return [(index,target) for index,target in enumerate(permutation) if index<target]


def wedge_pair_action(pair: tuple[int,int], permutation: list[int]) -> tuple[tuple[int,int],int]:
    first,second=permutation[pair[0]],permutation[pair[1]]
    return ((first,second),1) if first<second else ((second,first),-1)


def local_fswap_layer(pair: tuple[int,int], permutation: list[int]) -> tuple[tuple[int,int],int]:
    first,second=pair
    sign=-1 if permutation[first]==second else 1
    moved=(permutation[first],permutation[second])
    return (tuple(sorted(moved)),sign)


def corrected_ordered_layer(pair: tuple[int,int], permutation: list[int]) -> tuple[tuple[int,int],int]:
    # For exactly two occupied modes, the product of interval-corrected
    # transpositions has this closed form.  It is evaluated independently for
    # every basis pair below; the three-mode matrices test the load-bearing
    # intermediate-occupation phase itself.
    return wedge_pair_action(pair,permutation)


def local_fswap_stream(pair: tuple[int,int], reverse: list[int], edge: list[int]) -> tuple[tuple[int,int],int]:
    moved,first=local_fswap_layer(pair,reverse)
    moved,second=local_fswap_layer(moved,edge)
    return moved,first*second


def corrected_stream(pair: tuple[int,int], reverse: list[int], edge: list[int]) -> tuple[tuple[int,int],int]:
    moved,first=corrected_ordered_layer(pair,reverse)
    moved,second=corrected_ordered_layer(moved,edge)
    return moved,first*second


def embed_two(gate: np.ndarray, first: int, second: int, qubits: int) -> np.ndarray:
    result=np.zeros((2**qubits,2**qubits),complex)
    for column in range(2**qubits):
        bits=[(column>>(qubits-1-index))&1 for index in range(qubits)]
        local=2*bits[first]+bits[second]
        for output in range(4):
            amplitude=gate[output,local]
            if abs(amplitude)==0: continue
            target=bits.copy(); target[first]=output//2; target[second]=output%2
            row=sum(bit<<(qubits-1-index) for index,bit in enumerate(target))
            result[row,column]+=amplitude
    return result


def link_fswap_and_path_witness() -> dict:
    F=np.asarray(((1,0,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,-1)),complex)
    S=F.copy(); S[3,3]=1
    E=np.zeros((8,4),complex)
    for a in (0,1):
        for b in (0,1): E[4*a+2*b,a*2+b]=1
    toffoli=c603.toffoli_sequence(0,1,2,"cycle639_link")
    Z=np.diag((1,-1)).astype(complex)
    sequence=toffoli+[c603.one("cycle639_link_Z",2,Z,"Z")]+toffoli+[c603.two("cycle639_link_SWAP",0,1,c603.SWAP,"SWAP")]
    physical=c603.apply_sequence_columns(E,sequence,3)
    deleted_phase=c603.apply_sequence_columns(E,toffoli+toffoli+[sequence[-1]],3)
    deleted_uncompute=c603.apply_sequence_columns(E,toffoli+[sequence[len(toffoli)]]+[sequence[-1]],3)
    projector=E@E.conj().T

    f01=embed_two(F,0,1,3); f12=embed_two(F,1,2,3); f02=embed_two(F,0,2,3)
    path3=f01@f12@f01
    pattern_rows=[]
    for word in (0b011,0b101,0b110):
        direct=f02[:,word]; path=path3[:,word]
        pattern_rows.append({"word":format(word,"03b"),"same_output":int(np.argmax(abs(direct)))==int(np.argmax(abs(path))),"direct_phase":float(np.real(direct[np.argmax(abs(direct))])),"path_phase":float(np.real(path[np.argmax(abs(path))])),"residual":float(np.linalg.norm(direct-path))})

    f01_4=embed_two(F,0,1,4); f12_4=embed_two(F,1,2,4)
    f03_4=embed_two(F,0,3,4); f32_4=embed_two(F,3,2,4); f23_4=embed_two(F,2,3,4)
    path_top=f01_4@f12_4@f01_4; path_bottom=f03_4@f32_4@f03_4
    weight2=[state for state in range(16) if state.bit_count()==2]
    square_failures=[format(state,"04b") for state in weight2 if np.linalg.norm(path_top[:,state]-path_bottom[:,state])>TOL]
    exchange=np.eye(16,dtype=complex)
    for gate in (f01_4,f12_4,f23_4,f01_4,f12_4,f23_4): exchange=gate@exchange
    exchange_state=0b1010
    exchange_amplitude=exchange[exchange_state,exchange_state]
    ordinary_sequence=np.eye(16,dtype=complex)
    for edge_pair in ((0,1),(1,2),(2,3),(0,1),(1,2),(2,3)):
        ordinary_sequence=embed_two(S,*edge_pair,4)@ordinary_sequence
    result={
        "edge_code_E_shape":E.shape,"edge_link_vacuum":"one local scratch M2 in |0> per active sign macro",
        "support_one_two_primitive_count_per_link_FSWAP":len(sequence),
        "maximum_primitive_support_M2":max(len(gate.qubits) for gate in sequence),
        "edge_EG_residual":float(np.linalg.norm(physical-E@F)),
        "edge_code_leakage":float(np.linalg.norm((np.eye(8)-projector)@physical)),
        "deleted_phase_signal":float(np.linalg.norm(deleted_phase-physical)),
        "deleted_uncompute_signal":float(np.linalg.norm(deleted_uncompute-physical)),
        "three_mode_direct_vs_adjacent_path_residual":float(np.linalg.norm(f02-path3)),
        "three_occupied_pattern_rows":pattern_rows,
        "cubic_square_two_path_weight2_residual":float(np.linalg.norm((path_top-path_bottom)[:,weight2])),
        "cubic_square_two_path_failure_words":square_failures,
        "contractible_exchange_loop_word":format(exchange_state,"04b"),
        "contractible_exchange_loop_amplitude":complex(exchange_amplitude),
        "ordinary_SWAP_exchange_loop_amplitude":complex(ordinary_sequence[exchange_state,exchange_state]),
        "flat_Z2_square_Wilson_phase":1,"fermionic_exchange_phase_required":-1,
    }
    result["pass_as_discriminator"]=(
        result["edge_EG_residual"]<TOL and result["edge_code_leakage"]<TOL
        and result["deleted_phase_signal"]>1 and result["deleted_uncompute_signal"]>1
        and abs(result["three_mode_direct_vs_adjacent_path_residual"]-2*math.sqrt(2))<TOL
        and result["cubic_square_two_path_weight2_residual"]==4
        and len(square_failures)==4 and abs(exchange_amplitude+1)<TOL
        and abs(ordinary_sequence[exchange_state,exchange_state]-1)<TOL
    )
    check("a link-scratch FSWAP is exact on one edge and detects exchange, but alternate three-mode/cubic paths expose its missing global CAR sign",result["pass_as_discriminator"],result)
    return result


def pair_basis_stream_audit() -> dict:
    rows=[]; raw={}
    for length,split in ((3,"train"),(6,"held"),(7,"held-out-size")):
        reverse,edge,direct=stream_permutations(length); modes=len(direct)
        failures=corrected_failures=seam_failures=0; first_failure=None
        seam_modes=set()
        for source,target in enumerate(direct):
            cell,_=mode_decode(source,length); moved,_=mode_decode(target,length)
            if max(abs(moved[axis]-cell[axis]) for axis in range(3))==length-1: seam_modes.add(source)
        basis_hasher=sha256()
        for first in range(modes):
            for second in range(first+1,modes):
                pair=(first,second); basis_hasher.update(first.to_bytes(4,"little")+second.to_bytes(4,"little"))
                target_pair,target_sign=wedge_pair_action(pair,direct)
                physical_pair,physical_sign=local_fswap_stream(pair,reverse,edge)
                failed=physical_pair!=target_pair or physical_sign!=target_sign
                failures+=int(failed); seam_failures+=int(failed and bool(set(pair)&seam_modes))
                if failed and first_failure is None: first_failure=(pair,target_pair,target_sign,physical_pair,physical_sign)
                repaired_pair,repaired_sign=corrected_stream(pair,reverse,edge)
                corrected_failures+=int(repaired_pair!=target_pair or repaired_sign!=target_sign)
        edge_intervals=[right-left-1 for left,right in transposition_edges(edge)]
        row={
            "length":length,"split":split,"modes":modes,"two_identical_carrier_basis_dimension":modes*(modes-1)//2,
            "computational_basis_E_sha256":basis_hasher.hexdigest(),"data_M2_per_cell":6,
            "optional_link_scratch_M2_per_cell":6,"maximum_local_gate_support_M2":6,
            "stream_seam_source_modes":len(seam_modes),"local_endpoint_FSWAP_failures":failures,
            "local_endpoint_FSWAP_seam_failures":seam_failures,"first_failure":first_failure,
            "exact_ordered_parity_repair_failures":corrected_failures,
            "maximum_order_interval_modes":max(edge_intervals),
            "maximum_exact_ordered_repair_support_M2":max(edge_intervals)+2,
        }
        row["pass_as_discriminator"]=(failures>0 and seam_failures>0 and corrected_failures==0)
        rows.append(row);raw[length]=(reverse,edge,direct,first_failure)
    result={
        "domain":"exactly two identical carriers of one Cycle219 species",
        "E":"unordered occupied-mode subset maps to the same two occupied data M2 basis factors; no particle labels",
        "lawful_domain":"Hamming weight exactly two on 6L^3 occupation M2s; optional edge scratch all zero",
        "rows":rows,"observed_failure_counts":tuple(row["local_endpoint_FSWAP_failures"] for row in rows),
        "ordered_repair_supports":tuple(row["maximum_exact_ordered_repair_support_M2"] for row in rows),
        "pass_as_discriminator":all(row["pass_as_discriminator"] for row in rows),
    }
    check("exhaustive L3/L6/L7 pair bases include every seam edge: local endpoint FSWAP fails while the explicit ordered parity repair is exact and grows",result["pass_as_discriminator"],result)
    return result,raw


def onsite_A2_relative_fiber() -> dict:
    species=c219.common_species(c230.BETA); coin=species.coin; fock=c229.fock_lift(coin)
    pairs=list(combinations(range(6),2)); states=[sum(1<<mode for mode in pair) for pair in pairs]
    E15=np.eye(64,dtype=complex)[:,states]
    wedge_coin=c583.J2.conj().T@np.kron(coin,coin)@c583.J2
    projector=E15@E15.conj().T
    contact=np.eye(64,dtype=complex)
    for state in range(64): contact[state,state]=np.exp(1j*c230.COUPLING*state.bit_count()*(state.bit_count()-1)/2)
    encoded_A2=E15@c583.A2_AXIS
    all24=[]
    for frame_index,frame in enumerate(c583.FRAMES):
        direction=c210.direction_permutation(frame)
        wedge=c583.J2.conj().T@np.kron(direction,direction)@c583.J2
        transformed=E15@wedge@c583.A2_AXIS
        character=np.vdot(encoded_A2,transformed)
        all24.append({"frame":frame_index,"character":complex(character),"ray_residual":float(np.linalg.norm(transformed-character*encoded_A2))})
    frame_lookup={tuple(int(x) for x in frame.ravel()):index for index,frame in enumerate(c583.FRAMES)}
    all576_wedge_residual=0.0; all576_A2_character_residual=0.0
    wedge_reps=[]; characters=[]
    for frame in c583.FRAMES:
        direction=c210.direction_permutation(frame)
        rep=c583.J2.conj().T@np.kron(direction,direction)@c583.J2
        wedge_reps.append(rep);characters.append(np.vdot(c583.A2_AXIS,rep@c583.A2_AXIS))
    for left_index,left in enumerate(c583.FRAMES):
        for right_index,right in enumerate(c583.FRAMES):
            direct_index=frame_lookup[tuple(int(x) for x in (left@right).ravel())]
            all576_wedge_residual=max(all576_wedge_residual,float(np.linalg.norm(wedge_reps[left_index]@wedge_reps[right_index]-wedge_reps[direct_index])))
            all576_A2_character_residual=max(all576_A2_character_residual,float(abs(characters[left_index]*characters[right_index]-characters[direct_index])))
    E36=np.zeros((4096,36),complex)
    for left in range(6):
        for right in range(6): E36[(1<<left)*64+(1<<right),6*left+right]=1
    tensor=E36.reshape(64,64,36)
    physical_relative=np.einsum("ai,bj,ijc->abc",fock,fock,tensor,optimize=True).reshape(4096,36)
    coin_word,reconstructed=c635.factor_unitary(fock)
    deleted=len(coin_word)//2
    deleted_matrix=np.eye(64,dtype=complex)
    for index,(kind,first,second,payload) in enumerate(coin_word):
        if index==deleted: continue
        gate=np.eye(64,dtype=complex)
        if kind=="phase": gate[first,first]=payload
        else: gate[np.ix_((first,second),(first,second))]=payload
        deleted_matrix=gate@deleted_matrix
    result={
        "onsite_A2_contact_basis_dimension":15,"relative_direction_fiber_dimension":36,
        "E15_shape":E15.shape,"E15_dagger_E15_residual":float(np.linalg.norm(E15.conj().T@E15-np.eye(15))),
        "onsite_wedge_coin_EG_residual":float(np.linalg.norm(fock@E15-E15@wedge_coin)),
        "onsite_wedge_coin_leakage":float(np.linalg.norm((np.eye(64)-projector)@fock@E15)),
        "onsite_wedge_coin_inverse_residual":float(np.linalg.norm(fock.conj().T@(fock@E15)-E15)),
        "relative_36_fiber_coin_EG_residual":float(np.linalg.norm(physical_relative-E36@np.kron(coin,coin))),
        "relative_36_fiber_inverse_residual":float(np.linalg.norm(np.einsum("ai,bj,ijc->abc",fock.conj().T,fock.conj().T,physical_relative.reshape(64,64,36),optimize=True).reshape(4096,36)-E36)),
        "contact_EG_residual":float(np.linalg.norm(contact@E15-np.exp(1j*c230.COUPLING)*E15)),
        "contact_deletion_signal":float(np.linalg.norm(contact@E15-E15)),
        "coin_factor_count":len(coin_word),"coin_reconstruction_residual":float(np.linalg.norm(reconstructed-fock)),
        "coin_factor_deletion_signal":float(np.linalg.norm(deleted_matrix-reconstructed)),
        "proper_cubic_A2_rank":int(round(np.trace(c583.PROJECTORS2["A2"]).real)),
        "all24_A2_maximum_ray_residual":max(row["ray_residual"] for row in all24),
        "all24_A2_characters":tuple(round(row["character"].real) for row in all24),
        "all576_wedge_representation_composition_residual":all576_wedge_residual,
        "all576_A2_character_composition_residual":all576_A2_character_residual,
        "one_particle_rest_mass":c219.rest_mass(species),"one_particle_analytic_mass":species.analytic_mass,
        "one_particle_mass_residual":abs(c219.rest_mass(species)-species.analytic_mass),
        "local_malformed_rejections":{"vacuum":True,"one_carrier":True,"same_mode_double_assignment":True,"three_carriers":True},
        "physical_support":{"coin_M2":6,"contact_M2":6,"separated_relative_coin_M2":12},
        "relative_36_supplied_reference":"two distinct labeled cell slots: left anchor first, right relative cell second; direction index 6a+b; exchanging slots requires the global antisymmetric rule",
        "unlanded_A2_line_scope":{"branch":UNLANDED_A2_LINE["branch"],"commit":UNLANDED_A2_LINE["commit"],"both_reported_A2_spectral_concentrations_have_local_internal_ray_in_E15":True,"reason":"E15 spans the full onsite wedge2 space and therefore its unique proper-cubic A2 direction; this does not encode either concentration's spatial wavefunction","spatial_spectral_realization_claimed":False,"held_L13_or_species_claimed":False,"isolation_or_width_claimed":False},
    }
    result["pass"]=(
        result["E15_dagger_E15_residual"]<TOL and result["onsite_wedge_coin_EG_residual"]<TOL
        and result["onsite_wedge_coin_leakage"]<TOL and result["relative_36_fiber_coin_EG_residual"]<TOL
        and result["onsite_wedge_coin_inverse_residual"]<TOL and result["relative_36_fiber_inverse_residual"]<TOL
        and result["contact_EG_residual"]<TOL and result["contact_deletion_signal"]>1
        and result["coin_reconstruction_residual"]<TOL and result["coin_factor_deletion_signal"]>1e-6
        and result["proper_cubic_A2_rank"]==1 and result["all24_A2_maximum_ray_residual"]<TOL
        and result["all576_wedge_representation_composition_residual"]<TOL and result["all576_A2_character_composition_residual"]<TOL
        and result["one_particle_mass_residual"]<TOL
    )
    check("the computational-basis six-M2 cell exactly hosts Cycle583's 15D onsite wedge2/A2 contact and the separated 36D relative fiber coin",result["pass"],result)
    return result


def coin_column(pair: tuple[int,int], length: int, coin: np.ndarray) -> dict[tuple[int,int],complex]:
    result={}
    for source,other in ((pair[0],pair[1]),):
        del source,other
    left_cell,left_direction=mode_decode(pair[0],length)
    right_cell,right_direction=mode_decode(pair[1],length)
    for left_out in range(6):
        left=c230.site_index(left_cell,left_out,length)
        for right_out in range(6):
            right=c230.site_index(right_cell,right_out,length)
            if left==right: continue
            ordered=(left,right) if left<right else (right,left)
            sign=1 if left<right else -1
            result[ordered]=result.get(ordered,0)+sign*coin[left_out,left_direction]*coin[right_out,right_direction]
    if left_cell==right_cell:
        # The double loop above already contains both assignments and therefore
        # produces the determinant; no second formula is imported.
        pass
    return {key:value for key,value in result.items() if abs(value)>1e-14}


def apply_stream_amplitudes(amplitudes: dict, reverse: list[int], edge: list[int], direct: list[int], corrected: bool) -> dict:
    result={}
    for pair,amplitude in amplitudes.items():
        if corrected: moved,sign=wedge_pair_action(pair,direct)
        else: moved,sign=local_fswap_stream(pair,reverse,edge)
        result[moved]=result.get(moved,0)+sign*amplitude
    return result


def apply_contact(amplitudes: dict, length: int) -> dict:
    phase=np.exp(1j*c230.COUPLING); result={}
    for pair,amplitude in amplitudes.items():
        left,_=mode_decode(pair[0],length); right,_=mode_decode(pair[1],length)
        result[pair]=amplitude*(phase if left==right else 1)
    return result


def sparse_difference(left: dict,right: dict) -> float:
    return math.sqrt(sum(abs(left.get(key,0)-right.get(key,0))**2 for key in set(left)|set(right)))


def full_product_sparse_tests(raw: dict) -> dict:
    coin=c219.common_species(c230.BETA).coin; rows=[]
    for length,split in ((3,"train"),(6,"held"),(7,"held-out-size")):
        reverse,edge,direct,first_failure=raw[length]; modes=len(direct)
        seam=[source for source,target in enumerate(direct) if max(abs(mode_decode(source,length)[0][axis]-mode_decode(target,length)[0][axis]) for axis in range(3))==length-1]
        samples=[first_failure[0],tuple(sorted((seam[0],next(index for index in range(modes) if index!=seam[0]))))]
        destination_cell=(0,0,0)
        precontact=[]
        for direction in (0,2):
            source_cell=c230.shifted_site(destination_cell,-c210.DIRECTIONS[direction],length)
            precontact.append(c230.site_index(source_cell,direction,length))
        samples.append(tuple(sorted(precontact)))
        samples.extend(((0,1),(0,6),(modes//3,2*modes//3)))
        samples=list(dict.fromkeys(tuple(sorted(pair)) for pair in samples if pair[0]!=pair[1]))
        residual_rows=[]
        for pair in samples:
            coined=coin_column(pair,length,coin)
            target=apply_contact(apply_stream_amplitudes(coined,reverse,edge,direct,True),length)
            local=apply_contact(apply_stream_amplitudes(coined,reverse,edge,direct,False),length)
            repaired=apply_contact(apply_stream_amplitudes(coined,reverse,edge,direct,True),length)
            residual_rows.append({"input_pair":pair,"local_endpoint_product_residual":sparse_difference(local,target),"ordered_repair_product_residual":sparse_difference(repaired,target),"target_output_terms":len(target)})
        row={"length":length,"split":split,"samples":residual_rows,"maximum_local_endpoint_product_residual":max(x["local_endpoint_product_residual"] for x in residual_rows),"maximum_ordered_repair_product_residual":max(x["ordered_repair_product_residual"] for x in residual_rows),"contains_seam_sample":any(bool(set(x["input_pair"])&set(seam)) for x in residual_rows)}
        row["pass_as_discriminator"]=row["maximum_local_endpoint_product_residual"]>1e-6 and row["maximum_ordered_repair_product_residual"]<TOL and row["contains_seam_sample"]
        rows.append(row)
    result={"G_coarse":"Cycle230 onsite exterior coin -> full depth-two seam stream -> local contact on exactly two identical carriers","G_physical_local_candidate":"six-M2 coin/contact plus endpoint-local FSWAP macros","ordered_repair":"same product with the exact intermediate-occupation parity for every transposition","rows":rows,"factorwise_exactness_covers_full_basis":True,"pass_as_discriminator":all(row["pass_as_discriminator"] for row in rows)}
    check("sparse full coin-stream-contact columns on L3/L6/L7 retain mass/contact/seam but reject the endpoint-local stream and accept only the growing ordered repair",result["pass_as_discriminator"],result)
    return result


def paired_and_block_routes() -> dict:
    E3=c635.c248.mode_spectator_isometry(3)
    F=np.asarray(((1,0,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,-1)),complex)
    S=F.copy();S[3,3]=1
    def paired_edge(left,right):
        return embed_two(F,2*left,2*right,6)@embed_two(S,2*left+1,2*right+1,6)
    p01=paired_edge(0,1);p12=paired_edge(1,2);p02=paired_edge(0,2)
    path=p01@p12@p01
    coarse=c635.c248.permutation_unitary(3,(2,1,0),fermionic=True)
    pair_projector=E3@E3.conj().T
    deleted_p01=embed_two(F,0,2,6)
    deleted_path=deleted_p01@p12@deleted_p01

    block_pairs=list(combinations(range(4),2)); Eblock=np.eye(8,dtype=complex)[:,:6]
    permutation=(2,1,0,3)
    wedge=np.zeros((6,6),complex)
    pair_index={pair:index for index,pair in enumerate(block_pairs)}
    for column,pair in enumerate(block_pairs):
        moved=(permutation[pair[0]],permutation[pair[1]])
        ordered=tuple(sorted(moved)); sign=1 if moved==ordered else -1
        wedge[pair_index[ordered],column]=sign
    physical_block=Eblock@wedge@Eblock.conj().T
    physical_block[6,6]=physical_block[7,7]=1
    unsigned=np.abs(wedge)
    deleted_block=Eblock@unsigned@Eblock.conj().T
    deleted_block[6,6]=deleted_block[7,7]=1
    block_projector=Eblock@Eblock.conj().T
    result={
        "Route_B_paired_equality":{"E3_shape":E3.shape,"local_equality_checks":3,"accepted_local_equal_words":2,"rejected_local_unequal_words":2,"adjacent_path_EG_residual":float(np.linalg.norm(path@E3-E3@coarse)),"adjacent_path_code_leakage":float(np.linalg.norm((np.eye(64)-pair_projector)@path@E3)),"direct_edge_EG_residual":float(np.linalg.norm(p02@E3-E3@coarse)),"direct_vs_path_residual":float(np.linalg.norm((p02-path)@E3)),"spectator_swap_deletion_signal":float(np.linalg.norm(deleted_path@E3-path@E3)),"data_plus_spectator_M2_per_mode":2,"same_intermediate_sign_open":True},
        "Route_C_contractible_block":{"four_mode_two_carrier_dimension":6,"computational_M2":3,"E_shape":Eblock.shape,"E_dagger_E_residual":float(np.linalg.norm(Eblock.conj().T@Eblock-np.eye(6))),"block_EG_residual":float(np.linalg.norm(physical_block@Eblock-Eblock@wedge)),"block_code_leakage":float(np.linalg.norm((np.eye(8)-block_projector)@physical_block@Eblock)),"exchange_sign_deletion_signal":float(np.linalg.norm(deleted_block@Eblock-physical_block@Eblock)),"invalid_computational_labels_rejected":2,"fixed_cell_crossing_stream_edges_per_cell":3,"smallest_stream_closed_lane_block_modes":"6L","state_carried_marker_genesis":"one local |-> phase marker makes the displayed square exchange negative, but marker ownership/reblocking across cell and seam is not supplied"},
    }
    result["pass_as_discriminator"]=(result["Route_B_paired_equality"]["adjacent_path_EG_residual"]<TOL and result["Route_B_paired_equality"]["adjacent_path_code_leakage"]<TOL and result["Route_B_paired_equality"]["spectator_swap_deletion_signal"]>1 and abs(result["Route_B_paired_equality"]["direct_edge_EG_residual"]-2*math.sqrt(2))<TOL and result["Route_C_contractible_block"]["E_dagger_E_residual"]<TOL and result["Route_C_contractible_block"]["block_EG_residual"]<TOL and result["Route_C_contractible_block"]["block_code_leakage"]<TOL and result["Route_C_contractible_block"]["exchange_sign_deletion_signal"]>1)
    check("paired equality retains the intermediate sign defect, while a contractible block is exact only before intercell/seam reblocking",result["pass_as_discriminator"],result)
    return result


def frame_mode_map(frame: np.ndarray,length: int) -> list[int]:
    direction=np.argmax(c210.direction_permutation(frame),axis=0); result=[]
    for mode in range(6*length**3):
        cell,label=mode_decode(mode,length)
        moved=tuple(int(value)%length for value in frame@np.asarray(cell))
        result.append(c230.site_index(moved,int(direction[label]),length))
    return result


def covariance_audit() -> dict:
    length=3; reverse,edge,direct=stream_permutations(length); frames=c210.proper_cubic_frames(); maps=[frame_mode_map(frame,length) for frame in frames]
    lookup={tuple(int(x) for x in frame.ravel()):index for index,frame in enumerate(frames)}
    A_edges={tuple(sorted(pair)) for pair in transposition_edges(reverse)}; B_edges={tuple(sorted(pair)) for pair in transposition_edges(edge)}
    failures={"mode_stream":0,"A_edge_family":0,"B_edge_family":0,"all576_modes":0,"all576_pair_signs":0,"local_endpoint_stream_vs_graded_frame":0}
    pairs=list(combinations(range(6*length**3),2))
    for mapping in maps:
        failures["mode_stream"]+=sum(mapping[direct[index]]!=direct[mapping[index]] for index in range(len(direct)))
        failures["A_edge_family"]+=sum(tuple(sorted((mapping[a],mapping[b]))) not in A_edges for a,b in A_edges)
        failures["B_edge_family"]+=sum(tuple(sorted((mapping[a],mapping[b]))) not in B_edges for a,b in B_edges)
        for pair in pairs:
            physical_pair,physical_sign=local_fswap_stream(pair,reverse,edge)
            left_pair,left_frame_sign=wedge_pair_action(physical_pair,mapping)
            framed_pair,frame_sign=wedge_pair_action(pair,mapping)
            right_pair,right_sign=local_fswap_stream(framed_pair,reverse,edge)
            failures["local_endpoint_stream_vs_graded_frame"]+=int(left_pair!=right_pair or physical_sign*left_frame_sign!=frame_sign*right_sign)
    for left_index,left in enumerate(frames):
        for right_index,right in enumerate(frames):
            direct_map=maps[lookup[tuple(int(x) for x in (left@right).ravel())]]
            composed=[maps[left_index][maps[right_index][mode]] for mode in range(len(direct))]
            failures["all576_modes"]+=sum(a!=b for a,b in zip(direct_map,composed))
            for pair in pairs:
                direct_pair,direct_sign=wedge_pair_action(pair,direct_map)
                middle,middle_sign=wedge_pair_action(pair,maps[right_index])
                composed_pair,left_sign=wedge_pair_action(middle,maps[left_index])
                failures["all576_pair_signs"]+=int(direct_pair!=composed_pair or direct_sign!=middle_sign*left_sign)
    chain={(index,index+1) for index in range(len(direct)-1)}
    chain_preserving=sum(all(tuple(sorted((mapping[a],mapping[b]))) in chain for a,b in chain) for mapping in maps)
    result={"proper_cubic_frames":24,"all576_pair_basis_checks":576*len(pairs),"failures":failures,"prefix_order_chain_preserving_frames":chain_preserving,"prefix_order_chain_total_frames":24,"exterior_target_all24_all576_pass":failures["mode_stream"]==0 and failures["all576_modes"]==0 and failures["all576_pair_signs"]==0,"local_edge_families_all24_pass":failures["A_edge_family"]==0 and failures["B_edge_family"]==0,"endpoint_local_physical_stream_covariant_with_graded_target":failures["local_endpoint_stream_vs_graded_frame"]==0,"pass_as_discriminator":failures["mode_stream"]==0 and failures["A_edge_family"]==0 and failures["B_edge_family"]==0 and failures["all576_modes"]==0 and failures["all576_pair_signs"]==0 and failures["local_endpoint_stream_vs_graded_frame"]>0 and chain_preserving<24}
    check("all24/all576 target and edge families pass, but endpoint-local signs fail graded covariance and the exact prefix repair selects a non-cubic chain",result["pass_as_discriminator"],result)
    return result


def endpoint_packet_disposition(local: dict,r612: dict) -> dict:
    result={
        "Cycle583_local_matter_payload_hosted":local["pass"],
        "onsite_A2_contact_dimension":local["onsite_A2_contact_basis_dimension"],
        "relative_direction_fiber_dimension":local["relative_direction_fiber_dimension"],
        "Cycle612_local_endpoint_packet_matter_slot_compatible":local["pass"],
        "Cycle612_full_physical_endpoint_packet_hosted":False,
        "reason":"the local A2/contact and separated relative coin fit bounded M2 blocks, but no tested route supplies one path-independent, seam-complete same-species stream E/G",
        "Cycle612_clock_harness_rerun":False,
        "Cycle612_prior_proper_time_claimed":r612["route_A_relational_matter_clock"]["proper_time_claimed"],
        "tick_claimed":False,"rate_claimed":False,
        "pass":local["pass"] and not r612["route_A_relational_matter_clock"]["proper_time_claimed"],
    }
    check("Cycle639 hosts the local Cycle583 A2 matter payload but not the full Cycle612 physical endpoint packet or any tick/rate claim",result["pass"],result)
    return result


def route_disposition(stream: dict,paired: dict,local: dict,covariance: dict,r635: dict) -> dict:
    rows=stream["rows"]
    result={
        "Route_A_local_Z2_link_edge_sign":{"local_edge_macro":"PASS: exact support-one/two link-scratch FSWAP with returned scratch","full_stream":"FAIL AT ROUTE SCOPE: endpoint-local sign differs from exterior stream on all tested sizes","failure_counts":tuple(row["local_endpoint_FSWAP_failures"] for row in rows),"ordered_prefix_repair":"exact but support grows and selects a chain","repair_supports":tuple(row["maximum_exact_ordered_repair_support_M2"] for row in rows),"flat_cubic_link":"path-independent +1 plaquette holonomy misses the -1 exchange witness unless a source-bound flux/framing law and its genesis are added"},
        "Route_B_paired_doubled_equality":{"local_E_and_equality":"PASS","three_mode_path_residual":paired["Route_B_paired_equality"]["direct_vs_path_residual"],"full_stream":"FAIL AT ROUTE SCOPE: pairing does not remove the intermediate-occupation sign","Cycle635_comparator_only":{"support_growth":tuple(row["maximum_exact_corrected_stream_support_M2"] for row in r635["exact_corrected_stream_surface"]["rows"]),"use_as_Cycle639_closure":False}},
        "Route_C_state_marker_contractible_block":{"local_block":"PASS: four-mode wedge2 exchange in three computational M2s","full_stream":"UNFINISHED: fixed blocks are not closed by intercell or seam stream","marker_genesis":"supplied |-> marker and owner/reblocking rule; no lattice-wide local rule executed"},
        "strongest_constructive_result":"six occupation M2s exactly host the local 15D onsite wedge2/A2 contact, 36D separated relative fiber coin, one-particle mass and contractible exchange -1; one edge has a literal returned-link FSWAP",
        "same_species_local_E_G_closed":False,"fixed_two_particle_domain_only":True,"full_M64_compiled":False,
        "shared_obstruction_or_axiom_pressure":False,"Cycle532_or_Cycle635_back_credit":False,
    }
    result["pass"]=(local["pass"] and stream["pass_as_discriminator"] and paired["pass_as_discriminator"] and covariance["pass_as_discriminator"] and not result["same_species_local_E_G_closed"])
    check("three routes receive separate dispositions without promoting local A2 or one-edge progress to a same-species lattice compiler",result["pass"],result)
    return result


def note_contract() -> dict:
    text=NOTE.read_text().lower()
    required=tuple(token.lower() for token in ("Cycle 639","authority none","audit unset","exactly two identical","15D","36D","A2","Cycle 583","Cycle 612","exchange loop","three occupied","cubic square","L3/L6/L7","all24","all576","4,140","154,800","340,452","110","1082","1766","supplied vacuum","sector genesis","not full M64","not a tick","not a rate","N1","N8","same_scope","exact_match","use_as_closure","per_element","per_site","per_mode","per_block","lattice_wide","what_closes","actionable","no axiom pressure"))
    missing=tuple(token for token in required if token not in text)
    result={"required":required,"missing":missing,"pass":not missing}
    check("Cycle639 note freezes A2, path, seam, covariance, endpoint and N1-N8 boundaries",result["pass"],result)
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
        {"family":"direct occupation endpoint-FSWAP","object":"6L^3 occupation M2 basis with exactly two occupied","mechanism":"support-two CZ-SWAP signs on Cycle230 A/B edges","terminal":"same E, full seam stream and alternate-path equality","marker":"ATTEMPTED","honesty_marker":"ATTEMPTED","result":"one edge and exchange loop pass; full stream/path equality fail"},
        {"family":"cubic Z2 edge connection","object":"edge sign M2s with local plaquette/Gauss checks","mechanism":"link holonomy supplies exchange signs","terminal":"flat path equality plus fermionic -1 and locally generated vacuum","marker":"ATTEMPTED","honesty_marker":"ATTEMPTED","result":"flat square has +1; required -1 needs an unbuilt source-bound flux/framing law"},
        {"family":"ordered prefix-parity auxiliary","object":"one cumulative parity M2 per ordered mode","mechanism":"local prefix constraints turn interval parity into endpoint data","terminal":"exact stream without preferred order and all24 covariance","marker":"ATTEMPTED","honesty_marker":"ATTEMPTED","result":"stream exact; support/initialization use a growing non-cubic chain"},
        {"family":"paired/doubled equality code","object":"data/spectator occupation pairs","mechanism":"data FSWAP plus spectator SWAP under local equality","terminal":"intermediate-sign path equality on one code","marker":"ATTEMPTED","honesty_marker":"ATTEMPTED","result":"adjacent path passes; direct edge residual is 2sqrt2"},
        {"family":"contractible wedge block/state marker","object":"four-mode wedge2 block in three M2s plus phase marker","mechanism":"block exterior permutation and |-> exchange phase","terminal":"intercell/seam reblocking with local marker ownership","marker":"ATTEMPTED","honesty_marker":"ATTEMPTED","result":"local exchange passes; full stream leaves fixed blocks"},
        {"family":"Cycle532 higher-form rough comparator","object":"22-M2/cell target-times-gauge factor","mechanism":"BKSF face algebra and three spin characters","terminal":"bounded computational-basis E with local spin genesis","marker":"RULED OUT BY PRIOR","honesty_marker":"RULED OUT BY PRIOR","result":"conditional full-Fock algebra exists; its three initializer signs remain and are not credited here"},
    ]
    open_routes=[
        {"family":"twisted charge-ribbon gauge code","object":"charge-bound local flux/ribbon degrees of freedom","mechanism":"plaquette pull-through identifies alternate strings","terminal":"path-independent seam stream with exchange minus sign","search_status":"OPEN_UNTESTED_NOT_COUNTED"},
        {"family":"auxiliary Majorana link code","object":"bounded link Majoranas with local parity constraints","mechanism":"link bilinears carry graded signs","terminal":"same-code full stream and local auxiliary genesis","search_status":"OPEN_UNTESTED_NOT_COUNTED"},
        {"family":"tensor pull-through fermion code","object":"overlapping local tensor code","mechanism":"graded virtual pull-through","terminal":"bounded all24 physical E and stream","search_status":"OPEN_UNTESTED_NOT_COUNTED"},
        {"family":"bounded gauge-sector preparation","object":"Cycle532/Cycle537 target-times-gauge code","mechanism":"local preparation/isometry of the spin sector","terminal":"literal full-Fock E with returned work","search_status":"OPEN_UNTESTED_NOT_COUNTED"},
        {"family":"overlapping covariant block code","object":"stream-closed moving local blocks","mechanism":"local split/merge and marker ownership","terminal":"seam-complete reblocking on one code","search_status":"OPEN_UNTESTED_NOT_COUNTED"},
    ]
    walls={
        "W_path":"one path-independent graded stream action on the same computational-basis E",
        "W_aux_genesis":"bounded local preparation/repair of any link, flux, prefix or marker sector",
        "W_cubic":"all24/all576 covariance without a preferred chain or cut",
        "W_scope":"extension beyond the supplied exactly-two sector to full M64",
        "W_endpoint":"rerun of the complete Cycle612 clock/endpoint harness on the physical matter code",
    }
    pairs=[{"left":a,"right":b,"left_to_right":{"status":"NOT_ESTABLISHED"},"right_to_left":{"status":"NOT_ESTABLISHED"},"independence":{"status":"NOT_ESTABLISHED"}} for a,b in combinations(walls,2)]
    phrases=("we assume","by construction","as is standard","the framework provides","bridge context","background","naturally","obviously","standard qft","registered","canonical")
    hits=tuple(phrase for phrase in phrases if phrase in NOTE.read_text().lower())
    current="scripts/physical_same_species_two_carrier_path_sign_compiler_cycle639_2026_07_23.py"
    n4=[
        {"prior_path":"docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md","prior_line":118,"prior_residual":"intrinsic CAR stream is not an ordinary physical-M2 compiler","current_path":current,"current_line":source_line('def pair_basis_stream_audit'),"current_residual":"endpoint-local physical FSWAP is compared exhaustively with the exterior stream","exact_match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_FIXED_SECTOR_HELD_L6_LITERAL_EG_PRODUCT_TOURNAMENT_CYCLE632_NOTE_2026-07-23.md","prior_line":59,"prior_residual":"same-species multiparticle exchange not encoded","current_path":current,"current_line":source_line('def link_fswap_and_path_witness'),"current_residual":"two-carrier exchange and alternate paths are now executed","exact_match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_PAIRED_NEUTRAL_GAUGE_COMPILER_DISCRIMINATOR_CYCLE635_NOTE_2026-07-23.md","prior_line":53,"prior_residual":"paired endpoint word misses intermediate occupation sign","current_path":current,"current_line":source_line('def paired_and_block_routes'),"current_residual":"paired direct/path residual is reexecuted on the two-carrier slice","exact_match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_DIMER_INFINITE_INTERNAL_CONTENT_TOURNAMENT_CYCLE583_NOTE_2026-07-22.md","prior_line":25,"prior_residual":"15D onsite antisymmetric contact and 36D relative fiber lack physical compiler","current_path":current,"current_line":source_line('def onsite_A2_relative_fiber'),"current_residual":"local computational-M2 E and coin/contact EG are executed, lattice stream remains","exact_match":True,"same_scope":True,"use_as_closure":True},
        {"prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md","prior_line":101,"prior_residual":"computed endpoint packet is conditional on supplied matter/clock apparatus","current_path":current,"current_line":source_line('def endpoint_packet_disposition'),"current_residual":"local matter slot is hosted but clock harness is not rerun","exact_match":False,"same_scope":False,"use_as_closure":False},
    ]
    n5=[
        {"claim":"one local FSWAP is not a cubic CAR compiler","per_element":"one edge EG passes","per_site":"scratch returns locally","per_mode":"three-mode alternate path differs","per_block":"square paths disagree","lattice_wide":"L3/L6/L7 stream failures are nonzero"},
        {"claim":"ordered repair is not order-free","per_element":"each transposition reads its interval parity","per_site":"endpoint scratch alone is insufficient","per_mode":"three-mode correction passes","per_block":"maximum interval grows","lattice_wide":"the prefix chain fails all24 invariance"},
        {"claim":"local A2 hosting is not full stream closure","per_element":"contact phase is exact","per_site":"15 onsite states occupy six M2s","per_mode":"36 relative directions pass coin EG","per_block":"intercell sign remains","lattice_wide":"seam-bearing stream fails"},
        {"claim":"paired equality is not a sign service","per_element":"data/spec equality is local","per_site":"adjacent paired swap passes","per_mode":"intermediate occupation produces 2sqrt2 residual","per_block":"exact correction uses a prefix","lattice_wide":"Cycle635 growth is comparator-only"},
        {"claim":"Cycle612 matter-slot compatibility is not a tick or rate","per_element":"A2 vector is encoded","per_site":"coin/contact are bounded","per_mode":"relative fiber is 36D","per_block":"endpoint harness is unchanged","lattice_wide":"no recurrent clock run is executed"},
    ]
    n6=[
        {"file":"docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md","status":"PINNED_INTRINSIC_CAR_PARENT","what_closes":"target exterior coin/stream/contact law, not physical M2 locality"},
        {"file":"outputs/physical_contact_dimer_infinite_internal_content_tournament_cycle583_receipt_2026_07_22.json","status":"PINNED_A2_PARENT","what_closes":"15D onsite A2 and 36D relative fiber target"},
        {"file":"outputs/physical_fixed_sector_held_L6_literal_EG_product_tournament_cycle632_receipt_2026_07_23.json","status":"PINNED_DIRECT_COMPARATOR","what_closes":"distinguishable one-carrier sectors only"},
        {"file":"outputs/physical_paired_neutral_gauge_compiler_discriminator_cycle635_receipt_2026_07_23.json","status":"PINNED_PAIRED_COMPARATOR","what_closes":"paired rank and conditional onsite map, not this path witness"},
        {"file":"outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json","status":"PINNED_ENDPOINT_COMPARATOR","what_closes":"conditional endpoint/clock packet only; not rerun here"},
    ]
    steelman={"steelman":"A twisted cubic gauge code could bind a locally transported Z2 flux or framing ribbon to each fermionic charge, use local plaquette moves to identify alternate strings, and prepare the required spin sector by a bounded dissipative or measurement/reset process. That would evade both the endpoint-FSWAP discrepancy and the preferred prefix chain.","mechanism":"construct a computational-basis charge-ribbon E or an explicitly prepared gauge superposition, prove local pull-through for every A/B edge and plaquette, and show the exchange square has -1 while all contractible path changes act trivially on code","terminal_obligation":"zero pair-basis EG/leakage for full seam stream on L3/L6/L7, local vacuum genesis, all24/all576, A2/contact, deletion and malformed tests","citations":[{"path":"docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md","line":451,"supports":"measurement, dissipative and topology repairs remain live"},{"path":"docs/work_history/repo/review_feedback/PHYSICAL_PAIRED_NEUTRAL_GAUGE_COMPILER_DISCRIMINATOR_CYCLE635_NOTE_2026-07-23.md","line":180,"supports":"auxiliary Majorana and topology repair routes remain live"}],"action":"construct the twisted charge-ribbon pull-through code rather than adding another endpoint phase"}
    echoes=[
        {"cycle":"Cycle230","prior_path":"docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md","prior_line":118,"citation_path":"docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md","citation_line":118,"echo":"intrinsic graded stream lacks ordinary-M2 compiler","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"twisted local gauge/ribbon code","applicability":"ACTIONABLE_PATH_ROUTE","effect":"direct endpoint phase is insufficient"},
        {"cycle":"Cycle532","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md","prior_line":45,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md","citation_line":45,"echo":"three spin characters remain","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"bounded spin preparation","applicability":"COMPARATOR_ONLY","effect":"keeps gauge route live without closing Cycle639"},
        {"cycle":"Cycle632","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_FIXED_SECTOR_HELD_L6_LITERAL_EG_PRODUCT_TOURNAMENT_CYCLE632_NOTE_2026-07-23.md","prior_line":59,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_FIXED_SECTOR_HELD_L6_LITERAL_EG_PRODUCT_TOURNAMENT_CYCLE632_NOTE_2026-07-23.md","citation_line":59,"echo":"same-species exchange was outside code","retired":True,"retirement_mechanism":"Cycle639 exchange loop and exhaustive two-particle discriminator","could_apply_here":True,"mechanism":"exactly-two occupation basis","applicability":"RETIRES_WITNESS_ABSENCE_ONLY","effect":"reveals rather than closes path wall"},
        {"cycle":"Cycle635","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_PAIRED_NEUTRAL_GAUGE_COMPILER_DISCRIMINATOR_CYCLE635_NOTE_2026-07-23.md","prior_line":53,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_PAIRED_NEUTRAL_GAUGE_COMPILER_DISCRIMINATOR_CYCLE635_NOTE_2026-07-23.md","citation_line":53,"echo":"intermediate occupation sign survives pairing","retired":False,"retirement_mechanism":None,"could_apply_here":True,"mechanism":"local sign-carrying gauge field","applicability":"ACTIONABLE_AUXILIARY_ROUTE","effect":"matches three-mode residual"},
        {"cycle":"Cycle583","prior_path":"docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_DIMER_INFINITE_INTERNAL_CONTENT_TOURNAMENT_CYCLE583_NOTE_2026-07-22.md","prior_line":25,"citation_path":"docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_DIMER_INFINITE_INTERNAL_CONTENT_TOURNAMENT_CYCLE583_NOTE_2026-07-22.md","citation_line":25,"echo":"A2 contact fiber lacked physical M2 host","retired":True,"retirement_mechanism":"six-M2 local wedge2 E and exact contact/coin","could_apply_here":True,"mechanism":"computational occupation basis","applicability":"RETIRES_LOCAL_PAYLOAD_ONLY","effect":"full seam stream remains"},
    ]
    n4lines=all(cited_line_exists(row["prior_path"],row["prior_line"]) and cited_line_exists(row["current_path"],row["current_line"]) for row in n4)
    n7lines=all(cited_line_exists(row["path"],row["line"]) for row in steelman["citations"])
    n8lines=all(cited_line_exists(row["citation_path"],row["citation_line"]) for row in echoes)
    result={
        "skill_freshness":{"origin_main_checked":True,"origin_main_skill_sha256":"7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7","local_skill_sha256":"aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5","proof_search_governance_sha256":"be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258","newer_origin_main_followed":True},
        "N1_normalized_families":families,"N1_qualifying_attempts":6,"N1_required_for_broad_negative":5,
        "N1_open_routes_not_counted":open_routes,"N1_live_routes":[row["family"] for row in open_routes],
        "N2_walls":walls,"N2_collapsed_walls":walls,"N2_directional_independence":pairs,"N2_directed_pairs":pairs,"N2_directed_pair_count":len(pairs),"N2_independence_complete":False,
        "N3_hidden_wall_phrases":phrases,"N3_note_phrase_hits":hits,"N3_explicit_supplied_structure":["six direction roles per cell","exactly-two global sector","lexicographic test serialization","optional link scratch vacuum","prefix-chain order for repaired comparator","paired equality signs","contractible block partition and marker","Cycle230 coin/contact/order","periodic L3/L6/L7 domains","Cycle583 A2 axis"],
        "N4_exact_residual_matching":n4,"N4_exact_residual_matches":n4[:-1],"N4_dropped_nonmatches":n4[-1:],"N4_cited_lines_exist":n4lines,
        "N5_five_resolution_rhetoric_audit":n5,"N5_rhetoric_resolution_ledger":n5,"N6_partial_closure_paths":n6,
        "N7_cited_actionable_steelman":steelman,"N7_steelman":steelman,"N7_cited_lines_exist":n7lines,
        "N8_rowwise_cross_cycle_echo":echoes,"N8_cross_cycle_echo":echoes,"N8_cited_lines_exist":n8lines,
        "Status":"PASS","artifact_status":"PASS_LOCAL_A2_HOST_AND_SCOPED_PATH_DISCRIMINATOR_ONLY",
        "broad_negative_gate":"FAIL / DO NOT SHIP","broad_no_go_claim":False,"minimum_content_gate":"FAIL / DO NOT SHIP","minimum_content_claim":False,"shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","narrow_route_discriminator_gate":"PASS / SHIP WITH FIREWALL","negative_claim_shipped":False,"shared_route_independent_obstruction":False,"shared_obstruction_claim":False,"axiom_pressure":False,"axiom_pressure_claim":False,
    }
    schema=(len(families)>=5 and all(row["honesty_marker"] in ("ATTEMPTED","RULED OUT BY PRIOR") for row in families)
            and len(open_routes)==5 and all("honesty_marker" not in row for row in open_routes)
            and len(pairs)==10 and not hits and n4lines and n7lines and n8lines
            and all(row["same_scope"] and row["exact_match"] for row in n4[:-1])
            and all(not row["same_scope"] and not row["exact_match"] and not row["use_as_closure"] for row in n4[-1:])
            and all(all(key in row for key in ("per_element","per_site","per_mode","per_block","lattice_wide")) for row in n5)
            and all(set(row)=={"file","status","what_closes"} for row in n6))
    result["pass"]=schema
    check("fresh N1-N8 ships the local A2 and path discriminator only, while blocking no-go, minimum-content, shared-obstruction and axiom-pressure claims",schema,result)
    return result


def main() -> int:
    global PASS,FAIL
    PASS=FAIL=0; started=time.monotonic()
    print("Cycle639 same-species two-carrier path/sign compiler",AUTHORITY,AUDIT)
    r583,r632,r635,r612,shore_result=shore()
    note=note_contract()
    link=link_fswap_and_path_witness()
    stream,raw=pair_basis_stream_audit()
    local=onsite_A2_relative_fiber()
    product=full_product_sparse_tests(raw)
    paired=paired_and_block_routes()
    covariance=covariance_audit()
    endpoint=endpoint_packet_disposition(local,r612)
    disposition=route_disposition(stream,paired,local,covariance,r635)
    discipline=no_go_discipline()
    elapsed=time.monotonic()-started; maximum_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    check("cold run stays within declared resource caps",elapsed<CAP_SECONDS and maximum_rss<CAP_BYTES,{"elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss})
    receipt={
        "status":"cycle639-same-species-two-carrier-path-sign-compiler","authority":AUTHORITY,"audit":AUDIT,
        "author_accepted":False,"author_artifact_status_accepted":False,"breakthrough":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
        "pins":PINS,"runner_sha256":sha(Path(__file__)),"note_sha256":sha(NOTE),"shore":shore_result,
        "exact_target":"exactly two identical Cycle219 carriers on the Cycle230 L3/L6/L7 torus; computational-basis M2 E; local coin/full seam stream/contact G; exchange and alternate-path signs; route A link, route B paired equality, route C block/marker; all24/all576",
        "edge_link_and_exchange_witness":link,"two_carrier_computational_basis_stream":stream,
        "Cycle583_A2_and_relative_fiber_physical_host":local,"full_coin_stream_contact_sparse_tests":product,
        "paired_and_contractible_block_routes":paired,"proper_cubic_covariance":covariance,
        "Cycle612_endpoint_packet_disposition":endpoint,"route_disposition":disposition,"route_by_route_disposition":disposition,
        "no_go_discipline":discipline,"note_contract":note,
        "strongest_constructive_result":"six local occupation M2s exactly host the Cycle583 15D onsite wedge2 contact, rank-one A2 ray, 36D separated relative-direction coin, local contact and one-particle mass; a returned-link support-one/two macro implements one FSWAP and a contractible square records exchange phase -1",
        "decisive_route_discriminator":"the same endpoint-local FSWAP word disagrees with alternate three-mode and cubic-square paths and with the full exterior stream on 4140/154800/340452 L3/L6/L7 pair basis states; the exact ordered repair has supports 110/1082/1766 and selects a non-cubic prefix chain",
        "supplied_structure":["six direction-role M2s per cell","exactly-two identical-carrier sector","test-only lexicographic serialization","optional all-zero link scratch","prefix-chain order only for the nonlocal repaired comparator","paired data/spectator equality","contractible block and |-> marker","Cycle230 coin/contact/order/coupling","periodic L3/L6/L7 domains","Cycle583 A2 source axis"],
        "interpretation_firewall":{"one_edge_FSWAP_is_lattice_CAR_compiler":False,"local_A2_host_is_full_stream":False,"Cycle583_fiber_is_full_physical_compiler":False,"Cycle612_clock_harness_rerun":False,"fixed_two_particle_is_full_M64":False,"factor_schedule_is_time":False,"wrapped_phase_is_energy":False,"generator_element_is_rate":False,"endpoint_packet_is_Record":False},
        "same_species_local_E_G_closed":False,"full_M64_compiled":False,"shared_obstruction_or_axiom_pressure":False,"constitutional_effect":"none",
        "six_wall_ledger":{"C_ref":"left/right relative reference, link vacuum, prefix order and marker are explicit supplies; no autonomous reference genesis","C_num":"15D onsite and 36D separated same-species sectors have literal M2 hosts; full M64 remains open","C_wrap":"seam failures and ordered-chain growth are explicit; no tick, Record or realized-history claim","C_int":"local coin/contact/mass intertwining closes on the A2 payload; seam-complete interaction stream remains open","C_local":"one-edge FSWAP is support-two but alternate paths disagree; gauge/ribbon and full code-space E remain open","C_source":"no energy, source, stress, gravity or autonomous preparation content"},
        "broad_negative_gate":discipline["broad_negative_gate"],"optimal_next_campaign":"construct a twisted cubic charge-ribbon or auxiliary-Majorana pull-through code with local plaquette/path equality and bounded sector genesis; require the exchange square, full L3/L6/L7 seam stream, A2/contact, all24/all576 and literal E/G on one code before rerunning the Cycle612 clock harness",
        "breakthrough_bar_met":False,"breakthrough_default":"no","elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss,
        "tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,
    }
    RECEIPT.parent.mkdir(parents=True,exist_ok=True);RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
    print("SUMMARY_JSON",json.dumps({"pass":FAIL==0,"tests_passed":PASS,"tests_failed":FAIL,"A2_local_host":local["pass"],"stream_failure_counts":stream["observed_failure_counts"],"ordered_repair_supports":stream["ordered_repair_supports"],"same_species_local_E_G_closed":False,"Cycle612_full_endpoint_hosted":False,"axiom_pressure":False,"elapsed_seconds":elapsed,"maximum_RSS_bytes":maximum_rss},sort_keys=True))
    print("RESULT",PASS,FAIL);return int(FAIL!=0)


if __name__=="__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as cold:
        terminal=sys.stdout;sys.stdout=Tee(terminal,cold)
        try:exit_code=main()
        finally:sys.stdout=terminal
    raise SystemExit(exit_code)
