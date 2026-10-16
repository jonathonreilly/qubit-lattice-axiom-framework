---
title: Installed local-clock reset and entry preparation
claim_id: installed_local_clock_reset_preparation_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: finite_local_clock_word_windows_bounded_theorem_note_2026-10-15
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied Markov reset and finite positive entry pulse with a model-specific necessary damping-action bound
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: complete conditional analytic bounds with explicit reservoir, pulse, timing and complete-output premises
audit_required_before_effective_retained: true
bare_retained_allowed: false
status: proposed_retained
canonical_parent_binding_complete: true
publication_pr: null
publication_binding_complete: true
source_acceptance_status: checked_conditional_sources
upstream_dependencies: ["finite_local_clock_word_windows_bounded_theorem_note_2026-10-15"]
runner: scripts/installed_local_clock_reset_preparation_2026_10_15.py
packet: .claude/science/physics-loops/toe-local-clock-reset-preparation-20261015
next_trace_action: root source review and actual publication binding; separate cumulative landing and retained-audit gates remain
---

Status: proposed_retained

# Installed local-clock reset and entry preparation: conditional finite-time support

Claim type: `bounded_theorem`. Current scientific status: `conditional-support`.
This note combines two checked analytic sources: a sufficient finite-time
reset-plus-entry-preparation channel, and a necessary damping-action bound for
the same uniform local Markov model. The original finite generator stays
installed. The reservoir, its readiness and local damping law, and the positive
entry pulse are supplied physical interfaces. Neither theorem constructs that
reservoir or derives it from physical axioms.

## Concrete result and output domain

Let D contain the unchanged old system and C the literal positive boundary
clock, with n_C=L+9, L>=8. Keep H=K+H_app, including every original old term,
the occupied q0-q1 bond and all scalar/reserve terms. The input sigma_DCR may
be arbitrarily mixed, entangled or correlated across the old system, every
clock occupation sector and a passive reference R. A separately ready reservoir
implements the stipulated uniform one-site amplitude-damping generator; all
dissipative outcomes are summed and that reservoir is traced.

Finite smooth damping followed by one finite positive onsite pulse prepares
the actual v0 entry with a uniform complete-output trace/diamond allowance
epsilon_r+epsilon_p, capped at 2. Its ideal reduced output is

    U_K(t0) Tr_C(sigma_DCR) U_K(t0)* tensor |entry><entry|_C,
    t0=t_r+t_p.

The old/reference marginal ages for the full reset and pulse time. “Complete”
here refers to the retained D,C,R reduced output, not every reservoir/controller
factor. Reset exports clock-held information; it is not no-jump postselection,
a return of the bath to readiness, or preservation of a record held in C.
Positive subnormalized blocks inherit the bound multiplied by their trace;
normalized-success claims would need their own probability hypotheses.

The companion necessary-action result allows any finite number-preserving H
with vacuum restriction K and n>=1 clock qubits under the same nonnegative
uniform local lowering dissipators. Its comparison also includes actual old
free aging. For total damping action A_t=integral_0^t r(s)ds and eta=exp(-A_t),

    ||Phi_t-Q_t||_diamond >= max(sqrt(eta), 2[1-(1-eta)^n]).

The witnesses are separate allowed inputs: a vacuum/one-excitation coherence,
and a fully occupied clock. The two bounds are maximized, not added. Removing
number-sector coherences from the input domain removes that coherence witness.
The binary vacuum test used in the proof is a mathematical norm witness, not
an implemented detector.

## Explicit time, action, strength and energy prices

The complete preparation proof defines the literal coefficient C_* and proves
C_* <= ((9+5sqrt(2))/8)B, where B=||H_app|| on the full hard-core space. For
0<epsilon_r<=1 a sufficient smooth schedule is

    r>=16 C_*/epsilon_r,
    T=(2/r) log(4sqrt(n_C)/epsilon_r),
    t_r=T+2/r,                  A_final=rT+1.

Both ramps last 1/r and are included. The rate peak is r, its maximum slope
is pi r^2/2, and the reduced dissipative generator's complete norm/action
allowances are 2n_C r(t) and 2n_C(rT+1). Those are open-system generator prices,
not Hamiltonian norm or energy bounds for a microscopic reservoir.

The positive entry pulse is Omega_p(s)(I-X_v0), with
Omega_p(s)=(pi/t_p)sin^2(pi s/t_p). Its endpoint is exactly X_v0 including the
scalar phase. With the actual right-entry value

    G_e=sqrt(alpha0^2+2Lambda|z0|^2),
    0<t_p<=epsilon_p/(2G_e),

the pulse contributes at most epsilon_p. Its peak operator norm is 2pi/t_p,
peak derivative 2pi^2/t_p^2, norm action pi and derivative action 4pi/t_p.
Every term of H remains active; the proof neither cancels K nor assumes that
K commutes with the apparatus's old Pauli coefficients.

For reset accuracy epsilon in (0,1), the action theorem requires

    A_t>=2log(1/epsilon),
    A_t>=-log[1-(1-epsilon/2)^(1/n)].

The supplied sufficient schedule has
A_final=2log(1/epsilon_r)+log n_C+2log4+1. Its leading coefficient of the accuracy
logarithm matches the coherence lower bound only at fixed n. There is no
optimality claim for peak rate, runtime, energy, constants, joint size/accuracy
scaling, or arbitrary coherent finite-reservoir protocols. After the actual
unitary entry pulse, the necessary lower bound is weakened by its complete
allowance e_p=2G_e t_p; total accuracy epsilon entails lower_reset<=epsilon+e_p.
The pulse allowance cannot be omitted or transferred through a later discard.

The nominal uniform damping model obeys d<H>/dt=-r(t)<H_app><=0. This is an
ensemble statement for the specified reduced generator, not an individual-jump
cooling law, detailed balance or a physical bath construction. The pulse's
work is separately bounded by 4pi/t_p. Ideal entry moments of the SAME installed
H are the original old mean plus alpha0 and original old variance plus
2Lambda|z0|^2. For beta>=||H-aI|| and total output trace allowance epsilon,
the same-H mean and variance errors are bounded by beta epsilon and
3beta^2 epsilon; reference-valued linear centered moments cost beta^j epsilon.
Centering is an estimate, not removal of the installed physical scalar.

## Exact mathematical import and downstream use

The sole external mathematical target is the
[finite local-clock window note](FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md),
canonical SHA256 bcefbb192900b56ee937255d54d78a2aba777c1120416addc5b040147d06700a.
The imported complete clause is its positive occupied-chain boundary proof
b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1 at exact byte
interval [62134,80595). Its vacuum silence, number conservation, whole-space
norm/gap and right-entry compression support the preparation application.
This import does not mean that all other window conclusions are hypotheses of
the action theorem. The action proof's use of the preparation schedule and
pulse is internal to this combined note; it creates no self-edge. Stack ancestry
supplies no mathematical premise.

A downstream boundary-word use consumes the resulting aged entry and retains
the time order U_K(t) W U_K(t0). It does not replace it by U_K(t+t0)W for a
noncommuting K. The result supplies conditional upstream preparation support
for that installed-word experiment; it does not halt the subsequent moving
clock, construct a finite-duration classical reader, or make a permanent record.

## Sources, exposure, verification and remaining conditions

| Complete source | Source disposition and publication treatment |
| --- | --- |
| Reset/preparation 95fbc8dddb92e732e76327546eeb2ec89ce0a673939c8135c5f160c72fa03825 | Separate source-exposed assessment 6b4e4801; root acceptance 7672e171. The full accepted original is archived. Only its historical relative citation target is rendered to the canonical window filename; every other byte is unchanged. |
| Necessary action 30c1c586644956f5e09c47a71b58318b75a7bc2ff5af03539f958e7de0ba8551 | Separate source-exposed assessment 1a876891; root acceptance a5fe9c5e. Its complete body is appended unchanged. |

Both complete arguments, reviewer reports, root dispositions, exact source
copies, actual metadata streams and exposure/failure histories are preserved.
Historical “provisional” or “review pending” prose in the unchanged source
bodies records the time of writing; current conditional source acceptance is
stated above. The reset publication derivative has SHA256
58d8ab952bb0e950df83cf6e7c557d10187ef1bbfb479d8510a62b831b5385e9; its complete
before/after, one-link diff and exact inverse map are archived separately.

No scientific numerical program was run by the source authors, separate
assessors or root for these two results. Their analytic arguments are the
scientific evidence. Source-identity checks execute zero mathematical
predicates; their hashes and receipt counts do not prove a theorem. Separate
reviews disclose same-family and authorship exposure; no blind-discovery,
model-diversity, empirical-validation or retained-audit claim is made.
Amplitude damping, dilation, complete trace contraction and Duhamel are
standard machinery, credited as such rather than claimed as new.

The ready independent Markov reservoir, uniform local rates, calibrated smooth
controls, external timing and complete error certificates remain supplied.
Full generator faults, ready-domain correlations and unequal actual rates
need the stated complete calibration allowance; they do not automatically
inherit nominal number or energy laws. The actual reservoir geometry,
Hamiltonian norm/energy, purity source, reusable readiness, microscopic
derivation, native coefficients, detector/classical observation and physical
energy identification remain open. No result for a separate finite unitary
reservoir is included in this milestone.

## Complete reset and entry-preparation proof; one citation target rendered

# Conditional finite-time reset and one-head preparation with the boundary apparatus installed

This is a proposed conditional extension of the checked boundary apparatus, not an independently accepted result, retained audit, native cooling mechanism or microscopic bath construction. It supplies an explicit reduced channel if local amplitude damping and one bounded local pulse are supplied. It does not assume that the clock starts clean. Every original factor, the complete original generator K including its scalar/reserve, and every apparatus term remain installed throughout.

The new conclusion is a complete old-system/clock/passive-reference estimate for arbitrary initially correlated clock inputs. A local vacuum-silence estimate bounds reset backaction by a coefficient divided by the damping rate; increasing reset duration to suppress the remaining excitation does not multiply that backaction by the duration. A literal in-family counterexample below shows why number decay alone would not justify zero backaction. The reset reservoir is traced in this channel. Its retained outputs, microscopic energy, preparation, finite-memory realization and reuse require additional suppliers.

## 1. Exact premise and literal operator

The direct mathematical premise is the complete boundary construction [b3b6cb24](FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md), SHA256 b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1. Its conditional source acceptance and my earlier complete source-exposed assessment are archived separately; neither a hash nor an acceptance substitutes for its argument. This note uses its actual operator, full-space bounds and RIGHT-entry moment formula. It does not import the later physical-reader construction or another worker's reset source.

Let D be the finite original carrier, including the occupied chain q_l=(l,0,0), 0<=l<n_old, n_old>=2. Its arbitrary finite Hermitian K, all labels, factors and original terms are fixed. The old q_0-q_1 edge remains present. Further old sites must avoid the fresh positions below. Algebraically the proof permits arbitrary finite K on D; claiming that the entire installation is ordinary-NN additionally retains the parent's onsite/ordinary-NN support premise for K. No commutation between K and the old Pauli factors is assumed. Let R be an arbitrary passive reference.

Fix the already installed finite L>=8, Omega>0 and Lambda>0. There are n_C=L+9 new qubits C: heads

    v_0=(0,1,1), v_1=(-1,0,0), v_2=(0,-1,-1),
    v_j=(0,1-j,-1), 3<=j<=L,

and these eight mediators:

    cell0: l=v_1, r=v_0,
      a=(-1,1,0), b=(0,1,0), a'=(-1,0,1), b'=(0,0,1);
    cell1: l=v_1, r=v_2,
      a=(-1,-1,0), b=(0,-1,0), a'=(-1,0,-1), b'=(0,0,-1).

The original placement and the eight selected NN edges per cell are unchanged; the direct head bonds run from v_j to v_(j+1), 2<=j<L. Thus the Hamiltonian still has n_C fresh sites and L+14 added NN edges. No new Hamiltonian routing, relocation of D or access through an occupied old site is introduced here. Local damping access to every fresh site and an onsite pulse at v_0 are additional interface premises, not consequences of those coordinates.

Write a_u=|0><1|_u, n_u=a_u* a_u, N=sum_(u in C)n_u,
S_uv=a_u* a_v+a_v* a_u, and B_uv(z)=z a_u* a_v+conj(z)a_v* a_u. The parent fixes

    J_j=Omega sqrt((j+1)(L-j)), 0<=j<L,
    kappa_j=J_j for j=0,1,
    P_0=X_(q0), P_1=Z_(q0), phi_0=-pi/4, phi_1=pi/4,
    g_j=sqrt(kappa_j),
    z_j=sqrt(kappa_j)[-(209/120)cos(phi_j)
                              +i(209/32)sin(phi_j)],
    s_(j,l)=448 kappa_j/209, s_(j,r)=480|z_j|^2/209,
    L_j=sum_(u in A_j)n_u+(P_j/4)(n_b-n_b')
                                  -(S_ab+S_a'b')/4,
    V_j=g_j(S_al+S_a'l)+B_br(z_j)+B_b'r(conj(z_j)).       (1)

Each head receives its actual incident self-energies s_v: v_0 receives s_(0,r), v_1 receives s_(0,l)+s_(1,l), and v_2 receives s_(1,r). Set

    c=Omega(L+1), alpha_v=c+s_v,
    A=sum_v alpha_v=(L+1)c+sum_(j=0,1)(s_(j,l)+s_(j,r)),
    H_app=Lambda(L_0+L_1)+sqrt(Lambda)(V_0+V_1)
              +sum_v alpha_v n_v+sum_(j=2)^(L-1)J_j S_(v_j,v_(j+1)),
    H=K+H_app,                         B=||H_app||=A+8Lambda.  (2)

K acts trivially on C and R. The parent proves on the entire hard-core-qubit space, not just one excitation,

    H_app |vac>_C=0 on every old input, [H,N]=0,
    delta N <= H_app <= B I,
    delta=min(Omega,Lambda/2)/(1+2f/sqrt(Lambda))^2>0,
    f^2=max(2|z_0|^2,2(kappa_0+kappa_1),2|z_1|^2).      (3)

The zero space of H_app is D tensor the all-new vacuum. The gap is an apparatus statement, not a gap for arbitrary H. No reserve is added or subtracted in this note. A previously installed scalar is included in K. Mathematical centering below is only an estimate.

For the bare entry e=|1_(v0),0_else>, let J_e append that clock state. Because v_0 is the RIGHT port of the reversed first cell,

    alpha_0=c+s_(0,r),
    J_e* H_app J_e=alpha_0 I,
    J_e* H_app^2 J_e=(alpha_0^2+2Lambda|z_0|^2)I,
    G_e=||H_app J_e||=sqrt(alpha_0^2+2Lambda|z_0|^2).     (4)

Replacing |z_0| by g_0 would be incorrect for this geometry. All these quantities are finite and are computed from the actual installed coefficients.

## 2. The supplied reset interface and its output domain

The reset assumption is the following explicit local open-system generator, with no action directly on D or R:

    d rho/dt = -i[H,rho]+r(t) sum_(u in C) D[a_u](rho),
    D[a](rho)=a rho a* - (a* a rho+rho a* a)/2,          (5)

where r(t)>=0 is a specified finite continuous rate profile. The environment is in the ready domain required to implement (5), initially uncorrelated with DCR; all reset outcomes are summed. No condition is imposed on the initial density operator sigma_DCR. In particular, C may be arbitrary, mixed and entangled with D and R. This is not a conditioned no-jump trajectory or a vacuum-heralding instrument.

Equation (5) is a substantive dissipative supplier. Its jump operators have one-site system support, but this does not specify a finite microscopic reservoir, its Hamiltonian, its spatial ports or a whole-apparatus NN dilation. It is not derived from (3), a spectral gap, the native framework, detailed balance or a thermal assumption on D. The channel theorem retains every D, C and R factor. It traces the reset reservoir; specifying (5) alone would not determine a unique retained reservoir output or a physical classical jump record.

The finite-dimensional evolution in (5) is CPTP. One direct construction alternates the unitary generated by H with local amplitude-damping channels over small time slices. The local channel at integrated action x has Kraus operators

    E_0=|0><0|+e^(-x/2)|1><1|,
    E_1=sqrt(1-e^(-x))|0><1|.                           (6)

Its first-order expansion is I+x D[a], and the unitary's is I-i dt[H,.]. Products of these CPTP maps converge in the finite superoperator norm to the unique solution of (5); the local second-order errors sum to zero with the mesh. This proves the needed positivity and trace-contraction facts without treating (5) as an assumption of its desired endpoint state. The product construction is a mathematical justification, not a physical rapid-switching realization or a new control permission.

Let

    R(t)=integral_0^t r(s) ds, eta(t)=exp(-R(t)),
    U_K(t)=exp(-itK), sigma_DR=Tr_C sigma_DCR.           (7)

The actual expectation obeys an exact number law for every initial state:

    Tr[N rho(t)]=eta(t) Tr[N sigma].                    (8)

Indeed, i[H,N]=0 and sum D[a_u]^*(N)=-N. This does not say that each actual site occupation decays independently: the installed hopping redistributes it. Nor does (8) alone prove preservation of the old/reference marginal or elimination of clock coherences.

## 3. Local vacuum silence yields an integrable backaction bound

Use the comparison channel Psi_t generated by K and the same damping, omitting H_app only in this mathematical comparison. It factorizes exactly as free old evolution and the product of the channels (6), including on correlated inputs. Hence its site occupations are

    Tr[n_u Psi_t(sigma)]=eta(t) p_u, p_u=Tr[n_u sigma].  (9)

For any Hermitian h and normalized positive rho,

    ||[h,rho]||_1 <= 2 sqrt(Tr[h^2 rho]).               (10)

For example ||h rho||_1=||h sqrt(rho) sqrt(rho)||_1 is at most the product of the Hilbert-Schmidt norms, giving sqrt(Tr[h^2 rho]); the other commutator term has the same bound. This argument is unchanged with an arbitrary reference.

Every literal term in (2) has local vacuum silence. For an occupation term d P n_u with P an old Hermitian unitary (or P=I), its square is |d|^2 n_u. For an exchange B_uv(z),

    B_uv(z)^2=|z|^2(n_u+n_v-2n_u n_v)
                     <=|z|^2(n_u+n_v).                (11)

The coefficients in these statements commute with the new annihilators. We do not square a sum of noncommuting old Pauli terms or assume that K commutes with them.

Define C(sigma) by summing |d| sqrt(p_u) over the occupation terms and |z| sqrt(p_u+p_v) over the exchange terms in the literal decomposition (2). The eight Lambda n_u terms, four Lambda P n_u/4 terms, all head occupations, four mediator exchanges, eight ports and direct head exchanges are all included. Applying (9)-(11) termwise gives

    ||[H_app,Psi_t(sigma)]||_1 <=2 C(sigma)e^(-R(t)/2).

Let Phi(t,s) be the actual CPTP propagator. The exact time-dependent Duhamel identity and trace contraction give

    ||Phi(t,0)(sigma)-Psi_t(sigma)||_1
       <=2 C(sigma) integral_0^t e^(-R(s)/2) ds.         (12)

The integrand is evaluated on the explicit comparison channel, not on an assumed distribution for the actual interacting apparatus. This is why arbitrary noncommuting K and initial D-C-R correlations do not introduce a missing term.

A uniform, explicitly computable coefficient is

    C_* = A+9Lambda
          +sqrt(2)[Lambda+sum_(j=2)^(L-1)J_j
                         +2sqrt(Lambda)sum_(j=0,1)(g_j+|z_j|)]. (13)

Indeed p_u<=1. The occupation sum is A+8Lambda+Lambda; the four rail exchanges have total norm Lambda; the two cells' port norms sum to 2sqrt(Lambda)sum(g_j+|z_j|); each exchange receives at most sqrt(2). Thus C(sigma)<=C_* on the complete initial-state domain.

There is also a convenient comparison with the exact full norm, with no dimension-dependent square-root factor:

    C_* <= nu B, nu=(9+5sqrt(2))/8.                    (14)

To check it, write S=sum(s_(j,l)+s_(j,r)), A_0=(L+1)c, so A=A_0+S. The inequalities 2sqrt(Lambda)x<=Lambda+x^2 applied to g_0,|z_0|,g_1,|z_1| bound the port sum by 4Lambda+sum(g_j^2+|z_j|^2). Equation (1) implies sum(g_j^2+|z_j|^2)<=S/2. The head-incidence bound sum_v Gamma_v=2sum_(j=0)^(L-1)J_j<=A_0 gives sum_(j=2)^(L-1)J_j<=A_0/2. Consequently

    C_* <=(1+sqrt(2)/2)A+(9+5sqrt(2))Lambda
          <=nu(A+8Lambda).

Equation (12) therefore need not grow as B times the full reset duration. Vacuum silence and decaying occupations make its integral finite. This is a sufficient error bound, not a lower bound on every reset mechanism or an assertion that the actual state follows independent local damping.

## 4. Complete replacement error, including initial clock/reference coherence

The comparison channel has the following full-state replacement estimate:

    ||Psi_t(sigma)
        -U_K(t) sigma_DR U_K(t)* tensor |vac><vac|_C||_1
       <=2sqrt(1-(1-eta(t))^n_C)
       <=2sqrt(n_C)e^(-R(t)/2).                        (15)

Here and below tensor ordering is identified by the unchanged labels. To prove (15), dilate each damping channel using an auxiliary two-level environment:

    V_eta|0>=|0_C 0_E>,
    V_eta|1>=sqrt(eta)|1_C 0_E>+sqrt(1-eta)|0_C 1_E>.

At eta=0, V_0 transfers the input to E and fixes C to vacuum. The overlap operator is

    V_0* V_eta=diag(1,sqrt(1-eta)).

For n_C tensor factors its smallest eigenvalue is (1-eta)^(n_C/2). Purify any correlated sigma_DCR, apply the two isometries, and use this positive overlap lower bound. The trace distance between the two resulting pure states is at most 2sqrt(1-(1-eta)^n_C). Tracing E and the purifying system and applying U_K proves (15). This controls coherences and all passive references. It is stronger information than a bound solely on the probability of residual excitations. No purity of C was assumed.

Combining (12) and (15), the reset error is at most

    epsilon_reset(t)=min(2,
       2 C_* integral_0^t e^(-R(s)/2) ds
                       +2sqrt(n_C)e^(-R(t)/2)).        (16)

The same bound holds in diamond norm between the reduced D-C channels, with arbitrary passive R. One may instead use the input-dependent C(sigma) in a state-specific estimate. The estimate scales by the trace for a positive unnormalized input block; externally retained classical flags can be included in R. There is no normalization denominator or discarded failure branch. If C is initially exactly vacuum, vacuum silence proves exact old free evolution during reset, independently of the deliberately coarse uniform bound.

## 5. A finite smooth reset schedule and explicit rates

For any finite peak rate r>0 and plateau length T>=0, choose:

    r(t)=r sin^2(pi r t/2),               0<=t<=1/r;
    r(t)=r,                              1/r<=t<=1/r+T;
    r(t)=r cos^2(pi r (t-1/r-T)/2),       1/r+T<=t<=2/r+T;
    r(t)=0 outside this interval.

This profile is continuously differentiable, including its zero and plateau joins. Its reset duration, integrated action and maximum slope are

    t_r=T+2/r, R(t_r)=rT+1, max|r'(t)|=pi r^2/2.       (17)

Each ramp contributes at most 1/r to the integral in (16), and the plateau contributes at most 2/r. Thus

    epsilon_reset(t_r)<=min(2,8 C_*/r
                                      +2sqrt(n_C)e^(-rT/2)). (18)

For a prescribed reset allowance 0<epsilon_r<=1, one finite sufficient prescription is

    r>=16 C_*/epsilon_r,
    T=(2/r)log(4sqrt(n_C)/epsilon_r).                   (19)

Each term in (18) is then at most epsilon_r/2. The additional exp(-1/2) from the two ramps was conservatively discarded. The proof charges switching time rather than assuming an instantaneous rate change. If an external maximum slope or peak rate is imposed, it must accommodate this schedule or a newly checked allocation; (19) does not promise a solution under an arbitrary fixed cap.

Each local dissipator has complete induced trace-norm bound <=2r(t), because ||a_u||=1 and the two anticommutator contributions total at most one. The sum has bound <=2n_C r(t), so the total dissipative action bound is 2n_C(rT+1). These are finite generator/accuracy budgets, not Hamiltonian energy norms for a bath. There are n_C separately addressed local reset channels; hardware parallelization and their ready reservoirs are supplied. Neither a controller's native timing nor microscopic bath energy follows from these coefficients.

## 6. Prepare the entry head while the complete H remains active

After the damping rate reaches zero, apply only the additional onsite Hamiltonian

    H_p(s)=Omega_p(s)(I-X_(v0)),
    Omega_p(s)=(pi/t_p)sin^2(pi s/t_p), 0<=s<=t_p,      (20)

and zero outside, for a finite t_p>0. H_p is positive semidefinite, continuously differentiable, supported on the existing head v_0, and requires no fresh transit or old-site relocation. Its scalar is part of the actual pulse. The scalar envelope Omega_p integrates to pi/2, so the comparison evolution generated by K+H_p is exactly U_K(t_p) tensor X_(v0) at its endpoint:

    exp[-i(pi/2)(I-X)]=e^(-i pi/2)(iX)=X.              (21)

It is not -iX with a discarded phase. During the pulse the comparison clock is e^(-iTheta(s))[cos Theta(s)|vac>+i sin Theta(s)|e>], where Theta(s)=integral_0^s Omega_p. Since H_app annihilates the vacuum and (4) is exact on every old state,

    ||H_app J_comparison(s)||=G_e |sin Theta(s)|<=G_e.

Duhamel between the actual K+H_app+H_p(s) and this comparison, on the entire bare old input map, therefore gives

    ||U_actual(t_p)J_vac-J_e U_K(t_p)||
       <=G_e integral_0^(t_p)|sin Theta(s)|ds<=G_e t_p. (22)

No factorization of the actual evolution or commutation of K with H_app has been assumed. Tensoring a passive reference and purifying converts (22) to a trace-norm channel allowance 2G_e t_p. For a pulse allowance epsilon_p>0, take

    0<t_p<=epsilon_p/(2G_e).                            (23)

The actual Hamiltonian peak, slope and integrated load of the added pulse are

    max||H_p||=2pi/t_p,
    max||dot H_p||=2pi^2/t_p^2,
    integral||H_p||ds=pi,
    integral||dot H_p||ds=4pi/t_p.                     (24)

Thus the sufficient equality choice in (23) has peak 4pi G_e/epsilon_p. A stipulated added onsite cap J_p must be at least that value for this particular prescription. This is not a necessary cap for every possible pulse design. The complete instantaneous norm is at most ||K||+B+2pi/t_p, with all pre-existing incident loads retained. Positivity of H_p and H_app does not make an arbitrary signed K positive; an already installed reserve, if any, remains included in K.

## 7. Complete finite-time preparation theorem and later time order

Let P_actual be reset (5), with (17)-(19), followed by pulse (20), with the same H installed throughout. Put t_0=t_r+t_p. For every initial sigma_DCR, define the target

    P_ideal(sigma)=U_K(t_0) sigma_DR U_K(t_0)*
                                      tensor |e><e|_C. (25)

Then

    ||P_actual(sigma)-P_ideal(sigma)||_1
       <=min(2,epsilon_r+2G_e t_p)
       <=min(2,epsilon_r+epsilon_p).                  (26)

Proof: (16)-(19) compare the reset output with vacuum appended to the freely aged old/reference marginal. Propagating that difference through the actual pulse contracts trace norm. Apply the complete prepared-map estimate (22) to that ideal reset output. This does not assume that the actual intermediate clock is clean or independent. The supremum over references has the same bound. The theorem requires the ready-domain input for the damping supplier, not for C.

This is preparation with explicit free aging, not the identity channel on D. The target deletes clock-held information while preserving the old/reference marginal under K. Initial clock/reference correlations may be transferred to the reservoir; their elimination everywhere or environmental privacy is not claimed. An old record physically stored in a qubit being reset cannot also be declared an untouched passive reference. Separate protected records may be included in R only if their passivity is actually supplied.

For example, composing with the parent's later word evolution for a duration t starts that theorem on U_K(t_0) sigma_DR U_K(t_0)*. Its old target is therefore

    U_K(t) W U_K(t_0) sigma_DR U_K(t_0)* W* U_K(t)*,    (27)

with the parent's entire time-indexed clock output retained and its error added by contraction. One cannot replace the unitary order by U_K(t+t_0)W when W and K do not commute. The newly prepared head immediately resumes its clock motion after the pulse. No permanent halt, stationary record, reader or second-use reservoir domain is supplied by (26).

All finite formulas give existence for finite real coefficients. A computable prescription additionally requires effective coefficient data and certified upper bounds for C_* and G_e (and timing/calibration data). No recurrence search, hidden diagonalization or numerical certificate has been performed here.

## 8. Calibration and domain errors

Suppose the actual implementation differs from the nominal one by a Hermitian residual E(t), rate deviations delta r_u(t) with the actual rates remaining nonnegative, and any further complete-generator discrepancy with certified bound d(t). Complete Duhamel contraction gives the additional allowance

    epsilon_impl <=2 integral_0^(t_0)||E(t)||dt
                 +2 sum_u integral_0^(t_0)|delta r_u(t)|dt
                 +integral_0^(t_0)d(t)dt.              (28)

An initial joint ready-domain error epsilon_ready adds by contraction, provided it is a complete input certificate for the actual supplier, including any declared correlations. Unknown initial bath correlations cannot simply be called a small reduced system error. The total right side of (26) increases by epsilon_impl+epsilon_ready and is capped at 2. The nominal number law and energy balance below need not hold exactly under arbitrary residuals; their exactness is not asserted for faults.

A pulse-envelope error delta Omega contributes at most 4integral|delta Omega| to (28), since ||I-X||=2. Rate or timing shifts require their actual integrated error or another complete certificate. The finite derivative bounds in (17),(24) expose the switching sensitivity; they are not an automatic physical calibration guarantee. Positivity, locality and a ready domain of an erroneous device are separate assumptions, not consequences of a scalar norm bound. No readout call or measurement postselection is hidden in (26).

## 9. Installed energy, scalar, moments and reservoir price

During nominal reset, the adjoint dissipator acts on the literal quadratic terms as

    sum_u D[a_u]^*(n_v)=-n_v,
    sum_u D[a_u]^*(a_v* a_w)=-a_v* a_w, v!=w,
    sum_u D[a_u]^*(K)=0.

Old coefficients commute with all new a_u. Consequently, even though [K,H_app] may be nonzero,

    d Tr[H rho(t)]/dt=-r(t) Tr[H_app rho(t)]<=0.        (29)

The Hamiltonian part commutes with the complete fixed H itself. The exact nonnegative decrease Q in the installed generator's ensemble mean is

    Q=integral_0^(t_r)r(t)Tr[H_app rho(t)]dt.

Let m_0=Tr[N sigma], eta_r=e^(-R(t_r)). From (3), H_app<=B(I-|vac><vac|)<=BN, and (8),

    delta m_0(1-eta_r)<=Q<=B m_0(1-eta_r).             (30)

These bounds are finite, although the upper bound can be conservative. A useful independent upper bound follows by centering K only in the estimate: for h>=||K-alpha I|| and epsilon_back=min(2,2C_*integral_0^(t_r)e^(-R(s)/2)ds),

    Q=Tr[H_app sigma]-Tr[H_app rho(t_r)]
                          +Tr[K sigma]-Tr[K rho(t_r)]
      <=Tr[H_app sigma]+h epsilon_back<=B+h epsilon_back. (31)

The old comparison marginal is exactly free evolution under K, so its mean K is unchanged and (12) proves the last disturbance bound. No physical energy origin has been removed.

Equation (29) is a precise property of the stipulated generator. It does not say each individual jump lowers the interacting total energy, that the bath satisfies detailed balance, that a zero-temperature physical bath automatically generates a_u with K present, or that the controller/reservoir costs equal Q. A microscopic identification of H with energy and a realization of (5) would have to account for those physical costs separately.

During the pulse the nominal dynamics is closed under H+H_p(s). Since H_p vanishes at both endpoints,

    Delta Tr[H rho]=integral_0^(t_p)Tr[dot H_p(s) rho(s)]ds,
    |Delta Tr[H rho]|<=4pi/t_p.                        (32)

This work allowance is charged; the positive scalar Omega_p(s)I is not discarded. Its integrated phase pi/2 is precisely the scalar in (21). The installed apparatus's original Pauli scalar B/2 and the complete original scalar/reserve are also retained. The cancellation making its vacuum energy zero is an operator property of (2), not a permission to delete the scalar from H.

At the ideal output (25), the exact moments of the same installed H are

    mean=Tr[K sigma_D]+alpha_0,
    variance=Var_(sigma_D)(K)+2Lambda|z_0|^2.           (33)

They follow from the parent's square compression and free aging under K, not from independence of the initial clock. For a total output trace allowance epsilon and beta>=||H-alpha I|| (for example beta=h+B),

    |actual mean-target mean|<=beta epsilon,
    |actual variance-target variance|<=3beta^2 epsilon. (34)

The variance estimate follows by bounding the centered second-moment difference by beta^2 epsilon and the difference of squared centered means by 2beta^2 epsilon. Thus fixed moment tolerances impose the corresponding additional preparation precision; a small trace error is not a resource-independent energy guarantee.

For the reference-valued linear records M_j^R(rho)=Tr_DC[((H-alpha I)^j tensor I_R)rho], j=1,2, duality similarly gives

    ||M_j^R(actual)-M_j^R(target)||_1<=beta^j epsilon.   (35)

Indeed pairing with any norm-one reference test operator gives an observable of norm at most beta^j on the complete output. Equation (35) is an operator-valued mathematical moment bound, not a physical energy reader or a nonlinear conditional-variance record. Its growing beta^j cost is explicit.

The damping supplier also requires entropy and information capacity. For the exact ideal replacement on n_C qubits, a unitary implementation with a pure ready environment and unchanged old marginal must transfer orthogonal clock basis inputs into mutually orthogonal environment outputs. Its environment then needs dimension at least 2^n_C. A maximally mixed independent clock transfers n_C log 2 entropy in that exact ideal case. This elementary statement explains the required sink; it is not a dimension lower bound proved here for this approximate finite-time realization and not a thermodynamic work formula. A canonical lowering-jump unravelling, if supplied, has at most n_C jumps and mean count m_0(1-eta_r); neither count certifies finite temporal memory or returns the bath to its ready state.

## 10. Literal resource boundary and failed alternatives

The installed Hamiltonian hardware remains exactly the parent's n_C=L+9 new qubits and L+14 added edges. Its whole-term added loads remain: Lambda at old q_0; 5Lambda/4+sqrt(Lambda)g_j at each a/a'; 3Lambda/2+sqrt(Lambda)|z_j| at each b/b'; and alpha_v plus all incident direct J_j and both magnitudes of every incident cell port at a head. At v_1 both cell contributions count. The pulse adds its onsite peak 2pi/t_p only at v_0. The installed full-generator norm is bounded by ||K||+B, with the pulse contribution added during preparation. The damping rates are a separate open-system resource, not silently counted as Hamiltonian couplings of norm r.

The extra suppliers are n_C addressed local reset channels at finite peak r and slope pi r^2/2, their ready reservoir, one onsite positive pulse with (24), and an external schedule/calibration over the common completion time t_0. The algebraic reset terms have local system support, but no finite ordinary-NN placement, norm, positivity or preparation cost of their microscopic reservoirs/controller has been derived. The required reservoir readiness is transferred to an explicitly named supplier; it has not vanished. Subsequent reuse needs renewed reservoir/controller domains. There is no common strength cap, efficiency, native preparation, classical-record, reader or autonomous-stop claim.

Several tempting stronger conclusions fail or remain unproved:

* **Number decay does not eliminate old-data backaction.** Start the literal clock in |b_0> with every other new site vacant. Its compression is <b_0|H_app|b_0>=Lambda(I+X_(q0)/4). Tracing the dissipator over C has zero initial contribution to the old marginal. Hence the old derivative, relative to free K at t=0, is -i(Lambda/4)[X_(q0),rho_D]. With q_0 initially |0_Z> and any product state on the other old factors its trace-norm derivative is Lambda/2, regardless of the finite initial damping rate. For a concrete allowed noncommuting old background one may keep K=lambda Z_(q0)Z_(q1)+omega Y_(q0) with lambda and omega nonzero; the comparison subtracts its unchanged free derivative. It refutes an exact zero-backaction shortcut; it is not a lower bound for all final reset times or all alternative interfaces.
* **A gap does not supply a damping model.** Positivity and vacuum silence establish none of the reservoir state, transition operator, spectral selectivity, detailed balance or native control hypotheses in (5).
* **An unchanged old state is the wrong time target.** Even at exact clock vacuum, keep K=lambda Z_(q0)Z_(q1)+omega Z_(q0), lambda!=0, on the occupied old edge, and start q_0 in |+> and q_1 in |0_Z>. The old trace distance from the unaged state is 2|sin((lambda+omega)t)|. Choose lambda+omega!=0. The correct channel preserves the freely aged marginal; retaining the old interaction does not remove this issue.
* **Population alone is insufficient.** A residual number estimate does not by itself prove the full replacement channel for correlated inputs. The explicit dilation calculation in (15) and the interacting backaction calculation in (12) do different jobs.
* **The reservoir cannot be omitted from an all-hardware claim.** The exact ideal erasure transfers clock information elsewhere. The generator (5) specifies reduced dynamics, not the state of every external factor. No complete retained-reservoir output or reversible all-hardware reset has been proved.
* **A full-norm-times-duration estimate is not an impossibility theorem.** It is valid but loses the decay used in (12). Conversely, the finite coefficient-over-rate bound is sufficient and does not prove that every acceptable reset needs rate proportional to B/epsilon.
* **Finite-clock preparation is not repeatability or reading.** The clock begins evolving immediately, its output is time-indexed, and no reader, record protection, reservoir reset or second-use domain follows without an additional proof.

No numerical scientific program was needed or run. The proof uses standard amplitude damping, explicit finite dilations, complete trace contraction and Duhamel, with their hypotheses shown here. Its specific contribution is the literal installed-apparatus application, coefficient count, correlated-input estimate and finite positive-pulse/resource composition. There is no priority claim for the generic machinery. All source-only executions, exposure limits and actual interruptions are recorded separately. This candidate awaits separate substantive review.

## Complete necessary reset-action proof; unchanged

# Exact number-sector laws and necessary reset action

Status: provisional conditional derivation, not independently checked or retained.
Author: root, same user-selected model and reasoning effort. No scientific program
has been executed. This concerns the supplied uniform-damping reset stage in the
complete source95fbc8dd, not arbitrary reset protocols or microscopic baths.

## 1. Domain and comparator

Let D be the original finite carrier, C consist of n>=1 qubits, and R be any
passive reference. Set a_u=|0><1|_u, n_u=a_u^*a_u and N=sum_u n_u. Let H be a
finite self-adjoint installed Hamiltonian with[H,N]=0 and vacuum compression K:
H J_0=J_0 K, where J_0 appends the all-zero clock. The literal boundary parentb3b6
and the reset candidate95fbc satisfy these hypotheses, including the complete
old K and apparatus. No sector norm is substituted for a whole-space norm.

Consider the actual reduced channel Phi_t generated by

    L_t(X)=-i[H,X]+r(t) sum_u (a_u X a_u^* - {n_u,X}/2),
    r(t)>=0, R_t=integral_0^t r(s) ds, eta_t=exp(-R_t).

Finite integrable rates suffice for the integral identities below; the earlier
C1 finite schedule is a special case. The supplied environment is initially in
the declared ready domain and traced. This is the same reduced-channel premise,
not a new Hamiltonian realization of the damping.

The comparison channel is complete clock replacement with the actual old aging:

    Q_t(X)= U_K(t) Tr_C(X) U_K(t)^* tensor |vac><vac|_C.

Tensor identities on R are implicit. Define delta_t=||Phi_t-Q_t||_diamond,
using the trace norm convention in which two channels have distance at most2.
The result is

    delta_t >= max{sqrt(eta_t), 2[1-(1-eta_t)^n]}.                 (1)

These are necessary prices for this stated channel family. They are neither a
sharp formula for its diamond distance nor a universal physical reset bound.

## 2. Exact population law despite interactions

For any function f on{0,...,n}, functional calculus and a_u lowering N by one give

    sum_u D[a_u]^*(f(N)) = N [f(N-1)-f(N)].                    (2)

The value f(-1) is immaterial because the N=0 factor vanishes. One direct proof
is a_u^* f(N) a_u=n_u f(N-1), while n_u commutes with f(N). The Hamiltonian
contribution vanishes because[H,N]=0; the old/clock interactions do not change
this identity. Thus, for p_k(t)=Tr(P_k rho(t)),

    p_k'(t)=r(t)[(k+1)p_(k+1)(t)-k p_k(t)],                   (3)

with p_(n+1)=0. This is a law for total-number sectors only. It does not assert
independent damping of actual site marginals or absence of old backaction.

For an initially fully occupied clock, p_n(0)=1. Solving the finite triangular
system, or substituting and checking the initial values, yields

    p_k(t)=binom(n,k) eta_t^k (1-eta_t)^(n-k).                (4)

The formula holds with arbitrary original old/reference state and the full
installed interactions. Uniqueness of the finite linear integral system gives
the conclusion also for integrable r. Endpoint cases eta=1 and the n=1 case
are interpreted by continuity or by their explicit polynomial values.

The target Q_t has vacuum probability1. The binary observation{P_0,I-P_0}
therefore bounds the complete trace distance for this allowed input below by

    2(1-p_0(t))=2[1-(1-eta_t)^n].                            (5)

This is merely a mathematical test operator for a norm bound, not a constructed
physical number detector. It proves the second term of(1). It does not use the
weaker mean-number estimate p_nonvac>=<N>/n.

## 3. Vacuum–one-excitation coherence

Let H_k denote the restriction to sector P_k. Choose any unit vectors x in P_1
and y in P_0, including original carrier factors, and the allowed pure input

    rho_0=|z><z|, z=(x+y)/sqrt(2).                           (6)

No reference is needed to witness this lower bound. The initial support lies
in sectors0 and1. The Hamiltonian preserves that support and every jump lowers
number; hence no sector2 or higher is ever populated. For the off-diagonal
block X_t=P_1 rho(t) P_0 the jump term is zero: a jump would need an incoming
P_2 rho P_1 block. The anticommutator contributes-r(t)X_t/2. Consequently

    X_t=(sqrt(eta_t)/2) exp(-itH_1)|x><y|exp(itH_0),
    ||X_t||_1=sqrt(eta_t)/2.                                (7)

This is an exact block identity, including all noncommuting old dynamics inside
H_1. It is not obtained by inserting comparator occupations into the actual
state. The vacuum-silent premise supplies H_0=K under J_0, but the norm equality
itself only needs unitary restrictions of the installed self-adjoint H.

The ideal Q_t(rho_0) has no P_1–P_0 block. Put x_t=exp(-itH_1)x and
y_t=exp(-itH_0)y. The Hermitian test

    F_t=|x_t><y_t|+|y_t><x_t|                                (8)

has operator norm1 because the two sectors are orthogonal. Its expectation on
Phi_t(rho_0)-Q_t(rho_0) is sqrt(eta_t): the diagonal blocks contribute zero and
the two conjugate off-diagonal contributions each equal sqrt(eta_t)/2. Trace
duality gives the first term of(1). In particular, exact number decay alone
does not remove this square-root-in-survival coherent contribution.

This construction uses an input superposition across clock-number sectors,
which is in the arbitrary-input domain of the reduced reset theorem. A
superselection rule or a preparation-domain restriction excluding that input
would be a changed premise and would require a different accuracy claim.

## 4. Necessary action and sufficient-schedule comparison

If delta_t<=epsilon with0<epsilon<1, equation(1) implies separately

    R_t >= 2 log(1/epsilon),                                (9)
    R_t >= -log[1-(1-epsilon/2)^(1/n)].                     (10)

The second logarithm has a strictly positive argument less than1. For fixed n,
its small-epsilon form is log(2n/epsilon)+O(epsilon); equation(9) gives the
stronger leading2log(1/epsilon) at fixed n. These two bounds are independent
necessary consequences, not a claim that their maximum is sufficient or sharp.

For the previously supplied C1 schedule, R_final=rT+1 and
T=(2/r)log(4sqrt(n)/epsilon_r). Thus its total action is

    R_final=2log(1/epsilon_r)+log(n)+2log(4)+1.               (11)

Its leading coefficient2 of log(1/epsilon_r) matches the necessary coherence
price at fixed n. This statement is only about total damping action in that
model. The separate backaction requirement r>=16C_*/epsilon_r, finite ramp
times, rate slopes and full supplier/controller costs are still required by
the sufficient theorem. No optimality for peak rate, elapsed time, physical
energy, n-dependence or microscopic hardware is established by(11).

A clock-number-diagonal input domain removes the particular witness(6), but
does not by itself remove old-data backaction or prove a stronger upper bound.
The full-occupation input and population law remain available if that domain
includes the fully occupied sector.

## 5. Entry pulse: a bounded consequence, not a new reset protocol

Let V_p be the actual later finite pulse unitary on D,C, with the installed H
still active, and let E_(t,p) denote the ideal channel that appends the declared
entry after old free evolution for t+t_p. The prior pulse comparison supplies

    ||Ad(V_p) Q_t - E_(t,p)||_diamond <= e_p,
    e_p=2G_e t_p                                             (12)

or any sharper independently established complete pulse allowance. The same
bound holds uniformly for the old marginal supplied by Q_t. Triangle inequality
and invariance of diamond distance under unitary output conjugation give

    ||Ad(V_p) Phi_t - E_(t,p)||_diamond
       >= max{0, max(sqrt(eta_t),2[1-(1-eta_t)^n])-e_p}.       (13)

Thus a claimed total accuracy epsilon entails max(...)<=epsilon+e_p, under
this stated pulse comparison. One cannot simply transfer(9) with epsilon in
place of the reset-stage error while ignoring the pulse allowance. Equation(13)
does not price a new reservoir or show that arbitrary driven protocols obey the
same restriction.

## 6. Scope and remaining checks

The exact sector/coherence laws use only the displayed finite uniform-damping
generator, excitation conservation and the explicit input domains. They do not
derive that generator from physical axioms, construct a local bath, define a
classical detector, or return any environment to readiness. All underlying
physical K/energy and preparation/control identifications remain supplied.

Before publication a separate assessor should check the full adjoint identity,
the absence of incoming jump blocks in the chosen0/1 domain, the trace witness,
the noncommuting-K and all-reference scope, and the unitary post-pulse inequality.
No numerical Lindblad sample was selected: it would not establish these general
domain statements. A specific algebraic uncertainty found by review may justify
one presealed decisive calculation. No broad or repeated controls are requested.
