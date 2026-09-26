---
claim_id: composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: Supplied u=+1 quadratic Majorana comparator in one copy and a fixed hopping-sign convention.
  Exact four-site periodic reduction and characteristic polynomial at one rational momentum; finite floating-point
  adaptive cube searches and discrete Berry-flux diagnostics. No certified global exclusion of other zeros,
  continuum Chern number, exact node count or dispersion order, spin-Hamiltonian equivalence, ground-sector
  selection, phase, or physical identification.
upstream_dependencies:
- minimal_axioms
- the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
- composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
- composite_site_network_spin_model_ground_state_is_locally_flux_free_on_the_clusters_searched_with_the_projection_exact_bounded_theorem_note_2026-09-25
- composite_site_network_flux_free_sector_lowest_pair_excitation_falls_as_one_over_l_to_4000_sites_and_the_odd_term_thins_the_low_levels_bounded_theorem_note_2026-09-25
runner: scripts/composite_site_network_flux_free_band_touchings_certified_with_the_odd_term_2026_09_26.py
---

# A four-site Bloch reduction and finite band-touching diagnostics

**Type:** bounded_theorem
**Status:** exact algebra and finite numerical diagnostics for a supplied comparator; unaudited.

## Supplied model and exact reduction

Use the colored network and the explicitly supplied real antisymmetric hopping matrix from the linked parent notes, with u=+1 in the parent's oriented bond convention and one of three identical quadratic copies. This does not establish equality to the named positive-J spin Hamiltonian: the parent review found a sign-mapping obstruction. Nor is u=+1 proved to minimize energy, even at kappa=0; other cut representatives and sectors remain distinct.

The site and color rules are invariant under a1=(2,0,0), a2=(0,2,0), a3=(1,1,2). Translation by a3 swaps the z mod 4 cases while shifting both planar parities, preserving site membership and color. Representatives are (0,0,0),(1,0,0),(1,0,1),(1,1,1). Subtract n3=floor(z/2) copies of a3, then n1=floor((x-n3)/2), n2=floor((y-n3)/2) of a1,a2; the residual occupied site is uniquely one of these four. Every bond and oriented odd-path hop becomes t exp(2pi i f.n), paired with its negative conjugate in M(f). Thus H(f)=iM(f) is Hermitian.

For rectangular periodic tori with Lx,Ly divisible by two and Lz divisible by four, allowed f obey f1 Lx/2, f2 Ly/2, and f3 Lz/2-(f1+f2)Lz/4 integral. Fourier decomposition gives the real-space spectrum as the union of four-band spectra. The primary compares 32-,64-,256-site tori at three parameter sets; numerical deviations are finite precision checks, not the proof of translation symmetry.

At isotropic J=1 and f=(1/4,3/4,1/2), every phase is a power of i and exact symbolic evaluation gives

`det(H-lambda I)=(lambda²-48(1/2-kappa)²)(lambda²-48(1/2+kappa)²)`.

For kappa>=0 the middle pair at this point is ±4sqrt(3)|1/2-kappa|; hence it is exactly degenerate at zero for kappa=1/2. The polynomial alone establishes neither dispersion order nor the number or charge of neighboring nodes. The submitted linear/quadratic dispersion assertion lacks a checked expansion here and is not retained.

## Exact bound and its numerical implementation

For an off-diagonal paired hop the operator norm of its change is |t| times the phase difference; for a diagonal hop a factor two suffices. The triangle inequality and |exp(ix)-exp(iy)|<=|x-y| give

`||H(f)-H(f')|| <= lip ||f-f'||_infinity`,

where lip=sum factor |t| 2pi ||n||_1. Weyl's inequality therefore excludes a middle-band crossing in a cube of half-width h if its **exact** center gap exceeds 2lip h, and excludes a zero level if the exact minimum absolute level exceeds lip h.

The runner starts with 40³ cubes and recursively splits uncleared cubes into eight. It uses ordinary floating-point eigensolvers and does not enclose rounding errors, retain a certified lower bound on all clearing margins, or certify phase/constant evaluation. Consequently its cleared cells are numerical decisions, not rigorous exclusion certificates. Historical `certify` function names and the filename do not change that limitation. Uncleared cubes are candidates; their existence does not prove a zero inside them.

## Finite observations reproduced by the primary

- Isotropic kappa=0.3: fourteen search levels leave two groups near f=(0.3549,0.6451,0) and -f, with sup-norm group extent about 1.5e-4. The middle-gap and zero-level searches leave the same cells numerically. The last four uncleared counts are approximately stable.
- Determinant-overlap Berry fluxes for the lowest two sampled bands on spheres of radius 0.01 and 0.03, at meshes32 and64, give rounded values -1,+1. The minimum **sampled** sphere gap is about0.039. Twenty-four slices per axis at mesh48 give integer-valued discrete fluxes whose changes match these group assignments.
- Isotropic kappa=0.1,0.35 leaves two numerical groups; kappa=0.4,0.45,0.6,0.7 leaves six. Single-mesh sphere fluxes round to ±1, with total zero and sum -1 on the f1<f2 side. These sampled couplings do not locate a bifurcation or exclude additional groups between samples.
- At kappa=0.5, four numerical groups have rounded sphere fluxes -2,-1,+1,+2. The two larger-magnitude assignments lie near (1/4,3/4,1/2) and its partner. At this refinement the two broad groups have sup-norm extents about0.14, exceeding the sphere diameter0.04. Those spheres do not enclose the whole uncleared groups, so their fluxes cannot be assigned as the net charges of those groups. Only the polynomial proves the zero at the stated exact momentum.
- At J=(1,0.8,0.6), kappa=0.35, six numerical groups have rounded flux ±1 and sum zero. The revised check also requires integer residual and positive sampled gap, as in the isotropic scans.
- At kappa=0, final uncleared-count ratios are near two. This is a finite line-like diagnostic, not a dimension proof. At J=(1,1,2.5), kappa=0.3, both searches numerically clear every cell; the minimum absolute level on a48³ grid is about1.012. This does not rigorously extend the parent's analytic kappa=0 matching bound to nonzero kappa.

Discrete overlap fluxes need nonsingular overlaps and consistent seams. Even agreement on two meshes and nonzero sampled gaps does not certify a gap across a continuous surface or the continuum Chern number: an admissibility/error argument remains necessary. Sphere and slice consistency are finite diagnostics, not a proof that all continuum nodes were found. The linked finite level-count note also does not supply such a proof.

## Additional exact line identities and a numerical rank-loss diagnostic

For Jx=Jy=1 and Jz=J, set f=(x,1-x,f3), z=exp(2pi i x), w=exp(2pi i f3), c=cos(2pi x), and D=det H. Laurent-polynomial evaluation gives at w=1

`D=16[J²+4c²kappa²-2c-4kappa²-2]²`.

For -1<c<1 the zero-determinant curve is `J²=2(1+c)[1+2kappa²(1-c)]`. Define **C=(w partial_w)²D at w=1 = -partial_f3²D/(2pi)²**. On this curve,

`C=-64[(1+c)(J+2)-J²]²/(1+c)`.

Thus the actual second derivative in fractional f3 has the opposite sign and an additional (2pi)² factor. The submitted unqualified negative-curvature statement used C instead of that derivative. Solving C=0 together with D=0 gives

`c_star=(J-2)(J+1)/(J+2)`, `kappa_star²=J(J+2)/[4(4+2J-J²)]`.

For the positive-J, real-momentum, finite-positive-kappa branch take `0<J<1+sqrt(5)`; the endpoints and c=±1 are excluded from this division. At J=1, c_star=-2/3 and kappa_star²=3/20. These are exact algebraic statements about the supplied matrix. Vanishing determinant curvature by itself is not a proof of a specified directional velocity, node splitting, or charge transfer.

The runner additionally projects H's three momentum derivatives onto the numerically selected two near-zero modes at J=1 and computes the determinant of their Pauli coefficients. The submitted derivative-root search selected x=1/2 at kappa=0.35, whose spectrum is (-2,-2,2,2), not a node. The corrected calculation selects the explicit zero-determinant branch c=-(1+4kappa²)/(1+sqrt(1+4kappa²+16kappa⁴)), x=acos(c)/(2pi), then verifies the two middle eigenvalues are near zero and the outer levels remain separated. The submitted velocity determinant at0.35 is therefore not retained. In 50-digit arithmetic that determinant changes sign between kappa=0.35 and0.40 and its root agrees with sqrt(3/20). This is a high-precision rank-loss diagnostic, not a certified continuum topology or dispersion expansion. The adaptive searches at J=0.5 and1.5 leave two groups below and six above nearby sampled couplings. Finite group counts and local sphere fluxes do not prove an exact global two-to-six bifurcation or a net charge for groups not enclosed by those spheres.

## Boundary and review

One supplied quadratic copy and one chosen sector, with no adopted premise, physical particle identification, spin ground-state conclusion, thermodynamic phase claim, or audit verdict. Exact reduction, the rational-momentum polynomial and the analytic Lipschitz inequality are retained; global numerical certification, dispersion expansion and continuum topological interpretation remain open. Review narrowed the original claims and added finite-spectrum/overlap guards without reducing the search grid or tolerances. Seven primary checks reproduce the full submitted parameter grid. Original source is frozen at PR9273 head2eefc98c4ccc11ea0a6152cbbf5fceae0310c34d.

## Inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24](COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25](COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_SECTOR_LOWEST_PAIR_EXCITATION_FALLS_AS_ONE_OVER_L_TO_4000_SITES_AND_THE_ODD_TERM_THINS_THE_LOW_LEVELS_BOUNDED_THEOREM_NOTE_2026-09-25](COMPOSITE_SITE_NETWORK_FLUX_FREE_SECTOR_LOWEST_PAIR_EXCITATION_FALLS_AS_ONE_OVER_L_TO_4000_SITES_AND_THE_ODD_TERM_THINS_THE_LOW_LEVELS_BOUNDED_THEOREM_NOTE_2026-09-25.md)
