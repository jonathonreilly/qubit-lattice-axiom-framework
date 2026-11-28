lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T18:44Z

# Check of Lean Stage 3 of the gap chain (queue row 1666, checks FINISH row 1657)

Started 2026-11-28T06:44Z (date -u). Pinned commit 787645f36. Status: complete (sections are in the order written: 0, 6, 1, 2, 3, 4, 5, 7). Not an audit.

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

## 2. PairWindowEstimate (item 2) — HOLDS as a definition; it is not weaker than the conclusion, and it is not the open target rewritten

More sources for this section: `Stage3.lean` 5318-5350, 5494-5512, 5610-5660 (`boxSides`, `EncodesSlots`, `DiagonalTraces`), `Wilson.lean` 392-412 (`EnumeratesRatios`); the release at `~/ym4d-papers/sa-ym4-lean-full`: `InfiniteLattice/LimitsAlongTheCutoffs.lean` 74-78 (`centredMoment`), `GaugeFieldsAndStates.lean` 338-347 (`liftedWilsonMeasure`, `IsInfiniteVolumeLimit`).

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

**In mathematics.** Let a = L^(-k), V = 2 L^(v+k), and μ_V the periodic Wilson state at β on the torus of side V in each of the four directions (lifted to the infinite lattice). The release defines `centredMoment μ ν f` = E_μ[∏_i (E_{f_i} − ν(E_{f_i}))], with E_f the smeared plaquette energy. So for a monomial X write A_X = ∏_{f in X} (E_f − ν(E_f)). Then `windowCovariance` = Cov_{μ_V}(A_{θX}, A_{τ_t Y}): the expectation is in μ_V, the centring constants are those of ν, and the product of the two μ_V-means is subtracted. B_V is the spectrum list of the cube V^3: top = norm of the release transfer operator, and one ratio λ/top for each positive eigenvalue, with multiplicity, of the eight diagonal sectors (magnetic twist m, electric character m), the vacuum removed. `gap` = inf of log(top/λ) over that list; `thermal(a)` = sum of (λ/top)^a over that list. The premise says:

> for every pair of monomials X, Y of a positive-time test, there is C such that for every n there is D such that for all large v: if r ≤ gap(B_V), then |Cov_{μ_V}(A_{θX}, A_{τ_{(2n+1)a} Y})| ≤ C e^(−r(2n+1)) + D (1/V + thermal_V(⌊V/2⌋))^(1/2).

C does not depend on n or V. D may depend on n. This is the statement that the receipt displays. **The definition agrees with the receipt.**

**The torus data is not hidden behind `.choose`.** `(rectangularTorusData hβ).choose` satisfies `RealizesKappa`: on every box with sides at least 3 and every time a ≥ 3, top^a (1 + thermal(a)) = `kappaWeight`, Stage 0's signed sum of 64 twisted partition functions. These numbers for all a ≥ 3 fix top (the limit of the a-th root) and the positive ratios with multiplicity (power sums). So `gap` and `thermal` in the premise are fixed real quantities of the Wilson model. A person who proves the premise has all that is necessary from `choose_spec`.

**Strength against the conclusion.**
- As a closed statement, the premise does not give `ExpClusters`. The exponential bound is conditional on the finite-volume gap `r ≤ gap(B_V)`. Without the seed nothing gives that gap, and the premise is then empty.
- At a seeded cutoff the kernel proves the gap on every V ≥ 2N and thermal_V(V/2) → 0 (item 4). There the premise does contain the clustering bound: let v → ∞ along the subsequence of ν and the error term goes to 0, so |Cov_ν| ≤ C e^(−r(2n+1)) for each pair of monomials. The Lean step from premise to conclusion is this limit (`volumeU_tendsto`) and a finite weighted sum (`slabEstimate_of_pairWindows`). It is soft.
- The converse fails. The premise is a finite-volume bound for all large v with an explicit rate of approach, pair by pair in norm. `ExpClusters` is a bound in the limit state, for the real part of the sum, at frequent j. So the premise is **stronger than the conclusion at a seeded cutoff, not weaker**.
- Is the reduction then "equivalent, not progress"? No. The open target of this node is "seed gives clustering". The premise has no seed, no trajectory and no coupling condition: it is the general statement "a transfer gap gives exponential decay of the periodic state, up to a finite-volume error" (Theorem EV-L of row 731). It is true or false at every β independently of the gap problem, and the hand record says it is true (item 3). The part that depends on the seed (Theorem S-w: seed gives the gap on all larger cubes, and the tail goes to 0) is in the kernel. So the reduction splits the target into a kernel-checked hard half and a seed-free standard half. It does not hide the target in the premise.
- One caution for the standing text: the reduction's own step (premise to conclusion) proves no decay. All of "gap gives decay" is still in the premise. The correct summary is "W2-W6 checked; EV-L (W9) not assembled", not "Stage 3 reduced to a scalar estimate" alone.

## 3. Is the premise true by row 731, section 8.2? (item 3) — HOLDS by the hand argument; the missing step is bookkeeping

More sources: `library/gap-flux-exercise.md` 420-466 (all of 8.2); `library/gap-flux-exercise-check.md` verdict lines (row 732, gpt-6-astra: Lemma CB, Lemma MX, Lemma L1-ev, Theorem EV-L (c), (d) all HOLD); `Stage3.lean` 4838-4949, 6354-6486, 6660-6790, 7022-7057, 7086-7145, 7280-7309.

**The premise from 8.2 (my derivation, by hand, unformalized).** Put F = A_{θX}, H = A_{τ_d Y}, d = 2n+1. Both are bounded functions of plaquette traces, so they are in the class 𝔄_V for large v, with sup norms that do not depend on V (the constants ν(E_f) are fixed). Write c_A for the vacuum value of A on the cylinder V^3 × Z, and τ = thermal_V(⌊V/2⌋).
1. The neutral excited eigenvalues are a part of the list of B_V. So m_ev ≥ gap(B_V) ≥ r and S_ev(t) ≤ thermal_V(t).
2. Theorem EV-L (c) with δ = w(A)+1 and N = ⌊V/(2δ)⌋: N δ ≤ V/2, so S_ev(V − Nδ) ≤ τ, and 1/N ≤ 4δ/V. So |ω_per(A) − ω_ev(A)| ≤ ‖A‖ (8 max(4δ(1 + 2/(e^r − 1)), 6))^(1/2) (1/V + τ)^(1/2).
3. Lemma L1-ev, second claim: |ω_ev(A) − c_A| ≤ 2‖A‖ min(1, S_ev(V − w)) ≤ 2‖A‖ τ^(1/2).
4. Steps 2 and 3 for A = F, H and FH give three errors of size D' (1/V + τ)^(1/2). For FH the width, and so D', grows with n. The premise permits that.
5. On the cylinder, |c_FH − c_F c_H| ≤ ‖F‖‖H‖ e^(−r g), where g is the number of free transfer steps between the two slabs, and g ≥ d − c_0(X, Y). For the finitely many n with g < 1 use |Cov| ≤ 2‖F‖‖H‖. So C = 2‖F‖‖H‖ e^(r(c_0+1)) is sufficient, and it is chosen before n and V.
6. Cov_per(F, H) = [ω_per(FH) − c_FH] + [c_FH − c_F c_H] − [ω_per(F) ω_per(H) − c_F c_H]. This gives the premise at every β > 0 and r > 0, for any centring constants. So the closed `supply` of item 1 is also true by hand, not only its seeded form.

**What the kernel has.** Lemma CB: `CentreBlind` for the plaquette marks. Lemma MX (d): `jointPeriodic_mean_sq`. Lemma L1-ev: `normalized_split_covariance`, `normalized_single_window`, `normalized_word_polynomials` (words of marks, error 2e^(−rd) + 2 thermal(a)). Step 5: `vacuum_covariance`. Theorem EV-L (c) in abstract form: `periodic_polynomial_comparison`, with the one-copy and two-copy neutral estimates as hypotheses `single` and `pair`. Step 6: `periodic_covariance_of_three_means`. The physical observable as a polynomial in marks: `cutoff_polynomial_witness`.

**First step that the kernel does not carry.** In the proof of Theorem EV-L (c), the sentence "For j < l apply Lemma L1-ev to F = τ_{jδ}A and H = τ_{lδ}A", for a physical A. In Lean terms: nothing supplies `single` and `pair` of `periodic_polynomial_comparison` for the polynomial of `cutoff_polynomial_witness`. I counted uses: `periodic_polynomial_comparison`, `periodic_covariance_of_three_means`, `cutoff_polynomial_witness`, `normalized_word_polynomials`, `normalized_cyclic_single`, `time_average_placement`, `rotated_polynomial_words` and `jointNeutral_polynomial` are each used 0 times after their declaration. So the last assembly is open for all three observables F, H and FH, not only for the product. The receipt says the same in its "More explicitly" paragraph. Its sentence "the first missing identification occurs ... [for] the physical product" names the hardest of the three, not the first.

**Kind of step: transfer-matrix bookkeeping.** Each analytic estimate of 8.2 is in the kernel (spectral decay, thermal tail, mixture inequality with factor 8, variance of the time average). The work that remains:
- (a) `cutoff_polynomial_witness` gives the expansion of θX ++ τ_d Y existentially, and its `d` moves the whole list. A product form is necessary: expansion(θX) at a fixed place times expansion(Y) moved by d (two calls of `cutoff_translated_marks` and a pointwise product). Then c_FH is the ordered vacuum element of the two words with blank layers between (`padded_vacuum_word` covers only blanks at the ends), and `vacuum_covariance` applies.
- (b) The compositions `jointNeutral_polynomial` + `rotated_polynomial_words` + `time_average_placement` + `normalized_word_polynomials` to give `single` and `pair`, with one cube, one chart and one vacuum for all three observables.
- (c) The finitely many separations where the two slabs touch.
I see no estimate in (a)-(c) that is not already proved. I did not write the Lean, so the size of (a)-(c) is not measured; (a) needs a changed statement, not only a composition.

## 4. The kernel result against calibratedSpectralPropagation (item 4) — HOLDS

```lean
theorem calibratedSpectralPropagation ... (hL : Conventions.IsAdmissibleBlockingFactor L) (h : Inputs L M g₀ K ν S)
    {ℓ : ℕ} (hs : KappaSeedAlong L M g₀ ℓ K) :
    0 < gapRate ℓ ∧ ∃ᶠ j in atTop,
      let T := (rectangularTorusData (h.beta_pos j)).choose
      (∀ V ≥ ℓ * L ^ (K j : ℕ),
        ((gapRate ℓ * PeriodicLattice.meshSize L ((K j : ℕ) : ℤ) : ℝ) : EReal) ≤ (T.spectrum (cube V)).gap) ∧
        Tendsto (fun V : ℕ => (T.spectrum (cube V)).thermal (V/2)) atTop (𝓝 0)
```

- Same cutoff: one `K` in `Inputs`, in the seed and in the conclusion. The frequent set of j is the seed's own set (`hs.2.2.mono`).
- Same coupling: `h.beta_pos j` has type `0 < betaAt L M (K j) g₀`, so T is the torus data at the release's least-root coupling at cutoff K j. The seed is read at the same β, on a cube of side ℓ L^(K j) that the proof constructs (`seed_at_calibrated_cutoff`), and `seed_eq_thermal` turns Stage 0's `KappaSeedOnCube` into `T.seed N < 2^-18` with N = ℓ L^(K j)/2. This is S_κ(N; (2N)^3), as Stage 0 states it.
- Rate: `physicalRate_eq` gives gapRate ℓ · a_j = log(2^18/5041)/N. The receipt's m = (2/ℓ) log(2^18/5041) and "every integer V ≥ 2N" are exact.
- State witness: ν does not occur in this conclusion. It enters only through `Inputs` (positivity of β). The receipt's sentence about "the volume subsequence supplied by the same state witness" is true of `cutoff_bound_of_finiteTori` and of the reduction theorems, where `h.isLimit j` and `ν j` are used; it is not a property of this theorem. A wording point, no error.
- The gap is the gap of all eight diagonal sectors relative to the neutral vacuum. So it is at most the neutral gap, and the kernel statement is the stronger one.
- No vacuity: `hL` is Odd L ∧ 13 ≤ L. `Inputs` is supplied by the release witnesses (`FixedObservableWitnesses.inputs`, Stage 0). `rectangularTorusData` is a proved existence theorem. The range V ≥ ℓ L^(K j) is not empty, and each such cube is valid (side ≥ 26). The only open hypothesis is the seed `KappaSeedAlong`, which is the chain's hypothesis by design.

## 5. New definitions (item 5) — HOLDS; no definition makes a statement trivial

I printed the body of each of the 114 `def`, `abbrev` and `structure` declarations of `Stage3.lean` and read them. There is no `instance`, `class`, `inductive`, `opaque` or `axiom`.

- **Sector algebra.** `joinTwist e m` puts e on the three planes that contain the time axis 3 and m on the three spatial planes; `fluxEquiv` is a bijection with the 64 twists. `character e χ` = (−1)^(e·χ). `sectorWeight χ m` = (1/8) Σ_e (−1)^(e·χ) Z^(e,m). I checked the pairing by hand: Stage 0's Pfaffian pairs (0,3) with (1,2), (1,3) with (0,2), (2,3) with (0,1), and these are the pairs (e.1, m.1), (e.2.1, m.2.1), (e.2.2, m.2.2). So `kappaWeight_eq_diagonal` (κ-weight = Σ_m `sectorWeight m m`) states the correct identity.
- **Measures.** `twistedMeasure` and `jointState` are `Measure.tilted` of a product Haar measure by a density that is a product of exponentials, so they are probability measures (`jointState_probability`), not zero. `rectHaar`, `jointHaar`, `releasePairHaar` are products of normalized Haar measures. `jointState … zeroFlux m` is the periodic closure; `jointNeutralMean` is the mixture of the eight closures with the positive weights Z^(e,m). The lifted torus measure and the weak limit are the release's own.
- **Props.** `CentreBlind F` (F does not change when both slices get the same centre flip) is true of the constant 1 and proved for the plaquette marks; it is not `True`. `EncodesSlots` and `EnumeratesRatios` are injective codings with zero padding. `RealizesKappa` has two real equations. `DiagonalTraces`, `SectorResolution` and `NeutralResolution` are data with a positive top value; each has a proved existence theorem (`rectangularDiagonalTraces`, `markedSectorResolution`, `calibrated_neutralResolution`).
- **Index types.** `Flux` has 8 elements, `spatialAxis` 3, `Fin (p+2)` at least 2. The rotation index `Fin (V/(2·width))` is not empty under the stated hypothesis 4·width ≤ V. The supports `↥Z.val.support` in the premise are empty only for Z = 0.
- **Open Props, each used only as a hypothesis.** `SlabEstimate`, `PairWindowEstimate`, `NeutralSlabComparison` (the three forms of the open EV-L input) and `CubicTraceIdentity`. `CubicTraceIdentity` is never proved. Two theorems take it as a hypothesis (`projectedTrace_of_insertions`, `sectorWeight_nonneg_of_insertions`) and nothing after them uses them: a dead branch, replaced by `cube_sector_eigenspaces`. No final statement depends on it.

Two notes on the receipt's count "402 theorems". (1) It includes these two conditional theorems and seven reduction theorems with a `supply` or `hfinite` premise. (2) It includes the eight unused leaf lemmas of item 3. The axiom lines are correct for each; "402 theorems" is not "402 steps of one chain".

## 7. Verdicts

| Item | Verdict |
|---|---|
| 1. Both reduction theorems against Stage 0's type | **HOLDS** |
| 2. `PairWindowEstimate`: definition against the receipt | **HOLDS**. Not weaker than the conclusion; not equivalent to the open target (it is seed-free). |
| 3. Premise true by row 731, 8.2 | **HOLDS** by hand (rows 731, 732; my derivation above). First step not in the kernel: Lemma L1-ev applied to the shifted copies of a physical observable in the proof of EV-L (c). Bookkeeping, no new estimate. |
| 4. Kernel result against `calibratedSpectralPropagation` | **HOLDS** (one wording point on "state witness") |
| 5. Definitions | **HOLDS** |
| 6. Keyword counts | all 0 |

Corrections for the lead's standing text (none changes a Lean statement):
1. Say "W2-W6 kernel-checked; W9 (EV-L) proved in parts and not assembled". The premise holds all of "gap gives decay".
2. The closed premise of `expClusters_of_kappaSeed_of_pairWindows` asks for EV-L at every β > 0 and every r > 0. The hand argument gives that. A Lean proof can aim at the seeded form (`expClusters_of_seeded_pairWindows`) if that is shorter; the seed gives it nothing more than the gap, which the premise already has as its hypothesis.
3. `cutoff_polynomial_witness` needs a product form before the assembly (item 3 (a)).

Not checked here: the proofs (the kernel did that); the release beyond the four definitions named in item 2; the hand files (TR) and (L) that row 731 cites (row 732 checked 8.2 against them). The premise is new in this lane as a Lean statement: `library/open-core.md` and `library/open-registry.md` have no entry `PairWindowEstimate`; its hand content is Theorem EV-L (row 731, checked in row 732).

RESULT row 1666 (Claude Fable 5.2 high, reading check of row 1657; no Lean run): items 1, 2, 4, 5 HOLD, item 6 counts all 0, item 3 HOLDS by the hand argument. Stage 3's two reduction theorems have exactly Stage 0's type after the one premise. The kernel result (gap on every cube V ≥ 2N at rate (2/ℓ) log(2^18/5041), tail at V/2 to 0) is faithful and not vacuous. The premise `PairWindowEstimate` is the seed-free statement "finite-volume gap gives exponential decay of the periodic covariance, up to D (1/V + thermal(V/2))^(1/2)": it is stronger than the conclusion at a seeded cutoff and holds all of EV-L, but it is not the open target rewritten, and it is true by row 731 section 8.2. Open: the Lean assembly of EV-L (c) for the physical observables F, H and FH (bookkeeping: product form of the mark expansion, placement of rotated copies, one vacuum, small separations). Stage 0's `sorry` for `expClusters_of_kappaSeed` stays.
