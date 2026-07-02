# Quark Route-2 Positive-Diagonal E-Center Selector No-Go Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go / negative route pruning
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_positive_diagonal_e_center_selector_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_positive_diagonal_e_center_selector_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_positive_diagonal_e_center_selector_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_positive_diagonal_e_center_selector_no_go_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md), [OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md](OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md), [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md), [S3_TIME_PRIMITIVE_CHAIN_NOTE.md](S3_TIME_PRIMITIVE_CHAIN_NOTE.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)

## Question

The Route-2 E row has the positive two-endpoint form

```text
gamma_E(shell)  = alpha_E,
gamma_E(center) = alpha_E (1 + rho_E / 6),
q_E             = gamma_E(center) / gamma_E(shell).
```

The standing positivity note already proves that positivity gives only the
one-sided bound `rho_E > -6`. This block asks a stronger E-center-sensitive
question:

> Can the finite positive-diagonal / Record-additive readout classifier select
> the value `q_E = 15/8`, equivalently `rho_E = 21/4`, once it is applied
> directly to the positive diagonal pair
> `(gamma_E(shell), gamma_E(center))`?

The answer is no. The classifier can turn the pair into additive readout
families, determinant/log quotients, or scale-normalized functions of `q_E`.
Those constructions see the E-center. They still do not select a value of
`q_E`.

## Minimal Premises

Allowed:

- exact Route-2 restricted E-row endpoint algebra;
- positivity domain `q_E > 0`, equivalently `rho_E > -6`;
- the positive-diagonal readout classifier's exact statement that continuous
  direct-sum additive readouts are one-site sums;
- the classifier's determinant-only quotient result, which selects the
  logarithmic quotient after a positive diagonal readout family is supplied;
- exact rational arithmetic.

Forbidden proof inputs:

- observed quark masses;
- fitted endpoint values;
- nearest-rational selection from the live `N=15` calibration;
- bulk-limit promotion of the measured calibration;
- hidden declaration that `log(q_E)` or `q_E` must equal its target value.

## E-Center-Sensitive But Value-Blind

Normalize the positive E row by its shell scale:

```text
(gamma_E(shell), gamma_E(center)) / gamma_E(shell) = (1, q_E).
```

The positive-diagonal classifier says that a supplied continuous additive
readout family has the form

```text
W(1, q_E) = phi(1) + phi(q_E).
```

The determinant-only quotient narrows this to the logarithmic family:

```text
W_det(1, q_E) = c log(q_E).
```

Both formulas are E-center-sensitive. They distinguish `q_E=1`,
`q_E=5/6`, and `q_E=15/8`. But neither formula supplies an equation that
forces `q_E=15/8`.

For example, all of the following are positive and classifier-admissible:

```text
rho_E = 0      -> q_E = 1
rho_E = -1     -> q_E = 5/6
rho_E = 21/4   -> q_E = 15/8
rho_E = 1      -> q_E = 7/6
rho_E = 4      -> q_E = 5/3
```

The classifier turns each of these into a valid additive positive-diagonal
readout value. It does not prefer the target member.

## What This Prunes

This prunes the route

```text
Record-style finite scalar additivity
  + positive diagonal E endpoint pair
  + determinant/log quotient classifier
  => q_E = 15/8.
```

The route fails because additivity and determinant-only quotienting classify
the allowed functional shape; they do not supply the missing E-center selector
equation.

## What Remains Open

A positive Route-2 endpoint theorem still needs a same-surface ingredient that
does one of the following:

- derives `q_E = 15/8`;
- derives `rho_E = 21/4`;
- derives the equivalent center ratio `c_TE = -8/9` under the T-side
  candidates;
- supplies an explicit accepted readout-row selector for the E-channel
  direction.

This note does not rule out those future routes. It only says that the
positive-diagonal / Record-additive classifier alone is not that selector.

## What Is Not Claimed

- No derivation of `rho_E = 21/4`.
- No derivation of `q_E = 15/8`.
- No derivation of the endpoint triple `(-1, -2, 21/4)`.
- No unique exact `Theta_R -> Lambda_R` coupling theorem.
- No audit verdict or ledger/status change.
- No all-routes no-go against future fixed-carrier E-center primitives.

## Load-Bearing Inputs

- [[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the exact restricted E-row endpoint algebra.
- [[ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md)](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md)
  supplies the positivity boundary `rho_E > -6` and the warning that
  norm/sign conditions do not fix the E-row direction.
- [[OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md](OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md)](OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md)
  supplies the positive-diagonal readout classifier used as the tested route.
- [[MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)](MINIMAL_AXIOMS_2026-06-05.md) supplies
  the Record boundary: finite additivity after a readout context is supplied,
  with no weighting, normalization, probability, or readout context supplied
  by Record itself.
- [[S3_TIME_PRIMITIVE_CHAIN_NOTE.md](S3_TIME_PRIMITIVE_CHAIN_NOTE.md)](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) names
  the downstream open primitive-chain gate.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_positive_diagonal_e_center_selector_no_go_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=37, FAIL=0
VERDICT: positive-diagonal E-center readouts see q_E but do not select q_E=15/8.
```
