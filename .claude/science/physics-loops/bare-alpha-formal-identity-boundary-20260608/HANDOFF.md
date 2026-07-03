# Handoff

## Summary

This PR repairs
`framework_bare_alpha_ratio_assumed_input_identity_support_note_2026-04-30`
by recasting it as a bounded formal assumed-input identity theorem.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3266

The theorem proves:

```text
H1-H4 => alpha_3(bare)/alpha_em(bare) = 2d+3
H1-H4 => sin^2(theta_W)(bare) = (d+1)/(2d+3)
```

At `d=3`, these are `9` and `4/9`.

## Reviewer Notes

- No `docs/audit/**` files were changed.
- No new axiom is introduced.
- This row does not derive the physical EW-normalization hypotheses H2-H4.
- Do not extract this as a retained physical coupling theorem. Extract only the
  bounded formal identity if it passes review.

## Verification

```text
python3 scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py
TOTAL: PASS=44, FAIL=0

python3 scripts/precompute_audit_runners.py --runners scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py --force --allow-non-main
ok 1

git diff -- docs/audit --stat
<no output>
```
