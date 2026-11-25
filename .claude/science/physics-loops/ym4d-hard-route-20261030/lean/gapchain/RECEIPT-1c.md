# Repo search

The lead's November 8 digest searched main and PRs 10114, 10133, 10134 and 10141. I checked the Dirichlet Maxwell law and equal-side finite-clock Villain geometry on main `8b11ae2bb95e` and the Haar one-step plaquette witness on PR 10114 (lines 106–149). The first two concern different measures. The witness uses the positive convolution for a specific correlation. A targeted search of Lean files outside this lane at the refreshed five heads found no matching transfer or Hilbert–Schmidt declaration. The row-specific prior file is absent. The open registry has no competing entry for this Lean construction. [Lead digest](../../library/prior/repo-search-2026-11-08.md)

At the checkout pin `dad112a12358caddf076f980fabb86fc633d9fa2`, row 1504 already gives SU(2), Haar normalization, the rectangular partition function and the spectral consumer. Its kernel formula fixes which side the temporal gauge acts on. Claude Opus 5.5 wrote the hand construction in row 667, §§A0 and 2.2–2.4, and extended it to unequal sides in row 698, Lemma 1.1. Claude Fable 5.2 wrote row 697's spectral design. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the cubic transfer construction. The outline index led to the finite-volume definitions (240–278) and the cubic gauge projection and trace (2315–2335). CA-I 447–483 fixes the normalized plaquette action. Their half-convolution sandwich and the hand lemma's half-spatial-action sandwich place the factors in different orders. [Row 667](../../library/gap-transfer.md) · [Row 698](../../library/gap-seed-check.md) · [Stage 1b](RECEIPT-1b.md) · [Cubic GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335)

This is research work. Row 1506 confers no scientific status.

## Outcome

**BUILT.** For every box with three spatial periods at least 3 and every β > 0, `GapChain.Wilson.transfer_boxSpectrum` applies row 1504's spectral theorem to the gauge-averaged Wilson operator on the full complex spatial-link Haar L² space. The returned top is the operator norm. The enumeration includes every positive eigenvalue with its eigenspace multiplicity, and the weights for a ≥ 3 are the corresponding power sums. [Lean proof](GapChain/Transfer.lean)

| Result | Lean declaration | Scope |
| --- | --- | --- |
| Bounded integral operator | `Kernel.operator_apply`, `Kernel.operator_congr`, `Kernel.operator_norm_le` | For a square-integrable scalar kernel on a probability space, the output is its ordinary row integral almost everywhere. Product-almost-everywhere changes of kernel preserve the operator. Its norm is at most the product L² norm. |
| Hilbert–Schmidt bound and compactness | `Kernel.operator_hs`, `HSNormLE.isCompact`, `Kernel.operator_compact` | Every finite orthonormal family satisfies the sum-of-squares bound. Finite-rank truncations in an arbitrary Hilbert basis converge in operator norm. |
| Adjoint | `Kernel.pairing`, `Kernel.operator_adjoint`, `Kernel.operator_selfAdjoint` | The adjoint has kernel $(x,y)\mapsto\overline{k(y,x)}$. An almost-everywhere Hermitian kernel gives a self-adjoint operator. |
| Wilson formula | `Wilson.transferKernel_apply`, `Wilson.transfer_apply` | Each positive spatial edge carries normalized SU(2) Haar. The integral uses one independent temporal gauge variable per vertex, with one half of the spatial action at each endpoint. |
| Positivity and nonvanishing | `Wilson.transfer_positive`, `Wilson.transfer_ne_zero` | The operator is positive for β ≥ 0. For any real β, the strictly positive kernel sends the constant-one input to a function positive almost everywhere. |
| Compactness and explicit bound | `Wilson.transfer_compact`, `Wilson.transfer_hs` | The operator is compact at every real β. At β ≥ 0 it satisfies `HSNormLE (transfer β R) 1` on the full slice space. |

### Proof details

For almost every x, the conjugate kernel row is an L² vector. Its inner product with f represents the row integral. Bessel's inequality on that row gives the finite-family inequality after integration in x. Fubini applied to the kernel times the two test functions gives the adjoint identity. For compactness, the error of truncating the input basis expansion is bounded by the square root of the omitted column mass. This proof allows a nonseparable Hilbert space.

For the Wilson kernel, the real trace of a link product is a dot product of real and imaginary matrix entries. The exponential series therefore approximates the temporal kernel uniformly by finite sums of kernels $f(u)f(v)$ with real continuous f. Independent Haar averages at the two endpoints send each such kernel to another of the same form, including the two spatial half-weights. The corresponding rank-one operator is positive. Closedness of the positive cone gives the limit. Simultaneous gauge invariance and a left translation of the second gauge variable identify this construction with the single temporal-link integral. The pointwise bound $0<K_R\le1$ yields the constant 1 because product Haar has mass one. [Matrix and gauge proofs](GapChain/Transfer.lean) · [Hand construction](../../library/gap-transfer.md) · [CA-I action conventions](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L447-L483)

### Verification and trusted base

The default Lake target built with warnings treated as errors. A separate consumer imported the compiled module. It checked almost-everywhere kernel congruence, all four operator properties at β = 2 on the unequal box (3,4,5), the top and fifth power sum of that same operator, and the pointwise identity $K_R=1$ at β = 0. These are kernel-checked symbolic examples. Equality with the four-dimensional periodic partition integral and the physical gap seed are open.

The Mac mini Codex launcher selected `gpt-6.2-astra` with reasoning effort `max`. Proof checking used Lean 4.33.1 at `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, Mathlib at `0df444a360eaa60ab8c11dca51a86af692955474`, the pinned compiled package environment and the four existing gap-chain sources. Every new theorem's axiom report is reproduced below. The build used ordinary kernel proof terms throughout. A source scan found zero occurrences of `sorry`, `admit`, `axiom`, `native_decide` and `implemented_by` as standalone tokens. The four dependency sources were byte-compared with the git blobs at `dad112a12`. The delivered module and lakefile.toml were byte-compared with their tested copies.

Verified source SHA-256 is `4632ca88bc2345004cf2eecd8e581ab5e34cec817d401d252f7bfd30b17fa240` for Transfer.lean and `239b4cf4903499c54d206823daec2b37986ac85ff08465a8493d206ddef9d9c1` for lakefile.toml. The source downloads at Sussman–Alpoge revision `31a47c543775` and the complete raw run logs are in `/private/tmp/sa-lean-gap-chain-stage1c-astra62.zlcaV6`.

## Saved plan and build history

The receipt was created at 01:09:54 UTC on November 25. The saved plan was to check prior coverage, build the analytic operator, specialize it to the rectangular kernel, and verify the axiom inventory and spectral consumer. The initial source draft was saved before a full build could begin.

- The first eligible standalone compiler rebuilt SequenceLemma. The runner then switched to the normal Lake target and serialized its compiler children.
- `lake-01` rebuilt the pinned dependencies and exposed representative coercions, product-measure names, and the norm estimate for the averaging map in Transfer.
- `lake-02` checked the general integral and adjoint formulas, compactness and the finite-family inequality, along with Wilson nonvanishing and the bound 1. Corrections addressed product-null-set congruence, factorization of the averaged rank-one kernel, continuity of the matrix entries and the temporal product display.
- `lake-03` checked all 52 declarations with the standard axioms. Lake failed its warnings-as-errors check on three unused section instances for `sandwich_gram`. The next input omitted them.
- `lake-default` exposed the same newly unused Borel-space assumption in the theorem consuming `sandwich_gram`. The final source removes the redundant assumption from that section.
- `lake-final` built all five library roots. `consumer` checked the imported declarations and the examples above.

Each independent build or consumer began after a fresh system-wide free-memory reading of at least 50%. All ran under `/usr/bin/nice -n 10` with `LEAN_NUM_THREADS=2`. A scratch copy of the pinned Lake binary selected a wrapper that serialized and timed its compiler children. The children inherit the build's niceness. Their start readings below record memory conditions within the active build. A Darwin sandbox denied writes to the shared packages during Lake builds. The scratch manifest resolved the existing package cache.

Darwin `/usr/bin/time -l` measured elapsed wall time, maximum resident set size and peak memory footprint. The process peaks do not add. The first shell-level version query selected the machine default 4.36.0 and lacked isolated resource counters. A timed repeat measured the same executable. All proof compilations used 4.33.1 and have individual counters.

| Version query | Wall (s) | Maximum RSS (bytes) | Peak footprint (bytes) |
| --- | ---: | ---: | ---: |
| Default repeat, 4.36.0 | 1.07 | 51298304 | 10781392 |
| Pinned, 4.33.1 | 0.14 | 50987008 | 11272960 |

Elapsed time from the first saved plan to the end of the successful consumer was 1 h 16 min 35 s, including the memory waits.

### Build and consumer invocations

| Invocation | UTC start | Free | Exit | Wall (s) | Maximum RSS (bytes) | Peak footprint (bytes) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| base-SequenceLemma | 01:31:05 | 52% | 0 | 27.65 | 2237661184 | 483629544 |
| lake-01 | 01:49:12 | 51% | 1 | 184.38 | 2675687424 | 249798808 |
| lake-02 | 01:53:54 | 52% | 1 | 40.36 | 2419671040 | 204283864 |
| lake-03 | 01:57:59 | 50% | 1 | 41.39 | 2470002688 | 206233560 |
| lake-default | 02:19:28 | 50% | 1 | 90.29 | 2137522176 | 217391136 |
| lake-final | 02:22:29 | 50% | 0 | 64.19 | 2382495744 | 206643112 |
| consumer | 02:25:56 | 52% | 0 | 33.30 | 2393751552 | 507690864 |

### Lean compiler children of Lake

| Invocation | UTC start | Free | Exit | Wall (s) | Maximum RSS (bytes) | Peak footprint (bytes) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| lake-TheoremS-31784 | 01:49:20 | 39% | 0 | 26.54 | 2201272320 | 877960136 |
| lake-LemmaM1-31805 | 01:49:47 | 37% | 0 | 42.45 | 2091139072 | 517802256 |
| lake-Wilson-31988 | 01:50:29 | 36% | 0 | 50.40 | 2242117632 | 595443472 |
| lake-Transfer-32100 | 01:51:20 | 42% | 1 | 56.52 | 2675687424 | 622362576 |
| lake-Transfer-32932 | 01:54:02 | 42% | 1 | 32.15 | 2419671040 | 626819144 |
| lake-Transfer-33954 | 01:58:06 | 40% | 0 | 34.80 | 2470002688 | 643497840 |
| lake-SequenceLemma-41198 | 02:19:34 | 40% | 0 | 36.70 | 2137522176 | 486824352 |
| lake-Transfer-41204 | 02:20:10 | 37% | 0 | 47.49 | 2102657024 | 637435880 |
| lake-Transfer-42081 | 02:22:36 | 40% | 0 | 56.95 | 2382495744 | 640958440 |

## Verbatim axiom reports

The final consumer printed these lines from the imported module.

~~~text
'GapChain.Kernel.norm_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.norm_sq_toLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.sections' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.row_inner' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.row_norm_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.integrable_row_norm_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.integral_row_norm_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.row_inner_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.row_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_norm_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_congr' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_hs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.outer_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.pairing' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.adjKernel_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_adjoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_selfAdjoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.HSNormLE.isCompact' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_compact' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.realOperator_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.realOperator_gram' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.FiniteGram.mul_atom' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.FiniteGram.mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.FiniteGram.const' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.FiniteGram.pow' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.FiniteGram.smul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.FiniteGram.sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.FiniteGram.exp_mem_closure' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.sandwich_gram' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.positive_sandwich' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.continuous_spatialAction' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.spatialAction_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.gauge_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transferKernel_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.halfTrace_conjugate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.temporal_gauge' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transferKernel_eq_sandwich' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.halfTrace_mul_inv_entries' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.continuous_entry' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.score_gram' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.temporal_eq_exp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.temporal_gram_closure' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transferKernel_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transfer_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transfer_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transfer_compact' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transferKernel_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transferKernel_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transfer_hs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transfer_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.transfer_boxSpectrum' depends on axioms: [propext, Classical.choice, Quot.sound]
~~~

## Next two proposed rows and their decisive outcomes

1. **Cyclic kernel integral and spectral power sum.** Prove the L² kernel composition and Hilbert–Schmidt pairing needed for the periodic product of $a$ copies of $K_R$. The decisive result is a Lean equality between this cyclic integral and the multiplicity-weighted positive-eigenvalue sum of `Wilson.transfer β R` for every valid R and a ≥ 3.
2. **Periodic Haar factorization and the Wilson Stage 1 instance.** Construct the measure-preserving reindexing of four-dimensional links into time-indexed spatial slices and vertex gauges. Split the spatial action, integrate each temporal layer, and identify `Wilson.Z β a R` with the cyclic integral. The decisive result is the unconditional weight equality on valid boxes and a Wilson `TorusData` assembled using `fields_of_bridge` and row 1503's weight log-convexity proof. The physical seed estimate remains open.
