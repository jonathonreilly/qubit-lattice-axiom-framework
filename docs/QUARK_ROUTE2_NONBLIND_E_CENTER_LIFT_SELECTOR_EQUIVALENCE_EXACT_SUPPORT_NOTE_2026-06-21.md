# Quark Route-2 Nonblind E-Center Lift Selector Equivalence

**Date:** 2026-06-21
**Status:** exact support / bounded support; no endpoint derivation
**Claim type:** exact_support
**Status authority:** branch-local physics-loop packet only. This note does
not set an audit verdict and does not update repo-wide authority surfaces.
**Primary runner:**
[`scripts/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.py`](../scripts/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.py)
(`PASS=23 FAIL=0`)
**Runner output:**
[`outputs/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.txt`](../outputs/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.txt)

## Scope

Block50 showed that E-center-blind nonlinear tensor-polynomial observables
cannot derive `rho_E = 21/4`. This block attacks the next direct target:
what exactly must a nonblind E-center primitive prove?

The answer is an exact selector-equivalence packet. After the two T-side
endpoint candidates are granted, all of the following are the same target:

```text
rho_E = beta_E / alpha_E = 21/4
q_E = gamma_E(center)/gamma_E(shell) = 15/8
q_E / q_T = 9/4
gamma_T(center)/gamma_E(center) = -8/9
gamma_T(center)/gamma_E(center) = -R_conn, if the typed R_conn bridge is supplied at N_c = 3
```

This is support, not endpoint closure. The current authority surface still
does not supply the selector equation or typed bridge.

## Exact equivalence

With

```text
beta_T / alpha_T = -1
alpha_T / alpha_E = -2
```

the T-side quantities are

```text
q_T = 1 + (-1)/6 = 5/6
gamma_T(shell)/gamma_E(shell) = -2.
```

For arbitrary `rho_E`,

```text
q_E = 1 + rho_E/6
gamma_T(center)/gamma_E(center) = (-2)(5/6)/q_E.
```

Therefore:

```text
rho_E = 21/4
<=> q_E = 15/8
<=> q_E/q_T = 9/4
<=> gamma_T(center)/gamma_E(center) = -8/9.
```

The runner verifies all four directions by exact rational arithmetic.

## Typed bridge support

For `N_c = 3`,

```text
R_conn = (N_c^2 - 1)/N_c^2 = 8/9.
```

If a typed Route-2 source/readout theorem supplies

```text
gamma_T(center)/gamma_E(center) = -R_conn,
```

then the same endpoint algebra forces:

```text
q_E = 15/8
rho_E = 21/4.
```

The runner also checks wrong-structure falsifiers:

| Substitution | Result |
|---|---|
| `N_c = 2` | `rho_E = 22/3` |
| center denominator `5` | `rho_E = 4` |
| center denominator `12` | `rho_E = 51/4` |
| no E-center lift | `center T/E = -5/3` |

So the target is not produced by merely mentioning `8/9`, `6`, or a nonblind
column. The typed bridge and the support denominator are both load-bearing.

## Nonblind access is necessary but not sufficient

Evaluating the E-center column exposes the continuum

```text
P(rho_E) E-center = (1 + rho_E/6, 0).
```

The runner samples exact alternatives:

```text
rho_E = -1, 0, 1, 21/4, 8
```

All keep the granted T-side data fixed while producing distinct E-center
lifts. Positivity of the E-center readout gives only the bound
`rho_E > -6`; it does not select `21/4`.

Thus the next theorem target is not just "see E-center." It is:

```text
derive one selector equation equivalent to q_E = 15/8
```

or derive the typed source/readout bridge equivalent to
`center T/E = -8/9`.

## Authority-surface checks

The runner checks the current authority boundary:

- the E-center lift derivation attempt names the exact missing computation
  `gamma_E(center)/gamma_E(shell) = 15/8`;
- the source-domain bridge note keeps the typed
  `R_conn -> gamma_T(center)/gamma_E(center)` bridge missing;
- the measured calibration note is support/comparator evidence, not a
  derivation;
- the box-size scan closes the bulk-limit promotion of the `N=15` coincidence
  and supplies no selecting primitive;
- the exact readout note still names `beta_E/alpha_E` as the missing map
  entry;
- the theta-to-slice parent remains blocked by the endpoint triple.

## Consequence

This block gives the next positive PR an exact checklist. A successful
nonblind E-center lift theorem must prove at least one of the equivalent
selector equations above without using observed masses, fitted targets,
nearest-rational endpoint matching, or an untyped color/support identification.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=23, FAIL=0
```
