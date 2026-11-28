# Repo search

The lead’s November 8 search found a one-step lower bound for a centred Wilson loop on PRs 10114 and 10133. I checked the common source at lines 106–154. Main’s `ph1.md` gives inverse-power decay above a plateau, and `cl1.md` gives density of separated tensors. The requested four Lean names had no hits on main or PRs 10114, 10133, 10134 and 10141. At `fd75828e2` they occur only in Stage 0. The target-specific prior note is absent, and the open registry lists no other final-assembly owner. [Lead search, §11](../../library/prior/repo-search-2026-11-08.md) · [Wilson-loop bound](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L154) · [Plateau bound](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/research/ym4d/library/ph1.md#L278-L311) · [Tensor density](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/research/ym4d/library/cl1.md#L268-L277) · [Open registry](../../library/open-registry.md)

# Row 1670 · Final assembly

**BUILT.** Lean 4.33.1 accepted the four proofs and all four exact Stage 0 type comparisons. The new top theorem depends only on `propext`, `Classical.choice` and `Quot.sound`. This receipt records a research build and grants no status.

For all sufficiently large odd blocking factors $L$, there exist a reference parameter $M$ with torus side at least eight and a $\delta>0$ such that, at all sufficiently late cutoffs, the calibrated coupling is the least positive root of the release’s reference-level equation for every $0<g_0<\delta$. For each such $g_0$ there exist witnesses $K,v,\nu,S,X_2,X_4$ satisfying all of `FixedObservableWitnesses`. Fix these witnesses. For every $\ell$ satisfying `MNeutralAll L M g₀ ℓ`, the reconstructed Osterwalder–Schrader space of the centred, positive-time separated action-density tensors satisfies $\lVert T(t)\psi\rVert\le e^{-mt}\lVert\psi\rVert$ for every $\psi\perp\Omega$ and $t\ge0$, with $m=(2/\ell)\log(2^{18}/5041)>0$. Every vector fixed by all time shifts is a scalar multiple of the vacuum. The premise requires $\ell>0$, $4\mid\ell$ and, at all sufficiently large cutoffs $k$, the calibrated neutral rank-one test on every cube of side $\ell L^k$. This is the `MNeutralAll` hypothesis, distinct from the purity criterion (PUR-io). Existence of such a seed side remains unproved. [Stage 0 definitions](GapChain/Stage0.lean) · [Release statement](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/FixedObservableContinuum.lean#L20-L64)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the release. Their outline illustrates power-law decay with spectral support reaching zero, and their complete account explicitly leaves a positive gap and vacuum uniqueness open. Both texts were fetched once at `31a47c543775`. [Outline index](../../library/sa-index/chunk-29.md) · [Outline, lines 31871–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31871-L31882) · [Complete account I, lines 3212–3222](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3212-L3222)

Claude Fable’s design (1457), Codex’s corrections (1458), and the Stage 0 interface and check (1652–1653) fix the witness order and rate. The finite-cube implications come from Stage 4 (1658, check 1668). The proof of clustering uses Stage 3 (1657, check 1666) and Stage 3b (1667, check 1669 queued at the pin). Stage 2 (1654, check 1665) gives the semigroup estimate. [Design](../../library/lean-gap-chain-design-fable.md) · [Design check](../../library/lean-gap-chain-design-check-astra62.md) · [Stage 0](RECEIPT-0.md) · [Stage 4](RECEIPT-4.md) · [Stage 3b](RECEIPT-3b.md) · [Stage 2](RECEIPT-2.md)

Stage 0’s `neutralPhysicalSeed_of_mNeutral` inherits `sorryAx` through the original neutral-tail declaration. The first proof in `Final` uses `Stage4.neutralTail_of_rankOneAtTime` at the same time `max 3 (2 * w)` and applies `Stage4.kappaSeed_of_neutralPhysicalSeed` on that cube. The next two proofs apply `Stage3b.expClusters_of_kappaSeed`, `Stage2.massGap_of_expClusters` and the proved uniqueness lemma. The top proof takes the release’s six witnesses once, obtains their inputs and applies `MNeutralAll.along` to their increasing cutoffs. [Final module](GapChain/Final.lean)

## Verbatim axiom reports

The five message bodies below come from `logs/final-diagnostics.jsonl`, in source order.

```text
'GapChain.Final.kappaSeedAlong_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Final.expClusters_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Final.massGap_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Final.su2_fixed_observable_gap_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.su2_fixed_observable_continuum_limit' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Build and reproduction

The trusted base is the Lean 4.33.1 kernel (`819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) with the compiled Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`, the row 1455 YM4 release `3932084a9b82fc79466b4a2faad9ec032b637445` and the local proof objects. The kernel checks the exact arithmetic and proof terms. Closed natural-number comparisons use ordinary `decide`. A source scan of `Final.lean` found zero uses of `sorry`, `admit`, `native_decide` or `implemented_by` and zero `axiom` declarations. Each of the 47,189 external artifacts mapped into scratch was SHA-256 checked against its origin.

All eleven local prerequisite sources matched their committed SHA-256 at `fd75828e201422f8609c1de37ba78cf52972920f`. The scratch files `final-inputs.json` and `verified-imports.json` record the local module hashes and external artifact hashes, respectively. The final source SHA-256 is `af33bbe94fa48e63bae58e04ff728bdd30b7e35af2d51acf519cc2d4a6c71dae` and the compiled `Final.olean` SHA-256 is `a1804e4b8f43b869f847e36185e40b670987bceccdcd2168e502341a9ed42c21`.

The initial no-build check identified Stage 4 as the sole stale target. Its earlier Stage 3 object and Stage 3b’s copy differ only in six bytes of the embedded source pathname. Lake therefore recorded different import hashes. Rebuilding the committed Stage 4 source against the shared Stage 3 object reproduced the earlier Stage 4 object byte for byte. The only proof compilations were Stage 4 and Final. The wrapper enforced read-only access to the fixture, serialized the compilers, required at least 50% free from `memory_pressure` before each launch and used `LEAN_NUM_THREADS=2` under `/usr/bin/nice -n 10`. A pager reclaimed clean mapped pages of the scratch imports.

The scratch root is `/tmp/sa-lean-gap-chain-final-astra62.eczrFO`. These commands ran from its `project` directory. The last invocation verified that the target and its dependencies were current.

```sh
python3 ../run.py align-stage4 ../guard/bin/lake --no-cache build +GapChain.Stage4:olean
python3 ../run.py final ../guard/bin/lake --no-cache build +GapChain.Final:olean
python3 ../run.py final-up-to-date ../guard/bin/lake --no-cache --no-build build +GapChain.Final:olean
```

## Run measurements

Times are elapsed wall seconds. Peak RSS is in bytes. The two measured version commands use macOS `/usr/bin/time -l`. The guarded Lean processes use Darwin `wait4`. The first bare `~/.elan/bin/lean --version` resolved to the default 4.36.0. Its enclosing shell took 0.682 s. Its individual wall time and peak RSS were not captured. The measured default replay and pinned compiler probe are included below.

| Lean invocation | Free at launch | Wall s | Peak RSS bytes |
|---|---:|---:|---:|
| Default `--version` replay | — | 0.23 | 50,659,328 |
| Pinned `--version` | — | 0.39 | 50,216,960 |
| `preflight` / `--githash` | 69% | 0.066 | 49,807,360 |
| `align-stage4` / `--githash` | 70% | 0.072 | 49,807,360 |
| `align-stage4` / `Stage4` | 67% | 187.815 | 4,859,412,480 |
| `final` / `--githash` | 68% | 0.071 | 49,774,592 |
| `final` / `Final` | 67% | 176.879 | 4,857,872,384 |
| `final-up-to-date` / `--githash` | 68% | 0.071 | 49,790,976 |

Lake driver wall times were 23.583 s (`preflight`), 260.716 s (`align-stage4`), 202.640 s (`final`), 16.781 s (`final-up-to-date`). The initial no-build preflight exited 3 for the stale local Stage 4 target. The other three drivers exited 0. Raw measurements, diagnostics and full build logs are under `logs/` in the scratch root.

## Next row and decisive outcome

**Proposed row 1671, final assembly faithfulness check.** Following the queued Stage 3b check (1669), trace the six release witnesses through the four exact-type proofs. The decisive outcome is confirmation that the same witnesses give the stated semigroup rate and vacuum conclusion under `MNeutralAll` with exactly the three reported axioms, or the first failing witness identification, type comparison or axiom report.
