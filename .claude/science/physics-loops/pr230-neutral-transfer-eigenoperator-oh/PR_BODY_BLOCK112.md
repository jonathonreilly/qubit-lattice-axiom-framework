### Block112 checkpoint: Helmholtz action-integrability obstruction

Audited whether current source-response rows and finite taste-radial aliases
already supply the mixed derivatives needed to integrate an accepted
same-source EW/Higgs action or fix source-Higgs overlap.

What changed:

- Added `scripts/frontier_yt_pr230_block112_helmholtz_action_integrability_obstruction.py`.
- Added `outputs/yt_pr230_block112_helmholtz_action_integrability_obstruction_2026-05-17.json`.
- Added `docs/YT_PR230_BLOCK112_HELMHOLTZ_ACTION_INTEGRABILITY_OBSTRUCTION_NOTE_2026-05-17.md`.
- Wired Block112 into `scripts/frontier_yt_pr230_campaign_status_certificate.py`.
- Wired Block112 into `scripts/frontier_yt_pr230_assumption_import_stress.py`.
- Refreshed the loop-pack state, claim certificate, no-go ledger, opportunity queue, handoff, artifact plan, assumptions, and review history.

Validation:

```text
python3 -m py_compile scripts/frontier_yt_pr230_block112_helmholtz_action_integrability_obstruction.py scripts/frontier_yt_pr230_campaign_status_certificate.py scripts/frontier_yt_pr230_assumption_import_stress.py scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py scripts/frontier_yt_retained_closure_route_certificate.py scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# OK
python3 scripts/frontier_yt_pr230_block112_helmholtz_action_integrability_obstruction.py
# SUMMARY: PASS=15 FAIL=0
python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
# SUMMARY: PASS=432 FAIL=0
python3 scripts/frontier_yt_pr230_assumption_import_stress.py
# SUMMARY: PASS=115 FAIL=0
python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py
# SUMMARY: PASS=200 FAIL=0
python3 scripts/frontier_yt_retained_closure_route_certificate.py
# SUMMARY: PASS=325 FAIL=0
python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# SUMMARY: PASS=79 FAIL=0
python3 docs/audit/scripts/audit_lint.py --strict
# OK: no errors; 5 known warnings
bash docs/audit/scripts/run_pipeline.sh
# Pipeline complete; generated docs/audit diffs restored
git diff --check
# OK
```

Current status:

- All `63` higher-shell chunks have finite taste-radial alias rows and scalar source-response slopes.
- Nonempty source-Higgs time-kernel rows found: `0`.
- Nonempty W/Z response rows found: `0`.
- Helmholtz mixed-response/action rows are absent.
- A finite counterfamily shows source-only signatures do not determine source-Higgs overlap.

Claim boundary:

- no retained or `proposed_retained` top-Yukawa closure is claimed;
- source-only FH/LSZ rows are not treated as a physical `y_t` readout;
- finite `C_ss/C_sx/C_xx` aliases are not relabeled as canonical `C_ss/C_sH/C_HH`;
- the next admissible artifact remains accepted same-surface EW/Higgs action or canonical `O_H` plus strict pole rows, a strict W/Z packet, strict Schur/Feshbach rows, or neutral H3/H4 authority.
