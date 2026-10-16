# Conditional scalar reconstruction from lensing and dust velocities

**Date:** 2026-10-15
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_growth_lensing_inverse_check.py](../scripts/scalar_growth_lensing_inverse_check.py)

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: revised_scalar_action_potential_scale
target_blocker_text: Derive or eliminate the remaining scalar action, state, scale and measurement assumptions
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: Exact candidate admission and ambiguity classification inside a supplied linear response and physical input map
hypothetical_axiom_status: none proposed
admitted_observation_status: Published ACT/BOSS summaries exposed for development; no continuous input history or independent empirical test admitted
claim_type_reason: Mathematical inverse with candidate geometry and physical response premises explicit
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: Derive a controlled dynamical response or forward likelihood without supplying its homogeneous field history
```

The exact target is to characterize the revised scalar shape parameters compatible
with ideal lensing and dust-velocity histories, without supplying the initial
density contrast or its absolute amplitude, and to classify when two distinct
shapes reproduce the entire reduced history.

Root is the direct author. The result is conditional mathematics, with synthetic
checks. It does not choose the fundamental action, infer an observed scalar
parameter, or select an initial physical state. The familiar observable slip
construction is credited to [Amendola et al., arXiv:1210.0439v2](https://arxiv.org/pdf/1210.0439v2).
The integrated candidate inverse, its exceptional ambiguity and its combination
with background equations are derived here. No priority claim about all prior
literature is made.

## 1. Observations and explicit premises

Lensing and redshift-space distortions are distinct channels. Published
[ACT DR6/BOSS results, arXiv:2405.12795v2](https://arxiv.org/pdf/2405.12795v2)
give E_G=0.31 (+0.06,-0.05) for CMASS at effective z=0.555 and
0.49 (+0.14,-0.11) for LOWZ at z=0.316, central 68.27% intervals. These are
projected, window-weighted estimates with correlated calibration; they are
not continuous functions of time and wave number. ACT+Planck combinations share
galaxy and lensing information and do not supply extra independent epochs.
No maps, chains or numerical likelihood have been fitted here.

Take a spatially flat Jordan background with conserved pressureless matter,
rho=rho0 a^-3, H>0, and linear scalar perturbations in the convention

    ds^2=-(1+2Psi)dt^2+a^2(1-2Phi)dx^2.

Let N=ln a, E=H/H0, K=k_com/a>0. Prime is d/dN along a fixed comoving mode;
a fixed angular multipole or a fixed physical K is not that derivative.
The ideal physical input map includes the expansion/time calibration, a common
real coherent Fourier mode, lensing/velocity relative calibration, and any
deprojection/bias relation. Restrict to a connected interval with positive
velocity and lensing amplitudes below. Other sign/zero-crossing sectors require
their own domains.

Define W=-div(v)/(aH), h=H'/H. Linear dust conservation and Euler are

    delta'=W+3Phi',
    W'+(2+h)W=-K^2 Psi/H^2.                                 (1)

The supplied frozen-coefficient, single-scalar gravitational response is

    -2F K^2 Phi=delta_rho-K^2 delta_F,
    -2F K^2 Psi=delta_rho+K^2 delta_F,
    (K^2+m^2)delta_F=q delta_rho,
    F>0, q>0, m^2>=0, delta_rho=rho delta.                   (2)

These are a conditional quasistatic response, not the full relativistic field
equations. Time variation, density-gauge corrections, extra modes, effective
mass/mixing and the homogeneous scalar response need separate control. Even
arbitrarily large K/H does not bound a supplied free oscillation: the solution
S/Omega^2+A cos(Omega t) of xddot+Omega^2 x=S differs from its quasistatic
part by the unspecified amplitude A. A mass pole inferred within (2) is not
silently identified with a bare potential curvature.

Adding and subtracting (2) gives

    -K^2(Phi+Psi)=rho delta/F,
    Phi-Psi=delta_F/F,
    r=(Psi-Phi)/(Psi+Phi)=q K^2/(K^2+m^2).                  (3)

Set L=-a^3 K^2(Phi+Psi)/(3H0^2), P=L/W, P3=W'/W. Euler gives

    r=2E^2 a^3(P3+2+h)/(3P)-1.                             (4)

P uses the ACT E_G normalization. The literal P2 definitions in
arXiv:1210.0439v2 give P2=2P, despite the prose identifying P2 with E_G.
Equivalently eta=Phi/Psi=3P a^-3/[E^2(P3+2+h)]-1. The convention dictionary
was checked against primary-page renders; mixing the two definitions would
give the wrong scalar inference. The estimator and ACT papers also print
different theta signs, so this note defines W explicitly.

At one epoch, two distinct positive x_i=K_i^2 and positive r_i give

    1/r=b0+b1/x,
    b0=(x1/r1-x2/r2)/(x1-x2), b1=x1(1/r1-b0),
    q=1/b0, m^2=b1/b0.                                    (5)

Require b0>0, b1>=0 and test additional scales. Equal positive responses at
distinct scales give m^2=0 in this model. The identity r=q in the controls
below is that explicitly supplied light-response specialization. Actual
finite-error data need a model and uncertainty propagation, not exact division.

## 2. Candidate geometry and exact initial-density elimination

The revised candidate geometry is a supplied premise. For clarity it is
restated here. Let 0<k<1/3, beta=(1-k)(1+3k)/4 in (1/4,1/3), alpha=sqrt(beta),
s=(1+k)/[k(1-3k)], X=exp(2alpha u), T=1+sX and J_K=1+(1-3beta)sX.
The radial Einstein kinetic coefficient is K_uu=J_K/T^2, the matter conformal
factor is A^2=(1+s)X/T, and Q=Q0(1+k)>0. With F=Q/A^2 and
Fc=Qs/(1+s), direct differentiation gives

    F=Fc+[Q/(1+s)]exp(-2alpha u)>Fc,
    q=|d ln A|_K^2=beta/J_K
      =beta(F-Fc)/(F-3beta Fc),
    Z_beta(q)=F/Fc=beta(1-3q)/(beta-q), 0<q<beta.           (6)

In particular Z>1 and dZ/dq=beta(1-3beta)/(beta-q)^2>0.
Using this geometric q as (2)'s single response requires the stated radial
or otherwise controlled mode reduction. In a background with transverse
motion it is not automatically the stress-inferred 1/(2omega+3).

Normalize at W0>0: What=W/W0, Phihat=Phi/W0, What0=1. The ideal P3 fixes
What=exp(integral P3 dN). Define the density primitive

    J(N)=integral from N0 to N of What dN+3[Phihat(N)-Phihat(N0)].

Equation (1) integrates to delta/W0=J+C, with C unknown. The potential is
obtainable in the same mode normalization from the ideal readouts:

    Phihat=-3H0^2 a^-3 P What(1-r)/(2K^2).                   (7)

With B=rho0/(3H0^2 Fc)>0 the Weyl equation is exactly equivalent to

    Z_beta(q) P What=B(J+C),
    [Z_beta P What]_0^i=B(J_i-J_0).                       (8)

The endpoint equation removes C without setting it to zero. A common unknown
mode amplitude cancels. Once beta,B are fixed, C is reconstructed in that mode
normalization; this is inference within a supplied theory, not state selection.
For unrestricted F the same relation leaves the family F/[rho0/(3H0^2)]
=(J+C)/(P What). It is candidate geometry that restricts the family.

The 3DeltaPhi term is retained, so (8) uses exact linear dust kinematics,
conditional on (2). Omitting it is a separate leading-continuity approximation.
W>0 does not imply J'>0: Phi'=-W/3 makes delta'=0. With a Weyl discrepancy
L=b delta/F+epsilon_L, b=rho0/(3H0^2), the undivided residual is

    [F P W]-b[integral W+3DeltaPhi]=[F epsilon_L].           (9)

Known endpoint bounds |epsilon_L,i|<=e_i imply a bound F_i e_i+F_0 e_0.
The physical errors e_i are not produced by the theorem. A time-dependent
velocity gain also changes J; it is not a cancelled constant normalization.

## 3. Finite-epoch admission without a preferred root

Choose three epochs with distinct J values; translate J0 to zero. Put
t_i=P_i What_i(1-3q_i). Eliminate B between the two endpoint equations:

    C0=t0(J2-J1), C1=-t1 J2, C2=t2 J1,
    Q(beta)=sum_i Ci product_{j!=i}(beta-q_j)=0.           (10)

This polynomial has degree at most two. If it is nonzero, enumerate every real
root; require 1/4<beta<1/3, 0<q_i<beta, nonzero denominators and positive B
recovered from one nonzero J difference. Retain all compatible roots and test
the rest of the interval, additional epochs and other modes. If Q is identically
zero there is no finite-candidate conclusion. These are strict exact-data gates;
small coefficients or nearly repeated roots are finite-precision issues.

A separately derived lift gives a useful alternative implementation. With
u_b=1/beta, v_b=1/B and w_b=u_b C,

    [1,-Jq,-q,-P What(1-3q)] . [C,u_b,w_b,v_b] = -J.      (11)

Four full-rank rows give at most one lifted solution. It must obey
w_b=u_b C, 3<u_b<4, v_b>0 and the chart gates. A linear fit that fails the
product constraint is rejected. Rank four is sufficient, not necessary, for
uniqueness. The positive construction (8) is necessary and sufficient for
the reduced Weyl/conservation/candidate-chart equations on the declared
interval. Euler is included only when (4) holds for the same measured E,P,P3.
No finite set of rows establishes an interval identity or full-action membership.

## 4. Exact classification of interval ambiguity

Suppose two distinct beta_j in (1/4,1/3), B_j>0 and C_j satisfy (8) on an
interval with positive P,What and 0<q<min(beta1,beta2). Put a_j=B_j/beta_j.
Cancelling the common readout yields

    a1(beta1-q)(J+C1)=a2(beta2-q)(J+C2),
    q(J)=[a1 beta1(J+C1)-a2 beta2(J+C2)] /
          [a1(J+C1)-a2(J+C2)].                            (12)

The denominator cannot vanish: equality would then force a positive common
a_j(J+C_j) times beta1-beta2 to vanish. Thus, on a nonconstant J range with
varying q, a second shape requires q to be fractional linear in J. An exact
non-Mobius q(J) admits at most one shape, if a solution exists. This is an
exact-function statement, not a noise-tolerant uniqueness guarantee.

Conversely suppose candidate1 satisfies (8), J ranges over an interval and
the observed q varies as (u0 J+v0)/(w0 J+x0), with nonzero determinant
u0*x0-v0*w0 and denominator. Then the only possible distinct finite second
tuple is

    beta2=(v0-u0 C1)/(x0-w0 C1),
    C2=(beta1 x0-v0)/(beta1 w0-u0),
    B2=B1(beta2/beta1)(beta1 w0-u0)/(beta2 w0-u0).         (13)

Require all denominators, distinct beta, positive B2 and the interval chart.
For proof multiply the shared readout by w0 J+x0. Its two representations
are `(B_j/beta_j)[(beta_j w0-u0)J+beta_j x0-v0](J+C_j)`.
For distinct shapes the first linear factors have no common root, since their
determinant is (beta1-beta2)(u0*x0-v0*w0). Exchanging the two roots gives
(13), and substitution proves sufficiency. If beta1 w0-u0=0 the first side
has degree one and a distinct finite positive-B second tuple cannot match it.
If x0-w0 C1=0, the proposed second shape has no finite value. A repeated root
returns the original tuple, not a second one. A formal beta2 can also have
B2<0 and must be rejected. The rational evaluation at -C1 is algebraic
continuation, not an observed zero-density epoch. Constant J or constant q
is separate; for constant q, nonconstant J and compatible affine P What,
every chart-admissible beta can rescale B.

An exact example on a common interval around 0<=N<=1 is

    J=N, What=1, q=9/50-N/25,
    beta1=29/100, B1=1/5, C1=2,
    beta2=13/50, B2=26/145, C2=11/4,
    P=10(N+2)(4N+11)/[29(6N+23)].                          (14)

Both tuples satisfy (8) at every epoch. This example uses leading continuity
J=N; it is not relabelled as exact relativistic continuity or as two full
cosmological solutions. The independently constructed fractional-linear
example and the general proof corroborate the ambiguity.

An independently calibrated tensor coefficient ratio T_F=F_j/F_i at distinct
q_i,q_j adds a discriminator. Define U=T_F(1-3q_i)/(1-3q_j); then

    beta=(U q_j-q_i)/(U-1).                               (15)

For distinct q the candidate ratio Z_beta(q_j)/Z_beta(q_i) is injective in
beta away from poles. An unscreened, source/detector-calibrated propagation
distance ratio would give T_F=(dLGW_i/dLEM_i)^2/(dLGW_j/dLEM_j)^2.
This last identification is conditional transport physics. Equal local endpoint
F can erase cosmological sensitivity; GW170817 does not supply the history
used here. No tensor observation is fitted.

## 5. Background equations are additional tests

The supplied radial Jordan action is F R/2-omega(F)(partial F)^2/(2F)-V(F),
with omega=(1/q-3)/2. Its flat dust metric equations are

    3F H^2=rho+omega Fdot^2/(2F)+V-3H Fdot,
    -2F Hdot=rho+omega Fdot^2/F+Fddot-H Fdot.              (16)

Writing Z=F/Fc, Y=E^2 and using (8)'s B gives

    (2Z+Z')Y'/2+[Z''-Z'+omega Z'^2/Z]Y+3B a^-3=0,        (17)
    Y'/2+(P3+2)Y=(3/2)P a^-3(1+r).                      (18)

The second line is Euler. Let L1=2Z+Z', L0=Z''-Z'+omega Z'^2/Z and
D=P3+2. Their algebraic elimination is

    (L0-L1 D)Y+a^-3[(3/2)L1 P(1+r)+3B]=0.                (19)

If the Y coefficient is nonzero this gives a necessary Y; its derivative
must still satisfy (18). Zero coefficients require rank/consistency checks.
Alternatively a physically measured E can test (17) directly. No choice of
potential fixes a failure of this necessary kinetic equation.

For (14), additionally specify the light response r=q. Both forced Y(0)
values are positive, but the Euler residuals after differentiating the forced
Y are nonzero:

| beta | Forced Y(0) | Residual of (18) at N=0 |
| --- | --- | --- |
| 29/100 | 13384899/30100376 | -43561803701691/156212523334720 |
| 13/50 | 7664652/16404865 | -541963083069/1855997211505 |

Thus these two manufactured readouts fail full background-plus-Euler
compatibility under r=q. This is not empirical rejection of the scalar theory,
nor rejection of a finite-mass response with unspecified r.

The relative potential from (16) is

    V/(Fc H0^2)=Z(3Y+Y'/2)-3B a^-3/2
               +Y Z''/2+Y' Z'/4+(5/2)Y Z'.              (20)

For the supplied Einstein potential U=B0+nu B1, where

    B0=3/2+3s(X-1)^2/(2T^2), B1=(1+s)u^2/(2T^2),
    X=1/[s(Z-1)], u=ln X/(2sqrt(beta)), T=1+sX,
    Q/Fc=4beta/(1+k),

the conformal relation V=2Q Hv^2 U/A^4 gives

    V/(Fc H0^2 Z^2)=ell B0+tau B1,
    ell=2(Hv/H0)^2/(Q/Fc)>0, tau=ell nu>0.               (21)

Nondegenerate pairs calibrate ell,tau and later times test them. Neither these
calibrated ratios nor beta are a derivation of why the action has this form.
All reduced observables and the background equations retain the common
rescaling (F,Fc,rho0,Q0)->lambda(F,Fc,rho0,Q0); a separately calibrated
absolute source/normalization would be additional information. A change of
units alone supplies no dimensionless gravitational hierarchy.

## 6. Forward controls, retained failures and empirical limits

The first working inverse checked 48 exact manufactured profiles. It passed
259 controls but omitted the explicit q>0 software gate. A focused reviewer
constructed a negative-q input accepted by that version. Original source,
returns and witness remain unchanged; the current helper requires finite real
0<q<1/3 and tests that witness and zero/nonfinite inputs. The theorem itself
already required positive q. Four of the 48 profiles retained two roots at
the fourth epoch; that outcome motivated (12)-(13) and was not filtered out.

The extended working controls checked the exact lift, ambiguity, dust correction,
domain repair and background equations: 48 passed. Separately, three supplied
radial Einstein backgrounds and two modes per background were integrated with
the conditional r=q perturbation equations. For Phi=-cphi delta,
cphi=rho(1-q)/(2F K^2), exact linear dust continuity gives

    delta'=(W-3cphi' delta)/(1+3cphi),
    cphi'/cphi=-1-F'/F-q'/(1-q), I'=W.                   (22)

Euler is (1); the solver evolves I independently. The inverse receives only
q reconstructed through (4), P, What and J=[I+3(Phi-Phi0)]/W0 at the first
three fixed epochs. The generating beta,B and initial contrast are used only
afterwards to assess recovery. Three later synthetic epochs are separate
residual tests. Both modes share one background and have different initial
amplitudes; they are not independent empirical tests.
The order-unity contrasts are a linear mode normalization, not a physical claim
of nonlinear perturbation validity; all perturbations can be scaled together.
The continuity residual uses absolute normalized error despite the frozen
protocol key containing the word "relative"; the later identity residual is
relative. Returned candidates are also gated at every sampled epoch. No sampled
gate certifies unsampled times.

All 60 forward working controls passed at the frozen tolerances. The first
output write failed on a numpy Boolean after calculation; its partial output
and source remain preserved. A versioned serialization repair reran the same
cases, epochs and thresholds. The background equations come from the supplied
radial action; the perturbations still use (2), not the complete dynamical
scalar/metric system. ODE tolerances and extra inverse arithmetic precision
are computational settings, not rigorous error enclosures or observed digits.

The current executable and exact identities are bound in the linked review
record and source-bound cache. Independent derivations cover the inverse,
ambiguity, background equations and physical-source convention. Source
comparison is distinguished from blind derivation and numerical replication.
Neither passing controls nor reviewer agreement supplies a physical premise.

Actual ACT spectra use line-of-sight windows, transfer/bias/magnification
corrections and a correlated RSD beta likelihood. The necessary RSD machinery
is described in [Wenzl et al., arXiv:2401.12971v2](https://arxiv.org/pdf/2401.12971v2).
Sample-level beta=f/b is not W or P3. Finite E_G points cannot supply continuous
P3, common-mode integrals or their derivative errors without additional modeling.
The legitimate empirical continuation is to predict the actual bandpowers
through their windows and joint covariance. The exact numerical release has
not been admitted; a bounded unsuccessful search is not evidence of absence.

## 7. Obligation graph and claim boundary

The proof chain is: explicit physical input map and dust/response premises ->
Weyl/force quotient (3)-(5), proved algebraically -> candidate geometry (6),
directly differentiated -> conserved density identity (7)-(9), proved -> finite
admission (10)-(11), elimination with gates -> interval ambiguity classification
(12)-(13), linear-factor proof -> optional tensor/background discrimination
(15)-(21), with their extra physical premises retained. The strongest new
checked mathematics is the complete exact second-shape classification on the
varying-J chart together with the initial-density-free admission construction.
The lift was independently proposed by the focused checker and personally
verified by root; its independent origin is recorded.

The strongest missing supplier is a calibrated observation-to-response map
with controlled dynamical scalar/metric errors or a full dynamical substitute
for (2). It is not a terminal lemma claimed proved. The current candidate
geometry, action/potential choice, physical initial scalar history, environmental
matching and absolute calibration remain open beyond the stated conditional
construction. Registered scale, kinetic-isotropy and realized-state primitives
retain their exact registered scope; none supplies the measured histories or
the state-selection/response equations asserted as premises here.

The scope checklist (`.claude/science/physics-loops/observations-backward-24h-20261014/growth_bridge/NO_GO_DISCIPLINE_CHECKLIST.md`)
and review record (`.claude/science/physics-loops/observations-backward-24h-20261014/growth_bridge/REVIEW_RECORD_v1.md`)
separate constructed counterexamples from universal impossibility. No formal
audit, complete TOE, unconditional framework derivation or observational
confirmation is claimed. The [source-bound log](../logs/runner-cache/scalar_growth_lensing_inverse_check.txt)
is executable evidence only; independent review before landing and audit
ratification remain separate.
