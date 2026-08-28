# Block 231 Preregistration

No Block-231 primary runner may be written or executed before this packet is
committed. The topology, summary algebra, contact products, writer guard,
carrier budget, test order, proof obligations, and pivot gates are frozen.

## Exact target contract

| Field | Contract |
|---|---|
| statement | every execution of the frozen local rules on every finite declared typed tree terminates at one contact-correct Record normal; the exact labelled rows embed in the inherited rank-128 carrier and their positive-rate GKSL generator absorbs on the active component subspace |
| domain | a finite path whose two leaves are typed `rho` and seam/writer `alpha`, or a finite maximum-degree-three tree whose three graph leaves are exactly typed `rho/lambda/chi` and whose unique seam/writer `alpha` is an internal vertex; explicit one-site and zero-edge degeneracies only |
| allowed premises | supplied static reciprocal labelled tree incidence; the Block-230 five-atom algebra; the inherited rank-128 proper-cubic carrier; at most one exact foreign participant per site; a supplied common positive rate `gamma` as time unit |
| forbidden weakenings | bounded size as arbitrary proof; untyped pendant; supplied winner/order/scheduler; component size/count/diameter; owner/ID/coordinate/epoch/clock; hidden Record-times-summary tensor layer |
| completion witness | arbitrary-tree termination/confluence/contact-safety theorem, exact labelled isometry/row lift, finite carrier accounting, GKSL completeness, no active recurrent class, and analytic absorption bound |
| not closure | the minimal-Y control alone, abstract OR algebra alone, a dimension count without isometry, diagonal classical dynamics only, imported fairness, or promotion to Born/law selection/gravity/TOE |

Every ordinary three-leaf domain tree is therefore a subdivision of one Y:
there is exactly one degree-three junction, all other nonleaves have degree
two, and there is no untyped branch. The seam/writer may be the junction or
any internal arm vertex. Typed labels are distinct except in the explicitly
enumerated one-site degeneracy.

## Frozen summary/contact rules

Use exactly the Block-230 atoms and product:

```text
rho=1, alpha=2, lambda=4, chi=8, phi=16
Sigma={0,...,31}, x join y = x bitwise-OR y.
```

Initial summaries place the corresponding boundary atom at each typed site
and zero elsewhere; coincident degenerate labels are ORed. A live foreign
participant is exact incidence, not inferred from `phi`.

For every reciprocal labelled tree edge `(i,j)`, collect the complete live
participant mask `M` on its two endpoints and set

```text
u = s_i | s_j | (phi if M is nonempty else 0)
(s_i,s_j,M) -> (u,u,empty),
```

when either endpoint changes or `M` is nonempty. Consume exactly `M`. Quiet
and contact products have disjoint exact source cylinders. A one-site seed
consumes the sole-site participant in the zero-edge degeneracy.

Expected coverage is `rho|alpha` on a path and
`rho|alpha|lambda|chi` on a three-leaf tree.

## Frozen all-neighbor terminal rule

Let `w` be the unique seam/writer. A terminal star row is enabled only when

```text
E subset s_w
and s_v = s_w for every neighbor v of w.
```

Its support is the writer plus all incident neighbors, hence at most four.
Let `M_star` be the complete participant mask on that support and

```text
u = s_w | (phi if M_star is nonempty else 0).
```

The product row consumes exactly `M_star`, writes `u` to every incident
neighbor, and replaces the writer summary by `ABORT` iff `phi subset u`, else
`CLEAN`. No edge incident to a terminal writer remains enabled. Nonwriter
edges continue ordinary summary/contact merges until normal.

The terminal source checks equality, not size, boundary count, path length,
or absence at a distance. All `2^(1+degree(w))` local participant masks are
distinct exact cylinders. The one-site degeneracy uses the same outcome rule.

## Stage A — arbitrary-tree compiler theorem

First reproduce the Block-230 minimal Y counts `51 states / 70 transitions /
19 normals` under the old E-only guard and `33 / 52 / 1` under this guard.

Then exhaust:

- every contact subset on paths through twelve vertices;
- zero/one/two contacts on paths through twenty-four vertices;
- every labelled subdivision-Y arm-length triple with total vertices through
  ten, every internal seam/writer placement, and every contact subset;
- sparse, adjacent, dense, unequal-arm, junction-writer, arm-writer, translated
  Block-229 quotient, and one-site/zero-edge controls through total size
  twenty-four where full subsets are not requested.

Report fixtures, unique states, directed transitions, maximum graph, normal
count, cycles, rank failures, participant accounting, first failure, and child
reflection pairs. Multi-source union exploration is allowed only when each
fixture's initial state and expected normal remain separately checkable.

The arbitrary finite proof must establish:

1. pairwise OR merges terminate and have the component union as unique normal;
2. the integer rank
   `sum_live_summary_site(5-popcount(s_i)) + live_participants + live_writer`
   strictly decreases on every seed, merge, and terminal product;
3. typed-hull contact safety: if the writer has every typed endpoint bit, each
   still-live or already-quenched participant lies on a typed-leaf-to-writer
   information path and therefore contributes persistent `phi` before a clean
   terminal can fire;
4. at terminalization the writer holds the global union `U`; removing it leaves
   each component of `T\{w}` seeded at its boundary neighbor by `U`;
5. every reachable terminal/merge peak joins: disjoint rows commute, incident
   quiet writer edges are identities, contact products join inside the writer
   star, and reachable exterior-neighbor products cannot hide a participant
   beyond an equality-ready cut;
6. every execution, not merely every fair execution, reaches the same terminal
   outcome and all nonwriter sites reach `U`.

Any imported target-equivalent lemma or bounded census standing in for these
items fails Stage A and stops the physical lift.

## Stage B — explicit rank-128 labelled lift

Only after Stage A passes, construct rather than merely count an isometry for
two parity copies of the 32 summaries, four inherited QND terminal rays, and a
rank-60 complement:

```text
summary rays  0..63
terminal rays 64..67
default       68..127
```

The inherited per-parity transient `C4` multiplicities are `(9,8,10,8)`.
The summary subspace must realize `(8,8,8,8)`, leaving `(1,0,2,0)` per parity;
the six freed directions plus the inherited rank-54 default give rank 60.
For the `lambda<->chi` reflection, 16 fixed summaries occupy eight character-0
and eight character-2 rays; eight exchanged pairs occupy conjugate
character-1/character-3 rays. Materialize the basis map, Gram matrix,
intertwining action, complement projectors, terminal orthogonality, and
deterministic digest. A bookkeeping interval without vectors is failure.

Generate exact physical rows on labelled paths/Y subdivisions through total
size eight and all contact masks, including the inherited 47 signatures,
parallel equal-neighbor darts, reciprocal crosswire, all twelve Y triples, and
child reflection. Each row must satisfy `target == Row.apply(source)`, exact
reciprocal ports, participant-local consumption, distinct many-to-one
environment labels, no orphan role, support at most four, and the same visible
summary/terminal action as Stage A.

Static labelled incidence is an explicit premise. If a summary ray must itself
store a dynamic dart, Y orientation, or endpoint ID, declare the alias and
pivot to a distributed edge/incidence factor rather than silently importing it.

## Stage C — local GKSL generator and absorption

For each disjoint exact source cylinder/environment label use

```text
L_e = sqrt(gamma) |target_e><source_e|,
D_e(rho) = L_e rho L_e^dagger - 1/2 {L_e^dagger L_e,rho}.
```

Require nonnegative rates, exact source orthogonality where claimed, distinct
environment labels for many-to-one rows, termwise trace preservation, no
cross-cylinder amplitude addition, and QND identity on unmatched default and
terminal sectors.

On each finite active component, enumerate closed communicating classes for
the bounded fixtures and prove analytically that strict rank plus positive
rates leaves no active recurrent class. If `R_max` is the initial rank, report
the bounds `E[jumps] <= R_max` and `E[t_absorb] <= R_max/gamma`; distinguish
dimensionless jump count, supplied rate unit, and any unavailable physical
clock. State the induced clean/abort instrument separately from Born weight,
law selection, matter/gravity coupling, and arbitrary-lattice extension.

## Decision classes and pivot

- `positive-neighbor-ready-aci-physical-instrument`;
- `positive-neighbor-ready-aci-arbitrary-tree-open-labelled-lift`;
- `positive-neighbor-ready-aci-labelled-open-absorption`;
- `scoped-neighbor-guard-confluence-or-contact-failure`;
- `scoped-neighbor-guard-labelled-carrier-failure`;
- `scoped-neighbor-guard-cp-or-absorption-failure`;
- `partial-attempt-with-named-untested-routes` under the current N1--N8 gate.

Any Stage-A failure pivots first to distributed labelled incidence or an
acknowledgement semilattice. A Stage-B dynamic-dart alias pivots to an edge
factor. A genuine dimension overflow pivots to a larger carrier proposal and
owner approval. No author result changes an axiom, audit verdict, retained
status, obligation, or TOE percentage.
