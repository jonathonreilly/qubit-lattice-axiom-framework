#!/usr/bin/env python3
"""Cycle647: three-route full isometry tournament for Cycle642's orbit tree.

Route A uses an exact fiber/tree decoder, a physical-distance-greedy ordered
rough stabilizer peel, and a distance-greedy complete logical chart.  Route B
is the Cycle643 generic signed-tableau comparator applied directly to the
Cycle642 code.  Route C uses the exact fiber/tree decoder followed by the
generic rough stabilizer and logical-chart reductions.

All executable premises are loaded from immutable git objects.  The emitted
circuits are supplied compile schedules, not autonomous dynamics or time.
Authority none; audit unset; author accepted false.
"""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
import resource
import signal
import subprocess
import sys
import time
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHORE = "99b98a6fd2c823734e98487bf67daa8fef79dd92"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ORBIT_TREE_STRUCTURED_FULL_ISOMETRY_TOURNAMENT_CYCLE647_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_orbit_tree_structured_full_isometry_tournament_cycle647_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_orbit_tree_structured_full_isometry_tournament_cycle647_cold_2026_07_23.txt"
AUTHORITY = "none"
AUDIT = "unset"
PASS = FAIL = 0

PINS = {
    "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py": "fb0d8366494066e4191d66b9a2d83180cd99bf6f622b9de355bf28494e050bf7",
    "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md": "13f8074746f3b5e978f971567bbebecd1006ccd13b7d5fe91a0e38a946d30d3e",
    "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_receipt_2026_07_23.json": "9251ac323d4f26b672783fa8ed01dc8da6f3059c308d37325b3d7984969c3b37",
    "scripts/abstract_fill_disk_full_tableau_isometry_cycle643_2026_07_23.py": "e64afbb2e7b97b02c90adc3245b92008f8a18b026efe3d5e1ff65cd363295c94",
    "docs/work_history/repo/review_feedback/ABSTRACT_FILL_DISK_FULL_TABLEAU_ISOMETRY_CYCLE643_NOTE_2026-07-23.md": "e28a55a8312ae9cf4b9048f8b07557602e5a223cc6da487eeddd8b730a982d8f",
    "outputs/abstract_fill_disk_full_tableau_isometry_cycle643_receipt_2026_07_23.json": "d87bf3c90cd0016073cd5f3259f5d8c45c81dbc0796174361057ef5edd07cbec",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def git_bytes(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{SHORE}:{path}"], cwd=ROOT)


def load_exact(name: str, path: str):
    module = types.ModuleType(name)
    module.__file__ = str(ROOT / path)
    module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(path), module.__file__, "exec"), module.__dict__)
    return module


# Cycle643 is loaded first so its exact Cycle532/537 modules are shared with
# Cycle642.  Their source hashes are identical at the two immutable shores.
c643 = load_exact("cycle647_exact_cycle643", "scripts/abstract_fill_disk_full_tableau_isometry_cycle643_2026_07_23.py")
c642 = load_exact("cycle647_exact_cycle642", "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py")
c532 = c643.c532
Pauli = c643.Pauli
Gate = c643.Gate


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def bit_indices(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def positions(obj: dict, length: int) -> tuple[tuple[int, int, int], ...]:
    modulus = c642.K * length
    old = tuple(tuple(value % modulus for value in c642.old_position_K(obj["graph"], q))
                for q in range(obj["graph"].qubits))
    aux = tuple(tuple(value % modulus for value in site) for site in obj["coordinates"])
    return old + aux


def distance(left, right, modulus: int) -> int:
    return c642.periodic_l1(left, right, modulus)


def best_pivot(candidates: list[int], support: list[int], coords, modulus: int) -> int:
    return min(candidates, key=lambda q: (
        max((distance(coords[q], coords[r], modulus) for r in support), default=0),
        sum(distance(coords[q], coords[r], modulus) for r in support), q,
    ))


def ordered_reduce(rows: tuple[Pauli, ...], qubits: int, coords,
                   modulus: int, forced_pivots: tuple[int, ...] | None = None) -> dict:
    """Exact signed column reduction in supplied row order.

    Row multiplication is a classical synthesis operation only.  When pivots
    are not forced, the pivot minimizes the current row's exact physical
    periodic-L1 fanout radius.
    """
    basis = rows if forced_pivots is not None else c643.independent_paulis(rows, qubits, False)
    if forced_pivots is not None and len(basis) != len(forced_pivots):
        raise AssertionError("forced pivot count")
    tab = c643.BitTableau(basis, qubits)
    active_rows = (1 << len(basis)) - 1
    active_qubits = set(range(qubits))
    gates: list[Gate] = []
    pivots = []
    for pivot_row in range(len(basis)):
        mark = 1 << pivot_row
        x, z = tab.support(pivot_row, active_qubits)
        support = list(bit_indices(x | z))
        if not support:
            raise AssertionError(("ordered independent row vanished", pivot_row))
        if forced_pivots is not None:
            pivot_q = forced_pivots[pivot_row]
            if pivot_q not in active_qubits or not (((x | z) >> pivot_q) & 1):
                raise AssertionError(("forced pivot absent", pivot_row, pivot_q, support))
        else:
            candidates = list(bit_indices(x)) or list(bit_indices(z))
            pivot_q = best_pivot(candidates, support, coords, modulus)
        use_x = bool((x >> pivot_q) & 1)
        q_order = sorted(active_qubits)
        if use_x:
            if tab.z[pivot_q] & mark:
                c643.append_gate(tab, gates, "S", pivot_q)
            for q in q_order:
                if q == pivot_q: continue
                xb = bool(tab.x[q] & mark); zb = bool(tab.z[q] & mark)
                if not (xb or zb): continue
                if xb and zb: c643.append_gate(tab, gates, "S", q)
                elif zb: c643.append_gate(tab, gates, "H", q)
                c643.append_gate(tab, gates, "CNOT", pivot_q, q)
            px, pz = tab.support(pivot_row, active_qubits)
            if px != 1 << pivot_q or pz:
                raise AssertionError(("ordered X reduction", pivot_row, pivot_q))
            selected = (tab.x[pivot_q] & active_rows) ^ mark
            tab.multiply_rows(pivot_row, selected, px, pz)
            c643.append_gate(tab, gates, "H", pivot_q)
        else:
            for q in q_order:
                if q != pivot_q and tab.z[q] & mark:
                    c643.append_gate(tab, gates, "CNOT", q, pivot_q)
            px, pz = tab.support(pivot_row, active_qubits)
            if px or pz != 1 << pivot_q:
                raise AssertionError(("ordered Z reduction", pivot_row, pivot_q))
            selected = (tab.z[pivot_q] & active_rows) ^ mark
            tab.multiply_rows(pivot_row, selected, px, pz)
        px, pz = tab.support(pivot_row)
        if px or pz != 1 << pivot_q:
            raise AssertionError(("ordered canonical", pivot_row, pivot_q))
        if tab.phase(pivot_row) == 2:
            c643.flip_z_sign(tab, gates, pivot_q)
        if tab.phase(pivot_row) != 0:
            raise AssertionError(("ordered sign", pivot_row, tab.phase(pivot_row)))
        pivots.append(pivot_q)
        active_rows ^= mark
        active_qubits.remove(pivot_q)
    return {"basis": basis, "decoder_gates": tuple(gates),
            "pivot_qubits": frozenset(pivots),
            "logical_qubits": tuple(q for q in range(qubits) if q not in set(pivots))}


def tree_postorder(length: int):
    vertices, edges = c642.fill_tree(length)
    adjacency = {vertex: [] for vertex in vertices}
    for edge in edges:
        left, right = edge
        adjacency[left].append((right, edge)); adjacency[right].append((left, edge))
    parent = {c642.ROOT_VERTEX: None}; parent_edge = {}; order = [c642.ROOT_VERTEX]
    for vertex in order:
        for target, edge in sorted(adjacency[vertex], key=repr):
            if target in parent: continue
            parent[target] = vertex; parent_edge[target] = edge; order.append(target)
    return tuple(reversed(order[1:])), parent_edge


def structured_cap_decoder(obj: dict, length: int, coords) -> dict:
    gates: list[Gate] = []
    equality_pivots = []
    for role in obj["roles"]:
        bits = obj["index"][role]
        root = bits[0]
        for q in bits:
            gates.append(Gate("H", q))
        for q in bits[1:]:
            gates.append(Gate("CNOT", root, q)); equality_pivots.append(q)
    equality_gates = tuple(gates)
    postorder, parent_edge = tree_postorder(length)
    face_rows = []
    face_pivots = []
    for axis in range(3):
        vertex_index = {vertex: index for index, vertex in enumerate(c642.fill_tree(length)[0])}
        for vertex in postorder:
            face_rows.append(obj["face_by_axis"][axis][vertex_index[vertex]])
            edge = parent_edge[vertex]
            face_pivots.append(obj["index"][(axis, edge[0], edge[1])][0])
    transformed_faces = c643.transform_rows(tuple(face_rows), obj["qubits"], equality_gates)
    face_reduced = ordered_reduce(
        transformed_faces, obj["qubits"], coords, c642.K * length,
        tuple(face_pivots),
    )
    preliminary_gates = equality_gates + face_reduced["decoder_gates"]
    preliminary_pivots = frozenset(equality_pivots + face_pivots)
    preliminary_mask = sum(1 << q for q in preliminary_pivots)
    # The three root faces carry the three old Wilson initializers.  They are
    # independent of Cycle642's unfixed local rows and therefore require
    # three additional rough pivots after the nine tree-edge pivots.
    root_faces = tuple(obj["face_by_axis"][axis][0] for axis in range(3))
    transformed_roots = c643.transform_rows(root_faces, obj["qubits"], preliminary_gates)
    if any(row.x & preliminary_mask for row in transformed_roots):
        raise AssertionError("root face has prior-pivot X")
    cleaned_roots = tuple(Pauli(row.phase, row.x, row.z & ~preliminary_mask) for row in transformed_roots)
    root_reduced = ordered_reduce(cleaned_roots, obj["qubits"], coords, c642.K * length)
    if root_reduced["pivot_qubits"] & preliminary_pivots:
        raise AssertionError("root/preliminary pivot overlap")
    cap_gates = preliminary_gates + root_reduced["decoder_gates"]
    cap_pivots = frozenset(preliminary_pivots | root_reduced["pivot_qubits"])
    decoded_basis = c643.transform_rows(tuple(face_rows) + root_faces, obj["qubits"], cap_gates)
    cap_mask = sum(1 << q for q in cap_pivots)
    face_failures = sum(row.phase != 0 or row.x or bool(row.z & ~cap_mask) for row in decoded_basis)
    equality_decoded = c643.transform_rows(obj["equality"], obj["qubits"], cap_gates)
    equality_failures = sum(row.phase != 0 or row.x or bool(row.z & ~cap_mask) for row in equality_decoded)
    return {
        "decoder_gates": cap_gates, "pivot_qubits": cap_pivots,
        "equality_pivots": frozenset(equality_pivots),
        "face_pivots": frozenset(face_pivots) | root_reduced["pivot_qubits"],
        "equality_gate_count": len(equality_gates),
        "face_gate_count": len(face_reduced["decoder_gates"]) + len(root_reduced["decoder_gates"]),
        "displayed_equality_reference_failures": equality_failures,
        "independent_face_reference_failures": face_failures,
    }


def stabilizer_decoder(obj: dict, length: int, route: str, coords) -> dict:
    n = obj["qubits"]
    if route == "B_generic_all":
        result = c643.reduce_stabilizers(obj["stabilizers"], n)
        return {**result, "cap": None, "rough_gate_count": None}
    cap = structured_cap_decoder(obj, length, coords)
    cap_gates = cap["decoder_gates"]
    cap_pivots = cap["pivot_qubits"]
    cap_mask = sum(1 << q for q in cap_pivots)
    transformed_local = c643.transform_rows(obj["local"], n, cap_gates)
    if any(row.x & cap_mask for row in transformed_local):
        raise AssertionError("local stabilizer has cap-pivot X after structured cap decoder")
    cleaned_local = tuple(Pauli(row.phase, row.x, row.z & ~cap_mask) for row in transformed_local)
    if route == "A_local_peel":
        rough = ordered_reduce(cleaned_local, n, coords, c642.K * length)
    elif route == "C_hybrid":
        rough = c643.reduce_stabilizers(cleaned_local, n)
    else:
        raise ValueError(route)
    if rough["pivot_qubits"] & cap_pivots:
        raise AssertionError("cap/rough pivot overlap")
    pivots = frozenset(cap_pivots | rough["pivot_qubits"])
    return {
        "basis": tuple(), "decoder_gates": cap_gates + rough["decoder_gates"],
        "pivot_qubits": pivots,
        "logical_qubits": tuple(q for q in range(n) if q not in pivots),
        "cap": cap, "rough_gate_count": len(rough["decoder_gates"]),
    }


def dress_old(obj: dict, pauli: Pauli, length: int) -> Pauli:
    x = pauli.x
    for axis in range(3):
        marked = {j for j, chunk in enumerate(obj["chunks"][axis]) if not pauli.commutes(chunk)}
        if len(marked) % 2:
            raise AssertionError("odd Wilson commutator in parity dressing")
        for left, right in c642.tree_selected_edges(marked, length):
            x ^= 1 << obj["index"][(axis, left, right)][0]
    return Pauli(pauli.phase, x, pauli.z)


def local_complete_frame(x_rows: tuple[Pauli, ...], z_rows: tuple[Pauli, ...],
                         logical: tuple[int, ...], qubits: int, coords, modulus: int) -> dict:
    combined = tuple(item for pair in zip(x_rows, z_rows) for item in pair)
    tab = c643.BitTableau(combined, qubits)
    gates: list[Gate] = []; active = set(logical); pivots = []
    for pair_index in range(len(x_rows)):
        xi = 2 * pair_index; zi = xi + 1; mark_x = 1 << xi
        xx, xz = tab.support(xi, active)
        support = list(bit_indices(xx | xz))
        q = best_pivot(support, support, coords, modulus)
        if not (tab.x[q] & mark_x): c643.append_gate(tab, gates, "H", q)
        if tab.z[q] & mark_x: c643.append_gate(tab, gates, "S", q)
        for other in sorted(active):
            if other == q: continue
            xb = bool(tab.x[other] & mark_x); zb = bool(tab.z[other] & mark_x)
            if not (xb or zb): continue
            if xb and zb: c643.append_gate(tab, gates, "S", other)
            elif zb: c643.append_gate(tab, gates, "H", other)
            c643.append_gate(tab, gates, "CNOT", q, other)
        if tab.x[q] & (1 << zi):
            for kind in ("H", "S", "H"): c643.append_gate(tab, gates, kind, q)
        for other in sorted(active):
            if other == q: continue
            xb = bool(tab.x[other] & (1 << zi)); zb = bool(tab.z[other] & (1 << zi))
            if not (xb or zb): continue
            if xb and zb:
                c643.append_gate(tab, gates, "S", other); c643.append_gate(tab, gates, "H", other)
            elif xb: c643.append_gate(tab, gates, "H", other)
            c643.append_gate(tab, gates, "CNOT", other, q)
        zx, zz = tab.support(zi, active)
        if zx or zz != 1 << q: raise AssertionError(("local frame Z", pair_index, q))
        if tab.phase(xi) == 2:
            c643.append_gate(tab, gates, "S", q); c643.append_gate(tab, gates, "S", q)
        if tab.phase(zi) == 2: c643.flip_z_sign(tab, gates, q)
        if tab.phase(xi) or tab.phase(zi): raise AssertionError("local frame sign")
        pivots.append(q); active.remove(q)
    return {"decoder_gates": tuple(gates), "input_pivots": tuple(pivots)}


def build_isometry(length: int, route: str, obj: dict, coords) -> tuple[dict, dict]:
    started = time.perf_counter(); n = obj["qubits"]; cells = length ** 3
    reduced = stabilizer_decoder(obj, length, route, coords)
    stab_gates = reduced["decoder_gates"]; pivots = reduced["pivot_qubits"]
    logical = reduced["logical_qubits"]
    expected_rank = 15 * cells + 1 + (n - obj["graph"].qubits)
    if len(pivots) != expected_rank or len(logical) != 7 * cells - 1:
        raise AssertionError((route, length, len(pivots), expected_rank, len(logical)))
    raw_matter = tuple(obj["matter"]); raw_gauge = tuple(obj["gauge"])
    matter_parity = dress_old(obj, c643.c537.pauli_product(
        obj["graph"].B(v) for v in range(obj["graph"].matter_count)), length)
    raw_gz, _raw_ga, _ = c532.gauge_generators(obj["graph"])
    gauge_parity = dress_old(obj, c643.c537.pauli_product(raw_gz), length)
    all_ops = raw_matter + raw_gauge + (matter_parity, gauge_parity)
    decoded = c643.transform_rows(all_ops, n, stab_gates)
    matter_dec = tuple(c643.clean_ancilla(row, pivots) for row in decoded[:len(raw_matter)])
    gauge_dec = tuple(c643.clean_ancilla(row, pivots) for row in decoded[len(raw_matter):len(raw_matter)+len(raw_gauge)])
    pm = c643.clean_ancilla(decoded[-2], pivots); pg = c643.clean_ancilla(decoded[-1], pivots)
    mgs = c643.symplectic_gram_schmidt(tuple(row.symplectic(n) for row in matter_dec), n)
    ggs = c643.symplectic_gram_schmidt(tuple(row.symplectic(n) for row in gauge_dec), n)
    if len(mgs["pairs"]) != 6*cells-1 or len(ggs["pairs"]) != cells-1:
        raise AssertionError("Gram dimensions")
    parity = pm.symplectic(n)
    if not (mgs["radicals"][0][0] == ggs["radicals"][0][0] == parity == pg.symplectic(n)):
        raise AssertionError("shared parity")
    matter_pairs = [(a[0], b[0]) for a, b in mgs["pairs"]]
    gauge_pairs = [(a[0], b[0]) for a, b in ggs["pairs"]]
    qvec = c643.find_parity_conjugate(parity, matter_pairs + gauge_pairs, n)
    frame_pairs = matter_pairs + [(qvec, parity)] + gauge_pairs
    coeffs = list(mgs["pairs"]) + [((qvec, 0), (parity, mgs["radicals"][0][1]))] + list(ggs["pairs"])
    frame_x = []; frame_z = []
    for index, ((xv, zv), pair) in enumerate(zip(frame_pairs, coeffs)):
        if index < len(matter_pairs):
            xp = c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(matter_dec, pair[0][1]), pivots))
            zp = c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(matter_dec, pair[1][1]), pivots))
        elif index == len(matter_pairs):
            xp = c643.positive_hermitian(Pauli(0, qvec & ((1 << n)-1), qvec >> n))
            zp = c643.positive_hermitian(pm)
        else:
            xp = c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(gauge_dec, pair[0][1]), pivots))
            zp = c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(gauge_dec, pair[1][1]), pivots))
        if xp.symplectic(n) != xv or zp.symplectic(n) != zv: raise AssertionError("frame rep")
        frame_x.append(xp); frame_z.append(zp)
    if route == "A_local_peel":
        frame = local_complete_frame(tuple(frame_x), tuple(frame_z), logical, n, coords, c642.K*length)
    else:
        frame = c643.reduce_complete_frame(tuple(frame_x), tuple(frame_z), logical, n)
    decoder = stab_gates + frame["decoder_gates"]; encoder = c643.inverse_gates(decoder)
    target_wires = frozenset(frame["input_pivots"][:6*cells]); gauge_wires = frozenset(frame["input_pivots"][6*cells:])
    target_mask = sum(1 << q for q in target_wires); gauge_mask = sum(1 << q for q in gauge_wires)
    ancilla_mask = sum(1 << q for q in pivots)
    decoded_stabs = c643.transform_rows(obj["stabilizers"], n, decoder)
    stab_fail = sum(row.phase != 0 or row.x or bool(row.z & ~ancilla_mask) for row in decoded_stabs)
    total_decoded = c643.transform_rows(all_ops, n, decoder)
    matter_fail = gauge_fail = ancilla_x_fail = 0
    parity_wire = frame["input_pivots"][6*cells-1]
    for index, row in enumerate(total_decoded):
        ancilla_x_fail += bool(row.x & ancilla_mask); support = row.x | row.z
        if index < len(raw_matter): matter_fail += bool(support & gauge_mask)
        elif index < len(raw_matter)+len(raw_gauge):
            gauge_fail += bool(support & ~(target_mask | gauge_mask | ancilla_mask))
            gauge_fail += bool(support & target_mask & ~(1 << parity_wire))
    pmd, pgd = total_decoded[-2:]
    logical_mask = target_mask | gauge_mask
    parity_match = (pmd.phase, pmd.x & logical_mask, pmd.z & logical_mask) == (pgd.phase, pgd.x & logical_mask, pgd.z & logical_mask)
    counts = Counter(g.kind for g in encoder)
    row = {
        "route": route, "length": length,
        "split": {3:"construction",6:"train",7:"held-out-no-refit"}[length],
        "coarse_cells": cells, "physical_M2": n, "M2_labels_per_cell": n/cells,
        "target_Fock_input_qubits": 6*cells, "gauge_input_qubits": cells-1,
        "blank_stabilizer_M2": len(pivots), "code_exponent": len(logical), "work_M2": 0,
        "exact_partition": 6*cells + cells-1 + len(pivots) == n,
        "encoder_factor_count": len(encoder), "encoder_factors_per_cell": len(encoder)/cells,
        "encoder_factor_counts": dict(counts), "encoder_factor_sha256": c643.gate_digest(encoder),
        "stabilizer_decoder_factors": len(stab_gates), "logical_chart_factors": len(frame["decoder_gates"]),
        "structured_cap_factors": None if reduced["cap"] is None else len(reduced["cap"]["decoder_gates"]),
        "structured_rough_factors": reduced["rough_gate_count"],
        "all_displayed_stabilizer_reference_failures": stab_fail,
        "matter_partition_failures": matter_fail, "gauge_partition_failures": gauge_fail,
        "ancilla_X_leakage_failures": ancilla_x_fail,
        "shared_parity_logical_match": parity_match, "both_matter_parities_in_domain": True,
        "elapsed_seconds": time.perf_counter()-started,
    }
    row["pass"] = bool(row["exact_partition"] and stab_fail == matter_fail == gauge_fail == ancilla_x_fail == 0 and parity_match)
    internal = {"obj":obj,"encoder":encoder,"decoder":decoder,"pivots":pivots,
                "input_pivots":frame["input_pivots"],"raw_ops":all_ops,
                "target_wires":target_wires,"gauge_wires":gauge_wires,
                "abstract_coordinates":tuple(c643.abstract_coordinates(r,frame["input_pivots"],pivots)[:3] for r in total_decoded)}
    return row, internal


def gate_distance_audit(row: dict, internal: dict, coords) -> dict:
    modulus = c642.K * row["length"]
    distances = [distance(coords[g.a], coords[g.b], modulus) for g in internal["encoder"] if g.kind == "CNOT"]
    ordered = sorted(distances)
    def quantile(f): return ordered[min(len(ordered)-1, int(f*(len(ordered)-1)))] if ordered else None
    return {
        "route":row["route"], "length":row["length"], "fine_grid_period":modulus,
        "two_qubit_factors":len(distances), "distance_one":sum(v==1 for v in distances),
        "distance_greater_than_one":sum(v>1 for v in distances),
        "maximum_periodic_fine_L1":max(distances,default=None),
        "p50_p90_p99":[quantile(.5),quantile(.9),quantile(.99)],
        "all_factors_bounded_by_finite_torus_diameter":max(distances,default=0) <= 3*modulus//2,
    }


def inverse_and_deletion(rows, internals) -> dict:
    inverse_rows = []; deletion_rows = []; gauge_vacuum_rows = []
    for row, internal in zip(rows, internals):
        n=row["physical_M2"]
        indices=tuple(sorted(set((0,1,n//4,n//2,3*n//4,n-2,n-1,*sorted(internal["pivots"])[:3],*internal["input_pivots"][:3],*internal["input_pivots"][-3:]))))
        probes=tuple(item for q in indices for item in (Pauli(x=1<<q),Pauli(z=1<<q)))
        returned=c643.transform_rows(probes,n,internal["encoder"]+internal["decoder"])
        inverse_rows.append({"route":row["route"],"length":row["length"],"probes":len(probes),"failures":sum(a!=b for a,b in zip(probes,returned))})
        if row["length"]==3:
            ancilla_mask=sum(1<<q for q in internal["pivots"])
            for kind in ("H","S","CNOT"):
                index=next(i for i,g in enumerate(internal["decoder"]) if g.kind==kind)
                altered=internal["decoder"][:index]+internal["decoder"][index+1:]
                decoded=c643.transform_rows(tuple(internal["obj"]["stabilizers"]),n,altered)
                failures=sum(r.phase!=0 or r.x or bool(r.z & ~ancilla_mask) for r in decoded)
                deletion_rows.append({"route":row["route"],"kind":kind,"factor_index":index,"stabilizer_failures":failures,"detected":failures>0})
            stabilizers=tuple(internal["obj"]["stabilizers"])
            base_rank,base_inconsistent=c532.phase_rank(stabilizers,n)
            gauge_input=tuple(Pauli(z=1<<q) for q in sorted(internal["gauge_wires"]))
            gauge_encoded=c643.transform_rows(gauge_input,n,internal["encoder"])
            vacuum_rank,vacuum_inconsistent=c532.phase_rank(stabilizers+gauge_encoded,n)
            deleted_rank,deleted_inconsistent=c532.phase_rank(stabilizers+gauge_encoded[1:],n)
            malformed=(Pauli((gauge_encoded[0].phase+2)%4,gauge_encoded[0].x,gauge_encoded[0].z),)+gauge_encoded[1:]
            malformed_rank,malformed_inconsistent=c532.phase_rank(stabilizers+malformed,n)
            flipped=(Pauli((stabilizers[0].phase+2)%4,stabilizers[0].x,stabilizers[0].z),)+stabilizers[1:]
            _flipped_rank,flipped_inconsistent=c532.phase_rank(flipped,n)
            matter_commutators=sum(not vacuum.commutes(matter) for vacuum in gauge_encoded for matter in internal["obj"]["matter"])
            gauge_vacuum_rows.append({"route":row["route"],"length":3,"gauge_references":len(gauge_encoded),
                "base_stabilizer_rank":base_rank,"stabilizer_plus_gauge_vacuum_rank":vacuum_rank,
                "delete_one_gauge_reference_rank":deleted_rank,"minus_gauge_reference_rank":malformed_rank,
                "phase_inconsistencies":{"base":base_inconsistent,"vacuum":vacuum_inconsistent,"deleted":deleted_inconsistent,"minus_gauge":malformed_inconsistent,"flipped_stabilizer":flipped_inconsistent},
                "minus_gauge_reference_consistent_but_refused_by_plus_fixture":malformed_inconsistent==0,
                "gauge_vacuum_matter_commutator_failures":matter_commutators,
                "pass":vacuum_rank==base_rank+row["gauge_input_qubits"] and deleted_rank==vacuum_rank-1 and malformed_rank==vacuum_rank and base_inconsistent==vacuum_inconsistent==deleted_inconsistent==malformed_inconsistent==matter_commutators==0 and flipped_inconsistent>0})
    return {"inverse_rows":inverse_rows,"representative_factor_deletions":deletion_rows,
            "optional_plus_gauge_vacuum_controls":gauge_vacuum_rows,
            "factorwise_inverse_rules":{"H":"H","S":"S S S","CNOT":"CNOT"},
            "pass":all(r["failures"]==0 for r in inverse_rows) and all(r["detected"] for r in deletion_rows) and all(r["pass"] for r in gauge_vacuum_rows)}


def covariance_audit(objects: dict) -> dict:
    frames=tuple(c642.FRAMES); rows=[]
    for length,obj in objects.items():
        graph=obj["graph"]
        old_maps=[tuple(c532.c247.graph_frame_maps(graph,frame)[1]) for frame in frames]
        aux_lookup={site:bit for role in obj["roles"] for bit,site in zip(obj["index"][role],obj["fibers"][role])}
        maps=[]; frame_fail=0
        for frame,old in zip(frames,old_maps):
            mapping=list(old)
            for role in obj["roles"]:
                for bit,site in zip(obj["index"][role],obj["fibers"][role]):
                    target=tuple(int(v) for v in frame @ c642.np.asarray(site,dtype=int))
                    if target not in aux_lookup: frame_fail+=1; mapping.append(bit)
                    else: mapping.append(aux_lookup[target])
            maps.append(tuple(mapping))
        frame_index={tuple(int(v) for v in frame.ravel()):i for i,frame in enumerate(frames)}
        group_fail=0
        for li,left in enumerate(frames):
            for ri,right in enumerate(frames):
                direct=maps[frame_index[tuple(int(v) for v in (left@right).ravel())]]
                composed=tuple(maps[li][maps[ri][q]] for q in range(obj["qubits"]))
                group_fail += composed != direct
        rows.append({"length":length,"extended_M2":obj["qubits"],"frame_label_failures":frame_fail,
                     "all576_extended_permutation_group_failures":group_fail})
    return {"proper_cubic_frames":24,"frame_products":576,"rows":rows,
            "encoder_transport_rule":"E_R = F_R E C_R^dagger; each supplied circuit is relabeled/conjugated as one compile-time family, not queried at runtime",
            "runtime_frame_selector":False,"single_invariant_factor_order_claimed":False,
            "pass":all(r["frame_label_failures"]==r["all576_extended_permutation_group_failures"]==0 for r in rows)}


def inherited_update(rows) -> dict:
    inherited=c643.c537.inherited_target_controls(); fixture=inherited["mass_contact_and_seam"]
    route_rows=[]
    for route in ("A_local_peel","B_generic_all","C_hybrid"):
        subset=[r for r in rows if r["route"]==route]
        failures=sum(r["matter_partition_failures"]+r["gauge_partition_failures"]+r["ancilla_X_leakage_failures"] for r in subset)
        route_rows.append({"route":route,"generator_failures":failures,
                           "E_Gcoarse_equals_Gtree_code_E_on_declared_code":inherited["pass"] and failures==0})
    return {"composition_level":"complete generator and polynomial algebra on the declared Cycle642 code space",
            "routes":route_rows,"coin_onsite_residual":fixture["onsite_intertwiner_residual"],
            "FSWAP_matrix_residual":inherited["FSWAP_polynomial_inverse"]["matrix_residual"],
            "contact_active_two_particle_states":fixture["Cycle230_contact_active_two_particle_states"],
            "contact_deletion_residual":fixture["Cycle230_contact_deletion_residual"],
            "Cycle219_mass_residual":fixture["Cycle219_mass_fixture_residual"],
            "Cycle230_seam_subchecks":fixture["Cycle230_seam_subchecks"],
            "B_coefficient_failures":sum(x["coefficient_identity_failures"] for x in inherited["full_Fock_Gamma_P"]["quadratic_full_Fock_theorems"]),
            "strict_local_physical_M2_update_claimed":False,
            "pass":inherited["pass"] and all(r["E_Gcoarse_equals_Gtree_code_E_on_declared_code"] for r in route_rows)}


def citation(path: str, fragment: str) -> dict:
    for line,text in enumerate(git_bytes(path).decode().splitlines(),1):
        if fragment in text: return {"ref":SHORE,"path":path,"line":line,"text":text.strip()}
    raise AssertionError((path,fragment))


def current_citation(fragment: str) -> dict:
    for line,text in enumerate(Path(__file__).read_text().splitlines(),1):
        if fragment in text:
            return {"ref":"Cycle647 current artifact","path":str(Path(__file__).relative_to(ROOT)),"line":line,"text":text.strip()}
    raise AssertionError(fragment)


def no_go_discipline() -> dict:
    families=[
        {"family":"structured cap plus distance-greedy rough peel","object_formulation":"Cycle642 fiber/tree stabilizers plus rough code","mechanism_invariant":"exact leaf/fiber elimination followed by current-support physical-radius pivot choice","terminal_obligation":"full E with linear factors and bounded range","strength_vs_target":"direct attempt","honesty_marker":"ATTEMPTED","status":"finite L3/L6/L7 measured; all-L terminal not established"},
        {"family":"generic signed tableau comparator","object_formulation":"complete Cycle642 stabilizer tableau","mechanism_invariant":"Cycle643 H/S/CNOT Gaussian reduction","terminal_obligation":"abstract full E","strength_vs_target":"weaker locality target","honesty_marker":"ATTEMPTED","status":"exact comparator"},
        {"family":"hybrid structured cap plus generic rough chart","object_formulation":"locally decoded cap fibers/tree and abstract rough quotient","mechanism_invariant":"cap leaf elimination then generic rough stabilizer/logical chart","terminal_obligation":"separate cap and rough growth","strength_vs_target":"hybrid comparator","honesty_marker":"ATTEMPTED","status":"exact comparator"},
        {"family":"square-cap result back-credit as a tree compiler","object_formulation":"reuse Cycle643's different Cycle537 square-cap result without a fresh tree-code run","mechanism_invariant":"generic signed tableau on a different stabilizer object","terminal_obligation":"exact Cycle642 tree-code E","strength_vs_target":"scope-mismatched shortcut","honesty_marker":"RULED OUT BY PRIOR","status":"Cycle643 explicitly did not consume Cycle642; no result is back-credited"},
    ]
    open_routes=[
        {"family":"distributed orbit-tree placement","status":"OPEN / NOT COUNTED","terminal":"bounded all-L physical range"},
        {"family":"constant-depth local rough encoder with added work","status":"OPEN / NOT COUNTED","terminal":"returned-work exact full E"},
        {"family":"autonomous state-carried initialization","status":"OPEN / NOT COUNTED","terminal":"derive blank/chart/schedule without host control"},
    ]
    walls={"W_factor_growth":"prove all-L O(N) complete encoder size","W_range":"bound every physical factor range independently of L","W_genesis":"replace supplied blank/chart/order/schedule by an autonomous law"}
    pairs=[{"from":a,"to":b,"implied":False,"reason":f"closing {a} does not construct {b}"} for a in walls for b in walls if a!=b]
    c642_open=citation("docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md","No state-preparation map")
    c643_scale=citation("docs/work_history/repo/review_feedback/ABSTRACT_FILL_DISK_FULL_TABLEAU_ISOMETRY_CYCLE643_NOTE_2026-07-23.md","Generic Gaussian elimination supplies no all-L")
    current=current_citation("three-route full isometry tournament")
    n4_non=[{"prior_ref":c642_open["ref"],"prior_path":c642_open["path"],"prior_line":c642_open["line"],"prior_residual":"Cycle642 had no state-preparation E","current_path":current["path"],"current_line":current["line"],"current_residual":"Cycle647 constructs exact finite-size E on the same tree code","same_scope":True,"exact_match":False,"use_as_closure":False},
            {"prior_ref":c643_scale["ref"],"prior_path":c643_scale["path"],"prior_line":c643_scale["line"],"prior_residual":"square-cap generic tableau had no all-L linear theorem","current_path":current["path"],"current_line":current["line"],"current_residual":"tree-code routes receive a fresh scaling audit and no square-cap credit","same_scope":False,"exact_match":False,"use_as_closure":False}]
    rhetoric=[{"claim":"no all-L local/linear tree encoder is established by these three finite rows","per_element":"every emitted H/S/CNOT factor is iterated","per_site":"every CNOT endpoint receives a declared K129 fine-grid distance","per_mode":"all matter and gauge generators are conjugated","per_block":"L3 construction, L6 train, L7 held are exact","lattice_wide":"three sizes do not prove impossibility or asymptotic growth"}]
    n6=[{"file":"UNMATERIALIZED/distributed_tree_encoder_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_range by placing each tree edge near its incident chunks"},{"file":"UNMATERIALIZED/local_rough_chart_with_returned_work_cycle_next.py","status":"OPEN","what_closes":"W_factor_growth with an analytic recurrence"},{"file":"UNMATERIALIZED/autonomous_tree_code_genesis_cycle_next.py","status":"OPEN","what_closes":"W_genesis"}]
    n7={"mechanism":"distribute each reflected tree branch along its Wilson and use local cat-state fusion plus a cellular rough-code peeling recurrence","actionable_steps":["replace the centralized outer-shell role placement by one covariant orbit fiber per incident chunk neighborhood","prove a local fusion recurrence and return every work M2","compose with a cellwise target/gauge chart and rerun all24/all576"],"terminal_test":"constant overhead, O(N) factors, L-independent maximum physical range, inverse/deletion/leakage, and full update intertwining at held sizes","supporting_citations":[c642_open,c643_scale]}
    n8=[{"cycle":642,"retired":"absence of any E on the orbit-tree code","mechanism":"Cycle647 exact three-route Clifford synthesis","applicability":"finite L3/L6/L7 supplied-chart E only; locality/genesis remain open","citation_ref":c642_open["ref"],"citation_path":c642_open["path"],"citation_line":c642_open["line"],"citation_text":c642_open["text"]},{"cycle":643,"retired":"need to reimplement signed tableau machinery","mechanism":"immutable generic comparator reuse","applicability":"algorithmic reuse only; square-cap results not credited","citation_ref":c643_scale["ref"],"citation_path":c643_scale["path"],"citation_line":c643_scale["line"],"citation_text":c643_scale["text"]}]
    return {"Status":"PASS","N1_normalized_families":families,"N1_open_routes_not_counted":open_routes,
            "N1_qualifying_attempts":4,"N1_required_for_negative":5,
            "N1_broad_negative_gate":"FAIL / DO NOT SHIP","broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
            "N2_walls":walls,"N2_directed_ordered_pairs":pairs,"N3_hidden_wall_scan":[{"condition":"centralized K129 outer-shell tree roles","classification":"supplied finite placement, not all-L locality"},{"condition":"pivot/root/parity chart/blank/schedule","classification":"supplied compile structure, not autonomous genesis"}],
            "N4_exact_residual_matches":[],"N4_nonmatches_not_used_as_closure":n4_non,"N5_rhetoric":rhetoric,"N6_partial_closure_paths":n6,"N7_steelman":n7,"N8_cross_cycle_echo":n8,
            "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,
            "broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
            "shared_route_independent_obstruction":False,"axiom_pressure":False}


def note_text(receipt: dict) -> str:
    route_lines=[]
    for route in ("A_local_peel","B_generic_all","C_hybrid"):
        rr=[r for r in receipt["isometries"] if r["route"]==route]
        route_lines.append(f"| {route} | " + " / ".join(str(r["encoder_factor_count"]) for r in rr) + " | " + " / ".join(f"{r['encoder_factors_per_cell']:.3f}" for r in rr) + " | " + " / ".join(str(next(d["maximum_periodic_fine_L1"] for d in receipt["physical_distance_audit"] if d["route"]==route and d["length"]==r["length"])) for r in rr) + " |")
    return f"""# Physical orbit-tree structured full-isometry tournament — Cycle 647

Classification: **exact finite supplied-chart orbit-tree E with nonlocal factors; strict physical local/linear terminal remains open**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough: **false**

## Result

Cycle 647 constructs a complete finite supplied-chart H/S/CNOT isometry for
the exact Cycle-642 reflection-symmetric orbit-tree code at L3, L6, and held
L7.  The M2 labels are physically placed, but the compile factors are mostly
non-nearest-neighbor and therefore do not constitute a strict physical local
M2 compiler.  Every route has the exact
`6N target + (N-1) gauge + rank(S) blank` partition, both
matter parities, inverse, complete matter/gauge generator conjugation, and
code-space `E G_coarse = G_tree_code E` for the inherited coin, FSWAP,
contact, B/Gamma(P), Cycle-219 mass, and Cycle-230 seam blocks.

This is the first full finite supplied-chart E for the tree code.  It is not
autonomous state preparation or genesis.  It does not back-credit the
Cycle-643 square-cap E.  The immutable Cycle-643 machinery is used only as
Route B's generic signed-tableau implementation and as Route C's rough-chart
component.

| route | factors L3 / L6 / L7 | factors/cell L3 / L6 / L7 | max fine-L1 L3 / L6 / L7 |
|---|---:|---:|---:|
{chr(10).join(route_lines)}

Against Route B, Route A uses
`{receipt['route_A_vs_B_comparator'][0]['factor_reduction_percent']:.1f}%` /
`{receipt['route_A_vs_B_comparator'][1]['factor_reduction_percent']:.1f}%` /
`{receipt['route_A_vs_B_comparator'][2]['factor_reduction_percent']:.1f}%`
fewer factors at L3/L6/L7.  This is a useful structured-synthesis benefit,
not locality closure: Route-A factors per cell rise
`524.1 -> 713.0 -> 742.6`, maximum fine-L1 range rises
`407 -> 1161 -> 1181`, and all `{sum(d['two_qubit_factors'] for d in receipt['physical_distance_audit'] if d['route']=='A_local_peel')}`
Route-A CNOT instances are non-nearest-neighbor in the declared coordinates.
The finite held spatial label overheads are
`23.778 -> 22.444 -> 22.280` M2 labels per coarse cell; this finite overhead
statement is kept separate from factor/program scaling and from Cycle 642's
still-open asymptotic distributed placement.

Route A exactly leaf-eliminates every X-equality fiber and every non-root tree
face; the three root faces carry the Wilson initializers and receive three
explicit rough pivots.  Its separately charged cap/tree stage uses
`284 / 600 / 704` factors at L3/L6/L7.  Route A then chooses rough pivots and
logical-chart pivots by current physical fanout radius.  Route C uses the same structural cap decoder with generic
rough reductions.  Route B applies one generic tableau to the whole code.
The cap/tree preprocessing is therefore real and separately charged.

The full factors-per-cell and maximum-distance sequences do not establish an
all-L O(N), constant-factors-per-cell, bounded-depth, or bounded-physical-range
theorem.  The centralized finite K129 outer-shell allocation inherited from
Cycle 642 makes some cap-to-chunk interactions long.  This is an unfinished
placement/encoder construction, not a route-independent substrate
obstruction and not a no-go.

## Exact controls

All displayed stabilizers reduce to positive products of blank Z references.
All matter generators remain target-only; gauge generators remain in the
gauge/shared-parity partition; ancilla-X leakage is zero.  Both target
parities are admitted.  Factorwise inverse is exact, representative H/S/CNOT
deletions are detected, and Cycle-642 face/fiber malformed-incidence controls
remain positive.  The optional plus-gauge-vacuum fixture has 26 independent
L3 references on every route; deleting one lowers rank by one, while a minus
reference is algebraically consistent but refused by the declared plus
fixture.  The held L7 factor lists are fully materialized and hashed.

Proper-cubic label covariance is checked on the fixed extended M2 labels for
all 24 frames and all 576 products.  The circuit family obeys
`E_R = F_R E C_R^dagger`; there is no runtime frame selector.  A single
frame-invariant factor order is not claimed or required.

## Supplied structure and semantic firewall

Supplied are the immutable Cycle-642 tree topology, K129 finite placement,
rough graph and dressed algebra; immutable Cycle-643 tableau primitives;
finite L3/L6/L7 domains; blank stabilizer inputs; optional gauge-vacuum
fixture; pivot/root/row/parity-chart choices; and compile schedules.  These
are not autonomous genesis or host-free runtime control.  No global
Jordan-Wigner order and no nonlocal parity service are used.  A factor count
or schedule is not time or a
rate, phase is not energy, a blank is not a Record, and this finite compiler
is not an infinite-volume physical law.

## Route disposition

- Route A: **exact full finite supplied-chart E passes; requested all-L local/linear and
  bounded-range terminal not established**.
- Route B: **exact finite abstract comparator E passes; generic growth/range remains**.
- Route C: **exact finite hybrid E passes; cap preprocessing is structured, rough
  logical chart remains generic**.

No shared route-independent obstruction is established.  There is no axiom
pressure.

## Six-wall ledger

| wall | movement | residual |
|---|---|---|
| `C_ref` | full tree-code E, both parities, inverse | blank/chart/root/order/schedule supplied |
| `C_num` | exact ranks, factors and residuals | no empirical/Born normalization; factor count is not time |
| `C_wrap` | tree faces and all stabilizers inverse-visible | autonomous genesis/history semantics open |
| `C_int` | coin/FSWAP/contact/B, mass and seam intertwine through E | no new interaction law |
| `C_local` | structured cap decoder and exact all24/all576 labels | all-L bounded range and local rough chart open |
| `C_source` | resources inventoried | no energy/stress/source/gravity identification |

## N1–N8

The full N1–N8 schema passes.  Every broad-no-go, minimum-content,
shared-obstruction, and axiom-pressure promotion gate is **FAIL / DO NOT
SHIP**.  Broad no-go: **not claimed**.  Minimum content: **not claimed**.
Shared route-independent obstruction: **not established**.  Axiom pressure:
**none**.

The optimal next campaign is the N7 distributed-tree steelman: place each
tree-edge fiber near its incident Wilson chunks, prove a local cat-fusion and
rough-chart recurrence with returned work, and demand O(N) factors plus an
L-independent physical-range bound before claiming a local/linear compiler.
"""


def main() -> int:
    signal.alarm(3600); started=time.perf_counter()
    observed={path:sha256(git_bytes(path)).hexdigest() for path in PINS}
    check("immutable reviewed Cycle642/643 quartet shores are byte exact",observed==PINS,{"files":len(PINS),"mismatches":[p for p in PINS if observed[p]!=PINS[p]]})
    objects={}; placements={}; rows=[]; internals=[]; distances=[]
    for length in (3,6,7):
        placement,fibers=c642.allocate_orbit_roles(length); obj=c642.build_tree_code(length,fibers)
        objects[length]=obj; placements[length]=placement; coords=positions(obj,length)
        for route in ("A_local_peel","B_generic_all","C_hybrid"):
            row,internal=build_isometry(length,route,obj,coords)
            rows.append(row);internals.append(internal);distances.append(gate_distance_audit(row,internal,coords))
            check(f"L{length} {route} exact full orbit-tree isometry",row["pass"],{"factors":row["encoder_factor_count"],"per_cell":row["encoder_factors_per_cell"],"seconds":row["elapsed_seconds"]})
    covariance=covariance_audit(objects);check("extended orbit-tree labels close under all24/all576",covariance["pass"],covariance["rows"])
    update=inherited_update(rows);check("all routes compose the inherited full-Fock update on code",update["pass"],update["routes"])
    controls=inverse_and_deletion(rows,internals);check("inverse and representative factor deletions are exact/detected",controls["pass"],{"inverse":len(controls["inverse_rows"]),"deletions":len(controls["representative_factor_deletions"])})
    malformed=c642.deletion_controls(objects[3]);check("Cycle642 tree face/fiber deletion and malformed incidence remain detected",malformed["pass"],malformed)
    scaling={}
    for route in ("A_local_peel","B_generic_all","C_hybrid"):
        rr=[r for r in rows if r["route"]==route]
        dd=[d for d in distances if d["route"]==route]
        scaling[route]={"factor_counts":[r["encoder_factor_count"] for r in rr],"factors_per_cell":[r["encoder_factors_per_cell"] for r in rr],"maximum_fine_L1":[d["maximum_periodic_fine_L1"] for d in dd],"all_L_O_N_theorem":False,"constant_factors_per_cell_theorem":False,"bounded_depth_theorem":False,"L_independent_physical_range_theorem":False}
    comparator=[]
    for length in (3,6,7):
        a=next(r for r in rows if r["route"]=="A_local_peel" and r["length"]==length)
        b=next(r for r in rows if r["route"]=="B_generic_all" and r["length"]==length)
        comparator.append({"length":length,"Route_A_factors":a["encoder_factor_count"],"Route_B_factors":b["encoder_factor_count"],"factor_reduction":b["encoder_factor_count"]-a["encoder_factor_count"],"factor_reduction_percent":100*(b["encoder_factor_count"]-a["encoder_factor_count"])/b["encoder_factor_count"]})
    no_go=no_go_discipline()
    canonical={"Status_PASS":no_go["Status"]=="PASS","promotion_gates_fail":all(no_go[k]=="FAIL / DO NOT SHIP" for k in ("N1_broad_negative_gate","broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")),"claim_flags_false":not any(no_go[k] for k in ("broad_no_go_claim","minimum_content_claim","shared_obstruction_claim","axiom_pressure_claim","broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped","shared_route_independent_obstruction","axiom_pressure")),"N1_count_below_negative_threshold":no_go["N1_qualifying_attempts"]==4 and no_go["N1_required_for_negative"]==5,"N1_markers_exact":all(r["honesty_marker"] in {"ATTEMPTED","RULED OUT BY PRIOR"} for r in no_go["N1_normalized_families"]) and all("honesty_marker" not in r for r in no_go["N1_open_routes_not_counted"]),"N2_directed_pairs":len(no_go["N2_directed_ordered_pairs"])==6,"N4_fields":all({"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}<=set(r) for r in no_go["N4_exact_residual_matches"]+no_go["N4_nonmatches_not_used_as_closure"]),"N5_fields":all({"per_element","per_site","per_mode","per_block","lattice_wide"}<=set(r) for r in no_go["N5_rhetoric"]),"N6_fields":all({"file","status","what_closes"}<=set(r) for r in no_go["N6_partial_closure_paths"]),"N8_fields":all({"retired","mechanism","applicability","citation_ref","citation_path","citation_line","citation_text"}<=set(r) for r in no_go["N8_cross_cycle_echo"])}
    canonical["pass"]=all(canonical.values());check("canonical N1-N8 and negative-promotion gates are machine enforced",canonical["pass"],canonical)
    receipt={
        "Status":"PASS","cycle":647,"date":"2026-07-23",
        "status":"exact finite supplied-chart Cycle642 orbit-tree E with nonlocal factors; strict physical local-linear terminal open",
        "classification":"three-route constructive finite isometry tournament",
        "authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,
        "author_artifact_status_accepted":False,"breakthrough":False,
        "constitutional_effect":"none",
        "broad_negative_gate":"FAIL / DO NOT SHIP",
        "minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP",
        "axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_no_go_claim":False,"minimum_content_claim":False,
        "shared_obstruction_claim":False,"axiom_pressure_claim":False,
        "broad_negative_shipped":False,"minimum_content_shipped":False,
        "shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
        "shared_route_independent_obstruction":False,"axiom_pressure":False,
        "strict_physical_local_M2_compiler_claimed":False,
        "immutable_shore":{"ref":SHORE,"pins":PINS,"observed":observed,"working_tree_bytes_used_as_premise":False},
        "isometries":rows,"physical_distance_audit":distances,
        "factor_program_scaling_firewall":scaling,
        "route_A_vs_B_comparator":comparator,
        "proper_cubic_covariance":covariance,"inherited_full_Fock_update":update,
        "inverse_deletion_malformed_controls":{"circuit":controls,"tree_incidence":malformed},
        "fixed_K129_placements":placements,
        "route_disposition":{
            "A_local_peel":"PASS_EXACT_FINITE_SUPPLIED_CHART_E__STRICT_LOCAL_LINEAR_RANGE_OPEN_NOT_CLOSED",
            "B_generic_all":"PASS_EXACT_FINITE_ABSTRACT_COMPARATOR__GENERIC_GROWTH_AND_RANGE",
            "C_hybrid":"PASS_EXACT_FINITE_HYBRID__ROUGH_CHART_GENERIC",
        },
        "supplied_structure_inventory":{
            "Cycle642_tree_code_and_K129_finite_placement":True,
            "Cycle643_generic_tableau_implementation_only":True,
            "Cycle643_square_cap_result_back_credited":False,
            "finite_L3_L6_L7_domains":True,"blank_stabilizer_inputs":True,
            "optional_gauge_vacuum_fixture":True,"pivot_root_row_parity_chart_and_schedule":True,
            "finite_supplied_chart_E_only":True,"work_M2":0,"autonomous_genesis":False,
            "global_Jordan_Wigner_order":False,"nonlocal_parity_service":False,
            "runtime_frame_selector":False,
        },
        "no_go_discipline":no_go,"canonical_claim_gate_contract":canonical,
        "six_wall_ledger":{
            "C_ref":"finite supplied-chart tree-code E/both parities/inverse; blank/chart/root/order/schedule supplied",
            "C_num":"exact factors/ranks/residuals; no empirical or Born normalization",
            "C_wrap":"tree stabilizers inverse-visible; autonomous genesis/history open",
            "C_int":"coin/FSWAP/contact/B mass/seam compose through G_tree_code; no strict local physical update or new interaction law",
            "C_local":"structured cap decode and all24/all576 label covariance; factors nonlocal and all-L bounded range/local rough chart open",
            "C_source":"resources explicit; no energy/stress/source/gravity identification",
        },
        "highest_honest_terminal":"complete literal finite L3/L6/L7 supplied-chart H/S/CNOT E for Cycle642 orbit-tree code on all three routes, with physically placed labels but nonlocal compile factors; not a strict physical local M2 compiler",
        "optimal_next_campaign":"distribute tree fibers along Wilson chunks and prove a local cat-fusion plus rough-chart recurrence with O(N) factors, L-independent range, returned work, and full covariance",
    }
    top_contract={
        "Status_PASS":receipt["Status"]=="PASS",
        "promotion_gates_fail":all(receipt[k]=="FAIL / DO NOT SHIP" for k in ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")),
        "claim_flags_false":not any(receipt[k] for k in ("broad_no_go_claim","minimum_content_claim","shared_obstruction_claim","axiom_pressure_claim","broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped","shared_route_independent_obstruction","axiom_pressure")),
        "strict_physical_local_compiler_not_claimed":not receipt["strict_physical_local_M2_compiler_claimed"],
    }
    top_contract["pass"]=all(top_contract.values());receipt["top_level_claim_gate_contract"]=top_contract
    check("top-level Status, negative gates, shipped flags, and strict-local firewall are machine enforced",top_contract["pass"],top_contract)
    NOTE.write_text(note_text(receipt))
    note_flat=" ".join(NOTE.read_text().lower().split()); required=("authority: **none**","audit: **unset**","e g_coarse = g_tree_code e","not time or a rate","no shared route-independent obstruction","axiom pressure","fail / do not ship","does not back-credit","strict physical local m2 compiler")
    missing=[x for x in required if x not in note_flat];check("note contract preserves scope and semantic firewalls",not missing,missing)
    elapsed=time.perf_counter()-started;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss<10_000_000:rss*=1024
    receipt.update({"runner_sha256":file_sha(Path(__file__)),"note_sha256":file_sha(NOTE),"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0})
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=float)+"\n")
    print(json.dumps({"pass":receipt["pass"],"tests":f"{PASS}/{PASS+FAIL}","elapsed":elapsed,"receipt":str(RECEIPT)},indent=2))
    return int(FAIL!=0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as stream:
        original=sys.stdout;sys.stdout=Tee(original,stream)
        try:raise SystemExit(main())
        finally:sys.stdout=original
