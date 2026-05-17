# Artifact Plan

## Block120

Working title: PR230 Block120 source-reparametrization invariant minimal-data
boundary.

Purpose:

- derive the minimal invariant data needed to read `y_t` from same-surface
  PR230 observables without `v`, observed targets, `H_unit`, or unit
  normalizations;
- classify current source-only, finite-shell, W/Z, Schur, and neutral rows by
  source-reparametrization behavior;
- account for base Block117 strict Schur/scalar-LSZ absence and base Block118
  exact Hamming-Dirichlet `O_H` axis support without promoting either to
  closure;
- produce an exact next-packet contract that reduces future work to the
  smallest admissible physical certificate.

Files:

- `docs/YT_PR230_BLOCK120_SOURCE_REPARAM_INVARIANT_MINIMAL_DATA_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block120_source_reparam_invariant_minimal_data.py`
- `outputs/yt_pr230_block120_source_reparam_invariant_minimal_data_2026-05-17.json`

Result: exact negative boundary.  The runner found no current strict
source-Higgs, W/Z, Schur, or neutral disjunct and preserved the FH/LSZ formula
as exact support only.

## Gates

Run after Block120 and Block121:

- `python3 scripts/frontier_yt_pr230_block120_source_reparam_invariant_minimal_data.py`
- `python3 -m py_compile scripts/frontier_yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability.py`
- `python3 scripts/frontier_yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability.py`
- `python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py`
- `python3 scripts/frontier_yt_retained_closure_route_certificate.py`
- `python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py`
- `python3 scripts/frontier_yt_pr230_campaign_status_certificate.py`
- `python3 scripts/frontier_yt_pr230_assumption_import_stress.py`
- `git diff --check`

## Block121

Working title: PR230 Block121 Schur finite-packet pole-derivative
nonidentifiability boundary.

Purpose:

- test the strongest current Schur/Feshbach support packet after Block113;
- prove that complete finite A/B/C rows at the current finite qhat^2 nodes do
  not determine strict `K'(pole)` or residue;
- leave the next exact Schur requirement as strict pole derivative/residue rows
  or an accepted analytic continuation/model-class plus FV/IR/contact bridge.

Files:

- `docs/YT_PR230_BLOCK121_SCHUR_FINITE_PACKET_POLE_DERIVATIVE_NONIDENTIFIABILITY_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability.py`
- `outputs/yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability_2026-05-17.json`

Result: exact negative boundary.  The runner constructs a finite-node
vanishing perturbation that preserves all finite rows and the pole location
while changing `K'(pole)` and the residue.

Verified at `2026-05-17T15:00:45Z`:

- Block120 runner: `PASS=14 FAIL=0` on the pre-rebase Block116 surface
- full positive closure assembly: `PASS=200 FAIL=0`
- retained-route certificate: `PASS=325 FAIL=0`
- positive-closure completion audit: `PASS=79 FAIL=0`
- campaign status certificate: `PASS=436 FAIL=0`
- assumption/import stress: `PASS=119 FAIL=0`
- `git diff --check`: passed

Verified at `2026-05-17T15:11:38Z`:

- Block121 py_compile: passed
- Block121 runner: `PASS=10 FAIL=0`
- full positive closure assembly: `PASS=200 FAIL=0`
- retained-route certificate: `PASS=325 FAIL=0`
- positive-closure completion audit: `PASS=79 FAIL=0`
- campaign status certificate: `PASS=436 FAIL=0`
- assumption/import stress: `PASS=119 FAIL=0`
- `git diff --check`: passed

Verified at `2026-05-17T15:20:24Z` after rebasing onto PR230 head
`0cfce639f`:

- Block120 py_compile: passed
- Block120 runner: `PASS=16 FAIL=0`
- Block121 py_compile: passed
- Block121 runner: `PASS=10 FAIL=0`
- full positive closure assembly: `PASS=200 FAIL=0`
- retained-route certificate: `PASS=325 FAIL=0`
- positive-closure completion audit: `PASS=79 FAIL=0`
- campaign status certificate: `PASS=438 FAIL=0`
- assumption/import stress: `PASS=121 FAIL=0`

Verified at `2026-05-17T15:41:23Z` after rebasing onto PR230 head
`a7179acb5`:

- Block120 py_compile: passed
- Block120 runner: `PASS=16 FAIL=0`
- Block121 py_compile: passed
- Block121 runner: `PASS=10 FAIL=0`
- full positive closure assembly: `PASS=200 FAIL=0`
- retained-route certificate: `PASS=325 FAIL=0`
- positive-closure completion audit: `PASS=79 FAIL=0`
- campaign status certificate: `PASS=439 FAIL=0`
- assumption/import stress: `PASS=122 FAIL=0`
- `git diff --check`: passed
