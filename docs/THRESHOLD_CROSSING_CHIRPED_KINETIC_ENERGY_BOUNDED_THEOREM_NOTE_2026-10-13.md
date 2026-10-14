---
title: "Kinetic energy marginals through the pair threshold in the supplied massive free CAR vacuum"
claim_id: threshold_crossing_chirped_kinetic_energy_bounded_theorem_note_2026-10-13
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
assembly_status: publication_source_of_accepted_conditional_cores
scientific_execution: none_in_publication_source_preparation
runner: scripts/threshold_crossing_chirp_identity_2026_10_13.py
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied massive free CAR model and vacuum; fixed real compact smooth slots; fixed positive lower frequency and BV resources; separate conditional cell premises
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: bounded positive analytic theorem with explicit supplied dynamics and resource hypotheses, preserved derivations and separate source-exposed checks
next_trace_action: root review of exact publication source and two-phase integration; effective retained audit remains separate
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies:
  - chirped_kinetic_energy_bounded_theorem_note_2026-10-13
  - general_compact_control_kinetic_energy_bounded_theorem_note_2026-10-13
  - two_zero_kinetic_energy_bounded_theorem_note_2026-10-13
---

# Kinetic energy marginals through the pair threshold

**Type:** bounded_theorem

Claim type: bounded_theorem

Current surface: conditional-support. The exact 275-line root and 788-line
independent proof cores below received ordinary conditional analytic
acceptance at 15:01:34 UTC on 2026-10-13. The publication wrapper assembles those cores;
it adds no new theorem or audit verdict. Historical pending-review sentences
inside the cores remain verbatim and are superseded only as review history
by this dated wrapper. Publication and effective retained status are separate.

## Precise bounded conclusion

In the supplied two-component massive free CAR vacuum, arbitrary fixed real
compact smooth control slots admit the displayed kinetic energy marginal law,
separate mean and Wasserstein-one limit for resource-bounded real BV chirps
with fixed positive lower frequency, including equality with or crossings of
the pair threshold 2m.

The supplied dynamics are D(p)=-vp sigma_x-m sigma_y, with fixed m,v>0,
E(p)=sqrt(m^2+v^2p^2), the real structure Gamma k(p)=overline(k(-p)), the
specified positive-band Fock vacuum and free energy H0=dGamma(E). Fix real
f,g in C_c^infinity(R;R^2), F=(f,g), and M=2i[[0,1],[-1,0]]. The drive uses
the centered quadratic V and B=FMF* with their exact normalizations below.
No componentwise zero-integral condition on the slots is imposed.

Fix a finite slow-time interval [0,tau_star], a finite amplitude bound A,
finite variation bounds V_a,V_Omega and frequencies 0<omega0<=W<infinity.
Real BV profiles obey ||a||_infinity<=A, Var(a)<=V_a,
omega0<=Omega<=W a.e. and Var(Omega)<=V_Omega. With h=|lambda|,

    c_h(t)=a(h^2 t) cos(phi_h(t)),
    phi_h(t)=phi0+h^(-2) integral_0^(h^2 t) Omega(u)du,
    T=tau/h^2, 0<=tau<=tau_star.

The integrated phase is continuous even at frequency jumps. Monotonicity,
transversality, a finite crossing count and exclusion of a plateau at 2m are
not hypotheses. Representative changes on null sets do not change the
dynamics. Constants may depend on the fixed spatial/model data and resource
bounds; they do not depend on the particular bounded profile or on h.

Let r be the exact pair-energy pushforward density with the factor 1/2 in
the cores. Its extension by zero below 2m is continuous with r(2m)=0. Then

    Lambda_tau(de)=(pi/2) integral_0^tau
                        a(u)^2 r(Omega(u)) delta_(Omega(u))(de)du,
    chi_Pi_tau(s)=exp integral (exp(i s e)-1)Lambda_tau(de).

The exact one-time H0 law converges to Pi_tau, its mean converges to
integral e Lambda_tau(de), and convergence holds in Wasserstein one.
For each fixed real s the characteristic-function error and mean error are
O(eta_h), eta_h=sqrt(h log(2+h^(-2))). The W1 statement is qualitative,
uniform over the fixed resource class and tau; no W1 rate is stated.
An h-dependent family of profiles is compared to its own Lambda_tau,h.
A limit to one fixed law requires convergence of that measure family.

The full signed one-particle interaction propagator Z_h, rather than only a
pair block, satisfies for every fixed q>=0 on the same kinetic horizon

    ||E^(q/2)(Z_h-I)|| <= C_q eta_h,
    ||E^(q/2)(Z_h-I-K1_h)||_HS <= C_q eta_h,
    K1_h=-i lambda integral_0^T c_h(t)F_t M F_t*dt.

These mean bounded extensions established in the graph norm of the weight.
The vacuum energy mean is separately obtained by nonnegative energy cutoffs
and the q=1 bound. It is not inferred by differentiating characteristic
functions. The small full operator and weighted Hilbert--Schmidt remainder
also support the graph determinant argument, with all CAR normalizations
kept in the cores.

The jump measure gives zero weight to frequencies at or below 2m. A profile
entirely in that region has limiting energy law delta_0 and mean zero.
The direct threshold-plateau check gives Born energy O(h^2 log(2+T)), compatible
with the exact estimates. Zero slots, linearly dependent controls, zero
amplitude or vanishing sampled density are allowed and can yield delta_0.
The law constructs individual marginals; it asserts no measured multi-time
counting process, Markov dynamics, or independent quantum increments.

## Obligation graph and mathematical imports

The load-bearing new identity is Fhat(0) M Fhat(0)^T=(det Fhat(0))M for real
Fhat(0), together with proportionality of M and D(0). Opposite signed
threshold coefficients therefore vanish before norms are taken. This has
three distinct operator uses, each proved in both cores.

| Obligation | Status and location in the unchanged cores |
| --- | --- |
| Real threshold matrix identity and both band orientations | Root section 2; independent section 3: direct finite algebra |
| Causal square and kinetic-time resolvent | Root section 3; independent section 4: crossed coefficients vanish, same-band phases use omega0 |
| Full signed input, including the opposite threshold row | Root section 4; independent section 4: row vanishes before energy-density and Plancherel bounds |
| Weighted full Born operator and graph domains | Root sections 4--5; independent sections 5--6: exact threshold decomposition, all fixed q |
| Threshold density and BV secular estimate | Root section 6 composes the checked parent estimate; independent section 7 provides its threshold-continuous resource-uniform form |
| Pair normalization, graph law, mean and uniform W1 | Root section 6; independent sections 8--10: distinct weighted mean and compact-target tail argument |
| Degenerate controls and invalid-hypothesis witnesses | Independent section 11 and the frozen comparison: concrete analytic controls |
| Optional actual-cell implication | Both cores retain exact common-energy/control/commutator premises; no new embedding is constructed |

The direct source parents are the
[strict-gap chirp theorem](CHIRPED_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[general compact-control theorem](GENERAL_COMPACT_CONTROL_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md), and
[corrected weak-drive theorem](TWO_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md).
These canonical links have exact source and published-byte bindings. The chirp
owner contains both unchanged 515/850 cores; the other two contain unchanged
470/859 respectively. The parents supply stationary phase, corrected CAR
pictures, energy/graph machinery and the conditional cell comparison.
Their use here is ordinary conditional source dependence, not a claim that
this assembly has established their retained audit status.

PARENT_BINDINGS.json gives four byte-containment maps in three canonical
parents, with full hashes and line ranges. The actual strict-gap chirp
parent is regular OPEN PR9520 at af2e44428a10e59cf5eb7130df4265d2949db8df,
as recorded by its creation and attachment receipts. Its canonical1593 has
SHA-256 b0df91a85971695996ac32233c112dbe6718223ad733d1a28424666c9bde3874.
The intended threshold branch is physics-loop/toe-threshold-crossing-chirp-20261013,
directly based on that head. Source preparation creates no branch or PR.
Modulated, correlation and initial-state ancestry does not itself add a
direct mathematical dependency to this theorem.

## Boundaries and failed shortcuts preserved

All fixed resources and supplied structures are hypotheses. The current
proof makes no claim for a vanishing omega0, a massless limit, moving slots,
diverging BV/amplitude bounds, arbitrary complex slots or a changed control
matrix. These exclusions are scope boundaries, not impossibility theorems.

The two invalid-hypothesis controls are explicit matrices: complex
Fhat(0)=diag(1,i) with the original M, or real Fhat(0)=I with M replaced by
sigma_z, have a nonzero crossed threshold coefficient. They check the
dependence of this algebra on its hypotheses; they do not assert failure
of every possible kinetic limit for those different models.

Setting the old denominator omega_min-2m to zero does not justify the old
estimates. Pair-density vanishing alone does not prove full operator
cancellation. Discarding the signed input or attaching an unbounded output
weight after an unweighted estimate also leaves the needed obligation open.
The new cores explicitly replace those shortcuts. The general pair kernel
has O(t^-2) decay; no finite absolute first-time moment is silently assumed.
A fixed-accuracy step approximation to Omega has a phase error that can grow
as h^-2 and is not used as the uniform BV proof. These are records about
specific attempted estimates, not a no-go claim or a fabricated N-gate PASS.

Actual-cell transfer is a separate conditional implication under the exact
real energy embedding, common H0, unital band-Fock identification, exterior
vacuum and stated control/commutator errors. The displayed joint sufficient
scale is epsilon=o(h^2) for the mean/law/W1 conclusion. Necessity and a new
physical realization are not proved. The strongest unresolved application
obligation is verifying those concrete embedding and error hypotheses for a
specified cell family; it is not hidden as a lemma of the supplied-model
theorem. There is no identified open analytic lemma inside the accepted
conditional theorem. Ordinary source review and retained audit remain
distinct from that assessment.

## Source exposure, checks and finite algebra history

The root plan followed disclosed preliminary reasoning from shared parents,
and its proof was frozen at 14:20:53 UTC, before receiving independent target
findings. The fresh independent plan froze at 14:25:58 UTC; its proof froze
at 14:48:48 UTC with root target science, the aborted earlier worker's partial
findings and Lean excluded. Shared strict-gap parents were allowed from the
start. The fresh author later read the full root275 and froze comparison312
at 14:59:26 UTC. That comparison assesses root and self-checks the author's
own788; it is not a fresh independent verdict on its own derivation.

Root then read the full independent788, author checks and comparison312 and
issued acceptance1067eaa3 with reviewece4f214. No formula repair was requested.
The two Born decompositions differ: root uses smooth band-preserving frames;
independent uses auxiliary threshold-constant columns that need not remain
in the moving bands. Each exactly factors the actual kernel. The comparison
preserves this distinction and checks every cancellation use and normalization.
The derivations share a model family and parent arguments; model-diverse
verification is not claimed. Publication preparation is source exposed and adds only
an author packaging check.

Optional Lean corroboration was opened by this assembler only after both
independent and comparison freezes. It verifies three finite matrix identities
over a commutative ring: the alternating 2 by 2 transpose identity and two
opposite-band zero products with u^2=-1. The real-Fourier transpose/adjoint
identification, physical normalization, stationary phase, domains, BV
bounds, continuum CAR construction, and limiting laws remain analytic work.

Actual attempt01 exited 1 after a missing Fin.sum_univ_two import; its
unsolved goals and compiler-generated sorryAx diagnostics are preserved as
failed output. A single targeted import produced attempt02 source
d8ee4d04487b66c4a6e7794f477e3c56b4886916f9b5c76e163335df8a978ec4.
Actual attempt02 exited 0, printed only propext, Classical.choice and
Quot.sound for all three theorems, and retained three tactic-linter warnings.
The exact source snapshots, diff, seals, compiler streams, execution records,
original bounded runners and resulting olean are archived. This assembly did
not rerun them. That certificate verifies finite algebra only.

## Unchanged root core

The following 275 lines have SHA-256
6a5fba2249be73609673ccacc05369af478d4c2adf5feb0d2752a683629183b4.


# Chirped drives through the pair threshold

Provisional source-exposed root derivation. A new separate target check is
required before acceptance. This uses the supplied real two-component free
CAR model; it changes no physical axiom. The prior strict-gap theorem and
its frozen proofs remain valid and unchanged. No new numerical or formal
verification is claimed here.

## 1. Exact target and accepted inputs

Keep corrected859's K=L2(R;C^2), real conjugation Gamma fhat(p)=bar fhat(-p),
D(p)=-vp sigma_x-m sigma_y, E(p)=sqrt(m^2+v^2p^2), m,v>0,
P_epsilon(p)=(I+epsilon D(p)/E(p))/2. Fix real compact smooth slots f,g,
F=(f,g), M=2i J, J=[[0,1],[-1,0]], B=FMF*. Fhat(p) denotes the two-column
Fourier matrix; F_0=Fhat(0) is a real2x2 matrix. All slots and model
parameters remain fixed. F_0 need not be invertible or have nonzero determinant.

Use exactly the Fock control V and full/interaction propagators W,Y,S,Z
of the accepted chirp V2/515 and independent850. With h=|lambda|, let

 c_h(t)=a(h^2t)cos(phi0+h^-2 integral_0^(h^2t)Omega(u)du),
 0<omega_0<=Omega(u)<=W_0<infinity,
 ||a||_infinity<=A, Var(a)<=V_a, Var(Omega)<=V_Omega,
 0<=T<=tau_star/h^2.                                  (C1)

Profiles are real BV, with their phase integrated continuously across jumps.
The lower frequency is separated from zero, **not** from2m. The budgets,
positive mass, horizon and spatial slots stay fixed. Crossing2m, jumping
across2m or having a plateau at2m are allowed by the proposed conclusion.

The unchanged drive-independent parents supply the stationary phase kernel

 G(t)=F*exp(-itD)F
     =q(t)sum_(epsilon=+-1)exp(-i epsilon mt)C_epsilon+R(t),
 q(t)=(1+t)^-1/2, ||R(t)||<=C(1+t)^-3/2,
 C_epsilon=k_epsilon F_0*P_epsilon(0)F_0,              (C2)

where k_epsilon is the scalar nonzero Gaussian stationary phase coefficient.
The exact scalar is immaterial only for the cancellation below. It is the
same coefficient as the accepted expansion, not a modified normalization.
The expansion and all weighted synthesis estimates hold with fixed energy
powers. They use E=m+y^2 and Schwartz amplitudes, independently of C1.

The target is the same full weighted operator/HS estimate as before:

 ||E^(q0/2)(Z-I)||<=C_q0 eta_h,
 ||E^(q0/2)(Z-I-K1)||_HS<=C_q0 eta_h,
 eta_h=sqrt(h log(2+h^-2)), q0>=0 fixed,               (C3)

and the same resource-uniform one-time law/mean, now with

 Lambda_tau(de)=(pi/2) integral_0^tau
          a(u)^2 r(Omega(u)) delta_Omega(u)(de)du.     (C4)

The density r is the exact exterior-pair density, extended by zero below2m.
No new normalization or channel multiplicity is introduced. Char-functions
and means should have O_s(eta_h), O(eta_h) errors; W1 should converge
qualitatively, without a claimed rate. Sections2--5 repair the three proof
steps for which the old strict gap was used.

## 2. The threshold matrix cancellation

For any real2x2 matrix A, direct multiplication gives

 A J A^T=(det A)J.

Since D(0)=miJ, the exact threshold matrix is

 B_0=F_0 M F_0^*=(2 det F_0/m)D(0).
 P_epsilon(0)B_0P_delta(0)=0 if epsilon!=delta.        (C5)

Consequently

 C_epsilon M C_delta=0 if epsilon!=delta.             (C6)

Indeed expand C_epsilon M C_delta using C2 and insert B_0 in its middle.
The scalar stationary phase coefficients do not affect the zero. This is
an exact matrix identity before taking a norm; pair-density vanishing
alone would not justify discarding a full-input term. It uses the actual
real2x2 slot matrix and this rank-one band structure. No extension to a
generic multiband or complex-slot control is asserted.

## 3. Causal square without a gap above2m

Keep the accepted exact channel equation X=X0+lambda L_h X,

 X(t)=F_t*Z(t), X0(t)=F_t*, F_t=exp(itD)F,
 (L_h x)(t)=-i integral_0^t G(t-s)c_h(s)M x(s)ds.

Its exact squared kernel contains, for sigma=+-1,

 integral_0^r G(r-z)a(h^2(s+z))exp(i sigma Phi_h(s+z))M G(z)dz.          (C7)

After inserting C2, its leading band-epsilon/band-delta scalar phase is
-epsilon mr+(epsilon-delta)mz+sigma Phi_h(s+z).
Every epsilon!=delta coefficient is zero by C6. For the remaining terms
the derivative is sigma Omega(h^2(s+z)), of fixed sign and absolute value
at least omega_0. Its variation is at most V_Omega. The BV integration
lemma from the accepted chirp sources therefore bounds their integrals by

 q(r)[(4A+V_a)/omega_0+A V_Omega/omega_0^2].           (C8)

Terms containing R have the same absolute q*(1+t)^-3/2 bound as before.
Thus ||L_h||<=C sqrt(1+T) and ||L_h^2||<=C sqrt(1+T), also in HS
amplification. The actual operator square is being bounded. The exact
polynomial inverse identity then gives

 ||(I-lambda L_h)^-1||
 <=[1+C h sqrt(1+T)]/[1-C h^2 sqrt(1+T)]<=C          (C9)

on every fixed kinetic horizon for sufficiently small h. This is not an
hT expansion. The old all-coefficient absolute majorant obscured C6 and
therefore needed a stronger frequency gap than this step actually uses.

## 4. Full-input forcing with its matrix row retained

A leading term from band e in C2 acting on input band epsilon has the
matrix row

 R_(e,epsilon)(p)=C_e M Fhat(p)^*P_epsilon(p),

and scalar time integral, up to a unit-modulus factor and the fixed cosine
coefficient,

 J_(e,epsilon,sigma)(t,E)=integral_0^t q(t-s)a(h^2s)
        exp(i sigma Phi_h(s)-i(epsilon E-e m)s)ds.    (C10)

For e!=epsilon, C5 implies R_(e,epsilon)(0)=0. Smoothness gives
R_(e,epsilon)(p)=O(p), and Schwartz decay holds at infinity. Hence its
actual energy density

 w_(e,epsilon)(E)=sum_(p=+-sqrt(E^2-m^2)/v)
                  ||R_(e,epsilon)(p)||_HS^2/|E'(p)| (C11)

is bounded on [m,infinity): it is O(sqrt(E-m)) at threshold. Applying
temporal Plancherel to C10 over the full energy line costs at most
C A^2 log(1+t). It allows resonances moving through the threshold because
the singular Jacobian has already been canceled in C11.

For e=epsilon the matrix row need not vanish at zero. Fix
0<b<omega_0/4. On m<=E<=m+b, the phase derivative in C10 is
sigma Omega-epsilon(E-m), with modulus at least omega_0-b. The amplitude
has supremum A and variation at most A+V_a. The BV integration lemma
bounds J there uniformly. The original O((E-m)^-1/2) density is integrable
on this strip. Outside it the density is bounded, so Plancherel again
costs C log(2+t). This handles every input sign, carrier sign and leading
band, without substituting a negative-band-only estimate.

The R part in C2 is L1 in time and contributes a bounded HS row. Thus

 ||L_h X0||_(L2([0,T];HS))<=C sqrt(T log(2+T)),
 ||X-X0||_(L2 HS)<=C h sqrt(T log(2+T)).               (C12)

The weighted synthesis norm remains ||S_q0,T||<=C_q0(1+T)^1/4.
Exact Dyson integration and C12 give the weighted HS remainder C3.
Each finite-time integral first exists in its energy graph norm since the
slots have all fixed energy moments; closedness identifies the bounded
weighted operator. No unbounded weight is attached to a norm estimate
without this domain argument.

## 5. Small full Born operator at a threshold crossing

The HS remainder alone is insufficient: the whole first Born operator K1
must be small in operator norm. Choose a smooth cutoff chi(E-m), equal to
one near0 and supported in [0,b], with b as above. Far synthesis and
analysis are uniformly bounded in T by their bounded energy densities;
near ones cost O((1+T)^1/4). This holds with each fixed output energy power.
Every Born term with a far factor is therefore O(h(1+T)^1/4).

For both near factors, use smooth normalized band frames e_epsilon(p).
Write their channel rows and decompositions as

 v_epsilon(p)=e_epsilon(p)^*Fhat(p),
 U_epsilon(p)=chi(E(p)-m)e_epsilon(p)v_epsilon(p),
 U_epsilon^0(p)=chi(E(p)-m)e_epsilon(p)v_epsilon(0),
 R_epsilon(p)=U_epsilon(p)-U_epsilon^0(p)=O(p).        (C13)

These are finite-channel column maps into the signed band. For opposite
bands, C5 gives the scalar channel identity

 v_epsilon(0) M v_delta(0)^*=0, epsilon!=delta.

Thus the complete opposite-band near kernel decomposes exactly as

 U_epsilon(p)M U_delta(q)^*
  =R_epsilon(p)M U_delta(q)^*
                +U_epsilon^0(p)M R_delta(q)^*.       (C14)

Each term has one factor with a bounded energy density: squared O(p)
vanishing cancels the inverse Jacobian, exactly as in C11. That factor's
synthesis/analysis norm is O(1) by Plancherel; the other is O((1+T)^1/4).
Multiplication by the actual scalar c_h on the common time space costs
only A. Hence these Born terms have operator norm O(h(1+T)^1/4), even
at an exact frequency plateau2m. A possible cross term R_epsilon M R_delta*
is already included in the first term of C14, not omitted.

For same-band near kernels the phase derivative is
epsilon(E(p)-E(q))+sigma Omega(h^2t). Since both energies lie in [m,m+b],
its absolute value is at least omega_0-b and its variation at most V_Omega.
The BV lemma gives a uniform time integral. The resulting kernel has an
actual HS majorant C h||U_epsilon(p)|| ||U_epsilon(q)||. On this fixed
strip all fixed output energy weights are bounded. Thus these terms are
O_q0(h) in weighted HS and operator norm.

Combining the near and far terms gives

 ||E^(q0/2)K1||<=C_q0 h(1+T)^1/4<=C_q0 sqrt(h)        (C15)

on a fixed kinetic horizon, with harmless adjustment for T=0/small h.
C15 and the independently proved HS remainder establish both C3 bounds.
This uses the exact signed-band decomposition, not a scalar HS estimate
on the vacuum pair alone.

## 6. Secular measure and consequences at the checked scopes

The accepted density proof gives r(2m+x)=x rho(x), with rho smooth up to0,
and inverse-square Fourier decay for b=r, er and r(exp(ise)-1). These
remain statements about fixed slots, independent of the frequency path.
The resource-uniform chirp secular proof independent850(section6) uses:
bounded amplitude/variation; the BV translation bound for Omega; positive
omega_0 to control the sum-phase derivative Omega(u)+Omega(v); and Fourier
inversion at the instantaneous carrier. It does not use Omega>2m in that
proof. Since the zero extension of r is continuous also at2m, its same
formula holds there and below it. In particular b(-Omega)=0 for every
positive Omega. Keeping the original integrated phase gives

 h^2 integral b(e)|integral_0^(tau/h^2)c_h(t)exp(iet)dt|^2de
       =(pi/2)integral_0^tau a(u)^2 b(Omega(u))du+O_b(h).              (C16)

The weighted Born HS norms remain uniformly bounded even without C16:
the absolute integrable Fourier kernel bounds their squares by C h^2 T.
The accepted graph, determinant and positive energy identities now apply
using C3 and these HS bounds. They give

 chi_h,tau(s)=exp[integral(exp(ise)-1)Lambda_tau(de)]+O_s(eta_h),
 <H0>_h,tau=integral e Lambda_tau(de)+O(eta_h).         (C17)

The separate mean estimate is not a derivative of the characteristic
limit. The fixed-profile and resource-uniform W1 arguments use compact
positive energy support and bounded jump mass. Here r(Omega)=0 for
Omega<=2m, so Lambda has support in [2m,W_0] when nonzero. If W_0<=2m
it is simply zero. The same compact-measure subsequence and positive-tail
proof therefore gives qualitative resource-uniform W1 convergence. There
is still no claimed W1 rate.

If the entire profile lies below or at2m, C17 has zero limiting mean and
the energy law tends to delta0. The exact free gap then implies convergence
of the driven vacuum density to vacuum in trace norm. For a profile that
crosses2m, C4 counts only its above-threshold contribution, with the same
vanishing density at the crossing. No subleading crossing law, transition
boundary layer or altered microscopic interaction has been derived.

The inherited bounded CAR correlation conclusions use C3 unchanged.
The actual-cell work comparison does not require a gap of Omega from2m:
under its exact common-energy, control and commutator-error hypotheses,
epsilon=o(h^2) still transfers the one-time mean/law/W1 conclusion.
These are conditional implications only. Multi-time and prepared-state
applications would need their explicit source compositions checked; they
are not independently verified by this note.

## 7. Scope and failure preservation

The old proof's absolute leading-kernel and raw threshold-density estimates
cannot simply set their denominator omega_min-2m to zero. They have been
replaced here by C6, C11 and C14, with the corresponding same-band estimates.
Those old estimates are not rebranded as valid at a crossing. No theorem
about arbitrary complex controls or higher channel multiplicity follows
from this special real2x2 threshold identity. Frequency crossing zero,
massless limits, unbounded BV resources and moving spatial controls remain
outside this construction.

Root has not yet compared this new proof with an independent target
derivation. All upstream hypotheses, exact core identities and unresolved
physical realization obligations remain. The proposed cancellation and
every use of it require a separate check before this extension is accepted.

## Unchanged independent core

The following 788 lines have SHA-256
0406c0e397b82a95159a77e47d093771e19f316c46f80c996ec2969ca082cea4.
They are the fresh derivation frozen before root target or Lean exposure.


# Kinetic energy marginals through the pair threshold

Status: conditional-support; independent source derivation in the supplied
massive free CAR model. This is a proposed ordinary analytic proof, not an
audit verdict, formal certificate, physical model selection or empirical
prediction. The parent supervisor must assess its mathematics separately.

    target_claim_type: bounded_theorem
    actual_current_surface_status: conditional-support
    trace_class: upstream_support
    reachability_to_target: supports
    conditional_surface_status: supplied free CAR dynamics and vacuum
    hypothetical_axiom_status: null
    admitted_observation_status: null
    audit_required_before_effective_retained: true
    bare_retained_allowed: false

The strict separation of the drive frequency from 2m can be removed in this
model while retaining a fixed positive lower frequency and fixed BV resources.
The decisive additional ingredient is an operator-level threshold cancellation.
The pair density alone does not establish it. Sections 3--6 prove three
separate uses of the cancellation, before the graph and energy arguments.

## 1. Supplied model and precise conclusion

Let K=L2(R,dp;C^2), with the unitary spatial Fourier transform, inner product
linear in the second argument, and

    D(p)=-vp sigma_x-m sigma_y, E(p)=sqrt(m^2+v^2p^2),
    P_s(p)=(I+s D(p)/E(p))/2, s in {+1,-1}, P=P_+,
    Gamma k(p)=overline(k(-p)), m,v>0.

These are supplied dynamics and real structure. The physical carrier in this
conditional theorem is Fock(PK), with H0=dGamma(E|PK) and vacuum |0>.
Annihilation is antilinear, and for a real slot k,

    gamma(k)=a*(sqrt(2)Pk)+a(sqrt(2)Pk).

Fix arbitrary real f,g in C_c^infinity(R;R^2). Their component integrals
need not vanish. Let F=(f,g):C^2->K, write Fhat(p) for its 2 by 2 Fourier
matrix, and put

    M=2i [[0,1],[-1,0]], B=FMF*,
    V=(i/2)[gamma(f),gamma(g)]
                      -<0|(i/2)[gamma(f),gamma(g)]|0>I.

All spatial data, m and v are fixed. Fix 0<=tau_star<infinity, nonnegative
finite A,V_a,V_Omega, finite W, and omega0>0. The temporal profiles are real
BV functions on [0,tau_star] satisfying

    ||a||_infinity<=A, Var(a)<=V_a,
    omega0<=Omega(x)<=W a.e., Var(Omega)<=V_Omega.       (1)

Use one-sided representatives in the stated range. Isolated values do not
affect any integral or propagator. No monotonicity, transverse crossing,
finite crossing count or exclusion of a plateau at 2m is assumed. For real
lambda!=0, h=|lambda|, arbitrary phi0, and T=tau/h^2, set

    phi_h(t)=phi0+h^-2 integral_0^(h^2 t) Omega(x)dx,
    A_h(t)=a(h^2t), c_h(t)=A_h(t)cos(phi_h(t)).          (2)

Let W_h solve H0+lambda c_h V, S_h solve D+lambda c_h B, and define
Y_h(t)=exp(itH0)W_h(t), Z_h(t)=exp(itD)S_h(t). All start at I. Bounded
strongly measurable interaction generators give finite-time unitary
propagators. The corrected CAR and picture identities are

    Y_h* gamma(k)Y_h=gamma(Z_h* k),
    i Z_h'=lambda c_h F_t M F_t* Z_h, F_t=exp(itD)F,
    N_h=PZ_h P_- Z_h*P,
    <H0>_h=||E^(1/2)PZ_h P_-||_HS^2.                 (3)

The last identity initially denotes an extended nonnegative form, obtained
with finite-rank and bounded energy cutoffs. Its finiteness is proved below.
The H0 laws of W_h(T)|0> and Y_h(T)|0> agree.

In the smooth scalar positive-band frame set

    theta(p)=arctan(vp/m),
    e_+(p)=(exp(i theta(p)/2),-i exp(-i theta(p)/2))/sqrt(2),
    u(p)=sqrt(2)e_+(p)*fhat(p), w(p)=sqrt(2)e_+(p)*ghat(p),
    Delta(p,q)=u(p)w(q)-w(p)u(q),
    r(e)=(1/2) integral |Delta(p,q)|^2
                         delta(e-E(p)-E(q))dpdq.      (4)

This is an ordinary pushforward density, extended by zero below 2m. Define
the finite positive jump measure and its compound-Poisson law by

    integral b(e)Lambda_tau(de)
      =(pi/2) integral_0^tau a(x)^2 r(Omega(x))b(Omega(x))dx,
    chi_Pi_tau(s)=exp[integral (exp(ise)-1)Lambda_tau(de)]. (5)

The measure puts no mass at or below 2m: r(2m)=0, proved in section 7.
When its total mass is zero, Pi_tau=delta_0. Otherwise Pi_tau is the law
of a sum of a Poisson number of independent marks with measure
Lambda_tau/Lambda_tau(R). This constructs a single marginal law, not a
quantum counting process or a claim of independent increments.

**Conditional theorem.** Put eta_h=sqrt(h log(2+h^-2)). For every fixed
q>=0, all sufficiently small h, and 0<=T<=tau_star/h^2,

    ||E^(q/2)(Z_h(T)-I)||<=C_q eta_h,
    ||E^(q/2)(Z_h(T)-I-K1_h(T))||_HS<=C_q eta_h,
    K1_h(T)=-i lambda integral_0^T c_h(t)F_t M F_t*dt.   (6)

Weighted operators mean their bounded extensions, with the graph-domain
justification in section 5. If mu_h,tau is the exact H0 law, then for each
fixed real s,

    sup_tau |chi_mu_h,tau(s)-chi_Pi_tau(s)|<=C_s eta_h,
    sup_tau |integral e mu_h,tau(de)-integral e Lambda_tau(de)|
                                                        <=C eta_h,
    sup_tau W1(mu_h,tau,Pi_tau)->0.                    (7)

The estimates and the last comparison are uniform over profiles with the
fixed resources (1), initial phases and the sign of lambda. For h-dependent
profiles, (7) compares to their corresponding h-dependent Pi; it does not
assert a single limit without convergence of the target jump measures.
No rate for W1 is claimed. Constants can depend on the fixed slots, m,v,
q,s and resources, particularly omega0; they do not depend on a distance
of Omega from 2m. No omega0->0, m->0, growing variation, moving slot,
interacting spectrum or longer time scale is included.

## 2. Elementary analytic tools and the stationary coefficients

If psi is absolutely continuous, psi'=d has a real BV representative of
one sign with |d|>=delta>0, and w is complex BV, then

    |integral_l^r w(t)exp(i psi(t))dt|
       <=[2||w||_infinity+Var(w)]/delta
                           +||w||_infinity Var(d)/delta^2. (8)

Indeed 1/d is BV with variation at most Var(d)/delta^2. Integrate w/(id)
against d(exp(i psi)) and use Stieltjes integration by parts. The endpoint
terms and the derivative measure, including jumps, give (8). All phase
derivatives used here have a fixed sign on their application interval.

Write q0(t)=(1+t)^(-1/2), t>=0, and G(t)=F*exp(-itD)F. The smooth odd
coordinate

    p(y)=y sqrt(2m+y^2)/v, E(p(y))=m+y^2

changes each band integral to a quadratic phase with Schwartz amplitude.
For t>=1 the Gaussian Fourier identity gives the leading value at y=0
and an O(t^-3/2) remainder: the bound |exp(ix)-1|<=|x| controls the
error by the second absolute Fourier moment of that Schwartz amplitude.
Replacing t^-1/2 by q0(t) changes only the same remainder. Thus

    G(t)=q0(t) sum_(s=+-1) exp(-is mt) A_s+R(t),
    ||R(t)||<=C(1+t)^(-3/2),
    A_s=k_s F0^T P_s(0)F0,
    F0=Fhat(0), k_s=sqrt(2pi m)/v exp(-is pi/4).        (9)

Real spatial slots make F0 a real matrix, hence its adjoint is its
transpose. The same stationary estimate, with possibly different constants,
holds with fixed energy powers or smooth spectral cutoffs. Only its
O((1+|t|)^(-1/2)) bound is needed for general synthesis maps.

For completeness, temporal synthesis of a matrix amplitude H(p) on one
signed band is

    (S_s,H,q z)(p)=E(p)^(q/2)H(p)
                              integral_0^T exp(isE(p)t)z(t)dt.

If H is Schwartz and H(0)=0, its energy density matrix

    e^q sum_(p=+-sqrt(e^2-m^2)/v) H(p)*H(p)/|E'(p)|

is bounded. Near m this follows from H(p)=O(p) and |E'(p)| of order
|p|; at infinity it follows from Schwartz decay. Temporal Plancherel
therefore gives ||S_s,H,q||<=C_q uniformly in T. For a general fixed
Schwartz H, its Gram kernel instead gives
||S_s,H,q||<=C_q(1+T)^(1/4) by Schur's test. These are operator
bounds and also hold after Hilbert--Schmidt amplification.

## 3. The threshold cancellation is an operator identity

Set B0=F0 M F0^T. For every real 2 by 2 matrix F0, direct multiplication
of the alternating form gives

    B0=(det F0)M=(2 det F0/m)D(0).

Consequently B0 commutes with P_s(0), including when det F0=0, and

    P_s(0) B0 P_-s(0)=0.                              (10)

Three exact consequences will be used separately:

    A_s M A_-s=0,
    A_s M F0^T P_-s(0)=0,
    [P_s(0)F0] M [P_-s(0)F0]*=0.                     (11)

For the first identity substitute (9): the middle product is precisely
P_s(0)B0P_-s(0). The second and third follow in the same way, with the
nonzero scalar k_s harmless. Thus the first is a channel-matrix identity,
the second a full-input threshold-row identity, and the third a two-momentum
Born-kernel identity. None follows merely from a scalar statement about r.

There is also a distinct frame check. At p=0, conjugation exchanges the
one-dimensional P_+ and P_- ranges. The two associated slot rows are
complex conjugates. Their cross-band contraction with M reduces to a
scalar of the form z M z^T, which is zero since M^T=-M. This proves
the same opposite-band vanishing without the determinant calculation.

## 4. Causal square and both input signs at threshold

On L2([0,T];C^2), also amplified by Hilbert--Schmidt input columns, put

    (L_h x)(t)=-i integral_0^t G(t-u)c_h(u)M x(u)du,
    X(t)=F_t*Z_h(t), X0(t)=F_t*, X=X0+lambda L_h X.     (12)

The rows X(t) are HS with norm ||F||_HS by unitarity. Thus all finite-time
Fubini operations below are legitimate. From (9), ||L_h||<=C sqrt(1+T).
To improve the square retain the matrix order exactly:

    (L_h^2x)(t)=-(1/2)sum_(sigma=+-1) integral_0^t
                             H_sigma,h(u,t-u)c_h(u)M x(u)du,
    H_sigma,h(u,r)=integral_0^r G(r-z)A_h(u+z)
                              exp(i sigma phi_h(u+z))M G(z)dz. (13)

A leading-leading term with indices s,s' has matrix A_s M A_s' and
scalar phase -s mr+(s-s')mz+sigma phi_h(u+z). If s'=-s, its matrix
vanishes exactly by (11), including at the possible frequency 2m.
For s'=s the derivative is sigma Omega(h^2(u+z)), with magnitude
at least omega0 and variation at most V_Omega. The amplitude
q0(r-z)q0(z)A_h(u+z) has supremum A q0(r) and variation at most
(2A+V_a)q0(r). Equation (8) bounds every surviving leading term by

    q0(r)[(4A+V_a)/omega0+A V_Omega/omega0^2].

Terms containing R are bounded absolutely, using
q0*(1+t)^(-3/2)<=C q0, which follows by splitting at r/2. Therefore

    ||L_h^2||<=C sqrt(1+T),
    (I-lambda L_h)^(-1)
      =(I+lambda L_h)(I-lambda^2 L_h^2)^(-1),
    ||(I-lambda L_h)^(-1)||
      <=[1+C h sqrt(1+T)]/[1-C h^2 sqrt(1+T)]<=C.      (14)

For T<=tau_star/h^2 the denominator is at least 1/2 for small h. The
numerator stays bounded for any fixed finite tau_star. The polynomial/
series identity supplies both inverses; no normality, reordered matrices,
small hT assumption or small fixed tau_star is used.

The forcing requires a separate check on both input bands. A leading term
of L_h X0 on input P_epsilon, up to a fixed scalar factor, has row

    exp(-is mt) R_s,epsilon(p) J_s,epsilon,sigma(t,E(p)),
    R_s,epsilon(p)=A_s M Fhat(p)*P_epsilon(p),
    J_s,epsilon,sigma(t,e)=integral_0^t q0(t-u)A_h(u)
               exp[i sigma phi_h(u)-i(epsilon e-sm)u]du. (15)

Choose once b=omega0/4. When epsilon=-s, (11) says
R_s,-s(0)=0. Its full energy density

    w_s,epsilon(e)=sum_(p=+-sqrt(e^2-m^2)/v)
                         ||R_s,epsilon(p)||_HS^2/|E'(p)|

is therefore bounded on [m,infinity); it is O(sqrt(e-m)) at threshold.
Temporal Plancherel applied to the scalar time function in (15) gives

    integral_R |J_s,epsilon,sigma(t,e)|^2de
                  <=2pi A^2 integral_0^t q0(t-u)^2du
                  =2pi A^2 log(1+t).                 (16)

The sign epsilon and the fixed shift sm merely change the Fourier
orientation and modulation. Bounded w controls the whole crossed-input
contribution, even when Omega equals 2m or stays there indefinitely.

When epsilon=s, the phase derivative in (15) is
sigma Omega(h^2u)-s(e-m). For m<=e<=m+b it has magnitude at least
omega0-b and a fixed sign. Its variation is at most V_Omega. The
amplitude q0(t-u)A_h(u) has supremum A and variation at most A+V_a,
so (8) bounds J uniformly there. The possible w=O((e-m)^(-1/2))
is integrable on that interval. For e>=m+b, w is bounded and (16)
applies. The R remainder in (9) contributes a uniformly bounded HS row
because its time norm is integrable. Summing all signs proves

    ||(L_hX0)(t)||_HS<=C sqrt(log(2+t)),
    ||L_hX0||_(L2 HS)<=C sqrt(T log(2+T)),
    ||X-X0||_(L2 HS)<=C h sqrt(T log(2+T)).             (17)

The last assertion uses (14). This explicitly checks all input signs;
it is stronger than control of only the vacuum excitation block.

## 5. Weighted full remainder and its domain

For fixed q>=0 let S_q z=integral_0^T E^(q/2)F_t z(t)dt. Its weighted
Gram kernel has the bound from section 2, so
||S_q||<=C_q(1+T)^(1/4). Exact Dyson integration and (17) give

    E^(q/2)(Z_h-I-K1_h)=-i lambda S_q c_h M(X-X0),
    ||E^(q/2)(Z_h-I-K1_h)||_HS
       <=C_q h^2(1+T)^(1/4)sqrt(T log(2+T))
       <=C_q eta_h.                                  (18)

At finite T, every fixed column of F belongs to all fixed energy graph
domains. Integration of its free rotations against a time-L2 function on
a finite interval is a Bochner integral in that graph norm, since time-L2
embeds into time-L1 there. Closedness identifies the weighted output.
The same argument applied to each input basis column and summed gives the
HS amplification. The exact finite-time Dyson integral itself is graph-norm
integrable using the bounded HS row X. Thus (18) is an actual weighted
full-input operator identity, not multiplication of an unbounded weight
into a previously unweighted estimate.

## 6. A separate small Born operator bound

Choose a smooth real cutoff chi(E-m), equal to one near zero and supported
in E<=m+b, with the fixed b=omega0/4. For each sign define matrix columns

    W_s(p)=P_s(p)Fhat(p),
    U_s(p)=chi(E(p)-m)W_s(0), H_s(p)=W_s(p)-U_s(p).     (19)

This is an exact auxiliary decomposition; it does not change the physical
slots. Each H_s is Schwartz and H_s(0)=0. By section 2 its weighted
synthesis map with scalar phase exp(isEt) is bounded uniformly in T.
The corresponding U_s map is O((1+T)^(1/4)). These individual columns
need not lie in P_s(p)K; their scalar phase and their exact sum are what
the decomposition uses, so no false band assertion is needed.

Expand the full Born operator with
F_t(p)=sum_s exp(isE(p)t)[U_s(p)+H_s(p)]. Every term with at least one
H factor has weighted operator norm at most C_q h(1+T)^(1/4), by
synthesis--multiplication--analysis and ||c_h||_infinity<=A. This controls
all its frequency resonances without integration by parts.

For the U_s--U_s' terms, the constant matrix is W_s(0)M W_s'(0)*.
It vanishes when s'=-s by (11). When s'=s, expand the cosine: the time
factor has phase derivative

    s(E(p)-E(q))+sigma Omega(h^2t).

On the cutoff support |E(p)-E(q)|<=b, so this derivative has magnitude
at least omega0-b and variation at most V_Omega. Equation (8) bounds its
time integral by a fixed resource constant. The remaining kernel has a
weighted L2(dp dq) product majorant C_q h |chi(E(p)-m)chi(E(q)-m)|;
the cutoff support has finite momentum measure. Its weighted HS norm,
hence weighted operator norm, is O_q(h). Consequently

    ||E^(q/2)K1_h(T)||<=C_q h(1+T)^(1/4),
    ||E^(q/2)(Z_h(T)-I)||<=C_q eta_h.                 (20)

Together (18) and (20) prove (6). The Born HS norm itself need not be
small on kinetic time. Both the cancellation of the two threshold-constant
opposite-band factors and bounded synthesis for a threshold-vanishing
factor are essential to this operator estimate.

## 7. Pair density and a secular lemma with no threshold exclusion

The pair vector V|0> is i(u wedge w), with wavefunction i Delta/sqrt(2).
This fixes the exterior factor 1/2 in (4). The odd momentum coordinate of
section 2 in both variables and polar coordinates give, for x>=0,

    r(2m+x)=(1/4) integral_0^(2pi)
       |Delta(p(sqrt(x)cos t),p(sqrt(x)sin t))|^2
       p'(sqrt(x)cos t)p'(sqrt(x)sin t)dt.             (21)

The angular average of the smooth Schwartz amplitude is smooth in x down
to zero: Taylor expansion through any required even order cancels the odd
homogeneous terms after angular integration, with controlled differentiated
remainders. Antisymmetry gives Delta(0,0)=0. Hence

    r(2m+x)=x rho(x), x>=0,                            (22)

with rho smooth one-sided and with the needed derivatives rapidly decreasing
at infinity. The extension by zero is continuous but need not be C1. For

    b(e)=r(e), e r(e), or r(e)(exp(ise)-1), fixed real s,
    C_b(u)=integral b(e)exp(ieu)de,

two integrations by parts retain the finite derivative boundary term at 2m.
Because b(2m)=0 and b'' is integrable on (2m,infinity),

    |C_b(u)|<=K_b/(1+u^2), C_b in L1(R).              (23)

A finite first absolute time moment is not assumed. The initial-phase,
positive-frequency secular formula needed here is

    h^2 integral b(e)|I_h,T(e)|^2de
       =(pi/2) integral_0^tau a(x)^2
                    [b(Omega(x))+b(-Omega(x))]dx+O_b(h),
    I_h,T(e)=integral_0^T c_h(t)exp(iet)dt.             (24)

All errors are uniform over (1), tau and phi0. The proof is included to
check equality and crossing, rather than relying on an above-threshold
hypothesis in the parent statement.

Extend Omega to the real line by endpoint traces; its bounds and total
variation persist. Let A_tau equal a on [0,tau] and zero outside. Then

    ||A_tau||_infinity<=A, Var(A_tau)<=V_a+2A,
    ||A_tau(.+z)-A_tau||_1
                    <=min(2A tau_star,(V_a+2A)|z|).    (25)

The BV translation inequality follows by expressing a difference as the
derivative measure on a translated interval and using Fubini with its total
variation. It also bounds translated differences of the extended Omega,
even though Omega itself need not be integrable on the whole line.

Use cos(phi(t))cos(phi(s)) as half the sum of its difference and sum
phases. With u=t-s and x=h^2s, the difference-phase contribution is

    D_h,b=(1/2) integral_R C_b(u) integral_R
       A_tau(x+h^2u)A_tau(x)cos(Theta_h(x,u))dxdu,
    Theta_h(x,u)=integral_0^u Omega(x+h^2z)dz.         (26)

Finite-time Fubini and then (23) justify the integrals. Replacing the product
of amplitudes by A_tau(x)^2 costs at most C min(1,h^2|u|) after integration
in x, by (25). Its integral against |C_b(u)| is
O(h^2 log(2+h^-2)). For the phase, the BV translation bound gives

    integral_R |Theta_h(x,u)-u Omega(x)|dx
                                  <=h^2 V_Omega |u|^2/2.

The A_tau^2-weighted cosine error is consequently bounded by

    min(2A^2 tau_star, A^2 h^2 V_Omega u^2/2).

Integration against (23), splitting at |u|=h^-1, is O(h). Fourier inversion,
valid since b and C_b are integrable and b is continuous including at 2m,
then yields

    integral C_b(u)cos(u Omega(x))du
                            =pi[b(Omega(x))+b(-Omega(x))].

For the sum phase fix u and integrate s over the intersection of
0<=s<=T and 0<=s+u<=T. The amplitude A_h(s+u)A_h(s) has supremum A^2
and variation at most 2A V_a. The phase derivative is

    Omega(h^2(s+u))+Omega(h^2s)>=2omega0,

with variation at most 2V_Omega. Equation (8) uniformly bounds the inner
integral. Multiplication by h^2 and integration against |C_b(u)| makes
this part O(h^2). The initial phase cancels in (26) and changes the
two exponential components of the sum phase only by unit-modulus factors.
This proves (24).
No step in this argument requires Omega>2m. Since Omega>0 and b is
supported in [2m,infinity), b(-Omega)=0 in every application here.

## 8. Born norms and the separate energy mean

Set beta=PZ_hP_- and beta1=PK1_hP_-. In the scalar positive frame let
C be ordinary conjugation and J=Gamma C:PK->P_-K. Then J is linear,
unitary and energy intertwining. Direct field expansion gives
PB P_-=i(|u><Gamma w|-|w><Gamma u|), so beta1 J has kernel

    lambda Delta(p,q)I_h,T(E(p)+E(q)).

It follows that

    ||beta1||_HS^2=2h^2 integral r(e)|I_h,T(e)|^2de,
    ||E^(1/2)beta1||_HS^2=h^2 integral e r(e)|I_h,T(e)|^2de. (27)

The second equality symmetrizes the output energy E(p) against E(q).
The factor 1/2 in the exterior density cancels the resulting factor two
there, but it does not cancel it in the unweighted first equality. For
b=r or er, boundedness of b and temporal Plancherel give the uniform bound

    h^2 integral b(e)|I_h,T(e)|^2de
       <=2pi ||b||_infinity h^2 integral_0^T |c_h(t)|^2dt
       <=2pi ||b||_infinity A^2 tau_star.              (28)

Using q=1 in (18) and the difference-of-squares inequality therefore gives

    | ||E^(1/2)beta||_HS^2-||E^(1/2)beta1||_HS^2 |
                                                   <=C eta_h. (29)

Both weighted blocks are finite. Increasing bounded one-particle energy
cutoffs and finite rank sums in the CAR occupation identity justify the
full positive Fock energy identity (3) by monotone convergence. This uses
no cyclic permutation of an unbounded trace and no inference from state
norm convergence. Apply (24) to b=er in (27)--(29). The result is precisely
the mean assertion in (7), including its uniform error.

## 9. The exact graph and the complete energy law

Let A0=PZ_hP on PK. Equation (20) makes A0 invertible and
||A0^-1-I||<=C eta_h. The transformed annihilator of Y_h|0> is

    a(A0 xi)+a*(beta Gamma xi).

Changing variables to A0 xi defines the skew graph coordinate

    L=beta Gamma A0^-1 C, L^T=-L,
    ||L||<=C eta_h, ||L||_HS<=C,
    ||L-beta1 J||_HS<=C eta_h.                         (30)

Skewness follows from the vanishing CAR anticommutator of any two of
these annihilators. The estimates use (18), (20), (27)--(28) and
A0^-1-I; in particular beta's HS norm is bounded. No HS norm is assigned
to the identity on the infinite one-particle space.

The Gaussian overlap used next has a finite-exterior proof. For a finite
skew matrix L, set F_L=exp[(1/2)sum L_ij a_i*a_j*]|0>. Its coefficient
on an even subset S is Pf(L_S). Thus the mixed overlap is the sum of
overline(Pf(L_S))Pf(M_S). Expanding the block Pfaffian with diagonal
blocks L*,M and off-diagonal blocks -I,I gives that sum up to the common
sign fixed at zero. Squaring the block Pfaffian and eliminating blocks
gives

    <F_L,F_M>^2=det(I+L*M).

For ||L||||M||<1 the determinant is nonzero; continuity from zero fixes

    <F_L,F_M>=exp[(1/2)Tr log(I+L*M)].

Compress HS skew operators by finite-rank projections commuting with C.
They converge in HS norm; their products converge in trace norm. The
trace-log series is continuous on a common operator-norm ball smaller
than one, by telescoping the powers. The mixed-overlap formula therefore
makes the pair vectors Cauchy, with vacuum coefficient one and finite
nonzero norm. Bounded CAR operators pass their annihilation equations to
the limit. Conjugating with the actual Y_h proves uniqueness of the
common annihilation vacuum and identifies this normalized vector with
Y_h|0> up to phase. This constructs the state identity without a dynamical
finite-dimensional truncation.

Let R_s=exp(isE|PK) and L_s=R_s L R_s^T. On finite exterior products
exp(isH0) sends F_L to F_L_s; approximation passes this to the HS limit
even when the compressions do not commute with E. Consequently the exact
characteristic function has the continuous trace-log lift

    log chi_mu_h,tau(s)
      =(1/2)Tr log(I+L*L_s)-(1/2)Tr log(I+L*L).         (31)

This is the lift specified by its norm-convergent logarithm series, not
an arbitrary principal scalar logarithm. Since
||L*L_s||<=||L||^2 and ||L*L_s||_1<=||L||_HS^2, the total terms of degree
at least two are O(eta_h^2). Replacing L by beta1 J in the linear trace
costs O(eta_h) by HS Cauchy--Schwarz. With the kernel in section 8,

    log chi_mu_h,tau(s)
      =h^2 integral r(e)(exp(ise)-1)|I_h,T(e)|^2de
                                                   +O_s(eta_h). (32)

Equation (24) for b(e)=r(e)(exp(ise)-1) gives the exponent in (5), with
error O_s(h)+O_s(eta_h)=O_s(eta_h). Its real part and the real part of
the exact lift are nonpositive. Integrating the exponential derivative
along the joining segment bounds the characteristic-function difference
by the exponent difference. This proves the first assertion in (7).

## 10. Uniform W1, including resource-bounded varying paths

For fixed profiles and tau, (5) is a characteristic function continuous
at zero. The first part of (7) gives weak convergence; section 8 gives
the separate convergence of nonnegative means. The first-energy tail
step is explicit: whenever X_n converge weakly to X with converging
finite nonnegative means,

    E[(X_n-R)_+]=E[X_n]-E[min(X_n,R)]
                         ->E[X]-E[min(X,R)].

The right side tends to zero as R grows, and
x 1_(x>2R)<=2(x-R)_+. Treating the finite initial part of the sequence
separately gives uniform integrability of first moments. Truncation of
Lipschitz tests proves W1 convergence.

For resource-uniform comparison suppose instead that a sequence of allowed
profiles, horizons and h_n->0 violates the last assertion in (7). Their
Lambda_n have bounded total mass and common compact support in [omega0,W]
(they vanish below or at 2m). Extract a weakly convergent finite-measure
subsequence with limit Lambda. Continuity of exp(ise)-1 and of e on this
compact interval gives convergence of both the compound-Poisson exponents
and their means. The preceding tail argument gives W1(Pi_n,CP(Lambda))->0.
The uniform characteristic and mean bounds in (7) give the same weak and
first-moment convergence for the exact mu_n, hence its W1 convergence to
CP(Lambda). The triangle inequality contradicts the assumed violation.
This proves the uniform comparison without an asserted W1 rate.

## 11. Analytic stress tests and failed shortcuts

These are author analytic checks, not a second reviewer or a numerical run.

**Exact threshold dwell.** Take Omega=2m and constant amplitude a0, whenever
that path is in (1). Formula (22) makes r(2m)=0, hence Lambda_tau=0.
Directly, writing Q_T(z)=integral_0^T exp(izt)dt gives the two cosine
components at e-2m and e+2m. Since |Q_T(z)|<=min(T,2/|z|) and
er(e)=O(e-2m) at threshold,

    h^2 integral er(e)|I_h,T(e)|^2de
                                  <=C h^2 log(2+T).   (33)

Indeed the near-threshold resonant integral is bounded by a constant times
integral_0^1 x min(T^2,4/x^2)dx=O(log(2+T)); the nonresonant term is
bounded, and Cauchy--Schwarz controls the cross term. Together with (18),
this gives exact energy O(eta_h^2)=O(h log(2+h^-2)) on the kinetic window.
Thus a plateau at threshold is not treated as a positive pair rate. It is
also not excluded from the operator estimates. For fixed 0<Omega<2m the
direct Born mean is O(h^2); (7) again has zero limiting measure. These
are statements on this time scale, not claims about multiphoton response
on other scales.

**A slot pair with nonzero threshold slope.** Let b be a nonzero nonnegative
even real compact smooth bump, f=(b,0), g=(0,b), and let Bhat=bhat.
Both vector integrals are nonzero. Direct substitution into (4) gives

    Delta(p,q)=2 sin((theta(p)-theta(q))/2)Bhat(p)Bhat(q).

Writing Bhat(0)=b0>0 and using (21) gives

    r(2m+x)=(2pi b0^4/v^2)x+O(x^2), x down to 0.     (34)

To check the coefficient, Delta=(v/m)b0^2(p-q)+O((|p|+|q|)^2),
p'(0)=sqrt(2m)/v, and the angular integral of (cos t-sin t)^2 is 2pi.
This verifies a generally nonzero one-sided density slope while the
operator threshold cross term is exactly zero. Those facts are compatible:
one refers to the first nonzero momentum variation, the other to the
constant matrix at p=q=0. No improvement of (23) to an integrable full
first correlation-time moment is justified for this example.

**A separate finite-block secular check.** Suppose a and Omega are constant
on a fixed finite macroscopic partition, with arbitrary positive frequencies
omega_j in the allowed range, including those below, at and above 2m.
On each physical interval phi_h is affine, with its continuity-determined
phase offset. The difference-phase double integral has triangular factor
T_j-|u|. Replacing it by T_j and extending u to the line costs
O(log(2+T_j)) by (23); Fourier inversion gives
(pi/2)T_j[b(omega_j)+b(-omega_j)]. The sum phase costs O(1/omega0).
For two different intervals, integration of |C_b(t-s)| after measuring
distances from their facing endpoints is bounded by

    C integral_0^L integral_0^K (1+x+y+d)^(-2)dxdy
                                             <=C log(2+T).

This holds also for adjacent intervals (d=0). The finite cross sum vanishes
after multiplication by h^2. Consequently the final jump measure is

    sum_j (pi/2)a_j^2 r(omega_j)|J_j intersect [0,tau]| delta_omega_j.

This independently checks the secular coefficient and the treatment of a
crossing by a discontinuous schedule. It does not replace the BV proof:
a fixed approximation error delta in Omega can accumulate a phase error
of order delta h^-2, and a growing number of blocks needs extra control.
Equation (26)'s integrated BV estimate handles the full class directly.

**Assumption mutations caught by the threshold identity.** If the reality
hypothesis is dropped, F0=diag(1,i) would give F0 M F0*=2 sigma_x,
which does not commute with D(0)=-m sigma_y and has a nonzero opposite-band
block. The determinant argument is then inapplicable because F0* is not
F0^T. If the alternating M is replaced by sigma_z with F0=I, the cross
block is likewise nonzero. These explicit algebraic defects refute the
corresponding overgeneralized cancellation lemma. They are outside the
theorem and do not prove that every such enlarged model lacks a kinetic law.

**Old scalar bounds fail at equality.** At Omega=2m, an uncontracted
opposite-band leading term in (13) would have zero phase derivative.
Its absolute convolution integral integral_0^r q0(r-z)q0(z)dz approaches
pi rather than decaying as q0(r). Likewise a threshold forcing term with
a nonvanishing coefficient would face the unbounded inverse Jacobian,
and a near-near resonant time primitive need not be uniformly bounded.
The old strict-gap estimates cannot simply substitute gap=0. The present
proof removes those terms by (11), improves the crossed-input density,
and decomposes the full Born operator. These are failed proof estimates,
not counterexamples to the present theorem.

Degenerate controls, a=0, or tau=0 yield the expected zero law. Changing the
sign of a on parts of the schedule changes the exact coherent evolution,
but the limiting measure depends on a^2. No positive rate is asserted for
every nonzero slot pair or every frequency above threshold. Arbitrarily
many nonmonotone crossings, threshold level sets of positive measure,
BV jumps and h-dependent paths are covered within the fixed resources;
independent resets of the phase at a growing set of times are not the
continuously integrated phase in (2).

## 12. Remaining consequences and the exact strict-gap inventory

The three strict-gap uses in the allowed general-slot chirp arguments are
exhausted as follows. The source names below refer to their exact frozen
bytes in section 13.

| Old proof use | Replacement established here |
|---|---|
| Causal square: root H11--H13; independent (15)--(17) | A_s M A_-s=0 removes the derivatives which could vanish at 2m; the surviving derivative is bounded by omega0 in (13)--(14). |
| Full-input threshold: root H14--H15; independent (18)--(20) | Crossed-input coefficients vanish at zero momentum and have bounded energy density; same-input threshold is separated by omega0-b in (15)--(17). |
| Near-near Born bound: root H16/H6; independent (23) and its preceding cutoff argument | The exact threshold-value decomposition (19), the third cancellation in (11), and bounded synthesis for H_s prove (20). |
| Secular sum phase: root H20 and following; independent (30) | Its derivative only needs 2omega0>0; (24)--(26) include equality and crossing. |
| Secular evaluation at the local frequency | The extended b is continuous at 2m, so Fourier inversion applies there; r(2m)=0. |
| Graph and trace log | Invertibility and small graph norm follow from the full operator estimate; HS bounds and exterior normalization are separately established in (27)--(32). |
| Energy mean and W1 | Weighted remainder (18), the positive energy identity, (27)--(29), and section 10 give separate tail control. |
| Vacuum gap and finite-mode consequences | Their gap is the fixed free mass m, not a lower separation of the carrier from 2m. |

For clarity, the operator consequences survive with d_h=C eta_h. CAR
telescoping gives error at most n d_h product_j||k_j|| for a word of degree
n in real slots. Since 0<=N_h<=d_h^2 I, any rank-r positive-band projection
has reduced-state vacuum trace distance at most
2 min(1,sqrt(r)d_h). Its nonvacuum probability is bounded by its number
expectation r d_h^2. These statements are for finite rank; a bounded
continuum energy band need not have finite rank.

For fixed profiles and tau, the free gap m isolates the vacuum energy.
Equation (7) yields vacuum probability exp(-Lambda_tau(R)) in the limit,
and purity yields global vacuum trace distance
2 sqrt(1-exp(-Lambda_tau(R))). Fixed compact Fock operators have expectation
limit exp(-Lambda_tau(R))<0|K|0>: finite creation vectors with at least one
particle have vanishing matrix amplitudes by the uniform annihilation bound
||a(k)Y_h|0>||<=d_h||k||, and finite-rank approximation passes to compact K.
Common free rotation gives the corresponding full-state statements.
No spatial local-algebra norm limit, current law or multi-time process
follows from these marginal and operator results.

The accepted chirp notes' actual-cell conclusion also retains its exact
conditional form. If a common real energy embedding, H0, vacuum and
bounded centered controls V_ell are separately supplied with

    ||V_ell-V||<=d0 epsilon_ell,
    ||[H0,V_ell-V]||<=d1 epsilon_ell,
    ||[H0,V_ell]||,||[H0,V]||<=k1,
    ||B_ell-B||<=dB epsilon_ell,

as actual bounded commutator forms, let
D_h(t)=integral_0^t |lambda c_h(s)|ds<=A tau_star/h. Bounded-perturbation
Duhamel gives state trace distance at most 2d0 epsilon_ell D_h(t) and
one-particle distance at most dB epsilon_ell D_h(t). Regularize H0 by
H_R=H0(1+H0/R)^(-1). The commutator identity
[H_R,V]=Q_R[H0,V]Q_R, Q_R=(1+H0/R)^(-1), gives the exact first-energy
work identity after strong and monotone limits. Subtract the two work
identities and use the state bound to obtain

    |E_ell(t)-E_h(t)|
        <=epsilon_ell[d1 D_h(t)+k1 d0 D_h(t)^2].

Here integral D_h'(s)D_h(s)ds=D_h(t)^2/2. No derivative of the scalar
drive occurs, so BV jumps give no instantaneous H0-energy kick.
The sufficient epsilon_ell=o(h^2) transfers the law, mean and W1;
epsilon_ell=o(h) alone gives the unweighted state/law comparison. This
is conditional transfer only: no new calibration, embedding, cell
construction or stronger weighted cell-operator bound is proved.

## 13. Source identities, independence and remaining verification

The neutral PLAN.md was frozen before reading the target science, with
SHA-256 09ae83c6a4e0c38439c279a4619b22f9c1105197ce561174612239530bab1dd7.
The exact primary sources, all read completely, are:

| Source | Lines | SHA-256 |
|---|---:|---|
| CHIRPED_KINETIC_LAW_ROOT_PROBE_V2.md | 515 | 87011c662344ed684a7251f5067bb8193d156837a50a23e71fa29ccff38e92f6 |
| CHIRPED_KINETIC_LAW_INDEPENDENT.md | 850 | 279a96bc07b495a59b829cac70586ae8e115f0ddefca0d405bb15f0a7de6e95c |
| GENERAL_KINETIC_LAW_ROOT_PROBE.md | 470 | 6bbcf624e47e4d91f2a6fbd8982698d788923bba63612f90d5930d04920ca49b |
| WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT_V2.md | 859 | c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b |

The 16-line CHIRPED_KINETIC_LAW_ROOT_ACCEPTANCE.json was also read, SHA-256
9918f46bbf900e35241aae0ad51f92ba6164df21081ec6f75f97ff8576cc895c.
It records ordinary conditional analytic acceptance, not retained audit or
permission for this worker to publish. The four source bodies give 2694
lines of primary science coverage. Their references to other papers were
not treated as automatically read or accepted premises. The present model,
analytic tools and graph proof are stated above; the optional cell
corollary expressly assumes its missing construction.

The new load-bearing mathematics is (10)--(11), its causal and both-input
applications (13)--(17), and the exact threshold-value Born decomposition
(19)--(20). The determinant and band-frame calculations check the threshold
identity by different algebraic routes. Section 11 tests its necessary
hypotheses with explicit invalid mutations and checks threshold normalization
and piecewise-constant secular behavior analytically. These are author
checks, not model-diverse or external independent review.

The parent target derivation, all THRESHOLD_CROSSING_CHIRP_ROOT* contents,
threshold_crossing_chirp_root_probe/, threshold_crossing_chirp_lean/,
threshold_crossing_chirp_independent/, other new target derivations and
root opportunity/current-checkpoint additions were excluded. A preliminary
filename inventory exposed paths of duplicate allowed source names under
excluded directories, but no excluded source contents; its truncated output
does not establish scientific coverage. The failed previous worker's partial
findings were not inherited. This worker shares the allowed parent papers,
supplied model, task framing and inherited selected model family and effort.
It is a separate context with no claimed model-family diversity.

No scientific numerical calculation, finite-volume test, Lean build or
formal proof checker was run. Hashes and file operations are identity
bookkeeping only. No subagent, new physical axiom, audit verdict, editable
prompt change, repository source edit, commit, push, PR or other-chat message
was performed by this worker. A read-only Git show retrieved the governing
AGENTS instruction pointer target; no Git state was changed. The parent
owns freshness of the campaign's broader repository science and publication
decisions. No broad novelty search or complete framework-premise certification
outside this bounded source packet is claimed.

The author reports a complete conditional proof of (6)--(7), with the
source-bound cold check and exact final freeze recorded beside this file.
Focused independent mathematical assessment remains required before
substantial downstream reuse. In particular it should inspect all three
cancellations, the non-band auxiliary columns in (19), the full-input signs,
the weighted domain step, and the graph/mean normalizations. Formal retained
status remains exclusively with the later independent audit path. The proof
does not resolve physical selection of the model, removal of omega0>0, a
massless limit, growing resources, optimal rates, or a multi-time energy law.

## Publication source and verification boundary

The full accepted root and independent cores remain byte for byte unchanged.
PUBLICATION_EDITS.json records all five source pieces, exact byte/line maps,
complete three-context-line raw diffs and the wrapper changes. No mathematical
body edit was made. The standalone body claim-type line is explicit.

The packet is .claude/science/physics-loops/toe-threshold-crossing-chirp-20261013.
Its HANDOFF, REVIEW_HISTORY and CONFORMANCE expose all twelve handoff topics.
SOURCE_REVIEW_STATUS preserves the ordinary analytic/source acceptances and
their limits. The new publication wrappers remain subject to root's exact
review and acceptance. No retained verdict is supplied by this source package.

EVIDENCE_MAP archives the entire 110-file accepted assembly and its selected
original aliases. The accepted seal has 104 direct records; six additional
files are separately and exactly bound, including four nested freeze/log
files already bound by its frozen SOURCE_SELECTION. This records the actual
scope without changing any frozen byte. Both Lean attempts remain finite
algebra history only. The archive is not a recursive audit or whole toolchain.

The declared identity tool checks source bytes, exact reconstruction, parent
bindings and scoped archive closure. It performs zero mathematical predicates.
Its resolution statements report scientific nonexecution and supply no no-go
packet PASS. The proposed tool, cache, graph and prepare/verify programs were
not executed by the source preparer. Deterministic source generation, hashing,
diffing, AST parsing and source-only reconstruction have their own records.

Root owns the separate prepare/verify execution, exact staging, graph delta
of one node and three edges, regular PR publication and attachment. The driver
requires separate acceptance of the exact source freeze and program; it does
not stage, commit or publish. A later combined current-main gate and formal
retained audit remain separate. No physical axiom or editable prompt changed.


Review-loop integration note: current main 3ba0669dba5911b76939c62f452f1fba3ec277a4 plus this kinetic-energy batch supplies the reviewed live dependencies. Original proof bodies and archives are unchanged. Live parent hashes and consumed-core coordinates are refreshed, with original bindings preserved. Historical pending and review labels remain provenance, not audit authority.
