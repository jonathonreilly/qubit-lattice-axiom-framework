# W-Native Induced Vacuum Stress Tadpole Boundary

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:** [`scripts/frontier_universal_gr_induced_cosmological_constant.py`](../scripts/frontier_universal_gr_induced_cosmological_constant.py)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_induced_cosmological_constant.txt`](../logs/runner-cache/frontier_universal_gr_induced_cosmological_constant.txt)

## Summary

This note records a bounded stress-tadpole result in the W-native induced-gravity
program. The finite Brillouin-zone runner finds:

- an O(1) vacuum energy density in lattice units;
- a nonzero vacuum stress tadpole proportional to `delta_mu_nu` to numerical
  precision;
- no cancellation of that tadpole inside the computed finite induced-action
  term.

The clean positive sub-result is the SO(4)-isotropy of the computed vacuum
stress: the object has cosmological-constant form in the checked sector, not a
preferred-frame stress. The negative boundary is narrower than the submitted PR:
the runner does not model record-ontology unobservability, unimodular or
sequestering dynamics, counterterm subtraction, or the full gravitational
backreaction problem. Those remain open mechanisms, not failed mechanisms.

## Runner-Verified Result

On the staggered Kahler-Dirac finite carrier used by the W-native induced-gravity
packets, the runner checks:

- **T1 finite vacuum energy:** the lattice Brillouin zone regulates
  `eps_vac = -<log(m^2 + sum_mu sin^2(P_mu/2))>_BZ`, giving O(1) lattice-unit
  values `-0.667`, `-0.866`, `-1.068` for `m = 0.3, 0.7, 1.0`.
- **T2 isotropic vacuum stress:** the finite stress tadpole is nonzero and
  proportional to the Euclidean metric in the checked carrier:
  `diag = [0.8744, 0.8744, 0.8744, 0.8744]`, relative isotropy spread
  `3.8e-16`, maximum off-diagonal `6.5e-17`.
- **T3 no cancellation in this computed term:** the computed tadpole is O(1) and
  nonzero. If it is coupled to a metric in the ordinary induced-action way, it
  has cosmological-constant form. The runner does not prove that this coupling
  survives every possible record, sequestering, unimodular, or subtraction
  mechanism.

`TOTAL: PASS=3 FAIL=0`.

## Scope

This is a bounded theorem about a finite induced-action term. It establishes the
presence and SO(4)-isotropy of the vacuum stress tadpole in the checked W-native
fermion-loop sector.

It does **not** establish a final framework-level cosmological-constant no-go.
In particular, it does not prove:

- that an absolute uniform vacuum energy is observable in the Record sense;
- that unimodular or sequestering mechanisms are absent;
- that no counterterm, subtraction, or renormalization condition can remove the
  tadpole;
- that the induced Newton coupling and full backreaction problem are closed;
- that the observed cosmological constant is predicted or contradicted.

Using the `scale_reference_primitive` as a units conversion, an O(1) lattice-unit
vacuum stress would correspond to an O(`M_Pl^4`) scale. That is a scale reading,
not an observed-Lambda comparison and not a proof that the framework has no
resolution.

## No-Go Discipline Gate

This section applies the no-go discipline to the broad negative reading. The
submitted broad claim "the framework inherits the cosmological-constant problem
with no resolution" is **not** landed. The landed negative claim is only:
"the computed finite induced-action tadpole is nonzero and unsuppressed inside
the checked term."

- **N1 alternative routes:** direct zero/cancellation in the computed tadpole,
  anisotropic-vacuum evasion, mass-window sensitivity, record unobservability,
  sequestering/unimodular decoupling, counterterm subtraction, and full
  gravitational backreaction were considered. The runner directly addresses only
  the first two and samples the third; the remaining routes are open.
- **N2 wall independence:** the computed tadpole, observability, coupling to the
  conformal mode, and observed-Lambda matching are distinct residuals. This note
  closes only the computed-tadpole residual.
- **N3 hidden-wall scan:** "gravitates" is not used as an unconditional source
  verdict. The source note states the conditional induced-action reading instead.
- **N4 residual matching:** the W-native stress-coupling notes support the
  stress-tensor context; they do not by themselves close record/sequestering
  routes.
- **N5 rhetoric audit:** the phrase "cosmological-constant problem" is used only
  for the ordinary induced-action interpretation of a nonzero isotropic vacuum
  stress, not as a final framework no-go.
- **N6 partial-closure scan:** record ontology, unimodular gravity, sequestering,
  and subtraction/renormalization are explicit open partial-closure routes.
- **N7 steelman:** a uniform vacuum stress may decouple from observables or from
  the conformal mode in a future retained theory. That would defeat the broad
  no-solution claim, so the broad claim is not shipped.
- **N8 cross-cycle echo:** prior framework repairs have retired apparent walls
  by clarifying premise class or observable status. This note keeps the same
  possibility open for the cosmological-constant sector.

## Dependencies

- [UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  supplies the W-native stress-context boundary.
- [UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md](UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  supplies the induced-graviton finite-k context.
- [UNIVERSAL_GR_STAGGERED_TT_STIFFNESS_POSITIVE_BOUNDED_THEOREM_NOTE_2026-06-08.md](UNIVERSAL_GR_STAGGERED_TT_STIFFNESS_POSITIVE_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  records the adjacent staggered TT stiffness context.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) supplies
  units conversion only for the optional O(`M_Pl^4`) scale reading.

## No-Promotion Statement

This note sets no audit verdict and does not promote any gravity row. It adds a
bounded finite-runner result: the checked W-native induced-action sector has a
nonzero SO(4)-isotropic vacuum stress tadpole, and no cancellation appears inside
that computed term.
