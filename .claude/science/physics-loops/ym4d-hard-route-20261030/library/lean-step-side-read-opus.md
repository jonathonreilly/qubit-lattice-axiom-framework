lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T01:31Z

# lean-step-side-read-opus: what in the SA YM4 Lean release needs block side 2^40, and where the floor H is chosen

Queue row 1464 (next row 2 of row 1460). Started 2026-11-24T13:31Z on Mac mini worker 3. Read only, no proof, no build.
Source: Sussman-Alpoge YM4 Lean release at `~/ym4d-papers/sa-ym4-lean-full`, commit 3932084a9b82 (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text).

## Plan

1. Confirm the release commit; find `IsUnitMeshStepParameters` and its side hypothesis (side_ge / side_gt / 2^40).
2. List every lemma in `YangMills/Construction/ClusterExpansionOfAStep` and `YangMills/Construction/TotalDensitiesGiveASystem` that reads the side hypothesis, with the inequality each needs; then their direct consumers.
3. Find where the coupling ceiling/floor H of the calibration is chosen, and how it relates to the side.
4. Decide (a) explicit floor H(L) and smallest admissible side, with numbers, or (b) side bound structural, no small-block step.

## Results (written step by step)

### Step 1. The hypotheses (release 3932084a9b82fc79466b4a2faad9ec032b637445, confirmed by `git rev-parse HEAD` in the read-only copy)

All paths below are relative to the release root.

- `YangMills/Construction/TotalDensitiesGiveASystem/TopStatementDefs.lean:12-18`, `structure IsUnitMeshStepParameters (ℓ : TorusLumps.StepParameters)`:
  `coupling_eq_one : ℓ.coupling = 1`; `side_odd : Odd ℓ.side`; `side_ge : 2 ^ 40 ≤ ℓ.side`; `one_le_baseDepth : 1 ≤ ℓ.baseDepth`; `side_gt : 11 * 2 ^ 12 * ℓ.baseDepth < ℓ.side`; `threshold_mem : ℓ.threshold ∈ Ioo 0 1`.
- `YangMills/Construction/ClusterExpansionOfAStep/LumpsOnATorus.lean:11-27`, `structure StepParameters`: fields `coupling, side, grid, baseDepth, threshold, κ, κ₁, rt, n₁, E, E₃, derivBound, n₀, y₁, B`. Note: `coupling` here is a lattice-unit (mesh) parameter, set to 1 by `coupling_eq_one`; it is not beta.
- `YangMills/Construction/ClusterExpansionOfAStep/EffectiveDensityOfAStep.lean:211-230`, `structure StepParameters.Admissible`: `a_ge : 1 ≤ coupling`, `L_odd`, `L_ge : 2 ^ 16 ≤ side`, `κ ≤ 1/8`, `depth_lt : 11 * 2 ^ 12 * baseDepth < side`, `n₀_ge : 4096 ≤ n₀`, `y₁_ge : 1 ≤ y₁`, `range_ge : 2 ^ 16 ≤ clusterRange y₁`, positivity of the rest.
- So the step-level cluster expansion asks only side >= 2^16 (plus side > 11*2^12*baseDepth = 45056*baseDepth). The 2^40 appears in the top-level structure. Step 2 finds who reads 2^40.

### Step 2. Where the side is chosen (the order of choice)

The parameter structure the step reads is `RenormalizationStepParameters.ParameterAssignment` (`YangMills/Construction/ClusterExpansionOfAStep/ParametersOfARenormalizationStep.lean:34-61`), with `Admissible` at lines 90-126. Its side clauses: `L_odd` (99), `L_ge : 2 ^ 40 ≤ T.side` (100), `L_gt : 11 * 2 ^ 12 * T.baseDepth < T.side` (101), `J₀_ge : 625 ≤ T.baseDepth` (98), `σ_L : 2 ^ 10 * side * (N 0 + 1) * threshold ≤ 1` (112), and `fits : ∀ y ≥ floorMin, (stepParameters y).Admissible` (126) with `floorMin = max yC 2^1600` (88). Also `n₁ = side^(1/640)` (65).

The existence statement is `ParametersCanBeChosen` (`ClusterExpansionOfAStep/ParametersExist.lean:7-21`): for every a >= 1 (mesh coupling), there are cK, κ, δ₁, J₀; for every eventual property P there is **L₀** such that every odd L >= L₀ admits an assignment with side = L. Proof: `parametersCanBeChosen_holds` (`ParametersCanBeChosenProof.lean:184-...`), from five hypotheses `ChainCoercivity`, `holeSavingStatement`, `ColdChainAtSmallCoordinates`, `AdmissibleParametersExist`, `ExistsCutoff`. Proved in the release as `step_parameters_exist` (`TheStatementsProvedTogether/FromMeansAtABondProof.lean:75`).

Order of choice in that proof (lines 188-290):
1. a given; cK and LK from `ChainCoercivity` (189); κ from `holeSavingStatement a` (190); δ₁, LA from `ColdChainAtSmallCoordinates a` (191); J₀ = max 625 (Jf1, Jf2) from the hole saving at Θ = 1 and 9/8 (192-203); LB1, LB2 from the hole saving at J₀ (204-205).
2. LC from the eventual property P (207).
3. **L₀ = max (max (max LK LA) (max LB1 LB2)) (max LC (max (2 ^ 40) (11 * 2 ^ 12 * J₀ + 1)))** (208). So 2^40 is one floor among six; LK, LA, LB1, LB2, LC are existential witnesses (no number at this point of the release).
4. Then, at the chosen L: the cold-chain constants (lam, ρA, σA, cg, N) from `hA L` (224), the cut δ₂ (231-), Ct, κ₀, rt <= min(κ₀, δ₂/2^14, ceilRate) (256), η₃, the threshold σ <= min(..., 1/(2^10 L (N0+1)), ...) (284). The threshold shrinks like 1/L.
5. The standard lump grid `standardLumpGrid L` needs only `2 ^ 16 ≤ L` (lines 23-51: lumps are intervals of length 16384 = 2^14 around a central interval [-8192, 8192]).

So within this proof the side is chosen **before** the threshold, n₀, Cs and the floor of the step coupling; those depend on L. Step 3 reads where the coupling floor is fixed.

### Step 3. The coupling floor of a step: existential, with an explicit lower bound in L

Definitions (`ClusterExpansionOfAStep/EffectiveDensityOfAStep.lean:14`): `clusterRange x = ⌈x ^ (1/100)⌉₊`. (`ParametersOfARenormalizationStep.lean:33`): `boxRadius x = clusterRange x / 2 ^ 11` (natural division).

- `FloorConditions (C c x)` (`ParametersOfARenormalizationStep.lean:127-154`) is a list of 16 inequalities in the step coupling x. Among them `radius_ge : 16 ≤ boxRadius x ∧ C ≤ boxRadius x` (131) and `range_ge : C ≤ clusterRange x` (138).
- `EventuallyFloorConditions` (`ClusterExpansionOfAStep/FloorsOfTheParameters.lean:7-9`): for every admissible T and every C, c > 0 there is y with FloorConditions C c x for all x >= y. Proof `eventuallyFloorConditions_holds` (`FloorsOfTheParametersProof.lean:580-594`): `filter_upwards` of 16 `eventually_*` lemmas, then `eventually_atTop.1`. **The floor y is an existential witness of a filter statement. The release computes no number for it.**
- The C the cell of the flow uses: `CellOfTheFlow/TheDrawsStandOnGroundsProof.lean:119-121`: `hCpos : 0 < 2 ^ 40 * Tb.side + 4 * Tb.n₀ + 2 ^ 17`, `obtain ⟨yF, hyF⟩ := hFl Tb hAdm _ 1 hCpos one_pos`; the floor is `max (max yD yG) (max yF (max Tb.floorMin 1))` (121), with yD, yG further existential floors (from `stageStateDensityStatement`, `HullStateIsHotCase`). The same C at `TheStepGivenItsStateIsTheGasProof.lean:299, 327` and `ExpansionReturnsAtDrawnParametersProof.lean:30, 58-63`. The floor applies to every stage coupling: `hon.le_coupling` (`TheDrawsStandOnGroundsProof.lean:131`), i.e. y <= (T.stage j).coupling.
- `floorMin = max yC 2^1600` (`ParametersOfARenormalizationStep.lean:88`), yC = max y₀ 1 with y₀ existential from the eventual property P (`ParametersCanBeChosenProof.lean:357-363`).
- The well-posed step also asks `range_ge_side : 2 ^ 40 * R.params.side ≤ R.range` (`ClusterExpansionOfAStep/AdmissionAtAStepForm.lean:12`; also `FactorsOfAStep.lean:122`), with R.range = clusterRange of the stage coupling (`MarkedIntegralsAreTheGasAtAStepProof.lean:442`, `RegularityOfTheImageProof.lean:59`).

**Explicit lower bound on the floor (read off, arithmetic by hand, PROVED from the cited clauses).** Let x be any stage coupling at which the cell of the flow runs, L the side. Then FloorConditions (2^40 L + 4 n₀ + 2^17) 1 x holds, so by `radius_ge`, C <= ⌈x^(1/100)⌉ / 2^11 (natural division), hence ⌈x^(1/100)⌉ >= 2^11 C and x^(1/100) > 2^11 C - 1 >= 2^51 L + 2^13 n₀ + 2^28 - 1. So

  **H(L) := floor of the step coupling >= (2^51 L)^100 = 2^5100 L^100,** and also >= 2^1600 (floorMin).

At the smallest side the release admits through this clause, L = 2^40 (n₀ >= 4096): x > (2^91)^100 = **2^9100 ≈ 10^2739**. This is a lower bound on the floor, not the floor: the floor itself is max(yD, yG, yF, yC, 2^1600, 1) with yD, yG, yF, yC existential. The inequality is linear in L inside the 100th root, so the floor grows at least like L^100.

Caveat on units: x is the stage `coupling` of the flow (`(T.stage j).coupling`), the same quantity `TotalDensityFlow.coupling ℓ β K` that `IsFirstPassageDatum` compares with g^(-2) (`TopStatementDefs.lean:20-34`). So x is an inverse squared coupling on the β scale (to be confirmed in Step 4 against the flow's initial value).

### Step 4. Where the calibration's coupling ceiling is chosen, relative to the side

- The flow: `TotalDensityFlow.flowData ℓ β 0 = (β, wilsonWeight β)`, each later level `(nextCoupling side x_k (kernelImage ℓ x_k D_k), kernelImage ℓ x_k D_k)` (`WindowOfTheParameters/FlowOfTheTotalDensities.lean:22-27`). So the stage coupling x_0 is the Wilson β itself; Step 3's caveat on units is settled.
- First passage: `passageThreshold B g = g^(-2) + B`; K is the first index with x_K <= g^(-2) + B (`WindowOfTheParameters/FirstPassageOfASequenceForm.lean:5-10`). Every stage before K has x_k > g^(-2) + B.
- The top statement `SystemFromTotalDensities := HoldsAtAdmissibleParameters FlowDataAtParameters` (`TotalDensitiesGiveASystem/TheTotalDensitiesGiveASystem.lean:20-29`). Its order of quantifiers: there are constraints D (incl. `sideFloor`, `FirstExitPathDefs.lean:12-33`); for every admissible T meeting D there is y₀; for every step floor y >= y₀ (with `T.floorMin ≤ y` and `(T.stepParameters y).Admissible`, line 21); for every Bs >= 2 T.B there are c₅, lam, **top**, and **for every g in (0, top], `y ≤ g ^ (-2 : ℤ)`** (line 23).
- `ForSmallCoupling P := ∃ y₂, ∀ g > 0, y₂ ≤ g^(-2) → P g` (`FirstExitPathDefs.lean:37-38`) is how each consumer statement (`TheFlowPasses.lean:8-12`, `TheCouplingsGiveTheWindow.lean:14`, `TheBoundsOnTheWindow.lean:28`, and 13 more files listed by `git grep ForSmallCoupling`) chooses the ceiling on g. y₂ is existential and is chosen **after** T (so after the side L), after the step floor y and after Bs.
- `FlowPassage` (`TopStatementDefs.lean:31-38`) runs with lam = (3/4) `oneLoopShift side` = (3/4) (11·4/(12π²)) log L (`TopStatementDefs.lean:19`, `SystemsWithFiveBounds/SystemWithFiveBounds.lean:46`; slope 11/(3π²) ≈ 0.3715). At L = 2^40 one step lowers the coupling by about 0.3715 · 27.73 ≈ 10.3 (lam ≈ 7.7 as the guaranteed rate).

**Consequence (PROVED by reading the cited lines, with Step 3's arithmetic).** The calibration ceiling top on g is chosen after the side, and every admissible g satisfies g^(-2) >= y, where y is the step floor of Step 3. So every coupling the release's flow visits, from β down to the first-passage level, is at least

  **g^(-2) >= y >= max(2^1600, (2^11 (2^40 L + 4 n₀ + 2^17) - 1)^100) > (2^51 L)^100,**

which at the smallest side, L = 2^40, is **more than 2^9100 (about 10^2739)**. The release's datum therefore lives entirely at β above 2^9100. The true floor and the true ceiling top are not numbers in the release: they are `max` of existential witnesses (yD, yG, yF, yC, y₀, y₂) from `eventually_atTop` and the eventual property P. The bound above is a valid lower bound on them, not their value.

### Step 5. Inventory, `YangMills/Construction/ClusterExpansionOfAStep` (all paths in this step relative to that folder)

Method: a script (`inv.py`, kept in a scratch folder, not committed) lists every line matching `side_ge|side_gt|L_ge|L_gt|depth_lt|2 ^ 40|hL40|range_ge_side` with its enclosing declaration: 232 lines, 150 declarations over both folders. I read the binding ones in full. Three different hypotheses carry the name `L_ge`/`side_ge` and must not be confused:

- (S16) `StepParameters.Admissible.L_ge : 2 ^ 16 ≤ side` (`EffectiveDensityOfAStep.lean:214`), reached as `hfit.L_ge`, `hadm.L_ge`, `hR.admissible.L_ge`, `P.admissible.L_ge`, `hb.sizes.admissible.L_ge`, `hp.L_ge`. Also `KeptPartData.side_ge : 2 ^ 16 ≤ L` (`GeometryOfAKeptPart.lean:44`) and `ClassSumHypotheses.side_ge : 80 ≤ ℓ.side` (`SumOfAClassAtAStep.lean:14`), both filled from (S16).
- (S40) `ParameterAssignment.Admissible.L_ge : 2 ^ 40 ≤ T.side` (`ParametersOfARenormalizationStep.lean:100`), reached as `hT.L_ge`, `hD.L_ge`, `hDr.L_ge`, `hAdm.L_ge`, `hadm.L_ge` on a ParameterAssignment; and `IsUnitMeshStepParameters.side_ge` (`TopStatementDefs.lean:15`).
- (R40) `range_ge_side : 2 ^ 40 * side ≤ range` (`AdmissionAtAStepForm.lean:12`, `FactorsOfAStep.lean:122`), range = clusterRange(coupling) = ⌈x^(1/100)⌉. **This is a floor on the coupling x, not on the side:** x > (2^40 L - 1)^100.

**(a) Uses of (S16) or of the depth clause (`depth_lt`, `L_gt`: 11·2^12·J₀ < side).** Every other matched declaration. What each needs, by the pattern of the line:
- positivity only (0 < side, 1 <= side, 2 <= side; the `have := hfit.L_ge; omega` pattern): `AZeroFactorKillsTheStateProof.lean:86` coarseWeight_zero_of_factor_zero; `AdmissionAtAStepProof.lean:60, 348`; `BasesExistProof.lean:189`; `DensitiesAlongMoves.lean:52` side_pos; `FactorsAtACaseProof.lean:461`; `FactorsOfACaseAtAStepProof.lean:291`; `FormOfTheSharesProof.lean:110`; `GaugeCarriesTheKernelProofForm.lean:88`; `LumpsAreFibres.lean:137, 217, 318, 328, 359`; `MatchingClasses.lean:135, 146`; `PriceOfAClassBeforeItsLengthProof.lean:224`; `SharesOfHoledFieldsForgetProofForm.lean:101`; `TheKernelIsPlainFarFromLumpsProof.lean:95`; `TopFieldOffTheHull.lean:149`; `WilsonWeightHasTheExpansionProof.lean:360`; `ImageStateKeepsTheGaugeProof.lean:621`.
- lump geometry, side >= 2^16 (the lump grid of intervals of length 2^14 = 16384 around a central interval [-8192, 8192], `ParametersCanBeChosenProof.lean:13-51`, `standardLumpGrid L (hL : 2 ^ 16 ≤ L)`): `AllowedStatesReadTheirBoxProof.lean:1127, 1360, 1805-1819` (exists_offset_near, exists_hot_meets, sameNearbyLumps: `(side-1)/2` as a centre offset), `BlocksReadTheirBoxesProof.lean:1474-1476` blockDataIsLocal (2^16 and the depth clause), `ClassesOfAStepAreCountedProof.lean:467`, `ClustersOfAStepProof.lean:18`, `DoubleRatiosOfASettingProof.lean:1239`, `EnergyNearAClassProof.lean:1096, 2081, 3164, 3201, 3379, 4475`, `GeometryOfFreeBonds.lean:101`, `GeometryOfAKeptPart.lean:44-224` (div_side_add_one_le_div), `LengthOfAnImageUnionProofForm.lean:193, 411`, `LocalityOfTheKernelProof.lean:983` bondKernelLocality, `PriceOfAClassBeforeItsLengthProof.lean:255, 457, 634`, `RegionsOfASettingProof.lean:211`, `SettingWithAClassProofForm.lean:518`, `SettingsOfASharedGasProof.lean:665`, `TopFieldOffTheHull.lean:301`, `HotGroundIsOfItsStateProof.lean:85`, `InnerSupportsWithTheirCoresProof.lean:604`, `FourCornersProof.lean:622`, `FactorsOfAnAttachedUnionProof.lean:255, 277`, `SumOfAClassAtAStepProof.lean:106-111` (only 80 <= side), `WilsonWeightHasTheExpansionProof.lean:1030` (2^16·4096 <= side·n₀), `ThreeFactsOfAnExpansionProof.lean:76`, `TheImageIsGaugeInvariantProofForm.lean:277`, `OneCouplingAtGivenParametersProof.lean:164, 173`, `AdmissionEqualInBoxes.lean:62`.
- base depth (`depth_lt`/`L_gt`, side > 45056 J₀ with J₀ >= 625, so side > 2.8·10^7 ≈ 2^24.7): `AllowedStatesReadTheirBoxProof.lean:1867, 1963, 1996` (kernelLocal), `BlocksReadTheirBoxesProof.lean:1476`, `CostsOfTwoSettingsProof.lean:470`, `DoubleDifferenceOfFourSettingsProof.lean:313`, `OffNearDensitiesMoveLittleProof.lean:528`, `FlowWhereTheExpansionReturnsProof.lean:112`. This clause is the strongest *geometric* one: the base choice reaches depth J₀ inside a block, and J₀ >= 625 is fixed (`ParametersOfARenormalizationStep.lean:98`; J₀ = max 625 (Jf1, Jf2), `ParametersCanBeChosenProof.lean:194`, with Jf1, Jf2 existential from the hole-saving statement).

**(b) Uses of (S40) itself, with the inequality each needs (PROVED by reading, arithmetic by hand).**
1. `GradientsOfTwoSettingsProof.lean:527-530` `pow_mul_le_mul_sub_of_large`: from 2^40 <= L and j >= 4, 2^32 j <= L j - 2 L. **Needs L(j-2) >= 2^32 j for all j >= 4, i.e. L >= 2^33.** Consumed at 585-590 (potentialPart_locallyClose): converts the fine-scale rate `decayRate = rt / 2^12` over distance L j - 2L into the coarse rate 2^20 rt per block: (rt/2^12)(Lj - 2L) >= 2^20 rt j. **This is the binding use. It is a choice of rate bookkeeping, not geometry**: the coarse rate 2^20 rt is fixed by `pow_mul_rt_le_δ₁` (531-534: 2^20 rt <= δ₁, from rt <= δc/2^14 and δc <= δ₁/2^6). With the coarse rate c·rt in place of 2^20 rt, the same lemma needs L >= 2^13 c (at j = 4).
2. `GradientsOfTwoSettingsProof.lean:523-526` `le_mul_sub_sub_of_large`: j <= L j - L - 2^16 for j >= 4. Needs 3L >= 2^16 + 4, i.e. L >= 21847 ≈ 2^14.4. Consumed at 550 (blockCost_locallyClose).
3. `GradientsOfTwoSettingsProof.lean:755-758` (settingGradientsClose_of): 2^40 <= side only for 0 < side; and **line 775: the floor of this lemma is `max T.floorMin (max y₁ (max y₂ (max y₃ ((2 ^ 14 * T.side) ^ 100))))`** — a second explicit L^100 coupling floor, weaker than Step 3's.
4. `CostsOfTwoSettingsProof.lean:471-473` (blockCostsAgree_holds): `hL40` is put in context and read only by later `omega` calls (`fieldsAgreeNear_of_settings ... (by omega)`, 480). The bound it supplies is not isolated by the proof; the omega goals are linear in side, k, m, so a side of order 2^16-2^20 very likely suffices (GUESS, not checked).
5. `DeepDensitiesAgainstTheCutProof.lean:524-525, 921` (deepActivityIgnoresCutoff): range/(32 L) <= range/2^18, **needs L >= 2^13**.
6. `LocalityOfTheDensitiesProof.lean:256-279, 653` (densityLocality_holds): uses only 2^15 <= side.
7. `TwoSystemsOfTheGasProof.lean:275-290` `range_ceil_le`: needs r/(4L) <= (m₀+1)/4 from r < 2^11 (m₀+1), i.e. **L >= 2^9**.
8. `DoubleRatiosOfASettingProof.lean:1195`, `ExpansionsOfTheDensitiesOfASettingProof.lean:145`, `SumOfTheDensitiesNearAClassProof.lean:305`, `FloorsOfTheParametersProof.lean:287` (n₁_pos), `ParametersAgreeWithTheSumProof.lean:23, 36` (fills a downstream `side_ge` with it), `DoubleDifferenceOfFourSettingsProof.lean:317`: `have := hT.L_ge` then `omega`/`positivity`; positivity or small linear bounds (GUESS for the omega ones, by the pattern).
9. `ParametersCanBeChosenProof.lean:208-220, 386-387`: the producer (Step 2).

**(c) Uses of (R40), the coupling floor.** `AdmissionAtAStepProof.lean:46, 218`; `AdmissionEqualInBoxes.lean:70`; `AdmissionIsAProductProof.lean:39-66`; `AdmissionReadsVOnItsHullProof.lean:386-440` (frameReach_add_le_half, bondMark_eq_of_near: 2^40·2^16 <= 2^40·side <= range); `DensitiesOfTheImageProof.lean:275-279`; `FactorOfAClassIsOneRuleProof.lean:234-257, 545` (four_mul_side_le_interactionRadius: 4 side <= interaction radius); `FactorsAtACaseProof.lean:246`; `FactorsOfACaseAtAStepProof.lean:111`; `GasDensityOfAGroundIsBorelProof.lean:1619-1623`; `HullStatesAreGroundsProof.lean:102, 387`; `ImageFactorIsBorelProof.lean:337-341`; `ImageStateIsBorelProof.lean:488`; `ImageStateKeepsTheGaugeProof.lean:247, 575`; `ImageStateKeepsTranslationsProof.lean:902-905` (16·2^11 <= 2^40 side); `ZetaOfAGroundIsBorelProof.lean:899-977` (64 side + 2^16 <= 2^40 side). Producers: `FactorsOfAFamilyProof.lean:573-677`, `MarkedIntegralsAreTheGasAtAStepProof.lean:409-442`, `MarkedIntegralsAreTheGasProof.lean:501-533`, `RegularityOfTheImageProof.lean:19-59`, `ExpansionReturnsAtDrawnParametersProof.lean:30-68`: each takes a floor y from `EventuallyFloorConditions` with C = 2^40 side + 4 n₀ + 2^16 (or 2^17), then reads `range_ge` to get 2^40 side <= clusterRange. What the consumers need: the cluster range is a large multiple of the side (64 side + 2^16, 4 side, 16·2^11 are the explicit ones read). **So the factor 2^40 in (R40) is also bookkeeping; the consumers listed need range >= about 64 side + 2^16.**

**Verdict for this folder.** No step lemma needs side >= 2^40. The largest isolated need is L >= 2^33 (item b1, a rate conversion). Lump geometry needs 2^16; the base-depth clause needs side > 45056 J₀ >= 2.8·10^7. The step's coupling floor is x > (2^40 L)^100 through (R40) and (2^51 L)^100 through `radius_ge` (Step 3), so it rises as L^100.

