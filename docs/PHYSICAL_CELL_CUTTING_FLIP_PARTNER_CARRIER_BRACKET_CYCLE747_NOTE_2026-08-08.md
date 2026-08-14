# The flip partner of four has minimum carrier size 18 or 20 — Cycle 747

Date: 2026-08-08 (revised 2026-08-14 by review-loop)

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Runners:

- [primary rebuild, construction, and bounded search](../scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08.py)
- [independent opposite-pivot reconstruction](../scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_independent_check_2026_08_08.py)

Both runners are co-load-bearing. The checker imports no primary symbols. It
reconstructs the finite object with the opposite exact-cover pivot, rederives
the all-marked carrier census, and recomputes the weight-20 construction from
the landed Cycle 745 supports. The lower-bound certificate also binds Cycle
745's independent weight-16 search and Cycle 746's opposite-pivot parity
checker. An audit packet for this note is incomplete without the checker.

Direct dependencies:

- [Cycle 745 exact weight-16 census and target identities](PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md)
- [Cycle 746 forced block-parity classification](PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md)

Constitutional effect: none. This package changes no axiom, framework
Admissibility rule, primitive, policy, or audit status. It adds no import or
assumption to `MINIMAL_AXIOMS_2026-06-29.md`; that framework memo is context,
not a premise of this finite result.

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "resolve the remaining exact weight-18 carrier question without promoting the present resource-bounded sweep into an emptiness certificate"
```

## Status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "exact finite bracket and construction conditional on the Cycle 745/746 dependency chain; independent audit remains unset"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite all-marked carrier classification, exhaustive lower-size search, constructive upper bound, and explicitly incomplete weight-18 residual on one supplied incidence table"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_independent_check_2026_08_08.py
```

The packet-helper declaration is a hard landing condition: the matching
claim-scoped entry must exist in both supported helper registries before this
row is dispatched to independent audit.

## Inputs and provenance

### Load-bearing dependencies

Cycle 745 supplies the exact identity of the finite incidence system and
targets, the eleven anchored weight-16 carriers of `four`, the complete
weight-16 emptiness certificate for `four-flip`, and a dependency-bound
through-14 search. Its primary and independent receipts are both current and
are checked semantically, not merely named.

Cycle 746 supplies the exact even-total parity law for all six named
nonconstant readings, including `four-flip`. Its primary and independent
receipts are likewise current and bound. The lower bound here uses the
Cycle-745 search only at weights through 16 and the Cycle-746 even-parity
result only to exclude odd weights.

### Supplied finite-domain choices

- the one coordinate four-cube, its corner-simplex family, the declared
  192-column support order, and the exact 15,800-row cutting incidence;
- the names `one`, `four`, and `four-flip` for three exact binary target
  vectors;
- the anchor column 144, used only with a verified target-fixing transitive
  action;
- the weight-18 table guard of 30,000,000 intermediate rows.

These are finite scope choices. No physical charge identification, measured
constant, state, probability value, dynamics, readout, source, or continuum
interpretation is imported.

## Corrected bounded result

Write the incidence matrix as

\[
I\in\mathbb F_2^{15800\times192}.
\]

A support vector `x` carries a target `f` exactly when `Ix=f`. Let `1` be the
all-marked target and let `f_4` be `four`. Its flip partner is

\[
f_{4\mathrm f}=f_4+\mathbf 1.
\]

On the supplied finite system:

1. the minimum carrier weight of `one` is exactly 8;
2. there are exactly 192 weight-8 carriers of `one`, and each support column
   lies in exactly 8 of them;
3. the eleven landed anchored weight-16 carriers of `four` meet those 192
   carriers in at most two columns;
4. their XOR sums at overlap two give 512 distinct weight-20 carriers of
   `four-flip`;
5. no carrier of `four-flip` exists at any even weight through 16;
6. every carrier of `four-flip` has even weight.

Therefore the minimum carrier weight of `four-flip` is either 18 or 20:

\[
18\le d(f_{4\mathrm f})\le20,
\qquad d(f_{4\mathrm f})\in2\mathbb Z.
\]

The weight-18 primary sweep is incomplete and is not used to prove the lower
bound. It searches 4,770 of 4,796 scheduled splits, refuses 26 over the
declared table guard, and finds no carrier. Weight 18 remains open.

## Why the all-marked minimum is exactly eight

Every support column occurs in 1,975 cutting rows. If `k` columns carry the
all-marked target, every one of the 15,800 rows must be met a positive odd
number of times, so

\[
1975k\ge15800,
\]

and `k≥8`. At `k=8` the two sides are equal. Consequently every cutting must
meet the support exactly once. This is equivalent to saying that no cutting
contains two selected columns.

The primary and checker independently form the column-pair relation “no
cutting contains both” and enumerate every eight-clique. Both obtain 192
supports, all of which directly reproduce the all-marked target. Each column
lies in eight of them. Across the `C(192,2)=18,336` unordered pairs, their
intersection sizes have counts

| intersection size | pair count |
|---:|---:|
| 0 | 15,072 |
| 1 | 1,920 |
| 2 | 960 |
| 4 | 384 |

No bijection between pieces and carriers is claimed; the equality of their
two counts is accompanied by the measured eight-to-eight incidence
regularity above.

## The constructive ceiling at twenty

If `x` is a weight-16 carrier of `four` and `y` is a weight-8 carrier of
`one`, then

\[
I(x+y)=f_4+\mathbf 1=f_{4\mathrm f},
\]

and

\[
|x+y|=16+8-2|\operatorname{supp}(x)\cap\operatorname{supp}(y)|.
\]

The eleven Cycle-745 anchored carriers are rebound and directly rechecked in
both Cycle-747 executables. Against the 192 all-marked carriers, their overlap
counts are `1,216`, `384`, and `512` at overlaps 0, 1, and 2. The 512
overlap-two pairs yield 512 distinct supports of weight 20, and every support
directly reproduces `four-flip`. This is an existence theorem at weight 20,
not a census of all weight-20 carriers.

## Why the anchored searches decide the stated whole-system question

The submitted note attributed transitivity to the 48 geometric symmetries.
That was false: those symmetries fix each basic target but have four piece
orbits of size 48. The repaired proof uses the actual verified generator set.

Two additional order-two incidence automorphisms, `b0` and `b1`, are rebuilt
and checked to fix every one of the eight basic targets. Together with the 48
geometric target stabilizers they generate a transitive action on all 192
support columns. Thus any nonempty carrier has a target-preserving image
through column 144. Empty anchored searches are therefore global emptiness
certificates at the searched weight. The checker separately binds Cycle 745's
independent semantic verification of the same transitive group and exact
weight-16 target search.

## Exhaustive lower-size boundary

Cycle 745's independent checker exhausts all 2,004 anchored weight-16 splits
for `four-flip`, obtains zero, and binds the through-14 predecessor search.
The repaired Cycle-747 primary also searches every even weight 2 through 16;
its locally reconstructed result is

| weight | `four` anchored count | `four-flip` anchored count |
|---:|---:|---:|
| 2 | 0 | 0 |
| 4 | 0 | 0 |
| 6 | 0 | 0 |
| 8 | 0 | 0 |
| 10 | 0 | 0 |
| 12 | 0 | 0 |
| 14 | 0 | 0 |
| 16 | 11 | 0 |

At weight 16 the two targets use the same 204 licensed anchored cells and
the same exact 2,004-split inventory. The eleven positive `four` answers
equal the Cycle-745 supports byte-for-byte. The Cycle-746 parity law excludes
odd weights. Hence no `four-flip` carrier exists below 18.

## Weight eighteen: explicit resource residual

The weight-18 primary sweep visits every one of the 285 licensed anchored
cells. Its split inventory has 4,796 entries. It searches 4,770 and refuses
26 joins in 11 cells because their predicted intermediate tables exceed the
30,000,000-row guard; the predicted sizes range from 31 million to 21,766
million rows. No searched split returns a carrier.

This is a bounded computational observation with a named residual. It is not
an emptiness theorem, a solver timeout verdict, or evidence against an
unsearched support. Because even parity leaves only 18 between the exact
lower-size boundary and the weight-20 construction, the honest result is the
two-value bracket `{18,20}`.

## Proof contract and obligation graph

**Exact target.** Determine a rigorous finite bracket for the minimum support
weight carrying `four-flip`, while keeping any resource-limited weight-18
observation outside the certified lower bound.

The proof has five leaves:

1. Reconstruct the 15,800-by-192 incidence and exact target identities —
   discharged by the primary and the opposite-pivot checker.
2. Prove and enumerate the weight-8 all-marked carriers — discharged by the
   incidence-count lower bound and exhaustive noncooccurrence clique census.
3. Prove a weight-20 `four-flip` construction — discharged by direct GF(2)
   addition, the exact overlap census, and 512 direct incidence checks.
4. Exclude all weights through 16 — discharged by the current Cycle-745
   primary/independent receipts, the locally rebuilt matched search, and the
   verified target-fixing transitive action.
5. Exclude odd weights — discharged by the current Cycle-746
   primary/independent parity receipts.

There is no unresolved leaf in the bracket proof. The exact weight-18 value is
a separate open continuation, not a hidden obligation in either inequality.

## No-Go Discipline: N1–N8

The package asserts exact finite nonexistence through weight 16 and names a
resource wall at weight 18, so the complete stress record is required.

### N1 — alternative routes

1. **ATTEMPTED — direct primary search.** Exhaust every licensed anchored
   split at each even weight through 16; `four-flip` remains empty while
   `four` returns the eleven known controls at 16.
2. **ATTEMPTED — independent predecessor search.** Bind Cycle 745's
   opposite-pivot syndrome-DP/MITM checker, which independently exhausts the
   weight-16 inventory and verifies the target-fixing group.
3. **ATTEMPTED — unanchored escape.** Rebuild all target-fixing generators.
   The 48 geometric symmetries alone fail transitivity, while adjoining the
   two verified involutions gives one 192-column orbit.
4. **ATTEMPTED — constructive attack.** Enumerate every all-marked weight-8
   carrier and XOR it with every landed anchored `four` carrier. This finds
   512 weight-20 witnesses but no weight-18 witness because the maximum
   overlap is two.
5. **ATTEMPTED — independent all-marked reconstruction.** Choose the greatest
   uncovered exact-cover pivot, rebuild the relation, and enumerate all
   eight-cliques without primary imports; the same 192 carriers and 512
   weight-20 sums result.
6. **ATTEMPTED — weight-18 bounded search.** Search all cells and all joins
   below the guard; 26 joins remain explicitly unexecuted, so this route is
   recorded as incomplete and supplies no negative conclusion.

### N2 — wall independence

The exact lower bound has two independent ingredients: finite emptiness
through weight 16 and even total parity. The constructive upper bound uses
neither. The weight-18 table guard is not used in the lower bound at all; it
governs only the separately labelled incomplete continuation. Target identity,
anchor completeness, and split execution are distinct obligations rather than
multiple names for one wall.

### N3 — hidden-wall scan

The review found two hidden conditions in the submission: a 200-row stride
processed only 100 rows, and the claimed 48-symmetry transitivity silently
used `b0` and `b1`. The repair covers all 15,800 first endpoints, preserves
the skipped-half loop as a hostile rejector, and names/tests the two extra
target-fixing generators. “Guard,” “anchor,” and “supplied” now identify
explicit finite inputs rather than standing in for completeness.

### N4 — residual matching

| Cited source | Residual established there | Residual used here | Match |
|---|---|---|---|
| [Cycle 745 census](PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md) | exact target identities, eleven anchored `four` carriers, and no `four-flip` carrier through weight 16 | lower-size boundary and constructive inputs | yes |
| [Cycle 746 parity](PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md) | every carrier of the six nonconstant targets has even total weight | exclusion of odd weights | yes |

The weight-18 residual is exactly the 26 unexecuted joins. It is not matched to
or disguised as either predecessor result.

### N5 — resolution execution

- `per_element`: checked for all 192 support columns.
- `per_site`: checked and not executed; no framework site is identified.
- `per_mode`: checked and not executed; no field or momentum modes occur.
- `per_block`: checked for all 15,800 rows, every exact split through weight
  16, and the complete declared weight-18 split inventory.
- `lattice_wide`: checked and not executed; no multicell or continuum claim.

Both executables print these five resolution lines in their live evidence.

### N6 — partial-closure path scan

Weight 18 can be settled by an exact finite certificate, a different exact
join organization, or a proof-level replacement. None requires a new axiom,
primitive, physical interpretation, or convention. Other targets, incidence
tables, noncorner pieces, or multicell systems are different supplied
problems. The primitive registry adds no content to this finite GF(2)
question.

### N7 — steelman

The strongest objection is that a hidden carrier sits outside the anchor or
inside one of the refused weight-18 joins. The first possibility is excluded
by the semantically verified target-fixing transitive action and independent
Cycle-745 search. The second is not excluded and is therefore preserved as
the exact open candidate. A second objection is that the all-marked count is
only a heuristic clique search; the multiplicity equality proves the clique
characterization, and the checker reconstructs and enumerates it independently.

### N8 — cross-cycle echo

Cycle 745 teaches that anchored emptiness is global only after exact target
identity, complete split inventory, and transitive target-fixing action are
all verified. Cycle 746 teaches that the earlier half-width pair scan must be
rejected and that inconsistent targets must be separated before parity use.
This package imports those exact lessons and receipts; it does not echo their
finite claims into another system or promote weight 18 to a theorem.

## Review record (review-loop, 2026-08-14)

The submitted package was not landable as written. It reused the predecessor's
7,900-of-15,800 pair-inventory bug, attributed transitivity to a 48-element
geometric subgroup that actually has four piece orbits, carried stale
backticked dependencies, lacked a valid claim/status packet and N1–N8 record,
had no independent checker, and exited zero even if a gate failed.

The repair covers the full pair inventory, names the actual transitive
generator set, binds the current Cycle-745/746 primary and independent
receipts, adds a non-importing opposite-pivot checker, preserves hostile
mutations for each load-bearing family, writes fail-first receipts, and exits
nonzero on any failed gate. The scientific result is narrowed to the exact
bracket and construction; the weight-18 search remains explicitly incomplete.

Hard landing conditions are: (a) the claim-scoped packet-helper mapping exists
in both supported registries; (b) fresh primary and independent receipts and
canonical runner caches bind the final sources and declared inputs; and (c)
the citation-graph manifest is generated on the actual landing tree.
Independent audit remains required; this review record grants no audit verdict
or effective grade.

## Boundary and honest read

- Exact: one supplied 15,800-by-192 incidence table, one declared column order,
  and the exact `one`, `four`, and `four-flip` targets.
- Exact: all weight-8 `one` carriers, the eleven dependency-bound anchored
  weight-16 `four` carriers, 512 constructed weight-20 `four-flip` carriers,
  and no `four-flip` carrier below weight 18.
- Open: whether weight 18 is attained. The 26 refused joins are named evidence
  residue, not an emptiness certificate.
- Not claimed: a complete weight-20 census, minima for `six`, `seven`, or their
  flip partners, physical charge, arbitrary incidence systems, noncorner or
  nonsimplicial pieces, multicell compatibility, framework Admissibility,
  dynamics, boundaries, thermodynamic limits, or continuum physics.
- Audit remains unset; an independent audit is still required.
