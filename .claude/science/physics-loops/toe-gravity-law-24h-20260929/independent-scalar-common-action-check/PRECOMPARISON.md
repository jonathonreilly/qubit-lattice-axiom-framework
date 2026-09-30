# Independent coupled-scalar derivation before author proof

2026-09-30. New CONTRACT only has been read. No new author REPORT,
formulation, code, or results have been opened. The gravity spectral and
centered analytic evolutions were independently checked previously. This
is a prospective check of a supplied massless canonical scalar, not of
the original walker, record matter, rotor process, or clock.

## Actual finite variation

Write S=sqrt(det g), B=S g^{-1}, s=aK, and v_i=D_i phi. The added
algebraic density is

    M(g,w,v)=w^2/(2S)+(s/2) B^ij v_i v_j.

With density momentum w=n^3 W and the normalized grid mean, the scalar
canonical factor n^3 cancels the mean exactly, just as for metric p.
Using the actual skew finite D gives

    phi_dot=w/S,
    w_dot=s sum_i D_i(B^ij v_j),
    v_i_dot=D_i(w/S).

The gravity metric velocity A=T_p is unchanged. The gravitational p_dot
from the checked exact q=Dg,r=DB augmentation gains the local term -M_g
at fixed independent w,v. In matrix pairing,

    delta M= -w^2/(4S) tr(g^{-1} delta g)
       +(s/2) B'[delta g]^ij v_i v_j,
    B'[E]=S[(1/2)tr(g^{-1}E)g^{-1}-g^{-1}E g^{-1}].

Independent off-diagonal metric variations insert both symmetric entries;
pi_offdiag=p_offdiag/2 is still required. The scalar adds no metric p
dependence and hence changes neither q_dot=D A nor r_dot=D(B_g A).
The time identities preserve v-Dphi, q-Dg and r-DB exactly. A spatial
chain rule is neither needed nor generally valid on either grid.

For U=(h,p,q,r,phi,w,v), every RHS is still F0(U)+sum P(U) D_j Q(U).
All new local maps are polynomial in w,v and analytic in g on the same
metric-safe domain. The parent majorant construction therefore extends,
but its numerical constants must be ENLARGED for the scalar terms and
new initial norms; the vacuum values cannot simply be asserted unchanged.
A safe initial M0 adds ||phi0||_(2sigma0)+||w0||_(2sigma0) and
||phi0-mean(phi0)||_(2sigma0)/(e sigma0), the last bounding the full v
gradient. The kinetic metric-velocity bound still uses p, but can safely
use the enlarged total ball M. The same shrinking-radius and ordered
Volterra arguments should then give a positive common analytic time.

The spectral sampling defect has the previously checked exponential
rate; the centered defect has the previously checked all-frequency
epsilon^2 L(delta) rate. The initial v mismatch contributes its own
commutator on phi0. Local scalar coefficient maps commute with actual
sampling. No projection of scalar or metric canonical modes is allowed.

The scalar energy and w equation add only radius-one star terms and
radius-two equation stencils to the centered law. The augmented symbols
still require only upper derivative bounds, not an elliptic lower bound.

## Full continuum algebra and total constraints

Let G_m[X]=integral w X^i partial_i phi with normalized measure. Its
canonical action is delta phi=X.partial phi and delta w=partial_i(w X^i).
The sum with the gravity generator is the full cotangent lift and gives
{G[X],G[Y]}=G[[X,Y]]. M is a weight-one scalar density under this full
action, hence {G[X],C[N]}=C[X.partial N].

For the scalar CC bracket, ordinary continuum variation gives

    delta C_m[N]/delta phi=-s partial_i(N B^ij partial_j phi),
    delta C_m[N]/delta w=N w/S.

Their antisymmetrized contraction is

    s integral w g^ij partial_j phi (N partial_i M-M partial_i N)
       =G_m[s g^{-1}(N dM-M dN)].

The gravity-scalar cross bracket involving curvature is zero because
neither factor contains the conjugate metric momentum in that pairing.
The remaining metric kinetic/scalar pairing is pointwise proportional
to NM, and cancels only after the full lapse antisymmetrization. Together
with the parent gravity bracket, the exact FULL continuum result is

    {C[N],C[M]}=G[aK g^{-1}(N dM-M dN)].

Thus matching the scalar gradient coefficient to aK is load-bearing.
The claimed action is the common canonical action with this single C
and G, not propagation of test matter on a fixed metric. The matter
stress in p_dot is part of its actual variation.

The actual total density is C=C_g+M, and

    J_k=pi^ij q_k,ij-2D_j(g_ik pi^ij)+w v_k.

In the continuum at unit lapse and zero shift, J_dot=0 and
C_dot=partial_j(aK g^ij J_i). This is total constraint propagation;
separate gravity and matter momentum densities need not be conserved.
The densities have at most one derivative of a local augmented map, so
the parent's smaller-radius constraint-error argument should extend with
new majorants. No finite exact algebra is implied.

## Direct conformal reduction

Use a real analytic nonconstant periodic f, scalar amplitude b, phi=b f,
w=0, g_ij=psi^4 delta_ij, pi^ij=-(2H/a)psi^2 delta^ij with H constant.
Let F=|grad f|^2, beta=a b^2/16 and lambda=3H^2/(4aK).

The momentum constraint cancels pointwise:

    pi^ij partial_k g_ij=-(24H/a)psi^5 partial_k psi,
    -2partial_j(g_ik pi^ij)=+(24H/a)psi^5 partial_k psi.

The scalar contribution is zero since w=0. The gravity kinetic density
is -(6H^2/a)psi^6. In dimension three,
R(psi^4 delta)=-8psi^{-5}Delta psi. The matter gradient term is
(aK b^2/2)psi^2 F. Therefore the literal scalar constraint, divided
by the positive factor 8K psi, is exactly

    Delta psi=lambda psi^5-beta F psi.                 (A)

For mean psi=1, its mean equation fixes

    lambda=beta <F psi>/<psi^5>,
    H^2=(a^2 K b^2/12) <F psi>/<psi^5>.               (B)

No freely chosen nonzero H can be imposed independently here. The sign
of H can be chosen after its square is determined. For nonzero b and
nonconstant real f, the right side of (B) is positive once psi>0.

## A computable analytic fixed point

Fix the Wiener algebra A_rho with rho=2sigma0 and suppose F belongs to
it. This holds, for example, for the completely explicit f=cos(x_1),
where ||F||_rho=(1+exp(2rho))/2. Put psi=1+u, mean u=0, and let
L=-Delta on mean-zero functions, whose inverse has A_rho norm at most
one on the 2pi torus. Define

    R(u)=<F(1+u)>/<(1+u)^5>,
    Phi(u)=beta L^{-1}[F(1+u)-R(u)(1+u)^5].          (C)

The bracket is exactly mean zero; its sign in (C) follows from (A).
Choose r=1/100, s0=1+r, d0=2-s0^5>0, and M_F=||F||_rho.
On the mean-zero ball ||u||<=r, even before imposing reality,

    |<(1+u)^5>|>=d0,
    |R(u)|<=M_F s0/d0,
    Lip R<=M_F[1/d0+5s0^5/d0^2].

These give

    ||Phi(u)||<=beta M_F (2s0/d0),
    Lip Phi<=beta M_F[1+6t+5t^2],  t=s0^5/d0.

For r=1/100, 2s0/d0<11/5 and 1+6t+5t^2<14. The explicit smallness

    beta M_F<=1/256, equivalently a b^2 M_F<=1/16,    (D)

maps the ball strictly inside itself because (11/5)/256<1/100,
and gives contraction factor at most 14/256=7/128<1/16.
Iteration from u=0 therefore converges geometrically with an explicit
tail bound q^m/(1-q)||u_1-u_0||, q=7/128. It preserves real Fourier
symmetry and mean zero. The limit is real and psi>=99/100>0.

The solution has the required near-flat metric norm:

    ||g-I||_rho<=3[(1+r)^4-1]=0.12181203<1/8.

The factor three is essential because the parent metric norm sums all
three diagonal entries. B(g)=psi^2 I and the finite analytic pi above
also meet the parent's input requirements. The inverse Laplacian makes
the equation valid coefficientwise; its RHS is analytic, so no missing
elliptic regularity theorem needs to be imported for this fixed point.

For f=cos x_1, the first iterate is u_1=-(beta/8)cos(2x_1), and
lambda=beta/2+O(beta^2), H^2=a^2 K b^2/24+O(b^4).
These are independent normalization/sign checks. The solution cannot
be constant for nonzero b with this f: (A) at psi=1 would require F
constant. This gives actual inhomogeneous scalar and metric initial data.

These constraints are continuum identities only. Samples obey actual
finite constraints up to the controlled spectral or centered errors;
finite product-rule failure prevents silently making them exactly zero.
Their subsequent coupled evolution must include the scalar forcing and
the metric response, not hold the conformal ansatz fixed in time.

## Remaining author-proof checks

Check the six-component metric stress normalization; full, not merely
jet, continuum cross cancellation; added analytic norms/constants and
initial v mismatch; the sign and coefficients in (A)-(C); the metric
norm's factor three; a genuinely convergent analytic iteration with
positive denominator; correct total constraint densities; and clear
separation from original-record matter and from exact finite closure.
No numerical test, author's conformal proof, or general conformal-method
existence theorem was used to obtain this precomparison.
