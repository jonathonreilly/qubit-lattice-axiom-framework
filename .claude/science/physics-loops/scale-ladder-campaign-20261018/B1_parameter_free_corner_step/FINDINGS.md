# B1 findings: parameter-free corner step rules (main agent, in progress)

## Exact facts (runner Part 6 and these scripts)

- **Link hopping.** H_link(k)² = 2 at every k in infinite volume, so R_L = H_link/√2 is an exact local reflection. The chiral link orbits Tb1 and Tb2 square to 2 only on the L=4 torus; that is an artefact.
- **Walk R_L(1−2P₂).**
  - The node at k* is 6-fold, G3/2 + E1/2.
  - Four bands leave at ±|q|/√3, each 2-fold; two bands are exactly flat (forced by a dimension count).
  - This is the spin-1 ⊗ spin-½ type.
- **Lemma.** Symmetric factors with a k-independent spectrum give zero velocity to every spin-½ doublet at k*. The large Clifford-phase searches (about 16k + 4k walks) found no Weyl doublet, as the lemma predicts.
- **Diagonal shift S.** The map {d,e}@v → {d,e}@(v+d+e) is a gauge-consistent, symmetric signed permutation (`shift.py`, `S_110_0.npy`). It is exactly unitary, and its spectrum depends on k, so it escapes the lemma.
- **Shift walks.** 3738 walks of the form S·U, S·R_L·U or R_L·S·U (U a Clifford-phase on-site step) have Weyl doublets at k*.
  - The speed is √2/3 (0.4714045), isotropic, with anisotropy ∝ q².
  - Example S·(1−2Q_top): Berry flux +1 at both k* and −k*, but pinned 2-fold lines at quasi-energy π cross the zone.
  - Example S·R_L·(H23·L110): node at −π/2.
    - Weyl doublets at all 8 points (π/2)(±1,±1,±1).
    - At ±k* they are isotropic, speed √2/3, chiralities ±1.
    - At the other 6 they are anisotropic (spread about 0.3), chiralities ±1; the net is 0.
    - Nothing else reaches −π/2 (refined search).
- **Running:** `cube_scan.py`, looking for candidates whose node quasi-energy is reached only at ±k*.
