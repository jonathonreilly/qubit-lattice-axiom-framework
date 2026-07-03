# Quark Route-2 Nonblind Source/Readout Primitive Gate No-Go Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_nonblind_source_readout_primitive_gate_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_nonblind_source_readout_primitive_gate_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_nonblind_source_readout_primitive_gate_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_nonblind_source_readout_primitive_gate_no_go_2026_06_21.txt)
**Authority links:** [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md), [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md), [QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md), [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)

**Status authority:** independent audit lane only. This source note does not set,
predict, estimate, or apply any audit verdict.
This is not an audit verdict. It is a source note that
narrows the remaining source/readout ambiguity for the parent
`s3_time_theta_to_slice_coupling_note`.

## Scope

The parent [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) remains an open gate
because the upstream Route-2 readout-map endpoint triple is not derived:

```text
beta_T / alpha_T = -1,
alpha_T / alpha_E = -2,
beta_E / alpha_E = 21/4.
```

Recent supporting notes have already localized the live residual. The
conditional time/slice family is exact once a readout map is supplied; the
open problem is the readout-map selection, especially the E-center value

```text
rho_E := beta_E / alpha_E = 21/4.
```

This block asks the first-principles question that remains after those
localizations:

```text
Does the current named source bank contain an independent nonblind
source/readout primitive that sees the E-center lift and selects rho_E = 21/4
without importing the target?
```

The answer over the named current-bank candidate families is no. The result is
narrow: it does not rule out a future primitive.

## A_min

Allowed inputs:

1. the exact Route-2 carrier endpoint columns
   `E-shell=(1,0,0,0)`, `E-center=(1,0,1/6,0)`,
   `T-shell=(0,1,0,0)`, `T-center=(0,1,0,1/6)`;
2. the restricted bright readout form
   `P_R=[[alpha_E,0,beta_E,0],[0,alpha_T,0,beta_T]]`;
3. exact endpoint algebra
   `q_E = 1 + rho_E/6`, `q_T = 1 + rho_T/6`,
   `c_TE = s_TE q_T / q_E`;
4. the granted T-side values for this E-center subproblem,
   `rho_T = -1`, `q_T = 5/6`, and `s_TE = alpha_T/alpha_E = -2`;
5. exact Fierz/channel-count support
   `F_adj = (N_c^2 - 1)/N_c^2 = 8/9` at `N_c = 3`;
6. current repo source surfaces cited below.

Forbidden proof inputs:

1. observed quark masses;
2. fitted Yukawa values;
3. CKM or J target minimization;
4. endpoint proximity or nearest-rational selection from live data;
5. finite-box measured calibration as an exact infinite-volume theorem;
6. an untyped identification of a color fraction with a Route-2 endpoint
   readout;
7. a new readout, weighting, normalization, or source-domain axiom.

## Admissibility Gate

An independent nonblind primitive capable of deriving the missing E-center
entry must satisfy all of these conditions.

| Gate | Requirement |
|---|---|
| G1 nonblind | It distinguishes `E-center` from `E-shell`, not merely a shell normalization or time-factor property. |
| G2 selector | It fixes one exact dimensionless value of `rho_E`, `q_E`, or `c_TE`, not only a sign, interval, norm, or representative scale. |
| G3 target-free | It does not use endpoint fitting, nearest-rational matching, observed masses, measured calibration, or the target value as input. |
| G4 typed Route-2 readout | It maps into the Route-2 readout quantity `gamma_E(center)/gamma_E(shell)` or `gamma_T(center)/gamma_E(center)` with a typed source/readout bridge. |
| G5 current-surface | It is present on the current named source bank rather than supplied as the missing premise. |
| G6 target-compatible | Under the granted T-side values it gives `q_E=15/8`, equivalently `rho_E=21/4`, equivalently `c_TE=-8/9`. |

Failure of any gate means the candidate may still be useful support, but it is
not the missing independent primitive.

## Exact Algebra

With the T side granted,

```text
q_T = 5/6,
s_TE = -2.
```

For arbitrary E-center slope,

```text
q_E = 1 + rho_E/6,
c_TE = s_TE q_T / q_E = -5/(3 q_E).
```

The target equivalences are exact:

```text
rho_E = 21/4
<=> q_E = 1 + (21/4)/6 = 15/8
<=> c_TE = (-2)(5/6)/(15/8) = -8/9.
```

Likewise, if a typed bridge supplied

```text
c_TE = -F_adj = -8/9,
```

then the endpoint algebra would force

```text
q_E = 15/8,
rho_E = 21/4.
```

The remaining problem is not arithmetic. It is a target-free typed primitive
that supplies one of those equivalent E-center inputs.

## Current Candidate Classification

| Candidate family | Source surface | Gate failure |
|---|---|---|
| Carrier/time/factor rigidity | [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md) | G2 fails: the time factor is universal and the spatial prefactor keeps `rho_E` arbitrary. |
| Registration/idempotency/positivity | [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md) | G2 fails: norm/sign conditions leave the readout direction free or only bound it by `rho_E > -6`. |
| Positive projective `ell_E` sign family | [QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md) | G2/G6 fail: it gives `c_TE < 0` over the positive family, not the magnitude `|c_TE|=8/9`. |
| Active-branch eta-floor endpoint slopes | [QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md) | G2/G3/G4 fail: finite implemented-envelope comparator, no closed-form endpoint triple. |
| Measured E-center lift calibration | [QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md) | G2/G3/G4 fail: nonblind comparator evidence, with exact infinite-volume identification still open. |
| `F_adj` or `R_conn` color fraction | [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | G1/G4 fail unless the missing typed color/support endpoint bridge is supplied. |
| Register-not-read color-trace shortcut | [RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md) | G1/G2/G4 fail: Record supplies no physical EW readout or weighting rule. |
| Explicit `q_E=15/8` or `c_TE=-8/9` premise | [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md) | G3/G5 fail: this is exactly the missing premise, not an independent derivation. |

No named current-bank candidate satisfies all six gates.

## Stretch Attempt And Fan-Out

I tested the hard residual across five frames.

| Frame | Attempt | Result |
|---|---|---|
| Minimal endpoint algebra | Derive `rho_E` from the exact carrier columns and T-side values. | Fails: `rho_E=0` and `rho_E=21/4` are both exact carrier/readout maps with the same shell normalization and T side. |
| Positivity/sign | Use the positive E-family plus T orientation. | Partly succeeds: it gives `c_TE<0` for every `rho_E>-6`, but not the magnitude. |
| Source/readout registration | Use partial isometry, idempotency, or Record-style registration. | Fails: those are norm/sign conditions on the row, not shell-vs-center selectors. |
| Color/support bridge | Use `F_adj=8/9` or `R_conn`. | Conditional only: the target follows after a typed `c_TE=-F_adj` bridge, but that bridge is not in the current source bank. |
| Implemented nonblind comparators | Use eta-floor active slopes or measured E-center calibration. | Support only: they see the center, but remain finite/comparator or endpoint-fitted surfaces rather than exact target-free primitives. |

The useful sharpening is the gate itself: a future route does not merely need
"nonblindness." It must be nonblind and target-free and typed into the exact
Route-2 E-center readout magnitude.

## Theorem

**Theorem (current-bank nonblind source/readout primitive gate no-go).** On the
named current source bank and the exact Route-2 endpoint algebra above, no
current candidate family listed in this note is an independent nonblind
source/readout primitive deriving

```text
rho_E = beta_E/alpha_E = 21/4.
```

The candidates fail for different reasons:

- blind or selector-free families leave `rho_E` arbitrary;
- sign/positivity families fix only sign or bounds;
- comparator families are finite, fitted, measured, or endpoint-proximate;
- the color fraction route is exact only after the missing typed bridge is
  supplied.

Therefore the parent S3/Route-2 audit remains blocked at one of two sharp
positive tasks:

```text
derive gamma_E(center)/gamma_E(shell) = 15/8
```

directly from a target-free E-center source/readout primitive, or derive

```text
gamma_T(center)/gamma_E(center) = -8/9
```

as a typed color/support or source/readout bridge. Either task would collapse
the remaining algebra to `rho_E=21/4`.

## Boundary

This note establishes only a current-bank no-go over the named candidate
families. It does not establish:

- a derivation of the endpoint triple;
- a derivation of `rho_E = 21/4` on the current surface;
- closure of the parent `s3_time_theta_to_slice_coupling_note`;
- a no-go against all possible future primitives;
- an audit verdict;
- any quark-mass or CKM/J closure.

It does not rule out a future primitive. It says exactly what such a primitive
must supply without importing the target.

## Verification

Run:

```bash
python3 scripts/frontier_quark_route2_nonblind_source_readout_primitive_gate_no_go_2026_06_21.py
```

Expected final line:

```text
TOTAL: PASS=77, FAIL=0
```
