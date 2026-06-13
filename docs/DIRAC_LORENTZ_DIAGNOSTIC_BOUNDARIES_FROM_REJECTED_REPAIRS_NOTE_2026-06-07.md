# Dirac/Lorentz Diagnostic Boundaries from Rejected Repairs

**Date:** 2026-06-07
**Claim type:** open_gate
**Type:** open_gate / diagnostic boundary
**Status authority:** independent audit lane only. This note captures useful
science from rejected PRs #3015 and #3020 without repairing or promoting their
overstrong claims.
**Primary runner:** [`scripts/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.py`](../scripts/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.py)
**Cached runner output:** [`logs/runner-cache/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.txt`](../logs/runner-cache/frontier_dirac_lorentz_diagnostic_boundaries_2026_06_07.txt)

## Scope

This packet preserves two narrow facts:

1. The common-analytic-vector repair route in
   [`FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md)
   fails exactly where the audit said it fails. A rapidity Gaussian is an
   analytic vector for the boost generator `K = -i d/dzeta`, but it is not an
   analytic vector for `H = M_perp cosh(zeta)`.
2. The continuous-time Lorentz route has a useful invariant-counting boundary.
   On the native spatial `Z^3` surface there is one spatial quadratic speed
   coefficient, while a Euclidean `Z^3 x Z_tau` surface has two coefficients
   (`c_t`, `c_s`) unless an extra 4D hypercubic/normalization premise is
   supplied.

These facts are diagnostic/open-gate material. They do not establish an
infinite-dimensional Nelson commutator theorem, a unitary Poincare
representation, interacting Lorentz naturalness, or a full emergent-Lorentz
theorem.

## Rejected-PR salvage

PR #3015 contained a valuable falsity localization: the Gaussian used in the
failed self-adjointness note cannot be a common analytic vector for `K` and `H`.
That survives intact. The finite Hermite-truncation evidence for a Nelson
commutator repair is not retained here, because stable finite truncations do not
prove the needed infinite-dimensional operator/form bounds.

PR #3020 contained a useful route distinction: the marginal `c_t/c_s` anisotropy
is manufactured by treating time as a fourth lattice coordinate. The native
framework surface in [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
has spatial `Z^3`; continuous time, if supplied by a self-adjoint Hamiltonian,
does not add an independent temporal lattice spacing. This is not a derivation
of the Hamiltonian or of interacting Lorentz invariance.

## Runner checks

The runner verifies:

- `||K^n psi||/n!` decreases for the rapidity Gaussian at the sampled orders,
  while `||H^n psi||/n!` grows rapidly under the corrected `exp(-x^2)`
  Gaussian quadrature.  The runner also includes an analytic lower bound:
  on the interval `zeta = n/a + u`, `u in [0, 1]`, the inequality
  `cosh(zeta) >= exp(zeta)/2` gives
  `||H^n psi||/n! >= (mass/2)^n exp(n^2/(2a) - a/2)/n!`, which diverges.
  The old common-Gaussian analytic-vector bridge is therefore false.
- signed-permutation orbit counting gives one diagonal quadratic invariant for
  spatial `O_h`, two for `O_h x time-parity`, and one for the 4D hypercubic
  group.
- the free continuous-time lattice dispersion
  `E^2(p) = sum_i sin^2(p_i a)/a^2` has one quadratic speed coefficient and its
  first spatial anisotropy at the `p^4` term.

## Primitive-registry firewall

The 2026-06-13 source repair makes the audit caveat explicit rather than
leaving it to inference. The runner loads the current non-isolated premise
allowlist `docs/audit/data/axiom_premise_nodes.json` and checks that this
diagnostic packet's load-bearing premise set is only `minimal_axioms`, used for
the native spatial `Z^3`/one-site algebra surface.

The approved primitives are re-checked but not used as load-bearing inputs:

- `scale_reference_primitive` is units conversion only; no dimensionless scale
  or `a/l_P` identification enters this packet.
- `kinetic_isotropy_primitive` supplies only the structural OS0 kinetic-form
  ratio; it does not supply a self-adjoint Hamiltonian, an interacting Lorentz
  theorem, a radiative-naturalness theorem, or the rejected Nelson repair.
- `realized_state_primitive` supplies only a pointwise realized-state interface;
  no realized-state data, selection rule, probability measure, typicality
  predicate, or state-contingent value enters this packet.

Thus no registered primitive is load-bearing for the audited diagnostic scope.
The open gates below remain open.

## Open gates

- An actual self-adjointness repair still needs an analytic proof of the
  infinite-dimensional comparison-operator and commutator form bounds, not only
  finite Hermite evidence.
- A continuous-time route still needs the supplied dynamics gate: the framework
  must provide or admit the self-adjoint Hamiltonian surface.
- Interacting radiative naturalness remains outside this note. The runner only
  captures free/tree-level invariant counting and dispersion diagnostics.

## Dependencies

- [`FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md)
- [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

**No-promotion statement:** this note does not change the audit status of any
dependency. It is an open-gate diagnostic packet for later theorem repair.
