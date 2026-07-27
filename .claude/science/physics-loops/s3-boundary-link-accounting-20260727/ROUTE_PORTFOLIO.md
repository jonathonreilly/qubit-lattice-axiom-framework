# Route Portfolio

## Prior-art sweep

Searched landed commit `f7d78df6455d41cf50c143e41c81f204d3dec72e` with statement-level
queries in both noun orders for octahedral closures, connected Q_3 sides,
simplicial closures, PL 2-disks, and both runner-accounting decompositions.
The exact commands included:

```text
git grep -n -iE "(octahedral.*both.*connected|both.*connected.*octahedral|simplicial closure.*PL 2-disk|PL 2-disk.*simplicial closure)" origin/main -- 'docs/*.md'
git grep -n -iE "(119 EXACT.*2 BOUNDED|2 BOUNDED.*119 EXACT|120 EXACT.*1 BOUNDED|1 BOUNDED.*120 EXACT)" origin/main -- 'docs/*.md' 'logs/runner-cache/*.txt'
```

Matched hits:

- `docs/S3_BOUNDARY_LINK_THEOREM_NOTE.md` already contained the corrected
  parenthetical `119 EXACT, 2 BOUNDED` from commit `2ef33f4276`.
- `docs/audit/MISSING_DERIVATION_PROMPTS.md` still quoted the older packet's
  `120 EXACT, 1 BOUNDED` blocker.
- `docs/S3_ALL_R_BOUNDARY_LINK_DISK_THEOREM_NOTE_2026-05-30.md` is a stronger
  all-R candidate, but its audit row is `unaudited`; it is not authority for
  broadening this repair.

Classification: the science result is already present on matching premises;
this cycle is a source/packet synchronization repair, not novel physics.

## Artifact routes

| Route | Directness | Risk | Decision |
|---|---:|---:|---|
| Make the breakdown self-contained, name both bounded rows, and render a fresh packet | high | low | selected |
| Change runner classifications to reproduce `120 + 1` | false | high | rejected; contradicts completed evidence |
| Edit the audit ledger or effective-status tables | false | high | forbidden; audit-lane authority |
| Import the stronger all-R candidate | low for this blocker | high | rejected; changes scope and depends on an unaudited row |
| Add another scientific verification runner | low | medium | rejected as duplicate/churn; the primary runner already emits decisive evidence |
