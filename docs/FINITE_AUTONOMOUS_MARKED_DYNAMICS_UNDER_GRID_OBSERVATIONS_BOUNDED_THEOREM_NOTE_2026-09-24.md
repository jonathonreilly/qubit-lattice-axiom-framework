---
claim_id: finite_autonomous_marked_dynamics_under_grid_observations_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Conditional finite-dimensional original marked dynamics: one positive finite autonomous apparatus
  approximates any fixed number of grid observations with causal system/memory interventions and binned original
  marks. Explicit joint clock/battery error, supplied implementation and preparation; no unbinned timestamps, irreversible
  flags, native selection or infinite-time claim.'
upstream_dependencies:
- autonomous_finite_clock_for_the_original_reduced_dynamics_bounded_theorem_note_2026-09-24
- finite_energy_supply_for_marked_collision_dynamics_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/finite_autonomous_marked_dynamics_under_grid_observations_2026_09_24.py
---

# Finite autonomous marked dynamics under grid observations

**Type:** bounded_theorem

**Status:** conditional mathematical result; unaudited.

The earlier finite apparatus matched uninterrupted one-time reduced channels.
This note adds a joint-state estimate that survives a fixed finite number of
observations and interventions. It retains the original resolved or coherent
formation marks and the same actual correlated battery and clock throughout.
The unitary completion, packet, program, spectral couplings and preparations
are supplied implementation choices. All claims remain conditional mathematics.

## 1. Operational statement and assumptions

Let the system be finite dimensional with supplied H>=0 and jump operators L_j,
j=1,...,m. Put h=||H||, Gamma=sum L_j*L_j, g=||Gamma||. Its specified continuous
instrument is the quantum-jump unraveling with no-event generator -iH-Gamma/2
and the original resolved or coherent marks L_j. No energy-resolved replacement
of those marks is made. Fix T=n tau, tau g<=1/2.

A tester observes at q positive grid times 0<t_1<...<t_q<=T. At each such time
it reads the newly completed bin flags, keeps their classical values, and may
apply an arbitrary trace-preserving quantum operation to the system and its
own memory, controlled by all previous classical values. The memory may begin
entangled with the system. The outcome includes all retained classical records
and the final accessible quantum state at t_q. Any additional readout at T>t_q
counts as another interval and observation in q. Classical random choices and adaptive
instruments are included by keeping their results in the tester memory. The
tester has no access to the battery, clock, future flags or their preparation.
No division by rare-event probabilities occurs: distance is the unconditional
trace norm, at most two. A bound uniform over all such testers is the process
comparison used here. q is fixed independently of resource refinement.

The target continuous instrument is binned: a bin reports zero events, one
event of original mark j, or two-or-more events (one extra symbol). That last
symbol retains its complete conditional system map. The finite collision has
zero probability of the extra symbol. One may instead retain every finite
ordered word of marks in a bin, with the same bound, by embedding the finite
output alphabet in a countable one. Neither choice retains exact event times.

The implemented system, battery, all n flags and clock evolve with a positive,
finite, time-independent Hamiltonian. The external observations in the tester
are allowed interventions, not claimed to be autonomous irreversible readout.
In particular reading a flag dephases it and copies its value into external
classical memory while leaving the original physical flag present. That flag
can subsequently be changed by the history Hamiltonian's backward propagation.

For the finite battery width L, clock width w>=2 and boundary buffer R below,
the explicit bound is

    distance <= min(2, 4 q e_clock + q eta_L + T tau c_mark),
    c_mark = 7g^2+4hg,
    eta_L = min(2,8 sin(pi/[2(L+1)])),
    e_clock = 2 sqrt(tau g) [w+T sigma_V] + b_R,
    b_R = 4 exp(a) a^R/R!,                 a=2JT,
    sigma_V = (4J sin^2(theta)/3) sqrt((2N-3)/N),
    N=w+1, theta=pi/N,
    c_1=(2+cos(2theta))/3,                 2J c_1=1/tau.       (1)

For scalar H the battery is unnecessary and eta_L can be replaced by zero.
Constants in (1) are conservative, not optimal. A single construction and
preparation works for every allowed tester with at most q observations.

## 2. A collision completion close to the identity on the whole space

Let B: H_sys -> H_sys tensor C^m be the stacked operator

    B psi = sqrt(tau) (L_1 psi,...,L_m psi).

On H_sys tensor C^(m+1), take the Julia unitary

    U_c = [[sqrt(I-B*B), -B*],
           [B,             sqrt(I-BB*)]].                  (2)

Functional calculus gives sqrt(I-B*B)B*=B*sqrt(I-BB*), and its adjoint, so
block multiplication proves U_c*U_c=U_cU_c*=I. Its blank-flag column is exactly
the required collision isometry with K_0=sqrt(I-tau Gamma), K_j=sqrt(tau)L_j.
It supplies a completion for all possible intermediate flag inputs.

Write b=||B||=sqrt(tau g)<=1/sqrt(2). The off-diagonal block of U_c-I has norm b;
the diagonal block has norm 1-sqrt(1-b^2)<=b^2. Consequently

    ||U_c-I|| <= b+b^2 <= 2 sqrt(tau g).                    (3)

An arbitrary completion of the same blank column need not satisfy (3). The
completion choice is an explicit extra implementation hypothesis, not inferred
from the original instrument alone.

## 3. Finite energy-conserving lift and the program

Use the parent's positive finite battery: spectral gaps E_a above min(H), one
ladder 0,...,L+1 for each distinct positive gap, and the product sine state beta
on 1,...,L. Total-label blocks m=n+v_a are complete when each coordinate is in
1,...,L+1. The lift V(U) acts as U there, and as identity on all other blocks.
This is one common block decomposition for every unitary on system and flags.
It gives on the entire finite space, including incomplete blocks,

    [V(U),H+H_R]=0,
    V(U_2)V(U_1)=V(U_2U_1),
    ||V(U)-I||<=||U-I||,
    exp(iHs)V(U)exp(-iHs)=V(exp(iHs)U exp(-iHs)).             (4)

The last identity holds because spectral system phases act identically in the
block identification; the identity rule outside complete blocks is preserved.
This global near-identity property avoids a boundary problem that can arise
if separately lifted free evolution is later canceled by an unlifted inverse.

For the k-th fresh flag define interaction-picture gates

    W_k=exp(iH(k-1)tau)V(U_c,k)exp(-iH(k-1)tau),
    G_k=W_k...W_1, G_0=I.                                  (5)

All W_k conserve H+H_R and obey (3). Each is the lift of the corresponding
ideal interaction-picture collision. Products over every interval are lifts
of the ideal interval product, by (4). In the physical picture, the ideal
integer-time product is the sequence of U_c,k each followed by exp(-iH tau),
so the system Hamiltonian is included exactly once.

For every k,l in 0,...,n, telescoping unitaries gives the global estimate

    ||G_k-G_l|| <= 2 sqrt(tau g) |k-l|.                     (6)

This bound applies to arbitrary vectors of system, battery, all flags and an
untouched reference. No product condition on the battery is used in (6).

## 4. A compact packet with its boundary correction

Let N=w+1>=3 and theta=pi/N. The real amplitudes, zero extended, are

    a_j=sin^2(pi j/N)/sqrt(3N/8), j=1,...,N-1.

On positions x=-w,...,-1, put chi(x)=i^x a_(x+w+1). Sum roots of unity at
frequencies one and two to obtain sum sin^4(pi j/N)=3N/8. The cyclic overlap
of sin^2 at a shift ell is N[2+cos(2ell theta)]/8. At shift one no nonzero
cyclic term wraps past a zero endpoint. At shift two precisely one term,
sin^4(theta), must be removed. Hence the actual bilateral overlaps are

    c_1=sum_j a_j a_(j+1)=(2+cos(2theta))/3,
    c_2=sum_j a_j a_(j+2)
       =(2+cos(4theta))/3-8sin^4(theta)/(3N).                 (7)

The endpoint term is required, also at the minimal width N=3. It is not
legitimate to use a periodic packet for a finite-support state.

For the infinite translation T_+ and K=2JI-J(T_++T_+*), define
V=iJ(T_+-T_+*). Then i[K,X]=V, [K,V]=0, and X(t)=X+tV on the finite-moment
domain of this compact state. The phase i^x yields <V>=2Jc_1=1/tau. Equation
(7) gives

    Var(V)=2J^2(1+c_2)-4J^2c_1^2
          =16J^2 sin^4(theta)(2N-3)/(9N).                    (8)

Since ||X chi||<=w, the Hilbert-space triangle inequality gives

    ||(X-t/tau) exp(-iKt)chi|| <= w+t sigma_V.               (9)

No assumption of independent position and velocity is made. Projection of X
onto [0,n] cannot increase its pointwise distance from t/tau in [0,n].

## 5. Positive finite clock and a joint interval estimate

Let the finite clock positions run from -w-R to n+R, with M=n+w+2R+1. Put
k(x)=min(n,max(0,x)), Gcal=sum_x |x><x| tensor G_k(x),

    K_M=2JI-J(T_M+T_M*),
    e_0=2J[1-cos(pi/(M+1))],
    H_hist=Gcal [(K_M-e_0 I) tensor I] Gcal*,
    H_aut=H+H_R+H_hist.                                     (10)

The path spectrum proves positivity. Equation (4) proves
[H_hist,H+H_R]=0. The initial clock support has G_k(x)=I, so the stipulated
initial state is the product chi tensor beta tensor arbitrary system/reference
input tensor all blank flags. No clock-system pre-entangling operation is used.

Let phi_t be the freely evolved finite clock state, with the scalar e_0 phase
included. Compare it with the infinite-chain state using the same scalar
phase. Adjacency powers agree below order R on chi. The two exponential series
give vector error at most 2 exp(a)a^R/R!, uniformly on [0,T]. A controlled
unitary difference has norm at most two, so applying it to this state error
costs at most b_R in (1).

For a grid time t=k_t tau define

    d_t = sup_||psi||=1 || Gcal(phi_t tensor psi)
                          -phi_t tensor G_k_t psi ||.

Extend the clipped controls constantly beyond the finite path for comparison.
Equations (6),(9), plus the preceding boundary estimate, show d_t<=e_clock.
The same estimate holds for the inverse controls. It is a joint vector bound,
uniform on arbitrary correlated payload and reference inputs, not a statement
only about the reduced system channel.

Between grid observations s,t, the interaction-picture propagator is
Gcal exp(-i(K_M-e_0)(t-s))Gcal*. Acting on phi_s tensor psi, first replace
Gcal* by G_k_s*, at vector cost d_s. The free clock evolves exactly phi_s to
phi_t. Replace the final Gcal by G_k_t at vector cost d_t. Thus the output
differs from phi_t tensor G_k_t G_k_s* psi by at most d_s+d_t. Purification
and trace-norm contraction give joint channel error at most

    2(d_s+d_t)<=4 e_clock.                                 (11)

Interventions in this picture are conjugated by exp(-iHt) on the system;
the battery's free rotation does not affect an inaccessible battery. Classical
flag readout, causal feedback and tester memory operations are contractions
and act trivially on the ideal free clock. Telescope (11) over q intervals.
The ideal comparison always has a free product clock; the actual clock need
not. Earlier accumulated errors are propagated by actual trace-preserving
maps. No assumption about the state after an actual observation is inserted.
This proves the first term 4q e_clock in (1).

## 6. The same battery through interventions

For any interval the conserving program product is exactly V(U_interval) by
(4). On a product input psi tensor beta its output differs in joint trace norm
from U_interval psi tensor beta by at most eta_L, including arbitrary reference
and old-flag factors. This is the parent's controlled-translation isometry
estimate; it is uniform over the whole interval, not multiplied by its gate
count. Incomplete blocks cause no problem because the prepared beta is buffered.

Now compare the entire ideal-clock process to the ideal collisions with a
mathematical spectator beta. Telescope interval by interval: at each newly
compared ideal interval beta is a product spectator and the estimate applies;
earlier state error is carried by the actual conserving interval and the same
tester operation. This costs q eta_L. This proof never resets the implemented
battery or assumes that it returns to beta. Its actual correlations, including
those produced by energy-changing interventions, remain in the error carried
forward. The product beta occurs only in the ideal comparison process.

## 7. Marked-bin comparison with the original continuous instrument

Write N_t=exp[(-iH-Gamma/2)t]. For one bin the exact zero-event operator is
N_tau. The exact one-event mark-j completely positive map has Kraus density

    N_(tau-s) L_j N_s,  0<=s<=tau.

The collision zero operator is exp(-iH tau)sqrt(I-tau Gamma), and its one-mark
operators are sqrt(tau)exp(-iH tau)L_j. We bound their classical direct sum,
retaining marks, rather than infer an instrument bound from a reduced channel.

For contractions, ||A rho A*-B rho B*||_diamond<=2||A-B||. A dissipative product
formula and ||[H,Gamma]||<=2hg give

    ||N_tau-exp(-iH tau)exp(-tau Gamma/2)|| <= tau^2 hg/2.

The scalar bound |exp(-x/2)-sqrt(1-x)|<=x^2 on 0<=x<=1/2, by the two Taylor
remainders, gives zero-event map error <=tau^2(hg+2g^2).

For one-event maps, stack the original marks and define A_s by the operators
N_(tau-s)L_j N_s and B_s by exp(-iH tau)L_j. Both stacked operators have norm
at most sqrt(g). The survival perturbation estimate
||N_u-exp(-iHu)||<=ug/2 and the stacked commutator estimate
||( [H,L_j] )_j||<=2h sqrt(g) imply

    ||A_s-B_s|| <= sqrt(g)[tau g/2+2hs].

Dephasing the mark flag is a contraction. Integrating the corresponding
stacked-map difference costs at most tau^2(g^2+2hg), jointly for all marks.

For k>=2 events, the summed k-event CP map has diamond norm at most
(tau g)^k/k!: use contractive no-event maps and the CP jump map of diamond norm
g in the ordered time simplex. Summing gives at most
(tau g)^2 exp(tau g)/2 <=(tau g)^2. Coarsening all those outputs to the extra
symbol only contracts distance. Together these estimates give local marked
error <=tau^2(4g^2+3hg)<=tau^2 c_mark. Both complete instruments are channels.

Ideal fresh collision gates commute with later operations on previous flags,
so their dephasing/readout can be deferred until a tester observation. Telescope
the local marked bound through every bin, interspersing the same causal tester
maps, to get at most T tau c_mark. This proves the last term of (1) and the
complete finite-grid process bound. Exact continuous timestamps would
require a different output comparison; they are explicitly outside this result.

## 8. Resource and energy statements

For fixed T, c_1>=1/2, J<=1/tau, and sigma_V<=constant/(tau w^2). Choose
w of order (T/tau)^(1/3), bounded below by two, and R>=8a. Then

    e_clock=O(sqrt(g) T^(1/3) tau^(1/6))+O(exp(-7a)).         (12)

For fixed finite H,L_j and fixed q, taking tau->0 and L->infinity makes (1)
vanish. The clock dimension and hopping strength are O(tau^-1) at fixed T;
there are n=T/tau blank flags. These are sufficient bounds only.

The initial free battery energy is (L+1)sum_a E_a/2 and its dimension (L+2)^r.
Because the real clock overlaps are multiplied by i^x, its initial H_hist
expectation is 2J-e_0=2J cos(pi/(M+1)), above the actual ground. H_hist includes
program interactions; this is not claimed to be a separately free clock energy.
Between observations, both H+H_R and H_hist are conserved. Thus battery and
system energy changes balance exactly on every such interval. A tester may
inject system and interaction energy at an observation; that is additional
external work and is not hidden in a claimed closed energy balance.

For a bounded system observable H, final energy error is at most h times (1).
For example under supplied growth h=O(C^2), g=O(C) with fixed r and q, sufficient
choices L=ceil(c_L C^2), n=ceil(c_n C^15), tau=T/n,
w=max(2,ceil(n^(1/3))), and R=ceil(8a), with fixed positive c_L,c_n,
give process error O(C^-2) and absolute system-energy error O(1). When sum E_a=O(C^2), battery preparation
energy is O(C^4), while clock dimension, strength and preparation energy are
O(C^15). Flags number O(C^15) with exponentially large joint Hilbert space.
These conservative resources are not requirements or an improvement over the
cheaper parent bound when only one-time reduced channels are requested.

## 9. Limits and outstanding checks

The completion, spectral lift, clock packet, program couplings, pure blank
flags, energy reference and external observation convention are supplied.
Clock nearest-neighbor hopping does not make the payload couplings spatially
local. No bounded-strength, finite-density or infinite-time limit is proved.
No physically preferred H, compensation, electric completion, bath, vacuum,
time arrow or continuum theory is selected. This construction is consistent
with finite recurrence and with backward evolution of the program flags.

The result is a joint finite-observation
error estimate with explicit finite energy resources. It is not an exact
autonomous Markov instrument or an irreversible memory theorem. The separate PRE reconstruction was sealed before release of the root proof.
Released-source comparison and final publication bindings are in the review packet;
scientific comparison is distinct from retained audit status.

## 10. Completed finite author controls and a preserved failed diagnostic

The self-contained primary runner checks the zero-extended packet overlaps
at seven widths, including N=3, and rejects removal of the shift-two endpoint
term. Two-dimensional exact jump-superoperator exponentials retain zero, each
one-mark, and multiple-event branches. Their Choi trace-norm upper bounds obey
the marked-bin inequality at four steps. Swapping mark labels is detected; at
the smallest step a maximally entangled input itself witnesses violation of the
claimed bound for that altered instrument.

A complete finite battery and three physical flags are propagated without
reset. A reference-entangled system input undergoes a first flag measurement,
outcome-controlled system flip, continued autonomous evolution, and the two
remaining flag readings. Direct and inverse endpoint operator norms are also
computed on the whole 672-dimensional payload. At tau=.001 and .0001, all
identities, normalization and joint bounds pass; the smaller step has a joint
clock/battery trace distance about .00794 against the conservative bound 1.207.
These two examples have T=3tau and are finite implementation controls, not a
fixed-T convergence experiment or a numerical proof of (12). A completion
altered only on nonblank flag inputs loses the near-identity bound while keeping
the original blank column. A cyclic battery wrap remains unitary but violates
free-energy conservation. Both changes are detected.

An initial stronger control hit an absolute eigensolver positivity check at
large J: the exact zero eigenvalue was computed as -4.44e-12 at J=6496.27.
Its source, stdout, stderr and diagnosis are preserved in control_attempt02.
The exact path spectrum is nonnegative analytically. The corrected numerical
diagnostic compares the entire dimensionless K/J spectrum with that formula,
using the same 2e-12 tolerance; the actual maximum error is 1.78e-15. This is an
explicit scale correction of a numerical diagnostic, not a change to the
Hamiltonian or positivity theorem. The earlier smaller finite controls remain
in control_attempt01. All full outputs are retained; numerical values are
floating corroboration, not interval certificates or independent evidence.

## Imports and verification

- [Finite autonomous one-time construction](AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): the positive finite history Hamiltonian, interaction-picture convention, finite-path boundary comparison and resource accounting, with their supplied-model hypotheses.
- [Finite energy supply](FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): the buffered finite spectral lift and its reference-uniform joint-vector estimate, without an actual battery reset.

The direct interaction-picture lift, squared-sine packet, joint interval bound
and separate marked-cell estimate are proved above. Every original parent
assumption remains explicit. The primary controls are author corroboration;
they do not prove the analytic uniform quantifiers or create independence.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/finite_autonomous_marked_dynamics_under_grid_observations_2026_09_24.py
```

## Machine-status block

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: finite_autonomous_marked_dynamics_under_grid_observations_bounded_theorem_note_2026-09-24
target_blocker_text: "An uninterrupted one-time reduced-channel approximation does not establish the original marked statistics under observations and interventions."
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Determine physically constrained resource selection, locality and sustainable record storage under the original formation instrument."
conditional_surface_status: "Supplied finite H and original marks, explicit Julia completion, positive spectral battery, prepared squared-sine clock, program and finite grid tester convention."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Joint endpoint and hybrid bounds control correlated apparatus states and a separate marked-bin estimate controls the original continuous instrument at the stated resolution."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Landing-review boundary and No-Go Discipline Gate

N1: supplied finite Hamiltonian, marks and fixed grid observations. N2: continuous observation and unbinned event times remain outside this result. N3: the battery, clock and operations are prepared inputs. N4: the finite-clock and energy-supply parents retain their model hypotheses. N5: finite matrix controls corroborate the packet, lift and process estimates; the proof supplies uniform bounds. N6: no irreversible autonomous record or physical clock selection follows. N7: the actual clock and battery retain correlations between observations; the comparison does not reset them. N8: endpoint corrections and full-unitary near-identity control are essential, as are the stated resource scalings.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive the supplied dynamics.

Historical author checks remain provenance only. The complete original packet remains recoverable at PR #9067's frozen head. No audit verdict or retained grade is applied.
