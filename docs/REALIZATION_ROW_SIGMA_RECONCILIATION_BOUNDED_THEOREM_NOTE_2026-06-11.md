# The Realization Row Reconciled: One Sigma Law, One Consumed Slope, No Dial

**Date:** 2026-06-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem (the walk family's complete exact solution;
the OS0-indifference of the realization choice under the landed W-IR
premise; a sharpening-correction of one landed block05 statement)
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/realization_row_sigma_reconciliation_2026_06_11.py`](../scripts/realization_row_sigma_reconciliation_2026_06_11.py)
(SCORECARD: PASS=12, FAIL=0; cached:
[`logs/runner-cache/realization_row_sigma_reconciliation_2026_06_11.txt`](../logs/runner-cache/realization_row_sigma_reconciliation_2026_06_11.txt))

---

## What this answers

After block05, the kinetic-isotropy chain carried a named realization row:
two exhibited candidates for the realized matter tick — the factorized
per-axis class (blocks 02–04) and the eta-twisted walk family (block05) —
with the candidates' kinetic constants (1 per axis-factor vs
{1/6, 1/(2 sqrt 3)}) left as "reconciliation work". The landed B-W
reduction independently sharpened what the OS0 identification consumes to
one premise:

> **(W-IR)** "at the cone point, the realized tick's quasi-energy band and
> the supplied RP transfer's reconstructed dispersion agree to first order
> in momentum" — and (its T2) the extraction consumes **only** that slope.

This note computes the reconciliation exactly. The instrument is a new
exact result about the family itself.

## The sigma law (runner Part A; exact)

The walk family's FULL three-variable characteristic polynomial factors
over the whole Brillouin zone (rational identity in unimodular symbols);
each block's band equation collapses, branch-free, to a single-cosine law:

```text
  cos Phi = Re( e^{i psi} sigma(k) ) / 3,        X = lambda^2 = h e^{i Phi},
  sigma(k) = e^{i k1} + e^{i k2} + e^{i k3},     e^{i psi} = sqrt(beta/alpha),
```

with `h = sqrt(alpha beta)` the block's quasi-energy offset. **Momentum
enters only through the cubic adjacency symbol sigma.** The family is
completely solved.

## The moduli are frame content (runner Part B; exact)

`e^{i psi} sigma(k) = sigma(k + psi (1,1,1))` exactly: the psi-modulus is a
DIAGONAL MOMENTUM TRANSLATION, and h is a quasi-energy offset — per block,
the six landed phases reduce to two frame moduli each plus the inter-block
relative offset. Consequently the psi-band is the psi=0 band translated in
momentum, pointwise (verified at 200 random points to 1e-12), so **every
translation-invariant kinetic functional — BZ-suprema of gradients, band
widths, curvature ranges — is moduli-RIGID exactly.**

**Sharpening-correction of a landed statement:** the landed block05 note
says "off-axis FRONT SPEEDS vary continuously
with the moduli (computed: 0.19-0.24 across samples)". The computation
behind that sentence (fixed-line band-tracked
maxima) is reproduced here and its variation is real — but it is a SLICE
artifact: the scan line is not translation-aligned, so a translated band
shows a different maximum along the same fixed line while the full-BZ
front speed cannot move. With the translation identity in hand, the
family's translation-invariant kinetic geometry is rigid; the no-dial
classification holds in its strongest form. **Supersession scope:** the
landed block05 text states the front-speed-continuity reading in its
headline consequence paragraph, D4, the conditional-set row, the
does-not-claim list, and N5/N7 (and "the moduli are NOT pure momentum
translations" in D4, which this note refines: not pure translations OF THE
UNION — the per-block moduli are exactly translations plus offsets, and the
inter-block relative offset is the genuinely non-translational remainder,
moving only inter-block crossing geometry). The landed block05 file is left
unmodified; every one of those statements is superseded on this point by
the exact translation identity here. This is the residual block05's N7
steelman names, now computed.

## Strata, drift, diagonal — from the law (runner Part C; exact)

Two-line re-derivations from the cosine law: theta-slope at k = 0 is
exactly +-1/6 per axis (any psi != 0) and +-1/(2 sqrt 3) at psi = 0; the
gapless locus is exactly the BZ diagonal (`|sigma|^2 = 3 +
2 sum cos(k_i - k_j) = 9` iff all momenta coincide); on the diagonal the
law gives `Phi = +-(t + psi)`: **exactly linear, slope 1/2 in the cell
diagonal parameter, for all moduli** — the same quantized value as the
landed 1D dichotomy's saturating cell.

## The reconciliation (runner Parts D–E; exact)

- **(T1, drift equality)** The factorized symmetric cycle obeys
  `(S1 S2 S3)^2 = -(z1 z2 z3)^{-1} I` exactly, so its per-tick drift is
  `+-(1,1,1)/6` cells/tick — IDENTICAL to the family's rigid generic
  drift. The two exhibited candidates share their symmetric-point
  transport exactly.
- **(E1, OS0-indifference)** The per-axis candidate's transport-direction
  slope is 1/2 in cell units (the landed dichotomy value); the family's
  transport-direction (diagonal) slope is 1/2 in the cell diagonal
  parameter (exact, above). **Both candidates feed the SAME quantized
  first-order datum into the landed W-IR premise; the OS0-consumed content
  is identical; the realization choice is OS0-IRRELEVANT at the consumed
  level.** The kinetic-isotropy content of the chain does not depend on
  which exhibited candidate the matter sector occupies.
- **(E2, what still differs)** Transverse first-order flatness vs per-axis
  structure; off-locus curvature (present in the family, absent in the
  cycle's bands); the inter-block relative offset; single-tick vs
  composite mass realization. All exhibited, all OUTSIDE the consumed
  surface: shape/dynamics content, not W-IR content.

## The sigma kinship and the honest cone row (runner Part F)

The landed staggered Hamiltonian's dispersion is also sigma-driven:
`E(k) = +-sqrt((3 - Re sigma)/2)` on the 8-cell (computed; consistent with
the landed
[STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md](STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md),
which certifies the kernel's isotropic point cones on the same surface). One structure
function, two readings: the H-law and the tick-native cosine law. But the
H-cone at sigma -> 3 is isotropic (`E ~ |k|/2`) while the family's gapless
set is the diagonal LINE with 1D-like crossings (transverse-flat at first
order): **the isotropic 3D cone is realized by NEITHER candidate at this
density.** The matter-cone row (larger-cell content) is unchanged — stated,
not implied away.

## The conditional set after this cycle

| entry | status |
|---|---|
| the realization row ("which exhibited candidate; reconcile 1/6 vs 1") | RECONCILED: identical consumed W-IR slope (1/2, cell units, transport direction); the choice is OS0-irrelevant at the consumed level; the residual choice content is dynamics/shape (named, E2) |
| block05's "off-axis front speeds are continuous moduli content (honest scope)" | superseded: frame content (slice artifact; exact translation identity) |
| the standing readings + the landed W-IR premise + unaudited deps | unchanged (W-IR consumed as the landed text states it; the bare P2 reading was separately retired into two named readings by the landed [TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md), inherited not re-litigated) |
| the isotropic 3D matter cone | unchanged: larger-cell content for BOTH candidates (computed) |
| open 1 (full-family exhaustive closure) | unchanged (named, documented infeasible) |

## What this note does NOT claim

- **No registry action, no audit prediction.** The chain's grade calls
  belong to the audit lane.
- **Not a selection of the realized candidate.** The note proves the
  selection doesn't move the OS0-consumed content; selecting (or refusing
  to select) the dynamics/shape content remains realization work.
- **The W-IR premise is consumed, not strengthened**: the agreement of
  both candidates' slopes makes W-IR's input unambiguous; it does not make
  W-IR true. W-IR remains the chain's named bridge premise exactly as the
  landed B-W reduction states it.

## Falsifiers

- A licensed dispersive equivariant cell outside the six-orbit family
  whose transport-direction slope differs from 1/2 (the block05 census
  falsifier surface, inherited).
- A moduli point violating the translation identity (a counterexample to
  a verified rational identity).
- A landed sharpening of W-IR that consumes more than the first-order
  slope (would reopen the candidates' E2-level differences as consumed
  content — the named re-entry point).

## No-Go Discipline Gate

The negative claims: "no front-speed dial (the variation is a slice
artifact)"; "no isotropic cone point in either candidate".

- **N1 alternative routes:** (1) other scan lines/directions — closed by
  the translation identity (any translation-invariant functional is
  rigid); (2) the inter-block relative offset as a dial — it moves
  crossing geometry between blocks, not any per-band kinetic functional
  (named in E2 as shape content); (3) cells outside the family — the
  block05 census surface, inherited as a falsifier.
- **N2 wall independence:** the translation identity (B), the quantized
  diagonal law (C3), and the cycle's central square (D1) are three
  independently computed walls.
- **N3 hidden-wall scan:** "transport direction" is declared (diagonal for
  the family, per-axis for the cycle); the transverse flatness is
  computed, not assumed; the arccos branch is handled on the open interval
  (the touching set itself is measure zero and treated by the diagonal
  law).
- **N4 residual matching:** block05's does-not-claim bullet ("reconciliation
  work for the realization row, not asserted here", echoed in the loop
  pack's trace gate) and the landed B-W note's W-IR premise are the
  residuals consumed, by their landed wording.
- **N5 rhetoric audit:** "OS0-irrelevant" is scoped to "at the consumed
  level" everywhere; "rigid" is scoped to translation-invariant
  functionals; the correction of block05's front-speed sentence names the
  exact computation that produced the original number.
- **N6 partial-closure scan:** no prior note computes the global
  factorization, the cosine law, or the reconciliation.
- **N7 steelman:** "the diagonal slope 1/2 and the per-axis slope 1/2 are
  measured along different directions in different parametrizations — is
  the comparison fair?" Both are the first-order quasi-energy slope along
  the candidate's own transport direction in cell units, which is exactly
  the datum W-IR consumes (the supplied transfer's reconstructed
  dispersion is compared at the same point); the unit bookkeeping is part
  of the runner's E1 and the residual normalization-placement freedom is
  the chain's standing R-P reading, inherited not re-litigated.
- **N8 cross-cycle echo:** the quantization pattern survives its third
  formulation change (1D cells, 3D drifts, now the sigma law); the dial
  has now died at every level where it was sought, including inside the
  discovery family's own moduli.

## Claim scope note

The sigma law, the translation identity, the strata, the diagonal law, and
the cycle's central square are exact (rational identities or two-line
symbolic derivations from them). The OS0-indifference claim is scoped to
the consumed level defined by the landed W-IR premise (first-order
agreement at the comparison point); the candidates' E2-level differences
are exhibited, not adjudicated. The supersession of block05's front-speed
sentence is scoped to translation-invariant functionals; the original
fixed-line computation's numbers are real and reproduced.

## Reproduction

```bash
PYTHONHASHSEED=0 python3 scripts/realization_row_sigma_reconciliation_2026_06_11.py
```

Expected scorecard: `PASS=12 FAIL=0`.

## Dependencies

- [ETA_TWISTED_WALK_FAMILY_RIGID_DRIFT_DISCOVERY_BOUNDED_THEOREM_NOTE_2026-06-10.md](ETA_TWISTED_WALK_FAMILY_RIGID_DRIFT_DISCOVERY_BOUNDED_THEOREM_NOTE_2026-06-10.md) — landed (verbatim); the family, its strata, the census surface; one statement sharpened-corrected here.
- [BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md](BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md) — landed; the W-IR premise and the consumed-slope theorem (T2), consumed as stated.
- [KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md](KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md) — landed; the factorized class and the cycle witnesses.
- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md) — landed; the 1D quantized value 1/2 (cell units).
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) — the eta structure (`unaudited`, conditionality inherited).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
