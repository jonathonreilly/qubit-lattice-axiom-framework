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

Run after Block120, Block121, and Block122:

- `python3 scripts/frontier_yt_pr230_block120_source_reparam_invariant_minimal_data.py`
- `python3 -m py_compile scripts/frontier_yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability.py`
- `python3 scripts/frontier_yt_pr230_block121_schur_finite_packet_pole_derivative_nonidentifiability.py`
- `python3 -m py_compile scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py`
- `python3 scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py`
- `python3 -m py_compile scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py`
- `python3 scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py`
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

## Block122

Working title: PR230 Block122 Hamming-axis action/LSZ normalization gap.

Purpose:

- test whether the Block118 finite Hamming-Dirichlet `O_H` axis plus Block119
  native finite Dirichlet support fixes accepted action, scalar LSZ metric,
  source-overlap normalization, contact subtraction, or source-Higgs pole rows;
- construct a same-axis counterfamily that keeps the finite axis and a
  source-source proxy fixed while changing action normalization, `C_sH`,
  `C_HH`, and normalized source overlap;
- close the finite-axis/native-Dirichlet promotion shortcut without weakening
  the future action-first route.

Files:

- `docs/YT_PR230_BLOCK122_HAMMING_AXIS_ACTION_LSZ_NORMALIZATION_GAP_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block122_hamming_axis_action_lsz_normalization_gap.py`
- `outputs/yt_pr230_block122_hamming_axis_action_lsz_normalization_gap_2026-05-17.json`

Result: exact negative boundary.  The finite axis and native Dirichlet support
remain useful support, but they do not supply accepted action/LSZ/source-overlap
or strict physical `C_ss/C_sH/C_HH` pole rows.

Verified at `2026-05-17T15:48:22Z`:

- Block122 py_compile: passed
- Block122 runner: `PASS=11 FAIL=0`
- full positive closure assembly: `PASS=200 FAIL=0`
- retained-route certificate: `PASS=325 FAIL=0`
- positive-closure completion audit: `PASS=79 FAIL=0`
- campaign status certificate: `PASS=440 FAIL=0`
- assumption/import stress: `PASS=123 FAIL=0`
- target-timeseries full-set checkpoint: `PASS=9 FAIL=0`
- chunk063 higher-shell checkpoint: `PASS=15 FAIL=0`

## Block123

Working title: PR230 Block123 source-Higgs LSZ readout formula.

Purpose:

- derive the source-Higgs pole-row readout that would convert `dE_top/ds` into
  canonical-Higgs response without setting `kappa_s = 1`;
- prove source-coordinate rescaling invariance of
  `y_H=(dE_top/ds)*sqrt(Res C_HH)/Res C_sH`;
- record the orthogonal-top-coupling premise that source-Higgs residues alone
  do not remove unless Gram/covariance/top-coupling leakage is certified;
- preserve the claim firewall because the current strict pole rows and
  canonical `O_H`/action authority are absent.

Files:

- `docs/YT_PR230_BLOCK123_SOURCE_HIGGS_LSZ_READOUT_FORMULA_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block123_source_higgs_lsz_readout_formula.py`
- `outputs/yt_pr230_block123_source_higgs_lsz_readout_formula_2026-05-17.json`

Result: exact support plus open premise.  The readout formula is derived and
executable, but current PR230 does not satisfy the row/action premises.

Verified at `2026-05-17T15:56:21Z`:

- Block123 py_compile: passed
- Block123 runner: `PASS=12 FAIL=0`
- campaign status certificate: `PASS=441 FAIL=0`
- assumption/import stress: `PASS=124 FAIL=0`

## Block124

Working title: PR230 Block124 completed source-Higgs row intake.

Purpose:

- consume the completed 63/63 higher-shell source-Higgs/taste-radial packet;
- verify that the rows remain finite `C_ss/C_sx/C_xx` support and not strict
  same-pole `C_ss/C_sH/C_HH` residues;
- expose the finite Gram diagnostic without promoting it to scalar-LSZ or
  canonical-Higgs authority;
- keep the Block123 readout contract as the next exact positive target.

Files:

- `docs/YT_PR230_BLOCK124_COMPLETED_SOURCE_HIGGS_ROW_INTAKE_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block124_completed_source_higgs_row_intake.py`
- `outputs/yt_pr230_block124_completed_source_higgs_row_intake_2026-05-17.json`

Result: bounded support only.  The runner checks 693 finite rows and finds no
strict pole rows, no accepted canonical `O_H`, and no allowed closure.

Verified at `2026-05-17T16:19:17Z`:

- Block124 py_compile: passed
- Block124 runner: `PASS=10 FAIL=0`
- campaign status certificate: `PASS=442 FAIL=0`
- assumption/import stress: `PASS=125 FAIL=0`

## Block125

Working title: PR230 Block125 post-chunk strict contract resolver.

Purpose:

- scan all 63 completed raw production `ensemble_measurement.json` files after
  the chunk campaign;
- check whether source-Higgs schema fields hide strict `C_ss/C_sH/C_HH` pole
  rows or accepted canonical `O_H` authority;
- check whether W/Z, Schur, or neutral strict row/certificate roots are present
  on the completed surface;
- rank the next genuine artifact without promoting finite rows, scout rows, or
  support contracts.

Files:

- `docs/YT_PR230_BLOCK125_POST_CHUNK_STRICT_CONTRACT_RESOLVER_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block125_post_chunk_strict_contract_resolver.py`
- `outputs/yt_pr230_block125_post_chunk_strict_contract_resolver_2026-05-17.json`

Result: exact negative boundary.  The raw completed surface contains 693 finite
source-Higgs rows and 693 scalar LSZ support rows, but zero time-kernel rows,
zero pole-residue rows, zero W/Z response rows, zero Schur `K'`/pole hits, and
zero neutral transfer/primitive hits.

Verified at `2026-05-17T16:37:59Z`:

- Block125 py_compile: passed
- Block125 runner: `PASS=10 FAIL=0`
- campaign status certificate: `PASS=443 FAIL=0`
- assumption/import stress: `PASS=126 FAIL=0`

## Block126

Working title: PR230 Block126 matched top additive-subtraction packet.

Purpose:

- consume the completed raw production files for same-configuration top-side
  matching;
- join `dE_top/ds` and `dE_top/dm_bare` into `T_total`, `A_top`, and `T-A`
  rows;
- compute the top-side covariance packet that a future genuine W/Z route can
  join against;
- preserve the boundary that top-side rows alone are not W/Z response, strict
  `g2`, accepted action, or retained closure.

Files:

- `docs/YT_PR230_BLOCK126_MATCHED_TOP_ADDITIVE_SUBTRACTION_PACKET_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block126_matched_top_additive_subtraction_packet.py`
- `outputs/yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json`

Result: bounded support.  The runner checks 63/63 raw files, 1008 matched tau1
rows, and 23 complete tau slices.  It computes the top-side covariance packet
but leaves W/Z rows, matched top-W/Z covariance, strict `g2`, and accepted
action absent.

Verified at `2026-05-17T16:53:54Z`:

- Block126 py_compile: passed
- Block126 runner: `PASS=10 FAIL=0`
- campaign status certificate: `PASS=444 FAIL=0`
- assumption/import stress: `PASS=127 FAIL=0`

## Block127

Working title: PR230 Block127 W/Z builder Block126 top-packet adapter.

Purpose:

- wire the Block126 matched top-side additive-subtraction packet into the W/Z
  mass-fit response-row builder as the current top-side support input;
- preserve the strict W/Z boundary by refusing measurement rows until genuine
  W/Z mass-fit rows, matched top-W/Z covariance, strict non-observed `g2`, and
  accepted same-source EW/Higgs action authority exist;
- keep the route checkpoint focused on the now-real missing W/Z side instead
  of the retired missing top-response certificate.

Files:

- `docs/YT_PR230_BLOCK127_WZ_BUILDER_BLOCK126_TOP_PACKET_ADAPTER_NOTE_2026-05-17.md`
- `scripts/frontier_yt_wz_mass_fit_response_row_builder.py`
- `scripts/frontier_yt_pr230_block127_wz_builder_block126_top_packet_adapter.py`
- `outputs/yt_wz_mass_fit_response_row_builder_2026-05-04.json`
- `outputs/yt_pr230_block127_wz_builder_block126_top_packet_adapter_2026-05-17.json`

Result: bounded support.  The W/Z builder recognizes the 1008-row Block126
top-side packet and records that it is not strict W/Z input.  No strict rows
are written, and W/Z rows, matched top-W/Z covariance, strict `g2`, and
accepted action remain absent.

Verified at `2026-05-17T17:07:23Z`:

- W/Z builder current mode: `PASS=10 FAIL=0`
- W/Z builder scout mode: `PASS=9 FAIL=0`
- Block127 py_compile: passed
- Block127 runner: `PASS=10 FAIL=0`
- retained-route certificate: `PASS=325 FAIL=0`
- full positive closure assembly: `PASS=200 FAIL=0`
- positive-closure completion audit: `PASS=79 FAIL=0`
- target-timeseries full-set checkpoint: `PASS=9 FAIL=0`
- chunk063 higher-shell checkpoint: `PASS=15 FAIL=0`
- campaign status certificate: `PASS=445 FAIL=0`
- assumption/import stress: `PASS=128 FAIL=0`
