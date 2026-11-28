# Repo search

The lead’s November 8 digest covers main and PRs 10114, 10133, 10134 and 10141. I opened its closest operator hit on PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149. It proves a one-step plaquette correlation using a rank-one lower bound. The Stage 1 W1 controls a whole operator’s Hilbert–Schmidt mass from a rank-one approximation. The digest’s W1/W2/W5 witness labels concern a different task. I checked Lean filenames and declaration terms on all five refs. I found the hand arguments and the design, with no Stage 1 implementation hit. The target-specific prior file is absent at the pin. The open registry has no competing row, and row 1458 assigns these three pieces to 1459. [Lead search](../../library/prior/repo-search-2026-11-08.md) · [Design](../../library/lean-gap-chain-design-fable.md)

# Stage 1 Lean build receipt

FINISH row 1459, pinned repository revision `76676c64d`. This is a research build record.

## Plan

1. Check the Lean toolchain, prior work, owner rules, Sussman–Alpoge indexes and hand proofs. Identify the exact statements and their authors.
2. Build U4 and the forward implication W1 in a scratch Lake project with the pinned Mathlib.
3. Formalize the lane’s W5 from the weight hypotheses, recording the named lemmas and the constant in the conclusion.
4. Copy the verified sources here. Record the wall time, peak memory, kernel axiom output, remaining work and the next two rows.

## Sources

Claude Opus 5.5 wrote row 668 Lemma A2. Claude Fable 5.2 wrote row 1356 Lemma M1 and row 697 Theorem S. Row 1355 already optimized the rank-one projection and scale. Row 1359 checked M1, and rows 698–699 checked the Theorem S hand argument. Codex GPT-6 Astra supplied E′ and the all-integer S3′ correction in row 699. This build uses that correction. [U4 hand proof](../../library/gap-os-equiv.md) · [Row 1355](../../library/gap-mini-neutral-step-check-astra.md) · [M1 hand proof](../../library/gap-mini-mneutral-fable.md) · [Theorem S, §3.4](../../library/gap-crux-restate.md) · [Correction, point 8](../../library/gap-seed-check-astra.md)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the surrounding construction. I searched the outline’s chunk and obligation indexes and the CA indexes. Outline UI2–UI3 at 28272–28288 give the related reflection-moment inequalities. GCB43 at 27963–27971 uses a Hilbert–Schmidt norm for a Gaussian covariance. Outline 588–599 and 31871–31882 explain why polynomial decay permits arbitrarily small positive energies. CA-I 3216–3222 explicitly leaves the mass gap open. [Pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L28272-L28288) · [Pinned complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3216-L3222)

## Build record

- The receipt was created on 2026-11-24 at 20:40:32 UTC. The starting head was `76676c64d366` (detached at launch). GOAL, the requested FINISH rules, and the pinned source ranges were read before writing the proofs. The two source downloads have 32,992 and 166,711 lines respectively.
- The untimed initial shell version probe returned 4.36.0. The explicit 4.33.1 selection succeeds, and the project toolchain file selects it for every proof. The cached Mathlib HEAD is `0df444a360eaa60ab8c11dca51a86af692955474`.
- Scratch project and raw logs are in `/tmp/sa-lean-gap-chain-stage1-astra62.vjqaqw/`. A scratch-only manifest and a symlink resolve the pinned dependencies. The runner sets `LEAN_NUM_THREADS=2`, uses `nice -n 10`, and denies file writes to the replay packages. The distributable Lake project uses the git revision.
- U4 compiled. The geometric envelope may hold along an unbounded subsequence. The forward-zero case follows directly from the three-term inequality at the zero index. The all-index specialization is exported too.
- W1 compiled on an arbitrary complex Hilbert basis. It uses the design’s test on all finite orthonormal families, sums the rank-one and mixed terms by Parseval, and identifies the mass with the diagonal trace of B² by symmetry. This proves the direction for every positive scale without choosing an eigenvector. Two linter warnings were removed before the final build.
- The two-period K, X, E and E′ derivations elaborated. The proof obtains the normalized trace comparison at every integer period from the doubling inequality and discrete convexity. The bulk infimum belongs to each fixed pair of spectator periods. The spectral layer obtains the thermal squaring estimate by summing one term per eigenvalue multiplicity. At this point the three-axis cube argument was still pending.
- W5 compiled through the thermal recursion, all-integer Corollary S3′, Theorem D(b)’s pressure comparison and the exact pressure threshold 19/100000. The spectral gap is the extended-real infimum of the excitation energies for positive relative eigenvalues. A zero thermal seed forces an infinite gap on the stated boxes. The pressure alternative and the seed itself are conditional. Every W5 theorem, including private helpers, reported the expected three axioms.

## Checked statements

| Piece | Kernel-checked conclusion |
| --- | --- |
| U4 | For `q ≥ 0` and nonnegative log-convex `m`, an envelope `m j ≤ C q^j` at arbitrarily large indices gives `m (n+1) ≤ q m n` for every index. The all-index version is also exported. |
| W1 | For a positive Hilbert–Schmidt operator and any unit vector meeting the finite-family test at positive scale, `(1 − δ²) Tr(B²) ≤ ‖B‖²`. The proof sums the rank-one contribution and the mixed term on a Hilbert basis. |
| W5 | K, X, E and E′ give the three spatial enlargements. The counted excited spectrum supplies the time square, giving `s(2n) ≤ ((1+s(n))^64−1)^2`. The exact estimate `64 (641/640)^63 ≤ 71` yields `5041 = 71²`. |
| Theorem S and S3′ | At `N ≥ 3` put `s = S(N; (2N)³)`. A positive seed `s < 1/5041` gives `m(L³) ≥ log(1/(5041s))/N` at every integer `L ≥ 2N`. The dyadic thermal bound and the interpolated `(5041s)^(2^k)/71` estimate are both exported. A zero seed forces every excited eigenvalue on these boxes to vanish. |
| Pressure alternative | `log(1+s) ≤ Φ(N)`, so `Φ(N) ≤ 19/100000` implies the strict thermal seed. |

`PairWeight` takes positivity, exchange of periods, submultiplicativity, log-convexity and a finite lower bound on the log density. `TorusData` supplies the spectrum of each rectangular slice, the axis-exchange identities, log-convexity and the spectator-dependent lower bound. `BoxSpectrum.thermal_add` proves the excited-trace product inequality from summability with multiplicities. Instantiating these hypotheses on the Wilson trajectory and proving the physical seed remain open.

## Verification and trusted base

The three library roots built using Lean 4.33.1 (commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) and the pinned Mathlib cache. The final `lake --wfail build` compiled all three modules. The standard, installed `lake --no-build build` then reported all default targets up to date. A scratch consumer imported the three modules together, specialized W1 to coefficient `21/25` at tolerance `2/5`, and applied S3′ at `N=3, L=13` for positive and zero seeds.

The trusted base is the pinned Lean kernel and its environment of precompiled Mathlib and transitive dependencies. The kernel checks the proof terms for these modules, including their exact rational arithmetic. Every local theorem has the three dependencies printed below. The source scan found zero uses of `sorry`, `admit`, `axiom` declarations, `native_decide` or `implemented_by`. This build uses research hypotheses and confers no scientific status.

From this directory, with the pinned dependencies available, the default build command is

```sh
LEAN_NUM_THREADS=2 /usr/bin/nice -n 10 lake build
```

## Resource record

All times are UTC on 2026-11-24. Darwin `/usr/bin/time -l` supplied wall seconds and maximum resident set size in bytes. Failed elaborations are included. The first two version-only probes were unmetered. Their measured replays appear below. Raw stdout, resource counters and the run index are in `/tmp/sa-lean-gap-chain-stage1-astra62.vjqaqw/logs/`.

| UTC start | Invocation | Exit | Wall s | Max RSS, bytes |
| --- | --- | ---: | ---: | ---: |
| 20:42:58 | Pinned version replay | 0 | 0.02 | 50,298,880 |
| 20:43:38 | U4 | 0 | 26.49 | 2,297,380,864 |
| 20:45:25 | W1, failed on rank-one namespace and coercions | 1 | 35.14 | 2,290,319,360 |
| 20:46:57 | W1 | 0 | 21.64 | 2,722,332,672 |
| 20:48:15 | K, failed on index and infimum elaboration | 1 | 37.29 | 1,888,731,136 |
| 20:48:28 | W1, warning cleanup | 0 | 33.20 | 2,361,475,072 |
| 20:49:11 | K, remaining cast and unfolding errors | 1 | 27.39 | 2,436,988,928 |
| 20:50:18 | K–E′ and spectrum, one positivity goal | 1 | 24.84 | 2,381,479,936 |
| 20:51:34 | K–E′ and spectral layer | 0 | 17.53 | 2,484,944,896 |
| 20:53:51 | Cube layer, missing box type annotation | 1 | 69.89 | 2,071,052,288 |
| 20:55:13 | Cube and pressure lemmas, proof-script corrections | 1 | 14.67 | 2,471,739,392 |
| 20:55:51 | Complete W5 and axiom prints | 0 | 38.62 | 2,190,327,808 |
| 20:58:10 | Initial default Lake build | 0 | 83.48 | 2,189,852,672 |
| 20:58:58 | Default version replay | 0 | 0.93 | 48,562,176 |
| 21:00:31 | Lake build after source cleanup | 0 | 37.39 | 2,371,371,008 |
| 21:01:41 | Standard Lake up-to-date check | 0 | 7.17 | 713,113,600 |
| 21:02:22 | Consumer import and specializations | 0 | 33.34 | 2,485,157,888 |
| 21:02:57 | Final build, warnings are errors | 0 | 65.05 | 2,464,251,904 |
| 21:05:48 | Final standard Lake up-to-date check | 0 | 8.06 | 749,387,776 |

The following counters cover each compiler process launched by Lake. A byte-identical copy of the pinned Lake executable selected a scratch `bin/lean` timing wrapper, which forwarded its arguments to the installed 4.33.1 compiler. The Lake rows above give whole-command wall time and Darwin’s maximum RSS counter. Simultaneous process peaks are not summed.

| UTC start | Module | Raw counter | Wall s | Max RSS, bytes |
| --- | --- | --- | ---: | ---: |
| 20:58:17 | SequenceLemma.lean | `lake-lean.1db6Rf` | 37.05 | 2,012,086,272 |
| 20:58:18 | TheoremS.lean | `lake-lean.j6Xtol` | 37.39 | 2,189,852,672 |
| 20:58:55 | LemmaM1.lean | `lake-lean.s9aQM7` | 39.09 | 2,121,760,768 |
| 21:00:38 | TheoremS.lean | `lake-lean.dqANGU` | 30.20 | 2,226,520,064 |
| 21:00:38 | LemmaM1.lean | `lake-lean.cDtTUW` | 30.07 | 2,371,371,008 |
| 21:03:04 | SequenceLemma.lean | `lake-lean.q8exm8` | 25.94 | 2,175,500,288 |
| 21:03:05 | TheoremS.lean | `lake-lean.VNFBX7` | 25.98 | 2,187,722,752 |
| 21:03:30 | LemmaM1.lean | `lake-lean.agKcH6` | 31.65 | 2,464,251,904 |

## Axiom output

These are the verbatim `#print axioms` messages from the final build, in source order within each module. Each message was compared byte for byte with standalone Lean output. Lake’s file and line prefix is omitted. There are 2 theorems in U4, 3 in W1 and 44 in W5.

### SequenceLemma

```text
'GapChain.sequenceLemma' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.sequenceLemma_of_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
```

### LemmaM1

```text
'GapChain.HSNormLE.sum_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.lemmaM1_hsSq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.lemmaM1' depends on axioms: [propext, Classical.choice, Quot.sound]
```

### TheoremS

```text
'_private.GapChain.TheoremS.0.GapChain.PairWeight.secant_lower' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'_private.GapChain.TheoremS.0.GapChain.PairWeight.convex_first' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'GapChain.PairWeight.normalized_antitone' depends on axioms: [propext, Classical.choice, Quot.sound]
'_private.GapChain.TheoremS.0.GapChain.PairWeight.bounded_slopes' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'GapChain.PairWeight.ground_limit' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.ground_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'_private.GapChain.TheoremS.0.GapChain.PairWeight.ground_lower' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'_private.GapChain.TheoremS.0.GapChain.PairWeight.bulk_bounded' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'GapChain.PairWeight.bulk_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.deficit_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'_private.GapChain.TheoremS.0.GapChain.PairWeight.F_swap' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.ground_normalized_antitone' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.ground_multiple' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.ground_convex' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.deficit_convex' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.lemmaK' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.g_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.crossing' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.lemmaX' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.interpolate_log' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.lemmaE'' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.PairWeight.lemmaE' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.summable' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.thermal_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.member_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.thermal_antitone' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.thermal_add' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.weight_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.weight_add' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.log_weight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.log_weight_limit' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.BoxSpectrum.gap_of_pow_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.pair_thermal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.enlarge_side' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.cube_enlarge' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.theoremS_step' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.seed_polynomial' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.dyadic_thermal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.intermediate_thermal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.corollaryS3'' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.theoremS' depends on axioms: [propext, Classical.choice, Quot.sound]
'_private.GapChain.TheoremS.0.GapChain.TorusData.log_space_double' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'GapChain.TorusData.log_seed_le_phi' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.TorusData.seed_of_phi' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Source identification

| File | SHA-256 |
| --- | --- |
| `sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| `GapChain/SequenceLemma.lean` | `214444f13b68d9b4b8390d843af32ab3f1ece94a610d90b988ba41d59ff16b92` |
| `GapChain/LemmaM1.lean` | `98b041f1e2d7a59252af528b280fe5c40334c7fe363c2f9ba4f1a26972d93e68` |
| `GapChain/TheoremS.lean` | `bcd3e031c8550f5b493c5837cd34f9841098835db41adf30cb69b29d2616f35c` |
| `lakefile.toml` | `73084193ab0225b81e20545e12dba40c1e302e9b71671cc76f4fda9a3f00b03c` |
| `lean-toolchain` | `3aac669c7a910ec2389f4e4f921b605adf6ebf2d1e0c9b9cd0be4d33f3f5db71` |

## Next two rows

1. **Corrected Stage 0 statement file.** After row 1455 makes the replayed release available, apply row 1458’s corrections to the blocking factor, time axis, test domain and shared witnesses. Write out `latticeU`, specialize the seed to the calibrated trajectory, and import these three Stage 1 modules. Success means every definition elaborates and the only theorem placeholders belong to the designated Stage 0 implications. On failure, record the first declaration and its unmet type or witness requirement.
2. **Stage 2 upper half.** On those same witnesses, build the public reconstruction argument, identify the odd-grid moments, pass the frequent-cutoff bound to the limit and prove the estimate on the completed space. Success means `massGap_of_expClusters` and the positive-rate unique-vacuum corollary kernel-check with only `propext`, `Classical.choice` and `Quot.sound`. An unsuccessful build identifies the first missing implication or false equality. The physical seed remains a separate obligation.
