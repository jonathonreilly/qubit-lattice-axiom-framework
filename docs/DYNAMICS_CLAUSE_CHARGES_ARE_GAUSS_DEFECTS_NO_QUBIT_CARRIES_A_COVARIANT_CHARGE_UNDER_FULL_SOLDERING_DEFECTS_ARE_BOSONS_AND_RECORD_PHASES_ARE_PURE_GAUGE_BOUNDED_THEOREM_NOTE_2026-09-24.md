---
claim_id: dynamics_clause_charges_are_gauss_defects_no_qubit_carries_a_covariant_charge_under_full_soldering_defects_are_bosons_and_record_phases_are_pure_gauge_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied soldered spin-half links and soft Gauss energy. Fully soldered role stabilizers have no nonconstant scalar one-qubit charge; the four declared vertex actions give link-flip dimensions 0,0,0,2 and no covariant charge transfer. A flip creates opposite unit Gauss defects at unperturbed cost 2U. An explicit projected two-defect T-junction channel has equal nonzero hop products. The fourth-order ring includes the product of link amplitudes; exact on-link basis conjugation removes transverse phases in H0+fields but is generally not vertex gauge. Unequal magnitudes can split fourth-order diagonals. No physical quasiparticle statistics, finite-field gap or phase is established.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_charges_are_gauss_defects_2026_09_24.py
---

# Supplied Gauss defects: covariance, hopping channels and link-basis phases

**Type:** bounded_theorem

**Date:** 2026-09-24
**Status:** conditional-support; supplied-model mathematics, unaudited.

## Covariance and the one-qubit boundary

Take doubled-coordinate vertex, link, plaquette and cube roles, with
soldered link field E_l=s_l dot e_l. The four role stabilizers have orders
24,8,8,24. Under full soldering none fixes a nonzero Bloch axis: the
half-turns and quarter-turns together remove every invariant vector.
Thus a scalar one-qubit charge operator invariant under its role
stabilizer is constant. This concerns a scalar charge, not every
covariant vector observable or composite matter construction.

A vertex-link bond is fixed by quarter-turns about the link axis.
The link raising/lowering operators acquire phases ±i. A covariant
two-site term that changes the link needs the opposite phase on the
vertex. The declared trivial, sign-twist and axis actions have only
±1 phases on that stabilizer; full soldering has the required phases
but no nonconstant invariant scalar vertex charge. The corresponding
link-flip dimensions are 0,0,0,2. Hence none of those four supplied
vertex actions gives two-site transfer of such a scalar charge to
a soldered link. Alternative representations and larger supports
remain outside this statement.

## Unperturbed defects and a projected hopping channel

Supply H0=U sum_v(div E_v)², U>0, on the coarse L=6 torus.
Flipping one link of an ice state creates charges +1,-1 and costs 2U.
A +1 defect has four outward-positive links; flipping one whose far
end is neutral moves the defect there at the same H0 energy.
This is an unperturbed energy statement, not a finite-field gap theorem.
Total divergence vanishes identically on a closed lattice; the individual
local charges change under the transverse flips.

Bare operators on distinct links commute, but a statistics interpretation
also needs allowed projected particle hops. The primary constructs an
explicit channel: choose two incoming links j→i,l→i and one outgoing
link i→k in a zero-charge field. Create +1 defects at j,l by flipping
other incoming links at those leaves; their -1 partners lie away from
the junction. The two orders

    j→i, i→k, l→i    and    l→i, i→k, j→i

have nonzero unit-step amplitudes, keep every intermediate state at
energy 4U and finish in exactly the same electric configuration, with
positive defects at i,k. Each distinct link is flipped once, so
arbitrary nonzero local amplitudes also have the same product in
both orders. This realizes the +1 T-junction relation in this
supplied channel. The bare operator identity alone is not promoted
to a classification of physical quasiparticles or all projected
many-defect sectors.

The hopping-operator criterion is described by
[Levin and Wen, section III](https://arxiv.org/html/cond-mat/0302460).
Its particle Hilbert-space and allowed-hop assumptions matter.
String-dressed hopping, other sectors and physical phase identification
remain separate obligations. Auxiliary Majorana variables in a Kitaev
representation are not, merely by their notation, physical charged fermions.

## Fourth-order ring and exact phase conjugation

Let t_l be the directed flip amplitude needed to go from one flippable
configuration to the other. With the same soft Gauss denominators as
the companion ring calculation,

    <b|H_eff|a>=-(5/(2U³)) product_(four links) t_l

at fourth order. The twenty-four flip orders have first/third denominators
2U; sixteen have middle denominator 2U and eight have 4U.
Finite-h effective-Hamiltonian diagonalization checks approach to this
asymptote, not equality at nonzero h.

Write each transverse term as z_l S_l^+ + conjugate(z_l) S_l^-.
Since [E_l,S_l^+]=S_l^+, the product unitary

    W=product_l exp[-i arg(z_l) E_l]

commutes with H0 and takes this specified H0-plus-fields Hamiltonian
to one with positive real transverse coefficients. Zero amplitudes
need no phase choice. This equivalence is exact, hence also relates
consistently transformed perturbative Hamiltonians at every order.

This is an on-link BASIS transformation, generally not a Gauss-generated
vertex gauge transformation. A vertex transformation has link angles
given by endpoint differences and zero plaquette curl. Arbitrary supplied
link angles can have nonzero curl even though the oriented cube sum
of curls is zero. The runner checks both nonzero plaquette curl and
exact local conjugation. Consequently the old statements “pure gauge”
and “no background flux” are not retained as physical conclusions.
Additional fixed couplings, observables or external phase references
must transform too; keeping them unchanged defines a different model.

Unequal magnitudes alter both the ring strengths and the fourth-order
diagonal energies. For equal magnitudes, every ice vertex has nine
in-out pairs and six same-type pairs, giving a constant diagonal through
that order. Unequal pair weights remove that counting cancellation;
the runner exhibits distinct balanced configurations with different
diagonal contributions. This is neither state selection nor a
thermodynamic phase calculation.

## Evidence and deferred work

The primary retains role/bond covariance, exact defect energies, the
explicit projected channel, phase conjugation, asymptotic ring controls
and unequal-magnitude examples. The historical broad statistics,
physical-flux and independent-check narratives remain recoverable on
the original PR branch. They are not silently treated as present
evidence. Current review is not an independent audit verdict.

### N1
Examined alternatives are the four vertex actions, soft Gauss defects,
bare/projected local hopping and arbitrary transverse link phases.

### N2
One-qubit covariance, unperturbed energy and physical exchange statistics
are different questions; none closes the other automatically.

### N3
Soldering, Hamiltonian, fields, sectors and allowed particle hops are
supplied. No charge species, readout or physical phase is selected.

### N4
Actual linked parents supply the action menu and ring denominators.
Auxiliary Majorana algebra does not supply physical matter statistics.

### N5
Five resolutions are explicit: scope the scalar-charge obstruction;
construct a nonzero projected T-junction channel; distinguish link-basis
conjugation from vertex gauge; keep the ring formula fourth-order;
and separate magnitude effects from matter or state selection.
The runner prints each resolution.

### N6
General projected-sector statistics, finite-field gaps, composite matter,
additional phase-reference terms and physical interpretation remain open.

### N7
Nonzero link-phase curl directly refutes the unrestricted vertex-gauge
reading. Commuting bare flips alone do not replace a projected-hop
calculation. These limitations narrow the original claims.

### N8
This is a conditional Gauss-defect construction. It derives neither
Standard Model matter nor a photon phase, and makes no priority claim.

## Sources and execution

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22](THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md)
- [DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_THE_FIELD_MOVES_BY_RINGS_AND_HOPS_INSIDE_ONE_NEIGHBOURHOOD_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_THE_FIELD_MOVES_BY_RINGS_AND_HOPS_INSIDE_ONE_NEIGHBOURHOOD_BOUNDED_THEOREM_NOTE_2026-09-24.md)

[Primary](../scripts/dynamics_clause_charges_are_gauss_defects_2026_09_24.py) and [receipt](../logs/runner-cache/dynamics_clause_charges_are_gauss_defects_2026_09_24.txt).
