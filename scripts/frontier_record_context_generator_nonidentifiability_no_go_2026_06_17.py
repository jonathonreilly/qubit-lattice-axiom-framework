#!/usr/bin/env python3
"""Record/pre-record readout-context and generator nonidentifiability no-go.

This runner proves the finite obstruction behind the supplied-context boundary
in RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md.

It does not audit, promote, or retag the source row. It checks that:

  * the same one-qubit state and the same cited projective/Lueders algebra
    admit multiple complete readout contexts with different probability
    vectors;
  * once an outcome is realized, the post-record count update is the same
    one-hot append/count grammar for every context;
  * a one-step production vector does not identify the physical Markov kernel,
    continuous generator, or clock/rate normalization.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0
REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md"
SOURCE_GATE_PATH = "docs/RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def read_doc(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def trace(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(matrix[i, i] for i in range(matrix.rows)))


def projector(ket: sp.Matrix) -> sp.Matrix:
    return sp.simplify(ket * ket.T)


def is_zero_matrix(matrix: sp.Matrix) -> bool:
    matrix = sp.simplify(matrix)
    return all(matrix[i, j] == 0 for i in range(matrix.rows) for j in range(matrix.cols))


def probabilities(rho: sp.Matrix, projectors: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
    return sp.Matrix([sp.simplify(trace(projectors[0] * rho)), sp.simplify(trace(projectors[1] * rho))])


def valid_binary_projective_context(projectors: tuple[sp.Matrix, sp.Matrix]) -> bool:
    p0, p1 = projectors
    return (
        is_zero_matrix(p0 * p1)
        and is_zero_matrix(p0 + p1 - sp.eye(2))
        and is_zero_matrix(p0 * p0 - p0)
        and is_zero_matrix(p1 * p1 - p1)
    )


def row_stochastic(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(sum(matrix[i, j] for j in range(matrix.cols)) - 1) == 0 for i in range(matrix.rows))


def row_generator(matrix: sp.Matrix) -> bool:
    off_diag_nonnegative = all(
        matrix[i, j] >= 0
        for i in range(matrix.rows)
        for j in range(matrix.cols)
        if i != j
    )
    rows_zero = all(sp.simplify(sum(matrix[i, j] for j in range(matrix.cols))) == 0 for i in range(matrix.rows))
    return off_diag_nonnegative and rows_zero


def main() -> int:
    print("Record context/generator nonidentifiability no-go")
    print("status: exact negative boundary; source-side only; independent audit owns effective status")
    print()

    minimal_axioms = read_doc("docs/MINIMAL_AXIOMS_2026-06-05.md")
    source_gate = read_doc(SOURCE_GATE_PATH)
    note = read_doc(NOTE_PATH)
    clock_gate = read_doc("docs/RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md")
    post_record = read_doc("docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md")
    lsp_note = read_doc("docs/LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md")
    luders_note = read_doc("docs/LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md")

    print("A. source anchors and firewalls")
    flat_note = " ".join(note.split())
    flat_source_gate = " ".join(source_gate.split())
    flat_post_record = " ".join(post_record.split())
    check("note declares exact negative boundary", "Status: exact negative boundary" in note)
    check("note forbids bare retained status", "bare_retained_allowed: false" in note)
    check("note names direct blocker", "physical readout context, apparatus dynamics, Markov generator, or rate/clock normalization" in flat_note)
    check("note carries direct minimal-axiom link", "[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)" in note)
    check("note carries direct projective authority link", "LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md" in note)
    check("note carries direct Lueders authority link", "LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md" in note)
    check("note records no-go discipline pass", "Gate result: PASS for this narrow no-go boundary." in note)
    check("minimal axioms exclude measurement/Born/readout context", "measurement\ninstrument, Born rule" in minimal_axioms and "record supplies no readout context" in minimal_axioms)
    check("source gate is bounded supplied-context finite algebra", "bounded finite algebra under supplied readout context" in source_gate)
    check("source gate does not derive physical Markov generator", "derive a physical Markov generator" in source_gate)
    check("clock/rate gate requires supplied generators", "given a derived or admitted production generator" in clock_gate)
    check("post-record dynamics does not select the next atom", "not a selector for which atom will be produced next" in flat_post_record)
    check("projective authority supplies K_r = P_r, not a context selector", "K_r = P_r" in lsp_note)
    check("Lueders authority supplies branch form, not a context selector", "P sigma P" in luders_note.replace("sigma", "sigma").replace("σ", "sigma"))

    print("\nB. same pre-record state, distinct complete readout contexts")
    sqrt2 = sp.sqrt(2)
    psi = sp.Matrix([sp.sqrt(sp.Rational(2, 3)), sp.sqrt(sp.Rational(1, 3))])
    rho = projector(psi)
    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    ket_plus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), sp.sqrt(sp.Rational(1, 2))])
    ket_minus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), -sp.sqrt(sp.Rational(1, 2))])
    ket_y_plus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), sp.I * sp.sqrt(sp.Rational(1, 2))])
    ket_y_minus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), -sp.I * sp.sqrt(sp.Rational(1, 2))])

    contexts = {
        "Z": (projector(ket0), projector(ket1)),
        "X": (projector(ket_plus), projector(ket_minus)),
        "Y": (ket_y_plus * ket_y_plus.conjugate().T, ket_y_minus * ket_y_minus.conjugate().T),
    }
    p_z = probabilities(rho, contexts["Z"])
    p_x = probabilities(rho, contexts["X"])
    p_y = sp.Matrix([sp.simplify(trace(contexts["Y"][0] * rho)), sp.simplify(trace(contexts["Y"][1] * rho))])

    check("rho is the same normalized pure one-qubit state", trace(rho) == 1 and rho.det() == 0, f"rho={rho}")
    for name, projectors in contexts.items():
        check(f"{name} context is complete and projective", valid_binary_projective_context(projectors))
    check("Z probabilities are normalized", sp.simplify(sum(p_z) - 1) == 0, f"p_z={list(p_z)}")
    check("X probabilities are normalized", sp.simplify(sum(p_x) - 1) == 0, f"p_x={list(p_x)}")
    check("Y probabilities are normalized", sp.simplify(sum(p_y) - 1) == 0, f"p_y={list(p_y)}")
    check("Z context gives (2/3, 1/3)", p_z == sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 3)]), f"p_z={list(p_z)}")
    check("X context gives a different kernel", p_x == sp.Matrix([sp.Rational(1, 2) + sqrt2 / 3, sp.Rational(1, 2) - sqrt2 / 3]), f"p_x={list(p_x)}")
    check("Y context gives a third allowed kernel", p_y == sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)]), f"p_y={list(p_y)}")
    check("same rho plus same projective algebra does not select the context", len({tuple(p_z), tuple(p_x), tuple(p_y)}) == 3)

    print("\nC. realized post-record grammar is context-independent after selection")
    count = sp.Matrix([4, 2])
    e0 = sp.Matrix([1, 0])
    e1 = sp.Matrix([0, 1])
    update0 = count + e0
    update1 = count + e1
    expected_z = count + p_z
    expected_y = count + p_y
    check("outcome 0 count update is integral", update0 == sp.Matrix([5, 2]))
    check("outcome 1 count update is integral", update1 == sp.Matrix([4, 3]))
    check("same one-hot update grammar applies for every context", update0 - count == e0 and update1 - count == e1)
    check("ensemble expectations depend on context and are not realized atoms", expected_z != update0 and expected_z != update1 and expected_y != update0 and expected_y != update1)
    check("post-record layer consumes realized atom, not the probability vector", e0 != p_z and e1 != p_z and e0 != p_x and e1 != p_x)

    print("\nD. production vector does not identify a physical kernel or generator")
    # A one-step production row from a ready state to atoms can be embedded in
    # inequivalent stochastic dynamics with the same production row.
    k_absorbing = sp.Matrix([
        [0, sp.Rational(2, 3), sp.Rational(1, 3)],
        [0, 1, 0],
        [0, 0, 1],
    ])
    k_mixing = sp.Matrix([
        [0, sp.Rational(2, 3), sp.Rational(1, 3)],
        [0, sp.Rational(1, 2), sp.Rational(1, 2)],
        [0, sp.Rational(1, 3), sp.Rational(2, 3)],
    ])
    check("two candidate stochastic kernels are valid", row_stochastic(k_absorbing) and row_stochastic(k_mixing))
    check("candidate kernels have the same ready-state production row", list(k_absorbing[0, :]) == list(k_mixing[0, :]) == [0, sp.Rational(2, 3), sp.Rational(1, 3)])
    check("candidate kernels disagree after the atom is present", k_absorbing[1, :] != k_mixing[1, :] and k_absorbing[2, :] != k_mixing[2, :])

    pi = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)]])
    q1 = sp.Matrix([[-sp.Rational(1, 3), sp.Rational(1, 3)], [sp.Rational(2, 3), -sp.Rational(2, 3)]])
    q5 = 5 * q1
    check("Q1 is a valid row Markov generator", row_generator(q1))
    check("Q5 is a distinct valid row Markov generator", row_generator(q5) and q5 != q1)
    check("both generators stabilize the same probability vector", is_zero_matrix(pi * q1) and is_zero_matrix(pi * q5))

    r1 = sp.Integer(1)
    t1 = sp.log(sp.Rational(3, 2))
    r2 = sp.Integer(2)
    t2 = sp.log(sp.Rational(3, 2)) / 2
    write_prob_1 = sp.simplify(1 - sp.exp(-r1 * t1))
    write_prob_2 = sp.simplify(1 - sp.exp(-r2 * t2))
    check("distinct rate/clock pairs have the same dimensionless product", r1 != r2 and t1 != t2 and sp.simplify(r1 * t1 - r2 * t2) == 0)
    check("same product gives same one-step write probability", write_prob_1 == write_prob_2 == sp.Rational(1, 3), f"p={write_prob_1}")

    print("\nE. exact no-go conclusion")
    check("note keeps readout context underived", "Does not derive a readout context." in note)
    check("note keeps physical kernel/generator underived", "Does not derive a physical Markov kernel, Hamiltonian, transfer operator, or continuous generator." in " ".join(note.split()))
    check("note keeps clock/rate unit underived", "Does not derive a physical clock or rate unit." in note)
    check("source gate cannot be cited as production-generator closure", "it cannot cite this row for more than the finite supplied-context algebra above" in flat_source_gate)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: exact negative boundary. The supplied-context finite gate "
            "is self-consistent, but the same state/algebra admits multiple "
            "readout contexts and the resulting one-step probability vector "
            "does not identify the physical kernel, generator, or clock/rate."
        )
        return 0
    print("VERDICT: failed; do not cite this no-go.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
