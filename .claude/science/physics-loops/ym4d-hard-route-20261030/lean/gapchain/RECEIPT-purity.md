# Repo search

The lead’s November 8 search found a one-step lower bound for a centred Wilson loop. I checked lines 106–149 on PR 10114 and the identical source blob on PR 10133. Purity uses the whole neutral trace at two periods. Main’s orbit-space proposal leaves its curvature bound open. A search for the Lean names, the neutral purity and the fraction 457/625 found no match in Lean sources at the pin, on main or on PRs 10114, 10133, 10134, 10141 and 10144. The target-specific prior file is absent. The registry’s purity entries concern estimates on Wilson cubes. [Lead search, §11](../../library/prior/repo-search-2026-11-08.md) · [One-step bound](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L149) · [Orbit-space proposal, lines 188–195](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/research/mass-gap/library/gap-skeleton-max-b.md#L188-L195) · [Registry](../../library/open-registry.md)

Fact PUR comes from Codex rows 1373 and 1461, checked by Claude Opus in 1465 and restated by Claude Fable in 1468 §3.1. Gemini Neon records the two-period trace convention in row 1526. Row 1670 assembled the rank-one gap theorem, and row 1671 reproduced it. Codex check 1675 identified the direct route through the physical seed that is formalized here. [Fact PUR](../../library/gap-k2-tool-design-fable.md#31-the-consumer-sixteen-masses) · [Trace convention](../../library/gap-agy-seed-approaches-neon.md#L12) · [Final assembly](RECEIPT-final.md) · [Reproduction](../../library/lean-gap-chain-final-check-opus.md) · [Check 1675](../../library/gap-direction9-check-astra62.md)

## Row 1676

**BUILT.** Lean 4.33.1 accepted `GapChain.Purity.su2_fixed_observable_gap_of_purity` and its seven supporting theorems. For each calibrated choice in the release’s `FixedObservableLimit`, the theorem chooses $K,v,\nu,S,X_2,X_4$ once, with all of `FixedObservableWitnesses`. Every physical side ℓ satisfying `PurityAlong L M g₀ ℓ K` then gives `HasMassGap (centredOf S) (gapRate ℓ)` and `HasUniqueVacuum (centredOf S)`. Each proof uses only `propext`, `Classical.choice` and `Quot.sound`. Research build on `67a98bbb89843b4c3c327d7bac0bd13b6ad41545`. This record grants no status. [Purity module](GapChain/Purity.lean)

The frequency premise is indexed by the release witnesses’ own sequence `K`. An infinite passing set of original cutoffs may miss this sequence. Using PUR-io requires choosing release witnesses inside the passing set and establishing their continuum clauses there. No Wilson purity lower bound is proved. [Check 1653, §1.4](../../library/lean-gap-chain-stage0-check-opus.md) · [Check 1675](../../library/gap-direction9-check-astra62.md)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the release transfer, its Peter–Weyl trace and the fixed-observable continuum witnesses. Their outline exhibits a quadratically decaying correlation with spectral support reaching zero. Their complete account leaves the mass gap and vacuum uniqueness open. Both texts were fetched at `31a47c543775`. [Outline index](../../library/sa-index/chunk-01.md) · [Outline, lines 588–599](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L588-L599) · [Complete account I, lines 2692–2713](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2692-L2713) · [Fixed-observable release](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/FixedObservableContinuum.lean#L167-L171)

## Proof

The definition takes the real part of the complex trace quotient. For $\beta>0$ and $u\ge2$, `purity_eq_traceRatio` proves that coercing this real value back to ℂ recovers the quotient itself. Both traces use Stage 0’s `neutralProj`, the release transfer along `TimeAxis.timeIdx` and the release’s sum of diagonal Peter–Weyl entries. [Release trace](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/Construction/Matrices/HilbertSchmidtOperatorsTraceClassAndTraceOnG.lean#L13-L16) · [Neutral tail](GapChain/Stage0.lean#L86)

Stage 4 identifies the traces with real sector weights. The powers of the common transfer norm cancel in their ratio. On a cube of side $n$ divisible by four, the normalized neutral moments are convergent spectral sums. Write $D=\sum_i x_i$, where $x_i$ is the $i$th neutral eigenvalue at time $u$ in units of the vacuum eigenvalue at that time. The vacuum slot contributes one. The summable moment at $2u$ satisfies $\sum_i x_i^2\le D$ because $0\le x_i\le1$. Hence $2/3\le P\le1/D$ implies $D-1\le1/2$. The finite-cube theorem takes $u=\lfloor n/512\rfloor$ and uses $1536\le n$ for $3\le u$. The later Pfaffian estimate uses $2^{70}\le n$. [Stage 3 calibration](GapChain/Stage3.lean#L5920) · [Stage 4 trace and moments](GapChain/Stage4.lean#L111) · [Stage 4 spectrum](GapChain/Stage4.lean#L902)

For a positive side ℓ divisible by 1024, intersect the frequent passing indices with the eventual bound $K(j)\ge70$. Every cube there has side $n=\ell L^{K(j)}$, with $4\mid n$ and $2^{70}\le n$. Exact rational arithmetic gives $457/625>2/3$. Stage 4 gives the Pfaffian seed on each such cube. Stages 3b and 2 give the semigroup gap at $m=(2/\ell)\log(2^{18}/5041)>0$ in the centred action-density sector. The positive rate gives a unique vacuum. [Stage 4](GapChain/Stage4.lean#L1372) · [Stage 3b](GapChain/Stage3b.lean#L688) · [Stage 2](GapChain/Stage2.lean#L588) · [Rate](GapChain/Stage0.lean#L243)

## Verbatim axiom reports

The eight message bodies are copied from the final compiler run, in source order.

```text
'GapChain.Purity.neutralTrace_eq_scaledMoment' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Purity.purity_eq_traceRatio' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Purity.purity_eq_sectorMoments' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Purity.neutralTailLE_of_purity' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Purity.neutralPhysicalSeed_of_purity' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Purity.kappaSeedAlong_of_purity' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Purity.massGap_of_purity' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Purity.su2_fixed_observable_gap_of_purity' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Trusted base and build

The trusted base is the Lean 4.33.1 kernel (`819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) and its imported compiled declarations, including Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`, the YM4 release `3932084a9b82fc79466b4a2faad9ec032b637445` and the twelve local prerequisites from row 1670. The arithmetic tactics produce proof terms checked by the kernel. The final source scan found zero uses of `sorry`, `admit`, `native_decide` or `implemented_by` and zero axiom declarations.

Each local source matched both its Git blob at the pin and the row 1670 scratch copy by SHA-256. Each copied olean matched the corresponding build digest. The guard reused row 1670’s archived imports and SHA-256 manifest, checking the file identities, sizes and timestamps of all 47,189 mapped artifacts against their originals. The sandbox made the release, toolchain and prior scratch read-only. A single compiler ran at a time under `/usr/bin/nice -n 10`, with `LEAN_NUM_THREADS=2`, the row 1670 pager and at least 50% free memory required by the guard. Both proof runs compiled only `GapChain.Purity`. The final run emitted eight information messages and zero warnings or errors.

The scratch root is `/tmp/sa-lean-gap-chain-purity-astra62.dfmuFs`. From its `project` directory, the prerequisite preflight, final compilation and final currency check used the following commands. The last reported `All targets up-to-date (21148 jobs).`

```sh
python3 ../run.py preflight ../guard/bin/lake --no-cache --no-build build +GapChain.Final:olean
python3 ../run.py purity ../guard/bin/lake --no-cache build +GapChain.Purity:olean
python3 ../run.py purity-up-to-date ../guard/bin/lake --no-cache --no-build build +GapChain.Purity:olean
```

The delivered source is byte-identical to the compiled input. Its SHA-256 is `07895d22b4d9703f04e90f5bb6157a5b7e98cd4b5391f50e185fe1d5a93ed6b2`. The 422,944-byte `Purity.olean` has SHA-256 `d8eb1ecae5938eff8fa581e639f4d85cc8cf545cb40ff968e142eb220805311c`. The scratch root holds `local-inputs.json`, `proof-result.json`, `axioms-purity.txt` and the full driver and compiler logs under `logs/`.

## Run measurements

The required first bare version probe resolved to the machine default, Lean 4.36.0. Its enclosing command took 0.645 s and its peak RSS was not captured. The measured replay and the pinned version probe used macOS `/usr/bin/time -l`. The guard measured every Lean child of Lake with Darwin `wait4`. Both compilation attempts succeeded. The first emitted one unused-variable warning. The final source uses the side hypothesis explicitly.

| Lean invocation | Free at launch | Wall s | Peak RSS bytes |
|---|---:|---:|---:|
| Initial default `--version` | — | 0.645 (enclosing command) | unrecorded |
| Default `--version` replay | — | 0.23 | 50,642,944 |
| Pinned `--version` | — | 0.35 | 50,200,576 |
| `preflight` / `--githash` | 70% | 0.072 | 49,790,976 |
| `purity-1` / `--githash` | 70% | 0.072 | 49,807,360 |
| `purity-1` / `Purity` | 70% | 165.544 | 4,857,806,848 |
| `purity` / `--githash` | 64% | 0.071 | 49,790,976 |
| `purity` / `Purity` | 64% | 171.218 | 4,856,922,112 |
| `purity-up-to-date` / `--githash` | 65% | 0.062 | 49,790,976 |

Lake driver wall times were 23.151 s (`preflight`), 193.171 s (`purity-1`), 196.882 s (`purity`), 17.069 s (`purity-up-to-date`). All four drivers exited 0.

## Next row and decisive outcome

**Proposed next proof row — select release witnesses inside a PUR-io passing set.** Fix calibrated $L,M,g_0$ and a positive side ℓ divisible by 1024. Suppose an infinite set of original cutoffs $k$ passes the $457/625$ test on every cube of side $\ell L^k$. Construct the six release witnesses with their increasing cutoff sequence inside that set and all clauses of `FixedObservableWitnesses`. The decisive outcome is a kernel-checked gap and unique vacuum for the resulting extracted limit under PUR-io, with the same three axioms, or the first release witness clause for which selection inside the set remains unproved.
