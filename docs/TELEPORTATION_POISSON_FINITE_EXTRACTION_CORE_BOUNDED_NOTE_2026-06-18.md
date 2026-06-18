---
claim_id: teleportation_poisson_finite_extraction_core_bounded_note_2026-06-18
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Teleportation Poisson Finite Extraction Core

**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support.
**Trace class:** upstream_support.
**Reachability:** supports `teleportation_resource_from_poisson_note` by
isolating the finite offline extraction from the open native
preparation/readout theorem.
**Primary runner:** `scripts/teleportation_poisson_finite_extraction_core_2026_06_18.py`

## Scope

This companion certifies the bounded finite extraction that the parent
Poisson/CHSH teleportation row already computes:

1. the default finite surfaces are `1D N=8`, `G=1000` and `2D 4x4`, `G=1000`,
   with the `1D N=8`, `G=0` null control;
2. the Poisson/CHSH helper source constructs the finite Hamiltonians and
   ground states;
3. the retained-axis logical-operator selection is routed through RALA;
4. tracing cells and spectator tastes while keeping the last retained taste
   bit per species yields a deterministic logical two-qubit resource on the
   two Poisson/CHSH cases;
5. the `G=0` null control fails the high-fidelity entangled-resource test.

## Certified Bounded Claims

The runner checks:

- helper-source visibility for `scripts/frontier_bell_inequality.py`;
- RALA ledger status and theorem snippets;
- last-taste logical carrier checks on all default cases;
- ideal `Phi+` teleportation convention sanity;
- null-control separation;
- Bell overlap, negativity, CHSH, and standard teleportation-fidelity
  thresholds for the two Poisson/CHSH cases;
- parent-note firewalls preserving the native preparation/readout blocker.

This is a bounded finite computation theorem.  It is not a continuum theorem,
not a full resource-preparation theorem, and not a physical apparatus theorem.

## Cited Authority Surface

Load-bearing one-hop authority:

- [`TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md`](TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md)
  supplies the retained-axis logical-operator algebra (RALA) used for the
  finite last-taste logical carrier selection.

## Boundary

Do not cite this note as:

- deterministic physical teleportation-resource closure;
- native Poisson-resource preparation/readout authority;
- durable record or detector/apparatus closure;
- matter, charge, mass, or faster-than-light transport;
- a continuum or infinite-volume teleportation theorem;
- retained-grade status for the parent open gate.

The live parent blocker remains the native preparation/readout and apparatus
theorem for producing and reading this Poisson resource as a physical
deterministic resource.

## Review Boundary Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  The finite offline extraction closes on the named small surfaces, but the
  native preparation/readout and apparatus theorem remains open.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/teleportation_poisson_finite_extraction_core_2026_06_18.py
```

Expected result:

```text
TOTAL: PASS=... FAIL=0
```
