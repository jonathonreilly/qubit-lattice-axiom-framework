# No-Go Ledger

## Unconditional Sign Propagation

The old wording effectively implied:

```text
delta < 0 => K_C3 < 0
```

without a denominator branch. The exact formula

```text
K_C3 = t^2 delta / (eps_gap (eps_gap + delta))
```

shows this implication fails when `eps_gap + delta < 0`. The branch must be
stated.

## Magnitude As Flavor Value

The mediator sign and kernel normalization do not pin `|delta|` or a flavor
value. That remains an IR/gap problem.
