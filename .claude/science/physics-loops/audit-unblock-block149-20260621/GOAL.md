# Goal

Package a source-side audit-unblock repair for `mass_spectrum_derived_note`.

The block adds a parser-visible bounded wrapper that executes the mass-spectrum note's current validation commands, refreshes the stale expected total from `PASS=90 FAIL=0` to `PASS=99 FAIL=0`, removes a machine-local plan path from the touched note, and keeps the row `bounded_theorem` / `unaudited` / `effective_status: unaudited`.

This is not a full mass-spectrum retention claim. It is a reviewer/audit-readiness PR.
