# Flavor - Log-Det Factor 2 Disconnected-Block Record-Readout Lemma

**Date:** 2026-06-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** finite disconnected/block-diagonal Grassmann determinant
products realize a multiplicative finite scalar record-readout surface. This
does not discharge the full Factor 2 claim for a coupled KS Grassmann
partition.
**Status authority:** independent audit lane only. This note sets no audit
status and assigns no effective grade.
**Runner:** [scripts/flavor_logdet_factor_2_record_readout_realization_2026_06_04.py](../scripts/flavor_logdet_factor_2_record_readout_realization_2026_06_04.py)
**Runner cache:** [logs/runner-cache/flavor_logdet_factor_2_record_readout_realization_2026_06_04.txt](../logs/runner-cache/flavor_logdet_factor_2_record_readout_realization_2026_06_04.txt)
**Depends:**
[FLAVOR_LOGDET_GENERATOR_THREE_FACTOR_PROVENANCE_2026-06-04.md](FLAVOR_LOGDET_GENERATOR_THREE_FACTOR_PROVENANCE_2026-06-04.md)
(roadmap),
[MINIMAL_AXIOMS_2026-06-04.md](MINIMAL_AXIOMS_2026-06-04.md)
(Lattice/Record baseline statement; not a status source), and
[STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md)
(Grassmann substrate support, currently bounded/unaudited).

```yaml
target_claim_type: bounded_theorem
proposed_claim_type: bounded_theorem
trace_class: finite_disconnected_block_realization
factor_2_full_closure: false
record_baseline_status_source: false
```

## Claim

Let `Lambda` be a finite block of the `Z^3` lattice. For a declared
partition of `Lambda` into mutually disjoint record components

```text
Lambda = Lambda_1 sqcup ... sqcup Lambda_k,
```

suppose the finite Grassmann operator restricted to those components is
block diagonal:

```text
M = (D_1 + J_1) oplus ... oplus (D_k + J_k).
```

Then the amplitude

```text
F(Lambda_1 sqcup ... sqcup Lambda_k)
  := product_i det(D_i + J_i)
```

is a multiplicative finite scalar record-readout surface:

- each component amplitude is a finite scalar determinant;
- `F(empty) = 1`;
- for disjoint component collections `A` and `B`,
  `F(A sqcup B) = F(A) F(B)`;
- the logarithmic readout `I(A) = log|F(A)|` is additive where the
  determinants are nonzero.

This is the valid finite-block realization supplied by the runner.

## Boundary

This note does **not** prove that a general coupled KS Grassmann partition

```text
det(D|_{Lambda'} + J|_{Lambda'})
```

is multiplicative over arbitrary disjoint subcollections. If `D` has off-block
couplings between `Lambda_1` and `Lambda_2`, the determinant of the principal
block on `Lambda_1 sqcup Lambda_2` generally contains cross terms and need not
equal the product of the two component determinants. The runner includes a
hostile check demonstrating that failure.

Therefore Factor 2 remains incomplete after this note. The remaining
load-bearing task is to derive a physical/block-decoupling reason, an
equivalent component factorization, or a different record-readout map for the
coupled KS Grassmann surface.

## Relation To The Record Baseline

The approved Record baseline says finite scalar record readouts are additive over
disjoint record collections once the record-readout surface is specified. This
note supplies one bounded finite disconnected-block surface. It does not derive
Record additivity, does not treat Record as a status source, and does
not turn any axiom or primitive into evidence for a downstream grade.

The conditional log-det form theorem
`FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM_2026-06-04.md`, the Factor 3
det-character theorem, and the Factor 4a/4b source-action surfaces remain
separate claims. They are not discharged here.

## Runner Checks

The runner verifies:

- finite site set and empty determinant convention;
- finite scalar determinant and explicit Leibniz/Berezin determinant identity
  on a small block;
- multiplicativity and logarithmic additivity for declared block-diagonal
  component products;
- non-Hermitian and real-matrix sanity cases;
- a hostile coupled-principal-determinant counterexample where
  multiplicativity fails when off-block couplings are present;
- trace-surface and non-finite-operator rejection checks;
- load-bearing source paths exist.

## What This Does Not Claim

- It does not close full log-det Factor 2.
- It does not prove a general coupled KS Grassmann determinant is a record
  readout over arbitrary disjoint subsets.
- It does not derive or modify the Record baseline.
- It does not discharge Factors 3, 4a, or 4b.
- It does not promote any log-det-dependent row.
- It does not introduce a new axiom, primitive, admission, or import.
- It does not apply an audit verdict.
