# Goal

Repair the audited-conditional row
`g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19` by locking the
actual-surface scope to the residue-normalization obstruction plus conditional
map, not an unconditional `g_bare=1` theorem.

Audit blocker:

```text
missing_bridge_theorem: derive and audit the complete same-projected 1PI exhaustion theorem showing that the H_unit tree-level matrix element exhausts the full scalar-singlet 1PI residue for arbitrary g_bare on Q_L.
```

This branch does not add that theorem. It makes the missing theorem explicit
and prevents downstream rows from citing the conditional map as an actual
surface pinning result.
