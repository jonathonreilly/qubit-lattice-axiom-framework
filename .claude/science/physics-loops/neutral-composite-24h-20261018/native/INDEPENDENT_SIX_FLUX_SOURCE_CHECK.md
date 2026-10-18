# Q6 zone-corner source and symmetry check

Disposition: PASS with the root's refined exact probe (P_X+P_Y)/2. Calling bare P_X an exact microscopic A1 operator would be incorrect; its leading N0 projection has that character, but the symmetrized physical probe removes this issue.

## Bloch little-group signs

Use the common cell center c=r+(1/2,1/2) for the two diagonal-pair orientations. A site-centered quarter turn maps r to r'=(-r_y-1,r_x) and exchanges the two orientations, giving a minus sign in their difference. At q=(pi,pi), rotating q changes it by a reciprocal vector whose phase on this half-integer center is also minus. The signs cancel. An axial reflection similarly exchanges the two orientations and produces the half-cell reciprocal phase minus, again canceling. A diagonal reflection has neither sign. Thus the antisymmetric orientation combination is A1 at the zone corner. At q=0 the reciprocal phases are absent: quarter turn and axial reflection give minus, diagonal reflection gives plus, which is B2. These labels refer to the appropriate momentum little group, not a momentum-independent internal scalar.

I checked the discrete coefficient mapping on even R6 and R8: both site-centered C4 and an axial reflection preserve the q=(pi,pi) coefficient vector exactly. Its norm squared in the unordered two-column basis is one. There are 2R^2 distinct diagonal pairs with coefficient magnitude 1/(sqrt(2)R); no further orbit factor is needed for sufficiently large nonwrapping R.

## Exact physical spin operation

A symmetry quarter turn of the compass Hamiltonian includes spin rotation about Z by pi/2. It sends a whole-column X product to the whole-column Y product. For L=10,

 D_Y=i^L D_X product_z Z=-D_X product_z Z.

Only on N0 does product_z Z=1, so D_Y=-D_X there. The two-column products consequently agree on N0, but are not equal operators on wall states. Therefore exact C4 sends P_X to P_Y, after the preceding geometric/Bloch signs cancel; it sends P_Y back to P_X, since (-1)^L=+1 for the reverse spin map. Axial spatial reflection fixes each operator at this momentum. The average P_phys=(P_X+P_Y)/2 is therefore an exact A1 observable and retains the same leading N0 vector, with no extra factor of two in its amplitude or weight.

This also explains why a bare-X source can have the correct leading residue without being an exact scalar: only its A1 component contributes to the A1 mode. The symmetrized definition is cleaner and supports the exact representation claim directly.

## Dressing and residue

For either diagonal pair, P_X reverses the sign of 4L external YY bonds. A virtual transverse two-spin flip costs 8J. The matched initial/final wall-free overlap changes by -2(lambda/8)^2 per reversed bond, while unchanged virtual bonds cancel against normalization. Thus its amplitude factor is 1-Llambda^2/8. P_Y instead reverses 4L external XX bonds and has the identical factor at the supplied equal transverse couplings. Their average has the same factor.

At height ten, two insertions cannot produce a different wall-free column pattern, so no additional order-lambda^2 endpoint component is hidden in this calculation. The lower Q6 eigenvector is the antisymmetric endpoint combination. Its nonminimal Q6 admixture begins at lambda^4 and its non-Q6 admixture at lambda^6; neither changes this second-order amplitude. The source therefore has

 <B_pi,pi|P_phys|ground> = 1-Llambda^2/8+O(lambda^4),
 weight = 1-Llambda^2/4+O(lambda^4),

up to an irrelevant overall phase convention. Even-lambda symmetry excludes odd retained powers. At nonzero zone-corner momentum the translation-invariant ground expectation is zero, so no coherent vacuum piece needs subtracting; for other applications centering should precede a finite-pattern Gram estimate.

Fixed-order local dressings of each source density and the endpoint state have bounded relative support and overlap multiplicity. Their normalized Fourier sum hence has O(1) retained-coefficient norms, rather than O(R). This is the same finite-pattern argument used earlier, now with a compact diagonal-pair source rather than the nonlocal momentum-pair sum.

## Exact-transfer powers

The physical source norm is at most sqrt(2)R (and the average obeys the same bound). With a final absolute Hamiltonian tail O(R^2 lambda^M) and same-fibre orientation gap of order lambda^16, the crude source/projector error is O(R^3 lambda^(M-16)). For R~lambda^-p it is o(lambda^4) when M>20+3p. The stated condition is correct; equality would only supply an O(lambda^4) bound. Ground-projector errors use the larger charge gap and are smaller. Source-transform tails can be kept to the corresponding fixed order.

To resolve a dispersion signal of order lambda^18/R^2, the Hamiltonian tail must satisfy M>18+4p, also as stated. These are fixed-p asymptotic requirements and do not provide a numerical threshold. This check assumes the independently derived Q6 gap/dispersion and matched source transformations; it does not reprove their complete native path classification.

The result is a positive spectral atom of this explicitly defined physical pair source from the selected actual ground, not an on-shell scattering rate or universal force. Spatial A1 at the zone corner does not establish Lorentz-scalar transformation or a long-wavelength continuum field.

Read /tmp/neutral-q6-check.md and /tmp/neutral_q6_motion.py. No repository edits or formal audit.
