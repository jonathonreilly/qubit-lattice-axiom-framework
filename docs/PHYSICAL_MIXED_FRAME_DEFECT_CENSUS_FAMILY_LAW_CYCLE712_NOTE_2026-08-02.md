# Finite family census for the mixed-frame assembly defect — Cycle 712

**Date:** 2026-08-02 (review-loop repair 2026-08-11)

**Type:** bounded_theorem

**Status:** proposed_retained

**Primary runner:**
[`physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02.py`](../scripts/physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02.py)

**Independent checker:**
[`physical_mixed_frame_defect_census_family_law_cycle712_independent_check_2026_08_02.py`](../scripts/physical_mixed_frame_defect_census_family_law_cycle712_independent_check_2026_08_02.py)

**Receipt:**
[`physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02_receipt_2026-08-02.json)

## Claim boundary

For the supplied open-box compiler and the declared numerical classifier, a
complete scan of the 18 mixed proper cubic frames at
`L ∈ {3, 4, 5, 6, 7}` gives twelve signed numerical families. Their counts are
exact integers and equal the six stated polynomial evaluations at all five
sizes. At the three descriptor-extraction sizes `L ∈ {4, 5, 6}`, each
template's base-site set has a unique six-neighbor connected-component
decomposition into full product boxes; the normalized component descriptors
are frame-independent and size-independent on those three sizes. Descriptors
extracted there predict the held-out `L=3` and `L=7` counts exactly.

This is a bounded finite computation conditional on the compiler and classifier
choices below. Only the magnitude-4 swap family has an upstream exact stencil
derivation. Proximity of the other three family centers to
`2`, `2√2`, and `2√3` is numerical finite-difference evidence, not an exact
surd theorem.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: physical_minus_branch_response_floor_assembly_defect_law_cycle709_note_2026-08-02
target_blocker_text: "replace the finite response-floor measurements with a family-resolved size-scaling law"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive the per-family stencil values and propagate the finite family counts through the response solve"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite integer counts and component-box factorizations for five supplied open-box compiler instances, with non-4 surd-center interpretations kept numerical"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_mixed_frame_defect_census_family_law_cycle712_independent_check_2026_08_02.py
```

## Exact target and proof obligations

The exact target is: for the declared compiler, frame set, five sizes,
large-entry threshold, reference-center tolerance, and pair cuts, prove by
complete finite enumeration that every classified entry belongs to one of the
twelve signed families and that each per-sign family count equals the stated
integer polynomial evaluation.

| obligation | disposition |
|---|---|
| Produce the open-box static Hessian and the 24 proper-frame table. | Supplied by the compiler and frame-table imports below; not derived here. |
| Define the transported defect `E_g = Π_g^T Q Π_g − Q` on the bounding-box relabeling. | Imported from the Cycle-710 definition and independently reconstructed by both runners. |
| Show that the four numerical center bins and three pair classes are separated on the scanned data. | Closed by the complete scan: maximum center deviation `6.1×10⁻⁸`, second-center distance at least `5.4×10⁻¹`, and explicit pair-cut margins. |
| Show frame-uniform family counts and equal plus/minus cardinalities. | Closed by exact integer comparison over all 18 mixed frames and five sizes. No canonical sign-reversing map is claimed. |
| Factor each extraction-size template site set into product boxes without a decomposition choice. | Closed at `L=4,5,6` by unique six-neighbor components followed by exact equality with each component's bounding product box. |
| Convert the component descriptors to the six count expressions and test the held-out sizes. | Closed as finite integer arithmetic; `L=3` and `L=7` are not used to extract descriptors. |
| Identify every non-4 center as an exact surd and prove the laws for arbitrary `L`. | Open. These stronger statements are outside the target. |

**Proof-obligation disposition:** `CONDITIONAL`. The finite enumeration and
integer arithmetic close their stated target, conditional on the supplied
compiler and declared classifier. The exact non-4 stencil values and any
all-`L` extension remain open and are not target-equivalent missing lemmas for
the bounded finite claim.

## Imports and declared choices

### Load-bearing scientific and executable inputs

- The Cycle-710 defect definition and covariance boundary:
  [`PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md`](PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md).
- The Cycle-711 exact magnitude-4 stencil result and measured census anchors:
  [`PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02.md`](PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02.md).
- The supplied Cycle-696 compiler:
  [`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
  including its open-boundary simplex assembly, spatial classes, `LT=2`, and
  central finite-difference step `10⁻⁴`. The compiler contains additional
  declared modeling choices and conditional surfaces; this note consumes its
  static Hessian as a supplied finite object and makes no claim that the
  compiler is a derived gravity law.
- The proper cubic frame table and Regge support machinery imported transitively
  by Cycle 696, whose source-facing frame authority is
  [`FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md`](FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md).

The Cycle-710 and Cycle-711 rows remain subject to independent audit. Until
their dependency chain is retained-grade, this result is bounded conditional
support rather than a chain-satisfying authority. Cycle 710 proves its exact
cocycle only on the constant-sign sextet at `L={3,7}`; this note imports the
same finite transport definition for a census of the 18 mixed-frame
comparators and does not extend that cocycle or physical-covariance claim.

### Declared analysis choices

- sizes `L={3,4,5,6,7}`, with descriptor extraction restricted to
  `L={4,5,6}`;
- large-entry threshold `|E|>1.5` and Cycle-711 rounded-census cut `|E|>2`;
- numerical reference centers `{2,2√2,2√3,4}` and center tolerance `2×10⁻⁷`;
- pair cuts `0.5` and `10`, top-family cut `3.9`, center-2 offset window
  `10⁻⁷`, and diagonal perturbation `1.7`.

These are frozen classifier or rejector choices, not values derived from the
four framework axioms. The observed pair-value and center gaps make the family
assignment insensitive to small movements of the stated cuts, but no universal
classifier is claimed.

## Finite numerical family decomposition

Across all five sizes and 18 mixed frames, the complete scan contains 789,120
large entries. Every one lies within `2×10⁻⁷` of one reference center, and the
distance to the second-nearest center is at least `5.4×10⁻¹`. The pair class is
defined by the smaller of
`(|Q[Π_g(i),Π_g(j)]|, |Q[i,j]|)`:

- **swap:** below `0.5`; the observed maximum smaller side is `6.1×10⁻⁸`;
- **wall:** from `0.5` to below `10`; the smaller side lies within
  `5.8570965654 ± 1.2×10⁻¹⁰`;
- **edge:** at least `10`; the smaller side is at least `22`.

The six unsigned labels are center-4 swap, center-`2√3` swap,
center-`2√2` swap, center-`2√2` wall, center-2 swap, and center-2 edge.
Each has positive and negative populations of equal cardinality. “Sign
balance” here means exact equality of finite counts; it does not assert an
unimplemented canonical sign involution.

Only the center-4 swap label inherits an exact value from Cycle 711, where the
stencil is `LT×(−1−1)=−4`. For the other labels, “center-`2√k`” is a numerical
bin name.

## Connected-component product boxes

For each sign, family, frame, and extraction size, entries are first grouped by
the ordered spatial-class pair and the site offset. Each resulting base-site set
is split into its unique six-neighbor connected components. Every component is
then checked to equal its full Cartesian bounding box exactly.

An axis descriptor is either a wall pin `P` or a growing interval `G(s)` of
length `L−s`. After sorting axes and components, the descriptor multiset is the
same for all 18 mixed frames and all three extraction sizes. Per sign, the six
families have respectively `8/8/12/16/20/4` component boxes and
`0/0/0/1/0/2` wall pins per component.

## Finite count identities

Summing component-box cardinalities gives, per sign:

| numerical family | component count expression | counts at `L=3..7` |
|---|---|---|
| center-4 swap | `8(L−1)³` | 64, 216, 512, 1000, 1728 |
| center-`2√3` swap | `8(L−1)³` | 64, 216, 512, 1000, 1728 |
| center-`2√2` swap | `12(L−1)³` | 96, 324, 768, 1500, 2592 |
| center-`2√2` wall | `16(L−1)²` | 64, 144, 256, 400, 576 |
| center-2 swap | `12(L−1)³+8(L−1)²(L−2)` | 128, 468, 1152, 2300, 4032 |
| center-2 edge | `4(L−1)` | 8, 12, 16, 20, 24 |

At every tested size the measured count, descriptor prediction, and stated
expression agree exactly. Evaluating the descriptor expressions and the
written polynomials at `L=3..10` is an algebraic consistency check only; no
compiler measurement beyond `L=7` is claimed.

Rounding combines the center-`2√2` and center-`2√3` labels. The resulting
per-sign buckets are

- rounded `±4`: `8(L−1)³`;
- rounded `±3`: `20(L−1)³+16(L−1)²`;
- rounded `±2`: `12(L−1)³+8(L−1)²(L−2)+4(L−1)`.

Both signs of the center-4 family together contain `16(L−1)³` entries per
mixed frame. These expressions reproduce the Cycle-711 `L=3` and `L=7`
anchors exactly. The center-2 entries sit between `1.7×10⁻⁹` and
`5.7×10⁻⁸` above the cut at 2 on this finite-difference run.

## Measured values and rejectors

The wall entry pair has measured magnitudes
`5.857096565429 / 8.685523719688`; the edge pair has
`22.150846413069 / 24.150846469784`. Their reported spreads are at most
`1.2×10⁻¹⁰`, but no exact stencil evaluation is supplied.

A `1.7` diagonal perturbation of the assembled operator produces two large
entries at least `0.3` away from every reference center. The independent
checker separately reconstructs the transport and classification without
importing the primary, verifies all family counts from raw Hessians, and
demonstrates that a displaced center, a wrong pair cut, and a wrong count
coefficient are rejected.

## Honest boundary

- The result is finite at `L=3..7`; it is not an arbitrary-`L` or continuum
  theorem.
- The non-4 surd-center labels are numerical observations. Exact stencil
  evaluation remains open.
- The component boxes explain the finite position counts. They do not derive
  the incidence cancellations that generate each magnitude.
- No physical gravity, response-floor scaling, or path-symmetrized assembly
  conclusion follows from the census alone.
- The constant-sign sextet and nearby Cycle-707/708 source-stabilizer results
  are provenance context only; they do not seed dependencies for this claim.

## Review record

Review-loop iteration 1 narrowed the submitted “exact surd family law” to the
finite result actually computed. It replaced the depth-capped greedy box split
with unique connected components, changed the unconstructed “sign bijection”
to count balance, added pair-cut margin gates, declared the full transitive
input closure and timeout, and added an independent raw-Hessian checker.

Hard landing conditions:

1. the exact reviewed Cycle-710 and Cycle-711 predecessor commits must be
   contained in remote `main` before this package lands;
2. the citation-graph helper registry must map
   `physical_mixed_frame_defect_census_family_law_cycle712_note_2026-08-02`
   to
   `scripts/physical_mixed_frame_defect_census_family_law_cycle712_independent_check_2026_08_02.py`;
3. both runner caches must be fresh against every declared input;
4. the pipeline-generated ledger/status surfaces must be stripped, while the
   citation-graph manifest acknowledgment co-lands.

This package makes no negative or no-go claim, so the No-Go Discipline battery
is not applicable. Independent audit remains required for the proposed claim.
