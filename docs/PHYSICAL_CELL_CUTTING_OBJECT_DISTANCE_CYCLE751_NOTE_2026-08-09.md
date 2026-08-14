# Ambient preservation of carrier distances through three — Cycle 751

Date: 2026-08-09

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [dense ambient-graph runner](../scripts/physical_cell_cutting_object_distance_cycle751_2026_08_09.py)

Independent checker:

- [streamed-pair ambient-graph checker](../scripts/physical_cell_cutting_object_distance_cycle751_independent_check_2026_08_09.py)

Direct scientific dependencies:

- [Cycle 749 intrinsic family separator](PHYSICAL_CELL_CUTTING_FAMILY_SEPARATOR_CYCLE749_NOTE_2026-08-08.md)
- [Cycle 750 intrinsic cube graphs and pair-count distance layers](PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md)

```text
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_object_distance_cycle751_note_2026-08-09
target_blocker_text: compare each carrier component's intrinsic never-sharing distance with distance in the complete 192-vertex never-sharing graph
source_of_blocker_text: frontier_question
reachability_to_target: direct finite exhaustive computation on the supplied coordinate four-cube
artifact_role: bounded finite incidence theorem candidate
next_trace_action: independent audit of the landed primary and helper evidence
conditional_surface_status: direct Cycle 749 and Cycle 750 dependencies remain subject to independent audit
hypothetical_axiom_status: none
admitted_observation_status: none
claim_type_reason: an exhaustive theorem on one supplied finite incidence object, with no physical or multicell extension
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_object_distance_cycle751_independent_check_2026_08_09.py
```

## Exact target and terminology

On the supplied 15,800 by 192 cutting-piece incidence table, join two of the
192 pieces exactly when no cutting row contains both. Call the resulting graph
`G`. For each of the 132 Cycle 749 minimum carriers of the declared four
reading, compare distance within each connected component of its induced graph
with distance in `G`.

Every use of “distance” below means unweighted graph distance in this declared
never-sharing graph. It is not physical length, causal distance, an ambient
Euclidean metric, or a continuum observable.

## Inputs and provenance

The current primary and independent Cycle 749 certificates bind all 15,800
rows, the 192 supported pieces, the complete 132-member carrier census, and
the six intrinsic families. The current primary and independent Cycle 750
certificates bind the induced carrier graphs: 60 copies of `Q_4` and 72 copies
of `Q_3 disjoint-union Q_3`, together with their intrinsic distance layers.

Both Cycle 751 executables authenticate the source and receipt bytes of both
dependencies and reject failed or changed certificates. The primary also
rebuilds the finite object directly and forms the co-incidence matrix by a
dense integer Gram product. The helper replays Cycle 750's independent
row-streamed pair counter and constructive cube labelling without importing
Cycle 751 primary symbols.

The coordinate four-cube, declared four reading, and cyclic order used for the
controls are supplied finite data. No measured, fitted, literature,
normalization, boundary-condition, framework-primitive, or axiom value enters
the theorem.

## Complete ambient graph census

The graph `G` has 192 vertices, degree 33 at every vertex, and 3,168 edges.
All 384 supplied table symmetries preserve its adjacency. It is connected with
diameter three, and its unordered-pair distance distribution is exact:

| distance in `G` | unordered pairs |
| ---: | ---: |
| 1 | 3,168 |
| 2 | 12,576 |
| 3 | 2,592 |
| total | 18,336 |

Breadth-first search and Boolean adjacency powers agree on all 18,336 pairs.
This is an arithmetic cross-check of one graph, not two independent
reconstructions of the incidence object.

`G` is not distance-regular: the neighbor-count triples relative to a rooted
distance partition take 9 distinct values at distance one, 45 at distance two,
and 10 at distance three. This is the narrow graph-theoretic
inhomogeneity established here.

## Carrier embedding result

For each carrier, restrict attention to pairs in the same connected component
of its Cycle 750 induced graph. Every such pair at intrinsic distance one, two,
or three has the same distance in `G`:

| carrier-component comparison | pair occurrences | preserved in `G` |
| --- | ---: | ---: |
| intrinsic distance 1, 2, or 3 | 10,752 | 10,752 |
| intrinsic distance 3 only | 2,496 | 2,496 |

The first row counts a pair once for each carrier in which it occurs. Distance
one is definitional because carrier adjacency is the restriction of ambient
adjacency. Distance two is also automatic: a carrier path supplies an ambient
path, while a non-edge cannot become an ambient edge. The 2,496
distance-three pair occurrences are the nontrivial content: none acquires a
length-two path through a vertex outside its carrier.

The embedding is not globally isometric. Every one of the 480 `Q_4`
antipodal pair occurrences shortens from intrinsic distance four to ambient
distance three. In each `Q_3 disjoint-union Q_3` carrier, pairs across the two
components have no finite intrinsic graph distance, but in `G` 4,032 such pair
occurrences have distance two and 576 have distance three.

Thus the exact positive statement is preservation of within-component graph
distance through three. The submitted headline that the carrier shape “is the
object's own distance” is withdrawn because it suppresses both explicit
failure modes.

## Declared controls and count boundary

Four cyclic spacings at each of 192 starts give 768 declared sixteen-piece
control sets. In 730 sets, at least one pair connected in the induced subgraph
has a shorter distance in `G`. The carrier comparison above has no shortening
among its 10,752 tested within-component pairs through distance three. These
controls are not an exhaustive classification of sixteen-piece subsets and do
not establish rarity or causation by the charge.

Across all unordered pairs in `G`, 47 shared-cutting counts occur. Forty-four
counts determine ambient graph distance. The three values `202`, `212`, and
`250` occur at more than one ambient distance, and 1,632 unordered pairs lie
in those ambiguous count classes. Therefore Cycle 750's carrier-local
count-to-distance function does not extend to this complete 192-vertex graph.
No claim is made about a different finite incidence object.

## Proof-obligation graph

The obligation graph is acyclic:

1. current Cycle 749 receipts authenticate the full row inventory and complete
   carrier census;
2. current Cycle 750 receipts authenticate both induced carrier graph types
   and their intrinsic distance layers;
3. each Cycle 751 implementation reconstructs the complete pair-count matrix
   through a different arithmetic path;
4. each constructs `G` from exactly the zero co-incidence entries and computes
   all-pairs distance through a separate traversal implementation;
5. every carrier pair is then compared exhaustively, with antipodal and
   cross-component cases recorded separately rather than discarded;
6. exact equality, total-count, dependency, and hostile-mutation gates
   discharge the finite claim.

The strongest unproved extension is a classification of all sixteen-piece
subsets or any other reading, cell, or lattice. It is strictly stronger than
the target and is not claimed.

## No-Go Discipline Gate

The negative boundaries are narrow: this particular `G` is not
distance-regular, three exact count values are ambiguous on this graph, 730
declared controls exhibit a shortening, and the full carrier embedding is not
isometric. No universal physical or multicell no-go is asserted.

### N1 — alternative attacks

1. **Population route — ATTEMPTED.** Rebuild all cutting rows and carriers
   through the primary exact-cover route, then replay the opposite-pivot
   Cycle 749/750 helper route. Both bind all 15,800 rows and 132 carriers.
2. **Pair-arithmetic route — ATTEMPTED.** Replace the dense Gram product by
   row-streamed unordered-pair increments. The complete 192 by 192
   co-incidence matrix and zero-entry graph agree.
3. **Distance-algorithm route — ATTEMPTED.** Replace breadth-first all-pairs
   traversal by Boolean adjacency powers in the primary and an independent
   queue traversal in the helper. The 18,336 distances agree.
4. **Carrier-coordinate route — ATTEMPTED.** Compare the primary backtracking
   cube relabelling with Cycle 750's constructive breadth-first bit labels,
   then test every same-component pair occurrence. Both recover the exact
   preservation and antipodal/cross-component exceptions.
5. **Hostile/control route — ATTEMPTED.** Mutate dependency status, family and
   shape counts, ambient distance layers, preservation totals, antipodal
   layers, and ambiguous count values; also scan all 768 declared cyclic
   controls. The fail-closed contracts or exact gates reject each mutation.

These routes differ in primary object and terminal obligation: population,
pair arithmetic, path metric, local coordinate recognition, and adversarial
falsification.

### N2 — wall independence

No walls or open conditions are claimed as independent closure inputs. There
are two ordered data dependencies: Cycle 749 supplies the census and Cycle 750
supplies the intrinsic carrier graphs. Cycle 750 itself binds Cycle 749, but
Cycle 751 authenticates both directly so a stale intermediate certificate
cannot silently pass. No inflated wall count is advertised.

### N3 — hidden-wall scan

“By construction” applies only to the automatic distance-one and distance-two
comparisons and is stated explicitly. The supplied coordinate object, reading,
and cyclic controls are named finite inputs. No “standard”, “canonical”,
“registered”, background, or framework-provided physics premise is used.

### N4 — residual matching

Cycle 749 is cited only for the complete carrier census and family evidence.
Cycle 750 is cited only for the induced carrier graph types and intrinsic
distances. Neither is cited as evidence for the new ambient graph or embedding
comparison; both Cycle 751 implementations recompute those quantities.

### N5 — rhetoric and resolution

- `per_element`: all 192 pieces enter the ambient graph and distance census;
- `per_site`: one supplied coordinate four-cube only; no site family tested;
- `per_mode`: no modal decomposition exists for this finite binary object;
- `per_block`: every one of 15,800 cutting rows enters the pair counts;
- `lattice_wide`: no multicell, infinite-lattice, continuum, or physical
  metric conclusion is tested or claimed.

Both canonical caches must carry the corresponding five-line execution
certificate.

### N6 — partial closure and primitive scan

No new axiom or framework primitive is proposed or needed. The registered
premises are irrelevant to this finite graph theorem. A convention cannot
turn 768 controls into an exhaustive subset classification or repair the 480
explicit antipodal shortenings; those would require a different theorem or
object, not relabelling.

### N7 — steelman

A hostile reviewer can correctly object that “the carrier's shape is the
object's own distance” is false under the usual isometric-embedding meaning:
all 480 `Q_4` antipodes shorten, and the two components of every split carrier
interleave at finite ambient distance. That counterargument defeats the
submitted headline. This note therefore demotes the result to the exact
through-three, within-component preservation theorem and reports both failure
classes quantitatively.

### N8 — cross-cycle echo

Cycle 750 retired a similarly broad “not an ambient relabelling” phrase after
one tested corner statistic could not exclude every ambient interpretation.
The retirement mechanism was exact scoping, not a new axiom. Cycle 751 applies
the same mechanism: it replaces a total-isometry slogan with the exact tested
distance range and preserves the stronger counterexamples as boundaries.

No failure condition remains after the N7 demotion. Gate status: `PASS` for
the narrowed finite negatives above.

## Review record and hard landing conditions

Review-loop replaced the submitted half-row predecessor scan by the full
15,800-row inventory, added nonzero failure exits and fail-first receipts,
bound current Cycle 749 and Cycle 750 primary and independent certificates,
added a structurally independent helper, removed the raw cold-output artifact,
and narrowed the total-isometry and causal-charge wording to the exact finite
graph theorem.

Hard landing conditions:

- both runners and both input-bound receipts land with canonical cache
  envelopes;
- the primary and helper each fail nonzero on a load-bearing mutation;
- the helper mapping for claim id
  `physical_cell_cutting_object_distance_cycle751_note_2026-08-09` lands in
  both citation dependency maps;
- the citation-graph manifest is regenerated from the final proposed tree;
- generated ledger, queue, effective-status, and front-door outputs do not
  land;
- no audit verdict is applied by review-loop.

## Honest boundary

- The theorem is exact only for one supplied finite coordinate four-cube and
  the declared four reading.
- Cycles 749 and 750 are direct scientific dependencies and are not silently
  promoted by this note.
- Distance one and two preservation are automatic; the new measurement is the
  2,496 preserved distance-three pair occurrences.
- The 768 controls are declared controls, not an exhaustive rarity theorem.
- Full carrier isometry is explicitly false.
- No physical length, causal distance, continuum metric, another-charge
  classification, or multicell extension follows.
- Audit status remains unset until the independent audit lane acts.
