# Color-Einselection Pointer-Frame Fork as a Unistochastic Criterion

**Date:** 2026-06-09
**Claim type:** bounded_theorem (finite-dimensional channel criterion)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_color_einselection_pointer_frame_unistochastic_criterion_2026_06_09.py`](../scripts/frontier_color_einselection_pointer_frame_unistochastic_criterion_2026_06_09.py) (PASS=28 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_color_einselection_pointer_frame_unistochastic_criterion_2026_06_09.txt`](../logs/runner-cache/frontier_color_einselection_pointer_frame_unistochastic_criterion_2026_06_09.txt)

## Scope

This note is a finite-dimensional criterion for a color carrier with:

- one named record frame `B = {|e_i>}`;
- complete projective dephasing `D_B(X) = sum_i P_i X P_i`;
- a coherent matter color unitary `U` between record steps.

The one-step predictability-sieve channel is

`Phi(rho) = D_B(U rho U^dagger)`.

The note answers a narrow fork: under this supplied single-frame channel, when
does color polarization survive and when does the diagonal color state relax to
`I_3/3`?

The result is a criterion and relocation only. It does not derive the record
frame, the matter unitary, a continuous-time generator, a rate, a link-step
measure, a blocking isometry, or an action/source bridge from Record or from
the minimal axioms.

## The Criterion

Define the unistochastic transition matrix

`T_U[i,j] = |<e_i|U|e_j>|^2`.

Then:

1. `Phi` maps every state into the `B`-diagonal subalgebra in one step.
2. On diagonal states, `Phi(diag p) = diag(T_U p)`.
3. `T_U` is doubly stochastic for every unitary `U`, so `I_3/3` is always a
   fixed point.
4. Fixed points of `Phi` are exactly the `B`-diagonal states whose probability
   vector is stationary for `T_U`.
5. If `T_U` is reducible, color information survives in more than one
   stationary sector and the channel does not depolarize to `I_3/3`.
6. If `T_U` is irreducible but periodic, the fixed point is unique but
   pointwise relaxation can fail; the cyclic-permutation witness oscillates,
   while its Cesaro average is `I_3/3`.
7. If `T_U` is Perron primitive (irreducible and aperiodic), then
   `Phi^n(rho) -> I_3/3` for every initial state after the first dephasing
   step. A strictly positive `T_U` is a sufficient condition.

Equivalently: a single named record frame does not by itself decide the color
pointer-frame question. The decision is supplied by the matter unitary's
mixing of that frame, as captured by `T_U`.

## Regimes

- **Commuting limit.** If `U` is diagonal in `B`, then `T_U = I`. The entire
  `B`-diagonal simplex is fixed; frame `B` is a stable pointer frame and
  generic color polarization survives.
- **Reducible transition matrix.** If `U` is block diagonal relative to `B`,
  then `T_U` has multiple communicating classes. More than one stationary
  sector survives, so the channel does not depolarize to `I_3/3`.
- **Irreducible periodic transition matrix.** A cyclic-permutation unitary has
  a unique stationary distribution but no pointwise convergence. This
  separates fixed-point uniqueness from relaxation.
- **Perron-primitive transition matrix.** If `T_U` is irreducible and
  aperiodic, then the unique pointer state is `I_3/3` and the channel relaxes
  to it. If all amplitudes of `U` in frame `B` are nonzero, this condition is
  satisfied.

## Order Parameter

The runner uses the same reduced-color order parameter as the adjacent
depolarization work:

`P(rho) = Tr(rho^2) - 1/3 = ||traceless(rho)||_F^2`.

For the strictly positive transition witnesses tested in the runner, `P`
decreases monotonically to zero. For a general Perron-primitive transition
matrix, the load-bearing statement here is convergence to `I_3/3`; this note
does not require a one-step strict Lyapunov theorem for every primitive matrix.

## Relation to Adjacent Gauge-Dynamics Work

The landed block-04 note
[`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md`](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md)
narrows Ad-invariant link-step support to the unpolarized matter color density
condition `rho_color = I_3/3`. This note supplies a conditional route by which
a single named record frame plus a sufficiently mixing matter unitary can
produce that density.

This is not a claim that Record supplies the frame or the unitary alignment.
Record supplies no readout context, decomposition, sector-generation rule,
dynamics, probability rule, normalization, source/action, scale, or arbitrary
observable identification. The record frame remains a named instrument input,
and Perron-primitivity of `T_U` remains a matter-realization input.

## What This Relocates

The open input is no longer "must a second record instrument be admitted?" in
this supplied channel. A second instrument is sufficient but not necessary.
The narrower open input is:

> Does the derived matter color unitary mix the admitted record frame so that
> `T_U` is Perron primitive?

That is a concrete condition for a later matter-realization lane. This note
does not deliver that condition.

## Guards

- **Covariance is not contraction.** The identity channel is `SU(3)`-covariant
  and inert. Covariance alone does not imply depolarization.
- **Single-frame depolarization is conditional.** It requires the named record
  frame and Perron-primitivity of `T_U`; neither is supplied by Record.
- **Fixed-point uniqueness is not relaxation.** Irreducibility alone is not
  enough; aperiodicity is also needed for pointwise relaxation.
- **No open input is discharged.** ADM-1, a continuous-time generator/rate,
  R2 delivery, blocking isometry, and any theory ranking remain untouched.
- **No framework primitive is added.** "Perron primitive" is the standard
  finite Markov-chain term for irreducible and aperiodic transition matrices;
  it is not a framework primitive or accepted premise.

## Load-Bearing Inputs

- [GRAPH_FIRST_SU3_INTEGRATION_NOTE.md](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) -
  color action and invariant-density context.
- [RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md) -
  Record supplies no continuous Markov generator, rate, weighting, or
  normalization.
- [RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md) -
  generator embeddability boundary.
- [RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md) -
  record formation and frame/instrument choice are not forced by the minimal
  axioms.
- [MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md) -
  adjacent block-04 unpolarized-density condition.
- [RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md) -
  named record-instrument context.
- [PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md](PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md) -
  persistent record-instrument context.

## Computed Content

The runner checks the finite `3 x 3` color channel directly:

- one-step diagonalization and CPTP behavior;
- diagonal action `Phi(diag p) = diag(T_U p)`;
- double stochasticity of `T_U`;
- fixed point `I_3/3`;
- commuting, reducible, periodic, and Perron-primitive regimes;
- order-parameter contraction in strictly positive witnesses;
- covariance-not-contraction guard;
- diagonal-phase dressing invariance of `T_U`.

Random states are witnesses only; the decisive identities are finite matrix
identities. No Monte Carlo fit, external measured value, axiom, primitive, or
audit verdict is imported.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only status
authority.
