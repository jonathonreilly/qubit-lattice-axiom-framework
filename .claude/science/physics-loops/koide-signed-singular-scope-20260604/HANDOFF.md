# Handoff

## Summary

This branch repairs the overbroad one-negative inequality in the signed-eigenvalue
versus singular-value Koide readout note.

The corrected general statement is:

```text
Q(V) < Q(S) = (1 + 2r)/3
```

The stronger `Q(V)<2/3` statement is only claimed at `r=1/2`.

The runner adds the requested non-`r=1/2` regression:

```text
r=51/100, theta=46/25, one eigenvalue negative,
Q(V)=0.67114370 > 2/3 but Q(V)<Q(S)=0.67333333.
```

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_signed_vs_singular_value_readout_narrow.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_koide_signed_vs_singular_value_readout_narrow.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_signed_vs_singular_value_readout_narrow.py
python3 -m py_compile scripts/frontier_koide_signed_vs_singular_value_readout_narrow.py
git diff --check
```

Expected summary:

```text
PASS=30 FAIL=0
```

## Remaining Open Gates

- Independent audit must re-audit the same row.
- The physical `r=1/2` selector remains separate.
- Charged-lepton operator identification remains separate.
