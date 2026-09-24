# Released-source POST: microscopic finite-bin original records

Bounded independent comparison, 2026-09-24. The blind PRE and every member of its seal remain unchanged. This report compares the complete released root derivation and its complete recorded controls with that PRE. It neither certifies the supplied parent theorems nor inspects the other provisional readout candidates. No author numerical code was rerun, and no publication or audit state was changed.

**Finding.** The released argument supports the same conditional fixed-window microscopic-to-full-rotor event convergence and selectable relative-accuracy diagonal established in PRE. Its full-history partial-isometry register is valid on the stated reachable physical sectors. Its target-hazard boundary estimate is valid and improves the dependence of the PRE's loose area estimate. No load-bearing discrepancy was found. The concrete photon-packet contrast in root section 4 remains an explicitly imported hypothesis; only its microscopic diagonal transfer is checked here.

Two minor qualifications make the formulas valid at their edges: append operators always have norm at most one, with norm one when the history cap is positive; the explicit two-eigenvalue waiting formula requires distinct roots or its continuous extension at a double root. Neither qualification affects the physical two-event claim, any recorded control row, or the small-epsilon conclusion.

## 1. Frozen inputs and scope of evidence

The preserved independent report is `PRE.md`, SHA256 `e48f606abebb28c5e60cbd98539284aee214e3f2819597621c6809dc1f5d2ec0`. Its separate `PRE_SEAL.json` has SHA256 `34cbabad0237942680176e23a39bfdd6e9f4f34bbf56f1ff4f50b15178838f41`. All thirteen PRE members were rehashed successfully, including the original independent six-state control and complete results/logs.

Released root directory:

`/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/microscopic-record-readout-personal`

| Released input | SHA256 |
|---|---|
| `MICROSCOPIC_FINITE_BIN_RECORD_BRIDGE_ROOT.md` | `a04e25530ccf1dc8df8a27b41523d04703c09ff758664792a9487a8cea0ce60c` |
| `AUTHOR_CONTROL_SEAL.json` | `1c43b31b63f89ba2bf246e50aa5e8dd95d93d77f0e06aafd8d394909966a9146` |
| `finite_register_controls.py` | `dc9952e2ae47f69cc9a258b72c01d009b356b6459e168e830dc045dfaca59771` |
| `FINITE_REGISTER_CONTROL_RESULTS.json` and byte-identical `CONTROL.stdout.txt` | `520128a1354cb2c17cd67d46f3cf641418aa981f3dfdaabcbffca5ad9fe90823` |
| `CONTROL_EXECUTION.json` | `9931089898a357cb003510eb65658f4800086fea30aa2959f3018d046aafc50b` |
| `CONTROL.stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `SOURCE_PINS.json` | `0f040139e3db7d300fccf11725341d8cd05e477d308ccbb81820e2e223256928` |

All seven author-seal members match; all eight released files, including the seal itself, have exact read-only snapshots under `post-released/`. The complete argument, code, output, execution record, and source-pin metadata were inspected. `POST_SOURCE_PINS.json` and `POST_EVIDENCE_CHECK.json` bind the exact origins and snapshots.

The two physical parent sources remain the complete PRE-read arguments at main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`:

- `BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9`;
- `LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b`.

Their exact Git bytes and those of all three PRE-pinned instruction sources were reverified. Root's pins for these two parents match the PRE origins and identities. The other two entries in root's source-pin metadata refer to active target readout candidates. Their underlying files were not opened or hash-verified; their stated hypotheses receive no independent physics judgment here. Reading their metadata does not promote them to checked dependencies.

## 2. Full-history register and physical terminal sectors

Root uses the supplied initial physical sector `N0=|A|`. On the fixed finite graph, the Hamiltonian, compensation, and no-event evolution preserve physical record number N. Every original formation channel raises N by two. The hard-core matter space has at most `|A|+|B|` records, so at most

    M = floor(|B|/2)

formations occur. This bound concerns the full microscopic matter space, including excursions outside P, as well as the P rotor target. It does not assume that every A site stays occupied during microscopic no-event motion.

For m time bins and q original mark channels, root's register is the finite span of words of length at most M over `(bin,mark)` pairs. Its dimension is

    dim R = sum_(k=0)^M (m q)^k.

Including words with nonchronological bin labels is harmless: those basis states are unreachable from the empty word. The register grows when the fixed partition is refined; the proof claims no uniform bound in that dimension.

Let `Pi_<M` and `Pi_M` be the register projectors onto nonterminal and terminal words. For a fixed bin r and original mark j,

    V_(r,j)|w> = |w,(r,j)>  if |w|<M,
    V_(r,j)|w> = 0          if |w|=M.

Appending a fixed symbol is injective on nonterminal prefixes. Thus

    V_(r,j)* V_(r,j) = Pi_<M,
    ||V_(r,j)|| <= 1.

The norm is one for `M>=1`; when `M=0`, V is zero and no physical birth can occur. Root's unqualified phrase “norm-one” should be read with this trivial qualification. A first-two-event probability is itself zero when `M<2`.

The reachable joint space is

    R_reach = direct_sum_(k=0)^M H_(N0+2k) tensor R_(length k).

It is invariant: Hamiltonian/no-event terms preserve both summand labels, and each jump raises both labels together. At length M, the number of physical empty sites is

    |A|+|B|-(N0+2M) = |B|-2M, which is zero or one.

Every physical formation term requires two empty sites. Consequently every original j vanishes on that physical N sector, irrespective of record positions, signs, fields, or whether the microscopic state is in P. The effective B also raises N by two and vanishes on the corresponding target terminal sector.

For example, with `Gamma_micro=sum_j L_j*L_j`, the lifted loss is globally

    Gamma_micro tensor Pi_<M,

not `Gamma_micro tensor I` on the entire enlarged Hilbert space. The difference is `Gamma_micro tensor Pi_M`, which vanishes on `R_reach`. This distinction is essential and root states it correctly. One cannot append a zero terminal map and claim unchanged loss for arbitrary off-reachable system/register inputs. Here exact faithfulness follows from the actual physical cap, not from an artificial suppression of later physical events.

The register starts diagonal. Hamiltonian terms act as its identity, each jump sends a diagonal word block to one diagonal word block, and `V*V` is diagonal. Therefore it stays classical. On the reachable classical states, tracing the register gives the original physical jump term and original loss exactly. Continuing all words through their full allowed length includes all possible later events. Reading the first two entries places no restriction on entries after them.

This implementation differs from the independently derived PRE monitor. PRE used a saturated first-pair register, split by its classical source state, and finite archive copies. That construction continues the physical jumps even after the memory saturates and does not need this full-history cap. Root instead keeps the full finite history and the original number of channel operators. Both are valid mathematical encodings of the stated original instrument; they are not identical constructions and neither is evidence of a physical autonomous detector or irreversible memory resource.

## 3. Original coherent channels and the finite-partition limit

During one fixed time interval, root lifts each original microscopic channel as

    j_j,S tensor V_(r,j).

Hamiltonian, W, T, C, the physical P projector, and the canonical cluster rotation act as the physical operator tensored by I. In particular,

    [W tensor I, j_j,S tensor V] = -j_j,S tensor V,
    (j_j,S tensor V)(P tensor I) = 0,
    ||j_j,S tensor V|| <= ||j_j,S||,
    B_lifted = (-P j_j,S Pi_1 T_S P) tensor V.

Record-number conservation of T, C, and the Hamiltonian, and the physical Gauss constraints, are unchanged. All relevant register factors are bounded independently of S. The two stated parent register extensions therefore apply on each fixed interval.

For a prescribed coherent mark, the whole coherent physical operator is tensored by a single V. Its internal signed terms do not acquire distinct register labels. Thus its interference terms in the jump map and loss remain intact. A resolved instrument has its separate original resolved labels. Root does not substitute one instrument for the other.

At a deterministic bin switch, the physical state is not reset and no new physical measurement is introduced. The writing rule changes for the mathematical record only. The final joint density is a finite product of lifted semigroups. The microscopic-to-spin-target comparison telescopes by trace-norm contractivity: propagate the previous error using the microscopic map, and apply each fresh local comparison to the P-supported target input. The actual microscopic intermediate state need not itself remain in P. This is the same point made explicitly in PRE.

For the spin-target-to-rotor step, bounded jump/magnetic terms and their adjoints converge strongly, the full matter-dependent `K D` interaction-picture construction is unchanged, and finite register factors preserve these properties. Strong trace-class convergence on each fixed input, followed by a finite product argument and initial trace-norm approximation, suffices. No operator-norm convergence over all rotor preparations is being asserted.

For each fixed partition, every bounded classical word indicator therefore has a convergent expectation. The physical Hamiltonian after the first birth is still the full compensated rotor Hamiltonian. Nothing in this step invokes a field-only postbirth law, a common fast generator, exact-time conditioned convergence, or a microscopic hazard bound uniform in epsilon.

The particular full-history cap here is tied to `N0=|A|`. Extending the initial matter sector or allowing arbitrary mixtures of N sectors requires the corresponding cap or an alternative monitor such as PRE's construction. Root's arbitrary-normalizable-field statement keeps the stated initial matter sector; it does not by itself change that sector.

## 4. Positive-width event, target hazard, and bin removal

Take `I=[t,t+h]` with `t>=0`, `0<h<infinity`, `0<b<infinity`, all fixed, and a finite horizon `T*>t+h+b`. The event is the first overall mark j at time s in I, followed by the next overall mark l at time `s+u`, where `0<u<=b`. No event occurs before the first or between the two. Later events are unrestricted. This is the same joint event as PRE, not a probability conditioned on a first occurrence of j after other allowed marks.

Write the full rotor jump operators as `L_j=sqrt(kappa) B_j`, loss `Gamma=sum_j L_j*L_j`, and full self-adjoint Hamiltonian as `h_rotor=K D+delta H4`. For the no-event contraction

    V(u)=exp[u(-i h_rotor-Gamma/2)],
    T_u(rho)=V(u) rho V(u)*,

bounded positive Gamma gives a strongly continuous completely positive contraction even when the initial state has no finite energy moments. The target waiting-time density from a normalized post-event state sigma obeys

    f_sigma(u)=Tr[Gamma T_u(sigma)]
              <= ||Gamma|| Tr[T_u(sigma)] <= R,
    R=||Gamma||=kappa ||sum_j B_j*B_j||.

The same inequality bounds the first-event density. These density and survival identities use bounded loss and strong continuity; no derivative of the initial density under the unbounded Hamiltonian is needed. A zero-survival conditional state need not be normalized; it has zero contribution to the event measure.

For fixed original marks the exact joint kernel from PRE remains

    p(j,I;l,b)=integral_I ds integral_0^b du
              Tr[J_l T_u J_j T_s(rho)],
    J_j(rho)=L_j rho L_j*.

The no-event factor between births retains exact full postbirth dynamics. The full trace-preserving evolution after the second event drops out of this trace, precisely because later events are unrestricted.

Root's finite-word lower and upper events are pathwise brackets. The recorded word order handles two events in one bin without imposing a fictitious strict ordering of their bin indices. For mesh eta, their difference can only involve first times within eta of an endpoint of I, or lags within `2 eta` of b. The lag-zero boundary is already excluded by the ordering of two actual events; simultaneous events have no mass.

The first-time endpoint strips have total length at most `4 eta`, contributing at most `4 R eta`. Conditional on the first event and its state, the lag strip has length at most `4 eta`, contributing at most `4 R eta` to a next-wait distribution. Averaging over the first-event distribution multiplies that bound by a mass at most one. Thus

    p_rotor(A_eta^+ minus A_eta^-) <= 8 R eta.

This is a valid alternative to the PRE estimate `8 lambda_j lambda_l H eta`, where `lambda_j=kappa||B_j||^2`. The two bounds use different information and neither need be smaller for every numerical parameter choice. Root's bound removes the explicit horizon factor by using the normalized conditional waiting measure. This improvement belongs to the released root argument, not to the frozen PRE.

Fixing each partition first gives convergence of both bracket probabilities by section 3. Taking the microscopic/spin limit before eta tends to zero squeezes the actual event probability to the full-rotor event probability. At fixed microscopic parameters deterministic endpoint ties also have zero mass, but no uniform microscopic boundary-density estimate is required. The bare microscopic jump intensity scales as epsilon to the power minus two; using it in a simultaneous mesh limit would introduce an unproved uniformity.

The result is conditional on both parents, at fixed finite graph, positive K, delta, kappa, and fixed windows, along integer S tending to infinity with `epsilon^2 S(S+1)=delta/K`. Initial physical spin/P densities must converge in trace norm to the fixed rotor preparation. The result covers arbitrary normalizable fields under that approximation, with no high-field moment hypothesis. An unbounded observation horizon, exact-time density derivatives, continuous-history total variation, and arbitrary shrinking-window schedules are not supplied by this proof. A normalized conditional readout would require additional denominator control if its conditioning probability shrinks; the joint event used here has no such denominator.

## 5. Ordered transfer of the provisional packet contrast

The general diagonal conclusion agrees with PRE: for a fixed row of finitely many experiments, freeze its preparations, couplings, windows, and positive comparison scale, and use fixed-instance convergence to make all errors smaller than any chosen fraction of that scale. Row-dependent thresholds can then be selected; no modulus uniform across rows follows.

In root section 4 the unreviewed target input is specifically

    K_g=c g^2/(2a),    delta_g=c/(4a g^2),
    d_n=kappa^2 b_n g_n^2 > 0,
    (p_rotor,1(n)-p_rotor,0(n))/d_n -> -2 H_I,

under the other candidate's preparation and small-bin hypotheses. Here `c,a,kappa,I` and the graph are fixed. This POST does not establish that target limit, determine its small-bin condition, validate a packet construction, or identify its physical parameters. It checks the implication if those premises hold and the preparations meet the parents' fixed-instance assumptions.

For a fixed normalized rotor packet, its normalized physical spin-box projection converges in norm once the projection has nonzero mass. Keeping the bare P matter sector is allowed by the supplied parent. This is a convergence statement about the chosen preparations, not a preparation-cost estimate. The actual packet specifications remain outside this check.

At each n choose S large enough that both event probability errors are at most `eta_n d_n`, with positive `eta_n -> 0`. Then

    |(p_micro,1-p_micro,0)-(p_rotor,1-p_rotor,0)|/d_n
        <= 2 eta_n -> 0.

One common S per row works by taking the maximum of the two thresholds, since those two arms share the same couplings and scaling ratio. It can also be enlarged to make S_n strictly increase and epsilon_n tend to zero. For example, the additional condition

    S_n(S_n+1) >= n^2/(2 g_n^4)

ensures `epsilon(g_n,S_n)<=1/n` under the stated ratio `delta_g/K_g=1/(2g_n^4)`. This extra inequality is only one admissibility condition; it is not the unknown accuracy threshold or a sufficient standalone resource scaling for the contrast.

Consequently the imported normalized limit transfers along a suitably chosen diagonal. If `H_I>0`, the contrast is negative for all sufficiently large n. It is a difference of two nonnegative event probabilities, not a negative probability or a positive-click claim. If `H_I=0`, this implication transfers a zero normalized limit and supplies no nonzero contrast sign.

The constants and approximation tails may vary with n, and the strong rotor limit has no supplied general rate. An arbitrary prescribed simultaneous schedule cannot be substituted for the chosen diagonal. Root retains this restriction correctly. This conclusion supplies neither an economical spin cost nor a common detector, clock, feasible preparation, statistical sample size, or observational identification.

## 6. Root five-state control versus the independent PRE example

The complete root code and all six waiting rows and five grid rows were inspected. Its five states are `P0,Q0,P1,Q1,P2`; this is an abstract finite penalty model, explicitly not a physical cube, spin-link realization, or cubic photon simulation. The three P states have zero penalty, the two Q states penalty one, and the two active record stages have N equal to zero and two before ending at four.

The displayed matrices give `jP=0`, `[W,j]=-j`, `[N,j]=2j`, `[N,T]=[N,C]=0`, and `[W,C]=0`. The active compensation cancels the second and fourth coefficients exactly. With the root sign convention for T,

    B=|P1><P0|+|P2><P1|,

so the target first two waits are independent exponentials of rate kappa and then formation stops. The code's exact symbolic checks agree with these products. Its append check enumerates six legal images for two symbols and a cap of two and confirms the terminal physical jump column is zero. These are bounded corroborative checks of one abstract example; they do not replace the general reachable-sector argument in section 2.

In each active microscopic block the no-event amplitude matrix is

    A_e=-i delta epsilon^-4 [[epsilon^2,-epsilon],[-epsilon,1]]
        -(kappa/(2epsilon^2)) diag(0,1).

Actual jumps reset to the next bare P state, so the first-two event probability factorizes as

    [F_e(t+h)-F_e(t)] F_e(b).

For distinct eigenvalues lambda_s and lambda_f, the off-diagonal propagator is

    (i delta epsilon^-3)/(lambda_s-lambda_f)
       [exp(lambda_s u)-exp(lambda_f u)].

Squaring and integrating yields the root's three-term exponential CDF. This formula needs its continuous limit at a double eigenvalue; it is otherwise an ordinary exact two-by-two identity. The controls use epsilon from 0.4 down to 0.0125, delta=1, kappa=0.7, all away from coalescence. For arbitrary fixed positive delta and kappa, sufficiently small epsilon is also away from coalescence. The limiting exceptional formula is not needed for the claimed asymptotic.

The short-bin result follows analytically, not merely from the printed rows. If `b=epsilon^6`, then `b||A_e||=O(epsilon^2)`. Variation of constants for the Q amplitude gives, uniformly on `[0,b]`,

    Q(u)=i delta epsilon^-3 u [1+O(b||A_e||)].

Indeed its equation has that off-diagonal driving coefficient, while the P amplitude and the diagonal exponential remain `1+O(b||A_e||)` on the interval. Therefore

    F_e(b)=(kappa delta^2/3) epsilon^-8 b^3 [1+o(1)],
    F_e(b)/(kappa b)=(delta^2/3) epsilon^4 [1+o(1)] -> 0.

The target ratio `(1-exp(-kappa b))/(kappa b)` tends to one. This is a controlled relative-resolution counterexample in the separate abstract model, consistent with the PRE warning about arbitrary simultaneous schedules. It does not specify a sharp cube resolution threshold.

The PRE example is independently specified and remains separate: it has six states, the opposite hopping sign, an additional last excited state, two kappa arms, and shrinking first and lag windows proportional to epsilon to the fifth power. Its analytic conclusion is loss of an entire relative contrast. Root instead uses five states, one kappa, a fixed first window, and lag `epsilon^6` to compare a waiting CDF with its target. The global sign of the effective jump does not change that jump's CP map; the difference after the second event does not change an already recorded first pair. These points explain consistency, not identity of models, code, parameter rows, or numerical evidence.

The root finite-grid control uses the two-wait target density `kappa^2 exp(-kappa y)` in first/second absolute-time coordinates `(x,y)`. For unequal bins its integral is `eta kappa [exp(-kappa y0)-exp(-kappa y1)]`; for a diagonal bin it is `exp(-kappa x0)[1-exp(-kappa eta)(1+kappa eta)]`. The displayed control uses these correct masses. Its cell classifier gives conservative lower and upper events and includes same-bin event ordering. The total second-event mass is the Erlang-two CDF through its chosen horizon.

For `t=0.3`, `h=0.4`, `b=0.1`, `kappa=0.7`, the target event probability is `0.0133831741788604443...`. The root fixed-bin absolute error decreases across its displayed epsilon rows from `0.008480956799987...` to `0.0000233467869153...`. The smallest-epsilon microscopic shrinking-bin CDF ratio is `8.13802077124e-9`, with ratio to its analytic leading term `0.999999992370224...`; the target CDF ratio is `0.9999999999986649...`.

Across the five grid rows, bin counts 6 through 96 give bracket gaps from `0.0566714053063...` to `0.00321913544263...`, within the corresponding loose bounds `8 kappa eta`. These are finite high-precision numerical corroborations, not interval enclosures or proofs of a uniform numerical rate. No failed or adverse result is concealed: the unfavorable shrinking-bin limit is an intended preserved result, not a harness failure.

## 7. Binding checks, execution limits, and disposition of this check

The author result's source fingerprint and author execution's script fingerprint both equal the exact released code hash. The reported author execution exited zero with wall time `0.6305460829753429` seconds. Its result records internal elapsed time `0.29888254194520414` seconds, which is a different timing scope and not a discrepancy. Author stdout equals the result bytes exactly; stderr is empty. The root author seal binds these records together.

`verify_post_bindings.py` independently checks those byte bindings, all unchanged PRE members, all five exact Git origins, the two root parent pins, and arithmetic consistency of every recorded waiting/grid row using Decimal operations. It never imports or executes the author control. Its one successful binding run took `0.1586222080513835` seconds, exited zero, and had empty stderr. Complete output and execution records are retained as `POST_BINDING.stdout.log`, `POST_BINDING.stderr.log`, and `POST_BINDING_EXECUTION.json`; no failed binding run was discarded.

This establishes inspected source/result/execution correspondence and the stated analytic comparison. It is not a fresh independent numerical replication of the root values. The numerical evidence that was independently produced before release remains the six-state PRE packet, with its original scope and hashes.

The supported milestone is a conditional theorem about the actual original marked event in fixed positive windows and an existence diagonal for supplied shrinking contrasts. The load-bearing parent assumptions, original resolved/coherent instrument, full physical matter/field spaces, and order of limits are preserved. The two edge-formula qualifications above can be incorporated in final prose without changing the theorem. Other target readout claims remain provisional and outside this check. No publication approval, retained-grade audit verdict, new axiom, or apparatus claim is issued. Work stops with the separate POST seal.
