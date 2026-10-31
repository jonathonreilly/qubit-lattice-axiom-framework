# Mixed compact good caps and original-coordinate charts

This proves a pure small-chart comparison for the supplied four-dimensional
SU(N) bare step, at a FIXED REAL coarse center and complex original Wilson
sources. Every fine free link is integrated. On an arbitrary deterministic
block mask the exact compact chord cap is imposed; on its complement the
original product of whole-link coordinate balls is imposed. These different
domains have one identical full critical prefactor and uniformly small
complete-reader logarithms. Differences of the logarithms are anchored to
the changed mask owners.

The new argument groups variables by their original owner blocks, proves
the geometry of the actual cap, and uses a single exact translation/Stokes
identity on each block body. It changes no coordinate or Jacobian. Full-block
activation, including otherwise unused links of a selected vertex's owners,
is essential. The result is not a conditional cap theorem with pinned fine
boundary values, nor a normalized expectation bound for arbitrary compact
insertions. It does not finish the original-cut complement gas. Full non-free
continuum existence and a positive physical continuum mass gap remain OPEN.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

Bałaban's localization architecture and Dimock's exposition are antecedents;
Lohmann's cutoff analysis is compared precisely in section 10. No theorem
about a scalar model or d=3 is imported as a four-dimensional SU(N) theorem.
The parent target is the exact mixed-cut comparison, not a continuum theorem
renamed as a local lemma. The supplied bare action and its proved local
analytic producer estimates are explicit premises, not derived physical
axioms. No framework primitive is added or used to settle a dynamical gap.

## 1. Exact object and the common full prefactor

Use the actual density and pinned tree quotient of
[SC1](SOURCE_LOCAL_COMPACT_RETURN_ASTRA.md), at its frozen 597-line source
SHA256 `c39e78ac1d31024d5266e16ace022fa86497a6d09c45aa25b215ffa390533dff`.
Fix N>=2, odd L>=3, T>=2, u>=N and kappa in its admitted positive interval.
Write

    D=N^2-1, m0=3L^4+1, k=n0=D m0,
    n=m0 T^4, d=k T^4, sigma^2=N/u.

Let E_X be the m0 free positive whole links owned by coarse block X.
Every colour, crossing, root and harmonic direction remains. The integrated
nonroot gauge volume is one. Fix real Vbar with admitted small curvature
delta, and put U0=U0(Vbar). Relative coordinates are
U_e=exp(a_e)U0_e. Negative words always use the actual inverse.
The exact original-source density and chart phase are

    w_epsilon(U,Vbar)=exp[-u sum_p(1+epsilon_p)s(U_p)]
                          product_c k_(kappa u)(Vbar_c;M_c(U)),
    F_epsilon(a)=sigma^2[-log w_epsilon(exp(a)U0,Vbar)
                                      -sum_(e in E)log j_N(a_e)],
    F_epsilon=F_0+sum_p epsilon_p W_p,
    W_p=tr(2I-U_p-U_p^-1)/2.                             (MC1)

The original finite-t compact normalizer, its vacuum, the Haar logarithms
and all field-free original vertices are in F. The positive Haar constant
h_N remains outside it. Complex epsilon varies only on the original
Wilson labels, |epsilon_p|<rho. At real integration variables the kernel
normalizers are the original positive compact integrals. On the small
contours below their proven local analytic continuation is used.

For h=sqrt(N q), impose the injectivity conditions in section 2 and
sqrt(2)h<=r_a. Define the TWO block bodies in the real k-dimensional HS
coordinate space by

    D_X^0=product_(e in E_X){||a_e||HS<r_a},
    D_X^1={max_(e in E_X)||a_e||HS<1/2, Q_X(a)<q},
    Q_X(a)=N^-1 sum_(e in E_X)tr(2I-exp(a_e)-exp(-a_e)).  (MC2)

For an arbitrary deterministic set M of blocks put d_X=1_(X in M) and
D_M=product_X D_X^(d_X). The ACTUAL mixed integral is

    Z_M=int dH_E w_epsilon(U,Vbar)
              product_(X in M)1_(sum_(e in E_X)||U_e-U0_e||HS^2/N<q)
              product_(X notin M)1_(a_e exists, ||a_e||HS<r_a for all e in E_X)
       =h_N^n int_(D_M) exp[-F_epsilon(a)/sigma^2] da.    (MC3)

Section 2 proves the second equality and that this is precisely the cap's
principal injective component; the auxiliary 1/2 boundary is never reached.
Null boundaries may be included. This is neither a product of link caps
nor a white-coordinate cube. Z_empty is exactly the original-a chart
integral, and Z_all is the exact all-Q-good small-cap integral.

Use ONE global specialization Lambda=E of
[RF](REGIONAL_CRITICAL_FIELD_ASTRA.md), SHA256
`45a5665fc51683f026370e774ca8590b221bc5c9e13c07502225226cb13c962b`, with
[RC](REGIONAL_CHART_RETURN_ASTRA.md), SHA256
`b098d18ad22946d7b1e0a4d497e0b5d98250674e06803263d1106f14bf659094`.
Restore RF's outside empty-stencil constants to F. They do not change its
critical equation. The actual global objects are

    F_epsilon'(b)=0, K_*=F_epsilon''(b), C=K_*^-1,
    P_*=h_N^n(2pi sigma^2)^(d/2)
                   exp[-LogDet(K_*)/2-F_epsilon(b)/sigma^2].          (MC4)

These objects do not depend on M. LogDet is the accretive matrix branch
continued from the positive real Hessian, on ALL d coordinates. The source
values, compact normalizers, Haar factors and critical action are identical
in every P_*. No small estimate is assigned to that extensive prefactor.
The [regional-ratio theorem MR](MATCHED_REGIONAL_RATIO_ASTRA.md) compares
different active sets and does not already compare MC3's two cut geometries.

## 2. The actual cap is a small analytic convex body

Assume SC5's traceless-log margin

    sqrt(N q)<2sin(pi/(2N)),
    (pi/2)sqrt(N q)<1/2,
    sqrt(2N q)<=r_a<=1/4.                              (MC5)

The stricter SC5/SC6 buffer margins can also be imposed. If the physical
Q_X<q, every eigenangle theta of U_e U0_e^-1 lies in (-pi/N,pi/N).
The principal logarithm is traceless: the sum of the N angles is a multiple
of 2pi of absolute value <pi. It is the unique logarithm in this small
branch. The scalar sine estimate then gives

    sum_e ||a_e||HS^2 <= (pi^2/4)N Q_X < (pi^2/4)h^2.    (MC6)

Thus the physical cap has no other logarithmic component. Conversely every
small traceless a in MC2 gives the physical chord cap, since U0 is unitary.
Q is not treated as globally coercive on the Lie algebra.

Here is a direct full-Hessian proof, including noncommuting directions.
On the convex set max_e||a_e||HS<1/2, expand the trace exponentials.
The quadratic term is sum_e||a_e||HS^2/N. For two real HS directions v,w,
the degree-j differentiated trace is a sum of j(j-1) words. Schatten
Holder bounds each word by ||v_e||HS ||w_e||HS ||a_e||op^(j-2).
Only even j occur. Consequently

    ||Q''(a)-(2/N)I||op
          <=(2/N)sum_(even j>=4)(1/2)^(j-2)/(j-2)!
          =(2/N)(cosh(1/2)-1)<1/N,
    (1/N)I <= Q''(a) <= (3/N)I.                         (MC7)

Summing over links uses Cauchy--Schwarz in the block direct sum; k, rather
than D, is its dimension. The final strict numerical inequality follows,
for example, from cosh(1/2)<=sum_j(1/4)^j=4/3<3/2.
Integrating MC7 radially and using the exact sine upper bound gives

    ||a||^2/(2N)<=Q(a)<=||a||^2/N,
    ||a||/N<=||grad Q(a)||<=3||a||/N,
    a.grad Q(a)>=||a||^2/N.                             (MC8)

The first rough enclosure MC6 places the whole physical component in this
convex neighborhood. The stronger lower bound in MC8 now gives

    B_h^k subset D_X^1 subset B_(sqrt(2)h)^k,
    B_(r_a)^k subset D_X^0 subset B_(sqrt(m0)r_a)^k.      (MC9)

The cap is the sublevel of a strictly convex function in that neighborhood,
with closure away from its boundary, hence is convex. It is symmetric under
a->-a and has analytic boundary with nonzero gradient. Its outward unit
normal is grad Q/||grad Q||. The principal curvatures, from the restriction
of Q''/||grad Q|| to the tangent space, lie between

    1/(3sqrt(2)h) and 3/h.                              (MC10)

For an explicit surface bound write its boundary radially as r(omega)omega.
MC8 gives |grad_S log r|<=3, while r<=sqrt(2)h. Therefore, with omega_j
the area of S^(j-1) and v_j the volume of B_1^j,

    area(partial D_X^1)<=4 omega_k (sqrt(2)h)^(k-1),
    area(partial D_X^0)=m0 omega_D v_D^(m0-1) r_a^(k-1).
                                                                  (MC11)

The second equality sums the actual link-sphere faces; their intersections
have codimension at least two. Both bodies contain B_h^k, every boundary
point has norm >=h, and every coordinate/link of either body has its
original norm <=r_a. In scaled variables x=a/sigma put p_a=r_a/sigma,
p_-=h/sigma and

    C_area=max(4omega_k,m0 omega_D v_D^(m0-1)).

Then each scaled boundary has area <=C_area p_a^(k-1).
These are geometric bounds used to estimate an exact identity below;
no inclusion in MC9 replaces one domain integral by another.

## 3. Common producer, nonlinear envelopes and strengthened shift margin

Use RF's one ambient cover with R>=4 and beta=(16R)^-4, its canonical
critical-field atom family and both actual covariance tails. On the global
specialization y=0, RF19--RF23 give

    V_beta(b)<=tau,
    C=P+E, E=E_lift+T_crit,
    M_beta(E)<=e, B_beta(E)<=B_E,
    e<=min(c0/8,1/(4v_I),a/(64v_I^2)),
    a=c0/g^2, b_P=1/c0.                                (MC12)

M_beta is the maximum weighted row/column sum of individual coefficient
suprema; B_beta is the corresponding full-reader marked sum. B_E is fixed
and finite, not presumed small. V_beta has both scalar component-root and
summed marked-coordinate bounds. Every complete reader contains its field
owner and all original data. RF24 proves, for every active set I below,
Re(P[I]^-1)>=a and the row/column bound v_I. Full-block activation is a
particular whole-link restriction, so this interface applies literally.

Fix R and the preliminary RF/RC source/fine ceilings first. Restrict to
V=Vbar real, with a FIXED positive rho chosen inside RF17 at those ceilings.
The local normalizer domain and the full original vertex majorants remain
the ones actually proved in RF/RC. For the whole set of original vertices
let q_v=(8L^4+8)D, I0=15, s_v=27^4, v0=9L^4+5 and
d_v=v0 s_v. The larger RC roots are harmless at y=0. Take its
f_reg(t)=2H(1-t/a_f)^(-q_v) at fixed bar_tau,bar_rho and r_t.

The shifted Taylor/Mayer bounds SN8--SN9 are valid with that f_reg and the
new block side pattern J subset B_v, where
B_v={X: E_X meets the actual whole-link stencil L_v}. A fixed pattern
translates every actual slot in a side owner by the SAME parameter t_X.
The binomial expansion still has at most 2^l terms at degree l; each actual
scalar slot satisfies |sigma x_i|<=r_a, |b_i|<=tau. Since |B_v|<=q_v,
the old 2^q_v pattern bound is still an upper bound. Thus the safe positive
coefficient budgets can be fixed explicitly by

    A_sh=8(1+bar_rho)e^(beta s_v) f_reg'''(bar_tau+r_t)/6,
    B_sh=8q_v d_v(1+bar_rho)e^(beta s_v)
         [4f_reg'''(bar_tau+r_t)+(bar_tau+r_t)f_reg''''(bar_tau+r_t)]/6,
    W0=2^(q_v+1)A_sh, W1=2^(q_v+1)B_sh.                 (MC13)

Take NC7's A3,B3,A4,B4 with this SAME f_reg, ceilings, radius r_t and
root count d_v. Set
E0=2A4+2A3^2 and E1=2B4+4A3 B3+2A3^2(B3+B4)/A,
where A>=max(1,A_sh,A3,A4). These follow by the geometric-series
Mayer envelopes and the exact odd/even split of NC12--NC15, not by changing
u in its coefficients. Enlarging A only improves the displayed envelopes.

For reference the density constants are, exactly as in SN4,

    t=v_I e, t_E=v_I^2 e/(1-t), ell=-log(1-t)/2,
    c_*=2b_P^2/a+b_P+t_E+1,
    L_hat=sqrt(2)max(1,sqrt(2 exp(1)c_*)),
    K_m=v_I/[2(1-t)]+v_I^2(16/a+1)/(1-t)^2.             (MC14)

Now choose r_a small enough that r_a<r_t/8, r_a<=1/4, and
eta_bar=4A I0 r_a(1+r_a)<=a/128. Choose h>0 satisfying MC5 and
sqrt(2)h<=r_a. Only then choose the actual critical-field ceiling tau with

    tau<=min(bar_tau,h/(16k)),
    (L_hat^2+2eta_bar)(k tau)^2<=a h^2/64,
    2(r_a+tau)<=r_t.                                    (MC15)

Shrink the REAL curvature window so, besides all fixed RF ceilings,

    A_G g_*(1+rho)delta<=tau/8.                          (MC16)

RF's actual global force has bound g_*(1+rho)delta, with no exterior
y term. RF19's contraction then proves its actual solution has
V_beta(b)<=2A_G g_*(1+rho)delta<=tau/4, hence MC12. The stronger MC15
uses k tau against the SMALLER cap radius h; fitting b inside the larger
original chart alone would not suffice. This construction is uniform in M
because neither the phase nor its critical point depends on M. All choices
are positive and precede the eventual large-u bounds.

Here tau is a smaller bound for the GLOBAL branch at y=0, not a replacement
of SC's regional boundary ceiling zeta. Uniqueness identifies the smaller
contraction's solution with that same global branch. SC may keep its own
regional tau,zeta and q-to-zeta margin, fixed before this additional
curvature restriction. No requirement zeta<=this tau is imposed. In
particular shrinking the global force does not shrink an exterior domain
that this theorem never uses.

## 4. Exact block-body translation, including product-face corners

Put Omega_X=D_X^(d_X)/sigma and m_X=b_X/sigma, in all k block coordinates.
For a bounded Lipschitz body Omega and a holomorphic f on the entire sweep,
the fundamental theorem and the real divergence theorem, componentwise
also for a complex vector m, give

    int_Omega f(x-m) dx
      =int_Omega f(x) dx
          -int_0^1 dt int_(partial Omega)(m.n(x))f(x-tm)dS(x). (MC17)

This is integration of a holomorphic top form on translated chains. It is
not analytic continuation of an indicator. For D_X^0 the divergence theorem
is the sum over all its link-sphere faces with the other links still inside
their balls. Its within-block face intersections have surface measure zero;
their whole straight translation sweep is already in MC17. One does not
need extra codimension-two terms for a SINGLE simultaneous block homotopy.
Expanding translations link by link instead gives the same endpoint identity
with its iterated corner terms. Tensoring MC17 over blocks gives every
cross-block boundary/corner chain exactly.

Let R_v be the original vertex remainder after its constant, linear and
quadratic jets at b have been subtracted, as in RC7, and W_v=exp(-R_v)-1.
Only the sum of the linear jets vanishes. With g_C the normalized Gaussian
in all d dimensions, MC3 and MC4 now give EXACTLY

    Z_M/P_*=sum_(H subset blocks)(-1)^|H| int_[0,1]^H
       int_(product_(X in H)partial Omega_X times product_(X notin H)Omega_X)
         product_(X in H)(m_X.n_X) g_C(x-tm_H)
                              product_v[1+W_v(x-tm_H)] dS_H dx dt_H. (MC18)

The Jacobian of the translation is one. Scaling the volume, surface and
flux supplies sigma^d, sigma^(-(k-1)) and sigma^-1 in their exact places;
MC4 already has the full volume scaling. Every fine link on the sweep has
norm <=r_a+2k tau<a_f after the stated preliminary restrictions. Thus ALL
actual normalizer inputs stay in their proven small analytic domain.

For a selected set W of DISTINCT original vertices, put
F_b(W)=union_(v in W)B_v. Expand remaining body cuts as one minus their
exact exterior failures. Retain full block bodies on selected vertices'
non-side owner blocks. The admissible primitive families have side blocks
H, bad blocks B and selected vertices W with

    B disjoint H union F_b(W),
    J_v=H intersect B_v,
    I=all k scalar coordinates of every block in F_b(W) union H union B.
                                                                  (MC19)

All unselected Gaussian modes integrate to one, giving the principal
covariance C[I]. The shift is supported in I. Gaussian marginalization
extends to these complex translated active arguments by entire analyticity.
No inverse principal precision is substituted for C[I]. No vertex is
evaluated on an exterior bad block. At empty W,H,B the normalized marginal
is exactly one, with no residual vacuum.

Activating only L_v instead of all of E_(B_v) would leave part of Q_X in
an inactive variable. Then MC19's marginalization would be false. The
enlargement is paid: a vertex activates at most Q=q_v k scalar coordinates,
although its polynomial still uses at most q_v actual slots.

## 5. Every scalar factorial, surface factor and Gaussian tail

A nonlinear primitive is an actual reader atom with its block side pattern.
A bad primitive is one block with its signed exterior indicator. A side
primitive is one scalar flux atom -b_(i;S)n_i/sigma, with i owned by X,
the entire boundary partial Omega_X and its single t_X. The sign is already
in this primitive. A block may be a side or bad only once; a vertex may
occur only once. Attach Q_X=N_(16R)(X) and Q_v=N_(16R)(x_v) to these
primitive readers. Every added active link has an owner already in B_v,
so the core-patch displacement bound <=5R+9<=16R still applies. Set

    s_c=(32R+1)^4, d_c=v0 s_c, d_h=s_c.                 (MC20)

Here d_h counts BLOCK cut roots. The k scalar choices of a flux are paid
separately below. Components of overlapping primitive readers retain their
whole primitive list, masks, normals and side flags. Their active sets are
disjoint, P[I] is block diagonal between them, and a core inverse/determinant
reads its component once. Both presence and absence in J_v=H intersect B_v
are internal to these components. This is an exact invertible partition.

The normalized density on the active set is decomposed by the exact loop
and chain series of NR15: all powers of G E[I], G=P[I]^-1, including the
trace-log and inverse quadratic correction. On independent component-pair
masks |s_BB'|<2 the covariance remains accretive. Quantitative estimates use
real forest masks. The row bounds in MC12 and the Cauchy radii
sqrt(nu_i/(2c_*)) give the absolute density-list jet bound

    A_I exp[-a||x||^2/8] L_jet^|nu| product_i sqrt(nu_i!),
    A_I=(b_P/(2pi))^(|I|/2)exp(|I|ell), L_jet=L_hat/sqrt(2). (MC21)

The marked list bound has the extra factor K_m D_z(I), where
D_z(I)=sum_(i in I)sum_(j,S contains z)e^(beta|S|)sup|E_S(i,j)|,
and sum_i of this pin is <=B_E. The proof is the exact determinant/inverse
series, Young's inequality, and scalar optimized Cauchy estimates; it is
independent of the shape of Omega_X. No integration by parts onto a cutoff
or its normal occurs at ANY forest order.

Expand the Gaussian translation in b's actual atoms. At a side block its
scalar l1 atom mass is <=k tau. The elementary series
sum_j z^j/sqrt(j!)<=sqrt(2)exp(z^2), together with
sqrt((nu_i+j)!)<=2^((nu_i+j)/2)sqrt(nu_i!)sqrt(j!), changes MC21 to

    A_I exp[-a||x||^2/8] L_hat^|nu| product_i sqrt(nu_i!)
                  2^(k|H|/2) exp[L_hat^2(k tau/sigma)^2 |H|].        (MC22)

A reader mark in this translation retains its actual side-block root and
costs K_tr sum_(X in H)d_z^b(X), with

    s=k tau/sigma, K_tr=(L_hat/sigma)(1+sqrt(2)L_hat s),
    d_z^b(X)=sum_(i in E_X colours,S contains z)e^(beta|S|)sup|b_(i;S)|,
    sum_X d_z^b(X)<=tau.                                (MC23)

This follows by differentiating the same positive entire series. It keeps
the per-coordinate factorial product, also at mixed shift/forest orders.

Each distinct selected vertex contributes one cubic polynomial, or a
quartic plus the square of a cubic for a no-side parity singleton. The
original scalar incidence I0=15 is unchanged by integrating more fields:
extra coordinates do not enter the polynomial. Thus each coordinate has
degree at most 90. The regulator costs at most
exp[2eta_bar||x||^2+2eta_bar s^2|H|]. With

    M90=2^90 max(1,(2880/a)^45),
    K_g=max(1,exp(ell)sqrt(8b_P/a)),
    C_V=Q(1+Q)(K_g M90)^Q,
    A_k=(b_P/(2pi))^(k/2)exp(k ell),
    q_h=K_g^k 2^(k/2)exp[-a p_-^2/32],
    Q_s=A_k 2^(k/2)C_area p_a^(k-1) sigma^-1
                              (1+s)^(90k)exp[-a p_-^2/64],           (MC24)

the integrated mixed jets are bounded by

    L_hat^|nu| product_i sqrt(nu_i!) product_o a_o,
    a_vertex=C_V sigma w_(v,J;S),
    a_bad=q_h, a_side=Q_s sup|b_(i;S)|.                 (MC25)

To check all geometric uses: retain exp(-a||x||^2/16) after the polynomial
and regulator absorption in MC22. On a bad block x outside Omega_X,
||x||>=p_-. Splitting this Gaussian exponent in half gives q_h by the
k-dimensional product-Gaussian exponential moment. On a side block the
same lower radius and MC11 give its actual surface measure. MC15 absorbs
the shift exponential by exp(a p_-^2/64), leaving more than the decay
used in Q_s. The flux gives sigma^-1. The factor (1+s)^(90k) pays all
shifted powers on the whole side block. No normal is bounded by more
than one. Bulk active Gaussian normalizers cost K_g per coordinate;
at most Q can be assigned to a vertex. These assignments also overcount
coordinates shared by selected vertices, which is harmless since K_g>=1.
All determinant and surface factors are present.

A signed singleton nonlinear integral with NO side has weight
C_V sigma^2 e_(v;S): every Omega_X is symmetric under x->-x, and every
individual Gaussian list is even. Its exact odd part integrates to zero
at fixed u and fixed complex source. A side singleton, or any side-bearing
species, receives no such parity improvement.

## 6. Exact forests, marked sums and the connected logarithm

For an independent pair of primitive components the normalized heat identity
is

    partial_(s_BB') int Phi g_(C_I(s))(x-tm_H)
      =sum_(i in I_B,j in I_B')E(i,j)
                 int Phi partial_i partial_j g_(C_I(s))(x-tm_H).     (MC26)

It follows by differentiating both determinant and inverse; the two
symmetric entries remove the factor 1/2. Phi contains all exact body cuts,
surface normals, fluxes and common t_X parameters and is NOT differentiated.
Thus MC25 is the required all-order boundary estimate without derivatives
of a hard predicate. At disconnected forest endpoints the measures and
all fixed body patterns factor by component. The finite forest identity
is applied to independent pairs before path-minimum evaluation; its
monomial proof by independent clocks, as in SN20, applies on the analytic
radius-two pair polydisc. No derivative of a path minimum is used.

Raw species retain base compatibility from the primitive partition. Their
complete readers also contain every Gaussian-tree E reader, density-list
E reader and Gaussian-translation b reader. Each such label attaches to
an active endpoint already in its base. The complete union is connected.
Every species has a nonempty primitive; an empty Gaussian component is one.

For explicit simultaneous positive budgets set

    h_v=C_V sigma e^(beta s_c)(W1+d_c W0),
    h_2=C_V sigma^2 e^(beta s_c)(E1+d_c E0),
    h_h=d_h e^(beta s_c)q_h,
    h_s=Q_s e^(beta s_c)tau(1+d_h k), h_0=h_v+h_h,
    h_tr=K_tr Q_s e^(beta s_c)k tau^2,
    C0=1+K_m B_E,
    h_c=min(beta/16,1/[4(1+L_hat^2 e)],
                          beta/[64k(1+L_hat^2 e)]),
    epsilon_mix=C0(h_2+h_h)+(C0/h_c+L_hat^2 B_E)h_0^2
                    +2(C0+L_hat^2 B_E h_c)h_s+h_tr.     (MC27)

The h_s mark in an original b reader uses its total marked norm tau;
a collar mark uses d_h times the block component bound k tau. For h_tr,
first sum flux atoms at the SAME block as its translation pin, giving
k tau, then sum that pin over blocks, giving tau. Rooting it at an
unrelated vertex would lose this rare side factor and is not allowed.

Here are the summation checks. Spend beta/8 on primitive overlap trees.
The recursion T_o=v_o exp(sum_(o' overlaps o)T_o') has supersolution
a_o exp(beta|S_o|) if h=h_0+h_s<=beta/8. Spend a second beta/8 on
scalar Gaussian trees. Allocate child legs at each scalar coordinate
BEFORE summing: its 1/j! combines with sqrt((j+incoming)!) in MC25.
The series H0(y)<=exp(2y), H1(y)<=exp(4y), y<=1/2, and row mass e
give the supersolution whenever h<=h_c. Here |I_B|<=k|S_B|, including
the full-block activation, so its support cost remains linear in |S_B|.

Marks in a base reader, a density E reader or a tree E edge respectively
cost h, K_m B_E h and L_hat^2 B_E h^2. The last bound cuts the marked
edge into two incoming-leg trees. A translation-reader mark is rooted at
its actual side primitive; linearity in that distinguished root transports
the h_tr bound through both positive tree sums. Flux and nonlinear-shift
marks have already been counted in h_s and W1. These are full-reader
marks, not a total-volume estimate relabelled as locality.

For species without sides use the signed singleton bound h_2 or the hard
singleton h_h. Rescale ordinary positive primitive weights to h_c and
undo the degree-two rescaling on species with at least two primitives;
this gives the first two terms of epsilon_mix. For side-bearing species
rescale ONLY side weights by h_c/(2h_s), then undo at least one such
factor. The distinguished h_tr root scales once. This gives the last
two terms. All amplitudes, u, b, density lists and domains remain fixed
during these positive counting rescalings.

Impose

    sigma<=1, q_h<=1, h_0<=h_c/2, h_s<=h_c/2,
    epsilon_mix<=beta/16.                               (MC28)

Regroup each raw compatible family by overlap of its COMPLETE readers,
retaining old base compatibility within each joined group. This partition
is unique and invertible: complete-reader disjointness across groups
implies base disjointness. Spend a third beta/8 on its rooted overlap sum.
For the exact hard-core logarithm spend a fourth beta/8. The alternating
connected graph coefficient is bounded by spanning trees, by partitioning
graphs into the Boolean intervals of a fixed Kruskal tree. Its rooted
exponential recursion is stable at MC28. These arguments give

    Z_M=P_* exp[sum_(connected ambient Y)H_(M,Y)(Vbar,epsilon)],
    sup_x sum_(Y contains x)e^(mu|Y|)sup_(M,Vbar,epsilon)|H_(M,Y)|
                   <=epsilon_mix, mu=beta/2>0.          (MC29)

Suprema are of individual coefficients BEFORE summation and include all
deterministic masks; there is no sum over 2^(T^4) masks. Absolute convergence
of the uniform envelopes permits finite-list truncations, all integrations,
forest operations and regroupings to converge. The graph identity first
holds near zero common activity multiplier and extends throughout its unit
disc by those bounds. This proves nonvanishing before choosing the small
log branch. P_* is nonzero by its accretive determinant and exponential.

## 7. Canonical mask agreement and changed-owner ratios

Fix the ambient torus, cover, order of original vertices, scalar indices,
atom words and forest/cluster labels independently of M. Include every body
type d_X read by a primitive, its normal or a selected-vertex body constraint
in that primitive's base reader. All Gaussian producer coefficients are
the SAME functions for every mask. Core inverses and determinants read
their fixed base component. The complete unions in section 6 retain every
other reader. Therefore each finite decorated coefficient, and by absolute
convergence each H_(M,Y), agrees whenever its original data and body flags
agree on Y. In particular, at the same original data,

    H_(M,Y)=H_(M',Y) if Y intersect (M symmetric_difference M') is empty.
                                                                  (MC30)

This is coefficientwise agreement on one library, not a choice of unrelated
representations after bounding each integral. Keep zero coefficients and
inadmissible pattern labels in the common indexing. The original empty-mask
integral is identical to SN/RC's global original chart, even though this
blockwise construction need not have their old LINKWISE coefficient list.
MC30 compares masks only inside the present common blockwise library.

Let A=M symmetric_difference M'. The full prefactor cancels algebraically,
not by an estimate or discarded vacuum. The connected branch gives

    log(Z_M/Z_M')=sum_(Y:Y intersects A)[H_(M,Y)-H_(M',Y)],
    sup_x sum_(Y contains x)e^(mu|Y|)
                             sup|H_(M,Y)-H_(M',Y)|<=2epsilon_mix,
    |log(Z_M/Z_M')|<=2epsilon_mix |A|.                  (MC31)

Every displayed summand is attached to an actual changed owner. A fixed
owner ordering can assign it to the first owner of A in Y; this is exact
anchoring, with no additional reader deletion. For real sources the
density is positive and D_X^1 subset D_X^0, so enlarging M decreases Z_M;
the branch agrees with the real logarithm. For complex sources it is the
branch fixed by the connected expansion. At M=M' the ratio is exactly one.

For any fixed multiindex nu in original epsilon, on |epsilon|<rho/2,
the same coefficient sums are bounded by nu!(2/rho)^|nu| epsilon_mix,
or twice that for MC31's difference. A source outside a full reader has
zero derivative of that coefficient. No effective source label replaces an
original Wilson source. This theorem makes no complex coarse-domain or
unscaled coarse-jet assertion: Vbar is fixed real throughout MC1--MC31.

## 8. Fixed and shrinking parameter orders are nonempty

For fixed radii, first choose one RF ambient family, its preliminary fine
analytic/critical ceilings and a positive source radius at those ceilings.
Fix all local, matrix and marked constants there. Then choose r_a, q,
tau and real curvature delta in the order MC5, MC15, MC16. Finally choose
u large enough for MC28. Every constant preceding that last choice is
independent of T and M. At fixed h,r_a,tau, h_v=O(sigma), h_2=O(sigma^2),
whereas h_h,h_s,h_tr are fixed polynomials in sigma^-1 times
exp[-a h^2/(64sigma^2)]. Consequently MC28 eventually holds. Flat real
coarse centers, with the compatible holonomies admitted by RF, give
nonempty examples. No large numerical threshold is asserted.

For the shrinking cap/chart comparison fix c_q>0 first, with N c_q<=1/2
and any further SC5/SC33 buffer margins. Put gamma_q=sqrt(N c_q), choose
a fixed r_max inside section 3's chart bounds, and set

    eta_max=4A I0 r_max(1+r_max), C_max=L_hat^2+2eta_max,
    0<c_b<=min(1/(16k),sqrt(a)/(8k sqrt(C_max))),
    r_a=sigma p, q=c_q sigma^2 p^2,
    h=gamma_q sigma p, tau=c_b h,
    delta<=tau/[8A_G g_*(1+rho)].                        (MC32)

Keep the SAME rho and canonical producer construction. If p>=1, p tends
to infinity and sigma p tends to zero, all fixed MC5/fine ceilings and
MC15--MC16 hold eventually, with rho fixed before u. Forcing delta down
further to SC12's delta^2<=c_SC q/(8a_bulk V_K) is permitted; that extra
window is of order sigma p/K^2 and does not contradict MC32. SC's
q-dependent component scale K and its absence predicates are not inserted
into this pure-chart construction.

Insert MC32 directly into MC24--MC27. In Q_s the factor sigma^-1 is
canceled by tau in h_s. In h_tr its additional K_tr pole is canceled
by the SECOND tau; the distinguished root is a side. Hence, for fixed
finite C1,C2 and M_k=91k+2,

    epsilon_mix<=C1 sigma^2
             +C2(1+p^M_k)exp[-a N c_q p^2/64].          (MC33)

All constants are fixed before u,T and M; they may depend on N,L,c_q and
the admitted model/producer constants. The polynomial degree k is not D.
For example h_s has degree at most 91k and h_tr at most 91k+2.
MC33 tends to zero and verifies MC28 eventually. For the concrete SC
choice p=(log(2+u))^alpha, alpha>5/2, it applies with its additional
delta=O(sigma p/K^2) restriction. The stronger alpha condition is needed
for SC's compact entropy estimate; the pure-chart theorem itself only
uses p tending to infinity and sigma p tending to zero.

## 9. Exact interface still missing for compact gluing

MC29--MC31 compare fully integrated pure small-field masks. They do not
remove the product of q-good predicates on the exterior of a compact
insertion. Nor do they give a uniform normalized expectation norm for that
insertion, since it can depend on fields that were integrated in MC3.
An exact simultaneous compact substitution must match its numerator,
remaining sea predicates, common reference and signed local marginals
before this chart ratio can be used. No compact selector is deformed here.

No regional cap denominator with arbitrary q-good pinned boundary data is
claimed: such data can force a conditional critical point toward the cap
boundary. MC16 instead bounds the GLOBAL shift from its actual zero-exterior
force. The theorem has no unintegrated rough field. It cannot be applied to
a rough fine mean after complex deformation merely by citing RF/RC.

Likewise, at complex V a fixed physical cap centered at U0(Vbar) and an
a-chart transported by U0(V) are different chains. This note does not
identify them. A complex coarse extension would need its own fixed-center
local perturbation, critical prefactor and domain identity. Fixed REAL Vbar
with complex original epsilon is the full domain of the present result.

All-Q-good, the original-a product chart, the old white Omega, G and the
original chi_cut remain distinct. Choosing r_a inside the old cut/G margins
can give their established inclusions, not equalities. No inherited history,
future-conditioned kernel product, effective Wilson replacement or new
gauge quotient is introduced. Continuum existence, non-freeness and a
positive physical continuum mass gap remain OPEN.

## 10. Prior-art mapping, source boundaries and review

The read source comparison was on the actual statement: SC retains a
smaller joint block chord cap; RF/RC prove regional original-a link charts;
SH explicitly distinguishes the cap geometry; MR changes active regions
and their full prefactors. None is used as an existing mixed-cut theorem.
[SN](SHIFTED_NONLINEAR_READER_RETURN_ASTRA.md) and
[NR](NONLINEAR_READER_RETURN_ASTRA.md) supply the shape-independent
normalized Gaussian list/forest mechanism.
[NC](NONLINEAR_CHART_ACTIVITY_ASTRA.md) supplies the actual local
Taylor/Mayer/parity families.
The changed steps proved here are principal-component cap geometry,
block-body Stokes, full-block activation and dimension costs, stronger
global shift margins, and canonical body-mask agreement. The separate
[boundary-forest unit](CHART_BOUNDARY_FOREST_ASTRA.md)'s repeated weak
differentiation of link-ball indicators is not silently extended to this
cap; MC26 leaves the hard bodies undifferentiated.

The external comparison uses primary sources only for attribution and to
identify hypothesis mismatches; no external theorem supplies a missing
proof step. [Dimock, arXiv:1212.5562v2](https://arxiv.org/html/1212.5562v2),
sections 3.13--3.14, localizes the integrand before its cluster expansion in
scalar phi-four on a d=3 torus. Its characteristic-function and hole framework
is architectural context; its fields, dynamics and covariance are not MC1's.
[Lohmann, arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1), section
2.1.4, Proposition 3 and Remarks 2/10, treats single-scale bosonic/unbounded
spin models and explicitly restricts its cutoff proof to site-product
characteristic functions. Our cap becomes a product only at the level of
original OWNER BLOCKS, each with k coordinates. This explains the activation
and dimension debit. His original normal-covariance and interaction-norm
hypotheses are not identified with our symmetric accretive critical family.
His integration-by-parts cutoff theorem is not invoked: MC17 and
MC21--MC26 rebuild the needed boundary and Gaussian statements.

Bałaban's [Large field renormalization II](https://doi.org/10.1007/BF01238433),
CMP 122 (1989), 355--392, concerns the large-field R-operation and
four-dimensional pure-gauge ultraviolet stability. Its publisher abstract
and bibliographic record were consulted; the full paper was not recovered
from the publisher's subscription preview. No uninspected estimate is a
premise, and no ultraviolet stability statement is identified with the
full continuum existence-and-physical-gap goal.

The alternative analytic-Morse-coordinate route was considered but not used:
it would require retaining a nonlinear Jacobian and transformed phase, while
the larger original chart would keep another boundary shape. The direct
block-body method supplies an exact identity without either change. This is
a bounded positive theorem on explicit hypotheses, not a no-go or a claim
that other routes fail. The compact marked-expectation interface in section 9
is strictly beyond the pure-chart statement proved here.

Methodology is pinned at `01589af3faf806b736c42dc2f3bd625e9edead9f`; the
actual [PROCESS_LIGHT](PROCESS_LIGHT.md) governs this lane. No numerical
science experiment or additional worker is used. Source freeze precedes
compact [read provenance](checks/mixed_cap_chart_read_manifest.json) and
[author receipt](checks/mixed_cap_chart_receipt.json). Those records certify
reads and mechanical source checks only. A fresh hostile independent review
must examine the actual cap branch, full-block activation, all dimensions,
global shift window, canonical mask cancellation and exact object scope.
The coordinator owns that review and all Git, PR, shared-front and audit
operations. This author assigns no independent LAND or audit-ratified grade.
