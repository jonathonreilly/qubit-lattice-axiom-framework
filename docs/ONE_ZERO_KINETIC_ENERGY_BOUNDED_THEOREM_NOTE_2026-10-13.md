---
title: "One Zero Kinetic Energy Bounded Theorem Note"
claim_id: one_zero_kinetic_energy_bounded_theorem_note_2026-10-13
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
runner: scripts/one_zero_kinetic_identity_2026_10_13.py
assembly_status: publication_prepared_root_review_and_runtime_pending
scientific_execution: none_in_publication_preparation
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied massive free CAR model, specified vacuum, exact fixed control and time hypotheses, conditional actual-cell premises
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: unchanged reviewed conditional cores with exact source and exposure history
next_trace_action: root publication review and source integration; cumulative current-main review and retained audit remain separate
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies:
  - two_zero_kinetic_energy_bounded_theorem_note_2026-10-13
  - energy_adapted_calibration_bounded_theorem_note_2026-10-13
  - calibrated_energy_transfer_bounded_theorem_note_2026-10-13
---

Claim type: bounded_theorem

Publication source wrapper: all five historical cores and the accepted assembly retain their precise hypotheses and exposure history. This note adds canonical metadata and recovery links only. Mean, marginal energy law, fixed correlation tests and finite-mode bounds retain their different control classes, time windows and resources. No joint stochastic process, physical selector or retained status is asserted.

# One-zero extension of the kinetic energy law

Status: conditional-support; bounded theorem source assembly with an unchanged
421-line root proof and a complete ordinary source-exposed crosscheck. The
wrapper adds no mathematical conclusion or formal retained status.

    actual_current_surface_status: conditional-support
    target_claim_type: bounded_theorem
    trace_class: upstream_support
    reachability_to_target: partially_closes
    conditional_surface_status: supplied massive infinite free CAR model
    hypothetical_axiom_status: null
    admitted_observation_status: null
    audit_required_before_effective_retained: true
    bare_retained_allowed: false

## Scope and relationship to the other notes

At least one fixed real compact smooth smearing has zero integral in every
component; the other is arbitrary in that class. Equations O3--O4 give
operator and weighted Born-remainder estimates on bounded kinetic windows
uniformly for measurable real envelopes of magnitude at most one. The
Poisson, mean and Wasserstein-one conclusions O5 require a fixed cosine
drive. The estimates do not assert a propagator at infinite time or a
fixed-nonzero-coupling all-time bound. The fixed-frequency threshold and
zero-frequency cases, including the weaker zero-frequency error, remain.

The noncommuting Schur order O10 and temporal Hilbert--Schmidt ideal order
O15 are part of the proof. Ordinary input-operator estimates and temporal
Hilbert--Schmidt estimates have different roles. The one-zero proof cannot
silently extend its good-channel bounds to two arbitrary smearings. The
general mean theorem in the companion note is a separate argument with
different frequency and conclusion restrictions.

Section 8 is a conditional application of corrected V2 section 8 and its
actual-cell premises. The continuum zero integral is not imposed on the
calibrated band images. Fixed finite order, fixed weighted resources, actual
cell inputs, unital Fock embedding, common vacuum, first-energy work bound
and a^(N+1)=o(lambda^2) remain required. No sharper joint scale is inferred.

## Review and exposure history

The core is ONE_ZERO_CONTROL_KINETIC_ROOT_PROBE.md,
SHA-256 fccf1ea3387b059b1d625b985d38bb71573a5bfd48af12e251dc33489b551960.
Its seal records prior exposure to corrected V2, its review and confirmation,
root correlation 335, and the weighted interface. The separate general-mean
worker's scientific findings remained excluded until the root proof freeze.

ONE_ZERO_CONTROL_KINETIC_CROSSCHECK.md (198 lines, 86aaa6ab) checks O1--O25 and
the conditional transfer; ONE_ZERO_CONTROL_KINETIC_ROOT_ACCEPTANCE.json
binds that review without a formula repair. The crosschecker also authored
general mean 301. Its comments about that worker proof are author
re-examination, not independent acceptance. The later fresh general-mean
review has its own exact sources and evidence in the companion note.

The corrected two-zero theorem is a same-packet dependency for exact CAR,
normalization and reviewed Gaussian machinery. Its stronger two-zero
decay is not assumed on this larger control class. Exact owner relations
and canonical actual-cell dependencies are listed in DEPENDENCIES.json.
All source-era pending/open statements remain unchanged and are interpreted
chronologically. This source-exposed assembly creates no new independence,
model diversity, Lean result, empirical selection or retained audit.

## Unchanged one-zero proof core

# Kinetic energy with one zero-integral control channel

Status: conditional-support, new root derivation awaiting independent check.
The proof below uses the supplied massive free CAR model. It claims no physical
selector, empirical prediction, formal Lean verification or retained status.

## 1. Exact premises and statement

Use the corrected conventions of WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT_V2.md,
859 lines, SHA-256 c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b.
Its original picture defect and exact repair remain preserved. Fresh review
39a68949 and confirmation c2aa65ec checked the continuum proof and the general
CAR/graph/overlap machinery. This note does not import its two-zero-channel
kinetic theorem as a theorem for the larger class studied here.

Let K=L2(R;C^2), D=-vp sigma_x-m sigma_y, E=(m^2+v^2p^2)^(1/2),
P=(1+D/E)/2, P_-=I-P, with fixed m,v>0. Real conjugation Gamma satisfies
Gamma D Gamma=-D. On Fock(h), h=PK, use the free vacuum Omega and
H0=dGamma(E|h). For real smearings gamma(f)=a*(sqrt(2)Pf)+a(sqrt(2)Pf),
with a antilinear, a* linear and inner product linear in the second slot.

Fix real f,g in C_c^infinity(R;R^2). The single additional restriction is

    integral_R f_j(x)dx=0, j=1,2.                       (O1)

No integral condition is imposed on g. Interchanging f,g changes the sign
of the quadratic interaction and leaves the limiting rate below unchanged.
Put V=(i/2)[gamma(f),gamma(g)] minus its vacuum expectation, and let W(t)
be the full propagator of H0+lambda u(t)V, where u is measurable, real and
|u|<=1. Its interaction representative is Y(t)=exp(itH0)W(t).

Set F=(f,g), M=2i[[0,1],[-1,0]], B=FMF*. Let S be the full one-particle
propagator of D+lambda u(t)B and Z(t)=exp(itD)S(t). All propagators start
at I. The exact CAR identities are

    W*gamma(h)W=gamma(S*h), Y*gamma(h)Y=gamma(Z*h),
    N(T)=P Z(T)P_- Z(T)* P,
    E_lambda(T)=||E^(1/2)P Z(T)P_-||_HS^2.              (O2)

The energy identity is justified by positive finite-rank and bounded energy
cutoffs, then monotone convergence. The full and interaction states have the
same complete H0 law. These exact identities hold for arbitrary compact f,g;
no zero-integral decay estimate is used to establish them.

**Claim.** For every fixed tau_max<infinity and every fixed q>=0, there are
finite constants C and lambda_0>0, depending on f,g,m,v,q,tau_max, such that
for 0<|lambda|<=lambda_0, every T<=tau_max/lambda^2 and every such u,

    ||Z(T)-I|| <= C sqrt(|lambda|),
    ||E^(q/2)[P Z(T)P_- - B1(T)]||_HS <= C sqrt(|lambda|), (O3)

where the exact first Born block is

    B1(T)=-i lambda integral_0^T u(t)P F_t M F_t*P_- dt,
    F_t=exp(itD)F.                                      (O4)

For u(t)=cos(omega t), fixed omega>0 and T=tau/lambda^2,

    E_lambda(T) -> tau omega nu_omega,
    mu_lambda,T -> Law(omega N_tau),
    N_tau~Poisson(tau nu_omega), nu_omega=(pi/2)r(omega).  (O5)

The law convergence is weak and in W1. The mean and each fixed characteristic
function converge uniformly on bounded tau intervals, with an error bounded by
C sqrt(|lambda|)+C_omega lambda^2 log(2+tau_max/lambda^2). The density r is
the exact exterior-pair density below. For 0<omega<=2m the rate is zero; for
omega=0 the mean and law also converge to zero. This latter conclusion does
not claim the stronger O(lambda^2) exact-energy rate of the two-zero class.
Negative frequencies give the same cosine as their absolute values.

## 2. Good and bad channel estimates

Write f_1=f, f_2=g and

    G_ij(t)=<f_i,exp(-itD)f_j>.

For i,j other than (2,2), the massive band decomposition has scalar Schwartz
amplitudes a(p) with a(0)=0, because at least one slot is f. The phase E(p)
is even. Consequently its integral equals that of a_even(p)=[a(p)+a(-p)]/2.
This is a Schwartz even function with a_even(0)=a_even'(0)=0. Factoring
a_even=p^2 b(p), and using p=x sqrt(2m+x^2)/v, gives a quadratic zero in
the exact stationary coordinate E=m+x^2. One integration by parts and the
elementary quadratic-phase O(|t|^-1/2) bound then give

    |G_11(t)|+|G_12(t)|+|G_21(t)| <= C(1+|t|)^(-3/2),
    |G_22(t)| <= C(1+|t|)^(-1/2).                        (O6)

For the last bound no zero is factored: split the transformed integral at
|x|=|t|^-1/2 and integrate by parts on the outer rays. Schwartz bounds make
every displayed constant finite. Small times are controlled by Hilbert-space
norms. The same statements hold with either massive band projector and any
fixed power E^q inserted in the amplitudes. In particular a single vanishing
slot suffices for the cross terms: estimating the odd linear term by its
absolute value before integration would lose the cancellation used here.

Let H_T=L2([0,T];C). Define scalar causal operators

    (K_ij z)(t)=integral_0^t G_ij(t-s)u(s)z(s)ds.

Choose finite constants a_11,a_12,a_21,b,h, independent of T and u, with

    ||K_ij||<=a_ij for (i,j)=(1,1),(1,2),(2,1),
    ||K_22||<=b sqrt(1+T),
    ||K_22||_HS(H_T,H_T)<=h sqrt(T log(2+T)).             (O7)

The first bounds are Young inequalities using the half-line L1 integrals
in (O6). The bad operator bound follows from the truncated L1 integral of
(1+t)^(-1/2). The final bound is a separate kernel calculation:

    ||K_22||_HS^2 <= C^2 integral_0^T (T-s)/(1+s)ds
                  <= C^2 T log(2+T).

It is a Hilbert--Schmidt bound on scalar TIME space. It is not a claim that
the unsmoothed identity on the one-particle Hilbert space is Hilbert--Schmidt.

For fixed q>=0, introduce the positive-band synthesis maps

    L_f,q z=integral_0^T E^(q/2)P exp(itD)f z(t)dt,
    L_g,q z=integral_0^T E^(q/2)P exp(itD)g z(t)dt.

Their squared norms are bounded by the L1 norms of the corresponding
truncated weighted diagonal Gram kernels. By (O6), finite s_f,q,s_g,q exist
such that

    ||L_f,q||<=s_f,q, ||L_g,q||<=s_g,q(1+T)^(1/4).       (O8)

The full-space unweighted maps, with P omitted, have the same form of bounds,
denoted s_f, s_g. Their adjoints are the time-analysis maps. Restricting their
input to P_-K does not enlarge the operator bounds. All integrals over finite
time are Bochner integrals; graph-norm integration and closedness identify
the weighted maps since compact smooth f,g belong to every Dom E^k.

## 3. Schur inversion of the exact time equation

First let the initial input be all of K; restriction to P_-K will be made
when estimating Born errors. View

    X_j:K->H_T, (X_j xi)(t)=f_j,t* Z(t)xi,
    X_j,0:K->H_T, (X_j,0 xi)(t)=f_j,t*xi,
    f_j,t=exp(itD)f_j.

These are bounded operators on every finite interval. The exact bounded
Dyson equation gives the two coupled identities, including their signs,

    X_1=X_1,0-2lambda K_12 X_1+2lambda K_11 X_2,
    X_2=X_2,0-2lambda K_22 X_1+2lambda K_21 X_2.          (O9)

Suppose 2|lambda| max(a_12,a_21)<=1/2. Then

    R_1=(I+2lambda K_12)^(-1),
    R_2=(I-2lambda K_21)^(-1), ||R_1||,||R_2||<=2.

Eliminating X_2 yields the exact Schur equation

    [I+4lambda^2 R_1 K_11 R_2 K_22]X_1
        =R_1 X_1,0+2lambda R_1 K_11 R_2 X_2,0.          (O10)

Its extra inverse has norm at most2 whenever

    16lambda^2 a_11 b sqrt(1+T)<=1/2.                   (O11)

This condition is uniform for T<=tau_max/lambda^2 after reducing lambda_0,
because lambda^2 sqrt(1+T)<=lambda^2+|lambda|sqrt(tau_max).
Using ||X_1,0||<=s_f and ||X_2,0||<=s_g(1+T)^(1/4) now gives

    ||X_1|| <= 4s_f+16|lambda|a_11 s_g(1+T)^(1/4)
              =:A_lambda,T.                            (O12)

On the stated kinetic window A_lambda,T is uniformly bounded. The other
channel obeys

    ||X_2|| <= 2s_g(1+T)^(1/4)
                      +4|lambda|b sqrt(1+T)A_lambda,T.   (O13)

Equations (O10)--(O13) are ordinary operator estimates. No factor sqrt(T)
from a Hilbert--Schmidt source has entered (O12).

The full interaction map satisfies

    Z(T)-I=2lambda L_f,0(full) u X_2
                         -2lambda L_g,0(full) u X_1.

Here each L already integrates over time and u denotes bounded time
multiplication; the K operators above also contain the u in their own
internal time variable. Applying (O8),(O12),(O13) gives

    ||Z(T)-I||
      <=4|lambda|s_f s_g(1+T)^(1/4)
        +8lambda^2 s_f b sqrt(1+T)A_lambda,T
        +2|lambda|s_g(1+T)^(1/4)A_lambda,T.              (O14)

Since |lambda|(1+T)^(1/4)=O(sqrt(|lambda|)) and
lambda^2 sqrt(1+T)=O(|lambda|) uniformly on the kinetic window, (O14)
proves the first statement of (O3).

## 4. The temporal Hilbert--Schmidt improvement

Now restrict every X to P_-K. Put m_f=||P_-f|| and m_g=||P_-g||. Their
free time-analysis maps have exact Hilbert--Schmidt norms

    ||X_1,0||_HS=m_f sqrt(T), ||X_2,0||_HS=m_g sqrt(T).

Crucially, the ideal inequality applies in the OTHER order to the bad channel:

    ||K_22 X_1||_HS(P_-K,H_T)
       <=||K_22||_HS(H_T,H_T) ||X_1||
       <=h sqrt(T log(2+T)) A_lambda,T.                  (O15)

This is valid for arbitrary separable input space, by the Hilbert--Schmidt
ideal property (or expanding the positive trace in bases). It improves the
crude bound ||K_22|| ||X_1||_HS that would only grow as T. It does not remove
the logarithm by assuming an L2 kernel is L1.

Write J_T=sqrt(T log(2+T)). From X_2=R_2(X_2,0-2lambda K_22 X_1),

    ||X_2||_HS<=2m_g sqrt(T)+4|lambda|h J_T A_lambda,T.

Using ||R_1-I||<=4|lambda|a_12 and
||R_2-I||<=4|lambda|a_21 gives

    e_1:=||X_1-X_1,0||_HS
       <=|lambda|D_1 sqrt(T)+16lambda^2 a_11 h J_T A_lambda,T,
    D_1=4a_12 m_f+8a_11 m_g,

    e_2:=||X_2-X_2,0||_HS
       <=|lambda|D_2 sqrt(T)+4|lambda|h J_T A_lambda,T,
    D_2=4a_21 m_g.                                      (O16)

For example X_1-X_1,0=(R_1-I)X_1,0+2lambda R_1 K_11 X_2
gives the first line with exactly those constants. This also proves the needed
Hilbert--Schmidt membership, rather than assuming it at the start of the Schur
argument. All formulas are consistent at T=0.

Set beta=P Z(T)P_-. The exact output formula and (O8),(O16) show

    e_q,out:=||E^(q/2)(beta-B1)||_HS
       <=2|lambda|[s_f,q e_2+s_g,q(1+T)^(1/4)e_1]
       <=2lambda^2 sqrt(T)[s_f,q D_2+s_g,q(1+T)^(1/4)D_1]
         +8lambda^2 s_f,q h J_T A_lambda,T
         +32|lambda|^3 s_g,q a_11 h(1+T)^(1/4)J_T A_lambda,T. (O17)

For T<=tau_max/lambda^2 and small nonzero lambda, the terms are respectively
O(sqrt(|lambda|)), O(|lambda|sqrt(log(2+tau_max/lambda^2))) and
O(|lambda|^(3/2)sqrt(log(2+tau_max/lambda^2))). The middle logarithmic term
is also O(sqrt(|lambda|)); use boundedness of x log(1/x) near zero. This
proves the weighted remainder in (O3), uniformly over the stated time and
control window. No claim of uniformity for unbounded tau or fixed lambda
and T tending to infinity follows from (O11).

## 5. Pair density and the Born secular limit

In the scalar positive-band frame

    e_+(p)=(exp(i theta(p)/2),-i exp(-i theta(p)/2))/sqrt(2),
    theta(p)=arctan(vp/m),
    v_f(p)=sqrt(2)e_+(p)*fhat(p),
    v_g(p)=sqrt(2)e_+(p)*ghat(p),
    Delta(p,q)=v_f(p)v_g(q)-v_g(p)v_f(q),

the exterior pair density is

    r(e)=1/2 integral |Delta(p,q)|^2 delta(e-E(p)-E(q))dpdq. (O18)

The pair wavefunction is Delta/sqrt(2), and V Omega=i(v_f wedge v_g).
The radial coordinate E=m+x^2 makes this an ordinary continuous density,
rapidly decreasing at infinity. Antisymmetry gives Delta(0,0)=0; with just
(O1), Delta=O(|p|+|q|), so r(2m+s)=O(s), not necessarily O(s^3).
Extend r by zero below2m. It is continuous also at2m.

Let H2=E tensor I+I tensor E on the two-particle exterior space. The pair
correlations C_j(t)=<v_f wedge v_g,H2^j exp(itH2)(v_f wedge v_g)>, j=0,1,
are finite sums of products of one-particle correlations. The unweighted
diagonal product has decays t^-3/2 and t^-1/2; the cross product has two
t^-3/2 factors. The j=1 case inserts E in one of the factors and has the
same estimates. Thus

    |C_0(t)|+|C_1(t)| <= C(1+|t|)^(-2).                 (O19)

Their densities are r(e) and e r(e), respectively. The exact first Born
block, with J=Gamma C in the scalar band frame, has kernel

    (B1 J)(p,q)=lambda Delta(p,q) I_T(E(p)+E(q)),
    I_T(e)=integral_0^T u(t)exp(iet)dt.

The antisymmetry of Delta symmetrizes the single output energy. Therefore

    ||B1||_HS^2=2lambda^2 integral r(e)|I_T(e)|^2 de,
    ||E^(1/2)B1||_HS^2=lambda^2 integral e r(e)|I_T(e)|^2 de. (O20)

In particular both are bounded by C lambda^2 T for every |u|<=1: expand
the double time integral and use the L1 norm of the appropriate pair
correlation in (O19). This is an independent bound on the first Born term;
applying the bad synthesis norm alone would give an insufficient power of T.

For u(t)=cos(omega t), fixed omega>0, any of the densities b used below
with correlation |C_b(t)|<=C_b(1+|t|)^(-2) satisfies

    integral b(e)|I_T(e)|^2 de
       =(pi/2)T[b(omega)+b(-omega)]+O_b,omega(log(2+T)). (O21)

Indeed the cos(t-s) term produces
(1/2)integral_(-T)^T (T-|t|)cos(omega t)C_b(t)dt.
Replacing the triangular factor by T on the entire line costs at most
C integral_0^T t/(1+t)^2 dt+C T integral_T^infinity (1+t)^(-2)dt,
which is O(log(2+T)). Fourier inversion is justified by C_b in L1 and
continuity of b; its coefficient is the displayed pi/2. Integrating the
cos(t+s) term in the remaining time coordinate costs at most
||C_b||_L1/(2omega). This proof works for complex b and makes no finite
first absolute time-moment assumption.

Take b(e)=e r(e). Its negative-frequency value is zero. By (O17),(O20),

    |E_lambda(T)-||E^(1/2)B1||_HS^2|
       <=e_1,out[2||E^(1/2)B1||_HS+e_1,out] <=C sqrt(|lambda|)

on bounded kinetic windows. Equations (O20),(O21) prove the mean part of (O5).

## 6. Complete energy law

Let A=PZP, beta=PZP_-. Write C for scalar conjugation on h and
J=Gamma C. By (O14),(O17),(O20), uniformly on bounded kinetic windows,

    ||A-I||+||beta||=O(sqrt(|lambda|)),
    ||beta||_HS=O(1),
    ||beta-B1||_HS=O(sqrt(|lambda|)).

For sufficiently small lambda, A is invertible and the antisymmetric pair
coordinate is L=beta Gamma A^(-1) C. The exact transformed annihilator is
a(Axi)+a*(beta Gamma xi). The CAR consequently gives L^T=-L and the pair
state identified by this annihilator is Y(T)Omega up to phase. The reviewed
finite-exterior/overlap-ODE argument and its Hilbert--Schmidt limit apply,
because they need only the following bounds, now proved here:

    ||L||=O(sqrt(|lambda|)), ||L||_HS=O(1),
    ||L-B1 J||_HS=O(sqrt(|lambda|)).                     (O22)

For L_s=exp(isE)L exp(isE^T), the continuous trace-log lift gives the exact
energy characteristic function

    log chi_lambda,T(s)
      =1/2 Tr log(I+L*L_s)-1/2 Tr log(I+L*L).            (O23)

This logarithm is the lift obtained from the small operator-norm series,
not an assertion about a principal scalar logarithm for arbitrary tau.
The series remainder is bounded by C||L||^2||L||_HS^2=O(|lambda|).
Replacing L by B1J in the quadratic part costs O(sqrt(|lambda|)). The
exterior factor1/2 then yields

    log chi_lambda,T(s)
      =lambda^2 integral r(e)[exp(ise)-1]|I_T(e)|^2 de
                          +O(sqrt(|lambda|)).           (O24)

The correlation for b_s(e)=r(e)[exp(ise)-1] is C_0(t+s)-C_0(t).
For each fixed s it has the decay required by (O21). Hence, at
T=tau/lambda^2,

    log chi_lambda,T(s) -> tau nu_omega[exp(is omega)-1]. (O25)

The error is O(sqrt(|lambda|))+O_s,omega(lambda^2 log(2+tau_max/lambda^2)),
uniformly for bounded tau. The limiting characteristic function is continuous
at s=0 and is that of the law in (O5), proving weak convergence. The mean
limit was proved separately, so a rare tail carrying extra mean is excluded.
For nonnegative laws, weak convergence together with convergence of means
implies W1: E[(X-R)_+]=E[X]-E[min(X,R)], then use
x1_(x>2R)<=2(x-R)_+ and truncate Lipschitz test functions. This proves the
claimed W1 passage without a higher moment assumption.

For 0<omega<=2m, continuity and r(omega)=0 make the rate vanish, with the
same logarithmic secular bound valid even at the threshold. For omega=0,
|I_T(e)|<=2/e on the pair support e>=2m. The Born energy is O(lambda^2).
By (O17), the exact weighted block norm is O(|lambda|)+O(sqrt(|lambda|)),
so exact energy is O(|lambda|) on bounded kinetic windows and tends to zero.
The nonnegative energy law then tends to delta_0 also in W1 by its mean.
At tau=0 the exact state is Omega. If either control is identically zero,
the dynamics is free; proportional real controls likewise have centered V=0.

## 7. A nontrivial control outside the earlier class

Fix any omega>2m and k0=sqrt((omega/2)^2-m^2)/v. Choose a nonzero,
nonnegative, even b in C_c^infinity(-L,L) with k0 L<pi/2, and set

    f=(b',0), g=(b,0).

Then f satisfies (O1), while integral g_1>0. With the unitary Fourier
transform B(p)=bhat(p), the scalar slots give exactly

    Delta(p,q)=i(p-q)exp(-i(theta(p)+theta(q))/2)B(p)B(q).

Since B(k0)>0 by its positive cosine integral,
Delta(k0,-k0)=2ik0 B(k0)^2 is nonzero. A neighborhood on the regular
energy circle has positive angular measure, so r(omega)>0. The extension
therefore includes a strictly positive-rate control excluded by the old
two-zero-integral hypothesis. No numerical fitted coefficient is used.

## 8. Transfer and exact remaining limits

The actual-cell kinetic transfer in corrected V2 section8 uses weighted
calibration errors, exact energy identification, common vacuum and the work
identity. It does not require the actual calibrated images to retain zero
integrals. The continuum condition is used in the continuum kinetic proof,
now supplied here under (O1). Consequently the same conditional actual-lattice
transfer holds when its original finite-resource hypotheses are checked and
a^(N+1)=o(lambda^2). This is a composition statement, not a fresh proof of
the upstream embedding, ordered inverse, alias estimates or energy work bound.

The small feedback parameter here is lambda^2 sqrt(1+T), and the bad-channel
synthesis norm grows as (1+T)^(1/4). This proof gives no all-time fixed-lambda
estimate. If neither smearing has zero integral, the good cross kernels
and the Schur factor bounds used above may fail; the present argument makes
no theorem or impossibility claim about that larger class. The physical
interpretation remains the specified driven massive free infinite model.

The separate kinetic_mean_relaxation worker has been excluded from every
root source and root finding while this derivation is being written. No worker
scientific preview has been opened. The root route is source-exposed to the
older corrected kinetic theorem/reviews and root correlation335, and these
shared premises limit any later independence claim. No new numeric process
or Lean checker has been run for this proof. Independent checking is pending.
The heterogeneous Hilbert--Schmidt composition in (O15) and noncommuting Schur
identity (O10) are concrete scoped formal-audit candidates; no formal result is
assumed in place of the displayed analytic arguments.

## Assembly trace and verification limits

The exact core bytes, line/byte offsets, literal wrapper pieces and complete
wrapper-only unified diff are supplied with this note. The single diff
convention is three context lines (`difflib.unified_diff`, n=3), against the
verbatim concatenation of its included cores. Empty core diffs and exact
extraction record zero core edits. SOURCE_CHECKER.py checks reconstruction
and identity only; it does not certify any theorem.

The selected immediate source freezes and every directly bound byte object
are archived with explicit one-hop maps. Nested receipts are preserved
opaque, not recursively audited. Historical diagnostic programs/results
are provenance, not new execution or newly certified mathematics. The
review, exposure, limitation and dependency records remain part of the
packet. No CW, Git, cache, graph, PR, audit, axiom or prompt mutation is
authorized by this source assembly; the parent owns any later publication.


## Publication imports and recovery

- [two_zero_kinetic_energy_bounded_theorem_note_2026-10-13](TWO_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [energy_adapted_calibration_bounded_theorem_note_2026-10-13](ENERGY_ADAPTED_CALIBRATION_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [calibrated_energy_transfer_bounded_theorem_note_2026-10-13](CALIBRATED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-13.md)

These are the direct mathematical or conditional parents. The accompanying packet at `.claude/science/physics-loops/toe-kinetic-energy-20261013` binds canonical bytes, consumed same-packet cores and archived inputs to their actual consumers in `PARENT_BINDINGS.json` and `CLAIM_REGISTRY_ADDITIONS.json`. Five historical exposure/provenance relations are separate from the fourteen direct edges. Pair PR9515 supplies the actual Git parent; its ancestry and root484 exposure do not create a new mathematical edge. Historical pair792 has an exact canonical map; the separate root286 remains an archived provisional input.

The complete405-file accepted assembly, original847 picture defect, missed root check, exact V2 repair, all source reviews and the scoped one-hop closure are recoverable from content-addressed objects. Historical pending and exposure text remains unchanged. General301 remains mean-only; the separate470 core supplies the full-law extension with its own bounds. The published identity tools check byte reconstruction and declared inputs with zero mathematical predicates. They do not perform a fresh proof, independent review, retained audit or source-status promotion. Unaccepted modulated-drive work is excluded.
