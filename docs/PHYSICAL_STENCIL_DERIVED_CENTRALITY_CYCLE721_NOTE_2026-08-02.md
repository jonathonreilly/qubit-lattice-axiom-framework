# Finite stencil stabilizer and box-centre centrality — Cycle 721

**Date:** 2026-08-02 (review-loop repair 2026-08-12)

**Type:** bounded_theorem

**Status:** proposed_retained

**Primary runner:**
[`physical_stencil_derived_centrality_cycle721_2026_08_02.py`](../scripts/physical_stencil_derived_centrality_cycle721_2026_08_02.py)

**Independent checker:**
[`physical_stencil_derived_centrality_cycle721_independent_check_2026_08_02.py`](../scripts/physical_stencil_derived_centrality_cycle721_independent_check_2026_08_02.py)

**Primary cache:**
[`physical_stencil_derived_centrality_cycle721_2026_08_02.txt`](../logs/runner-cache/physical_stencil_derived_centrality_cycle721_2026_08_02.txt)

**Independent cache:**
[`physical_stencil_derived_centrality_cycle721_independent_check_2026_08_02.txt`](../logs/runner-cache/physical_stencil_derived_centrality_cycle721_independent_check_2026_08_02.txt)

**Receipt:**
[`physical_stencil_derived_centrality_cycle721_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_stencil_derived_centrality_cycle721_2026_08_02_receipt_2026-08-02.json)

## Claim boundary

For the supplied Cycle-696 stencil of 24 four-dimensional monotone path
simplices, exhaustively enumerate the 48 spatial signed axis permutations. A
template image is compared after a free spatial translation and the supplied
periodic tick shift modulo two. On this exact finite domain, the template-set
stabilizer has order 12 and equals the stabilizer of the spatial
body-diagonal line. It is a subgroup with six determinant-one and six
determinant-minus-one elements. Its proper half is exactly frame indices
`(1, 4, 9, 15, 18, 23)` in the supplied 24-frame table, so the proper-frame
right-coset count is four.

In the explicit tick-fixed comparison, the same enumeration gives the unsigned
order-six coordinate-permutation subgroup, with determinant split `3+3`.
Allowing the modulo-two tick shift adds the disjoint globally sign-reversed
coset, also split `3+3`. Thus the proper sextet contains three tick-fixed even
permutations and three sign-reversed odd permutations; the extra coset is not
the improper half. This comparison is not a uniqueness statement about other
tick models or other stencils.

For the open-box slot sets at `L in {3,5}`, the centre-conjugate site maps and
their induced edge-slot maps are exact permutations and obey the declared
composition order on all `48^2` pairs. The scalar point reflection `-I` is
therefore central in the induced finite action. For the supplied assembled
static form at `L in {3,4,5}`, the exact order-12 stencil prediction agrees
numerically with all 48 relabeling tests: within-stabilizer residual is at most
`1.243450e-10`, while the smallest outside residual is `4`.

These are finite results about the supplied compiler bytes and conventions.
They provide neither an arbitrary-size incidence theorem nor a derivation of
the stencil, tick fold, or improper relabelings from the framework axioms.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: physical_assembly_defect_isospectrality_and_source_pairing_cycle714_note_2026-08-02
target_blocker_text: "derive exact stencil-level sextet invariance and an arbitrary-L incidence theorem, then classify the source subspaces that reduce the four numerical clusters"
source_of_blocker_text: next_trace_action
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive an arbitrary-L incidence theorem for the supplied stencil family, or identify the exact finite boundary at which the slot action changes"
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
claim_type_reason: "exact finite signed-permutation, template-stabilizer, subgroup, and slot-action identities plus numerical assembled-form comparisons at three supplied box sizes"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_stencil_derived_centrality_cycle721_independent_check_2026_08_02.py
```

## Exact target and proof-obligation graph

**Exact target.** On the declared finite signed-permutation, stencil-template,
and box-index sets, determine the stencil stabilizer, its determinant split and
proper-frame cosets, and the centrality of the induced box-centre point
reflection; then compare the exact prediction with the supplied assembled
matrix at the three declared sizes.

| obligation | disposition |
|---|---|
| Reconstruct the 24 path simplices and the 48 signed axis permutations. | Closed by exhaustive integer enumeration; the independent checker generates the paths from all permutations of the four coordinate steps. |
| Prove the centre-conjugate site and slot action on the declared boxes. | Closed at `L=3,5` by bijectivity, 48 distinct maps, and all 2,304 composition pairs. Reversing composition changes 175,104 and 1,094,400 entries. |
| Transport centrality from `-I` to the slot maps. | Closed because `-I` commutes with all 48 integer matrices and the finite slot maps obey the homomorphism law. A non-scalar sign flip fails against 32 frames. |
| Determine the folded template stabilizer and relate it to the body diagonal. | Closed on all 48 candidates: both predicates select the same 12 elements; product and inverse closure are checked explicitly. |
| Separate the periodic-tick and tick-fixed canonicalizations. | Closed for the supplied template set: the tick-fixed stabilizer is the unsigned `S_3` coordinate-permutation subgroup with determinant split `3+3`; folding adds its globally sign-reversed coset, also split `3+3`. |
| Identify the proper sextet and four cosets. | Closed against the supplied frame table and independently against determinant/parity arithmetic. |
| Compare the exact prediction with the assembled form. | Closed numerically at `L=3,4,5`, with an explicit within/outside margin and six altered-template controls at `L=3`. |
| Derive the stencil or tick fold from Lattice, Qubit, Admissibility, and Record, or extend the slot/assembly result to arbitrary `L`. | Open and outside this bounded target. |

**Proof-obligation disposition:** `CONDITIONAL`. The group, template, subgroup,
and finite map statements are exact for the declared finite sets. The result is
conditional on the supplied Cycle-696 stencil and storage conventions, and the
assembled-matrix comparisons are numerical at the three named sizes.

## Load-bearing inputs and declared choices

### Scientific and executable inputs

- The supplied
  [Cycle-696 open-coframe compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
  and its four transitive Cycle-576/Regge modules provide the stencil, static
  slot index, spatial direction classes, local Hessian construction, frame
  table, open boundary, and tick length two.
- The finite body-diagonal action and transversal comparison is recorded by
  [Cycle 717](PHYSICAL_BODY_DIAGONAL_FRAME_FUNCTIONAL_TRANSVERSAL_LAW_CYCLE717_NOTE_2026-08-02.md),
  its [runner](../scripts/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py),
  and its [receipt](../outputs/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02_receipt_2026-08-02.json).
- The finite proper-frame cosets and point-reflection map used for comparison
  are recorded by
  [Cycle 719](PHYSICAL_LEVEL_SET_ORBIT_LAW_IMPROPER_CENTER_IDENTITY_CYCLE719_NOTE_2026-08-02.md),
  its [runner](../scripts/physical_level_set_orbit_law_improper_center_identity_cycle719_2026_08_02.py),
  and its [receipt](../outputs/physical_level_set_orbit_law_improper_center_identity_cycle719_2026_08_02_receipt_2026-08-02.json).
- The finite ambient/domain distinction used to keep improper relabelings out
  of the physical-symmetry claim is recorded by
  [Cycle 720](PHYSICAL_AMBIENT_DOMAIN_SYMMETRY_SPLIT_CYCLE720_NOTE_2026-08-02.md),
  its [runner](../scripts/physical_ambient_domain_symmetry_split_cycle720_2026_08_02.py),
  and its [receipt](../outputs/physical_ambient_domain_symmetry_split_cycle720_2026_08_02_receipt_2026-08-02.json).
- The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) grant proper cubic
  rotations as Lattice symmetries. They do not grant improper spatial
  permutations; the six determinant-minus-one elements remain computational
  relabelings of this supplied assembly.

Both runners declare the complete note/runner/receipt and compiler-module
closure in `AUDIT_INPUT_PATHS`. They import no audit grade from these sources.

### Declared finite and numerical choices

- exact signed-permutation and template comparisons over 48 group candidates
  and 24 templates;
- site and slot action checks at `L={3,5}` and assembled-form checks at
  `L={3,4,5}`;
- relative equality tolerance `1e-8` for assembled matrices and separation
  ratio `1e3`;
- central finite-difference step `1e-4`, local Regge conventions, open boundary,
  and tick length two inherited from the compiler;
- six named altered-template subsets at `L=3`: full set, templates 0 and 7
  separately, one full orbit, the first 12 templates, and templates `(0,1)`.

The tolerances and finite subsets are analysis choices, not physical constants.
No fitted, measured, observational, or literature value enters this cycle.

## Exact finite derivation

For a signed axis permutation `R`, box centre `c=((L-1)/2)1`, and site `s`,
the centre-conjugate map is

`f_R(s) = R(s-c)+c = Rs+(I-R)c`.

Every row of `R` has one sign `epsilon_a`, so coordinate `a` of the offset is
`((L-1)/2)(1-epsilon_a)`, namely `0` or `L-1`. For each edge with stored
non-negative direction `w`, the image edge is stored with direction `|Rw|` and
with the smaller image endpoint as its low corner. Exhaustive index comparison
then gives `m_(RS)=m_R after m_S` on the declared boxes. The reversed order is
the explicit convention rejector.

The point reflection is `sigma=-I`, which is central in the signed-permutation
group. The exact finite homomorphism therefore gives
`m_sigma m_R = m_R m_sigma`. Direct endpoint transport independently recovers
the closed slot formula

`(w,x) -> (w,(L-1)1-x-w)`.

The four-dimensional path templates are the maximal chains obtained by adding
the four coordinate steps in all 24 orders. Each contains the zero and all-one
vertices. Exhaustive action on these 24 chains shows that the folded-template
stabilizer is exactly the set of spatial signed permutations taking
`(1,1,1)` to `+(1,1,1)` or `-(1,1,1)`. The positive case is the unsigned
coordinate-permutation subgroup; in the negative case the supplied modulo-two
tick shift supplies the fourth-coordinate complement and admits the globally
sign-reversed coset. Each order-six set has determinant split `3+3`. The proper
sextet therefore draws three elements from each set.

## Numerical assembly comparisons

For the supplied static matrix `Q`, the stencil-derived order-12 set equals the
tolerance-resolved relabeling-invariance set at each of `L=3,4,5`. The maximum
within-set max-entry residual is `1.243450e-10`; the minimum outside residual is
`4`, while the largest matrix entry is `2.945214e1`. The 24 proper frames form
four numerical matrix classes of six, identical to the exact proper right
cosets.

The 24 compiler local Hessian pieces have numerical spread zero while their 24
class tuples are distinct. Six altered template subsets produce exact derived
stabilizer orders `(12,1,1,12,2,1)` and the same six tolerance-resolved matrix
symmetry orders at `L=3`. These are discriminating finite controls. They show
that this stabilizer calculation responds to the selected template set; they do
not classify admissible stencils in general.

## Independent reconstruction and hostile checks

The independent checker imports no Cycle-721 code. It generates the 24 paths
from coordinate-order permutations, represents signed permutations as pure
integer `(permutation, signs)` tuples, transports edge endpoints directly
rather than using the primary low-corner formula, and recomputes the stabilizer,
determinant split, subgroup closure, central map, proper cosets, and finite
assembled-matrix comparisons. It reads the primary receipt only after its own
calculation.

On the repaired source the primary reports `TOTAL: PASS=49 FAIL=0` and the
independent checker reports `TOTAL: PASS=30 FAIL=0`.

Review-loop hostile mutations separately confirmed that the gates reject:

1. disabling the periodic tick shift in the folded stabilizer;
2. reversing the slot-composition order;
3. changing the expected proper sextet;
4. raising the matrix classifier tolerance above the outside-group floor.

## Honest boundary

- Exactness applies to finite integer comparisons over the declared group,
  templates, and index sets. The assembled Hessian, local-piece equality, and
  relabeling residuals are floating-point measurements of the supplied
  compiler.
- The periodic-tick comparison identifies what changes between two explicit
  canonicalizations of this stencil. It is not an exhaustive classification of
  tick models, stencils, boundary conditions, or improper symmetries.
- The determinant-minus-one half is a computational identity of the supplied
  assembly, not a framework Lattice symmetry. Physical statements use the
  determinant-one sextet only.
- Arbitrary `L`, other boundaries, other stencil families, continuum limits,
  and derivation of the compiler conventions from the axioms remain outside
  the result.

## Review record

Review-loop iteration 1 retained the exact finite stabilizer result but repaired
its package and boundary. It replaced raw cold stdout with canonical caches,
declared the full input closure and timeout, added an implementation-independent
checker and subgroup-closure gate, and corrected a substantive false inference
in the submitted `46/0` result: the primary checked only that the tick-fixed
stabilizer had order six and was a proper subset, then identified it in prose
with the determinant-one half. Independent enumeration shows instead that it
is unsigned `S_3`, with three proper and three improper elements, while the fold
adds its globally sign-reversed coset. The repair also separates exact finite
identities from numerical assembly measurements and narrows “sole source” and
“different admissible stencil” language to the two explicit canonicalizations
and six altered template subsets actually tested.

Hard landing conditions:

1. reviewed predecessor PRs #5908 and #5911 must be contained in remote `main`;
2. the citation-graph helper registry must map
   `physical_stencil_derived_centrality_cycle721_note_2026-08-02` to
   `scripts/physical_stencil_derived_centrality_cycle721_independent_check_2026_08_02.py`;
3. both caches must be fresh against the complete declared input closure;
4. pipeline-generated ledger and status outputs must be stripped, while the
   citation-graph manifest acknowledgment co-lands because topology changes.

Independent audit remains required for the proposed bounded claim.
