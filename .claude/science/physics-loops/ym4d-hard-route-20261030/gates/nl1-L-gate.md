First failing step: none.

# Pass-3 referee report: `library/nl1-L.md` (NL1 input (L) and the CI reduction)

Text checked: `library/nl1-L.md`, 727 lines, read once, line by line.
Imports checked against: `st1-r3.md` (with `st1-r2.md` and `st1-draft3.md` where the text cites round 2 or the round-3 draft), `pan-draft.md`, `in1.md`, `ci-form-draft.md`, `pr-lay.md`, `p82.md`, `tp1.md`, `gates/kept-cov-check.md`, `gates/in1-gate.md`, `gates/p82-gate.md`, `gates/tp1-gate.md`. No gate exists yet for ST1 round 3, PAN or CI-form.

## 1. What was checked and holds

**Definitions (L14–107).** (1): with Pauli `T_a` (orthonormal for ½Tr), each `‖T_a‖ = 1`, so `‖u(ζ)‖ ≤ 3g|ζ|_∞`; `c_T = 3` is right. (2), the mask, and (5), the centred substitution, are well defined. (4) agrees with ST1 (18) for the main step `t = i` (`d_* = (1−θ_s)β_s 2^{−(t−m)}`, `w = ½ d_* r_0`). The text extends `w` to `m = i` only as a comparison weight (L87–89), and says so.

**Order and constants (L200–236).** `r_*` sits in ST1 r3 order row 6, before `κ` and `M`. `C_lev` and `K_pin` are "independent of depth and M, κ̄" (ST1 r3 Lemma 4, L306). `ρ_0` with `μρ_0/2 ≥ log 16` is ST1 r3 row 3. `C_0` and `C_1` come after `M, κ, κ̄` (ST1 r3 row 9; IN1 row 6; SA 19466–19470). `C_0` in (8) depends on `E_κ̄` and `e^{κ̄}` only through the late constant `B_L`. Every inequality in (9) is a ceiling on `γ`:
- `ℓ^{p_0−q} → 0`;
- `δ_0 → 0`;
- `gℓ^q → 0`;
- `C_win A_1 ℓ^{p_0}/ℓ^q → 0`.

`c_R = 1` is early, and every loss sits in late `C_0`, in `C_1 ≥ K_rad M C_0`, or in coupling ceilings. The constants rule holds.

**Lemma 1.**
- `|(log r)'| ≤ (½+q)/θ` for `θ ≥ e`. This gives the adjacent ratios. Then `w(m') ≤ 4^{|m'−m|} w(m)` and `L^{−pν} w(m+ν) ≤ w(m)` both follow.
- (10) is ST1 r2's row-5 floor (`C_RA λ ε_m ≤ c_min² λ r_0(m)/16`) with Tq inserted.
- In (11):
  - `θ_i/θ_m ≤ 1+ν` uses `θ_m ≥ B̄`.
  - `log θ_m ≤ 2 log θ_i` uses `θ_m ≤ θ_i + c_5 ≤ 2θ_i`; the floor `γ^{−2} ≥ max(B̄, c_5, e)` covers both.
  - `(1+ν)^{1/2} L^{−2ν} ≤ 1`.
- The witness quotient and output quotient go to zero as stated. The stage quotient also goes to zero: `p_1 + r < p_0 < q` follows from `p_0 − p_1 > r`.
- The exponential-series bound `e^{−x/2} x^d ≤ 2^n n! x^{d−n}` is correct.

**Lemma 2.**
- With `ν = i−1−m_+ ≥ −1`, `w^{−1} ≤ 4·4^{ν_+}/(β_* r_0(i−1))`.
- `4^{ν_+} 16^{−(ν−3)_+} ≤ 64`; it equals `4^{6−ν}` for `ν ≥ 4`.
- `256 e^{μC_car/2} = C_Q`.
- For the second bound: `μρ_0/4 ≥ log 4`, `4^{ν_+} 4^{−(ν−3)_+} ≤ 64`, and `e^{μC_car/4} ≤ e^{μC_car/2}`.
- The separation input is ST1 r3 (74), one-sided at `j = t−1`.

Both inequalities of (12) hold.

**Lemma 3.**
- `t ↦ φ(te)` has a zero of order `≥ k_f` (order 0 is included, since `k_f ≥ 1`). The maximum principle and `c' ↑ c_W` give `|φ(w)| ≤ B_f(‖w‖/c_W)^{k_f}`, and (13) follows.
- Diameter `2R_W+2 < M` gives at most 2 cubes per coordinate, so at most `2^4 = 16` corner-connected cubes.
- The four amplitude conversions check:
  - `θ(gℓ^q)^3 = gℓ^{3q}`;
  - `θε(gℓ^q)^2 = A_0 g ℓ^{p_0+2q}`;
  - each is at most `g ℓ^{3q+r}`, because `p_0 < q`.

**Theorem 4: masking and centring (L3, L5).**
- `‖v‖ ≤ δ_0 + c_T g e^{κ̄} R`, since `⊕` is the stored/free split.
- The last three entries of (9) keep `v`, `S(v)` and `S(v_0)` in the H-FL and H-DR balls.
- (14): the three responses contribute `δ_0 + (δ_0 + c_T g e^{κ̄} R) + δ_0`, each decaying from `supp S ⊂ 𝒮`.
- (15): `C_lev A_V Q_f` with `r_0(i−1) = C_0 g ℓ^q` splits into a stored part and a fluctuation part:
  - stored part `≤ r_*/8` by the first entry of (9);
  - fluctuation part `= B_L c_T e^{κ̄}/(β_* C_0) ≤ r_*/8` by (8).
- `2K_pin A_V < ε_lev` forces levelling, as ST1 r3 Lemma 4 (27) requires.
- L5: at `ζ = 0`, `v = v_0` and the last two terms of (5) cancel, so `Π_f(P;s,0) = ρ(P ∔ 𝒫_P h_0)` for every `s`.
- L3:
  - Cubes corner-adjacent to `K` and outside it have `s = 0`.
  - Source rows assigned to `K` read only `K` and its first layer (`R_σ < M−2`).
  - The face-components of `supp s` that meet `X_f` are face-components of `K` itself, so they are the same for `s` and `s'`.
  - H-DR row locality then fixes the response on the reads in `X_f`.
  - `h_0` is common to both switch choices, and all pin reads lie in `X_f`.
- Reality and the real centre hold, as does `B_f − f_0 ≥ 0` for islands.
- The six PAN clauses map as follows: holomorphy is L1; clause 1 is L2; clause 2 is L3; clause 3 is L4 and L5; clause 4 is L6, in the amended form.

**Corollary 4.1 (Schwarz/recentring).** Take `|e|_∞ = 1`. Then `(F(s,te) − f_0)/t` is holomorphic on `|t| < R_f`, and the maximum principle gives `|F − f_0| ≤ ω_f|ζ|/R_f`. This is exactly the conclusion of PAN Lemma 5.3(a), whose proof (`pan-draft.md` L197–L200) uses only `|φ| ≤ ω`. PAN uses the absolute two-sided bound only through Lemma 5.3(a): (6.1) and Proposition 6.1(d) use `o_f(r)` only. The one-sided (b) is unchanged. So the oscillation form of L6 suffices, and `ω_f = 2b_f` has the same value as PAN's.

**Lemma 5.** At radius `R^scr`:
- `C_A c_T g e^{κ̄} R^scr ≤ c_cap`;
- source `< s_D/3`;
- chart `< a_ch/3`;
- levelling `< ε_lev/2`.

The stored and fluctuation parts of (15) are each `≤ r_*/8`, using `R^scr e^{−μD_f/4} ≤ R`. The identity (17) is right. The two "Outstanding" points are correct observations:
- the triangle bound (14) does not localize to the support of the source difference;
- `ℓ_m` is unbounded at fixed `θ_{i−1}`, from the frame with `b ∈ [λ, B̄]`.

**Lemma 6.**
- The formula is draft Proposition C's (`nl1-L-draft.md` L136–L142).
- The first splitting `(W, 0)` gives `B = 0`.
- The second splitting `(I, (iη)^{−1} Log W)` has `𝐔 = W`, and `M(W)(c_0) = U[c] = e^{iLtT_3}` for flat constant links (SA average (5): flat loop factors are `I`). So `B = LtT_3`, `Tr B² = 2L²t² > 0`, and `f ≠ 0`.
- ST1 §1 requires "equality at two real splittings of one pair" (`st1-r3.md` L120).

The lemma is correct. ST1 r3 L185 independently records the same counterexample. Necessity of Tq is properly withdrawn.

**D4 and Theorem 7.**
- The induction is a correct reduction.
- Cauchy's formula is integrated against the (18) majorant on a compact polydisc. Normal convergence passes holomorphy to the sum.
- Borel dependence and overlap agreement come from CI-form.
- The CI-maps hypothesis supplies everything in Theorem 4 except the old bounds, and CI supplies those.
- The stage-cost remark checks: ST1 (18) gives `w(j) = β_s r_0(j)/(16N)`, so the cost is `∝ N(θ_j)/C_0`.
- The counterexamples check: the pairing `1/[2n(2n−1)] ≤ 1/[n(n+1)]`, the dyadic harmonic blocks `≥ ½`, and `(2−z_2)^{−1}`.

**Sources.** I read every cited locator except those listed as not opened below, and each reading is confirmed:
- **SA (`ym4.tex`; its line numbers match the cited `YM4_sketch_500.tex`).**
  - 4006–4012: B4 is a source/coupling box.
  - 4863–4885.
  - 5999–6048: running minimum; `α_{ι,j} = C_ι θ_j^{−1/2}(log θ_j)^q` at 6033.
  - 5762–5825: R9 holomorphy; wall-component splitting; `Ce^{Cκ̄} sup|B'|`.
  - 10354–10410.
  - 6141–6158: lift; inclusions are "analytic inclusion hypotheses" at 6156.
  - 6180–6214: hull convention and (R23).
  - 14276–14315: "holomorphic on their declared complex fluctuation boxes" at 14314.
  - 14404–14412.
  - 14640–14657.
  - 14758–14768: normal convergence from positive majorants at 14763.
  - 15150–15174: `ρ ≥ c_R α/δ`; `e^{−Cκ̄}` loss at 15165; membership not proved by the Cauchy argument.
  - 15721–15745.
  - 15784–15820.
  - 17518–17566: kept-form oscillation at 17564.
  - 17648–17654.
  - 17270–17278.
  - 17797–17831: supremum inside the integral.
  - 17882–17892: "O(k−j)" at 17887–17888.
  - 17982–17997.
  - 19466–19493: order `M ≺ (A_1, A_0, C_0, C_1, …) ≺ γ`; `q−p_0 > Cr` at 19490.
- **CA-II.**
  - 79910–79965: carried-background and coupling-profile brace.
  - 79985: `z^{(k)}`.
  - 79996–79997: stored/free split.
  - 80010–80011: Bałaban's derivation "is not reproduced".

  The three corrected locators are right.
- **YM3.**
  - 39230–39246: `C_𝒜 𝔟` polydisc.
  - 39296–39309.
  - 52573–52588: hull product of `s̄`.
  - 53550–53565: half polydisc.
- **CA-III.** 111381–111402: "proof incomplete" inventory.
- **CA-I.** 49495–49546 and 54280–55005: spot-checked, consistent.

Not opened: SA 14518–14560 and 14730–14757, and CA-I 48527–48578. These rows make only negative claims ("does not supply").

## 2. Findings

None of the findings is fatal. All are repairable by local edits.

1. **L60, L63, L127–L128, L153 (ST1 citation base): repairable.** "Round 3" links to `st1-draft3.md`, Claude's pass-1 draft, not to the frozen distilled `st1-r3.md` at the same commit.
   - "Round-3 Lemma 11′ for lifted cores" exists only in the draft. `st1-r3.md` replaced lifted cores by the unit-lift R1 with Lemma 9′ and Lemma 11.
   - The unlabelled "ST1 (56), (59), (60)" (L64, L259, L289) are round-2 equation numbers. In `st1-r3.md` those numbers denote different displays: (56) is the raw-exponent bound, (59) is `C_U ℓ^{2r_R} ε_m`, and (60) is the `ε_f r_0(i)` gauge bound.
   - The Tq0 branch is fully supplied by `st1-r3.md`: the Tq0 table, Lemma T/T3, Proposition R°, Lemma 4 (27), Lemma 11 (63)–(65), Lemma 13 (74), and order row 6.
   - The Tq-with-lifts branch rests on a lifted-core admission that is not in the frozen ST1.

   Repair: cite `st1-r3.md` throughout, and tag each equation with its round. Either restrict Theorem 4 to Tq0, or list the lifted-core admission (draft3 Lemma 11′) as an explicit H-ST import.

2. **L186 versus L130/L148 (symbol clash): repairable.** `𝒮` denotes the text's full source carrier. In the B row it is also SA's label in `d^♮(𝒮;X)` (SA 6191–6197, R23), which is a different object. Repair: rename the source carrier, for example `𝒮_src`.

3. **L205, L219 (symbol clash): repairable.** `C_Q = 256 e^{μC_car/2}` clashes with two other constants of the same name: ST1's AV/CURV constant `C_Q` (`st1-r3.md` L127, L163) and PAN's `C_Q(M)`. Repair: rename it, for example `C_Q^{rd}`.

4. **L205 (floor on L): repairable, cosmetic.** "Choose `L ≥ 13`" is weaker than frozen IN1, which requires odd `L ≥ 27` (`in1.md` L9) and its row-2 floor. IN1's order is declared retained, so nothing breaks. Repair: state "odd `L` meeting IN1 row 2 (`L ≥ 27`)".

5. **L169–L171 with L436–L437 (H-DR row locality): repairable, precision only.** "Its response reads only `s|_{K'}` and the source rows assigned to `K'`" should say what the L3 proof uses: the response restricted to the bonds and stencils of `K'` depends only on those data. Otherwise a component outside `K` could feed a read in `X_f`. This is SA's own splitting (5797–5801: "the equations split over the remaining components"). Repair: one sentence.

6. **L593 (Theorem 7 proof): repairable, wording.** "CI for old activities supplies H-ACT for the carried factors" overstates. CI (D4) gives the bound and the interface. The term decomposition, strip and W identification, and branches come from CI-maps, which imports Theorem 4's hypotheses other than the old bounds. The theorem's statement is right. Repair: one clause.

Remark (not a defect). For kinds S, Z, E, R and B, Theorem 4 also gives PAN's original form `|F_f| ≤ b_f = ½ω_f`. The PAN Lemma 5.3(a) amendment is therefore needed only for the kept forms K and the W terms.

## 3. Verdict

Every numbered statement is proved exactly as stated, under the imports named in its Result:
- Theorem 4, with `c_R = 1`;
- Lemmas 1, 2, 3, 5 and 6;
- Corollary 4.1;
- Theorem 7.

The masking and centring construction gives L3 and L5. The Schwarz/recentring step shows that the oscillation form of L6 suffices for PAN Lemma 5.3(a). Lemma 6 correctly refutes Proposition C's necessity claim through the real tie. The constants rule holds: every constant is fixed before `κ`, independent of `M` and `κ̄`, and every loss sits in late `C_0`, `C_1` or coupling ceilings. The six findings are citation, notation and wording repairs. Finding 1 is the only one with content: the Tq-with-lifts branch cites a draft-only lemma. The Tq0 branch is complete against frozen ST1 r3. ADVANCE as a conditional result, after the repairs.

Checked line by line by Claude (fresh session).
