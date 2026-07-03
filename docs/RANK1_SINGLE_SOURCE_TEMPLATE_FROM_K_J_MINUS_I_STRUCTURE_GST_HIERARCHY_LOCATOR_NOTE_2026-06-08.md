# The Derived C₃ Coupling K = |K|(J−I) Supplies a Rank-1 / Single-Source Template; GST Magnitudes Still Reduce to the Hierarchy — Locator Note

**Date:** 2026-06-08
**Claim type:** bounded_theorem (structural locator: derived `K=|K|(J−I)` supplies the rank-1 singlet-plus-doublet template; GST magnitudes still require the mass hierarchy)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/rank1_single_source_from_K_J_minus_I_structure_runner.py`](../scripts/rank1_single_source_from_K_J_minus_I_structure_runner.py)
**Cached output:** [`logs/runner-cache/rank1_single_source_from_K_J_minus_I_structure_runner.txt`](../logs/runner-cache/rank1_single_source_from_K_J_minus_I_structure_runner.txt)

## Audit context

The companion GST note reduced the small-mixing **magnitude** to a **rank-1 / single-source
C₃-symmetric mass plus single-source breaking**. This note shows that the framework's derived C₃
coupling supplies the same **singlet-plus-degenerate-doublet structural template**. It does not, by
itself, identify that coupling with the physical mass operator or close the small-angle magnitude
chain.

## Safe statement

**Theorem.** The framework's C₃ coupling, derived from the interaction asymmetry δ
([`INTERACTION_ASYMMETRY_DELTA_OCCUPATION_CURVATURE_TWO_BODY`](INTERACTION_ASYMMETRY_DELTA_OCCUPATION_CURVATURE_TWO_BODY_STRUCTURE_THEOREM_NOTE_2026-06-06.md),
`retained`), is `K = |K|(J − I)`.

1. **K's generation-distinguishing part is rank-1 — the single C₃-singlet template.** `J = 3·P_singlet`
   is **rank-1** (eigenvalues `3,0,0`); so `K = 3|K|·P_singlet − |K|·I` and `(J−I)` has eigenvalues
   `(2,−1,−1)`: a **distinct singlet** + a **2-fold degenerate doublet**. The rank-1 `J` piece (the
   C₃-singlet/democratic direction) matches the single-source structure the GST rank-1 condition
   requires, subject to the separate mass/readout identification.
2. **K ⟹ singlet + degenerate doublet.** `K`'s spectrum is `(2|K|, −|K|, −|K|)`: the singlet is
   distinct, the doublet degenerate — the rank-1 singlet-dominance template.
3. **Degenerate-doublet mixing locator.** In a reduced two-state model, a 2-fold degenerate doublet
   plus symmetric C₃-breaking gives **maximal** 1–2 mixing, `θ = 45°` (verified). This is a leading
   atmospheric-angle candidate pattern, not a prediction from this note alone.
4. **The small Cabibbo reduces to the hierarchy.** The *small* Cabibbo (`θ_C ≈ 13°`, not 45°) requires
   the doublet to be **split** (hierarchical) at C₃-symmetry: a split doublet `(m_d ≪ m_s)` gives
   `θ ≈ 12.6°` in the GST toy block, verified. So the small-mixing **magnitude** still reduces to
   the doublet **mass hierarchy** (`m_d ≪ m_s` → `α_s`), not to `K` alone.

## What this closes

- The rank-1 / single-source **template** the GST texture needs is present in a framework-native
  object: the rank-1 `J` piece of the **derived** coupling `K = |K|(J−I)` (the C₃-singlet/democratic
  source).
- The same template gives a leading maximal-mixing pattern in a degenerate two-state block and shows
  why small mixing requires a split/hierarchical doublet in the GST block.
- The remaining residuals are explicit: identify the relevant physical mass/readout operator and
  derive the doublet mass hierarchy (`m_d ≪ m_s` → `α_s`). This note does not close those residuals.

## Boundary (honest)

- **Supplies a rank-1 template; the magnitude is still the hierarchy.** This identifies the rank-1 /
  single-source structure in `K` and a qualitative pattern (singlet/doublet split, degenerate-doublet
  maximal mixing in the reduced block, split doublet → small Cabibbo). It does **not** prove that `K`
  is the physical mass operator.
- θ₂₃ ≈ 45° is a leading degenerate-doublet candidate pattern; the observed ~49° is comparator-only.
- Distinct from the Koide `r`-dial; no claim about `r`.

## Forbidden imports check

No new axiom. A_min + the derived C₃ coupling `K=|K|(J−I)` + standard 2×2/3×3 algebra
(reproduced). PDG `θ₂₃`, `θ_C` are comparison data only (dimensionless). Memory-safe.

## Runner check breakdown

Class A: (A1) `K=|K|(J−I)`, `J` rank-1 (single singlet template); (A2) `K` ⟹ singlet + degenerate
doublet; (A3) degenerate doublet ⟹ maximal mixing in a reduced block; (A4) split doublet ⟹ small
Cabibbo in the GST toy block, magnitude still reduces to the hierarchy. Expected
`runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

The derived C₃ coupling `K=|K|(J−I)` has the rank-1 `J=3·P_singlet` piece — the single C₃-singlet
template — so `K` yields a distinct singlet plus a degenerate doublet, matching the structural pattern
the GST texture reduces to. In reduced two-state blocks, a degenerate doublet gives maximal mixing
and a split doublet gives the GST small-angle scaling. The note is honest that it supplies a locator,
not a closure: the physical mass/readout identification and the hierarchy magnitude remain residuals.
Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/rank1_single_source_from_K_J_minus_I_structure_runner.py
```
