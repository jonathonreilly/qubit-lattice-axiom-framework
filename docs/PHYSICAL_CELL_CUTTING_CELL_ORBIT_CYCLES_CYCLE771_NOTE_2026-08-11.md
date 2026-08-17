# Order-four stabilizer products and characteristic-independent orbit-table rank

Date: 2026-08-11

Authority: none; self-contained finite construction proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [cell-orbit cycle runner](../scripts/physical_cell_cutting_cell_orbit_cycles_cycle771_2026_08_11.py)

Direct scientific dependencies: none.

Constitutional effect: none. This note changes zero axioms, primitives,
registries, policy rules, audit verdicts, effective statuses, or framework claims.

## Trace and status fields

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_cell_orbit_cycles_cycle771_note_2026-08-11
target_blocker_text: "explain the uniform singleton-orbit cycle length and rank on the declared finite cell object"
source_of_blocker_text: frontier_question
reachability_to_target: direct
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "the target domain is the declared finite unit-four-cube object"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "finite group-action and integral linear-algebra theorems with exhaustive certificates"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

**Target theorem.** On the finite object declared below, the signed-coordinate
action on piece-cover pairs is free; every one of its `96` orbit tables is a
disjoint union of `48` eight-edge bipartite cycles because all `48` relevant
stabilizer-generator products have order four; and over every field each table
has rank `144`, nullity `48`, and a cyclewise integral alternating kernel basis.

The theorem domain is finite combinatorics and linear algebra. Physical
interpretation, a Record map, probability or measurement content, continuum or
multicell extension, and framework-level consequences are separate open targets.

## Inputs, imports, and provenance

| item | classification | role and provenance |
| --- | --- | --- |
| labelled corners `{0,1}^4` | declared finite-model data | Defines the unit four-cube used by this packet. |
| five-corner simplices with determinant magnitude one | declared selection rule | Enumerated directly from the `16` labelled corners. |
| minimum adjacency cost | declared selection rule | Counts non-edge corner pairs; the minimum and all minimizers are recomputed. |
| shifted `5^4` rational grid | enumeration nuisance | Drives the exact-cover search; genericity, masks, uniqueness, volumes, and continuous cutting conditions are checked. |
| cutting and cover definitions | declared finite-model data | A cutting is a full-cell union of `24` selected simplices with pairwise disjoint interiors; a cover is an eight-piece set meeting every cutting once. |
| full signed-coordinate action | declared symmetry data | All `4! * 2^4 = 384` maps are built and checked as a group action on pieces and covers. |
| orbit-stabilizer, two-involution normal form, determinant/rank-nullity facts | standard mathematical import | Used in the finite proof; all concrete hypotheses are rebuilt and gated. |
| `p=1000003`, `q=1000033`, seed `3` | computational nuisances | Both moduli are gated prime and distinct. The seed is fixed but does not affect the exact theorem. |
| Python integer/Fraction arithmetic and NumPy `int64` arrays | implementation import | Exact geometry and theorem paths use integers or `Fraction`; modular arrays have ample signed-64-bit headroom. |
| cache | execution evidence | The canonical cache records one exact invocation; it supplies no scientific premise. |
| physical, Record, probability-law, continuum, and multicell bridges | open bridge inventory | These lie outside the declared theorem and supply zero premise. |

No measured, fitted, observational, or literature value enters. The minimal
axiom set supplies zero premise. Branch ancestry and cycle numbering supply zero
scientific premise.

## Declared finite object and exact geometry certificate

The runner enumerates all `2,672` determinant-one five-corner candidates, finds
adjacency-cost floor `6`, and keeps all `400` minimizers. Its shifted grid avoids
every kept facet plane. The exact-cover search returns `15,800` distinct mask
covers, each containing `24` distinct pieces.

That mask calculation is not the continuous certificate by itself. The runner
also checks every kept simplex has normalized volume one, each returned set has
total normalized volume `24`, and every pair of co-occurring simplices has
intersection of affine dimension at most three. Each simplex lies in the unit
cube because its vertices do. Pairwise interior disjointness and total volume
therefore make the closed union the whole cube: a nonempty relatively open
complement would have positive volume. Thus the returned sets are genuine
continuous simplex cuttings, not merely sampled covers.

Exactly `192` pieces occur, each in `1,975` cuttings, with
`24 * 15,800 = 192 * 1,975 = 379,200`. The clique construction returns `192`
distinct covers. Every cover contains eight pieces, every piece belongs to eight
covers, and each cover meets every cutting once (`C0-C1`).

## Free pair action

Permuting coordinates and independently flipping them gives `384` distinct
corner maps. The runner checks all `147,456` compositions, the induced action
law, bijectivity, distinctness, and transitivity on both the `192` pieces and the
`192` covers (`C2`). Both point stabilizers have order two (`C3`).

Exactly `12` nonidentity maps fix a piece and exactly `4` fix a cover. The two
sets are disjoint; their fixed-point counts account for every piece and cover,
and all `16` maps are involutions (`C4-C6`). Consequently the stabilizer of each
piece-cover pair is trivial. The `36,864` pairs split into exactly `96` disjoint
orbits of size `384` (`C7`).

## Order-four products and eight-edge cycles

Read one orbit as a binary table with covers as rows and pieces as columns.
Every row and column contains two ones (`C8`). The unique nonidentity cover
stabilizer swaps the two pieces in its row; the unique nonidentity piece
stabilizer swaps the two covers in its column (`C9`).

Let `p` and `c` be those involutions at a base edge. Alternating row and column
switches generates the component through that edge. The two-involution normal
form consists of `(pc)^k` and `p(pc)^k`, so freeness makes the component size
`2 ord(pc)`. Reversing the product gives a conjugate and preserves its order.

There are `12` distinct piece-stabilizer generators and `4` distinct
cover-stabilizer generators. Every one of their `48` products has order exactly
four (`C10`). Hence every component has eight edges. The independent component
walk finds exactly `48` cycles in each table and `4,608` in all, and checks the
local product-order identity on every cycle (`C12-C13`). The order-four fact is
selective: combining the same `12` piece generators with all `75` involutions
gives the exact product-order histogram
`{1:12, 2:216, 4:480, 8:192}` (`C11`).

## Rank and integral kernel over every field

Order the four cover vertices and four piece vertices cyclically on one
component. Its block is

```text
1 1 0 0
0 1 1 0
0 0 1 1
1 0 0 1
```

Its determinant is zero and its leading `3 x 3` minor has determinant one.
Thus the block has rank exactly three and nullity one over every field,
including characteristic two (`C14`). The runner checks every component has
this exact block and that its rows and columns carry no entries outside the
block (`C15`). Therefore each table has rank `48 * 3 = 144` and nullity `48`
over every field (`C16`).

On each cycle the integral vector `(1,-1,1,-1)` is annihilated. The `48` cycle
vectors in one table have disjoint supports and are primitive; the unit minor
proves the kernel has rank one per block. They therefore form a basis of the
integral kernel, and their reductions form the field kernel in every
characteristic (`C17`). Direct elimination at `F_1000003` and `F_1000033`
returns rank `144` on all `96` tables as an internal cross-check (`C18`). It is
not the proof of the characteristic-independent result. Moving one entry in a
scratch table breaks two-regularity and changes its `F_1000003` rank from `144`
to `145` (`C19`).

## Incidence corollaries with explicit fields

The `96` orbit tables partition all piece-cover pairs, so their entrywise sum is
the all-ones `192 x 192` table (`C20`). The cover-membership incidence table is
the exact sum of four derived orbit labels (`C21`). Its rank is `105` over both
declared primes, with modular kernel dimension `87` and a `39`-rank drop from a
singleton table (`C22`). At `F_1000003`, each of the four summands has rank
`144`, while their six pair sums have ranks
`72,93,117,129,144,144` (`C23`). These field-specific measurements are
auxiliary finite claims; no rational value is inferred from them here.

## What is new relative to current main

Current-main Cycle 768, named here only as non-load-bearing context by
`PHYSICAL_CELL_CUTTING_COMPLEMENT_SPACES_CYCLE768_NOTE_2026-08-11`, already
records the all-`96` singleton cycle structure and exact rational rank `144`.
Cycles 758 and 766 likewise predate this landing. This note does not claim the
all-`96` rational census as new.

The new science is the exhaustive order-four theorem for all `48` relevant
stabilizer products, the resulting dihedral explanation of every cycle length,
the unit-minor proof valid in every characteristic, and the explicit integral
cyclewise kernel basis. The rational result is prior corroboration; the proof
route and characteristic-independent/integral conclusions are stronger. Any
unlanded companion cycle supplies zero premise.

## Proof-obligation graph

The obligation graph is acyclic:

1. `declared corners and selectors -> continuous simplex cuttings and covers` -
   proved here by exhaustive search, exact volume, and exact intersection gates.
2. `finite object + signed-coordinate maps -> group actions` - proved here by
   exhaustive closure, bijection, action-law, and transitivity checks.
3. `disjoint fixer classes -> free diagonal action -> 96 full orbits` - proved
   here and independently partition-checked.
4. `two-regular tables + stabilizer switches + order-four products -> eight-edge
   cycles` - the two-involution lemma is standard; every concrete hypothesis and
   component is checked here.
5. `cycle blocks + zero determinant + unit minor -> all-field rank/nullity` -
   proved here without large-matrix elimination.
6. `primitive alternating vectors + disjoint supports + block nullity one ->
   integral kernel basis` - proved here.
7. `orbit partition -> all-ones sum`, and `cover equivariance -> four-orbit
   incidence sum -> modular incidence/pair ranks` - proved here with field labels.

The finite theorem has no open internal lemma. The strongest missing bridge is
an interpretation of this declared finite object as a physical, Record,
probabilistic, continuum, or multicell construction; that bridge is outside the
claim and supplies no premise.

## Mutation and independent-check ledger

Every scratch mutation is in memory and leaves the scientific object unchanged:

| family | mutation | required response |
| --- | --- | --- |
| mask constructor | zero one kept-piece mask | full-cover certificate rejects |
| continuous geometry | change one normalized simplex volume | volume/union certificate rejects |
| group constructor | duplicate one signed-coordinate map | distinct/closure certificate rejects |
| induced action | swap two images in the identity permutation | action-law certificate rejects |
| freeness | give one cover fixer an artificial piece fixed point | common-fixer certificate rejects |
| orbit partition | delete one pair from one orbit | exhaustive partition certificate rejects |
| component walk | delete one piece vertex from one cycle | cycle-partition certificate rejects |
| order census | change one product order | exact histogram certificate rejects |
| block orientation | delete one orbit-table entry | exact block certificate rejects |
| integral kernel | delete one nonzero kernel coordinate | annihilation/support certificate rejects |
| modular rank | duplicate a row of a pinned rank-two matrix | rank pin rejects |
| incidence decomposition | increment one entry of the four-orbit sum | exact incidence certificate rejects |
| pair-rank vector | increment one of the six values | exact vector certificate rejects |

Independent review used implementation paths separate from the runner: a
Leibniz determinant on every five-corner subset; direct signed-affine descriptor
composition; set-based orbit partitioning; vertex-component breadth-first
search; a Smith-form calculation yielding `diag(1,1,1,0)` for the block; trial
division for both primes; and a separate incidence-orbit reconstruction. These
checks found zero discrepancies. The runner reports all `13` mutations rejected
in `C24`.

## Edge-case and scope ledger

| case | disposition |
| --- | --- |
| characteristic two | included; the unit minor remains one and the alternating vector reduces to a nonzero all-ones cycle vector |
| `pc` versus `cp` | both orders agree because the two products are conjugate |
| common piece/cover stabilizer | excluded by exhaustive fixer disjointness, which proves freeness |
| rational interpretation of incidence and pair-rank measurements | not claimed; the declared fields remain explicit |
| choice of four incidence labels | derived from cover membership, not supplied externally |
| singleton rank as a selector | uniform across all `96`; it is recorded here only as a common finite invariant |
| physical quantity, Record readout, probability law, continuum, multicell lattice | outside the declared finite domain |
| audit status | unset pending independent audit; this note sets zero verdict |

The landing set consists of this note, the runner, its canonical cache, the
harness registration, and the required citation manifest only. Generated audit
rows, queue/status outputs, and audit verdicts are outside this review-lane
change.
