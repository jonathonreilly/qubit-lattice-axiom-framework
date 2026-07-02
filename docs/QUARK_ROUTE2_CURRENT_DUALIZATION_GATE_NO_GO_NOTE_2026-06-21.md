# Quark Route-2 Current Dualization Gate No-Go

**Date:** 2026-06-21
**Actual current-surface status:** no-go for current-bank canonical-dual dualization shortcut
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_current_dualization_gate_no_go_2026_06_21.py`

Actual current-surface status: no-go for current-bank canonical-dual dualization shortcut

## Scope

This note attacks the next sharp residual in the Route-2 endpoint problem:

```text
derive the inverse-square / canonical-dual source-readout law that would
turn the Schur weights w_E=1/3 and w_T=1/2 into q_E/q_T=9/4.
```

The result is negative on the current authority bank. The current bank contains
exact carrier/readout algebra, an exact conditional time family, a source-domain
bridge boundary, an E-center derivation attempt with a named missing row, and a
registration/positivity no-go. It does not contain the needed two-sided
canonical-dual law.

This is not an audit verdict and does not resolve the parent
`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md` row. It does not rule out a future inverse-square dualization theorem. It only prunes the shortcut that the current Route-2 source/readout authority bank already supplies that theorem.

## Exact Dual-Factor Arithmetic

On the six-arm Schur frame, the same-domain weights are:

```text
w_E = 1/3
w_T = 1/2
w_T / w_E = 3/2
```

If a channel lift has `p` inverse Schur-weight factors,

```text
q_X proportional to w_X^-p,
```

then:

```text
q_E / q_T = (w_E / w_T)^-p.
```

The target after granting the T-side conditional values is:

```text
q_T = 5/6
q_E = 15/8
rho_E = beta_E / alpha_E = 21/4
gamma_T(center) / gamma_E(center) = -8/9.
```

The controls are exact:

| Dual factors | Interpretation | `q_E/q_T` | `rho_E` | Center T/E |
|---:|---|---:|---:|---:|
| `0` | no dual factor | `1` | `-1` | `-2` |
| `1` | source-only or readout-only dual | `3/2` | `3/2` | `-4/3` |
| `2` | source and readout both dualized | `9/4` | `21/4` | `-8/9` |

Thus one-sided source-only or readout-only dualization gives `p=1`, not the
endpoint. The endpoint needs two inverse Schur-weight factors.

## Current Authority Bank

The tested current bank is:

| Surface | What it supplies | What remains missing |
|---|---|---|
| `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` | class-A carrier definition `K_R(q)` under named inputs | physical primitive bridge and source/readout adjointness |
| `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | exact restricted readout class and missing-map obstruction | `beta_E/alpha_E = 21/4` |
| `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md` | exact conditional family after a supplied `P_R` | a theorem selecting unique `P_R` |
| `S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md` | ambiguity localized in spatial prefactor, universal time channel | spatial readout selector |
| `QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md` | exact conditional arithmetic and named E-center target | exact E-channel source/readout row |
| `QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md` | T-side values reproduced after candidate row is supplied | derivation of that row |
| `QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md` | typed-edge color/source boundary | `R_conn -> c_TE` source/readout bridge |
| `ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md` | positivity/registration fix norm or bounds | readout direction `rho_E` |

The current authority bank does not supply a source/readout adjointness or
canonical-dual law. In runner-firewall form: the current authority bank does not supply a source/readout adjointness or canonical-dual law. The runner
searches the bank for the relevant semantics:

```text
canonical dual, dual frame, Moore-Penrose, pseudoinverse, Riesz,
adjoint readout, source/readout adjoint, two-sided dual,
two-sided canonical, inverse-square dualization.
```

None is present in the tested bank.

## The No-Go Boundary

The pruned shortcut is:

```text
current Route-2 source/readout bank
  => two-sided canonical-dual Schur compliance
  => p = 2
  => rho_E = 21/4.
```

The first implication is not currently supplied. The current notes instead say:

1. the time row starts after `P_R` is supplied;
2. the exact readout map row leaves `rho_E` as the irreducible missing entry;
3. the E-center attempt says the source bank lacks the exact E-channel row;
4. the T-side attempt reproduces the values only after the candidate row is supplied;
5. registration/positivity conditions fix norm or sign bounds rather than readout direction;
6. source-domain color/Rconn data need an extra typed bridge.

So a valid future positive route must add new theorem content: a typed
source/readout adjointness theorem, a canonical-dual frame law, a
Moore-Penrose/Riesz representative law over the same Schur frame, or an
equivalent inverse-square source/readout coefficient theorem.

## Stuck Fan-Out

The attempted current-bank derivation was checked across five frames:

| Frame | Result |
|---|---|
| Source-only dual | Gives one inverse factor, hence `p=1` and `rho_E=3/2`. |
| Readout-only dual | Same obstruction: one inverse factor gives `p=1`. |
| Two-sided dual | Would give the target, but the current bank lacks the law tying both sides to the same Schur dual frame. |
| Generic Gram/Riesz/pseudoinverse | No typed Route-2 `P_R` theorem with those semantics appears in the tested authority bank. |
| Registration/positivity | Fixes norm or a one-sided bound, not the shell-vs-center readout direction. |

All frames point to the same wall: the endpoint needs a two-sided
inverse-Schur source/readout theorem, and that theorem is not already in the
current bank.

## Consequence

This block narrows the next science target. The remaining positive target is:

```text
derive a typed two-sided inverse-Schur source/readout theorem on the Route-2
carrier, or provide an equivalent coefficient theorem fixing p=2 without
endpoint fitting.
```

This note does not say such a theorem is impossible. It says only that the
current authority bank does not already contain it.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_current_dualization_gate_no_go_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=62, FAIL=0
```
