# U-integration on the Corner Transfer Is Reading-Blind and Dictionary-Blind

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source-side bounded theorem note only. This note records a finite
witness-class theorem plus a structural quantification over matter-blind
weights on that supplied background class; it is not an audit verdict.
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry, queue, ledger, or publication-status surfaces.
**Primary runner:** `scripts/frontier_u_integration_reading_dictionary_blind_2026_06_12.py`

## Boundary

This note proves Q1-Q4 below on the stated finite witness class and states the
structural quantification over any matter-blind weight on that class: any
nonnegative functional `w[U]` of the supplied gauge background alone.

It does not claim continuum gauge dynamics, full gauge dynamics, a full
interacting matter-gauge construction, or any universal nonperturbative gauge
measure theorem. It does not enact any reclassification. It does not select a
species reading, does not select a cell, does not fix `r`, and does not close
the dictionary route.

FIREWALL / WALLS-MOVE: the U-integrated surface, for any matter-blind measure on
this supplied witness class, does not determine the dictionary; future surfaces
and non-matter-blind couplings remain open. This is next-path language, not a
closure claim.

## The supplied surface

The fixed-background corner-transfer family is the supplied per-background,
per-channel kernel family `t_k[U](delta)` with masses
`lambda_k(delta) = a + 2B cos(delta + 2 pi k/3)` on the positivity domain. The
finite runner uses the supplied circulant class and the witness class of `U(1)`
phase backgrounds on the `1+1d`, `L_s = 2` spatial links in temporal gauge,
with Haar quadrature over the residual phase.

The structural measure class on this supplied background family is:

`M_mb = { w[U] >= 0 : w is a functional of the background U alone }`.

A measure in `M_mb` is independent of both the `hw` reading and the Berezin
dictionary normalization. The physical Wilson-form gauge action `S_G` is not
consumed here; the theorem quantifies over the matter-blind measure class
instead of selecting a physical gauge action.

## Theorem

> On the fixed-background corner-transfer witness family described above, for
> every matter-blind measure `w[U] >= 0` on that family, U-integration preserves the same
> reading-blind and dictionary-blind status already present pointwise on the
> supplied finite surface.

**Q1 -- Factorization (runner checks A1-A4).** Any matter-blind measure is
independent of both the `hw` reading and the Berezin dictionary by construction:
the reading lives on the matter/generation factor and the dictionary in the
matter measure normalization, while `w[U]` is a gauge-sector functional. The
integrand factorizes as `w[U]` times the matter trace datum. This is a
structural statement, and the runner verifies it on the witness class where
both factors are computed explicitly.

**Q2 -- Reading-blind, species consequence (runner checks A5-A9).** The
registrable matter trace data are equal for the two `hw` readings pointwise in
`U`. The trace-reality strengthening is the reason: traces of positive transfer
operators are real, and the conjugated-background relation then gives same-`U`
equality. The runner reproves the pointwise fact on real and complex witness
backgrounds and then performs Haar quadrature with three matter-blind weights:
uniform, plaquette-like `1 + cos(theta)/2`, and a seeded positive smooth weight.
For each weight and each domain point, the two readings have equal integrated
registrable data. The `hw` choice remains unregistrable at the U-integrated
level on this supplied surface.

**Q3 -- Dictionary-blind, occupancy consequence (runner checks A10-A13).** The
dictionary/kernel normalization acts on the matter factor only: rescaling the
doublet Berezin block by `rho` multiplies the per-background matter datum by
the same `rho^kappa` at every `U`, with exponent `kappa` independent of the
background. Therefore the rescale commutes with U-integration for every
matter-blind measure on the supplied witness class:
`int dU w[U] rho^kappa f[U] = rho^kappa int dU w[U] f[U]`.

The integrated objects per dictionary differ by exactly the fixed-background
factor structure; the gauge integral supplies no new determination of the
dictionary. The tested U-integrated surface does not decide the occupancy atom.
This strengthens the registered-pattern classification of the dial while
keeping the route open: the U-integrated surface, for any matter-blind measure
on this supplied witness class, does not determine the dictionary; future surfaces and
non-matter-blind couplings remain open. The occupancy binary stays open.

**Q4 -- Consequences (runner checks A14-A18).**

(a) For the species bridge, the supplied vacuity chain
`slot model -> free dynamics -> fixed background -> U-integrated matter-blind
witness class` is complete on the levels represented here. The non-naming
content of the bridge is unregistrable throughout that supplied chain. The
reclassification question is audit-lane-owned and is not enacted here.

(b) For the occupancy lane, the U-integrated route returns underdetermination.
The remaining derivation legs are the outcome-independence and K-reality
routes, both named here and not discharged here.

## Consequence

For the species reading, U-integration over any matter-blind gauge measure on
this supplied witness class does not turn the `hw` reading into a registrable
datum. For the dictionary reading, U-integration over any matter-blind gauge
measure on this supplied witness class does not turn the Berezin
normalization into a selected occupancy atom. The surface remains useful
because it moves the walls: it shows exactly which integrated route fails and
which hypotheses would have to change next.

## What this note does NOT claim

- It does not claim full continuum gauge dynamics.
- It does not claim a physical Wilson-action gauge measure is derived or used.
- It does not claim non-matter-blind matter-gauge couplings are blind.
- It does not select `hw=1`, `hw=2`, any species reading, or any cell.
- It does not fix `r` or derive a charged-lepton value.
- It does not enact or predict a reclassification; that is audit-lane-owned.
- It does not decide the occupancy atom.
- It does not close the dictionary route.
- It does not remove the outcome-independence or K-reality derivation legs.
- The occupancy binary stays open.
- No new axiom, primitive, admission, probability rule, normalization rule, or
  audit verdict is added.

## Dependencies

- [`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)
- [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)

Context, backticked and not load-bearing because the relevant facts are
reproven in the runner:

- `FIXED_BACKGROUND_CORNER_TRANSFER_NOTE_IN_REVIEW.md`
- `HW_DYNAMICS_CORNER_TRANSFER_NOTE_IN_REVIEW.md`
- `TRACE_CORRESPONDENCE_CORNER_TRANSFER_NOTE_IN_REVIEW.md`
- `FREE_CORNER_TRANSFER_NOTE_IN_REVIEW.md`
- `S_G`

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status
authority.
