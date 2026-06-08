## Handoff

This branch repairs the conditional audit blocker for the Dirac/Lorentz
diagnostic packet. The audit objection was not to the algebraic conclusion but
to the certificate: the runner used the wrong Gaussian quadrature weight for
the displayed norm ratios.

## Change

- `hermegauss` was replaced with `hermgauss`, matching the squared Gaussian
  norm weight after `x=sqrt(a) zeta`.
- The runner now asserts an analytic lower bound for `||(mass cosh zeta)^n
  psi||/n!`, showing superfactorial growth independent of the quadrature table.
- The note states the corrected certificate and preserves open-gate scope.

## Verification

```bash
python3 scripts/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.py
python3 -m py_compile scripts/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.py
git diff --name-only -- docs/audit
git diff --check
```

Expected result: `TOTAL: 5 PASS / 0 FAIL` and no `docs/audit` edits.

