# Claim Status Certificate

claim_id: `rconn_derived_note`

actual_current_surface_status: `bounded-support`

conditional_surface_status: null

hypothetical_axiom_status: null

admitted_observation_status: null

proposal_allowed: false

proposal_allowed_reason: this branch does not derive or admit matching rule M
or the physical connected-trace readout.

audit_required_before_effective_retained: true

bare_retained_allowed: false

The branch-local theorem surface is exact:

```text
F_adj(N_c) = (N_c^2 - 1) / N_c^2
F_adj(3) = 8/9
```

The following are explicitly outside theorem scope:

- matching rule M
- identification of the lattice connected-trace dynamical observable with the
  adjoint channel fraction
- `kappa_EW = 0`
- any retained physical EW readout

Pipeline after repair:

- `audit_status: unaudited`
- `effective_status: unaudited`
- `deps: []`
- audit queue position: 1
- ready: true
