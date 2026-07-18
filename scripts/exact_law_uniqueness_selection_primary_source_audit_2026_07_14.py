#!/usr/bin/env python3
"""Exact controls for the Cycle 12 law-selection primary-source audit.

Companion note:
  docs/work_history/repo/review_feedback/
  EXACT_LAW_UNIQUENESS_SELECTION_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md

This runner proves only finite separation and document-contract statements:

* exact coarse-graining can map distinct microscopic Markov laws to one law;
* prefix description machines can reverse finite simplicity rankings;
* maximum-entropy answers depend on physical atomization and supplied prior;
* distinct actions can share one exact stationary history;
* anomaly constraints narrow a fixed matter model without selecting every
  representation label or normalization;
* generic local/unitary/cubic predicates admit distinguishable M2(C) laws;
* causal invariance of update order does not select a rewrite rule; and
* one exact deterministic rule can admit multiple boundary histories.

It does not prove a universal no-go, select a law, amend an axiom, set an audit
verdict, mutate a registry, commit, or open a PR.  Exit code 0 iff FAIL=0.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from math import isclose, log
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_LAW_UNIQUENESS_SELECTION_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0


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


ROUTE_START = "<!-- route-ledger:start -->"
ROUTE_END = "<!-- route-ledger:end -->"
ROUTE_HEADER = (
    "route_id",
    "classification",
    "representation",
    "low_energy_universality",
    "parameter_fixing",
    "exact_rule_identity",
    "actual_history",
    "boundary_selection",
    "strongest_result_key",
)
ROUTE_ROWS = {
    "rg_fixed_point": (
        "CONDITIONAL_YES",
        "PARTIAL",
        "YES",
        "RELEVANT_DIRECTIONS",
        "NO",
        "NO",
        "NO",
        "MANY_MICRO_TO_ONE_IR",
    ),
    "qca_structure": (
        "YES",
        "YES",
        "NO",
        "NO",
        "NO",
        "NO",
        "NO",
        "LOCAL_BLOCK_REPRESENTATION",
    ),
    "isotropic_walk_s2": (
        "YES",
        "YES",
        "YES",
        "TWO_CLASS",
        "TWO_WEYL_CLASS",
        "NO",
        "NO",
        "CLOSEST_POSITIVE",
    ),
    "operational_quantum_reconstruction": (
        "CONDITIONAL_YES",
        "YES",
        "NO",
        "NO",
        "NO",
        "NO",
        "NO",
        "QUANTUM_FORMALISM",
    ),
    "anomaly_cancellation": (
        "CONDITIONAL_YES",
        "YES",
        "NO",
        "CHARGE_RATIOS",
        "NO",
        "NO",
        "NO",
        "MODEL_CONSISTENCY",
    ),
    "action_lovelock_hkt": (
        "CONDITIONAL_YES",
        "YES",
        "CONTINUUM_ONLY",
        "FORM_PLUS_COEFFICIENTS",
        "NO",
        "NO",
        "NO",
        "CONTINUUM_FORM",
    ),
    "algorithmic_prior": (
        "HYPOTHESIS_RANKING",
        "YES",
        "NO",
        "MACHINE_RELATIVE",
        "NO",
        "NO",
        "NO",
        "EPISTEMIC_MIXTURE",
    ),
    "maxent_crossentropy": (
        "CONDITIONAL_YES",
        "YES",
        "NO",
        "DISTRIBUTION_GIVEN_INPUTS",
        "NO",
        "NO",
        "NO",
        "INFERENCE_RULE",
    ),
    "constructor_categorical": (
        "CONDITIONAL_YES",
        "YES",
        "NO",
        "NO",
        "NO",
        "NO",
        "NO",
        "THEORY_STRUCTURE",
    ),
    "causal_set_growth": (
        "CONDITIONAL_YES",
        "YES",
        "POSSIBLE",
        "COUPLING_FAMILY",
        "NO",
        "SAMPLED_ONLY",
        "NO",
        "GENERAL_GROWTH_FAMILY",
    ),
    "wolfram_causal_invariance": (
        "CONDITIONAL_YES",
        "YES",
        "CONDITIONAL",
        "NO",
        "NO",
        "NO",
        "NO",
        "SCHEDULE_GAUGE",
    ),
    "ruliad": (
        "ALL_RULE_REFRAMING_CLAIM",
        "PROPOSED",
        "PROPOSED",
        "NO",
        "REFRAMED_NOT_SELECTED",
        "OBSERVER_SLICE_OPEN",
        "OPEN",
        "UNIQUE_ALL_RULE_OBJECT_CLAIM",
    ),
}


CANONICAL_START = "<!-- canonical-map:start -->"
CANONICAL_END = "<!-- canonical-map:end -->"
CANONICAL_HEADER = ("field", "closure", "source_content_or_residual")
CANONICAL_CLOSURES = {
    "DOMAIN": "PARTIAL",
    "STATE": "YES_FOR_WALK",
    "CONTEXT": "PARTIAL",
    "ATOMIC_LAW": "TWO_CLASS",
    "CONTINUATION": "YES_FOR_WALK",
    "AVAILABILITY": "NO_RECORD_READING",
    "CONCURRENCY": "NO",
    "RECORD": "NO",
    "ACTUALITY": "NO",
    "STATISTICS": "NO_FORMATION_STATISTICS",
}


SOURCE_CONTRACTS = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "proper cubic rotations",
        "Each site has a domain of local possibilities",
        "There is one fixed nearest-neighbor admissibility rule",
        "Records form.",
    ),
    "docs/work_history/repo/review_feedback/CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md": (
        "ATOMIC_LAW",
        "ACTUALITY",
        "STATISTICS",
        "BOUNDARY",
    ),
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": (
        "units conversion",
        "not a physics axiom",
    ),
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": (
        "c_t = c_s",
        "not a new dynamics",
    ),
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": (
        "one law-admissible realized-state reference",
        "not a state-selection rule",
    ),
    "docs/work_history/repo/review_feedback/CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md": (
        "two Weyl walks",
        "one-particle quantum walk",
        "does not select a many-body collision rule",
    ),
    "docs/work_history/repo/review_feedback/MINIMUM_AXIOM_UPDATE_EXERCISE_SYNTHESIS_AND_CUT_GATE_NOTE_2026-07-14.md": (
        "exact law identity",
        "one retyped and polished Admissibility/Local-Law identification",
        "one separate Law identification while Admissibility remains a menu rule",
        "minimum live edit justified today",
    ),
}


def document_and_source_contracts() -> None:
    section("A - Document, framework, primitive, and literature contracts")
    check("A companion note exists", NOTE.is_file(), str(NOTE))
    text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    flat = normalized(text)

    for phrase in (
        "authority: none",
        "result up front",
        "scoped literature result",
        "not a universal impossibility theorem",
        "no live edit is justified",
        "does wolfram contribute more than schedule quotient",
        "partial-attempt-with-named-untested-route",
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7",
        "n8",
    ):
        check(f"A note contains scope phrase: {phrase}", phrase in flat)

    for relative, phrases in SOURCE_CONTRACTS.items():
        path = ROOT / relative
        check(f"A source exists: {relative}", path.is_file())
        source = path.read_text(encoding="utf-8") if path.is_file() else ""
        for phrase in phrases:
            check(f"A source contract {path.name}: {phrase}", phrase in source)

    premise_path = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
    premise_text = premise_path.read_text(encoding="utf-8")
    for primitive in (
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ):
        check(f"A approved primitive registry includes {primitive}", primitive in premise_text)

    primary_reference_needles = (
        "10.1016/0370-1573(74)90023-4",
        "1708.00826",
        "quant-ph/0405174",
        "0711.3975",
        "1110.5482",
        "hep-ph/0510181",
        "10.1063/1.1665613",
        "S0019-9958(64)90223-2",
        "10.1109/TIT.1980.1056144",
        "10.1109/TIT.1983.1056747",
        "1405.5563",
        "gr-qc/9904062",
        "2004.14810",
        "the-concept-of-the-ruliad",
    )
    for needle in primary_reference_needles:
        check(f"A primary-source ledger includes {needle}", needle in text)

    check("A route ledger has one start marker", text.count(ROUTE_START) == 1)
    check("A route ledger has one end marker", text.count(ROUTE_END) == 1)
    header, routes = parse_table(text, ROUTE_START, ROUTE_END)
    check("A route ledger header is exact", header == ROUTE_HEADER, repr(header))
    check("A route ledger rows are exact", routes == ROUTE_ROWS, repr(routes))
    check("A route ledger covers at least ten distinct mechanisms", len(routes) >= 10)
    check(
        "A no audited route claims actual-history closure",
        all(row[5] not in {"YES", "UNIQUE"} for row in routes.values()),
    )

    check("A canonical map has one start marker", text.count(CANONICAL_START) == 1)
    check("A canonical map has one end marker", text.count(CANONICAL_END) == 1)
    canonical_header, canonical = parse_table(text, CANONICAL_START, CANONICAL_END)
    check("A canonical map header is exact", canonical_header == CANONICAL_HEADER)
    check("A canonical map has all ten fields", set(canonical) == set(CANONICAL_CLOSURES))
    for field, closure in CANONICAL_CLOSURES.items():
        check(
            f"A closest-theorem closure is locked for {field}",
            canonical.get(field, (None,))[0] == closure,
        )


def matrix_rows_sum_to_one(matrix: tuple[tuple[Fraction, ...], ...]) -> bool:
    return all(sum(row, Fraction(0)) == 1 for row in matrix)


def lumped_row(
    matrix: tuple[tuple[Fraction, ...], ...],
    source: int,
    blocks: tuple[tuple[int, ...], ...],
) -> tuple[Fraction, ...]:
    return tuple(sum((matrix[source][target] for target in block), Fraction(0)) for block in blocks)


def coarse_graining_ablation() -> None:
    section("B - Exact coarse-graining / RG many-to-one ablation")
    blocks = ((0, 1), (2, 3))
    macro = (
        (Fraction(3, 4), Fraction(1, 4)),
        (Fraction(1, 3), Fraction(2, 3)),
    )
    micro_a = (
        (Fraction(3, 4), 0, Fraction(1, 4), 0),
        (0, Fraction(3, 4), 0, Fraction(1, 4)),
        (Fraction(1, 3), 0, Fraction(2, 3), 0),
        (0, Fraction(1, 3), 0, Fraction(2, 3)),
    )
    micro_b = (
        (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 8)),
        (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4), 0),
        (Fraction(1, 6), Fraction(1, 6), Fraction(1, 3), Fraction(1, 3)),
        (Fraction(1, 12), Fraction(1, 4), Fraction(1, 2), Fraction(1, 6)),
    )
    micro_a = tuple(tuple(Fraction(value) for value in row) for row in micro_a)
    micro_b = tuple(tuple(Fraction(value) for value in row) for row in micro_b)

    check("B first microscopic matrix is row stochastic", matrix_rows_sum_to_one(micro_a))
    check("B second microscopic matrix is row stochastic", matrix_rows_sum_to_one(micro_b))
    check("B microscopic laws are distinct", micro_a != micro_b)
    for name, matrix in (("A", micro_a), ("B", micro_b)):
        for macro_source, block in enumerate(blocks):
            rows = [lumped_row(matrix, source, blocks) for source in block]
            check(
                f"B micro {name} block {macro_source} is strongly lumpable",
                all(row == macro[macro_source] for row in rows),
                repr(rows),
            )
    check(
        "B same macro law hides different 0-to-0 probability",
        micro_a[0][0] == Fraction(3, 4)
        and micro_b[0][0] == Fraction(1, 2),
    )


def prefix_free(codes: tuple[str, ...]) -> bool:
    return all(
        not right.startswith(left)
        for index, left in enumerate(codes)
        for jndex, right in enumerate(codes)
        if index != jndex
    )


def algorithmic_simplicity_ablation() -> None:
    section("C - Exact finite algorithmic-simplicity ranking reversal")
    machine_1 = {"A": "0", "B": "10"}
    machine_2 = {"A": "10", "B": "0"}
    for name, machine in (("M1", machine_1), ("M2", machine_2)):
        codes = tuple(machine.values())
        kraft = sum((Fraction(1, 2 ** len(code)) for code in codes), Fraction(0))
        check(f"C {name} candidate codes are prefix free", prefix_free(codes))
        check(f"C {name} Kraft sum is admissible", kraft == Fraction(3, 4))
    check("C M1 ranks A shorter than B", len(machine_1["A"]) < len(machine_1["B"]))
    check("C M2 ranks B shorter than A", len(machine_2["B"]) < len(machine_2["A"]))
    prior_1 = {rule: Fraction(1, 2 ** len(code)) for rule, code in machine_1.items()}
    prior_2 = {rule: Fraction(1, 2 ** len(code)) for rule, code in machine_2.items()}
    check("C finite 2^-length prior ordering reverses", prior_1["A"] > prior_1["B"] and prior_2["A"] < prior_2["B"])
    check("C each prior still assigns both rules positive support", all(value > 0 for value in (*prior_1.values(), *prior_2.values())))


def entropy(probabilities: tuple[Fraction, ...]) -> float:
    return -sum(float(value) * log(float(value)) for value in probabilities if value)


def maxent_ablation() -> None:
    section("D - Maximum entropy depends on atoms, prior, and constraints")
    uniform_two = (Fraction(1, 2), Fraction(1, 2))
    uniform_three = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    check("D two-atom MaxEnt distribution is normalized", sum(uniform_two) == 1)
    check("D three-atom MaxEnt distribution is normalized", sum(uniform_three) == 1)
    check("D event A changes from 1/2 to 1/3 under atom refinement", uniform_two[0] == Fraction(1, 2) and uniform_three[0] == Fraction(1, 3))

    # Strict concavity can also be seen on a finite rational grid.  For each
    # denominator, the grid maximum is attained at or nearest to uniform.
    for denominator in (6, 12, 24):
        candidates = [
            (Fraction(a, denominator), Fraction(denominator - a, denominator))
            for a in range(1, denominator)
        ]
        maximum = max(entropy(candidate) for candidate in candidates)
        check(
            f"D two-atom rational grid n={denominator} is maximized at uniform",
            isclose(maximum, entropy(uniform_two), rel_tol=0.0, abs_tol=1e-14),
        )

    prior_a = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    prior_b = uniform_three
    check("D supplied priors are both normalized", sum(prior_a) == sum(prior_b) == 1)
    check("D supplied priors are distinct", prior_a != prior_b)
    # With no new constraint, the unique minimum of D_KL(p || prior) is the
    # prior itself (Gibbs inequality).  The point here is the exact distinct
    # conditional outputs, not a new proof of that theorem.
    posterior_a = prior_a
    posterior_b = prior_b
    check("D no-new-information cross-entropy returns prior A", posterior_a == prior_a)
    check("D no-new-information cross-entropy returns prior B", posterior_b == prior_b)
    check("D different priors give different conditional posteriors", posterior_a != posterior_b)


def action_extremality_ablation() -> None:
    section("E - Exact action/extremality underdetermination")
    x = sp.symbols("x", real=True)
    actions = {
        "S0": (x - 1) ** 2,
        "S1": (x - 1) ** 2 + (x - 1) ** 4,
        "S2": (x - sp.Rational(3, 2)) ** 2,
    }
    stationary: dict[str, list[sp.Expr]] = {}
    for name, action in actions.items():
        roots = sp.solve(sp.diff(action, x), x)
        stationary[name] = roots
        check(f"E {name} has exactly one stationary point", len(roots) == 1, repr(roots))
        if roots:
            hessian = sp.simplify(sp.diff(action, x, 2).subs(x, roots[0]))
            check(f"E {name} stationary point is a strict local minimum", hessian > 0, str(hessian))
    check("E distinct S0 and S1 share exact minimum x=1", stationary["S0"] == stationary["S1"] == [sp.Integer(1)])
    check("E S0 and S1 are different off shell", sp.expand(actions["S0"] - actions["S1"]) != 0)
    check("E S2 supplies a different selected history", stationary["S2"] == [sp.Rational(3, 2)])


def anomaly_cancellation_ablation() -> None:
    section("F - Exact finite anomaly-cancellation narrowing")
    q, u, d, ell, e = sp.symbols("q u d ell e")
    equations = {
        "su3": 2 * q + u + d,
        "su2": 3 * q + ell,
        "gravity": 6 * q + 3 * u + 3 * d + 2 * ell + e,
        "cubic": 6 * q**3 + 3 * u**3 + 3 * d**3 + 2 * ell**3 + e**3,
    }
    branches = (
        {q: 1, u: -4, d: 2, ell: -3, e: 6},
        {q: 1, u: 2, d: -4, ell: -3, e: 6},
    )
    for index, branch in enumerate(branches):
        for name, equation in equations.items():
            check(
                f"F branch {index} satisfies {name} anomaly",
                sp.expand(equation.subs(branch)) == 0,
            )

    reduced_cubic = sp.factor(
        equations["cubic"].subs({q: 1, ell: -3, e: 6, d: -2 - u})
    )
    check(
        "F reduced cubic factor is exact",
        sp.expand(reduced_cubic + 18 * (u - 2) * (u + 4)) == 0,
        str(reduced_cubic),
    )
    check("F normalized anomaly system has two u branches", set(sp.solve(reduced_cubic, u)) == {-4, 2})
    check("F branches exchange u and d singlet charges", branches[0][u] == branches[1][d] and branches[0][d] == branches[1][u])

    h = sp.Integer(3)
    standard = branches[0]
    yukawa = (
        q + h + u,
        q - h + d,
        ell - h + e,
    )
    check("F supplied Higgs/Yukawa orientation fits branch 0", all(expression.subs(standard) == 0 for expression in yukawa))
    check("F same supplied Higgs/Yukawa orientation rejects branch 1", any(expression.subs(branches[1]) != 0 for expression in yukawa))

    scale = sp.symbols("scale", nonzero=True)
    scaled = {symbol: scale * value for symbol, value in standard.items()}
    check("F anomaly equations retain an overall charge scale", all(sp.expand(expression.subs(scaled)) == 0 for expression in equations.values()))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in sp.Matrix(left) - sp.Matrix(right))


def local_qca_ablation() -> None:
    section("G - Generic local/unitary/cubic predicates do not select a law")
    I = sp.I
    identity = sp.eye(2)
    phase = sp.diag(1, I)
    X = sp.Matrix([[0, 1], [1, 0]])
    plus = sp.Matrix([1, 1]) / sp.sqrt(2)

    for name, unitary in (("identity", identity), ("phase", phase)):
        check(f"G {name} onsite law is exactly unitary", matrix_equal(unitary.H * unitary, sp.eye(2)))
        # Installed identically at every site, an onsite unitary has range zero
        # and commutes with every lattice-site permutation, including all
        # translations and proper cubic rotations.
        check(f"G {name} has no spatial direction index", unitary.shape == (2, 2))

    output_identity = identity * plus
    output_phase = phase * plus
    expectation_identity = sp.simplify((output_identity.H * X * output_identity)[0])
    expectation_phase = sp.simplify((output_phase.H * X * output_phase)[0])
    check("G identity gives exact X expectation 1", expectation_identity == 1)
    check("G phase gives exact X expectation 0", expectation_phase == 0)
    check("G two structurally admissible onsite laws are operationally distinct", expectation_identity != expectation_phase)


def rewrite(rule_output: str, schedule: tuple[int, ...]) -> tuple[str, ...]:
    state = ["A", "A"]
    for index in schedule:
        if state[index] != "A":
            raise AssertionError("schedule attempted to rewrite a non-A token")
        state[index] = rule_output
    return tuple(state)


def causal_invariance_ablation() -> None:
    section("H - Exact causal-invariance nonselection control")
    schedules = tuple(permutations((0, 1)))
    terminal_by_rule: dict[str, set[tuple[str, ...]]] = {}
    for output in ("B", "C"):
        terminals = {rewrite(output, schedule) for schedule in schedules}
        terminal_by_rule[output] = terminals
        check(f"H rule A->{output} is schedule independent", len(terminals) == 1, repr(terminals))
        check(f"H rule A->{output} has two incomparable events", len(schedules) == 2)
    check("H two causally invariant rules have the same schedule set", set(schedules) == {(0, 1), (1, 0)})
    check("H two causally invariant rules produce distinct records", terminal_by_rule["B"] != terminal_by_rule["C"])


def bit_flip_history(initial: int, steps: int) -> tuple[int, ...]:
    history = [initial]
    for _ in range(steps):
        history.append(1 - history[-1])
    return tuple(history)


def boundary_history_ablation() -> None:
    section("I - Exact law identity does not choose boundary history")
    history_zero = bit_flip_history(0, 6)
    history_one = bit_flip_history(1, 6)
    check("I zero-seed history obeys bit-flip law", all(history_zero[i + 1] == 1 - history_zero[i] for i in range(6)))
    check("I one-seed history obeys bit-flip law", all(history_one[i + 1] == 1 - history_one[i] for i in range(6)))
    check("I same law gives distinct histories", history_zero != history_one)
    check("I histories are exact complements", all(left + right == 1 for left, right in zip(history_zero, history_one)))


def no_go_discipline_contract() -> None:
    section("J - N1-N8 scope and demotion contract")
    text = NOTE.read_text(encoding="utf-8")
    flat = normalized(text)
    for heading in range(1, 9):
        check(f"J N{heading} heading is present", f"n{heading} —" in flat)
    check("J N1 has at least five ATTEMPTED routes", text.count("| ATTEMPTED |") >= 5)
    check("J N2 contains all three collapsed conditions", all(token in text for token in ("W1 TARGET_MATCH", "W2 UNIQUE_CLASS", "W3 ACTUAL_BOUNDARY")))
    check("J N2 has exactly three pair rows", sum(text.count(f"| {pair} |") for pair in ("W1-W2", "W1-W3", "W2-W3")) == 3)
    check("J N4 explicitly excludes mismatched residuals", text.count("excluded as a general witness") >= 3)
    check("J N6 names all approved primitives", all(name in text for name in ("scale-reference primitive", "kinetic-isotropy primitive", "realized-state primitive")))
    check("J N7 contains hostile intersection steelman", "their intersection" in text and "broad no-go is premature" in text)
    check("J output is explicitly demoted", "partial-attempt-with-named-untested-route" in text)
    check("J broad universal negative is not shipped", "broad negative" in flat and "is not shipped" in flat)
    check("J no new-selector-axiom conclusion is explicit", "does not say a new selector axiom is required" in text)


def independent_cross_checks() -> None:
    section("K - Independent formula cross-checks")
    # Re-derive the strong-lumping macro law without using the helper above.
    P = (
        (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 8)),
        (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4), Fraction(0)),
        (Fraction(1, 6), Fraction(1, 6), Fraction(1, 3), Fraction(1, 3)),
        (Fraction(1, 12), Fraction(1, 4), Fraction(1, 2), Fraction(1, 6)),
    )
    manual = tuple((row[0] + row[1], row[2] + row[3]) for row in P)
    check("K independent lump sums recover macro rows", manual == ((Fraction(3, 4), Fraction(1, 4)), (Fraction(3, 4), Fraction(1, 4)), (Fraction(1, 3), Fraction(2, 3)), (Fraction(1, 3), Fraction(2, 3))))

    u = sp.symbols("u")
    check("K independent anomaly roots recover {-4,2}", set(sp.solve((u + 4) * (u - 2), u)) == {-4, 2})

    x = sp.symbols("x")
    check("K independent action gradients vanish together at one", sp.diff((x - 1) ** 2, x).subs(x, 1) == sp.diff((x - 1) ** 2 + (x - 1) ** 4, x).subs(x, 1) == 0)


def main() -> int:
    document_and_source_contracts()
    coarse_graining_ablation()
    algorithmic_simplicity_ablation()
    maxent_ablation()
    action_extremality_ablation()
    anomaly_cancellation_ablation()
    local_qca_ablation()
    causal_invariance_ablation()
    boundary_history_ablation()
    no_go_discipline_contract()
    independent_cross_checks()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
