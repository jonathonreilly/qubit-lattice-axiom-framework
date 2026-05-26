# Review History

## Local science review

Finding: the prior note already named the H_unit-residue admission, but the
proof body still contained unconditional language:

- "Therefore the scalar-singlet coefficient identity holds..."
- "Representation B is valid..."
- "Why the equality is mathematically unavoidable"
- "This proves the theorem"

Resolution: the branch rewrites those claims as conditional on the
H_unit-residue admission and explicitly says the missing same-projected 1PI
exhaustion bridge is not derived.

## Verification

Completed:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/vocab_lint.py --report-only docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md .claude/science/physics-loops/g-bare-1pi-pinning-conditional-firewall
python3 scripts/render_controlled_vocabulary.py --check
python3 docs/audit/scripts/repair_missing_dependency_edges.py
git diff --check
```

Result: all passed. Strict audit lint reported existing notices only and no
errors. `repair_missing_dependency_edges.py` found zero candidate rows.
