# Color `MR_color` Carrier/Routing Split

**Date:** 2026-06-05
**Claim type:** meta
**Trace class:** upstream support map.
**Status authority:** independent audit lane only. This source note does not
apply audit verdicts, edit audit data, or assert package promotion.
**Primary runner:**
[`scripts/frontier_color_mr_carrier_routing_split_2026_06_05.py`](../scripts/frontier_color_mr_carrier_routing_split_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_color_mr_carrier_routing_split_2026_06_05.txt`](../logs/runner-cache/frontier_color_mr_carrier_routing_split_2026_06_05.txt).

**Local support inputs:**

- [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md)
- [`GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md`](GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md)
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- [`LHCM_MATTER_ASSIGNMENT_SU3_BLOCK_REPRESENTATION_NARROW_THEOREM_NOTE_2026-05-17.md`](LHCM_MATTER_ASSIGNMENT_SU3_BLOCK_REPRESENTATION_NARROW_THEOREM_NOTE_2026-05-17.md)
- [`CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md)
- [`RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md`](RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md)

**Related landed source input:**

- [`COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md`](COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md)

## Purpose

The prior block named `MR_color` as the residual between algebraic
symmetric-base `SU(3)` and physical color. This note splits that residual into
smaller pieces so later work can target the real blocker instead of treating
the whole matter realization as opaque.

## Result

`MR_color` decomposes into a supported carrier-content half plus three
remaining realization gates:

| subpiece | current support | status in this map | output |
|---|---|---|---|
| axis selection | graph-first selector | support | a selected axis, hence a canonical fiber/base split |
| symmetric-base `SU(3)` carrier | graph-first integration and Gell-Mann embedding | support | `Sym^2(C^2)` is the 3D non-trivial `SU(3)` block |
| LH doublet block content | LHCM narrow theorem | support | `(2,3) ⊕ (2,1)` structural decomposition |
| SM species naming | parent LHCM convention | residual convention | names the `SU(3)`-charged block "quark" and singlet block "lepton" |
| color-record readout | landed record-invariance antecedent | residual antecedent | says the physical records are color singlets |
| link-index routing | not supplied by the carrier block | residual construction | puts the base-`SU(3)` index on links/connections |
| formation/action dynamics | not supplied here | residual construction | Gauss generators, Wilson observables, action/couplings, rates, time |

Therefore the useful refined form is:

```text
MR_color =
  supported carrier-content surface
  + SM species naming convention
  + color-record readout antecedent
  + link-index routing construction
  + formation/action dynamics.
```

The first line is no longer the hard part. The remaining blocker is not "find a
3D color block"; the framework already has a structural 3D block. The blocker
is to route that block into physical matter, records, and link transport
without silently importing the physical interpretation.

## No-Go Discipline Gate

**No-go discipline result:** PASS for support-map scoping only. This note does
not foreclose physical color; it prevents carrier support from being mistaken
for full matter realization.

**N1. Alternative routes.** Five possible overclaim routes are checked:
carrier-content-only closure, SM species naming by algebra alone,
color-record readout by carrier support alone, base-`SU(3)` link routing by
block dimension alone, and post-record append/count closure. Each remains
separate in the interface table.

**N2. Wall independence.** The map collapses the residual to four named gates:
species naming, color-record readout, link-index routing, and formation/action
dynamics. None is presented as closing another.

**N3. Hidden-wall scan.** "Supported carrier content" means only the structural
block outputs listed in the runner. The physical interpretation gates are
explicit residuals, not hidden assumptions.

**N4. Residual matching.** Graph-first/LHCM sources support carrier structure;
the landed record-invariance bridge supports the color-record antecedent only
when adopted. Neither is cited as a full color realization.

**N5. Rhetoric audit.** The phrase "no longer the hard part" applies only to
finding a 3D structural block. It does not claim the SM species names, record
readout, link routing, or dynamics are solved.

**N6. Partial-closure path scan.** Rows needing only structural block content
can consume the support chain. Rows needing physical color still need explicit
admission or derivation of the remaining gates.

**N7. Steelman.** A future graph-first matter theorem might derive species
naming and link routing from the same carrier support. This map leaves that
route open rather than precluding it.

**N8. Cross-cycle echo.** The split follows the same carrier-versus-physical
interpretation discipline used in the landed color record-invariance bridge.

## What this buys

This split makes later color and matter audit work more precise:

1. A row needing only the structural `(2,3) ⊕ (2,1)` block content can cite the
   graph-first/LHCM support chain.
2. A row that calls the `(2,3)` block a quark doublet still consumes the SM
   naming convention.
3. A row that claims physical color-singlet records still consumes the
   color-record readout antecedent.
4. A row with Wilson lines, Gauss laws, gauge bosons, couplings, or QCD
   dynamics still consumes link-routing and dynamics/action bridges.
5. Record append/count dynamics becomes useful only after a formation/readout
   bridge supplies realized color-singlet atoms.

## Interface diagram

```text
graph-first selector
  -> canonical axis
  -> Sym^2(C^2) + Anti^2(C^2)
  -> structural SU(3) block content: (2,3) + (2,1)
  -- still needs -->
     SM species naming
     color-record readout antecedent
     base-SU(3) link-index routing
     formation/Gauss/action dynamics
  -> realized color-singlet record atoms
  -> post-record O* / N^O append-count dynamics
```

## Boundaries

- Does not derive physical color.
- Does not derive the SM species names.
- Does not identify color-singlet records as the physical record algebra.
- Does not route the base-`SU(3)` index onto link variables.
- Does not derive Gauss generators, Wilson observables, gauge action,
  couplings, rates, time, confinement, or continuum QCD.
- Does not select a Koide/generation dial location.
- Does not apply audit verdicts.

## Runner summary

The runner verifies:

- `dim Sym^2(C^2)=3`, `dim Anti^2(C^2)=1`, and the LH doublet split has
  dimensions `(2,3)=6` and `(2,1)=2`;
- the carrier-content outputs are disjoint from the required link-routing and
  post-record outputs;
- the color-record readout antecedent is separate from both carrier content
  and post-record append/count;
- full `MR_color` remains incomplete if link-index routing or the
  color-record readout antecedent is absent;
- the note keeps physical-color derivation, species naming derivation, link
  routing, action/coupling, and dial-selection claims out of scope.

Expected result:

```text
SCORECARD PASS=53 FAIL=0
```

Claim ID for audit seeding: `color_mr_carrier_routing_split_2026-06-05`.
