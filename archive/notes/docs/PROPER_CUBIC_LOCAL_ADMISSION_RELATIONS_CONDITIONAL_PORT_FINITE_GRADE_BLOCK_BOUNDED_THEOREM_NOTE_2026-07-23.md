# Proper-cubic local admission relations, conditional port, and finite grade block

**Date:** 2026-07-23

**Claim type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Runner:** [`scripts/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_2026_07_23.py`](../scripts/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_2026_07_23.py)

**Receipt:** [`outputs/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_receipt_2026_07_23.json`](../outputs/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_receipt_2026_07_23.json)

**Runner cache:** [`logs/runner-cache/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_2026_07_23.txt`](../logs/runner-cache/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_2026_07_23.txt)

## Controlled claim

This note records three finite statements, all conditional on the supplied
structures listed below.

1. The five displayed radius-one Boolean relations on a six-direction word are
   total, nonconstant, invariant under all 24 proper-cubic frames, and pairwise
   extensionally distinct on the exhaustive 64-word domain.
2. If `unique_quorum` is supplied as the candidate admission relation, its
   Boolean answer feeds the displayed lane-zero conditional port equations.
   A separately supplied finite LOCK/readout generator algebra preserves the
   emitted payload under every finite word of that declared algebra.
3. If the displayed endpoint-to-count calibration and 4x4x4 address chart are
   supplied, the finite grade block produces one exact denominator-64 grade
   vector for each endpoint word, covariantly over all 24 frames.

The first statement is a positive finite-model theorem: it exhibits five
models of the declared schema. Physical formation or selection is outside the
theorem scope.

## Five explicit relations

Let `w` be a six-bit word ordered only for storage by the geometric labels
`(+x,-x,+y,-y,+z,-z)`. The laws depend solely on Hamming weight, so the storage
order is not a preferred incident ordering. With `fresh` Boolean, define

```text
A_S(w,fresh) = fresh AND [weight(w) in S].
```

The supplied shell sets and exhaustive census are:

| relation | accepted shells `S` | accepted /64 | train `weight<=3` | held `weight>=4` |
|---|---:|---:|---:|---:|
| `unique_quorum` | `(1,)` | 6 | 6 | 0 |
| `odd_shells` | `(1,3,5)` | 32 | 26 | 6 |
| `nonempty` | `(1,2,3,4,5,6)` | 63 | 41 | 22 |
| `low_density` | `(1,2)` | 21 | 21 | 0 |
| `even_nonzero` | `(2,4,6)` | 31 | 15 | 16 |

The runner exhausts all ten unordered pairs and emits at least one truth-table
separator for each. It also checks all `5*64*24 = 7,680` frame relations and
the all-false freshness branch. Uniformly applying one of these functions at
each site is translation homogeneous. The static shell set is the supplied
rule definition; no site-dependent, state-dependent, or host-selected rule
service is modeled.

These five relations are finite witnesses, not five claims about nature.

## Unique-quorum conditional port candidate

For `occ = [weight(w)=1]`, the finite port is

```text
archive6  = w
losers6   = w XOR one_hot(unique winner), if occ=1; otherwise w
ready     = 1-occ
spent     = occ
edge      = occ
member5   = (occ,0,0,0,0)
receipt5  = (occ,0,0,0,0)
snapshot12= (occ,occ,occ,0,0,0,0,0,0,0,0,0)
```

The reconstructed finite lane-zero equations are

```text
occurrence = edge AND member5[0] AND receipt5[0]
precommit  = snapshot12[0]
occurrence = snapshot12[1]
atom_flag  = snapshot12[2]
```

with the remaining nine snapshot fields zero. The archive makes the finite map
injective on its declared domain. Every collision loser is retained. The runner
checks the equations, inverse provenance, malformed-domain refusals,
field-presence witnesses, all 64 input words, and all `64*24 = 1,536` rotated
ports.

This is a candidate conditional tuple. The supplied choice of
`unique_quorum`, lane-zero binding, blank rails, and ready token is not
derived. The construction derives neither actuality nor an identification of
the tuple as a framework Record.

## Finite LOCK/readout preservation candidate

The conditional scalar payload

```text
(edge, member5, receipt5, snapshot12)
```

has 23 bits. The supplied finite generator family consists of:

```text
read_i:       readout_i <- readout_i XOR payload_i
prewrite_i:   payload_i <- payload_i XOR ((1-LOCK) AND transient)
matter-X_d:   matter_d  <- matter_d XOR 1
```

Every generator fixes every payload coordinate and `LOCK` when `LOCK=1`.
Induction therefore proves preservation under every finite composition in
this declared generator monoid. The runner checks all generators and all
ordered generator pairs on the six formed unique-direction ports, both
transient values, inverse application, preformation nontriviality at `LOCK=0`,
continued matter/readout action, and all-24 generator-family closure.

The LOCK genesis and the restriction to this generator monoid are supplied.
This finite preservation result derives neither a framework-Record
identification nor the physical future-operation class. Its proved scope is
finite-word invariance in the displayed monoid; all-future, noisy,
thermodynamic, and infinite-volume permanence are outside that scope.

## Finite denominator-64 grade block candidate

Pair the six endpoints into three axes and define the supplied calibration

```text
n_axis     = endpoint_plus + endpoint_minus in {0,1,2}
count_axis = 2*n_axis in {0,2,4}
p_axis     = count_axis/4 = n_axis/2.
```

For each equally weighted address `(a_x,a_y,a_z)` in `{0,1,2,3}^3`, set three
threshold bits by comparing `a_axis >= count_axis`. Their eight possible
labels give a 512-bit mask: eight labels times 64 addresses. Exactly one label
is marked at each address, hence exactly 64 mask bits are one. Dividing the
eight label counts by 64 gives the grade vector.

The auxiliary proper-cubic action is supplied as follows: a frame permutes the
three unoriented axes, its sign flips act trivially on each four-address axis,
and it permutes the three threshold-label bits by the same unsigned axis
permutation. Thus this auxiliary action factors through the unsigned axis
permutation representation of the 24-frame group.

The runner verifies for all 64 endpoint words that this vector equals the
corresponding exact product-grade arithmetic, sums to one, and equals the
complete-block count vector. It checks all `64*24*65 = 99,840` count/label
covariance comparisons, all 576 frame products on four axis probes, forward
provenance and controlled uncompute with the original endpoint word retained,
malformed inputs, and held sizes 137 and 211.

The load-bearing controls are exact:

- deleting one endpoint changes the grade by L1 residual `1`;
- on the explicit endpoint witness `w=(1,0,1,0,1,0)`, replacing the declared
  counts `(2,2,2)` from `count=2*n` by the counterfactual counts `(1,1,1)`
  from `count=n` changes the grade by L1 residual `11/16`;
- reversing the address order leaves the grade-count vector unchanged but
  separates all 64 address labels on the explicit witness
  `w=(1,0,1,0,0,0)`, whose declared counts are `(2,2,0)`;
- odd external count words and non-complete block sizes are refused.

The calibration, uniform address weighting, address chart, label convention,
complete-block rule, auxiliary frame action, and finite noiseless Boolean
operations are supplied candidate structure. The construction derives no
physical state, apparatus, menu, outcome, corpus, probability interpretation,
Born calibration, or realized-history identification.

## Supplied / derived / scope inventory

Supplied:

- six geometric directed-neighbor labels and opposite pairing;
- the five accepted-shell sets, Boolean freshness, and uniform tiling;
- identification of unique quorum as the conditional-port candidate;
- lane-zero member/receipt adapter, blank fields, ready token, LOCK genesis,
  transient/readout rails, finite generator list, and trivial proper-cubic
  action on scalar payload/readout lanes;
- endpoint-to-count calibration, equally weighted 4x4x4 address chart,
  eight-label convention, complete-block rule, unsigned-axis/sign-trivial
  auxiliary proper-cubic action, original endpoint word retained for
  controlled uncompute, and finite noiseless Boolean operations.

Derived on the declared finite domains:

- the exact five-law census, all ten extensional separators, and all-24
  covariance;
- the 64-word unique-quorum conditional-port equations, injective archive,
  retained losers, inverse provenance, field-presence/domain controls, and
  all-24 covariance;
- finite-composition payload preservation inside the supplied LOCK/readout
  generator monoid;
- the 27 reachable even-count words, exact denominator-64 grade/product
  identity, held-input controlled uncompute, deletion, held-size,
  address-order, and all-24/all-576 controls.

Not derived by this finite construction:

- a physical formation/admission dynamics selecting one extensional law;
- objective actuality and identification of the conditional tuple as a
  framework Record;
- derivation of LOCK genesis and the physical class of future operations;
- derivation of the endpoint-to-grade calibration;
- a physical apparatus/menu/outcome and objective corpus law;
- probability meaning, Born calibration, independence, convergence, and held
  non-complete sizes without a supplied order;
- a physical M2 compiler, resource bounds, noise, renewal, scaling, and
  infinite-volume control.

## Interpretation boundaries

The finite port supplies no framework-Record identification and derives no
actuality. The finite LOCK construction proves only invariance within the
declared generator monoid. The finite grade supplies no probability or Born
calibration. The 64-address mask supplies no objective-corpus or
realized-history identification. Normalization alone is not used as a
probability bridge. No generator is called a rate, no phase is called energy,
and no resource rail is assigned stress, source, or gravity meaning.

The theorem scope is exactly the three positive finite statements in the
controlled claim. A physical-M2 compiler and physical law-selection result are
not derived. Authority remains `none`; audit remains `unset` for the
independent audit lane.

## Dependency closure and reproducibility

The runner uses only Python standard-library modules. All mathematics above is
defined in the runner itself. It imports no campaign runner, opens no archived
object, invokes no external command, and performs no network access. The
package therefore runs from a clean checkout of current `origin/main` after
adding exactly this note, runner, receipt, and cache.

The receipt records the exact runner and note hashes, full row results,
extensional separators, residuals, malformed controls, supplied-structure
inventory, and dependency-closure inventory. The independent audit lane alone
may set an audit verdict or effective status.
