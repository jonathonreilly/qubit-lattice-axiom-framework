# Physical occupancy-to-six-q syndrome extractor — Cycle 675

Date: 2026-07-23
Authority: **none**
Audit: **unset**

## Result

Cycle 675 closes Cycle 672's supplied-q wall on an explicit bounded physical
input family.  Every tested coarse cell receives six independent physical M2
occupancy rails at the proper-cubic radius-four orbit.  Its six q sites are the
existing radius-three shadow orbit and begin blank on the lawful code.  The
corresponding matter/q pairs are nearest neighbors.

The reversible extractor is an 18-factor SWAP written as three six-CNOT
commuting layers:

1. all six `matter -> q` CNOTs;
2. all six `q -> matter` CNOTs;
3. all six `matter -> q` CNOTs.

Direction factors inside a layer are disjoint and commute, so the serialized
list is not a preferred physical direction schedule.  On coherent A2 input the
first extractor moves the complete amplitude vector from physical matter to q
and blanks matter.  The product then prepares Cycle 672's declared role-table
code, executes its detector macro, applies the Cycle-668 binder/contact
Toffoli, reverses the detector, decodes the role table, and applies the inverse
extractor.  Matter and q are restored while the opportunity bit is toggled
exactly when physical A2 matter and the binder are both present.

The chronological segments are:

`SWAP(matter,q) ; inverse(W_cell) ; [W_cell ; P_A2 ; inverse(W_cell)] ; binder-Toffoli ; inverse([W_cell ; P_A2 ; inverse(W_cell)]) ; W_cell ; inverse(SWAP(matter,q))`.

At the origin, the bracketed detector's factor count and digest equal the exact
committed Cycle-672 detector.  Generic cells use the same Cycle-672 construction
with their committed Cycle-608 local role tables and local read blocks.  Their
words are exported independently and are not called the exact origin word.

## Executed scope

The runner executes L3 train, L4 held-out-size and L6 held fixtures.  At each
size the cell family is the origin plus the complete proper-cubic orbit of the
lexicographically first cell having the maximum incident-C count.  This gives
23 cells total: three exact-origin baselines and 20 generic cells whose
Cycle-608 incident-C context is nonzero.

Across those cells it executes 460 four-bit comparisons: all material/binder
values, contact on/off, and five Cycle-662 train/held biased/nonproduct coherent
spectator profiles.  The maximum detector/interface and initial-q
counterfactual residuals are below `1e-15`; terminal leakage is zero.  Six
one-particle directions per cell remain detector-negative to numerical
tolerance.  Dirty branch work has zero overlap with the clean asserted output.

The decisive counterfactuals pass:

- with the same initially blank q, vacuum matter leaves opportunity unchanged
  while A2 matter toggles it under contact;
- with the same A2 matter, initial q words `0`, `21`, and `63` are restored and
  do not alter the detector result;
- an A2 state placed only in the initial q register with physical matter vacuum
  is ignored by the detector composition and restored unchanged.

Thus this circuit follows physical matter, not an input q label.  Blank q is
still the declared lawful-code condition; the nonblank cases are explicit
malformed/counterfactual controls, not an enlargement silently assumed.

## Placement, covariance and deletion controls

The radius-four matter orbit is globally injective and collision-free against
all inherited physical, q, branch, work, path and read roles on L3/L4/L6.  All
matter/q pairs have M2 distance one.  Depending on the compiled generic cell,
the full chronological product contains 3,215–3,791 macro factors, at most 73
operand M2 sites, and maximum individual macro support eight; these bounds do
not grow with held size.

All 24 proper-cubic frames and all 576 ordered products pass after an explicit
local fermionic repair.  Coordinate-only transport fails 48 of 72 signed state
comparisons with residual `4/3`: it permutes occupation bits but omits the wedge
sign, so it is retained as a failed control rather than called physical CAR
covariance.  For a mode permutation, that sign is the parity of inverted
occupied pairs.  Cycle 675 realizes it before and after the transported word by
at most 15 local matter-rail CZ factors, with maximum bounded route length
eight.  No global parity string is used.  The repaired executed transport has
zero state failures, the fermionic representation passes all 576 composition
tests, and the A2 orbit overlap has absolute value one to tolerance.  Every
extractor edge stays nearest-neighbor and the three commuting layers remain six
disjoint pairs.  This is compile-time transported circuit covariance.  It is
not promoted to a same unprogrammed all-cell device, and there is no runtime
frame selector.

For reviewability, the receipt does not repeat every one of the 524–3,791
generated `W_cell` factor descriptors for all 23 cells. It retains each word's
factor count, canonical digest, and first/last four coordinate-explicit
descriptors; the runner regenerates and executes the full word before writing
those summaries. The extractor, predicate, conjunction, covariance sheath,
residual, and deletion exports remain explicit. This is receipt compaction,
not a reduced execution domain.

Each of the 18 extractor factors has an executed full-extractor deletion
witness with signal `sqrt(2)`.  The witness is constructed by applying the
inverse prefix to a local matching-control/target-zero basis state.  Some
deletions are masked on the single A2/contact target fixture because the outer
extract/unextract pair and that restricted state have an XOR symmetry; the
receipt retains those near-zero target-fixture signals rather than hiding them.
Every factor of every complete product additionally has the exact Cycle-672
unitary prefix/suffix deletion construction, with minimum local signal greater
than `0.765`.  The central A2 predicate deletion changes every tested full
interface fixture by `sqrt(2)`.

## Strict boundary

This is a strong bounded partial, not the strict target.

The selected generic cells are chosen using Cycle 608's incident-C census, but
their executed word contains the local A/SELECT/D Cycle-672 macro only.  It does
not prepare neighboring branches and insert the incident C equality phase rows.
Consequently a physical incident-C star product remains open.  Also, each
generic local table and read block is compiled from the supplied chart.  The
family is proper-cubic closed and functionally tested, but no autonomous
unprogrammed device shared by every cell is constructed.

Finally, the radius-four M2 occupation rails are genuine independent inputs,
but their A2 amplitudes and their identification as framework matter are
supplied.  No autonomous matter genesis or general physical-code embedding is
claimed.

## Prior-art and novelty boundary

Cycle 560 supplied separated physical/q coordinates and local role tables but
no matter-to-q dynamics.  Cycle 608 supplied local factor/count blueprints and
an algebraic incident-C audit but no physical detector product.  Cycle 668
supplied the four-bit comparison kernel.  Cycle 672 newly executed the origin
macro but required supplied q.  Cycle 675's new content is the explicit
collision-free radius-four matter orbit, the three-layer coherent SWAP
extractor, its actual composition with Cycle 672 and Cycle 668, initial-q
counterfactuals, generic proper-cubic cell family, signed covariance execution,
and extractor-factor deletion witnesses.  None of this is back-credited.

Cycle 608's provenance-only 12/13 replay defect and Cycle 612's
`detector_reference` schema failure remain disclosed through the pinned Cycle
672 replay packet.  Neither prior artifact is repaired.

## N1–N8 and dependency ledger

Full current N1–N8 discipline is serialized in the receipt.  Three qualifying
constructive attempts are separated from two open routes, so the five-route
negative threshold is not met.  The incident-C star, same-device chart and
framework-matter identification walls are directionally separated.  Hidden
wall, exact residual, rhetoric, partial closure, actionable steelman and
cross-cycle echo audits are explicit.

No broad no-go, minimum-content claim, shared route-independent obstruction or
axiom pressure is licensed.

- `C_ref`: advances because q is blank and derived from independent matter;
  A2 amplitudes, binder and matter identification remain supplied.
- `C_num`: unchanged; finite committed matrices/profiles remain supplied.
- `C_wrap`: unchanged; no wrapped phase or energy claim.
- `C_int`: advances through the executed extractor/detector/binder/uncompute
  product.
- `C_local`: advances on a proper-cubic-closed generic family; incident-C star
  and same-device chart remain open.
- `C_source`: unchanged; no energy, gravity or source identification.

The optimal next campaign is to split local W into A/SELECT/D prefixes, prepare
the target and incident neighbors, insert every C equality phase row, execute
their deletion controls, and then replace compiled read blocks with a uniform
cellular tile.

Constitutional effect: **none**.  No axiom, foundation, Qualification,
primitive, registry, policy, queue or audit-status file is edited.
