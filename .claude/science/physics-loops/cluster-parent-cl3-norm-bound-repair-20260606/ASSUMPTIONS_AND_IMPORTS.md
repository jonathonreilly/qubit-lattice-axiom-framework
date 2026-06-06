# Assumptions And Imports

## Load-Bearing Premises

- The 8 canonical Cl(3) monomials act with operator norm 1 on the minimal
  complex spinor module.
- Operator norm obeys the triangle inequality.
- The finite local-rule hypothesis bounds how many local terms can touch a
  site.

## Forbidden Inputs Not Used

- No new axiom.
- No external theorem import.
- No observed target value or fitted selector.
- No audit verdict edit.
- No unconditional L2 spatial clustering claim.

## Repair

The old bound `||sum c_alpha gamma^alpha|| <= ||c||_2` is removed. The repaired
bound is:

```text
||sum c_alpha gamma^alpha|| <= sum |c_alpha| <= sqrt(8) ||c||_2.
```
