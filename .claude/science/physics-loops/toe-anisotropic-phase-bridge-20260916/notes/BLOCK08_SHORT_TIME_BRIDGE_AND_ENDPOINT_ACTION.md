# Short physical time: convex bridge fluctuations and the endpoint action

Working derivation, 2026-09-16. This treats the actual supplied compact
Hamiltonian through its continuous Brownian paths. The interior path
fluctuations on a sufficiently short interval admit estimates uniform in
the spatial volume. The resulting endpoint action has a controlled
second-derivative correction and spatially decaying mixed derivatives.
These statements do not assert a phase, a globally convex compact endpoint
law, or the uniform susceptibility required in BLOCK02.

## 1. Model, constants, and the exact fixed-lift kernel

Let C be the oriented link-to-plaquette incidence matrix of a finite free
box in spatial dimension d>=2. Write E and P for the link and plaquette
counts and set

    q=2(d-1), Lambda=4q=8(d-1), ||C||_2^2<=Lambda,
    V(z)=sum_p[1-cos((Cz)_p)],
    H=-(g^2/2) Delta + V/g^2, g>0.

The bounds use only four links per plaquette and at most q plaquettes per
link. In the three-dimensional spatial model, q=4 and Lambda=16.
The full-angle Hamiltonian commutes with Gauss transformations. Its
kernel acts on the physical neutral subspace by restriction to invariant
functions, or by applying the Gauss projector to endpoints. A full-torus
kernel is not silently identified with a gauge-fixed quotient kernel.

Choose real lifts x,y in R^E of two compact endpoint configurations. Let

    ell_s=(1-s/T)x+(s/T)y, 0<=s<=T,
    G_T(s,t)=min(s,t)-st/T.

Under the free bridge law, eta has independent link components with
covariance g^2 G_T and zero endpoints. Define

    S(eta;x,y)=integral_0^T V(ell_s+eta_s) ds,
    F_T(x,y)=-g^2 log E_bridge exp[-S/g^2].                    (1)

Feynman-Kac gives the exact covering-space heat kernel with respect to
Lebesgue measure,

    k_T(x,y)=(2pi g^2 T)^(-E/2)
                  exp[-||y-x||^2/(2g^2 T)-F_T(x,y)/g^2].     (2)

The compact kernel with respect to normalized Haar is

    K_T(x,y)=(2pi)^E sum_(n in Z^E) k_T(x,y+2pi n).          (3)

This winding sum is part of the exact model. No term is dropped in the
claims below. Bounds on F_T concern one fixed lift; passage from those
bounds to estimates for the normalized sum(3) is a separate obligation.

## 2. Uniform convexity of the interior fluctuations

Set

    kappa=T^2/pi^2, r=Lambda kappa,

and assume r<1. The Dirichlet temporal precision is D=-partial_s^2.
Its inverse is G_T and its smallest eigenvalue is pi^2/T^2. The total
bridge action, before dividing by g^2, has fluctuation Hessian

    D + C* diag(cos(C(ell+eta))) C >= D-C*C >= (1-r)D.        (4)

This is positive at every fluctuation configuration and every real pair
of endpoints. It requires no small-field assumption and does not use a
false global comparison of a compact cosine with a raw squared curl.

We use the standard Brascamp-Lieb covariance inequality and its
Helffer-Sjostrand gradient representation. A primary source for the
finite-dimensional covariance bound and gradient commutator is Carlen,
Cordero-Erausquin and Lieb,
[arXiv1106.0709v2](https://arxiv.org/abs/1106.0709v2), equations(1.3)-(1.4)
and section2. PDF1-8 were read; SHA256
`f51623643f84a9b412ee9a4b098f177f7952b3ff38ec8d067a99a1b35ab7d4cc`.
The application here has a smooth quadratic confining action plus a
bounded cosine potential and the explicit positive Hessian(4).

To justify the infinite-dimensional bridge use, first retain finitely
many sine modes of the Dirichlet bridge on every link. Their precision
eigenvalues are exactly (n pi/T)^2; the same r applies for every cutoff.
The projected cosine Hessian has norm at most Lambda. Apply the
finite-dimensional inequalities there, then let the mode cutoff grow.
The bridge converges in L2 time, S is bounded and continuous in that
topology in each fixed finite box, and all endpoint derivatives used
below have bounded integrands. Dominated convergence passes their
expectations and covariances. Bounds for evaluation at a fixed time
follow by linear-functional approximation in the covariance form.
Thus no time lattice spacing occurs in the resulting constants.

In particular, under the tilted bridge measure of(1),

    Var[(C eta_s)_p] <= [g^2/(1-r)] 4 G_T(s,s)
                     <= g^2 T/(1-r).                        (5)

## 3. Mean displacement and a cosine comparison

Gaussian integration by parts gives, for each link e,

    E eta_e(s)=-integral_0^T G_T(s,t)
                    E[(C* sin(C(ell_t+eta_t)))_e] dt.

Every summand has modulus at most1 and there are at most q of them.
Since G_T is nonnegative and its row integral is s(T-s)/2,

    |E eta_e(s)|<=q T^2/8,
    |E(C eta_s)_p|<=q T^2/2.                                (6)

These are continuum identities; no claim of pointwise positivity of a
truncated sine-series covariance kernel is needed for this step.

For a real random variable Z with mean m and finite variance, Taylor's
formula with bounded second derivative yields

    |E cos(alpha+Z)-cos(alpha)| <= |m|+Var(Z)/2,

and the same bound for sin. By(5)-(6), put

    delta_0=q T^2/2 + g^2 T/[2(1-r)].

Uniformly in x,y,p,s and the volume,

    |E cos(C(ell_s+eta_s))_p-cos(C ell_s)_p|<=delta_0,       (7)

with the analogous sine estimate. The quantity in the first cosine is
the p-th scalar curl; the notation means taking cosine componentwise.

## 4. A small Hessian correction to the straight-path action

For an endpoint variation u=(u_0,u_1) define

    w_u(s)=(1-s/T)u_0+(s/T)u_1,
    Q_T(u)=integral_0^T ||C w_u(s)||^2 ds
          =(T/3)(||Cu_0||^2+<Cu_0,Cu_1>+||Cu_1||^2),
    A_u(eta)=integral_0^T <sin(C(ell+eta)),C w_u> ds.

Differentiation of the finite, positive bridge integral gives

    D_u F_T=E A_u,
    D_u D_v F_T
      =E integral <Cw_u,diag(cos(C(ell+eta))) Cw_v> ds
                      -g^(-2) Cov(A_u,A_v).                 (8)

The fluctuation derivative of A_u is C*[cos(C(ell+eta)) Cw_u]. Its
squared L2 time norm is at most Lambda Q_T(u). From(4) and
||D^(-1)||=kappa, the covariance inequality gives

    g^(-2)|Cov(A_u,A_v)|
         <= [r/(1-r)] sqrt(Q_T(u)Q_T(v)).                    (9)

Now let

    P_T(x,y)=integral_0^T V(ell_s) ds,
    R_T=F_T-P_T,
    delta=delta_0+r/(1-r).

Combining(7)-(9) proves the volume-independent estimate

    |D_u D_v R_T(x,y)|<=delta sqrt(Q_T(u)Q_T(v)).             (10)

In particular, delta tends to zero as T tends to zero at fixed g, and
has size O(T^2+g^2 T). The source directions are measured by their
spatial curls, so pure-gauge endpoint directions correctly have zero
bound and zero response. This is an actual coupled-Hamiltonian bridge
estimate, not the isolated Bessel convolution used in BLOCK01.

Inversion symmetry gives D R_T(0,0)=0. Integrating(10) along a line of
endpoints gives

    |R_T(x,y)-F_T(0,0)| <= (delta/2) Q_T((x,y)).              (11)

The field-independent constant obeys

    0<=F_T(0,0)<= P g^2 T^2/3.                              (12)

Indeed Jensen bounds F_T by the free expectation of S, while a free
plaquette fluctuation has variance4g^2G_T(s,s), giving
E[1-cos(Ceta)_p]<=2g^2G_T(s,s) and integral G_T(s,s)ds=T^2/6.
Equation(12) is extensive; it is not a volume-uniform bound on a total
partition-function error.

## 5. Spatial decay of the induced mixed derivatives

Join two spatial links if they share a plaquette. For a variation u,
let E_u be the set of links in plaquettes on which Cu_0 or Cu_1 is
nonzero. Suppose the plaquette supports of u and v are disjoint, and
let h be the graph distance between E_u and E_v (h may be0 when the
supports share an edge). Then

    |D_u D_v F_T| <= [r^(h+1)/(1-r)] sqrt(Q_T(u)Q_T(v)).      (13)

Here is the locality argument. In the finite sine-mode approximation,
write the total action as U, its fluctuation Hessian as D+W, and use
the nonnegative diffusion operator

    L_g=-g^2 Delta_eta + grad U dot grad_eta.

Integration by parts and the gradient commutator yield

    Cov(A_u,A_v)
      =g^2 E <grad A_u,(L_g+D+W)^(-1) grad A_v>.             (14)

For example, solve L_g f=A_v-E A_v, differentiate this equation, and
use grad L_g=(L_g+Hess U)grad. The explicit convexity gives the needed
inverse and finite-volume spectral gap; no gap in the physical spatial
Hamiltonian is assumed.

Let K_0=L_g+D. It has inverse norm at most kappa and preserves the
spatial link label of a vector field. Although L_g acts on functions of
all path variables, it acts separately on each vector component and
does not change that component's spatial label. The matrix W has norm
at most Lambda and can move a label only between links sharing a
plaquette. Consequently the norm-convergent Neumann expansion

    (K_0+W)^(-1)=sum_(n>=0)(-K_0^(-1)W)^n K_0^(-1)

has no matrix element between the two gradient supports before h
spatial moves. Its remaining norm is at most kappa r^h/(1-r).
Using the gradient bounds preceding(9) gives the stated covariance
bound. The direct first term of(8) is zero for disjoint plaquette
supports, proving(13). Passing the sine cutoff as above completes
the continuum-time argument. The same estimate holds for R_T since
P_T has no such mixed derivative.

## 6. What this controls and what it leaves open

Equations(10) and(13) control the actual effective action from integrating
interior continuous paths over a fixed short physical time T. Their
constants are independent of spatial volume and of any time regulator.
They supply a local small correction to the straight-path action at
small T. They do not show that the endpoint action is itself convex:
P_T contains the original compact cosine and has negative curvature
around plaquette angle pi.

The distinction is necessary already for a single plaquette. With fixed
endpoints of curl pi, the interior Hessian in its plaquette direction
has lowest temporal eigenvalue pi^2/T^2-4. It becomes negative for
T>pi/2. Thus the present short-time convexity mechanism cannot be
extended to all time intervals by the same bound. This observation
does not imply a mass gap or a phase obstruction.

The compact kernel remains the sum(3). Controlling the winding sectors
after repeated block composition, and connecting the corrected block
law to a gauge-phase estimate or the electric susceptibility, are still
open. The straight-path action is an integral along lifted endpoint
interpolation; replacing it by one midpoint or one endpoint Wilson
factor has not been justified here. No native law, coupling selection,
relativistic limit, matter theorem or axiom update follows from these
short-time estimates.

## Review and proposal status

The [claim-status contract](../CLAIM_STATUS_CERTIFICATE.md) and
[premise inventory](../ASSUMPTIONS_AND_IMPORTS.md) apply to this author
proposal. The [negative-claim checklist](../NO_GO_DISCIPLINE_CHECKLIST.md)
records the scoped comparison restrictions and untested alternatives.
Independent review, formal registration and retained landing are pending.
