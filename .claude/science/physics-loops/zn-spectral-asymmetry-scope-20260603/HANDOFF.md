# Handoff

## Summary

This branch repairs the conditional scope defect on the finite `Z_N`
spectral-asymmetry note. The old statement said nonzero weights make the local
weight-sum finite. That is only true for prime `N`; for composite `N`, a
nonzero nonunit weight can make `zeta_N^(k a)-1` vanish.

The repair adds the exact admissible/unit-weight condition:

```text
gcd(a_j, N) = 1 for every local weight a_j.
```

The load-bearing `N=3` `(1,2)` calculation is unchanged, since both nonzero
weights modulo 3 are units.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py
python3 -m py_compile scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py
git diff --check
```

Expected runner summary: `PASS=33 FAIL=0`.
