# Actual local Hamiltonian in a supplied scalar clock gauge

Root proof candidate. Not independently checked, not a formal review or
framework result. The scalar and continuous canonical metric remain supplied
comparators. This attempts the contractf77dc148 and never identifies scalar
time with a physical Record clock. No square-root-reduced finite evolution
is substituted for the actual finite Hamiltonian below.

## 1. Exact normalization and changed law

Use the complete canonical gravity/scalar source in provisional PR9398,
head6515ffa8570f21a0b3a8790fdd8a2879347550b8. Write q=sqrt(det g),
B^ij=q g^ij, a,K>0 and s=aK. Its gravity density is

 T_g=(a/q)[tr(g pi g pi)-tr(g pi)^2/2],
 C_g=T_g-K B^ij R_ij,
 R_ij=D_k Gamma^k_ij-D_j Gamma^k_ik
       +Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik.

The coefficient is a/q, not a/(2q). Gamma is the literal Christoffel
expression using Dg. On each odd n=2J+1 torus use all six canonical pairs
p=n^3P, pi_ii=p_ii, pi_ij=p_ij/2 off diagonal. The continuum uses the
normalized mean on the period2pi torus. D is separately either the full
spectral representative ik_j or the centered i sin(epsilon k_j)/epsilon,
epsilon=2pi/n; products are ordinary grid products and all modes remain.

Supply a positive real time-independent analytic density w0(x) whose
reciprocal is analytic in the stated Wiener radius. It is the clock scalar's
density momentum, not a new degree of freedom in the reduced finite law.
Define N=q/w0 and the actual metric-only canonical Hamiltonian

 H_clock=mean[(q/w0)C_g+w0/2].                              (C1)

Define the diagnostic constraint densities

 C=C_g+w0^2/(2q),
 J_i=pi^jk D_i g_jk-2D_j(g_ik pi^jk).                      (C2)

Thus H_clock=mean N C exactly. N depends on the varied metric. The complete
canonical derivative is

 delta H_clock=mean[N delta C+C delta N].                  (C3)

Here delta w0=0; the scalar has been fixed to phi=t, Dphi=0. The extra
C delta N term is part of the finite Hamiltonian. It is not dropped at a
small but nonzero finite constraint residual.

For comparison only, on the open pointwise domain -2q C_g>0 define the
usual branch expression H_red=-mean sqrt(-2q C_g). At C=0 its derivative
is mean[(q/w0)delta C_g+(C_g/w0)delta q], exactly the derivative of(C1).
Its value there is -mean w0 whereas(C1) has value zero. Equality of
derivatives on the specified submanifold is the statement; no equality
away from it, no exact finite preservation and no all-data reduction follow.

## 2. Continuum constraint propagation, including the fixed density

This section uses continuum derivatives only. The already checked gravity
algebra is {C_g[f],C_g[l]}=G[s g^-1(f dl-l df)] and the spatial generator
acts on g by its Lie derivative. Adding the local potential w0^2/(2q)
does not change the CC bracket: kinetic/potential mixed terms cancel
because their undifferentiated factor fl is symmetric. This holds for
the fixed density w0 even when it is spatially nonconstant.

For a fixed test f, the metric dependence of N contributes

 {C[f],N}=f zeta,       zeta=a tr(g pi)/(2w0).             (C4)

Indeed the metric velocity of C[f] is
2af/q [g pi g-g tr(g pi)/2]; its g-inverse trace is
-af tr(g pi)/q. Since {C[f],N} is minus N/2 times this trace, the
sign and factor in(C4) follow. Full six-slot variation supplies the
same answer, including both entries of each off-diagonal variation.
Consequently(C3) and integration by parts give

 Cdot=s g^ij J_i partial_j N
       +partial_j(s N g^ij J_i)+zeta C.                   (C5)

Momentum propagation needs care: G contains only metric momentum and does
not transform the frozen density w0. A derivation that treats w0 as a
dynamical scalar density inside its bracket would be wrong. Under the
metric Lie variation, delta_X q=div(qX). Therefore

 delta_X N=N(X.grad log q+div X).

If the full scalar density were varied, delta_X w0 would be div(w0 X).
Correcting for its absence in the metric-only bracket gives

 {G[X],C[l]}=C[X.grad l]+mean[l(w0/q)div(w0 X)]

for external l. Include the additional bracket acting on N in H_clock:

 {G[X],H_clock}
  =mean[C(X.grad N-delta_X N)]+mean div(w0 X)
  =-mean[(q C/w0^2)div(w0 X)]
  =mean[w0 X.grad(q C/w0^2)].

The periodic integral of the divergence vanishes. Thus

 Jdot_i=w0 partial_i(q C/w0^2).                           (C6)

Equations(C5)-(C6) are a homogeneous linear first-order system for(C,J)
with coefficients determined by the evolving analytic metric/momentum and
the fixed analytic density. Zero initial constraints therefore propagate
for any interval on which these coefficients are bounded analytically.
An explicit uniqueness argument and its radius/time price are given below;
no finite-grid product rule is used to transfer this continuum statement.

On that zero-constraint solution, (C3) agrees with the full gravity-plus-
massless-scalar canonical equations at lapse N=q/w0 and zero shift. Its
scalar equations give phidot=Nw0/q=1 and
wdot=s partial_i(N B^ij partial_j phi)=0. Initial phi=0 therefore yields
phi=t and w=w0. Its spatial scalar momentum w partial_i phi vanishes, and
all total continuum constraints are(C2). Thus the same supplied scalar is
strictly monotone and supplies this coordinate time; no external unit-lapse
trajectory was relabeled as the finite evolution.

## 3. Exact finite adjoint variation and spatial support

Set eta=1/w0, Z^ij=(det g)eta g^ij and
T_c=a eta[tr(g pi g pi)-tr(g pi)^2/2]. Use analysis variables
u_l,A=D_l g_A, v_l,ij=D_l Z^ij. Define

 V(g,eta,u,v)=K[v_k,ij Gamma^k_ij-v_j,ij Gamma^k_ik]
              -K Z^ij[Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik],

with all repeated tensor indices summed and Gamma(g,u). Skew summation by
parts on the actual finite grid proves, exactly,

 H_clock=mean[T_c+V(g,eta,Dg,DZ)+w0/2].                   (C7)

In particular DZ has not been replaced by Z_g Dg+Z_eta Deta. The last
term has zero metric variation. With six-coordinate derivatives at fixed
eta, u,v, the full canonical equations are

 gdot_A=A_A=(T_c)_pA,
 pdot_A=-(T_c)_gA-V_gA+sum_l D_l V_u_l,A
                       +sum_l,ij Z^ij_gA D_l V_v_l,ij,
 udot_l,A=D_l A_A,
 vdot_l,ij=D_l(sum_A Z^ij_gA A_A),
 etadot=0.                                               (C8)

The plus sign and placement of Z_g outside D in pdot follow from varying
V_v D(Z_g delta g) and moving D by its skew adjoint. This includes the
metric-dependent-lapse correction(C3); treating Z as an independent
physical field would omit it. Time differentiation gives exact invariants
u-Dg=0 and v-DZ=0 from consistent initial conditions. These auxiliary
variables add no physical or canonical pairs.

Every equation has the form F0(U)+sum P_l(U)D_j Q_l(U), for
U=(g-I,p,u,v,eta). All local maps are algebraic analytic on |g-I|<1
and any bounded eta range. The eta dependence is polynomial; no evolving
inverse eta is taken. Spatial variation of w0 is retained through the
actual D Z and its continuum counterpart.

For centered D, each density term in(C7) is supported on a radius-one
star, with diameter two. Its actual canonical equations have radius at
most two. The literal scalar diagnostic C has radius two, and J radius
one. Spectral D keeps its full line support. These are changed collocated
laws, not a completion of the fixed staggered block112 seed.

## 4. Common analytic time and actual constraint error

Use |f|_rho=sum_k |fhat(k)|exp(rho|k|_1), ordinary or wrapped Fourier
coefficients as appropriate, and the summed component norm/N seminorm of
the checked analytic-evolution source. Assume real initial
|g0-I|_(2sigma0)<=1/8, and finite |p0|_(2sigma0), |eta|_(2sigma0)
and |w0|_(2sigma0), with pointwise w0>=w_min>0. The last two functions
are reciprocal on the real torus and their analytic norms are explicit
data hypotheses. They are sampled exactly; the finite reciprocal agrees
pointwise, not by Fourier truncation.

A uniform initial augmented bound is

 M0=|g0-I|_(2sigma0)+|p0|_(2sigma0)+|eta|_(2sigma0)
       +[|g0-I|_(2sigma0)+|Z(g0,eta)|_(2sigma0)]/(e sigma0).

Using Z rather than Z minus a constant is a safe upper bound. On
|g-I|<=1/4, |U|<=M=2M0+2, the same convergent inverse-metric series and
finite product majorants construct finite C0,C1,C_g and scale-Lipschitz
C with

 |F(U)|_rho<=C0+C1 N_rho(U),       |A(U)|_rho<=C_g,
 |F(U)-F(V)|_rho'<=C |U-V|_rho/(rho-rho').                (C9)

Unlike merely invoking the old constants, these constants are recomputed
from the actual T_c,Z,V and their six-coordinate derivatives in(C8), on
the new M ball. eta is included among the bounded components and has
zero derivative. Both derivatives satisfy |D_j(k)|<=|k_j|. The circular
product N inequality, rather than a discrete Leibniz equality, gives(C9).

For v=C1+1 choose

 T0=min{(M-M0)/(2(C0+1)),1/(16(C_g+1)),sigma0/(4v)}.

The shrinking-radius Dini argument at rho(t)=sigma0-vt gives
|U(t)|_rho(t)<=M0+C0t<M and |g-I|_rho(t)<=3/16<1/4,
rho(t)>=3sigma0/4. It applies to the ACTUAL finite ODE and yields
continuation to T0, uniformly in n. Exact auxiliary consistency follows
from(C8). Reality and positive metric are retained. Fixed w0 cannot
cross zero during the evolution.

Finite-mode compactness, the radius-reserved product limit and the ordered
Volterra argument from the checked parent now apply to this explicit
first-derivative system. With rho1=sigma0/2, rho0=sigma0/4 and
T1=min(T0,sigma0/(8eC)), they give a unique bounded analytic continuum
solution and the actual finite-to-sampled continuum comparison. This
step uses the identical proven norm inequalities, not an unverified
smooth-data existence theorem.

For clarity the new consistency constants can be made explicit by the
same finite list of maps in(C8). Let m_P,m_Q be their analytic norm
bounds at3sigma0/4 and delta=sigma0/4. For spectral D the derivative
commutator is bounded by

 4/(e delta) exp[-delta(J+1)/2]|f|_(3sigma0/4).

Thus take K_R=4 sum m_P m_Q/(e delta) and
K_0=4[|g0-I|_(3sigma0/4)+|Z(g0,eta)|_(3sigma0/4)]/(e delta).
For centered D take instead

 L(delta)=(1/6)[3/(e delta)]^3,
 K_R=L(delta)sum m_P m_Q,
 K_0=L(delta)[|g0-I|_(3sigma0/4)+|Z(g0,eta)|_(3sigma0/4)].

The eta sample has zero initial mismatch and zero evolution mismatch.
All local maps commute with actual sampling; the only failure is D.
These constants and the same Volterra estimate give

 |U_n(t)-I_n U(t)|_(sigma0/4)
 <=2(K_0+T1 K_R) r_n,

where r_n=exp[-sigma0(J+1)/8] or epsilon^2 respectively. Interpolant
comparison adds the usual analytic sampling tail. No multiplier on a
discarded high mode or projection of a canonical derivative is used.

To justify the zero-constraint propagation needed here, coefficients in
(C5)-(C6) and their spatial derivatives are bounded with a reserve from
3sigma0/4 to sigma0/2; w0 and its reciprocal have the required analytic
norms. The homogeneous first-order operator on(C,J) has a scale bound
K_cons/(rho-rho') for0<=rho'<rho<=sigma0/2, constructed by the product
and derivative bounds. Its Volterra uniqueness on the two radii
sigma0/2 and sigma0/4 follows for T_cons=sigma0/(8eK_cons), enlarged
K_cons if needed. Shorten the common time to T=min(T1,T_cons).
With zero initial constraints the continuum densities remain zero on
[0,T]. This is an additional time price; it is not an appeal to finite
closure.

The literal finite C,J in(C2) contain at most one D of a local analytic
map of U; q,u,eta and the fixed sampled w0 determine all other factors.
Their local Lipschitz estimate from sigma0/4 to sigma0/8, plus the same
sampling commutator, gives

 |C_n(t)|_(sigma0/8)+|J_n(t)|_(sigma0/8)<=K_diag r_n        (C10)

for continuum-compatible data. K_diag is finite, source-dependent and
independent of n. The equations do not preserve exact finite constraints
and do not acquire exact finite first-class algebra from this estimate.

## 5. Explicit inhomogeneous compatible clock data

Let lambda be any nonzero real constant. Let A(x) be a real symmetric,
trace-free, divergence-free analytic tensor on the torus. Put

 g0=I,  pi0=lambda I+A(x),  phi0=0,
 w0=sqrt(3a lambda^2-2a tr(A^2)), positive branch.          (C11)

Assume |A|_(2sigma0)<=|lambda|/4, where matrix norm sums all entries.
Then |2tr(A^2)/(3lambda^2)|_(2sigma0)<=1/24. The convergent binomial
series proves w0 and eta=1/w0 analytic with explicit norm bounds, for
example

 |w0|_(2sigma0)<=sqrt(3a)|lambda|*(1-1/24)^(-1/2),
 |eta|_(2sigma0)<=[sqrt(3a)|lambda|]^-1*(1-1/24)^(-1/2).

On the real torus w0>=sqrt(3a)|lambda|sqrt(23/24)>0.
Since R(g0)=0, the actual scalar density is
a[tr(A^2)-3lambda^2/2]+w0^2/2=0. The momentum density is
-2partial_j A^ij=0. All four continuum constraints are satisfied.
The sign of lambda is an additional expansion/contraction choice, while
the selected positive w0 fixes scalar clock orientation. Neither is a
physical selector supplied by the framework.

A nonconstant concrete family is

 A(x)=b cos(x3) diag(1,-1,0),
 0<|b| exp(2sigma0)<=|lambda|/8.

Its summed matrix norm is2|b|exp(2sigma0)<=|lambda|/4.
It is transverse and trace-free literally, and
w0^2=3a lambda^2-4a b^2 cos^2(x3) is nonconstant. Every actual finite
sample, for either derivative, also has C_n(0)=J_n(0)=0 exactly:
the flat curvature is zero, the scalar identity is pointwise, and each
nonconstant diagonal momentum component is independent of its own
differentiation coordinate. This includes aliased samples on small odd
grids; it is not an assertion that exact constraints remain zero later.

For a normalization control, b=0 gives w0=sqrt(3a)|lambda|, and the
continuum homogeneous solution is

 g(t)=exp[-a lambda t/w0] I,
 pi(t)=lambda exp[a lambda t/w0] I,
 N(t)=exp[-3a lambda t/(2w0)]/w0,
 phi=t, w=w0.

Direct substitution in(C8) and(C2) verifies it; every spatial derivative
is zero, so it is an exact finite solution as well. This is a control,
not the inhomogeneous analytic-time proof or a physical cosmology claim.

## 6. Scope and unclosed obligations

If independently confirmed, (C1)-(C11) supply a local canonical analytic
approximation in a supplied internal scalar time, with explicit nonconstant
clock density and constraint-compatible initial tensors. They retire the
unit-lapse condition only within this comparator, at the price of a positive
scalar density, its analytic inverse and a fixed clock branch. The local
extension(C1) is selected off the continuum constraint surface; other
off-surface laws and the direct square-root finite law are not covered.

The root's derivation is presently unchecked. Complete independent checking
must reconstruct especially(C4)-(C6), metric-dependent lapse variation and
the uniform first-derivative augmentation. A literal finite-gradient control
is not yet run. Native M2 realization, original rotor/record matter, actual
Record-clock selection, exact grid closure, smooth/Sobolev stability, physical
source law and long-time dynamics remain unresolved. No current axiom
inconsistency, retained status or TOE completion follows.
