lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-28T18:35:07Z

# Faithfulness check of Lean Stage 2 of the gap chain (queue row 1665)

Started 2026-11-28T06:35:07Z (date -u). Pinned commit b31d9c96b, branch
claude/ym4d-hard-route. Reader: Claude Opus 5.5, high reasoning, Mac mini
worker. Lean was not run. Object of check: lean/gapchain/GapChain/Stage2.lean
and lean/gapchain/RECEIPT-2.md (FINISH row 1654, by gpt-6.2-astra max).
Baseline: library/lean-gap-chain-stage0-check-opus.md (row 1653).

Status: in progress. Sections are added as each step finishes.

## 0. Sources read

- `lean/gapchain/GapChain/Stage2.lean`, all 657 lines. SHA-256 `989e4972…db87`, equal to the hash in RECEIPT-2.
- `lean/gapchain/RECEIPT-2.md`, all. FINISH rows 1654 and 1665.
- `library/lean-gap-chain-stage0-check-opus.md` (row 1653), all.
- `lean/gapchain/GapChain/Stage0.lean` L1-30 and L170-292 (HasMassGap, HasUniqueVacuum, listMoment, latticeU, CutoffStates, ExpClusters, Inputs, the Chain section).
- Release declarations: see Section 3 for the files I read and the ones I could not read.

Method: I compare each statement and definition with Stage 0 and with the hand construction (check 1458, cited by the receipt). Lean was not run. Where the kernel's acceptance settles a point, I say so and rely on the receipt's build log.

## 1. Item 1: the declaration that discharges massGap_of_expClusters

Quote, Stage2.lean L588-590 (inside `namespace GapChain.Stage2`, file variables L23):

```lean
variable {L M : ℕ} {g₀ : ℝ} {K : ℕ → ℕ+} {ν : CutoffStates L K} {S : CumulantFamily}
theorem massGap_of_expClusters (hL : Conventions.IsAdmissibleBlockingFactor L)
    (h : Inputs L M g₀ K ν S) {m : ℝ} (hm : 0 < m) (hc : ExpClusters L K ν m) :
    HasMassGap (centredOf S) m
```

Stage0.lean L250-254 has the same section variables, in the same order, and the same binders and conclusion, character for character.

The agreement check is L613:
`example : type_of% @GapChain.massGap_of_expClusters := @massGap_of_expClusters`.

Which constant does the bare name on the right resolve to? Inside `namespace GapChain.Stage2`, both `GapChain.Stage2.massGap_of_expClusters` and `GapChain.massGap_of_expClusters` are visible. If the right side named the Stage 0 constant, the example would be `X : type X`, which proves nothing. I settle this from the receipt's axiom report, not from the Lean name-resolution rule:
- L618, in the same namespace, uses the same bare name in `uniqueVacuum_of_expClusters`.
- The receipt reports `uniqueVacuum_of_expClusters` depends on `[propext, Classical.choice, Quot.sound]` only. The Stage 0 constant depends on `sorryAx` (RECEIPT-0, check 1653 Section 6).
- So at L618 the bare name resolved to the Stage 2 constant. (If both had been candidates and both elaborated, Lean would have reported an ambiguity error and the build would have failed.)
- L613 has the same name in the same scope, so it also names the Stage 2 constant.

So the kernel checked that `@GapChain.Stage2.massGap_of_expClusters` has the type of `@GapChain.massGap_of_expClusters`, with every implicit binder (the `@` forms). The check is up to definitional equality. That is enough: Stage 0's type was found faithful (check 1653, Sections 3-4).

Extra hypotheses: none. The `Completion` section adds `variable {σ} {hσ}` (L520). The statement does not mention σ or hσ, so Lean does not add them; an extra binder would also make the L613 example fail. `hm : 0 < m` is in the signature and not used in the proof (the linter is switched off, L586). That is harmless: the proof shows the bound for every m, and the signature only matches Stage 0.

Note: Stage 2 does not change Stage 0. `GapChain.massGap_of_expClusters` keeps its `sorry`. The Stage 0 compositions `massGap_of_mNeutral` and `su2_fixed_observable_gap_of_mNeutral` still call the Stage 0 constant, so their axiom lists keep `sorryAx` until a later stage rewires them to `Stage2.massGap_of_expClusters`. Stage 2 discharges the placeholder in the sense "a sorry-free term of the same type exists", which is what the brief asked.

Verdict item 1: **HOLDS.**

## 4. Item 4: forbidden tokens in Stage2.lean

Counts by `grep -c` (lines) and `grep -ow` (whole words), run on the pinned file:

| token | lines | whole words |
|---|---:|---:|
| sorry | 0 | 0 |
| admit | 0 | 0 |
| axiom | 33 | 0 |
| native_decide | 0 | 0 |
| opaque | 0 | 0 |
| implemented_by | 0 | 0 |

The 33 lines with `axiom` are the 33 `#print axioms` commands (L625-657); the whole word is `axioms`, so no `axiom` declaration exists. There are 33 theorems and 33 print commands, one each, matching the 33 reports in RECEIPT-2. No `instance` and no `local` attribute. The file has two `set_option` lines (autoImplicit false, Elab.async false) and one `set_option linter.unusedVariables false in`; none changes what the kernel accepts. The receipt says the build used the default heartbeat limit; I see no `maxHeartbeats` option in the file.

Verdict item 4: **HOLDS** (all six counts are zero as declarations).
