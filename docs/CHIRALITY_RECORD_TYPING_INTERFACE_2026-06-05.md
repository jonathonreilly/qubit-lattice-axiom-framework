---
claim_id: chirality_record_typing_interface_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Chirality / Record Typing Interface

**Date:** 2026-06-05
**Claim type:** bounded support map and negative route-pruning certificate.
**Status authority:** independent audit lane only. This source note does not
apply audit verdicts, edit audit data, or assert package promotion.
**Primary runner:**
[`scripts/frontier_chirality_record_typing_interface_2026_06_05.py`](../scripts/frontier_chirality_record_typing_interface_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_chirality_record_typing_interface_2026_06_05.txt`](../logs/runner-cache/frontier_chirality_record_typing_interface_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md`](RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md)
- [`RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md`](RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md)
- [`KOIDE_SIGNED_READOUT_IS_NOT_CHIRALITY_NARROW_NO_GO_NOTE_2026-06-04.md`](KOIDE_SIGNED_READOUT_IS_NOT_CHIRALITY_NARROW_NO_GO_NOTE_2026-06-04.md)
- [`KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md`](KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md)
- [`FLAVOR_CHIRALITY_GATE_NARROWS_TO_ONE_SPIN_STATISTICS_IMPORT_2026-05-31.md`](FLAVOR_CHIRALITY_GATE_NARROWS_TO_ONE_SPIN_STATISTICS_IMPORT_2026-05-31.md)
- [`FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md`](FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md)

## Purpose

Record typing now separates pre-record carrier dynamics from post-record
information dynamics. This note applies that separation to the chirality lane:

```text
Does post-record sign/readout information supply chirality?
```

No. A signed spectrum or signed record readout can be post-record information.
Chirality is a carrier/dynamics relation: an anticommutation, graded tensor
support, CAR/Jordan-Wigner frame, or first-order Dirac/staggered structure.

The useful output is an interface:

```text
carrier supplies chirality / readout bridge
  -> realized chiral or signed record atoms
  -> post-record histories/counts/readouts.
```

The last arrow is exact record information dynamics. The first arrow remains
the chirality gate.

## Result

| object | layer | what record dynamics can do | what remains outside record dynamics |
|---|---|---|---|
| signed scalar readout | post-record information | append, count, coarse-grain, add finite scalar readouts | force the signed-vs-absolute readout choice |
| chiral grading | carrier algebra | record a realized chiral label after a bridge supplies it | derive anticommutation or graded support |
| CAR/Jordan-Wigner frame | carrier/tensor support | record outcomes after a fermionic frame is supplied | choose the fermionic frame from ungraded qubits |
| chiral/holomorphic Koide readout | carrier/readout bridge | record the chosen readout as data | select chiral over vector readout |
| emergent spacetime chirality | carrier dynamics | record realized labels if transported | transport generation chirality by itself |

So record dynamics is a consumer, not a chirality source.

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| signed eigenvalues imply chirality | pruned | a signed Hermitian operator can commute with a grading |
| Hermiticity forces signed square-root readout | pruned | signed and absolute readouts are both real-valued choices on a real spectrum |
| post-record counts select chiral/holomorphic weighting | pruned | counts update after a readout is chosen |
| ungraded qubit tensor product selects CAR | pruned | existing chirality gate shows Jordan-Wigner changes tensor-support bookkeeping |
| emergent spacetime chirality transports to generation | pruned | existing no-transport note keeps that bridge open |

These are route-specific prunings. They do not say chirality is impossible.

## What remains open

- A carrier or dynamics theorem that supplies the chiral grading relation.
- A spin-statistics / CAR / Jordan-Wigner bridge for the physical matter frame.
- A derivation of chiral/holomorphic rather than vector/real readout on the
  Koide `r` lane.
- A generation transport bridge if spacetime chirality is used.
- A measurement/readout bridge that turns carrier chirality into realized
  record atoms.

## What this unlocks

Audit and physics lanes can now route claims by type:

1. Claims needing only finite signed labels, counts, or additive scalar readout
   can use the exact post-record layer.
2. Claims needing anticommutation, chirality, CAR, spin-statistics, or
   chiral/holomorphic weighting still need carrier/readout bridge support.
3. A future chirality theorem can feed record dynamics cleanly after it
   supplies realized atoms; it does not need a new history axiom.

## Boundaries

- Does not derive chirality.
- Does not derive a fermionic matter frame, CAR, spin-statistics, or
  Jordan-Wigner selection.
- Does not select signed over absolute square-root readout.
- Does not derive Koide `r = 1/2` or the chiral/holomorphic readout.
- Does not derive measurement, production, rates, or time.
- Does not select a Koide/generation dial location.
- Does not apply audit verdicts.

## Runner summary

The runner verifies:

- a signed Hermitian operator can commute with a grading and fail the
  anticommutation chirality test;
- an anticommuting chiral operator has the sign-symmetric spectrum pattern but
  signed spectrum alone is not enough to identify chirality;
- signed and absolute readouts are distinct real-valued readout choices on the
  same real spectrum;
- post-record outputs are disjoint from chirality/carrier outputs;
- record dynamics can consume realized chiral labels but cannot produce the
  carrier grading relation.

Expected result:

```text
SCORECARD PASS=44 FAIL=0
```

```yaml
claim_id: chirality_record_typing_interface_2026-06-05
actual_current_surface_status: bounded-support
trace_class: negative_route_pruning
reachability_to_target: prunes
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
