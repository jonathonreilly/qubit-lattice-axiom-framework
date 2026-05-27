# Handoff

## Summary

This PR repairs `field_equation_derivation_note` by narrowing it to the exact
Euler-Lagrange identity for the displayed quadratic graph action.

## Claim Movement

- Before: the row suggested the screened Poisson equation was not merely chosen
  and was uniquely lowest-order within a restricted class.
- After: the row says only that the supplied action varies to
  `(L+mu^2 I)Phi = G_c rho`.
- Remaining: deriving or selecting the action, mass term, and source coupling
  remains open.

## Verification

- `python3 scripts/frontier_field_equation_variational_scope_repair.py`
- `python3 scripts/vocab_lint.py --report-only docs/FIELD_EQUATION_DERIVATION_NOTE.md .claude/science/physics-loops/field-equation-variational-scope-repair-20260527/*.md`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`

## Next Action

Open as a draft PR. If review accepts the scope repair, independent audit can
re-audit the row as bounded variational support.
