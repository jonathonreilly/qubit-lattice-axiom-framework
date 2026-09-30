# Independent endpoint reconstruction before author proof

This is a focused mathematical check, not formal review/audit or a gravity/record identification. Exposure before this freeze: root's neutral task and the complete CONTRACT (including its proposed Fourier/nonzero-mode and compact-support routes). No forthcoming root proof, code or results, and no root PRE, have been read. I previously authored the spectral gravity precursor and handled its mechanical preparation; its analytic evolution theorem is not a premise here. I read the exact provisional PR9398 canonical definitions and compatible flat-slice data at bd6f6e6368d615bfc0437760e2396cd471837cd7. The continuous carrier, this scalar form, endpoint metric and source identification are supplied conditions.

## Independent real-space decomposition

Use normalized torus mean <.>, real smooth symmetric sigma, div sigma=0 and the scalar quadratic form Q(sigma)=tr(sigma^2)−(tr sigma)^2/2. At pi0=lambda I, exact endpoint subtraction gives

    delta rho/a = lambda tr sigma − Q(sigma).                 (1)

The sign follows from the kinetic cross term 2lambda tr sigma−3lambda tr sigma=−lambda tr sigma. No linearization is used. Set M=<sigma>, t=tr M, A=M−(t/3)I. Solve the mean-zero scalar Poisson equation

    Delta u = (tr sigma−t)/2,
    S(u)=I Delta u−Hess u,
    T=sigma−M−S(u).

Then div S=0, tr S=2Delta u, and T is mean-zero, divergence-free and trace-free. Torus integrations by parts give

    <T:S(u)>=0,
    <|Hess u|^2>=<(Delta u)^2>,
    <Q(S(u))>=0.

Constant/nonconstant cross terms also integrate to zero. Therefore

    <Q(sigma)>=|A|^2−t^2/6+<|T|^2>,
    <delta rho>/a=lambda t+t^2/6−|A|^2−<|T|^2>.             (2)

This gives the sign by a real-space Poisson/York decomposition rather than assigning a positivity sign to the unrestricted pointwise DeWitt form. The inverse Laplacian and T need not preserve compact support. They are proof variables, not new constraints or carrier fields.

## Compact support and null directions

If sigma is supported compactly inside a proper coordinate ball, extend its coordinate expression by zero and integrate div(x_i sigma_.j)=sigma_ij. Smooth cutoff coordinates equal x_i near the support suffice on the torus. Thus every component of M vanishes. Equation(2) then gives

    <delta rho>=−a<|T|^2><=0.                              (3)

Equality does not force sigma=0. For any compactly supported smooth u, S(u)=I Delta u−Hess u is a compactly supported divergence-free null direction for the INTEGRATED quadratic form. Its exact pointwise source is

    delta rho/a=2lambda Delta u+(Delta u)^2−|Hess u|^2,      (4)

and has mean zero. It will generally be signed. Neither (3) nor (4) says Q(S(u)) vanishes pointwise. At lambda=0 the integrated nonpositivity still holds and the linear term disappears. If a required delta rho is nonnegative pointwise, compact support forces it identically zero; existence of nontrivial sigma for a specified zero source is a separate nonlinear equation, not implied by integrated equality.

## Complex Fourier cross-check and homogeneous escape price

At nonzero real wavevector k, symmetry and k_i sigmahat_ij=0 put sigmahat in a COMPLEX symmetric transverse 2-by-2 block B. For a real field Parseval pairs k and −k by conjugation. The contribution is

    ||B||_F^2−|tr B|^2/2
       =|B11−B22|^2/2+2|B12|^2 >=0.

Its null space is B=cI_2 with complex c. Equivalently sigmahat=c(I−kk^T/|k|^2). It is not correct to use tr(B^2) without conjugation for a single complex mode. The transverse trace-free part is exactly That in (2). The k=0 mode has no divergence restriction and must be kept.

Let d=<delta rho> and E=|A|^2+<|T|^2>. The exact homogeneous trace condition is

    (t+3lambda)^2=9lambda^2+6d/a+6E.                       (5)

For d>0 it implies the necessary sharp lower price

    |t| >= sqrt(9lambda^2+6d/a)−3|lambda|.                 (6)

The branches are t=−3lambda +/- sqrt(9lambda^2+6d/a+6E). For lambda!=0 the minimum is on the branch with t having the sign of lambda; for lambda=0 the two signs are symmetric and |t|>=sqrt(6d/a). A homogeneous pure trace sigma=(t/3)I realizes equality with uniform d=a(lambda t+t^2/6), so (6) is sharp over the stated unrestricted endpoint family. It is not a sufficient condition for an arbitrary prescribed spatial delta rho. Nonconstant scalar transverse null modes may coexist with the same integrated price; equality does not force homogeneity unless further conditions are supplied.

Signed d is governed by the exact identity(2), not the positive-d square-root simplification. In particular d>=−3a lambda^2/2 is not an unconditional bound because E may be arbitrarily large; it is the pure-trace homogeneous family's lower limit. Homogeneous traceless and mean-free TT parts lower the mean source. A change of metric, nonzero source momentum, nonlocal homogeneous momentum or changed source identification leaves this frozen endpoint problem.

No numerical computation is required for these identities. The only remaining task is comparison with the forthcoming frozen proof, verification of any stronger scope/source claims, and final source-bound receipt. No quantum record process or supplied matter energy is equated with rho, and no dynamics or no-go for local gravity is inferred.
