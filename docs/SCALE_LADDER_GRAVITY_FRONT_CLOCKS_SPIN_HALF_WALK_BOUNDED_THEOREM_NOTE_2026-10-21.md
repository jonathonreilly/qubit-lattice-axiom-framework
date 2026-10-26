---
claim_id: scale_ladder_gravity_front_clocks_spin_half_walk_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite plane-wave and packet comparisons of supplied front tick rates on a supplied spin-1/2 split-step walk in 3D against m^2/eps; no physical clock law, gravitational redshift, derivation of the flip rule or empirical identification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/scale_ladder_gravity_front_clocks_spin_half_walk_2026_10_21.py
---

# Front clocks on a spin-1/2 walk in 3D

Claim type: bounded_theorem.
Primary runner: `scripts/scale_ladder_gravity_front_clocks_spin_half_walk_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the walk, coin or tick rules below. This note compares supplied tick rates with the rest frequency over gamma.

## Supplied walk and tick rates

The state has two chirality blocks of two components. Each tick a coin exp(-i th beta) mixes the blocks. Then shifts move each component one site along x, y and z according to the eigenvalue of alpha_i = diag(sigma_i, -sigma_i). For a positive-frequency eigenmode at momentum k with frequency eps, rest frequency m and group velocity v, the comparison target is m^2/eps. For a relativistic dispersion this equals m/gamma.

Four per-tick rates are compared:

- **product:** 4 eps pL pR;
- **geometric:** 2 th sqrt(pL pR);
- **coherent:** th psibar psi / psi^dag psi, evaluated at mid-coin, i.e. th times twice the real chirality overlap;
- **phase:** eps - k.v.

Here pL and pR are the chirality occupations. The first two count chirality flips by occupation; the third sets flips by the coherence between chiralities.

## Plane waves

Off the axes the two positive bands split. The runner evaluates each band separately at fixed k/th while th halves from .05 to .0125. Along (1,1,0) with k = th, (1,1,1) with k = 2 th and (2,1,0) with k = 2 th, the coherent rate's relative error roughly halves with each halving of th. The two bands carry errors of opposite sign. The phase rate's error is smaller still and falls faster on two of the three rays. These are finite decreasing-error observations at three angles, not an asymptotic convergence certificate or an error bound.

On the axes the bands are degenerate, so the spin state inside the degenerate pair is a free choice. The product and geometric rates change with that choice, while the coherent rate does not, to rounding. An occupation-counted flip clock therefore depends on spin orientation in this walk; the coherent rate does not.

## Packets

On a 48^3 torus with th = .1 the runner builds packets from the two positive bands with a Gaussian of momentum width .1. It does this for a packet at rest, one moving along (1,1,0), and two crossing head-on. It sums th psibar psi over sites and divides by the norm. Each signed total is within 3 percent of the actual normalized superposition's spectral average of m^2/eps. The comparator is sum_(k,b) |u_kb^dag F_k|^2 th^2/eps_kb divided by sum_k ||F_k||^2, where F is the Fourier transform of the final superposed packet and the positive-band vectors are orthonormal within each spectral subspace. Thus the reciprocal is taken per band, and superposition cross terms enter before normalization. Degenerate subspaces use orthonormal projectors; the original supplied packet construction is unchanged. The overlap is negative on part of the moving and crossing packets' weight. Summing its absolute value overshoots where the packets cross. A counting rule that ticks at the absolute overlap must therefore give its ticks the overlap's sign for the expected count to equal the signed total. The phase rate is positive on the tested plane-wave rays; packet-local phase counting is untested. Positivity does not extend to the full positive-frequency domain: at th=.1 and k=(-2.76429615,-1.19039056,1.37089841), a positive eigenfrequency eps=1.2892292751449 has phase rate approximately -.1678501083297.

## Scope

The walk, coin angle, mid-coin evaluation, band selection and packet construction are supplied. No clock law, gravitational redshift, derivation of the coherent flip rule or physical identification is established.

## Claim status and review record

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Physical clock identification remains open; downstream consumer not yet known.
source_of_blocker_text: frontier_question
reachability_to_target: Finite supplied-model comparison only.
artifact_role: bounded numerical support
next_trace_action: Independently review corrected spectral comparator and finite error checks.
conditional_surface_status: Supplied walk and tick rules only.
hypothetical_axiom_status: No new axiom adopted.
admitted_observation_status: No empirical observation imported.
claim_type_reason: Finite numerical observations under explicitly supplied choices.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The repair replaces the mean-frequency and separate-packet mean comparator with the per-band expectation in the actual superposition. It adds finite monotonic and error-ratio phase checks and withdraws an unrestricted phase-positivity sentence, preserving the counterexample above. The walk, M4 carrier, ordered shifts, coin, observables, comparator and packet selection remain supplied mathematical model choices; their physical bridges remain open. The minimal axioms do not select them. Original source is recoverable from PR 9832 head f30232ad08f0b0777c86559773421f8ac44af7ae. Independent affected-source confirmation and combined landing validation remain required; this author repair grants no review or audit verdict.
