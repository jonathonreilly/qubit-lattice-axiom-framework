# Block-parity licensing for seventeen supplied targets — Cycle 746

Date: 2026-08-08 (revised 2026-08-14 by review-loop)

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Runner:

- [primary rebuild and parity derivation](../scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py)
- [independent opposite-pivot checker](../scripts/physical_cell_cutting_carrier_parity_law_cycle746_independent_check_2026_08_08.py)

Both runners are co-load-bearing. The independent checker reconstructs the
finite object with the opposite exact-cover pivot and does not import primary
symbols, so an audit packet for this note is incomplete without it.

Direct dependency:

- [Cycle 745 exact target population and identities](PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md)

Constitutional effect: none. This package changes no axiom, framework
Admissibility rule, primitive, policy, or audit status. It adds no import or
assumption to `MINIMAL_AXIOMS_2026-06-29.md`; that framework memo is context,
not a premise of the finite result.

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "test whether these necessary parity licenses materially reduce a later exact carrier search; no downstream consumer is yet claimed"
```

## Status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "exact finite result conditional on the Cycle 745 target-identity package and its independent dependency-chain closure"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite GF(2) classification and split-profile counts for one supplied incidence table and seventeen realizable supplied targets"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_carrier_parity_law_cycle746_independent_check_2026_08_08.py
```

The packet-helper declaration is a hard landing condition: the matching
claim-scoped entry must exist in `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in both
the citation-graph builder and packet-dependency helper before this row is sent
to independent audit.

## Inputs and provenance

### Load-bearing dependency

- Cycle 745 supplies the ordered target names, exact witness supports, planted
  controls, and the inconsistent-control identity. Both Cycle 746 runners bind
  the current primary and independent Cycle 745 receipts and recheck the target
  semantics against an independently reconstructed incidence table. This
  package remains conditional support unless that dependency and this row
  independently achieve retained-grade chain closure.

### Supplied finite-domain choices

- the one coordinate four-cube, its corner-simplex family, the declared
  192-column support order, the two halves and four 48-column quarters, and the
  finite target population named above;
- the reported profile-count range, support sizes 1 through 20, and the Q3
  anchor condition used only for the stated split-count comparison.

These are exact discrete inputs and scope choices, not measured or fitted
physical values. No literature constant, observational comparator,
normalization, state choice, probability value, or physical charge
identification is imported.

## Corrected bounded result

In the exact supplied 15,800-by-192 binary incidence table, consider the
seventeen Cycle 745 targets that lie in the incidence column space. For each
target, every carrier support has fixed parity on the total support, the two
96-column halves, and quarters Q2 and Q3. Parities on Q0 and Q1 are free.
Because each half is a union of two quarters, three forced parities suffice:

\[
(|S|,\ |S\cap Q_2|,\ |S\cap Q_3|)\pmod 2.
\]

The seventeen realizable targets occupy exactly two triples:

- `(0,0,0)`: fifteen targets, including all six named nonconstant charge
  readings;
- `(0,1,1)`: two planted controls.

Therefore every carrier of any of the six named charge readings has even
size and meets Q2 and Q3 evenly. This is a necessary licensing condition, not
a carrier-existence or sufficiency theorem.

The submitted note incorrectly reported three realizable classes. Its alleged
third class was produced solely by `odd-ctl`, the deliberately planted one-hot
inconsistent target from Cycle 745. In the repaired canonical row ordering,
that control's formal row-space projection has triple `(0,0,0)`, but this
projection is not a carrier invariant because exact augmented GF(2)
elimination proves that `odd-ctl` is not in the incidence column space. It
remains in this package only as a hostile rejector and is not called a reading
or carrier class.

The repaired control puts its single bit on the lexicographically least
packed incidence row and binds that row's hash. The submitted `row 0` form was
traversal-order-dependent and would name a different cutting under the
checker’s opposite exact-cover pivot.

## Exact finite object and provenance

Both executables rebuild the exact-cover population: 15,800 distinct cutting
rows on 192 used support columns, with row weight 24, column weight 1,975,
and GF(2) rank 88. They bind Cycle 745's current primary and independent
receipts, exact source/input closure, canonical row-order-independent
incidence identity, support-column order, ordered 18-target population,
per-target function identities and column-space status, four fixed-control
supports, seeded five-control specification and supports, and the explicit
non-column-space status of `odd-ctl`.

The primary exact-cover traversal chooses the least uncovered sample; the
checker chooses the greatest. Target identity is compared by canonical hashes
of incidence-row bytes paired with target bits, so differing row traversal
orders do not weaken the binding.

The submitted move scan repeated an earlier chunking defect: it advanced by
200 rows but processed only 100, covering 7,900 of 15,800 possible first
endpoints. The repaired scan covers all 15,800. The complete inventory leaves
the reconstructed target functions and final parity numbers unchanged. A
hostile inventory gate preserves the skipped loop as a rejected control.

## Linear-algebra derivation

Write the incidence matrix as

\[
I\in\mathbb F_2^{15800\times192}.
\]

A support vector `x` carries target `f` exactly when `Ix=f`. A block indicator
`u` has target-forced parity precisely when `u` lies in the row space of I:
if `u=y^T I`, then every solution obeys

\[
u\cdot x=y\cdot f.
\]

If `u` is outside the row space, a kernel vector `k` exists with `Ik=0` and
`u·k=1`; whenever one carrier exists, `x` and `x+k` realize both block
parities. Thus “free” is proved only for realizable targets. This is why the
inconsistent odd control cannot legitimately form another carrier class.

Exact elimination gives row rank 88 and kernel dimension 104. The primary
constructs a 104-vector kernel basis and checks every vector against all
15,800 rows, not only against pivot rows. Its basis vectors have weights 8
through 20; that interval describes this basis only and is not a minimum
kernel-weight theorem.

Among the seven declared block indicators, the row-space members are
`total`, `L`, `R`, `Q2`, and `Q3`; Q0 and Q1 are outside. The independently
constructed kernel basis meets Q0 and Q1 oddly but meets every fixed block
evenly. The identities

\[
R=Q_2+Q_3,\qquad L=\mathrm{total}+R
\]

then reduce the five fixed parities to the three stated coordinates. Because
every column occurs in the odd number 1,975 of rows, the total-support parity
also equals the parity of the target's Hamming weight.

## Proof contract and obligation graph

**Exact target.** For every realizable target in the supplied Cycle 745
population, classify which of the seven declared block indicators have a
carrier-independent parity, derive the resulting three-coordinate class, and
count the licensed split profiles on the stated finite size range.

The proof has four leaves:

1. Reconstruct the declared 15,800-by-192 incidence table and target identities
   with traversal-independent hashes — discharged independently by both
   runners.
2. Prove the fixed/free criterion: a block parity is fixed on a nonempty affine
   solution set exactly when its indicator is in the row space; otherwise a
   kernel vector flips it — discharged by the row-space/annihilator identity
   over `GF(2)` and explicit kernel bases of dimension 104.
3. Reject inconsistent targets before classifying carrier parities — discharged
   by two augmented eliminations with opposite pivot conventions.
4. Count only profiles satisfying the three necessary parities — discharged by
   direct four-variable enumeration and the closed finite sums stated below.

There is no unresolved terminal lemma. Degenerate zero and constant targets are
included when realizable; `odd-ctl` is excluded from the carrier quantifier
because its affine solution set is empty. The proof does not cross the explicit
boundary from necessary profile licensing to carrier existence or sufficiency.

## Finite licensed-split counts

A split is a quadruple `(q0,q1,q2,q3)` of nonnegative integers summing to
the candidate support size, with each entry at most 48. These counts enumerate
split profiles satisfying the necessary parities. They do not count carriers.

For even sizes 2 through 20, the all-even class licenses

`5,14,30,55,91,140,204,285,385,506`

profiles. Requiring `q3≥1` leaves

`1,5,14,30,55,91,140,204,285,385`.

On this measured range, for size `2k` these are respectively

\[
\sum_{j=1}^{k+1}j^2,
\qquad
\sum_{j=1}^{k}j^2.
\]

Their difference is `(k+1)^2`. Thus the anchored profile count at one listed
size equals the unanchored count at the preceding listed size. This is a
profile-count identity; “one size step” is not a wall-clock or solver-cost
claim.

The `(0,1,1)` class licenses

`1,5,14,30,55,91,140,204,285,385`

profiles at the same sizes, all already having `q3≥1`. Direct enumeration of
all four Q2/Q3 parity pairs independently reproduces the two formulas and
shows that only `(0,0)` gives the all-even sequence. Across sizes 1 through
20, the three-parity predicate agrees with the runner's block-licensing test
on every one of the 180,625 pairs of a split and a realizable target.

## No-Go Discipline: N1–N8

The claim excludes other fixed/free blocks and excludes an apparent third
realizable class, so the finite negative statements receive the complete
stress record.

### N1 — alternative routes

Five distinct attacks were executed against the finite negative statements:

1. **ATTEMPTED — direct row-space attack.** Reduce all seven block indicators
   against the exact primary row basis; this fails to add another fixed block
   because only `total`, `L`, `R`, `Q2`, and `Q3` reduce to zero residual.
2. **ATTEMPTED — kernel-witness attack.** Construct the full 104-vector kernel
   basis and seek an odd pairing with each allegedly fixed block; this fails
   for the five fixed blocks but succeeds for Q0 and Q1, independently
   separating fixed from free.
3. **ATTEMPTED — traversal-independence attack.** Rebuild the table with the
   opposite exact-cover pivot and repeat augmented elimination; this fails to
   produce another realizable class and again rejects `odd-ctl`.
4. **ATTEMPTED — column-weight attack.** Re-derive total-support parity from
   the odd column weight 1,975 rather than the stored row combinations; this
   fails to produce an odd-size realizable class.
5. **ATTEMPTED — direct profile-enumeration attack.** Enumerate every
   four-quarter split through size 20 without consulting the incidence
   solver; this fails to disagree with the licensing predicate on any of the
   180,625 split-target pairs.

### N2 — wall independence

There is no named external wall set, so a pairwise wall table is not
applicable. The three internal obligations are nevertheless separated: block
classification depends only on exact row space and kernel; target-class
membership depends on exact augmented consistency and forced RHS parities;
and the combinatorial count formulas use only the resulting parity triples.
No carrier-search nonexistence or Cycle 745 census count is used to prove the
parity law.

### N3 — hidden-wall scan

The crucial hidden wall was realizability. Treating all supplied vectors as
readings let the inconsistent `odd-ctl` contaminate the class census. The
repaired runner checks `Ix=f` consistency for every target before classifying it. It
also distinguishes free block parity from existence of a carrier at any
specified size.

The checklist terms “canonical” and “by construction” occur only in the
non-load-bearing sense of row-order-independent identifiers and explicitly
seeded controls. No “we assume,” “as is standard,” “framework provides,”
“bridge context,” “background,” “naturally,” “obviously,” “standard QFT,” or
“registered” phrase supplies a proof step.

### N4 — residual matching

| Cited source | Residual established there | Residual used here | Match |
|---|---|---|---|
| [Cycle 745 target population](PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md) | seventeen realizable named targets plus one exact inconsistent hostile control | the exact right-hand sides whose block parities are classified here | yes |

No prior no-go is used. For a realizable target and a block outside the row
space, the kernel-orthogonality argument constructs the residual parity flip.
For a block inside the row space, the exact row combination fixes its parity.
These cases exhaust the seven block indicators. The inconsistent control is
separately rejected and has no carrier residual.

### N5 — resolution execution

- `per_element`: checked for all 192 support columns.
- `per_site`: checked and not executed; no framework site is identified.
- `per_mode`: checked and not executed; no field or momentum modes occur.
- `per_block`: checked for all seven block indicators and all supplied targets.
- `lattice_wide`: checked and not executed; no multi-cell or continuum claim.

“Licenses” means satisfies necessary block-parity conditions. It does not mean
that a carrier exists. “Charge” is only the inherited name of six exact
binary targets; no physical charge interpretation is asserted. Closed forms
are reported only on the explicitly checked finite ranges.

### N6 — partial-closure path scan

No new axiom, primitive, convention, or physical bridge is needed to alter the
finite negative boundary. Another support partition, target family, or
incidence table would be a different supplied finite problem, not a
convention-based closure of this one. The positive continuation is explicit:
use the necessary licenses to search for carriers and test sufficiency, without
promoting the present classification into an existence statement. The
primitive registry supplies no additional content relevant to this finite
linear-algebra question.

### N7 — steelman

The strongest competing explanation is that Q0 or Q1 is actually fixed for a
particular target despite being free generically. For every realizable target,
adding the explicitly checked kernel vector that pairs oddly with the block
preserves `Ix=f` and flips that block parity. Conversely, no such vector can
flip a row-space block. This proves target-by-target freedom and fixation.

### N8 — cross-cycle echo

Cycle 745 supplies the exact target population and uses `odd-ctl` as a control;
this package preserves that role rather than promoting the control to science.
The similar finite emptiness boundaries in `Cycle 741` and the exact control
rejection in `Cycle 745` have not been retired by a convention or primitive;
they remain scope-bounded exhaustive statements. Cycles 742–744 are context
only here: no automorphism-completeness, hidden-geometry, or carrier-census
result is imported into the parity proof.

## Review record (review-loop, 2026-08-14)

The submitted result was not landable as written. Its third alleged class came
only from treating the inconsistent `odd-ctl` vector as though it had a
carrier, and its pair scan skipped half of the possible first endpoints. The
review repair rejects that target before classification, makes the control
row-order independent, covers all 15,800 pair endpoints, adds a non-importing
opposite-pivot checker, and narrows every surface to necessary parity licensing
and finite profile counts. It also records the complete proof contract,
dependency/import boundary, trace/status fields, and N1–N8 negative-claim
discipline.

Hard landing conditions are: (a) the claim-scoped packet-helper mapping for the
independent checker exists in both supported helper registries; (b) fresh
primary and independent receipts and canonical runner caches bind the final
sources and declared inputs; and (c) the citation-graph manifest is regenerated
on the actual landing tree. Independent audit remains required; this review
record grants no verdict or effective grade.

## Boundary and honest read

- Exact: one supplied 15,800-by-192 binary incidence table, the declared
  support-column ordering, seventeen exact realizable targets, and one
  inconsistent hostile control.
- Exact: necessary block-parity conditions and split-profile counts over the
  sizes stated above.
- Not claimed: existence or count of carriers at any profile, sufficiency of a
  licensed profile, physical charge, search-runtime complexity, other target
  families, other support partitions, noncorner/nonsimplicial pieces,
  multi-cell compatibility, framework Admissibility, arbitrary lattice size,
  boundaries, thermodynamic limits, or continuum physics.
- Audit remains unset; an independent audit is still required.
