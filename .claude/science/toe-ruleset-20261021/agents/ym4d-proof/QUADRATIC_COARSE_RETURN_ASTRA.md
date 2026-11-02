# A quadratic coarse debit for the actual local compact/chart ratio

This extends the coarse domain of the actual coefficient in
[SC](SOURCE_LOCAL_COMPACT_RETURN_ASTRA.md), frozen at SHA256
c39e78ac1d31024d5266e16ace022fa86497a6d09c45aa25b215ffa390533dff.
It replaces SC22--SC24's linear coarse debit by a quadratic one, leaving
SC's original compact numerator, fixed selectors and actual regional chart
denominator intact. The permitted coarse radius becomes a fixed constant
times sqrt(q)/K^2, with the same local suppression exponent as SC30.

The new ingredients are an original-energy bound on the mean-spread
deficit, and a local mixed-derivative estimate for the full Haar-inclusive
critical action with physical exterior links fixed. No numerical experiment
or external theorem is needed for these steps. SC's reviewed status is
provenance; its stated mathematical interface is checked below. This new
author proposition requires fresh independent review.

Credit for the constructive antecedents remains with Bałaban and Dimock.
No theorem from their work is imported into this argument.

~~~yaml
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
~~~

## 1. One actual model, one regional family and the unchanged coefficient

Use [CS](CUT_SECTOR_COERCIVITY_ASTRA.md)1--CS12 and
[OC](OUTSIDE_CHART_RETURN_ASTRA.md)1--OC13, with SC's precise shell
partition. Retain ONE ambient radius R_amb, beta=(16R_amb)^(-4), and the
same complete-reader [RF](REGIONAL_CRITICAL_FIELD_ASTRA.md) /
[RC](REGIONAL_CHART_RETURN_ASTRA.md) construction, including both covariance
tails, all membership readers and its actual principal regional matrices.
R_amb is distinct from an integrated block region R below. Preliminary
ceilings are restricted jointly in section 3, before final chart/data
radii; no two independently built atom families are identified.

Fix N>=2, odd L>=3, T>=2, u>=N, kappa in [kappa_-,kappa_+], and

    sigma^2=N/u, D=N^2-1, m0=3L^4+1, n0=D m0.
    w_epsilon(U,V)=exp[-u sum_p(1+epsilon_p)s(U_p)]
                    product_c k_(kappa u)(V_c;M_c(U)),
    s(P)=||I-P||HS^2/(2N),
    k_t(V;M)=exp[t h(V;M)]/Z_t(M),
    h(V;M)=Re tr(V^* M)/N,
    M_c=(24L^4)^(-1) sum_tau P_(c,tau)(U).                 (QC1)

Every original paired word, of length at most 5L, is used. For complex
coarse data, h means the forward/backward holomorphic continuation, not a
real-part operation on complex arguments. Compact numerator fine inputs
always remain real. Their original positive Z_t(M) never changes with V.
The root-pinned tree quotient has probability Haar measure on every free
whole link; nonroot gauge volumes are one. All D colour coordinates remain.

For a block set R, J_R consists of all free links owned by R. P_R and C_R
are ALL original plaquettes and kernels whose full field stencils meet J_R.
Then |J_R|=m0|R|, |P_R|<=6m0|R| and |C_R|<=8|R|. Their actual exterior
free-link readers are in N_1(R) minus R. The original hard cut is retained
on its original block-interior plaquettes. G and the original white cube
Omega are not changed or identified with the product chart used below.

At fixed real Vbar, set Q_X=sum_(free f owned X)||U_f-U0_f(Vbar)||HS^2/N
and Q(S)=sum_(X in S)Q_X. Choose rho_0 in (0,1), subject to the common
RF/RC preliminary conditions, and define exactly SC4's constants

    B_fill=30L^2, C_F=8 B_fill^2 L^3(L+20), C_psi=8L^3,
    c=min((1-rho_0)/C_F,kappa_-/C_psi),
    a_bulk=6(1+rho_0)m0,
    a_shell=24(1+rho_0)+4kappa_+(5L)^2,
    alpha=min(1,c/(8a_shell)), g=log(1+alpha),
    K=ceil max(1,(8/g)^2,(2/g)[1+log(2500m0/q)]),
    V_K=(4K+1)^4, r_g=2K+2, S_K=(4K+9)^4.                (QC2)

Take 0<q<=4m0, zeta<=1/4, with
sqrt(q)<=zeta/(8pi sqrt(N)) and sqrt(Nq)<2sin(pi/(2N)).
Thus every q-good exterior link has its actual traceless principal
coordinate bar_y_f=Log[U_f U0_f(Vbar)^(-1)] of HS norm <=zeta/16.
Let A be nonempty and connected in the periodic sup-range-r_g graph.
SC8--SC10's EXACT selector is

    C_A=product_(X in A)1_(Q_X>=q)
           product_(X in N_(r_g)(A) minus A)1_(Q_X<q),
    B_n=N_n(A), I_j=B_(2j), R_j=B_(2j+1),
    S_j=B_(2j+2) minus B_(2j+1),
    pi_Aj=C_A 1_(Q(S_j)<=alpha Q(I_j))
                product_(i<j)1_(Q(S_i)>alpha Q(I_i)), 0<=j<K. (QC3)

The finite shell-growth proof gives sum_j pi_Aj=C_A. ALL predicates,
including every earlier failed shell test and q-good absence test, stay
frozen at Vbar. Set R=R_j, Q_I=Q(I_j), Q_s=Q(S_j). On pi_Aj, for
e=Re epsilon, |epsilon_p|<=rho<=rho_0, and center curvature <=delta,

    E_R^e=sum_(p in P_R)(1+e_p)s(U_p)
                  +kappa sum_(c in C_R)[m(M_c)-h(Vbar_c;M_c)],
    E_R^e>=c Q_I, Q_I>=q|A|, |R|<=V_K|A|,
    A_ref^e<=a_bulk delta^2 |R|+a_shell Q_s,
    a_bulk delta^2 |R|<=c Q_I/8, a_shell Q_s<=c Q_I/8,    (QC4)

where m(M)=max_(Q in SU(N))h(Q;M), A_ref is SC11's actual reset
comparison, and delta^2<=c q/(8a_bulk V_K). These are the local CS
coercivity and OC shell inequalities with their FULL brick supports.
They are not an additional energy price to multiply into the later bound.

For admitted fixed real exterior z, use exactly SC3 and SC25:

    I_R=h_N^(m0|R|) int_(product_(J_R)B_(r_a))
                         exp[-F_R(a;y(V))/sigma^2] da,
    y_f(V)=Log[z_f U0_f(V)^(-1)],
    I_R=h_N^(m0|R|)(2pi sigma^2)^(n0|R|/2)
          det(K_R^*)^(-1/2) exp[-A_R/sigma^2+H_R],
    A_R=F_R(b_R;y(V)), F_R'(b_R;y(V))=0,
    N_Aj=int_(SU(N)^J_R) dH chi_R pi_Aj w_R,epsilon(U,V),
    B_Aj=N_Aj/I_R.                                      (QC5)

F_R contains every touching normalized kernel and the active Haar logs.
K_R^* is its actual full-colour critical Hessian. The determinant branch,
the critical action, h_N and every mode in QC5 are retained. Require
r_a<=epsilon_1/8 and all RC chart restrictions. Outside the exterior
q-good absence event, define B_Aj=0 without evaluating an unadmitted
denominator. Deep exterior compact fields may be arbitrary and fixed.

## 2. The rough numerator: the missing mean-spread cost is payable

For each c use CS8's actual two-block labelled brick and root-straight
word S_c. In particular its T=2 convention retains the chosen common
face and excludes the other periodic seam; distinct coarse labels remain
distinct. With |X|_n=||X||HS/sqrt(N), CS's telescoping/filling gives

    q_c=average_tau |P_(c,tau)-S_c|_n^2
                      <=2 B_fill^2 sum_(p in brick(c))s(U_p),
    1-m(M_c)<=1-|M_c|_n^2<=q_c.                          (QC6)

For clarity, the second line needs no polar choice: averaging the
competitors P_(c,tau) gives m(M)>=|M|_n^2, while variance about S_c
equals 1-|M|_n^2+|M-S_c|_n^2. The first line is the original word filling,
not a bound on a surrogate mean or on independently chosen group angles.

Each fine plaquette lies in at most eight labelled bricks. Every c in C_R
has an endpoint block in R. If p in its brick is NOT in P_R, all its free
inputs are exterior and lie in N_1(R) minus R, hence in S_j. Such a p is
unchanged by the reset. A brick plaquette has U0_p=I: a double-face
plaquette, which could carry a coarse curvature, is not in one brick.
The four-edge product inequality therefore gives

    s(U_p)<=4 sum_(free exterior occurrences f in p)
                                      |U_f-U0_f|_n^2.

Each free edge occurs in six fine plaquettes. Consequently

    sum_(c in C_R) sum_(p in brick(c) minus P_R)s(U_p)
                                                       <=192 Q_s,
    sum_(c in C_R)[1-h(Vbar_c;M_c)]
       <=A_E E_R^e+A_Q Q_s,
    A_E=1/kappa_-+16 B_fill^2/(1-rho_0),
    A_Q=384 B_fill^2.                                    (QC7)

This pays the outside brick plaquettes explicitly. It does not claim that
1-h equals psi=m-h, or that Ntilde_t=e^(-t)Z_t for an arbitrary mean.
The latter identity holds only at a unitary mean with m=1.

Now fix a real fine configuration, put V_c=exp(v_c)Vbar_c, and
max||v_c||HS<=eta<=1. For one real unitary word let Q=P Vbar_c^(-1).
Its holomorphic numerator is tr[exp(-v)Q+Q^(-1)exp(v)]/(2N).
The linear term is tr[v(Q^(-1)-Q)]/(2N). Since
||Q^(-1)-Q||HS<=2||Q-I||HS, averaging and Cauchy--Schwarz give

    |h(V_c;M_c)-h(Vbar_c;M_c)|
      <=sqrt(2/N)||v_c||HS sqrt(1-h(Vbar_c;M_c))
                                  +exp(eta)||v_c||HS^2/(2N). (QC8)

The remainder follows directly from
||v^k||_1<=||v||HS^2 ||v||op^(k-2) and the exponential series.
All forward/backward words are paired before averaging. Thus the original
Z_t(M_c) cancels IDENTICALLY in the comparison of the two numerator
densities. QC7, |C_R|<=8|R| and Young's inequality yield

    |w_R,epsilon(U,V)| <= w_R,e(U,Vbar)
       exp{u[E_R^e/32+(a_shell/4)Q_s+C_num eta^2|R|]},
    C_num=128kappa_+^2 A_E/N
               +16kappa_+^2 A_Q/(N a_shell)+4exp(1)kappa_+/N. (QC9)

Indeed the two linear terms are at most
(4kappa_+/sqrt(N))eta sqrt(|R|)[sqrt(A_E E_R^e)+sqrt(A_Q Q_s)].
Their Young coefficients are respectively 1/32 and a_shell/4.
No fine numerator field was moved into a complex chart or assumed small.

## 3. Fixed local derivative budgets for the actual denominator

The analytic constants in this section are fixed BEFORE q,K,u and the
final tau,zeta,delta,eta. Retain RF's common fine radius a_f0 and local
vacuum-subtracted bound H. Set a_0=min(a_f0,1/4). Choose positive
preliminary ceilings satisfying RF17 and RC's preliminary conditions,
and further require

    bar_tau<=a_0/(64sqrt(D)), bar_zeta<=a_0/4,
    eta_v<=min(a_0/128,1/64, the common local coarse analytic ceiling),
    r_f=a_0/(64D), r_v=eta_v/(4D).                         (QC10)

These restrictions are possible at the same R_amb. Decreasing the final
field/source/data radii restricts the same RF/RC coefficient formulas.
Keep all source and Hessian budgets computed at the fixed preliminary
ceilings; they have no inverse actual-zeta or inverse actual-tau factor.

Use a fixed physical boundary template
z_f=exp(bar_y_f)U0_f(Vbar), and define a LOCAL analytic phase
Phi_R(v,a;bar_y,epsilon) by substituting

    U_e=exp(a_e)U0_e(exp(v)Vbar)      for e in J_R,
    U_f=exp(bar_y_f)U0_f(Vbar)       for touching exterior f,
    Phi_R=-sigma^2 log w_R,epsilon
                         -sigma^2 sum_(e in J_R)log j_N(a_e). (QC11)

Only the touching original vertices occur. This is exactly F_R with
y(V) substituted, including its active Haar factor. The exterior physical
U_f, not its varying logarithm, is held fixed when differentiating v.
All branches are the common RF/RC branches.

Here are explicit margins for local Cauchy estimates. At every actual
critical point, active link HS norms are at most sqrt(D)bar_tau. At the
real center, ||bar_y_f||HS<=bar_zeta/16. Allow all D scalar increments
per fine link of modulus r_f and all D coarse increments of modulus r_v
about max||v_c||HS<=eta_v/2. The fine a,bar_y norms stay below a_0/32;
coarse v stays below eta_v. For a crossing exterior link its relative
coordinate is Log[exp(bar_y_f)exp(-v_c)]. The exponential and logarithm
series bound its norm by

    4(||bar_y_f||HS+||v_c||HS)<=5a_0/32<a_f0/4.

The intermediate matrix is within operator distance 1/2 of I; determinant
one and continuation from zero fix the traceless logarithm. Internal
boundary links simply have coordinate bar_y_f. Hence every LOCAL Cauchy
polydisc stays inside the existing fine analytic chart. A critical point
is needed only on the final smaller RF/RC tube, not on these larger local
Cauchy circles.

Write Phi_R=sum_xi phi_xi over the original touching vertices.
For a kernel vertex xi, its all-zero original-lift value is
c_xi(u)=sigma^2 log Ntilde_(kappa u)(I), independent of coarse v by Haar
invariance and analytic continuation. For Haar and Wilson vertices take
c_xi=0; the Wilson all-zero value is bounded by
(1+rho_0)N(1+exp(4eta_v)). Thus SC's local bound remains

    |phi_xi-c_xi(u)|<=H_loc:=2(1+rho_0)[H+N(1+exp(4eta_v))]. (QC12)

Only this identical constant is removed for a derivative estimate.
It remains in the actual phase, critical value and normalization.
For conservative derivative counts retain the whole RC radius-13 root,
including every radius-9 boundary-membership reader, and put

    s_v=27^4, d_v=(9L^4+5)s_v, q_v=4D s_v,
    q_f=(8L^4+8)D, I0=15,
    M_vf=H_loc/(r_v r_f), M_vv=2H_loc/r_v^2,
    L_vf=M_vf max(d_v q_f,I0 q_v),
    L_vv=M_vv d_v q_v.                                   (QC13)

There are at most 9L^4+5 original vertices per block, q_f fine scalar
slots per vertex, and 15 original vertices per fine scalar. Restriction
to touching vertices cannot increase these numbers. A coarse scalar
belongs to at most d_v enlarged roots. Cauchy's two derivative bounds,
including the diagonal 2! in M_vv, give maximum mixed row/column sums
d_v q_f M_vf and I0 q_v M_vf. The Schur inequality proves L_vf bounds
the mixed operator norm; L_vv bounds the coarse Hessian norm.

These are counts for local original phase derivatives with fixed masks.
They do not truncate the solved critical field or covariance readers.
No exterior y is promoted to an independent fine variable in the integral;
allowing it as a local analytic argument here only proves a derivative bound.

## 4. Zero-field coarse force and the full critical Schur complement

The coarse variables actually used by Phi_R are contained in C_R.
An active internal fine link has U0=I. An active crossing link uses only
its own coarse face V_c, whose original kernel belongs to C_R. Exterior
fine links are fixed in QC11. Accordingly the varying coarse vector has
at most 8D|R| scalar components, and ||v||2^2<=8eta^2|R|.

At v=a=bar_y=0, each kernel has every P_tau=Vbar_c. A real coarse
direction differentiates its paired means to
(A Vbar_c,-Vbar_c^(-1)A), where A is an average of traceless
anti-Hermitian tangent generators. The numerator h has zero derivative
at these matching means, including its explicit coarse-output derivative.
The ORIGINAL Z_t has zero derivative in this tangent: along
(exp(sA)Vbar_c,Vbar_c^(-1)exp(-sA)) it is constant by the Haar change of
variable Q=exp(sA)Q'. Complex linearity gives the same zero for complex
coarse directions. This uses only the derivative at a unitary lift.
It does not assert that a rough or nonzero-field normalizer is constant.
Active Haar terms have no explicit coarse dependence.

For each Wilson vertex the all-zero plaquette is I or an actual coarse
plaquette. Its defect has operator norm <=delta. A unit HS coarse scalar
direction has at most four occurrences in it. Writing its tangent as
A P and W(P)=N-tr(P+P^(-1))/2 gives

    |partial W|=|tr[A(P-P^(-1))]/2|<=4sqrt(N)delta.

This proves a LOCAL touching-vertex force bound, without importing a
full-phase cancellation for a regional boundary gradient:

    ||Phi_v(0,0;0,epsilon)||2<=G_v delta sqrt(|R|),
    G_v=4(1+rho_0)sqrt(N) d_v sqrt(8D).                    (QC14)

Let B_*=B+gamma/2 and G_0=(1+rho_0)g_* be SC14's actual fine Hessian
and zero-field force constants. On the admitted critical fields and the
segments used below, whose fine scalar amplitudes are at most 2bar_tau,
the full fine Hessian has operator norm <=B_* and real part >=gamma/2;
its regional critical inverse has norm <=2/gamma. This Hessian assertion
is not imposed on the whole product chart or on the larger local Cauchy
circles. With v=0 and complex epsilon,
SC15, obtained by integrating that active Hessian from zero to b, gives

    ||b||2<=(2/gamma)[G_0 delta sqrt(n0|R|)+B_*||bar_y||2]. (QC15)

One can see the boundary term directly: the regional zero-active force is
the active projection of the full force with boundary fields bar_y.
Its change from the all-zero force is a mixed submatrix of the bounded
full Hessian, hence at most B_*||bar_y||2. It need not vanish at delta=0.
The segment average of the active Hessian is accretive, proving QC15.

Integrate the QC13 mixed bound along (s b,s bar_y), at v=0. Stationarity
of the FULL Phi_R then yields

    ||partial_v A_R(0,epsilon;z)||2
                         <=a_v delta sqrt(|R|)+b_v||bar_y||2,
    a_v=G_v+2L_vf G_0 sqrt(n0)/gamma,
    b_v=L_vf(1+2B_*/gamma).                               (QC16)

For the actual holomorphic critical branch at each admitted v, implicit
differentiation gives exactly

    partial_v b=-(K_R^*)^(-1)Phi_av,
    partial_v^2 A_R=Phi_vv-Phi_va(K_R^*)^(-1)Phi_av,
    ||partial_v^2 A_R||op<=B_v:=L_vv+2L_vf^2/gamma.         (QC17)

Every kernel-normalizer derivative, source Hessian, physical boundary
substitution and active Haar derivative is included in these operators.
In particular stationarity of Phi does NOT mean stationarity of its
Haar-free physical part: at b the latter's fine derivative equals
sigma^2 partial_a sum log j_N(b). The Hessian in QC17 is never replaced
by the lift precision or by a product of independent colour inverses.

Taylor's integral formula along s v is now valid on the actual common
RF/RC tube. It gives

    |A_R(v)-A_R(0)|
      <=sqrt(8)eta sqrt(|R|)[a_v delta sqrt(|R|)+b_v||bar_y||2]
                                             +4B_v eta^2|R|.

Using ||bar_y||2^2<=pi^2 N Q_s/4 and sigma^2=N/u, Young's inequality
with coefficients a_bulk/8 and a_shell/8 proves the quadratic debit

    |A_R(v)-A_R(0)|/sigma^2
       <=u[(a_bulk delta^2|R|+a_shell Q_s)/8
                                                +C_den eta^2|R|],
    C_den=4B_v/N+16a_v^2/(N^2 a_bulk)
                                   +4pi^2 b_v^2/(N a_shell).           (QC18)

Delta in the first derivative is the REAL center curvature. No delta
bound is substituted for delta+8eta on the complex domain: the latter
still enters every RF existence/uniqueness and covariance restriction.
The second derivative estimate, not an incorrect center-force supremum,
pays the additional complex variation.

## 5. One energy inequality with source, reset and coarse debits

Retain SC14--SC21's imaginary-source comparison, with its signed reset
minimum. In its notation, computed at the common preliminary ceilings,

    B_W=2d2 exp(beta s0)[f''(2bar_tau)+2bar_tau f'''(2bar_tau)],
    a_s=g_*+2B_W G_0/gamma, b_s=B_W(1+2B_*/gamma),
    C_delta=2a_s^2 n0/(gamma N), C_shell=pi^2 b_s^2/(2gamma),
    D_s=C_delta c/(8a_bulk)+C_shell alpha,
    0<rho<=min(rho_0,sqrt[c/(8D_s)]).                      (QC19)

Here f,d2,s0 are RF13's original local majorants; omit the second source
constraint if D_s=0. Source rho is a FIXED positive radius. To recall the
exact mechanism, set H_s=sum_(p in P_R)s_p W_p. At epsilon=e+i t s,
stationarity gives
A''=(partial_a H_s)^T(K_R^*)^(-1)partial_a H_s; Re A'(0)=0.
The L2 source gradient is bounded by
rho[a_s delta sqrt(n0|R|)+b_s||bar_y||2].
At real e, the critical point minimizes the actual small-chart phase and

    A_R(Vbar,e;z)<=F_R(0;bar_y,e)
      =N E_R^e(U^R)+sigma^2 sum_(c in C_R)log Ntilde_(kappa u)(M_c(U^R))
      <=N A_ref^e.

This keeps the normalizer in the equality and uses its signed log<=0.
Consequently the imaginary-source debit is exactly bounded by

    Re A_R(Vbar,epsilon;z)/sigma^2
       <=u A_ref^e+u S_src,
    S_src=rho^2[C_delta delta^2|R|+C_shell Q_s]<=c Q_I/8. (QC20)

Set C_quad=C_num+C_den and replace SC24, and ONLY its coarse-debit
restriction, by

    eta_c<=min(1,eta_v/2,zeta/16,eta_RC,
                                  sqrt[c q/(32C_quad V_K)]).           (QC21)

Here eta_RC denotes the actual RF/RC restrictions on the SAME family,
including delta_hat=delta+8eta_c, Y=c_y zeta, the boundary-force budget,
the critical tails, RC8, and RC13's u-dependent convergence conditions.
It is not a separate unproved covariance hypothesis. Section 7 supplies
an explicit shrinking choice where this intersection retains the stated
sqrt(q)/K^2 order.

Combining QC9, QC18 and QC20 inside the actual compact integral leaves
the following single pointwise energy on pi_Aj:

    (31/32)E_R^e - A_ref^e - S_src
          -(a_shell/4)Q_s
          -(a_bulk delta^2|R|+a_shell Q_s)/8
          -C_quad eta_c^2|R|
       >=[(31-8-4-1-1)/32]c Q_I-c q|A|/32
       >=c q|A|/2.                                      (QC22)

Thus the reset spends 8/32, imaginary sources 4/32, the numerator shell
1/32, and denominator Young terms 1/32, in units c Q_I; the numerator
has already spent 1/32 of E_R. The coarse quadratic term spends at most
c q|A|/32. Nothing is borrowed a second time from SC13's E-2A_ref
comparison. A_ref and S_src are functions of the actual fixed exterior;
QC22 is applied pointwise before integrating the interior Q_I-dependent
shell predicate, not by taking a random threshold out of the integral.

## 6. Exact normalization, locality and the retained coefficient norm

All polynomial and dimensional costs are the original ones. For arbitrary
real compact means, CS15's cap about an actual maximizer gives

    Ntilde_(kappa u)(M)^(-1)<=C_norm(1+u)^(D/2),
    C_norm=max(1,c_*^(-1)max(1,kappa_+)^(D/2)),
    c_*=c_H r_H^D exp[-r_H^2/(2N)], r_H=min(1,pi/(2sqrt(N))),
    c_H=[sin(r_H)/r_H]^(N(N-1)) v_D/Vol_HS(SU(N)).         (QC23)

This includes singular M and keeps the full probability Haar cap.
Hence the numerator has cost C_norm^(8|R|)(1+u)^(4D|R|).
RC's actual log has |H_R|<=epsilon_reg|R|, epsilon_reg<=beta/16:
each nonempty connected term contains an active owner in R, and summing
its rooted bound over R keeps every full remote reader. There is no
residual-only empty vacuum. Therefore QC5 gives

    |I_R|^(-1)<=h_N^(-m0|R|)
             [B_*/(2pi sigma^2)]^(n0|R|/2)
                         exp[Re A_R/sigma^2+epsilon_reg|R|],
    p0=8log C_norm+m0 log max(1,h_N^(-1))
           +(n0/2)log max(1,B_*/(2pi N))+beta/16,
    p1=4D+n0/2,
    sup |B_Aj|<=exp{[p0+p1 log(1+u)]V_K|A|-c u q|A|/2}.  (QC24)

The remaining compact Haar mass is at most one. The determinant estimate
is on all n0|R| modes of the same critical matrix, with the RF/RC branch;
neither it nor the critical action has been erased as a vacuum.

The compact numerator is holomorphic in the original epsilon and coarse
v on QC21 because every fine input and predicate is fixed and real.
The denominator is the exact nonzero regional chart integral on the same
physical domain. Thus the coefficient is holomorphic there. Its complete
native reader remains SC's Gamma_A=N_(r_g+2)(A), |Gamma_A|<=S_K|A|.
It includes all earlier shell/absence tests, original source plaquettes,
paired words, trees and coarse outputs. Locality follows from the two
ORIGINAL local integrals in QC5, not by relabelling individual RF/RC
covariance or critical-field atoms with smaller supports.

Let Delta=max(1,(4K+5)^4-1). A traversal of a spanning tree bounds the
number of n-site connected A through an anchor by Delta^(2(n-1)).
For any fixed original-block support rate mu>=0, set

    t=K exp{mu S_K+[p0+p1 log(1+u)]V_K-c u q/2}.
    sup_x sum_(A:x in Gamma_A) exp(mu|Gamma_A|)
                    sum_(j=0)^(K-1) sup |B_Aj|
        <=S_K t/(1-Delta^2 t),        Delta^2 t<1.         (QC25)

There are at most S_K choices of an anchor near x; the finite j sum
costs K. Suprema include every admitted fixed real exterior and the
entire new complex tube. RC's small beta has not been replaced by a
two-unit support margin. For fixed q, SC32's explicit large-u thresholds
still imply QC25<=exp(-c q u/8), because QC24 is unchanged.

The exact single-insertion identity, with actual exterior Haar measure,
outside-only factors and the remaining cut predicates, stays

    int dH chi_cut pi_Aj w_epsilon
      =int_(E_Aj^out) dH_out chi_out W_out I_R B_Aj.       (QC26)

No normalized complex exterior law has been assigned total variation
one. The identical deep factors cancel only inside B_Aj and remain in
QC26. This is not a simultaneous gas factorization for the whole cut.

## 7. A genuinely wider shrinking tube and its derivative costs

There is a noncircular choice retaining ONE R_amb,beta and source rho.
First choose the joint preliminary ceilings, all local Cauchy constants
and RF/RC budgets above. Choose r_a and tau with RC8, then boundary and
coarse radii with RF18; at fixed radii take u large enough for RC13 and
QC25. This proves a nonempty fixed-radius theorem without changing atoms.

For the useful shrinking specialization let

    p=(log(2+u))^alpha_cut, alpha_cut>5/2,
    r_a=sigma p, tau=c_a sigma p,
    0<c_a<=min(1/(16D),
                       sqrt(a_P)/(8D sqrt(L_hat^2+a_P/64))).           (QC27)

Here a_P,L_hat are the unchanged regional precision and density constants
of RC, computed at fixed preliminary ceilings. Its boundary choices give

    C_N=N''(bar_tau/2)/2,
    B_bd=1+Q_K+rho B_src+(1+rho)C_N bar_tau/2,
    k_y=min(1/2,1/(8A_G B_bd)),
    k_delta=1/(8A_G g_*(1+rho)),
    k_v=min(k_delta/9,k_y/(16c_y)),
    c_z=k_y c_a/c_y, zeta=c_z sigma p, Y=c_y zeta=k_y tau. (QC28)

The N in C_N is RF13's nonlinear force majorant, not the rank N.
Thus A_G times the boundary force is <=tau/8. RC17 admits every
delta,eta<=k_v tau, with its remaining coarse force <=tau/8, and keeps
the same unique RF critical branch and both covariance tails.

Choose fixed positive c_q,c_delta,c_eta with

    c_q<=c_z^2/(64pi^2 N), c_delta<=sqrt[c/(8a_bulk)],
    c_eta<=sqrt[c/(32C_quad)],
    q(u)=c_q sigma^2 p^2,
    delta(u)<=c_delta sqrt(q(u))/(4K(q(u))+1)^2,
    eta_c(u)=c_eta sqrt(q(u))/(4K(q(u))+1)^2.              (QC29)

All fixed preliminary constants stay independent of u. Since q tends to
zero, K(q) tends to infinity and is O(1+log u). Both delta/tau and
eta_c/tau tend to zero like K^(-2). Therefore the explicit RF/RC bounds
delta,eta<=k_v tau, eta<=zeta/16 and every fixed local cap in QC21 hold
for all sufficiently large u. This establishes the ACTUAL radius
eta_c of order sqrt(q)/K^2; it is not just a formal upper bound hidden
behind an unspecified eta_RC. The q-good boundary and traceless-log
margins follow from QC29, while r_a<=epsilon_1/8 is eventual.

RC18 supplies, on this same shrinking family,
epsilon_reg<=C1 sigma^2+C2(1+p^(91D+2))exp(-a_P p^2/64).
Thus its convergence/nonzero conditions hold. Further, u q=N c_q p^2,
whereas V_K log(1+u)=O((1+log u)^5), mu S_K=O((1+log u)^4) and
log Delta=O(log log(2+u)). Consequently QC25 is eventually at most

    exp[-c N c_q p^2/8].                                 (QC30)

The original source radius stays fixed. On the half coarse/source tubes,
ordinary finite-order jets of the ACTUAL coefficient obey

    |partial_v^ell partial_epsilon^nu B_Aj|
      <=ell! nu! (2D/eta_c)^|ell| (2/rho)^|nu|
                exp{[p0+p1 log(1+u)]V_K|A|-c u q|A|/2}.   (QC31)

Use scalar Cauchy radii eta_c/(2D), rho/2 inside the full link/source
domains. No indicator is differentiated. Readers stay Gamma_A; derivatives
outside the actual input labels vanish. Unscaled coarse derivatives still
have the displayed growing inverse-radius costs.

## 8. Exact scope and provenance of the advance

CS supplied the actual filling, compact normalizer and local energy;
OC supplied the shell/reference charge; SC supplied this exact local
coefficient and the signed, energy-weighted imaginary-source denominator.
RF/RC supplied the unique full-colour regional critical field, normalized
fixed-chart integral and complete-reader log on the common family.
QC6--QC9, QC10--QC18 and QC22 are the new mean-spread, mixed-derivative
and single-budget calculations. Their full source readings and mechanical
checks are recorded in the separate frozen packet; author checks are not
independent review evidence. No new literature theorem is imported.

The gain from q/K^4 to sqrt(q)/K^2 is material. The latter is still of
order sigma p/K^2 in QC29 and does not establish an unscaled fixed coarse
domain or match a larger original RG consumer class. Additional SC34/OC27
margins can place the all-q-good group event inside the unchanged Omega;
they do not identify I_R with the original selected-sector integral.
Nothing here transports G/Omega or hard histories, constructs an exact
global complement gas, handles arbitrary inherited effective weights,
or closes a renormalization induction. Full non-free continuum existence
and the positive physical continuum mass gap remain OPEN.

Only this source and checks/quadratic_coarse_return_* are authored.
[PROCESS_LIGHT](PROCESS_LIGHT.md) and the coordinator's file boundary
govern. Predecessor sources and packets remain unchanged. The source is
frozen before provenance packaging and a fresh independent review.
