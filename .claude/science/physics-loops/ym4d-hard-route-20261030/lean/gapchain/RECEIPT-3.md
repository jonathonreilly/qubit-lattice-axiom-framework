# Repo search

The November 8 lead search found a positive one-step Wilson-loop correlation on PRs 10114 and 10133. I checked its derivation in `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 and the inverse-power plateau estimate in main’s `research/ym4d/library/ph1.md` 278–311. Neither gives an exponential upper bound from a Pfaffian seed. An exact-name Lean search on main and the local refs for PRs 10114, 10133, 10134, 10141 and 10144 found no implementation of this implication. There is no row-specific prior file or competing Stage 3 assignment in the open registry. [Lead search, §11](../../library/prior/repo-search-2026-11-08.md) · [Registry](../../library/open-registry.md)

In the pinned lane, row 731 gives Theorem S-w and EV-L on paper. Rows 1457 and 1458 specify the Lean chain and its witness corrections. The checked W5 theorem takes abstract positive spectral data. Row 1525 instantiates it with the untwisted periodic weight. Stage 0 defines the signed weight, the calibrated coupling and the same-state odd-grid correlation. Stage 2 consumes that correlation bound. [Flux argument, §§8.2–8.4](../../library/gap-flux-exercise.md) · [Design, §5.2](../../library/lean-gap-chain-design-fable.md) · [Design check](../../library/lean-gap-chain-design-check-astra62.md) · [Wilson assembly](GapChain/Assembly.lean) · [Stage 0](GapChain/Stage0.lean) · [Stage 2](GapChain/Stage2.lean)

# Stage 3 of the conditional gap chain

**BUILT-PARTIAL.** The kernel proves that the calibrated Pfaffian seed propagates to the spectral gap on every larger integer cube and to a vanishing excited thermal tail at half the temporal period. The remaining obligation is the periodic, centered two-window comparison for Stage 0’s physical test span. No scientific or audit status is claimed.

## Kernel result

Let `j` be one of the frequently seeded cutoffs, `a = L^(-K j)`, `β = betaAt L M (K j) g₀`, and `N = ℓ * L^(K j) / 2`. With `T = (rectangularTorusData (h.beta_pos j)).choose`, the conclusion of `calibratedSpectralPropagation` gives

```text
m = (2/ℓ) log(2^18/5041) > 0
m a ≤ (T.spectrum (cube V)).gap          for every integer V ≥ 2N
(T.spectrum (cube V)).thermal (V/2) → 0    as V → ∞.
```

The same `K` and release coupling occur in the hypothesis and both conclusions. The estimate includes a zero seed. The limit argument uses the volume subsequence supplied by the same state witness.

| Part | What the kernel checks |
|---|---|
| W2–W4 | `kappaWeight_eq_diagonal` decomposes the signed sum over 64 twists into eight diagonal electric/magnetic sectors. Axis permutations preserve the signed weight. `rectSector_moments` identifies each of the 64 individual electric/magnetic coefficients, for each temporal period at least two, as a positive power sum on one fixed spatial Hilbert space. Positive eigenvalues carry geometric multiplicity. The inequalities used after exchanging axes hold on the rotated boxes. |
| Cubic normalization | `cube_sector_eigenspaces` transports all positive eigenspaces between the rectangular symmetric kernel and the YM4 release. Its proof uses Haar recoding and the positive spectra of the two orders of the half-transfer factors. `calibrated_cubicNorm` identifies the neutral top with the norm of the release’s periodic transfer on that very cube. |
| W5–W6 | `rectangularTorusData` supplies real signed Wilson integrals, crossing and enumerated spectra to the imported `GapChain.TheoremS`. `seed_eq_thermal`, `halfSide_thermal_tendsto` and `physicalRate_eq` specialize its conclusions to the prescribed seed. `calibrated_neutralResolution` gives the actual release neutral eigenbasis with one distinguished vacuum and an excited trace bounded by the signed thermal tail. |
| W9, physical insertions | The positive periodic Gibbs integral is exactly the joint Haar-layer integral, with the same partition function, by `physicalJoint_partition` and `physicalJoint_expectation`. For spatial and temporal plaquettes the marks are center-blind and have norm at most two. The finite expansion of centered smeared products fixes the coefficients and time levels before choosing a volume, and translates the same family of marks. |
| W9, neutral trace | `averaged_mark_trace` and `normalized_split_covariance` identify and bound the actual electric average. For two specified words of marks separated by empty arcs of lengths `d` and `a ≥ 3`, the normalized average differs from the two vacuum means’ product by at most `C₁ C₂ (2 exp(−r d) + 2 B.thermal a)`. Each `Cᵢ` is the product of the mark norms in that word. The vacuum is chosen once on the cube and the closing seam must satisfy the displayed invariance condition, which holds for an empty edge. |
| W9, periodic measure | `jointPeriodic_mean_sq` proves the positive mixture inequality with factor eight. `jointPeriodic_shift_mean` proves equality of periodic means for rotated observables. Given the indicated two-copy covariance envelope, `periodic_rotates_error` bounds the periodic-vacuum mean difference by a constant times `√(1/V + τ)` using `⌊V/(2 width)⌋` rotations. |
| W10–W11 | `liftedWilson_moments_unitCube` identifies the moments on the actual release torus of side `2 L^(v+k)`. `oddGrid_marginals` identifies the one-point factors after site reflection and integer time translation at the prescribed centering. `volumeU_connected_sum` expands the entire finite complex span into two-window covariances. `volumeU_tendsto` passes the finite covariance to `latticeU (ν j)` on the volume subsequence from `Inputs.isLimit`. |

The theorem `cutoff_polynomial_witness` gives each actual finite-volume monomial and all its grid translates as a periodic mean of one finite marked polynomial. Its coefficients, width and norm bound are chosen before the volume. The physical time origin is arbitrary and the centering is always the original `ν j`.

For the same vacuum used in the two-word bound, `normalized_single_window` bounds the neutral one-word error by twice the word’s norm budget times the thermal tail. `padded_vacuum_word` proves that empty leading and trailing layers preserve its vacuum value.

The theorem `normalized_word_polynomials` sums the translated two-word result for finite families with complex coefficients. Its error constant is the product of the two weighted norm budgets. The leading blank edge enforces the seam condition.

For the `⌊V/(2(w+1))⌋` repeated copies, `time_average_placement` places every distinct ordered pair beyond the seam, leaving an opposite arc of at least `V/2` and a near arc at least the distance between copy indices.

The positive neutral integral of a real polynomial equals the weighted sum of electric traces by `jointNeutral_polynomial`. The formula `rotated_polynomial_words` gives the product labels and weights for two rotated copies.

The theorem `periodic_polynomial_comparison` derives the time-average bound from estimates on the one-copy neutral means and on pairs of distinct copies. It handles coincident copies using the sup norm and takes the real part of the common complex vacuum value.

The theorem `periodic_covariance_of_three_means` combines the three periodic-vacuum errors with a vacuum connected-term estimate, preserving its exponential prefactor.

## First remaining estimate

Fix a seeded cutoff, its given state `ν j`, and the lattice rate `r = m aⱼ`. Write `μᵥ` for the physical **periodic** Gibbs measure, `V = 2 L^(v+K j)`, and `B = T.spectrum (cube V)`. For two monomials in the support of a Stage 0 test, the remaining scalar statement is `PairWindowEstimate`. With `d = 2n+1` it asks for

```text
|Cov_{μᵥ}(θX, τ_{d aⱼ}Y)| ≤ C_XY exp(−r d) + D_XY,n √(1/V + B.thermal(V/2)).
```

Each factor inside each monomial is centered with the original `ν j`. The outer connected covariance subtracts the product of the two periodic means. The prefactor `C_XY` must be chosen before the separation and volume. The error constant `D_XY,n` may depend on the separation. The statement applies eventually in volume when `r ≤ B.gap`.

The first missing identification occurs when applying the single- and double-word estimates to the physical product `G = (θX)(τ_{d aⱼ}Y)`. The vacuum value assigned to this product as **one** slab for time averaging must be the ordered vacuum matrix element of the **two** original marked slabs with their intervening empty transfer steps. All three observables must use one cube, chart, neutral vacuum and prescribed cutoff centering. The product width and its averaging constant may grow with `d`. The norm budgets for the connected vacuum term must stay fixed before `d`. This also requires a finite bound for the finitely many separations at which the original supports overlap.

More explicitly, for each of the two separate slabs and their product, insert the physical polynomial in `periodic_polynomial_comparison`. For a single vacuum value `c_G` at this volume the inputs on distinct rotations are

```text
|E₀ Gᵢ − c_G| ≤ M_G B.thermal(V/2),
|E₀(Gᵢ Gⱼ) − c_G²| ≤ D_G (q^|j−i| + B.thermal(V/2)),    i ≠ j,  0 ≤ q < 1.
```

Row 731, §8.2, supplies the hand argument. The kernel result stops at the stated physical witness and estimate. [Theorem S-w and EV-L](../../library/gap-flux-exercise.md) · [Witness and test-domain corrections](../../library/lean-gap-chain-design-check-astra62.md)

The declaration `expClusters_of_kappaSeed_of_pairWindows` has result type `type_of% @GapChain.expClusters_of_kappaSeed` after the displayed scalar premise. `expClusters_of_seeded_pairWindows` only needs this estimate on the seeded cutoffs, and preserves the original order `∀ Z, ∃ᶠ j`. This checks definitional agreement with Stage 0. Removing the extra premise is open. Stage 3 establishes no continuum gap or audit status.

## Sources and conventions

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the YM4 release, its fourth-coordinate time axis, cubic quotient Haar convention, transfer factorization and volume-first states. The outline identifies the inverse-power plateau bound. Complete account I distinguishes that result from clustering and a mass gap. I used the lane’s full-read indices first and consulted the cited source excerpts at revision `31a47c543775`. Both text downloads were made once in the new scratch directory. The outline has 32,992 lines and SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. Complete account I has 166,711 lines and SHA-256 `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`. [Outline, lines 3238–3254](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L3238-L3254) · [Outline, lines 31871–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31871-L31882) · [Account I, lines 3216–3222](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3216-L3222)

The lane supplies Theorem S-w (731), the electric and magnetic conventions (1004 and 1008), the design and correction (1457 and 1458), the replay (1455), the Stage 1 transfer and trace tools (1506 and 1508), and the Stage 0 statement and check (1652 and 1653). Row 1643 identified the fixed-coupling scope of row 1525’s Wilson assembly. Stage 2 (1654) is the downstream consumer. [Design](../../library/lean-gap-chain-design-fable.md) · [Design check](../../library/lean-gap-chain-design-check-astra62.md) · [Stage 0 check](../../library/lean-gap-chain-stage0-check-opus.md) · [Stage 2 receipt](RECEIPT-2.md)

## Reproduction and trusted base

The source checkout is `d560b9a095666cbc7f4f3697cc51321d61b332eb`. The scratch project used the v4.33.1 Lean kernel, Mathlib `0df444a360eaa60ab8c11dca51a86af692955474` and the replayed YM4 release `3932084a9b82fc79466b4a2faad9ec032b637445`. Stage 3 imports Stage 0, which imports the three Stage 1 modules, and the lane’s Hilbert–Schmidt trace module. Only the Stage 0 and Stage 3 module targets were requested. The lane-local `GapChain.Transfer` and `GapChain.Trace` built as dependencies. The original release and package tree were read-only. The package directory was linked into scratch. The compiler read byte-identical release artifacts through the scratch archive to keep the working set below six GB.

From the retained scratch project, the measured Stage 3 command was

```sh
python3 ../run.py stage3-41 ../guard/bin/lake --no-cache build +GapChain.Stage3:olean
```

The wrapper serializes Lean, checks system memory pressure and records the child process peak with macOS `wait4`. It disallows release module compiles. The scratch archive manifest records each copied import’s source, size and SHA-256. The final dependency check used `lake --no-build --no-cache build +GapChain.Stage0:olean +GapChain.Stage3:olean`.

The final Stage 3 compile (`stage3-41`) completed in **344.066 s** with **4,860,395,520 resident bytes** peak. Each of 402 theorem declarations has a corresponding `#print axioms` below. The reports contain only Lean’s `propext`, `Classical.choice` and `Quot.sound`. The four inherited Stage 0 placeholders still elaborate there. None occurs in the dependencies of a new theorem. The build used `LEAN_NUM_THREADS=2`, `nice -n 10`, a memory-pressure admission check of at least 50% free and serialized compiler processes for the verified run. A no-build preflight checked the final Stage 0 and Stage 3 targets.

| Artifact | SHA-256 |
|---|---|
| Stage3.lean | `6fee80c685c8e60806af2707b4e6c02387a29d3e1c922cd2722c2ecadcd7eb6b` |
| Stage3.olean | `6f035ef90b4e6e96b8aa5e3544e384e0022b32f19f523bea85bd4f346a84d1e4` |

The first requested bare `~/.elan/bin/lean --version` resolved to the machine default v4.36.0 and was unmetered. The timed repeat took 0.64 s and 51,118,080 peak resident bytes according to macOS time. The outer driver and the separate pinned v4.33.1 version check are listed below. The first local bootstrap ran before Lake propagated the process-metering wrapper. Its aggregate was 51.738 s and 3,739,123,712 resident bytes. Lake reported 17 s for SequenceLemma, 18 s for TheoremS, 3.7 s for LemmaM1 and 4.9 s for Wilson. Stage0 was interrupted during that bootstrap. Individual peak RSS values for those first workers are unavailable. The serialized Stage0 replay took 198.038 s at 3,714,793,472 peak resident bytes. An initial guarded no-build preflight stopped when Lake attempted to record a failed compiler-version probe in the read-only packages. Permitting its read-only `--githash` probe restored the dependency check. No release module was rebuilt. Full run logs, the project, compile inputs and diagnostics are in `/tmp/sa-lean-gap-chain-stage3-astra62.l16Yek`.

The successful Stage 3 compiler emitted 77 warnings, recorded in the final diagnostic log. The counts by diagnostic kind are 13 `Lean.Linter.deprecatedAttr`, 31 `linter.style.haveILetI`, 6 `linter.unnecessarySeqFocus`, 3 `linter.unreachableTactic`, 3 `linter.unusedSectionVars`, 16 `linter.unusedSimpArgs`, 3 `linter.unusedTactic`, 2 `linter.unusedVariables`.

## Measured runs

Times are elapsed seconds and peaks are resident bytes on macOS. The compiler columns include the admitted free-memory percentage, elapsed time, peak and exit code. The outer Lake driver includes dependency checks, compiler startup and waiting. Each `--githash` invocation has its own measurement. A dash means that process was absent or lacks an individual measurement. The local prerequisite rows give the individual peaks for the successful serialized replay.

| Run | Compiler process | Free % | Compiler s | Compiler peak B | Exit | Lake s | Lake peak B | Lake exit |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| pinned-version | version | 68 | 0.071 | 49,790,976 | 0 | 0.572 | 49,790,976 | 0 |
| preflight | — | — | — | — | — | 13.368 | 1,030,225,920 | 0 |
| stage0 | — | — | — | — | — | 51.738 | 3,739,123,712 | 1 |
| guarded-preflight | — | — | — | — | — | 7.178 | 864,010,240 | 3 |
| guarded-preflight-hash | githash | 66 | 0.066 | 49,807,360 | 0 | 17.371 | 1,030,127,616 | 0 |
| stage0-serial | githash | 67 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | SequenceLemma | 66 | 4.150 | 2,983,673,856 | 0 | — | — | — |
|  | TheoremS | 66 | 3.102 | 3,403,808,768 | 0 | — | — | — |
|  | LemmaM1 | 66 | 2.808 | 3,177,332,736 | 0 | — | — | — |
|  | Wilson | 67 | 4.287 | 3,400,990,720 | 0 | — | — | — |
|  | Stage0 | 67 | 198.038 | 3,714,793,472 | 0 | 277.962 | 3,714,793,472 | 0 |
| stage3-crossing | githash | 68 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 67 | 381.426 | 3,689,889,792 | 1 | 405.707 | 3,689,889,792 | 1 |
| stage3-02 | githash | 67 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 67 | 1029.852 | 4,865,638,400 | -2 | 1054.115 | 4,865,638,400 | 1 |
| stage3-03 | githash | 66 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 65 | 173.834 | 4,854,349,824 | 1 | 197.672 | 4,854,349,824 | 1 |
| default-version-replay | — | — | — | — | — | 0.756 | 51,118,080 | 0 |
| stage3-04 | githash | 65 | 0.068 | 49,774,592 | 0 | — | — | — |
|  | Stage3 | 65 | 169.477 | 4,862,099,456 | 1 | 192.921 | 4,862,099,456 | 1 |
| stage3-05 | githash | 66 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 65 | 175.091 | 4,859,166,720 | 0 | 198.685 | 4,859,166,720 | 0 |
| stage3-06 | githash | 66 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 65 | 161.547 | 4,859,707,392 | 1 | 185.699 | 4,859,707,392 | 1 |
| stage3-07 | githash | 66 | 0.071 | 49,774,592 | 0 | — | — | — |
|  | Stage3 | 67 | 173.918 | 4,860,739,584 | 1 | 198.335 | 4,860,739,584 | 1 |
| stage3-08 | githash | 67 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 67 | 165.727 | 4,854,759,424 | 1 | 189.801 | 4,854,759,424 | 1 |
| stage3-09 | githash | 66 | 0.062 | 49,823,744 | 0 | — | — | — |
|  | Stage3 | 66 | 174.144 | 4,861,984,768 | 1 | 198.356 | 4,861,984,768 | 1 |
| stage3-10 | githash | 64 | 0.068 | 49,823,744 | 0 | — | — | — |
|  | Stage3 | 64 | 168.437 | 4,860,510,208 | 1 | 192.618 | 4,860,510,208 | 1 |
| stage3-11 | githash | 64 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 64 | 178.125 | 4,860,461,056 | 1 | 202.383 | 4,860,461,056 | 1 |
| stage3-12 | githash | 65 | 0.068 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 64 | 173.496 | 4,859,985,920 | 1 | 197.106 | 4,859,985,920 | 1 |
| stage3-13 | githash | 66 | 0.067 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 66 | 174.077 | 4,857,102,336 | 1 | 198.604 | 4,857,102,336 | 1 |
| stage3-14 | githash | 63 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 63 | 171.253 | 4,874,502,144 | 1 | 194.584 | 4,874,502,144 | 1 |
| stage3-15 | githash | 65 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 65 | 169.835 | 4,857,069,568 | 1 | 194.093 | 4,857,069,568 | 1 |
| stage3-16 | githash | 65 | 0.068 | 49,774,592 | 0 | — | — | — |
|  | Stage3 | 65 | 181.483 | 4,858,740,736 | 1 | 205.960 | 4,858,740,736 | 1 |
| stage3-17 | githash | 67 | 0.070 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 66 | 176.325 | 4,860,035,072 | 1 | 200.544 | 4,860,035,072 | 1 |
| stage3-18 | githash | 66 | 0.064 | 49,823,744 | 0 | — | — | — |
|  | Stage3 | 66 | 202.556 | 4,860,231,680 | 1 | 225.846 | 4,860,231,680 | 1 |
| stage3-19 | githash | 66 | 0.066 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 66 | 229.011 | 4,865,736,704 | 0 | 252.382 | 4,865,736,704 | 0 |
| stage3-20 | githash | 67 | 0.072 | 50,741,248 | 0 | — | — | — |
|  | Transfer | 67 | 25.337 | 3,449,929,728 | 0 | — | — | — |
|  | Trace | 67 | 2.418 | 3,412,131,840 | 0 | — | — | — |
|  | Stage3 | 67 | 192.227 | 4,863,246,336 | 1 | 244.038 | 4,863,246,336 | 1 |
| stage3-21 | githash | 67 | 0.071 | 49,774,592 | 0 | — | — | — |
|  | Stage3 | 66 | 200.975 | 4,871,815,168 | 1 | 225.455 | 4,871,815,168 | 1 |
| stage3-22 | githash | 66 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 65 | 213.989 | 4,858,560,512 | 1 | 238.295 | 4,858,560,512 | 1 |
| stage3-23 | githash | 66 | 0.062 | 49,823,744 | 0 | — | — | — |
|  | Stage3 | 66 | 361.514 | 4,859,297,792 | 1 | 389.040 | 4,859,297,792 | 1 |
| stage3-24 | githash | 62 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 62 | 254.844 | 4,860,067,840 | 1 | 282.355 | 4,860,067,840 | 1 |
| stage3-25 | githash | 68 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 67 | 304.629 | 4,870,062,080 | 1 | 327.300 | 4,870,062,080 | 1 |
| stage3-26 | githash | 68 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 67 | 253.498 | 4,859,969,536 | 1 | 277.573 | 4,859,969,536 | 1 |
| stage3-27 | githash | 68 | 0.064 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 68 | 432.750 | 4,862,984,192 | 1 | 456.342 | 4,862,984,192 | 1 |
| stage3-28 | githash | 69 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 69 | 434.669 | 4,868,669,440 | 1 | 458.745 | 4,868,669,440 | 1 |
| stage3-29 | githash | 69 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 69 | 267.659 | 4,863,934,464 | 1 | 291.708 | 4,863,934,464 | 1 |
| stage3-30 | githash | 70 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 69 | 263.341 | 4,857,708,544 | 1 | 287.842 | 4,857,708,544 | 1 |
| stage3-31 | githash | 69 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 69 | 246.588 | 4,861,706,240 | 1 | 271.147 | 4,861,706,240 | 1 |
| stage3-32 | githash | 68 | 0.067 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 67 | 277.751 | 4,860,018,688 | 1 | 302.566 | 4,860,018,688 | 1 |
| stage3-33 | githash | 67 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 67 | 263.480 | 4,860,968,960 | 1 | 288.534 | 4,860,968,960 | 1 |
| stage3-34 | githash | 67 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 67 | 281.048 | 4,862,050,304 | 1 | 305.597 | 4,862,050,304 | 1 |
| stage3-35 | githash | 68 | 0.071 | 49,823,744 | 0 | — | — | — |
|  | Stage3 | 67 | 432.323 | 4,862,525,440 | 1 | 456.751 | 4,862,525,440 | 1 |
| stage3-36 | githash | 69 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 68 | 275.516 | 4,868,079,616 | 1 | 300.455 | 4,868,079,616 | 1 |
| stage3-37 | githash | 68 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 68 | 296.627 | 4,872,241,152 | 1 | 320.004 | 4,872,241,152 | 1 |
| stage3-38 | githash | 69 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 68 | 296.985 | 4,857,937,920 | 1 | 320.305 | 4,857,937,920 | 1 |
| stage3-39 | githash | 69 | 0.071 | 49,807,360 | 0 | — | — | — |
|  | Stage3 | 69 | 307.832 | 4,859,953,152 | 1 | 332.196 | 4,859,953,152 | 1 |
| stage3-40 | githash | 69 | 0.071 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 68 | 294.010 | 4,866,703,360 | 1 | 318.501 | 4,866,703,360 | 1 |
| stage3-41 | githash | 69 | 0.070 | 49,790,976 | 0 | — | — | — |
|  | Stage3 | 69 | 344.066 | 4,860,395,520 | 0 | 368.272 | 4,860,395,520 | 0 |
| final-preflight | githash | 69 | 0.071 | 49,823,744 | 0 | 16.914 | 985,169,920 | 0 |

## Verbatim kernel axiom reports

The 402 theorem reports below come from the final source elaboration. Their union is `propext`, `Classical.choice` and `Quot.sound`.

```text
'GapChain.Stage3.planeOf_swap' depends on axioms: [propext]
'GapChain.Stage3.mapPlane_planeOf' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.mapPlane_mul' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.mapPlane_one' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.faceAction_swap' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.faceAction_planeOf' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.faceAction_relabel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_permute' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.pfaffianSign_swap' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.pfaffianSign_permute' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.kappaWeight_permute' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.pfaffianSign_join' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.character_orthogonal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.kappaWeight_eq_diagonal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.character_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.character_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.join_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.character_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.sectorWeight_le_neutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_eq_sectorSum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electric_untwist' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.eraseIncident_map' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.eraseIncident_time' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.untwist_axis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.all_twists_le_periodic' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.partition_div_eight_le_neutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.sectorWeight_le_eight_neutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.partition_div_eight_le_kappa' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedMeasure_probability' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodic_mean_sq_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.mixtureMean_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.mixture_window_comparison' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodic_window_comparison' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.summable_time_decay' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkCentre_comm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkCentre_xor' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkCentre_inv' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.bitSign_xor' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.halfTrace_linkCentre' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.resign_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkCentre_mul_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkCentre_inv_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.transport_resign' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.signedIntegral_resign' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.signedIntegral_stackBits' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.oneStack_swap' depends on axioms: [propext]
'GapChain.Stage3.interval_curl' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.stripLinks_curl' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.signedIntegral_moveStack' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.oneStack_plane' depends on axioms: [propext]
'GapChain.Stage3.locatedStacks_partition' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabFields_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.transport_slabField' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.signedDensity_eq_slabs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.signedIntegral_eq_slabKernels' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_eq_slabKernels' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabDensity_off_electric_cut' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabDensity_adjacent' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.spatialLevels_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_eq_kernelCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabField_flipSlice' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.seamLinks_curl' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.layerKernel_electric' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.finRotate_ne_self_of_two' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_eq_electricCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.mem_cuts' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.fluxBit_add' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.character_add' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.character_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centreElt_mul_self' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translation_characterProj' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.characterProj_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centreShift_add' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electricTranslation_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translation_electricProj' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electricProj_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electricTranslation_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electricTranslation_isSelfAdjoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electricProj_isSelfAdjoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electricProj_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.electricProj_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.continuous_magneticHolonomy' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticEnergy_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.continuous_magneticEnergy' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticEnergy_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticDensity_continuous' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticDensity_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticMultiplier_formula' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticMultiplier_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticTransfer_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticTransfer_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticTransfer_traceClass' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centreSign_comm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centreSign_linkClass' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centreSign_ofAxis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centreSign_shift_transverse' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.holonomy_centreShift' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticEnergy_centreShift' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.commutes_magneticMultiplier' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centreShift_gauge' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.commutes_gaugeProjection' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.commutes_sqrtLink' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticTransfer_commutes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticTransfer_commutes_proj' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticMultiplier_half_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.layerFactor_products' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.symmetricMagnetic_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.symmetricMagnetic_zero_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticEnergy_gaugeAct' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticMultiplier_commutes_gaugeProjection' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.halfTransfer_squared' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.symmetricMagnetic_kinetic' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.product_eigenspaces' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.symmetricMagnetic_sector_eigenspaces' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.level_siteOfCode' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.spatialCode_siteOfCode' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slicePeriods_of_spatialCode' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.spatialCode_of_translate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.releaseLinkLabel_class' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.sliceLink_ofAxis_axis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkClass_eq_of_code' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.releaseLayer_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.releaseLayer_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_eq_releasedCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectVertices_spaceStep' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectVertices_timeStep' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magnetic_temporal_bit' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.layerKernel_eq_rectKernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_eq_rectCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectKernel_factorization' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.continuous_rectSpatialAction' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectGauge_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTemporal_gauge' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymKernel_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectKernel_eq_sym' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTemporal_gram' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymOperator_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSpatialAction_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectGauge_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTemporal_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectHalfWeight_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymKernel_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.twistedPartition_eq_symCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.continuous_rectKernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectFlip_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSeamKernel_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectFlip_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectFlip_involution' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectFlip_add' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTranslation_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTranslation_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTranslation_selfAdjoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectProj_idempotent' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectProj_selfAdjoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectRight_insert' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectLeft_insert' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymEntry_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymSeam_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymOperator_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymOperator_commutes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymOperator_commutes_proj' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSector_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.kernel_norm_domination' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTestEntry_continuous' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTestEntry_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTestEntry_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTestOperator_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectOperator_insert' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.integral_seamZero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectInsertedTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectElectricEntry_operator' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectElectricEntry_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymLoop_partition' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSectorTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSector_compact' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSector_moments' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.sectorWeight_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.zmod_val_rotate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.spatialCode_shift' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.vertexFromCode_class' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkFromCode_class' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.releaseFaceLabel_class' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.faceClass_eq_of_code' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.readLinks_holonomy' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.codeResidue_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticFace_readCode' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.halfTrace_magneticHolonomy' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectFaceTerm_readCode' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.magneticEnergy_readLinks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkCoordinates_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.gaugeCoordinates_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.linkCoordinates_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.gaugeCoordinates_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.readLinks_gaugeAct' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.readLinks_electric' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.singleBondWeight_real' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTemporal_readLinks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectHalfWeight_readLinks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymKernel_release' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.integral_row_gaugeProjection' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.symmetricMagnetic_hasKernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cubeIsometry_surjective' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cubeIsometry_intertwines' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectSymOperator_cube_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cubeIsometry_electric' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cubeIsometry_proj' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cube_sector_eigenspaces' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.releaseSector_spectral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.edgeMemLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.edgeOperator_compose' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.edgeLoop_cons' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.integral_edgeLoop' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.hasSum_edgeLoop' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.hasSum_markedCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.fieldOfPairs_spatial' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.fieldOfPairs_temporal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.releasePairWeight_boltzmann' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.liftedGibbs_integral_pairs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.markedPair_integral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.readLinks_continuous' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.readVertices_continuous' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodicHalfWeight_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.integral_markedPairs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTestEntry_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTestOperator_commutes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.writeLinks_readLinks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.readLinks_writeLinks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.writeLinks_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.spatialFaceMark_blind' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.temporalFaceMark_blind' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.faceEnergy_halfTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.spatialFaceMark_read' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.temporalFaceMark_read' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.face_as_layer_plaquette' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.face_at_base_level' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.wilsonFace_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.spatialFaceMark_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.temporalFaceMark_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translate_temporalPlaquette' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translate_spatialPlaquette' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.faceEnergy_translated_layerMark' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translatedUnitTest_center' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translated_smearedEnergy_layerMarks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.faceEnergy_layerMark' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.smearedEnergy_layerMarks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cubeTimeIndex' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.finite_time_word' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.word_residue_support' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.residue_word_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.anchoredCubeTimeIndex' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.residue_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physical_marked_trace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.combineTests_blind' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.combineTests_off' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.combineTests_values' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.combineTests_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.combineTests_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translated_centeredProduct_layerExpansion' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centeredProduct_layerExpansion' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointDensity_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.continuous_jointDensity' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.joint_markedCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectTestEntry_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.joint_partition' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.flipLayerMap_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.edgeOperator_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.closing_mark_trace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.averaged_mark_trace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.closing_partition' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointState_probability' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointState_integral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physicalJointCoordinates_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physicalJointCoordinates_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physicalJointCoordinates_density' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physical_shifted_jointMark' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physicalJoint_partition' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physicalJoint_expectation' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointPeriodic_mean_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointNeutralMean_weight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.relabelJoint_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.relabelJoint_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodicDensity_relabel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointPeriodic_shift_mean' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.joint_window_comparison' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointNeutralMean_centered_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.joint_covariance_envelope' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.translated_residue_rotation' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.time_average_placement' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.weighted_window_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.weighted_window_pair_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.real_vacuum_errors' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodic_covariance_of_three_means' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodic_rotates_error' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointNeutralMean_le_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodic_polynomial_comparison' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.layerOperator_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.layerOperator_commutes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.projectedLayer_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectProj_norm_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.projectedLayer_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabProduct_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabProduct_factor' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.ofFn_empty_arc' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.ofFn_split_windows' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.shifted_word_entry' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.ofFn_word_segment' depends on axioms: [propext, Quot.sound]
'GapChain.Stage3.cyclic_two_words' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointNeutralMean_of_marks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointMark_relabel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointMark_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointNeutral_rotated_product' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.continuous_jointMark' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.jointNeutral_polynomial' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rotated_polynomial_words' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.normalized_mark_trace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectShape_boxSides' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.boxSector_moments' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.boxSector_labeledList' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.boxSector_list' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.boxNeutral_norm_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.boxNeutral_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cubicTraceIdentity_iff_kernelCycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.projectedTrace_of_insertions' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.sectorWeight_nonneg_of_insertions' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.kappaWeight_cross' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.diagonal_values_le_periodic_top' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectangularDiagonalTraces' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.DiagonalTraces.hasSum_weight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.DiagonalTraces.boxSpectrum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.DiagonalTraces.weight_logConvex' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.DiagonalTraces.neutralTail_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.DiagonalTraces.gap_le_neutralSlot' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.vacuumComplement_power_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.normalizedNeutral_symmetric' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.neutralMatrixElement_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.periodic_boxSides' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.torusData_of_diagonalTraces' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.torusData_of_cubicNorm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.boxShape_cube' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.calibrated_cubicNorm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rectangularTorusData' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.seed_eq_thermal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.seedRate_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.halfSide_thermal_tendsto' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.physicalRate_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.volumeU_self' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centredMoment_weak' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.volumeU_tendsto' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.volumeSide_tendsto' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.rescale_cubicPeriods' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.liftedWilson_unitCube' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.smearedEnergy_unitTest' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.measurable_smearedEnergy_unitTest' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.centredMoment_unitTest' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.liftedWilson_moments_unitCube' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cutoff_joint_moments' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.frozenMoment_motion' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.pushed_list_moment' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.siteReflection_motion' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.gridTranslation_motion' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.frozen_smearedMean_motion' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.unitTest_gridTranslation' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cutoff_translated_marks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cutoff_polynomial_witness' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.oddGrid_marginals' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.volumeU_connected_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabEstimate_of_pairWindows' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.release_sector_moments' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.release_neutralTail' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.neutralPartition_ratio' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.divide_trace_error' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.sectorResolution_of_slots' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.markedSectorResolution' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.vacuum_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.release_neutralResolution' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.calibrated_neutralResolution' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.basis_insertedTrace_tail' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.sector_trace_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.markedSector_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.split_marked_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.normalized_split_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.padded_vacuum_word' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.normalized_single_window' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.normalized_cyclic_words' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.normalized_cyclic_single' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.normalized_word_polynomials' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.NeutralResolution.insertedTrace_tail' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.NeutralResolution.normalized_contraction' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.NeutralResolution.twoInsertion_trace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.slabEstimate_of_neutralComparison' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.cutoff_bound_of_finiteTori' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.seed_at_calibrated_cutoff' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.calibratedSpectralPropagation' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.expClusters_of_finiteTori' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.expClusters_of_kappaSeed_of_finiteTori' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.expClusters_of_kappaSeed_of_neutralComparison' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'GapChain.Stage3.expClusters_of_seeded_windows' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.expClusters_of_seeded_pairWindows' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.expClusters_of_kappaSeed_of_pairWindows' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3.expClusters_of_kappaSeed_of_slabComparison' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Next row and decisive outcome

FINISH row **1658**, `lean-gap-chain-stage4-astra62`, owns the two Stage 4 implications. Its decisive outcome is a kernel build of `neutralTail_of_rankOneAtTime` and `kappaSeed_of_neutralPhysicalSeed` at the exact Stage 0 types using only the three stated axioms, or the precise first estimate or witness identification that prevents that build.
