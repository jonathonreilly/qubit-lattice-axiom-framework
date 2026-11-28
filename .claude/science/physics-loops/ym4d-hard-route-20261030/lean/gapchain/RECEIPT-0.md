# Repo search

The lead's 8 November search covered main and PRs 10114, 10133, 10134 and 10141. I checked those refs for the proposed Lean declarations and opened the closest prior results. PR 10114's `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–151 gives a one-step lower bound for a centred Wilson-loop correlation. Main's `research/ym4d/library/ph1.md` 278–311 bounds a remainder above an invariant plateau by inverse powers of distance. Main's `research/ym4d/library/cl1.md` discusses tensor density at lines 271 and 349. None supplies the positive-rate continuum implication. The target-specific prior file is absent, and the open registry has no competing row for Stage 0. [Lead search](../../library/prior/repo-search-2026-11-08.md) · [Open registry](../../library/open-registry.md)

At the pin, `Assembly.wilson_theoremS` supplies fixed-coupling propagation on dyadic boxes. Row 1643 identifies the missing centre projection, twists and continuum passage. Row 1459 already supplies the Stage 1 sequence inequality U4, rank-one estimate W1 and abstract Theorem S W5. Stage 0 imports all three and reuses the Wilson matrices and plaquettes of row 1504. [Direction checkpoint, §§1.5 and 3](../../library/gap-direction8-fable.md) · [Stage 1 receipt](RECEIPT.md) · [Assembly](GapChain/Assembly.lean) · [Wilson](GapChain/Wilson.lean)

# Stage 0 of the calibrated gap chain

**ELABORATES.** On FINISH row 1652, Lean 4.33.1 accepted every definition and theorem statement in `GapChain.Stage0`. Four later-stage proofs are placeholders. The top theorem reports the release's three foundational axioms and `sorryAx`. The physical seed and its implication to a continuum gap are still open. This is research text and grants no scientific status. [Statement file](GapChain/Stage0.lean)

## Statement and witnesses

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the release, its calibration, observables and reconstruction conventions. The outline index and the CA-I sub-index led to the distinctions used here. The outline states the separated-observable hierarchy and illustrates a power-law correlation with spectral support down to zero. CA-I 3216–3222 leaves vacuum uniqueness and a positive gap outside its theorem. The Lean design is Claude Fable's row 1457, §§4.1–4.5, as corrected by the Codex check in row 1458. [Outline, 31760–31795](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31760-L31795) · [Spectral example, 31871–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31871-L31882) · [Complete account, 3216–3222](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3216-L3222) · [Design](../../library/lean-gap-chain-design-fable.md) · [Check](../../library/lean-gap-chain-design-check-astra62.md)

- **Physical hypothesis.** For a fixed admissible calibration level $g_0$, take a positive $\ell$ divisible by four. At every sufficiently late cutoff $K$, the cube has side $\ell L^K$ and $\beta_K=1/g_K^2$ for the release's least-root bare coupling. On that cube `NeutralRankOneTest` requires $w\ge1$, $1024w\le\ell L^K$, and a positive scale and a unit vector giving Hilbert–Schmidt error at most $2/5$. The transfer uses the release's time coordinate 3. $P_0$ is the average of eight explicit Haar-preserving centre actions on slice $L^2$. `MNeutralAll.along` proves the passage from a tail of cutoffs to frequent indices of the extracted strictly increasing sequence. [Trajectory check](../../library/sa-ym4-lean-trajectory-check-astra62.md)
- **Finite-volume quantities.** `NeutralTailLE` requires a summable Peter–Weyl trace and a positive transfer norm. `kappaWeight` uses the signed Pfaffian sum of 64 geometric twists with prefactor $1/8$. Lean proves that the zero twist recovers `Wilson.partition`. The Stage 4 statement asks for the bound $4/21$ at $2w$ and $\max(3,2w)$. The eventual cube size $n\ge2^{70}$ and $4\mid n$ are proved from the cutoff and side hypotheses. [Neutral trace, row 1356](../../library/gap-mini-mneutral-fable.md) · [Twisted transfer, row 1004](../../library/gap-transfer-twisted.md) · [Finite aspect, row 1161](../../library/gap-solve9-astra62.md)
- **Lattice correlation.** `latticeU` is the real part of the explicit finite double sum on the full positive-time complex span of separated real $C^1_c$ tuples. It conjugates the first coefficient, reflects the first tuple, translates the second, and subtracts the squared norm of the mean in the same state. Lists keep both factors at overlapping times. `ExpClusters` tests $(2n+1)a_j$ for $n\ge0$, as required by the link mirror at $-a_j/2$. For each test, infinitely many cutoffs admit a prefactor that works for every $n$. The set of such cutoffs can depend on the test, and each cutoff can have its own prefactor.
- **Continuum conclusion.** Both halves take `Conventions.IsAdmissibleBlockingFactor L`, meaning odd $L\ge13$. `FixedObservableWitnesses.inputs` extracts the increasing cutoffs, positive calibrated couplings, infinite-volume limits and all separated-tuple moment limits. `fixedObservableContinuum_iff` holds by definitional equality. It checks the original quantifier scopes for cutoffs $K$, volumes $v$, states $\nu$, cumulants $S$, the two nontriviality tests, the flat hierarchy and the component decomposition. The outer proof chooses all six witnesses once and then quantifies over seed sides. For those witnesses the asserted semigroup bound on $\Omega^\perp$ is $\exp[-mt]$, with $m=(2/\ell)\log(2^{18}/5041)>0$. Every fixed vector is a multiple of the vacuum. The space is the OS completion of the constructed centred plaquette-energy tensors in the $\mathrm{tr}\,F^2$ sector. The design assigns the larger flat-Schwartz and spectral corollaries to Stage 5. [Release statement, lines 20–64](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/FixedObservableContinuum.lean#L20-L64)

## Proof placeholders

| Stage | Declaration in `GapChain` | Remaining implication |
| --- | --- | --- |
| 2 | `massGap_of_expClusters` | Construct the public tuple-form reconstruction on the named witnesses and pass the frequent odd-grid bound to the completed OS space. |
| 3 | `expClusters_of_kappaSeed` | Propagate the Pfaffian seed through twisted transfer and even slab estimates to clustering in the specified infinite-volume states. Covers W2–W6 and W9–W11, with W5 imported. |
| 4 | `neutralTail_of_rankOneAtTime` | Identify the release's neutral operator trace with the Stage 1 rank-one estimate at $2w$ and bound the tail at $\max(3,2w)$ (W8). |
| 4 | `kappaSeed_of_neutralPhysicalSeed` | Deduce the strict Pfaffian seed $S_\kappa(n/2;n^3)<2^{-18}$ from the periodic neutral trace test in the two flux alternatives (W7). |

The other thirteen theorems have written proofs. `HasMassGap.uniqueVacuum` uses the release's fixed vacuum, subtracts its component from any fixed vector, and applies strict contraction at time one. It has no placeholder dependency. The conditional assembly lemmas that invoke one of the four rows above inherit `sorryAx`.

## Kernel output

Lean's messages below are verbatim. The object imported by the scratch check reproduced all seventeen Stage 0 lines.

```text
'GapChain.centreShift_measurePreserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.centreTranslation_spec' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.twistedPartition_untwisted' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.neutralTail_of_rankOneAtTime' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.neutralPhysicalSeed_of_mNeutral' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.kappaSeed_of_neutralPhysicalSeed' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.MNeutralAll.along' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.HasMassGap.uniqueVacuum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.gapRate_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.massGap_of_expClusters' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.kappaSeedAlong_of_mNeutral' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.expClusters_of_kappaSeed' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.expClusters_of_mNeutral' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.massGap_of_mNeutral' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.fixedObservableContinuum_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.FixedObservableWitnesses.inputs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.su2_fixed_observable_gap_of_mNeutral' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
```

The scratch import also proved that dropping the added clause recovers the release statement, that an actual cube exists at each admissible seed side and cutoff, that the mask counts are eight and 64, and that the zero test has zero correlation at every real time. It printed the following lines for those checks and for the imported results.

```text
'Stage0Check.forgetGap' depends on axioms: [propext, Classical.choice, Quot.sound]
'Stage0Check.eightTranslations' depends on axioms: [propext, Classical.choice, Quot.sound]
'Stage0Check.sixtyFourTwists' depends on axioms: [propext, Classical.choice, Quot.sound]
'Stage0Check.seedCubeExists' depends on axioms: [propext, Classical.choice, Quot.sound]
'Stage0Check.zeroCorrelation' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.su2_fixed_observable_continuum_limit' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.sequenceLemma' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.sequenceLemma_of_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.lemmaM1' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.theoremS' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Build and resource record

The checkout is pinned at `4e52c7dd360c6c2308f1072e6323f4e2e1b439fd`. The compiler is Lean `4.33.1` (`819816b2e0a3bf405af45ae5c7af2491d8f5bee6`), Mathlib is `0df444a360eaa60ab8c11dca51a86af692955474` and the row 1455 release is `3932084a9b82fc79466b4a2faad9ec032b637445`. The release receipt supplies the replay provenance for the imported theorem. All claimed checks here use the pinned kernel and those compiled inputs. The source contains no axiom declaration, `native_decide` or `implemented_by`. [Replay, FINISH row 1455](../../FINISH.md#L1537) · [Stage 1 build provenance](RECEIPT.md) · [Release sources](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean)

The fresh scratch root is `/tmp/sa-lean-gap-chain-stage0-astra62.fEp2U8`. Its `project` has the pinned GapChain sources, the Stage 0 root in its Lake file, and a `.lake/packages` symlink to the built packages. The guard denies writes to the release and rejects external Lean compilation. The no-build preflight reported all 21,134 dependency jobs up to date. Lake's recorded upstream messages were replayed from existing traces. The local build target was `+GapChain.Stage0:olean`, with `LEAN_NUM_THREADS=2` and `/usr/bin/nice -n 10`. Each recorded launch began at or above the 50% system-free threshold.

A direct load reached the resident-memory threshold before checking the declarations. To fit the full import, `archive.py` copied 55,879 archive files (12,253,929,520 bytes) to scratch and compared the SHA-256 of every original with its copy. `resident.py` allowed macOS to discard clean mapped pages of these read-only scratch copies while Lean ran. The scratch setup agreed field for field with Lake's generated setup after the path substitution, across 21,123 modules and 55,883 artifact paths. The four local GapChain imports kept their original paths. Lean used the same binary, options, dependencies and kernel. The final compiler process took 163.272 seconds and reached 3,910,926,336 resident bytes. Lake finished the target in 180.425 seconds. These times include page faults and pauses. The compiled source matched the checkout byte for byte (SHA-256 `eb46735f0a44a13524c1cec8e1c0d3a4f220f3e7fa25f41a81a0c5954a069a1c`). The source, archive manifest, launch scripts and raw logs remain under the scratch root. With `SA` set to that directory, the successful invocation was

```sh
STAGE0_PAGED_ARCHIVES=1 python3 "$SA/run.py" stage0-final "$SA/guard/bin/lake" --no-cache build +GapChain.Stage0:olean
```

The entries use decimal bytes and elapsed wall seconds. Driver peaks and child peaks are Darwin `wait4` counters. The timed version replay used `/usr/bin/time -l`. Each log name denotes `logs/<name>.log`. The detailed counters are in `logs/runs.jsonl` and `logs/compilers.jsonl`.

| Log name | Free at start | Driver wall s / peak bytes | Lean process wall s / peak bytes | Outcome |
| --- | --- | --- | --- | --- |
| `pinned-version` | 74% | 0.511 / 49,790,976 | 0.042 / 49,790,976 | Pinned compiler version, exit 0. |
| `prebuilt-imports` | 74% | 23.562 / 1,028,472,832 | No compiler launched. | Preflight succeeded. All release targets current. |
| `stage0-first` | 74% | 37.566 / 907,444,224 | SequenceLemma ~17 s, TheoremS ~18 s, LemmaM1 ~3.7 s (Lake tasks). Child peaks unavailable. | Local launcher failed before Stage 0. See the missing counters below. |
| `stage0-elaboration` | 73% | 95.384 / 6,051,790,848 | SequenceLemma 20.359 / 2,982,002,688<br>TheoremS 3.063 / 3,391,488,000<br>LemmaM1 4.076 / 3,180,249,088<br>Stage0 52.875 / 6,051,790,848 | Stage 1 passed on serial replay. First full Stage 0 load stopped at the RSS guard. |
| `stage0-direct` | 65% | 6.660 / 1,481,834,496 | Stage0 3.062 / 1,481,834,496 | Lean's module-mode diagnostic rejected legacy Stage 1 imports. |
| `stage0-direct-legacy` | 65% | 11.624 / 6,003,572,736 | Stage0 11.179 / 6,003,572,736 | Direct full load stopped at the RSS guard. |
| `pinned-help` | 65% | 0.066 / 49,823,744 | 0.031 / 49,823,744 | Compiler options help, exit 0. |
| `release-import-alone` | 66% | 9.152 / 5,986,893,824 | Stage0 8.667 / 5,986,893,824 | The fixed-observable import alone reached the RSS guard. |
| `bounded-release-import` | 67% | 0.436 / 696,254,464 | No compiler launched. | Darwin rejected the attempted resource limit before Lean started. |
| `compiler-options` | 67% | 3.913 / 1,330,839,552 | 3.877 / 1,330,839,552 | Compiler-option inventory, exit 0. |
| `public-definitions` | 68% | 33.079 / 5,897,601,024 | Wilson 11.800 / 3,400,859,648<br>Stage0 16.867 / 5,897,601,024 | Wilson and the partial source with smaller imports elaborated. |
| `compact-allocator-import` | 68% | 34.820 / 5,964,480,512 | Stage0 34.396 / 5,964,480,512 | Allocator settings still reached the tighter RSS guard. |
| `stage0-paged` | 66% | 252.797 / 3,917,594,624 | Stage0 229.994 / 3,917,594,624 | Full import loaded. The eventual-cutoff proof failed to elaborate. |
| `stage0-final` | 67% | 180.425 / 3,910,926,336 | Stage0 163.272 / 3,910,926,336 | Final Stage 0 object built. Four designated placeholders. |
| `compiled-interface` | 68% | 137.181 / 3,914,137,600 | Stage0Check 136.645 / 3,914,137,600 | Compiled import and five interface checks passed. |
| `startup-version-replay` | 68% | 0.411 / 51,167,232 | elan/Lean 0.40 / 51,167,232 | Measured repetition of the initial default compiler version probe. |

The initial checkout-wide `~/.elan/bin/lean --version` reported 4.36.0 before individual resource accounting started. The measured replay is the last line of the table. On `stage0-first`, the sandbox denied the recorder's `/bin/ps` call, so the original three child peaks and exact child wall times are unavailable. The next run used a serial lock and Darwin process counters and measured each of those same three local modules. Two early guard stops registered 6,051,790,848 and 6,003,572,736 bytes before termination, above the decimal 6 GB cap. The final full build and compiled-interface check both stayed below 4 GB. The fixture supplied every release object without a rebuild.

Both TeX files were downloaded once at `31a47c543775`. SHA-256 was `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` for the outline and `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` for CA-I.

## Next row

**Stage 2, the upper half.** On these same witnesses, supply reconstruction from the public lattice clauses, identify the odd-grid moments at the negative link mirror, pass the frequent bound to the continuum and extend the estimate to the completed space. The decisive outcome is that `massGap_of_expClusters` and its positive-rate unique-vacuum corollary print only `propext`, `Classical.choice` and `Quot.sound`, or that the first missing implication or false equality is identified on those witnesses. The physical seed remains open.
