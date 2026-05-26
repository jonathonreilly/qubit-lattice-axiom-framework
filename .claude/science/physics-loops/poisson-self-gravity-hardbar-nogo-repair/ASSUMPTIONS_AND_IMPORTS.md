# Assumptions And Imports

## Included Artifacts

- `logs/runner-cache/poisson_self_gravity_loop.txt`
- `logs/runner-cache/poisson_self_gravity_born_audit.txt`
- `logs/runner-cache/poisson_self_gravity_loop_v3.txt`

The runner parses these cached outputs instead of rerunning the long sweeps.

## Not Imported

- No physical gravity observation.
- No fitted attraction target.
- No new self-gravity axiom.
- No audit verdict.

## Scope

The no-go is finite: it applies to the tested exact-lattice family and cached
runner outputs. It is not a universal self-gravity impossibility theorem.
