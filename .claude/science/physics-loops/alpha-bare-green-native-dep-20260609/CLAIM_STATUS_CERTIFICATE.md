# Claim Status Certificate

## Current Claim Surface

Actual current-surface status:

```text
exact-support
```

This PR does not mark the alpha-bare parent retained and does not edit audit
results.

## Repaired

- Replaces the Maradudin accepted-premise Green coefficient dependency with the
  framework-local `Z^3` Green-kernel theorem.
- Keeps BZ, I1, I2, and I3 dependency boundaries unchanged.
- Updates the runner source firewall and verdict text to require the
  framework-local Green theorem and certificate runner.
- Refreshes the runner cache to `TOTAL: PASS=40 FAIL=0`.

## Still Open

- Independent audit must decide whether this dependency repair changes the
  alpha-bare parent row's effective status.
- I1, I2, and I3 remain separate dependencies.
