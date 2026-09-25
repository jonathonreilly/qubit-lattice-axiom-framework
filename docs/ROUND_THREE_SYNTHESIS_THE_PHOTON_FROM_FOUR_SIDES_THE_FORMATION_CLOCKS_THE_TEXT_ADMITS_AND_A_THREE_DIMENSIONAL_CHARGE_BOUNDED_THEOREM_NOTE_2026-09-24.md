---
claim_id: round_three_synthesis_the_photon_from_four_sides_the_formation_clocks_the_text_admits_and_a_three_dimensional_charge_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Ring sum rules, a dephasing criterion and a finite colored network: synthesis. Conditional identities
  and finite constructions only; all imported structures and unresolved wider inferences explicit.'
upstream_dependencies:
- gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
- minimal_axioms
- ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_continuously_bounded_theorem_note_2026-09-24
- ring_model_ice_transverse_weight_sum_rule_the_ring_term_moves_the_weight_from_the_smallest_momenta_to_the_zone_corner_without_a_growing_peak_bounded_theorem_note_2026-09-24
- ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
- ring_model_the_ten_cubed_point_lies_between_the_linear_and_level_readings_and_a_constant_plus_a_linear_term_fits_the_four_sizes_mildly_better_than_a_power_bounded_theorem_note_2026-09-24
- ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
- the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
runner: scripts/round_three_synthesis_one_identity_per_block_and_the_register_2026_09_24.py
---

# Ring sum rules, a dephasing criterion and a finite colored network: synthesis

**Type:** bounded_theorem

## Supplied setting

This note consolidates eight checks. All Hamiltonians, constraints,
kinematics, sectors, clocks and patterns are supplied constructions.
Only the identities and finite observations below are retained. No phase,
physical species, exhaustive clock classification or premise adoption is
conferred by this synthesis.

## Ring identities

For a real ground vector of H=-g A+V D in a connected flip component with
g>0, and diagonal O, the double commutator has entries
[O^dag,[H,O]]_ij=-|O_i-O_j|^2 H_ij. Its ground expectation is twice
the Rayleigh numerator when the conjugate modes give equal terms. For the
six axis/polarization modes normalized by 1/sqrt(N), their average is
2 g u s^2, u=<U+U^dag> averaged over all plaquettes, s=2sin(k/2).
The runner checks this on the 864-state component at g=1,V=0 and verifies
the eigenvector residual. It is not an identity for arbitrary-state
Rayleigh numerators or for individual orientations without further symmetry.
A gap bound also requires removing the full ground-space component from
O psi. Substituting finite-population estimates does not yield a rigorous
bound on the physical gap.

Parseval gives sum_k sum_a |O_a(k)|^2=3N for every spin-half ice basis
configuration in the runner's sigma=+/-1 normalization. Gauss law removes
the longitudinal component at nonzero k. At zero momentum it imposes no
condition on the three harmonic modes. The nonzero-zone average is
(3N-T(0))/(N-1), not identically 3; the all-zone total divided by N is 3.
Finite Monte Carlo samples check these configuration identities without
certifying mixing or the ground-state distribution.

At V=g>0 the component Hamiltonian is a graph Laplacian:
x^dag(D-A)x=sum_edges |x_i-x_j|^2 (with edge multiplicity).
It is nonnegative and annihilates constants on each component. There is
no unique global uniform state across disconnected components. Finite
walkers need not have equilibrated, and an RK identity does not bound
away-from-RK bias.

## Reduced oscillator comparator

For U,K>0, supply the nonzero transverse oscillator modes and omit both
longitudinal and harmonic zero modes. The quadratic theory then has
E covariance (sqrt(K/U)/2)(C^T C)^(1/2). Diagonalizing each positive mode
as a harmonic oscillator proves this formula. In the positive Fourier
convention g_a=(1-exp(-ik_a))/|s|, it is A|s|(I-gg^dag),
A=sqrt(K/U)/2. The runner's 4^3 curl matrix has kernel N+2 and checks the
formula. A normalizable full noncompact zero-mode vacuum has not been
constructed by simply assigning zero covariance there. Fixed U,K give
no size dependence at a fixed lattice momentum; this conditional comparator
does not exclude every Gaussian effective model or select stiffness from
Gauss law. Matching a ring f-sum is an additional assumption.

## A dephasing criterion and finite graph

For a fixed menu, Delta(rho)=sum_q P_q rho P_q is idempotent. A functional
f factors through Delta iff f=f composed with Delta: one direction is
immediate, and conversely restrict f to the image of Delta. For a qubit,
Delta keeps r dot n. Functions (1+r dot n)/2 and exp(-(r dot n)^2)
therefore pass; purity and transverse coherence do not, as explicit Bloch
vectors demonstrate. Calling this image 'registered content' is a supplied
interpretation; actual registered outcomes, probabilities and a density
matrix are distinct data. This criterion does not classify all clocks
allowed by the axioms or establish how a clock evolves between events.

The explicitly defined colored-site rule from the network note gives
64 sites on the 4x4x8 torus. The runner checks axial degree three,
connectivity and bipartiteness there. This does not establish infinite-cover
connectivity, a physical record pattern, a complete node count or a
charged physical Weyl phase. Its graph is a supplied construction.

## Historical fit arithmetic

The hardcoded four-size values (.692,.557,.575,.510) and weights from
(.013,.022,.028,.046) are historical inputs, not newly reproduced
observations. The power fit minimizes weighted log residual; the affine
fit minimizes original-scale weighted residual. The runner reports the
log objective separately from the original-scale residual sum at that
power fit. The latter is not the minimum of a nonlinear original-scale
power fit. These descriptive numbers do not establish fit significance,
a preferred asymptotic exponent, single-exponential decay or a universal
factor-two error adjustment. Larger auxiliary runs are not authority here.
The regulator comparison remains finite and cannot establish boundary
independence or eliminate population bias.

## Validation and remaining work

Eight checks retain the identities, graph, historical arithmetic and an
explicitly unadopted fourteen-choice register. Supplied definitions copied
from parents are not independent review evidence. Global phases, controlled
large-volume inference, formation dynamics and physical realization remain
open; the original branch retains the broader hypotheses for recovery.

## Source dependencies

[Current axiom authority](MINIMAL_AXIOMS_2026-06-29.md).

- [9161: scoped parent source](RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9163: scoped parent source](RING_MODEL_ICE_TRANSVERSE_WEIGHT_SUM_RULE_THE_RING_TERM_MOVES_THE_WEIGHT_FROM_THE_SMALLEST_MOMENTA_TO_THE_ZONE_CORNER_WITHOUT_A_GROWING_PEAK_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9169: scoped parent source](RING_MODEL_FROM_THE_RK_POINT_TO_THE_PURE_RING_POINT_THE_TRANSVERSE_WEIGHT_MOVES_TO_THE_ZONE_CORNER_CONTINUOUSLY_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9166: scoped parent source](GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9168: scoped parent source](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9171: scoped parent source](RING_MODEL_THE_TEN_CUBED_POINT_LIES_BETWEEN_THE_LINEAR_AND_LEVEL_READINGS_AND_A_CONSTANT_PLUS_A_LINEAR_TERM_FITS_THE_FOUR_SIZES_MILDLY_BETTER_THAN_A_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9220: scoped parent source](RING_MODEL_TWO_REGULATORS_A_REGION_BOUNDED_BY_RECORDS_MATCHES_THE_TORUS_AT_SIZE_EIGHT_AND_THE_WALKER_POPULATION_IS_THE_LARGER_REGULATOR_BOUNDED_THEOREM_NOTE_2026-09-25.md).

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied supports, representations, trajectories and finite experiments above.
- **N2 — Independence:** fresh primary execution is distinct from the independent controls recorded with this review.
- **N3 — Imports:** Hilbert kinematics, models, patterns, clocks and sectors remain supplied rather than framework admissions.
- **N4 — Dependencies:** linked current scoped parents govern; historical titles do not strengthen these claims.
- **N5 — Resolution:** numerical spectra, quadrature, sampled fits and Berry sums are not certified global enclosures.
- **N6 — Residuals:** physical realization, complete classification and larger-system inference require separate evidence.
- **N7 — Counterroutes:** alternative representations, sectors, nonlinear laws and different orders of limits remain available where stated.
- **N8 — Boundary:** this is source review, not an audit verdict or a retained-grade promotion.

## Recovery and falsifiers

An example satisfying a theorem's exact hypotheses but violating its conclusion
refutes that theorem. A failed finite check requires investigation; it is not
silently converted into a different physical interpretation. The original
branch preserves wider proposed claims and all original calculations for
explicit recovery. This source's scope controls its historical identifier.

Original PR #9172, frozen head `4e37c6e728cb50f9b289dd9ba13b07c5aa0467be`.
