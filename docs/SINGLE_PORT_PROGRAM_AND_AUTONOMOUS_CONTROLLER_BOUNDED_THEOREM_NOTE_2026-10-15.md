---
title: A single-port program compiler and a prepared autonomous nearest-neighbor controller
claim_id: single_port_program_and_autonomous_controller_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: finite one-port endpoint/window compilation followed by a static ordinary-NN prepared-controller realization, with complete retained outputs and explicit growing resource costs
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: a supplied computable finite plant and target, unrestricted finite compilation time, specified pure clock and auxiliary vacuum, paid static coefficients, scalar reserves, isolation and calibration; no native initialization or resource reuse
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["positive_unary_cycle_clock_bounded_theorem_note_2026-10-14"]
runner: scripts/single_port_program_and_autonomous_controller_2026_10_15.py
next_trace_action: execute bounded source-integrity and integration gates on the separately bound stack, then regular PR and separate retained audit
---

Claim type: bounded_theorem

# One accessible port, then a prepared static controller

Can a finite program act on a fixed plant through one boundary port, and can a finite static nearest-neighbor apparatus supply that port's drive while retaining its own outputs? Two conditional constructions answer these questions at finite, unrestricted resource cost. The first compiles a supplied unitary into a smooth external X/Y schedule. The second realizes any schedule of that stated class with a prepared coherent clock and vacuum mediators. Their composition removes runtime external driving within the installed Hamiltonian model. It does not prepare the controller, install or isolate its hardware, supply consumed memory, or establish a repeatable native apparatus.

Primary-runner role: source integrity only. The proposed runner checks exact proof/review bodies, source recovery, canonical dependency bytes and actual binding evidence. It executes no scientific program, pulse search, simulation or proof test. The historical source proposal was unexecuted. This separately bound version requires real root publication-review and selected-base receipts; later primary, cache, mutation, graph and publication outcomes remain separate. The runner certifies no retained audit.

The external compiler has current qualified root acceptance `bbe2e9c911e3323f840855fb2e77cc5e86d1669486eb8c8dda2e8cdec3ff53eb`. The autonomous controller and their explicit conditional composition have root acceptance `134cbee6390a6f999813dd0234fe869bdd0bec2dddbd5d47a2209091c0dcbe5f`. Those are scientific source dispositions. Root has separately reviewed this publication interpretation under acceptance6077453829fd70821e2b251624346ed533dc2447cf877992bdbaafe9077ee425; actual downstream integration outcomes remain separate. Four complete historical bodies follow unchanged: compiler derivation `bda0be88…`, its separate review `3ad0ab65…`, controller derivation `0e91f936…`, and its separate review `52eb2e2d…`. Their original pending language and the compiler's identified intermediate wording defects remain visible. This current wrapper applies the mandatory qualifications; packaging is not an additional independent science check.

## 1. Two interfaces with one full-output composition

| Interface | Supplied inputs and generator | Actual-time comparison | Remaining supply |
|---|---|---|---|
| External compiler | Nonempty finite fixed inventory, complete computable onsite/ordinary-NN H, target W and determinant lift, arbitrary old/filler/reference input; added weak positive path lambda J, reserve r and one smooth positive X/Y port drive C(t) | `U_C(T+s)` approximates `exp[-i chi(T+s)] exp(-isH) W exp(-iTH)` for `0<=s<=w`; T is returned by a terminating search | External timing/waveform, installed path/reserve, coefficient access, isolation, any consumed memory |
| Static prepared controller | The resulting positive plant background `H_P=H+rI+lambda J`, or any independently supplied positive finite plant background, and an admitted finite C(t); new coherent one-head clock and mediator vacuum | `exp(-itK_phys)J_in` approximates `exp(-itR_pos)[vac_A tensor phi_a(t) tensor U_C(t)]` uniformly to a selected `tau>T+w` | Prepared clock/vacuum, static couplings/counterterms/reserves, complete calibration and observation interface |
| Composition | The exact compiler output schedule satisfies the controller's waveform contract | At T+s the target is `exp[-i(R_pos(T+s)+chi(T+s))] [vac_A tensor phi_a(T+s) tensor exp(-isH)W exp(-iTH)]` | All preceding supply and aged-state premises remain; no discarded controller or restored-resource assertion |

Every plant factor and passive reference is retained. Filled-box path factors have arbitrary input; they are not silently initialized mediators. The new pure clock and vacuum are separate independently supplied inputs. An identity action on fillers means no additional disturbance relative to the full target: joint old–filler correlations still transform under W and H. The actual physical time is the same throughout. The target window follows H evolution; it does not freeze an output state.

## 2. The external compiler and its mandatory corrections

Enclose the nonempty old inventory in a rectangular integer box with one margin layer, add all missing factors, and install a Hamiltonian path through that box. Its L−1 bonds are `I−SWAP`, each positive of norm 2. A single port at the fresh corner admits only `g f(t)(I+sigma P)`, P=X or Y, `sigma=±1`, with serial nonoverlapping pulses. The original H, its scalar and every retained installed term remain present. Complete matrix coefficients and a norm bound are supplied; the norm bound alone is not compiler data.

The pure-path Lie induction uses double commutators. After subtracting known prefix terms, `T_X=−2(YY+ZZ)`, `T_Y=−2(XX+ZZ)`, and `T_Z=−2(XX+YY)`. Their linear combinations isolate the bond axes; prefix rotations, commutators and the adjoint ideal complete the induction. A single commutator is `i(YZ−ZY)`, not the isotropic bond. The separate review supplies this correction to the historical source.

Replacing the path drift by the supplied drift plus lambda times that path gives a nonzero Lie-word determinant polynomial: its highest coefficient is the nonzero pure-path determinant. Thus some arbitrarily weak rational lambda can be selected by certified dovetailing. This does not say every weak lambda works. The augmented compact-group argument tracks actual H aging while using only positive physical durations. A finite rational-word search, with supplied target phase lift, terminates existentially under the stated computability premises. It supplies no practical resource estimate, measured pulse instance or prescribed runtime bound.

Same-duration cubic ramps produce a C1 positive physical waveform. The traceless smoothing allowance is `g sum rho_l`; the physical positive pulse has norm `2g f_l`, scalar area `A_s=g sum(t_l−rho_l)`, variation `4gN_a` and peak slew at most `3g/rho_min`. With `j0=(L−1)/2`, its coherent phase is `chi(T+s)=(r+lambda j0)(T+s)+A_s+theta`. The path is included exactly during compilation; only the post-compilation window uses the small bound `lambda b_J w`, `b_J=3(L−1)/2`. No assumption `lambda T<<1` is made.

The norm reserve `r>=h+zeta_peak` proves positivity of the **whole** actual generator. It does not make separately listed old or faulty local channels positive blocks. A consumer requiring that stronger decomposition must explicitly supply local terms and adequate allocated reserves, with the changed scalar phase and action paid. Whole-generator positivity suffices for the controller's `H_P>=0` hypothesis; the new controller blocks have their own positive decompositions.

For regular closed driven dynamics, endpoint-defect bounds can control calibration-dependent work without derivative bounds. With the same initial state, zero endpoint C and defect D, the accepted bound is

    |W_actual−W_nominal|
      <= [h+lambda(L−1)] min(2,2E_cal) + ||D(T)|| + ||D(0)||.

Variation/derivative control is a separate sufficient route for termwise work estimates. Integrated unitary error alone does not supply endpoint work or peak positivity. The oscillatory scalar with zero endpoint work and the terminal scalar spike with unbounded endpoint work remain explicit witnesses in the review. These are finite-Hamiltonian bookkeeping statements, not a microscopic work, heat-bath or Landauer identification.

## 3. From the admitted waveform to a finite prepared clock

For a supplied finite C1 port waveform, choose a positive step approximation on K equal cells of `[0,T]`, zero afterward. Its integrated error is at most `L_C T^2/(2K)` and its total variation, including the final return to zero, is at most `Var(C)`. Encode this step waveform with a positive Fejer average on a circle of length `4tau`. Each sample is `a_j I+b_jX+c_jY`, with `0<=a_j<=g` and `sqrt(b_j^2+c_j^2)<=a_j`. The scalar samples are physical clock occupation terms; they cannot be removed before comparing the controller.

The sole direct mathematical parent is the [accepted positive unary-cycle clock theorem](POSITIVE_UNARY_CYCLE_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-14.md). Its exact current note is 42,367 bytes, SHA256 `fa7028e0e9ad6c2c7d4c1c399feae8f9581f301dda5b46f8800eb6c355137542`. Its complete c7a proof appears uniquely at bytes `[8789,41808)`. The canonical packet's separate review is the gzip object stored as 12,394 bytes, SHA256 `736e2741a361d4630c8a62be986382fb607711889745ee1a2fdaba882a2b6cee`; decompression yields the complete 29,118-byte `8d76345b…` review at `[0,29118)`. The dependency packet binds both forms. The old large publication archive is not copied recursively.

Use that theorem at horizon tau, including the inactive tail, with arbitrary unchanged finite `H_P`. The finite positive step waveform is inside its proved domain. The strict ordinary-band alias guard, **two** Dyson comparisons, packet and smoothing errors, sine dispersion and the actual free-clock phase remain charged. Its independent specified one-head packet is essential. Neither a generic arbitrary-clock theorem nor the old theorem's nonlocal geometry or optional controlled initialization is imported. The b726 restatement and earlier mediator are provenance/context; the new contraction and exterior geometry are proved below, so they are not additional direct mathematical parents.

## 4. One exterior component and the two-axis mediator

Translate coordinates only as notation so the filled plant corner is `(0,0,0)`. Place the M-site clock square at z=−3 and its auxiliary copy at z=−2, with lower-left coordinates `(d0,d0)` and `d0>=2`. A tail joins `a=(−1,0,0)` to the auxiliary square with length `2d0+3`. The auxiliary graph has `m=E_A=M+2d0+3`, maximum internal degree 3, and one connected cycle-plus-tail component. There are `2M+2d0+3` fresh factors and `3M+2d0+4` new declared geometric edges. The only new plant edge is p–a; all old positions and terms remain fixed. Multiple Pauli coefficients use an existing edge, not additional neighbors.

The auxiliary penalty uses one-excitation matrix `B=I−A_B/12`. Explicit positive local blocks give the **full-sector** bound `L>=3N_A/4`, a unique vacuum and a bounded reduced resolvent. Positive inverse entries obey `t_j=(B^-1)_(a,u_j)>=12^-dist(a,u_j)`. These denominators are certified but may make source strengths enormous; no polynomial-resource assertion follows.

Use port `q(XX+YY)` and clock-controlled auxiliary quadratures with `z_j=−(b_j+i c_j)/(2q t_j)`. With the stated Pauli convention the vacuum creation operator at p is `q(X+iY)`, whose square is `4q^2 n_p`, not a scalar. On the nominal one-head clock sector only, the vacuum contraction is `Sigma=C0−W`, where

    W=sum_j n_j(b_j X+c_jY),
    C0=4q^2 gamma_a n_p+sum_j |z_j|^2 gamma_j n_j.

C0 is actually installed and priced. Multi-head cross terms do not vanish. Number conservation is exact for the nominal construction; arbitrary leakage faults require the unrestricted full-space perturbation allowance.

For `K_Delta=Delta L+sqrt(Delta)V+H_b+C0`, the comparison corrector `Z=J−Delta^-1/2 X1+Delta^-1 Y2` uses the complete reduced resolvent. Y2 lies in the two-excitation auxiliary sector. The exact residual retains every noncommuting H_P, clock, counterterm and program product. Both endpoint differences between Z and the bare vacuum injection J are included, giving the stated finite error `F1/sqrt(Delta)+F2/Delta`. No dressed state is prepared. The literal reserve `R_pos=sqrt(Delta)(2q+sum|z_j|)` makes the static generator positive on the full space and has an explicit allocation to new positive edge blocks.

## 5. Error, moments and paid resources

The autonomous isometry error is `eta_step+eta_clk+eta_med`. Composing the accepted compiler adds its `epsilon_c+epsilon_w` allowance. For arbitrary plant/reference density operators, the complete retained trace error is at most twice the sum, capped at 2. Initial full-state error adds directly and an actual generator defect E adds `2 integral||E(t)||dt` over the actual interval. Every omitted edge, scalar, source, counterterm, old-background error and number-leaking term belongs in that full-space budget. Observation-time error uses the full installed generator norm or changes the time-indexed target consistently.

The full norm, normalized Pauli scalar and local channel ledgers remain as written in the bodies. They include clock bonds, transport diagonals, both port quadratures, both clock-source quadratures, the nonscalar p counterterm, sampled scalar fields and every positive reserve. On a plant/clock density rho with fresh auxiliary vacuum,

    mean(K_phys)=Tr(rho A)+R_pos,
    Var(K_phys)=Var_rho(A)
       +Delta[4q^2 Tr(rho n_p)+sum_j |z_j|^2 Tr(rho n_j)].

All covariance within A remains. Full static energy moments are conserved; component energies need not be. Vacuum leakage probability at most `eta_med^2` gives only a penalty-energy allowance `Delta ell_L eta_med^2`, which need not vanish. Approximate return in trace norm does not establish small energy variance, refunded preparation or reuse.

Static nominal operation has no external pulse-work integral. Installation, independent state preparation, physical coefficient access, clock coherence, full calibration, isolation and observation remain supplied interfaces. Runtime and local strengths can be arbitrarily large, and accuracy refinement can require correspondingly tighter absolute precision. The compiler's search and the controller's finite inverse-entry bounds do not establish efficient synthesis, a common hardware/temperature cap, native energy interpretation or a laboratory device.

## 6. Counterexamples and remaining obligations

The bodies retain failures of specific shortcuts: cancellation of the useful path at a particular lambda; inability to obtain the endpoint's actual H aging from an unaugmented controllability statement; the evolving two-qubit path after an endpoint; phase and scalar deletion; unpriced memory aging; the work witnesses; omission of the mediator's p counterterm; nonzero multi-head clock cross terms; the failure of an XX-only source to supply the second axis; deletion of a_j; and substitution of a dressed input for the bare vacuum. These witnesses delimit those routes. They are not universal no-go claims or a manufactured route-count gate.

Pure-memory reset requires an independent supplied memory on which the relevant background is trivial up to retained scalars, or a separately adequate state premise after the actual aging time. A general compressor likewise requires its own proved contract on that actual input. No Gibbs-source, correlated-memory or later frontier theorem is imported by this publication. Positivity and a finite static graph do not manufacture pure clock/vacuum states. No detector interaction, permanent record mechanism, resource restoration or native control bootstrap is proved.

The two decisive checks were source exposed with the same selected model/effort and shared earlier machinery. Their current claims are analytic; no pulse-search instance, simulation, scientific fixture, historical science replay or formal proof was executed for these new sources. Metadata identities preserve the exact evidence and failure history without supplying extra mathematical validation. Scientific source acceptance, publication interpretation, actual Git binding/execution, regular PR publication and independent retained audit remain distinct stages. The source decisions and publication interpretation are complete at the exact recorded identities. The current binding identifies the separately selected Git base and real review evidence; actual execution, regular publication and retained audit are separately recorded outcomes. The transverse-field predecessor is Git ancestry only and supplies no theorem here.


---

## Immutable source body: compiler_author

Historical source retained exactly; the current wrapper and separate root decisions govern interpretation.

# A weak fixed path and one externally driven port: a finite full-output endpoint/window reduction

Status: author-proposed conditional theorem; separate independent checking is pending. The autonomous prepared-controller interface remains open. This is a different contract from uniform simulation of the previous sampled Hamiltonian H_aut.

The result below reduces spatial control access for a supplied finite preparation unitary to one boundary port. It does so by adding a known positive NN path, supplying complete computable background coefficients, permitting arbitrarily long but finite compilation time, and supplying one externally timed X/Y waveform. It proves a full retained-plant output bound at the actual preparation endpoint and throughout a predeclared finite window. It does not manufacture that waveform, its timing apparatus, a quantum controller state, or reset-memory purity. No claim of native control or efficient resources is made.

## 1. Exact target, domains and premises

Let V_old be a supplied finite set of distinct fixed cubic-lattice sites. Every original data, apparatus, memory and clock factor intended to remain in the problem is included, at its original position. Let H be the complete fixed background on these factors, extended by identity to subsequently added qubits. H includes the literal unchanged original H0. It may also include a retained K_X or other declared installed terms. Specify which terms are present before applying the result; it is not permissible to remove K_X or replace H0 by relabeled terms. H is a finite ordinary-NN two-qubit/onsite Hermitian sum with computable coefficients and a certified full-space bound h >= ||H||. Its coefficients, not merely this norm bound, are supplied to the compiler. No commutation among its terms is assumed.

Let F be all added path fillers, including the control port. All of F is retained and may start in an arbitrary state, correlated with V_old and an arbitrary passive reference R. The compiler acts on the entire plant P=V_old union F. A supplied finite computable unitary W_old on V_old specifies the desired finite preparation program. Set W=W_old tensor I_F. More generally a target may explicitly act on selected new memory factors, provided those factors are included in V_old for the geometry and in W from the outset. The name V_old means the fixed inventory for this invocation, not a claim about manufacture or thermodynamic origin.

The channel theorem is for every density operator rho_PR, with no clean-filler assumption and no restriction to a single-excitation sector. If a consequence of W, such as resetting a register, requires supplied pure or biased memory, that is a separate explicit restriction of rho_PR. A unitary compiler does not prepare arbitrary mixed memory for free.

Choose supplied computable data: a port strength g>0, a finite output-window length w>=0, and positive tolerances epsilon_c, epsilon_w. The allowed external controls are onsite terms at one port p only. They have the form

    C(t) = g f(t) (I + sigma P_p),
    P in {X,Y}, sigma in {+1,-1}, 0<=f<=1,

with at most one pulse active at a time; zero is allowed. The scalar I is the same physical global identity whether assigned to p or to a bond. These controls are positive, and their scalar phase is retained. Their smooth envelopes, signs and start times are supplied external settings. No other time-dependent plant channel is used.

We will construct a fixed added network lambda J and a finite C^1 pulse schedule of duration T. T is an output of a terminating search, not a user-fixed deadline or an efficient bound. At t=0 and T the controls vanish. They remain zero on [T,T+w]. With a retained scalar rI, the actual nominal generator is

    H_ph(t) = H + rI + lambda J + C(t).                         (1)

The preparation and window target, up to an explicit known phase, is

    U_tar(T+s) = exp(-i s H) W exp(-i T H),   0<=s<=w.           (2)

Thus actual H aging of duration T precedes the ideal endpoint program, and actual H aging of duration s follows it. The physical generator (1) acts continuously, and lambda J is included exactly during compilation. Formula (2) is a direct endpoint/window comparison; it does not claim that W was literally instantaneous, or that intermediate states follow the earlier autonomous program. In particular it is not the old split t_c/t_s comparison with K replacing apparatus evolution during a swap.

## 2. Whole-program geometry without moving any old factor

Enclose V_old in an integer rectangular box B with one empty margin layer in each coordinate direction. For example let

    l_alpha=min_{v in V_old} v_alpha-1,
    u_alpha=max_{v in V_old} v_alpha+1,
    n_alpha=u_alpha-l_alpha+1,  L=n_x n_y n_z.

Put one qubit at every previously unoccupied site of B. These L-|V_old| qubits are precisely F. They are physical new factors, not relabeled old data, and no state is assumed for them. The corner p=(l_x,l_y,l_z) is fresh. An explicit Hamiltonian path starts there: traverse x forwards/backwards on alternate y rows in the lowest z plane; traverse the resulting complete two-dimensional list forwards/backwards on alternate z planes. Adjacent rows meet at the same x endpoint, and adjacent planes meet at the same (x,y) endpoint, so every step is NN. Each site occurs once. Write the resulting ordered sites v_1=p,...,v_L.

Install

    J = sum_{k=1}^{L-1} (I-SWAP_{v_k,v_{k+1}})
      = (L-1)I/2 - (1/2) sum_{k=1}^{L-1}
                           (X_k X_{k+1}+Y_k Y_{k+1}+Z_k Z_{k+1}). (3)

Every bond is positive with norm 2. Hence J>=0, ||J||<=2(L-1). Its normalized trace is j0=(L-1)/2 and

    Jbar = J-j0 I,   ||Jbar||<= b_J=3(L-1)/2.                  (4)

The path adds at most two incident bond channels per site, on geometric edges already allowed by the cubic lattice. Old-old, old-new and new-new added bonds are all expressly supplied. In particular a saturated site such as v1=(-1,0,0) is not given a seventh neighbor: an added path interaction uses an edge to an already occupied neighbor. The input of that neighbor remains arbitrary. The proof treats all such sites as interacting data, not as initialized mediators. H0 is never conjugated by a change of labels.

The geometric edge set of the filled box has

    E_B=(n_x-1)n_y n_z+n_x(n_y-1)n_z+n_x n_y(n_z-1)

members. The nominal nonzero edge inventory is the union of the original declared supports and the L-1 path edges. Their overlap means addition of coefficients on the same physical two-qubit support, not another edge. Every edge in the set difference between all NN pairs in B and this union is a nominal zero channel. All such unlisted old-new, new-new and old-old bonds are covered by the full-space isolation budget in section 8. There are no original factors outside B in the supplied finite inventory. A larger occupied environment would have to be included or separately bounded; this construction does not assert a vacuum boundary for an unspecified infinite substrate.

The onsite external port uses no fresh neighboring site. Its negative-coordinate neighbors lie outside B and are available only if a later explicitly supplied autonomous controller uses them. That future controller is not part of the present geometry theorem.

## 3. Pure-path Lie algebra, checked independently here

Remove identity terms and use skew-Hermitian generators. The pure path Jbar with X_1,Y_1 generates su(2^L). Here is the elementary induction underlying that statement.

The two port controls give Z_1 by commutation. Suppose the full traceless algebra on sites 1,...,k is available. Commute a Pauli at k with Jbar. All edges beyond (k,k+1) commute with it, and contributions from earlier edges belong to the already available prefix algebra and may be subtracted as Lie-algebra elements. The remaining coupling is a nonzero multiple of

    X_k X_{k+1}+Y_k Y_{k+1}+Z_k Z_{k+1}.

Double commutators with X_k,Y_k,Z_k respectively isolate the sums YY+ZZ, XX+ZZ, XX+YY, up to nonzero real factors. Their linear combinations isolate XX, YY and ZZ. Commutation with prefix single-site Paulis then supplies, for example, X_k Y_{k+1}. Commuting X_k X_{k+1} with X_k Y_{k+1} supplies Z_{k+1}; cyclic variants supply X_{k+1},Y_{k+1}. All are statements in the skew-Hermitian algebra with harmless nonzero real factors retained by linear span; no negative physical-time pulse is inferred at this stage.

The adjoint closure of any nonzero traceless prefix factor under su(2^k) spans that algebra: its span is a nonzero ideal, and su(n) is simple for n>=2. With the new single-site algebra this yields every traceless tensor-product Pauli on the enlarged prefix and hence su(2^{k+1}). Equivalently this last assertion follows directly from commutators of matrix units. Induction proves the claim.

This agrees with the endpoint-Heisenberg special case of Burgarth, Bose, Bruder and Giovannetti, Phys. Rev. A 79, 060305 (2009), arXiv:0805.3975v2. Their graph-infection criterion is context for this algebraic step; it supplies neither the compilation time nor a physical autonomous controller. The proof above is supplied so that extra background edges are handled by the next lemma, rather than being silently covered by a pure-path infection hypothesis.

## 4. Arbitrarily weak controllability despite the fixed background

Put d=2^L, h0=Tr(H)/d, Hbar=H-h0I. The coefficient h0 is an energy offset, not the earlier symbol H0 for the original Hamiltonian. All matrices below are full d-dimensional matrices, never excitation-sector restrictions.

Select d^2-1 iterated Lie words in the three symbols iJbar,iX_p,iY_p whose evaluations form a real basis of su(d). Such a finite list exists by section 3. It can be found by exact rational Lie closure, since the pure-path matrices are rational Pauli combinations. Let r_l be the number of occurrences of the drift symbol in word l.

Replace iJbar by i(Hbar+lambda Jbar) in every word. In a fixed real basis of su(d), column l is a polynomial in lambda of degree at most r_l, with leading column lambda^{r_l} times its selected pure-path evaluation. Consequently the determinant p(lambda) is a polynomial with nonzero leading coefficient at degree sum_l r_l. It is not identically zero. Its real roots form a finite set. Whenever p(lambda)!=0, the background-plus-path drift and the two port axes generate su(d).

For every lambda_max>0 there is therefore a rational

    0<lambda<lambda_max,    p(lambda)!=0.                       (5)

This is an existence statement for every supplied computable H, not an assertion that every weak coupling works, or that a fixed waveform works without knowing H. Some choices cancel the useful path or acquire an exact symmetry. The following semidecision gives a constructive choice: enumerate rationals in (0,lambda_max); dovetail certified interval evaluations of their determinants; accept any candidate whose determinant interval excludes zero. Computable matrix coefficients give converging error certificates. At least one candidate is nonzero, so dovetailing terminates. No test for exact equality of a general computable real is required.

For example take lambda_max=epsilon_w/[b_J(1+w)] in the chosen time units, or a smaller certified positive cap. Then every selected lambda satisfies lambda b_J w < epsilon_w, including w=0 without deciding equality of a computable real. Rational candidates are admitted to the search only after certifying their strict inclusion in (0,lambda_max). The strict window inequality is preserved by this search. This weak-network choice controls only the post-compilation window. The full drift Hbar+lambda Jbar, at its actual chosen lambda, is used exactly in the compilation that follows, however long that compilation lasts.

## 5. Actual time and central phases: an augmented compact group

A bare endpoint-controllability statement does not imply (2), because T itself changes when a word is chosen. We solve this timing problem using a second mathematical coordinate that records actual background aging. This coordinate is not a physical auxiliary, a second clock, or a replacement evolution.

Let A=Hbar+lambda Jbar. Consider the five traceless generators A, A+gX_p, A-gX_p, A+gY_p, A-gY_p. Alongside their propagator U, evolve the mathematical coordinate R_H=exp(-it Hbar) for the same elapsed time. Thus each positive-time constant segment has the pair

    (exp[-it(A+v)], exp[-it Hbar]),
    v in {0,+gX_p,-gX_p,+gY_p,-gY_p}.                          (6)

The ambient compact group is SU(d) times the closure T_H of the one-parameter subgroup exp(-it Hbar). Let G be the closure of the semigroup generated by (6). It is a group: for each generator element, compactness makes a subsequence of positive integer powers approach identity, and hence positive powers approximate its inverse. This can also be seen by finite simultaneous phase recurrence of its eigenvalues. Products and closure then supply inverses of every element of G.

The projection of the Lie algebra g_G to the first factor is su(d), by section 4. Let

    I={Q in su(d):(Q,0) lies in g_G}.

It contains iX_p and iY_p, obtained by differences of the generators' tangent vectors. It is an ideal of su(d): for any S in su(d), choose a lift (S,z) in g_G; its commutator with (Q,0) is ([S,Q],0). Simplicity gives I=su(d). Thus G contains SU(d) times identity. Multiplying a drift pair by a compensating element of this subgroup gives (identity,exp[-it Hbar]); closure gives identity times T_H. Therefore

    G=SU(d) times T_H.                                        (7)

This proof does not assume that Hbar has rationally related eigenvalues or that a recurrence period is known. Rational positive durations suffice: they are dense in positive durations, and finite products are continuous.

Supply a computable scalar theta with Wtilde=exp(-i theta)W in SU(d). For a target furnished as a finite circuit, one obtains theta from the chosen gate logarithms/traces. Alternatively this determinant lift is additional target data. This avoids a hidden U(d) central-phase controllability assertion. Enumerate all finite words over the five symbols and positive rational segment lengths; dovetail certified matrix-exponential/norm bounds until a word of duration T satisfies

    ||U_pc(T)-Wtilde|| < epsilon_c/4,
    ||exp(-i T Hbar)-I|| < epsilon_c/4.                         (8)

Density (7) guarantees a witness with strict margins and hence finite termination. This is an explicit effective search with certified tests, albeit potentially unusably large. It follows that

    ||U_pc(T)-Wtilde exp(-i T Hbar)|| < epsilon_c/2.             (9)

One may search directly for (9), but (8) supplies a simple termination proof. Its recurrence is fully paid by the returned T. The scalar h0 T need not recur: it is retained in physical phases below. No finite common cap, known recurrence rate, efficient gate count or complexity class is claimed. The symbolic algorithm has not been run on a selected plant in this packet.

## 6. Smooth positive pulses at the same actual endpoint

Let the accepted word have N segments, durations t_l>0 and N_a nonzero-control segments. For each active segment choose a positive rational rho_l<t_l/3 so that

    g sum_active rho_l < epsilon_c/2.                          (10)

If there are no active segments, smoothing is empty. On each active segment ramp its scalar envelope from 0 to 1 during rho_l using q(z)=3z^2-2z^3, retain 1 in the middle, then use the reversed ramp during rho_l to return to 0. These envelopes are C^1, have zero endpoint derivative and have exactly the same segment endpoints as the accepted word. All zero-control segments remain zero. Total physical duration is still exactly T.

For each active segment the lost envelope area relative to a constant pulse is rho_l. Duhamel applied to the traceless plant generators therefore costs at most g sum rho_l, so (9)-(10) give

    ||U_c(T)-Wtilde exp(-i T Hbar)|| < epsilon_c.               (11)

The actual positive pulse is g f_l(t)(I+sigma_l P_l), not just its signed traceless part. Define

    A_s = int_0^T g sum_l f_l(t) dt
        = g sum_active (t_l-rho_l),
    chi(T+s)=r(T+s)+lambda j0(T+s)+A_s+theta.                  (12)

All identity terms commute and have been retained exactly. At the endpoint,

    ||U_ph(T)-exp[-i chi(T)] W exp(-i T H)|| < epsilon_c.       (13)

During the window C=0 and the installed network remains. Factoring its scalar j0 and applying full-space Duhamel only over this window yields

 sup_{0<=s<=w} ||U_ph(T+s)-exp[-i chi(T+s)]
                    exp(-i s H) W exp(-i T H)||
       <= epsilon_c + lambda b_J w
       < epsilon_c + epsilon_w.                              (14)

The proof has not estimated the compilation interval by lambda T. Its entire weak-network effect during [0,T] was included in the nominal generator A used in the word search. The interval estimate lambda b_J w is used only after the schedule stops.

The control word can include long waits with zero drive; they contribute to T, H aging, static action and phase. The original Hamiltonian is neither turned off nor dynamically replaced in (1). Nevertheless the endpoint comparison is a deliberately synthesized net transformation; it is not a claim that uncontrolled background aging commuted through the actual pulses.

## 7. Complete output and application to finite preparation

For any rho_PR, including arbitrary old/filler/reference correlations, the trace-norm distance between the actual joint output at T+s and the joint conjugation by (2) is at most

    min{2, 2(epsilon_c+epsilon_w)},   uniformly 0<=s<=w.        (15)

This follows from (14) tensor identity_R and the two-sided operator-product bound. Every old factor, filler and passive reference appears on both sides. The phase (12) is absent from density conjugation but remains explicit in the operator statement. There is no marginal discard or encoded-data relabeling. The ideal W is identity on F, so the comparison restores every filler state and its correlations at the endpoint, after whatever explicit H aging applies to it (here H is identity on F). During the compilation the fillers may become arbitrarily entangled and need not remain in their initial states.

For a concrete finite reset program, declare disjoint target sites S and supplied memory endpoints E of equal size within the fixed inventory. Supply their initial memory state independently in the necessary pure product, or supply the exact biased-memory state class of a separate compression result. Let W first run the desired reversible compressor when applicable, then exchange each S factor with its declared E endpoint; optionally include a specified computable clock-packet synthesis unitary on the reset clock. This is a finite computable W, and it is compiled globally by sections 3-6. No separate pulse channel is installed at S or E, including saturated sites. All displaced records remain in E. An arbitrary target packet is a supplied normalized computable unit vector. A computable unitary completion is obtained by taking it as the first column and successively selecting standard-basis columns with a strictly positive Gram determinant; at every incomplete stage some candidate exists, so dovetailed certified positivity tests terminate. Gram-Schmidt then uses only certified positive denominators. This specifies a full computable target unitary, with the determinant lift required in section 5, rather than a free physical packet. A finite circuit description may also be supplied directly.

If H is trivial on the independent supplied memory before the program, exp(-iTH) preserves that independence and purity. If H includes memory interactions, the target in (2) acts on the actually aged memory too, and the reset consequence requires a separately checked state hypothesis at that time. It cannot simply reuse a fresh-memory theorem. If H=H0+K_X with disjoint original clock and nonclock supports, (2) contains their exact T aging before W. A W that resets the original clock resets that aged clock using its supplied memory and retains the displaced record. A W that does not reset it must accept the aged clock. No preimage or unaged packet is silently substituted.

For clarity, in the pure-memory case let H act trivially on E and let rho_ZSFR be completely arbitrary, where Z contains the fixed factors other than S and E. Supply |0><0|_E independently. Choose W=U_psi,S SWAP_SE, with U_psi,S|0>_S=|psi>_S. The exact ideal endpoint in (2) is then

    |psi><psi|_S tensor T_{S->E}
       [exp(-iTH) rho_ZSFR exp(+iTH)] T_{S->E}^*,             (15a)

where T is only notation for the factor-identification map in this displayed ideal output; the actual construction does not move coordinates or conjugate H by this map. All Z,F,E,R factors and correlations occur in (15a). The physically compiled W executes the exchange at the net endpoint. The actual joint state is within (15), plus calibration error, of (15a); the window comparison then conjugates the entire ideal output by exp(-isH). Taking S to be the original clock plus any apparatus/auxiliary register and |psi> to be their specified joint ready state gives the complete reset-and-synthesis endpoint, conditional on that consumed pure memory. Persistence of a ready state during the window requires its actual H evolution to have that property; equation (14) itself promises the evolved ready state, not a frozen one.

This compiler can implement the endpoint unitary of the earlier finite preparation program but does not reproduce its entire intermediate schedule, its t_c/t_s phase convention, or the earlier uniform H_aut prepared-map theorem. Reusing a prior failure estimate requires applying that theorem to the exact aged input and the actual W defined here; the algebraic ability to approximate W alone is not a theorem that every old comparison target is unchanged.

## 8. Whole-space isolation, calibration, positivity and prices

Assume a full-space actual Hamiltonian defect D(t), incorporating all omitted geometric bonds, field errors, unwanted distant terms if present, and coefficient errors. Let

    zeta(t) >= ||D(t)||,
    E_cal=int_0^{T+w} zeta(t)dt < infinity.                    (16)

A sufficient zeta is the sum of the operator norms of every declared residual local term. In particular the edge set difference in section 2 must be enumerated from the actual enlarged box, not just from the old auxiliary diagram. Each residual Pauli coefficient is counted with its full-space norm, including scalar coefficients. Errors are not projected onto a low-excitation or prepared sector. Additional interaction with an unspecified external environment is not automatically covered: include its factors and supports or supply a compatible full-output perturbation model.

Duhamel adds E_cal to (14), hence 2 E_cal to (15). A constant engineering bound zeta requires zeta <= epsilon_cal/(T+w) to achieve a selected calibration allocation epsilon_cal. Large recurrence time therefore costs precision; it is not free time. Calibration may alter the useful controllability algebra, but the proof compiles the stated nominal matrices and bounds the entire actual evolution by (16), rather than presuming controllability survives an unpriced defect.

Choose a supplied computable r>=h+sup_t zeta(t), using a certified peak upper bound rather than requiring computation of the exact supremum. Then the actual generator (1)+D(t) is positive on the entire Hilbert space, since J and every C(t) are positive. If no bounded peak zeta is supplied, only the integrated error conclusion is available from (16); this positivity certificate requires a separate finite peak bound. A calibrated constant scalar reserve may be placed at p and remains installed. Its complete phase is in (12).

Concrete finite output prices, once the searches return lambda and the word, are:

* Qubits: L-|V_old| fresh fillers; no clean mediator or physical clock is included by this external-control theorem. Exactly L-1 static two-qubit path blocks are added.
* Static coefficients: per path bond, lambda/2 on I and -lambda/2 on each XX, YY, ZZ. The combined bond norm is 2lambda. A site sees at most two added path blocks, so its added block-norm load is at most 4lambda, plus its declared port load and scalar reserve if assigned there. In a scalar/Pauli channel accounting the four coefficients are separately retained.
* Peak added Hamiltonian norm is at most r+2lambda(L-1)+2g. The literal total including original H and actual defects is at most h+r+2lambda(L-1)+2g+sup zeta. These are upper bounds, not norm equalities.
* Added norm action through the complete endpoint plus window is at most

      [r+2lambda(L-1)](T+w)+2g sum_active(t_l-rho_l).

  The network and reserve continue to accrue action during every wait and throughout the window. The control action is exactly 2g sum_active(t_l-rho_l), since the pulses are nonoverlapping positive rank-one blocks on p.
* On a ramp, ||dot C|| <= 3g/rho_l because max q'=3/2 and ||I+sigma P||=2. With rho_min=min_active rho_l, peak control slew is at most 3g/rho_min, and total control variation is exactly 4g N_a. Without active segments both are zero. All are finite once the successful word and ramps are specified.
* Boundary timing and waveform errors require actual controls and times. For example a uniform schedule shift delta, with C extended by zero outside [0,T], has integrated difference at most |delta| Var(C)=4g N_a |delta|. An endpoint readout-time error may instead be bounded using the full generator norm times the duration error. If comparing to an ideal state at a changed actual time, its H aging and phase must change as well; no clock age is reset by a calibration convention.

The network is supplied already installed at t=0 and remains installed at T+w. This is not a fabrication or turn-on theorem. For nominal closed-system dynamics, the external work over preparation is

    W_ext = int_0^T Tr[rho(t) dot C(t)]dt
          = Tr[(H+rI+lambda J)(rho(T)-rho(0))].                (17)

There is no dot J term because the path never switches. Consequently |W_ext|<=4g N_a; also |W_ext|<=2h+2lambda(L-1), using 0<=J<=2(L-1)I. The scalar reserve cancels in the endpoint energy difference, while its positive action and coherent phase do not disappear. The added network's endpoint-energy change is explicitly lambda Delta<J>, with magnitude at most 2lambda(L-1). The endpoint target need not be an eigenstate of J. The work formula is a chosen finite-dimensional driven-Hamiltonian bookkeeping convention; no native energy bridge, heat bath, Landauer saturation or thermalization is inferred. Calibration-dependent work would additionally require bounds on derivatives of the actual defect; an integrated unitary error alone supplies no work bound for a rapidly varying fault.

## 9. Why the conditional result is not the autonomous target

The theorem supplies a returned finite waveform and its mathematical prices. A physical device that issues that waveform has not been built or assigned a retained quantum output. The external command is a classical parameter in (1), not an unmentioned auxiliary that may be traced out. Calling it a prepared controller would add an unsupported premise.

A sufficient next constructive interface is the following selected-waveform lemma. For the returned finite single-site C(t), fixed plant background H+rI+lambda J, T,w and error epsilon_Q, construct a finite fresh controller Q at explicit cubic-lattice sites with a specified input |q_in>, a time-independent ordinary-NN two-qubit generator H_tot, and a retained path |q(t)> such that

  sup_{0<=t<=T+w} || exp(-it H_tot)(I_P tensor |q_in>)
                 - exp[-i phi_Q(t)](U_ph(t) tensor |q(t)>) ||
       <= epsilon_Q,                                        (18)

on the entire plant Hilbert space. Here controller-plant interactions have support only at p and adjacent declared fresh controller sites; every new factor and every additional scalar/reserve is retained. The controller, its state preparation, isolation, installation, clock baseline and all coefficient/time costs must be explicit. Equation (18) is one sufficient uniform interface; a directly proved endpoint/window version at t=T+s would also suffice. It must use the same actual physical elapsed time, or explicitly transform and charge it.

The spatial reduction is meaningful: the waveform acts on a single onsite X/Y port, regardless of the number or saturation of scheduled original data pairs. However (18) is not proved here. The old autonomous clock source supplies a nonlocal sampled operator involving every clock site; the accessible-pair mediator theorem has its own literal pair geometry, source-state and full-output premises. Neither theorem, without a new compatible construction, automatically implements (18) on this filled-box inventory. In particular the three free neighbors at a box corner have a different incidence pattern from the previously published accessible pair. A future translated gadget plus a connecting tail might fit, but must prove that geometry and the required Pauli assignments, full controller-state supply, scalar terms and entire time horizon. No such fit is presumed in this result.

The result therefore retires separate externally addressable pulse channels at saturated old pairs **within the supplied weak-path/external-port model**. It does not retire the autonomous controller supplier, the new static-coupling supplier, full background calibration, finite-memory purity, or unrestricted-time premises. These are explicit inputs/open tasks, not asserted independent impossibility walls. Complete current autonomous realization is still open.

## 10. Failed shortcuts, scope checks and negative-claim discipline

The failed shortcuts are narrow and do not establish a universal no-go.

1. Applying the pure-path infection result directly to H plus a path ignores the arbitrary extra H terms. The polynomial determinant construction handles them only after supplying their computable coefficients and selecting lambda; it does not say every lambda works. For example H=cI-lambda_* J on the same path, with c>=2lambda_*(L-1), is positive but makes that chosen total traceless drift zero at lambda=lambda_*, and port controls alone leave remote factors inaccessible.
2. Endpoint control at a time selected after specifying an unaged target is insufficient to prove actual-H aging. Equations (6)-(13) solve a different explicitly stated moving-target problem. They use arbitrarily long recurrence if necessary, with all resulting action and calibration charges.
3. Exact endpoint preparation does not freeze a static added network. Already with H=0 and J=I-SWAP on two qubits, starting from |01> gives, up to phase, cos(lambda s)|01>+i sin(lambda s)|10>. Its density distance from the endpoint state is 2|sin(lambda s)|. The declared finite window and lambda choice address this effect; an unlimited window is not supplied.
4. Full su(d) does not let a unitary erase arbitrary mixed input records without memory. In particular the maximally mixed state stays maximally mixed under all unitary controls. The reset specialization uses separately supplied memory and retains its output.
5. Lie algebra uses real linear combinations and inverse directions; these are not themselves allowed negative-duration pulses. The compact positive-semigroup argument and the rational-word search, followed by explicit smoothing, are essential extra steps.
6. Dropping positive identity offsets would change the prepared-map phase. The determinant lift, h0, j0, r and pulse scalar A_s are retained in (12)-(14). No relative phases across a coherent superposition of different program labels are claimed by this single-selected-program theorem.

Alternative live directions are a direct distributed autonomous routing construction, a single-port prepared clock transducer satisfying (18), and a direct endpoint/window autonomous computation model with its own geometry. They are not ruled out here. This task actually pursued one algebraic/control route and checked the listed shortcuts; it did not perform five distinct failed construction families or obtain a negative-packet PASS. No universal no-go or wall-independence count is asserted. The known saturated-v1 and gauge-conjugation witnesses apply to their literal old routes, not to all possible static networks. Rephrasing the external waveform as a native primitive would not resolve a theorem; it would change the supplied model. No axiom or primitive is added.

## 11. Evidence and exposure

This is an analytic author derivation. No selected many-qubit matrix, pulse-search execution, numerical propagation, fixture, or historical scientific runner was executed. The Lie-word and rational-word algorithms are finite procedures proved to terminate under the stated exact computability premises; no concrete duration or gate count has been measured. Their practical feasibility remains entirely unassessed.

This author wrote the earlier single-port, joint-readiness and selection-memo sources. Root supplied the present question and checked source context. Root's later message specifically requested central-phase, computability, actual-aging, filler-domain, endpoint-energy and isolation scrutiny. It did not supply independent validation of the argument here. Exact source identities, read-scope limits, actual metadata receipts and final hashes are saved alongside this file. Source copying, searches and hashes are metadata, not scientific tests. Independent checking of this new determinant/augmented-group/finite-control construction remains pending.


---

## Immutable source body: compiler_assessment

Historical source retained exactly; the current wrapper and separate root decisions govern interpretation.

# Decisive source check of the weak-path, one-port program compiler

## 1. Finding and required current qualifications

The frozen source **bda0be884fa79905ff81f0a2642def9e2efd5302796262f5f9eb4033b2c436c0**, 33,757 bytes, supports a conditional full-space endpoint/window compiler with one externally driven X/Y port, a supplied static weak positive NN path, complete computable nominal background data, and unrestricted finite compilation time. The generic-coupling determinant, compact positive-time semigroup, augmented actual-time group, effective search, scalar reconstruction and smoothing argument hold at that scope. This does not prove the autonomous-controller interface (18) or reproduce the old autonomous program's intermediate trajectory.

Three current clarifications are needed while preserving the frozen source:

1. In section3, a single Pauli commutator with the Heisenberg bond is not a multiple of XX+YY+ZZ. The subsequent double-commutator route works; section3 below supplies the exact corrected induction. This is a repair of the stated intermediate algebra, not reliance on an unverified pure-chain citation.
2. The final sentence of section8 overstates what is required to bound calibration-dependent work. A derivative/variation bound is one sufficient route. The exact endpoint-energy identity plus endpoint-defect bounds and a final-state trace error is another, and suffices without a uniform derivative bound. An integrated unitary-error allowance alone, without endpoint information, still does not bound work. Section8 below gives both the bound and analytic witnesses.
3. Positivity certified by r>=h+sup zeta is positivity of the whole actual generator. It does not certify that every separately listed old or faulty local channel is itself a positive block. Any physical consumer demanding that stronger literal decomposition must supply it or separately reprice reserves. The new path and port blocks themselves are positive as claimed.

Also make the nonempty fixed inventory explicit for the min/max box formulas. In the intended nonempty setting, each box side has length at least3, so L>=27 and b_J>0. An empty inventory is a separate trivial construction, not an input to the displayed min/max and lambda_max formulas. Any expression dividing by T+w is for T+w>0; a zero-duration/zero-window comparison is handled without that division.

All operator and trace estimates are for the stated target

\[
U_{\rm tar}(T+s)=e^{-isH}W e^{-iTH},\qquad0\le s\le w,
\]

with the literal declared H, including original H0 and every retained installed term. Fillers are acted on by the identity in the intended target; joint correlations transform under the intended old-system unitary. “Returned filler correlations” means no additional disturbance relative to that full target, not that old–filler correlation observables remain numerically unchanged under a nontrivial W or H aging.

This is a source-exposed mathematical check using the same inherited model/effort and shared prior research context. It is not candidate-blind independence, an audit verdict, a native-controller construction or a concrete pulse-search execution.

## 2. Sources, exposure and actual review coverage

The complete changed DERIVATION, author REPORT **f6e98cb5b38470ace605d81befd6df2e8c96e483b3e9b57c922c87e0b20e498c** (5,194 bytes), READ_COVERAGE, LITERATURE_SCOPE and SELECTED_PLAN were read in untruncated outputs. The complete source manifest, source-current verification, launch/capture/finalization receipts, freeze receipt and both author metadata helpers were then read. The source freeze **15d6ad5e756548ddd1437624513b0d3b43060ba99a735b8a2ea9036449f7ba4c** has34 entries under `members`, not `files`; all are verified by the actual metadata checks accompanying this report.

The author wrote earlier mediator/joint sources, while this worker previously reviewed that machinery and the more recent memory/readiness sources. Root supplied the neutral check request and the requested scrutiny domains. Root had already read the candidate. No separate pre-exposure derivation for this program compiler was requested or created. My earlier transverse-field comparison was sealed before I opened this source, as instructed.

The new argument is self-contained apart from standard finite-dimensional Lie-group facts, whose load-bearing uses are reconstructed below. The older autonomous sourceb726 and accessible-pair source d4ed are background scope comparisons, not proof premises that establish the new filled-box controller. I did not reopen their entire historical proof graph. I did not read the author's next-realization memo or treat its source ancestry as an additional mathematical dependency. Hashing their recovery files as frozen members is not reading or validating those arguments.

I did not read or retrieve the Burgarth et al. paper in this review. The author's exact PDF and limited reading/retrieval provenance are preserved, including its statement that the earlier web extraction was not contemporaneously archived. My induction does not require the paper's infection hypothesis. No novelty, priority, full-figure or experimental corroboration is inferred. No external web theorem of efficient, exact prescribed-time or autonomous control is imported.

The proof obligations checked here are the actual Pauli propagation, leading determinant coefficient, positive-time recurrence, zero-second-coordinate Lie ideal, rational semidecision termination, all central phases, same-endpoint smoothing, full-reference trace comparison, consumed-memory specialization, enlarged geometry, and static/control/error/work prices. No scientific program, selected full matrix, symbolic solver, pulse-search fixture, numerical propagation or old runner was executed. Metadata evidence establishes exact source recovery only.

## 3. Corrected full-space path propagation

Write the traceless path drift as

\[
\bar J=-\frac12\sum_{k=1}^{L-1}
(X_kX_{k+1}+Y_kY_{k+1}+Z_kZ_{k+1}).
\]

Port iX_1,iY_1 generate iZ_1. Suppose su(2^k) on the first k sites is available. For a=k's X,Y,Z, take the double commutator [a,[a,Jbar]]. Contributions beyond edge(k,k+1) vanish; contributions from the preceding edge lie entirely on the controlled prefix and may be subtracted as known Lie-algebra elements. Denote the remaining Hermitian expressions by T_X,T_Y,T_Z. Direct Pauli multiplication gives

\[
T_X=-2(Y_kY_{k+1}+Z_kZ_{k+1}),
\quad T_Y=-2(X_kX_{k+1}+Z_kZ_{k+1}),
\quad T_Z=-2(X_kX_{k+1}+Y_kY_{k+1}).
\]

Multiplication by i places these in the skew-Hermitian algebra, with only an immaterial real sign from the nested skew commutators. Set S_a=-T_a/2. Then

\[
X_kX_{k+1}=(S_Y+S_Z-S_X)/2,
\]

and cyclic formulas yield YY and ZZ. In contrast, the single commutator is

\[
[X_k,-(XX+YY+ZZ)/2]=i(Y_kZ_{k+1}-Z_kY_{k+1}),
\]

which explains the source's intermediate wording defect. It is the double-commutator calculation, not that incorrect single-commutator identification, that supplies the isotropic bond components.

Prefix Pauli rotations produce, for example, X_kY_(k+1). Since [X_kX_(k+1),X_kY_(k+1)]=2iZ_(k+1), the new local Z is available. Cyclic choices give all three new one-site axes. Starting from one nonzero traceless prefix factor coupled to one new Pauli, its adjoint span under the prefix su(2^k) is a nonzero ideal, hence the whole prefix algebra. New-site rotations yield every prefix traceless factor tensor X,Y,Z. Together with prefix tensor I and I tensor the new axes, these span su(2^(k+1)). This also follows by counting the complete traceless tensor-Pauli basis: (4^k-1)*3+(4^k-1)+3=4^(k+1)-1.

The finite-dimensional simplicity fact used here can be seen from matrix-unit commutators: a nonzero ideal in su(n), after complexification, is a nonzero ideal in sl_n(C); commutators with diagonal matrices isolate a nonzero off-diagonal matrix unit, or create one from a nonzero traceless diagonal element, and commutators with other matrix units generate all off-diagonal units and their traceless diagonal differences. Returning to the compact real form gives the whole su(n). Thus the induction genuinely applies to the complete 2^L-dimensional plant, without a single-excitation assumption. It uses Lie linear combinations only to establish algebraic span; negative physical time is supplied neither here nor implicitly later.

## 4. Generic weak lambda and effective selection

Choose actual iterated Lie words in iJbar,iX_p,iY_p that form a real basis of su(d), d=2^L. Exact rational/Gaussian-rational matrix arithmetic can discover such a list by adjoining independent commutator words until the dimension d^2-1 is reached. The previous induction proves that this finite process terminates. It has not been executed and can be astronomically expensive.

For a word with r_l drift occurrences, replacing iJbar by i(Hbar+lambda Jbar) gives a matrix polynomial whose coefficient of lambda^(r_l) is exactly that pure-path word. The determinant formed from all selected word columns therefore has coefficient at degree sum_l r_l equal to the nonzero pure-path basis determinant. Lower terms involving Hbar cannot cancel this highest coefficient. Hence p(lambda) is a nonzero polynomial, for every fixed supplied Hbar, and has only finitely many real zeros.

There are consequently rational nonzeros in every interval (0,lambda_max). The proposed dovetail is effective with computable complete matrix coefficients: enumerate rational candidates, semidecide their strict inclusion in that positive interval, and refine certified determinant intervals in parallel until one excludes zero. It does not need to decide whether a general computable real equals zero. At least one valid candidate has a nonzero determinant, and refinement for that candidate eventually certifies it.

For the nonempty filled-box construction b_J=3(L-1)/2>0. The suggested cap epsilon_w/[b_J(1+w)] is computable and positive for computable w>=0 and epsilon_w>0. Strict certified inclusion guarantees lambda b_J w<epsilon_w, including w=0 without an equality test. These are exact-matrix computability premises, not finite experimental identification of an unknown H. A norm bound h alone would not supply this compiler. Small unmodeled errors are handled later by a full-time perturbation estimate, not by assuming algebraic controllability is robust at no cost.

The counterexample H=cI-lambda_*J, c>=2lambda_*(L-1), is valid for L>=2: the chosen total traceless drift vanishes at lambda=lambda_*, leaving only port controls. Thus “some arbitrarily weak rational lambda can be selected” cannot be replaced by “every weak lambda works.” The determinant argument addresses exactly that distinction.

## 5. Positive durations and the actual-time group

Let A=Hbar+lambda Jbar. The closed semigroup in SU(d) times T_H generated by

\[
(e^{-it(A+v)},e^{-it\bar H}),\quad t\ge0,
\quad v\in\{0,\pm gX_p,\pm gY_p\},
\]

is a group. For any one of its generator elements a, compactness gives arbitrarily large positive powers arbitrarily close to identity, by recurrence of powers in a compact group. Then a^(n-1) approximates a^(-1). Products and closure supply inverses of products and limits. This gives an inverse in the closure; it does not assign a zero-cost or negative-duration physical pulse.

Its Lie algebra projects onto su(d), because the projected tangent generators contain the drift and, by differences, both port axes; the selected lambda makes their Lie closure full. Let I consist of the first coordinates with zero second coordinate. Differences of tangent generators give nonzero iX_p,iY_p in I. For any S in su(d), lift S to an element(S,z) of the group's Lie algebra. Then [(S,z),(Q,0)]=([S,Q],0), so I is an ideal of su(d). Simplicity gives I=su(d), hence the group contains SU(d) times identity. Multiplying a drift pair by the inverse of its first component inside that subgroup gives (I,e^(-itHbar)); closure yields identity times T_H. The product-group conclusion (7) follows.

This remains valid when Hbar=0, when its frequencies are rationally related, or when its recurrence closure has higher torus dimension. The algorithm does not need the torus dimension or an exact recurrence period. The torus coordinate is mathematical elapsed-time bookkeeping, not a physical auxiliary whose state was omitted.

Rational positive durations are dense in real positive durations, so the rational finite-word semigroup has the same closure. Given a computable target W and its stated determinant lift theta with Wtilde=e^(-itheta)W in SU(d), density supplies a word satisfying the two strict epsilon_c/4 tests. Dovetailing computable matrix-exponential/error estimates semidecides these open inequalities and terminates on some successful word. One can make the numerical certificate explicit by approximating finite matrix exponentials through their Taylor series with a certified norm remainder and bounding the final error in Frobenius norm. This is conservative for operator norm but still has a strict witness by density. Thus no exact equality test or unproved computability of recurrence time is needed.

The returned T is the sum of actual rational segment durations. The inequalities imply

\[
\|U_{\rm pc}(T)-\widetilde W e^{-iT\bar H}\|
\le\|U_{\rm pc}(T)-\widetilde W\|
 +\|I-e^{-iT\bar H}\|<\epsilon_c/2.
\]

The scalar h0=Tr(H)/d need not recur. Determinant lifts from chosen finite-circuit logarithms are valid additional data; an arbitrary computable target is not silently treated as a pre-supplied phase-normalized SU(d) matrix. All finite searches may have enormous runtime, memory, duration, word length and precision demands. No actual T,N or practical efficiency is certified by this source or review.

## 6. Smoothing, scalar phase and the finite window

For each active segment, two cubic ramps of length rho_l each have total envelope area rho_l, while the middle has area t_l-2rho_l. Thus total area is t_l-rho_l and the lost area is exactly rho_l. The traceless Hamiltonian changes by an integrated norm g rho_l. Choosing positive rational rho_l<t_l/3 with g sum rho_l<epsilon_c/2 is effective with supplied computable positive g and epsilon_c. No duration is appended: every segment retains its start/end and the full duration remains exactly T. Endpoint values and derivatives vanish, so the concatenated controls are C^1.

The factor g, rather than2g, in this smoothing comparison is correct because it compares the traceless dynamics. The physical positive pulse is g f(I+sigma P), with norm2g f and its own actual scalar area A_s=g sum_active(t_l-rho_l). That scalar is restored explicitly rather than compared to the discarded constant-pulse scalar. This prevents an unpriced phase error while retaining the sharper traceless estimate.

The physical propagator at T is

\[
e^{-i[(h_0+r+\lambda j_0)T+A_s]}U_c(T),
\quad j_0=(L-1)/2.
\]

Using Wtilde=e^(-itheta)W and H=h0I+Hbar gives exactly the candidate phase

\[
\chi(T)=(r+\lambda j_0)T+A_s+\theta.
\]

No uncontrolled U(d) central-phase claim is required. During the window the exact added scalar accumulates another(r+lambda j0)s. Full-space Duhamel compares e^(-is(H+lambda Jbar)) with e^(-isH) at cost lambda||Jbar||s<=lambda b_J w. Consequently (13)–(14) hold. The weak path has been included exactly during the entire compiled interval; the proof does not require lambda T to be small. The full H aging stays on its specified side of W. It is not obtained by commuting H through the actual pulses.

Every zero-drive wait contributes to T, to static action and to scalar phase. The persistent path also contributes throughout the declared window. The two-qubit example e^(-is lambda(I-SWAP))|01>, with density displacement2|sin(lambda s)|, correctly shows why an endpoint claim would not by itself give an unlimited frozen window. Here the promised window follows the target's actual H evolution and has finite supplied length w.

## 7. Full inputs, reset consequence and enlarged geometry

For operator error eta the complete channel comparison, tensor arbitrary passive I_R, obeys

\[
\|U\rho U^*-V\rho V^*\|_1\le2\|U-V\|
\le2\eta,
\]

for every joint density, by expanding the two products and using the operator/trace norm inequality. The distance is also at most2. This proves (15) with no hidden dimension factor or clean-filler premise. Fillers may entangle during compilation. The target is the specified W_old and H on the old inventory tensor identity on fillers, so filler marginal states are unchanged in the ideal output, while their joint correlations undergo the prescribed old-system transformation. No additional filler output is discarded or treated as independent.

For a pure-memory reset, H must act trivially on independently supplied E up to an irrelevant explicitly retained scalar, or an adequate aged-state premise must separately be proved. Then e^(-iTH) leaves E pure and independent, and SWAP_SE transfers every S record and its correlations into E before U_psi prepares S. This gives (15a), with all Z,F,E,R factors retained. The factor-identification symbol in that ideal formula is not a physical coordinate move or conjugation of original H0. The arbitrary normalized computable target vector can be completed to a unitary by the stated dovetailed positive-Gram-minor search and certified Gram–Schmidt; at an incomplete span at least one standard basis vector increases the rank. The determinant lift remains part of the target data.

A biased-memory compressor consequence must apply to the exact aged input e^(-iTH)rho e^(iTH), not automatically to its initial state. When H has memory couplings, the long returned T can spoil a pre-existing diagonal/purity premise. The candidate explicitly preserves this obligation. A compiler of a supplied W does not produce the required memory, and cannot erase arbitrary maximally mixed records by unitarity. The window target evolves the reset output by H; it does not promise that the reset state is stationary.

For nonempty V_old, the integer box with one margin layer encloses all fixed original sites and has a fresh corner port. Alternating the x direction between successive y rows gives a NN Hamiltonian path through each plane. Reversing that entire two-dimensional list on alternate z planes joins the same(x,y) endpoint across consecutive planes. Thus every step is NN, no site is repeated, and there are L-1 path edges. Every added factor is retained with arbitrary input. No old coordinate is moved.

Each path bond I-SWAP is positive with norm2. Its Pauli expansion and normalized trace are exactly the ones in (3)–(4). Triangle inequality gives ||J||<=2(L-1) and ||Jbar||<=3(L-1)/2; these are safe bounds. A path adds degree at most2 at each site. A saturated old vertex uses already occupied neighbors and newly supplied interactions on existing geometric edges, not a seventh neighbor or an assumed pure mediator. Original H and the path may overlap in support; their coefficients add on that support.

The box's total NN edge count is exactly the sum of the three directional counts in the source. The omitted-edge set is all such edges minus the union of original supports and path edges, including new–old and new–new adjacencies created by filling the whole box. A finite full-space sum of their residual norms can bound their total defect. The previous sparse mediator adjacency inventory cannot be substituted. Unknown exterior occupied factors or couplings need a compatible explicit enlarged model or full-output perturbation bound; the box is not evidence of native boundary isolation.

The corner has three geometric neighbors outside the box, but a future autonomous controller's complete incidence and state constraints are not proved by that fact. No old accessible-pair gadget theorem is imported as a ready realization of (18).

## 8. Positivity, all static costs and the corrected work contract

With D(t) a compatible whole-space actual-minus-nominal defect and zeta(t)>=||D(t)||, Duhamel adds E_cal=int_0^(T+w)zeta to the uniform operator estimate and2E_cal to the trace estimate. Scalars are included. For every shorter time prefix the integral is no larger, so one bound serves the complete finite window. For T+w>0 a constant allowance zeta<=epsilon_cal/(T+w) is sufficient. Large compilation time therefore consumes calibration precision; no fixed precision or hardware-cap conclusion is available.

A certified finite peak zeta_pk and r>=h+zeta_pk imply

\[
H+rI+D(t)\ge(r-h-\zeta_{\rm pk})I\ge0,
\]

and adding positive lambda J and C(t) preserves whole-generator positivity. An integrated defect bound by itself does not give that peak certificate. This proof does not make each separately specified original term positive. For example, if X_a and Z_a are distinct literal channels of H=X_a+Z_a, a whole-H bound h=sqrt(2) and reserve r=sqrt(2) certify the total operator, but do not supply nonnegative individual X_a and Z_a blocks with that same independent-channel allocation. A stricter positive-block consumer must state its decomposition and allocate sufficient certified local scalar reserves, then retain their phase/action and actual fault contract. No such stronger decomposition follows from h>=||H|| alone. The source theorem can remain at its declared whole-generator level.

The static path has four literal Pauli coefficients per bond, each of magnitude lambda/2, and whole-block norm2lambda. Added incident path-block norm load is at most4lambda. The global reserve, every path bond and the old background remain installed during all waits and the entire window. The source's peak and action allowances therefore follow by triangle inequality, and its control action is exactly2g sum_active(t_l-rho_l). These costs do not include manufacture or installation; the network and reserve are supplied already present at t=0.

Since max q'=3/2, each ramp has ||dot C||<=3g/rho_l. A complete up/down pulse has variation4g; the nonoverlapping total is4g N_a. The claimed shift bound follows from the L1 translation inequality for a bounded-variation operator-valued function extended by zero, so the zero endpoint condition is relevant. A changed readout time requires the complete background aging and phase to change or an explicit full-generator duration-error allowance. Without active segments, action/variation/slew vanish as stated.

For nominal regular closed dynamics and B=H+rI+lambda J, C(0)=C(T)=0 gives the exact endpoint identity

\[
W_{\rm nom}=\int_0^T\operatorname{Tr}(\rho\dot C)dt
=\operatorname{Tr}[B(\rho_{\rm nom}(T)-\rho_0)].
\]

Hence |W_nom|<=4gN_a. Also the H energy difference is at most2h and the positive J energy range is at most2(L-1), yielding |W_nom|<=2h+2lambda(L-1). The scalar r cancels from the endpoint difference, though its action and coherent phase remain. The lambda Delta<J> contribution is present; an endpoint target need not be a J eigenstate. There is no missing dot J work because this network never switches within the stated experiment.

**Required correction to the fault-work sentence.** Suppose actual dynamics start at the same rho_0 and have generator B+C(t)+D(t), with regularity sufficient for the formal work identity. Then

\[
W_{\rm act}-W_{\rm nom}
=\operatorname{Tr}[B(\rho_{\rm act}(T)-\rho_{\rm nom}(T))]
 +\operatorname{Tr}[D(T)\rho_{\rm act}(T)]
 -\operatorname{Tr}[D(0)\rho_0].
\]

The scalar part of B drops out of the first term. Since0<=J<=2(L-1)I, subtracting(r+lambda(L-1))I from B gives norm at most h+lambda(L-1). Consequently

\[
|W_{\rm act}-W_{\rm nom}|
\le [h+\lambda(L-1)]\|\rho_{\rm act}(T)-\rho_{\rm nom}(T)\|_1
 +\|D(T)\|+\|D(0)\|
\le [h+\lambda(L-1)]\min\{2,2E_{\rm cal}\}
 +\|D(T)\|+\|D(0)\|.
\]

Thus endpoint-defect bounds, including the supplied peak bound when applicable, suffice for this work comparison. No uniform derivative bound is necessary. Derivative or total-variation bounds remain a sufficient alternative if one estimates the work integral termwise, or if a more detailed control-work contract requires them. The source's assertion that calibrated work would require derivatives should be replaced by this endpoint-or-variation distinction.

Two analytic witnesses keep the scope exact. D(t)=a sin(Omega t)I with Omega T an integer multiple of2pi has zero endpoint defect, zero net scalar work and zero net scalar area for any arbitrarily large frequency; its derivative can be arbitrarily large. Conversely a smooth positive scalar defect that rises from0 to M only in a terminal interval of length M^(-2) has integral norm at most1/M but endpoint work M. Hence an integrated defect allowance alone, with no endpoint control, cannot bound the work. Both examples are finite regular scalar Hamiltonians; no numerical fixture is needed. The second may require a larger explicitly paid peak reserve if used in a robust positivity contract.

The formal work convention does not supply a native physical energy bridge, actuator, bath or Landauer statement. The external waveform remains a supplied classical control, with no modeled quantum controller output.

## 9. Bounded conclusion, evidence and open interface

With the corrected Pauli step, endpoint-or-variation work qualification, explicit nonempty domain and whole-generator positivity scope, the endpoint/window theorem is supported. All pure/reset and biased-memory consequences retain their separate aged-state hypotheses. The theorem gives no uniform resource efficiency, common calibration cap, computed pulse instance, unchanged intermediate H_aut trajectory or native control/purity supplier.

The explicit remaining interface (18) asks for a finite prepared controller, time-independent NN two-qubit generator, retained controller path and phases, and a uniform full-plant operator comparison over the same actual time interval. None of the group coordinates, proof recurrences, external schedules or arbitrary fillers supplies that physical controller. Earlier mediator sources have different literal geometry and state requirements. This review does not close (18), import it as a primitive or assert a general impossibility theorem against other routes.

SOURCE_MANIFEST and READ_EXPOSURE record exact selected snapshots and actual reading limits. Metadata verification checks the34 original frozen members and the selected source/current instruction identities. It does not recursively validate all historical freezes named by the author's recovery files. All current review files, nested selected source receipts and actual launch/stream/exit records are included by full path in FINAL_FREEZE. The original author files remain unchanged. Historical author metadata are preserved as actual in-process records, not upgraded into missing subprocess stdout/stderr or a scientific run. Earlier uncaptured web reading remains uncaptured.

No scientific diagnostic was necessary to resolve the substantive risks: the Pauli, group, exponential, smoothing, geometry and work calculations above are analytic. The only new executed helpers perform source capture, syntax/identity verification and sealing; their actual UTC times, source-at-launch, stdout, stderr, failures and exit codes are recorded. No W/Git/PR/audit/checkpoint/lock/prompt/axiom edit, model override, new agent or other-worker consultation occurred. Source reading and metadata checks do not themselves establish an audit disposition.


---

## Immutable source body: controller_author

Historical source retained exactly; the current wrapper and separate root decisions govern interpretation.

# One accessible port with a prepared autonomous NN controller

Status: root-proposed conditional theorem, requiring a separate decisive check. This source is not an acceptance or retained audit. It composes a supplied finite external-port schedule with the accepted finite unary-clock estimate and proves a new one-component two-quadrature mediator realization. The prepared coherent controller and vacuum auxiliaries remain supplied. It does not derive those states, thermalization, physical energy identification, a detector, or a reusable controller.

## 1. Exact interface and source roles

Let P be a finite qubit plant filling a rectangular cubic-lattice box whose minimum corner is p. Translate coordinates so p=(0,0,0) and all plant sites have nonnegative coordinates. No old factor is moved by this coordinate notation. The supplied fixed finite ordinary-NN/onsite generator H_P contains the literal old H0 at its original strength. It may include a weak fixed path, its physical scalar reserve and every other already declared installed term. Assume H_P>=0 and a computable full-space bound h_P>=||H_P||. The construction works for a general signed background after an additional actual positive reserve, but that variant must carry its phase and cost. Here the positive H_P case suffices for the single-port candidate.

Every plant input and passive reference R is arbitrary. In particular the filled-box auxiliaries in the single-port compiler remain arbitrary retained plant factors, not new clean controller factors. Supply one finite computable C1 waveform C(t), supported at p, with C(t)=0 outside [0,T], C and its derivative zero at the endpoints, and

    C(t)=g f(t)(I+sigma P_p),
    P_p in {X_p,Y_p}, sigma in {+1,-1}, 0<=f<=1,

with at most one nonzero pulse at a time. A finite piecewise-cubic description such as the single-port source provides all integrals and bounds. More generally it suffices to supply the needed effective uniform approximation and variation certificates. Let U_C(t) be the chronological propagator of H_P+C(t), and select a finite rational horizon tau>T+w, w>=0. Let c=2g, V_C>=Var(C) and L_C>=sup||dot C|| be supplied finite computable bounds. For the previously constructed smooth schedule, V_C=4g N_a and L_C=3g/rho_min suffice; if no pulse is active, both are zero.

The new aim is a static ordinary-NN two-qubit Hamiltonian on P plus a fresh finite clock X and fresh mediators A, with an explicit prepared isometry J_in, such that for all 0<=t<=tau

    exp(-it K_phys) J_in
      ~= exp(-it R_pos) [I_A-vac tensor phi_a(t) tensor U_C(t)].       (1)

All factors are retained, time is the same physical t, phi_a(t) is the actual free finite clock state, and R_pos is an installed scalar, not a dropped phase. The operator norm is over the entire plant, hence includes arbitrary references. The notation I_A-vac means appending the auxiliary vacuum, not tracing it out.

Two existing sources are used with their hypotheses:

* The source b726766403bf6f4b0080172d046cf773facad028eed538d7473417683b931bb7, sections4 and6-8, restates the accepted arbitrary-background finite unary-cycle estimate from c7a19c3acb7d731a95b97bfadc8a32e2624196d60555ac08e8e77b3ad71d1135. Its Fourier guard, two Dyson tails, sine dispersion and actual free-clock phase remain required. Only this analytic scheduling theorem is imported, not its old memory/routing geometry or preparation-state claims.
* The root-exposed new single-port program source bda0be884fa79905ff81f0a2642def9e2efd5302796262f5f9eb4033b2c436c0 supplies one optional external schedule and an endpoint/window target. Its separate checking is pending as this source is written. The present scheduling implication does not assume its controllability proof: C(t) can instead be any independently supplied waveform satisfying the explicit contract above.

The older d4ed04f7 single-port pair mediator is technique/context. Its full auxiliary inverse, second corrector and scalar discipline motivate the calculation here, but its Pe-dependent inverse and fixed pair geometry are not applied. The new two-quadrature contraction and actual geometry are proved below.

## 2. Positive finite step approximation and the exact clock import

To use precisely the already checked finite step-waveform clock estimate, divide [0,T] into K equal cells of width d=T/K and let C_0(t)=C(ld) on cell l, zero afterward and before zero. Every sample is positive, supported at p and has norm<=c. An effective integer K can be selected so that

    integral_0^tau ||C_0-C|| dt <= L_C T^2/(2K) <= eta_step.          (2)

The proof integrates L_C(t-ld) on each cell. If L_C=0, the zero-endpoint waveform is zero; any K works. One can simply choose a certified integer larger than 1+L_C T^2/(2 eta_step), avoiding an equality oracle. Discrete variation including the final return to zero is at most Var(C), because the sample sequence plus the true endpoint is a partition of the original path. Thus V_0:=V_C is a valid step-waveform variation bound. Duhamel gives ||U_0(t)-U_C(t)||<=eta_step uniformly to tau, where U_0 uses H_P+C_0. No physical switching process is executed here: C_0 is encoded statically below.

Take S_c=4tau, omega=2pi/S_c, and extend C_0 periodically with zero on [T,S_c). Use the positive Fejer kernel of order R_f and define

    V_R(x)=integral_circle F_R(y) C_0(x-y)dy,
    F_R(y)=|sum_(l=0)^R_f exp(il omega y)|^2/[S_c(R_f+1)].           (3)

Then V_R is positive and ||V_R||<=c. All its finite Fourier coefficients follow by integrating each constant interval: the q=0 coefficient is the duration-weighted average, and each nonzero |q|<=R_f coefficient has the Fejer weight (1-|q|/(R_f+1)) times

    sum_l [exp(-iq omega a_l)-exp(-iq omega b_l)] C_0(a_l)
          /(iq omega S_c).

These coefficients are computable from the supplied finite description. Since only I,X,Y occur at p, write exactly

    V_R(x_j)=a_j I+b_j X_p+c_j Y_p,
    0<=a_j<=g, sqrt(b_j^2+c_j^2)<=a_j, x_j=j a_c.                 (4)

There is no Z term. The scalar samples a_j are physical clock onsite terms in the next Hamiltonian; they are not discarded as plant-global phases.

Choose 0<eta_clk<=1 and the same explicit conservative integers as the accepted clock theorem:

    Z=V_0 S_c/eta_clk,
    R_f=k>=max(1,2Z^2),
    n_D>=max(2,6c tau,log_2(32/eta_clk)), r_D=n_D-1,
    B_mom=k+R_f r_D,
    M>=2B_mom+R_f+1,
    M^2>=[2tau S_c^2 omega^3/(3eta_clk)](B_mom^3+k^3),

rounding M upward to a multiple of four and choosing strict certified larger integers where needed. Let a_c=S_c/M. On M physical clock qubits around a square ring set

    K_X=sum_j [n_j+n_(j+1)
       +i(sigma_(j+1)^+ sigma_j^- -sigma_j^+ sigma_(j+1)^-)]/(2a_c),
    H_aut=H_P+K_X+sum_j n_j(a_j I+b_j X_p+c_j Y_p).                (5)

Here sigma^+=|1><0| and Y|0>=i|1>. Each clock bond is positive with norm1/a_c. H_aut is positive on the full space because every sampled program block is positive. It preserves N_X. The full bound ||K_X||<=M/a_c is retained for physical prices; no one-excitation norm is substituted there.

Let |ell> be the Fourier one-excitation states with amplitudes exp(2pi i ell j/M), and supply

    chi_k=(2k+1)^(-1/2) sum_(ell=-k)^k |ell>,
    phi_a(t)=exp(-it K_X)chi_k.                                  (6)

The accepted prepared-clock estimate on the entire plant is

    || exp(-it H_aut)(chi_k tensor I_P)
          -phi_a(t) tensor U_0(t) || <= eta_clk, 0<=t<=tau.       (7)

In detail its four terms are d_R+d_k+4E_(r_D)(tau)+tau(delta_B+delta_k), with d_R=V_0 S_c/sqrt[8(R_f+1)], d_k=V_0 S_c/sqrt[8(2k+1)], E_r(t)=sum_(j>=r+1)(ct)^j/j!, and delta_m=a_c^2(omega m)^3/6. The strict alias guard and actual phase1/a_c are part of (7). The theorem applies to arbitrary finite H_P without commuting it through V_R. Equations(2) and(7) already prove a nonlocal prepared-controller statement with error eta_clk+eta_step. The next sections supply the ordinary-NN realization that statement lacks.

## 3. One-component physical geometry outside the fixed plant

Fix an integer d0>=2. Put the M=4q_c clock sites on the square perimeter at z=-3 with lower-left corner (d0,d0,-3) and side q_c. Each corner is counted once in a consistent orientation. Put a transport copy of the same cycle at z=-2; its vertex u_j is the vertical NN neighbor of clock site j. Append a tail from the new port-adjacent auxiliary a=(-1,0,0) through

    (-1,0,-2), (d0,0,-2), (d0,d0,-2).                           (8)

Each segment includes its integer steps. The last point is the transport-cycle lower-left corner. The tail length is ell_tail=2d0+3; it meets the transport cycle only at its endpoint. The auxiliary graph B has

    m=M+2d0+3 vertices, E_A=M+2d0+3 edges,
    maximum internal degree3.                                 (9)

It is a connected unicyclic graph; a is a tail endpoint, distinct from every u_j. All its sites and all clock sites are disjoint from the nonnegative-coordinate plant box: the port a has x<0, and all other new sites have z<0 or x<0. The clock and transport cycles are at different z. The tail lies at y=0 below the transport square's y>=d0, except for its final vertical-in-y segment x=d0, which enters the cycle once. The vertical part at x=-1 is outside both cycles and the plant.

The added interactions are M clock bonds, E_A auxiliary graph bonds, M clock-to-u_j source edges, and the single p-to-a edge. Thus the declared new geometric edge count is

    M+E_A+M+1=3M+2d0+4.                                      (10)

Several Pauli coefficients can live on one such edge. They do not require extra neighbors. At p exactly one formerly exterior neighbor is used, whatever original internal incidences were saturated. At each clock vertex there are two clock neighbors and one source neighbor. At an auxiliary cycle root there are three internal neighbors plus its clock source, and at a one internal neighbor plus p. All declared degrees are <=4, within cubic degree6.

The full new factor count is M+m=2M+2d0+3, in addition to the complete retained plant. Possible unlisted geometric NN edges, including near the tail and plant boundary, are absent nominally or priced over the whole horizon. A safe incidence bound is 6(|P|+M+m). A tighter count can be obtained by enumerating the explicit finite coordinates; no isolation follows from calling a site fresh. An occupied environment outside this inventory must be included or separately modeled. The construction does not assume clean old sites, an extra seventh neighbor, displaced H0, or a universal infinite vacuum.

## 4. Full auxiliary gap and positive inverse transport

Let A_B be the real adjacency matrix of the graph above, and define the exact rational matrix

    B=I-A_B/12, tau_B=B^(-1).

Because maximum degree is3, ||A_B||<=3 and B>=3I/4. Its inverse is the convergent nonnegative Neumann series sum_(r>=0)(A_B/12)^r. Connectivity gives strictly positive tau_B(a,u_j), with the explicit lower bound 12^(-dist(a,u_j)) from one shortest walk. Also ||tau_B||<=4/3. These are finite, certified denominators; no zero test on an unknown inverse entry occurs.

On the full auxiliary qubit space install

    L=sum_v n_v -(1/12)sum_{uv in E_A}
                         (sigma_u^+sigma_v^-+sigma_v^+sigma_u^-). (11)

Its one-excitation matrix is B. The full-space inequality is L>=g0 N_A with g0=3/4: either factor B-g0I as R*R and sum the corresponding lowering-operator squares, or write explicitly

    L=sum_v(1-deg(v)/12)n_v
      +(1/12)sum_uv [n_u+n_v
                    -(sigma_u^+sigma_v^-+sigma_v^+sigma_u^-)].

Every displayed onsite/edge block is positive. The bracket has pair eigenvalues0,0,2,2, so this also gives an ordinary-NN positive-block implementation. The vacuum is its unique zero state. Let J0 append that vacuum, P0=J0J0*, Q0=I-P0 and R_A=Q0(L|Q0)^(-1)Q0. Then ||R_A||<=1/g0 on all auxiliary sectors. A safe full norm is ell_L=m+E_A/12; the exact normalized Pauli scalar is m/2. No many-particle free-fermion assumption is used.

## 5. Two onsite axes through one physical source edge

Choose q>0, and write t_j=tau_B(a,u_j)>0, gamma_j=tau_B(u_j,u_j), gamma_a=tau_B(a,a). Set

    z_j=-(b_j+i c_j)/(2q t_j),
    V=q(X_p X_a+Y_p Y_a)
         +sum_j n_j[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)].             (12)

These are all Hermitian onsite/ordinary-NN two-qubit operators on the declared edges. The two port quadratures XX and YY share the one p-a edge. Each clock source uses two coefficients on one clock-u_j edge. Their combined norm is |z_j|. The port block has norm2q. A full bound is

    v=2q+sum_j|z_j| >= ||V||.                                 (13)

The convention Y|0>=i|1> means that V creates auxiliary a with plant operator q(X_p+iY_p), and creates u_j with plant/clock operator z_j n_j. Crucially,

    (X-iY)(X+iY)=2(I-Z)=4n_p.                                 (14)

It is not a scalar source-square. At second order, on the entire N_X=1 clock domain,

    J0* V R_A V J0 = C0-W,
    W=sum_j n_j(b_j X_p+c_j Y_p),
    C0=4q^2 gamma_a n_p+sum_j |z_j|^2 gamma_j n_j.               (15)

Proof: the a-a contraction is4q² gamma_a n_p. The u_j-u_k contraction is z_j* z_k tau_B(u_j,u_k)n_jn_k. On N_X=1 the off-diagonal j!=k terms vanish, leaving the second term in C0. The a-u_j plus conjugate contraction is

    q t_j n_j[(X-iY)z_j+z_j*(X+iY)]
      =2q t_j n_j[Re(z_j)X+Im(z_j)Y]
      =-n_j(b_jX+c_jY).

This proves (15), including both signs and the nonscalar onsite counterterm. On general multi-excitation clock states the off-diagonal n_jn_k terms remain; no full-clock contraction identity is claimed. All nominal generators preserve N_X, while implementation leakage is charged by a full-space perturbation bound.

C0 is positive and is actually installed. In particular its p occupation field changes the added control apparatus; it is not erased as a gauge, a modification of H0, or an uncharged compensation. The original background remains literally present.

Since |b_j+i c_j|<=g and dist(a,u_j)<=D_*=2d0+3+M/2, one optional explicit allowance is |z_j|<=Z_*=g 12^(D_*)/(2q). Then v<=2q+M Z_* and ||C0||<=c0_*=(16/3)q²+(4/3)M Z_*². These bounds may be enormous. They certify finite effective choices, not efficiency or common hardware caps.

## 6. Same-time bare prepared-map realization

Define the full retained clock/plant background

    H_b=H_P+K_X+sum_j a_j n_j,
    A=H_b+C0,
    K_Delta=Delta L+sqrt(Delta)V+A, Delta>0.                    (16)

H_b and C0 are positive. On N_X=1, the target is H_tar=H_b+W=H_aut. They preserve this domain and act on no auxiliary factor. Restrict J0 to that clock domain and call it J. Define

    X1=R_A V J, Y2=R_A V X1,
    Z=J-epsilon X1+epsilon²Y2, epsilon=Delta^(-1/2).

X1 has one auxiliary excitation. V X1 has vacuum and two-excitation components; R_A removes the vacuum, so Y2 has two excitations. Thus J*VY2=0, and direct expansion using (15) gives

    K_Delta Z-Z H_tar
     =epsilon[X1 H_tar-A X1+VY2]
       +epsilon²[A Y2-Y2 H_tar].                              (17)

No commutator of H_P, K_X, n_p, C0 or W is dropped. Z is a comparison corrector, not a physically prepared dressed input. Two endpoint differences between Z and J and unitary Duhamel give

    sup_(0<=t<=tau)||exp(-itK_Delta)J-Jexp(-itH_aut)||
       <=F1/sqrt(Delta)+F2/Delta=:eta_med,                     (18)

where, for any full-space bounds a>=||A|| and b>=||H_aut||,

    x=v/g0, y=v²/g0²,
    F1=2x+tau[(a+b)x+v y],
    F2=2y+tau(a+b)y.

Safe choices are h_b=h_P+M/a_c+sum_j a_j, c0=4q² gamma_a+sum_j|z_j|² gamma_j,

    a=h_b+c0,
    b=h_b+sum_j(|b_j|+|c_j|).

The last b is conservative; the positivity of each original sampled V_R also gives other bounds. Full-space allowances are deliberately kept when pricing physical leakage and calibration. Choosing Delta>=max(1,(2F1/eta_goal)^2,2F2/eta_goal) ensures eta_med<=eta_goal. All selected matrices/inverses and strict denominator bounds are computable from finite data.

The actual constant reserve R_pos=sqrt(Delta)v makes K_phys=K_Delta+R_pos I positive on every plant/clock/auxiliary sector. This follows already from A,L>=0 and V>=-vI. It can also be distributed literally: add2qI to the port XX+YY block and |z_j|I to each clock-source block, multiplied by sqrt(Delta), each a positive local edge block. Their total identity coefficient is exactly R_pos. Thus the reserve has both a full-generator and an explicit positive-block interpretation. Every reserve contribution is physically retained and priced.

Equations(2),(7),(18) now give the promised same-time autonomous comparison (1) with operator error

    eta_tot=eta_med+eta_clk+eta_step, uniformly0<=t<=tau.        (19)

J_in appends chi_k on X and vacuum on all m auxiliaries. No other new input is hidden. Arbitrary plant/reference inputs follow by tensoring identity_R; the full density output error is at most min(2,2eta_tot). Every controller factor remains in the comparison. The original filled-box arbitrary fillers remain part of U_C's plant, while the newly supplied mediator vacuum is a separately declared resource.

## 7. Composition with the single-port endpoint/window contract

This section is conditional on the separate acceptance of source bda0be88. If its returned C(t), T and weak-path H_P=H+rI+lambda J satisfy

    ||U_C(T+s)-exp[-i chi(T+s)] exp(-isH) W exp(-iTH)||
       <=epsilon_c+epsilon_w, 0<=s<=w,

then (19) gives the complete static autonomous prepared map with error at most

    eta_med+eta_clk+eta_step+epsilon_c+epsilon_w,

and target

    exp[-i(R_pos(T+s)+chi(T+s))]
      [vac_A tensor phi_a(T+s) tensor exp(-isH)Wexp(-iTH)].     (20)

This retains all plant records/fillers/references and the new free comparison clock/vacuum auxiliaries. It is an evolved output window, not an automatically frozen ready state. Reset consequences still require the exact consumed-memory premise at the actually aged input. No changed elapsed time, hidden recurrence refund or pure-memory regeneration is inferred. The old H0 is unchanged in every actual Hamiltonian.

The new controller supplies the physical support missing from the previously nonlocal sampled drive for this single-port waveform. It does not claim ordinary-NN implementation of every original distributed clock/data program directly. The single-port compilation changes that program contract explicitly before this controller construction is applied. This dependence must remain visible in any future publication.

## 8. Complete physical costs, moments and faults

K_phys is static. Its complete norm allowance is

    B_full=h_b+c0+Delta ell_L+sqrt(Delta)v+R_pos.

Its exact normalized full Pauli scalar is

    s(H_P)+M/(2a_c)+(1/2)sum_j a_j
       +Delta m/2+2q² gamma_a+(1/2)sum_j|z_j|² gamma_j+R_pos.   (21)

The clock free phase, the sampled plant-global terms a_j, the p occupation counterterm, transport diagonal and positive reserve are all present. The terms in V are traceless on the full plant/clock/auxiliary space. Raw moment and physical energy statements use (21), not a recentered surrogate. A density bound can forget a global phase only after its operator and scalar ledgers have been written.

On an admitted initial plant/clock density rho with N_X=1 and fresh auxiliary vacuum, define p_j=Tr(rho n_j). Orthogonality of distinct auxiliary flips gives exactly

    mean(K_phys)=Tr(rho A)+R_pos,
    Var(K_phys)=Var_rho(A)
       +Delta[4q² Tr(rho n_p)+sum_j|z_j|² p_j].               (22)

Every clock/plant covariance is retained inside Var(A). No product assumption beyond the actual prepared clock used for (19) is needed for this identity. No covariance cancellation from an unrelated polynomial program is borrowed. The nonzero p source-square is the same term required in (14)-(15). Mean and variance of the full static Hamiltonian are conserved, but pieces can exchange energy. Approximate return of vacuum does not refund the penalty: an auxiliary leakage probability bounded by eta_med² only gives a penalty-energy allowance Delta ell_L eta_med², not vanishing energy or reuse. No external pulse-work integral describes this static model; installation and initial state preparation are supplied operations.

Literal new channels include: M positive clock bonds; m auxiliary onsite occupations and E_A real hopping edges with coefficients1 and-1/12 before Delta; two port coefficients sqrt(Delta)q on XX and YY; two clock-source quadratures per j; the positive p counterterm4q² gamma_a; M nonnegative clock counterterms |z_j|² gamma_j; M scalar-drive clock onsite terms a_j; and the actual reserve. If channels are expanded into Pauli occurrences, n_j(Re z X+Im zY) contributes both onsite-auxiliary and clock-Z/auxiliary products, each half the displayed quadrature, and an n occupation includes its identity. Do not price a combined block and each expansion as independent physical strengths twice. The primitive full block-norm envelope and the literal chosen Pauli decomposition are separate conventions.

Per new auxiliary site, a safe installed penalty load is Delta[1+deg(v)/12], with its appropriate source contribution. At p add2sqrt(Delta)q+4q² gamma_a, in addition to its original H_P load and any assigned scalar. At clock j add its two clock-bond loads2/a_c, source sqrt(Delta)|z_j|, onsite a_j+|z_j|² gamma_j. Combined two-quadrature source pricing can be replaced by |Re z|+|Im z| when those coefficients have separate errors. Every clock and auxiliary position is fixed before computing Delta. No common cap, polynomial size, useful compilation time or laboratory implementation is claimed.

Let the actual full initial state differ from the stated prepared product/plant state by trace error eta_init, and let the actual generator be K_phys+E(t), including all omitted edges, old-background changes, scalar, quadrature, counterterm and clock-number-leakage errors. Then add

    eta_init+2 integral_0^tau ||E(t)||dt

to the full density bound. A bound only inside N_X=1 is insufficient for leakage. Positivity of the faulty implementation needs a separate peak reserve or a positive-block implementation certificate, not just integrated error. At a fixed nominal observation time, a full-space bound B_full gives additional trace error2B_full|delta t|, with implementation integration over the actual elapsed interval; a time-indexed target may instead use its actual t. A detector interaction is a further explicit Hamiltonian, not implied by an unperturbed window.

## 9. Boundaries and decisive checks still required

The main new algebraic risks to check are the complex-source sign, the nonscalar4q² gamma_a n_p source-square, the restriction eliminating n_jn_k only on N_X=1, the two-excitation corrector, and the one physical port's explicit exterior geometry. The two source quadratures are real physical coefficients, not additional vacant sites. All old/filler/reference inputs remain arbitrary. The new product clock and auxiliary vacuum do not arise from positivity or a generic realized-state reference.

Failed shortcuts are explicit: using only XX at the port would only furnish one fixed plant axis with real sources; treating q(X+iY) as a unitary would erase its n_p square; deleting a_j would change clock-relative phases; dropping multi-clock cross terms on the full space would overstate the admitted domain; replacing the bare map by a dressed input would require preparation not supplied; and a prepared-map norm estimate alone would not establish energy return or controller reuse.

This root proposal is original composition/derivation within explicit finite Hamiltonian premises. It does not alter physical axioms or an editable prompt. No matrix evolution, scientific fixture, numerical program, pulse search or formal prover has been run for it. Exact source identities, the complete proof and any eventual independent check must be preserved before publication. The pure controller/vacuum supply, installation, isolation, coefficient access, physical time/energy identification and readout remain unresolved physical obligations.


---

## Immutable source body: controller_assessment

Historical source retained exactly; the current wrapper and separate root decisions govern interpretation.

# Separate analytic check: one supplied port schedule and a prepared autonomous NN controller

Disposition: the unchanged candidate supports its **conditional, finite, same-time schedule-to-controller theorem**. I found no mathematical repair necessary in the stated domain. This disposition covers a supplied waveform satisfying section 1, a supplied independent coherent one-head clock and auxiliary vacuum, the explicitly installed counterterms/reserves, and the full retained plant/controller/reference output. The optional external-compiler composition is separate: its qualified root acceptance arrived late in this review and is recorded below, without treating that acceptance as a check of the new controller.

The checked candidate is `DERIVATION.md`, 24,070 bytes, SHA256 `0e91f9369e387608f8fb3720c290e67f6aa98b10f13428866334c8507b9e989d`; its 704-byte proposal freeze is `f3b497f3db6c64809877be9b8b547e048e673da9203e3a7d40a106d51e166d10`. Exact paths, recovery copies, current byte counts, read coverage and actual metadata receipts accompany this report. Source identities establish what was checked, not that a theorem is true.

## 1. Exposure, scope and evidence limits

This is a source-exposed separate analytic review by the same selected model family/effort. Root authored the candidate. I received its requested risk list and the information that another reviewer had found a Pauli-induction wording correction and an endpoint-defect work refinement in the optional 33,757-byte controllability source. I did not derive this result before seeing the proposal, and this is not a blind, model-diverse, formal-proof or retained-audit check. No other agent was spawned and no scientific program, pulse search, numerical propagation or historical fixture was run in this task.

Late exposure update: after completing the standalone mathematical assessment and drafting this report, root supplied the external compiler's actual acceptance, sealed at 18:33:02 UTC. I then read its complete 4,801-byte `ACCEPTANCE.md`, SHA256 `bbe2e9c911e3323f840855fb2e77cc5e86d1669486eb8c8dda2e8cdec3ff53eb`, and its verification/freeze metadata. Its freeze is `9b7d3b4d1305a80c221ccfe749a5e4921def521260adbf772e07a26a1124c969`. The historical candidate's pending wording stays unchanged. I did not read the separate compiler review `3ad0ab65…` as a new scientific review in this task; the qualified decision is an explicitly attributed dependency disposition.

I read the complete changed candidate, the complete original 33,019-byte unary-clock argument `c7a19c3a…`, the needed sections 4 and 6–8 of its 31,689-byte restatement `b7267664…`, and the actual unary/autonomous-preparation acceptances. For the optional controllability source `bda0be88…`, I read sections 1–2 and 6–9, defining its plant geometry, smooth schedule, phases, endpoint/window contract and physical prices. I did not re-review its Lie/determinant/compact-group proof in sections 3–5. The earlier pair-mediator source `d4ed04f7…` is technique context with prior exact-identity exposure; its geometry and operator-dependent inverse are not imported into this proof. The report does not rely on its acceptance for the new algebra.

The current instructions and review skill were followed at their pinned identities. The current task retained their same-model/no-delegation and source-only boundaries; no audit, publication or checkout operation followed merely from reading a workflow. The current candidate and exact proof sources remain unchanged. Editable prompt files changed: none. Metadata programs here only capture identities, validate source/recovery consistency and seal this report. They do not numerically test its equations. The analytic plan was recorded after source exposure and is expressly not represented as pre-exposure registration.

## 2. Exact supplied contract and what is proved

The plant fills a finite rectangular box, with a corner port `p`, a finite positive fixed onsite/ordinary-NN background `H_P`, and a full-space norm bound `h_P`. Its original terms, including literal `H0`, remain installed. Its entire initial state may be arbitrary and correlated with a passive reference, including all old filled-box factors. The fresh clock and mediator factors are different physical resources: the theorem appends the specified pure `chi_k` and the mediator vacuum independently of that unknown plant/reference state.

The supplied serial waveform is `C(t)=g f(t)(I+sigma P_p)`, where `P_p` is X or Y, `sigma=±1`, `0<=f<=1`, and its finite C1 description or effective approximation/variation certificates are available. It vanishes outside `[0,T]`, with the stated endpoint guards. A finite rational horizon `tau>T+w` is selected. Positivity of the waveform is part of this contract; an arbitrary unbounded, noncomputable or differently supported drive is not included.

For finite choices of the step approximation, clock cutoffs and mediator penalty, the statement is an operator bound from the **entire plant** into the complete enlarged system:

    sup_(0<=t<=tau) ||exp(-it K_phys) J_in
      - exp(-it R_pos)[vac_A tensor phi_a(t) tensor U_C(t)]||
      <= eta_step + eta_clk + eta_med.

The physical clock comparator is its actual free finite-clock evolution. The physical elapsed time is the same `t` in every factor. The target includes all plant outputs, fillers, records and references, and every new clock/auxiliary factor. It is neither a clock-discarded simulation nor a frozen output or returned-resource assertion. The initial resource-supply premise is not established by positivity, the clock theorem or the new NN geometry.

## 3. The step waveform fits the accepted clock theorem without a domain extension

For equal cells of length `d=T/K`, the left-endpoint approximation satisfies, by the supplied Lipschitz bound,

    integral_cell ||C(t)-C(ld)|| dt <= L_C d^2/2,
    integral_0^tau ||C-C_0|| dt <= L_C T^2/(2K).

The same bound controls every partial time integral up to `tau`, so unitary Duhamel gives the uniform propagator error in candidate (2). The final jump of `C_0` to zero belongs in its variation. The sequence `C(0), C(d), ..., C((K-1)d), C(T)=0` is a partition of the continuous path, so its total variation is at most `Var(C)`. The initial zero and the periodic zero segment add no omitted jump. If `L_C=0`, the zero endpoint implies the zero waveform. Strict integer upper choices make the approximation effective without an equality oracle.

Apply the original clock theorem with its runtime parameter equal to **tau**, not to the shorter active-waveform interval T. Its waveform is the finite step function on `[0,T]` followed by zero on `[T,tau]`, with circle length `S_c=4tau`. Adjacent cells are serial intervals up to irrelevant measure-zero endpoints. Every cell is a one-site Hermitian matrix of norm at most `c=2g`. The original theorem explicitly permits an improved finite-variation bound, so replacing `2c` times an interval count by `V_C` is licensed. It accepts any finite noncommuting background `H_P`; no step commutes that background through the program.

I independently checked the constants from the original proof. For the Fejer kernel, its first cosine moment is `R/(R+1)`. On the short arc, `sin(pi|y|/S_c)>=2|y|/S_c`, giving `E_F |y|^2 <= S_c^2/[8(R+1)]` and hence the first-moment bound used for `d_R`. The flat packet has squared density `F_(2k)`, giving `d_k`. The BV shift estimate controls the characteristic propagators even with noncommuting `H_P`, by Duhamel and integration over the whole circle.

The discrete sampled potential is a finite trigonometric polynomial before sampling. On ordinary modes `[-B,B]`, its matrix element contains the discrete sum at frequency `q+l-k`. The strict condition `M>2B+R_f` excludes every nonzero multiple of M. Thus the compression is ordinary Toeplitz compression, rather than a silently wrapped momentum band. Starting in `[-k,k]`, every word through Dyson order `r_D` stays within `B=k+R_f r_D`. There are two separate comparisons—continuum to ordinary band, and ordinary band to actual ring—each costing `2E_(r_D)`, for the stated total `4E_(r_D)`. The free sine and linear dispersions differ by at most `a_c^2(omega m)^3/6` on either required band. The further `delta_k` term changes the linear comparator to the actual free clock; it is not redundant.

Writing `Z=V_C S_c/eta_clk`, the cutoff `R_f=k>=2Z^2` gives `d_R,d_k<=eta_clk/4`. With `n_D>=6c tau`, the factorial/geometric tail bound gives `4E<=2^(3-n_D)`; `n_D>=log2(32/eta_clk)` makes this at most `eta_clk/4`. Finally,

    tau(delta_B+delta_k)
      = tau S_c^2 omega^3(B^3+k^3)/(6M^2) <= eta_clk/4

under the stated M bound. These four allocations establish the imported tolerance. The `1/a_c` one-head clock phase is retained in `phi_a(t)`; it is distinct from the full-space normalized Pauli scalar `M/(2a_c)`. The old theorem's arbitrary-clock-state exclusion remains in force. Its optional state-preparation circuit and old nonlocal geometry are not imported.

The positive Fejer average also verifies the coefficient restrictions used later: the scalar is an average of `g f` and lies in `[0,g]`; the X/Y coefficient vector is an average of vectors of length `g f`, so its length is at most that scalar. Consequently `sqrt(b_j^2+c_j^2)<=a_j`, and every sampled program block is positive. Those scalar samples are real clock occupation fields, not a plant-global phase that can be deleted before the clock comparison.

## 4. Explicit exterior geometry and omitted edges

The coordinate construction is consistent with fixed old coordinates. Translate the coordinate origin to the plant corner; this is notation, not a physical movement. The clock square is at z=-3, its transport copy at z=-2, and the path starts at `a=(-1,0,0)`. Its successive segment lengths are 2, `d0+1` and `d0`, totaling `ell_tail=2d0+3`. The tail endpoint is already one cycle vertex; all other tail vertices are new. Hence

    auxiliary vertices = M + ell_tail,
    auxiliary edges    = M + ell_tail,
    fresh factors      = 2M + ell_tail,
    new declared edges = 3M + ell_tail + 1.

This gives exactly candidate (9)–(10). The auxiliary graph is connected and unicyclic. The path enters the lower-left transport corner from y below the square and does not cross another transport vertex. Its x=-1 vertical segment is outside the plant. All new sites have a negative x or z coordinate. Matching transport/clock vertices differ by one in z, so every source edge is NN. The p–a port edge is the sole new edge incident to the plant.

The auxiliary cycle root has internal degree 3 and, including its clock source, physical declared degree 4. Other clock/transport vertices have degree at most 3; the tail endpoint a has its internal neighbor and p. The plant corner uses one exterior neighbor; no old interaction is moved or an extra seventh neighbor supplied. The square side and integer cutoff conditions give distinct cycle sites and a valid closing NN edge.

All original plant geometric edges remain subject to their declared Hamiltonian inventory. The theorem does not deduce isolation merely from freshness. Its full-space perturbation model must include every undeclared occupied NN pair and any admitted extra environment couplings, over the whole actual horizon. `6(|P|+M+m)` is a conservative incidence allowance, not an exact count or an automatic isolation mechanism. The explicit new coordinates do not hide an interaction with an unspecified infinite environment. Onsite terms and multiple Pauli coefficients on an already declared edge do not require additional neighboring sites.

## 5. All-sector positive gap and inverse-entry bounds

The degree bound gives `||A_B||<=3`, hence `B=I-A_B/12>=3I/4`. Its Neumann series has nonnegative entries. A shortest walk of length d contributes exactly `12^-d` to the relevant inverse entry, so `t_j>=12^-dist(a,u_j)>0` and `||B^-1||<=4/3`. No graph mixing estimate, many-particle fermion spectrum or unproved uniform lower bound is used. The furthest cycle vertex is at graph distance at most `ell_tail+M/2`, establishing the candidate's exponential coefficient allowance.

For the full auxiliary Hilbert space, the explicit positive-block decomposition is stronger than a one-particle assertion. On a pair,

    n_u+n_v-(sigma_u^+sigma_v^-+sigma_v^+sigma_u^-)

has vacuum eigenvalue 0, one-head eigenvalues 0 and 2, and double-occupation eigenvalue 2. Its onsite remainder is `1-deg(v)/12>=3/4`. Summing gives `L>=3N_A/4`, so the only zero state is the vacuum and every nonvacuum sector has gap at least `g0=3/4`. The resolvent `R_A` on the entire orthogonal complement therefore obeys `||R_A||<=1/g0`. This is the resolvent needed for the two-excitation correction, not just the one-excitation matrix inverse.

Each hopping pair has norm 1 before its factor 1/12. The conservative full-space bound `ell_L=m+E_A/12` and normalized trace `m/2` are correct. The positive-block decomposition has the same total scalar: the redistribution of onsite coefficients does not remove the transport scalar or change L.

## 6. Independent vacuum-block reconstruction of the two-axis contraction

I reconstructed the contraction through the vacuum/off-vacuum block equations, rather than assuming a scalar Pauli-source square from the older mediator. Write the vacuum-to-one-excitation map as

    B_in = |a> S + sum_j |u_j> Z_j,
    S=q(X+iY),              Z_j=z_j n_j.

The declared convention gives `X+iY=2|0><1|` on p, so `S* S=4q^2 n_p`. On the one-excitation auxiliary space, `R_A` is the real symmetric matrix `tau_B`. Therefore

    Sigma := B_in* tau_B B_in
      = 4q^2 gamma_a n_p
        + sum_(j,k) z_j* z_k tau_B(u_j,u_k)n_j n_k
        + sum_j q t_j n_j[(X-iY)z_j+z_j*(X+iY)].

On the entire `N_X=1` space, `n_j n_k=delta_jk n_j`. The last bracket equals `2[Re(z_j) X+Im(z_j)Y]`; the sign of its Y component follows from `i(z_j*−z_j)=2 Im(z_j)`. With `z_j=−(b_j+i c_j)/(2q t_j)`, this gives exactly

    Sigma = C0-W,
    C0=4q^2 gamma_a n_p + sum_j |z_j|^2 gamma_j n_j,
    W=sum_j n_j(b_j X+c_jY).

Block elimination of the fast auxiliary space gives the leading vacuum operator `A−Sigma`, so installing `A=H_b+C0` gives `H_b+W` with the required signs and both independent onsite axes. This is not a scalar source-square and not a claim on arbitrary clock sectors. The full-space source norm bound `2q+sum_j|z_j|` is valid: the port XX+YY block has norm 2q and each combined source has norm `|z_j|`. Its separate real Pauli coefficients can be charged separately when calibration uses that convention.

The inverse denominators are certified positive. Together with `|b_j+i c_j|<=g`, they give `|z_j|<=g 12^(ell_tail+M/2)/(2q)`. The stated `c0_*` follows from `gamma<=4/3`. These bounds establish finite effective choices, potentially extremely large ones. They establish neither polynomial resources nor a common cap. A rational q>0 can be freely selected; no optimal q or efficient table of coefficients is claimed.

## 7. Finite two-excitation correction and the bare prepared map

The block reconstruction alone is not a finite-error theorem. For that, let `epsilon=Delta^-1/2`. Solving the off-vacuum block equation to its first two orders gives

    X1=R_A VJ,
    Y2=R_A Q0 V X1=R_A V X1,
    Z=J−epsilon X1+epsilon^2 Y2.

`VJ` has exactly one auxiliary excitation. V changes that number by ±1, including the port term with its plant operator, while L preserves it. Hence `VX1` has only zero and two auxiliary excitations, and `Y2` has only two. In particular `J*VY2=0`; no scalar third-order term is quietly inserted into the target. The inverse in Y2 is the full resolvent proved above, so a one-excitation free-particle formula is not being extended to a two-particle sector.

The exact identities `LX1=VJ`, `LY2=Q0 VX1`, `AJ=JA`, and `J*VX1=Sigma` cancel the negative powers and the order-one vacuum term. Direct subtraction then leaves precisely

    K_Delta Z−Z H_tar
      = epsilon[X1 H_tar−A X1+VY2]
        + epsilon^2[A Y2−Y2 H_tar].

Here `H_tar=H_b+W` on `N_X=1`. Every potentially noncommuting plant, clock, p-counterterm and program term remains in the displayed products. One does not commute `H_P` through a Pauli source, `K_X` through `n_j`, or W through C0.

For completeness, the finite bound follows directly from the intertwining integral. With `D=K_Delta Z−Z H_tar`,

    ||exp(-itK_Delta)J−J exp(-itH_tar)||
      <= 2||J−Z|| + t||D||.

This needs no assumption that Z is an isometry and prepares no dressed state. The two endpoint differences are essential. `||X1||<=x=v/g0` and `||Y2||<=y=v^2/g0^2` give

    2(epsilon x+epsilon^2 y)
      + tau{epsilon[(a+b)x+v y]+epsilon^2(a+b)y},

which is exactly `F1/sqrt(Delta)+F2/Delta`. The supplied a and b are conservative full-space norms; using them on the invariant sector is safe. The proposed Delta makes each of the two summands at most `eta_goal/2`. The proof is finite-dimensional and uniform for `0<=t<=tau`; no uncontrolled asymptotic notation remains in the final estimate.

Adding `R_pos=sqrt(Delta)v` is a literal scalar reserve. Since A and L are positive, it proves full-space positivity even outside the approximation sector. Alternatively the port block plus `2q I`, and each source block plus `|z_j|I`, are positive local edge blocks, with total scalar exactly v before multiplication by `sqrt(Delta)`. This positivity certificate does not expand the clock approximation to other number sectors.

## 8. Full output, phases, timing and optional composition

First apply the mediator estimate to the entire one-head clock/plant space, then restrict the input to the independently supplied chi. Apply the accepted clock estimate and the step Duhamel estimate at that same time. All embeddings have norm one. The triangle inequality gives exactly `eta_med+eta_clk+eta_step`; the installed reserve multiplies both sides by its known phase. Tensoring any passive reference preserves the operator bound. The two-sided density-product estimate gives `min(2,2 eta_tot)` for the complete retained output, including all correlations.

For optional composition, substitute a separately established external endpoint/window bound for `U_C(T+s)` and keep `H_P=H+rI+lambda J`. The resulting target phase is exactly `R_pos(T+s)+chi(T+s)`, where chi already contains the external compiler's reserve, weak-path scalar, pulse scalar area and determinant lift. There is no additional removal of the sampled scalar-drive terms: those are what make the clock implement the physical positive C, including its scalar area.

The resulting plant target is `exp(-isH) W exp(-iTH)`. All factors age by the actual T and s. Reset or compression consequences require their memory hypotheses at that aged input. The new prepared clock and vacuum are supplied before the entire static evolution; they are not generated from the reset program that the construction is supposed to implement. They are not asserted to be reusable afterward. The standalone proof does not need the separate Lie-algebra proof, a work comparison from that source, or a claim that every weak path coupling works.

Under the late qualified compiler acceptance, its nonempty fixed inventory, complete computable background coefficients, target determinant/phase lift, certified strict searches, smooth positive waveform and actual aged-memory premises must all be retained. Those are additional compiler premises, not consequences of this controller construction. The correction to the compiler's intermediate Pauli-induction wording is not a correction to the new vacuum contraction.

The positivity interfaces match at the level actually needed here: `r>=h+zeta_peak` makes the compiler's whole `H+rI+lambda J` positive, which is sufficient for the present hypothesis `H_P>=0`. It does **not** show that each old local term is a separately positive block. The new auxiliary penalty, counterterms, clock and reserved source blocks have explicit positive-block descriptions; the old `H_P` is used as a whole positive generator. A consumer demanding separately positive old/faulty local blocks must additionally supply the local decomposition and adequate allocated scalar reserves, retaining their changed phase and action. A full norm h alone is not that local certificate.

A horizon `tau>T+w` covers the claimed window without changing physical time. A readout-time perturbation within the admitted interval is charged using the full nominal generator norm, with actual implementation error integrated over the actual elapsed interval. If the target itself is indexed by the actual observation time, its clock path and plant aging must use that time. A detector or repeated intervention requires another explicit Hamiltonian and is not supplied by this output window.

## 9. Scalars, energy moments and physical precision prices

The candidate's complete norm allowance

    B_full=h_b+c0+Delta ell_L+sqrt(Delta)v+R_pos

is a safe upper bound, not a norm equality. Its normalized Pauli scalar follows by tracing each literal term: `s(H_P)`, `M/(2a_c)`, half the sum of `a_j`, `Delta m/2`, `2q^2 gamma_a`, half the clock counterterm sum, and `R_pos`. All source terms are traceless on the full space. The full scalar and the one-head free-clock phase play different roles and both are correctly retained.

The initial moment formula can be derived without the older clock covariance argument. On an arbitrary plant/clock density rho tensored with auxiliary vacuum,

    K_phys J = J(A+R_pos) + sqrt(Delta) VJ.

The two terms lie in orthogonal auxiliary sectors. Thus the first moment is `Tr rho A+R_pos` and the second moment is `Tr rho(A+R_pos)^2+Delta Tr rho J*V^2J`. Distinct auxiliary flips are orthogonal before any transport inverse appears, giving

    J*V^2J = 4q^2 n_p + sum_j |z_j|^2 n_j.

Subtracting the squared mean proves candidate (22), including arbitrary plant/clock covariance inside `Var_rho(A)`. No product cancellation of a noncommuting covariance has been assumed. The supplied product chi is needed for the propagation theorem; it is not an extra hidden hypothesis used to derive this moment identity. Full static mean and variance are conserved. The individual plant, interaction, auxiliary and clock energy pieces need not be.

The mediator bound gives auxiliary leakage probability at most `eta_med^2` from the ideal bare-input domain. Since `L<=ell_L Q0`, the penalty-energy allowance is `Delta ell_L eta_med^2`. At the displayed sufficient scaling this need not tend to zero. Trace closeness to vacuum does not refund the penalty, establish small energy variance, or provide a reusable resource. For approximate preparation, moment bounds require full norms: an initial trace defect eta changes a nominal energy mean by at most `B_full eta` and admits the conservative variance bound `3 B_full^2 eta`. A low-sector norm cannot price leakage.

The listed local block loads are correct for the declared decomposition: an auxiliary site has penalty load at most `Delta[1+deg(v)/12]` plus its source; p has the port load `2sqrt(Delta)q` and counterterm `4q^2 gamma_a`; clock j has `2/a_c`, its source and both occupation coefficients. Assigned scalar reserves must also be charged at their declared locations. Expanding occupation-controlled quadratures into onsite and Z-product Pauli terms is valid, with coefficient halves. Counting those terms and then the entire same block again would double-charge a decomposition, not reveal new physical supports.

Calibration is on the **physical installed generator**, not on a normalized effective model. For example, a penalty error `delta_Delta` alone costs at most `ell_L |delta_Delta|` in the generator norm. If it also changes the source and reserve through the same square root, while other coefficients remain nominal, a sufficient additional allowance is

    ell_L |delta_Delta|
       + 2v |sqrt(Delta+delta_Delta)−sqrt(Delta)|.

This expression includes the phase reserve. Independently specified installed coefficient errors are instead summed with the norms of their literal full-space channels, including C0, clock fields, source quadratures and omitted edges. In all cases the trace price is `2 integral ||E(t)||dt`. Thus large Delta, graph size, inverse-entry coefficients and runtime are paid in absolute hardware strength and precision; the theorem promises no fixed precision across refinements. Integrated generator error alone proves neither positivity of a faulty implementation nor its work cost. Endpoint-defect bounds can suffice for a closed-system endpoint work identity; variation/derivative bounds are another possible contract for estimating work termwise. A finite peak reserve/positive-block certificate is separately required for positivity.

In particular, the separately accepted compiler's work qualification is preserved: for its regular closed dynamics, common initial state, zero endpoint C and actual defect D, the endpoint method bounds the work discrepancy by `[h+lambda(L-1)] min(2,2E_cal)+||D(T)||+||D(0)||`. This is an attributed compiler conclusion, not a new derivation or required premise of the present static theorem. Unbounded scalar derivatives can have zero net endpoint work, whereas a terminal scalar spike can have vanishing integrated norm and unbounded endpoint work. Thus neither a universal derivative requirement nor an integrated-error-only work guarantee should be inferred.

The autonomous model is static, so its nominal closed evolution has no time-dependent pulse-work integral. This is not zero installation cost, free preparation, or a microscopic identification of the chosen finite Hamiltonian's scalar/energy units. The reference external waveform's work convention does not automatically transfer to energy exchanged among the actual autonomous components. Those supply and physical-identification obligations remain open, as the candidate states.

## 10. Explicit failure routes and boundaries

These are failures of specified shortcuts, not universal no-go claims.

1. **Omitting the nonscalar port counterterm fails even when the requested drive is zero.** Set `C=0`, hence all z_j=0, with `H_P=0`. The same vacuum-block calculation gives effective plant drift `−4q^2 gamma_a n_p` if that counterterm is omitted. It remains of order one as Delta increases. For plant input `|+>`, the density distance from the intended unchanged plant is `2|sin(2q^2 gamma_a t)|`, apart from the mediator approximation error. The freely selectable q can place a nonzero discrepancy inside a finite horizon. A scalar reserve cannot erase this relative phase. The candidate includes the required counterterm and does not suffer this defect.

2. **The claimed contraction cannot be extended to a multi-head clock.** On the clock basis vector with heads j and k, j≠k, the extra contraction is `2 Re(z_j* z_k) tau_B(u_j,u_k)`. For a nonzero positive X-only pulse, its Fejer coefficients give real sources of the same sign; the inverse entry is positive, so this term is nonzero. It vanishes on the vacuum and one-head sectors and is not a universal global scalar. The source-square formula with only diagonal n_j terms is therefore false on the full clock space. The candidate uses exact nominal number conservation and a separate unrestricted fault budget instead.

3. **One XX port alone does not supply the second axis in this contraction.** With source `qX` the cross term is `2q t_j Re(z_j) X`; an imaginary clock source does not turn that plant operator into Y. Conversely conjugating the proposed z_j would reverse the implemented Y coefficient. The actual XX+YY port, the stated Y convention and the displayed complex z_j are essential. Their use does not require a second geometric port edge.

4. **Dropping the sampled a_j terms changes the controller.** On the one-head space the operator is `sum_j a_j |j><j|`. It is generally not a scalar. Even if a special waveform made it constant, its isometry phase would still need retention. The original positive pulse's scalar cannot be discarded before the autonomous clock comparison.

5. **A dressed-input argument does not prove the bare-input claim.** The comparison map differs from the actual vacuum injection by order `Delta^-1/2`. Both endpoint differences occur in the exact Duhamel inequality. Removing them would leave an unsupported claim about supplying a dressed state or about a stronger bare-input rate. Likewise a trace-error bound by itself is not a return-energy or repeat-use theorem.

6. **The supplied domain is material.** Arbitrary clock inputs, unspecified environmental couplings, missing full-space calibration, a fixed coupling cap, unaged/reset memory without its state premise, or an unknown waveform without effective approximation data are not covered. Their absence is not a theorem that other architectures cannot address them.

No numerical witness was needed: these are exact finite algebraic or norm arguments. They do not turn the author's statement of zero scientific executions into empirical corroboration or produce a PASS quota.

## 11. Claim-by-claim disposition and open obligations

| Claim | Checked disposition and restriction |
|---|---|
| Finite positive step approximation | Correct with supplied effective C1/Lipschitz/variation data and the true final return to zero. |
| Accepted unary-clock application | Correct at horizon tau, arbitrary fixed finite `H_P`, independent specified one-head packet; all four error terms and phase retained. |
| One-component ordinary-NN mediator geometry | Counts and exterior placement correct; all unlisted interactions still require the stated physical isolation/error contract. |
| Full auxiliary gap | Correct on every excitation sector by explicit positive blocks. |
| Two-axis second-order realization | Correct, with complex sources and the positive **nonscalar** port counterterm, only in the nominal one-head clock domain. |
| Bare prepared-map estimate | Exact finite residual/Duhamel bound; both endpoint errors and full two-excitation resolvent retained. |
| Positivity | Correct full-space nominal certificate after actually adding `R_pos`; faulty positivity remains separate. |
| Complete retained channel and references | Correct factor-two conversion with no discard or postselection normalization. |
| Scalars and moments | Correct literal scalar and initial variance; no energy-return or native physical-energy conclusion. |
| Effective finite resources | Correct finite sufficient allowances, potentially exponential or worse; no efficiency/common-cap claim. |
| Optional external compilation | Exact endpoint/window premise now has a separate qualified root acceptance. The composition matches its actual-time, phase, nonempty-plant, coefficient, aged-memory and whole-generator-positivity contract; this report does not independently re-review its controllability proof. |
| State supply, reuse and native closure | Open supplied-interface obligations, not consequences of this theorem. |

There is no requested amendment to the frozen candidate. Any publication should retain the conditional status, complete source/target domain, actual-time target, full scalar ledger, one-head restriction, all physical prices and separate optional-composition status. No retained audit status is conferred.

## 12. Recovery and actual verification record

`SOURCE_MANIFEST.json` identifies every captured source by exact bytes and SHA256, with a SHA-deduplicated recovery member and its read scope. `READ_COVERAGE.json` distinguishes complete readings, partial dependency readings, exact reused instruction exposure and context-only sources. `METADATA_INSPECTION.json` records source/receipt consistency checks performed by the bounded metadata verifier; it does not assert that hashes prove the mathematics. `metadata_runs/` holds the actual process argv, source-at-launch, stdout, stderr and return status for this task's metadata execution. `FINAL_FREEZE.json` seals every deliverable member except itself.

The evidence package includes the original proposal, source pins, necessary clock proof/restatement and actual acceptance records once. The optional controllability source is preserved with its historical pending wording and freeze; its separate late qualified acceptance is captured as a distinct current source. No historical scientific outputs are rerun or counted as current evidence, and no recursive publication package is copied. The current report, source manifest, coverage record and actual metadata receipts together specify the recovery boundary and the limits of this separate check.
