---
claim_id: color_mr_carrier_routing_split_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Color `MR_color` Carrier/Routing Split

**Date:** 2026-06-05
**Claim type:** bounded support map.
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

**Related open PR input, not imported as current-main authority:**

- PR #2729, `color-su3-bridge-from-record-2026-06-05`

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
| color-record readout | PR #2729-style antecedent | residual antecedent | says the physical records are color singlets |
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

```yaml
claim_id: color_mr_carrier_routing_split_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
