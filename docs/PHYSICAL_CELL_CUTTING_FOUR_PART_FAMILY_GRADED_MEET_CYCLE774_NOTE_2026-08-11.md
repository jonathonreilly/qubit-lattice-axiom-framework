# Finite four-part orbit-table family and sign-character meet

Date: 2026-08-11

Authority: none; self-contained finite construction proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [four-part family runner](../scripts/physical_cell_cutting_four_part_family_graded_meet_cycle774_2026_08_11.py)

Direct scientific dependencies: none.

Constitutional effect: none. This note changes zero axioms, primitives,
registries, policy rules, audit verdicts, effective statuses, or framework claims.

## Trace and status fields

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_four_part_family_graded_meet_cycle774_note_2026-08-11
target_blocker_text: "characterize exact kernel overlap and selected-block fibres inside the declared finite four-part orbit-table family"
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "the target domain is the declared finite unit-four-cube object and the two named odd prime fields"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "finite geometry, group-action combinatorics, integer identities, and explicitly field-labelled linear algebra"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

**Target theorem.** On the declared finite unit-four-cube object:

1. the `384` signed-coordinate maps act freely on the `192 * 192 = 36,864`
   piece-cover pairs, producing `96` disjoint orbit tables, each 2-regular in
   rows and columns;
2. every four-table subset is therefore a distinct binary 8-regular matrix,
   giving exactly `C(96,4) = 3,321,960` family members;
3. the cover-incidence member and the first four non-incidence orbit-table
   member both have nullity `87` and meet dimension `33` over each of
   `F_1000003` and `F_1000033`, with kernel-dimension profile
   `[3,3,6,6,12]` and meet profile `[3,0,3,0,12]` by sign-character weight;
4. the weight-four character block has an exact integral basis of dimension
   `12` annihilated by every one of the `96` orbit tables; and
5. the weight-zero quotients have the same three-dimensional rational
   nullspace, while the declared deterministic sample has the exact
   selected-weight-three counts stated below over `F_1000003`.

The theorem domain is this finite construction. Framework identification,
physical-cell selection, Admissibility, Record/readout, probability,
measurement, dynamics, continuum interpretation, and multicell compatibility
remain open bridge targets outside this theorem.

## Inputs, imports, and provenance

| item | classification | role and provenance |
| --- | --- | --- |
| labelled corners `{0,1}^4` | declared finite-model data | Define the unit four-cube used in this packet. |
| five-corner simplices with determinant magnitude one | declared selection rule | Enumerated directly from the `16` labelled corners. |
| minimum adjacency cost | declared selection rule | Counts non-edge corner pairs; the minimum and every minimizer are recomputed. |
| shifted `5^4` rational grid with offsets `(1,2,4,8)/80` | enumeration nuisance | Drives candidate exact-cover search; genericity, mask visibility, uniqueness, volumes, and continuous geometry are separately gated. |
| cutting and cover definitions | declared finite-model data | A cutting is a full-cube union of `24` selected simplices with pairwise disjoint interiors; a cover is an eight-piece set meeting each cutting once. |
| full signed-coordinate action | declared symmetry data | All `4! * 2^4 = 384` maps and their actions on pieces and covers are rebuilt. |
| orbit and selector ordering | declared deterministic convention | Piece-cover pairs use piece-major lexicographic order; new orbits are recorded at their first unseen pair. The comparison uses the first four non-incidence orbit indices. |
| sample and selected-character rules | declared deterministic convention | The raw sample and selected weight-three character are defined explicitly below. |
| `1000003`, `1000033` | computational nuisances | The runner certifies that the distinct moduli are prime before field arithmetic. |
| finite group actions, constant-fibre projection, character decomposition in odd characteristic, rank-nullity, simplex volume and separation | standard mathematics | Concrete hypotheses are rebuilt and gated. |
| Python integer/`Fraction` arithmetic and NumPy `int64` arrays | implementation import | Scientific paths are exact; modular products stay within signed-64-bit headroom. |
| canonical cache | execution evidence | Records one invocation and supplies zero scientific premise. |
| framework/physical/Record/probability/continuum/multicell interpretations | open bridge inventory | Supply zero premise to the finite theorem. |

Measured, fitted, observational, and literature inputs: none. The framework
minimal axioms, branch ancestry, predecessor branches, and cycle numbering
supply zero scientific premise.

## Obligation graph

- `P0`: enumerate the `2,672` unit-determinant candidates and all `400`
  adjacency-cost-six minimizers.
- `P1` (depends on `P0`): enumerate the `15,800` shifted-mask exact covers and
  certify their continuous simplex geometry.
- `P2` (depends on `P1`): obtain the `192` used pieces and `192` covers, each
  cover meeting every cutting once.
- `P3` (depends on `P2`): build the signed-coordinate group, its actions, and
  the free pair-orbit partition with constant fibres.
- `P4` (depends on `P3`): prove the exact four-part family count and identify
  the incidence and comparison members by deterministic selectors.
- `P5` (depends on `P3`, `P4`): build the sixteen integral character blocks,
  prove the all-signs integer identity, and compute the two named-field kernel
  and meet profiles.
- `P6` (depends on `P5`): compute the exact weight-zero rational kernel and the
  explicitly selected-field sweep/sample counts.
- `P7`: reject one-fault mutations for geometry, orbit fibres, character signs,
  field ranks, quotient parity, selectors, sample construction, primality, and
  family membership.

Every obligation is a hard runner gate, and the dependency graph is acyclic.

## Exact geometry of the declared object

The runner finds `2,672` determinant-one five-corner candidates, adjacency-cost
floor `6`, and `400` minimizers. The shifted grid avoids every candidate facet.
Its exact-cover search returns `15,800` unique mask covers of `24` distinct
simplices.

The grid is an enumeration device rather than the continuous proof. Every kept
simplex has normalized volume one, so every returned 24-simplex set has the
four-cube's normalized volume `24`. Among used simplices, exactly `15,168`
unordered pairs co-occur. For each pair the runner finds a nonzero normal in
`{-1,0,1}^4` whose exact integer dot products weakly separate the two vertex
sets. Full dimensionality makes their interiors strictly separated. Pairwise
interior disjointness plus total volume establishes continuous union of the
unit four-cube.

Exactly `192` pieces occur, each in `1,975` cuttings, giving `379,200` slots by
either count. The exhaustive eight-piece cover search returns `192` covers and
checks that every cover meets every cutting exactly once.

## Orbit tables and the four-part family

Index a piece-cover pair by `s = 192*i + j`, with piece index `i` outer and
cover index `j` inner. Scan `s=0,...,36,863`; whenever a pair is unseen, record
its sorted orbit under the `384` signed-coordinate maps. This defines the orbit
order without predecessor authority.

The action is free, so all `96` orbits have size `384`. Transitivity on pieces
and covers makes both orbit projections constant-fibre maps. Since
`384/192=2`, every orbit table has exactly two ones in each row and each
column. The tables have disjoint support and partition the all-ones matrix.

Consequently every four distinct tables sum to a binary matrix with row and
column sums eight. Disjoint nonempty supports make two different four-subsets
different, so the family size is exactly `C(96,4)=3,321,960`.

The incidence member consists of orbit indices `[0,1,2,3]`. Define the ordered
outside list by removing those indices from `[0,...,95]`; the comparison member
is its first four entries, `[4,5,6,7]`. Both index identities are rebuilt from
the incidence matrix and selector rule. A repeated-table mutation and a
five-table mutation independently test binary membership and 8-regularity.

## Integral characters and named-field meet

The `16` pure coordinate flips act freely on the `192` pieces, with `12`
orbits. For sign mask `s`, put on each flip orbit the vector whose coordinate
at flip `f` is `(-1)^{popcount(s & f)}`. These sixteen integral blocks each
have dimension `12`. Their stacked Walsh transform has full rank over the two
named odd prime fields; characteristic two is outside this decomposition.

Every orbit table annihilates the entire weight-four block by direct integer
multiplication. Thus its twelve integral basis vectors lie in the kernel of
every four-part family member.

For the incidence and comparison members, over each of `F_1000003` and
`F_1000033`:

| character weight | number of blocks | incidence nullity | comparison nullity | meet dimension |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 3 | 3 | 3 |
| 1 | 4 | 3 | 3 | 0 |
| 2 | 6 | 6 | 6 | 3 |
| 3 | 4 | 6 | 6 | 0 |
| 4 | 1 | 12 | 12 | 12 |

Weighted totals give nullities `87/87` and meet `33`. The incidence-exclusive
profile is `[0,3,3,6,0]`, totaling `54`, and `54+33=87`. Both members are held
by the full signed-coordinate group. Its coordinate-permutation subgroup acts
transitively on sign masks of a fixed Hamming weight, which proves the reported
within-weight constancy. Over `F_1000003`, the difference has block-rank profile
`[6,9,6,6,0]` and total rank `102`.

## Weight-zero quotient

The flip action on covers has `24` orbits of size `8`; its action on pieces has
`12` orbits of size `16`. Each member's quotient is `24 x 12` with entries
exactly in `{0,2}`. The runner checks evenness before exact division. Each has
`12` distinct rows repeated twice. Halving one copy gives a binary `12 x 12`
matrix, 4-regular in both directions and rank `9` at both named primes.

Exact rational elimination on the incidence quotient supplies three independent
integer kernel vectors with entries in `{-1,0,1}`. Their disjoint size-four
supports partition the twelve coordinates, with two `+1` and two `-1` entries
per vector. Direct integer multiplication shows that these same vectors
annihilate the comparison quotient. Their independence gives rational nullity
at least three; a nonzero rank-nine minor modulo either named prime gives
rational rank at least nine. Hence both rational ranks are nine and the common
three-vector span is exactly their shared rational nullspace. The two quotient
matrices themselves are distinct and have different row multisets.

## Declared sweep and sample

All remaining statements in this section are over `F_1000003`. The selected
weight-three mask is the smallest integer mask of weight three, `7`.

The one-swap sweep replaces one incidence orbit index by one outside index. Its
`4*92=368` members realize `185` kernel/meet signatures. Kernel totals range
from `48` to `120`; meet totals with incidence range from `12` to `59`.

The raw deterministic sample concatenates:

- the `368` one-swap members;
- the `23` consecutive four-entry blocks of the ordered outside list; and
- all `C(8,4)=70` four-subsets of base `[0,1,4,5,6,7,8,9]`.

This makes `461` raw entries. The comparison member `[4,5,6,7]` occurs twice;
canonical sorted-tuple deduplication yields `460` unique members. At selected
mask `7`, their kernel-dimension histogram is
`{6:366, 7:55, 9:37, 12:2}`. Among the `366` dimension-six kernels, `169` meet
the incidence selected-block kernel in dimension zero. The sample realizes
`130` distinct selected-block kernels, `103` of dimension six, with maximum
multiplicity `27`. Incidence's selected-block kernel occurs `13` times and the
comparison kernel occurs twice. These are exact counts for this declared,
non-random sample. Full-family frequencies remain a separate open target.

## Mutation record

Gate `E31` requires all thirteen copied one-fault mutations to fail their
production predicates:

| mutation | protected path |
| --- | --- |
| erase one shifted mask | exact-cover object |
| change one simplex determinant | continuous volume closure |
| toggle one orbit-table entry | binary support and 2-regular fibres |
| flip one integral character sign | all-signs annihilation |
| toggle one incidence entry | named-field nullity/meet |
| make one quotient entry odd | exact quotient division |
| shift the four-index comparison selector | deterministic member identity |
| append a raw sample duplicate | sample construction/deduplication |
| alter one canonical multiplicity | canonical-kernel census |
| substitute a composite modulus | field premise |
| repeat one selected table | binary family membership |
| add a fifth selected table | 8-regular family membership |
| swap two incidence columns | character-block decomposition |

The runner declares `AUDIT_TIMEOUT_SEC = 300`. Its canonical cache is generated
through the repository cache harness and records the exact source hash,
resolved timeout, exit status, stdout, stderr, elapsed time, and peak memory.

## Scope boundary

This packet establishes the bounded finite theorem above. The next mathematical
target is a full-family fibre census for the selected-block kernel map. The
framework-to-four-cube selection bridge and all physical, Record, probability,
continuum, and multicell interpretations remain open and supply no premise here.
