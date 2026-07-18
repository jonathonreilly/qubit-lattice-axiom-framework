#!/usr/bin/env python3
"""Exact finite controls for a record-only global-history process law.

This runner checks Bell/CHSH, interference and history coarse-graining,
instrument context, identity-slot projective consistency, and documentation
contracts.  It does not select a physical law, amend the foundation, or issue
an audit verdict.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE29 = REVIEW / "RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md"

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
    section("A - Source and authority boundary")
    for path in (NOTE, AXIOMS, REALIZED, CYCLE29):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8")
    realized = REALIZED.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A note does not amend an axiom", "does not amend an axiom" in note)
    check("A exact state sentence is quoted", "a state is a configuration of records" in note)
    check("A live axiom says state is records", "A state is a configuration of records." in axioms)
    check("A live axiom denies dynamics", "Admissibility is not a dynamics axiom." in axioms)
    check("A realized primitive supplies no measure", "state-selection rule" in realized and "no averaging over alternatives" in realized)
    check("A no state amendment is forced", "no qualification amendment is forced" in note)
    check("A no live edit is authorized", "no live axiom or primitive edit is justified" in note)
    for source in (
        "https://doi.org/10.1103/physrevlett.23.880",
        "https://arxiv.org/abs/gr-qc/9507057",
        "https://arxiv.org/abs/0712.1325",
        "https://arxiv.org/abs/1512.00589",
        "https://arxiv.org/abs/1712.02589",
    ):
        check(f"A primary source cited: {source.rsplit('/', 1)[-1]}", source in note)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = sp.Matrix([1, 1]) / sp.sqrt(2)
KET_MINUS = sp.Matrix([1, -1]) / sp.sqrt(2)
P0 = KET0 * KET0.H
P1 = KET1 * KET1.H
RHO_PLUS = KET_PLUS * KET_PLUS.H
RHO_MINUS = KET_MINUS * KET_MINUS.H


def exact_trace(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(matrix))


def born(projector: sp.Matrix, rho: sp.Matrix) -> sp.Expr:
    return sp.simplify(exact_trace(projector * rho))


def output_probabilities(rho: sp.Matrix) -> tuple[sp.Expr, sp.Expr]:
    final = sp.simplify(H * rho * H.H)
    return born(P0, final), born(P1, final)


def bell_chsh_control() -> None:
    section("B - Bell/CHSH global record-transcript control")
    phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    rho = phi * phi.H
    alice = {0: Z, 1: X}
    bob = {0: (Z + X) / sp.sqrt(2), 1: (Z - X) / sp.sqrt(2)}
    check("B Bell state normalizes", exact_trace(rho) == 1)
    for name, observable in {"A0": Z, "A1": X, "B0": bob[0], "B1": bob[1]}.items():
        check(f"B {name} squares to identity", sp.simplify(observable * observable - I2) == sp.zeros(2))

    correlations: dict[tuple[int, int], sp.Expr] = {}
    table: dict[tuple[int, int], dict[tuple[int, int], sp.Expr]] = {}
    for x, y in product((0, 1), repeat=2):
        correlations[(x, y)] = sp.simplify(
            (phi.H * sp.kronecker_product(alice[x], bob[y]) * phi)[0]
        )
        probabilities: dict[tuple[int, int], sp.Expr] = {}
        for a, b in product((-1, 1), repeat=2):
            pa = (I2 + a * alice[x]) / 2
            pb = (I2 + b * bob[y]) / 2
            probabilities[(a, b)] = sp.simplify(
                exact_trace(sp.kronecker_product(pa, pb) * rho)
            )
            formula = sp.simplify((1 + a * b * correlations[(x, y)]) / 4)
            check(f"B context {(x, y)} outcome {(a, b)} has correlation form", sp.simplify(probabilities[(a, b)] - formula) == 0)
        table[(x, y)] = probabilities
        check(f"B context {(x, y)} normalizes", sp.simplify(sum(probabilities.values()) - 1) == 0)
        check(f"B context {(x, y)} is positive", all(p.is_nonnegative for p in probabilities.values()))
        for a in (-1, 1):
            marginal = sp.simplify(sum(p for (ao, _), p in probabilities.items() if ao == a))
            check(f"B Alice marginal at {(x, y)} a={a} is one-half", marginal == sp.Rational(1, 2))
        for b in (-1, 1):
            marginal = sp.simplify(sum(p for (_, bo), p in probabilities.items() if bo == b))
            check(f"B Bob marginal at {(x, y)} b={b} is one-half", marginal == sp.Rational(1, 2))

    expected = {
        (0, 0): 1 / sp.sqrt(2),
        (0, 1): 1 / sp.sqrt(2),
        (1, 0): 1 / sp.sqrt(2),
        (1, 1): -1 / sp.sqrt(2),
    }
    check("B exact correlation table matches target", all(sp.simplify(correlations[key] - value) == 0 for key, value in expected.items()))
    chsh = sp.simplify(correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)])
    check("B exact CHSH is two-root-two", sp.simplify(chsh - 2 * sp.sqrt(2)) == 0, f"S={chsh}")
    check("B operational table is no-signalling", all(
        sp.simplify(sum(table[(x, 0)][(a, b)] for b in (-1, 1)) - sum(table[(x, 1)][(a, b)] for b in (-1, 1))) == 0
        for x, a in product((0, 1), (-1, 1))
    ) and all(
        sp.simplify(sum(table[(0, y)][(a, b)] for a in (-1, 1)) - sum(table[(1, y)][(a, b)] for a in (-1, 1))) == 0
        for y, b in product((0, 1), (-1, 1))
    ))

    responses = tuple(product((-1, 1), repeat=2))
    local_values = tuple(
        aa[0] * bb[0] + aa[0] * bb[1] + aa[1] * bb[0] - aa[1] * bb[1]
        for aa in responses
        for bb in responses
    )
    check("B sixteen deterministic Bell-local vertices", len(local_values) == 16)
    check("B every Bell-local vertex has abs CHSH two", {abs(value) for value in local_values} == {2})
    weights = tuple(Fraction(index + 1, 136) for index in range(16))
    check("B displayed local mixture is normalized positive", sum(weights) == 1 and all(weight >= 0 for weight in weights))
    check("B displayed local mixture stays within two", abs(sum(weight * value for weight, value in zip(weights, local_values))) <= 2)


def interference_and_instruments() -> None:
    section("C - Interference, omission, and contextual instruments")
    coherent = RHO_PLUS
    dephased = sp.simplify(P0 * coherent * P0 + P1 * coherent * P1)
    coherent_probs = output_probabilities(coherent)
    dephased_probs = output_probabilities(dephased)
    check("C coherent preparation normalizes", exact_trace(coherent) == 1)
    check("C dephased preparation normalizes", exact_trace(dephased) == 1)
    check("C omission/identity gives a bright output", coherent_probs == (1, 0), str(coherent_probs))
    check("C measure-and-forget gives half-half", dephased_probs == (sp.Rational(1, 2), sp.Rational(1, 2)), str(dephased_probs))
    check("C omission is not measure-and-forget", coherent_probs != dephased_probs)

    joint_luders: dict[tuple[int, int], sp.Expr] = {}
    branches: list[sp.Matrix] = []
    for w, projector in enumerate((P0, P1)):
        branch = sp.simplify(projector * coherent * projector)
        branches.append(branch)
        for d, output_projector in enumerate((P0, P1)):
            joint_luders[(w, d)] = sp.simplify(exact_trace(output_projector * H * branch * H.H))
    check("C selective path instrument has four quarter-probability transcripts", set(joint_luders.values()) == {sp.Rational(1, 4)})
    check("C selective path transcripts normalize", sp.simplify(sum(joint_luders.values()) - 1) == 0)
    check("C branch maps sum to dephasing", sp.simplify(sum(branches, sp.zeros(2)) - dephased) == sp.zeros(2))
    for d in (0, 1):
        check(
            f"C outcome coarse-graining matches nonselective channel d={d}",
            sp.simplify(sum(joint_luders[(w, d)] for w in (0, 1)) - dephased_probs[d]) == 0,
        )

    # A second instrument has the same current Z-record probabilities but a
    # different conditional future: measure Z, then prepare |+> on each branch.
    joint_reprepare: dict[tuple[int, int], sp.Expr] = {}
    for w, projector in enumerate((P0, P1)):
        branch_probability = born(projector, coherent)
        branch = sp.simplify(branch_probability * RHO_PLUS)
        for d, output_projector in enumerate((P0, P1)):
            joint_reprepare[(w, d)] = sp.simplify(exact_trace(output_projector * H * branch * H.H))
    current_luders = tuple(sp.simplify(sum(joint_luders[(w, d)] for d in (0, 1))) for w in (0, 1))
    current_reprepare = tuple(sp.simplify(sum(joint_reprepare[(w, d)] for d in (0, 1))) for w in (0, 1))
    check("C two instruments have identical current outcome statistics", current_luders == current_reprepare == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("C reprepare instrument sends every branch to bright output", joint_reprepare == {(0, 0): sp.Rational(1, 2), (0, 1): 0, (1, 0): sp.Rational(1, 2), (1, 1): 0})
    check("C equal current records do not identify the future instrument", joint_luders != joint_reprepare)


def event_measure(matrix: sp.Matrix, event: tuple[int, ...]) -> sp.Expr:
    return sp.simplify(sum(matrix[i, j] for i in event for j in event))


def decoherence_functional_control() -> None:
    section("D - Decoherence functional and coarse-graining control")
    alpha = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2)])
    decoherence = sp.simplify(alpha * alpha.H)
    universe = tuple(range(4))
    out0 = (0, 1)
    out1 = (2, 3)
    check("D functional is Hermitian", decoherence.H == decoherence)
    check("D functional has rank one", decoherence.rank() == 1)
    check("D functional eigenvalues are one and three zeros", decoherence.eigenvals() == {sp.Integer(1): 1, sp.Integer(0): 3})
    check("D complete event normalizes", event_measure(decoherence, universe) == 1)
    check("D constructive output has measure one", event_measure(decoherence, out0) == 1)
    check("D destructive output has measure zero", event_measure(decoherence, out1) == 0)
    check("D every fine diagonal is one-quarter", {decoherence[i, i] for i in universe} == {sp.Rational(1, 4)})
    classical_out0 = sum(decoherence[i, i] for i in out0)
    check("D classical diagonal sum would give one-half", classical_out0 == sp.Rational(1, 2))
    check("D interference cross term supplies other half", sp.simplify(event_measure(decoherence, out0) - classical_out0) == sp.Rational(1, 2))

    grade_two_ok = True
    triple_count = 0
    for assignment in product(range(4), repeat=4):
        events = tuple(tuple(i for i, label in enumerate(assignment) if label == target) for target in (1, 2, 3))
        a, b, c = events
        lhs = event_measure(decoherence, tuple(sorted(a + b + c)))
        rhs = sp.simplify(
            event_measure(decoherence, tuple(sorted(a + b)))
            + event_measure(decoherence, tuple(sorted(a + c)))
            + event_measure(decoherence, tuple(sorted(b + c)))
            - event_measure(decoherence, a)
            - event_measure(decoherence, b)
            - event_measure(decoherence, c)
        )
        grade_two_ok &= sp.simplify(lhs - rhs) == 0
        triple_count += 1
    check("D grade-two sum rule holds for every labelled disjoint triple", grade_two_ok and triple_count == 256)

    coarse = sp.Matrix([[1, 1, 0, 0], [0, 0, 1, 1]])
    output_functional = sp.simplify(coarse * decoherence * coarse.T)
    recorded_path = sp.diag(*([sp.Rational(1, 4)] * 4))
    recorded_output = sp.simplify(coarse * recorded_path * coarse.T)
    check("D coherent coarse-graining is bright-dark", output_functional == sp.diag(1, 0))
    check("D recorded-path coarse-graining is half-half", recorded_output == sp.diag(sp.Rational(1, 2), sp.Rational(1, 2)))
    check("D recorded-path functional remains normalized", event_measure(recorded_path, universe) == 1)

    # A scalar quantum measure on one fixed two-path event algebra loses the
    # sign of an imaginary relative phase; the full functional does not.
    beta_plus = sp.Matrix([1, sp.I]) / sp.sqrt(2)
    beta_minus = sp.Matrix([1, -sp.I]) / sp.sqrt(2)
    d_plus = sp.simplify(beta_plus * beta_plus.H)
    d_minus = sp.simplify(beta_minus * beta_minus.H)
    subsets = ((), (0,), (1,), (0, 1))
    check("D opposite imaginary phases give distinct functionals", d_plus != d_minus)
    check("D opposite imaginary phases give the same fixed-algebra quantum measure", all(event_measure(d_plus, event) == event_measure(d_minus, event) for event in subsets))
    phase_gate = sp.diag(1, sp.I)
    out_plus = sp.simplify(H * phase_gate * beta_plus)
    out_minus = sp.simplify(H * phase_gate * beta_minus)
    probs_plus = tuple(sp.simplify(sp.conjugate(out_plus[i]) * out_plus[i]) for i in range(2))
    probs_minus = tuple(sp.simplify(sp.conjugate(out_minus[i]) * out_minus[i]) for i in range(2))
    check("D later phase context distinguishes the two functionals", probs_plus == (0, 1) and probs_minus == (1, 0), f"plus={probs_plus}, minus={probs_minus}")


def projective_process_control() -> None:
    section("E - Identity-slot containment and projective consistency")
    # The one-slot process is the linear map from an inserted operation to the
    # final record distribution.  Its no-slot member is defined by identity
    # insertion, as required by generalized process consistency.
    identity_output = output_probabilities(RHO_PLUS)
    no_slot_output = (sp.Integer(1), sp.Integer(0))
    check("E omitted-slot process equals identity insertion", identity_output == no_slot_output)

    branch_outputs: list[tuple[sp.Expr, sp.Expr]] = []
    for projector in (P0, P1):
        branch = sp.simplify(projector * RHO_PLUS * projector)
        branch_outputs.append(output_probabilities(branch))
    summed_instrument = tuple(sp.simplify(sum(row[d] for row in branch_outputs)) for d in (0, 1))
    dephased = sp.simplify(P0 * RHO_PLUS * P0 + P1 * RHO_PLUS * P1)
    nonselective_output = output_probabilities(dephased)
    check("E instrument outcomes sum to its nonselective channel", summed_instrument == nonselective_output == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("E nonselective measurement is not slot omission", nonselective_output != no_slot_output)
    check("E linearity holds under branch-map addition", all(sp.simplify(summed_instrument[d] - nonselective_output[d]) == 0 for d in (0, 1)))
    check("E identity and nonselective channels both normalize", sum(identity_output) == sum(nonselective_output) == 1)

    # Conditional Bell tables extend to a joint finite cylinder family after
    # assigning explicit setting-record weights.
    correlations = {(0, 0): 1 / sp.sqrt(2), (0, 1): 1 / sp.sqrt(2), (1, 0): 1 / sp.sqrt(2), (1, 1): -1 / sp.sqrt(2)}
    joint = {
        (x, y, a, b): sp.simplify((1 + a * b * correlations[(x, y)]) / 16)
        for x, y in product((0, 1), repeat=2)
        for a, b in product((-1, 1), repeat=2)
    }
    check("E joint setting-outcome history family normalizes", sp.simplify(sum(joint.values()) - 1) == 0)
    for x, y in product((0, 1), repeat=2):
        check(f"E marginal setting cylinder {(x, y)} has weight one-quarter", sp.simplify(sum(joint[(x, y, a, b)] for a, b in product((-1, 1), repeat=2)) - sp.Rational(1, 4)) == 0)
    for x, y, a in product((0, 1), (0, 1), (-1, 1)):
        check(f"E Alice setting-outcome cylinder {(x, y, a)} is one-eighth", sp.simplify(sum(joint[(x, y, a, b)] for b in (-1, 1)) - sp.Rational(1, 8)) == 0)
    for x, y, b in product((0, 1), (0, 1), (-1, 1)):
        check(f"E Bob setting-outcome cylinder {(x, y, b)} is one-eighth", sp.simplify(sum(joint[(x, y, a, b)] for a in (-1, 1)) - sp.Rational(1, 8)) == 0)


def record_sufficiency_control() -> None:
    section("F - Record sufficiency and ontology separation")
    plus_future = output_probabilities(RHO_PLUS)
    minus_future = output_probabilities(RHO_MINUS)
    check("F phase-opposite preparations have different exact futures", plus_future == (1, 0) and minus_future == (0, 1))
    coarse_records = {"plus": "open", "minus": "open"}
    check("F erased preparation label makes the current record fibre equal", len(set(coarse_records.values())) == 1)
    check("F equal coarse record fibre then has unequal futures", plus_future != minus_future)
    persistent_records = {"plus": "prep:+", "minus": "prep:-"}
    check("F persistent preparation records split the future-distinct fibre", len(set(persistent_records.values())) == 2)
    derived_calculator = {persistent_records["plus"]: plus_future, persistent_records["minus"]: minus_future}
    check("F fixed record decoder gives one future law per complete record", len(derived_calculator) == 2 and all(sum(probabilities) == 1 for probabilities in derived_calculator.values()))


def documentation_contract() -> None:
    section("G - Minimum data, placement, and no-go discipline")
    note = normalized(NOTE)
    required = (
        "normalized strongly positive decoherence functional",
        "positive process functional",
        "identity insertion",
        "measure-and-forget",
        "record-fibre future-equivalence",
        "law-side computational refinement",
        "no qualification amendment is forced",
        "global law specification",
        "local nearest-neighbor construction",
        "separate law placement",
        "quantum measure alone",
        "actual-history reference",
        "boundary",
        "decoder",
        "no record clause is forced",
    )
    for phrase in required:
        check(f"G note contains {phrase}", phrase in note)
    check("G global finite construction is not called a local derivation", "does not derive a homogeneous nearest-neighbor law" in note)
    check("G amplitudes are not silently made ontic", "amplitude is law data, not state content" in note)
    check("G actuality remains separate from measure", "the measure does not select the actual history" in note)
    check("G scalar quantum-measure limitation is narrow", "fixed coarse event algebra" in note and "unless supplemented" in note)
    for index in range(1, 9):
        check(f"G N{index} section exists", f"n{index} —" in note)
    check("G no-go discipline passes", "no-go-discipline status: pass" in note)


def main() -> int:
    source_contract()
    bell_chsh_control()
    interference_and_instruments()
    decoherence_functional_control()
    projective_process_control()
    record_sufficiency_control()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print("TYPE_GATE: a fixed global process/decoherence law can preserve record-only ontology; local nearest-neighbor generation remains unproved")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
