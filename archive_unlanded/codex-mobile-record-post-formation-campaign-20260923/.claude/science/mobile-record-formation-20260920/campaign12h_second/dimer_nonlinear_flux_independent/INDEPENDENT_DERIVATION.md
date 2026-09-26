# Independent reconstruction before author-code comparison

2026-09-21. This document was written after reading the complete two supplied
notes, and the actual state, rate and current premises of the corrected routed
note at the identities in `PRE_COMPARISON_SOURCES.json`. No author nonlinear
checker, result or simulation was opened. The earlier routed proof is reused
only for its unchanged premises; its stationary fluctuation theorem is not a
nonlinear hydrodynamic theorem.

No actionable mathematical defect was found in this reconstruction. The
conclusions below have the finite-algebra and initial-time scope claimed by
the notes.

## 1. Coordinates and all population fluxes

Let the fourteen feature rows be mass, D1,D2,D3, X1,X2,X3, Y1,Y2,Y3,
Z12,Z13,Z23,w. On the six axis labels these are the signed-coordinate and
axis-indicator functions; on the eight cube labels they are all Walsh
characters. The resulting integer matrix has determinant -32768 in the
independent ordering. Inverting it gives exactly

    p_(Ai,sign) = (D_i + sign X_i)/2,
    p_(B,b) = [1-sum D + b.Y + sum_(i<j) b_i b_j Z_ij + b123 w]/8.

There are thirteen independent coordinates after fixing mass one. All
fourteen numerators must be strictly positive for an interior profile.

The homogeneous current of any scalar feature g follows by summing the
species current directly:

    F_g = gamma [<g e> cross Y + X cross <g b> - 2 <g> X cross Y].

For g=D_i, X_i, Y_i, Z_ij,w the needed expectations are respectively

    (<g e>,<g b>) = (X_i e_i,0), (D_i e_i,0),
                    (0,M_B e_i),
                    (0,Y_j e_i+Y_i e_j+w e_k),
                    (0,(Z23,Z13,Z12)).

This proves every component of the thirteen fluxes and F_rhoA without a
closure assumption. Their direct symbolic equality was also checked in all
39 spatial components. The total species flux vanishes on mass one.

At the orbit-isotropic rest background, the population D and Z feedback
starts quadratically in the vector perturbations; w is then driven through
Z at the next order. Existing nonzero Z or w would change that order
counting. The source explicitly confines the assertion to the stated
background.

## 2. Entropy identity on the simplex, not the ambient space

For fixed n define the symmetric matrix K by the two cross products in the
source; v=Kp and M=p^T Kp. The directional flux is
gamma[p elementwise v-pM]. Its ambient derivative is

    A=gamma[diag(v-M)+diag(p)K-2p v^T].

Although the ambient extension need not have zero total flux off the
simplex, A maps its mass-zero tangent space into itself at mass one. For
tangent u,z, with H=diag(1/p),

    u^T H A z = gamma u^T [diag((v-M)/p)+K]z.

This is symmetric in u,z and H is strictly positive. Taking a full-rank
tangent basis B therefore gives a positive metric B^T H B that symmetrizes
the actual thirteen-dimensional Jacobian. Every directional characteristic
matrix is similar to a real symmetric matrix; repeated or zero speeds are
allowed. This proves symmetrizability in the interior, not strict
hyperbolicity or any global solution theorem.

For eta=sum p log p and

    q/gamma = (p elementwise log p)^T v - eta M - M/2,

differentiate along a tangent z. Since dM=2v^T z, the derivative is

    gamma { (log p+1) elementwise (v-M)
            +K(p elementwise log p)-(2 eta+1)v }^T z,

which equals grad(eta)^T A z. The term -M/2 is necessary. At the exact
rational profile p_a=(a+1)/105, n=(1,2,-1), gamma=2/3 and
z=unit_0-unit_7, omitting it leaves derivative error -4/35. The independent
control verifies zero residual for the full formula and exact symmetry of
the restricted Hessian/Jacobian. Thus a smooth interior solution of the
candidate PDE conserves this mathematical entropy flux. No microscopic
inhomogeneous entropy-production estimate has been established here.

## 3. Rest optics and what its isotropy tests

At any constant rest population X=Y=0, the six vector equations close
linearly. Write D=diag(D_i), B=M_B, and R_n z=n cross z. Their directional
flux Jacobian is

    A6(n) = [[0,-gamma D R_n],[gamma B R_n,0]].

Equivalently Xdot=gamma D curl Y and Ydot=-gamma B curl X. Strict positivity
of the six axis weights gives D>0; strict positivity of the eight cube
weights gives B>0 because their vectors span R^3. The metric
diag(D^-1,B^-1) symmetrizes A6. On a periodic domain, integration by parts
then conserves (X^T D^-1 X+Y^T B^-1 Y)/2. The separately conserved
divergences are div(D^-1 X) and div(B^-1 Y). For example, D=(1/5,1/6,1/7),
n=(1,1,0),Y=e3 gives n.D(n cross Y)=1/30, while the D^-1-weighted quantity
is zero. Unweighted Gauss assertions would be false at this anisotropic
background; they are not claimed by the note.

For n=e1, the nonzero squared speeds are the eigenvalues of

    gamma^2 [[D2 rhoB,-D2 Z23],[-D3 Z23,D3 rhoB]].

Its trace, determinant and discriminant give exactly the displayed
square-root formula. B>0 implies rhoB^2>Z23^2, so both are strictly positive
when gamma!=0. Coincidence requires D2=D3 and Z23=0 because the discriminant
is a sum of two nonnegative terms. Applying the three cyclic tests forces
D_i=rhoA/3 and all Z=0, which in turn gives the same two speeds in every
unit direction. This criterion concerns the given vector rest sector.

The specified Z23=1/14 example has squared speeds 1/14 and 9/98 along e1
at gamma=1, and 4/49 twice along e2 and e3. All probabilities are positive.
For a separate generic positive anisotropic profile, the exact full
thirteen-field Jacobian was checked in all three coordinate directions and
n=(1,2,2)/3: its vector block is as above and receives no linear contribution
from the other seven fields. The full matrices have rank four in these
controls, with additional population response outside the vector block.

At D_i=1/7, X=Y=Z=0, changing w from zero to 1/14 preserves strict positivity
and the entire vector block but changes the full Jacobian. A proper rotation
that exchanges axes 1 and 2 and reverses axis 3 has determinant +1 and
flips b123, so this nonzero-w law is not fully cubic invariant. Optical
isotropy is genuinely weaker than full color-law isotropy. At gamma=0 all
Jacobians vanish; the source correctly excludes this case from positive
propagating-speed statements.

## 4. Exact four-context current and initial drift

For the winding matching, q_delta moves a black anchor by a_delta=delta-e1.
The +e1 channel is fixed and omitted. The remaining route cycles have four
distinct contexts for even N>=8, so their initial independent laws can be
multiplied even though later laws need not factorize.

With S=(gamma/2)K_delta, condition on the two endpoint labels a,b. Averaging
the outside labels gives E[h|a,b]=s_a-s_b with s=S(p_l+p_r). The net outward
species current is the expectation of

    (unit_a-unit_b)[k0/2+h/4].

Summing its two endpoint contributions gives exactly

    J = (k0/2)(p_u-p_w)
        +[(p_u+p_w) elementwise s-p_u(p_w.s)-p_w(p_u.s)]/4.

The current has mass zero. At equal laws p, it reduces to
J_delta=F_delta/2, retaining the routed channel's actual outer half rate.
The independent program enumerates all 14^4 quadruples in each of the five
nonfixed directions with four different rational laws, gamma=2/3 and
k0=5/2. All seventy current entries agree exactly. The integer drive range
is [-4,4] in units gamma/2, consistent with positivity for k0>|gamma|.
This is a direct finite-channel enumeration, not a full-torus trajectory
simulation.

An event changes the two endpoint indicators only. Hence initial drift at
u is sum_delta[J(u-a_delta)-J(u)]; contexts where u is outside the endpoints
change the rate, not its indicator. No incoming/outgoing channel is omitted
or doubled.

Here is a uniform Taylor justification independent of a product-evolution
assumption. Put h=1/N and extend each finite-stencil current to a smooth
periodic function J_h(x) by evaluating p at x-ha,x,x+ha,x+2ha. Its polynomial
dependence on these values implies J_0(x)=F_delta(p(x))/2. The fundamental
theorem of calculus gives

    R_h(x)=(J_h(x)-J_0(x))/h=integral_0^1 partial_h J_(theta h)(x) d theta.

The h derivative contains one derivative of p; its spatial derivative
contains at most two. Fixed C^3 periodic p is more than sufficient to bound
R_h in C^1 uniformly for N>=8. The constants depend on the fixed profile
and fixed rates, not N. A further spatial finite difference yields

    N[J_h(x-ha)-J_h(x)] = -(a.grad)F_delta(p(x))/2 + O(1/N).

Finally (1/2)sum_nonfixed a_delta tensor delta=I. This proves the stated
uniform initial-derivative estimate for all black anchors. The current
polynomial and the first Taylor coefficient were independently checked:
for the linear stencil p_l=p-hz,p_u=p,p_w=p+hz,p_r=p+2hz,

    d_h J_h|0 = DF_delta(p)z/4-k0 z/2.

As a control on the finite-N floor contribution, gamma=0 gives the exact
Fourier drift eigenvalue k0 sum_delta[cos(Q.a_delta/N)-1]. Because
sum a_delta a_delta^T=diag(8,2,2), N^2 times this eigenvalue tends to
-k0(4Q1^2+Q2^2+Q3^2). The symmetric floor therefore has a nonzero finite-N
effect, despite having zero leading Euler current. No diffusion limit is
being claimed here.

For a separately chosen fixed positive trigonometric profile, exact
four-context expectations and analytic derivatives were evaluated at four
fixed black anchors for N=8,16,32,64,128,256. The maximum initial-derivative
residual falls from 1.57624 to 0.0586614; N times it remains between 12.61
and 15.02. These sampled numerical values corroborate the estimate; the
uniform assertion is established by the derivative argument above, not by
the six-size table.

## 5. Verification boundary and failures

`independent_check.py` is independently assembled and has no author-code
imports. It uses exact SymPy/integer calculations for moment identities,
entropy normalization, optical tests, all 192080 four-context quadruples,
and the first stencil coefficient. Only the fixed-profile size sequence is
floating point. Its first execution succeeded; stdout, empty stderr,
versions and command/source receipt are preserved. No failed attempt was
discarded.

There is no finite-time local-equilibrium or nonlinear hydrodynamic proof
in this packet. No source is taken to provide one. The supplied winding
matching, independent inhomogeneous initial preparation, fixed C^3 profile,
even N>=8, strictly positive probabilities, and fixed k0>|gamma| are
material hypotheses. This initial preparation is not asserted to follow
from the earlier empty-start formation law. No quantum operation, matter
coupling, spacetime interpretation or physical field identification follows
from these checks.
