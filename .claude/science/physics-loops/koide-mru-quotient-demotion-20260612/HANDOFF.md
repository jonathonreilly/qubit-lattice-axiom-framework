# Handoff

This branch repairs the Koide MRU weight-class obstruction source.

Science result:

- preserve the exact unreduced determinant obstruction: weights `(1,2)` land at
  `kappa = 1`;
- preserve the exact two-slot quotient algebra: if the scalar lane is supplied
  as an `SO(2)` quotient, the reduced carrier is equal weight and lands at
  `kappa = 2`;
- remove the claim that this note derives the physical quotient;
- expose the missing bridge as the scalar-lane `SO(2)` quotient or equivalent
  `cos(3 arg b)` decoupling theorem.

Verification:

```text
PYTHONPATH=scripts python3 scripts/frontier_koide_mru_weight_class_obstruction_theorem.py
# classified_pass=31 fail=0

python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_mru_weight_class_obstruction_theorem.py --allow-non-main
# ok 1, nonzero_exit 0
```

No audit ledger/result files were edited.
