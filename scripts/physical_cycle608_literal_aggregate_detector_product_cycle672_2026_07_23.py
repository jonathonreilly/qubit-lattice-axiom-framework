#!/usr/bin/env python3
"""Cycle 672: execute Cycle608 literal aggregate detector factor product."""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "export and execute the literal aggregate detector factor product latent in immutable Cycle608 at the strongest tractable physical level, with explicit ordered factors, operand coordinates and M2 placement, and verify agreement with Cycle668's four-bit material/binder predicate rather than substituting factor counts or occurrence",
    "quantifiers_domain": "Cycle608 L3 train, L4 held-out-size and L6 held detector fixtures; Cycle662 train and held biased/nonproduct state labels; contact-on/off and all four material/binder inputs; all exported factors and their single deletions; all 24 proper-cubic frames and all 576 ordered products",
    "allowed_premises": "byte-pinned committed Cycle608 local factor/count blueprint and exact primitive decompositions; byte-pinned Cycle668 four-bit detector-predicate interface and disclosed Cycle608/Cycle612 replay-defect packet; immutable finite Cycle662 state labels; explicit finite M2 computational rails, compile-time charts, sparse reversible permutations and tensor/MPO contractions",
    "forbidden_weakenings": "calling aggregate counts or hashes an executed product; importing a target-equivalent detector output; using occurrence as material; host-side branch selection, runtime grade lookup or shell-predicate ROM; allocating or claiming an unexecuted dense 2^N matrix; hiding contact-off, deleted-factor, dirty-work, leakage, held-size, biased/nonproduct or covariance failures; repairing Cycle608/Cycle612; protected edits or axiom language",
    "required_edge_cases": "blank and dirty work; matter/binder zero and one; contact off and on; Cycle662 train, held biased and held nonproduct labels; L3/L4/L6; every single exported factor deletion; inverse and leakage; bounded support/depth/M2; all24/all576; exact supplied-structure and replay-defect inventory",
    "completion_witness": "a committed-shore-derived explicit ordered factor list with named reversible primitive, operand M2 coordinates and placement for every factor, an actually executed sparse circuit or MPO product on every declared fixture, exact product/inverse/leakage and per-factor deletion certificates, and equality of its clean-code output with Cycle668's four-bit detector predicate under every frozen quantifier",
    "outcomes_not_closure": "Cycle608 factor counts or aggregate SHA alone; replaying Cycle668's predicate without deriving an aggregate factor word; a truth table with no ordered product; a host-composed detector label; a dense-size estimate; agreement only on L3 or train states; a route-specific missing export promoted to shared obstruction, minimum content or axiom pressure",
}

from contextlib import contextmanager
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import importlib.util
import io
import json
import math
from pathlib import Path
import resource
import struct
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE608_LITERAL_AGGREGATE_DETECTOR_PRODUCT_CYCLE672_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / "outputs/physical_cycle608_literal_aggregate_detector_product_cycle672_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_cycle608_literal_aggregate_detector_product_cycle672_cold_2026_07_23.txt"
SHORE = "617f83f851885c2817f681a7eab9d0d28cae0fbe"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-10
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py":
        "ac2a337140d40624500a5f23fc771b9b716d4c4bd467eb27a1963d1db5eac875",
    "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md":
        "6e8e3aae72547e8a13b0ced4cea7230c7b594348073e45802c95e6a55329ee54",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json":
        "4ccba85490c08120aab645917fee87dbd58f21cf4fb17c5f60b3a4fab9dbca48",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_cold_2026_07_22.txt":
        "087e3ef7a5657a85432553f29e7050458a9c8552a3e59852e74ae86b5f9fc605",
    "scripts/physical_detector_formation_current_interval_kernel_cycle668_2026_07_23.py":
        "2e3402d01b1af725b51fcd8888c1c074f82bc6add07d34d2b020952308b1742b",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETECTOR_FORMATION_CURRENT_INTERVAL_KERNEL_CYCLE668_NOTE_2026-07-23.md":
        "9d991077c7533c98fc65114e6c3f516f523eeaf547722151ae5af8e0a1fc51fd",
    "outputs/physical_detector_formation_current_interval_kernel_cycle668_receipt_2026_07_23.json":
        "f7f733820abdbcf5520a7edf9de9aca067aa7998374e02f3af07204c2718f6a0",
    "outputs/physical_detector_formation_current_interval_kernel_cycle668_cold_2026_07_23.txt":
        "8218b3de130fb1b4d83683a6e4eb1b1fd10495e2ecdd267bdbe8b80f53f2edbd",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json":
        "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
}

Coord = tuple[int, int, int]
Basis = frozenset[Coord]
SparseState = dict[Basis, complex]


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
    target_line = next(i for i, line in enumerate(source, 1) if line.startswith("TARGET_CONTRACT ="))
    evidence_line = next(i for i, line in enumerate(source, 1) if line.startswith("def shore_controls"))
    fields = sorted(TARGET_CONTRACT)
    expected = ["allowed_premises", "completion_witness", "forbidden_weakenings",
                "outcomes_not_closure", "quantifiers_domain", "required_edge_cases", "target_statement"]
    return {"target_line": target_line, "first_evidence_load_line": evidence_line,
            "frozen_before_evidence": target_line < evidence_line,
            "target_contract_sha256": stable_digest(TARGET_CONTRACT),
            "proof_search_governance_exact_fields": fields,
            "pass": target_line < evidence_line and fields == expected}


def shore_controls() -> tuple[dict[str, object], dict[str, object]]:
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipts = {
        "Cycle608": json.loads(git_bytes("outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json")),
        "Cycle662": json.loads(git_bytes("outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json")),
        "Cycle668": json.loads(git_bytes("outputs/physical_detector_formation_current_interval_kernel_cycle668_receipt_2026_07_23.json")),
    }
    boundary = receipts["Cycle608"]["physical_promotion_boundary"]
    replay = receipts["Cycle668"]["unchanged_shore_runner_replay"]
    passed = (observed == PINS and all(receipts[name]["authority"] == "none" and receipts[name]["audit"] == "unset"
                                      for name in receipts)
              and all(boundary[key] is None for key in ("physical_encoder_E", "physical_update_G",
                  "physical_placement", "physical_primitive_product", "intertwiner_certificate", "full_code_leakage"))
              and not replay["frozen_unchanged_shore_active_replay_obligation_met"])
    return {"ref": SHORE, "pins": PINS, "observed": observed,
            "Cycle608_null_promotion_boundary": boundary,
            "Cycle668_disclosed_replay_packet": replay,
            "working_tree_bytes_used_as_scientific_premise": False,
            "author_status_accepted_as_audit": False, "pass": passed}, receipts


@contextmanager
def committed_cycle608_module():
    """Load Cycle608 and its imports from committed SHORE bytes, never dirty files."""
    archive = subprocess.run(("git", "archive", "--format=tar", SHORE, "scripts"), cwd=ROOT,
                             check=True, stdout=subprocess.PIPE).stdout
    with tempfile.TemporaryDirectory(prefix="cycle672-committed-") as temporary:
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
            bundle.extractall(temporary, filter="data")
        path = Path(temporary) / "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py"
        module_name = "cycle672_committed_cycle608"
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        assert spec.loader is not None
        spec.loader.exec_module(module)
        try:
            yield module
        finally:
            sys.modules.pop(module_name, None)


def complex_rows(matrix: np.ndarray) -> list[list[list[float]]]:
    return [[[float(value.real), float(value.imag)] for value in row] for row in matrix]


@dataclass(frozen=True)
class Factor:
    kind: str
    controls: tuple[Coord, ...]
    values: tuple[int, ...]
    targets: tuple[Coord, ...]
    matrix: tuple[tuple[complex, ...], ...] | None
    label: tuple[object, ...]

    def inverse(self) -> "Factor":
        matrix = None if self.matrix is None else tuple(tuple(value for value in row)
            for row in np.asarray(self.matrix, dtype=complex).conj().T)
        return Factor(self.kind, self.controls, self.values, self.targets, matrix,
                      ("inverse",)+self.label)

    def descriptor(self, ordinal: int | None = None) -> dict[str, object]:
        result = {"kind": self.kind, "controls": [list(c) for c in self.controls],
                  "values": list(self.values), "targets": [list(c) for c in self.targets],
                  "label": list(self.label), "support_M2": len(set(self.controls+self.targets))}
        if ordinal is not None: result["ordinal"] = ordinal
        if self.matrix is not None: result["matrix"] = complex_rows(np.asarray(self.matrix))
        return result


def factor_digest(factors: tuple[Factor, ...]) -> str:
    return stable_digest([factor.descriptor(i) for i, factor in enumerate(factors)])


def inverse_word(factors: tuple[Factor, ...]) -> tuple[Factor, ...]:
    return tuple(factor.inverse() for factor in reversed(factors))


def local_W_factors(c608, layout, cell_index: int) -> tuple[tuple[Factor, ...], str, dict[str, int]]:
    qsites = layout.q[cell_index]; branch = layout.branch[cell_index]
    roles = layout.roles[cell_index]
    role_sites = tuple(c608.c560.c533.coordinate_for_qubit(layout.code, layout.code.qubits+role) for role in roles)
    rows = c608.local_word_data(layout, cell_index, 2)
    factors: list[Factor] = []
    legacy = sha256(); census: dict[str, int] = {key: 0 for key in
        ("branch_initialization", "A_Givens", "SELECT_X", "SELECT_Z", "D_comparator_rows")}
    factors.append(Factor("X", (), (), (branch[0],), None, ("branch_initialization", cell_index)))
    census["branch_initialization"] += 1
    for word, _entries, schedule, _patterns, _subset, *_ in rows:
        values = c608.q_values(word)
        for target, matrix in schedule:
            matrix = np.asarray(matrix, dtype=complex)
            factors.append(Factor("GIVENS", qsites, values, (branch[0], branch[int(target)]),
                                  tuple(tuple(complex(v) for v in row) for row in matrix),
                                  ("A", cell_index, word, int(target))))
            census["A_Givens"] += 1
            legacy.update(repr(("A", cell_index, word, int(target), tuple(
                c608.c560.c533.complex_token(value) for value in matrix.reshape(-1)))).encode())
    for word, entries, _schedule, _patterns, _subset, *_ in rows:
        for branch_index, (term, _amplitude) in enumerate(entries):
            controls = qsites+(branch[branch_index],); values = c608.q_values(word)+(1,)
            representative = term.representative
            for kind, bits in (("X", representative.x), ("Z", representative.z)):
                for bit in range(bits.bit_length()):
                    if not ((bits >> bit) & 1): continue
                    target = c608.c560.c533.coordinate_for_qubit(layout.code, bit)
                    factors.append(Factor("MCX" if kind == "X" else "MCZ", controls, values,
                                          (target,), None,
                                          ("SELECT", cell_index, word, branch_index, kind, bit)))
                    census[f"SELECT_{kind}"] += 1
                    legacy.update(repr(("SELECT", cell_index, word, branch_index, kind, bit, target)).encode())
    for word, entries, _schedule, patterns, subset, *_ in rows:
        for branch_index, (_term, _amplitude) in enumerate(entries):
            selected_sites = tuple(role_sites[index] for index in subset)
            selected_values = tuple(patterns[branch_index][index] for index in subset)
            controls = qsites+selected_sites; values = c608.q_values(word)+selected_values
            factors.append(Factor("MCX", controls, values, (branch[branch_index],), None,
                                  ("D", cell_index, word, branch_index, tuple(subset))))
            census["D_comparator_rows"] += 1
            legacy.update(repr(("D", cell_index, word, branch_index, subset,
                                 selected_values, branch[branch_index])).encode())
    return tuple(factors), legacy.hexdigest(), census


def a2_matrix() -> np.ndarray:
    first = np.asarray((0.0, 0.0, -0.4999999999999997, -0.5000000000000003,
                        0.4999999999999999, 0.4999999999999999))
    second = np.asarray((0.5773502691896258, 0.5773502691896258,
                         -0.28867513459481287, -0.2886751345948128,
                         -0.2886751345948129, -0.28867513459481287))
    columns = [first, second]
    for unit in np.eye(6):
        work = unit.copy()
        for column in columns: work -= np.dot(column, work)*column
        if np.linalg.norm(work) > 1e-11: columns.append(work/np.linalg.norm(work))
    matrix = np.column_stack(columns)
    if np.linalg.det(matrix) < 0: matrix[:, -1] *= -1
    return matrix


def a2_predicate_factors(c608, layout, origin: int) -> tuple[tuple[Factor, ...], dict[str, object]]:
    work = a2_matrix().copy(); rotations = []; digest = sha256()
    for column in range(5):
        for lower in range(5, column, -1):
            top = lower-1; a, b = float(work[top,column]), float(work[lower,column])
            if abs(b) < 1e-15: continue
            radius = math.hypot(a,b); cosine, sine = a/radius, b/radius
            left, right = work[top,column:].copy(), work[lower,column:].copy()
            work[top,column:] = cosine*left+sine*right
            work[lower,column:] = -sine*left+cosine*right
            matrix = np.asarray(((cosine,sine),(-sine,cosine)),dtype=complex)
            rotations.append((top,matrix)); digest.update(struct.pack("<Idd",top,cosine,sine))
    digest.update(np.diag(work).copy().tobytes())
    qsites = layout.q[origin]; forward = tuple(Factor("GIVENS",(),(),(qsites[top],qsites[top+1]),
        tuple(tuple(complex(v) for v in row) for row in matrix),("A2_mesh",index,int(top)))
        for index,(top,matrix) in enumerate(rotations))
    predicate = Factor("MCX",qsites,(1,1,0,0,0,0),(layout.pointer,),None,("A2_predicate",))
    factors = forward+(predicate,)+inverse_word(forward)
    return factors, {"mesh_digest": digest.hexdigest(), "mesh_residual": float(np.linalg.norm(work-np.diag(np.diag(work)))),
                     "rotations": len(rotations), "diagonal": [float(v) for v in np.diag(work)]}


def controls_match(bits: Basis, factor: Factor) -> bool:
    return all(int(coord in bits) == value for coord, value in zip(factor.controls, factor.values))


def apply_factor(state: SparseState, factor: Factor) -> SparseState:
    result: SparseState = {}
    for bits, amplitude in state.items():
        if not controls_match(bits, factor):
            result[bits] = result.get(bits,0j)+amplitude; continue
        if factor.kind in ("X","MCX"):
            target = factor.targets[0]
            updated = frozenset(set(bits)^{target})
            result[updated] = result.get(updated,0j)+amplitude
        elif factor.kind == "MCZ":
            phase = -1 if factor.targets[0] in bits else 1
            result[bits] = result.get(bits,0j)+phase*amplitude
        elif factor.kind == "GIVENS":
            first, second = factor.targets; left, right = first in bits, second in bits
            if left == right:
                result[bits] = result.get(bits,0j)+amplitude
            else:
                matrix = np.asarray(factor.matrix,dtype=complex)
                column = 0 if left else 1
                for row in (0,1):
                    target_bits = set(bits); target_bits.discard(first); target_bits.discard(second)
                    target_bits.add(first if row == 0 else second)
                    target_bits_frozen = frozenset(target_bits)
                    result[target_bits_frozen] = result.get(target_bits_frozen,0j)+matrix[row,column]*amplitude
        else: raise ValueError(f"unknown factor {factor.kind}")
    return {bits: amplitude for bits,amplitude in result.items() if abs(amplitude)>2e-15}


def apply_word(state: SparseState, factors: tuple[Factor,...], skip: int | None = None) -> SparseState:
    for ordinal, factor in enumerate(factors):
        if ordinal != skip: state = apply_factor(state,factor)
    return state


def state_distance(first: SparseState, second: SparseState) -> float:
    return math.sqrt(sum(abs(first.get(key,0)-second.get(key,0))**2 for key in set(first)|set(second)))


def state_norm(state: SparseState) -> float:
    return float(sum(abs(amplitude)**2 for amplitude in state.values()))


def q_basis(layout, origin: int, word: int, extras: tuple[Coord,...]=()) -> SparseState:
    bits = set(extras)
    for direction,coord in enumerate(layout.q[origin]):
        if (word>>direction)&1: bits.add(coord)
    return {frozenset(bits):1+0j}


def a2_state(c608, layout, origin: int, extras: tuple[Coord,...]=()) -> SparseState:
    result: SparseState = {}
    for word, amplitude in c608.a2_word_amplitudes().items():
        if abs(amplitude)<=1e-14: continue
        bits = next(iter(q_basis(layout,origin,word,extras)))
        result[bits] = complex(amplitude)
    norm = math.sqrt(state_norm(result))
    return {bits:amplitude/norm for bits,amplitude in result.items()}


def expected_toggle(state: SparseState, coordinate: Coord) -> SparseState:
    return {frozenset(set(bits)^{coordinate}):amplitude for bits,amplitude in state.items()}


def find_interface_coordinates(layout, factors: tuple[Factor,...], count: int = 2,
                               additionally_used: tuple[Coord,...] = ()) -> tuple[Coord,...]:
    used = {coord for factor in factors for coord in factor.controls+factor.targets}
    used.update(additionally_used)
    pointer = layout.pointer
    candidates = []
    for radius in range(1,layout.modulus):
        for offset in product(range(-radius,radius+1),repeat=3):
            if sum(abs(value) for value in offset)!=radius: continue
            coord = tuple((pointer[axis]+offset[axis])%layout.modulus for axis in range(3))
            if coord not in used and coord not in candidates: candidates.append(coord)
            if len(candidates)==count: return tuple(candidates)
    raise ValueError("no interface coordinates")


def tensor_profile(state: SparseState, coordinates: tuple[Coord,...],
                   profile_row: dict[str,object]) -> SparseState:
    """Tensor an explicit coherent spectator profile from a pinned Cycle662 row."""
    result: SparseState = {}
    branches = profile_row["branches"]
    for bits, amplitude in state.items():
        for branch in branches:
            pattern = tuple(int(value) for value in branch["pattern"])
            if len(pattern) > len(coordinates):
                raise ValueError("insufficient spectator coordinates")
            augmented = set(bits)
            augmented.update(coord for bit,coord in zip(pattern,coordinates) if bit)
            result[frozenset(augmented)] = result.get(frozenset(augmented),0j) + (
                amplitude*math.sqrt(float(branch["propensity"])))
    norm = math.sqrt(state_norm(result))
    return {bits: amplitude/norm for bits,amplitude in result.items()}


def table_magnitude_controls(c608, layout, origin: int, W: tuple[Factor,...]) -> dict[str,object]:
    maximum_magnitude_residual = maximum_inverse = maximum_branch_leakage = 0.0; rows=[]
    branch_sites = set(layout.branch[origin]); qsites = set(layout.q[origin])
    for word,entries,*_ in c608.local_word_data(layout,origin,2):
        source = q_basis(layout,origin,word); encoded = apply_word(source,W)
        maximum_branch_leakage = max(maximum_branch_leakage,sum(abs(a)**2 for bits,a in encoded.items() if bits&branch_sites))
        observed = sorted(abs(amplitude) for amplitude in encoded.values())
        expected = sorted(abs(complex(amplitude)) for _term,amplitude in entries)
        maximum_magnitude_residual = max(maximum_magnitude_residual,max(abs(a-b) for a,b in zip(observed,expected)))
        maximum_inverse = max(maximum_inverse,state_distance(apply_word(encoded,inverse_word(W)),source))
        rows.append({"q_word":word,"entries":len(entries),"encoded_sparse_terms":len(encoded),
                     "q_register_preserved":all({coord for coord in bits if coord in qsites}==
                     {coord for coord in next(iter(source)) if coord in qsites} for bits in encoded)})
    return {"rows":rows,"row_count":len(rows),"maximum_table_magnitude_residual":maximum_magnitude_residual,
            "maximum_W_inverse_residual":maximum_inverse,"maximum_terminal_branch_leakage_probability":maximum_branch_leakage,
            "pass":max(maximum_magnitude_residual,maximum_inverse,maximum_branch_leakage)<TOL}


def factor_local_deletion_rows(factors: tuple[Factor,...]) -> tuple[list[dict[str,object]],float]:
    rows=[]; minimum=math.inf
    for ordinal,factor in enumerate(factors):
        if factor.kind in ("X","MCX"): signal=math.sqrt(2.0)
        elif factor.kind=="MCZ": signal=2.0
        else:
            signal=float(np.linalg.svd(np.asarray(factor.matrix)-np.eye(2),compute_uv=False)[0])
        minimum=min(minimum,signal)
        rows.append({"ordinal":ordinal,"kind":factor.kind,"label":list(factor.label),
                     "deletion_signal":signal,
                     "global_witness":"apply inverse prefix to the factor-local matching-control witness; unitary suffix preserves this norm"})
    return rows,minimum


def rotate_coord(c608, coord: Coord, frame: np.ndarray, modulus: int) -> Coord:
    return c608.c560.c533.c527.rotate_coord(coord,frame,modulus)


def rotate_factor(c608, factor: Factor, frame: np.ndarray, modulus: int) -> Factor:
    return Factor(factor.kind,tuple(rotate_coord(c608,c,frame,modulus) for c in factor.controls),factor.values,
                  tuple(rotate_coord(c608,c,frame,modulus) for c in factor.targets),factor.matrix,factor.label)


def covariance_controls(c608, layout, factors: tuple[Factor,...], probe: SparseState) -> dict[str,object]:
    frames=c608.c560.c532.c235.proper_cubic_frames(); frame_keys={tuple(frame.reshape(-1)) for frame in frames}
    base=apply_word(probe,factors); equivariance=group_failures=distance_failures=0; comparisons=0
    pair_distances={(factor_index,left,right):layout.distance(left,right) for factor_index,factor in enumerate(factors)
                    for left,right in zip(factor.targets[:-1],factor.targets[1:])}
    for frame in frames:
        rotated_word=tuple(rotate_factor(c608,factor,frame,layout.modulus) for factor in factors)
        rotated_probe={frozenset(rotate_coord(c608,c,frame,layout.modulus) for c in bits):amp for bits,amp in probe.items()}
        rotated_base={frozenset(rotate_coord(c608,c,frame,layout.modulus) for c in bits):amp for bits,amp in base.items()}
        equivariance+=state_distance(apply_word(rotated_probe,rotated_word),rotated_base)>TOL; comparisons+=1
        for key,distance in pair_distances.items():
            _,left,right=key
            distance_failures+=layout.distance(rotate_coord(c608,left,frame,layout.modulus),
                                               rotate_coord(c608,right,frame,layout.modulus))!=distance
    for first in frames:
        for second in frames:
            group_failures+=tuple((first@second).reshape(-1)) not in frame_keys
            for coordinate in {coord for factor in factors[:12] for coord in factor.controls+factor.targets}:
                direct=rotate_coord(c608,coordinate,first@second,layout.modulus)
                composed=rotate_coord(c608,rotate_coord(c608,coordinate,second,layout.modulus),first,layout.modulus)
                group_failures+=direct!=composed
    return {"proper_cubic_frames":len(frames),"ordered_frame_products":len(frames)**2,
            "executed_state_equivariance_comparisons":comparisons,"executed_state_equivariance_failures":equivariance,
            "pair_distance_transport_failures":distance_failures,"group_coordinate_failures":group_failures,
            "compile_time_transported_factor_family":True,"same_unprogrammed_device_covariance_claimed":False,
            "runtime_frame_selector":False,"pass":len(frames)==24 and not (equivariance or distance_failures or group_failures)}


def execute_size(c608, length: int, profile_rows: tuple[dict[str,object],...],
                 pinned_row: dict[str,object]) -> dict[str,object]:
    layout=c608.build_layout(length); origin=layout.cells.index((0,0,0))
    W,legacy_digest,census=local_W_factors(c608,layout,origin)
    predicate,predicate_meta=a2_predicate_factors(c608,layout,origin)
    detector=W+predicate+inverse_word(W)
    binder_coord=layout.path[origin]
    free_coordinates=find_interface_coordinates(
        layout,detector,count=5,
        additionally_used=(binder_coord,)+tuple(layout.work[origin])+tuple(layout.read_work))
    matter_coord,opportunity_coord=free_coordinates[:2]
    spectator_coordinates=free_coordinates[2:]
    conjunction=Factor("MCX",(layout.pointer,binder_coord),(1,1),(opportunity_coord,),None,("binder_contact_Toffoli",))
    composite=detector+(conjunction,)+inverse_word(detector)
    table=table_magnitude_controls(c608,layout,origin,W)
    comparisons=[]; maximum_compute=maximum_composite=maximum_norm=maximum_encoding=0.0
    for profile_row in profile_rows:
        label=str(profile_row["state"])
        for matter,binder in product((0,1),repeat=2):
            extras=tuple(coord for bit,coord in ((matter,matter_coord),(binder,binder_coord)) if bit)
            raw_label=a2_state(c608,layout,origin,extras) if matter else q_basis(layout,origin,0,extras)
            raw_label=tensor_profile(raw_label,spectator_coordinates,profile_row)
            # Cycle608's literal D = W^dag P W acts on the declared role-table
            # image E(label)=W^dag(label tensor blank).  This is not a physical
            # matter-to-q encoder; the independent matter bit below is a pinned
            # interface witness showing exactly that retained limitation.
            source=apply_word(raw_label,inverse_word(W))
            encoding_residual=state_distance(apply_word(source,W),raw_label)
            computed=apply_word(source,detector)
            expected_compute=expected_toggle(source,layout.pointer) if matter else source
            output=apply_word(source,composite)
            expected=expected_toggle(source,opportunity_coord) if matter and binder else source
            compute_residual=state_distance(computed,expected_compute); composite_residual=state_distance(output,expected)
            maximum_compute=max(maximum_compute,compute_residual); maximum_composite=max(maximum_composite,composite_residual)
            maximum_norm=max(maximum_norm,abs(state_norm(output)-1.0))
            maximum_encoding=max(maximum_encoding,encoding_residual)
            comparisons.append({"Cycle662_state_label":label,"Cycle662_split":profile_row["split"],
                                "spectator_pattern_bits":len(profile_row["branches"][0]["pattern"]),
                                "spectator_profile_terms":len(profile_row["branches"]),
                                "logical_material_fixture":matter,"independent_matter_interface_bit":matter,
                                "supplied_q_label":"A2" if matter else "vacuum","contact_binder":binder,
                                "contact":"on" if binder else "off","compute_residual":compute_residual,
                                "encoding_inverse_residual":encoding_residual,
                                "Cycle668_four_bit_residual":composite_residual,"output_sparse_terms":len(output)})
    clean_encoded=apply_word(a2_state(c608,layout,origin,(matter_coord,)),inverse_word(W))
    dirty=expected_toggle(clean_encoded,layout.branch[origin][0])
    dirty_output=apply_word(dirty,composite)
    clean_expected=expected_toggle(clean_encoded,opportunity_coord)
    dirty_clean_overlap=abs(sum(np.conj(dirty_output.get(bits,0))*amp for bits,amp in clean_expected.items()))
    raw_unencoded=a2_state(c608,layout,origin,(matter_coord,))
    raw_unencoded_residual=state_distance(apply_word(raw_unencoded,detector),
                                          expected_toggle(raw_unencoded,layout.pointer))
    q0_matter1_raw=q_basis(layout,origin,0,(matter_coord,binder_coord))
    q0_matter1=apply_word(q0_matter1_raw,inverse_word(W))
    q0_matter1_output=apply_word(q0_matter1,composite)
    q0_matter1_residual=state_distance(q0_matter1_output,q0_matter1)
    a2_matter0_raw=a2_state(c608,layout,origin,(binder_coord,))
    a2_matter0=apply_word(a2_matter0_raw,inverse_word(W))
    a2_matter0_output=apply_word(a2_matter0,composite)
    a2_matter0_q_driven_residual=state_distance(a2_matter0_output,
                                                expected_toggle(a2_matter0,opportunity_coord))
    deletion_rows,minimum_delete=factor_local_deletion_rows(detector)
    central=next(i for i,factor in enumerate(detector) if factor.label==("A2_predicate",))
    source_on=apply_word(a2_state(c608,layout,origin,(matter_coord,binder_coord)),inverse_word(W))
    deleted_predicate=apply_word(apply_word(source_on,detector,skip=central),(conjunction,)+inverse_word(detector))
    expected_on=expected_toggle(source_on,opportunity_coord)
    global_predicate_delete=state_distance(deleted_predicate,expected_on)
    used={coord for factor in detector for coord in factor.controls+factor.targets}
    used.update(layout.work[origin]);used.update(layout.read_work)
    maximum_support=max(len(set(f.controls+f.targets)) for f in detector)
    pinned_local=pinned_row["local_factor_count_blueprint"]
    export={"W_forward_factors":[factor.descriptor(i) for i,factor in enumerate(W)],
            "predicate_factors":[factor.descriptor(i) for i,factor in enumerate(predicate)],
            "aggregate_chronological_order":"W_forward ; A2_mesh ; equality-MCX(pointer) ; inverse(A2_mesh) ; inverse(W_forward)",
            "algebraic_operator_order":"W_forward^dagger P_A2 W_forward; rightmost W_forward acts first",
            "aggregate_detector_macro_factors":len(detector),"aggregate_detector_factor_sha256":factor_digest(detector),
            "legacy_W_factor_word_sha256":legacy_digest,"pinned_legacy_W_factor_word_sha256":pinned_local["materialized_factor_word_sha256"],
            "legacy_digest_matches":legacy_digest==pinned_local["materialized_factor_word_sha256"],
            "census":census,"pinned_census":pinned_local["origin_local_factor_census_one_direction"],
            "inverse_rule":"reverse order and conjugate-transpose every Givens; X/MCX/MCZ are self-inverse"}
    covariance=covariance_controls(c608,layout,composite,source_on)
    placement={"fine_modulus":layout.modulus,"explicit_operand_coordinates":True,
               "placed_M2_sites":len(used|set(free_coordinates)|{binder_coord}),
               "independent_matter_interface_coordinate":list(matter_coord),
               "independent_matter_bit_is_detector_control":False,
               "binder_contact_coordinate":list(binder_coord),
               "detector_pointer_coordinate":list(layout.pointer),"opportunity_coordinate":list(opportunity_coord),
               "Cycle662_spectator_coordinates":[list(c) for c in spectator_coordinates],
               "q_coordinates":[list(c) for c in layout.q[origin]],"branch_coordinates":[list(c) for c in layout.branch[origin]],
               "conjunction_work_coordinates":[list(c) for c in layout.work[origin]+layout.read_work],
               "maximum_macro_support_M2":maximum_support,
               "maximum_pair_route_edges":pinned_local["counts_candidate_Wdagger_predicate_W_word"]["maximum_pair_route_edges"],
               "installed_one_two_M2_factor_count":pinned_local["counts_candidate_Wdagger_predicate_W_word"]["elementary_total"],
               "installed_factor_count_called_rate_or_time":False,
               "primitive_lowering":"Cycle608 exact negative-control shells, Toffoli 9 one/6 two M2 word, controlled-Givens seven two-M2 core, and route-return SWAP installation",
               "dense_full_Hilbert_matrix_allocated":False}
    return {"length":length,"split":pinned_row["split"],"factor_export":export,"predicate_meta":predicate_meta,
            "table_and_inverse":table,"fixture_comparisons":comparisons,"fixture_comparison_count":len(comparisons),
            "maximum_detector_compute_residual":maximum_compute,"maximum_Cycle668_four_bit_residual":maximum_composite,
            "maximum_encoding_inverse_residual":maximum_encoding,"maximum_norm_residual":maximum_norm,
            "dirty_to_clean_code_overlap":dirty_clean_overlap,
            "lawful_domain_controls":{"declared_code":"E(label)=W_forward^dagger(label tensor blank role-table auxiliaries)",
                "raw_unencoded_A2_expected_toggle_residual":raw_unencoded_residual,
                "same_q_vacuum_different_independent_matter_bit_identity_residual":q0_matter1_residual,
                "same_independent_matter_zero_different_q_A2_q_driven_residual":a2_matter0_q_driven_residual,
                "detector_follows_supplied_q_not_independent_matter":True,
                "raw_unencoded_state_is_outside_declared_code":True,
                "pass":raw_unencoded_residual>1e-3 and max(q0_matter1_residual,a2_matter0_q_driven_residual)<TOL},
            "per_factor_deletions":deletion_rows,"per_factor_deletion_count":len(deletion_rows),
            "minimum_per_factor_deletion_signal":minimum_delete,"deleted_predicate_full_fixture_residual":global_predicate_delete,
            "placement_and_support":placement,"covariance":covariance,
            "pass":(export["legacy_digest_matches"] and census==export["pinned_census"] and table["pass"]
                    and max(maximum_compute,maximum_composite,maximum_encoding,maximum_norm,dirty_clean_overlap)<TOL
                    and raw_unencoded_residual>1e-3 and max(q0_matter1_residual,a2_matter0_q_driven_residual)<TOL
                    and minimum_delete>1e-8 and global_predicate_delete>1e-3 and covariance["pass"])}


def no_go_discipline() -> dict[str,object]:
    walls={
        "W_material_state_to_q_encoder": "the executed Cycle608 word takes the six-q detector label as an input register; it does not derive q from an independently supplied physical matter state",
        "W_same_device_generic_read_chart": "Cycle608's chosen origin has zero incident C rows and its transported frame/chart program is compile-time supplied; a same unprogrammed detector at every read cell is not executed",
    }
    families=[
        {"family":"streamed sparse origin read-light-cone circuit","honesty_marker":"ATTEMPTED","object_formulation":"coordinate-indexed sparse amplitudes and 1,065 ordered macro factors","mechanism_invariant":"exact W† P_A2 W product with reversible inverse","terminal_obligation":"Cycle668 four-bit equality on L3/L4/L6","status":"positive on supplied-q declared code","strength_vs_target":"strongest bounded partial"},
        {"family":"fully lowered one/two-M2 primitive stream","honesty_marker":"ATTEMPTED","object_formulation":"Cycle608 lowering recipes and explicit macro operands","mechanism_invariant":"negative shells, Toffoli, Gray controlled-Givens, route-return SWAP","terminal_obligation":"execute all 696,307 primitive factors per detector","status":"placement/count/digest exported; primitive-by-primitive state evolution not executed","strength_vs_target":"stronger physical execution"},
        {"family":"full-torus W cancellation to read light cone","honesty_marker":"RULED OUT BY PRIOR","object_formulation":"all-cell W and C equality rows","mechanism_invariant":"foreign-pivot cancellation and origin zero-incident-C chart","terminal_obligation":"full W†PW equality","status":"Cycle608 algebraic comparison only; not promoted here","strength_vs_target":"stronger/global"},
        {"family":"direct six-q A2 projector","honesty_marker":"ATTEMPTED","object_formulation":"17-factor mesh/equality/mesh inverse","mechanism_invariant":"number-preserving Slater mesh","terminal_obligation":"toggle detector pointer","status":"positive but weaker because it bypasses W","strength_vs_target":"weaker"},
        {"family":"physical occupancy-to-q syndrome extractor","honesty_marker":"OPEN / NOT ATTEMPTED","object_formulation":"independent physical matter rails and blank q ancillas","mechanism_invariant":"local reversible syndrome extraction","terminal_obligation":"derive q then run the executed product","status":"no extractor is supplied or constructed in this cycle; excluded from the qualifying-attempt count","strength_vs_target":"would close material-state semantics"},
    ]
    return {"N1_normalized_families":families,"N1_qualifying_attempts_for_negative":3,
            "N1_required_for_negative":5,"N1_threshold_met_for_negative":False,
            "N1_open_routes_not_counted":[{"family":"MPO contraction of the full primitive stream","status":"OPEN / NOT COUNTED"}],
            "N2_walls":walls,"N2_directed_ordered_pairs":[
                {"from":"W_material_state_to_q_encoder","to":"W_same_device_generic_read_chart","implied":False,"reason":"a q extractor need not remove chart programming"},
                {"from":"W_same_device_generic_read_chart","to":"W_material_state_to_q_encoder","implied":False,"reason":"a uniform chart does not derive q from matter"}],
            "N3_hidden_wall_scan":[
                {"condition":"six-q input label","classification":"explicit supplied structure and W_material_state_to_q_encoder"},
                {"condition":"origin read cell and compile-time transported frame","classification":"explicit supplied implementation and W_same_device_generic_read_chart"},
                {"condition":"N<=2 local table domain","classification":"explicit frozen quantifier, not hidden"},
                {"condition":"Cycle608 primitive decompositions","classification":"byte-pinned retained premise; macro execution does not back-credit full primitive execution"}],
            "N4_exact_residual_matches":[
                {"prior_cycle":608,"prior_residual":"physical primitive product null","current_residual":"origin macro product executed but primitive-by-primitive 696,307-factor evolution not executed","exact_match":False,"use_as_closure":False},
                {"prior_cycle":668,"prior_residual":"literal Cycle608 aggregate product open","current_residual":"origin read-light-cone W†P_A2W product executed","exact_match":True,"use_as_closure":True},
                {"prior_cycle":608,"prior_residual":"physical matter detector/readout null","current_residual":"material-state-to-q extraction remains absent","exact_match":True,"use_as_closure":False}],
            "N5_rhetoric":[
                {"claim":"macro product is not a dense full-Hilbert matrix","per_element":"all macro factors executed","per_site":"all operands placed","per_mode":"six q modes","per_block":"L3/L4/L6","lattice_wide":"full torus primitive evolution not claimed"},
                {"claim":"q-label agreement is not autonomous material detection","per_element":"q controls explicit","per_site":"matter interface is spectator","per_mode":"A2 projector exact","per_block":"three sizes","lattice_wide":"no autonomous detector network"},
                {"claim":"factor count is not rate or time","per_element":"ordered ordinal only","per_site":"route length only","per_mode":"no frequency","per_block":"finite circuit","lattice_wide":"no dynamics calibration"}],
            "N6_partial_closure_paths":[
                {"file":"UNMATERIALIZED/cycle608_physical_occupancy_to_q_extractor_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_material_state_to_q_encoder"},
                {"file":"UNMATERIALIZED/cycle608_full_primitive_sparse_stream_cycle_next.py","status":"OPEN","what_closes":"primitive-by-primitive execution gap"},
                {"file":"scripts/physical_cycle608_literal_aggregate_detector_product_cycle672_2026_07_23.py","status":"EXECUTED PARTIAL","what_closes":"origin macro product and Cycle668 interface equality"}],
            "N7_steelman":{"mechanism":"A hostile reviewer can close both named walls by reversibly extracting the six local occupation/parity syndromes into blank q ancillas at every cell with the already placed Cycle560 code coordinates, then applying a translation-invariant color-scheduled copy of this exact factor word and uncomputing q. The terminal test is a primitive-stream execution from two independently encoded physical states with the same former q label, at every read cell and frame, showing the detector follows matter rather than an imported q program.",
                "actionable_steps":["construct an explicit physical-rail-to-q syndrome circuit","execute it before and after the 696,307-factor primitive stream","repeat at every read cell with all24/all576 and q-label counterfactuals"],
                "terminal_test":"same-q/different-matter and same-matter/different-q counterfactuals, zero leakage, generic cells, full primitive stream"},
            "N8_cross_cycle_echo":[
                {"cycle":608,"mechanism":"factor/count blueprint","retired":"absence of an executed origin macro product","applicability":"does not retire material-to-q or generic-chart walls"},
                {"cycle":612,"mechanism":"computed Pd material predicate","retired":"supplied detector-output pointer at packet interface","applicability":"shows compute/uncompute shape but its active replay has schema drift"},
                {"cycle":668,"mechanism":"16-state D-F-D code kernel","retired":"missing detector-interface composition","applicability":"provides exact four-bit comparison target, not the q extractor"}],
            "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,
            "shared_route_independent_obstruction":False,"axiom_pressure_claim":False,
            "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
            "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","pass":True}


def resource_maxrss_bytes() -> int:
    value=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform=="darwin" else value*1024)


def main() -> int:
    global PASS,FAIL
    started=time.monotonic(); NOTE.parent.mkdir(parents=True,exist_ok=True); RECEIPT.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as cold:
        original=sys.stdout;sys.stdout=Tee(original,cold)
        try:
            freeze=target_freeze_controls();shore,receipts=shore_controls()
            check("target frozen before evidence",freeze["pass"],freeze)
            check("Cycle608/Cycle662/Cycle668 shores byte pinned with replay defects disclosed",shore["pass"],shore["ref"])
            with committed_cycle608_module() as c608:
                profile_by_label={}
                for profile_row in receipts["Cycle662"]["stochastic_dilation"]["rows"]:
                    profile_by_label.setdefault(profile_row["state"],profile_row)
                profile_rows=tuple(profile_by_label.values())
                pinned_rows={row["length"]:row for row in receipts["Cycle608"]["compiler_rows"]}
                size_rows=[]
                for length in (3,4,6):
                    row=execute_size(c608,length,profile_rows,pinned_rows[length]);size_rows.append(row)
                    check(f"L{length} committed sparse aggregate product",row["pass"],{
                        "four_bit":row["maximum_Cycle668_four_bit_residual"],"inverse":row["table_and_inverse"]["maximum_W_inverse_residual"],
                        "delete":row["minimum_per_factor_deletion_signal"],"covariance":row["covariance"]["pass"]})
            max_four=max(row["maximum_Cycle668_four_bit_residual"] for row in size_rows)
            max_compute=max(row["maximum_detector_compute_residual"] for row in size_rows)
            total_fixtures=sum(row["fixture_comparison_count"] for row in size_rows)
            total_deletions=sum(row["per_factor_deletion_count"] for row in size_rows)
            check("train/held biased/nonproduct contact-on/off aggregate equality",max(max_four,max_compute)<TOL,
                  {"fixtures":total_fixtures,"max_four_bit":max_four,"max_compute":max_compute})
            check("every exported aggregate factor has deletion witness",total_deletions==3*1065 and
                  min(row["minimum_per_factor_deletion_signal"] for row in size_rows)>1e-8,total_deletions)
            nogo=no_go_discipline();check("full current N1-N8 with no no-go or axiom claim",nogo["pass"] and not nogo["shared_obstruction_claim"],nogo["N2_walls"])
            status=("positive executed sparse Cycle608 origin aggregate detector macro product on the supplied-q declared code; "
                    "physical matter-to-q extraction, generic same-device chart and primitive-by-primitive full stream remain open")
            receipt={"cycle":672,"date":"2026-07-23","authority":AUTHORITY,"audit":AUDIT,"status":status,
                     "Status":"PASS" if FAIL==0 else "FAIL","pass":FAIL==0,"tests_passed":PASS,"tests_failed":FAIL,
                     "elapsed_seconds":time.monotonic()-started,"maximum_RSS_bytes":resource_maxrss_bytes(),
                     "target_contract":TARGET_CONTRACT,"target_freeze":freeze,"shore":shore,
                     "committed_dependency_execution":"Cycle608 module graph loaded from git archive of SHORE; dirty matching copies not used",
                     "size_rows":size_rows,"aggregate_summary":{"sizes":[3,4,6],"Cycle662_state_labels":list(profile_by_label),
                        "fixture_comparisons":total_fixtures,"per_factor_deletion_witnesses":total_deletions,
                        "maximum_detector_compute_residual":max_compute,"maximum_Cycle668_four_bit_residual":max_four,
                        "all24_all576_failures":sum(not row["covariance"]["pass"] for row in size_rows),
                        "literal_origin_macro_product_executed":True,"primitive_by_primitive_696307_factor_state_evolution_executed":False,
                        "full_torus_all_cell_product_executed":False,"pass":all(row["pass"] for row in size_rows)},
                     "supplied_structure_inventory":{"six_q_label_register":True,"Cycle608_local_tables_and_Pauli_representatives":True,
                        "Cycle608_A2_orbitals_mesh_and_primitive_lowerings":True,"Cycle668_four_bit_target":True,
                        "Cycle662_biased_nonproduct_profiles_as_explicit_tensor_spectators":True,"contact_binder_mapping":True,
                        "blank_branch_work_pointer_and_opportunity":True,"compile_time_chart_and_frames":True,
                        "Cycle608_inverse_role_table_code_preparation":True,
                        "physical_matter_to_q_encoder":False,"same_unprogrammed_generic_read_device":False,
                        "host_scheduler":False,"runtime_grade_lookup":False,"shell_predicate_ROM":False},
                     "route_disposition":{"sparse_origin_macro_product":"PASS_EXECUTED",
                        "direct_A2_projector":"PASS_WEAKER","fully_lowered_primitive_state_evolution":"OPEN_NOT_EXECUTED",
                        "full_torus_product":"OPEN_ALGEBRAIC_CANCELLATION_ONLY","physical_matter_to_q":"OPEN_NOT_SUPPLIED"},
                     "highest_honest_terminal":"bounded executed origin read-light-cone macro product on the explicit inverse-role-table image of supplied q labels",
                     "target_contract_candidate_terminal_met":False,"bounded_partial_construction_pass":True,
                     "strict_full_framework_terminal_met":False,
                     "strongest_constructive_result":"1,065-factor coordinate-explicit W_origin dagger P_A2 W_origin sparse product executed on L3/L4/L6 and composed on its explicit inverse-role-table code to the Cycle668 four-bit interface with zero-to-tolerance leakage, inverse and transported-frame checks plus exact unitary per-factor deletion witnesses",
                     "six_wall_ledger":{"C_ref":"unchanged; q label, A2 orbitals and contact binder supplied",
                        "C_num":"unchanged; committed Cycle608 matrices and Cycle662 labels supplied",
                        "C_wrap":"unchanged; no wrapped phase/energy claim","C_int":"advance: literal origin macro product now executed",
                        "C_local":"advance on origin read light cone; matter-to-q and generic chart open",
                        "C_source":"unchanged; no energy/gravity/source identification"},
                     "no_go_discipline":nogo,"shared_obstruction_claim":False,"shared_route_independent_obstruction":False,
                     "axiom_pressure":False,"axiom_pressure_claim":False,"constitutional_effect":"none",
                     "optimal_next_campaign":"construct and execute a reversible physical-occupancy-to-six-q syndrome extractor, then lower and stream every one/two-M2 factor of the detector at generic read cells"}
            receipt["runner_sha256"]=sha256(Path(__file__).read_bytes()).hexdigest()
            receipt["note_sha256"]=sha256(NOTE.read_bytes()).hexdigest() if NOTE.exists() else None
            RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
            print("REPORT_JSON",json.dumps(receipt,sort_keys=True,separators=(",",":")))
            print("SUMMARY",{"tests_passed":PASS,"tests_failed":FAIL,"status":status})
        finally:sys.stdout=original
    return int(FAIL!=0)


if __name__=="__main__":raise SystemExit(main())
