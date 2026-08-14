# Forced-mean identity and finite multiplicity rankings — Cycle 753

Date: 2026-08-09

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_shared_count_variance_law_cycle753_2026_08_09.py)

Independent checker:

- [row-blocked multiplicity-profile checker](../scripts/physical_cell_cutting_shared_count_variance_law_cycle753_independent_check_2026_08_09.py)

Direct scientific dependency:

- [Cycle 752 complete induced-`Q_4` census and pair-total separation](PHYSICAL_CELL_CUTTING_SHAPE_CENSUS_LEAST_SHARING_CYCLE752_NOTE_2026-08-09.md)

Scope: an exact theorem on one supplied finite cutting system. The primary
rebuilds the cell complex, cuttings, readings, carrier census, and block
bookkeeping from scratch. The helper live-replays Cycle 752's structurally
independent least-vertex enumeration and row-streamed pair counter, then
recomputes the new multiplicity profiles in cutting-row blocks. This package
changes no Lattice, Qubit, Admissibility, or Record axiom, no approved
primitive, no policy, and no audit status.

```text
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_shared_count_variance_law_cycle753_note_2026-08-09
target_blocker_text: explain the Cycle 752 pair-total ranking and compare it with exact multiplicity-profile statistics
source_of_blocker_text: Cycle 752 finite-object boundary
reachability_to_target: direct algebra plus exhaustive computation on the supplied coordinate four-cube
artifact_role: bounded finite incidence theorem candidate
next_trace_action: independent audit of the landed primary and helper evidence
conditional_surface_status: direct Cycle 752 dependency remains subject to independent audit
hypothetical_axiom_status: none
admitted_observation_status: none
claim_type_reason: exact algebra and exhaustive finite rankings on one supplied incidence object, without causal, charge-specific, probability, or multicell extension
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_shared_count_variance_law_cycle753_independent_check_2026_08_09.py
```

## What this answers

The unit four-cube cuts into least-volume pieces at the adjacency cost floor
in 15800 ways, and those cuttings use 192 pieces between them, 24 to a cutting
and 1975 cuttings through each piece. The charge called four is marked on 5664
of the cuttings and needs sixteen pieces to carry it.

[Cycle 752](PHYSICAL_CELL_CUTTING_SHAPE_CENSUS_LEAST_SHARING_CYCLE752_NOTE_2026-08-09.md)
joined two pieces whenever no cutting used both, counted every sixteen pieces
joined exactly like the corners of a four-cube, found 59736 of them with 4978
through every single piece, and ranked them by one number: take each pair of
pieces, count how many cuttings use both, and add those counts over all pairs.
The 60 shapes that carry the declared four reading came out lightest. That
cycle reported the ranking as a measurement and a floor underneath it as a
derivation, without reducing the ranking to the complete row-multiplicity
profile used here.

This cycle supplies that reduction. The ranked total is a spread about a mean
the system fixes in advance. Two exact finite classifiers must be kept
distinct: a largest-first threshold in the twice-met count and equality to the
four-reading support size in the odd-met count. The latter does identify the
same 60 shapes, but its descending order runs opposite to the low-total
extremum.

## Inputs and provenance

Cycle 752 supplies current primary and independent certificates for the
complete `59,736`-member induced-`Q_4` census, the exact `60/59,676` reading
split, the shared-cutting totals, and the parity floor. Both Cycle 753
executables authenticate the source and receipt bytes of both Cycle 752
executables and reject failed, stale, or changed certificates.

The primary rebuilds the `15,800` cutting rows, `192` supported pieces, all
eight reading vectors, the complete minimum-carrier census, the induced-`Q_4`
population, and every row-multiplicity profile. The helper imports no Cycle
753 primary symbols. It live-replays Cycle 752's independent least-vertex
`Q_4` enumerator and row-streamed pair counter, then constructs every
multiplicity histogram in cutting-row blocks rather than the primary's
shape-blocked route.

The coordinate four-cube and eight declared reading vectors are supplied
finite data of this lane. No measured, fitted, literature, observational,
normalization, boundary-condition, framework-primitive, or axiom value enters
the theorem.

## The mean is fixed before any shape is chosen

For a set of sixteen pieces write `m` for the number of its pieces lying on a
given cutting. Each piece lies on 1975 cuttings, so the sixteen pieces meet
the 15800 cuttings 31600 times in total, and

```
31600 = 2 x 15800
```

Whichever sixteen pieces are taken, and whether or not they carry anything,
the average number of them met per cutting is exactly two. Nothing about the
choice can move it.

## The ranked total is the squared departure from that mean

Every cutting met `m` times contributes `m(m-1)/2` such pairs, so the ranked
total is the sum of `m(m-1)/2` over the 15800 cuttings. Expanding about two,

```
sum (m-2)^2  =  sum m^2  -  4 x 31600  +  4 x 15800
```

and the ranked total is `(sum m^2 - 31600) / 2`, so for every sixteen-piece
set whatsoever,

```
ranked total  =  15800  +  (1/2) x sum (m-2)^2
```

This is an identity, not a fit. It carries no condition on how large `m` may
get. The right-hand side is a whole number because the departures sum to zero
and a square has the parity of its root, so their squares sum to an even
number.

So the quantity the preceding cycle ranked by is a spread. Ranking the shapes
by shared cuttings is ranking them by how far their meetings stray from the
two-per-cutting average the system already imposed, and being light means
being flat.

## The floor, and exactly what reaching it would take

Carrying a reading marked on `S` cuttings means meeting each of those an odd
number of times, so the departure from two is at least one on each of them and
at least zero elsewhere. Hence

```
ranked total  >=  15800 + S/2
```

for any carrier of that reading, which for the charge called four is 18632.
The identity says more than the bound: equality holds precisely when the
carrier meets each of the 5664 marked cuttings once or three times and each of
the rest exactly twice. The mean then forces the split, 2832 met once and 2832
met three times. The floor is not merely a number to sit above; it
names a single profile, and any carrier failing to reach it fails by a
countable number of off-mean cuttings.

In particular the floor demands that the carrier miss no cutting at all. A
cutting the carrier does not meet sits two below the mean, so it costs four
where a marked cutting costs one, and a missed cutting cannot be a marked one
because zero is even. The floor therefore rises by two for every cutting
missed. So the floor is not merely unreached by the carriers found here; it is
out of reach for any carrier that misses a cutting, and the shortfall grows
with the number missed.

The preceding cycle derived 18632 and left it there. What is added here is
that reaching it is a determinate combinatorial demand, so the gap between
18632 and what carriers actually do is a fact about the object rather than
slack in the argument.

## What the carriers actually do

The lightest carrier meets 9632 cuttings twice, 2832 once, 2832 three times,
252 not at all and 252 four times, and no cutting more than four times. Its
squared departure is 7680, so its total is

```
15800 + 7680/2 = 19640
```

which is 1008 above the floor, and the 1008 is accounted for exactly by the
cuttings sitting two away from the mean, 252 in each direction.
Across all 132 smallest carriers the squared departure takes 4 values, least
7680 and most 16832.

## A largest-first threshold from the twice-met count

Rank all 59736 shapes by how many cuttings they meet exactly twice, largest
first. The 60 carriers occupy the top 60 places. The least of them meets
9616 cuttings twice; the next shape down the list meets 8688. So within
this population the carriers are exactly the shapes meeting at least 9616
cuttings exactly twice, with no shape tying across the boundary.

That is a sharper one-sided threshold than the preceding cycle's pair-total
ordering. It says that, on this population, the carriers maximize the number
of cuttings sitting exactly on the mean. It does not say this is the only
possible classifier.

## Descending odd-count rank does not reproduce the low-total extremum

The tested hypothesis was that the low pair-total order might simply be the
largest-first order of the reading-support-sized odd count. It is not. Every
four-reading carrier has 5664 odd meetings. Ranking the shapes by odd meetings,
largest first, puts those carriers 57973rd to 58032nd of 59736: 57972 shapes
have more odd meetings and 1704 have fewer.

There is an important countervailing fact. Exactly 60 shapes have 5664 odd
meetings, and they are exactly the 60 four-reading carriers. Thus equality to
the known support size is itself an exact classifier on this finite
population. The computation rules out only the proposed descending-rank
explanation; it does not rule out reading-support information, a nonlinear
odd-count rule, or a joint explanation. The twice-met count supplies the
largest-first threshold. Why either classifier aligns with the declared
reading is a further question this page does not answer.

## Where the earlier linear form does and does not hold

If no cutting is met more than four times, eliminating the thrice-met count
between the two sum rules gives a linear form in the odd count and the
twice-met count alone, with the four-times count cancelling. That form holds
on exactly 17544 of the 59736 shapes. It fails on the rest because the
condition fails on the rest: 42192 of the shapes have some cutting met more
than four times. The shapes satisfying the form and the shapes no cutting
meets more than four times are the same 17544 shapes.

How far a cutting can go is not a measurement. Two pieces joined in the
never-sharing graph lie on no common cutting, so the pieces of one shape that
a single cutting meets are pairwise unjoined, and a four-cube has at most 8
corners that are pairwise unjoined. No cutting can meet one of these shapes
more than 8 times, and 8 is reached.

This is recorded because the linear form is the natural first thing to write
down, and it is the identity above, not that one, that holds without a
condition.

## Boundary

- The identity relating the ranked total to the squared departure is derived
  and holds for every sixteen-piece set in the system, carrier or not. The
  floor and its equality condition are derived. Everything else on this page is
  measured over the 59736 four-cube-shaped sets and is not claimed beyond them.
- What the runner measures about the identity is its premise and its arithmetic,
  not the identity itself: that the multiplicities of each of the 59736 shapes
  sum to 15800 and weigh 31600, and that the total taken from the multiplicity
  profile agrees with the total taken from the shared-cutting counts. Given the
  premise the identity is algebra, and that is what makes it unconditional.
- **The floor 18632 is still not shown to be attained.** No shape found here
  reaches it. Nothing here shows 19640 is forced, and nothing here rules out a
  carrier of some other shape reaching 18632.
- **The twice-met criterion is a threshold on this population, not a proof.**
  Nothing here derives 9616, and nothing here shows a shape outside these 59736
  could not meet at least that many cuttings twice without carrying anything.
- Within these 59736 sets, carrying a reading and carrying the charge called
  four coincide, so what these rankings demonstrably separate is sets that
  carry something from sets that carry nothing. Neither ranking is shown to
  tell the charge called four from a different reading.
- The negative result concerns only a descending odd-count ordering: that
  ordering does not reproduce the low-total extremum. Equality to the known
  support size `5664` exactly selects the same 60 shapes, so no broader
  dismissal of reading-support information follows.

## Independent reconstruction and proof-obligation graph

The obligation graph is acyclic:

1. current Cycle 752 primary and helper receipts bind the complete induced-
   `Q_4` population, reading split, pair totals, and parity floor;
2. the Cycle 753 primary rebuilds the supplied incidence system and constructs
   profiles in shape blocks, while the helper live-replays Cycle 752's
   least-vertex enumeration and row-streamed pair counter;
3. the helper constructs the new histograms in cutting-row blocks and imports
   no Cycle 753 primary symbols;
4. both routes check the fixed total weight `31,600`, the squared-spread
   identity, the parity floor and equality profile, all 132 carrier spreads,
   both finite ranking statements, and the cap-four linear form;
5. exact equality, dependency, and hostile-mutation gates discharge the finite
   target.

The strongest unproved extensions are a derivation of either classifier from
the declared reading, discrimination among multiple nonzero readings, a
probability measure, a causal selector, or an extension to another cell or
lattice. The proof-obligation result is `CLOSED` for the stated finite theorem
and `OPEN` for those extensions.

## No-Go Discipline Gate

The negative statement retained here is only that descending odd-count rank
does not reproduce the low-pair-total extremum on the supplied `59,736`-shape
population. The submitted broader claim that odd support does not select the
carriers is withdrawn: equality to `5664` selects them exactly.

### N1 — alternative attacks

1. **Algebraic route — ATTEMPTED.** Expand `sum m(m-1)/2` about the forced
   mean `2`; this proves the pair-total identity for every sixteen-piece set
   without assuming a multiplicity cap.
2. **Population route — ATTEMPTED.** Enumerate every induced `Q_4` and every
   row multiplicity; all `59,736` profiles have row count `15,800` and weight
   `31,600`.
3. **Independent route — ATTEMPTED.** Replace rooted shape construction and a
   dense Gram product with Cycle 752's least-vertex enumeration and streamed
   pair count, then replace shape blocks with row-blocked profiles; every
   total and boundary agrees.
4. **Reading-signature route — ATTEMPTED.** Compare the odd-count equality set
   directly with the declared-four set. This route defeats the broad submitted
   negative: both are the same 60 shapes.
5. **Rank-direction route — ATTEMPTED.** Count strict positions around `5664`;
   `57,972` shapes lie above, 60 equal it, and `1,704` lie below, so only the
   descending-ranking explanation fails.
6. **Hostile provenance route — ATTEMPTED.** Mutate the Cycle 752 census and
   the Cycle 753 odd-equality boundary; fail-closed contracts reject both.

These routes differ in terminal obligation: algebra, population completeness,
object reconstruction, reading equality, ordering direction, and adversarial
provenance.

### N2 — wall independence

No independent walls or admissions are claimed. Cycle 752 is one ordered
finite-data dependency and is authenticated through both its primary and
helper certificates. There is no wall count to inflate.

### N3 — hidden-wall scan

The supplied coordinate object and eight declared target vectors are named
finite inputs. The floor's equality condition is expanded into its exact
multiplicity profile. No “standard,” “canonical,” “framework provides,”
background, or primitive language supplies an unstated scientific premise.

### N4 — residual matching

| cited source | exact residual used here | match |
| --- | --- | --- |
| Cycle 752 | complete induced-`Q_4` census, reading split, pair totals, and parity floor | yes |

Cycle 752 is not cited as evidence for the new forced-mean reduction or either
multiplicity ranking; both Cycle 753 implementations compute those results.

### N5 — rhetoric and resolution

- `per_element`: all `192` pieces enter the complete induced-`Q_4` profile
  census;
- `per_site`: one supplied coordinate four-cube only; no site family tested;
- `per_mode`: no modal decomposition exists for this finite binary object;
- `per_block`: every one of `15,800` cutting rows enters the profile counts;
- `lattice_wide`: no multicell, infinite-lattice, continuum, causal, or
  physical charge mechanism is tested or claimed.

Both canonical caches must carry the corresponding five-line execution
certificate.

### N6 — partial closure and primitive scan

No new axiom or framework primitive is proposed or needed. Relabelling cannot
derive `9616`, make the twice-met threshold unique, explain why equality to
`5664` selects the carriers, or extend the finite census. Those tasks require
a separate theorem or additional population, not a convention.

### N7 — steelman

A hostile reviewer can correctly observe that the odd count is not a failed
classifier: equality to `5664` identifies exactly the 60 four-reading
carriers. That observation defeats the broader submitted rhetoric. It does
not defeat the narrow ordering result, because `57,972` shapes have a larger
odd count and `1,704` a smaller one. The same reviewer can correctly treat the
twice-met threshold as one exact finite classifier rather than a derived or
unique physical selector; this note now does so.

### N8 — cross-cycle echo

Cycle 752 narrowed a broad shape/charge slogan to a complete finite census and
an exact within-population separation. Cycle 753 follows the same discipline:
the false exclusivity claim about twice-met counts is replaced by two distinct
finite classifiers, while the negative statement is restricted to one rank
direction that the exhaustive census actually tests.

No failure condition remains after that demotion. Gate status: `PASS` for the
narrow finite negative above.

## Review record and hard landing conditions

Review-loop added nonzero failure exits and fail-first receipts, bound the
current Cycle 752 primary and independent certificates, added a structurally
independent helper, removed the raw cold-output artifact, and replaced the
false claim that odd support does not select the carriers with the exact
equality-classifier and descending-rank statements.

Hard landing conditions:

- both executables and both input-bound receipts land with canonical cache
  envelopes;
- the primary and helper each fail nonzero on a load-bearing mutation;
- the helper mapping for claim id
  `physical_cell_cutting_shared_count_variance_law_cycle753_note_2026-08-09`
  lands in both citation dependency maps;
- the citation-graph manifest is regenerated from the final proposed tree;
- generated ledger, queue, effective-status, and front-door outputs do not
  land;
- no audit verdict is applied by review-loop.

## Runner

The primary rebuilds the cell complex, cuttings, readings, complete induced-
`Q_4` census, and profiles from scratch. The helper live-replays the independent
Cycle 752 census and reconstructs profiles in cutting-row blocks. Class-A:
integer and two-element-field arithmetic on a finite explicit object, no
solver.

```
primary: TOTAL: PASS=44 FAIL=0
helper:  TOTAL: PASS=13 FAIL=0
```
