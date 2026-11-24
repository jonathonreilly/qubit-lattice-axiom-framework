lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T02:36Z

# Row 1470: sizing the weak-coupling floor for a K-II tool by step certificates

Started 2026-11-24T14:36Z (date -u), Mac mini worker 2, Claude Opus 5.5 high. Read only, no new proof.
Pinned at commit 95f65cd6f on claude/ym4d-hard-route.

Question (row 1468 Section 8 row 2, queue row 1470): at what inverse coupling X does a weak-coupling
block step with explicit constants close, for block side 2 or 3, or 2^m built by iterating a small map?
Outcome (a): X <= 100 with the clause list (order-one part <= ~400 steps, proof-design row justified);
outcome (b): X >= 1e4 or a structural reason (K-II by step certificates closed by count).

## Plan

1. Read FINISH rows 1464, 1467 (if landed), 1468; library/lean-step-side-read-opus.md Steps 3-6; row 1468 output.
2. Read the floor clauses in the Sussman-Alpoge YM4 Lean release (~/ym4d-papers/sa-ym4-lean-full, read only).
3. Read Balaban's small-field / large-field conditions (library/lit-balaban.md; CMP 109, 116, 119, 122 in ~/ym4d-papers).
4. Table: each binding clause, its floor as written, smallest x if the 1/100 exponent and constants are re-chosen,
   structural or bookkeeping, label proved / read / guessed, file:line.
5. Verdict (a) or (b).

## Step 1. Inputs read (14:40Z)

- Row 1464 (`library/lean-step-side-read-opus.md`, author only, unchecked; check 1467 has not landed: no file
  `library/lean-step-side-read-check-astra62.md` at 95f65cd6f). Its ledger of floor clauses (READ there, not re-read yet):
  `FloorConditions (C c x)` at `ParametersOfARenormalizationStep.lean:127-154` (16 inequalities), `radius_ge` (131),
  `range_ge` (138), `floorMin = max yC 2^1600` (88), `clusterRange x = ceil(x^(1/100))`
  (`EffectiveDensityOfAStep.lean:14`), `boxRadius x = clusterRange x / 2^11` (33), the C used by the flow
  C = 2^40 L + 4 n0 + 2^17 (`ExpansionReturnsAtDrawnParametersProof.lean:30`), the second floor (2^14 L)^100
  (`GradientsOfTwoSettingsProof.lean:775`), (R40) `range_ge_side` (`AdmissionAtAStepForm.lean:12`).
  Its bound: every admissible g has g^-2 > (2^51 L)^100 and >= 2^1600.
- Row 1468 (`library/gap-k2-tool-design-fable.md` 5.1, 8): map Q2 (side 2, contour mean, vMF kernel strength a x);
  one-loop drift per side-2 step 0.2575 (SKETCHED there); order-one part step count ~ 3.88 (X - 2.3);
  X = 30-100 GUESSED as the best case for a small-field expansion with computed constants (5.1).

What this row must add: re-read the 16 clauses of FloorConditions (which bind, with what C), classify each as
structural or bookkeeping, then do the same for Balaban's small-field conditions, and give the smallest x for
each clause when exponents and constants are re-chosen.

## Step 2. The release's floor clauses, re-read (Sussman-Alpoge YM4 Lean, 3932084a9b82, read only)

Paths relative to `YangMills/Construction/ClusterExpansionOfAStep/` of the release unless stated.
`FloorConditions (C c x)` is at `ParametersOfARenormalizationStep.lean:127-154`; the flow uses it with
C = 2^40 L + 4 n0 + 2^17 and c = 1 (row 1464 Step 3, `ExpansionReturnsAtDrawnParametersProof.lean:30`), at every
stage coupling x >= y, and every admissible g has g^-2 >= y (row 1464 Step 6).

### 2.1 A clause that binds far above row 1464's bound (PROVED from the definitions; hand arithmetic; new)

Definitions read:
- `stable_nearby : 200 * T.B <= x ∧ ...` (`ParametersOfARenormalizationStep.lean:145`), and
  `sqrt_bounds : C (1 + E) + 1 <= sqrt(x lam/4) ∧ 1 + E₃ <= sqrt x` (:132), with E = 4 B, E₃ = E/η₃, η₃ <= 1 (:66-68, :106).
- `B = expansionConstant Cs (maxOfFirstFour N) rt n₁` (:66), `n₁ = side^(1/640)` (:63).
- `expansionConstant Cs Na rt n₁ = weightGrowthSup rt n₁ * (2 Cs + baseConstant Cs rt * Na) + baseConstant Cs rt`,
  `baseConstant Cs rt = Cs * potentialDecaySum rt + 1` (`NumbersOfTheStep.lean:28-30`).
- `weightGrowthSup rt n₁ = ⨆ m, expansionWeight rt n₁ m * exp(-2 (rt/2^10) m)` and
  `expansionWeight rt n₁ m = max 1 ((m/n₁)^16000) * exp(rt/2^10 * m)` (`NumbersOfTheStep.lean:17-18, 25-26`).
  So weightGrowthSup = sup over m of max(1, (m/n₁)^16000) e^(-r m), r = rt/2^10.
- Rate chain: `rt_le : rt <= δc/2^14`, `δc_le : δc <= δ₁/2^6` (:104-106), and δ₁ <= 1/8 from `chain :
  ColdChainConstants` (`ConstantsOfTheColdChain.lean:10`, first clauses `0 < δ ∧ δ ≤ 1/8`). So r <= 2^-33.

Bound. Take m = 2^47. Then r m <= 2^14, so weightGrowthSup >= (2^47/n₁)^16000 e^(-16384)
= 2^(752000) L^(-25) 2^(-23637.6) > 2^728362 L^-25 (n₁^16000 = L^(16000/640) = L^25; the sup is finite since r > 0,
so it dominates each term). With baseConstant >= 1 (Cs > 0, potentialDecaySum a tsum of non-negative terms) and
maxOfFirstFour N >= N 0 > 0:

  B >= (2 Cs + N 0) 2^728362 L^-25,   and the step floor obeys   x >= (1 + E₃)^2 > E^2 = 16 B^2.

At L = 2^40 (L^25 = 2^1000): **x > 16 (2 Cs + N 0)^2 2^1454724**. The release puts no lower bound on Cs or N 0 beyond
positivity (`Cs_pos`, `ColdChainConstants` N j > 0), so as a number this is conditional on 2 Cs + N 0 not being below
2^-700000; both are bound constants of the cold chain and the expansion (they bound quantities of order one or larger),
so this proviso is GUESSED harmless. Unconditionally the clause gives only x >= 200 (from `B_ge : 1 <= B`, :116).
Row 1464's bound (2^51 L)^100 = 2^9100 stays valid and unconditional; this one is larger by a factor about 2^1445000
under the proviso. Grep: `weightGrowthSup`, `16000`, `stable_nearby` in `library/open-core.md`, `FINISH.md` and
`library/*.md`: see Step 6 (repo search).

What makes it large, and whether it is structural:
- the polynomial weight degree 16000 in `expansionWeight`: BOOKKEEPING. Summing a polynomial-times-exponential
  weight over pairs of bonds in Z^4 needs a degree above about 8 (8 coordinates of a pair); 16000 is a choice.
- the rate dilution rt <= δ₁/2^20 and r = rt/2^10 (three factors 2^6, 2^14, 2^10): BOOKKEEPING (fixed margins
  between rates, cf. row 1464 Step 5 b1 for 2^20 and 2^12).
- the form "x >= const * B" and "sqrt x >= 1 + E₃" (coupling must beat the expansion constant): STRUCTURAL in form.
  Any expansion in g = x^(-1/2) needs g times its combinatorial constant to be small. Its size is not fixed by the form.

