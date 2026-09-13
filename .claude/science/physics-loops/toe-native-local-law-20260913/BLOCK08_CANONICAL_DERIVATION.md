# Moving frames, canonical spinors and a conditional metric action

Author derivation, 2026-09-13. Independent review pending. This is a
classical canonical construction on a compact oriented spin three-manifold
(or compact support), not an axiom derivation or quantum constraint theorem.
Use a three-torus to avoid bundle and boundary qualifications in the native
comparison. Fields are smooth, g is positive definite, and there is one
complex two-component spinor of each chirality. The equations below also
make sense for a single such classical spinor. Quantum interpretation,
canonical geometry, the source action and constraint interpretation are
supplied. No empirical constants are inferred.

## The phase-space term that moving geometry adds

Write a coordinate-row orthonormal inverse frame B, so g=(BB^T)^-1.
Rotating B to B R acts on its spinor as psi -> Spin(R)^-1 psi. On the
bundle of frames over positive metrics define the matrix connection

    A_B(delta B)=anti(B^-1 delta B),   anti(X)=(X-X^T)/2,
    rho(Omega)=Omega_ab sigma_a sigma_b/4.

It transforms as A_(BR)=R^-1 A_B R+R^-1 delta R. Thus delta psi+rho(A)psi
is covariant, and i/2 psi^dagger <->(delta+rho(A)) psi is invariant and
horizontal under simultaneous frame/spin rotation. At a fixed background
coordinate change J independent of the metric variation, B -> J B leaves
B^-1 delta B unchanged. This is the appropriate configuration-space
connection; it is not the intrinsic spatial Levi-Civita connection.

In the symmetric positive section E=g^-1/2, the reduced symplectic potential is

    Theta = int pi^ij delta g_ij
          + i/2 int psi^dagger <->delta psi
          + i int psi^dagger rho(A_E(delta E)) psi.          (P1)

Here pi is the gravitational momentum. Its coordinate canonical momentum
is P=pi+a, where a(delta g)=i psi^dagger rho(A(delta g)) psi. This is an
explicit Darboux description, so nondegeneracy and the Jacobi identity
follow from the ordinary product canonical structure. Use {g_ij,P^kl}=
delta_(i^k delta_j)^l and {psi_alpha(x),psi_beta^dagger(y)}=-i delta_alpha beta
 delta(x-y). For metric coordinates q^I (the six independent components),

    {pi_I,psi}=rho(A_I)psi,
    {pi_I,pi_J}=i psi^dagger rho(F_IJ)psi,
    F_IJ=partial_I A_J-partial_J A_I+[A_I,A_J].              (P2)

These formulas follow by substituting pi=P-i psi^dagger rho(A)psi. They
must not be replaced by a product bracket for (g,pi,psi).

For E=I+S, A=-[S,delta S]/2+O(S^2 delta S). Therefore

    F_E(V,W)|_I=-[V,W],
    F_g(h,k)|_I=-[h,k]/4.                                 (P3)

The second formula uses delta E=-h/2. The connection cannot be dropped
merely because A itself vanishes at the identity: its first variation is
nonzero. This is a curvature statement of this explicit connection, not a
no-go about other phase-space descriptions. Darboux momenta absorb its
one-form while changing the form of the Hamiltonian.

## The covariant variation that removes lapse-gradient cross terms

Let D_g be the intrinsic, torsion-free, self-adjoint Dirac operator on spinor
half-densities, D_g=-i gamma^i nabla_i^hd. For a covariant metric variation
h_ij, compare spinors using A. Its configuration-covariant variation is

    delta_h^A D_g = i/2 gamma^i h_i^j nabla_j^hd
                  +i/4 gamma^i nabla^j h_ij.              (P4)

A proof can be made at an arbitrary point in background normal coordinates
and a parallel orthonormal frame, then transported using covariance. At
that point delta e_a^i=-h_ai/2, and the intrinsic connection varies by

    delta omega_iab=(partial_b h_ia-partial_a h_ib)/2.

In -i sigma_i delta omega_iab sigma_a sigma_b/4, the Pauli vector contraction
is -i sigma.(d tr h-div h)/4. Its axial contraction vanishes because h is
symmetric. The variation of the half-density correction is
+i sigma.d tr h/4; these trace-gradient terms cancel. Together with the
principal variation +i sigma_i h_ij partial_j/2 this proves P4 at the point.
The construction is covariant under the frame and coordinate changes used
in choosing those normal coordinates. For an arbitrary section, the left
side is delta D+[rho(A_h),D], not just the component derivative of D.

Define the normal matter functional by the arithmetic source

    H_m[N]=int psi^dagger {N,D_g} psi/2.

Integrating the two first-order terms in P4 by parts, on a closed slice or
compact support, gives

    delta_h^A H_m[N]
      =i/4 int N h_ij [psi^dagger gamma^i nabla_hd^j psi
                     -(nabla_hd^j psi)^dagger gamma^i psi]. (P5)

All terms with derivatives of N cancel. This cancellation is specific to
the complete spin connection, half-density identification and the declared
symmetric source. It is the useful variation identity for the constraint
calculation, rather than a numerical vanishing check on a flat background.

For any spinor bilinear H=psi^dagger h(g)psi, P2 gives

    {pi_I,H}=-psi^dagger (partial_I h+[rho(A_I),h])psi.

Consequently P5 is exactly the derivative entering the mixed geometry/matter
Poisson bracket.

## Spatial generator and the normal matter bracket

For a spatial vector field a let D_g[a] be the half-density Kosmann operator

    D_g[a]=-i(a^i nabla_i^hd+div_g(a)/2
                 +gamma^i gamma^j nabla_[i a_j]/4),        (P6)

where antisymmetrization has weight 1/2. In flat coordinates this is
-i(a.partial+partial.a/2)+sigma.curl(a)/4. Set

    D_total[a]=int pi^ij (L_a g)_ij-int psi^dagger D_g[a]psi. (P7)

To check its origin without assuming a fixed-frame Lie algebra, consider
the active push of the coordinate-row symmetric frame. If J_a=partial a,
its polar rotation is the antisymmetric solution

    E Omega_a+Omega_a E=J_a E-E J_a^T,
    V_a E=-a.partial E+J_a E-E Omega_a,
    V_a psi=-(a.partial+partial.a/2)psi+rho(Omega_a)psi.

The geometric variation is V_a g=-L_a g. Evaluation of P1 on V_a is the
negative of P7. Indeed, the rotation coefficient from its two matter
terms is

    Omega_a+A_E(V_a E)=anti(E^-1 J_a E)-a^i A_E(partial_i E).

This is the component expression for the spin term in P6, with the stated
sign convention. It is also obtained by substituting the intrinsic
Levi-Civita connection and cancelling its coordinate Christoffel terms.
Invariance of P1 under the finite polar action gives an equivariant moment
map. In particular {D_total[a],D_total[b]}=D_total[[a,b]]. This statement
concerns the joint metric/spinor action; it does not assert that the
fixed-background spinor operators alone have that bracket.

For a fixed g the first-order operator identity is

    i[{N,D_g}/2,{M,D_g}/2]=D_g[a],
    a^i=g^ij(N partial_j M-M partial_j N).                 (P8)

At background normal coordinates, the common NM second-order and curvature
terms cancel. The remaining vector term is -i(a.partial+div(a)/2), and
the Pauli commutator is the spin term in P6, since
nabla_[i a_j]=(partial_i N)(partial_j M)-(partial_i M)(partial_j N).
This local calculation is covariant, proving P8 globally on the common
smooth domain. The classical bilinear Poisson convention then gives

    {H_m[N],H_m[M]}=-int psi^dagger D_g[a]psi.              (P9)

The minus sign follows from -i psi^dagger[h_N,h_M]psi and should not be
changed to i times the operator commutator.

## The local metric ansatz and its coefficient selection

In d>=2 dimensions temporarily, consider exactly the time-reversal-even
local scalar family

    H_g[N]=int N [alpha/sqrt(g)(pi^ij pi_ij-lambda pi^2)
                              +beta sqrt(g) R+gamma sqrt(g)],
    D_g^can[a]=int pi^ij L_a g_ij,
    pi=g_ij pi^ij.                                      (P10)

The pi here is a density of weight one. Coefficients are real constants.
There are no momentum derivatives, additional canonical fields or higher
curvature terms in this ansatz. We do not derive those exclusions from
native admissibility or matter propagation.

With an ordinary metric bracket, the terms ultralocal in the lapse cancel
between N,M. The only surviving functional derivative is the second-lapse-
derivative part of delta int N sqrt(g) R/delta g_ij:
sqrt(g)(nabla^i nabla^j N-g^ij Delta N). Contracting it with
2 alpha M(pi_ij-lambda pi g_ij)/sqrt(g) and integrating by parts yields

    {H_g[N],H_g[M]}
     =-alpha beta D_g^can[a]
       +2 alpha beta [(d-1)lambda-1] int a^j nabla_j pi.   (P11)

Here a^i=g^ij(N partial_j M-M partial_j N), and the derivative of the
density is its density-covariant derivative. The coefficient follows from
(pi_ij-lambda pi g_ij)(Hess^ij N-g^ij Delta N)
=pi_ij Hess^ij N+[(d-1)lambda-1]pi Delta N.

Strong equality to D_g^can[a] for every field in this ansatz gives

    alpha beta=-1,  lambda=1/(d-1),  gamma arbitrary.       (P12)

These conditions are sufficient by P11. Necessity does not presume that
the two structures are independent: at g=I on a torus, use N=1,M=cos x1.
A momentum with only pi^22=cos x1 has zero divergence but a nonzero integral
of a.partial pi, forcing the second coefficient to vanish. Then only
pi^11=cos x1 fixes -alpha beta=1. Thus neither alpha nor beta is zero.
The degenerate cases with one zero have zero pure normal bracket and do
not satisfy the displayed nonzero strong target for all momenta. This is
an ansatz classification, not a classification of every gravitational law.

For d=3, the inverse kinetic trace coefficient is lambda=1/2. Its Legendre
inverse has the familiar covariant kinetic trace coefficient 1; these are
different coefficients and should not be compared as equal numbers.

## Full classical closure in this declared family

Use P1/P2, d=3 and H[N]=H_g[N]+H_m[N]. The configuration-curvature addition
to {H_g[N],H_g[M]} is zero: both momentum gradients at the same point are
the same vector times N or M, and F is antisymmetric. The connection-
covariant mixed bracket vanishes after antisymmetrization in N,M by P5:
each factor is ultralocal in its lapse. Thus P11 and P9 give, at P12,

    {H[N],H[M]}=D_total[g^-1(N dM-M dN)],
    {D_total[a],H[N]}=H[L_a N],
    {D_total[a],D_total[b]}=D_total[[a,b]].                (P13)

The latter two follow from the invariant symplectic potential, scalar
Hamiltonian density and equivariant spatial action. This is strong
classical closure on the stated smooth phase space. It is not an
operator-ordered quantum algebra or a proof of its anomaly cancellation.
Necessity of P12 for this combined ansatz follows already on psi=0.
The coefficient gamma and nonzero alpha remain free; this construction
alone supplies no value for Newton's constant or the cosmological term.

The metric equation is dot g-L_shift g=2N alpha(pi_ij-pi g_ij/2)/sqrt(g).
Writing K_ij=(dot g-L_shift g)_ij/(2N), Legendre inversion gives
pi^ij=sqrt(g)(K^ij-Kg^ij)/alpha and the metric Lagrangian

    L_g=N sqrt(g)/alpha [K_ij K^ij-K^2+R-alpha gamma].      (P14)

Hence it is the ADM Einstein-Hilbert family with 16 pi G=alpha and
2 Lambda=alpha gamma, provided those conventional identifications are
chosen. A healthy TT kinetic branch asks alpha>0; that sign is an added
physical requirement, not selected by the algebra. Matter contributes the
last term of P1 to the Lagrangian and the H_m/D_m source terms. Dropping
that term changes the canonical structure used to establish P13.

## Status and next checks

The identities above are an author proposal pending independent review. The author primary now checks:
normal-coordinate Koszul variation and half-density cancellation; exact
Darboux curvature and polar moment map at generic positive frames; metric
bracket normalization and independence witnesses; native realization of
temporal spin and shift coefficients at both cones. A complete native
metric phase-space realization and a quantum interacting continuum remain
open. No closed conditional constraint algebra creates those premises.

## Two explicit checks of the omitted-connection model

These compare two declared models, not every possible canonical formulation.
If one uses a product bracket for (g,pi,psi) while leaving P7/P10 unchanged,
the connection terms in P2 are missing. Two local witnesses isolate their
effect; compactly supported smearings can reproduce these jets in an open
coordinate patch.

At g=I, take linear vector fields with symmetric Jacobians X and Y.
Their bracket has Jacobian -[X,Y]. The two metric/matter cross variations
of the product-bracket spatial generators give 2i rho([X,Y]); the bare
matter bracket gives i times the half-density transport of [a,b]. P7 asks
for only i rho([X,Y]) in addition to that transport. Thus the product-
bracket defect is i rho([X,Y]). The missing curvature contribution is
-i rho([X,Y]), from F_g(2X,2Y), and cancels it. With
X=diag(1,0,0) and Y_12=Y_21=1, the defect is -sigma3/2. It can have a
nonzero expectation in a spin-polarized test field. The natural connection
is zero at the flat frame, yet its curvature matters in this test.

A normal-bracket witness uses E=diag(2,3,4), zero spatial frame jets and a
metric velocity whose corresponding E velocity V has V_12=V_21=1.
Use N=1 and M=x3 at the chosen point x=0. The bare mixed bracket reduces
to the variation of the scalar spin connection with partial_3 delta E=V:

    delta C=-1/4 epsilon_abc E_3a V_jb (E^-1)_cj=1/6.

The first-order variation of gamma3 vanishes. Hence the product-bracket
mixed term is +(psi^dagger psi)/6 at that point. Any metric velocity V can
be attained by a suitable pi when lambda=1/2 and alpha is nonzero.
The general omitted term is

    -i/2 psi^dagger {gamma^j,rho(A_u)} psi
                                (N partial_j M-M partial_j N),

where u is the gravitational metric velocity for unit lapse. The natural
connection in P2 cancels this term by P5. The statement is about the
explicit single-chirality or unequal-density pair; an imposed cancellation
between equal opposite-chirality densities would not test every phase-space
field required by the strong bracket.
