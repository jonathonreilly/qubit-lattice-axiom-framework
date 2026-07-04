# Quark Route-2 E-Center Blindness No-Go

**Date:** 2026-06-17
**Type:** no_go
**Status:** exact negative boundary / no-go; no quark-mass or CKM closure
**Runner:** `scripts/frontier_quark_route2_e_center_blindness_no_go.py`
**Load-bearing parent:** [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
(effective_status: `retained`) supplies the reduced endpoint carrier,
endpoint columns, channelwise readout form, and exact endpoint-ratio algebra
used here.

**Context parents, not load-bearing dependencies:** `QUARK_ENDPOINT_RATIO_CHAIN_LAW_NOTE_2026-04-19.md`,
`QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md`, and
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`.
These earlier rows motivated the residual but are not needed as audit
authority for this no-go.

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

The reduced carrier below is not an uncited hard-coded setup. It is the
exact restricted carrier/readout surface supplied by
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md),
Section 1. This note consumes that retained carrier and then proves a
separate negative boundary about constraints that do not evaluate the
E-center column.

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

The T-side values are the granted conditional values in the exact readout-map
parent's "smallest exact obstruction" block; this no-go does not derive them.
Its claim is narrower: even after those T-side values are supplied, every
E-center-blind constraint built from shell normalization, T-side endpoint
data, channel preservation, and low-rational/naturality filters sees exactly
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

## No-Go Discipline Gate

**N1. Alternative routes tested.** The closed claim is only the
E-center-blind endpoint route. Five attacks were checked: shell-only
normalization, T-side transfer, channel preservation, low-rational naturality,
and pairwise endpoint equalities among the blind columns. The runner shows all
five see the same signature for `rho_E = -1, 0, 1, 21/4` and therefore do not
select `21/4`.

**N2. Wall independence.** There is one wall: the constraint set does not
evaluate or otherwise supply the E-center column. No independent wall count is
being claimed.

**N3. Hidden-wall scan.** The granted T-side endpoint data are explicit
conditions sourced as the conditional obstruction surface in the retained
exact readout-map parent. "Equivalent readout primitive" and "source-domain
rule" are open positive routes, not proof inputs. The phrase "audited
numerical-match rows" is context for the rows being repaired, not status
authority for this note.

**N4. Residual matching.** The companion naturality no-go attacks the narrower
minimal-naturality residual and matches this note only as a subcase. The
R-connection bridge obstruction attacks a different residual, namely the
missing typed source-domain bridge, so it is not used as a witness here.

**N5. Rhetoric audit.** "Cannot derive" always means "cannot derive from
E-center-blind endpoint constraints." The note does not claim that Route-2,
quark masses, CKM/`J`, source-domain bridges, measured calibrations, or
future readout primitives are impossible.

**N6. Partial-closure path scan.** A partial closure is explicitly left open:
derive or approve a source-domain rule, tensor readout-map theorem, equivalent
E-center lift primitive, or alternate up-sector scalar-law route. This is not
classified as a new axiom requirement.

**N7. Steelman.** A hostile reviewer should try to show that the T-side data,
source-domain geometry, or measured E-center calibration secretly carries an
E-center condition. If so, the route is not E-center-blind and would be a
positive repair target, not a counterexample to this no-go.

**N8. Cross-cycle echo.** Prior Route-2 cycles already identified the same
missing E-center/source-readout residual. Some later notes give measured or
conditional bridge evidence, but none supplies an audited exact E-center
selection rule. This note therefore narrows the old residual instead of
closing the positive route.

## 2026-07-04 dependency-boundary repair

The conditional audit found that the runner's algebra is sound but the source
packet did not expose one-hop authority for the reduced endpoint carrier and
T-side conditional setup. This repair wires the retained exact readout-map
row as the load-bearing parent for the carrier/readout setup and clarifies the
claim boundary:

- retained parent supplies the exact reduced carrier columns and channelwise
  readout form;
- retained parent supplies the exact endpoint-ratio algebra in which the
  two T-side candidates are the conditional obstruction surface;
- this no-go still does not prove the T-side candidates or the missing
  E-center lift;
- the theorem remains the negative statement that E-center-blind constraints
  cannot select `rho_E = 21/4` even after the T-side values are granted.

Status authority remains independent audit lane only. This edit does not set
`audit_status`, `effective_status`, a retained tag, or any verdict.

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
