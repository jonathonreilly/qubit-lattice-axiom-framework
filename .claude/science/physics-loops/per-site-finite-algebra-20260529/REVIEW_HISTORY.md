# Review History

2026-05-29:

- Identified four per-site audited conditional rows whose common blocker was
  reliance on an older per-site uniqueness row for physical `H_x = C^2`.
- Repaired the statements against A1's explicit `M_2(C)` qubit algebra.
- Added runner source firewalls to prevent accidental reintroduction of the
  old load-bearing dependency.
- Ran the four repaired runners, Python compilation, and the audit pipeline.

No review-loop PR review has been run from this branch. The Codex reviewer
is expected to review and extract/land the science.
