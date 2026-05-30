#!/usr/bin/env python3
"""Audit companion for CHSH_TSIRELSON_LATTICE_QUBITS_BOUND_NOTE_2026-05-20.

Purpose:
  * verify the repaired Landau/Tsirelson square identity for the note's
    plus/plus/plus/minus CHSH convention;
  * catch the old wrong-sign square identity as a negative control;
  * verify the 2*sqrt(2) Bell-state saturation witness on C^2 tensor C^2.

No observational inputs, fitted parameters, or new axioms are used.
"""

from __future__ import annotations

import sys

try:
    import numpy as np
    from sympy import I, Matrix, eye, kronecker_product, simplify, sqrt, zeros
except ImportError as exc:  # pragma: no cover - audit environment guard
    print(f"FAIL: missing required package: {exc}")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS (A)" if ok else "FAIL (A)"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def as_numpy(mat: Matrix) -> np.ndarray:
    return np.array(mat.evalf().tolist(), dtype=complex)


def pauli_matrices() -> tuple[Matrix, Matrix, Matrix, Matrix]:
    id2 = eye(2)
    sx = Matrix([[0, 1], [1, 0]])
    sy = Matrix([[0, -I], [I, 0]])
    sz = Matrix([[1, 0], [0, -1]])
    return id2, sx, sy, sz


def main() -> int:
    print("CHSH Tsirelson lattice-qubit audit companion")
    print("surface: finite two-site M_2(C) tensor M_2(C) operator algebra")

    id2, sx, sy, sz = pauli_matrices()
    id4 = eye(4)

    a1 = sz
    a2 = sx
    b1 = (sz + sx) / sqrt(2)
    b2 = (sz - sx) / sqrt(2)

    for name, op in [("A_1", a1), ("A_2", a2), ("B_1", b1), ("B_2", b2)]:
        check(f"{name} is self-adjoint", op == op.H)
        check(f"{name} is an involution", simplify(op * op - id2) == zeros(2, 2))

    a1t = kronecker_product(a1, id2)
    a2t = kronecker_product(a2, id2)
    b1t = kronecker_product(id2, b1)
    b2t = kronecker_product(id2, b2)

    for a_name, at in [("A_1", a1t), ("A_2", a2t)]:
        for b_name, bt in [("B_1", b1t), ("B_2", b2t)]:
            comm = simplify(at * bt - bt * at)
            check(f"tensor locality [{a_name} tensor I, I tensor {b_name}] = 0", comm == zeros(4, 4))

    chsh = a1t * b1t + a1t * b2t + a2t * b1t - a2t * b2t
    check("CHSH operator is self-adjoint", simplify(chsh - chsh.H) == zeros(4, 4))

    comm_a = a1 * a2 - a2 * a1
    comm_b = b1 * b2 - b2 * b1
    actual_square = simplify(chsh * chsh)
    landau_rhs = simplify(4 * id4 - kronecker_product(comm_a, comm_b))
    old_wrong_rhs = simplify(4 * id4 + kronecker_product(comm_a, comm_b))

    check(
        "repaired Landau identity C^2 = 4I - [A_1,A_2] tensor [B_1,B_2]",
        simplify(actual_square - landau_rhs) == zeros(4, 4),
    )
    check(
        "negative control: old plus-sign identity is not the displayed square",
        simplify(actual_square - old_wrong_rhs) != zeros(4, 4),
    )

    expected_comm = 2 * I * sy
    check("[sigma_z, sigma_x] = 2i sigma_y", simplify(comm_a - expected_comm) == zeros(2, 2))
    comm_a_norm = np.linalg.norm(as_numpy(comm_a), ord=2)
    comm_b_norm = np.linalg.norm(as_numpy(comm_b), ord=2)
    check("||[A_1,A_2]|| <= 2", comm_a_norm <= 2.0 + 1e-12, f"{comm_a_norm:.15f}")
    check("||[B_1,B_2]|| <= 2", comm_b_norm <= 2.0 + 1e-12, f"{comm_b_norm:.15f}")

    chsh_norm = np.linalg.norm(as_numpy(chsh), ord=2)
    target = 2.0 * np.sqrt(2.0)
    check("||C|| = 2*sqrt(2) for the standard witness configuration", abs(chsh_norm - target) < 1e-12, f"{chsh_norm:.15f}")
    eigvals = np.linalg.eigvalsh(as_numpy(chsh))
    check(
        "CHSH spectrum stays within [-2*sqrt(2), 2*sqrt(2)]",
        bool(np.all(eigvals <= target + 1e-12) and np.all(eigvals >= -target - 1e-12)),
        ", ".join(f"{x:.12f}" for x in eigvals),
    )

    bell = Matrix([1, 0, 0, 1]) / sqrt(2)
    check("Bell state has unit norm", simplify((bell.H * bell)[0, 0] - 1) == 0)
    expectation = simplify((bell.H * chsh * bell)[0, 0])
    check(
        "<Phi+|C|Phi+> = 2*sqrt(2)",
        simplify(expectation - 2 * sqrt(2)) == 0,
        f"{expectation}",
    )

    # A small random Bloch-sphere sweep is not the proof; it is a falsifiable
    # implementation guard for the Landau identity and bound away from the
    # canonical Pauli witness.
    rng = np.random.default_rng(20260530)
    sx_np = as_numpy(sx)
    sy_np = as_numpy(sy)
    sz_np = as_numpy(sz)
    id2_np = np.eye(2, dtype=complex)
    max_norm = 0.0
    max_identity_residual = 0.0
    for _ in range(250):
        ops = []
        for _j in range(4):
            v = rng.standard_normal(3)
            v /= np.linalg.norm(v)
            ops.append(v[0] * sx_np + v[1] * sy_np + v[2] * sz_np)
        a1n, a2n, b1n, b2n = ops
        c = (
            np.kron(a1n, b1n)
            + np.kron(a1n, b2n)
            + np.kron(a2n, b1n)
            - np.kron(a2n, b2n)
        )
        rhs = 4.0 * np.eye(4, dtype=complex) - np.kron(a1n @ a2n - a2n @ a1n, b1n @ b2n - b2n @ b1n)
        max_identity_residual = max(max_identity_residual, np.linalg.norm(c @ c - rhs, ord=2))
        max_norm = max(max_norm, np.linalg.norm(c, ord=2))
    check("random involution sweep preserves Landau identity", max_identity_residual < 1e-12, f"max residual {max_identity_residual:.3e}")
    check("random involution sweep obeys Tsirelson upper bound", max_norm <= target + 1e-12, f"max ||C|| {max_norm:.15f}")

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
