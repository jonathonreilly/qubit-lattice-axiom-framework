# Handoff

The primary runner now constructs a native-parity block certificate before its expected classification checks. For each audited case it verifies the matrix identity `Z_native|_e = sigma_s Z_logical`, exact environment multiplicity, sign balance, and the resulting factorization boundary.

The full runner presently reaches the downstream boundary guard and exits nonzero because several separate audit-controlled downstream rows are `unaudited`. The local factorization and no-record checks complete successfully before that guard.

Review-loop disposition: PASS. The validation pipeline and strict lint completed without errors, and its generated audit surfaces were restored to `origin/main`. A separate exhaustive enumeration reproduced every block sign and count without importing the runner.

Exact next action: commit the review-clean block, push its science-fix branch, and open the review PR for independent re-audit after landing.
