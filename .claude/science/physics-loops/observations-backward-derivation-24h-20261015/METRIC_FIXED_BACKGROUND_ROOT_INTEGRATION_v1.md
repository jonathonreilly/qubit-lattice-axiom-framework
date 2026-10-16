# Spherical reconstruction with local integration kernels retained

Root's post-exposure rederivation, 2026-10-16. The focused checker independently
identified and treated the local traceless-Hessian and velocity-potential
kernels in `independent_metric_fixed_action/DERIVATION_BEFORE_AUTHOR_v1.md`
(SHA d3b0f8120f4cb95ff973b3f47069afcaa7f0fd1cddc23a5c713da6622e98947e).
Root personally read the complete proof and rederived the statements here.
This is attributed integration, not an independent second discovery.

## Correct scope of the earlier formula

The earlier fixed-background source used the equal-Einstein-potential branch
inherited from nonzero Fourier modes. On a local Cartesian patch, absence of
anisotropic stress alone instead gives

    (partial_i partial_j-delta_ij Delta/3)chi=0,
    PsiE=P+chi, PhiE=P-chi, J=chi+bw.

In three dimensions this implies chi=c0(tau)+c_i(tau)X_i+c2(tau)|X|^2:
off-diagonal Hessian entries vanish; all diagonal entries are equal; mixed
third-derivative compatibility makes their common spatial value constant.
Spatially integrated momentum and Euler also allow time-only functions.
They must not silently be discarded on a generic local angular patch.
Full-sky l>=2 projection removes this polynomial kernel, but a generic mask
does not. The earlier explicit w formula is conditional on chi=0 and a
fixed integrated velocity-potential convention. Keep that condition explicit.

## Why the actual slip is still unique

Retain one fixed compatible homogeneous background, a,R>0 and b,x!=0,
on an open spherical product chart r>0. For the difference of two solutions
with the same Weyl P and corrected radial redshift Rz, P=Rz=0. Set

    G=x/b, C=R/G, lambda=aC!=0,
    nu=6h-4q+2x'/x+C,
    Q=a^2(nu'-Cnu).

Momentum, Euler and Hamiltonian, retaining the kernel, imply
w=(R/x)Z+pi_w, J=CZ+pi_J, Z'=-CZ+pi_t and delta=nu Z+pi_delta,
where each pi is a spatial polynomial c0+c_i X_i+c2 r^2. These follow
because the background coefficients depend only on time. For example the
coefficient of Z in Hamiltonian is
-[(R/x)'/(R/x)-C]-Fbar/x=6h-4q+2x'/x+C, using dust transport.
Continuity and the observed radial redshift therefore imply

    Z_r-lambda Z=S, (Delta+Q)Z=T,
    S,T in span{1,X_1,X_2,X_3,r^2}.

At fixed time write S=s2 r^2+s1(n)r+s0 with s1(n)=s_vec dot n. A particular
radial solution is

    Zp=-s2 r^2/lambda-(2s2/lambda^2+s1/lambda)r
         -(2s2/lambda^3+s1/lambda^2+s0/lambda).

The general local solution is Z=Zp+exp(lambda r)f(n). After multiplying the
Helmholtz equation by r^2 the contribution from Zp and T is a polynomial of
degree at most four in r. Five radial derivatives kill it. Put A=lambda^2+Q.
The exponential coefficient has r^2 coefficient lambda^5 A f and r
coefficient (10lambda^4 A+2lambda^6)f. Their combination eliminates A and
gives 2lambda^6 f=0. Hence f=0 without dividing by A or selecting a spectrum.

The negative powers in (Delta+Q)Zp are -4s2/(lambda^2 r) and
2s1/(lambda^2 r^2). Their absence in T forces s2=s1=0 on the angular patch.
Thus Z is spatially constant and the actual slip/lapse difference
J=Z_r/a=0. The constant Z is a velocity-potential representation freedom.
This proves uniqueness of J, not all scalar/background representation modes,
without choosing chi or a boundary. Existence for given nonzero records still
requires all original equations with their kernel terms.

## A nonsingular variant of root's equal-potential formula

Within the explicitly fixed chi=0 convention, root's previous derivation
gave D w=N and w_r=Cw+f, where now C=aRb/x (the previous paragraph's lambda),
D=Lambda-C^2-C/r. Differentiate the first identity radially and eliminate
w_r. Since D_r=C/r^2!=0, one obtains everywhere on the annulus

    w=(r^2/C)[N_r-CN-Df].

This does not divide by D and therefore removes the isolated D=0 chart
issue by using another derivative. It is a necessary candidate followed by
all original residual tests, not an existence or finite-noise stability claim.
The checker's independently derived expression reconstructs Z from momentum,
continuity and radial data; this is root's post-exposure integration using its
own trace/scalar commutator identity. Both are conditional on the specified
equal-potential branch for an explicit formula.

## Geometry witness and new controls

The checker supplied a full-action planar null witness. Root independently
substitutes it into the original matter equations on the known power background:

    a=2tau, h=1/tau, b=1, x=q=1/(2tau), R=1/(4tau^2),
    Fbar=-1/(2tau^2), kappa=7/(4tau^2),
    Z=tau^(-1/2)exp(z+sqrt(14)X), P=0,
    w=J=Z/(2tau), delta=5Z/(2tau).

All full equations hold and -J+Z_z/a=0. Its observer-centered radial
redshift is nonzero on an open angular patch. Thus the theorem needs actual
spherical radial geometry; a plane-parallel replacement changes this exact
observability problem. This is a bounded local existence witness, not an
empirical cosmology or a global stability/normalizability claim.

The new control protocol checks the traceless-Hessian kernel, the homogeneous
Hamiltonian coefficient, the radial polynomial particular solution, fifth-
derivative coefficient elimination, negative-power coefficients, root's
nonsingular reconstruction for an arbitrary smooth field, and every original
equation of the planar witness. No observations, acceptance-tolerance changes,
or additional physical premises are introduced. The pre-exposure root source
and all independent failed attempts remain unchanged.
