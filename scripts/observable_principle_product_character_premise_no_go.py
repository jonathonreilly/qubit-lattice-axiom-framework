#!/usr/bin/env python3
"""Check that source factoring alone does not force a product-character readout."""

from __future__ import annotations

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail else ""))


def generic(prefix: str, n: int) -> sp.Matrix:
    return sp.Matrix(n, n, lambda i, j: sp.Symbol(f"{prefix}{i}{j}"))


def block_sum(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(sp.BlockDiagMatrix(a, b))


print("=" * 78)
print("A. Source insertion is an operator-product identity")
print("=" * 78)

for n in (2, 3):
    d = sp.Matrix(n, n, lambda i, j: 1 if i == j else (sp.Symbol(f"d{i}{j}") if i < j else 0))
    j = generic("j", n)
    source = sp.eye(n) + d.inv() * j
    residual = sp.simplify(d + j - d * source)
    check(f"D + J = D(I + D^-1 J) for n={n}", residual == sp.zeros(n))

a, b, c, d = sp.symbols("a b c d")
d2 = sp.Matrix([[a, b], [c, d]])
det_d2 = a * d - b * c
d2_inv = sp.Matrix([[d, -b], [-c, a]]) / det_d2
j2 = generic("q", 2)
residual2 = sp.simplify(d2 + j2 - d2 * (sp.eye(2) + d2_inv * j2))
check("D + J identity holds for a generic symbolic 2x2 invertible D",
      residual2 == sp.zeros(2))

print()
print("=" * 78)
print("B. Product and block-sum axes are different")
print("=" * 78)

x = generic("x", 2)
y = generic("y", 2)
check("det(A S) = det(A)det(S) on the product axis",
      sp.simplify((x * y).det() - x.det() * y.det()) == 0)
check("det(A block_sum B) = det(A)det(B) on the block-sum axis",
      sp.simplify(block_sum(x, y).det() - x.det() * y.det()) == 0)
check("tr(A block_sum B) = tr(A) + tr(B)",
      sp.simplify(block_sum(x, y).trace() - x.trace() - y.trace()) == 0)

trace_product_gap = sp.simplify((x * y).trace() - x.trace() * y.trace())
check("trace is not a product character in symbolic 2x2 form",
      trace_product_gap != 0, str(trace_product_gap))

print()
print("=" * 78)
print("C. Concrete trace witness")
print("=" * 78)

a0 = sp.Matrix([[2, 1], [1, 2]])
s0 = sp.Matrix([[3, 0], [1, 4]])
prod_trace = int((a0 * s0).trace())
trace_prod = int(a0.trace() * s0.trace())
trace_sum = int(a0.trace() + s0.trace())
check("concrete matrices are invertible",
      a0.det() != 0 and s0.det() != 0, f"det(A)={a0.det()} det(S)={s0.det()}")
check("tr(A S) differs from tr(A)tr(S)",
      prod_trace != trace_prod, f"tr(AS)={prod_trace}, tr(A)tr(S)={trace_prod}")
check("tr(A S) also differs from tr(A)+tr(S)",
      prod_trace != trace_sum, f"tr(AS)={prod_trace}, tr(A)+tr(S)={trace_sum}")

print()
print("=" * 78)
print("D. Logical implication gap")
print("=" * 78)

fac_true_for_trace = (a0 * s0).trace() is not None
block_sum_additive = sp.simplify(block_sum(a0, s0).trace() - a0.trace() - s0.trace()) == 0
product_character_fails = prod_trace != trace_prod
check("trace reads product operators and is block-sum additive",
      fac_true_for_trace and block_sum_additive)
check("trace satisfies the tested motivations while failing the product law",
      fac_true_for_trace and block_sum_additive and product_character_fails)

det_product_ok = sp.simplify((a0 * s0).det() - a0.det() * s0.det()) == 0
check("det satisfies the product law once that law is supplied",
      det_product_ok)
check("trace separates additive block-sum behavior from product-character behavior",
      block_sum_additive and product_character_fails)

print()
print("=" * 78)
print("N5 EXECUTION CERTIFICATE: WHAT THIS RUNNER RESOLVES")
print("=" * 78)
print(
    "per_element: resolved, and every identity is certified entrywise rather than at "
    "a norm. The source matrices are constructed cell by cell as generic symbol grids "
    "(j00..j11, q00..q11, x00..x11, y00..y11), the unit-diagonal upper-triangular D is "
    "written index by index, and the factorization residual D + J - D(I + D^-1 J) is "
    "compared against the exact zero matrix over all 4 entries at n = 2 and all 9 at "
    "n = 3. The product-character gap is likewise reported as a full symbolic "
    "expression, -x00 y11 + x01 y10 + x10 y01 - x11 y00, not as a magnitude."
)
print(
    "per_site: checked and not executed. There is no lattice and no position index "
    "anywhere in this file. The matrix indices label abstract source and operator "
    "slots, and the block-sum axis is an algebraic direct sum of two matrices rather "
    "than a spatial decomposition, so nothing carries a coordinate, a neighbour or a "
    "volume and no site-resolved amplitude exists to evaluate."
)
print(
    "per_mode: checked and not executed. Nothing is diagonalized in this runner: only "
    "matrix products, inverses, traces and determinants are formed. Trace and "
    "determinant are of course symmetric functions of a spectrum, but they are "
    "computed straight from the entries here, and no eigenvalue, eigenvector or "
    "spectral weight is ever produced, so there is no mode at which to resolve "
    "anything."
)
print(
    "per_block: resolved with amplitudes, and it is exactly the axis the no-go turns "
    "on. The runner builds the block-diagonal sum of two 2 x 2 matrices and certifies "
    "both block laws on it - det(A (+) B) = det(A) det(B) and tr(A (+) B) = tr(A) + "
    "tr(B) - then sets that against the product axis A S, where the same two readouts "
    "part company: on the concrete witness A = [[2, 1], [1, 2]] and S = [[3, 0], "
    "[1, 4]] with determinants 3 and 12, the trace gives tr(AS) = 15 against "
    "tr(A) tr(S) = 28 and tr(A) + tr(S) = 11, while the determinant obeys the product "
    "law exactly."
)
print(
    "lattice_wide: checked and not executed, and the missing global statement is this "
    "note's own boundary. The claim is universal in form - that source factoring does "
    "not force a product character for every scalar readout - but it is established by "
    "exhibiting a single counterexample, the trace, not by classifying the admissible "
    "readouts. The note itself scopes 'does not force' to the two tested "
    "factorization facts and leaves the product-character premise open as admission "
    "work, so no global classification is available to execute."
)
print(
    "  scope: section D adds little beyond recombination. Three of its four checks are "
    "conjunctions of booleans already established in sections B and C, and each of "
    "those conjunctions carries the term (A S).trace() is not None, which is true of "
    "any SymPy result and discriminates nothing. Only the determinant product-law "
    "check in that section computes something new."
)
print(
    "  scope: the concrete leg rests on one witness pair at n = 2 and the symbolic "
    "legs on generic 2 x 2 and 3 x 3 grids; no larger dimension, no singular or "
    "degenerate matrix, and no readout other than trace and determinant is exercised. "
    "The runner is fully deterministic - no RNG stream and no optimizer - with exact "
    "SymPy throughout."
)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("Source factoring and determinant block-sum factoring do not imply")
print("chi(A S)=chi(A)chi(S) for every scalar readout. Trace is the witness.")
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")

if FAIL:
    raise SystemExit(1)
