lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-28T19:34Z

# Check of Lean Stage 4 of the gap chain (FINISH row 1668)

Provenance: Claude Opus 5.5, effort high, Mac mini worker, commit d34cad103.
Not an audit. Started 2026-11-28T07:34:27Z (date -u). I did not run Lean.
I read the source text only.

Subject: `lean/gapchain/GapChain/Stage4.lean` and `lean/gapchain/RECEIPT-4.md`
(row 1658, gpt-6.2-astra max). This is a check from a different provider.

## Repo search

Reading check only; PR branches not searched. In the lane: `grep -c` of `neutralTail_of_rankOneAtTime`, `kappaSeed_of_neutralPhysicalSeed`, `FluxSpectrum` and `aligned_half_small` in `library/open-core.md` gives 0. In FINISH.md the two theorem names occur only in rows 1652, 1653, 1658 and 1668; the other two names do not occur. This report states no new mathematical statement.

Sources read: `RECEIPT-4.md`; `Stage4.lean` L1-352 and L727-1397 (L353-726, the geometric lemmas, only their declaration lines), plus a count of the `#print axioms` lines; `Stage0.lean` L60-160; the statements in `Stage3.lean` that Stage 4 cites (named below); `LemmaM1.lean` L40-60; `Wilson.lean` L477-479; `library/gap-solve9-astra62.md` L205-227; the check files of rows 1653 and 1666. SHA-256 of `Stage4.lean` = `1c19a96e...a1d`, the same as in the receipt. I rely on the receipt for the kernel output; I did not reproduce it.

## 0. Verdicts

| Item | Verdict |
|---|---|
| 1. Types of the two public theorems | **HOLDS** |
| 2. New definitions and intermediate hypotheses | **HOLDS**, none trivializes |
| 3. W8 reads the release neutral trace at 2w and max(3, 2w) | **HOLDS** |
| 4. W7: cube, coupling, half-period map, constants | **HOLDS** (one scope remark: the route is not row 1161's, see 4.4) |
| 5. Keyword counts | all 0 |

## 1. The two public theorems (item 1) — HOLDS

`Stage4.lean` L202-208 and L1372-1374, L1397:

```lean
theorem neutralTail_of_rankOneAtTime (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    {w : ℕ} (hw : 1 ≤ w) (h : RankOneAtTime Γ μt β w) :
    NeutralTailLE Γ β (2 * w) (4 / 21) ∧ NeutralTailLE Γ β (max 3 (2 * w)) (4 / 21)
example : type_of% @GapChain.neutralTail_of_rankOneAtTime := @neutralTail_of_rankOneAtTime

theorem kappaSeed_of_neutralPhysicalSeed (Γ : CubicPeriodSublattice) {β : ℝ} (hβ : 0 < β)
    (hfour : 4 ∣ Γ.side) (hlarge : 2 ^ 70 ≤ Γ.side) (hs : NeutralPhysicalSeed Γ β) :
    KappaSeedOnCube Γ β
example : type_of% @GapChain.kappaSeed_of_neutralPhysicalSeed := @kappaSeed_of_neutralPhysicalSeed
```

- I compared the binder text with `Stage0.lean` L127-129 and L145-147 by `diff`, after the substitution μt = `TimeAxis.timeIdx` (L26 is `local notation "μt" => TimeAxis.timeIdx`). The text is identical. Stage 0's `variable (Γ) (μ)` (L34) is inside `section Slice`, which ends at L82, so no binder is added there.
- No Stage 0 name is redefined in Stage 3 or Stage 4 (grep), so the Stage 4 types use the Stage 0 constants.
- In each `example` the right side resolves to the Stage 4 theorem (innermost namespace). Were it the Stage 0 constant, the line would be trivial; the textual identity settles the point either way, and the receipt's axiom report for `GapChain.Stage4.…` has no `sorryAx`.
- No extra hypothesis. `SectorBasis` and `FluxSpectrum` are built inside the proofs, not assumed.

Remark (not a defect): Stage 0's two `sorry` declarations stay. Stage 4 adds new constants of the same type, so a sorry-free chain must call `GapChain.Stage4.…`. The receipt says so.

## 2. New definitions and intermediate hypotheses (item 2) — HOLDS

- The public types contain only Stage 0 definitions, so no new definition can weaken them, and there is no premise to be vacuous (section 1).
- No junk value meets a Stage 0 statement. W8: `projectedTrace_eq_sectorWeight` proves `TraceSummablePW` and `tracePW(P₀Tᵃ) = sectorWeight(n,n,n,a; 0,0)` for a ≥ 2 (not the `tsum` default 0), and `periodicTransfer_norm_pos` gives ‖T‖ > 0. W7: `FluxSpectrum.vacuum` and `moment` give `sectorMoment 0 0 t ≥ 1`, so `kappaWeight/top^N ≥ 1`.
- `SectorBasis`: an eigenbasis with values ≥ 0 and the sector moments as sums for a ≥ 2, built on the release slice by `exists_positive_slot_basis` (zero eigenspace included).
- `FluxSpectrum`: per sector (q, m), levels in [0, 1], first maximal, vacuum level 1, moments = `sectorMoment q m t` (t ≥ 2), and a second top slot when misaligned (section 4.2). `cubeFluxSpectrum` builds it from `boxSector_labeledList` (one slot per positive eigenvector, with multiplicity).
- `sectorMoment Γ β χ m t` = `sectorWeight β (n,n,n,t) χ m / ‖Γ.transfer μt β‖ᵗ`: every sector uses the release periodic vacuum, as row 1161 requires. `rawMoment` has the same denominator.
- Finite tables (`inFrame`, `crossedCoeff`, `magneticRow`, `shear`, `comparisonPath`, `pureTwist`, `referenceTwist`) enter through lemmas that `decide` checks. `misaligned m q` = m ≠ 0 ∧ q ≠ 0 ∧ q ≠ m: neither empty nor universal, as in row 1161 ("for Mq ≠ 0"). The geometric definitions (`halfTurn` … `magneticShift`) only build the map of 4.2.
- Index types `Flux` (8), `spatialAxis` (3), `Shear` (12), `TwistIndex` (64) are not empty. `PositiveSlot T` is empty only for a zero sector, which `misaligned_partner` treats on its own (`v 0 = 0`).
- No Stage 3 open Prop occurs: `grep -c` of `PairWindowEstimate|SlabEstimate|NeutralSlabComparison|CubicTraceIdentity` in `Stage4.lean` is 0.

## 3. W8 (item 3) — HOLDS

- `h : RankOneAtTime Γ μt β w` is about Stage 0's `neutralProj Γ μt * Γ.transfer μt β ^ w`. The proof rewrites it by `electricProj_zero` (Stage 3 L1241: `electricProj Γ zeroFlux = neutralProj Γ TimeAxis.timeIdx`, a bijection of the eight terms onto the eight cut sets) and `magneticTransfer_zero` (`= Γ.transfer μt β`); `projected_power` gives P₀Tʷ = (TP₀)ʷ.
- M1 and the trace use **one** basis B = `releaseSectorBasis Γ hβ 0 0`, an eigenbasis of TP₀ on the release slice. `lemmaM1_hsSq` gives (1 − (2/5)²) Σᵢ vᵢ^(2w) ≤ ‖(TP₀)ʷ‖² ≤ ‖T‖^(2w), with Σᵢ vᵢ^(2w) = `sectorWeight(n,n,n,2w; 0,0)`.
- `neutralTail_iff_sectorWeight` unfolds Stage 0's `NeutralTailLE` and rewrites back by the same two lemmas. So the bounded quantity is `(tracePW (neutralProj Γ μt * Tᵃ)).re / ‖T‖ᵃ − 1` at a = 2w (`le_rfl`) and a = max(3, 2w) (`le_max_right`).
- `pwTrace_of_eigenbasis` passes to the release Peter–Weyl basis by Parseval and Tonelli on the terms vᵢ|⟨e_k, bᵢ⟩|² ≥ 0. This gives the absolute summability that `TraceSummablePW` asks.
- Monotonicity uses vᵢ ≤ ‖TP₀‖ ≤ ‖T‖ (`neutral_projection_norm_le`: ‖P₀‖ ≤ 1 from the C*-identity). No neutral top eigenvector is assumed. This is the route of check 1653 P1.

## 4. W7 (item 4) — HOLDS

### 4.1 Conclusion

`KappaSeedOnCube Γ β`, same Γ and β as the hypothesis. The proof shows Stage 0's sides equal `boxSides (cube n) (n/2)` = ![n, n, n, n/2] (`fin_cases`), uses `kappaWeight_eq_diagonal` (the eight diagonal sectors, checked in row 1666) and the same top ‖Γ.transfer μt β‖, whose positivity comes from `boxNeutral_norm_pos` and `calibrated_cubicNorm`. So it is S_κ(n/2; n³) < 2⁻¹⁸ on the same cube.

### 4.2 The antilinear half-period map

`misaligned_not_simple`: J = D ∘ C, C complex conjugation, D = `magneticShift h m i` the compensated half-period translation on the box 2h. J maps the eigenspace V_r into itself (D commutes with the sector; the kernel is real). D² is the centre translation by `magneticRow m i` (`magneticShift_square`), which acts on sector (q, m) by a character that is −1 for some i when m, q are misaligned (`misaligned_row`, `decide`). J² = −1 follows by cancelling r ≠ 0 (`hr : 0 < r`), so it is proved **only on V_r with r > 0**. Then `finrank_ne_one_of_antilinear` gives dim V_r ≠ 1.

The only caller, `misaligned_partner`, takes r from a `PositiveSlot` (r > 0) and treats v 0 = 0 without J; the cube enters as n = 2k + 2k from `4 ∣ n`. No zero eigenspace and no non-misaligned sector uses J.

### 4.3 Constants, from 4 ∣ n, 2⁷⁰ ≤ n and the seed 3 ≤ u, 512u ≤ n

I re-derived each by hand.

- **k = ⌊n/2⁶⁹⌋** (`differenceStep`). 2⁶⁹ ≤ n gives k ≥ 1. n < 2⁶⁹(k+1) ≤ 2⁷⁰k because k ≥ 1. u + k + 2⁶⁸k ≤ n(2⁻⁹ + 2⁻⁶⁹ + 2⁻¹) < n. Also 2 ≤ n − k.
- **Short moment 3/2.** X₀₀(u) ≤ 3/2 from the seed; `sectorWeight_le_periodicNeutral` (two frame changes, positivity) gives every X_qm(u) ≤ 3/2. Lean needs only u ≥ 2.
- **Misaligned and tails.** (3/2)(3/4)^511 ≤ 2⁻¹⁶⁹, because (3/4)³ < 1/2 and 3·170 = 510 ≤ 511 (`short_ratio_at`). This needs 512u ≤ n. The neutral excess X₀₀(n) − 1 is at most the same bound.
- **Second difference.** z^(n−k)(1 − z^k)² ≤ z^u ((z^k)^(2⁶⁷)(1 − z^k))² ≤ z^u 2⁻¹³⁴, by p z^p(1 − z) ≤ 1 − z^p with p = 2⁶⁷. This needs n − k ≥ u + 2·2⁶⁷k, from the budget. The sector sum is ≤ (3/2)2⁻¹³⁴ ≤ 2⁻¹³³. Fourier inversion over 8 characters gives 2⁻¹³⁰. Positivity at n ± k then gives |crossed misaligned drop| ≤ 2⁻¹³⁰ + 2·2⁻¹⁶⁹ ≤ 2⁻¹²⁹. A shear changes one value by at most 16 times that, and a path has at most 4 shears, two paths per comparison: 128·2⁻¹²⁹ = 2⁻¹²².
- **2⁻¹²¹.** The magnetic drop Z_n(0,m) − Z_{n+k}(0,m) ≤ (X₀₀(n) − X₀₀(n+k)) + 2⁻¹²² ≤ 2⁻¹⁶⁹ + 2⁻¹²² ≤ 2⁻¹²¹ (`pureMag_upper`, using X₀₀(n+k) ≥ 1).
- **2⁻⁴⁹.** x = ρⁿ, ρ the top level of the aligned sector (m, m). ρⁿ + ρⁿ ≤ X_mm(n) + X_0m(n) ≤ Z_n(0,m) ≤ 1 + 2⁻¹⁶⁹ + 2⁻¹⁶⁰ ≤ 3/2 gives x ≤ 3/4. Next, x(1 − ρᵏ) ≤ 2⁻¹²¹. Then 1 − x ≤ 1 − (ρᵏ)^(2⁷⁰) ≤ 2⁷⁰(1 − ρᵏ), from n ≤ 2⁷⁰k. Together: x(1 − x) ≤ 2⁻⁵¹, so x/4 ≤ 2⁻⁵¹ and x ≤ 2⁻⁴⁹.
- **2⁻²².** ρ^(n/2) = √x ≤ 2⁻²⁴·⁵ ≤ 2⁻²². This needs (n/2)·2 = n, from 4 ∣ n.
- **(3/2)(3/4)^255 ≤ 2⁻⁸⁴.** 3·85 = 255. It is applied at t = n/2 with (255+1)u ≤ n/2, which follows from 512u ≤ n.
- **Sum.** S_κ ≤ 2⁻⁸⁴ + 7(2⁻²² + 2⁻⁸⁴) = (7/16 + 2⁻⁶³)·2⁻¹⁸ < 2⁻¹⁸.

No other numerical premise occurs.

### 4.4 Comparison with row 1161, L213-227

The statement is row 1161's statement, so the conclusion is faithful. The route is not row 1161's:
- Row 1161 uses a real exponent, |I''| ≤ 768 and a Taylor step at r = ⌈n2⁻⁷⁰⌉/n. Lean uses the integer step k and the exact identity z^(n+k) + z^(n−k) − 2zⁿ = z^(n−k)(1 − zᵏ)².
- Row 1161 splits into two alternatives (the seven periodic charged top weights all small, or all large). Lean has no split: for every m ≠ 0 it bounds the aligned top level from the magnetic mass (x ≤ 3/4) and the magnetic drop. So the constants differ (row 1161: 2⁻⁵⁹, 2⁻⁵¹, 2⁻⁴⁷, 2⁻⁴⁶; Lean: 2⁻¹²¹, 2⁻⁴⁹); 2⁻⁸⁴ and 2⁻²² + 2⁻⁸⁴ are common. Row 1643's check of the row 1161 numbers is therefore not what this proof uses; 4.3 checks the Lean numbers directly.

Not checked: the proofs of the geometric lemmas and of the Stage 3 identities (the kernel checked them).

## 5. Keyword counts (item 5)

`grep -c -w` on `Stage4.lean` (1491 lines, comments included): `sorry`, `admit`, `axiom`, `native_decide`, `opaque`, `implemented_by` all 0; also `unsafe`, `extern`, `macro`, `reduceBool` 0. 91 `theorem` lines, 91 `#print axioms` lines. The axiom list [propext, Classical.choice, Quot.sound] is the receipt's kernel output, not re-run.

## 6. For the lead

1. W7 and W8 are discharged at the Stage 0 types under `GapChain.Stage4` names. Still open on the chain: `expClusters_of_kappaSeed` (EV-L assembly) and the seed (M-neutral-all).
2. W7 uses its own route (4.4); cite Stage 4 and 4.3 for its constants, not row 1161's.
3. No defect found that breaks a consumer.

RESULT row 1668 (Claude Opus 5.5 high, reading check of row 1658; no Lean run): items 1-4 HOLD and item 5 counts are all 0. Both Stage 4 theorems have Stage 0's types word for word, with no extra hypothesis. W8 bounds the Stage 0 neutral trace tracePW(neutralProj·Tᵃ)/‖T‖ᵃ − 1 at a = 2w and max(3, 2w), and M1 and the trace use one release eigenbasis. W7 gives S_κ(n/2; n³) < 2⁻¹⁸ on the same cube and β. J² = −1 is used only on eigenspaces with r > 0. Every constant (k = ⌊n/2⁶⁹⌋, 2⁻¹²¹, 2⁻⁴⁹, 2⁻²², 2⁻⁸⁴, final 2⁻⁸⁴ + 7(2⁻²² + 2⁻⁸⁴) < 2⁻¹⁸) follows by hand from 4 ∣ n, 2⁷⁰ ≤ n and 512u ≤ n. Open: Stage 3's EV-L assembly, the seed itself.
