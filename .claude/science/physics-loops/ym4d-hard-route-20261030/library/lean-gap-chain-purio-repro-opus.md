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

In progress. Order: SequenceLemma, LemmaM1, TheoremS, Wilson, Transfer, Trace, Stage0, Stage2, Stage3, Stage3b, Stage4, Final, Purity, PurIo, Offset (Assembly and Periodic are not imported by Offset and are not built).

Note on the watchdog log. `~/.elan` resolves to `/Volumes/SANDISK SSD/Mac Storage/Developer/elan`, so the `ps` command name of each lean process contains a space and the sample log labels it `SANDISK:<pid>`. The tree walk uses pids, so these processes are in the sum (checked: during SequenceLemma the lean pid 90268 is in every sample, with its RSS and footprint). Build sequence script: `tools/seq.sh` (stops on a kill, on a dead watchdog, or on free memory below 50 percent for 20 min; waits for 50 percent free before each module). Started 17:02:39Z.

Progress 17:06:23Z: SequenceLemma to Stage0 built, rc 0 each, no kill. Through Stage0 the watchdog samples give tree peak footprint 1,738,012,256 B, tree peak RSS 6,953,910,272 B, minimum free 55 percent. (Final table below when all modules are done.)
