# Real-Diagonal Source Det-Positivity + Log Readout (Self-Contained Lemma)

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. No audit verdict asserted; no
promotion language. Introduces no new axiom, no fitted/imported value.
**Primary runner:**
[`scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py`](../scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py)
(SCORECARD PASS=4 FAIL=0, exact numpy).

## Why this lemma exists (audit-graph decoupling)

The observable-principle parent
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` needs exactly one fact to make its old
**P2** (phase-blind vs phase-sensitive) distinction vacuous on the consumed real
source surface: that the source-dressed determinant is a **strictly positive
real** number (no phase). It had been citing that fact from the application note
`OBSERVABLE_PRINCIPLE_POSITIVE_SOURCE_CONE_P2_ELIMINATION_NARROW_THEOREM_NOTE_2026-06-06.md`,
which in turn depends on the parent — a load-bearing **2-cycle** (parent ↔
application, both unaudited) that stalled ~722 downstream rows from ever reaching
the auditor dispatch queue.

This lemma **extracts the self-contained fact the parent actually needs**. It is
pure linear algebra plus the Record additivity premise; it consumes **none** of
the parent. The parent now depends on this lemma (one-directional); the
application note keeps depending on the parent — breaking the cycle.

## Statement

Let `D` be a real antisymmetric finite matrix (`D^T = -D`) and `S` a real
positive-diagonal matrix (the positive source cone). Then:

- **(L1) Det-positivity.** `det(S + D) > 0` — a strictly positive real number,
  with **no determinant phase**. Proof: `S + D = S^{1/2}(I + B)S^{1/2}` with
  `B = S^{-1/2} D S^{-1/2}` real antisymmetric; `eig(B) ∈ {0, ±iλ_k}`, so
  `det(I + B) = ∏_k (1 + λ_k^2) ≥ 1 > 0`, and `det S > 0`.
- **(L2) Sign-constant derivative patch.** For invertible real antisymmetric `D`
  and a real diagonal source `J` with `‖D^{-1} J‖ < 1`, the path `D + tJ`
  (`t ∈ [0,1]`) is invertible (Neumann) and its real determinant never crosses
  zero, so it keeps the positive sign of `det D = ∏_k λ_k^2 > 0`. Hence
  `det(D + J) ∈ ℝ_{>0}` on a concrete finite local-source neighborhood.
- **(L3) Log readout selected on `ℝ_{>0}` under explicit regularity.** The
  determinant is multiplicative over disjoint blocks
  (`det(A ⊕ B) = det A · det B`). The Record axiom supplies only finite scalar
  additivity over disjoint records. With the additional explicit finite-block
  continuity/regularity convention on `ℝ_{>0}`, the readout family satisfies the
  multiplicative-to-additive Cauchy equation, whose continuous solutions are
  `W_c = c · log det`; `c = 1` is the conventional representative.

## What this is and is not

- **Is:** the self-contained det-positivity + log-readout fact (L1–L3), reproven
  from linear algebra + the Record additivity premise; the exact fact the
  observable-principle parent consumes for its P2-vacuity step.
- **Is not:** it does **not** derive the observable principle, the source-response
  theorem, any species/flavor content, or a numerical value; it does **not**
  depend on the observable-principle parent or on the P2-elimination application
  note. It is a one-directional input.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Record
  axiom supplies only the finite scalar additivity over disjoint records used in
  (L3). The axiom baseline chain-satisfies as an approved premise.
- Explicit regularity/baseline conventions — continuity on the positive real
  determinant branch and the choice `c=1` are conventions for this bounded
  lemma, not supplied by Record and not promoted as axioms.
- (L1), (L2) are elementary linear algebra (real antisymmetric spectrum,
  Neumann bound), reproven in the runner, not imported.

## Forbidden-imports check

No PDG / fitted / literature numerical comparator is consumed. The
real-antisymmetric spectral fact, the Neumann bound, and the Cauchy
functional-equation solution are reproven in the runner.
