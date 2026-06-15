# Handoff

This branch unlocks the Wilson test-mass / finite-L distance-law row for direct
runner-backed re-audit.

Changed:

- `docs/WILSON_TEST_MASS_CONTINUUM_NOTE_2026-04-11.md`
  - Adds `Claim type`, `Runner`, and `Runner cache` lines.
  - Tightens the safe claim wording from "continuum-limit companions" to
    "finite-L distance-law companions" to match the already narrowed audited
    scope.
- `scripts/audit_companion_wilson_test_mass_continuum_finite_l_packet_2026_06_15.py`
  - Verifies source boundaries, supporting source compile, completed
    test-mass/perturbative caches, completed finite-L continuum cache, and
    diagnostic-only firewall language.
- `logs/runner-cache/frontier_continuum_limit.txt`
  - Refreshes the former timeout cache under a 600 second cap; it now exits 0
    and contains the complete L = 12, 15, 18, 20, 22, 25 table.
- `logs/runner-cache/audit_companion_wilson_test_mass_continuum_finite_l_packet_2026_06_15.txt`
  - SHA-pinned companion cache.

Generated audit/publication outputs were restored after local pipeline
verification and are not part of the PR.
