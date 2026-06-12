# Handoff

This PR repairs the source-side reason the archived bare-alpha row failed:
the old wrapper now points at the canonical live formal assumed-input identity
note and is checked as non-authority conditional algebra only.

Reviewer focus:

- The archived wrapper should remain a historical handoff, not a live theorem.
- The live canonical note should remain the source of the narrowed algebraic
  result.
- No ledger row should be retagged by this PR.
- If accepted, the row can be handed to independent audit as a narrowed,
  auditable source packet rather than an electroweak-normalization claim.

Verification:

```text
python3 scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py
TOTAL: PASS=56, FAIL=0
VERDICT: FORMAL ASSUMED-INPUT IDENTITY THEOREM VERIFIED

python3 scripts/precompute_audit_runners.py --runners scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py --allow-non-main
ok 1, nonzero_exit 0
```
