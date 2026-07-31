# Marked but unscheduled — the k=3 stall is pure scheduling — Cycle 849

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the exact k=3 three-source meeting
structure; the native minimal mark with exhaustive minimality; the
stall localized after marking)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle849_scheduling_contrast_2026_07_28.py`](../scripts/frontier_cycle849_scheduling_contrast_2026_07_28.py)
- [`frontier_cycle849_contrast_independent_check_2026_07_28.py`](../scripts/frontier_cycle849_contrast_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 847's million-tick null asked WHERE the k=3 machinery stalls:
before its meets, at the mark, or after. The answer is **MARKED** —
the stall is after marking:

- **the meets exist and are exact**: all six trio keys' first common
  all-source wavefront meets occur at **tick 3**, with meet centers
  `(3)`, `(10)`, and `(0,10)` — the three-source meeting structure is
  fully derived, and the checker re-derived it independently;
- **the inherited marks fail, a native mark exists**: both k=2 wire
  triples (the nine-triple `40/81/105` and the pair-triple
  `88/124/125`) FAIL to transfer — the checker confirmed both collide
  across classes. But the k=3 stratum carries its own mark:
  **`bit[256] == bit[262]`** separates trio keys from non-trio k=3
  keys at their meets, in both directions;
- **the mark is exhaustively minimal** (the checker's strengthening):
  **no single-bit mark exists**, and `(256,262)` is the FIRST minimal
  pair in enumeration order — the minimality is censused, not
  asserted;
- **the stall is after the mark**: the marked trios show no clean
  postimage, no recurrence, and no full-state funnel through
  **T=1,048,576** (checker horizon; primary swept 65,536) —
  `AFTER_MARK_PURE_SCHEDULING`.

**What this gives the program**: the cross-stratum contrast is now
exact. Both strata mark their backbone meets with native wire-pair
marks; the k=2 stratum's marks all fired (family complete at
t=1,142,432); the k=3 stratum's marks have not fired by a million
ticks. Within the censused machinery, everything before the schedule
is in place — meets exact, mark native and minimal — so the silence
is a scheduling fact, not a marking failure. This is precisely the
freedom the axiom-silence package (Cycle 828) hands the owner: the
marked trios are waiting for exactly the sentence under decision. The
trio bet also sharpens: any future trio resolution must sit at a
`bit[256]==bit[262]` meet, adding a mark clause beside the braid
clause.

## Supplied / derived / open

### Supplied

- the 719 two-rail controller core (sha-pinned); the landed k=2
  resolution family and the 847 null; everything the cited packages
  declare.

### Derived

- the six-trio meeting structure (times and centers); the k=2 triple
  transfer failures; the native mark with two-direction separation and
  exhaustive pair-minimality; the after-mark stall localization.

### Open

- when (whether) the marked trios' records form — the schedule input
  itself (owner surface, Cycle 828); the merged why; the off-backbone
  quiet.

## Negative-claim discipline

The transfer failures are exact at the censused meets; the
no-single-bit and first-pair minimality claims are exhaustive
enumerations at the declared mark family; the stall null is scoped to
the swept horizons (65,536 primary / 1,048,576 checker) and the three
declared resolution modes. Nothing here claims the trios never
resolve.

## Verdict

The k=3 stratum turns out not to be broken, or unready, or unmarked —
it is dressed, marked, and standing at its meets, and has been since
tick 3. What it lacks is a turn. The contrast between a finished
family and a silent one is now a single free input: the schedule.
Independent audit still required.
