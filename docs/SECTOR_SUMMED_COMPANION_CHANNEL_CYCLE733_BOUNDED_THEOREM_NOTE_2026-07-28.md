# The sector-summed companion channel — the full-sector isometry, constructed — Cycle 733

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle733_sector_summed_companion_channel_2026_07_28.py`](../scripts/frontier_cycle733_sector_summed_companion_channel_2026_07_28.py)
- [`frontier_cycle733_sector_sum_independent_check_2026_07_28.py`](../scripts/frontier_cycle733_sector_sum_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 727 made the reference-to-companion relation exact per parity
sector and froze the obstruction: the per-sector channel is not a
full-sector isometry, and the note named "a sector-summed or direct-sum
companion channel" as the only route — new construction, not
nomenclature. This cycle builds it on the landed fixtures:

- **the direct-sum channel `V = V₊ ⊕ V₋`** over the declared sector
  family (even and odd parity sectors, each of dimension `2^47`; summed
  domain `2^48`), with one supplied convention — the printed outer
  direct-sum ordering (even before odd; within-sector coordinates
  unchanged from the landed modules);
- **full-sector isometry achieved**: `V†V − I` is exactly zero on the
  summed domain, verified structurally over the projector algebra (the
  Gram block table: identity on both diagonal blocks, exact zero on
  both off-diagonal blocks) — `full_sector_isometry_achieved: true`,
  `frozen_obstruction: null`;
- **intertwining block structure, exhausted at generator level**: over
  all 312 landed generators, every one of the 624 intertwining
  off-diagonal blocks and 1,248 representation off-diagonal blocks is
  exactly zero — `(VA − BV)_{t,s} = δ_{t,s}(V_s A_s − B_s V_s)`, and
  the per-sector factors vanish by the landed Cycle-727 exactness,
  which reruns unchanged as the anchor;
- **cross-sector diagnostics**: 936 superposed two-sector intertwining
  tests and six coherence routes, zero failures, norm preservation
  exact (each diagnostic has one vector in each orthogonal sector, so
  the exhaustive per-sector and block results extend by linearity);
- **no new supply**: an AST audit finds zero fitted constants and zero
  new physics conventions beyond the printed sector ordering;
  everything else is the landed modules' own declared data.

## Supplied / derived / open

### Supplied

- the outer direct-sum ordering convention (declared, printed);
- everything the landed Cycle-720 geometry/gauge modules and the
  Cycle-727 exactness surface themselves declare.

### Derived

- the direct-sum channel and its exact full-domain isometry;
- the delta-block intertwining identity with all off-diagonal blocks
  exactly zero at generator level, extended to superposed states by
  linearity with exhaustive diagnostics;
- the unchanged per-sector anchors.

### Open

- the second Cycle-727 frozen obstruction (no marker-to-coframe
  correspondence) is untouched — it was a separate census result and
  no correspondence is claimed here;
- the global tiled channel tensor, bounded physical common-E
  preparation, and every inherited open item at its original scope;
- occurrence, time, Record, Born, and source content remain exactly as
  inherited.

## Negative-claim discipline

No negative claim ships. Cycle 727's first frozen obstruction (the
absence of a full-sector isometry among the landed per-sector channels)
is discharged by construction along exactly the route its own note
named; the obstruction record stands as history, not as a live wall.

## Verdict

The route Cycle 727 named as "the only route to a full-sector isometry"
is now a construction: one supplied ordering convention, then an exact
direct-sum isometry whose off-diagonal blocks vanish identically at
generator level. The companion-channel program's matter-lane bridge no
longer has a sector gap. Independent audit still required.
