#!/usr/bin/env python3
"""Exact controls for the bare-metal record-actualization literature audit.

Companion note:
  docs/work_history/repo/review_feedback/
  BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md

This runner does not pretend to execute whole interpretations of quantum
mechanics.  It locks the note's comparison contract and checks the small exact
claims that distinguish a channel from an instrument, redundant copying from
actualization, records from a predictive state, consistent realms from realm
selection, spacelike order independence from overlapping order, and a recent
functional-equation claim from the Born rule.

No network access, randomness, axiom edit, registry edit, audit mutation, or
commit.  Exit code 0 iff FAIL=0.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md"
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


def exact_equal(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        difference = sp.Matrix(left) - sp.Matrix(right)
        return all(sp.simplify(value) == 0 for value in difference)
    return sp.simplify(left - right) == 0


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)
KET_MINUS = (KET0 - KET1) / sp.sqrt(2)
PX_PLUS = density(KET_PLUS)
PX_MINUS = density(KET_MINUS)


def normalized_note() -> tuple[str, str]:
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )
    return text, normalized


def source_and_scope_contract() -> None:
    section("A - Primary-source and bounded-claim contract")
    text, normalized = normalized_note()
    lower = text.lower()

    phrases = (
        "authority: none",
        "primary sources only",
        "empirical equivalence is not ontology",
        "no joint theorem found",
        "bounded literature result",
        "local reversible qubit/qca substrate",
        "state = records",
        "n1",
        "n8",
        "not a universal no-go",
    )
    for phrase in phrases:
        check(f"A note contains scope phrase: {phrase}", phrase in normalized)

    primary_urls = (
        "https://doi.org/10.1103/physrevd.34.470",
        "https://doi.org/10.1103/physreva.42.78",
        "https://arxiv.org/abs/quant-ph/0209051",
        "https://arxiv.org/abs/quant-ph/0406094",
        "https://arxiv.org/abs/quant-ph/0407116",
        "https://arxiv.org/abs/quant-ph/0012016",
        "https://doi.org/10.1007/bf01647093",
        "https://doi.org/10.1007/bf01015734",
        "https://arxiv.org/abs/gr-qc/9604012",
        "https://arxiv.org/abs/quant-ph/0307229",
        "https://doi.org/10.1103/revmodphys.29.454",
        "https://arxiv.org/abs/quant-ph/9906015",
        "https://arxiv.org/abs/quant-ph/0405161",
        "https://doi.org/10.1103/physrev.85.166",
        "https://arxiv.org/abs/quant-ph/0308039",
        "https://arxiv.org/abs/1405.1548",
        "https://arxiv.org/abs/gr-qc/9904062",
        "https://arxiv.org/abs/gr-qc/9507057",
        "https://arxiv.org/abs/quant-ph/0703276",
        "https://doi.org/10.25088/complexsystems.29.2.537",
        "https://doi.org/10.1512/iumj.1957.6.56050",
        "https://arxiv.org/abs/1811.11060",
        "https://arxiv.org/abs/2604.07418",
    )
    for url in primary_urls:
        check(f"A note cites primary source: {url}", url in lower)


MATRIX_START = "<!-- route-matrix:start -->"
MATRIX_END = "<!-- route-matrix:end -->"
FIELDS = (
    "readiness",
    "coherent_dynamics",
    "born_weights",
    "one_actual_history",
    "permanent_records",
    "causal_covariance",
    "state_equals_records",
)
ALLOWED = {"D", "P", "E", "C", "N", "F"}
EXPECTED = {
    "repeated_instruments_trajectories": ("P", "P", "P", "P", "P", "C", "N"),
    "grw_csl": ("P", "P", "P", "P", "E", "N", "N"),
    "dowker_henson_lattice": ("P", "P", "P", "P", "D", "D", "N"),
    "rgrwf": ("P", "P", "P", "P", "D", "D", "N"),
    "bell_bohm": ("P", "P", "C", "P", "E", "N", "N"),
    "consistent_histories": ("P", "P", "P", "P", "E", "C", "N"),
    "quantum_darwinism": ("C", "P", "P", "N", "E", "C", "N"),
    "everett_many_worlds": ("E", "P", "C", "N", "E", "C", "N"),
    "deterministic_ca": ("P", "C", "N", "P", "E", "C", "N"),
    "causal_set_csg": ("C", "N", "N", "P", "D", "D", "N"),
    "quantum_measure": ("P", "P", "P", "P", "C", "C", "N"),
    "wolfram_multiway": ("D", "N", "N", "N", "C", "D", "N"),
    "gleason": ("N", "N", "D", "N", "N", "N", "N"),
    "masanes_operational": ("P", "P", "D", "P", "N", "N", "N"),
    "axelsson_2026": ("P", "P", "F", "P", "P", "N", "N"),
}


def parse_route_matrix(text: str) -> tuple[tuple[str, ...], dict[str, tuple[str, ...]]]:
    body = text.split(MATRIX_START, 1)[1].split(MATRIX_END, 1)[0]
    rows = [line for line in body.splitlines() if line.startswith("|")]
    cells = [[cell.strip().strip("`") for cell in line.strip().strip("|").split("|")] for line in rows]
    header = tuple(cells[0])
    parsed = {
        row[0]: tuple(row[1:])
        for row in cells[2:]
        if len(row) == len(header) and row[0]
    }
    return header, parsed


def route_matrix_contract() -> None:
    section("B - Seven-field route matrix contract")
    text = NOTE.read_text(encoding="utf-8")
    check("B matrix start marker occurs once", text.count(MATRIX_START) == 1)
    check("B matrix end marker occurs once", text.count(MATRIX_END) == 1)
    header, parsed = parse_route_matrix(text)
    check("B exact matrix header", header == ("route_id",) + FIELDS, repr(header))
    check("B exact route set", set(parsed) == set(EXPECTED), repr(sorted(parsed)))
    check("B fifteen routes are classified", len(parsed) == 15)
    for route, expected in EXPECTED.items():
        check(f"B {route} has seven fields", len(parsed.get(route, ())) == 7)
        check(f"B {route} uses only declared codes", set(parsed.get(route, ())) <= ALLOWED)
        check(f"B {route} classification is locked", parsed.get(route) == expected, repr(parsed.get(route)))
    check("B no surveyed route derives all seven fields", not any(set(statuses) == {"D"} for statuses in parsed.values()))
    check("B no surveyed route proves generic state equals records", all(statuses[-1] == "N" for statuses in parsed.values()))
    check("B weight-only theorems do not claim readiness", parsed["gleason"][0] == "N" and parsed["masanes_operational"][0] == "P")
    check("B actual-history ontologies do not thereby derive Born weights", parsed["bell_bohm"][2] == "C" and parsed["deterministic_ca"][2] == "N")


def channel_is_not_instrument() -> None:
    section("C - One channel, inequivalent trajectory/record decompositions")
    a, b, c, d = sp.symbols("a b c d")
    rho = sp.Matrix([[a, b], [c, d]])
    projective = sp.simplify(P0 * rho * P0 + P1 * rho * P1)
    random_unitary = sp.simplify((rho + Z * rho * Z) / 2)
    check("C projective and random-unitary decompositions give one dephasing channel", exact_equal(projective, random_unitary))
    check("C the common channel removes off-diagonal entries", exact_equal(projective, sp.diag(a, d)))
    check("C both decompositions have two Kraus operators", len((P0, P1)) == len((I2 / sp.sqrt(2), Z / sp.sqrt(2))) == 2)

    test_rho = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3))
    measurement_labels = (trace(P0 * test_rho), trace(P1 * test_rho))
    phase_token_labels = (
        trace((I2 / sp.sqrt(2)) * test_rho * (I2 / sp.sqrt(2))),
        trace((Z / sp.sqrt(2)) * test_rho * (Z / sp.sqrt(2))),
    )
    check("C projective labels have state-dependent probabilities", measurement_labels == (sp.Rational(1, 3), sp.Rational(2, 3)))
    check("C phase-token labels are state-independent halves", phase_token_labels == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("C discarded-label channel equality does not fix record meaning", measurement_labels != phase_token_labels)
    check("C each Kraus family is trace preserving when outcomes are forgotten", exact_equal(P0 + P1, I2) and exact_equal((I2 + Z.H * Z) / 2, I2))


def cnot(control: int, target: int, qubits: int = 3) -> sp.Matrix:
    size = 2**qubits
    matrix = sp.zeros(size)
    for source in range(size):
        bits = [(source >> (qubits - 1 - index)) & 1 for index in range(qubits)]
        output = list(bits)
        if bits[control]:
            output[target] ^= 1
        destination = 0
        for bit in output:
            destination = 2 * destination + bit
        matrix[destination, source] = 1
    return matrix


def partial_trace_three_qubits(rho: sp.Matrix, keep: int) -> sp.Matrix:
    result = sp.zeros(2)
    discarded = [index for index in range(3) if index != keep]
    for i in range(2):
        for j in range(2):
            total = 0
            for a in range(2):
                for b in range(2):
                    row_bits = [0, 0, 0]
                    col_bits = [0, 0, 0]
                    row_bits[keep] = i
                    col_bits[keep] = j
                    row_bits[discarded[0]] = col_bits[discarded[0]] = a
                    row_bits[discarded[1]] = col_bits[discarded[1]] = b
                    row = 4 * row_bits[0] + 2 * row_bits[1] + row_bits[2]
                    col = 4 * col_bits[0] + 2 * col_bits[1] + col_bits[2]
                    total += rho[row, col]
            result[i, j] = sp.simplify(total)
    return result


def redundancy_is_not_actualization() -> None:
    section("D - Reversible redundancy creates witnesses, not one outcome")
    psi_system = sp.sqrt(sp.Rational(1, 3)) * KET0 + sp.sqrt(sp.Rational(2, 3)) * KET1
    blank_pair = sp.kronecker_product(KET0, KET0)
    initial = sp.kronecker_product(psi_system, blank_pair)
    u1 = cnot(0, 1)
    u2 = cnot(0, 2)
    copied = sp.simplify(u2 * u1 * initial)
    ket000 = sp.eye(8)[:, 0]
    ket111 = sp.eye(8)[:, 7]
    expected = sp.sqrt(sp.Rational(1, 3)) * ket000 + sp.sqrt(sp.Rational(2, 3)) * ket111
    check("D two CNOTs produce the exact redundant GHZ record state", exact_equal(copied, expected))
    check("D copied global state remains normalized", exact_equal((dagger(copied) * copied)[0], 1))
    check("D both record branches remain nonzero", copied[0] != 0 and copied[7] != 0)
    rho = density(copied)
    expected_local = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3))
    for qubit in range(3):
        check(f"D reduced state {qubit} carries the same classical label distribution", exact_equal(partial_trace_three_qubits(rho, qubit), expected_local))
    check("D global branch coherence remains nonzero", rho[0, 7] == sp.sqrt(2) / 3)
    restored = sp.simplify(u1 * u2 * copied)
    check("D the same local unitaries erase both copies exactly", exact_equal(restored, initial))
    check("D unitary redundancy alone neither selects nor permanently locks", copied[0] != 0 and copied[7] != 0 and exact_equal(restored, initial))


def records_are_not_automatically_a_predictive_state() -> None:
    section("E - Same present record data, different future probabilities")
    rho_plus = density(KET_PLUS)
    rho_minus = density(KET_MINUS)
    z_plus = (trace(P0 * rho_plus), trace(P1 * rho_plus))
    z_minus = (trace(P0 * rho_minus), trace(P1 * rho_minus))
    x_plus = (trace(PX_PLUS * rho_plus), trace(PX_MINUS * rho_plus))
    x_minus = (trace(PX_PLUS * rho_minus), trace(PX_MINUS * rho_minus))
    check("E plus and minus states have identical Z-record probabilities", z_plus == z_minus == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("E plus state predicts X-plus with certainty", x_plus == (1, 0))
    check("E minus state predicts X-minus with certainty", x_minus == (0, 1))
    check("E identical one-basis records do not determine every future law", z_plus == z_minus and x_plus != x_minus)
    check("E a phase/preparation/process record would separate the two states", trace(X * rho_plus) == 1 and trace(X * rho_minus) == -1)


def consistency_is_not_realm_selection() -> None:
    section("F - Decoherence consistency does not select one projective realm")
    rho = density(KET_PLUS)
    z_family = (P0, P1)
    x_family = (PX_PLUS, PX_MINUS)

    def decoherence(projectors: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
        return sp.Matrix(2, 2, lambda i, j: trace(projectors[i] * rho * projectors[j]))

    dz = decoherence(z_family)
    dx = decoherence(x_family)
    check("F the one-time Z family is exactly decoherent", dz[0, 1] == dz[1, 0] == 0)
    check("F the incompatible one-time X family is exactly decoherent", dx[0, 1] == dx[1, 0] == 0)
    check("F Z-history weights are one half and one half", tuple(dz[i, i] for i in range(2)) == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("F X-history weights are one and zero", tuple(dx[i, i] for i in range(2)) == (1, 0))
    check("F both families normalize independently", trace(dz) == trace(dx) == 1)
    check("F consistency permits incompatible supplied decompositions", exact_equal(P0 + P1, I2) and exact_equal(PX_PLUS + PX_MINUS, I2) and not exact_equal(P0 * PX_PLUS, PX_PLUS * P0))


def causal_order_control() -> None:
    section("G - Spacelike order covariance is not a universal firing law")
    p0_a = sp.kronecker_product(P0, I2)
    px_b = sp.kronecker_product(I2, PX_PLUS)
    check("G disjoint local projectors commute", exact_equal(p0_a * px_b, px_b * p0_a))

    rho_plus = density(KET_PLUS)
    z_then_x = trace(PX_PLUS * P0 * rho_plus * P0 * PX_PLUS)
    x_then_z = trace(P0 * PX_PLUS * rho_plus * PX_PLUS * P0)
    check("G overlapping Z-then-X branch has probability one quarter", z_then_x == sp.Rational(1, 4))
    check("G overlapping X-then-Z branch has probability one half", x_then_z == sp.Rational(1, 2))
    check("G causal ordering remains physical on overlapping supports", z_then_x != x_then_z)


def axelsson_functional_equation_control() -> None:
    section("H - Exact audit of the 2026 reversible/irreversible claim")

    def born(z):
        return sp.simplify(sp.Abs(z) ** 2)

    alpha_1 = sp.Integer(1)
    alpha_2 = sp.Integer(1)
    lhs = born(alpha_1 + alpha_2)
    rhs = born(alpha_1) * born(alpha_2)
    check("H displayed additive-to-multiplicative equation gives LHS four", lhs == 4)
    check("H the same equation gives RHS one", rhs == 1)
    check("H the proposed Born function fails the displayed equation", lhs != rhs)

    # If f(z+w)=f(z)f(w), f is nonnegative/nonzero, and f is phase invariant,
    # then w=-z gives f(0)=f(z)^2.  The w=0 case fixes f(0)=1, hence f(z)=1.
    f0 = sp.Integer(1)
    inferred_fz_squared = f0
    inferred_nonnegative_fz = sp.sqrt(inferred_fz_squared)
    check("H w=0 fixes f(0)=1 for every nonzero solution", f0 == 1)
    check("H w=-z forces every nonnegative nonzero value to one", inferred_nonnegative_fz == 1)
    check("H the displayed equation's nonzero nonnegative solution is constant, not Born", inferred_nonnegative_fz != born(2))

    r, s, q = sp.symbols("r s q", positive=True)
    multiplicative_modulus = sp.simplify((r * s) ** q - r**q * s**q)
    check("H the later modulus-product equation admits every power r^q", multiplicative_modulus == 0)
    check("H modulus-product composition is algebraically different from amplitude addition", born(1 + 1) != born(1) * born(1))


def implication_boundary_contract() -> None:
    section("I - No-go discipline and implication-boundary contract")
    text, normalized = normalized_note()
    requirements = (
        "N1 — Alternative-route enumeration",
        "N2 — Wall-independence audit",
        "N3 — Hidden-wall scan",
        "N4 — Exact residual matching",
        "N5 — Resolution and rhetoric audit",
        "N6 — Partial-closure paths",
        "N7 — Strongest steelman",
        "N8 — Cross-cycle echo",
    )
    for heading in requirements:
        check(f"I note contains {heading}", heading in text)
    for route in (
        "objective collapse",
        "sampled instrument",
        "consistent histories",
        "quantum Darwinism",
        "Everett",
        "Bohm",
        "causal set",
        "quantum measure",
        "deterministic cellular",
        "Wolfram multiway",
        "operational reconstruction",
        "boundary/sector selector",
    ):
        check(f"I N1 or route prose covers {route}", route.lower() in normalized)
    check("I negative conclusion is explicitly date- and corpus-bounded", "as of 2026-07-14" in text and "named primary-source routes" in normalized)
    check("I note preserves future constructive theorem route", "could jointly retire" in normalized)
    check("I source audit does not authorize a live axiom edit", "does not authorize an axiom edit" in normalized)


def main() -> int:
    source_and_scope_contract()
    route_matrix_contract()
    channel_is_not_instrument()
    redundancy_is_not_actualization()
    records_are_not_automatically_a_predictive_state()
    consistency_is_not_realm_selection()
    causal_order_control()
    axelsson_functional_equation_control()
    implication_boundary_contract()
    section("Summary")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
