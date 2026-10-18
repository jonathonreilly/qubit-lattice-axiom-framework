# Distinct algebra check: exact selector reference energy

Disposition: SUPPORT. The complete sector root lists, their ordering, exact ground energy, exact full gap and both rationalizations are correct. No runtime, fidelity, preparation or cooling conclusion is strengthened by this supplement.

## Evidence and exposure

The complete new source read and hash verified is `common_product_selector_exact_energy/PROPOSAL.md`, SHA256 `0ef4a6cdf6b2f228bb93e39f244720db533c47c6df3f8cb531b48ce8c424714c`, under N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The exact polynomial output `common_product_loader_bond_realization_check/exact_square.txt`, SHA256 `4023c5f3fbd8eeabfe7feaa2d3cea77f694da7e1cece3ea5897dbf28e8247758`, was completely reread and hash verified. I previously authored its exact calculation and review f71cdc4e4039f923f99c8ed1f2abab9baedee9f8f9456c1d77ed6a9978b9fd58; the script109b3f33919446f0c7cb7fa5cbcec5209df4f381bdbd145f5ab3661fb46f9ee3 was not rerun. The complete immediately preceding reads of selector source ab894394a2b2bd76dcc59b591f5d39d2aa070d7c1c3aa62528b76c99c6cd8c18 and my review c34ef97e7ae4a3b96932e9904b79aacc18cae6b6ac0f8c999006395a2b1aa32a are reused unchanged for its conditional energy-certificate scope.

ROOT authored this new reduction and supplied the candidate and requested checks. I share the earlier square-calculation and selector-check ancestry. The work below is a distinct exposed algebra check of the new formulas, not independent replication of the characteristic polynomials or a blind review.

## Sector mapping and roots

Removing 4hI leaves H0-h sum s_r X_r. Local Z conjugations remove the individual signs and multiply F by their product sigma. Thus original F=sigma maps to all-positive-field F=+1, and F=-sigma maps to F=-1. Conjugating by all four Z operators changes the sign of the transverse perturbation while preserving F. A single Z exchanges F parity and flips one field sign. These identities justify use of the frozen scalar-square matrices with omega=+1 and -1, respectively, despite the opposite sign convention for the perturbation. There is no data-dependent energy shift or use of the joint interacting-gadget scalar.

Substituting E=2-w into the frozen plus quartic gives exactly

    w^4-(4+16u)w^2+32u.

Its quadratic roots in w^2 are 2+8u +/- 2sqrt(1+16u^2). Indeed their sum is 4+16u and product32u. For u>0, (1+4u)^2-C^2=8u>0, so M^2>0. Also L>M>0. The quartic therefore contributes 2-L,2+L,2-M,2+M; the other factor contributes four copies of2. The plus-sector lowest root is uniquely 2-L. In particular L>2 for u>0, so this root is negative.

The frozen minus factors directly give the double roots2-2r and2+2r and the roots1+/-D and3+/-D. This accounts for all eight eigenvalues including multiplicity. On 0<r<=1/64, 1-D<0, while2-2r>0 and3-D>0; the other displayed roots are positive as well. Thus the minus-sector lowest root is uniquely1-D. No hidden repeated low root is lost in taking square roots.

## Exact gap, positivity and ordering against all states

Subtracting the selected plus-sector low root from the minus-sector low root gives L-1-D. The following direct derivation checks the cancellation-free expression:

    (L-1-D)(L+1+D)=4u+2(C-D),
    C-D=(16u^2-4u)/(C+D).

Consequently the first numerator equals

    4u(C+D-2+8u)/(C+D).

Using C-1=16u^2/(C+1) and D-1=4u/(D+1) makes this

    4u^2[8+16u/(C+1)+4/(D+1)]/(C+D).

Division by the positive L+1+D gives exactly equation(2). All factors are positive for u>0, so the lower sector is F=sigma. As u tends to zero, C,D tend to1 and L tends to2; the bracket tends to10 and the denominator to8. The gap divided by Delta*u^2 therefore tends to5, as claimed.

The full first-gap claim also holds, rather than just the algebraic splitting. H0 has exactly two zero eigenvalues on the full square, one per sector, with the other fourteen at least2Delta. The transverse perturbation norm is at most4h. Weyl therefore keeps all those fourteen centered energies above2Delta-4h. The selected ground has nonpositive centered energy, whereas the two low energies each lie within4h of zero. Their separation is at most8h<=Delta/8<Delta; every complementary gap exceedsDelta. This verifies that the splitting is the actual first full spectral gap throughout the stated domain. At h=0 the sectors become degenerate; the source correctly excludes that endpoint from uniqueness.

## Exact energy and certificate scope

The exact identity scalar removed at the start is4h, so the ground energy is precisely4h+Delta(2-L). Rationalizing its small centered correction gives

    2-L=(4-L^2)/(L+2)
       =-[8u+2(C-1)]/(L+2)
       =-[8u+32u^2/(C+1)]/(L+2),

which proves equation(3). This avoids cancellation in evaluating the small centered correction. It does not eliminate the need to control the error in subtracting12e_sel from an actual selector-energy expectation. Certified intervals must enclose that exact reference tightly enough for the supplied excess allowance; an unbounded Taylor replacement cannot inherit the certificate.

The enlarged algebraic domain r<=1/64 does not silently enlarge the static-selector theorem's operating prescription. Its conservative gap lower bound and all h/time allocations continue to use r<=1/(4*32^3). The exact roots change neither the runtime scalar48h nor the distinction between the selector observable and the full operating Hamiltonian. The sum of twelve isolated selector reference energies is12e_sel; it is not the ground energy of the interacting running device or an extra runtime phase. No new fidelity budget, gap-based cooling process, measurement accuracy feasibility or native state-preparation assertion appears in the source.

Only this review file was created. No scientific program was rerun, and no other source, W, Git, checkpoint, editable prompt or model setting was changed.
