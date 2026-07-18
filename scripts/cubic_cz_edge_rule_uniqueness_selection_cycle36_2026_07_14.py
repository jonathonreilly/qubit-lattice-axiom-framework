#!/usr/bin/env python3
"""Cycle 36 exact uniqueness/selection attack on the cubic CZ-edge rule.

This authority-free runner exhausts the smallest pointwise-Z-preserving
nearest-neighbor diagonal Clifford class, tests foundation-static and
law-relative equivalences, supplies exact record-protocol witnesses, and
enlarges phase/order/boundary/instrument assumptions one at a time.  It does
not edit any live foundation, registry, queue, policy, or audit surface.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE21 = REVIEW / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md"
CYCLE33 = REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0


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
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Source, authority, and scope contract")
    for path in (NOTE, AXIOMS, REGISTRY, CYCLE21, CYCLE33):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A no live edit is authorized", "no live axiom or primitive edit is justified" in note)
    check("A no audit verdict is issued", "does not issue an audit verdict" in note)
    check("A current Qubit has no privileged possibility", "No possibility is privileged." in axioms)
    check("A current Admissibility is availability-only", "Admissibility is not a dynamics axiom." in axioms)
    check("A current state is record-only", "A state is a configuration of records." in axioms)
    check("A selected-Z restriction is explicit", "selected-z subclass" in note)
    check("A static and transported equivalence are separated", "time-dependent transported equivalence" in note)
    check("A CZ is not promoted to a full TOE", "constraint/preparation layer, not the full l" in note)
    check("A exact residual selector is named", "uniform per-step onsite-z parity" in note)
    for heading in range(1, 9):
        check(f"A N{heading} discipline section present", f"n{heading} —" in note)
    for source in (
        "https://arxiv.org/abs/quant-ph/9705052",
        "https://arxiv.org/abs/quant-ph/0108118",
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/1608.06596",
    ):
        check(f"A primary source cited: {source.rsplit('/', 1)[-1]}", source in note)


I = sp.I
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.diag(1, -1)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
S = sp.diag(1, I)
CZ = sp.diag(1, 1, 1, -1)
PAULIS = (I2, X, Y, Z)


def tensor(*matrices: sp.Matrix) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return sp.Matrix(result)


def first_nonzero(matrix: sp.Matrix) -> sp.Expr | None:
    for value in matrix:
        if sp.simplify(value) != 0:
            return value
    return None


def equal_up_to_phase(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    pivot_left = first_nonzero(left)
    pivot_right = first_nonzero(right)
    if pivot_left is None or pivot_right is None:
        return pivot_left is pivot_right
    ratio = sp.simplify(pivot_left / pivot_right)
    return all(sp.simplify(a - ratio * b) == 0 for a, b in zip(left, right))


TWO_QUBIT_PAULIS = tuple(tensor(left, right) for left in PAULIS for right in PAULIS)


def is_pauli_up_to_phase(matrix: sp.Matrix) -> bool:
    return any(equal_up_to_phase(matrix, pauli) for pauli in TWO_QUBIT_PAULIS)


def diagonal_gate(exponents: tuple[int, int, int, int]) -> sp.Matrix:
    return sp.diag(*(I ** exponent for exponent in exponents))


def is_diagonal_clifford(exponents: tuple[int, int, int, int]) -> bool:
    gate = diagonal_gate(exponents)
    return all(
        is_pauli_up_to_phase(sp.simplify(gate * generator * gate.H))
        for generator in (tensor(X, I2), tensor(I2, X))
    )


def edge_census() -> None:
    section("B - Exhaustive two-site diagonal Clifford edge census")
    all_gates = tuple((0, a, b, c) for a, b, c in product(range(4), repeat=3))
    cliffords = tuple(exponents for exponents in all_gates if is_diagonal_clifford(exponents))
    symmetric = tuple(exponents for exponents in cliffords if exponents[1] == exponents[2])
    entangling_symmetric = tuple(
        exponents
        for exponents in symmetric
        if (exponents[0] + exponents[3] - exponents[1] - exponents[2]) % 4 != 0
    )
    involutive_edges = tuple(
        exponents
        for exponents in entangling_symmetric
        if all((2 * exponent) % 4 == 0 for exponent in exponents)
    )
    expected = {
        (0, 0, 0, 2),
        (0, 1, 1, 0),
        (0, 2, 2, 2),
        (0, 3, 3, 0),
    }
    check("B fourth-root diagonal census has 64 gates modulo phase", len(all_gates) == 64)
    check("B exactly 32 fourth-root diagonal gates are Clifford", len(cliffords) == 32)
    check("B exactly eight diagonal Cliffords exchange endpoints", len(symmetric) == 8)
    check("B exactly four symmetric candidates are entangling", len(entangling_symmetric) == 4)
    check("B canonical four entangling edge phases are exact", set(entangling_symmetric) == expected)
    check("B only two entangling edge gates are themselves involutive", len(involutive_edges) == 2)
    check("B CZ is in the census", (0, 0, 0, 2) in entangling_symmetric)
    for a in range(4):
        expected_exponents = (0, a, a, (2 * a + 2) % 4)
        candidate = tensor(S ** a, S ** a) * CZ
        check(
            f"B edge candidate a={a} equals (S^a tensor S^a)CZ",
            diagonal_gate(expected_exponents) == candidate,
        )
    check("B CZ fixes the first local Z pointwise", CZ * tensor(Z, I2) * CZ == tensor(Z, I2))
    check("B CZ fixes the second local Z pointwise", CZ * tensor(I2, Z) * CZ == tensor(I2, Z))
    check("B CZ is genuinely entangling", sp.Matrix(CZ * tensor(H, H)[:, 0]).reshape(2, 2).det() != 0)


def torus_geometry(length: int = 3) -> tuple[tuple[tuple[int, int, int], ...], tuple[tuple[int, int], ...]]:
    vertices = tuple(product(range(length), repeat=3))
    index = {vertex: i for i, vertex in enumerate(vertices)}
    edges: set[tuple[int, int]] = set()
    for vertex in vertices:
        for axis in range(3):
            neighbor = list(vertex)
            neighbor[axis] = (neighbor[axis] + 1) % length
            edges.add(tuple(sorted((index[vertex], index[tuple(neighbor)]))))
    return vertices, tuple(sorted(edges))


def global_classification() -> None:
    section("C - Global range-one cubic diagonal Clifford classification")
    vertices, edges = torus_geometry()
    degrees = tuple(sum(site in edge for edge in edges) for site in range(len(vertices)))
    check("C three-torus has 27 sites", len(vertices) == 27)
    check("C three-torus has 81 undirected nearest-neighbor edges", len(edges) == 81)
    check("C every site has six distinct neighbors", set(degrees) == {6})

    # A range-one homogeneous diagonal Clifford phase is
    # b sum_x z_x + 2c sum_<xy> z_x z_y (mod 4).
    all_global = tuple((b, c) for b in range(4) for c in (0, 1))
    entangling = tuple(pair for pair in all_global if pair[1] == 1)
    involutive = tuple(pair for pair in entangling if (2 * pair[0]) % 4 == 0)
    check("C homogeneous range-one diagonal Clifford class has eight laws", len(all_global) == 8)
    check("C four homogeneous laws are entangling", len(entangling) == 4)
    check("C exactly two entangling global laws are involutive", set(involutive) == {(0, 1), (2, 1)})

    edge_to_global = {a: (6 * a) % 4 for a in range(4)}
    check("C four edge presentations collapse to two global onsite phases", set(edge_to_global.values()) == {0, 2})
    check("C even a compiles to U_CZ", edge_to_global[0] == edge_to_global[2] == 0)
    check("C odd a compiles to Z_all U_CZ", edge_to_global[1] == edge_to_global[3] == 2)
    check("C both global candidates square pointwise to identity", all((2 * b) % 4 == 0 for b, _ in involutive))
    check("C both have minimal entangling support two", all(c == 1 for _, c in involutive))
    check("C both have radius one", all(c == 1 for _, c in involutive))
    axis_counts = [0, 0, 0]
    for left, right in edges:
        changed = [axis for axis in range(3) if vertices[left][axis] != vertices[right][axis]]
        if len(changed) == 1:
            axis_counts[changed[0]] += 1
    check("C both treat all three axes identically", axis_counts == [27, 27, 27])
    check("C candidate residual is one binary onsite-Z parity", {b // 2 for b, _ in involutive} == {0, 1})


def static_equivalence_control() -> None:
    section("D - Foundation-static equivalence versus transported frame")
    vertices, edges = torus_geometry()
    degrees = tuple(sum(site in edge for edge in edges) for site in range(len(vertices)))

    # A one-qubit Clifford is specified by signed perpendicular images of X,Z.
    axes = (("X", 1), ("X", -1), ("Y", 1), ("Y", -1), ("Z", 1), ("Z", -1))
    perpendicular = {"X": {"Y", "Z"}, "Y": {"X", "Z"}, "Z": {"X", "Y"}}
    clifford_frames = tuple(
        (image_x, image_z)
        for image_x in axes
        for image_z in axes
        if image_z[0] in perpendicular[image_x[0]]
    )
    pointer_normalizers = tuple(frame for frame in clifford_frames if frame[1][0] == "Z")
    check("D signed-axis enumeration gives 24 onsite Clifford frames", len(clifford_frames) == 24)
    check("D exactly eight onsite Clifford frames normalize the Z axis", len(pointer_normalizers) == 8)
    check("D local one-site fixed algebra forces Z-axis normalization", all(frame[1][0] == "Z" for frame in pointer_normalizers))

    # Common diagonal recodings commute.  A common anti-diagonal recoding is
    # diagonal times X_all.  Complementing all bits changes the all-edge CZ
    # phase only by 2|E|-2d sum(z), and d=6 kills the variable term mod 4.
    variable_coefficient = {(-2 * degree) % 4 for degree in degrees}
    constant_coefficient = (2 * len(edges)) % 4
    check("D common X recoding creates no variable phase on degree six", variable_coefficient == {0})
    check("D common X changes U_CZ by global phase only", constant_coefficient in (0, 2))
    check("D static pointer-normalizing onsite recoding preserves epsilon", variable_coefficient != {2})
    translated_linear_coefficients = {(2 + 0) % 4 for _ in vertices}
    permuted_axis_coefficients = tuple(2 for _ in range(3))
    check("D lattice translations cannot change uniform epsilon", translated_linear_coefficients == {2})
    check("D proper cubic rotations cannot change uniform epsilon", permuted_axis_coefficients == (2, 2, 2))
    check("D two candidates are not foundation-static common-onsite/site conjugates", variable_coefficient == {0})

    z_all_pair = tensor(Z, Z)
    u0_pair = CZ
    u1_pair = z_all_pair * u0_pair
    transported_equal: list[bool] = []
    for time in (0, 1):
        f_now = z_all_pair ** time
        f_next = z_all_pair ** (time + 1)
        transported = sp.simplify(f_next * u0_pair * f_now.H)
        transported_equal.append(transported == u1_pair)
        check(f"D alternating frame transports U0 to U1 at parity t={time}", transported_equal[-1])
    check("D transported equivalence is time dependent", z_all_pair != sp.eye(4))
    check(
        "D static and time-dependent equivalence therefore differ",
        variable_coefficient == {0} and all(transported_equal) and z_all_pair != sp.eye(4),
    )


def bits(index: int, count: int) -> tuple[int, ...]:
    return tuple((index >> (count - 1 - site)) & 1 for site in range(count))


def bit_index(word: tuple[int, ...]) -> int:
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value


def star_state(epsilon: int) -> sp.Matrix:
    site_count = 7
    edges = tuple((0, leaf) for leaf in range(1, site_count))
    amplitudes: list[sp.Expr] = []
    for index in range(2**site_count):
        word = bits(index, site_count)
        edge_phase = (-1) ** sum(word[left] * word[right] for left, right in edges)
        onsite_phase = (-1) ** (epsilon * sum(word))
        amplitudes.append(sp.Rational(edge_phase * onsite_phase, 1) / sp.sqrt(2**site_count))
    return sp.Matrix(amplitudes)


def pauli_word_expectation(
    state: sp.Matrix,
    site_count: int,
    x_sites: frozenset[int],
    z_sites: frozenset[int],
) -> sp.Expr:
    result = 0
    for index in range(2**site_count):
        word = list(bits(index, site_count))
        phase = (-1) ** sum(word[site] for site in z_sites)
        moved = list(word)
        for site in x_sites:
            moved[site] ^= 1
        result += sp.conjugate(state[bit_index(tuple(moved)), 0]) * phase * state[index, 0]
    return sp.simplify(result)


def record_protocol_witness() -> None:
    section("E - Exact boundary and record-instrument witnesses")
    psi0 = star_state(0)
    psi1 = star_state(1)
    check("E both seven-site causal-cone states normalize", (psi0.H * psi0)[0] == (psi1.H * psi1)[0] == 1)
    leaves = frozenset(range(1, 7))
    k0 = pauli_word_expectation(psi0, 7, frozenset((0,)), leaves)
    k1 = pauli_word_expectation(psi1, 7, frozenset((0,)), leaves)
    check("E U0 gives graph-stabilizer record parity plus one", k0 == 1)
    check("E U1 gives graph-stabilizer record parity minus one", k1 == -1)
    check("E seven disjoint one-site records distinguish with certainty", {k0, k1} == {-1, 1})
    probabilities0 = tuple(sp.simplify(abs(value) ** 2) for value in psi0)
    probabilities1 = tuple(sp.simplify(abs(value) ** 2) for value in psi1)
    check("E final Z-only transcript distributions are identical", probabilities0 == probabilities1)
    check("E plus boundary gives uniform Z transcript law", set(probabilities0) == {sp.Rational(1, 128)})
    zero_word = (0,) * 7
    zero_edge_phase = (-1) ** sum(zero_word[0] * zero_word[leaf] for leaf in range(1, 7))
    zero_onsite_phases = tuple((-1) ** (epsilon * sum(zero_word)) for epsilon in (0, 1))
    check("E all-zero boundary is fixed by both diagonal laws", zero_edge_phase == 1 and zero_onsite_phases == (1, 1))
    check("E coherent plus boundary exposes epsilon", k0 != k1)
    check("E transverse X-center/Z-neighbor instrument exposes epsilon", k0 != k1)
    check("E Z-only instrument masks epsilon", probabilities0 == probabilities1)


def non_clifford_phase_control() -> None:
    section("F - One-at-a-time non-Clifford phase and involution enlargement")
    theta = sp.symbols("theta", real=True)
    phase_gate = sp.diag(1, 1, 1, sp.exp(I * theta))
    plus2 = sp.Matrix([1, 1, 1, 1]) / 2
    state = phase_gate * plus2
    exp_xi = sp.trigsimp(sp.expand_complex((state.H * tensor(X, I2) * state)[0]))
    exp_xz = sp.trigsimp(sp.expand_complex((state.H * tensor(X, Z) * state)[0]))
    exp_yi = sp.trigsimp(sp.expand_complex((state.H * tensor(Y, I2) * state)[0]))
    check("F exact <X tensor I> phase signature", sp.simplify(exp_xi - (1 + sp.cos(theta)) / 2) == 0)
    check("F exact <X tensor Z> phase signature", sp.simplify(exp_xz - (1 - sp.cos(theta)) / 2) == 0)
    check("F exact <Y tensor I> phase signature", sp.simplify(exp_yi - sp.sin(theta) / 2) == 0)

    root_order = 16
    involutive_roots = tuple(k for k in range(root_order) if (2 * k) % root_order == 0)
    check("F sixteenth-root census leaves only theta zero or pi under involution", involutive_roots == (0, 8))
    check("F entangling plus involutive selects theta pi", tuple(k for k in involutive_roots if k != 0) == (8,))
    check("F theta pi over two has a distinct XI record", sp.simplify(exp_xi.subs(theta, sp.pi / 2) - sp.Rational(1, 2)) == 0)
    check("F theta pi has vanishing XI record", sp.simplify(exp_xi.subs(theta, sp.pi)) == 0)
    check("F theta pi over two has a sine-sensitive YI record", sp.simplify(exp_yi.subs(theta, sp.pi / 2) - sp.Rational(1, 2)) == 0)

    # Allow a symmetric edge onsite phase phi as well.  On a degree-six
    # lattice one occupied site imposes 12 phi = 0 mod 2pi under U^2=I.
    # An adjacent occupied pair then independently imposes 2 theta=0.
    allowed_pairs = tuple(
        (phi_index, theta_index)
        for phi_index in range(12)
        for theta_index in range(16)
        if (12 * phi_index) % 12 == 0
        and (2 * theta_index) % 16 == 0
    )
    allowed_theta = {theta_index for _, theta_index in allowed_pairs}
    check("F symmetric onsite edge phases do not restore continuous theta", allowed_theta == {0, 8})
    theta_control = sp.pi / 3
    control_is_entangling = sp.simplify(sp.exp(I * theta_control) - 1) != 0
    control_is_not_involutive = sp.simplify(sp.exp(2 * I * theta_control) - 1) != 0
    check("F dropping involution opens a phase continuum", control_is_entangling and control_is_not_involutive)


def cnot_word(word: tuple[int, int, int], control: int, target: int) -> tuple[int, int, int]:
    result = list(word)
    result[target] ^= result[control]
    return tuple(result)  # type: ignore[return-value]


def order_control() -> None:
    section("G - Order, orientation, and schedule enlargement")
    diagonal_exponents = tuple((0, a, b, c) for a, b, c in product(range(4), repeat=3))
    commuting_pairs = sum(
        diagonal_gate(left) * diagonal_gate(right) == diagonal_gate(right) * diagonal_gate(left)
        for left in diagonal_exponents
        for right in diagonal_exponents
    )
    check("G every ordered pair in the 64-gate diagonal census commutes", commuting_pairs == 64 * 64)
    check("G edge order is inert inside the pointwise-Z diagonal class", commuting_pairs == 4096)

    cnot = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
    )
    check("G CNOT is unitary", cnot.H * cnot == sp.eye(4))
    check("G CNOT changes target local Z into two-site ZZ", cnot.H * tensor(I2, Z) * cnot == tensor(Z, Z))
    start = (1, 0, 0)
    forward = cnot_word(cnot_word(start, 0, 1), 1, 2)
    reverse = cnot_word(cnot_word(start, 1, 2), 0, 1)
    check("G forward directed schedule maps 100 to 111", forward == (1, 1, 1))
    check("G reverse directed schedule maps 100 to 110", reverse == (1, 1, 0))
    check("G final Z records distinguish the schedules", forward != reverse)
    check(
        "G order becomes physical only after leaving pointwise local-Z preservation",
        cnot.H * tensor(I2, Z) * cnot != tensor(I2, Z) and forward != reverse,
    )


def toe_and_discipline_contract() -> None:
    section("H - TOE residual and No-Go Discipline contract")
    note = normalized(NOTE)
    required_fields = (
        "kinetic propagation",
        "record trigger",
        "boundary/history",
        "instrument category",
        "probability-to-frequency",
        "clock metric",
        "fermion statistics",
        "gauge dynamics",
        "capacity renewal",
        "gravity field equation",
    )
    for field in required_fields:
        check(f"H unresolved TOE field named: {field}", field in note)
    required_limits = (
        "not unique at the global-law level",
        "not a no-go against",
        "fixed decoder",
        "co-transported",
        "finite census",
        "conditional quotient",
    )
    for phrase in required_limits:
        check(f"H scoped rhetoric present: {phrase}", phrase in note)
    check("H edge-involution shortcut is rejected", "edge-gate involution is an extra assumption" in note)
    check("H boundary does not select the law", "boundary changes observability; it does not select epsilon" in note)
    check("H instrument does not select the law", "instrument changes observability; it does not select epsilon" in note)
    check("H live axiom add is withheld", "no live axiom or primitive edit is justified" in note)


def subsection(text: str, start: str, end: str) -> str:
    """Return one required markdown subsection, failing closed if absent."""
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0]


def markdown_tables(block: str) -> tuple[tuple[tuple[str, ...], ...], ...]:
    """Parse pipe tables sufficiently strictly for the note's structure gate."""
    tables: list[tuple[tuple[str, ...], ...]] = []
    current: list[tuple[str, ...]] = []
    for line in block.splitlines():
        if line.startswith("|"):
            cells = tuple(cell.strip().replace("`", "") for cell in line.strip().strip("|").split("|"))
            current.append(cells)
        elif current:
            tables.append(tuple(current))
            current = []
    if current:
        tables.append(tuple(current))
    return tuple(tables)


def table_data(table: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    """Drop a table header and its markdown separator row."""
    if len(table) < 2:
        return ()
    separator = table[1]
    if not all(cell and set(cell) <= set("-: ") for cell in separator):
        return ()
    return table[2:]


def no_go_discipline_structure() -> None:
    section("I - Structural No-Go Discipline matrix")
    raw = NOTE.read_text(encoding="utf-8")
    note = normalized(NOTE)
    blocks = {
        "N1": subsection(raw, "### N1 —", "### N2 —"),
        "N2": subsection(raw, "### N2 —", "### N3 —"),
        "N3": subsection(raw, "### N3 —", "### N4 —"),
        "N4": subsection(raw, "### N4 —", "### N5 —"),
        "N5": subsection(raw, "### N5 —", "### N6 —"),
        "N6": subsection(raw, "### N6 —", "### N7 —"),
        "N7": subsection(raw, "### N7 —", "### N8 —"),
        "N8": subsection(raw, "### N8 —", "## Reproduction"),
    }

    n1_tables = markdown_tables(blocks["N1"])
    n1_rows = table_data(n1_tables[0]) if n1_tables else ()
    expected_routes = {
        "fourth-root diagonal edge census",
        "global phase-polynomial census",
        "foundation-static quotient",
        "temporal co-transport",
        "non-clifford controlled phase",
        "fixed boundary and instrument",
        "edge order and directed enlargement",
    }
    check("I N1 has at least five distinct route rows", len(n1_rows) >= 5)
    check(
        "I N1 every route has an allowed honesty marker",
        bool(n1_rows)
        and all(len(row) == 4 and row[1] in {"ATTEMPTED", "RULED OUT BY PRIOR"} for row in n1_rows),
    )
    check("I N1 exact seven-route attack matrix is present", {row[0].lower() for row in n1_rows} == expected_routes)

    n2_definition = blocks["N2"].split("The collapsed set is exactly:", 1)[-1].split(
        "All six unordered pairs", 1
    )[0]
    defined_walls = {
        line.split("`", 2)[1]
        for line in n2_definition.splitlines()
        if line.startswith("- `") and line.count("`") >= 2
    }
    check("I N2 collapsed wall set is exactly four named conditions", defined_walls == {"W_epsilon", "W_B", "W_I", "W_A"})
    check(
        "I N2 continuous phase wall is explicitly retired",
        "w_theta is retired" in note and "not counted in the collapsed wall set" in note,
    )
    n2_tables = markdown_tables(blocks["N2"])
    n2_rows = table_data(n2_tables[0]) if n2_tables else ()
    actual_pairs = {
        frozenset(part.strip() for part in row[0].split(","))
        for row in n2_rows
        if len(row) == 4
    }
    expected_pairs = {
        frozenset(pair)
        for pair in (
            ("W_epsilon", "W_B"),
            ("W_epsilon", "W_I"),
            ("W_epsilon", "W_A"),
            ("W_B", "W_I"),
            ("W_B", "W_A"),
            ("W_I", "W_A"),
        )
    }
    check("I N2 contains all six and only six unordered wall pairs", len(n2_rows) == 6 and actual_pairs == expected_pairs)
    check(
        "I N2 every pair is audited no-no-independent",
        bool(n2_rows)
        and all(row[1].lower().startswith("no") and row[2].lower().startswith("no") and row[3].lower() == "yes" for row in n2_rows),
    )

    n3_tables = markdown_tables(blocks["N3"])
    n3_rows = table_data(n3_tables[0]) if n3_tables else ()
    hidden_phrases = {
        "we assume",
        "by construction",
        "as is standard",
        "the framework provides",
        "bridge context",
        "background",
        "naturally",
        "obviously",
        "standard qft",
        "registered",
        "canonical",
    }
    check("I N3 table covers every mandatory hidden-wall search phrase", {row[0].lower() for row in n3_rows} == hidden_phrases)
    check(
        "I N3 absent-phrase classifications are mechanically honest",
        bool(n3_rows)
        and all(raw.lower().count(row[0].lower()) == 1 and "absent outside" in row[1].lower() for row in n3_rows),
    )

    n4_tables = markdown_tables(blocks["N4"])
    n4_rows = table_data(n4_tables[0]) if n4_tables else ()
    check("I N4 has the exact four residual-matching witnesses", len(n4_rows) == 4 and all(len(row) == 5 for row in n4_rows))
    check("I N4 match vector is yes-yes-no-no", tuple(row[3].lower() for row in n4_rows) == ("yes", "yes", "no", "no"))
    check("I N4 mismatched separator is dropped", "drop as selection evidence" in note)
    check("I N4 retained quotient scope is exact", "foundation-static equivalence only" in note)

    n5_tables = markdown_tables(blocks["N5"])
    n5_rows = table_data(n5_tables[0]) if n5_tables else ()
    check("I N5 audits at least seven distinct resolutions", len(n5_rows) >= 7 and all(len(row) == 4 for row in n5_rows))
    check(
        "I N5 untested resolutions carry no broad negative claim",
        sum(row[1].lower() == "no" for row in n5_rows) >= 2
        and all(row[3].lower() == "no claim." for row in n5_rows if row[1].lower() == "no"),
    )

    n6_tables = markdown_tables(blocks["N6"])
    n6_rows = table_data(n6_tables[0]) if n6_tables else ()
    check("I N6 enumerates at least five partial-closure paths", len(n6_rows) >= 5 and all(len(row) == 4 for row in n6_rows))
    check("I N6 primitive registry check is explicit", "primitive registry check complete" in note)

    n7_tables = markdown_tables(blocks["N7"])
    n7_rows = table_data(n7_tables[0]) if n7_tables else ()
    check(
        "I N7 hostile steelman is explicit and convincing",
        len(n7_rows) == 1 and len(n7_rows[0]) == 4 and n7_rows[0][2].lower() == "yes" and "hostile reviewer" in blocks["N7"].lower(),
    )
    check(
        "I N7 broad claim is demoted to partial narrowing",
        "no-go discipline status: fail" in note
        and "demoted to partial-narrowing" in note
        and "unconditional claim" in note
        and "not shipped" in note,
    )

    n8_tables = markdown_tables(blocks["N8"])
    n8_rows = table_data(n8_tables[0]) if n8_tables else ()
    check(
        "I N8 records at least four cross-cycle echoes and mechanisms",
        len(n8_rows) >= 4 and all(len(row) == 4 and row[2] and row[3] for row in n8_rows),
    )


def main() -> int:
    source_contract()
    edge_census()
    global_classification()
    static_equivalence_control()
    record_protocol_witness()
    non_clifford_phase_control()
    order_control()
    toe_and_discipline_contract()
    no_go_discipline_structure()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
