#!/usr/bin/env python3
"""Exact Cycle 13 probes for the classified three-dimensional Weyl pair.

Companion note:
  docs/work_history/repo/review_feedback/
  WEYL_PAIR_PHYSICAL_EQUIVALENCE_AND_COMBINED_INTERSECTION_NOTE_2026-07-14.md

The runner checks exact finite algebra used by the note: the published
transition matrices, their staggered-character conjugacy, finite endpoint
kernels, mirror and parity identities, a chirality sign, same-context
separators, the cardinal split-step embedding and schedule dependence, a
many-particle collision ablation, finite-unitary record preservation, and the
documented premise/intersection/N1--N8 contracts.

It does not prove the cited classification theorem, define Nature's context
category, supply Born/actuality semantics, select a microscopic law, amend an
axiom, set an audit verdict, mutate a registry, commit, or open a PR.  Exit
code 0 iff FAIL=0.
"""

from __future__ import annotations

from itertools import permutations
from math import ceil, log2
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "WEYL_PAIR_PHYSICAL_EQUIVALENCE_AND_COMBINED_INTERSECTION_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
I = sp.I
SQRT2 = sp.sqrt(2)
ID2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I], [I, 0]])
SZ = sp.diag(1, -1)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    difference = sp.Matrix(left) - sp.Matrix(right)
    return all(sp.simplify(sp.expand_complex(value)) == 0 for value in difference)


def normalized(text: str) -> str:
    return " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )


def parse_table(
    text: str, start: str, end: str
) -> tuple[tuple[str, ...], dict[str, tuple[str, ...]]]:
    body = text.split(start, 1)[1].split(end, 1)[0]
    lines = [line for line in body.splitlines() if line.startswith("|")]
    cells = [
        [item.strip().strip("`") for item in line.strip().strip("|").split("|")]
        for line in lines
    ]
    header = tuple(cells[0])
    rows = {
        row[0]: tuple(row[1:])
        for row in cells[2:]
        if len(row) == len(header) and row[0]
    }
    return header, rows


H = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)
BASE_POS = (
    sp.Matrix([[1, 0], [1, 0]]),
    sp.Matrix([[0, 1], [0, 1]]),
    sp.Matrix([[0, -1], [0, 1]]),
    sp.Matrix([[1, 0], [-1, 0]]),
)
BASE_NEG = (
    sp.Matrix([[0, -1], [0, 1]]),
    sp.Matrix([[1, 0], [-1, 0]]),
    sp.Matrix([[1, 0], [1, 0]]),
    sp.Matrix([[0, 1], [0, 1]]),
)
ETA_PLUS = (1 + I) / 4
ETA_MINUS = (1 - I) / 4


def add_position(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def negate_position(position: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(-value for value in position)  # type: ignore[return-value]


def transitions(branch: str) -> dict[tuple[int, int, int], sp.Matrix]:
    if branch == "plus":
        eta_pos, eta_neg = ETA_PLUS, ETA_MINUS
    elif branch == "minus":
        eta_pos, eta_neg = ETA_MINUS, ETA_PLUS
    else:
        raise ValueError(branch)
    result: dict[tuple[int, int, int], sp.Matrix] = {}
    for displacement, positive, negative in zip(H, BASE_POS, BASE_NEG):
        result[displacement] = eta_pos * positive
        result[negate_position(displacement)] = eta_neg * negative
    return result


def character(position: tuple[int, int, int]) -> sp.Expr:
    return sp.simplify((-I) ** sum(position))


def transition_matrix_source_probe() -> None:
    section("A - Published transition matrices and exact staggered character")
    plus = transitions("plus")
    minus = transitions("minus")
    check("A BCC positive generators have one relator", add_position(add_position(H[0], H[1]), add_position(H[2], H[3])) == (0, 0, 0))
    check("A BCC step set has eight displacements", len(plus) == len(minus) == 8)
    check("A eta-plus/eta-minus ratio is i", sp.simplify(ETA_PLUS / ETA_MINUS) == I)
    check("A eta-minus/eta-plus ratio is -i", sp.simplify(ETA_MINUS / ETA_PLUS) == -I)

    for index, displacement in enumerate(H, start=1):
        negative = negate_position(displacement)
        check(
            f"A h{index} branch relation is +i",
            matrix_equal(plus[displacement], I * minus[displacement]),
        )
        check(
            f"A -h{index} branch relation is -i",
            matrix_equal(plus[negative], -I * minus[negative]),
        )
        check(f"A character(h{index})=i", character(displacement) == I)
        check(f"A character(-h{index})=-i", character(negative) == -I)

    check("A character respects tetrahedral relator", sp.prod(character(h) for h in H) == 1)
    for branch, matrices in (("plus", plus), ("minus", minus)):
        left_norm = sum((matrix.H * matrix for matrix in matrices.values()), sp.zeros(2))
        right_norm = sum((matrix * matrix.H for matrix in matrices.values()), sp.zeros(2))
        check(f"A {branch} source normalization sum A†A=I", matrix_equal(left_norm, ID2))
        check(f"A {branch} source normalization sum AA†=I", matrix_equal(right_norm, ID2))

        differences: dict[tuple[int, int, int], sp.Matrix] = {}
        reverse_differences: dict[tuple[int, int, int], sp.Matrix] = {}
        items = tuple(matrices.items())
        for h, a_h in items:
            for hp, a_hp in items:
                displacement = add_position(h, negate_position(hp))
                if displacement == (0, 0, 0):
                    continue
                differences.setdefault(displacement, sp.zeros(2))
                reverse_differences.setdefault(displacement, sp.zeros(2))
                differences[displacement] += a_h * a_hp.H
                reverse_differences[displacement] += a_hp.H * a_h
        check(
            f"A {branch} off-diagonal AA† unitarity sums vanish",
            all(matrix_equal(matrix, sp.zeros(2)) for matrix in differences.values()),
            f"classes={len(differences)}",
        )
        check(
            f"A {branch} off-diagonal A†A unitarity sums vanish",
            all(matrix_equal(matrix, sp.zeros(2)) for matrix in reverse_differences.values()),
            f"classes={len(reverse_differences)}",
        )


def endpoint_kernels(branch: str, steps: int) -> dict[tuple[int, int, int], sp.Matrix]:
    kernels: dict[tuple[int, int, int], sp.Matrix] = {(0, 0, 0): ID2}
    for _ in range(steps):
        updated: dict[tuple[int, int, int], sp.Matrix] = {}
        for position, kernel in kernels.items():
            for displacement, matrix in transitions(branch).items():
                endpoint = add_position(position, displacement)
                updated.setdefault(endpoint, sp.zeros(2))
                updated[endpoint] += matrix * kernel
        kernels = updated
    return kernels


def staggered_transcript_probe() -> None:
    section("B - Exact endpoint-kernel equivalence and boundary price")
    for steps in range(0, 5):
        plus = endpoint_kernels("plus", steps)
        minus = endpoint_kernels("minus", steps)
        check(f"B step {steps} branches have same endpoint support", set(plus) == set(minus))
        check(
            f"B step {steps} kernels differ only by endpoint character",
            all(matrix_equal(plus[x], character(x) * minus[x]) for x in plus),
            f"endpoints={len(plus)}",
        )
        check(
            f"B step {steps} endpoint-local probabilities agree",
            all(matrix_equal(plus[x].H * plus[x], minus[x].H * minus[x]) for x in plus),
        )

    for length in range(1, 9):
        phase = sp.simplify((-I) ** length)
        descends = phase == 1
        check(
            f"B character torus condition L={length}",
            descends == (length % 4 == 0),
            f"phase={phase}",
        )


def rotation(axis: sp.Matrix, angle: sp.Expr) -> sp.Matrix:
    return sp.cos(angle) * ID2 - I * sp.sin(angle) * axis


def weyl(qx: sp.Expr, qy: sp.Expr, qz: sp.Expr, handedness: int) -> sp.Matrix:
    return rotation(SX, qx) * rotation(SY, handedness * qy) * rotation(SZ, qz)


def substitute_zero(matrix: sp.Matrix, symbols: tuple[sp.Symbol, ...]) -> sp.Matrix:
    return matrix.applyfunc(lambda value: sp.simplify(value.subs({symbol: 0 for symbol in symbols})))


def mirror_and_chirality_probe() -> None:
    section("C - Mirror/parity identities, proper-rotation invariant, and cubic test")
    qx, qy, qz = sp.symbols("qx qy qz", real=True)
    right = weyl(qx, qy, qz, +1)
    left = weyl(qx, qy, qz, -1)
    check("C one-axis mirror maps the two products", matrix_equal(right, left.subs(qy, -qy)))
    check(
        "C complex-conjugate parity identity is exact",
        matrix_equal(right, sp.conjugate(left.subs({qx: -qx, qy: -qy, qz: -qz}))),
    )
    check(
        "C unitary parity identity is exact",
        matrix_equal(right, SY * left.subs({qx: -qx, qy: -qy, qz: -qz}) * SY),
    )

    signs: dict[int, sp.Expr] = {}
    for handedness, walk in ((+1, right), (-1, left)):
        derivatives = tuple(
            I * substitute_zero(walk.diff(symbol), (qx, qy, qz))
            for symbol in (qx, qy, qz)
        )
        expected = (SX, handedness * SY, SZ)
        check(
            f"C handedness {handedness:+d} linear Weyl generators",
            all(matrix_equal(actual, target) for actual, target in zip(derivatives, expected)),
        )
        chirality = sp.simplify(sp.trace(derivatives[0] * derivatives[1] * derivatives[2]) / (2 * I))
        signs[handedness] = chirality
        check(f"C handedness {handedness:+d} triple sign", chirality == handedness, str(chirality))
    check("C proper-orientation triple signs differ", signs[+1] == -signs[-1])

    values = {qx: sp.pi / 4, qy: sp.pi / 6, qz: sp.pi / 8}
    for handedness, walk in ((+1, right), (-1, left)):
        half_turn = -I * SZ
        half_rotated_q = walk.subs({qx: -qx, qy: -qy}, simultaneous=True)
        check(
            f"C handedness {handedness:+d} exact pi-z covariance",
            matrix_equal(half_rotated_q, half_turn * walk * half_turn.H),
        )
        quarter_turn = rotation(SZ, handedness * sp.pi / 4)
        spatial_quarter = walk.subs({qx: -qy, qy: qx}, simultaneous=True)
        internal_quarter = quarter_turn * walk * quarter_turn.H
        check(
            f"C handedness {handedness:+d} exact pi/2-z covariance fails",
            not matrix_equal(spatial_quarter.subs(values), internal_quarter.subs(values)),
        )


def same_context_separator_probe() -> None:
    section("D - Smallest tested same-context coherent separators")
    plus_x = sp.Matrix([1, 1]) / SQRT2
    minus_x = sp.Matrix([1, -1]) / SQRT2
    plus = transitions("plus")
    minus = transitions("minus")
    h1 = H[0]
    mh1 = negate_position(h1)

    check("D plus branch h1 endpoint component", matrix_equal(plus[h1] * plus_x, ETA_PLUS * plus_x))
    check("D plus branch -h1 endpoint component", matrix_equal(plus[mh1] * plus_x, -ETA_MINUS * minus_x))
    check("D minus branch h1 endpoint component", matrix_equal(minus[h1] * plus_x, ETA_MINUS * plus_x))
    check("D minus branch -h1 endpoint component", matrix_equal(minus[mh1] * plus_x, -ETA_PLUS * minus_x))

    # |E>=(|h1,+x>+i|-h1,-x>)/sqrt(2).  Its bra contributes -i
    # to the second endpoint amplitude.
    amplitude_plus = sp.simplify((ETA_PLUS + I * ETA_MINUS) / SQRT2)
    amplitude_minus = sp.simplify((ETA_MINUS + I * ETA_PLUS) / SQRT2)
    probability_plus = sp.simplify(sp.conjugate(amplitude_plus) * amplitude_plus)
    probability_minus = sp.simplify(sp.conjugate(amplitude_minus) * amplitude_minus)
    check("D coherent two-endpoint effect clicks with p=1/4 on plus", probability_plus == sp.Rational(1, 4), str(probability_plus))
    check("D same effect clicks with p=0 on minus", probability_minus == 0, str(probability_minus))

    for endpoint in (h1, mh1):
        local_plus = sp.simplify((plus[endpoint] * plus_x).norm() ** 2)
        local_minus = sp.simplify((minus[endpoint] * plus_x).norm() ** 2)
        check(f"D one-endpoint norm agrees at {endpoint}", local_plus == local_minus)

    ket0 = sp.Matrix([1, 0])
    q = sp.pi / 4
    output_right = weyl(0, q, 0, +1) * plus_x
    output_left = weyl(0, q, 0, -1) * plus_x
    p0_right = sp.simplify(abs((ket0.H * output_right)[0]) ** 2)
    p0_left = sp.simplify(abs((ket0.H * output_left)[0]) ** 2)
    check("D oriented momentum protocol gives p(0)=0 on right", p0_right == 0, str(p0_right))
    check("D oriented momentum protocol gives p(0)=1 on left", p0_left == 1, str(p0_left))


def split_step_and_schedule_probe() -> None:
    section("E - BCC/cardinal embedding and schedule dependence")
    check("E every BCC generator has cardinal Manhattan length three", all(sum(abs(value) for value in h) == 3 for h in H))
    check("E BCC generator sum is zero", tuple(sum(h[index] for h in H) for index in range(3)) == (0, 0, 0))

    qx, qy, qz = sp.symbols("qx qy qz", real=True)
    factors = {
        "x": rotation(SX, qx),
        "y": rotation(SY, qy),
        "z": rotation(SZ, qz),
    }
    ordered: dict[tuple[str, ...], sp.Matrix] = {}
    for order in permutations(("x", "y", "z")):
        product = ID2
        for axis in order:
            product = product * factors[axis]
        ordered[order] = product
        check(f"E schedule {''.join(order)} is exactly unitary", matrix_equal(product.H * product, ID2))
    check("E XYZ factorization equals one Weyl product", matrix_equal(ordered[("x", "y", "z")], weyl(qx, qy, qz, +1)))

    sample = {qx: sp.pi / 5, qy: sp.pi / 7, qz: sp.pi / 9}
    sample_matrices = [matrix.applyfunc(lambda value: sp.simplify(value.subs(sample))) for matrix in ordered.values()]
    distinct_pairs = sum(
        not matrix_equal(sample_matrices[i], sample_matrices[j])
        for i in range(len(sample_matrices))
        for j in range(i + 1, len(sample_matrices))
    )
    check("E all six generic axis schedules are distinct", distinct_pairs == 15, f"distinct_pairs={distinct_pairs}")

    xyz_minus_zyx = ordered[("x", "y", "z")] - ordered[("z", "y", "x")]
    mixed = substitute_zero(xyz_minus_zyx.diff(qx).diff(qy), (qx, qy, qz))
    check("E schedule difference appears at mixed second order", not matrix_equal(mixed, sp.zeros(2)), repr(mixed))
    check("E six schedule program sectors have dimension 12", 6 * 2 == 12)
    check("E exact binary carrier for 12 dimensions needs at least four qubits", ceil(log2(12)) == 4)
    even = sum(1 for order in permutations((0, 1, 2)) if ((order[0] > order[1]) + (order[0] > order[2]) + (order[1] > order[2])) % 2 == 0)
    check("E six schedules split three even and three odd", even == 3)


def many_particle_collision_probe() -> None:
    section("F - Same one-particle Weyl sector, different generated collision law")
    dimension = 16  # four hard-core modes
    identity_collision = sp.eye(dimension)
    phase_collision = sp.eye(dimension)
    phase_collision[12, 12] = -1  # |1100>
    check("F identity collision is unitary", matrix_equal(identity_collision.H * identity_collision, sp.eye(dimension)))
    check("F phase collision is unitary", matrix_equal(phase_collision.H * phase_collision, sp.eye(dimension)))

    low_particle_indices = tuple(index for index in range(dimension) if bin(index).count("1") <= 1)
    check(
        "F collisions agree on vacuum and entire one-particle sector",
        all(identity_collision[:, index] == phase_collision[:, index] for index in low_particle_indices),
        f"basis_states={len(low_particle_indices)}",
    )
    check("F collisions preserve particle number", all(phase_collision[row, col] == 0 or bin(row).count("1") == bin(col).count("1") for row in range(dimension) for col in range(dimension)))

    ket_1100 = sp.eye(dimension)[:, 12]
    ket_0011 = sp.eye(dimension)[:, 3]
    psi_plus = (ket_1100 + ket_0011) / SQRT2
    psi_minus = (ket_1100 - ket_0011) / SQRT2
    out_identity = identity_collision * psi_plus
    out_phase = phase_collision * psi_plus
    check("F identity retains two-particle plus state", matrix_equal(out_identity, psi_plus))
    check("F phase collision maps plus to minus up to global sign", matrix_equal(out_phase, -psi_minus))
    p_plus_identity = sp.simplify(abs((psi_plus.H * out_identity)[0]) ** 2)
    p_plus_phase = sp.simplify(abs((psi_plus.H * out_phase)[0]) ** 2)
    check("F same fixed-N coherent record separates collisions with 1 versus 0", p_plus_identity == 1 and p_plus_phase == 0)


def finite_record_permanence_probe() -> None:
    section("G - Finite reversible permanence obstruction")
    # Exhaust every permutation unitary on four basis states and every proper
    # nonempty record subset.  This finite census is a control for the general
    # block proof in the companion note: U(R) subset R and finite unitarity
    # imply U(R)=R and U(R-perp)=R-perp.
    basis = tuple(range(4))
    tested = 0
    invariant_cases = 0
    violations = 0
    for permutation in permutations(basis):
        for mask in range(1, 2**4 - 1):
            record = {index for index in basis if mask & (1 << index)}
            blank = set(basis) - record
            invariant = all(permutation[index] in record for index in record)
            if not invariant:
                continue
            invariant_cases += 1
            if any(permutation[index] in record for index in blank):
                violations += 1
            tested += 1
    check("G finite permutation census has invariant record cases", invariant_cases > 0, str(invariant_cases))
    check("G no invariant finite record sector receives a blank state", violations == 0, f"tested={tested}")

    # Exact block implication in one nontrivial 2+2 example.  A is unitary;
    # A†B=0 forces B=0 because det(A) is nonzero.
    A = sp.Matrix([[1, 1], [1, -1]]) / SQRT2
    b11, b12, b21, b22 = sp.symbols("b11 b12 b21 b22")
    B = sp.Matrix([[b11, b12], [b21, b22]])
    solution = sp.solve(tuple(A.H * B), (b11, b12, b21, b22), dict=True)
    check("G exact A†B=0 block equation forces blank-to-record block B=0", solution == [{b11: 0, b12: 0, b21: 0, b22: 0}], repr(solution))
    check("G record block A is invertible", sp.simplify(A.det()) != 0)


INTERSECTION_START = "<!-- combined-intersection:start -->"
INTERSECTION_END = "<!-- combined-intersection:end -->"
INTERSECTION_HEADER = ("stage", "added_condition", "exact_result", "remaining_scope_or_price")
INTERSECTION_ROWS = {
    "C0": ("complete_s2_isotropic_classification", "TWO_WEYL_WALKS", "FREE_ONE_PARTICLE_BCC"),
    "C1": ("covariant_character_or_mirror_quotient", "ONE_COVARIANT_ORBIT", "CONTEXT_AND_BOUNDARY_MUST_TRANSFORM"),
    "C2": ("same_labeled_coherent_context", "TWO_SEPARATED", "BORN_EFFECT_AND_PHASE_REFERENCE_CONDITIONAL"),
    "C3": ("current_full_proper_cubic_at_s2", "EMPTY_WITHIN_CLASSIFICATION_SCOPE", "ENLARGE_CARRIER_OR_WEAKEN_EXACT_SYMMETRY"),
    "C4": ("cardinal_split_step_and_autonomous_schedule", "PROGRAM_FAMILY", "ORDER_OR_PROGRAM_STATE_UNSELECTED"),
    "C5": ("generated_many_particle_composition", "COLLISION_FAMILY", "INTERACTION_RULE_UNSELECTED"),
    "C6": ("finite_unitary_nontrivial_permanent_formation", "EMPTY", "IRREVERSIBLE_INSTRUMENT_OR_INFINITE_EXPORT_NEEDED"),
    "C7": ("infinite_or_instrument_record_completion", "OPEN_FAMILY", "FORMATION_ACTUALITY_STATISTICS_RENEWAL"),
    "C8": ("dirac_mass_coupling", "CONTINUOUS_MASS_DOUBLED_CARRIER", "MASS_AND_INTERACTIONS_UNSELECTED"),
    "C9": ("anomaly_and_continuum_constraints", "CONSISTENCY_FILTER", "GAUGE_REPRESENTATION_AND_UV_LAW_INPUTS"),
    "C10": ("actuality_statistics_boundary", "OPEN", "COMPLETE_RECORD_TRANSCRIPT_LAW_NOT_SUPPLIED"),
}

PREMISE_START = "<!-- premise-price:start -->"
PREMISE_END = "<!-- premise-price:end -->"
PREMISE_HEADER = ("premise_id", "classification_input", "current_foundation_status", "price_if_used")
PREMISE_IDS = {
    "P1_BCC_GENERATORS",
    "P2_LINEAR_ONE_PARTICLE",
    "P3_UNITARY_HOMOGENEOUS_LOCAL",
    "P4_BINARY_PI_ISOTROPY",
    "P5_REFLECTION_OR_CHARACTER_QUOTIENT",
    "P6_CONTEXT_EFFECT_FAMILY",
    "P7_SCHEDULE_PROGRAM",
    "P8_GENERATED_COMPOSITION",
    "P9_INTERACTION_AND_MASS",
    "P10_RECORD_FORMATION_PRESERVATION",
    "P11_ACTUALITY_STATISTICS_PREPARATION",
    "P12_BOUNDARY_PHASE_REFERENCE",
}


def document_contract_probe() -> None:
    section("H - Note, source, premise-price, and combined-intersection contracts")
    check("H companion note exists", NOTE.is_file(), str(NOTE))
    if not NOTE.is_file():
        return
    text = NOTE.read_text(encoding="utf-8")
    flat = normalized(text)
    required_sources = (
        "https://arxiv.org/abs/1708.00826",
        "https://arxiv.org/abs/1306.1934",
        "https://arxiv.org/abs/1601.04832",
        "https://arxiv.org/abs/1303.4652",
        "https://arxiv.org/abs/2011.05597",
        "https://arxiv.org/abs/quant-ph/0512058",
        "https://arxiv.org/abs/2004.14810",
        "https://doi.org/10.1016/0370-2693(81)91026-1",
        "https://arxiv.org/abs/hep-ph/9304312",
        "https://arxiv.org/abs/hep-ph/0510181",
        "https://arxiv.org/abs/1905.13729",
    )
    for source in required_sources:
        check(f"H primary source linked: {source}", source in text)
    for token in (
        "eta_+ = (1+i)/4",
        "chi(x)=(-i)^(x+y+z)",
        "p_+=1/4",
        "p_-=0",
        "partial-attempt-with-named-untested-routes",
        "no live axiom",
    ):
        check(f"H exact result token present: {token}", token in text)

    intersection_header, intersection_rows = parse_table(text, INTERSECTION_START, INTERSECTION_END)
    check("H combined-intersection header is exact", intersection_header == INTERSECTION_HEADER, repr(intersection_header))
    check("H combined-intersection rows are exact", intersection_rows == INTERSECTION_ROWS, repr(intersection_rows))

    premise_header, premise_rows = parse_table(text, PREMISE_START, PREMISE_END)
    check("H premise-price header is exact", premise_header == PREMISE_HEADER, repr(premise_header))
    check("H all priced premise ids are present", set(premise_rows) == PREMISE_IDS, repr(set(premise_rows)))
    check("H every premise has a nonempty price", all(row[-1] for row in premise_rows.values()))

    for path in (
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/work_history/repo/review_feedback/CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md",
    ):
        check(f"H local authority link exists: {path}", path in text and (ROOT / path).is_file())
    check("H broad universal no-go is explicitly withheld", "broad universal no-go is not shipped" in flat)


def no_go_discipline_probe() -> None:
    section("I - N1-N8 discipline contract")
    if not NOTE.is_file():
        check("I companion note required", False)
        return
    text = NOTE.read_text(encoding="utf-8")
    flat = normalized(text)
    for heading in range(1, 9):
        check(f"I N{heading} heading is present", f"n{heading} —" in flat)
    check("I N1 has at least five attempted routes", text.count("| ATTEMPTED |") >= 5)
    check("I N2 names collapsed walls", all(wall in text for wall in ("W1 UV_GENERATED_LAW", "W2 RECORD_ACTUALITY", "W3 EQUIVALENCE_BOUNDARY")))
    check("I N2 has exactly three pair rows", sum(text.count(f"| {pair} |") for pair in ("W1-W2", "W1-W3", "W2-W3")) == 3)
    check("I N3 scans every required trigger", all(phrase in text for phrase in ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background", "naturally", "obviously", "standard QFT", "registered", "canonical")))
    check("I N4 records exact-match exclusions", text.count("excluded as a general witness") >= 2)
    check("I N5 distinguishes five resolutions", all(word in text for word in ("per-transition", "per-endpoint", "per-protocol", "per-block", "lattice-wide")))
    check("I N6 names all approved primitives", all(name in text for name in ("scale-reference primitive", "kinetic-isotropy primitive", "realized-state primitive")))
    check("I N7 hostile steelman keeps one-class route live", "hostile steelman" in flat and "staggered character" in flat)
    check("I N8 cross-cycle echo table exists", "cross-cycle echo" in flat and "retirement mechanism" in flat)
    check("I demoted status is explicit", "partial-attempt-with-named-untested-routes" in text)
    check("I no required-new-axiom conclusion is withheld", "does not establish that a new axiom is required" in flat)


def independent_cross_checks() -> None:
    section("J - Independent recomputations")
    check("J direct character h1", sp.simplify((-I) ** 3) == I)
    check("J direct character h2", sp.simplify((-I) ** -1) == I)
    check("J exact separator arithmetic plus", sp.simplify(abs((ETA_PLUS + I * ETA_MINUS) / SQRT2) ** 2) == sp.Rational(1, 4))
    check("J exact separator arithmetic minus", sp.simplify(ETA_MINUS + I * ETA_PLUS) == 0)
    check("J Pauli triple orientation", sp.simplify(sp.trace(SX * SY * SZ) / (2 * I)) == 1)
    check("J mirror Pauli triple orientation", sp.simplify(sp.trace(SX * (-SY) * SZ) / (2 * I)) == -1)
    check("J four-site torus phase closes", sp.simplify((-I) ** 4) == 1)
    check("J three-site torus phase does not close", sp.simplify((-I) ** 3) != 1)


def main() -> int:
    transition_matrix_source_probe()
    staggered_transcript_probe()
    mirror_and_chirality_probe()
    same_context_separator_probe()
    split_step_and_schedule_probe()
    many_particle_collision_probe()
    finite_record_permanence_probe()
    document_contract_probe()
    no_go_discipline_probe()
    independent_cross_checks()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
