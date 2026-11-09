# Exact SU(2) two-region source and boundary response

**Date:** 2026-11-08
**Type:** bounded_theorem
**Primary runner:** `scripts/frontier_su2_two_region_boundary_response.py`

**Claim:** for the supplied finite-volume
Wilson measure and normalized S4-prime soft kernel, the formulas below give
the complete two-region source response and finite exterior changes, including
the shared-link covariance for two adjacent plaquettes. They are finite-model
identities and explicit sufficient estimates, not a continuum mass-gap proof.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Finite-model identities and a sufficient small-parameter estimate under stated model premises."
target_claim_id: null
target_blocker_text: "Exact two-block boundary response with all source terms and conditional covariance retained."
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "Estimate the actual hidden-posterior connected insertions at a fixed positive physical scale."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Provenance and supplied model

The normalized kernel, disjoint-loop transport, total covariance and rectangular
boundary-response machinery were used in the historical Yang–Mills working
notes `MASS_GAP_CONSTRUCTION_ASTRA.md` and `MASS_GAP_LOCAL_BLOCK_ASTRA.md`
at commit `89faef229ff6e6bde42baad15ed8270c2f4087d8`. Their statements are
not premises of this note: the required model and arguments are given here.
The historical consumer is the fixed-physical-scale crossover question in
`MASS_GAP_CROSSOVER_REDUCTION.md` at that commit. Its mathematical status is
not decided here. The new application is the source-complete two-region
response and explicit tilted shared-edge contraction, including its exterior
response. Patrick Rebeschini and Ramon van Handel are credited below for the
comparison machinery; the finite-product proof used here is included.

Supplied inputs are the finite four-dimensional Wilson action, normalized Haar,
and the explicitly defined path-averaged soft kernel. They define a mathematical
model; no observation, fit, selected state, physical scale conversion or
ontology-to-action identification is supplied or derived. No repository theorem
is used as a proof premise. The elementary SU(2) and comparison steps are proved
in this note and its appendices.

The proof dependencies are: normalized Haar and the supplied finite Wilson
action; the specified continuous path means; elementary disintegration,
bounded differentiation, SU(2) moments and finite-product comparison, proved
below. No continuum theorem or framework identification is a premise. The
source and moment identities have no open mathematical sublemma; the later
physical-scale application requires additional estimates described in section 7.

## 1. Exact measure and the two-region convention

Use positively oriented independent links on a finite four-dimensional torus,
with sufficiently many sites that the plaquettes in question have distinct
edges. All Haar measures have mass one. Let

    q_beta(U) = exp[-beta sum_p (1-w(U_p))],
    w(A) = (1/2) Re tr A,            beta >= 0.

Fixed fine boundary values may instead be included in the plaquette products.
For the order-averaged path construction (historically called S4-prime), fix
odd L>=3. Take the fine torus (Z/NZ)^4 with N a multiple of L and N/L>=3.
Put h=(L-1)/2, coarse centres X in (LZ/NZ)^4, and the disjoint blocks
B(X)=X+{-h,...,h}^4, with coordinates read periodically. Each positive coarse
edge c=(X,Y), Y=X+L e_mu, has the mean

    M_c(U) = (4! L^4)^(-1) sum_(sigma,y in B(X)) T_y^sigma(U).

Here T runs from the centre of X to y in coordinate order sigma, takes L
straight steps toward Y, then follows the reverse of the translated coordinate-order path from the
centre of Y to y+L e_mu. This defines the path word, including orientation and
any repeated fine edges, without an external geometry premise. As a real
quaternion M_c has norm r_c<=1. For finite lambda>=0,

    k_c(v|U) = exp[lambda <v,M_c(U)>]/Z(lambda r_c(U)),
    <v,M> = w(v^dagger M),
    Z(z) = integral_SU(2) exp[z w(v)]dv
         = sum_(n>=0) z^(2n)/(4^n n!(n+1)!).                 (1)

For completeness, Haar SU(2) is uniform S^3, whose first coordinate has
density (2/pi)sqrt(1-x^2) on [-1,1]. The beta integral gives
E[x^(2n)]=(2n)!/(4^n n!(n+1)!), and odd moments vanish. Integrating the
uniformly convergent exponential series proves (1).

Thus integral k_c dv=1, including r_c=0 and lambda=0. All soft-link
normalizers in (1) are functions of the fine field U. The joint law is
proportional to q_beta(U) product_c k_c(V_c|U)dU dV.

Let A,B be disjoint sets of coarse random edges, I=A union B and O=I^c;
they may share vertices and fine path footprints. Condition on exterior
V_O=xi. This defines a density at every xi by strict positivity. A union of
two adjacent plaquettes has seven edges: assign the shared edge once to I.
The plaquette observables may both use it; their independence is never assumed.

For bounded real fine observables F,G, not necessarily disjoint or invariant,
and real sources s,t, set

    W_xi(x;s,t) = integral q_beta exp[sF+tG] K_O(xi|U)K_I(x|U)dU,
    Q_xi(s,t) = integral q_beta exp[sF+tG] K_O(xi|U)dU,
    p_xi(x;s,t) = W_xi(x;s,t)/Q_xi(s,t).                    (2)

K denotes the indicated product of kernels. Integrating x gives Q, exactly.
Define two fine posteriors

    rho_xi(dU) = Q_xi^(-1) q_beta exp[sF+tG] K_O dU,
    pi_(xi,x)(dU) = W_xi^(-1) q_beta exp[sF+tG] K_OK_I dU.  (3)

The fundamental disintegration is

    rho_xi(dU) K_I(x|U)dx = p_xi(x)dx pi_(xi,x)(dU).       (4)

All products and integrations include their overlapping fine footprints.

## 2. Full two-source coefficient and reconstruction

Use m_F(x)=E_pi F, c_FG(x)=Cov_pi(F,G), M_F=E_rho F,
C_FG=Cov_rho(F,G). Differentiation of (2) gives, at any real s,t,

    partial_s log W = m_F,       partial_s partial_t log W = c_FG,
    partial_s log Q = M_F,       partial_s partial_t log Q = C_FG,
    partial_s log p = m_F-M_F,
    partial_s partial_t log p = c_FG-C_FG.                (5)

In particular the complete degree-two jet of log W at zero is

    log W(0,0)+s m_F+t m_G
        +(s^2/2)c_FF+st c_FG+(t^2/2)c_GG,                 (6)

with the coefficients on the right evaluated at zero. The jet of log p
subtracts the *entire* jet of log Q. The term log Q is constant in x but
depends on sources and on xi. It carries C_FG; it must be retained in the
generating functional.

For the density, rather than its logarithm,

    partial_s partial_t p
      = p[(m_F-M_F)(m_G-M_G)+c_FG-C_FG].                  (7)

Integrating (7), or taking the conditional expectation of FG in (4), proves

    Cov_rho(F,G) = E_p Cov_pi(F,G)+Cov_p(m_F,m_G).         (8)

For a fixed coarse observable a(x), source differentiation includes the
response of the conditional mean itself:

    partial_t m_F = c_FG,
    partial_s partial_t E_p a
       = Cov_p(a,c_FG)+kappa_3,p(a,m_F,m_G).              (9)

Here kappa_n is the joint cumulant in the indicated normalized law. To recover
the unconditioned fine source covariance, also integrate the exterior with
density n_O(xi)=Q_xi/Z_beta(s,t), where Z_beta(s,t)=integral q_beta exp[sF+tG]dU:

    Cov_(mu_beta;s,t)(F,G)
      = E_(n_O)[E_p c_FG+Cov_p(m_F,m_G)]
          +Cov_(n_O)(M_F,M_G).                           (10)

This last exterior term distinguishes a fixed-boundary calculation from the
original Wilson covariance. At lambda=0, W=Q=Z_beta(s,t), p=1 and pi=rho is
the source-tilted Wilson law. Then the conditional-covariance term in (8)
carries all the fine covariance, while every source derivative of log p
vanishes. This is an exact normalization check.

## 3. Finite exterior changes and all source responses

Change one exterior edge j from xi_j to xi'_j and put

    H_j(U)=lambda <xi'_j-xi_j,M_j(U)>,       |H_j|<=2 lambda.

The Z(lambda r_j) factor cancels in the pointwise kernel *ratio*, giving
K_O(xi'|U)/K_O(xi|U)=exp H_j. It stays in both baseline posteriors (3).
Consequently the exact endpoint ratios are

    W_xi'/W_xi = E_pi exp H_j,
    Q_xi'/Q_xi = E_rho exp H_j,
    p_xi'/p_xi = (E_pi exp H_j)/(E_rho exp H_j).          (11)

Interpolate by multiplying the baseline fine weight by exp[u H_j], 0<=u<=1.
Write pi_u,rho_u,p_u for the resulting normalized laws. This is interpolation
of positive weights, not a path of boundary points inside SU(2). Then

    partial_u log p_u = E_pi_u H_j-E_rho_u H_j,
    partial_u c_FG = kappa_3,pi_u(F,G,H_j),
    partial_s partial_t partial_u log p_u
       = kappa_3,pi_u(F,G,H_j)-kappa_3,rho_u(F,G,H_j).    (12)

Integrate from 0 to 1 for exact finite differences. The complete remainder
after the first boundary derivative of c_FG is

    c_FG(1)-c_FG(0)
       = kappa_3,pi_0(F,G,H_j)
           +integral_0^1 (1-u)kappa_4,pi_u(F,G,H_j,H_j)du. (13)

For two distinct exterior changes with insertions H_j,H_k, multiply by
exp[uH_j+vH_k]. Their rectangular mixed response is

    Delta_j Delta_k c_FG
       = integral_[0,1]^2 kappa_4,pi_(u,v)(F,G,H_j,H_k)du dv. (14)

For the mixed source coefficient of log p, subtract the same expression in
rho. These are connected cumulants, not uncentered moments. Explicitly
kappa_4(X,Y,Z,T) is E[X°Y°Z°T°] minus the three covariance-pair products.

The response of the total-covariance identity is also exact. Put
h=E_pi H_j, d_F=Cov_pi(F,H_j), d_G=Cov_pi(G,H_j). Differentiating (8) yields

    kappa_3,rho(F,G,H_j)
      = E_p kappa_3,pi(F,G,H_j)+Cov_p(c_FG,h)
         +Cov_p(d_F,m_G)+Cov_p(m_F,d_G)
         +kappa_3,p(m_F,m_G,h).                          (15)

Thus boundary changes of conditional source means are retained. For four
arguments Y=(F,G,H_j,H_k), the full reconstruction is

    kappa_4,rho(Y) = sum_(P set partition of {1,2,3,4})
          kappa_(|P|),p( kappa_pi(Y_i:i in D) : D in P). (16)

A one-argument outer cumulant means expectation. Formula (16) contains one
conditional fourth-cumulant expectation, four triple/mean covariances, three
covariance/covariance terms, six conditional-covariance/mean/mean third
cumulants, and one fourth cumulant of means. To prove it, use (4) at fixed
parameters to expand log E_p exp[log E_pi exp(sum z_i Y_i)]. Collect the term
with each of the four labelled variables once. This proves (16) without
treating parameter-dependent means as constants.

## 4. Explicit adjacent-plaquette contraction

Let two plaquettes share exactly one random edge V, in opposite orientations,
and write their Wilson observables, after cyclically choosing starting points,
as W_P=w(VA), W_Q=w(V^dagger B). A and B are the ordered products of the
three remaining edges of each face. Those six random edges are all distinct.
Conditional on fine U they are independent, even if their fine path footprints
overlap. Set

    b(z)=Z'(z)/Z(z),             a(z)=b(z)/z,    a(0)=1/4,
    f_lambda(r)=b(lambda r)/r,   f_lambda(0)=lambda/4,
    Abar=product_(three edges of P) f_lambda(r_c) M_c^(orientation),
    Bbar=product_(three edges of Q) f_lambda(r_c) M_c^(orientation).

A negative orientation means M_c^dagger, never M_c^(-1). Products retain
their order. Let M be the shared mean, r=|M|, z=lambda r. Define

    h_lambda(r)=[1-4a(z)-b(z)^2]/r^2,
    h_lambda(0)=-lambda^2/48.                             (17)

Then the two conditional means and the conditional covariance are exactly

    B_P(U)=f_lambda(r) w(M Abar),
    B_Q(U)=f_lambda(r) w(M^dagger Bbar),
    C_PQ(U)=a(z) w(Abar Bbar)
              +h_lambda(r) w(M Abar)w(M^dagger Bbar).    (18)

In particular

    E[W_P W_Q|U]=a(z) w(Abar Bbar)
       +[1-4a(z)]/r^2 w(M Abar)w(M^dagger Bbar).          (19)

The apparent quotients in (17)-(19) have their continuous values at r=0.
There the last term of (19) is zero, whereas its first term need not vanish
pointwise. The formula includes the singlet contraction across the shared
edge, in addition to the product of conditional means.

**Moment proof.** In real quaternion coordinates, put v=(v_0,...,v_3) and
m=M. Rotational symmetry on S^3 gives

    E[v v^T|M]=a(z) I_4+[1-4a(z)] m m^T/r^2.             (20)

Indeed, tangential differentiation of the radial partition Z(|lambda m|)
gives the transverse eigenvalue Z'(z)/(zZ(z)). Its trace is E|v|^2=1,
fixing the longitudinal eigenvalue. Differentiation is legitimate on the
compact sphere. Alternatively the series (1) proves
Z''+(3/z)Z'=Z and the same identity, with continuous values at zero.

The linear coefficient vectors of w(VA) and w(V^dagger B) are respectively
(A_0,-A_vec) and (B_0,B_vec). Their dot product is w(AB), and their dot
products with m are w(MA) and w(M^dagger B). Contracting (20), subtracting
the product of means, and integrating the six distinct links proves (18)-(19).
No commutativity of A,B,M was used.

**Different derivation and checks.** In the character/Fierz derivation, write
M=rW and rotate V=WY. The tilt of Y is central, so the traceless part of
E[y_vec y_vec^T] is zero and the adjoint moment is scalar. Let
q(z)=I_3(z)/I_1(z), q(0)=0. The spin-one character average is 3q; since
chi_1(Y)=4y_0^2-1, E[y_0^2]=(1+3q)/4 and E[y_i^2]=(1-q)/4.
The recurrence I_1-I_3=4I_2/z gives (1-q)/4=a(z), reproducing (20) and
(19). A full independent derivation is preserved in
Appendix A.
For fixed B=A^dagger, the covariance before averaging other edges becomes
a variance. Its eigenvalues are a(z)>0 transversely and
1-3a(z)-b(z)^2=Var(y_0)>0 longitudinally for finite z. At M=0 the fixed
test A=B=1 gives E[w(V)^2]=1/4, agreeing with Haar and retaining the term
missed by multiplying first moments. This is a one-link check, not an
assertion about the fully Haar-integrated plaquette pair.

**First nonzero conditional term.** The convergent local series gives
b(z)=z/4-z^3/96+O(z^5). If A_M,B_M denote the two ordered products of
three oriented fine means, then, uniformly in the fine configuration,

    C_PQ(U)=lambda^6/4^7 w(A_M B_M)+O(lambda^8),
    B_P(U)B_Q(U)=O(lambda^8).                            (21)

This is a pointwise conditional expansion. The exterior posterior itself
depends on lambda; its derivatives must also be kept when expanding a fully
integrated covariance. Equation (21) is not a claim that its Wilson average
has a nonzero coefficient for every beta or boundary.

## 5. Exact boundary response of the coupled plaquettes

With the seven-edge union included in I, integrate over the exterior-conditioned
fine law rho in (3). The actual coarse pair covariance is

    Cov_p(W_P,W_Q)=Cov_rho(B_P,B_Q)+E_rho C_PQ.           (22)

This also follows by inserting coarse sources uW_P+vW_Q in the *full* weight:
its mixed log-source coefficient is exactly (22). Thus (18) supplies the
conditional source term, not only an observable average. Coarse source insertions
break conditional link independence at nonzero u,v; (22) evaluates their
second derivative at u=v=0, where (18) applies.

Under the finite exterior interpolation exp[zeta H_j], B_P,B_Q,C_PQ have
no explicit zeta dependence. Hence

    partial_zeta Cov_(p_zeta)(W_P,W_Q)
       = kappa_3,rho_zeta(B_P,B_Q,H_j)
          +Cov_rho_zeta(C_PQ,H_j).                       (23)

Integrating zeta from 0 to 1 gives the exact endpoint response. With two
exterior changes H_j,H_k, the rectangular response is

    Delta_j Delta_k Cov_p(W_P,W_Q)
       = integral_[0,1]^2 [kappa_4,rho(B_P,B_Q,H_j,H_k)
                          +kappa_3,rho(C_PQ,H_j,H_k)]du dv. (24)

All rhos in this integral have the matching interpolated weights. Formula
(23) contains the response of the conditional covariance itself; it is
present even though the six unshared links are conditionally independent.
Fine source derivatives replace an H insertion by F or G. For example,
partial_s partial_t of (22) is kappa_4,rho(B_P,B_Q,F,G)
plus kappa_3,rho(C_PQ,F,G). This explicitly retains both kinds of source.

## 6. Differentiability and boundary-log estimate

For finite volume and bounded real source parameters all factors in (1)-(3)
are positive and bounded above and below on the compact product space.
Parameter derivatives insert bounded products of F,G,H. Dominated convergence
justifies every finite differentiation and interpolation integral above;
strictly positive denominators justify logarithms. The Taylor expansions are
uniform on the finite product and on fixed sufficiently small parameter disks.
They supply no cutoff-uniform Taylor remainder by themselves.

For distinct coarse coordinates i,j, fix all the others and change endpoints
v_i to v'_i and v_j to v'_j. Put A_i=lambda<v'_i-v_i,M_i> and
H_j=lambda<v'_j-v_j,M_j>. In the fully conditioned fine posterior, interpolate
both log weights. For the actual integrated weight W at zero fine sources,

    Delta_i Delta_j log W
        = integral_[0,1]^2 Cov_pi_(u,v)(A_i,H_j)du dv.     (25)

This formula is exact at arbitrary beta and lambda. The interior conditional
normalizer is independent of v_i and cancels from its mixed oscillation.
The analogous boundary response of the mixed fine-source coefficient is
the integral of kappa_4,pi(F,G,A_i,H_j), retaining the same posterior.

Precisely, gamma_i(dv_i|v_-i)=W(v)dv_i/integral W(z_i,v_-i)dz_i,
and C_ij is the supremum of TV(gamma_i(.|eta),gamma_i(.|xi)) over
environments eta,xi differing only at j. This is the full single-link
conditional, not a one-link marginal of an unconditioned block.

Since osc A_i, osc H_j<=4lambda, the elementary range covariance inequality
gives |Delta_i Delta_j log W|<=4lambda^2. For probabilities whose log density
ratio has oscillation D, TV<=tanh(D/4). To check the constant, let X=dnu/dmu
have minimum m and maximum M with M/m<=exp D and EX=1. The chord bound for
the convex function |X-1| gives TV<=(1-m)(M-1)/(M-m). Maximizing subject to
M/m<=exp D gives m=exp(-D/2), M=exp(D/2), and tanh(D/4).
Thus each single-coarse-link influence obeys

    C_ij <= tanh(lambda^2).                              (26)

The bound (26) has no distance factor. Section 7 gives the quantitative
spatial criterion in terms of the actual fine posterior.

## 7. A proved volume-uniform domain and the crossover consumer

This section proves a sufficient spatial bound with all soft normalizers.
Take zero fine sources for the quantitative estimates. Arbitrary bounded
sources remain in the identities above; an estimate at arbitrary source
strength would require their additional mixed-oscillation bounds.

Let S_c be the fine-edge footprint of M_c. For distinct fine edges e,f let
n^p_ef count their common plaquettes and n^s_ef the supports S_c containing
both. Put zero on the diagonal. For any subset of conditioned coarse links,
including the interpolations in (25), the fine posterior log density is

    beta sum_p w(U_p)
      +sum_(conditioned c) [lambda<q_c,M_c>-log Z(lambda r_c)],
    |q_c|<=1.                                             (27)

Unconditioned coarse links integrate to one, so their entire kernel factors
are absent, including their normalizers. Conditioned links retain both terms.
The matrix below overcounts by using all possible supports.

A plaquette contributes at most 4beta to a mixed fine-link rectangle.
The first soft term in (27) contributes at most 4lambda. For the second,
Haar symmetry gives

    1<=Z(lambda r)<=cosh(lambda r)<=exp(lambda^2/2).

The last inequality follows by integrating tanh z<=z. A rectangle of a
function taking values in [0,lambda^2/2] has magnitude at most lambda^2.
Thus the fine conditional TV influences have the symmetric majorant

    B_ef=beta n^p_ef+(lambda+lambda^2/4)n^s_ef.            (28)

This is a conservative estimate; its lambda^2/4 term explicitly accounts
for the U-dependent soft normalizer. Intermediate q_c remain in the unit
ball, so (28) holds uniformly throughout every endpoint interpolation.

On a torus with at least three L-blocks per direction, each S_c lies in its
two endpoint blocks and their shared crossings. Each block contains
4(L-1)L^3 internal edges, and their common face has L^3 crossings. Hence

    |S_c|<=s_L=(8L-7)L^3,
    sup_e #{c:e in S_c}<=8,
    sup_e sum_f B_ef<=q=18beta+8(s_L-1)(lambda+lambda^2/4). (29)

An internal fine edge can be used only by the eight coarse edges incident
to its block; a crossing edge only by its own coarse face. Each fine edge
has six plaquettes, each with three other edges. These observations prove
the counts in (29), without assuming all these uses actually occur. Other
finite geometries use their own incidence counts, not (29).

**Comparison proof.** For a finite product probability with influence
majorant B and row sum q<1, put D=(I-B)^(-1)=sum_(n>=0)B^n. Compare it
with a second law whose one-site kernels at identical environments differ
by at most b_e in TV. Couple random-scan single-site updates maximally.
Telescoping the conditioning coordinates bounds the mismatch probability
at an updated site e by sum_f B_ef p_f+b_e. With n sites the vector
recursion has matrix (1-1/n)I+B/n and forcing b/n. Its row norm is
at most 1-(1-q)/n<1, so its limiting upper bound is Db.
The marginals converge to their stationary laws: all conditional densities
are bounded below, and a prescribed complete sweep minorizes product Haar.
The oscillation inequality |f(x)-f(y)|<=sum_e delta_e f 1_(x_e!=y_e)
then proves |mu f-nu f|<=sum_e delta_e f (Db)_e.

Compare a law pi with its bounded tilt exp[tg]pi. The conditional log-ratio
oscillation is at most |t|delta_e g, so the TV lemma gives
b_e<=|t|delta_e g/4. Divide the comparison inequality by |t| and let t tend
to zero, justified by bounded differentiation. This proves

    |Cov_pi(f,g)| <= (1/4)sum_(e,f') delta_e f D_(e,f') delta_(f') g. (30)

This is the finite-product Dobrushin comparison argument, already used in
the historical slab calculation; it is standard machinery. Patrick Rebeschini and Ramon
van Handel's *Comparison Theorems for Gibbs Measures* (2014),
[arXiv:1308.4117](https://arxiv.org/abs/1308.4117), provides broader comparison results. The
bounded proof above is the tool used here, not an import of their stronger
block theorem.

For the insertions in (25), delta_e A_i<=4lambda 1_(e in S_i).
Using (30) and the TV lemma proves the actual coarse influence bound

    C_ij<=tanh[lambda^2 sum_(e in S_i,f in S_j) D_ef]
         <=lambda^2 sum_(e in S_i,f in S_j) D_ef,    i!=j. (31)

The identity term of D retains overlapping footprints; its higher powers
retain indirect interactions between separated footprints. Equation (30)
also bounds the conditional covariance Cov_pi(F,G) in (8) at zero sources,
with the actual oscillations of F and G.

For an explicit weighted version use shortest periodic l1 distance between
edge midpoints in fine-lattice units. Let x_c be a coarse-edge midpoint and
r=5L. The rectangular union of the two endpoint blocks gives
d(x_c,x_e)<=r for e in S_c. Each nonzero entry of B connects fine midpoints
at distance at most 2r (also true for plaquette interactions). For alpha>0
with q_alpha=exp(2r alpha)q<1, the triangle inequality and the Neumann series
give

    sup_e sum_f exp[alpha d(x_e,x_f)]D_ef<=1/(1-q_alpha).

Apply the triangle inequality once more and count at most eight supports
through any fine edge. From (31), including an overcount of the excluded
coarse diagonal, one obtains

    sup_i sum_(j!=i) exp[alpha d(x_i,x_j)] C_ij
      <= Q_alpha=8s_L lambda^2 exp(2r alpha)/(1-q_alpha). (32)

It follows that the explicit domain

    q+8s_L lambda^2<1                                   (33)

admits Q_alpha<1: choose any positive alpha<(2r)^(-1)
log[1/(q+8s_L lambda^2)] when the denominator is positive. If beta=lambda=0,
all responses vanish. For lambda=0 and beta>0 the coarse responses also
vanish exactly, whether or not the sufficient fine-posterior criterion holds.

For completeness (32) controls an actual two-region conditional with many
changed exterior links. Let J be any interior coarse edge set, including
the union of two regions, and H the exterior edges where two configurations
xi,eta differ. With D_J=(I-C_JJ)^(-1), the same comparison argument gives

    |E_(p_eta) f-E_(p_xi) f|
       <= sum_(i in J) delta_i f sum_(j in H)(D_J C_(J,H))_ij
       <= Q_alpha/(1-Q_alpha) sum_(i in supp f) delta_i f
                         exp[-alpha d(x_i,H)].           (34)

Here one may use the symmetric upper matrix on the right of (31) for C,
with its diagonal set to zero. For H empty the bound is zero. Positivity
defines every boundary conditional, and (34) holds for bounded measurable
f. Constants are independent of volume for fixed L,beta,lambda satisfying
(33); distances and rates are in lattice units.

**Next physical-scale obligation.** The sufficient domain (33) is an explicit
small-beta, small-lambda endpoint. The exact response formulas (11)-(25)
hold at every finite beta,lambda. The required next estimate is an
all-boundary, cutoff- and volume-uniform summable bound on their *actual
posterior* connected insertions along the Wilson weak-coupling trajectory,
after enough normalized blocking steps to reach a fixed positive physical
scale. The two-source part includes (12)-(16) and, for adjacent loops,
both terms in (23)-(24). Our endpoint criterion supplies no such trajectory
or multi-step estimate; the mass gap and the source/continuum bridge remain
open. The posterior-decay criterion is a sufficient route, potentially
stronger than the desired coarse contraction, so this reduction is not a
near-closure claim about crossover.

For multi-step use the exact original joint chain
q_beta(U_0) product_(h=0)^(k-1) K_h(U_(h+1)|U_h), with sources on U_0.
Conditioning on the last layer leaves the entire hidden chain as the
posterior. An endpoint change inserts the last-layer H_j; every earlier
kernel normalizer remains. Equations (5), (8), (11)-(16), and (25) apply
to that finite hidden product without further assumptions. Equations
(18)-(24) also apply to two plaquettes in the last layer, conditional on
the entire hidden chain and using its last-layer path means; rho then
integrates the whole hidden chain. Only last-layer coarse links are being
integrated independently in the moment calculation. Equations
(28)-(34) have only been proved for the one-step posterior (27); intermediate
blocked laws have not been identified with a new Wilson action.

## 8. Reproduction, review record and scope

Run `python3 scripts/frontier_su2_two_region_boundary_response.py` for exact
finite cumulant, spherical-moment and path-incidence controls. The runner tests
representative instances and low-order coefficients; it is not a computational
proof of all finite volumes, all odd L or the continuum statement. The general
proofs are sections 1–7, the character contraction in Appendix A, and the
semigroup/Poisson derivation in Appendix B. Its declared source input binds the
checks to this note. No numerical physical gap is computed.

This canonical source preserves the finite-model argument from the seven-file
proposal at `a50a62bf088b0e9fd2828e1c36f6237da71ccf99`, including the two
alternative proof arguments. The original `HANDOFF.md`, `PRIOR_WORK.json`,
`REVIEW_HISTORY.md` and `SOURCE_MANIFEST.json`, and the original checker
transcripts, remain historical recovery material at that immutable commit.
Their author-side conclusions grant no landing or audit status. The prior-work
inventory is a bounded search record, not a novelty or absence theorem.

The integration makes the supplied block geometry explicit and puts the proof
and supplemental controls in canonical source locations. It adopts no draft
ancestor theorem. The physical-scale obligation in section 7 remains open;
no numbered finite-model formula is promoted to a mass-gap conclusion.
All results concern the supplied Wilson action and normalized kernel. The
ontology-to-action map is not derived here. Review and runner checks do not
confer retained status; independent audit remains a separate process.

## Appendix A. Character contraction for the shared edge

This is a second derivation of section 4 with explicit oriented products.
Its equation numbers are local to this appendix.

### 1. Scope and exact formulas

Fix the fine field $U$ and real $\lambda\geq0$. The shared coarse link has normalized law

\[
 k_\lambda(V\mid M)\,dV
 =\frac{\exp[\lambda w(V^\dagger M)]}{Z(\lambda r)}\,dV,
 \qquad M=rW,\quad 0<r\leq1,\quad W\in SU(2),
\]

where $w(Q)=\tfrac12\operatorname{Re}\operatorname{tr}Q$, Haar measure has total mass one, and $Z(z)=2I_1(z)/z$. Every matrix to which $w$ is applied below is a real quaternion, so its trace is real. Initially also fix the six other links, and hence $A,B\in SU(2)$, with loops

\[
 P=w(VA),\qquad Q=w(V^\dagger B).
\]

Products within $A$ and $B$ retain their actual oriented order. Set

\[
 z=\lambda r,\quad b(z)=\frac{I_2(z)}{I_1(z)},\quad
 q(z)=\frac{I_3(z)}{I_1(z)},\quad t(z)=\frac{1-q(z)}4,
 \quad c=w(WA),\quad d=w(W^\dagger B).
\]

At $z=0$, the removable values are $b=q=0$ and $t=1/4$. Then

\[
 \boxed{\mathbb E_V[P]=bc,\qquad \mathbb E_V[Q]=bd,}
 \tag{1}
\]

\[
 \boxed{\mathbb E_V[PQ]=t\,w(AB)+qcd,}
 \tag{2}
\]

\[
 \boxed{\operatorname{Cov}_V(P,Q)
       =t\,w(AB)+(q-b^2)cd.}
 \tag{3}
\]

The subscript $V$ means that the other six links are held fixed. In particular, the two occurrences of the shared link have not been replaced by independent copies or by independent means.

The underlying second matrix moment is

\[
 \boxed{\mathbb E_V[V_{ij}(V^\dagger)_{kl}]
   =q\,W_{ij}(W^\dagger)_{kl}
    +\frac{1-q}{2}\delta_{il}\delta_{jk}.}
 \tag{4}
\]

This is a raw second moment; subtracting the product of matrix means replaces $q$ by $q-b^2$ in its first term.

### 2. Character and tensor derivation

Write $V=WX$. Haar invariance gives the central law

\[
 d\nu_z(X)=Z(z)^{-1}e^{z w(X)}dX.
\]

For the spin-$j$ character, put $n=2j+1\in\{1,2,\ldots\}$. The class coordinate $X\sim\operatorname{diag}(e^{i\theta},e^{-i\theta})$ has Haar class density $2\sin^2\theta/\pi$, and

\[
 \chi_j(\theta)=\frac{\sin(n\theta)}{\sin\theta}.
\]

Consequently,

\[
 \begin{aligned}
 \int e^{z w(X)}\chi_j(X)\,dX
 &=\frac2\pi\int_0^\pi e^{z\cos\theta}
                      \sin\theta\sin(n\theta)\,d\theta\\
 &=I_{n-1}(z)-I_{n+1}(z)
 =\frac{2n}{z}I_n(z).
 \end{aligned}
 \tag{5}
\]

The only special-function inputs here are the cosine integral for integer-order $I_n$ and its adjacent-order recurrence; both are recorded in [NIST DLMF 10.32.3](https://dlmf.nist.gov/10.32.E3) and [10.29.1](https://dlmf.nist.gov/10.29.E1). All values at zero follow by continuity of the integrals. Dividing (5) by its $j=0$ case yields

\[
 \mathbb E_{\nu_z}\chi_j=(2j+1)\frac{I_{2j+1}(z)}{I_1(z)}.
 \tag{6}
\]

The fundamental representation has scalar central average $bI$, since its normalized trace average is $I_2/I_1$. For the second moment use

\[
 \mathbb C^2\otimes\overline{\mathbb C^2}
   =\mathbf1\oplus\mathbf3.
\]

Under vectorization this is the decomposition of $2\times2$ matrices into scalar matrices and traceless matrices. $X\otimes\bar X$ acts as conjugation $T\mapsto XTX^\dagger$: it is the identity on the scalar part, while the traceless part is the irreducible spin-one representation. Centrality and Schur's lemma therefore give

\[
 \mathbb E_{\nu_z}[X\otimes\bar X]=P_0+qP_1,
 \qquad q=\frac{\mathbb E\chi_1}{3}=\frac{I_3}{I_1}.
 \tag{7}
\]

Here $P_0(T)=\tfrac12\operatorname{tr}(T)I$ and $P_1=I-P_0$. In indices this says

\[
 \mathbb E[X_{ij}(X^\dagger)_{kl}]
 =q\delta_{ij}\delta_{kl}
   +\frac{1-q}{2}\delta_{il}\delta_{jk}.
 \tag{8}
\]

Multiplication by $W$ and $W^\dagger$ gives (4). Contract (4) with $A_{ji}B_{lk}/4$. The first term gives $qcd$; the singlet contraction gives

\[
 \frac{1-q}{8}\operatorname{tr}(AB)
 =\frac{1-q}{4}w(AB).
\]

This proves (2), including the factor $1/4$ for normalized traces. Subtracting (1)'s product proves (3). No commutation of $A,B,W$ was used. In particular, $AB$, $WA$, and $W^\dagger B$ are the products forced by the specified opposite orientations.

### 3. Regular form at $M=0$, and small coupling with remainders fixed

For $r>0$, equations (2)–(3) can be written without normalized polar factors:

\[
 \mathbb E_V[PQ]
 =t(\lambda r)w(AB)
  +\frac{q(\lambda r)}{r^2}w(MA)w(M^\dagger B),
 \tag{9}
\]

\[
 \operatorname{Cov}_V(P,Q)
 =t(\lambda r)w(AB)
  +\frac{q(\lambda r)-b(\lambda r)^2}{r^2}
                         w(MA)w(M^\dagger B).
 \tag{10}
\]

The coefficient limits at $r=0$ are respectively $\lambda^2/24$ and $-\lambda^2/48$. Both multiplied terms are then zero because $M=0$. Thus the formulas have a regular extension with no choice of $W$.

The series are

\[
 \begin{aligned}
 b(z)&=z/4-z^3/96+z^5/1536+O(z^7),\\
 q(z)&=z^2/24-z^4/384+O(z^6),\\
 t(z)&=1/4-z^2/96+z^4/1536+O(z^6),\\
 q(z)-b(z)^2&=-z^2/48+z^4/384+O(z^6).
 \end{aligned}
 \tag{11}
\]

Hence, with $A,B$ fixed,

\[
 \mathbb E_V[PQ]
 =\frac14w(AB)
  +\lambda^2\left[-\frac{r^2}{96}w(AB)
                  +\frac1{24}w(MA)w(M^\dagger B)\right]
  +O(\lambda^4),
 \tag{12}
\]

\[
 \operatorname{Cov}_V(P,Q)
 =\frac14w(AB)
  -\lambda^2\left[\frac{r^2}{96}w(AB)
                  +\frac1{48}w(MA)w(M^\dagger B)\right]
  +O(\lambda^4).
 \tag{13}
\]

These remainders are uniform for $A,B\in SU(2)$ and $r\in[0,1]$ in a fixed sufficiently small coupling interval. Analyticity follows from the explicit Bessel series and the nonvanishing normalized denominator near zero; all matrix products have bounded norm.

If $\lambda=0$, or if $M=0$ at any $\lambda$, the shared link is Haar:

\[
 \mathbb E_V[P]=\mathbb E_V[Q]=0,\qquad
 \mathbb E_V[PQ]=\operatorname{Cov}_V(P,Q)=\tfrac14w(AB).
 \tag{14}
\]

For the explicit fixed-remainder test M=0 and A=B=1, the covariance equals 1/4 while the product of first moments equals zero. The source's transport statement concerns disjoint coarse edges.

### 4. Conditioning only on the fine field: the actual two-plaquette formula

Now integrate the six other coarse links. Assume the two simple plaquettes share exactly one unoriented edge, used once in each, and their other three-edge paths are disjoint. Conditional on $U$, these six links and $V$ are independent under the stated normalized kernel. Consequently $A,B,V$ are independent as three random objects, although $P$ and $Q$ share $V$.

For an oriented external edge $e$, let

\[
 m_e=f_\lambda(r_e)M_e^{(\epsilon_e)},\qquad
 f_\lambda(r)=b(\lambda r)/r,\qquad f_\lambda(0)=\lambda/4,
\]

where $M_e^{(+)}=M_e$ and $M_e^{(-)}=M_e^\dagger$. Define the ordered path means

\[
 \bar A=\mathbb E[A\mid U]=m_{a_1}m_{a_2}m_{a_3},\qquad
 \bar B=\mathbb E[B\mid U]=m_{b_1}m_{b_2}m_{b_3}.
\]

They are real quaternions, generally not unitary. The trace contractions remain linear separately in $A,B$. Independence of these two paths gives the exact identities

\[
 \boxed{\mathbb E[PQ\mid U]
 =t\,w(\bar A\bar B)
  +q\,w(W\bar A)w(W^\dagger\bar B),}
 \tag{15}
\]

\[
 \boxed{\operatorname{Cov}(P,Q\mid U)
 =t\,w(\bar A\bar B)
  +(q-b^2)w(W\bar A)w(W^\dagger\bar B).}
 \tag{16}
\]

The individual conditional means are $b\,w(W\bar A)$ and $b\,w(W^\dagger\bar B)$. Equations (9)–(10) with $A,B$ replaced by $\bar A,\bar B$ give their regular $M=0$ forms.

To state the coupling order without hiding the other six kernel factors, put

\[
 A_M=M_{a_1}^{(\epsilon_{a_1})}M_{a_2}^{(\epsilon_{a_2})}
                  M_{a_3}^{(\epsilon_{a_3})},\qquad
 B_M=M_{b_1}^{(\epsilon_{b_1})}M_{b_2}^{(\epsilon_{b_2})}
                  M_{b_3}^{(\epsilon_{b_3})}.
\]

For a common small $\lambda$ on all seven links,

\[
 \bar A=(\lambda/4)^3A_M+O(\lambda^5),\qquad
 \bar B=(\lambda/4)^3B_M+O(\lambda^5).
\]

It follows that

\[
 \boxed{\mathbb E[PQ\mid U]
       =\operatorname{Cov}(P,Q\mid U)+O(\lambda^8)
       =\frac{\lambda^6}{4^7}w(A_MB_M)+O(\lambda^8).}
 \tag{17}
\]

The coefficient may vanish for a particular $U$; “order six” means the first allowed generally nonzero coefficient. The product of the two plaquette conditional means is only $O(\lambda^8)$. Equations (17)–(18) are pointwise fine-field-conditional expansions, with the fine field and its path means $M_e(U)$ fixed as $\lambda$ varies. No expansion of a coupling-dependent exterior posterior, or remainder after integrating against such a posterior, is asserted.

For an additional coefficient check, set $S=\sum_{e\text{ among all seven links}}r_e^2$ and $H=w(MA_M)w(M^\dagger B_M)$, with $M$ the shared-edge mean. Direct expansion gives

\[
 \begin{aligned}
 \mathbb E[PQ\mid U]
 &=\frac{\lambda^6}{4^7}w(A_MB_M)
  +\frac{\lambda^8}{4^6}
       \left[-\frac S{96}w(A_MB_M)+\frac H{24}\right]
  +O(\lambda^{10}),\\
 \operatorname{Cov}(P,Q\mid U)
 &=\frac{\lambda^6}{4^7}w(A_MB_M)
  -\frac{\lambda^8}{4^6}
       \left[\frac S{96}w(A_MB_M)+\frac H{48}\right]
  +O(\lambda^{10}).
 \end{aligned}
 \tag{18}
\]

Their difference is $\lambda^8H/4^8+O(\lambda^{10})$, as independently obtained by multiplying the individual plaquette means.

Two different zero-limit statements must be kept separate. At $\lambda=0$ on all coarse links, $\bar A=\bar B=0$, so the fine-$U$-conditional moment and covariance in (15)–(16) are zero. At $M=0$ only on the shared edge and $\lambda>0$ elsewhere, both instead equal $\tfrac14w(\bar A\bar B)$, which need not vanish. If any external edge has zero mean, the corresponding path mean vanishes and both quantities are exactly zero.

### 5. Independent orientation and positivity checks

Write $X=x_0I+i\boldsymbol x\cdot\boldsymbol\sigma$. Centrality gives zero vector mean, zero scalar-vector mixed moments, and $\mathbb E[x_ix_j]=t\delta_{ij}$. Since the spin-one character is $4x_0^2-1$, equation (6) gives

\[
 a:=\mathbb E[x_0^2]=(1+3q)/4,\qquad
 t=(1-a)/3=(1-q)/4.
\]

For $C=AW=cI+i\boldsymbol c\cdot\boldsymbol\sigma$ and $D=W^\dagger B=dI+i\boldsymbol d\cdot\boldsymbol\sigma$, direct quaternion multiplication yields

\[
 P=x_0c-\boldsymbol x\cdot\boldsymbol c,\qquad
 Q=x_0d+\boldsymbol x\cdot\boldsymbol d,
\]

so $\mathbb E[PQ]=acd-t\boldsymbol c\cdot\boldsymbol d=t\,w(CD)+(a-t)cd$. Because $CD=AB$ and $a-t=q$, this independently checks (2)'s contraction and its dagger sign.

An explicit noncommuting check is

\[
 A=i\sigma_1,\quad B=i\sigma_2,\quad
 W=(I+i\sigma_1+i\sigma_2+i\sigma_3)/2.
\]

Here $AB=-BA$, $w(AB)=0$, $c=-1/2$, and $d=1/2$. Thus the raw moment is $-q/4$ and the covariance is $(b^2-q)/4=z^2/192+O(z^4)$. No commuting-orientation reduction is needed.

For the equal-loop check take fixed $B=A^\dagger$. Then $Q=P$, $w(AB)=1$, $d=c$, and

\[
 \mathbb E[P^2]=t+qc^2,\qquad
 \operatorname{Var}(P)=t+(q-b^2)c^2
   =t(1-c^2)+(a-b^2)c^2\geq0.
 \tag{19}
\]

Indeed $|c|\leq1$, $t=\mathbb E[x_1^2]\geq0$, and $a-b^2=\operatorname{Var}(x_0)\geq0$. Both coefficients are strictly positive for finite real $z$, because the density is strictly positive on all of $SU(2)$. At $z=0$, the variance is exactly $1/4$. This is a fixed-remainder algebraic check; imposing $B=A^\dagger$ on random paths would remove their independence and is not the distinct-plaquette hypothesis used in (15)–(18).


## Appendix B. Semigroup comparison and boundary response

The finite product laws, strictly positive conditional densities, oscillations,
B, D and supports are those in section 7. This provides a different proof of
the covariance and boundary estimates under those same hypotheses. It is not
an additional physical premise.

**Semigroup covariance estimate.** Let E_e be heat-bath conditional expectation at fine coordinate e under one of these posteriors pi, let N be the number of fine coordinates, and let

    P = N^(-1) sum_e E_e,
    L = sum_e(E_e−I),       P_t = exp(tL).

Write delta f for the column vector of single-coordinate oscillations. For j≠e, changing coordinate j in E_e f gives

    delta_j(E_e f) ≤ delta_j f + B_ej delta_e f,
    delta_e(E_e f)=0.

It follows by iteration and Poissonization that

    delta(P_t f) ≤ exp[t(B^T−I)] delta f.

Since the row sums of B are at most q<1, the right side tends to zero in l1 at rate at least 1−q. Invariance of pi then implies P_t f→E_pi f uniformly. Heat-bath conditional expectation is self-adjoint, and integrating the generator identity gives

    Cov_pi(f,g)
      = integral_0^infinity sum_e E_pi[Cov_e(P_t f,g)] dt.

The one-coordinate range covariance inequality bounds the integrand by (1/4) sum_e delta_e(P_t f)delta_e g. Hence

    |Cov_pi(f,g)|
      ≤ (1/4) delta g^T (I−B^T)^(-1) delta f
      = (1/4) delta f^T D delta g,       D=(I−B)^(-1).

This proves section 7 equation (30), including its factor 1/4, without using a tilted comparison measure. It applies uniformly to the posterior interpolations because the same B bounds all of them.

**Coarse influences.** Let R_ie=1_(e in S_i). The two endpoint insertions in (25) satisfy delta A_i≤4lambda R_i and delta H_j≤4lambda R_j. The rectangle integral therefore has absolute value at most 4lambda²(RDR^T)_ij. Normalizing the coarse one-site density subtracts a term independent of its own coordinate, so its boundary likelihood-ratio log oscillation has the same bound. The TV lemma gives

    C_ij ≤ tanh[lambda²(RDR^T)_ij] ≤ lambda²(RDR^T)_ij,    i≠j.

The identity term in D explicitly retains S_i∩S_j. It cannot be dropped when the two coarse edges have overlapping fine footprints.

**Weighted resolvent and coarse sum.** Put r=5L and use the stated periodic l1 midpoint distance. The two-block rectangle is contained in the radius-r ball about its coarse midpoint; each B-step connects fine edges at distance at most 2r. For q_alpha=e^(2r alpha)q<1, the path expansion for B^n and the triangle inequality give

    sup_e sum_f e^(alpha d(e,f))D_ef ≤ sum_(n≥0)q_alpha^n
                                             =1/(1−q_alpha).

For each e∈S_i and f∈S_j,

    d(i,j)≤r+d(e,f)+r.

Summing first over coarse j containing a fixed fine f incurs at most the incidence factor eight. Summing next over e∈S_i incurs at most s_L. Therefore

    sup_i sum_(j≠i)e^(alpha d(i,j))C_ij
       ≤ 8s_L lambda² e^(2r alpha)/(1−q_alpha) = Q_alpha.

Including the coarse diagonal during this upper bound is harmless. Solving Q_alpha<1 is exactly e^(2r alpha)[q+8s_L lambda²]<1, which yields (33) and the alpha interval in section 7 following (33). There is no hidden additional factor of two or support-incidence factor.

**Many changed exterior links by a Poisson equation.** For two coarse laws mu,nu on J with different exteriors, use the mu heat-bath semigroup and define

    h = integral_0^infinity(P_t f−mu f)dt,
    L_mu h = mu f−f.

Since nu L_nu h=0,

    nu f−mu f = nu[(L_nu−L_mu)h].

At equal interior environments the one-site kernel difference is at most b_i≤sum_(j in H)C_ij, by telescoping the changed exterior coordinates. The same oscillation contraction as in this appendix gives delta h≤(I−C_JJ^T)^(-1)delta f, hence

    |nu f−mu f|≤delta f^T(I−C_JJ)^(-1)C_JH 1_H.

The weighted row norm is submultiplicative by the distance triangle inequality. Its geometric sum is Q_alpha/(1−Q_alpha), and every path ending in H has total length at least d(i,H). This proves both inequalities of (34) with the stated decay factor. This second derivation covers the actual two-region boundary conditional, not merely a formal covariance matrix.
