---
claim_id: scale_ladder_gravity_burn_and_turn_source_tensor_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Exact covariance identity for supplied algebraic traffic statistics on finite direction sets, group velocity on differentiable eigenbranches, finite smoothed packet diagnostics and finite clock-comparator observations; no realized front process or physical source identification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/scale_ladder_gravity_burn_and_turn_source_tensor_2026_10_21.py
---

# Burn and turn contributions to a supplied walk tensor

Claim type: bounded_theorem.
Status: proposed_retained
Primary runner: `scripts/scale_ladder_gravity_burn_and_turn_source_tensor_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are context only: they choose none of the walks, coins, traffic statistics or tensor assignments below. “Burn” and “turn” name the supplied tensor contributions. This note establishes conditional algebra and reports finite deterministic diagnostics; a process of realized fronts is not constructed.

## Supplied model and exact target

A deterministic lossless walk has components labelled by a finite set of step directions d. Each tick a unitary site coin C mixes them, then each component moves one link along its d. Let P_d be the component Born densities and rho their sum. The supplied exchange traffic is 2 eps P_d P_d' / rho for ordered pairs d != d'. For rho=0 its value is defined as zero. Nonnegative traffic requires eps>=0; for negative eps only a signed algebraic identity remains.

The burn tensor is eps sum_d P_d d d^T. Each unit of assigned traffic contributes -(d'-d)(d'-d)^T/4 to the turn tensor. For packets the runner also supplies a net-redistribution array from the coin's density change D=P'-P: neg(D_d) pos(D_d') / sum pos(D), with zero array when the denominator vanishes. These are statistics assigned to the deterministic walk, not a one-turn transition coupling or a demonstrated multiple-jump process.

The exact target is: for any normalized nonnegative P on a finite direction set and real eps, burn plus exchange-turn equals eps v v^T, where v=sum_d P_d d. At eps>=0 the exchange coefficients are nonnegative. Zero probabilities and eps=0 are included.

## Plane-wave identity and group velocity

For independent directions d,d' with law P,

    E[(d'-d)(d'-d)^T] = 2(E[d d^T] - v v^T).

Consequently, summing all ordered pairs (the diagonal terms vanish),

    turn = -sum_{d != d'} 2 eps P_d P_d' (d'-d)(d'-d)^T/4
         = -eps(E[d d^T] - v v^T),
    burn + turn = eps v v^T.

This proves every component including shear, without a path-realization premise. For a normalized differentiable eigenpair U(k)u(k)=exp(-i omega(k))u(k), U(k)=diag(exp(-i k.d))C with k-independent C, differentiation gives d_j omega = u^* C^* D_j C u. The eigenmode condition implies |(Cu)_d|=|u_d|, hence d_j omega=sum_d |u_d|^2 d_j. A simple eigenvalue suffices locally; at a degeneracy the eigenvector must belong to the chosen differentiable eigenbranch. An arbitrary eigenvector in a degenerate eigenspace does not suffice.

The runner checks the tensor identity and finite-difference eigenbranch velocities on a two-component line walk, a six-direction walk on Z^3 and a supplied eight-body-diagonal walk. No D4 carrier identification is made. At the sampled points the burn-only tensor has nonzero discrepancies, including absolute errors about .019–.05 in 1D; no uniform “order one” estimate is claimed.

## Turn trace and finite clock comparator

The turn trace is **-eps(E[|d|^2]-|v|^2)**. The positive assigned turn action is its negative. On the line |d|=1, so action=eps(1-v^2). For the supplied two-component coin with angle theta, cos(eps)=cos(theta)cos(k), and

    1-v^2 = sin(theta)^2 / sin(eps)^2,
    action / (theta^2/eps) = eps^2 sin(theta)^2 / (theta^2 sin(eps)^2).

The runner compares action with the supplied continuum-motivated comparator theta^2/eps at theta=.05 and k=0,.03,.06,.12; all four relative discrepancies are below 1%. In a continuum dispersion E^2=m^2+p^2 with gamma=E/m, m/gamma=m^2/E. Substituting m=theta and E=eps motivates the comparator but does not make finite lattice eps an exact relativistic energy. Its coefficient is separately checked by exact rational arithmetic, including theta=3/10, eps=1/2 giving 9/50; a discrepancy test alone cannot validate this normalization.

At theta=.3, |k|=.3, on the tracked six-direction branch along (1,1,0) and (1,1,1), **each** of the two action/comparator discrepancies exceeds 5%. The runner checks both, not their maximum. These are two finite observations, with no clock classification for other bands, readouts, normalizations or the eight-direction walk.

## Finite packet diagnostics

The packet Born densities are those of the deterministic coin-and-shift walk. The runner forms the assigned traffic tensor, the coin impulse eps sum_d d(P'_d-P_d), and the post-coin burn stress. It Gaussian-smooths these fields with half the packet width and compares impulse plus the centered-difference divergence of the turn stress, relative to the centered-difference divergence of the burn stress. This centered proxy is not an exact time-placed link conservation law.

On the line, widths 30,60,120 give decreasing relative residuals (about .0802,.0409,.0191) while the relative impulse norm is about .440,.427,.415. On the six-direction walk along (1,1,0), widths 3,5,8 give residuals about .284,.188,.115 and relative impulse norms about .922,.933,.943. The periodic sizes, tick windows and smoothing choices are fixed in the runner. These finite observations do not prove an asymptotic rate or exact local packet conservation.

## Preserved counterexamples and open bridges

- One-turn traffic overdraw: theta=eps=.05 and psi=C^*(0,1) give P_+=sin(.05)^2=.00249791736 and P'_+=0, but exchange plus required outgoing net traffic is .00274708514, exceeding available P_+. A separate admissible process would need a construction and hypotheses; it is not supplied here.
- At eps=-.05 and P=(.5,.5), exchange traffic is -.025. This is why the nonnegative-traffic interpretation requires eps>=0.
- For C=I at k=0, the equal-superposition eigenvector has mean step zero while the two eigenbranches have slopes +1 and -1. This preserves the differentiable-eigenbranch restriction above.
- Taking theta to zero at fixed k=1 gives action/comparator ratio tending (1/sin(1))^2=1.412282927, not one. A small-angle limit alone is insufficient; the displayed ratio tends one in the joint small-theta, small-k regime. The numerical claim remains the four stated samples.
- Independent finite periodic data exhibit an exact link-balance error about 3.47e-18 but centered-proxy error .0155043. The proxy diagnostic is therefore not used as an exact local conservation certificate.

The coins, directions, exchange coefficient, per-turn stress, phase/band choice and eps, packet envelopes, smoothing and comparator are supplied mathematical choices. The six-direction dispersion is anisotropic. No observed physical data enter. Physical source identification, a realized front process, gravity dynamics and a physical clock law remain unproved.

## Current claim status and repair record

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: physical source identification and front-process realization are not established
source_of_blocker_text: review_loop
reachability_to_target: conditional tensor algebra and finite diagnostics only
artifact_role: conditional algebraic support
next_trace_action: specify and check any proposed physical or stochastic-process bridge separately
conditional_surface_status: supplied finite walk and traffic statistics
hypothetical_axiom_status: none introduced
admitted_observation_status: none
claim_type_reason: covariance identity under explicit mathematical inputs plus finite numerical diagnostics
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

A downstream consumer is not identified here. This repair withdraws the asserted realized front process, unrestricted eigenvector/group-velocity identification, positive stress trace, exact packet conservation, D4 identification and universal clock conclusion. It preserves the conditional covariance proof and the counterexamples above. The two-point clock predicate is strengthened and comparator normalization is tested separately. The candidate-law register is removed from the input closure; minimal axioms remain contextual. No independent audit outcome is prescribed.

Reproduce with `python3 scripts/scale_ladder_gravity_burn_and_turn_source_tensor_2026_10_21.py`. Successful bounded diagnostics do not establish any of the open physical bridges.
