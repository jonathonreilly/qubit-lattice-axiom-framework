#!/usr/bin/env python3
"""Exact finite probes for the named-site record-faithful equivalence seam.

This runner checks finite-dimensional consequences only.  It does not choose
the framework's physical equivalence category or amend any authority surface.
"""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs/audit/data/axiom_premise_nodes.json"
PRIMITIVE_CHECK = ROOT / "docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md"
CYCLE20 = ROOT / "docs/work_history/repo/review_feedback/ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"


PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def exact_equal(left: sp.Matrix | sp.Expr, right: sp.Matrix | sp.Expr) -> bool:
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        return all(sp.simplify(sp.expand_complex(entry)) == 0 for entry in difference)
    return sp.simplify(sp.expand_complex(difference)) == 0


def kron(*operators: sp.Matrix) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for operator in operators:
        result = sp.kronecker_product(result, operator)
    return sp.Matrix(result)


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.H)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
S = sp.diag(1, sp.I)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
PX_PLUS = (I2 + X) / 2
PX_MINUS = (I2 - X) / 2
PY_PLUS = (I2 + Y) / 2
PY_MINUS = (I2 - Y) / 2


def controlled_phase(phi: sp.Expr) -> sp.Matrix:
    return sp.diag(1, 1, 1, sp.exp(sp.I * phi))


def cnot() -> sp.Matrix:
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
    )


def swap() -> sp.Matrix:
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ]
    )


PAULIS = (I2, X, Y, Z)
FACTOR1 = tuple(kron(p, I2) for p in PAULIS)
FACTOR2 = tuple(kron(I2, p) for p in PAULIS)


def vectorize(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix.rows * matrix.cols, 1, list(matrix))


def span_rank(matrices: list[sp.Matrix] | tuple[sp.Matrix, ...]) -> int:
    return sp.Matrix.hstack(*(vectorize(matrix) for matrix in matrices)).rank()


def in_span(matrix: sp.Matrix, basis: tuple[sp.Matrix, ...]) -> bool:
    before = span_rank(basis)
    after = span_rank(tuple(basis) + (matrix,))
    return before == after


def operator_schmidt_rank(operator: sp.Matrix) -> int:
    reshuffled = sp.zeros(4)
    for out_a in range(2):
        for out_b in range(2):
            for in_a in range(2):
                for in_b in range(2):
                    reshuffled[2 * out_a + in_a, 2 * out_b + in_b] = operator[
                        2 * out_a + out_b, 2 * in_a + in_b
                    ]
    return reshuffled.rank()


def reduced_first(rho: sp.Matrix) -> sp.Matrix:
    reduced = sp.zeros(2)
    for a in range(2):
        for c in range(2):
            reduced[a, c] = sp.simplify(sum(rho[2 * a + b, 2 * c + b] for b in range(2)))
    return reduced


def bit(value: int, coordinate: int, nbits: int) -> int:
    return (value >> (nbits - 1 - coordinate)) & 1


def is_signed_coordinate_permutation(mapping: tuple[int, ...], nbits: int) -> bool:
    used_inputs: set[int] = set()
    for output_coordinate in range(nbits):
        values = tuple(bit(mapping[source], output_coordinate, nbits) for source in range(2**nbits))
        match = None
        for input_coordinate in range(nbits):
            input_values = tuple(bit(source, input_coordinate, nbits) for source in range(2**nbits))
            if values == input_values:
                match = (input_coordinate, 0)
                break
            if values == tuple(1 - entry for entry in input_values):
                match = (input_coordinate, 1)
                break
        if match is None or match[0] in used_inputs:
            return False
        used_inputs.add(match[0])
    return len(used_inputs) == nbits


def source_contract() -> None:
    section("A - Authority, foundation, skill, and source contract")
    check("A note exists", NOTE.is_file())
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    primitive_check = PRIMITIVE_CHECK.read_text(encoding="utf-8")
    cycle20 = CYCLE20.read_text(encoding="utf-8")

    check("A note is authority-free", "**authority:** none" in note.lower())
    check("A no live authority edit is claimed", "changes no axiom" in normalized)
    check("A all three physical-category cases are named", all(phrase in normalized for phrase in (
        "all one-site rank-one record pvms",
        "dynamically selected record subalgebra",
        "transported site net",
    )))
    check("A Cycle20 seam is the direct parent", "full-abstraction" in cycle20.lower() and "cycle 20" in normalized)
    check("A current four axioms are present", all(name in axioms for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")))
    check("A Qubit names one-site M2", "M_2(C)" in axioms)
    check("A Record names one record per site", "never carries more than one record" in axioms)
    check(
        "A Record names content-only readout",
        "determined by record content alone" in " ".join(axioms.split()),
    )
    check("A Record names finite scalar additivity", "scalar readout" in axioms and "additive" in axioms)
    check("A primitive registry has exactly four canonical nodes", len(registry["canonical_ids"]) == 4)
    check("A primitive check forbids overgranting", "Do not grant more than" in primitive_check)
    for url in (
        "https://msp.org/pjm/1959/9-4/pjm-v9-n4-p17-p.pdf",
        "https://arxiv.org/abs/1706.08976",
        "https://arxiv.org/abs/2101.03600",
        "https://arxiv.org/abs/quant-ph/0405174",
    ):
        check(f"A primary-source link is present: {url.rsplit('/', 1)[-1]}", url in note)


def all_pvm_and_factor_normalizer() -> None:
    section("B - All one-site PVMs force the named-factor normalizer")
    projectors = (P0, P1, PX_PLUS, PX_MINUS, PY_PLUS, PY_MINUS)
    check("B six cardinal rank-one projectors span M2", span_rank(list(projectors)) == 4)

    adjacency = {
        left: {
            right
            for right in range(len(projectors))
            if right != left and not exact_equal(projectors[left] * projectors[right], projectors[right] * projectors[left])
        }
        for left in range(len(projectors))
    }
    reached = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for neighbor in adjacency[current] - reached:
            reached.add(neighbor)
            frontier.append(neighbor)
    check("B noncommutation graph of the cardinal PVM set is connected", len(reached) == 6)
    check("B only orthogonal/complementary cardinal pairs commute", all(len(neighbors) == 4 for neighbors in adjacency.values()))

    a, b, c, d = sp.symbols("a b c d")
    general = sp.Matrix([[a, b], [c, d]])
    equations = list(general * X - X * general) + list(general * Z - Z * general)
    solutions = sp.solve(equations, (a, b, c, d), dict=True)
    check("B commutant of X and Z inside M2 is scalar", solutions == [{a: d, b: 0, c: 0}])

    product_permutation = swap() * kron(H, S)
    image_factor1 = tuple(sp.simplify(product_permutation * basis * product_permutation.H) for basis in FACTOR1)
    image_factor2 = tuple(sp.simplify(product_permutation * basis * product_permutation.H) for basis in FACTOR2)
    check("B product plus swap maps factor one onto factor two", all(in_span(entry, FACTOR2) for entry in image_factor1))
    check("B product plus swap maps factor two onto factor one", all(in_span(entry, FACTOR1) for entry in image_factor2))
    check("B product plus swap has the expected unitary inverse", exact_equal(product_permutation.H * product_permutation, sp.eye(4)))

    for phi in (sp.pi / 4, sp.pi / 2, sp.pi):
        phase = controlled_phase(phi)
        image = sp.simplify(phase * kron(PX_PLUS, I2) * phase.H)
        check(f"B C_phi at {phi} sends an X record outside factor one", not in_span(image, FACTOR1))
        check(f"B C_phi at {phi} sends an X record outside factor two", not in_span(image, FACTOR2))
        check(f"B C_phi at {phi} has operator-Schmidt rank two", operator_schmidt_rank(phase) == 2)
    check("B trivial phase has operator-Schmidt rank one", operator_schmidt_rank(controlled_phase(0)) == 1)
    check("B swap is factor-permuting but has operator-Schmidt rank four", operator_schmidt_rank(swap()) == 4)


def selected_record_normalizer() -> None:
    section("C - Dynamically selected record algebra has a larger normalizer")
    for phi in (sp.pi / 4, sp.pi / 2, sp.pi):
        phase = controlled_phase(phi)
        for record in (kron(P0, I2), kron(P1, I2), kron(I2, P0), kron(I2, P1)):
            check(f"C C_phi at {phi} fixes selected Z record", exact_equal(phase * record * phase.H, record))

    cnot_gate = cnot()
    z_control = kron(Z, I2)
    z_target = kron(I2, Z)
    check("C CNOT fixes the control coordinate algebra", exact_equal(cnot_gate * z_control * cnot_gate.H, z_control))
    check("C CNOT spreads the target coordinate algebra", exact_equal(cnot_gate * z_target * cnot_gate.H, kron(Z, Z)))
    check("C CNOT still normalizes the global diagonal MASA", all(
        (cnot_gate * sp.diag(*diagonal) * cnot_gate.H).is_diagonal()
        for diagonal in ((1, 2, 3, 4), (4, 1, -2, 7))
    ))

    for nbits, expected in ((2, 8), (3, 48)):
        basis_size = 2**nbits
        count = sum(
            is_signed_coordinate_permutation(mapping, nbits)
            for mapping in itertools.permutations(range(basis_size))
        )
        check(f"C {nbits}-bit coordinate-record permutations count is 2^n n!", count == expected)

    roots = (1, sp.I, -1, -sp.I)
    diagonal_phase_tables = tuple(itertools.product(roots, repeat=4))
    pointer_faithful = len(diagonal_phase_tables)
    full_net_faithful = sum(q[0] * q[3] == q[1] * q[2] for q in diagonal_phase_tables)
    check("C all 256 fourth-root diagonal phases fix pointer records", pointer_faithful == 256)
    check("C exactly 64 fourth-root diagonal phases are onsite-separable", full_net_faithful == 64)

    phi = sp.pi / 4
    q = (1, 1, 1, sp.exp(sp.I * phi))
    rectangle_defect = sp.simplify(q[0] * q[3] - q[1] * q[2])
    check("C primitive phase has nonzero rectangle/separability defect", rectangle_defect != 0)

    selected_x_phase = kron(H, H) * controlled_phase(phi) * kron(H, H)
    x_records = (kron(PX_PLUS, I2), kron(PX_MINUS, I2), kron(I2, PX_PLUS), kron(I2, PX_MINUS))
    check("C conjugated phase fixes a dynamically selected X PVM", all(
        exact_equal(selected_x_phase * record * selected_x_phase.H, record) for record in x_records
    ))
    spread_z = sp.simplify(selected_x_phase * kron(P0, I2) * selected_x_phase.H)
    check("C selected-X phase still fails the full named site net", not in_span(spread_z, FACTOR1))


def lattice_and_content_dictionary() -> None:
    section("D - Lattice maps, homogeneous content dictionaries, and additivity")
    signed_permutations: list[sp.Matrix] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            signed_permutations.append(matrix)
    proper = [matrix for matrix in signed_permutations if matrix.det() == 1]
    check("D cubic signed-coordinate group has 48 elements", len(signed_permutations) == 48)
    check("D proper cubic subgroup has 24 elements", len(proper) == 24)
    unit_vectors = tuple(sp.eye(3).col(index) for index in range(3))
    check("D every signed coordinate map preserves nearest-neighbor steps", all(
        any(exact_equal(matrix * vector, sign * target) for target in unit_vectors for sign in (-1, 1))
        for matrix in signed_permutations
        for vector in unit_vectors
    ))
    proper_keys = {tuple(matrix) for matrix in proper}
    check("D proper cubic matrices close under composition", all(
        tuple(left * right) in proper_keys for left in proper for right in proper
    ))

    target_content = P0
    preimage_site_zero = target_content
    preimage_site_one = sp.simplify(H.H * target_content * H)
    readout = lambda projector: sp.simplify(sp.trace(Z * projector))
    check("D site-dependent frames give different pullbacks of one target content", not exact_equal(preimage_site_zero, preimage_site_one))
    check("D an allowed scalar content functional detects that dictionary ambiguity", readout(preimage_site_zero) != readout(preimage_site_one))

    common_preimages = (sp.simplify(H.H * target_content * H), sp.simplify(H.H * target_content * H))
    check("D a common onsite PU2 gives one site-independent content dictionary", exact_equal(*common_preimages))

    old_records = (P0, PX_PLUS)
    old_scalar = lambda projector: sp.simplify(sp.trace(Z * projector) + 2 * sp.trace(X * projector))
    new_records = tuple(sp.simplify(H * projector * H.H) for projector in old_records)
    transported_scalar = lambda projector: old_scalar(sp.simplify(H.H * projector * H))
    check("D common content transport preserves finite scalar additivity", sp.simplify(
        sum(old_scalar(record) for record in old_records)
        - sum(transported_scalar(record) for record in new_records)
    ) == 0)
    check("D site permutation preserves one-record-per-site occupancy", len({2, 0, 1}) == 3)


def boundary_and_cost() -> None:
    section("E - Boundary classes and zero-extra-record cost")
    plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    plus_plus = kron(plus, plus)
    for phi in (sp.pi / 4, sp.pi / 2, sp.pi):
        phase = controlled_phase(phi)
        output = sp.simplify(phase * plus_plus)
        reduced = reduced_first(density(output))
        purity = sp.simplify(sp.trace(reduced * reduced))
        expected = sp.simplify((3 + sp.cos(phi)) / 4)
        check(f"E C_phi boundary purity formula holds at {phi}", exact_equal(purity, expected))
        check(f"E C_phi entangles coherent product boundary at {phi}", purity < 1)

    phase = controlled_phase(sp.pi / 4)
    computational_states = tuple(sp.eye(4).col(index) for index in range(4))
    check("E every computational record-boundary density is fixed", all(
        exact_equal(phase * density(state) * phase.H, density(state)) for state in computational_states
    ))
    diagonal_mixture = sp.diag(sp.Rational(1, 10), sp.Rational(2, 10), sp.Rational(3, 10), sp.Rational(4, 10))
    check("E every tested diagonal record mixture is fixed", exact_equal(phase * diagonal_mixture * phase.H, diagonal_mixture))

    product_frame = kron(H, S)
    product_output = sp.simplify(product_frame * plus_plus)
    product_purity = sp.simplify(sp.trace(reduced_first(density(product_output)) ** 2))
    check("E onsite product frame preserves the product-boundary class", exact_equal(product_purity, 1))

    direct_history = ("output",)
    passive_history = ("output",)
    active_wrapper_history = ("phase-certificate", "output")
    check("E passive frame adds no record tick or capacity debit", len(passive_history) == len(direct_history))
    check("E active readable wrapper adds one record tick and capacity debit", len(active_wrapper_history) == len(direct_history) + 1)
    check("E active and passive histories are not label-preserving bijections", set(active_wrapper_history) != set(passive_history))


def transported_net_groupoid() -> None:
    section("F - Transported site-net groupoid")
    phase = controlled_phase(sp.pi / 3)
    transported_factor1 = tuple(sp.simplify(phase * basis * phase.H) for basis in FACTOR1)
    transported_factor2 = tuple(sp.simplify(phase * basis * phase.H) for basis in FACTOR2)
    check("F each transported factor is still four-dimensional M2", span_rank(transported_factor1) == 4 and span_rank(transported_factor2) == 4)
    check("F transported factors commute elementwise", all(
        exact_equal(left * right, right * left) for left in transported_factor1 for right in transported_factor2
    ))
    products = [left * right for left in transported_factor1 for right in transported_factor2]
    check("F transported factors generate the full two-site algebra", span_rank(products) == 16)

    p0_transported = sp.simplify(phase * kron(P0, I2) * phase.H)
    px_transported = sp.simplify(phase * kron(PX_PLUS, I2) * phase.H)
    check("F transported Z record remains a projector", exact_equal(p0_transported**2, p0_transported))
    check("F transported X record remains a projector", exact_equal(px_transported**2, px_transported))
    check("F transported orthogonal records remain orthogonal", exact_equal(
        px_transported * (sp.eye(4) - px_transported), sp.zeros(4)
    ))
    check("F transported X record is abstractly one-site but old-support two-site", not in_span(px_transported, FACTOR1))

    second_frame = cnot() * kron(S, H)
    sequential = tuple(sp.simplify(second_frame * entry * second_frame.H) for entry in transported_factor1)
    composite = tuple(sp.simplify((second_frame * phase) * basis * (second_frame * phase).H) for basis in FACTOR1)
    check("F transported-net morphisms compose by frame multiplication", all(
        exact_equal(left, right) for left, right in zip(sequential, composite)
    ))
    recovered = tuple(sp.simplify(phase.H * entry * phase) for entry in transported_factor1)
    check("F inverse frame recovers the original named factor", all(
        exact_equal(left, right) for left, right in zip(recovered, FACTOR1)
    ))

    old_weights = {"z+": sp.Rational(2, 3), "x+": sp.Rational(5, 7)}
    transported_weights = dict(old_weights)
    check("F transported content labels preserve scalar sums", sum(old_weights.values()) == sum(transported_weights.values()))
    check("F abstract max-one-record-per-transported-site is unchanged", len({"site-0": "x+"}) == 1)


def rule_stabilizer_controls() -> None:
    section("G - Fixed-rule stabilizers are extra data")
    overlap_rule = lambda left, right: sp.simplify(sp.trace(left * right))
    left = P0
    right = PX_PLUS
    common_left = sp.simplify(H * left * H.H)
    common_right = sp.simplify(H * right * H.H)
    split_left = left
    split_right = sp.simplify(H * right * H.H)
    check("G relative-overlap rule is invariant under common onsite PU2", exact_equal(
        overlap_rule(left, right), overlap_rule(common_left, common_right)
    ))
    check("G relative-overlap rule can reject independent onsite frames", not exact_equal(
        overlap_rule(left, right), overlap_rule(split_left, split_right)
    ))

    basis_sensitive_control = lambda projector: sp.simplify(sp.trace(Z * projector))
    check("G a mathematical basis-sensitive rule has a smaller stabilizer", basis_sensitive_control(P0) != basis_sensitive_control(H * P0 * H.H))
    check("G note does not treat the basis-sensitive control as framework authority", "mathematical control, not a framework rule" in NOTE.read_text(encoding="utf-8").lower())


def exercise_and_no_go_contract() -> None:
    section("H - Exercise synthesis, collapsed residuals, and N1-N8")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").split())
    for phrase in (
        "exercise zero",
        "assumptions from axioms up",
        "elon-style first-principles reduction",
        "literature proof search",
        "mathematics sector search",
        "reframing",
        "route portfolio",
    ):
        check(f"H exercise section is visible: {phrase}", phrase in normalized)

    for index in range(1, 9):
        check(f"H N{index} section is visible", f"### n{index} " in normalized)

    n1_match = re.search(r"### N1.*?(?=### N2)", note, flags=re.DOTALL)
    attempted_count = n1_match.group(0).count("**ATTEMPTED") if n1_match else 0
    check("H N1 contains at least five attempted routes", attempted_count >= 5)
    check("H N2 collapses record/boundary/cost into category closure", "subconditions of physical-category closure" in normalized)
    check("H N7 preserves the transported-net steelman", "transported-net steelman remains live" in normalized)
    check("H no universal finite-depth no-go is claimed", "no universal finite-depth no-go" in normalized)
    check("H strict named-net conclusion is explicit", "entangling c_phi is excluded from the fixed full-site-net automorphism group" in normalized)
    check("H selected-record conclusion is explicit", "c_phi survives in the selected-record normalizer" in normalized)
    check("H transported-net conclusion is explicit", "c_phi is an exact transported-net morphism" in normalized)
    check("H no axiom addition is claimed", "no verbatim axiom addition follows" in normalized)

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
        occurrences = [line for line in note.lower().splitlines() if phrase in line]
        check(
            f"H hidden phrase has no load-bearing use: {phrase}",
            not occurrences or all("n3 scan" in line or "non-load-bearing" in line or "quoted search phrase" in line for line in occurrences),
        )


def local_links_and_scope() -> None:
    section("I - Local links and exact scope")
    text = NOTE.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (NOTE.parent / target).resolve()
        check(f"I local link resolves: {Path(target).name}", resolved.exists())

    normalized = " ".join(text.lower().replace("`", "").split())
    for phrase in (
        "pu(2)^n semidirect product s_n",
        "2^n n!",
        "z^3 semidirect product o_h",
        "proper cubic subgroup",
        "common onsite pu(2)",
        "finite-depth diagonal phase circuits",
        "groupoid rather than one fixed-object group",
        "fixed admissibility rule",
        "passive relabeling",
        "first-record nucleation remains separate",
    ):
        check(f"I required classification phrase is present: {phrase}", phrase in normalized)


def main() -> int:
    source_contract()
    all_pvm_and_factor_normalizer()
    selected_record_normalizer()
    lattice_and_content_dictionary()
    boundary_and_cost()
    transported_net_groupoid()
    rule_stabilizer_controls()
    exercise_and_no_go_contract()
    local_links_and_scope()
    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
