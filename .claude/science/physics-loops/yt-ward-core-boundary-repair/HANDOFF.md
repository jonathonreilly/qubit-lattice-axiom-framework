# Handoff

## Summary

This block repairs `yt_ward_identity_derivation_theorem` after the latest
audit batch changed the YT dependency surface. The broad source note used to
bundle three different claims:

- exact `H_unit` scalar-singlet matrix-element algebra;
- a physical top-Yukawa readout identification;
- a shared tadpole transport statement giving `y_t(M_Pl)/g_s(M_Pl)`.

Only the first item is retained in the auditable core of this PR.

## Expected Pipeline Impact

The repaired citation graph should leave the row with one one-hop dependency:

```yaml
deps:
  - native_gauge_closure_note
ready: true
audit_queue_rank: 1
```

The removed one-hop dependencies are:

- `left_handed_charge_matching_note`
- `yukawa_color_projection_theorem`
- `yt_ew_color_projection_theorem`
- `yt_vertex_power_derivation`

After `bash docs/audit/scripts/run_pipeline.sh`, the row is:

```yaml
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
criticality: critical
transitive_descendants: 960
ready: true
```

The row remains unaudited until the independent audit lane reviews it. This PR
does not apply an audit verdict and does not retag the ledger by hand.

## Verification

Completed before packaging:

```bash
python3 -m py_compile scripts/frontier_yt_ward_identity_derivation.py
python3 scripts/frontier_yt_ward_identity_derivation.py
```

Runner result:

```text
PASS: 44
FAIL: 0
```

Additional verification completed:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md scripts/frontier_yt_ward_identity_derivation.py .claude/science/physics-loops/yt-ward-core-boundary-repair
```

Strict lint returned OK with one pre-existing warning and legacy notices not
introduced by this branch.
