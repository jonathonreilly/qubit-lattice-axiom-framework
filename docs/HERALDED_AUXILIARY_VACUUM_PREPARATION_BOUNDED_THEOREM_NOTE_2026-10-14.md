---
title: Heralded auxiliary-vacuum preparation with one clean pointer
claim_id: heralded_auxiliary_vacuum_preparation_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied exact circuit, initial pointer, eligible factors, net control and complete readout; successful same-K scalar mean and variance with full old/reference bounds
hypothetical_axiom_status: null
admitted_observation_status: null
status: proposed_retained
canonical_parent_binding_complete: true
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies: ["multi_port_preparation_energy_moments_bounded_theorem_note_2026-10-14", "chain_preparation_moment_scaling_bounded_theorem_note_2026-10-14"]
runner: scripts/heralded_auxiliary_vacuum_preparation_2026_10_14.py
claim_type_reason: explicit finite conditional instrument and resource binding with checked circuit algebra and separate conditional moment proof; native apparatus remains supplied
next_trace_action: milestone source verification and independent retained audit before any retained promotion
---

Claim type: bounded_theorem

# Heralded auxiliary-vacuum preparation with one clean pointer

**Conditional theorem proposal.** A finite circuit can test the complete auxiliary vacuum while using only one initially clean pointer and one additional workspace qubit that may be in an arbitrary state. It preserves all within-failure-sector coherence under the supplied terminal binary instrument. On success, the auxiliaries are exactly in their specified product vacuum; correlations can still change the old system and its passive reference. The theorem below accounts for that conditional change, the complete failed outcome, the identical installed Hamiltonian and the apparatus premises.

This is a concrete application of existing controlled-projector and dirty-workspace machinery. The generic binary dilation and global-vacuum probability preparation certificate were already present in the repository. The new binding supplies the literal gate word, the restricted-chain physical layout and the successful energy-moment consequences together. The abstract projector identity, Barenco's gate synthesis and elementary conditioning inequalities are not claimed as new general mathematical machinery. The bounded prior-work survey is preserved with its exact coverage and nonexhaustive limits in the source packet.

The imported mathematical sources are the [preparation-moment theorem with its complete de7 and 79d clauses](MULTI_PORT_PREPARATION_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-14.md), and the [priced restricted-chain preparation scaling](CHAIN_PREPARATION_MOMENT_SCALING_BOUNDED_THEOREM_NOTE_2026-10-14.md). The former contains the full unchanged placement and same-K identities, not only a pointer to an unbound premise. The [binding record](../.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/BINDING.json) pins their exact current bytes, actual dated PR observations and complete parent-clause intervals. Branch ancestry alone is not a mathematical dependency.

## Result and resources

For every finite M>=1, let B be the 4M designated auxiliaries in the already supplied chain. The circuit realizes

    U=(I-P_B) tensor I_F + P_B tensor X_F,
    P_B=|0^(4M)><0^(4M)|,

with identity on all other factors, including arbitrarily entangled borrowed workspace and passive references. A supplied initial pure |0> pointer and terminal Born/Lueders Z instrument give the complete Kraus pair P and Q=I-P. Returning workspace as an operator identity does not mean that its conditional marginal cannot be steered by the outcome.

The concrete box is extended to `{-1,...,M} x {0,1,2} x {0,1,2}`, with `9(M+2)` sites. The new pointer is at(-1,0,0) and the arbitrary extra qubit at(-1,0,1). The installed K is extended by tensor identity on the new layer; this absence of new-layer background couplings is a supplied physical premise. Old coordinates and H terms remain fixed. All transits must be eligible for the scheduled gates: final return does not license changing an already permanent Record during the word.

The exact Toffoli count is10 at M=1 and8(4M-3) at M>=2. Each exact Toffoli is decomposed into five addressed two-qubit gates with its phases preserved. The 8M outer X gates and explicit monotone returned routes give the sufficient bound

    G_M <= 8M+5 T_(4M)(2M+9).

Actual emitted counts for M=1,2,3,8 are166,808,1680,7856 one-qubit or ordinary-neighbor two-qubit primitives. Under supplied net control generators bounded by J_c>0 *after drift removal*, pi G_M/J_c is a sufficient serial gate duration. The cancellation apparatus, clock, switching, physical energy/fuel, initial pointer and terminal readout/formation time are additional supplied resources. The preparation interval need not conserve K. All later moment comparisons use the same complete installed K and final physical coordinates.

## Success, correlations and scalar moment budgets

Let the actual full old/reference input marginal be within unhalved trace norm epsilon of rho, without any auxiliary independence assumption. Let q be the actual nonvacuum weight. For p=1-q>0, successful old/reference state tau obeys

    ||tau-rho||_1 <= e=min(2,epsilon+2q),
    q <= min(1,sum_u Tr(sigma n_u)).

The failed block remains Q sigma Q. Retesting that same failed state ideally cannot succeed without renewal. No repeated-attempt or free-reset conclusion follows from p.

Write the unchanged installed operator as `K=H+cI+Delta L+sqrt(Delta)V` and retain the parent coefficient kappa, excluding Delta. Successful scalar moments are exactly

    mean_+ K = Tr(H tau)+c,
    Var_+ K = Var_tau(H)+Delta kappa.

The actual baseline Delta*kappa and installed scalar/reserve remain charged. With W the spectral width of H, t=e/2, and f(t)=t(1-t) for t<=1/2 and f(t)=1/4 otherwise, the independently derived bounds are

    |mean_+-mean_0| <= W t,
    |Var_+-Var_0| <= W^2 f(t) <= 2 h0^2 e,

when ||H||<=h0. The root's original factor3 variance bound is a valid weaker result and remains preserved below. The sharper modulus is universal for the stated upper-distance information; it is not an optimal physical preparation cost.

On the restricted family Delta=D M^6 and ||H||<=hM, supplied old/reference epsilon of order M^-2 and per-auxiliary defect nu of order M^-3 suffice for fixed successful scalar mean/variance tolerances, with explicit constants. For positive tolerances A,B, choose

    C=min(1,A/h,B/(2h^2)),
    epsilon<=C/(2M^2), nu<=C/(16M^3),

interpreting zero-denominator quotients as infinity. Then p>=3/4, e<=C/M^2, mean error<=hC/M and variance error<=2h^2 C. This is a success-conditioned preparation claim under the additional instrument, not a replacement of the existing unconditioned M^-20/M^-14 results on their original hypotheses.

These scalar allowances do not certify physical raw second moments for an arbitrarily growing c. Their separate bound is `(e/2) osc((H+cI)^2)`. Conditional reference-valued centered second records also retain `Delta*kappa*||tau_R-rho_R||_1`; the initial reference can be correct and the selected reference still change. Every such term is displayed in the complete proof below.

## Imperfection and evidence limits

For a supplied full-reference discrepancy zeta between complete actual and ideal flagged outputs, including both branches, actual success remains positive when zeta<2p for the actual ideal probability. With a certified lower bound p_*>0 and zeta<2p_*, actual-versus-ideal normalized success error is at most `min(2,zeta/p_*)`. Pass frequencies or local fidelities do not prove this complete contract. General residual accepted auxiliary error restores the large full-space energy sensitivity; the conservative chain variance allocation remains of order M^-14 in this normalized instrument error. The theorem does not remove that apparatus-precision obligation.

The root emitted and checked concrete routes and finite permutation columns. A separate reviewer used independently written exact Gaussian-rational matrices to check Toffoli phases and generic returned routing, and subsequently checked every actual M=1,2 logical/decomposed entry. Another worker derived the conditional state/moment theorem before seeing the root candidate, then checked the composition. All selected model/source exposure, actual streams, wrong-interface controls and read limits are preserved. There was no independent full physical-word matrix check or numerical moment sweep. The all-M conclusions follow the displayed proofs, not a finite test count.

The canonical runner binds complete source identities and performs scoped exact circuit checks on the frozen words, using the preserved emitter and independent phase semantics. Its success is not a proof of every analytic inequality, native implementation or retained status. Whole proof bodies below are preserved byte for byte; their original provisional/exposure labels are historical. Current conditional acceptance is recorded in ROOT_ACCEPTANCE within the source index. The separate unfinished dyadic-filter investigation is excluded.

One clean pointer, a specified frame, eligible factors, identity background on the new layer, addressed net controls, drift removal, a clock and a complete terminal instrument remain supplied. Native dynamics, readable permanent framework Records, physical-energy identification, reset, renewable attempts, arbitrary occupied packing and a common strength cap remain unresolved. No physical axiom or editable prompt changes.

## Complete root construction

# Vacuum acceptance with one clean pointer and returned arbitrary workspace

Provisional root candidate, 2026-10-14. This is a conditional construction and proof proposal, not an accepted theorem, native implementation or retained audit. The original preparation-moment and chain-scaling publications are unchanged. A separate worker has been asked to derive the conditional-state/moment consequences from the source premises, without this candidate. A second worker is checking relevant prior work and physical obligations. Their new results have not been read in writing this draft. Earlier campaign context and the selected model are shared.

## 1. Exact question and supplied apparatus

Can a binary vacuum test replace very stringent initial auxiliary-defect budgets with explicit heralding, while preserving the full old-system/reference guarantee? The proposal separates an exact ideal instrument from the resources and errors of implementing it. It does not supply a native preparation law or a free measurement.

Let D be the old finite system, B contain n=4M auxiliary qubits, and R be an arbitrary passive reference. Put

    P_B = |0^n><0^n|,  P = I_DR tensor P_B,  Q=I-P.

The initial normalized sigma_DBR is arbitrary, including entanglement. The intended old/reference density is rho_DR, with a supplied certificate

    ||sigma_DR-rho_DR||_1 <= epsilon.

For each auxiliary u, an actual excitation bound Tr(sigma n_u)<=nu may be supplied. No independence is assumed. Define q=Tr(Q sigma), p=1-q. Then I-P_B<=sum_u n_u implies q<=min(1,n nu). These are actual-state premises, not costless measurements or an inference from single-site data about DR.

The apparatus additionally supplies one **unrecorded**, initially pure pointer F in |0>, one distinct eligible borrowed qubit C in an arbitrary state, and individually addressed one/two-qubit unitaries in a specified computational frame. C may be correlated or entangled with DBR. Routing may use other arbitrary unrecorded eligible factors. The full statement is an operator identity on these factors, so no cleanliness of C or routing factors is used. Eligibility for the scheduled operations is a premise; returning a factor at the end would not authorize violating an already permanent Record during the word.

Only F undergoes the terminal supplied Born/Lueders Z event. Both outcomes are retained. The circuit stops using F afterward, so its declared record is not erased or overwritten. The auxiliary qubits remain unrecorded and available for the later installed Hamiltonian. The readout/formation process, timing, chosen coframe, controls, drift removal or compensation, and pointer preparation remain supplied. The four current axioms alone supply none of these particular operations.

## 2. An explicit exact circuit without clean workspace

The standard dirty-workspace Toffoli constructions are existing machinery, not a discovery here; see Barenco et al., *Elementary gates for quantum computation*, arXiv:quant-ph/9503016, section 7.1, Lemmas 7.2–7.3. The primary source explicitly treats initial workspace values as arbitrary and restores them. The following word and proof make the particular all-zero acceptance operation self-contained. We count exact Toffoli gates, without importing relative-phase optimizations or an optimality claim. Source: https://arxiv.org/abs/quant-ph/9503016.

Write T(a,b;t) for the exact Toffoli permutation t -> t xor ab. For m controls x_1,...,x_m, target t and m-2 arbitrary distinct borrowed bits y_1,...,y_(m-2), define

    g_1 = T(x_1,x_2;y_1),
    g_j = T(x_(j+1),y_(j-1);y_j), 2<=j<=m-2,
    g_(m-1) = T(x_m,y_(m-2);t).

For m>=3, apply the following chronological word:

    A = g_1 ... g_(m-2) g_(m-1) g_(m-2) ... g_1,
    B = g_2 ... g_(m-2) g_(m-1) g_(m-2) ... g_2.

Empty ranges are omitted. Each word separately restores all y bits. A toggles t by a polynomial in the original y bits plus x_1...x_m. B toggles t by exactly the same y-dependent polynomial without that product, because only g_1 introduces x_1 x_2. Their composition therefore toggles t by x_1...x_m and changes no other bit. The gate count is (2m-3)+(2m-5)=4(m-2). This is an equality of exact phase-free permutations on every computational basis vector, hence an equality of unitaries on arbitrary superpositions and all passive references. For m=1 use CNOT; for m=2 use one exact Toffoli.

Now let n>=5, partition the n controls into S and T with

    a=|S|=ceil((n+1)/2), b=|T|=n-a.

Let c be the one extra borrowed qubit and f the pointer. Define A_0=C^S X_c and B_0=C^(T union {c}) X_f. Apply A_0, B_0, A_0, B_0 chronologically. If u=product(S), v=product(T) and the initial borrowed value is c_0, the two pointer toggles sum modulo two to

    (c_0 xor u) v xor c_0 v = uv.

The borrowed c is restored. Implement A_0 by the preceding ladder using a-2 spectators from T union {f}; implement B_0 using b-1 spectators from S. These sets have sufficient size because of the balanced choice of a. Each subword is an exact identity on its spectators, even when a spectator is a logical control or the pointer of a different subword. There is no phase residue or assumption that these spectators are classical.

Both control counts a and b+1 are at least three for n>=5. The total number of exact Toffolis is

    2[4(a-2)] + 2[4(b-1)] = 8(n-3).

For n=4, use |S|=2, |T|=2: A_0 is one Toffoli, B_0 has three controls and uses four Toffolis, so the same commutator construction uses ten Toffolis. In the present n=4M family these two cases suffice. Thus

    T_n=10 for n=4;  T_n=8(n-3) for n>=8.

Conjugate the n controls by X before and after this word. The exact resulting unitary is

    U = (I-P_B) tensor I_F + P_B tensor X_F,

tensored with the identity on D, C and all other spectators. It writes 1 exactly on the complete auxiliary vacuum. In particular it does not retain any fine-grained nonvacuum pattern in workspace or in several independently read bits. The failure outcome preserves coherences within Q under the ideal instrument.

An exact Toffoli admits a five two-qubit word. Choose the unitary V with V^2=X, for example V=(I+X)/2+i(I-X)/2. For controls a,b and target t, use chronological

    CV(b,t), CNOT(a,b), CV†(b,t), CNOT(a,b), CV(a,t).

For each a,b the exponent of V on t is b-(a xor b)+a=2ab. Controls return and V^2=X, proving the exact Toffoli identity with no global or relative phase ambiguity. All constituent controls remain supplied operations. Therefore the construction has 2n one-qubit X gates and 5T_n addressed two-qubit gates, one initially clean pointer, and one extra arbitrary borrowed qubit. It is not a claim of optimal gate count or minimal purity consumption.

## 3. Ordinary nearest-neighbor routing and resource boundary

Suppose all n+2 named factors lie in a supplied connected finite subset of the ordinary cubic lattice, and every addressed pair used above has a supplied simple path of length at most d. For a two-qubit operation between path endpoints v_0 and v_l, swap the factor at v_0 along v_0,...,v_(l-1), apply the operation to neighboring factors at v_(l-1),v_l with its correct operand order, and undo every swap in reverse order. This uses 2l-1 nearest-neighbor two-qubit primitives and acts as the desired endpoint operation tensor identity on every intermediate factor. The proof is conjugation by the actual swap permutation; it applies to arbitrary entanglement and not just product transit states.

The total serial primitive count is at most

    G = 2n + 5 T_n (2d-1).

For a connected rectangular open box d can be taken as its L1 diameter. A specified embedding with d=O(M) therefore has G=O(M^2); the exact geometry must be supplied and checked for an actual installation. A periodic seam is not an ordinary open-box edge. The circuit does not by itself provide an arbitrary occupied-site or already-recorded-site packing theorem.

If the scheduled one/two-qubit gate generators after drift removal have norm at most J_c>0, a logarithm with norm at most pi realizes each supplied unitary in a slot pi/J_c. Thus G pi/J_c is a sufficient serial gate duration. This does not price an arbitrary cancellation Hamiltonian, external clock, switching, the terminal record event, energy/fuel, or pointer supply. A scalar used to make a control Hamiltonian positive has its own physical energy cost. The installed K below is the same in both final-state comparisons; no assertion is made that the preparation controls commute with K or preserve its energy during the preparation interval.

## 4. Full instrument and conditional old/reference disturbance

From the initial |0>_F, the exact pointer Kraus operators on DB are P for outcome 1 and Q for outcome 0, tensored with identity on C and any passive reference. All-outcome completeness is P+Q=I. This is a supplied binary instrument, not a derivation of the Born or Record-formation law.

For p>0, the successful normalized state is

    sigma_+ = P sigma P / p = tau_DR tensor P_B,
    tau_DR = <0^n|sigma|0^n>/p.

The auxiliary is exactly vacuum in this ideal successful branch. Put omega_DR=Tr_B(Q sigma Q)/q when q>0. Cross terms have zero partial trace over B, so

    sigma_DR = p tau_DR + q omega_DR.

Consequently ||tau_DR-sigma_DR||_1<=2q, and

    ||tau_DR-rho_DR||_1 <= e := min(2,epsilon+2q).

The endpoint q=0 gives equality tau=sigma_DR; q=1 has no normalized success state and is excluded. The coefficient 2q is attained by orthogonal old states on the pass and failure branches. The same proof works with C and any routing factors added to R if a target/certificate on that enlarged reference is specified. Operator return of C does **not** mean its conditional marginal cannot be steered by postselection when it was correlated with B. Its unconditional marginal is unchanged by the complete local instrument.

The guarantee requires no repeated-attempt or independence assumption. In fact, reapplying this same ideal test after failure gives success probability zero, because that state lies in Q. Fresh attempts require an actual renewal mechanism and fresh record capacity. No expected finite retry time is claimed.

## 5. Same installed Hamiltonian: scalar and reference-valued moments

Use the complete de7 source at SHA256 de7e79161faf1c35941285c9670e9cc421f798c51204da139575c36870ab9976, now contained unchanged in the preparation-moment canonical note SHA256 9cfc7b475f26975e61de5c52d5c616098e0d5e34f86507a95cccffc9f47df21f. In its notation,

    K=H+cI+Delta L+sqrt(Delta)V,
    ||H||<=h0, L>=0, LJ=0, J*VJ=0, J*V^2J=kappa I,
    ||L||=4M, ||V||<=v, J appends the B vacuum.

Delta>0, c and every coefficient are the identical actually installed values in both comparisons. The old operator H, arbitrary passive reference and all resource premises are retained. No new parent theorem is inferred from branch ancestry.

For every old/reference density x,

    J*KJ=H+cI,
    J*K^2J=(H+cI)^2+Delta kappa I,
    mean_(JxJ*) K=Tr(H x_D)+c,
    Var_(JxJ*) K=Var_(x_D) H+Delta kappa.

The second identity follows by expanding KJ=(H+c)J+sqrt(Delta)VJ and using orthogonal vacuum/off-vacuum columns. Thus the ideal successful input retains the paid baseline variance Delta kappa. Comparing it with J rho J*, the preceding full-reference error e gives

    |mean_+ K-mean_0 K| <= h0 e,
    |Var_+ K-Var_0 K| <= 3 h0^2 e.

For the variance estimate, the H^2 expectation changes by at most h0^2 e, and the square of the H mean changes by at most 2h0^2 e. This is a sufficient bound, not a claim that the coefficient 3 is sharp. It is independent of c, Delta and kappa because their identical scalar/baseline contributions cancel in this particular scalar comparison. These physical baseline quantities have not been deleted from either actual distribution.

Reference-valued records retain a different cost. Let m0=Tr(H rho_D), H0=H-m0 I and d0>=||H0||. For epsilon_R^+=||tau_R-rho_R||_1, duality gives

    ||Tr_DB[(K-mean_0 K)(sigma_+-JrhoJ*)]||_1 <= d0 e,
    ||Tr_DB[(K-mean_0 K)^2(sigma_+-JrhoJ*)]||_1
        <= d0^2 e + Delta kappa epsilon_R^+.

Here the partial traces leave an R operator. The last term is generally nonzero: selection can steer R. The uncentered first record can instead be bounded by (h0+|c|)e. Scalar variance cancellation is not equality of arbitrary reference-valued records.

## 6. Chain consequence and a saturating disturbance family

On the already accepted restricted chain, keep Delta=D M^6, ||H||<=h M and n=4M. Its growing strength, calibration and geometry costs are unchanged. The ideal instrument gives p>=1-4Mnu and

    mean error <= hM(epsilon+8Mnu),
    variance error <= 3h^2 M^2(epsilon+8Mnu).

Hence epsilon<=c_e M^-2 and nu<=c_n M^-3, with c_n<1/4 and sufficiently small explicit c_e+8c_n, are sufficient for uniform simultaneous scalar tolerances. For prescribed positive mean tolerance A and variance tolerance B and h>0, it suffices to choose

    c_e+8c_n <= min(A/h, B/(3h^2)),  c_n<1/4.

The mean bound actually decays as M^-1 under this choice. When h=0 these scalar moment differences vanish for the exact vacuum instrument. Mean-only control needs only epsilon=O(M^-1), nu=O(M^-2). No bare O-symbol waives the constants or the positive success requirement. This replaces the *initial bulk-defect requirement for the successful ideal-instrument branch*, not the precision/resource requirements of the whole apparatus.

The loss q<=4Mnu and the old/reference disturbance can both be attained. Let u run over the n one-excitation words, and choose orthogonal old states alpha,beta. Set

    sigma=(1-q)|alpha><alpha| tensor P_B
          +(q/n) sum_u |beta><beta| tensor |u><u|,
    rho_D=(1-q)|alpha><alpha|+q|beta><beta|.

Then epsilon=0, each auxiliary defect is q/n, and the conditional old-state error is exactly 2q. If H has eigenvalues +hM and -hM on alpha and beta, the scalar variance changes by exactly 4h^2 M^2 q(1-q) in magnitude, while the same Delta kappa remains in both variances. Such an old H can be a sum of M bounded single-site Z terms on the available old sites. This witnesses the stated disturbance mechanism, not a universal optimality or no-go result for other preparations/instruments.

For full reference-valued second-record control, the Delta kappa term has the already charged chain upper bound D k M^7 epsilon_R^+. Merely choosing scalar epsilon=O(M^-2) is insufficient to suppress it uniformly. One sufficient stronger choice is e=O(M^-7), for example epsilon=O(M^-7), nu=O(M^-8), with the corresponding constants. No reference-decoupling assumption is inserted.

## 7. A precise imperfect-instrument allowance and its substantial cost

Let the ideal complete flagged output for the actual input be X_+ direct-sum X_-, and the actual output be Y_+ direct-sum Y_-, including the same quantum output factors and full passive reference. Both have total trace one. Suppose the **full** trace-norm contract

    ||Y_+-X_+||_1 + ||Y_--X_-||_1 <= zeta

has actually been justified. Let p=Tr X_+, s=Tr Y_+. Then |s-p|<=zeta/2. If p>zeta/2, actual success is positive. Put a=||Y_+-X_+||_1 and b=||Y_--X_-||_1. Because |s-p|<=b,

    ||Y_+/s-X_+/p||_1
       <= (a+|s-p|)/s and <= (a+|s-p|)/p
       <= zeta/max(p,s) <= zeta/p.

The bound is capped at 2. This uses both branches; a pass-block-only error certificate would not justify the same constant. If p has only the certified lower bound p_*=1-4Mnu>0, require zeta<2p_* and use e_inst=min(2,zeta/p_*). An outcome probability alone is not a full instrument certificate.

For coherent scheduled unitary errors delta_j in operator norm, a joint pointer-initialization trace error e_F, and an independently justified full-reference terminal-instrument allowance e_read, telescoping and contractivity give the sufficient zeta<=e_F+2 sum_j delta_j+e_read. This requires the stated joint preparation and operator/instrument contracts; arbitrary memory-bearing dissipative noise is not automatically covered by a list of local gate fidelities.

Let ell_K=h0+4MDelta+sqrt(Delta)v bound ||K-cI||. The actual successful output may have residual auxiliary excitations. The generic bounded-observable and variance inequalities therefore give

    actual mean error <= h0 e + ell_K e_inst,
    actual scalar variance error <= 3h0^2 e + 3 ell_K^2 e_inst.

Thus a completely general residual instrument error on this chain still needs e_inst=O(M^-14) for uniform scalar variance through this sufficient estimate. The proposed instrument does not eliminate a demanding precision problem; it moves the bulk preparation requirement to an explicit measurement/control contract. Restricted physical error models might improve that contract, but none is assumed here.

The full-norm cost is not merely cosmetic. Mixing a small false-accepted weight into a fully excited auxiliary branch can contribute a variance term of order (4MDelta)^2 times that weight. Its physical possibility and rate must be handled by the actual instrument model. This is a concrete error family, not a no-go for fault-tolerant or better structured implementations.

## 8. What remains to be checked and what is not concluded

The new load-bearing items are the exact emitted dirty-workspace word and routing contract, the conditional full-reference disturbance/moment composition, and the imperfect full-instrument normalization bound. The root will select focused exact controls for these, preserving all actual sources, failures and streams. A separate analytic derivation and prior-work review are pending. Source-identity checks on the already published notes do not validate this new proposal.

The construction is conditional on one clean unrecorded pointer, eligible workspace, addressed controls with a chosen frame, drift/timing/switching and a complete terminal instrument. It supplies neither a law selecting the full old/reference state nor native dynamics, physical energy identification, an apparatus energy/fuel ledger, a record formation law, an arbitrary recorded-site compiler, reset or a renewable stream of attempts. The entire installed Hamiltonian, scalar and baseline variance remain charged. No physical axiom or editable prompt is changed.

## Complete concrete chain layout

# Concrete ordinary-neighbor binding for the restricted chain

Root provisional addition after the frozen derivation 88f60f60, 2026-10-14.
This supplies a particular layout to section 3; it does not change that draft.
The prior-work survey f3770960 was read before this addition. No output from
the new independent conditional-state derivation or circuit check was read.

Use the complete 79d2388a chain placement with its original coordinates fixed.
Its original box is B_M={0,...,M} x {0,1,2} x {0,1,2}. Reserve the same four
auxiliaries per cell; their candidate input can now be arbitrary as specified
in the new test. Extend the supplied box by one transverse layer:

    E_M={-1,0,...,M} x {0,1,2} x {0,1,2}.
    F=(-1,0,0), C=(-1,0,1).

F is the one newly supplied pure |0> pointer. C and the other seven new sites
may be arbitrary and correlated with the original system/reference. All old
and new transit factors must be eligible for the scheduled gates; this is not
a compiler that can modify already permanent Records. No existing original
site or Hamiltonian term is moved. Extend the installed K by identity on the
nine new factors. That identity extension is a declared apparatus-background
premise, not a consequence of merely adding lattice sites.

The exact inventory is 9(M+2) physical sites, 4M candidate auxiliaries, one
clean pointer, and 5M+17 other factors. The last count includes the one
arbitrary borrowed C, the 2M+1 required original data factors and the remaining
transits/spectators; these categories are not additional disjoint inventory.
In particular, the 5M+17 factors need not start in product states or have zero
physical energy. The actual original H can act on old spectators as in 79d;
its extension acts as identity on the newly supplied layer.

For each addressed pair, route first along x, then y, then z, monotonically
between the endpoints. This path is simple, lies in E_M, and has length their
L1 distance, at most

    d_M=(M+1)+2+2=M+5.

Each endpoint operation is conjugated by the forward swap path excluding the
last edge, followed by its exact inverse. Every intermediate factor is
returned as an operator identity, not only on classical inputs. Even old data
may be such a transit under the supplied control/drift contract; intermediate
displacement is not free evolution under the unchanged background. The same
K comparisons refer to the final physical coordinates after the complete word.

Let n=4M, T_4=10, and T_n=8(n-3) when M>=2. The emitted exact word has 2n
one-qubit gates and 5T_n addressed two-qubit gates before routing. Thus a
sufficient serial primitive count and duration are

    G_M <= 8M+5T_(4M)(2M+9),
    t_gates <= pi G_M/J_c,

under the original supplied net control norm J_c>0 and drift removal. The
gate count is a bound, not the actual sum of lengths for a selected M; the
emitter records both. No unbounded-control optimization, physical cancellation
cost, readout duration, fresh attempt, clock reset or purity supply is removed.

The all-M coordinate/disjointness proof is the unchanged 79d construction,
plus the disjoint new x=-1 layer. The all-M path assertion follows directly
from coordinate monotonicity. Finite emitted examples and routing controls
will check implementation of these proofs, not establish the quantified
claims by extrapolation. The matrix identity of each exact Toffoli and the
all-input dirty-workspace word are separately checked. Neither source hashes
nor geometric edge counts alone establish the full quantum instrument.

This conditional resource binding is the proposed new contribution. The
abstract complementary-projector dilation and global-probability preparation
certificate are existing repository results; Barenco's dirty-workspace
construction is standard external machinery. The supplied ideal instrument
still has to be distinguished from a physical readable/permanent Record.

## Complete independent conditional-state and moment derivation

# A conditional vacuum-outcome certificate for preparation moments

**Proposed independent derivation, sealed before new root-candidate exposure.** A supplied ideal binary vacuum instrument gives an exact vacuum state on its successful branch, with a sharp universal old/reference disturbance bound controlled by its failure weight. Its successful scalar energy-moment sensitivity is then governed by the original H rather than the large auxiliary penalty. Success must have positive probability; failure is retained; conditional reference marginals can change. This argument supplies no instrument, native probability/readout law, reset, physical-energy identification or retained status.

## 1. Exact premises, source roles and exposure

The complete mathematical application sources read for this task are:

- `sources/sharper_moment.md`: original `joint_preparation_moment_block_independent/DERIVATION.md`, SHA256 `de7e79161faf1c35941285c9670e9cc421f798c51204da139575c36870ab9976`,15982 bytes/199 lines. Its exact vacuum identities and same-installed-K ledger are imported; its quantitative preparation inequalities are not assumed to prove the conditioning estimate below.
- `sources/chain_scaling_canonical.md`: current `docs/CHAIN_PREPARATION_MOMENT_SCALING_BOUNDED_THEOREM_NOTE_2026-10-14.md`, SHA256 `883e0c0ad7d31fc039de0d895fb586818c2562150acef528fb4c79c784f9441b`. Its restricted family, complete underlying proof composition and charged strength/time/baseline scope are retained. Section7 below is a new conditional application with an additional supplied binary instrument; it is not a correction to that note's unconditioned preparation bounds.

`SOURCE_RECEIPT.json` pins both complete copies and their actual capture. The first combined tool display truncated the chain note; both complete line ranges1–180 and181–360 were then read, covering its entire body. This is not a claim that a truncated display supplied complete coverage. Current selected procedural main92574ffe and instruction3a4b2c66 coverage is reused where unchanged; the physics-loop discovery/premise discipline is applied to this bounded source-only assignment. There is no fresh global prior-art or novelty claim, no autonomous campaign pivot and no PR or audit action.

The author previously derived sharper de7, reviewed same-family mediator and moment arguments, and assembled the accepted preparation sources. Root supplied this task's exact state/instrument target and the two sources, but no new root formula or candidate body. No future root candidate directory was opened, searched or requested. This is independent of that candidate, with prior shared-model/source exposure, not blind or model-diverse evidence. The elementary mixture, spectral and normalization arguments below are proved here. No external result is adopted merely by name.

Let A be all original factors, including dirty factors, B the n=4M auxiliary qubits, and R an arbitrary passive reference. All statements allow arbitrary correlations in the normalized positive trace-class state sigma_ABR. Let rho_AR be normalized and

    tau=Tr_B sigma,       ||tau-rho||_1 <= epsilon.             (1)

The source supplies the operator identities on finite AB and arbitrary finite R. The proof below extends to an infinite reference as well: all AB observables are bounded, and finite-rank reference compressions on the common separable support of the two trace-class states converge in trace norm after normalization. Outcome weights and moments converge; normalized successful branches converge whenever s>0. This argument licenses no division at s=0. Equivalently, the mixture and trace-duality steps below work directly for trace-class operators.

The trace norm is unhalved throughout. Let Omega=|0...0>_B, let J append Omega, and put P=JJ*, Q=I-P, with identities on A,R understood. The supplied ideal instrument is the complete channel

    I(sigma)=|PASS><PASS|_F tensor P sigma P
              +|FAIL><FAIL|_F tensor Q sigma Q.               (2)

Equation(2), including its classical flag semantics, is a supplied formal instrument contract. Its branch traces are probabilities within that supplied model; no native Born/readout mechanism is derived. In particular, the failure branch preserves its Q-sector coherence. Measuring all auxiliary bits and forgetting their values need not implement(2).

For the energy application the *identical installed* finite generator on AB is

    K=H+c I+Delta L+sqrt(Delta)V,   Delta>0,
    c=s0+r_installed,
    LJ=0, J*VJ=0, J*V^2J=kappa I,
    kappa=(209/16)sum_i |lambda_i|.                            (3)

Here H is the original unchanged Hermitian operator on A. K acts trivially on R. The scalar c and any actual reserve are the same in every comparison. K is not retuned after seeing an outcome. Kappa here excludes Delta, as in sharper de7. Full auxiliary-space facts, port placement, local strengths, positivity conditions and calibration remain those of the parent. Clock, reader and reset degrees of freedom have not silently been added to K.

## 2. Outcome weights and the exact old/reference mixture

Define unnormalized positive old/reference blocks

    S=J* sigma J,        T=Tr_B(Q sigma Q),
    s=Tr S=Tr(P sigma),  q=Tr T=Tr(Q sigma)=1-s.               (4)

The identity

    tau=S+T                                                   (5)

is exact. To see it, expand B in an orthonormal basis beginning with Omega. Every P-sigma-Q or Q-sigma-P matrix element has two different B basis labels, so its partial B trace is zero. This reasoning does not constrain AR or assume sigma is block diagonal. Positivity supplies S,T>=0.

If s>0, define alpha=S/s. The normalized successful joint state is exactly

    omega_plus=P sigma P/s=J alpha J*.                        (6)

Thus B is exactly vacuum and is in product with the *joint* AR state alpha; A and R may still be entangled. For q>0, put beta=T/q. Equation(5) becomes

    tau=s alpha+q beta.                                       (7)

At q=0 the beta term is simply absent. At s=0 no successful normalized state is defined. Retain the zero unnormalized branch instead of dividing by zero.

There is no positive lower bound on s from(1) alone: sigma=rho tensor |e><e| for any nonvacuum word e has epsilon=0 and s=0. A success-probability guarantee therefore needs a supplied auxiliary certificate or another actual lower bound on s. If delta_u=Tr(sigma n_u), n_u=(I-Z_u)/2, and eta=sum_u delta_u, then commuting projector inequalities give

    max_u delta_u <= q <= min(1,eta),
    max(0,1-eta) <= s <= 1-max_u delta_u.                     (8)

Indeed n_u<=Q<=sum_u n_u. For only certified upper bounds delta_u<=d_u, the useful conclusion is s>=max(0,1-sum d_u); do not insert those upper bounds into the upper bound on s as though they were actual populations. Per-qubit delta_u<=nu yields s>=1-min(1,4M nu). No independence or product success formula is used.

The two endpoint bounds in(8) are sharp for the information consisting only of actual local populations. Classical diagonal auxiliary distributions suffice. Realize the excitation events as nested subsets of a unit-probability interval to obtain union probability max delta_u. To obtain min(1,sum delta_u), place intervals of those lengths consecutively on a circle of circumference1; for sum<=1 they are disjoint, and for sum>=1 their union covers the circle. Their event-indicator words define a diagonal density operator. This is a sharpness construction, not a physical preparation protocol.

## 3. Conditional full old/reference disturbance

For s>0, (7) gives alpha-tau=q(alpha-beta). Consequently

    ||alpha-rho||_1 <= d_*:=min{2, epsilon+2q},
    ||omega_plus-J rho J*||_1=||alpha-rho||_1.                 (9)

The second equality is invariance of trace norm under the isometry J. The bound has no epsilon/s amplification: the complete pre-instrument old/reference marginal is already the mixture of the two conditional marginals. The potentially large change caused by rare postselection is retained by q approaching1 and the cap2. A certified upper bound q<=q_bar may replace q monotonically; a positive successful branch is still required.

Equation(9) is a sharp *universal* bound as a function only of q and an upper bound epsilon, allowing rho to vary. Put alpha=|0><0|, beta=|1><1| on one old bit and choose rho diagonal with probability t=q+epsilon/2 on |1> when t<=1. Then tau has probability q there, the marginal error is epsilon and the conditional distance is2q+epsilon. If q+epsilon/2>=1, take rho=|1><1| to achieve distance2 within the epsilon budget. The actual joint sigma can be block diagonal with vacuum weight s and one nonvacuum word of weight q; no pre-instrument coherence is required.

For a fixed specified rho, this universal expression need not be optimal. The exact feasible old conditional states at fixed0<s<1 are precisely the alpha for which there is a normalized beta with

    alpha,beta>=0, Tr alpha=Tr beta=1,
    ||s alpha+q beta-rho||_1<=epsilon.                       (10)

Necessity is(7); sufficiency follows from the two-word block-diagonal sigma just described. Additional spectral or state information can therefore sharpen the certificate without a new physical assumption. For example, if epsilon=0 and rho is pure on the *whole AR system*, positivity of rho=s alpha+q beta forces alpha=rho whenever s>0. No such purity is presumed in(9).

The full pre-instrument joint state can change by order sqrt(q), even though its successful AR marginal changes by at most2q relative to tau. Take

    |Psi>=(4/5)|0>_A|0>_R|Omega>_B
                     +(3/5)|1>_A|1>_R|e>_B,              (11)

where e has just one excitation. Then q=9/25, rho=tau and epsilon=0. The successful alpha is |00><00| and ||alpha-rho||_1=18/25, exactly2q. But || |Psi><Psi|-omega_plus ||_1=6/5=2sqrt(q). Thus(9) cannot be reinterpreted as a linear-q bound on disturbance of the original ABR state. This selected exact analytic control settles that distinction without a numerical run.

The successful reference marginal also need not stay fixed. With epsilon_R=||tau_R-rho_R||_1, define e_R^+=||alpha_R-rho_R||_1. The same mixture argument and partial-trace contraction give

    e_R^+ <= min{2, epsilon_R+2q, d_*}.                     (12)

Even epsilon_R=0 before the instrument does not imply e_R^+=0. The example(11) attains e_R^+=2q. Discarding the flag gives the same unconditional old/reference marginal tau exactly; retaining a particular outcome is different.

## 4. Exact successful energy moments and sharp universal scalar bounds

From(3),

    KJ=J(H+c I)+sqrt(Delta)VJ,
    J*KJ=H+c I,
    J*K^2J=(H+c I)^2+Delta kappa I.                         (13)

The cross term in the last equality vanishes because J*VJ=0; the remaining vacuum column is exactly J*V^2J=kappa I. This proof uses the actual full K, not the compression squared. In particular, (J*KJ)^2 alone misses Delta kappa.

Write m0=Tr(rho H), mu0=m0+c, and v0=Var_rho(H)+Delta kappa. For the successful state,

    mu_+=Tr(alpha H)+c,
    Tr(omega_plus K^2)=Tr(alpha(H+c I)^2)+Delta kappa,
    Var_(omega_plus)(K)=Var_alpha(H)+Delta kappa.            (14)

These are exact normalized-state identities, with all traces over the old/reference state where appropriate. The coupling variance remains in the baseline; its cancellation in a difference does not make it free. An installed scalar changes the physical first and raw second moments and retains its timing/phase and implementation costs.

Let osc(O)=lambda_max(O)-lambda_min(O) for a finite Hermitian operator O, set W=osc(H), and put t_*=d_*/2=min{1,q+epsilon/2}. For any Hermitian O on A, trace zero of alpha-rho gives

    |Tr[O(alpha-rho)]| <= osc(O) t_*.                        (15)

Subtract the midpoint of O's spectrum, then use trace duality. Thus

    |mu_+-mu0| <= W t_*,
    |Tr(omega_plus K^2)-Tr(J rho J* K^2)|
                       <= osc((H+c I)^2) t_*,
    |Tr[omega_plus(K-mu0 I)^2]-v0|
                       <= osc((H-m0 I)^2) t_*.              (16)

The raw-second bound retains c. If only ||H||<=h0 is supplied, an explicit spectral-interval upper bound for its coefficient is

    osc((H+c I)^2)
       <=(|c|+h0)^2-[max(0,|c|-h0)]^2.                     (17)

There is also a sharp universal variance modulus. Define the nondecreasing function on[0,1]

    f(t)=t(1-t) for0<=t<=1/2;   f(t)=1/4 for1/2<=t<=1.

Then

    |Var_(omega_plus)(K)-v0| <= W^2 f(t_*).                  (18)

To prove this without assuming commuting density operators, measure the spectral projections of H mathematically. The two resulting probability laws have total variation r<=||alpha-rho||_1/2<=t_*. For W=0 the assertion is immediate; otherwise rescale the eigenvalues to[0,1]. Write the laws as (1-r)C+rU and(1-r)C+rV using their common pointwise mass. Let a,u,v be the means of C,U,V. For the orientation in which the variance difference is nonnegative, its exact value is

    r(Var U-Var V)+r(1-r)[(u-a)^2-(v-a)^2].                 (19)

Reflect the interval if necessary so u>=v. Since a>=0, Var U<=u(1-u) and Var V>=0, (19) is at most

    r[u-r u^2-(1-r)v^2] <= r(u-r u^2).

The maximum over0<=u<=1 is r(1-r) for r<=1/2 and1/4 for r>=1/2. Interchange the two laws for the opposite sign and use monotonicity of f. The r=0 case is equality of laws; at r=1 the common part may be chosen arbitrarily because its coefficient vanishes. This proves(18) on the full arbitrary-reference input domain.

For a trace-distance upper budget, this modulus is attained by endpoint distributions: a pure endpoint versus an endpoint mixture of weight t_* when t_*<=1/2; a pure endpoint versus the balanced endpoint mixture once t_*>=1/2. These choices can satisfy(7) and the epsilon upper budget whenever q+epsilon/2 has the stated size, by selecting the fail mixture accordingly. Hence(18), like(9), is universally sharp from these scalar bounds, not an optimality claim for a fixed extra-known rho or a physical preparation cost.

With ||H||<=h0, simpler consequences are

    |mu_+-mu0|<=h0 d_*,
    |Var_(omega_plus)(K)-v0|<=4h0^2 f(d_*/2)<=2h0^2 d_*.
                                                               (20)

Neither coefficient contains a penalty norm. This occurs because the successful state is exactly in P and the actual square compression was retained, not because Delta or the baseline variance is small. When H=0, the normalized successful scalar mean c and variance Delta kappa are exact for every alpha, however different its reference marginal may be.

For the selected control(11), choose an allowed old H=Z on its displayed old bit, with any other original factors fixed and the same parent's K. Then W=2, m0=7/25, mu_+-mu0=18/25 and

    |Var_(omega_plus)(K)-v0|=576/625
                         =4(9/25)(16/25).                  (21)

The actual Delta kappa is present in both variances and cancels only in this difference. Equations(9),(16),(18) are simultaneously saturated in this example. The old states may be embedded in the parent's distinct original port factors; no invariant old-data eigenbasis for L,V is required for the vacuum calculation.

## 5. Reference-valued and unnormalized statements

Let M_omega(O)=Tr_AB[(O tensor I_R)omega]. The exact successful records are

    M_(omega_plus)(K)=Tr_A[(H+c I)alpha],
    M_(omega_plus)(K^2)=Tr_A[(H+c I)^2 alpha]+Delta kappa alpha_R.
                                                               (22)

For any real z, Hermitian-reference duality and(9),(12) imply

    ||M_(omega_plus)(K)-M_(J rho J*)(K)||_1
           <=||H-z I|| d_*+|z+c| e_R^+,
    ||M_(omega_plus)(K^2)-M_(J rho J*)(K^2)||_1
           <=||(H+c I)^2-z I|| d_*+|z+Delta kappa| e_R^+,
    ||M_(omega_plus)((K-mu0 I)^2)
                  -[Tr_A((H-m0 I)^2 rho)+Delta kappa rho_R]||_1
           <=||(H-m0 I)^2-z I|| d_*+|z+Delta kappa| e_R^+.
                                                               (23)

Choose z to minimize any displayed bound if useful. The duality step uses ||O tensor Y||<=||O|| for every Hermitian reference contraction Y; it imposes no classical-reference restriction. These are linear moment records, not an operator-valued variance. For example, the midpoint choice z=(h_min+h_max)/2 in the first line gives (W/2)d_*+|z+c|e_R^+.

To isolate the necessity of the reference term, use(11) with H=0 and nonzero kappa. Then epsilon=epsilon_R=0, yet the centered second-record difference is exactly

    Delta kappa ||alpha_R-rho_R||_1=2q Delta kappa.          (24)

The uncentered first-record difference is2q|c|. All normalized scalar moments nevertheless agree exactly. Pre-instrument preservation of the reference does not justify dropping these *conditional* terms.

No probability-free normalization is used. The successful unnormalized state is s omega_plus. Comparing it with s J rho J* multiplies every linear trace or reference-record bound above by s. Such homogeneous linear bounds remain meaningful at s=0, while alpha and its variance do not. The physical full instrument output includes Q sigma Q of trace q as well; an unnormalized branch is never silently promoted to a normalized channel or a reference-valued variance.

## 6. Both outcomes, backaction, time and the unchanged ledger

For q>0 define omega_minus=Q sigma Q/q. On the complete CQ output, the AB observable I_F tensor K has

    mean=s mu_++q mu_-,
    second=s second_++q second_-,
    variance=s Var_+(K)+q Var_-(K)+s q(mu_+-mu_-)^2.        (25)

These exact mixture formulas retain the failure contribution and the between-outcome spread. They do not include a physical energy assigned to the flag, instrument or reader; those are additional apparatus costs.

For a concrete unchanged-parent counterexample, take the source's correlated mixture of auxiliary vacuum and the fully excited word, with H=0 and the same old/reference state in both branches. Every local defect equals q, L has eigenvalues0 and4M on those words, and each has V expectation0 and V-squared expectation kappa. Successful scalar moments are exactly the ideal ones, but the unconditional variance excess remains

    (4M Delta)^2 q(1-q).                                    (26)

The state is already P/Q block diagonal, so the nonselective instrument does not even change it. Successful certification therefore does not prove improved unconditional preparation moments when both outcomes are retained. One cannot infer a reset or an expected repeated-trial resource from s alone without a separately supplied repeated-input/operation contract.

For a coherent input the instrument can change K-moments. Let D_P(sigma)=P sigma P+Q sigma Q. Since ||QKJ||=sqrt(Delta kappa), positivity of the state block gives the finite bound

    |Tr[(D_P(sigma)-sigma)K]|
                            <=2sqrt(Delta kappa)sqrt(sq).  (27)

For a chosen center mu0, the corresponding centered-square change is at most2||Q(K-mu0 I)^2J||sqrt(sq); the full-space column bound gamma of de7 equation12 may bound that norm. For the raw square, a sufficient column bound is gamma+2|mu0|sqrt(Delta kappa). These are AB expectation changes caused by the stipulated channel, not a Hamiltonian implementation/work ledger for that channel.

After successful certification, evolve both omega_plus and J rho J* by the same closed K for any common elapsed time. Their total K moments and the comparisons(14)–(20) are conserved. Their complete trace distance stays at most d_*, and a subsequent common channel contracts it. B need not remain vacuum during K evolution; one must not append a fresh vacuum to a later old marginal or repeat the vacuum formulas on that different comparator.

The supplied certification operation itself has no derived duration or physical generator here. If it takes time, its dynamics, background, controls, calibration, record, stopping and any reset must be supplied and charged. The chain's subsequent nominal time T is still T; no statement removes a preceding certification interval. Conservation under closed K is not asserted through an external measurement/control operation. Identifying K with physical energy, implementing(2), or interpreting its flag as a native measured record remain separate premises.

## 7. Conditional implication for the already priced chain

Retain the complete accepted chain family and its fixed constants: ||H_M||<=hM, Delta_M=D M^6 with D>0 satisfying its dynamical prescription, the same installed scalar/reserve, and all actual placement, strength and full-space costs. Suppose each actual local auxiliary population is at most nu_M. Then q_M<=min(1,4M nu_M), and for a successful ideal outcome

    d_(+,M)<=min{2,epsilon_M+8M nu_M},
    mean error<=hM d_(+,M),
    variance error<=4h^2 M^2 f(d_(+,M)/2).                  (28)

These are scalar errors. They require neither pre-instrument block diagonality nor independent auxiliary defects. They do require the additional exact binary instrument and retain its failure weight.

For desired positive scalar tolerances m_*,v_*, define

    C=min{1, m_*/h, v_*/(2h^2)},
    epsilon_M<=C/(2M^2),    nu_M<=C/(16M^3),                (29)

where a quotient with zero denominator is+infinity. Then, for every finite M>=1,

    s_M>=1-C/(4M^2)>=3/4,
    d_(+,M)<=C/M^2,
    mean error<=h C/M<=m_*,
    variance error<=2h^2 C<=v_*.                            (30)

Uniform accuracy of the physical **raw second moment** requires the separate allocation `osc((H_M+c_M I)^2)(epsilon_M+8M nu_M)/2` from(16). It does not follow from(30) for an arbitrarily growing installed reserve. The centered scalar second moment has its separately displayed H-centered bound; the physical uncentered scalar is not silently removed.

When h=0 the scalar moment errors are exactly zero under the ideal successful branch; the probability and reference qualifications remain. For mean alone, C=min{1,m_*/h}, epsilon_M<=C/(2M), nu_M<=C/(16M^2) gives s_M>=1-C/(4M)>=3/4 and mean error<=h C. These are explicit sufficient *conditional* certificates, not a supplier of these populations or the binary instrument.

Within the stated worst-case information class, the surviving powers have an elementary witness. Choose old H_M with eigenstates |a>,|b> of eigenvalues+hM,-hM, and put

    sigma_M=(1-q_M)|a><a| tensor |Omega><Omega|
             +(q_M/(4M))sum_u |b><b| tensor |u><u|,
    rho_M=Tr_B sigma_M.                                    (31)

Every local defect is nu_M=q_M/(4M), epsilon_M=0, and successful old state is |a>. The exact successful mean and variance deviations from rho_M's vacuum comparator are

    2hM q_M=8hM^2 nu_M,
    4h^2 M^2 q_M(1-q_M)=16h^2 M^3 nu_M(1-4M nu_M).          (32)

Thus when h>0, q_M tends to0 and these products diverge, a uniform smaller scalar-error claim from local populations alone fails. This witnesses the particular information-class distinction; it does not assert a necessary cost for all stronger state certificates or a physical preparation no-go. Such an H_M is allowed by the unchanged arbitrary-H premise; it can also be a sum of h Z over M original sites. No coupling or Delta is altered by the conditioning argument.

The actual baseline is still Tr(rho_M H_M)+c_M and Var_(rho_M)(H_M)+Delta_M kappa_M, with kappa_M<=kM and k=209Lambda/16. Full Pauli scalar, optional reserve, local loads of order M^6 and total norm/baseline variance bounds of order M^7 remain paid. Equations(29)–(30) change a success-conditioned input requirement; they do not replace the published unconditioned M^-20 or M^-14 certificates on the same hypotheses.

A reference-valued centered second record still pays Delta_M kappa_M e_(R,M)^+. Using only(12) and the chain upper bound yields

    Delta_M kappa_M e_(R,M)^+
            <=D k M^7 min{2,epsilon_(R,M)+2q_M}.            (33)

The scalar budgets(29) alone do not bound this uniformly: even epsilon_(R,M)=0 before certification can leave a contribution of order M^5. A sufficient separate allocation requires epsilon_(R,M)+2q_M of order M^-7, or an independently justified conditional reference-preservation premise. With only the union bound, q_M=O(M^-7) requires per-qubit nu_M=O(M^-8). The other record term involving the old centered square remains charged through the full marginal bound. For uncentered first records retain the actual scalar coefficient in(23). No reference-valued variance is claimed.

## 8. A precise imperfect-instrument extension

This section adds an explicit *supplied* norm contract; it does not derive that contract from observed outcome frequencies or implement it. Let tilde I be a CPTP binary instrument with the same AB output and classical flag, acting as identity on passive R. For the particular actual normalized input sigma, suppose

    ||(tilde I tensor id_R)(sigma)-I(sigma)||_1<=zeta.        (34)

A diamond-norm upper bound zeta on the two complete channels is a sufficient uniform alternative; the convention is again the unhalved norm. Both outcomes and arbitrary reference correlations are included. Let ideal output blocks be S_+=P sigma P,S_-=Q sigma Q, actual blocks tilde S_+,tilde S_-, and actual success weight a=Tr tilde S_+. Put e_+=||tilde S_+-S_+||_1 and e_-=||tilde S_--S_-||_1. CQ block orthogonality and total normalization imply

    e_++e_-<=zeta,    |a-s|<=min(e_+,e_-)<=zeta/2.          (35)

For s>0 and a>0, write tilde omega_plus=tilde S_+/a. Two triangle expansions, dividing once by a and once by s, give

    ||tilde omega_plus-omega_plus||_1
       <=min{2,(e_++|a-s|)/max(a,s)}
       <=r_*:=min{2,zeta/max(a,s)}.                         (36)

If a supplied lower bound s>=s0>zeta/2 is available, actual success is guaranteed with a>=s0-zeta/2>0 and r_*<=min(2,zeta/s0). If this positivity condition is not available, normalized actual-success statements apply only when a>0; spurious rare outcomes cannot be treated probability-free. For equal a=s, the factor zeta/s is attained by perturbing only the conditional pass state, with the fail block unchanged. If s=0 the ideal normalized pass comparator is undefined, though(34)–(35) and the unnormalized branches remain valid.

The actual successful output need not be exactly vacuum. The ideal probability of the event PASS and Q is zero. Measuring that event and using the total normalized output trace distance yields

    Tr(Q tilde omega_plus)<=min{1,zeta/(2a),r_*/2}.          (37)

For the branch-resolved information, the stronger bound (e_++a-s)/(2a) also holds: apply the positive-part trace bound to tilde S_+-S_+, whose trace is a-s. All bounds are conditional on a>0. A label called PASS alone does not establish exact projection.

Consequently the actual conditional full-state error to J rho J* is at most min{2,d_*+r_*}. On the same installed K let W_K=osc(K). Triangle comparison through omega_plus and the proved spectral/variance inequalities give

    actual mean error <=W t_*+(W_K/2)r_*,
    actual raw-second error <=osc((H+c I)^2)t_*
                                      +(osc(K^2)/2)r_*,
    actual variance error <=W^2 f(t_*)+W_K^2 f(r_*/2).        (38)

These are sufficient finite bounds. They expose the penalty sensitivity of imperfect projection rather than treating(14) as exact on a mislabeled branch. The parent's full-space bounds imply, for example,

    W_K<=W+4M Delta+2sqrt(Delta)v,
    v=sum_u |g_u|,

by spectral-diameter subadditivity,0<=L<=4M I and ||V||<=v. This scalar-independent diameter does not delete c from the physical energy or raw K^2 bound. Alternatively, actual certified post-success local populations and full old/reference error may be supplied to the sharper source's complete formulas. Equation(37) alone gives only a global leakage bound and cannot justify independent-cell estimates.

If an actual apparatus has drift, finite operating time, calibration error, extra outputs or discarded work, those belong in the definition and proof of its complete channel contract(34), or in separately priced Hamiltonian/read-time bounds. This note does not infer(34) from average-state testing, flag probabilities, auxiliary population tests or an unobserved coherent flag. It also does not equate a mathematical partial trace with a physical collapse or classical reader.

## 9. Necessary distinctions and disposition

Several shortcuts are explicitly refuted at their claimed scope. Old/reference accuracy alone gives no success lower bound. A successful projection need not preserve old/reference input or the conditional reference marginal. Full pre-instrument joint-state disturbance can be square-root in q even when the old/reference conditional bound is linear. Exact auxiliary vacuum still leaves Delta kappa baseline variance. Success-conditioned bounds do not erase failure or its unconditional energy spread. Approximate flag accuracy does not certify an accurate instrument or an exact vacuum.

For the last distinction, even when s=1 an actual operation can rotate the old state inside P while always reporting PASS; outcome probability and vacuum tests remain perfect but the old/reference state can change maximally. For the failure-coherence distinction, take a nonvacuum superposition (|u>+|v>)/sqrt(2) with u!=v. Ideal FAIL retains its pure state, whereas measuring all bits and coarse-graining yields the diagonal mixture, trace-distance1. Mixing this with any vacuum weight s leaves pass behavior unchanged and gives full CQ discrepancy q. Both outcomes are part of the stipulated contract, so a fine-syndrome measurement is not silently substituted.

The analytic mixture proof and the independently organized bounded-variable variance proof are complete within the displayed finite contract. The rational-amplitude and correlated-mixture controls are exact symbolic calculations, not numerical evidence or a broad sweep. No mathematical program was executed. The only recorded program captures exact source bytes and identities. There was no mathematical failed run; the initial display truncation was repaired by complete source reads and is disclosed. Root's future candidate remains unexposed until the seal.

The concrete remaining physical obligation is a fully specified implementation or independently certified complete binary-vacuum instrument meeting a useful success and full-reference error contract, with its operating time, unchanged-background comparison, clean work, control geometry/strength, reader, failure handling and reset costs. This derivation is a conditional certificate to assess such a supplier. It does not certify that supplier, a universal optimum physical cost, a native readout law or retained science.
