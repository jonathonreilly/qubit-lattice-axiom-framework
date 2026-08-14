# Intrinsic pair signatures classify the minimum carriers — Cycle 749

Date: 2026-08-08 (revised 2026-08-14 by review-loop)

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Runners:

- [primary dense-Gram rebuild and separator runner](../scripts/physical_cell_cutting_family_separator_cycle749_2026_08_08.py)
- [independent opposite-pivot row-streaming checker](../scripts/physical_cell_cutting_family_separator_cycle749_independent_check_2026_08_08.py)

Both runners are co-load-bearing. The checker imports no symbols from the
primary. It reconstructs the cutting population with the opposite exact-cover
pivot, verifies the declared group action, and increments unordered pair counts
by streaming every cutting support rather than using the primary's dense Gram
product. An audit packet for this note is incomplete without the checker.

Direct dependency:

- [Cycle 748 complete carrier census and group-family theorem](PHYSICAL_CELL_CUTTING_CENSUS_FAMILIES_CYCLE748_NOTE_2026-08-08.md)

Scope: exact identities of one supplied finite cutting system. Constitutional
effect: none. This package changes no axiom, framework Admissibility rule,
primitive, policy, or audit status. It adds no import or assumption to
`MINIMAL_AXIOMS_2026-06-29.md`; that framework memo is context rather than a
premise of this finite GF(2) theorem.

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "derive a closed-form description of the six intrinsic signatures and the two maximum-pair values"
```

## Status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "exact finite intrinsic classification conditional on the current Cycle 748 primary and independent certificates; independent audit remains unset"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exhaustive finite pair-incidence classification on all 132 minimum carriers, with an independent opposite-pivot row-streaming implementation"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_family_separator_cycle749_independent_check_2026_08_08.py
```

The packet-helper declaration is a hard landing condition: the matching
claim-scoped entry must exist in both supported helper registries before this
row is dispatched to independent audit.

## Inputs and provenance

Cycle 748 supplies current primary and independent certificates for the exact
15,800-by-192 incidence object, the complete census of 132 minimum weight-16
`four` carriers, and their six orbits under the declared order-384
target-fixing incidence group. This package binds both receipts by schema,
status, source hash, declared-input hashes, processed-row count, census digest,
carrier count, and family sizes. It then rebuilds the incidence and repeats the
carrier and orbit checks locally.

The supplied finite choices are the coordinate four-cube, the 192-column
support order, the exact 15,800 cutting rows, the named binary target `four`,
and the declared incidence symmetries. No physical charge identification,
measured constant, probability, dynamics, state, readout, source,
arbitrary-domain rule, or continuum interpretation is imported.

## Exact result

For one of the 132 carriers, retain only its sixteen columns. For each of the
120 unordered column pairs, count how many of the 15,800 cutting rows contain
both columns, and sort those 120 counts. Call the resulting tuple the
carrier's intrinsic pair signature.

The declared order-384 group partitions the 132 carriers into six families of
sizes 12, 12, 12, 24, 24, and 48. The signature is constant on each family and
different between every pair of families. Thus the six signature classes are
exactly the six group orbits.

There is also a stronger, group-independent consequence. Every automorphism of
the incidence table preserves column co-incidence counts and therefore
preserves each sorted intrinsic pair signature. Since the declared group is
already transitive within each signature class, no larger incidence
automorphism group can merge two of the six classes. Proving that the declared
order-384 group is the full automorphism group is unnecessary for this orbit
classification.

## The strict refinement chain

Five carrier readings form a strict refinement chain. Each is constant on the
six declared group families, and each partition refines the preceding one.

| intrinsic reading | groups of families | family sizes held together |
| --- | ---: | --- |
| intersection histogram on the `four`-marked rows | 1 | 12+12+12+24+24+48 |
| sorted counts of zero co-incidences at each of the sixteen columns | 2 | 12+12+12+24 \| 24+48 |
| sum of the 120 pair co-incidence counts | 4 | 12 \| 12 \| 12+24 \| 24+48 |
| overlap profile with the 192 minimum all-marked carriers | 5 | 12 \| 12 \| 12+24 \| 24 \| 48 |
| complete sorted intrinsic pair signature | 6 | 12 \| 12 \| 12 \| 24 \| 24 \| 48 |

The fourth row is the five-profile result of Cycle 748. The fifth resolves its
single merged size-36 profile into the size-12 and size-24 group orbits. The
five tried readings do not define a natural hierarchy outside this finite
object; the theorem is only the exact refinement relation displayed here.

## Further exact identities

All 132 carriers have the same intersection histogram on the 5,664 rows marked
by `four`: 2,832 rows meet the carrier once and 2,832 meet it three times; no
marked row has any other intersection size.

For each carrier, exactly eight unordered pairs attain its largest pair count,
and those eight pairs cover all sixteen columns once. The largest value is 433
for 60 carriers and 666 for 72 carriers. As a declared control rather than a
probability estimate, the four cyclic spacings 1, 5, 7, and 11 give 768
sixteen-column sets, exactly one of which has the same maximum-pair property.

Across all `132 choose 2 = 8,646` unordered pairs of minimum carriers, the
intersection-size distribution is

| shared columns | carrier pairs |
| ---: | ---: |
| 0 | 4,926 |
| 1 | 960 |
| 2 | 1,440 |
| 4 | 960 |
| 8 | 360 |

These five counts exhaust all 8,646 pairs. In particular, intersection sizes
3, 5, 6, and 7 do not occur in this complete finite census.

## Proof contract and obligation graph

**Exact target.** On the supplied 15,800-by-192 incidence object and the
complete Cycle 748 weight-16 `four` census, prove that the sorted 120-entry
pair-co-incidence signature has exactly six classes equal to the declared
group orbits, and enumerate only the additional finite identities stated
above.

The proof has five leaves:

1. Reconstruct all 15,800 cutting rows and 192 support columns. The primary
   uses the least uncovered exact-cover sample and the checker uses the
   greatest; both obtain row weight 24 and column weight 1,975.
2. Reconstruct and semantically verify the complete 132-carrier Cycle 748
   census and the six declared group orbits. Both runners bind the current
   Cycle 748 primary and independent receipts before using them.
3. Compute the 192-by-192 co-incidence table. The primary uses an integer dense
   Gram product; the checker streams every cutting and increments unordered
   pairs, then compares with its independently rebuilt dense matrix.
4. Restrict the table to every carrier, derive the five readings, and compare
   their induced family partitions. Both runners obtain the strict group-count
   sequence 1, 2, 4, 5, 6 and six distinct final signatures.
5. Enumerate the marked-row histograms, maximum-pair graphs, declared controls,
   and all 8,646 carrier intersections. Every reported total is exhausted in
   place and mutation-checked.

There is no unresolved leaf in the finite classification. A closed-form reason
for the signature values, a physical interpretation, a multicell extension,
and the full incidence-group presentation remain outside the target rather
than terminal lemmas of this theorem.

## No-Go Discipline Gate

The exact non-occurrence claims in the complete overlap census trigger the
N1-N8 discipline even though the source row is a positive bounded theorem.

### N1 — alternative routes

1. **ATTEMPTED — missing-row attack.** A skipped half-inventory could create
   false pair counts; the primary now processes all 15,800 rows and rejects a
   hostile Cycle 748 receipt with 7,900 processed rows, while the [checker](../scripts/physical_cell_cutting_family_separator_cycle749_independent_check_2026_08_08.py)
   independently reconstructs all rows with the opposite pivot.
2. **ATTEMPTED — alternate pair-count formulation.** A dense Gram-product bug
   could manufacture the gaps; the checker instead streams each cutting's 24
   columns and increments its unordered pairs, and the two tables agree
   exactly.
3. **ATTEMPTED — incomplete carrier-family attack.** An omitted carrier could
   hide an extra signature or overlap; both runners bind and recheck the
   [Cycle 748 complete-census proof](PHYSICAL_CELL_CUTTING_CENSUS_FAMILIES_CYCLE748_NOTE_2026-08-08.md),
   including 132 carriers, eleven through every column, and the six family
   sizes.
4. **ATTEMPTED — subgroup artifact attack.** A larger incidence group might
   merge declared orbits; every incidence automorphism preserves the intrinsic
   signature, the signatures differ between all six declared orbits, and the
   declared group is already transitive within each one.
5. **ATTEMPTED — tally and mutation attack.** The checker exhausts all 8,646
   unordered carrier pairs and rejects hostile reintroduction of an
   overlap-three count; the five reported bins sum independently to 8,646.

The five routes differ respectively in their primary object and terminal
obligation: row inventory, pair-count implementation, census completeness,
group-action invariance, and exhaustive overlap tally.

### N2 — wall independence

The finite theorem has two load-bearing scoped inputs, not hidden physics
walls.

| pair | closing first closes second? | closing second closes first? | independent? |
| --- | --- | --- | --- |
| supplied exact incidence / complete Cycle 748 census | no | no | yes |

The first fixes co-incidence counts but not which supports are the complete
minimum-carrier census. The second fixes the supports only on the bound
incidence bytes. Neither is collapsed into the other.

### N3 — hidden-wall scan

The proof contains no use of “we assume,” “as is standard,” “the framework
provides,” “background,” “naturally,” “obviously,” or “standard QFT.” The
supplied finite choices and declared group are explicit scope inputs. The word
“complete” refers only to the Cycle 748 exhaustiveness proof that is linked and
receipt-bound; it is not an uncited assertion.

### N4 — residual matching

No prior no-go is cited as a witness. The sole scientific dependency is the
positive Cycle 748 census whose exact residual is the missing intrinsic
separator between its size-12 and size-24 families inside the shared size-36
profile. This theorem computes that separator on the identical 132 supports,
so the residual matches exactly.

### N5 — rhetoric audit

The negative statements are only that no larger *incidence-table
automorphism* can merge two signature classes and that overlap sizes 3, 5, 6,
and 7 do not occur among the 8,646 carrier pairs. Per element, all 192 columns
are checked. Per block, all 15,800 rows are used. Per site and per mode are not
applicable to this one finite combinatorial object. A lattice-wide statement is
not made. The primary cache carries the required substantive execution lines
for all five resolution classes.

### N6 — partial-closure and primitive scan

The primitive registry was checked. No framework axiom or approved primitive
supplies or is needed for this finite incidence theorem, and no new axiom is
requested. Relabeling the six classes would change names only; it would not
alter the six exact intrinsic signatures or close any scientific residual.

### N7 — steelman

A hostile reviewer should ask whether “family” was defined only relative to a
convenient subgroup and could disappear under an undiscovered table symmetry.
That would be decisive if the separator depended on the subgroup. It does not:
an incidence automorphism preserves every pair co-incidence count, hence the
sorted restricted signature, and the six subgroup orbits have six different
signatures. The strongest remaining counterroute is therefore a map that fails
to preserve incidence rows; such a map is not an automorphism of the supplied
object and does not attack the theorem's target.

### N8 — cross-cycle echo

Cycle 748 recorded the same shape of incompleteness: overlaps with the 192
all-marked carriers gave five profiles for six group families. That residual is
retired here by changing the invariant, not by importing authority: the full
120-entry intrinsic pair signature separates the merged pair. The mechanism
has been applied to the only prior same-support wall identified in this chain;
no similar retired convention or primitive route applies to finite pair
incidence.

No-Go discipline status: PASS for the narrow finite non-occurrence claims.

## Boundary

- The signatures and overlap gaps are exact only for this supplied finite
  15,800-by-192 object and the complete 132-carrier census.
- The theorem proves that larger incidence automorphisms cannot merge the six
  classes. It does not present or prove the full automorphism group.
- The maximum-pair matching is exhibited and counted, not explained by a
  closed-form structural theorem.
- The 1-of-768 spacing result is a declared control family, not a rarity or
  probability claim.
- No physical reading of the carriers, signatures, families, or pairings is
  claimed.
- Nothing here resolves the open weight-18 flip-partner question inherited by
  the broader cell-cutting program.

## Review record

The review repaired the submitted half-row pair scan, added nonzero failure
exit behavior, bound the current Cycle 748 primary and independent receipts,
added the opposite-pivot row-streaming checker, and replaced branch-local
status language with the controlled source-note fields above. The submitted
tracked cold stdout was removed; only canonical caches and fail-first receipts
remain.

Outstanding at landing, as hard landing conditions:

- the checker must be mapped to this claim id in both supported packet-helper
  registries;
- both canonical caches must bind the final sources and note;
- the citation manifest must be regenerated from the final proposed tree;
- audit status remains unset and may be changed only by the independent audit
  lane.
