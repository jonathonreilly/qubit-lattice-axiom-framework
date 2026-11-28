# Repo search

The lead searched main and PRs 10114, 10133, 10134 and 10141. I reopened the finite-clock Villain and Dirichlet Maxwell models on main (`8b11ae2bb9`) and the one-step Haar plaquette witness on PR 10114 (`f76f6c649c`, lines 106–149). The first two use different measures. The third bounds a correlation. I found no matching Lean declaration outside this lane at those heads or at `89faef229f`, `1e70c7211a` and `a2f6a430e2`. The row-specific prior file was absent, and the registry search found no competing assignment. [Lead search](../../library/prior/repo-search-2026-11-08.md)

At the checkout pin `2ff9eeb6b15eda8f8e65d55b49e4535f9bb0a133`, row 1504 supplies the Wilson partition function and `fields_of_bridge`. Row 1506 supplies the pointwise kernel and its spectral witness. Row 1508 owns the cyclic spectral identity. [Stage 1b](RECEIPT-1b.md) · [Stage 1c](RECEIPT-1c.md)

## Outcome

**BUILT (A and B), FINISH row 1509.** Lean 4.33.1 built the six-root library and a separate importing consumer. The Mac mini runner used `gpt-6.2-astra` at max effort. This finite-volume research receipt grants no audit status.

- **A.** `GapChain.Wilson.Periodic.Z_eq_cyclic` proves `Z β a R = cyclic β R a` for every real β, every box R and every natural time period a. The consumer proves `Z β 0 R = 1`. [Periodic.lean](GapChain/Periodic.lean)
- **B.** For β > 0, `torusData_of_trace` constructs a `TorusData` from one hypothesis. On each valid R and for every a ≥ 3, the cyclic integral must equal the sum of the a-th powers over `PositiveSlot (transfer β R)`. The theorem `torusData_of_trace_spectrum` identifies its valid-box spectrum with the witness chosen from `transfer_boxSpectrum`, including its top eigenvalue and multiplicities. The consumer proves that its weights equal `Z` on that domain. The total spectrum function uses the side-3 cube at the same coupling on invalid boxes. The physical seed estimate remains open.

The consumer defines the cyclic integral from the exact row 1508 interface in a separate namespace, proves equality of the two functions by `rfl`, and passes that namespace's trace hypothesis directly to the constructor. Integration with the separately produced `Trace.lean` is the first proposed row below.

## Proof and sources

1. `layers` is a measurable equivalence from all four-dimensional links to a pair of time-indexed families, spatial slices and vertex gauges. `measurePreserving_layers` sends product link Haar to the product of their time-indexed Haar measures. Each link occurs exactly once.
2. `action_eq_geometric` uses `halfTrace_reverse` to combine the two orientations of each plaquette. `action_eq_layers` splits the six geometric planes into three spatial and three temporal planes. In the (0,i) plane the word is $g_t(x)u_{t+1}(x,i)g_t(x+e_i)^{-1}u_t(x,i)^{-1}$, with time advanced by `finRotate`. Claude Opus 5.5 gives the hand construction in row 667, §1.1–1.3, and its extension to unequal spatial sides in row 698, Lemma 1.1. [Row 667](../../library/gap-transfer.md) · [Row 698](../../library/gap-seed-check.md)
3. `density_eq_layerProduct` assigns half the spatial action to each endpoint. Rotation permutes the time indices, so the two half sums recover the original spatial sum. After the Haar change of variables, integrability follows from `integrable_density`. Fubini separates the slice and gauge integrals. Each gauge field occurs in a single factor, and `integral_layerWeight` identifies its integral with `transferKernel`.
4. The trace hypothesis, A and the chosen spectral witness give the weight equality required by `fields_of_bridge`. It supplies the crossing and lower-bound fields. The log-convexity field uses Claude Opus 5.5's checked `Check1503.weight_logConvex` proof, ported from the appendix of row 1503. [Row 1503](../../library/lean-gap-chain-stage1-check-opus.md)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the normalized Haar and plaquette conventions and the cubic transfer identity GL8. I checked the indexed outline ranges 240–264 and 2315–2335, and CA-I 447–483, at `31a47c543775`. The rectangular proof above uses the half-spatial-action kernel of row 1506. [Finite lattice conventions](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L240-L264) · [Outline GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [Complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L447-L483)

## Plan

1. Check the pinned sources, prior work, registry ownership and indexed plaquette and transfer conventions.
2. Build a time-slice reindexing of the links, prove the action split, then integrate the temporal links and identify the cyclic product.
3. Port the checked log-convexity proof and construct the conditional torus data from the trace hypothesis.
4. Build the collected module against the specified toolchain, copy its axiom reports, and record run costs, remaining obligations and the next two rows.

## Kernel verification and run record

The trusted base is the Lean 4.33.1 kernel at `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, its core library, and the compiled Mathlib package environment at `0df444a360eaa60ab8c11dca51a86af692955474` with its manifest dependencies. The five prerequisite gap-chain modules were built from byte-identical copies of the pinned Git sources. The proof uses kernel-checked terms throughout. The source scan found zero admissions, axiom declarations, uses of `native_decide` or uses of `implemented_by`. The successful module and consumer emitted eight identical axiom messages and zero warnings or errors.

The collected `Periodic.lean` is byte-identical to the built source. Its SHA-256 is `308cf7fa1ef8b6dc510992ea5fe28bc56829f7651f32a843e83804064d35248d`. The scratch project, minimal consumer, raw compiler output, build logs and timing records are under `/tmp/sa-lean-gap-chain-stage1e-astra62.a370G5`. The two build logs are `logs/base.log` and `logs/factor-02.log`. The per-step receipt before final verification is in `logs/checkpoint-before-final.md`.

- The first build compiled all five prerequisites. It stopped on the coordinate reductions for periodic steps, an elaboration timeout, and the finite-subset overload of the permutation sum lemma. The correction exposes the zero and successor coordinates, supplies the site summand explicitly, and uses `Equiv.sum_comp` on the full time index. The action proof has a local elaboration budget of 800,000 heartbeats.
- The build used the committed library configuration in scratch with the Periodic root added. The corrected command was `lake build GapChain Consumer`. The scratch manifest uses the pinned package revision and the Git URL from the committed configuration. A filesystem sandbox protected the fixture from writes.
- Both builds used `/usr/bin/nice -n 10` and `LEAN_NUM_THREADS=2`, with serialized compiler children. They began at 52% and 51% free memory. The child readings below were taken inside each active build. The initial checkout version probe selected Lean 4.36.0 and was unmetered. Its timed replay and the explicit version check of the proof toolchain appear below.

Wall time is in seconds. Peak RSS is Darwin `wait4.ru_maxrss` in bytes. Times are UTC on 2026-11-25. Build wall time starts at the qualifying memory reading. The receipt was opened at 02:35 UTC, and the successful library and consumer build finished at 05:15 UTC.

| Invocation | Start UTC | Free | Exit | Wall s | Peak RSS bytes |
| --- | --- | ---: | ---: | ---: | ---: |
| Initial version probe, timed replay | 02:42:51 | 39% | 0 | 1.03 | 51,216,384 |
| Pinned toolchain version | 02:42:52 | 39% | 0 | 0.06 | 50,249,728 |
| Lake build · base | 03:22:56 | 52% | 1 | 239.41 | 2,451,718,144 |
| base · SequenceLemma.lean | 03:23:04 | 40% | 0 | 22.40 | 2,326,429,696 |
| base · TheoremS.lean | 03:23:27 | 39% | 0 | 35.67 | 2,195,226,624 |
| base · LemmaM1.lean | 03:24:02 | 38% | 0 | 42.17 | 2,246,082,560 |
| base · Wilson.lean | 03:24:45 | 40% | 0 | 41.05 | 2,451,718,144 |
| base · Transfer.lean | 03:25:26 | 39% | 0 | 39.66 | 2,216,165,376 |
| base · Periodic.lean | 03:26:06 | 46% | 1 | 49.36 | 2,160,754,688 |
| Lake build · factor-02 | 05:13:39 | 51% | 0 | 112.18 | 2,221,981,696 |
| factor-02 · Periodic.lean | 05:13:46 | 40% | 0 | 36.83 | 2,221,981,696 |
| factor-02 · Consumer.lean | 05:14:23 | 37% | 0 | 67.77 | 1,583,480,832 |

## Verbatim axiom reports

```text
'GapChain.Wilson.Periodic.measurePreserving_layers' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Periodic.action_eq_layers' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Periodic.integral_layerWeight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Periodic.density_eq_layerProduct' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Periodic.Z_eq_cyclic' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Periodic.weight_logConvex' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Periodic.torusData_of_trace' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Periodic.torusData_of_trace_spectrum' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Next two proposed rows and their decisive outcomes

1. **Join rows 1508 and 1509.** Import the actual Trace and Periodic modules in one consumer and supply row 1508’s theorem to `torusData_of_trace`. The decisive outcome is a kernel-checked Wilson `TorusData` with only β and its positivity proof as inputs, together with its valid-box weight equality to `Z` for all a ≥ 3.
2. **Prove a physical Wilson seed bound.** For a specified Wilson coupling in the intended regime and a specified N ≥ 3, prove `T.seed N < 1 / 5041`, where `T.seed N` is `(T.spectrum (cube (2 * N))).thermal N`. The decisive outcome is a kernel-checked seed inequality that instantiates `TorusData.corollaryS3'` for every L ≥ 2N. [Seed and spectral-gap consumer](GapChain/TheoremS.lean)
