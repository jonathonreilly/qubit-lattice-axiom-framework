# Finite frame-group complement and probe-blinding census — Cycle 715

**Date:** 2026-08-02 (review-loop repair 2026-08-11)

**Type:** bounded_theorem

**Status:** proposed_retained

**Primary runner:**
[`physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02.py`](../scripts/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02.py)

**Independent checker:**
[`physical_frame_group_complement_and_finite_probe_blinding_cycle715_independent_check_2026_08_02.py`](../scripts/physical_frame_group_complement_and_finite_probe_blinding_cycle715_independent_check_2026_08_02.py)

**Primary cache:**
[`physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02.txt`](../logs/runner-cache/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02.txt)

**Independent cache:**
[`physical_frame_group_complement_and_finite_probe_blinding_cycle715_independent_check_2026_08_02.txt`](../logs/runner-cache/physical_frame_group_complement_and_finite_probe_blinding_cycle715_independent_check_2026_08_02.txt)

**Receipt:**
[`physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_frame_group_complement_and_finite_probe_blinding_cycle715_2026_08_02_receipt_2026-08-02.json)

## Claim boundary

For the supplied Cycle-696 open-box static Hessian at `L ∈ {3,4}`, the same
six frame labels have transport defect below `10⁻⁹`. Conditional on this
numerically identified sextet `S`, exact finite-group arithmetic shows that it
is a subgroup of the 24 proper cubic frames and that the independently rebuilt
Cycle-707 centered-source stabilizer `C4` is one of four order-four complements
of `S`. The exact labels split into four right cosets of `S`. The 24 transported
Hessians form four numerical clusters at tolerance `10⁻⁶`, with within-cluster
residual at most `1.2×10⁻¹⁰` and between-cluster separation at least `4`.

For any subgroup `H`, `S H = G` is an algebraic sufficient condition for an
`H`-averaged source to have a frame-independent quadratic pairing, conditional
on exact `S`-invariance of the Hessian. The exact subgroup census has 30
members; nine cover, and the smallest covering order is four, attained by four
complements. For the three deterministic Gaussian probes with disclosed seeds
at each of `L=3,4`, observed numerical blindness agrees with covering for all
30 subgroups. This finite probe agreement is not a universal necessity theorem:
the all-ones probe is an explicit accidentally blind witness already for the
identity subgroup.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: physical_minus_branch_response_floor_assembly_defect_law_cycle709_note_2026-08-02
target_blocker_text: "Mixed-sign prediction. Extend the law to the 18 mixed-sign frames: predict each frame's response defect from its own measured E before running the transport, upgrading the law from two branches to all 24."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "test whether the four measured Hessian clusters determine the mixed-frame response defects before the response transport is executed"
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
claim_type_reason: "exact finite group arithmetic conditional on a numerically identified Hessian stabilizer at two supplied box sizes, plus a finite six-probe subgroup census"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_frame_group_complement_and_finite_probe_blinding_cycle715_independent_check_2026_08_02.py
```

## Exact target and proof obligations

The target is to classify the finite frame labels, transported-Hessian clusters,
covering subgroups, and the declared deterministic probe responses at the two
supplied sizes.

| obligation | disposition |
|---|---|
| Reconstruct the proper-frame multiplication table and the bounding-box relabeling. | Closed by exact integer matrices and all `24²` composition checks at both sizes. |
| Identify the Hessian stabilizer without assuming its membership. | Closed numerically at tolerance `10⁻⁹`; the same sextet appears at `L=3,4`, with the nearest nonmember defect separated by at least `4`. |
| Reconstruct the Cycle-707 one-edit source stabilizer without a membership pin. | Closed at the Cycle-707 odd centered sizes `L=3,7`; both give `{20,21,22,23}`, also generated independently as powers of the x-axis quarter turn. |
| Prove the complement and subgroup-covering statements. | Closed as exact arithmetic on the 24 supplied frame labels. |
| Establish the transported-operator classes. | Closed as four finite numerical clusters at `L=3,4`; no symbolic equality or arbitrary-size result is claimed. |
| Prove covering suffices for subgroup-average blindness. | Closed algebraically conditional on exact `S`-invariance, and numerically tested for every covering subgroup and declared probe. |
| Prove covering is necessary for every source or that four is the universal minimum blinding order. | Refuted within the computed sector by the all-ones identity-subgroup witness; this stronger claim is excluded from the target. |

**Proof-obligation disposition:** `CONDITIONAL`. The group calculations are
exact on the supplied frame labels. The operator premise and pairings are finite
floating computations at two sizes. Universal source necessity, symbolic
Hessian invariance, arbitrary-size transport, continuum, and physical gauge
claims remain outside the target.

## Inputs and declared choices

### Load-bearing scientific inputs

- The source-stabilizer construction whose decorated one-edit domain is rebuilt
  here:
  [Cycle 707 source-stabilizer result](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md),
  its [runner](../scripts/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01.py),
  and its [receipt](../outputs/physical_source_stabilizer_coset_collapse_k_sign_law_cycle707_2026_08_01_receipt_2026-08-01.json).
- The supplied
  [Cycle-696 open-coframe compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
  including its static Hessian, open-box admission rule, finite-difference
  assembly, frame-site map, spatial classes, and transitive Cycle-576/Regge
  helpers declared by both runners. The compiler is consumed as a supplied
  finite object; this note does not promote its modeling choices to axioms.

The Cycle-709 response-floor note is a trace target, not a scientific input.
Cycles 708–714 are context only and supply no bytes or conclusions to this
package.

### Declared analysis choices

- Hessian sizes `L={3,4}` and Cycle-707 centered-source reconstruction sizes
  `L={3,7}`;
- near-zero-defect threshold `10⁻⁹`, numerical cluster threshold `10⁻⁶`, and
  between-cluster floor `1`;
- three normalized Gaussian probes per Hessian size, generated with NumPy
  `default_rng` seeds `7153` and `7154`;
- blindness threshold `10⁻⁶` and explicit solve/norm residual gates.

The thresholds and random seeds are disclosed analysis choices, not derived
constants and not physical source data.

## Finite group result

The exact frame table has identity label `23`. At both Hessian sizes, the
near-zero-defect labels are

`S = {1,4,9,15,18,23}`.

They close under all 36 ordered products. The one-edit centered decorated
domain used by Cycle 707 has proper stabilizer

`C4 = {20,21,22,23}`

at `L=3` and `L=7`. The primary derives this set from decorated-domain equality
and separately generates it as the powers of the x-axis quarter turn; no
stabilizer membership list is an input. `S ∩ C4 = {23}` and `S C4` contains all
24 labels, so `C4` is a complement.

The four right cosets are

- `{1,4,9,15,18,23}`;
- `{0,6,10,12,19,21}`;
- `{2,5,11,14,16,20}`;
- `{3,7,8,13,17,22}`.

With the runner's index-array convention, the exact composition check is
`m_(ab) = m_a ∘ m_b` for all 576 pairs. This implies
`Q_(s a) = (Q_s)` relabeled by `a`, so an exact fixing relation for `s ∈ S`
would make the right cosets constancy classes. Reversing the array composition
matches only 120 of 576 pairs, and the corresponding left blocks have Hessian
spread `4` at both sizes.

Numerically, the within-right-coset residual is `1.2×10⁻¹⁰` and the minimum
between-coset max-entry separation is `4` at both sizes. Therefore the data form
four clusters at `10⁻⁶`; floating matrices separated by a nonzero residual are
not described as literally identical.

## Covering subgroups and declared probes

Exact enumeration gives 30 subgroups. For every subgroup `H`, the product-set
count agrees with

`S H = G  ⇔  |H| = 4 |H ∩ S|`.

The nine covering subgroup orders are
`4,4,4,4,8,8,8,12,24`. Thus the minimum *covering-subgroup* order is four and
four complements attain it. This does not say that four is the minimum averaging
order for every source.

For each declared Gaussian probe `b`, the runner forms
`b̄_H = |H|⁻¹ Σ_(h∈H) P_h^T b`, gates `H`-invariance of the average, normalizes
only after a non-cancellation check, and evaluates
`b̄_H^T Q_g⁻¹ b̄_H` for all 24 labels. At each size, observed blindness agrees
with covering for all 30 subgroups and all three probes. The smallest
noncovering worst-probe spread is `2.5×10⁻²` at `L=3` and `9.5×10⁻²` at `L=4`;
the largest covering spread is `1.1×10⁻¹¹` and `1.8×10⁻¹⁰`, respectively.

The all-ones probe is permutation-invariant. Its pairing spread for `H={23}` is
`2.2×10⁻¹⁶` at `L=3` and `8.6×10⁻¹⁴` at `L=4`, even though that subgroup does
not cover. It is a constructive scope witness: covering is sufficient, while
the finite Gaussian agreement cannot establish universal necessity.

## Hostile and independent checks

The primary carries:

- the reversed-composition and left-block orientation witnesses;
- an order-four subgroup with two elements in `S`, whose product covers only 12
  labels;
- a single-entry Hessian mutation that breaks sextet invariance;
- noncovering Gaussian probes with resolved pairing spread;
- average-invariance and non-cancellation gates; and
- the all-ones accidental-symmetry witness.

The independent checker does not import the primary. It separately rebuilds
the relabeling, group table, 30 subgroups, centered-source stabilizer, Hessians,
source averages, and linear solves. It reads the primary receipt only after its
own calculation and compares the finite invariants.

## Honest boundary

- `S` is a numerical near-zero-defect sextet at `L=3,4`, not a symbolic or
  arbitrary-size Hessian stabilizer.
- Four is the exact index of the label subgroup and the minimum order among
  covering subgroups. It is not a universal minimum source-blinding order.
- The six Gaussian vectors are deterministic test probes, not supplied
  physical sources. Their `30/30` agreement is a finite observation.
- The operator statement concerns functions of `Q_g` alone. Source-dependent
  pairings, solved floors, spectra with additional inputs, or response-chain
  quantities require their own covariance checks.
- No equality between the four-frame and 24-frame averaged vectors or physical
  observables is claimed.
- The Hessians are nonsingular and indefinite in the tested sector. The signed
  quadratic form is not interpreted as a positive energy.
- No preferred frame, continuum covariance, gauge principle, or physical
  gravity conclusion follows from this finite classification.

## Review record

Review-loop iteration 1 replaced the submitted universal “minimal blinding”
claim with the exact minimum-covering result and the finite probe observation it
actually computed. It exposed the all-ones counterexample to universal
necessity, derived the Cycle-707 stabilizer rather than hard-coding it, checked
the sextet at both Hessian sizes, corrected the relabeling composition wording,
added conditioning and averaged-source invariance gates, added hostile
mutations, declared the complete input closure and timeout, replaced raw cold
stdout with canonical caches, and added an independent checker.

Hard landing conditions:

1. reviewed predecessor PRs #5898 and #5899 must be contained in remote `main`;
2. the citation-graph helper registry must map
   `physical_frame_group_complement_and_finite_probe_blinding_cycle715_note_2026-08-02`
   to
   `scripts/physical_frame_group_complement_and_finite_probe_blinding_cycle715_independent_check_2026_08_02.py`;
3. both caches must be fresh against every declared input;
4. pipeline-generated ledger and status outputs must be stripped, while the
   citation-graph manifest acknowledgment co-lands if the graph changes.

This package ships a positive bounded result and a constructive accidental-
symmetry witness, not a no-go claim, so the No-Go Discipline battery is not
applicable. Independent audit remains required for the proposed claim.
