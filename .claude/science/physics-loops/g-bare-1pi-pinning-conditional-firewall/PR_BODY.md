# Summary

This PR repairs `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` by
adding a conditional-use firewall around the same-1PI Path-2 pinning step.

The branch does not introduce a new axiom, does not assign an audit verdict,
and does not claim retained status. It makes the current status explicit:
bounded/conditional support, with off-surface `g_bare = 1` available only under
the H_unit-residue exhaustion admission.

# Science Boundary

- Actual current-surface status: `bounded-support / conditional-support`
- Conditional surface: off-surface `g_bare = 1` if H_unit-residue exhaustion is accepted
- Proposal allowed: `false`
- Bare retained allowed: `false`
- Independent audit required before any retained/effective-retained treatment

# Pipeline Result

`bash docs/audit/scripts/run_pipeline.sh` resets the row to:

```yaml
audit_status: unaudited
effective_status: unaudited
ready: true
criticality: critical
load_bearing_score: 13.83
open_dependency_paths: []
```

# Handoff

Loop pack:
`.claude/science/physics-loops/g-bare-1pi-pinning-conditional-firewall/HANDOFF.md`

# Verification

Completed:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/vocab_lint.py --report-only docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md .claude/science/physics-loops/g-bare-1pi-pinning-conditional-firewall
python3 scripts/render_controlled_vocabulary.py --check
python3 docs/audit/scripts/repair_missing_dependency_edges.py
git diff --check
```

Strict audit lint passed with existing notices only; dependency-edge repair
found zero candidate rows.
