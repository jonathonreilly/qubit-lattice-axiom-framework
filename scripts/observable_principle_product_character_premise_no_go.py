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
print("VERDICT")
print("=" * 78)
print("Source factoring and determinant block-sum factoring do not imply")
print("chi(A S)=chi(A)chi(S) for every scalar readout. Trace is the witness.")
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")

if FAIL:
    raise SystemExit(1)
