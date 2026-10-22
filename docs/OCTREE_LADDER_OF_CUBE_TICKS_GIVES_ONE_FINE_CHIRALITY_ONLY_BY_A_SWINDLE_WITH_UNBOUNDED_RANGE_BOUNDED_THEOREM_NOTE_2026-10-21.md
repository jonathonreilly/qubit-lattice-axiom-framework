---
claim_id: octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For a supplied octree ladder (coarse cells of the nested tilings as extra sites, every rung running the register's cube tick at the fine step, cells coupled to their eight children through X = W(1 - g5)/2), with a copy mass above the exchange one light Weyl field of one handedness sits on the fine lattice and its mirror on the top rung; with infinitely many rungs the ladder stays unitary and the mirror sits on no finite rung, but only by an Eilenberg swindle in which rung j acts across 2^(j+2) sites, and any bounded truncation restores it; the ladder supplies no tilt, its one exact charge is anomalous, and it gives 1 generation; the coarse sites, the coupling and any adopted rule are not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_2026_10_21.py
---

# An octree ladder of cube ticks gives one fine chirality only by a swindle with unbounded range

Claim type: bounded_theorem.
Primary runner: `scripts/octree_ladder_of_cube_ticks_gives_one_fine_chirality_only_by_a_swindle_with_unbounded_range_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and says a finite-range update gives no net chirality at any rung. This note builds a ladder in which the coarse cells of the nested tilings are themselves sites, and asks whether it gives one chirality on the fine lattice, a spectral tilt, or gauge and generation content. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) contain no coarse sites; adding them changes the Lattice and Qubit axioms and breaks nearest-neighbour admissibility in physical distance.

## Statement

Supplied: rung j's cells are the 2^(j+1) blocks of the nested tilings, one mode per corner; each rung runs the register's cube tick at the fine step st; each cell exchanges with the same corner of its 8 children (amplitude 1/sqrt8) through X = (W + iG4)/2 = W(1 - g5)/2, with exchange kappa = 0.5 and copy mass M = st > kappa st.

1. The tick supplies its own fifth matrix G4 = i W g5 and its own isotropic Wilson term (K^2/6) W, and the copy mass is a Dirac mass on copy 1.
2. The exchange is H5 = T + T^+ with T an isometry, so H5^3 = H5 and the kernel holds exactly 8 modes per fine cell for every number of rungs R. The ladder above rung 1 is the ladder on a lattice twice as coarse.
3. With the copy mass, the fine rung carries Weyl index +1 and the top rung -1; without it, +2 and -2.
4. With infinitely many rungs the ladder is unitary and the mirror sits on no finite rung, by an Eilenberg swindle; bounded range restores the mirror.
5. The only block-local operator commuting with every ladder block is the identity, so total mode number N is the one exact charge, and it sits on one Weyl field of one handedness (anomalous). The generation count is 1 (2 without the copy mass).

## Derivation

Unitarity. |H5| = 1 gives exp(-i tau H5) = 1 - i sin(tau) H5 + (cos tau - 1) H5^2, and every rung tick is a block unitary, so the ladder is a quasi-free automorphism for any number of rungs.

Swindle. Three cell-child swap layers give Shift_j x Shift_(j+1)^-1 exactly, and the depth-6 circuit gives Shift on rung 0 and the identity on every other rung. Stopping the circuit at rung 2, which bounds its range, brings Shift_2^-1 back on the cut rung. So the ladder evades the conclusion of Nielsen-Ninomiya only by giving up bounded physical range: rung j acts across 2^(j+2) sites. With bounded range and bounded mode density the cited GNVW index puts the mirror back on the truncation rungs.

Mirror decoupling. At fixed physical momentum the mirror's energy is 2^R times the boundary's, so its light states fill a ball shrinking as 2^-R and its share of phase space falls as 8^-R. At zero momentum the light chain decouples exactly. A species mass mu pairs boundary and mirror into a residual mass falling by mu/(kappa st) per rung. The fine rate is what hides the mirror: at the zoom rate 2^-j it stays light on coarse rungs.

No tilt. A white start stays white, since an ensemble proportional to the identity is invariant. A rung-j cell is shared by 8^j fine sites, so correlations carried through the tree contribute at most |p|^3 in 3D (|p|^1 in 1D, so 1D toys would mislead).

## Checks

The runner gives `TOTAL: PASS=20 FAIL=0` in 20.1 s.

- A1: the light algebra, G4 anticommuting with a_i and W, X^2 = 0, X X^+ = P+, X^+ X = P- (errors 2e-9, 2e-9, 3e-10).
- A2: K^2 Wilson coefficient 0.1665, spread 8e-8. A3: the copy projector commutes with W, a_i, g5; the copy mass is -M P1 W.
- B1: real space (576 modes) equals the momentum tree to 2e-15; kernel 512 = 8 x 64 at R = 1, 2. B2: self-similarity residual 0 at R = 2, 3.
- C1: Berry flux (2.0, -2.0) with no copy mass; (1.0, -1.0) at R = 1, 2; +1.0 on rung 0 at R = 3; (1.0, -1.0) for the discrete-time ladder.
- C2: bulk gap 0.416, 0.389 st; middle-rung weight below 0.25 st at most 1.6e-3; mirror over boundary energy 1.99 (R = 1), 3.94 (R = 2).
- D1: the boundary state's top-rung weight at |q_R| = 0.5 is 3.2e-4, 7.8e-9, 1.3e-14 (predicted 4.3e-4, 1.2e-8, 2.0e-14); the mirror's weight on the light rung-0 node 1e-2, 1e-5, 5e-8.
- D2: |E| < 4e-11 at mu = 0 for R = 1, 4, 16; at mu = 0.2 st the residual mass ratio per rung is 0.3995.
- D3: weight by rung at the zoom rate [2.0, 0.01, 0.68, 3.31] against [2.0, 0.0, 0.0, 0.0] at the fine rate.
- E1, E2: unitarity; shifts by rung [4095, 0, 0, 0] for the full circuit and [4095, 0, 1, 0] when stopped.
- E3: at st = 0.3, R = 3 on 32^3 sites the support grows 4 sites per tick against the fine cone's 2; probability beyond the fine cone is 8e-8, 3e-8, 5e-8 from a one-cell source and at most 1e-10 from a smooth source.
- F1: rung-1 admixture over q^4 is 0.1106 to 0.1108 (1/9) and the velocity shift over q^2 is -0.0416 (-0.0417), so dv/v = -(ka)^2/2.
- G1: on 40^3 sites the rung-0 density has a white floor of 2.4e-3 (index tends to 0), the all-rung density has index 1.92 (tends to 2).
- H1: commutant dimension 1. H3: generation count 1, never 3.
- F2, F3, H2: the estimates below.

Estimates (not checks). With a = sqrt(8 pi) Planck lengths, at 1.4 PeV the admixture is 2e-49 and dv/v = -1.7e-25 (subluminal, no vacuum Cherenkov), a quadratic scale of 3.4e18 GeV against the GRB 221009A bound above 7.3e11 GeV. If the photon kept the bare band, photons would decay to e+e- above about 71 PeV, an untested prediction. The beyond-cone signal is likewise an untested prediction for Planck-localized sources. A thermal slab mirror adds dN_eff < 0.02 for R >= 2. A link on N would drain fine-lattice charge at about 6e34 per m^3 per s in 1 MV/m parallel to 1 T, excluded by vector-like QED. The measured n_s = 0.965 is 230 and 246 sigma from the indices 0 and 2.

## Boundary

Supplied: the coarse sites (axiom-level), the split, the fine rate, the dimerized coupling X with the sign of G4 that picks the handedness (G4 x s3 would make the content vector-like), kappa = 0.5 with M > kappa st (otherwise both copies bind), the steps 0.04 and 0.3, the Floquet ordering, the unit map and measured inputs. Cited: GNVW. Forced: G4, the Wilson term, the copy mass as wall height, the kernel count, self-similarity, the swindle and the small-momentum laws. Negative results: the single fine chirality needs unbounded range and loses the bounded light cone; the ladder gives no tilt; its one exact charge is anomalous and cannot carry a massless link; it gives 1 generation, never 3. No coarse sites, coupling or rule are established.
