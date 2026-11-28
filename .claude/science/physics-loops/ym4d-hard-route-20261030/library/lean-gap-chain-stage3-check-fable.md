lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T18:44Z

# Check of Lean Stage 3 of the gap chain (queue row 1666, checks FINISH row 1657)

Started 2026-11-28T06:44Z (date -u). Pinned commit 787645f36. Status: in progress; sections are appended as each item is checked.

Reader: Claude Fable 5.2, high effort. The author of Stage 3 was gpt-6.2-astra max. I did not run Lean. I read the Lean source and the receipt only.

## 0. Sources read (updated as the check proceeds)

- `lean/gapchain/GapChain/Stage0.lean` (all 376 lines); `library/lean-gap-chain-stage0-check-opus.md` (all, row 1653).
- `lean/gapchain/RECEIPT-3.md` lines 1-140 (text, kernel result, first remaining estimate, trusted base).
- `lean/gapchain/GapChain/Stage3.lean`: the list of all 114 `def`/`abbrev`/`structure` lines (by grep), and in full the ranges 5770-6005, 6008-6082, 6484-6608, 7380-7608. More ranges are listed in the sections below.
- `lean/gapchain/GapChain/TheoremS.lean` 310-540 (`BoxSpectrum`, `gap`, `thermal`, `TorusData`, `seed`).
- SHA-256 of `Stage3.lean` at the pinned commit: `6fee80c6...d7eb6b`. It is equal to the receipt's value.

Credit: the YM4 Lean release and its conventions are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Stage 3 is by gpt-6.2-astra (row 1657). Theorem S-w and EV-L are row 731 of this lane.

## 6. Forbidden keywords (item 6) — HOLDS

`grep -c -w` on `Stage3.lean` (8011 lines), whole-word match, comments included:

| word | lines | occurrences |
|---|---:|---:|
| `sorry` | 0 | 0 |
| `admit` | 0 | 0 |
| `axiom` | 0 | 0 |
| `native_decide` | 0 | 0 |
| `opaque` | 0 | 0 |
| `implemented_by` | 0 | 0 |

More counts: 402 lines start with `theorem` (or `private theorem`, `lemma`); 402 lines start with `#print axioms`. The words `unsafe`, `partial def`, `extern`, `macro`, `syntax`, `elab`, `reduceBool` and `trustCompiler` do not occur. `decide` occurs only as the `Decidable.decide` function in definitions and as the kernel tactic `by decide` on small closed facts. The only options set are `autoImplicit false`, `Elab.async false` and three `maxHeartbeats` raises. The receipt's statement (no sorry, axiom or native_decide) agrees with the file.

## 1. The two reduction theorems (item 1) — HOLDS

Quoted from `Stage3.lean` 7567-7593:

```lean
theorem expClusters_of_seeded_pairWindows {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K}
    {S : CumulantFamily} (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K)
    (supply : ∀ j, (∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ (K j : ℕ) →
        KappaSeedOnCube Γ (betaAt L M (K j) g₀)) →
      PairWindowEstimate L (K j) (betaAt L M (K j) g₀) (ν j) (rectangularTorusData (h.beta_pos j)).choose
        (gapRate ℓ * PeriodicLattice.meshSize L ((K j : ℕ) : ℤ))) :
    ExpClusters L K ν (gapRate ℓ)

theorem expClusters_of_kappaSeed_of_pairWindows (supply : ∀ {L : ℕ} (k : ℕ+) {β : ℝ}
    (ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ)))),
    Conventions.IsAdmissibleBlockingFactor L → ∀ hβ : 0 < β, IsInfiniteVolumeLimit L k β ν →
    ∀ r : ℝ, 0 < r → PairWindowEstimate L k β ν (rectangularTorusData hβ).choose r) :
    type_of% @GapChain.expClusters_of_kappaSeed
```

Stage 0 (`Stage0.lean` 275-277, with the section variables `{L M} {g₀} {K} {ν} {S}`):

```lean
theorem expClusters_of_kappaSeed (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K) :
    ExpClusters L K ν (gapRate ℓ)
```

- `expClusters_of_kappaSeed_of_pairWindows`: the result type is written `type_of% @GapChain.expClusters_of_kappaSeed`. Lean elaborates this to the type of the Stage 0 constant itself. So the conclusion is that type by construction, binders included, and the kernel checked the proof against it. The only hypothesis is `supply`. `supply` is a closed statement: it has no seed, no `Inputs`, no `K`, no `S`. It asks for `PairWindowEstimate` at every admissible `L`, every cutoff `k`, every `β > 0`, every infinite-volume limit `ν` and every rate `r > 0`, at the torus data `(rectangularTorusData hβ).choose`. **HOLDS**: Stage 0's type after one premise, and nothing else.
- `expClusters_of_seeded_pairWindows`: the hypotheses are Stage 0's three (`hL`, `h`, `hs`) and `supply`. The conclusion `ExpClusters L K ν (gapRate ℓ)` is Stage 0's conclusion, letter for letter. Here `supply` asks for the estimate only at one rate, `gapRate ℓ * a_j`, only at the given `(K j, β_{K j}, ν j)`, and only at a `j` where the seed holds on every cube of side `ℓ L^(K j)`. **HOLDS**. This form is not stated with `type_of%`, because `supply` comes after `hs` and reads `h`; the second theorem is the one that gives literal agreement.
- The second theorem is proved from the first (line 7589). It discards the seed that the first one offers to `supply`. So the closed premise is stronger than what the proof uses. This matters for item 2: the closed premise must be true at every `β`, not only at seeded cutoffs.

No correction is needed.
