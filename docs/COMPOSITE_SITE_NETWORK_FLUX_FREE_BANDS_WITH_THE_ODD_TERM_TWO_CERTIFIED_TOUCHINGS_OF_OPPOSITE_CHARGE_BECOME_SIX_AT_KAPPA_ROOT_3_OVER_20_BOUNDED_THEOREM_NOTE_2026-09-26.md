---
claim_id: composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied colored periodic network of composite sites of the landed network note, bonds J_lam and the three-site odd term kappa in the sign convention of open PR 9255, in the sector with every bond variable u = +1 (open PR 9255's locally flux-free sector), one of the three identical free-Majorana copies. Exact: the site and colour rules are invariant under (2,0,0), (0,2,0), (1,1,2), four sites per cell, and the 4x4 Bloch matrix reproduces the real-space levels of the 32-, 64- and 256-site tori (deviation 2.7e-14); at f = (1/4, 3/4, 1/2), isotropic J = 1, the characteristic polynomial is (l^2 - 48(1/2 - kappa)^2)(l^2 - 48(1/2 + kappa)^2). Certified by Weyl's inequality with an explicit Lipschitz constant on adaptive cubes of the fractional zone (floating-point eigenvalues): at isotropic J, kappa = 0.3 the middle two levels meet, and a level vanishes, nowhere outside two groups of diameter 1.5e-4 at f = (0.3549, 0.6451, 0) and -f, with sphere Chern numbers -1 and +1 of the lowest two bands and slice Chern numbers that jump by the enclosed charges; two groups (charges -1, +1) at kappa = 0.1 and 0.35; six groups of charge +-1 at kappa = 0.4, 0.45, 0.6, 0.7 and at J = (1, 0.8, 0.6), kappa = 0.35, total charge 0, the f1 < f2 side -1 throughout; at kappa = 0.5 the off-plane groups meet at (1/4, 3/4, 1/2) and its partner with charges -2 and +2. The determinant of the velocity matrix of the touching on the line f = (x, 1 - x, 0) changes sign between kappa = 0.35 and 0.40 at a root that equals sqrt(3/20) to 50 digits, where the touching sits at cos(2 pi x) = -2/3 (high-precision identifications, not symbolic proofs). At kappa = 0 the uncleared count doubles at each halving, as a line of touchings would require; at J = (1, 1, 2.5), kappa = 0.3 every cube is cleared. No ground-sector claim at kappa != 0, no count of points inside a group, no phase and no physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
runner: scripts/composite_site_network_flux_free_band_touchings_certified_with_the_odd_term_2026_09_26.py
---

# The composite-site network's flux-free bands with the odd term: two certified touchings of opposite charge, which become six at κ = √(3/20)

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact reduction and identity, and a certified finite computation, for one sector of the supplied model; unaudited.

## Result

The landed network note located two candidate crossings of the flux-free
Majorana bands at `κ = 0.3`, near `k/2π = (0.355, 0.645, 1)` and
`(0.645, 0.355, 1)`, with opposite discrete Berry fluxes, and stated that
this "does not exclude additional nodes elsewhere". This block covers the
whole zone with a certificate, and follows the touchings as `κ` grows.

- **An exact four-band reduction.** The network's site and colour rules
  are invariant under the translations `(2,0,0)`, `(0,2,0)` and `(1,1,2)`,
  which leave four sites per cell. In the sector with every bond variable
  `u = +1`, the hopping problem is a `4 × 4` Bloch matrix `H(f) = i M(f)` of
  the fractional momentum `f ∈ [0,1)³`. Its levels at the momenta of the 32-,
  64- and 256-site tori reproduce the real-space levels of those tori to
  `2.7 × 10⁻¹⁴`, at `κ = 0`, `0.3` and anisotropic couplings.
- **A certificate over the whole zone.** Weyl's inequality bounds how far
  each level can move across a cube of half-width `h`: by `lip · h`, with
  `lip` the sum over hopping terms of `|t| 2π |n|₁` (`98.0` at isotropic `J`,
  `κ = 0.3`). A cube is cleared when the gap between the middle two levels at
  its centre exceeds `2 lip h`, so they cannot meet inside it, and separately
  when every level at its centre exceeds `lip h` in size, so none can reach
  zero inside it. Uncleared cubes are halved, fourteen times at `κ = 0.3`,
  down to half-width `1.5 × 10⁻⁶`.
- **At κ = 0.3: two groups, charges −1 and +1.** Every cube of the zone is
  cleared except those in two groups of diameter `1.5 × 10⁻⁴`, centred at
  `f = (0.3549, 0.6451, 0)` and at `−f`. Both certificates leave exactly the
  same cubes, so no level reaches zero anywhere else. The uncleared count
  stays near 15 200 at every halving, as isolated linear touchings would
  give. Spheres of radius `0.01` and `0.03` around the groups carry Chern
  numbers `−1` and `+1` of the lowest two bands (meshes 32 and 64 agree),
  with middle gap at least `0.039` on the spheres. Positions and charges agree
  with the landed runner's two candidate crossings.
- **Slices agree.** On 24 slices along each fractional axis, the Chern
  number of the lowest two bands is an integer, and between neighbouring
  slices it jumps by exactly the charge of the groups between them: along
  `f₁` it is `+1` outside the interval between the groups and `0` inside,
  along `f₂` it is `−1` outside and `0` inside, and along `f₃`, where both
  groups sit at `f₃ = 0`, it is `0` throughout.
- **Two become six.** At isotropic `J` the certificate leaves two groups at
  `κ = 0.1` and `0.35`, and six at `κ = 0.4`, `0.45`, `0.6` and `0.7`. The
  total charge is always `0`, and the groups on the side `f₁ < f₂` of the
  `κ = 0.3` group at `(0.355, 0.645, 0)` always carry `−1` in total: at
  `κ = 0.4` a `+1` group on the plane `f₃ = 0` at `(0.368, 0.632, 0)` and two
  `−1` groups at `(0.345, 0.655, ±0.129)`. As `κ` grows the off-plane pair
  moves apart in `f₃` (`±0.298` at `κ = 0.45`), and leaves the line
  `f₁ + f₂ = 1` beyond `κ = 0.5` (`(0.120, 0.681, 0.400)` and
  `(0.319, 0.880, 0.600)` at `κ = 0.6`).
- **Where two become six: κ = √(3/20).** Follow the touching of
  charge `−1` along the line `f = (x, 1 − x, 0)`. The determinant of its
  `3 × 3` velocity matrix (the derivatives of `H` projected on its two zero
  modes) falls from `95.8` at `κ = 0.35` to `−13.0` at `κ = 0.40`, and its
  root, computed with 50 digits, equals `√(3/20) = √15/10 = 0.38730` to better
  than `10⁻⁴⁰`; there the touching sits at `cos(2πx) = −2/3` to the same
  precision. At that point the touching's velocity along `f₃` vanishes, its
  charge turns from `−1` to `+1`, and the two off-plane touchings of charge
  `−1` leave it, keeping the side's total at `−1`. These two identifications
  are high-precision numerical ones, not symbolic proofs.
- **Where they meet, exactly.** At `f = (1/4, 3/4, 1/2)` and isotropic
  `J = 1`, the characteristic polynomial of `H` is exactly
  `(λ² − 48 (1/2 − κ)²)(λ² − 48 (1/2 + κ)²)`: the middle levels there are
  `±4√3 |1/2 − κ|` and meet at `κ = 1/2`. At `κ = 0.5` the certificate leaves
  four groups, and spheres of radius `0.02` about `(1/4, 3/4, 1/2)` and its
  partner carry charges `−2` and `+2`, beside the `+1`, `−1` pair on the
  plane: the two off-plane `−1` groups meet there. The dispersion at that
  point is linear along `(1, −1, 0)` and quadratic along `(1, 1, 0)` and
  `(0, 0, 1)`.
- **An anisotropic case.** At `J = (1, 0.8, 0.6)`, `κ = 0.35` the certificate
  leaves six groups of charge `±1`, total `0`.
- **Two controls.** At `κ = 0` the uncleared count doubles at every halving
  (ratios `1.997`, `2.000`, `1.997`), as a line of touchings would require
  and as isolated points would not. At `J = (1, 1, 2.5)`, `κ = 0.3` both
  certificates clear every cube, and the smallest level size on a `48³` grid is
  `1.012`: the gap that the landed note's matching bound gives at `κ = 0`
  stays open at this `κ`.

These are statements about one free-Majorana copy in one sector of the
supplied model. The certificate uses floating-point eigenvalues, with errors
near `10⁻¹⁴`, far below the clearing margins.

## Setting and decision points

- **D-network, D-bonds, D-odd, D-majorana (supplied, landed).** The colored
  periodic network, bonds and odd term of the landed network note
  `THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  in the six-Majorana representation of the landed composite-site note
  `COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
  The filenames are historical; the note bodies govern.
- **D-sector (open PR 9255).** The sector with every bond variable `u = +1`
  in the key orientation of open PR 9255, which is its locally flux-free
  sector. That PR found this sector lowest on every cluster it searched at
  `κ = 0`, and at `κ = 0.3` on the annealed 64- and 256-site clusters, but a
  half-fluxed sector lower on 32 sites at `κ = ±0.3`. No ground-sector claim
  is made here for `κ ≠ 0`.
- **D-sign.** The odd term's sign convention of open PR 9255, which the
  landed runner calls `ODD_SIGN = +1`; both give the same positions and
  charges at `κ = 0.3`.

## Method

1. **Reduction.** Each site of the network reduces to one of four cell
   representatives `(0,0,0)`, `(1,0,0)`, `(1,0,1)`, `(1,1,1)` plus an integer
   combination `n` of the three translations. Every bond `2 J_λ u` and every
   odd-term hop `2κ u u` becomes a term `t e^{2πi f·n}` of `M(f)`. The torus
   `(Lx, Ly, Lz)` allows exactly the `f` with `f₁ Lx/2`, `f₂ Ly/2` and
   `f₃ Lz/2 − (f₁ + f₂) Lz/4` integer.
2. **Clearing cubes.** For `f, f'` in one cube,
   `‖H(f) − H(f')‖ ≤ Σ |t| |e^{2πi f·n} − e^{2πi f'·n}| ≤ lip · ‖f − f'‖_∞`
   (twice the term for a hop between images of one cell site), so each level
   moves by at most `lip · h` from the centre. Starting from `40³` cubes,
   cleared cubes are dropped and the rest are split into eight.
3. **Charges.** Chern numbers of the lowest two bands on spheres (latitude–
   longitude grid with shared poles and seam) and on slices (periodic seams),
   by the lattice link method with determinants of two-band overlaps.
4. **The identity.** At `f = (1/4, 3/4, 1/2)` every phase is a power of
   `i`; the runner builds `H` with `κ` symbolic and checks the factorized
   characteristic polynomial exactly.
5. **The split point.** With 50-digit arithmetic, the touching on the line
   `(x, 1 − x, 0)` is the root of `∂ₓ det H`, and the velocity matrix is
   `v_{ia} = ½ tr(P_i σ_a)` with `P_i` the derivative `∂_i H` projected on the
   two zero modes; `κ_c` is the root of `det v`.

## Relation to other work

- The landed network note's runner found the two candidate crossings at
  `κ = 0.3` and their opposite discrete fluxes. The certificate adds that, in
  this sector and at these couplings, no other touching of the middle bands
  and no other zero level exists in the zone, and it follows the touchings
  through the change from two to six.
- Open PR 9264 counted physical levels of the flux-free sector on clusters
  up to 4000 sites: count exponents near 3 at `κ = 0.3` and between 2 and 3 at
  `κ = 0`. Isolated linear touchings at `κ = 0.3` and a line-like set at
  `κ = 0` are what those exponents would approach; that is a reading of
  finite counts, not a derivation of them.
- **Prior art (not premises).** Band touchings with opposite Berry charges
  in three-dimensional Kitaev-type Majorana models with time-reversal-odd
  terms (M. Hermanns, K. O'Brien, S. Trebst, Phys. Rev. Lett. 114, 157202
  (2015)); the lattice link method for Chern numbers (T. Fukui, Y. Hatsugai,
  H. Suzuki, J. Phys. Soc. Jpn. 74, 1674 (2005)); Weyl's eigenvalue
  inequality (standard).

## Boundary

- One sector (`u = +1`) and one free-Majorana copy; the three copies are
  identical. No statement about other sectors or about which sector holds
  the ground state at `κ ≠ 0`.
- The certificate places the touching set inside the listed groups and
  gives each group's net charge; it does not count the touching points inside
  a group. The split point `κ_c = √(3/20)` and the position `cos(2πx) = −2/3`
  are identified to 50 digits, not derived symbolically.
- The `κ = 0` doubling is a finite-level diagnostic of a line-like set, not a
  proof of its dimension.
- No phase, no thermodynamic-limit statement about the spin model, and no
  physical particle identification.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_band_touchings_certified_with_the_odd_term_2026_09_26.py
```

Seven checks; prints `TOTAL: PASS=7 FAIL=0` in about 80 s.
