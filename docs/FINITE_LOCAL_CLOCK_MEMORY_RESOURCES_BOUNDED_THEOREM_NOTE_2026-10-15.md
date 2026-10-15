---
title: Finite memory resources for an installed local-clock reset
claim_id: finite_local_clock_memory_resources_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: finite mixed-memory readiness and supplied biased-memory preparation with installed H0
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: two checked conditional applications with distinct reduced and full retained-output contracts
audit_required_before_effective_retained: true
bare_retained_allowed: false
status: proposed_retained
canonical_parent_binding_complete: true
publication_pr: null
publication_status: dated_separately_from_source_acceptance
source_acceptance_status: checked_conditional_source
upstream_dependencies: ["finite_reservoir_boundary_clock_preparation_bounded_theorem_note_2026-10-15"]
runner: scripts/finite_local_clock_memory_resources_2026_10_15.py
packet: .claude/science/physics-loops/toe-local-clock-memory-resources-20261015
next_trace_action: root-reviewed regular milestone; native purity, scheduling and recycling remain separate
---

Claim type: bounded_theorem

# Finite memory resources for an installed local-clock reset

How much ready memory does a finite unitary clock-reset device need, and can
a larger biased register supply approximate readiness without discarding its
trash? This note groups two checked conditional applications. The first gives
a spectral readiness bound and its finite-clock allocation. The second gives
an explicit returned nearest-neighbour compression circuit, positive finite
pulses and a complete retained-output comparison while the original
`H0 = K + H_app` remains installed.

Current scientific status is **conditional-support**, claim type
**bounded_theorem**. Both complete sources were conditionally accepted without
mathematical repair after separate source-exposed assessments. The historical
provisional/pending sentences in the unchanged bodies below describe their
original freeze dates; they are not the present source disposition. This is
a source-bound publication proposal. Its direct canonical parent is identified
below; actual feature, fresh refs and subsequent outcomes require separate root
records. The preserved offline draft left those fields null. Source acceptance
is not canonical execution, a retained audit or a physical supplier.

## Two contracts, kept separate

All distances use the unhalved trace norm. In the spectral application the
input is arbitrary `sigma_DCR` tensored with a fixed independent reservoir
`tau_E`; every additional entropy sink belongs to `E`. The old output is
protected. The comparison traces out `E` and asks for a fixed old unitary and
a pure clock output with every passive reference. Write `d = dim C`,
`m = dim E`, `q_s = floor(m/d)`, `r_s = m-d q_s`, and decreasing reservoir
eigenvalues `lambda_j`. Every allowed unitary has reduced-channel error at
least

    2[1 - sum_(j=1)^q_s lambda_j - (r_s/d) lambda_(q_s+1)].

For `m=d q_s`, `q_s>=1`, the unrestricted-unitary optimum is exactly
`2[1-sum_(j=1)^q_s lambda_j]`. For unequal nondivisible dimensions the stated
upper and lower estimates need not coincide; for `m<d` the general lower
witness is the claim. These results do not price arbitrary basis alignment or
unitary synthesis. The underlying spectral-packing and generalized-SWAP
machinery is established literature, credited below.

The literal equal-size memory has `d=m=2^n`, `n=L+9`. Necessary reduced reset
error is at least `2(1-lambda_max)`. If the highest-weight eigenvector is the
declared vacuum and the reservoir is independent as specified, the parent's
full retained-output construction instead has the sufficient error

    min(2, 2(1-lambda_max) + 2B t_s + 2G_e t_p).

That sufficient full-output triangle bound is not a full-environment optimum.
The impurity ceiling `Theta(epsilon^3)` applies only to the stated
equal-size, independent identical aligned family with positive fixed clock
constants and `n=Theta(epsilon^-2)`. It is a trace-error allocation, not a
universal hardware or energy-moment bound. Gibbs inequalities require an
actual Gibbs premise. They do not supply cooling, a thermal reservoir or
physical energy identification; retaining a nonzero reservoir Hamiltonian
changes both the comparison and its ledger.

The constructive application uses different symbols: `q` is a certified
single-qubit impurity, `0<q<=q_bar<1/2`; `r>=1` is a recursion depth; and
`Q=3^r` is the length of each of `n` disjoint memory rays. The full initial
state is `sigma_DCR tensor Theta_AS`, with `A=EF` and
`Tr_S Theta_AS=tau_q^(tensor nQ)`. `S` may purify the memory. Product structure
of the `A` marginal and independence between `DCR` and `AS` are supplied,
load-bearing assumptions. Equal one-site bias is insufficient.

Reversible majority compression gives `q_(j+1)=3q_j^2-2q_j^3` and
`p0=(1-q_r)^n`. Its normalized good-block comparison is
`P rho_AS^c P / p0 = |vac_E><vac_E| tensor omega_FS`, and its uniform
retained-purifier error is `delta_r=2sqrt(1-(1-q_r)^n)`. `omega_FS` is a
normalized comparison state, not a measured or postselected output, and it
does not assert exact restoration of `S`. The linear error `2(1-p0)` applies
only to the unpurified diagonal comparison. Search for the sufficient depth
is over integers `r>=1`; choose `r=1` if the original bias already meets the
requested allocation, rather than inserting a zero-slot pulse formula.

## Finite controls, elapsed time and retained information

The recursive word transports gate labels along each ordinary ray and returns
every routing SWAP. It acts on arbitrary dirty transit and retains all
`n(Q-1)` trash qubits. The total physical two-qubit gate count and positive
logarithm action are

    P = n[(20r/3)Q - (7/2)(Q-1)],
    A_c = n pi[(20r/3)Q - (13/4)(Q-1)].

The exact compression scalar action is `A_c/4`. With the stated serialized
smooth pulses, sufficient peak full norm and per-site load are at most
`3 pi P/t_c`, with variation `4 A_c P/t_c`. Reset and entry add the parent's
full `n pi` and `pi` actions, scalars, strengths and durations. The construction
uses `n(1+Q)` added qubits including the clock, on the explicit vacant rays;
all original old sites and every term of `K` remain. Isolation from unlisted
couplings, axes, bias, addressable gates and an external schedule are supplied.
An insufficient fixed cap is not cured by a finite existence proof.

During compression the memory-only controls commute with `H0`, so the exact
old/clock state ages under `H0` for `t_c`. Let `sigma^c` denote that state.
The complete retained `D,C,E,F,R,S` target transfers `C` to `E`, keeps the
normalized `omega_FS`, ages the old system for the additional `t_s+t_p`, and
prepares the clock entry. Its error is

    min(2, delta_r + 2B t_s + 2G_e t_p).

Replacing that target by free old aging under `K` for the entire
`T_ready=t_c+t_s+t_p` costs the additional `2B t_c`. Slow capped compression
belongs to the actual-`H0` target. The free-`K` target can require shorter
compression and larger controls. Neither output contract drops elapsed time.
Subsequent word use preserves the order of preparation, old aging and word
action; no reader, stop or permanent record is supplied here.

The complete scalar, baseline moments and covariances in the two bodies are
retained. In particular the ready entry has mean `Tr(K sigma_D)+alpha0` and
variance `Var(K)+Q_e` for the free-aging target; the actual-aged target uses
the aged old marginal. Positivity of added pulses and `H_app` gives total
positivity only when the installed `K` is positive. No reserve is appended
silently. The instantaneous bounds concern the nominal scheduled generator.
For an actual perturbation `F(t)`, instantaneous energy estimates must also
include `||F(t)||`; an integrated channel-error allowance alone does not bound
its peak. Full-space initial and integrated-generator errors add
`eta0 + 2 integral ||F(t)|| dt` to the trace comparison. All calibration,
storage, timing shifts and changed elapsed-time costs remain explicit.

The construction consumes biased memory and retains entropy in trash and
transferred input. It does not restore a reusable reservoir, erase a passive
purifier, generate native purity, supply autonomous scheduling or implement
classical observation. The finite state and Hamiltonian contracts do not
identify thermodynamic energy or prove practical efficiency.

## Sources, attribution and evidence

The sole external theorem import is the complete accepted finite-reservoir
argument `26220ec995a93bd6af725a6b3463d0b676b9d8a864b4867459bef7dd9560e9b4`
under acceptance `51a1622784a86aac00ef24e5a97af364ccf9034f323a532f8ca0938ddb516e2f`.
Its raw body is archived as `premises/finite_reservoir.md`. The direct
[finite-reservoir canonical note](FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md)
has SHA256 `3560cefa1c9a9e8064a11d2fc683bedd0cab3109905df5bffecdbe1999ad15ad`,
with that complete raw body unique at byte interval `[14549,41771)`.
Actual PR9599 at `94390940f270a7a3db8ca832206ab6076e21025b` is the dated
parent observation. Future feature/ref/source-review and publication records
are separately required; the older null fields remain immutable history.
This theorem edge follows the two bodies' actual use of the reservoir result,
not its position in the PR stack.
The two new bodies do not import each other's theorem. Their grouping supplies
an explicit larger-memory route alongside the equal-size readiness limit.

| Role | Exact source | Current scope |
| --- | --- | --- |
| Spectral application | `f463f5ca12ff7e12d41469cb7129f4602d463420fa13a8163b3bbb53f66dfd74` | Accepted conditional source, root `32b8c2ce`; reduced bound and scoped full-output extension |
| Constructive biased memory | `f38d4590d700db0ce12c491c4e2c21a7843207d226b74089b537519acbd5a86a` | Accepted conditional source, root `435cf70b`; full-reference construction with explicit costs |
| Spectral packing / virtual subsystem | [Ticozzi–Viola (2014)](https://doi.org/10.1038/srep05192), [primary preprint](https://arxiv.org/abs/1403.8143) | Established machinery; the paper's theorem assumes environment dimension at least system dimension |
| Reversible majority recursion | [Kaye (2007)](https://arxiv.org/abs/quant-ph/0703194) | Established independent-bit compression method; no optimal-rate claim |
| Controlled square-root circuit | [Barenco et al. (1995)](https://arxiv.org/abs/quant-ph/9503016) | Established two-qubit decomposition; phases and returned routes checked in the application |

The separate assessments are source-exposed and share the model/family. Their
assessor authored the finite-reservoir parent; they are not blind re-proofs of
that parent. The spectral application is analytic and ran no science program.
The constructive author ran one presealed nine-qubit, `Q=9`, exact phase and
permutation control. Its 92 emitted gates and wrong-dagger, missing-return,
scalar-phase, correlation and purifier discriminators are preserved. It is
not a general geometry enumeration, installed-generator propagation, hardware
experiment or theorem certificate. No science was replayed for this draft.

The proposed primary checks source bytes, complete-body extraction and
historical execution identities only: **zero mathematical predicates**.
External full papers and extracted pages remain local. The explicit exclusion
inventory records every selected copy, including review-archive duplicates,
with identity and primary URL. Authored proofs, programs, full actual streams,
failures and dispositions remain recoverable. Exclusions are not missing
historical evidence and the draft does not claim to reconstruct those papers.

The exact bodies follow without citation, notation, mathematical or status
rewrites. Their original source-relative text is historical provenance.

## Complete accepted spectral-readiness application; unchanged historical source

# Finite-clock preparation from a mixed reservoir: spectral readiness contract

Provisional conditional application, requiring separate substantive assessment. This note does not claim discovery of the general purification principle. Finite-environment spectral packing and generalized SWAP are established machinery; see Francesco Ticozzi and Lorenza Viola, [Quantum resources for purification and cooling: fundamental limits and opportunities](https://doi.org/10.1038/srep05192), Scientific Reports 4, 5192 (2014), also [arXiv:1403.8143](https://arxiv.org/abs/1403.8143). The spectral probabilities in (1)-(3) reproduce their theorem and Methods, with our factor-two full-trace convention. The application here keeps the clock's protected old/reference output and translates reservoir readiness into the literal n=L+9 clock resource schedule. Every argument needed below is given explicitly.

## 1. Model and the complete retained output

Let C have dimension d>=2, E finite dimension m>=1 and D any finite protected old system. R is an arbitrary passive reference. The initial state is sigma_DCR tensor tau_E, with arbitrary normalized sigma_DCR and a fixed independent reservoir state tau. Include every quantum entropy sink, ancilla or discarded controller in E; an omitted sink is outside this model. A prescribed classical time-dependent Hamiltonian may generate any unitary U_DCE. For the lower bounds, no locality, control strength, energy conservation, runtime or complete controllability is assumed. The upper constructions explicitly allow arbitrary joint unitaries, and do not price their implementation.

The retained channel is Phi_U(sigma)=Tr_E[(U tensor I_R)(sigma tensor tau)(U* tensor I_R)]. Fix the target

    Q(sigma)=(V_D tensor I_R) Tr_C(sigma) (V_D* tensor I_R)
             tensor |e><e|_C,

where V_D is fixed, for example the actual elapsed exp(-it0 K), and e is a fixed vacuum or prepared entry. Tensor order is restored to D,C,R. Set delta(U)=||Phi_U-Q||_diamond, using the full trace norm (maximum 2 for two channels). No outcome conditioning or classical detector is involved. A lower bound already follows from an ordinary input without R; an upper bound must hold with arbitrary R. Protecting the old output prevents quietly treating D as an additional disposable bath.

Write lambda_1>=...>=lambda_m>=0 for tau's eigenvalues, sum lambda_j=1. Put q=floor(m/d), r=m-dq and lambda_(m+1)=0. Empty sums are zero. Define

    M_(d,m)(tau)=sum_(j=1)^q lambda_j + (r/d) lambda_(q+1),
    S_q(tau)=sum_(j=1)^q lambda_j.

## 2. Universal lower bound, including old-system protection

For every allowed U,

    delta(U) >= 2[1-M_(d,m)(tau)].                         (1)

Choose sigma_DC=|phi><phi|_D tensor I_C/d. Its desired DC output is the pure vector V phi tensor e. Before U the nonzero global eigenvalues are lambda_j/d, each repeated d times; the unused old directions contribute zeros. Let P=|V phi,e><V phi,e|_DC tensor I_E, a rank-m projection. For any density matrix A with decreasing eigenvalues a_i and any rank-m projection P,

    Tr(PA)=sum_i a_i <i|P|i> <= sum_(i=1)^m a_i.

Indeed 0<=<i|P|i><=1 and their sum is m; shifting weight toward the largest a_i can only increase the sum. This is the elementary spectral variational principle, not a new mathematical ingredient. Applying it to U A U* gives p=Tr(PUAU*)<=M_(d,m). The ideal state gives probability 1 to P. The binary effect {P,I-P}, used only as a trace-norm witness, yields retained trace distance at least 2(1-p), hence (1). The old system's size and the choice of V do not improve this bound.

## 3. Sharp complete-channel contract when m=dq

If m is divisible by d, q>=1, then

    inf_U delta(U)=2[1-S_q(tau)].                         (2)

Only the upper direction requires unrestricted unitary choice. Choose a reservoir eigenbasis and identify E with C' tensor F, dimensions d and q. Assign its q largest eigenvalues to |0>_(C') tensor |j>_F, j=1,...,q, and assign the remaining eigenvalues to the other d-1 groups. A supplied reservoir-basis unitary realizes this identification; it is not a cost-free physical operation. The reduced C' state omega is diagonal with omega_00=S_q. SWAP C and C', followed by the fixed old unitary V and a fixed rotation sending 0 to e, gives for every correlated sigma_DCR

    Phi_U(sigma)=V Tr_C(sigma) V* tensor omega_e.

The reservoir's original C'-F correlations do not create correlations with the initial DCR input, because tau was independent and the entire E is traced in this comparison. The difference from Q is the old channel tensored with omega_e-|e><e|. Its diamond norm equals ||omega_e-|e><e|||_1=2(1-S_q): the upper estimate follows from trace-norm contraction and tensor multiplicativity, and equality is attained on any normalized input. Equation (1) supplies the matching lower bound. This is an exact reduced-channel statement with all passive references, not merely a high ground-state population on one test input.

For general m with q>=1, the constructive upper bound is

    inf_U delta(U) <= 2[1-S_q(tau)].                     (3)

Use E=(C' tensor F) direct-sum E_rem, with dim E_rem=r, and pack the q largest eigenvectors into |0> tensor F. The normalized state supported on that subspace differs from tau by trace norm 2(1-S_q). A SWAP on the tensor-product summand, extended by the identity on C tensor E_rem, resets that normalized ready state exactly; contraction proves (3). No claim that (1) is sharp for r>0 is made. If q=0 only the general lower bound is asserted here.

In particular, exact replacement requires rank(tau)<=floor(m/d). Conversely this rank condition permits the just-described exact SWAP extension. This statement assumes fixed independent tau, unrestricted C input and retention of the old output. It does not price spatial embedding or controls.

## 4. The literal equal-size reservoir

The accepted finite-neighbour construction has n=L+9 clock qubits and n reservoir qubits, so d=m=2^n. Equation (2) becomes

    inf_U delta(U)=2[1-lambda_max(tau)].                 (4)

Therefore any actual finite unitary protocol achieving complete reset or entry-preparation error <=epsilon<2 with this hardware boundary must have

    lambda_max(tau)>=1-epsilon/2.                       (5)

This lower bound includes arbitrary driven H0 and the entry pulse, since their complete propagator is one unitary and the final target C state is pure. Unlike transferring the Markov damping-action inequality through a pulse comparison, no pulse-error subtraction is needed in (5). The two statements use different mechanisms and hypotheses.

Spectral purity alone does not identify the required ready vector. A pure tau orthogonal to the declared reservoir vacuum has lambda_max=1 but the literal SWAP prepares the wrong clock state at trace distance 2. The upper construction in (2) supplies a basis-alignment unitary; omitting its cost would be a physical overclaim. For the already aligned ready mixture satisfying tau|vac>=lambda_max|vac>,

    ||tau-|vac><vac|||_1=2(1-lambda_max).

The accepted finite-reservoir theorem, exact raw source 26220ec995a93bd6af725a6b3463d0b676b9d8a864b4867459bef7dd9560e9b4, compares its full D,C,E,R endpoint with pure ready memory while keeping H0=K+H_app installed. Its bound 2B t_s+2G_e t_p therefore extends by initial-state trace contraction to

    full-output error <= min(2,
        2[1-lambda_max(tau)] + 2B t_s + 2G_e t_p).      (6)

The ideal full target is exactly that parent theorem's transferred-input reservoir state; the actual mixed reservoir and its correlations remain in the output. Equation (6) is a sufficient triangle estimate, not a matching optimum. The universal necessary bound (5) is on the reduced D,C,R output and hence also constrains any full-output realization with that marginal target. It does not require or prove full-environment optimality.

## 5. Product readiness and clock scaling

If the reservoir consists of independent, correctly aligned qubits

    tau=tensor_u[(1-p_u)|0><0|+p_u|1><1|],
    0<=p_u<=1/2,

then lambda_max=product_u(1-p_u). For equal p, reset accuracy epsilon requires

    p <= 1-(1-epsilon/2)^(1/n).                         (7)

With L+9=n=Theta(epsilon^-2) for the specified positive-constant clock family, the right side is asymptotic to epsilon/(2n), hence Theta(epsilon^3). This is a necessary per-qubit error scale in this equal-size, independent, identically mixed reservoir family. It is not a universal lower bound on hardware error and does not assume the actual noise is independent. For a sufficient allocated readiness budget epsilon_ready, impose 2[1-(1-p)^n]<=epsilon_ready and retain the parent's separate drift/pulse allocations. Enlarging the memory or using correlations changes the spectral sum and can relax the per-qubit condition.

The independence qualification is load-bearing. For the correlated mixture (1-p)|0^n><0^n|+p|1^n><1^n| with p<=1/2, each marginal has the same impurity p but lambda_max=1-p, so the optimal reduced error is 2p rather than 2[1-(1-p)^n]. Marginal purity alone cannot be multiplied into a joint readiness certificate. Conversely, correct joint spectral weight without alignment need not certify the literal vacuum.

## 6. Conditional thermal interpretation and its extra costs

This section adds a Gibbs premise; it does not derive thermodynamics or alter the parent's zero reservoir Hamiltonian. For tau=exp(-beta H_E)/Z, beta>=0, d=m and spectral width Delta=E_max-E_min,

    lambda_max <= [1+(d-1)exp(-beta Delta)]^-1.

Subtract E_min only in this estimate: each of the remaining d-1 Boltzmann weights is at least exp(-beta Delta). Combining with (5), for 0<epsilon<=1,

    beta Delta >= log[(d-1)(2-epsilon)/epsilon].         (8)

At beta=0 or Delta=0 the state is maximally mixed and the optimal reduced reset error is 2(1-1/d). Increasing the dimension of a completely maximally mixed E also does not help: (1) always gives that same bound, and a trivial replacement is not supplied by adding unpolarized memory.

For n independent positive-gap thermal qubits with identical gap g and beta>0, the exact product-state condition is

    (1+exp(-beta g))^-n >= 1-epsilon/2,
    beta g >= -log[(1-epsilon/2)^(-1/n)-1].             (9)

As epsilon decreases with n=Theta(epsilon^-2), this requires beta g=3 log(1/epsilon)+O(1). The full reservoir width is ng. The parent finite construction had H_E=0 and a supplied pure state; a nonzero H_E changes its installed comparison. In an elementary complete-operator perturbation comparison, the additional full-output allowance over duration T is at most 2T||H_E-aI||, if the omitted scalar is retained separately in the operator/phase ledger. A sharper resonant control construction is a new obligation. Equations (8)-(9) neither install such a Hamiltonian nor supply a thermalization or purity-generation procedure.

These dimensionless beta-energy conditions do not identify the repository's physical energy, temperature, finite heat capacity or controller work. There is no Landauer-cost, runtime or locality optimum claim. A reservoir-basis rotation, concentration step, changed bath spectrum or rethermalization remains an actual additional operation.

## 7. Positive escape routes and counterexamples to stronger readings

For m=dq with q>1 it is the top-q spectral weight, not lambda_max alone, that governs (2). For example d=2,m=4 and spectrum (1/2,1/2,0,0) admit exact reset even though lambda_max=1/2: the reservoir contains a pure two-dimensional factor and an arbitrary mixed spectator. Thus the equal-size purity requirement cannot be exported to larger memory. Biased many-qubit reservoirs can also concentrate purity into a virtual subsystem; the necessary controls and discarded-memory inventory must be supplied.

Known/reset-restricted clock inputs, initial input-reservoir correlations, conditioning on an outcome, an extra bath or disposal of the protected old system change the model. A known pure C can already be ready with no pure E. Discarding D permits it to serve as an entropy sink and defeats the protected-output proof. These routes are not ruled out by (1), and no universal cooling or TOE obstruction is proposed. Exact reuse of the same reservoir readiness and its correlations is not established by a reduced reset channel; the parent SWAP memory remains consumed.

## 8. Evidence and obligations

The spectral extremization, product formula, Gibbs inequalities and complete-reference SWAP contraction are analytic, with their hypotheses shown. No scientific program, numerical optimization, pulse simulation or new empirical test has been executed for this note. The known general purification machinery is credited; novelty is limited to the explicit protected-output/readiness application and its finite-clock allocation, not asserted as a new general theorem or exhaustive literature novelty.

Required separate checks are the rank-m protected-output witness, the exact diamond upper construction, the full-output versus reduced-output distinction in (6), the independence/alignment counterexamples and the fixed-family epsilon^3/logarithmic calibration. The actual native source of purity, control/calibration, memory recycling, classical observation and physical energy remains unresolved. Formal retained audit is separate. No physical axiom, editable prompt or installed science source changed.

## Complete accepted biased-memory construction; unchanged historical source

# Finite biased memory for the supplied nearest-neighbour clock reset

Status: provisional conditional construction, awaiting separate review. This is an explicit application of known reversible polarization compression, not a new general purification theorem. It replaces the finite-reservoir parent's fresh pure-memory assumption by a larger, initially independent biased mixed register, additional vacancies and calibrated scheduled controls. It does not derive those resources from the lattice axioms, construct a thermal bath, or identify a native cooling law.

## 1. Exact imports and the endpoint to be supplied

The sole mathematical parent is the complete finite-reservoir source26220ec995a93bd6af725a6b3463d0b676b9d8a864b4867459bef7dd9560e9b4, copied as sources/finite_reservoir.md. Its conditional root acceptance, beginning51a16227, is copied exactly. The prior complete source-exposed assessment188275ad is reused at that exact identity; relevant geometry, full-space comparison and energy clauses are refreshed here. Neither the separate provisional reservoir-purity candidate nor its formulas were opened or imported.

Let D be the complete original finite old system, C the parent's n=L+9 clock/mediator qubits, L>=8, and R an arbitrary passive reference. Initially sigma_DCR is arbitrary, including every C-number sector and old-clock-reference correlations. Retain the entire installed operator

    H0 = K + H_app,    ||K-aI|| <= h,
    H_app |vac_C> = 0,    0 <= H_app <= B I,
    ||H_app|| = B,    ||H_app J_e|| = G_e,
    J_e* H0 J_e = K+alpha0 I,
    J_e* H0^2 J_e = (K+alpha0 I)^2+Q_e I,
    G_e = sqrt(alpha0^2+Q_e),    Q_e=2 Lambda |z0|^2.       (1)

All literal parameters, geometry and complete operator formulas are in parent equations1–7. K is arbitrary Hermitian and may fail to commute with H_app. Its scalar and any existing positivity reserve are retained. The center a is only an estimate center. The new register has engineered zero free Hamiltonian and no unlisted couplings. Any failure of this isolation must enter the full-space perturbation budget below.

The parent gives n mutually disjoint ordinary NN pairs u,e(u), u in C. With fresh vacuum on E={e(u)}, its positive parallel SWAP pulse of duration t_s followed immediately by a positive entry pulse of duration t_p has complete output trace error

    2B t_s + 2G_e t_p                                      (2)

relative to C in its bare entry state and the entire initial C register transferred to E, while D ages under K for t_s+t_p. E is retained, including its correlations with D/R. This is a prepared-domain statement, not a channel comparison on arbitrary dirty E. We will supply the missing approximate vacuum while retaining the compression trash as well.

## 2. Supplied biased input, including a passive purifier

Choose an integer r>=1 and Q=3^r. At each e(u) attach Q-1 further qubits along the explicit ray in section5. Let A=E F denote all nQ memory qubits; F contains n(Q-1) trash qubits. No additional clean ancilla is used by compression. Supply

    tau_q=(1-q)|0><0|+q|1><1|,    0<q<1/2,
    Theta_AS with Tr_S Theta_AS = tau_q^(tensor nQ),
    rho_initial = sigma_DCR tensor Theta_AS.                (3)

S is any additional passive reference, possibly a purification of the mixed memory. Thus product structure is required only for the A marginal and between DCR and AS; S need not factor over individual memory qubits. A certified rational q_bar with q<=q_bar<1/2 suffices for effective choices. Bias, independence, the chosen computational axes and engineering the degenerate isolated memory remain supplied conditions. Equal one-site marginals without independence do not suffice. An initial joint-state discrepancy eta0 from (3) is charged in section9.

All norms below are unhalved trace norms. Retaining S matters: the main readiness estimate is of square-root order, even though the unpurified diagonal register has a stronger linear estimate.

## 3. Ancilla-free reversible compression and its finite error

On three bits a,b,c perform, chronologically,

    CX(a,b), CX(a,c), CCX(b,c;a).                           (4)

The first two operations replace b,c by b xor a,c xor a. The final a is

    a xor [(b xor a)(c xor a)] = maj(a,b,c).                (5)

For a=0 this is bc, and for a=1 it is b OR c. The other outputs retain reversible garbage. Every operation is unitary, so the entire transformation is a permutation, not a many-to-one deletion or a postselected operation. Equation(5) proves the majority property on all eight basis states and hence fixes the linear operator once its gate implementation is specified.

For each length-Q ray, recursively compress each of its three contiguous length-Q/3 subblocks, retaining every qubit. Then apply (4) to the first site of each subblock, with the first site of the whole block as output. Recursion stops at one site. The first physical site e(u) contains the recursively cooled bit. Write

    q_0=q,    q_(j+1)=3q_j^2-2q_j^3.                      (6)

At a parent node its three input subblocks have independent marginals, because each came from a disjoint initial product subblock and only internal unitaries have acted. A child output can be correlated with its own trash; this does not destroy independence between the three child marginals. Thus the output error is exactly(6). Different rays have independent A marginals. For the full compression unitary U_c,

    rho_AS^c=(U_c tensor I_S)Theta_AS(U_c* tensor I_S),
    p0=Tr[(|vac_E><vac_E| tensor I_FS)rho_AS^c]
      =(1-q_r)^n,    p_bad=1-p0 <= n q_r.                  (7)

Define omega_FS by normalized projection onto that vacuum event. This is a comparison state, not an actual measurement:

    P rho_AS^c P / p0 = |vac_E><vac_E| tensor omega_FS.

Purify rho_AS^c if necessary, apply P to the purification, and normalize. The overlap of the two pure vectors is sqrt(p0). Their trace distance is 2sqrt(1-p0); partial trace contracts. Hence

    ||rho_AS^c-|vac_E><vac_E| tensor omega_FS||_1
          <= delta_r := 2sqrt(1-(1-q_r)^n)
          <= 2sqrt(n q_r).                               (8)

This bound is uniform over every extension S in(3). If S is absent, the entire A output is diagonal and has orthogonal good/bad E blocks. Its exact distance to the normalized good block is 2p_bad, at most2nq_r. That stronger claim does not hold for a general purifier: for a pure Theta_AS, the projected pure comparison has distance exactly2sqrt(p_bad). We use(8) throughout the full-output theorem.

To choose a finite r for any rational delta>0, iterate(6) starting from rational q_bar until q_r<=delta^2/(4n). All arithmetic can be rational; no numerical eigenproblem or undecidable equality test is needed. Termination follows directly. With b_j=1-2q_j,

    b_(j+1)=b_j(3-b_j^2)/2.

While b_j<=1/2 the factor is at least11/8. Thereafter q_j<=1/4, and 3q_(j+s)<=(3/4)^(2^s). Thus a finite effective certificate exists. These inequalities provide a sufficient bound, not an optimal compression rate. For fixed nonzero initial bias, Q=O([log(n/delta^2)]^(log_2 3)) as delta tends to zero, with bias-dependent constants. For small initial bias the preceding finite amplification phase must also be paid. The exact recurrence and integer stopping rule are the primary resource specification.

## 4. Phase-exact two-qubit word and returned routes

Let V=P_+ + iP_- with P_±=(I±X)/2; V^2=X. The chronological five-gate word

    CV(c,a), CX(b,c), CV†(c,a), CX(b,c), CV(b,a)            (9)

is CCX(b,c;a). For control basis bits b,c its target exponent is c-(c xor b)+b=2bc, and b,c are restored. There are no relative or common phases omitted. Combining(4) and(9) uses seven two-qubit logical gates: four CX, two CV and one CV†.

Every pair gate on ray indices i<j is compiled by moving the state at i to j-1 using the consecutive SWAPs (i,i+1),...,(j-2,j-1), applying the intended ordered two-qubit gate to j-1,j, then applying the routing SWAPs in reverse order. The resulting conjugation is precisely the gate on the original i,j factors and identity on all intermediate factors. Gate control/target orientation is transported with the labels, not inferred from left/right order. This operator identity holds for arbitrary states and correlations of the intermediate factors, including trash. No clean transit assumption occurs.

At recursion level j, put d=3^(j-1). The representatives have indices s,s+d,s+2d. The seven logical distances are d,2d,2d,d,2d,d,d, whose sum is10d. Compiling a distance-l gate costs2l-1 NN gates. Thus one level-j node costs20d-7 physical two-qubit gates. There are Q/3^j such nodes per ray, and the total is

    P_one = sum_(j=1)^r 3^(r-j)(20*3^(j-1)-7)
          = (20r/3)Q - (7/2)(Q-1),
    P = n P_one.                                         (10)

For r=1 this is13 gates per ray. Recursion and the routing rule constitute a finite explicit emitter for every r; no exponentially large unitary synthesis or clean work register is hidden. The construction may serialize all n rays, so only one added compression edge is active at a time. More parallel control is not assumed or credited.

## 5. Literal disjoint rays on the parent's occupied-chain geometry

Retain q_l=(l,0,0), 0<=l<n_old, n_old>=2, every parent C site and all original terms. Use exactly its n reservoir endpoints:

| u | e(u) | ray direction d_u |
| --- | --- | --- |
| v0 | (0,2,1) | +x |
| v1 | (-2,0,0) | -x |
| v_j,2<=j<=L | (1,1-j,-1) | +x |
| a0 | (-2,1,0) | -x |
| b0 | (1,1,0) | +x |
| a0' | (-2,0,1) | -x |
| b0' | (1,0,1) | +x |
| a1 | (-2,-1,0) | -x |
| b1 | (1,-1,0) | +x |
| a1' | (-2,0,-1) | -x |
| b1' | (1,0,-1) | +x |

The ray sites are a_(u,k)=e(u)+k d_u, 0<=k<Q. Negative rays have x<=-2 and distinct(y,z). Positive rays other than v0 have x>=1 and distinct(y,z); their(y,z) never equals(0,0), so they avoid the old chain. Pairs of negative/positive rays sharing(y,z) are separated by their x ranges. The v0 ray has(y,z)=(2,1), unique in the list. All parent C sites have x=-1 or0 and avoid these rays; the v0 endpoint is also outside C. This proves disjointness for every L>=8 and Q, without an all-L enumeration. Extra old sites, if any, must avoid the full enlarged rays.

Every compression edge is an ordinary adjacent ray edge and every reset edge remains(u,e(u)). No wrap-around, crossing identification, new q0 neighbour, motion of physical sites or compression through the old chain is used. Including C, there are n(1+Q) added qubits and

    (L+14)+n(Q-1)+n = L+14+nQ                            (11)

selected edges beyond old K; entry is onsite. The occupied construction lies in

    -Q-1 <= x <= max(n_old-1,Q),
    1-L <= y <= 2,    -1 <= z <= 1.                       (12)

The containing integer box has 3(L+2)[max(n_old-1,Q)+Q+2] sites. Not every site in that box must be a controlled ancilla. Supply the listed vacancies and selected interactions; absence of unlisted couplings is an isolation premise, even where rays approach the old system. This is conditional geometry and addressability, not homogeneous native implementation or a proper-cubic-covariance derivation.

## 6. Positive finite pulses, full scalar and duration

Each physical gate G in(10) has a positive Hermitian logarithm F_G satisfying exp(-iF_G)=G exactly. For Pi=|1><1|_control tensor P_-^target,

    F_SWAP=(pi/2)(I-SWAP),    ||F_SWAP||=pi,
    F_CX=pi Pi,              ||F_CX||=pi,
    F_CV=(3pi/2)Pi,          ||F_CV||=3pi/2,
    F_CV†=(pi/2)Pi,          ||F_CV†||=pi/2.               (13)

In particular CV uses the positive3pi/2 branch, not a negative pi/2 pulse. The scalar component is Tr(F_G)/4=||F_G||/4 for all four rank-one logarithms. SWAP has Pauli expansion pi(I-XX-YY-ZZ)/4; Pi=(I-Z_c-X_t+Z_c X_t)/4. These are full onsite/NN two-qubit terms with their literal scalar included.

Choose a finite compression time t_c>0 and equal slot duration d=t_c/P. In slot ell apply

    G_c(s)=f_d(s)F_ell,    f_d(s)=(2/d)sin^2(pi s/d),
    0<=s<=d,    integral f_d=1.                           (14)

The envelope and its first derivative vanish at slot endpoints. The full installed generator H0 is active in every slot. Since all F_ell act on A alone, [H0,G_c(s)]=0 and the exact compression propagator is

    U_compression = exp(-it_c H0) tensor U_c.              (15)

There is no drift error for this exact factorization and no cancellation pulse. Compression does, however, age D/C under the complete H0, not generally under K alone.

The exact sum of logarithm norms, called the control action A_c, is

    A_c=n*pi[(20r/3)Q-(13/4)(Q-1)] <= (3pi/2)P.           (16)

To obtain(16), each node has20d_node-14 routing SWAPs and logical logarithm norm total15pi/2. The exact integrated Pauli-identity coefficient is A_c/4. Removing those identity terms multiplies the total compression unitary by exp(iA_c/4); it is not the same phase-exact word.

Finite sufficient compression prices are

    peak full added norm = peak per-site load <= 3pi P/t_c,
    integral ||G_c|| = A_c,
    peak ||dot G_c|| <= 3pi^2 P^2/t_c^2,
    integral ||dot G_c|| = 4 A_c P/t_c.                   (17)

The last equality holds for these serialized pulses; the peak bounds are conservative. A fixed cap J_c requires t_c>=3pi P/J_c for this sufficient schedule. The purity recursion alone supplies no fast control or cap-independent implementation.

After compression, apply exactly the parent's pulses, without idle gaps:

    G_s(s)=(pi/t_s)sin^2(pi s/t_s) sum_u(I-SWAP_(u,e(u))),
    G_p(s)=(pi/t_p)sin^2(pi s/t_p)(I-X_v0).               (18)

Their exact endpoints on the comparison domains are SWAP and X, with no dropped phase. The first added full norm peaks at2n*pi/t_s, per-site at2pi/t_s; its action is n*pi and its integrated scalar n*pi/4. Entry peaks at2pi/t_p, action pi and integrated scalar pi/2. The full scheduled duration is

    T_ready=t_c+t_s+t_p.                                 (19)

All added pulses are positive. H_app remains positive. Thus the full instantaneous generator is positive if the already installed K is positive. For arbitrary signed K, positivity of the added controls does not make the total generator positive; no undeclared reserve is appended.

## 7. Complete retained-output theorem and two aging contracts

Let sigma^c=exp(-it_c H0)sigma exp(it_c H0), including R. Let T relabel the complete C register as E. With F,S retained and omega_FS defined by(8), define

    rho_*^aged = |entry_C><entry_C| tensor
       exp[-i(t_s+t_p)K] T sigma^c T*
       exp[i(t_s+t_p)K] tensor omega_FS.                  (20)

Tensor ordering is notational. The original C/R information is in E and may remain entangled with D/R; compression garbage and its purifier remain in F/S. Apply(8) after the exact factorization(15). Then apply the parent's complete prepared-domain comparison, treating F/S as extra passive references. Trace norm contracts under actual unitary evolution. Therefore the entire actual output of(14),(18) satisfies

    ||rho_out-rho_*^aged||_1 <= min(2,delta_r+2Bt_s+2G_et_p). (21)

This is uniform over all sigma_DCR and every Theta_AS allowed by(3), with the actual noncommuting K throughout. It is not a diamond estimate on arbitrary A input. For any fixed supplied Theta_AS it is a reference-complete comparison for the old/clock input channel. The comparison omega_FS depends on the supplied reservoir extension, not on sigma.

If one instead requires the simpler old free-aging target

    rho_*^free = |entry_C><entry_C| tensor
       exp(-iT_ready K) T sigma T* exp(iT_ready K)
       tensor omega_FS,                                  (22)

then Duhamel on the full finite DC space gives

    ||exp(-it_c H0)-exp(-it_c K)|| <= B t_c,
    ||rho_out-rho_*^free||_1
       <= min(2,delta_r+2B(t_c+t_s)+2G_et_p).              (23)

The term2Bt_c is genuine. Leaving H_app installed while compressing cannot silently preserve the original old marginal or replace exp(-it_c H0) by exp(-it_cK). Contract(21) permits slow capped compression but has the actual H0-aged target. Contract(23) permits the free-old target with sufficiently short compression and the larger finite peak in(17). Neither contract removes a conflict with an insufficient fixed control cap.

For positive allocations delta,epsilon_c,epsilon_s,epsilon_p, choose r as in section3 and finite

    t_c <= epsilon_c/(2B),
    t_s <= epsilon_s/(2B),    t_p <= epsilon_p/(2G_e).     (24)

Then(23) is at most delta+epsilon_c+epsilon_s+epsilon_p. Certified rational upper bounds for B,G_e can replace them, giving rational durations. These bounds are finite because the literal parent has B,G_e>0. Equation(21) needs no epsilon_c allocation. No example with a chosen small error proves viability at a hardware cap.

Subsequent use of the unchanged parent word must retain actual order: for(22) the old target is exp(-itK)W exp(-iT_ready K), W=exp(-i pi Z_q0/4)exp(-i pi X_q0/4), with the parent's moving clock factor. For(20), the actual initial sigma^c must remain. This does not supply a stop, permanent record, classical reader or autonomous scheduler.

## 8. Whole energy, covariance, work and retained information

Set beta=h+B. Because the engineered memory free Hamiltonian is zero, all its initial bias and later trash have zero contribution to the stipulated H0, without making their preparation or storage thermodynamically free. Initially the exact H0 variance contains

    Var(K)+Var(H_app)+Tr rho {K-mu_K I,H_app-mu_app I}.    (25)

At any driven time add Var(G) and the symmetrized covariance of H0 and G. No covariance is omitted by assumption. During nominal compression only, DC and AS remain factorized by(15), and H0 acts on DC while G acts on A; that particular covariance vanishes. During SWAP it generally does not vanish. Whole-space instantaneous estimates are

    |Tr(H_total rho)-a| <= beta+||G||,
    Tr[(H_total-aI)^2 rho] <= (beta+||G||)^2,
    Var(H_total) <= (beta+||G||)^2.                       (26)

Insert(17) or the two peaks after(18), as appropriate. The estimates apply to every actual sector; a one-head norm is not substituted for a full-space norm. All original H0 scalars and the control scalars in(13),(16),(18) remain in the actual operator and phase. Raw uncentered moments require ||H0|| or restored a-dependent terms.

With each control vanishing at the stage endpoints, the exact nominal external-work identity is Delta Tr(H0 rho)=integral Tr(dot G rho). During compression this change is exactly zero, since U_compression commutes with H0. The finite variation price4A_c P/t_c in(17) is still charged and bounds an absolute-work integral; it is not a proof of zero controller-resource cost. During reset and entry the parent's sufficient absolute bounds are4n*pi/t_s and4pi/t_p. Work need not be negative. The autonomous controller, its source of precise timing and its own energy storage have not been constructed.

At target(22), with controls off,

    mu_* = Tr(K sigma_D)+alpha0,
    Var_* = Var_sigma_D(K)+Q_e.                           (27)

At target(20), replace sigma_D by the actual aged marginal sigma_D^c. Given complete endpoint trace error epsilon, the same installed H0 obeys

    |mu_out-mu_*| <= beta epsilon,
    |second centered moment difference| <= beta^2 epsilon,
    |Var_out-Var_*| <= 3beta^2 epsilon.                   (28)

For any retained passive subsystem of E,F,R,S, the corresponding linear reference-valued centered moment of order j=1,2 differs by at most beta^j epsilon in trace norm. This is bounded-operator duality after partial trace, not a nonlinear conditional-variance assertion or an energy measurement. Fixed energy-moment allowances can force a much smaller epsilon than trace preparation alone.

The compression unitary preserves total entropy S(A)=nQ h_2(q). Its retained E marginal has entropy n h_2(q_r), so subadditivity implies S(F)>=nQ h_2(q)-n h_2(q_r); equality is not asserted. Correlations with F/S are retained, not erased. The later SWAP stores the original unrestricted n-qubit C information in E. No trash qubit or consumed E is restored to its initial biased state. Fresh repeated uses require fresh biased registers or separately supplied restoration. Even with perfect gates, q_r>0 for finite r and0<q<1/2; this construction supplies arbitrary finite approximate accuracy with growing resources, not exact vacuum from a fixed finite mixed supply.

## 9. Calibration, effective data and finite storage

Let the initial complete state be within eta0 of(3), and let the actual full Hermitian generator differ from the specified complete schedule by integrable F(t), with passive references untouched. For either target above, add

    eta0 + 2 integral_0^T_ready ||F(t)|| dt                (29)

to its displayed error, capped at2. This is full-space Duhamel and state contraction. A norm bound only on the intended excitation sector is insufficient; controls and faults may visit other sectors.

If a compression pulse is f_d F_ell, with a dimensionless logarithm error ||Delta F_ell||<=zeta_ell and envelope error e_ell(s), then a sufficient integrated perturbation bound is

    sum_ell [zeta_ell +(||F_ell||+zeta_ell)integral|e_ell|]. (30)

Multiplying by2 gives its trace-error price. Uniform relative envelope error integral|e_ell|<=rho and uniform absolute logarithm error zeta cost at most2[P zeta+rho(A_c+P zeta)]. There are P addressed gates; a single-gate precision allowance cannot be reused without this sum. The exact coefficients in(13) are computable multiples of pi; physical finite calibration uses certified errors, not a claim of exact real settings.

A shift d_ell of a zero-extended nominal compression envelope, compared in a common fixed interval, satisfies integral|f_d(s-d_ell)-f_d(s)|<=4|d_ell|/d. Thus its contribution is at most8 sum_ell ||F_ell|| |d_ell|/d, or8A_c d_max/d. This does not excuse a changed total elapsed time. The parent's corresponding swap and entry shift prices are8n*pi|d_s|/t_s and8pi|d_p|/t_p. Gaps during memory-only compression can be folded into the actual H0 aging in(20); the free target additionally charges2B times that duration. Arbitrary other gaps require their actual-generator comparison. A wrong post-pulse endpoint time dt separately costs at most2||H0|| |dt| on states, or must be reflected in the time-indexed target. Phase-sensitive maps retain the full scalar.

An unwanted memory free Hamiltonian or coupling is included in F for the entire actual duration, not just gate times. A later storage disturbance of norm at mostnu for T_store adds at most2nu T_store. Engineered degeneracy/isolation, bias certification, axis selection, the nQ vacancies, switching, classical scheduling and any eventual readout remain supplied. No instantaneous reader, measurements during compression, refresh bath or microscopic reservoir law is used.

All finite inputs needed by this recipe are explicit: L and the parent finite coefficients with certified upper bounds B,G_e,h; n_old; rational bias certificate q_bar<1/2; requested positive error allocations; the ray vacancy/isolation certificate; and full-space control/timing-error budgets. The rational recurrence chooses r, (10) fixes every gate count, the recursive routing rule fixes every edge, and(24),(30) give finite sufficient durations/precision. No recurrence search or generic controllability oracle is hidden.

## 10. Prior machinery, selected check and unresolved supply

Ticozzi–Viola, arXiv:1403.8143, physical PDF pp2–3, gives virtual-subsystem purification under initial factorization and unrestricted unitary controllability. It does not itself supply the local timed circuit here. Kaye, arXiv:quant-ph/0703194v3, sections2,3.2,4.1, treats independent biased bits, reversible three-bit majority and its recursive use; that mechanism and bias polynomial are prior art. We do not use its small-bias approximation near unit polarization. Barenco et al., arXiv:quant-ph/9503016v1, section6.1, pp14–15, supplies the standard controlled-square-root decomposition, which(9) checks directly. No optimality or general purification novelty is claimed. The fresh application is the explicit returned NN ray word, its full positive/scalar schedule and its reference-complete composition with this unchanged installed H0, with the costs and two aging targets separated.

One predeclared selected calculation checks r=2,Q=9,q=1/4. It implements the compiled quantum gates using exact Gaussian rational amplitudes and compares all512 basis columns against a separate recursive Boolean permutation. It checks the full gate phase and returned dirty transit, not only output labels. CV† substitution, a missing route-return SWAP and scalar deletion are discriminators. A fully correlated all-equal input with the same one-site bias demonstrates the necessity of independence. The purified-output overlap demonstrates why the linear diagonal readiness price cannot be asserted with an arbitrary retained purifier. The general all-r/all-L statements, drift comparison and energy identities remain analytic; no parent science program is replayed.

The unitary compression does not by itself prove a useful native supply. It trades fresh pure memory for a larger supplied biased product marginal, finite isolated vacancies and the paid schedule. A fixed insufficient cap can invalidate the short-time free-old target; a slow schedule retains the actual H0-aged target. Purity/trash restoration, environmental isolation, autonomous implementation, physical energy identification and classical reading are separate undeveloped interfaces. This is a bounded constructive conditional candidate, not a universal negative theorem or a closure claim.
