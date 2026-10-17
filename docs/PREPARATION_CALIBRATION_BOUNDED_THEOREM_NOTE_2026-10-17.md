---
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: real_control_autonomous_output_bounded_theorem_note_2026-10-17
target_blocker_text: "Exact preparation-channel amplitudes and pure auxiliary delivery in the supplied five-unit real-control construction."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review and package the bounded setup-calibration and correlated-seed implication above the unchanged PR9667 apparatus."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Finite-box complete trace bound under explicit preparation and unchanged runtime premises, including correlated auxiliary delivery."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---
# Preparation calibration and correlated seed delivery for a real two-rail apparatus

Status: proposed_retained
Claim type: bounded_theorem

Primary runner: [local exact calibration corroboration](../scripts/preparation_calibration_2026_10_17.py).

## Target theorem

For the exact two-rail runtime and five-unit setup of the
[real-control complete-output theorem](REAL_CONTROL_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md),
multiplying each of its fourteen entire positive preparation blocks by a
separately chosen constant 1+xi_a, |xi_a|<=eta, 0<=eta<=10^-5, and supplying any joint
old/reference/auxiliary input with full auxiliary seed deficiency at most
0<=epsilon<=10^-9, gives complete finite unhalved trace distance <.00996404
from the specified ideal output on every release-time t in [T,2T], where
T=kappa^-2, M=ceil(50T), kappa in [10^-12,10^-8].

The ideal output uses the actual old/reference marginal of the delivered state.
It includes every rail, emitter, source and old qubit and any passive reference,
the original normalized infinite comparison waveform, nominal common phase,
fixed calibration residual, and total old age t+5. The finite apparatus is
chosen before setup. This theorem concerns the PR9667 apparatus and setup;
it does not apply to the later autonomous endpoint-product-seed apparatus of
PR9668, whose graph and preparation contract differ.

The corrected source result and selective analytical review are root-qualified
for provisional composition. This source proposal assigns no audit verdict or
retained authority. No new scientific execution is asserted by this draft.

## Imports and obligation graph

| Input | Role | Provenance | Open physical bridge |
|---|---|---|---|
| Exact real positive full-qubit H_R,M, coefficients, selected NN edges and source interactions | Unchanged dynamics and output embedding | Linked real-control note's preserved realifier body at c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018 | Native Hamiltonian/coefficients and time/energy identification |
| Nominal fourteen local channels and five-unit C1 schedule | Defines the calibration family | Same note's preserved preparation at 57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c | External controller, timing and calibration supplier |
| Nominal supported ramp bound and exact runtime resonance interface | Baseline complete-output estimate | Same preparation body and its named conditional dependencies | No recertification of ancestral scattering or physical Record map |
| Joint full-seed probability >=1-epsilon | Delivery quality | Explicit supplied condition below, not a thermal result | Pure-state/correlated-delivery manufacture remains supplied |
| Fourteen constant whole-block errors <=eta | Allowed setup variation | Explicit mathematical model below | No independent Pauli, timing or persistent runtime error model |

The proof graph is nominal setup/runtime implication plus full-space Duhamel
-> complete pure-seed operator bound -> two-isometry trace bound; separately,
purification and monotonicity -> correlated-seed trace bound; then common
unitary invariance and triangle inequality -> the target theorem. Positive
block scaling and profile variation separately control strengths, slew and
modeled work. The rank-one seed lemma is proved here, so the older single-rail
Gibbs construction is not a dependency. The strongest missing physical bridge
is provision/identification of the exact runtime and controlled preparation;
no such bridge is asserted by this conditional implication. Registered units,
kinetic normalization and realized-state specialization do not select these
coefficients, controls or joint seed probabilities. No new axiom is proposed.

## Exact contract and nominal preparation

Use exactly the realifier c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018
and preparation 57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c,
qualified together by root acceptance 98315ba16275ceb44dd3fcf32d655d1e92d42da7c7678600327be89d9d1ba852.
The same literal HR,M, exact static coefficients, kappa in[1e-12,1e-8],
M=ceil(50/kappa^2), T=kappa^-2, old K and W are retained. The fourteen
positive preparation terms act on the same eight sites and no old/source
qubits. All statements below use the same fixed apparatus before and after
setup. Time t denotes time after the five-unit setup.

Write the nominal added control as

    A(s)=u(s) sum_{a=1}^9 R_a
       +w1(s)[Q_e0,m(+1)+n_e1]
       +w2(s)[Q_m,e1(-1)+n_e0] +w3(s)n_e1.

These are fourteen separately counted term channels; the last n_e1 channel
has a different time window from the first pulse spectator. The fixed R_a
are the eight positive edge complements and the positive pin from the
parent. Their norm sum is

    Aiso=4J+4kappa(1+c+s)+E0-kappa < 1/7.

The parent supplies nonnegative C1 profiles on[0,5], all zero at endpoints,
with integral u=4, integral w1=pi/4, integral w2=integral w3=pi/2. The full
Q(+1) and Q(-1) norms are2, and each occupation norm is1.

For each of the fourteen channels independently, multiply its entire fixed
positive local block by a constant 1+xi_a with |xi_a|<=eta, 0<=eta<1. Keep its nominal
profile, support and internal coefficient ratios. This is a box of static
amplitude calibrations of the preparation channels. It is not a box of
independent Pauli coefficients or arbitrary errors in the runtime Hamiltonian.
In particular an entire Q/complement scales together, preserving positivity.


### Fixed operators, channels and nominal comparison

Use n=(I-Z)/2, a=|0><1|, the literal K=2I+Z1 Z2 and
W=[(9+12i)I+(-16+12i)X1 X2]/25. Thus [W,K]=0; no commutation of the
interacting runtime with K is assumed. The exact parent coefficients include
J=.030021107107032, nu=1.459892813020969 and q0=4.510351185997098.
Set k0=2 arctan(1/q0), E(k)=2J(1-cos k), E0=E(k0), c=cos(2k0),
s=sin(2k0), d_c=1+c+s, L=12 and sigma=10^-6. Every other runtime coefficient,
positive block and full two-rail embedding is exactly the linked parent's.

For a real h,

    Q_uv(h)=|h|(n_u+n_v)+h(a_u^dagger a_v+a_v^dagger a_u)

has full two-qubit spectrum {0,0,2|h|,2|h|}. Its complement
2|h|I_uv-Q_uv(h) is likewise positive with norm 2|h|. No identity term is
dropped from norms, errors, phases or work. On the six emitter edges the
signed runtime hoppings are

    e0--c12,0:+kappa; e1--c12,1:+kappa;
    e0--c14,0:-kappa c; e1--c14,1:-kappa c;
    e1--c14,0:+kappa s; e0--c14,1:-kappa s.

Let m=c14,0. Eight R_a are complements on these six edges and the two -J
clock edges m--c13,0, m--c15,0. The ninth is (E0-kappa)n_m. These are
positive throughout the stated coupling interval. The eight touched sites
are e0=(8,2,1), e1=(9,3,1), m=(9,2,1), c12,0=(8,1,1), c12,1=(9,3,0),
c14,1=(8,3,1), c13,0=(9,1,1), c15,0=(10,2,1); all used edges are ordinary
nearest neighbors. M>=16 holds for every permitted device.

The nominal unit ramp is u_up(x)=3x^2-2x^3 and its reverse is 1-u_up(x).
The isolation profile u is the upward ramp on [0,1], one on [1,4], and
the downward ramp on [4,5]. With q(x)=30x^2(1-x)^2, w1=(pi/4)q(s-1)
on [1,2], w2=(pi/2)q(s-2) on [2,3], and w3=(pi/2)q(s-3) on [3,4];
each is zero elsewhere. Here s in the profile argument is setup time, not
sin(2k0). Values and first derivatives join continuously. The profile has
integral one, max q=15/8 and max |q'|=10sqrt(3)/3; ramp slope is <=3/2.

E_e0 inserts the full auxiliary seed with e0 occupied and every other
emitter/clock/source qubit blank. E_chi=(E_e0-i E_e1)/sqrt(2). The parent
proves the supported nominal preparation inequality

    ||U0 E_e0-exp(-iPhi)E_chi exp(-5iK)||<=sqrt(2)kappa,
    cR=2nu+2kappa d_c, cseed=E0+cR,
    r=4J+3kappa d_c, Phi=5cseed+4r+3pi/4.

Its local core cancellation and exit Gram 2I justify this bound, rather than
a full-space small-norm assumption on the extensive runtime. The qualified
runtime bound from E_chi is <.004832 on [T,2T] and <.003832 on the infinite
apparatus for t>=T. B_t^R denotes its fixed actual common normalized output
profile in rail state (|0>-i|1>)/sqrt(2), empty emitters and source vacuum.
The same zeta=-exp(-4ik0)alpha uses the exact bare site-one reflection alpha
at old energy 1 and parity -1. The positive central ceiling 1.76e-13 remains
charged by the inherited interface. The finite comparison uses the embedded
infinite profile, not a newly truncated and renormalized packet.

## 1. Uniform control-error budget

Let A_xi be this perturbed control and U_xi the actual five-unit evolution
under HR,M+A_xi. With U_0 the nominal preparation, full-space unitary
Duhamel and the triangle inequality give

    ||U_xi-U_0|| <= integral_0^5 ||A_xi(s)-A(s)|| ds
       <= eta [4Aiso+3pi/4+3pi/2+pi/2]
       = eta [4Aiso+11pi/4] <= 10 eta.            (1)

Explicitly, differentiating U_xi(5,s)U0(s,0) yields

    U_xi(5,0)-U0(5,0)
      =-i integral_0^5 U_xi(5,s)[A_xi(s)-A(s)]U0(s,0) ds.

The unchanged full base Hamiltonian cancels from this identity. At eta=0
both sides of the calibration bound are zero, so its final inequality is
non-strict; the subsequent output ceilings have independent strict slack.

The coefficient3 counts a two-site block of norm2 and its spectator of norm1.
Using pi<22/7, the bracket is less than129/14<10. This estimate is on the
full finite qubit space, independent of M, and remains valid after tensoring
any passive reference. It does not assume that the actual perturbed state
stays in the ideal isolated core. Global scalar errors from the local
complements are included in the full operator difference.

Combining (1) with the nominal supported preparation estimate gives

    ||U_xi E_e0 - exp(-iPhi) E_chi exp(-5iK)||
       <= sqrt(2)kappa + eta[4Aiso+11pi/4].       (2)

Phi=5cseed+4r+3pi/4 is the nominal comparison phase. This is a bound to
that specified phase, not an assertion that the perturbed evolution has
exactly the same scalar action or exactly the same prepared head state.

Propagate the entire difference under the unchanged HR,M runtime and use
the qualified complete resonance interface. Uniformly for t in[T,2T],

    ||exp(-itHR,M) U_xi E_e0
      -zeta exp[-i(Phi+cR*t)] B_t^R exp[-i(t+5)K]W||
       < .00483202 + 10 eta.                    (3)

Every old/reference/source/emitter/rail output, the actual common waveform,
fixed central residual and old aging remain in the same comparator. The
nominal finite window and enormous apparatus size are unchanged. There is
no setup-time factor multiplying the later huge runtime t in (1): the
new perturbation vanishes after setup. Static runtime calibration errors,
if present, would require a different analysis and are not included here.

For eta=10^-5 the complete finite operator bound is <.00493202. Thus the
unhalved trace distance for the stipulated pure seed and every old/reference
input is <.00986404, using the two-isometry expansion. On the infinite
apparatus the same addition applies to the .00383202 bound for all t>=T;
this does not create an all-future finite-device theorem.

## 2. Supplied imperfect seed with arbitrary old/reference correlations

For 0<=epsilon<=1, suppose the actual joint input omega_DRA has actual
old/reference marginal rho_DR and apparatus seed probability at least1-epsilon:

    Tr[(I_DR tensor |e0><e0|)omega_DRA] >= 1-epsilon.

Here |e0> denotes the entire required auxiliary product seed: both sources
and clocks blank, e0 occupied, e1 blank. The general rank-one marginal bound is rederived below; the earlier
product-preparation source is historical provenance only, and its single-rail
Gibbs apparatus is not imported:

    ||omega_DRA-rho_DR tensor |e0><e0|||_1
      <= g(epsilon)
      := epsilon+sqrt[epsilon(4-3epsilon)] <=3sqrt(epsilon). (4)

Let d=1-Tr[(I_DR tensor |e0><e0|)omega_DRA] be the actual deficiency,
so 0<=d<=epsilon. Projecting onto the seed gives a subnormalized state whose
trace distance from omega is at most sqrt[d(4-3d)]. To see this, purify omega
and split the purification into its orthogonal seed and complement parts.
The difference from its projected rank-one operator has eigenvalues
(d+sqrt[d(4-3d)])/2 and (d-sqrt[d(4-3d)])/2. Partial trace is contractive.
Replacing the projected old/reference marginal by rho_DR costs d, because
the residual marginal is positive with trace d. Thus the triangle bound
is g(d), followed by g(d)<=g(epsilon). The complete function g is monotone
on[0,1]: its derivative is 1+(2-3x)/sqrt[x(4-3x)] on(0,1); this is
nonnegative below2/3, and above2/3 follows from
x(4-3x)-(3x-2)^2=4(1-x)(3x-1)>=0. Continuity includes the endpoints.
The simpler projection term alone is not monotone on all[0,1]; d=2/3 and
epsilon=1 give2/sqrt(3)>1, so its isolated replacement by epsilon would be
false. No such replacement is used here. The final estimate g(epsilon)
<=3sqrt(epsilon) follows from epsilon<=sqrt(epsilon) and 4-3epsilon<=4.
This is an input-quality implication, not a cooling theorem. The proof above
requires only the displayed seed-probability premise.

For old/reference density rho and isometries F,V, expand

    F rho F*-V rho V*=(F-V)rho F*+V rho(F*-V*)

and use ||AXB||_1<=||A||||X||_1||B|| to get trace error <=2||F-V||.
Embedding the full finite apparatus into the common output space preserves
trace distance even for bad many-head components. Those components are
handled by trace stability, not fed to the ideal one-head scattering theorem.

Both the perturbed setup and later runtime are the same actual unitary for
the two initial states, so their trace distance is preserved. Combining(3)
and(4), the complete finite output trace error is strictly below

    g(epsilon) + .00966404 + 20 eta.             (5)

The explicit box eta<=10^-5 and epsilon<=10^-9 gives

    g(epsilon)+.00986404
      <=3sqrt(10^-9)+.00986404 < .00996404 < .01.

The inequality3sqrt(10^-9)<10^-4 follows by squaring positive quantities.
No independence between old/reference and auxiliary input is required.
No measurement or postselection is performed; all initial bad-sector weight
and preparation leakage remain in the full trace bound. The pure-input
operator estimate(3) is not extended as an isometry statement to mixed inputs.

## 3. Full positivity, support, slew and modeled work

All factors1+xi_a are positive constants, so the changed controls remain
real PSD local blocks with the same ordinary-neighbor supports. They remain
C1, zero at both endpoints, and identically absent after time5. There are
still fourteen channels on eight sites and no new qubits or old/source
controls. The old added incident cap two, old edge norm3 and source loads
are unchanged. There is no all-site cap-two claim.

There are 2M+6 qubits and 2M+28 positive runtime blocks excluding K;
adding fourteen preparation channels gives 2M+42 channels, without adding
qubits. The source loads remain 27.936224853155858 and 22.228906875353305,
and the old added loads remain 1.993757127633340 and 1.198638631120596.
For each touched site, a safe total-load estimate is its unchanged runtime
load plus (1+eta) times its nominal added-control peak load. Only added-control
loads are rescaled; the runtime/source loads are not calibration variables.
At kappa=10^-8, T=10^16, M=5e17 and qubit count 10^18+6 remain enormous
sufficient resources in Hamiltonian units, with elapsed window [5+T,5+2T].

Full positive-block norm sums and incident derivative norm sums increase by
at most1+eta. Thus for eta<=10^-5, valid rounded bounds are

    added control norm sum <9.001,
    maximum incident control slew <20.001,
    absolute modeled setup work <33.001.

The added-control peak sum is <=(1+eta)[Aiso+45pi/16]<9(1+eta).
Ramp incident slew is <=(1+eta)(3/2)Aiso; the largest pulse pair-site slew
is <=(1+eta)2(pi/2)(10sqrt(3)/3)<20(1+eta). Isolation is constant during
pulses, so its ramp derivative is not added to the pulse peak.

For work, the finite-space identity for the actual state is

    d/ds Tr[rho(s)(HR,M+A_xi(s))]=Tr[rho(s) dot A_xi(s)].

The commutator contribution vanishes by cyclicity. Since A_xi is zero at
both endpoints, Wsetup=Tr[HR,M rho(5)]-Tr[HR,M rho(0)] equals the integral
of that right-hand side. Each isolation profile has total variation two;
each pulse variation is twice its peak.
Integrating the sum of absolute coefficient variations times full block
norms gives at most(1+eta)[2Aiso+165pi/16] <33(1+eta)<33.001.
No ideal-core zero-work shortcut is applied to leaked or imperfect inputs.
The work is modeled Hamiltonian work only, with no microscopic controller
heat, fabrication, reset cost or physical energy identification supplied.

The same operator bound(1) would hold for bounded time-dependent relative
errors, but the displayed C1/slew/work bounds do not follow from a mere
amplitude bound in that wider class. The present result deliberately uses
constant calibration errors. Timing shifts, pulse-overlap errors, altered
static hoppings, density/complement imbalance and changing supports are
separate models and are not included by relabeling them as xi_a.

## 4. Readiness and energy limits

The theorem weakens exact pulse-area and exact pure-seed requirements to
explicit supplied amplitude and joint seed-probability contracts. It supplies
neither their native calibration nor their physical manufacture. The old
single-rail Gibbs construction is not transported to this doubled apparatus.

For explicit energy bookkeeping, the parent's full-space identity coefficient is

    alpha_R=2+(DeltaA+DeltaB+gA+gB)/2+hAB+u_AB/4
       +2JM+lambdaA+lambdaB+mu0+nu+E0+2kappa d_c.

If alpha_a is the identity coefficient of R_a, then alpha_a=|h_a| for an
edge complement and (E0-kappa)/2 for the pin, with sum alpha_a=Aiso/2.
With channel ordering R_1,...,R_9,Q_e0,m,n_e1,Q_m,e1,n_e0,n_e1, the
integrated identity coefficient error is exactly

    delta_theta=4 sum_(a=1)^9 xi_a alpha_a
       +(pi/4)xi_10+(pi/8)xi_11+(pi/2)xi_12
       +(pi/4)xi_13+(pi/4)xi_14.

It is bounded by eta[2Aiso+11pi/8] and already charged in Duhamel. The
full-space integrated coefficient 5alpha_R+2Aiso+11pi/8+delta_theta is
not the supported comparison phase Phi; old K's 2I remains inside its
old evolution. Charging delta_theta again would double count it.

The channel/readiness bound alone does not extend the parent's preparation
energy-moment guarantees uniformly over growing M. For a concrete witness take old |00> and auxiliary mixture

    (1-epsilon)|e0><e0|+epsilon|all><all|,

where |all> occupies every auxiliary qubit. This satisfies the exact seed
probability promise. Each occupied clock bond Q(-J) contributes 2J;
the two rails' M-1 bonds and four endpoint occupations give exactly 4JM.
Using u_AB for the parent's source interaction coefficient, its two means are

    E_good=3+E0+2nu+2kappa d_c,
    E_bad=4JM+3+DeltaA+DeltaB+2hAB+u_AB+gA+gB
             +2(lambdaA+lambdaB+mu0)+2E0+2kappa d_c.

All hopping expectations vanish in the occupied basis vector; its source
vacancies vanish. Neither vector is presumed an energy eigenstate. The
mixture mean shift is epsilon(E_bad-E_good)=4J epsilon M+O(epsilon), and

    Var_mix(H)>=epsilon(1-epsilon)(E_bad-E_good)^2,

because its within-component variances are nonnegative. This is an explicit
allowed-state counterexample to simply continuing the pure-seed moment
formula from trace closeness. The specified coupling interval has a finite
maximum M, so an apparatus-norm-dependent finite bound still exists. A small
clock-length-independent moment continuation requires additional weighted
moment/tail input. The actual control work bound remains valid: it limits
the change of incoming mean energy, not the energy initially delivered.
No general impossibility or cooling obstruction is claimed by this witness.

Native control/thermal suppliers, autonomous preparation, joint static
runtime calibration, noise through the long runtime, complete capture/reset/
reuse, practical resources and physical Hamiltonian/energy/Record identification
remain open. Only the five-unit control calibration box and the stated
correlated input-quality implication are qualified for provisional composition
after the preserved selective analytical check and these two corrections.
Publication, transport checks and independent retained audit are separate.

## Review record and publication boundary

The original calibration proposal is preserved at SHA256
64d81ab828fe2ad28efd526350f8f0286bd07455db0bab9686f2053008c35adc.
The corrected V2 is 6ccdf001f139fa1e2f6ab0fc198984fd5293e489490c29735ac8f5563968b528.
The separate review identified two corrections: use <=10eta at eta=0, and
use actual deficiency d before applying monotonicity of the complete g.
The isolated projection function is not monotone over [0,1]; the d=2/3,
epsilon=1 witness above is retained. Neither correction changes the advertised
small error box or promotes the initial failed wording into a passed proof.
CORRECTIONS.json reverses to the original source; source qualification records
these exact repairs. The finite-permanence result in that same acceptance
file is unrelated and is not imported by this note.

The reviewer authored earlier preparation sources and knew the parent
realifier/resonance chain. The root supplied the proposal before review.
This is same-model, source-exposed analytical reconstruction, not blind or
model-diverse review and not an independent audit of all runtime premises.
The earlier non-discriminating ramp-budget comparison remains budget
arithmetic only; the load-bearing nominal premise is the frozen local
Gram/Duhamel proof. The present calibration derivation is analytical; no
scientific program, parameter scan, dynamics or mutation run was performed
for its source qualification or this drafting task.

The linked parent preserves the exact realifier body and preparation body
with only three Markdown-destination adaptations in the latter. This draft
uses their precise runtime/setup contract and does not widen its coupling,
calibration or thermal scope. Root must carry the corrected proposal,
corrections, selective review and acceptance as provenance, bind any canonical
runner and required helper inputs, and conduct publication/landing checks.
This note supplies no such runner results, audit fields or effective status.
A regular bounded-theorem proposal remains subject to those separate gates.

## Canonical corroboration and integration

The publication adds `scripts/preparation_calibration_2026_10_17.py`, with
18 literal integrity inputs under `outputs/preparation_calibration_2026_10_17_inputs/`.
Its local exact arithmetic is corroboration, not the proof of the analytical
or inherited runtime implications. The source inventory and corrected/original
arguments remain frozen, including both repaired mistakes.

The bounded canonical run passed 63 arithmetic checks and input integrity,
exit 0, 0.08389616012573242 seconds. Eighteen mathematical mutations under
Python -O failed in their intended families; four separate integrity cases
failed before arithmetic, and inert import produced no output. Complete
streams, prelaunch source/runtime identities and resource receipts are in
`outputs/preparation_calibration_2026_10_17_validation/`. CPU10s/file16MiB
limits and external wall limits were applied; no memory cap was applied.

The full expanded identity scalar, individual channelwise phase sensitivities,
energy/variance witness and runtime graph count are covered by analytical
bookkeeping review, not by this runner. Its largest dense matrices have dimension4.
No whole-device evolution, quadrature, full current-main landing gate or retained
audit is claimed. The new source review found no implemented-formula mismatch;
it is same-model and source-exposed and assigns no audit status.
