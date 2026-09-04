# Quark Route-2 T-Row Primitive Minimality Selector Boundary

**Date:** 2026-06-22
**Type:** no_go
**Claim type:** no_go
**Assessment role:** conditional primitive/minimality selector no-go.
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Any `audit_status` and
`effective_status` fields are pipeline-derived.
**Primary runner:** [scripts/frontier_quark_route2_t_row_primitive_minimality_selector_boundary_2026_06_22.py](../scripts/frontier_quark_route2_t_row_primitive_minimality_selector_boundary_2026_06_22.py)
**Runner cache:** [logs/runner-cache/frontier_quark_route2_t_row_primitive_minimality_selector_boundary_2026_06_22.txt](../logs/runner-cache/frontier_quark_route2_t_row_primitive_minimality_selector_boundary_2026_06_22.txt)

## Scope

The current Route-2 T-side endpoint attempt records the first two endpoint
targets as values reproduced only after a readout row is supplied:

```text
beta_T / alpha_T = -1,
alpha_T / alpha_E = -2.
```

This note does not import an unlanded row-shape theorem. It asks whether the
enumerated primitive-integer, orientation, and minimality rules below can
select the full relative row

```text
(alpha_E, alpha_T, beta_T) = (1, -2, 2)
```

without importing the endpoint target.

The result is a primitive/minimality selector boundary. Under the conditional
row-shape or shell-scale premises below, the enumerated selectors do not derive
the full T row. The target `n=2` remains an extra selector.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md) | Records the exact endpoint algebra and the missing T-row shape and E/T shell-normalization selectors. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Names the Route-2 readout-map endpoint triple as an open theorem target, not a closed input. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Supplies the premise boundary that Record does not provide a readout context, weighting rule, or normalization rule. |

## Premise Boundary

The minimal axiom and approved-primitive surfaces do not supply a readout
context, row selector, weighting rule, or normalization rule. In particular:

- Record begins only after a readout context is given.
- The scale-reference primitive carries no dimensionless readout content.
- The kinetic-isotropy primitive supplies no selector or readout bridge.
- The realized-state primitive supplies the evaluation slot, not a state or
  selector.

Therefore a derivation of `(1,-2,2)` must come from a separate physical
readout-row theorem, not from the existing approved premise registry alone.

## Supplied Premises

Both tests below are conditional. They supply the integer-domain restriction,
the E-shell unit convention `alpha_E=1`, and the negative T-shell orientation.
The shape-family test additionally supplies `beta_T=-alpha_T`; the shell-family
test additionally supplies `alpha_T=-2`. The ratio
`q_T = 1 + (beta_T / alpha_T) / 6` uses the current-main endpoint algebra's
center-column normalization from the cited Route-2 T-side endpoint note. None
of these supplied premises is derived here as a selector.

## Shape-Supplied Integer Family

Suppose the T-row shape law is supplied:

```text
beta_T = -alpha_T.
```

With E-shell unit convention `alpha_E=1` and negative T-shell orientation, the
integer family is

```text
(alpha_E, alpha_T, beta_T) = (1, -n, n),  n >= 1.
```

For every `n` in this family,

```text
rho_T = beta_T / alpha_T = -1,
q_T = 1 + rho_T / 6 = 5/6,
s_TE = alpha_T / alpha_E = -n.
```

The endpoint target is the specific member `n=2`. But the enumerated primitive
or minimality selectors do not pick it:

| Selector | Selected member | Result |
| --- | --- | --- |
| Full integer-row gcd `gcd(1,n,n)=1` | all `n` | no selection |
| Primitive T-subrow gcd `gcd(n,n)` | `n=1` | misses target |
| Minimal `|alpha_T|` | `n=1` | misses target |
| Minimal Frobenius norm `1+2n^2` | `n=1` | misses target |
| Minimal center deformation `|beta_T/(6 alpha_T)|` inside the shape family | all `n` tie | no selection |

The target row is primitive as a three-entry row, but so is `(1,-1,1)`. The
target T subrow has gcd `2`, while `(alpha_T,beta_T)=(-1,1)` has gcd `1`.
Thus primitive T-subrow gcd selects `n=1`, not `n=2`.

## Shell-Scale Supplied Beta Family

Conversely, suppose the shell scale is supplied:

```text
alpha_E = 1,
alpha_T = -2.
```

Then the integer beta family is

```text
(alpha_E, alpha_T, beta_T) = (1, -2, beta_T).
```

Every member has

```text
s_TE = -2.
```

But the T-row shape remains free:

| `beta_T` | `rho_T` | `q_T` |
| ---: | ---: | ---: |
| `0` | `0` | `1` |
| `1` | `-1/2` | `11/12` |
| `2` | `-1` | `5/6` |
| `3` | `-3/2` | `3/4` |

Minimal Frobenius norm on this fixed-shell family selects `beta_T=0`.
Smallest positive integer beta selects `beta_T=1`. The target `beta_T=2`
requires an additional evenness or multiplicity-two rule.

## Missing Positive Premise

No approved premise supplies the multiplicity-two rule

```text
n = 2
```

or an equivalent full-row selector. Evenness is not supplied by the current
premise registry, the carrier columns, the common time factor, Record
additivity, or the enumerated row-minimality tests.

The positive route left open is therefore sharper than "derive the T row":
derive a non-circular physical reason why the T shell has multiplicity two
relative to the E-shell unit, while also keeping the T-center row shape
`beta_T=-alpha_T`.

## Boundary

This note does not prove that no future T-row theorem exists. It proves only
that the following overread fails:

```text
integer row + orientation + row-shape support + enumerated minimality
  => (alpha_E, alpha_T, beta_T) = (1, -2, 2).
```

It separately checks the fixed-shell beta family, where the enumerated
minimality tests select `beta_T=0` or `beta_T=1` instead of `beta_T=2`.

The target row still requires a physical multiplicity-two theorem, an
owner-approved readout primitive, or another non-circular selector for the full
relative row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_t_row_primitive_minimality_selector_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=74, FAIL=0
```
