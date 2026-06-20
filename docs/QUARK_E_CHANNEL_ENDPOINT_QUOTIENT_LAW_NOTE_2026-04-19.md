# Quark E-Channel Endpoint Quotient Law

**Date:** 2026-04-19  
**Status:** theory-first bounded endpoint-law candidate for the remaining
`E`-channel readout primitive  
**Primary runner:** `scripts/frontier_quark_e_channel_endpoint_quotient_law.py`
**Runner cache:** `logs/runner-cache/frontier_quark_e_channel_endpoint_quotient_law.txt`

**Replay-time repair (2026-06-17).** The runner now uses the fast endpoint
certificate replay supplied by `frontier_quark_endpoint_readout_constraints.py`
and skips non-load-bearing refit diagnostics in its anchored-branch comparison.
The bounded law checks and traceability checks are unchanged.

## Safe statement

The current branch still does **not** derive the remaining quark `E`-channel
readout primitive exactly.

But the new endpoint-readout reduction already makes the right object precise:

```text
r_E = b_E / a_E = 6 * (gamma_E(center)/gamma_E(shell) - 1).
```

So the live problem is no longer “guess an up-amplitude law.” It is:

> what is the shell/center quotient `gamma_E(center)/gamma_E(shell)`?

This note gives the sharpest theory-first bounded candidate on the current
surface:

- the exact-support `T` channel already sits on the shell/center quotient
  `5/6`, giving `r_T = -1`;
- in a controlled low-rational endpoint class, the nearest `E`-channel
  shell/center quotient is `15/8`;
- that implies the bounded exact ratio law
  `r_E = 6 * (15/8 - 1) = 21/4`;
- and, together with the live shell-multiplicity candidate `a_T / a_E = -2`,
  it gives the anchored denominator candidate
  `D_E = r_E / 2 = 21/8`.

This is new bounded science, not an exact theorem.

## 1. Exact endpoint algebra

The endpoint-readout note already fixed the affine coefficients exactly from
the two support endpoints:

```text
gamma_E(delta_A1) = a_E + b_E delta_A1
gamma_T(delta_A1) = a_T + b_T delta_A1
delta_A1(center)  = 1/6
delta_A1(shell)   = 0.
```

That immediately yields the exact quotient identities

```text
r_E = b_E / a_E = 6 * (gamma_E(center)/gamma_E(shell) - 1)
r_T = b_T / a_T = 6 * (gamma_T(center)/gamma_T(shell) - 1).
```

So the open `E`-channel primitive is exactly equivalent to the shell/center
quotient `gamma_E(center)/gamma_E(shell)`.

## 2. T-channel template

On the same live endpoint data,

```text
gamma_T(center)/gamma_T(shell) = 0.833328...
```

which is already extremely close to the exact-support quotient

```text
5/6.
```

That quotient implies

```text
r_T = 6 * (5/6 - 1) = -1
```

exactly.

So the `T` channel already supplies the structural template:

- an endpoint quotient,
- one exact small fraction,
- one exact readout-ratio law.

## 3. E-channel bounded rationalization

The live `E`-channel shell/center quotient is

```text
gamma_E(center)/gamma_E(shell) = 1.876246130347...
```

The runner searches a **controlled** low-rational class:

- numerator `<= 96`
- denominator `<= 32`
- no wider expression grammar

and finds that the nearest candidate is

```text
15/8 = 1.875
```

with relative gap about `0.066%`.

That is already materially sharper than nearby small-rational competitors such
as `13/7`, `17/9`, or `47/25`.

So the clean bounded endpoint-law candidate is

```text
gamma_E(center)/gamma_E(shell) = 15/8.
```

## 4. Implied E-channel law

Using the exact endpoint identity,

```text
r_E = 6 * (15/8 - 1) = 21/4.
```

This law is within about `0.14%` of the live bounded `E`-channel ratio.

So the endpoint-quotient lane now reduces the remaining `E` primitive to one
small rational candidate:

```text
r_E = 21/4.
```

## 5. Anchored denominator candidate

If the live shell/intercept ratio is promoted to the clean shell-multiplicity
candidate

```text
a_T / a_E = -2
```

and the `T` channel is promoted to

```text
r_T = -1,
```

then the exact endpoint algebra gives

```text
|b_E / b_T| = r_E / 2.
```

So the `E`-quotient candidate implies the anchored denominator law

```text
D_E = 21/8 = 2.625.
```

That matters because:

- `21/8` is only about `0.13%` from the live bounded denominator
  `|b_E / b_T| = 2.621601...`;
- it is much closer to the live endpoint denominator than the older direct
  `sqrt(7)` proxy;
- and the corresponding anchored quark branch still stays below `1%` on the
  anchored CKM+`J` package.

So the rationalized `E`-channel law lands on the **same anchored branch** as
the live bounded endpoint solve.

## 6. What this unlocks

This note changes the remaining open problem.

The branch no longer needs to ask generically:

> what is the missing up-sector scalar law?

It can now ask more sharply:

1. can `gamma_E(center)/gamma_E(shell) = 15/8` be derived from the Route-2
   tensor support observable?
2. can `a_T / a_E = -2` be promoted from bounded shell multiplicity to theorem
   status?

If either of those lands, the `E`-channel law stops being a floating bounded
number.

## 7. Audit traceability

This note was audited 2026-05-05 with verdict
`audited_numerical_match` (class G, `chain_closes = false`). The audit
verdict is precise: the closed-form algebra from `q_E = 15/8` to
`r_E = 21/4` and `D_E = 21/8` is exact, but the load-bearing
identification `q_E = 15/8` is a nearest-rational match to an imported
live endpoint value `gamma_E(center)/gamma_E(shell) = 1.876246...`
rather than a derivation from retained tensor machinery. The re-audit
guidance names two missing bridge theorems explicitly:

```text
missing_bridge_theorem: provide a retained first-principles derivation
of gamma_E(center)/gamma_E(shell) = 15/8, and separately close the
a_T/a_E = -2 bridge before promoting the denominator law.
```

The scope-narrowing companion
`QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md`
isolates the within-scope content that the audit accepts as conditional
closed-form algebra, versus the two named missing bridge theorems that
would be required to promote the row.

A retained, audited no-go bounds the first of those two missing bridges:

> [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
> (`retained_no_go`, `audited_clean`, 28 PASS / 0 FAIL).

That no-go proves that in the exact restricted Route-2 carrier/readout
class, after granting the two T-side candidates
`beta_T/alpha_T = -1` and `alpha_T/alpha_E = -2`, the E-channel readout
entry `rho_E = beta_E/alpha_E` remains a free parameter unless an
additional E-center endpoint ratio, source-domain, or readout-map
primitive is supplied. Under that no-go, `rho_E = 21/4` is equivalent
to the endpoint ratio `gamma_T(center)/gamma_E(center) = -8/9`, but it
is not derived by carrier linearity, shell normalization, T-side
transfer, or low-rational naturality alone.

So the bounded status of this note is not merely an unresolved gap; it
is anchored to a retained no-go boundary. Any future promotion of this
row must either:

1. supply the additional E-center primitive named by the
   `naturality_no_go` (a source-domain rule, a tensor readout-map
   theorem beyond the restricted carrier columns, or an equivalent
   E-center lift), and only then can a derivation of `15/8` from
   tensor machinery proceed; or
2. supply a separate retained shell-multiplicity theorem deriving
   `a_T/a_E = -2` from shell-counting algebra, narrowing the open
   derivation problem to the first identification only.

Neither bridge is supplied by the current packet. The 2026-05-10
companion records that the audit explicitly accepts this scope.

The companion
`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md` closes a broader
false repair route. It proves that any endpoint repair which is blind to the
E-center column leaves `rho_E = beta_E/alpha_E` free, even after shell
normalization, the two T-side endpoint candidates, channel preservation, and
low-rational/naturality filters are granted. Therefore the quotient target
`15/8` cannot be derived by another shell-only or T-side rationalization; a
positive repair must add a real E-center lift or equivalent source/readout
primitive.

## Honest endpoint

The current best theory-first bounded candidate is:

```text
gamma_E(center)/gamma_E(shell) = 15/8
=> r_E = 21/4
=> D_E = 21/8
```

This is useful new science because it rationalizes the remaining `E`-channel
primitive into one controlled endpoint law candidate. But it is still bounded,
not retained, because the current theorem stack does not yet derive `15/8`
from exact tensor machinery. The retained no-go in
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`
makes the obstruction explicit: in the exact restricted Route-2
carrier/readout class with the granted T-side candidates, `rho_E`
remains a free parameter, so a `15/8` derivation requires an
additional E-center primitive beyond the retained carrier surface.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_e_channel_endpoint_quotient_law.py
```

Current expected result on this branch:

- `frontier_quark_e_channel_endpoint_quotient_law.py`: `PASS=22 FAIL=0`

The runner now exercises an explicit `PART 5: Audit Traceability
Cross-References` block in addition to the original four parts. The
extra checks assert that the parent note exposes its 2026-05-05 audit
verdict, names both missing bridge theorems, and cross-references both
the 2026-05-10 scope-narrowing companion and the retained
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`.
This keeps the bounded status formally traceable from the runner
output without altering the bounded scope of the law candidate itself.
