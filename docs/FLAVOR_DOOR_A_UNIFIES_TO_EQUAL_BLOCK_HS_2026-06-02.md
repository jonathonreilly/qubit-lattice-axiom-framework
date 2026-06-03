# Flavor — the "geometry-fixed action" axis (Door A) is the same wall as the measure axis: every action-level condition reaching r=1/2 reduces to the native equal-block Hilbert-Schmidt weight 3a²=6|b|²

**Date:** 2026-06-02
**Claim type:** a unification / localization result (no action fixes the value; the residual is one named native object). Not closure, not an import adoption.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade.
**Runner:** `scripts/flavor_door_a_unifies_to_equal_block_hs_2026_06_02.py` (SCORECARD 4/4).

## Question
Does any framework-internal lattice **action** geometrically fix the charged-lepton ratio
`r = |b|²/a²` at `r=1/2` (`|b|/a = 1/√2`), rather than leaving the on-site mass a free Yukawa? Four
action-level routes were examined: a Wilson term, the hw=1 induced diagonal, the Cl(3) grade /
heat-kernel (spectral-action) form, and a critical/self-dual fixed point.

## Result — no action fixes r=1/2; and every route that *reaches* it collapses to one object
No framework-internal action geometrically fixes `a:|b|`. In each route the value either stays free
or lands away from `1/2`:

- **Wilson term** (an admitted import): the bare mass `m₀` remains a free dial; the induced hopping
  depends on an unforced Schur reference energy — `r` is a free function. Import-dependent *and*
  non-fixing.
- **hw=1 projection** (native): forces the democratic endpoint `r=0` (companion note) — geometry
  gives zero generation hopping, not `r=1/2`.
- **Cl(3) grade / heat-kernel / spectral action** (native): the Clifford norms fix only the basis
  scale, not the coefficients; the spectral-action critical point sits at `|b|/a ≈ 1.0` (not `0.707`),
  and the RG flow *repels* from `1/2`.
- **Self-dual / critical** (various): `r=1/2` is hit only by a tunable member of a one-parameter
  family; other natural members give `r=0`, `r≈0.134`, `r=1`.

**The unification.** Every route that lands *exactly* on `r=1/2` reduces algebraically to the single
condition

> **3a² = 6|b|²**  ⇔  `‖aI‖²_F = ‖bC + b̄C²‖²_F`  ⇔  `r = 1/2`  ⇔  `Q = 2/3`,

i.e. **equal total Hilbert–Schmidt norm of the mass block and the hopping block** — the already-named
block-count weighting `AC_φλ`. The multiplicities `1:2` here (mass `Tr(I)/3 = 1` on the trivial
grade; hopping = two shift generators `C, C²` giving `‖C‖²_F + ‖C²‖²_F = 3+3 = 6` on the doublet
grade) are **forced geometric trace-counts**, not free parameters. So **Door A (action axis) is the
same wall as the previously-mapped measure axis**, reached from a new direction.

The faithful A1 metric — dimension / trace / Plancherel weighting (equal HS power per *coefficient*,
not per *block*) — gives `3a² = 3|b|²` ⇒ `r = 1` ⇒ `Q = 1`. So the single residual is one binary
**granularity** choice: equal weight per real-irreducible **block** (`r=1/2`) vs per **dimension/
coefficient** (`r=1`). Both are realizable; nothing in the actions examined forces one.

## Two strengthenings this records
1. **The gap is native, not Wilson-dependent.** The only mechanisms that even *reach* `r=1/2` are
   native (Cl(3) grade-norm equipartition); the Wilson-import route is strictly worse (import-dependent
   and non-fixing). The open problem does **not** lean on the admitted Wilson action.
2. **The gap is one precise object.** The whole value question is now `3a²=6|b|²` (equal-block HS
   weight) vs the dimension default — a single, sharply-stated, coordinate-free condition rather than a
   diffuse "missing dynamics."

## The next paths this opens (not closing)
- **Derive the granularity, don't adopt it:** attempt to derive `3a²=6|b|²` (equal HS norm of mass
  vs hopping block) from the A1 qubit Hilbert–Schmidt metric + A2 locality alone, as a *lemma* rather
  than a prior. If it cannot be derived, the precise statement of where `r=1/2` escapes is "equal-block
  HS weight is independent of the A1+A2 metric."
- **Pin the native action form:** the candidate native heat-kernel / Casimir action's Seeley–DeWitt
  `a₂` coefficient fixes a mass:kinetic weighting; whether a *unique* native form forces
  `‖mass‖ = ‖hop‖` (vs leaving cutoff-shape freedom) is the single most decisive open computation on
  this axis, and it is entangled with the open action-form question.

## Provenance (verified 2026-06-02)
- HS block norms `3a²` and `6|b|²`; `3a²=6|b|² ⇔ r=1/2 ⇔ Q=2/3`; dimension reading ⇒ `r=1`; the
  exact line `Q=1/3+(2/3)r`: verified directly (runner 4/4). From the four-lane Door-A analysis
  (workflow `wf_c8faf07e`).
- This note sets no audit status; it localizes the value gap to one named native object and records
  that the action axis coincides with the measure axis.
