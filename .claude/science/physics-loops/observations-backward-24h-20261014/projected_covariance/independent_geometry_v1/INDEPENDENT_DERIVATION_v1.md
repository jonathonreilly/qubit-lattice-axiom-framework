# Independent shell geometry and differential covariance compatibility

Frozen before exposure to any root `projected_covariance` derivation or implementation. This is a focused conditional mathematics check; root remains author. The only scientific source read is the complete supplied M14 note, SHA256 `592df22cbc7421da970842b42157129ba65e8f0c71d6928ca90fa189474702ce`, copied as `SUPPLIED_M14_NOTE_v1.md`. The requested base identity was supplied by root; I did not invoke Git to verify it. No observations, network resources, author code, aggregate or ODE were opened/run.

**Result.** There is a local necessary differential constraint on the ideal shell correlations of S and radial proper peculiar velocity. It preserves the same five lifted coefficient combinations as M14. It needs no chosen scalar initial covariance and no integration of radial velocity into a potential. A naive projection of the M14 time derivative is incorrect because the radial projection changes with shell radius. A compatibility commutator removes that extra term. Missing angular ell=0,1 can then be eliminated by an additional differential operator. The resulting relation is only necessary, can lose rank and information, and demands high derivatives of calibrated continuous correlations. It supplies neither actual lensing deprojection nor an observational error model.

## 1. Premises and source identity

Use the Jordan-frame notation of M14. Let N=ln a, H>0, h=H'/H, V=H v, x=F'/F, q>0, y=x/q, J=3 exp(-3N)/E^2 and gamma=JR. Write

    a_m=(y-x-2)/2,   c_m=-h y-gamma.

The necessary local field identity inherited from M14 is

    S_N-y V_N=a_m S+c_m V.                                      (1)

The derivatives here are at fixed comoving position. This is not an assumed quasistatic relation and does not remove the free scalar initial data. For the current calculation, assume smooth real joint statistically homogeneous/isotropic scalar fields, sufficiently many derivatives to interchange expectation and differentiation, and finite covariances. No Gaussian law, independence of Fourier bands or deterministic common transfer is required. Means can be subtracted consistently. Homogeneous velocity-potential gauge terms must be handled in the same nonzero-mode convention as the supplied momentum equation.

For A,B in {S,V}, define equal-time correlations K_AB(N,r) at comoving separation r. Homogeneity and isotropy make them radial and imply K_SV=K_VS. Differentiating a two-point correlation uses both time legs. Correlating (1) with S-yV at the other point, adding the exchanged equation and dividing by two gives

    (K_SS,N-2y K_SV,N+y^2 K_VV,N)/2
      =a_m K_SS+(c_m-a_m y)K_SV-c_m y K_VV.                    (2)

Here y is an epoch coefficient, not differentiated. Equation (2) is the real-space counterpart of the supplied equal-time covariance identity; no Fourier inversion of observed data is used.

## 2. Equal-distance shell geometry

In flat FLRW, the background past light cone from a fixed observer epoch has comoving radius chi(N)>0 and

    calH=aH,   chi_N=-1/calH.

The sign is for increasing N toward the observer, with light speed one. At shell points X=chi n and X'=chi n', set mu=n.n' and

    r=chi sqrt(2(1-mu)),   0<r<2chi.

The proper peculiar radial velocity supplied in the question is

    u(n,N)=n.grad(v)/a=n.grad(V)/calH,

with the spatial derivative at fixed N. Let the three ideal angular correlations be

    A(N,mu)=<S(X)S(X')>,
    Xc(N,mu)=<S(X)u(X')>,
    U(N,mu)=<u(X)u(X')>.

Writing these instead as functions of (N,r), differentiation of the isotropic two-point function gives

    A=K_SS,
    Xc=r K_SV,r/(2chi calH),                                  (3)
    calH^2 U=r^2 K_VV,rr/(4chi^2)
                   +(r/(4chi^2)-1/r) K_VV,r.                  (4)

Both radial factors in the cross correlation have the positive r/(2chi) sign. In the velocity Hessian, n.rhat=r/(2chi) while n'.rhat=-r/(2chi), and the mixed spatial derivative is minus the Hessian with respect to separation. Thus the sign in (4) is not a plane-parallel assumption. At coincidence its regular limit is -K_VV,rr(0)/calH^2; the displayed elimination below excludes coincidence and the shell endpoints.

Equivalently, for the angular restriction f(mu)=K_VV(r(mu)),

    chi^2 calH^2 U=(1-mu)^2 f_mumu+mu f_mu.                    (5)

The cross relation is Xc=-(1-mu)K_SV,mu/(chi calH).

A time derivative at fixed separation is observable from an ideal family of shells only after correcting the changing angular coordinate:

    D_N|r = partial_N|mu +2(chi_N/chi)(1-mu) partial_mu.         (6)

The derivative must be evaluated on a common open (N,r) domain lying inside neighboring shells. Fixed multipole, fixed angle and fixed physical separation are different derivatives. The geometry, distance-redshift relation, a,H and normalizations are supplied inputs.

## 3. Failed shortcut and local compatibility elimination

Let p=K_VV,r and use the measured derivative of the cross covariance rather than its primitive:

    b=K_SV,r=2chi calH Xc/r,
    s=K_SS,r=A_r,
    alpha=1/r-4chi^2/r^3,
    g=4chi^2 calH^2 U/r^2.

Equation (4) is

    (partial_r+alpha)p=g.                                    (7)

The homogeneous radial derivative p0=r^-1 exp(-2chi^2/r^2) is a nontrivial smooth-away-from-zero kernel of this operator, and it extends flatly to r=0. Constants are also invisible in the potential covariance itself. This is a statement about the projection operator; it is not a claim that every such null function is a globally positive-definite covariance of an admissible full action solution. In particular, positivity or additional global boundary information could remove some operator ambiguities, but neither is needed for the necessary result below.

The tempting step of commuting the projection in (4) with D_N is wrong. For its operator B_chi,

    B_chi=r^2/(4chi^2) partial_r^2
                +(r/(4chi^2)-1/r) partial_r,
    partial_N B_chi=-2(chi_N/chi)(B_chi+r^-1 partial_r).

The extra term still involves p. Ignoring it would give a different constraint even for smooth fields. An exact Gaussian test below detects this shortcut.

Differentiate (2) once with respect to r, and set

    d=a_m s+(c_m-a_m y)b-s_N/2+y b_N,
    E=(y^2/2)D_N+c_m y,
    P=partial_r+alpha.

Then the two necessary equations for p are

    E p=d,   P p=g.                                          (8)

All coefficients in E are functions of N only. Therefore

    [E,P]p=(y^2/2)alpha_N p,
    alpha_N=-8chi chi_N/r^3.                                 (9)

Define the fully observable, coefficient-dependent expression

    Fobs=E g-P d,
    m=(y^2/2)alpha_N.

Equations (8)-(9) imply Fobs=m p. On the rolling chart y!=0, chi>0 and chi_N!=0, this locally determines the derivative p algebraically. No primitive of u or initial p is supplied. On a regular expanding past cone alpha_N=8chi/(calH r^3)>0.

Since m_r/m=-3/r, substituting p=Fobs/m back into (7) yields the undivided necessary constraint

    Zobs=(partial_r+alpha+3/r)Fobs-m g=0.                    (10)

This expression contains no hidden velocity-potential covariance. It involves radial derivatives, fixed-separation time derivatives of the three measured correlation functions and the background geometry. It does not contain x_N or y_N: the spatial compatibility operation does not differentiate the epoch coefficients.

Equation (10) is necessary even when y=0 by its undivided derivation, but the reconstruction p=Fobs/m then fails and q is not identified by that instantaneous chart. The observer endpoint chi=0, r=0, absence of neighboring time shells or a stationary-radius construction are outside this local inversion. Equation (10) alone is not sufficient for (8): a reconstructed p must additionally satisfy E p=d. Nor does (8) alone certify a global positive covariance or all scalar/dust field equations. This is a necessary compatibility filter, not an equivalence to the full physical model.

## 4. The five lifted coefficients survive

Let z=(x,y,y^2,gamma-xy/2,gamma y). Then

    d=-s-s_N/2-z1 s/2
        +z2[s/2+(1-h)b+b_N]-z3 b/2-z4 b,                    (11)
    Fobs=z3(g_N/2-hg)-z5 g-P d,
    Zobs=(partial_r+alpha+3/r)Fobs-z3 alpha_N g/2.             (12)

Thus (10) is affine in exactly the five lifted variables used by M14. Each admitted separation produces a row. If enough resulting rows actually have rank five, one may solve for z and impose the original nonlinear gates z3=z2^2, z5=(z4+z1*z2/2)z2, positive R=(z4+z1*z2/2)/J, nonzero y and q=x/y>0. Nothing here proves that the projected rows have rank five, that they are well conditioned, or that the universe realizes them. A formally solved vector without those tests is not a physical reconstruction.

## 5. Missing sky monopole and dipole

If full-sky correlations of the two scalar sky maps are known only for ell>=2, rotational invariance means each of A, Xc, U is determined only up to

    A -> A+A0(N)+A1(N)mu,
    Xc -> Xc+B0(N)+B1(N)mu,
    U -> U+C0(N)+C1(N)mu.                                   (13)

These sky modes are not the same as a spatial Fourier k=0 mode. Arbitrary smooth coefficients in (13) safely encompass the unknown lower multipoles of the three channels. The statement requires a known full-sky harmonic projection. An arbitrary survey mask or calibration mixing is not automatically described by (13).

At fixed N, mu=1-r^2/(2chi^2). Consequently the nuisance contributions satisfy

    Delta s in span{r},
    Delta b in span{r^-1,r},
    Delta g in span{r^-2,1}.

Their fixed-r N derivatives stay in those same spans. Hence Delta d is in span{r^-1,r}, Delta Fobs in span{1,r^-2,r^-4}, and

    Delta Zobs in span{r^-1,r^-3,r^-5,r^-7}.                 (14)

No covariance amplitudes or coefficient values were used in this inclusion. Therefore define the radial Euler annihilator

    K=(r partial_r+1)(r partial_r+3)
          (r partial_r+5)(r partial_r+7).

The directly evaluable necessary condition from the high-multipole representatives is

    K Zobs=0.                                               (15)

Equivalently, at fixed N, differentiate r^7 Zobs four times with respect to r^2 (or four times with respect to mu, with its nonzero scale factor). It vanishes independently of all six missing lower-multipole functions. The annihilator acts only on r, so (15) remains affine in z. The exact controls include a nonzero response that survives this removal; it is not identically empty. However, its full kernel contains additional information beyond the supplied nuisance set, so passing (15) is still weaker than passing (10), and much weaker than full action membership. No minimum derivative count or optimality claim is made.

## 6. Controls and physical limits

`independent_geometry_controls_v1.py` gives 23 passing exact controls and no failures. It does not import or call any author implementation. It checks the Hessian projection, angular conversion, fixed-separation time conversion, commutator and radial null derivative; it preserves a nonzero witness against naive time/projection commutation. A smooth positive spatial covariance example uses correlated stationary isotropic fields xi,eta with Gaussian covariance exp(-r^2), correlation 1/3, S=t^-1 xi and V=t eta, where t=exp(N), x=y=1,h=0,gamma=1. These fields satisfy the reduced relation S_N-V_N=-S-V. With chi=t^-1-1 and calH=t, the exact observation formulas verify (10), the local p reconstruction and a wrong-x rejection. This fixture is a real covariance satisfying the reduced identity; it is not represented as a full scalar cosmological solution or a member of the revised q<beta family.

Independent arbitrary monopole/dipole additions give a nonzero unfiltered residual but zero annihilated residual. The implementation tests each of the four nuisance powers, the alternative fourth derivative form, a surviving wrong-coefficient response and affine five-variable structure. All values are exact symbolic or rational expressions, not measured precision or numerical integration enclosures. The explicit failed shortcut is retained in this report and as a nonzero control rather than silently discarded.

The mathematical relation starts from the action and the statistical, smoothness and light-cone sampling premises. A real lensing map is usually an integrated response, not the S shell map appearing here. A reported velocity catalogue is not automatically the proper peculiar u in (3)-(4). Physical deprojection, tracer/observer treatment, units, masks, window functions, derivative estimation and a joint error budget remain required. The high derivative order may be impractical and amplify small observational errors; this exact necessary relation does not supply a useful finite-data bound by itself. Perturbed light-cone and redshift remapping require their own accuracy model; these formulas use ideal equal-background-time shells at linear field order. No initial covariance has been chosen for the theorem, but statistical homogeneity/isotropy and access to a continuous covariance family are explicit conditional inputs. No new empirical test, unique TOE or action selection is claimed.
