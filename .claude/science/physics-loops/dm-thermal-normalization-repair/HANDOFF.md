# Handoff

PR: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1941

This block repairs `dm_thermal_average_sommerfeld_textbook_import_note_2026-05-17`
by narrowing it to a runner-backed normalization packet.

Generated audit state after the pipeline:

```text
audit_status=unaudited
effective_status=unaudited
claim_type=bounded_theorem
ready=true
open_dependency_paths=[]
```

Runner checks:

- MB denominator equals `sqrt(pi)/(4 a^(3/2))`.
- `<1/v> = 2 sqrt(a)/sqrt(pi) = 5/sqrt(pi)` at `x_f=25`.
- `<1/v^2> = 2a = 25/2` at `x_f=25`.
- `alpha_eff/v = alpha_eff sqrt(a/t)` under `t=a v^2`.
- `1/Gamma(3/2) = 2/sqrt(pi)`.

Reviewer focus:

- Confirm `x_f=25` is an explicit benchmark, not a derived result.
- Confirm context references are not load-bearing.
- Confirm the row is ready for independent re-audit.
