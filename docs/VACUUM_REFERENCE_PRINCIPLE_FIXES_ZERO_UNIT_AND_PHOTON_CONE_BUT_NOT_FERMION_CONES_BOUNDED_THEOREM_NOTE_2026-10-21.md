---
claim_id: vacuum_reference_principle_fixes_zero_unit_and_photon_cone_but_not_fermion_cones_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied free sea on static cells at second order, a supplied vacuum-reference principle (edges and links respond only to departures from the vacuum of the same edges with flat links, in the vacuum's units) removes every vacuum term from the edges, makes the subtracted link running cell-blind and puts the dressed photon cone on the edge cone at q -> 0; fixing the 4-volume per record removes none of the massless sea's shape dependence; no response law fixes charged-fermion cones; the principle is adopted, not derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/vacuum_reference_principle_fixes_zero_unit_and_photon_cone_but_not_fermion_cones_2026_10_21.py
---

# The vacuum-reference principle fixes the zero, the unit and the photon cone, but not fermion cones

Claim type: bounded_theorem.
Primary runner: `scripts/vacuum_reference_principle_fixes_zero_unit_and_photon_cone_but_not_fermion_cones_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law carries four clauses: (a) a fixed 4-volume per record, (b) a vacuum zero, (c) a shared light cone, and (d) a dressed coupling that is one unit in every cell. This note tests one principle against all four. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) imply none of them.

## Statement

The principle, supplied: edges and links respond only to departures from the vacuum of the same edges, in the vacuum's own units. The vacuum's phase on those edges, with flat links, is the zero, and the vacuum's dressed coupling at one proper wavelength is the unit of every link, the same for electric and magnetic fields and in every cell.

For the supplied free sea on static cells at second order:

1. Clause (b) follows and removes every vacuum term from the edges. The reference must be taken with flat links; subtracting the vacuum at the actual links would remove vacuum polarisation from the response.
2. Clause (d) follows: the subtracted running at the same proper q/m is cell-blind, and both electric and magnetic runnings extrapolate to one-loop QED.
3. Clause (c) follows for the photon: one unit for E and B puts the dressed photon speed at q -> 0 exactly on the edge cone, and the remaining E/B difference falls as (mL)^2. It does not follow for charged fermions: no response law acts on the update's kinetic terms.
4. Clause (a) does not follow, is not needed, and is not sufficient. The massless sea's phase depends on a cell only through tau/L, so a shape change at fixed 4-volume moves it at first order.

## Derivation

The vacuum carries no field, so a field is a departure from it; the reference is therefore the vacuum on the same edges with flat links. Subtracting that phase removes the sea's Lambda-type term, its tensor gradient term, its shear softness and its missing Newtonian part, so the transverse and Newtonian couplings both equal the hinge-sum G. Gravitational waves are not dressed by the sea and travel on the edge cone.

Without the unit, the sea's uniform-field E and B couplings differ by a constant dC, and A(0) follows the cell size with the QED logarithm. That constant is all the unit removes; after it, the E and B runnings agree up to a lattice term falling as (mL)^2. The unit is one condition per link, summed over all species, not a counterterm per species.

A fermion's dressed cone is set by the tick law and its link dressing, and nothing in the response law acts on the tick's kinetic terms. The tick has no symmetry between time and space steps, so a one-loop shift of order alpha/pi times an unforbidden lattice constant is expected; it was not computed here. Clause (c) for fermions therefore belongs to the tick law.

For the massless sea, a change (tau e^{3x}, L e^{-x}) keeps the 4-volume and moves the phase at first order, while a conformal change does not move it at all. For a massive sea the conformal part, which is all that fixing 4-volume removes, is a small fraction of the shape part. The lattice vacuum stress is radiation-like, not w = -1. So it is clause (b), not clause (a), that keeps the sea's Planck-scale stress from gravitating. Without (a) a split's junction residual stays a one-slab mismatch of order (Hl)^2; with (a) each split kicks Lambda by rho^2/rho*.

On the register's "each part" source, a 12-site gapped Dirac ring (924 configurations, 2-site parts) shows that the literal reference lets the frozen sea's configuration make the source fluctuate, while the vacuum taken at the same configuration gives exactly 0. Subtracting local phases at the same configuration keeps the mean, gives a total with no noise for every eigenstate, and places a local excitation's source on its own block and neighbours. A departure that changes a conserved number has no vacuum amplitude at any of its configurations, so that form is undefined there; this stays open.

## Checks

The runner ends with `TOTAL: PASS=10 FAIL=0`. Its lines:

- `[PASS] A1 massless sea: the phase depends on the cell only through tau/L (Weyl), so a shape change at fixed 4-volume ... moves it at first order and a conformal one not at all`.
- `[PASS] A2 massive sea (mu = 0.0025): the conformal part, the only part fixed 4-volume removes, is a fraction 3e-04 of the fixed-volume part; the lattice vacuum stress is radiation-like, not w = -1  shape -38.230 c0, conformal -1.20e-02 c0`.
- `[PASS] B1`: without the principle the uniform-field E and B couplings differ by dC = 0.1506, 0.1399, 0.1324 at mL = 0.4, 0.32, 0.256, and A(0) follows the cell size with slopes 0.979 and 0.987.
- `[PASS] B2`: with the principle the dressed photon speed at q -> 0 is the edge cone exactly, and |R_E - R_B|/|R| = 0.0617, 0.0406, 0.0249, falling as (mL)^2.
- `[PASS] B3`: at the same proper q/m, cells 25% apart differ by 0.0159 and 0.0116 of the unfixed shift (power 1.44), and a shape change eps 0.05 -> 0.3 moves it by 2.1e-3.
- `[PASS] B4 both subtracted runnings extrapolate to one-loop QED as mL -> 0  R_E/R_QED 1.1359 -> 0.9916; R_B/R_QED 1.0582 -> 1.0018`.
- `[PASS] C1`: a fixed record 4-volume turns each split's junction residual into a permanent kick rho^2/rho* of Lambda; with the principle that rule can go and the residual stays a one-slab mismatch.
- `[PASS] D1`: with the literal reference the source fluctuates (sd 0.2529); with the vacuum at the same configuration it is 0 everywhere.
- `[PASS] D2 charge-neutral excitations: subtracting part-conditioned vacuum phases loses energy (mean/target below 0.9); subtracting local phases at the same configuration keeps the mean exactly, gives a noise-free total for every eigenstate`.
- `[PASS] E1 arithmetic`: the residual and the photon's Lorentz violation are far below the bounds, and the wrong reference fails MICROSCOPE by more than 1e8.

## Estimates against measurement

Subtracting the vacuum at the actual links would leave 1/alpha(M_Z) at 137.04 against 128.9 and give an Eotvos parameter of about 7e-6 against MICROSCOPE's 3e-15. With the principle, the residual d ln alpha/d Phi is about 2e-34 against the clock bound 1.4e-8, and the photon's lattice Lorentz violation at the electron is about 7e-44. The unit at a fixed proper wavelength also holds Lambda_QCD, and so m_p, in proper units; without it baryons would fall with 4/3 of the lapse, against Cassini. The transverse-to-Newtonian G ratio is 1 against 0.81 without clause (b). For charged fermions an unforbidden one-loop offset of order 2.3e-3 times a lattice constant would far exceed the LEP and LHAASO bounds; this is an estimate, not a computation. The measured Lambda needs a supplied geometric constant per proper 4-volume, giving w = -1 exactly.

## Boundary

Supplied: the principle itself, adopted to meet measurement and not derived from the axioms; the filled sea as the vacuum, an adiabatic vacuum on time-dependent edges, and a Boulware-like vacuum on edges with a horizon (an untested risk); the reference wavelength (a uniform field for QED, a fixed proper wavelength for colour); the constants 1/e0^2, G's unit of area and Lambda; and the models (free sea, static cells, second order, tori and fits, the 1D toy, QED as the comparator, Standard Model charges, measured numbers). Not forced: fermion cones, the size of Lambda, a consistent split junction, and the source for departures that change a conserved number. Dropping the fixed 4-volume clause would make the isotropic gauge available again; how it bears on the register's split cosmology is not settled here.
