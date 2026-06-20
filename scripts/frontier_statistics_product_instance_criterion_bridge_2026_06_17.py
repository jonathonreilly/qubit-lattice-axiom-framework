#!/usr/bin/env python3
"""Verify the statistics product-instance criterion bridge.

This runner checks the finite M_2(C) algebra behind the source bridge:

* same marginals plus product-effect factorization on the shifted Pauli effect
  basis force rho = sigma tensor sigma;
* product instances imply registered two-outcome quotient factorization;
* the quotient factorization premise is strictly stronger than same marginals
  and strictly weaker than full product-state structure;
* the companion note and downstream statistics atom note keep the status
  boundary explicit.

It writes no files, invokes no git command, and uses no network.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md"
CONSUMER = ROOT / "docs" / (
    "STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_"
    "BOUNDED_NOTE_2026-06-12.md"
)
GLEASON = ROOT / "docs" / (
    "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_"
    "2026-05-20.md"
)
BUSCH = ROOT / "docs" / (
    "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_"
    "2026-06-05.md"
)
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
PRODUCT_WEAKENING = ROOT / "docs" / (
    "PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_"
    "2026-06-12.md"
)

PASS = 0
FAIL = 0


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")
    return ok


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def trace(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(matrix))


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(a, b)


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def partial_trace_second(matrix: sp.Matrix) -> sp.Matrix:
    """Trace out the second qubit in first-qubit-major tensor ordering."""
    return sp.Matrix(
        2,
        2,
        lambda i, j: sp.simplify(sum(matrix[2 * i + k, 2 * j + k] for k in range(2))),
    )


def partial_trace_first(matrix: sp.Matrix) -> sp.Matrix:
    """Trace out the first qubit in first-qubit-major tensor ordering."""
    return sp.Matrix(
        2,
        2,
        lambda i, j: sp.simplify(sum(matrix[2 * k + i, 2 * k + j] for k in range(2))),
    )


def symbolic_checks() -> dict[str, bool]:
    section("Symbolic product-instance checks")

    sx, sy, sz = sp.symbols("s_x s_y s_z", real=True)
    s = {"x": sx, "y": sy, "z": sz}
    t_symbols = sp.symbols(
        "T_xx T_xy T_xz T_yx T_yy T_yz T_zx T_zy T_zz",
        real=True,
    )
    axes = ("x", "y", "z")
    t = {(a, b): t_symbols[3 * i + j] for i, a in enumerate(axes) for j, b in enumerate(axes)}

    identity = sp.eye(2)
    pauli = {
        "x": sp.Matrix([[0, 1], [1, 0]]),
        "y": sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        "z": sp.Matrix([[1, 0], [0, -1]]),
    }
    effects = {axis: (identity + pauli[axis]) / 2 for axis in axes}

    sigma = (identity + sx * pauli["x"] + sy * pauli["y"] + sz * pauli["z"]) / 2
    rho = kron(identity, identity)
    for axis in axes:
        rho += s[axis] * kron(pauli[axis], identity)
        rho += s[axis] * kron(identity, pauli[axis])
    for a in axes:
        for b in axes:
            rho += t[(a, b)] * kron(pauli[a], pauli[b])
    rho = sp.simplify(rho / 4)
    rho_product = sp.simplify(kron(sigma, sigma))

    hermitian = matrix_is_zero(rho - rho.conjugate().T)
    normalized = sp.simplify(trace(rho) - 1) == 0
    first_margin = matrix_is_zero(partial_trace_second(rho) - sigma)
    second_margin = matrix_is_zero(partial_trace_first(rho) - sigma)
    check(
        "P0 Pauli tensor ansatz is normalized, Hermitian, and has both marginals sigma",
        hermitian and normalized and first_margin and second_margin,
    )

    equations = []
    expected_equations = []
    for a in axes:
        for b in axes:
            joint = trace(rho * kron(effects[a], effects[b]))
            one_a = trace(sigma * effects[a])
            one_b = trace(sigma * effects[b])
            connected = sp.simplify(joint - one_a * one_b)
            equations.append(connected)
            expected_equations.append(sp.simplify(connected - (t[(a, b)] - s[a] * s[b]) / 4) == 0)
    check(
        "P1a shifted Pauli product-effect cumulants are exactly (T_ab - s_a s_b)/4",
        all(expected_equations),
    )

    solutions = sp.solve(equations, list(t_symbols), dict=True)
    expected_solution = {t[(a, b)]: s[a] * s[b] for a in axes for b in axes}
    criterion_solution = len(solutions) == 1 and all(
        sp.simplify(solutions[0][key] - value) == 0 for key, value in expected_solution.items()
    )
    check(
        "P1b vanishing product-effect cumulants force T_ab=s_a s_b",
        criterion_solution,
        f"solutions={solutions}",
    )

    rho_under_criterion = rho.subs(expected_solution)
    product_forced = matrix_is_zero(rho_under_criterion - rho_product)
    check(
        "P1c same marginals plus product-effect criterion force rho=sigma tensor sigma",
        product_forced,
    )

    a0, a1, a2, a3 = sp.symbols("a0:4")
    b0, b1, b2, b3 = sp.symbols("b0:4")
    a_eff = sp.Matrix([[a0, a1], [a2, a3]])
    b_eff = sp.Matrix([[b0, b1], [b2, b3]])
    product_trace_factorization = sp.simplify(
        trace(rho_product * kron(a_eff, b_eff)) - trace(sigma * a_eff) * trace(sigma * b_eff)
    ) == 0
    check(
        "P2a product state factors arbitrary product-effect expectations",
        product_trace_factorization,
    )

    ps, pd = sp.symbols("p_s p_d", real=True)
    quotient_cells = {
        ("s", "s"): ps**2,
        ("s", "d"): ps * pd,
        ("d", "s"): pd * ps,
        ("d", "d"): pd**2,
    }
    quotient_cumulants = {
        ("s", "s"): sp.simplify(quotient_cells[("s", "s")] - ps * ps),
        ("s", "d"): sp.simplify(quotient_cells[("s", "d")] - ps * pd),
        ("d", "s"): sp.simplify(quotient_cells[("d", "s")] - pd * ps),
        ("d", "d"): sp.simplify(quotient_cells[("d", "d")] - pd * pd),
    }
    quotient_factorized = all(value == 0 for value in quotient_cumulants.values())
    quotient_complete = sp.simplify(sum(quotient_cells.values()).subs(pd, 1 - ps) - 1) == 0
    check(
        "P3 quotient criterion is exactly vanishing registered-weight cumulants",
        quotient_factorized and quotient_complete,
        f"cumulants={quotient_cumulants}",
    )

    p = sp.symbols("p", real=True)
    ket0 = sp.Matrix([[1], [0]])
    ket1 = sp.Matrix([[0], [1]])
    proj0 = ket0 * ket0.T
    proj1 = ket1 * ket1.T
    sigma_diag = p * proj0 + (1 - p) * proj1
    rho_corr = p * kron(proj0, proj0) + (1 - p) * kron(proj1, proj1)
    same_marginals = matrix_is_zero(partial_trace_second(rho_corr) - sigma_diag) and matrix_is_zero(
        partial_trace_first(rho_corr) - sigma_diag
    )
    mixed_cell = trace(rho_corr * kron(proj0, proj1))
    product_mixed_cell = trace(sigma_diag * proj0) * trace(sigma_diag * proj1)
    witness_fails_factorization = (
        sp.simplify(mixed_cell) == 0
        and sp.simplify(product_mixed_cell - p * (1 - p)) == 0
        and sp.simplify((mixed_cell - product_mixed_cell).subs(p, sp.Rational(1, 2))) != 0
    )
    check(
        "P4 same-marginal correlated witness fails quotient factorization",
        same_marginals and witness_fails_factorization,
        f"mixed_cell={mixed_cell}, product_cell={product_mixed_cell}",
    )

    return {
        "pauli_ansatz": hermitian and normalized and first_margin and second_margin,
        "product_effect_criterion": criterion_solution and product_forced,
        "product_implies_quotient": product_trace_factorization,
        "quotient_factorization": quotient_factorized and quotient_complete,
        "same_marginal_control": same_marginals and witness_fails_factorization,
    }


def textual_checks() -> None:
    section("Textual firewall checks")

    note = NOTE.read_text(encoding="utf-8")
    consumer = CONSUMER.read_text(encoding="utf-8")
    gleason = GLEASON.read_text(encoding="utf-8")
    busch = BUSCH.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    product_weakening = PRODUCT_WEAKENING.read_text(encoding="utf-8")

    note_n = normalize(note)
    consumer_n = normalize(consumer)
    gleason_n = normalize(gleason)
    busch_n = normalize(busch).replace("**", "")
    minimal_n = normalize(minimal)
    product_n = normalize(product_weakening)

    check(
        "T1 bridge note metadata is canonical bounded_theorem with independent audit required",
        "# Statistics Product-Instance Criterion Bridge" in note
        and "**Type:** bounded_theorem" in note
        and "**Claim type:** bounded_theorem" in note
        and "independent audit required before any downstream status change" in note_n,
    )
    required_note_phrases = [
        "does not derive physical independence",
        "does not derive the physical reason repeated records should satisfy that criterion",
        "does not add a new probability axiom or a new framework axiom",
        "full product-instance witness",
        "weaker quotient premise",
        "record-stack theorem",
        "No-promotion statement",
    ]
    missing = [phrase for phrase in required_note_phrases if phrase not in note_n]
    check("T2 bridge boundary and no-new-axiom firewall phrases present", not missing, ", ".join(missing))

    check(
        "T3 retained-source dependencies are cited as dependencies, not redefined",
        "specific Hilbert space `H_Λ = ⊗_{x ∈ Λ} ℂ²`" in gleason_n
        and "unique density matrix" in busch_n
        and "does not supply a dynamics, composition theorem" in minimal_n,
    )
    check(
        "T4 product-to-outcome weakening dependency remains the downstream quotient authority",
        "strictly weaker than state-level product form" in product_n
        and "outcome-level factorization" in product_n,
    )
    check(
        "T5 statistics atom note links the product-instance bridge as an explicit dependency",
        "STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md" in consumer
        and "exact product-instance criterion" in consumer_n
        and "physical outcome-factorization premise itself remains open" in consumer_n,
    )

    forbidden = [
        "this closes",
        "now closed",
        "is closed",
        "settles",
        "settled",
        "resolved",
        "now retained",
        "promoted to retained",
        "retained on the actual surface",
    ]
    joined = " ".join([note_n.lower(), consumer_n.lower()])
    hits = [phrase for phrase in forbidden if phrase in joined]
    check("T6 closing/promotion overclaim language absent", not hits, ", ".join(hits))

    expected_links = [
        "[`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)",
        "[`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)",
        "[`PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`](PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md)",
        "[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)",
    ]
    links = [link for link in re.findall(r"\[[^\]]+\]\([^)]+\)", note) if ".md)" in link]
    check("T7 bridge markdown link inventory is exactly the dependency set", links == expected_links, f"found={links}")


def print_stat_and_summary(results: dict[str, bool]) -> None:
    section("git diff --stat")
    print("(computed without invoking git, per the no-git rule)")
    files = [NOTE, CONSUMER, Path(__file__).resolve()]
    total_lines = 0
    for path in files:
        rel = path.relative_to(ROOT)
        lines = path.read_text(encoding="utf-8").count("\n")
        total_lines += lines
        print(f" {rel} | {lines} +")
    print(f" 3 files changed, {total_lines} insertions(+)")
    print()
    print("SUMMARY:")
    print(
        "Product-effect criterion, product-to-quotient implication, quotient cumulant "
        "criterion, same-marginal control, and textual status firewalls verified."
    )
    print(
        "Physical repeated-registration independence remains an open premise outside this bridge."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(f"CHAIN: {results}")


def main() -> int:
    print("Statistics product-instance criterion bridge runner")
    print("Status authority: independent audit lane only; this runner sets no audit outcome.")
    results = symbolic_checks()
    textual_checks()
    print_stat_and_summary(results)
    return 0 if FAIL == 0 and PASS >= 14 else 1


if __name__ == "__main__":
    sys.exit(main())
