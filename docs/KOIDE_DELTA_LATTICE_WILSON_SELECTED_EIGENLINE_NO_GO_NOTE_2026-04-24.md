# Koide delta lattice Wilson selected-eigenline no-go

**Date:** 2026-04-24
**Runner:** `scripts/frontier_koide_delta_lattice_wilson_selected_eigenline_no_go.py`
**Status:** no-go; finite Wilson support selects a spectral subspace, not the physical selected line

## Theorem Attempt

Upgrade the finite L=3 Wilson-Dirac support model into a positive Brannen
endpoint bridge.  The hoped-for theorem was:

```text
Wilson operator + body-diagonal Z3 action
  -> canonical rank-one boundary eigenline
  -> selected open endpoint is the unit APS/anomaly channel.
```

## Result

Negative for the selected-eigenline route.  The zero-mode character sector
relevant to the selected endpoint has rank two: the retained Wilson data
select a spectral projector/eigenspace, not a unique rank-one line inside
it.  This obstruction is structural and `r`-independent.

The runner also computes the ambient finite Wilson eta proxy as a diagnostic.
On the current frozen calculation it matches the APS comparator `2/9`, so this
branch does **not** claim an ambient eta mismatch residual. The no-go is only
the selected-eigenline obstruction and the endpoint-lift residual; see "Scope
of the retained claim" below.

The runner constructs two orthonormal zero-mode lines with the same spin-lift
`Z3` character.  Every normalized mixture:

```text
psi(alpha) = cos(alpha) psi_0 + sin(alpha) psi_1
```

is still a Wilson zero mode with the same character.

## Unified Residual

The rank-two line freedom gives:

```text
selected_channel = cos(alpha)^2
spectator_channel = sin(alpha)^2
```

and therefore:

```text
delta_open / eta_APS - 1 =
  -spectator_channel + c / eta_APS.
```

Closure requires:

```text
alpha = 0
c = 0.
```

Those are a selected rank-one eigenline theorem and an endpoint-lift theorem.
They are not consequences of the finite Wilson data.

## Endpoint Lift

Even if the ambient APS value is supplied externally and a rank-one line is
selected, multiplying its lift by:

```text
exp(i s t)
```

leaves the projector and Wilson eigenline unchanged while shifting the open
endpoint by `s`.  Thus the endpoint basepoint remains an independent residual.

## Residual

```text
RESIDUAL_ENDPOINT = theta_end-theta0-eta_APS
RESIDUAL_EIGENLINE = rank_two_zero_mode_character_sector_not_canonically_split
RESIDUAL_TRIVIALIZATION = wilson_eigenline_endpoint_lift_not_fixed
RESIDUAL_SCALAR = minus_spectator_channel_plus_c_over_eta_APS
```

## Falsifiers

- A retained theorem proving the physical Brannen line is a unique rank-one
  summand of the finite Wilson zero-mode character sector.
- A retained theorem excluding the orthogonal zero-mode line as a spectator.
- A retained theorem fixing the Wilson eigenline endpoint lift/basepoint.

## Verification

Run:

```bash
python3 scripts/frontier_koide_delta_lattice_wilson_selected_eigenline_no_go.py
python3 scripts/frontier_koide_hostile_review_guard.py
python3 scripts/frontier_koide_lane_regression.py
```

The primary runner reports 14/14 PASS at the runner's frozen Wilson mass
`r = 1.0`. Check `A.3` records that the finite Wilson eta proxy is diagnostic
and is not used as an obstruction: the current frozen calculation gives
`|eta|/fixed_site = 0.222222222222`, matching `2/9 = 0.222222222222`.

The runner's no-go flag is therefore the all-pass closeout:

```text
KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO=TRUE
DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_CLOSES_DELTA=FALSE
RESIDUAL_ENDPOINT=theta_end-theta0-eta_APS
RESIDUAL_EIGENLINE=rank_two_zero_mode_character_sector_not_canonically_split
RESIDUAL_TRIVIALIZATION=wilson_eigenline_endpoint_lift_not_fixed
RESIDUAL_SCALAR=minus_spectator_channel_plus_c_over_eta_APS
AMBIENT_ETA_PROXY_NOT_USED_AS_OBSTRUCTION=TRUE
```

The `KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO=TRUE` flag
reports that, at this runner's frozen `r = 1.0` setting, the
selected-eigenline route returns the negative result documented above:
finite Wilson data select a rank-two character sector rather than a
unique rank-one selected line, and the endpoint lift is not fixed.

## Scope of the retained claim

The structural part of this no-go — that the relevant zero-mode
character sector has rank two, that a CP^1 family of rank-one lines
shares the same Wilson zero-mode and Z3 character data, and that the
selected/spectator residual is `delta/eta_APS - 1 = -spectator_channel +
c / eta_APS` — does not depend on the value of the Wilson mass `r`. It
is a count of multiplicities and an algebraic identity in `alpha` and
`c`.

The ambient eta diagnostic is deliberately excluded from the load-bearing no-go.
The current frozen runner returns `|eta|/fixed_site = 2/9`, so there is no
ambient eta mismatch to retain. Even if a future Wilson-mass convention changed
that diagnostic, it would require its own scoped theorem and would not be a
substitute for the selected-eigenline obstruction.

Accordingly, the retained no-go content of this note is the rank-two
selected-eigenline obstruction and the endpoint-lift residual. The
ambient-eta diagnostic is not a load-bearing residual.
