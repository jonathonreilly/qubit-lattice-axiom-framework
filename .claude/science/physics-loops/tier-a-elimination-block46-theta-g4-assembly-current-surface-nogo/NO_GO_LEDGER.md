# No-Go Ledger

| Route | Verdict | Reason |
|---|---|---|
| Paired-shift covariance | no-go for value selection | Preserves `theta_bar`; does not set it to zero. |
| Balanced fixed grading | no-go for retirement | `n = 0`, so transfer is trivial. |
| Synthetic nonzero grading | support only | Shows cancellation mechanism but is not a supplied physical theta surface. |
| G1 carrier/defect gates | prerequisite open | Current surface does not supply physical 4D carrier or defect closure/suppression. |
| G3 phase insertion | prerequisite open | Current surface does not supply phase source, coefficient, or physical registration. |
| Mass determinant bridge | prerequisite open | W2 physical registrability and action-level determinant entry remain open. |
| Owner governance | governance, not derivation | Not imported in this block. |

## Exact Witness

The runner verifies:

```text
theta_gauge' = theta_gauge - n alpha
argdet'      = argdet + n alpha
theta_bar'  = theta_bar
```

The expression still depends on the initial gauge and mass values. Zero
requires the relation `argdet = -theta_gauge`; invariance alone does not
derive that relation.
