#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`.

Verifies, on the smallest non-trivial finite blocks, the four operator-
algebra identities the bridge theorem proves:

  (T1) Unitarity:                    T_a T_a^†   = I,    T_a^† T_a = I.
  (T2) Group law:                    T_a T_b     = T_{a+b}.
  (T3) Fermion-operator covariance:  T_a a_x T_a^†   = a_{x+a},
                                     T_a a_x^† T_a^† = a_{x+a}^†.
  (T4) Charge conservation:          [T_a, Q_total]  = 0, Q_total := Σ a_x^† a_x.

The construction stands on A1 (per-site dim-two factor with σ_± ladder
matrices) + A2 (Z^3 lattice translation structure). Every PASS is a
class-(C) algebraic computation on the explicit tensor-product
representation, with framework primitives instantiated as exact sympy
matrices and the identities verified by direct entrywise comparison.

No physics conventions, no PDG values, no fitted inputs, no
floating-point arithmetic.
"""

from __future__ import annotations

import sys
from itertools import product

try:
    import sympy
    from sympy import Matrix, eye, zeros, simplify, Rational
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (C)"
    else:
        FAIL += 1
        tag = "FAIL (C)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def mat_eq(A: Matrix, B: Matrix) -> bool:
    """Exact matrix equality via sympy.simplify on every entry."""
    if A.shape != B.shape:
        return False
    diff = A - B
    return all(simplify(diff[i, j]) == 0 for i in range(diff.rows) for j in range(diff.cols))


def is_zero(M: Matrix) -> bool:
    return all(simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


# ---------------------------------------------------------------------------
# Construction utilities
# ---------------------------------------------------------------------------

# A1 primitives: ladder matrices on the per-site dim-two factor.
SIGMA_PLUS = Matrix([[0, 1], [0, 0]])   # σ_+ : |0⟩ → |1⟩
SIGMA_MINUS = Matrix([[0, 0], [1, 0]])  # σ_- : |1⟩ → |0⟩
ID2 = eye(2)


def tensor_chain(factors):
    """Kronecker product of a non-empty list of sympy Matrices."""
    out = factors[0]
    for f in factors[1:]:
        out = sympy.kronecker_product(out, f)
    return out


def site_op_1d(N: int, x: int, local: Matrix) -> Matrix:
    """Build the operator `I ⊗ ... ⊗ local^{(x)} ⊗ ... ⊗ I` on (C²)^{⊗ N}.

    The tensor-product convention: factor 0 is the leftmost (most-significant)
    in the Kronecker product; basis index for a configuration (b_0, b_1, ..., b_{N-1})
    is b_0 * 2^{N-1} + b_1 * 2^{N-2} + ... + b_{N-1} * 2^0.
    """
    factors = [local if i == x else ID2 for i in range(N)]
    return tensor_chain(factors)


def a_op_1d(N: int, x: int) -> Matrix:
    return site_op_1d(N, x, SIGMA_MINUS)


def adag_op_1d(N: int, x: int) -> Matrix:
    return site_op_1d(N, x, SIGMA_PLUS)


def basis_index_1d(bits: tuple[int, ...]) -> int:
    """Map an N-bit tuple (b_0, ..., b_{N-1}) to a basis index under the
    factor-0-leftmost convention."""
    N = len(bits)
    idx = 0
    for i, b in enumerate(bits):
        idx += b * (1 << (N - 1 - i))
    return idx


def translation_1d(N: int, a: int) -> Matrix:
    """Tensor-permutation cyclic-shift T_a on (C²)^{⊗ N}, 1D periodic block.

    Definition (matches eq. (2) of the source note): on a basis state
    ⊗_x |b_x⟩_x indexed by the tuple (b_0, ..., b_{N-1}), T_a acts by
        T_a (⊗_x |b_x⟩_x)  :=  ⊗_x |b_{(x - a) mod N}⟩_x.
    Built explicitly as a permutation matrix in the basis-index labelling.
    """
    dim = 1 << N
    M = zeros(dim, dim)
    for bits in product((0, 1), repeat=N):
        # Output configuration at factor x is the input bit at site (x - a) mod N.
        out_bits = tuple(bits[(x - a) % N] for x in range(N))
        i_in = basis_index_1d(bits)
        i_out = basis_index_1d(out_bits)
        M[i_out, i_in] = 1
    return M


def q_total_1d(N: int) -> Matrix:
    Q = zeros(1 << N, 1 << N)
    for x in range(N):
        Q = Q + adag_op_1d(N, x) * a_op_1d(N, x)
    return Q


# ---------------------------------------------------------------------------
# 2D utilities (Lx × Ly)
# ---------------------------------------------------------------------------

def basis_index_2d(bits, Lx: int, Ly: int) -> int:
    """Map a (Lx, Ly)-shaped bit tuple to a basis index.

    Sites are enumerated in row-major (i, j) order; factor 0 = (0, 0),
    factor 1 = (0, 1), ..., factor Lx*Ly-1 = (Lx-1, Ly-1).
    """
    flat = [bits[i][j] for i in range(Lx) for j in range(Ly)]
    return basis_index_1d(tuple(flat))


def site_op_2d(Lx: int, Ly: int, ix: int, iy: int, local: Matrix) -> Matrix:
    """Build local^{(ix, iy)} on (C²)^{⊗ Lx*Ly} with row-major factor order."""
    N = Lx * Ly
    flat_site = ix * Ly + iy
    return site_op_1d(N, flat_site, local)


def a_op_2d(Lx: int, Ly: int, ix: int, iy: int) -> Matrix:
    return site_op_2d(Lx, Ly, ix, iy, SIGMA_MINUS)


def translation_2d(Lx: int, Ly: int, ax: int, ay: int) -> Matrix:
    """Tensor-permutation translation T_{(ax, ay)} on the 2D block."""
    N = Lx * Ly
    dim = 1 << N
    M = zeros(dim, dim)
    for bits_flat in product((0, 1), repeat=N):
        bits = [[bits_flat[i * Ly + j] for j in range(Ly)] for i in range(Lx)]
        out_bits = [
            [bits[(ix - ax) % Lx][(iy - ay) % Ly] for iy in range(Ly)]
            for ix in range(Lx)
        ]
        i_in = basis_index_2d(bits, Lx, Ly)
        i_out = basis_index_2d(out_bits, Lx, Ly)
        M[i_out, i_in] = 1
    return M


# ---------------------------------------------------------------------------
# Test sections
# ---------------------------------------------------------------------------

def test_block_1d(N: int) -> None:
    section(f"1D N={N}: T_a unitarity, fermion covariance, charge conservation")
    dim = 1 << N
    Id = eye(dim)
    Q = q_total_1d(N)
    Ts = {a: translation_1d(N, a) for a in range(N)}

    # (T1) Unitarity for every a.
    for a in range(N):
        T = Ts[a]
        check(f"(T1) T_{a} T_{a}^† = I  [N={N}]", mat_eq(T * T.H, Id))
        check(f"(T1) T_{a}^† T_{a} = I  [N={N}]", mat_eq(T.H * T, Id))

    # (T2) Group law T_a T_b = T_{a+b mod N}; T_0 = I; T_N = T_0 = I.
    for a in range(N):
        for b in range(N):
            lhs = Ts[a] * Ts[b]
            rhs = Ts[(a + b) % N]
            check(
                f"(T2) T_{a} T_{b} = T_{(a + b) % N}  [N={N}]",
                mat_eq(lhs, rhs),
            )
    check(f"(T2) T_0 = I  [N={N}]", mat_eq(Ts[0], Id))

    # (T3) Fermion-operator covariance T_a a_x T_a^† = a_{(x+a) mod N}
    # and the adjoint identity; check for every (a, x).
    for a in range(N):
        T = Ts[a]
        Tdag = T.H
        for x in range(N):
            lhs_a = T * a_op_1d(N, x) * Tdag
            rhs_a = a_op_1d(N, (x + a) % N)
            check(
                f"(T3) T_{a} a_{x} T_{a}^† = a_{(x + a) % N}  [N={N}]",
                mat_eq(lhs_a, rhs_a),
            )
            lhs_adag = T * adag_op_1d(N, x) * Tdag
            rhs_adag = adag_op_1d(N, (x + a) % N)
            check(
                f"(T3) T_{a} a_{x}^† T_{a}^† = a_{(x + a) % N}^†  [N={N}]",
                mat_eq(lhs_adag, rhs_adag),
            )

    # (T4) Charge conservation [T_a, Q_total] = 0 for every a.
    for a in range(N):
        T = Ts[a]
        comm = T * Q - Q * T
        check(f"(T4) [T_{a}, Q_total] = 0  [N={N}]", is_zero(comm))


def test_block_2d_two_by_two() -> None:
    section("2D 2×2: independent axis translations and joint covariance")
    Lx, Ly = 2, 2
    N = Lx * Ly
    dim = 1 << N
    Id = eye(dim)

    Tx = translation_2d(Lx, Ly, 1, 0)
    Ty = translation_2d(Lx, Ly, 0, 1)

    # Unitarity of each axis translation.
    check("(T1) T_x T_x^† = I  [Lx=2,Ly=2]", mat_eq(Tx * Tx.H, Id))
    check("(T1) T_y T_y^† = I  [Lx=2,Ly=2]", mat_eq(Ty * Ty.H, Id))

    # Commutativity of the two independent axis translations:
    # T_x T_y = T_y T_x = T_{(1,1)}.
    Txy = translation_2d(Lx, Ly, 1, 1)
    check("(T2) T_x T_y = T_y T_x  [Lx=2,Ly=2]", mat_eq(Tx * Ty, Ty * Tx))
    check("(T2) T_x T_y = T_{(1,1)}  [Lx=2,Ly=2]", mat_eq(Tx * Ty, Txy))

    # (T3) for both axis translations and every site.
    for ix in range(Lx):
        for iy in range(Ly):
            lhs = Tx * a_op_2d(Lx, Ly, ix, iy) * Tx.H
            rhs = a_op_2d(Lx, Ly, (ix + 1) % Lx, iy)
            check(
                f"(T3) T_x a_{{{ix},{iy}}} T_x^† = a_{{{(ix + 1) % Lx},{iy}}}  [Lx=2,Ly=2]",
                mat_eq(lhs, rhs),
            )
            lhs = Ty * a_op_2d(Lx, Ly, ix, iy) * Ty.H
            rhs = a_op_2d(Lx, Ly, ix, (iy + 1) % Ly)
            check(
                f"(T3) T_y a_{{{ix},{iy}}} T_y^† = a_{{{ix},{(iy + 1) % Ly}}}  [Lx=2,Ly=2]",
                mat_eq(lhs, rhs),
            )

    # (T4) Charge conservation for both axes on the 2D block.
    Q = zeros(dim, dim)
    for ix in range(Lx):
        for iy in range(Ly):
            Q = Q + a_op_2d(Lx, Ly, ix, iy).H * a_op_2d(Lx, Ly, ix, iy)
    check("(T4) [T_x, Q_total] = 0  [Lx=2,Ly=2]", is_zero(Tx * Q - Q * Tx))
    check("(T4) [T_y, Q_total] = 0  [Lx=2,Ly=2]", is_zero(Ty * Q - Q * Ty))


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25")
    print("Goal: sympy verification of (T1)-(T4) on small finite blocks of H_Λ = ⊗_x C²_x")
    print("=" * 88)

    for N in (2, 3, 4):
        test_block_1d(N)

    test_block_2d_two_by_two()

    print()
    print("=" * 88)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 88)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
