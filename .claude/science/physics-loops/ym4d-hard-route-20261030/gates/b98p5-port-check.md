lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-08T08:52Z

# Check of library/b98p5.md sections 2.1-2.5 (queue row 446, b98p5-port-check)

Provenance: Claude Opus 5.5, max effort, commit 9fcc75acc, branch claude/ym4d-hard-route. One line-by-line reading by one model of another model's text (Codex gpt-6-astra). Not an audit. No numerics were run.

Sources read. CMP 98 printed pp. 22-24, 27-28 and 30-42 as page images (`~/ym4d-papers/png/`), using the OCR only to locate them. CMP 109 printed pp. 251-254, rendered from the local PDF. The CMP 96 OCR at (2.45)-(2.46), for the distance. In this repository: library/b98p5.md sections 1-2.5, a1-balaban.md (3.7)-(3.9), a3-balaban.md 715-745, b98.md Lemmas 2, 6 and 7, and b98p5-r3.md sections 4.3 and 4.6. The account at `31a47c543775`, fetched by URL into a scratch folder; SHA-256 of SA, CA-I and CA-III agree with the note's table. Line numbers below are those files. Credit: Tadeusz Bałaban for the construction and the proof method; Ethan Sussman and Levent Alpoge, with Claude and Codex as text authors, for the account.

## Verdicts

| Step | Verdict |
|---|---|
| 2.1 map, subtraction, read set | ADVANCE |
| 2.2 one-step bounds (7)-(10) | ADVANCE |
| 2.3 moving reference (11)-(15) | ADVANCE |
| 2.4 density, Cauchy, transposes (16), bound (4) | ADVANCE |
| 2.5 relation to the real proof; symmetrised map; plain average | ADVANCE, with two steps REVISE (R1, R2 below; each repair is written out) |

First failing step: none. Sections 2.1-2.5 prove (3) and (4) of the note as an implication from (11) at every row, on the stated balls, with the explicit constants (2). Every constant in (2) depends on (d, L, N) only, and the order of choice p, n_*, r, B_*, ρ, e_*, C_*, C_{α,κ} is not circular. This check does not reach (11) on the account class (the note's Section 3), or Sections 1, 3 and 4.

## 2.1 The map, its subtraction, and its complete read: ADVANCE

Checked against the printed formulas, not the OCR.

- The comb map M in (5) is CMP 98 (42), p. 23, and its iterate is (43), p. 24: `Ū_c = exp[i Σ_{x∈B(c_-)} L^{-d} (1/i) log U(Γ_{c,x})U(c)^{-1}] U(c)`.
- The site factor m_W(a;y) is Bałaban's `\overline{R_{0,y}V_1}` of (110), p. 34, with (62), p. 28. The right side of `P_{e^{ia}W}(γ) P_W(γ)^{-1} = Π_{b⊂γ} R(W(γ_{y,b_-})) e^{ia(b)}` (ordered) is the product of CMP 98 (58). I rederived the identity, which is b98.md (11), and the note's reverse-edge rule agrees with it.
- F_W(a) is (1/i) log of CMP 98 (89), p. 31 (= (63), p. 28), with V_0 = W, V_1 = e^{ia}. Indeed `R̄_{0,c} = R((V̄_0)_c)` (CMP 98 (59); CA-I 24268) turns `g(c_-)^{-1} \overline{V_1V_0}_c (V̄_0)_c^{-1} R̄_{0,c} g(c_+)` into `g(c_-)^{-1} \overline{V_1V_0}_c g(c_+) (V̄_0)_c^{-1}`, which is the bracket in (5).
- Recursion (6) is CMP 98 (91) and CA-I 24320-24326; the quotation is at CA-I 24324-24326 (the note cites 24323-24332, which contains it). q_c = a_j(c) is Bałaban's Q_j(U_0, ηA, c) = (1/i) log(Ū_1^j)_c of Proposition 4, p. 38. R_c in (1) is Bałaban's C_j(U_0, L^jηA, c) of (150).
- I rederived the factorisation `M(e^{ia}W) = (e^{iF_W(a)} M(W))^{m_W(a)}` with `V^u(c) = u(c_-)V(c)u(c_+)^{-1}`, and the covariance `F_{W^u}(a^u) = Ad(u(c_-)) F_W(a)` with `a^u(b) = Ad(u(b_-)) a(b)`. Both hold wherever the principal logarithms are defined.
- Read set: CMP 98 p. 24 and p. 31, and CA-I 24332-24336, state that the value on c reads only bonds in B^k(c_-) ∪ B^k(c_+). The note's backward induction proves it: for odd L with centred blocks, B^{m+1}(y) is the union of the B^m(z), z ∈ B(y), and each straight segment [x, x'] lies in B(c_-) ∪ B(c_+).

No defect. The note's claim that its extension of the potential off E_c needs no cutoff derivative is correct, because the map never reads outside E_c.

## 2.2 Fixed one-step bounds: ADVANCE

I recomputed each step.

- (7): the multinomial majorant gives `‖Π e^{X_i} − I‖_F ≤ e^t − 1 ≤ 2t` for t ≤ 1/4. The product has no identity factor after expansion, so ‖I‖_F = √N never enters. The log series gives the second bound.
- (8): a closed loop in (5) has at most d(L−1) + 2L ≤ 8dL = p bonds. I assembled the bracket of F as one ordered product of exponentials. Its factors are m(c_-)^{-1}, e^{Y_V}, P_V(c), m(c_+), P_W(c)^{-1} and e^{-Y_W}, and their total length is at most 355pr. This is below the note's count of 1408pr. So ‖F‖ ≤ 4·355pr < 2^{16}pr = 2^{-8}, and ‖log m‖ ≤ 128pr. Every intermediate argument stays within 1/2 of I.
- (9): at W = I, a = 0 the internal connector terms cancel against the two site factors. What remains is S_L. Its row sum is L^{-d}·L^d·L = L. In its column sum a fixed μ-bond is counted once for each of its L starting offsets, which gives L^{1-d}. This is CMP 98 (125), p. 36, in angle units (the factor L^{-(d+1)} there is per length).
- (10): the second directional derivative of F is at most r^{-2} on the 2r ball, because sup‖F‖ < 1 and the circles stay in the 8r polydisc. The note's 2r^{-2} is also valid. The entries are bounded as colour operators through unit colour vectors, so no colour-dimension count is needed. A one-step row reads fewer than 4dL^d < n_* bonds, and a fine bond is read by at most 2d rows. Then 2n_*r^{-2} ≤ L·B_* and 2n_*r^{-2} ≤ L^{1-d}B_* give the first two lines. The third line follows from the Cauchy bound on the first derivative, ‖log m‖ ≤ ‖a‖/r ≤ B_*‖a‖.

## 2.3 Moving the reference without a depth factor: ADVANCE

- (12): I rederived `M^m(e^{iηB}) = (e^{ib_m})^{g_m}` with `g_{m+1} = g_m|z_m`, using M(I) = I and `(V^u)^v = V^{vu}`.
- (14): with `a_m = Ad(g_m) â_m`, the covariance identity of 2.1 gives `â_{m+1} = Ad(g_{m+1}^{-1} g_m) F_{e^{ib_m}}(â_m) = Ad(z_m^{-1}) F_{e^{ib_m}}(â_m)`. The comb map is covariant under G^c-valued gauges algebraically.
- The bootstrap and the bounds: ‖b_0‖ < ρτ_0. Each step costs at most L·e^{14B_*ρτ_m}, Σ_{m<j} τ_m < 1/(L−1), and 14B_*ρ = 14r/2^{20}. The inputs of (10) satisfy ‖b_m‖ + ‖â_m‖ ≤ 10ρτ_m ≤ 2r. These give (13) and (15) with the factors 3/2 and 2, so 3L^j ≤ 8L^j.
- Hypothesis (11) is a separate gauge and B for each row c. The bound in (15) is a bound for the globally extended map e^{iηB^{(c)}}. Only its row-c entries are used later, and they agree with the true map because of the read set of 2.1. So the per-row hypothesis is enough. The same holds for A: replace A by 1_{E_c}A before the sup-norm bootstrap. This leaves q_c unchanged (2.1) and makes ‖â_0‖ ≤ uτ_0 a global bound. The note leaves this step implicit, and it is a one-line addition.

## 2.4 Density before Cauchy; then the transpose: ADVANCE

- Each counting entry is at most the column norm: η·8L^{(1-d)j} = 8η^d s_c^{1-d}. For the flat main term this is sharp up to a fixed factor. The flat column sum is exactly L^{(1-d)j}, and a fine μ-bond has nonzero weight in at most two μ-rows. So s_c^{1-d} is the true scaling, and it agrees with the a1-balaban.md (3.9) kernel bound C_3 r s_j^{1-d}.
- The Cauchy circles stay in the 4ρ ball: the radii reach s_c‖·‖ ≤ 2ρ for one circle and 3ρ for two. The value bound is |R_c| ≤ 4ρ^{-1}(s_c‖A‖_F)². The note's 64ρ^{-2} is valid, and 8ρ^{-2} would do.
- Conversion to (3): from the account's conventions (CA-I 12739-12771), |A|_{(-1)} = sup ℓ(b)|A(b)|. Every bond of E_c has local scale ℓ(b) ∈ {s_c, s_c/L}. This holds because the rows are the interior and outward bonds of SA 9607, and SA 9625 omits the inward bonds, and an outward row's outer block B^j(z) consists of interior bonds of height j−1. Hence s_c‖A‖_{∞,E_c,F} ≤ L√N |A|_{(-1)}. With e_* = ρ/(16L√N) and C_* = 2^{24}N²dL^4ρ^{-2}, each line of (3) holds, the worst being 64ρ^{-2}L²N^{3/2}.
- (16): the formula is correct for the pairings of CA-I 12756-12760 (η^d fine, ℓ_j^d on Λ_j). A fine bond lies in at most 2d rows of its own height and at most 2d outward rows of the next height, so in at most 4d carriers. Hence s_c/ℓ(b) ∈ {1, L}.
- Weight ratio: d(·,·) is CMP 96 (2.46), printed p. 231. CMP 99b p. 397 cites it, printing the number as (2.36). It is the infimum over contours that use Λ_j-bonds in layer j. The centres read by one row are within about d(L+2) ≤ 4dL of each other.
- Inserting these facts gives at most 4d·8ρ^{-1}N^{3/2}L^{1+|α+1|}e^{4dLκ}, which is below C_{α,κ}. The proof uses only |v|_{(-1),w}, so the N^w(v) in (4) is weaker than what is proved. α = −4 agrees with (J5) at CA-I 13775-13781.

## 2.5 Relation to the real proof, the symmetrised map, the plain average: ADVANCE (R1, R2 REVISE)

- The a1-balaban.md (3.9) coefficient is CMP 98 (154), p. 41, as printed. With C_3 ≥ 6C''_1, 4dC'_1αL^{-1} ≤ 1/4 and the bracket squared ≤ 3, it is at most 1 − L^{-2} + L^{-2}/4 + L^{-2}/2 = 1 − L^{-2}/4. The quotation is accurate.
- The symmetrised map is CMP 109 (0.10)-(0.12), printed pp. 253-254. The note's M_sym is (0.12), with U(x', c_+) = U(c_+, x')^{-1} by (0.5). Its site factor is SA (PX141), SA 11516-11522, and its outer map is SA (QC3). (17) is (0.10) with general convex weights. I checked the majorant −log(2−e^t) − t, its derivative 2(e^t−1)/(2−e^t) ≤ (8/3)t on t ≤ 1/8, the self-map of the 2x ball (x + 72x² ≤ 2x) and the Lipschitz bound 48x ≤ 1/2. At zero the derivative is the arithmetic mean, so (9) is unchanged.
- The plain average (input to CA-III 36721, read at CA-III 36720-36722): with G_j the ordered product of the site factors, M^j(e^{iηA}Ũ)(c) = G_j(c_-) e^{ia_j(c)} W_j(c) G_j(c_+)^{-1}. Its logarithm relative to A = 0 is at most about 5u. Cauchy at radius ρ/(s_c‖v‖) then gives a directional derivative of at most 30 s_c‖v‖_{∞,E_c,F}, below C_* s_c‖v‖_{∞,E_c}. Converting to the multiplicative direction δU = iηvU costs at most 2 through dexp.

### R1 (REVISE). Covariance of the symmetrised inner mean under G^c-valued gauges

*Step.* "Uniqueness gives covariance on the common logarithm domain." For the comb map, covariance is algebraic. For the symmetrised map, (12) and (14) need T_{V^g} = g(y) T_V g(x)^{-1} for the non-unitary g_m = Π z_i. r3 §4.6(c) needs the same for its G^c-valued w.

*Gap.* If Z solves (17) for {X_i} with ‖Z‖ ≤ 2x, x = max‖X_i‖, then Ad(g)Z solves (17) for X'_i = Ad(g)X_i, because (17) is conjugation-covariant. But when ‖Ad g^{±1}‖ ≤ 2, ‖Ad(g)Z‖ can reach 8x', with x' = max‖X'_i‖. That lies outside the ball ‖Z‖ ≤ 2x' where the note proves uniqueness.

*Repair.* Let x' ≤ 1/256. On ‖Z‖ ≤ 8x' we have t ≤ 9x' ≤ 9/256 < 1/8, so ‖D_Z E‖ ≤ 16t ≤ 144/256 < 1. The right side of (17) is then a strict contraction on that ball. Hence it has at most one solution there, and the mean of {X'_i} is Ad(g)Z. The relative transports in (8) are of order pr, so x' ≤ 1/256 holds with room, at every level of (14) and on r3's data. Covariance of T, of the site factor of (PX141) and of M_sym follows from this by anchoring at one path.

### R2 (REVISE). Constant in the plain-average site factors

*Step.* "The sum of their logarithms is bounded by B_*Σ_m‖a_m‖." Line three of (10) holds only at backgrounds e^{ib} with b small. At the moving reference W_m = (e^{ib_m})^{g_m}, the site factor is m_{W_m}(a_m) = Ad(g_m) m_{e^{ib_m}}(â_m). So ‖log m_{W_m}(a_m)‖ ≤ 2B_*‖â_m‖ ≤ 4B_*‖a_m‖.

*Repair.* Replace B_* by 4B_*. The sum is still at most 16B_*u/(L−1), which is uniform in depth and tiny. The bound C_* s_c‖v‖ is unchanged.

## Source notes (they break nothing)

- CMP 98 (156)-(157) can be read in full on printed p. 42. (156) is `|δQ_k(U_0,ηA,c)/δA_b| ≤ 1 + 2C'_1α_0 + C_3|A| < 1 + 2C'_1α_0 + C_3α_1`. (157) is `|δC_k(U_0,A,c)/δA_b| ≤ C_3|A| < C_3α_1`. Only the OCR is damaged, although the note calls the display "damaged" in Sections 1 and 2.5. The first-derivative line of (3) replaces the leading 1 + 2C'_1α_0 by C_*. Its R-lines have the form of (157). A consumer that needs a leading coefficient near 1 is not served by (3). Neither covered use of b98p5-r3.md needs one.
- The account labels B98-P5 "printed without proof" (CA-I 13175-13196, quoting CMP 98 p. 43: "The formulations are obvious"). For the account's own map, CMP 109 p. 254 says the CMP 98 results hold "in most cases unchanged; in others only minor and obvious modifications are needed." Section 2.5 supplies that modification for Proposition 5. So this note is a proof of a step that both sources assert without proof, not a re-proof of a proved statement.

## The covered uses in b98p5-r3.md

- r3 §4.3 (CA-II 5.8:lem-averaging-correction) reads the following from Sections 2.3-2.4: holomorphy on u < 4ρ; on u ≤ ρ, the value bound 4ρ^{-1}u² and the density 8ρ^{-1}u s_c^{1-d} of DR_c. Each of these holds as recomputed above.
- r3 §4.6 (CA-III 36721) reads the plain-average row bound of Section 2.5, which holds with the constant of R2. For the symmetrised map, its step (5) also needs covariance under the G^c-valued gauge w. The reason it gives ("convergent series") covers the comb map but not the implicit inner mean. R1 supplies that covariance, since there ‖Ad_w^{±1}‖ ≤ 2 and the logarithms are small. This is evidence for the owner of b98p5-r3.md.
- The other inputs of those uses are outside this check: Corollary 3.5 and the frame giving (11), and CMP 102 Theorem 1 and Proposition 9.

## What this check does not show

It does not show (11) on the account class 𝔖, which is the note's open carrier lemma of Section 3. It also does not cover Section 1's orbit-extension clause, the use check of Section 4, or any step of b98p5-r3.md. Holomorphy in the background twist 𝔞 is shown here only through B; the map from 𝔞 to B is Section 3. Everything verified here is an implication from (11) at every row.

Checked line by line by Claude (Opus 5.5).
