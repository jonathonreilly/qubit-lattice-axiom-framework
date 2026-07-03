# P-FLUX Point-Zero-Set Supplier Narrow No-Go

**Date:** 2026-06-10
**Type:** no_go
**Claim type:** no_go
**Claim scope note:** narrow candidate-supplier no-go for the P-FLUX
selector. On the two nearest-neighbor flux branches tested here, the linked
spectral/clustering, count/no-proper-quotient, and Record/readout candidates
do not supply a branch selector requiring a point-like zero set,
`ker = carrier`, or no extra massless sectors. The separating facts are real
and computed, but they remain separate input rather than a consequence of
those linked rows.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/p_flux_point_zero_set_check_2026_06_10.py`](../scripts/p_flux_point_zero_set_check_2026_06_10.py)
(`TOTAL: PASS=22 FAIL=0`).
**Runner cache:**
[`logs/runner-cache/p_flux_point_zero_set_check_2026_06_10.txt`](../logs/runner-cache/p_flux_point_zero_set_check_2026_06_10.txt).

---

## Question

The parent matter-content route no-go
[`P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10.md)
shows that the generation-carrier battery does not select the P-FLUX branch:
both tested branches pass that battery.

The next question is whether a linked candidate row already supplies one of
the missing selector clauses named by that parent:

- a point-like zero set;
- `ker = carrier`, equivalently no extra massless sectors on this surface;
- a branch-neutral transfer/positivity route that would force either of the
  above.

This note tests the first two clauses against the linked supplier candidates
and checks that the third is not closed by the same finite computation.

## Result

The finite spectral separator is real:

```text
K0: uniform plaquette flux +1, scalar nearest-neighbor hopping
K1: uniform plaquette flux -1, Kawamoto-Smit sign hopping

zero-mode counts, L = 4,8,12:
K0 = 20, 68, 140
K1 = 8, 8, 8

extra zero modes beyond the embedded carrier, L = 4,8:
K0 = 12, 60
K1 = 0, 0
```

So `K1` is exactly the point-like/kernel-exact branch in this finite test.
The problem is supplier authority: the linked candidate rows do not require
that property.

The runner certifies three failures of the proposed supplier routes:

1. The gap/clustering route is branch-neutral on this surface. At `m = 0`
   both branches are gapless. Under the shared anticommuting staggered-mass
   probe `m epsilon`, both branches gap to exactly `m`. The range and
   hopping-norm data used by locality-style bounds are also identical.
2. The count/no-proper-quotient route admits no branch-separating reading.
   Read on the finite carrier, it is true on both branches. Read on the full
   kernel, it is false on both branches: the full `K1` kernel already splits
   into four Hamming-class blocks, and the kernel-global count readouts are
   `8/4` for `K1` and `20/8` for `K0`, never `3`.
3. The Record/readout route is conditional on a supplied readout context and
   finite sector decomposition. It does not by itself select a kinetic kernel,
   bound a kernel dimension, or identify the realized matter carrier.

Therefore this note does not derive the P-FLUX selector. It narrows the live
residual: a later theorem must supply a genuine point-zero-set,
kernel-exactness, no-extra-sector, or branch-neutral transfer/positivity
principle. This note supplies none of those principles.

## Computed Witnesses

### Zero-Set Geometry

For `K0`, the kernel is the lattice trace of

```text
sum_mu cos(p_mu) = 0.
```

The runner checks that this symbol count matches exact diagonalization at
`L = 4, 8, 12`, giving `20, 68, 140` zero modes and a measured growth exponent
about `1.78`. For `K1`, the kernel stays at `8` across the same volumes.

The point-zero property is not a synonym for first-order kinetic order: a
scalar comparator with on-site term `-6` has a point-like zero set
`1, 1, 1` but does not carry the generation carrier.

### Clustering And Locality Candidates

The cluster-decomposition row is conditional on a positive transfer gap for
the load-bearing exponential-clustering leg. At `m = 0`, both branches have
gap `0`, so that hypothesis fails on both. With the shared mass probe
`m epsilon(x)`, `epsilon(x) = (-1)^(x1+x2+x3)`, the runner verifies
anticommutation with both branch operators and exact gap `m` on both. The
hypothesis, when made true by that probe, is true branch-neutrally.

The log-transfer quasilocality row is scoped to the free bilinear staggered
two-step sector and has sharp rate `arcsinh(m)`, which goes to `0` at the
licensed massless surface. It is not a point-zero-set or kernel-exactness
selector here.

### Count And No-Proper-Quotient Candidates

The carrier-conditional reading is the linked row's own reading. On both
branches, the embedded `hw = 1` carrier generates `M_3(C)`, has commutant
dimension `1`, and gives count `3`.

The kernel-global restatement is the only reading that could see the extra
`K0` modes, but it cannot be what the linked rows mean: it fails on `K1`
itself. On the full kernels the restricted algebra has commutant dimension
`4` for `K1` and `8` for `K0`; the kernel-global species readouts are `8/4`
and `20/8`. This is false/false, not a selector.

The entire branch separation is the extra clause `ker = carrier`. Adding it
would select `K1`; this note does not add it.

### Record Candidate

The Record axiom is a durable realized-outcome readout in a supplied readout
context. It supplies no readout context, central-sector decomposition,
sector-generation rule, weighting, normalization, probability rule,
measurement/decoherence dynamics, time metric, within-sector state, occupancy
rule, source/action bridge, scale, or arbitrary observable identification.
The record-function finite-sector row is likewise conditional on a supplied
finite record-sector decomposition. Neither statement bounds the massless
sector of a kinetic operator.

## Boundaries

- Finite-volume scope: `L = 4, 8, 12` with periodic boundary conditions.
  Infinite-volume classification is not claimed.
- The mass deformation `m epsilon` is a hypothesis probe for branch-neutral
  gap behavior. It is not a claim that this mass is the realized dynamics.
- The kernel-global readings tested are the natural invariant-subspace and
  species-count restatements. Exhaustiveness over every conceivable future
  restatement is not claimed.
- Predicate `G` from the parent remains a declared kernel-sector realization
  reading. This note does not turn it into a physical bridge.
- The mass-pattern and `AC_phi_lambda` side of the P-FLUX program is out of
  scope.
- No framework axiom, primitive, accepted-premise registry entry, empirical
  input, probability rule, weighting rule, normalization rule, readout bridge,
  or audit verdict is added here.

## No-Go Discipline Gate

- **N1 alternative routes:** zero-set geometry is attempted and succeeds as a
  computation, but no linked candidate row requires it; clustering/locality is
  attempted and is branch-neutral under the gap tests; count/no-proper-quotient
  is attempted and ties true/true on the carrier; kernel-global restatement is
  attempted and ties false/false; Record/readout is attempted and is only
  conditional on supplied sectors; transfer/positivity remains a separate live
  route, not closed here.
- **N2 wall independence:** for escapes (i) and (ii), the apparent walls
  collapse to one missing selector clause: require the realized massless sector
  to be point-like/kernel-exact/no-extra-sector. Escape (iii) is independent
  and is not claimed closed by this note.
- **N3 hidden-wall scan:** finite volumes, periodic boundaries, carrier
  restriction, kernel-global restatement, and the mass probe are explicit.
  The missing selector clause is named rather than smuggled.
- **N4 residual matching:** the residual matches the parent note's stated
  escape set. This note only sharpens the point-zero and kernel-exactness
  escapes; it does not claim a global P-FLUX no-go.
- **N5 rhetoric audit:** "no supplier" means no supplier among the linked
  candidates tested here under the stated finite surfaces and readings. It
  does not mean `K1` is unphysical, wrong, or underivable.
- **N6 partial-closure scan:** a later theorem could still close the selector
  by deriving point-like zero sets, `ker = carrier`, no extra massless sectors,
  density-of-states/critical-decay selection, or a branch-neutral
  transfer/positivity principle.
- **N7 steelman:** the strongest counterargument is that the physically
  realized matter sector should be the whole kernel, so the extra `K0` modes
  should disqualify `K0`. That would select `K1`, but it is exactly the missing
  kernel-exactness/no-extra-sector requirement, not a consequence of the linked
  carrier-count rows.
- **N8 cross-cycle echo:** this has the same shape as earlier selector walls:
  a carrier theorem can be true on an embedded surface without selecting the
  realizing dynamics. The note preserves the missing bridge as a residual.

## Runner Checks

The runner checks:

- branch construction, Hermiticity, and uniform plaquette fluxes;
- zero-mode counts and symbol-surface matching at `L = 4, 8, 12`;
- the point-zero scalar comparator;
- gap failure at `m = 0` and exact branch-neutral gap under `m epsilon`;
- branch-identical locality/range data and a computed density-of-states
  separator;
- carrier-conditional `M_3(C)`, commutant, and count readouts on both
  branches;
- kernel-global commutants and count readouts on both branches;
- text checks for the linked count-row carrier quantifiers;
- Record/readout conditionality;
- non-vacuity: adding the missing point-zero/kernel-exactness clause selects
  exactly `K1`, and dropping it restores the pass/pass tie.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  Lattice, Quantum, and Record baseline. Record is used only for its
  conditional readout boundary.
- [P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10.md](P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10.md)
  supplies the parent route scope and named residuals.
- [U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md](U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md)
  supplies the single-mode per-site one-particle surface.
- [TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
  supplies the finite periodic Fock/translation setting.
- [AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
  is the tested clustering candidate.
- [TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
  is the tested log-transfer/quasilocality candidate.
- [THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md),
  [THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md](THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md),
  and [THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  are the tested count/no-proper-quotient candidates.
- [THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  and
  [STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  supply the Hamming/carrier vocabulary instantiated by the runner.
- [RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md](RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md)
  is the tested record-function candidate.

## Command

```bash
python3 scripts/p_flux_point_zero_set_check_2026_06_10.py
```

Expected deterministic summary:

```text
TOTAL: PASS=22 FAIL=0
```

## Honest Status

```yaml
claim_type_author_hint: no_go
claim_scope: "On the two finite NN flux branches tested here, the linked spectral/clustering, count/no-proper-quotient, and Record/readout candidates do not supply the point-like-zero-set or kernel-exactness selector. The finite separator is computed, but the missing selector clause remains separate input."
upstream_dependencies:
  - minimal_axioms
  - p_flux_selection_from_matter_content_narrow_no_go_note_2026-06-10
  - u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20
  - tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25
  - axiom_first_cluster_decomposition_theorem_note_2026-04-29
  - transfer_matrix_log_quasilocality_narrow_theorem_note_2026-06-10
  - three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02
  - three_generation_observable_count_corollary_note_2026-05-03
  - three_generation_observable_theorem_note
  - three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10
  - staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17
  - record_function_finite_sector_algebra_2026-06-05
admitted_context_inputs: []
source_sets_audit_outcome: false
```
