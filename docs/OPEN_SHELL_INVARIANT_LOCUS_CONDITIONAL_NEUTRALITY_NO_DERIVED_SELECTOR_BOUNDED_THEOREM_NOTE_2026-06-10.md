# Open-Shell Invariant-Locus Neutrality and No Derived Selector Bounded Theorem

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** conditional theorem on the supplied `C^3` carrier, the
named color-diagonal hopping, the half-filled open-shell ground manifold, and
the named color-blind instrument class. It proves neutrality on the
`SU(3)`-invariant locus, shows the derived structure does not select either the
invariant locus or its complement, and supplies a continuous all-site invariant
order parameter for departure from the locus.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_open_shell_invariant_locus_no_derived_selector_2026_06_10.py`](../scripts/frontier_open_shell_invariant_locus_no_derived_selector_2026_06_10.py)
(expected `TOTAL: PASS=17 FAIL=0`; deterministic exact linear algebra/numerics,
no Monte Carlo).

## Result

The runner establishes four scoped facts on the finite open-shell surface.

1. **Invariant-locus neutrality.** The half-filled open-shell ground manifold
   is `SU(3)`-invariant and decomposes as `4 x singlet + 2 x octet` in the
   tested normalization. The commutant dimension is exactly `4^2 + 2^2 = 20`.
   Every invariant density in that commutant has per-site color marginal
   `I_3/3`, so all-site neutrality follows on the invariant locus.
2. **No derived selector.** The named hopping, color-blind instruments, and
   count/Casimir conservation laws commute with the global `SU(3)` action.
   The invariant locus is stable through an interleaved Hamiltonian-plus-record
   step, but color-blind records also preserve a non-invariant state's per-site
   color marginal. Thus the derived structure preserves the locus if supplied
   and preserves a departure if supplied; it selects neither direction.
3. **Continuous all-site order parameter.** The runner uses
   `D = max_x (Tr(rho_color(x)^2) - 1/3)`, the worst-site purity excess.
   `D` is `SU(3)`-invariant, two-copy estimable per site, zero on the
   invariant locus, positive on a non-invariant ground state, and continuous
   along convex mixtures into the invariant state. Single-site readings are
   not faithful; the separator must be all-site.
4. **Existence-only equipartition witness.** `P_gs/20` is an invariant neutral
   existence witness. No realization, weight, measure, or selector is assigned.
   The runner also checks that a broken state's exact invariant average has a
   non-flat manifold spectrum, so this witness is not a hidden twirl of that
   exhibit.

The remaining open question is which locus the realized state occupies. The state-conditioning here is the registered [`realized_state_primitive`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) interface: pointwise evaluation at the supplied law-admissible realized state, nothing more; the state-contingent data quoted remain registered data per its counterfactual clause. This
note does not answer that question.

## Inputs and Boundary

| Input | Role | Boundary |
|---|---|---|
| [`COLOR_NEUTRALITY_ENTANGLEMENT_DEPOLARIZATION_IS_GLOBAL_INVARIANT_NOT_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_NEUTRALITY_ENTANGLEMENT_DEPOLARIZATION_IS_GLOBAL_INVARIANT_NOT_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md) | global-invariance neutrality context | not promoted; the runner recomputes the finite open-shell claim |
| [`COLOR_PURITY_DOES_NOT_REDUCE_TO_PAST_HYPOTHESIS_SLOT_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_PURITY_DOES_NOT_REDUCE_TO_PAST_HYPOTHESIS_SLOT_NARROW_THEOREM_NOTE_2026-06-09.md) | past-hypothesis non-reduction context | no initial-condition selector is imported |
| [`RELATIVE_ORIENTATION_FUSION_STATE_SELECTION_POINTER_FRAME_ONE_VACUOUS_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](RELATIVE_ORIENTATION_FUSION_STATE_SELECTION_POINTER_FRAME_ONE_VACUOUS_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-06-10.md) | frame-naming exception context | used only to mark the color-blind instrument boundary |
| Standard finite-dimensional representation theory | isotypic decomposition, commutant dimension, Schur-style neutrality | all used finite facts are recomputed by the runner |

This note adds no framework premise, measure, weight, probability rule,
initial-condition selector, thermodynamic-limit claim, spontaneous-symmetry-
breaking claim, or empirical input. It is conditional on the named finite
surface and instrument class.

## No-Go Discipline Gate

**N1 -- Alternative routes tested.** The invariant-locus route is tested and
does give neutrality. The non-invariant ground-state route is tested and still
sits at the ground energy. Color-blind record steps are tested and preserve the
non-invariant marginal rather than depolarizing it. The equipartition witness is
tested only as an existence witness. The frame-naming instrument route is tested
as an exception to color-blind equivariance.

**N2 -- Wall independence.** Neutrality on the invariant locus, absence of a
derived selector, and the all-site order parameter are independent. Proving
one does not choose the realized locus.

**N3 -- Hidden-wall scan.** The carrier, hopping, ground manifold, global
`SU(3)` action, and instrument class are explicit inputs. The theorem imports
no weight, measure, initial condition, or dynamics selector.

**N4 -- Residual matching.** The residual addressed here is the open-shell
state-locus question. The theorem narrows its shape; it does not claim the
realized state lies in either locus.

**N5 -- Rhetoric audit.** "No derived selector" means no selector from the
named finite derived structure. It is not a no-go against future dynamics,
state-preparation, or initial-condition work.

**N6 -- Partial-closure path scan.** A future theory could still supply a
state-realization rule or dynamics that selects a locus. This theorem leaves
that path open.

**N7 -- Steelman.** A hostile reviewer could argue that invariant-locus
neutrality is physically irrelevant unless a formation rule puts the state
there. Correct: this note proves the conditional locus theorem and does not
derive the formation rule.

**N8 -- Cross-cycle echo.** Prior color-neutrality and pointer-frame work
separate global-invariant content from local frame and initial-condition
content. This note preserves that separation.

## Reproduction

```bash
python3 scripts/frontier_open_shell_invariant_locus_no_derived_selector_2026_06_10.py
```

Expected scorecard: `TOTAL: PASS=17 FAIL=0`. A passing run supports only the
finite-surface invariant-locus neutrality, non-selection, order-parameter, and
existence-witness claims stated above.
