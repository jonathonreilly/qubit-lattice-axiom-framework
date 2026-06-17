# Handoff

This block creates a live exact-support source for the NNI algebraic identities
T1-T4 and retargets the Cabibbo work-history note to that source.

What changed:

- added a live structural identities note;
- added a self-contained symbolic runner;
- retargeted the Cabibbo source edge to the live structural note;
- preserved the bounded/import-dependent boundary for the numerical Cabibbo
  value.

What remains open:

- derive quark masses on the framework surface;
- derive the NNI geometric coefficients on the framework surface;
- independently review and audit the new source edge before any repo-wide
  status change.

No generated audit/status surfaces are intentionally modified by this PR.

Verification run:

- `python3 scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py`
  -> `TOTAL: PASS=18 FAIL=0`.
- `python3 scripts/cached_runner_output.py scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py --refresh --timeout-sec 120`
  -> cache refreshed, exit 0.
- `python3 scripts/cached_runner_output.py scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py --check-only --timeout-sec 120`
  -> fresh.
- `python3 scripts/cached_runner_output.py scripts/frontier_ckm_mass_basis_nni.py --check-only --timeout-sec 120`
  -> fresh.
- `python3 scripts/frontier_ckm_mass_basis_nni.py` direct local run was blocked
  before repo code by a SciPy code-signing failure; the runner was unchanged.
- `python3 -m py_compile scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py scripts/cached_runner_output.py`
  -> pass.
- `git diff --check` -> pass.
- Forbidden generated/status path guard -> pass.
