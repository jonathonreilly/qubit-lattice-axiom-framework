# Quark Route-2 Inverse-Square Covariance Primitive Candidate

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** conditional support / primitive-target characterization
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** conditional support / primitive-target characterization
**Trace class:** open_gate_boundary
**Reachability to target:** supports the open Route-2 endpoint by isolating a bounded source/readout condition; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py`](../scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)


## Question

Prior Route-2 work relocated the missing E-center datum to a same-domain
covariance bridge

```text
lambda := q_E/q_T = kappa^2 = 9/4,
```

where `kappa=3/2` is the exact `O_h` shell leverage between the Route-2 `E`
and `T1` channels. The quadratic route then proved that ordinary `O_h`
quadratic invariants leave the `E:T1` reduced-matrix-element ratio free, and
that the desired bridge is equivalent to an inverse-square channel-weight law.

This note packages that remaining primitive target exactly:

```text
q_X proportional to w_X^-2.
```

It asks what follows if this primitive is supplied, whether it is unique in a
power-law family, and whether the current surface already supplies it.

## Exact Conditional Construction

The six-arm `O_h` star has channel dimensions

```text
dim(E) = 2,
dim(T1) = 3,
N_arm = 6.
```

So the per-arm projector weights are

```text
w_E = dim(E)/6 = 1/3,
w_T = dim(T1)/6 = 1/2,
kappa = w_T/w_E = 3/2.
```

If the readout/covariance primitive is the dual inverse-square channel metric

```text
q_X proportional to w_X^-2,
```

then

```text
lambda = q_E/q_T = (w_T/w_E)^2 = (3/2)^2 = 9/4.
```

With the granted T-side value `q_T=5/6`,

```text
q_E = lambda q_T = (9/4)(5/6) = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

Thus the inverse-square primitive would close the same endpoint arithmetic as
the color-ray and `c_TE=-R_conn` conditional routes, but by a same-domain
covariance rule rather than a cross-domain color identification.

## Uniqueness Among Power-Law Channel Rules

For a power-law channel rule

```text
q_X proportional to w_X^p,
```

the covariance ratio is

```text
lambda(p) = q_E/q_T = (w_E/w_T)^p = (2/3)^p.
```

Solving

```text
(2/3)^p = 9/4
```

gives exactly

```text
p = -2.
```

The runner verifies this both by an exact integer scan and by the real
logarithmic solution. Nearby natural laws fail:

| Rule | `p` | `lambda` | `rho_E` |
|---|---:|---:|---:|
| equal response | `0` | `1` | `-1` |
| dimension-weight response | `1` | `2/3` | `-8/3` |
| quadratic response | `2` | `4/9` | `-34/9` |
| inverse-linear response | `-1` | `3/2` | `3/2` |
| inverse-square response | `-2` | `9/4` | `21/4` |

So the exact target is not "some covariance law." It is specifically the
dual/inverse-square channel law.

## Current-Surface Firewall

The current repo surface does not supply this primitive.

- The sharper covariance note says the free datum is the covariance bridge and
  that `O_h` equivariance does not supply it.
- The quadratic follow-on note says no named functional produces an
  inverse-square-of-projector-weight center lift, while future nonlinear
  constructions remain open.
- The record/positivity no-go says `rho_E` needs a shell-vs-center
  distinguishing input, not a generic registration principle.
- The exact readout-map note keeps the endpoint triple open and names the
  `E`-channel ratio as the irreducible missing map entry.

In typed-graph terms, the current surface has no path

```text
O_h shell weights -> inverse-square covariance primitive -> rho_E=21/4.
```

Adding exactly that primitive creates the path. Therefore this block is a
target characterization and conditional-support packet, not an actual
current-surface derivation.

## What This Moves

This block gives the next positive target a precise mathematical shape:

```text
derive q_X proportional to w_X^-2
```

from a named same-domain tensor/source/readout construction, or rule it out
for a larger class of nonlinear functionals.

It also supplies falsifiers for common substitutes: equal response,
dimension-weight response, ordinary quadratic response, and inverse-linear
response all miss `rho_E=21/4`.

## What Remains Open

Open routes:

- derive an actual inverse-square covariance primitive from same-domain
  Route-2 source/readout structure;
- find a different E-center lift primitive that bypasses the `O_h` weight law;
- prove a no-go for a broader nonlinear functional class;
- pivot to a different up-sector scalar-law route.

This note does not derive the endpoint triple on the actual current surface,
does not adopt a new axiom or convention, and does not use observed quark
masses, CKM/J targets, live endpoint proximity, or fitted values.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py
```

Expected result:

```text
PASS=23 FAIL=0 TOTAL=23
```
