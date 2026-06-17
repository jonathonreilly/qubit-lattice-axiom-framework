# Hierarchy B4 Determinant-Only Factor-Signature No-Go

**Date:** 2026-06-17
**Claim type:** no_go
**Claim-strength label:** exact boundary theorem on open gate
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome, does not edit the audit ledger, and
does not change any effective status.
**Primary runner:**
[`scripts/frontier_hierarchy_b4_determinant_only_factor_signature_no_go_2026_06_17.py`](../scripts/frontier_hierarchy_b4_determinant_only_factor_signature_no_go_2026_06_17.py)

## Purpose

This note sharpens the B4 hierarchy-formula blocker in
[`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md).
The existing source packet already computes the minimal-block determinant
surface and states that B4 remains open:

```text
determinant side: u_0^16
hierarchy formula side: alpha_LM^16 = alpha_bare^16 u_0^(-16)
```

The exact boundary proved here is narrower than the open B4 problem. It
rules out only a determinant-only repair of B4: finite products, powers,
or quotients of the checked determinant-degree factor cannot supply the
`alpha_bare^16` coupling-power content required by `alpha_LM^16`.

Non-determinant attachment-observable routes remain open. In particular,
the named B4 target in
[`HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md`](HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md)
is still the identification of a ratio-normalized log-partition,
determinant, or readout observable in which one taste decoupling
contributes the required coupling factor multiplicatively.

## Theorem

Let the factor signature of a monomial be

```text
sig(C alpha_bare^a u_0^b) = (a, b),
```

where `C` is independent of `alpha_bare` and `u_0`. The checked
minimal-block determinant side gives

```text
|det(u_0 D)|_{m=0} = 4^8 u_0^16,
sig(u_0^16) = (0, 16).
```

The hierarchy-formula coupling power gives

```text
alpha_LM^16 = (alpha_bare / u_0)^16,
sig(alpha_LM^16) = (16, -16).
```

Therefore no determinant-only expression generated from the determinant
degree and constants independent of `alpha_bare` can equal
`alpha_LM^16` as an identity in the independent symbols
`alpha_bare` and `u_0`. Even if quotient operations are allowed, the
alpha exponent of every determinant-only expression stays zero.

Relative to the stripped determinant factor, the exact missing
transport multiplier is

```text
alpha_LM^16 / u_0^16
  = alpha_bare^16 u_0^(-32)
  = (alpha_bare / u_0^2)^16
  = alpha_s^16.
```

Thus the determinant supplies the taste count and the `u_0^16` side of
the bookkeeping identity, but a B4 closure still needs an independent
attachment-observable rule supplying one `alpha_s` factor per taste
decoupling, or an equivalent non-determinant mechanism with the same
factor signature.

## Consequence for B4

This packet prunes the following route:

```text
"The minimal-block determinant carries degree 16, therefore it supplies
alpha_LM^16."
```

That route is false at the factor-signature level. The determinant
degree is useful support for the species/taste side of the hierarchy
lane, but it is not a coupling-power transport theorem.

The live B4 target is now forced into a sharper form:

```text
Find a framework-native attachment observable whose per-taste
contribution carries alpha_s = alpha_bare u_0^(-2), or prove a
different non-determinant transport rule with signature (16, -32)
relative to u_0^16.
```

This statement is not a global no-go for B4. It does not rule out
strong-coupling one-link observables, beyond-mean-field link
fluctuations, Green-kernel readout dressing, or any outside-K1-K8
observable named as surviving route families in the delta-zero gate
packet. It only prevents determinant-degree evidence from being treated
as if it were the missing coupling-power transport.

## Non-Claims

This note does not claim:

- an EW VEV prediction;
- hierarchy formula closure;
- a derivation of `M_Pl`, `u_0`, `alpha_bare`, `alpha_s`, or
  `alpha_LM`;
- a new axiom, primitive, or textbook import;
- an audit verdict or ledger status change;
- exhaustion of every possible future B4 mechanism.

## Verification

Run:

```bash
python3 scripts/frontier_hierarchy_b4_determinant_only_factor_signature_no_go_2026_06_17.py
```

Expected result:

```text
VERDICT: hierarchy B4 determinant-only factor-signature no-go checks pass.
TOTAL: PASS=N, FAIL=0
```
