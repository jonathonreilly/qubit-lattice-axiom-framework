---
claim_id: wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the update of the candidate laws register and supplied wall models, the zoom ladder keeps W3 and is locked to momentum, the step pi/2 tick has index 0 at quasi-energy 0 and pi in every site-phase background, and exact mode number with the mirror reflection forbids gapping the mirror alone, so none of the three routes gives net chirality under the register as written; a supplied internal-index wall binds Weyl content at its ends; no chiral family, gapped mirror phase or adopted rule is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_2026_10_21.py
---

# Wall, pump and mirror-gapping routes to chirality under the candidate laws

Claim type: bounded_theorem.
Primary runner: `scripts/wall_pump_and_mirror_gapping_routes_to_chirality_under_the_candidate_laws_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note tests three routes to net chirality against it: a domain wall along an internal or zoom coordinate, Floquet pumping between quasi-energy 0 and pi, and gapping the mirror through the response law. None works with the register as written. A wall along a supplied internal index does bind Weyl content at its ends, but only with rules the register does not contain. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## Statement

1. Zooming to the next rung keeps W3, and the zoom level is locked to momentum, so no rung holds a light field down to k = 0.
2. At step pi/2 the tick is a product of two traceless reflections, and its index at quasi-energy 0 and pi is 0 in every site-phase link background.
3. The register's laws conserve the total mode number N exactly. Every mass that keeps SU(2)_even x SU(2)_odd pairs the family with the mirror, and the exact mirror reflection maps one onto the other, so no history allowed by the register gaps the mirror alone.
4. A Wilson-Dirac chain along a supplied internal index, built from the tick's own algebra, binds left-handed content at one end and right-handed at the other.

## Derivation

Finite circuits. A finite product of block-local unitaries has W3 = 0 and W1 = 0 at any depth, step, mass, link phases or rung, because each factor deforms to a constant in the connected group U(n). The same holds sector by sector for a symmetry carried through the factors. That finite-range non-circuit unitaries also have W3 = 0 is the cited vanishing of SK1(C[Z^3]).

Zoom. Folding a walk to the next rung leaves W3 unchanged. In the Haar multiresolution the weight of momentum k on level n is f_n(k) = sin^4(2^(n-2) k)/(4^(n-1) sin^2(k/2)), at most (pi^2/4) 4^(n-2) k^2, and the profile moves one level per octave of k. Carrying a 2^n-site cell's internal index unchanged to the next cell is a nearest-neighbour swap circuit of depth 2^(n+1) - 1, so the fine light cone is kept.

The tick's own chirality operator. At K = 0 the tick gives {A_a, A_b} = 2c^2 delta_ab and mass matrix beta = W. Then g5 = -i A1 A2 A3/c^3 is a traceless 8-site block operator, and the commutant is M_2, the copy factor.

Wall ends. For a Wilson-Dirac chain along an internal index built from (A_a, W), the near end holds the X = -1 space of X = i beta' G4', where X commutes with every A_a and anticommutes with beta'. With X = -g5 both copies bind left-handed at one end and right-handed at the other, and all 24 rotations survive. With a copy-mixing mass W s1 and X = -s3 one whole copy binds at step pi/2; there C3 turns the mass by 120 degrees, so rotations survive only at long wavelength. The end brings back doublers at X, M and R unless tau(2 - m0) stays below the tick's smallest doubler gap, about 1.15 eps.

Two reflections. For U = R1 R2, tr R1 on the U = +1 space is (tr R1 + tr R2)/2 and on U = -1 it is (tr R1 - tr R2)/2. At step pi/2 the tick is W_o W_e with W_o U W_o = U^dag, a Floquet Ginsparg-Wilson form, and both W stay traceless reflections under any site-phase links. So the index at 0 and pi is 0. The 2D overlap operator gets a nonzero index only because sign(H_W) is not ultralocal.

Mirror gapping. Every term of the register's update and response commutes with N. With c-number links every realised history is a free block circuit, so the response law has no four-fermion vertex. One family with a right-handed neutrino has N-Y^2 anomaly -2 and N-SU(2)^2 anomaly +2, with the mirror opposite. With N and Y exact on-site, the free case is ruled out sector by sector; the interacting case uses cited 't Hooft anomaly matching. An instanton vertex changes N by 4 per family, so a gapping term must break U(1)_N to at most Z_k with k dividing 4. The mirror reflection M = (odd rotation)(inversion) is exact at every step and mass and maps the family onto the mirror on the same cells. The register states that inversion swaps left and right; in fact inversion alone swaps SU(2)_even and SU(2)_odd and leaves the copy label fixed, and M is the symmetry that exchanges family and mirror.

Floquet pumping in the 3D bulk is forbidden by the finite-circuit result. An effective 3D unitary with W3 nonzero exists only at the end of a 4D bulk, so that route reduces to the wall.

## Checks

The runner gives 18 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- Zoom: a quasi-local W3 = -1 walk folded to 16 bands gives -0.999992 then -0.999995, and the register's tick gives 3.1e-20. The Haar formula holds to 2e-15, with mean levels 11.148, 10.148, 9.148, 8.149, 7.149 at successive octaves. Swap depths are 3, 7, 15.
- 1D wall at step 0.30: layer 0 holds one right-mover crossing w = 0 only at k = 0 and the last layer one left-mover, with leakage ratio 0.4000 per layer.
- Tick algebra at steps pi/2 and 0.04 (c = 0.5774, 0.0231); with X = -g5 the end Berry fluxes are +-2.000 at both steps and both orientations.
- Doublers: off K = 0 the ratio of end to bare |w| is 0.0004 at eps = 0.04, tau = 0.6 (doublers return) and 0.81 at tau = 0.02. The copy wall at step pi/2 gives sector fluxes +-1.0, doublers gapped at 0.85, and is symmetric under M with layer reversal to 8.9e-11.
- On the rung-1 cell, one (4,2), the plain end has SU(4)^3 anomaly 4. An end with an involution Xi on (4,2,1) + (4,1,2) is anomaly-free, but that content is not in the rung-1 cell.
- Two-reflection traces are exact integers. On a 4^3 torus at step pi/2 the free tick has dimensions (8, 8) at 0 and pi with W_o-traces 0, and random links give (0, 0). The 2D overlap gives index 0, -1, -2 in flux 0, 1, 2 with a far element 4.0e-3.
- N is exact; a four-mode term has [N, O] = -4 O. The 4 symmetric masses all anticommute with s3. The mirror reflection is exact to 4e-15.

## Against measurement (estimates)

A Planck-suppressed term changing N by 4 gives a proton lifetime near 8e42 yr, against the bound of 2.4e34 yr. A massless mirror coupled through sphalerons would thermalise and add Delta N_eff of about 1.04, against N_eff = 2.99 +- 0.17, so it is excluded and the mirror must be gapped. A leakage mass below 0.05 eV at |1 - m0| = 0.4 and cutoff M_P/3 needs at least 73 layers; at m0 = r the chain dimerises and the end modes are exact for any length of at least 2. The copy wall needs step pi/2, which the register's bound eps < 0.04 excludes.

## Boundary

Supplied: the internal index carried in parallel, the synthetic mass beta', m0, r, tau, the layer count, Xi, the four-mode term changing N by 4 and its symmetry, and the wall orientation, which is where handedness enters. Cited, not rederived: the vanishing of SK1(C[Z^3]), 't Hooft anomaly matching and the existence of a gapped symmetric mirror phase. No interacting test of the gapped mirror was run. Under the register as written all three routes give no net chirality. Chirality is accommodated by an oriented supplied rule, not derived. No chiral family, gapped mirror phase or adopted rule is established.
