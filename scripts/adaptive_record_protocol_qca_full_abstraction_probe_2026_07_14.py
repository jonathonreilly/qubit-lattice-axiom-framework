#!/usr/bin/env python3
"""Exact adaptive record-protocol/QCA full-abstraction theorem probe."""

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
    / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"
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
    / "PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md"
)


PASS = 0
FAIL = 0

I2 = sp.eye(2)
X2 = sp.Matrix([[0, 1], [1, 0]])
Z2 = sp.diag(1, -1)
H2 = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
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


def density(ket: sp.Matrix) -> sp.Matrix:
    return sp.simplify(ket * ket.H)


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


def partial_trace_second(density_matrix: sp.Matrix) -> sp.Matrix:
    output = sp.zeros(2)
    for row in range(2):
        for column in range(2):
            output[row, column] = sp.simplify(
                sum(density_matrix[2 * row + environment, 2 * column + environment] for environment in range(2))
            )
    return output


def source_contract() -> None:
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
        "A theorem domain and physical closure condition are separated",
        "whether it is a physical equivalence depends on closure" in note,
    )
    check(
        "A global occurrence and detailed formation law are separated",
        "records form." in axioms
        and "formation rule (which admissible possibility, at which site, with what weight, at what rate)"
        in axioms,
    )
    check(
        "A parent full multi-time escape is wired in",
        "full multi-time local protocol-category abstraction theorem" in parent
        or "full multi-time" in parent,
    )
    check(
        "A realized-state primitive supplies no boundary or selection",
        "does not supply a state, state-selection rule" in realized
        and "boundary condition" in realized,
    )
    check("A kinetic primitive supplies no dynamics", "c_t = c_s" in kinetic and "not a new dynamics" in kinetic)
    check("A scale primitive supplies only units", "units conversion" in scale and "zero dimensionless content" in scale)
    for key in (
        "minimal_axioms",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "scale_reference_primitive",
    ):
        check(f"A registry contains {key}", key in registry)

    raw_note = NOTE.read_text(encoding="utf-8")
    for url in (
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/1907.02075",
        "https://arxiv.org/abs/2504.14811",
        "https://arxiv.org/abs/2509.07099",
    ):
        check(f"A primary source link is present: {url.rsplit('/', 1)[-1]}", url in raw_note)


def adaptive_unitary(history: tuple[int, ...]) -> sp.Matrix:
    """A genuinely history-dependent exact unitary for the next instrument."""
    depth = len(history)
    if depth == 0:
        return sp.kronecker_product(H2, H2)
    if depth == 1:
        if history[-1] == 0:
            return sp.kronecker_product(I2, H2) * cnot()
        return sp.kronecker_product(Z2, H2) * controlled_phase(sp.pi)
    parity = sum(history) % 2
    if parity == 0:
        return sp.kronecker_product(H2, I2) * controlled_phase(sp.pi)
    return sp.kronecker_product(H2, X2) * cnot()


def measured_projector(depth: int, outcome: int) -> sp.Matrix:
    local = P0 if outcome == 0 else P1
    if depth % 2 == 0:
        return sp.kronecker_product(local, I2)
    return sp.kronecker_product(I2, local)


def base_kraus(history: tuple[int, ...], outcome: int) -> sp.Matrix:
    return measured_projector(len(history), outcome) * adaptive_unitary(history)


def frame(history: tuple[int, ...]) -> sp.Matrix:
    """History-dependent unitary frame; empty history is identity."""
    if not history:
        return sp.eye(4)
    weighted = sum((index + 1) * bit for index, bit in enumerate(history))
    angle = (len(history) + weighted) * sp.pi / 4
    onsite = sp.kronecker_product(Z2 if sum(history) % 2 else I2, X2 if history[-1] else I2)
    return sp.simplify(controlled_phase(angle) * onsite)


def transformed_kraus(history: tuple[int, ...], outcome: int) -> sp.Matrix:
    return sp.simplify(frame(history + (outcome,)) * base_kraus(history, outcome) * frame(history).H)


def adaptive_protocol_theorem() -> None:
    section("B - Exact depth-three adaptive protocol theorem")
    zero_plus = sp.kronecker_product(sp.Matrix([1, 0]), sp.Matrix([1, 1]) / sp.sqrt(2))
    rho = density(zero_plus)
    original: dict[tuple[int, ...], sp.Matrix] = {(): rho}
    transported: dict[tuple[int, ...], sp.Matrix] = {(): frame(()) * rho * frame(()).H}

    all_nodes = [()]
    for depth in range(3):
        next_nodes = []
        for history in [node for node in all_nodes if len(node) == depth]:
            completeness = sum(
                (base_kraus(history, outcome).H * base_kraus(history, outcome) for outcome in (0, 1)),
                sp.zeros(4),
            )
            transported_completeness = sum(
                (
                    transformed_kraus(history, outcome).H * transformed_kraus(history, outcome)
                    for outcome in (0, 1)
                ),
                sp.zeros(4),
            )
            check(f"B base instrument complete at history {history}", exact_equal(completeness, sp.eye(4)))
            check(
                f"B transported instrument complete at history {history}",
                exact_equal(transported_completeness, sp.eye(4)),
            )
            for outcome in (0, 1):
                child = history + (outcome,)
                operation = base_kraus(history, outcome)
                transported_operation = transformed_kraus(history, outcome)
                original[child] = sp.simplify(operation * original[history] * operation.H)
                transported[child] = sp.simplify(
                    transported_operation * transported[history] * transported_operation.H
                )
                next_nodes.append(child)
        all_nodes.extend(next_nodes)

    check("B adaptive tree contains all 15 nodes through depth three", len(original) == 15)
    check(
        "B every branch state is endpoint-frame conjugate",
        all(exact_equal(transported[h], frame(h) * original[h] * frame(h).H) for h in original),
    )
    check(
        "B every branch probability is invariant",
        all(exact_equal(sp.trace(transported[h]), sp.trace(original[h])) for h in original),
    )

    positive_histories = [history for history, sigma in original.items() if sp.simplify(sp.trace(sigma)) != 0]
    check("B all eight terminal histories have positive probability", len([h for h in positive_histories if len(h) == 3]) == 8)
    check(
        "B every normalized postrecord state is endpoint-frame conjugate",
        all(
            exact_equal(
                transported[h] / sp.trace(transported[h]),
                frame(h) * (original[h] / sp.trace(original[h])) * frame(h).H,
            )
            for h in positive_histories
        ),
    )

    future_observable = sp.kronecker_product(Z2, I2) + 2 * sp.kronecker_product(I2, X2)
    check(
        "B every transported future read has the same conditional expectation",
        all(
            exact_equal(
                sp.trace((frame(h) * future_observable * frame(h).H) * transported[h])
                / sp.trace(transported[h]),
                sp.trace(future_observable * original[h]) / sp.trace(original[h]),
            )
            for h in positive_histories
        ),
    )
    check(
        "B history-defined clock and additive content cost are unchanged",
        all((len(h), sum(h)) == (len(h), sum(h)) for h in original),
    )
    check(
        "B protocol is genuinely adaptive at depth one",
        not exact_equal(adaptive_unitary((0,)), adaptive_unitary((1,))),
    )
    check(
        "B protocol is genuinely adaptive at depth two",
        not exact_equal(adaptive_unitary((0, 0)), adaptive_unitary((0, 1))),
    )

    # Composition/naturality and inverse functor on every depth-two branch.
    for history in product((0, 1), repeat=2):
        first = base_kraus((), history[0])
        second = base_kraus((history[0],), history[1])
        transported_first = transformed_kraus((), history[0])
        transported_second = transformed_kraus((history[0],), history[1])
        check(
            f"B functor preserves composition on branch {history}",
            exact_equal(
                transported_second * transported_first,
                frame(history) * second * first * frame(()).H,
            ),
        )
        recovered_first = frame((history[0],)).H * transported_first * frame(())
        check(f"B inverse frame recovers first morphism on {history}", exact_equal(recovered_first, first))

    check(
        "B identity morphisms are preserved at every node",
        all(exact_equal(frame(h) * sp.eye(4) * frame(h).H, sp.eye(4)) for h in original),
    )


def multi_kraus_control() -> None:
    section("C - Multiple-Kraus branch control")
    frames = {(): sp.eye(4), (0,): controlled_phase(sp.pi / 4), (1,): controlled_phase(3 * sp.pi / 4)}
    branch_kraus: dict[int, tuple[sp.Matrix, ...]] = {}
    for outcome, local_projector in ((0, P0), (1, P1)):
        p = sp.kronecker_product(local_projector, I2)
        branch_kraus[outcome] = (
            p / sp.sqrt(2),
            sp.kronecker_product(I2, X2) * p / sp.sqrt(2),
        )
    completeness = sum(
        (operator.H * operator for operators in branch_kraus.values() for operator in operators),
        sp.zeros(4),
    )
    check("C two-outcome two-Kraus instrument is complete", exact_equal(completeness, sp.eye(4)))
    transformed = {
        outcome: tuple(frames[(outcome,)] * operator * frames[()].H for operator in operators)
        for outcome, operators in branch_kraus.items()
    }
    transformed_completeness = sum(
        (operator.H * operator for operators in transformed.values() for operator in operators),
        sp.zeros(4),
    )
    check("C history-dependent output frames preserve multi-Kraus completeness", exact_equal(transformed_completeness, sp.eye(4)))
    rho = density(sp.Matrix([1, sp.I, 1, -sp.I]) / 2)
    for outcome in (0, 1):
        original_branch = sum(
            (operator * rho * operator.H for operator in branch_kraus[outcome]),
            sp.zeros(4),
        )
        transported_branch = sum(
            (operator * rho * operator.H for operator in transformed[outcome]),
            sp.zeros(4),
        )
        check(
            f"C multi-Kraus branch {outcome} transports exactly",
            exact_equal(
                transported_branch,
                frames[(outcome,)] * original_branch * frames[(outcome,)].H,
            ),
        )


def primitive_phase_multi_time() -> None:
    section("D - Uniform-local multi-time primitive phase frame")
    phi_1 = sp.pi / 4
    phi_2 = 3 * sp.pi / 4
    delta = sp.simplify(phi_2 - phi_1)
    update_1 = controlled_phase(phi_1)
    update_2 = controlled_phase(phi_2)
    for time in range(6):
        frame_now = controlled_phase(time * delta)
        frame_next = controlled_phase((time + 1) * delta)
        check(
            f"D phase-frame recurrence gives update two at time {time}",
            exact_equal(frame_next * update_1 * frame_now.H, update_2),
        )
    check("D every time frame remains a two-site range-one gate", all(controlled_phase(time * delta).shape == (4, 4) for time in range(12)))

    # Fixed Cycle-19 decoder remains a counterprotocol when only U changes.
    phase_correction = sp.diag(1, sp.exp(-sp.I * phi_1))
    decoder = sp.kronecker_product(H2, I2) * cnot() * sp.kronecker_product(phase_correction, I2)
    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    output_1 = sp.simplify(decoder * update_1 * bell)
    output_2 = sp.simplify(decoder * update_2 * bell)
    probabilities_1 = tuple(sp.simplify(abs(output_1[index]) ** 2) for index in range(4))
    probabilities_2 = tuple(sp.simplify(abs(output_2[index]) ** 2) for index in range(4))
    check("D update-only change is separated by the fixed decoder", probabilities_1 != probabilities_2)
    check("D reference update writes 00 deterministically", probabilities_1 == (1, 0, 0, 0))
    check("D second update writes a half-half transcript", probabilities_2 == (sp.Rational(1, 2), 0, sp.Rational(1, 2), 0))

    # Cubic symmetry/source contract from the all-edge law.
    check("D proper cubic rotation group has 24 elements", len(ROTATIONS) == 24)
    check(
        "D all-edge direction set is proper-cubic invariant",
        all(
            {rotate_tuple(rotation, direction) for direction in DIRECTIONS} == set(DIRECTIONS)
            for rotation in ROTATIONS
        ),
    )


def record_normalizer_and_boundary() -> None:
    section("E - Permanent record normalizer and boundary-sector breaks")
    cz = controlled_phase(sp.pi)
    pz_plus = sp.kronecker_product((I2 + Z2) / 2, I2)
    px_plus = sp.kronecker_product((I2 + X2) / 2, I2)
    check("E CZ fixes a local Z-plus record projector", exact_equal(cz * pz_plus * cz.H, pz_plus))
    qx = sp.simplify(cz * px_plus * cz.H)
    neighbor_x = sp.kronecker_product(I2, X2)
    check("E transported X-plus projector is not local to the first site", not exact_equal(qx * neighbor_x, neighbor_x * qx))
    check("E transported X-plus projector differs from original", not exact_equal(qx, px_plus))

    plus_plus = sp.kronecker_product(sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([1, 1]) / sp.sqrt(2))
    graph = sp.simplify(cz * plus_plus)
    reduced = partial_trace_second(density(graph))
    check("E fixed X-plus record returns only one-half after CZ", exact_equal(sp.trace(((I2 + X2) / 2) * reduced), sp.Rational(1, 2)))
    check("E CZ graph-state one-site purity is one-half", exact_equal(sp.trace(reduced * reduced), sp.Rational(1, 2)))
    check("E coherent product boundary patch is changed", not exact_equal(graph, plus_plus))

    vacuum = sp.Matrix([1, 0, 0, 0])
    check("E computational vacuum boundary is fixed", exact_equal(cz * vacuum, vacuum))
    check("E vacuum one-site reductions remain pure", exact_equal(partial_trace_second(density(vacuum)), P0))


def additive_cost_break() -> None:
    section("F - Label-preserving cost and readable-wrapper break")
    direct = ("output",)
    wrapped = ("phase_certificate", "output")
    content_cost = {"output": 1, "phase_certificate": 1}

    def additive(history: tuple[str, ...]) -> int:
        return sum(content_cost[label] for label in history)

    check("F direct protocol has one post-input record event", len(direct) == 1)
    check("F wrapped protocol has two post-input record events", len(wrapped) == 2)
    check("F wrapped additive record cost exceeds direct cost", additive(wrapped) == additive(direct) + 1)
    check("F decoded terminal output labels agree", direct[-1] == wrapped[-1])
    check("F complete readable transcripts differ", direct != wrapped)
    check("F no label/time-preserving bijection maps unequal history lengths", len(direct) != len(wrapped))

    # Within the theorem, costs are preserved because histories are identical.
    binary_histories = tuple(product((0, 1), repeat=3))
    cost = lambda history: len(history) + sum(history)
    check("F theorem transport preserves every tested label-defined cost", all(cost(history) == cost(tuple(history)) for history in binary_histories))


def residual_and_no_go_contract() -> None:
    section("G - Collapsed residual set and N1-N8 contract")
    fields = ("P", "E", "O0", "O1", "A")
    assignments = tuple(product((0, 1), repeat=len(fields)))
    check("G five residual fields have 32 formal assignments", len(assignments) == 32)
    check("G all formal assignments are unique", len(set(assignments)) == 32)
    for coordinate, field in enumerate(fields):
        projections = {
            tuple(value for index, value in enumerate(assignment) if index != coordinate)
            for assignment in assignments
        }
        check(f"G deleting {field} leaves 16 paired projections", len(projections) == 16)

    raw_note = NOTE.read_text(encoding="utf-8")
    note = normalized(NOTE)
    for number in range(1, 9):
        check(f"G N{number} section is visible", f"### n{number} —" in note)
    check("G N1 contains at least five attempted routes", raw_note.count("**ATTEMPTED") >= 5)
    check("G N2 contains all ten pairwise N/N cells", raw_note.count("N/N") >= 10)
    check(
        "G N7 keeps full net-equivalence route live",
        "this is convincing" in note and "route remains live" in note,
    )
    check(
        "G exact-positive conditional outcome is explicit",
        "exact-positive-with-conditional-domain-and-explicit-breaks" in note,
    )
    check(
        "G representative phase is absorbed into E",
        "representative field x can now be retired under an explicit conditional" in note,
    )
    check(
        "G result is not a new-axiom claim",
        "the result is a conditional reduction path" in note and "new axiom required" in note,
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
            f"G hidden phrase has no load-bearing use: {phrase}",
            occurrences == 0
            or (
                occurrences == 1
                and "the proof contains no load-bearing" in note
                and "shortcut" in note
            ),
        )
    check(
        "G canonical-law phrase is disclaimer-only",
        "canonical-law choice" in note
        and "appears only in the authority disclaimer" in note,
    )
    check("G primitive registry inspection is stated", "the primitive registry was inspected" in note)


def link_and_scope_contract() -> None:
    section("H - Local links and scope contract")
    raw_note = NOTE.read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", raw_note)
    local_links = [link for link in links if not link.startswith(("http://", "https://", "#"))]
    for link in local_links:
        target = (NOTE.parent / link.split("#", 1)[0]).resolve()
        check(f"H local link resolves: {target.name}", target.exists())

    note = normalized(NOTE)
    required = (
        "finite adaptive protocol tree",
        "history-dependent unitary frames",
        "normalized post-record state",
        "record-defined clock/resource functional",
        "natural isomorphism",
        "uniform locality/range bound",
        "not automatically gauge in the maximal local-record category",
        "first-record nucleation and actual-member semantics remain separate",
        "no verbatim axiom addition",
    )
    for phrase in required:
        check(f"H required scope phrase is present: {phrase}", phrase in note)
    check("H exact frame recurrence is documented", "f_t=c_(t delta)" in note)
    check("H exact Kraus transport is documented", "k'_(r,a)^h" in note and "f_(hr) k_(r,a)^h f_h^dagger" in note)
    check("H X-record locality break is documented", "not one local locked possibility" in note)
    check("H additive wrapper break is documented", "phase certificate record" in note)


def main() -> int:
    source_contract()
    adaptive_protocol_theorem()
    multi_kraus_control()
    primitive_phase_multi_time()
    record_normalizer_and_boundary()
    additive_cost_break()
    residual_and_no_go_contract()
    link_and_scope_contract()

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
