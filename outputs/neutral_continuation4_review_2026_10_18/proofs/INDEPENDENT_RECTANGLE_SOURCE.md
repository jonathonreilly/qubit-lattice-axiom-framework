<!-- Owning original: PR9762; source SHA256 61b9dcdba5406aee3ba51529c183f6f1b3e9c3e0350a85ff2b439cc6fb399bf8. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Odd-height 4x6 rectangle: original-readout activation

Disposition: PASS within the specified maximal central-character sector at fixed sizes. Do not infer global-ground selection from the square argument without an additional order-lambda8 central-sector check. No repository edits or formal audit.

## Coefficients and original source

For transverse Nx=4, Ny=6 and open L=5, use the unnormalized original C=sum Z_z Z_(z+2) and H+sC. The normalization matters: division by sqrt(120) divides the amplitude by sqrt(120) and weight by120.

The native inputs give K=19Jz lambda^4/128 and t=Jz lambda^5/16. The preceding fixed-size hierarchy gives

 tau_row=12 t^3/(8K)^2=3Jz lambda^7/1444,
 tau_col=4 t^2/(8K)=Jz lambda^6/76.

With U norm4 and V norm6 in the maximal center, set U=4X,V=6Z. The effective Hamiltonian's leading nonscalar part is -aX-bZ, a=3Jz lambda^7/361, b=3Jz lambda^6/38. The leading character/multiplicity representation remains legitimate even though epsilon_y=(-1)^3=-1; its sign is absorbed consistently into U, and U,V anticommute.

Independently differentiated all minimal L=5 two-column paths using their open-chain denominators: at Jz=1 the amplitude is -1/16 and its H+sC derivative is -9/32. Thus t'/t=9/(2Jz). The inherited plaquette derivative gives K'/K=3(L+13)/[(L+14)Jz]=54/(19Jz). For r_n=n t'/t-(n-1)K'/K, r3-r2=63/(38Jz). The projected derivative source is consequently -r3 aX-r2 bZ, up to the connection correction and higher terms. Its offdiagonal magnitude is

 |ab(r3-r2)|/sqrt(a^2+b^2)
   = (189/13718) lambda^7+o(lambda^7).

The corresponding per-ground-state spectral weight is (189/13718)^2 lambda^14+o(lambda^14). No extra physical-doublet factor is present for a neutral observable.

## Refined parity and parameter connection

The transverse bipartite grading conjugates H(lambda,s) to H(-lambda,s), with C invariant. A full four-column flip has an even number (two) of black columns and odd height, so its amplitude is even in lambda. A full six-column flip has three black columns and odd height, hence its amplitude is odd. Thus b has no order-lambda7 correction and a begins at lambda7. In the specified center, the gap is 2sqrt(a^2+b^2)=3Jz lambda^6/19+O(Jz lambda8), subject to the fixed-size analytic reductions.

For the source derivative one needs projected connections, not merely small full rotations. At the first exact Kato reduction the N=0 reference projector is independent of s: the leading direct-rotation generator and its derivative are off-block O(lambda), so P0(partial_s W)W†P0 starts at O(lambda²). At the second reduction the leading plaquette eigenspace P+ is again s-independent (only its common positive coefficient changes). Off-block mixing starts at lambda^(L-4)=lambda; its projected connection also starts quadratically. Conjugating the first projected connection by this near-identity second rotation preserves its O(lambda²) bound. All statements require a fixed neighborhood of s with an analytic open gap, available at fixed geometry.

The effective derivative identity is W C W†=partial_s H_eff-[D,H_eff]. Every lower P+ contribution is scalar; the first nonscalar term is orderlambda6. Therefore the connection contributes O(lambda8), below the desired lambda7 matrix element. Differentiating source-dependent denominators or energy-dependent intermediate reductions cannot bypass this exact identity. Merely saying the full connection is O(lambda) would be insufficient at the desired accuracy.

## Scope warning: center versus actual global ground

Within the specified maximal center the activation, gap and weight above follow. Loss of xy exchange removes the square's exact even-C darkness, and the unequal derivative ratios produce the nonzero leading matrix element without adding a scalar-source constant.

However, the earlier square argument for global-ground selection does not transfer automatically. At fixed maximal C-center, variation of the R-center first changes -sqrt(b²+a² r²/16) at order a²/b=O(lambda8), because b dominates. That is the same order as presently unspecified higher coefficients. A separate classification must show that no competing R-center-dependent term at orderlambda8 reverses the selection before calling this the response of the actual unrestricted ground. Hamming/plane/parity restrictions may well establish this, but it is an additional obligation. The simpler and currently justified wording is a neutral transition in the specified maximal central sector. Higher-center comparisons are not needed for that sector-conditional statement.

All conclusions are fixed finite 4x6x5 native asymptotics with supplied geometry, source and coupling regime. They are not 120-qubit ED, a growing-volume theorem, or a cubic/Lorentz scalar or cosmological detector identification.

## Addendum: global-ground selection and static line contribution

Final disposition: PASS, including actual finite-size global-ground selection for sufficiently small positive lambda. Read native/RECTANGLE_SOURCE_ACTIVATION_PROOF.md. Its new symmetry/valuation classification discharges the outstanding order-lambda8 objection above.

To justify the unique phase, write an operator with a fixed gauge-pattern translation as f(a,b) R_I C_J in the real orthonormal sign basis. Commutation with every physical R_x forces f to be independent of all a signs. Commutation with each physical A C_y then requires f(b with b_y reversed)=(-1)^p f(b), p=|I|. Fourier characters on the b hypercube give exactly f=constant times B^p. This is well-defined on the quotient because Ny=6 is even. Replacing I,J by their simultaneous complements changes neither the translation nor p modulo two, so introduces no new phase. Constant physical Y-plane phases cancel from this commutation calculation.

Since C_J reverses B by (-1)^q, (B^p R_I C_J)^T=(-1)^(pq) B^p R_I C_J. For pq odd the real matrix is antisymmetric. A real symmetric effective Hamiltonian cannot contain it; distinct translations cannot cancel this restriction. Exact direct Kato reductions can preserve both reality and the plane representation, so the exclusion applies to the actual hierarchical coefficients, not just the leading model.

The changed-column count is k=6p+4q-2pq. Explicit enumeration modulo (p,q)~(4-p,6-q) gives precisely (p,q;k)=(0,1;4),(0,2;8),(1,0;6),(1,1;8) for 0<k<=8. The inherited fixed-size valuation is k/2+4. The mixed row/column case is forbidden by real symmetry. The row term begins at lambda7 and has odd checkerboard parity, so has no lambda8 correction. Consequently through lambda8 all other nonscalar terms are column flips or pairs of column flips, plus a common scalar. This classification includes arbitrary pattern-dependent coefficients through the unique-phase argument; it does not overlook diagonal functions of central characters.

The order-lambda6 term first selects the sector with all relative C_y characters positive. In its lower branch the column-only lambda8 corrections have identical values for every R-center. The order-lambda7 row term couples that branch to its upper partner, and second-order perturbation across the order-lambda6 gap gives -tau_row^2 r^2/(2b) at orderlambda8. It is strictly minimized by |r|=4, equivalently all relative R_x characters positive. At fixed geometry the remaining norm error is o(lambda8), so it cannot overturn this strict center ordering. Thus the actual global ground belongs to the maximal center and is exactly the protected physical doublet for sufficiently small lambda. This remains a fixed-size asymptotic claim with no certified numerical threshold.

For the unnormalized original C, the resulting line's positive static Lehmann contribution is

  2 |C_ge|^2 / gap
    = 2 (189/13718)^2 /(3/19) * lambda8/Jz + o(lambda8/Jz)
    = (11907/4952198) lambda8/Jz + o(lambda8/Jz).

The rational coefficient was checked exactly. This is this neutral line's contribution, not the total susceptibility. It tends to zero: softness of the gap alone does not create a static enhancement. For C/sqrt(120), divide this contribution by120. No additional factor arises from averaging the physical ground doublet, because the neutral operator acts identically on that irreducible factor.
