# Multi-Factor Connes-Lott Purchases, Does Not Derive, the Koide (1,1) Multiplicity (Narrow Obstruction + Campaign Convergence)

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow, route-specific) — prunes the multi-factor Connes-Lott route
(#3), the last open dynamical route to the Koide r=1/2. With it, the dynamical class is
exhausted; this note also records the campaign convergence using repo-canonical vocabulary.
**Claim scope:** any **flavor-blind** extra algebra factor (trivial C3-action: chirality
`H_L (+) H_R`, color, KO/real-structure doubling) multiplies the C3 singlet and doublet
isotypes **equally**, preserving the `(1,2)` real-dimension weighting (F3, kappa=1, r=1).
Reaching the `(1,1)` multiplicity weighting (F1, kappa=2, r=1/2) requires a
**flavor-dependent**, isotype-distinguishing operator `W = P_+ + (1/2) P_doublet` (relative
factor 2 on the doublet) — i.e. flavor structure **admitted**, not a separate clean factor.
So multi-factor Connes-Lott **purchases** r=1/2; it does not derive it.
**actual_current_surface_status:** exact structural pruning of the multi-factor route;
**conditional** on the open staggered-Dirac realization gate. Not retained on the current surface.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_multifactor_cannot_cleanly_give_koide_multiplicity_exact.py`](./../scripts/audit_companion_multifactor_cannot_cleanly_give_koide_multiplicity_exact.py)

## Context (physics-loop dirac-corner-coupling, block 3 — terminal)

`r = 1/2` (Q=2/3) needs the `(1,1)` **multiplicity** weighting of the C3 singlet/doublet (F1,
kappa=2); the retained Gaussian measure gives the `(1,2)` **real-dimension** weighting (F3,
kappa=1, r=1; Probe 25/29). Blocks 1 (#2601, fermion determinant) and 2 (#2607, taste = qubit)
ruled out two dynamical routes. The single-factor Connes-Lott is barred (Z3-equivariance +
`Gamma_chi` forces `D=0` on a single `R^3`). The last route was **multi-factor** Connes-Lott:
a spectral triple `A = M_2(C) (+) A_2` with the Yukawa connecting the factors.

## Statement

1. (**isotype weights**) On the generation space `C^3`, the C3 isotypes are singlet (real-dim 1)
   and doublet (real-dim 2): weighting `(1,2)`. The Yukawa `M = aI + bC + b-bar C^2` splits as
   `||aI||^2 = 3a^2` (singlet, 1 real param) and `||bC + b-bar C^2||^2 = 6|b|^2` (doublet, 2 real
   params).
2. (**flavor-blind tensor**) For any flavor-blind factor `V = C^n` (trivial C3 on `V`), the
   enlarged space has isotype dims `(n, 2n) = n·(1,2)` — the ratio `1:2` is **preserved**
   (verified `n = 2, 3, 4`).
3. (**flavor-blind direct sum**) Chirality `H_L (+) H_R` gives `(2,4)`; the KO/real-structure
   (particle/antiparticle) doubling gives `(2,4)` — both preserve `1:2`.
4. (**the (1,1)-maker is flavor structure**) The operator `W = P_+ + (1/2) P_doublet` that turns
   `(1,2)` into the per-block `(1,1)` balance is C3-**equivariant** (commutes with `C`) but
   **isotype-distinguishing** (not a scalar) — i.e. it is flavor structure, an admission, not a
   separate clean factor.
5. (**two balance points**) F3 (per-real-dimension equipartition): `3a^2 = 6|b|^2/2 = 3|b|^2`
   gives `r = 1`. F1 (per-block): `3a^2 = 6|b|^2` gives `r = 1/2`. The gap between them is exactly
   the relative factor 2 in `W`.

All nine checks pass exactly (sympy).

The reason is Schur: tensoring or direct-summing with a C3-**trivial** space scales every
isotype multiplicity by the same integer, so it can never change the singlet:doublet **ratio**.
Only a C3-equivariant operator that acts by **different scalars** on the two isotypes (flavor
structure) can — and that is precisely the admitted `(1,1)` multiplicity principle, not a factor.

## Campaign convergence — the dynamical class is exhausted

| route | result | status |
|---|---|---|
| free Gaussian measure on Herm_circ(3) | (1,2)/F3 -> kappa=1, r=1 | ruled out (Probe 25) |
| corner fermion determinant `det(M)` | shape-stationary at r=1, r=4 | ruled out (block 1, #2601) |
| Z3 scalar potential `V(Tr K)` | V_eff min != physical point | ruled out (framework Section 5) |
| taste-breaking normalization | tastes span M_2(C), no multiplicity | ruled out (block 2, #2607) |
| **multi-factor Connes-Lott** | flavor-blind preserves (1,2); (1,1) purchased | **ruled out (this block)** |

**Verdict.** Every dynamical route the framework's clean single-qubit structure supplies
delivers the `(1,2)` real-dimension weighting `kappa = 1` (r = 1, Q = 1). The empirical
charged-lepton value `kappa = 2` (r = 1/2, Q = 2/3) is the `(1,1)` **multiplicity** weighting,
which no clean route produces — it is the **irreducible admission** (= BAE, the
`|b|^2/a^2 = 1/2` carrier input). This is the precise, now-exhaustive content of Probe 29's
partial falsification: the framework **predicts** `kappa = 1` for a clean color-singlet
C3-triplet fermion, in tension with the empirical leptons, and the only escape is to admit the
multiplicity-counting principle (equivalently, a flavor-dependent isotype reweighting), which
is not derivable from the existing axioms.

This is a genuinely falsifiable statement and a clean stopping point: the Koide r=1/2 is not a
theorem of `{Quantum, Locality, Record}` plus the staggered-Dirac realization; it is the one
irreducible flavor admission on the charged-lepton lane.

## NO-GO DISCIPLINE GATE (N1-N8)

| # | Check | Result |
|---|---|---|
| N1 | >= 5 attack routes named | 5: free measure [Probe 25]; fermion determinant [block 1]; Z3 scalar potential [framework Section 5]; taste-breaking [block 2]; **multi-factor [this block]**. All 5 RULED OUT -> the dynamical class is exhausted; the residual is the admitted multiplicity principle itself (not a route). |
| N2 | wall independence | The multi-factor wall (Schur ratio-invariance) is independent of the determinant, measure, and taste walls (it is a representation-multiplicity fact). |
| N3 | hidden-wall scan | Sole admission explicit: CONDITIONAL on the staggered-Dirac gate. The isotype/Schur facts are reproven from the C3 permutation primitive; Connes-Lott is comparator only. |
| N4 | residual matching | Matches Probe 25/29: the (1,1) multiplicity is "not derivable from cited dynamics" — here shown that no flavor-blind factor supplies it, and the flavor-dependent maker IS the admission. |
| N5 | rhetoric resolution | Scoped to "flavor-blind factors preserve (1,2); (1,1) needs flavor structure"; not "no mathematics whatsoever gives r=1/2" (the admission route is named, not denied). |
| N6 | partial-closure path | The "purchase vs derive" distinction IS the honest resolution: r=1/2 is reachable by admission, foreclosed as a clean derivation. |
| N7 | steelman | "A specific minimal 2-factor triple might force the flavor-dependent W by an order-one / first-order axiom." Residual: such a triple would still be ADDING `A_2` (a structural admission beyond `{Quantum, Locality, Record}`); even if it forces W internally, the factor itself is the admission. Folded into the gate/no-new-axioms discipline, not claimed impossible. |
| N8 | cross-cycle echo | Consistent with the 30-probe (1,2) convergence and blocks 1-2; the same real-dimension residue recurs, now traced to Schur ratio-invariance — the deepest of the four walls. |

**Verdict:** narrow route-pruning (route #3) that closes the dynamical class; the campaign's
terminal obstruction. Residual: the admitted multiplicity principle (= BAE), by construction
not a derivation.

## What this claims / does NOT claim

- Claims: flavor-blind multi-factor extensions preserve the `(1,2)` weighting (exact, Schur);
  the `(1,1)`/r=1/2 weighting requires a flavor-dependent admission; hence the dynamical class
  is exhausted and r=1/2 is the irreducible admission.
- Does **not** claim NCG/Connes-Lott is wrong, nor that no 2-factor model fits the leptons —
  only that any such model **purchases** r=1/2 by adding `A_2` (a structural admission), not
  derives it from `{Quantum, Locality, Record}`.
- Does **not** claim Q=2/3 is empirically wrong.
- Conditional on the open staggered-Dirac realization gate.

## Trace gate

```yaml
trace_class: negative_route_pruning
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "dynamical class exhausted; r=1/2 is the irreducible flavor admission. Open: whether the staggered-Dirac gate, once resolved, fixes the multiplicity principle by an order-one/first-order axiom (would still be a structural addition)."
```

## Forbidden imports

- Literature (Connes-Lott NCG, KO-dimension, real structure J) is comparator only; the isotype
  decomposition and Schur ratio-invariance are reproven from the C3 permutation primitive. No
  PDG values as derivation inputs.

## Cross-references

- `CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`
  (block 1, #2601).
- `STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`
  (block 2, #2607).
- `KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`
  (#2591) — why r=1/2 must be dynamical.
- `KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md` — the F1/F3 weighting
  and the isotype Frobenius split.
