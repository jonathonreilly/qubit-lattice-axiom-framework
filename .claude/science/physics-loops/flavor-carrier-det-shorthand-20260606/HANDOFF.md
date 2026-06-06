This PR repairs the formula-inventory blocker on
`docs/FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md`.

The previous text used a false shorthand:

```text
1/(omega^k-1) = det(1-g)^-1
```

The repaired note and runner state and verify the actual determinant inverse:

```text
det(1-g^k | N)^-1 = 1 / ((omega^k - 1)(omega^(2k) - 1)).
```

Scope boundary for review:

- This closes the formula-inventory repair item.
- It does not derive the physical charged-lepton carrier.
- It does not derive `r=1/2`.
- It does not update `docs/audit/**` or any ledger status.
