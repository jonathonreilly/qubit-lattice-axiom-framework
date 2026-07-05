# Interleaved Mean Map: Peripheral Count Collapse and Mean-Level Removal of the Record-Free Almost-Periodicity Obstruction

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** conditional theorem on the supplied `C^3` carrier, the
named quadratic hopping, the named color-blind record instrument class, and
supplied `(λ,τ)` instrument parameters. It proves a one-body mean-map spectral
collapse, count-form relaxation, and deflated-transient convergence. It does
not supply a continuous generator, a step measure, a probability/weight rule,
an instrument-selection rule, or any retained-status update.
**Script:** `scripts/frontier_interleaved_mean_map_peripheral_count_collapse_relaxation_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_interleaved_mean_map_peripheral_count_collapse_relaxation_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=14 FAIL=0`, exact,
deterministic, no MC.

## The wall, and what this note is — and is not

The continuous-generator residual is bounded by the record dynamics boundaries
[`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
and
[`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md).
The heat-kernel CLT still needs an i.i.d. central step measure. **This note is
not a step-measure delivery**: it gives no measure on `SU(3)`, and its central
finding, convergence of the induced orientation to a state-dependent limit, is
the opposite of the nonzero-variance spread the CLT premise needs.

What it does show is narrower: compose the exact one-body hopping closure
[`SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09`](SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
with the named record-channel rules
[`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md)
into the exact linear mean map `Φ = D_λ∘Ad_W` on the `81`-dimensional one-body
matrix space. The spectral analysis removes the record-free almost-periodicity
sub-obstruction from
[`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10`](INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md)
at the mean-map level only, and identifies the conserved quantities.

## The results (exact — runner `PASS=14 FAIL=0`)

**(M1) The peripheral count collapse — the new load-bearing structure.** `Φ`'s peripheral
spectrum is **exactly 3-dimensional**: the per-color uniform diagonals, i.e. **the
conserved color counts** — verified as exact fixed points, with the dimension count
closing the identification. The genuinely new content is the **collapse 9 → 3** driven by
the color-blind hop (the gap itself is per-step, per-color *decoherence damping* — a
single-color toy reproduces the same gap values; "mixing" in the forbidden
continuous-ergodic sense is neither claimed nor implied; the map is **discrete-time**
throughout). Gap values instance-labeled (`0.321` at `(λ,τ)=(0.45,0.35)`; `0.174` at
`(0.25,0.6)` — structure stable, values parameter-dependent: `λ, τ` are *supplied*
parameters of the named instrument admission). The matter mean **relaxes to the count
form** `ρ_color(x) = diag(N_c)/N`. This is the count-form reduction in
[`PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10`](PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10.md):
equal counts give the neutral marginal in that sharp-count reading, while the
state-realization/selector question remains the separate open-shell locus
boundary in
[`OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10`](OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md).
The mean link carrier dies at the derived dominant **per-step ratio**
(clean-window match; tolerance instance-labeled).

**(M2) The refuted shortcut** *(a one-body re-exhibit of block-02 content)*. One record
step is exact scalar damping on the cross-block — polar-invariant in isolation — but the
composition with the flow is **not** scalar: the induced orientation departs at order 1
within six steps. The polar-invariance shortcut is false; exhibited so it isn't retried.

**(M3) The removal of the almost-periodicity obstruction — the single load-bearing new
dent.** Along the interleaved mean trajectory, computed on **deflated genuine signal**
(`X ← (I−P_per)Φ(X)` with the oblique peripheral spectral projector; plain
renormalization lets `μ=1` round-off capture the iterate by `n≈100`): the induced
curvature `C(n)`
**converges** (last-century change `<10⁻⁸`; the limit value is **one realization's
number** — state-realization data, not a derived constant); the orientation converges
Cauchy-tight; the converged cross-block lies in the dominant family's cross-block image,
whose **rank is exactly 3** (the random control's expected residual for a
3-of-9 image is `√(1−⅓) = 0.816`; the check is dimension-counting, not a hidden
fit); and **the convergence rate is itself derived**: the orientation-error
log-slope matches `ln(|μ₂|/|μ₁|)` to a few percent (`−0.0176` vs `−0.0172` per step — an
un-deflated iteration gives a floor artifact). **Fixed-point qualification:**
the fixed point itself is *diagonal* and carries **no link**; the convergent
object is the polar **orientation of the vanishing centered transient** (a
scale-invariant direction), not a gauge configuration present at the fixed
point. The limit is **initial-state-dependent**: no universal selection is
claimed, matching the open-shell state-realization boundary linked above. The state-conditioning here is the registered [`realized_state_primitive`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) interface: pointwise evaluation at the supplied law-admissible realized state, nothing more; the state-contingent data quoted remain registered data per its counterfactual clause.

**(M4) Color-blind record erasure.** The color-blind per-site total-occupation
instrument's site-pinching is scalar **zero** on adjacent cross-blocks —
instant link erasure at instrumented sites — while the on-site color block is
preserved exactly. This is the one-body erasure content of the named record
instrument note linked above, re-exhibited in the present map.

## Where This Leaves the Generator and Step-Measure Residuals

- **Removed at mean level:** the record-free almost-periodicity sub-obstruction
  from the induced-holonomy note. With the named record channel interleaved, the
  centered induced trajectory relaxes at a derived per-step rate into a derived
  spectral subspace.
- **Untouched:** the retained continuous-generator boundaries. The map is
  discrete-time throughout; no continuous generator or rate law is claimed or
  implied.
- **Untouched:** the CLT step-measure premise. Nothing here supplies a
  distribution on `SU(3)`; mean convergence to a state-dependent limit marks
  how much is still missing, not progress toward a nonzero-variance central
  step spread. The link remains a slaved coordinate of one-body data.
- **Doors named:** the **stochastic unraveling** (outcome-resolved trajectories would
  carry the step distribution the CLT needs — requires outcome-weight/Born structure; a
  named separate thread); **structured/frame-naming instruments** (= the `{P_r}` root);
  **interactions** (non-quadratic terms break the one-body closure). Conditional
  on the supplied `C³` carrier, the named hopping, and the named instrument
  class; instrument existence and `(λ,τ)` are supplied parameters. No new axiom,
  primitive, measure, probability rule, or weight; `r` untouched. The audit
  lane grades.

## Cross-references

- Prior finite dephasing+unitary spectral context:
  [`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md)
  and
  [`RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md).
  M1 generalizes their fixed-point style to the full sites×colors one-body
  matrix with an exact peripheral-completeness statement; M2/M4 re-exhibit
  content from the named record-instrument source.
- The continuous-generator boundaries respected: `record_classical_semigroup_boundary_2026-06-06`
  (retained), `record_markov_generator_embeddability_boundary_2026-06-06`
  (retained_no_go).
- The almost-periodicity obstruction removed at the mean level:
  [`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10`](INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- The exact one-body rules composed:
  [`SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09`](SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  and
  [`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md).
- The count form:
  [`PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10`](PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- The state-realization clause:
  [`OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10`](OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- Standard math (method only): linear dynamical maps; peripheral spectra; oblique
  spectral projectors and deflation; projective/subspace iteration; non-normal matrix
  numerics.
