# PR230 Block129 Schur pole-authority construction attempt

## Summary

This stacked physics-loop block pivots after Block128 to the Schur/Feshbach
route.  It tests whether the prior finite `C_x|s` one-pole/Stieltjes diagnostic
can become pole authority now that the higher-shell Schur packet is complete,
then attempts the stricter construction from explicit row sidecars, raw
higher-shell rows, and finite A/B/C support.

Result: exact negative boundary.  The two-point one-pole scout is falsified by
unused higher-shell rows with max absolute residual z-score
`243.36741086003715`; no finite Loewner/Stieltjes proxy survives necessary
sign tests; no explicit strict row sidecar exists; 63/63 raw higher-shell files
contain 693 finite source-Higgs rows and 693 finite scalar-LSZ rows but zero
strict pole keys; finite A/B/C promotion remains blocked by Block121; and
Block128 keeps W/Z and source-Higgs bridge roots absent.

## Artifacts

- `docs/YT_PR230_BLOCK129_SCHUR_ONE_POLE_LOEWNER_FALSIFICATION_NOTE_2026-05-17.md`
- `docs/YT_PR230_BLOCK129_SCHUR_POLE_AUTHORITY_CONSTRUCTION_ATTEMPT_NOTE_2026-05-17.md`
- `scripts/frontier_yt_pr230_block129_schur_one_pole_loewner_falsification.py`
- `scripts/frontier_yt_pr230_block129_schur_pole_authority_construction_attempt.py`
- `outputs/yt_pr230_block129_schur_one_pole_loewner_falsification_2026-05-17.json`
- `outputs/yt_pr230_block129_schur_pole_authority_construction_attempt_2026-05-17.json`
- `.claude/science/physics-loops/pr230-retained-closure-campaign-20260517/HANDOFF.md`

## Verification

- `python3 -m py_compile scripts/frontier_yt_pr230_block129_schur_one_pole_loewner_falsification.py scripts/frontier_yt_pr230_block129_schur_pole_authority_construction_attempt.py scripts/frontier_yt_pr230_campaign_status_certificate.py scripts/frontier_yt_pr230_assumption_import_stress.py`
- `python3 scripts/frontier_yt_pr230_block129_schur_one_pole_loewner_falsification.py` -> `PASS=13 FAIL=0`
- `python3 scripts/frontier_yt_pr230_block129_schur_pole_authority_construction_attempt.py` -> `PASS=14 FAIL=0`
- `python3 scripts/frontier_yt_pr230_campaign_status_certificate.py` -> `PASS=449 FAIL=0`
- `python3 scripts/frontier_yt_pr230_assumption_import_stress.py` -> `PASS=132 FAIL=0`
- `python3 scripts/frontier_yt_retained_closure_route_certificate.py` -> `PASS=325 FAIL=0`
- `python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py` -> `PASS=200 FAIL=0`
- `python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py` -> `PASS=79 FAIL=0`
- `python3 scripts/frontier_yt_fh_lsz_target_timeseries_full_set_checkpoint.py` -> `PASS=9 FAIL=0`
- `python3 scripts/frontier_yt_pr230_schur_higher_shell_chunk_checkpoint.py --chunk 63` -> `PASS=15 FAIL=0`

## Claim Boundary

This PR does not claim retained or `proposed_retained` closure.  PR #230 stays
open/draft.  The next admissible Schur move is a true strict pole-row artifact
with pole coordinate, `K'(pole)` or `l K' r`, source projection numerator,
FV/IR/contact/model-class authority, and a physical bridge.  Otherwise pivot to
neutral H3/H4 physical-transfer/source-coupling authority.
