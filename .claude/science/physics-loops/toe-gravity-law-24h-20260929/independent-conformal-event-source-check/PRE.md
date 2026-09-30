# Independent conformal reconstruction before author-proof exposure

Exposure: complete CONTRACT plus root task. The contract discloses division by a positive factor and monotone elliptic reconstruction; this is not a blinded target. No root proof, results or PRE read. I previously authored the spectral precursor and independently checked the flat-slice endpoint identity. Provisional PR9398 literal definitions are supplied model inputs; no analytic evolution theorem or record-to-gravity source assignment is used. Current main fb5da8dd, selected procedures7146; exact unchanged actual primitive/registry reads are reused from the immediately preceding checks. No scientific compute is planned.

## Exact constraints and sign

Let rho_b=3a lambda²/2>0, g=psi⁴I, pi=lambda psi²I. Then sqrt(g)=psi⁶, g pi=lambda psi⁶I, and the kinetic density is −rho_b psi⁶. Ordinary conformal curvature is R=−8psi^(-5)Delta psi, so −K sqrt(g)R=+8K psi Delta psi. The momentum density is pi^jk partial_i g_jk−2partial_j(g_ik pi^jk); its two contributions are12lambda psi⁵ partial_i psi and−12lambda psi⁵ partial_i psi. Thus it vanishes exactly for constant lambda.

The scalar constraint with coordinate density rho_b+f is

    8K psi Delta psi−rho_b psi⁶+rho_b+f=0,
    −8K Delta psi+F(x,psi)=0,
    F(x,z)=rho_b z⁵−(rho_b+f(x))/z.                       (1)

The density factor psi in the undivided curvature term and the inverse psi in the last term are essential. A physical-volume scalar density prescribed instead of this coordinate density would give a different equation.

## Existence, uniqueness and global response

For smooth f>=0 let M=(1+||f||infty/rho_b)^(1/6). Constants1 andM are respectively sub- and supersolutions. F_z=5rho_b z⁴+(rho_b+f)/z²>0 forz>0. An elementary monotone construction chooses c>=sup_[1,M]F_z and iterates

    (-8K Delta+c)psi_(n+1)=c psi_n−F(x,psi_n), psi_0=1.

The positive torus resolvent preserves order, c z−F is nondecreasing on the interval, and induction gives1<=psi_n<=psi_(n+1)<=M. Uniform bounded right sides supply W^(2,p) bounds at each finite p; compactness and the monotone limit solve(1), and elliptic regularity bootstraps to smoothness. Equivalently, the strictly convex energy is integral[4K|grad psi|²+rho_b psi⁶/6−(rho_b+f)log psi] on positive fields. The monotone iteration avoids asserting a direct method at the logarithmic boundary without a lower barrier.

Any positive solution has the same constant bounds by testing its minimum/maximum. Subtracting two positive solutions and integrating against their difference yields8K||grad difference||²+integral(F(psi)-F(chi))(psi-chi)=0, proving uniqueness. This uses the complete nonlinear monotonicity, not smallness of f. For f=0 the unique positive solution is1.

For nonzero f>=0, u=psi−1 solves

    -8K Delta u+c_psi(x)u=f/psi,
    c_psi=rho_b(psi⁵−psi^(-1))/(psi−1)>0

with the continuous value6rho_b atpsi1. Positivity of the torus Green resolvent/strong maximum principle gives u>0 everywhere. Hence a local positive coordinate-density increment does NOT have a compactly supported conformal response. This is elliptic endpoint support, not a propagation speed or causal statement. Nonconstant f forces nonconstant psi; constant f givespsi=(1+f/rho_b)^(1/6).

Integrating the UNDIVIDED constraint gives the exact quantitative identity

    <f>=rho_b<psi⁶−1>+8K<|grad psi|²>.                    (2)

Consequently0<=<psi⁶−1><=<f>/rho_b and6rho_b<psi−1><=<f>. Gradient cost is positive, not negative. For nonconstant f the gradient term is strictly positive. No extra normalization<psi>=1 can be imposed for nonzero positivef; it would conflict withpsi>1. The response has no useful uniform lambda→0 bound from this construction.

## Massless scalar realization and conserved charge

Set phi spatially constant and

    w=psi³ sqrt(2(rho_b+f))>0.                            (3)

The actual supplied scalar densityw²/(2sqrt(g)) equalsrho_b+f, and its source momentumw grad phi vanishes. Thus it realizes the endpoint constraint data exactly. This does not produce a trajectory from the initial homogeneous scalar data psi1,pi=lambda I,w_b=sqrt(2rho_b),phi constant.

For the actual massless common Hamiltonian with lapseN and shiftX, the w equation is a spatial divergence:

    wdot=aK partial_i(N sqrt(g)g^ij partial_j phi)+partial_i(X^i w).

Therefore< w > is conserved on the torus for the closed supplied scalar system. The initial value isw_b. For nonzero nonnegativef,psi>1 andsqrt(2(rho_b+f))>=w_b, so(3) givesw>w_b everywhere and<w>>w_b. Even allowing intermediate scalar gradients does not remove this conserved-charge mismatch. A change of scalar branch, external charge supply, scalar potential or different source map changes the hypotheses; endpoint matching alone is not an actual scalar event.

As an optional independent check of the scale, Cauchy-Schwarz and(2) give

    <w>²<=2(rho_b+<f>)<psi⁶>
          <=2(rho_b+<f>)²/rho_b,
    0<<w>−w_b<=2<f>/w_b.                                 (4)

The upper bound is exact for homogeneousf and strict for nonconstantf. This bound is not needed for the charge incompatibility. No positive lower bound proportional only to<f> is claimed here.

## Boundary cases and nonclaims

For lambda=0, rho_b=0 and the divided equation isDelta psi=−f/(8Kpsi). Its integral is impossible for nonzero nonnegativef. Forf=0, every positive constantpsi solves the constraint withpi0; uniqueness requires an added normalization. The scalar realization then hasw0, not a positive scalar-clock density. Signedf may defeat barriers/positivity and is not covered. Variablelambda/nonconformal tensors/nonzero source momentum or metric law changes are separate problems.

This is a supplied ordinary-continuum endpoint result. It proves no selected record source, original microscopic energy identification, causal event or evolution matching, physical clock or new framework premise. Await the complete frozen author proof for comparison. No numerical control would establish these universal PDE/constraint statements.
