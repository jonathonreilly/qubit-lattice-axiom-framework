# Finite small-block decomposition and Hamming-weight-four rank census

Date: 2026-08-09

Authority: none; self-contained finite construction proposed for independent
audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [finite small-block census runner](../scripts/physical_cell_cutting_small_matrix_census_cycle765_2026_08_09.py)

Direct scientific dependencies: none.

Boundary authority only:

- [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), cited only to distinguish the
  framework's proper-cubic and Record vocabulary from this declared finite
  full-four-cube action. It supplies no premise of the finite theorem.

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## Trace and status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: finite_small_block_hamming_weight_four_rank_census_2026-08-09
target_blocker_text: "decompose the declared finite covariant-table space and census its binary Hamming-weight-four family"
source_of_blocker_text: frontier_question
reachability_to_target: "direct exact finite construction and exhaustive enumeration"
artifact_role: "bounded finite representation-and-census theorem candidate"
next_trace_action: "independent audit of the landed source and runner evidence"
conditional_surface_status: "bounded to the declared labelled unit-four-cube object, full 384-map action, and stated coefficient fields"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite decomposition, rank, and exhaustive modular-census identities on one declared object"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

Let `G` be the `384`-element signed-coordinate-permutation group acting on the
declared `192` supported pieces and `192` covers below. Over the rationals, the
piece and cover permutation modules split into twenty common central parts. On
part `i`, every `G`-equivariant cover-to-piece table has the form
`identity(d_i) tensor M_i`, with `M_i` an `mc_i` by `m_i` rational matrix.
Consequently its rank is

```text
sum_i d_i rank(M_i),
```

and is at most `144`. The reconstructed cover table has exact rational rank
`105`; its eight non-full cover blocks have weighted rank drops summing to `39`.
An explicit equivariant integer table has exact rational rank `144`.

Over `F_1000003`, exhaustively enumerate the `C(96,4) = 3,321,960` binary
coefficient vectors of Hamming weight four in the cell-orbit basis. Their modular
ranks take `79` distinct values, with minimum `24`, maximum `144`, and the pinned
bin counts stated below. Exact rational elimination separately gives rank `24`
and `144` for explicit members of this finite family and rank `105` for the cover
reference table. Thus the rational minimum and maximum over this same binary
family are exactly `24` and `144`; the remaining histogram is explicitly a
modular histogram.

The theorem is finite combinatorics and finite representation theory. It is not a
selection rule for general covariant tables, a probability law, a proper-cubic
framework theorem, a physical piece-to-Record map, dynamics, or a continuum
claim.

## Declared finite object

Start with the sixteen binary corners of the unit four-cube. A candidate piece is
a five-corner simplex whose four edge vectors from its first corner have
determinant of absolute value one. Keep the candidates at the minimum declared
adjacency cost. A cutting is a set of kept pieces with pairwise disjoint interiors
that fills the cell. A cover is an eight-piece set that meets every cutting once.

The runner rebuilds the object from those definitions. It obtains `2,672`
unit-determinant candidates, adjacency-cost floor `6`, `400` candidates at that
floor, `15,800` cuttings of `24` pieces, `192` supported pieces, and `192`
eight-piece covers.

The `5^4 = 625` shifted rational sample points avoid every facet plane, and every
one of the `400` kept pieces contains a sample point. The exact-cover recursion
branches on every kept piece containing the first uncovered point. It then checks
that the output is unique and that every returned mask family is disjoint and
covers all sample points. Exact facet/intersection tests certify every pair that
co-occurs, and twenty-four determinant-one simplices give normalized volume
`24/24`. The cover search is also unique; every cover meets every cutting exactly
once, and the cover-by-piece table has constant row and column sums `8`.

Let `A` be the cutting-by-piece table and `B` the cover-by-piece table. Exact
rational elimination gives:

| table | rank | kernel dimension |
| --- | ---: | ---: |
| `A` | 88 | 104 |
| `B` | 105 | 87 |

The runner binds the Gram identity used for `A`, direct annihilation of both
integer kernel bases, their independent ranks, and direct selected-row rank
controls. These are gates, not report-only diagnostics.

## Field bridge and twenty-block form

The fields have distinct roles. Exact incidence ranks and the advertised rank
ceiling are over `Q`. The exhaustive histogram and explicit small-block
coordinates are over `F_1000003`; `F_1000033` supplies a same-implementation
cross-prime check.

The representation bridge is the following standard finite-group theorem, with
its hypotheses exposed here. Maschke's theorem makes `Q[G]` semisimple. Moreover,
`G` is the signed permutation group `C2 wr S4`. Its rational irreducibles are the
absolutely irreducible bipartition modules constructed by inducing tensor products
of rational Specht modules and the two rational characters of `C2`; hence `Q` is
a splitting field for this action. The double-centralizer decomposition therefore
writes each common simple part as a degree-`d` rational irreducible tensored with
its multiplicity space, and every equivariant map is identity on that irreducible
factor tensored with one multiplicity-space matrix.

The runner does not infer applicability from a name alone. The `104` disjoint
piece-pair orbit matrices are a rational basis of the piece commutant. Exact
commutator elimination gives a `20`-dimensional center, and exact multiplication
by one central element has twenty distinct integer eigenvalues, each simple in
the center. The corresponding central operator is checked against the orbital
representation. This identifies the twenty rational central parts.

Both primes are distinct, do not divide `|G| = 384`, and keep the twenty central
values distinct. On each prime, the runner directly obtains the part dimensions
and the `m`, `mc` multiplicities. Their certified sums are

```text
sum dim = 192,  sum m^2 = 104,  sum m mc = 96,
sum mc^2 = 120,  sum d mc = 192.
```

For distinct values `lambda_i`, the rational central projectors are the Lagrange
polynomials
`e_i = product_(j != i) (Z0-lambda_j I)/(lambda_i-lambda_j)`. Separation modulo
each prime makes every displayed denominator a prime-field unit, so these same
orthogonal projectors reduce without collision. Reduction cannot increase the
rank of the integer orbit-coordinate matrices. The displayed component sums
equal the exact orbit-basis dimensions, leaving no lost dimension to redistribute;
thus the reduced projector, commutant, and cross-map component dimensions recover
the same `d`, `m`, and `mc` as the split rational modules. This is the
computation-specific lift used here. The `96`
cell-orbit indicators are already a rational basis for `Hom_G` because they have
disjoint supports and exhaust its orbits. Their block-coordinate maps have rank
`96` at both primes. Thus the rational tensor form follows from the split-module
theorem and the orbit basis, while the finite-field coordinates are separately
certified at each stated prime.

## Cover-block accounting

For the cover table, eight of the twenty modular small matrices are not full
rank. Each is identified by its zero-based ordinal in increasing central
eigenvalue order, the central eigenvalue, `(d,m,mc,rank,drop)`, and the first
twelve hexadecimal digits of SHA-256 applied to its canonical comma-separated
row-major entries modulo `1,000,003`.

| part | eigenvalue | `d/m/mc/rank/drop` | matrix SHA-256 prefix |
| ---: | ---: | --- | --- |
| 5 | -289 | `2/2/2/1/2` | `ad99991a9949` |
| 7 | -143 | `4/2/3/1/4` | `8a2a064491eb` |
| 8 | -141 | `6/2/3/1/6` | `54a6d07a25bf` |
| 11 | -17 | `8/4/6/3/8` | `5b08ea4b39b9` |
| 12 | 7 | `6/4/3/2/6` | `9c5db65b241e` |
| 13 | 19 | `6/2/3/1/6` | `31e2a61b7a16` |
| 15 | 159 | `6/4/3/2/6` | `6a2e89a5e087` |
| 18 | 635 | `1/1/1/0/1` | `5feceb66ffc8` |

The weighted drops add to `39`. The modular block ranks add to `105`, equal to
the exact rational rank of `B`. Since each modular block rank is no larger than
its corresponding rational block rank and the totals agree, equality holds
part-by-part for this table. The eight displayed losses therefore also account
for the rational cover-table shortfall from the `144` ceiling.

Two blocks are `1` by `1`. In one, the `96` orbit coefficients consist of `48`
plus and `48` minus values, so exactly
`C(48,2) C(48,2) = 1,272,384` binary four-orbit subsets give zero on that block.
In the other, all `96` values have the same sign, so none does. The closed-form
counts agree with the exhaustive enumeration.

## Hamming-weight-four modular census

The enumerated population is exactly the uniformly counted binary
Hamming-weight-four coefficient vectors in the `96`-element cell-orbit basis. It
is not the set of arbitrary covariant tables with unrestricted coefficients.

At `p = 1,000,003`, all `3,321,960` subsets are visited exactly once. The modular
histogram has `79` distinct ranks. Its minimum is `24`; its maximum is `144`, and
`511,872` subsets occupy the maximum bin. Relative to the exact cover reference
rank `105`, the modular counts are:

| modular condition | count |
| --- | ---: |
| rank at most 105 | 106,536 |
| rank exactly 105 | 24,768 |
| rank below 105 | 81,768 |
| rank 24 | 72 |

Gate C36 pins all four values and the partition identity
`106,536 = 24,768 + 81,768`; a corruption of any displayed count fails the run.

The field boundary is directional:

- the modular at-most-`105` and below-`105` counts are upper bounds on the
  corresponding rational counts;
- the modular exact-`105` count has no one-sided implication for the rational
  exact-`105` count;
- because `24` is the exact rational minimum, the modular rank-`24` bin is an
  upper bound on the rational minimum bin;
- because `144` is the exact rational ceiling, the modular rank-`144` bin is a
  lower bound on the rational maximum bin; and
- `79` is the number of distinct modular ranks and has no one-sided implication
  for the number of distinct rational ranks.

Exact rational elimination gives rank `24` for orbit subset `0/2/12/14`, rank
`144` for `0/1/2/7`, and rank `105` for the cover reference subset `0/1/2/3`.
These certify both extrema and one non-extremal reference point.

The second-prime check uses the same implementation and the already constructed
integer object; it is not an independent implementation. At `1,000,033`, all
twenty blocks pass the same five construction conditions, the coordinate map
again has rank `96`, and ranks agree for `200,000` deterministically selected
subsets. The selection is every sixteenth iterator position among the first
`3.2` million subsets.

## Finite label diagnostics

The even subgroup has order `192`. It gives two `96`-piece classes and two
`96`-cover classes, and every cover meets each piece class four times. Gates
C20-C25 report six additional stabilizer, sign, split-count, and ordered-label
identities. They are diagnostic leaves and carry no inference about an excluded
explanation or unavailable construction.

## Inputs, imports, and provenance

| input | class and provenance | role and sensitivity |
| --- | --- | --- |
| labelled unit four-cube, determinant-one simplex rule, adjacency cost, cutting and cover rules | declared finite-model data in this note and runner | define the theorem object; changing one defines another object |
| shifted `5^4` rational grid | deterministic enumeration device | exact facet, visibility, search-output, disjointness, and volume gates bind its use |
| full coordinate permutations and independent flips | declared finite action | defines `G`; it is not imported from the framework's proper-cubic covariance |
| Maschke, rational bipartition modules for `C2 wr S4`, and double centralizer | standard finite representation theorem | load-bearing rational field bridge; hypotheses and use are stated above |
| primes `1,000,003` and `1,000,033` | insensitive computational nuisances | first supplies the histogram; second is a same-code cross-prime check |
| deterministic central and pure-vector coefficients | insensitive computational nuisances | carry no selector meaning; success and dimension conditions are gated |
| LCG seed `3` and sixty four-subsets | insensitive computational nuisance | direct-versus-reduced rank spot checks only |
| deterministic stride sample of `200,000` subsets | insensitive computational nuisance | same-code second-prime comparison only; selection rule disclosed above |
| uniform counting on binary Hamming-weight-four vectors | explicit finite counting measure | defines the census population and no wider probability law |
| Python exact integers/fractions and NumPy integer arrays | implementation substrate | no floating point enters a gate; bounds keep products inside signed 64-bit range |
| exact cover rank and all prior finite-object counts | recomputed here | no earlier campaign artifact or open pull request is imported |
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | framework boundary authority only | distinguishes proper-cubic/Record scope; contributes no theorem premise |
| piece-to-Record map, dynamics, continuum, observation, fitted value | absent/support-only | outside this target |

The primitive-registry check returns an empty premise dependency set for the
finite target. The runner declares no external input path because it reads no
scientific data file; its own source bytes are bound by the canonical cache.

## Proof-obligation graph

The target closes through this acyclic graph:

1. P0 defines the corners, determinant/cost rule, cutting/cover rule, fields,
   matrix orientations, counting measure, and the full `384`-map action.
2. P1, depending on P0, enumerates the candidates and binds facet avoidance,
   visibility of every kept piece, exact-cover output, disjointness, and volume.
3. P2, depending on P1, reconstructs the unique regular cover table and exact
   rational cutting/cover ranks with Gram, kernel, and direct-rank controls.
4. P3, depending on P1-P2, constructs `G`, checks closure and incidence
   equivariance, and enumerates the `104/120/96` orbit bases.
5. P4, depending on P3, computes the exact rational commutant center and a
   separating central element.
6. P5, depending on P3-P4 and the declared split-module theorem, establishes the
   rational twenty-part tensor form; the rank-sum and separated-value checks bind
   its reduction at both primes.
7. P6, depending on P5, constructs the twenty small matrices and proves both
   prime-field coefficient maps have rank `96`.
8. P7, depending on P2 and P6, identifies the eight cover blocks and proves their
   weighted drops sum to `39`, with stable ordinal/eigenvalue/hash identities.
9. P8, depending on P6, exhausts all binary Hamming-weight-four subsets and pins
   the modular histogram counts; same-code second-prime checks are controls.
10. P9, depending on P5 and P8, combines the rational ceiling with exact rational
    witnesses to prove minimum `24` and maximum `144` for the finite binary family.
11. P7-P9 discharge the field-qualified target. The finite label diagnostics are
    leaves and have no load-bearing edge.

## Degenerate and boundary-case ledger

- Determinant-zero and non-cost-floor simplices lie outside the declared object.
- Facet contacts between pieces are permitted; sample points avoid facets, while
  exact pair tests certify that co-occurring interiors do not overlap.
- Empty search or census families are excluded by the exact positive cardinality
  gates and `C(96,4)` enumeration total.
- Five parts have `mc = 0`; the implementation represents their cover block by
  `None` and gates their count. They contribute zero cover rank.
- One active `1` by `1` cover block is the zero matrix and is included in the
  eight-drop table.
- The primes are distinct, do not divide `384`, and preserve all twenty central
  eigenvalues; a bad-characteristic or collided-value calculation is outside the
  claim and fails the stated gates.
- Modular rank may fall below rational rank. Every inference from the histogram
  uses only the directions listed above.
- Arbitrary field coefficients, other Hamming weights, smaller symmetry groups,
  multicell geometries, physical readings, and continuum limits are outside the
  target rather than counterexamples to it.

## Runner and review record

The runner has `43` fail-closed gates and declares `AUDIT_TIMEOUT_SEC = 900`.
It checks a `2,500 MB` peak-resident budget, source hygiene, and a pre-trailer
stdout character count. Any failed gate increments the final `FAIL` count and
causes a nonzero process exit. The canonical cache binds the source hash, timeout,
exit status, stdout, and stderr.

The first combined review independently rebuilt the full second-prime census,
recomputed the three exact rational ranks, and reproduced the finite rank core.
It then required twelve repairs. This revision:

- binds all object/tiling and Gram/kernel/direct-rank certificates;
- makes every displayed census count fail closed;
- states the rational split-module and finite-field bridge explicitly;
- keeps six label checks as positive diagnostics rather than negative claims;
- adds the complete trace/status/import/proof/boundary contract;
- removes campaign ancestry as scientific authority;
- adds canonical harness routing and requires integrated-tree manifest generation;
- gates all second-prime construction flags and coordinate rank while accurately
  calling the path same-implementation and partial-domain;
- names the exact Hamming-weight-four population and counting measure;
- identifies every drop by ordinal, eigenvalue, and stable matrix hash; and
- labels stdout accounting as pre-trailer.

This record is review provenance, not an audit verdict. Effective retained status
still requires the repository's separate audit process.
