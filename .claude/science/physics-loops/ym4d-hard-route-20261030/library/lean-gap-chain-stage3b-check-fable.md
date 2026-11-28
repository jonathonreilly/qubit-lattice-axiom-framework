lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T19:53:08Z

# Check of Lean Stage 3b of the gap chain (row 1669, checks row 1667)

Provenance: Claude Fable 5.2, high effort, pinned commit fd75828e2, started 2026-11-28T07:53:08Z, complete 2026-11-28T07:58:20Z (date -u). A reading check of statements and definitions, not an audit. The author of Stage 3b was gpt-6.2-astra max. I did not run Lean and did not replay proofs. Status: complete.

Credit: the YM4 Lean release and its conventions are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Theorem EV-L is row 731; row 732 checked it.

## 0. Verdicts

| Item | Verdict |
|---|---|
| 1. `pairWindowEstimate` against `supply`; final theorem against Stage 0 | **HOLDS** |
| 2. One cube and chart, centring, combined word | **HOLDS** |
| 3. Constants, touching case, thermal > 1, quantifier order | **HOLDS** |
| 4. New definitions | **HOLDS**, none trivial |
| 5. Keyword counts | all 0 |

Sources read: `Stage3b.lean`, all 718 lines; `RECEIPT-3b.md`, all; check 1666, all; in `Stage3.lean` the statements of 36 declarations that Stage 3b uses (not all of them; inside 3690-7310, and 6492-6522, 7583-7590); `Stage0.lean` 270-280. The SHA-256 values of `Stage3b.lean` (`24c31a78...5364cf0`) and `Stage3.lean` (`6fee80c6...d7eb6b`) are equal to the receipt's values.

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

`supply` (`Stage3.lean` 7583-7586) is `∀ {L : ℕ} (k : ℕ+) {β : ℝ} (ν : Measure (GaugeField (meshSize L ((k : ℕ) : ℤ)))), IsAdmissibleBlockingFactor L → ∀ hβ : 0 < β, IsInfiniteVolumeLimit L k β ν → ∀ r : ℝ, 0 < r → PairWindowEstimate L k β ν (rectangularTorusData hβ).choose r`.

- The binders agree one by one, in order. The conclusions are the same term. `pairWindowEstimate` has no other hypothesis. Stage 3b defines no second `PairWindowEstimate`; the name is Stage 3's (line 6510).
- The final proof term is one application of Stage 3's theorem to `@pairWindowEstimate`, with no other argument.
- `GapChain.expClusters_of_kappaSeed` is declared one time in the folder (`Stage0.lean` 275, proof `sorry`). `type_of%` reads only its type: `(hL) (h : Inputs L M g₀ K ν S) {ℓ} (hs : KappaSeedAlong L M g₀ ℓ K) : ExpClusters L K ν (gapRate ℓ)`. The receipt's axiom line has no `sorryAx`.

## 2. Product witness and combined word (item 2) — HOLDS

`cutoff_product_witness` (501-518), shortened:

```lean
∃ I _ (x : I → ℂ) (b : ℤ) (u : ℕ) (K : ℝ) J _ (y : J → ℂ) (c : ℤ) (w : ℕ) (M : ℝ), 0 ≤ K ∧ 0 ≤ M ∧
  ∀ v : ℕ+, ∃ Γ (E : Fin Γ.side ≃ ZMod Γ.side) (F : WordFamily _ Γ.side I u) (H : WordFamily _ Γ.side J w),
    Γ.side = volumeSide L k v ∧ (∀ i, E i = (i.val : ZMod Γ.side)) ∧
    (u ≤ Γ.side → F.cost x ≤ K) ∧ (w ≤ Γ.side → H.cost y ≤ M) ∧
    ∀ d : ℕ, let G := monomial ν Γ E (pushList timeReflection X.val)
             let P := monomial ν Γ E (gridShift a d Y.val)
      (∀ z, (G z : ℂ) = F.value x b z) ∧ (∀ z, (P z : ℂ) = H.value y (c + d) z) ∧
      (∀ z, (monomial ν Γ E (… X.val ++ gridShift a d Y.val) z : ℂ) = F.value x b z * H.value y (c + d) z) ∧
      windowCovariance ν (liftedWilsonMeasure L v k β) X Y (d * a) =
        periodicMean Γ β (fun z => G z * P z) - periodicMean Γ β G * periodicMean Γ β P
```

- **One cube, one chart.** For each `v` there is one `Γ` and one `E`. `G`, `P`, their pointwise product and the three means use this `Γ`, this `E` and one measure, `jointState (fun _ => Γ.side) β zeroFlux zeroFlux`. The last line is an equality with Stage 3's `windowCovariance`, the object of `PairWindowEstimate`. `polynomial_periodic` takes a second `E` from `anchoredCubeTimeIndex Γ 0`; it is the same function `i ↦ (i.val : ZMod Γ.side)`. `WordFamily.value` does not contain `E`.
- **Order of choice.** Labels, coefficients, anchors `b, c`, widths `u, w` and budgets `K, M` come before `v` and `d`. `K = Σ_j ‖x_j‖ 2^length` (447).
- **Centring.** `monomial ν Γ E fs z` is the product over `f ∈ fs` of `smearedEnergy (unitTest a f) (…) − ∫ smearedEnergy f ∂ν`. For `P` the list is `gridShift a d Y.val`. So each factor is centred at ν(E_{τ_d f}), as in `centredMoment μ ν`. One family `H` at position `c + d` represents all translates because ν(E_{τ_d f}) = ν(E_f) (`frozen_smearedMean_motion`, Stage 3 6317, from `hν`).
- **Combined word.** `separated` (45-47): `mark p t = F.mark p.1 t * G.mark p.2 (t − (u+g))`. `separated_value` (61-64): its value at `s` is `F.value x s z * G.value y (s + (u+g)) z`, pointwise. `separated_word` (76-79), under `u+g+w ≤ V`:

```lean
(F.separated G g).word p = F.word p.1 ++ List.replicate g 1 ++ G.word p.2
```

- **Transfer power.** In `separated_vacuum` (180-220), `hm` is `M (U ++ replicate g 1 ++ W) = (M U * T^g) * M W`, with `M = slabProduct n β B.top zeroFlux` and `T = B.top⁻¹ • rectSector n β zeroFlux zeroFlux`. By `projectedLayer_one` (Stage 3, 5009) the mark `1` gives exactly `T`. `B.top` is the norm of the transfer operator (`hn`). `vacuum_covariance` with `d := g` gives the error `F.cost x * G.cost y * 2 exp(−r g)`.
- **g is the true blank count.** `place` (667-672) is `c + d = b + (u+g)` in ℤ. So the `F` word is on layers `b … b+u−1` and the `H` word starts at `b+u+g`.
- **One vacuum.** `separated_periodic_covariance` (567-598) takes `⟨A, Q, enum, trace⟩` from `common_resolution` one time. It uses this `Q` for `F`, `H`, the product family and `separated_vacuum`. `polynomial_periodic` supplies `single` and `pair` to `periodic_polynomial_comparison` from `single_trace` and `PairTrace Q`. The constants agree: `B = K`, `M = 2K`, `D = 2K²` give `A = 2K² + 3K(2K) + 4K²`, as in `meanError`.

So items (a), (b), (c) of check 1666, section 3, are supplied: (a) by `cutoff_product_witness`; (b) by `common_resolution`, `polynomial_periodic` and `separated_periodic_covariance`; (c) by `trivial_covariance`.

## 3. Constants and quantifier order (item 3) — HOLDS

The proof of `pairWindowEstimate` (618-631), in order:

```lean
intro Z X Y
obtain ⟨I,fi,x,b,u,K,J,fj,y,c,w,M,hK,hM,all⟩ := cutoff_product_witness hL k hβ hν X.val Y.val
let c₀ := (b-c).natAbs + u
let C := 2*K*M * Real.exp (r*((c₀ : ℝ)+1))
refine ⟨C,fun n => ?_⟩
let d := 2*n+1
let g := (c+(d : ℤ)-b-u).toNat
let D := covarianceError K M u w g r + 2*K*M
refine ⟨D,?_⟩
filter_upwards [eventually_ge_atTop 1,grow (eventually_ge_atTop (4*(u+g+w+1)+6))] with v hv size
```

- This is the order of `PairWindowEstimate`: ∀ Z X Y, ∃ C, ∀ n, ∃ D, ∀ᶠ v. `C` has only `K, M, b, c, u, r`; it is fixed before `n` and `v`. `D` has `n` through `g`; it has no `v`.
- The goal after the case split is `‖cov‖ ≤ C*exp(−r*d) + D*δ`, δ = `sqrt(1/Γ.side + thermal(Γ.side/2))`, `Γ.side = volumeSide L k v`. `D` multiplies only δ.
- **Touching, d ≤ c₀** (661-665). `trivial_covariance` gives `‖cov‖ ≤ 2KM`. `exponential_offset` with `g = 0` gives `2KM ≤ C exp(−r d)`, because `d ≤ c₀ + 1`. The gap hypothesis is not used.
- **Separated, d > c₀, thermal ≤ 1** (666-678). Then `c + d − b − u > (c − b) + |b − c| ≥ 0`, so `toNat` is exact and `g ≥ 1`. Also `g + c₀ + 1 ≥ d + 1`, so `KM · 2 exp(−r g) ≤ C exp(−r d)`. `covarianceError ≤ D`.
- **thermal > 1** (679-685). Then δ ≥ 1 and `‖cov‖ ≤ 2KM ≤ D ≤ D δ`. This is why `D` has the term `2KM`.
- The volume condition `4(u+g+w+1)+6 ≤ volumeSide` depends on `n`. That is permitted: `v` comes after `n`.
- `C` is the hand constant of check 1666, step 5, with the budgets `K, M` in place of the sup norms.

## 4. New definitions (item 4) — HOLDS

The file has 14 definitions: one `structure`, two `abbrev`, eleven `def`. It has no `instance`, `class` or `inductive`.

- `WordFamily n V J width`: marks `J → ZMod V → LayerMark n`, each `CentreBlind`, each equal to 1 outside the residues `0 … width−1`. It is data. `J` can be empty; then `value = 0`, and the proved pointwise identity with `monomial` does not permit that for a non-zero observable.
- `word`, `cost`, `value`, `separated`, `vacuumValue`: a list, a non-negative real, two finite sums, a product family.
- `spectrum`, `CubeResolution`: abbreviations of Stage 3 objects on `cube Γ.side`. `spectrum hβ Γ` is the term `T.spectrum (cube V)` of `PairWindowEstimate` at `V = Γ.side`.
- `PairTrace Q`: the only new `Prop`. It is a ∀-statement with the conditions `0 < l`, `3 ≤ a`, `V = l+u+d+w+a`, which have solutions. `common_resolution` proves it; `polynomial_periodic` uses it at `V = Γ.side`.
- `monomial`, `gridShift`, `periodicMean`: the centred product, the translated list, the integral in the periodic state. `jointState` is a probability measure for side ≥ 2, not zero.
- `meanError`, `covarianceError`: explicit reals. They occur only in the existential witness `D`. The `tsum` in `meanError` converges for `r > 0`.
- No hypothesis on the path is unsatisfiable: `hL`, `0 < β`, `hν`, `0 < r` are the hypotheses of `supply`. The proof supplies `u ≤ Γ.side` and the size bound, and splits on `thermal ≤ 1`.

## 5. Keyword counts (item 5)

`grep -c -w` and `grep -o -w` on `Stage3b.lean` (comments included): `sorry` 0, `admit` 0, `axiom` 0, `native_decide` 0, `opaque` 0, `implemented_by` 0, as lines and as occurrences. Also 0: `unsafe`, `extern`, `macro`, `reduceBool`, `decide`. There are 26 `theorem` lines and 26 `#print axioms` lines; a `diff` shows that their names are the receipt's 26 names.

## 6. For the lead

1. Stage 0's constant `GapChain.expClusters_of_kappaSeed` is still `sorry`, and `Stage0.lean` 283 (`expClusters_of_mNeutral`) calls it. The final assembly must call `GapChain.Stage3b.expClusters_of_kappaSeed`. `Stage4.lean` and `Assembly.lean` do not name either one (grep count 0).
2. The receipt's "proposed next row 1668" is this row, 1669. No other correction to the receipt.
3. `pairWindowEstimate` has no entry in `library/open-core.md`, `library/open-registry.md` or `library/t0-tree.md` (grep count 0). It is the Lean form of Theorem EV-L (rows 731, 732), not a new mathematical statement.

Not checked: the proofs and the axiom reports (I did not run Lean; the logs are in the author's scratch folder, which I did not read); the Stage 3 statements that I did not open; the release beyond what check 1666 read.

RESULT row 1669 (Claude Fable 5.2 high, reading check of row 1667; no Lean run): items 1-4 HOLD and the item 5 counts are all 0. `pairWindowEstimate` has exactly the type of the closed premise `supply`, and `Stage3b.expClusters_of_kappaSeed` has exactly Stage 0's type. F, H and FH are on one cube, one chart and one neutral vacuum; the centring at ν is kept; the combined word is U ++ 1^g ++ W with the normalized neutral transfer to the power g. C = 2KM exp(r(c₀+1)) is fixed before n and V, and D multiplies only sqrt(1/V + thermal(V/2)). Open: the Pfaffian seed (a hypothesis by design), and the final assembly that replaces Stage 0's `sorry` constant in its consumers.
