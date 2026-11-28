State of attack
==============

**Gap; honest stop: the total-action shell estimate
(E-SHELL), or its direct weighted consequence (WAM), below.** FALL permits
an error proportional to the sampled weight rate times total energy. This
allows a weaker shell target than a comparison of excess variances. The
scalar implication and the two-site/two-scale tests below are written
arguments. The same far-tail slab that obstructed arbitrary weights has a
depth-uniform slow-weight total-energy comparison, proved in Section 4.
The required four-dimensional nonlinear seam estimate is still missing;
even the general four-dimensional linear seam norm is not supplied by the
slab calculation. END, SEC-unif, TRIAL-J and the original SHELL retain
their source labels. No claim that any of them is false is made.

Pinned source: `f3aa2a8c5a14f737c324fb1a4bbd6097495488bf`.
Author: OpenAI Codex, 2026-11-01. This is bounded author work, not an
independent check or audit. No numerical computation has been run. The
Theorem EX proofs are inputs and are not being revised.

**Unchecked outside this task.** The other FALL inputs (class-minimum
identification, energy/cubic decay, and the relevant source/response
estimates for DS) do not become proved by a scalar recurrence. The required
upper coefficient may depend on the fixed block side L and fixed weight
parameters; it must be free of x, depth, volume, position and multiplication
of the weight by a positive constant.

## 1. Exactly what FALL consumes

**Discharged: notation and telescoping algebra.** Fix L, a top level k,
and one chain V_j, with V_0=U. FALL states nu<=delta/4; the common mapped
family also imposes nu<=min(nu_0,delta_#/8,1/8). Keep any required inverse
moment margin as well. In top physical coordinates extend log w by
ell(z)=min_y[log w(y)+nu d(z,y)], with y ranging over top sites.
At a top site z the Lipschitz inequality makes every term >=log w(z),
and y=z gives equality. The triangle inequality gives
ell(z)<=ell(z')+nu d(z,z'); interchange z,z' for the reverse bound.
Thus this is a Lipschitz extension with the same constant. Sample exp ell
at every level. Write w_j for these samples and nu_j=nu L^(j-k). Put

    E_j = E_j(V_j;w_j),       a_j = I_j^grad(V_j;w_j),
    Y_l = E_0-E_l,           T_l = sum_(j=1)^l a_j,   T_0=0.

Then e_(j-1)=E_(j-1)-E_j gives Y_l=sum_(j=1)^l e_(j-1) exactly.
This is the weighted algebra of (TS), independently of the proof that the
chosen fields are nested class minimizers. That identification is a
separate premise when minimality is used below.

**Unchecked inputs, carried from the consumer.** The scalar proof needs
the following estimates, uniformly over the allowed chains and weights:

    e_(j-1) >= c a_j - b_j,             c>0,
    b_j <= D_EX(L)(f_j+nu_j)E_j + tau_j,
    f_j <= theta^(k-j) f,               0<theta<1,
    E_j <= C_E(L)E_k,
    tau_j <= C_tau(L) theta_tau^(k-j) tau_k,  0<theta_tau<1. (INPUT)

Here f=f_k, tau_j>=0, and the energies and gradients use the same sampled
convention. If the no-toron EX-loc version is used, tau may be zero.
EX-loc itself is a supplied proved input; this display records the
consumer-level packaging of its cubic and weight errors, and the separate
flux/energy/tail premises. This note does not certify those other premises.
In particular, "Gronwall" in the consumer is not treated here as a proof of
the displayed C_E bound.

**Gap: the sufficient upper estimate being attacked.** It is enough to
prove, at every partial top 1<=l<=k,

    Y_l <= C_TOP(L) a_l
              + D_TOP(L)[(f_l+nu_l)E_l+tau_l].             (UP)

Only the upper sign is needed. C_TOP need not be absolute in L. No
hierarchical variance comparison, relative logarithm estimate, or
derivative of the minimizer occurs in (UP). It suffices on the positive
slow profiles actually used by FALL/DS, with their required fixed
enlargements absorbed into the constants. It need not hold for indicators.

**Discharged bookkeeping; implication for applying the supplied estimates.**
Compatible down-averages are convex averages of samples within a fixed
top-cell distance R_w: one-step support radii sum to at most a fixed
multiple of sum_(m>=0) L^-m. Thus, when restarted from w_l,

    exp(-R_w nu_l) w_j <= W_j^q <= exp(R_w nu_l) w_j.

This is a support bound, not a shrinking edge-jump claim for W_j^q.
Positive energies can be compared using it. For the signed excess it gives

    Y_l^sample <= exp(R_w nu_l) Y_l^compatible
                         +(exp(R_w nu_l)-1)E_l.

Indeed compare the positive fine energy first, then subtract E_l. The
last term is <=R_w exp(R_w nu_*) nu_l E_l for nu_l<=nu_*.
On one step the reverse energy comparison gives
e_sample >= exp(-R_w nu_j)e_compatible
                   -(1-exp(-R_w nu_j))E_j.
These are precisely the allowed weight-energy errors. A fixed enlargement
has w^+<=C_w w by the same Lipschitz comparison (or by summing the
kernel's exponential moment). No such comparison is iterated at every
depth for already compatible descendants.

**Implication, proved: (INPUT)+(UP) give the FALL used by DS.** Set

    B = a_k+(f+nu)E_k+tau_k,
    F_l = sum_(j=1)^l b_j,
    G_l = D_TOP[(f_l+nu_l)E_l+tau_l],
    sigma = max(theta,1/L,theta_tau) < 1.

Summing the first inequality in (INPUT) gives c T_l<=Y_l+F_l.
The geometric sums in (INPUT) give

    F_l+G_l <= D_0(L) sigma^(k-l) B,

where, for example, one may take

    D_0 = D_EX C_E[(1-theta)^-1+(1-1/L)^-1]
          +C_tau/(1-theta_tau)+D_TOP(2C_E+C_tau).

Enlarge C_TOP to C>=max(C_TOP,2c). Since a_l=T_l-T_(l-1),

    T_(l-1) <= q_h T_l + (D_0/C) sigma^(k-l)B,
    q_h = 1-c/C in [1/2,1),
    T_k <= (C+D_0)B/c.                                    (HF)

Induction on m now gives

    T_(k-m) <= q_h^m T_k
                 +(D_0/C)B sum_(r=0)^(m-1) q_h^(m-1-r)sigma^r.

Let r_0=max(q_h,sigma), choose q_bar=(1+r_0)/2, and put t=r_0/q_bar<1.
The sum is <=m r_0^(m-1)<=q_bar^(m-1)/(1-t)^2. The last inequality
follows from m t^(m-1)<=sum_(h>=1)h t^(h-1)=(1-t)^-2;
the series identity is the product of two geometric series. Therefore

    sum_(m'=m)^(k-1) I^grad_(k-m')(V_(k-m');w_(k-m'))
        = T_(k-m) <= C_F(L) q_bar^m B,
    C_F = (C+D_0)/c + D_0/[C q_bar(1-r_0/q_bar)^2].         (FALL-1)

This includes equal contraction/forcing rates. All constants are finite
at fixed L. There is no bare level-0 gradient in this sum: DS uses
Z_(k-m-1) at arguments of levels 1 through k. The stronger endpoint
claim is not a consequence of (HF). Also cub(V_j;w_j)<=f_j E_j by the
pointwise inequality |theta|^3<=f_j |theta|^2, so (INPUT) gives its
geometric decay separately. SRC, CRUDE and the spatial-rate/domain
requirements of DS remain additional inputs.

## 2. The weaker comparison and tests fixed before the calculation

**Gap: proposed direct comparison.** Write A_X(w) for the normalized
Wilson action of a fine field X, with the same sampled fine weight w.
Let T be the specified admissible trial and U the class minimizer with
the same terminal parent. Instead of comparing their variances, try

    A_U(w) <= [1+D_A(L) nu_l] A_T(w)                       (WAM)

at every partial top l and every allowed sampled rate 0<=nu_l<=nu_*.
The coefficient must be uniform over that whole interval, including the
limit at zero, and over x, depth, volume, position, sectors and weight
normalization. At nu_l=0 it is the unweighted variational comparison,
conditional on the class-minimum identification. There is no assertion
here that (WAM) follows from that single endpoint.

**Discharged test criteria, set before the following calculations.**
Test the homogeneous quadratic analogue with arbitrarily small field
amplitude. A ratio exceeding 1+D nu for every depth-independent D
would kill this route. A ratio 1+O(nu) or 1+O(nu^2), uniformly in
depth and volume, survives this test but proves no nonlinear claim.
Keep a distant-site version to test whether locality is indispensable.
No numerical computation is used.

**Discharged two-site calculation.** Minimize u_1^2+u_2^2 subject to
u_1+u_2=a. Completing the square gives u_*=(a/2,a/2). An arbitrary
trial is t=(a/2+s,a/2-s). For weights w_1,w_2>0 the weighted trial
energy has minimum a^2/(w_1^-1+w_2^-1): this follows by completing
the square in s, or by Cauchy--Schwarz with equality t_i proportional
to w_i^-1. Consequently, for every trial in this fibre,

    E_w(u_*)/E_w(t) <= (w_1+w_2)(w_1^-1+w_2^-1)/4
                     = cosh^2((log w_2-log w_1)/2).

Equality is achieved by that weighted minimizing trial. At sites of
distance d, the slow-weight condition bounds the ratio by cosh^2(nu d/2).
For these ratio formulas take a!=0; at a=0 the minimizing energy is
zero and the desired inequality holds directly, without division.
The possible excess over trial energy is quadratic in the amplitude;
it cannot be paid by a cubic-only error. For d=1,
cosh^2(nu/2)-1=sinh^2(nu/2)<=nu^2 cosh^2(nu_*/2)/4,
using sinh z=integral_0^z cosh t dt<=z cosh z for z>=0.
Thus this obstruction is paid by the permitted nu E error. If d=R
can grow, the ratio is unbounded at fixed nu: locality is essential.
This is a test of an inference, not a Yang--Mills counterexample.

**Discharged two-scale and arbitrary-depth tensor test.** Index N=2^n
coordinates by epsilon in {0,1}^n, impose sum u_epsilon=a, and minimize
sum u_epsilon^2. The minimizer is a/N in each coordinate, by
sum(u_epsilon-a/N)^2=sum u_epsilon^2-a^2/N. Place the coordinates at
x_epsilon=sum_(j=0)^(n-1) epsilon_j L^-j and take w=exp(nu x).
These are samples of one log-Lipschitz profile. The same weighted
Cauchy--Schwarz calculation gives the exact worst trial ratio

    (sum w)(sum w^-1)/N^2
       = product_(j=0)^(n-1) cosh^2(nu L^-j/2)
       <= exp[nu^2/(4(1-L^-2))].                          (TENSOR)

The product identity follows by distributing each binary sum into its
n two-term factors. For the bound, tanh z<=z follows because
(z-tanh z)'=tanh^2 z>=0 and both vanish at zero. Integrating gives
log cosh z<=z^2/2. Summing the geometric series proves (TENSOR).
For 0<=nu<=nu_* its excess over 1 is <=C(L,nu_*)nu^2, since
exp v-1=integral_0^v exp t dt<=v exp v. This includes n=2, has no
depth growth, and is independent of a and weight normalization.
It tests sampled scales, not compatible descendants with persistent
jumps, and is only a linear constrained model.

## 3. A total-energy shell budget would suffice

**Gap: concrete replacement for the earlier variance SHELL.** Work in
top-l units but index the fine plaquette anchors, summing orientations
at each anchor. Let A_X(D) be the nonnegative Wilson action density
of X summed on D. Put S_r(D)=D^(+r) minus D^(-r). A sufficient
localized variational estimate, for every superlevel set D of the
sampled scalar weights, is

    A_U(D)-A_T(D)
       <= A_s(L)[A_U(K*1_(S_r(D)))
                              +A_T(K*1_(S_r(D)))].        (E-SHELL)

Here r<infinity is measured in top units, K is a symmetric nonnegative
probability kernel on the periodic fine anchors, and
M_*:=sup_(depth,volume) sum_z K(z)exp(nu_* d(z,0))<infinity.
The radius, coefficient and moment must be uniform in depth and volume;
they may depend on L and the fixed rate parameters. Delta at zero is
allowed for K; nonlinear correction tails require their actual kernel.
The estimate must concern the normalized action for which U is minimal.
It charges the full quadratic energy at the seam. It does not require
the hierarchy/transport identification CJ/CR or a relative fibre chart.

**Implication, proved: (E-SHELL) gives (WAM) at a stated rate.** For
D_t={w>t}, layer integration gives integral 1_(D_t)dt=w and

    integral 1_(S_r(D_t))dt = w_r^+-w_r^-
        <= 2 sinh(nu_l r)w,
    K*w <= M_* w.

The first equality follows because a point belongs to D_t^(+r)
exactly for t<max_(d<=r)w, and to D_t^(-r) exactly for
t<min_(d<=r)w, apart from irrelevant equality endpoints. The bounds
follow from exp(-nu_l r)w<=w_r^-<=w_r^+<=exp(nu_l r)w and the
triangle inequality for log w. All sums are finite, so integration
commutes with sums. Symmetry of K allows its transfer onto w. Hence

    A_U(w)-A_T(w) <= beta(nu_l)[A_U(w)+A_T(w)],
    beta(s)=2A_s M_* sinh(sr) <= b_s s,
    b_s=2A_s M_* r cosh(nu_* r).

If b_s nu_*<=1/2, division by 1-beta is legitimate and

    A_U(w) <= [(1+beta)/(1-beta)] A_T(w)
             <= [1+4b_s nu_l] A_T(w).                    (WAM-shell)

The second inequality uses 2beta/(1-beta)<=4beta. Thus D_A=4b_s.
This is an explicit rate condition, not permission to absorb an
arbitrary C(L) at the consumer's already fixed spatial rate. If it
fails there, this shell argument proves only the smaller-rate result;
the required consumer-rate result stays open. A direct proof of (WAM)
at that rate would avoid this absorption condition.

**Implication, proved: (WAM) gives (UP) with named inputs.** Assume the
trial/class premises of TR-SLOW and its sampled conversion give

    E_T(w_0)-E_l <= A_t(L)a_l+B_t(L)(f_l+nu_l)E_l.          (TR)

The four forward covariant differences obey
|Ad(V)theta(x+e)-theta(x)|^2<=2|theta(x+e)|^2+2|theta(x)|^2.
Shift the first sum and use w_l(x-e)<=exp(nu_*)w_l(x). Then

    a_l <= C_g E_l,       C_g=8(1+exp(nu_*)),
    E_T(w_0) <= K_t E_l,
    K_t=1+A_t C_g+B_t(f_*+nu_*),                           (ET)

for f_l<=f_*<=1. This is a direct energy bound on the trial.

For completeness the action-to-angle conversion is elementary in SU(2).
For X=i a.sigma, t=|a|, the Pauli anticommutation identities give
X^2=-t^2 I. Grouping even and odd powers in exp X gives trace(exp X)=2 cos t.
In the normalization with quadratic term t^2, a plaquette's action is
therefore 2(1-cos t). For t>=0,
0<=t-sin t=integral_0^t(1-cos s)ds<=t^3/6, since
1-cos s=2 sin^2(s/2)<=s^2/2; |sin u|<=|u| follows by integrating
cos u and using |cos u|<=1. Integrating once more gives

    0 <= t^2-2(1-cos t) <= t^4/12.

The functions are even, so the estimate holds for signed t as well.
Assume, as an additional field premise, flux(U)<=C_f(L) f_l.
Put c_w=C_f(L)^2/12 and choose f_* with c_w f_*^2<=1/2.
Then E_U<=(1+2c_w f_l^2)A_U, because (1-z)^-1<=1+2z
for 0<=z<=1/2. Also A_T<=E_T. Combining with (WAM) gives

    E_U-E_l <= A_t a_l+B_t(f_l+nu_l)E_l
       +K_t[D_A nu_l+2c_w(1+D_A nu_*) f_l^2]E_l.

Since f_l^2<=f_l, this is (UP), with, for example,

    C_TOP=A_t,
    D_TOP=B_t+K_t[D_A+2c_w(1+D_A nu_*)].                   (UP-constants)

Adding a nonnegative tau term only weakens it. Thus a full-energy seam
estimate can suffice for FALL even though it need not give the original
variance SHELL, END, SEC-unif, TRIAL-J or HC-W. The implication uses
(TR), class admissibility/minimality and the displayed flux premise;
it does not discharge them.

## 4. Linear slab test and the actual missing nonlinear step

### 4.1 The old far-tail model satisfies the weaker bound at every depth

**Discharged: a written linear lemma.** Let B=L^n, L odd >=3, and use
a periodic line with M>=4 coarse cells and MB fine sites. Define

    (Q_B A)(j) = sum_(a=-(B-1)/2)^((B-1)/2) A(jB+a),
    F(x)=A(x+1)-A(x),
    (C_B F)(j)=sum_x t_j(x)F(x),
    t_j(x)=#{(a,s): |a|<=(B-1)/2, 0<=s<B, x=jB+a+s}.

These are the path-average and curvature constraints of the commuting
slab model. Indeed Q_B A(j+1)-Q_B A(j) is the sum of the B telescoping
increments at each of the B values of a, giving C_B F. Composing the
centered Q_L n times gives Q_B: the offsets are
sum_(h=0)^(n-1) L^h a_h with |a_h|<=(L-1)/2. Induction shows that
they cover every integer from -(B-1)/2 to (B-1)/2 once, since consecutive
translated intervals of length L^(n-1) meet without overlap or gaps.
This identifies the two scales without a depth-dependent coefficient.

The triangular row t_j is 1,2,...,B,...,2,1. It has sum B^2;
the column sum is B (the two adjacent triangles add to B).
Only adjacent rows overlap, so, with S the cyclic shift,

    G=C_B C_B^* = a_B I+b_B(S+S^-1),
    a_B=(2B^3+B)/3,      b_B=(B^3-B)/6,
    2b_B/a_B < 1/2.                                      (GRAM)

To verify the coefficients, the diagonal is
B^2+2 sum_(h=1)^(B-1) h^2 and the adjacent overlap is
sum_(h=1)^(B-1) h(B-h). Use sum_(h=1)^m h=m(m+1)/2 and
sum_(h=1)^m h^2=m(m+1)(2m+1)/6; both formulas follow by induction,
since the difference at m and m-1 is respectively m and m^2.
The displayed inequality follows by multiplying by 2B^3+B>0.

G is positive definite: its quadratic form is at least
(a_B-2b_B)sum v_j^2, by 2|v_j v_(j+1)|<=v_j^2+v_(j+1)^2.
For any trial F_t with C_B F_t=b, the unique least-energy solution is

    F_* = R F_t,       R=C_B^* G^-1 C_B.

It satisfies the constraint and is orthogonal to ker C_B, so every
other solution has energy ||F_*||^2+||F-F_*||^2. Also R^*=R and
R^2=R, hence ||R||_(2->2)<=1: ||Rv||^2=<v,Rv><=||v|| ||Rv||.
If sum b=0, then B sum F_*=sum C_B F_*=0, so F_* integrates to a
periodic potential. Q_B A then differs from a prescribed potential
with curl b by a constant; adjusting A by a constant fixes it, since
Q_B of that constant is B times it. Thus no scalar potential constraint
is lost in this calculation. It is not a proof for general four-dimensional
fields or for nonlinear SU(2).

**Discharged: uniform kernel moment, including the fine-site count.**
Let d_B(x,y) be fine-site distance divided by B, and d_c the coarse
cyclic distance. Choose s=(log 2)/2 and 0<nu_*<=s. The Neumann
series for G^-1 has its h-th term supported at coarse distance <=h,
with absolute row sum <=a_B^-1(2b_B/a_B)^h. Consequently

    sup_i sum_j |(G^-1)_(ij)| exp(s d_c(i,j))
        <= a_B^-1/(1-exp(s)/2).

This follows by summing a convergent geometric series; multiplying its
partial sums by G leaves a remainder with norm tending to zero.
If t_i(x)t_j(y)>0, then d_B(x,y)<=2+d_c(i,j)+2. The row and column
sums of C_B stated above therefore give

    sup_x sum_y |R_(xy)| exp(s d_B(x,y))
        <= exp(4s) B^3/[a_B(1-exp(s)/2)]
        <= C_s := (3/2)exp(4s)/(1-exp(s)/2).               (MOM)

The column bound is the same by symmetry. This accounts explicitly for
the increasing number of fine sites. It is uniform in B, n, L and M.
Periodicity is harmless: distance traveled in h cyclic nearest-neighbor
steps is at most h, and the same triangle inequality applies across
the seam. With

    D_s = C_s/(s-nu_*/2),

the row and column sums of |R_(xy)|d_B(x,y)exp(nu_* d_B(x,y)/2)
are at most D_s. This uses
d exp(nu_* d/2)<=exp(s d)/(s-nu_*/2), which follows from
z<=exp z for z>=0.

**Discharged: direct weighted comparison in this model.** Let w>0
have log-Lipschitz rate nu<=nu_* in d_B, and let W be its diagonal
matrix. Put

    W^(1/2) R W^(-1/2) = R+J,
    J_(xy) = [(w(x)/w(y))^(1/2)-1]R_(xy).

By exp v-1=integral_0^v exp t dt,

    |J_(xy)| <= (nu/2)d_B(x,y)exp(nu d_B(x,y)/2)|R_(xy)|.

Its row and column absolute sums are <=nu D_s/2. The operator norm
has the same bound: apply
|sum_y J_(xy)v_y|^2 <=(sum_y|J_(xy)|)sum_y|J_(xy)||v_y|^2
and then sum over x. The triangle inequality with ||R||<=1 now proves

    E_w(F_*) <= (1+nu D_s/2)^2 E_w(F_t)
       <= [1+D_lin nu]E_w(F_t),
    D_lin=D_s+nu_* D_s^2/4.                               (WAM-slab)

D_lin is independent of L, depth, volume, position, data amplitude
and weight normalization. It depends on the chosen rate margin.
No search, floating-point computation, or enumeration establishes any
step here. This proves the weaker comparison in the explicit slab
model that previously had a nonzero linear far tail. It does not prove
the nonlinear comparison or (E-SHELL), even in the slab.

### 4.2 Where the four-dimensional variational attempt actually stops

**Discharged finite linear algebra; its needed norm bound is a gap.**
At the trivial field let Q_n be the true composite linear parent map,
T_n a linear right inverse, A_* a Maxwell minimizer, A_t=T_n v and
H=A_t-A_*. For bond, plaquette and parent cutoffs chi_b, chi_p, chi_c
with the same core and exterior, put

    D_chi=chi_b H-T_n Q_n chi_b H,
    A_chi=A_*+D_chi.

Since Q_n H=0 and Q_n T_n=I, Q_n D_chi=0. With
[d,chi]=d chi_b-chi_p d and [Q_n,chi]=Q_n chi_b-chi_c Q_n,
the exact curvature identity is

    d A_chi=(1-chi_p)d A_*+chi_p d A_t+R_chi,
    R_chi=[d,chi]H-d T_n[Q_n,chi]H.                       (SEAM)

Thus the specific additional linear estimate sought is a parent-fixed
choice of endpoint representatives and cutoffs for which

    sum_p |R_chi(p)|^2
       <= C_seam(L) sum_p (K*1_(S_r(D)))(p)
                            [|dA_*(p)|^2+|dA_t(p)|^2],   (LC)

with all affected stencils/tails included, and with the same uniform
top-unit radius and kernel moment as above. For compactly supported
linear corrections, support lies in a fixed enlarged shell; (LC)
then bounds the shell action using |v+r|^2<=2|v|^2+2|r|^2 and
|(1-chi)u+chi t|^2<=(1-chi)|u|^2+chi|t|^2 for 0<=chi<=1.
Global minimality converts that shell action bound into (E-SHELL),
with the enlarged shell and a changed fixed coefficient. These two
elementary inequalities follow respectively from 2|v||r|<=|v|^2+|r|^2
and subtraction of chi(1-chi)|u-t|^2.

The slab moment argument controls R's weighted operator in its scalar
curvature space; it does not estimate this four-dimensional R_chi.
The commutator [Q_n,chi]H is first order: for Q(h_1,h_2)=(h_1+h_2)/2,
H=(t,-t), chi_b=(1,0), it is t/2 although QH=0. It cannot be
replaced by the trial correction's quadratic flux source. Neither the
local support of T_n nor the existence of a finite-dimensional inverse
supplies (LC). In particular H is a relative connection, and controlling
it by the two endpoint curvatures in a parent-fixed gauge is an
unproved local estimate here.

**Gap: exact nonlinear seam statement.** For every depth n, allowed
parent V, specified U and T, and relevant D, construct an admissible
field X_D with M_n(X_D)=V and every intermediate image in the defining
class. Let a_X(p) be its normalized nonnegative
Wilson plaquette density, and define the complete replacement cost

    R_D = sum_(p in D)[a_X_D(p)-a_T(p)]
                +sum_(p outside D)[a_X_D(p)-a_U(p)].

The missing estimate, including any failure of exact agreement caused
by correction tails, is

    R_D <= A_s(L) sum_p (K*1_(S_r(D)))(p)
                                  [a_U(p)+a_T(p)].        (GLUE-E)

Indeed A(X_D)-A(U)=R_D-[A_U(D)-A_T(D)]; class minimality makes
the left side nonnegative and gives (E-SHELL). This calculation
specifies exactly what the nonlinear construction must pay. Its
uniform parameters must also meet b_s nu_*<=1/2 for this route to
give (WAM) at the required consumer rate. Alternatively a direct
proof of (WAM) with finite D_A at that rate would suffice without
(GLUE-E). Neither estimate is established in this note.

**Unchecked source applicability; no promotion of a tangent estimate.**
Theorem F in `fibre-propagator.md` gives its weighted tangent inverse
at the actual lift under its own hypotheses. Its hostile point (6')
explicitly requires the box L^4 curvature and nested-contour control
of R3, not just an Eps ball. This note has not checked those proofs,
constructed a genuine finite nonlinear interpolation, or controlled
its conversion to the true parent-fixed fibre. F therefore is not a
justification here for replacing the scalar R in (WAM-slab) by a
nonlinear energy projection, or for asserting (GLUE-E). The known
finite TRUE-CH construction likewise supplies no uniform endpoint
or seam estimate. No new failure of F or of END is asserted.

## 5. Constants, scope and final disposition

**Discharged dependency accounting; mathematical inputs keep their labels.**
Every consumer constant below must be independent of x, depth, volume,
position, sector and multiplication of w by a positive scalar. Dependence
on dimension four, SU(2), the fixed blocking profiles and fixed positive
rate margins is allowed. The table adds the dependence on L.

| Quantity | Dependence on L and exact role | Label |
|---|---|---|
| C_TOP, D_TOP in (UP) | Finite dependence on L is allowed by FALL; formulas (UP-constants) are conditional | implication |
| C_E, D_EX, theta, C_tau, theta_tau, trial A_t and B_t, C_f | May depend on fixed L and rate parameters; must satisfy (INPUT), (TR) and the stated fine-flux bound uniformly | unchecked inputs |
| A_s, C_seam, r, M_* | May depend on L, but not on the number of scales; r is in current top units and M_* is a supremum over depths/volumes | gap |
| b_s, D_A | b_s=2A_s M_* r cosh(nu_* r), D_A=4b_s if b_s nu_*<=1/2; otherwise no consumer-rate conclusion from this shell proof | implication |
| f_* | Choose after L and the preceding constants, with f_*<=1, c_w f_*^2<=1/2 and all inherited trial/class thresholds | conditional choice |
| q_bar, C_F | Explicit in (HF)/(FALL-1); may depend on L and the fixed inputs; no uniform separation of q_bar from 1 as L grows is needed | implication |
| D_lin | Explicit in (WAM-slab); free of L as well as depth and volume for that linear model only | discharged |

If the consumer has already fixed nu_req>0, the (GLUE-E) route must
establish its moment at least through nu_req and check b_s nu_req<=1/2.
Choosing nu_*<nu_req does not prove that consumer's statement. A
separately authorized choice of a smaller DS profile would also need
its other spatial rates adjusted and checked; no such adjustment is
made here. All weighted estimates in this note are homogeneous, so no
constant depends on weight normalization. The normalized action removes
the common coupling factor x; no x-dependent coefficient is used to
hide a linear or quadratic cost.

**Unchecked/read boundary and mechanical verification.** Read at the
pinned commit: GOAL; FINISH's independence, efficiency and rules sections;
the excess part's Summary, Sections 3, 6 and Obligations, plus the
setting/weight statements and trial-bound statement needed here; all three
requested continuation/stop notes; sector-values' (TS), TOP, FALL and
the DS consumer ranges; and fibre-propagator's setting, Theorem F and
(6'). Theorem EX proofs were not changed or re-certified. Source
mathematics outside the written model/implication proofs in this note
retains its earlier labels. Initial large search outputs were only
locators; consequential ranges were reread without truncation. The
workflow was read from pinned HEAD because it is absent in this sparse
working tree. Relevant physics-loop instructions were inspected within
the user's explicit bounded scope. No independent-side files, forbidden
library files, gates, external proof accounts or historical numeric logs
were opened. Numerical claims occurring incidentally in permitted source
excerpts are not evidence for anything discharged here.

Only `library/excess-shell-end.md` was written. No numeric job, numeric
lock acquisition, numerical script, subagent, audit, commit, push or post
was used.
Scope/whitespace checks are mechanical checks, not independent mathematical
verification. This note has no independent review or retained status.

**Discharged, what is proved.** The scalar implication (INPUT)+(UP)
implies exactly the levels-1-through-k FALL needed by DS, with explicit
depth-uniform constants. The local two-site/two-scale tests and the
all-depth scalar slab bound (WAM-slab) are written proofs. The latter
shows that the earlier linear far-tail obstruction does not kill this
weaker slow-weight, total-energy route. No numerical computation was run.

**Implication, conditional on exactly what.** An admissible nonlinear
replacement satisfying (GLUE-E), plus its kernel-moment and rate condition,
implies (E-SHELL) and then (WAM). A direct (WAM) proof could replace these.
Either way, (TR), its class/minimality identification and thresholds, and
flux(U)<=C_f(L)f_l give (UP) via (UP-constants). Finally (INPUT) gives
(FALL-1). This route does not use hierarchical CJ/CR or HC-W, and does
not imply or discharge END, SEC-unif or TRIAL-J. Those remain gaps;
the carried all-depth CJ/CR statements remain unchecked. DS still has
its source, derivative, tail, domain and spatial-rate premises.

**Gap, what is still open.** No uniform (GLUE-E), (E-SHELL), (WAM), or
(UP) for the actual nonlinear four-dimensional class chain has been
proved. The exact missing estimate in the attempted construction is
(GLUE-E), with A_s(L), r(L), M_*(L) uniform in all the variables listed
above and with its displayed absorption condition at the required rate.
Even the general four-dimensional linear estimate (LC) has not been
derived here. A concrete next step is a parent-fixed localized construction
proving (LC) and then controlling its nonlinear correction and admissible
descendants; the successful slab calculation cannot replace that step.
This is a named gap, not a counterexample to TOP-W, END or Yang--Mills.
