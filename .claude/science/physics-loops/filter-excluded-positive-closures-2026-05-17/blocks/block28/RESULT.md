# Block 28 RESULT — axiom_first_cluster_decomposition_theorem_note_2026-04-29

**Date:** 2026-05-17
**Status:** positive narrow closure (bounded conditional theorem) landed.

## What landed

**Source theorem note:**
`docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md`

**Runner:**
`scripts/cluster_decomposition_spatial_slab_bridge_check.py`

**Cached output:**
`logs/runner-cache/cluster_decomposition_spatial_slab_bridge_check.txt`
`outputs/cluster_decomposition_spatial_slab_bridge_check_2026-05-17.txt`

**Block artifacts:** this directory.

## What was closed

The auditor's `verdict_rationale` on the parent row names two repair
targets:

> (a) derive Δ_T > 0 on the canonical Cl(3) ⊗ Z^3 staggered + Wilson
>     Hamiltonian, AND
> (b) add a retained spatial cluster-decomposition theorem with constants.

The 2026-05-09 mass-gap bridge note
`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`
already addresses the *temporal* half of (b) as a closed-form
conditional theorem (B.1)-(B.2), conditional on Δ_T > 0.

Block 28 lands the **spatial direction mirror**: a closed-form
conditional theorem (S.1)-(S.2) on the spatial slab transfer matrix,
conditional on
- **H1.** existence of a positive Hermitian slab transfer matrix `T_x`,
- **H2.** `Δ_x := -log(λ_1(T_x)/M_x) > 0`.

This puts the spatial direction at the *same authority level* the
temporal direction reached with the 2026-05-09 bridge. Repair target
(b) is satisfied at the conditional-closed-form level.

## What remains open

- (a) Δ_T > 0 derivation on the canonical Hamiltonian (unchanged).
- (H1) slab transfer-matrix existence on the canonical Hamiltonian
  (requires either spatial OS reflection positivity along axis x, or
  a direct columnar slab-positivity argument).
- (H2) Δ_x > 0 derivation on the canonical Hamiltonian (same difficulty
  class as Δ_T > 0).
- All three remain explicitly named open inputs of the bounded
  conditional theorem (S); the spatial bridge does not derive them.

The parent row's L2 unconditional spatial claim therefore remains
`audited_conditional` until *all three* open inputs are derived. The
spatial bridge does not promote the parent row.

## Runner results

```
S1 (spatial spectral identity S.6):    PASS  (10/10 trials, max err < 1e-9)
S2 (ground-state spatial bound S.7):   PASS  (200/200 = 100%)
S3 (thermal spatial bound S.8):        PASS  (640/640 = 100%)
S4 (no-gap spatial counter-example):   PASS  (5/5 trials, |connc| ≈ 1.0 at sep=20)
S5 (temporal/spatial parallelism):     PASS  (80/80 bounds identical at 1e-12)
                                       -----
                                       5/5 PASS
```

## Distinctness from block 25

Block 25 landed a Case-A `det(M_KS + mI) > 0` closed-form sub-theorem
of the **OS reflection positivity** axiom — a determinant positivity
result for the staggered Dirac operator at the linear-algebra level.

Block 28 (this block) lands a closed-form spectral-decomposition + 
Cauchy-Schwarz bound on the **cluster decomposition** axiom in the
spatial direction — a finite-dim spectral identity result for a slab
transfer matrix.

Different OS axiom; different proof shape (RP positivity → determinant
positivity vs. spectral-gap input → exponential decay); different
target row.

## V1-V5 enumeration

See `V_CANDIDATES.md`. V3 (spatial-slab mirror) was selected as the
cheapest narrow positive theorem that directly addresses repair
target (b); V1 (slab transfer-matrix existence) is a strictly weaker
sub-step listed as one of V3's hypotheses (H1); V4 (Δ_T > 0 strong-
coupling) is too large for one block and was deferred; V5 (spatial↔
temporal gap equivalence) requires Z^4 framing outside this row's
scope.

## Hard-rule compliance

- A_min only: yes.
- Source-only PR: yes (1 source note + 1 runner + 1 cached output +
  block artifacts).
- No atlas / harness / audit-data touches: yes (no edits to
  `docs/audit/data/*`).
- No main push: enforced by branch.
- No merge: PR opened, not merged.

## Honest verdict

Bounded conditional theorem landed. Repair target (b) satisfied at the
same authority level the temporal bridge satisfied repair target (a)'s
temporal half. Three open derivation targets remain explicitly named
on the bridge note's H1, H2 list (spatial) and on the 2026-05-09
bridge's `Δ_T > 0` (temporal).
