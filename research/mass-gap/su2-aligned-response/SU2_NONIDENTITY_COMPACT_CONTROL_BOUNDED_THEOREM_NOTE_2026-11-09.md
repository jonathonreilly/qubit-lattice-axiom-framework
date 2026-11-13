# Compact control of the SU(2) marginal at small nonidentity backgrounds

Status: proposed_retained

This note extends the actual seven-edge two-plaquette marginal from identity
terminal output to a fixed small neighborhood of terminal backgrounds. It
constructs its unique normalized Haar-density mode, proves compact energy
control around that mode, and transports the source-complete connected
expansion. The supplied finite two-hidden-layer SU(2) model and its existing
identity coercivity are premises. This is not a Yang-Mills mass-gap theorem.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "compact control for nonidentity terminal backgrounds in the actual seven-edge marginal"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Identify the conditional geometries and rough terminal components of a third exact transition, then prove the required inherited-law estimates."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Uniform finite-model compact estimates on a specified small-background class, conditional on the supplied model and identity coercivity; connected consequences use sufficiently large u."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## Model and parameter domain

Fix odd L>=3, kappa>0, m>=3, fine torus side L^2 m, Wilson beta=u and
both kernel strengths kappa u. Let J be the seven terminal edges of two
distinct elementary plaquettes sharing one edge, O=E2\J. At zero sources,

    rho_V=Q_J(V)^(-1) q_u(U0) K0(U1|U0)
                          product_(c in O) k1,c(V_c|U1) dU0 dU1,
    epsilon=max_(c in O) chord(V_c,I)<=epsilon_*.

The positive constant epsilon_* depends only on L,kappa, not on u or
volume. Every K0 and surviving terminal numerator and radial normalizer
remains. The entire normalized J kernels have been integrated out. The
terminal-root forest admits arbitrary permitted internal trees and leaves
product probability Haar on all fine non-tree and intermediate coordinates
a. The root-fixed orbit remains independent product Haar at zero sources,
because its transformations fix the terminal endpoints even when V is
nonidentity. Write nu_V for the quotient law.

## Compact mode and regional control

For u>=1 define the complete normalized kernel energy

    Phi_u(v,M)=kappa(1-<v,M>)
                   +[log Z(kappa u |M|)-log Z(kappa u)]/u,
    Z(t)=integral_SU(2) exp(t w(Q))dQ.

Sum these over actual surviving kernels together with fine Wilson factors
to form E_u(a;V). There is a unique global Haar-density mode a*=a*(V,u),
with sup_e |log a*_e|<=C epsilon, such that for EVERY compact q,

    c sum_e chord(q_e,I)^2
      <= E_u(a*q;V)-E_u(a*;V)
      <= C sum_e chord(q_e,I)^2.                              (1)

All constants are uniform in volume, pair placement/orientation, permitted
trees and u>=1. The exact density ratio to its mode is the exponential of
minus u times this increment. This includes vanishing means and antipodal
relative links. It does not assert uniqueness of every stationary point.

The [mode proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/nonidentity-marginal-compact-mode.md)
also constructs unique regional Haar modes when the hidden collar is small
relative to a*. Their difference from the global mode decays exponentially
with distance from the collar. A terminal perturbation on a set S changes
the global mode by at most C times its sup size times exp(-alpha distance
to S). These are background-dependent modes, not asserted coordinate means.

The [regional proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/nonidentity-centered-regional-estimates.md)
subtracts each local factor's linear right-tangent term using Im(q_e).
Global stationarity cancels their sum exactly. In a whole-factor regional
selection the remaining compensation depends only on the exterior and
cancels from the actual conditional ratio. With T_A the sum of 1-w(q_e)
owned by A, the compensated selected energy obeys

    c' T_A-K T_collar <= Ebar_A <= K(T_A+T_collar)              (2)

under arbitrary compact quotient exterior. Individual compensated factors
need not be nonnegative. The exact Haar-cap/profile argument gives
E chord(a_e,a*_e)^p<=C_p u^(-p/2) for every fixed p>0. It holds on the full
compact law for all u>=1 and on a centered shrinking product chart for
sufficiently large u. No exact mean-zero symmetry is used.

## Compact connected expansion and source response

Take the chart q_e=exp(i x_e.sigma) with every scalar |x_e,k|<rho,
rho=u^(-1/2)log(2+u)^A and fixed A>5/2. All coordinates, selectors and
the Gaussian reference are frozen at the base V,u,a*. For bounded local
quotient insertions X_i, use normalized source parameters with fixed small
complex radii and retain every complete source reader. The
[composition proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/nonidentity-compact-connected-response.md)
proves, for u>=u_0 uniformly over the background class,

    log(Z_compact/Z_chart)=sum_Y Psi_Y,
    sup_x sum_(Y contains x) exp(beta_f |Y|/2) sup|Psi_Y|
                              <=C exp[-c log(2+u)^(2A)].      (3)

Here beta_f>0 is a fixed spatial weight, distinct from Wilson beta=u.
Each Y is connected, contains a compact label, and contains every source
reader differentiated in that coefficient. All marked regional denominators
and the marked chart law remain. The
[Gaussian producer](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/nonidentity-frozen-gaussian-producers.md)
keeps E_u(a*;V), actual surviving kernel counts, both physical normalizers,
probability-Haar constants and the Gaussian determinant in its exact common
prefactor. No lower bound on full-volume chart probability is assumed.

For distinct c,d in O, let A_c=kappa u <dot V_c,M1,c> and similarly for d.
Let F,G be bounded local C2 quotient singlets, with fixed norm and complete
reader size/diameter bounds. For tau_4 the minimal axial cell tree meeting
their four reader sets, the full compact response obeys

    |kappa4_nuV(F,G,A_c,A_d)|
      <=C |dot V_c||dot V_d| (epsilon^2+u^(-1)) exp(-mu tau_4). (4)

For unit tangents and 0<=eta<mu, the sum over c!=d of exp(eta tau_4)
times the left side is bounded by
C_eta(epsilon^2+u^(-1)) exp[-b_eta d1(S_F,S_G)]. At epsilon=0 this
recovers the identity u^(-1) estimate. The epsilon^2 allowance follows
from the proved centered moments; no optimality or impossibility of a
stronger estimate is claimed.

For original local C2 singlet sources, integrate their joint orbit factor
E_h exp(sF+tG), and set f=E_h F, g=E_h G, C_FG=E_h(FG)-fg. Exactly,

    kappa4_rhoV(F,G,A_c,A_d)
      =kappa4_nuV(f,g,A_c,A_d)+kappa3_nuV(C_FG,A_c,A_d).        (5)

The second term vanishes for disjoint orbit-reader sets H_F,H_G; otherwise
it is retained with the proved upper allowance C(1+epsilon sqrt(u)). With
the endpoint-extended bounded source regions T_F,T_G, the resulting bound is

    C |dot V_c||dot V_d|
      [epsilon^2+u^(-1)+(1+epsilon sqrt(u)) 1_(H_F intersects H_G)]
                                 exp[-mu' tau_4(T_F,T_G,S_c,S_d)]. (6)

It has the corresponding weighted pair sum. The extra allowance is not
asserted sharp or nonzero; it avoids dropping conditional orbit covariance
or silently assuming an additional cumulant cancellation.

If ALL terminal outputs, including those in J, obey the small-background
condition, restore the seven kernels to handle the fully pinned numerator
law pi_V. Its identity reference gap follows by adding the seven nonnegative
leading energies; the same finite-template proof applies to its own mode.
The exact two-plaquette conditional density p_J=N_V/Q_J(V_O) satisfies

    D_c D_d partial_s partial_t log p_J
       =kappa4_piV(F,G,A_c,A_d)
                   -1_(c,d in O) kappa4_rhoV(F,G,A_c,A_d).     (7)

Equations (4) or (6) bound both terms separately, with epsilon taken over
all terminal outputs. No normalizer subtraction is erased. These are
distinct-link derivatives at zero sources; fixed-score generating functions
reproduce that coefficient without differentiating the chosen chart.

## Evidence and next obligation

The [Luna source check](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/nonidentity-compact-prior-art-20261109.md)
preceded proof delegation. Its
[current-main and open-PR addendum](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/nonidentity-main-search-addendum-20261109.md)
records the wider bounded search. Existing local chart control already
allowed small nonidentity outputs; the new step is control of the compact
complement and its exact connected contribution. No external background-field
theorem was imported without checking its hypotheses.

The new proof check is recorded in the pack's
[review history](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/REVIEW_HISTORY.md),
with exact final source identities and the limits of inherited-premise
coverage. Fable 5.2 approach advice is separately scoped. Author and
fresh-context research checks confer no formal retained status; independent
audit remains required. Earlier primary notes remain frozen milestones.

The next missing bridge is the actual conditional geometry/background class
generated by a third exact transition. Everywhere-small terminal fields
have not been shown sufficient: rough terminal components and their
normalization/reader costs need their own estimates. Inherited-action
closure, unbounded blocking depth, physical-scale limits, continuum QFT
construction and a positive physical Yang-Mills gap remain open. The mode
and posterior Hessian here are auxiliary finite-model quantities.
