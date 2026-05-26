# Summary

This PR repairs `koide_q_delta_linking_relation_theorem_note_2026-04-20` by
narrowing it to the exact conditional implication
`I1 ∧ P => delta = Q/d`.

It does not introduce a new axiom, does not assign an audit verdict, and does
not claim retained status. It removes overstrong retained-authority wording
around source/context rows and updates the runner text to match the
conditional surface.

# Science Boundary

- Actual current-surface status: `conditional-support`
- Conditional surface: `I1 and P imply delta = Q/d`
- Proposal allowed: `false`
- Bare retained allowed: `false`
- Independent audit required before any retained/effective-retained treatment

# Pipeline Result

`bash docs/audit/scripts/run_pipeline.sh` resets the row to:

```yaml
audit_status: unaudited
effective_status: unaudited
ready: true
criticality: high
load_bearing_score: 12.288
open_dependency_paths: []
```

# Verification

Completed:

```bash
python3 scripts/frontier_koide_q_delta_linking_relation.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_q_delta_linking_relation.py --allow-non-main
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/vocab_lint.py --report-only docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md .claude/science/physics-loops/koide-q-delta-conditional-firewall
python3 scripts/render_controlled_vocabulary.py --check
python3 docs/audit/scripts/repair_missing_dependency_edges.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_q_delta_linking_relation.py --allow-non-main --check-only
git diff --check
```

Strict audit lint passed with existing notices only; runner cache check reports
the target runner fresh.
