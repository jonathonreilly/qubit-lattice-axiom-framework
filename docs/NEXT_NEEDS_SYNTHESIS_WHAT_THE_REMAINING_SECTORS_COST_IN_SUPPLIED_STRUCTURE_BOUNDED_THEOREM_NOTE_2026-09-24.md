---
claim_id: next_needs_synthesis_what_the_remaining_sectors_cost_in_supplied_structure_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Composition, clocks, composite charge and ring diagnostics: scoped synthesis. Conditional identities
  and finite constructions only; all imported structures and unresolved wider inferences explicit.'
upstream_dependencies:
- composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
- gauging_the_composite_site_charge_the_link_field_dresses_the_yao_lee_bond_and_the_z2_partner_survives_bounded_theorem_note_2026-09-24
- minimal_axioms
- record_formation_clock_in_the_clause_the_field_aligned_menu_s_odds_do_not_depend_on_when_records_form_bounded_theorem_note_2026-09-24
- record_readout_locality_read_as_local_tomography_admits_the_ordinary_composite_and_excludes_the_graded_one_bounded_theorem_note_2026-09-24
- ring_model_between_the_rokhsar_kivelson_and_pure_ring_points_small_torus_and_variational_diagnostics_bounded_theorem_note_2026-09-24
- ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
- tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
runner: scripts/next_needs_synthesis_consolidated_certificates_2026_09_24.py
---

# Composition, clocks, composite charge and ring diagnostics: scoped synthesis

**Type:** bounded_theorem

## Status and common premise boundary

This synthesis retains nine consolidated checks for eight supplied model
blocks. Their constructions, conditional theorems and residual questions
are summarized below; a successful identity check does not prove every
original claim of its parent. No decision point is adopted, and review is
not an independent audit. Hilbert kinematics, tensor composition,
Hamiltonians, ensembles, clocks, graphs and record patterns remain supplied.

## Exact identities and their limits

**Composition.** Four tetrahedral axes give 16 product projectors spanning
two-qubit Hermitian matrices. Their local Gram matrix has diagonal 1 and
off-diagonal 1/3, hence eigenvalues 2 and 2/3; its tensor square is
invertible. These are probabilities across different menus, not a single
normalized 16-outcome POVM. For two parity-superselected modes, the Bell
states (01+10)/sqrt(2) and (01-10)/sqrt(2) agree on every even local
product but are distinct globally. This counterexample does not exclude
every fermionic composition or force local tomography from Record.
Half the swap W has eigenvalue -1/2, while its product expectation is
|<a,b>|^2/2>=0. Product positivity alone is weaker than positivity on the
full generated matrix algebra. Both composition assumptions remain explicit.

**Clock.** For an isolated Bloch vector precessing about a fixed field,
d(r dot hhat)/dt=0. Thus every normalized formation-time measure supported
on this trajectory gives the same field-menu probability (1+r dot hhat)/2.
This does not characterize all cases of clock independence: stationary
states, other constant observables and particular coincident averages are
counterroutes. The runner compares constant and purity rates, normalized
on its finite integration interval. Such a state-dependent hazard and the
conditional state/preparation are supplied; the listed rates are examples,
not an exhaustive class. A tilted menu generally changes with the hazard.

**Composite charge.** The four-dimer star Hamiltonian is a sum of tau bond
factors times sigma dot sigma. Its total matter spin commutes termwise;
at J=(1,.8,.6) the displayed finite spectrum has levels (-3e,-e,e,3e),
e=sqrt(2), with multiplicities (32,96,96,32). The bare-Majorana projection obstruction is specific to
that gauge-odd operator. It does not prohibit one-qubit U(1) models or
prove physical charged fermions or chiral edges.

**Tensor comparator.** For the explicitly supplied periodic constraint G,
scalar pattern S and quadratic form M(E), the runner tests G S^T=0,
M(S^T a)=0 and M(E+S^T a)=M(E) when E is in ker G. It also tests a
nonzero change for the *same* off-constraint E before and after the shift.
These finite matrix identities and the parent quotient argument concern a
noncompact comparator. They do not prohibit every compact completion.
Truncated oscillator commutators have a boundary-level defect; control is
state dependent, rather than uniform convergence in operator norm.

**Ring model.** Complete 2^3 ice enumeration gives 9600 states, 937 flip
classes and largest class 864. On that component, the negative adjacency
matrix has a sampled Jastrow-family minimum at alpha=.14 on the 101-point
grid; this is not the continuous optimum or the global optimum over states.
A short finite-population guided projection is compared to its exact
component energy. The quoted error is a bin-based diagnostic from one
seed, not a bound on population, projection-time or correlation bias.
Neither energy agreement nor structure factors on a few tori prove absence
of order or a thermodynamic photon phase.

**Gauged bond.** At the source of a dressed hop, link flux and occupation
rise together, and at its destination both outward flux and occupation
fall. Their difference G therefore commutes with the hop. A two-partner
product also commutes in the checked two-dimer cluster. No generic cubic
static-link reduction follows. A background is one way to allow positive
total occupation on a closed graph; zero background still allows vacuum.

**Winding.** On the even L=4 torus the alternating seed is divergence
free. Reversing q of its selected negative x-lines leaves divergence zero
and gives W=(2q,0,0), independently of the cut. The runner checks q=0,1,2.
This proves a finite construction, not that winding labels one flip class.
Uniform guided walkers correspond to inverse-guide initial wavefunction,
not the uniform quantum state. Thresholded log fits cannot certify a gap
or a multi-exponential relaxation law.

## Register and unresolved work

The runner retains fourteen explicitly unadopted model/method choices and
checks their coverage of eight blocks. A register is bookkeeping, not an
axiom admission mechanism. None of the supplied choices acquires authority
through this synthesis. Physical realization of composites, independent
control of projector errors, clocks selected by the axioms, compact tensor
completions and the photon phase remain unresolved. Historical claims and
numerical payloads are preserved on the original branches for recovery.

## Source dependencies

[Current axiom authority](MINIMAL_AXIOMS_2026-06-29.md).

- [9140: scoped parent source](RECORD_READOUT_LOCALITY_READ_AS_LOCAL_TOMOGRAPHY_ADMITS_THE_ORDINARY_COMPOSITE_AND_EXCLUDES_THE_GRADED_ONE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9142: scoped parent source](RECORD_FORMATION_CLOCK_IN_THE_CLAUSE_THE_FIELD_ALIGNED_MENU_S_ODDS_DO_NOT_DEPEND_ON_WHEN_RECORDS_FORM_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9144: scoped parent source](COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9145: scoped parent source](TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9146: scoped parent source](RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_SMALL_TORUS_AND_VARIATIONAL_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9148: scoped parent source](RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9149: scoped parent source](GAUGING_THE_COMPOSITE_SITE_CHARGE_THE_LINK_FIELD_DRESSES_THE_YAO_LEE_BOND_AND_THE_Z2_PARTNER_SURVIVES_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9153: scoped parent source](RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md).

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

Original PR #9155, frozen head `6b4ca7cd38d56db2093f5794637b9d337cb431d0`.
