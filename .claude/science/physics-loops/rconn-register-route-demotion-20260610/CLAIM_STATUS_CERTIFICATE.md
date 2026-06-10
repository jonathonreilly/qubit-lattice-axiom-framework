# Claim Status Certificate

## Current Claim Surface

Actual current-surface status:

```text
demotion / negative route pruning
```

This branch does not propose a positive `kappa_EW = 0` theorem. It
repairs the source surface for the audited-conditional Rconn row by demoting
the specific register-not-read color-trace route.

## What Moves

- The exact Fierz `S+C` decomposition and `F_adj = 8/9` channel-count algebra
  remains intact.
- The previous shortcut "singlet trace is unregistered, therefore
  `kappa_EW = 0`" is now marked as not closed on the current surface.
- The runner verifies the load-bearing obstruction directly:
  - singlet projection is a twirl, not a finite central-sector partition;
  - `8/9` is a count, while `kappa_EW` is a within-channel weight;
  - the Record/Quantum axiom memo does not supply the missing readout context
    or physical observable bridge.

## Still Open

`kappa_EW` remains open. A future non-axiom theorem, explicit convention, or
owner-approved admission could still supply the physical EW readout/weighting
bridge. This branch does not foreclose those routes.

## Proposal Gate

```yaml
actual_current_surface_status: demotion
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The artifact prunes one proposed selector route; it does not close the selector."
audit_required_before_effective_status_change: true
bare_retained_allowed: false
```
