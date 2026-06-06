# Goal

Repair the `flavor_kreal_instrument_two_letter_phase_orthogonal_2026-06-02`
conditional row by separating the finite K-real algebra from the missing
physical readout/instrument theorem.

The branch should preserve the useful finite result:

```text
K-real readout supplied -> K-even alphabet span{I, C + C^2}
K-odd phase             -> orthogonal phase channel i(C - C^2)
```

It should also state the no-go boundary:

```text
baseline Record alone -> no supplied instrument, no two-letter measure selector
```

The intended audit effect is honest route pruning and source-side scope repair,
not a direct positive status change by this branch.
