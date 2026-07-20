# Physical Route-C Q6 factorized resource scout — Cycle 512

Date: 2026-07-20
Authority: none
Audit: unset
Disposition: bounded constructive update-2 prefix; Cycle-511 depth-5 sentinel remains open

## Result

Cycle 512 closes a real implementation question at the first entangling layer of the frozen Cycle-511 Route-C sentinel.

For each of the three axial pure components of `rho_AB3`, the canonical N=2 CAR matter state and the literal hard-core Q=6 mediator state admit a nine-term matter–mediator factor representation after update 2. The unpruned complex128 factor construction reproduces every stored packed amplitude with L2 residual between `4.15e-20` and `4.65e-20`. The numerical Schmidt rank at the declared relative cutoff `1e-12` is `9` for all three components. No amplitude or singular value was truncated.

This is not a depth-5 result. It supplies no update-3 rank bound, no response value, no deletion or held row, no source-selection law, no global physical-M2 compiler, and no physical-time interpretation of the update counter.

## Frozen scope

The run inherits the exact Cycle-511 scout authorization rather than inventing a new execution scope:

- target: `RouteC8[0]`, intact L15 middle-beta row;
- matter: canonical two-CAR-mode exterior state;
- mediator: canonical sorted Q=6 occupation of the physical seven-M2 local receiver modes;
- update word: frozen Cycle-511 free-plus-contact/emitter/collision/stream word;
- resource caps: wall `<1200 s`, RSS `<3,000,000,000 B`, process swap `0`;
- execution: one resource scout, no science or response row;
- runner integrity: byte-exact SHA-256 required in addition to the frozen token.

The actual runner SHA was:

`d90525f7c25c92762851ac07b9ea58c28123c378fd0fdea6ce3ab565108834fe`

## Construction

Before the first collision the state is a product. At update 2, each axial component has exactly two disjoint active collision cells. On the supported input at either cell, the local physical collision reduces to three factor terms:

1. `I`: identity;
2. `D`: the diagonal correction with coefficient `cos(theta)-1`;
3. `X`: reciprocal matter/mediator exchange with coefficient `i sin(theta)`.

The two active cells commute, so their Cartesian factor word has the nine terms:

`II, ID, IX, DI, DD, DX, XI, XD, XX`.

The resulting factor matrices have shapes `5104 x 9` for matter and `1296 x 9` for the mediator. The amplitude convention is `A = X Y^T`; the small core therefore uses `R_x R_y^T`, not an adjoint. The mediator stream is a permutation applied independently to every right factor.

This gives an explicit untruncated nine-term expression in the implemented complex128 arithmetic for the declared update-2 layer. Minimal Schmidt rank is reported more narrowly as a numerical statement at the declared cutoff.

## Support ledger

Three different notions are kept separate:

| Per axial component at update 2 | Count |
|---|---:|
| Stored packed canonical keys, including exact zeros and cancellation residues | 3,626,856 |
| Machine `value != 0j` entries | 1,890,378 |
| Analytically nonzero entries | 1,625,022 |
| Exact-zero or cancellation-residue squared norm below `1e-14` | about `1.297e-33` |

The analytic count is not obtained by deleting small floating values. A parallel exact diagnostic evolves tags in `Q(zeta_9)[z]`, where `z=exp(i*37/100)`, while leaving the floating state untouched. The decimal contact declaration `0.37` is interpreted as the exact rational `37/100`. Lindemann–Weierstrass supplies the explicit theorem import: `exp(i*37/100)` is transcendental over the algebraic field `Q(zeta_9)`, so a nonzero formal contact polynomial cannot vanish at the declared phase.

The post-collision analytic count is additionally conditional on the supplied collision diagonal and exchange coefficients being nonzero. Their executed values are `0.9987329089332052` and magnitude `0.05032471176090357`, safely separated from zero numerically; this receipt does not provide an analytic interval certificate for that supplied angle.

The exact matter supports are `9 -> 81 -> 2169`. The stored matter dictionaries are larger, `9 -> 153 -> 4911`, because the no-pruning implementation retains cancelled keys. At update 2 the exact collision-opportunity counts are `{0:1990, 1:178, 2:1}`; outgoing-only active-mode incidents are zero on every axis. These facts give collision sectors `(k0,k1,k2)=(1,537,542,43,578,81)` and packed analytic support `k0 + 2 k1 + 4 k2 = 1,625,022`.

## Exact operation and key ledger

Every axis independently matched the frozen ledger:

| Quantity | Per axis |
|---|---:|
| Pre-collision Cartesian inputs | 3,580,119 |
| Source occupied-cell stages | 7,098,273 |
| Actual local lookup calls after branching | 7,121,601 |
| Branch histogram | `{1:3,533,544, 2:46,494, 4:81}` |
| Inputs with a nontrivial branch | 46,575 |
| Diagonal contributions | 3,580,119 |
| Off-diagonal contributions | 46,737 |
| Generated contributions / unique packed keys | 3,626,856 |
| Packed-key collisions | 0 |
| Lawfulness, pack-roundtrip, and nonfinite failures | 0 |

The distinction between occupied-cell stages and actual lookup calls matters: branching at the first active cell creates another `23,328 = 96 x 243` lookup invocations at the second cell.

## Numerical factor and packed comparison

For all three axial components:

- numerical Schmidt rank at relative cutoff `1e-12`: `9`;
- ninth-to-first singular-value ratio: about `5.55998e-11`;
- all-axis spectrum disagreement: `6.77236e-15`;
- factor-versus-packed L2 residual: `4.15e-20` to `4.65e-20`;
- factor-versus-packed residual divided by the ninth singular value: below `8.37e-10`;
- factor norm residual: at most `1.42109e-14`;
- stream Gram residual: `1.11026e-16`;
- packed joint norm residual: at most `2.96230e-12`;
- maximum reported technical residual: `2.96230e-12`, below the inherited `1e-8` ceiling.

The packed comparator ceiling is `1e-12` and it separately requires `L2/s9 <= 0.1`. Thus it cannot pass while omitting the ninth Schmidt direction. The SVD is diagnostic only: all nine columns and singular values are retained and discarded norm is zero.

## Covariance, CAR, and preservation

The prefix gates the physical-law ingredients under all 24 proper-cubic frames:

- Cycle-219 coin covariance residual: `0`;
- local collision-generator covariance residual: `0`;
- six-direction emitter carried-covariance residual: `0`;
- finite-stream covariance failures: `0`;
- collision generator and axis-block Hermiticity residuals: `0`;
- axis-block commutator maximum: `0`.

A separate 12-case global-CAR fixture covers three axes, forward and Hermitian-conjugate hops, and spectators in earlier and later cells. Generator sign, full N=2/Q=6 reconstruction, independent stream target, manual packing, and unpacking all pass with zero failures.

The inherited one-particle mass fixture remains unchanged, with maximum residual `4.44089e-16`. Contact is identity for N<=1 and the collision generator is identity for Q=0. The execution-touched collision components have maximum size `2`; the exhaustive N<=2, Q<=6 preservation scan has maximum component size `4`. The former is not a global bound.

## Resource and quarantine result

- elapsed wall time: `366.125642 s`;
- maximum RSS: `623,607,808 B`;
- process swap count: `0`;
- resource wall: none;
- response rows: `0`;
- held rows: `0`;
- science rows: `0`;
- occupation/bond fields: `0`;
- state hashes: `0`;
- classifier, selector, and refit: false.

The raw transcript is preserved byte-for-byte. Its NumPy count leaves were serialized as strings by `default=str`; the separate typed receipt normalizes selected counts to JSON integers and records both source hashes. This serialization issue does not affect the in-process numerical gates.

Wall time and RSS are embedded process measurements from monotonic time and `getrusage`; the wrapper separately records exit code zero. No independent external wall-clock corroboration was collected.

## Supplied structure inventory

Cycle 512 still imports rather than derives:

- the L15 size, N=2 matter sector, and Q=6 mediator sector;
- the `rho_AB3` packet, middle beta, Cycle-219 coin family, and contact coupling;
- the source cells, inward directions, emitter/collision angle, and frozen update order;
- the finite boundary law and physical seven-M2 local receiver alphabet;
- the two update-2 active cells for each axial preparation;
- the unexecuted updates-3–5 no-collision stored-key counts and the `128 B/key` host-layout estimate used only for the counterfactual flat projection;
- numerical cutoffs and host resource ceilings;
- the exact-decimal interpretation `0.37=37/100` and Lindemann–Weierstrass theorem import;
- the Cycle-511 observable, free, deletion, occupation/species, preservation, and authorization contracts.

Still open at law level are beta/species selection, source/current selection and rate, protection and stability, the parity-carrier or local superselection mechanism of a complete physical-M2 compiler, a bridge from update order to derived causal time, and the bridge from this technical state prefix to a response/prediction row.

## No-Go Discipline N1–N8

No representation-independent negative passes.

### N1 — normalized alternatives

Every family below is normalized as `(object or formulation; mechanism or invariant; terminal obligation)`. Any open terminal obligation forces the broad no-go gate to fail.

| Family | Normalized object / mechanism / terminal obligation | Honesty marker | Evidence and exact gap |
|---|---|---|---|
| Flat packed joint map | Canonical joint amplitude dictionary; in-core exact aggregation; complete updates 3–5 under the frozen caps | **ATTEMPTED through update 2; update 3 only counterfactually projected — OPEN** | Current raw transcript and typed receipt. No interacting update-3 state exists. |
| Factor-Schmidt | Matter/mediator product factors; local operator-Schmidt gates with every direction retained; complete update 3 and then depth 5 with inverse/covariance controls | **ATTEMPTED through update 2 — OPEN** | Current receipt positively closes update 2 at nine factors; no update-3 rank/resource result. |
| Coherent branch DAG | Shared coherent history graph; memoized recombination without branch deletion; complete the same sentinel and prove equality | **UNATTEMPTED in Cycle 512 — OPEN** | Current receipt lists the route as open; Cycle 478 supplies only a mechanism echo for bounded exact sharing, not this state. |
| Charge-aware tensor network | U(1)-sector spatial tensor state; exact charge blocks and untruncated rank accounting; reproduce the complete sentinel | **UNATTEMPTED — OPEN** | No Cycle-512 tensor evaluator or route-matched residual exists. |
| Heisenberg/reduced observable | Backward local observable or reduced state; telescoping/locality plus an equivalence proof; reproduce observable, free, deletion, and inverse obligations | **UNATTEMPTED — OPEN** | No Cycle-512 observable-only equivalence proof exists. |
| Exact reachable configurations | Only analytically reachable joint configurations; exact-zero aggregation and no magnitude pruning; establish actual update-3/depth-5 support and resources | **UNATTEMPTED beyond update 2 — OPEN** | `HARDCORE_GLOBAL_Q2_MEDIATOR_CYCLE331_NOTE_2026-07-18.md` is a positive smaller-Q mechanism echo, not a Q6/L15/depth-5 result. |
| Out-of-core/distributed exact map | Sharded keyed amplitudes; external exact sort/reduce; complete depth 5 while retaining per-process caps and determinism | **UNATTEMPTED — OPEN** | No Cycle-512 external-memory or distributed evaluator exists. |

N1 therefore fails every representation-independent negative.

### N2 — wall independence

The declared counterfactual flat projection supplies one compound host wall: full Cartesian materialization plus complex-amplitude storage plus the frozen 3 GB cap. Key count and per-entry layout are not independent physics walls. Runtime, factor growth, and substrate content are separate questions and were not closed negatively.

### N3 — hidden conditions

The `190,156,800` update-3 count is a declared no-collision Cartesian reference, not propagated interacting support. The `128 B/key` value is a host-layout estimate. Update number is a schedule index, not physical time. No-pruning and in-core storage are representation choices. The exact-support theorem import and exact-decimal interpretation are now explicit.

### N4 — residual matching

The flat update-3 estimate does not match an actual update-3 state, a depth-5 resource receipt, or a substrate obstruction. Conversely, the update-2 factor state matches the actual packed update-2 vector at L2 below `4.66e-20`.

### N5 — rhetoric

Admissible: for one axial component, the declared counterfactual no-collision update-3 flat plan has `46,425 x 4,096 = 190,156,800` slots. Complex128 values alone require `3,042,508,800 B`, exceeding both the `3,000,000,000 B` RSS ceiling and `2,700,000,000 B` preallocation gate. Thus only that full in-core materialization is ineligible. The `24,340,070,400 B` packed figure is a `128 B/entry` estimate, not measured RSS. Inadmissible: Route C is infeasible, the interacting update-3 state exceeds 3 GB, depth 5 cannot close, or the substrate requires another axiom.

### N6 — partial closure

The nine-factor prefix is a direct partial-closure path. It retires full packed update-2 materialization as a necessary representation and makes update-3 factor growth the next constructive obligation.

### N7 — hostile steelman

A hostile reviewer can now point to the successful factor representation: `5104 x 9` and `1296 x 9` factors reproduce a `3,626,856`-key packed state with no truncation. The concrete counter-route is to propagate all nine factors through update 3 with a generic exact local low-operator-Schmidt block expansion, retain every singular direction, and establish update-3 rank/resource/inverse/covariance before attempting the depth-5 terminal obligation. Any broad resource negative that ignores this live counter-route is false.

### N8 — cross-cycle echo

- `HARDCORE_GLOBAL_Q2_MEDIATOR_CYCLE331_NOTE_2026-07-18.md`: a projection-specific failure was repaired by an explicit covariant collision-conditioned completion, and reachable Q2 support was much smaller than ambient support. That reopen mechanism remains live; it is not a Q6 proof.
- `PHYSICAL_BORN_SUPPORT_NINE_MIXED_QUOTIENT_AUXILIARY_CYCLE478_NOTE_2026-07-19.md`: an inherited coordinate-overflow/resource estimate was retired by a bounded `126 x 9` allocation and exact-sharing DAG without changing the science row. Bounded DAG sharing remains a live algorithmic remedy here.
- `DISTINGUISHABLE_ANTISYMMETRIC_FOCK_COMPILER_CYCLE239_NOTE_2026-07-17.md`: a route-specific bounded-resource miss left local gauge/occupation compression explicitly open and forbade a constitutional conclusion. That compression mechanism remains open.
- `PHYSICAL_ROUTE_C_LOCAL_SEVEN_MODE_RECEIVER_CYCLE510_NOTE_2026-07-20.md`: the bounded local physical Q6 receiver is positive while the global compiler remains open. Cycle 512 extends this only through update 2.
- `PHYSICAL_ROUTE_C_RESPONSE_REVISION4_PREFLIGHT_CYCLE511_NOTE_2026-07-20.md`: resource feasibility and the actual response sentinel were explicitly frozen-unexecuted; Cycle 512 closes only the update-2 prefix.

These echoes all force the same disposition: local implementation failure or one representation wall is not shared-substrate evidence.

No shared substrate obstruction, minimum-content result, or axiom pressure follows.

## Three-route disposition

1. Direct local-even-CAR encoding: bounded local algebra and mass/contact fixtures remain positive, but global parity/superselection and scale closure remain open.
2. Local gauge/auxiliary encoding: strongest route. The physical seven-M2 receiver, explicit local hard-core/charge sectors, all-24-covariant collision/emitter/stream ingredients, and the update-2 nine-factor prefix are constructive. A derived auxiliary constraint law, depth 5, and the complete compiler remain open.
3. Staggered/time-multiplexed encoding: not exercised by Cycle 512. The frozen host update word remains supplied; no schedule has been compiled into physical M2, no schedule variable is promoted to physical time, and no depth-5 staggered compiler has been shown.

A route-specific open wall is not constitutional evidence.

## Dependency-ledger effect

- `C_ref`: unchanged; reference/frame supply remains explicit.
- `C_num`: exact pre-collision support and conditional post-collision support/cancellation semantics are now controlled; the parity/superselection import remains.
- `C_wrap`: unchanged; update order remains a host schedule, not derived time.
- `C_int`: materially advanced through the first physical Q6 entangling layer; contact/source selection, rate, and protection remain open.
- `C_local`: narrowed from generic state-size concern to update-3 factor-growth and complete physical-M2 compiler obligations.
- `C_source`: update-2 host-resource feasibility is closed only for this frozen L15/Q6 prefix and implemented factor algorithm; the actual response/current-source law and depth-5 sentinel remain open.

## Optimal next campaign

Cycle 513 should propagate the nine-factor state through update 3 without allocating the counterfactual flat Cartesian map. It should:

1. replay the complete Cycle-512 prefix and require the existing ledger, factor/packed comparison, and spectrum before enabling update 3;
2. apply the full update-3 geometry, or prove a conservative support-derived cell set equivalent to it, without introducing a physical selector or state-dependent law;
3. replace the special update-2 `I/D/X` form with a generic local matrix-unit/block decomposition, include lawful size-four collision components, and validate it exhaustively against every local N<=2, Q<=6 lookup state;
4. retain every structural factor during propagation, perform no SVD or magnitude truncation, and record raw factor growth plus diagnostic numerical ranks at `1e-10`, `1e-12`, and `1e-14`;
5. perform QR/core analysis, norm and inverse checks, forward/reverse computational cell-order comparison, and rotated-axis spectrum/covariance checks with every singular direction retained;
6. compare against a bounded exact reachable-state slice or independently checkable reduced observable;
7. stop before any response/train/held execution unless a new fail-closed review authorizes that surface.

The decisive next question is whether rank growth remains controlled at update 3. That is an unfinished constructive implementation question, not a demonstrated shared obstruction.

## Artifacts

- runner: `scripts/physical_route_c_q6_factorized_resource_scout_cycle512_2026_07_20.py`
- raw authorized transcript: `outputs/physical_route_c_q6_factorized_resource_scout_cycle512_2026_07_20.log`
- typed receipt: `outputs/physical_route_c_q6_factorized_resource_scout_cycle512_receipt_2026_07_20.json`

Hashes before packaging commit:

- runner: `d90525f7c25c92762851ac07b9ea58c28123c378fd0fdea6ce3ab565108834fe`
- raw transcript: `203a24590329119b44ce13f2c3c39581f011457cd4db217e62c3f985ea840f67`
- typed receipt: `40de95deab66e3d32113d1f91cb14d9a1ac92e96fc7cae27b2ea87c56980b983`
