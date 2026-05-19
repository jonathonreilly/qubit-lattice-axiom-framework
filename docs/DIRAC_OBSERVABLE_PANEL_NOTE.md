# Dirac Observable Panel Note

**Status:** bounded - bounded or caveated result note
**Claim type:** bounded_theorem
**Date:** 2026-04-10  
**Scope:** one Dirac 3+1D harness, many gravity readouts.

**Audit-conditional perimeter (2026-05-03; panel cert inlined 2026-05-18):**
The current generated audit ledger records this row `audited_conditional` with
`auditor_confidence = high`, `chain_closes = false`, and `claim_type =
bounded_theorem`. The audit chain-closure explanation is exact: "The
dependency now closes for retained bounded core results, including
multi-observable gravity under primary readouts, but the supplied
runner output does not report the observable-panel-specific readouts
listed in this note. The missing step is a panel run or retained
summary tying centroid, peak, first-arrival, early accumulation,
current, and shell imbalance to the stated default sweep and sign-
alignment questions." This rigorization edit only sharpens the
boundary of the conditional perimeter; nothing here promotes audit
status. The supported content of this note is the bounded
methodological framing: the panel of readouts, the interpretation
rules, and the default sweep are all auditable framings, not
numerical claims.

The panel-specific runner
`scripts/frontier_dirac_walk_3plus1d_observable_panel.py`
(sha256 `a83db7…0ce834e`) has now been executed on the default sweep
`n=21, offset=3, layers=10,12,14,16,18,20, mass=0.3, strength=5e-4`
and its full stdout deposited at
`logs/runner-cache/frontier_dirac_walk_3plus1d_observable_panel.txt`
(exit_code=0, elapsed≈1.41s). The cache reports all six listed
readouts (centroid shift, peak shift, first-arrival, early shell
accumulation, directional current, and shell imbalance) on the stated
sweep. This inlines the panel cert; what the panel data itself
**does not** support is a sign-locked statement about gravity: across
the six layer counts the panel returns three `ALL` rows
(`A0AA, A0AA, A0AA` at N=10,12,14) and three `MIX` rows
(`T0AA, T0TA, TATA` at N=16,18,20), with the centroid flipping sign
between N=14 and N=16 while peak remains zero or `-3` only at N=20.
The honest reading is that the panel exhibits a recurrence- and
readout-driven sign split on the default sweep, exactly the
diagnostic the methodological framing was designed to detect. The
note therefore remains `bounded_theorem` as a methodological card
plus a registered panel run; the framing is auditable and the runner
is reproducible, but no sign-locked gravity claim is made from the
panel output.

The current Dirac work has reached the point where the main question is not
just whether a sign is `TOWARD` or `AWAY`, but whether the sign survives under
different physically plausible readouts.

This panel is the early bottleneck test for that question.

## What The Panel Measures

On the same `frontier_dirac_walk_3plus1d_v3.py` harness, the panel compares:

- centroid shift
- peak shift
- first-arrival layer for mass-side accumulation
- early mass-side accumulation
- directionally projected current
- mass-side shell imbalance

The point is to separate:

- geometric transport
- packet-shape effects
- recurrence / boundary effects
- readout-specific artifacts

from each other before they become a paper-level claim.

## Why It Matters

The branch already shows that a single gravity readout can be misleading.
Different observables can disagree even when they come from the same lattice,
same coupling, and same propagation law.

The panel is designed to answer three questions:

1. Do all readouts agree on sign in the same basin?
2. Do disagreements appear only near recurrence windows?
3. Is the remaining non-monotonicity geometric, or just a readout artifact?

## Interpretation Rules

- If centroid, peak, current, and shell imbalance agree, the sign is probably
  geometric.
- If peak disagrees but the others agree, the readout is too wave-sensitive.
- If the sign flips only at large `N`, boundary recurrence is still active.
- If first-arrival and early accumulation disagree with the final observables,
  the panel is telling us the transport is not settling before the detector
  window.

## Core-Card Connection

This panel is the concrete implementation target for the historical multi-readout
panel row later absorbed into the audited Dirac-core discussion in
[DIRAC_CORE_CARD_NOTE.md](./DIRAC_CORE_CARD_NOTE.md):

- first-arrival
- peak
- current
- centroid
- torus-aware centroid

If the architecture cannot keep these readouts aligned on a clean operating
point, the gravity story is not yet stable enough for promotion.

## Default Run

The default sweep is intentionally modest:

- `n=21`
- `offset=3`
- `layers=10,12,14,16,18,20`
- `mass=0.3`
- `strength=5e-4`

That is enough to expose the readout split without turning the panel into a
new sprawling campaign.

### Registered panel cert (2026-05-18)

Runner: `scripts/frontier_dirac_walk_3plus1d_observable_panel.py`
(sha256 `a83db713cce4556d432e324314a578e555c744898cc7b5dc56028d80e0ce834e`).
Full stdout is cached at
`logs/runner-cache/frontier_dirac_walk_3plus1d_observable_panel.txt`
(exit_code=0, elapsed≈1.41s).

Default-sweep panel output (excerpted from the cache):

```
   N      centroid          peak  first+   early_shell       current         shell   sig  cons
--------------------------------------------------------------------------------------------
  10   -5.6732e-05   +0.0000e+00       6   -3.2937e-06   -1.3245e-06   -3.0502e-07  A0AA   ALL
  12   -3.5467e-05   +0.0000e+00       6   -1.3506e-06   -2.3064e-06   -4.0074e-07  A0AA   ALL
  14   -2.2252e-06   +0.0000e+00       6   +3.9628e-07   -2.6985e-06   -2.0704e-07  A0AA   ALL
  16   +1.2310e-05   +0.0000e+00       6   +1.2553e-06   -1.4828e-06   -9.4977e-08  T0AA   MIX
  18   +2.9339e-05   +0.0000e+00       6   +2.2711e-06   -2.2882e-06   +4.7059e-07  T0TA   MIX
  20   +2.9436e-05   -3.0000e+00       6   +1.9661e-06   -4.7811e-06   +1.7158e-06  TATA   MIX
```

Agreement summary (from the same cache):

- centroid vs peak: `0/6`
- centroid vs shell: `5/6`
- centroid vs current: `3/6`
- peak vs shell: `0/6`
- all-four agree: `3/6`
- mixed-sign cases: `3/6`

The six listed readouts (centroid shift, peak shift, first-arrival,
early shell accumulation, directional current, shell imbalance) are
each produced for every layer count on the default sweep. The panel
is registered as a methodological cert: the runner reproduces, the
columns are populated, and the answer to "do all readouts agree on
sign?" is recorded as a recurrence-driven `ALL/MIX` split, not as a
sign-locked claim. Interpretation rules above are framing only; no
gravity sign is asserted by this note.
