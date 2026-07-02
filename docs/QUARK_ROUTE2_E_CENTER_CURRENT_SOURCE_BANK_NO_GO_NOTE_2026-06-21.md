# Quark Route-2 E-Center Current Source-Bank No-Go

**Date:** 2026-06-21
**Type:** no_go
**Claim type:** no_go
**Actual current-surface status:** no-go / bounded current-bank obstruction.
This note does not derive `rho_E = 21/4`, does not prove that no future
source-domain primitive can derive it, and does not close the
`s3_time_theta_to_slice_coupling_note` open gate.
**Status authority:** branch-local physics-loop artifact only. Independent
review and the normal audit lane are required before any repo-wide status
change.
**Primary runner:** [scripts/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.py](../scripts/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.py)
**Runner cache:** [logs/runner-cache/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.txt](../logs/runner-cache/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.txt)

## Scope

This block attacks the typed E-center source/readout primitive route for the
Route-2 endpoint triple

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).
```

The target is the E-row slope

```text
rho_E := beta_E/alpha_E = 21/4,
q_E = 1 + rho_E/6 = 15/8,
c_TE = -8/9
```

after the current T-side candidates are granted.

The result is a bounded no-go over the current named source bank. It says the
current bank has no E-center-evaluating invariant that distinguishes
`rho_E=0` from `rho_E=21/4`. Therefore a proof of the target cannot be a
function only of the current bank's named invariants; it must add an explicit
E-center bridge.

## Current Source Bank

The bank tested here is deliberately narrow and repo-internal:

- [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md)
  supplies the support scalar endpoint step `delta_A1(center)-delta_A1(shell)=1/6`.
- [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)
  defines the carrier symbol
  `K_R(q)=(u_E,u_T,delta_A1 u_E,delta_A1 u_T)` under named admitted inputs,
  but does not identify a physical readout primitive.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the restricted readout class and endpoint algebra.
- [`QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md)
  records the positive E-projective family `rho_E > -6` and sign separation.
- [`OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md`](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md)
  supplies `kappa=3/2`, `kappa^2=9/4`, and `Hom_Oh(E,T1)=0`.
- [`QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md)
  and [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md) supply exact
  `F_adj=8/9` support while keeping the typed Route-2 center bridge open.
- [`QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md)
  supplies stack-internal measured calibration as comparator evidence, not as
  a proof input.

Forbidden proof inputs are observed quark masses, fitted Yukawa entries, CKM/J
target minimization, nearest-rational selection from live endpoint data,
eta-floor endpoint fitting, and untyped identification of a color fraction
with a Route-2 center readout.

## Exact Counter-Witness Pair

Grant the T-side candidates

```text
rho_T = beta_T/alpha_T = -1,
s_TE = alpha_T/alpha_E = -2,
q_T = 5/6.
```

The normalized readout family is

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

Consider two exact admissible E rows:

```text
rho_E = 0,
rho_E = 21/4.
```

They share identical current source-bank invariants:

```text
delta_A1(center)-delta_A1(shell) = 1/6,
K_R(q) = (u_E,u_T,delta_A1 u_E,delta_A1 u_T),
q_T = 5/6,
s_TE = -2,
F_adj = 8/9,
kappa = 3/2,
kappa^2 = 9/4,
Hom_Oh(E,T1) = 0,
rho_E > -6,
c_TE < 0.
```

But they have different E-center outputs:

| `rho_E` | `q_E=1+rho_E/6` | `c_TE=(-2)(5/6)/q_E` | E-center lift |
|---:|---:|---:|---:|
| `0` | `1` | `-5/3` | `1` |
| `21/4` | `15/8` | `-8/9` | `15/8` |

Therefore the current source-bank invariants are not enough to select the
target E-center value. A deterministic theorem using only those invariants
would have identical inputs for the two rows above but would need to output
different `q_E` values.

## Theorem

**Theorem (current source-bank no-go).** In the exact Route-2 restricted
readout family after granting the T-side candidates, the current source bank
listed above does not determine `rho_E`. The two maps `P(0)` and `P(21/4)`
agree on all bank invariants tested here and both lie in the positive
sign-correct family, yet they have different E-center lift, different `q_E`,
and different `c_TE`. Thus no derivation of `rho_E=21/4` can be obtained as a
function only of the current bank invariants. A successful derivation must add
at least one non-blind E-center bridge, such as:

```text
q_E = 15/8,
c_TE = -F_adj,
q_E/q_T = kappa^2,
```

with the bridge itself derived rather than inserted.

## What This Prunes

This prunes attempts that recombine the current bank without adding a new
E-center-evaluating rule:

- `delta_A1=1/6` supplies the denominator but not the E-row slope.
- The carrier symbol `K_R` supplies the coordinate slot
  `delta_A1 u_E` but not the coefficient `beta_E/alpha_E`.
- Positivity and sign separation give `rho_E>-6` and `c_TE<0`, not the
  magnitude `8/9`.
- `F_adj=8/9` supplies an exact color/channel fraction, but the typed edge
  `F_adj -> c_TE=-F_adj` is the missing bridge.
- `kappa^2=9/4` is exact shell leverage support, but the covariance rule
  `q_E/q_T=kappa^2` is the missing bridge.
- Measured calibration is comparator evidence and cannot be used as the
  source theorem.

## What Remains Open

The positive target is now sharply stated:

```text
derive an E-center bridge that distinguishes P(0) from P(21/4)
```

without observed/fitted/nearest-rational inputs. Equivalently, derive one of
the following from a typed source/readout theorem:

```text
q_E = 15/8,
c_TE = -8/9,
q_E/q_T = 9/4,
gamma_T(center)/gamma_E(center) = -F_adj.
```

## What Is Not Claimed

- This note does not derive `rho_E=21/4`.
- This note does not rule out future source-domain or nonlinear primitives.
- This note does not close the s3-time parent open gate.
- This note does not apply or predict an audit verdict.
- This note does not update repo-wide authority surfaces.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.py
```

Expected summary:

```text
TOTAL: PASS=21, FAIL=0
```
