---
claim_id: dimension_upper_bound_dependency_edge_repair_note_2026-06-08
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Dimension Upper-Bound Dependency-Edge Repair Note

**Date:** 2026-06-08
**Type:** `bounded_theorem`
**Source role:** bounded source-graph dependency-edge repair only. This file is
not the parent dimension-selection theorem, not a `positive_theorem`, and not
an effective-status promotion vehicle.
**Primary runner:**
[`scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py`](../scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/dimension_upper_bound_dependency_edge_repair_2026_06_08.txt`](../logs/runner-cache/dimension_upper_bound_dependency_edge_repair_2026_06_08.txt)

## Scope

This note repairs the source-side dependency edge for
`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`.
The source claim audited here is only the wrapper's dependency graph and exact
finite-set composition; a full audit of the parent dimension-selection theorem
must be run on the parent theorem's own scope, not inferred from this repair
note.
The previous wrapper recorded Bertrand and atomic-stability results as named
textbook imports, but the current source surface exposes the available
one-hop bounded support packets as load-bearing authorities. The decisive
stable-orbit edge is now native to the repo; textbook Bertrand references are
parallel context for the stronger closed-orbit theorem.

This repair makes the current graph explicit:

| Upper-bound role | Source support packet | Runner/cache |
| --- | --- | --- |
| Native stable-orbit route | [`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/bertrand_stable_orbit_green_kernel_bridge.py`](../scripts/bertrand_stable_orbit_green_kernel_bridge.py), [`logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt`](../logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt) |
| Atomic / Coulomb route | [`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/frontier_coulomb_stability_scaling_repair.py`](../scripts/frontier_coulomb_stability_scaling_repair.py), [`logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt`](../logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt) |
| Current composition gate | [`D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md`](D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md) | [`scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py`](../scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py), [`logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt`](../logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt) |

## Bounded Composition

The current lower-bound packet exposes the finite checked support set:

```text
L_runner = {3,4,5}.
```

The two upper-bound routes compose differently with that set:

```text
L_runner intersect {d : d <= 3} = {3}      # native stable-orbit route
L_runner intersect {d : d <= 4} = {3,4}    # weak atomic-stability route
L_runner intersect {3} = {3}               # strict Coulomb-spectrum route, if separately scoped
```

So the currently decisive uniqueness gate is the native stable-orbit upper
route. The atomic route is compatible companion support under the weaker
`d <= 4` stability statement, and becomes unique only if the stronger
`d = 3` spectral statement is separately admitted and scoped.

## Non-Claims

This repair does not:

- derive the full Bertrand closed-orbit theorem from the framework;
- derive atomic stability from the framework;
- derive a framework-native electromagnetic sector or hydrogenic spectrum;
- derive a `Z^d` substrate from the present `Z^3` substrate;
- serve as the parent dimension-selection theorem;
- ask the audit lane to treat this row as a `positive_theorem`;
- promote any dimension-selection row or apply an audit verdict;
- edit `docs/audit/**`.

Its role is narrower: expose the one-hop support packets and exact finite-set
composition so the upper-bound wrapper is auditable without a load-bearing
textbook-import edge.

## Runner Certificate

The runner verifies:

- the visible source type is the canonical `bounded_theorem` enum while the
  prose role is bounded source-graph repair only;
- this note cites the wrapper, the one-hop support packets, their runners, and
  their cached outputs;
- the wrapper cites this repair note and the support packets;
- the support packets preserve their bounded support firewalls;
- the finite-set composition above is exact;
- no audit verdict is applied by this source repair.

Expected output:

```text
SUMMARY: PASS=51 FAIL=0
```

## Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "dependency-edge repair for the dimension upper-bound wrapper"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This note repairs the source graph; independent audit owns any effective-status change."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
