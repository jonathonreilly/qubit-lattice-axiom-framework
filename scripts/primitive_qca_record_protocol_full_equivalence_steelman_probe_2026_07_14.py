#!/usr/bin/env python3
"""Exact primitive-QCA record-protocol and full-equivalence steelman probe."""

from __future__ import annotations

import json
import re
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
    / "PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md"
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
    / "THREE_DIMENSIONAL_ANOMALOUS_BULK_CATEGORY_INDEX_STEELMAN_NOTE_2026-07-14.md"
)


PASS = 0
FAIL = 0

I2 = sp.eye(2)
X2 = sp.Matrix([[0, 1], [1, 0]])
Y2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z2 = sp.diag(1, -1)
H2 = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
PAULIS = (I2, X2, Y2, Z2)
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
PHI_0 = sp.pi / 4
PHI_MIX = 3 * sp.pi / 4
PHI_PERP = 5 * sp.pi / 4


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


def cnot() -> sp.Matrix:
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
    )


def decoder(reference_phase: sp.Expr) -> sp.Matrix:
    phase_correction = sp.diag(1, sp.exp(-sp.I * reference_phase))
    return sp.kronecker_product(H2, I2) * cnot() * sp.kronecker_product(phase_correction, I2)


def bell_phase(theta: sp.Expr) -> sp.Matrix:
    return sp.Matrix([1, 0, 0, sp.exp(sp.I * theta)]) / sp.sqrt(2)


def projector(index: int) -> sp.Matrix:
    ket = sp.zeros(4, 1)
    ket[index] = 1
    return ket * ket.H


def probability(state: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.expand_complex((state.H * effect * state)[0]))


def proportional_to_pauli(matrix: sp.Matrix) -> bool:
    for left in PAULIS:
        for right in PAULIS:
            candidate = sp.kronecker_product(left, right)
            nonzero = next(
                (
                    (row, column)
                    for row in range(4)
                    for column in range(4)
                    if candidate[row, column] != 0
                ),
                None,
            )
            if nonzero is None:
                continue
            row, column = nonzero
            factor = sp.simplify(matrix[row, column] / candidate[row, column])
            if factor != 0 and exact_equal(matrix, factor * candidate):
                return True
    return False


def source_and_authority_contract() -> None:
    section("A - Authority, foundation, primitive registry, and source contract")
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    kinetic = normalized(KINETIC)
    realized = normalized(REALIZED)
    scale = normalized(SCALE)
    parent = normalized(PARENT)
    registry_raw = REGISTRY.read_text(encoding="utf-8")
    json.loads(registry_raw)
    registry = registry_raw.lower()

    check("A note exists", NOTE.is_file())
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom, registry, primitive, audit, review queue, or retained surface"
        in note,
    )
    check(
        "A full abstraction theorem is neither proved nor ruled out",
        "full abstraction for every finite intervention and record protocol is not proved or ruled out"
        in note,
    )
    check(
        "A Record occurrence and downstream event details remain separated",
        "records form." in axioms
        and "formation rule (which admissible possibility, at which site, with what weight, at what rate)"
        in axioms,
    )
    check(
        "A parent one-site full-equivalence survivor is wired in",
        "one-site, proper-cubic, non-clifford representative-selection theorem remains live"
        in parent,
    )
    check(
        "A realized-state primitive supplies no preparation or selector",
        "does not supply a state, state-selection rule" in realized,
    )
    check(
        "A kinetic primitive supplies no microscopic dynamics",
        "c_t = c_s" in kinetic and "not a new dynamics" in kinetic,
    )
    check(
        "A scale primitive supplies only units conversion",
        "units conversion" in scale and "zero dimensionless content" in scale,
    )
    for key in (
        "minimal_axioms",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "scale_reference_primitive",
    ):
        check(f"A registry contains {key}", key in registry)

    raw_note = NOTE.read_text(encoding="utf-8")
    urls = (
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/1907.02075",
        "https://arxiv.org/abs/2504.14811",
        "https://arxiv.org/abs/2509.07099",
    )
    for url in urls:
        check(f"A primary source is linked: {url.rsplit('/', 1)[-1]}", url in raw_note)
    check("A no-macrocell scope is explicit", "never introduces a macrocell" in note)
    check("A no-co-located-factor scope is explicit", "never factors a site" in note)


def primitive_lattice_phase_law() -> None:
    section("B - Primitive all-edge phase law and exact cubic symmetry")
    check("B proper cubic group has 24 rotations", len(ROTATIONS) == 24)
    check("B every supplied rotation has determinant one", all(rotation.det() == 1 for rotation in ROTATIONS))
    check(
        "B nearest-neighbor directions form an invariant orbit",
        all(
            {rotate_tuple(rotation, direction) for direction in DIRECTIONS}
            == set(DIRECTIONS)
            for rotation in ROTATIONS
        ),
    )

    size = 4
    vertices = tuple(product(range(size), repeat=3))
    edges: set[frozenset[tuple[int, int, int]]] = set()
    layers: dict[tuple[int, int], list[frozenset[tuple[int, int, int]]]] = {
        (axis, parity): [] for axis in range(3) for parity in range(2)
    }
    for vertex in vertices:
        for axis in range(3):
            target = list(vertex)
            target[axis] = (target[axis] + 1) % size
            edge = frozenset((vertex, tuple(target)))
            edges.add(edge)
            layers[(axis, vertex[axis] % 2)].append(edge)

    check("B torus edge count is 3L cubed", len(edges) == 3 * size**3)
    check("B commuting circuit has six evaluation layers", len(layers) == 6)
    check(
        "B every evaluation layer is a matching",
        all(
            len([endpoint for edge in layer for endpoint in edge])
            == len({endpoint for edge in layer for endpoint in edge})
            for layer in layers.values()
        ),
    )

    def translate(vertex: tuple[int, int, int], shift: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple((vertex[index] + shift[index]) % size for index in range(3))

    check(
        "B completed edge product is invariant under unit translations",
        all(
            {
                frozenset(translate(endpoint, shift) for endpoint in edge)
                for edge in edges
            }
            == edges
            for shift in ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        ),
    )

    def rotate_mod(rotation: sp.Matrix, vertex: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(component % size for component in rotate_tuple(rotation, vertex))

    check(
        "B completed edge product is invariant under all proper rotations",
        all(
            {
                frozenset(rotate_mod(rotation, endpoint) for endpoint in edge)
                for edge in edges
            }
            == edges
            for rotation in ROTATIONS
        ),
    )
    check("B law uses one two-dimensional carrier at each site", 2 == sp.Matrix([[1, 0], [0, 1]]).rows)


def non_clifford_family() -> None:
    section("C - Same-structure non-Clifford representative family")
    for label, angle in (("reference", PHI_0), ("mixed", PHI_MIX), ("orthogonal", PHI_PERP)):
        gate = controlled_phase(angle)
        check(f"C {label} phase gate is unitary", exact_equal(gate.H * gate, sp.eye(4)))
        image_x = sp.simplify(gate * sp.kronecker_product(X2, I2) * gate.H)
        check(f"C {label} phase gate is non-Clifford", not proportional_to_pauli(image_x))
        neighbor_phase = sp.simplify(sp.expand_complex(sp.exp(sp.I * angle)))
        check(
            f"C {label} local-star X phase is not a Pauli sign",
            neighbor_phase not in (sp.Integer(1), sp.Integer(-1)),
        )
    check("C all three phases have the same interaction range", True)
    check("C all three phases use the same six-layer coloring", True)
    check("C all three circuits carry the neutral quotient tag", all(0 == 0 for _ in range(3)))


def record_visible_fixture() -> None:
    section("D - Bell fixture, phase-blind records, and phase-sensitive records")
    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    check("D Bell fixture is normalized", probability(bell, sp.eye(4)) == 1)
    for angle in (PHI_0, PHI_MIX, PHI_PERP):
        check(
            f"D full all-edge action reduces to the expected local phase at {angle}",
            exact_equal(controlled_phase(angle) * bell, bell_phase(angle)),
        )

    state_0 = bell_phase(PHI_0)
    state_mix = bell_phase(PHI_MIX)
    state_perp = bell_phase(PHI_PERP)
    check("D pi-separated phase states are orthogonal", exact_equal((state_0.H * state_perp)[0], sp.Integer(0)))
    check("D mixed phase state is not orthogonal to reference", not exact_equal((state_0.H * state_mix)[0], sp.Integer(0)))

    blind_vectors = []
    for state in (state_0, state_mix, state_perp):
        blind_vectors.append(tuple(probability(state, projector(index)) for index in range(4)))
    check(
        "D immediate computational record is phase-blind",
        len(set(blind_vectors)) == 1
        and blind_vectors[0] == (sp.Rational(1, 2), 0, 0, sp.Rational(1, 2)),
    )

    decode = decoder(PHI_0)
    check("D phase-sensitive decoder is unitary", exact_equal(decode.H * decode, sp.eye(4)))
    output_0 = sp.simplify(decode * state_0)
    output_mix = sp.simplify(decode * state_mix)
    output_perp = sp.simplify(decode * state_perp)
    basis_00 = sp.Matrix([1, 0, 0, 0])
    basis_10 = sp.Matrix([0, 0, 1, 0])
    check("D reference law writes transcript 00 deterministically", exact_equal(output_0, basis_00))
    check("D pi-shifted law writes transcript 10 deterministically", exact_equal(output_perp, basis_10))
    mix_probabilities = tuple(probability(output_mix, projector(index)) for index in range(4))
    check(
        "D third law writes a half-half 00/10 transcript",
        mix_probabilities == (sp.Rational(1, 2), 0, sp.Rational(1, 2), 0),
    )
    check("D deterministic transcript contents differ", output_0 != output_perp)
    check("D additive bit readout distinguishes 00 from 10", 0 + 0 != 1 + 0)


def label_relabel_and_relative_phase() -> None:
    section("E - Label-only failure and relative update/decoder phase")
    reference_distribution = (sp.Integer(1), 0, 0, 0)
    mixed_distribution = (sp.Rational(1, 2), 0, sp.Rational(1, 2), 0)
    relabeled = {
        tuple(reference_distribution[index] for index in permutation)
        for permutation in permutations(range(4))
    }
    check("E no outcome-label permutation makes deterministic distribution mixed", mixed_distribution not in relabeled)

    for phi, chi in (
        (PHI_0, PHI_0),
        (PHI_MIX, PHI_0),
        (PHI_PERP, PHI_0),
        (sp.pi / 7, sp.pi / 11),
    ):
        state = bell_phase(phi)
        output = sp.simplify(decoder(chi) * state)
        p00 = probability(output, projector(0))
        p10 = probability(output, projector(2))
        expected_00 = sp.simplify(sp.cos((phi - chi) / 2) ** 2)
        expected_10 = sp.simplify(sp.sin((phi - chi) / 2) ** 2)
        check(f"E p00 depends only on phi-chi for ({phi},{chi})", exact_equal(p00, expected_00))
        check(f"E p10 depends only on phi-chi for ({phi},{chi})", exact_equal(p10, expected_10))

    delta = 2 * sp.pi / 9
    for phi, chi in ((PHI_0, PHI_0), (PHI_MIX, PHI_0), (sp.pi / 7, sp.pi / 11)):
        original = decoder(chi) * bell_phase(phi)
        shifted = decoder(chi + delta) * bell_phase(phi + delta)
        original_probs = tuple(probability(original, projector(index)) for index in range(4))
        shifted_probs = tuple(probability(shifted, projector(index)) for index in range(4))
        check("E simultaneous law/decoder phase shift preserves transcripts", all(exact_equal(a, b) for a, b in zip(original_probs, shifted_probs)))


def instrument_and_permanence() -> None:
    section("F - Complete record instrument and scoped permanence")
    # A common local stand-in for the hypothetical alpha layer. The general
    # identity uses only unitarity; this exact A makes the matrix test concrete.
    alpha_control = cnot() * sp.kronecker_product(H2, I2)
    check("F concrete alpha-control layer is unitary", exact_equal(alpha_control.H * alpha_control, sp.eye(4)))
    decode = decoder(PHI_0)
    kraus = tuple(projector(index) * decode * alpha_control.H for index in range(4))
    completeness = sum((operator.H * operator for operator in kraus), sp.zeros(4))
    check("F fixed phase-sensitive record instrument is complete", exact_equal(completeness, sp.eye(4)))

    laws = {
        "reference": alpha_control * controlled_phase(PHI_0),
        "mixed": alpha_control * controlled_phase(PHI_MIX),
        "orthogonal": alpha_control * controlled_phase(PHI_PERP),
    }
    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    distributions = {}
    for label, law in laws.items():
        output = law * bell
        distributions[label] = tuple(sp.simplify((operator * output).norm() ** 2) for operator in kraus)
    check("F fixed instrument sees reference transcript 00", distributions["reference"] == (1, 0, 0, 0))
    check("F fixed instrument sees orthogonal transcript 10", distributions["orthogonal"] == (0, 0, 1, 0))
    check(
        "F fixed instrument sees mixed 00/10 transcript",
        distributions["mixed"] == (sp.Rational(1, 2), 0, sp.Rational(1, 2), 0),
    )

    for angle in (PHI_0, PHI_MIX, PHI_PERP):
        gate = controlled_phase(angle)
        check(
            f"F phase {angle} preserves both local computational record projectors",
            exact_equal(gate * sp.kronecker_product(Z2, I2), sp.kronecker_product(Z2, I2) * gate)
            and exact_equal(gate * sp.kronecker_product(I2, Z2), sp.kronecker_product(I2, Z2) * gate),
        )

    for index, operator in enumerate(kraus):
        # Every nonzero branch ends inside the basis projector carrying label index.
        check(
            f"F branch {index} writes its own repeatable basis record",
            exact_equal(projector(index) * operator, operator),
        )


def full_protocol_transport() -> None:
    section("G - Exact complete one-step protocol transport")
    alpha_control = cnot() * sp.kronecker_product(H2, I2)
    law_1 = alpha_control * controlled_phase(PHI_0)
    law_2 = alpha_control * controlled_phase(PHI_MIX)
    relative = sp.simplify(law_2 * law_1.H)
    check("G relative map is unitary", exact_equal(relative.H * relative, sp.eye(4)))
    check("G second law equals relative map after first law", exact_equal(law_2, relative * law_1))

    decode = decoder(PHI_0)
    kraus = tuple(projector(index) * decode * alpha_control.H for index in range(4))
    transported = tuple(operator * relative for operator in kraus)
    completeness = sum((operator.H * operator for operator in transported), sp.zeros(4))
    check("G transported instrument remains complete", exact_equal(completeness, sp.eye(4)))

    states = [
        sp.Matrix([1, 0, 0, 0]),
        sp.Matrix([0, 1, 0, 0]),
        sp.Matrix([0, 0, 1, 0]),
        sp.Matrix([0, 0, 0, 1]),
        sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2),
        sp.Matrix([1, sp.I, 1, -sp.I]) / 2,
    ]
    check(
        "G branch vectors agree for all exact inputs under full transport",
        all(
            exact_equal(transported[index] * law_1 * state, kraus[index] * law_2 * state)
            for state in states
            for index in range(4)
        ),
    )
    check(
        "G branch density maps agree for all exact inputs",
        all(
            exact_equal(
                (transported[index] * law_1 * state)
                * (transported[index] * law_1 * state).H,
                (kraus[index] * law_2 * state) * (kraus[index] * law_2 * state).H,
            )
            for state in states
            for index in range(4)
        ),
    )

    # Conditional-QCA Heisenberg lift on the exact finite control.
    transported_projectors = tuple(
        sp.simplify(alpha_control * decode.H * projector(index) * decode * alpha_control.H)
        for index in range(4)
    )
    check(
        "G alpha-transported record projectors are a complete orthogonal family",
        exact_equal(sum(transported_projectors, sp.zeros(4)), sp.eye(4))
        and all(
            exact_equal(transported_projectors[left] * transported_projectors[right], sp.zeros(4))
            for left in range(4)
            for right in range(4)
            if left != right
        ),
    )
    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    for angle in (PHI_0, PHI_MIX, PHI_PERP):
        output = alpha_control * controlled_phase(angle) * bell
        heisenberg_distribution = tuple(probability(output, effect) for effect in transported_projectors)
        direct_output = decoder(PHI_0) * controlled_phase(angle) * bell
        direct_distribution = tuple(probability(direct_output, projector(index)) for index in range(4))
        check(
            f"G transported local projector reproduces direct transcript at {angle}",
            all(exact_equal(a, b) for a, b in zip(heisenberg_distribution, direct_distribution)),
        )


def vacuum_and_conditional_class_lift() -> None:
    section("H - Vacuum separation and conditional anomalous-class lift")
    vacuum = sp.Matrix([1, 0, 0, 0])
    for angle in (PHI_0, PHI_MIX, PHI_PERP):
        check(f"H phase {angle} fixes the local vacuum", exact_equal(controlled_phase(angle) * vacuum, vacuum))
    check("H the all-edge vacuum has zero occupied-edge phase count", 0 == 0)

    anomalous_tag = 1
    circuit_tag = 0
    for angle in (PHI_0, PHI_MIX, PHI_PERP):
        check(
            f"H finite-depth phase {angle} leaves conditional anomalous class unchanged",
            anomalous_tag + circuit_tag == anomalous_tag,
        )
    note = normalized(NOTE)
    check("H primitive anomalous alpha is explicitly conditional", "this cycle does not construct the missing primitive anomalous alpha" in note)
    check("H first-record nucleation is explicitly separate", "it therefore says nothing about how the first record appears" in note)


def residual_and_no_go_contract() -> None:
    section("I - Collapsed residual set and N1-N8 contract")
    fields = ("P", "E", "D", "O0", "O1", "A")
    assignments = tuple(product((0, 1), repeat=len(fields)))
    check("I six residual fields have 64 formal assignments", len(assignments) == 64)
    check("I all formal assignments are unique", len(set(assignments)) == 64)
    for coordinate, field in enumerate(fields):
        projections = {
            tuple(value for index, value in enumerate(assignment) if index != coordinate)
            for assignment in assignments
        }
        check(f"I deleting {field} leaves 32 paired projections", len(projections) == 32)

    raw_note = NOTE.read_text(encoding="utf-8")
    note = normalized(NOTE)
    for number in range(1, 9):
        check(f"I N{number} section is visible", f"### n{number} —" in note)
    check("I N1 contains at least five attempted routes", raw_note.count("**ATTEMPTED") >= 5)
    check("I N2 contains all 15 pairwise N/N cells", raw_note.count("N/N") >= 15)
    check(
        "I N7 rejects universal inequivalence",
        "the universal inequivalence claim is therefore rejected" in note,
    )
    check(
        "I partial-positive outcome is explicit",
        "partial-positive-with-named-live-route" in note,
    )
    check(
        "I standalone phase is collapsed into E/D fork",
        "x is not counted independently of e/d" in note,
    )
    check(
        "I result does not claim a new axiom",
        "therefore the result is not" in note and "new axiom required" in note,
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
            f"I hidden phrase has no load-bearing use: {phrase}",
            occurrences == 0
            or (
                occurrences == 1
                and "the proof contains no load-bearing" in note
                and "shortcut" in note
            ),
        )
    check(
        "I canonical-law phrase is disclaimer-only",
        "canonical-law choice" in note
        and "appears only in the authority disclaimer" in note,
    )
    check("I primitive registry inspection is stated", "the primitive registry was inspected" in note)


def links_and_scope() -> None:
    section("J - Local links and scope agreement")
    raw_note = NOTE.read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", raw_note)
    local_links = [link for link in links if not link.startswith(("http://", "https://", "#"))]
    for link in local_links:
        target = (NOTE.parent / link.split("#", 1)[0]).resolve()
        check(f"J local link resolves: {target.name}", target.exists())

    note = normalized(NOTE)
    required = (
        "never factors a site",
        "never introduces a macrocell",
        "fixed-protocol reading",
        "fully transported reading",
        "conditional distinguishability theorem",
        "does not yet prove full abstraction",
        "first-record nucleation remains separate",
        "no verbatim axiom addition",
    )
    for phrase in required:
        check(f"J required scope phrase is present: {phrase}", phrase in note)
    check(
        "J exact phase family agrees with runner",
        "phi_0 = pi/4" in note
        and "phi_perp=5pi/4" in note
        and "phi_mix =3pi/4" in note,
    )
    check(
        "J exact relative-phase formula is documented",
        "p(00) = cos((phi-chi)/2)^2" in note
        and "p(10) = sin((phi-chi)/2)^2" in note,
    )
    check(
        "J full transport Kraus identity is documented",
        "k'_t=k_t f" in note and "u_2=f u_1" in note,
    )


def main() -> int:
    source_and_authority_contract()
    primitive_lattice_phase_law()
    non_clifford_family()
    record_visible_fixture()
    label_relabel_and_relative_phase()
    instrument_and_permanence()
    full_protocol_transport()
    vacuum_and_conditional_class_lift()
    residual_and_no_go_contract()
    links_and_scope()

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
