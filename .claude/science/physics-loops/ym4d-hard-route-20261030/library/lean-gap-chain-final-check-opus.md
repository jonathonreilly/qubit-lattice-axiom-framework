lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-28T20:23Z

# Check of the final Lean assembly of the gap chain (row 1671)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 1, branch claude/ym4d-hard-route at 6761f287f. Started 2026-11-28T08:23:11Z (date -u). Not an audit. Item: FINISH row 1671, check of row 1670 (lean/gapchain/GapChain/Final.lean, lean/gapchain/RECEIPT-final.md, by gpt-6.2-astra max).

## Plan

- Part A: fresh scratch Lake project under /tmp, copy of the committed lean/gapchain sources, packages linked to the built release fixture (read only), build GapChain.Final, run Check.lean with #print axioms (Final top theorem, Final massGap, release continuum limit, Stage 0 top theorem as sorryAx control). SHA-256 of every built source, wall time and peak memory of each build.
- Part B: faithfulness items 1-4 (example lines, inline seed step, witness order, receipt wording).

## Repo search

This row checks a Lean module, so the search is for earlier checks of it. FINISH.md names `Final.lean` only in rows 1670 and 1671. In `library/`, the name `su2_fixed_observable_gap_of_mNeutral` occurs only in the design (row 1457) and the Stage 0 and Stage 2 checks; none of them checks `Final.lean`. `library/open-core.md` has no match. So there is no earlier check of row 1670. The RECEIPT-final.md search section (main and PRs 10114, 10133, 10134, 10141) is the author's and is not repeated.

## Part A. Reproduction

Setup (my own, not copied from the author's scratch folders; no olean or log of /tmp/sa-lean-gap-chain-* was read or used):

- Scratch root `/tmp/opus-final-check.Hc6JBw`, project in `project/`. I copied the committed `lean/gapchain/GapChain/*.lean` and `lean-toolchain` at 6761f287f. SHA-256 list: `logs/committed-sha256.txt`; the copies match it.
- The committed `lakefile.toml` requires only Mathlib and cannot resolve the `YangMills` and `Formulation` imports of Stage 0. So I wrote my own scratch `lakefile.toml`: one path requirement on the release (`.lake/packages/YangMillsMinimalFull`, a symlink to the fixture root) and one `lean_lib GapChain` with root `GapChain.Final`. The scratch `lake-manifest.json` copies the fixture's nine git entries (same revs) and adds the path entry. `.lake/packages/<name>` are symlinks to the fixture packages. No release artifact was copied.
- Write guard: every lake run is under `sandbox-exec` with `(deny file-write* (subpath "/Volumes/SANDISK SSD"))` and the same for `~/.elan`. Test of the profile: a write through a symlink to a denied path gave `Operation not permitted`.
- Toolchain: `~/.elan/bin/lean --version` gave `Lean (version 4.33.1, arm64-apple-darwin24.6.0, commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6, Release)` (run from the repository, whose path resolves the pinned toolchain). All lake runs call the v4.33.1 toolchain binaries directly, with PATH set to that toolchain.
- Release preflight: `lake --no-cache build --no-build +Formulation.FixedObservableContinuum:olean +YangMills.Construction.TransferOperators.FactsOfTheOperatorsOfACubicTorus:olean` exit 0, `All targets up-to-date (21134 jobs).` (9.5 s wall). So Lake does not recompile any release or Mathlib module for the two release imports of Stage 0.
- Build: one `lake --no-cache build +GapChain.<M>:olean` per local module, in dependency order SequenceLemma, LemmaM1, TheoremS, Wilson, Transfer, Trace, Stage0, Stage2, Stage3, Stage3b, Stage4, Final; each starts only at 50 percent free or more (memory_pressure -Q); `LEAN_NUM_THREADS=2`, `/usr/bin/nice -n 10`; wall and peak RSS from `/usr/bin/time -l` (maximum over the lake process and its waited children); a watchdog kills any lean process above 6 GB. Started 2026-11-28 about 08:33Z.

Source scan (all 14 committed modules in `lean/gapchain/GapChain/`, by grep): `sorry` occurs only in Stage0.lean (4, the four designated placeholders at `neutralTail_of_rankOneAtTime`, `kappaSeed_of_neutralPhysicalSeed`, `massGap_of_expClusters`, `expClusters_of_kappaSeed`). No module has `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `opaque`, an `axiom` declaration, `skipKernelTC` or another `debug.` option, `ofReduceBool`, or a local `elab`/`macro`/`syntax` command (so no local command can change what `#print axioms` prints). The only options are `autoImplicit false`, `Elab.async false`, `linter.unusedVariables false` and `maxHeartbeats` raises; none of them weakens the kernel check.

Check.lean (in `/tmp/opus-final-check.Hc6JBw/check/`, imports `GapChain.Final`): the four requested `#print axioms` lines, seven extra ones (the other two Final theorems, Stage 0's `neutralPhysicalSeed_of_mNeutral`, the four proved stage constants), and two meta checks of my own: (i) a traversal of all constants reachable from a root's type and value that lists the axioms it reaches (written independently of `Lean.collectAxioms`), and (ii) an exact `Expr ==` comparison of the type and universe parameters of each Final theorem and each stage constant against the Stage 0 constant of the same name. Check (ii) is stronger than the `example : type_of% ... := ...` lines in Final.lean, which only show definitional equality.

### Part A results

Date of results: 2026-11-28T08:51Z (date -u, this step). Full logs: `/tmp/opus-final-check.Hc6JBw/logs/` (`build-<M>.log`, `time-<M>.txt`, `build-summary.txt`, `uptodate.log`, `check-output.txt`, `time-check.txt`).

**Verdict A: REPRODUCED.** From the committed sources, in my own scratch project, Lake compiled each of the twelve local modules once (each build log shows `Built GapChain.<M>` for the target and only `Replayed` for local modules built before). No Mathlib or release module was built in any of the twelve runs (count of `Built Mathlib|YangMills|Formulation|Reconstruction|Batteries|Aesop|Qq|Plausible|ProofWidgets` lines: 0 in every log), and the fixture was write-denied throughout. `lake build --no-build +GapChain.Final:olean` afterwards: `All targets up-to-date (21147 jobs).` The kernel accepted Final.lean; its four `example` lines elaborated. My own `#print axioms` run gives `[propext, Classical.choice, Quot.sound]` for the Final top theorem, with no `sorryAx`, and the Stage 0 control shows `sorryAx`. My own traversal (not `collectAxioms`) reaches 340,483 constants from the Final top theorem and finds the same three axioms and no `sorryAx`; from the Stage 0 top theorem it reaches `sorryAx`. The receipt's note that Stage 0's `neutralPhysicalSeed_of_mNeutral` carries `sorryAx` is confirmed. All four proved stage constants have types syntactically equal to the Stage 0 placeholders they replace.

SHA-256 of the committed sources I built (copies verified equal):

```text
3aac669c7a910ec2389f4e4f921b605adf6ebf2d1e0c9b9cd0be4d33f3f5db71  lean-toolchain
f2d2d22de26009a946d9a6c47180353c7fae5135f874b614ff0edf7db3603864  lakefile.toml
dd87171d4979c6d8ffef3e4c99829b522bdb9ab4ba4ae7edc5c6139b634e02f5  GapChain/Assembly.lean
af33bbe94fa48e63bae58e04ff728bdd30b7e35af2d51acf519cc2d4a6c71dae  GapChain/Final.lean
98b041f1e2d7a59252af528b280fe5c40334c7fe363c2f9ba4f1a26972d93e68  GapChain/LemmaM1.lean
308cf7fa1ef8b6dc510992ea5fe28bc56829f7651f32a843e83804064d35248d  GapChain/Periodic.lean
214444f13b68d9b4b8390d843af32ab3f1ece94a610d90b988ba41d59ff16b92  GapChain/SequenceLemma.lean
eb46735f0a44a13524c1cec8e1c0d3a4f220f3e7fa25f41a81a0c5954a069a1c  GapChain/Stage0.lean
989e49720b4d8093479812dec3d85fbd03eba02124a6f1dc27fe37810b33db87  GapChain/Stage2.lean
6fee80c685c8e60806af2707b4e6c02387a29d3e1c922cd2722c2ecadcd7eb6b  GapChain/Stage3.lean
24c31a781243266a0b358d7841678de5736e56631fcab17fcd69403ef5364cf0  GapChain/Stage3b.lean
1c19a96e9b79cf19689df32849fcf41e716078c42e503107b62ae3a9a825ab1d  GapChain/Stage4.lean
bcd3e031c8550f5b493c5837cd34f9841098835db41adf30cb69b29d2616f35c  GapChain/TheoremS.lean
dc9cc02c3cf3f0ea15004901a014430bdafa6b6fc8344c4650f4cbf245aea8a1  GapChain/Trace.lean
4632ca88bc2345004cf2eecd8e581ab5e34cec817d401d252f7bfd30b17fa240  GapChain/Transfer.lean
71422003ba8a11cf2c5d5b040988822a09c388a4897c84e09fb050e2f5a4f5e0  GapChain/Wilson.lean
```

(`lakefile.toml` is listed but not used; see setup.) `Final.olean` from my build: `d54b29648759fa07c5bcb23b1749498de81926585a6e3f9eb39102022d7f3391`. It differs from the author's `a1804e4b...`, as expected for a different project path and package layout (oleans embed paths); it is not a byte reproduction of their artifact, and none was required. Check.lean SHA-256: `63f7949f3aca9a27ba0e6a2049d9752ac2cbb36273591207b81502b7a98e17ef`.

Measurements (`/usr/bin/time -l` around nice + sandbox-exec + lake; wall in seconds; peak RSS is the largest single process, in bytes; "compile" is Lake's own time for the module):

| Run | Free at start | Wall s | Compile s | Peak RSS bytes |
|---|---:|---:|---:|---:|
| SequenceLemma | 70% | 25.54 | 21 | 2,982,903,808 |
| LemmaM1 | 70% | 4.84 | 3.5 | 3,176,513,536 |
| TheoremS | 70% | 4.49 | 3.2 | 3,402,661,888 |
| Wilson | 70% | 5.95 | 4.5 | 3,402,072,064 |
| Transfer | 70% | 5.14 | 3.8 | 3,464,085,504 |
| Trace | 70% | 3.76 | 2.6 | 3,417,915,392 |
| Stage0 | 70% | 131.58 | 116 | 7,234,125,824 |
| Stage2 | 63% | 179.73 | 139 | 7,345,520,640 |
| Stage3 | 63% | 269.89 | 230 | 7,355,121,664 |
| Stage3b | 64% | 181.46 | 139 | 7,271,956,480 |
| Stage4 | 63% | 187.64 | 148 | 7,354,908,672 |
| Final | 63% | 168.42 | 129 | 7,352,270,848 |
| up-to-date check | 64% | — | — | — |
| Check.lean (`lake env lean`) | 64% | 241.00 | — | 7,610,286,080 |

A first attempt failed at once with `unknown module GapChain.SequenceLemma` (my lakefile had `roots` instead of `globs`); nothing was built; log `build-summary-attempt1.txt`. Check.lean also needed one fix of my own meta code (wrong API name); the first run's `#print axioms` lines were the same.

**Deviation, memory.** Peak RSS of the Stage 0 to Final compilations was 7.2 to 7.6 GB, above the 6 GB cap that row 1670's brief names. My 6 GB kill watchdog had exited before Stage 0 started (found at 08:37Z), so it did not guard Stage 0 to Stage 3; a sampler from Stage 3b on logged free memory every 5 s (minimum 56 percent; its RSS column did not capture the lean process). `memory_pressure` never reported less than 56 percent free during the builds, so most of the RSS is file-backed mapped olean pages (the author ran a pager to evict those, which explains their 4.86 GB). No swap pressure was seen; I record the cap excess as a fact, not as a harm.

Not done: `lean4checker` (an independent re-check of the imported oleans by a second kernel run) was not run; Check.lean trusts the oleans that my builds produced, as `#print axioms` always does.

Verbatim output of Check.lean:

```text
'GapChain.Final.su2_fixed_observable_gap_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Final.massGap_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.su2_fixed_observable_continuum_limit' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.su2_fixed_observable_gap_of_mNeutral' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.Final.kappaSeedAlong_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Final.expClusters_of_mNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.neutralPhysicalSeed_of_mNeutral' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'GapChain.Stage4.neutralTail_of_rankOneAtTime' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.kappaSeed_of_neutralPhysicalSeed' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage3b.expClusters_of_kappaSeed' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage2.massGap_of_expClusters' depends on axioms: [propext, Classical.choice, Quot.sound]
GapChain.Final.su2_fixed_observable_gap_of_mNeutral: reached 340483 constants (267389 theorems, 67 opaque, 0 unsafe); axioms [propext,
 Classical.choice,
 Quot.sound]; sorryAx reached: false
GapChain.su2_fixed_observable_gap_of_mNeutral: reached 338637 constants (265917 theorems, 67 opaque, 0 unsafe); axioms [propext,
 sorryAx,
 Classical.choice,
 Quot.sound]; sorryAx reached: true
GapChain.Final.kappaSeedAlong_of_mNeutral vs GapChain.kappaSeedAlong_of_mNeutral: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Final.expClusters_of_mNeutral vs GapChain.expClusters_of_mNeutral: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Final.massGap_of_mNeutral vs GapChain.massGap_of_mNeutral: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Final.su2_fixed_observable_gap_of_mNeutral vs GapChain.su2_fixed_observable_gap_of_mNeutral: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Stage4.neutralTail_of_rankOneAtTime vs GapChain.neutralTail_of_rankOneAtTime: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Stage4.kappaSeed_of_neutralPhysicalSeed vs GapChain.kappaSeed_of_neutralPhysicalSeed: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Stage3b.expClusters_of_kappaSeed vs GapChain.expClusters_of_kappaSeed: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Stage2.massGap_of_expClusters vs GapChain.massGap_of_expClusters: type == : true; levelParams [] / []; kinds thm: true / true
GapChain.Final.su2_fixed_observable_gap_of_mNeutral : YangMills.FixedObservableLimit
  GapChain.FixedObservableContinuumWithGap
def GapChain.FixedObservableContinuumWithGap : ℕ → ℕ → ℝ → Prop :=
fun L M g₀ =>
  ∃ K v ν S X₂ X₄,
    GapChain.FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧
      ∀ (ℓ : ℕ),
        GapChain.MNeutralAll L M g₀ ℓ →
          GapChain.HasMassGap (YangMills.Construction.LimitTheorem.centredOf S) (GapChain.gapRate ℓ) ∧
            GapChain.HasUniqueVacuum (YangMills.Construction.LimitTheorem.centredOf S)
def YangMills.FixedObservableLimit : (ℕ → ℕ → ℝ → Prop) → Prop :=
fun P =>
  ∃ L₀,
    ∀ (L : ℕ),
      Odd L →
        L₀ ≤ L →
          ∃ M δ,
            8 ≤ YangMills.Construction.PeriodicLattice.torusSide L ↑M ∧
              0 < δ ∧
                (∀ᶠ (k : ℕ) in Filter.atTop,
                    ∀ g₀ ∈ Set.Ioo 0 δ,
                      IsLeast
                        {t | 0 < t ∧ YangMills.referenceResponse L (↑M) k (t ^ 2)⁻¹ = YangMills.fixedPhysicalLevel g₀}
                        (YangMills.renormalizedBareCoupling L (↑M) k g₀)) ∧
                  ∀ g₀ ∈ Set.Ioo 0 δ, P L (↑M) g₀
```

## Part B. Faithfulness (reading)

**Item 1. The four example lines. HOLDS (reading, and confirmed by the exact `Expr ==` check in Part A: `type == : true` for all four, no universe parameters).** Each line is `example : type_of% @GapChain.<name> := @Final.<name>` inside `namespace GapChain.Final`, for `<name>` = `kappaSeedAlong_of_mNeutral`, `expClusters_of_mNeutral`, `massGap_of_mNeutral`, `su2_fixed_observable_gap_of_mNeutral`. Name resolution: `GapChain.<name>` inside namespace `GapChain.Final` tries `GapChain.Final.GapChain.<name>` and `GapChain.GapChain.<name>` first; neither exists, so it resolves to Stage 0's constant. `Final.<name>` resolves to `GapChain.Final.<name>`. So each line compares the Final theorem with the Stage 0 constant of the same name. An `example` shows definitional equality only; the exact `Expr` comparison in Check.lean tests syntactic equality.

**Item 2. Inline seed step in `kappaSeedAlong_of_mNeutral`. HOLDS.** Stage 0 (Stage0.lean L130-L131): `NeutralPhysicalSeed Γ β := ∃ u, 3 ≤ u ∧ 512 * u ≤ Γ.side ∧ NeutralTailLE Γ β u (1/2)`. `NeutralRankOneTest` (L95-L96) gives `w` with `1 ≤ w`, `1024 * w ≤ Γ.side` and `RankOneAtTime`. Final takes `u = max 3 (2 * w)`:
- `3 ≤ u` by `le_max_left`.
- `512 * u ≤ Γ.side`: if `3 ≤ 2w`, then `u = 2w` and `512 * 2w = 1024 w ≤ side` (omega from `hwSide`); if `2w ≤ 3`, then `u = 3` and `512 * 3 ≤ 2^70 ≤ side` from `hlarge`, which Final derives from `K j ≥ 70`, `L ≥ 2`, `ℓ ≥ 1` exactly as Stage 0 does. Stage 0's own route needed `1536 ≤ side` for the same case; `2^70` is stronger, so nothing is lost.
- Tail: the second conjunct of `Stage4.neutralTail_of_rankOneAtTime` is `NeutralTailLE Γ β (max 3 (2w)) (4/21)`, destructured into `0 < ‖T‖`, trace summability and `re tr(P₀T^u)/‖T‖^u − 1 ≤ 4/21`; `htail.trans (4/21 ≤ 1/2)` gives the bound at `1/2`. These are the three conjuncts of `NeutralTailLE Γ β u (1/2)` (L123-L127), with `T` the transfer along `TimeAxis.timeIdx`, the axis that `NeutralAtCutoff` uses.
The step is Stage 0's `neutralPhysicalSeed_of_mNeutral` proof text with `neutralTail_of_rankOneAtTime` replaced by its Stage 4 proof and the `1536` bound replaced by `2^70`. The result goes into `Stage4.kappaSeed_of_neutralPhysicalSeed Γ (hβ j) hfour hlarge`, with `hfour` from `4 ∣ ℓ`.

**Item 3. Witness order in the top theorem. HOLDS.** Release (`Formulation/FixedObservableContinuum.lean` L58-L64 in the fixture): `FixedObservableLimit P := ∃ L₀, ∀ L, Odd L → L₀ ≤ L → ∃ M δ, 8 ≤ torusSide L M ∧ 0 < δ ∧ (∀ᶠ k, ∀ g₀ ∈ (0,δ), IsLeast ...) ∧ ∀ g₀ ∈ (0,δ), P L M g₀`. Stage 0 (L337-L340): `FixedObservableContinuumWithGap L M g₀ := ∃ K v ν S X₂ X₄, FixedObservableWitnesses L M g₀ K v ν S X₂ X₄ ∧ ∀ ℓ, MNeutralAll L M g₀ ℓ → HasMassGap (centredOf S) (gapRate ℓ) ∧ HasUniqueVacuum (centredOf S)`. So the six witnesses are bound by one existential outside `∀ ℓ`; they depend on `L, M, g₀` only. In the Final proof, `obtain ⟨K, v, ν, S, X₂, X₄, hw⟩ := (fixedObservableContinuum_iff L M g₀).mp (hlim g₀ hg₀)` takes them once from the release's `su2_fixed_observable_continuum_limit`, and the same tuple goes into the anonymous constructor before `fun _ hs => ...`, so no witness is re-chosen per `ℓ`. `fixedObservableContinuum_iff` is `Iff.rfl`, so `FixedObservableWitnesses` is definitionally the body of the release's `FixedObservableContinuum` (`FixedObservableContinuumWith OSAxioms`), and `M`, `δ`, the side bound and the root clause are passed on from the release unchanged. `L₀` becomes `max L₀ 13` for the admissible blocking factor.

**Item 4. RECEIPT-final.md's statement paragraph. HOLDS.** Clause by clause against the Lean statement:
- "all sufficiently large odd L ... M with torus side at least eight ... δ > 0 ... at all sufficiently late cutoffs the calibrated coupling is the least positive root ... for every 0 < g₀ < δ": the release's `FixedObservableLimit` clauses, as written.
- "witnesses K, v, ν, S, X₂, X₄ satisfying all of FixedObservableWitnesses. Fix these witnesses. For every ℓ satisfying MNeutralAll L M g₀ ℓ": the order of item 3.
- "‖T(t)ψ‖ ≤ e^{−mt}‖ψ‖ for every ψ ⊥ Ω and t ≥ 0, with m = (2/ℓ) log(2^18/5041) > 0": `HasMassGap (centredOf S) (gapRate ℓ)` (L176-L179) and `gapRate` (L240). Lean also asserts the positive semidefinite reflection form and `HasReconstruction`; the receipt calls this "the reconstructed Osterwalder-Schrader space", which is not stronger.
- "Every vector fixed by all time shifts is a scalar multiple of the vacuum": `HasUniqueVacuum` (L181-L184), exactly.
- "The premise requires ℓ > 0, 4 ∣ ℓ and, at all sufficiently large cutoffs k, the calibrated neutral rank-one test on every cube of side ℓL^k ... the MNeutralAll hypothesis, distinct from the purity criterion (PUR-io). Existence of such a seed side remains unproved.": `MNeutralAll` (L157-L158) with `NeutralAtCutoff` (L152-L154), exactly; the two required disclaimers are present.
No clause is stronger than the Lean statement. Minor point, no correction needed: "positive-time separated action-density tensors" describes the release's tuple space in words; the Lean object is `centredOf S` on `PositiveSpan`, checked in Stage 0's check, not here. Not checked: the receipt's sentence on what the Sussman-Alpoge outline and complete account say about the gap (cited lines not fetched in this row), and the author's artifact counts and hashes.

## Verdicts

Finished 2026-11-28T08:53:48Z (date -u).

- Part A, kernel claim of row 1670: **REPRODUCED** on an independent data path (my own project layout, lakefile, manifest and sandbox; no artifact or log of the author's scratch folders used). Final top theorem: `[propext, Classical.choice, Quot.sound]`, no `sorryAx`; Stage 0 control: `sorryAx` present.
- Item 1: HOLDS (exact type equality, not only definitional).
- Item 2: HOLDS.
- Item 3: HOLDS.
- Item 4: HOLDS. No wording is stronger than the Lean statement.
- Defects that break something: none. Deviation: compiler peak RSS 7.2 to 7.6 GB, above the 6 GB cap of row 1670's brief, with at least 56 percent memory free throughout.

What this does not establish: the seed (`∃ ℓ, MNeutralAll L M g₀ ℓ`) is a hypothesis and is not proved; the faithfulness of the Stage 0 definitions themselves (`HasMassGap`, `NeutralRankOneTest`, `ExpClusters`, `Inputs`) rests on the Stage 0 check (row 1653) and was not repeated; `lean4checker` was not run.

Credit: the release (YM4 Lean at 3932084a) is by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Final.lean and its receipt are by gpt-6.2-astra max (row 1670); the design and its check are rows 1457 and 1458; the stages are rows 1652, 1654, 1657, 1658 and 1667, with checks 1653, 1665, 1666, 1668 and 1669.
