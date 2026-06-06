# Handoff

## Summary

This PR repairs the new conditional row
`lsp_projective_canonical_kp_equals_p_narrow_theorem_note_2026-06-05`.

Audit accepted the canonical/sufficiency algebra but found the necessity clause
too broad in zero-projector edge cases. The source note now says displayed
physical outcome labels satisfy `P_r != 0`; formal zero-effect labels are
bookkeeping-only. If kept, the necessity claim applies only to rows mixing into
distinct nonzero sectors.

## Files

- `docs/LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md`
- `scripts/audit_companion_lsp_projective_canonical_kp_equals_p_2026_06_05.py`
- `logs/runner-cache/audit_companion_lsp_projective_canonical_kp_equals_p_2026_06_05.txt`

## Verification

```text
python3 scripts/audit_companion_lsp_projective_canonical_kp_equals_p_2026_06_05.py
TOTAL: 53 PASS / 0 FAIL
```

```text
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_lsp_projective_canonical_kp_equals_p_2026_06_05.py --check-only --allow-non-main
All relevant caches are fresh.
```

## Boundaries

- No new axioms.
- No audit ledger/result edits.
- No measurement axiom, Born rule, physical instrument-selection rule, or
  instrument-uniqueness theorem is claimed.
- Effective status still requires independent audit.
