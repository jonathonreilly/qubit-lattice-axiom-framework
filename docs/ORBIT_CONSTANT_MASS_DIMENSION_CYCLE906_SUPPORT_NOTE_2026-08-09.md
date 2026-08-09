# The dimension of orbit-constant pushforward masses that vanish on a required-zero subset — Cycle 906 (demotion)

Date: 2026-08-09

Authority: none

Audit: unset

Status: proposed_retained

Claim type: bounded_theorem

Runners:

- [`frontier_cycle906_orbit_constant_mass_dimension_2026_08_09.py`](../scripts/frontier_cycle906_orbit_constant_mass_dimension_2026_08_09.py)
- [`frontier_cycle906_orbit_constant_mass_dimension_independent_check_2026_08_09.py`](../scripts/frontier_cycle906_orbit_constant_mass_dimension_independent_check_2026_08_09.py)

Receipt:

- [`orbit_constant_mass_dimension_cycle906_receipt_2026_08_09.json`](../outputs/orbit_constant_mass_dimension_cycle906_receipt_2026_08_09.json)
- [`orbit_constant_mass_dimension_independent_check_cycle906_receipt_2026_08_09.json`](../outputs/orbit_constant_mass_dimension_independent_check_cycle906_receipt_2026_08_09.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: rebuilt by the review-loop fix pass on 2026-08-09 after
the submitted Cycle-906 package was reviewed FIX_THEN_PROCEED, and rebuilt
again after the confirmation round returned FAIL (see the Review record).
What survives is a proved lemma of finite linear algebra and nothing else.
Independent audit still required.

## What the claim is, exactly

A statement of finite linear algebra about a declared abstract structure,
and nothing more. Both runners are SELF-CONTAINED, and every path either
declares is a file of this same landing delta, reviewed here.

The primary's declared evidence closure is exactly ONE path: its own
source. It reads no ancestor source, receipt or note, reads no axiom
surface, imports no repository module, and scans no directory; the single
read it performs is of its own bytes, for a content hash, for an
abstract-syntax read that the declared closure really is self-only, and for
the syntax-tree recomputation of its own route helper sets. A literally
empty declaration would not have said this correctly — the cache envelope
and the evidence-readiness gate both read an empty `AUDIT_INPUT_PATHS` as an
INVALID one — so the honest input-free shape is the single package-local
integrity read that actually happens. The independent checker declares
exactly two paths, the primary's source and the receipt that run emitted,
pinned by sha256 and git blob and verified hard-fail before any comparison.

The declared structure is: a finite set of **base points**; a finite cyclic
group acting on them, so that they partition into **orbits**; a finite set
of **fibre points**, each lying over exactly one base point, with every
fibre non-empty; and a distinguished subset of base points called the
**required-zero subset**. A **weighting** is a rational-valued function on
the fibre points. Its **pushforward mass** at a base point is the total of
its values over that base point's fibre. Two linear conditions are imposed:

- **vanishing** — the weighting is zero at every fibre point over the
  required-zero subset;
- **orbit constancy** — the pushforward mass takes the same value at every
  base point of an orbit.

Call an orbit **disjoint** when it does not meet the required-zero subset.

Every fraction emitted by either runner is labelled **"bookkeeping
fraction, not probability."** Nothing below is a probability postulate, a
Born-rule claim, a measure selection, a symmetry credential, an interface
or bridge claim, or a statement about any repository census, event space,
monitor family, or physical configuration.

## The certified statements, exactly

Each statement is proved for all finite instances in **Proof obligations**
below, and each is checked by a computation that can fail: the check that
would break if the statement were false is named beside it.

1. **Parameterization.** The solutions of the two conditions are exactly
   the span of an explicitly constructed basis with two kinds of vector: a
   within-fibre difference for every fibre point after the first at each
   base point outside the required-zero subset, and one orbit vector for
   each disjoint orbit. Its dimension is therefore

   > (number of disjoint orbits)
   > + the sum, over base points outside the required-zero subset, of
   > (fibre size − 1).

   *Discriminating check:* the dimension is recomputed on every swept
   instance by exact fraction-free rank of the constraint matrix, a route
   that shares no helper with the formula, and six declared WRONG
   coefficient sets must each be refuted by an exhibited instance.

2. **Pushforward dimension.** The space of admissible pushforward masses
   has dimension exactly the number of disjoint orbits. Where that number
   is one, every admissible pushforward mass is a rational multiple of one
   fixed admissible mass — and that is the only determined-up-to-a-scalar
   statement this package makes.

   *Discriminating check:* exact rank of the base-level matrix on every
   swept instance against the disjoint-orbit count, with four declared
   wrong coefficient sets each refuted by an exhibited instance.

3. **Support containment under non-negativity.** For a base point lying
   outside every disjoint orbit, the functional "total mass over this base
   point's fibre" is a coordinatewise non-negative vector in the row space
   of the constraint matrix. Every solution therefore has zero total there,
   and every NON-NEGATIVE solution is zero at each of that base point's
   fibre points.

   *Discriminating check:* the primary tests membership in the row space by
   exact rank at all 46,510 such base points of the family, and runs the
   same test at the 17,344 base points inside a disjoint orbit, where it
   must FAIL — that control is what makes the certificate discriminating.
   The checker instead BUILDS the combination explicitly out of its own
   constraint rows and requires the result to equal the indicator vector.

4. **Non-negative normalized corollary**, on instances with at least one
   disjoint orbit. Adding non-negativity and total mass one leaves a set of
   dimension

   > (number of disjoint orbits − 1)
   > + the sum, over base points of those orbits, of (fibre size − 1),

   whose extreme points are exactly the weightings that place one disjoint
   orbit's whole mass on a single fibre point at each of that orbit's base
   points; there are, therefore, the sum over disjoint orbits of the product
   of that orbit's fibre sizes of them.

   *Discriminating check:* the dimension is squeezed between two bounds that
   are computed WITHOUT the formula — an exact rank upper bound on the
   affine hull, and the affine rank of exhibited points each verified to be
   a non-negative normalized solution — and five declared wrong coefficient
   sets are each refuted. The extreme points are re-enumerated by brute
   force over all supports on the declared bounded subfamily (the 1,757
   instances with a disjoint orbit and at most six fibre points) and the
   enumerated set must equal the claimed set exactly.

5. **Two exhibited representatives.** Wherever a disjoint orbit exists, the
   **fibre-uniform** weighting (equal value on every fibre point of one
   disjoint orbit) and the **concentrated** weighting (a base point's whole
   share on its first fibre point) are both non-negative, normalized
   solutions with the SAME pushforward mass. On 5,547 of the 14,374 swept
   instances they are distinct, and they are distinct exactly when their
   zero counts differ. A zero count is therefore a property of an exhibited
   representative, not of the solution set.

   *Discriminating check:* both are verified against every declared property
   on every instance that has a disjoint orbit, the distinctness/zero-count
   equivalence is tested per instance, and the checker recounts every tally
   from its own rebuild.

6. **A signed solution off the disjoint orbits.** Whenever a base point lies
   outside the required-zero subset, lies in an orbit that meets it, and
   carries at least two fibre points, the difference of two of its fibre
   weights is a solution supported strictly outside every disjoint orbit.
   That hypothesis holds at **6,268** of the 14,374 swept instances — 2,298
   of them with a disjoint orbit and 3,970 without — and a witness is
   exhibited at every one of them. Support containment is thus a consequence
   of non-negativity, not of the two linear conditions alone.

   *Discriminating check:* the hypothesis and the witness are tested on
   EVERY instance and required to hold together, both tallies are recounted
   independently of the sweep loop so that a loop skipping part of the
   family disagrees with its own recount, and the hypothesis with its
   two-fibre-point clause dropped must FAIL on at least one instance.

7. **Two declared larger instances**, carried for scale only. Their
   parameters are chosen numbers and describe no repository census: twelve
   orbits of eleven base points, one instance with 129 fibre points
   everywhere and the first eleven orbits required zero, the other with
   mixed fibre sizes and a required-zero subset that cuts one orbit
   partially. Solution dimensions 1,409 and 1,469; pushforward dimension 1
   in both; non-negative normalized dimension 1,408 in both.

   *What is and is not run there:* the fibre-level rank routes — the dense
   nullspace rank, the row-space support certificate and the two-sided
   normalized-dimension bounds — are NOT run at this size, because exact
   elimination over thousands of columns is outside the runners' declared
   budget. These two rows are arithmetic evaluations of laws proved below
   and verified by those routes on the exhaustive family, cross-checked
   here by the explicit basis length, by the count of basis vectors
   supported inside the disjoint orbits, by the exact base-level rank, by
   the exhibited representative, and by the checker's independent rebuild
   from the declared parameters alone.

The sweep is EXHAUSTIVE over its declared family: every instance with at
most five base points, every orbit partition of them, fibre sizes from the
declared alphabet (1–3 up to four base points, 1–2 at five), and EVERY
subset of base points as the required-zero subset — 14,374 instances.

## How the sentences themselves are gated

The theorem the primary emits is not free text. Each dimension law is
declared as a coefficient set; the sentence is RENDERED from those
coefficients by a function in the runner; the coefficients are checked
against a dimension computed without them on every instance; and the
declared wrong coefficient sets must each be refuted by an exhibited
instance. A sentence therefore cannot drift from the numbers the run
verifies without failing the rendering comparison or the evaluation.

The checker holds its own transcription of the laws, of the phrases they
render with, and of the sentence frames, and re-renders the whole theorem
from its OWN recomputed counts. Any receipt sentence differing by one
character is a disagreement and a nonzero exit. A short list of sentence
fragments withdrawn as false — the ones this note's Review record names —
must not appear anywhere in the emitted output or in either receipt; both
runners publish only the SHA-256 digests of that list, so the withdrawn
wording itself reaches no machine surface.

What this cannot detect is a coordinated edit of BOTH runners; no in-package
check can. That is why the proof below is recorded in full: the proof, not
the runner, is what makes the sentences true, and the runners are there to
catch the errors a proof-reader misses.

## Independent math routes, and what each shares

Stated exactly, because the earlier draft overstated it. The primary has
four routes to the numbers, and their helper sets are recomputed from the
runner's own syntax tree and compared with the declared sharing, so no route
can be advertised as more independent than it is:

- the **closed form** and the **explicit basis length** share the orbit
  classification (`disjoint_orbits`). They are two readings of one
  classification, and their agreement confirms the classification, not the
  formula.
- the **exact fraction-free nullspace rank** shares no helper with the
  closed form. It is the independent confirmation of the solution
  dimension.
- the **exact base-level rank** shares only the generic rank routine with
  the nullspace route, and no structural helper. It is the independent
  confirmation of the pushforward dimension.

The independent checker rebuilds every instance in a reverse base-point
layout with consecutive-difference orbit rows, so it solves a different
matrix with the same solution space, and it obtains the dimension three
further ways: modular rank over three large primes, a rank-nullity split
that never touches the fibre-level matrix, and a rational reduced row
echelon form whose free-variable basis is re-verified vector by vector. Its
modular-rank and split routes do share the modular rank routine at base
level; that is disclosed rather than denied. It re-derives every advertised
number from its own rebuild and compares — it never reprints a receipt
value — including a digest over the full per-instance dimension table, the
support-containment tallies, the extreme-point enumeration, the witness
tallies, and every theorem sentence.

Both runners are fail-closed. The primary plants twenty mutations covering
eleven check families and the checker plants eighteen covering eight gates;
each must be caught by the gate that owns it, and any that does not bite
fails the run. Both exit nonzero on any failed certificate; the checker
exits nonzero on any disagreement.

## Proof obligations

**Exact target, in one sentence.** For every finite cyclic group action on
finitely many base points, every assignment of non-empty finite fibres, and
every required-zero subset, the weightings satisfying vanishing and orbit
constancy are exactly the span of the constructed basis, so their dimension
is the number of disjoint orbits plus the sum over base points outside the
required-zero subset of (fibre size − 1).

**The proof, for all finite instances.** Write `B` for the base points, `Z`
for the required-zero subset, `F(v)` for the fibre over `v`, and `m(x, v)`
for the pushforward mass of a weighting `x` at `v`. Let `V` be the solution
space of the two conditions.

1. *The pushforward map.* For `x` in `V` the value `m(x, v)` is constant
   along each orbit; write it `m(x, o)`. Sending `x` to the tuple of those
   values is a linear map from `V` to the rational functions on orbits.
2. *Its image.* If an orbit meets `Z`, pick a base point of it in `Z`: `x`
   vanishes on that whole fibre, so the orbit's common mass is zero. So the
   image lies in the coordinates of the disjoint orbits. Conversely, for a
   disjoint orbit and any rational `t`, placing `t` on one fibre point of
   each of that orbit's base points — possible because every fibre is
   non-empty — and zero elsewhere gives a solution with that orbit's mass
   `t` and every other orbit's mass zero. The image is therefore exactly
   the disjoint-orbit coordinates, of dimension the number of disjoint
   orbits. That is statement 2, and it also proves the pushforward map onto
   the admissible masses is surjective.
3. *Its kernel.* A solution with every orbit mass zero is exactly a
   weighting that vanishes on the fibres over `Z` and has zero fibre total
   at every other base point. Those conditions do not interact between base
   points, so the kernel is the direct sum, over base points outside `Z`, of
   the zero-sum vectors on that fibre: dimension the sum of (fibre size − 1)
   over base points outside `Z`.
4. *The dimension.* Rank plus nullity gives statement 1's formula.
5. *The basis.* Each within-fibre difference has zero pushforward
   everywhere, so it lies in the kernel; the differences at one base point
   are a basis of that fibre's zero-sum space, and different base points use
   disjoint coordinates, so together they are a basis of the kernel. Each
   orbit vector is a solution whose image is a distinct standard basis
   vector of the image. A vanishing combination of the whole family must
   therefore have zero coefficients on the orbit vectors (apply the map) and
   then zero coefficients on the differences. The family is independent, it
   has as many members as the dimension computed in step 4, and it lies in
   `V`; so it is a basis and it spans. That is statement 1.
6. *Support containment.* Let an orbit meet `Z` at a base point `v`, and let
   `w` be any base point of that orbit. The functional "fibre total at `w`"
   equals "fibre total at `v`" plus a combination of the orbit-constancy
   rows, and "fibre total at `v`" is the sum of the vanishing rows at `v`.
   So the indicator vector of `F(w)` lies in the row space of the constraint
   matrix and is coordinatewise non-negative. Every solution therefore has
   zero fibre total at `w`; a non-negative one has each of those weights
   zero. That is statement 3, and it is the certificate both runners build.
7. *The normalized set's dimension.* Assume at least one disjoint orbit.
   By step 6 every non-negative normalized solution vanishes off the
   disjoint orbits, so the set lies in the subspace `V'` of solutions
   supported there; steps 3–5 applied to `V'` give its dimension as the
   number of disjoint orbits plus the sum of (fibre size − 1) over their
   base points. Total mass is a functional that is not identically zero on
   `V'`, so the affine slice of total mass one has one dimension less. The
   weighting that gives each disjoint orbit an equal share and spreads each
   base point's share uniformly over its fibre is strictly positive at every
   coordinate of that support, hence lies in the relative interior of the
   slice; so the affine hull of the non-negative normalized set is the whole
   slice, and its dimension is as stated in statement 4.
8. *Its extreme points.* If two disjoint orbits carry positive mass, the
   solution is a proper convex combination of its two normalized
   restrictions, each again a non-negative normalized solution, so it is not
   extreme. An extreme point therefore carries one disjoint orbit's whole
   mass. Within that orbit the constraints on the fibres are independent of
   each other, so the set at that mass level is a product of scaled
   simplices, whose extreme points are exactly the single-fibre-point
   choices; each such point has enough active constraints to determine it
   uniquely, so each is extreme. This gives statement 4's extreme-point
   description and the count.
9. *The signed solution.* If a base point `u` is outside `Z`, sits in an
   orbit that meets `Z` and carries two fibre points, then the difference of
   two of its fibre weights vanishes on `Z`'s fibres, has zero pushforward
   everywhere, and is supported at `u`, which lies in no disjoint orbit.
   That is statement 6.

**Obligation graph.** Every lemma the argument leans on, and where it
stands:

1. the constructed vectors satisfy both conditions — **proved here** (step
   5), and re-verified vector by vector on every swept instance and on both
   declared larger instances;
2. the constructed vectors are linearly independent — **proved here** (step
   5), and re-verified by exact integer rank on every swept instance;
3. they span the solution space — **proved here** (steps 1–5), and
   re-verified as the equality of the basis length with the exact nullspace
   dimension on every swept instance, and independently by the checker's
   reduced row echelon free-variable basis;
4. the pushforward map onto admissible pushforward masses is surjective,
   which needs every fibre non-empty — **proved here** (step 2), and
   separately certified by the base-level rank agreeing with the
   disjoint-orbit count;
5. under non-negativity, a base point outside every disjoint orbit carries
   zero mass and hence zero weight at each of its fibre points — **proved
   here** (step 6), and certified per base point by the row-space
   certificate, with the control at base points inside a disjoint orbit;
6. the dimension and the extreme points of the non-negative normalized set
   — **proved here** (steps 7–8), verified by the two-sided bounds on every
   qualifying instance and by brute-force enumeration on the declared
   bounded subfamily;
7. the identification of this structure with any repository census, group
   action, or physical condition — **OPEN, and expressly not attempted**.

**Hypotheses, preserved.** Finiteness of the base set, the group and every
fibre; non-emptiness of every fibre; a group action, so that orbits
partition the base points; rational coefficients. None is dropped between
lemma and theorem: step 2 uses non-emptiness explicitly, statements 4 and 5
additionally require at least one disjoint orbit, and the declared fibre
alphabet starts at one so the sweep never contains an empty fibre.

**Boundary and degenerate cases covered.** The required-zero subset may be
empty or the whole base set; orbits may have size one; fibres may have size
one; and the group may act with orbits of unequal size — every one of these
appears in the exhaustive sweep. The action enters only through its orbit
partition, which the sweep therefore ranges over directly, and which the
primary certifies against the generated group on every instance.

**Boundary NOT covered.** Statements 4 and 5 are stated only for instances
with at least one disjoint orbit; instances without one lie outside their
declared domain, and the runner marks them with a sentinel rather than
asserting anything about them. Infinite base sets, infinite fibres,
non-cyclic groups and coefficients outside the rationals are all outside the
declared hypotheses and nothing is claimed about them. The extreme-point
enumeration, as a computation, runs only on the declared bounded subfamily;
the extreme-point statement itself is proved above for all finite instances.

**Strongest missing lemma.** Any lemma identifying this abstract structure
with a landed repository census, event space, or group action. Without it
nothing here reaches physics, and this package deliberately supplies no
candidate for it.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "retain, as self-contained finite linear algebra, the orbit/pushforward dimension result that the reviewed Cycle-906 package computed correctly, and nothing that package claimed beyond it"
source_of_blocker_text: review_loop
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "no downstream consumer is claimed and none is known; any future use of this lemma must supply its own base points, group action, fibres and required-zero subset from landed sources, because this package supplies none"
```

## Status fields

```yaml
actual_current_surface_status: exact-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "conditional on the declared abstract structure only -- a finite cyclic group action on finitely many base points, non-empty finite fibres, and a declared required-zero subset; there are no inherited premises and no open bridges load-bearing on any statement above"
hypothetical_axiom_status: null
admitted_observation_status: null
packet_helper_runner: scripts/frontier_cycle906_orbit_constant_mass_dimension_independent_check_2026_08_09.py
claim_type_reason: "a general proof recorded in this note for all finite instances, with an explicit basis, verified on an exhaustively enumerated declared family by routes that do not share the formula's implementation path, with every declared wrong coefficient set refuted by an exhibited instance and thirty-eight planted mutations all caught; the structure is stipulated in-file, so the result is bounded by its declared hypotheses rather than global"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

None. Neither runner reads any external or ancestral scientific input.
There is no measured, fitted, literature or observational value anywhere in
this package, and no imported convention. Following the two-kinds rule, the
only file reads are package-local integrity reads: the primary reads its
own source for a content hash and for two syntax-tree checks of itself, and
the checker reads the primary's source and receipt, both of which are in
this delta and pinned by sha256 and git blob. Those are the runners'
declared `AUDIT_INPUT_PATHS`, and they carry no scientific content.

### Derived (conditional on the declared structure)

- the explicit solution basis and the dimension formula;
- the pushforward-mass dimension, and the up-to-a-scalar statement at one
  disjoint orbit;
- support containment under non-negativity, as a row-space certificate;
- the non-negative normalized set's dimension and its extreme points;
- the two exhibited representatives, their shared pushforward mass and
  their differing zero counts;
- the signed solution supported off the disjoint orbits;
- the two declared larger instances, as arithmetic evaluations of the above.

### Open (expressly not decided here)

- whether this abstract structure describes any repository census, event
  space, group action, or physical condition — no identification is made,
  and none is available from this package;
- everything the withdrawn package claimed beyond the algebra above; the
  Review record inventories it, and none of it is established;
- whether any covariance, interface, or occurrence condition applies to any
  weighting anywhere in the framework.

## Review record

The submitted Cycle-906 package ("The tension resolves by one orbit: a new
weighting exists, unique up to scale") was reviewed on 2026-08-09 by the
sole combined adversarial science review, iteration 1, disposition
FIX_THEN_PROCEED with Code/Runner FAIL, Proof Obligations FAIL,
Imports/Support FAIL, No-Go Discipline FAIL, Audit Compatibility BLOCKED,
Nature Retention BOUNDED and Physics Claim Boundary SUPPORT. The required
repair was a demotion, not a patch. The first demotion was then confirmed
FAIL on the grounds that its load-bearing theorem text stayed green under
mutation and that the reduced surface still carried false or unproved
claims. This package is the second repair, and the paragraphs below record
what each of those findings cost.

**Dropped, and NOT ESTABLISHED.** None of the following may be cited from
this note or from the withdrawn package:

- that the lane's covariance-versus-interface tension is resolved
  constructively, or resolved at all — the premise it rested on was the
  rejected Cycle-905 interface-exclusion claim, which did not land;
- that exactly one covariant interface-compatible weighting exists, or that
  any weighting is determined up to a scalar at the event level;
- that any covariant zero-mass weighting has a zero set of 90,841 of 92,260
  events and support on exactly eleven worlds;
- the incompatibility theorem inside the 25-dimensional extension, the
  five-generator span, the fibre dimension, and the "price is exactly one
  new generator" statement — all rested on absent Cycle-902 and Cycle-905
  artifacts;
- the "covariance is a credential, not a law" verdict and its
  drop-covariance pricing, which were computed by a recursive scan of every
  top-level document and script in the branch worktree;
- the downstream exhaustive-ratio failure and its hard-coded scale
  literal 19,003, which was labelled "from 905", never read from any source
  field, and has no authority on `origin/main`;
- the two filed cross-lane premises, the blocker-ledger rows, and the
  campaign ship receipt.

**Withdrawn in this second repair, as false or unproved.**

- *The non-negative normalized solution set "is a product of simplices."*
  FALSE, and removed from every surface. The dimension it was attached to is
  correct and is retained; the shape claim is not. The smallest instance in
  the declared family that separates them has two orbits of one base point,
  fibre sizes one and two, and an empty required-zero subset: the solution
  set has three extreme points, and a product of an orbit-mass simplex with
  the fibre simplices would have four. The runners now enumerate the extreme
  points by brute force and publish that separating instance as an exhibited
  witness on the declared finite domain.
- *"Three routes that share no implementation path."* Not true as written:
  the closed form and the basis length share the orbit classification, and
  the two rank routes share the generic rank routine. The claim is replaced
  by an exact route inventory whose helper sets are recomputed from the
  runner's own syntax tree, so the sharing statement itself is now gated.
- *The signed-witness tally of 2,298 instances.* Undercounted: both runners
  skipped the witness test whenever no disjoint orbit existed, although the
  witness's stated hypothesis never mentions one. The hypothesis holds at
  6,268 instances — 2,298 with a disjoint orbit and 3,970 without — and the
  smallest omitted case is one orbit of two base points with fibre sizes one
  and two and the first base point required zero. Both tallies are now
  recounted independently of the sweep loop.
- *A universal theorem carried by a bounded sweep.* The earlier note
  substituted computation for the universal quantifier. The general proof is
  now recorded above, and the sweep is described as verification of it.
- *"Of the fourteen paths the withdrawn primary pinned, four were on
  `origin/main`."* Wrong count and undated. Recomputed at
  `origin/main = 323d7fc32d77598f74ea6cd4d30c38dda0fe5070` on 2026-08-09:
  **five** of the fourteen exist, and exactly **one** of those five is at
  its pinned git blob; the Cycle-863 runner is absent entirely.
- *The primary docstring's claim that `AUDIT_INPUT_PATHS` is the empty
  tuple.* It never was, after the cure; the docstring now states the
  one-path closure that the code declares and the receipt, cache, note and
  checker all report.
- *"This note adds a citation-graph node and removes the withdrawn one."*
  The withdrawn note is not on `origin/main`, so nothing is removed; the
  landing adds one node and no deletion.

**Per-finding disposition of the first review.** Self-containment (both
closures required rejected or unlanded ancestor blobs): cured by reducing
both closures to delta-local files — the primary declares only its own
source, the checker only the primary's source and receipt. The rejected
Cycle-905 originals are in neither closure, and the landed narrow Cycle-905
salvage is not pinned either, because the retained algebra does not need it.
Semantic bridge, overclaimed uniqueness, overclaimed universal support, the
hidden 19,003 literal, the ambient worktree scan, and the campaign ship
receipt: all removed with the claims that carried them. Non-decisive PASS
predicates and a checker that exited zero while disagreeing: both runners
were rewritten so that every load-bearing value sits inside a decisive
assertion and any disagreement exits nonzero. Stale caches: both caches are
written by `scripts/runner_cache.py` `execute_and_write_cache` at each
runner's own declared `AUDIT_TIMEOUT_SEC` after every source and receipt
edit was final, and the receipts carry no timing, so they are byte-stable
across reruns. Repo governance: the code-like object names are gone — the
objects are named in plain mathematical language, with no bare letter-number
claim names anywhere — and the campaign/branch state is gone with the ship
receipt. No `docs/repo/ACTIVE_REVIEW_QUEUE.md` or
`docs/CANONICAL_HARNESS_INDEX.md` entry is added: after the demotion there
are no open premises or blockers to route, and a narrow support lemma is not
a canonical harness.

**Mutation record.** One load-bearing mutation per check family, each
applied on a scratch copy at `origin/main` plus this delta and reverted
immediately. Twenty are planted inside the primary and eighteen inside the
checker, and every run refuses to pass unless all of them bite. The
mutations run by hand against the whole package in this repair, and their
results:

| mutation | result |
|---|---|
| the receipt's pushforward sentence replaced by "the event-level weighting is unique up to scale", the receipt regenerated and the checker's sha256/git-blob pins refreshed to the mutated bytes — the confirmation round's own mutation | primary exits 1 (the sentence no longer carries the rendered formula, and the withdrawn-sentence scan finds it); with the primary forced green, the checker exits 1 with `VERDICT DISAGREES` on the re-rendered sentence |
| the withdrawn "product of simplices" sentence appended to the receipt's corollary, pins refreshed | checker exits 1, withdrawn sentence found |
| the solution-dimension coefficients shifted from (1, 1, 0) to (1, 1, 1) | primary exits 1; the law disagrees with the exact nullspace rank on all 14,374 instances |
| the support-containment control inverted, so a certificate is claimed at base points inside a disjoint orbit | primary exits 1 on 17,344 control defects |
| the witness sweep restored to skipping instances with no disjoint orbit | primary exits 1: the sweep tally 2,298 disagrees with the independent recount 6,268 |

**No-Go Discipline.** The N-gate obligation is discharged by WITHDRAWAL,
not by a packet. Every universal negative and route-foreclosure sentence of
the withdrawn package was removed together with the claim that carried it,
and every sentence that remains is scoped to the declared finite structure.
What remains is a parameterization theorem, an explicit basis, and exhibited
existence witnesses on a declared finite domain, among them the instance
that separates the solution set from a product of simplices, published as an
exhibited pair of counts on that domain. Every sentence that remains — in
this note, in both runner docstrings, in every emitted certificate string,
in both receipts and in the closing verdict — is a positive statement about
the declared finite structure or an exhibited witness on it.

**Hard landing conditions.** All three must be satisfied at landing; none is
performed on this branch.

- The independent checker is claim-scoped and co-load-bearing: it is
  deliberately not imported by the primary, so import discovery cannot see
  it, while the corroboration verdict exists only on its surface. It is
  declared `packet_helper_runner` in the Status fields above. At landing the
  orchestrator must add exactly this claim-scoped entry to
  `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
  `docs/audit/scripts/build_citation_graph.py`:

  ```python
  "orbit_constant_mass_dimension_cycle906_support_note_2026-08-09": [
      "scripts/frontier_cycle906_orbit_constant_mass_dimension_independent_check_2026_08_09.py",
  ],
  ```

  The claim id was verified against
  `build_citation_graph.claim_id_from_path` for this note's path.
- That registry edit is NOT yet an ordinary landing step, and this is its
  governed stop. At `origin/main = 323d7fc32d77598f74ea6cd4d30c38dda0fe5070`
  (checked 2026-08-09) `docs/audit/scripts/build_citation_graph.py` is still
  inside `DEPENDENCY_POLICY_SOURCES` in
  `docs/audit/scripts/audit_science_fingerprint.py`, so the dependency-policy
  impact gate applies and the epoch is already in mismatch. The mapping must
  therefore WAIT for the owner resolution recorded as queue item
  `2026-08-08-dependency-policy-epoch-debt-helper-registry`, or for the
  owner-approved amendment that scopes the claim-scoped helper registry out
  of the governed bytes, to land first. Landing the mapping before either
  requires the full impact gate — the pipeline's invalidation set inspected
  and a fresh scientific audit for every mismatching fingerprint. This
  branch must not edit audit tooling on its own authority, and does not.
- This note adds one citation-graph node and removes none — the withdrawn
  note is not on `origin/main`, and a cold cherry-pick of this delta onto
  `origin/main` produces seven additions and no deletion. The landing set
  must therefore still carry a regenerated
  `docs/audit/data/citation_graph_manifest.json` acknowledgment, produced on
  the landing tree, because a node addition alone requires it. It is
  deliberately absent from this branch-local package.

**Honest summary of what survives.** A proved lemma of finite linear
algebra: one dimension formula with its explicit basis, one statement about
the pushforward, one support-containment certificate, the dimension and the
extreme points of the non-negative normalized set, and two exhibited
existence witnesses — all on a structure this package stipulates for itself.
It is not a Born-lane result, not an interface result, and not a statement
about any physical census. That is the correct outcome of the demotion, and
it is stated here rather than dressed up.

## Verdict

Two linear conditions on a weighting over a finite fibred set, and the exact
dimension of what satisfies them: a formula, a basis that realizes it, a
proof that covers every finite instance, and the one determined-up-to-a-
scalar statement the algebra actually supports — at the level of the
pushforward, when a single orbit avoids the required-zero subset. Under
non-negativity the support is confined by an explicit certificate and the
solution set's dimension and extreme points are pinned down; two
representatives are exhibited so that no reader mistakes one of them for the
solution set. Everything that made the withdrawn package look like physics
has been removed and is listed as not established, and everything this note
could not prove has been removed with it. Independent audit still required.
