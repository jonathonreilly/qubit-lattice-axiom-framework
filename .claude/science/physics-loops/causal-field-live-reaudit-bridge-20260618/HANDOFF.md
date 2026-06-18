# Handoff

## What This PR Does

Adds a source-side re-audit bridge for `causal_propagating_field_note`.

The bridge verifies that:

- the archived note remains explicitly retracted and non-authoritative;
- the live packet note points to an executable primary runner/cache;
- the manifest runner/cache/JSON are present and passing;
- the live packet does not restore the archived `0.63 / 0.45` table.

## What It Does Not Do

- No audit ledger or queue edits.
- No status promotion.
- No main landing by this agent.
- No claim of physical wave-speed measurement, geometry independence, or
  cross-family portability.

## Reviewer Focus

Check whether this is enough source-side structure for the auditor to re-audit
the live packet as a bounded finite replay. If accepted, the reviewer can
extract the bridge without needing to merge any audit results from this PR.
