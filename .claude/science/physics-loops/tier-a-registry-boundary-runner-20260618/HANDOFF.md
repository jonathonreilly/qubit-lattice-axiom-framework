# Handoff

This branch adds a primary runner/cache for the Tier-A registry note. The
runner checks the human source and machine registry agree that the only genuine
Tier-A derivation targets are AC_phi_lambda and theta, that Record and the
scale-reference primitive are outside Tier-A, and that Y0/g0 are conventions.

What this does not do:

- It does not audit the Tier-A registry row.
- It does not retag ledger or effective-status outputs.
- It does not add, remove, retire, or re-grade any Tier-A admission.
- It does not promote dependents to unbounded retained.
- It does not change `tier_a_admissions.json`; it only reads it.

Reviewer extraction path: keep the source note runner pointer, runner, and
cache together. The loop pack can be retained or dropped at reviewer discretion.

Next exact action after this PR: repair the YT neutral Higgs carrier conditional
or inspect the anomaly-forces-time meta row for a similar runner gap.
