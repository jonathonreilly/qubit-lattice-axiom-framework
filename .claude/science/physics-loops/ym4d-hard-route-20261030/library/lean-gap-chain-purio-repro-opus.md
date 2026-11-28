lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-29T04:59Z

# Independent Lean reproduction of the (PUR-io) consumer under the footprint cap (FINISH row 1691)

Started 2026-11-28T16:59:46Z (date -u). Worker: Claude Opus 5.5, effort high, Mac mini worker 1.
Pinned commit: 9cd49b2b27b8f085c9b9054ae060f48f51894845 (branch claude/ym4d-hard-route).

Scope: Part A of row 1681 (`library/lean-gap-chain-purio-check-opus.md`) again, with the lead's
new memory rule: kill the build when the physical footprint of the lean/lake process tree goes
above 6 GB, or when system free memory (memory_pressure) goes below 40 percent. Part B of row 1681
is done; it is not repeated here.

Credit: the Lean release is by Sussman-Alpoge (with Claude and Codex). GapChain Purity.lean,
PurIo.lean and Offset.lean are by gpt-6.2-astra max (rows 1676, 1678, 1679). The method reuses
rows 1671 and 1681 (`library/lean-gap-chain-final-check-opus.md`,
`library/lean-gap-chain-purio-check-opus.md`).

## Repo search

FINISH.md names this reproduction only in rows 1681 and 1691. Row 1681 (`library/lean-gap-chain-purio-check-opus.md`) is NOT REPRODUCED under the RSS cap. No other kernel run of Purity, PurIo or Offset by a second provider is on file. This row adds no new mathematical statement, so open-core.md has nothing to match.

## Setup (step 1, 2026-11-28T17:00-17:05Z)

- New scratch root `/tmp/opus-purio-repro.hH2Aoo`, project in `project/`. Copies of the committed `lean/gapchain/GapChain/*.lean` (17 files) and `lean-toolchain` at 9cd49b2b2. Each working-tree file equals its git blob at 9cd49b2b2 (0 mismatches). `logs/committed-sha256.txt` is byte-identical to row 1681's list (same 17 sources). The copies pass `shasum -c` (0 failures).
- My own `lakefile.toml` (path requirement on the release, `lean_lib GapChain`, `globs = ["GapChain.+"]`) and `lake-manifest.json`, both carried from my rows 1671/1681 (not from the author). The manifest's nine git revisions equal the fixture's (script check: all equal). `.lake/packages/<name>` are symlinks to the fixture packages; `YangMillsMinimalFull` links to the fixture root. No olean is copied or reused; `.lake/build` starts empty.
- Sandbox profile `tools/sb.sb` on every lake and lean run: deny writes to `/Volumes/SANDISK SSD` and `~/.elan`; deny reads of `/tmp/sa-lean-gap-chain-*`, of row 1671's `.lake/build` and of row 1681's `.lake`. Tests: a write into the fixture through the symlink, a write into `~/.elan`, a listing of row 1671's build folder and of `/tmp/sa-lean-gap-chain-final-astra62.eczrFO` each gave `Operation not permitted`.
- Toolchain: `~/.elan/bin/lean --version` from the scratch project gives `Lean (version 4.33.1, arm64-apple-darwin24.6.0, commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6, Release)`. (From the repository root it now gives 4.36.0, so every run calls the v4.33.1 toolchain binaries directly, with PATH set to that toolchain.) Lake 5.0.0-src+819816b.
- Watchdog `tools/watch.sh`, started with nohup at 17:01:29Z, heartbeat every 60 s. Every 5 s it takes the process tree under the pid of the current run (written by `tools/run.sh`), sums the `ps` RSS and the `phys_footprint` from `/usr/bin/footprint -p <pid> --noCategories -f bytes` over the tree, and reads the free percentage of `memory_pressure -Q`. It kills the tree when the summed footprint is above 6,000,000,000 B or free memory is below 40 percent. Samples: `logs/watch-samples.log`.
- Runner `tools/run.sh`: `/usr/bin/time -l` around `nice -n 10` and `sandbox-exec`, `LEAN_NUM_THREADS=2`; logs start time and free memory.
- Release preflight: `lake --no-cache build --no-build +Formulation.FixedObservableContinuum:olean +YangMills.Construction.TransferOperators.FactsOfTheOperatorsOfACubicTorus:olean` exit 0, `All targets up-to-date (21134 jobs).` (25.8 s wall, 72 percent free).

## Builds (step 2)

Order: SequenceLemma, LemmaM1, TheoremS, Wilson, Transfer, Trace, Stage0, Stage2, Stage3, Stage3b, Stage4, Final, Purity, PurIo, Offset (Assembly and Periodic are not imported by Offset and are not built). One `lake --no-cache build +GapChain.<M>:olean` per module, 17:02:39Z to 17:31:58Z. Every run exit 0, no kill (`watch.log`: 0 KILL lines; no `KILLED` file), and the watchdog stayed alive the whole time (heartbeat every 60 s, last before the end at 17:31:49Z; 331 samples).

**Result: all 15 modules built from the committed sources.** Each log has exactly one `Built GapChain.<M>` line, for the target. No log has a `Built` line for Mathlib, YangMills, Formulation, Reconstruction, Batteries, Aesop, Qq, Plausible or ProofWidgets (count 0 in every log), so nothing of the release or Mathlib was recompiled. No log has an error. The Offset log shows `Built GapChain.Offset (157s)` and 14 `Replayed GapChain.*` lines (the modules built before).

Measurements. Free % is at the start (memory_pressure). Wall is from `/usr/bin/time -l`. "time RSS" and "time fp" are that tool's maximum resident set size and peak memory footprint. The last three columns are from the watchdog samples over the run: peak of the summed footprint of the tree, peak of the summed RSS of the tree, and minimum free %.

| Module | Free at start | Wall s | time RSS B | time fp B | Tree peak fp B | Tree peak RSS B | Min free |
|---|---:|---:|---:|---:|---:|---:|---:|
| SequenceLemma | 72% | 26.72 | 2,981,232,640 | 192,044,920 | 550,385,992 | 3,341,451,264 | 71 |
| LemmaM1 | 72% | 7.95 | 3,177,037,824 | 199,319,440 | 691,202,712 | 3,854,630,912 | 70 |
| TheoremS | 72% | 5.91 | 3,389,784,064 | 200,023,904 | 904,494,200 | 3,863,592,960 | 69 |
| Wilson | 70% | 6.52 | 3,398,156,288 | 205,217,656 | 598,597,064 | 3,668,115,456 | 68 |
| Transfer | 70% | 5.09 | 3,464,069,120 | 202,973,096 | 730,341,624 | 4,031,823,872 | 68 |
| Trace | 70% | 3.84 | 3,413,524,480 | 207,036,304 | 767,173,048 | 4,078,551,040 | 68 |
| Stage0 | 69% | 167.27 | 6,858,817,536 | 478,273,616 | 1,738,012,256 | 6,953,910,272 | 55 |
| Stage2 | 62% | 186.20 | 6,854,967,296 | 476,504,216 | 1,766,962,976 | 7,144,570,880 | 55 |
| Stage3 | 62% | 279.11 | 6,786,908,160 | 496,590,904 | 4,461,133,568 | 7,332,036,608 | 48 |
| Stage3b | 63% | 180.24 | 6,944,178,176 | 477,126,712 | 1,801,500,568 | 7,217,102,848 | 56 |
| Stage4 | 63% | 189.75 | 6,902,939,648 | 480,239,720 | 2,268,428,352 | 7,187,873,792 | 55 |
| Final | 62% | 170.71 | 6,905,643,008 | 479,486,080 | 1,729,640,416 | 7,298,367,488 | 55 |
| Purity | 62% | 177.67 | 6,908,755,968 | 472,424,504 | 1,727,461,344 | 7,001,456,640 | 55 |
| PurIo | 62% | 168.99 | 6,958,694,400 | 478,994,560 | 1,766,651,944 | 7,382,450,176 | 55 |
| Offset | 62% | 182.99 | 6,911,492,096 | 488,972,464 | 1,788,557,424 | 7,120,814,080 | 55 |

Peaks over all builds: tree footprint 4,461,133,568 B (Stage3, one sample at 17:14:06Z, as the module finished), below the 6,000,000,000 B cap; tree RSS 7,382,450,176 B (PurIo); minimum free 48 percent (the same Stage3 sample), above the 40 percent stop. Every other sample had at least 55 percent free. As in rows 1671 and 1681, the RSS is mostly clean mapped olean pages: RSS above 6.8 GB with a footprint of 1.7-1.8 GB.

Olean SHA-256 of my build (not a byte reproduction of the author's artifacts; oleans embed paths, and none was required): Purity `fbe2e19a1340e06b56db059da0d967046211e41e0b847e44276ee5741bb30fb0`, PurIo `b616e1cd3361c9d8211aabb75265a3e8cfe2fce0644d7f6b1c8191b0eee9ccb6`, Offset `bd357c63806e885ef601b33d24b0202adfc08de2b4b96c5129585e1415d51219`.

## Axiom check (step 3)

In progress: Check.lean (SHA-256 `101c4bb76ba641abde8467b620bbe00c8db2c7d1de4369947555edcbeb8182a5`), importing GapChain.Offset.

Note on the watchdog log. `~/.elan` resolves to `/Volumes/SANDISK SSD/Mac Storage/Developer/elan`, so the `ps` command name of each lean process contains a space and the sample log labels it `SANDISK:<pid>`. The tree walk uses pids, so these processes are in the sum (checked: during SequenceLemma the lean pid 90268 is in every sample, with its RSS and footprint). Build sequence script: `tools/seq.sh` (stops on a kill, on a dead watchdog, or on free memory below 50 percent for 20 min; waits for 50 percent free before each module). Started 17:02:39Z.

Progress 17:06:23Z: SequenceLemma to Stage0 built, rc 0 each, no kill. Through Stage0 the watchdog samples give tree peak footprint 1,738,012,256 B, tree peak RSS 6,953,910,272 B, minimum free 55 percent. (Final table below when all modules are done.)
