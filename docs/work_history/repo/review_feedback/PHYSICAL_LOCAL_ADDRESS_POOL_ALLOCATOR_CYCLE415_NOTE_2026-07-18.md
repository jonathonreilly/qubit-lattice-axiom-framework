# Physical local address equality / finite pool allocator — Cycle 415

Date: 2026-07-18

Authority: none

Audit: unset

## Claim boundary

Cycle 415 is a bounded constructive extension of Cycle 414. It replaces the supplied same-target alias value with **local target-address equality** over two lawful six-rail one-hot nearest-neighbour direction registers. It also replaces the single reserve demonstration with a **two-slot** finite blank pool: a fixed connected-nearest-neighbour FIFO schedule performs **two target exchanges**, one local pool shift, and two collision-guarded repeat appends. There is no host branch query.

The exact declared-code relation is

\[
E_{415}G_{415}=G_{\mathrm{physical},415}E_{415},
\]

and the enlarged fixed gate permutation has an exact inverse. The comparator
truth table and inverse cover all 36 ordered pairs of cubic nearest-neighbour
request labels. The complete concurrency/pool schedule is tested on one
perpendicular distinct pair (`+z,+y`), one equal-label representative, and
their 24 proper-cubic frame orbits, plus blind held L6 response sectors.

As in Cycle 414, A and B remain distinct preallocated physical target/work
blocks even when their request labels are equal. The comparator derives a
local request-context equality bit used for two-write suppression; it does not
instantiate an actual shared-register race or derive a global address system.
The binding from each supplied request label to its preallocated target block
is also supplied; the comparator derives equality of the rails, not that
binding or either label's genesis.

In plain-text certificate notation: E_415 G_415 = G_physical,415 E_415.

## Physical construction

Each request address is six M2 rails with exactly one occupied rail, labeled by the six oriented cubic nearest-neighbour directions. Six local Toffoli gates compute railwise matches. A connected prefix/return network XORs their parity into the Cycle-414 alias M2 and cleans every comparator work M2. On the lawful one-hot code, parity is exact equality. Proper-cubic frames permute the six physical direction rails, so equality is invariant without a preferred axis or ordering.

The two supplied blank pool slots are adjacent 32-M2 words. The fixed
predeclared exchange schedule is:

1. exchange target A with slot 0;
2. collision-guarded repeat append at target A;
3. exchange slot 0 with slot 1;
4. exchange target A with slot 0;
5. collision-guarded repeat append at target A.

Thus two blank words permit two additional bounded uses of target A. Reversing
these layers exactly restores the input. The repeat guards matter: a
same-target collision suppresses the initial pair and both later repeat
appends, leaving both pool slots blank. The distinct `+z,+y` requests exercise
adjacent target neighborhoods with a common 95-M2 source spine. The schedule
does not search for availability, choose a slot, replenish the pool, or
dynamically handle a dirty/occupied pool word; malformed pool inputs reject.

## Results and controls

- 452 represented M2 sites: Cycle 414 plus 32 address/comparator M2 and one additional 32-M2 blank slot.
- All gates have support at most three and connected nearest-neighbour support; every schedule is fixed from the state-independent layout.
- Exhaustive 36-pair request-label comparator truth table: exact equality, zero comparator-work leakage, exact inverse.
- Two exchanges of target A plus one pool shift: target A, target B, slot 0, and slot 1 all carry lawful coherent candidate labels in the tested open distinct-target sector; inverse residual is exactly zero.
- Same-target: collision is derived locally, all initial/repeat candidates are suppressed, both pool slots stay blank, and inverse residual is exactly zero.
- Closed response: no target or pool candidate.
- All 24 proper-cubic frames: zero mapping, locality, candidate, collision, or inverse failures.
- Blind held L6: candidate-sector weights match the inherited response-sector weights for every inherited source route and both tested origins; all inverse residuals are zero.
- Equality-gate and pool-shift deletion tests are visible; non-neighbour addresses and dirty/occupied second-slot inputs reject.
- The Cycle-219 mass fixture is rechecked; contact/source bridge keys, prior
  Records, and dependency depth are structural/inherited spectators and remain
  unchanged under the new register action.

## Supplied, derived, open

Supplied structure is explicit: the Cycle-414 response/payload/predecessor and two target/work blocks; two lawful one-hot nearest-neighbour request labels and their target-block bindings; two preallocated blank 32-M2 pool slots; the collision-suppression policy; one fixed exchange schedule; the L6 boundary, proper-cubic frames, physical routing, and readout.

Derived here: local reversible target equality rather than a supplied alias value; exact same-target suppression including repeat use; two finite target exchanges, one local pool shift, inverse cleanup, held-size transfer, and 24-frame covariance.

Still open: physical request-label genesis, target-block binding, or target
choice outside this declared local code; an actual shared-register race;
availability search; blank genesis; pool replenishment; unbounded renewal;
resource accounting; actual Record formation, permanence, and actuality;
normalized statistics/Born law; physical time/rate; source/stress; and gravity
response.

The pool labels are coherent reusable candidates, **not actual Records**. This is **not blank genesis**, **not a renewal law**, not permanence, not resource conservation, probability, time, source, or gravity. There is no negative, minimum-content, shared-obstruction, or axiom-pressure claim.
