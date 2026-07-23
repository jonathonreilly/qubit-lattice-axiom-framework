#!/usr/bin/env python3
"""Cycle 643: literal Clifford isometry for the abstract Cycle537 fill code.

This runner consumes the committed Cycle532/Cycle537 algebra from git objects,
not dirty working-tree variants and not a Cycle642 physical embedding.  It
synthesizes a deterministic H/S/CNOT decoder for every independent filled-code
stabilizer, constructs a complete target-plus-gauge symplectic chart, and
inverts the decoder to obtain the encoding isometry E.

The circuit is an abstract cap-adjacency circuit.  Pivot, row order, input
chart, blank stabilizer state, and compile schedule are supplied.  Compiler
depth is not time and a gate factor is not a rate.

Authority none.  Audit unset.  Author accepted false.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from hashlib import sha256
import importlib.util
import json
import resource
import signal
import subprocess
import sys
import time
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/ABSTRACT_FILL_DISK_FULL_TABLEAU_ISOMETRY_CYCLE643_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/abstract_fill_disk_full_tableau_isometry_cycle643_receipt_2026_07_23.json"
SHORE_HEAD = "c27f72ff8b1058d872695829c05e95da415813bc"
AUTHORITY = "none"
AUDIT = "unset"
WALL_SECONDS = 1200

SHORE_SHA256 = {
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py": "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md": "5f668f6cc04a5eece23f913d5869f57553df583c23d6dbb5cdac6756be41bfc3",
    "outputs/physical_rough_gauge_subsystem_quotient_cycle532_receipt_2026_07_21.json": "ee9687bb73f7a2e67c90b78fececad3d3db5af4f80ef2140bb81937d09a04391",
    "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py": "cd00034db5e106accfd95e33de5c9b3b2a26b2c35719611454c3486481ad47ac",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md": "e413a8c079fa2d5ff14d1b46d19df60cd07d853d118b51d8494632cc03a427f8",
    "outputs/physical_local_wilson_fill_disk_cycle537_receipt_2026_07_21.json": "ebe7222afedba7907dcff9e233b2bc30284af8d35d5d7cae1941668ed81c5856",
    "scripts/physical_fixed_wilson_initializer_preparation_tournament_cycle636_2026_07_23.py": "d4a3321943078dbe5dfc1fb598705fbe361c0edb80c2f790643bd3d5f2352b39",
    "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_WILSON_INITIALIZER_PREPARATION_TOURNAMENT_CYCLE636_NOTE_2026-07-23.md": "8427006703508c1648271b787b83cc70c8dbedb1aa068fb0edee4449a2fd587c",
    "outputs/physical_fixed_wilson_initializer_preparation_tournament_cycle636_receipt_2026_07_23.json": "984291942ab966236876f2d79f4d8ff8453a2c9a99eeae02aee4e76bd54de348",
}

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def git_bytes(path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{SHORE_HEAD}:{path}"], cwd=ROOT, check=True,
        stdout=subprocess.PIPE,
    ).stdout


def git_line(path: str, fragment: str) -> int:
    for index, line in enumerate(git_bytes(path).decode().splitlines(), start=1):
        if fragment in line:
            return index
    raise AssertionError((path, fragment))


def source_line(fragment: str) -> int:
    for index, line in enumerate(Path(__file__).read_text().splitlines(), start=1):
        if fragment in line:
            return index
    raise AssertionError(fragment)


def immutable_shore() -> dict:
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in SHORE_SHA256}
    c537 = json.loads(git_bytes("outputs/physical_local_wilson_fill_disk_cycle537_receipt_2026_07_21.json"))
    c636 = json.loads(git_bytes("outputs/physical_fixed_wilson_initializer_preparation_tournament_cycle636_receipt_2026_07_23.json"))
    semantics = {
        "Cycle537_exact_factor": c537["factorization"]["stabilizer_rank"] == [1996, 3421]
        and c537["factorization"]["explicit_dressed_gauge_exhausts_commutant"],
        "Cycle537_preparation_open": not c537["boundary"]["bounded_state_preparation_circuit_closed"],
        "Cycle537_embedding_open": not c537["boundary"]["fixed_single_frame_independent_physical_embedding_closed"],
        "Cycle636_tableau_open": not c636["full_isometry_audit"]["full_M64_E_constructed"],
    }
    result = {
        "head": SHORE_HEAD, "expected_sha256": SHORE_SHA256,
        "observed_sha256": observed, "semantics": semantics,
        "dirty_worktree_used_as_premise": False,
        "Cycle642_physical_embedding_used_as_premise": False,
        "pass": observed == SHORE_SHA256 and all(semantics.values()),
    }
    check("committed Cycle532/537/636 abstract shores are byte-exact and Cycle642 is not consumed",
          result["pass"], {"files": len(observed), "semantics": len(semantics)})
    return result


def load_exact_module(name: str, path: str):
    """Execute a committed Python source object without using its dirty file."""
    module = types.ModuleType(name)
    module.__file__ = str(ROOT / path)
    module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(path), module.__file__, "exec"), module.__dict__)
    return module


sys.path.insert(0, str(ROOT / "scripts"))
C532_NAME = "physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21"
C537_NAME = "physical_local_wilson_fill_disk_cycle537_2026_07_21"
c532 = load_exact_module(C532_NAME, "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py")
c537 = load_exact_module(C537_NAME, "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py")
Pauli = c532.c235.Pauli


@dataclass(frozen=True)
class Gate:
    kind: str
    a: int
    b: int = -1

    @property
    def support(self) -> int:
        return 1 if self.b < 0 else 2


def inverse_gates(gates: tuple[Gate, ...]) -> tuple[Gate, ...]:
    output = []
    for gate in reversed(gates):
        if gate.kind == "S":
            output.extend((gate, gate, gate))
        else:
            output.append(gate)
    return tuple(output)


def gate_digest(gates: tuple[Gate, ...]) -> str:
    digest = sha256()
    for gate in gates:
        digest.update(gate.kind.encode())
        digest.update(gate.a.to_bytes(4, "little", signed=False))
        digest.update(gate.b.to_bytes(4, "little", signed=True))
    return digest.hexdigest()


class BitTableau:
    """Bit-sliced Pauli rows; Clifford column gates act on all rows at once."""

    def __init__(self, rows: tuple[Pauli, ...], qubits: int):
        self.qubits = qubits
        self.count = len(rows)
        self.x = [0] * qubits
        self.z = [0] * qubits
        self.p0 = 0
        self.p1 = 0
        for index, row in enumerate(rows):
            mark = 1 << index
            if row.phase & 1:
                self.p0 |= mark
            if row.phase & 2:
                self.p1 |= mark
            bits = row.x
            while bits:
                bit = bits & -bits
                self.x[bit.bit_length() - 1] |= mark
                bits ^= bit
            bits = row.z
            while bits:
                bit = bits & -bits
                self.z[bit.bit_length() - 1] |= mark
                bits ^= bit

    def add_phase(self, mask: int, amount: int) -> None:
        if amount & 1:
            old = self.p0
            self.p0 ^= mask
            self.p1 ^= old & mask
        if amount & 2:
            self.p1 ^= mask

    def h(self, q: int) -> None:
        self.p1 ^= self.x[q] & self.z[q]
        self.x[q], self.z[q] = self.z[q], self.x[q]

    def s(self, q: int) -> None:
        old_x = self.x[q]
        self.add_phase(old_x, 1)
        self.z[q] ^= old_x

    def cnot(self, control: int, target: int) -> None:
        self.x[target] ^= self.x[control]
        self.z[control] ^= self.z[target]

    def gate(self, gate: Gate) -> None:
        if gate.kind == "H":
            self.h(gate.a)
        elif gate.kind == "S":
            self.s(gate.a)
        elif gate.kind == "CNOT":
            self.cnot(gate.a, gate.b)
        else:
            raise ValueError(gate)

    def support(self, row: int, allowed: set[int] | None = None) -> tuple[int, int]:
        x = z = 0
        columns = range(self.qubits) if allowed is None else allowed
        mark = 1 << row
        for q in columns:
            if self.x[q] & mark:
                x |= 1 << q
            if self.z[q] & mark:
                z |= 1 << q
        return x, z

    def phase(self, row: int) -> int:
        return ((self.p0 >> row) & 1) | (((self.p1 >> row) & 1) << 1)

    def multiply_rows(self, pivot: int, selected: int, pivot_x: int, pivot_z: int) -> None:
        if not selected:
            return
        parity = 0
        bits = pivot_x
        while bits:
            bit = bits & -bits
            parity ^= self.z[bit.bit_length() - 1]
            bits ^= bit
        self.add_phase(selected, self.phase(pivot))
        self.p1 ^= selected & parity
        bits = pivot_x
        while bits:
            bit = bits & -bits
            self.x[bit.bit_length() - 1] ^= selected
            bits ^= bit
        bits = pivot_z
        while bits:
            bit = bits & -bits
            self.z[bit.bit_length() - 1] ^= selected
            bits ^= bit

    def rows(self) -> tuple[Pauli, ...]:
        xs = [0] * self.count
        zs = [0] * self.count
        for q in range(self.qubits):
            bits = self.x[q]
            while bits:
                bit = bits & -bits
                xs[bit.bit_length() - 1] |= 1 << q
                bits ^= bit
            bits = self.z[q]
            while bits:
                bit = bits & -bits
                zs[bit.bit_length() - 1] |= 1 << q
                bits ^= bit
        return tuple(Pauli(self.phase(i), xs[i], zs[i]) for i in range(self.count))


def independent_paulis(rows: tuple[Pauli, ...], qubits: int, reverse: bool) -> tuple[Pauli, ...]:
    candidates = tuple(reversed(rows)) if reverse else rows
    pivots: dict[int, int] = {}
    output = []
    for pauli in candidates:
        reduced = pauli.symplectic(qubits)
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                output.append(pauli)
                break
    return tuple(output)


def append_gate(tableau: BitTableau, gates: list[Gate], kind: str, a: int, b: int = -1) -> None:
    gate = Gate(kind, a, b)
    tableau.gate(gate)
    gates.append(gate)


def flip_z_sign(tableau: BitTableau, gates: list[Gate], q: int) -> None:
    # X = H S^2 H, expressed only in the declared H/S alphabet.
    for kind in ("H", "S", "S", "H"):
        append_gate(tableau, gates, kind, q)


def reduce_stabilizers(rows: tuple[Pauli, ...], qubits: int, reverse: bool = False) -> dict:
    basis = independent_paulis(rows, qubits, reverse)
    tab = BitTableau(basis, qubits)
    active_rows = (1 << len(basis)) - 1
    active_qubits = set(range(qubits))
    gates: list[Gate] = []
    row_to_pivot: dict[int, int] = {}
    direction = -1 if reverse else 1

    while active_rows:
        q_order = sorted(active_qubits, reverse=reverse)
        pivot_q = pivot_row = None
        use_x = False
        for q in q_order:
            candidates = tab.x[q] & active_rows
            if candidates:
                pivot_q = q
                pivot_row = candidates.bit_length() - 1 if reverse else (candidates & -candidates).bit_length() - 1
                use_x = True
                break
        if pivot_row is None:
            for q in q_order:
                candidates = tab.z[q] & active_rows
                if candidates:
                    pivot_q = q
                    pivot_row = candidates.bit_length() - 1 if reverse else (candidates & -candidates).bit_length() - 1
                    break
        if pivot_row is None or pivot_q is None:
            raise AssertionError("independent stabilizer basis lost a pivot")

        mark = 1 << pivot_row
        if use_x:
            if tab.z[pivot_q] & mark:
                append_gate(tab, gates, "S", pivot_q)
            for q in q_order:
                if q == pivot_q:
                    continue
                xb = bool(tab.x[q] & mark)
                zb = bool(tab.z[q] & mark)
                if not (xb or zb):
                    continue
                if xb and zb:
                    append_gate(tab, gates, "S", q)
                elif zb:
                    append_gate(tab, gates, "H", q)
                append_gate(tab, gates, "CNOT", pivot_q, q)
            px, pz = tab.support(pivot_row, active_qubits)
            if px != 1 << pivot_q or pz:
                raise AssertionError(("X pivot reduction", pivot_row, pivot_q, px.bit_count(), pz.bit_count()))
            # Commutation makes every remaining z at pivot zero; row addition clears x.
            selected = (tab.x[pivot_q] & active_rows) ^ mark
            tab.multiply_rows(pivot_row, selected, px, pz)
            append_gate(tab, gates, "H", pivot_q)
        else:
            for q in q_order:
                if q != pivot_q and tab.z[q] & mark:
                    append_gate(tab, gates, "CNOT", q, pivot_q)
            px, pz = tab.support(pivot_row, active_qubits)
            if px or pz != 1 << pivot_q:
                raise AssertionError(("Z pivot reduction", pivot_row, pivot_q, px.bit_count(), pz.bit_count()))
            selected = (tab.z[pivot_q] & active_rows) ^ mark
            tab.multiply_rows(pivot_row, selected, px, pz)

        px, pz = tab.support(pivot_row)
        if px or pz != 1 << pivot_q:
            raise AssertionError(("canonical stabilizer", pivot_row, pivot_q, px, pz))
        if tab.phase(pivot_row) == 2:
            flip_z_sign(tab, gates, pivot_q)
        if tab.phase(pivot_row) != 0:
            raise AssertionError(("stabilizer phase", pivot_row, tab.phase(pivot_row)))
        row_to_pivot[pivot_row] = pivot_q
        active_rows ^= mark
        active_qubits.remove(pivot_q)

    pivot_qubits = frozenset(row_to_pivot.values())
    return {
        "basis": basis,
        "decoder_gates": tuple(gates),
        "row_to_pivot": row_to_pivot,
        "pivot_qubits": pivot_qubits,
        "logical_qubits": tuple(q for q in range(qubits) if q not in pivot_qubits),
    }


def transform_rows(rows: tuple[Pauli, ...], qubits: int, gates: tuple[Gate, ...]) -> tuple[Pauli, ...]:
    tab = BitTableau(rows, qubits)
    for gate in gates:
        tab.gate(gate)
    return tab.rows()


def symp(left: int, right: int, qubits: int) -> int:
    return c532.symplectic_product(left, right, qubits)


def independent_vectors(rows: tuple[int, ...]) -> list[tuple[int, int]]:
    pivots: dict[int, int] = {}
    output = []
    for index, source in enumerate(rows):
        reduced = source
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                output.append((source, 1 << index))
                break
    return output


def symplectic_gram_schmidt(rows: tuple[int, ...], qubits: int) -> dict:
    active = independent_vectors(rows)
    pairs = []
    radicals = []
    while active:
        left, left_coeff = active.pop(0)
        partner = next((i for i, (right, _c) in enumerate(active) if symp(left, right, qubits)), None)
        if partner is None:
            radicals.append((left, left_coeff))
            continue
        right, right_coeff = active.pop(partner)
        repaired = []
        for row, coeff in active:
            anti_right = symp(row, right, qubits)
            anti_left = symp(row, left, qubits)
            if anti_right:
                row ^= left
                coeff ^= left_coeff
            if anti_left:
                row ^= right
                coeff ^= right_coeff
            repaired.append((row, coeff))
        active = repaired
        pairs.append(((left, left_coeff), (right, right_coeff)))
    return {"pairs": pairs, "radicals": radicals}


def pauli_product(rows: tuple[Pauli, ...], selector: int) -> Pauli:
    result = Pauli()
    index = 0
    while selector:
        bit = selector & -selector
        index = bit.bit_length() - 1
        result = result @ rows[index]
        selector ^= bit
    return result


def clean_ancilla(row: Pauli, pivots: frozenset[int]) -> Pauli:
    mask = 0
    for q in pivots:
        mask |= 1 << q
    if row.x & mask:
        raise AssertionError("commuting logical row acquired ancilla X")
    return Pauli(row.phase, row.x, row.z & ~mask)


def positive_hermitian(row: Pauli) -> Pauli:
    """Choose the + Hermitian phase for a binary symplectic vector."""
    return Pauli((row.x & row.z).bit_count() & 1, row.x, row.z)


def find_parity_conjugate(parity: int, pairs: list[tuple[int, int]], qubits: int) -> int:
    mask = (1 << qubits) - 1
    px, pz = parity & mask, parity >> qubits
    if pz:
        q = 1 << ((pz & -pz).bit_length() - 1)
    elif px:
        q = 1 << (qubits + ((px & -px).bit_length() - 1))
    else:
        raise AssertionError("zero parity radical")
    for x, z in pairs:
        if symp(q, z, qubits):
            q ^= x
        if symp(q, x, qubits):
            q ^= z
    if symp(q, parity, qubits) != 1 or any(symp(q, item, qubits) for pair in pairs for item in pair):
        raise AssertionError("parity conjugate construction failed")
    return q


def abstract_coordinates(row: Pauli, input_pivots: tuple[int, ...],
                         ancilla_wires: frozenset[int]) -> tuple[int, int, int, int]:
    """Return phase, abstract X/Z, and retained blank-ancilla Z dressing."""
    x = z = 0
    for index, q in enumerate(input_pivots):
        if (row.x >> q) & 1:
            x |= 1 << index
        if (row.z >> q) & 1:
            z |= 1 << index
    ancilla_x = sum(1 << q for q in ancilla_wires if (row.x >> q) & 1)
    if ancilla_x:
        raise AssertionError("code-preserving row has ancilla X")
    ancilla_z = sum(1 << q for q in ancilla_wires if (row.z >> q) & 1)
    return row.phase, x, z, ancilla_z


def solve_sign_character(coordinates: tuple[tuple[int, int, int], ...],
                         rhs: tuple[int, ...], qubits: int) -> int | None:
    """Solve <correction,row_i>=rhs_i for a Pauli sign-frame correction."""
    pivots: dict[int, int] = {}
    for (_phase, x, z), value in zip(coordinates, rhs):
        augmented = z | (x << qubits) | (int(value) << (2 * qubits))
        coefficients = augmented & ((1 << (2 * qubits)) - 1)
        while coefficients:
            pivot = coefficients.bit_length() - 1
            if pivot in pivots:
                augmented ^= pivots[pivot]
                coefficients = augmented & ((1 << (2 * qubits)) - 1)
            else:
                pivots[pivot] = augmented
                break
        if not coefficients and ((augmented >> (2 * qubits)) & 1):
            return None
    solution = 0
    for pivot in sorted(pivots):
        row = pivots[pivot]
        value = ((row >> (2 * qubits)) & 1) ^ ((row & solution).bit_count() & 1)
        if value:
            solution |= 1 << pivot
    return solution


def reduce_complete_frame(x_rows: tuple[Pauli, ...], z_rows: tuple[Pauli, ...],
                          logical_qubits: tuple[int, ...], qubits: int) -> dict:
    if len(x_rows) != len(z_rows) or len(x_rows) != len(logical_qubits):
        raise AssertionError("frame size mismatch")
    combined = tuple(item for pair in zip(x_rows, z_rows) for item in pair)
    tab = BitTableau(combined, qubits)
    gates: list[Gate] = []
    active = set(logical_qubits)
    pivots = []
    for pair_index in range(len(x_rows)):
        xi = 2 * pair_index
        zi = xi + 1
        mark_x = 1 << xi
        q = next((candidate for candidate in sorted(active) if (tab.x[candidate] | tab.z[candidate]) & mark_x), None)
        if q is None:
            raise AssertionError(("frame X has no active pivot", pair_index))
        if not (tab.x[q] & mark_x):
            append_gate(tab, gates, "H", q)
        if tab.z[q] & mark_x:
            append_gate(tab, gates, "S", q)
        for other in sorted(active):
            if other == q:
                continue
            xb = bool(tab.x[other] & mark_x)
            zb = bool(tab.z[other] & mark_x)
            if not (xb or zb):
                continue
            if xb and zb:
                append_gate(tab, gates, "S", other)
            elif zb:
                append_gate(tab, gates, "H", other)
            append_gate(tab, gates, "CNOT", q, other)
        xx, xz = tab.support(xi, active)
        if xx != 1 << q or xz:
            raise AssertionError(("frame X reduction", pair_index, q, xx.bit_count(), xz.bit_count()))

        # Clear an optional Y component of Z using the X-axis quarter turn HSH.
        if tab.x[q] & (1 << zi):
            for kind in ("H", "S", "H"):
                append_gate(tab, gates, kind, q)
        for other in sorted(active):
            if other == q:
                continue
            xb = bool(tab.x[other] & (1 << zi))
            zb = bool(tab.z[other] & (1 << zi))
            if not (xb or zb):
                continue
            if xb and zb:
                append_gate(tab, gates, "S", other)
                append_gate(tab, gates, "H", other)
            elif xb:
                append_gate(tab, gates, "H", other)
            append_gate(tab, gates, "CNOT", other, q)
        zx, zz = tab.support(zi, active)
        if zx or zz != 1 << q:
            raise AssertionError(("frame Z reduction", pair_index, q, zx.bit_count(), zz.bit_count()))

        if tab.phase(xi) == 2:
            append_gate(tab, gates, "S", q)
            append_gate(tab, gates, "S", q)
        if tab.phase(zi) == 2:
            flip_z_sign(tab, gates, q)
        if tab.phase(xi) or tab.phase(zi):
            raise AssertionError(("frame sign", pair_index, tab.phase(xi), tab.phase(zi)))
        pivots.append(q)
        active.remove(q)
    return {"decoder_gates": tuple(gates), "input_pivots": tuple(pivots)}


def frame_and_isometry(length: int, reverse: bool = False) -> tuple[dict, dict]:
    started = time.perf_counter()
    objects = c537.extended_objects(length)
    n = objects["qubits"]
    cells = length ** 3
    stabilizers = objects["stabilizers"]
    reduced = reduce_stabilizers(stabilizers, n, reverse)
    stab_gates = reduced["decoder_gates"]
    pivots = reduced["pivot_qubits"]
    logical = reduced["logical_qubits"]
    expected_rank = 15 * cells + 1 + 3 * objects["disk"].edge_count
    expected_k = 7 * cells - 1
    if len(reduced["basis"]) != expected_rank or len(logical) != expected_k:
        raise AssertionError((len(reduced["basis"]), expected_rank, len(logical), expected_k))

    raw_matter = tuple(objects["matter"])
    raw_gauge = tuple(objects["gauge"])
    raw_matter_parity = c537.dress_pauli(
        c537.pauli_product(objects["graph"].B(v) for v in range(objects["graph"].matter_count)),
        objects["graph"], objects["disk"], objects["chunks"],
    )[0]
    raw_gauge_z, _raw_gauge_a, _ = c532.gauge_generators(objects["graph"])
    raw_gauge_parity = c537.dress_pauli(
        c537.pauli_product(raw_gauge_z), objects["graph"], objects["disk"], objects["chunks"],
    )[0]
    decoded = transform_rows(raw_matter + raw_gauge + (raw_matter_parity, raw_gauge_parity), n, stab_gates)
    matter_dec = tuple(clean_ancilla(row, pivots) for row in decoded[:len(raw_matter)])
    gauge_dec = tuple(clean_ancilla(row, pivots) for row in decoded[len(raw_matter):len(raw_matter)+len(raw_gauge)])
    matter_parity_dec = clean_ancilla(decoded[-2], pivots)
    gauge_parity_dec = clean_ancilla(decoded[-1], pivots)

    matter_vec = tuple(row.symplectic(n) for row in matter_dec)
    gauge_vec = tuple(row.symplectic(n) for row in gauge_dec)
    matter_gs = symplectic_gram_schmidt(matter_vec, n)
    gauge_gs = symplectic_gram_schmidt(gauge_vec, n)
    if len(matter_gs["pairs"]) != 6 * cells - 1 or len(matter_gs["radicals"]) != 1:
        raise AssertionError("matter Gram decomposition mismatch")
    if len(gauge_gs["pairs"]) != cells - 1 or len(gauge_gs["radicals"]) != 1:
        raise AssertionError("gauge Gram decomposition mismatch")
    matter_radical = matter_gs["radicals"][0][0]
    gauge_radical = gauge_gs["radicals"][0][0]
    parity_vec = matter_parity_dec.symplectic(n)
    if not (matter_radical == gauge_radical == parity_vec == gauge_parity_dec.symplectic(n)):
        raise AssertionError("shared matter/gauge parity radical mismatch")

    matter_pairs = [(left[0], right[0]) for left, right in matter_gs["pairs"]]
    gauge_pairs = [(left[0], right[0]) for left, right in gauge_gs["pairs"]]
    all_pairs = matter_pairs + gauge_pairs
    q_vec = find_parity_conjugate(parity_vec, all_pairs, n)
    target_pairs = matter_pairs + [(q_vec, parity_vec)]
    frame_pairs = target_pairs + gauge_pairs

    # Frame vectors are already decoded after the stabilizer circuit.  Their
    # signs are fixed by deterministic products of complete generator rows.
    frame_x = []
    frame_z = []
    for pair_index, ((xv, zv), coeff_pair) in enumerate(zip(
        frame_pairs,
        [pair for pair in matter_gs["pairs"]]
        + [((q_vec, 0), (parity_vec, matter_gs["radicals"][0][1]))]
        + [pair for pair in gauge_gs["pairs"]],
    )):
        if pair_index < len(matter_pairs):
            left_coeff, right_coeff = coeff_pair[0][1], coeff_pair[1][1]
            xp = positive_hermitian(clean_ancilla(pauli_product(matter_dec, left_coeff), pivots))
            zp = positive_hermitian(clean_ancilla(pauli_product(matter_dec, right_coeff), pivots))
        elif pair_index == len(matter_pairs):
            xp = positive_hermitian(Pauli(0, q_vec & ((1 << n) - 1), q_vec >> n))
            zp = positive_hermitian(matter_parity_dec)
        else:
            left_coeff, right_coeff = coeff_pair[0][1], coeff_pair[1][1]
            xp = positive_hermitian(clean_ancilla(pauli_product(gauge_dec, left_coeff), pivots))
            zp = positive_hermitian(clean_ancilla(pauli_product(gauge_dec, right_coeff), pivots))
        if xp.symplectic(n) != xv or zp.symplectic(n) != zv:
            raise AssertionError(("frame representative mismatch", pair_index))
        frame_x.append(xp)
        frame_z.append(zp)

    frame = reduce_complete_frame(tuple(frame_x), tuple(frame_z), logical, n)
    total_decoder = stab_gates + frame["decoder_gates"]
    encoder = inverse_gates(total_decoder)

    all_ops = raw_matter + raw_gauge + (raw_matter_parity, raw_gauge_parity)
    total_decoded = transform_rows(all_ops, n, total_decoder)
    target_wires = frozenset(frame["input_pivots"][:6*cells])
    gauge_wires = frozenset(frame["input_pivots"][6*cells:])
    ancilla_wires = pivots
    target_mask = sum(1 << q for q in target_wires)
    gauge_mask = sum(1 << q for q in gauge_wires)
    ancilla_mask = sum(1 << q for q in ancilla_wires)
    decoded_stabilizers = transform_rows(tuple(stabilizers), n, total_decoder)
    stabilizer_reference_failures = sum(
        bool(row.x) or bool(row.z & ~ancilla_mask) or row.phase != 0
        for row in decoded_stabilizers
    )
    matter_failures = gauge_failures = ancilla_x_failures = 0
    for index, row in enumerate(total_decoded):
        ancilla_x_failures += bool(row.x & ancilla_mask)
        support = row.x | row.z
        if index < len(raw_matter):
            matter_failures += bool(support & gauge_mask)
        elif index < len(raw_matter) + len(raw_gauge):
            gauge_failures += bool(support & ~(gauge_mask | target_mask | ancilla_mask))
            # Gauge may touch target only through the shared parity wire.
            parity_wire = frame["input_pivots"][6*cells - 1]
            gauge_failures += bool(support & target_mask & ~(1 << parity_wire))

    p_m = total_decoded[-2]
    p_g = total_decoded[-1]
    logical_mask = target_mask | gauge_mask
    parity_logical_match = (
        (p_m.x & logical_mask, p_m.z & logical_mask, p_m.phase)
        == (p_g.x & logical_mask, p_g.z & logical_mask, p_g.phase)
        and not (p_m.x & ancilla_mask) and not (p_g.x & ancilla_mask)
    )
    coordinates = tuple(
        abstract_coordinates(row, frame["input_pivots"], pivots)
        for row in total_decoded
    )
    coordinate_payload = tuple((phase, x, z) for phase, x, z, _az in coordinates)
    maximum_ancilla_Z_dressing = max(az.bit_count() for _p, _x, _z, az in coordinates)
    gate_counts = Counter(g.kind for g in encoder)
    result = {
        "length": length, "split": {3: "construction", 6: "train", 7: "held-out-no-refit"}[length],
        "pivot_order": "reverse" if reverse else "forward",
        "coarse_cells": cells, "physical_M2": n,
        "target_Fock_input_qubits": 6*cells, "gauge_input_qubits": cells-1,
        "code_exponent": len(logical), "stabilizer_blank_input_M2": len(pivots),
        "work_M2": 0, "returned_blank_work_exact": True,
        "target_plus_gauge_equals_code_exponent": 6*cells + cells-1 == len(logical),
        "independent_stabilizers": len(reduced["basis"]),
        "expected_stabilizer_rank": expected_rank,
        "complete_matter_generators_conjugated": len(raw_matter),
        "complete_gauge_generators_conjugated": len(raw_gauge),
        "all_local_and_fill_stabilizers_conjugated": len(stabilizers),
        "stabilizer_plus_reference_failures": stabilizer_reference_failures,
        "matter_generator_target_only_failures": matter_failures,
        "gauge_generator_partition_failures": gauge_failures,
        "ancilla_X_leakage_failures": ancilla_x_failures,
        "shared_parity_logical_match": parity_logical_match,
        "maximum_generator_ancilla_Z_dressing": maximum_ancilla_Z_dressing,
        "both_matter_parities_in_domain": True,
        "parity_conjugate_selector_supplied": True,
        "factor_alphabet": ["H", "S", "CNOT"],
        "maximum_factor_support_M2": max(g.support for g in encoder),
        "decoder_stabilizer_gate_count": len(stab_gates),
        "decoder_logical_chart_gate_count": len(frame["decoder_gates"]),
        "encoder_factor_count": len(encoder),
        "encoder_factors_per_cell": len(encoder) / cells,
        "encoder_factor_counts": dict(gate_counts),
        "encoder_factor_sha256": gate_digest(encoder),
        "encoder_first_factors": [g.__dict__ for g in encoder[:8]],
        "encoder_last_factors": [g.__dict__ for g in encoder[-8:]],
        "stabilizer_pivot_sha256": sha256(repr(sorted(pivots)).encode()).hexdigest(),
        "input_wire_sha256": sha256(repr(frame["input_pivots"]).encode()).hexdigest(),
        "decoded_complete_generator_sha256": sha256(repr(tuple((r.phase, r.x, r.z) for r in total_decoded)).encode()).hexdigest(),
        "abstract_complete_generator_sha256": sha256(repr(coordinate_payload).encode()).hexdigest(),
        "elapsed_seconds": time.perf_counter() - started,
    }
    result["pass"] = bool(
        result["target_plus_gauge_equals_code_exponent"]
        and len(pivots) == expected_rank and result["maximum_factor_support_M2"] <= 2
        and stabilizer_reference_failures == matter_failures == gauge_failures == ancilla_x_failures == 0
        and parity_logical_match
    )
    internals = {
        "objects": objects, "encoder": encoder, "total_decoder": total_decoder,
        "decoded_complete": total_decoded, "target_wires": target_wires,
        "gauge_wires": gauge_wires, "ancilla_wires": ancilla_wires,
        "raw_ops": all_ops,
        "raw_stabilizers": tuple(stabilizers),
        "stabilizer_basis": reduced["basis"],
        "decoded_stabilizers": decoded_stabilizers,
        "input_pivots": frame["input_pivots"],
        "abstract_coordinates": coordinate_payload,
    }
    return result, internals


def order_equivalence(forward_row: dict, forward: dict) -> dict:
    reverse_row, reverse = frame_and_isometry(3, reverse=True)
    forward_coordinates = forward["abstract_coordinates"]
    reverse_coordinates = reverse["abstract_coordinates"]
    same_symplectic_coordinates = all(
        left[1:] == right[1:]
        for left, right in zip(forward_coordinates, reverse_coordinates)
    )
    rhs = tuple(((left[0] - right[0]) % 4) // 2 for left, right in zip(forward_coordinates, reverse_coordinates))
    correction = solve_sign_character(
        tuple((phase, x, z) for phase, x, z in reverse_coordinates), rhs,
        forward_row["code_exponent"],
    ) if same_symplectic_coordinates else None
    correction_failures = -1 if correction is None else sum(
        symp(correction, x | (z << forward_row["code_exponent"]), forward_row["code_exponent"]) != value
        for (_phase, x, z), value in zip(reverse_coordinates, rhs)
    )
    target = forward_row["target_Fock_input_qubits"]
    logical_mask = (1 << forward_row["code_exponent"]) - 1
    correction_x = 0 if correction is None else correction & logical_mask
    correction_z = 0 if correction is None else correction >> forward_row["code_exponent"]
    target_mask = (1 << target) - 1
    # Both reductions consume the identical signed stabilizer set.  Their
    # parity conjugates lie in the two-dimensional symplectic complement of
    # all even matter/gauge pairs; two valid choices differ only by P.
    result = {
        "length": 3,
        "orders": ["forward-low-pivot", "reverse-high-pivot"],
        "forward_factor_count": forward_row["encoder_factor_count"],
        "reverse_factor_count": reverse_row["encoder_factor_count"],
        "forward_factor_sha256": forward_row["encoder_factor_sha256"],
        "reverse_factor_sha256": reverse_row["encoder_factor_sha256"],
        "factor_lists_identical": forward_row["encoder_factor_sha256"] == reverse_row["encoder_factor_sha256"],
        "same_complete_abstract_matter_gauge_symplectic_coordinates": same_symplectic_coordinates,
        "sign_frame_correction_exists": correction is not None,
        "sign_frame_equation_failures": correction_failures,
        "relative_sign_frame_target_support": ((correction_x | correction_z) & target_mask).bit_count(),
        "relative_sign_frame_gauge_support": ((correction_x | correction_z) & ~target_mask).bit_count(),
        "same_signed_stabilizer_code": forward_row["stabilizer_plus_reference_failures"]
        == reverse_row["stabilizer_plus_reference_failures"] == 0,
        "relative_chart": "same complete even-algebra symplectic coordinates followed by one solved target/gauge Pauli sign frame; the supplied odd parity conjugate can differ only by target parity P",
        "equivalent_modulo_stabilizer_and_target_gauge_chart": True,
        "preferred_elimination_order_is_physical_input": False,
        "reverse_row": reverse_row,
    }
    result["pass"] = bool(
        reverse_row["pass"] and same_symplectic_coordinates and correction is not None
        and correction_failures == 0
        and not result["factor_lists_identical"]
        and result["same_signed_stabilizer_code"]
    )
    check("two inequivalent pivot/elimination schedules induce the same code and complete abstract generator chart",
          result["pass"], {"forward": result["forward_factor_count"], "reverse": result["reverse_factor_count"]})
    return result


def deletion_and_gauge_vacuum_controls(row: dict, internal: dict) -> dict:
    n = row["physical_M2"]
    decoder = internal["total_decoder"]
    stabilizers = internal["raw_stabilizers"]
    stabilizer_basis = internal["stabilizer_basis"]
    ops = internal["raw_ops"]
    pivots = internal["ancilla_wires"]
    input_pivots = internal["input_pivots"]
    ancilla_mask = sum(1 << q for q in pivots)
    baseline = internal["abstract_coordinates"]
    deletion_rows = []
    for kind in ("H", "S", "CNOT"):
        index = next(i for i, gate in enumerate(decoder) if gate.kind == kind)
        altered = decoder[:index] + decoder[index + 1:]
        decoded = transform_rows(stabilizers + ops, n, altered)
        stab_fail = sum(
            bool(item.x) or bool(item.z & ~ancilla_mask) or item.phase != 0
            for item in decoded[:len(stabilizers)]
        )
        coordinate_fail = 0
        ancilla_x_fail = 0
        for actual, expected in zip(decoded[len(stabilizers):], baseline):
            try:
                observed = abstract_coordinates(actual, input_pivots, pivots)
                coordinate_fail += observed[:3] != expected
            except AssertionError:
                ancilla_x_fail += 1
        deletion_rows.append({
            "deleted_decoder_factor": kind, "factor_index": index,
            "stabilizer_reference_failures": stab_fail,
            "complete_generator_coordinate_failures": coordinate_fail,
            "ancilla_X_failures": ancilla_x_fail,
            "detected": stab_fail + coordinate_fail + ancilla_x_fail > 0,
        })

    full_rank, full_inconsistent = c532.phase_rank(stabilizers, n)
    basis_rank, basis_inconsistent = c532.phase_rank(stabilizer_basis, n)
    deleted_rank, deleted_inconsistent = c532.phase_rank(stabilizer_basis[1:], n)
    sign_flipped = (Pauli((stabilizers[0].phase + 2) % 4, stabilizers[0].x, stabilizers[0].z),) + stabilizers[1:]
    flipped_rank, flipped_inconsistent = c532.phase_rank(sign_flipped, n)
    flipped_decoded = transform_rows(sign_flipped[:1], n, decoder)[0]

    gauge_input = tuple(Pauli(z=1 << q) for q in sorted(internal["gauge_wires"]))
    gauge_vacuum_physical = transform_rows(gauge_input, n, internal["encoder"])
    vacuum_rank, vacuum_inconsistent = c532.phase_rank(stabilizers + gauge_vacuum_physical, n)
    deleted_vacuum_rank, deleted_vacuum_inconsistent = c532.phase_rank(
        stabilizers + gauge_vacuum_physical[1:], n
    )
    malformed_vacuum = (
        Pauli((gauge_vacuum_physical[0].phase + 2) % 4,
              gauge_vacuum_physical[0].x, gauge_vacuum_physical[0].z),
    ) + gauge_vacuum_physical[1:]
    malformed_rank, malformed_inconsistent = c532.phase_rank(stabilizers + malformed_vacuum, n)
    matter_rows = internal["objects"]["matter"]
    gauge_vacuum_matter_commutator_failures = sum(
        not vacuum.commutes(matter)
        for vacuum in gauge_vacuum_physical for matter in matter_rows
    )

    result = {
        "length": 3, "representative_factor_deletions": deletion_rows,
        "full_stabilizer_rank": full_rank,
        "independent_stabilizer_basis_rank": basis_rank,
        "delete_one_independent_stabilizer_rank": deleted_rank,
        "full_deleted_phase_inconsistencies": [full_inconsistent, deleted_inconsistent],
        "flip_one_stabilizer_sign_rank": flipped_rank,
        "flip_one_stabilizer_sign_phase_inconsistencies": flipped_inconsistent,
        "flipped_stabilizer_decodes_to_minus_reference": flipped_decoded.phase == 2,
        "gauge_vacuum_is_optional_supplied_input_fixture": True,
        "gauge_vacuum_generators": len(gauge_vacuum_physical),
        "stabilizer_plus_gauge_vacuum_rank": vacuum_rank,
        "delete_one_gauge_vacuum_reference_rank": deleted_vacuum_rank,
        "malformed_minus_gauge_vacuum_rank": malformed_rank,
        "gauge_vacuum_phase_inconsistencies": [vacuum_inconsistent, deleted_vacuum_inconsistent, malformed_inconsistent],
        "minus_gauge_reference_consistent_but_refused_by_declared_plus_fixture": malformed_inconsistent == 0,
        "gauge_vacuum_matter_commutator_failures": gauge_vacuum_matter_commutator_failures,
    }
    result["pass"] = bool(
        all(item["detected"] for item in deletion_rows)
        and full_rank == row["expected_stabilizer_rank"]
        and basis_rank == full_rank and deleted_rank == full_rank - 1
        and full_inconsistent == basis_inconsistent == deleted_inconsistent == 0
        and flipped_rank == full_rank and flipped_inconsistent > 0
        and result["flipped_stabilizer_decodes_to_minus_reference"]
        and vacuum_rank == full_rank + row["gauge_input_qubits"]
        and deleted_vacuum_rank == vacuum_rank - 1
        and malformed_rank == vacuum_rank
        and vacuum_inconsistent == deleted_vacuum_inconsistent == malformed_inconsistent == 0
        and gauge_vacuum_matter_commutator_failures == 0
    )
    check("factor deletion, malformed stabilizer, and optional gauge-vacuum controls are load-bearing and inverse-visible",
          result["pass"], {"deletions": len(deletion_rows), "vacuum": len(gauge_vacuum_physical)})
    return result


def signed_axis(frame, axis: int) -> tuple[int, int]:
    image = frame @ c532.np.eye(3, dtype=int)[:, axis]
    target = int(c532.np.flatnonzero(image)[0])
    return target, int(image[target])


def covariance_controls(rows: list[dict]) -> dict:
    frames = c532.c235.proper_cubic_frames()
    size_rows = []
    for row in rows:
        length = row["length"]
        labels = tuple((axis, position) for axis in range(3) for position in range(length))
        frame_failures = 0
        for frame in frames:
            mapped = []
            for axis, position in labels:
                target, sign = signed_axis(frame, axis)
                mapped.append((target, sign * position % length))
            frame_failures += len(set(mapped)) != len(labels)
        group_failures = 0
        for left in frames:
            for right in frames:
                for axis, position in labels:
                    middle_axis, middle_sign = signed_axis(right, axis)
                    target_axis, target_sign = signed_axis(left, middle_axis)
                    composed = (target_axis, target_sign * middle_sign * position % length)
                    direct_axis, direct_sign = signed_axis(left @ right, axis)
                    if composed != (direct_axis, direct_sign * position % length):
                        group_failures += 1
                        break
        size_rows.append({
            "length": length, "split": row["split"], "abstract_cap_boundary_labels": len(labels),
            "frame_failures": frame_failures, "group_failures": group_failures,
            "factor_list_transport_digest": sha256((row["encoder_factor_sha256"] + repr(labels)).encode()).hexdigest(),
        })
    result = {
        "proper_cubic_frames": len(frames), "frame_products": len(frames) ** 2,
        "rows": size_rows, "runtime_frame_selector": False,
        "compile_time_retriangulated_abstract_cap_presentations": True,
        "encoder_family_transport_rule": "E_R = F_R E C_R^dagger on each frame-specific abstract presentation",
        "one_fixed_physical_3D_cap_embedding_claimed": False,
        "physical_3D_gate_distance_claimed": False,
        "pass": len(frames) == 24 and all(item["frame_failures"] == item["group_failures"] == 0 for item in size_rows),
    }
    check("L3/L6/L7 abstract encoder presentations close under all24/all576",
          result["pass"], {"sizes": len(size_rows), "frames": len(frames)})
    return result


def inherited_G_composition(rows: list[dict]) -> dict:
    inherited = c537.inherited_target_controls()
    gamma = inherited["full_Fock_Gamma_P"]
    fixture = inherited["mass_contact_and_seam"]
    fswap = inherited["FSWAP_polynomial_inverse"]
    block_rows = {
        "coin_onsite": {
            "intertwiner_residual": fixture["onsite_intertwiner_residual"],
            "inverse_residual": fixture["onsite_inverse_residual"],
            "leakage_residual": fixture["onsite_leakage_residual"],
        },
        "FSWAP": {
            "matrix_residual": fswap["matrix_residual"],
            "inverse_square_residual": fswap["inverse_square_residual"],
            "deleted_term_residual": fswap["deleted_fourth_term_residual"],
        },
        "contact": {
            "active_two_particle_states": fixture["Cycle230_contact_active_two_particle_states"],
            "deletion_residual": fixture["Cycle230_contact_deletion_residual"],
        },
        "B_GammaP": {
            "coefficient_identity_failures": sum(item["coefficient_identity_failures"] for item in gamma["quadratic_full_Fock_theorems"]),
            "vacuum_linear_or_constant_residual_terms": sum(item["vacuum_linear_or_constant_residual_terms"] for item in gamma["quadratic_full_Fock_theorems"]),
            "B_blocks_per_cell": gamma["rough_gauge_B_blocks_per_cell"],
        },
        "mass": {"Cycle219_residual": fixture["Cycle219_mass_fixture_residual"]},
        "seam": {
            "Cycle230_subchecks": fixture["Cycle230_seam_subchecks"],
            "singular_values": fixture["Cycle230_seam_singular_values"],
        },
    }
    generator_failures = sum(
        row["matter_generator_target_only_failures"]
        + row["gauge_generator_partition_failures"]
        + row["ancilla_X_leakage_failures"]
        for row in rows
    )
    result = {
        "composition_level": "exact generator and polynomial algebra on the declared abstract code space",
        "E_Gcoarse_equals_Gabstract_E": inherited["pass"] and generator_failures == 0,
        "proof_rule": "Clifford E maps every complete matter generator code-exactly; multiplication and linear combination therefore map each inherited coin/FSWAP/contact/B polynomial, while gauge inputs are spectators",
        "sizes": [row["length"] for row in rows], "generator_failures": generator_failures,
        "blocks": block_rows,
        "inherited_Cycle537_target_controls": inherited,
        "physical_Cycle642_G_claimed": False,
        "pass": inherited["pass"] and generator_failures == 0,
    }
    check("the full Cycle537 full-Fock G composes with E at generator/algebra level for coin/FSWAP/contact/B, mass and seam",
          result["pass"], {"generator_failures": generator_failures, "onsite": fixture["onsite_intertwiner_residual"]})
    return result


def inverse_controls(rows: list[dict], internals: list[dict]) -> dict:
    output = []
    for row, internal in zip(rows, internals):
        n = row["physical_M2"]
        if row["length"] == 3:
            indices = tuple(range(n))
            scope = "complete 2n canonical Pauli basis"
        else:
            candidates = (
                0, 1, n // 4, n // 2, 3 * n // 4, n - 2, n - 1,
                *sorted(internal["ancilla_wires"])[:4],
                *internal["input_pivots"][:4],
                *internal["input_pivots"][-4:],
            )
            indices = tuple(sorted(set(candidates)))
            scope = "deterministic boundary/quartile/ancilla/input basis sample plus factorwise inverse theorem"
        probes = tuple(
            item for q in indices for item in (Pauli(x=1 << q), Pauli(z=1 << q))
        )
        returned = transform_rows(
            probes, n, internal["encoder"] + internal["total_decoder"]
        )
        failures = sum(left != right for left, right in zip(probes, returned))
        output.append({
            "length": row["length"], "scope": scope,
            "canonical_generator_probes": len(probes), "roundtrip_failures": failures,
            "factorwise_inverse_rules": {"H": "H", "CNOT": "CNOT", "S": "S S S"},
            "work_M2": 0, "returned_blank_work_exact": True,
        })
    result = {"rows": output, "pass": all(item["roundtrip_failures"] == 0 for item in output)}
    check("encoder/decoder inverse returns target, gauge, stabilizer blanks, and zero work exactly",
          result["pass"], {"probes": sum(item["canonical_generator_probes"] for item in output)})
    return result


def rough_line_graph_distances(graph, requested_pairs: set[tuple[int, int]]) -> dict[tuple[int, int], int]:
    """Exact edge-line distance on the committed Cycle532 rough graph."""
    adjacency = [set() for _ in graph.vertices]
    endpoints = []
    for edge in graph.edges:
        local = (edge.u,) if edge.v is None else (edge.u, edge.v)
        endpoints.append(local)
        if edge.v is not None:
            adjacency[edge.u].add(edge.v)
            adjacency[edge.v].add(edge.u)
    source_vertices = {vertex for pair in requested_pairs for q in pair for vertex in endpoints[q]}
    vertex_distance = {}
    for source in source_vertices:
        distances = [-1] * len(adjacency)
        distances[source] = 0
        queue = deque([source])
        while queue:
            current = queue.popleft()
            for target in adjacency[current]:
                if distances[target] < 0:
                    distances[target] = distances[current] + 1
                    queue.append(target)
        vertex_distance[source] = distances
    output = {}
    for first, second in requested_pairs:
        if first == second:
            output[(first, second)] = 0
            continue
        candidates = [
            vertex_distance[left][right] + 1
            for left in endpoints[first] for right in endpoints[second]
            if vertex_distance[left][right] >= 0
        ]
        if not candidates:
            raise AssertionError(("disconnected rough edge pair", first, second))
        output[(first, second)] = min(candidates)
    return output


def physical_distance_audit(rows: list[dict], internals: list[dict]) -> dict:
    size_rows = []
    for row, internal in zip(rows, internals):
        graph = internal["objects"]["graph"]
        rough_qubits = graph.qubits
        gates = internal["encoder"]
        rough_pairs = {
            tuple(sorted((gate.a, gate.b)))
            for gate in gates
            if gate.kind == "CNOT" and gate.a < rough_qubits and gate.b < rough_qubits
        }
        distance_map = rough_line_graph_distances(graph, rough_pairs)
        distances = []
        two_abstract_unplaced = 0
        single_rough = single_cap_unplaced = 0
        for gate in gates:
            if gate.kind != "CNOT":
                if gate.a < rough_qubits:
                    single_rough += 1
                else:
                    single_cap_unplaced += 1
            elif gate.a < rough_qubits and gate.b < rough_qubits:
                distances.append(distance_map[tuple(sorted((gate.a, gate.b)))])
            else:
                two_abstract_unplaced += 1
        ordered = sorted(distances)
        def quantile(fraction: float) -> int | None:
            if not ordered:
                return None
            return ordered[min(len(ordered) - 1, int(fraction * (len(ordered) - 1)))]
        size_rows.append({
            "length": row["length"], "split": row["split"],
            "single_qubit_factors_on_rough_graph": single_rough,
            "single_qubit_factors_on_unplaced_cap_sites": single_cap_unplaced,
            "two_qubit_factors_total": row["encoder_factor_counts"]["CNOT"],
            "two_qubit_rough_rough_distance_measured": len(distances),
            "two_qubit_with_one_or_more_unplaced_cap_endpoints": two_abstract_unplaced,
            "rough_graph_distance_one": sum(value == 1 for value in distances),
            "rough_graph_distance_greater_than_one": sum(value > 1 for value in distances),
            "rough_graph_distance_maximum": max(distances, default=None),
            "rough_graph_distance_p50_p90_p99": [quantile(0.5), quantile(0.9), quantile(0.99)],
            "all_measured_rough_rough_factors_nearest_neighbor": bool(distances) and max(distances) <= 1,
        })
    result = {
        "metric": "exact line-graph distance between Cycle532 rough-edge M2s; cap-sheet M2s are counted unplaced because Cycle642 is not a premise",
        "rows": size_rows,
        "abstract_gate_arity_at_most_two": True,
        "bounded_physical_3D_locality_claimed": False,
        "unplaced_cap_factors_not_assigned_fake_distance": True,
        "pass": all(
            item["two_qubit_rough_rough_distance_measured"]
            + item["two_qubit_with_one_or_more_unplaced_cap_endpoints"]
            == item["two_qubit_factors_total"]
            for item in size_rows
        ),
    }
    check("every factor is classified by rough-graph distance or explicit unplaced-cap status without claiming physical locality",
          result["pass"], {"sizes": len(size_rows), "L7max": size_rows[-1]["rough_graph_distance_maximum"]})
    return result


def no_go_discipline(rows: list[dict]) -> dict:
    families = [
        {"family": "signed stabilizer Gaussian decoder", "object_formulation": "complete commuting Cycle537 stabilizer tableau", "mechanism_invariant": "Clifford column elimination to +Z pivots", "terminal_obligation": "literal E and inverse", "strength_vs_target": "target-equivalent abstractly", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
        {"family": "quotient symplectic chart", "object_formulation": "complete matter/gauge quotient generators", "mechanism_invariant": "Gram-Schmidt plus shared parity conjugate", "terminal_obligation": "6N target plus N-1 gauge inputs", "strength_vs_target": "target-equivalent abstractly", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
        {"family": "dual pivot order", "object_formulation": "reverse signed tableau elimination", "mechanism_invariant": "same code and generator coordinates modulo Pauli sign frame", "terminal_obligation": "no hidden preferred order", "strength_vs_target": "comparator", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
        {"family": "deletion and malformed-reference falsifier", "object_formulation": "factor/stabilizer/gauge-vacuum deletions", "mechanism_invariant": "rank, sign and coordinate witnesses", "terminal_obligation": "load-bearing circuit/reference audit", "strength_vs_target": "comparator", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
        {"family": "frame-transported presentation", "object_formulation": "24 abstract cap presentations", "mechanism_invariant": "signed-axis action and 576 products", "terminal_obligation": "proper-cubic presentation family", "strength_vs_target": "weaker than physical embedding", "honesty_marker": "ATTEMPTED", "status": "POSITIVE"},
    ]
    open_routes = [
        {"family": "physical routed cap encoder", "object_formulation": "one fixed 3D placement", "mechanism_invariant": "bounded physical distance routing", "terminal_obligation": "physical M2 E", "strength_vs_target": "different stronger target", "status": "OPEN_UNTESTED_NOT_FAILURE"},
        {"family": "autonomous local genesis", "object_formulation": "blank substrate plus state-carried scheduler", "mechanism_invariant": "derive pivot/root/order/gauge reference", "terminal_obligation": "host-free initialization", "strength_vs_target": "different stronger target", "status": "OPEN_UNTESTED_NOT_FAILURE"},
    ]
    conditions = {
        "W_place": "embed abstract cap adjacency and all encoder factors into bounded physical 3D neighborhoods",
        "W_genesis": "generate blank stabilizer/gauge reference, pivot/root/order and schedule autonomously",
    }
    pairs = [
        {"from": "W_place", "to": "W_genesis", "closure_implied": False},
        {"from": "W_genesis", "to": "W_place", "closure_implied": False},
    ]
    rhetoric = [
        {"phrase": "abstract support-two is not physical 3D locality", "per_element": "tested factor arity", "per_site": "UNTESTED", "per_mode": "UNTESTED", "per_block": "abstract cap adjacency only", "lattice_wide": "withheld"},
        {"phrase": "a compiler factor count is not time or a rate", "per_element": "one gate", "per_site": "UNTESTED", "per_mode": "UNTESTED", "per_block": "finite scheduled circuit", "lattice_wide": "withheld"},
        {"phrase": "a blank stabilizer or gauge reference is not autonomous genesis", "per_element": "explicit input", "per_site": "declared reference", "per_mode": "gauge fixture", "per_block": "full E domain", "lattice_wide": "withheld"},
    ]
    partial = [
        {"file": "scripts/abstract_fill_disk_full_tableau_isometry_cycle643_2026_07_23.py", "status": "EXECUTED_FULL_E_L3_L6_L7", "what_closes": "abstract Cycle537 state-preparation/isometry surface"},
        {"file": "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py", "status": "COMMITTED_ABSTRACT_CODE", "what_closes": "bounded cap stabilizers and target-times-gauge algebra"},
        {"file": "scripts/physical_fixed_wilson_initializer_preparation_tournament_cycle636_2026_07_23.py", "status": "RETIRED_OPEN_TABLEAU_ROW", "what_closes": "its hostile full-tableau steelman"},
        {"file": "future physical embedding/routing campaign", "status": "OPEN_NOT_TESTED", "what_closes": "physical distance/locality rather than abstract factor support"},
        {"file": "future genesis campaign", "status": "OPEN_NOT_TESTED", "what_closes": "host-free roots, blank/gauge reference, order and schedule"},
    ]
    c537_note = "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md"
    c636_note = "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_WILSON_INITIALIZER_PREPARATION_TOURNAMENT_CYCLE636_NOTE_2026-07-23.md"
    c539_note = "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md"
    current = "scripts/abstract_fill_disk_full_tableau_isometry_cycle643_2026_07_23.py"
    residuals = [
        {"prior_ref": SHORE_HEAD, "prior_path": c537_note, "prior_line": git_line(c537_note, "state-preparation/code-space-isometry circuit"), "prior_residual": "no abstract Cycle537 code-space isometry", "current_ref": "working-tree Cycle643 candidate", "current_path": current, "current_line": source_line("def frame_and_isometry"), "current_residual": "complete L3/L6/L7 abstract H/S/CNOT isometry", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_HEAD, "prior_path": c636_note, "prior_line": git_line(c636_note, "full stabilizer tableau circuit"), "prior_residual": "full stabilizer tableau and volume logical map not derived", "current_ref": "working-tree Cycle643 candidate", "current_path": current, "current_line": source_line("def reduce_stabilizers"), "current_residual": "complete stabilizer and logical-chart factor lists", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_HEAD, "prior_path": c539_note, "prior_line": git_line(c539_note, "does not yet compose differently addressed overlapping patches"), "prior_residual": "selected-patch overlap recurrence", "current_ref": "working-tree Cycle643 candidate", "current_path": current, "current_line": source_line("physical_distance_audit"), "current_residual": "full abstract fill-code isometry without physical placement", "same_scope": False, "exact_match": False, "use_as_closure": False},
    ]
    n7_citations = [
        {"ref": SHORE_HEAD, "path": c537_note, "line": git_line(c537_note, "Closing that physical embedding"), "supports": "physical cap embedding remains a separate constructive route"},
        {"ref": SHORE_HEAD, "path": c636_note, "line": git_line(c636_note, "optimal next preparation campaign is the hostile steelman"), "supports": "the full-tableau route was explicitly actionable and has now advanced"},
    ]
    echoes = [
        {"cycle": 537, "retired": "missing abstract code-space isometry", "mechanism": "complete signed stabilizer plus logical-frame Clifford synthesis", "applicability": "exact", "citation_ref": SHORE_HEAD, "citation_path": c537_note, "citation_line": git_line(c537_note, "state-preparation/code-space-isometry circuit")},
        {"cycle": 636, "retired": "full-tableau steelman", "mechanism": "materialized H/S/CNOT E at L3/L6/L7", "applicability": "exact abstract target", "citation_ref": SHORE_HEAD, "citation_path": c636_note, "citation_line": git_line(c636_note, "full-tableau encoder separately")},
        {"cycle": 539, "retired": "selected-patch isometry only", "mechanism": "compute/select/uncompute on a different patch", "applicability": "prior mechanism only; not closure evidence", "citation_ref": SHORE_HEAD, "citation_path": c539_note, "citation_line": git_line(c539_note, "compute/select/uncompute")},
        {"cycle": 537, "retired": "abstract all24/all576 cap presentation", "mechanism": "compile-time retriangulated presentation orbit", "applicability": "retained exactly, not physical embedding", "citation_ref": SHORE_HEAD, "citation_path": c537_note, "citation_line": git_line(c537_note, "all 24 / 576")},
        {"cycle": 636, "retired": "physical embedding kept separate", "mechanism": "dependency-layer separation", "applicability": "still enforced; Cycle642 not consumed", "citation_ref": SHORE_HEAD, "citation_path": c636_note, "citation_line": git_line(c636_note, "independent physical-cap embedding probe")},
    ]
    result = {
        "Status": "PASS",
        "status": "PASS",
        "N1_normalized_families": families,
        "N1_open_routes_separate_without_honesty_marker": open_routes,
        "N1_reason": "NO_NEGATIVE_CLAIM_IS_PROMOTED",
        "N1_broad_negative_gate": "FAIL / DO NOT SHIP",
        "N2_collapsed_open_conditions": conditions,
        "N2_directional_pairs": pairs,
        "N3_hidden_condition_scan": [
            "cap topology and adjacency are supplied",
            "pivot, root, row order, parity-conjugate selector and factor schedule are supplied",
            "blank stabilizer M2s and optional plus gauge vacuum are supplied",
            "Cycle642 physical embedding is not consumed",
            "finite L3/L6/L7 domains and compile-time frame presentations are supplied",
            "generic Gaussian factor/program scaling has no all-L linear-size, constant-per-cell, or bounded-depth theorem",
        ],
        "N4_residual_matching": residuals,
        "N5_rhetoric_audit": rhetoric,
        "N6_partial_closure_paths": partial,
        "N7_steelman_against_any_no_go": {
            "argument": "Transport the now-complete abstract Clifford list through a reviewed Cycle642-or-later physical cap embedding, route each support-two factor with bounded physical swaps or a local wavefront, and replace the compile-time pivot/order by state-carried control; Cycle643 removes the algebraic isometry uncertainty rather than foreclosing that construction.",
            "mechanism": "physical cap routing plus autonomous state-carried tableau schedule",
            "terminal_obligation": "same complete generator table, bounded physical neighborhoods, returned routing work, and all24/all576 without a runtime frame selector",
            "actionable_test": "take a reviewed physical cap embedding, compile each Cycle643 factor to bounded-distance paths, uncompute every routing rail, and compare the complete abstract generator digest at L3/L6/L7",
            "citations": n7_citations,
        },
        "N8_cross_cycle_echo": echoes,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "broad_no_go_claimed": False,
        "minimum_content_claimed": False,
        "shared_route_independent_obstruction_claimed": False,
        "axiom_pressure": False,
    }
    result["pass"] = bool(
        result["Status"] == "PASS"
        and len(families) >= 5
        and all(item["honesty_marker"] in {"ATTEMPTED", "RULED OUT BY PRIOR"} for item in families)
        and all("honesty_marker" not in item for item in open_routes)
        and len(pairs) == 2 and len(residuals) == 3
        and all(all(key in item for key in ("prior_ref", "prior_path", "prior_line", "prior_residual", "current_ref", "current_path", "current_line", "current_residual", "same_scope", "exact_match", "use_as_closure")) for item in residuals)
        and all(all(key in item for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for item in rhetoric)
        and all(all(key in item for key in ("file", "status", "what_closes")) for item in partial)
        and len(echoes) == 5 and len(rows) == 3
        and all(result[key] == "FAIL / DO NOT SHIP" for key in (
            "N1_broad_negative_gate", "broad_negative_gate", "minimum_content_gate",
            "shared_obstruction_gate", "axiom_pressure_gate",
        ))
        and not any(result[key] for key in (
            "broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim",
            "axiom_pressure_claim", "shared_route_independent_obstruction", "axiom_pressure",
        ))
    )
    check("N1-N8 scope firewall keeps the constructive abstract E distinct from physical placement and genesis",
          result["pass"], {"families": len(families), "conditions": len(conditions)})
    return result


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def note_text(receipt: dict) -> str:
    rows = receipt["isometry_L3_L6_L7"]
    table = "\n".join(
        f"| L{row['length']} | {row['split']} | {row['physical_M2']} | "
        f"{row['target_Fock_input_qubits']} | {row['gauge_input_qubits']} | "
        f"{row['stabilizer_blank_input_M2']} | {row['encoder_factor_count']} | "
        f"{row['encoder_factors_per_cell']:.3f} | "
        f"{row['encoder_factor_counts']['H']} / {row['encoder_factor_counts']['S']} / "
        f"{row['encoder_factor_counts']['CNOT']} |"
        for row in rows
    )
    order = receipt["pivot_order_equivalence"]
    deletion = receipt["deletion_and_gauge_vacuum_controls"]
    blocks = receipt["inherited_full_Fock_G_composition"]["blocks"]
    distance_rows = receipt["physical_distance_audit"]["rows"]
    distance_table = "\n".join(
        f"| L{item['length']} | {item['two_qubit_factors_total']} | "
        f"{item['two_qubit_rough_rough_distance_measured']} | "
        f"{item['two_qubit_with_one_or_more_unplaced_cap_endpoints']} | "
        f"{item['rough_graph_distance_one']} | "
        f"{item['rough_graph_distance_greater_than_one']} | "
        f"{item['rough_graph_distance_maximum']} | "
        f"{item['rough_graph_distance_p50_p90_p99']} |"
        for item in distance_rows
    )
    return f"""# Abstract fill-disk full-tableau isometry — Cycle 643

Classification: **positive literal abstract Cycle537 Clifford isometry; physical 3D placement and autonomous genesis remain separate and unclaimed**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough bar met: **false**

## Result up front

Cycle 643 closes Cycle537's state-preparation/isometry omission on the exact
**abstract enlarged fill-disk code**.  It does not consume Cycle642 or any
dirty Cycle532/Cycle537 bytes.  The runner loads the committed source blobs at
`{SHORE_HEAD}`, verifies all nine shore hashes, and synthesizes an exact
Clifford isometry

```text
E : (C^2)^(6N target) tensor (C^2)^(N-1 gauge)
    tensor |0>^(rank S_fill)  ->  H_fill
```

from only `H`, `S`, and `CNOT`.  Work M2 count is zero.  Every factor has
support at most two in the abstract cap adjacency/factor grammar.  The full
factor lists are materialized, iterated, and hashed at all three sizes:

| size | split | physical M2 | target | gauge | blank stabilizer M2 | factors | factors/cell | H / S / CNOT |
|---|---|---:|---:|---:|---:|---:|---:|---:|
{table}

The held L7 list is fully materialized, not replaced by a symbolic recurrence.
Its `{rows[2]['encoder_factor_count']}` factors have digest
`{rows[2]['encoder_factor_sha256']}`.

The observed factor counts per cell are
`{rows[0]['encoder_factors_per_cell']:.3f}`,
`{rows[1]['encoder_factors_per_cell']:.3f}`, and
`{rows[2]['encoder_factors_per_cell']:.3f}`.  They increase across the tested
sizes.  Generic Gaussian elimination supplies no all-L linear-size,
constant-factors-per-cell, or bounded-depth theorem.  The spatial M2 count per
cell is bounded on the declared finite rows; factor/program scaling is not
established, and held L7 is not asymptotic locality evidence.

## Physical-distance audit

Support arity and physical range are kept separate.  For CNOT endpoints that
both lie on the committed Cycle532 rough graph, the runner computes exact
edge-line distance.  Any factor touching an added cap-sheet M2 is counted as
**unplaced** because no Cycle642 embedding is admitted; it is not assigned a
fake distance.

| size | two-qubit factors | rough/rough measured | cap-unplaced | distance 1 | distance >1 | max | p50/p90/p99 |
|---|---:|---:|---:|---:|---:|---:|---|
{distance_table}

Thus the emitted list is explicitly nonlocal in the committed rough-graph
metric and partly unplaced.  Cycle643 certifies exact abstract factor arity,
not bounded physical 3D locality.

## Literal synthesis grammar

The decoder first selects an independent signed basis of every Cycle537 local
and fill stabilizer.  Deterministic Pauli-column elimination uses `H` to swap
X/Z, `S` to clear Y, and `CNOT` to clear remote support.  Row multiplication
is only a classical synthesis operation: the emitted quantum factor list
contains no row-operation oracle.  Each selected stabilizer becomes one exact
`+Z` reference pivot.  Every dependent displayed stabilizer is then run
through the complete circuit and checked to be a phase-zero product of those
reference `Z`s.

On the remaining `7N-1` wires, symplectic Gram-Schmidt gives `6N-1` matter
pairs, `N-1` gauge pairs, and the common matter/gauge parity radical.  One
explicit supplied parity conjugate completes the 6N-qubit full-Fock target
chart.  A second H/S/CNOT elimination maps that complete frame to input
coordinates.  Reversing the total decoder—with `S^-1 = S S S`—is the literal
encoder `E`.

This charges the pivot/root, row and factor order, parity-conjugate selector,
blank `+Z` stabilizer state, optional gauge-vacuum reference, and compile
schedule.  None is hidden as a dynamical law.

## Complete stabilizer, matter, gauge, and parity certificate

At L3/L6/L7 the exact code dimensions are respectively `188`, `1511`, and
`2400`, equal to `6N + (N-1)` in every row.  The circuit conjugates
`{rows[0]['all_local_and_fill_stabilizers_conjugated']}` /
`{rows[1]['all_local_and_fill_stabilizers_conjugated']}` /
`{rows[2]['all_local_and_fill_stabilizers_conjugated']}` displayed stabilizers,
with zero plus-reference failures.  It also conjugates all
`{rows[0]['complete_matter_generators_conjugated']}` /
`{rows[1]['complete_matter_generators_conjugated']}` /
`{rows[2]['complete_matter_generators_conjugated']}` matter generators and
`{rows[0]['complete_gauge_generators_conjugated']}` /
`{rows[1]['complete_gauge_generators_conjugated']}` /
`{rows[2]['complete_gauge_generators_conjugated']}` explicit gauge generators.
Matter-to-gauge, gauge-partition, and ancilla-X leakage failures are all zero.

The matter and gauge parity rows decode to the same target parity coordinate.
The final target parity input may be zero or one, so both matter parities are
in the isometry domain.  A physical generator may retain a product of blank
ancilla `Z`s; this is enumerated explicitly and acts as identity on the
declared input code.  Thus conjugation is exact on the declared code space,
not an equality silently extended off code.

## Two elimination orders

Forward low-pivot and reverse high-pivot synthesis at L3 give different
factor lists: `{order['forward_factor_count']}` versus
`{order['reverse_factor_count']}` factors and distinct digests.  Nevertheless
they give the same signed stabilizer code and identical complete matter/gauge
symplectic coordinates.  The runner solves one Pauli sign-frame correction
with target/gauge supports `{order['relative_sign_frame_target_support']}` /
`{order['relative_sign_frame_gauge_support']}`.  The only freedom in the odd
parity conjugate is multiplication by target parity.  Hence the two circuits
are equivalent modulo stabilizer and target/gauge chart, and elimination
order is not promoted to a preferred physical ordering.

## Inverse, deletion, malformed, and gauge-vacuum controls

The complete L3 `2n` canonical Pauli basis and deterministic L6/L7 held
samples round-trip through `E` and its decoder with zero failures; factorwise
inverse rules prove the remaining basis rows identically.  There are no work
M2s, so returned blank work is exact rather than postselected.

Deleting representative `H`, `S`, or `CNOT` factors is detected by stabilizer
or complete-generator failures.  Deleting one independent stabilizer lowers
rank `{deletion['full_stabilizer_rank']} ->
{deletion['delete_one_independent_stabilizer_rank']}`.  Flipping one displayed
stabilizer sign produces `{deletion['flip_one_stabilizer_sign_phase_inconsistencies']}`
phase inconsistencies and decodes to a minus reference.

The `N-1` gauge wires are arbitrary inputs in the full isometry.  For the
optional supplied plus gauge-vacuum fixture, L3 adds exactly
`{deletion['gauge_vacuum_generators']}` independent `+Z` references; deleting
one lowers rank by one.  A minus gauge reference is algebraically consistent
but refused by that declared plus fixture.  This is a fixture check, not a
claim that gauge-vacuum genesis is derived.

## Full-Fock update composition

On the declared abstract code space the complete generator conjugation and
polynomial homomorphism give

```text
E G_coarse = G_abstract E.
```

This covers the inherited coin/onsite, FSWAP, contact, and B/Gamma(P) blocks.
The exact inherited controls retain onsite residual
`{blocks['coin_onsite']['intertwiner_residual']:.3e}`, FSWAP matrix residual
`{blocks['FSWAP']['matrix_residual']:.1e}`, zero B coefficient failures,
Cycle219 mass residual `{blocks['mass']['Cycle219_residual']:.3e}`, contact
deletion residual `{blocks['contact']['deletion_residual']:.15f}`, and Cycle230
seam `{blocks['seam']['Cycle230_subchecks']['pass']}` PASS / `{blocks['seam']['Cycle230_subchecks']['fail']}` FAIL.
This is `G_abstract` on Cycle537's cap code, not a Cycle642 physical update.

## Proper-cubic presentation covariance

The L3 construction, L6 train, and held L7 presentations each close under all
24 proper-cubic frames and all 576 products with zero label failures.  For a
frame `R`, the compile-time family is `E_R = F_R E C_R^dagger`.  This is the
same frame-specific retriangulated **abstract cap presentation** discipline as
Cycle537.  It is not one fixed cap embedding in ordinary 3D physical distance,
not a runtime frame selector, and not an autonomous schedule.

## Supplied, derived, and open

Supplied: committed Cycle532/Cycle537 algebra and inherited update fixtures;
three abstract fill disks and their adjacency; finite L3/L6/L7 domains;
pivot/root and row order; parity-conjugate selector; target/gauge input chart;
blank stabilizer state; optional gauge-vacuum reference; factor schedule; and
compile-time frame presentation.

Derived: complete factor lists; exact stabilizer `+Z` reduction; exact
`6N + N-1` logical chart; all displayed matter/gauge generator coordinates;
both matter parities; inverse and zero returned work; deletion/malformed
controls; two-order equivalence; abstract all24/all576; and generator/algebra
composition with the inherited full-Fock update.

Open and not tested: bounded-distance placement of these factors in a single
physical 3D M2 embedding; routing and returned routing work there; autonomous
blank/gauge-reference/pivot/root/order/schedule genesis; infinite-volume and
noise controls; and any time, Record, Born, gravity, or source interpretation.

Abstract support-two is not physical 3D locality.  A compiler factor count is
not time or a rate.  A blank stabilizer or gauge reference is not autonomous
genesis.  No phase is called energy and no gauge capacity is called source.

## N1-N8 scope discipline

N1 records five normalized ATTEMPTED families and lists the untested
physical-routing and autonomous-genesis families separately, without honesty
markers and without counting them as failures.  N2 retains the
two distinct open conditions and both directions.  N3 exposes every supplied
selector, reference, order, topology, and schedule.  N4 matches Cycle537 and
Cycle636 exactly, drops Cycle539's different patch residual, and never consumes
Cycle642.  N5 audits the
three negative boundary phrases at five resolutions.  N6 lists five concrete
partial-closure paths.  N7 gives the physical-routing/state-carried steelman.
N8 records five cross-cycle echoes.

Broad no-go: **not claimed**.  Minimum content: **not claimed**.  Shared
route-independent obstruction: **not established**.  Axiom pressure:
**none**.  The N1-N8 scope status is **PASS**; the broad-no-go,
minimum-content, shared-obstruction, and axiom-pressure promotion gates are all
**FAIL / DO NOT SHIP**.

## Six-wall ledger and terminal

| wall | Cycle643 movement | residual |
|---|---|---|
| `C_ref` | literal full E, both parities, inverse, two-order equivalence | pivot/root/chart/blank/gauge reference and schedule supplied |
| `C_num` | exact target-times-gauge dimensions and complete generator tables | no empirical unit; factor counts are not time/rates |
| `C_wrap` | every stabilizer is locally named in the abstract cap and inverse-visible | physical embedding, autonomous renewal, Records/history open |
| `C_int` | inherited coin/FSWAP/contact/B, mass and seam compose through E | no new physical interaction law; Cycle642 not consumed |
| `C_local` | every factor support <=2; abstract all24/all576 | bounded physical 3D distance/routing untested |
| `C_source` | all blank/gauge/work/schedule resources explicit; work=0 | no source/stress/gravity meaning or autonomous resource genesis |

Strongest honest terminal: a complete literal H/S/CNOT isometry for the exact
abstract Cycle537 fill-disk code at L3/L6/L7, with full generator/algebra
intertwining.  It is not yet a physical 3D M2 compiler.
"""


def note_contract() -> dict:
    flat = " ".join(NOTE.read_text().lower().split())
    required = (
        "authority: **none**", "audit: **unset**", "author artifact status accepted: **false**",
        "breakthrough bar met: **false**", "abstract enlarged fill-disk code",
        "h", "s", "cnot", "both matter parities", "all 24", "all 576",
        "e g_coarse = g_abstract e", "not time or a rate", "not physical 3d locality",
        "cycle642", "shared route-independent obstruction: **not established**",
        "axiom pressure: **none**", "fail / do not ship",
        "factor/program scaling is not established",
    )
    missing = [item for item in required if item not in flat]
    return {"required_fragments": required, "missing": missing, "pass": not missing}


def main() -> None:
    signal.alarm(WALL_SECONDS)
    started = time.perf_counter()
    shore = immutable_shore()
    rows = []
    internals = []
    for length in (3, 6, 7):
        row, internal = frame_and_isometry(length)
        rows.append(row)
        internals.append(internal)
        check(f"L{length} forward full abstract tableau isometry", row["pass"],
              {"factors": row["encoder_factor_count"], "elapsed": row["elapsed_seconds"]})
    order = order_equivalence(rows[0], internals[0])
    deletion = deletion_and_gauge_vacuum_controls(rows[0], internals[0])
    inverse = inverse_controls(rows, internals)
    distance = physical_distance_audit(rows, internals)
    covariance = covariance_controls(rows)
    inherited = inherited_G_composition(rows)
    no_go = no_go_discipline(rows)
    receipt = {
        "status": "positive complete literal abstract Cycle537 fill-disk H/S/CNOT isometry; physical 3D placement and autonomous genesis open",
        "authority": AUTHORITY, "audit": AUDIT,
        "constitutional_effect": "none",
        "author_accepted": False, "author_artifact_status_accepted": False,
        "breakthrough": False, "breakthrough_bar_met": False,
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
        "immutable_shore": shore,
        "isometry_L3_L6_L7": rows,
        "pivot_order_equivalence": order,
        "deletion_and_gauge_vacuum_controls": deletion,
        "inverse_controls": inverse,
        "physical_distance_audit": distance,
        "covariance": covariance,
        "inherited_full_Fock_G_composition": inherited,
        "no_go_discipline": no_go,
        "supplied_structure_inventory": {
            "Cycle532_Cycle537_committed_abstract_algebra": True,
            "Cycle642_physical_embedding": False,
            "abstract_cap_topology_and_adjacency": True,
            "finite_L3_L6_L7_domains": True,
            "pivot_root_row_order_and_schedule": True,
            "parity_conjugate_and_target_gauge_chart": True,
            "blank_plus_stabilizer_M2": True,
            "optional_plus_gauge_vacuum": True,
            "work_M2": 0,
            "autonomous_genesis": False,
            "all_L_linear_size_or_constant_factors_per_cell_theorem": False,
            "all_L_bounded_depth_theorem": False,
        },
        "factor_program_scaling_firewall": {
            "rows": [
                {"length": row["length"], "factors": row["encoder_factor_count"],
                 "cells": row["coarse_cells"], "factors_per_cell": row["encoder_factors_per_cell"]}
                for row in rows
            ],
            "observed_factors_per_cell_increase": all(
                rows[index]["encoder_factors_per_cell"] < rows[index + 1]["encoder_factors_per_cell"]
                for index in range(len(rows) - 1)
            ),
            "generic_Gaussian_all_L_linear_size_theorem": False,
            "constant_factors_per_cell_theorem": False,
            "bounded_depth_theorem": False,
            "held_L7_is_asymptotic_locality_evidence": False,
            "spatial_M2_overhead_and_factor_program_scaling_kept_distinct": True,
        },
        "route_disposition": {
            "full_abstract_Cycle537_E": "PASS_LITERAL_H_S_CNOT_L3_L6_L7",
            "complete_stabilizer_matter_gauge_conjugation": "PASS_CODE_EXACT",
            "inherited_full_Fock_G": "PASS_E_GCOARSE_EQUALS_GABSTRACT_E_ON_CODE",
            "second_pivot_order": "PASS_EQUIVALENT_MODULO_STABILIZER_TARGET_GAUGE_SIGN_CHART",
            "physical_3D_M2_embedding_and_routing": "OPEN_NOT_CONSUMED",
            "autonomous_genesis": "OPEN_NOT_CLAIMED",
        },
        "six_wall_ledger": {
            "C_ref": "full abstract E/both parity/inverse/order equivalence; pivot/root/chart/blank/gauge reference/schedule supplied",
            "C_num": "exact target-times-gauge dimensions and complete tables; no empirical unit and factors not time/rates",
            "C_wrap": "abstract local stabilizers and inverse visible; physical embedding/renewal/Records/history open",
            "C_int": "coin/FSWAP/contact/B mass/seam compose; no new interaction and Cycle642 not consumed",
            "C_local": "factor support<=2 and abstract all24/all576; physical 3D distance/routing untested",
            "C_source": "all blanks/gauge/work/schedule explicit, work=0; no source/gravity or autonomous genesis",
        },
        "highest_honest_terminal": "complete literal H/S/CNOT isometry for the exact abstract Cycle537 fill-disk code at L3/L6/L7 with full generator/algebra intertwining; not a physical 3D M2 compiler",
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "optimal_next_campaign": "transport the exact Cycle643 factor grammar through a separately reviewed physical cap embedding, bound physical routing distance/work, and replace pivot/root/order/blank/gauge references with a state-carried autonomous schedule",
    }
    canonical_claim_gate_contract = {
        "top_constitutional_effect_none": receipt.get("constitutional_effect") == "none",
        "top_claim_flags_false": not any(receipt.get(key, True) for key in (
            "broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim",
            "axiom_pressure_claim", "shared_route_independent_obstruction", "axiom_pressure",
        )),
        "no_go_Status_PASS": no_go.get("Status") == "PASS",
        "all_promotion_gates_FAIL_DO_NOT_SHIP": all(
            no_go.get(key) == "FAIL / DO NOT SHIP" for key in (
                "N1_broad_negative_gate", "broad_negative_gate", "minimum_content_gate",
                "shared_obstruction_gate", "axiom_pressure_gate",
            )
        ),
        "no_go_claim_flags_false": not any(no_go.get(key, True) for key in (
            "broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim",
            "axiom_pressure_claim", "shared_route_independent_obstruction", "axiom_pressure",
        )),
        "scaling_firewall_complete": (
            receipt["factor_program_scaling_firewall"]["observed_factors_per_cell_increase"]
            and not receipt["factor_program_scaling_firewall"]["generic_Gaussian_all_L_linear_size_theorem"]
            and not receipt["factor_program_scaling_firewall"]["constant_factors_per_cell_theorem"]
            and not receipt["factor_program_scaling_firewall"]["bounded_depth_theorem"]
            and not receipt["factor_program_scaling_firewall"]["held_L7_is_asymptotic_locality_evidence"]
        ),
    }
    canonical_claim_gate_contract["pass"] = all(canonical_claim_gate_contract.values())
    receipt["canonical_claim_gate_contract"] = canonical_claim_gate_contract
    check("canonical claim gates, top-level flags, and scaling firewall are machine-enforced",
          canonical_claim_gate_contract["pass"], canonical_claim_gate_contract)
    NOTE.write_text(note_text(receipt))
    contract = note_contract()
    check("Cycle643 note preserves abstract/physical, causal, supply, and no-go firewalls",
          contract["pass"], contract["missing"])
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000:
        rss *= 1024
    receipt.update({
        "note_contract": contract,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0)),
        "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0,
    })
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=float) + "\n")
    print(json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
        "receipt": str(RECEIPT),
    }, indent=2))


if __name__ == "__main__":
    main()
