# Same-Family 3D Closure: Valley-Linear

**Date:** 2026-04-04 (inline-cache repair: 2026-05-18)
**Status:** bounded same-family closure note; the wrapper presents the
**Claim type:** bounded_theorem
closure card backed by the inlined per-`L` / per-`W` cached certificates
in the "Per-L / per-W cached certificates" section below. The wrapper
does **not** itself recompute the load-bearing observables. Rows 1-7
(core card at `h=0.25, W=10, L=12`) and the row-10 tails (`W=10` core
and `W=12` companion) are anchored against the inlined cache excerpts.
Rows 8-9 at `L=8` and `L=10` are narrowed to queued follow-up status
because the 2026-04-04 per-`L` source logs at the matching `h=0.25,
W=10` slice could not be located on 2026-05-18; the `L=12` anchor for
those rows is supported by the inlined core-card cache. The script is
therefore a print-aggregation wrapper for an already-frozen multi-log
core (now made visible from this packet), not a live re-derivation
harness.

**Audit-conditional perimeter (2026-05-02):**
The current generated audit ledger records this row `audited_conditional` with
`auditor_confidence = high`, `chain_closes = false`, and `claim_type =
bounded_theorem`. The audit chain-closure explanation is exact: "The
source note itself says the wrapper aggregates and prints frozen rows
and does not recompute the load-bearing observables. With deps=[] and
no retained log/runner dependency chain, the closure card cannot be
retained as an independently audited theorem." This rigorization edit
only sharpens the boundary of the conditional perimeter; nothing here
promotes audit status. The supported content of this note is the
print-aggregation wrapper itself: the script
[`scripts/same_family_3d_closure.py`](../scripts/same_family_3d_closure.py)
prints the frozen 10-row table and the registered cache
[`logs/runner-cache/same_family_3d_closure.txt`](../logs/runner-cache/same_family_3d_closure.txt)
captures the wrapper output. The note is honest in §"What remains
open" that the wrapper is replay-only; that honesty is exactly the
audit-stated reason the row cannot promote — there are no live
deps=[] in the wrapper. The supported perimeter is the wrapper
print itself, not the underlying closure checks. A future repair
would explicitly enumerate the per-`L` and per-`W` runs as
dependencies (with their own ledger entries) so the chain rule could
close; that step is deferred to a downstream rebuild and is not in
the scope of this print-aggregation note.

## Current on-disk artifacts

- Script: [`scripts/same_family_3d_closure.py`](/Users/jonreilly/Projects/Physics/scripts/same_family_3d_closure.py)
- Log: [`logs/2026-04-04-same-family-3d-closure.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-04-same-family-3d-closure.txt)

## Per-L / per-W cached certificates (load-bearing for restricted packet, inlined 2026-05-18)

The wrapper print-aggregates the closure card from already-frozen rows. The
audit verdict (2026-05-02) explicitly notes that the wrapper itself does not
recompute the load-bearing observables and has no `deps=[]` chain to the
per-`L` / per-`W` source runs. This section inlines the cache excerpts that
the closure card draws from, so the source data backing rows 1-7 (core card),
the W=12 companion in row 10, and the L=12 anchor for rows 8-9 are visible
directly from this packet without needing to traverse the wrapper.

The repair makes no audit-status claim. It scopes the supported perimeter of
this note to the rows that have a retained, on-disk source-log excerpt below.
Rows 8 and 9 at L=8 and L=10 are explicitly narrowed at the end of this
section because no retained source log carrying those replays at h=0.25, W=10
could be located on 2026-05-18.

### Sub-section A — Core h=0.25, W=10, L=12 (rows 1-7 + L=12 anchor for rows 8-9)

Inlined from [`logs/2026-04-04-valley-linear-same-harness-compare.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-04-valley-linear-same-harness-compare.txt)
and [`logs/2026-04-04-valley-linear-asymptotic-bridge.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-04-valley-linear-asymptotic-bridge.txt):

```text
========================================================================================
SAME-HARNESS ACTION COMPARISON: spent-delay vs valley-linear
  fixed family: 3D ordered dense lattice, 1/L^2 kernel, h^2 measure
  h=0.25, W=10, L=12, max_d=12, nodes=321,489
========================================================================================
action                 Born        k=0      F~M    gravity   TOWARD                   tail
valley-linear      4.20e-15  +0.00e+00     1.00  +0.000224      8/8 z>=4: -0.93 (R²=0.983)

VALLEY-LINEAR ASYMPTOTIC BRIDGE (h=0.25 core retained anchor)
core retained   0.25   10   4.20e-15  +0.00e+00     1.00   +0.000224      9/9 z>=4: -1.00 (R²=0.979) z>=5: -1.12 (R²=0.991, n=6)
```

This anchors rows 1, 3, 4, 5, and the W=10 core tail of row 10
(`b^(-0.93)` from same-harness-compare; the `b^(-1.00)` z≥4 read from
asymptotic-bridge is a consistent same-family replay) at the same core
family. Rows 2 (`d_TV=0.83`), 6 (Decoherence=49.9%), and 7 (MI=0.64 bits)
are carried inside the wrapper's frozen-card values and are not separately
inlined here; they are part of the supported "frozen-card" perimeter of
the wrapper, not of the load-bearing per-`L` chain this section restores.

### Sub-section B — W=12 width companion for row 10 far tail

Inlined from [`logs/2026-04-04-valley-linear-wide-tail-replay.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-04-valley-linear-wide-tail-replay.txt):

```text
========================================================================================
3D VALLEY-LINEAR WIDE-TAIL REPLAY
  Bounded h=0.25, W=12 follow-up on the ordered-lattice 1/L^2 family.
  nodes=461,041  layers=49  h=0.25  W=12  max_d=12
========================================================================================
Barrier sanity: Born=4.82e-15  k=0=+0.000000
TOWARD support: 9/9
Tail from peak (z>=4): b^(-1.07), R^2=0.990  n=7
Far tail (z>=5): b^(-1.17), R^2=0.997  n=6
Total time: 128.1s
```

This anchors the W=12 companion `b^(-1.07)` value in row 10 of the card.

### Sub-section C — Honest narrowing of rows 8-9 (L=8 and L=10 at h=0.25, W=10)

The wrapper claims that "L=8 and L=10 were replayed separately on 2026-04-04"
with hardcoded values `grav={8: 0.000157, 10: 0.000199}` and
`1-pur={8: 0.4997, 10: 0.4994}`. On 2026-05-18 a careful sweep of the
`logs/` and `logs/runner-cache/` directories did not locate any retained
log under `logs/2026-04-04-*.txt` that carries L=8 or L=10 at the same
core slice `h=0.25, W=10` with those specific (grav, 1-pur) pairs. The
only retained 2026-04-04 logs that mention `L=8` or `L=10` together with
purity are at different slices (`h=1.0, W=6` in
`2026-04-04-lattice-3d-dense-10prop.txt`, and `h=0.5, max_d=3` in
`2026-04-04-valley-linear-robustness-sweep.txt`), which are not the same
family as the closure card's core slice.

Consequently, rows 8 and 9 (the same-`h` multi-`L` rows with `L=8` and
`L=10`) are narrowed here to **queued follow-up** status. The card's L=12
anchor row remains supported by Sub-section A above. The intended same-`h`
multi-`L` story is not removed from the card — it is honestly demoted to
"needs a recovered or re-run source log" pending a future repair that
produces the per-`L` source artifacts.

The wrapper print-output still includes the hardcoded L=8 and L=10 lines,
but for the supported perimeter of *this* note they read as queued
follow-ups rather than as load-bearing rows. A future repair that adds
explicit dependency entries for live or cached per-`L` certificates can
restore those rows to the supported chain; that future step is outside
the scope of this inline-cache repair.

This is a same-family closure on one retained family:

- action: `S = L(1-f)`
- kernel: `1/L^2` with `h^2` measure
- field: `s/r`
- ordered 3D dense lattice

It is not a single-instance theorem card. Properties `8-9` are same-family
multi-`L` rows, and property `10` includes a same-family width companion.
The frozen wrapper replays `L=8` and `L=10`, then reuses the retained core
`L=12` row so the whole note stays on one family at one `h`.

## Architecture
- Action: S = L(1-f) (valley-linear)
- Kernel: 1/L^2 with h^2 measure
- Lattice: 3D dense, h=0.25, W=10, max_d=3
- Field: s/r with s=5e-5

## Card

| # | Property | Value | Same family? |
|---|----------|-------|-------------|
| 1 | Born | 4.20e-15 | h=0.25 W=10 L=12 |
| 2 | d_TV | 0.83 | h=0.25 W=10 L=12 |
| 3 | k=0 gravity | 0.000000 | h=0.25 W=10 L=12 |
| 4 | F∝M alpha | 1.00 | h=0.25 W=10 L=12 |
| 5 | Gravity sign | +0.000224 TOWARD | h=0.25 W=10 L=12 |
| 6 | Decoherence | 49.9% | h=0.25 W=10 L=12 |
| 7 | MI | 0.64 bits | h=0.25 W=10 L=12 |
| 8 | Purity stable | 50.0% (L=8,10,12) | h=0.25 W=10 |
| 9 | Gravity grows | +0.157→+0.224 | h=0.25 W=10 |
| 10 | Distance tail | b^(-0.93) W=10 / b^(-1.07) W=12 | h=0.25 |

Properties 8-9 use `L=8,10,12` at the SAME `h=0.25` and `W=10`.
No `h=0.5` companions are needed, but the `L=12` multi-`L` row is carried
through the frozen core-card values rather than recomputed inside the wrapper.

## What this closes

This is the first time the same-family closure is carried as a real
script/log/note chain. The fixed core rows remain at `h=0.25, W=10, L=12`;
properties `8-9` are same-`h` multi-`L` rows; and property `10` still carries
a width companion for the far tail.

## What remains open

- The distance exponent is near-Newtonian but not exactly -1.0. The frozen
  W=10 and W=12 rows stay as companion width checks. Cache excerpts for
  both widths are inlined above.
- Properties 8-9 use multiple `L` values (necessary for scaling checks).
  This is a same-family multi-size test, not a single-instance card. As
  of the 2026-05-18 inline-cache repair, the `L=8` and `L=10` per-`L`
  source logs at the matching `h=0.25, W=10` slice could not be located
  on disk; rows 8-9 at those `L` values are therefore narrowed to
  **queued follow-up** status (see Sub-section C above). The `L=12`
  anchor for these rows remains supported.
- The wrapper is partly replayed and partly frozen by design: it is a review-
  facing closure note, not a new heavyweight all-live card harness. The
  script `scripts/same_family_3d_closure.py` aggregates and prints the
  frozen rows but does not itself recompute the underlying closure
  observables. Live recomputation lives in the per-`L` and per-`W` runs;
  the cached certificate excerpts for the rows the per-`L`/per-`W` chain
  *does* cover are now inlined above so the supported perimeter is visible
  directly from this packet.
- The action is selected, not derived (though the universality-class result
  shows it's the simplest member of the Newtonian family).
