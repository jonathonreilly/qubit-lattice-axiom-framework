---
title: Dyadic auxiliary-number filtering with conditional moments and ordinary-neighbor routing
claim_id: dyadic_auxiliary_number_filter_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: complete supplied filter instrument with restricted phase errors, three distinct scalar-moment contracts, returned dirty transit and separately priced persistent-background control error
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: finite conditional operator and moment estimates with explicit preparation, control and readout premises; selected controls do not establish native physical realization
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["multi_port_preparation_energy_moments_bounded_theorem_note_2026-10-14", "chain_preparation_moment_scaling_bounded_theorem_note_2026-10-14"]
runner: scripts/dyadic_auxiliary_number_filter_2026_10_14.py
next_trace_action: exact source/runner integration, regular review PR and later independent retained audit
---

Claim type: bounded_theorem

# Dyadic auxiliary-number filtering on the installed chain

**Conditional research milestone; no retained audit or native apparatus claim.** This note binds an explicit complete measurement instrument to the same installed multi-port generator and the accepted restricted-chain coordinates. It retains every outcome, arbitrary old/reference correlations, all success denominators, the coupling-variance baseline and the costs of the supplied control apparatus. The four complete arguments below retain their original status/exposure wording. Their exact identities, review disposition and execution records are in the accompanying packet. A source freeze is provenance, not a mathematical verdict.

The mathematical parents are [preparation moments and the complete chain premise](MULTI_PORT_PREPARATION_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-14.md), canonical9cfc7b47 with complete sharper bodyde7e7916 and placement79d2388a, and [chain moment scaling](CHAIN_PREPARATION_MOMENT_SCALING_BOUNDED_THEOREM_NOTE_2026-10-14.md), canonical883e0c0a. The first parent supplies the actual operator K, four auxiliaries per cell, full-state block estimates and unchanged old H. The second supplies the explicit norm/power constants reused in the new sufficient tolerances. Neither branch ancestry nor another filter's success projector supplies an additional theorem premise. No other open PR is imported.

For n=4M auxiliary qubits, let N be their total occupation, P its vacuum projector, and k=ceil(log2(n+1)). Supply k independent clean pointers, their stated preparations, addressed controlled phases and a terminal X instrument. With theta_j=2pi/2^(j+1), the complete Kraus family is

    F_b = product_j [I + (-1)^b_j exp(i theta_j N)]/2.

Its all-plus operator is exactly P: each positive occupation h has an odd multiple of pi at j=v2(h). The nonselective output is sum_h Pi_h sigma Pi_h. Accordingly, the aggregated failure channel is sum_(h>=1) Pi_h sigma Pi_h, which generally differs from Q sigma Q. Keeping the same success projector does not make these two complete instruments interchangeable. Fine X outcomes are retained, and are not individually identified with number-projective outcomes.

The structured error family is exactly exp(i(theta_j+e_ju)n_u n_Fj), with fixed real certified |e_ju|<=delta and exact pointer preparation, routing and readout. The successful nonvacuum amplitude is at most min(1,n delta/2); occupation-one and occupation-two amplitudes are separately at most delta/2 and delta. Vacuum success is exact. Every occupation probability and the nonselective old/reference marginal are preserved, even with inhomogeneous angle errors; within-number coherences can change. These statements do not cover arbitrary gate noise, imperfect SWAPs, uncontrolled Hamiltonian drift or a faulty reader.

For input vacuum mass p and false-success mass t, the actual successful probability is s=p+t. Conditional nonvacuum weight is t/s, and all normalization uses this actual s. Coherent P-Q terms can contribute linearly in the angle error to energy moments although false-success population is quadratic. The source-exposed comparison supplies an analytic one-cell witness, and the selected control preserves a nonzero P-Q moment discriminator. Neither ignoring the retained failure outcomes nor replacing the successful state by its vacuum block is an allowed simplification.

## Three different sufficient moment contracts

Within each fixed-M comparison, the installed generator K_M is unchanged: K=H+cI+Delta L+sqrt(Delta)V. Its scalar c, fixed old H, and vacuum variance term Delta*kappa remain. In the chain design Delta=D M^6, assume ||H||<=hM and a fixed per-port coefficient bound. The following are sufficient simultaneous **scalar** mean/variance prescriptions with explicit positive tolerance constants in the complete bodies. None is claimed necessary or optimal. The local defect is a bound on each auxiliary occupation; no independence between cells is used.

| Output and target | Old/reference input error | Initial local occupation | Per-phase error | Additional premise |
| --- | --- | --- | --- | --- |
| All outcomes retained, scalar moments against the intended old state plus the installed vacuum baseline | O(M^-2) | O(M^-14) | O(M^-3) | Exact structured phase family; this does not remove unconditional population |
| Normalized all-plus output, scalar moments against the intended old state plus the same baseline | O(M^-2) | O(M^-3) | O(M^-17/2) | Explicit constants ensure initial vacuum mass and success at least3/4 |
| Normalized all-plus output, scalar moments against its own ideal conditional vacuum state rho_P plus the same baseline | No intended-state closeness supplied by this contract | No initial small-defect assumption | O(M^-11) | A supplied positive vacuum-mass floor p>=p0 |

The last row does not certify closeness to an independently intended old state. The first row controls scalar moments of the unconditioned physical output, with the record retained as an identity factor in K; it is not an arbitrary record-valued cancellation theorem. The complete independent derivation also gives mean-only alternatives. These are separate statements, rather than three estimates of a single accuracy requirement.

The root supplement explicitly allocates successful/intended-state mean tolerance m_tol and variance tolerance v_tol. It chooses t=min(m_tol,sqrt(v_tol/2)), C=min(1,t/(3h),v_tol/(24h^2)) with the stated zero-h convention, then epsilon=C/(2M^2) and local nu=C/(16M^3). The residual phase constant is chosen from four displayed positive constraints. The result has E1<=t and E2<=v_tol/2, so E2+E1^2<=v_tol and success>=3/4. The scalar conclusion includes the existing Delta*kappa baseline rather than bounding that baseline by a constant.

The reference-valued distinction is material. A centered second-moment operator can additionally pay Delta*kappa times a reference-marginal discrepancy; raw first/second moments retain the associated scalar/reserve costs. Arbitrary observables of the newly created outcome record require their own full output-marginal contract. Scalar mean/variance estimates alone supply neither that contract nor a physical energy measurement.

## Concrete ordinary-neighbor layout and persistent background

Keep every original chain coordinate and H summand fixed. Supply the finite box {0,...,M+k} x {0,...,4} x {0,...,3}, with exactly k pointers at (M+1+j,3,3); the added region carries an identity extension of K. Its total size is20(M+k+1), including11(M+1)+20k new factors. Apart from the pointers, the added transit may be arbitrary and entangled with old factors or a passive reference. This is an availability/isolation premise for the specified region, not a way to clear an occupied lattice or act through an ineligible permanent Record.

Each pointer travels along the explicit corridor/stem path to the neighbor of one auxiliary; a phase gate is applied there and every SWAP is reversed. The full operator identity T* exp(i phi n_v n_u) T=exp(i phi n_F n_u) returns all transit, including its arbitrary correlations. All routes are serial. With chi_M=1 for M mod4 in{2,3}, the exact counts are

    W_swap = 4k[M^2+Mk+11M-2chi_M],
    N_phase = 4Mk,
    A_c = pi W_swap + 8pi M(1-2^-k) + E_angle + k pi/4.

There are also k plus preparations and k supplied X reads. The physical controls are signed one-/two-site Hermitian terms of norm at most Jc, with the displayed scalar and one-site contributions retained. Their coherent serial time is T_c=A_c/Jc. Initialization, readout, switching and idle time require their actual separate contracts. Only the added controls are certified nearest-neighbor if the supplied H itself has longer-range terms.

Exact net SWAP/phase gates give the precise structured-error instrument. If instead the unchanged K remains on during additive pulses, the full output differs from that comparator by at most min(2,2 beta_M T_c), where beta_M bounds the **whole** installed ||K||, including its scalar and reserve. Generic residuals, preparation and reader errors are charged separately in the complete error epsilon_gen. This bound covers all old/transit/reference factors and all outcomes; exact transit return and vacuum immunity then belong to the comparator, with the actual result only approximate.

For the full normalized outputs, generic error adds at most beta_M epsilon_gen to the scalar mean bound and3 beta_M^2 epsilon_gen to the variance bound. If beta_M<=C_beta M^7, the sufficient epsilon_gen=O(M^-14) costs Jc=O(M^23 log M) under this particular serial fast-pulse estimate. A fixed-output trace tolerance instead permits O(M^9 log M). The reserve-growth hypothesis and all constants are explicit. These are finite conditional resource prices, not a fixed-cap result or optimal rates. Their failure under a chosen cap proves no impossibility. Successful-branch perturbations additionally require a success floor and normalization; the unconditional bound cannot simply be applied to a rare normalized output.

An exact finite-duration reader confined to the new pointers/apparatus commutes with K on the old/auxiliary carrier. Its comparison target may include the known free aging. K moments are then invariant, but vacuum population need not remain zero. If an undelayed state is the target, the elapsed background evolution must be paid. No physical reader, pure apparatus, permanent Record, reset, timing law or conserved controller energy is constructed here.

## Evidence, attribution and review boundary

The full root argument252836f4 was frozen before the independent result0e75e69e was exposed to root. Both share the same model family and already accepted mathematical premises. The subsequent comparisoncf3c7ebd, constants review5a6cb94e and separate layout check are source-exposed checks; they are not blind or model-diverse evidence. The layout86f5b54d is an author extension of the independent filter proof. Its precheck argument, residue-row drafting correction and exact final scope-clarification diff are preserved.

The original selected floating n=4 control compares explicit pointer evolution with the product Kraus formulas, retains every outcome, uses the literal noncommuting one-cell K and a passive reference, and checks population/marginal/moment inequalities. Its rejected alternatives are binary-Q failure, an omitted phase row and omission of successful P-Q coherence. It is a selected finite check, not a proof of all-M inequalities or apparatus performance.

The separate presealed integer/Fraction M=5 layout control emits every path and physical gate:2100 SWAPs,100 phases and five pointer preparations. It checks complete label return and logical phase operands. Deleting one reverse SWAP leaves a pointer/transit exchange and19 wrong phase labels; its analytic Bell-transit witness has false-negative probability1/2. No2^220-dimensional amplitude computation or active-K dynamics simulation is claimed. The all-state routing identity and all-M formulas are proved analytically. The canonical runner binds complete original evidence and executes only these two stated finite controls; its actual cache records that execution separately from the earlier runs.

Controlled phase tests, Fourier products and repeated postselected products are established machinery. Primary attribution is to [Kitaev's eigenvalue-measurement construction](https://arxiv.org/pdf/quant-ph/9511026v1), [Cleve, Ekert, Macchiavello and Mosca's phase-estimation analysis](https://arxiv.org/pdf/quant-ph/9708016v1), and [Choi et al.'s Rodeo filter](https://arxiv.org/pdf/2009.04092v3). The bounded literature report records exact inspected sections and limits. No claim of priority for the abstract filter, random-time performance, generalized phase-noise robustness, or an exhaustive literature search is made. The new claim is the explicit mediator/chain, error, normalization, moment and resource binding on the stated supplied domain.

Canonical source identities, complete-body intervals, all original artifacts and exact current parent clauses are bound by the runner manifest. Historical provisional wording remains within preserved bodies; later review records explain current disposition. Actual canonical output is separate from immutable source inputs. Publication changes no editable prompt, physical axiom, audit verdict or source parent. Full integrated-current-main landing checks and independent retained audit remain separate gates; publication does not mark them complete.

## Complete root selected-output derivation

# Provisional dyadic population-preserving preparation filter

Root construction and bounds, 2026-10-14. This is an unaccepted second route,
separate from the one-clean-pointer binary instrument. The mechanism (but no
error/scaling answer) was sent to endpoint_precision_recovery. Its new output
has not been read. The earlier independent vacuum-conditioning result 1ffd740f
has been read; the exact mixture and same-K identities below reuse that result.
Existing phase-estimation/filter machinery is not claimed novel. A primary
literature check and independent proof comparison are pending.

## 1. Exact complete instrument

Let n=4M, N=sum_u n_u and k=ceil(log2(n+1)), so 2^k>n. Supply k initially
pure, unrecorded pointers. For j=0,...,k-1 prepare pointer j in |+>, apply
controlled exp(i theta_j N), theta_j=2pi/2^(j+1), then measure it in X.
Each controlled unitary is a product of n commuting addressed diagonal gates
exp(i theta_j n_u n_Fj). Retain every k-bit outcome r, and stop operating each
recorded pointer. The exact complete Kraus family on the auxiliary system is

    A_r = product_j [I+(-1)^r_j exp(i theta_j N)]/2.

The operators commute. For each j the two squared Kraus magnitudes add to I;
therefore sum_r A_r^* A_r=I. This is the complete supplied instrument, with
identities on all old factors and arbitrary reference. All-plus is r=0.

For an integer weight w in 1,...,n, write w=2^j times an odd integer. Then
j<=k-1 and exp(i theta_j w)=-1, so A_0 vanishes on that weight. At w=0 all
factors are one. Consequently A_0=P_B exactly. Successful state, success
probability p, old/reference disturbance and scalar moments equal the ideal
vacuum-pass formulas already derived. This does NOT give binary Lüders Q on
aggregated failure: the failure records can resolve more about the input.
The comparison instrument must retain these actual branches, not replace them
by Q sigma Q. Fine failure information and all consumed pointers remain paid.

At the addressed-gate level this uses nk diagonal two-qubit gates, 2k Hadamard
gates if X read is realized by H then supplied Z read, k terminal events, and
k clean pointers. There is no reset or reuse. Addressability, frame, net drift
removal, clock, pointer purity and the complete readout remain supplied.
Ordinary-neighbor routing and its errors require a separate actual binding.

## 2. Restricted diagonal angle errors

For this section only, replace each controlled phase by

    exp(i (theta_j+e_ju) n_u n_Fj), |e_ju|<=delta,

and keep all other operations, pointer preparation, stopping and readout exact.
This is a structured coherent error family, not a bound on arbitrary faulty
gates, memory-bearing noise or readout. If routing is used, exact swaps are
additional premises until their full errors are charged separately.

For a computational word z of weight w define

    a_z=product_j [1+exp(i(theta_j w+sum_u e_ju z_u))]/2.

The actual all-plus operator A is diagonal, a_0=1, and |a_z|<=1. For the j
chosen by the two-adic valuation of w, the factor that ideally vanished now
has modulus |sin(sum e_ju z_u/2)|. Thus on the weight-w sector

    ||A Pi_w|| <= r_w := min(1,w delta/2),       w>=1.

In particular A=P+A_Q, ||A_Q||<=r_n. The operation never generates a new
auxiliary computational population from a different input word, even though
it can retain P-Q coherence. This distinction is essential for moment bounds.

For arbitrary initial sigma let p=Tr P sigma, q=1-p, eta=Tr N sigma, and let
epsilon bound its complete old/reference marginal error to rho. Actual
success has weight s=p+q_A, q_A=Tr A_Q sigma A_Q^*, with

    0<=q_A<=r_n^2 q,   p<=s<=1.

When p>0 the normalized successful sigma'=A sigma A^*/s is defined. Its
vacuum leakage is q'=q_A/s<=r_n^2 q/p. Moreover

    eta'=Tr N sigma' <= r_n^2 eta/p.

Partial trace over B removes all off-diagonal word pairs. The full old/reference
input marginal is the convex mixture of the actual successful marginal and
the aggregate failed marginal. The weight of all failed outcomes is 1-s<=q.
Therefore the actual successful old/reference marginal tau' satisfies

    ||tau'-rho||_1 <= e := min(2,epsilon+2q).

No approximation of sigma by a diagonal state was made. The global output
still contains coherent P-Q blocks unless the physical input or operation
removes them. Full probability information is not an instrument certificate.

## 3. Same-K moment estimates using the excitation sectors

Import the complete de7 source de7e79161faf1c35941285c9670e9cc421f798c51204da139575c36870ab9976
and unchanged chain source 79d2388a, with its actual K=H+c+Delta L+sqrt(Delta)V.
The exact successful-state comparison is to J rho J* for this identical K.
Put h0>=||H||, m0=Tr rho H, D_old=H-m0, d>=||D_old|| (d<=2h0 can be chosen),
and retain kappa, kappa2, v, ell1=(9+sqrt(5))/8 from de7. The scalar and the
baseline Delta*kappa remain present in the actual moments.

The parent's L preserves total auxiliary excitation number and satisfies
0<=L<=3N/2; the latter also follows directly by summing the sharper bound on
eta_a,eta_b. Hence u'=Tr sigma' L<=3 eta'/2. A sufficient first-moment bound is

    E1 = h0 e + Delta u' + 2 sqrt(Delta*kappa*eta').

This is de7's first bound evaluated on the actual successful state; its
full old/reference marginal certificate has just been supplied above.

For the centered-square P-Q column define

    B1=Pi_1 (K-mean_0 K)^2 J,
    B2=Pi_2 (K-mean_0 K)^2 J.

There are no other excitation sectors in this column. H and L preserve N;
V changes it by one. From the de7 column argument,

    ||B1|| <= gamma1=sqrt(Delta*kappa)(2d+Delta*ell1),
    ||B2|| <= gamma2=Delta*sqrt(kappa2).

Since A is diagonal and preserves N,

    ||A_Q^*(B1+B2)|| <= Gamma_delta
       := sqrt(r_1^2 gamma1^2+r_2^2 gamma2^2).

The squared norm bound follows from the orthogonal one- and two-excitation
output sectors after A_Q^*, using the two operator norm bounds separately.
Positivity gives ||P sigma Q||_1<=sqrt(pq). In the normalized actual success
state, the complete P-Q centered-second contribution is consequently bounded by

    2 Gamma_delta sqrt(pq)/s <= 2 Gamma_delta sqrt(q/p).

This is more informative than replacing every nonvacuum amplitude by r_n.
The remaining Q-Q terms may safely use the parent's complete upper expression

    RQ(p',u') = 4M Delta^2 u' + Delta c_v p'
             + 2Delta(d+sqrt(Delta)v)sqrt(4M p' u')
             + 2sqrt(Delta)d v p',
    c_v=max(kappa,v^2-kappa),     p'=q'.

Thus one sufficient centered-second allowance is

    E2 = d^2 e + 2 Gamma_delta sqrt(q/p) + RQ(q',u'),
    -E2-E1^2 <= Var_(sigma')(K)-Var_(JrhoJ*)(K) <= E2.

Every P-Q and Q-Q contribution is retained. These expressions require an
independent source/proof check before acceptance. In particular the use of the
weight-sector bounds on the full centered-square column is load-bearing.

## 4. Provisional sufficient chain exponents and constants to allocate

Use Delta=D M^6, h0<=hM, kappa<=kappa0 M, v<=v0 M and
kappa2<=2 kappa0^2 M^2. Supply epsilon<=c_e M^-2 and each local defect
nu<=c_n M^-3 with 0<c_n<1/4. Then

    q<=eta<=4c_n M^-2, p>=p0:=1-4c_n>0,
    e<=(c_e+8c_n)M^-2,
    q'<=A_M, eta'<=A_M, u'<=3A_M/2,
    A_M:=16 c_n delta^2/p0.

The use of r_n<=n delta/2 makes these bounds valid even if the displayed
upper bound exceeds one. Under the final small-error design they decrease.

Because r_1<=delta/2 and r_2<=delta,

    Gamma_delta <= delta G1 M^(19/2),
    G1=sqrt[D*kappa0*(4h+D*ell1)^2/4 + 2D^2*kappa0^2].

Both cross-column exponents and the entire subleading two-flip term are bounded
using M>=1. With the accepted chain coefficient Q0 (not a new constant), the
same algebra as its RQ estimate gives RQ<=Q0 M^13 A_M. Thus

    E1 <= h(c_e+8c_n)/M
       +24D c_n delta^2 M^6/p0
       +8 sqrt(D*kappa0*c_n/p0) delta M^(7/2),
    E2 <=4h^2(c_e+8c_n)
       +4G1 sqrt(c_n/p0) delta M^(17/2)
       +16Q0 c_n delta^2 M^13/p0.

In particular delta<=c_delta M^(-17/2), with c_e,c_n,c_delta sufficiently
small for the required tolerances, is a provisional sufficient simultaneous
scalar design under this restricted error model. No optimality is claimed.
The constant allocation must include E1^2 and the already displayed baseline,
success and marginal conditions; big-O notation alone is not a tolerance.
This does not replace a generic full-instrument error allowance, suppress
readout mistakes, or price imperfect routing. Those remain separate contracts.

## 5. Open obligations

Independently check the exact multi-outcome instrument, diagonal error model,
one/two-excitation column calculation, constants, and useful discriminators.
Read primary literature to distinguish standard filter/phase-estimation
machinery from this particular physical-resource application. Supply a concrete
ordinary-neighbor layout if the route is selected for publication. Charge
pointer purity, failed records, the unchanged background, actual gate errors
outside the diagonal model, readout duration/calibration and renewed attempts.
Reference-valued moments retain the previously shown conditional reference
and installed-scalar terms. No physical axiom, prompt or canonical source has
been changed, and this unfinished route is not an accepted theorem or PR.

## Complete explicit successful-output tolerance allocation

# Explicit constants for the proposed successful-branch dyadic bound

This is an author-side completion of the constant allocation left open in the root argument at SHA256 `252836f496963d3410d0d77369a85dd11c7f98990475d11fb5406d957bdbf973`. It introduces no new error family or physical operation. It was written after reading the independently sealed argument `0e75e69e` and source-exposed comparison `cf3c7ebd`; it is not a pre-exposure independent derivation. The earlier source remains unchanged. Separate review of this allocation is pending.

Fix positive desired scalar mean and variance errors m_tol and v_tol. Take M>=1, the same installed mediator K, Delta=D M^6 with D>0, ||H||<=hM with h>=0, and a positive certified upper bound Lambda on the absolute port coefficients. Lambda may be chosen positive even when the actual coefficients vanish. Set

    kappa0=209 Lambda/16,
    v0=4 sqrt(209 Lambda/64),
    l1=(9+sqrt(5))/8,
    G1=sqrt(D kappa0(4h+D l1)^2/4 + 2D^2 kappa0^2),
    Q0=6D^2+D max(kappa0,v0^2)+4 sqrt(6) D h
             +2 sqrt(6) D^(3/2) v0+4h v0 sqrt(D).

Q0 is exactly the accepted chain population coefficient in the canonical chain note `883e0c0ad7d31fc039de0d895fb586818c2562150acef528fb4c79c784f9441b`, not a freely adjustable constant. The complete de7 source supplies the centered-square vacuum column and Q-Q estimate. All comparisons retain the same scalar reserve c and baseline Delta*kappa.

Let

    t=min(m_tol,sqrt(v_tol/2)),
    C=min(1,t/(3h),v_tol/(24h^2)),
    c_e=C/2,       c_n=C/16,       p0=1-4c_n.

For h=0, interpret the two quotients with zero denominator as positive infinity. Thus C>0, c_n<=1/16 and p0>=3/4. Require the complete initial old/reference marginal to satisfy epsilon<=c_e M^-2 and every designated auxiliary population to satisfy nu_u<=c_n M^-3. No independence between factors is assumed. Then

    q<=eta<=4c_n M^-2,
    p=1-q>=p0,
    epsilon+2q <= (c_e+8c_n) M^-2 = C M^-2.

Here p is the initial vacuum mass, not de7's nonvacuum notation. The successful actual filter probability s obeys s>=p under precisely the stated diagonal phase-error model. This is a conditional probability theorem about a supplied instrument and preparation certificate, not an empirical confidence bound.

Define four positive constants

    a1=24D c_n/p0,
    a2=8 sqrt(D kappa0 c_n/p0),
    b1=4G1 sqrt(c_n/p0),
    b2=16Q0 c_n/p0.

Choose

    c_phi=min(1, sqrt(t/(3a1)), t/(3a2),
                  v_tol/(6b1), sqrt(v_tol/(6b2))),
    delta_M=c_phi M^(-17/2),

and require every actual controlled phase to be exactly

    exp(i(theta_j+e_ju) n_u n_Fj),    |e_ju|<=delta_M.

Pointers, X readings and the other logical operations are exact at this stage. No off-axis, imperfect-SWAP, control-background, preparation or readout fault is included in e_ju. Any implementation of this logical contract must state its separate residual-error allowance.

The root's sector-sensitive estimates give, for the normalized actual all-plus output and the separately intended old/reference target rho,

    |mean_+ K-[Tr(rho H)+c]| <= E1,
    -E2-E1^2 <= Var_+ K-[Var_rho(H)+Delta*kappa] <= E2,

with the following sufficient bounds after the displayed substitutions:

    E1 <= h C M^-1 + a1 c_phi^2 M^-11 + a2 c_phi M^-5,
    E2 <= 4h^2 C + b1 c_phi + b2 c_phi^2 M^-4.

The first line follows from the original terms h(c_e+8c_n)/M, (24D c_n/p0) delta_M^2 M^6 and 8sqrt(D kappa0 c_n/p0) delta_M M^(7/2). The second follows from 4h^2(c_e+8c_n), 4G1 sqrt(c_n/p0) delta_M M^(17/2) and (16Q0 c_n/p0) delta_M^2 M^13. This displays every residual power rather than treating big-O notation as a tolerance.

Since M>=1, the choices of C and c_phi make the three mean terms at most t/3 each, and the three E2 terms at most v_tol/6 each. Consequently

    E1<=t<=m_tol,
    E2+E1^2<=v_tol/2+t^2<=v_tol.

This proves the explicit sufficient scalar tolerances uniformly in the finite chain family, subject to the inherited dynamical requirement on D and all stated input/instrument premises. The actual success probability is at least3/4. The failed outcomes remain in the complete instrument and are not certified by these successful-branch bounds. The all-outcome ensemble still preserves its initial occupation populations.

This result does not replace the distinct retained-outcome allocation in independent equations(19)-(20), or its different comparison to rho_P with only a vacuum-mass floor. The exponent17/2 is sufficient and is not proved necessary or optimal. No claim about reference-valued moments follows by dropping their Delta*kappa reference term, and no arbitrary-reserve physical raw-second-moment tolerance follows from scalar variance alone. Native pointer preparation, controls, drift handling, readable Records, energy identification and reset remain open.

The allocation is a finite chain of inequalities; no scientific program or new numerical test has been executed for this supplement. All source constants and scope have been displayed for a narrow independent review.

## Complete independent instrument and moment derivation

# A population-preserving dyadic auxiliary filter with its complete outcome record

**Proposed conditional finite result; separate review pending.** Root supplied the mechanism and the diagonal angle-error class, but no derived error or scaling conclusion. The calculations below were made before any root candidate/result exposure. Earlier work on the same mediator and preparation sources is disclosed in SOURCE_PINS.json; this is not blind or model-diverse research. The controlled-phase/Fourier filter, Kraus calculus, purification and moment inequalities are established machinery. No generic priority, native apparatus, optimality or physical-energy identification is claimed.

The input is an arbitrary normalized state sigma on D B R, with n=4M specified auxiliary qubits B, M>=1, and arbitrary finite passive reference R. All original dirty/spectator factors are part of D. Set

    N=sum_u n_u,   n_u=|1><1|_u,   k=ceil(log2(n+1)),   Lc=2^k>n,
    P=I_DR tensor |0^n><0^n|,   Q=I-P,
    theta_j=2*pi/2^(j+1), j=0,...,k-1.

Supply k initially independent clean pointer qubits, their exact plus preparation, the addressed controlled phases, exact X instruments, and no drift during this filter. Every outcome is retained. These are engineering premises; they are not supplied by a probability formula. Same-K moment comparisons below evaluate one identical installed mediator K on two states and its subsequent free evolution. They do not implement the filter while that K remains active.

## 1. Complete ideal instrument, not a binary-Lueders substitution

For pointer j, the exact controlled unitary is I on its zero branch and D_j=exp(i theta_j N) on its one branch. On a prepared plus pointer its X-outcome b_j in {0,1} has Kraus operator

    A_(j,b_j)=(I+(-1)^b_j D_j)/2.

All D_j commute. Thus for the complete outcome b in {0,1}^k,

    F_b=product_j A_(j,b_j),
    I_b(sigma)=F_b sigma F_b*,
    Omega(sigma)=sum_b |b><b|_C tensor I_b(sigma).                 (1)

Identities on D,R are implicit. If the measured pointers are retained, append their product X-eigenstate |x_b><x_b| to block b. Before the supplied read, the full map is the coherent isometry sum_b |x_b>_F tensor F_b. The classical record in (1) describes the supplied instrument, not a derived occurrence/Record law. Because sum_bj A_jbj* A_jbj=I and all factors commute, sum_b F_b* F_b=I. Both coherence and all unnormalized blocks, including every failure, are specified for arbitrary D B R.

The all-plus operator is exactly P. On occupation number h,

    f_+(h)=2^-k product_j(1+exp(2*pi*i*h/2^(j+1)))
           =Lc^-1 sum_(r=0)^(Lc-1) exp(2*pi*i*r*h/Lc).           (2)

The product identity follows by expanding product_(r=0)^(k-1)(1+z^(2^r)); all powers 0,...,Lc-1 occur once. Since 0<=h<=n<Lc, (2) is one at h=0 and zero otherwise. Equivalently, for h>0 the factor j=v_2(h) is zero. Therefore I_+(sigma)=P sigma P, and every other F_b annihilates P.

After forgetting the outcome label, the channel is

    E(sigma)=Lc^-1 sum_(r=0)^(Lc-1) exp(2*pi*i*r*N/Lc)
                          sigma exp(-2*pi*i*r*N/Lc)
            =sum_(h=0)^n Pi_h sigma Pi_h,                         (3)

where Pi_h is the total-number projector. The first equality comes from independently averaging Ad(D_j) or Id; the second uses the same geometric sum on h-h'. Hence the aggregated failure map is

    sum_(b!=+) I_b(sigma)=sum_(h=1)^n Pi_h sigma Pi_h,             (4)

which is generally NOT Q sigma Q. A coherent superposition of number one and number two, already wholly in Q, loses its cross term in (4), whereas binary Lueders failure would retain it. Within one fixed h the ideal filter is scalar and preserves all old/reference and auxiliary-degeneracy coherence. Individual failure outcomes need not resolve h; some conditional failure states retain coherence between different nonzero h even though their sum is (4). No claim that the whole fine record is merely a binary flag is made.

Every Kraus operator is diagonal in the auxiliary occupation basis. Thus no branch moves population between occupation words; conditional normalization can reweight those words. Unconditionally every occupation probability, q=Tr(Q sigma), eta=Tr(N sigma), and every local delta_u=Tr(n_u sigma) is preserved exactly. The complete old/reference marginal tau=Tr_B sigma is also preserved exactly by this local trace-preserving channel. This is not an excitation-removal map if failures are kept.

## 2. The declared structured phase errors

Fix real errors e_ju with certified |e_ju|<=d_ju. The actual two-qubit gates are precisely

    exp(i(theta_j+e_ju) n_u n_Fj).

There are no axis, pointer-state, readout, extra coupling, drift or timing errors outside those already represented by these phases. For occupation word z, define h=|z| and

    E_j(z)=sum_u e_ju z_u,
    phi_j(z)=theta_j h+E_j(z),
    f_b(z)=product_j [1+(-1)^b_j exp(i phi_j(z))]/2.             (5)

The actual F_b are the diagonal operators with these entries. Equation (1), with these F_b, is the complete actual instrument; its completeness and population/old-marginal preservation are exact. Its nonselective Schur multiplier is

    [E_e(sigma)]_(z,z') = sigma_(z,z')
             product_j [1+exp(i(phi_j(z)-phi_j(z')))]/2.         (6)

Blocks sigma_(z,z') are operators on D R. Formula (6) need not equal exact number pinching and can also dephase within a fixed h when errors vary across u.

Since phi_j(0)=0 exactly, F_+P=P and F_bP=0 for every b!=+. A true auxiliary vacuum never fails or acquires excitations in this error model. This is a structural property, not a generic apparatus robustness claim. Let F=F_+=P+F_Q and define alpha=||F_Q||. A computable certificate is

    alpha<=alpha_bar:=max_(1<=h<=n) min{1,
                      (1/2) sum of the h largest d_(v_2(h),u)}.
                                                                    (7)

Indeed the factor j=v_2(h) has modulus |sin(E_j(z)/2)|, bounded by half the indicated error sum, and all other factors have modulus at most one. A simpler certificate is alpha_bar<=min(1,(1/2)max_j sum_u d_ju). If d_ju<=delta, then alpha<=min(1,n delta/2).

This n factor cannot be uniformly removed from this particular worst-case certificate: when n is a power of two, put errors delta on every gate of row j=log2(n), all other errors zero, and take the all-occupied word. Every other success factor is one and |f_+(Full)|=|sin(n delta/2)|. This is a finite allowed error/input family, not a necessity theorem for every state or calibration architecture.

For the full instrument, put E_tot=sum_ju d_ju. All controlled errors commute on B F. The joint implemented unitary differs from the ideal one by an operator of norm at most min(2,E_tot), since its error generator is sum_ju e_ju n_u n_Fj. Preparing the pointers and applying the same exact X instruments are contractions. Consequently

    ||Omega_e(sigma)-Omega_0(sigma)||_1<=min(2,2E_tot)          (8)

uniformly over all inputs and passive references, with the full outcome record and the retained postmeasurement pointers if desired. This is closeness to the IDEAL MULTI-OUTCOME FILTER, not to binary Lueders failure or to an always-clean preparation. No archive/program is traced out to manufacture a stronger channel.

## 3. Success, false acceptance, conditional states and unchanged failures

Let a=Tr(P sigma)=1-q and

    t=Tr(F_Q sigma F_Q*),   s=Pr(plus)=a+t.

Then, exactly and for any correlations,

    0<=t<=alpha^2 q,   a<=s<=a+alpha^2 q,
    Tr(Q sigma_+)=q_+=t/s,
    eta_+=Tr(N F_Q sigma F_Q*)/s<=alpha^2 eta/s,              (9)

where sigma_+=F sigma F*/s is defined only if s>0. For a>0,

    q_+<=alpha^2 q/(a+alpha^2 q),
    eta_+<=min(n q_+,alpha^2 eta/a).                         (10)

If a=0 and s>0, q_+=1. Rare false acceptance on an entirely nonvacuum input is not clean preparation. A useful uniform success guarantee needs a supplied positive lower bound a>=a0 or other state information; no protocol-wide success floor is inferred.

For a>0 define the ideal accepted old/reference state rho_P by P sigma P=a J rho_P J*. The actual accepted joint state obeys

    ||sigma_+-J rho_P J*||_1<=2sqrt(q_+),
    ||Tr_B sigma_+-rho_P||_1<=2q_+.                          (11)

For the first inequality purify sigma, apply F and normalize, and compare to its normalized P projection: the overlap is sqrt(1-q_+). Partial trace contracts the pure-state bound. For the second, cross blocks vanish under Tr_B and the old marginal is a convex mixture of rho_P and the normalized Q contribution with weights 1-q_+,q_+. The unnormalized success discrepancy also obeys

    ||F sigma F*-P sigma P||_1<=sqrt(t^2+4at).                (12)

This is the trace norm of the purified two-by-two block [[0,sqrt(at)],[sqrt(at),t]], followed by contraction. It retains the coherent term linear in sqrt(t). These arguments include arbitrary R.

The intended pre-filter old state need not be rho_P. If ||tau-rho||_1<=epsilon_old, then

    ||Tr_B sigma_+-rho||_1<=epsilon_old+2(1-s)
                              <=epsilon_old+2q,            (13)

because tau=s tau_+ +(1-s)tau_fail after all outcomes are summed. Conditioning can steer an entangled old/reference state. A small q_+ alone cannot certify an independently intended old state. Equations (11) and (13) are different target comparisons and must not be interchanged.

Every non-plus block is supported exactly in Q, even with these phase errors. Their sum has trace 1-s, their total occupation expectation is eta-s eta_+, and together with success they restore every initial population and the old/reference marginal. The actual aggregate failure is E_e(sigma)-F sigma F*, generally neither Q sigma Q nor the ideal expression (4). All of these blocks remain part of (1). A numerical acceptance frequency also requires its separate sampling/statistical contract; (9) concerns the actual state/instrument probabilities.

## 4. Same installed K and the low-number coherence that must remain

Import the complete de7 statement at the exact copied identity, with the same literal noncommuting multi-port model and arbitrary old H:

    K=H+c I+Delta L+sqrt(Delta)V,  c=s0+r,
    kappa=(209/16)sum_i |lambda_i|,  v=4sum_i sqrt(209|lambda_i|/64),
    mu0=Tr(rho H)+c,   nu0=Var_rho(H)+Delta kappa.

The reserve r is the same installed scalar in both comparisons. Set h0>=||H||, d=2h0, l1=(9+sqrt(5))/8, and retain the actual kappa2 from de7(8), including anticommuting-port cancellations. Define

    gamma1=sqrt(Delta kappa)(2d+Delta l1),
    gamma2=Delta sqrt(kappa2),
    cv=max(kappa,v^2-kappa),
    Qc=6M Delta^2+Delta cv+2Delta sqrt(6M)(d+sqrt(Delta)v)
                                      +2sqrt(Delta)d v.      (14)

The source's exact centered-square vacuum column C has its number-one and number-two parts bounded by gamma1 and gamma2. Their ranges are orthogonal. No common eigenbasis for overlapping old Pauli factors is imposed.

Two much smaller-support filter amplitudes govern this column:

    a1=max_u |f_+(one_u)|
       <=min(1,(1/2)max_u d_0u),
    a2=max_(u<v) |f_+(one_u+one_v)|
       <=min(1,(1/2)max_(u<v)(d_1u+d_1v)),
    gamma_e=sqrt(a1^2 gamma1^2+a2^2 gamma2^2).               (15)

Here k>=3, so row 1 exists. The bounds use the exact zero factor for h=1 or h=2. In particular uniform angle bounds give a1<=delta/2, a2<=delta, even though the global alpha certificate can scale as n delta.

Let bar_sigma=E_e(sigma), retaining an arbitrary pre-existing R but summing the outcome for the scalar moments. Its old marginal, q, eta and delta_u are unchanged. Use the source's population bound u=min((5/4)eta_a+(3/2)eta_b,4M q). Then

    |mu_(bar_sigma)(K)-mu0|
       <= E1:=h0 epsilon+Delta u+2a1 sqrt(Delta kappa eta),
    |Tr(bar_sigma (K-mu0 I)^2)-nu0|
       <= E2:=d^2 epsilon+2gamma_e sqrt(q(1-q))+RQ,
    |Var_(bar_sigma)(K)-nu0|<=E2+E1^2,                     (16)

where epsilon=||tau-rho||_1 and RQ is exactly de7(13), evaluated at the unchanged q and a certified u:

    RQ=4M Delta^2 u+Delta cv q
           +2Delta(d+sqrt(Delta)v)sqrt(4M q u)
           +2sqrt(Delta)d v q.

A convenient monotone version is E2<=d^2 epsilon+2gamma_e sqrt(eta)+Qc eta. The actual mean-centering square E1^2 is retained; variance is not centered at an unjustified physical mean.

Proof of the improvement in E1: under (6), a flip of auxiliary u has coherence multiplier

    product_j [1+exp(i(theta_j+e_ju))]/2=f_+(one_u)

or its conjugate, independent of every other occupation. The adjoint channel therefore rotates X_u in its X/Y plane and contracts it by |f_+(one_u)|. The local positive-block Cauchy-Schwarz estimate in de7 gives |Tr(bar_sigma V)|<=2sum_u |g_u|a1 sqrt(delta_u(1-delta_u))<=2a1 sqrt(kappa eta). This includes Q-Q coherences and does not declare them zero at imperfect angles.

For E2, subtract D0^2+Delta kappa I exactly as in de7, with D0=H-Tr(rho H)I. The P-P difference is zero. In the P-Q term the adjoint of (6) multiplies the vacuum column by the success diagonal F_Q (or its conjugate, immaterial to its norm). Its number-one and number-two parts are bounded by a1 gamma1 and a2 gamma2, giving gamma_e. Positivity bounds the input cross block by sqrt(q(1-q)). The Q-Q term is still evaluated on the actual output Q bar_sigma Q and bounded by the unchanged RQ proof. No invariance of L under inhomogeneous phase errors is assumed: its bound follows from the preserved local populations. The old/reference comparison contributes d^2 epsilon. This proves (16).

At zero phase error a1=a2=0. The ideal nonselective map removes all number-changing V expectation and all P-Q terms; it still keeps its Q population and the RQ cost. At nonzero errors these coherence terms are generally nonzero and linear in the small phase scale, not its square. The accepted state likewise retains P-Q coherence. The de7 one-cell coherent-sign example, after applying the diagonal F and choosing the input relative phase to align its nonzero one-excitation amplitude, has a coupling mean and centered-second-moment cross term linear in |f_+(one_u)| although its accepted excitation probability is quadratic. Dropping those cross terms is invalid.

The scalar moments of the full retained CQ output (1) equal those of bar_sigma, because K is tensored with identity on the record. These are unconditional moments; they do not assert every recorded failure branch has those same conditional moments. For one normalized recorded branch, use that branch's actual populations and complete old/reference marginal in the original de7 bounds.

For reference-valued moment operators on the pre-existing passive R, the same duality proof works before summing the D trace: replace h0 epsilon by d epsilon in the first centered-moment bound, and add Delta kappa epsilon_R to E2 in the second. The uncentered first moment still pays |mu0|epsilon_R. Here epsilon_R=||tau_R-rho_R||_1 is unchanged by the nonselective filter. The newly produced record C is different: a record-dependent dual contraction can prevent cancellations used in the E1 improvement. We do not export that improved first-moment bound to arbitrary reference-valued records on R C. The original de7 theorem remains applicable with C included, but needs the complete intended D R C marginal certificate and its epsilon_RC term. Keeping C physically is not permission to ignore that distinction.

## 5. Accepted-branch moments: a conservative direct source application

For a>0, choose the comparison old state rho_P in (11), or a separately certified intended state. The normalized sigma_+ has actual p=q_+, eta=eta_+ and complete marginal error epsilon_+. The full de7(7),(12),(13),(15),(17),(18) apply without deleting its P-Q coherences. In particular

    E1_+<=h0 epsilon_++(3/2)Delta eta_+
                                 +2sqrt(Delta kappa eta_+),
    |Var_(sigma_+)(K)-[Var_(rho_P)(H)+Delta kappa]|
       <=d^2 epsilon_++2h0^2 epsilon_+^2+2gamma sqrt(eta_+)
                                      +(Qc+2k1^2)eta_+,     (17)

when eta_+<=1, with gamma=sqrt(gamma1^2+gamma2^2) and k1=(3/2)Delta+2sqrt(Delta kappa). For the rho_P target, epsilon_+<=2q_+. A different intended old state requires its own additional comparison. Formula (17) deliberately uses the complete source bound; the small accepted population does not authorize replacing gamma sqrt(eta_+) by a linear population term. More detailed column-weighted bounds can be sharper, but are not needed for the sufficient application below.

Exact ideal success has eta_+=0 and state J rho_P J*, so its baseline moments are exact. Its success probability is a, not one. Keeping failures still does not prepare the unconditional vacuum. After filtering, the same static K conserves each state's own total first and second moments; applying the filter itself is a controlled/read operation and need not conserve them. Extra physical clock, pointer, reader and work Hamiltonians are outside K and need their own ledger.

## 6. Explicit sufficient chain-length prescriptions

Use exactly the copied chain theorem: original sites and reserved geometry, |lambda_i|<=Lambda, ||H_M||<=hM, Delta=D M^6 with D>0 satisfying the original fixed-time dynamical prescription. Take a positive certified Lambda upper bound, so the constants below have positive denominators. Write

    Ck=209Lambda/16,   v0=4sqrt(209Lambda/64),
    G=sqrt(D Ck(4h+3D/2)^2+2D^2 Ck^2),
    Q0=6D^2+D max(Ck,v0^2)+4sqrt(6)Dh
                           +2sqrt(6)D^(3/2)v0+4h v0sqrt(D),
    K1=3D/2+2sqrt(D Ck).

The complete source gives kappa<=Ck M, gamma<=G M^(19/2), Qc<=Q0 M^13 and k1<=K1 M^6, including all subdominant terms. Uniform per-gate phase error delta<=1 gives gamma_e<=delta G M^(19/2). Equations (16) imply

    E1<=hM epsilon+(3/2)D M^6 eta
                                 +delta sqrt(D Ck)M^(7/2)sqrt(eta),
    E2<=4h^2M^2 epsilon+2delta G M^(19/2)sqrt(eta)+Q0 M^13 eta.
                                                                    (18)

These are retained-all-outcome scalar moments, with arbitrary original/reference correlations. The filter does not lower eta.

**Mean alone.** Epsilon<=B M^-1, eta<=A M^-6 (sufficient per-auxiliary delta_u<=A M^-7/4), and phase delta<=E M^-1/2, 0<E<=1, give E1<=hB+(3/2)DA+E sqrt(D Ck A). Choose positive constants to fit the requested mean tolerance. This is a moment certificate, not uniform small full-instrument distance: (8) can grow under this mean-only phase prescription.

**Simultaneous mean and variance.** Require

    epsilon<=B M^-2,
    eta<=A M^-13  (sufficient delta_u<=A M^-14/4),
    max_ju |e_ju|<=E M^-3,  0<E<=1.                          (19)

Then E1<=hB M^-1+(3/2)DA M^-7+E sqrt(D Ck A)M^-6, while

    E2<=4h^2 B+2E G sqrt(A)+Q0 A.

Every omitted displayed power is nonpositive; the variance adds the actual E1^2. For fixed positive tolerances m_tol,v_tol set t0=min(m_tol,sqrt(v_tol/4)) and choose

    B=min{1,t0/[3(h+D)],v_tol/[16(h^2+D^2)]},
    A=min{1,2t0/(9D),[t0/(3sqrt(D Ck))]^2,
                    [v_tol/(8G)]^2,v_tol/(4Q0)}.            (20)

The three mean terms are each at most t0/3. The old-marginal, coherence, Q-Q and mean-square variance allowances are each at most v_tol/4. Thus (19)-(20) suffice uniformly in every finite M, without assuming [sigma,P]=0 or independent cells. These are sufficient, not optimal, angle/population budgets. They retain the M^-14 local-population scale of the source's separately block-diagonal case by paying a specifically structured phase-filter accuracy; they do not make a generic noisy apparatus block diagonal.

If full-instrument accuracy against the ideal multi-outcome filter is also requested, (8) gives error<=8E k/M^2 under (19). Since k<=3M for M>=1, choosing E<=min(1,epsilon_inst/24) is one uniform sufficient prescription. This additional bound still compares to (1)-(4), not to an all-clean or binary-Lueders channel.

**Accepted state with only a success-mass premise.** Separately suppose a>=a0>0, without any small initial eta assumption. Under uniform phase error delta,

    q_+<=4M^2 delta^2/a0,
    eta_+<=16M^3 delta^2/a0,
    epsilon_+<=8M^2 delta^2/a0                               (21)

for comparison to the ideal accepted old state rho_P. Direct substitution in (17) yields

    E1_+<= (8h/a0)M^3 delta^2+(24D/a0)M^9 delta^2
                             +8sqrt(D Ck/a0)M^5 delta,
    Evar_+<= (32h^2/a0)M^4 delta^2
             +(128h^2/a0^2)M^6 delta^4
             +(8G/sqrt(a0))M^11 delta
             +[16(Q0+2K1^2)/a0]M^16 delta^2.               (22)

The variance statement assumes eta_+<=1. A sufficient mean-only choice is delta<=b M^-5 with small b. A sufficient simultaneous choice is delta<=b M^-11. For the latter, eta_+<=1 follows from b<=sqrt(a0)/4. Define

    Cm1=8sqrt(D Ck/a0),       Cm2=(8h+24D)/a0,
    Cv1=8G/sqrt(a0),
    Cv2=[32h^2+16(Q0+2K1^2)]/a0,   Cv4=128h^2/a0^2.

One explicit b is the minimum of 1, sqrt(a0)/4, m_tol/(2Cm1), sqrt(m_tol/(2Cm2)), v_tol/(3Cv1), sqrt(v_tol/(3Cv2)), and (v_tol/(3Cv4))^(1/4); a zero denominator is interpreted as infinity. With delta=b M^-11, the residual mean powers are -19,-13,-6 and the residual variance powers are -18,-38,0,-6. Hence all displayed terms are controlled, including coherent ones. This conservative prescription is not asserted optimal; (15) can support sharper accepted-branch refinements. It does not certify an independently specified old input, nor erase the retained rejected trials or supply a statistical lower bound a0.

The physical baseline remains Tr(rho H)+c and Var_rho(H)+Delta kappa, with the appropriate input or accepted rho. The coupling variance can grow as M^7. Reference-valued centered-second-moment comparisons still pay Delta kappa epsilon_R<=D Ck M^7 epsilon_R; the uncentered first record pays |mu0|epsilon_R, with the actual installed reserve. Exact preservation of the pre-existing R marginal holds only when all outcomes are summed, not on a selected branch. No scalar moment bound is a channel/readout/physical-energy theorem.

## 7. Resources, failed shortcuts and scope

The logical phase stage uses exactly nk=4M ceil(log2(4M+1)) addressed diagonal two-qubit gates, k clean plus pointers and k X readings; there are 2^k complete outcome blocks and a k-bit record. Its nominal total phase action is n sum_j theta_j=2*pi*n(1-2^-k). If an actual signed two-qubit control norm cap Jc is supplied, a serial phase schedule with durations (theta_j+d_ju)/Jc has sufficient total time [2*pi*n(1-2^-k)+E_tot]/Jc. Exact plus preparation can additionally use k supplied Y rotations of angle pi/4, with serial time k*pi/(4Jc); actual read duration, clock and preparation time are separate. This does not identify signed phase-control generators or K with a physical positive-energy apparatus.

Addressability is not ordinary-neighbor geometry: every pointer interacts with every auxiliary. If a supplied path of length d_ju connects their physical sites, a returned route can use 2(d_ju-1) SWAPs plus the phase gate, returning arbitrary entangled transit by the full permutation identity. This optional parameterized compilation needs its actual paths, timing, control and drift contract. No collision-free whole layout or persistent-K route is supplied here. The k extra clean factors and their readout/reset are not certified by the filter itself.

The exact/structured results fail to justify the following shortcuts:

* Replacing aggregate failure by Q sigma Q fails already on a number-one/number-two superposition.
* Dropping a dyadic row admits some nonzero occupations; the selected control includes this failure.
* Calling the unconditional filter excitation removal is contradicted by every diagonal preparation. In particular the chain source's vacuum/all-occupied correlated mixture is unchanged and retains variance excess (4M Delta)^2 p(1-p).
* Treating small false-acceptance probability as linear moment error drops success P-Q coherences. The source's coherent one-excitation witness survives the structured filter whenever that amplitude is nonzero.
* An input supported wholly in Q can falsely pass with small positive probability while its conditional excitation probability is one. A success floor and target-marginal statement are separate premises.
* Treating a scalar cancellation as arbitrary record-valued cancellation ignores the new outcome label and the epsilon_R terms.
* Allowing pointer/readout/axis/drift faults would invalidate exact vacuum immunity and population/marginal preservation. Such faults require a separate complete error and actual K-moment budget; no theorem here absorbs them silently.

A clean initial pointer, calibrated phase gate, classical read, elapsed time, continued memory and reset remain supplied. Each retained X pointer is in its recorded eigenstate, not automatically restored to its independent initial plus state. Permanence or repeated fresh capacity requires a separate contract. The result is finite conditional filter and moment mathematics, not a new physical axiom, native preparation, all-outcome purification, universal no-go or retained audit.

## 8. Evidence and source boundaries

The general identities and bounds above are analytic. Complete de7 and current chain arguments were read; exact copies and prior exposure are pinned in SOURCE_PINS.json. The root-supplied mechanism is credited as such. The next section will record the selected one-cell check only after its source and control plan have been sealed. Numerical identities are discriminators, not proofs of the all-M inequalities. No parent or archived scientific code is imported or replayed.


## 9. Actual selected evidence and final disposition

The pre-execution proof, control plan, input pins and program were sealed at 2026-10-14T23:16:31.398523+00:00 in PRECHECK_SEAL.json. The exact prior proof is retained at history/DERIVATION.precheck.md; this evidence section is an append-only change, with its full diff preserved. The sole scientific launch ran at 23:16:49.747423–23:16:49.922231 UTC, returned zero and produced no stderr. Its executed source was b646fb16bc22945f8521b0f0de76fa3cb6670da9fa1cb85b443c7e2070187450 before and after. Full raw streams, the exact executed copy, argv, recorder identity and receipt are in run001. No failed launch occurred; the deliberately erroneous constructions below are retained as countermodels, not rewritten into successful history.

The explicit pointer-state evolution and product Kraus formulas agreed to 4.48e-16; completeness, exact success P, number pinching, structured vacuum immunity, population preservation and the complete old/reference marginal had residuals below 9e-16. These are floating selected checks, not exact arithmetic or general proofs. The input includes entangled old/reference degrees, coherent vacuum/one-/two-/four-excitation sectors, and the literal one-cell K with an installed reserve 17. Its noncommuting H-L commutator on that input had norm 0.0387298.

For uniform angle error 1/64, measured success-filter amplitudes were alpha=0.0312144, a1=0.00504714 and a2=0.0108728, within their distinct certified bounds. Starting from a=0.6 and eta=0.7, actual all-plus probability was 0.6000715443618997, false-acceptance mass 0.0000715443619000868, accepted excitation probability 0.0001192263865405669 and accepted total population 0.00039233312596824335. All eight outcome weights and their unnormalized K moments are printed in full; no rejected outcome was dropped from the retained calculation.

The wrong binary-Q aggregate failure had full-reference trace-norm witness 1 on the specified number-one/number-two coherent pair. Omitting the j=0 row falsely accepted number one with probability 0.4267766952966369. Deleting actual success P-Q coherences changed its K mean by 0.023308966011590826 and its variance by 0.3721075121446802. The baseline variance was 64.14, including the actual Delta*kappa=64, whereas the retained-outcome variance was about 354.17: acceptance filtering did not clean the unconditional ensemble. The selected mean, centered-second-moment and variance deviations obeyed (16), whose conservative bounds were not close to saturated. No parameter sweep, large-M test or generic physical-apparatus simulation is inferred.

The resulting proposed theorem is the complete finite instrument (1)–(6), structured success/state bounds (7)–(13), and the same-K conditional bounds and sufficient applications (14)–(22). It does not repair binary failure into Q, erase excitation population on retained trials, certify unknown clean pointers/readout, or eliminate drift/reset/Record obligations. The literal channel identities and all-M powers rest on the analytic arguments, with exact accepted-parent hypotheses and scopes preserved. Source acceptance and any independent review remain with root; no audit verdict is asserted.

## Complete ordinary-neighbor layout and control-error ledger

# An explicit ordinary-neighbor layout for the chain auxiliary filter

**Proposed conditional author extension.** The accepted restricted-chain geometry is imported at raw identity 79d2388a; the immutable dyadic-filter argument is the author's prior source 0e75e69e, not an independently accepted theorem inferred from its freeze. Exact paths and complete identities are in SOURCE_PINS.json. No other candidate or review result was used. Returned-SWAP conjugation and finite-time Duhamel estimates are established methods, proved directly here. This note supplies a concrete restricted layout and its costs, not a native apparatus, fixed-cap construction, physical-energy identification or audit verdict.

There are two distinct conclusions. Exact net SWAPs and diagonal phase gates realize the prior complete filter with its phase-only error model, returning all transit as an operator identity. If the literal installed K remains present during additive control pulses, the same geometric word gives a full-input/reference approximation with an additional explicitly priced drift error. That error is not a diagonal phase error. No cancellation, attenuation, repositioning or conjugate transport of K is assumed.

## 1. Fixed old geometry and the extra-region premise

Let M>=1, n=4M, and k=ceil(log2(4M+1)). All old coordinates and operators are exactly those of the accepted chain. For r=i mod 4 set

    (Y_0,Y_1,Y_2,Y_3)=(0,1,2,1),
    (Z_0,Z_1,Z_2,Z_3)=(1,2,1,0),
    d_i=(i,Y_r,Z_r), beta=(1,0,0),
    (s_i^y,s_i^z)=(+,+),(+,-),(-,-),(-,+).

For even i put eta_i=(0,0,s_i^z), gamma_i=(0,s_i^y,0); for odd i put eta_i=(0,s_i^y,0), gamma_i=(0,0,s_i^z). Cell i, 0<=i<M, has original roles d_i,p_i=d_i+eta_i,d_(i+1), and four auxiliary sites

    a_i=d_i+beta,            b_i=d_i+eta_i+beta,
    a'_i=d_i+gamma_i,        b'_i=d_i+eta_i+gamma_i.       (1)

The old box is B_M={0,...,M} x {0,1,2} x {0,1,2}. The imported analytic incidence proof makes the 4M sites (1) disjoint and avoids every required original role. The other box factors can be arbitrary dirty originals. Earlier spare vertices are not all available: w_i=a'_(i+1) for i<M-1. None is relabeled or moved here. The original H remains its identical summand on its original factors, without a commutation assumption.

Supply the finite enlarged ordinary open box

    Bhat_M={0,...,M+k} x {0,1,2,3,4} x {0,1,2,3}.           (2)

Its new sites Bhat_M\B_M must be available new factors, with no pre-existing H support or unpriced couplings there. If the old model contains outside original factors, they must avoid this specified new region. This is a supplied-placement/support premise, not an ability to clear occupied space. Put the k new pointer qubits at

    F_j=(M+1+j,3,3),  0<=j<k.                              (3)

They are supplied in independent |0> states. All other new factors, denoted E, can be arbitrary and jointly entangled with the old D B and passive R; no clean transit is required. Here B denotes the 4M candidate auxiliaries, which need not be clean. The exact old K is extended by identity on every new pointer/transit factor. We compare states on all D B E R, with every outcome retained; E is never discarded to manufacture a return claim.

The box has 20(M+k+1) sites, the old box has 9(M+1), and exactly 11(M+1)+20k new sites are supplied. Of these k are clean pointers and 11(M+1)+19k are arbitrary transit/spectator factors. The original 2M+1 required data roles, 4M candidate auxiliaries, 8M selected chain edges and all original coordinates are unchanged. The box is a simple sufficient footprint, not a packing optimum.

## 2. Explicit simple paths and collision avoidance

For each auxiliary u=(x,y,z) in (1), route pointer j along this ordered path:

    (M+1+j,3,3) -> (M+1+j,4,3)
      -> (x,4,3) -> (x,y,3) -> (x,y,z),                    (4)

where each arrow is expanded into every intervening unit step along its single axis. The x motion is decreasing, the second y motion is decreasing, and the z motion is decreasing. All vertices lie in (2). The initial stem has x>M, whereas both final stems have x<=M. The two stems cannot intersect each other; the intervening coordinate segments meet only at their stated junctions. Thus (4) is simple. It is ordinary nearest-neighbor throughout, with no wrap, periodic seam or long-range edge.

No path contains another pointer site: its long corridor has y=4, its final stems have x<=M, and its initial stem has only its own x-coordinate. Paths for different gates can intersect, and can pass through old active auxiliaries or arbitrary old data. All routes are executed serially and returned before the next route; therefore such intersections do not cause simultaneous occupation or gate conflicts. Their validity does not depend on transit being blank, separable or outside the support of H. Active H during these moves is accounted for separately in Section 6, not transported with the tokens.

The length in edges is exactly

    d_ju=M+j+9-x-y-z.                                     (5)

Every auxiliary has x+y+z>=2, with equality for a_0 and a'_0. This follows directly from the four residue rows: the minimum auxiliary sums in cells of residues 0,1,2,3 are i+2,i+2,i+1,i+1 respectively; the last two residues start at i=2 and i=3. Hence the exact maximum over all routes is M+k+6, attained at j=k-1 and a_0 or a'_0.

For exact total counts write chi_M=1 when M mod 4 is 2 or 3, and zero otherwise. Each cell's four auxiliary x-coordinates sum to 4i+2. Its four transverse sums y+z are, by residue, 8,12,8,4. Consequently, for every M,

    sum_u (x_u+y_u+z_u)=2M^2+8M+4chi_M,
    D_sum:=sum_(j,u) d_ju
         =k(2M^2+28M-4chi_M)+2M k(k-1).                  (6)

The four-residue formulas, not a finite enumeration, prove these all-length identities.

## 3. Exact returned word, including arbitrary entangled transit

For a path v_0=F_j,...,v_d=u let T be the chronological product of SWAPs on (v_0,v_1),...,(v_(d-2),v_(d-1)); the endpoint u is never swapped. Apply T, then

    G=exp(i phi_ju n_(v_(d-1)) n_(v_d)),

then the reverse SWAP word T*. The net unitary is exactly

    T* G T = exp(i phi_ju n_Fj n_u) tensor I_other.          (7)

Indeed a SWAP permutes complete tensor factors, so T* n_(v_(d-1)) T=n_Fj and T* n_(v_d) T=n_u. Functional calculus gives (7). This is an equality of full operators, including every scalar phase, not a statement about classical labels or one prepared input. Tensoring with I_R and applying it to any density matrix proves the full-reference identity, even when transit is entangled with the two endpoints or with R. The outside factors are unchanged by this remote gate; their correlations change only through the stated endpoint operation. Returning each block proves the product identity for the entire word, despite intersections of different paths.

Order the gates first by j=0,...,k-1 and then by cell i and roles a,b,a',b'. Prepare each clean pointer by exp(-i pi Y/4)|0>=|+>. Set phi_ju=theta_j+e_ju, theta_j=pi/2^j. Apply the returned word (7) for all n k pairs, and then supply the exact X instrument on each original pointer position (3). In the exact net-gate model the entire routed phase stage is therefore

    product_(j,u) exp(i(theta_j+e_ju)n_Fj n_u),              (8)

tensored with the returned transit identity. The full pre-read unitary is (8) multiplied on the right by product_j exp(-i pi Y_Fj/4); equivalently (8) acts on the prepared plus pointers. Since all logical phase factors commute, there is no schedule-dependent sign or missing phase.

For fixed real e_ju, the full retained instrument on an arbitrary input sigma_DBER is

    Omega_e(sigma)=sum_b |b><b|_C tensor F_b sigma F_b*,
    F_b=product_j [I+(-1)^b_j exp(i sum_u(theta_j+e_ju)n_u)]/2.
                                                                    (9)

The identities on D,E,R are implicit. Each measured pointer may also be retained in its recorded X eigenstate. Before the supplied read the coherent output is sum_b |x_b>_F tensor F_b. This is not a physical observation/Record derivation. Every unnormalized success and failure block is specified. At e=0, success is exactly the B-vacuum projector P and aggregate failure is sum_(h>=1) Pi_h sigma Pi_h, generally different from Q sigma Q. No geometric step changes that distinction.

## 4. Exact resources and the meaning of the phase-only class

A length-d remote gate uses 2(d-1) SWAPs and one two-qubit phase. Thus the exact counts, before supplying readout, are

    N_phase=n k=4M k,
    W_swap=2D_sum-2n k
          =4k[M^2+M k+11M-2chi_M],
    G_two=W_swap+n k=4k[M^2+M k+12M-2chi_M].                (10)

There are k one-qubit plus preparations and k X readings, with 2^k complete outcomes. Only k fresh clean qubits are added. The number of distinct old auxiliary factors remains 4M. At any instant the serial schedule uses at most one added one-/two-qubit control. A fixed site is incident to at most four elementary gates per remote block, hence at most 4n k+1 gates including its possible preparation. This is a cumulative-use bound; the instantaneous added whole-term norm load will be at most Jc below. Original background loads are added to that cap, not displaced by it.

The structured class means the **net physical gates** in Section 3 are exact SWAPs and exactly exp(i(theta_j+e_ju)n_v n_w) on their adjacent physical endpoints, with certified fixed real |e_ju|<=d_ju^err. There is no environment-conditioned coefficient, axis error, extra one-qubit phase, residual swap, unwanted interaction, preparation fault, read error or unpriced drift. Superscript err distinguishes angle bounds from geometric lengths (5). Under these hypotheses, exact SWAP conjugation transports the two number projectors with their intended labels, and these physical phase errors become precisely the prior logical e_ju. An inaccurate SWAP generally rotates/transports other observables and is not absorbed into e_ju. Exact SWAPs here include their actual operator phase.

For this class, all conclusions of the pinned filter algebra apply on the enlarged D E reference system: every occupation probability and the unconditional D E R marginal are preserved; a true B vacuum has all-plus outcome with certainty; no branch transfers occupation; and false success is bounded using alpha<=min(1,(1/2)max_j sum_u d_ju^err). In particular, if every d_ju^err<=delta then alpha<=min(1,2M delta). The full complete-instrument error relative to the ideal multi-outcome filter is at most min(2,2 E_angle), E_angle=sum_ju d_ju^err. Conditioning still needs its actual success probability; an input entirely in Q need not become clean when a rare false success occurs. Failure is retained and is not binary Lueders failure.

The prior same-K phase-filter moment refinements are statements about (9) and their stated input marginals/population budgets. They do not automatically apply to faults outside this class. In particular retaining outcomes does not remove excitation population, and new-record-valued conditioning is not scalar cancellation. The installed baseline, scalar/reserve and coherent P-Q terms remain those of the prior sources.

## 5. Explicit bounded NN pulses, time and scalar costs

For a supplied Jc>0 use one pulse at a time. A SWAP S on an edge is implemented by

    H_swap=(pi/(2 tau_s))(I-S),  tau_s=pi/Jc.

Its norm is Jc and exp(-i tau_s H_swap)=S exactly: on the symmetric and antisymmetric sectors the phases are 1 and -1. Equivalently H_swap=(pi/(4tau_s))(I-XX-YY-ZZ). The identity term is retained, and the sum of the four Pauli coefficient magnitudes equals Jc. Dropping that scalar changes the operator phase and is not this exact word.

For the physical adjacent phase use

    tau_ju=(theta_j+d_ju^err)/Jc,
    H_phase,ju=-(theta_j+e_ju)n_v n_w/tau_ju.

Its norm is at most Jc. The expansion n_v n_w=(I-Z_v-Z_w+Z_v Z_w)/4 retains all scalar and one-site terms. Its signed Hermitian control is a supplied capability, not a positive-energy identification. A plus preparation uses H_p=Jc Y for tau_p=pi/(4Jc). In the drift-free comparator these pulses implement the exact word above. Their certified total coherent duration is

    T_c=A_c/Jc,
    A_c=pi W_swap+8pi M(1-2^-k)+E_angle+k pi/4.            (11)

This counts serial plus preparation as well as routing and phases. Preparation of the k independent zero states, an actual reader's time, setting changes and calibration operations are separate physical premises. If nonzero switching/idle times total t_idle, they must be included in the background time in Section 6; (11) does not erase them.

The controls are piecewise constant one-/two-site ordinary-neighbor generators with finite count and exactly specified intervals. Each gate at most saturates Jc. Including a local decomposition of K, the instantaneous per-site whole-term load is at most its unchanged background load plus Jc. A sufficient bound on the time-integrated added load at any one site is 4pi n k+E_angle+pi/4: within a remote block the four-SWAP case costs 4pi, while the phase-adjacent site costs at most 2pi+theta_j+d_ju^err<=3pi+d_ju^err. This is not a parallelism or common-volume optimization.

For bounded d_ju^err, k=O(log(M+1)), the footprint is O(M+log M), the swap count and coherent control action are O(M^2 log M). All constants and the exact finite expressions are (2), (10), (11). Each supplied Jc gives a finite time. Neither the pulse signs nor a scalar reserve identifies a physical controller, power supply, clock or nonnegative total Hamiltonian.

## 6. The same installed K left continuously active

For clarity, the literal old generator and its chosen scalar are

    K=H+Delta L+sqrt(Delta)V+(s0+r)I,
    s0=(29/2)sum_i |lambda_i|, Delta>0, r>=0,
    L=sum_i[N_i+(1/4)Z_p_i(n_b_i-n_b'_i)
                    -(1/4)(S_a_i,b_i+S_a'_i,b'_i)],
    V=sum_i[t_i Z_d_i(X_a_i+X_a'_i)
                +q_i X_d_(i+1)(X_b_i-X_b'_i)],
    t_i=sqrt(209|lambda_i|/64), q_i=sign(lambda_i)t_i.       (12)

The same r, possibly zero, is used before, during and after the filter; it is not chosen anew by this layout. With h0>=||H|| and v=4 sum_i t_i, an accepted full-space bound is

    beta_M=h0+s0+r+4M Delta+sqrt(Delta)v >= ||K||.           (13)

K is extended by identity on F,E, without added couplings. If H is not itself ordinary-neighbor, this note does not change its range; it certifies the added controls' geometry. If H is ordinary-neighbor, all terms of K plus the displayed controls are one-/two-site ordinary-neighbor. Original H acts at its old coordinates while tokens move through them; it is never silently conjugated along a route.

Let G_e(t) be the entire pulse schedule in Section 5 and U_e its drift-free unitary. The actual controlled generator is literally K+G_e(t), acting for T_c (plus any included switching intervals), with no cancellation or attenuation of K. Duhamel gives on the full space

    U_actual(T_c)-U_e(T_c)
      =-i integral_0^T_c U_actual(T_c,t) K U_e(t,0) dt,
    ||U_actual-U_e|| <= min(2,beta_M T_c).                (14)

This uses only unitary norms, so arbitrary noncommuting H and arbitrary references are allowed. The scalar in K remains in the phase-sensitive operator difference (14). It has not been discarded to improve a norm estimate. The full instantaneous Hamiltonian has norm at most beta_M+Jc. These are finite operator/control bounds, not a physical energy or free-work claim.

For an exact supplied terminal X instrument, including every branch and the returned transit in the output,

    ||Omega_actual(sigma)-Omega_e(sigma)||_1
         <= epsilon_bg:=min(2,2 beta_M T_c).              (15)

The density-matrix inequality follows by purifying the input, using unitary-vector distance, and applying the same trace-preserving read. Thus it is uniform in all initial old/auxiliary/transit/reference states and is not restricted to initial K-code or near-vacuum inputs. Exact return and population preservation apply to the comparator; the actual continuously active implementation has only the complete error (15). Combining with the phase certificate yields min(2,epsilon_bg+2 E_angle) against the ideal multi-outcome filter.

If a full generator residual has certified integral f=int||E(t)||dt, an initial clean-pointer/preparation error is epsilon_p in complete trace norm, and the reader differs from its specified instrument by complete error epsilon_r on its actual input domain, one sufficient additional budget is

    epsilon_gen=min(2,epsilon_p+2 beta_M T_total+2f+epsilon_r),
    T_total=T_c+t_idle.                                  (16)

Instead of an integral residual, per-gate operator errors eta_g can be telescoped with 2sum_g eta_g; do not count the same fault twice. The errors e_ju already defining G_e are not generic residuals. The preparation term must cover actual correlations with D B E R, rather than only a pointer marginal. A finite scalar cap or geometric placement alone supplies none of these certificates. Coherent switching transients require their full actual residual/time allowance.

An exact finite-duration reader confined to F and its own supplied apparatus commutes with K on D B. Its ideal final output is then Ad(exp(-iK t_read)) Omega_e, with the recorded pointers/apparatus included as specified. No extra beta_M t_read is required if this aged ideal output is the comparison target. If the target is instead the undelayed output (9), add min(2,2 beta_M t_read). The same reasoning applies to uncontrolled storage after the read. K moments are invariant during this exact free aging, but vacuum population need not be: sqrt(Delta)V couples vacuum to excitations. The reader apparatus, its clean state, finite-time instrument error, record accessibility/permanence and reset are supplied, not derived.

This distinction is consequential. Starting with a bare vacuum, a free interval tau under a nonzero V has excitation probability Delta*kappa*tau^2+O(tau^3), where kappa=(209/16)sum_i|lambda_i|>0. An ideal dyadic filter after that interval can fail with that probability, whereas every phase-only gate error in Section 4 leaves a vacuum input certainly all-plus. A generic residual or active background therefore cannot be renamed e_ju. A particular compensated net-gate implementation could satisfy the exact class, but its compensation would be an extra proved/priced premise, not a consequence of routing.

## 7. Accuracy prescriptions and same-K moments

For a requested generic full-output error 0<epsilon_*<=2, with no residuals, no idle intervals and the supplied exact terminal instrument, it suffices to choose

    Jc >= 2 beta_M A_c/epsilon_*.                         (17)

K's coefficients and H are unchanged. This grows control strength, not an attenuation of the background; it is a conditional finite implementation with no fixed cap asserted. If a cap Jc is already fixed, (15) is the available sufficient guarantee, which can be uninformative. Failure of this fast-pulse bound does not prove that a fixed-cap construction is impossible.

In the chain design Delta=D0 M^6, |lambda_i|<=Lambda, h0<=h M, put

    A0=h+(29/2)Lambda, nu=4sqrt(209Lambda/64).

Then beta_M<=A0 M+nu sqrt(D0)M^4+4D0 M^7+r. If the original optional reserve r=h0+sqrt(Delta)v is installed, it is O(M^4) and remains included. More generally require a declared r<=C_r M^7 to write

    beta_M<=C_beta M^7,
    C_beta=A0+nu sqrt(D0)+4D0+C_r.                        (18)

For a uniform finite angle bound delta_max, E_angle<=4M k delta_max. Since k<=3M for M>=1, (10)-(11) imply the explicit convenient bound

    A_c <= C_A M^2 k,
    C_A=60pi+8pi+pi/4+4delta_max.                        (19)

Indeed W_swap<=4k(M^2+Mk+11M)<=60kM^2, 8pi M<=8pi kM^2, and the other two terms are bounded as shown. This loose but sufficient bound keeps the actual logarithmic k. Thus a full-output tolerance independent of M is supplied by Jc>=2C_beta C_A M^9 k/epsilon_*, still with the identical K at every length. The runtime is the actual (11), not a rescaled simulated time.

Let rho_a,rho_e denote the full normalized actual and comparator outputs, with the outcome record retained, and ||rho_a-rho_e||_1<=epsilon_gen. On these enlarged outputs K is the unchanged operator on D B, tensored with identity on the record, pointers and new E factors. Old sites used as transit remain part of D B and can carry K. Direct trace duality gives

    |mean_a(K)-mean_e(K)| <= beta_M epsilon_gen,
    |Var_a(K)-Var_e(K)| <= 3 beta_M^2 epsilon_gen.         (20)

The latter uses |Tr K^2(rho_a-rho_e)|<=beta_M^2 epsilon_gen and |m_a^2-m_e^2|<=2 beta_M^2 epsilon_gen. This safe bound works with the actual installed scalar; it does not erase reserves, old marginal mismatch, the baseline coupling variance, or the original coherent P-Q and Q-Q terms. For record-valued raw first/second moments, the trace-norm increments are bounded by beta_M epsilon_gen and beta_M^2 epsilon_gen, respectively, through duality with arbitrary bounded observables on the full retained reference/record. A separately centered second moment pays ||K-mu I||^2 epsilon_gen; scalar variance cancellation is not a record-valued theorem.

Therefore any valid phase-only comparator moment certificate from the pinned source can be used with the additional allowances (20). For fixed positive incremental mean/variance tolerances m_err,v_err one sufficient choice is

    epsilon_gen <= min{1,m_err/beta_M,v_err/(3 beta_M^2)}. (21)

For example, using (18), choose E0<=min{1,m_err/C_beta,v_err/(3C_beta^2)} and epsilon_gen<=E0 M^-14. With no other generic faults this is supplied by Jc>=2C_beta C_A M^23 k/E0. This deliberately conservative M^23 log M control-price example is not an optimal calibration claim; it shows the cost of retaining the prior same-K moment conclusions while also paying a generic active-background error. Phase-error budgets, e.g. the pinned simultaneous scalar-moment prescription, remain separate and must themselves be satisfied. No independence between cells is used.

For an individual actual success block A and comparator success block B, ||A-B||_1<=epsilon_gen and their weights differ by at most epsilon_gen. If the comparator success probability s exceeds epsilon_gen, normalized success states differ by at most min(2,2epsilon_gen/(s-epsilon_gen)). Generic faults can create false negatives or excitations from vacuum, so exact immunity and phase-only false-acceptance bounds require this additional complete error and any necessary success floor. Discarding failure is never part of (15)-(21). All these moment statements concern the same mathematical installed K; they are not a preparation, energy-measurement, native control or Record postulate.

## 8. Selected control plan and remaining premises

The analytic coordinate, conjugation and Duhamel arguments establish the proposed finite conditional result. A single new integer/Fraction fixture will use M=5, k=5, including all four coordinate residues and a repeat. Before execution, its source, this argument and CONTROL_PLAN.md will be sealed. It will emit every gate and path, check ordinary-neighbor edges, all fixed old roles, fresh pointer avoidance, full token return and the logical labels at every physical phase. Token verification is a check of the monomial-operator structure, not simulation of 2^220 amplitudes or active-K dynamics. The all-state/ref proof is (7).

The deliberate error is omission of the last reverse SWAP in the first remote block. It must leave a nonidentity tensor-factor permutation. With the affected dirty transit Bell-entangled to a passive reference, all B initially vacuum and the pointers plus, this deletion makes pointer 0 fail its X test with probability 1/2 instead of zero; this follows from its maximally mixed Bell marginal. The fixture will preserve the erroneous emitted word and the actual label mismatch, not repair it silently. No broad sweep or parent replay is planned.

Necessary supplied interfaces remain: the extra region and identity extension of K; k independent clean pointers; signed addressed bounded controls with certified angles/timing and switching errors; either exact net gates or the explicit full-background comparison; an actual X reader and any clean/readout resources; and a separate reset/permanence contract for repeated use. Transit requires no initialization. The original H is arbitrary and unchanged, but only the added controls are certified NN unless H's own locality is supplied. This restricted chain routing does not solve arbitrary occupied-lattice packing or a fixed-cap autonomous apparatus. No editable prompt or prior source is changed.


## 9. Actual selected evidence and final scope

PRECHECK_SEAL.json was written at 2026-10-14T23:43:37.385175Z, before the sole selected launch at 23:43:41.424803–23:43:41.482241Z. The exact executed source was 35b24a4efd5b9bf78e764a382dcde507dfbd61d114ef587410015a7f58268509 before and after. The program exited zero; stderr is empty. Its full source, complete stdout, receipt, all paths and both complete emitted words are retained under run001. No scientific program was replayed, no numerical sweep was made and no execution failed. The intentionally defective word is evidence of a rejected construction, not a failed run relabeled as success.

For the selected M=5, k=5 fixture, the enlarged box has 220 sites: 54 old sites, five new clean pointers and 161 new arbitrary transit/spectator sites. The program emitted 100 remote phases, 2100 SWAPs, five plus preparations and five X reads. There are 2205 coherent gates and 2210 total emitted records. The sum of route lengths is 1150, the maximum is 16, and nominal coherent action is exactly 2140 pi. The largest cumulative site incidence is 400, within the analytic 4nk+1=401 bound. Every intended logical phase pair and every correct block's return labels matched; the correct final tensor-factor permutation is identity.

Deleting the first block's final reverse SWAP leaves exactly the exchange of F_0=(6,3,3) with its adjacent corridor factor (6,4,3), and 19 subsequent phase-label mismatches. Both the complete defective word and all mismatches are retained. The analytic Bell-transit witness in Section 8 therefore has false-negative probability 1/2. This discriminator concerns complete quantum correlations through the permutation identity; no 2^220-dimensional wavefunction was simulated. Separately, the scalar convention is also consequential: omitting only each SWAP generator's identity contribution would multiply each SWAP by exp(i pi/4), hence the selected complete word by exp(i pi*2100/4)=-1. That alters its phase-sensitive operator identity even though it leaves its channel unchanged.

The post-run final read clarified three phrases without changing the emitted control or its proof: (8) is the routed phase stage, with the stated plus rotations supplied separately in the full pre-read unitary; the exact-net hypotheses are sufficient, with no assertion that they are the only conceivable physical implementation; and only the new E transit factors have the identity extension, while old transit sites retain their original K action. The exact sealed precheck proof and full final diff are preserved. The earlier residue-table drafting correction is also retained. No rerun was justified by these clarifications.

The proposed result is the explicit all-M placement/count contract (1)–(11), full operator/reference identity (7)–(9) for the declared exact/phase-only class, and conditional active-background and generic-fault guarantees (12)–(21). Its finite-M control is a selected structural check, not proof of arbitrary-length formulas, background dynamics or physical apparatus supply. Same installed H/K, all outcomes, dirty transit and actual scalar costs are preserved. Growing controls and independent clean/readout resources remain supplied; no common cap, reset, native preparation, autonomous timing, Record law, physical energy or retained status follows. Root review remains separate.
