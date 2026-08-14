# Exact incidence shadow and unseen exchanges — Cycle 754

Date: 2026-08-09 (revised 2026-08-14 by review-loop)

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [exact incidence-shadow runner](../scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_2026_08_09.py)

Independent checker:

- [SymPy/modular incidence-shadow checker](../scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_independent_check_2026_08_09.py)

Both executables are co-load-bearing. The checker imports no Cycle 754
primary symbols. It live-replays the current Cycle 753 helper, then uses an
exact SymPy nullspace, modular-rank witnesses, different modular exchange
signatures, direct integer comparisons, and SHA-512 buckets with exact
collision confirmation. An audit packet for this note is incomplete without
the checker.

Direct scientific dependency:

- [Cycle 753 forced-mean identity and finite multiplicity rankings](PHYSICAL_CELL_CUTTING_SHARED_COUNT_VARIANCE_LAW_CYCLE753_NOTE_2026-08-09.md)

Both Cycle 754 executables authenticate the current Cycle 753 primary and
independent receipts, including their source and declared-input hashes.

Scope: an exact theorem about one supplied finite `15,800`-by-`192` incidence
object. This package changes no axiom, framework Admissibility rule, primitive,
policy, or audit status. It adds no physical charge, causal, probability,
multicell, or continuum interpretation.

```text
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_shadow_rank_unseen_swap_cycle754_note_2026-08-09
target_blocker_text: determine what the cutting-multiplicity vector can distinguish and test the proposed spectral and full-rank routes
source_of_blocker_text: Cycle 753 finite multiplicity-ranking boundary
reachability_to_target: exact algebra plus exhaustive finite computation on the supplied coordinate four-cube
artifact_role: bounded finite incidence theorem candidate
next_trace_action: independent audit of the landed primary and helper evidence
conditional_surface_status: direct Cycle 753 dependency remains subject to independent audit
hypothetical_axiom_status: none
admitted_observation_status: none
claim_type_reason: exact finite rank, kernel, exchange, and multiplicity-collision results without a physical or multicell lift
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_shadow_rank_unseen_swap_cycle754_independent_check_2026_08_09.py
```

## Exact target

For the supplied incidence matrix `I`, determine its rational and binary
ranks, exhibit and verify its rational kernel, find the smallest
equal-cardinality `{−1,0,1}` exchange that is invisible to every row, and
measure how many multiplicity vectors remain on the landed minimum-carrier and
induced-`Q_4` populations. Test only two proposed proof routes: a
minimum-eigenvalue lower bound for the Cycle 753 pair total, and a
full-column-rank uniqueness argument for the equation `I x = 2·1`.

The target does not decide whether a `0/1`, weight-16 solution to that equation
exists. It does not exclude another spectral, integer-programming, coding, or
combinatorial lower-bound route. It does not claim that arbitrary invariants of
the labeled pairwise co-incidence matrix factor through a multiplicity vector.

## The exact shadow

The incidence matrix has `15,800` rows and `192` columns. Every row has weight
`24`, every column has weight `1,975`, and all columns are distinct. Its exact
rational rank is `88`, so its kernel has dimension `104`.

The primary obtains a free-column basis by exact rational RREF and verifies all
`104` vectors against `I` in exact integers. The helper independently obtains
an exact SymPy nullspace and supplies rank-`88` lower witnesses modulo two
different primes. Thus the explicit `104`-dimensional kernel and the modular
minor witnesses close both rank inequalities without floating-point rank
estimation.

Every kernel vector is balanced. The sum of all rows is `1,975` times the
all-ones row because every column has that weight. The all-ones row therefore
lies in the row span, so every vector orthogonal to the row span has coordinate
sum zero.

The particular free-column basis produced by both exact eliminations has
entries in `{−1,0,1}` and support histogram

| support | 8 | 12 | 14 | 16 | 18 | 20 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| vectors | 38 | 30 | 14 | 13 | 3 | 6 |

This histogram is a property of that reported basis, not a basis-independent
invariant of the kernel.

## What the two proposed routes actually show

The Cycle 753 shared-cutting total is a positive-semidefinite Gram quadratic
form. The proposed minimum-eigenvalue/Rayleigh route gives no improvement over
the universal `15,800` baseline: the balanced subspace contains the
`104`-dimensional kernel, so the least eigenvalue on that subspace is zero.
This is a failure of that route only. No claim is made that a different
spectral or combinatorial bound cannot explain the observed carrier minimum
`19,640`.

Likewise, full column rank would have made the rational solution of
`I x = 2·1` unique. Rank `88` instead leaves a `104`-dimensional affine
rational solution space. That invalidates the full-rank uniqueness argument;
it neither constructs nor excludes a `0/1`, weight-16 two-cover.

## The first equal-cardinality exchange is four for four

A `{−1,0,1}` kernel vector is balanced, so its positive and negative supports
are disjoint sets of equal cardinality met equally often by every cutting.
Call such a pair an exchange.

| exchange | result | load-bearing check |
| --- | --- | --- |
| one for one | absent | all `192` columns are distinct |
| two for two | absent | exact signature injectivity over all `18,336` pairs |
| three for three | absent | exact signature injectivity over all `1,161,280` triples |
| four for four | present | `{4,5,10,11}` versus `{1,3,7,9}` checked row by row |

The proof routes must not be conflated. Nonzero exact Gram determinants for
every two- and three-column subset prove that no arbitrary linear dependence
has support at most three. A two-for-two exchange can have support four and a
three-for-three exchange can have support six, so those determinant checks do
not prove the corresponding exchange rows.

The exchange exclusions are carried by exhaustive necessary-signature
sweeps. The primary weights all cutting rows by three exact integer moments;
the helper instead uses three fixed modular weight streams and exactly compares
every signature collision. Equal column sums must have equal signatures, so
absence of an exact exchange after complete coverage is decisive. The next
size has the explicit row-by-row witness above, whose orbit under the `384`
verified incidence symmetries has `96` members.

The result is only about equal-cardinality `{−1,0,1}` exchanges. It does not
classify general integer kernel vectors with coefficients outside that set.

## Multiplicity-vector collisions

For a piece set with indicator `x`, its cutting multiplicity vector is `m=Ix`.
The complete `132`-member minimum-carrier population from the landed chain
gives only `108` distinct vectors. The `24` non-singleton classes are all
pairs, and the two carriers in each pair are disjoint. Thus these are exact
sixteen-for-sixteen exchanges realized inside the census, not only abstract
kernel directions.

The complete `59,736` induced-`Q_4` population gives `53,632` distinct
multiplicity vectors. The primary counts SHA-256 keys; the helper uses SHA-512
only as a bucket index and exactly compares every repeated bucket against a
recomputed representative, so a digest collision cannot change the helper's
count.

Any statistic explicitly proved to factor through `m` is constant on these
classes. Examples are the Cycle 753 row-multiplicity histogram, squared spread,
and total

```text
T = sum over rows c of binomial(m_c, 2).
```

No broader statement is made about arbitrary labeled pairwise-co-incidence
invariants.

## Binary shadow

Over `GF(2)`, independent row and column eliminations both give rank `88`.
The binary kernel therefore has dimension `104`; the reachable readings form
an `88`-dimensional image, and each reachable reading has `2^104` preimages.
All eight declared finite reading vectors lie in that image. This is a finite
linear-algebra count, not a probability statement.

## Localizing the universal baseline

For a sixteen-piece set `S`, let

```text
d_p = (number of cuttings shared by p with S minus p) - 1975.
```

Summing over selected pieces counts each selected pair twice, hence

```text
sum over p in S of d_p = 2 (T(S) - 15800).
```

Cycle 753 supplies the stronger universal identity

```text
T(S) = 15800 + (1/2) sum over rows c of (m_c - 2)^2.
```

Consequently `T(S)=15,800` iff every row has multiplicity two. In that case
each selected piece meets exactly one other selected piece on each of its
`1,975` rows, so every `d_p=0`. Conversely, if every `d_p=0`, the displayed
local sum gives `T(S)=15,800`. This is the licensed equivalence; the local sum
identity by itself would not prove the forward implication.

The `15,800` number is the universal sixteen-set baseline, not the applicable
four-reading parity floor. Cycle 753's direct parity floor for a carrier of the
declared four reading is `18,632`. Across the complete `132` minimum carriers,
both implementations agree on every local vector, none reaches the universal
baseline, and the smallest observed total remains `19,640`. Nothing here shows
that `19,640` is forced outside that complete minimum-carrier population.

## Proof-obligation graph

1. Current Cycle 753 primary and helper receipts bind the complete finite
   incidence, carrier, induced-`Q_4`, forced-mean, and parity-floor boundary.
2. The Cycle 754 primary rebuilds the object and computes exact rational and
   binary shadows; the helper live-replays the independent predecessor object
   and uses different elimination and signature routes.
3. Exact kernel vectors plus two modular rank witnesses establish rational
   rank `88`; separate packed row and column eliminations establish binary rank
   `88`.
4. Complete pair/triple signature sweeps exclude exchanges through size three;
   a direct row comparison supplies the size-four witness.
5. Both implementations rederive carrier and induced-`Q_4` collision counts,
   with exact confirmation of helper digest collisions.
6. Cycle 753's universal spread identity and the locally rechecked pair sums
   establish the precisely scoped baseline equivalence.
7. Source/input-bound receipts, zero-exit hostile mutations, and independent
   helper contracts close the process obligations.

There is no unresolved leaf in this finite theorem. Integer feasibility of a
weight-16 two-cover, a stronger lower bound, basis-independent kernel
classification, and any physical or multicell interpretation remain open.

## No-Go Discipline Gate

The negative claims are narrow: exchanges of sizes one through three are
absent on this finite matrix, and two named linear proof routes fail. No
universal no-go is asserted.

### N1 — alternative routes

1. **ATTEMPTED — direct column route.** Bytewise comparison of all `192`
   incidence columns closes the one-for-one case.
2. **ATTEMPTED — exact moment-signature route.** The primary exhausts every
   pair and triple under three integer row moments; injectivity excludes the
   corresponding equal-cardinality exchanges.
3. **ATTEMPTED — independent modular-signature route.** The helper changes the
   weights and arithmetic, covers the same subsets, and exactly compares every
   modular collision.
4. **ATTEMPTED — small-support linear route.** Exact Gram minors exclude all
   dependencies on at most three columns. This is retained as a separate
   boundary and is not misused as a proof about four- or six-column exchanges.
5. **ATTEMPTED — next-boundary construction.** The explicit four-for-four
   vector is checked against all `15,800` rows and under the full symmetry
   group, showing the preceding exclusions stop at the claimed boundary.
6. **ATTEMPTED — rank/nullspace route.** Exact rational and modular
   calculations establish the balanced `104`-dimensional kernel, which
   directly falsifies only the minimum-eigenvalue and full-rank proposals.

These families differ in object or terminal obligation: column equality,
equal-set signatures, independent modular collision checking, arbitrary
small-support dependence, explicit construction, and global nullspace.

### N2 — wall independence

No multiple walls or admissions are claimed. Exchange minimality is a finite
classification with separate size obligations. The failed Rayleigh and
full-rank routes are independent proposals and neither is presented as closing
the other or the wider lower-bound/two-cover questions.

### N3 — hidden-wall scan

The supplied coordinate object, support ordering, symmetry permutations, and
eight reading vectors are named finite inputs. “By construction” is used only
for explicit matrix products or exhaustive set enumerations. No standard,
canonical, background, framework-provided, or primitive language supplies an
unstated premise.

### N4 — residual matching

| cited source | residual established there | residual used here | match |
| --- | --- | --- | --- |
| [Cycle 753](PHYSICAL_CELL_CUTTING_SHARED_COUNT_VARIANCE_LAW_CYCLE753_NOTE_2026-08-09.md) | complete finite populations, forced-mean identity, four-reading floor `18,632`, observed minimum `19,640` | localization equivalence and exact population boundary | yes |

Cycle 753 is not cited as evidence for rank `88`, exchange minimality, or the
new collision counts; both Cycle 754 implementations compute those results.

### N5 — rhetoric and resolution

- `per_element`: all `192` piece columns enter the exact shadow and exchange
  checks;
- `per_site`: one supplied coordinate four-cube only; no site family tested;
- `per_mode`: no modal decomposition exists for this finite binary object;
- `per_block`: every one of `15,800` cutting rows enters the rank, witness,
  and collision computations;
- `lattice_wide`: no multicell, infinite-lattice, causal, or continuum claim
  is tested.

Both canonical caches must carry the corresponding five-line execution
certificate.

### N6 — partial closure and primitive scan

No new axiom or framework primitive is proposed or needed. A convention cannot
turn rational affine freedom into a `0/1`, weight-16 solution or derive a
stronger lower bound. Those are explicit finite mathematical obligations, not
labeling walls.

### N7 — steelman

A hostile reviewer should reject any broader no-go: singularity of the Gram
matrix does not prevent a useful bound after imposing `0/1`, weight, parity,
reading, orbit, or support constraints, and affine rational freedom says
nothing decisive about integer feasibility. The exact actionable continuation
is an integer-feasibility or symmetry-reduced search for `I x=2·1`, together
with lower bounds on the constrained balanced complement. This steelman is why
the note claims only failure of the two named unconstrained linear routes.

### N8 — cross-cycle echo

Cycle 753 initially risked broadening a failed descending odd-count ranking
into a dismissal of odd-support information; review found that equality to
`5,664` classifies the same `60` carriers and narrowed the negative. The same
repair mechanism is applied here: rank deficiency invalidates two proposed
routes but is not promoted into a general spectral or feasibility no-go.

N1-N8 status: **PASS for the narrowed finite claims.**

## Evidence boundary

The primary and helper are fail-closed and write canonical source/input-bound
receipts. Their caches include the N5 execution certificate. The exact rank,
kernel, exchange, and collision results remain proposed for independent audit;
this review changes no audit verdict.
