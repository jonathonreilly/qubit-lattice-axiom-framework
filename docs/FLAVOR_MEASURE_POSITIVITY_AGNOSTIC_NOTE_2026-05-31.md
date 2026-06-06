# Flavor Measure/Positivity Agnostic Note - three checked positivity/readout tests

> **2026-06-06 scope repair:** the earlier exhaustion and campaign-capstone
> language was too broad. This note is now scoped to the
> three algebraic checks actually run by
> `scripts/flavor_measure_positivity_agnostic_2026_05_31.py`: OS Gram
> positivity is blind to the 1-complex versus 2-real count in the tested free
> covariance, the qubit Bargmann complex structure is central and not the
> generation-doublet `J_cs`, and Hermitian readout gives
> `Q=(1+2r)/3` for the displayed `r` values. It does **not** claim that all
> symmetry-side or measure-side selectors have been ruled out, and it does **not**
> close `r=1/2`.
>
> **Packaging / supersession (2026-06-02):** the old finite-enumeration framing
> is superseded by `FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31`
> and the chain-of-custody
> `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`. Cite the
> chain-of-custody note for current flavor-lane status.

**Date:** 2026-05-31
**Claim type:** bounded_support
**Claim boundary:** three checked positivity/readout tests only; no complete selector theorem.
**Runner:** `scripts/flavor_measure_positivity_agnostic_2026_05_31.py`
(`SCORECARD PASS=3`, cache:
`logs/runner-cache/flavor_measure_positivity_agnostic_2026_05_31.txt`).
**Source:** 6-agent build `wf_9c630d58`, repaired to match the runner-backed scope.

## Question
With `J_cs` forced by the generation algebra, do the displayed
positivity/holomorphicity checks select the Kahler `det_C` count of `J_cs` and
fix `r=1/2`?

## Scoped Verdict
The displayed checks are agnostic to the `det_C` versus `det_R` count. This is
a narrow negative/support result, not a proof that every possible
positivity-side or symmetry-side selector has been ruled out.

1. **OS reflection positivity is blind to the tested count.** For the displayed
   free covariance, the OS Gram
   `<theta(f_i) f_j> = G(tau_i + tau_j)` is positive semidefinite for both the
   one-complex-field representation and the two-real-field representation.
   The runner checks both Gram matrices and finds nonnegative minimum
   eigenvalue up to numerical tolerance.

2. **The Bargmann descent uses the central qubit complex structure, not
   `J_cs`.** The qubit coherent-state complex structure is represented by the
   central `i I_3`. The generation-doublet structure
   `J_cs=(C-C^2)/sqrt(3)` is traceless with eigenvalues `{0,+i,-i}` on the
   generation space. The tested Bargmann route therefore does not select the
   `det_C` count on the generation doublet.

3. **Hermitian readout fixes the readout class, not the value of `r`.** The
   runner verifies the signed/Hermitian readout identity
   `Q=(1+2r)/3` for the displayed sample values
   `r in {0.3, 0.5, 1.0, 2.0}`. This supports the readout class used in the
   flavor lane, but it holds for every displayed `r` and therefore does not
   select `r=1/2`.

## What This Does Not Claim
- It does not close the `r=1/2` flavor-selection problem.
- It does not prove that all symmetry-side selectors have been ruled out.
- It does not prove that all measure-side or positivity-side selectors have
  been ruled out.
- It does not promote this row to an unbounded or retained result; independent
  audit remains required for any status change.

## Live Downstream Use
This row can be cited only as a narrow no-selection check for the three tested
routes. The live route for `r=1/2` remains the chain-of-custody framing: reduce
the value to the sharply located reality/statistics or cross-factor bit, then
derive or admit that bit separately. This note supplies evidence that the three
displayed positivity/readout checks alone do not perform that derivation.

## Stale-Citation Flags
- `axiom_first_reflection_positivity` and
  `osterwalder_schrader_from_framework` remain separate audit surfaces.
- `free_field_os_wightman_reconstruction` records the statistics-selection gap.
- `koide_real_rep_block_count_permitted_not_forced` and
  `koide_z3_equivariant_anticommuting_no_go` are background context, not
  authorities that make this row exhaustive.
