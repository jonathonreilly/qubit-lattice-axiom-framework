# The coupled pen and the two machines — Cycle 855

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the free-sector characterization; the
coupling channel; the checker's per-key autonomy refinement; the
braid's exactly-characterized home)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle855_free_sector_reduction_2026_07_28.py`](../scripts/frontier_cycle855_free_sector_reduction_2026_07_28.py)
- [`frontier_cycle855_reduction_independent_check_2026_07_28.py`](../scripts/frontier_cycle855_reduction_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 854 proved the braid lives in the free sector. This cycle
characterizes that sector as a dynamical system:

- **the free sector is 495 wires**, including the k=3 mark bits
  {256, 262} and all braid supports;
- **across keys it is COUPLED, and the channel is physical**: the
  inherited two-wire state (x1,x6) — in its two occurring values
  (0,1) and (1,0) — feeds the free wires {71, 105, 124, 125, 255,
  256} through all nine generators (3,447 witnesses, 50 channel
  signatures). Those receiving wires are not anonymous: 105, 124,
  125 are the landed three-wire-predicate wires and 256 is a mark
  bit — the braid is authored in the free sector, but the pen is
  held by an inherited two-bit state;
- **the checker's constructive refinement: PER_KEY_AUTONOMOUS** —
  inherited values are boundary-constant per key, and with the
  (x1,x6) parameter FIXED the free projection is closed under the
  boundary step: the braid lives in a parameterized family of
  495-wire machines with per-parameter reachable sizes **221,832**
  and **236,462**;
- **the braid is reproduced inside**: all 20 coincidence events and
  86/86 transition probes.

**What this gives the merged why**: its exact home. Not one reduced
machine (the cross-key coupling forbids that), but two — one per
inherited parameter value — with the parameter entering through six
named wires. Any braid derivation now has a bounded arena: the
parameterized free machine, roughly half the full state count each.

## Supplied / derived / open

### Supplied

- the 854 inherited family and 848 braid census (sha-pinned, tracked
  here); the 719 core; everything the cited packages declare.

### Derived

- the 495-wire free complement; the coupling channel with witnesses
  and signatures; the per-key autonomy theorem; the reduced machines'
  reachable sizes; the braid reproduction.

### Open

- the braid's derivation inside the parameterized machine (the
  merged why's final arena); why (x1,x6) takes exactly two values
  across the family; the third parameter-sector question (keys at
  other (x1,x6) values, if any).

## Negative-claim discipline

The COUPLED verdict is witnessed (3,447 exact witnesses); the
autonomy refinement is scoped per key at generator boundaries; the
reduced sizes are exhaustive censuses, not samples.

## Verdict

The free sector turned out to be two rooms, not one — and the
inherited world reaches into both through six named wires, five of
which we already knew as the predicate and the mark. The why has
never had a smaller address. Independent audit still required.
