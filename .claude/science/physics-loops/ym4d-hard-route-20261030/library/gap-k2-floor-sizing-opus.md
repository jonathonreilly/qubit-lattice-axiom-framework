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

## Step 3. Balaban's small-field and large-field conditions (read in ~/ym4d-papers OCR text; formulas checked only where the OCR is legible)

- CMP 109 (249), p. 259, Theorem 1 (OCR `cmp109.txt` L555-566): "If the sequence of the effective coupling constants
  is contained in an interval ]0, γ] with a sufficiently small positive γ, then the effective actions for small fields are
  given by (0.22)-(0.24)". Small-field domain: |∂U_k(V) - 1| < ε0 η^2 "for ε0 sufficiently small" (L558-560). Theorem 2
  (p. 259, L582-590): "γ a sufficiently small positive constant", proof by perturbative calculation announced, not
  published (as on file, `library/lit-balaban.md` L147). READ: no number for γ or ε0.
- CMP 122 (175), p. 175 (OCR `cmp122a.txt` L18-30): a large plaquette is one with |U(∂p) - 1| >= g0 p0(g0),
  p0(g) = A0 (log g^-2)^p0 with a positive integer p0; its Wilson weight is at most exp(-p0(g0)^2)-type. Balaban:
  "For d = 4 ... the bound does not give any positive power of ε. It is still small for ε small, and it controls a
  large number of steps, but this number is a small fraction of the total number of steps." READ.
- CMP 122 (175), p. 185 (OCR L512-517): "The quotient on the right-hand side ... is a negative power of log g_j^-2,
  hence the coefficient at δ_j can be arbitrarily small, also after multiplying it by O(1)L from (1.37), if γ is
  sufficiently small." p. 185-186 (L569-578): M chosen large, γ or A1/A0 small; "the conditions on M, γ, A0 and A1
  ... do not depend on any scale". READ: every condition is existential (L large, M large, γ small, A1/A0 small).

Floor clauses of Balaban's scheme and their kind:

| Clause (Balaban) | Form | Kind | Smallest x if constants re-chosen |
|---|---|---|---|
| (B1) small-field analyticity, ε0 small (CMP 109 p. 259) | the expansion of the small-field action converges for |∂U-1| < ε0 | STRUCTURAL (any small-field expansion) | none by itself: ε0 is a fixed number, a field cut, not a coupling floor |
| (B2) large-field cut g p(g) with p(g) = A0 (log g^-2)^p0 (CMP 122 p. 175) | the cut must be below ε0 and the suppression exp(-p(g)^2) must beat the polymer entropy of the large-field regions | STRUCTURAL in form (a cut between the typical field g and ε0); the log power is Balaban's choice | x >= (A0^2 (log x)^(2 p0)) / ε0^2 and A0^2 (log x)^(2p0) >= entropy; GUESS, no constant on file |
| (B3) coefficients "a negative power of log g^-2" times O(1) L (CMP 122 p. 185) | K L (log x)^(-q) <= 1/2 | STRUCTURAL to Balaban's d = 4 large-field renormalization (his own words at p. 175: in d = 4 the suppression gives no positive power of the cutoff) | x >= exp((2 K L)^(1/q)); exponential in the constants. With K L >= 10 and q = 1 this is >= e^20 = 4.9e8. GUESS (K, q not read as numbers) |
| (B4) γ small for the effective couplings (CMP 109 Theorem 1) | union of all of the above | existential | none on file |

What this gives (READ, with the one structural inference marked): Balaban's scheme states no number. Its d = 4
large-field step (B3) makes some small parameters only inverse powers of log g^-2, so its floor in x is
exponential in its constants; this is a structural property of his large-field renormalization in d = 4 (his
p. 175), not of every small-field expansion. A rebuilt step that avoided (B3) would need a different
large-field mechanism; none is on file.

## Step 4. The sixteen clauses of `FloorConditions`, one by one (release, read only)

Notation: R = clusterRange x = ceil(x^(1/100)), boxR = R/2^11 (natural division); flow values C = 2^40 L + 4 n0 + 2^17,
c = 1; rt <= 2^-23 (Step 2.1). "Release floor" is the lower bound on x the clause forces at the release's choices
(L = 2^40 where L enters); the logarithms were solved in floating point (`python3 -I -c`, GUIDE for the digits; the
inequalities themselves are PROVED by hand from the clause). "Re-chosen" means: R chosen freely (not tied to x),
C cut to what the consumers read (row 1464 Step 5(c): range about 64 L + 2^16), polynomial degrees and rate margins
set to order one. Kind: S = structural in form (any small-field expansion has a clause of this form), B = bookkeeping
(comes from tying R to x, from C doubling as an exponent, or from fixed margins).

| # | Clause (line in `ParametersOfARenormalizationStep.lean`) | Release floor | What drives it | Kind | Re-chosen floor |
|---|---|---|---|---|---|
| 1 | coupling_le 2/a <= x (128) | x >= 2 | mesh coupling a = 1 | trivial | 2 |
| 2 | drift_le C(1+E₃) + x^C e^(-cR) <= x lam/16 (129) | (i) x >= 16 C (1+E₃)/lam, with E₃ >= 4B (huge, 2.1); (ii) R >= C ln x - ln(x lam/16): x ~ 2^9265 at L = 2^40 | (i) error vs the coercive scale x lam (lam is the cold-chain constant of `ColdChainConstants`, not the one-loop shift; role READ from the definition only); (ii) C as an exponent | (i) S, (ii) B | (i) x >= 16 K/lam_cold, K the error constant of the step; no number on file |
| 3 | sqrt_bounds (130-131) | x >= (1+E₃)^2 > 16 B^2 > 2^1454728 (2 Cs + N0)^2 L^-50 (2.1) | B, via degree 16000 and r <= 2^-33 | form S (g K <= 1), size B | x >= K_exp^2, K_exp the expansion constant; no number on file |
| 4 | radius_ge 16 <= boxR, C <= boxR (131) | 16 alone: x > (2^15 - 1)^100 ~ 2^1500 at every side; with C: x > (2^51 L)^100 (row 1464) | R tied to x by the exponent 1/100, factor 2^11 | B | none (R free) |
| 5-8 | cold_tail, rate_tail, square_tail, root_tail (132-137) | conditions on boxR against x^2, threshold; met once R is large | decay e^(-δc boxR/4) beats prefactors | S as conditions on R; B as x-floors | none on x; they force R >= (k/δ) ln(x/σ) |
| 9 | weight_tail for n <= C (138-139) | x >= (2^5 C weight(C)/E)^2; with weight(C) ~ (C/n₁)^16000: of order 2^(1.1e6) at L = 2^40 (GUIDE) | degree 16000, C as a range of n | B | x >= (32 C w(C)/E)^2 with order-one degree: polynomial in C; no number on file |
| 10 | range_ge C <= R (140) | x > (2^40 L)^100 | R tied to x | B | none |
| 11 | stretched_tail (141-142) | R >= C ln x + x^(1/200) | R tied to x | B | none |
| 12 | log_powers (143-145) | C ln x <= x^(1/50) (using R^8 ~ x^(8/100)): x ~ 2^4582 at L = 2^40; and x^(5/6) >= 1/gasRate | R^8, R^12 (volume of a pair of range boxes) against a power of x | S in form (a volume of the range against a power of x); exponents 1/10, 1/6 B | with R = (k/δ) ln x forced by 5-8: x^a >= C (k/δ)^8 (ln x)^9; with a = 1/10, k/δ = 10, C = 1 this is ln x ~ 1170, x ~ e^1170 (GUESS: a, k/δ are not read as numbers for a rebuilt step) |
| 13 | stable_nearby 200 B <= x (146-148) | x >= 200 B > 2^728369 (2 Cs + N0) L^-25 (2.1) | B | form S, size B | x >= 200 K_exp |
| 14 | error_sum (149-152) | x >= (C/min(1, E/64))^2 and R-terms | C, R | form S | x >= K^2 |
| 15 | gas_powers (153-156) | x^(89/90) >= 1/gasRate and gasRate x/4 >= C ln x + max_n [16000 ln(1+n/n₁) - rt n/2^10]; gasRate <= 2^-31 L^-2 (σ_L, κ <= 1/8): x ~ 2^206 at L = 2^40 | large-field (hot) suppression e^(-gasRate x) with gasRate ~ κ σ^2, σ the hot threshold; σ <= 2^-10/L (σ_L, 112) | S (large field vs entropy); the 1/L in σ and the 2^-8 B | x κ σ^2 >= 4 (entropy + ln of prefactors): with κ = 1/2 (SU(2): 1 - Re U = abs(U-1)^2/2), σ = 1/2 to 1, entropy about 5: x >= 40 to 160 (GUESS) |
| 16 | chain_tail (157-161) | first term alone: 4 e^(-(15/16)(rt/32) m) <= e^(-rt m/2^12) at m = ceil((R-1)/64) needs rt m >= 47.72, so R > 64 (47.72/rt - 1) + 1 >= 3054 * 2^23: **x > 2^3457 at every side** | rt <= 2^-23 with R tied to x | B | none (R free) |

New unconditional number (PROVED by hand from clause 16 and rt <= 2^-23; float only for 47.72 = ln 4/(15/512 - 1/4096),
which is exact to the digits shown): at every side, every admissible parameter set, the step floor exceeds 2^3457.
This raises row 1464 Step 8 item 4 ("at any side above 2^2800") to 2^3457. Under the proviso of 2.1 on Cs, N0,
clauses 3 and 13 give 2^1454728 L^-50 (2 Cs + N0)^2 and 2^728369 L^-25 (2 Cs + N0), far larger.

Tally. Of the sixteen, the ones that set the release's floor (3, 13, 9, 2(ii), 4, 10, 16, 12) are all B as
x-floors: they come from (i) tying the range R to x by R = x^(1/100), (ii) the degree 16000 and the rate dilution
2^-33, (iii) C = 2^40 L + ... used as an exponent. Removing them leaves clauses of four structural forms:
(F1) x >= K_exp^2 or 200 K_exp (2, 3, 13, 14): the coupling beats the expansion constant;
(F2) x κ σ^2 >= entropy (15): large-field suppression;
(F3) x^a >= C R^8 polylog with R >= (k/δ) ln x (12 with 5-8): the volume of the range against a power of x;
(F4) conditions on R alone (4-11, 16): no x-floor.
None of K_exp, lam_cold, δ, a, σ is a number anywhere in the release (all existential: row 1464 Steps 2-4).

## Step 5. Best-case floors of the structural forms at block side 2 or 3 (all GUESSED; no constant below is computed anywhere on file)

Normalization: x = β, Wilson weight exp(-x (1 - Re U_p)) per plaquette, U_p a unit quaternion, so
1 - Re U = abs(U - 1)^2/2 (exact for unit quaternions). A side-2 block in d = 4 has 16 sites, 64 links and
96 plaquettes (6 planes x 16); it has 80 neighbours in the star (3^4 - 1) and 8 nearest neighbours.

- **(F2) large field.** A block is large if one of its plaquettes has abs(U - 1) >= σ. Probability per plaquette
  at most about e^(-x σ^2/2) (Haar factor ignored, GUIDE). A polymer bound with star-connected animals needs
  96 e^(-x σ^2/2) e μ <= 1 with μ <= e 80: x σ^2/2 >= ln(96 e^2 80) ~ 10.9, so x >= 21.8/σ^2: 22 at σ = 1,
  87 at σ = 1/2, 349 at σ = 1/4. σ must lie inside the domain where the small-field expansion is analytic with
  its explicit constants (Balaban's ε0 "sufficiently small", Step 3 (B1)); no value of ε0 is on file.
- **(F1) coupling against the expansion constant.** With the Kotecky-Preiss criterion on block animals, an
  activity per block z needs z e μ <= 1 roughly. If the first-order terms are removed (the local O(g^2) part
  extracted into the running coupling, z = c₁/x): x >= e μ c₁, between 54 c₁ (nearest-neighbour animals,
  μ ~ 20) and 590 c₁ (star animals). If a term of order g = 2/sqrt(x) survives in the norm (sup bounds on the
  small-field region give x σ^3-type terms, as in Balaban's p(g)-weighted norms): x >= (2 e μ c₁)^2, between
  1.2e4 c₁^2 and 1.4e6 c₁^2. c₁ is the per-block constant of the remainder; no value is on file, and a block holds
  96 plaquettes.
- **(DR) drift against error** (row 1468 (K2-STEP)): the one-loop drift of a step is 0.2575 at side 2 and 0.408 at
  side 3 ((11/(3 π^2)) ln b, row 1468 4.4, SKETCHED there for Q2). A readout error bounded by K/x needs
  x >= K/(drift/2) = 7.8 K (side 2), 4.9 K (side 3). K not on file.
- **Iterating a small map versus one block of side 2^m.** A 2^m block built from m steps of Q2 has the side-2
  floor (each step must close in the band). One step of side L = 2^m pays the release's σ_L clause
  (`ParametersOfARenormalizationStep.lean:112`, σ <= 2^-10/(L (N0+1))), structural in form (a fine cut must
  keep the coarse defect, a sum over the block, small): (F2) becomes x >= 21.8 L^2/σ_c^2 with σ_c the coarse
  cut. So iterating side 2 is the better choice, and the side-2 numbers above are the relevant ones.

Count (row 1468 5.1, GUIDE): the order-one part has 3.88 (X - 2.3) side-2 steps, so outcome (a)'s 400 steps is
X <= 105. The best cases above straddle that line: (F2) alone needs σ >= 0.46 inside an analytic domain with
explicit constants; (F1) needs c₁ <= 2 with first-order terms removed, or is above 1e4 if they are not. No row and
no source on file supplies any of σ, c₁, K, μ for a rebuilt small-side step.

## Step 6. Repo search (grep of `library/open-core.md`, `FINISH.md`, `QUEUE_DONE.md`, `library/*.md`)

`weightGrowthSup`, `chain_tail`, `stable_nearby`, `expansionConstant`, `728362`: no match. `x_pert`, "floor of
human size": only row 1468 (`library/gap-k2-tool-design-fable.md` 5.1, the GUESS 30-100 this row tests).
"explicit constants" in FINISH: rows on CMP 98 walk expansions (b98p5), IN1, Langevin gap at β < 1/4; none sizes a
weak-coupling coupling floor. Row 1418 (`library/gap-rg-step-sizing-astra62.md`) sizes an order-one tensor step,
not a weak floor. So the numbers of Steps 2.1 and 4 (2^3457 at every side; the B-clauses) are new as far as this
grep shows; they refine row 1464 (Step 8 item 4: "above 2^2800 at any side").

## Step 7. Verdict

**Outcome (b), on the record.** Labels: PROVED (hand, from cited clauses), READ, GUESSED.

1. Release (Sussman-Alpoge YM4 Lean 3932084a9b82). Every explicit floor is far above 1e4. PROVED, unconditional,
   at every side and every admissible parameter set: x > 2^3457 (clause chain_tail with rt <= 2^-23, Step 4 row 16).
   At L = 2^40: x > 2^9100 (row 1464) and about 2^9265 (drift_le (ii), GUIDE digits). PROVED given 2 Cs + N0 not
   astronomically small (GUESSED harmless): x > 2^1454728 (2 Cs + N0)^2 L^-50 (sqrt_bounds with weightGrowthSup,
   Step 2.1). All of these are BOOKKEEPING as x-floors (R = x^(1/100), degree 16000, rate dilution 2^-33, C as an
   exponent). If those are chosen again, what is left is four structural forms (F1)-(F4) whose constants the
   release does not name (all existential).
2. Balaban (CMP 109 p. 259, CMP 122 pp. 175, 185). READ: no number; γ, ε0, M, L, A1/A0 are existential. His d = 4
   large-field renormalization makes some small parameters inverse powers of log g^-2 (p. 185), so his floor is
   exponential in his constants: structural to his method (his p. 175 explains why), not shown necessary for every
   method.
3. Re-chosen, side 2 or 3 (Step 5). GUESSED best cases straddle the (a) line X <= 105: (F2) 22-349 by the cut σ,
   (F1) 54 c₁ to 590 c₁ if first-order terms are removed, 1.2e4 c₁^2 and up if not, (DR) 7.8 K. Nothing on file
   fixes σ, c₁, K. So (a) cannot be met: there is no list of clauses with numbers giving X <= 100, only guesses
   that reach 100 under the most favourable unproved assumptions.
4. Hence, per the row's decision rule, **a K-II tool by step certificates is closed on the record by count**: the
   only weak-coupling step with stated clauses has its floor above 2^3457 (2^3457 is about 10^1040, so about 10^1040
   side-2 steps below it would need certificates), and no explicit-constant step at small side exists to lower it. The band
   stays stopped under row 1442 with its triggers.
5. Reopen trigger (proposed, for the lead): a small-field step at side 2 or 3 with explicit constants, i.e. numbers
   for the analyticity cut σ (or Balaban's ε0), the per-block remainder constant c₁ and the readout error K, with
   (F1), (F2), (DR) giving X <= 105. That is a hand analysis (T1 of row 1468), not a computation. Independent of X,
   row 1468 5.3 puts the smallest piece of one order-one step on file at 1e5 to 1e6 Lean rows (unchecked; the
   smallest piece on file, not a proved lower bound), so even X = 100 (about 380 steps) would not make step
   certificates feasible without a new representation.

What this row does not show: the true floor of the release (existential); the role of each clause in its proof
beyond the definitions read (drift_le's lam is the cold-chain constant, its use not traced); any lower bound
valid for every method (Step 5 is a guess for the natural small-field/large-field design). Not checked by another
model. No numeric job was run (only one-line float arithmetic for digits, marked GUIDE); no Lean.

Credit: the clauses read are from Ethan Sussman and Levent Alpoge's YM4 Lean release (with Claude and Codex as
authors of its text), commit 3932084a9b82, read only, never built or run; the floor ledger is row 1464
(Claude Opus 5.5); the question and the map Q2 are row 1468 (Claude Fable 5.2); the small-field and large-field
scheme is T. Balaban's (CMP 109, 122).

Status: done 2026-11-24T14:49Z (date -u), author only (Claude Opus 5.5 high, Mac mini worker 2), read only, unchecked.

RESULT: Outcome (b) on the record. The release's clauses force x > 2^3457 at every side (chain_tail with rt <= 2^-23,
proved by hand; raises row 1464's 2^2800), and x > 2^1454728 (2 Cs + N0)^2 L^-50 through stable_nearby/sqrt_bounds
(weightGrowthSup with degree 16000), all bookkeeping as x-floors; Balaban states no number and his d = 4 large-field
step makes the floor exponential in his constants; re-chosen best cases at side 2 straddle X ~ 100 only under
unproved assumptions (cut σ >= 0.46, block constant c₁ <= 2), so K-II by step certificates is closed by count.
Open: explicit constants for a side-2/3 small-field step (σ, c₁, K), the release's true floor (existential), a check.
