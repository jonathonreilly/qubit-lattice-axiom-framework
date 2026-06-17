# Handoff

This PR adds `scripts/propagator_family_scaffold_bridge.py` and pairs it with
`docs/PROPAGATOR_FAMILY_UNIFICATION_NOTE.md`.

Claim movement:

- Adds 18-check bounded source certificate for the factorized scalar
  edge-update scaffold shared by wavefield, complex-action, and electrostatics
  source runners.
- Updates the synthesis note away from stale conditional prose about the
  complex-action parent and toward bounded scaffold support.
- Adds canonical primary-runner/cache metadata to
  `docs/SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md`, the remaining upstream
  dependency for this synthesis.

Limits:

- No audit result files are changed.
- No ledger retagging is done.
- No new axioms are introduced.
- The branch does not claim continuum closure, full electromagnetism,
  self-gravity, geometry-generic transfer, or retained status.
- The source-resolved wavefield dependency still needs independent audit.

Reviewer next step: run the review-loop if desired, extract the bounded source
packet, and decide whether to queue the bridge plus wavefield dependency for
independent audit.

