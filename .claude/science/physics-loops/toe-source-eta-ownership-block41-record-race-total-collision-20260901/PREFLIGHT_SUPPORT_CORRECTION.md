# Preflight support correction — legal/reachable transaction sector

**Frozen before the Block-41 target runner was executed.**

The preregistered transaction-grant route survives, but three adversarial
configurations require an explicit domain and liveness correction.

## Counterexamples

1. Two head Records can each occupy a site in the other's future write
   footprint. Because Records are permanent, neither unchanged Block-38 trial
   can complete. Requiring a productive winner on that input is impossible
   without a new collision-specific successor row.
2. A singleton `H` with an inert permanent Record already at a future `A`
   target still has the literal Block-38 `H -> T` proposal, whereas a
   complete-footprint grant law must decline it. Exact singleton equality can
   therefore apply only to the source-declared clean-footprint sector.
3. An arbitrary map can contain two already-written overlapping `T` grants or
   an orphan `T` that later acquires a matching `H`. Such a map is not a
   reachable grant-consistent history and has no encoded priority/order that
   could choose a historical winner.

## Corrected state contract

The generator is defined on every finite well-typed map, but its positive
transaction theorem is on the **reachable grant-consistent sector** generated
from finite clean heads and archives:

- a clean ungranted head has all 18 write sites blank;
- every valid `T` grant has a matching source `H` and protocol;
- valid granted write footprints are pairwise disjoint;
- every continuation Record is produced inside exactly one granted footprint;
- old completed footprints and malformed/orphan/conflicting pregrants are
  inert obstacles, not new owners; and
- heads whose footprint is already occupied or intersects a valid grant are
  terminally absorbed. Their permanent `H` plus the blocking Record/grant make
  that disposition state-visible.

On a nonempty component of clean mutually conflicting heads, the equal-rate
grant race has at least one winner and its grant/loss kernel is normalized. On
a component with no clean head, the defined outcome is terminal absorption;
no productive-winner or elastic-scattering claim is made. Unrelated valid
components must remain active rather than being frozen by a malformed remote
component.

Exact singleton reduction means equality with Block 38 from one clean head
through the complete trial. It does not mean equality on arbitrary
archive-contaminated singleton maps, a domain Block 38 itself did not totalize
transactionally.

## Impact consequence

Block 41 may claim a total absorptive/exclusion process only with this
terminal boundary. Whether that is sufficient to retire the registered `W3`
existence wall is reserved for the independent post-execution impact gate. If
the gate requires a productive collision-specific successor on mutually
blocked heads, the result remains route progress/backlog and the first missing
law field is that successor/resource row.
