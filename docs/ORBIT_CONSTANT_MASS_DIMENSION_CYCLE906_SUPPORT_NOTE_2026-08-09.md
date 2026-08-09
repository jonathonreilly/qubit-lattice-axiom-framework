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
the submitted Cycle-906 package was reviewed FIX_THEN_PROCEED with severe
lens verdicts (see the Review record below). What survives that repair is a
narrow support lemma of finite linear algebra and nothing else. Independent
audit still required.

## What the claim is, exactly

A statement of finite linear algebra about a declared abstract structure,
and nothing more. Both runners are SELF-CONTAINED, and every path either
declares is a file of this same landing delta, reviewed here.

The primary's declared evidence closure is exactly ONE path: its own
source. It reads no ancestor source, receipt or note, reads no axiom
surface, imports no repository module, and scans no directory; the single
read it performs is of its own bytes, for a content hash and to confirm by
an abstract-syntax read that the declared closure really is self-only. A
literally empty declaration would not have said this correctly — the cache
envelope and the evidence-readiness gate both read an empty
`AUDIT_INPUT_PATHS` as an INVALID one — so the honest input-free shape is
the single package-local integrity read that actually happens. The
independent checker declares exactly two paths, the primary's source and
the receipt that run emitted, pinned by sha256 and git blob and verified
hard-fail before any comparison.

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

Every fraction emitted by either runner is labelled **"bookkeeping
fraction, not probability."** Nothing below is a probability postulate, a
Born-rule claim, a measure selection, a symmetry credential, an interface
or bridge claim, or a statement about any repository census, event space,
monitor family, or physical configuration.

## The certified statements, exactly

1. **Parameterization.** The solutions of the two conditions are exactly
   the span of an explicitly constructed basis with two kinds of vector: a
   within-fibre difference for every fibre point after the first at each
   base point outside the required-zero subset, and one orbit vector for
   each orbit disjoint from that subset. Its dimension is therefore

   > (number of orbits disjoint from the required-zero subset)
   > + the sum, over base points outside that subset, of (fibre size − 1).

2. **Pushforward dimension.** The space of admissible pushforward masses
   has dimension exactly the number of orbits disjoint from the
   required-zero subset. At one disjoint orbit the pushforward mass is
   therefore determined **up to a single scalar** — and that is the only
   uniqueness statement this package makes.

3. **Non-negative normalized corollary.** Adding non-negativity and total
   mass one confines every solution to the union of the disjoint orbits,
   and leaves a product of simplices of dimension

   > (number of disjoint orbits − 1)
   > + the sum, over base points of those orbits, of (fibre size − 1).

4. **Two exhibited representatives.** Wherever a disjoint orbit exists, the
   **fibre-uniform** weighting (equal value on every fibre point of one
   disjoint orbit) and the **concentrated** weighting (a base point's whole
   share on its first fibre point) are both non-negative, normalized
   solutions with the SAME pushforward mass. On 5,547 of the 14,374 swept
   instances they are distinct and have different zero counts. A zero count
   is therefore a property of an exhibited representative, not of the
   solution set.

5. **A signed solution off the disjoint orbits.** Whenever a base point lies
   outside the required-zero subset, lies in an orbit that meets it, and
   carries at least two fibre points, there is a signed solution supported
   strictly outside every disjoint orbit (2,298 swept instances). Support
   containment in the disjoint orbits is thus a consequence of
   non-negativity, not of the two linear conditions alone.

6. **Two declared larger instances**, carried for scale only. Their
   parameters are chosen numbers and describe no repository census: twelve
   orbits of eleven base points, one instance with 129 fibre points
   everywhere and the first eleven orbits required zero, the other with
   mixed fibre sizes and a required-zero subset that cuts one orbit
   partially. Solution dimensions 1,409 and 1,469; pushforward dimension 1
   in both; non-negative normalized dimension 1,408 in both.

The sweep is EXHAUSTIVE over its declared family: every instance with at
most five base points, every orbit partition of them, fibre sizes from the
declared alphabet (1–3 up to four base points, 1–2 at five), and EVERY
subset of base points as the required-zero subset — 14,374 instances.

## Independent math routes and fail-closed evidence

Three routes that share no implementation path agree on the dimension of
every one of the 14,374 instances: the explicit basis construction (each
vector verified against both conditions, the family verified independent by
exact rank), exact fraction-free integer elimination on the constraint
matrix, and the closed-form combinatorial count. The dense elimination
route is deliberately NOT run on the two declared larger instances —
elimination over more than ten thousand columns is outside the runner's
budget — which the primary states in its own certificate.

The independent checker rebuilds every instance in a reverse base-point
layout with consecutive-difference orbit rows, so it solves a different
matrix with the same solution space, and it obtains the dimension three
further ways: modular rank over three large primes, a rank-nullity split
that never touches the fibre-level matrix, and a rational reduced row
echelon form whose free-variable basis is re-verified vector by vector. It
re-derives every advertised number from its own rebuild and compares — it
never reprints a receipt value — including a digest over the full
per-instance dimension table.

Both runners are fail-closed. The primary plants nine mutations (dropped
constraint rows, two wrong closed forms, a weighting on the required-zero
subset, broken orbit constancy, a rescaled representative, an event-level
uniqueness claim, a dependent basis) and every one is caught by the gate
that owns it. The checker plants nine receipt corruptions and every one is
refused. Both exit nonzero on any failed certificate; the checker exits
nonzero on any disagreement. Verified live during this repair: a planted
receipt lie (claiming the non-negative solution set of a larger instance is
a single point) produced `VERDICT DISAGREES` and exit code 1.

## Proof obligations

**Exact target, in one sentence.** For every finite cyclic group action on
finitely many base points, every assignment of non-empty finite fibres, and
every required-zero subset, the weightings satisfying vanishing and orbit
constancy are exactly the span of the constructed basis, so their dimension
is the number of orbits disjoint from the required-zero subset plus the sum
over base points outside that subset of (fibre size − 1).

**Obligation graph.** Every lemma the argument leans on, and where it
stands:

1. the constructed vectors satisfy both conditions — **proved here**, and
   re-verified vector by vector on every swept instance and on both
   declared larger instances;
2. the constructed vectors are linearly independent — **proved here** by
   exact integer rank on every swept instance;
3. they span the solution space — **proved here** as the equality of the
   basis length with the exact nullspace dimension of the constraint
   matrix, on every swept instance, and independently by the checker's
   reduced row echelon free-variable basis;
4. the pushforward map from admissible weightings onto admissible
   pushforward masses is surjective, which needs every fibre non-empty —
   **proved here** by exhibiting a preimage, and separately certified by
   the base-level rank agreeing with the disjoint-orbit count;
5. under non-negativity, a base point whose orbit meets the required-zero
   subset carries zero mass and hence zero weight at every one of its
   fibre points — **proved here**, and exercised on every swept instance
   through the support check of both representatives;
6. the identification of this structure with any repository census, group
   action, or physical condition — **OPEN, and expressly not attempted**.

**Hypotheses, preserved.** Finiteness of the base set, the group and every
fibre; non-emptiness of every fibre; a group action, so that orbits
partition the base points; rational coefficients. None is dropped between
lemma and theorem: statement 4 uses non-emptiness explicitly, and the
declared fibre alphabet starts at one so the sweep never contains an empty
fibre.

**Boundary and degenerate cases covered.** The required-zero subset may be
empty or the whole base set; orbits may have size one; fibres may have size
one; and the group may act with orbits of unequal size — every one of these
appears in the exhaustive sweep. The action enters only through its orbit
partition, which the sweep therefore ranges over directly, and which the
primary certifies against the generated group on every instance.

**Boundary NOT covered.** The non-negative normalized corollary is stated
only for instances with at least one orbit disjoint from the required-zero
subset; instances without one lie outside its declared domain, and the
runner marks them with a sentinel rather than asserting anything about
them. Infinite base sets, infinite fibres, non-cyclic groups and
coefficients outside the rationals are all outside the declared hypotheses
and nothing is claimed about them.

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
claim_type_reason: "an explicit basis with a matching exact dimension count, agreed by three implementation-disjoint routes in the primary and three further routes in the independent checker, over an exhaustively enumerated declared family, with both exhibited representatives verified against every declared property and eighteen planted mutations all caught; the structure is stipulated in-file, so the result is bounded by its declared hypotheses rather than global"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

None. Neither runner reads any external or ancestral scientific input.
There is no measured, fitted, literature or observational value anywhere in
this package, and no imported convention. Following the two-kinds rule, the
only file reads are package-local integrity reads: the primary reads its
own source for a content hash, and the checker reads the primary's source
and receipt, both of which are in this delta and pinned by sha256 and git
blob. Those are the runners' declared `AUDIT_INPUT_PATHS`, and they carry
no scientific content.

### Derived (conditional on the declared structure)

- the explicit solution basis and the dimension formula;
- the pushforward-mass dimension, and the up-to-scale statement at one
  disjoint orbit;
- the non-negative normalized corollary and its simplex-product dimension;
- the two exhibited representatives, their shared pushforward mass and
  their differing zero counts;
- the signed solution supported off the disjoint orbits;
- the two declared larger instances.

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
repair was a demotion, not a patch, and this package is that demotion.

**Dropped, and NOT ESTABLISHED.** None of the following may be cited from
this note or from the withdrawn package:

- that the lane's covariance-versus-interface tension is resolved
  constructively, or resolved at all — the premise it rested on was the
  rejected Cycle-905 interface-exclusion claim, which did not land;
- that exactly one covariant interface-compatible weighting exists, or that
  any weighting is unique up to scale at the event level;
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

**Why the uniqueness claim was withdrawn rather than narrowed in wording.**
The reviewed runner computed the world-level quotient dimension correctly
and then read it as uniqueness of the weighting. It is not: at the shape
the withdrawn package reported — one distinguished orbit of eleven worlds
carrying 129 events each — the general formula certified here gives a
1,408-dimensional family of normalized non-negative solutions, not a
unique one. Those shape numbers are quoted from the review finding as
process provenance; they are not re-established here, and no runner in this
package reads them. The corresponding declared instance in the primary
reproduces the 1,408 independently from chosen parameters.

**Per-finding disposition.** Self-containment (both closures required
rejected or unlanded ancestor blobs; of the fourteen paths the withdrawn
primary pinned, four were on `origin/main` at all and only one at its
pinned blob): cured by reducing both closures to delta-local files — the
primary declares only its own source, the checker only the primary's source
and receipt. The rejected Cycle-905 originals are in neither closure, and
the landed narrow Cycle-905 salvage is not pinned either, because the
retained algebra does not need it. Semantic bridge, overclaimed uniqueness,
overclaimed universal support, the hidden 19,003 literal, the ambient
worktree scan, and the campaign ship receipt: all removed with the claims
that carried them. Non-decisive PASS predicates and a checker that exited
zero while disagreeing: both runners were rewritten so that every
load-bearing value sits inside a decisive assertion and any disagreement
exits nonzero. Stale caches: both caches are written by
`scripts/runner_cache.py` `execute_and_write_cache` at each runner's own
declared `AUDIT_TIMEOUT_SEC` after every source and receipt edit was final,
and the receipts carry no timing, so they are byte-stable across reruns.
Repo governance: the code-like object names are gone — the objects are
named in plain mathematical language, with no bare letter-number claim
names anywhere — and the campaign/branch state is gone with the ship
receipt. No `docs/repo/ACTIVE_REVIEW_QUEUE.md` or
`docs/CANONICAL_HARNESS_INDEX.md` entry is added: after the demotion there
are no open premises or blockers to route, and a narrow support lemma is
not a canonical harness.

**No-Go Discipline.** The N-gate obligation is discharged by WITHDRAWAL,
not by a packet. Every universal negative and route-foreclosure sentence of
the withdrawn package is gone: there is no "incompatible", no "does not
lift", no "not a law", no "fails", and no sentence quantifying over any
generalization, extension or broader reading. What remains is a
parameterization theorem, an explicit basis, and exhibited existence
witnesses on a declared finite domain. No residual sentence in this note,
in either runner's docstring, in any emitted certificate string, in either
receipt, or in the closing verdict functions as a no-go.

**Hard landing conditions.** Both must be satisfied at landing; neither is
performed on this branch.

- The independent checker is claim-scoped and co-load-bearing: it is
  deliberately not imported by the primary, so import discovery cannot see
  it, while the corroboration verdict exists only on its surface. It is
  declared `packet_helper_runner` in the Status fields above. At landing
  the orchestrator must add exactly this claim-scoped entry to
  `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
  `docs/audit/scripts/build_citation_graph.py` — this branch must not edit
  audit tooling, and the dependency-policy epoch-debt queue item covers the
  registry mechanism — and then run the current-main changed-evidence gate
  on the landing topology:

  ```python
  "orbit_constant_mass_dimension_cycle906_support_note_2026-08-09": [
      "scripts/frontier_cycle906_orbit_constant_mass_dimension_independent_check_2026_08_09.py",
  ],
  ```

- This note adds a citation-graph node and removes the withdrawn one, so
  the landing set must carry a regenerated
  `docs/audit/data/citation_graph_manifest.json` acknowledgment, produced
  on the landing tree. It is deliberately absent from this branch-local
  package.

**Honest summary of what survives.** A support lemma of finite linear
algebra: one dimension formula, one explicit basis, one up-to-scale
statement about a pushforward, one corollary under non-negativity, and
three existence witnesses — all on a structure this package stipulates for
itself. It is not a Born-lane result, not an interface result, and not a
statement about any physical census. That is the correct outcome of the
demotion, and it is stated here rather than dressed up.

## Verdict

Two linear conditions on a weighting over a finite fibred set, and the
exact dimension of what satisfies them: a formula, a basis that realizes
it, and the one uniqueness statement the algebra actually supports — at the
level of the pushforward, up to scale, when a single orbit avoids the
required-zero subset. Two representatives are exhibited so that no reader
mistakes one of them for the solution set. Everything that made the
withdrawn package look like physics has been removed and is listed as not
established. Independent audit still required.
