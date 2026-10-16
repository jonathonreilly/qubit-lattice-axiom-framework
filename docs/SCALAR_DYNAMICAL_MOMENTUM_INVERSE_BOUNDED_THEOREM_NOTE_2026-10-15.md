# Scalar reconstruction with the free dynamical wave retained

**Date:** 2026-10-15
**Status:** conditional-support
**Claim type:** bounded_theorem
**Primary runner:** [scalar_dynamical_momentum_inverse_check.py](../scripts/scalar_dynamical_momentum_inverse_check.py)

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: revised_scalar_action_potential_scale
target_blocker_text: Derive or eliminate the remaining scalar action, state, scale and measurement assumptions
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: Exact momentum identification and equal-time covariance lift under a supplied canonical scalar and conformal dust action
hypothetical_axiom_status: none proposed
admitted_observation_status: Published lensing and growth products are exposed context; no full input history or independent empirical test admitted
claim_type_reason: A conditional inverse with explicit action, background, rank and physical measurement premises
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: Derive or test a calibrated observable covariance supplier and the remaining full-history field equations
```

**Exact target.** For every regular linear perturbation solution of the stated
canonical-scalar/conformal-dust action on a flat expanding background, identify
its common coefficients R, x and q from calibrated simultaneous mode data, or
from five independent equal-time covariance rows and their total time
derivatives, without choosing scalar initial perturbations or a quasistatic
response.

Root personally derived and implemented this construction. The implication
has explicit hypotheses; it is neither a fundamental action selection nor an
observational detection. Standard scalar perturbation equations, conformal
transformations and matrix perturbation bounds are not claimed as new. The
combined momentum inverse, covariance elimination and candidate tests are
derived here without asserting priority over all literature. The supplied
radial action is restated in section 6 so this proof does not depend on an
unmerged earlier note's conclusion.

## 1. Observational motivation and supplied premises

Lensing probes a projected metric combination, while velocities enter through
a separate tracer and redshift inference. The inspected
[ACT DR6/BOSS estimator, arXiv:2405.12795v2](https://arxiv.org/pdf/2405.12795v2),
Eqs. 1–7 and 14–19, forms projected spectrum ratios with windows, RSD and
calibration inputs. The [precision estimator, arXiv:2401.12971v2](https://arxiv.org/pdf/2401.12971v2),
Eq. 8 and Eqs. 14–20, needs velocity/bias relations in converting those spectra.
Neither inspected product is treated as an observed individual Fourier ratio
or the continuous covariance collection below. No raw maps, catalogues,
chains or numerical likelihood are fitted here. Those papers are development
context, not independent empirical tests of this scalar theory.

Use natural units and signature (-+++). The supplied action class is

    S = integral sqrt(-gE)[Q R_E/2 -(partial chi)^2/2 - V_E(chi)]
        + S_m[A(chi)^2 gE,psi],  Q>0, A>0.                 (1)

A and V_E are sufficiently smooth, matter is universally coupled pressureless
dust, and the homogeneous background is spatially flat. Write b=d ln A/dchi,
s=chi_dot and rho for Einstein dust energy density. Dots in sections 2–3 mean
Einstein proper time unless explicitly labeled Jordan time. Matter particle
number is conserved; its Einstein mass is proportional to A. The scalar and
dust perturbations are linear, with no other anisotropic stress. Wave numbers
are nonzero and comoving. The physical clock, spatial-mode calibration, channel
normalizations, derivative estimation and survey projection model are supplied
inputs, not consequences of (1).

Both scalar initial data remain arbitrary subject to the gravitational
constraints. No vacuum, growing-mode, common-transfer, Gaussian or zero-wave
preparation is imposed. A finite smooth ensemble and interchange of derivatives
with expectation are additional premises only in the covariance construction.
The action, actual background, physical measurements and absolute normalization
remain open as derivations from the framework. Approved scale-reference,
kinetic-isotropy and realized-state primitives keep their limited unit,
structural and pointwise roles; none supplies these particular functions,
measured histories or probability covariances. No registry or axiom is amended.

## 2. Full linear equations from the action

Set gE00=-(1+2phi), gEij=aE^2(1-2phi)deltaij. Equality of the two Einstein
potentials follows from vanishing linear anisotropic stress. Let u_i=partial_i v,
X=delta chi, Z=delta chi_dot, p=k_com/aE. The number contrast n is the contrast
of the **proper rest-frame particle-number density on Newtonian-gauge time
slices**; it is not the coordinate-volume contrast n-3phi. Thus delta_E=n+bX.

Background variation gives

    chi_dot=s,  s_dot=-3Hs-V_E,chi-b rho,
    rho_dot=(-3H+b s)rho,  H_dot=-(s^2+rho)/(2Q),
    3QH^2=s^2/2+V_E+rho,  aE_dot=H aE.                    (2)

The complete first-order perturbation system in this sector is

    phi_dot=-Hphi+(sX-rho v)/(2Q),
    X_dot=Z,
    Z_dot=-3HZ-[p^2+V_E,chichi+rho(b_chi+b^2)]X
          +4s phi_dot-2(V_E,chi+b rho)phi-b rho n,
    n_dot=p^2 v+3phi_dot,
    v_dot=-phi-bX-bs v.                                  (3)

Here is a direct derivation of the nontrivial source terms. Matter variation
has trace T=-rho, giving box chi-V_E,chi=b rho. Number conservation uses
sqrt(-gE)N u^0=aE^3 Nbar(1+n-3phi); its lapse terms cancel. The covariant dust
force is u^mu nabla_mu u_i=-b(partial_i X+s partial_i v), giving the last
line of (3). Expanding the scalar wave operator gives

    delta(box chi)=-Z_dot-3HZ-p^2X
                   +2phi(s_dot+3Hs)+4s phi_dot.           (4)

Use (2) and delta rho=rho(n+bX) in (4). This produces both rho b^2 X and the
matter-dependent lapse source -2b rho phi in (3). Dropping either is a changed
equation, not a choice of density convention with the rest held fixed.
The 0i metric equation is the first line of (3). Direct linearized Christoffel,
Ricci and Einstein tensors independently assemble its sign and factor in the
geometry helper, together with the 00 and pressure components.

After the 0i substitution, the undivided 00 constraint is

    C=(2Qp^2-s^2)phi+rho n+sZ
       +(V_E,chi+b rho+3Hs)X-3Hrho v=0.                  (5)

Differentiate C with (2)–(3), p_dot=-Hp, b_dot=b_chi s and
(V_E,chi)_dot=V_E,chichi s. Every term cancels except -3HC, hence

    C_dot=-3H C.                                         (6)

Likewise differentiating phi_dot gives identically

    phi_ddot+4Hphi_dot+(2H_dot+3H^2)phi
       =(sZ-s^2phi-V_E,chi X)/(2Q).                       (7)

These algebraic identities propagate the initial constraint and the spatial
trace. They do not repeatedly project the numerical trajectory onto a chosen
field response. With rho>0 choose finite phi,v,X,Z initially and solve (5) for
n; both X and Z remain free. In particular no division by 2Qp^2-s^2 is needed.
Smooth coefficients give the usual local linear initial-value solution; common
amplitude scaling preserves smallness on a fixed regular finite interval.

## 3. Physical-frame momentum identification

Define dtJ=A dt, aJ=A aE, HJ=(H+bs)/A, F=Q/A^2 and rhoJ=rho/A^4. Require
H+bs>0. With the explicit Jordan slots gJ00=-(1+2Psi),
gJij=aJ^2(1-2Phi)deltaij,

    Psi=phi+bX, Phi=phi-bX, S=Psi+Phi=2phi, T=Psi-Phi=2bX,
    vJ=A v, deltaJ=n-3bX, K=k_com/aJ, N=ln aJ,
    W=K^2 vJ/HJ, h=HJ'/HJ.                              (8)

Prime is d/dN along the same comoving mode. It is not a derivative at fixed
physical K or fixed angular multipole. Direct substitution in (3) gives

    deltaJ'=W+3Phi',
    W'+(2+h)W=-K^2 Psi/HJ^2.                             (9)

Thus W is not automatically f deltaJ in the full dynamics. The common Weyl
combination and physical-clock mapping agree with the limited classical
conformal scope of [Rondeau and Li, arXiv:1709.07087v1](https://arxiv.org/pdf/1709.07087v1),
§§IV–V: its A_paper equals this note's A^2, and its conformal-time derivative
must be converted by d/dN=(aJ HJ)^-1 d/deta. Its velocity notation alone does
not identify the H-normalized W. Observed redshift is aJ0/aJ-1.

Put q=2Qb^2>0, x=F'/F and y=x/q. The transformed Einstein momentum equation,
using Jordan-time dots only in the next line, is

    Sdot+HJ S=-rhoJ vJ/F +(Fdot/F)[-T/(2q)-S/2].          (10)

For example substituting Fdot/F=-2bs/A and T=2bX into (10) gives precisely
twice the first line of (3) divided by A. Neither p^2, scalar mass nor a
quasistatic approximation enters this identity.

Normalize aJ=1 at a reference epoch; H0=HJ there and E=HJ/H0. At an epoch use
calibrated real mode components (or enough real components of complex modes
with the same real physical coefficient vector). Where S and W are nonzero,

    P=-aJ^3 K^2 S/(3H0^2 W),  r=T/S,  P3=W'/W,
    M=P'+P P3=P(1+S'/S),
    R=rhoJ aJ^3/(3H0^2 F)>0.                             (11)

The last equality for M uses (aJ^3K^2)'=aJ^3K^2. Euler (9) gives
r=2E^2 aJ^3(P3+2+h)/(3P)-1, with no r=q replacement. Equation (10) becomes

    [1,-P_i/2,-P_i r_i/2] (R,x,y)^T=M_i.                (12)

**Three-mode theorem.** Three invertible real rows determine R,x,y uniquely.
If y!=0 and x/y>0, they determine q=x/y. A fourth row tests the same triple
without refitting. For any solution of (1), the recovered values equal its
physical coefficients; passing this necessary relation alone does not establish
all field equations or a full-history solution. Unknown constant common mode
amplitudes cancel, but relative channel gains and time-dependent normalizations
generally do not.

Rank is available within the conditional action. Set
c=2A aE^3(H+bs)/(3H0^2). Then P_i=-c phi_i/v_i and
P_i r_i=-cbX_i/v_i, so

    det L=c^2 b det[v_i,phi_i,X_i]/(4 v1 v2 v3).           (13)

For b!=0, nonzero v_i and independent triples, choose Z_i freely and solve
(5) for n_i. This proves compatibility with local initial-value solutions,
not a guarantee about cosmic preparation or observed rank. Proportional
triples fail; distinct wave numbers alone do not guarantee independence.
At s=0 and b!=0, x=y=0 and this instantaneous inverse does not identify q.
The canonical equations remain regular. A smooth limiting inference through a
turning point would use additional time information. b=0 is outside the q>0
chart. At S=0 or W=0 use the undivided constraint rather than inventing ratios.

## 4. Covariances and elimination of the separate time-leg input

Individual Fourier ratios are not survey spectrum ratios. Write
C_AB=Re E[A B*] on a common differentiable ensemble. Let D=aJ^3K^2/(3H0^2).
The undivided momentum equation is

    D(S'+S)+R W+(D/2)(x S+y T)=0.                        (14)

Correlating with W gives C_WW R+(D/2)(C_SW x+C_TW y)
=-D(C_S'W+C_SW). When normalized, P=-D C_SW/C_WW,
r=C_TW/C_SW and M=-D(C_S'W+C_SW)/C_WW obey (12). Euler supplies r using
P and gW=C_W'W/C_WW=(ln C_WW)'/2. However the product rule yields

    M=P'+P(2gW-eta), eta=C_SW'/C_SW,                     (15)

where the prime in C_SW' acts on W alone. The total derivative is
(C_SW)'=C_S'W+C_SW'. A common deterministic transfer W'=gW W suffices for
eta=gW; arbitrary free states do not impose it. Exact finite-ensemble examples
in the runner have eta!=gW. Equal-time C_SW and its total derivative alone do
not identify its first time leg. This statement concerns that smaller input
set; it is not a universal observational impossibility.

A larger equal-time collection removes the separate partial derivative. Define

    V=HJ vJ=W/(K/HJ)^2, J=3 exp(-3N)/E^2.

J is positive and common to simultaneous modes. Equations (9),(14) imply

    V'=h V-(S+T)/2,
    S'=-(1+x/2)S-yT/2-JR V,
    S'-yV'=a S+c V,
    a=(y-x-2)/2, c=-h y-JR.                             (16)

Multiply the last relation by (S-yV)*, take the real expectation, and collect
symmetric derivative pairs. At this epoch y is a coefficient; it is not being
differentiated. Hence only total equal-time derivatives occur:

    [(C_SS)' -2y(C_SV)' +y^2 (C_VV)']/2
       =a C_SS+(c-a y)C_SV-c y C_VV.                    (17)

**Five-covariance theorem.** Define the lifted vector
z=(x,y,y^2,JR-xy/2,JRy). Each mode gives the row

    [C_SS/2,
     -C_SS/2-(C_SV)'+(h-1)C_SV,
     (C_VV)'/2+C_SV/2-h C_VV,
     C_SV,-C_VV] z = -(C_SS)'/2-C_SS.                      (18)

Five independent rows suffice; no minimum-data claim is made. They determine z. Require the nonlinear consistency tests
z3=z2^2 and z5=(z4+z1*z2/2)z2. Then x=z1, y=z2,
R=(z4+xy/2)/J; positive R, nonzero y and positive q=x/y give the physical
rolling coefficient chart. Additional rows are no-refit tests. A generic
linear solution without the monomial checks is not a physical identification.
No direct slip covariance, coherent-mode phase or unequal-time partial
derivative is required by (18). Actual calibrated powers and their total
derivatives remain inputs. Finite uncertain data require joint error treatment;
the exact monomial test is not a statistical rejection rule for noisy data.

For rank availability substitute (16) into the columns in (18). They become

    [C_SS/2, x C_SV/2+C_ST/2+y C_VT/2+JR C_VV,
     -C_VT/2, C_SV,-C_VV].                              (19)

The transformation from (C_SS,C_SV,C_VV,C_ST,C_VT) has determinant 1/8 in
this ordering. Positive-definite covariances of (S,V,T) contain an open set,
so five independent rows exist. Finite ensembles realize these covariances;
with b!=0, finite S,V,T correspond to allowed phi,v,X and free Z, and (5)
fixes n. Small amplitude scaling preserves rank. The runner supplies six
positive-definite rational examples: five calibrate, one is reserved. No
assumption of independent bands is needed for the algebra, though correlations
must enter an actual measurement error model. The proof does not promise
well-conditioned rank in our universe.

## 5. Coefficient error enclosure and whole-background obligations

For (12), let Lhat and Mhat be supplied real fitted quantities with justified
absolute envelopes ePi, eri, eMi and already admitted normalized observables.
The exact product bound gives

    d=max_i [ePi+(abs(Phat_i)eri+abs(rhat_i)ePi+ePi eri)]/2,
    e=max_i eMi, n=||Lhat^-1||_infinity, eta=n d.

If eta<1, Neumann's inverse bound and
L(z-zhat)=(M-Mhat)-(L-Lhat)zhat give

    ||z-zhat||_infinity <= epsilon=n(e+d||zhat||_infinity)/(1-eta).

For abs(yhat)>epsilon,

    abs(q-qhat)<=epsilon(1+abs(qhat))/(abs(yhat)-epsilon). (20)

Rhat>epsilon and qhat greater than the latter error bound certify positive
**coefficients**, conditional on defined physical readouts. This does not
certify every S/W denominator or an achieved observational precision. An exact
reviewer witness has a P interval crossing zero while the coefficient enclosure
remains positive; the original broad label and witness are preserved. Failed
sufficient inequalities are inconclusive. All differentiation, projection,
calibration, numerical and covariance uncertainties must be in the supplied
envelopes. The implemented exact-decimal convention does not turn rounded
measurements into exact physics. The 512 corner controls test an application;
the norm proof establishes the interior bound. Equation (20) is for the
three-row matrix, not a claimed error analysis of the five-row covariance lift.

Conserved Jordan dust requires R'/R=-x; equivalently
R(N2)/R(N1)=exp[-integral x dN]. This yields relative F without a chosen
initial scalar state. Its absolute normalization stays tied to rhoJ0.
For q>0 put omega=(1/q-3)/2. Transforming (2), or varying the single-field
Jordan action F R_J/2-omega(F)(partial F)^2/(2F)-V_J(F), gives

    x'+(h-1)x+(omega+1)x^2+2h+3R exp(-3N)/E^2=0,
    vpot=V_J/(F H0^2)=3E^2(1+x)-omega E^2 x^2/2
                      -3R exp(-3N).                    (21)

The identities are checked directly from the Einstein background, with
V_J=V_E/A^4. They reconstruct a potential only along an admitted trajectory.
Off-trajectory completion, extra fields, absolute Q and the measured-force
identification of F remain open. These necessary background identities,
constraint propagation and the perturbation scalar/dust equations must still
be tested together; neither (12) nor (18) alone certifies a complete solution.

## 6. Supplied revised scalar family and potential tests

For the supplied family choose 0<k<1/3, beta=(1-k)(1+3k)/4 in (1/4,1/3),
alpha=sqrt(beta), s_m=(1+k)/[k(1-3k)], e_u=exp(2alpha u),
f=1+s_m e_u, j=1+(1-3beta)s_m e_u. Its radial coefficients are

    K_uu=j/f^2, A^2=C=(1+s_m)e_u/f, Q=Q0(1+k),
    U0=3/2+3s_m(e_u-1)^2/(2f^2),
    U1=(1+s_m)u^2/(2f^2), U_rad=U0+nu U1,
    S_E=Q integral sqrt(-gE)[R_E/2-K_AB partial phi^A partial phi^B-2Hv^2 U]
        +S_m[C gE,psi], Q0,Hv,nu>0.                     (22)

To state the transverse premise completely, call its two coordinates xi,zeta:

    R_perp=1+2(1+k)(xi^2+zeta^2)/3,
    K_xixi=(1+s_m)4k/(9f R_perp),
    K_zetazeta=(1+s_m)k/(3f R_perp), K off-diagonal=0,
    U=U_rad+(k/2)xi^2 exp[-(1-k)u/alpha]
            +(k/3)zeta^2 exp[-(1+k)u/alpha].             (23)

The homogeneous radial background xi=zeta=0 is an invariant truncation.
K_uu and A are transverse-independent, U_xi=U_zeta=0 there, and radial/transverse
mixed derivatives vanish. Consequently arbitrary transverse **linear** modes
have no first-order energy, momentum, radial source or matter coupling. Their
own equations retain initial data, with friction 3H+dot K_perp/K_perp and
mass term Hv^2 U_perpperp/K_perp. This is linear decoupling about that background,
not a physical selection of zero transverse amplitudes, a nonlinear theorem,
or stability inferred from potential curvature alone. A nonradial background
requires the full coupled treatment.

The dimensionful canonical coordinate satisfies chi_u=sqrt(2QK_uu),
V_E=2QHv^2 U_rad and b=(ln A)_u/chi_u. Direct differentiation gives

    Fc=Q s_m/(1+s_m)>0, F=Fc+[Q/(1+s_m)]exp(-2alpha u)>Fc,
    q=beta/j=beta(F-Fc)/(F-3beta Fc), 0<q<beta.

With constant kappa=3H0^2 Fc/(rhoJ aJ^3)>0,

    q/beta+R(1-3q)kappa=1.                               (24)

Two epochs solve linearly for (1/beta,kappa). On an exact member of this family
the determinant is (q1-q2)/kappa, so differing q gives uniqueness within the
chosen branch. Check beta in (1/4,1/3), kappa>0 and 0<q<beta, and test later
epochs with the same pair. Constant q does not select a pair; finite-epoch
agreement does not prove an interval identity.

Recover k=[1-2sqrt(1-3beta)]/3 and
exp(2alpha u)=(beta/q-1)/[(1-3beta)s_m]. Equations (21)–(22) then imply

    vpot C/2=gamma U0+gamma nu U1, gamma=(Hv/H0)^2.       (25)

Two independent basis rows determine gamma,gamma nu, with gamma,nu>0;
further epochs test the same values. This is reconstruction inside a supplied
functional family. Near u=0 the second basis is small and the inverse can be
severely ill-conditioned. It does not explain why this action, potential or
scale is physical. No fitted selector is counted as a derived action.

## 7. Proof obligations, controls and reproducibility

The obligation graph is explicit. Lemma A, action-to-linear equations and
constraint propagation, is proved in section 2. Lemma B, physical-frame mapping
and coefficient inverse, is proved in section 3. Lemma C, covariance elimination
and rank availability, is proved in section 4. Lemma D, coefficient error
propagation and relative background identities, is proved in section 5.
Lemma E is a conditional family membership/potential reconstruction, proved
from the fully supplied coefficients in section 6. The theorem composes A–D;
E is an optional candidate test. None uses survey summaries as its own target.
The strongest missing physical lemma is a calibrated observation operator and
error model supplying the required same-time spectra and derivatives, together
with full-history compatibility of the inferred action and measured gravity.
That lemma is not claimed solved by these finite algebraic inverses.

The primary imports all five calculation helpers and declares every local input.
It computes exact symbolic geometry, constraint/background identities, rank and
covariance examples, exact rational coefficient envelopes and a fixed numerical
protocol. The source-bound cache is generated by scripts/runner_cache.py using
the primary's declared timeout. No helper registry policy change is needed;
the actual generated packet inventory must still be checked before publication.
Run from the repository root:

    python3 scripts/scalar_dynamical_momentum_inverse_check.py

The fixed supplied numerical experiment uses Q=Hv=1, two radial backgrounds,
four modes per background and seven saved epochs. Initial X and Z are both
specified freely; only n is solved from (5). DOP853 evolves the complete
coupled system with rtol=2e-12, atol=2e-15 and a fixed maximum step. The first
three modes calibrate (12), the fourth is reserved. Epochs 0 and 2 calibrate
(24); epochs 3–6 are reserved, and epoch 1 is retained but not labeled a test.
The inherited protocol key reserved_scaled_max actually bounds absolute
dimensionless mode/candidate residuals; the runner and reports retain this
naming distinction without changing the threshold.

The two backgrounds' maximum |r-q| are about 0.183 and 0.327, so their successful
reconstruction does not rely on r=q. Independent canonical-state/log-aE Radau
integration, with independently assembled action derivatives frozen before
root-code exposure, agrees on all 56 mode rows at 14 epochs. The original
root 22 forward/equation controls and independent 16 controls are distinct from
17 later correspondence checks. Root's 301-time constraint diagnostic is not
represented as independently rerun; the separate check covers seven saved
epochs per background. Numerical samples are not rigorous integration enclosures.

Both histories have opposite signs of y at saved fractions .10 and .25.
Continuous exact histories with those signs contain an intervening zero; no
rigorous root enclosure was computed. The saved-epoch inverse therefore does
not establish uniform interval identification. Potential recovery is separately
diagnostic: raw basis condition numbers are about 9.76e5 and 1.07e5, and the
independent reconstruction confirms strong conditioning. Tiny residuals are
not observed precision. No new pass threshold is invented for that diagnostic.

## 8. Review record, source distinctions and remaining work

The pre-exposure independent equation proof has 30 exact controls; its subsequent
working-source correspondence has 14 separately labeled controls. The initial
correspondence script's BooleanAtom counting setup error is preserved; its
serialization repair changed no mathematics. The observed broad coefficient
certificate label was narrowed without changing its proved envelope. No failed
candidate or numerical comparison is hidden behind that wording repair.

The final source has 85 author controls. The first 24-variant damage run exposed
two surviving wrong error-bound denominators and two selector setup failures.
The original conservative corner fixtures did not discriminate those wrong
formulas. Two exact attained-bound witnesses now give state error 1/24 and
coupling-ratio error 1/16, exceeding the wrong bounds 1/26 and 3/52. Independent
pre-exposure algebra confirms both; the production envelope is unchanged.
An initial sharp-ratio fixture had the wrong sign in one supplied rational
entry and failed its unchanged baseline. That entire second mutation run is
invalid evidence and remains preserved. The corrected third run checks a clean
baseline first, then records 21 failed-check rejections and three exceptions
among 24 variants, with no survivor or selector failure. These are not 24
assertion rejections and do not exhaust possible implementation errors.

The earlier vacuum finite-mode note and the frozen local material inverse have
different background/source premises. Their complete notes were read. The old
vacuum Phi/Psi pair does not specify metric slots; a different naming convention
is consistent with (8), so no physical sign defect is asserted. The preceding
growth/lensing construction supplied a quasistatic scalar closure; this note
removes that closure from its displayed inverse by deriving the rolling momentum
constraint and retaining the free wave. The standard dynamical equations are
also compared, within constant-coupling scope only, with
[Amendola et al., arXiv:1407.2156v1](https://arxiv.org/pdf/1407.2156v1),
§II and §VI, Eqs. 77–81. Its later small-scale approximation is not used here.

The source reports separate pre-exposure derivation, post-exposure correspondence,
canonical-source confirmation and delivery checks. Their individual scopes and
immutable identities are preserved in the campaign pack. Full integrated-main
validation and formal audit remain pending. No author result ratifies a status,
and no merge or main push is part of this work.

The scope checklist (`.claude/science/physics-loops/observations-backward-24h-20261014/dynamical_response/NO_GO_DISCIPLINE_CHECKLIST.md`)
records the actual attempted routes and counter-routes. The mathematical
construction reduces initial-preparation, quasistatic and separate-time-leg
inputs to the inverse. It leaves action selection, the actual background and
initial history, absolute scale, environmental force calibration, and a usable
measurement likelihood unresolved. Next test a concrete observation operator
for the joint covariance collection; do not substitute a supplied common
transfer or ideal history for its derivation.
