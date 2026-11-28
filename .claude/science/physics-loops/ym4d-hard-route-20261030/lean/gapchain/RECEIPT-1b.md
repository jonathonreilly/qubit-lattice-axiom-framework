# Repo search

The lead's November 8 digest covered main and PRs 10114, 10133, 10134 and 10141. I checked the main finite-clock Villain result (equal even sides), the Dirichlet Maxwell covariance result, the open temporal-gauge slab result, and PR 10114's one-step Haar plaquette witness. Each uses a different measure, geometry or observable. A fresh content search on main `8b11ae2bb95e` and those PR heads found no Wilson, Haar-measure, transfer-operator, `TorusData` or `BoxSpectrum` symbol in their 12 distinct Lean files outside the lane. The pinned lane has exact quaternion moment arithmetic, the Stage 1 abstract theorem and the rectangular hand proof. The row-specific prior is absent. The registry search found no competing owner for the untwisted Lean construction. [Lead digest](../../library/prior/repo-search-2026-11-08.md) · [Stage 1 check, Steps 2 and 6](../../library/lean-gap-chain-stage1-check-opus.md)

## Outcome

**BUILT (A)–(C).** At fixed `β > 0`, `Z β a R` is the integral over one normalized SU(2) Haar variable for every positive link. The four periodic coordinates have lengths `a, R.x, R.y, R.z`. For the exchanged lengths a and b and spectator lengths s₁ and s₂, the module proves `log Z ≥ −6 β a b s₁ s₂`. The exported results are in `GapChain.Wilson`. [Wilson.lean](GapChain/Wilson.lean)

| Item | Kernel-checked result |
| --- | --- |
| A | `SU2` is Mathlib's determinant-one unitary subgroup of complex 2 × 2 matrices. The whole compact group normalizes the one-link Haar measure. `action_eq_geometric` gives one term `1 − Re tr(Uₚ)/2` for each vertex and pair of directions i < j. `integrable_density` proves integrability of the exponential and `Z_bounds` gives `0 < Z ≤ 1`. |
| B | `measurePreserving_relabel`, `faceTrace_relabel` and `action_relabel` transport links, faces and their weights under any permutation of the four axes. `partition_permute` transports the integral and `cross` specializes it to the time axis and a chosen spatial axis. Reversing a face takes the inverse transport and preserves its real trace. |
| C | `integral_faceTrace` uses multiplication by −I on the first edge of a face. A side of length at least two makes that edge distinct from its opposite. `mean_action` gives Haar mean `6 × number of sites`. The exponential Jensen inequality `jensen` then yields `log_lower` with `d = −6 β × spectatorArea R i`. This single d works for all a,b ≥ 3. |
| Stage 1 interface | `fields_of_bridge` has the exact quantifiers of `TorusData.cross` and `TorusData.lower`. Its hypothesis equates the proposed spectral weights with the integrals on valid boxes and time lengths only. |
| D, spectral component | For a nonzero compact positive operator with a finite `GapChain.HSNormLE` bound on a complex Hilbert space, `boxSpectrum_of_operator` supplies a `BoxSpectrum` whose top is the operator norm and whose weights equal the sums of eigenvalue powers for a ≥ 3. Every positive eigenvalue contributes its full eigenspace dimension. One maximal slot contributes the explicit 1 in the normalized weight. |

The remaining Wilson obligation is to construct the positive rectangular slice operator with the required Hilbert–Schmidt bound and identify its spectral power sums with these particular Haar integrals. The physical seed remains open. This is a research build and grants no audit status.

## Hand sources and normalization

Claude Fable 5.2 wrote row 697 §1 and §3.4 and the W3/W10/R4 design. Claude Opus 5.5 wrote row 667, row 698 Lemma 1.1 and the row 1503 check. Codex wrote the Stage 1 Lean consumer. Here the action counts six geometric plaquettes per site, the Boltzmann factor is `exp(−β S)`, and the intended transfer trace includes every flux sector. [Row 697](../../library/gap-crux-restate.md) · [Row 698](../../library/gap-seed-check.md) · [Row 667](../../library/gap-transfer.md) · [Design](../../library/lean-gap-chain-design-fable.md)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the finite-cutoff conventions, the orientation argument and the cubic transfer design. I followed the outline index (chunks 01/02, their neighbouring rows and obligations) to the definitions and GL8 and checked the corresponding CA-I passages. Both source files were fetched once at `31a47c543775` into the fresh scratch directory below. [Finite-volume definition and bounds](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L240-L278) · [Cubic GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [CA-I action](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L447-L483) · [CA-I invariance](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L559-L597)

## Spectral bridge at Mathlib `0df444a360ea`

For a rectangle R, take X to be SU(2) on the positive spatial links with product Haar probability. Row 698, Lemma 1.1, extends row 667's transfer kernel to X. The kernel averages the one-step temporal weight over vertex gauges and places half the spatial potential at each end. The top and all multiplicities must refer to this same operator. In the cubic release, the lane design identifies `CubicPeriodSublattice.transfer`, `TransferProperties`, `PartitionFunctionEqTrace`, `KernelCycleTrace.Statement`, `IsHilbertSchmidtPW` and `tracePW`. These are release identifiers. The table gives Mathlib and lane identifiers available to the Lean build.

| Component | Exact declarations at the pin | Status and remaining proof |
| --- | --- | --- |
| Slice L², kernels and Fubini | `MeasureTheory.Lp`, `MeasureTheory.L2.inner_def`, `MeasureTheory.L1.integralCLM'`, `MeasureTheory.integral_prod`, `InnerProductSpace.rankOne` | The library has the Hilbert space, scalar integration and product integration. A rectangular kernel still needs a bounded map on L², independence of representatives, an L² norm estimate and the adjoint identity. |
| Compact and positive operators | `IsCompactOperator`, `IsCompactOperator.comp_clm`, `IsCompactOperator.clm_comp`, `isCompactOperator_of_tendsto`, `ContinuousLinearMap.IsPositive`, `ContinuousLinearMap.IsPositive.isSelfAdjoint`, `ContinuousLinearMap.isSelfAdjoint_iff_isSymmetric` | Row 667 §2.2 supplies a positive finite-rank approximation of the one-link convolution. Lift the kernel to the slice, justify convergence in operator norm, and implement the gauge average and the two spatial multipliers. Operator positivity needs the positive factorization or an equivalent quadratic-form proof. |
| Compact spectral theorem and top | `IsCompactOperator.hasEigenvalue_iff_mem_spectrum`, `LinearMap.IsSymmetric.orthogonalFamily_eigenspaces`, `ContinuousLinearMap.orthogonalComplement_iSup_eigenspaces_eq_bot`, `ContinuousLinearMap.finite_dimensional_eigenspace`, `CStarAlgebra.norm_mem_spectrum_of_nonneg` | The pin proves density of compact self-adjoint eigenspaces on a complete Hilbert space and finite dimension for each nonzero eigenvalue. The zero eigenspace may be infinite-dimensional. `compact_eigenblocks` builds the Hilbert sum using `IsHilbertSum.mkInternal`. `IsHilbertSum.linearIsometryEquiv` and `HilbertBasis.hasSum_repr` expose the associated expansion APIs. `positive_top_eigenvalue` proves attainment and strict positivity of the top for the nonzero positive operator. |
| Multiplicity and normalization | `LinearMap.IsSymmetric.eigenvalues`, `LinearMap.IsSymmetric.eigenvectorBasis`, `LinearMap.IsSymmetric.card_filter_eigenvalues_eq`, `stdOrthonormalBasis`, `eigenvalue_nonneg_of_nonneg`, `spectrum.norm_le_norm_of_mem` | The sorted list and its counting identity assume a finite-dimensional whole space. Here `PositiveSlot` takes every positive real eigenvalue with one index per basis vector of its eigenspace. `nonzero_eigenvalue_has_slot` assigns a positive slot to every nonzero eigenvalue of the compact positive operator. `boxSpectrum_of_operator` proves square summability, countability, and convergence of every required power sum. It exposes an injection into ℕ, sets the chosen top slot and unused indices to zero and divides each remaining eigenvalue by the top. Further copies of a repeated top become ratios of one. |
| Hilbert–Schmidt and trace class | `GapChain.HSNormLE`, `GapChain.hsSq` (Stage 1), `LinearMap.trace`, `LinearMap.trace_eq_matrix_trace` (Mathlib) | `HSNormLE` bounds finite sums of squared norms over orthonormal families. `hsSq` gives the corresponding sum on a Hilbert basis. The algebraic trace uses a finite basis and returns zero in its absence. I found no pinned Mathlib interface from an L² scalar kernel to a Hilbert–Schmidt operator and its norm identity, or from an infinite-dimensional positive trace-class operator to its analytic trace. The one-step trace-class claim in row 667 §§A0–A2 and 2.2–2.4 uses a Gram factorization. |
| Cyclic Haar integral to the spectral sum | `MeasureTheory.integral_prod`, `GapChain.Wilson.partition_permute`, `GapChain.Wilson.boxSpectrum_of_operator` | The unresolved equality has two parts. Split the torus links into spatial layers and temporal vertex variables, then integrate the latter to obtain the cyclic integral of the same rectangular kernel. Identify that integral with the eigenvalue power sum for each integer time length a ≥ 3. This last equality discharges `fields_of_bridge`. |

The missing equality can be stated on these exact link variables. For a positive spatial link e from x to y, write Uₑ and Vₑ for its values in successive layers, gₓ for the time link at x, and Sₛ for the spatial plaquette action of a layer. The candidate kernel from the hand construction is

```math
K_R(U,V)=e^{-\beta(S_s(U)+S_s(V))/2}
\int\prod_{e:x\to y}\exp\!\left[-\beta\left(1-\tfrac12\operatorname{Re}\operatorname{tr}(g_x V_e g_y^{-1} U_e^{-1})\right)\right]\,dg .
```

Here dg is product Haar probability on the spatial vertices. Each time-like plaquette occurs in one factor and each spatial plaquette receives two half-weights in a periodic cycle. For positive β, the pointwise bounds put the candidate kernel's L² norm at most one. This supplies a target for the operator estimate once the kernel-to-operator inequality is proved. The proposed interface equates the cyclic integral of these kernels to the sum of the a-th powers of the positive eigenvalues with multiplicity.

**Size of the remaining bridge.** Three proof units remain after the eigenvalue enumeration. The general analytic unit is the L² kernel estimate, composition and Hilbert–Schmidt pairing, which can be developed first on finite sums of tensor products and extended by density. The Wilson-specific unit constructs the rectangular positive nonzero operator, proves compactness and provides its numerical Hilbert–Schmidt bound. The last unit proves the periodic link decomposition and applies the analytic pairing to the one-step and (a−1)-step kernels. For a ≥ 3 this gives the power trace needed here without requiring a general one-step trace-class API. These are prospective proof obligations.

**First component built.** `boxSpectrum_of_operator` turns the stated analytic operator hypotheses into the exact Stage 1 spectral weight. Square summability follows by applying `HSNormLE` to the orthonormal family indexed by positive multiplicity slots. Countability follows from the support of that sum. With ratios in [0,1], the square-sum then dominates each power needed by Stage 1. `boxSpectrum_of_slots` isolates the reindexing and top removal so its finite and repeated-top cases can be tested directly. [Stage 1 definitions](GapChain/TheoremS.lean) · [Hilbert–Schmidt bound](GapChain/LemmaM1.lean)

## Plan, run history and trusted base

Row 1504 began on 2026-11-24 at 23:55 UTC at repository commit `068e3d55c1316c6e742301aea906e0a18bf0dd29`. The Mac mini runner identified the model as `gpt-6.2-astra` and its launcher set reasoning effort to `max`. The first receipt recorded the plan to define normalized Haar on the four-period box, prove axis exchange, compute the mean action for Jensen, and size and build the first spectral component. The toolchain was Lean 4.33.1, commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, with the pinned Mathlib `0df444a360eaa60ab8c11dca51a86af692955474` and its manifest dependencies. The trusted base is the Lean kernel and the imported compiled environment from those pins, with the axiom dependencies printed below. The decision procedures for the finite identities produce proof terms checked by the kernel. The proof uses no numerical samples, native evaluator, user-declared axioms or admitted obligations.

The scratch project was built from the three committed Stage 1 modules with the shared package directory symlinked read-only. Every build used `LEAN_NUM_THREADS=2` under `/usr/bin/nice -n 10`. Each started after a fresh `memory_pressure` reading of at least 50%. The Lake and consumer jobs were serialized. The default target builds all four module roots. The consumer imports the compiled module, resolves the 30 declarations in the inventory, and checks four examples. It swaps the time length 5 and spatial length 7 in the unequal box (5,3,4,7), gets the spectator constant −72β, proves Z = 1 at zero coupling, and checks that the multiplicity list (2,2,1) leaves ratios 1 and 1/2 and has third power sum 17.

Darwin `/usr/bin/time -l` supplies elapsed seconds, maximum resident set size and peak memory footprint in bytes. The first table gives the whole invocation. The second gives every Lean compiler process separately, including failed attempts. Lake can replay prior modules in later runs. The two peak measures describe individual processes and are not additive.

| Run | UTC start (Nov 25) | Free | Command | Exit | Wall s | Max RSS B | Peak footprint B |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| 01-Wilson | 00:18:24 | 52% | target Wilson | 1 | 76.89 | 2,318,778,368 | 243,163,216 |
| 02-Wilson | 00:21:09 | 52% | target Wilson | 1 | 61.13 | 2,498,101,248 | 209,461,232 |
| 03-default | 00:23:28 | 50% | default build | 0 | 38.83 | 2,316,959,744 | 221,814,792 |
| 04-enumeration | 00:26:36 | 51% | default build | 1 | 47.57 | 2,362,195,968 | 208,166,872 |
| 05-default | 00:49:22 | 50% | default build | 0 | 44.33 | 2,367,635,456 | 207,069,144 |
| 06-consumer | 00:55:58 | 50% | consumer | 1 | 36.22 | 2,508,914,688 | 138,272,440 |
| 07-consumer | 01:01:12 | 52% | consumer | 0 | 29.95 | 2,584,674,304 | 139,763,432 |

The target command was `lake build +GapChain.Wilson:olean`. The default command was `lake --wfail build`. The consumer ran `lake env lean -DwarningAsError=true Inventory.lean` with the timed scratch Lean wrapper.

| Run | Lean input | Wall s | Max RSS B | Peak footprint B |
| --- | --- | ---: | ---: | ---: |
| Initial | Lean version | 0.08 | 50,561,024 | 10,830,568 |
| 01-Wilson | TheoremS.lean | 25.23 | 2,265,382,912 | 882,219,928 |
| 01-Wilson | Wilson.lean | 43.55 | 2,318,778,368 | 562,822,808 |
| 02-Wilson | LemmaM1.lean | 22.09 | 2,498,101,248 | 519,096,640 |
| 02-Wilson | Wilson.lean | 32.48 | 2,353,414,144 | 573,472,528 |
| 03-default | SequenceLemma.lean | 30.75 | 2,082,734,080 | 486,513,104 |
| 03-default | Wilson.lean | 30.68 | 2,316,959,744 | 592,936,696 |
| 04-enumeration | Wilson.lean | 40.66 | 2,362,195,968 | 581,926,744 |
| 05-default | Wilson.lean | 37.25 | 2,367,635,456 | 594,575,168 |
| 06-consumer | Inventory.lean | 32.00 | 2,508,914,688 | 503,070,576 |
| 07-consumer | Inventory.lean | 26.37 | 2,584,674,304 | 502,300,456 |

Run 01 located six elaboration errors in the first draft, including the determinant closed-set coercion, product cardinality and the eigenspace family for the Hilbert sum. Run 02 narrowed the remaining errors to a topology instance and the new spectral enumeration. Run 03 passed the complete default build with A–C and the spectral power-sum equality. Run 04 exposed one type-inference error while making the multiplicity injection public. Giving the padding function its explicit type ℕ → ℝ resolved it. The final default build checks the public enumeration as well as A–C.

Run 06 resolved all 30 inventory declarations and checked the three Wilson examples. Its repeated-top example left one concrete vector lookup in the proof of the ratio 1/2. The revised consumer evaluates that lookup by definitional reduction.

Run 07 passed all four examples with warnings treated as errors. It also printed the axiom reports below directly from the imported compiled module.

Complete inputs and logs are in `/private/tmp/sa-lean-gap-chain-stage1b-astra62.9NgCmG`, including `project/Inventory.lean`, `logs/runs.tsv` and the per-process `logs/lean.*` records. The built and delivered Wilson source has SHA-256 `71422003ba8a11cf2c5d5b040988822a09c388a4897c84e09fb050e2f5a4f5e0`.

## Verbatim axiom reports

The consumer printed the following lines from the compiled module.

~~~text
'GapChain.Wilson.continuous_halfTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.halfTrace_inv' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.halfTrace_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.halfTrace_centerMinus' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.halfTrace_reverse' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.action_eq_geometric' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.continuous_faceTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.continuous_action' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.integrable_density' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.partition_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.measurePreserving_relabel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.siteEquiv_step' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.faceTrace_relabel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.action_relabel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.partition_permute' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.integral_faceTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.mean_action' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.jensen' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.partition_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Z_bounds' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.cross' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.log_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.fields_of_bridge' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.compact_eigenblocks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.nonzero_eigenblock_basis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.positive_top_eigenvalue' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.boxSpectrum_of_slots' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.nonzero_eigenvalue_has_slot' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.boxSpectrum_of_operator' depends on axioms: [propext, Classical.choice, Quot.sound]
~~~

## Next two proposed rows and their decisive outcomes

1. **Rectangular Wilson transfer operator.** Construct the gauge-averaged one-step operator on the spatial Haar L² space with the split spatial potential. The decisive outcome is a Lean theorem proving positivity, nonvanishing, compactness and an explicit finite `HSNormLE` bound for every valid rectangle, so `boxSpectrum_of_operator` applies to that operator.
2. **Periodic kernel identity and Stage 1 instance.** Decompose the torus product Haar integral by time layer, integrate the temporal links and identify the resulting cyclic kernel integral with the positive eigenvalue power sum for all a ≥ 3. The decisive outcome is the rectangular Wilson bridge equality and a `TorusData` instance combining `fields_of_bridge` with the log-convexity theorem `Check1503.weight_logConvex` from row 1503, Step 5. The separate physical seed estimate remains open.
