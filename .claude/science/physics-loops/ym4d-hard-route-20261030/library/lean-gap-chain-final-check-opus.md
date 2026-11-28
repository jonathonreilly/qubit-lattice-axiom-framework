lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-28T20:23Z

# Check of the final Lean assembly of the gap chain (row 1671)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 1, branch claude/ym4d-hard-route at 6761f287f. Started 2026-11-28T08:23:11Z (date -u). Not an audit. Item: FINISH row 1671, check of row 1670 (lean/gapchain/GapChain/Final.lean, lean/gapchain/RECEIPT-final.md, by gpt-6.2-astra max).

## Plan

- Part A: fresh scratch Lake project under /tmp, copy of the committed lean/gapchain sources, packages linked to the built release fixture (read only), build GapChain.Final, run Check.lean with #print axioms (Final top theorem, Final massGap, release continuum limit, Stage 0 top theorem as sorryAx control). SHA-256 of every built source, wall time and peak memory of each build.
- Part B: faithfulness items 1-4 (example lines, inline seed step, witness order, receipt wording).

## Repo search

This row checks a Lean module, so the search is for earlier checks of it. FINISH.md names `Final.lean` only in rows 1670 and 1671. In `library/`, the name `su2_fixed_observable_gap_of_mNeutral` occurs only in the design (row 1457) and the Stage 0 and Stage 2 checks; none of them checks `Final.lean`. `library/open-core.md` has no match. So there is no earlier check of row 1670. The RECEIPT-final.md search section (main and PRs 10114, 10133, 10134, 10141) is the author's and is not repeated.

## Part A. Reproduction (in progress)

Setup (my own, not copied from the author's scratch folders; no olean or log of /tmp/sa-lean-gap-chain-* was read or used):

- Scratch root `/tmp/opus-final-check.Hc6JBw`, project in `project/`. I copied the committed `lean/gapchain/GapChain/*.lean` and `lean-toolchain` at 6761f287f. SHA-256 list: `logs/committed-sha256.txt`; the copies match it.
- The committed `lakefile.toml` requires only Mathlib and cannot resolve the `YangMills` and `Formulation` imports of Stage 0. So I wrote my own scratch `lakefile.toml`: one path requirement on the release (`.lake/packages/YangMillsMinimalFull`, a symlink to the fixture root) and one `lean_lib GapChain` with root `GapChain.Final`. The scratch `lake-manifest.json` copies the fixture's nine git entries (same revs) and adds the path entry. `.lake/packages/<name>` are symlinks to the fixture packages. No release artifact was copied.
- Write guard: every lake run is under `sandbox-exec` with `(deny file-write* (subpath "/Volumes/SANDISK SSD"))` and the same for `~/.elan`. Test of the profile: a write through a symlink to a denied path gave `Operation not permitted`.
- Toolchain: `~/.elan/bin/lean --version` gave `Lean (version 4.33.1, arm64-apple-darwin24.6.0, commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6, Release)` (run from the repository, whose path resolves the pinned toolchain). All lake runs call the v4.33.1 toolchain binaries directly, with PATH set to that toolchain.
- Release preflight: `lake --no-cache build --no-build +Formulation.FixedObservableContinuum:olean +YangMills.Construction.TransferOperators.FactsOfTheOperatorsOfACubicTorus:olean` exit 0, `All targets up-to-date (21134 jobs).` (9.5 s wall). So Lake does not recompile any release or Mathlib module for the two release imports of Stage 0.
- Build: one `lake --no-cache build +GapChain.<M>:olean` per local module, in dependency order SequenceLemma, LemmaM1, TheoremS, Wilson, Transfer, Trace, Stage0, Stage2, Stage3, Stage3b, Stage4, Final; each starts only at 50 percent free or more (memory_pressure -Q); `LEAN_NUM_THREADS=2`, `/usr/bin/nice -n 10`; wall and peak RSS from `/usr/bin/time -l` (maximum over the lake process and its waited children); a watchdog kills any lean process above 6 GB. Started 2026-11-28 about 08:33Z.
