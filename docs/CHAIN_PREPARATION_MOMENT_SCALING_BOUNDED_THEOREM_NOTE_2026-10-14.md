---
title: Sufficient preparation-moment budgets for a restricted noncommuting chain
claim_id: chain_preparation_moment_scaling_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: same-K scalar moment sensitivity with supplied full old/reference marginal and local auxiliary bounds; block diagonality separately supplied
hypothetical_axiom_status: null
admitted_observation_status: null
status: proposed_retained
canonical_parent_binding_complete: true
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies: ["multi_port_preparation_energy_moments_bounded_theorem_note_2026-10-14"]
runner: scripts/chain_preparation_moment_scaling_identity_2026_10_14.py
claim_type_reason: accepted conditional source composition; sufficient costs only, no native preparation or physical-energy identification
next_trace_action: root-owned integration verification and any later independent audit
---

Claim type: bounded_theorem

# Sufficient preparation-moment budgets for a restricted noncommuting chain

**Conditional support; the mathematical sources and source components have separate recorded acceptances.**

How accurately must the old system and the clean auxiliary qubits be prepared if a longer mediator chain is to keep a fixed tolerance on its initial mean and variance? The corollary below supplies sufficient budgets for normalized preparations of the same installed Hamiltonian. It requires a supplied certificate for the complete old-system/reference marginal, and its auxiliary data are actual local excitation probabilities. This full marginal error epsilon is distinct from the additional epsilon_R cost for reference-valued records. It does not assume independent cell errors. In the root corollary, nu bounds one auxiliary excitation probability and eta<=4M nu bounds their sum. The separately supplied [sigma,P]=0 condition removes P-Q cross terms while retaining Q-Q coherences. The centered second reference-valued record still pays Delta*kappa*epsilon_R, with the chain upper bound D*k*M^7*epsilon_R; scalar moment tolerances do not remove that term.

The concrete application is the already accepted restricted chain in an ordinary open cubic box of size `9(M+1)`: `2M+1` required original sites, `4M` distinct fresh auxiliaries, `6M+1` port-active sites and `8M` selected nearest-neighbor edges. Original sites are fixed before choosing H. Consecutive three-Pauli targets anticommute; M=1 has only one target. Unselected contacts must be absent or charged. Only the added terms are certified nearest-neighbor unless H itself has that property. The complete unchanged placement and cost proof is preserved as [79d source](../.claude/science/physics-loops/toe-chain-preparation-scaling-20261014/source/archive/objects/79d2388a7f6e2ce36d8b1055bd2ad80149a9e5375ff7f23248391d72bf5692ff.gz), not presented here as a new placement theorem.

With fixed bounds `|lambda_i|<=Lambda` and `||H||<=h M`, that application chooses a separate finite apparatus for each M with `Delta=D M^6`, where D meets the full sufficient dynamical prescription in its section 6. The nominal physical time remains T; H is an identical summand. Local penalty loads can grow as M^6, port strengths as M^3 and the full-space norm bound as M^7. The source also charges coefficient calibration, the optional positivity reserve, timing, jointly clean auxiliaries and supplied terminal operations. The scaling result below changes none of those prices. It bounds preparation sensitivity, not the growing baseline spread of the installed Hamiltonian or a whole output channel.

The sole imported canonical theorem source is the [preparation-moment theorem and restricted-chain prerequisite](MULTI_PORT_PREPARATION_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-14.md). Its complete de7 and 79d clauses match the frozen premises exactly. The be8 simultaneous operator result is transitive; no additional theorem edge follows from branch ancestry. Parent PR 9575 was observed regular OPEN at 2026-10-14T22:24:45.407505+00:00 at head `84d28d386cf8d8dbbdd4506387ad18296161fe53`. The clean child `physics-loop/toe-chain-preparation-scaling-20261014` was observed at that head at 2026-10-14T22:24:45.843690+00:00. These are dated observations, not claims about future PR state. The [binding record](../.claude/science/physics-loops/toe-chain-preparation-scaling-20261014/ACTUAL_BINDING.json) preserves the exact receipts and complete parent-body extractions.

The following sections preserve, byte for byte, the accepted root corollary e943, the independently composed pre-candidate derivation e734 and the explicit-constant section of the later comparison 2ace. Their original status and exposure paragraphs are historical. Current scientific disposition is recorded by [acceptance 3787850c](../.claude/science/physics-loops/toe-chain-preparation-scaling-20261014/source/archive/objects/3787850cc78f5653bf5ed918e2ab7072b0cfaa4a8ff044d3e4cf09152ba91259.gz) and [root review 8682e1b7](../.claude/science/physics-loops/toe-chain-preparation-scaling-20261014/source/archive/objects/8682e1b71d250dfb7b0d41e99f4bbfdf5d7d93610e31fa33fd0732f9a7fdfa87.gz). Notation is local to each preserved source: in particular, the independent derivation's coefficient bound `nu` differs from the root corollary's per-auxiliary defect `nu`.

These results concern scalar moments with arbitrary passive references. The separate reference-valued record terms, full old/reference marginal condition, same installed scalar/reserve, baseline coupling variance and supplied vacuum-block diagonality remain explicit. No optimality, native preparation/readout/reset, physical-energy identification, probability-free normalized postselection, fixed-cap realization or retained-audit status follows.

## Complete accepted root corollary

# Sufficient local preparation budgets on the reserved chain

Proposed source, not yet accepted. Root composed the separately reviewed de7e7916 moment theorem with accepted chain79d section6. This extends only the supplied preparation-sensitivity certificate. Actual preparation, statistics, old/reference control, physical energy, baseline spread, scalar reserve, timing and reader/reset remain charged. No optimality or necessary-cost claim.

Take every integer M>=1 in the declared reserved-chain family, with 4M auxiliaries, |lambda_i|<=Lambda, ||H||<=h M, and the fixed installed Delta=D M^6, D>0. The chain's dynamical target assumptions and sufficient D remain unchanged. Compare normalized preparations sigma and J rho J* under this same K (including the same actual scalar), with full old/reference marginal error epsilon and each actual excitation probability<=nu. Then eta<=4M nu. This is statewise; uniform preparation claims require these data uniformly over the full input/reference family. All constant tolerances below are independent of M.

Set k=209Lambda/16, v0=4sqrt(209Lambda/64), l1=(9+sqrt(5))/8<3/2. The exact parent gives kappa<=kM, v<=v0M and d=2hM. From de7 equations12,17,18, define finite nonnegative constants

G=sqrt(D k(4h+3D/2)^2+2D^2 k^2),
Q0=6D^2+D max(k,v0^2)+4sqrt(6)Dh+2sqrt(6)D^(3/2)v0+4h v0sqrt(D),
K1=3D/2+2sqrt(D k),
A1=3D/2+sqrt(D)v0.

The two squared-column terms have powers M^19 and M^14, so gamma<=G M^(19/2). All terms in q have powers13, at most8,15/2,21/2,5, respectively; M>=1 gives q<=Q0 M^13. Also k1<=K1 M^6. These upper estimates use only upper coefficient bounds and no nonzero lower bound on kappa.

For arbitrary coherent sigma, the mean deviation obeys

Emean<=h M epsilon+6D M^7 nu+4sqrt(D k) M^4 sqrt(nu).

For eta<=1 the absolute variance deviation obeys

Evar<=4h^2 M^2 epsilon+2h^2 M^2 epsilon^2
      +4G M^10 sqrt(nu)+4(Q0+2K1^2) M^14 nu.

Consequently epsilon<=c_e M^-1 and nu<=c_n M^-8 suffice for any fixed positive mean tolerance when the M-independent positive constants c_e,c_n are chosen small enough. For fixed positive variance tolerance, epsilon<=c_e M^-2 and nu<=c_n M^-20 suffice; taking c_n<=1/4 ensures eta<=1. At M>=1 the residual powers are nonpositive. These are explicit sufficient bounds; the mean budget is unchanged from the generic block bound, while the coherent variance exponent improves from22 to20.

Separately suppose [sigma,P]=0 for the complete joint auxiliary vacuum projector. This does NOT require every local auxiliary to be dephased. It kills only the P-Q cross terms. Since PVP=0, |Tr sigma V|<=v p<=v eta, including possible Q-Q coherences. Thus Emean<=h M epsilon+A1 M^6 eta<=hM epsilon+4A1 M^7nu. The Q-Q term RQ remains; E2<=4h^2 M^2 epsilon+Q0 M^13eta. With eta<=1, Emean^2<=2h^2 M^2epsilon^2+2A1^2 M^12eta, hence

Evar<=4h^2 M^2epsilon+2h^2 M^2epsilon^2+4(Q0+2A1^2)M^14nu.

It follows that epsilon<=c_e M^-1, nu<=c_n M^-7 suffice for fixed mean tolerance under this extra block condition; epsilon<=c_e M^-2, nu<=c_n M^-14 suffice for fixed variance tolerance. Again c_n<=1/4 and sufficiently small constants suffice. Optional complete local dephasing is a supplied paid way of obtaining the block condition; its implementation error and duration are separate. Treating block diagonality as Tr sigma V=0 would be an unjustified shortcut; the Q-Q estimate above retains it.

For simultaneous mean and variance tolerances use the stricter variance budgets and choose constants for both. The original mean includes m+c and variance includes Var_rho H+Delta kappa. Their actual values can grow with M; these formulas bound preparation sensitivity only. The scalar cancels only in same-K scalar deviations. Reference-valued moment maps retain de7's epsilon_R terms (Delta kappa epsilon_R in the centered second moment and |mu0|epsilon_R in the uncentered first moment); the exponents above describe scalar mean and variance, not a new reference-valued or full-output certificate. No normalization of rare outcomes is licensed.

Root initially considered a possible coherent mean exponent7, but checking the surviving M^4sqrt(nu) term rejects it. Only the additional block condition permits exponent7 here. This failed provisional inference is retained; no source or claim was published from it. The general all-M argument is algebraic. No numerical suite or new scientific program was executed.


## Complete separately composed derivation and failure families

This body was sealed before exposure to the root scaling candidate. The authors share earlier source/model context; this is not blind or model-diverse evidence. The exact correlated and coherent counterexamples, all constant choices and the historical pre-seal units clarification are retained in the archive.

# Sufficient chain-length preparation budgets for fixed physical moment errors

**Proposed conditional composition, written before any root scaling-candidate exposure.** For the supplied reserved-strip family and the same physical Hamiltonian on each length M, sufficient per-auxiliary population budgets are of order M^-20 for arbitrary coherent preparation and M^-14 when the joint state is separately certified to commute with the vacuum projector. In both cases a full old/reference marginal trace-norm budget of order M^-2 suffices for fixed scalar mean and variance tolerances. Explicit constants and all subdominant terms are below. These are sufficient budgets, not optimality claims, preparation procedures, new source acceptance or retained-audit findings.

The arbitrary reference and old correlations are retained. “Scalar mean/variance with arbitrary references” is distinguished below from trace-norm estimates for reference-valued moment operators; the latter require the additional reference-marginal term from the moment source. No operator-valued variance is introduced.

## 1. Exact sources, prior exposure and conditional input

The complete moment argument is de7e79161faf1c35941285c9670e9cc421f798c51204da139575c36870ab9976,15982 bytes/199 lines, in `joint_preparation_moment_block_independent/DERIVATION.md`; its19-file freeze is35e22f87b1ec2a05c92ac2d9859f912d828a42ff0d08b224f6d6a2cb67dad56f. I just completed the source-exposed review6e570746c8d010bc4c81711d17ce8e4d05af1acbec4553ccaaa8ee485f0d1bdd and selected exact overlapping-port check; neither is rerun. Root reported reading that review and that acceptance was being written, but this note does not assume an unseen acceptance.

The chain argument is79d2388a7f6e2ce36d8b1055bd2ad80149a9e5375ff7f23248391d72bf5692ff,20897 bytes/218 lines, in `joint_multi_port_chain_placement/DERIVATION.md`. Its complete body was freshly read, with the length prescription in section6. I authored that chain and its multi-port parentbe8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc. This is independent of a new root scaling candidate, not blind or model-diverse work. No root proposed exponents or coordinate modifications were supplied. The directory `joint_preparation_moment_chain_scaling_candidate` has not been opened or searched.

Fix M>=1, the supplied chain coordinates and its4M fresh auxiliary qubits. Let |lambda_i|<=Lambda, with fixed Lambda>0, and let the unchanged original Hamiltonian obey ||H_M||<=h M for fixed h>=0. All original dirty/spectator factors and an arbitrary finite passive reference R may be correlated. The model retains the literal parent L_M,V_M and

    K_M=H_M+c_M I+Delta_M L_M+sqrt(Delta_M)V_M,
    c_M=s0(M)+r_M,  s0(M)=(29/2)sum_i|lambda_i|,
    Delta_M=D M^6,  D>0 fixed independently of M.                 (1)

D is the chain's supplied D0 from section6, or any larger certified constant. Thus it may be chosen to secure a fixed ideal prepared-map tolerance e over fixed physical time T. D is not the moment source's centered old operator D0; below that operator is written H_M-m_M I. Each preparation comparison keeps the same actual c_M, Delta_M and K_M. H is neither rescaled nor moved. A changed implementation requires separate calibration allowances.

For normalized actual sigma_M on old,auxiliary,R and intended rho_M on old,R define

    epsilon_M=||Tr_aux sigma_M-rho_M||_1,
    delta_(M,u)=Tr(sigma_M n_u),
    eta_M=sum_(u=1)^(4M) delta_(M,u),
    p_M=Tr(sigma_M Q_M)<=min(1,eta_M),
    P_M=J_M J_M*, Q_M=I-P_M.                                  (2)

These are supplied joint preparation facts. No independent-cell, product-state or classical-reference assumption is made. The optional block condition is the full joint equality `[sigma_M,P_M tensor I_R]=0`; local population bounds do not imply it.

## 2. Uniform coefficient bounds and complete powers

Set the following fixed positive/finite constants:

    k=(209/16)Lambda,
    nu=4sqrt(209 Lambda/64),         nu^2=4k,
    l=(9+sqrt(5))/8,
    a1=(3/2)D+2sqrt(D k),
    b1=(3/2)D+sqrt(D)nu,
    G=sqrt(D k(4h+D l)^2+2D^2 k^2),
    Qc=6D^2+D nu^2+4sqrt(6)D h
                       +2sqrt(6)D^(3/2)nu+4sqrt(D)h nu.       (3)

The moment source gives kappa_M=(209/16)sum|lambda_i|<=kM, v_M<=nu M, kappa2_M<=2kappa_M^2<=2k^2 M^2. Choose the centered old norm certificate d_M=2hM, which bounds ||H_M-Tr(rho_M H_M)I|| for every intended state. This avoids requiring the actual old mean to select the budgets.

Substitute these estimates into the source's gamma-squared expression(12), without dropping any nonnegative term:

    gamma_M^2
      <=16D k h^2 M^9
        +(8D^2 k h l+2D^2 k^2)M^14
        +D^3 k l^2 M^19
      <=G^2 M^19.                                             (4)

This retains both old-H cross terms and the two-flip contribution; a common commuting-data basis is not used. The source q in(17) satisfies the complete expansion

    q_M<=6D^2 M^13 +D nu^2 M^8
           +4sqrt(6)D h M^(15/2)
           +2sqrt(6)D^(3/2)nu M^(21/2)
           +4sqrt(D)h nu M^5
        <=Qc M^13.                                            (5)

For the source's k1,

    k1_M<=(3/2)D M^6+2sqrt(D k)M^(7/2)<=a1 M^6.                (6)

Equations(4)–(6) use M>=1 to dominate lower powers. They do not replace the actual kappa2 by an equality or impose a fixed global operator cap. They preserve all M-dependence of the quoted sufficient certificates.

## 3. Arbitrary coherent preparations

The mean bound(7) and variance bound(18) of the moment source imply, whenever eta_M<=1,

    |mu_sigma(K_M)-mu0_M|
      <=hM epsilon_M+(3/2)D M^6 eta_M
                           +2sqrt(D k)M^(7/2)sqrt(eta_M),     (7)
    |Var_sigma(K_M)-nu0_M|
      <=4h^2 M^2 epsilon_M+2h^2 M^2 epsilon_M^2
        +2G M^(19/2)sqrt(eta_M)
        +(Qc M^13+2a1^2 M^12)eta_M.                          (8)

Here mu0_M and nu0_M are the actual bare-state physical moments stated in section5. The term quadratic in the actual mean error has not been removed.

Choose fixed0<alpha<=1 and0<beta<=1, and require

    epsilon_M<=beta M^-2,
    eta_M<=alpha M^-19.                                       (9)

An entirely local sufficient certificate for the latter, with no independence assumption, is

    delta_(M,u)<=(alpha/4) M^-20  for every one of the4M auxiliaries. (10)

Summing the actual populations proves(9). Substitution checks all powers:

    mean error<=h beta M^-1+(3/2)D alpha M^-13
                                  +2sqrt(D k alpha)M^-6,
    variance error<=4h^2 beta+2h^2 beta^2 M^-2
                   +2G sqrt(alpha)+Qc alpha M^-6
                                      +2a1^2 alpha M^-7.     (11)

Thus no positive residual power of M was hidden. In particular the controlling coherent term is gamma_M sqrt(eta_M), not a diagonal population term.

For arbitrary desired fixed positive mean and variance tolerances m_tol,v_tol, one fully explicit prescription is

    beta=min{1, m_tol/[3(h+D)], v_tol/[18(h^2+D^2)]},
    alpha=min{1, 2m_tol/(9D),
                [m_tol/(6sqrt(D k))]^2,
                [v_tol/(6G)]^2,
                v_tol/[3(Qc+2a1^2)]}.                        (12)

All denominators are positive because Lambda,D>0. The mean's three uniform terms are each at most m_tol/3. Since beta<=1, its two old-marginal variance terms sum to at most6h^2 beta<=v_tol/3; the coherent term and remaining alpha term are each at most v_tol/3. Therefore(9)–(12) imply both requested tolerances for every finite M>=1 and every admissible sigma_M,rho_M,R. These are conservative sufficient constants, not necessary or optimized ones. Certified upper coefficient bounds and smaller positive rational budget constants may be used effectively.

## 4. Separately supplied vacuum-block-diagonal preparations

Now additionally assume `[sigma_M,P_M tensor I_R]=0`. This removes P-Q coherences, including the entire off-diagonal contribution2gamma sqrt(p(1-p)) to the second-moment bound. It does not make the auxiliary excitations independent, diagonal in number, or uncorrelated with old data/reference. The Q-Q part and its full-space bound remain unchanged.

Moreover PVP=0 and the off-diagonal state blocks vanish, so

    |Tr sigma_M V_M|=|Tr Q_M sigma_M Q_M V_M|
                       <=v_M p_M<=nu M eta_M.                (13)

This yields the sharper mean estimate `hM epsilon_M+b1 M^6 eta_M`. Keeping the actual-mean centering square and the source RQ bound gives

    variance error<=4h^2 M^2 epsilon_M+Qc M^13 eta_M
                       +(hM epsilon_M+b1 M^6 eta_M)^2.       (14)

No factorization of Q sigma Q was used. With

    epsilon_M<=beta M^-2,
    eta_M<=alpha_b M^-13,
    delta_(M,u)<=(alpha_b/4)M^-14 as a sufficient local certificate,
    0<alpha_b<=1,                                             (15)

the individual terms are bounded by

    mean error<=h beta M^-1+b1 alpha_b M^-7,
    variance error<=4h^2 beta+Qc alpha_b
                  +2h^2 beta^2 M^-2+2b1^2 alpha_b^2 M^-14
                <=6h^2 beta+(Qc+2b1^2)alpha_b.                (16)

Use beta from(12) and set

    alpha_b=min{1, 2m_tol/(3b1),
                       2v_tol/[3(Qc+2b1^2)]}.               (17)

The old-marginal portions are at most one third of the respective tolerances, and the alpha_b portions at most two thirds. This proves uniform-in-length scalar moment tolerances under the additional block condition. The stronger local exponent improvement is conditional on that condition, not a conclusion of the population budgets themselves.

## 5. Baseline, reserve, references and fixed physical time

For the same generator the exact intended physical baseline remains

    mu0_M=Tr(rho_M H_M)+s0(M)+r_M,
    nu0_M=Var_rho_M(H_M)+Delta_M kappa_M.                     (18)

Consequently `|mu0_M|<=(h+29Lambda/2)M+|r_M|` and `nu0_M<=h^2 M^2+D k M^7`. The baseline is not made small by(12) or(17). The exact full Pauli scalar is `a_H+2D M^7+s0+r_M`, distinct from the bare initial mean. The optional positivity reserve remains the actually installed `r_M=h0(M)+sqrt(Delta_M)v_M`, bounded by `hM+sqrt(D)nu M^4`, with its full strength, scalar, phase and timing costs. It shifts mean and not variance. It cancels from the preparation difference only because both states use the identical installed scalar.

The marginal certificate in(9)/(15) is the full old/reference trace norm. This makes the scalar guarantees valid for arbitrary correlations and arbitrary finite reference dimensions, possibly growing with M. It does not turn them into estimates on reference-valued records. For the centered-second-moment operator in de7 equation(20), the additional term is `Delta_M kappa_M epsilon_(R,M)<=D k M^7 epsilon_(R,M)`. To allocate a separate fixed tolerance v_R>0 to it, require `epsilon_(R,M)<=v_R/(D k) M^-7`, or separately certify exact reference-marginal preservation. The uncentered-first-moment record additionally needs `|mu0_M| epsilon_(R,M)`; use the actual reserve/mean bound. The common M^-2 marginal budget alone does not control that record term uniformly. No operator-valued variance, normalized rare-block claim or unconditional observation theorem follows.

The chain's ideal prepared-map design still uses unchanged physical time T and the actual Delta_M in(1). No time slowdown or sequential composition is added here. These moment comparisons concern the same physical K_M on two preparations; its moments are individually conserved during the same closed static evolution, so those same comparisons remain true at every such time. This is not equality with the target Hamiltonian's energy distribution, nor a channel/readout/record guarantee inferred from small moments. Perturbed generators, extra operations, initialization, stopping, reader and reset require their separate supplied allowances. Large strengths and the chain's reserved-site/controlled-contact premises remain.

## 6. Failed shortcuts and explicit analytic discriminators

First, retaining only the global auxiliary failure probability and assuming independent cell defects would miss an allowed correlated state. Take H=0, any equal nonzero lambda_i=Lambda, and

    sigma=(1-p) rho tensor |Omega><Omega|
                         +p rho tensor |Full><Full|,

where Full occupies all4M auxiliaries. The old/reference marginal is exactly rho, sigma commutes with P, and every local defect is p. L has eigenvalues0 and4M on the two auxiliary words, V has zero expectation, and V^2 has diagonal expectation kappa on each. The exact variance excess is

    (4M Delta_M)^2 p(1-p)=16D^2 M^14 p(1-p).                 (19)

This preserves baseline Delta_M kappa and shows why the Qc M^13 eta term cannot simply be replaced by an independent-cell estimate under the stated information. In particular a slower-decaying local population budget alone need not keep the variance bounded. This is a specific correlated-preparation counterexample, not a general preparation no-go or an optimality claim for all stronger certificates.

Second, the block-diagonal budget cannot be exported to coherent states. Let H=0 and lambda_i=Lambda>0. For any pure old state psi put F=VJ, kappa=kM, chi=F psi/sqrt(kappa), and

    Psi=sqrt(1-eta)J psi+sqrt(eta)chi.                       (20)

F*F=kappa I makes this normalized; chi has total auxiliary number one. Its full old/reference marginal differs from the pure intended input by at most2eta, and each auxiliary defect is exactly eta/(4M). Since L>=N/2,

    <chi,L F psi>=<F psi,L F psi>/sqrt(kappa)>=sqrt(kappa)/2.

The centered-square vacuum-to-chi matrix element is `Delta_M^(3/2)<chi,L F psi>`; its two-excitation component is orthogonal to chi. Positivity of K0 squared gives the lower bound

    variance excess >=sqrt(1-eta)sqrt(eta)Delta_M^(3/2)sqrt(kappa)
                      -eta Delta_M kappa
                      -[(3/2)Delta_M eta
                                   +2sqrt(Delta_M kappa eta)]^2. (21)

At eta=a M^-13 with fixed0<a<=1, the first term grows as `D^(3/2)sqrt(k a) M^3 sqrt(1-aM^-13)`. The subtracted eta Delta kappa term is `a D k M^-6`; the last squared bracket is O(M^-6). The old marginal error is at most2aM^-13 and satisfies any fixed positive beta M^-2 for sufficiently large M. Thus the block-diagonal M^-14 per-qubit budget fails for this coherent family even while the full marginal budget is met. The coherent M^-20 sufficient budget retains exactly this missing square-root mechanism. No claim is made that its particular constants are optimal.

Finally, eta alone cannot bound a changed old H-distribution at perfect vacuum. The epsilon_M premise cannot be omitted. Neither an installed scalar cancellation nor the conservation of K_M moments creates a physical preparation or measurement apparatus.

## 7. Evidence and status

The displayed powers and constants are derived by substitution and operator inequalities above. No author code, old scientific suite, selected numerical sweep or new mathematical program was executed. Source identity/sealing uses deterministic bookkeeping only. The complete argument is sealed before any root scaling-candidate exposure. The earlier de7 and chain source bodies remain unchanged; copies and exact pins are preserved with an explicit exposure record. No canonical/Git/network/PR/checkpoint/physical-axiom/editable-prompt change, new agent or model/effort override occurred. Root assessment and independent acceptance of this proposed composition remain separate.


## Explicit constants from the accepted comparison

The following exact section is extracted from the [complete source-exposed comparison](../.claude/science/physics-loops/toe-chain-preparation-scaling-20261014/source/archive/objects/2ace6b191f80514c24dec8a46b2e113beddf9db1036f47e70163c1dad240c68c.gz). Its variables refer to the root corollary above. The full comparison also verifies the mean-only exponents and clarifies that the coherent counterexample has population `eta g_u^2/kappa` generally and exactly `eta/(4M)` under its explicitly equal couplings. Neither frozen proof required a repair.

## Explicit choices of the constants

For completeness the root's instruction to choose constants sufficiently small can be made literal. Let m_*>0 and v_*>0 be the requested scalar mean and variance tolerances. In the following minimums, a quotient with zero denominator is interpreted as +infinity; D>0 ensures the displayed choices are still finite and strictly positive.

For coherent mean alone choose

    c_e=min{1,m_*/(3h)},
    c_n=min{1/4,m_*/(18D),m_*^2/(144Dk)}.

For coherent simultaneous tolerances choose

    c_e=min{1,m_*/(3h),v_*/(18h^2)},
    c_n=min{1/4,m_*/(18D),m_*^2/(144Dk),
                         v_*^2/(144G^2),v_*/[12(Q0+2K1^2)]}.

Indeed the mean is at most h c_e+6D c_n+4sqrt(Dk c_n), with each part at most m_*/3. For the simultaneous row the variance is at most 6h^2c_e+4Gsqrt(c_n)+4(Q0+2K1^2)c_n, with each part at most v_*/3. We used c_e<=1 and M>=1, so all remaining powers are nonpositive. The same constants are allowed in the mean-only row.

For block-diagonal mean alone choose

    c_e=min{1,m_*/(2h)},
    c_n=min{1/4,m_*/(8A1)}.

For block-diagonal simultaneous tolerances choose

    c_e=min{1,m_*/(2h),v_*/(12h^2)},
    c_n=min{1/4,m_*/(8A1),v_*/[8(Q0+2A1^2)]}.

The two mean contributions are each at most m_*/2; the variance is bounded by 6h^2c_e+4(Q0+2A1^2)c_n<=v_*. In both variance classes c_n<=1/4 guarantees eta<=1 for every M>=1. These are sufficient choices, not necessary costs or optimized constants. They also cover Lambda=0 by the specified zero-denominator convention.



## Evidence, reproduction and remaining publication obligations

The [body map](../.claude/science/physics-loops/toe-chain-preparation-scaling-20261014/BODY_MAP.json) gives exact source intervals and their positions in this note. The preserved [source map](../.claude/science/physics-loops/toe-chain-preparation-scaling-20261014/source/SOURCE_MAP.json.gz) retains every original alias and maps identical byte strings to one archive object. The complete accepted 252-file sharper-moment assembly and 158-file restricted-chain assembly are preserved, along with the 11-file independent scaling argument, 14-file comparison, dispositions and actual outer source records. Historical failed attempts retain their actual streams or their explicitly recorded limits; no retrospective launch pin is invented.

No mathematical program was executed for the scaling composition or this packaging. The general result and failure families rest on the displayed arguments and their source-exposed reviews. The archived parent controls retain their original selected scopes. The new identity-only runner checks preservation, byte reconstruction and declared source closure; its success is not a theorem proof or audit verdict.

The mathematical sources were accepted under 3787850c and the complete unbound source components under a2d2310c at 2026-10-14T22:02:40.263776+00:00. This publication rendering was constructed at 2026-10-14T22:36:42.573511+00:00 from the dated parent/child evidence above. The original unbound note and all historical pending status text remain preserved byte for byte. Canonical integration, cache/graph checks, staging and publication have separate root-owned records. This note and its identity runner confer no retained audit status or apparatus supply.
