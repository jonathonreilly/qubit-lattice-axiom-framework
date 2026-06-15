# Claim Status Certificate

## Claim

On `Herm_circ(3)`, the block-total Frobenius slots
`E_+ = ||pi_+(H)||_F^2` and `E_perp = ||pi_perp(H)||_F^2` give a
framework-native 1:1 algebraic candidate for the MRU scalar carrier. If the
scalar lane is carried by `log E_+ + log E_perp`, the equal-weight extremum at
fixed `E_+ + E_perp` gives `kappa = 2`.

## Status

Bounded algebraic support, not unbounded physical closure.

## What Is Proved Here

- The symbolic block-total formulas `E_+ = 3 a^2` and
  `E_perp = 6 |b|^2`.
- The equal-weight extremum implies `E_+ = E_perp`, equivalently
  `kappa = 2`, when the block-total law is stipulated.
- `Herm_circ(d)` has multiplicities
  `(1, floor((d - 1) / 2), 1 if d is even else 0)`, so `d = 3` is the unique
  finite dimension in the scanned family with exactly one trivial irrep and one
  doublet irrep and no sign slot.

## What Is Not Claimed

- This PR does not derive the scalar-lane `SO(2)` quotient.
- This PR does not prove the block-total law is the canonical physical scalar
  measure.
- This PR does not apply or change audit ledger verdicts.
