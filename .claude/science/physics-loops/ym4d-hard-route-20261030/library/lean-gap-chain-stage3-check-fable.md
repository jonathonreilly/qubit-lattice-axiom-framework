lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T18:44Z

# Check of Lean Stage 3 of the gap chain (queue row 1666, checks FINISH row 1657)

Provenance: Claude Fable 5.2, high effort, pinned commit 787645f36, started 2026-11-28T06:44Z (date -u). A reading check, not an audit. The author of Stage 3 was gpt-6.2-astra max. I did not run Lean. Status: complete.

Credit: the YM4 Lean release and its conventions are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Theorem S-w and Theorem EV-L are row 731 of this lane; row 732 (gpt-6-astra) checked them.

## 0. Verdicts

| Item | Verdict |
|---|---|
| 1. Both reduction theorems against Stage 0's type | **HOLDS** |
| 2. `PairWindowEstimate` | **HOLDS** as a definition. It is not weaker than the conclusion. It is not the open target rewritten: it has no seed. |
| 3. Premise true by row 731, section 8.2 | **HOLDS** by hand. First step not in the kernel: Lemma L1-ev applied to the shifted copies of a physical observable, in the proof of EV-L (c). Bookkeeping, no new estimate. |
| 4. Kernel result against `calibratedSpectralPropagation` | **HOLDS** (one wording point) |
| 5. New definitions | **HOLDS**, none trivial |
| 6. Keyword counts | all 0 |

Sources read: `Stage0.lean` and its check (row 1653), all; `RECEIPT-3.md` 1-140; `TheoremS.lean` 310-540; `library/gap-flux-exercise.md` 420-466 and the verdict lines of its check; in `Stage3.lean` all 114 definition bodies and the ranges 4838-4949, 5770-6082, 6354-6608, 6660-6790, 7022-7145, 7280-7309, 7380-7608; in the release (`~/ym4d-papers/sa-ym4-lean-full`) `InfiniteLattice/LimitsAlongTheCutoffs.lean` 74-78 and `GaugeFieldsAndStates.lean` 338-347. The SHA-256 of `Stage3.lean` (`6fee80c6...d7eb6b`) is equal to the receipt's value.

## 1. The two reduction theorems (item 1) — HOLDS

`Stage3.lean` 7567-7587:

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

Stage 0 (`Stage0.lean` 275-277) has `(hL) (h : Inputs L M g₀ K ν S) {ℓ} (hs : KappaSeedAlong L M g₀ ℓ K) : ExpClusters L K ν (gapRate ℓ)`.

- Second theorem: `type_of% @GapChain.expClusters_of_kappaSeed` elaborates to the type of the Stage 0 constant. So the conclusion is that type by construction, binders included. The only hypothesis is `supply`, a closed statement with no seed, no `Inputs`, no `K`: `PairWindowEstimate` at every admissible `L`, every cutoff, every `β > 0`, every infinite-volume limit and every `r > 0`. **HOLDS.**
- First theorem: Stage 0's three hypotheses and `supply`; Stage 0's conclusion, letter for letter. Here `supply` is necessary only at one rate, at the given `(K j, β, ν j)`, and only where the seed holds. **HOLDS.**
- The second is proved from the first and discards the seed. So the closed premise must be true at every β; item 3 shows that it is.

## 2. PairWindowEstimate (item 2) — HOLDS as a definition

```lean
def windowCovariance {a : ℝ} (ν μ : Measure (GaugeField a)) (X Y : SepTuple) (t : ℝ) : ℂ :=
  let M (fs : List RealValued) := CutoffLimits.centredMoment μ ν fs.get
  let f := pushList TimeAxis.timeReflection X.val
  let g := pushList (translate (t • timeBasisVec)) Y.val
  M (f ++ g) - M f * M g

def PairWindowEstimate (L k : ℕ) (β : ℝ) (ν : Measure (GaugeField (PeriodicLattice.meshSize L (k : ℤ))))
    (T : TorusData) (r : ℝ) : Prop :=
  ∀ Z : PositiveSpan, ∀ X Y : ↥Z.val.support, ∃ C : ℝ, ∀ n : ℕ, ∃ D : ℝ, ∀ᶠ v : ℕ in atTop,
    let V := volumeSide L k v
    let B := T.spectrum (cube V)
    let d := 2 * (n : ℝ) + 1
    (r : EReal) ≤ B.gap →
      ‖windowCovariance ν (liftedWilsonMeasure L v k β) X.val Y.val
          (d * PeriodicLattice.meshSize L (k : ℤ))‖ ≤
        C * Real.exp (-r * d) + D * Real.sqrt (1/(V : ℝ) + B.thermal (V/2))
```

**In mathematics.** Let a = L^(-k), V = 2 L^(v+k), and μ_V the periodic Wilson state at β on the torus of side V in all four directions. The release defines `centredMoment μ ν f` = E_μ[∏_i (E_{f_i} − ν(E_{f_i}))], E_f the smeared plaquette energy. For a monomial X put A_X = ∏_{f in X} (E_f − ν(E_f)). Then `windowCovariance` = Cov_{μ_V}(A_{θX}, A_{τ_t Y}): expectation in μ_V, centring constants from ν. B_V is the spectrum list of the cube V^3: top = norm of the release transfer operator; one ratio λ/top for each positive eigenvalue, with multiplicity, of the eight diagonal sectors (magnetic twist m, electric character m), the vacuum removed. `gap` = inf of log(top/λ); `thermal(a)` = Σ (λ/top)^a. The premise:

> for each pair of monomials X, Y of a positive-time test there is C such that for each n there is D such that for all large v: if r ≤ gap(B_V), then |Cov_{μ_V}(A_{θX}, A_{τ_{(2n+1)a} Y})| ≤ C e^(−r(2n+1)) + D (1/V + thermal_V(⌊V/2⌋))^(1/2).

C does not depend on n or V. This is the receipt's display.

**Nothing is hidden behind `.choose`.** The chosen data satisfies `RealizesKappa`: on each box with sides ≥ 3 and each a ≥ 3, top^a (1 + thermal(a)) = Stage 0's `kappaWeight`. These numbers fix top and the positive ratios with multiplicity. So `gap` and `thermal` are fixed quantities of the Wilson model.

**Strength.**
- Alone, the premise does not give `ExpClusters`: its bound is conditional on `r ≤ gap(B_V)`, and without the seed nothing gives that gap.
- At a seeded cutoff the kernel proves the gap for all V ≥ 2N and thermal_V(V/2) → 0 (item 4). There the premise contains the clustering bound: v → ∞ along the subsequence of ν gives |Cov_ν| ≤ C e^(−r(2n+1)) for each pair. The Lean step from premise to conclusion is this limit (`volumeU_tendsto`) and a finite weighted sum (`slabEstimate_of_pairWindows`). It proves no decay.
- The converse fails: the premise is a finite-volume bound for all large v, with a rate of approach, pair by pair in norm. So at a seeded cutoff the premise is **stronger than the conclusion, not weaker**.
- It is still not "equivalent, not progress". The open target of this node is "seed gives clustering". The premise has no seed, no trajectory and no condition on the coupling: it is the general statement "a transfer gap gives exponential decay of the periodic state, up to a finite-volume error" (Theorem EV-L). Its truth does not depend on the gap problem (item 3). The seed-dependent part (Theorem S-w) is in the kernel. So the target is split into a kernel-checked hard half and a seed-free standard half.

## 3. Is the premise true by row 731, section 8.2? (item 3) — HOLDS by hand

Row 732 checked Lemma CB, Lemma MX, Lemma L1-ev and Theorem EV-L (c), (d): all HOLD. The premise from them (my derivation, unformalized): put F = A_{θX}, H = A_{τ_d Y}, d = 2n+1, τ = thermal_V(⌊V/2⌋), and c_A the vacuum value of A on the cylinder V^3 × Z. F and H are bounded functions of plaquette traces, in the class 𝔄_V for large v, with sup norms independent of V.
1. The neutral excited eigenvalues are part of the list B_V. So m_ev ≥ gap(B_V) ≥ r and S_ev(t) ≤ thermal_V(t).
2. EV-L (c) with δ = w(A)+1, N = ⌊V/(2δ)⌋: |ω_per(A) − ω_ev(A)| ≤ ‖A‖ (8 max(4δ(1 + 2/(e^r − 1)), 6))^(1/2) (1/V + τ)^(1/2).
3. L1-ev, second claim: |ω_ev(A) − c_A| ≤ 2‖A‖ min(1, S_ev(V − w)) ≤ 2‖A‖ τ^(1/2).
4. Steps 2 and 3 for A = F, H, FH give three errors D' (1/V + τ)^(1/2). For FH, D' grows with n; the premise permits that.
5. |c_FH − c_F c_H| ≤ ‖F‖‖H‖ e^(−r g), g the number of free transfer steps between the slabs, g ≥ d − c_0(X, Y). For the finitely many n with g < 1 use |Cov| ≤ 2‖F‖‖H‖. So C = 2‖F‖‖H‖ e^(r(c_0+1)).
6. Cov_per(F, H) = [ω_per(FH) − c_FH] + [c_FH − c_F c_H] − [ω_per(F) ω_per(H) − c_F c_H].

This holds at every β > 0, every r > 0 and any centring constants. So the closed `supply` is true by hand, not only its seeded form.

**In the kernel.** Lemma CB: `CentreBlind` for the plaquette marks. MX (d): `jointPeriodic_mean_sq`. L1-ev for words of marks: `normalized_split_covariance`, `normalized_single_window`, `normalized_word_polynomials`. Step 5: `vacuum_covariance`. EV-L (c) in abstract form: `periodic_polynomial_comparison`, with the one-copy and two-copy neutral estimates as hypotheses `single` and `pair`. Step 6: `periodic_covariance_of_three_means`. The observable as a polynomial in marks: `cutoff_polynomial_witness`.

**First step not in the kernel.** In the proof of EV-L (c): "For j < l apply Lemma L1-ev to F = τ_{jδ}A and H = τ_{lδ}A", for a physical A. Nothing supplies `single` and `pair` for the polynomial of `cutoff_polynomial_witness`. By my count, `periodic_polynomial_comparison`, `periodic_covariance_of_three_means`, `cutoff_polynomial_witness`, `normalized_word_polynomials`, `normalized_cyclic_single`, `time_average_placement`, `rotated_polynomial_words` and `jointNeutral_polynomial` are each used 0 times after their declaration. So the assembly is open for all three observables F, H and FH. The receipt's "More explicitly" paragraph says so; its "first missing identification" (the product) names the hardest of the three, not the first.

**Kind: transfer-matrix bookkeeping.** Each analytic estimate of 8.2 is proved (spectral decay, thermal tail, mixture factor 8, variance of the time average). What remains:
- (a) `cutoff_polynomial_witness` gives the expansion of θX ++ τ_d Y existentially, and its `d` moves the whole list. A product form is necessary: the expansion of θX at a fixed place times the expansion of Y moved by d. Then c_FH is the ordered vacuum element of two words with blank layers between them (`padded_vacuum_word` has blanks only at the ends), and `vacuum_covariance` applies. This needs a changed statement, not only a composition.
- (b) The composition of `jointNeutral_polynomial`, `rotated_polynomial_words`, `time_average_placement` and `normalized_word_polynomials` to give `single` and `pair`, with one cube, one chart and one vacuum for the three observables.
- (c) The finitely many separations where the slabs touch.

I see no estimate in (a)-(c) that is not already proved. The size of this Lean work is not measured.

## 4. The kernel result (item 4) — HOLDS

`calibratedSpectralPropagation` (7488-7495) has hypotheses `hL`, `h : Inputs L M g₀ K ν S`, `hs : KappaSeedAlong L M g₀ ℓ K`, and concludes `0 < gapRate ℓ ∧ ∃ᶠ j`, with `T := (rectangularTorusData (h.beta_pos j)).choose`: (i) for all `V ≥ ℓ * L ^ (K j)`, `gapRate ℓ * meshSize L (K j) ≤ (T.spectrum (cube V)).gap`; (ii) `(T.spectrum (cube V)).thermal (V/2)` tends to 0.

- Same cutoff: one `K` in `Inputs`, seed and conclusion; the frequent set is the seed's own (`hs.2.2.mono`).
- Same coupling: `h.beta_pos j : 0 < betaAt L M (K j) g₀`. The seed is read at that β on a constructed cube of side ℓ L^(K j) (`seed_at_calibrated_cutoff`), and `seed_eq_thermal` turns `KappaSeedOnCube` into `T.seed N < 2^-18`, N = ℓ L^(K j)/2: this is S_κ(N; (2N)^3). `physicalRate_eq` gives gapRate ℓ · a_j = log(2^18/5041)/N. The receipt's m and "V ≥ 2N" are exact.
- State witness: ν does not occur in this conclusion; it enters only through `Inputs`. The receipt's sentence on "the volume subsequence supplied by the same state witness" is true of `cutoff_bound_of_finiteTori` and the reduction theorems, which use `h.isLimit j`. A wording point.
- The gap is over all eight diagonal sectors, so it is at most the neutral gap: the stronger statement.
- No vacuity: `hL` is Odd L ∧ 13 ≤ L; `Inputs` comes from the release witnesses; `rectangularTorusData` is a proved existence; each cube in range is valid (side ≥ 26). The only open hypothesis is the seed, by design.

## 5. New definitions (item 5) — HOLDS

I read the body of each of the 114 `def`, `abbrev` and `structure` declarations. There is no `instance`, `class` or `inductive`.

- **Sector algebra.** `joinTwist e m` puts e on the three planes with the time axis 3 and m on the three spatial planes; `fluxEquiv` is a bijection with the 64 twists. `sectorWeight χ m` = (1/8) Σ_e (−1)^(e·χ) Z^(e,m). Stage 0's Pfaffian pairs (0,3)|(1,2), (1,3)|(0,2), (2,3)|(0,1); these are the pairs (e.1, m.1), (e.2.1, m.2.1), (e.2.2, m.2.2). So `kappaWeight_eq_diagonal` (κ-weight = Σ_m `sectorWeight m m`) is the correct identity.
- **Measures.** `twistedMeasure` and `jointState` are `Measure.tilted` of product Haar measures by products of exponentials: probability measures, not zero. `jointState … zeroFlux m` is the periodic closure; `jointNeutralMean` is the mixture of the eight closures with positive weights.
- **Props.** `CentreBlind` is not `True`; it is proved for the plaquette marks. `EncodesSlots`, `EnumeratesRatios`: injective codings with zero padding. `RealizesKappa`: two real equations. `DiagonalTraces`, `SectorResolution`, `NeutralResolution`: data with a positive top value, each with a proved existence theorem.
- **Index types.** None is empty: `Flux` (8), `spatialAxis` (3), `Fin (p+2)`, and `Fin (V/(2·width))` under the stated 4·width ≤ V.
- **Open Props, used only as hypotheses.** `SlabEstimate`, `PairWindowEstimate`, `NeutralSlabComparison` (three forms of the EV-L input), and `CubicTraceIdentity`. The last is never proved; two theorems assume it (`projectedTrace_of_insertions`, `sectorWeight_nonneg_of_insertions`) and nothing later uses them. A dead branch; `cube_sector_eigenspaces` replaced it. No final statement depends on it.

On the receipt's "402 theorems": the count includes those two conditional theorems, seven reduction theorems with a `supply` or `hfinite` premise, and the eight unused lemmas of item 3. The axiom lines are correct; 402 is not the length of one chain.

## 6. Keyword counts (item 6)

`grep -c -w` on `Stage3.lean` (8011 lines, comments included): `sorry` 0, `admit` 0, `axiom` 0, `native_decide` 0, `opaque` 0, `implemented_by` 0 (lines and occurrences). Also absent: `unsafe`, `extern`, `macro`, `reduceBool`. There are 402 theorem lines and 402 `#print axioms` lines. `decide` occurs only as the `Decidable.decide` function and as the kernel tactic `by decide`.

## 7. For the lead

1. Standing text: "W2-W6 kernel-checked; W9 (EV-L) proved in parts, not assembled". All of "gap gives decay" is still in the premise.
2. `cutoff_polynomial_witness` needs a product form first (item 3 (a)).
3. `PairWindowEstimate` has no entry in `library/open-core.md` or `library/open-registry.md` (grep count 0). Its hand content is Theorem EV-L (rows 731, 732), so it is not a new mathematical statement.

Not checked: the proofs (the kernel did that); the release beyond the definitions named above; the hand files (TR) and (L) that row 731 cites.

RESULT row 1666 (Claude Fable 5.2 high, reading check of row 1657; no Lean run): items 1, 2, 4, 5 HOLD; item 6 counts are all 0; item 3 HOLDS by the hand argument. The two reduction theorems have exactly Stage 0's type after the one premise. The kernel result (gap on every cube V ≥ 2N at rate (2/ℓ) log(2^18/5041); tail at V/2 to 0) is faithful and not vacuous. `PairWindowEstimate` is the seed-free statement "finite-volume gap gives exponential decay of the periodic covariance, up to D (1/V + thermal(V/2))^(1/2)". At a seeded cutoff it is stronger than the conclusion and holds all of EV-L; it is not the open target rewritten, and it is true by row 731 section 8.2. Open: the Lean assembly of EV-L (c) for F, H and FH (bookkeeping: product form of the mark expansion, placement of rotated copies, one vacuum, small separations). Stage 0's `sorry` for `expClusters_of_kappaSeed` stays.
