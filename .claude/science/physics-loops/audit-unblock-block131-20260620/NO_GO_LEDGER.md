# No-Go Ledger

## Do Not Delete Repo-Referenced Caches

Observation: `logs/runner-cache/chsh_structural_bound_narrow_2026_05_17.txt`
has no live runner in the cleanup candidate set, but it is still cited by
`docs/CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`.

Result: runner-orphan cleanup can create broken evidence links unless it also
checks repository references.

Status: blocked by this PR's referenced-cache preservation rule.

## Do Not Resolve The CHSH Evidence Boundary Here

Whether the CHSH note should keep a historical cache, migrate to another
runner, or be demoted is out of scope for this tooling PR.
