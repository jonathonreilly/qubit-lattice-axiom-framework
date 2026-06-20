#!/usr/bin/env python3
"""Exact finite checks for the gauge factor-local selector normalizer theorem.

The runner works only on the supplied carrier H = C^3(base) x C^2(fiber).
It proves a finite matrix-algebra statement: infinitesimal generators whose
commutator derivations preserve the two supplied factor observable algebras are
exactly u(3) x I_2 + I_3 x u(2), i.e. su(3) + su(2) + u(1) after removing the
shared center. It does not derive MR_color, the physical factor-locality rule,
chiral su(2)_L, gauge dynamics, or an audit verdict.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/GAUGE_FACTOR_LOCAL_SELECTOR_NORMALIZER_THEOREM_NOTE_2026-06-18.md"
PARENT = ROOT / "docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md"

PASS = 0
FAIL = 0
TOL = 1e-8


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(ok))
    FAIL += int(not ok)


def hermitian_u_basis(n: int) -> list[np.ndarray]:
    """Real Hermitian basis for u(n)."""
    basis: list[np.ndarray] = []
    for i in range(n):
        mat = np.zeros((n, n), dtype=complex)
        mat[i, i] = 1.0
        basis.append(mat)
    for i in range(n):
        for j in range(i + 1, n):
            sym = np.zeros((n, n), dtype=complex)
            sym[i, j] = sym[j, i] = 1.0
            asym = np.zeros((n, n), dtype=complex)
            asym[i, j] = -1j
            asym[j, i] = 1j
            basis.extend([sym, asym])
    return basis


def pauli() -> list[np.ndarray]:
    return [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]


def gell_mann() -> list[np.ndarray]:
    return [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3),
    ]


def vec_real(mat: np.ndarray) -> np.ndarray:
    return np.concatenate([mat.real.reshape(-1), mat.imag.reshape(-1)])


def rank(mats: list[np.ndarray], tol: float = TOL) -> int:
    if not mats:
        return 0
    arr = np.array([vec_real(mat) for mat in mats])
    return int(np.linalg.matrix_rank(arr, tol=tol))


def complement_projector(target_mats: list[np.ndarray]) -> np.ndarray:
    columns = np.array([vec_real(mat) for mat in target_mats], dtype=float).T
    u, s, _ = np.linalg.svd(columns, full_matrices=True)
    r = int(np.sum(s > TOL))
    return u[:, r:]


def residual_to_span(mat: np.ndarray, comp: np.ndarray) -> float:
    return float(np.linalg.norm(comp.T @ vec_real(mat)))


def derivation(generator: np.ndarray, observable: np.ndarray) -> np.ndarray:
    return 1j * (generator @ observable - observable @ generator)


def main() -> int:
    print("GAUGE FACTOR-LOCAL SELECTOR NORMALIZER THEOREM")
    print("=" * 72)

    i2 = np.eye(2, dtype=complex)
    i3 = np.eye(3, dtype=complex)
    i6 = np.eye(6, dtype=complex)

    u3 = hermitian_u_basis(3)
    u2 = hermitian_u_basis(2)
    u6 = hermitian_u_basis(6)
    gm = gell_mann()
    ps = pauli()

    base_alg = [np.kron(a, i2) for a in u3]
    fiber_alg = [np.kron(i3, b) for b in u2]
    local_basis = [np.kron(a, i2) for a in gm] + [np.kron(i3, p) for p in ps] + [i6]
    cross_basis = [np.kron(a, p) for a in gm for p in ps]

    local_dim = rank(local_basis)
    cross_dim = rank(cross_basis)
    full_dim = rank(local_basis + cross_basis)

    check(
        "local factor-preserving span has dimension 12 = 8 + 3 + 1",
        local_dim == 12,
        f"rank(local)={local_dim}",
    )
    check(
        "cross-factor tensors have dimension 24",
        cross_dim == 24,
        f"rank(cross)={cross_dim}",
    )
    check(
        "local plus cross spans full u(6), dimension 36",
        full_dim == 36 and rank(u6) == 36,
        f"rank(local+cross)={full_dim}; rank(u6)={rank(u6)}",
    )

    comp_base = complement_projector(base_alg)
    comp_fiber = complement_projector(fiber_alg)

    rows: list[np.ndarray] = []
    for obs in base_alg:
        projections = [comp_base.T @ vec_real(derivation(gen, obs)) for gen in u6]
        rows.extend(np.array(projections).T)
    for obs in fiber_alg:
        projections = [comp_fiber.T @ vec_real(derivation(gen, obs)) for gen in u6]
        rows.extend(np.array(projections).T)
    constraint_matrix = np.vstack(rows)
    constraint_rank = int(np.linalg.matrix_rank(constraint_matrix, tol=TOL))
    normalizer_nullity = len(u6) - constraint_rank

    check(
        "factor-algebra preservation constraints have nullity 12 inside u(6)",
        normalizer_nullity == 12,
        f"constraint_rank={constraint_rank}; nullity={normalizer_nullity}",
    )

    max_local_residual = 0.0
    for gen in local_basis:
        for obs in base_alg:
            max_local_residual = max(
                max_local_residual,
                residual_to_span(derivation(gen, obs), comp_base),
            )
        for obs in fiber_alg:
            max_local_residual = max(
                max_local_residual,
                residual_to_span(derivation(gen, obs), comp_fiber),
            )
    check(
        "every local generator preserves both factor observable algebras",
        max_local_residual < 1e-9,
        f"max residual={max_local_residual:.3e}",
    )

    cross_witnesses = []
    for gen in cross_basis:
        max_residual = 0.0
        for obs in base_alg:
            max_residual = max(max_residual, residual_to_span(derivation(gen, obs), comp_base))
        for obs in fiber_alg:
            max_residual = max(max_residual, residual_to_span(derivation(gen, obs), comp_fiber))
        cross_witnesses.append(max_residual)
    min_cross_violation = min(cross_witnesses)
    check(
        "every nonzero su(3) x su(2) cross tensor fails factor-algebra preservation",
        min_cross_violation > 1e-6,
        f"minimum cross residual={min_cross_violation:.3e}",
    )

    comp_local = complement_projector(local_basis)
    max_lie_residual = 0.0
    for a in local_basis:
        for b in local_basis:
            max_lie_residual = max(
                max_lie_residual,
                residual_to_span(derivation(a, b), comp_local),
            )
    check(
        "local factor-preserving span is Lie closed",
        max_lie_residual < 1e-9,
        f"max Lie residual={max_lie_residual:.3e}",
    )

    max_su3_su2_comm = max(
        np.linalg.norm(np.kron(a, i2) @ np.kron(i3, p) - np.kron(i3, p) @ np.kron(a, i2))
        for a in gm
        for p in ps
    )
    check(
        "su(3) x I_2 and I_3 x su(2) commute inside the selected local span",
        max_su3_su2_comm < 1e-12,
        f"max commutator norm={max_su3_su2_comm:.3e}",
    )

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    firewall_phrases = [
        "does **not** supply that physical bridge",
        "It does not derive why gauge generators must preserve the factor observable",
        "It does not derive chiral `su(2)_L`",
        "It does not update audit ledgers",
    ]
    for phrase in firewall_phrases:
        check(f"source-note firewall present: {phrase}", phrase in note)
    check(
        "source note names parent as trace target without markdown back-edge",
        "`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md`" in note
        and "](GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md)" not in note,
    )
    check(
        "parent note records the factor-local normalizer addendum",
        "GAUGE_FACTOR_LOCAL_SELECTOR_NORMALIZER_THEOREM_NOTE_2026-06-18.md" in parent
        and "Factor-local normalizer addendum" in parent,
    )

    print("=" * 72)
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT (exact-support boundary): on the supplied C^3 x C^2 carrier, "
        "factor-observable preservation has the unique 12-dimensional normalizer "
        "su(3)+su(2)+u(1). The 24 cross tensors are precisely the nonlocal "
        "complement to full u(6). This proves the finite algebra once a "
        "factor-local rule is supplied; it does not derive MR_color, the rule's "
        "physical source, chiral su(2)_L, or any audit status."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
