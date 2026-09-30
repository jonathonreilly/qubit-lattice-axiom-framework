---
claim_id: nonlinear_canonical_gravity_analytic_approximation_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied continuous canonical metric law on odd periodic cubic grids: exact strict-band spectral constraint coefficients and structure-Jacobi coefficients, grid-uniform short-time analytic convergence of the full Hamiltonian evolution and true constraint densities, a centered finite-range continuation with second-order error, a coupled canonical massless scalar with explicit compatible conformal data, and a metric-only canonical extension in a supplied positive scalar-clock density with full analytic-time constraint control. The carrier, law, analytic preparation, lapse or clock gauge, and continuum refinement are supplied."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nonlinear_canonical_gravity_analytic_approximation_2026_09_30.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Test a physical source and carrier realization separately from this supplied analytic approximation."
conditional_surface_status: "The stated approximation theorems hold for the law and analytic data explicitly defined here."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A controlled nonlinear approximation for a supplied canonical law, with its finite carrier and all canonical variations retained."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Analytic approximation of a supplied canonical gravity and scalar law

**Type:** bounded_theorem

**Status:** conditional-support (supplied model; unaudited)

This is an author proposal for the conditional mathematical theorem below.
Independent review and audit remain separate; no audit status is asserted.

**Target.** Prove strict-band spectral coefficient identities and a common
positive analytic time of convergence for the actual full finite canonical
Hamiltonians defined below, including their true constraint densities,
their local centered continuation, their supplied massless scalar, and a
metric-only evolution in a specified scalar clock gauge.

The continuous metric carrier, Hamiltonian, external unit lapse or supplied
scalar clock gauge, scalar, analytic initial data and refinement of a fixed
period are mathematical inputs. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) specify their
own lattice, one-site algebra, admissibility and record content; this note
does not derive the present inputs from them. The registered scale-reference,
kinetic-isotropy and realized-state primitives retain their declared roles.
No axiom or primitive is added. No original walker, rotor record process,
physical record clock or observable-source identification enters the proof.

## Statement and proof obligations

Fix a,K>0 and s=aK. On the period-2pi three-torus, let g=I+h be a real
positive metric and pi its symmetric density momentum. On every odd grid
n=2J+1 use all six independent canonical metric pairs. The optional scalar
adds one real canonical pair. Define the full finite functions by the
literal formulas in the next section and use ordinary grid products.

The theorem has four related parts.

1. For the spectral derivative, evaluate fields and all independent
   smearings on Fourier support Q_B with 5B<=J. The full finite Poisson
   bracket agrees with the continuum constraint algebra through field
   degree three for scalar-scalar and spatial-scalar brackets, through
   the complete degree two for spatial-spatial brackets, and through
   degree two for the substituted structure-Jacobi expressions. Explicit
   scalar-constraint coefficients through degree four are given below.
   Functional differentiation takes place on the full carrier.
2. For any sigma0>0, real initial ||h0||_(2sigma0)<=1/8 and finite analytic
   momentum norms, the actual unit-lapse, zero-shift finite Hamiltonian
   solutions from sampled data exist on a common T>0. Spectral solutions
   converge in radius sigma0/4 to the continuum solution with error
   C exp[-sigma0(J+1)/8]. The actual finite constraint densities have the
   same rate in radius sigma0/8 when the continuum initial constraints
   vanish. The constants are finite and independent of J.
3. Replacing every derivative in the Hamiltonian by the centered difference
   with epsilon=2pi/n gives the same common-time conclusion with
   O(epsilon^2) state and constraint errors. Its unit-lapse Hamiltonian
   has a radius-one-star density. The massless scalar extension satisfies
   both evolution results with enlarged constants. A computable conformal
   contraction below supplies nonconstant scalar data satisfying all
   continuum constraints and the stated metric norm bound.
4. For a fixed positive analytic scalar density w0 with analytic reciprocal,
   the metric-only Hamiltonian (36) has its own grid-uniform analytic time
   T1 and the same spectral and centered error rates. Its true continuum
   scalar and momentum constraints propagate on all of T1 by a positive
   constraint energy. For compatible data this solution realizes phi=t,
   w=w0 in the supplied scalar theory. Explicit nonconstant tensor/clock
   data are given in (47). The finite law retains the metric-dependent
   lapse variation even off the constraint surface.

The spectral coefficient statement also allows the explicitly specified
quadratic scalar potential m^2 phi^2/2. The evolution and compatible-data
statements here are made for m=0. They do not require strict-band
preservation during evolution. T is constructed from majorants; a plotted
trajectory duration is not its certification. The algebraic statements
include zero modes, B=0 and arbitrary permitted smearings. The analytic
argument requires positive metric and positive radius reserves; a,K>0
and the fixed physical period are part of the theorem's domain.

The obligation chain is proved in this note: canonical pairing and literal
variation; full continuum algebra and structure variations; full-carrier
contraction-tree transfer; exact first-order augmentation; uniform analytic
majorants and continuation; compactness and ordered Volterra uniqueness;
sampling consistency; total constraint propagation; the conformal fixed
point; and the scalar-clock variation, positive constraint energy and
analytic approximation. There is no unproved terminal lemma inside the
stated theorem.
Physical realization of the supplied carrier and source is a further
question, not an implicit premise or claimed consequence of this theorem.

## Full carrier, pairing and literal law

Let V=n^3, x_r=2pi r/n and Q_J={-J,...,J}^3. Grid mean is V^{-1}sum_r;
continuum mean is (2pi)^{-3}integral. The independent coordinates have

    {h_A(r),P_B(t)}=delta_AB delta_rt,
    A=(11,22,33,12,13,23), p_A=V P_A,
    pi_ii=p_ii, pi_ij=p_ij/2 for i<j.

Then mean(pi^ij delta g_ij)=sum_(r,A) P_A delta h_A exactly. With
fhat(k)=V^{-1}sum_r f(r)exp(-ik.x_r), the bracket is

    {hhat_A(k),phat_B(l)}=delta_AB delta_(k+l=0 modulo n).

Reality pairs opposite modes. Complex Fourier calculations mean the
complexification of this real bracket, not a different canonical law.
The spectral D_j has multiplier ik_j on Q_J. Products are convolution
modulo n. D is skew under the mean, but generally has no product rule.
Its one-dimensional off-diagonal matrix entries are
(-1)^(r-t)/(2sin(pi(r-t)/n)); its support grows along coordinate lines.
No low-band projection is part of the law or bracket.

At each positive g define, with repeated spatial indices summed,

    S=sqrt(det g), B^ij=S g^ij,
    Gamma^k_ij=(1/2)g^kl(D_i g_jl+D_j g_il-D_l g_ij),
    R_ij=D_k Gamma^k_ij-D_j Gamma^k_ik
             +Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik,
    T=a/S [tr(g pi g pi)-(1/2)tr(g pi)^2],
    C_g[N]=mean N[T-K B^ij R_ij],
    G_g[X]=mean pi^ij[X^k D_k g_ij+g_ik D_j X^k+g_jk D_i X^k].       (1)

The curvature is a literal definition; no discrete chain-rule rewrite is
used. The Hamiltonian for the unit-lapse results is H=C_tot[1], with shift zero.
The separate scalar-clock result uses (36), also with shift zero.
For a supplied scalar phi and density w=V W, {phi(r),W(t)}=delta_rt,

    M=w^2/(2S)+(s/2)B^ij D_i phi D_j phi+(m^2/2)S phi^2,
    C_tot[N]=C_g[N]+mean(N M),
    G_tot[X]=G_g[X]+mean(w X^i D_i phi).                         (2)

The action is integral dt[mean(pi:gdot+w phidot)-C_tot[N]-G_tot[X]].
Unit-lapse finite evolution varies the canonical fields at fixed N=1,X=0. In the
continuum these same functionals have the constraint algebra proved below.
No finite multiplier-consistency or first-class claim is inferred merely
from this action's notation.

This collocated law changes the derivative, placements and lapse timing of
the staggered nearest-difference seed considered elsewhere in the repo.
A slot-offset Fourier rephasing of both canonical partners preserves the
opposite-mode bracket, but such interpolation is generally nonlocal and
does not restore the former lapse timing. This is an explicitly changed
law, not a completion of a fixed finite-zone seed.

## Explicit Taylor coefficients and structures

Count each h,pi,phi,w as field degree one and smearings as degree zero.
Let t=tr h, t2=tr h^2, t3=tr h^3 and set

    s0=1, s1=t/2, s2=t^2/8-t2/4,
    s3=t^3/48-t t2/8+t3/6,
    u1=-t/2, u2=t^2/8+t2/4.                                  (3)

The s coefficients belong to S, and the u coefficients to 1/S. To retain
all derivative placements, define H_r=(-h)^r and, for positive r,s,

    Gamma_r^k_ij=(1/2)H_(r-1)^kl(D_i h_jl+D_j h_il-D_l h_ij),
    L_r,ij=D_k Gamma_r^k_ij-D_j Gamma_r^k_ik,
    Q_rs,ij=Gamma_r^k_kl Gamma_s^l_ij-Gamma_r^k_jl Gamma_s^l_ik.

The curvature coefficients are

    R1=delta^ij L_1,ij,
    R2=delta^ij(L_2,ij+Q_11,ij)-h^ij L_1,ij,
    R3=delta^ij(L_3,ij+Q_12,ij+Q_21,ij)
         -h^ij(L_2,ij+Q_11,ij)+(h^2)^ij L_1,ij,
    R4=delta^ij(L_4,ij+Q_13,ij+Q_22,ij+Q_31,ij)
         -h^ij(L_3,ij+Q_12,ij+Q_21,ij)
         +(h^2)^ij(L_2,ij+Q_11,ij)-(h^3)^ij L_1,ij.            (4)

In particular R1=D_i D_j h_ij-D_k D_k tr h. Put

    A0=tr(pi^2)-(1/2)tr(pi)^2,
    A1=2tr(h pi^2)-tr(pi)tr(h pi),
    A2=tr(h pi h pi)-(1/2)tr(h pi)^2.

The gravity scalar densities through degree four are exactly

    C1=-K R1,
    C2=a A0-K(R2+s1 R1),
    C3=a(A1+u1 A0)-K(R3+s1 R2+s2 R1),
    C4=a(A2+u1 A1+u2 A0)-K(R4+s1 R3+s2 R2+s3 R1).            (5)

C_d[N] means mean N times this density. The spatial functional terminates:

    G1[X]=2mean(pi^ij D_i X_j),
    G2[X]=mean pi^ij(X^k D_k h_ij+h_ik D_j X^k+h_jk D_i X^k),
    G_d=0 for d>=3.                                          (6)

For v_j=N D_j M-M D_j N, the structure coefficients are

    F0^i=s v_i, F1^i=-s h^ij v_j, F2^i=s(h^2)^ij v_j,
    U(X,N)=X^j D_j N,
    V(X,Y)^i=X^j D_j Y^i-Y^j D_j X^i.                        (7)

No h correction to U,V is supplied in this family. Quartic C4 is needed:
{G1,C4} has degree three, and a nested (4,1,1) bracket has degree two.

Writing phi_i=D_i phi, the scalar additions are

    M2=w^2/2+s phi_i phi_i/2+m^2 phi^2/2,
    M3=u1 w^2/2+s(s1 delta^ij-h^ij)phi_i phi_j/2+m^2 s1 phi^2/2,
    M4=u2 w^2/2+s(s2 delta^ij-s1 h^ij+(h^2)^ij)phi_i phi_j/2
                                               +m^2 s2 phi^2/2. (8)

There is no degree-one scalar term; G_m is exactly degree two. These
expressions follow by inverse/determinant series in (1)-(2), with the
full grid operations retained. They are not defined by imposing desired
bracket residuals.

## Continuum algebra, sign and field-dependent Jacobi terms

In this section replace D by ordinary torus derivatives. The generator's
actual cotangent action is

    {g_ij,G[X]}=X^k partial_k g_ij+g_ik partial_j X^k+g_jk partial_i X^k,
    {pi^ij,G[X]}=partial_k(X^k pi^ij)
                     -pi^kj partial_k X^i-pi^ik partial_k X^j,
    {phi,G[X]}=X^i partial_i phi,
    {w,G[X]}=partial_i(X^i w).                                (9)

The finite formulas with the unexpanded D(X pi) are also exact by skew
summation. Continuum tensor Lie commutators and scalar-density covariance
give {G[X],G[Y]}=G[[X,Y]] and {G[X],C[N]}=C[X.partial N].

For the nontrivial scalar-scalar identity put pi_g=g_ij pi^ij. Ordinary
variation, the determinant identity, the covariant delta-Gamma formula
and two integrations by parts give

    delta C_g[N]/delta pi^ij=2a N/S(pi_ij-g_ij pi_g/2),
    delta mean(N S R)/delta g_ij
       =S[-N Einstein^ij+nabla^i nabla^j N-g^ij Delta_g N].   (10)

Here delta Gamma^k_ij=g^kl(nabla_i delta g_jl+nabla_j delta g_il
-nabla_l delta g_ij)/2. Periodicity removes the boundary terms. Kinetic-
kinetic and curvature-curvature brackets vanish; ultralocal terms
proportional to NM cancel. In dimension three the DeWitt subtraction gives

    (pi_ij-g_ij pi_g/2)(nabla^i nabla^j N-g^ij Delta_g N)
       =pi^ij nabla_i nabla_j N.

Hence

    {C_g[N],C_g[M]}
      =2s mean pi^ij(N nabla_i nabla_j M-M nabla_i nabla_j N)
      =G_g[s g^{-1}(N dM-M dN)].                             (11)

Symmetry of pi cancels the crossed first derivatives in the last equality.
At g=I this is G1[+s(N partial M-M partial N)], fixing the positive sign.

For the scalar,

    delta C_m[N]/delta w=Nw/S,
    delta C_m[N]/delta phi=-s partial_i(N B^ij partial_j phi)+N S m^2 phi.

Direct contraction gives the same shift in G_m. The gravity curvature has
zero bracket with C_m. The remaining gravity kinetic/scalar cross terms
are generally nonzero individually, but their metric variations are local
with a factor NM, so their two antisymmetrized orders cancel. This remains
true for those cross terms on the grid and alone asserts no finite scalar
algebra. The continuum combined generators act on all fields in (9), so
the full common density obeys

    {C[N],C[M]}=G[F(N,M)], F=s g^{-1}(N dM-M dN),
    {G[X],C[N]}=C[X.partial N], {G[X],G[Y]}=G[[X,Y]].         (12)

The scalar gradient coefficient s=aK is load-bearing. With kinetic and
gradient coefficients b,c in that sector one instead needs bc=aK.
The value s=aK is an explicit law input; its physical walker or stress
identification is outside this construction.

Canonical Jacobi is exact for differentiable functionals. For substituted
structure expressions, its field dependence must actually be included.
For three scalar generators,

    {{C[N],C[M]},C[L]}=C[F(N,M).partial L]+G[{F(N,M),C[L]}],
    {F^i(N,M),C[L]}=-2as L/S (pi^ij-g^ij pi_g/2)
                                      (N partial_j M-M partial_j N). (13)

The cyclic C smearing cancels by symmetry of g^{-1}; the cyclic G
smearing cancels because sum_cyclic L(N dM-M dN)=0. The matter density
contains no metric momentum and adds no term to this variation of F.
Writing delta_X F={F,G[X]} with independent fixed N,M, the remaining
nontrivial shift relation is

    F(X.partial N,M)+F(N,X.partial M)-[X,F(N,M)]+delta_X F(N,M)=0.

The first two terms equal s g^{-1} L_X(N dM-M dN); the last two are its
negative because delta_X g^{-1}=L_X g^{-1}. The scalar relation is
[X,Y].partial N-X.partial(Y.partial N)+Y.partial(X.partial N)=0,
and the all-spatial relation is sum_cyclic [[X,Y],Z]=0. These establish
all structure-Jacobi types with the inverse-metric variation retained.

## Transfer to the full finite spectral bracket

Suppose every original field and independent smearing has support Q_B.
A homogeneous degree-d functional has d field leaves and one smearing
leaf. Full functional variation removes a field leaf before any band
evaluation; its evaluated gradient can have support dB, including modes
absent from the input. Those directions remain in the canonical bracket.

Expand a nested bracket of t original polynomial functionals using the
ordinary product rule for functional differentiation. Each term has a
tree of t vertices and t-1 canonical contractions: each new bracket joins
a new functional to the previous component, and the constant Poisson
tensor introduces no additional vertex or loop. For final field degree r,
the number of surviving original field/smearing leaves is r+t.

Cut a contraction edge. Momentum conservation fixes its unwrapped momentum
as the signed sum of leaves on one component. A differentiated product
subtree has the same subset-sum property. Thus every internal momentum,
including momenta supplying derivative multipliers, has componentwise
size at most (r+t)B. If (r+t)B<=J, these modes all exist on the FULL
finite carrier, partial products do not wrap, and the spectral multipliers
equal the continuum ones. There is no free loop momentum. The final
total momentum also lies within J<n, so modular zero equals actual zero.
The Fourier Poisson pairing has already been normalized. Every contracted
coefficient therefore agrees with its continuum value.

For a single CC or GC bracket through r=3, t=2 gives five leaves. For
nested brackets through r=2, t=3 again gives five. GG has r<=2 and t=2.
The RHS structures have the same original leaves; an evaluated F2 can
have support 4B and is not relabeled as band B. Consequently 5B<=J gives

    [{C_<=4[N],C_<=4[M]}-G[F0+F1+F2]]_(degree<=3)=0,
    [{G[X],C_<=4[N]}-C_<=4[X.DN]]_(degree<=3)=0,
    {G[X],G[Y]}-G[X.DY-Y.DX]=0,                              (14)

and the structure-Jacobi expressions through degree two. Scalar and
gravity-scalar terms have the same leaf counting. C4 contains every
possible original vertex degree at the nested order. One applies the
tree lemma afresh to a nested bracket; differentiating an equality known
only at band-restricted evaluations would not be a proof.

For fixed band directions scale all fields by z. The full sampled functions
and their residuals are analytic on a sufficiently small complex disk
connected to g=I, for example where |z|max_x||hbar(x)||_op<1. The vanishing
coefficients imply the finite-system Cauchy estimate

    |residual(z)|<=M_R (|z|/R)^4/(1-|z|/R),
    M_R=max_(|w|=R)|residual(w)|,

on any regular closed circle R. This fixed-system remainder is separate
from the uniform evolution estimate proved next.

An explicit all-zone value illustrates the evaluation scope. At n=7 take
x-dependent h_yy=q=cos x, pi^yy=p=cos3x, all other entries zero, and
X^x=1,Y^x=cos3x. The relevant functional is mean(p X Dq). For mode
indices alpha,beta,gamma,delta summing to zero modulo7 its GG difference
has coefficient

    -gamma[wrap(beta+gamma)-wrap(alpha+gamma)-(beta-alpha)].

The two conjugate tuples (0,3,1,3) and (0,-3,-1,-3) contribute 7/8
each, giving exactly 7/4. This is a concrete value for the supplied law
outside 5B<=J, not a theorem excluding other laws. Also X.Dh already
generates a 2B harmonic from appropriate band-B X,h. The analytic
evolution argument below retains that harmonic and every other generated
canonical mode.

## Exact first-order analysis of the actual Hamiltonian

For the evolution claims set m=0. Let q_l,A=D_l g_A and r_l,ij=D_l B^ij.
For the scalar also put z_i=D_i phi. Treat q as six metric slots per
derivative and r as nine independent matrix slots while differentiating
local functions; evaluate on their actual symmetric values afterwards.
Skew summation by parts, with no spatial chain rule, gives

    H=mean[T+V(g,Dg,DB)+M(g,w,Dphi)],
    V=K[r_k,ij Gamma^k_ij-r_j,ij Gamma^k_ik
           -B^ij(Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik)]. (15)

Here Gamma is algebraic in g,q. Set A_A=T_pA. The exact augmented system is

    gdot_A=A_A,
    pdot_A=-T_gA-V_gA-M_gA+sum_l D_l V_q_l,A
                              +sum_l,ij B^ij_gA D_l V_r_l,ij,
    qdot_l,A=D_l A_A,
    rdot_l,ij=D_l(sum_A B^ij_gA A_A),
    phidot=w/S,
    wdot=s sum_i D_i(B^ij z_j),
    zdot_i=D_i(w/S).                                         (16)

Omit M and the last three equations for vacuum. In the r variation,
delta r=D(B_g delta g); moving D by its adjoint puts B_g OUTSIDE D V_r
in the Hamiltonian gradient and yields the positive sign in pdot. In
particular DB has not been replaced by B_g Dg. The scalar stress at fixed
w,z is determined by

    delta M=-w^2 tr(g^{-1}delta g)/(4S)+(s/2)B'[delta g]^ij z_i z_j,
    B'[E]=S[(1/2)tr(g^{-1}E)g^{-1}-g^{-1}E g^{-1}].           (17)

This includes both symmetric entries in an off-diagonal coordinate
variation. Matter changes the metric momentum, not just the scalar
trajectory on a fixed background. The factors V from the density brackets
cancel the normalized mean in all equations.

Ordinary TIME differentiation gives (q-Dg)dot=0, (r-DB)dot=0 and
(z-Dphi)dot=0. Consistent initial data remain consistent exactly, so (16)
is an analysis of the same canonical Hamiltonian rather than an enlarged
physical phase space. It is also an analytic vector field on a full
neighborhood off those relations. Every component has the finite form

    F(U)=F0(U)+sum_l P_l(U) D_(j_l) Q_l(U),                  (18)

where U=(h,p,q,r,phi,w,z) and the local maps are algebraic analytic near
g=I. Thus the analysis loses only one spatial derivative. In vacuum drop
the scalar slots. These identities hold for either derivative and for
ordinary continuum derivatives.

## Uniform analytic majorants and positive common time

For a scalar use ||f||_rho=sum_k |fhat(k)|exp(rho|k|_1), and N_rho(f)
for the same sum with the factor |k|_1. Sum norms over all components.
Metric matrix norms count both off-diagonal entries, whereas p has six
independent entries. For q use its symmetric metric placement and for r
all nine slots. Include these fixed component weights in every majorant.
Finite sums use Q_J; continuum sums use Z^3.

For both ordinary and circular products,

    ||fg||_rho<=||f||_rho||g||_rho,
    N_rho(fg)<=||f||_rho N_rho(g)+N_rho(f)||g||_rho,
    ||D_j f||_rho'<=||f||_rho/[e(rho-rho')].                  (19)

The first two follow from |wrap(k+l)|_1<=|k|_1+|l|_1. The last follows
from sup_(u>=0)u exp[-(rho-rho')u]=1/[e(rho-rho')]. For centered D its
symbol is bounded above by |k_j|, giving the same estimate. None of
these statements is a finite Leibniz rule or a lower symbol bound.

Here is a finite procedure specifying all constants below. For z=||h||<1,
Neumann and exp[+/-tr log(I+h)/2] series give

    ||g^{-1}||<=3+z/(1-z),   N(g^{-1})<=N(h)/(1-z)^2,
    ||S||,||1/S||<=(1-z)^(-1/2),
    N(S),N(1/S)<=N(h)/[2(1-z)^(3/2)].                        (20)

Indeed |tr h^m|<=||h||^m in the matrix entry norm; differentiating the
absolutely convergent scalar majorants and using the product seminorm
rule gives the N bounds. Local component derivatives use
delta g^{-1}=-g^{-1}delta g g^{-1} and delta S=S tr(g^{-1}delta g)/2,
including the norm, at most two, of each symmetric coordinate injection.
Expand the finite tensor sums in (15)-(18) and apply triangle/product
rules and (20) to each map and its ordinary component derivatives.
This determines finite local norm, Lipschitz and N coefficients with
no J-dependent sum. Scalar maps add only the displayed monomials.

On ||h||<=1/4 and ||U||<=M choose the resulting C0,C1,C_h with

    ||F(U)||_rho<=C0+C1 N_rho(U),  ||A||_rho<=C_h.

C0 can bound F0; C1 can be the sum of m_P times the N coefficient of Q.
A permissible explicit metric-velocity bound is
C_h=3a(3+1/4)^2(1-1/4)^(-1/2)M, from
A=2a/S[g pi g-g tr(g pi)/2] and ||pi||=||p||. The enlarged total M
is safe for the coupled case although A itself has no scalar momentum.
If L0,L_P,L_Q and m_P,m_Q are the corresponding Lipschitz and norm
bounds, the choice

    C=1+sigma0 L0+sum_l(m_P_l L_Q_l+L_P_l m_Q_l)/e            (21)

gives ||F(U)-F(V)||_rho'<=C||U-V||_rho/(rho-rho') for
0<=rho'<rho<=sigma0 on a segment inside the ball. The second product
term is (P(U)-P(V)) D Q(V); it is controlled by Cauchy, not a chain rule.

Let real g0=I+h0,p0,phi0,w0 have finite norms at 2sigma0 and
||h0||_(2sigma0)<=1/8. Sample g0,p0,phi0,w0 exactly and initialize
q,r,z using the actual finite D. Sampling contracts the Wiener norm.
A valid uniform initial bound is

    M0=||h0||_(2sigma0)+||p0||_(2sigma0)
       +[||h0||_(2sigma0)+||B(g0)-I||_(2sigma0)]/(e sigma0)
       +||phi0||_(2sigma0)+||w0||_(2sigma0)
       +||phi0||_(2sigma0)/(e sigma0).                      (22)

Drop the final three terms for vacuum. Summing all derivative components
uses |k|_1, so there is no additional factor three. The B norm is bounded
by (20). Put M=2M0+2, recompute every local constant on this ball, set
v=C1+1, and take

    T0=min{(M-M0)/[2(C0+1)],1/[16(C_h+1)],sigma0/(4v)}.       (23)

Along rho(t)=sigma0-vt, upper Dini differentiation of the finite Fourier
absolute values gives d||U||_rho(t)/dt<=C0+(C1-v)N(U)<=C0.
Separately d||h||_rho(t)/dt<=C_h. Through T0 these give ||U||<M,
||h||<=3/16<1/4 and rho(t)>=3sigma0/4. The strict bootstrap margins
close by continuity. Realness is preserved and every metric stays positive.
Finite-dimensional ODE continuation yields existence through T0 on every
grid. No energy coercivity or strong-hyperbolicity assertion is used.

## Continuum construction and analytic uniqueness

Embed each finite solution by its trigonometric interpolant. The stronger
radius bound gives uniformly small Fourier tails in every rho<3sigma0/4.
Equation (18) and one radius reserve give uniform time derivative bounds
there. Finite-mode Arzela-Ascoli and a diagonal subsequence thus give a
limit in C([0,T0],A_rho), with the stronger bound retained by Fatou.

Products, inverse and square-root series converge in smaller Wiener
algebras. Sampling an analytic local map and interpolating introduces
only an exponentially bounded Fourier tail. The same is true with a
derivative after another positive radius reserve. For centered D,
fixed-mode multipliers converge to ik and the uniform analytic tails
control the remainder. Thus each term of the integral equation passes
to the continuum. Initial consistent data converge, and the time
identities in (16) give q=partial g,r=partial B,z=partial phi in the
limit. Its g,p,phi,w solve the continuum Hamiltonian equations.

Uniqueness and the quantitative rate need a derivative-loss argument.
Put rho1=sigma0/2, rho0=sigma0/4, d=sigma0/4 and shorten to

    T=min{T0,d/(2eC)}.                                      (24)

Linearizing the difference of two bounded trajectories along their
metric-safe convex segment gives a time-dependent operator with scale
bound C/(rho-rho'). Iterate its Volterra equation m times and allocate
d/m to each factor. The time-ordered simplex volume is t^m/m!, so
the operator contribution is at most (Cm/d)^m t^m/m!<=(eCt/d)^m.
The final remainder multiplies the common stronger-radius difference
bound and tends to zero on [0,T]. Summing initial and forcing terms gives

    ||w(t)||_rho0 <= [||w(0)||_rho1+T sup_(u<=T)||R(u)||_rho1]
                                      /[1-eCT/d].           (25)

Operator order is retained; commutation is not assumed. All intermediate
radius spaces use the same bounded trajectories. With zero initial
difference and forcing this proves uniqueness in the stated analytic
class, so the compactness limit is unique on the shortened interval.
This is not an estimate in a fixed Sobolev norm.

## Sampling error and actual total constraints

Let I_J denote actual sampling. It is an algebra homomorphism for grid
data, including analytic matrix maps where the series converge, and a
contraction in the representative Wiener norm. Trigonometric
interpolation is not being asserted to be an algebra homomorphism.

For spectral D and delta=rho-rho'>0, modes in Q_J have zero derivative
commutator. Outside Q_J, |k|_1>=J+1 and the total representative
displacement is at most 2|k|_1. Therefore

    sum_j ||(D_j I_J-I_J partial_j)f||_rho'
      <=4/(e delta) exp[-delta(J+1)/2] ||f||_rho.             (26)

Use 2u exp(-delta u)<=4/(e delta)exp(-delta u/2). This is a full
alias estimate, including arbitrarily high original modes and the
combined gradient without an extra dimension factor.

Take rho2=3sigma0/4 and delta=rho2-rho1=sigma0/4. In (18), local maps
commute with sampling exactly, leaving only P times derivative
commutators. Define

    K_R=4 sum_l m_P_l m_Q_l/(e delta),
    K_0=4[||h0||_rho2+||B(g0)-I||_rho2+||phi0||_rho2]/(e delta),

omitting phi0 in vacuum. Initial g,p,phi,w samples agree exactly; q,r,z
account for the K0 mismatch. The source and initial errors are bounded
by K_R and K_0 times exp[-sigma0(J+1)/8]. The sampled continuum
trajectory can have q!=D_J g and similarly for r,z; (16) is defined on
the whole analytic ball, so comparison there is legitimate. Equation
(25) proves

    ||U_J(t)-I_J U(t)||_rho0
       <=2(K_0+T K_R)exp[-sigma0(J+1)/8].                   (27)

Interpolant convergence adds its controlled sampling tail.

The actual finite densities, rather than the alternative unit-lapse
energy density, are

    C_J=T-K B^ij[D_k Gamma^k_ij-D_j Gamma^k_ik
                      +Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik]+M,
    J_J,k=pi^ij q_k,ij-2D_j(g_ik pi^ij)+w z_k.              (28)

The second formula is exact finite summation by parts in G. Each has
at most one D acting on a local analytic map of augmented U. Its scale
Lipschitz bound from rho0 to sigma0/8 and the separate sampling estimate
from the available stronger continuum radius preserve the rate in (27).
All constants follow the same finite majorant procedure.

From the FULL continuum algebra (12), for arbitrary independent analytic
smearings, {G[X],C[1]}=0 and {C[N],C[1]}=-G[s g^{-1}dN]. Hence

    Jdot_i=0, Cdot=partial_j(s g^ij J_i).                    (29)

Analytic smearings separate the densities. Initially zero total
continuum constraints remain zero, so (28) has the stated small finite
constraint errors. These allow nonzero initial sampling defects and
later Fourier growth; no exact finite constraint ideal is asserted.

## The centered local continuation

Define a new Hamiltonian by replacing EVERY D in (1)-(2) with
D_epsilon,j f(x)=[f(x+epsilon e_j)-f(x-epsilon e_j)]/(2epsilon).
This real skew operator has symbol i sin(epsilon k_j)/epsilon and obeys
the upper bound used in (19). The algebraic maps, initial estimates,
majorant algorithm, bootstrap and Volterra constants therefore remain
valid. No lower symbol bound or removal of ultraviolet modes enters.

The literal scalar density uses a graph ball of radius two. But (15)
is a sum of densities supported on the center and its six nearest
neighbors, of radius one and diameter two. Its canonical equations have
radius at most two; the momentum density has radius one. Scalar terms
add only nearest-neighbor phi values to the density. Inverse and
determinant operations act pointwise. These are stencil distances,
multiplied by epsilon for physical lengths. The unit-lapse rewrite is
not a claim of exact finite closure with arbitrary lapse.

For every original continuum mode k, including all aliases,
sin(epsilon wrap(k)_j)=sin(epsilon k_j). Thus the complete derivative
sampling commutator has multiplier i[sin(epsilon k_j)/epsilon-k_j]
before alias summation. The global real inequality |sin u-u|<=|u|^3/6,
|wrap(k)|_1<=|k|_1, and sum_j|k_j|^3<=|k|_1^3 give

    sum_j ||(D_epsilon,j I_J-I_J partial_j)f||_rho'
       <=epsilon^2 L(delta)||f||_rho,
    L(delta)=(1/6)[3/(e delta)]^3.                           (30)

A separate alias term is unnecessary in this commutator because its
periodic symbol included every alias. The interpolant comparison still
has its usual tail. Replace K_R,K_0 in (27) by

    K_R^loc=L(delta)sum_l m_P_l m_Q_l,
    K_0^loc=L(delta)[||h0||_rho2+||B(g0)-I||_rho2+||phi0||_rho2],

and replace the exponential factor by epsilon^2. The same comparison
and density argument proves the centered result, with all canonical
modes retained. Its high-frequency behavior is outside any claimed
generic smooth-data stability or mode-purity conclusion.

## Explicit compatible massless-scalar initial data

It remains to show that the compatible analytic-data hypothesis is
nonempty with actual inhomogeneous matter. Take a real nonconstant
trigonometric polynomial f, amplitude b, and constant H, and put

    phi0=b f, w0=0, g0=psi^4 I,
    pi0^ij=-(2H/a)psi^2 delta^ij, mean psi=1.                (31)

The gravity momentum terms are respectively
-(24H/a)psi^5 partial_k psi and +(24H/a)psi^5 partial_k psi,
and the matter term vanishes. Direct conformal Christoffels give
R=-8psi^{-5}Delta psi: the squared-gradient terms cancel. The kinetic
density is -(6H^2/a)psi^6 and the matter density is
(aK b^2/2)psi^2 q, where q=sum_i(partial_i f)^2. Thus C_tot=0 is exactly

    Delta psi+lambda q psi-c_H psi^5=0,
    lambda=a b^2/16, c_H=3H^2/(4aK).                         (32)

With psi=1+u and mean u=0 define

    c(u)=mean[q(1+u)]/mean[(1+u)^5],
    T(u)=-lambda Delta_0^{-1}[q(1+u)-c(u)(1+u)^5],
    H^2=(a^2 K b^2/12)c(u).                                 (33)

Delta_0^{-1} has multiplier -1/|k|_2^2 off zero and zero at zero,
so its mean-zero Wiener norm is at most one. The input in brackets
is identically mean zero; no zero-mode equation is discarded.

All following norms are at rho=2sigma0. Set B0=||q||_rho,
r=1/128, R=1+r, d=2-R^5>0 and

    A0=R+R^6/d, L0=1+6R^5/d+5R^10/d^2.                     (34)

On the complex ball ||u||<=r the denominator in c differs from one
by at most R^5-1, hence has modulus at least d. Product and quotient
bounds give norm at most B0 A0 and Lipschitz constant at most B0 L0
for the bracket in (33). Explicitly, the numerator variation contributes
B0 R^5/d, the fifth-power variation 5B0 R^5/d, and denominator variation
5B0 R^10/d^2, in addition to B0 from q(1+u).

Choose b!=0 satisfying

    lambda B0<=min{r/(2A0),1/(2L0)}.                         (35)

The map sends the radius-r ball into radius r/2 and has contraction
factor at most 1/2. Starting u_0=0, u_(m+1)=T(u_m) converges in A_rho
with explicit tail ||u-u_m||<=2 lambda B0 A0 2^{-m}. Zero mean and
reality are preserved. The limit has psi>=1-r>0. Since f is nonconstant,
q is nonnegative and not identically zero on the real torus, so c(u)>0
and H^2>0. Either sign of H is an initial expansion branch, not a
selected cosmological parameter. All four continuum constraints hold.

The actual matrix norm satisfies
||g0-I||_rho<=3[(129/128)^4-1]=25462275/268435456<1/8, and
||p0||_rho<=6|H|R^2/a. Thus these data meet (22)'s hypotheses.
For f=cos x_1, the first iterate is -(lambda/8)cos2x_1 and
H^2=a^2 K b^2/24+O(b^4), providing direct sign/normalization controls.
For b=0 the construction extends to psi=1,H=0; the nonconstant-matter
claim is for b!=0. The evolution afterwards is the full coupled system,
not a projection that keeps the initial conformal ansatz fixed.

## A supplied scalar clock gauge

This fourth part keeps the same gravity density C_g and canonical metric
pairing, but changes the evolution Hamiltonian. Supply a real positive,
time-independent analytic density w0(x), with analytic reciprocal eta=1/w0.
The scalar is fixed to phi=t, so its spatial gradient vanishes. On the full
six-pair metric carrier define, for either derivative,

    N=S/w0,
    H_clock=mean[(S/w0) C_g+w0/2]=mean(N C),
    C=C_g+w0^2/(2S),
    J_i=pi^jk D_i g_jk-2D_j(g_ik pi^jk).                    (36)

The fixed w0 is an input function, not a new canonical pair. The ordinary
canonical derivative varies N with g. With delta w0=0 it is exactly

    delta H_clock=mean[N delta C+C delta N],
    delta N=(N/2)tr(g^-1 delta g).                          (37)

The term C delta N is retained at every finite residual. Relative to the
full scalar equations varied at an externally fixed lapse, it contributes
-C N_g to pdot and nothing to gdot. An off-diagonal independent metric
variation changes both matrix entries, just as in (1).

For comparison only, on the open pointwise domain -2S C_g>0 put
W=sqrt(-2S C_g) and H_red=-mean W. Direct variation gives

    delta H_clock-delta H_red
       =mean[(1/w0-1/W) delta(S C_g)].                      (38)

On the identically constrained surface C=0, W=w0, so the functional
gradients agree in every direction. Their values differ: H_clock=0 there
and H_red=-mean w0. Away from that surface they need not agree; spatial
derivatives of the coefficient in (38) enter the functional gradient.
The finite law remains (36), not square-root evolution or a projection
onto an exactly invariant finite constraint surface.

### Continuum propagation and a positive constraint energy

Use continuum derivatives in this subsection. Adding w0^2/(2S) to C_g
does not change its CC bracket: its kinetic/potential cross terms carry
the symmetric undifferentiated test product fl and cancel. For a fixed
test f, metric variation of N in the complete bracket gives

    {C[f],N}=f zeta, zeta=a tr(g pi)/(2w0),
    Sdot/S=-zeta,
    Cdot=s g^ij J_i partial_j N
              +partial_j(s N g^ij J_i)+zeta C.             (39)

Indeed the metric velocity generated by C[f] is
2af/S[g pi g-g tr(g pi)/2]; its g-inverse trace is
-af tr(g pi)/S. Negating its contraction with N_g gives the first
identity. Applying the full CC algebra (12) to mean(N C), including
this extra bracket on N, and integrating the derivative of f yields
the last identity with the signs displayed.

The fixed density must also be treated correctly in the spatial bracket.
G contains only metric momentum and does not transform w0. Under its
metric Lie variation delta_X S=div(S X). The missing density variation
that a dynamical w would have had is div(w0 X). Therefore, for an external l,

    {G[X],C[l]}=C[X.grad l]+mean[l(w0/S)div(w0 X)].

Also delta_X N=N(X.grad log S+div X). The bracket on N in H_clock then
adds -mean(C delta_X N), giving

    {G[X],H_clock}
       =mean[C(X.grad N-delta_X N)]+mean div(w0 X)
       =-mean[(S C/w0^2)div(w0 X)],
    Jdot_i=w0 partial_i(S C/w0^2).                         (40)

The mean divergence vanishes on the torus. Thus neither a frozen scalar
function transformation for w0 nor an unvaried lapse gives the right
momentum equation when w0 is nonconstant.

Set u=S C/w0^2 and A_clock^ij=N^2 g^ij. Combining (39)-(40), using the
continuum product rule and time independence of w0, yields

    udot=(s/w0)partial_j(A_clock^ij J_i),
    Jdot_i=w0 partial_i u.                                 (41)

For example, (S C)dot=s S[g^ij J_i partial_j N+
partial_j(N g^ij J_i)]=s w0 partial_j(N^2 g^ij J_i).
The real periodic quadratic functional

    F=(1/2)mean[w0 u^2+(s/w0)J_i A_clock^ij J_j],
    Fdot=(s/2)mean[w0^-1 J_i (A_clock^ij)dot J_j]            (42)

is positive for positive metric and the supplied a,K,w0. To see the
second identity, the two cross terms are
s mean[u partial_j(A_clock^ij J_i)+J_i A_clock^ij partial_j u]
and cancel by integration by parts. The w0 factors cancel before this
integration; no derivative of w0 is omitted. On a compact smooth
positive-metric interval, k(t)=sup_x||A_clock^(-1/2) Adot_clock
A_clock^(-1/2)|| is bounded. Hence |Fdot|<=k(t)F. Zero initial C,J
therefore remain zero throughout such an interval by Gronwall, including
all of the analytic interval T1 constructed below. No extra
constraint-only shortening of that interval is required.

The conserved mean(S C/w0)=H_clock follows from (41) and is an
indefinite Hamiltonian, not the positive functional F. Equations
(39)-(42) are continuum identities; they are not discrete product rules.
On the zero-constraint continuum solution, (37) agrees with the full
massless-scalar equations at N=S/w0. Those scalar equations give
phidot=Nw0/S=1 and wdot=s partial_i(N B^ij partial_j phi)=0.
From phi(0)=0 they realize phi=t,w=w0 and zero scalar spatial momentum.
This is an internal coordinate in the supplied model, with a supplied
positive branch, not an identification with a physical Record clock.

### Literal finite variation and analytic approximation

Let Z^ij=(det g)eta g^ij and
T_c=a eta[tr(g pi g pi)-tr(g pi)^2/2]. For this subsection use the
auxiliary variables q_l,A=D_l g_A and r_l,ij=D_l Z^ij. With Gamma(g,q), set

    V_c=K[r_k,ij Gamma^k_ij-r_j,ij Gamma^k_ik]
          -K Z^ij[Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik],
    H_clock=mean[T_c+V_c(g,eta,Dg,DZ)+w0/2].                (43)

The second identity is exact skew summation by parts in the literal
curvature of (36). DZ is the actual grid derivative, never replaced by
Z_g Dg+Z_eta Deta. For six-coordinate local derivatives at fixed eta,q,r,
put A_A=(T_c)_pA. Full canonical variation is

    gdot_A=A_A,
    pdot_A=-(T_c)_gA-(V_c)_gA+sum_l D_l(V_c)_q_l,A
                      +sum_l,ij Z^ij_gA D_l(V_c)_r_l,ij,
    qdot_l,A=D_l A_A,
    rdot_l,ij=D_l(sum_A Z^ij_gA A_A), etadot=0.             (44)

In the r term, varying D(Z_g delta g) and taking its skew adjoint leaves
Z_g outside D in pdot. This includes the full metric-dependent lapse
variation (37). Time differentiation proves the exact invariants
q-Dg=0 and r-DZ=0 from consistent data. These are analysis variables,
not extra physical pairs. Every equation is F0(U)+sum_l P_l(U)D_j Q_l(U)
for U=(h,p,q,r,eta), with local analytic maps on ||h||<1 and bounded eta.

For centered D, (43)'s density has radius one and diameter two; its
canonical equations have radius at most two, and literal C,J have
radii two and one. These are stencil distances multiplied by epsilon.
For spectral D the line support remains. Both remain the collocated
changed law described after (2), with all canonical modes retained.

Here are the new quantitative analytic hypotheses and constants. Assume
real ||h0||_(2sigma0)<=1/8, finite norms of p0,w0,eta at 2sigma0, and
w0>=w_min>0 on the real torus. The analytic reciprocal is an explicit
hypothesis; real positivity alone is not substituted for that strip
bound. Sample w0 and eta exactly, so their finite values are reciprocal
pointwise. With all component norms summed as above, take

    M0=||h0||_(2sigma0)+||p0||_(2sigma0)+||eta||_(2sigma0)
          +[||h0||_(2sigma0)+||Z(g0,eta)||_(2sigma0)]/(e sigma0),
    M=2M0+2.                                              (45)

On ||h||<=1/4, ||U||<=M, apply the finite product and convergent inverse
series majorants of (20)-(21) to the actual T_c,Z,V_c and all their
coordinate derivatives in (44). This constructs new finite constants
C0,C1,C_vel,C_scale satisfying ||F(U)||_rho<=C0+C1 N_rho(U),
||A(U)||_rho<=C_vel, and the scale Lipschitz bound
C_scale||U-V||_rho/(rho-rho'). The eta dependence is polynomial and
etadot=0. These constants are recomputed for this law and M, rather
than identified with the old unit-lapse constants. Both derivatives
satisfy |D_j(k)|<=|k_j|; the wrapped product seminorm inequality (19),
not a product-rule equality, supplies the estimates.

With v=C1+1 set

    T0=min{(M-M0)/(2(C0+1)),1/(16(C_vel+1)),sigma0/(4v)},
    T1=min{T0,sigma0/(8e C_scale)}.                         (46)

Increase C_scale to a positive number if necessary. The same Dini
estimate as (23), at rho(t)=sigma0-vt, gives ||U||<M,
||h||<=3/16<1/4 and rho>=3sigma0/4 up to T0. It applies directly
to the actual finite ODE, and positive metric and reality persist.
Fixed w0 cannot cross zero. The mode compactness and radius-reserved
product limit proved above produce a continuum solution of (44);
(24)-(25)'s ordered Volterra argument gives uniqueness and comparison
on T1. Their only required form is the now explicit first-derivative
system and its recomputed scale bounds. Equation (42) propagates the
continuum constraints on all of T1, without a smooth-data metric
existence assertion or an added constraint-only time restriction.

For completeness let delta=sigma0/4 and let m_P_l,m_Q_l be the
majorants for the maps in (44) at 3sigma0/4. Define for spectral D
K_R=4 sum_l m_P_l m_Q_l/(e delta) and
K_0=4[||h0||_(3sigma0/4)+||Z(g0,eta)||_(3sigma0/4)]/(e delta).
For centered D replace 4/(e delta) in both constants by L(delta)
from (30). Then, with r_n=exp[-sigma0(J+1)/8] or epsilon^2 respectively,

    ||U_n(t)-I_n U(t)||_(sigma0/4)<=2(K_0+T1 K_R)r_n,
    ||C_n(t)||_(sigma0/8)+||J_n(t)||_(sigma0/8)<=K_diag r_n

for continuum-compatible data. The sampled eta component has zero
initial and evolution discrepancy. All local maps commute with sampling;
(26) and (30) bound every alias in the only remaining derivative
commutators. The actual finite densities in (36) contain at most one D
of a local map of U. Their scale Lipschitz bound across the remaining
radius reserve and the same commutator give the second estimate with
finite n-independent K_diag. Interpolant comparison adds the analytic
sampling tail. This does not claim exact finite constraint preservation,
finite first-class closure, or uniform control as w_min tends to zero.

### Compatible nonconstant and homogeneous data

Take lambda!=0 and a real analytic symmetric trace-free tensor A(x)
with partial_j A^ij=0 and summed matrix norm
||A||_(2sigma0)<=|lambda|/4. Define

    g0=I, pi0=lambda I+A(x), phi0=0,
    w0=sqrt(3a lambda^2-2a tr(A^2))>0.                      (47)

The analytic norm of 2tr(A^2)/(3lambda^2) is at most 1/24. Binomial
series therefore give ||w0||_(2sigma0)<=sqrt(3a)|lambda|(1-1/24)^(-1/2)
and ||eta||_(2sigma0)<=[sqrt(3a)|lambda|]^-1(1-1/24)^(-1/2), while
w_min>=sqrt(3a)|lambda|sqrt(23/24). Flat curvature, trace-freeness and
divergence-freeness give exactly
C=a[tr(A^2)-3lambda^2/2]+w0^2/2=0 and J_i=-2partial_j A^ij=0.
Thus (45)'s hypotheses and all continuum constraints are satisfied.

A concrete nonconstant family is A=b cos(x3)diag(1,-1,0) with
0<|b|exp(2sigma0)<=|lambda|/8. Its w0^2=3a lambda^2-4ab^2 cos^2(x3)
is nonconstant. Every finite sample for either derivative also satisfies
C_n(0)=J_n(0)=0 exactly: the curvature is flat, the scalar identity is
pointwise, and each nonconstant diagonal momentum is independent of its
own differentiation coordinate. This includes small-grid aliases; it
says nothing about exact preservation after time zero.

For b=0, w0=sqrt(3a)|lambda| is constant and direct substitution gives

    g(t)=exp[-a lambda t/w0]I,
    pi(t)=lambda exp[a lambda t/w0]I,
    N(t)=exp[-3a lambda t/(2w0)]/w0, phi=t, w=w0.            (48)

All spatial derivatives vanish, so (48) solves the actual finite equations
as well as the continuum equations. It checks normalization and signs;
it does not replace the inhomogeneous analytic proof. The sign of lambda
and the positive choice of w0 are supplied branch choices. The fixed
clock density, continuous scalar carrier and physical Record meaning
have not been selected by the framework axioms or registered primitives.

## Reproducible controls and their role

The [primary runner](../scripts/nonlinear_canonical_gravity_analytic_approximation_2026_09_30.py)
is a source-bound author implementation. Its exact sparse Fourier
directional-differentiation machinery is reused from the development
calculation and is not labeled independent. It forms the literal
Christoffel polynomial and full canonical variations, retaining generated
high modes and all symmetric tensor entries. Exact sample residuals test
the jets; the continuum and tree proofs above supply their universal scope.

The finite Hamiltonian variation controls compare derivatives of the
original energy with the skew-adjoint augmented variation, including the
scalar metric stress. The clock group compares the literal (36) against
(43)-(44) with nonconstant w0, full symmetric metric variations and all
six canonical pairs. It tests the actual DZ placement, the adjoint term,
and the nonconstant compatible data. This group adapts the source-bound
development control and is author reuse, not an independent implementation
or a clock-gauge PDE trajectory test. Analytic initial-data smallness is checked by exact
rational bounds where available. Floating conformal solves and actual
coupled scalar trajectories report literal finite constraints and numerical
errors; they are neither interval-certified continuum solves nor proofs
of a useful numerical T. The primary also requires the finest sampled trajectory error to be below
one quarter of the coarsest for each derivative. That broad diagnostic
rejects nonconvergent implementations; it proves neither the asserted rate
nor the majorant time. A separate matrix-versus-neighbor action check and
single-mode symbol check test the centered derivative normalization on grids
with one, three and seven sites. High-frequency and product-rule controls exercise
the distinctions used in the proof. Meaningful implementation mutations
and actual execution records belong with the source-bound cache and review
record; a passing terminal alone is not the mathematical argument.

The [runner cache](../logs/runner-cache/nonlinear_canonical_gravity_analytic_approximation_2026_09_30.txt)
is generated through the repository execution envelope from these exact
sources. No campaign report, native model, rotor process or outside
numerical target is a runtime scientific input. The theorem's constants
are construction bounds, not fitted to those diagnostics.

## Inputs, relation to existing work and limits

The mathematical inputs are the period-2pi torus and refinement, a real
continuous canonical tensor carrier and optional canonical scalar, the
specific functions (1)-(2), a,K and m where allowed, the derivative choice,
unit lapse or the explicit scalar-clock Hamiltonian (36), zero shift,
and analytic preparation near I. The clock branch additionally supplies
positive w0, its analytic reciprocal, orientation and off-constraint law.
The proof determines consequences of these choices. The scalar gradient
normalization s=aK is supplied for the common algebra. There are no
observed comparison values or fitted selectors in the theorem.

The continuum constraint and conformal methods are standard mathematical
methods; no historical novelty is claimed. Existing repository static
conformal, tensor-transfer and improved-stencil results have their own
carrier and evaluation scopes. Here one explicit nonlinear canonical
family connects full finite coefficient transfer to actual analytic-time
evolution, a local second-order continuation and a supplied internal scalar
clock with positive continuum constraint energy. Current-main/open-prior
comparisons and exact source provenance are recorded in the preparation
pack, not used as unexplained mathematical lemmas in this note.

The conclusions do not assert exact finite full-zone first-class closure,
an invariant strict band, Sobolev or long-time stability, a unique
low-energy gravitational mode content, derivation of a native M2 carrier,
the original walker/record matter action, a physical record clock, or a
framework TOE. The theorem applies precisely to the supplied family and analytic class
stated above. The explicit 7/4 example records one finite evaluation.

## Review record

This note composes the source-contained argument. Development-stage focused
checks covered precursor proofs and selected controls, with exact identities
retained in the preparation record. Independent review of this composition
requires a separate reviewer of its complete frozen source and evidence.
Formal audit remains unset.

Before landing, run the source-bound primary and meaningful mutations,
check its declared input closure, complete focused vocabulary/diff checks,
and perform the coordinated current-main combined validation. The original addition of this note changes citation-graph topology;
its generated acknowledgment remains part of the unit. This clock extension
adds no separate scientific node or premise link; actual graph/source
identity checks must confirm that boundary before any authorized landing. No helper-runner registry amendment is planned. Integration and audit remain separate requirements.
