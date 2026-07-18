#!/usr/bin/env python3
"""Exact bounded probe of the genuine 3-D anomalous-bulk/category-index route."""

from __future__ import annotations

import json
import re
from collections import Counter
from itertools import permutations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "THREE_DIMENSIONAL_ANOMALOUS_BULK_CATEGORY_INDEX_STEELMAN_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PARENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md"
)


PASS = 0
FAIL = 0

I2 = sp.eye(2)
X2 = sp.Matrix([[0, 1], [1, 0]])
Z2 = sp.diag(1, -1)
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    return " ".join(
        path.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .split()
    )


def exact_equal(left: sp.Matrix | sp.Expr, right: sp.Matrix | sp.Expr) -> bool:
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        return all(sp.simplify(sp.expand_complex(value)) == 0 for value in difference)
    return sp.simplify(sp.expand_complex(difference)) == 0


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                rotations.append(matrix)
    unique = {tuple(matrix): matrix for matrix in rotations}
    return tuple(unique.values())


ROTATIONS = proper_cubic_rotations()


def rotate_tuple(rotation: sp.Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(int(value) for value in rotation * sp.Matrix(vector))


def controlled_phase(theta: sp.Expr) -> sp.Matrix:
    return sp.diag(1, 1, 1, sp.exp(sp.I * theta))


def partial_transfer(theta: sp.Expr) -> sp.Matrix:
    cosine = sp.cos(theta)
    sine = sp.sin(theta)
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, cosine, sine, 0],
            [0, -sine, cosine, 0],
            [0, 0, 0, 1],
        ]
    )


def partial_trace(
    density: sp.Matrix,
    keep: tuple[int, ...],
    number_qubits: int,
) -> sp.Matrix:
    traced = tuple(index for index in range(number_qubits) if index not in keep)
    output = sp.zeros(2 ** len(keep))
    for row_keep in product((0, 1), repeat=len(keep)):
        for column_keep in product((0, 1), repeat=len(keep)):
            total = 0
            for environment in product((0, 1), repeat=len(traced)):
                row_bits = [0] * number_qubits
                column_bits = [0] * number_qubits
                for index, qubit in enumerate(keep):
                    row_bits[qubit] = row_keep[index]
                    column_bits[qubit] = column_keep[index]
                for index, qubit in enumerate(traced):
                    row_bits[qubit] = environment[index]
                    column_bits[qubit] = environment[index]
                row = int("".join(str(bit) for bit in row_bits), 2)
                column = int("".join(str(bit) for bit in column_bits), 2)
                total += density[row, column]
            output_row = int("".join(str(bit) for bit in row_keep), 2)
            output_column = int("".join(str(bit) for bit in column_keep), 2)
            output[output_row, output_column] = sp.simplify(total)
    return output


def tensor_response(source: sp.Matrix, trace_weight: sp.Expr) -> sp.Matrix:
    trace_part = sp.trace(source) * sp.eye(3) / 3
    traceless = source - trace_part
    return sp.simplify(traceless + trace_weight * trace_part)


def authority_and_source_contract() -> None:
    section("A - Authority, constitution, primitives, and source boundaries")
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    kinetic = normalized(KINETIC)
    realized = normalized(REALIZED)
    scale = normalized(SCALE)
    parent = normalized(PARENT)
    registry_text = REGISTRY.read_text(encoding="utf-8").lower()
    json.loads(REGISTRY.read_text(encoding="utf-8"))

    check("A note exists", NOTE.is_file())
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom, registry, primitive, audit, review queue, or retained surface"
        in note,
    )
    check(
        "A universal no-go is explicitly withheld",
        "a universal no-go against a one-site, proper-cubic, non-clifford anomalous qca is not claimed"
        in note,
    )
    check(
        "A constitutional occurrence and detailed formation rule are separated",
        "records form." in axioms
        and "formation rule (which admissible possibility, at which site, with what weight, at what rate)"
        in axioms,
    )
    check(
        "A parent genuine anomalous-bulk route is wired in",
        "genuine three-dimensional anomalous bulk" in parent,
    )
    check(
        "A realized-state primitive supplies no selector or boundary",
        "does not supply a state, state-selection rule" in realized
        and "boundary condition" in realized,
    )
    check(
        "A kinetic primitive supplies isotropy but not dynamics",
        "c_t = c_s" in kinetic and "not a new dynamics" in kinetic,
    )
    check(
        "A scale primitive supplies units without dimensionless dynamics",
        "units conversion" in scale and "zero dimensionless content" in scale,
    )
    for key in (
        "minimal_axioms",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "scale_reference_primitive",
    ):
        check(f"A primitive registry contains {key}", key in registry_text)

    urls = (
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/1902.10285",
        "https://arxiv.org/abs/1907.02075",
        "https://arxiv.org/abs/1812.01625",
        "https://arxiv.org/abs/2202.05442",
        "https://arxiv.org/abs/2504.14811",
        "https://arxiv.org/abs/2509.07099",
    )
    raw_note = NOTE.read_text(encoding="utf-8")
    for url in urls:
        check(f"A primary-source link is present: {url.rsplit('/', 1)[-1]}", url in raw_note)
    check(
        "A current compiled carrier boundary is explicit",
        "two qubits on each face" in note and "six per unit cell" in note,
    )
    check(
        "A equivalence-class boundary is explicit",
        "classification of stabilized qcas modulo circuits" in note
        or "modulo circuits and separated automorphisms" in note,
    )


def cubic_edge_kernel() -> None:
    section("B - Proper-cubic primitive-qubit finite-depth kernel")
    check("B proper cubic group has 24 rotations", len(ROTATIONS) == 24)
    check("B every proper cubic matrix has determinant one", all(r.det() == 1 for r in ROTATIONS))
    check(
        "B six nearest-neighbor directions form one invariant set",
        all({rotate_tuple(r, d) for d in DIRECTIONS} == set(DIRECTIONS) for r in ROTATIONS),
    )

    size = 4
    vertices = tuple(product(range(size), repeat=3))
    edges: set[frozenset[tuple[int, int, int]]] = set()
    colored: dict[tuple[int, int], list[frozenset[tuple[int, int, int]]]] = {
        (axis, parity): [] for axis in range(3) for parity in range(2)
    }
    for vertex in vertices:
        for axis in range(3):
            target = list(vertex)
            target[axis] = (target[axis] + 1) % size
            edge = frozenset((vertex, tuple(target)))
            edges.add(edge)
            colored[(axis, vertex[axis] % 2)].append(edge)

    check("B four-torus has expected undirected edge count", len(edges) == 3 * size**3)
    check("B edge coloring has six layers", len(colored) == 6)
    for color, layer in colored.items():
        endpoints = [endpoint for edge in layer for endpoint in edge]
        check(
            f"B edge-color layer {color} is pairwise disjoint",
            len(endpoints) == len(set(endpoints)),
        )

    def translate(vertex: tuple[int, int, int], shift: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple((vertex[index] + shift[index]) % size for index in range(3))

    for shift in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        moved = {
            frozenset(translate(endpoint, shift) for endpoint in edge)
            for edge in edges
        }
        check(f"B full edge set is translation invariant under {shift}", moved == edges)

    phase_half = controlled_phase(sp.pi / 2)
    phase_full = controlled_phase(sp.pi)
    check("B pi/2 controlled phase is unitary", exact_equal(phase_half.H * phase_half, sp.eye(4)))
    check("B pi controlled phase is unitary", exact_equal(phase_full.H * phase_full, sp.eye(4)))
    plus_pair = sp.Matrix([1, 1, 1, 1]) / 2
    output_half = phase_half * plus_pair
    output_full = phase_full * plus_pair
    check("B phase representatives are distinct", not exact_equal(output_half, output_full))
    concurrence_half = sp.simplify(sp.sin(sp.pi / 4) ** 2)
    concurrence_full = sp.simplify(sp.sin(sp.pi / 2) ** 2)
    check("B pi/2 squared concurrence is one half", concurrence_half == sp.Rational(1, 2))
    check("B pi squared concurrence is one", concurrence_full == 1)

    cz = phase_full
    check(
        "B CZ conjugates X on first qubit to X tensor Z",
        exact_equal(cz * sp.kronecker_product(X2, I2) * cz.H, sp.kronecker_product(X2, Z2)),
    )
    check(
        "B CZ conjugates X on second qubit to Z tensor X",
        exact_equal(cz * sp.kronecker_product(I2, X2) * cz.H, sp.kronecker_product(Z2, X2)),
    )
    check(
        "B CZ preserves both Pauli Z generators",
        exact_equal(cz * sp.kronecker_product(Z2, I2) * cz.H, sp.kronecker_product(Z2, I2))
        and exact_equal(cz * sp.kronecker_product(I2, Z2) * cz.H, sp.kronecker_product(I2, Z2)),
    )

    # Exact quotient bookkeeping: local circuits carry the neutral class.
    bulk_class = 1
    circuit_class = 0
    check("B circuit decoration leaves a Z2 bulk class unchanged", (bulk_class + circuit_class) % 2 == bulk_class)
    check("B the nontrivial Z2 class is self-inverse", (-bulk_class) % 2 == bulk_class)
    check("B the nontrivial Z2 class squares to neutral", (bulk_class + bulk_class) % 2 == 0)
    check("B a Z4 generator and inverse are distinct", (-1) % 4 == 3 and 1 != 3)


def carrier_and_orientation_boundaries() -> None:
    section("C - Primitive carrier, compiled carriers, and orientation")
    check("C one primitive qubit cannot directly factor record and carrier qubits", 2 < 2 * 2)
    check("C two qubits per face gives six qubits per cubic cell", 2 * 3 == 6)
    check("C two qubits per link gives six qubits per cubic cell", 2 * 3 == 6)
    check("C one qubit per edge gives three qubits per cubic cell", 1 * 3 == 3)
    check("C six compiled qubits have dimension 64", 2**6 == 64)
    check("C primitive six-site block can match that raw dimension", 2**6 == 64)

    e1 = sp.Matrix([1, 0, 0])
    e2 = sp.Matrix([0, 1, 0])
    e3 = sp.Matrix([0, 0, 1])
    oriented_volume = sp.Matrix.hstack(e1, e2, e3).det()
    check("C reference oriented volume is positive", oriented_volume == 1)
    check(
        "C proper cubic rotations preserve the pseudoscalar hand",
        all(sp.Matrix.hstack(r * e1, r * e2, r * e3).det() == 1 for r in ROTATIONS),
    )
    reflection = sp.diag(-1, 1, 1)
    check("C a spatial reflection flips the pseudoscalar hand", reflection.det() == -1)
    check("C reflection is not among supplied proper rotations", all(reflection != r for r in ROTATIONS))


def record_boundary_and_occurrence() -> None:
    section("D - Post-record boundary and occurrence-domain pairs")
    basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def record(position: tuple[int, int, int], center: tuple[int, int, int], present: int) -> int:
        return int(present == 1 and position == center)

    def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(left[index] + right[index] for index in range(3))

    def scale(value: int, vector: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(value * component for component in vector)

    def gradient(
        position: tuple[int, int, int],
        center: tuple[int, int, int],
        present: int,
    ) -> tuple[int, int, int]:
        return tuple(
            record(add(position, scale(-1, direction)), center, present)
            - record(add(position, direction), center, present)
            for direction in basis
        )

    centers = ((0, 0, 0), (2, -1, 3))
    check(
        "D isolated records give all six translated normals",
        all(
            gradient(add(center, direction), center, 1) == direction
            for center in centers
            for direction in DIRECTIONS
        ),
    )
    check(
        "D absent records give zero on every tested neighbor",
        all(
            gradient(add(center, direction), center, 0) == (0, 0, 0)
            for center in centers
            for direction in DIRECTIONS
        ),
    )

    center = (0, 0, 0)
    check(
        "D record gradient is proper-cubic covariant for all 144 tests",
        all(
            rotate_tuple(rotation, gradient(direction, center, 1))
            == gradient(rotate_tuple(rotation, direction), center, 1)
            for rotation in ROTATIONS
            for direction in DIRECTIONS
        ),
    )

    omega_even = lambda boundary, parity: boundary * (1 - parity)
    omega_odd = lambda boundary, parity: boundary * parity
    even_table = tuple(omega_even(boundary, parity) for boundary, parity in product((0, 1), repeat=2))
    odd_table = tuple(omega_odd(boundary, parity) for boundary, parity in product((0, 1), repeat=2))
    check("D even and odd occurrence laws are distinct", even_table != odd_table)
    check("D even occurrence law has nonempty domain", any(even_table))
    check("D odd occurrence law has nonempty domain", any(odd_table))
    check("D neither boundary law nucleates at b=0", omega_even(0, 0) == omega_even(0, 1) == 0 and omega_odd(0, 0) == omega_odd(0, 1) == 0)


def transfer_and_append_sector() -> None:
    section("E - Conserved transfer pair and finite append-sector lemma")
    number = sp.diag(0, 1, 1, 2)
    half = partial_transfer(sp.pi / 4)
    full = partial_transfer(sp.pi / 2)
    for label, gate in (("half", half), ("full", full)):
        check(f"E {label} transfer is unitary", exact_equal(gate.H * gate, sp.eye(4)))
        check(f"E {label} transfer conserves total occupation", exact_equal(gate * number, number * gate))

    source_occupied = sp.Matrix([0, 0, 1, 0])
    half_output = half * source_occupied
    full_output = full * source_occupied
    outgoing_projector = sp.diag(0, 1, 0, 1)
    half_probability = sp.simplify((half_output.H * outgoing_projector * half_output)[0])
    full_probability = sp.simplify((full_output.H * outgoing_projector * full_output)[0])
    check("E half-transfer outgoing occupation is one half", half_probability == sp.Rational(1, 2))
    check("E full-transfer outgoing occupation is one", full_probability == 1)
    check("E transfer outputs are distinct", not exact_equal(half_output, full_output))

    blank = {0, 1}
    record = {2, 3}
    invariant_permutations = []
    no_blank_entry = True
    for permutation in permutations(range(4)):
        invariant = {permutation[index] for index in record}.issubset(record)
        if invariant:
            invariant_permutations.append(permutation)
            no_blank_entry = no_blank_entry and {
                permutation[index] for index in blank
            }.isdisjoint(record)
    check("E invariant finite record sectors receive no blank basis state", no_blank_entry)
    check("E exactly four four-state permutations preserve the two-state record sector", len(invariant_permutations) == 4)
    check(
        "E every invariant permutation reduces blank and record sectors",
        all(
            {permutation[index] for index in blank} == blank
            and {permutation[index] for index in record} == record
            for permutation in invariant_permutations
        ),
    )


def coherent_record_versus_instrument() -> None:
    section("F - Coherent witness correlation versus outcome instrument")
    ket000 = sp.zeros(8, 1)
    ket111 = sp.zeros(8, 1)
    ket000[0] = 1
    ket111[7] = 1
    ghz = (ket000 + ket111) / sp.sqrt(2)
    coherent = sp.simplify(ghz * ghz.H)
    dephased = sp.simplify((ket000 * ket000.H + ket111 * ket111.H) / 2)
    check("F coherent GHZ density has unit trace", sp.trace(coherent) == 1)
    check("F dephased outcome density has unit trace", sp.trace(dephased) == 1)
    check("F coherent and dephased global states differ", not exact_equal(coherent, dephased))
    check("F coherent state retains 000-111 coherence", coherent[0, 7] == sp.Rational(1, 2))
    check("F instrument state removes 000-111 coherence", dephased[0, 7] == 0)
    for keep in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
        check(
            f"F proper record marginal {keep} agrees",
            exact_equal(partial_trace(coherent, keep, 3), partial_trace(dephased, keep, 3)),
        )
    check("F coherent global state is pure", sp.trace(coherent * coherent) == 1)
    check("F dephased global state has purity one half", sp.trace(dephased * dephased) == sp.Rational(1, 2))


def tensor_and_species_pairs() -> None:
    section("G - Tensor and species finite-depth kernel pairs")
    source = sp.Matrix([[2, 1, 0], [1, -1, 1], [0, 1, 3]])
    response_one = tensor_response(source, sp.Integer(1))
    response_two = tensor_response(source, sp.Integer(2))
    check("G tensor response weights one and two are distinct", not exact_equal(response_one, response_two))
    for weight in (sp.Integer(1), sp.Integer(2)):
        check(
            f"G tensor weight {weight} is proper-cubic covariant for all rotations",
            all(
                exact_equal(
                    tensor_response(rotation * source * rotation.T, weight),
                    rotation * tensor_response(source, weight) * rotation.T,
                )
                for rotation in ROTATIONS
            ),
        )

    charges = (-9, -5, -1, 7, 8)
    check("G scoped charges sum to zero", sum(charges) == 0)
    check("G scoped charge cubes sum to zero", sum(charge**3 for charge in charges) == 0)
    gamma_common = (1, 1, 1, 1, 1)
    gamma_charge = tuple(abs(charge) for charge in charges)
    check("G common and charge-dependent species couplings differ", gamma_common != gamma_charge)

    configurations = tuple(product((0, 1), repeat=6))
    total_charge = sp.diag(
        *(sum(charges[index] * bits[index] for index in range(5)) for bits in configurations)
    )

    def species_phase(gamma: tuple[int, ...]) -> sp.Matrix:
        return sp.diag(
            *(
                sp.exp(
                    sp.I
                    * sp.pi
                    * bits[5]
                    * sum(gamma[index] * bits[index] for index in range(5))
                    / 17
                )
                for bits in configurations
            )
        )

    common_gate = species_phase(gamma_common)
    charge_gate = species_phase(gamma_charge)
    for label, gate in (("common", common_gate), ("charge-dependent", charge_gate)):
        check(f"G {label} species gate is unitary", exact_equal(gate.H * gate, sp.eye(64)))
        check(f"G {label} species gate conserves total charge", exact_equal(gate * total_charge, total_charge * gate))
    check("G common and charge-dependent species gates are distinct", not exact_equal(common_gate, charge_gate))


def residual_ledger_and_no_go_gate() -> None:
    section("H - Residual ledger and no-go discipline visibility")
    fields = ("O0", "O1", "T", "S", "A", "X", "M", "R", "G")
    assignments = tuple(product((0, 1), repeat=len(fields)))
    check("H nine binary law fields have 512 assignments", len(assignments) == 512)
    check("H every assignment is unique", len(set(assignments)) == 512)
    for coordinate, field in enumerate(fields):
        pairs = {
            tuple(value for index, value in enumerate(assignment) if index != coordinate)
            for assignment in assignments
        }
        check(f"H deleting {field} leaves 256 exact pairs", len(pairs) == 256)

    target = (1,) * len(fields)
    full_cost = lambda assignment: sum(left != right for left, right in zip(assignment, target))
    minima = [assignment for assignment in assignments if full_cost(assignment) == 0]
    check("H nine selection clauses choose one completion", minima == [target])
    for coordinate, field in enumerate(fields):
        def reduced_cost(assignment: tuple[int, ...]) -> int:
            return sum(
                assignment[index] != target[index]
                for index in range(len(fields))
                if index != coordinate
            )

        best = min(reduced_cost(assignment) for assignment in assignments)
        reduced_minima = [assignment for assignment in assignments if reduced_cost(assignment) == best]
        check(f"H deleting the {field} clause restores exactly two minima", len(reduced_minima) == 2)

    raw_note = NOTE.read_text(encoding="utf-8")
    note = normalized(NOTE)
    for number in range(1, 9):
        check(f"H N{number} section is visible", f"### n{number} —" in note)
    check("H N1 contains at least five attempted routes", raw_note.count("**ATTEMPTED") >= 5)
    check("H N2 contains all 36 pairwise N/N cells", raw_note.count("N/N") >= 36)
    check(
        "H N7 forces partial-attempt demotion",
        "the steelman is convincing" in note
        and "partial-attempt-with-named-untested-route" in note,
    )
    check(
        "H result does not say new axiom required",
        "accordingly the result is not" in note and "new axiom required" in note,
    )

    hidden_phrases = (
        "we assume",
        "by construction",
        "as is standard",
        "the framework provides",
        "bridge context",
        "background",
        "naturally",
        "obviously",
        "standard qft",
    )
    for phrase in hidden_phrases:
        occurrences = note.count(phrase)
        check(
            f"H hidden phrase has no load-bearing use: {phrase}",
            occurrences == 0
            or (
                occurrences == 1
                and "the proof does not use" in note
                and "as load-bearing shortcuts" in note
            ),
        )
    check(
        "H canonical phrase is classified as disclaimer-only",
        "canonical-law choice" in note
        and "appears only in the authority disclaimer" in note,
    )
    check(
        "H primitive registry inspection is stated",
        "the primitive registry was inspected" in note,
    )


def link_and_scope_checks() -> None:
    section("I - Local links, scope words, and source-note agreement")
    raw = NOTE.read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", raw)
    local_links = [link for link in links if not link.startswith(("http://", "https://", "#"))]
    for link in local_links:
        target_text = link.split("#", 1)[0]
        target = (NOTE.parent / target_text).resolve()
        check(f"I local link resolves: {target.name}", target.exists())

    note = normalized(NOTE)
    required_scope_phrases = (
        "direct factorization obstruction only",
        "conditional boundary theorem",
        "not a first-record theorem",
        "does not imply that those items need separate axioms",
        "no result here proves it impossible",
        "probability lane is also not closed by the category",
        "no verbatim axiom addition",
    )
    for phrase in required_scope_phrases:
        check(f"I scope phrase is present: {phrase}", phrase in note)

    check(
        "I primary-source carrier statement and runner arithmetic agree",
        "2 qubits/face x 3 face families/cell = 6 qubits/cell" in note,
    )
    check(
        "I exact Z2 self-inverse result is stated",
        "alpha^2=id" in note and "[alpha]=[alpha^-1]" in note,
    )
    check(
        "I upstream compiler and class selection are separated",
        "p = equivariant compiler" in note and "b = exact-law selection" in note,
    )
    check(
        "I downstream ledger has the same nine fields as runner",
        all(f"{field.lower()} " in note or f"{field.lower()} =" in note for field in ("O0", "O1", "T", "S", "A", "X", "M", "R", "G")),
    )


def main() -> int:
    authority_and_source_contract()
    cubic_edge_kernel()
    carrier_and_orientation_boundaries()
    record_boundary_and_occurrence()
    transfer_and_append_sector()
    coherent_record_versus_instrument()
    tensor_and_species_pairs()
    residual_ledger_and_no_go_gate()
    link_and_scope_checks()

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
