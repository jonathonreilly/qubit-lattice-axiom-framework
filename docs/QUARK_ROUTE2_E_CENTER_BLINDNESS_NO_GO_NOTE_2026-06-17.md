# Quark Route-2 E-Center Blindness No-Go

**Date:** 2026-06-17
**Status:** exact negative boundary / no-go; no quark-mass or CKM closure
**Runner:** `scripts/frontier_quark_route2_e_center_blindness_no_go.py`
**Primary parents:**
`QUARK_ENDPOINT_RATIO_CHAIN_LAW_NOTE_2026-04-19.md`,
`QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md`,
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`

## Scope

This note sharpens the repair target for the quark Route-2 endpoint
numerical-match rows. It does not derive the missing value

```text
rho_E := beta_E / alpha_E = 21/4
```

or the equivalent endpoint ratios

```text
gamma_E(center)/gamma_E(shell) = 15/8
gamma_T(center)/gamma_E(center) = -8/9.
```

Instead it proves an exact negative boundary: any Route-2 endpoint repair that
is blind to the E-center column cannot derive those values. A positive repair
must supply a genuine E-center lift, source-domain rule, or equivalent
readout primitive.

## Reduced Endpoint Carrier

On the restricted Route-2 endpoint carrier, the exact columns are

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6).
```

The E-center-blind subspace is

```text
span{E-shell, T-shell, T-center}.
```

The runner checks that this subspace has rank `3`, while the full endpoint
carrier has rank `4`. The missing fourth direction is

```text
E-center - E-shell = (0, 0, 1/6, 0),
```

which is not in the E-center-blind subspace.

## Invariance Theorem

After the two T-side candidates are granted,

```text
beta_T / alpha_T = -1
alpha_T / alpha_E = -2,
```

normalize `alpha_E = 1` and write the reduced readout as

```text
P(rho_E) =
[[1, 0, rho_E, 0],
 [0,-2, 0,     2]].
```

Then for every value of `rho_E`,

```text
P(rho_E) E-shell  = (1, 0)
P(rho_E) T-shell  = (0,-2)
P(rho_E) T-center = (0,-5/3)
```

and therefore

```text
q_T = gamma_T(center)/gamma_T(shell) = 5/6
gamma_T(shell)/gamma_E(shell) = -2.
```

All E-center-blind constraints built from shell normalization, T-side endpoint
data, channel preservation, and low-rational/naturality filters see exactly
the same data for all `rho_E`.

But

```text
P(rho_E) E-center = (1 + rho_E/6, 0).
```

So the E-center lift varies freely until a constraint actually evaluates the
E-center column or supplies an equivalent source/readout primitive.

## Target Equivalence

The target value is exactly equivalent to the missing E-center lift:

```text
rho_E = 21/4
  <=> gamma_E(center)/gamma_E(shell) = 15/8
  <=> gamma_T(center)/gamma_E(center) = -8/9
```

under the granted T-side endpoint data.

The runner checks this by exact rational arithmetic:

```text
1 + (21/4)/6 = 15/8
(-5/3) / (15/8) = -8/9
```

and conversely solving

```text
(-5/3) / (1 + rho_E/6) = -8/9
```

recovers `rho_E = 21/4` uniquely.

## Consequence

This no-go retires a broad class of tempting repairs:

```text
Route-2 endpoint carrier
+ shell normalization
+ T-side endpoint candidates
+ channel preservation
+ low-rational / naturality filter
=> rho_E = 21/4.
```

That implication is false. The runner gives exact admissible alternatives
such as

```text
rho_E = -1, 0, 1, 21/4
```

all of which preserve the same E-center-blind data but produce different
E-center values.

Therefore another rational scan, shell-only normalization argument, or
T-side transfer argument cannot repair the audited numerical-match rows. The
next positive theorem must contain new information that sees the E-center
column.

## What Remains Open

The exact positive target is unchanged:

```text
derive gamma_T(center)/gamma_E(center) = -8/9
```

or equivalently derive

```text
gamma_E(center)/gamma_E(shell) = 15/8.
```

Viable positive routes now have to include at least one of:

1. a source-domain rule that fixes the E-center endpoint weight;
2. a tensor readout-map theorem beyond the restricted endpoint carrier columns;
3. an equivalent E-center lift primitive;
4. a different up-sector scalar-law route outside Route-2 endpoint readout.

## Validation

Run:

```bash
python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
python3 scripts/cached_runner_output.py scripts/frontier_quark_route2_e_center_blindness_no_go.py --refresh
python3 scripts/cached_runner_output.py scripts/frontier_quark_route2_e_center_blindness_no_go.py --check-only
```

Current expected result:

```text
frontier_quark_route2_e_center_blindness_no_go.py: PASS=14 FAIL=0
```
