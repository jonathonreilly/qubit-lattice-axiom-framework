# Finite frame-orbit spectral measures and Rayleigh census — Cycle 718

**Date:** 2026-08-02 (review-loop repair 2026-08-12)

**Type:** bounded_theorem

**Status:** proposed_retained

**Primary runner:**
[`physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_2026_08_02.py`](../scripts/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_2026_08_02.py)

**Independent checker:**
[`physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_independent_check_2026_08_02.py`](../scripts/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_independent_check_2026_08_02.py)

**Primary cache:**
[`physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_2026_08_02.txt`](../logs/runner-cache/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_2026_08_02.txt)

**Independent cache:**
[`physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_independent_check_2026_08_02.txt`](../logs/runner-cache/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_independent_check_2026_08_02.txt)

**Receipt:**
[`physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_2026_08_02_receipt_2026-08-02.json)

## Claim boundary

For the supplied Cycle-696 open-box static Hessian at `L ∈ {3,4}`, the 24
transported matrices are permutation-similar by construction. The exact finite
frame action fixes the inverse-left conjugator and partitions the frame labels
into four body-diagonal fibres of six. Numerically, transported matrices vary by
at most `1.3×10⁻¹⁰` within a fibre and by at least `4` across fibres.

The Hessian eigenvalues resolve into 66 numerical eigenspaces at `L=3` and 187
at `L=4`, including 32 and 92 doublets. For each of two disclosed deterministic
Gaussian probes at each size, the 24 pulled source vectors are distinct, while
their eigenspace-summed spectral measures agree within each body-diagonal fibre
to at most `3.1×10⁻¹⁰` in `L¹` distance and differ across fibres by at least
`0.675`. Their inverse-Hessian Rayleigh values consequently form four separated
numerical fibre clusters.

For one declared right coset of a regular order-four subgroup, the 24 left
translates collapse to six distinct averaged source vectors. Those vectors are
related by the numerical near-symmetry sextet and have the same eigenspace-summed
spectral measure to at most `2.0×10⁻¹⁰`; their Rayleigh spread is at most
`6.6×10⁻¹¹`. Individual eigenvector weights inside the doublets are
basis-dependent and are not evidence of different spectral content.

The single-slot Rayleigh census is finite: at `L=3`, 98 slots realize 14 of the
15 partitions of four labels and the finest-partition count is zero; at `L=4`,
279 slots realize all 15 and the finest count is 48. The closest resolved pair
gaps are `4.3×10⁻⁵` and `1.8×10⁻⁴`, well above the `10⁻⁸` equality threshold.
No arbitrary-size pattern or source-generic classification is inferred.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: physical_assembly_defect_isospectrality_and_source_pairing_cycle714_note_2026-08-02
target_blocker_text: "derive exact stencil-level sextet invariance and an arbitrary-L incidence theorem, then classify the source subspaces that reduce the four numerical clusters"
source_of_blocker_text: next_trace_action
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive exact spectral projectors for the sextet action and classify which source subspaces share each eigenspace measure without relying on finite numerical clustering"
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
claim_type_reason: "exact finite permutation algebra plus numerical eigenspace, source-orbit, regular-coset, and single-slot measurements at two supplied box sizes"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_independent_check_2026_08_02.py
```

## Exact target and proof obligations

The target is to reconstruct the finite frame action and measure basis-invariant
source spectral weights, inverse-Hessian Rayleigh fibres, and single-slot
partitions at the two declared box sizes.

| obligation | disposition |
|---|---|
| Construct the proper-frame action and identify its composition order. | Closed by exact integer matrices and all `24²` index-array comparisons at each size; the reversed order matches only 120 pairs. |
| Establish permutation similarity and the pairwise conjugator. | Closed for the constructed matrices by exact permutation roundtrip and all 576 inverse-left conjugator comparisons. The reversed product has residual `4`. |
| Separate the numerical body-diagonal fibres. | Closed at `L=3,4`: maximum within-fibre matrix residual `1.3×10⁻¹⁰`, minimum cross-fibre max-entry distance `4`. |
| Define source spectral content independently of an eigenbasis choice. | Closed by summing squared projections over every numerically isolated eigenspace. Internal cluster splitting is below `3.6×10⁻¹⁴`; external gaps exceed `4.6×10⁻³`. |
| Test the spectral-measure fibre claim on independently generated probes. | Closed for the four named deterministic Gaussian probes; both runners reconstruct every measure. Other sources may merge fibres and are outside this target. |
| Explain the selected regular-coset blindness without equating source vectors. | Closed numerically: six normalized sources are separated by at least `0.97`, are explicitly related by sextet pullbacks, and have matching eigenspace measures and Rayleigh values. |
| Classify every single-slot Rayleigh partition at the two sizes. | Closed by full enumeration of 98 and 279 slots with explicit classifier margins. |
| Extend the numerical sextet symmetry, eigenspaces, or census to arbitrary `L`. | Open and outside the bounded target. |

**Proof-obligation disposition:** `CONDITIONAL`. The frame-label and permutation
arithmetic is exact on the finite supplied index sets. The Hessian invariance,
eigenvalue clustering, spectral measures, inverse solves, and partition counts
are numerical computations conditional on the supplied compiler at `L=3,4`.

## Load-bearing inputs and declared choices

### Scientific and executable inputs

- The landed finite similarity and seeded-pairing result:
  [Cycle 714](PHYSICAL_ASSEMBLY_DEFECT_ISOSPECTRALITY_AND_SOURCE_PAIRING_CYCLE714_NOTE_2026-08-02.md),
  its [runner](../scripts/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02.py),
  and its [receipt](../outputs/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02_receipt_2026-08-02.json).
- The finite sextet/complement and covering-sufficiency result:
  [Cycle 715](PHYSICAL_FRAME_GROUP_COMPLEMENT_AND_FINITE_PROBE_BLINDING_CYCLE715_NOTE_2026-08-02.md),
  its [runner](../scripts/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02.py),
  and its [receipt](../outputs/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02_receipt_2026-08-02.json).
- The complete finite averaging-set scan for its declared sources:
  [Cycle 716](PHYSICAL_COMPLETE_AVERAGING_SET_FRAME_BLINDNESS_CLASSIFICATION_CYCLE716_NOTE_2026-08-02.md),
  its [runner](../scripts/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02.py),
  and its [receipt](../outputs/physical_complete_averaging_set_frame_blindness_classification_cycle716_2026_08_02_receipt_2026-08-02.json).
- The body-diagonal action and finite transversal result:
  [Cycle 717](PHYSICAL_BODY_DIAGONAL_FRAME_FUNCTIONAL_TRANSVERSAL_LAW_CYCLE717_NOTE_2026-08-02.md),
  its [runner](../scripts/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py),
  and its [receipt](../outputs/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02_receipt_2026-08-02.json).
- The supplied
  [Cycle-696 open-coframe compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
  and its four transitive Cycle-576/Regge helper modules. The compiler supplies
  the matrix, open-box index, site map, spatial classes, finite-difference
  assembly, and frame table; no modeling choice in it is promoted here.

Both runners declare these paths in `AUDIT_INPUT_PATHS`. Cycles 714–717 remain
subject to independent audit; this note imports their finite source surfaces,
not an audit grade.

### Declared analysis choices

- box sizes `L={3,4}`, unwrapped boundary, and proper-frame table supplied by
  Cycle 696;
- deterministic Gaussian probe seeds `7183/7184` and `7184/7185`, obtained as
  base seeds `7180/7181` plus `L`;
- eigenvalue-cluster tolerance `10⁻⁹`, spectral-measure and Rayleigh-fibre
  thresholds `10⁻⁸`, cross-measure floor `0.1`, and Rayleigh gap floor `10⁻⁴`;
- single-slot equality threshold `10⁻⁸`, resolved-gap floor `10⁻⁵`, and 20
  deterministic Gaussian census probes with seeds `900+s+L`;
- rank-one spectral witness size `10⁻³` and common doublet-basis rotation grid
  of 33 angles from zero to `π/2`.

These are classifier, conditioning, and hostile-witness choices, not physical
constants.

## Finite permutation and matrix result

The 24 supplied signed permutation frames have determinant one. At each size,
their degree-of-freedom maps are bijections and satisfy

`m_(ab) = m_a ∘ m_b`

for all 576 pairs. With the dense pullback convention this is an anti-action,
`P_(ab)=P_b P_a`. Therefore the conjugator from transported matrix `Q_b` to
`Q_a` is the frame label `b⁻¹a`. Every inverse-left comparison roundtrips bit
for bit. The reversed label `ab⁻¹` differs on 456 pairs and reaches residual
`4`, fixing the convention.

The matrix `Q_g=Q[m_g,m_g]` is permutation-similar to `Q` by construction.
Sorted eigenvalues agree numerically to `1.9×10⁻¹³` at `L=3` and
`4.9×10⁻¹³` at `L=4`; trace, Frobenius norm, determinant sign, and
log-absolute-determinant are consistent at their displayed residuals. The
determinant signs are `+1` and `−1`, respectively. A rank-one `10⁻³` matrix
mutation shifts an eigenvalue by at least `2.1×10⁻⁴`, providing a resolved
spectral witness.

The body-diagonal stabilizer is the sextet

`S={1,4,9,15,18,23}`.

The four label fibres are its right cosets. This is exact group arithmetic.
Constancy of the compiled matrix inside them remains numerical: within-fibre
residual `1.3×10⁻¹⁰`, cross-fibre distance `4` at both sizes.

## Spectral measures rather than eigenvector coordinates

For a nonzero source `u`, let `Π_λ` be the orthogonal projector onto a complete
eigenspace of `Q` and define

`μ_u(λ)=||Π_λ u||²/||u||²`.

Then

`R(u)=uᵀQ⁻¹u/||u||² = Σ_λ μ_u(λ)/λ`.

The weights are nonnegative and sum to one, so the finite Rayleigh values lie
inside the convex hull of the inverse eigenvalues. The measured hull is
`[−0.7066,2.1168]` at `L=3` and `[−2.3225,27.1972]` at `L=4`. It spans both
signs, and the reported functional is signed.

The eigenspaces must be kept intact. At `L=3`, 32 of the 66 eigenspaces are
doublets; at `L=4`, 92 of 187 are doublets. The maximum splitting within a
cluster is `3.6×10⁻¹⁴`, while the smallest gap between clusters is
`1.28×10⁻²` and `4.67×10⁻³`. Coordinates assigned to the two individual
eigenvectors of a doublet change under an allowed two-dimensional basis
rotation, while their sum is invariant.

For the two named probes at each size, pulled source vectors in the 24-frame
orbit are pairwise separated by at least `11.9` and `20.9`. Their spectral
measures have the following `L¹` separation:

| size | seed base | within a body-diagonal fibre, maximum | across fibres, minimum |
|---:|---:|---:|---:|
| 3 | 7180 | `2.14×10⁻¹⁰` | `0.6757` |
| 3 | 7181 | `2.59×10⁻¹⁰` | `0.8256` |
| 4 | 7180 | `2.98×10⁻¹⁰` | `0.8674` |
| 4 | 7181 | `3.08×10⁻¹⁰` | `0.8836` |

Thus these finite probes have four separated spectral-measure fibres, not only
four coincident Rayleigh values. Their within-fibre Rayleigh spreads are at most
`3.0×10⁻¹²` and `1.9×10⁻¹⁰`; cross-fibre gaps are at least `2.7×10⁻³` and
`5.6×10⁻³`.

## Regular-coset source averages

The runner enumerates all 30 subgroups and derives four order-four subgroups
transitive on the body diagonals. It selects one and forms a declared right
coset `A`. The product of that subgroup with `S` covers all 24 labels. Therefore
the 24 left translates of `A` reduce to six, each expressible as `sA` for a
label `s∈S`.

For either probe, the six averaged source vectors obey the corresponding
sextet-pullback relation to relative residual `1.2×10⁻¹⁶`. After normalization,
their pairwise distances are at least `0.97`; vector equality is not the source
of the shared value. Their maximum pairwise spectral-measure distances and
Rayleigh spreads are:

| size | seed base | spectral-measure `L¹` maximum | Rayleigh spread |
|---:|---:|---:|---:|
| 3 | 7180 | `3.51×10⁻¹¹` | `2.81×10⁻¹²` |
| 3 | 7181 | `1.03×10⁻¹⁰` | `1.83×10⁻¹²` |
| 4 | 7180 | `1.43×10⁻¹⁰` | `6.59×10⁻¹¹` |
| 4 | 7181 | `1.96×10⁻¹⁰` | `1.27×10⁻¹¹` |

This is the symmetry mechanism behind the shared finite value: the distinct
vectors share the complete eigenspace-summed spectral measure to numerical
precision. The submitted comparison instead split each doublet into arbitrary
eigenvectors and reported individual-weight differences as large as `0.92`.
Under a common allowed rotation of those doublet bases, that `L¹` comparison
moves through ranges `0.40–0.66`, while the eigenspace measure remains fixed.

A four-frame collection drawn from one body-diagonal fibre supplies a contrast.
It has 24 left translates; for the declared probes their maximum
spectral-measure separation is `1.12–1.47` and their Rayleigh spread is
`0.039–0.518`.

## Finite single-slot census

For each coordinate slot, the runner evaluates the four representative
diagonal entries of the transported inverse and records their equality
partition. Every within-fibre representative substitution is below `10⁻⁸`.
Every pair entering the partition is either within the equality threshold or
at least `4.3×10⁻⁵` apart at `L=3` and `1.8×10⁻⁴` at `L=4`.

| size | slots | realized partitions | finest-partition count | frame-constant slots |
|---:|---:|---:|---:|---:|
| 3 | 98 | 14 of 15 | 0 | 6 |
| 4 | 279 | 15 of 15 | 48 | 19 |

The six constant slots at `L=3` split as two each in direction classes 1, 3,
and 7. At `L=4`, the 19 split as four each in classes 5, 9, and 11 and seven in
class 13. Twenty disclosed deterministic Gaussian census probes realize the
finest partition at each size; this is a finite sample, not a generic-source
theorem.

## Hostile and independent checks

The primary carries:

- reversed action and conjugator indices;
- a rank-one spectral mutation;
- minimum cross-fibre matrix and spectral-measure separation, rather than only
  a maximum witness;
- solve and nonzero-average margins for every transfer calculation;
- a regular-coset source-symmetry reconstruction and a nonregular contrast;
- a 33-angle doublet-basis rotation showing individual-weight dependence; and
- explicit close/far classifier margins for every single-slot pair.

The independent checker imports no Cycle-718 code. It constructs dense
permutation matrices rather than index-array slices, rebuilds the group and
subgroups, recomputes eigenspace projectors and every finite census anchor, and
reads the primary receipt only after its own calculation.

## Honest boundary

- The numerical Hessian, sextet invariance, eigenspaces, spectral measures,
  solves, and census are measured only at `L=3,4` on the supplied unwrapped
  compiler surface.
- The body-diagonal group action and permutation identities are exact on the
  finite label/index sets. They are not a continuum or framework-level
  covariance theorem.
- The fibre and regular-coset measurements use four named Gaussian probes.
  Symmetric or specially supported sources can merge the measured fibres.
- The Cycle-716 powerset and Cycle-717 transversal results retain their own
  source and size boundaries; this note does not widen them.
- The signed inverse-Hessian Rayleigh quotient is not interpreted as a norm,
  positive energy, or physical probability.
- The single-slot zero count at `L=3` and count 48 at `L=4` are finite census
  values, not an obstruction or a size law.

## Review record

Review-loop iteration 1 replaced the submitted “coincidence of levels with
different spectral weights” interpretation by the basis-invariant
eigenspace-measure calculation. It corrected the cross-fibre gate from a
maximum witness to a minimum separation, named log-absolute-determinant and its
sign, added inverse and classifier margins, narrowed every generic/source and
size surface, declared the full predecessor/compiler input closure and timeout,
replaced raw cold stdout with canonical caches, and added an independent dense
checker.

Hard landing conditions:

1. reviewed predecessor PRs #5902 and #5903 must be contained in remote `main`;
2. the citation-graph helper registry must map
   `physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_note_2026-08-02`
   to
   `scripts/physical_frame_orbit_spectral_measure_and_rayleigh_census_cycle718_independent_check_2026_08_02.py`;
3. both caches must be fresh against the complete declared input closure;
4. pipeline-generated ledger and status outputs must be stripped, while the
   citation-graph manifest acknowledgment co-lands if topology changes.

This package makes a positive bounded finite claim and ships no negative or
no-go result, so the No-Go Discipline battery is not applicable. Independent
audit remains required for the proposed claim.
