# Review History

Verification run locally:

```bash
python3 scripts/probe_kawamoto_smit_phase_forcing.py
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/probe_kawamoto_smit_phase_forcing.py --force --push-mode none --allow-non-main
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/probe_kawamoto_smit_phase_forcing.py --check-only --allow-non-main
python3 docs/audit/scripts/build_citation_graph.py
jq '.nodes["staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07"].deps' docs/audit/data/citation_graph.json
git restore docs/audit/data/citation_graph.json
git diff --check
```

Results:

- runner: `TOTAL: PASS=47 FAIL=0`;
- cache freshness check: all relevant caches fresh;
- regenerated source graph deps for this row:
  `axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29`,
  `fermion_parity_z2_grading_theorem_note_2026-05-02`;
- generated audit graph was restored and is not committed.
