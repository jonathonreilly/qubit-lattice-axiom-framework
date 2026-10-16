# Projected covariance: post-exposure source correspondence

This report follows the immutable pre-exposure proof `INDEPENDENT_DERIVATION_v1.md` (SHA256 `1321e0de7fff6d20de3f8ae587dde4af734e3143629599e24d3019a7c2b6c821`) and its 23 exact controls. It does not replace that independent record. Root remains the author. No author aggregate, forward ODE, Git operation or formal audit was run.

I read the complete frozen `WORKING_v1.md`, `CHECK_v2.py`, `RESULTS_v2.json` and original `FAILURE_v1.md`; compared the complete v1 source/result against v2; and then inspected the complete v2-to-v3 changes and updated failure record. Source snapshots and exact hashes are in `AUTHOR_EXPOSURE_v1.json` and `AUTHOR_EXPOSURE_v2.json`. No WEAK_FORM source or new FORWARD source/results were opened. The updated failure record incidentally summarizes the separate weak-form finding; I do not verify that route here.

## Operator equivalence

The geometry agrees with the independent proof, including both radial projection signs, proper-velocity factor aH, the fixed-separation chain derivative and the smooth radial operator kernel. Root's D=partial_r/r and E=[r^2/(4chi^2)](r partial_r+2)-1 give U=E D C_VV, with U=a^2 H^2 C_uu. The angular cross-correlation gives d=D C_SV without selecting its integration constant.

Let Hc denote the unprocessed covariance residual (left side minus right side of the M14 scalar covariance identity). To avoid confusing root's operators with those in my proof, set

    alpha_r=1/r-4chi^2/r^3,
    P_r=partial_r+alpha_r,
    Q_r=partial_r+alpha_r+3/r.

My unannihilated observable residual equals Q_r P_r partial_r Hc. Direct operator algebra gives

    Q_r P_r partial_r = (16chi^4/r^5) E^2 D.                 (1)

Writing K=r partial_r and L=(K+1)(K+3)(K+5)(K+7), multiplication by r^5 conjugates root's P=(K+2)K(K-2)(K-4):

    P(r^5 f)=r^5 L f.

Hence root's final processed constraint Q Hc=0, Q=P E^2 D, equals r^5/(16chi^4) times my final annihilated compatibility residual. On 0<r<2chi, chi>0, these necessary constraints are exactly equivalent. Root's route does not divide by y or chi_N and therefore needs no additional nonzero-roll premise merely to state the necessary relation. Nonzero y and the other M14 gates remain necessary for interpreting a solved lifted vector as q=x/y.

For the time-dependent operator, E_N=g(E+1), g=-2chi_N/chi. Therefore

    E U_N-g(E+1)U=E^2 D(C_VV,N).

This equality uses E(E+1)=(E+1)E at the same N. It never replaces an ordinary derivative of a processed covariance by its derivative input functional. Root's A1, B1 and C1 have the correct separate definitions and order. P and E do not commute; the supplied implementation preserves the displayed order. All five row coefficients and the inhomogeneous term correspond to Q Hc, with the original monomial consistency and positivity gates still required. The processed quantities need not form a positive covariance matrix.

## Angular nulls and shear inverse

The low-mode cancellation matches the independently derived nuisance space. A missing sky monopole/dipole changes an angular correlation by a degree-one polynomial in mu, or degree one in r^2 at fixed N. This gives the stated ambiguities in C_SS, d and U. E^2 maps the first two into powers r^-2,1,r^2,r^4; the C1 operation stays in that same finite span. P annihilates it. Equivalently, multiplying my nuisance residual by r^5 maps its powers r^-1,r^-3,r^-5,r^-7 to root's r^4,r^2,1,r^-2. No null coefficient is fitted, selected or set to zero.

I also checked the displayed Born Volterra inverse within its declared convention. For

    psi(s)=integral_0^s [1/chi-1/s] S(chi) dchi,

regularity/integrability at the observer gives s^2 psi_s=integral_0^s S(chi)dchi and therefore partial_s(s^2 psi_s)=S(s). The spin-two inversion is only for ell>=2. Smooth regular angular modes near the observer justify the lower endpoint in this ideal setup. Covariance reconstruction differentiates both source arguments where two shear channels occur. It remains a past-light-cone deprojection premise; it does not by itself supply a realistic measured S shell map, finite-bin derivative estimate, mask correction or error model. No lost physical calibration premise was identified in the working note's stated scope.

## Original failed symbolic control

I reproduced the v1 nonzero SymPy expression. It is the difference between

    Subs(Derivative(C(xi,r_shell(N)),xi),xi,N)

and

    Subs(Derivative(C(N,r),N),r,r_shell(N)).

Both mean the first-argument partial derivative of C evaluated at (N,r_shell(N)); the second argument is held fixed during their respective derivative operations. The difference is a binding/representation failure of this literal symbolic equality test, not a surviving physical chain-rule term. Independently, the coefficient of C_r is exactly

    r_shell,N +2(1-mu)(chi_N/chi) r_shell,mu=0.

This proves the chain rule for arbitrary differentiable C. The v2 explicit N/r fixture is additional evidence, not a replacement for that general coefficient identity. The source diff changes only this comparison and the versioned output name. The results differ only in this one check, counts and source identity; all synthetic data are identical. The stated 17/1 failure history and its diagnosis are justified. No tolerance, scientific formula, synthetic case or threshold was relaxed.

## Concrete finding and repair: matrix norm label

The v2 `condition_inf` value 3.232125392...e9 was produced with `mp.norm(matrix,'inf')`, which is the entrywise maximum. It is not the induced infinity matrix norm. I verified the local mpmath implementation and independently reconstructed the matrix from the saved processed data. Explicit maximum row sums give

    ||M||_inf ||M^-1||_inf = 6.3175917129191095...e9.

This was reported immediately. Root preserved v1/v2 and repaired v3 using `mp.mnorm`. The complete v3 delta changes only those two norm calls and the output filename. Its saved determinant, states, recovered coefficients, check outcomes and synthetic data are unchanged; the corrected diagnostic agrees with my independent row-sum calculation. The finding is recorded separately in `FINDING_MATRIX_NORM_v1.json`. Neither number is measured precision. The corrected, larger value makes the severe conditioning limitation stronger. A small 90-digit synthetic residual does not establish observational stability.

## Finite homogeneous shell ensemble and independent rank certificate

Each of the five supplied 3x3 (S,V,T) covariance matrices is positive definite. A finite sum of spectral shells is a legitimate smooth homogeneous/isotropic covariance: for each shell choose a uniform random direction n, uniform phase theta and an independent bounded vector a with covariance Sigma. The real vector field sqrt(2) a cos(k n.x+theta) has covariance Sigma j0(kr). Summing five independent shells realizes precisely the supplied spatial covariance. This is a finite number of shells with continuous direction/phase randomness, not a claim that a finite discrete list of directions is exactly isotropic. Gaussianity is unnecessary.

At a regular M14 event the arbitrary finite (S,V,T) states map to allowed (phi,v,X), with the remaining scalar momentum free and the density fixed by the 00 constraint. Thus the covariance construction is compatible with the local initial-data freedom. The chosen event has q=3/20>0 and nonzero roll. As an additional local generic-action consistency check, Q=A=H_J=1, b^2=3/40, pi=-x/(2b), H_E=1-b pi, rho=28/15 and V_E=39301/30000 satisfy the Friedmann value; a finite potential slope can give the specified h=-2/7. This is a local generic action witness, not a reconstructed cosmic history or a fitted revised-family potential.

The author 90-digit determinant and inverse are numerical diagnostics. I supplied a separate exact nonsingularity enclosure for the first five separations without using the author's symbolic differentiation/lambdified kernel. Expand

    j0(kr)=sum_n (-1)^n (kr)^(2n)/(2n+1)!.

Apply the analytically derived Q action to each monomial. Through n=36 this gives rational entries at the supplied rational k,r,chi. For every omitted n>=37 and kr<=5, each positive absolute-envelope term has next/current ratio at most

    [(n-2)/(n-3)]^7 *25/[(2n+2)(2n+3)] <1/2.

Consequently twice the first omitted absolute envelope bounds the complete tail. After explicit rational rounding to denominator 10^30, the matrix error in the induced infinity norm is bounded by 3.141e-30. Exact rational inversion of that rounded matrix gives

    ||M_rounded^-1||_inf ||M-M_rounded||_inf <6.24e-23<1.

Neumann's argument therefore proves nonsingularity of this exact kernel matrix. The separate moment-row basis determinant is exactly 1/1920. This is a mathematical rank witness for this manufactured setup, not an empirical input or guarantee of observed rank. Its ill-conditioning remains. I did not extend this enclosure to the reserved sixth-separation residual or any subsequent rolling numerical evolution.

## Evidence boundary

There are 13 new post-exposure controls in `POSTEXPOSURE_RESULTS_v1.json`, including the exact operator equivalence and rational rank enclosure, distinct from the 23 pre-exposure controls and the author's 18 controls. Their script imports no author implementation. The complete read identities are:

- WORKING_v1.md: `641a730694795f2e18af4b57e3083f82bd62f4a89902ac0dbc25aab1dd33d92d`.
- CHECK_v2.py / RESULTS_v2.json: `54e3d7c6373f95159572446969c54d38d91601bdaaa62e4a60246c15a75d0fef` / `9f4bfe10c2506caf3e0991e9ab347bc71310cdbeabffe5b480d1486949a14b3d`.
- Corrected CHECK_v3.py / RESULTS_v3.json: `36d3d29e3d10b8af91e793a62ad3f624c8ebc47db909b2b9d3cf6ddea95e8616` / `a47151273d73e92b54aa7aa823ffd4e9b82c559915a81f0fce1d34c6313689b5`.

No unresolved theorem or implementation discrepancy was found in this reviewed scope after the norm repair. I do not claim a complete observation supplier, practical derivative stability, full-history action membership, independent verification of later forward outputs, formal audit or publication approval.
