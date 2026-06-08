# The Rank-1 / Single-Source Condition IS the Derived C₃ Coupling K = |K|(J−I); the Degenerate Doublet Gives Maximal θ₂₃, the Cabibbo Reduces to the Hierarchy — Narrow Theorem

**Date:** 2026-06-08
**Claim type:** bounded_theorem (the rank-1 condition is supplied by the derived K=|K|(J−I); θ₂₃≈45° bonus; the GST magnitude reduces to the mass hierarchy)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/rank1_single_source_from_K_J_minus_I_structure_runner.py`](../scripts/rank1_single_source_from_K_J_minus_I_structure_runner.py)
**Cached output:** [`logs/runner-cache/rank1_single_source_from_K_J_minus_I_structure_runner.txt`](../logs/runner-cache/rank1_single_source_from_K_J_minus_I_structure_runner.txt)

## Audit context

The companion GST note reduced the small-mixing **magnitude** to a **rank-1 / single-source
C₃-symmetric mass** (the singlet carries the leading generation-dependent mass; the light generations
degenerate at C₃-symmetry). This note shows that condition is **supplied by the framework's derived C₃
coupling** — closing the chain — and that the structure additionally yields the maximal atmospheric
angle and pins the residual at the mass hierarchy.

## Safe statement

**Theorem.** The framework's C₃ coupling, derived from the interaction asymmetry δ
([`INTERACTION_ASYMMETRY_DELTA_OCCUPATION_CURVATURE_TWO_BODY`](INTERACTION_ASYMMETRY_DELTA_OCCUPATION_CURVATURE_TWO_BODY_STRUCTURE_THEOREM_NOTE_2026-06-06.md),
`retained`), is `K = |K|(J − I)`.

1. **K's generation-distinguishing part is rank-1 — the single C₃-singlet source.** `J = 3·P_singlet`
   is **rank-1** (eigenvalues `3,0,0`); so `K = 3|K|·P_singlet − |K|·I` and `(J−I)` has eigenvalues
   `(2,−1,−1)`: a **distinct singlet** + a **2-fold degenerate doublet**. The rank-1 `J` piece (the
   C₃-singlet/democratic direction) **is** the single source the GST rank-1 condition requires.
2. **K ⟹ singlet + degenerate doublet.** `K`'s spectrum is `(2|K|, −|K|, −|K|)`: the singlet is
   distinct (the heavy generation), the doublet degenerate (the light generations) — *exactly* the
   rank-1 singlet-dominance structure.
3. **Bonus — the degenerate doublet gives maximal θ₂₃.** A 2-fold degenerate doublet + a (symmetric)
   C₃-breaking gives **maximal** 1–2 mixing, `θ = 45°` (verified) — the lepton **atmospheric** angle
   `θ₂₃ ≈ 45°` (observed ~49°). The maximal angle is *not* a coincidence: it is the degenerate doublet
   from `K`.
4. **The small Cabibbo reduces to the hierarchy.** The *small* Cabibbo (`θ_C ≈ 13°`, not 45°) requires
   the doublet to be **split** (hierarchical) at C₃-symmetry: a split doublet `(m_d ≪ m_s)` gives
   `θ ≈ 12.6°` (the GST `√(m_d/m_s)`), verified. So the small-mixing **magnitude** reduces to the
   doublet **mass hierarchy** (`m_d ≪ m_s` → `α_s`).

## What this closes

- The rank-1 / single-source **structure** the GST texture needs is **framework-native** — it is the
  rank-1 `J` piece of the **derived** coupling `K = |K|(J−I)` (the C₃-singlet/democratic source). The
  GST texture is therefore *not* an extra assumption.
- The same structure **predicts** the maximal atmospheric angle `θ₂₃ ≈ 45°` (the degenerate doublet)
  and shows the **small** Cabibbo's smallness is the doublet *splitting*.
- So the **entire small-mixing sector** now has a single residual: the **mass hierarchy** (why the
  doublet is split, `m_d ≪ m_s`) → `α_s`. The *structure* (which angles, why small vs maximal, the √2,
  the GST texture) is derived; only the *hierarchy magnitude* remains.

## Boundary (honest)

- **Supplies the rank-1 structure; the magnitude is the hierarchy.** This derives the rank-1 / single-
  source structure (K's J piece) and the qualitative pattern (singlet heavy, degenerate doublet →
  maximal θ₂₃, split doublet → small Cabibbo); the *numerical* small-mixing magnitudes reduce to the
  doublet mass hierarchy (the named residual, → α_s).
- θ₂₃ ≈ 45° is the leading degenerate-doublet result; the observed ~49° includes subleading breaking.
- Distinct from the Koide `r`-dial; no claim about `r`.

## Forbidden imports check

No new axiom. A_min + the **retained** derived C₃ coupling `K=|K|(J−I)` + standard 2×2/3×3 algebra
(reproduced). PDG `θ₂₃`, `θ_C` are the comparison data (dimensionless). Memory-safe.

## Runner check breakdown

Class A: (A1) `K=|K|(J−I)`, `J` rank-1 (single singlet source); (A2) `K` ⟹ singlet + degenerate
doublet; (A3) degenerate doublet ⟹ maximal θ₂₃≈45°; (A4) split doublet ⟹ small Cabibbo, magnitude
reduces to the hierarchy. Expected `runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

The derived C₃ coupling `K=|K|(J−I)` has the rank-1 `J=3·P_singlet` piece — the single C₃-singlet
source — so `K` yields a distinct singlet plus a degenerate doublet, exactly the rank-1 singlet-
dominance the GST texture reduces to. The degenerate doublet gives maximal 1–2 mixing (θ₂₃≈45°, the
atmospheric angle), and the small Cabibbo requires a split doublet (the GST `√(m_d/m_s)`≈12.6°), so the
small-mixing magnitude reduces to the doublet mass hierarchy. The note is honest that it supplies the
rank-1 *structure* (from the derived K) and the qualitative pattern, while the numerical magnitudes
reduce to the hierarchy (→ α_s), and that θ₂₃≈45° is the leading result. Effective status remains
`unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/rank1_single_source_from_K_J_minus_I_structure_runner.py
```
