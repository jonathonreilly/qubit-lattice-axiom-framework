---
claim_id: s3_time_primitive_chain_note
claim_type_author_hint: bounded_theorem
claim_scope: >-
  Conditional bounded theorem: exact primitive-chain reductions and unconditional
  no-go boundary used at its audited no-go scope, with P_R and Xi_R pinned only
  under ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT.
---

# Primitive Chain Readout and Time-Coupling Update

**Type:** bounded_theorem
**Date:** 2026-04-19
**Primary runner:** [`frontier_s3_time_primitive_chain_reaudit.py`][runner]
**Purpose:** restate the remaining Route-2 primitives as exact reductions plus
named-premise conditional algebra, with the no-go boundary preserved at its
audited no-go scope.

No new axiom, primitive, bridge, or Tier-A content is introduced here; the named
supplied premises below are conditional assumptions of this packet, not new
registered structure.

## Safe statement

This packet is a bounded conditional theorem, not a derivation of the endpoint
ratio triple. Its load-bearing content is:

1. the unconditional primitive-chain reductions P0 through P3 on the existing
   Route-2 carrier/readout/time stack;
2. the conditional pinning of the normalized readout map P_R and the coupling
   family Xi_R under the named supplied premises ENDPOINT-QE, ENDPOINT-RT, and
   SHELL-MULT;
3. the unconditional boundary that the restricted Route-2 carrier/readout class
   leaves rho_E free unless an additional E-center endpoint ratio,
   source-domain, or readout-map primitive is supplied.

Primitive P4, the Einstein/Regge identification, stays open and outside the
claim.

## Named conditional premises

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

These premises are supplied conditions only. They are not derived, selected, or
naturalized by this packet.

## Exact identities

The exact Route-2 stack already supplies the following primitive-chain objects.

### Primitive P0: kinematic scaffold

- `PL S^3 x R`
- **Status:** exact upstream scaffold

### Primitive P1: bilinear microscopic carrier

- `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`
- **Status:** exact reduction exists

On the live support surface the endpoint carrier columns are:

```text
E-shell  = (1, 0, 0,   0)
E-center = (1, 0, 1/6, 0)
T-shell  = (0, 1, 0,   0)
T-center = (0, 1, 0, 1/6)
```

### Primitive P2: restricted readout map

The exact carrier/readout reduction gives the channelwise class:

```text
gamma_E = alpha_E u_E + beta_E delta_A1 u_E
gamma_T = alpha_T u_T + beta_T delta_A1 u_T

P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]]
```

Its endpoint identities are unconditional algebra:

```text
q_T  := gamma_T(center) / gamma_T(shell)
     = 1 + (beta_T / alpha_T) / 6

q_E  := gamma_E(center) / gamma_E(shell)
     = 1 + (beta_E / alpha_E) / 6

s_TE := gamma_T(shell) / gamma_E(shell)
     = alpha_T / alpha_E

c_TE := gamma_T(center) / gamma_E(center)
     = s_TE * q_T / q_E
```

Therefore the supplied endpoint triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)
```

is exactly equivalent to:

```text
q_T = 5/6
s_TE = -2
q_E = 15/8
c_TE = -8/9
```

This equivalence is exact algebra. It is not a derivation of any member of the
triple.

### Primitive P3: readout-to-slice coupling family

For any specified admissible P_R on the restricted class, the coupling family is:

```text
Xi_R(t ; c) = (P_R c) tensor exp(-t Lambda_R) u_*
```

The time-coupling authority writes this object `Xi_P`; this packet keeps its
original `Xi_R` symbol for the same object.

This is an exact conditional family over the cited readout and slice-semigroup
authorities. The unique theorem is not claimed without a derived P_R.

### Primitive P4: final Einstein/Regge identification

- identify the exact carrier/readout/coupling package with the final
  Einstein/Regge tensor law on the current restricted class
- **Status:** open and outside this claim

## Conditional chain

Under ENDPOINT-RT:

```text
gamma_T(center) / gamma_T(shell) = 5/6
beta_T / alpha_T = 6*(5/6 - 1) = -1
```

Under SHELL-MULT:

```text
alpha_T / alpha_E = -2
```

Under ENDPOINT-QE:

```text
gamma_E(center) / gamma_E(shell) = 15/8
beta_E / alpha_E = 6*(15/8 - 1) = 21/4
```

Thus, in the normalized shell gauge `alpha_E = 1`, the supplied-premise readout
map is pinned to:

```text
P_R^prem =
[[1, 0, 21/4, 0],
 [0, -2, 0, 2]]
```

The endpoint images then check exactly:

```text
P_R^prem E-shell  = (1, 0)
P_R^prem E-center = (15/8, 0)
P_R^prem T-shell  = (0, -2)
P_R^prem T-center = (0, -5/3)
```

Consequently:

```text
gamma_T(center) / gamma_T(shell) = (-5/3)/(-2) = 5/6
gamma_T(shell) / gamma_E(shell) = -2
gamma_T(center) / gamma_E(center) = (-5/3)/(15/8) = -8/9
```

Under the same named premises, the coupling family is pinned to:

```text
Xi_R^prem(t ; c) = (P_R^prem c) tensor exp(-t Lambda_R) u_*
```

This is the conditional bounded theorem. It does not derive ENDPOINT-QE,
ENDPOINT-RT, SHELL-MULT, P4, or a unique readout-to-slice theorem without the
named premises.

## Motivation exhibit

This section is evidence only; not load-bearing; no value below is consumed by
any claim.

The nearest-rational scan and live endpoint-fixed replay are kept only as
motivation-tier context. They are not proof inputs.

```text
live beta_T / alpha_T = -1.000030814262
live alpha_T / alpha_E = -2.005382749600
live beta_E / alpha_E = 5.257476782081

live q_T  = 0.833328197623
live s_TE = -2.005382749600
live c_TE = -0.890683778231
```

The nearby exact values

```text
q_T = 5/6
s_TE = -2
c_TE = -8/9
q_E = 15/8
beta_E / alpha_E = 21/4
```

are treated here only as supplied-premise values when the named premises are
explicitly invoked. The scan does not select them for theorem use.

## Unconditional boundary

The no-go boundary used here is
[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md][no-go]
and it is used at its audited no-go scope.

The load-bearing non-derivation boundary is
[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md).

Section 6 of the no-go note, quoted verbatim:

````text
**Theorem (Route-2 E-channel readout naturality no-go).** In the exact
restricted Route-2 carrier/readout class, after granting the conditional
T-side candidates

```text
beta_T/alpha_T = -1,
alpha_T/alpha_E = -2,
```

the E-channel readout entry

```text
rho_E = beta_E/alpha_E
```

remains a free parameter unless an additional E-center endpoint ratio,
source-domain, or readout-map primitive is supplied. The value `rho_E = 21/4`
is equivalent to the endpoint ratio `gamma_T(center)/gamma_E(center) = -8/9`
under the granted T-side conditions, but it is not derived by carrier
linearity, shell normalization, T-side transfer, or low-rational naturality
alone.
````

Section 4 of the no-go note, quoted verbatim:

````text
The target value is equivalent to any of these exact statements:

```text
rho_E = 21/4,
q_E = gamma_E(center)/gamma_E(shell) = 15/8,
c_TE = gamma_T(center)/gamma_E(center) = -8/9
```

given the granted T-side values `q_T = 5/6` and
`gamma_T(shell)/gamma_E(shell) = -2`.
````

For this row, the boundary is unconditional: the current restricted objects do
not uniquely select `beta_E / alpha_E = 21/4`. The value remains supplied by
ENDPOINT-QE until a new retained derivation supplies an additional E-center
endpoint ratio, source-domain, or readout-map primitive.

The no-go is not an exhaustive theorem against all possible readout primitives.
It is a boundary for the restricted Route-2 carrier/readout class.

## Residuals / open derivation targets

The remaining positive-science target is:

> derive an additional E-center endpoint ratio, source-domain, or readout-map
> primitive that supplies rho_E = beta_E / alpha_E = 21/4 without importing the
> live endpoint scan.

The dependency ranking remains:

1. exact readout map P_R beyond supplied-premise pinning;
2. exact readout-to-slice coupling theorem without supplied P_R;
3. final Einstein/Regge identification.

P4 is open. The conditional package here must not be used as P4 closure.

## Citation contract (audit-gated)

Audit-gated citations may cite:

- the exact Route-2 carrier/readout/time authority chain;
- the unconditional reduced-family algebra and endpoint identities;
- the conditional readout/coupling package only when ENDPOINT-QE, ENDPOINT-RT,
  and SHELL-MULT are named as supplied premises;
- the no-go boundary for the restricted Route-2 carrier/readout class.

Audit-gated citations may not cite audited_conditional or unaudited rows as
load-bearing authority. In particular,
`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md` is context only
unless a later retained-grade audit changes its status.

### Upstream authorities (Route-2 theorem notes)

- [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) -
  exact bilinear carrier `K_R` and restricted bright readout class `P_R`.
- [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md) -
  exact slice backbone `Lambda_R` and one-step transfer
  `T_R = exp(-Lambda_R)`.
- [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) -
  no-go boundary for non-selection of `beta_E / alpha_E = 21/4`.

## Downstream source-boundary firewall

Allowed downstream uses of this packet are limited to:

- cite the exact Route-2 carrier/readout/time authority chain;
- cite the reduced-family algebra showing that `rho_E = 21/4` gives
  `q_E = 15/8` and, under the granted T-side data, center `T/E = -8/9`;
- cite the admissibility boundary that the current restricted
  carrier/readout class leaves `beta_E / alpha_E` free;
- cite the open positive target: derive an additional E-center endpoint ratio,
  source-domain, or readout-map primitive;
- cite the conditional readout/coupling package under the named premises
  ENDPOINT-QE, ENDPOINT-RT, SHELL-MULT at its stated scope.

Forbidden downstream uses without a new retained bridge:

- do not cite this packet as a derivation of `beta_E / alpha_E = 21/4`;
- do not cite it as a unique readout-to-slice time-coupling theorem;
- do not cite it as final Einstein/Regge identification;
- do not cite the granted T-side candidates as selecting the E-channel ratio;
- do not use the Route-2 no-go as an exhaustive no-go against all possible
  readout primitives;
- do not promote this packet to a positive readout theorem unless a new
  E-center/source/readout primitive is supplied;
- the 2026-07-07 recut re-types this packet as a conditional bounded theorem;
  promotion to a positive or unconditional readout theorem still requires a new
  retained E-center/source/readout primitive;
- the named premises may not be cited as derived.

Re-audit should be triggered if a downstream row uses this packet as a positive
readout theorem, as a derivation of the `21/4` E-channel entry, as closure of
the Route-2 readout-to-slice time-coupling theorem, or as a derivation of any
named premise. Promotion to a positive or unconditional readout theorem still
requires a new retained E-center/source/readout primitive.

## Audit history

### 2026-05-28 Repair Boundary

Earlier review found that the full positive theorem still does not close
because the readout map `P_R`, specifically `beta_E / alpha_E = 21/4`, is left
open. The narrow repair target was either to derive
`beta_E / alpha_E = 21/4` from the restricted primitive-chain objects or to
prove an admissibility boundary showing why the current restricted class cannot
select it uniquely.

That split remains preserved:

- **Load-bearing after this recut:** exact reductions, exact endpoint algebra,
  and conditional consequences under named supplied premises.
- **Not load-bearing:** the live match, nearest-rational scan, and any claim
  that the current Route-2 objects derive `beta_E / alpha_E = 21/4`.

### 2026-07-07 Recut Boundary

This recut re-types the audited clean open-gate row as a bounded conditional
theorem. The formerly matched endpoint values are re-typed as the named supplied
premises ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT. The load-bearing claim is now
the exact conditional algebra under those premises plus the unconditional
no-go boundary. The positive target remains open: derive an additional
E-center endpoint ratio, source-domain, or readout-map primitive.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py
```

Expected result:

```text
S3 primitive-chain conditional bounded-theorem re-audit helper
LOAD-BEARING: PASS=33 FAIL=0
MOTIVATION-TIER (non-load-bearing; does not affect exit status)
MOTIVATION: PASS=7 FAIL=0
TOTAL: PASS=33 FAIL=0
VERDICT: conditional bounded theorem checks passed; motivation is non-fatal.
```

[runner]: ../scripts/frontier_s3_time_primitive_chain_reaudit.py
[readout-map]: QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md
[time-coupling]: QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md
[no-go]: QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md
