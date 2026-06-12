actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "diagnostic finite-box source/cache packet for hydrogen, helium Hartree, and one-parameter helium Jastrow companion numerics"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch repairs restricted-packet source/cache visibility; it does not promote the atomic companion to retained physics."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Dependency Classes

- Hydrogen lattice-spectrum companion runner and cache: checked.
- Helium Hartree companion runner and cache: checked.
- Helium Jastrow companion runner and cache: checked.
- Lattice-kinetic / Coulomb-kernel dependency repair verifier and cache:
  checked.

## Open Imports

- Continuum/volume-control closure is outside scope.
- Exact helium is outside scope.
- Absolute eV scale is outside scope.
- Atomic retained derivation-chain authority is outside scope.

## Firewalls

- No `docs/audit/data/**` edits.
- No audit status update.
- No retained promotion.
