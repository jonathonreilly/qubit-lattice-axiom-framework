# The smallest carriers of a charge, counted and sorted into families — Cycle 748

Date: 2026-08-08 (revised 2026-08-14 by review-loop)

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Runners:

- [primary rebuild, census, and family runner](../scripts/physical_cell_cutting_census_families_cycle748_2026_08_08.py)
- [independent opposite-pivot census checker](../scripts/physical_cell_cutting_census_families_cycle748_independent_check_2026_08_08.py)

Both runners are co-load-bearing. The checker imports no symbols from the
primary. It reconstructs the finite object with the opposite exact-cover
pivot, rebuilds and semantically verifies every symmetry generator, and
rederives the census, group families, overlap profiles, XOR family, and
conditional weight-18 shape bound. An audit packet for this note is incomplete
without the checker.

Direct dependencies:

- [Cycle 746 full-inventory parity classification](PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md)
- [Cycle 747 exact anchor census and flip-partner bracket](PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_CYCLE747_NOTE_2026-08-08.md)

Scope: exact identities of one supplied finite cutting system. Constitutional
effect: none. This package changes no axiom, framework Admissibility rule,
primitive, policy, or audit status. It adds no import or assumption to
`MINIMAL_AXIOMS_2026-06-29.md`; the framework memo is context, not a premise
of this finite GF(2) result.

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "resolve weight 18 exactly or classify the six weight-16 and twenty-six constructed weight-20 group families by intrinsic invariants"
```

## Status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "exact finite census and family theorem conditional on the current Cycle 746/747 evidence chain; independent audit remains unset"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite group-action census, exhaustive anchor transfer, overlap enumeration, direct GF(2) checks, and a conditional shape theorem on one supplied incidence table"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_census_families_cycle748_independent_check_2026_08_08.py
```

The packet-helper declaration is a hard landing condition: the matching
claim-scoped entry must exist in both supported helper registries before this
row is dispatched to independent audit.

## Inputs and provenance

Cycle 746 supplies a current primary and independent certificate for the full
15,800-row pair inventory and the even-total carrier-parity boundary. Cycle
747 supplies current primary and independent certificates for the exact 192
all-marked weight-8 carriers, the exhaustive eleven-carrier weight-16 anchor
census, the target-fixing transitive action, and the unresolved `{18,20}`
flip-partner bracket. This package binds all four receipts by schema, status,
source hash, declared-input hashes, and load-bearing semantic fields, then
rebuilds the incidence and support families locally.

The supplied finite choices are the one coordinate four-cube, its 192-column
support order, the exact 15,800 cutting rows, the named binary targets `one`,
`four`, and `four-flip`, and anchor column 144. No physical charge
identification, measured constant, probability, dynamics, state, readout,
source, arbitrary-domain rule, or continuum interpretation is imported.

## Headline

[Cycle 747](PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_CYCLE747_NOTE_2026-08-08.md)
binds the exact earlier result that `four` needs sixteen pieces to carry it
and has eleven sixteen-piece carriers through one fixed anchor piece. That was
an anchored count: it said what passes through one piece, not what the system
contains. This cycle answers the whole-system question.

The symmetries of the incidence table close into a group of 384 which is
transitive on the 192 pieces and permutes the 192 eight-piece carriers of the
all-marked reading among themselves. Carrying the anchored eleven around by
that group produces 132 sixteen-piece carriers of four, each checked back
against the incidence directly, and every one of the 192 pieces sits on exactly
eleven of them. Eleven is the same count the anchored sweep returned, so every
piece stands to the 132 exactly as the anchor does, and the 132 are all of
them: the census is complete, not a sample.

The 132 are not one family. The group cuts them into six, of sizes 12, 12, 12,
24, 24 and 48. This is a real structural fact about the object and not a
bookkeeping artifact: the symmetries of the table do not carry every smallest
carrier of the charge onto every other one, even though they carry every piece
onto every other one. Transitivity on pieces does not descend to transitivity
on the smallest carriers.

The overlap ceiling of the previous cycle now holds for the system rather than
for the anchor. Across all 25344 pairs of a smallest carrier of four with an
eight-piece carrier of the all-marked reading, the overlap is 0 in 14592 cases,
1 in 4608 and 2 in 6144, never more; each of the 132 meets those carriers 128
times with multiplicity. The 6144 pairs at the cap give 6144 different
twenty-piece carriers of the flip partner of four, one per pair with no
collisions, every one of the 192 pieces on exactly 640 of them, falling into
twenty families of 192 and six of 384.

The same two measurements constrain the one size still undecided. Were an
eighteen-piece carrier of the flip partner to exist, it could share at most 4
pieces with any eight-piece carrier of the all-marked reading.

## The rebuilt system

The runner rebuilds the incidence table of the cutting system from scratch:
15800 distinct cuttings on 192 pieces, each cutting using 24 pieces, each piece
sitting in 1975 cuttings. A set of pieces carries a reading when the cuttings it
meets an odd number of times are exactly the ones the reading marks. The
all-marked reading marks all 15800; the charge called four marks 5664; the flip
partner of four marks the remaining 10136.

The all-marked reading needs exactly 8 pieces, and its eight-piece carriers are
exactly the 192 sets of eight pieces that no cutting uses twice, one for each
piece of the object. Each piece lies on 8 of them, and two of them share 0, 1, 2
or 4 pieces, never 3, with counts 15072, 1920, 960 and 384. These facts are
re-derived and re-gated here rather than carried over.

## Why the anchored eleven decide the system

Two measurements license the transfer. The 48 geometric symmetries that fix a
basic reading have four piece orbits of size 48, so they do not by themselves
make an anchored sweep a whole-system statement. Adjoining the two explicitly
verified target-fixing incidence symmetries `b0` and `b1` gives a group of 384
with one orbit on the 192 pieces. Every element sends an eight-piece carrier of
the all-marked reading to another one, so that family of 192 is stable under
the group.

Because the group fixes the reading, it sends a carrier of four to a carrier of
four. The images of the anchored eleven are therefore carriers of four, and the
runner does not take that on trust: it recomputes the incidence sum of every
image directly and reports zero failures.

Completeness follows from the count rather than from a further search. Any
sixteen-piece carrier of four contains some piece; a group element carries that
piece to the anchor; the image is a sixteen-piece carrier of four through the
anchor, hence one of the eleven the anchored sweep found; so the original is in
the census. The arithmetic confirms it in place: every one of the 192 pieces
sits on exactly eleven members of the 132, the same eleven the anchored sweep
returned at the anchor.

## Six families, five profiles

Sorting the 132 by the group gives six families, of sizes 12, 12, 12, 24, 24
and 48. Sorting them instead by how they meet the 192 eight-piece carriers of
the all-marked reading gives only five profiles, of sizes 12, 12, 24, 36 and 48.

The profile is constant on a family, since the group permutes the eight-piece
carriers among themselves, so the profile is a coarsening of the family
structure. Five profiles from six families therefore means one profile is shared
by two families, and the sizes say which: the profile of size 36 covers a family
of 12 and a family of 24. The overlap pattern with the eight-piece carriers is a
genuine separator, but not a complete one.

## The ceiling at twenty, for the system

Adding an eight-piece carrier of the all-marked reading to a sixteen-piece
carrier of four gives a carrier of the flip partner of four, because a reading
and its flip partner differ by the all-marked reading. The size of the sum is 24
less twice the overlap, so the smallest sums come from the largest overlaps.

Every one of the 25344 pairs is measured here, not only those through the anchor. The
overlap takes the value 0 in 14592 pairs, 1 in 4608 and 2 in 6144, and never
exceeds 2. The cap of 2 is therefore a property of the whole system rather than
of the anchored eleven, and the smallest sum built this way has twenty pieces.

The 6144 pairs at the cap give 6144 distinct twenty-piece carriers: the map from
pair to sum is injective, with no two pairs landing on the same set. Every one of
them checks back against the incidence, every one of the 192 pieces sits on
exactly 640 of them, and the group sorts them into twenty families of 192 and
six of 384, which accounts for all 6144.

## What an eighteen-piece carrier would have to look like

The least size for the flip partner of four is bracketed between eighteen and
twenty by the previous cycle, with eighteen undecided. Suppose an eighteen-piece
carrier of the flip partner existed and met some eight-piece carrier of the
all-marked reading in k pieces. Their sum carries four and has 26 less twice k
pieces. For k at least 6 that is under sixteen, which no carrier of four
achieves. For k equal to 5 it is exactly sixteen, so the sum is a member of the
census, and it meets the eight-piece carrier in 8 less 5 pieces, which is 3 and
breaks the cap of 2. So k is at most 4.

This is a derivation from two measured inputs rather than a search: the least
size sixteen for four, and the whole-system cap of 2. The previous cycle stated
the same bound from the anchored cap; the input here is the system-wide one, so
the conclusion no longer inherits an anchored scope. It does not settle
eighteen — the totals it permits remain consistent with such a carrier existing
— but it is a shape constraint any construction or refutation at eighteen must
respect.

## Proof contract and obligation graph

**Exact target.** On the one supplied 15,800-by-192 incidence object, prove
that the complete minimum weight-16 `four` census contains 132 carriers,
partition it under the declared order-384 target-fixing group, enumerate its
overlaps with every minimum `one` carrier, and derive only the licensed
conditional consequence for a hypothetical weight-18 `four-flip` carrier.

The proof has six leaves:

1. Reconstruct the exact incidence, target identities, and full pair
   inventory — discharged independently here and bound to the current Cycle
   746 primary/independent receipts.
2. Establish the exhaustive eleven-carrier weight-16 anchor census —
   discharged by the local exact search and exact equality with the current
   Cycle 747 primary/independent supports and split inventory.
3. Establish a target-fixing transitive action — discharged by direct row and
   target checks for the 48 geometric maps, `b0`, and `b1`, closure to order
   384, and the one-orbit calculation.
4. Transfer the anchor census globally — discharged by mapping an arbitrary
   carrier's contained column to the anchor, plus 132 direct target checks and
   the regularity identity `132*16 = 192*11`.
5. Enumerate group families and all overlaps — discharged by exhaustive
   finite orbit closure, all `132*192 = 25,344` intersections, and a second
   implementation with the opposite exact-cover pivot.
6. Derive the conditional weight-18 shape boundary — discharged by GF(2)
   addition, the exact minimum 16 for `four`, and the system-wide overlap cap
   2. Existence or nonexistence at weight 18 is not a leaf of this theorem.

There is no unresolved leaf in the 132-carrier census, the stated family
partitions, or the `k<=4` implication. Classification by intrinsic invariants
and the weight-18 existence question are explicit continuations.

## No-Go Discipline: N1–N8

The package makes an exact finite completeness statement and preserves an
unresolved weight-18 boundary, so the complete stress record is required.

### N1 — alternative routes

1. **ATTEMPTED — direct global search.** The primary exhausts the anchor at
   weight 16, then uses the verified transitive group to enumerate every
   global image and rechecks all 132 against the incidence.
2. **ATTEMPTED — independent reconstruction.** The checker chooses the
   greatest uncovered exact-cover sample, rebuilds all rows and columns, and
   rederives the same census and families without importing primary symbols.
3. **ATTEMPTED — unanchored escape.** An arbitrary weight-16 carrier contains
   a column; transitivity maps it to the anchor, where the exact Cycle 747 and
   local inventories contain all eleven answers. No unanchored orbit remains.
4. **ATTEMPTED — subgroup-only transfer.** The 48 geometric maps leave four
   48-column orbits and fail. The two additional row- and target-preserving
   involutions are therefore named, checked, and required.
5. **ATTEMPTED — profile classification.** Overlap profiles give five classes,
   not six; the size-36 profile combines one 12-orbit and one 24-orbit, so the
   profile is retained only as a coarsening.
6. **ATTEMPTED — constructive weight-18 attack.** XOR with every all-marked
   weight-8 carrier yields weight 20 at the overlap cap 2, not 18. The package
   converts this failed construction only into the conditional `k<=4` shape
   constraint and makes no emptiness claim.

### N2 — wall independence

Anchor completeness, group transitivity, direct target preservation, family
closure, and overlap enumeration are independently gated obligations. The
weight-18 open question is not used in the weight-16 census. The conditional
shape bound uses only the exact weight-16 lower boundary and the separately
enumerated system-wide overlap cap; it does not use the resource-limited
weight-18 sweep from Cycle 747.

### N3 — hidden-wall scan

Review found a stale loop that advanced 200 rows while processing 100. The
repair processes all 15,800 first endpoints and keeps the 7,900-row mutation
as a hostile rejector. It also exposes the two nongeometric generators that
the submitted transitivity language had hidden, binds both landed dependency
receipts and their independent counterparts, and rejects zero-exit failures.
“Complete,” “family,” and “system-wide” now refer only to the supplied finite
incidence, target, and declared group action.

### N4 — residual matching

| Cited source | Residual established there | Residual used here | Match |
|---|---|---|---|
| [Cycle 746 parity](PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md) | exact 15,800-row inventory and carrier-parity classification | full-inventory dependency boundary | yes |
| [Cycle 747 bracket](PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_CYCLE747_NOTE_2026-08-08.md) | exact 192 all-marked carriers, exhaustive eleven-carrier anchor census, and unresolved weight 18 | census inputs and honest open boundary | yes |

No cited residual proves more than is consumed. In particular, Cycle 747's
26 unexecuted weight-18 joins remain an open residual and are not repackaged
as evidence of nonexistence.

### N5 — resolution execution

- `per_element`: checked for all 192 support columns.
- `per_site`: checked and not executed; no framework site is identified.
- `per_mode`: checked and not executed; no field or momentum modes occur.
- `per_block`: checked for all 15,800 cutting rows and every exact anchored
  search block through weight 16.
- `lattice_wide`: checked and not executed; no multicell or continuum claim.

Both executables print these five resolution lines in their live evidence.

### N6 — partial-closure path scan

The six weight-16 families may be distinguished by an intrinsic invariant,
and weight 18 may be settled by an exact construction, search certificate, or
proof-level obstruction. Neither continuation requires a new axiom,
primitive, physical interpretation, or convention. Other targets, incidence
tables, noncorner pieces, arbitrary domains, and multicell systems are
different supplied problems.

### N7 — steelman

The strongest objection is that a weight-16 carrier lies outside the orbit of
the eleven anchor answers. That would require either a nontransitive action, a
generator that fails to fix `four`, or an incomplete anchor inventory. The
checker independently rejects all three possibilities by direct row/target
actions, one-orbit closure, and exact dependency equality. A second objection
is that 6,144 overlap-two pairs collide after XOR; independent set enumeration
finds 6,144 distinct supports, exactly the pair count, and directly checks
every support against `four-flip`.

### N8 — cross-cycle echo

Cycle 746 teaches that a half-width pair scan cannot license a whole-system
claim. Cycle 747 teaches that the 48 geometric maps alone are not transitive
and that weight 18 remains open. This package imports those exact lessons and
current receipts, but does not echo their finite conclusions into another
incidence system or promote the open boundary into a theorem.

## Review record (review-loop, 2026-08-14)

The submitted package was not landable as written. It repeated the
7,900-of-15,800 pair-inventory bug, relied on one self-attesting executable,
carried stale backticked dependencies, used invalid claim/status vocabulary,
omitted the proof/trace/N1–N8 surfaces, wrote no fail-first receipt, and exited
zero even if a gate failed.

The repair covers the full pair inventory, binds exact current Cycle 746/747
primary and independent receipts, names and semantically checks the actual
transitive generator set, adds a non-importing opposite-pivot checker,
preserves hostile mutations for every load-bearing boundary, writes canonical
fail-first receipts, and exits nonzero on failure. The science remains narrow:
the group families are counted rather than intrinsically classified, the
6,144 weight-20 supports are only the stated XOR construction, and weight 18
remains open.

Hard landing conditions are: (a) the claim-scoped packet-helper mapping exists
in both supported registries; (b) fresh primary and independent receipts and
canonical runner caches bind the final sources and declared inputs; and (c)
the citation-graph manifest is generated on the actual landing tree.
Independent audit remains required; this review record grants no audit verdict
or effective grade.

## Boundary and honest read

- Every statement here is about the finite cutting system. No physical reading
  of the readings, the carriers, the census or the families is claimed.
- The census of 132 is complete for the charge called four at size sixteen, and
  its completeness rests on two gated facts: the anchored sweep at sixteen is
  complete and returns eleven, and the group is transitive on the 192 pieces.
  Both are checked by the primary and independently reconstructed by the
  checker.
- The six families are the families of the group of 384 recorded in this
  runner, which is generated by the 48 together with the two extra symmetries
  the table admits. This note does not claim that group is the full symmetry
  group of the table; that larger classification is not assumed here.
- The cap of 2 and the resulting ceiling of twenty are exact for sums of a
  smallest carrier of four with an eight-piece carrier of the all-marked
  reading. This note does not claim that every twenty-piece carrier of the flip
  partner arises that way, and the 6144 counted here are the ones that do.
- The bound of 4 at eighteen is conditional on such a carrier existing. Nothing
  here asserts that one does, and nothing here asserts that none does. The
  bracket between eighteen and twenty is unchanged by this package.
- The families of the 132 and of the 6144 are counted, not classified. This note
  names no invariant that tells the two families sharing a profile of size 36
  apart, and finding one is open.
- Nothing here bounds the least size for the other charges or for their flip
  partners.
- Both runners print named fail-closed gates and the five-line resolution
  certificate; their canonical caches and receipts bind the exact landed
  sources and inputs.
