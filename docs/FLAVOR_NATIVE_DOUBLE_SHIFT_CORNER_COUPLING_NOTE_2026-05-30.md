# Flavor Native Double-Shift Corner Coupling (Bounded Support)

**Date:** 2026-05-30
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not quote, set, or predict audit outcomes.
**Primary runner:** [`scripts/flavor_native_double_shift_corner_coupling_2026_05_30.py`](../scripts/flavor_native_double_shift_corner_coupling_2026_05_30.py)

## 0. Scope

This note records a finite corner-cube calculation on the three Hamming-weight-1
generation labels inside `(Z_2)^3`. It corrects the local operator language for
the symmetric off-diagonal generation coupling.

Let `S_mu` flip bit `mu` on the eight cube corners, and let `P` project onto the
Hamming-weight-1 triplet. Then:

```text
P S_mu P^T = 0,
P (S_y S_z + S_z S_x + S_x S_y) P^T = J - I.
```

So a single bit flip is not a within-triplet operator. The symmetric
within-triplet off-diagonal coupling is instead the sum of double shifts, which
projects to `J-I`.

## 1. Consequence for the Symmetric Two-Parameter Form

For

```text
Y = a I + b (J - I),
```

the square-root spectrum is

```text
{a + 2b, a - b, a - b}.
```

When the entries are read as positive square-root masses, the Koide ratio is

```text
Q = (sum_i y_i^2) / (sum_i y_i)^2
  = (3 a^2 + 6 b^2) / (9 a^2)
  = 1/3 + (2/3) (b/a)^2.
```

Thus `Q=2/3` is equivalent, inside this symmetric two-parameter form, to
`(b/a)^2 = 1/2`. This note does not derive that coefficient ratio; it only
identifies the finite native operator shape whose coefficient would be `b`.

## 2. What This Claims

- A single cube bit flip projects to zero on the Hamming-weight-1 triplet.
- The symmetric sum of double bit flips projects exactly to `J-I`.
- In the symmetric form `aI + b(J-I)`, the Koide ratio depends only on
  `(b/a)^2` as `Q = 1/3 + (2/3)(b/a)^2`.

## 3. What This Does Not Claim

- It does not derive `b/a = 1/sqrt(2)`.
- It does not derive three distinct charged-lepton masses.
- It does not select a chiral/oriented complex splitting.
- It does not claim an observed-mass match, a fitted value, or a new axiom.

## 4. Runner

```bash
python3 scripts/flavor_native_double_shift_corner_coupling_2026_05_30.py
```

Expected result: `SCORECARD PASS=4 FAIL=0`.
