---
claim_id: admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Finite free-fermion instantaneous filled-negative-band energy on an even torus with supplied massless/staggered
  walk. Conditional scalar homogeneous action with this prescribed source gives the stated turning point and massive
  threshold, not nonexistence of a full lattice solution. Nonzero finite hard-core hopping sectors have negative
  spectral minimum; this does not identify a half-filled sea, and completely occupied massless hard-core hopping
  is zero. Length-dependent sea subtraction changes the source and pressure; fixed-background conservation does
  not establish its dynamical compatibility.
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_bounded_theorem_note_2026-09-25
- minimal_axioms
runner: scripts/admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_2026_09_25.py
---

# Instantaneous sea energies and a conditional homogeneous turning point

**Type:** bounded_theorem
**Status:** finite spectra and supplied scalar source model; unaudited.

## Supplied objects and parent scope

Use an even finite torus of side at least four, two coin states per site, real mass mu>=0, and the free-fermion walk `H(k)=sigma.sin(k)/ell` or its staggered-mass doubled block. Filling all negative one-particle modes is a supplied free-fermion state, not a physical vacuum identification. Zero-energy occupations do not change its energy. The current parent classifies a fixed density and eight-dimensional site-term family; it does not select a universal physical zero of energy.

Separately supply the homogeneous scalar action of the companion note, with alpha>0, ell>0 and constraint `24alpha ell³ lambdadot²=m(lambda)`. It is not a proven nonlinear solution of the full lattice constraints. Feeding an instantaneous ground energy into m is an additional source/adiabatic ansatz. In the massive case Hamiltonians at different lengths generally do not commute, so unitary evolution need not follow the instantaneous filled sea.

## Theorem T1 — finite instantaneous spectra

The massless two-by-two symbol has eigenvalues plus/minus |sin k|/ell. The massive four-by-four block has trace zero and square `(mu²+sum sin²(k)/ell²) I`, so its eigenvalues are the two opposite roots with equal multiplicity. Counting each reduced-zone pair once gives the sea energy per site

`m_sea=-I/ell` or `-average_k sqrt(mu²+sum sin²(k)/ell²)`.

On side four each sin² coordinate is zero or one with equal multiplicity, so `I=(3+3sqrt(2)+sqrt(3))/8`. The corresponding energy per volume divides by ell³. At least one mode has nonzero sin k, ensuring strict negativity, strict increase with ell of m_sea, and nonconstant volume density. A torus supported only at zero-sine momenta would be an exception; it is excluded here.

For massless nearest-neighbor hopping compressed to one record per site on a finite even torus, multiply each occupation basis state by the product of its occupied sublattice signs. Every allowed hop reverses this sign. Thus the compressed Hermitian matrix anticommutes with this involution. In any sector where that matrix is nonzero its finite spectrum is symmetric and has a strictly negative minimum. The primary two-particle control uses the symmetric exchange convention; the sign argument itself also tolerates antisymmetric exchange signs. It does not determine a many-body half-filled ground state by filling one-particle modes. At complete occupation every attempted hop is blocked and the compressed massless hopping is zero. The supplied scalar staggered onsite term also sums to zero on an even torus, since the two sublattices have equal size. In particular one particle per site must not inherit the free two-coin half-filled sea's negative energy.

With the supplied dilation pressure `p=-dm/dlambda/(3ell³)`, the massless sea has `p=rho/3`. For one massive mode put `y=s²/ell²`; differentiation gives `p/rho=y/[3(mu²+y)]`. When mu>0 this lies in [0,1/3), and the full sea ratio is the energy-magnitude-weighted average of those ratios. The stated torus has a nonzero-sine mode, so its total ratio is strictly between zero and one third. For mu=0 it is one third. Constant volume density instead gives p=-rho. These are instantaneous prescribed-source equations of state, not an adiabatic evolution proof. The full-zone sum includes all eight zero-sine corners; no additional physical species identification is made.

## Theorem T2 — a specified homogeneous source

For m=m_sea<0 the scalar constraint has no real solution. This excludes only this homogeneous supplied model, not all static or nonuniform lattice geometries.

Let m0>0 and I>0, with `m=m0-I/ell`. The permitted lengths obey ell>=I/m0. The length equation gives `lambdaddot=m0^4/(48alpha I^3)>0` at the turn. On each side of the bounce,

`t(ell)=±sqrt(24alpha)/m0² [(2/3)(m0 ell-I)^(3/2)+2I sqrt(m0 ell-I)]`.

Its derivative squared is `24alpha ell²/(m0 ell-I)`, the inverse of ell_dot² from the constraint. Joining the contracting and expanding branches at t=0 satisfies the second-order equation; holding ell at the turn would not. The construction applies on positive-length intervals.

For mu>=0 and `m=m0-average sqrt(mu²+s²/ell²)`, at least one s²>0 makes m strictly increasing from minus infinity to m0-mu. Consequently for m0>mu there is exactly one finite turning length and a permitted branch toward arbitrarily large ell. For m0<=mu no finite ell is allowed. This is a conditional instantaneous-source statement; no hard-core sea energy is substituted into it.

## Theorem T3 — subtraction is an extra dynamical choice

At fixed ell a spatially uniform constant density subtraction changes no spatial divergence and has zero time derivative. During a stretch, however, m_sea(ell(t)) is time dependent: in the massless case `d m_sea/dt=I ell_dot/ell²`. It cannot be removed from an unchanged conservation law merely by calling it constant per site.

One may instead supply a different scalar source action with `m_new=m_old-m_sea(lambda)`. Its associated dilation pressure must also change, by `p_new=p_old+m_sea_prime/(3ell³)`. The scalar constraint and length equation then remain compatible by variation of that new action. This is an additional coupling/counterterm choice; the full matter-field conservation law, inhomogeneous completion and physical source prescription remain open. No owner decision or new premise is inferred.

## Late source update: commuting stretch and conditional adiabatic response

For the massless symbol H(ell)=H(1)/ell, Hamiltonians commute at all positive lengths; an initially filled negative band keeps its occupations under any uniform length history. A supplied counterterm +I/ell cancels its instantaneous energy, with pressure +I/(3ell⁴). A fixed +I/ell0 counterterm has zero dilation pressure and leaves I/ell0-I/ell. Spatial uniformity alone still does not conserve a time-dependent subtraction; the counterterm action and its pressure must be supplied as in T3.

For the massive four-dimensional block H=A/ell+B, A=(sigma.s)tau_z, B=mu tau_x, one has {A,B}=0 and [H(ell1),H(ell2)]=2(1/ell1-1/ell2)AB. Its squared Frobenius norm is 16mu²s²(1/ell1-1/ell2)². Writing E²=mu²+s²/ell² and P±=(1±H/E)/2 gives Tr(P+ H_lambda P- H_lambda)=2mu²s²/(ell²E²). Nonzero off-diagonal derivative permits first-order transition amplitudes; it does not prove nonzero excitation for every stretch history or an energy change linear in rate.

For mu>0 and slow smooth motion with the adiabatically dressed state prepared (no uncontrolled initial switching transient), the first-order amplitude is proportional to lambda_dot times the derivative matrix element divided by (2E)². Multiplying its squared modulus by the excitation gap 2E gives energy excess lambda_dot² Tr(P+ H_lambda P- H_lambda)/(2E)³ per reduced-zone block. There are half as many such blocks as sites, so the excess per site is (1/2)m_lambda lambda_dot², where m_lambda=average mu²s²/(4ell²E⁵). This derives the coefficient rather than inferring dynamics from noncommutation. Its bound m_lambda<=average s²/(4mu³ell²) follows from E>=mu. An arbitrary evolving sea can also carry history-dependent excitations; the local expression is only a leading adiabatic approximation.

If one additionally supplies the lapse-covariant effective action term +(1/2)m_lambda lambda_dot²/w, then lapse variation gives (24alpha ell³-m_lambda/2)lambda_dot²=m_remaining. This is a conditional effective-action model, not a consequence of the fixed-background conservation identity. T2 uses the instantaneous source alone; its no-motion conclusion for m0<=mu is not extended to this modified model, and small effective kinetic coefficient can invalidate the slow-motion approximation. No continuum, interacting-vacuum, or complete lattice backreaction result is inferred.

## No-Go Discipline Gate

- **N1:** finite even tori with a nonzero-sine mode; supplied scalar action, real positive length and stated source.
- **N2:** no repository no-go wall is an input.
- **N3:** free statistics, instantaneous occupation/source and subtraction model are supplied.
- **N4:** current parent scopes do not fix a physical energy zero or full zero-mode completion.
- **N5:** exact finite arithmetic checks spectra and scalar equations, not full lattice backreaction.
- **N6:** massive time evolution, interacting filling, shear and nonlinear source conservation remain open.
- **N7:** complete hard-core occupation is a zero-hopping counterroute; time-dependent subtraction changes the balance law.
- **N8:** retain finite spectral and conditional bounce lemmas, not a statement that a lattice cannot exist.

## Verification and recovery

Original source and campaign are frozen at PR #9240 head df4a90a84bdbb0ec425a75b694d02675b843c41f. Fresh controls include the full-occupation counterroute and time-dependent subtraction. Historical filenames are identifiers only.

This note studies supplied finite spectra and a homogeneous scalar action; no full nonlinear lattice completion or physical energy zero follows; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Inputs

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_WITH_THE_STATIC_PULLS_COUPLING_IFF_ALPHA_EQUALS_K_OVER_FOUR_AND_TOP_SPEED_WALKERS_LOSE_ENERGY_AS_ONE_OVER_THE_LENGTH_BOUNDED_THEOREM_NOTE_2026-09-25](ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_WITH_THE_STATIC_PULLS_COUPLING_IFF_ALPHA_EQUALS_K_OVER_FOUR_AND_TOP_SPEED_WALKERS_LOSE_ENERGY_AS_ONE_OVER_THE_LENGTH_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25](ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
