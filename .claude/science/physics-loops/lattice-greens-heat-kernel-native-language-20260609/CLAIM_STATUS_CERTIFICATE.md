# Claim Status Certificate

## Claim

`lattice_greens_1_over_r_from_heat_kernel_resolvent_theorem_note_2026-06-07`

## Actual Current-Surface Status

`exact-support`

The row now records exact support for the leading Green-kernel term via the
stronger framework-native lattice-correction theorem for the same exact
heat-kernel/Bessel resolvent.

## Imports Retired Or Exposed

- Retired from this row's load-bearing path: stale wording that called the
  leading asymptotic an `accepted-premise textbook import`.
- Preserved as non-load-bearing references: Maradudin/Lawler/Spitzer and
  standard Bessel/Gaussian asymptotics for the alternate local-CLT route and
  runner sanity checks.
- Still open: a direct uniform local-CLT/tail-domination proof from the
  heat-kernel integral.

## Firewalls

- `proposal_allowed`: true for exact support of the leading term.
- `bare_retained_allowed`: false.
- `audit_required_before_effective_retained`: true.
- `audit_results_modified`: false.

## Verification

```text
python3 scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
TOTAL: PASS=20 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
python3 -m py_compile scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
git diff --check
git diff --name-only -- docs/audit
```
