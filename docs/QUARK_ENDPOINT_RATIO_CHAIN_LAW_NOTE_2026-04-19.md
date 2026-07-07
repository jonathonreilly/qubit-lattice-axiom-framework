---
claim_id: quark_endpoint_ratio_chain_law_note_2026-04-19
claim_type_author_hint: bounded_theorem
claim_scope: >-
  Conditional bounded theorem: if ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT are
  supplied, exact endpoint-chain algebra maps {5/6, -2, -8/9} to q_E = 15/8,
  r_E = 21/4, and D_E = 21/8, while the Route-2 no-go used at its audited
  no-go scope keeps the E-center leg non-derived.
---

# Quark Endpoint Ratio-Chain Law

**Date:** 2026-04-19
**Status:** conditional bounded endpoint-ratio-chain theorem under named
supplied premises
**Type:** bounded_theorem
**Primary runner:** `scripts/frontier_quark_endpoint_ratio_chain_law.py`
**Runner cache:** `logs/runner-cache/frontier_quark_endpoint_ratio_chain_law.txt`

**Replay-time repair (2026-06-17).** The runner uses the fast endpoint
certificate replay supplied by `frontier_quark_endpoint_readout_constraints.py`
and skips non-load-bearing refit diagnostics in its anchored-branch comparison.
The replay is motivation-tier only; it does not supply any theorem premise.

## Safe Statement

This note does not derive the exact Route-2 tensor readout law or any of the
three endpoint-ratio inputs.

The claimed content is narrower: under the named supplied premises
ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT, the exact endpoint-chain algebra gives

```text
{5/6, -2, -8/9} => q_E = 15/8 => r_E = 21/4 => D_E = 21/8.
```

The chain maps exactly as follows:

```text
5/6  maps to ENDPOINT-RT.
-2   maps to SHELL-MULT.
-8/9 maps to the ENDPOINT-QE equivalence granted ENDPOINT-RT and SHELL-MULT.
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

The endpoint coefficients satisfy the unconditional endpoint identities

```text
r_E = 6 * (gamma_E(center)/gamma_E(shell) - 1)
r_T = 6 * (gamma_T(center)/gamma_T(shell) - 1).
```

The `E` quotient also factors exactly as

```text
gamma_E(center)/gamma_E(shell)
  = [gamma_E(center)/gamma_T(center)]
    [gamma_T(center)/gamma_T(shell)]
    [gamma_T(shell)/gamma_E(shell)].
```

No numerical scan is needed for these identities.

## Conditional Chain

Under ENDPOINT-RT,

```text
gamma_T(center)/gamma_T(shell) = 5/6.
```

Under SHELL-MULT,

```text
gamma_T(shell)/gamma_E(shell) = a_T/a_E = -2.
```

Under ENDPOINT-QE, granted ENDPOINT-RT and SHELL-MULT,

```text
gamma_T(center)/gamma_E(center) = -8/9
gamma_E(center)/gamma_T(center) = -9/8.
```

Therefore the exact chain closes:

```text
gamma_E(center)/gamma_E(shell)
  = (-9/8) * (5/6) * (-2)
  = 15/8.
```

Then the exact endpoint identity gives

```text
r_E = 6 * (15/8 - 1) = 21/4.
```

Together with ENDPOINT-RT and SHELL-MULT,

```text
b_E/b_T
  = (r_E a_E)/(r_T a_T)
  = ((21/4) a_E)/((-1)(-2 a_E))
  = 21/8.
```

Thus the bounded theorem claimed here is conditional only:

```text
ENDPOINT-QE + ENDPOINT-RT + SHELL-MULT
=> {5/6, -2, -8/9} => q_E = 15/8
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
gamma_T(center)/gamma_T(shell) = 0.833328...  near 5/6
gamma_T(shell)/gamma_E(shell)  = -2.005384... near -2
gamma_T(center)/gamma_E(center)= -0.890684... near -8/9
gamma_E(center)/gamma_E(shell) = 1.876246...  near 15/8
```

The bounded low-rational endpoint scan found the nearest candidates

```text
gamma_T(center)/gamma_T(shell) = 5/6
gamma_T(shell)/gamma_E(shell)  = -2
gamma_T(center)/gamma_E(center)= -8/9
```

and those candidates multiply exactly to `15/8`. The scan is kept because
it motivates why the three premises were named, but it does not derive any
member of the chain.

## Unconditional Boundary

The no-go boundary used here is
[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md][no-go],
used at its audited no-go scope.

The load-bearing non-derivation boundary is
[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md).

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

Read against the chain, the no-go proves that the third leg

```text
gamma_T(center)/gamma_E(center) = -8/9
```

is exactly equivalent to fixing `rho_E = 21/4` under the granted T-side
conditions. This is why the `-8/9` chain leg is carried only through the
ENDPOINT-QE premise and is not claimed as a derived endpoint-ratio theorem.

The companion
[QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md][e-blind]
is context only here. It is not consumed as load-bearing support for this row.

## Residuals / Open Derivation Targets

The open theorem targets remain:

1. derive ENDPOINT-QE, equivalently derive the `-8/9` E-center chain leg or a
   stronger readout/source-domain primitive that fixes `rho_E = 21/4`;
2. derive ENDPOINT-RT if a future row needs the `5/6` leg without a supplied
   premise;
3. derive SHELL-MULT if a future row needs the `-2` shell leg without a
   supplied premise;
4. derive the full endpoint ratio chain from retained Route-2 tensor
   machinery.

Until those land through retained-grade rows, this note can only be cited for
the exact conditional chain under the named premises and for the unconditional
no-go boundary.

## Citation Contract (Audit-Gated)

This row may be cited only as:

```text
Under ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT, exact endpoint-chain algebra
maps {5/6, -2, -8/9} to q_E = 15/8, r_E = 21/4, and D_E = 21/8; the Route-2
naturality no-go, used at its audited no-go scope, proves that the E-center leg
is not derived by the restricted carrier/readout class.
```

It may not be cited as a derivation of the ratio chain, of any chain leg, of
`gamma_E(center)/gamma_E(shell) = 15/8`, of `rho_E = 21/4`, or of the anchored
quark branch.

### Audit history preserved

This note was audited 2026-05-05 with verdict `audited_numerical_match`
(class G, `chain_closes = false`). The audit verdict is precise: the
chain-multiplication algebra from the rational triple `{5/6, -2, -8/9}` to
`gamma_E(center)/gamma_E(shell) = 15/8` and the downstream consequences
`r_E = 21/4`, `D_E = 21/8` is exact, but the load-bearing identification of
each of the three rationals was a nearest-rational match to an imported live
endpoint value rather than a derivation from retained tensor machinery:

```text
gamma_T(center)/gamma_T(shell) = 0.833328...  --[nearest small rational]--> 5/6
gamma_T(shell)/gamma_E(shell)  = -2.005384... --[nearest small rational]--> -2
gamma_T(center)/gamma_E(center)= -0.890684... --[nearest small rational]--> -8/9
```

The re-audit guidance named the missing primitive explicitly:

```text
re_audit_target: an independent first-principles derivation of
endpoint_readout() and the exact ratio chain from the Route-2 tensor
observable.
```

The scope-narrowing companion
[QUARK_ENDPOINT_RATIO_CHAIN_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md][ratio-scope]
isolates the within-scope content that the audit accepts as conditional
closed-form algebra (the chain identity, the chain multiplication, and the
downstream consequences), versus the open numerical-match identification of
the three input small rationals.

#### 2026-07-07 recut

This recut re-types the matched values as supplied named premises. ENDPOINT-RT
carries the `5/6` chain leg, SHELL-MULT carries the `-2` chain leg, and
ENDPOINT-QE carries the `-8/9` E-center equivalence when ENDPOINT-RT and
SHELL-MULT are granted. The exact chain algebra under those premises is the
load-bearing bounded theorem. The live endpoint replay and nearest-rational
scan are kept only as a motivation exhibit.

The permitted ledger greps on 2026-07-07 found retained Route-2 readout-map
and time-coupling rows, but their scoped claims carry the restricted
readout/time-coupling algebra and obstruction, not derivations of ENDPOINT-RT
or SHELL-MULT. No T-side endpoint value is cited here as retained-derived.

The complementary single-quotient form
[QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md][quotient-note]
is recut with the same named premise block and the same no-go boundary.

[no-go]: QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md
[e-blind]: QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md
[ratio-scope]: QUARK_ENDPOINT_RATIO_CHAIN_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md
[quotient-note]: QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md

## Firewall

Forbidden uses:

1. observed quark masses;
2. fitted Yukawa values;
3. minimizing CKM/`J` error against the live quark target;
4. selecting the nearest rational to a live endpoint ratio as if that were a
   derivation;
5. adding a hidden E-center source weight;
6. citing ENDPOINT-QE, ENDPOINT-RT, or SHELL-MULT as derived, selected, or
   natural;
7. citing the named premises as derived.

The named premises may not be cited as derived.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_endpoint_ratio_chain_law.py
```

Expected result after the 2026-07-07 recut:

```text
MOTIVATION-TIER (non-load-bearing; does not affect exit status)
MOTIVATION: PASS=9 FAIL=0
TOTAL: PASS=32 FAIL=0
```

The final `TOTAL` line is load-bearing only. The runner separately reports
the motivation-tier scan/replay checks, verifies the displayed premise matrix
and endpoint images, checks the no-go quote and scope links, and prints a final
declaration that the premises are supplied and not claimed as derived.
