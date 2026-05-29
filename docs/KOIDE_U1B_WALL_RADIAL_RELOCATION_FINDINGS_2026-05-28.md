# Koide F1 wall — 6-mechanism attack relocates it from angular to radial

**Date:** 2026-05-28
**Claim type:** bounded_obstruction (sharpened + relocated); promotion
routes OPEN. NOT a closure. Imports no axiom/comparator/convention;
promotes no row; sets no retained status. Local-branch working note.
**Scope:** full multi-phase attack on the `U(1)_b` doublet-phase quotient
named in `KOIDE_F1_SELECTION_PANEL_FINDINGS_2026-05-28.md` as the residual
F1-selection wall (`|b|²/a²=1/2` → Q=2/3).
**Runner:** `scripts/koide_u1b_wall_radial_relocation_2026_05_28.py`;
cache `logs/runner-cache/koide_u1b_wall_radial_relocation_2026_05_28.txt`.

## Method
Six mechanism classes attacked in parallel, each pre-briefed with the
already-obstructed routes (Probe-14 retained-U(1) hunt, Berry-bundle
topological triviality, γ-involution `det^{1/dim}` non-derivation) so none
re-tread them; each could run scratch code; any route claiming a clean
measure-acting escape was adversarially refuted. Classes: (1) is θ=arg(b)
physical/gauge, (2) dynamical discrete-time phase averaging, (3)
record/persistence/decoherence primitives, (4) operational MaxEnt past its
residual, (5) measure-theory enumeration, (6) crossed-product / outer
action.

## Result: wall STANDS (0/6), and is RELOCATED
No mechanism produced an import-free, non-circular, measure-acting
derivation of `|b|²/a²=1/2`. But the campaign delivered two structural
advances that change where the wall is.

### Advance 1 — the wall is NOT angular (corrects prior framing)
The circulant `H = aI + bC + b̄C²` has spectrum
`λ_j = a + 2|b|cos(θ + 2πj/3)` (verified). Therefore:

- `Σλ_j = 3a`, `Σλ_j² = 3a² + 6|b|²`, so `Q = 1/3 + (2/3)(|b|²/a²)` is
  **exactly independent of θ = arg(b)** (verified: Q=0.44 for all θ at
  r=0.16). θ is the Brannen phase δ — it deforms the individual
  sqrt-masses but is **orthogonal** to the F1/F3 knob `r = |b|²/a²`.
- Hence "quotient the doublet phase `U(1)_b`" is a **category error**: no
  θ-operation can fix `r`. Marginalizing θ under the flat C₃-invariant
  Gaussian leaves the polar Jacobian `|b|d|b|dθ`, which keeps both real
  dimensions → `r ≈ 2` (verified), never 1/2.
- **Correction to `KOIDE_F1_SELECTION_PANEL_FINDINGS_2026-05-28.md`:** the
  residual wall named there as "the `U(1)_b` angular quotient" is
  mis-located. Phase routes (gauge, dynamical averaging, decoherence,
  operational-MaxEnt-via-θ) are now collectively dead.

### Advance 2 — Probe 14 superseded; the additive U(1) exists
Probe 14 found no retained U(1) supplying the additive shift on the C₃
grading (all inventoried candidates act by conjugation). Mechanism 6
**supplies it**: the crossed-product / Pontryagin-dual **outer** action
`ρ_α: grade-j ↦ e^{iαj}` (canonical on the `M(C) ⋊ Z₃` dual) realizes the
additive θ-shift. But `ρ_α` rotates `arg(b)` and leaves `|b|²/a²`
invariant (verified: r=0.25 for all α) — it is the symmetry of the wrong
direction. The crossed product's canonical dual-Plancherel weight still
counts the doublet as 2 dual modes → F3.

## The wall, correctly located: a RADIAL 2→1 reduction
All six mechanisms collapse to one missing object: a derived rule
reducing the doublet isotype's **real-dimension count from 2 to 1 in the
measure**. A1+A2 supply the Frobenius metric, the C₃-isotype split, and
(now) the additive grading-phase action — but NOT the normalization
choosing

- equate **total** isotype Frobenius norms `3a² = 6|b|²` → r=1/2 (F1), vs
- equate **per-real-dimension** norms `3a²/1 = 6|b|²/2` → r=1 (F3).

Every canonical measure counts the doublet by real dimension 2 → F3 (or a
free ratio). F1 requires the `{ω, ω̄}` pair to count as ONE complex unit —
the `det^{1/dim}` / `(1,1)`-multiplicity primitive, the SAME object
flagged non-derived in `CL3_GAMMA_INVOLUTION_DETERMINANT_NARROW_THEOREM`.

## Highest-value next experiment
The one untested place "pair = 1" might be **forced** rather than
imported: the **modular (Tomita–Takesaki) weight of the trace state on the
Hermitian circulant algebra**, where Hermiticity ties `b̄ = conj(b)` so the
`{ω, ω̄}` modes are not independent. Test whether that modular weight
counts the Hermitian-conjugate doublet as one complex dimension. (Note the
tension with the prior panel's "modular/KMS is blind" finding, which
addressed the abstract center `R⊕C`, not the reality constraint on the
circulant — so this is a genuinely distinct probe.) If it still gives 2,
the `(1,1)` primitive is non-derivable and the phase-route family should be
promoted to `retained_no_go`, with the radial gap as the sole frontier.

## Status
Bounded obstruction, relocated and sharpened; promotion routes OPEN. No
closure. r=1/2 is not derived from A1+A2+retained. The frontier is now the
radial 2→1 real-dimension reduction, not any phase quotient.
