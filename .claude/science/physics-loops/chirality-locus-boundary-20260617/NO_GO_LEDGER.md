# No-Go Ledger

## Complement-neutral triplet selection

Claim tested: a `C_3`-invariant, complement-even selector on the corner cube can
choose exactly the `hw=1` triplet.

Result: false. Exhaustive enumeration shows the only `C_3`-invariant,
complement-even projectors are:

- empty;
- `L_0 union L_3`;
- `L_1 union L_2`;
- all corners.

There is no complement-even three-corner projector. A selector for `hw=1` over
`hw=2` is necessarily complement-odd.

## Not a global chirality no-go

This does not rule out a future theorem that supplies a complement-odd
orientation bit. It only prunes the route where complement-neutral corner data
was supposed to select the physical triplet.
