---
title: "Chirped kinetic energy in the supplied massive free CAR vacuum"
claim_id: chirped_kinetic_energy_bounded_theorem_note_2026-10-13
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
assembly_status: publication_source_of_accepted_conditional_cores
scientific_execution: none_in_publication_source_preparation
runner: scripts/chirped_kinetic_identity_2026_10_13.py
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: partially_closes
conditional_surface_status: supplied massive free CAR model and vacuum; fixed compact smooth slots; bounded BV resources and strict frequency gap; conditional cell premises
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: two distinct accepted conditional derivations with their original hypotheses and exposure history
next_trace_action: root publication-source review and exact prepare/verify contract; effective retained audit remains separate
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies:
  - modulated_kinetic_energy_bounded_theorem_note_2026-10-13
  - general_compact_control_kinetic_energy_bounded_theorem_note_2026-10-13
  - two_zero_kinetic_energy_bounded_theorem_note_2026-10-13
  - kinetic_correlation_limits_bounded_theorem_note_2026-10-13
---

# Chirped one-time vacuum energy laws

Claim type: bounded_theorem

Status: conditional-support; bounded theorem publication source. The root V2
515-line proof and the independent 850-line proof below are distinct,
unchanged cores accepted for assembly by the ordinary root review of
2026-10-13. Historical pending-review wording inside them remains verbatim.
This current wrapper records the later disposition and adds no mathematics.
This publication wrapper binds the dated claim identifier, note and identity
runner to the accepted assembly. Source preparation does not execute that
runner or insert the claim in the graph. Root owns the subsequent integration
and regular PR. Effective retained status still requires independent audit.
The intended physical downstream consumer is not yet known; this upstream
support result supplies no physical selector or closed physical blocker.

## Common hypotheses and marginal conclusion

The supplied massive free CAR model, its specified vacuum and fixed positive
m,v are premises. The two real compact smooth control slots are fixed and
general; componentwise zero integrals are not imposed. On a fixed finite
slow-time interval [0,tau_star], a and Omega are real BV functions with fixed
finite bounds on amplitude, frequency and total variation, and with a fixed
strict lower gap ess inf Omega >= 2m+kappa for kappa>0. All spatial and model
resources stay fixed. The drive is

    lambda a(h^2 t) cos(phi_h(t)) V,   h=|lambda|,
    phi_h(t)=phi0+h^(-2) integral_0^(h^2 t) Omega(u)du,
    T=tau/h^2.

The phase is the integral of the BV frequency. Frequency jumps do not reset
the phase; isolated representative values do not change the dynamics.
Amplitude jumps, frequency jumps, amplitude sign and an arbitrary fixed
initial phase are allowed within the stated resources. Closing the gap,
diverging BV resources, varying control slots or the massless limit is outside
the common theorem.

Let r be the exact pair-energy density of the fixed control and supplied
vacuum, with the normalization in each core. The limiting one-time jump
measure and its energy law are

    Lambda_tau(de)=(pi/2) integral_0^tau
                      a(u)^2 r(Omega(u)) delta_(Omega(u))(de)du,
    characteristic function = exp integral (exp(i s e)-1)Lambda_tau(de),
    limiting mean = integral e Lambda_tau(de).

This is a family of one-time compound-Poisson probability laws for the free
energy. The exact mean is controlled separately with energy-weighted norms;
Wasserstein-one convergence uses that mean and positive-tail truncation.
These statements do not define a measured multi-time process, independent
emissions, a Markov approximation or a kinetic equation for every observable.

For constant Omega=omega the law is omega times a Poisson variable with
intensity nu_omega J_tau, where nu_omega=(pi/2)r(omega) and
J_tau=integral_0^tau a(u)^2 du. J_tau alone is not the Poisson intensity.
Piecewise constant profiles give the corresponding finite sum of jump
measures. Zero control, zero amplitude, or vanishing sampled density can
give Lambda_tau=0 and the point mass at zero. No positive response for every
allowed pair of slots or profile is asserted.

## Distinct strengths of the two proofs

Root V2 proves the marginal law, separate mean and W1 limit uniformly in
tau on the fixed kinetic interval for each fixed pair of BV profiles. Its
secular limiting argument is qualitative at that scope. It also explicitly
proves the full signed-input weighted Born remainder and the all-fixed-q
weighted full-operator estimate for Z-I with the stated square-root/logarithm
bound. An unbounded output weight is controlled in its graph norm before
taking estimates; it is not attached to an unweighted inequality afterwards.

Independent850 proves an O(h) secular estimate uniformly over the stated
bounded BV resource class. Together with its full-input Born comparison it
gives the fixed-characteristic-function and mean error at
eta_h=sqrt(h log(2+h^(-2))), and a qualitative W1 comparison uniform over
that profile class and the kinetic interval. No W1 rate is claimed. The
resource-uniform assertions, including comparison of h-dependent profiles
with their own Lambda_tau,h, belong to Independent850. Convergence to one
fixed law still needs convergence of that measure family. Root's subsequent
review separately checked these stronger arguments; they are not silently
attributed to root V2's fixed-profile secular proof.

Both proofs preserve the general-control threshold behavior and its time
moment limitation. The faster special zero-component-integral route keeps
its own hypotheses. The independent fixed-partition check recovers the
normalization and controls cross-block contributions; approximating a BV
frequency to fixed accuracy is not a proof of the full result, because the
phase error can accumulate as delta/h^2. This failed shortcut is preserved.

## Conditional application to actual cells

Cell transfer is conditional on the exact real energy embedding, unital band
Fock identification, exterior vacuum and common free energy, with the stated
finite-order control and commutator-form error bounds and fixed resources.
The one-particle control comparison is retained where the field comparison
needs it. A calibration label alone supplies none of these premises.
The common sufficient joint scale for the displayed mean and W1 transfer is
epsilon_ell=o(h^2); epsilon_ell=o(h) only supplies the weaker unweighted
state/law comparison at this level. For the stated finite order, the error
is O(ell^(N+1)). These are sufficient conditions, not optimality or necessity
claims and not a new construction of actual-cell calibration.

## Exact revisions, later review and publication parent

The root original515, SHA-256
03d2e4cd8c36b1ec5c5d04fb4efdaaefeae6b0346d58ad4885b1a292cb7a0d48,
was sealed at 12:04:15 UTC before the independent findings. Root V2 changes
exactly line247 to state the wavefunction of V|0> as i Delta/sqrt(2).
The creation commutator supplies this i and the Born Dyson coefficient -i
cancels it. The density and all response coefficients are unchanged.
Independent850 gives the phase correctly; its archived ANALYTIC_CHECKS
line72 is phase-suppressed shorthand, clarified by the precision record.
No frozen original has been edited. The complete eleven-line n=3 phase diff
is preserved alongside the original root and accepted V2.

The independent proof was frozen at 12:22:52 UTC with root chirp science
excluded. Its recorded preliminary heuristic exposure before its plan is
preserved. Comparison344 was frozen at 12:45:57 UTC after reading root515.
Its review of the independent author's own proof is an author self-check.
Root's later complete read and separate assessment are recorded in
CHIRPED_KINETIC_LAW_ROOT_REVIEW.md and acceptance9918f46b. Both derivations
use the same selected model family and shared parent machinery; this is not
model-diverse verification or a fresh independent review by the assembler.

The failed 62-character digest assertion, its corrected seal-bound identity,
and the later source-reading chronology remain archived. The earlier
original847 picture defect and missed root check remain historical evidence;
corrected859 and its review/repair confirmation are the accepted machinery.
The harmless phase precision here does not erase that earlier distinct error.

The modulated parent is now regular, OPEN, attached PR9517 at recorded head
c5eaa6bf752a0893c83c0509c7c349dab53bff14, as bound by the supplied creation
and attachment receipts. Its canonical note contains unchanged modulated464.
The earlier provisional statements in frozen sources remain historical.
The other three direct mathematical parents have exact canonical/core maps.
Initial-state publication, later branch ancestry and unrelated work create
no initial-state mathematical dependency for this vacuum theorem. This
publication preparation proposes branch physics-loop/toe-chirped-kinetic-energy-20261013
from that exact PR9517 head. Root creates/selects the child separately; the
source generator does not require CW to select it. The runtime contract
requires that exact clean branch and base before installation. This source
wrapper makes no new remote-status or current-main audit claim.

The four direct canonical proof parents are the
[modulated-drive theorem](MODULATED_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[general compact-control theorem](GENERAL_COMPACT_CONTROL_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[corrected two-zero theorem](TWO_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md), and
[correlation limits theorem](KINETIC_CORRELATION_LIMITS_BOUNDED_THEOREM_NOTE_2026-10-13.md).
The general parent also contains historical mean301; that containment does
not add a fifth dependency. Canonical parents retain their conditional scope.

## Unchanged root V2 core: fixed-profile law and weighted full-operator bound


# Kinetic energy marginals under a slowly varying carrier

Status: new conditional root derivation, awaiting a focused independent check.
The massive free CAR model and drive below are supplied premises. This is
original mathematics after exposure to its stated parents, not a physical
model selection, empirical prediction, formal certificate or retained audit.

## 1. Model, drive and claimed conditional result

Use the exact corrected full/interaction conventions of corrected kinetic859,
SHA c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b;
the full-input and threshold analysis of general470,
SHA 6bbcf624e47e4d91f2a6fbd8982698d788923bba63612f90d5930d04920ca49b;
and the bounded-variation amplitude extension464,
SHA 422a92a8a24daa8fa240251ccae041fcca737af0335a486f33f3b20de0fb665a.
All three have scoped ordinary analytic acceptance in their exact stated
domains. Their original pending wording and source-exposure history remain.
No conclusion from the new arbitrary-initial-state route is imported here.

On K=L2(R;C^2), let D(p)=-vp sigma_x-m sigma_y, E(p)=sqrt(m^2+v^2p^2),
P=(I+D/E)/2, P_-=I-P, m,v>0. Real conjugation is
Gamma hhat(p)=overline(hhat(-p)). The carrier is Fock(PK), with
H0=dGamma(E|PK) and vacuum Omega_vac. Inner products are linear in the
second argument and annihilation is antilinear. For a real slot k,
gamma(k)=a*(sqrt(2)Pk)+a(sqrt(2)Pk).

Fix real f,g in C_c^infinity(R;R^2), F=(f,g), M=2i[[0,1],[-1,0]],
B=FMF*, and V=(i/2)[gamma(f),gamma(g)] minus its vacuum expectation.
No componentwise zero-integral assumption is imposed. Fix tau_star<infinity
and real BV profiles a,varpi on [0,tau_star], with fixed resources

    ||a||_infinity<=A_star, Var(a)<=V_a,
    2m<omega_min<=varpi<=omega_max<infinity,
    Var(varpi)<=V_omega.                               (H1)

Bounds for BV representatives are understood up to changing isolated values.
Choose bounded one-sided representatives within the stated ranges. Such
changes have no effect on the integrals or propagators. For real lambda!=0,
h=|lambda|, and any real initial phase phi0 (which may depend on h), define

    Phi_h(t)=phi0+h^-2 integral_0^(h^2 t) varpi(u)du,
    A_h(t)=a(h^2 t), c_h(t)=A_h(t)cos(Phi_h(t)),
    T=tau/h^2, 0<=tau<=tau_star.                       (H2)

The phase is absolutely continuous, with derivative varpi(h^2 t) almost
everywhere, including when frequency has jumps. Let W solve H0+lambda c_h V,
Y=exp(itH0)W, S solve D+lambda c_h B, and Z=exp(itD)S, initially I.
Bounded strongly measurable interaction perturbations give these finite-time
unitary propagators. Their exact corrected covariance identities are

    Y*gamma(k)Y=gamma(Z*k),
    N=PZP_- Z*P,
    <W Omega_vac,H0 W Omega_vac>=||E^(1/2)PZP_-||_HS^2. (H3)

The last expression is a nonnegative energy form. Its finiteness is proved
below using energy cutoffs and the weighted estimates, not inferred from
state-norm convergence. W Omega_vac and Y Omega_vac have identical H0 laws.

Let r(e) be the exact exterior-pair energy density defined in section5.
Define a finite positive measure Lambda_tau on energy by

    integral b(e)Lambda_tau(de)
       =(pi/2) integral_0^tau a(u)^2 r(varpi(u)) b(varpi(u))du. (H4)

It is supported in [omega_min,omega_max]. Let CP(Lambda_tau) denote the
compound-Poisson probability law with characteristic function

    exp(integral (exp(ise)-1)Lambda_tau(de)).            (H5)

This law is delta0 when Lambda_tau has total mass zero. Otherwise it can
be constructed as the sum of N independent marks, N Poisson with parameter
Lambda_tau(R), marks distributed as Lambda_tau/Lambda_tau(R). This is a
representation of one probability law, not a claim about the dynamics of
an emission process, intermediate measurements or independent increments.

The conditional claims are, for each fixed q>=0 and small h,

    sup_tau ||E^(q/2)(Z(T)-I)||<=C_q eta_h,
    sup_tau ||E^(q/2)(Z(T)-I-K1_h(T))||_HS<=C_q eta_h,
    eta_h=sqrt(h log(2+h^-2)),
    K1_h(T)=-i lambda integral_0^T c_h(t)F_t M F_t*dt,
    F_t=exp(itD)F.                                    (H6)

Weighted operators in(H6) mean their bounded extensions, justified below.
Constants in these estimates are uniform within the fixed resources(H1),
the fixed model/slots, q and tau_star. For each fixed pair of profiles a,varpi,
the energy characteristic functions and means satisfy, for every fixed s,

    sup_tau |chi_h,tau(s)-exp(integral(exp(ise)-1)Lambda_tau(de))| ->0,
    sup_tau |<W Omega_vac,H0 W Omega_vac>
                                  -integral e Lambda_tau(de)| ->0. (H7)

In particular the exact energy laws converge in W1 to CP(Lambda_tau),
uniformly in tau in [0,tau_star]. No numerical rate for(H7) or W1 is claimed
for a general BV frequency profile. The initial phase is arbitrary and its
choice does not affect the limit. Negative lambda is included.

No threshold crossing, massless limit, diverging variation, moving spatial
slot, fixed-coupling all-time law, interacting spectrum or physical selector
is supplied. The one-time compound-Poisson law is not a multi-time theorem.

## 2. Nonstationary phase with BV derivative

Here is the scalar estimate needed instead of a fixed Fourier denominator.
Let psi be absolutely continuous on [l,r], v=psi' almost everywhere have a
real BV representative with |v|>=d>0, and let w be complex BV. Then

    |integral_l^r w(t)exp(i psi(t))dt|
      <=(2||w||_infinity+Var(w))/d
                                 +||w||_infinity Var(v)/d^2. (H8)

Indeed 1/v is BV and Var(1/v)<=Var(v)/d^2: for any two nonzero values
in this range, |1/x-1/y|=|x-y|/|xy|<=|x-y|/d^2. This also covers
opposite signs across a jump. Therefore
Var(w/v)<=Var(w)/d+||w||_infinity Var(v)/d^2. Since
d exp(i psi)=i v exp(i psi)dt, integrate w/v against this continuous
absolutely continuous function. Stieltjes integration by parts gives two
endpoint terms and an integral against D(w/v), proving(H8). The derivative
measure includes every jump; no piecewise differentiability is assumed.

The gap and variation of a phase derivative are distinct resources. An
estimate that replaces the constant frequency by its instantaneous value
inside a denominator without the variation term would be insufficient.

## 3. The causal square still has the kinetic gain

Set q0(t)=(1+t)^-1/2 for t>=0 and G(t)=F*exp(-itD)F. The exact stationary
phase input from general470 is

    G(t)=q0(t) sum_(alpha=+-m) exp(i alpha t)C_alpha+R(t),
    ||R(t)||<=C(1+t)^-3/2.                            (H9)

It holds with any fixed energy power and band inserted. It follows from
E=m+y^2 under the smooth odd momentum coordinate and the controlled Gaussian
Fourier remainder for Schwartz amplitudes. It is independent of the drive.

On L2([0,T];C^2), including its Hilbert--Schmidt amplification, let

    (L_h x)(t)=-i integral_0^t G(t-s)c_h(s)M x(s)ds,
    X(t)=F_t*Z(t), X0(t)=F_t*, X=X0+lambda L_h X.       (H10)

The row X(t) has HS norm ||F||_HS by unitarity. All finite-time Fubini
operations are thus legitimate; no HS norm is assigned to the identity.
Writing r=t-s, the exact square, with matrix order preserved, is

    (L_h^2 x)(t)=-(1/2)sum_(sigma=+-1) integral_0^t
                          H_sigma,h(t,s)c_h(s)M x(s)ds,
    H_sigma,h(t,s)=integral_0^r G(r-z)A_h(s+z)
                           exp(i sigma Phi_h(s+z))M G(z)dz. (H11)

A leading-leading term has amplitude b_r(z)A_h(s+z), with
b_r=q0(r-z)q0(z), sup b_r=q0(r), Var(b_r)<=2q0(r), and phase
alpha r+(beta-alpha)z+sigma Phi_h(s+z), alpha,beta in {+-m}.
Its derivative is beta-alpha+sigma varpi(h^2(s+z)), whose modulus is
at least d0=omega_min-2m and whose variation is at most V_omega.
The amplitude has sup at most A_star q0(r) and variation at most
(2A_star+V_a)q0(r). Estimate(H8) gives the bound

    q0(r)[(4A_star+V_a)/d0+A_star V_omega/d0^2].        (H12)

Every term containing R is bounded absolutely by C A_star q0(r), since
q0*(1+t)^-3/2<=Cq0. Hence a nonconvolution kernel majorant and Young's
inequality imply

    ||L_h||<=C0 sqrt(1+T), ||L_h^2||<=C2 sqrt(1+T).    (H13)

The constants depend on the fixed resources. The second bound is for the
operator square, not the square of the first norm. The exact identity

    (I-lambda L_h)^-1=(I+lambda L_h)(I-lambda^2 L_h^2)^-1

gives norm at most [1+hC0 sqrt(1+T)]/[1-h^2 C2 sqrt(1+T)]. For
T<=tau_star/h^2 the denominator is at least1/2 for small h and the numerator
is bounded. The argument works for any fixed finite tau_star; it does not
require h sqrt(T) to tend to zero or an absolutely small hT expansion.

## 4. Both full-input signs and weighted operator smallness

A constant-frequency translation of the old forcing profile is unavailable.
Instead split the input energy at a fixed distance from its threshold. On
input band epsilon=+-1, a leading term of L_h X0 has fixed matrix row
C_alpha M Fhat(p)*P_epsilon(p), a unit-modulus factor exp(i alpha t), and
scalar integral

    J_t(e)=integral_0^t q0(t-s)A_h(s)
                     exp(i sigma Phi_h(s)-i(epsilon e+alpha)s)ds,
    e=E(p), alpha in {+-m}, sigma in {+-1}.            (H14)

Choose b0>0 with 2b0<omega_min-2m. For m<=e<=m+b0 the derivative of
this phase has modulus at least omega_min-2m-b0. The amplitude has sup
at most A_star and variation at most A_star+V_a, because q0(t-s) is
monotone with variation at most1. Applying(H8) makes |J_t(e)| bounded
uniformly in t,h and near-threshold e. The input density in e is integrable
there (at most C(e-m)^-1/2), so this region gives bounded squared HS norm.

On e>=m+b0 the matrix-row spectral density is uniformly bounded. This
follows by changing from each momentum half-line to energy: the only inverse
Jacobian singularity is at m, and the spatial Fourier slots are Schwartz.
For each alpha,sigma, apply temporal Plancherel to
1_[0,t](s) q0(t-s)A_h(s)exp(i sigma Phi_h(s)-i alpha s).
Its squared L2 norm is at most A_star^2 log(1+t). The transform may be
evaluated at either sign epsilon e; extending the energy integral to the
whole real line only increases the bound. Thus the far region costs
C log(2+t). The remainder R in(H9) has integrable norm and contributes a
bounded HS row. This checks all four choices of epsilon,sigma explicitly.

It follows using(H13) that

    ||L_h X0||_(L2 HS)<=C sqrt(T log(2+T)),
    ||X-X0||_(L2 HS)<=C h sqrt(T log(2+T)).             (H15)

For S_q z=integral_0^T E^(q/2)F_t z(t)dt, the weighted Gram-kernel
version of(H9) gives ||S_q||<=C_q(1+T)^1/4. Each finite-time integral
first exists in the graph norm of E^(q/2), because the fixed slots are in
every such domain and time L2 embeds in time L1. Closedness identifies
the weighted integral as the claimed operator. Exact Dyson integration gives

    E^(q/2)(Z-I-K1_h)=-i lambda S_q c_h M(X-X0),
    ||E^(q/2)(Z-I-K1_h)||_HS
        <=C_q h^2(1+T)^1/4 sqrt(T log(2+T))<=C_q eta_h. (H16)

For the Born operator itself use a fixed smooth spectral cutoff chi(E-m)
supported in [0,b0], equal to one near0, and split F=F_near+F_far.
Weighted near synthesis has norm C_q(1+T)^1/4; weighted far synthesis
has norm C_q by its bounded signed-energy density and temporal Plancherel.
The same is true of unweighted adjoint synthesis. Every Born term with
one far slot is bounded by C_q h(1+T)^1/4.

The remaining near-near momentum kernel has time factors
integral_0^T A_h(t) exp(i(epsilon E(p)-epsilon' E(q))t+i sigma Phi_h(t))dt.
Its phase derivative has modulus at least omega_min-2(m+b0)>0 and variation
at most V_omega. Formula(H8) bounds it uniformly by a fixed constant.
On this output strip E^(q/2) is bounded, so the resulting kernel is bounded
by C_q h||F_near(p)|| ||F_near(q)||, an actual L2(dp dq) majorant.
Its weighted HS and operator norms are O(h). Combining with(H16) proves
both parts of(H6). At no point is an unbounded weight multiplied into an
unweighted small-operator estimate without a graph-norm/synthesis argument.

## 5. Secular spectral measure at the local carrier frequency

In the smooth positive band frame, put u(p)=sqrt(2)e_+(p)*fhat(p),
w(p)=sqrt(2)e_+(p)*ghat(p), Delta(p,q)=u(p)w(q)-w(p)u(q). Then

    r(e)=(1/2)integral |Delta(p,q)|^2
                                 delta(e-E(p)-E(q))dpdq. (H17)

The wavefunction of V|0> is i Delta/sqrt(2). The checked threshold change of
variables gives r(2m+x)=x rho(x), with rho smooth up to zero and rapid
decay of the needed derivatives at infinity. Extend r by zero below2m.
For b=r, b(e)=e r(e), and b(e)=r(e)(exp(ise)-1) with fixed real s,

    C_b(delta)=integral b(e)exp(i e delta)de,
    |C_b(delta)|<=C_b(1+|delta|)^-2.                  (H18)

This retains the possibly nonzero derivative boundary term at2m. A finite
first absolute time moment is not assumed; no stronger false decay import
from a zero-integral slot class is used. Complex b is permitted.

Let I_h,T(e)=integral_0^T A_h(t)cos(Phi_h(t))exp(iet)dt. The new secular
claim, uniform in 0<=tau<=tau_star for the fixed profiles, is

    h^2 integral b(e)|I_h,tau/h^2(e)|^2de
      ->(pi/2)integral_0^tau a(u)^2[b(varpi(u))+b(-varpi(u))]du. (H19)

At finite T, integrability of b and bounded amplitude justify exact Fubini.
Write cos(Phi_h(t))cos(Phi_h(s)) as half the sum of the difference-phase
and sum-phase cosines. For the difference term put delta=t-s and
u=h^2(t+s)/2. The Jacobian is dt ds=h^-2 du ddelta and the admissible
u interval is [h^2|delta|/2,tau-h^2|delta|/2], empty if |delta|>T.
After multiplying by h^2, this term is exactly

    (1/2) integral_R C_b(delta) integral_admissible_u
       a(u+h^2 delta/2)a(u-h^2 delta/2)
       cos(h^-2 integral_(u-h^2 delta/2)^(u+h^2 delta/2) varpi(v)dv)
                                                        du ddelta. (H20)

For each fixed delta and almost every u in (0,tau), BV continuity away
from its countable jump set gives convergence of the product to a(u)^2.
Lebesgue differentiation gives convergence of the phase to delta varpi(u),
including negative delta with the signed integral. Endpoints are negligible.
The inner integrand is bounded by A_star^2, and after integration in u the
majorant A_star^2 tau_star |C_b(delta)| is integrable on the line. Dominated
convergence and Fourier inversion yield the right side of(H19) from(H20),
because integral C_b(delta)cos(varpi delta)ddelta
=pi[b(varpi)+b(-varpi)]. No reality or positivity of C_b was used.

To treat the sum phase fix delta and integrate over the intersection of
s in [0,T] and s+delta in [0,T]. The amplitude A_h(s+delta)A_h(s) has
sup at most A_star^2 and variation at most2 A_star V_a. The phase derivative
varpi(h^2(s+delta))+varpi(h^2 s) is at least2omega_min and has variation
at most2V_omega. Formula(H8) bounds its oscillatory integral by a constant
independent of delta,h,T and phi0. Integrating against |C_b(delta)| gives
O(1) before multiplication by h^2 and O(h^2) afterward. This proves(H19).

For uniformity in tau, if a sequence h_n->0 and tau_n in the compact horizon
violated(H19), extract tau_n->tau0. In(H20) the varying interval indicators
converge almost everywhere to 1_(0,tau0), with the same integrable majorant.
The limiting right side is continuous in tau, by its bounded integrand.
The sum-phase bound is already uniform. This contradicts a bad sequence.
All initial phases disappear from(H20) and only contribute a modulus-one
factor to the uniformly bounded sum phase. Thus the result is uniform in
that phase. A quantitative BV-profile rate is not asserted by this proof.

## 6. The graph law and a separately controlled mean

Write beta=PZP_- and beta1=PK1_h P_-. The same exact exterior normalization
as corrected859 and modulated464 gives

    ||beta1||_HS^2=2h^2 integral r(e)|I_h,T(e)|^2de,
    ||E^(1/2)beta1||_HS^2=h^2 integral e r(e)|I_h,T(e)|^2de. (H21)

The second identity symmetrizes the output energy over the antisymmetric
pair. There is no extra factor2 in the energy identity. Each right side is
uniformly bounded on the kinetic window: use exact time Fubini and
|A_h cos Phi_h|<=A_star, obtaining
integral |b(e)| |I_h,T(e)|^2de<=C T for nonnegative b=r or er from
the integrable correlation bound. More directly, for these nonnegative b,
the exact integral is bounded by A_star^2 T ||C_b||_L1.

The q=1 remainder(H16) therefore gives

    | ||E^(1/2)beta||_HS^2-||E^(1/2)beta1||_HS^2 |
                                                        <=C eta_h. (H22)

Finite-rank and bounded energy cutoffs first identify the exact energy
expectation in(H3); the finite weighted HS norm and monotone convergence
give the full nonnegative form identity. Applying(H19) with b=er, for which
b(-varpi)=0, proves the second assertion of(H7). This is an independent
energy-tail obligation; the characteristic function alone would not give it.

For the full distribution let A0=PZP on PK. Estimate(H6) at q=0 makes
A0 invertible and ||A0^-1-I||<=C eta_h. Choose the scalar conjugation C
on PK used in the corrected parent, set J=Gamma C, and form the skew graph

    L=beta Gamma A0^-1 C, L^T=-L.

The exact transformed annihilator and its CAR relations justify this graph
for Y Omega_vac. Bounds(H6),(H16),(H21) give

    ||L||<=C eta_h, ||L||_HS<=C,
    ||L-beta1 J||_HS<=C eta_h.                        (H23)

The finite-exterior overlap formula and its HS limit, proved in corrected859,
therefore apply with all their hypotheses checked. They give the continuous
trace-log lift

    log chi_h,tau(s)=(1/2)Tr log(I+L*L_s)
                                      -(1/2)Tr log(I+L*L),
    L_s=exp(isE)L exp(isE^T).                          (H24)

The lift is fixed by the norm-convergent operator logarithm series; this is
not a principal scalar-log convention at arbitrary macroscopic time. Terms
of degree at least two in L*L_s have total trace bounded by
C||L||^2||L||_HS^2=O(eta_h^2). Replacing L by beta1 J in the quadratic
term costs O_s(eta_h) by HS Cauchy--Schwarz. The exact pair normalization gives

    log chi_h,tau(s)=h^2 integral r(e)(exp(ise)-1)|I_h,T(e)|^2de
                                                   +O_s(eta_h). (H25)

Use(H19) with b=r(e)(exp(ise)-1). Its limit is exactly
integral(exp(ise)-1)Lambda_tau(de), uniformly in tau. The real part of
this limiting exponent is nonpositive and its modulus is bounded on the
fixed horizon. Exponentiation proves the first assertion of(H7).
This derivation uses the full small operator and HS graph, not the mean
alone or a scalar heuristic about independent creation events.

For each fixed tau the limiting characteristic function is continuous at
zero and is that of CP(Lambda_tau), so the laws converge weakly. Their
nonnegative means converge separately by(H22). The identity
E[(X-R)_+]=E[X]-E[min(X,R)] then gives the needed tail control, and
truncation of Lipschitz tests proves W1 convergence. To make it uniform
in tau, take any sequence tau_h in the compact horizon and extract
tau_h->tau0. Uniform(H7) and continuity of the limiting exponent and mean
give weak and first-moment convergence along that subsequence to
CP(Lambda_tau0), hence W1 convergence to that law.

The comparison laws themselves are W1-continuous: for tau>=sigma,
Lambda_tau-Lambda_sigma is positive, and coupling by an independent compound
Poisson increment bounds

    W1(CP(Lambda_tau),CP(Lambda_sigma))
       <=integral e (Lambda_tau-Lambda_sigma)(de)<=C|tau-sigma|. (H26)

This is a coupling of auxiliary comparison laws. It imposes no independent
increments on the quantum dynamics. The triangle inequality contradicts
any bad sequence and proves the uniform W1 assertion without a rate.

## 7. Correlations and global-state topology

The fixed-CAR and finite-mode argument of exact correlation335,
SHA 40bebe4fa79afe383d50aae1941598f10007e79594464cfc7969c6cfd658dc19,
uses the operator bound and CAR rather than a constant carrier. Thus with
d_h=C eta_h, a fixed real word of degree n has vacuum-reference difference
at most n d_h product_j ||k_j||. Common free rotation handles the full state.
The exact number covariance satisfies 0<=N<=d_h^2 I, so for any rank-r
positive-band projection Q the restricted state obeys

    ||rho_Q-P_vac,Q||_1<=2 min(1,sqrt(r)d_h).           (H27)

A detection probability at least p0 requires r>=p0/d_h^2. This is a
necessary lower resource estimate, not an optimal construction or sufficient
detector rank. Infinite-rank energy bands and spatial regions are not
automatically covered by a finite-mode trace-norm statement.

The free gap m separates the global vacuum from all nonzero H0 energy.
Since Lambda_tau is supported above2m, weak energy convergence and a
continuous cutoff inside that gap give vacuum weight tending to
exp(-Lambda_tau(R)). The states are pure, and therefore their global trace
distance to vacuum tends to

    2 sqrt(1-exp(-Lambda_tau(R))).                    (H28)

For compact Fock K, the limit is

    Tr(rho_h,tau K)->exp(-Lambda_tau(R))<Omega_vac,K Omega_vac>. (H29)

For completeness, the small one-particle off-diagonal norm makes
||a(k)Y Omega_vac||<=d_h||k||. Testing against finite creation vectors
then makes every fixed nonvacuum matrix amplitude vanish. These vectors
are dense in the orthogonal complement of the vacuum. Vacuum magnitude
is fixed by the energy-gap argument; finite-rank approximation of K gives
(H29), with no global normalization of the limiting compact functional.
The same conclusion for the full state follows either by the corresponding
freely rotated annihilation estimate or by repeating the finite-vector
argument there. The annihilation estimate is uniform in the rotated k.
These topologies coexist with finite energy response and do not yield a
spatial-algebra norm limit or any multi-time process.

## 8. Explicit conditional transfer to calibrated cells

Let ell denote the actual mesh parameter, distinct from the amplitude
profile a. Retain the supplied real energy embedding, common exact H0 and
vacuum, and centered image control V_ell and one-particle generator B_ell.
Assume, at fixed order N and fixed resources,

    ||V_ell-V||<=d0 epsilon_ell,
    ||[H0,V_ell-V]||<=d1 epsilon_ell,
    ||[H0,V]||,||[H0,V_ell]||<=k1,
    ||B_ell-B||<=d_B epsilon_ell,
    epsilon_ell=O(ell^(N+1)).                          (H30)

These are actual hypotheses, including the real/Fock/domain identifications;
no new actual-cell calibration or embedding construction is proved here.
The scalar work budget satisfies

    B_h(T)=integral_0^T |lambda c_h(t)|dt<=A_star tau_star/h.

The bounded-perturbation and first-energy work identities of the corrected
parent require this budget, not periodicity or a derivative of c_h. They give

    ||rho_ell^E-rho||_1<=2d0 epsilon_ell B_h(T),
    |E_ell-E|<=epsilon_ell[d1 B_h(T)+k1 d0 B_h(T)^2].   (H31)

The second estimate subtracts the two work identities, uses the first
state bound inside the commutator expectation and integrates
B_h'(t)B_h(t) to B_h(T)^2/2. Bounded energy resolvents justify the work
identity on finite-first-energy states before taking their cutoff limit.
Neither amplitude nor frequency jumps insert an instantaneous H0-energy
kick: the interaction Hamiltonian is locally integrable and its propagator
continuous. No derivative-of-drive term belongs in the H0 work identity.

Thus epsilon_ell=o(h^2) suffices for transfer of the law, mean and uniform
W1 conclusion. The weaker epsilon_ell=o(h) supplies only the unweighted
state/law comparison. One-particle Duhamel adds C epsilon_ell/h to the
unweighted d_h for CAR and finite-mode bounds. No stronger weighted
operator estimate for the actual cell is inferred from(H30) alone.

## 9. Checks, failed shortcuts and exposure

If a=0 almost everywhere, the exact drive is zero and Lambda_tau=0.
For constant varpi=omega>2m, (H4) reduces to an atom at omega of mass
(pi/2)r(omega) integral_0^tau a(u)^2du. This exactly recovers the accepted
amplitude theorem, including its exterior1/2 normalization. The amplitude
may change sign: only its square enters the limiting measure, although
finite-h coherent evolution still depends on the signed profile.

For finitely many slow-time blocks I_j with constant amplitudes a_j and
frequencies omega_j>2m, (H4) is the finite sum of atoms with masses
(pi/2)a_j^2 r(omega_j)|I_j intersect[0,tau]|. The marginal comparison law
can be represented as sum_j omega_j N_j with independent Poisson N_j of
those parameters; coincident frequencies may be combined. This is an
auxiliary marginal representation, not an observed counting process.
At the end of a schedule, reordering blocks with the same weights leaves
that limiting measure unchanged. No finite-h order-independence is claimed.
Frequency jumps are allowed, but the phase(H2) is integrated continuously;
independently resetting the phase at an arbitrary growing number of jumps
would be a different drive class and is not silently included.

No positive pair rate is assumed for every nonzero slot or amplitude. The
zero-rate/degenerate cases simply give zero measure in(H4). The strict
frequency gap is used twice, in the causal square and near-near Born kernel,
and again to separate the full-input threshold. Failure of these estimates
at a crossing is not a theorem that threshold-crossing protocols cannot
have limits. That route is outside this proof and remains available.

The constant-frequency forcing denominator cannot merely be replaced by
an instantaneous one. The threshold-strip/Plancherel argument(H14)--(H15)
replaces it. A naive finite first correlation-time moment also fails for
general slots; the secular proof instead uses integrable C_b and dominated
convergence. Consequently no unjustified quantitative BV-frequency error
rate is advertised. The mean requires(H21)--(H22), in addition to the
trace-log calculation; weak convergence by itself is insufficient.

The root48-line plan was sealed at2026-10-13T11:47:42.610380Z, SHA
ed9943398e71ca3b1b45b94d4a788be8b98dc57f196bfea57ce5d2bb4228675d.
Root had read and accepted the exact parent proofs and source-exposed
reviews before this extension. During drafting root received a separately
frozen initial-state derivation's summary, but none of its conclusions is
used here. New independent chirp findings have not been opened before this
root proof's freeze. No numerical scientific computation or Lean build was
run for this derivation. Symbolic special cases are author checks, not
independent validation. The new phase lemma, full-input forcing, secular
limit, graph hypotheses and actual-cell quantifiers need focused review.
The defective original847 picture identity and earlier root miss remain
preserved history; they are not rehabilitated by this new construction.

## Unchanged independent core: resource-uniform strengthening

The following separately frozen 850-line proof is reproduced in full, with
its original notation and historical author-status sentences. Its stronger
uniform rate and profile-W1 conclusions have the separate root assessment
described above. The assembler is this core's author, so the assembly and
comparison add no additional independent author check of this core.


# One-time kinetic energy law for a slowly chirped BV drive

Status: conditional-support; complete author derivation in the supplied free
model, awaiting a separate ordinary analytic check. No retained or formal
status, physical model selection, Markov assumption or multi-time process
claim is supplied. The selected model and reasoning effort are unchanged.

    target_claim_type: bounded_theorem
    actual_current_surface_status: conditional-support
    trace_class: upstream_support
    reachability_to_target: supports
    hypothetical_axiom_status: null
    admitted_observation_status: null
    audit_required_before_effective_retained: true
    bare_retained_allowed: false

## 1. Exact premises, conventions and statement

Use K=L2(R,dp;C^2), second-slot-linear inner product, the unitary spatial
Fourier transform, and the supplied real structure and massive generator

    D(p)=-vp sigma_x-m sigma_y, E(p)=sqrt(m^2+v^2p^2),
    P=(I+D/E)/2, P_-=I-P, Gamma k(p)=overline(k(-p)),
    m,v>0, h_+=P K, H0=dGamma(E|h_+), vacuum |0>.       (1)

All model data and the two real spatial slots f,g in C_c^infinity(R;R^2)
are fixed. No zero-integral condition is imposed. Put

    gamma(f)=a*(sqrt(2)Pf)+a(sqrt(2)Pf),
    V=(i/2)[gamma(f),gamma(g)]
                       -<0|(i/2)[gamma(f),gamma(g)]|0>I,
    F(z1,z2)=z1 f+z2 g, M=2i[[0,1],[-1,0]], B=F M F*.

The fields are bounded, V is bounded selfadjoint and even, and B is a
selfadjoint rank-at-most-two one-particle perturbation. Scalar centering
changes a Fock phase only. For a scalar positive-band description choose

    theta(p)=arctan(vp/m),
    e_+(p)=(exp(i theta(p)/2),-i exp(-i theta(p)/2))/sqrt(2),
    u(p)=sqrt(2)e_+(p)*fhat(p), w(p)=sqrt(2)e_+(p)*ghat(p),
    Delta(p,q)=u(p)w(q)-w(p)u(q),
    r(e)=(1/2) integral |Delta(p,q)|^2
                           delta(e-E(p)-E(q)) dp dq.    (2)

The last expression denotes the ordinary pushforward density. It is
nonnegative, vanishes below 2m, and is continuous. Its exact threshold and
regularity properties used below are established in section 2. There is
one scalar positive band and no extra spin multiplicity.

Fix 0<=tau_star<infinity, real a,Omega in BV([0,tau_star]), and finite bounds

    ||a||_infinity<=A, Var(a)<=V_a,
    2m+kappa<=Omega(u)<=W a.e., Var(Omega)<=V_Omega,
    kappa>0, W<infinity.                               (3)

One-sided BV representatives and their endpoint traces are understood.
Changing isolated values has no effect on the integrals or propagators.
Every fixed BV path with ess inf Omega>2m admits such constants. They and
the supplied model/slots are kept fixed as h tends to zero.

For real lambda!=0, h=|lambda|, arbitrary real phi0 and 0<=tau<=tau_star,
set T=tau/h^2 and

    phi_h(t)=phi0+h^-2 integral_0^(h^2 t) Omega(x)dx,
    c_h(t)=a(h^2 t)cos(phi_h(t)),
    H_h(t)=H0+lambda c_h(t)V.                          (4)

Let W_h be the full Fock propagator, Y_h(t)=exp(itH0)W_h(t) its interaction
propagator, S_h the full one-particle propagator of D+lambda c_h(t)B,
and Z_h(t)=exp(itD)S_h(t). Bounded interaction generators give these
unitaries at every finite T. Define mu_h,tau as the spectral probability
law of H0 in Y_h(T)|0>. It is also the law in W_h(T)|0>.

The resulting limiting measure is specified by a finite positive jump measure

    Lambda_tau(A0)=(pi/2) integral_0^tau
       a(x)^2 r(Omega(x)) 1_A0(Omega(x)) dx.            (5)

Here A0 is a Borel set in R; it is not the amplitude resource A. The measure
is supported in [2m+kappa,W]. Write

    ell_tau=Lambda_tau(R),
    m_tau=integral e Lambda_tau(de)
          =(pi/2) integral_0^tau a(x)^2 Omega(x)r(Omega(x))dx.

Let Pi_tau be the compound-Poisson probability measure determined by

    chi_Pi_tau(s)=exp[integral (exp(ise)-1)Lambda_tau(de)]. (6)

If ell_tau=0, Pi_tau=delta_0. Otherwise it is the law of a sum of N iid
jump energies with distribution Lambda_tau/ell_tau, where N is Poisson
with parameter ell_tau. This probabilistic representation identifies a
single-time law; it is not an assertion about the driven system at several
times. Formula (5) is derived below, not assumed as a local emission rule.

**Theorem.** With eta_h=sqrt(h log(2+h^-2)), for sufficiently small h,

    sup_(0<=tau<=tau_star)
       |chi_mu_h,tau(s)-chi_Pi_tau(s)| <= C_s eta_h,
    sup_(0<=tau<=tau_star)
       |integral e mu_h,tau(de)-m_tau| <= C eta_h,       (7)
    sup_(0<=tau<=tau_star) W1(mu_h,tau,Pi_tau) ->0.      (8)

The characteristic estimate is for each fixed real s. The constants depend
only on fixed model/slot data and the resources in (3), tau_star and, where
indicated, s. They are independent of phi0, the sign of lambda and the
positions of BV jumps. No W1 rate is asserted. The proof also gives uniform
comparison with the path-dependent family (5) over resource-bounded paths;
for h-dependent paths this is an approximation statement, not convergence
to a single fixed Pi. Convergence of the corresponding jump measures is
a sufficient additional condition for a single limiting law.

There is no single jump energy in general. For constant Omega=omega,
J_tau=integral_0^tau a(x)^2dx and ell_tau=(pi/2)r(omega)J_tau; then Pi_tau
is Law(omega Poisson(ell_tau)). J_tau is the amplitude-square integral,
while ell_tau is the Poisson intensity. A genuine varying-frequency path
instead gives the measure (5). No strict positivity for arbitrary slots
or paths is asserted.

## 2. Inherited source facts and their actual hypotheses

Only the following exact, previously completely read scientific sources are
used. Their conditional physical model and actual-cell assumptions remain
exposed. References inside them are not automatically additional premises.

| Source | Lines | SHA-256 |
|---|---:|---|
| MODULATED_KINETIC_LAW_ROOT_PROBE.md | 464 | 422a92a8a24daa8fa240251ccae041fcca737af0335a486f33f3b20de0fb665a |
| GENERAL_KINETIC_LAW_ROOT_PROBE.md | 470 | 6bbcf624e47e4d91f2a6fbd8982698d788923bba63612f90d5930d04920ca49b |
| WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT_V2.md | 859 | c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b |
| KINETIC_CORRELATION_ROOT_PROBE.md | 335 | 40bebe4fa79afe383d50aae1941598f10007e79594464cfc7969c6cfd658dc19 |

First, CAR and the corrected picture conventions give, for bounded measurable
real c_h,

    Y_h(t)* gamma(k)Y_h(t)=gamma(Z_h(t)*k),
    i Z_h'(t)=lambda c_h(t)F_t M F_t* Z_h(t),
    F_t=exp(itD)F,
    N_h=P Z_h P_- Z_h*P,
    <H0>_h=||E^(1/2)P Z_h P_-||_HS^2.                 (9)

The full identity is W_h*gamma(k)W_h=gamma(S_h*k), not the interaction
identity with S substituted for Z. The coefficient of a full Heisenberg
field solves the right equation R'=R i(D+lambda c_h B), so R=S_h*.
Passing to Y gives Z_h*=S_h*exp(-itD), fixing order and sign. The occupation
identity follows by expressing creation/annihilation through real fields.
Finite-rank sums and increasing bounded energy cutoffs give the last identity
as an extended positive form. Section 5 proves its finiteness. No unbounded
trace is cyclically permuted. Real conjugation exchanges P and P_- and makes
the propagators preserve the real fields.

Second, let q(t)=(1+t)^(-1/2), t>=0. The two-channel kernel has the controlled
stationary-phase decomposition

    G(t)=F*exp(-itD)F
        =q(t) sum_(alpha=+-m) exp(i alpha t) C_alpha+R(t),
    ||R(t)||<=C(1+t)^(-3/2).                          (10)

The same decay bound O((1+|t|)^(-1/2)) holds for every Gram kernel with a
fixed nonnegative energy power and a fixed smooth spectral cutoff. To recall the
hypotheses, the odd smooth coordinate p=y sqrt(2m+y^2)/v gives E=m+y^2.
Each band amplitude including its Jacobian is Schwartz. For t>=1 the
Gaussian Fourier integral and |exp(ix)-1|<=|x| give a leading t^-1/2 term
and an O(t^-3/2) remainder controlled by an integrable second Fourier moment.
Replacing t^-1/2 by q(t) changes only that remainder. Fixed energy powers
and smooth band factors preserve the Schwartz property. Thus (10) applies
to general compact smooth slots, including nonzero component integrals.

Third, the pair vector V|0> has wavefunction i Delta/sqrt(2). The same odd
coordinate in both momenta, followed by polar integration, expresses r(2m+x)
as one quarter of the angular integral of a smooth Schwartz amplitude at
radius sqrt(x). Its angular average is smooth in x>=0. Antisymmetry gives
Delta(0,0)=0 and hence

    r(2m+x)=x rho(x), x>=0,                            (11)

with rho smooth one-sided and all the required derivatives rapidly decreasing
at infinity. Smoothness in x follows either from angular Taylor expansion
with odd powers cancelling or from repeated smooth even radial differentiation.
The Jacobian is polynomially bounded and nonzero at zero. The coefficient
rho(0) need not vanish or be positive. Extension by zero need not be C1.

Consequently for each of

    b(e)=r(e), e r(e), or r(e)(exp(ise)-1), fixed s,
    C_b(t)=integral b(e)exp(iet)de,

we have

    |C_b(t)|<=K_b/(1+t^2), C_b in L1(R).               (12)

Indeed b(2m)=0, b'(2m+) is finite and b'' on (2m,infinity) is integrable.
Two integrations by parts retain the boundary derivative and give
C_b(t)=[b'(2m+)exp(i2mt)+integral_2m^infinity b''(e)exp(iet)de]/(it)^2
for t!=0. The small-time bound uses ||b||_1. A first absolute time moment
is not assumed; it can diverge logarithmically. This positive Fourier-phase
convention is the one used in the double-time integral below.

The small-pair graph and overlap formula from corrected859 require an
invertible PZP, an antisymmetric Hilbert--Schmidt graph coordinate, and its
small operator norm. They do not intrinsically require zero-integral slots.
Sections 3--6 establish those hypotheses for this new drive before using
the formula. The zero-integral estimates from859 are not substituted for
the unrestricted-slot estimates proved here.

## 3. BV nonstationary integration and the exact causal square

We first record the elementary integration fact used at every jump. Let
psi be absolutely continuous on [l,r], with a fixed-sign BV representative
d=psi' a.e. satisfying |d|>=delta>0. For a complex BV amplitude v,

    |integral_l^r v(t)exp(i psi(t))dt|
      <= [2||v||_infinity+Var(v)]/delta
                         +||v||_infinity Var(d)/delta^2. (13)

To prove it, use d(exp(i psi))=i d(t)exp(i psi)dt, so the Lebesgue integral
equals the Stieltjes integral of v/(i d) against exp(i psi). Integration
by parts gives its two endpoint traces and the measure derivative of v/d.
The reciprocal is BV with variation at most Var(d)/delta^2 when d has a
fixed sign. All applications here have that property. The BV product bound
then proves (13). Phase continuity and the Stieltjes measure retain every
frequency or amplitude jump. No derivative of a or Omega as a function
is assumed.

Set X(t)=F_t*Z_h(t), X0(t)=F_t*. Both are full-input Hilbert--Schmidt row
operators K->C^2, with ||X(t)||_HS=||F||_HS. Dyson gives exactly

    X=X0+lambda L_h,T X,
    (L_h,T x)(t)=-i integral_0^t G(t-s)c_h(s)M x(s)ds.  (14)

The time operator acts on L2([0,T];C^2), and on its Hilbert--Schmidt
amplification with the same estimates. From (10) and Young's inequality,
||L_h,T||<=C sqrt(1+T). It is not a convolution operator in this problem.

Changing order on the finite causal triangle in L_h,T^2, putting r=t-s,
and expanding only the inner cosine gives

    (L_h,T^2 x)(t)=-(1/2) sum_(sigma=+-1) integral_0^t
          H_sigma,h(s,t-s)c_h(s)M x(s)ds,
    H_sigma,h(s,r)=integral_0^r G(r-z)a(h^2(s+z))
                  exp(i sigma phi_h(s+z))M G(z)dz.     (15)

Every matrix order is retained; the final factor is c_h(s)M. Fubini is
legitimate on a finite triangle with bounded kernels and L2 time inputs.
For a product of two leading terms in (10), its scalar phase derivative
with respect to z is

    beta-alpha+sigma Omega(h^2(s+z)), alpha,beta in {+-m}.

It has sign sigma, absolute value at least kappa and variation at most
V_Omega. The scalar amplitude is
v(z)=q(r-z)q(z)a(h^2(s+z)). Since q(r-z)q(z) has supremum q(r), decreases
then increases and has total variation at most 2q(r),

    ||v||_infinity<=A q(r),
    Var(v)<=q(r)(2A+V_a).

Equation (13) bounds the leading integral by

    q(r)[(4A+V_a)/kappa+A V_Omega/kappa^2].

Terms with at least one R are bounded absolutely. Splitting the convolution
at r/2 gives q*(1+t)^(-3/2)<=C q; the double remainder is no larger at this
order. Therefore, uniformly in the allowed s,r,h,

    ||H_sigma,h(s,r)||<=C q(r),
    ||L_h,T^2||<=C sqrt(1+T).                          (16)

The second is the norm of the operator square, not the square of the first
norm. A scalar causal majorant and Young's inequality suffice even though
H depends separately on s and r. The same proof covers HS amplification.

For T<=tau_star/h^2 and small h,

    (I-lambda L_h,T)^(-1)
       =(I+lambda L_h,T)(I-lambda^2 L_h,T^2)^(-1),
    ||(I-lambda L_h,T)^(-1)||
       <=[1+C h sqrt(1+T)]/[1-C h^2 sqrt(1+T)]<=C.     (17)

The denominator is at least 1/2 for sufficiently small h. All factors are
polynomials or norm-convergent series in the same bounded operator, so this
is both a left and right inverse, without normality or commutativity of the
channel matrices. The numerator stays bounded because h sqrt(1+T) is
bounded, while h^2 sqrt(1+T)=O(h). No expansion small in hT is used.

## 4. Full-input forcing by a different energy-space estimate

For chirped forcing it is inappropriate to use a single fixed resonant-root
primitive. The following energy-space split proves the needed uniform bound
without assuming monotonicity of Omega or tracking its moving resonances.

The R part of L_h,T X0 is uniformly bounded in HS norm at each time by its
L1 time norm. For a leading term and input band epsilon=+-1, the row kernel,
up to fixed matrices and the factor 1/2, is

    exp(-i epsilon E(p)t) K_alpha,epsilon,sigma(t,E(p))
                                      C_alpha M Fhat(p)*P_epsilon(p),
    K_alpha,epsilon,sigma(t,e)=integral_0^t q(z)a(h^2(t-z))
          exp(i(alpha+epsilon e)z+i sigma phi_h(t-z))dz. (18)

The harmless ordering of the scalar exponential does not move C_alpha or M.
The nonnegative input-energy majorant is

    w_epsilon(e)=sum_(p=+-sqrt(e^2-m^2)/v)
                     ||Fhat(p)*P_epsilon(p)||_HS^2/|E'(p)|.

It is integrable on [m,infinity), bounded away from m, rapidly decreasing
at infinity, and O((e-m)^(-1/2)) near m. These statements follow directly
from the two energy branches and the fixed Schwartz slot amplitudes.

For m<=e<=m+kappa/2, the phase derivative in (18) is

    alpha+epsilon e-sigma Omega(h^2(t-z)).

Since |alpha+epsilon e|<=2m+kappa/2, its magnitude is at least kappa/2,
its sign is -sigma, and its variation is at most V_Omega. The amplitude
q(z)a(h^2(t-z)) has supremum at most A and variation at most A+V_a.
Equation (13) gives |K|<=C uniformly in this entire threshold region.
Its squared integral against w_epsilon is therefore uniformly bounded.

For e>=m+kappa/2, w_epsilon is bounded. Extend the scalar time amplitude
q(z)a(h^2(t-z))exp(i alpha z+i sigma phi_h(t-z)) by zero outside [0,t].
Temporal Plancherel, integrating the full real energy line, gives

    integral_R |K_alpha,epsilon,sigma(t,e)|^2de
        =2pi integral_0^t q(z)^2 |a(h^2(t-z))|^2dz
        <=2pi A^2 log(1+t).                           (19)

This bound includes all interior stationary energies, multiple crossings
and plateaus. The sign epsilon changes only the Fourier orientation.
Combining the finitely many bands/phases/matrices and the remainder gives

    ||(L_h,T X0)(t)||_HS<=C sqrt(log(2+t)),
    ||L_h,T X0||_(L2 HS)<=C sqrt(T log(2+T)),
    ||X-X0||_(L2 HS)<=C h sqrt(T log(2+T)).             (20)

The last step uses the genuine inverse (17). It is a full-input estimate,
not an estimate on a scalar mean or only on the negative input band.

## 5. Weighted full remainder and small one-particle norm

For each fixed q0>=0 define S_q0,T z=integral_0^T E^(q0/2)F_t z(t)dt.
The weighted version of (10), Schur's test and HS amplification give

    ||S_q0,T||<=C_q0(1+T)^(1/4).                      (21)

At finite T these integrals exist in the corresponding fixed-slot energy
graph norm. The slots are in every fixed graph domain, E commutes with the
free evolution, and finite-interval L2 functions are L1. Closedness of the
energy multiplier identifies the graph integral with the weighted vector.
The same argument on an input basis and summation gives the HS statement.

Let Z1(T)=-i lambda integral_0^T c_h(t)F_t M F_t*dt be the full first Born
operator, and beta=PZ_h(T)P_-, beta1=PZ1(T)P_-. From (20)--(21),

    ||E^(q0/2)(Z_h(T)-I-Z1(T))||_HS
       <=C_q0 h^2(1+T)^(1/4)sqrt(T log(2+T))
       <=C_q0 eta_h, 0<=T<=tau_star/h^2.              (22)

Thus the weighted block in (9) is finite at finite time. The graph-domain
conclusion precedes any kinetic limiting argument.

We separately need an operator bound on the entire Z_h-I. Choose a smooth
near-threshold cutoff chi(E), supported in E<=m+kappa/4 and equal to one
on a smaller threshold interval. Write F=F_near+F_far using chi and 1-chi.
The far synthesis and analysis maps have norms bounded independently of T:
their energy-density matrices are bounded, so temporal Plancherel applies.
The near maps have norm O((1+T)^(1/4)). This also has a direct energy proof:
the near density is O(x^-1/2), x=e-m; split at x=1/T, use the pointwise
Fourier bound T||z||_2^2 below that value and Plancherel above it.

Every Born term with a far factor is -i lambda S_j c_h M S_k* and has norm
at most C h(1+T)^(1/4). For a near-near term, expand both band projections
and the cosine. Its scalar phase derivative is

    epsilon E(p)-epsilon' E(q)+sigma Omega(h^2 t).

On these supports it has sign sigma, magnitude at least kappa/2 and
variation at most V_Omega. Equation (13), with amplitude a(h^2 t), bounds
the time integral uniformly by a fixed resource constant. The resulting
kernel is bounded by C h ||F_near(p)|| ||F_near(q)||. This is a square-
integrable product majorant, so its HS norm, and hence operator norm, is
O(h). Consequently

    ||Z1(T)||<=C h(1+T)^(1/4),
    ||Z_h(T)-I||<=C eta_h.                            (23)

Neither estimate treats the identity on the infinite input space as HS.
The phase derivative bound covers same-band as well as opposite-band terms.
The cutoff only decomposes an exact operator; it does not alter the model,
slots or original drive.

Finally, with

    I_h,T(e)=integral_0^T c_h(t)exp(iet)dt,

the exact Born pair identities are

    ||beta1||_HS^2=2 h^2 integral r(e)|I_h,T(e)|^2de,
    ||E^(1/2)beta1||_HS^2
                         =h^2 integral e r(e)|I_h,T(e)|^2de. (24)

Indeed beta1 J has kernel lambda Delta(p,q)I_h,T(E(p)+E(q)), where
J=Gamma C in the scalar positive frame. The unweighted exterior factor
1/2 in (2) gives the factor two in the first formula. Symmetrizing the
output energy E(p) against E(q) cancels that two in the second. Both
norms are uniformly bounded on the kinetic window: for bounded b,

    h^2 integral |b(e)| |I_h,T(e)|^2de
       <=2pi ||b||_infinity h^2 integral_0^T |c_h(t)|^2dt
       <=2pi ||b||_infinity A^2 tau_star.              (25)

## 6. A chirped secular lemma with a uniform error

For any of the real or complex b in (12), the new secular assertion is

    h^2 integral b(e)|I_h,tau/h^2(e)|^2de
       =(pi/2) integral_0^tau a(x)^2
                   [b(Omega(x))+b(-Omega(x))]dx+O_b(h), (26)

uniformly for 0<=tau<=tau_star and the resources (3). For the present
positive-energy densities b(-Omega)=0. We prove the two signs and coefficient
before imposing that support condition.

Extend Omega to R by its endpoint traces; it remains BV with variation at
most V_Omega, the same positive lower bound and the same upper bound. Let
A_tau(x) equal a(x) on [0,tau] and zero elsewhere. As an a.e. BV function,

    ||A_tau||_infinity<=A,
    Var(A_tau)<=V_a+2A,
    ||A_tau(.+z)-A_tau||_1
                  <=min(2A tau_star, (V_a+2A)|z|).    (27)

For any BV function f whose distributional derivative is a finite measure,
the translation bound ||f(.+z)-f||_1<=|z|Var(f) follows by writing the
difference as the measure of a translated interval and applying Fubini to
its total variation. This also applies to the extended Omega, even though
that function need not itself be integrable on R.

Expanding the double-time integral using
cos(phi(t))cos(phi(s))=[cos(phi(t)-phi(s))+cos(phi(t)+phi(s))]/2 gives
a difference-phase part D_h,b and a sum-phase part S_h,b. With u=t-s and
x=h^2 s, the difference part is exactly

    D_h,b=(1/2) integral_R C_b(u) integral_R
       A_tau(x+h^2 u)A_tau(x)cos(Theta_h(x,u)) dx du,
    Theta_h(x,u)=integral_0^u Omega(x+h^2 z)dz.         (28)

The extensions only fill places where the amplitude product is zero;
they do not change the original dynamics. All interchanges are legitimate
by finite-time Fubini followed by C_b in L1 and the finite slow-time support.

Replace the product in (28) by A_tau(x)^2, keeping its phase. Equation (27)
bounds the integrated amplitude error by C min(1,h^2|u|). With (12), its
u integral is at most C_b h^2 log(2+h^-2). Next compare the phase to its
local linear value u Omega(x). The BV translation inequality gives

    integral_R |Theta_h(x,u)-u Omega(x)|dx
                      <=(h^2 V_Omega/2)|u|^2.          (29)

The same formula holds for negative u by reversing the integral. Since
|cos x-cos y|<=min(2,|x-y|), the A_tau^2-weighted phase error has integral
at most

    min(2A^2 tau_star, A^2 h^2 V_Omega u^2/2).

Integrate this against K_b/(1+u^2), splitting at |u|=h^-1. The inner
integral is O(h^2 h^-1) and the outer tail is O(h), proving an O_b(h)
error, uniform in tau. This is the step that permits jumps and arbitrary
nonmonotone BV frequency paths. It uses an integrated translation bound,
not a uniform pointwise Taylor expansion of Omega.

Fourier inversion, valid because b and C_b are integrable and b is continuous,
now gives

    integral_R C_b(u)cos(u Omega(x))du
                    =pi[b(Omega(x))+b(-Omega(x))].

Thus D_h,b equals the right side of (26), up to O_b(h).

For the sum-phase part, keep u fixed and integrate over
max(0,-u)<=s<=min(T,T-u). Its inner amplitude a(h^2(s+u))a(h^2 s) has
supremum at most A^2 and variation at most 2A V_a. Its phase
phi_h(s+u)+phi_h(s) has a.e. derivative

    Omega(h^2(s+u))+Omega(h^2 s)>=2(2m+kappa),

with variation at most 2V_Omega. Equation (13) bounds this entire inner
oscillatory integral by a constant independent of u,T,h and phi0. Therefore

    |S_h,b|<=C h^2 ||C_b||_1.                         (30)

The initial phase cancels from the difference term and affects only this
uniformly negligible sum term. Equations (28)--(30) prove (26). In the
special case Var(Omega)=0 the phase-localization error is exactly zero;
the same proof gives O_b(h^2 log(2+h^-2)). A finite first absolute moment
of C_b was nowhere smuggled into the argument.

## 7. Exact state, graph coordinate and characteristic function

On h_+, let A0=PZ_h P and beta=PZ_h P_-. Equation (23) makes A0 invertible
for all small h, uniformly on the kinetic window. Equations (22), (24)
and (25) give ||beta||_HS<=C, ||beta-beta1||_HS<=C eta_h. In the scalar
positive frame let C denote ordinary complex conjugation and J=Gamma C.
The actual pair coordinate is

    L=beta Gamma A0^-1 C,
    ||L||<=C eta_h, ||L||_HS<=C,
    ||L-beta1 J||_HS<=C eta_h, L^T=-L.                (31)

The transformed annihilator of Y_h|0> is
a(A0 xi)+a*(beta Gamma xi). Changing variables to b=A0 xi gives
a(b)+a*(L Cb); the vanishing CAR anticommutator forces the skew transpose.
The order Gamma A0^-1 C is material. The norm estimates follow from
||A0^-1-I||<=||A0-I||/(1-||A0-I||) and the already proved full-input
and operator estimates, not from the energy mean.

For clarity, the exact Gaussian identity being used has an ordinary
finite-to-infinite-dimensional proof. For finite skew matrices L,M, the
pair exponential F_L=exp[(1/2)sum L_ij a_i* a_j*]|0> has even-subset
coefficients Pf(L_S). Its overlap satisfies

    <F_L,F_M>^2=det(I+L*M), <F_0,F_0>=1.

Expansion of the block Pfaffian [[L*,-I],[I,M]] in its identity pairings
gives the even-subset overlap and the displayed determinant after squaring.
In the region ||L||||M||<1, continuity from zero and the nonvanishing
determinant fix the overlap as exp[(1/2)Tr log(I+L*M)], with its convergent
trace-log series. The annihilation equation is
a(b)F_L=-a*(L Cb)F_L, fixing the sign of this coordinate.

For HS skew L, take finite-rank projections commuting with C and converging
strongly to I. Their compressed skew matrices converge in HS norm and have
a common operator bound less than one. Products of two compressions converge
in trace norm. On that operator-norm ball, the trace-log series is trace-
norm continuous, since telescoping its powers bounds the difference by
||X-Y||_1/(1-delta^2) when both operator norms are at most delta^2<1.
The mixed-overlap formula therefore makes the unnormalized pair vectors
Cauchy, with vacuum component one and finite nonzero norm. Bounded CAR
operators pass the annihilation equations to the limit. Conjugating by
the already existing Y_h gives uniqueness of the ordinary Fock vacuum;
the normalized limit is Y_h|0> up to phase. This is a proof of a state
identity, not a finite-dimensional approximation of the dynamics.

With R_s=exp(isE|h_+) and L_s=R_s L R_s^T, second quantization rotates
the pair exponential accordingly. Finite exterior sectors prove this first,
and Fock norm continuity gives the HS limit even when the finite-rank
projections do not commute with E. Consequently

    log chi_mu_h,tau(s)
       =(1/2)Tr log(I+L*L_s)-(1/2)Tr log(I+L*L).       (32)

This is a continuous trace-log lift, not necessarily the principal scalar
logarithm for all kinetic times. Its real part is log|chi|. Since
||L*L_s||<=||L||^2 and ||L*L_s||_1<=||L||_HS^2, the terms beyond the
linear trace in (32) are O(eta_h^2). Replacing L by beta1 J in the linear
term costs O(eta_h), using the bounded HS norms in (31). The exact kernel
in (24), including its exterior factor 1/2, then yields

    log chi_mu_h,tau(s)
       =h^2 integral r(e)(exp(ise)-1)|I_h,T(e)|^2de
                                            +O_s(eta_h). (33)

Applying (26) with b(e)=r(e)(exp(ise)-1) gives precisely
integral(exp(ise)-1)Lambda_tau(de). Since h=O(eta_h), the error remains
O_s(eta_h). Both exact and limiting exponents have nonpositive real part;
integration along the joining segment bounds the difference of their
exponentials by the difference of the exponents. This proves the first
part of (7), with no branch-winding ambiguity.

## 8. Separate mean and the uniform W1 conclusion

The q0=1 case of (22), the bounded weighted Born norm in (25), and the
difference-of-squares inequality give

    |<H0>_h-h^2 integral e r(e)|I_h,T(e)|^2de|
                                                    <=C eta_h.

Equation (26) with b(e)=e r(e) identifies the remaining expression with
m_tau+O(h). This proves the second part of (7), independently of the
characteristic-function limit. No derivative of a characteristic-function
limit or exchange with an unbounded energy observable is used.

For fixed tau, (6) is a continuous characteristic function at zero, so
characteristic convergence gives weak convergence to Pi_tau. Both laws
are nonnegative and their means converge. The missing tail step is explicit:
for every R>0 and any such convergent sequence X_n,

    E[(X_n-R)_+]=E[X_n]-E[min(X_n,R)]
                         ->E[X]-E[min(X,R)].          (34)

The right side tends to zero as R grows. Since
x 1_(x>2R)<=2(x-R)_+, the sequence's first moments are uniformly integrable
after treating its finite initial segment. Truncating Lipschitz test functions
then proves W1 convergence. An uncontrolled rare tail cannot carry a missing
finite mean through this argument.

Uniformity in tau follows by contradiction. A failing sequence has a
subsequence tau_n->tau. The jump measures (5) differ in total variation by
at most C|tau_n-tau| and in their first-energy mass by the same order.
Couple a compound-Poisson law on the common measure and independent extra
jumps on the remaining interval; this gives W1(Pi_tau_n,Pi_tau)<=C|tau_n-tau|.
The uniform characteristic and mean estimates then imply weak and W1
convergence of mu_h_n,tau_n to Pi_tau, contradicting that failing sequence.

The resource-uniform comparison stated after (8) has the same justification:
all Lambda have bounded total mass and support in the same compact positive
energy interval. Every sequence has a weakly convergent jump-measure
subsequence; its compound-Poisson characteristic functions and means converge
to those of the limiting jump measure. Equation (34) gives W1 for these
target laws and for the exact laws along that subsequence. This uses no
convergence of the frequency paths themselves and supplies no W1 rate.

As a quantitative specialization, if every component integral of both
f and g vanishes, the channel kernel is L1 and the weighted synthesis maps
are bounded independently of T, as proved in corrected859/correlation335.
Those estimates require only a bounded real scalar drive: multiplication
by c_h has norm at most A. Their causal inverse is small in h, the weighted
Born remainder is O(h^2 sqrt(T))=O(h), and ||Z_h-I||=O(h). Using (26) and
the same graph argument therefore improves both errors in (7) to O_s(h)
and O(h) in this subclass. It does not yield a W1 rate or remove the strict
frequency/resource assumptions from the general-slot theorem.

## 9. A distinct piecewise-constant check and degenerate cases

There is a useful independent check of the secular coefficient and jump
interpretation which does not linearize the chirped phase. Suppose a and
Omega are constant, a_j and omega_j>2m, on each interval of a fixed finite
macroscopic partition. On its physical interval I_j, phi_h is exactly
an affine phase of slope omega_j, with the continuity-determined offset.
The diagonal j=j term of the spectral integral is a constant-frequency
cosine calculation with that arbitrary offset. The difference-phase part
and Fourier inversion give

    h^2 integral b(e)|I_j(e)|^2de
       =(pi/2)|J_j| a_j^2[b(omega_j)+b(-omega_j)]
                                  +O_b(h^2 log(2+h^-2)), (35)

where J_j is the macroscopic interval truncated at tau. Its sum-phase term
is bounded by oscillatory integration at frequency 2omega_j. The shift in
initial phase has no effect on the leading term.

For j!=k the intervals are disjoint. By (12), their absolute cross term
is bounded, before the exterior h^2, by

    C integral_0^Lj integral_0^Lk (1+x+y+d)^(-2)dxdy
                                        <=C log(2+T), (36)

where d>=0 is their separation and x,y measure distance from the facing
endpoints. The last bound follows by first integrating in y, then in x.
It remains valid for adjacent intervals and for equal or different carrier
frequencies. Thus every cross term vanishes after multiplication by h^2.
Summing the finitely many diagonal terms reproduces (26), without assuming
loss of phase coherence as a physical axiom. In particular, a frequency
jump yields a sum of atoms in Lambda, not a Poisson law with a single
averaged jump energy. This is a substantive analytic check of (5) and the
factor pi/2; it is not a numerical test or a proof of the full BV case.

The finite-step check cannot replace sections 3--6 by an unqualified step
approximation argument. An O(delta) error in Omega can accumulate an
O(delta h^-2) phase error over kinetic time. Approximation at fixed accuracy
is therefore not uniform in h; letting the number of steps grow also
requires controlling (36)'s accumulated constants. The BV translation
argument (29) handles the full class directly and avoids that failed route.

Other checks are exact or immediate from the proved formulas:

* For Omega=omega constant, (5) has one atom and recovers the previously
  checked amplitude-modulated law with Poisson intensity nu_omega J_tau.
* For a=a0 constant as well, J_tau=a0^2 tau. The rate depends on a0^2;
  changing its sign or phi0 does not change the limiting law.
* For a positive value on one macroscopic interval and its negative on
  another, the signs do not cancel the diagonal weights a_j^2. Cross terms
  are controlled by (36), including the shared endpoint. A zero time average
  of the amplitude is not a zero-intensity criterion.
* For a=0 a.e., T=0, or V=0 (for example a slot vanishes or g is a real
  multiple of f), the exact law is delta_0. If instead only
  r(Omega(x))a(x)^2=0 a.e., the proved limit is delta_0
  with vanishing mean/W1; exact finite-h equality is not asserted.
* Frequency jumps change phi_h' but not the continuous integrated phase
  phi_h. BV amplitude jumps change a bounded perturbation at isolated times;
  they do not introduce delta-function kicks. Equations (13), (29) and (30)
  retain all their variation and endpoint contributions.

No actual multi-time measurement law or independent-increment assertion
follows from these marginal formulas. The auxiliary random-sum construction
of Pi_tau is a representation of the limiting single-time distribution.

## 10. Conditional actual-cell transfer and sufficient joint scale

Let ell>0 denote spatial cell spacing, to distinguish it from the amplitude
path a. Assume, rather than construct, the common real energy-adapted embedding
and exterior vacuum of the source premises. In that common Fock space let
V_ell be the embedded centered cell control, selfadjoint and bounded, and
assume for a fixed finite calibration order N that

    ||V_ell-V||<=d0 epsilon_ell,
    ||[H0,V_ell-V]||<=d1 epsilon_ell,
    ||[H0,V_ell]||,||[H0,V]||<=k1,
    ||B_ell-B||<=d_B epsilon_ell,
    epsilon_ell=O(ell^(N+1)).                         (37)

The commutator forms are assumed bounded on D(H0) x D(H0), not merely
reported as formal expressions on unspecified vectors. For bounded
selfadjoint controls this implies preservation of D(H0), by the defining
adjoint characterization of D(H0), and gives the resolvent commutation
identity used below. The energy and vacuum are the same under the
embedding; for the one-particle comparison its extension uses the same
free D on the common real carrier. The one-particle estimate is explicit;
it is needed when also transferring the operator/correlation bounds, not as a substitute for the
weighted commutator estimate. No actual embedding, alias, frame, inverse
or calibration construction is proved in this note.

For the same chirped scalar drive, put

    D_h(t)=integral_0^t |lambda c_h(s)|ds
                                     <=A tau_star/h.

Let rho_h(t) and rho_ell^E(t) denote the full pure states in this common
Fock space. Common free conjugation gives the same comparison for the
interaction states. Unitary bounded-perturbation Duhamel gives

    ||rho_ell^E(t)-rho_h(t)||_1<=2d0 epsilon_ell D_h(t),
    ||Z_ell(t)-Z_h(t)||<=d_B epsilon_ell D_h(t).        (38)

The energy comparison must be proved separately. For R>0 regularize
H0 by H_R=H0(1+H0/R)^(-1), and write Q_R=(1+H0/R)^(-1). Resolvent
commutation gives [H_R,V]=Q_R[H0,V]Q_R and likewise for V_ell.
The bounded-H_R work identity holds directly; Q_R converges strongly to I,
the commutators have a uniform norm bound and D_h(t)<infinity. Passing to
the limit in that identity proves finiteness and the exact first-energy
work identity, without a second moment and without differentiating c_h.
Subtracting the two work identities and using (38) gives

    |E_ell(t)-E_h(t)|
       <=epsilon_ell[d1 D_h(t)+k1 d0 D_h(t)^2].        (39)

The factor in the quadratic term follows from
integral_0^t D_h'(s)D_h(s)ds=D_h(t)^2/2. Thus the sufficient joint scale

    h->0, ell->0, epsilon_ell=o(h^2),
    in particular ell^(N+1)=o(h^2),                  (40)

makes the state/law and mean errors vanish uniformly on bounded kinetic
windows. The common H0 spectral projections transfer the characteristic
law; the separate mean and nonnegative-tail argument (34) transfer W1.
The embedded actual-cell energy laws therefore have the same marginal
limit (5)--(8), conditionally on (37) and the common embedding premises.

Only epsilon_ell=o(h) is needed for the unweighted state/law comparison
in (38). It does not follow that this weaker scale transfers means or W1:
small trace distance alone permits rare arbitrarily high-energy tails.
Condition (40) is sufficient, not claimed necessary or optimal. It also
makes the one-particle comparison term epsilon_ell/h=o(h), smaller than
the general eta_h bound. This last fact preserves the corresponding
finite-mode consequences if desired; it adds no cell-construction theorem.

## 11. Topology check, limitations and failed estimates

The nontrivial marginal law is consistent with a small one-particle norm.
Equation (23) and CAR telescoping give, for a word of degree k in fixed or
varying bounded-norm real slots, an expectation error at most
k d_h product ||f_j||, where d_h=C eta_h. The exact occupation satisfies
0<=N_h<=d_h^2 I. For every finite-rank one-particle projection Q,

    ||rho_h,Q-|0_Q><0_Q|||_1
                      <=2 min(1,sqrt(rank(Q))d_h).     (41)

The finite-mode number expectation bounds nonvacuum probability by
rank(Q)d_h^2; the trace estimate follows from the elementary pure-state
distance and convexity. Hence excitation probability at least p0 requires
rank(Q)>=p0/d_h^2 when d_h>0. This is a necessary resource bound, not an
optimal rate or sufficient detector. A finite energy band has infinite
rank in this continuum.

For fixed tau the free gap isolates the vacuum event: use the spectral
interval (-b0,b0) with 0<b0<m, whose boundaries have zero limiting mass.
Thus (7) gives
p_h=|<0|Y_h|0>|^2->exp(-ell_tau). Global purity gives trace distance to
the vacuum tending to 2sqrt(1-exp(-ell_tau)). Fixed CAR observables still
converge to their vacuum values by polynomial approximation. Finite-rank
Fock sections and (41) give compact-operator expectations converging to
exp(-ell_tau)<0|K|0>. Their vacuum/nonvacuum cross block is bounded by
the square root of the nonvacuum section mass; then compact approximation
passes to arbitrary compact K. These are different topologies, not a
contradiction and not spatial local-algebra norm convergence. The same
reasoning applies to the full state because its energy law and vacuum
probability agree and its occupation is a free conjugate with the same
operator bound. No energy-current or spatial-escape law is inferred.

The strict lower frequency gap is used in (15), (18) and the near-near
Born estimate; the BV resources enter (13) and (29). If the gap closes
or variations grow with h without fixed bounds, these estimates no longer
provide the theorem. Their failure is not a counterexample to a different
threshold, massless or high-variation theorem. Keeping the absolute
||L||=O(sqrt(T)) estimate and applying a small-hT Neumann series is another
failed route on the whole kinetic interval. Equation (17), not that
uncontrolled series, is the needed inverse.

The phase-localization error was bounded by O(h); the full remainder by
eta_h. No optimality is asserted. The supplied model, vacuum and free
dispersion are premises. The theorem does not derive them from axioms,
fit a physical constant, certify an empirical prediction, assume a Markov
limit, or identify a physical instantaneous emission mechanism.

## 12. Exposure, evidence and next decision

The neutral plan and exact source pins were frozen before the substantive
derivation. A contemporaneous precision record preserves the exploratory
pre-plan ideas: frequency-dependent spectral weighting and a threshold/far
input-energy split were considered as possibilities, not established
conclusions. The four exact source bodies in section 2 were already fully
read in the preceding task; their complete argument coverage and byte
identities were reused and refreshed. Corrected859's graph/overlap passage
was also reread for this task. Its earlier picture defect and root miss
remain historical; the corrected V2 identity, not the defective847 version,
is used here.

No CHIRPED_KINETIC_LAW_ROOT_PLAN.md, new root chirp file or root finding
was opened. No other new worker mathematics or external literature was
used. This is a separate same-family derivation excluding the new root
chirp work, with substantial prior source exposure to the modulated and
kinetic machinery. It is not a blinded or model-diverse check. The selected
model and effort were unchanged; no extra agent was spawned.

The new load-bearing steps are the BV reciprocal-phase control in the
nonconvolution causal square, the full-input energy split and Plancherel
bound (18)--(20), the threshold-separated chirped Born operator estimate,
and the integrated BV phase-localization/sum-phase proof (26)--(30).
The finite-step calculation (35)--(36) is a genuinely different analytic
check of the resulting coefficient and jump interpretation. It is not a
second independent reviewer or a numeric simulation. The normalized graph
identity is inherited and its hypotheses are freshly established above.

No scientific numerical runner, finite-volume approximation, Lean/formal
build or interval computation was executed. Source copying, hashing and
membership checks are bookkeeping only. Actual records, full-source read
coverage, failed routes, source refresh, current checkpoint and immutable
final freeze accompany the note in chirped_kinetic_law_independent/. No
finding was sent to the parent before that final freeze. No Git, CW,
canonical runner/cache/pipeline, PR, audit, axiom, editable prompt or
other-chat mutation occurred. The prior source assembly remains unchanged;
its J-versus-Poisson-intensity wording correction is reserved for a later
publication copy and was not silently applied to that frozen archive.

The next decision is a focused ordinary analytic comparison/review after
the separate root derivation is frozen, especially of (13)--(23) and the
uniform BV localization in (29). Root acceptance, publication and retained
audit are separate from this author's completed conditional derivation.


## Publication reconstruction, provenance and verification limits

The source packet preserves the complete 162-file accepted source assembly,
including its earlier wrapper and raw diffs, with all 106 selected source
aliases and the exact immediate root, independent and comparison closures.
Nested receipts are preserved at their documented scope. This is not a
recursive upstream audit or a closure of every cited proof obligation.

Both mathematical cores above are byte-for-byte unchanged. Exact byte and
line maps bind each to the accepted assembly and to this publication note.
Complete n=3 diffs bind the earlier note and each old wrapper piece to the
publication wrappers; the historical one-line phase correction is archived.
The convention is LF-preserving difflib.diff_bytes(unified_diff), three
context lines, literal labels and no timestamps. Raw diff bytes are stored
in lossless gzip archives with exact raw and stored pins. Context-marker
spaces are preserved, with no broad whitespace exemption.

The accompanying identity runner has zero mathematical predicates. It reads
the declared compressed archive, reconstructs this exact note, checks the
four canonical parents and five contained-core maps, and checks the pinned
scope metadata. It performs no scientific calculation, simulation, proof or
formal audit. Its five resolution statements explicitly record scientific
nonexecution. An identity match is not mathematical verification.

During publication source preparation, neither that runner, its canonical
cache, graph builder, prepare/verify driver nor combined validation program
was executed. Source-only reconstruction and syntax checks have separately
retained actual logs. Root must review the exact source freeze and complete
driver before installation, then run the prescribed canonical cache and
graph integration, stage the exact path list, and verify index/worktree
identity before the changed-evidence checker. Current-main combined landing
validation, strict audit lint and effective retained review remain separate
obligations. Earlier accepted author/source reviews are not converted into
new independent scientific reviews by this packaging.
