# PR230 Block106 Neutral Multiplicity Gate Refresh

Status: bounded-support / runner-maintenance and source-Higgs rescan only.

Block106 refreshes the same-surface neutral multiplicity-one intake gate after
the clean source-Higgs route selector moved from the older invariant-ring/GNS
path to the action-first/FMS source-Higgs path.  The old runner still required
the exact legacy selected-route id, so a current run produced one stale failure
even though the physics verdict was unchanged: the candidate
`outputs/yt_pr230_same_surface_neutral_multiplicity_one_certificate_2026-05-07.json`
is present but rejected on the current PR230 surface.

The updated gate now checks the route-selector invariant that matters for this
contract: proposal remains disallowed and the selected route still keeps the
canonical `O_H` / source-Higgs pole-row root open.  It does not relax any
candidate acceptance criterion.  The candidate must still supply:

- same-surface `Cl(3)/Z^3` neutral representation/action data;
- multiplicity-one or primitive/irreducible generator proof;
- canonical scalar metric and LSZ normalization;
- source-to-canonical-Higgs overlap or strict `C_ss/C_sH/C_HH` pole rows;
- clean forbidden-import firewall.

The source-Higgs pole-row assembly was also rerun after the completed
higher-shell packet entered the branch.  It scanned the expanded output set and
still found no strict source-Higgs pole-row packet.  The finite higher-shell
rows remain support-only `C_ss/C_sx/C_xx` rows under the taste-radial source,
not canonical `O_H` rows and not `C_sH/C_HH` pole residues.

Verification:

```text
python3 -m py_compile scripts/frontier_yt_pr230_same_surface_neutral_multiplicity_one_gate.py
# OK
python3 scripts/frontier_yt_pr230_same_surface_neutral_multiplicity_one_gate.py
# SUMMARY: PASS=17 FAIL=0
python3 scripts/frontier_yt_canonical_higgs_operator_certificate_gate.py
# SUMMARY: PASS=11 FAIL=0
python3 scripts/frontier_yt_source_higgs_cross_correlator_certificate_builder.py
# SUMMARY: PASS=5 FAIL=0
python3 scripts/frontier_yt_source_higgs_pole_row_assembly.py
# SUMMARY: PASS=12 FAIL=0
python3 scripts/frontier_yt_pr230_full_positive_closure_assembly_gate.py
# SUMMARY: PASS=200 FAIL=0
python3 scripts/frontier_yt_retained_closure_route_certificate.py
# SUMMARY: PASS=325 FAIL=0
python3 scripts/frontier_yt_pr230_positive_closure_completion_audit.py
# SUMMARY: PASS=79 FAIL=0
python3 scripts/frontier_yt_pr230_campaign_status_certificate.py
# SUMMARY: PASS=427 FAIL=0
python3 scripts/frontier_yt_pr230_assumption_import_stress.py
# SUMMARY: PASS=111 FAIL=0
bash docs/audit/scripts/run_pipeline.sh
# PASS with 5 existing warnings
python3 docs/audit/scripts/audit_lint.py --strict
# PASS with 5 existing warnings
git diff --check
# PASS
```

No closure statement: this block does not claim retained or
`proposed_retained` closure.  PR230 remains open/draft.  The cleanest next
physics artifact is still accepted same-surface `O_H`/action plus strict
`C_ss/C_sH/C_HH` pole rows, or a genuine W/Z response packet, strict
Schur/scalar-LSZ pole authority, or neutral H3/H4 primitive-transfer authority.
