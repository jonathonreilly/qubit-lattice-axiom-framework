# Repo search

The lead’s November 8 search covered main and PRs 10114, 10133, 10134 and 10141. I checked those refs for the Lean declarations `massGap_of_expClusters`, `ExpClusters` and `ReflectionMomentsLogConvex`. I found no matching Lean declaration there. Main’s `research/ym4d/library/ph1.md` 278–311 gives an inverse-power bound above the plateau. Its `cl1.md` 268–277 and 345–353 proves tensor density. PR 10114’s `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 gives a positive one-step Wilson-loop correlation. Stage 2 needs an exponential upper bound for the whole reconstructed vacuum complement. The row-specific prior file is absent and the open registry assigns this implication to no other row. [Lead search](../../library/prior/repo-search-2026-11-08.md) · [Registry](../../library/open-registry.md)

In the pinned lane, row 1643 places `wilson_theoremS` at fixed coupling on periodic dyadic cubes. Row 1652 states the exact continuum implication as a placeholder and proves the positive-rate implication from the mass gap to the unique vacuum. Stage 2 supplies the intervening argument on its specified witnesses. [Direction 8, §§1.1 and 3](../../library/gap-direction8-fable.md) · [Wilson assembly](GapChain/Assembly.lean) · [Stage 0 source](GapChain/Stage0.lean)

# Stage 2 of the conditional gap chain

**BUILT.** On Stage 0’s calibrated witnesses, `ExpClusters L K ν m` with $m>0$ implies `HasMassGap (centredOf S) m` and `HasUniqueVacuum (centredOf S)`. The kernel checked the one-line agreement with the exact type of `GapChain.massGap_of_expClusters`. All 33 new theorems report exactly `propext`, `Classical.choice` and `Quot.sound`. Exponential clustering remains the physical hypothesis of this implication. [Stage 2 source](GapChain/Stage2.lean)

Research build record for FINISH row 1654, checkout `1a3355b0c9e1bdeca72e7abaf5244203042fd98f`. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the YM4 release at `3932084a9b82`. The argument follows Claude Fable’s design in row 1457 and the corrections from GPT-6.2 Astra in row 1458. Row 1455 supplies the compiled release. Row 1459 supplies the scalar sequence lemma. Row 1652 supplies the public witness types and the positive-rate uniqueness implication. [Design, §5.1](../../library/lean-gap-chain-design-fable.md) · [Design check](../../library/lean-gap-chain-design-check-astra62.md) · [Stage 0](RECEIPT-0.md)

The full-read outline index points to the link-mirror scalar-product limit at lines 25834–25847, UI2–UI3 at 28272–28288, and reconstructed Hilbert space, clustering and scope at 31760–31797 and 31871–31882. Complete account I, lines 3216–3222, leaves uniqueness and a mass gap outside its theorem. Both upstream TeX files were fetched once at revision `31a47c543775` into the fresh scratch root. [Outline index](../../library/sa-index/README.md) · [Outline, Hilbert space and clustering](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31760-L31797) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3216-L3222)

## Proof on the named witnesses

1. The reconstruction triple uses cutoff `K i.natPred` and state `ν i.natPred`. The inverse reindexing is `j.succPNat`. Gibbs symmetry supplies a common face mean at each cutoff. The release identifies the tuple representative with the product centered in that very state. Moment convergence to the given `S`, reflection positivity and the release’s tuple-form reconstruction theorem yield `HasReconstruction (centredOf S) hp`.
2. For a fixed positive-time formal span $Z$, subtract its finite-cutoff expectation. Once the mesh $a$ is at most its support margin, this centered representative belongs to the upper algebra for the link mirror at $-a/2$. With insertion $1$, the $n$-fold transfer is translation by $2na$. Translating both factors forward one more step moves the reflected factor to the site reflection and the other to displacement $(2n+1)a$. The release’s product identity and the two means give exactly Stage 0’s `latticeU`, including its complex conjugation and squared-mean subtraction.
3. At each cutoff supplied by `ExpClusters`, reflection positivity gives real nonnegative, log-convex odd moments. `sequenceLemma_of_bound` and iteration give a ratio estimate between two odd times without the cutoff’s prefactor. Odd $L$ makes every coarse odd time odd at all later levels. For a fixed $Z$ and pair of coarse times, the frequent cutoffs intersect both eventual conditions on mesh size and refinement. Convergence of the two fixed moments passes the ratio estimate to the continuum. Rounding any $t ≥ 0$ to an odd midpoint costs at most one coarse spacing. Strong continuity permits that spacing to tend to zero.
4. The vacuum matrix coefficient agrees with the tuple mean by span induction. In the completed OS Hilbert space the centered covariance is continuous in the vector at each time. The dense range of `posClass` therefore extends the estimate to every vector, so vacuum orthogonality can be imposed after completion. On that complement the self-adjoint semigroup at $2t$ gives the squared norm at $t$. Taking the nonnegative square root preserves the rate $m$. The positive-rate uniqueness implication is the one already checked in row 1652.

## Kernel and build

The trusted base is the Lean 4.33.1 kernel at `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, with the replayed import objects for Mathlib `0df444a360eaa60ab8c11dca51a86af692955474` and the Sussman–Alpoge YM4 release `3932084a9b82fc79466b4a2faad9ec032b637445`. The build used the ordinary kernel and the default proof heartbeat limit. The imported Stage 0 module has its four declared placeholders. The agreement example takes the type of its upper-half declaration. The 33 axiom reports below give the transitive logical dependencies of the new proofs.

Scratch root `/tmp/sa-lean-gap-chain-stage2-astra62.TJDzKD` contains the Lake project, source snapshots, compiled object and logs. The project copied the committed GapChain sources, added roots `GapChain.Stage0` and `GapChain.Stage2`, and linked `.lake/packages` to the fixture. The no-build dependency preflight reported 21,134 jobs current. The Stage 0 target compiled its four local prerequisites and Stage 0. The final command `lake --no-cache build +GapChain.Stage2:olean` built only Stage 2 and returned `Build completed successfully (21141 jobs).` A subsequent `--no-build` check of both roots returned `All targets up-to-date (21141 jobs).`

All builds ran serially with `LEAN_NUM_THREADS=2` under `/usr/bin/nice -n 10`. The runner queried `memory_pressure` before each start and enforced the 50% threshold. A file lock serialized compiler processes. The fixture was read-only, and the compiler wrapper rejected any source outside the local module allowlist. To stay under 6 GB, the wrapper redirected import paths to 55,879 read-only scratch artifacts (12,253,929,520 bytes) whose SHA-256 hashes matched the originals at copy time. It periodically released clean file-backed pages of those scratch copies. The compiler, module contents and proof-checking settings used the pinned toolchain. The final Stage 2 compiler took **184.408 s** and peaked at **4,661,018,624 bytes RSS**. The Lake run took **209.328 s**.

| Item | SHA-256 |
|---|---|
| Stage 2 source, identical in the checkout and build project | `989e49720b4d8093479812dec3d85fbd03eba02124a6f1dc27fe37810b33db87` |
| `project/.lake/build/lib/lean/GapChain/Stage2.olean` | `586be6fa3e0f31f0d6d1cdd621908f2566e085ce972f321e2d9f694625b34a7d` |
| `sa_ym4.tex`, 32,992 lines | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `sa_ca_I.tex`, 166,711 lines | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |

## Run measurements

The table gives elapsed wall time and Darwin maximum resident set size for each compiler process and its enclosing driver. Driver and child times overlap. The first required bare `~/.elan/bin/lean --version` query reported the machine default 4.36.0 in about 0.12 s. Peak RSS was unrecorded for that initial query. Its measured replay took 0.66 s and used 51,249,152 bytes RSS. The project selected 4.33.1 for every proof. Raw measurements are in `logs/runs.jsonl`, compiler output in `logs/<run>.log`, and import hashes in `archive.tsv`, all under the scratch root.

The first Stage 2 draft exposed implicit-argument errors. Attempt 02 tried a saved compiler header and stopped before elaboration with ``region_reader: dep regions have overlapping `base_addr` ranges``. Attempts 03–07 used ordinary imports and exposed proof elaboration errors. The final two fixes supplied the reconstruction spacing explicitly to `translate_negativeMirror` and the lattice-membership proof at that same spacing to `dif_pos`. Attempt 08 checked the full proof. The final Lake build also checked it at the default heartbeat limit and emitted the compiled object.

| Run | Process | Free before start | Wall seconds | Peak RSS, bytes | Exit |
|---|---|---:|---:|---:|---:|
| `pinned-version/version` | lean | 69% | 0.113 | 49,758,208 | 0 |
| `pinned-version` | driver | 69% | 0.621 | 49,758,208 | 0 |
| `preflight` | driver | 69% | 26.698 | 955,809,792 | 0 |
| `stage0/SequenceLemma` | lean | 68% | 20.434 | 2,983,165,952 | 0 |
| `stage0/TheoremS` | lean | 68% | 3.164 | 3,401,302,016 | 0 |
| `stage0/LemmaM1` | lean | 69% | 3.712 | 3,180,527,616 | 0 |
| `stage0/Wilson` | lean | 68% | 5.117 | 3,397,632,000 | 0 |
| `compiler-help` | driver | 65% | 0.312 | 49,807,360 | 0 |
| `stage0/Stage0` | lean | 68% | 217.726 | 3,615,637,504 | 0 |
| `stage0` | driver | 69% | 273.102 | 3,615,637,504 | 0 |
| `stage2-01/Stage2` | lean | 69% | 273.663 | 4,667,408,384 | 1 |
| `stage2-01` | driver | 69% | 296.567 | 4,667,408,384 | 1 |
| `stage2-02/Stage2` | lean | 67% | 3.291 | 1,853,095,936 | 1 |
| `stage2-02` | driver | 67% | 8.372 | 1,853,095,936 | 1 |
| `default-version-replay` | driver | 64% | 0.912 | 51,249,152 | 0 |
| `stage2-03/Stage2` | lean | 67% | 157.217 | 4,664,164,352 | 1 |
| `stage2-03` | driver | 67% | 161.965 | 4,664,164,352 | 1 |
| `stage2-04/Stage2` | lean | 67% | 195.983 | 4,664,999,936 | 1 |
| `stage2-04` | driver | 68% | 200.628 | 4,664,999,936 | 1 |
| `stage2-05/Stage2` | lean | 68% | 274.570 | 4,665,835,520 | 1 |
| `stage2-05` | driver | 68% | 279.350 | 4,665,835,520 | 1 |
| `stage2-06/Stage2` | lean | 68% | 206.207 | 4,700,143,616 | 1 |
| `stage2-06` | driver | 68% | 211.187 | 4,700,143,616 | 1 |
| `stage2-07/Stage2` | lean | 68% | 156.371 | 4,668,833,792 | 1 |
| `stage2-07` | driver | 68% | 161.063 | 4,668,833,792 | 1 |
| `stage2-08/Stage2` | lean | 67% | 156.218 | 4,662,509,568 | 0 |
| `stage2-08` | driver | 67% | 160.982 | 4,662,509,568 | 0 |
| `stage2-final/Stage2` | lean | 67% | 184.408 | 4,661,018,624 | 0 |
| `stage2-final` | driver | 67% | 209.328 | 4,661,018,624 | 0 |
| `final-up-to-date` | driver | 66% | 16.952 | 983,613,440 | 0 |

## Verbatim axiom reports

```text
'GapChain.Stage2.gibbsAt' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.faceMeanData' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.mesh_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.approximation_rp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.integral_tupleRep' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.approximation_converges' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.reconstruction' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.latticeU_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.average_tendsto' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.latticeU_tendsto' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.translate_negativeMirror' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.oddDisplacement' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.integral_spanRep' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.centered_pair_integral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.oneInsertion_iterate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.linkTest_mem' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.linkMoments' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.centered_reflectionMoment' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.translated_pair' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.oddMoment_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.oddGrid_ratio' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.cutoff_ratio' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.scale_tendsto_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.refine_odd_times' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.continuum_grid_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.oddTime_floor_dist' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.bound_all_times' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.vacuum_mean' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.osCovariance_continuous' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.osCovariance_posClass' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.completed_covariance_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.massGap_of_expClusters' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.uniqueVacuum_of_expClusters' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Next row

Stage 3 has the lower implication, `expClusters_of_kappaSeed`. It must propagate the calibrated Pfaffian seed to frequent-cutoff exponential clustering on the same `K` and `ν` for a positive rate. Its decisive outcome is a kernel build at Stage 0’s exact type with only `propext`, `Classical.choice` and `Quot.sound`, or a precise statement of the first missing estimate or witness identification. [Stage 0 handoff](RECEIPT-0.md)
