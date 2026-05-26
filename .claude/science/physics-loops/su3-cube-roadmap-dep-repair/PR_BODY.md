# Summary

Repairs the remaining audit blocker for
`su3_cube_perron_solve_combined_theorem_note_2026-05-03`.

The latest audit did not reject the narrowed PBC/trivial-sector science;
it flagged the non-retained roadmap as a cited authority. This branch:

- removes the roadmap markdown citation and YAML dependency;
- keeps the theorem bounded to PBC geometry, bipartite adjacency, and
  trivial-sector Reference B recovery;
- keeps non-trivial cube rho/intertwiner traces explicitly out of scope;
- refreshes runner output.

# Verification

```bash
python3 -m py_compile scripts/frontier_su3_cube_perron_solve.py
python3 scripts/frontier_su3_cube_perron_solve.py
python3 docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/SU3_CUBE_PERRON_SOLVE_COMBINED_THEOREM_NOTE_2026-05-03.md scripts/frontier_su3_cube_perron_solve.py .claude/science/physics-loops/su3-cube-roadmap-dep-repair
git diff --check
```

# Post-Pipeline Queue State

The repaired row is `unaudited` / `awaiting_audit`, ready in the audit
queue, high criticality, and has `criticality_rank: 2`. No audit verdict
is applied by this branch.

# Status Boundary

This is bounded support only. It does not claim a full cube Perron value,
`P_cube(6) >= P_trivial(6)`, or any audit-ratified retained status.
