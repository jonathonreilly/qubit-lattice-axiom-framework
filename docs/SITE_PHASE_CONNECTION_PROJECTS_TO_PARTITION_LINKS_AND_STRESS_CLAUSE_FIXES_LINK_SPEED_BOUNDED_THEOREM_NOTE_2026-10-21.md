---
claim_id: site_phase_connection_projects_to_partition_links_and_stress_clause_fixes_link_speed_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied two-partition block lattice with a site phase chi entering by minimal coupling, an exact gauge-covariant map Pi sends chi to an even-partition link connection whose kernel is the four gapped branches at k = 0; a block-local update depends on chi only through electric fluxes; a register hopped by the supplied coin is double-valued under rotations; and the stress-symmetry clause of the candidate-law register requires the link speed to equal the fermion speed at leading order. Beyond leading order the supplied continuous-time and leapfrog link laws are compared with measured bounds as estimates. No photon field, carrier register, link law or coarse-rung carrier is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/site_phase_connection_projects_to_partition_links_and_stress_clause_fixes_link_speed_2026_10_21.py
---

# A site-phase connection projects to partition links, and the stress clause fixes the link speed

Claim type: bounded_theorem.
Primary runner: `scripts/site_phase_connection_projects_to_partition_links_and_stress_clause_fixes_link_speed_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It contains two placements of the photon: electric and magnetic fields on links between neighbouring block centres, and a phase chi on each site that enters the odd half-tick by minimal coupling. This note gives the exact relation between them, says what a block-local update can do with chi, and asks what fixes the link speed. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## One complex

Every site is the midpoint of the bond from its even block centre to its odd block centre, with offset in {+1, -1}^3, so each even centre has 8 distinct odd neighbours. The even-even and odd-odd partition links are the next-nearest bonds of this body-centred lattice. Each mixed plaquette spans two even and two odd blocks and is a tetrahedron whose free edges are one even link along axis a and one odd link along an axis b different from a. Per cell the complex has 2 vertices, 8 + 3 + 3 edges, 24 triangles and 12 tetrahedra, so its Euler number is 0.

## The map from site phases to partition links

Let Pi send chi to the mean holonomy of the four two-site paths between neighbouring even centres. Odd-block gauge phases drop out and even-block phases enter as the even-lattice gradient, so Pi is gauge covariant and Pi(chi) is an even-lattice connection. Per cell chi carries 8 - 2 = 6 gauge-invariant values, Pi(chi) carries 2 and the kernel carries 4. At k = 0 the kernel is exactly the four gapped branches of the twelve-rhombus magnetic form (eigenvalues 8, 8, 8, 24), and the zero modes are the uniform connection and one gauge mode. The massless pair is visible to Pi, with |Pi v|/|v| = 0.707, and transverse, with longitudinal part at most 2.0e-3. The link fields are therefore conjugate to and the curl of Pi(chi). The connection itself sits on sites, and only its holonomies sit on partition links.

## What a block-local update can do

Inside one block the 8 sites lie in 8 different blocks of the other partition, so gauge phases shift each chi independently. The commutant of independent shifts, checked for Z_5 on two registers, is the N^2 = 25-dimensional algebra of functions of the electric fluxes alone. A magnetic term is never block-local, because mixed plaquettes are not.

A register hopped by the supplied coin carries the rotation class invariant -1 (double-valued); the flux-free control gives +1. Its quanta have half-integer helicity, so a fermion cannot emit one singly, and the photon cannot reuse the fermion coin.

## What fixes the link speed

The register's stress clause asks for a flat background in which every source's stress is symmetric. In g = diag(-alpha, 1, 1, 1) this needs alpha = v_g v_p to be the same for every source. The fermion gives alpha = 1/3 (runner value 0.33333330), so a link source needs c_link^2 = 1/3 at leading order for any placement: tau^2 g_E g_B = 2/3 for the quadratic site-phase law and Courant number C = 1/sqrt(3) for the Yee law. The Yee band at C = 1/sqrt(3) equals the fermion band at all 500 sampled K to 5.3e-15.

Beyond leading order the runner measures (v_link - v_fermion)/c per w^2 over 123 directions. For the continuous-time site-phase law the range is [-0.0417, +0.0521]. For the leapfrog law with electric and magnetic half-ticks it is [-0.0000, +0.0937], equal along face diagonals. As estimates against measured bounds: the continuous-time law is slower by 0.042 w^2 = 9.4e-17 at 1e20 eV, above the 4.4e-23 proton vacuum-Cherenkov bound, if protons carry the fermion's O(K^2) term. The leapfrog law is faster by at most 4.1e-26 at 1.4 PeV, below the 2.7e-19 photon-decay threshold.

## Coarser rungs

Under the massive tick no proper subset of sites conserves its own number. Under the massless tick only the two sublattice sectors do, and 90-degree rotations swap them. Fermion-pair collective modes at fixed total K form a continuum at or above w(K) (w(K) = 0.2639, pair energies in [0.3206, 5.8443]), not a two-helicity pole. Counting alone allows one-mode carriers from rung 3 (216 modes against 64 for Z_5 links), but not at rung 1 (8 against 64). Using them would need sites assigned to roles and a number constraint, which the block-update law does not supply.

## Checks

The runner prints `TOTAL: PASS=16 FAIL=0`. Its PASS lines cover the midpoint and tetrahedron geometry, gauge covariance and the rank count of Pi, the kernel at k = 0, the transverse massless pair, the electric-flux commutant, the double-valued coin class, the stress-fixed speed, Yee agreement with the fermion band, the two beyond-leading-order comparisons, and the three coarse-rung counts.

## Supplied and boundary

Supplied: the coin, the two partitions, minimal coupling through site phases, the quadratic and Yee link laws, the leapfrog time split, the block of 2a, and the stress clause, whose use here to fix the link coupling is new. Cited from the literature and not rederived: the Coulomb phase of Z_N for N >= 5 and of U(1) lattice gauge theory. Measured bounds enter only as estimates. No photon field, carrier register, link law or coarse-rung carrier is established.
