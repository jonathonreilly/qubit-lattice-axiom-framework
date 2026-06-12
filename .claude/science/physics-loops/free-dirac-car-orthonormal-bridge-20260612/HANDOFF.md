# Free Dirac CAR Orthonormal Bridge Handoff

## Target

`free_dirac_car_positive_energy_equal_time_anticommutator_support_bounded_note_2026-06-08`

Prior audit blocker:

```text
add and check explicit bridge from cited 2E-normalized Dirac spinors to orthonormal eigenspinor projector identity, or include required 1/(2E) field-expansion factor before claiming I4 equal-time matrix.
```

## Repair Summary

The note now states that the live calculation uses orthonormal Hamiltonian
eigenspinors from the finite Hermitian Dirac Hamiltonian, not covariant
`2E`-normalized spin sums. It records that a covariant-spinor route would need
the compensating `1/(2E)` field-expansion weight.

The runner adds checks that the eigenspinor columns are orthonormal, that the
positive/negative projectors are orthogonal and idempotent, and that the source
note declares the normalization bridge.

## Verification

```text
python3 scripts/frontier_free_dirac_car_positive_energy_equal_time_support.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_free_dirac_car_positive_energy_equal_time_support.py --force --concurrency 1 --push-mode none --allow-non-main
git diff --check
git diff --name-only -- docs/audit/data
```

No audit-ledger files should be changed by this PR.
