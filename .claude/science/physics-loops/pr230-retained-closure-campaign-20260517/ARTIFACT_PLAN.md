# Artifact Plan

## Block117

Working title: PR230 Block117 source-reparametrization invariant minimal-data
boundary.

Purpose:

- derive the minimal invariant data needed to read `y_t` from same-surface
  PR230 observables without `v`, observed targets, `H_unit`, or unit
  normalizations;
- classify current source-only, finite-shell, W/Z, Schur, and neutral rows by
  source-reparametrization behavior;
- produce an exact next-packet contract that reduces future work to the
  smallest admissible physical certificate.

Files:

- `docs/YT_PR230_BLOCK117_SOURCE_REPARAM_INVARIANT_MINIMAL_DATA_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py`
- `outputs/yt_pr230_block117_source_reparam_invariant_minimal_data_2026-05-17.json`

Result: exact negative boundary.  The runner found no current strict
source-Higgs, W/Z, Schur, or neutral disjunct and preserved the FH/LSZ formula
as exact support only.

## Gates

Run after Block117:

- `python3 scripts/frontier_yt_pr230_block117_source_reparam_invariant_minimal_data.py`
- `python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py`
- `python3 scripts/frontier_yt_retained_closure_route_certificate.py`
- `python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py`
- `python3 scripts/frontier_yt_pr230_campaign_status_certificate.py`
- `python3 scripts/frontier_yt_pr230_assumption_import_stress.py`
- `git diff --check`

Verified at `2026-05-17T15:00:45Z`:

- Block117 runner: `PASS=14 FAIL=0`
- full positive closure assembly: `PASS=200 FAIL=0`
- retained-route certificate: `PASS=325 FAIL=0`
- positive-closure completion audit: `PASS=79 FAIL=0`
- campaign status certificate: `PASS=436 FAIL=0`
- assumption/import stress: `PASS=119 FAIL=0`
- `git diff --check`: passed
