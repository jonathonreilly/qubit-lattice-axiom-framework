# SU(2) u0 Single-Plaquette Beta=16 Native Interval

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This proves a source-side bounded interval for the single-plaquette SU(2) beta=16 u0 input used by the g_2(v) interval row; independent audit is still required before effective status changes."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** bounded support for the native SU(2) beta=16 one-plaquette
`u_0` interval only.
**Runner:** [`scripts/su2_u0_single_plaquette_beta16_native_interval_2026_06_18.py`](./../scripts/su2_u0_single_plaquette_beta16_native_interval_2026_06_18.py)

## Claim

On the native SU(2) one-plaquette Wilson class-angle surface at
`beta_W = 16`, define

```text
u0(SU2, beta=16) := <(1/2) Re Tr U_p>^(1/4).
```

Then

```text
u0(SU2, beta=16) in [0.9761, 0.9762] subset [0.96, 0.98].
```

This closes the row-local need for a literature-supplied numerical
interval in `G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md`.
It does not assert an audit-ratified retained status, and it does not
replace independent audit.

## Construction

Use the native SU(2) class-angle parametrization

```text
U ~ diag(exp(i theta), exp(-i theta)),  theta in [0, pi],
P(theta) := (1/2) Re Tr U = cos(theta).
```

The SU(2) class-angle Haar density is proportional to

```text
sin(theta)^2 dtheta.
```

The one-plaquette Wilson-weighted partition function and plaquette
expectation are

```text
Z(beta) = int_0^pi sin(theta)^2 exp(beta cos(theta)) dtheta,

P_SU2(beta) =
  int_0^pi cos(theta) sin(theta)^2 exp(beta cos(theta)) dtheta
  / Z(beta).
```

Equivalently, differentiating the standard SU(2) class-angle integral
gives

```text
P_SU2(beta) = I_2(beta) / I_1(beta),
```

where `I_n` is the modified Bessel function of the first kind. The
runner evaluates both the direct quadrature and the Bessel ratio and
requires agreement to high precision.

## Result

At the Wilson coefficient supplied by the one-hop lattice-alpha anchor
[`SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md`](SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md),
`beta_W = 16`, the direct computation gives

```text
P_SU2(16)  =  0.907814845880750...
u0         =  P_SU2(16)^(1/4)
           =  0.976111254449673...
```

Therefore

```text
u0(SU2, beta=16) in [0.9761, 0.9762] subset [0.96, 0.98].
```

The parent g_2(v) bounded interval keeps its wider endpoints
`[0.96, 0.98]` so the already-audited endpoint formulas remain
unchanged. This bridge only changes the source authority for the X1
interval: the interval is now framework-native one-plaquette support,
not a row-local literature admission.

## Boundaries

- This is a one-plaquette SU(2) Wilson class-angle computation at
  `beta_W = 16`.
- This is not a full thermodynamic SU(2) gauge-field continuum limit.
- This is not an observed g_2(v) input.
- This consumes no fitted selector.
- This consumes no SU(2) Monte Carlo plaquette value.
- This leaves no literature numerical interval load-bearing role.
- Literature may be cited in parallel for the standard SU(2)
  class-angle integral, but the runner computes the integral directly.

## Verification

Run:

```text
python3 scripts/su2_u0_single_plaquette_beta16_native_interval_2026_06_18.py
```

Expected summary:

```text
TOTAL: PASS=10 FAIL=0
```
