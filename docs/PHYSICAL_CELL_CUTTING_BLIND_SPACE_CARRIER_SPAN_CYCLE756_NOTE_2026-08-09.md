# Exact-cover differences span the characteristic-zero incidence kernel — Cycle 756

Date: 2026-08-09 (revised 2026-08-15 by review-loop)

Authority: none

Status: proposed_retained

Claim type: bounded_theorem

Constitutional effect: none.

Primary runner:

- [finite-fixture rebuild and gate runner](../scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_2026_08_09.py)

Independent checker:

- [exact-rank and clique-enumeration checker](../scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_independent_check_2026_08_09.py)

Both executables are load-bearing. The primary constructs the supplied finite
incidence fixture. The checker live-runs that construction, then replaces the
primary's modular rank routine and carrier-search recursion with exact
characteristic-zero domain-matrix elimination and NetworkX maximal-clique
enumeration. The checker therefore shares the declared fixture construction
while supplying implementation-disjoint checks of the rank and exact-cover
claims. Its receipt is written to
`outputs/physical_cell_cutting_blind_space_carrier_span_cycle756_independent_check_2026_08_09_receipt_2026-08-09.json`.

```text
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: independent audit of the supplied finite-fixture theorem and both runner surfaces
conditional_surface_status: exact finite theorem conditional on the supplied coordinate four-cube and cost-rule fixture
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: exact characteristic-zero linear algebra and finite incidence identities for one explicitly supplied fixture
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_independent_check_2026_08_09.py
```

## Supplied fixture and coefficient scope

The supplied finite fixture is defined by the runner, rather than derived from
the framework baseline. Its vertices are `{0,1}^4`. Its candidate pieces are
five-vertex subsets with determinant magnitude one. For a piece, the supplied
cost counts vertex pairs whose four-coordinate Manhattan distance exceeds one;
the fixture retains pieces at the minimum of that cost. A deterministic
interior-point exact-cover construction then produces the finite row family.

These coordinate, determinant, cost and selection choices are the premises of
this bounded theorem. They are not a physical-cell identification. The
framework memo `MINIMAL_AXIOMS_2026-06-29.md` is administrative context only
and supplies none of those choices, so it is deliberately not a citation-graph
dependency.

The incidence matrix and carrier vectors are integral. Ranks, spans and kernels
in the theorem are taken over `Q`; scalar extension gives the same dimensions
and equality over `R`. The support-eight statements below concern explicitly
constructed signed integer vectors. Literature inputs, empirical data, fitted
parameters and external repository data play zero role. NumPy, SymPy and
NetworkX are implementation dependencies rather than scientific premises.

## Exact target and proof obligations

**Target.** For the supplied finite incidence matrix, prove that its kernel over
`Q` is exactly the span of differences of the 192 eight-piece exact covers.

The obligation graph is:

1. **Fixture integrity — proved here.** Rebuild the candidate pieces and rows;
   verify every exact integer unimodular inverse in both multiplication orders, the
   interior-point encoder's collision count, and the incidence census.
2. **Exact-cover family — proved here.** Enumerate all eight-piece sets whose
   columns never co-occur in a row, and verify that each meets every row once.
   The helper repeats the family search with a maximal-clique algorithm.
3. **Characteristic-zero dimensions — proved here.** Compute ranks with two
   prime-field eliminations, independently compute exact ranks in the helper,
   and use containment plus the dimension squeeze below.
4. **Overlap-class spans — proved here.** Partition carrier pairs by their
   overlap and verify that every populated class of differences has exact span
   dimension 104.
5. **Boundary — explicit here.** The strongest open structural target is an
   analytic derivation of carrier rank 105 from the supplied fixture. Support
   minima, classification of support-eight kernel vectors, physical
   interpretation and lattice-wide extension are outside this claim.

## The finite incidence object

The rebuild gives 15,800 rows and 192 columns. Every row contains 24 columns,
every column occurs in 1,975 rows, and both incidence totals equal 379,200.
Call this integer matrix `A`.

The zero-cooccurrence graph on the 192 columns has exactly 192 maximal cliques
of size eight. Writing their indicator rows as a matrix `W`, direct
multiplication gives

`A W^T = 1`,

where the right-hand side is the 15,800-by-192 all-ones matrix. Thus every row
of `W` is an exact cover of the row family and every difference of two rows of
`W` lies in `ker_Q(A)`.

The 18,336 unordered carrier pairs have overlap profile

`0:15072, 1:1920, 2:960, 3:0, 4:384`.

In particular, the 384 overlap-four pairs produce signed integer kernel vectors
with exactly eight nonzero coordinates. This is an existence statement about
those constructed vectors; support minima and support-eight classification are
outside the target above.

## Exact span theorem

The primary computes ranks over the prime fields with moduli `33,554,393` and
`1,000,003`. Both computations give

`rank(W) = 105`, and `rank(A) = 88`.

The two moduli are robustness checks through the same elimination routine, not
independent implementations. The characteristic-zero argument uses the standard
inequality `rank_Q(M) >= rank_Fp(M mod p)` together with containment.

Fix one carrier `w_0` and let

`D = span_Q{w_i - w_0}`.

Every incidence row evaluates each carrier to one and every vector in `D` to
zero. Hence `w_0` lies outside `D`, while `span(W) = D + span{w_0}`. The
prime-field carrier rank therefore gives `dim(D) >= 104`. Since `D` is
contained in `ker_Q(A)` and the prime-field incidence rank gives
`dim ker_Q(A) <= 192 - 88 = 104`, equality holds throughout:

`D = ker_Q(A)`, `dim(D) = 104`, and `rank_Q(A) = 88`.

The helper independently obtains exact characteristic-zero ranks 105, 88 and
104 using domain-matrix elimination. It also computes exact rank 104 for the
difference family in each overlap class `0`, `1`, `2` and `4`. Consequently,
each populated overlap class by itself spans the same 104-dimensional kernel.

## What the executables gate

The primary gates:

- exact unimodular inverses, a collision-free interior-point encoding, and the
  precisely named 48-element subgroup made from 24 proper spatial cubic
  rotations times an optional fourth-coordinate reflection;
- the row/column incidence census and the 192 exact covers;
- the carrier overlap profile and 384 constructed support-eight kernel vectors;
- both prime-field ranks, the characteristic-zero dimension squeeze, and the
  rank of every overlap-class difference family;
- a single 900-second runtime contract, a portable 2,500 MiB memory contract,
  complete-output accounting, and fail-closed process status.

The helper gates exact domain-matrix ranks, independent maximal-clique
enumeration, direct carrier/kernel multiplication, exact overlap-class ranks,
source/input hashes, and hostile receipt mutations. Current gate counts,
elapsed resources and complete stdout are carried by the canonical caches.

## Review record and landing conditions

Review-loop narrowed the original package to the proved characteristic-zero
span theorem and positive finite observations. It withdrew the support-minimum
theorem, failed-route rhetoric and carrier-floor exclusivity; removed the
unbound hand-authored PASS receipt and duplicate raw stdout; classified the
finite fixture explicitly; corrected the group name; and added the exact
implementation-disjoint checker.

Hard landing conditions:

1. the claim-scoped helper mapping for
   `physical_cell_cutting_blind_space_carrier_span_cycle756_note_2026-08-09`
   must name
   `scripts/physical_cell_cutting_blind_space_carrier_span_cycle756_independent_check_2026_08_09.py`;
2. both canonical runner caches and the helper receipt must match the landed
   source/input bytes;
3. the citation-graph manifest must be regenerated from the final integrated
   tree, with this source node carrying zero scientific dependency edges; and
4. independent audit remains the only path that can ratify an audit status.

The current package proposes bounded finite support for independent audit. It
leaves axioms, framework primitives, policy and audit verdicts unchanged.
