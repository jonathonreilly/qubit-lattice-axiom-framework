# Cycle 728: W1's global remainder compresses to one marked-edge holonomy bit — after a refuted first convention

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle728_bksf_holonomy_compression_2026_07_28.py`](../scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py)

Independent check:

- [`frontier_cycle728_holonomy_independent_check_2026_07_28.py`](../scripts/frontier_cycle728_holonomy_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front — including the self-correction

Cycle 724 fixed the exact local/global split of the controller's
one-token sector: bounded-radius rows cannot see a distant second token.
The campaign's charge-row convention proposed compressing that global
remainder into a ring-holonomy datum. This cycle delivers the
compression — after first REFUTING its own original formula:

- **The refutation (frozen in-package).** The originally declared
  holonomy — the XOR of consecutive reference-agreements around the
  ring — is a coboundary: on a closed ring every reference bit enters
  exactly two rows, so the sum is a size-parity constant, not a degree
  of freedom. The runner's exhaustive censuses (one value across all
  1,024 / 2,048 reference states on rings 10/11; zero matching states
  for the original direction-(a) claim; 2,099,200 direction-(b)
  separation failures) are frozen as the refutation record. Chained-
  difference holonomies on closed rings are always trivial.
- **The amended convention (a declared supply).** One holonomy register
  `h` at a single marked edge `s*` enters exactly one local row:
  `L_{s*} = A ⊕ B ⊕ ref_{s*} ⊕ ref_{s*+1} ⊕ h`; all other rows are the
  unchanged radius-one parity constraints.
- **The compression theorem (exact, exhaustive).** The twist telescope
  `XOR_s L_s = (global token parity) ⊕ h` holds as an algebraic identity
  on rings 11/35/130 and exhaustively over all ring-11 states. Both
  directions hold exactly: every state satisfying all local rows has
  token parity equal to `h` (2,048 fixed-reference matches per sector),
  and for each value of `h` the satisfied set is exactly the
  corresponding token-parity sector (2,097,152 projected states per
  sector, zero separation failures).
- **Non-derivability stays sharp (the block04 lesson, upgraded).** A
  frozen witness pair — `(A, refs, h) = (0,0,0)` versus `(4,6,1)` —
  satisfies every local row while differing in `h`, and is
  indistinguishable on all nine radius-one windows excluding the marked
  edge. The global remainder of W1's token sector is therefore exactly
  ONE declared bit at one declared edge: no less, and localized.
- The frozen R-pullback law: the row set is not permuted by the
  controller's swap layers (the actual transformation is frozen as a
  table), but `token parity ⊕ h` is invariant under the full step with
  static references. Controls (reference flips, rail flips, row-order
  permutation, `h` flip) all detect as expected.

## Supplied / derived / open

### Supplied

- the mode-graph convention, the clean reference chain, the marked edge
  `s*`, and the holonomy register `h` (declared clean supplies, per the
  campaign decision record and its amendment);
- the controller inventory unchanged (one-token genesis remains supplied;
  the rows here are observables and identities, not yet enforcement).

### Derived

- the coboundary refutation of the original chained holonomy, with
  frozen exhaustive censuses;
- the twist telescope identity and the two-direction compression theorem
  with frozen counts;
- the marked-edge non-derivability witness (radius-one window census);
- the frozen R-pullback law and the invariance of `token parity ⊕ h`;
- support censuses: every row radius-one; only `L_{s*}` reads `h`.

### Open

- integration of the charge rows into the refusal wrap (enforcement
  rather than observation) — the named next enforcement leg;
- autonomous preparation of the reference chain and `h` (genesis stays
  supplied);
- everything inherited (occurrence, time, Record, Born, source) at its
  original scope.

## Negative-claim discipline

The refutation of the original formula is scoped exactly to that
formula (chained-difference holonomies on closed rings), with the
exhaustive censuses as witnesses; it is a self-correction of a campaign
convention, not a route no-go. The non-derivability witness is a
radius-one statement on the tested ring, in the block04 pattern.

## Verdict and next experiment

W1's enforcement ledger now reads: dirty rails refused everywhere
(Cycle 723); radius-one collisions refused everywhere (Cycle 724); and
the remaining global content of the one-token sector compressed to a
single declared marked-edge holonomy bit whose value no bounded window
away from the mark can see (this cycle) — with the campaign's own first
convention honestly refuted and replaced en route. The named next legs:
wire the charge rows into the refusal wrap as enforcement; the Born-lane
feed; the sector-summed companion channel; and the autonomy items per
the forcing ledger. `w1_closed: false` — genesis is untouched.
