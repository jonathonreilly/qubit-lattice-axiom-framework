# Repo search

The November 8 lead search found a one-step Wilson-loop correlation bound on PRs 10114 and 10133. I checked lines 106–149 on PR 10114 and the matching blob on PR 10133. It gives a positive finite-lattice correlation. Main’s Dirichlet Maxwell result bounds finite-volume covariance for a specified noncompact measure. Neither result transports the SU(2) volume-first witness. A Lean declaration search on main and PRs 10114, 10133, 10134, 10141 and 10144 found no match for the witness, purity and cutoff-dilation symbols. The registry’s unassigned FIRST-PASSAGE-OFFSETS concerns a bare-coupling offset. Row 1678, on this lane, selects the integer difference of cutoff indices and leaves the witness transport open. The target-specific prior file was absent. [Lead digest, §11](../../library/prior/repo-search-2026-11-08.md#11-w1w2w5-witness-matching) · [One-step bound](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649c/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L149) · [Main covariance result](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb9/docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md#L120-L145) · [Row 1678](RECEIPT-purio.md#next-row-and-decisive-outcome) · [Registry](../../library/open-registry.md#L217)

## Row 1679

**BUILT.** `GapChain.Offset.su2_fixed_observable_gap_of_infinite_passing` puts every chosen cutoff in the prescribed infinite passing set. It supplies all six release witnesses, proves the mass gap at the original physical side and proves uniqueness of the vacuum. The calibration $M,\delta$ precedes $g_0$, $\ell$ and $A$. The continuum witnesses may depend on all three. At each cutoff in $A$, every cube of side $\ell L^K$ must have Wilson neutral purity at least $457/625$ at time $\ell L^K/512$. This is a research result at `dae1fc8bdf007d604af4915705ec8a84a4d41278` and grants no audit status. [Offset module](GapChain/Offset.lean#L701) · [Witness definition](GapChain/Stage0.lean#L296)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the YM4 outline, complete account and Lean release. RF53 gives the finite change of variables, including the absence of a field-normalization factor. CA-I states its growing-volume conclusion along a subsequence. The release's tuned-sequence lemma makes the change at fixed torus size under a common tuning level. For the growing tori here, the proof uses RF53 at each side and at the bare inverse coupling from its original cutoff. The offset is common to the sequence. Lane row 1652 supplies the witness conjunction, rows 1654, 1658, 1667 and 1670 assemble the spectral implication, row 1676 gives its purity input, and row 1678 selects the offset. [RF53](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L22014-L22040) · [CA-I, Theorem 0(ii)](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2692-L2711) · [Tuned torus limit](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/LimitsOfATunedSequence.lean#L54-L81) · [Row 1676](RECEIPT-purity.md) · [Row 1678](RECEIPT-purio.md)

### Matching the two limits

Write $a=L^{-r}$ and $D_a f(x)=f(ax)$. For $K=J+r$, the passage side with exponent $m+r$ and the original side with exponent $m$ have the same number of lattice sites. Periodizing the scaled test gives exactly the dilation of the periodized original test. The equality of finite cumulants therefore holds at the same $\beta$ for each real test in each slot. The release’s state pushforward gives the identical substitution for smeared infinite-lattice cumulants. [Finite torus identity](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/DilationOfSeparatedTuples.lean#L167-L177) · [State dilation](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/Construction/InfiniteLattice/CopyOfAStateOnADilatedLattice.lean#L24-L52)

For a given passage state $\mu$, use its defining cubic tori, keep a subsequence with exponents exceeding $r$, subtract $r$ and use cubic weak compactness at $K$. The resulting original-mesh state $\nu$ is an actual subsequential volume limit. For every separated tuple of order at least two, the two sequences of finite cumulants agree term by term, and each converges to its respective state's cumulant. This identifies $\nu$ with the dilated $\mu$ on every cumulant used by the witness. Equality of measures on all gauge-field observables is unnecessary. The order of choices gives one state for all tests. [Cubic compactness and local convergence](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/Construction/InfiniteLattice/InfiniteVolumeLimitPointsOfTheTorusStates.lean#L36-L82)

Apply the release's frequent-passage theorem at $J$ and $\beta_j=\mathrm{betaAt}(L,M,K_j,g_0)$. A further common subsequence makes the outer torus exponents exceed $r$. Their reduced sides still tend to infinity. On those indices, both the original volume states and the growing original tori converge to $S'_n(X)=S_n(D_a X)$. The singleton-free moment–cumulant identity gives both centred-moment limits, including arities zero and one. [Passage export](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/ContinuumLimit.lean#L117-L165)

### Which clauses fix a scale

| Witness clause | Transport at $K=J+r$ |
|---|---|
| Calibration and both coupling limits | The reference response fixes the torus $M$, its test and the reading `fixedPhysicalLevel g₀`. Keep the least root and both limits at $K$ from row 1678. |
| Infinite-volume states and growing tori | Both clauses use the original lattice spacing and the original $\beta_j$. Choose a cubic weak limit at $K_j$ and subtract $r$ from the growing passage-side exponents. Their cumulants converge to the same $S'$. |
| Euclidean tests and positive smooth pair and quadruple | Compose all argument tests with $x\mapsto ax$. Pull the positive witnesses back with the inverse map. The values agree exactly and smoothness is preserved. |
| Centred moments | On both sides of the volume-first limit, the finite partition sum uses the transported cumulants at every arity. Its value is exactly the centred moment of $S'$. |
| Mixture and component Schwinger representatives | Evaluate the original degree-$n$ representative on $\varphi(a x_1,\ldots,a x_n)$. Degree zero keeps its scalar. Diagonals and positive time are invariant and tensor products commute with this operation. |
| Factorial growth | Put $b=\max(1,a^{-1})\max(1,a)$. The order-$q$ Schwartz seminorm costs at most $b^q$. For $q=kn$, replace the common exponential base $B$ by $B b^k$. The same constants work in every component, at every arity. |
| Euclidean invariance, permutation symmetry, reflection positivity and reflection reality | Conjugation by the dilation changes a Euclidean motion's translation and preserves its orthogonal part. Permutations and time reflection commute with dilation. Finitely supported positive-time sequences pull back to such sequences, preserving the reflection pairing. |
| Canonical decomposition | Keep the component space and its law. Compose each component with the tuple dilation. Its inverse preserves separation of components. Translating a cluster by $v$ becomes translation by $a^{-1}v$. This bijection preserves the filter at infinity, the iterated limits and their integral identities. |
| Component clustering and non-Gaussianity | The ray $t v$ becomes $t(a^{-1}v)$ with a nonzero spatial direction. For almost every component, rescale the smooth quadruple inversely. Its connected value survives exactly. |
| Gap and unique vacuum | The physical side $\ell$ and the time units of the semigroup fix the required rate. Use row 1676 on the original-mesh states, original bare couplings and $K_j\in A$. Its rate is $\frac{2}{\ell}\log(2^{18}/5041)$. |

The fixed-observable witness asks for positive tests and existential growth constants. Its continuum clauses impose no reading of $S'$ at a prescribed unit-distance test. The fixed calibration reading and the gap rate are both met in their stated physical units. [Release formulation](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/FixedObservableContinuum.lean#L20-L67) · [Gap rate](GapChain/Stage0.lean#L243)

### Kernel check

The proof module imports `GapChain.PurIo`. The kernel is Lean 4.33.1 at `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, with mathlib `0df444a360eaa60ab8c11dca51a86af692955474` and the Sussman–Alpoge release `3932084a9b82fc79466b4a2faad9ec032b637445`. I compared the source SHA-256 values of all 14 imported lane modules with their blobs at the pin and the previous build, and checked their oleans against the previous receipt. The scratch copy of row 1678’s project adds `GapChain.Offset` to its library roots and uses that row’s pager and compiler guard. Its build target was `lake --no-cache build +GapChain.Offset:olean`. Its cached imports are part of the trusted build inputs. The guard admitted only the new proof file for compilation. Lean checked the proof terms. The top theorem’s full axiom report is `propext`, `Classical.choice` and `Quot.sound`.

| Checked artifact | SHA-256 |
|---|---|
| `GapChain/Offset.lean` | `e119ac9879dd73a387db9818fc9442d4fe62b869dc2f02f7b0f7ba929f7df6a0` |
| `GapChain/Offset.olean` (1,792,232 bytes) | `651eb0213ca81529370b292bae92f5cd246ff3d0bf7acc1a0f72163ba010b519` |

The serial build used `LEAN_NUM_THREADS=2`, `/usr/bin/nice -n 10` and the archive pager. Admission for each compiler process required at least 50% system-wide free memory from `memory_pressure`. Lake’s `--no-build` check passed on `+GapChain.PurIo:olean` before development and on `+GapChain.Offset:olean` after the successful build. The latter reported all 21,150 jobs current. A process sandbox denied writes to the release fixture. The final run produced 51 axiom reports and zero module warnings or errors. The delivered source matches the source of the successful build byte for byte.

Full Lake logs, per-run compiler arguments, Lean JSON diagnostics and `runs.jsonl` are in `/private/tmp/sa-lean-gap-chain-offset-transport-astra62.qBF93O/logs`. The driver elapsed time includes Lake startup and the pager. Compiler RSS is Darwin `ru_maxrss` in bytes. The first required shell probe, `~/.elan/bin/lean --version`, reported the checkout default 4.36.0 in 0.583 s of enclosing shell time. That first probe's peak RSS was unmeasured. Its measured replay took 0.93 s and peaked at 51,068,928 bytes. All proof runs used 4.33.1.

| Run and process | Wall s | Peak RSS, bytes | Free at admission | Exit |
|---|---:|---:|---:|---:|
| `pinned-version` version | 0.073 | 49,790,976 | 68% | 0 |
| `pinned-version` version driver | 0.562 | 49,790,976 | 68% | 0 |
| `preflight` githash | 0.071 | 49,823,744 | 68% | 0 |
| `preflight` Lake driver | 20.874 | 1,029,488,640 | 68% | 0 |
| `mesh-1` githash | 0.072 | 49,807,360 | 68% | 0 |
| `mesh-1` Offset | 156.389 | 4,859,084,800 | 68% | 1 |
| `mesh-1` Lake driver | 183.306 | 4,859,084,800 | 68% | 1 |
| `canonical-1` githash | 0.071 | 49,774,592 | 67% | 0 |
| `canonical-1` Offset | 157.969 | 4,857,184,256 | 67% | 1 |
| `canonical-1` Lake driver | 183.259 | 4,857,184,256 | 67% | 1 |
| `full-1` githash | 0.071 | 49,807,360 | 67% | 0 |
| `full-1` Offset | 163.088 | 4,863,115,264 | 66% | 1 |
| `full-1` Lake driver | 188.198 | 4,863,115,264 | 67% | 1 |
| `full-2` githash | 0.071 | 49,774,592 | 67% | 0 |
| `full-2` Offset | 442.998 | 4,860,755,968 | 66% | 1 |
| `full-2` Lake driver | 468.127 | 4,860,755,968 | 67% | 1 |
| `full-3` githash | 0.071 | 49,807,360 | 64% | 0 |
| `full-3` Offset | 159.582 | 4,860,346,368 | 64% | 1 |
| `full-3` Lake driver | 186.181 | 4,860,346,368 | 64% | 1 |
| `full-4` githash | 0.071 | 49,823,744 | 65% | 0 |
| `full-4` Offset | 183.538 | 4,857,380,864 | 65% | 0 |
| `full-4` Lake driver | 208.614 | 4,857,380,864 | 65% | 0 |
| `offset-current` githash | 0.071 | 49,823,744 | 67% | 0 |
| `offset-current` Lake driver | 17.115 | 984,547,328 | 67% | 0 |

The development builds mesh-1 (4 errors), canonical-1 (19 errors), full-1 (16 errors), full-2 (4 errors), full-3 (2 errors) failed during elaboration. The fixes covered the periodized torus identity, the dependent list indices in the canonical component, flat-test membership and the translation action. The table includes those attempts.

### Verbatim `#print axioms` output

```text
'GapChain.Offset.scaleTuple_inverse' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.torus_cumulant_at_offset' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.shift_volumes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.mesh_at_offset' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.stateAtOffset_cumulant' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.match_volume_state' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.disjoint_scaled' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.disjointlySupported_scaled' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.functional_ext' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scaleList_toList' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.centred_scale' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.connected_scale' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.nonGaussian_scale' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scaleList_translate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scaleList_juxt' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_shiftedJuxt' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_shiftedComponents' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_zip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_atInfinity' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.iterLimit_scale' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.canonical_scale' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scaleCost_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_affine' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_weight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_schwartz_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_flat_on_domain' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_diagonal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_posTime' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_flat_mem' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_bracket' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scaleConstants_valid' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_growth' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.eval_sep_scale' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_representative' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_motion' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_euclidInvariant' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_permSymmetric' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_reflectionReal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scaleRaw_cast' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_tensor' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_shift' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_eval' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scalePosSeq_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scalePosSeq_finite' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_pairing' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_osPositive' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_cluster' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.scale_OS' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.volume_moments_tendsto' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Offset.su2_fixed_observable_gap_of_infinite_passing' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
```

## Next row and decisive outcome

Establish the Wilson purity premise `(PUR-io)` at the same calibrated $L,M,g_0$. For an admissible physical side $\ell$, prove that `PurIo.passingCutoffs L M g₀ ℓ` is infinite. Every cube at each selected cutoff must pass the $457/625$ neutral-purity bound at time `Γ.side / 512`. Taking this set for $A$ in the present theorem then gives the full witnesses, the explicit gap and the unique vacuum. [Passing cutoffs](GapChain/PurIo.lean#L25) · [Wilson neutral purity](GapChain/Purity.lean#L25)

**Decisive outcome.** A kernel-checked proof of that infinitude at the calibrated parameters discharges the remaining premise. A partial result should identify the first Wilson estimate that still lacks the required uniformity in cubes or cutoffs.
