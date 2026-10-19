# Compact patches with native quantum dressing

Claim type: open_gate. Status: open. Direct author research, independent review pending. This is model development, not an observational test or a stable-particle claim. The target and source comparison are in CONTRACT.md.

## Exact geometry before optimization

Let U_S be the product of physical X operators over a finite set S and H=-sum_x XX-sum_y YY-sum_z ZZ. Pauli conjugation, with no weak-coupling approximation, gives

    D_S = U_S† H U_S-H = 2 sum_(b in boundary_y,z(S)) P_b.

All x-directed XX bonds commute with U_S, including those crossing its boundary. A genuinely interior k by w by ell rectangular block changes 2k ell YY bonds and 2k w ZZ bonds. It has no XX contribution at the two faces normal to x. For a homogeneous reference with correlations C_y=<YY> and C_z=<ZZ>, the exact raw trial energy is

    <U_S† H U_S>-<H> = 4 C_y k ell + 4 C_z k w.

The correlations are properties of the reference, not supplied positive constants. Their signs and quantum response need calculation. The disappearance of XX face terms does not delete XX from H; it is a conjugation identity for this chosen X-product family. It cannot justify isotropy or scalar identification.

For disjoint S,T the exact fusion identity is

    D_(S union T)-D_S-D_T = -4 sum_(y,z bonds joining S to T) P_b.

If the joining correlations are positive in the reference, adjacent raw trials favor coalescence. There is no such diagonal fusion contribution across an x-directed shared face. This is an identity for unrelaxed trial-state expectations, not a theorem about optimized bound states, capture or lifetimes. In particular, <H> for U_S U_T g is not automatically the energy of two separated physical particles. Patch area/volume is not a conserved particle count, and minimizing energy per flipped site would insert a new identification.

`fusion_control.py` checks coefficient dictionaries directly on 12 disjoint compact-patch placements. `mpo_check.py` compares the general 3D matrix-product Hamiltonian with independently formed full Pauli matrices on 6-, 8-, and 9-qubit geometries, with zero differences. Each tensor site has physical dimension two.

## Quantum dressing derived from H

For an exact reference eigenvector Hg=Eg,

    (H-E)(U_S-<U_S>)g = U_S D_S g.

Therefore the individual states U_S P_b g for changed native boundary bonds span the first Hamiltonian-generated dressing of the compact source. This determines the extra states and their coefficients from H. No new potential, repulsive term, coupling or selector is introduced.

The numerical calculation does not assume the MPS reference is an eigenstate. It forms the full Gram matrix G, centered matrix K of H-e and Q of (H-e)^2 directly. For a normalized generalized Ritz vector c, its full-H residual is sqrt(c†Qc-epsilon²). Thus reference error is included, rather than dropped using the eigenvector identity. A Rayleigh value below another trial is variational evidence only; it is not a certified excitation above the actual ground.

On the 72-qubit 3 by 4 by 6 box at MPS bond limit 32, mixing only centered 2x2 and 2x4 patch sources gives lowest reference-relative energy 7.633675 and residual 4.598953. Adding their 20 individual native boundary-bond dressings gives 4.838003 and residual 4.156010. The normalized source overlaps with the lowest dressed state are approximately .4401 and .3217. These are overlaps with nonorthogonal probes, not mutually exclusive size probabilities. Dressing is substantial but this state is not close enough to stationary to establish stability.

## Exact one-layer control and numerical failure preserved

The original one-layer geometry 1 by Ny by Nz has YY and ZZ bonds and no x bonds. It is not a 3D result. An on-site spin rotation and coordinate relabeling give an equivalent XX-ZZ sheet; the physical X patch becomes a Y-product patch. In this second implementation both compatible plane-character families are fixed. All character choices remain explicit model conditions.

For the 4 by 6 sheet the independent selected-sector eigensolver finds a source-visible excitation gap 1.57358678856854 with full residual about 2.3e-14. The squared overlaps with normalized centered 2x2 and 2x4 probes are .0121407773 and .0000337425. A depth-40 full-H Krylov calculation reproduces the energy with residual about 1e-6, and the rotated 6 by 4 calculation agrees. This is finite-volume evidence of genuine strong quantum dressing without an extra interaction. It does not select an intrinsic size or prove an infinite-volume isolated pole.

The 4 by 4 sheet has a source-visible gap 3.4084373433114 and normalized probe weight .1282052. Deep Krylov runs also introduced lower approximate states with source overlaps around 1e-30 and poor residuals; sorting only by Ritz energy would have misidentified them as patch modes. Their presence is preserved in the raw outputs. Source overlap, symmetry controls and an independent eigensolver distinguish them. No stable-size conclusion is inferred from comparing different finite boxes.

## Full 3D tests and remaining work

`ground_states.py` and `refine_states.py` use the unchanged full H on 48, 72 and 108 physical qubits. Centered patches have side boundaries inside the box. The 108-qubit probe family includes 2x2, 2x4, 4x2, 4x4 and two diagonal disjoint 2x2 patches. `volume_ground.py` and `volume_response.py` additionally test thickness one and two on a 96-qubit 4 by 4 by 6 box, including truly volumetric 2x2x2 and 2x2x4 supports. All reference and candidate residuals are reported; finite bond dimension and open boundaries are explicit.

Raw and mixed energies do not by themselves determine a stable size. Needed next: converge reference and dressed candidate residuals, enlarge native dressing beyond one boundary action, compare true separated and merged spectral channels, and measure an internal relative-coordinate size as all box dimensions grow. A mixed state's spatial energy profile can include center-of-mass delocalization; it cannot be equated automatically with internal feature size. The oriented X patch family and anisotropic boxes also do not supply scalar transformation properties.

## Scope of negative language

No no-go is proposed. N1: the actual algebra, MPS, native dressing, Krylov and symmetry/eigensolver routes were attempted; none exhausts larger 3D dressing or thermodynamic spectra. N2: reference, dressing and volume errors are coupled and not counted as independent impossibility walls. N3: supplied H, geometry, state, characters, probes and numerical truncation are explicit. N4: prior thin-string and weak-coupling results do not match a universal compact strong-coupling claim and are not used as exclusions. N5: checks reach individual Pauli bonds, finite sites, finite source-visible modes and finite blocks; no infinite-lattice conclusion. N6: no new axiom is said to be necessary. N7: a more strongly dressed compact state could have a stable relative size below its continuum despite the present trial failures; this is the live counter-route. N8: the prior string block's missing side boundaries motivated this calculation, rather than being treated as a universal wall. The no-go packet is not PASS; this is exploratory partial progress with a positive finite-sheet spectral control and an open 3D target.

The first-step coefficients can also be kept at their exact native values instead of optimizing each boundary bond separately. The resulting four-dimensional source/dressing space has lowest value 4.855944 and full-H residual 4.117123. For the real numerical reference, the discrepancy between actual H-action and U_S D_S g is (U_S-<U_S>)r, where r=(H-e)g. The measured defects 1.41662 and 1.41869 obey the corresponding bounds 1.52731 and 1.43015. `dressing_checks.py` verifies this from separately saved full-H moments. This establishes where the approximation enters; the state dressing itself was not supplied as a new interaction.

The moment implementation is also checked with a deliberately nonstationary random reference on an eight-qubit cube. Independent dense vectors and tensor contractions agree on G,K,Q and the full residual formula to 5.4e-15 (`moment_control.py`). Small residuals of finite-sheet eigenvectors do not cure the much larger 3D reference/candidate residuals.

## Refined 3D result limits

At bond limit 128 the reference residuals on the 48-, 72- and 108-qubit boxes are respectively 1.45171, .84797 and 1.62859. The lowest rectangle-mixture reference-relative energies are 6.45045, 7.58021 and 7.78030, with full residuals 4.90059, 4.49328 and 4.57376. Thus improving reference energy did not turn the restricted patch mixture into a stationary mode. This does not exclude a stable component or a more fully dressed state.

On the 108-qubit refined reference, the eight-site 2x4 rectangle has raw energy 9.40642, compared with 14.35893 for two diagonal four-site patches. This is a same-support-count trial comparison, not a two-particle binding energy: placement and reference correlations differ and no conserved constituent count or scattering threshold has been established. The sixteen-site 4x4 trial has raw energy 12.65748; it must not be misreported as an equal-constituent comparison with the two four-site patches.

On the separate 96-qubit box, raw energies for 1x2x2, 1x2x4, 2x2x2 and 2x2x4 supports are 7.57474, 8.67918, 15.36332 and 17.63423. Their lowest mixed candidate has full residual 5.01655. This is an actual volumetric test, with unresolved reference/dressing error; it is not evidence that a minimum allowed support is a dynamically selected particle size.

## Exact small 3D periodic control

`exact_periodic_cube.py` restores the native wrap bonds in all three directions on a 27-qubit cube, in a selected CSS sector of dimension 4,194,304. The reference energy is -38.19164989239814 with residual 3.2e-13. Single-layer 1x2x2 and volumetric 2x2x2 X sources have raw energies 7.5440296 and 15.0880592. Their mixed Ritz value starts at 8.0702572 with residual 4.94261. Native full-H Krylov dressing lowers it to 4.2831781 at depth one and 1.5766211 at depth eight, the latter still having residual .50705. This independently confirms substantial strong dressing in full 3D without an approximate reference; it does not yet certify that Ritz vector. The periodic box has only a one-site complement in each cut direction, so it cannot establish a surrounding infinite vacuum or a preferred size. `exact_cube_poles.py` separately resolves low eigenvectors and their compact-source weights.

The separate 12-eigenvector calculation resolves a source-visible level at gap 1.423237955386 J, with maximum residual 1.21e-12 among its two returned eigenvectors. Their summed captured weights are .019615815 for the normalized single-layer source and .001179427 for the normalized volumetric source. Summing within the returned degenerate group avoids assigning physical meaning to an arbitrary eigenvector basis. Completeness of every degeneracy is not claimed. Lower returned levels near .463946 and 1.361916 have negligible overlap with these probes. This is a genuine compact-source-visible finite-box eigenmode of the full native 3D Hamiltonian. It is not an independently certified infinite-volume pole, rest mass, scalar irrep, lifetime or preferred feature size. Both source sizes feed the same energy level, so treating the chosen source support as the mode's internal size would be circular. `pole_analysis.py` records the grouping and numerical visibility threshold.
