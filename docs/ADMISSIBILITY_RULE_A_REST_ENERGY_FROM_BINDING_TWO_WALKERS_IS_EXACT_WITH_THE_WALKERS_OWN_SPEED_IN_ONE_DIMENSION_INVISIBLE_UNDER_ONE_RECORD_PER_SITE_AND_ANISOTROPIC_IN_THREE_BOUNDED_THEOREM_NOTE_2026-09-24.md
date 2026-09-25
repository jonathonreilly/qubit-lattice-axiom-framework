---
claim_id: admissibility_rule_a_rest_energy_from_binding_two_walkers_is_exact_with_the_walkers_own_speed_in_one_dimension_invisible_under_one_record_per_site_and_anisotropic_in_three_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Supplied attractive contact pair: exact negative one-dimensional bound energies and their squared-energy
  expansions; off-spectrum three-dimensional contact resolvent; strong-binding squared-energy coefficients through
  V^-2 and axial momentum degree2; contact projection and finite-support timed-translation algebra. No exact continuum
  dispersion, weak-binding 3D existence theorem, physical mass, or global unbounded evolution.'
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- minimal_axioms
runner: scripts/admissibility_rule_a_rest_energy_from_binding_two_walkers_exact_in_one_dimension_invisible_under_one_record_per_site_anisotropic_in_three_2026_09_24.py
---

# Contact-bound walkers: negative-energy bands, squared-energy curvature and clock algebra

**Type:** bounded_theorem
**Status:** bounded-support; supplied operators, unaudited.

This note studies a supplied two-walker contact Hamiltonian, its negative-energy bound branches, strong-binding squared-energy coefficients and finite-support clock algebra. It supplies no physical rest mass, record reading or force law; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Use only the current parent walk H1=sum sigma_j D_j, D_j=(i/2)(T_j-T_j^dagger), (T_j psi)(x)=psi(x-e_j); on the line use sigma_z D. Supply two walkers with H0=H1 tensor I+I tensor H1 and contact V P, V<0, where P projects onto coincident positions. The full two-particle space and interaction are extra assumptions; they do not follow from the one-record clause. At fixed total momentum K the contact fiber has four coin components in three dimensions. Its free symbol is A(q;K)=sum[sin(q_j+K_j/2)sigma_j^1+sin(K_j/2-q_j)sigma_j^2]. Brillouin averages are normalized infinite-lattice integrals, not finite-torus sums.

For the clock supply the sum of the individually timed one-walker hops and the contact V w(x)P on coincidence. Restrict all exponential-clock algebra to finite-support vectors with the required translated neighborhoods; a global self-adjoint pair realization is not proved.

## Theorem T1 — exact line bound state

In a fixed coin sector a shift of relative momentum reduces the free energy to a single sine or cosine of amplitude B: B^2=4sin^2(K/2) for equal coins and B^2=4cos^2(K/2) for opposite coins. For real E outside [-|B|,|B|], the contact equation is1=V <(E-epsilon(q))^-1>. The integral equals sign(E)/sqrt(E^2-B^2); substitution z=exp(iq) gives this by the single pole inside the unit circle, or elementary real integration. V<0 therefore selects E=-sqrt(V^2+B^2), not both square roots. The resolvent wave function is proportional to1/(E-epsilon(q)); it is square-integrable and gives a unique relative bound state in that coin fiber. At B=0 it is the coincidence delta with energy V.

Consequently equal coins give E^2=V^2+K^2-K^4/12+O(K^6); opposite coins give E^2=V^2+4-K^2+O(K^4). The coefficient1 of the first squared-energy expansion is a low-momentum parameter, not an exact continuum relativistic dispersion. Its group velocity has magnitude |sin K|/sqrt(V^2+4sin^2(K/2))<=1; no physical speed is selected. Since E is negative, the signs of E curvature and E^2 curvature are opposite. In particular the equal-coin branch has a local energy maximum at K=0, while the opposite-coin branch has a local minimum there. Calling either curvature a physical inertial mass requires additional structure.

## Theorem T2 — three-dimensional off-spectrum contact condition

At K=0, A=h(q).(sigma^1-sigma^2), h_j=sin q_j. In singlet S and Cartesian triplets T_j, the singlet diagonal resolvent is E/(E^2-4|h|^2). The triplet block is (I-nn^T)/E+nn^T E/(E^2-4|h|^2), n=h/|h|, with its continuous expression used at h=0. The singlet-triplet elements are odd in h. For E<-2sqrt3 these formulas have no poles. Cubic averaging gives

    1=V I(E),                 singlet,
    1=V[2/(3E)+I(E)/3],       each triplet,
    I(E)=<E/(E^2-4|h|^2)>.

These are bound-state conditions, not an assertion that every attractive V produces all four 3D branches. Weak binding and threshold states are not classified.

## Theorem T3 — strong-binding expansion, not an exact truncated dispersion

The free fiber operator has norm at most2sqrt3. For sufficiently large |V| the four-dimensional contact cluster near V is separated from the free spectrum; bounded perturbation of the isolated contact eigenspace supplies its local analytic expansions in1/V. The resolvent series is valid for |E|>2sqrt3. Odd moments vanish by shifting all relative momenta by pi. Its first even moments are M2=3I-sum cos(K_j)sigma_j^1 sigma_j^2 and M4=<A^4>.

For motion along an axis, M2 and M4 are diagonal in S and the three Cartesian triplets. Substituting E=V+m2/V+(m4-2m2^2)/V^3+O(V^-5) in the contact equation yields

    E^2=V^2+2m2+(2m4-3m2^2)/V^2+O(V^-4).

The moment constant terms give, for axial momentum kappa, the coefficients

    S:       V^2+12-24/V^2 -(1-8/V^2)kappa^2,
    T_across:V^2+4 +16/V^2 +(1-2/V^2)kappa^2  (two components),
    T_along: V^2+4 +16/V^2 -(1+4/V^2)kappa^2.

Each expression has omitted terms O(kappa^4)+O(V^-4) in a small-momentum strong-binding neighborhood; equivalently its constant and quadratic coefficients are specified through V^-2. Degenerate higher-order splitting is not inferred from these two moments. The signs quoted are squared-energy curvatures; negative bound-energy curvatures reverse them. The displayed coefficient anisotropy is not a universal exclusion of all composite interactions, all couplings or all physical mass mechanisms.

## Theorem T4 — exchange and projected exclusion

At coincidence, particle exchange acts on the two coins: S has eigenvalue-1, triplets+1. Thus an antisymmetric pair's contact amplitude lies in S, and a symmetric pair's lies in the triplets. No exchange statistics are selected by the calculation.

If exclusion is separately imposed with Q=I-P, then Q(VP)Q=0. The appropriate restricted dynamics is QH0Q, since unprojected H0 need not preserve the no-coincidence subspace. This proves the supplied contact term is invisible in that projected model; it does not rule out kinetic boundary effects or other binding interactions.

## Theorem T5 — finite-support clock scaling

For w(x+a)=lambda w(x), each individually timed hop and the timed contact obeys H_w T_a=lambda T_a H_w under simultaneous translation of both particles. For a hop, the two square-root clock factors together supply lambda; at coincidence w itself supplies lambda. This proves the identity on finite support for every permitted translation, beyond the runner's seven-site interior fixture. The untimed contact commutes with T_a instead, giving a nonzero mismatch (1-lambda)V P T_a when V!=0, lambda!=1 and the vector reaches coincidence. If any of those conditions fail it need not break the identity. Finite powers require the corresponding neighborhoods; continuous-time functional calculus requires a compatible self-adjoint realization and is not supplied here.

## No-Go Discipline Gate

### N1 — Exceptions
Only contact binding, negative branches and the stated strong-binding coefficients are treated. No universal binding or physical-mass no-go follows.
### N2 — Wall independence
No repository no-go wall is used.
### N3 — Additional assumptions
Two-particle amplitudes, V, optional exchange statistics, projected exclusion and the timed contact are supplied.
### N4 — Dependencies
The current parent supplies only its explicit walk and finite-support algebra. Original references to other blocks are historical motivation, not premises here.
### N5 — Resolution
Exact checks cover four line integrals, algebraic expansions, a symbolic coin resolvent, Laurent moment coefficients, exchange and a finite interior translation fixture. General integral/domain/asymptotic conclusions use the displayed arguments.
### N6 — Primitive boundary
No site-algebra enlargement or new physical primitive is adopted.
### N7 — Strongest objection
The attractive energy is negative; interpreting positive curvature of E^2 as positive curvature of E is wrong. The source explicitly distinguishes them.
### N8 — Historical scope
Original nearest-neighbor examples, numerical grids, conditional ray interpretations and author referee reports are preserved in the original PR but not fresh evidence here.

## Falsifiers

An off-band negative line eigenvalue violating T1, a wrong moment coefficient under the stated fiber convention, or a nonzero projected contact QPQ refutes the corresponding claim. A different interaction or continuum interpretation does not.

## Imports

Contour integration, tensor-product algebra, resolvent series and bounded analytic perturbation of an isolated finite-dimensional spectral cluster are the mathematical imports; no physical premise follows from them.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): current supplied walk and domain boundaries.

## Review record — historical author provenance

Original PR9157 harvests two author-reported probes attempts. Their historical verdicts do not replace the present scoped checks. All original source remains recoverable; no audit verdict is conferred.

## Verification

Run `python3 scripts/admissibility_rule_a_rest_energy_from_binding_two_walkers_exact_in_one_dimension_invisible_under_one_record_per_site_anisotropic_in_three_2026_09_24.py`. Expected TOTAL: PASS=11 FAIL=0.
