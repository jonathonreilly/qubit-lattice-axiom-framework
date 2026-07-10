# Season Review Brief -- PRs #5061-#5091, One Ordered Pass

**Date:** 2026-07-09
**Type:** reviewer handoff (process surface; no science claims of its own)
**Status authority:** none -- this brief organizes review, it does not
set or predict any status.

Thirty-one stacked PRs from the 2026-07-08/09 season, ten campaigns.
This brief gives one recommended review order, the load-bearing spine,
and per-campaign checks. Per-PR verification commands live in each
campaign's HANDOFF file under `.claude/science/physics-loops/`.

## The season in one paragraph

The gravity chain is now derived from the four axioms up to one shared
convention and measured constants: energy makes records (activity
necessity exhibited exactly), crowding slows record formation (an
axiom corollary, sign universal in the constraint reading), slow
formation is slow time (one constant in the weak field), and slow time
is universal fall (lapse-channel kernel exactly massless, protected by
energy conservation). The extremes run end to end in a coupled
comparator (collapse, frozen stars, bridging mergers, an exact area
analog, memory imprints, saturation endgame). The one supplied
threshold was shown to have a forced shape (redundancy onset), and
one-dimensional worlds were shown unable to host permanence-grade
records at all -- the bar's location is a d=3 measurement waiting to
be made.

## The load-bearing spine (review these hardest)

1. **#5076** -- the saturation corollary (full sites form no records),
   the availability census, and the constraint-reading sign. Everything
   from #5077 onward leans on this PR. The constraint reading of
   Admissibility is a DECLARED reading (owner deliberately left it
   unruled); check that every downstream use says so.
2. **#5073/#5074** -- the lapse-channel kernel (exactly massless at
   every mass; the continuity protection at 5e-12) and the abelian
   obstruction. This pair is the derivation-first resolution of the
   season's one axiom trigger; the owner ruling is recorded in the
   energy-sector pack.
3. **#5082** -- kappa(theta) conventions (excess distinguishability
   above the interacting-GS baseline). The registration-bar campaign
   (#5089-#5091) reuses these conventions; a defect here propagates.
4. **#5083** -- the coupled-toy engine, including the 2026-07-09
   Poisson deposition fix folded into its branch. #5084-#5086 all run
   on it.

## Recommended order, by campaign

| Wave | PRs | Campaign | One-line claim | First check |
|---|---|---|---|---|
| 1 | #5061-#5065 | matter-mass-wep | framework yields mass; scaling-window WEP, derived exponents | m=0 control width-splits; residual/sigma_p^2 collapse |
| 1 | #5066-#5067 | gauged-mass-equivalence | static-channel separation; ~5% cross-species metric universality | separation gates |
| 2 | #5068-#5069 | mass-identity-and-source | conserved-density kernel exactly {Q_a,Q_b,H}; source = gamma x energy | kernel exactness runner |
| 2 | #5070-#5072 | wilson-identity-source-dynamics | Poisson unique shift-symmetric member; compact surface forces background subtraction | forced-subtraction leg |
| 3 | #5073-#5075 | energy-sector-field-derivation | lapse kernel massless + protected; Route B obstruction; owner surface | 5e-12 protection residual; the ruling record |
| 4 | #5076-#5078 | record-rate-gravity | clock sector derived: saturation corollary, sign, one weak-field constant | the corollary's axiom-text derivation |
| 4 | #5079-#5081 | energy-to-records | activity-energy bound; wake self-regulates; season synthesis | wake CHECK-07/08 sub-geometric gates |
| 5 | #5082, #5085, #5087 | record-deposition-rate | kappa measured; mobility forces sparsity (4 decades); constraint map | baseline subtraction; the separation gate |
| 5 | #5083, #5084, #5086 | collapse-merger-comparator | engine valid; frozen star; merger by bridging, exact area analog | Poisson fix changelog; husk identity convention |
| 6 | #5089-#5091 | registration-bar | bar shape forced; d=1 cannot host R>=2; necessity exact | the Markov-blanket argument; probe caches |

Waves 1-3 are the mass/field half; waves 4-6 are the gravity half.
Within a wave, order as listed (stacked bases). Every runner has a
cache; `diff <(python3 <runner>) <cache>` is the uniform check.

## Standing items the season did NOT decide (owner's list, unchanged)

- Constraint reading of Admissibility: declared, deliberately unruled.
- Lawful-rate-law existence: named premise where used, unruled.
- The record-reading convention (quantum-Darwinism): the ONE shared
  convention carrying both the dynamics-form theorem and the gravity
  chain; unchanged in status.

## Named successors (banked, not commissioned)

d=3 registration comparator (Z^3 is the target -- owner reminder
2026-07-09); June conformal-class input audits (two unaudited inputs;
audit-readiness verification in progress); axiom-reconciliation blocks
(2,278 pre-reset rows).
