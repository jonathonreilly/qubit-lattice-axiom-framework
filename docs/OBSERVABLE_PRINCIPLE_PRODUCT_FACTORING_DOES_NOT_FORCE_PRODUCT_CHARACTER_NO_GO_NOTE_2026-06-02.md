# Product Factoring Does Not Force the Observable Product-Character Law

**Date:** 2026-06-02
**Claim type:** no_go
**Review provenance:** source theorem candidate; post-landing review decides the
ledger grade. This note introduces no axiom, primitive, Tier-A admission, or
observable-principle registry change.
**Primary runner:** `scripts/observable_principle_product_character_premise_no_go.py`
(SCORECARD PASS=14)

## Claim

The source-factorization facts behind the determinant form-selection theorem do
not by themselves derive the product-character readout law

```text
chi(A S) = chi(A) chi(S).                         (M)
```

The determinant form-selection theorem remains a valid theorem once `(M)` is
supplied. This note checks a narrower question: whether `(M)` follows from the
usual source-insertion motivations.

The answer is no. The facts

```text
D + J = D (I + D^{-1} J)
det(A block_sum B) = det(A) det(B)
```

are true, but they constrain the operator argument and the Berezin weight. They
do not constrain every scalar readout on the operator product. The trace is a
counterexample: `tr(A S)` is a well-defined scalar readout of a product operator
and `tr(A block_sum B) = tr(A) + tr(B)`, yet generically

```text
tr(A S) != tr(A) tr(S).
```

Therefore the bridge

```text
source insertion is multiplicative
        -> scalar readout must be a product character
```

is an additional product-character premise, not a consequence of those
factorization facts alone.

## Boundary

This note does not claim `(M)` is false or unmotivated. It does not alter the
determinant form-selection theorem, does not derive or reject P1, and does not
register any new admitted premise. It only rules out the route that tries to
derive `(M)` from operator source factoring plus independent-patch determinant
factorization.

## Computation

The runner verifies:

1. `D + J = D (I + D^{-1}J)` for symbolic invertible matrices.
2. `det(A S) = det(A)det(S)` for symbolic matrices.
3. `det(A block_sum B) = det(A)det(B)`.
4. `tr(A block_sum B) = tr(A) + tr(B)`.
5. Concrete invertible matrices give `tr(A S) != tr(A)tr(S)`.
6. The trace witness satisfies the two source-factorization motivations while
   failing `(M)`.
7. The product axis and the block-sum axis are distinct; determinant selection
   and additive exponent selection are different steps.

## No-Go Discipline Gate

**Gate result:** PASS for the scoped product-character-premise no-go only.

### N1 - Alternative Route Enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Source-product route | Use `D + J = D(I + D^{-1}J)` to force every readout to be product-multiplicative. | The identity is about the operator argument; `tr(D(I + D^{-1}J))` is well-defined and need not factor. | ATTEMPTED |
| Independent-patch route | Use determinant factorization over block sums to force `(M)`. | That factorization is a determinant-weight fact on the block-sum axis; trace is additive on the same block-sum axis. | ATTEMPTED |
| Trace-exclusion route | Exclude trace from source factoring alone. | Trace respects the tested source-factoring motivations but fails `(M)`, so source factoring alone does not exclude it. | ATTEMPTED |
| Product-axis theorem route | Use the determinant character theorem itself to derive `(M)`. | The theorem assumes `(M)`; using it to prove `(M)` is circular. | ATTEMPTED |
| P1-additivity route | Use independent-subsystem additivity to force the product-character law. | Additivity lives on the block-sum axis; trace separates that axis from the product-character axis. | ATTEMPTED |
| Owner-approved product-character premise | Add `(M)` as an explicit premise. | Out of scope and left open; this would be governance/admission work, not a derivation from the two tested facts. | OUT OF SCOPE |

### N2 - Wall-Independence Audit

The collapsed wall set has one wall: the tested source-factorization facts do
not imply the readout law `(M)`. The routes above are different tests of that
same implication gap.

### N3 - Hidden-Wall Scan

Phrase scan result: no load-bearing step uses "we assume", "by construction",
"as is standard", "the framework provides", "bridge context", "naturally",
"obviously", or "canonical" as proof support. The proof uses explicit matrix
identities and a trace counterexample.

### N4 - Residual Matching

The residual attacked here is only:

```text
source-factorization facts -> product-character readout law.
```

It is not the residual of selecting `det` after `(M)` is supplied, and it is not
the residual of selecting `log` inside the determinant family.

### N5 - Rhetoric Audit

"Does not force" is scoped to the two tested factorization facts. It does not
mean the product-character law is wrong, physically useless, or unavailable as
an explicit premise.

### N6 - Partial-Closure Path Scan

Open paths remain: explicitly approve `(M)` as a product-character premise,
derive `(M)` from a stronger source/readout theorem, or keep the determinant
form-selection theorem conditional on `(M)`.

### N7 - Steelman

A hostile reviewer can argue that the physical scalar readout is not an
arbitrary scalar functional: the Berezin integral already computes a determinant,
so the determinant character should be the physical readout. That is a strong
motivation for `(M)`. It does not derive the general product-character readout
law from the two tested facts; it supplies the missing readout premise.

### N8 - Cross-Cycle Echo

The repeated failure mode is to move from "the operator weight factors" to "the
readout law is forced" without checking the quantifier shift. This note keeps
those levels separate: operator identities and determinant-weight
factorization are true, but the product-character readout law remains an extra
step unless proved separately.

## Command

```bash
python3 scripts/observable_principle_product_character_premise_no_go.py
```

Expected output: `SCORECARD: PASS=14 FAIL=0`.
