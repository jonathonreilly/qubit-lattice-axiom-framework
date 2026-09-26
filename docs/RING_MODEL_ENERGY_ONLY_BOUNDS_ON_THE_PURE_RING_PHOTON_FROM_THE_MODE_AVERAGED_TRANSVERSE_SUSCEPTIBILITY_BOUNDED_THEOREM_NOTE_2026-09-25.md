---
claim_id: ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Conditional finite spectral moment inequalities in the supplied ring Hamiltonian, with real ground
  vector and centered transverse modes. Energy curvature equals the triple susceptibility only under the stated
  momentum-sector and symmetry hypotheses. Full finite-population simulations are biased diagnostics, not spectral
  enclosures, photon or phase conclusions; mixed population averages and fit errors are descriptive only.
upstream_dependencies:
- minimal_axioms
- ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
- ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
- ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_controlled_population_the_transverse_susceptibility_from_energies_bounds_the_photon_2026_09_25.py
---

# Conditional spectral-moment bounds and finite energy-curvature diagnostics

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

## Supplied model and exact inequality

Supply the link-qubit ice Hamiltonian `H=-sum_p(U_p+U_p†)` at g=1 on an L³ torus, and a real normalized ground vector in a selected connected flip component. The component ground vector is unique. Center every mode by removing its ground overlap; a disconnected-sector statement must remove all ground-space components instead. Write `N=L³`, `s²=2-2cos k`, and take the three modes `O_a=N^(-1/2) sum_(a-links) exp(ik x_(a+1)) sigma`, with axes cyclic.

Each plaquette orientation changes one of the three modes by squared magnitude `4s²/N`. For diagonal O, `[O†,[H,O]]_ij=-|O_i-O_j|² H_ij`. In a real ground eigenvector, the O and O† spectral numerators coincide; half the double-commutator expectation is either numerator. Averaging the triple gives `m1=2u s²`, where `u=sum_p<R_p>/(3N)=-E0/(3N)`. No cubic rotation symmetry is needed for this averaged identity. It is not an arbitrary-state f-sum.

For the positive excited-state measure `a_n=(1/3)sum_a |<n|O_a|0>|²`, let `m_j=sum_n a_n omega_n^j`, with `omega_n>0`. Assume nonzero spectral weight. Define the centered structure factor `S=m0` and spectral susceptibility `chi=2m_(-1)`. Weighted means and Cauchy-Schwarz give

`omega_min <= m0/m_(-1) <= sqrt(m1/m_(-1)) <= m1/m0`,

hence `omega_min <= 2s sqrt(u/chi)` and `S <= s sqrt(u chi)`. These exact inequalities concern the lowest excitation coupled to the chosen modes. They are not a lower bound on a photon speed. A mode with smaller energy and sufficiently small spectral weight is not excluded.

## Reading chi from energy

For the real probe `F=sum_(a-links) cos(k x_(a+1)) sigma`, second-order perturbation gives `E(h)=E0-h<F>-h²<F Q(H-E0)^(-1)Q F>+O(h³)`. To replace the resolvent expression by `3N chi/4`, additionally require a translation-invariant ground state/support, distinct nonzero mode momenta and absence of cross terms between them; realness pairs +k and -k. When `2k=0` modulo 2pi, the prefactor doubles to `3N chi/2`. An even expansion with O(h⁴) further needs a symmetry mapping F to -F while preserving the component and H. Zero winding alone does not establish all these properties. The exact L=2 control checks its actual mode responses; larger-torus energy fits assume the applicable symmetry sector.

Under the even-expansion assumption, at h and 2h the expression `(15E0-16E(h)+E(2h))/(12h²)` eliminates the quartic term and estimates the quadratic coefficient, with remaining order-h⁴ bias from the sixth-order term. For this triple the coefficient is `3 pref N chi/4`, pref=1 or 2. It is not N chi/4.

## Executed finite diagnostics

The retained runner computes the L=2 component's complete numerical eigensystem and residuals, centered spectral susceptibilities, the moment chain, and the finite-field fit. It also compares a compiled fixed-population projector with one 3646-state bounded-region component and runs the full original population and momentum grid (480/1920 walkers, projection 30, fields 0, 0.15, 0.30). Fresh stdout contains the actual estimates; original numerical tables remain recoverable from PR #9236 and are not separate exact evidence.

Local rate updates depend only on nearby plaquettes, but event selection sums a number of blocks growing with volume. The implementation does not prove constant total event cost. The L=2 diagonalization is a numerical control, not a rigorous enclosure; all moment supports are included instead of a truncated multiplet.

The mixed energy identity is exact for the ideal ground-state mixed distribution with any positive guide. Finite projection and fixed population do not achieve that distribution exactly, and subtraction does not guarantee bias cancellation. Loop-based initialization preserves zero winding but is not proved to stay in one plaquette-flip component; the larger runs can mix components. The bounded-region Hamiltonian is the supplied compressed operator, not an autonomous record-locking theorem.

At L=8 the reported grid combines four seeds at 480 walkers with four at 1920, while its u estimate comes from the lower population. This is a mixed-settings diagnostic, not eight iid 480-walker repetitions. Report the populations separately as the runner does before their pooled table. Energy E0 is reused across momenta within a seed, so fitted slopes, ratios and nominal z values have unaccounted covariance. The pooled seed/bin multiplier can be below one; taking the larger of two estimates is not a coverage guarantee. The bounds' displayed errors omit u uncertainty, field-fit truncation and systematic population/component errors.

Comparisons with earlier forward-walking values additionally compare six-mode and cyclic-triple averages. Equality requires the relevant cubic symmetry. Nominal deviations are not hypothesis exclusions. The finite estimates do not establish a nonzero or vanishing infinite-volume structure factor, a photon dispersion, rejection of all quadratic modes or a single-mode saturation law. The Gaussian parameter reading is an optional comparator ansatz, not a measured unique effective action.

## Evidence limits and No-Go Discipline Gate

- **N1:** finite supplied supports, positive spectral measure and explicit energy-response symmetries.
- **N2:** primary reproduction is distinct from independent mathematical controls.
- **N3:** Gauss constraint, ring dynamics, guide, sampling and probe are supplied.
- **N4:** current narrowed parents govern; historical filenames are identifiers.
- **N5:** numerical residuals and seeded estimates are not certified enclosures or calibrated statistical tests.
- **N6:** component connectivity, symmetry, projection/population convergence and smaller-field control remain open.
- **N7:** weak spectral weights, other sectors, non-Gaussian states, finite-size bias and correlated errors remain counterroutes.
- **N8:** retain exact inequalities and finite diagnostics; no physical selection or audit verdict.

## Verification and recovery

Run the primary script without --dry for the full original experiment. The small --dry settings are not a substitute for its reported grid. A failed control must be investigated. Original source, numerical tables and cache are frozen at PR #9236 head 874b0990d39d1c878674daa26aa856dc460556a9. Full source review found the response-domain, population-label, uncertainty and truncated-spectrum defects corrected above.

## Inputs

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [RING_MODEL_TWO_REGULATORS_A_REGION_BOUNDED_BY_RECORDS_MATCHES_THE_TORUS_AT_SIZE_EIGHT_AND_THE_WALKER_POPULATION_IS_THE_LARGER_REGULATOR_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_TWO_REGULATORS_A_REGION_BOUNDED_BY_RECORDS_MATCHES_THE_TORUS_AT_SIZE_EIGHT_AND_THE_WALKER_POPULATION_IS_THE_LARGER_REGULATOR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
