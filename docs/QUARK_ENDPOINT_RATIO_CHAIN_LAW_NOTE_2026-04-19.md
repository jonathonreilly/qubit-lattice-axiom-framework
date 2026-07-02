# Quark Endpoint Ratio-Chain Law

**Date:** 2026-04-19  
**Status:** theory-first bounded endpoint-ratio-chain candidate  
**Primary runner:** `scripts/frontier_quark_endpoint_ratio_chain_law.py`
**Runner cache:** `logs/runner-cache/frontier_quark_endpoint_ratio_chain_law.txt`

**Replay-time repair (2026-06-17).** The runner now uses the fast endpoint
certificate replay supplied by `frontier_quark_endpoint_readout_constraints.py`
and skips non-load-bearing refit diagnostics in its anchored-branch comparison.
The bounded chain checks and traceability checks are unchanged.

## Safe statement

The endpoint-quotient law already reduced the remaining `E`-channel primitive
to the candidate

```text
gamma_E(center)/gamma_E(shell) = 15/8.
```

This note goes one step more structural.

On the live endpoint data, three simpler endpoint ratios are all nearest to
small rationals:

```text
gamma_T(center)/gamma_T(shell) = 5/6
gamma_T(shell)/gamma_E(shell)  = -2
gamma_T(center)/gamma_E(center)= -8/9
```

These imply

```text
gamma_E(center)/gamma_E(shell)
  = [gamma_E(center)/gamma_T(center)]
    [gamma_T(center)/gamma_T(shell)]
    [gamma_T(shell)/gamma_E(shell)]
  = (-9/8) * (5/6) * (-2)
  = 15/8.
```

So the current best theory-first bounded endpoint law is no longer just one
quotient. It is a **ratio chain**:

```text
{5/6, -2, -8/9} => 15/8 => r_E = 21/4 => D_E = 21/8.
```

This is still bounded, not retained.

## 1. Exact endpoint chain identity

The endpoint coefficients already satisfy exact identities:

```text
r_E = 6 * (gamma_E(center)/gamma_E(shell) - 1)
r_T = 6 * (gamma_T(center)/gamma_T(shell) - 1).
```

And the `E` quotient itself factors exactly as

```text
gamma_E(center)/gamma_E(shell)
  = [gamma_E(center)/gamma_T(center)]
    [gamma_T(center)/gamma_T(shell)]
    [gamma_T(shell)/gamma_E(shell)].
```

So once three endpoint ratios are selected, the `E` quotient is fixed.

## 2. Controlled small-rational candidates

Inside the same low-rational endpoint class used on this branch, the nearest
candidates are:

- `gamma_T(center)/gamma_T(shell) = 5/6`
- `gamma_T(shell)/gamma_E(shell) = -2`
- `gamma_T(center)/gamma_E(center) = -8/9`

The first was already structurally privileged by the exact-support `T` law.
The new science is that the two `T/E` endpoint ratios also collapse to very
small rational candidates.

## 3. Implied E-channel law

Those three candidates force:

```text
gamma_E(center)/gamma_E(shell) = 15/8
```

and therefore

```text
r_E = 6 * (15/8 - 1) = 21/4.
```

So the earlier standalone `15/8` law is no longer an isolated rationalization.
It is the exact output of a smaller endpoint-ratio chain.

## 4. Anchored denominator candidate

Using the live shell-multiplicity candidate

```text
a_T / a_E = -2
```

together with the exact-support `T` law

```text
r_T = -1,
```

the ratio chain implies

```text
|b_E / b_T| = 21/8.
```

This remains very close to the live bounded denominator and lands on the same
anchored quark branch.

## Honest endpoint

The theorem-grade target is now narrower than before.

It is no longer simply:

> derive `gamma_E(center)/gamma_E(shell) = 15/8`.

It is:

> derive the exact endpoint ratio chain
> `{5/6, -2, -8/9}`
> from the exact Route-2 tensor observable.

If that lands, the bounded `E`-channel quotient law, the `r_E = 21/4` law,
and the anchored denominator candidate `D_E = 21/8` all follow immediately.

The audited 2026-04-28 retained no-go
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`
isolates which leg of the chain carries the irreducible obstruction: the
first leg `5/6` already coincides with the exact-support `T`-channel
quotient and the second leg `-2` is the live shell-multiplicity ratio,
but the third leg `-8/9` is exactly equivalent (under the granted
T-side conditions) to the missing E-center readout primitive that the
no-go proves the restricted Route-2 carrier class does **not** fix.

## 6. Audit traceability

This note was audited 2026-05-05 with verdict
`audited_numerical_match` (class G, `chain_closes = false`). The audit
verdict is precise: the chain-multiplication algebra from the rational
triple `{5/6, -2, -8/9}` to `gamma_E(center)/gamma_E(shell) = 15/8` and
the downstream consequences `r_E = 21/4`, `D_E = 21/8` is exact, but
the load-bearing identification of each of the three rationals is a
nearest-rational match to an imported live endpoint value rather than
a derivation from retained tensor machinery:

```text
gamma_T(center)/gamma_T(shell) = 0.833328...  --[nearest small rational]--> 5/6
gamma_T(shell)/gamma_E(shell)  = -2.005384... --[nearest small rational]--> -2
gamma_T(center)/gamma_E(center)= -0.890684... --[nearest small rational]--> -8/9
```

The re-audit guidance names the missing primitive explicitly:

```text
re_audit_target: an independent first-principles derivation of
endpoint_readout() and the exact ratio chain from the Route-2 tensor
observable.
```

The scope-narrowing companion
`QUARK_ENDPOINT_RATIO_CHAIN_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md`
isolates the within-scope content that the audit accepts as conditional
closed-form algebra (the chain identity, the chain-multiplication, and
the downstream consequences), versus the open numerical-match
identification of the three input small rationals.

A retained, audited no-go now bounds **which leg** of the chain is the
irreducible obstruction:

> [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
> (`retained_no_go`, `audited_clean`).

Read against the chain, the no-go proves the following decomposition.
After granting the conditional T-side candidates (the first two chain
legs)

```text
beta_T/alpha_T = -1   (equivalent to gamma_T(center)/gamma_T(shell) = 5/6)
alpha_T/alpha_E = -2  (equivalent to gamma_T(shell)/gamma_E(shell) = -2)
```

the third chain leg

```text
gamma_T(center)/gamma_E(center) = -8/9
```

is exactly equivalent to fixing the E-channel readout entry
`rho_E = beta_E/alpha_E = 21/4`, which the no-go proves is **not**
forced by carrier linearity, shell normalization, T-side transfer, or
low-rational naturality in the exact restricted Route-2 carrier class.
Specifically, the no-go's section 4 shows

```text
rho_E = 21/4
  <=> q_E = gamma_E(center)/gamma_E(shell) = 15/8
  <=> c_TE = gamma_T(center)/gamma_E(center) = -8/9
```

given the granted T-side values. So the chain's third leg is exactly
the missing E-center lift that the no-go bounds.

This anchors the bounded status of the chain candidate to a retained
boundary rather than leaving it as an unresolved gap. Any future
promotion of this row must either:

1. supply the additional E-center primitive named by the
   `naturality_no_go` (a source-domain rule, a tensor readout-map
   theorem beyond the restricted carrier columns, or an equivalent
   E-center lift), and only then can a derivation of the third chain
   leg `-8/9` from tensor machinery proceed; **or**
2. supply a stronger Route-2 readout primitive that derives all three
   chain legs simultaneously, retiring the nearest-rational
   identification.

Neither bridge is supplied by the current packet. The 2026-05-10
scope-narrowing companion records that the audit explicitly accepts
this scope.

The companion
`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md` sharpens this
obstruction one step further. It proves by exact rational linear algebra that
every E-center-blind endpoint repair is invariant under changing
`rho_E = beta_E/alpha_E`: shell normalization, the two T-side endpoint
candidates, channel preservation, and low-rational/naturality filters all see
the same data for all `rho_E`. Thus any positive repair of the third chain leg
must supply a genuine E-center lift, source-domain rule, or equivalent readout
primitive; another endpoint-only rational scan cannot derive `-8/9`.

The complementary single-quotient form
`QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md`
is independently audited at the same numerical-match grade; this chain
note differs from that partner by exposing the chain decomposition that
isolates `-8/9` (rather than `15/8`) as the irreducible chain leg under
the no-go.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_endpoint_ratio_chain_law.py
```

Current expected result on this branch:

- `frontier_quark_endpoint_ratio_chain_law.py`: `PASS=21 FAIL=0`

The runner now exercises an explicit `PART 5: Audit Traceability
Cross-References` block in addition to the original four parts. The
extra checks assert that the parent note exposes its 2026-05-05 audit
verdict (`audited_numerical_match`, class `G`), names the missing
first-principles derivation of `endpoint_readout()` and the chain, and
cross-references both the 2026-05-10 scope-narrowing companion and the
retained no-go
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`.
The bounded scope of the chain candidate is unchanged; the new checks
keep the bounded status formally traceable from the runner output.
