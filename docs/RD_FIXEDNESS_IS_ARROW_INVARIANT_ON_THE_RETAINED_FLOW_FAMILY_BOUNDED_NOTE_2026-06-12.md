# R-D Fixedness Is Arrow-Invariant on the Retained Flow Family

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome, does not adopt any
premise, and does not edit any registry or audit data file.
**Primary runner:** `scripts/frontier_rd_fixedness_arrow_invariant_2026_06_12.py`

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or premise. R-D remains a proposed premise, not
an adopted rule.

## Boundary

This note proves F1-F4 only on the retained two-map family already supplied in
the 2026-06-02 flow notes:

- the records/Luders sharpening map `phi(r) = 2 r^2`;
- the reverse/thermalizing map `g(r) = sqrt(r/2)`.

It does not adopt R-D, does not derive the R-D bridge premise, does not select
an occupancy cell, does not fix `r`, does not resolve the coarse-graining
prong, and does not claim this two-map family exhausts admissible record
dynamics. R-D remains a proposed premise; `r = 1/2` is never forced by this
note; the occupancy binary stays open.

This note does not select an occupancy cell.

## The Retained Family

The separatrix note supplies the records/Luders map as exactly `r -> 2r^2`
and states its own boundary: it "does not derive that this map is the physical
emergent charged-lepton records flow."

The thermalizing-arrow note supplies the reverse map `g(r) = sqrt(r/2)` and
states its own boundary: it "does not derive that charged-lepton `r`
physically evolves by this map."

This note consumes those maps only as the named retained family. It does not
choose which map is the physical arrow and does not identify charged-lepton
re-registration with either map.

## Theorem

**F1 - inverse pair [check 01-02].** On `r >= 0`,
`g(phi(r)) = r` and `phi(g(r)) = r` exactly. Thus the two supplied maps are
inverse orientations of the same one-dimensional flow family on the retained
coordinate.

**F2 - fixedness is arrow-invariant [check 03-07].** The finite fixed-point
sets agree:

```text
Fix(phi) = Fix(g) = {0, 1/2}.
```

The projective point at infinity is common as well: under the same
conjugation `s = 1/r`, both maps fix `s = 0`. This is the concrete instance
of the general lemma `Fix(f) = Fix(f^-1)` for an invertible map on its
domain.

**F3 - stability is arrow-dependent [check 08-10].** The multiplier at the
shared finite interior fixed point changes with orientation:

```text
phi'(1/2) = 2 > 1
g'(1/2) = 1/2 < 1
phi'(1/2) g'(1/2) = 1
```

So the landed instability and stability statements are not contradictory.
They are the two orientations of one inverse-pair structure.

**F4 - R-D selection consumes fixedness, not stability [check 11-15].** If
the proposed R-D selection mechanism is read as "durably registered value =
flow-fixed point", then within this retained family it consumes only F2, not
F3. With the registered side conditions `delta != 0` and the unsigned branch,
the extended stationary set `{0, 1/2, infinity}` loses `0` by the degenerate
`B -> 0` spectrum `[a, a, a]` and loses `infinity` by the unsigned positive
trace channel. The remaining admissible set is `{1/2}`. The same set
arithmetic holds for `phi` and for `g`, because the fixed-point set is the
same.

## Consequence

For the R-D route only, the arrow half of the named "which coarse-graining +
which arrow" admission does not bear on the selection: the arrow changes
stability, but the proposed R-D mechanism reads fixedness. What remains open
is the coarse-graining prong, namely the 2-sector partition / custody selector
(i), and the R-D bridge premise itself, namely that re-registration composes
by a member of this retained family. Both are named here; neither is resolved
here.

## Does NOT

- Does NOT adopt R-D or the R-D bridge premise.
- Does NOT derive that charged-lepton re-registration composes by this family.
- Does NOT select an occupancy cell; the occupancy binary stays open.
- Does NOT force `r = 1/2` as a physical value.
- Does NOT resolve the 2-sector coarse-graining prong.
- Does NOT claim that stability is arrow-invariant.
- Does NOT claim this family exhausts admissible record dynamics.

## Dependencies

- [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
- [`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md)

## Context

`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`
and
`KOIDE_OCCUPANCY_DURABILITY_PREMISE_EQUIVALENCE_ON_REGISTERED_SURFACE_BOUNDED_THEOREM_NOTE_2026-06-11.md`
are in review; the side-condition exclusions are reproven in the runner.
`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md` is the
custody note and the home of the coarse-graining prong.
