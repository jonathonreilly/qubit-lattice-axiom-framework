# Complete induced-`Q_4` census and shared-cutting-total separation — Cycle 752

Date: 2026-08-09

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [direct finite-object runner](../scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_2026_08_09.py)

Independent checker:

- [all-row streamed-pair checker](../scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_independent_check_2026_08_09.py)

Direct scientific dependencies:

- [Cycle 750 intrinsic cube graphs and pair-count distance layers](PHYSICAL_CELL_CUTTING_CARRIER_CUBE_METRIC_CYCLE750_NOTE_2026-08-09.md)
- [Cycle 751 ambient preservation of carrier distances through three](PHYSICAL_CELL_CUTTING_OBJECT_DISTANCE_CYCLE751_NOTE_2026-08-09.md)

```text
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_shape_census_least_sharing_cycle752_note_2026-08-09
target_blocker_text: enumerate every induced Q4 in the complete never-sharing graph and test whether a reading-blind shared-cutting total separates its declared-reading classes
source_of_blocker_text: frontier_question
reachability_to_target: direct finite exhaustive computation on the supplied coordinate four-cube
artifact_role: bounded finite incidence theorem candidate
next_trace_action: independent audit of the landed primary and helper evidence
conditional_surface_status: direct Cycle 750 and Cycle 751 dependencies remain subject to independent audit
hypothetical_axiom_status: none
admitted_observation_status: none
claim_type_reason: an exhaustive theorem on one supplied finite incidence object, with no causal, charge-specific, physical-metric, or multicell extension
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_shape_census_least_sharing_cycle752_independent_check_2026_08_09.py
```

## Exact target and terminology

On the supplied `15,800` by `192` cutting-piece incidence table, join two
distinct pieces exactly when no cutting contains both. Call the resulting
graph `G`. An induced `Q_4` is a sixteen-vertex subset whose induced graph in
`G` is isomorphic to the four-dimensional cube graph.

For any sixteen-piece subset `S`, define its shared-cutting total by

```text
T(S) = sum over unordered {p,q} contained in S of
       (the number of cutting rows containing both p and q).
```

This statistic uses the incidence table but does not consult a reading label.
“Reading” means one of the eight declared binary target vectors already
reconstructed by the finite cutting lane. The theorem asks for the complete
induced-`Q_4` census and the distribution of `T` across its reading classes.

No frequency measure on all sixteen-subsets is declared. Accordingly this
note does not call `Q_4` “common” or “rare.” No causal meaning is assigned to
`T`, and the phrase “carries the charge” is not used as a scientific claim.

## Inputs and provenance

Cycle 750 supplies the current primary and independent certificates for the
complete `132`-member minimum-carrier census and its `60` induced-`Q_4` / `72`
split-`Q_3` classification. Cycle 751 supplies the current primary and
independent certificates for the complete `192`-vertex ambient
never-sharing graph. Both Cycle 752 executables authenticate the source and
receipt bytes of both dependencies and reject failed or changed certificates.

The primary independently rebuilds all `15,800` cutting rows, the `192`
supported pieces, all eight reading vectors, all `132` minimum carriers, the
dense co-incidence matrix, and the induced-`Q_4` census. The helper imports no
Cycle 752 primary symbols. It live-replays Cycle 751's all-row streamed-pair
checker, then enumerates each induced `Q_4` once at its least-numbered vertex
by coordinate completion.

The coordinate four-cube and eight declared reading vectors are supplied
finite data of this lane. No measured, fitted, literature, observational,
normalization, boundary-condition, framework-primitive, or axiom value enters
the theorem.

## Complete induced-`Q_4` census

The complete census is:

| quantity | exact count |
| --- | ---: |
| induced `Q_4`s through each piece | `4,978` |
| induced `Q_4`s in `G` | `59,736` |
| realizing none of the eight declared readings | `59,676` |
| realizing the declared four reading | `60` |
| realizing any of the other seven declared readings | `0` |

The incidence identity `192 * 4,978 = 16 * 59,736` checks the per-piece and
global counts. The primary verifies closure under its `50` checked generators;
the helper verifies closure under all `384` supplied incidence symmetries.

These `59,676` counterexamples establish one narrow negative: induced-`Q_4`
shape is not sufficient to imply any declared reading on this supplied finite
object. They do not show that `Q_4` shape is uncorrelated with a reading,
unnecessary for four, or irrelevant in a different population.

## Exact separation by shared-cutting total

Within the enumerated induced-`Q_4` population, `T` separates the two observed
reading classes:

| class | exact range boundary |
| --- | ---: |
| all `60` four-reading induced `Q_4`s | `T <= 19,800` |
| all `59,676` no-reading induced `Q_4`s | `T >= 20,338` |

Thus the first `60` shapes in nondecreasing `T` order are exactly the
four-reading shapes. Equivalently, on this enumerated domain only,
`T <= 19,800` if and only if the induced `Q_4` realizes the declared four
reading. There is no sampled tail and no unclassified induced `Q_4` between
the two bounds.

The separation is also vertex-local. At every one of the `192` pieces, the
five least-`T` induced `Q_4`s through that piece are exactly its five
four-reading carriers. The smallest difference from the fifth to the sixth is
`538`.

Two weaker diagnostics show why the exact population statement matters:

| diagnostic on `Q_4` graph-distance bands | admitted shapes |
| --- | ---: |
| maximum distance-two count below minimum distance-three count | `60` |
| maximum distance-three count below minimum distance-four count | `1,488` |
| every antipodal count equal to `433` | `672` |

On the `60` four-reading `Q_4`s, the exact shared-count bands are the current
Cycle 750 bands: distance two uses
`{170,171,173,174,178,183,184}`, distance three uses `{240,245,250}`, and
distance four uses `{433}`.

The separation does not distinguish four from another reading in a mixed
population: no induced `Q_4` in this census realizes one of the other seven
declared readings. It therefore supports neither a charge-specific selector
nor a causal mechanism.

## Derived parity floor

Every piece occurs in `1,975` cutting rows, so a sixteen-piece set has
`16 * 1,975 = 31,600` total row incidences. Realizing the four target forces
odd multiplicity on `5,664` rows and even multiplicity on the remaining
`10,136` rows. For row multiplicity `m`, that row contributes
`binomial(m,2)` to `T`.

The integer minimum is obtained by a discrete-convex marginal argument.
Start the odd rows at multiplicity one and the even rows at zero. Adding two
incidences to a row of current multiplicity `m` preserves parity and increases
`binomial(m,2)` by `2m+1`. The target total requires

```text
(31,600 - 5,664) / 2 = 12,968
```

such two-incidence increments. The `10,136` cheapest increments are the
even-row moves `0 -> 2`, each costing one. The remaining `2,832` cheapest
increments are odd-row moves `1 -> 3`, each costing three. Every further
increment costs at least five. Therefore

```text
T >= 10,136 * 1 + 2,832 * 3 = 18,632.
```

Both executables reconstruct this minimum from the sorted marginal costs; it
is not inferred from the observed carriers.

The minimum induced-`Q_4` carrier total is `19,640`, or `1,008` above the
floor. A minimum example has row-multiplicity histogram

```text
m = 0: 252 rows
m = 1: 2,832 rows
m = 2: 9,632 rows
m = 3: 2,832 rows
m = 4: 252 rows.
```

Its incidence sum is `31,600` and its pair total is `19,640`. Across all
`132` minimum carriers, the totals are exactly
`{19,640, 19,672, 19,800, 24,216}`. The `1,008` excess and these realized
totals are measured finite-object facts; the parity argument does not derive
them or prove the lower bound attainable.

## Independent reconstruction and proof-obligation graph

The obligation graph is acyclic:

1. current Cycle 750 primary and helper receipts bind the complete carrier
   census and intrinsic graph classification;
2. current Cycle 751 primary and helper receipts bind the ambient graph and
   explicitly reject total `Q_4` isometry;
3. the Cycle 752 primary rebuilds all cutting rows and uses a dense integer
   Gram product, while the helper replays the independently streamed pair
   matrix;
4. the primary uses rooted backtracking over checked generators, while the
   helper roots only at the least vertex and completes binary coordinates by
   exact adjacency signatures;
5. both classify all eight declared reading vectors by row parity, rank all
   `59,736` shapes, and check every vertex-local ranking;
6. both derive the parity floor by an explicit marginal-cost construction;
7. exact equality, dependency, and hostile-mutation gates discharge the
   finite target.

The strongest unproved extensions are a probability measure on sixteen-piece
subsets, a mixed-reading `Q_4` classification, a causal explanation of `T`, or
an extension to another cell or lattice. Each is stronger than the target and
is not claimed. The proof-obligation result is `CLOSED` for the stated finite
theorem and `OPEN` for those extensions.

## No-Go Discipline Gate

The negative statement retained here is only that induced-`Q_4` shape is not
sufficient for a declared reading on this supplied object. The broader
submitted slogans about rarity and what “carries” charge are withdrawn.

### N1 — alternative attacks

1. **Population route — ATTEMPTED.** Rebuild all `15,800` rows and enumerate
   every induced `Q_4`; both implementations return `59,736`, so the
   counterexamples are not a sampled-control artifact.
2. **Pair-arithmetic route — ATTEMPTED.** Replace the primary dense Gram
   product with Cycle 751's row-streamed unordered-pair counter; every census
   and separation boundary agrees.
3. **Graph-enumeration route — ATTEMPTED.** Replace rooted backtracking with
   least-vertex coordinate completion and exact induced-degree checks; the
   global and per-piece counts agree.
4. **Reading route — ATTEMPTED.** Reconstruct all eight target vectors from
   witness supports and compare packed row-parity signatures for every shape;
   exactly `60` match four and none match another declared reading.
5. **Symmetry/local route — ATTEMPTED.** Check all `384` supplied incidence
   symmetries and all `192` rooted rankings; the census is closed and the
   local five-versus-sixth boundary holds everywhere.
6. **Hostile route — ATTEMPTED.** Mutate dependency status, the Cycle 751
   antipodal boundary, census count, and pair-total edge; fail-closed
   contracts reject each change.

These routes differ in primary object or terminal obligation: population,
pair arithmetic, graph construction, reading parity, symmetry/locality, and
adversarial provenance.

### N2 — wall independence

No independent walls or admissions are claimed. Cycle 750 and Cycle 751 are
ordered finite-data dependencies, and Cycle 751 already cites Cycle 750; both
are authenticated directly here to prevent a stale intermediate receipt.
There is no wall count to inflate.

### N3 — hidden-wall scan

“By construction” is used only for the explicit parity-floor minimization and
is expanded into its marginal costs. The supplied coordinate object and eight
declared targets are named finite inputs. No “standard,” “canonical,”
“framework provides,” “background,” or primitive language supplies an
unstated scientific premise.

### N4 — residual matching

| cited source | exact residual used here | match |
| --- | --- | --- |
| Cycle 750 | complete `60/72` intrinsic carrier-shape census and carrier-local count bands | yes |
| Cycle 751 | complete ambient graph and the explicit failure of total `Q_4` isometry | yes |

Neither dependency is cited as evidence for the new `59,736`-shape census or
pair-total separation; both Cycle 752 implementations compute those results.

### N5 — rhetoric and resolution

- `per_element`: all `192` pieces enter the complete induced-`Q_4` census;
- `per_site`: one supplied coordinate four-cube only; no site family tested;
- `per_mode`: no modal decomposition exists for this finite binary object;
- `per_block`: every one of `15,800` cutting rows enters the pair counts;
- `lattice_wide`: no multicell, infinite-lattice, continuum, or physical
  charge mechanism is tested or claimed.

Both canonical caches must carry the corresponding five-line execution
certificate.

### N6 — partial closure and primitive scan

No new axiom or framework primitive is proposed or needed. A naming
convention cannot turn the exact census into a probability measure, add an
other-reading `Q_4`, or establish causation. Those extensions require new
finite populations or a separate physical bridge, not relabelling.

### N7 — steelman

A hostile reviewer can correctly argue that `59,676` no-reading `Q_4`s do not
make the shape irrelevant: `Q_4` could still be necessary for the four
reading, strongly associated with it under a future measure, or one component
of a joint selector. The same reviewer can also argue that the low pair total
does not “carry” charge, because the enumerated population contains no
other-reading `Q_4` against which charge specificity could be tested. That
steelman defeats the broader submitted rhetoric. It does not defeat the
narrow counterexample statement or the exact within-population separation,
which are the only claims retained here.

### N8 — cross-cycle echo

Cycle 750 withdrew a broad non-ambient interpretation after one corner
statistic failed to exclude every relabelling. Cycle 751 withdrew total
isometry after every `Q_4` antipode shortened. Both were repaired by replacing
the slogan with the exact tested population and explicit counterexamples.
Cycle 752 applies the same mechanism: “common,” “the mark,” and “carries the
charge” are replaced by a complete finite census, a sufficiency counterexample,
and an exact restricted-domain equivalence.

No failure condition remains after those demotions. Gate status: `PASS` for
the narrow finite negative above.

## Review record and hard landing conditions

Review-loop replaced the submitted half-row predecessor scan with the full
`15,800`-row inventory, added nonzero failure exits and fail-first receipts,
bound current Cycle 750 and Cycle 751 primary and independent certificates,
added a structurally independent helper, removed the raw cold-output artifact,
proved the parity floor by explicit discrete-convex marginals, and narrowed
the rarity/mark/causal-charge language to the exact finite theorem.

Hard landing conditions:

- both executables and both input-bound receipts land with canonical cache
  envelopes;
- the primary and helper each fail nonzero on a load-bearing mutation;
- the helper mapping for claim id
  `physical_cell_cutting_shape_census_least_sharing_cycle752_note_2026-08-09`
  lands in both citation dependency maps;
- the citation-graph manifest is regenerated from the final proposed tree;
- generated ledger, queue, effective-status, and front-door outputs do not
  land;
- no audit verdict is applied by review-loop.

## Honest boundary

- The theorem is exact only for one supplied finite coordinate four-cube and
  eight declared readings.
- Cycles 750 and 751 are direct scientific dependencies and are not silently
  promoted by this note.
- No frequency measure is supplied, so no statistical rarity claim follows.
- Shape non-sufficiency does not imply non-necessity or lack of association.
- The pair-total equivalence is restricted to the enumerated induced-`Q_4`
  population, whose only present reading is four.
- No causal selector, physical charge mechanism, another-reading
  discrimination, all-sixteen-subset classification, physical metric, or
  multicell extension follows.
- Audit status remains unset until the independent audit lane acts.
