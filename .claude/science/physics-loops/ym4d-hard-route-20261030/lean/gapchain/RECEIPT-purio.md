# Repo search

The lead’s November 8 digest found a one-step Wilson-loop correlation bound on PR 10114. I checked its operator inequality and the identical source blob on PR 10133. It controls one finite-lattice observable. Main’s orbit-space proposal asks for a curvature bound. A Lean-source search on main and local PR heads 10114, 10133, 10134, 10141 and 10144 found no `FixedObservableWitnesses` or `PurityAlong`. The registry assigns Wilson purity estimates to other rows. I found no owner for this extraction and no target-specific prior file. [Lead digest, §11](../../library/prior/repo-search-2026-11-08.md#11-w1w2w5-witness-matching) · [One-step inequality](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L149) · [Orbit-space proposal](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/research/mass-gap/library/gap-skeleton-max-b.md#L188-L195) · [Registry](../../library/open-registry.md)

Within the lane, row 1652 identifies the full witness predicate by definitional equality, row 1670 assembles the gap, and row 1676 proves the gap and unique vacuum from purity along a chosen sequence. Checks 1653 §1.4 and 1675 identify the mismatch with infinitely many original cutoffs. The earlier trajectory check already identifies the release’s record cutoffs and the bounded-distance first-passage argument. [Stage 0](GapChain/Stage0.lean) · [Row 1670](GapChain/Final.lean) · [Row 1676](GapChain/Purity.lean) · [Trajectory check](../../library/sa-ym4-lean-trajectory-check-astra62.md)

## Row 1678

**BUILT-PARTIAL.** When infinitely many cutoffs of a prescribed passing set are records of the calibrated one-loop table, Lean constructs six witnesses inside that set satisfying `FixedObservableWitnesses` and proves the gap and unique vacuum. For an arbitrary infinite set, Lean constructs the least-root sequence, both coupling limits, infinite-volume states, and a first-passage sequence at one fixed integer offset. A full continuum witness at the original cutoffs for a nonzero offset remains open. Each result carries its own calibration, fixed before $g_0$ and $A$. Mac mini Codex research at `0bd4166853954d5d03959ac5a4c3f4f374e63559`. This receipt grants no scientific status. [PurIo module](GapChain/PurIo.lean)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the YM4 release, outline and complete account. The finite test is the lane’s Fact PUR from rows 1373, 1461 and 1468, with check 1465. For a positive side ℓ divisible by 1024, (PUR-io) means that `passingCutoffs L M g₀ ℓ` is infinite. At each member $k$, every cube of side $n=ℓL^k$ satisfies the $457/625$ bound at $u=n/512$ and $β=\mathrm{betaAt}(L,M,k,g_0)$. The Wilson lower bound remains a hypothesis. [Purity consumer, §3.1](../../library/gap-k2-tool-design-fable.md#31-the-consumer-sixteen-masses) · [Row 1676](RECEIPT-purity.md)

### Where the release chooses the cutoffs

Write $a_t$ for the release’s one-loop coefficients and $s=11\log L/(3\pi^2)$. The first restriction on the outer cutoff is `BranchHot.slope_record_cutoffs`. It gives infinitely many $k$ satisfying

$$
\sum_{i\le t<k} a_t \;\ge\; \tfrac{s}{2}(k-i)\qquad\text{for every }i<k .
$$

`uniform_record_gap` uses this at line 62. The fixed-observable proof takes its result at line 98 and chooses $w$ at lines 102–104. Its other two conditions there, least-root tuning and positive cutoff, hold eventually. Replacing the domain with an infinite $A$ preserves those two conditions. Relative records of the partial sums on $A$ would compare only with earlier members of $A$, whereas first passage requires comparison with **every** earlier level. [Record proof, lines 24–65](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/RecordCutoffs.lean#L24-L65) · [Outer extraction and first passage, lines 98–150](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/FixedObservableContinuum.lean#L98-L150)

The release’s `HasAverageSlope` bounds the absolute error on each interval by $2c$. The exact example $F(n)=n-(n\bmod 2)$, $a_t=F(t+1)-F(t)$ has $s=1$, $c=1$ and nonnegative increments. At every odd $k$, the singleton interval ending at $k$ has sum zero. Lean proves that the infinite set of odd cutoffs is disjoint from the records. This specializes the lane’s alternating-error example and refutes the proposed inference from the average-slope bound. The example concerns an abstract table. The compactness theorem for continuum moments applies after the proof finds a fixed first-passage window on the selected sequence. The outline lists geometric convergence of the physical coefficients as RF10. CA-I 4.2 states the partial-sum bound. The stronger increment estimate already has its own registry owner, `rf10-2`. [Earlier counterexample](../../library/rf10-incr.md#1-the-exact-reduction) · [RF10](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L20348-L20363) · [CA-I 4.2](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3901-L3929) · [Registry](../../library/open-registry.md#L455)

### What Lean proves

1. **Full witnesses on passing records.** `su2_fixed_observable_selection_on_records` chooses the calibration $M,δ$ and the one-loop table before $g_0$ or $A$. If $A$ meets the records infinitely often, it starts $w$ in that intersection. No-escape and the recurrent window apply to this $w$. The release then returns a further subsequence $w\circ φ$ still in the intersection. The theorem returns the entire `FixedObservableWitnesses` conjunction, including growing tori, both families of cumulant and centred-moment limits, the positive smooth tests, the mixture’s Schwinger representative and the canonical component export. For $A$ passing at ℓ, row 1676 gives `HasMassGap (centredOf S) (gapRate ℓ)` and `HasUniqueVacuum (centredOf S)`. **$S$ can depend on $A$ and hence on ℓ when the passing set is chosen for ℓ.** [Release passage export](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/ContinuumLimit.lean#L117-L165) · [Witness conjunction](GapChain/Stage0.lean#L296-L348)
2. **A sufficient test using only passing cutoffs.** Choose $d>4c/s$. Maximizing $F(k)=\sum_{t<k}a_t-sk/2$ up through $n+d$ gives a record in $[n,n+d]$. A maximizer before $n$ would be below $F(n+d)$ by the interval estimate. Thus `su2_fixed_observable_gap_of_passing_blocks` needs only arbitrarily late runs of $d+1$ consecutive passing cutoffs, for one $d$ chosen from the calibration. Its conclusion puts every witness cutoff inside the prescribed set. [Block and selection proofs](GapChain/PurIo.lean)
3. **Arbitrary infinite sets, with the original bare coupling.** `su2_fixed_observable_cutoffs_at_fixed_offset` gives strictly increasing $K,J$, original infinite-volume states $ν_j$, and one $r\ge0$ such that $K_j\in A$ and $K_j=J_j+r$ for every $j$. The least root is the one at $K_j$. With $β_j=g_{K_j}^{-2}$, Lean proves $g_{K_j}^2 K_j\log L\to3\pi^2/11$ and $β_j/(K_j\log L)\to11/(3\pi^2)$. Every $(J_j,β_j)$ is a first-passage pair for **one** admissible window. The recurrent interval has width one. Descent bounds $K-J$ by `runDepth lam (cr + 1)` strictly, and finite pigeonhole fixes $r$. The slope at $J$ transfers because $J/(J+r)\to1$. This formalizes the relevant BND-2 argument of rows 1451 and 1453 for the varying terminal values of the least roots. [Trajectory check](../../library/sa-ym4-lean-trajectory-check-astra62.md) · [Release first-passage arithmetic](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/FirstPassageOfATunedPair.lean#L36-L60)

For $r>0$ the passage theorem supplies moments and OS representatives at mesh $L^{-J}$, while the requested witnesses use mesh $L^{-K}$. The first missing step on this route is to transport the *joint* passage export to $J+r$ at the same $β_j$. Original-mesh infinite-volume states chosen merely by compactness need a proof that their moments match the transported limit. The release’s torus dilation theorem gives exact finite-volume cumulant identities. Its tuned-sequence theorem uses a common terminal value and exports a fixed-torus limit. The outline’s diagonal lemma requires uniform bounds on the chosen sequence. The full volume-first transport requires a further proof. [Finite torus dilation](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/DilationOfSeparatedTuples.lean#L167-L177) · [Tuned torus limit](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/LimitsOfATunedSequence.lean#L54-L81) · [Outline RF53](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L22014-L22040) · [Outline diagonal lemma](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L479-L523)

### Kernel verification

The trusted base is the Lean 4.33.1 kernel (`819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) and its imported compiled declarations, including Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`, the read-only YM4 release `3932084a9b82fc79466b4a2faad9ec032b637445`, and the 13 local prerequisites through row 1676. All 13 scratch sources matched the pinned Git blobs and their build manifests by SHA-256. All 13 oleans matched the row 1676 manifest or its Purity receipt. The inherited pager used 47,189 verified external artifacts. The guard admitted only this module for compilation. The arithmetic tactics produced kernel-checked proof terms. The final module emitted ten information messages, with zero warnings or errors. Its source scan passed the restrictions on proof placeholders, extra axioms, compiled evaluation and implementation overrides.

```text
'GapChain.PurIo.record_in_every_block' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.averageSlope_can_miss_infinite_set' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.drop_at_record' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.exists_coupling_at_threshold' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.coupling_limit_of_beta_limit' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.su2_fixed_observable_selection_on_records' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.su2_fixed_observable_gap_of_passing_blocks' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.passage_before_endpoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.coupling_limits_at_offset' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PurIo.su2_fixed_observable_cutoffs_at_fixed_offset' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Source SHA-256 `956de7cf4da125b22485c69e31323a3c9e9c7424840eb00510286d1c1076e14b`. The compiled olean has 1,867,784 bytes and SHA-256 `b0570550a7f9c9ec7bf06bee49d56f857b5e1cc1500ff91c5e5a0fa65861e34d`. The delivered source matches the compiled input byte for byte. Full compiler diagnostics, timings, the verified input manifest and the olean are under `/tmp/sa-lean-gap-chain-purio-select-astra62.GkSZwJ`. The outline and CA-I were each fetched once at `31a47c543775` into that fresh scratch directory.

### Run measurements

Lean ran serially with `LEAN_NUM_THREADS=2`, `/usr/bin/nice -n 10`, the row 1670/1676 pager and a 50% free-memory admission threshold. The sandbox protected the fixture, toolchain and prior build. The no-build prerequisite preflight reported `All targets up-to-date (21148 jobs).` Lake reported an inherited Mathlib manifest URL warning. The installed revision matched the requested pin. From the scratch `project` directory the final proof build and currency check used

```sh
python3 ../run.py purio-final ../guard/bin/lake --no-cache build +GapChain.PurIo:olean
python3 ../run.py purio-current ../guard/bin/lake --no-cache --no-build build +GapChain.PurIo:olean
```

The first required bare version probe selected the machine default, Lean 4.36.0. Its enclosing command took 0.542 s and did not capture the child’s peak RSS. The separate timed replay is included below. All compiler runs used the pinned binary. Times are wall seconds and peak RSS is in bytes.

| Run | Lean invocation | Free | Wall s | Peak RSS | Exit |
|---|---|---:|---:|---:|---:|
| Initial default | `--version` | — | 0.542 (enclosing) | unrecorded | 0 |
| Default replay | `--version` | — | 0.26 | 50,659,328 | 0 |
| `pinned-version` | `--version` | 68% | 0.396 | 50,298,880 | 0 |
| `preflight` | `--githash` | 68% | 0.071 | 49,889,280 | 0 |
| `records-1` | `--githash` | 68% | 0.071 | 49,823,744 | 0 |
| `records-1` | `PurIo` | 68% | 157.865 | 4,858,281,984 | 1 |
| `records-2` | `--githash` | 64% | 0.071 | 49,774,592 | 0 |
| `records-2` | `PurIo` | 64% | 172.612 | 4,855,529,472 | 0 |
| `offset-1` | `--githash` | 63% | 0.071 | 49,807,360 | 0 |
| `offset-1` | `PurIo` | 63% | 155.367 | 4,861,460,480 | 1 |
| `offset-2` | `--githash` | 64% | 0.071 | 49,823,744 | 0 |
| `offset-2` | `PurIo` | 65% | 176.335 | 4,855,037,952 | 0 |
| `purio-final` | `--githash` | 66% | 0.071 | 49,807,360 | 0 |
| `purio-final` | `PurIo` | 65% | 173.718 | 4,861,526,016 | 0 |
| `purio-current` | `--githash` | 65% | 0.071 | 49,807,360 | 0 |

Lake driver wall times were 15.449 s (`preflight`), 180.195 s (`records-1`), 198.035 s (`records-2`), 181.032 s (`offset-1`), 201.906 s (`offset-2`), 198.942 s (`purio-final`), 16.939 s (`purio-current`). The first build lacked the transfer-operator namespace. The first offset build left a reciprocal identity unsolved. The next offset build passed and reported a redundant tactic, which was removed for the final build. The final no-build check reported `All targets up-to-date (21149 jobs).`

## Next row and decisive outcome

**Transport the full volume-first export across one fixed cutoff offset.** At $K_j=J_j+r$, keep $β_j=\mathrm{betaAt}(L,M,K_j,g_0)$ and pull the passage limits at $J_j$ back under $x\mapsto L^{-r}x$. This requires matching original-mesh infinite-volume states and growing tori on the same subsequence, then transporting the full Schwinger representatives, their growth constants, the canonical decomposition and the component OS and non-Gaussian clauses. With those witnesses the purity-to-gap argument already runs at $K_j$ and side ℓ. [Release state dilation](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/Construction/InfiniteLattice/CopyOfAStateOnADilatedLattice.lean#L24-L52) · [Original witness clauses](GapChain/Stage0.lean#L296-L336)

**Decisive outcome.** Lean proves the top theorem from (PUR-io) alone with every $K_j\in A$, the original rate `gapRate ℓ` and the same three axioms, or the row identifies the first unproved transport clause and the exact input it lacks.
