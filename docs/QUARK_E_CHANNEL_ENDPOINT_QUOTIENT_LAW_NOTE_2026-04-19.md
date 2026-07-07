---
claim_id: quark_e_channel_endpoint_quotient_law_note_2026-04-19
claim_type_author_hint: bounded_theorem
claim_scope: >-
  Conditional bounded theorem: if ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT are
  supplied, exact endpoint algebra gives r_E = 21/4 and D_E = 21/8, while the
  Route-2 no-go used at its audited no-go scope keeps ENDPOINT-QE non-derived
  by the restricted carrier class.
---

# Quark E-Channel Endpoint Quotient Law

**Date:** 2026-04-19
**Status:** conditional bounded endpoint theorem under named supplied premises
**Primary runner:** `scripts/frontier_quark_e_channel_endpoint_quotient_law.py`
**Runner cache:** `logs/runner-cache/frontier_quark_e_channel_endpoint_quotient_law.txt`

**Replay-time repair (2026-06-17).** The runner uses the fast endpoint
certificate replay supplied by `frontier_quark_endpoint_readout_constraints.py`
and skips non-load-bearing refit diagnostics in its anchored-branch comparison.
The replay is motivation-tier only; it does not supply any theorem premise.

## Safe Statement

This note does not derive the remaining quark `E`-channel readout primitive
exactly.

The claimed content is narrower: under the named supplied premises
ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT, the exact endpoint algebra gives the
conditional consequences

```text
gamma_E(center)/gamma_E(shell) = 15/8
=> r_E = beta_E/alpha_E = 21/4
=> D_E = |b_E/b_T| = 21/8.
```

The nearest-rational scan and every live endpoint value below are a motivation
exhibit only. They are not consumed by the claim.

## Named Conditional Premises

```text
ENDPOINT-QE (named conditional premise): the E-channel center/shell endpoint
quotient is SUPPLIED as gamma_E(center)/gamma_E(shell) = 15/8; equivalently
rho_E = beta_E/alpha_E = 21/4 (rho_E is written r_E in the endpoint notes)
via the exact identity rho_E = 6*(q_E - 1); equivalently, granted ENDPOINT-RT
and SHELL-MULT, the center ratio gamma_T(center)/gamma_E(center) = -8/9.
Not derived: the no-go note
QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md, used at
its audited no-go scope, proves the restricted Route-2 carrier/readout class
leaves rho_E free unless an additional E-center endpoint ratio,
source-domain, or readout-map primitive is supplied.

ENDPOINT-RT (named conditional premise): the T-channel center/shell endpoint
quotient is SUPPLIED as gamma_T(center)/gamma_T(shell) = 5/6; equivalently
r_T = beta_T/alpha_T = -1.

SHELL-MULT (named conditional premise): the shell coefficient ratio
(historically the shell-multiplicity candidate) is SUPPLIED as
a_T/a_E = alpha_T/alpha_E = -2.
```

## Exact Identities

The endpoint coefficients satisfy exact affine endpoint identities:

```text
gamma_E(delta_A1) = a_E + b_E delta_A1
gamma_T(delta_A1) = a_T + b_T delta_A1
delta_A1(center)  = 1/6
delta_A1(shell)   = 0
```

Therefore, with

```text
q_E := gamma_E(center)/gamma_E(shell)
q_T := gamma_T(center)/gamma_T(shell)
r_E := b_E/a_E
r_T := b_T/a_T
```

the unconditional endpoint identities are

```text
r_E = 6 * (q_E - 1)
r_T = 6 * (q_T - 1).
```

The denominator identity is also exact once the ratios are supplied:

```text
b_E/b_T = (r_E a_E)/(r_T a_T).
```

No numerical scan is needed for these identities.

## Conditional Chain

Under ENDPOINT-QE,

```text
q_E = 15/8
r_E = 6 * (15/8 - 1) = 21/4.
```

Under ENDPOINT-RT,

```text
q_T = 5/6
r_T = 6 * (5/6 - 1) = -1.
```

Under SHELL-MULT,

```text
a_T/a_E = -2.
```

Combining those exact relations gives

```text
b_E/b_T
  = (r_E a_E)/(r_T a_T)
  = ((21/4) a_E)/((-1)(-2 a_E))
  = 21/8.
```

Thus the bounded theorem claimed here is conditional only:

```text
ENDPOINT-QE + ENDPOINT-RT + SHELL-MULT
=> r_E = 21/4
=> D_E = |b_E/b_T| = 21/8.
```

## Premise Readout Matrix Check

Under the supplied premises, the runner checks this displayed readout map
independently over exact rational arithmetic:

```text
P_R^prem = [[1, 0, 21/4, 0],
            [0, -2, 0, 2]]

E-shell  = (1, 0, 0, 0) -> (1, 0)
E-center = (1, 0, 1/6, 0) -> (15/8, 0)
T-shell  = (0, 1, 0, 0) -> (0, -2)
T-center = (0, 1, 0, 1/6) -> (0, -5/3)
```

Those endpoint images recompute `q_E = 15/8`, `q_T = 5/6`, and
`c_TE = gamma_T(center)/gamma_E(center) = -8/9` by two independent routes:
the direct image ratio and the quotient identity `s_TE*q_T/q_E`.

## Motivation Exhibit

Evidence only; not load-bearing; no value below is consumed by any claim.

The live endpoint replay motivating the supplied premises has historically
printed:

```text
gamma_T(center)/gamma_T(shell) = 0.833328...       near 5/6
gamma_E(center)/gamma_E(shell) = 1.876246130347... near 15/8
|b_E/b_T|                         = 2.621601...    near 21/8
```

The bounded scan searched a controlled low-rational class:

```text
numerator <= 96
denominator <= 32
no wider expression grammar
```

Within that scan, `15/8 = 1.875` was the nearest low-rational candidate to the
live `E`-channel quotient, with relative gap about `0.066%`. The corresponding
`21/8` denominator is about `0.13%` from the live bounded denominator and is
closer than the older direct `sqrt(7)` proxy.

These facts remain useful motivation for why ENDPOINT-QE was named, but they
do not derive ENDPOINT-QE, ENDPOINT-RT, SHELL-MULT, `r_E = 21/4`, or
`D_E = 21/8`.

## Unconditional Boundary

The no-go boundary used here is
[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md][no-go],
used at its audited no-go scope.

Section 6 of the no-go note, quoted verbatim:

```text
**Theorem (Route-2 E-channel readout naturality no-go).** In the exact
restricted Route-2 carrier/readout class, after granting the conditional
T-side candidates

beta_T/alpha_T = -1,
alpha_T/alpha_E = -2,

the E-channel readout entry

rho_E = beta_E/alpha_E

remains a free parameter unless an additional E-center endpoint ratio,
source-domain, or readout-map primitive is supplied. The value `rho_E = 21/4`
is equivalent to the endpoint ratio `gamma_T(center)/gamma_E(center) = -8/9`
under the granted T-side conditions, but it is not derived by carrier
linearity, shell normalization, T-side transfer, or low-rational naturality
alone.
```

Section 4 of the no-go note, quoted verbatim:

```text
rho_E = 21/4,
q_E = gamma_E(center)/gamma_E(shell) = 15/8,
c_TE = gamma_T(center)/gamma_E(center) = -8/9
```

given the granted T-side values `q_T = 5/6` and
`gamma_T(shell)/gamma_E(shell) = -2`.

Therefore this note's conditional algebra is compatible with the no-go only
because ENDPOINT-QE is named as a supplied premise, not as a derived theorem.

Context only (audited_conditional); not load-bearing for this row. The
companion
[QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md][e-blind]
closes a broader false repair route. It proves that any endpoint repair which
is blind to the E-center column leaves `rho_E = beta_E/alpha_E` free, even
after shell normalization, the two T-side endpoint candidates, channel
preservation, and low-rational/naturality filters are granted. Therefore the
quotient target `15/8` cannot be derived by another shell-only or T-side
rationalization; a positive repair must add a real E-center lift or equivalent
source/readout primitive.

## Residuals / Open Derivation Targets

The open theorem targets remain:

1. derive ENDPOINT-QE, equivalently derive the E-center endpoint ratio or a
   stronger readout/source-domain primitive that fixes `rho_E = 21/4`;
2. derive ENDPOINT-RT if a future row needs it without a supplied premise;
3. derive SHELL-MULT from shell-counting algebra if a future row needs the
   denominator law without a supplied premise.

Until those land through retained-grade rows, this note can only be cited for
the exact conditional consequences under the named premises and for the
unconditional no-go boundary.

## Citation Contract (Audit-Gated)

This row may be cited only as:

```text
Under ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT, exact endpoint algebra gives
r_E = 21/4 and D_E = 21/8; the Route-2 naturality no-go, used at its
audited no-go scope, proves that ENDPOINT-QE is not derived by the restricted
carrier/readout class.
```

It may not be cited as a derivation of `gamma_E(center)/gamma_E(shell) = 15/8`,
`a_T/a_E = -2`, `gamma_T(center)/gamma_T(shell) = 5/6`, `rho_E = 21/4`, or
the anchored quark branch.

### Audit history preserved

This note was audited 2026-05-05 with verdict `audited_numerical_match`
(class G, `chain_closes = false`). The audit verdict is precise: the
closed-form algebra from `q_E = 15/8` to `r_E = 21/4` and `D_E = 21/8` is
exact, but the load-bearing identification `q_E = 15/8` was a nearest-rational
match to an imported live endpoint value
`gamma_E(center)/gamma_E(shell) = 1.876246...` rather than a derivation from
retained tensor machinery. The re-audit guidance named two missing bridge
theorems explicitly:

```text
missing_bridge_theorem: provide a retained first-principles derivation
of gamma_E(center)/gamma_E(shell) = 15/8, and separately close the
a_T/a_E = -2 bridge before promoting the denominator law.
```

The scope-narrowing companion
[QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md][e-scope]
isolates the within-scope content that the audit accepts as conditional
closed-form algebra, versus the two named missing bridge theorems that would
be required to promote the row.

#### 2026-07-07 recut

This recut re-types the matched values as supplied named premises. ENDPOINT-QE,
ENDPOINT-RT, and SHELL-MULT now carry the conditional inputs; the exact
algebra under those premises is the load-bearing bounded theorem. The live
endpoint replay and nearest-rational scan are kept only as a motivation
exhibit.

The permitted ledger greps on 2026-07-07 found retained Route-2 readout-map
and time-coupling rows, but their scoped claims carry the restricted
readout/time-coupling algebra and obstruction, not derivations of ENDPOINT-RT
or SHELL-MULT. No T-side endpoint value is cited here as retained-derived.

[no-go]: QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md
[e-blind]: QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md
[e-scope]: QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md

## Firewall

Forbidden uses:

1. observed quark masses;
2. fitted Yukawa values;
3. minimizing CKM/`J` error against the live quark target;
4. selecting the nearest rational to the live E-channel endpoint as if that
   were a derivation;
5. adding a hidden E-center source weight;
6. citing ENDPOINT-QE, ENDPOINT-RT, or SHELL-MULT as derived, selected, or
   natural.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_e_channel_endpoint_quotient_law.py
```

Expected result after the 2026-07-07 recut:

```text
MOTIVATION-TIER (non-load-bearing; does not affect exit status)
MOTIVATION: PASS=13 FAIL=0
TOTAL: PASS=31 FAIL=0
```

The final `TOTAL` line is load-bearing only. The runner separately reports
the motivation-tier scan/replay checks, verifies the displayed premise matrix
and endpoint images, checks the no-go quote and scope links, and prints a final
declaration that the premises are supplied and not claimed as derived.
