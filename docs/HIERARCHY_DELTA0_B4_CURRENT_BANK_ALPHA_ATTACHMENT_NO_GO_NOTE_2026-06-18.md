# Hierarchy DELTA0 B4 Current-Bank Alpha-Attachment No-Go

**Date:** 2026-06-18
**Claim type:** no_go
**Claim-strength label:** exact current-bank no-go theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome, does not edit the audit ledger, and
does not change any effective status.
**Primary runner:** [`scripts/frontier_hierarchy_delta0_b4_current_bank_alpha_attachment_no_go_2026_06_18.py`](../scripts/frontier_hierarchy_delta0_b4_current_bank_alpha_attachment_no_go_2026_06_18.py)

## Target

The current audited conditional blocker for
[`HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md`](HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md)
is not the arithmetic identity

```text
u_0^16 alpha_s^16 = alpha_LM^16.
```

The blocker is the missing theorem identifying a ratio-normalized block
readout in which one decoupling taste contributes

```text
alpha_s = alpha_bare u_0^-2
```

multiplicatively. This note does not supply that positive attachment
theorem. It proves the narrower negative boundary needed for the
current bank: the already-enumerated K1-K8 candidate bank cannot be
read as that theorem.

## Current-Bank Theorem

Use the factor signature

```text
sig(C alpha_bare^a u_0^b) = (a, b),
```

where `C` is independent of `alpha_bare` and `u_0`. The current B4
candidate bank is the K1-K8 enumeration of
[`HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_NOTE_2026-06-11.md`](HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_NOTE_2026-06-11.md).
For the attachment question its rows split into two classes.

1. Genuine candidate readouts. These are determinant/share,
   Matsubara-density, static-potential, plaquette-action, equal-share,
   threshold-exponential, and BZ log-det readouts. They are observable
   mechanisms, but none carries a native `alpha_bare` generator; their
   alpha exponent is zero.
2. Supplier-chain scalar rows. These contain `1/(4 pi)`, `alpha_bare`,
   or `alpha_s` by construction, but they are not identified block
   readout mechanisms. The two K2 match-window cells equal `alpha_s`
   because the grid row is the supplier-chain identity itself.

Therefore every finite product, quotient, or integer power made only
from genuine current-bank readouts and constants independent of
`alpha_bare` keeps alpha exponent zero. It cannot equal the required
per-taste attachment factor

```text
sig(alpha_s) = sig(alpha_bare u_0^-2) = (1, -2),
```

and it cannot supply the sixteen-taste transport multiplier

```text
sig(alpha_s^16) = (16, -32).
```

If an expression reaches those signatures by inserting the alpha-bearing
supplier-chain rows, then the expression has inserted exactly the
missing coupling supplier as an external scalar. That is bookkeeping,
not an attachment-observable identification.

## Consequence

This no-go prunes the route:

```text
The existing K1-K8 bank already contains a mechanistic alpha_s
per-taste attachment once products, quotients, or ratio normalizations
are allowed.
```

That route is false at the factor-signature and mechanism-class level.
The current bank contains either genuine readout mechanisms with alpha
exponent zero, or alpha-bearing supplier-chain identities with no
readout mechanism. It contains no row satisfying both requirements:

```text
native readout mechanism + one alpha_s factor per decoupling taste.
```

## Remaining Open Routes

This is not a global B4 no-go and does not close the DELTA0 hierarchy
gate. A future positive row could still identify an outside-K1-K8
log-partition readout, a non-perturbative one-link/Haar mechanism,
beyond-mean-field link fluctuations, a Green-kernel readout-dressing
mechanism, or a non-link transport rule. Any such row must exhibit an
actual observable mechanism carrying signature `(1, -2)` per taste or
`(16, -32)` over the sixteen-taste product, not merely insert the
supplier-chain value.

## Non-Claims

This note does not claim:

- hierarchy formula closure;
- an electroweak-VEV derivation;
- a derivation of `alpha_bare`, `alpha_s`, `u_0`, or `<P>`;
- exhaustion of readouts outside K1-K8;
- a new axiom, primitive, fitted coefficient, or textbook import;
- any audit verdict, ledger update, or effective-status movement.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_delta0_b4_current_bank_alpha_attachment_no_go_2026_06_18.py
```

Expected result:

```text
VERDICT: hierarchy DELTA0 B4 current-bank alpha-attachment no-go checks pass.
TOTAL: PASS=N, FAIL=0
```
