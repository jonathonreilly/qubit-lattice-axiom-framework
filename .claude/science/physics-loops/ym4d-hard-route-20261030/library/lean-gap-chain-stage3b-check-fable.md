lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T19:53:08Z

# Check of Lean Stage 3b of the gap chain (row 1669, checks row 1667)

Started 2026-11-28T07:53:08Z (date -u). Pinned commit fd75828e2.
Kind: reading check of statements and definitions. Lean was not run. Proofs were not replayed.
Files read: `lean/gapchain/GapChain/Stage3b.lean` (718 lines), `lean/gapchain/RECEIPT-3b.md`,
the named anchors of `Stage3.lean`, and `library/lean-gap-chain-stage3-check-fable.md` (row 1666).

Status: IN PROGRESS. Sections are appended as each item is done.

Credit: the YM4 Lean release and its conventions are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Theorem EV-L is row 731; row 732 checked it. Stage 3b is by gpt-6.2-astra max (row 1667).

SHA-256 of the sources at fd75828e2 are equal to the receipt's values: `Stage3b.lean` `24c31a78...5364cf0`, `Stage3.lean` `6fee80c6...d7eb6b`.

## 5. Keyword counts (item 5)

`grep -c -w` and `grep -o -w` on `Stage3b.lean` (718 lines, comments included): `sorry` 0, `admit` 0, `axiom` 0, `native_decide` 0, `opaque` 0, `implemented_by` 0 (lines and occurrences). Also 0: `unsafe`, `extern`, `macro`, `reduceBool`, `decide`, `instance`, `class`, `inductive`. The file has 26 `theorem` lines and 26 `#print axioms` lines; the 26 names are the 26 names of the receipt. Options set: `autoImplicit false`, `Elab.async false`, one `maxHeartbeats 900000`.

## 1. The closed premise and the Stage 0 type (item 1) — HOLDS

`Stage3b.lean` 613-617 and 688-689:

```lean
theorem pairWindowEstimate {L : ℕ} (k : ℕ+) {β : ℝ}
    (ν : Measure (GaugeField (PeriodicLattice.meshSize L ((k : ℕ) : ℤ))))
    (hL : Conventions.IsAdmissibleBlockingFactor L) (hβ : 0 < β)
    (hν : IsInfiniteVolumeLimit L k β ν) (r : ℝ) (hr : 0 < r) :
    PairWindowEstimate L k β ν (rectangularTorusData hβ).choose r

theorem expClusters_of_kappaSeed : type_of% @GapChain.expClusters_of_kappaSeed :=
  expClusters_of_kappaSeed_of_pairWindows @pairWindowEstimate
```

`supply` at `Stage3.lean` 7583-7586 is `∀ {L : ℕ} (k : ℕ+) {β : ℝ} (ν : Measure (GaugeField (meshSize L ((k : ℕ) : ℤ)))), IsAdmissibleBlockingFactor L → ∀ hβ : 0 < β, IsInfiniteVolumeLimit L k β ν → ∀ r : ℝ, 0 < r → PairWindowEstimate L k β ν (rectangularTorusData hβ).choose r`.

- The binders agree one by one: `{L}`, `(k : ℕ+)`, `{β}`, `(ν)`, admissible `L`, `0 < β`, the limit, `r`, `0 < r`. The conclusions are the same term. `pairWindowEstimate` has no other hypothesis. Stage 3b defines no second `PairWindowEstimate`; the name is Stage 3's (line 6510).
- The final proof term is one application of Stage 3's theorem to `@pairWindowEstimate`, with no other argument. So the kernel accepted the type of `pairWindowEstimate` as `supply`.
- `GapChain.expClusters_of_kappaSeed` is declared one time in the folder (`Stage0.lean` 275, proof `sorry`). `type_of%` reads only its type. So the Stage 3b theorem has the Stage 0 type: `(hL) (h : Inputs L M g₀ K ν S) {ℓ} (hs : KappaSeedAlong L M g₀ ℓ K) : ExpClusters L K ν (gapRate ℓ)`. Its axiom line has no `sorryAx`.
- The seed `hs` stays a hypothesis. That is Stage 0's design.
