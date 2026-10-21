# Exact reference energy for the signed square selector

ROOT-authored algebraic supplement, requiring a distinct check. This makes the exact ground-energy subtraction in the static selector certificate explicit. It changes no runtime construction, selector field, preparation budget or physical assumption.

Write r=h/Delta, u=r^2, and take 0<r<=1/64. For the signed selector Hsel=H0+h sum(I-s_r X_r), prod s=sigma, remove the exact identity4hI and divide byDelta. Sign conjugation and an all-four-Z conjugation identify its F=sigma and F=-sigma sectors with the previously checked omega=+1 and omega=-1 scalar-square matrices, respectively. The all-four-Z conjugation changes the sign of all four fields and preserves F; one-Z conjugation exchanges F sectors and reverses one field sign. Thus the characteristic polynomials already computed in the scalar-square check apply, not the interacting twelve-gadget energy formula.

That exact output gives the plus-sector factor

    (E-2)^4 [E^4-8E^3+(20-16r^2)E^2
                              +(64r^2-16)E-32r^2],

up to a nonzero overall sign. Put w=2-E. The quartic becomes

    w^4-(4+16u)w^2+32u.

Define positive real quantities

    C=sqrt(1+16u^2), D=sqrt(1+4u),
    L=sqrt(2+8u+2C), M=sqrt(2+8u-2C).

The smaller radicand is positive: (1+4u)^2-(1+16u^2)=8u>0. The full plus-sector spectrum is

    2 (multiplicity4), 2-L, 2+L, 2-M, 2+M.

Its unique lowest eigenvalue is 2-L. The minus-sector factorization gives the complete spectrum

    2-2r (multiplicity2), 2+2r (multiplicity2),
    1-D, 1+D, 3-D, 3+D.

On the stated small domain the unique minus-sector lowest eigenvalue is1-D. These are full eight-dimensional sector spectra, including the repeated roots; neither spectrum refers to a single data column in an attached router.

Therefore the exact selector ground energy and the two-low-sector splitting are

    e_sel=4h+Delta(2-L),
    gap_sel=Delta(L-1-D).                              (1)

The positivity of the splitting can be proved without a truncated expansion. Rationalizing gives the exact identity

    gap_sel = 4Delta u^2
       [8+16u/(C+1)+4/(D+1)] / [(C+D)(L+1+D)].         (2)

Every factor on the right is positive. To verify (2), first use L^2-(1+D)^2=4u+2(C-D), rationalize C-D, and then use C+D-2=16u^2/(C+1)+4u/(D+1). No approximate phase or energy subtraction occurs.

The remaining fourteen states do not produce a smaller gap. In each F sector the zero-space dimension at h=0 is1 and the complementary H0 gap is2Delta. Weyl bounds every other centered energy below by2Delta-4h. The lower selected energy is<=0 by a cat trial state. The two low eigenvalues each lie within4h of0; their splitting is<=8h<Delta on r<=1/64, whereas every complementary gap exceedsDelta. Hence (1) is the exact full selector spectral gap, not merely a splitting between two possibly excited states. Positivity of (2) selects F=sigma. Signed fields have identical spectra by the local Z conjugation.

A subtraction-free expression for the small centered ground correction is

    e_sel=4h-Delta [8u+32u^2/(C+1)]/(L+2).            (3)

Equations(1) and(3) are algebraically identical. Equation(3) avoids subtracting2 from a nearby square root; (2) similarly avoids subtracting near-equal low energies. They do not solve the experimental or numerical precision requirement in an excess-energy certificate. In particular E_sel=Tr(A_sel omega)-12e_sel must still be bounded with enough absolute accuracy for its actual allowance. Using a fourth-order Taylor truncation without a remainder bound is not justified.

As u tends to zero, (2) gives gap_sel/(Delta u^2)->5, consistently with the previously checked fourth-order coefficients. The static-selector theorem uses its more conservative g_sel=4h^4/Delta^3 on r<=1/(4*32^3). That lower bound, all h/time allocations, and the exact reference-safe energy comparison remain unchanged here. One may evaluate the exact reference12e_sel by these expressions or certified intervals; this source supplies no cooling, measurement procedure or precision feasibility theorem.

Sources and exposure: ROOT fully read common_product_static_cat_selector/PROPOSAL.md ab894394a2b2bd76dcc59b591f5d39d2aa070d7c1c3aa62528b76c99c6cd8c18 and its complete distinct review c34ef97e7ae4a3b96932e9904b79aacc18cae6b6ac0f8c999006395a2b1aa32a. The exact characteristic-polynomial output common_product_loader_bond_realization_check/exact_square.txt 4023c5f3fbd8eeabfe7feaa2d3cea77f694da7e1cece3ea5897dbf28e8247758 was directly refreshed; its script109b3f33919446f0c7cb7fa5cbcec5209df4f381bdbd145f5ab3661fb46f9ee3 and reviewf71cdc retain their prior complete reads. No script was rerun. ROOT reduced the displayed polynomials to the roots and rationalizations above. This is a new same-model exposed algebraic derivation, not independent replication of the polynomial computation. A distinct checker should verify the sector maps, complete root lists, ordering, identity(2), exact reference(3), and the absence of any altered runtime or physical preparation claim.
