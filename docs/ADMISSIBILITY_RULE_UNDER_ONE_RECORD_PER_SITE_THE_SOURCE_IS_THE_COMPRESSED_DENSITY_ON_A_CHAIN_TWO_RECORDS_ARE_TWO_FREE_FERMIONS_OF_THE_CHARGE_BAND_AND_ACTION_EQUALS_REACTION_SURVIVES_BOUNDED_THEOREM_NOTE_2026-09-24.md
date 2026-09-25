---
claim_id: admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_on_a_chain_two_records_are_two_free_fermions_of_the_charge_band_and_action_equals_reaction_survives_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied position-excluding pair dynamics. At fixed nonzero projected state the logarithmic-rate derivative
  equals the compressed local energy density and sums to total energy. On finite open chains with diagonal conserved
  coins, a site gauge identifies each ordered-coin sector with two spinless free fermions; the density is a one-particle
  reduced-density trace. A simultaneous translation in an exponential clock field scales the generator on finite
  support. No exact crystal-momentum force, passive mass, physical statistics or action-reaction theorem is derived.
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
- admissibility_rule_many_records_under_exclusion_source_is_the_projected_density_chessboard_invisible_interacting_sea_stiffens_clocks_oppositely_bounded_theorem_note_2026-09-22
- admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
- minimal_axioms
runner: scripts/admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_two_records_are_two_free_fermions_on_a_chain_2026_09_24.py
---

# Excluded pairs: fixed-state source, open-chain charge representation and clock scaling

**Type:** bounded_theorem
**Status:** bounded-support; supplied operators, unaudited.

This note studies a supplied compressed two-particle generator, its fixed-state rate derivative, an open-chain charge representation and finite-support translation scaling. No physical passive mass or exact force law follows; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Supply H_w=phi sigma3 D phi on a finite ring or finite open chain, (D psi)(x)=[psi(x+1)-psi(x-1)]/(2i), phi_x>0, w_x=phi_x^2=exp(u_x). Supply H2=H_w tensor I+I tensor H_w and a fixed position projector P removing coincident sites. Tensor-product amplitudes, the compressed dynamics A=P H2 P and either exchange sign are model choices; one record per site does not derive this Hamiltonian or statistics.

All normalized expectations below use a fixed nonzero vector v=P Psi, independent of rates. For the chain reduction only, coins are conserved because sigma3 is diagonal, hopping is nearest neighbor, and endpoints are open. No analogous coin-sequence factorization is supplied for a ring or general 3D coin walk. In the scaling identity lambda>0 and support and its one-step translated neighborhoods lie inside the domain. Infinite exponential clocks require a separate operator realization for evolution.

## Theorem T1 — fixed-state source identity

Let e_x^(2)=sum_s Re<v|P_x^[s] H_w^[s]|v>/<v|v>. Since dH_w/du_x={P_x,H_w}/2 and P is fixed and commutes with P_x in each slot,

    d<v|A|v>/du_x / <v|v> = e_x^(2),
    sum_x e_x^(2)=<v|A|v>/<v|v>.

The derivative keeps v and its norm fixed. Rate-dependent states contribute additional terms unless a separate eigenstate differentiation theorem applies. These algebraic identities extend to any finite graph and any number of slots with the same fixed site projector and rate dependence. They do not determine a force or a sign of the density.

For the six-site ring, phi_x=1+((3x^2+x) mod5)/7 and the two orthogonal complex orbitals explicitly defined in the runner, the projected antisymmetric pair gives E_hc=12349656/122046701; the sum of separately normalized one-record energies is E_free=16169964/134909593. Their local densities differ at all six sites. This is one counterexample to universal additivity over the original orbitals; special states can agree. The runner evaluates exact central differences of the fixed-state quadratic polynomial in one phi_x.

## Theorem T2 — finite open-chain reduction

Use the orthonormal ordered basis x_L<x_R with the two coin labels in spatial order, for either supplied exchange sign. Multiply each down-coin coordinate by (-1)^x. The gauged compressed generator is h2 tensor I_coin-sequence, where h2 is the exterior-square lift of the scalar up-coin hopping matrix h=phi D phi.

Indeed nearest-neighbor hopping under exclusion never crosses the other occupied site, so each spatially ordered coin label is unchanged and no exchange sign is encountered. Across each bond the down-coin gauge product is -1 and removes its opposite hopping sign. In a spinless exterior-product basis, an allowed nearest-neighbor hop cannot cross another occupied site either, so its matrix element is precisely the same h_yx. Diagonals vanish in both models. This proves equality of every matrix element, including the zeros. The state-space dimensions match: choose(L,2) times four coin sequences. No particle statistics are selected physically.

The finite seven-site control checks all nonzero compressed entries for both exchange signs. Open boundaries are essential; a ring permits winding and a boundary exchange twist. Non-nearest hops or coin-changing terms can also defeat the ordered-sequence proof.

## Theorem T3 — charge density, not universal two-orbital additivity

In one fixed ordered-coin sector extend its charge amplitude antisymmetrically to c(x,y), c(y,x)=-c(x,y). With ||c||^2=sum_xy |c(x,y)|^2,

    e_x^(2)=2 Re sum_z,b conjugate(c(x,z)) h(x,b)c(b,z)/||c||^2.

The site gauge commutes with each position projector, so the source identity is preserved by the T2 unitary map. Summing the two equivalent particle slots gives the factor2. This is the actual state's one-particle reduced-density trace. A general charge state need not be a single Slater determinant; only for a determinant does it reduce to a sum over exactly two occupied orthonormal orbitals. Mixed coin sectors use the corresponding reduced-state sum, not a chosen pair of original free orbitals.

An open chain has no periodic translation symmetry or conserved crystal momentum merely because rates are uniform; its endpoints matter. The common-translation statement of the parent is for a periodic system and does not transfer through this open-chain identification.

## Theorem T4 — finite-support translation scaling

In an exponential clock field w(x)=lambda^(2x1), simultaneous translation T of both positions by +e1 gives

    A T = lambda^2 T A.

Every one-body hopping coefficient contains phi_x phi_y, multiplied by lambda^2 under the translation, in any spatial dimension. P commutes with simultaneous translation because coincident positions remain coincident. This proves the matrix identity on finitely supported vectors with complete required neighborhoods, and finite powers with correspondingly larger neighborhoods. The finite runner checks 12 chain columns and400 interior columns of a 5x3x3 three-dimensional walk. It does not test all 3D columns.

This discrete covariance is not an exact canonical crystal-momentum commutator and does not prove d<p>/dt=-g<E>, a passive mass, or action equals reaction. Those conclusions require additional domain, packet and force-model assumptions not derived here. If a reciprocal point-force model is separately supplied and passive response is separately assumed proportional to E, choosing source S=E satisfies its common-ratio condition algebraically. That conditional comparison adds no evidence for the physical assumptions.

The two nonzero energies in T1 have ratio E_free/E_hc=3356276805253/2833481402466. This is a bookkeeping mismatch between two source choices in that example, not a measured force mismatch. General S/E comparisons require E!=0; the derivative and scaling identities also hold when E=0.

## No-Go Discipline Gate

### N1 — Exceptions
Original-orbital nonadditivity is example-specific. The free charge representation needs an open nearest-neighbor chain and conserved coins. Rings, other couplings and higher dimensions are outside it.
### N2 — Wall independence
No repository no-go wall is used.
### N3 — Supplied structure
Amplitudes, tensor products, compression, exchange sign, clock coupling and optional reciprocal forces are supplied separately.
### N4 — Dependencies
The current sources below control. In particular the parent clock covariance supplies no universal exact momentum-force theorem.
### N5 — Resolution
Fresh checks cover the six-site density and energy example, seven-site charge mapping and density trace, and the stated interior translation fixtures. General statements use the displayed finite-dimensional and finite-support proofs.
### N6 — Primitive boundary
No physical mass, statistics, filling rule or new primitive is adopted.
### N7 — Strongest objection
Discrete scaling and the fixed-state energy derivative do not together establish equal physical active and passive mass. The original action-reaction inference is deferred explicitly.
### N8 — Historical scope
The author's distant-pair bound and force interpretation remain recoverable from the original PR; neither is fresh proof here.

## Falsifiers

A fixed nonzero projected state violating the derivative identity, an allowed open-chain matrix element violating the gauge correspondence, or a supported translated hop violating T4 refutes the corresponding statement. A ring boundary effect is outside T2.

## Imports

Finite tensor products, exterior powers, diagonal unitary gauges, polynomial differentiation and reduced density matrices are mathematical imports. The correspondence is proved directly by matrix elements above.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Current conditional input](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current conditional input](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current conditional input](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md)
- [Current conditional input](ADMISSIBILITY_RULE_MANY_RECORDS_UNDER_EXCLUSION_SOURCE_IS_THE_PROJECTED_DENSITY_CHESSBOARD_INVISIBLE_INTERACTING_SEA_STIFFENS_CLOCKS_OPPOSITELY_BOUNDED_THEOREM_NOTE_2026-09-22.md)

## Review record

Original PR9174 and its two author-reported probes attempts are provenance, not independent audit authority. Stronger passive-mass and force conclusions are deferred while the exact source and charge statements are retained.

## Verification

Run `python3 scripts/admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_two_records_are_two_free_fermions_on_a_chain_2026_09_24.py`. Expected TOTAL: PASS=11 FAIL=0.
