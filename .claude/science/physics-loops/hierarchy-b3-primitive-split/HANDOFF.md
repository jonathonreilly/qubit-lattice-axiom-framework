# Handoff

## What Changed

This branch updates the hierarchy formula support row so B3 is no longer a single vague substrate/regulator gate.

- B3a is now the four-direction kinetic-form substrate, sourced to the approved `kinetic_isotropy_primitive`.
- B3b remains the hierarchy-specific regulator/species realization gate.
- B4 remains the attachment-observable gate for `alpha_LM^16` transport.

The runner now verifies the primitive registration, the primitive's scope, and the note's status firewall. Its scorecard is `PASS=29 FAIL=0`.

## What Did Not Change

- No audit verdict was written.
- No ledger row was retagged.
- No generated audit/publication/front-door status surface was committed.
- No EW VEV prediction or hierarchy formula closure is claimed.
- B3b, B4, and B5 remain open where applicable.

## Reviewer Focus

Check that the B3a split is legitimate and useful for re-audit: it should let audit treat the kinetic substrate separately from the still-open regulator/species and coupling-transport gates.
