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

### Evictor attempts (step 3) and Part A verdict

My own evictor (`tools/evict.py`, run in the same sandbox): for every running `lean`, list the `.olean` files it maps (`lsof -p`, 3,497 files for the probe), map each file read-only and call `msync` on it. No file is written. Results on two more runs of the probe:

| Probe run | Eviction | Killed at (RSS) | `ru_maxrss` (time -l) | Wall |
|---|---|---|---|---|
| 1 (13:36Z) | none | 6,298,624 KB | 6,455,656,448 B | 158.4 s |
| 2 (13:39Z) | `MS_INVALIDATE` every 10 s, 0 errors | 6,334,352 KB | 6,487,801,856 B | 48.5 s |
| 3 (13:41Z) | one pass each of `MS_KILLPAGES`, `MS_DEACTIVATE`, both | 6,314,896 KB | 6,469,632,000 B | 30.7 s |

No flag lowered the RSS of the lean process (run 3: 4,055,440 KB before, 4,245,184 KB after the three passes, rising). `/usr/sbin/purge` gave `Unable to purge disk buffers: Operation not permitted`. I found no other user-space way on macOS to take clean mapped pages away from another process, and I did not create memory pressure on purpose (other workers share the machine). The watchdog ran from 13:35:39Z to 13:42:19Z and made all three kills (`logs/watch.log`). Memory free per `memory_pressure`: 71 percent before the runs, 62 percent at the end.

**Verdict A: NOT REPRODUCED (blocked by the 6 GB cap of the brief).** With the pinned toolchain and the release fixture on this machine, the import of the two release modules that Stage 0 imports reaches 6.3-6.5 GB resident before any local code runs. Every module from Stage 0 to Offset imports this closure, and Check.lean imports all of it, so each of them would exceed 6 GB. As the brief directs, I stopped and did not continue with a larger cap. No local module was compiled, no `#print axioms` was run, and the kernel claim of rows 1676, 1678 and 1679 has no independent reproduction from this row. The author's own builds report 4.86 GB with their pager; I did not read or use that pager, so I cannot say how it gets the RSS down.

What I did check without a build:
- SHA-256 of the three new sources equals the receipts: Purity `07895d22b4d9703f04e90f5bb6157a5b7e98cd4b5391f50e185fe1d5a93ed6b2`, PurIo `956de7cf4da125b22485c69e31323a3c9e9c7424840eb00510286d1c1076e14b`, Offset `e119ac9879dd73a387db9818fc9442d4fe62b869dc2f02f7b0f7ba929f7df6a0`. The other 14 modules are byte-equal to what row 1671 built and checked.
- Source scan of Purity.lean, PurIo.lean, Offset.lean (grep): no `sorry`, `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, `axiom` declaration, `skipKernelTC` or other `debug.` option, `ofReduceBool`, `elab`, `macro` or `syntax` command. Options: only `autoImplicit false` and `Elab.async false`; no `maxHeartbeats` change. So no local command can change what `#print axioms` prints, but this is not a kernel check.

**For the lead (proposal, not done):** the physical footprint of the import was 0.95 GB against 6.3 GB RSS. A cap on physical footprint (for example 6 GB), or an RSS cap of 8 GB with the 50 percent free rule, would let a fresh build run on this machine; row 1671 ran at 7.2-7.6 GB RSS with at least 56 percent free. The reproduction needs one of those rulings, or a different machine. Expected cost from row 1671: about 25 min for the 12 old modules plus about 10 min for Purity, PurIo and Offset, and 4 min for Check.lean.

Files: `/tmp/opus-purio-check.Qk6YOv/logs/` (`watch.log`, `watch-rss.log`, `watch-fp.log`, `evict.log`, `time-probe*.txt`, `preflight.log`, `committed-sha256.txt`).

## Part B. Faithfulness (reading)

(The Lean statements below are read from the committed sources. Part A gives no kernel confirmation of them.)

### Item 1. `purity` and `passingCutoffs` against the lane's P_K. HOLDS.

Lean (Purity.lean L25-L28, PurIo.lean L25-L27):

```lean
def purity (Γ : CubicPeriodSublattice) (β : ℝ) (u : ℕ) : ℝ :=
  let T := Γ.transfer μt β
  let P₀ := neutralProj Γ μt
  (tracePW (P₀ * T ^ (2 * u)) / tracePW (P₀ * T ^ u) ^ 2).re
def passingCutoffs (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) : Set ℕ :=
  {k | ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ k →
    457 / 625 ≤ purity Γ (betaAt L M k g₀) (Γ.side / 512)}
```

Lane (row 1468 §3.1; `gap-agy-seed-approaches-neon.md` L12): n = ℓ b^K, u = n/512, T the Wilson transfer at β_K on the spatial torus of side n, P_0 = (1/8) Σ_z C_z on the centre-neutral gauge-invariant states, Z_+(v) = Tr(P_0 T^v), P_K = Z_+(2u)/Z_+(u)^2, and (PUR-io) = P_K ≥ 457/625 at infinitely many K for one ℓ ∈ 1024 N_{>0}.

Match, piece by piece:
- T: the release transfer of the cube along `TimeAxis.timeIdx` (the same axis as Stage 0's `NeutralTailLE`). β: `betaAt L M k g₀ = (renormalizedBareCoupling L M k g₀ ^ 2)⁻¹` (Stage0.lean L151), the calibrated least root, the lane's β_K.
- P_0: `neutralProj` (Stage0.lean L71-L72) = (1/8) Σ over the 8 subsets of the three spatial axes of `centreTranslation`, which is the lane's (1/8) Σ_z C_z. It is the centre average on all of L^2, not only on gauge-invariant vectors. The release T carries the gauge projection P_G on both sides, so P_0 T^v = P_0 P_G T^v for v ≥ 1 (design row 1457 §2.1; Stage 0 check §1.1). So the traces are the lane's gauge-invariant traces.
- Square-root placement: the release T is K^(1/2) e^(-V) K^(1/2), the lane's is e^(-V/2) K e^(-V/2) (design §2.1 item 5; row 1680 makes the same point). The centre translations commute with K and with e^(-V) (−1 is central; a spatial plaquette has 0 or 2 flipped links). With A, B commuting with P_0, Tr(P_0 (AB)^v) = Tr(P_0 (BA)^v) by cyclicity. So P_K has the same value in both conventions. P_K is also unchanged under T → cT for a scalar c > 0, so normalisations of the transfer do not matter.
- Trace: `tracePW` is the release's sum of diagonal Peter-Weyl entries. `purity_eq_traceRatio` (β > 0, u ≥ 2) proves that the complex ratio is real, so `.re` loses nothing. `purity_eq_sectorMoments` proves purity = m(2u)/m(u)^2 with m the zero-flux (neutral, untwisted) sector moment of Stage 4, that is (1 + Σ r_i^(2u))/(1 + Σ r_i^u)^2 in the notation of Fact PUR.
- u: `Γ.side / 512` is natural division; for 1024 ∣ ℓ it is exact, u = ℓL^k/512. The PurIo and Offset theorems require 0 < ℓ and 1024 ∣ ℓ, so u is the lane's u.
- "Every cube of side ℓL^k": `CubicPeriodSublattice` (release, `CubicToriAndProductsOfOperatorsOnPowersOfG.lean` L8-L12) has data `side` and `lattice`, and `lattice` is a `PeriodSublattice 1` whose only data field is `periods`, fixed by `periods_eq` to the cubic sublattice of that side. So all Γ of one side are equal (proof irrelevance), and the quantifier is over one cube. This is the lane's single torus (Z/n)^3.

Not vacuous, in both senses:
- The condition is not trivially true. A Γ of side n exists for n ≥ 3: the release builds a `PeriodSublattice` with cubic periods (`PeriodicGibbsStatesAtASpacingProof.lean` L29, `cubicPeriodSublattice ha s hs`, and the a = 1 version used in `CubicToriAmongTheToriOfAnyShapeProof.lean` L42-L88). I read this; I did not check in Lean that its periods are literally `cubicSublattice 1 n`. So membership of k is a real inequality on one number, and A ⊆ passingCutoffs is not empty for a type reason.
- The condition can hold in principle. The proof of `neutralTailLE_of_purity` gives 0 < purity ≤ 1/D ≤ 1 with D = Σ x_i ≥ 1, and purity → 1 when the excited neutral ratios to the power u go to 0. So 457/625 < 1 is not excluded by the definition. Whether it holds at β = β_K with u = n/512 is (PUR-io) and is open.

Remark (not a defect). The Lean consumer uses only 2/3 ≤ purity (Purity.lean L75, L124: `2/3 ≤ 457/625` by `norm_num`). From 2/3 it gets D − 1 ≤ 1/2, which is the bound Stage 0's `NeutralPhysicalSeed` asks for. So, if the Lean proof is right, the threshold of (PUR-io) can be lowered from 457/625 to 2/3 without change to the rest of the chain. The lane's Fact PUR uses 457/625 to reach s ≤ 4/21; the Lean route does not need 4/21 because Stage 4 starts from the tail bound 1/2. RECEIPT-purity.md states this inequality ("2/3 ≤ P ≤ 1/D implies D − 1 ≤ 1/2") but no receipt says that the threshold may be lowered. Grep of FINISH.md and `library/open-core.md` for "2/3" next to "purity" or "PUR": see the search note at the end of Part B.
