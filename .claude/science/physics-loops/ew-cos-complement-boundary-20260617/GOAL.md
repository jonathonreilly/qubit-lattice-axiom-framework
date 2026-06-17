# Goal

Repair the EW `cos^2(theta_W)` complement bridge so it no longer blocks the
audit with stale retained-language and stale runner/cache failures.

This branch does not audit the row, retag the ledger, or land anything to
`main`. It prepares a source-side review PR that the reviewer can extract.

Target result: bounded-support source packet with exact arithmetic preserved,
dependency gates named, cache refreshed, and no hard runner failure markers.
