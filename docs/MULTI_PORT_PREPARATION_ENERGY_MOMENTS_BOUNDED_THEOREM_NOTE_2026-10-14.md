---
title: Preparation energy moments for finite multi-port Hamiltonians
claim_id: multi_port_preparation_energy_moments_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Preparation accuracy required for the supplied finite multi-port Hamiltonian
source_of_blocker_text: user_goal
reachability_to_target: supports
conditional_surface_status: same installed finite Hamiltonian, full original/reference marginal and actual auxiliary-defect premises
hypothetical_axiom_status: null
admitted_observation_status: null
status: proposed_retained
canonical_parent_binding_complete: true
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies: ["simultaneous_multi_port_three_pauli_bounded_theorem_note_2026-10-14"]
runner: scripts/preparation_moment_source_identity_2026_10_14.py
claim_type_reason: checked conditional moment bounds with a complete restricted-chain prerequisite; physical preparation and energy identification remain supplied
next_trace_action: establish or independently certify the stated preparation and physical calibration premises before physical use
---

Claim type: bounded_theorem

# What does imperfect auxiliary preparation cost in energy moments?

A mediator construction can approximate its target dynamics while carrying a large energy variance in its bare auxiliary vacuum. Imperfect preparation changes that distribution again. This note bounds the second change without discarding the first. It combines two checked finite arguments for the same installed Hamiltonian, and supplies the complete restricted-chain prerequisite used in the generic argument's length-dependent examples.

The scientific bodies are unchanged: the generic vacuum-block proof `be126506`, the sharper local-defect proof `de7e7916`, and the restricted placement proof `79d2388a`. Each appears in full below. Their original proposed or pending-review sentences are historical source text. Current conditional analytic acceptances are respectively `237b2dad`, `d7fa3588` and `8d3de83e`; their source assemblies were separately accepted under `702367be`, `825da3a2` and `b104daaf`. Exact identities and dispositions are preserved in the accompanying source manifest. These source decisions do not confer independent audit or retained status.

## Domain, comparison and actual energy costs

Both moment comparisons use exactly the same finite installed K, including every original factor, all auxiliaries and the actual scalar reserve. The original H is arbitrary within its stated finite norm bound and remains unchanged. The actual preparation may correlate old data, dirty factors, auxiliaries and an arbitrary passive reference. The required old-marginal estimate is a full old/reference trace-norm estimate; one-site data marginals do not replace it. Auxiliary excitation expectations and their certified upper bounds are supplied preparation information, not an apparatus for measuring them.

For the multi-port application, write

    K = H + c I + Delta L + sqrt(Delta) V,  Delta > 0,
    c = s0 + r_installed,
    J*V^2J = kappa_vac I,  kappa_vac = (209/16) sum_i |lambda_i|.

The exact ideal mean is Tr(rho H)+c. The exact ideal variance is Var_rho(H)+Delta kappa_vac. Original covariances, the coupling variance, full penalty strengths, scalar, elapsed time, precision and any installed positivity reserve remain charged. A smaller sensitivity bound does not lower those baseline costs or identify K with a native physical-energy observable. Conservation refers to two specified preparations evolved under this same closed K; it does not permit appending a new vacuum to a later old marginal.

The generic argument uses a scalar vacuum-column identity C*C=kappa I and its actual full excited block. The sharper argument uses the literal local penalty and the actual one- and two-excitation columns. In particular, two-flip contributions of anticommuting old Pauli ports cancel, while commuting pairs contribute. Shared old factors are therefore retained rather than replaced by independent cells.

The two proofs use different local symbols. In the generic proof, kappa is the physical column value Delta kappa_vac and q is the nonvacuum probability. In the sharper proof, kappa denotes kappa_vac, p is the nonvacuum probability and eta is the sum of local auxiliary excitation probabilities. The generic D is the excited block H_Q+E; the sharper D0 is the centered original operator H-m I. In the appendix, D=2h+(31/2)Lambda is a scalar bound coefficient, while D0 is the scalar prefactor in Delta_M=D0 M^6; the generic chain subsection writes that prefactor as D_0. None of these D symbols denotes the others. The generic epsilon_old and sharper epsilon both control the complete old/reference marginal. Equation numbers belong to their own proof, not to a shared numbering system.

For normalized states, the source bounds cover mean, centered second moment and scalar variance. Reference-valued moments require the additional epsilon_R=||sigma_R-rho_R||_1 terms stated in the sharper proof, including Delta kappa_vac epsilon_R for its centered second moment and the scalar-dependent contribution to its uncentered mean. Positive unnormalized blocks inherit homogeneous linear moment statements; a normalized rare outcome requires its actual probability. No operator-valued variance or complete-output accuracy theorem follows merely from these moment estimates.

## Proof obligations and dependency roles

The generic block expansion, positivity estimate and variance bookkeeping are proved in Part I. The literal local-population, square-column and reference-valued refinements are proved in Part II. Their common external mathematical parent is the [simultaneous multi-port theorem](SIMULTANEOUS_MULTI_PORT_THREE_PAULI_BOUNDED_THEOREM_NOTE_2026-10-14.md), canonical SHA256 `f02e80d2c69be61819c9fc43a8a3125cc1432f895c01b93a5e7081ec2b4d8755`, whose complete raw body remains `be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc`. The canonical identity is observed at commit `463fa381d9fe9403b6b6f3e3ce19505aa947edf2`, regular PR9574. The parent supplies the exact global K, full auxiliary-domain facts, vacuum scalar and paid resource contract.

The complete Appendix supplies the restricted `3 by 3` reserved-site chain construction used by Part I. It is an explicit internal prerequisite, not an invented canonical chain citation and not a new independent retained result. Its own sole theorem import is the same multi-port parent. Its fixed-time sufficient prescription Delta=D0 M^6, growing strengths and literal geometry remain conditional on all displayed premises. The newer chain-scaling proposal is not imported by this note, keeping later composition acyclic.

The earlier local-defect trace estimate `c163db2d` is preserved as comparison evidence. The two moment proofs already state and prove their required preparation estimates, so that trace result is not an additional theorem supplied by this publication. Its full body remains recoverable to check the historical coarse-bound comparison. Mathematical block, trace-norm, variance and projection tools are established machinery; no generic novelty claim is made.

The displayed local-defect exponents are sufficient bounds with tolerance-dependent constants. Exact inequalities take precedence over big-O notation, including at zero coefficients or H=0. Optional exact block dephasing has extra implementation, elapsed-time, control, calibration and reset costs. The appendix applies only to its reserved-site family and supplies no arbitrary occupied-site packing algorithm.

## Evidence and unresolved physical premises

The generic source was reviewed by a separate source-exposed block argument. The sharper source has an author's exact one-cell moment calculation on the full 16-dimensional auxiliary space and a separate reviewer's exact overlapping-port column calculation over all 32 old basis inputs with eight auxiliaries. The latter rejects a forced-commuting treatment. The restricted placement has its complete author and separate review evidence, including its incompatible-spare control. All recorded source exposure, actual programs, outputs, receipts and failures remain recoverable. A shared source family, prior parent authorship and exposure before selected checks are disclosed; the evidence is not presented as blind or model-diverse. No historical scientific computation was replayed for this publication.

The primary runner is a source-identity checker with zero mathematical predicates. It checks the declared complete inputs and reconstructs the three exact bodies and archived records; it does not prove the inequalities, rerun controls, certify geometry or supply an audit verdict. The identity manifest and byte/line maps distinguish current framing from historical records and allow exact reconstruction without duplicating complete proofs.

The strongest missing physical obligation is an implemented or certified preparation meeting the full old/reference marginal and auxiliary-defect premises while retaining the stated physical Hamiltonian and cost contract. Native preparation, local statistical certification and disturbance, common available strength caps, calibrated controls, physical energy identification, reader/reset and arbitrary occupied geometry remain supplied or open. This finite conditional result establishes no continuum, permanent-record or native-apparatus claim.

## Review record

The three accepted raw bodies are preserved verbatim. This grouping adds explanatory framing, a notation map and complete prerequisite placement; it alters no mathematical assertion or source boundary. Actual component review, integration checks and any later retained audit have distinct records. No audit verdict or platform, editable-prompt or physical-axiom change is part of the result. Provenance-only references are written as source identifiers; the one Markdown theorem link is the sole external citation edge.

## Part I. Complete generic vacuum-block argument

# Preparation moment sensitivity from the vacuum block

Proposed conditional analytic source, not yet separately reviewed or accepted. This addresses the moment cost of an imperfect auxiliary preparation for the already supplied multi-port Hamiltonian. It does not construct a preparation/certification apparatus, identify physical energy, or lower the actual ideal-state energy variance. No novelty claim is made for block-matrix or trace-norm inequalities.

The complete local-defect source c163db2da7ea4a26e8c4de0f097e645374e11485494c295d457e0a229c030a10 gives a general joint trace-distance certificate. Applying a full-space norm to that certificate is sufficient but can discard the actual vacuum-to-excited coupling size. The present argument instead computes the energy moments through the actual vacuum block. It does not alter or contradict that earlier general certificate.

## 1. Exact state and Hamiltonian premises

Let O include every original factor and every passive reference. Let A be m auxiliary qubits, J append the normalized auxiliary vacuum Omega, P=JJ*, and Q=I-P. For an arbitrary finite density operator sigma on OA, set

    rho=Tr_A sigma, q=Tr(Q sigma),
    r=sum_j Tr(n_j sigma), n_j=|1><1| on auxiliary j.

No independence, diagonal-state or absence-of-coherence premise is imposed. Q<=sum_j n_j, so q<=u:=min(1,r). Let rho_* be a specified complete old/reference target with

    ||rho-rho_*||_1 <= epsilon_old.

The trace norm, not half trace distance, is used. These are supplied properties of the actual input, not properties inferred from single-state samples or local old marginals.

Let K be the actual bounded nominal Hamiltonian. Suppose a known scalar s and a bounded original operator H satisfy the following complete operator identities. Write K'=K-sI and identify the P sector with O:

    K' = [ H   C* ] on P direct-sum Q,
         [ C   D  ]
    ||H||<=a, C*C=kappa I_O, kappa>=0,
    D=H_Q+E, H_Q=Q(H tensor I_A)Q, ||E||<=d.        (1)

The scalar can include an installed common reserve. Subtracting it in this calculation does not remove its physical energy or coefficient: differences of means between two normalized states and each state's variance are invariant under a common scalar translation. All states below use exactly the same installed K and physical coordinates. The reference is passive, so the Hamiltonian acts on it by identity.

The equality C*C=kappa I is a substantive structural premise. A general joint trace-distance bound alone does not give it. Define the ideal auxiliary extension sigma_0=J rho J* and the intended extension sigma_*=J rho_* J*.

## 2. Vacuum block identities and the coherence estimate

Write P sigma P=J tau J* and chi=Tr_A(Q sigma Q). Partial traces of the P/Q cross blocks vanish because the auxiliary vacuum is orthogonal to its complement. Consequently

    rho=tau+chi, chi>=0, Tr chi=q.                 (2)

Hilbert-Schmidt Holder gives

    ||P sigma Q||_1
      <= ||P sqrt(sigma)||_2 ||sqrt(sigma) Q||_2
      = sqrt(q(1-q))=:z.                          (3)

This remains valid at q=0,1. It is the only off-diagonal-state estimate required.

For K', the ideal mean is mu_0=Tr(H rho), with |mu_0|<=a. In the actual-minus-ideal mean, the H contribution on the Q block cancels exactly against Tr(H chi) from the missing P block. The remaining diagonal term is Tr(E Q sigma Q), while the cross term contains C. Hence

    |Tr(K sigma)-Tr(K sigma_0)|
       <= e_1(q):=d q+2 sqrt(kappa) z.             (4)

The coherence term cannot be dropped without a further state premise. For example, with a one-dimensional O, K'=[[0,c],[c,d]], c,d>0 and sigma the pure vector (sqrt(1-q),sqrt(q)), the mean difference is exactly d q+2c sqrt(q(1-q)). This is a narrow counterexample to diagonal-only pricing, not a claim of preparation impossibility.

Squaring the same block matrix gives

    P K'^2 P = H^2+kappa I,
    Q K'^2 Q = D^2+C C*,
    Q K'^2 P = C H+D C.                            (5)

The diagonal second-moment difference, after using (2), is

    Tr[Q sigma Q (D^2-H_Q^2+C C*-kappa I_Q)].       (6)

Since D=H_Q+E, ||D^2-H_Q^2||<=2ad+d^2. Also 0<=C C*<=kappa I_Q, so ||C C*-kappa I_Q||<=kappa; no extra factor two is needed. The cross block obeys

    ||C H+D C|| <= sqrt(kappa)(2a+d).

Therefore

    |Tr(K'^2 sigma)-Tr(K'^2 sigma_0)|
      <= e_2(q)
       :=(2ad+d^2+kappa)q
          +2 sqrt(kappa)(2a+d) z.                 (7)

Let delta_mu=Tr(K' sigma)-mu_0. The exact variance difference subtracts 2mu_0 delta_mu+delta_mu^2 from the second-moment difference. Thus

    |Var_sigma(K)-Var_sigma_0(K)|
       <= e_2(q)+2a e_1(q)+e_1(q)^2.              (8)

No covariance on old data was factorized. These are bounds on total moments of the same implementing Hamiltonian, not on a different target Hamiltonian H+W.

## 3. Intended old marginal and local supplied bounds

The exact ideal-state identities are

    Tr(K sigma_0)=s+Tr(H rho),
    Var_sigma_0(K)=Var_rho(H)+kappa.               (9)

The large kappa term is a real variance cost. It is independent of rho under (1), so it cancels when comparing ideal extensions of rho and rho_*:

    |Tr(K sigma_0)-Tr(K sigma_*)|<=a epsilon_old,
    |Var_sigma_0(K)-Var_sigma_*(K)|<=3a^2 epsilon_old. (10)

The variance inequality follows from the H^2 moment bound a^2 epsilon_old and the squared-mean bound 2a^2 epsilon_old. In particular, charging kappa epsilon_old here is unnecessary under the scalar C*C premise. This improvement would need modification if C*C were not scalar.

For a certificate based only on q<=u, use monotone upper envelopes

    E_1(u)=d u+2 sqrt(kappa) sqrt(u),
    E_2(u)=(2ad+d^2+kappa)u
              +2 sqrt(kappa)(2a+d) sqrt(u).       (11)

The replacement z<=sqrt(u) is deliberate. The function sqrt(q(1-q)) is not increasing on the whole unit interval, so substituting q=u directly into z is not justified for arbitrary u. The resulting complete sufficient bounds are

    mean error <= a epsilon_old+E_1(u),
    variance error <=3a^2 epsilon_old
                       +E_2(u)+2a E_1(u)+E_1(u)^2. (12)

These can be used with any certified upper bound on r; take its minimum with one. The right-hand sides are sufficient estimates, not assertions of sharpness. Under the stronger [sigma,P]=0 premise, the cross blocks vanish and one may instead use

    E_1^diag(u)=d u,
    E_2^diag(u)=(2ad+d^2+kappa)u.                  (13)

Local auxiliary dephasing is one supplied route to that premise, with its implementation/duration/control/reset costs still charged. An approximate dephasing output needs its own complete-state error budget; no unpriced approximation is inserted into (13).

The estimates hold at every time under the same closed K evolution because that evolution conserves its total first and second moments. This fact does not equate K-energy to target H+W energy or a native physical-energy observable. A uniform preparation-channel statement would require the input premises uniformly over all original/reference inputs.

## 4. Checked-source multi-port specialization, pending separate review here

The complete multi-port source is be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc. It supplies

    K_Delta=H+s_0 I+Delta L+sqrt(Delta)V,
    L J=0, J*VJ=0, ||L||=4M, ||V||<=v,
    J*V^2J=(209/16)ell I,
    ell=sum_i |lambda_i|,
    v=4 sum_i sqrt(209|lambda_i|/64).              (14)

The last identity is also directly visible from its four distinct auxiliary flips per cell: VJ has orthogonal auxiliary columns, each old Pauli squares to I, and their squared amplitudes sum to 4 sum_i t_i^2=(209/16)ell. Distinct cells have distinct clean auxiliaries, so cross columns remain orthogonal even for noncommuting old Pauli supports. This uses the actual global vacuum, not independent cell evolutions.

Taking s=s_0, or s=s_0+R_pos for an actually installed scalar reserve, gives (1) with

    a=||H||,
    kappa=(209/16)Delta ell,
    d=4M Delta+sqrt(Delta)v.                       (15)

Here C=sqrt(Delta)Q V J and E=Q(Delta L+sqrt(Delta)V)Q. All identities are on the full old/reference space; no invariant old-sign sector is substituted. The possible large Q-sector norm d remains in (12). The result improves a sensitivity estimate, not the growing penalties, port strengths, full norm, scalar or baseline variance of the construction.

The chain-placement source 79d2388a7f6e2ce36d8b1055bd2ad80149a9e5375ff7f23248391d72bf5692ff supplies a restricted reserved-strip family with m=4M and one sufficient Delta=D_0 M^6 under fixed tolerance/time, bounded coefficients and ||H||<=hM. With |lambda_i|<=Lambda, define fixed upper constants

    K_c=(209/16)D_0 Lambda,
    D_c=4D_0+4 sqrt(D_0) sqrt(209 Lambda/64).

For every M>=1,

    kappa<=K_c M^7, d<=D_c M^7, a<=hM.            (16)

If each actual auxiliary excitation is at most nu_M, then u<=min(1,4M nu_M). Equations (11)-(12), with their actual constants, imply these sufficient budgets:

* Fixed absolute mean-error tolerance: choose epsilon_old bounded by a sufficiently small constant times M^-1 and nu_M by a sufficiently small constant times M^-8. Both terms d u and 2sqrt(kappa u) are then bounded by arbitrarily small fixed constants.
* Fixed absolute variance-error tolerance: choose epsilon_old bounded by a sufficiently small constant times M^-2 and nu_M by a sufficiently small constant times M^-22. The potentially largest coherence term sqrt(kappa)d sqrt(u) is then bounded independently of M; choosing its constant small makes it arbitrarily small. The diagonal d^2 u term decays as M^-7, and E_1(u)=O(M^-7), so the remaining terms also obey a uniform small budget.
* Under the additional exact block-diagonal preparation premise, nu_M of sufficiently small order M^-15 suffices for fixed variance tolerance; d^2u is then bounded, and the coherence terms are absent. Fixed mean tolerance still has the conservative M^-8 sufficient local budget from (15).

These statements mean there exist sufficiently small M-independent constants for prescribed positive moment tolerances. They do not mean an arbitrary big-O constant meets a chosen tolerance. The exact acceptance inequalities are (12) or (12) with (13); zero coefficients and zero H cause no division-by-zero exception because these inequalities, rather than divided formulas, are primary.

For comparison, the earlier generic joint-trace/full-norm substitution gave coherent local sufficient budgets M^-15 for the mean and M^-29 for the variance. The present M^-8 and M^-22 estimates exploit (1), especially the much smaller vacuum coupling and scalar ideal variance contribution. Neither set is a necessary lower bound or an optimal hardware threshold. The joint output-state preparation certificate remains a separate requirement if output accuracy is also demanded; at these vanishing budgets its supplied bound can be charged explicitly rather than inferred from moments alone.

## 5. Evidence plan and outstanding obligations

This is a complete proposed argument. Root has checked the displayed block expansion, trace/marginal cancellation, scalar-variance cancellation and exponent substitution analytically. Root has not run a scientific program for it, and no independent reviewer has yet seen this candidate. The underlying exact parent bodies and their prior conditional acceptance are reused only for (14) and the stated chain costs; the new sensitivity theorem still requires selective separate review.

A useful tiny control would retain an actual coherent auxiliary state and compute the complete first and second moments directly, distinguishing (12) from an erroneously diagonal-only price. A different independently selected fixture or analytic block derivation is preferable to replaying a formula as its own test. Failed checks or material qualifications must remain preserved. No blanket Lean, simulation or audit gate is imposed, and no computational PASS would replace the general proof.

Physical identification of the apparatus Hamiltonian, actual auxiliary preparation, nondestructive/statistical certification of local defects, complete old/reference marginal control, common strength caps, calibration, reader/reset and arbitrary occupied-site placement remain unresolved. The statement makes no change to physical axioms or editable prompts and grants no retained/audit or publication status.

## Part II. Complete sharper local-defect argument

The following body uses its own notation as described above. Its original pre-candidate and pending-review language is historical.

# Preparation sensitivity from the actual multi-port vacuum block

This is an independent pre-candidate derivation from the already exposed and conditionally accepted multi-port source `be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc`. It does not read or assume the new root preparation-moment candidate. The author of this check previously reviewed the parent and related mediator constructions; this is neither a blind nor a model-diverse derivation. Its new claims remain proposed pending separate review. No preparation procedure, source acceptance, physical axiom, native interaction or retained audit is supplied here.

## 1. Exact Hamiltonian and the preparation information

Keep the parent's finite original system D, its arbitrary unchanged Hermitian H with `||H||<=h0`, all dirty original factors, and all 4M fresh auxiliary qubits. A passive reference R can have arbitrary finite dimension and arbitrary correlations. Within cell i, write the auxiliaries as `(a_i,b_i,a'_i,b'_i)`, with `n=(I-Z)/2` and `S_uv=(X_u X_v+Y_u Y_v)/2`. The exact operators are

    N_i=n_a+n_b+n_a'+n_b',
    L_i=N_i+(1/4) B_i(n_b-n_b')-(1/4)(S_ab+S_a'b'),
    L=sum_i L_i,                 N=sum_i N_i,
    V_i=t_i A_i(X_a+X_a')+q_i C_i(X_b-X_b'),
    V=sum_i V_i,
    t_i=sqrt((209/64)|lambda_i|),
    q_i=sign(lambda_i)t_i,
    ell=sum_i |lambda_i|,        s0=(29/2)ell.

The old single-qubit Pauli factors A_i, B_i, C_i may overlap and fail to commute between cells. They commute within a cell because the three original sites there are distinct. No simultaneous old-data eigenbasis is assumed. The exact physical generator throughout this note is

    K=H+c I+Delta L+sqrt(Delta)V,        c=s0+r, Delta>0.       (1)

Here r is any fixed actually installed scalar reserve, including the parent's optional `r=h0+sqrt(Delta)v`. It is the **same** K and the same c in both preparation comparisons. None of the bounds changes K, deletes a scalar, retunes Delta, or replaces the physical reference dynamics. A changed or uncertain Hamiltonian requires a separate calibration allowance.

Let J append the complete auxiliary vacuum, P=JJ*, Q=I-P. For a normalized actual state sigma on D,A,R and a normalized intended old/reference state rho on D,R, define

    tau=Tr_A sigma,               epsilon=||tau-rho||_1,
    delta_u=Tr(sigma n_u),        eta=sum_u delta_u=Tr(sigma N),
    p=Tr(sigma Q) <= min(1,eta),  epsilon_R=||tau_R-rho_R||_1.
                                                               (2)

All traces include the passive reference. Epsilon is a **full old/reference** marginal bound, not a collection of one-site fidelities. Delta_u are actual auxiliary excitation probabilities, or may be replaced by certified upper bounds as specified below. They are not asserted to be physically measurable at no cost. The ideal comparison state is J rho J*. A local excitation certificate alone cannot bound a change in the old input H-distribution.

Flatten the four ports per cell into a list `(g_u,P_u)` so `V=sum_u g_u P_u X_u`: the coefficients are `(t_i,q_i,t_i,-q_i)` on `(a_i,b_i,a'_i,b'_i)` and the old factors are `(A_i,C_i,A_i,C_i)`. Set

    kappa=sum_u g_u^2=4 sum_i t_i^2=(209/16)ell,
    v=sum_u |g_u|=4 sum_i t_i.                               (3)

The following parent facts are retained on the entire auxiliary Hilbert space:

    L>=N/2>=Q/2,       ||L||=4M,       LJ=0,
    J*VJ=0,            J*V^2J=kappa I.                       (4)

In particular, the actual baseline moments are

    m=Tr(rho H),        mu0=m+c,
    nu0=Var_rho(H)+Delta kappa.                             (5)

The baseline coupling variance `Delta kappa` remains a paid resource. Every old covariance remains in `Var_rho(H)`. Scalar r changes mu0, but not nu0. Closed evolution of this same K conserves the actual total moments; a moment comparison is not an output-channel simulation, work extraction, reset, or reader theorem.

## 2. Local population estimates and the mean

For one auxiliary pair, `-n_u-n_v<=S_uv<=n_u+n_v`; this follows on its zero-, one- and two-excitation blocks. Also `-n_b-n_b'<=B_i(n_b-n_b')<=n_b+n_b'`. Hence, without assuming that different B_i commute,

    L <= (5/4)N_a+(3/2)N_b,                                 (6)

where N_a counts a,a' and N_b counts b,b'. With eta_a,eta_b their expectations define

    u=min{(5/4)eta_a+(3/2)eta_b, 4M p}.

Then `0<=Tr(sigma L)<=u<=3eta/2`, and functional calculus gives `L^2<=4M L`. Since L annihilates P, these estimates also hold on Q sigma Q.

Positivity of the 2-by-2 state block at auxiliary qubit u, followed by the Hilbert-Schmidt Cauchy-Schwarz inequality, gives

    |Tr(sigma P_u X_u)| <= 2 sqrt(delta_u(1-delta_u)).

This allows arbitrary correlations with every other auxiliary, D, and R. Thus, with

    w=min{v, 2 sum_u |g_u|sqrt(delta_u(1-delta_u))},

one has `|Tr(sigma V)|<=w<=2 sqrt(kappa eta)`. No sum of local trace distances is used. Subtracting the two means in (1), the identical scalar cancels exactly, giving

    |mu_sigma(K)-mu0| <= E1:=h0 epsilon+Delta u+sqrt(Delta)w
                       <=h0 epsilon+(3/2)Delta eta
                                      +2 sqrt(Delta kappa eta).    (7)

The inequality remains valid when only upper bounds on eta and epsilon are available. For the sharper individual-probability expression, an upper bound d_u replaces `sqrt(delta_u(1-delta_u))` by `sqrt(d'_u(1-d'_u))`, where `d'_u=min(d_u,1/2)`. Simply substituting a large upper bound into the nonmonotone square-root expression would be invalid. For u use a certified p upper bound, or drop its `4M p` branch.

## 3. A second vacuum-block identity

Let `D0=H-m I` and choose a certified `d>=||D0||` (the state-independent choice `d=2h0` is sufficient). Write `K0=K-mu0 I=D0+Delta L+sqrt(Delta)V`. Define

    kappa2=4 sum_{u<v : [P_u,P_v]=0} g_u^2 g_v^2.
                                                               (8)

The sum is over the actual finite port list, including distinct auxiliary ports that act on the same old factor. Each pair of Hermitian Pauli factors either commutes or anticommutes. Applying V twice to vacuum gives

    V^2J=kappa J+
       sum_{u<v} g_u g_v {P_u,P_v} tensor |u,v>.

Distinct auxiliary two-excitation words are orthogonal. Anticommuting pairs contribute zero; for a commuting pair the anticommutator is twice a unitary. Therefore the exact identity is

    (QV^2J)*(QV^2J)=kappa2 I,
    0<=kappa2<=2(kappa^2-sum_u g_u^4)<=2kappa^2.                (9)

This is not an independent-cell tensor product or a claim that the old factors commute. Shared noncommuting factors enter explicitly in (8).

On the total one-excitation sector, L is a direct sum over the occupied cell/path. Each corresponding old-dependent 2-by-2 block is `[[1,-1/4],[-1/4,1 +/- B_i/4]]`. Its largest eigenvalue is bounded by

    l1=(9+sqrt(5))/8 <3/2.                                   (10)

Diagonalizing B_i for that single block is valid; a common eigenbasis for different B_i is unnecessary. Put F=VJ, so `F*F=kappa I`. The exact off-vacuum column of the centered square is

    C:=Q K0^2 J
      =sqrt(Delta)(F D0+D0 F)+Delta^(3/2)L F
                                      +Delta QV^2J.          (11)

The first two terms have auxiliary number one; the last has number two. Their ranges are orthogonal. Equations (9)-(10) prove the full operator bound

    ||C|| <= gamma:=sqrt{Delta kappa(2d+Delta l1)^2
                                      +Delta^2 kappa2}.      (12)

A separately justified smaller bound on this same column can replace gamma. Taking `l1=3/2` and `kappa2=2kappa^2` gives a simpler fully explicit upper bound. This column has order `Delta^(3/2)sqrt(kappa)` at large Delta, rather than the square of the full penalty norm.

## 4. Complete second-moment and variance sensitivity

Define `cv=max{kappa,v^2-kappa}` and

    RQ=4M Delta^2 u + Delta cv p
         +2Delta(d+sqrt(Delta)v)sqrt(4M p u)
         +2sqrt(Delta)d v p,
    E2=d^2 epsilon+2gamma sqrt(p(1-p))+RQ.                     (13)

Then for every normalized sigma,rho and every passive reference,

    |Tr(sigma K0^2)-nu0| <= E2,                              (14)
    -E2-E1^2 <= Var_sigma(K)-nu0 <= E2,
    |Var_sigma(K)-nu0| <= E2+E1^2.                           (15)

Proof of (14). Subtract the block-diagonal operator `D0^2+Delta kappa I` and call the difference T. The vacuum identity makes `PTP=0`. Its P-Q column is exactly C. Positivity of sigma gives `||P sigma Q||_1<=sqrt(p(1-p))`, so the two off-diagonal contributions have absolute value at most `2gamma sqrt(p(1-p))`. For the Q-Q contribution use the exact expansion

    T=Delta^2 L^2+Delta(V^2-kappa I)+Delta{D0,L}
                    +sqrt(Delta){D0,V}+Delta^(3/2){L,V}.     (16)

The Q-block has trace p. Its L-square expectation is at most `4M u`. Since `0<=V^2<=v^2 I`, the norm of `V^2-kappa I` is at most cv. Cauchy-Schwarz bounds the three anticommutators by, respectively,

    2d sqrt(4M p u),       2d v p,       2v sqrt(4M p u).

These are exactly RQ after their coefficients in (16). None uses `[H,L]=0` or `[L_i,L_j]=0`. Finally `Tr(sigma D0^2)-Tr(rho D0^2)` is bounded by `d^2 epsilon`; the scalar `Delta kappa` has identical expectation in both normalized states. This proves (14).

For (15), let `delta_mu=mu_sigma(K)-mu0`. The exact identity

    Var_sigma(K)=Tr(sigma K0^2)-delta_mu^2

and (7) give both sides. In particular the reference mean mu0, which contains the actual reserve, is not substituted for the actual mean when computing variance. The physical scalar never disappears from the physical mean, but it cancels from a same-Hamiltonian variance sensitivity exactly as it must.

If p is not supplied, use `p<=min(1,eta)` in increasing terms. For the off-diagonal square root, either use `sqrt(eta)` or maximize over `0<=p<=min(1,eta)`; substituting p=eta when eta>1/2 without this maximization is not valid. A compact monotone certificate using only eta and epsilon is

    E2 <= d^2 epsilon+2gamma sqrt(eta)+q eta,
    q=6M Delta^2+Delta cv
          +2Delta sqrt(6M)(d+sqrt(Delta)v)+2sqrt(Delta)d v.    (17)

Thus local defect and the full old/reference marginal certificate give explicit finite mean/variance tolerances. For eta<=1 let `k1=(3/2)Delta+2sqrt(Delta kappa)`. The sufficient bound

    |Var_sigma(K)-nu0|
       <=d^2 epsilon+2h0^2 epsilon^2+2gamma sqrt(eta)
                                      +(q+2k1^2)eta          (18)

follows from (7), (15) and `(x+y)^2<=2x^2+2y^2`. This is a preparation-quality requirement, not a method for achieving that quality. There is no assertion that it is optimal or uniformly smaller than every possible full-state trace estimate. At fixed M and coefficients its coherent defect coefficient scales as `Delta^(3/2)` rather than the `Delta^2` coefficient obtained by applying the full-norm variance bound to a generic `O(sqrt(eta))` state error. The `Delta^2 M eta` term and the baseline `Delta kappa` remain.

## 5. Reference-complete meaning and its limits

The proofs above act on the actual joint sigma and use the full epsilon in (2); no product or classical-reference assumption is made. A stronger linear statement makes this explicit. Let `M_sigma(O)=Tr_DA[(O tensor I_R)sigma]`. For the centered first moment, dualizing against any Hermitian reference contraction gives

    ||M_sigma(K0)-Tr_D(D0 rho)||_1
                          <=d epsilon+Delta u+sqrt(Delta)w.  (19)

The same duality and Cauchy-Schwarz proof of (14) gives

    ||M_sigma(K0^2)-[Tr_D(D0^2 rho)+Delta kappa rho_R]||_1
                                        <=E2+Delta kappa epsilon_R. (20)

For the scalar trace in (14), the last term cancels because both states have trace one. For a reference-valued moment it does not cancel if the actual reference marginal differs. For the **uncentered** physical first moment an additional `|mu0| epsilon_R` is sufficient on top of (19). If the preparation acts only on D,A and preserves the reference marginal, epsilon_R=0. These distinctions prevent a scalar-shift cancellation from being misrepresented as an equality of arbitrary reference-valued records. No nonstandard operator-valued variance is asserted.

These are moment bounds, not a full trace-distance, CQ-history, normalized postselection, or readout guarantee. Positive unnormalized blocks have homogeneous linear moment statements, but normalizing a rare block needs its actual probability; (15) is stated for normalized input states. A common external reference, arbitrary dirty original factors and their old covariances are retained throughout.

The entire spatial/strength/preparation/read-time contract of be8f is unchanged: supplied fresh auxiliary sites and initial quality; unchanged arbitrary H; the installed scalar and all actual local loads; finite Delta; external calibration and timing. The physical energy distribution is not the scalar Pauli coefficient, and a small moment sensitivity does not make the baseline distribution free. A different implemented generator, an additional operating interval, or a reader has its own costs. No new packing, native, common-cap, efficient, permanent-record or reset theorem is inferred.

## 6. Independently selected exact discriminator, fixed before execution

Use one actual parent cell, `lambda=64/209`, so t=q=1, `kappa=4`, `s0=928/209`, with H=0 and old Pauli eigenvalues A=B=C=+1. This is a legitimate invariant old subspace of this particular allowed H. Retain all sixteen auxiliary basis states and the actual L,V. Take Delta=16. The optional parent positivity reserve is r=16 and will be compared with r=0 without changing any other term. A passive entangled old/reference spectator may be appended without affecting these exact moment computations; the general reference claim rests on the proof, not on that spectator observation.

Choose once `a=2499/2501`, `b=100/2501`, so `a^2+b^2=1`. Compare the two coherent states `psi_+=a|0000>+b|1000>` and `psi_-=a|0000>-b|1000>`, and their common dephased mixture. Their old/reference marginal is identical and their local defects agree: only the a port has `delta_a=p=b^2`. With bit ordering `(a,b,a',b')`, |1000> denotes the first-port excitation, irrespective of integer endianness in the program. Direct analytic matrix entries predict

    (L^2)_aa=17/16,        (L V Omega)_a=3/4,
    kappa2=24,
    ||Q(K-s0 I)^2 Omega||^2=Delta^3(33/8)+24Delta^2=23040.

For the coherent signs the predicted values are

    mu-s0=Delta p +/-2sqrt(Delta)ab,
    Tr[sigma(K-s0 I)^2]-4Delta
                   =(17/16)Delta^2 p +/- (3/2)Delta^(3/2)ab,
    Var(K)-4Delta = preceding line - (mu-s0)^2.              (21)

The dephased state drops exactly the displayed ab terms; its mean shift is Delta p. The r=16 reserve must add exactly16 to each mean and zero to each variance. The selected program will compute these from exact rational 16-by-16 matrices, not from (21), then compare the formulas. It will report the discarded-coherence residual and the missing-baseline error; it will not import parent or new-candidate code, perform a parameter sweep, or simulate the full original model.

As an analytic family with `b=sqrt(eta)` tending to zero, (21) gives a leading variance change of sign-dependent `(3/2)Delta^(3/2)sqrt(eta)`. Therefore a universally linear-in-eta variance bound for arbitrary coherent preparation cannot be justified merely by local populations and an exact old marginal. This is a precise obstruction to that shortcut, not a no-go for preparation or an optimality theorem for every coefficient. Likewise, with eta=0 but a changed old input, H's mean/variance can change; omitting epsilon would fail independently.

The complete argument and complete selected program will be sealed before the first run. Actual execution, failed attempts if any, all raw streams, a source-before/after receipt and the resulting limited disposition will be archived separately. This note is not amended in response to unseen root-candidate formulas.

## Appendix. Complete restricted-chain prerequisite

This unchanged accepted argument supplies the restricted geometry and sufficient resource scaling invoked in Part I. Its opening pending-assessment language is historical. The later chain-scaling refinement is not used here.

# A finite noncommuting three-Pauli chain in a 3 by 3 cubic strip

**Conditional placement/application candidate; separate assessment pending.** For every finite M>=1 this note gives explicit original coordinates and4M disjoint clean auxiliary positions for the accepted simultaneous multi-port theorem. The target supports form a connected chain, with consecutive targets anticommuting when M>=2. The enclosing ordinary open box has9(M+1) sites. Original H remains an identical summand on its original factors, at the same physical time. This is a restricted family, not arbitrary hypergraph packing, a compiler for a fully occupied L4 box, native initialization/readout or a fixed-control-cap theorem.

The sole mathematical theorem imported is the complete simultaneous source `be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc`, accepted unchanged under `72484571373fe450298b11763f71680097a53543368a7136e588e5ae181da7e6`, with root review `2f2de29a4722863a276fc3b6752757184a09f2d5228082ae41b67cb795dacbb2`. Its full proof and both current root bodies were read. This author wrote that source; no blind-independence claim is made. Root supplied no coordinate construction for this task. The result below discharges a new restricted placement premise and substitutes its resource parameters; it does not rerun or extend the parent's general operator theorem.

## 1. Fixed original sites and the periodic cell maps

Fix an integer M>=1. All coordinates below are chosen before specifying the original H; after that H and its factors are not moved or modified. Work in the ordinary, nonperiodic cubic box

    B_M={0,...,M} x {0,1,2} x {0,1,2}.

For every i>=0 put r=i mod4 and define

    (Y_0,Y_1,Y_2,Y_3)=(0,1,2,1),
    (Z_0,Z_1,Z_2,Z_3)=(1,2,1,0),
    d_i=(i,Y_r,Z_r),
    (s_i^y,s_i^z)=(+,+),(+,-),(-,-),(-,+) respectively.

Let beta=(1,0,0). Define the other two signed unit vectors by

    eta_i=(0,0,s_i^z), gamma_i=(0,s_i^y,0),  i even;
    eta_i=(0,s_i^y,0), gamma_i=(0,0,s_i^z),  i odd.

They are three orthogonal signed coordinate vectors. Directly from the four-entry table,

    d_(i+1)=d_i+beta+eta_i+gamma_i,
    gamma_(i+1)=-eta_i.                              (1)

The first identity also holds when r=3 because the transverse coordinates return to their r=0 values. The second follows because exactly the eta_i component changes sign at the next step, and the transverse roles switch. Thus these are all-i identities, not an extrapolation from a finite layout test.

For cell i=0,...,M-1 choose the three original roles and four auxiliary roles

    x_i=d_i,        y_i=p_i=d_i+eta_i,       z_i=d_(i+1),
    a_i=d_i+beta,  b_i=d_i+eta_i+beta,
    a'_i=d_i+gamma_i,  b'_i=d_i+eta_i+gamma_i.         (2)

The map from the parent cell is

    (u,v,w) -> d_i+u eta_i+v beta+w gamma_i.           (3)

It is a translation and signed permutation of cubic coordinates. In particular it sends the parent's x000,y100,z111,a010,b110,a'001,b'101 to(2). It changes neither a Pauli basis nor an already specified physical Hamiltonian. The eighth vertex is

    w_i=d_i+beta+gamma_i=d_(i+1)-eta_i.               (4)

Original factors include every d_i,0<=i<=M, and every p_i,0<=i<M. Additional original/dirty/spectator factors may occupy any other box sites except the reserved auxiliaries in(2), or be supplied outside the box. H is any finite Hermitian operator on those original factors, with a supplied bound h0>=||H||. It acts as identity on the newly appended auxiliary factors. This is an explicit vacancy/initialization and background-support hypothesis, not a procedure for removing an old qubit or old coupling from an occupied site.

## 2. Collision-free placement for every finite length

Let C_i be the eight-vertex unit cube generated by beta,eta_i,gamma_i at d_i. Its x coordinates are i and i+1. Hence C_i and C_j are disjoint for |i-j|>=2. Consecutive transverse step signs differ on exactly the eta_i axis and agree on the other axis. Their two closed cubes therefore intersect in the edge on the eta_i axis,

    C_i intersection C_(i+1)={d_(i+1), w_i}.         (5)

At x=i+1 their coordinate on the nonflipping transverse axis must equal its common endpoint; on the flipping axis both endpoint values occur. This proves exactly the two vertices in(5). In C_i, w_i is the single unused vertex. Equation(1) gives

    w_i=d_(i+1)+gamma_(i+1)=a'_(i+1).               (6)

Thus w_i becomes a fresh auxiliary of the next cell, rather than a second common occupied vertex. The occupied seven-vertex sets of consecutive cells intersect only at d_(i+1), which is an original site in both. Nonconsecutive occupied sets are disjoint. Within each cell all seven roles are distinct. These facts prove simultaneously that all4M auxiliary sites are distinct, every auxiliary avoids every original role in every cell, and the only shared original roles are z_i=x_(i+1).

It is important that the parent says an unused vertex *may* contain an arbitrary spectator for a single supplied cell, not that all such choices can be combined. Here w_i for i<M-1 is reserved as the next clean auxiliary. Declaring all w_i to be old occupied factors would violate the global premise at exactly those M-1 sites. The final w_(M-1) is unrestricted. This is an explicit compatibility condition, not a no-go for other layouts.

Every parent edge

    x-a, x-a', z-b, z-b', y-b, y-b', a-b, a'-b'

maps to a unit step along one of beta,eta_i,gamma_i. All added two-body terms are therefore ordinary nearest-neighbor terms in the fixed open box. Edges cannot coincide across cells: occupied-cell intersections have at most one vertex, while an edge has two. The selected interaction graph is connected since each seven-vertex cell graph is connected and successive graphs share d_(i+1).

There can be additional ordinary-neighbor contacts between active sites that are not selected edges. The contract specifies the literal parent Hamiltonian, not an automatically coupled induced lattice graph. Unlisted auxiliary couplings must be absent, or their full operator contribution must be included in the implementation-error budget over T. Geometry alone does not manufacture this addressability or control.

## 3. Counts, degree and genuinely noncommuting targets

Each step adds one new connector d_(i+1), one branch original p_i, and four auxiliaries. The original p_i have first coordinate i and differ from d_i by eta_i, so they are all distinct from connectors and each other. Consequently the required inventory is

| Quantity | Exact count |
|---|---:|
| Required original data factors | 2M+1 |
| Distinct fresh auxiliaries | 4M |
| Port-active physical sites | 6M+1 |
| Selected distinct ordinary-neighbor edges | 8M |
| Parent Pauli/identity occurrences before aggregation | 15M |
| Vertices in the union of the closed unit cubes | 6M+2 |
| Sites in the declared enclosing box | 9(M+1) |
| Other box sites outside the port-active set | 3M+8 |

The cube-union count is8M-2(M-1), since only successive cubes intersect and no vertex is in three cubes. Of that union only w_(M-1) is outside the active set; all earlier w_i are already counted by(6). The box size is a convenient exact declared footprint, not a minimal enclosing volume for short lengths. If every box site carries a qubit, the3M+8 other sites can be arbitrary original spectators, giving5M+9 original factors and4M fresh auxiliaries. H may activate additional original spectators;6M+1 counts the port inventory, not every possible support of arbitrary H.

The selected graph has3M+2 vertices of degree2,2M vertices of degree3, and M-1 vertices of degree4. In detail the two endpoint connectors and M branch originals have degree2; a_i,a'_i have degree2; b_i,b'_i have degree3; each internal connector has degree4. At d_i,1<=i<M, the previous z-role neighbors are d_i-gamma_(i-1) and d_i-beta, while the new x-role neighbors are d_i+beta and d_i+gamma_i=d_i-eta_(i-1). These four are distinct. Summing degrees gives16M=2(8M). There is no degree overload, and no original site is used in more than two cells.

Use fixed one-site Pauli operators

    A_i=Z_(d_i), B_i=Z_(p_i), C_i=X_(d_(i+1)),
    P_i=Z_(d_i) Z_(p_i) X_(d_(i+1)).                 (7)

Consecutive supports intersect only at d_(i+1), where X from P_i meets Z from P_(i+1). Therefore P_i P_(i+1)=-P_(i+1)P_i, while nonneighbors have disjoint supports and commute. For real nonzero lambda_i,lambda_(i+1), the commutator of the weighted terms has norm2|lambda_i lambda_(i+1)|. More explicitly P_i P_(i+1) is -i times

    Z_(d_i) Z_(p_i) Y_(d_(i+1)) Z_(p_(i+1)) X_(d_(i+2)),

so the commutator has the corresponding -2i phase. For M=1 there is just one three-body term; the noncommuting assertion begins at M=2. The incidence graph of target supports is exactly a path.

In this particular family the B_i factors are disjoint, so different bare L_i actually commute. This does not make the targets commute: neighboring drive factors act as X and Z on their common original connector. No claim is made that the geometry fixture independently tests the parent's more general noncommuting-penalty clause. Arbitrary original H can also fail to commute with all these factors.

## 4. Literal simultaneous Hamiltonian and imported error theorem

Set n=(I-Z)/2 and S_uv=(X_u X_v+Y_u Y_v)/2. For any supplied real coefficients lambda_i put

    ell=sum_i |lambda_i|, c=209/64,
    t_i=sqrt(c|lambda_i|), q_i=sign(lambda_i)sqrt(c|lambda_i|),
    s_i=(29/2)|lambda_i|, s0=sum_i s_i.

At zero lambda use t_i=q_i=0. On the positions(2), define the actual static operator

    L_i=N_i+(1/4)B_i(n_bi-n_bi')-(1/4)(S_ai,bi+S_ai',bi'),
    L=sum_i L_i,
    V=sum_i[t_i A_i(X_ai+X_ai')+q_i C_i(X_bi-X_bi')],
    K_Delta=H+Delta L+sqrt(Delta)V+s0 I,  Delta>0.     (8)

H is precisely the originally supplied summand. The auxiliaries start in the jointly supplied product vacuum Omega; J appends Omega and does not modify any original/reference state. Equations(2)–(6) discharge the parent's geometric/disjointness premises, and(7) supplies its nonidentity Pauli roles with C_i=X. Thus its full-space facts apply: L>=N_tot/2, ker L=original space tensor Omega and ||L||=4M. The parent's actual reduced inverse, second-order response, mixed correction and full residual are imported, not replaced by products of per-cell evolutions.

For a supplied bound h0>=||H|| define

    v=4 sum_i t_i, a=h0+s0, b=h0+ell,
    F1=4v+T[2v(a+b)+4v^3],
    F2=8v^2+4T v^2(a+b).                             (9)

The accepted theorem gives the phase-sensitive prepared-map estimate

    sup_(0<=t<=T) ||exp(-it K_Delta)J-J exp(-it(H+sum_i lambda_i P_i))||
          <= E_M=F1/sqrt(Delta)+F2/Delta.             (10)

For each finite M, a sufficient choice for E_M<=e is Delta>=max{Delta_*,(2F1/e)^2,2F2/e}, with any supplied reference energy Delta_*>0. Both sides use the same physical t; no M-fold sequential runtime, attenuation or rescaling of H is introduced. Arbitrary passive references preserve the operator bound; the complete joint trace-norm output bound is min(2,2E_M). It includes the returned bare auxiliaries and all old dirty factors. Supplied terminal instruments contract the sum of unnormalized block errors; normalized rare postselection needs an additional probability bound. No reader is constructed here.

The original H keeps all its actual supports. Only the added terms are certified one-/two-site nearest-neighbor. If H itself has one-/two-site ordinary-neighbor supports, then so does the full generator(8), but that extra premise says nothing about preparation or readout. A concrete noncommuting-background example is H_M=h_* sum_(j=0)^M Y_(d_j), with h_*>0 fixed and identity action on other original factors. It is onsite, remains active unchanged, has ||H_M||=h_*(M+1)<=2h_*M, and does not commute with the target chain. This example is optional, not a restriction hidden in(10).

## 5. Shared-site and full-space resource prices

Use the parent's literal15M-occurrence decomposition, including the scalar(2Delta+s_i)I assigned to a_i. No cancellation removes H or the installed scalar. Let ell_H(u) be the actual sum of original H-term norms incident at an original site u, when a local decomposition is supplied. The added role loads are

| Site | Added whole-term norm load |
|---|---:|
| d_0 | 2 sqrt(Delta)t_0 |
| d_M | 2 sqrt(Delta)t_(M-1) |
| d_i,1<=i<M | 2 sqrt(Delta)(t_(i-1)+t_i) |
| p_i | Delta/4 |
| a_i | (11/4)Delta+sqrt(Delta)t_i+s_i |
| a'_i | (3/4)Delta+sqrt(Delta)t_i |
| b_i,b'_i | (7/8)Delta+sqrt(Delta)t_i each |

Add ell_H(u) on original sites. The reuse of an earlier spare as a'_i creates no earlier-cell load there: the earlier cell is identity on that unused vertex. Auxiliary sets are otherwise disjoint. These are sums of whole-term norms with the declared scalar assignment; they are not operator norms of a whole incident sum. Selected spatial degree and energy load are distinct quantities.

A valid global full-space norm bound is

    B_M=h0+s0+4M Delta+sqrt(Delta)v.                  (11)

The exact added Pauli scalar is2M Delta+s0; the full scalar is a_H+2M Delta+s0. If a nonnegative full generator is required, the parent's sufficient reserve R=h0+sqrt(Delta)v can be assigned to a_0. Its full value is then added to that site's load, the scalar and initial mean. The reference generator also gets R I, so the phase exp(-itR) is retained at the same time. Use B_M+R for timing and energy-error bounds. No fixed common cap or physical-energy identification follows.

For any actual old-data/reference state rho with bare Omega,

    mean(K_Delta)=Tr rho H+s0,
    Var(K_Delta)=Var_rho(H)+(209/16)Delta ell.         (12)

All H correlations remain. The large full scalar is not the initial vacuum mean. The reserve shifts mean but not variance. Auxiliary return error gives only nonvacuum probability<=E_M^2 and the coarse energy bound<Delta L><=4M Delta E_M^2; it supplies no energy reimbursement, reset or reusable catalyst.

## 6. Explicit M-dependent sufficient design

Equations(9)–(11) are the general certificate for arbitrary supplied finite h0(M) and coefficients. To display one transparent length scaling, suppose |lambda_i|<=Lambda with a supplied fixed Lambda>0 and h0(M)<=hM for a supplied h>=0. For a genuinely noncommuting weighted chain choose, for example, every lambda_i=Lambda>0. Fix T,e>0 and all these bounds independently of M. Set

    tau=sqrt(209 Lambda/64), nu=4tau,
    A=h+(29/2)Lambda, D=2h+(31/2)Lambda,
    C1=4nu+2T nu D+4T nu^3,
    C2=8nu^2+4T nu^2 D,
    D0=max{Delta_*,(2C1/e)^2,2C2/e},
    Delta_M=D0 M^6.                                  (13)

For M>=1, v<=nu M, a+b<=D M, hence

    F1<=4nu M+2T nu D M^2+4T nu^3 M^3<=C1 M^3,
    F2<=8nu^2 M^2+4T nu^2 D M^3<=C2 M^3.

Substituting(13) gives E_M<=C1/sqrt(D0)+C2/(D0 M^3)<=e. Certified upper constants may replace the displayed real values. This is a separate finite design for each M with explicitly growing strength, not a volume-independent accuracy claim at fixed Delta or a uniform-cap simulation. The hM premise is an additional norm bound, not inferred merely from the coordinates or arbitrary H. No optimal exponent or necessary lower bound is claimed.

The physical port strengths obey sqrt(Delta_M)t_i<=tau sqrt(D0)M^3. The largest internal-connector drive load is4tau sqrt(D0)M^3; the branch originals carry D0 M^6/4. The a_i load is at most(11/4)D0 M^6+tau sqrt(D0)M^3+(29/2)Lambda, and the other auxiliary loads follow the table. Thus this sufficient prescription has order M^6 local penalty loads, even though the physical box grows only linearly.

The full norm/scalar prices are bounded by

    B_M<=A M+nu sqrt(D0)M^4+4D0 M^7,
    R<=hM+nu sqrt(D0)M^4.                             (14)

The exact bare mean has absolute bound A M, and

    Var(K_Delta_M)<=h^2 M^2+(209/16)D0 Lambda M^7.     (15)

An optional separated low-energy band can be obtained by enlarging D0 to also dominate256nu^2 and16A. Then the parent's sufficient conditions Delta>=256v^2,16a hold for every selected finite M; the separation is at least Delta/4. That optional statement is not used by(10) and does not make the input a dressed state or a unique ground state.

## 7. Effective specification, calibration and supplied resources

The coordinates require only a four-entry integer table and O(M) emitted roles/edges, with coordinate bit length O(log(M+1)). That is a geometry specification, not a physical state-preparation or control-synthesis algorithm. For effective energetic coefficients the parent requires computable lambda_i and certified finite bounds/tolerances; its continuous signed square root avoids an exact zero/sign oracle. A fixed positive rational Lambda in the example supplies a particularly simple valid instance. H remains supplied with its actual representation and norm bound.

All15M declared new coefficients multiply unit-norm Pauli/identity operators. Uniform absolute errors<=xi give a total perturbation norm<=15M xi when H is exact. For a requested static perturbation allowance zeta, xi<=zeta/(15M) is sufficient. Summing actual absolute coefficients yields the useful alternative bound

    S_coeff=(19/4)M Delta+s0+sqrt(Delta)v.             (16)

Indeed one cell contributes its2Delta+s_i scalar, four Delta/2 onsite terms, two Delta/8 BZ terms, four Delta/8 exchange terms, and four sqrt(Delta)t_i ports. A relative coefficient budget eta<=zeta/S_coeff is sufficient when meaningful; under(13) this is conservatively of order M^-7. Unknown tiny coefficients use absolute budgets. Such arbitrary coefficient perturbations do not by themselves preserve a positive structured penalty; the comparison uses their full norm. If positivity is required, charge an extra reserve zeta as in the parent. Any reserve's own calibration error, any change of H and any unlisted auxiliary coupling require separate allowances.

More generally let f=integral_0^T ||E_actual(t)||dt over the actual whole interval. Add f to the operator error in(10). A supplied joint preparation trace error epsilon_p, timing error allowance epsilon_time and reader error epsilon_read yield

    epsilon_out<=min{2,epsilon_p+2(E_M+f)+epsilon_time+epsilon_read}. (17)

For a terminal time offset delta t, a sufficient trace allowance is2(B_M+R+sup||E_actual||)|delta t|, with R omitted if not installed. Under(13) a fixed timing-error allocation can therefore demand order M^-7 absolute timing accuracy. There is no extra M multiplier in nominal elapsed T, but the apparatus needs all simultaneous coefficients, clean resources and calibration throughout that unchanged T.

Mean/variance sensitivity to joint preparation trace error is bounded by B epsilon_p and3B^2 epsilon_p, where B is the full installed nominal norm including any reserve. Under(14), fixed absolute moment tolerances can require sufficient preparation errors of order M^-7 and M^-14. Local fidelities do not automatically supply the joint error certificate. Neither this note nor the geometry control supplies clean qubits, a clock/stop mechanism, physical measurement, reset, native addressability or uniformly bounded available strength.

## 8. Route limits and one selected check

A monotone d_i=(i,i,i) chain is an immediate collision-free corner-sharing alternative, but its naive enclosing box grows cubically. It does not meet the stronger strip-size target achieved here. Simply reflecting both transverse directions each step in an attempted width-two tube makes consecutive cubes share a face; the seven-used-vertex cells then conflict with reserved auxiliaries. That route failure is not a packing no-go. The present four-step path flips only one transverse direction at a time and changes the canonical y-axis to the flipping direction, making the shared nonconnector vertex the earlier unused vertex.

The selected presealed M=9 integer program will emit the complete coordinate/edge data, pairwise cube and occupied intersections, vertex degrees and Pauli-support commutation signs. It will reject the incompatible contract that treats all spares as old original spectators, by the8 actual clashes with later a' sites. This is one finite combinatorial check, not a proof for every M or a numerical channel/spectral calculation. The all-M argument is sections1–3, and the dynamical conclusion is the stated conditional import with all its hypotheses verified.

Actual execution, full streams, failures and the program/plan/proof seal are recorded separately. No conclusion relies on a PASS label or hash. The completed family remains a chosen finite vacant-site geometry with supplied original H and controls; it does not place an arbitrary preexisting hypergraph, solve occupied-L4 packing, provide native hardware, or remove the M-dependent global accuracy/energy costs. No canonical, Git, network, operational checkpoint, prompt or physical axiom is changed.

---

The three complete bodies above retain their original hypotheses and historical wording. Current source status, exact extraction, separate evidence and physical limitations are recorded in the opening framing and accompanying source manifest.
