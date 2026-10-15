# Scalar constraints as finite shear and velocity pair statistics

**Date:** 2026-10-15
**Status:** conditional-support
**Claim type:** bounded_theorem
**Primary runner:** [scalar_unequal_pair_check.py](../scripts/scalar_unequal_pair_check.py)

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: revised_scalar_action_potential_scale
target_blocker_text: Derive or eliminate the remaining scalar action, state, scale and measurement assumptions
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: Necessary scalar constraint as an unbiased finite-pair ensemble statistic under the stated field law, geometry, statistics and calibrated sampling conditions
hypothetical_axiom_status: none proposed
admitted_observation_status: Primary-source context and synthetic controls only; no survey data or empirical test
claim_type_reason: Explicit differential elimination, angular quotient, adjoint and finite-sampling proof with an error functional and stated conditions
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: Establish an actual pair-selection/window/uncertainty supplier or derive a further observable that eliminates it
```

**Exact target.** Derive a nonzero necessary test of candidate scalar coefficients
from a finite weighted shear/velocity pair statistic in ensemble expectation.
The construction eliminates the latent velocity-potential boundary, missing
full-sky angular modes and the exact equal-epoch diagonal. It neither selects
an initial state nor establishes the supplied dynamics or sampling model.
It is not a coefficient-uniqueness, precision, full-history sufficiency or
observational-detection theorem.

The local field-law premise below is derived conditionally for the rolling
scalar/dust model in [M14](SCALAR_DYNAMICAL_MOMENTUM_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md).
[M15](SCALAR_PROJECTED_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-15.md)
constructs the preceding ideal equal-epoch test; its continuum supplier is
not imported as observed data here. This note states the complete local-law
premise and proof. Root personally derived the normalized elimination,
explicit annihilator, adjoint construction and sensitivity witness. Standard
Born inversion, integration by parts and importance sampling are not claimed
as new discoveries. No global literature-priority or formal audit claim is made.

**Admitted domain.** Use units c=1, flat expanding physical Jordan geometry,
N=ln(a), H=dln(a)/dtJ, S=Phi+Psi, V=H vJ, and scalar proper velocity
v_phys=grad(vJ)/a. Signals have smooth homogeneous/isotropic unequal-time
second moments and finite integrals sufficient to commute the displayed
derivatives, expectations and integrations. No Gaussianity, stationary time
law, growing mode or chosen initial covariance is assumed. Covariances may
replace second moments when the true ensemble means are handled; estimating
means from the same catalogue introduces a separate window operator. The
field equation, Born/scalar approximation, geometry, measurement identification
and selection/error conditions are hypotheses, not observational results.

Choose each real smooth test weight and candidate coefficient history before
examining the tested data, or supply a separate procedure for data-adaptive
inference. Calibration/development observations cannot become independent
holdouts through this construction. No observed dataset is used below.

## Geometry and elimination

Use physical Jordan N=ln(a), H>0, alpha=1/(aH), chi_N=-alpha. Positions are
x_i=chi_i n_i; r=|x_2-x_1| and mu=n_1.n_2. Work on a compact interior chart
of |chi_1-chi_2|<r<chi_1+chi_2, r>0, with p_1 p_2 nonzero. All N_1
derivatives below fix r and N_2, not the observed angle. In observed coordinates,
partial_1|r = partial_1|mu + chi1_N (chi1^2-chi2^2+r^2)/(2chi1^2 chi2) partial_mu.
This is a one-leg derivative, not the simultaneous equal-shell derivative. Write

    p_1=(chi_2 mu-chi_1)/r, p_2=(chi_2-chi_1 mu)/r,
    C_Su=alpha_2 p_2 J, J=partial_r C_SV,
    C_uu=-alpha_1 alpha_2[p_1 p_2 R_r+(mu-p_1 p_2)R/r],
    R=partial_r C_VV.

This is direct differentiation of an isotropic covariance, not a growth-law
or initial-state model. S belongs to leg1. The supplied local law is
partial_1 S-y partial_1 V=a0 S+c0 V
(M14: a0=(y-x-2)/2,c0=-hy-m).
Define

    gamma=(mu-p_1 p_2)/(p_1 p_2 r), P=partial_r+gamma,
    G=-C_uu/(alpha_1 alpha_2 p_1 p_2),
    T=y partial_1+c0, D=partial_1-a0, d=D J.

Then P R=G and T R=d. Let U=partial_chi1 gamma, b=y chi_1,N1,
L=U P-U_r and F=T G-P d. Since [T,P]=b U, F=b U R, hence

    H=L(T G-P D J)-b U^2 G=0.                         (1)

No division by b or U is used in (1). Thus vanishing y or U does not invalidate
necessity, though it can remove information. If bU is nonzero, additional
temporal compatibility can reconstruct R locally; (1) alone is not a
sufficiency or parameter-identifiability theorem. No PSD/full-history
converse is asserted. p_1 p_2=0 remains outside this chart.

## Removing unmeasured angular modes

Let A=chi_1,B=chi_2,delta=A^2-B^2, q_-=r^2-delta,q_+=r^2+delta.
Then p_1 p_2=(delta^2-r^4)/(4ABr^2) and

    gamma=[2r^2(A^2+B^2)-r^4-delta^2]/[r(delta^2-r^4)].

The full-sky shear inverse loses ell0,1. In the isotropic S-u correlation,
the missing terms are arbitrary a(N1,N2)+b0(N1,N2)mu. Dividing by alpha2 p2
maps these into span{r,r/q_-}. A fixed-r N1 derivative adds only r/q_-^2
to that span; arbitrary time-dependent coefficients remain arbitrary.
Thus the nuisance in H lies in span{LP r, LP(r/q_-), LP(r/q_-^2)}.

Exact rational reduction gives denominators respectively q_-^4 q_+^4,
q_-^5 q_+^4,q_-^6 q_+^4. Their numerators are even polynomials with common
r^4 and degrees at most12,8,10 respectively. Therefore with

    W=q_-^6 q_+^4/r^4, K=r partial_r,
    Z=[product_{j=0}^6(K-2j)] W,

ZH is independent of the missing angular coefficients. Multiplication W
acts first. This follows because each W LP nuisance is a polynomial in r^2
of degree at most6, which the seven Euler factors kill. This is an explicit
geometry-derived annihilator; no nuisance coefficients are fitted or supplied.
It also removes some genuine signal. Sensitivity, conditioning and arbitrary
angular masks cannot be inferred from cancellation alone.


For an explicit expansion let t=r^2, d=A^2-B^2, v=B^2. Then

    WLP r = -32 A (t-d)^2 P0(t),
    WLP(r/q_-) = -64 A^3 (t-d) P1(t),
    WLP(r/q_-^2) = -64 A P2(t),
    P0 = t^4-(4d+2v)t^3+(6d^2+16dv+2v^2)t^2
         -(4d^3+18d^2v+20dv^2)t+d^4+4d^3v+10d^2v^2+8dv^3,
    P1 = (2d+v)t^2-(4d^2+6dv)t+2d^3+5d^2v+4dv^2,
    P2 = (2d+v)t^3+v^2 t^2-(6d^3+7d^2v+2dv^2)t
         +4d^4+14d^3v+13d^2v^2+4dv^3.

These follow by differentiating the displayed rational gamma, with A,B
independent. Since K=2t partial_t, the annihilation follows term by term.

## Weak functional in two independent distances

Use compact smooth weights w(N1,N2,r) strictly inside the chart, with measure
dN1 dN2 dr. Formal adjoints are

    Z* w=W product_{j=0}^6(-K-1-2j)w = z,
    P*=-partial_r+gamma,
    L*f=-partial_r(U f)+(U gamma-U_r)f,
    T*f=-partial_1(y f)+c0 f,
    D*f=-partial_1 f-a0 f.

For eta=1/(alpha2 p2), beta=-1/(alpha1 alpha2 p1 p2), set

    K_uu=beta[T*L*z-b U^2 z],
    K_Su=-eta D*P*L*z.                                (2)

Then integral(K_uu C_uu+K_Su C_Su)=0. All derivatives hit weights and
candidate/geometry coefficients; none hit measured correlations. Smooth
compact support removes boundary terms, including moving chart boundaries.
This is an expectation constraint, not an identity for every finite sky
realization. Finite regularity alternatives require their own boundary proof.
The coefficients can be challenged using multiple prespecified weights;
uniqueness or a useful parameter rank has not yet been proved.

For fixed kernels, a supplied pointwise correlation-error envelope gives
|delta I| <= integral(|K_uu|epsilon_uu+|K_Su|epsilon_Su).
Unknown geometry, candidate-dependent kernels and sample variance are not
automatically covered. They require their own delta-kernel/error terms.

## Pullback to measured shear and radial velocities

Use chi1,chi2,mu coordinates. The absolute volume factor is
Jgeom=chi1 chi2/(alpha1 alpha2 r). Put k=Jgeom K for both terms.
Because the nuisance cancellation holds for arbitrary time coefficients,
k_Su has zero angular moments against1 and mu at each chi1,chi2.

On each observable ell>=2 Born mode,
psi_lm(s)=integral_0^s(1/chi-1/s)S_lm(chi)dchi and
S_lm=partial_s(s^2 partial_s psi_lm)=D_s psi_lm. Require the
corresponding integrability near the observer. No finite or known observer
monopole/dipole lensing potential is required or reconstructed. D_s is self-adjoint in ds on
these compact weights. Move it onto k_Su at fixed angular directions, after the coordinate change.
Next use the full-sky spin-2
map gamma_lm=h_l psi_lm, h_l=1/2 sqrt[(l-1)l(l+1)(l+2)], l>=2.
The scalar weight has no l0,1, so its adjoint inverse is well-defined:
divide its harmonic coefficients by h_l and use spin-2 harmonics. Pair the
result with shear by Re(q* gamma). This moves the entire inverse onto a
known smooth weight. It does not reconstruct individual missing modes.
The angular inverse generally destroys compact angular support: full-sky
coverage, or a separately proved masked inverse, is still a condition.

Statistical isotropy converts integral dmu k C into
(1/(8pi^2)) integral dOmega1 dOmega2 k(n1.n2) E[signal1 signal2].
Both source distances stay independent. Unlike an equal-epoch diagonal,
the resulting pair weight contains no delta(chi1-chi2).

## Finite sampling and the remaining physical assumptions

For independent disjoint catalogue draws of fixed sizes n_s>=1,n_v>=2
from known positive p_s(chi,n),p_v(chi,n)
with respect to dchi dOmega and positive over the full pulled-back weight support,
positions independent of the latent field, and measurements conditionally
unbiased and with zero cross-object/cross-channel noise products conditional
on the latent fields and all sampled positions (or with those conditional
products supplied and subtracted), the cross-pair
average of Re(q* e_i) v_j/(p_s p_v) and the ordered distinct velocity-pair
average of k_uu v_i v_j/(8pi^2 p_v p_v) estimate the two integrals above.
q includes D_s and the 1/(8pi^2) angular factor. Their sum has zero ensemble
expectation under the conditional field law. Pair averages use n_s n_v and
n_v(n_v-1), respectively. Integrability must hold; no finite variance or
observational error bar follows from unbiasedness alone.

This is a conditional mathematical supplier for a finite statistic, not a
claim that galaxy positions are field-independent or selection functions,
shear calibration, true distances and peculiar velocities are already known.
Density-biased tracers, correlated noise, intrinsic alignments, redshift
mapping and survey masks require explicit treatment. More pairs do not erase
cosmic variance in a fixed survey. A fixed finite grid cannot exactly integrate
arbitrary smooth correlation functions: a bump between sample points gives
a direct counterexample. Random sampling targets an expectation instead.

## Nonvacuity on a positive covariance family

Let g(x)=sqrt(2) cos(k.x+theta), theta uniform and k~N(0,2lambda I),
lambda>0 independent. This bounded homogeneous/isotropic ensemble has
C_g(r)=exp(-lambda r^2), so positivity is established by an explicit random
field rather than an arbitrary radial function. Take V=e^N g and
S=[(y+c0)/(1-a0)]e^N g with constant y,a0,c0, a0!=1. The supplied local law
holds. For example y=2/5,a0=-83/100,c0=-3/5 with alpha=1,h=-1 corresponds
to x=3/50,q=3/20,m=1 at the coefficient level. No full gravity/background
solution is asserted; this is a kinematic field-law witness.

Changing only the tested c0 by dc changes the final constraint by
dc Z L P R, where R=-2lambda r exp(-lambda r^2)e^(N1+N2). After removing
the positive time factor and Gaussian, WLP R is an even polynomial of degree16
in r, with leading coefficient32 chi1 lambda^3. Applying the seven Euler
factors gives degree30 with leading coefficient -4096 chi1 lambda^10.
Thus the operator does not vanish on this positive-covariance family.
The checked interior point chi1=2,chi2=3,r=5/2,lambda=1/2 has nonzero response.
A compact sign-consistent weight in a sufficiently small neighborhood then
has nonzero expectation for that wrong candidate. This proves existence of
a discriminator, not parameter uniqueness, useful signal/noise, full-solution
embedding or success on an observed survey.


## Actual selection, windows and uncertainty remain to be supplied

For a general selected catalogue, let lambda_ab^(2) be its joint ordered-pair
intensity with respect to the declared product measure, including pair count.
Require this intensity to be known and strictly positive wherever K is nonzero,
and require absolute integrability of the weighted first moment below.
Let C_ab^pair be the response-corrected mark product conditional on a selected
pair. Linearity of the marked counting measure gives

    E[sum_pairs K Y/lambda_ab^(2)] = integral K C_ab^pair.

This equals the desired field functional only when C_ab^pair=C_ab, or a
justified correction supplies that equality. There is no extra normalization
by the random number of observed pairs. The independent-draw theorem above
is one sufficient case. A known field-conditional pair intensity can instead
cancel selection conditional on the field under the analogous positivity and
integrability conditions, but an unobserved such intensity
is not an operational correction merely because it appears in a formula.

Exact witness: a latent mark product is1 or3 equiprobably, with inclusion
probabilities1/4 or3/4. The marginal inclusion probability1/2 is known;
inverse marginal weighting returns5/2 in expectation rather than the target2.
Field-conditional inverse weighting returns2. This shows the missing premise,
not a universal failure of catalogue methods. A random catalogue that encodes
a mean selection function does not automatically remove mixed density-signal
moments. Ratio estimators with random normalization need their own expectation
calculation; the ratio of expectations is generally different.

Once selection permits a justified linear two-point response C_obs=A C+B,
a data weight g tests the desired kernel K if A* g=K on the admitted signal
space and B is removed. An approximate adjoint equality contributes
integral(A*g-K)C, which needs its own bound. Finite redshift/photo-z windows,
noisy distances and masks do not automatically represent our prescribed K.
Noise correlated with positions or signals can invalidate the linear form
itself. The theorem does not supply the actual A, B or error bound.

Unbiasedness is not precision. The variance includes shared-object and cosmic
four-point terms; an increasing pair count does not count independent skies.
For a supplied variance bound V, Chebyshev gives
Pr(|Ihat-E Ihat|>=t)<=V/t^2. No such observational V is derived here. Even the
importance estimator1/(2x) for x drawn from p(x)=2x on(0,1) has mean1 and
infinite variance. Thus integrability alone cannot supply a rejection threshold.
For uncertain weights, the fixed-kernel bound above must also include the
kernel-error and error-cross terms. High derivative order and small projection
factors can make this construction impractical despite exact algebra.

Primary context is scoped, not used as a fitted proof premise:
[Taylor v1](https://arxiv.org/pdf/astro-ph/0111605v1) for flat-Born conventions;
[Schneider et al. v1](https://arxiv.org/pdf/astro-ph/0206182v1) for finite weighted
shear estimators and covariance terms;
[Schmidt et al. v3](https://arxiv.org/pdf/0904.4703v3) for density/selection
couplings;
[Wang et al. v1](https://arxiv.org/pdf/2108.08036v1) for finite radial-velocity
pair weighting; and
[Davis and Scrimgeour v2](https://arxiv.org/pdf/1405.0105v2) for distance/redshift
and velocity identification. Their fitted cosmologies, Gaussian closures,
mock corrections and numerical parameters are not imported. Exact source
versions, reading scopes and independent measurement findings are recorded in
[the source report](../.claude/science/physics-loops/observations-backward-24h-20261014/unequal_window/independent_observation_v1/REPORT_v1.md).

## Verification, failures and permissible use

The primary runs two declared helpers. Geometry checks use independently
assembled Cartesian polynomial contractions, generic commutators, exact
rational nuisance polynomials and the bounded positive-covariance witness.
The weak/sampling controls integrate generic nonconstant-coefficient operators
exactly, check Born inversion and explicit Legendre spin integrals, and
exhaustively enumerate finite catalogue positions with unequal selection
probabilities. Generic polynomial fixtures test the algebra and are not full
cosmological solutions. Finite enumeration is a discrete sampling control,
not a fabricated survey or a replacement for the continuum proof.

Preserved failures/qualifications: raw commutator tests are sensitive to a
missing monopole until the additional annihilator is applied; unconditional
noise decorrelation allows a weighted bias; fixed samples can miss a smooth
functional; a direct expanded Gaussian symbolic calculation was stopped after
172seconds without an assertion/result, then the same witness was evaluated
through exact conjugated polynomial operators. None of these failures is
relabelled as an empirical exclusion. No tolerance, fitted value or physical
case was changed to force agreement.

Independent derivations check the projection/elimination and the separate
weak/sampling proof, with original exposure scopes preserved. Final source
correspondence and current executable counts live in the paired summary and
review record. The explicit low-mode quotient removes a mathematical nuisance;
the random-design theorem replaces a continuous-history demand with stated
sampling conditions. It does not retire those conditions, select an action or
initial state, set physical scales, solve an environment, identify measured G,
or establish the revised scalar theory as a TOE.

The immediate next useful test is an actual calibrated pair-selection and
window-response supplier, or a new observable that eliminates that supplier.
Do not insert a convenient covariance or selection model and call it derived.
