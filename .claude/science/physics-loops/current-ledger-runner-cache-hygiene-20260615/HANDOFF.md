# Handoff

This block is now a narrow source-side hygiene pack after rebasing onto
`origin/main` at `fc08b0519`. Reviewer landings already absorbed the runner
script/cache repairs from the original branch, so this refreshed PR preserves
only the still-relevant non-overlapping source edits.

The source-side changes are:

- `docs/repo/ROOT_FILE_GUIDE.md` no longer lists the top-level legacy artifact
  with a bare `.py` filename, which can be misread as a runner path when the
  citation graph is rebuilt. The file is still documented as a top-level Python
  legacy artifact.
- The two observable-principle P1 source notes now state that the unit-record
  finite-additivity schema is currently `audited_conditional`, so the source
  boundary matches the live ledger without promoting any row.

No audit verdicts, queue files, rendered ledgers, runner-cache logs, or
publication generated views are committed.

Verification performed:

- `git diff --check origin/main...HEAD`
  - clean.
- Generated-authority guard:
  - no `docs/audit/`, `docs/publication/ci3_z3/`, lane registry, active review
    queue, front-door status, status board, or README files are changed.
- `python3 -m py_compile scripts/observable_principle_p1_br_license_check_2026_06_10.py scripts/observable_principle_p1_cap_k_check_2026_06_10.py scripts/p_flux_finite_species_density_check_2026_06_10.py scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py`
  - passed; the scripts are unchanged relative to current main after conflict
    resolution.
- `python3 scripts/observable_principle_p1_br_license_check_2026_06_10.py`
  - `TOTAL: PASS=31 FAIL=0`.
- `python3 scripts/observable_principle_p1_cap_k_check_2026_06_10.py`
  - `TOTAL: PASS=31 FAIL=0`.
- `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main`
  - `2892 fresh, 0 stale, 0 missing` on the refreshed branch.
- Disposable current-main diagnostic before refreshing this PR:
  - `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main`
    reported `2914 fresh, 0 stale, 0 missing`.

Independent audit/review remains required for any row status movement. This PR
does not ask the repo to treat the observable-principle rows as retained.
