---
title: Geometric-time refinement of local Gauss-penalty recovery
claim_id: geometric_time_local_gauss_penalty_recovery_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: finite even volumes, local physical output and arbitrary passive reference, supplied initial K state and static controls, horizon-dependent sufficient slowdown
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: accepted local geometric estimate and horizon-specific sufficient control-time bound; identity runner evaluates no mathematics
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["uniform_local_gauss_penalty_recovery_bounded_theorem_note_2026-10-14", "microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18", "microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18"]
runner: scripts/geometric_time_local_gauss_penalty_recovery_identity_2026_10_14.py
next_trace_action: separate root review and guarded integration of this publication package, then regular PR and independent retained audit
---

Claim type: bounded_theorem

# Conditional geometric-time refinement of local Gauss-penalty recovery

This source assembly presents a sufficient degree-four effective-time error factor for local physical outputs with an arbitrary passive reference. Under the accepted whole-term control budget, a horizon-dependent weaker supplied static drive gives a sufficient physical-time cost O(tau_star^5) at fixed remaining positive parameters. This refines the earlier local-uniformity theorem; it does not modify that theorem's canonical package or assert an optimal or native implementation.

**Current status.** Root conditionally accepted the complete new analytic source at **2026-10-14T10:51:16.230119Z** under `1cecae561962c855f1704363fda4fc43e1758965ccb1ef6676d8ddbecb09cb3a`, following complete root and separate review. The appended proof's opening and final statements that it is unreviewed or that no reviewer has received it are preserved historical status, superseded by this acceptance. The exact wrapper and assembly were accepted under `7f45dd068ac8fdb2b5cef5f3cf3c65e4807fe5e385570efb32352c0f401cbb13`, following root review `58bf88196e0123317dd0de42e432b0848c3efc7e9b68afd482b12f44b9242dea`. This publication rendering and driver require separate root review. Neither the source acceptance nor this packet assigns retained/audit status or authorizes a publication driver or canonical execution.

## Finite physical statement and the one mathematical parent

Use the declared even coarse tori L>=4, physical spacing 16 and physical period 16L, literal matter-edge qubits and hard-cutoff link pairs, including idle physical factors. The supplied static Hamiltonian is

    H_(lambda,kappa,L) = lambda N_(full,L) + kappa B_(0,L),

with the complete cycle/link/Gauss penalty and the exact coefficient/support contract of the accepted local-uniformity theorem. Let R_(0,L) be its reducing precode and K_L=R_(0,L) intersect ker N_(G,L), with N_(G,L)=sum_x G_x^2. On R_(0,L), full penalty dynamics agrees with the Gauss-only dynamics used in the proof. The full physical cycle/link terms and their scalar remain charged in the Hamiltonian resource ledger.

For every normalized initial density operator supported on K_L tensor R, arbitrary passive reference R, physical output S and t>=0, compare the reduced full physical evolution with the accepted physical compressed target B_(*,L)=kappa B_(0,*,L). The comparison includes actual local effects of leakage and has no postselection or reference-dimension factor. Its constants are uniform over the declared finite volumes and allowed static coefficient lists; no compatible infinite-volume state is constructed.

The sole mathematical parent is `uniform_local_gauss_penalty_recovery_bounded_theorem_note_2026-10-14`, canonical [local-uniformity theorem](UNIFORM_LOCAL_GAUSS_PENALTY_RECOVERY_BOUNDED_THEOREM_NOTE_2026-10-14.md) at SHA256 `52525335689adb5938a2e306b22c9a3752f0328e2cc21ac17ba727e41d36a573` (PR9540). Its four complete accepted bodies are archived and occur byte-identically, exactly once each, in that canonical note:

| Exact body | Role in this refinement |
| --- | --- |
| `fca3350c6572e7a60305974f5aba733910d0347847f859c7ea784d990d35f5ad` | Repaired periodic primitive, rotating frame, local remainder series, matrix-chain bound and endpoint cost |
| `ac224bb872353875eb8bf996f10c403747d9800d0929e387755219467d77e777` | Literal finite family, reducing precode/target interface and uniform physical supports |
| `2ddbcafc82ea479a04cceed7130003d61d60f82decbe3a5569f72226369d2a4a` | Nonempty subcode inside K_L for each declared even volume; existence only |
| `45ea7ab896996ea0d94ce43f8280776a2658a662ab9124a85d3e7292b24dd779` | Full whole-term physical budget, scalar, effective data and supplied-control/time limitations |

These are components of one canonical mathematical parent, not four new graph parents. The alternative cutoff proof is used for its actual geometric/physical interfaces; its complete error bound is not silently substituted for the direct-frame estimate. The stronger all-cycle subcode establishes inclusion and nonemptiness, not equality of cycle spans, an all-volume CAR/cubic representation or an input-preparation procedure. Earlier routes, neutral preparation, binary admission, and branch/publication ancestry add no theorem premise.

## Geometric estimate and polynomial

For a finite cubic carrier or rectangular periodic cubic torus, let the static comparison interaction A have nonempty labelled supports of size at most k, physical metric diameter at most r>=1 and per-site sum of norms at most g>0. The nonnegative matrix M_ij=sum_(Z contains i,j)||a_Z|| has row sum at most kg and no step longer than r. Exponential reweighting gives

    sum_j exp(dist(i,j)/r) [exp(2uM)]_ij <= exp(2e k g u),

including the zero-step diagonal. Physical balls obey |B(i,rho)|<=(2rho+1)^d, also after wrapping or filling a finite torus.

The transformed perturbation K(s) needs only an absolutely summable labelled decomposition with per-site norm h; its supports may be large or disconnected. Every label meeting the ball is charged in full to the near incidence sum. A far label must miss the entire ball, so every support site is outside before the weighted matrix tail is used. This yields

    sum_X ||[K_X(s), exp(iuA) O exp(-iuA)]||
       <= 2 |S| ||O|| h [(1+4e r k g u)^d+1].

Duhamel evolves the observable under finite-range A; the full perturbed propagator occurs only as an outer norm-preserving conjugation. Thus no finite-range propagation assumption is imposed on K. The passive reference never enters a metric ball or interaction count. Extensive ordinary norms establish finite-carrier convergence only and do not enter the displayed local error.

The repaired periodic primitive has local norm at most pg. For q0=2kpg<=1/4, the accepted frame series gives remainder norm h<=12kpg^2 and terminal frame cost at most 2|S|pg. Its growing supports are exactly the class handled by the new geometric estimate; F(0)=0 removes the initial frame. The integral is

    I_d(t;g)=t+[(1+4e r k g t)^(d+1)-1]/[4e r k g (d+1)].

In the literal Gauss application, p=2pi/lambda, k=57, r=36, c=60 and g=(10+11sqrt(3))J. Here r=36 describes the rotated comparison-drive supports, not the full physical decomposition's conservative diameter 48 and cardinality bound 32. The final fast Gauss conjugation enlarges the physical output to at most c|S| sites. For each terminal time that conjugated observable is fixed during interpolation; target expectations are unchanged because the target remains in ker N_G.

For lambda>=16pi k g, the accepted refinement gives

    ||rho_(S R)^full(t)-rho_(S R)^target(t)||_1
       <= min{2, (4pi c |S| g/lambda) P_3(g t)},

    P_3(z)=1+12kz+[3/(4e r)] [(1+4e r k z)^4-1].

P_3 is a sufficient positive increasing degree-four polynomial for z>=0. The error bound grows with time and can reach the trivial cap 2. It may be combined with the earlier exponential bound by taking their minimum where both hypotheses hold; it is not necessarily smaller at every finite time. Empty physical output, zero drive and zero elapsed time are treated directly, without dividing by zero or claiming the displayed conservative endpoint bound is exact.

## Horizon-dependent supplied time at fixed whole-term cap

Let B_L=kappa B_(0,L), J=kappa J0 and g=kappa g0, with g0=(10+11sqrt(3))J0 and J0>0. For effective time tau and physical Hamiltonian time t=tau/kappa, the polynomial argument is g0 tau while the prefactor is linear in kappa. Fix a finite requested effective horizon tau_star>=0, |S|<=s with s>=1, tolerance 0<epsilon<=2 and positive supplied whole-term cap Lambda. With beta=9+2sqrt(3), choose

    lambda = Lambda/332,
    0 < kappa <= min{1, Lambda/(2 beta J0),
                       lambda/(16pi k g0),
                       epsilon lambda/[4pi c s g0 P_3(g0 tau_star)]}.

The full whole-term budget is at most `166lambda+beta kappa J0<=Lambda`. It includes cycle/link terms which vanish on the reducing precode and the literal `(43/4)L^3 I` scalar; it is not the sharper L=4 resolved-Pauli coefficient extended to all L. The physical drive coefficient beta differs from the rotating-frame coefficient in g0. The total driven Hamiltonian need not be positive.

Choosing the displayed largest allowed kappa gives the sufficient terminal time

    T_phys(tau_star)=tau_star max{1, 2 beta J0/Lambda,
                        16pi k g0/lambda,
                        4pi c s g0 P_3(g0 tau_star)/(epsilon lambda)}.

At fixed positive g0, Lambda, epsilon, fixed s and literal constants, this is O(tau_star(1+tau_star)^4), hence O(tau_star^5) at large horizon. The statement chooses a weaker static drive for each requested horizon. It is not a fixed-drive all-time approximation, a lower bound, an optimal resource estimate or a practical synthesis claim. Certified smaller positive choices can preserve the sufficient inequalities with a controlled constant-factor slowdown when effective parameter data are supplied; arbitrary rounding robustness is not asserted. Exact static multi-qubit controls, integer penalty, normalized K_L input preparation, coefficient setting/precision, clock and readout remain supplied. The Hamiltonian time parameter is not thereby identified with a native physical clock or derived energy law.

## Source exposure, actual evidence and limits

The entire new proof `841e5f7416c58afed64c40e01aca9976bcd8efbe7c36fe6b628afb32f8fd5ad0` is preserved unchanged, with its six-file root package sealed by `76933c1fe63d7f7f588247f3fb95e82aab1a3977ceb69fb44772ae6aec0a59a3`. The complete 31-file separate review is preserved under seal `c6b24677395bb9542e8e17a061401c29adfd1e0a0ff671916ec330a3efef1a93`, with report `4d97142d98631805f717e606417979d8689f9281315ca5872d9306bf99e76208`.

The reviewer sealed a distinct clipped-profile/layer-cake assessment at 10:24:35Z before opening the new root source at 10:24:50Z. Its looser constants and log|S| term remain unchanged. The target and prior machinery were shared; the detailed review and selected control are source-exposed within the same model family. This is limited pre-exposure separation, not a blind whole-theorem review or model-diverse audit.

One exact toy physical-period-4 Pauli control refutes the incorrect rule that a crossing support is far whenever any site lies outside the ball: the actual local/reference commutator norm is 2 while that wrong intermediate bound is 0. It is a single named support-interface discriminator, not the literal coarse-L4 geometry, a dynamics simulation or proof of the uniform theorem. Its actual source/input/streams/receipt are preserved. The separate source-recording run is bookkeeping only. The failed inline bookkeeping attempt stopped at parsing; only its actual combined tool output exists, and no separate streams or exact start timestamp are fabricated. Root's binding and actual outer execution are preserved. The earlier incomplete broad overlap search remains incomplete and supplies no absence conclusion.

Lieb–Robinson propagation, weighted matrix bounds, light-cone volume estimates and local perturbation comparisons are existing machinery. The canonical [finite-volume LR walk-expansion context](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md) and [weighted quasilocal LR context](MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md) are attribution-only citations: the analytic source records a complete first-source read with its truncated middle recovered, and lines 1–120 only of the second. Their theorem constants and other conclusions are not imported. The root's prior-art exposure and the reviewer's more limited metadata exposure retain their exact separate scopes. No external theorem constant or generic-method novelty is imported. The already accepted neutral source-assembly programs and root review are reused solely as procedural patterns; their scientific theorem is not a premise.

Global-product and resonant-drive counterexamples, finite-penalty virtual corrections and the positive-lambda/static-control requirements remain. No global trace or leakage bound, compatible infinite-volume state, normalized postselection claim, native/autonomous apparatus, physical energy/time identification, photon sector or continuum law follows. This assembly executes only source identity, extraction and closure checks, with zero mathematical predicates and no archived scientific rerun.

## Complete unchanged accepted refinement

The following 15153-byte body is preserved exactly at 841e5f74. Its original opening/final pending-review assertions are historical; current acceptance and exposure are stated above. No mathematical sentence, formula, citation or source status is silently rewritten.

# Proposed geometric finite-time refinement of local penalty averaging

Status: root-authored conditional derivation, not independently reviewed or accepted. It does not change the already accepted four-body local-uniformity source. The purpose is to replace its exponential sufficient effective-time cost by a polynomial sufficient cost when the already declared cubic geometry is used. The constants are conservative; no optimal, practical, autonomous or native realization is claimed.

This proof reuses the accepted finite rotating-frame construction and matrix-chain commutator bound from root DERIVATION_V2.md, SHA fca3350c6572e7a60305974f5aba733910d0347847f859c7ea784d990d35f5ad, accepted by910939c9 after separate review76ecfbd2. The complete102-line source was reread for this extension. The second local source ac224bb872353875eb8bf996f10c403747d9800d0929e387755219467d77e777, already completely reviewed, supplies the literal uniform geometric supports; its sections1–4 were refreshed. The all-volume nonempty source2ddbcafc and physical budget45ea7ab8 are used only in the final literal corollary at their accepted identities. No binary-admission or neutral-preparation theorem is used.

Lieb–Robinson bounds, exponential reweighting, light-cone volume estimates and local perturbation comparisons are established machinery. The repository's July18 all-time nearest-neighbor walk note and weighted-quasilocal note already carry that machinery on supplied interaction classes. The first was read completely, with the initially truncated middle separately recovered; only lines1–120 of the weighted note were read for attribution. The external primary-author review by Kliesch, Gogolin and Eisert, [arXiv:1306.0716v2](https://arxiv.org/pdf/1306.0716), was inspected for its introductory scope and Theorems1–2 (PDF pages5–8). It describes bounded local propagation and spatial truncation. No numerical constant or proof step below is imported from that review. No generic-method novelty or exhaustive overlap search is claimed. The additional proposed result is the explicit composition with this campaign's finite Gauss averaging and physical-cap corollary.

## 1. Geometric stability for a perturbation with only a local norm

Let Omega be a finite subset of the unit cubic lattice Z^d, or a finite rectangular periodic cubic torus, with its ambient ordinary or periodic l1 metric dist. There is at most one interacting tensor factor per lattice site; idle factors may be included. Every metric ball satisfies, for real rho>=0,

    |B(i,rho)| <= (2 floor(rho)+1)^d <= (2rho+1)^d.          (1)

For the torus each coordinate has at most min(period,2floor(rho)+1) possibilities, so the same upper bound remains valid even after a ball fills the volume. No relation between rho and system size is required. For S nonempty, its rho-neighborhood B(S,rho) has size at most |S|(2rho+1)^d by a union bound. Disconnected S is allowed.

Let A=sum_Z a_Z be a static Hermitian interaction with nonempty fixed supports of cardinality at most k>=1 and metric diameter at most r>=1. Labels with the same support are counted separately. Assume

    sup_i sum_(Z contains i) ||a_Z|| <= g,   g>0.

Define the nonnegative matrix M_ij=sum_(Z contains i,j)||a_Z||. Its row sums are at most kg; it vanishes whenever dist(i,j)>r. Set v=2e kg. For every u>=0 and each i,

    sum_j exp(dist(i,j)/r) [exp(2uM)]_ij <= exp(vu).          (2)

Proof: in a term of M^n, the triangle inequality gives dist(i,j)<=sum_l dist(i_(l-1),i_l). Each nonzero matrix step has length at most r. Summing its weight with exp(length/r) costs at most e kg at each step. Thus the weighted row sum of M^n is at most (e kg)^n. The n=0 term is1. Summing the exponential series proves(2) without a volume factor. All entries are nonnegative, so no cancellation argument is used. In particular,

    sum_(j:dist(i,j)>rho) [exp(2uM)]_ij
        <= exp(vu-rho/r).                                  (3)

For a physical/reference observable O on S and an arbitrary passive reference, the accepted matrix-chain bound is

    ||[Q_X, exp(iuA)O exp(-iuA)]||
       <= 2||Q_X||||O|| sum_(i in S,j in X)[exp(2uM)]_ij.    (4)

It follows by the finite commutator/Duhamel recursion, selecting one site in each consecutive support overlap; those selections overcount all valid interaction chains. The zero-order diagonal term covers overlapping supports. Its proof and all hypotheses are carried by the accepted sourcefca3350c, section2. Passive reference factors do not enter M or geometric counting. We also use the universal bound2||Q_X||||O||.

Now let K(s)=sum_X K_X(s) be a Hermitian perturbation with an absolutely convergent labelled interaction decomposition on each finite carrier and

    sup_(s,i) sum_(X contains i) ||K_X(s)|| <= h.

Its supports need not have bounded cardinality, diameter, or connectedness. Identity terms may be dropped because their commutators vanish; all other supports are nonempty. Finite carrier size and this local norm give ordinary operator convergence, since sum_X||K_X||<=|Omega|h. The assertions below also hold for a finite list of terms. Take any rho>=0 and split the labels into those meeting B(S,rho) and those missing it.

For the near labels, the trivial commutator bound gives

    sum_(X meets B(S,rho)) ||[K_X(s),exp(iuA)O exp(-iuA)]||
        <= 2||O|| h |B(S,rho)|
        <= 2|S| ||O|| h (2rho+1)^d.                         (5)

Indeed sum_(X meets B)||K_X||<=sum_(j in B)sum_(X contains j)||K_X||<=h|B|. A support crossing the ball boundary is wholly placed in this near class. No assumption that K is local in metric range is hidden here.

For the far labels, every site of X lies outside the entire B(S,rho). Sum(4), interchange nonnegative summands, and use the per-site K norm and(3):

    sum_(X misses B(S,rho)) ||[K_X(s),exp(iuA)O exp(-iuA)]||
      <= 2||O|| h sum_(i in S,j outside B(S,rho))[exp(2uM)]_ij
      <= 2|S| ||O|| h exp(vu-rho/r).                         (6)

Choosing rho=rvu=2e rkg u makes the last exponential1. Combining(5–6) yields the proposed geometric stability integrand

    sum_X ||[K_X(s),exp(iuA)O exp(-iuA)]||
      <= 2|S| ||O|| h [(1+4e rkg u)^d+1].                   (7)

At u=0 the far contribution actually vanishes; the displayed bound merely overcounts it. No limit or large-u approximation is used. The global norm ||K|| can be extensive. It is the unperturbed A, not K, whose finite geometric range is used.

Let U_(A+K)(t) be the unitary propagator of A+K(s). Duhamel interpolation between that propagator and exp(-itA), using unitarity of the outer propagator and(7), gives for t>=0

    ||U_(A+K)(t)^* O U_(A+K)(t)-exp(itA)O exp(-itA)||
       <= 2|S| ||O|| h I_d(t;g),                            (8)

    I_d(t;g)=integral_0^t [(1+a u)^d+1]du
             =t+[(1+a t)^(d+1)-1]/[a(d+1)],
    a=4e rkg>0.                                            (9)

This comparison requires only piecewise continuous K(s) (and its stated summability) in finite dimension. It does not evolve O under K when estimating the commutator. Thus no geometric bound on the possibly long supports of K is needed. Equations(5–6), particularly this point, require separate scrutiny.

## 2. Periodic averaging with the geometric stability estimate

Take the accepted finite periodic interaction setting: H(s)=sum_Z h_Z(s), with period p>0, fixed nonempty supports of size<=k and diameter<=r, and local norm g=sup_i sum_(Z contains i)sup_s||h_Z(s)||. Every term is Hermitian and piecewise continuously differentiable. Its termwise average is A. Define

    F_Z(t)=integral_0^t [h_Z(s)-a_Z]ds,    F=sum_Z F_Z.

The mean-zero periodic integral is bounded using either endpoint of a period:

    ||F_Z(t)|| <= 2 min(theta,p-theta) sup_s||h_Z(s)||
               <= p sup_s||h_Z(s)||,

where theta is t modulo p. Hence F(0)=0 and the local norm of F is at most f0=pg. This is the corrected periodic-primitive argument, not the rejected coefficient substitution in the old root V1.

Set W(t)=exp(iF(t))U_H(t). The accepted differentiable exponential identity gives generator A+K(t), with

    K=sum_(n>=1) i^n/n! [n/(n+1) ad_F^n(H)
                        +1/(n+1) ad_F^n(A)].

The accepted overlap-count estimate for interactions gives a local norm bound

    ||ad_F^n(H)||_local, ||ad_F^n(A)||_local
        <= (2k f0)^n (n+1)! g.

Thus, with q0=2k f0<=1/4,

    h:=sup_t ||K(t)||_local
       <= g[(1-q0)^(-2)-1] <= 6g q0 =12k p g^2.             (10)

The scalar inequality follows from [(1-q)^(-2)-1]/q=(2-q)/(1-q)^2<=2/(3/4)^2<6 for0<q<=1/4. Atq=0 the expression is zero by continuity. The commutator-series supports grow with n, but the series is absolutely summable in the per-site norm and in ordinary operator norm on each finite carrier. This is precisely the unrestricted-K support class in section1; no assertion of a fixed range for K is made.

The final frame costs at most2|S| f0||O||, since

    ||exp(iF)O exp(-iF)-O|| <= ||[F,O]|| <=2|S| f0||O||.

There is no initial frame. Combining this with(8) and(10), for||O||<=1,

    ||U_H(t)^*O U_H(t)-exp(itA)O exp(-itA)||
       <= 2|S| p g [1+12kg I_d(t;g)].                       (11)

All terms are finite for every fixed t; the bound can exceed the trivial2 norm-difference cap. It is not an all-time smallness theorem. For any fixed physical output region and arbitrary passive reference, trace duality gives the same bound capped at2 for reduced output states, uniformly over all initial joint states. Empty physical support has exact zero difference. Ifg=0, H is zero up to discarded identities and there is no error; the divided formulas need not be used.

## 3. Literal Gauss penalty and the effective-time polynomial

Use the unchanged commuting integer-spectrum Gauss penalty N_G=sum_x G_x^2 and the static bare drive B on the declared evenL>=4 family. On the reducing precode R0,L, the full cycle/link/Gauss penalty agrees exactly with the Gauss-only evolution. The rotating drive H_I(t)=exp(i lambda N_G t)B exp(-i lambda N_G t) has periodp=2pi/lambda, lambda>0. Its average A acts on the initial K_L kernel as the unchanged compressed target. This is the accepted section2 reduction of sourceac224bb8; no assertion about all nonzero Gauss sectors is imported.

That source's analytic geometry gives k=57, r=36 and g=(10+11sqrt(3))J, uniformly over the declared even tori. Unchanged nonstream supports have diameter<=20; each rotated stream is supported on D_x union D_y, of size57 and periodic diameter<=36. These are fixed declared supports throughout each period.

The final fast Gauss conjugation replaces an output observable on S by one on Y consisting of S and the G supports originally meeting S. Commutativity prevents iterative enlargement. For each site touched by a Gauss term the union of its at most two30-site supports contains that site; an untouched site contributes just itself. Consequently |Y|<=c|S| withc=60, as in accepted root sourcefca3350c. The more conservative61 from the cutoff source is also permissible. For each final time t, this conjugated observable is held fixed during the Duhamel interpolation; no derivative of that observable is added. The metric counting in section1 applies to any shape of Y, with no connectedness requirement. The target state lies in ker N_G, so replacing O by its final Gauss conjugate leaves its target expectation unchanged.

Forlambda>=16pi kg, q0=4pi kg/lambda<=1/4. Equation(11) therefore proposes

    error_(S,reference)(t)
       <= min{2, (4pi c|S|g/lambda) P_d(gt)},               (12)

    P_d(z)=1+12kz
             +[3/(e r(d+1))] [(1+4e rkz)^(d+1)-1].        (13)

The algebra follows fromkg I_d(t;g)=kg t+[(1+4e rkg t)^(d+1)-1]/[4e r(d+1)]. Ind=3,

    P_3(z)=1+12kz+[3/(4e r)] [(1+4e rkz)^4-1].             (14)

It is a positive increasing degree-four polynomial forz>=0. The bound remains local in physical support and complete in the passive reference; it gives no global leakage estimate. It can be combined with the accepted direct exponential bound by taking their minimum once this new argument is independently accepted. No assertion that(12) is smaller for every finite time is made.

ForB=kappa B0 withg0=(10+11sqrt(3))J0>0, takeg=kappa g0 and physical timet=tau/kappa for0<kappa<=1. The complete polynomial argument is thenz=g0 tau, independent ofkappa and volume. At a selected finite effective horizon0<=tau<=tau_star, fixed output bound|S|<=s withs>=1, and tolerance0<epsilon<=2, it is sufficient to impose

    kappa <= lambda/(16pi k g0),
    kappa <= epsilon lambda/[4pi c s g0 P_3(g0 tau_star)].  (15)

The accepted whole-term physical budget is at most166lambda+beta kappa J0, withbeta=9+2sqrt(3), keeping its scalar and every penalty term. For any supplied positive physical capLambda choose

    lambda=Lambda/332,
    0<kappa<=min{1, Lambda/(2beta J0),
                    lambda/(16pi k g0),
                    epsilon lambda/[4pi c s g0 P_3(g0 tau_star)]}.      (16)

Each denominator is positive. The penalty consumesLambda/2 and the drive at mostLambda/2. Under the accepted nonempty-subcode construction, each declared even volume has admissible initial K_L states. The initial preparation remains supplied. For fixed positiveg0,Lambda,epsilon,s and other literal constants, choosing the maximum allowed right-hand side in(16) gives physical time at most a constant times tau_star(1+tau_star)^4, hence O(tau_star^5) as the requested effective horizon grows. This is a sufficient externally timed cost of this loose bound, not a lower bound or an optimized algorithm. The static finite-range multi-qubit controls still have to be supplied. J0=0 and empty output are stationary/trivial cases handled without division; tau_star=0 has exact zero dynamical error.

## 4. Review obligations and limits

The decisive new obligation is the near/far K-support split: an arbitrarily large K term meeting the geometric ball must be charged once by the local-norm incidence sum, while every site of a far term must lie outside that whole ball before applying the weighted M row bound. Check both labels and support intersections, finite-torus volume growth, the use of physical rather than interaction-graph distance, and the independence of the reference dimension. Check Duhamel ordering, final-frame cost, q0 constants and the effective-time substitution separately. A small finite check may target these steps, but a printed polynomial or numerical agreement does not prove the uniform theorem.

All previous global-product counterexamples, resonant time-dependent-drive exclusions, finite-penalty virtual corrections, positive-lambda requirement and supplied static-control premises remain. The error bound grows with time and is capped by2; it does not imply a uniform long-time approximation at fixedkappa. The new scaling chooses a slower physical drive for each requested horizon. It does not identify physical energy/time, derive a native clock/readout or photon sector, prove an infinite-volume state or continuum law, change physical axioms, or grant retained status. No independent reviewer has yet received or checked this new derivation.
