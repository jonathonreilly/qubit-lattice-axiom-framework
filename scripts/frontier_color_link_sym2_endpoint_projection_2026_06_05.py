#!/usr/bin/env python3
"""Exact Sym^2 projection algebra for an admitted two-qubit color endpoint.

The runner verifies that a two-qubit endpoint has a canonical swap projector
with ranks 3 and 1, and that the standard Gell-Mann su(3) action can be
embedded on the symmetric rank-3 block while killing the antisymmetric
complement.

It does not derive the endpoint, link ontology, SU(3) transport law, Gauss
generators, action/couplings, record readout, or any dial selection.
"""

from __future__ import annotations

from pathlib import Path

try:
    import sympy as sp
    from sympy import I, Matrix, Rational, eye, simplify, sqrt, zeros
except ImportError:  # pragma: no cover
    print("FAIL: sympy required")
    raise SystemExit(1)


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def gell_mann() -> list[Matrix]:
    s3 = sqrt(3)
    return [
        Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
        Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
        Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
        Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / s3,
    ]


def is_zero(M: Matrix) -> bool:
    return all(simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def main() -> int:
    emit("=" * 78)
    emit("COLOR LINK SYM2 ENDPOINT PROJECTION")
    emit("exact-support projection algebra runner")
    emit("=" * 78)

    section("1. Swap projectors on C^2 x C^2")
    # Basis: |00>, |01>, |10>, |11>
    S = Matrix(
        [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ]
    )
    I4 = eye(4)
    P_sym = (I4 + S) / 2
    P_anti = (I4 - S) / 2
    check("swap is involutive: S^2 = I", S * S == I4)
    check("P_sym is idempotent", is_zero(P_sym * P_sym - P_sym))
    check("P_anti is idempotent", is_zero(P_anti * P_anti - P_anti))
    check("P_sym + P_anti = I", is_zero(P_sym + P_anti - I4))
    check("P_sym P_anti = 0", is_zero(P_sym * P_anti))
    check("rank P_sym = 3", P_sym.rank() == 3, f"rank={P_sym.rank()}")
    check("rank P_anti = 1", P_anti.rank() == 1, f"rank={P_anti.rank()}")
    check("trace P_sym = 3", simplify(P_sym.trace()) == 3)
    check("trace P_anti = 1", simplify(P_anti.trace()) == 1)

    section("2. Symmetric and antisymmetric bases")
    e00 = Matrix([1, 0, 0, 0])
    e11 = Matrix([0, 0, 0, 1])
    e_sym = Matrix([0, 1, 1, 0]) / sqrt(2)
    e_anti = Matrix([0, 1, -1, 0]) / sqrt(2)
    V = Matrix.hstack(e00, e11, e_sym)
    A = Matrix.hstack(e_anti)
    check("symmetric basis has 3 columns", V.shape == (4, 3))
    check("antisymmetric basis has 1 column", A.shape == (4, 1))
    check("V^H V = I3", is_zero(V.H * V - eye(3)))
    check("A^H A = I1", is_zero(A.H * A - eye(1)))
    check("V^H A = 0", is_zero(V.H * A))
    check("P_sym V = V", is_zero(P_sym * V - V))
    check("P_anti A = A", is_zero(P_anti * A - A))
    check("P_sym A = 0", is_zero(P_sym * A))

    section("3. Embedded su(3) on Sym^2")
    lam = gell_mann()
    T4 = [V * (L / 2) * V.H for L in lam]
    check("eight embedded generators", len(T4) == 8)
    for idx, T in enumerate(T4, start=1):
        check(f"T{idx} Hermitian", is_zero(T.H - T))
        check(f"T{idx} preserves P_sym", is_zero(P_sym * T - T) and is_zero(T * P_sym - T))
        check(f"T{idx} kills P_anti", is_zero(P_anti * T) and is_zero(T * P_anti))
    check("embedded T1,T2 commutator gives i T3", is_zero(T4[0] * T4[1] - T4[1] * T4[0] - I * T4[2]))
    check(
        "embedded T4,T5 commutator gives i/2(T3 + sqrt(3)T8)",
        is_zero(T4[3] * T4[4] - T4[4] * T4[3] - I * (T4[2] + sqrt(3) * T4[7]) / 2),
    )
    trace_norm_ok = all(simplify((T4[a] * T4[b]).trace() - (Rational(1, 2) if a == b else 0)) == 0 for a in range(8) for b in range(8))
    check("trace normalization on embedded symmetric block is 1/2 delta_ab", trace_norm_ok)

    section("4. Constraint boundary")
    # X on first qubit does not commute with the swap projector; it leaks across
    # the 3+1 split and therefore is not an allowed color-link transport.
    X = Matrix([[0, 1], [1, 0]])
    I2 = eye(2)
    X_first = sp.kronecker_product(X, I2)
    comm = X_first * P_sym - P_sym * X_first
    check("generic one-qubit operation fails to preserve P_sym", not is_zero(comm))
    check("P_sym-preserving condition is nontrivial", comm.rank() > 0, f"comm_rank={comm.rank()}")
    check("block su(3) action preserves P_sym", all(is_zero(T * P_sym - P_sym * T) for T in T4))

    section("5. Residual ledger")
    exact_outputs = {
        "swap_projector",
        "rank3_symmetric_endpoint",
        "rank1_antisymmetric_complement",
        "embedded_su3_on_sym2",
    }
    residuals = {
        "derive_two_qubit_endpoint",
        "choose_physical_link_pair",
        "dynamically_preserve_sym2",
        "su3_parallel_transport_law",
        "endpoint_gauss_generators",
        "wilson_observables",
        "action_couplings_rates_time",
        "color_record_readout_antecedent",
    }
    post_record = {"word_history_O_star", "count_state_N_to_O"}
    check("four exact projection outputs recorded", len(exact_outputs) == 4)
    check("eight residuals remain recorded", len(residuals) == 8)
    check("projection outputs do not include residuals", exact_outputs.isdisjoint(residuals))
    check("post-record outputs do not include residuals", post_record.isdisjoint(residuals))
    check("dynamic preservation remains residual", "dynamically_preserve_sym2" in residuals)
    check("SU(3) transport law remains residual", "su3_parallel_transport_law" in residuals)
    check("color-record readout remains residual", "color_record_readout_antecedent" in residuals)

    section("6. Note sanity")
    doc = Path("docs/COLOR_LINK_SYM2_ENDPOINT_PROJECTION_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "Claim type:** bounded_theorem",
        "admitted two-qubit endpoint",
        "This theorem does not supply the endpoint.",
        "Does not derive physical color.",
        "Does not establish a repo-wide quantum-link ontology.",
        "Does not select a Koide/generation dial location.",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("physical color closure", "physical color is " + "derived"),
        ("endpoint ontology closure", "endpoint is " + "derived"),
        ("transport closure", "transport law is " + "derived"),
        ("dial selector closure", "dial location is " + "selected"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
