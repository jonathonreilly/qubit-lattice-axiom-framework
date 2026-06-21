# Quark Route-2 Readout Inverse-Square Gate No-Go

**Date:** 2026-06-21
**Actual current-surface status:** bounded current-bank no-go for readout-only inverse-square coefficient shortcut
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_readout_inverse_square_gate_no_go_2026_06_21.py`

Actual current-surface status: bounded current-bank no-go for readout-only inverse-square coefficient shortcut.

## Scope

This block continues the S3/Route-2 endpoint campaign after the source-map
route narrowed to a missing source-excess theorem. It checks the alternate
route:

```text
readout-only inverse-square coefficient theorem.
```

This is not an audit verdict and does not resolve the parent gate
`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`. It asks whether the current named
readout/Schur/registration bank already promotes the exact inverse-square
Schur value to a readout-row coefficient law.

## Exact Algebra

The Schur weights are:

```text
w_E = 1/3
w_T = 1/2.
```

The current bank already contains the exact structural value:

```text
(w_E/w_T)^-2 = 9/4.
```

If this value were supplied as a readout coefficient law, then with the T-side
candidate `rho_T = beta_T/alpha_T = -1`:

```text
q_T = 1 + rho_T/6 = 5/6
q_E = q_T (w_E/w_T)^-2 = (5/6)(9/4) = 15/8
rho_E = beta_E/alpha_E = 6(q_E - 1) = 21/4
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So the readout-only inverse-square route is algebraically sharp. The missing
step is not the arithmetic; it is the coefficient theorem:

```text
inverse_square_value_9_4 -> readout_coefficient_law_p2.
```

## Current-Bank Gap

The current bank supplies:

- exact restricted readout family `P(rho_E)`;
- exact endpoint algebra;
- Schur projector weights and the exact `9/4` value;
- a quadratic-invariant no-go showing the E:T reduced matrix element remains
  free;
- registration, partial-isometry, idempotency, and positivity no-gos showing
  `rho_E` remains a direction or one-sided bound;
- factor rigidity showing that the one-parameter `P(rho_E)` family remains
  arbitrary in the spatial prefactor.

The current bank supplies the value `9/4` but not the coefficient bridge. In
particular:

```text
exact_readout_family -> rho_E_free_parameter
schur_projector_weights -> inverse_square_value_9_4
quadratic_invariants -> rho_E_free_parameter
registration_conditions -> rho_E_free_parameter
positivity_conditions -> rho_E_lower_bound
factor_rigidity -> rho_E_free_parameter
```

There is no current typed edge:

```text
inverse_square_value_9_4 -> readout_coefficient_law_p2.
```

Adding that missing edge would immediately create the path to
`rho_E=21/4`. Without it, the current readout-only route remains open.

## Boundary

The pruned shortcut is:

```text
current readout/Schur/registration bank
  => readout-only inverse-square coefficient theorem
  => rho_E = 21/4.
```

The first implication is not present. This block does not rule out a future
readout-only theorem. It says the current named bank does not already contain
that coefficient law.

## Fan-Out Synthesis

| Frame | Result |
|---|---|
| Exact readout reduction | `P(rho_E)` remains a one-parameter family. |
| Schur value | `9/4` is present as `(w_E/w_T)^-2`. |
| Quadratic invariants | E:T reduced-matrix-element ratio remains free. |
| Registration/idempotency | Fixes row norm, not direction. |
| Positivity | Gives only `rho_E > -6`. |
| Factor rigidity | Localizes readout ambiguity but does not select `rho_E`. |

All frames agree: the current bank contains the target value as a structural
number, but not the readout coefficient theorem that would make it load-bearing.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_readout_inverse_square_gate_no_go_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=61, FAIL=0
```
