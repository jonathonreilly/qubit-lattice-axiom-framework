# Repo search

The lead’s November 8 search found a positive one-step Wilson-loop correlation on PRs 10114 and 10133. I checked lines 106–149 of `MASS_GAP_LOCAL_BLOCK_ASTRA.md`. The file has the same Git blob on both refs. Main’s `research/ym4d/library/ph1.md`, lines 278–311, bounds the approach to a plateau by inverse powers of distance. Neither supplies the exponential upper bound required here. I searched the Lean sources on main and the local refs for PRs 10114, 10133, 10134 and 10141 for `PairWindowEstimate`, `expClusters_of_kappaSeed`, `cutoff_polynomial_witness` and `normalized_word_polynomials`. All five searches returned zero matches. At the pinned revision there is no row-specific prior file or matching owner in the open registry. [Lead search, §11](../../library/prior/repo-search-2026-11-08.md) · [Registry](../../library/open-registry.md)

Row 731 §8.2 supplies the hand proof of EV-L. Row 732 checked it. Rows 1457–1458 designed and corrected the gap chain. Rows 1652–1653 fixed and checked its Stage 0 interface. Row 1657 supplied the spectral propagation, marked trace estimates and finite-volume consumer. Check 1666, by Claude Fable 5.2, identified the missing product witness, common-vacuum assembly and treatment of overlapping windows. [EV-L](../../library/gap-flux-exercise.md) · [EV-L check](../../library/gap-flux-exercise-check.md) · [Design](../../library/lean-gap-chain-design-fable.md) · [Design check](../../library/lean-gap-chain-design-check-astra62.md) · [Stage 3 receipt](RECEIPT-3.md) · [Check 1666](../../library/lean-gap-chain-stage3-check-fable.md)

# Row 1667 · Lean Stage 3b

**BUILT.** `GapChain.Stage3b.pairWindowEstimate` proves the closed supply for every admissible blocking factor, positive cutoff, positive coupling, infinite-volume limit at that cutoff and positive lattice rate. The sole argument supplied to Stage 3’s reduction is this theorem. Lean checks the following declaration with the exact Stage 0 type. The original physical Pfaffian seed is still a hypothesis of that type. This is a research result for the conditional chain and grants no audit status. [Stage 3b](GapChain/Stage3b.lean) · [Stage 0](GapChain/Stage0.lean)

```lean
theorem expClusters_of_kappaSeed : type_of% @GapChain.expClusters_of_kappaSeed :=
  expClusters_of_kappaSeed_of_pairWindows @pairWindowEstimate
```

## How the estimate closes

1. **Physical product.** `cutoff_product_witness` chooses the two label sets, coefficients, integer anchors, widths and norm budgets before the cube or displacement. At each volume it supplies one cube and one joint-coordinate chart for both factors, their pointwise product and their periodic covariance. Each smeared factor retains its centring at the prescribed state `ν`, including after translation. When the first word has width `u` and there are `g` empty layers before the second, `WordFamily.separated_word` identifies the combined word with `U ++ List.replicate g 1 ++ W`. Its slab operator is the ordered product with the normalized neutral transfer raised to `g` in the middle. `separated_vacuum` applies `vacuum_covariance` to that product.
2. **One neutral vacuum.** `common_resolution` extracts the resolution and its two-word estimate from `normalized_word_polynomials`. For each real polynomial, `polynomial_periodic` places the rotated copies using `time_average_placement`. It converts their positive neutral means to marked traces with `jointNeutral_polynomial`, `normalized_cyclic_single` and `rotated_polynomial_words`. These supply both hypotheses of `periodic_polynomial_comparison`. Its real-part estimate and the single-copy bound on the imaginary part give a complex norm estimate when the half-period thermal tail is at most one. `separated_periodic_covariance` applies the estimate to the two factors and their product with the same resolution, then uses `periodic_covariance_of_three_means`.
3. **Uniform prefactor.** Write `b,c` for the anchors, `K,M` for the two fixed weighted norm budgets and `d = 2n+1`. Lean takes `c₀ = |b−c|+u` and `C = 2KM exp(r(c₀+1))`. For `d ≤ c₀`, the periodic probability bound gives `|Cov| ≤ 2KM`. For `d > c₀`, the empty interval has length `g = c+d−b−u ≥ 0` and `d ≤ g+c₀+1`. If the thermal tail exceeds one, the same probability bound is absorbed by the allowed finite-volume error. Thus `C` is independent of separation and volume. The coefficient of `√(1/V + thermal(V/2))` may depend on `n`, as Stage 3’s finite-volume premise permits.

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the YM4 release, its Wilson states, fourth-coordinate time convention and transfer normalization. The indexed outline’s plateau estimate is polynomial. Complete account I explicitly leaves clustering and the mass gap outside the stated theorem. Both source files were fetched once at `31a47c543775` in the new scratch directory. [Outline, lines 3238–3254](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L3238-L3254) · [Complete account I, lines 3216–3222](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3216-L3222)

## Reproduction and trusted base

The source revision is `7da021cbfdd796ff5e6a2c97e5d3fc9ffcd9f3e6`. The kernel is Lean 4.33.1 at `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, with Mathlib `0df444a360eaa60ab8c11dca51a86af692955474` and the YM4 release `3932084a9b82fc79466b4a2faad9ec032b637445`. The scratch project contains the committed gap-chain sources, copies of the matching Stage 0 and Stage 3 build products, and a link to the built packages. The wrapper serializes the compiler, admits each run at 50% or more free memory, sets `LEAN_NUM_THREADS=2`, runs at `nice -n 10` and guards compiler RSS below the 6 GB cap. The fixture and toolchain are write-protected. The guard allows proof compilation only for Stage 3b. Lake replays Stage 3’s cached diagnostics when checking the two targets.

From the scratch project, the final commands are

```sh
cd /tmp/sa-lean-gap-chain-stage3b-astra62.nxVa3N/project
python3 ../run.py s3b-final ../guard/bin/lake --no-cache build +GapChain.Stage3:olean +GapChain.Stage3b:olean
python3 ../run.py s3b-preflight ../guard/bin/lake --no-build --no-cache build +GapChain.Stage3:olean +GapChain.Stage3b:olean
```

The kernel axiom reports below contain only `propext`, `Classical.choice` and `Quot.sound`. The exact-type theorem has no dependency on a Stage 0 placeholder, a compiled decision procedure or an added axiom. The release and its dependencies were reused from their built artifacts.

| Module | Source SHA-256 | Olean SHA-256 |
|---|---|---|
| Stage0 | `eb46735f0a44a13524c1cec8e1c0d3a4f220f3e7fa25f41a81a0c5954a069a1c` | `5b329fce0c0033cd52b91e6eb4305929e39a9b7b415ea41fb4def916305eafb1` |
| Stage3 | `6fee80c685c8e60806af2707b4e6c02387a29d3e1c922cd2722c2ecadcd7eb6b` | `6f035ef90b4e6e96b8aa5e3544e384e0022b32f19f523bea85bd4f346a84d1e4` |
| Stage3b | `24c31a781243266a0b358d7841678de5736e56631fcab17fcd69403ef5364cf0` | `0ed55868b734a1ebd7b2099a288ecd42163dc266e987f1be7799f4cfd5bb696a` |

## Measured runs

The final Stage 3b compiler completed in **191.861 s** and peaked at **4,861,083,648 resident bytes**. It emitted 26 axiom reports and zero warnings or errors. The subsequent no-build dependency check exited successfully.

Every metered Lean process and its Lake or development driver is listed below. Peak RSS is the macOS `wait4` value in bytes. The first requested bare `~/.elan/bin/lean --version` resolved to the machine default 4.36.0. Its individual time and RSS were not captured. The separate metered repeat is labeled below. The `pinned-version` row is the compiler used for proofs.

| Run | Process | Free at start | Wall s | Peak RSS bytes | Exit |
|---|---|---:|---:|---:|---:|
| pinned-version | version | 69% | 0.073 | 49,774,592 | 0 |
| pinned-version | driver | 69% | 0.570 | 49,774,592 | 0 |
| s3b-01 | githash | 69% | 0.071 | 49,823,744 | 0 |
| s3b-01 | Stage3b | 69% | 162.788 | 4,867,457,024 | 1 |
| s3b-01 | driver | 69% | 194.406 | 4,867,457,024 | 1 |
| dev-01 | Stage3b | 66% | 480.966 | 4,861,083,648 | 0 |
| dev-01 | driver | 66% | 481.181 | 4,861,083,648 | 0 |
| default-version-replay | version | 66% | 0.682 | 51,347,456 | 0 |
| s3b-final | githash | 66% | 0.061 | 49,807,360 | 0 |
| s3b-final | Stage3b | 66% | 191.861 | 4,861,083,648 | 0 |
| s3b-final | driver | 66% | 218.497 | 4,861,083,648 | 0 |
| s3b-preflight | githash | 67% | 0.071 | 49,807,360 | 0 |
| s3b-preflight | driver | 67% | 17.438 | 983,957,504 | 0 |

The initial compile `s3b-01` stopped at the slice of a finite list that identifies the interior word. The repair uses the zero-offset segment identity and the exact prefix length. The development process reused one imported environment for eight successive source elaborations. Their elapsed times in milliseconds were 6904, 7842, 2626, 2618, 3146, 3122, 3568, 3441. The process peak covers all eight. Intermediate errors and the final clean elaboration are recorded in `development/response-*.txt`. Its scratch driver is outside the delivered module. The standalone Lake build used the production source with all axiom commands.

The full build log, raw axiom diagnostics, timings and copied-source setup are in `/tmp/sa-lean-gap-chain-stage3b-astra62.nxVa3N/logs/` under `s3b-final.log`, `s3b-final-diagnostics.jsonl`, `runs.jsonl` and `s3b-final-Stage3b.setup.json`. No release compiler process ran.

## Verbatim kernel axiom reports

```text
'GapChain.Stage3b.WordFamily.separated_value' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.WordFamily.separated_word' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.WordFamily.separated_cost' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.WordFamily.word_norm_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.WordFamily.cost_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.WordFamily.norm_value_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.WordFamily.continuous_value' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.norm_vacuumValue_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.separated_vacuum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.common_resolution' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.single_trace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.polynomial_periodic' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.monomial_append' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.list_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.cutoff_list_chart' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.gridShift_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.cutoff_word_family' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.norm_periodicMean_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.trivial_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.cutoff_product_witness' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.meanError_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.covarianceError_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.separated_periodic_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.exponential_offset' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.pairWindowEstimate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.expClusters_of_kappaSeed' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Next row and decisive outcome

Row 1658 owns Stage 4. The pinned queue ends at 1667. **Proposed next row 1668** is an independent faithfulness check of Stage 3b. Its decisive outcome is confirmation that the common-cube product, centring, two constants and quantifier order give the exact Stage 0 implication under the reported axioms, or the first source line where that identification fails.
