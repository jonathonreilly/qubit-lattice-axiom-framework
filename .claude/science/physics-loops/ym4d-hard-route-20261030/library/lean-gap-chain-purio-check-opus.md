lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-29T01:33Z

# Check of the (PUR-io) consumer of the Lean gap chain (FINISH row 1681)

Started 2026-11-28T13:33:13Z (date -u). Worker: Claude Opus 5.5, high, Mac mini worker 1.
Branch claude/ym4d-hard-route at 44550e2f4. Method of row 1671 (library/lean-gap-chain-final-check-opus.md).
Memory free at start: 71 percent (memory_pressure).

Status: in progress. Sections are appended as each step ends.

## Repo search

FINISH.md names `Offset.lean`, `PurIo.lean` or `Purity.lean` only in rows 1676-1685 (the author rows 1676, 1678, 1679, this row 1681 and the queue rows after it). No earlier check of these three modules is on file; `library/open-core.md` has no match for `passingCutoffs`, `PurityAlong` or `su2_fixed_observable_gap_of_infinite_passing`. The author's searches (main, PRs 10114, 10133, 10134, 10141, 10144) are in the three receipts and are not repeated.

## Part A. Reproduction

### Setup (step 1, 2026-11-28T13:33Z-13:39Z)

- Scratch root `/tmp/opus-purio-check.Qk6YOv` (new, made by `mktemp`). Project in `project/`: copies of the committed `lean/gapchain/GapChain/*.lean` and `lean-toolchain` at 44550e2f4; copies verified against `logs/committed-sha256.txt` (0 mismatches). The 14 modules built in row 1671 have the same SHA-256 as there; the three new ones are Purity `07895d22...`, PurIo `956de7cf...`, Offset `e119ac98...`, equal to the values in the three receipts.
- Lakefile and manifest: my own files from row 1671 (one path requirement on the release fixture, `globs = ["GapChain.+"]`; manifest = the fixture's nine git entries plus the path entry). Package directories are symlinks to the fixture. No olean is reused: the project has no `.lake/build` at start, and my row 1671 build folder is read-denied.
- Sandbox profile (`tools/sb.sb`), used for every lake and lean run: deny file-write under `/Volumes/SANDISK SSD` and `~/.elan`; deny file-read of `/tmp/sa-lean-gap-chain-*` (the author's scratch) and of my row 1671 `.lake/build`. Tests: `touch` in the fixture gave `Operation not permitted`; `ls` of the old build folder gave `Operation not permitted`.
- Release preflight: `lake --no-cache build --no-build +Formulation.FixedObservableContinuum:olean +YangMills.Construction.TransferOperators.FactsOfTheOperatorsOfACubicTorus:olean`: exit 0, `All targets up-to-date (21134 jobs).`, 16.2 s.
- Watchdog (`tools/watch.sh`), started 13:35:39Z with nohup, before any Lean run. Every second it reads `ps` RSS of every `lean` process and kills one above 6 GiB (6,291,456 KB); every 5 s it logs the physical footprint (`top` MEM). It stops only when I create `tools/STOP`; it writes a heartbeat line about every minute (`logs/watch.log`).

### Memory probe (step 2): the import alone exceeds the cap

`check/Probe.lean` = the two release imports of Stage 0 and `#eval 1`, run by `lake env lean` (nice 10, `LEAN_NUM_THREADS=2`, sandbox). Result: the watchdog killed the lean process at 13:38:53Z with **RSS 6,298,624 KB (6.45 GB)**, while its **physical footprint was 949 MB** (`logs/watch-fp.log`). The RSS grew slowly over three minutes while the import faulted in olean pages. So almost all of the resident set is clean, file-backed pages of the memory-mapped release and Mathlib oleans, not heap. Every build from Stage 0 on imports at least this closure. Under the 6 GB RSS cap of the brief, no such build can run unless the mapped pages are evicted while it runs. This explains the 7.2-7.6 GB of row 1671 and the author's 4.86 GB (the author ran a pager).

Next: test an evictor of my own (no code from the author's scratch).
