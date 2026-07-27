## Science block

Closes the finite derivation behind the teleportation initial-state
preparation open gate without claiming an operational preparation protocol.

## Artifacts

- [`HANDOFF.md`](.claude/science/physics-loops/teleportation-initial-state-preparation-closure/HANDOFF.md)
- [`TRACE_GATE.md`](.claude/science/physics-loops/teleportation-initial-state-preparation-closure/TRACE_GATE.md)
- [`REVIEW_HISTORY.md`](.claude/science/physics-loops/teleportation-initial-state-preparation-closure/REVIEW_HISTORY.md)
- [`CLAIM_STATUS_CERTIFICATE.md`](.claude/science/physics-loops/teleportation-initial-state-preparation-closure/CLAIM_STATUS_CERTIFICATE.md)
- [`TELEPORTATION_INITIAL_STATE_PREPARATION_PROBE_NOTE.md`](docs/TELEPORTATION_INITIAL_STATE_PREPARATION_PROBE_NOTE.md)
- [`frontier_teleportation_initial_state_preparation_probe.py`](scripts/frontier_teleportation_initial_state_preparation_probe.py)
- [`frontier_teleportation_initial_state_preparation_probe.txt`](logs/runner-cache/frontier_teleportation_initial_state_preparation_probe.txt)

## Claim movement

The note now gives the exact periodic Fourier spectrum, proves the unique
uniform one-species ground and exact gaps on both default surfaces, propagates
that result through the two-species Kronecker sum, and closes separability and
maximal native-support formulas. The runner independently checks the matrix
identities, expected energies/gaps, factorization, Schmidt ranks, and support,
and exits nonzero on a failed certificate.

Trace class: `direct_blocker_closure`. Reachability closes the finite
open-gate statement only. Cooling/control/readout, noise, and operational
preparation-time scaling remain open.

## Verification

- runner compile/default certificate/cache freshness: pass
- independent shift-matrix and pair-spectrum check: pass
- custom high-gap failure and exact-boundary tolerance checks: pass
- vocabulary lint and diff check: pass
- audit pipeline and strict lint: no errors
- review-loop: pass after two iterations

Independent audit is required before the repo treats the changed source as a
clean open-gate authority surface. This PR contains no audit verdict or
generated audit-authority output.
