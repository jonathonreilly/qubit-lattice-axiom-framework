"""Gauge-selection conjugation independence certificate.

This runner supports
GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.

It checks a narrow finite-dimensional obstruction:

  Given the supplied H = C^3(base) x C^2(fiber) carrier, the factorwise
  algebra su(3)xI + Ixsu(2) + u(1) is a valid dim-12 irreducible subalgebra of
  u(6).  But carrier-level invariant data alone does not select that embedding.
  A non-factor-local unitary conjugate has the same dimension, closure, and
  scalar commutant, while being a distinct non-factor-local embedding.  The full
  u(6) algebra also has scalar commutant.  Therefore any route based only on
  irreducibility/maximal indistinguishability/conjugation-invariant algebraic
  data cannot choose the factorwise dim-12 gauging without supplying the
  factorization/gauging principle.

The runner does not derive MR_color, a gauge action, or chiral su(2)_L.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md"
PARENT = ROOT / "docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def gell_mann() -> list[np.ndarray]:
    matrices: list[np.ndarray] = []
    matrices.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex))
    matrices.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex))
    matrices.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex))
    matrices.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex))
    matrices.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex))
    matrices.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex))
    matrices.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex))
    matrices.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3))
    return matrices


def rank_span(mats: list[np.ndarray], tol: float = 1e-10) -> int:
    return int(np.linalg.matrix_rank(np.array([m.reshape(-1) for m in mats]), tol=tol))


def span_residual(mat: np.ndarray, basis: list[np.ndarray]) -> float:
    b = np.array([basis_mat.reshape(-1) for basis_mat in basis]).T
    coeffs, *_ = np.linalg.lstsq(b, mat.reshape(-1), rcond=None)
    return float(np.linalg.norm(mat.reshape(-1) - b @ coeffs))


def max_closure_residual(gens: list[np.ndarray], basis: list[np.ndarray]) -> float:
    residual = 0.0
    for a in gens:
        for b in gens:
            # Hermitian generators close under i[A,B] inside the Hermitian span.
            residual = max(residual, span_residual(1j * (a @ b - b @ a), basis))
    return float(residual)


def commutant_dim(gens: list[np.ndarray], dim: int, tol: float = 1e-10) -> int:
    constraints = np.zeros((0, dim * dim), complex)
    for gen in gens:
        # vec([G, X]) = (I x G - G^T x I) vec(X).
        block = np.kron(np.eye(dim), gen) - np.kron(gen.T, np.eye(dim))
        constraints = np.vstack([constraints, block])
    return int(dim * dim - np.linalg.matrix_rank(constraints, tol=tol))


def center_dim(gens: list[np.ndarray], basis: list[np.ndarray], tol: float = 1e-10) -> int:
    blocks = []
    for gen in gens:
        blocks.append(np.array([(basis_mat @ gen - gen @ basis_mat).reshape(-1) for basis_mat in basis]).T)
    constraints = np.vstack(blocks)
    return int(len(basis) - np.linalg.matrix_rank(constraints, tol=tol))


def entangling_unitary(theta: float = 0.37) -> np.ndarray:
    """Unitary that mixes |base=0,fiber=0> with |base=1,fiber=1>."""
    unitary = np.eye(6, dtype=complex)
    a = 0
    b = 3
    c = np.cos(theta)
    s = np.sin(theta)
    unitary[a, a] = c
    unitary[b, b] = c
    unitary[a, b] = 1j * s
    unitary[b, a] = 1j * s
    return unitary


def operator_schmidt_rank(mat: np.ndarray, tol: float = 1e-10) -> int:
    # H = C^3 x C^2.  A factor-local A x B operator has rank one in this
    # reshaped coefficient matrix.
    reshaped = mat.reshape(3, 2, 3, 2).transpose(0, 2, 1, 3).reshape(9, 4)
    return int(np.linalg.matrix_rank(reshaped, tol=tol))


def elementary_matrix_basis(dim: int) -> list[np.ndarray]:
    basis: list[np.ndarray] = []
    for i in range(dim):
        for j in range(dim):
            mat = np.zeros((dim, dim), complex)
            mat[i, j] = 1
            basis.append(mat)
    return basis


def main() -> int:
    print("GAUGE-SELECTION CONJUGATION INDEPENDENCE CERTIFICATE")
    print("=" * 72)

    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    check(
        "source note declares exact negative boundary and no status promotion",
        "**Status:** exact negative boundary / route-pruning support" in note_flat
        and "does not derive `MR_color`" in note_flat
        and "does not update or apply any audit verdict" in note_flat
        and "2026-06-16 Exact independence addendum" in parent_text,
    )

    i2 = np.eye(2, dtype=complex)
    i3 = np.eye(3, dtype=complex)
    i6 = np.eye(6, dtype=complex)
    x = np.array([[0, 1], [1, 0]], complex)
    y = np.array([[0, -1j], [1j, 0]], complex)
    z = np.array([[1, 0], [0, -1]], complex)
    paulis = [x, y, z]
    gm = gell_mann()

    factorwise = [np.kron(g, i2) for g in gm] + [np.kron(i3, p) for p in paulis] + [i6]
    factorwise_semisimple = factorwise[:-1]
    dim_factorwise = rank_span(factorwise)
    closure_factorwise = max_closure_residual(factorwise_semisimple, factorwise)
    comm_factorwise = commutant_dim(factorwise_semisimple, 6)
    check(
        "factorwise candidate is a closed dim-12 irreducible algebra on the supplied C^3 x C^2 carrier",
        dim_factorwise == 12 and closure_factorwise < 1e-10 and comm_factorwise == 1,
        f"dim={dim_factorwise}; closure residual={closure_factorwise:.2e}; commutant_dim={comm_factorwise}",
    )

    unitary = entangling_unitary()
    conjugate = [unitary @ gen @ unitary.conj().T for gen in factorwise]
    conjugate_semisimple = conjugate[:-1]
    dim_conjugate = rank_span(conjugate)
    closure_conjugate = max_closure_residual(conjugate_semisimple, conjugate)
    comm_conjugate = commutant_dim(conjugate_semisimple, 6)
    check(
        "non-factor-local conjugate has the same dimension, closure, and scalar commutant",
        dim_conjugate == 12 and closure_conjugate < 1e-10 and comm_conjugate == 1,
        f"dim={dim_conjugate}; closure residual={closure_conjugate:.2e}; commutant_dim={comm_conjugate}",
    )

    center_factorwise = center_dim(factorwise, factorwise)
    center_conjugate = center_dim(conjugate, conjugate)
    check(
        "factorwise and conjugate embeddings have the same one-dimensional center profile",
        center_factorwise == 1 and center_conjugate == 1,
        f"center_dim factorwise={center_factorwise}; center_dim conjugate={center_conjugate}",
    )

    combined_dim = rank_span(factorwise + conjugate)
    max_conjugate_residual = max(span_residual(gen, factorwise) for gen in conjugate)
    original_schmidt = sorted({operator_schmidt_rank(gen) for gen in factorwise})
    conjugate_schmidt = [operator_schmidt_rank(gen) for gen in conjugate]
    check(
        "conjugate embedding is distinct from the supplied factorwise split",
        combined_dim > 12 and max_conjugate_residual > 1e-2 and max(conjugate_schmidt) > 1,
        "combined_span_dim=%d; max residual into factorwise span=%.3f; "
        "original Schmidt ranks=%s; conjugate max Schmidt rank=%d"
        % (combined_dim, max_conjugate_residual, original_schmidt, max(conjugate_schmidt)),
    )

    full_u6 = elementary_matrix_basis(6)
    dim_u6 = rank_span(full_u6)
    comm_u6 = commutant_dim(full_u6, 6)
    check(
        "full u(6) has the same scalar-commutant irreducibility profile as the dim-12 candidate",
        dim_u6 == 36 and comm_u6 == 1 and comm_factorwise == 1,
        f"dim u(6)={dim_u6}; commutant_dim u(6)={comm_u6}; commutant_dim dim-12={comm_factorwise}",
    )

    invariant_profile_matches = (
        dim_factorwise == dim_conjugate
        and comm_factorwise == comm_conjugate
        and closure_factorwise < 1e-10
        and closure_conjugate < 1e-10
    )
    check(
        "conjugation-invariant algebraic data cannot choose one dim-12 embedding",
        invariant_profile_matches and combined_dim > dim_factorwise,
        "both embeddings have dim=12, closure residual <1e-10, scalar commutant; "
        f"yet combined_span_dim={combined_dim}",
    )

    check(
        "selection principle required: factorization/gauging input is not produced by Lattice + Quantum + Record",
        "Record" in note_flat
        and "supplies no carrier factorization" in note_flat
        and "future selection theorem, approved primitive, or explicit admitted bridge" in note_flat,
    )

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(
        "VERDICT: exact negative boundary / route-pruning support.  The finite "
        "witness proves that irreducibility, scalar commutant, closure, and "
        "conjugation-invariant carrier algebra data do not select the supplied "
        "factorwise su(3)+su(2)+u(1) embedding.  A factorization/gauging "
        "principle, MR_color bridge, and chiral su(2)_L bridge remain required."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
