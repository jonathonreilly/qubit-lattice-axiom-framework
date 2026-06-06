# Handoff

Target:
`luders_rule_from_composition_consistency_note_2026-05-20`.

What changed:

- Rewired the parent note to use the native finite operator-algebra
  PEP/trace bridge.
- Added the explicit positive-probability domain:
  `Tr(P sigma P)>0` and `Tr(K sigma K†)>0`.
- Added the missing cache for
  `scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py`.
- Added cache links to the bridge note.

Boundary:

- No audit ledger/status edits.
- No new axioms.
- No Born-chain promotion; broader Born dependencies remain separate.

Suggested reviewer check:

Confirm that the parent note's new markdown links create the intended
dependency surface and that the cache is fresh under `precompute_audit_runners`.
