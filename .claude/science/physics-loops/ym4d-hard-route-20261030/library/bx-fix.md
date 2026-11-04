lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T12:52Z

# bx-fix: check of `bx.md`, and (BX) on a Hölder core (row 210)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session; checkout `6d040d5ee`. Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775` fetched by URL into a private scratch folder (sha1 `107abaef…8348885`, 32992 lines). Balaban CMP 109 read from `~/ym4d-papers/cmp109.txt`, pp. 276–277 and 284–285. Research text, not an audit; it grants no status. Proved by Claude, not yet checked by the other model.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the pointed-window theorem (SA 13426–13866, (PW1)–(PW15)), the pair class (R4)–(R6) (SA 5650–5730) and the box package (SA 15821–15826). Tadeusz Balaban for the explicit Hölder hypothesis on the substituted field (CMP 109, (3.31)–(3.32), p. 276–277, used for (4.17)–(4.18), p. 285) and for the averaging bounds of CMP 98 (rebuilt in `a1-balaban.md` 3.5, 7.1). OpenAI Codex for `bx.md`, `wf7-bf.md`, `dec-field.md`.

No numeric job was run. Every step below is by hand.

## 1. Check of `bx.md` (Codex), line by line

**Verdict: ADVANCE. The counterexample is correct.** Checked line by line by Claude, first failing step none. (BX), as `b2-extract.md` Section 7 states it, fails on the full admitted half-radius core. The input is admitted, and its box datum violates the affine remainder bound for every uniform constant. Codex's scope statement is also right: this refutes neither SA's theorem given (PW6) nor B4's (19).

**Section 2 (the missing input).** Correct. (R4) bounds curvature, |A'|, |∇_U A'|, |𝐉| and a real-gauge |A|, |∇A| (SA 5650–5680). (R5)–(R6) bound tower curvatures and currents (SA 5690–5716). No clause bounds a Hölder seminorm, so none implies (PW6) (SA 13560–13567). (PW7)–(PW13) are derived from (PW6) at SA 13582–13722. Balaban's (3.31) is a hypothesis on the class of substituted fields A, and (3.32) is derived from it; CMP 109 p. 285 uses (3.32) for (4.17)–(4.18). Confirmed in the scan.

**Section 3 (the input is in the core).** Each step was redone.

1. *Simple clauses.* In Codex's splitting P = (1, A, 0), so U = 1 and 𝐔 = e^{iηA}. Then |∂U − 1| = 0 and the real-gauge potential is 0. All matrices lie in exp(iℝT), so the plaquette holonomy is exp(iη² curl A). Also |cos(u+v) − cos u| ≤ |v| gives |curl A| ≤ πεa and |∇A| ≤ πεa in level-k units. So |∂𝐔 − 1| ≤ πεaη² < α_0η² once πεC_α < 1. |A'| ≤ εaσ and |∇_U A'| ≤ πεa are below α_1, since a ≤ C_αα_0 and Mα_0 ≪ α_1. 𝐉 = 0.
2. *Tower clauses.* `a3-close.md` Lemma T, Step 1, applies to any real field with curvature at most a' in level-p units. Here 𝐔 is real with a' = b_p = πεaτ², τ = L^{p−k}. Step 1 gives |∂U_n − 1| ≤ BC_1L²b_pη_p² and |J(U_n)| ≤ BC_1L²b_pL^{2(n−p)}. These are below a quarter of the (R6) radii a_0τη_p² and a_0τL^{2(n−p)} once KπεC_α < 1/4, K = BC_1L², because τ² ≤ τ. The towers of U = 1 are 1. So Codex's (3) holds. It avoids Lemma T's complex Step 3, which is not needed for a real field.
3. *Units, box clause.* Passing to level-(k+1) units multiplies these bounds by fixed powers of L. One further fixed decrease of ε covers them.
4. *Zero response.* With B' = 0, the zero field solves R9: W_s(0) = 0 and 𝒞(0) = 0. Proposition 5.1 of `dec-field.md` gives a unique solution in its ball. So 𝐇 = 0 and 𝐔_{t,ν} = U on the whole disc.
5. *Torus.* The period 2σ of (1) is 2L bare steps. The torus side N_kL^k (bare) is divisible by 2L when N_k is even. So (1) is periodic.

**Section 4 (the datum violates (BX)).** Each step was redone with (R3).

1. *Direction 2.* A_2 does not depend on x_2. So the contour from c_+ to x' is the translate of the contour from c_− to x, with equal transport. Hence U(c_−,x)U(x',c_+) = 1. The straight segment contributes iσA_2(x_1), and U[c]^{−1} contributes −iσA_2(σn_1). Averaging over x = σn + ηr gives log 𝓜(U)(c) = iσL^{−1}Σ_{r_1}A_2(σn_1 + ηr_1). Since cos(πn_1 + πr_1/L) = (−1)^{n_1}cos(πr_1/L), this is iβ(−1)^{n_1}T with β = εaσ²c_L. Every cos(πr/L) with |r| ≤ (L−1)/2 is positive, and the r = 0 term is 1, so c_L ≥ 1/L.
2. *Directions 1, 3, 4.* Here U[c] = 1 and the straight segment sees no A. Each contour contributes iηr_2 times a function of (n_1, r_1), because it crosses direction 2 at x_1 ∈ {σn_1, σn_1 + ηr_1}. The block sum over the symmetric range of r_2 vanishes.
3. *Axial gauge.* With g(n) = e^{iβn_2T}, B̂_2(n) = β[(−1)^{n_1} − 1]T and B̂_1 = B̂_3 = B̂_4 = 0. This is exactly the gauge of (PW7): B̂_1 ≡ 0, B̂_2 = 0 on {n_1 = 0}, B̂_3 = B̂_4 = 0. The second difference in n_1 at 0 has norm 4β. Every affine ℓ_F has zero second difference.
4. *Inequality (5).* The bond midpoints (0,½,0,0), (1,½,0,0), (2,½,0,0) lie within 3 of z = 0. The weights 1, 2, 1 sum to 4, and 4·3^{1+h} ≤ 36, 4·4² = 64. With a/r_{B,1} ≤ Cρ_1 ≤ C√k (WF1), the right side of (5) tends to 0 as k → ∞, while the left side 4ε/L is fixed.
5. *Other axial orderings.* The plaquette holonomies at 0 and e_1 are e^{∓2iβT}. Their transports to z are gauge covariant up to one common conjugation, and 2|sin 2β| ≥ 2β. An affine-plus-E form would make both logarithms equal to one constant curl up to C[aσ^{2+h} + r_B^{−1}a²σ⁴ + a²σ⁴]. Division by aσ² gives the same contradiction.

**One addition (not a defect).** The obstruction does not depend on the splitting or the gauge. The curvature itself is F_{12}(x) = −c_L'εa sin(π(x_1 + η/2)/σ)T with c_L' = 2L sin(π/2L) ≥ 2, so it changes sign over the distance σ. Section 2.3 shows that every gauge with small potential then has a gradient Hölder seminorm of order εaσ^{−α}. So the repaired domain excludes this input.

## 2. The repair: a Hölder clause (H) in the core

### 2.1 Choice

Two repairs were proposed: restrict the step's input to scale-(k+1) critical pairs, or add a Hölder clause. **I take the Hölder clause.** Reasons, on evidence:

- Both repairs need the same two analytic facts. These are a Hölder bound for the critical map (T4's Hölder member) and a Hölder bound for the fluctuation response. Criticality is only used through the first fact.
- The clause is one explicit local inequality, like (R4). It is kept under restriction to Y ⊂ X, under real gauge transformations, and under the torus translations and hypercube group (so `ti-2.md`'s symmetric setting is kept). A critical-input domain would depend on a choice of tower and box for each activity.
- It is Balaban's method. His class U^c_j (CMP 109 (1.11)–(1.16)) is SA's (R4)–(R6) and has no Hölder clause. He imposes (3.31) on the field that is substituted, then derives (3.32). Here the same bound sits in the core, so that the induction over steps carries it.

### 2.2 Definition

Fix the exponent α_H ∈ (0,1) of (WF1). For a bond field f on a cube D (fixed gauge, ordinary lattice differences), put [f]_{α,D} := sup |f_•(x) − f_•(x')| / |x − x'|^α. The supremum runs over x ≠ x' in D with the same component labels •, and |·| is the Euclidean distance between base points.

**(H) at radii (a_0, a_1).** A level-ℓ triple P = (U, A', 𝐉) on X satisfies (H) if every cube D ⊂ X of side at most C_box LM has a unitary gauge g on D with U = (e^{iη_ℓ A_r})^g, such that in level-ℓ units
\[
 |A_r|,\ |\nabla A_r|,\ [\nabla A_r]_{\alpha_H,D}<C_{\rm pot}Ma_0,\qquad
 [\nabla A'']_{\alpha_H,D}<a_1,\quad A'':=\operatorname{Ad}(g^{-1})A' .
\]
The first two bounds are the real-gauge clause of (R4). The new content is the two Hölder bounds, in the same gauge. In layered position the units are the ambient local units, as for (R4) (`wf-c.md` Theorem A (A1)).

**The repaired core** is U^H_ℓ(X; a_0, a_1, a_2) := U°_ℓ(X; a_0, a_1, a_2) ∩ {P satisfies (H) at (a_0, a_1)}. The inequalities are strict and the lattice is finite, so the set is open. (H) is convex in A' at fixed U and g, like the other simple clauses.

### 2.3 Codex's input is excluded

Work in level-k units with the input (1) of `bx.md`. In the original gauge the (1,2)-plaquette curvature is F(x) = −c_L'εa sin(π(x_1 + η/2)/σ)T, with c_L' := 2L sin(π/2L) ∈ [2, π]. Take x, x' with x_1 + η/2 = σ/2 and x'_1 + η/2 = 3σ/2, so |x − x'| = σ and F(x') = −F(x), |F(x)| = c_L'εa.

Let g be any gauge on a cube containing x, x', with potential B' of size |B'| ≤ b_0. The plaquette logarithm in the new gauge is η²Ad(g(x))F(x), and it equals η²(curl B' + Q) with |Q| ≤ Cb_0². The straight path from x to x' has L bare bonds and A_1 = 0, so |g(x)g(x')^{−1} − 1| ≤ 2σb_0. Hence
\[
 2[\nabla B']_{\alpha}\sigma^{\alpha}\ \ge\ |\operatorname{curl}B'(x)-\operatorname{curl}B'(x')|
 \ \ge\ 2c_L'\varepsilon a(1-C\sigma b_0)-2Cb_0^2\ \ge\ c_L'\varepsilon a ,
\]
once σb_0 and b_0²/(εa) are small. The radii make b_0 ~ Mα_0 and a ~ α_k, so b_0²/(εa) → 0. So [∇B']_α ≥ c_L'εa/(2σ^α), which is unbounded as k → ∞. In any splitting, the potential w = A'' ⊞ A_r of 𝐔^g has [∇w]_α ≤ [∇A'']_α + [∇A_r]_α + (smaller terms). So one of the two Hölder bounds of (H) fails at level k+1, in every real gauge, for all large k.

### 2.4 Named inputs

| label | statement used | state |
|---|---|---|
| [T4] | `a3-derivative.md` Theorem 4 at U_0 = 1 for the Landau map 𝓗_T of a Rule W box tower T: holomorphy on {sup\|B\| < r_B}, first response \|∂_{B(c)}Z_y(B)\| ≤ C_1e^{−θd(y,y_c)} at every datum of the polydisc in the pair norm (SA (PW2)), its Hölder member 7.4, and uniqueness of the critical orbit modulo residual gauge | proved, conditional on P81, P82°, M1; at U_0 = 1 these reduce to the flat package (`o1-decoupled.md` 4.2 [Φ], rows 89, 95, 99) |
| [AV] | `a1-balaban.md` 3.5 (3.7) with 7.1: the j-fold actual mean on a double block in one layer is 𝓠_j(w) + 𝓒_j(w), with 𝓠_j the flat linear map, 𝓒_j holomorphic on {sup\|w\| < r_0} in double-block units, sup\|𝓒_j\| ≤ C_Qr_0², 𝓒_j(0) = 0, D𝓒_j(0) = 0, constants independent of j | implication, gated as cited there |
| [9.3] | `a1-balaban.md` (9.3): exact restriction of a critical field to an admitted smaller tower, mod residual gauge | gated |
| [PW], [NL] | `dec-field.md` Section 5 | open premises |
| **[PW-H]** | **the Hölder member of [PW]**: H_1(s), H(s): Y_w → X_w and 𝔊(s): F_w → X_w also satisfy sup_y w(y) ξ_y^{2+α_H}[∇_𝐔 a]_{α_H,y} ≤ B‖input‖, with the covariant comparison along straight paths at separations at most ξ_y, uniformly on the whole polydisc | **open; new here** |
| (20), (ER8u), (UR), (YA) | as in `b2-extract.md` Section 7 | as recorded there |

## 3. Two lemmas on regularity

**Lemma 0 (Hölder member of the response).** Assume [PW], [NL], [PW-H]. Write [a]_{H,w} := sup_y w(y)ξ_y^{2+α_H}[∇_𝐔a]_{α_H,y}. For b = ‖B'‖_{Y,w} < cB^{−4}, with c ≤ min{r_0/4, 1/(16C_W), 1/(16C_C)} as in `dec-field.md` Proposition 5.1, the R9 field satisfies [𝐇]_{H,w} ≤ 2Bb on the whole polydisc.

*Proof.* Use the fixed points of the proof of Proposition 5.1: 𝐇 = h, h = a − H𝒞(h), a = H_1B' − 𝔊W_s(a), with ‖a‖_{X,w} ≤ R := 2Bb and ‖h‖_{X,w} ≤ 2R. [NL] with v = 0 gives ‖W_s(a)‖_{F,w} ≤ C_WB²R² and ‖𝒞(h)‖_{Y,w} ≤ 4C_CR². [PW-H] applied to each term gives
\[
 [h]_{H,w}\le B b+B\,C_WB^2R^2+B\,4C_CR^2
 = Bb\,[1+4b(C_WB^4+4C_CB^2)]\le2Bb ,
\]
since 4bC_WB⁴ ≤ 4cC_W ≤ 1/4 and 16bC_CB² ≤ 16cC_C ≤ 1 with B ≥ 1. Separations above ξ_y cost a factor 2, by twice the gradient bound. □

So in the window, with h := (η_k/η)(t+νζ)𝐇_k and |t+νζ|δ_k ≤ (s_k + c_ν)α_k as in `wf-c.md` Theorem A, (A1):
\[
 \xi_y|h|+\xi_y^2|\nabla_{\mathbf U}h|+\xi_y^{2+\alpha_H}[\nabla_{\mathbf U}h]_{\alpha_H,y}\le C(s_k+c_\nu)\alpha_k\quad\text{at top-layer points.}\tag{3.1}
\]

**Lemma 1 (averages of Hölder fields are Hölder, uniformly in depth).** Work in level-j units, bare mesh η_j = L^{−j}. Let Λ be a cube, and w a complex su(2)-valued bare potential on the bonds of Λ with
\[
 \sup|w|\le b\sigma,\qquad\sup|\nabla w|\le b\sigma^2,\qquad[\nabla w]_{\alpha,\Lambda}\le b\sigma^{2+\alpha},\qquad 0<\sigma\le1,\ 0<b\le b_V .
\]
For a level-j bond c whose read set Δ(c) (its double block) lies in Λ, put B(c) := (1/i) log 𝓜^j(e^{iη_jw})(c), with node values in the gauge of w. Then B is holomorphic in w, and for such c, c' = c + d (d a level-j lattice vector) and unit lattice vectors e,
\[
 |B(c)|\le2b\sigma,\qquad|\nabla_eB(c)|\le C_Vb\sigma^2,\qquad|\nabla_eB(c')-\nabla_eB(c)|\le C_Vb\sigma^{2+\alpha}|d|^\alpha .
\]
Here ∇_e is the level-j difference. C_V and b_V depend only on L and α, not on j, σ or the depth.

*Proof.* By [AV], B = 𝓠_jw + 𝓒_j(w). 𝓠_j is linear and |𝓠_jf| ≤ 2 sup|f| (scaling limit of the bootstrap bound |log 𝓜^q(e^{iηw})| ≤ 2t_q sup|w|, `o1-decoupled.md` 4.3). The same bootstrap gives |B| ≤ 2bσ. The mean at c + e reads Δ(c) + e by the same formula. So 𝓠_j and 𝓒_j commute with level-j translations τ_e: B(c+e) = 𝓠_j(τ_ew)(c) + 𝓒_j(τ_ew)(c). Cauchy's estimate on the ball of radius r_0, applied on its half ball, gives |D²𝓒_j(v)[f,f']| ≤ C_2 sup|f| sup|f'|. With D𝓒_j(0) = 0 this gives |D𝓒_j(v)f| ≤ C_2 sup|v| sup|f|. Take b_V ≤ r_0/8, so all arguments below stay in the half ball.

*Differences of w.* Put g_e := τ_ew − w. Along the L^j bare bonds of a unit segment, g_e(x) = Σ_m η∇_ew(x + mηe), so |g_e| ≤ bσ². The same sum gives |τ_dg_e − g_e| ≤ [∇w]_α|d|^α ≤ bσ^{2+α}|d|^α, and for unit e' the second difference Δ := τ_{e'}g_e − g_e has |Δ| ≤ bσ^{2+α}.

*First differences.* ∇_eB(c) = 𝓠_jg_e(c) + ∫_0^1 D𝓒_j(w + θg_e)[g_e]dθ. So |∇_eB| ≤ 2bσ² + 2C_2bσ·bσ² ≤ C_Vbσ².

*Second differences.* Put Ψ(θ,θ') := 𝓒_j(w + θg_e + θ'g_{e'} + θθ'Δ). Then the second difference of 𝓒_j(τ_•w) along e, e' is Ψ(1,1) − Ψ(1,0) − Ψ(0,1) + Ψ(0,0) = ∫∫∂_θ∂_{θ'}Ψ. Here ∂_θ∂_{θ'}Ψ = D²𝓒_j[g_e + θ'Δ, g_{e'} + θΔ] + D𝓒_j[Δ]. Its size is at most C_2(2bσ²)² + C_2·4bσ·bσ^{2+α} ≤ 8C_2b²σ^{3+α}.

*Hölder quotient.* ∇_eB(c+d) − ∇_eB(c) = 𝓠_j(τ_dg_e − g_e)(c) + [∇_e𝓒(c+d) − ∇_e𝓒(c)], with 𝓒 := 𝓒_j(τ_•w). The first term is at most 2bσ^{2+α}|d|^α. For the second, put t := |d| ≥ 1.
- If t ≤ σ^{−1}, walk from c to c+d by |d|_1 ≤ 2t unit steps. This bounds it by 16C_2tb²σ^{3+α} = 16C_2bσ^{2+α}t^α·(bσt^{1−α}) ≤ 16C_2bσ^{2+α}t^α, because bσt^{1−α} ≤ bσ^α ≤ 1.
- If t > σ^{−1}, use twice the first-difference bound of 𝓒: 4C_2b²σ³ = 4C_2bσ^{2+α}t^α·(bσ^{1−α}t^{−α}) ≤ 4C_2bσ^{2+α}t^α.

So C_V := 2 + 16C_2 works. □

The point of the lemma is that 𝓒_j's sup bound C_Qb²σ² is never used for the Hölder part. It would be too large by b σ^{−α}. Only its translation covariance and second derivative enter.

## 4. Lemma 2: the window datum has (PW6) on the whole disc

**Lemma 2.** Let z be a top-layer base point (ℓ(z) = k) of an old member of level j < k, σ = L^{−(k−j)}, and σ' := σ/L = ξ_j/ξ_{k+1}. Let D_z be a cube of side C_boxLM (level-(k+1) units) containing the Rule W window R_z, inside the step's domain. Let P ∈ U^H_{k+1}(D_z) at half radii (α_0/2, α_1/2). Assume [PW], [NL], [PW-H] and [AV]. Take any 0 ≤ t ≤ 1, |ν| < c_ν/s_k, |s_Δ| < e^{κ̄} and admitted B'. Let g be the real gauge of (H) on D_z. Then the level-j datum B_{t,ν}(c) := (1/i)log 𝓜^j(𝐔^g_{t,ν})(c), at level-j rows c whose read sets lie in R_z, is holomorphic in all these variables and satisfies, in level-j units,
\[
 |B_{t,\nu}|\le2a_*\sigma',\qquad|\nabla B_{t,\nu}|\le C_Va_*\sigma'^2,\qquad[\nabla B_{t,\nu}]_\alpha\le C_Va_*\sigma'^{2+\alpha},
 \qquad a_*:=C_7\big(C_{\rm pot}M\alpha_0+\alpha_1+L^3(s_k+c_\nu)\alpha_k\big).\tag{4.1}
\]

*Proof.* Work first in level-(k+1) units on D_z. Here α_0, α_1 are the level-(k+1) radii.

1. *Real part.* (H) at half radii gives |A_r|, |∇A_r|, [∇A_r]_α < C_potMα_0/2.
2. *Complex part.* A'' = Ad(g^{−1})A' has |A''| = |A'| < α_1/2 and [∇A'']_α < α_1/2. In the gauge g, ∇_UA' becomes ∇A'' + i[A_r, A''] + O(η|A_r|²|A''|). So |∇A''| ≤ α_1/2 + 2C_potMα_0α_1 ≤ α_1.
3. *Response.* Put h̃ := Ad(g^{−1})h. At top-layer points ξ_y = ξ_k = 1/L in these units. So (3.1) gives |h̃| ≤ LC(s_k+c_ν)α_k, |∇_𝐔h| ≤ L²C(s_k+c_ν)α_k, and a covariant Hölder bound L^{2+α}C(s_k+c_ν)α_k at separations up to 1/L. The potential w_0 = A'' ⊞ A_r of 𝐔^g has |w_0| ≤ C_potMα_0 + α_1. The ordinary differences of h̃ differ from the covariant ones by [w_0, h̃] terms. A straight transport over length s ≤ 1 differs from 1 by at most Cs|w_0|. The variation of [w_0, h̃] over length s is at most (|∇w_0||h̃| + |w_0||∇h̃|)s ≤ (…)s^α. Separations above 1/L use twice the gradient bound. So |h̃|, |∇h̃|, [∇h̃]_α ≤ CL³(s_k+c_ν)α_k.
4. *Composition.* Bondwise, e^{iηh̃}e^{iηA''}e^{iηA_r} = e^{iηw} with w = h̃ + A'' + A_r + R. Here R = η^{−1}Ψ(ηh̃, ηA'', ηA_r) and Ψ is holomorphic near 0 and vanishes to second order. So |R| ≤ Cη|X|², |∇R| ≤ Cη|X||∇X|, and [∇R]_α ≤ Cη(|∇X|² + |X|[∇X]_α), where X = (h̃, A'', A_r). These are below the main terms by a factor η|X| ≤ 1. Hence |w|, |∇w|, [∇w]_α ≤ a_* for a fixed C_7.
5. *Units.* In level-j units a potential gains the factor σ', a gradient σ'², and a gradient Hölder seminorm σ'^{2+α}. So w satisfies the hypothesis of Lemma 1 with b = a_* and σ', once a_* ≤ b_V, which the small radii and c_ν give. Lemma 1 gives (4.1).

Holomorphy holds because each step is a composition of holomorphic maps (Proposition 5.1 for 𝐇, [AV] for 𝓜^j). □

Lemma 2 is the step that fails in `bx.md`: there (H) is false, and no bound like [∇w]_α ≤ a_* holds.

## 5. Lemma 3: the axial expansion (SA (PW7)–(PW8), rebuilt and sharpened)

**Lemma 3.** Let B be a level-j datum on a cube Λ_j of the level-j lattice, in some gauge, with |B| ≤ b_1σ, |∇B| ≤ b_1σ², [∇B]_α ≤ b_1σ^{2+α}, 0 < σ ≤ 1. Let z ∈ Λ_j and Q_z := {x : |x − z|_∞ ≤ C_w/σ} ⊂ Λ_j, with (1 + C_w)b_1 ≤ c_3 for a fixed small c_3. Let V̂ = (e^{iB})^{g_z} be the complete axial gauge about z in comb order 1, 2, 3, 4: V̂_1 ≡ 1, V̂_2 = 1 on {x_1 = z_1}, V̂_3 = 1 on {x_1 = z_1, x_2 = z_2}, V̂_4 = 1 on {x_1 = z_1, x_2 = z_2, x_3 = z_3}. Put B̂ := (1/i)log V̂ and F_{κμ} := (1/i)log V̂_{p_{κμ}(z)} (plaquette at z, based at z). Then on Q_z
\[
 \widehat B_\mu(x)=\ell_{F,\mu}(x)+r_\mu(x),\quad \ell_{F,\mu}(x)=\sum_{\kappa<\mu}(x-z)_\kappa F_{\kappa\mu},\qquad
 |F|\le3b_1\sigma^2,\quad|\widehat B(x)|\le Cb_1\sigma^2|x-z|,\quad|r(x)|\le C_3b_1\sigma^{2+\alpha}|x-z|^{1+\alpha}.\tag{5.1}
\]
Also r = 0 on the root lines. The constants depend only on c_3, C_w and α.

*Proof.* *(a) Plaquettes in the original gauge.* For a plaquette p at x in the (κ,μ) plane, log V_p = Ψ_p(X) with X = (B_κ(x), B_μ(x+e_κ), −B_κ(x+e_μ), −B_μ(x)). Ψ_p is the holomorphic logarithm of a product of four exponentials, and DΨ_p(0)X is the sum of the entries. So log V_p = i curl B(p) + Ψ_2(X), with Ψ_2 := Ψ_p − DΨ_p(0), curl B(p) = ∇_κB_μ(x) − ∇_μB_κ(x), and |DΨ_2(X)| ≤ C|X|. Let p' be the translate of p by d. Then |curl B(p') − curl B(p)| ≤ 2b_1σ^{2+α}|d|^α. Also |X(p') − X(p)| ≤ 4b_1σ²|d| and |X| ≤ 4b_1σ, so |Ψ_2(X(p')) − Ψ_2(X(p))| ≤ Cb_1²σ³|d|. Hence
\[
 |\log V_{p'}-\log V_p|\le2b_1\sigma^{2+\alpha}|d|^\alpha+Cb_1^2\sigma^3|d|,\qquad|\log V_p|\le2b_1\sigma^2+Cb_1^2\sigma^2\le3b_1\sigma^2 .
\]
This is the non-Abelian commutator term of SA 13600–13606.

*(b) Transport to z.* V̂_p = Ad(g_z(x))V_p, and g_z(x) is the product of at most |x − z|_1 ≤ 2|x − z| comb factors e^{iB}. So |Ad(g_z(x)) − 1| ≤ Cb_1σ|x − z|. With f(p) := (1/i)log V̂_p and F = f(p_z) (g_z(z) = 1),
\[
 |f(p)-F|\le C\big[b_1\sigma^{2+\alpha}|x-z|^\alpha+b_1^2\sigma^3|x-z|\big].
\]

*(c) Comb products.* For κ < μ, the (κ,μ)-plaquette at y has V̂_κ = 1 on both of its κ-edges whenever (y_1,…,y_{κ−1}) = (z_1,…,z_{κ−1}). There V̂_μ(y + e_κ) = V̂_p(y)V̂_μ(y). Reduce x_1 to z_1 with (1,μ) plaquettes, then x_2 to z_2 with (2,μ) plaquettes at points with y_1 = z_1, and so on, until V̂_μ = 1 is reached. So V̂_μ(x) is an ordered product of n ≤ Σ_{κ<μ}|x_κ − z_κ| ≤ 2|x − z| factors e^{±if(p_i)}, with (x_κ − z_κ) signed factors from the (κ,μ) planes. The finite-product estimate |log Π e^{Y_i} − ΣY_i| ≤ C(Σ|Y_i|)² (SA 13612–13621) applies, because Σ|f(p_i)| ≤ 6|x − z|b_1σ² ≤ 6C_wb_1σ ≤ c. Hence B̂_μ(x) = Σ_i ±f(p_i) + O(b_1²σ⁴|x − z|²), and
\[
 \sum_i\pm f(p_i)=\ell_{F,\mu}(x)+\sum_i\pm\big(f(p_i)-F_{\kappa_i\mu}\big).
\]
Every |p_i − z| ≤ |x − z| + 2. So (b) gives |r(x)| ≤ C[b_1σ^{2+α}|x−z|^{1+α} + b_1²σ³|x−z|² + b_1²σ⁴|x−z|²], with |x−z| ≥ 1 off the root lines.

*(d) Absorption in the window.* For 1 ≤ |x − z| ≤ 2C_w/σ,
b_1²σ³|x−z|² = b_1σ^{2+α}|x−z|^{1+α}·b_1(σ|x−z|)^{1−α} ≤ b_1σ^{2+α}|x−z|^{1+α}·2C_wb_1. The σ⁴ term is smaller. This proves (5.1). The bound on |B̂| is the unexpanded product bound. □

This is SA's argument (credit as in the header), with two changes. The remainder is |x − z|^{1+α} rather than (1 + |x−z|)², which is the form `b2-extract.md` (BX) states. And the commutator term is absorbed only inside the window |x − z| ≤ C_w/σ, which is where Proposition W reads it.

## 6. Lemma 4: affine data are reproduced, up to a gauge direction

This replaces the finite-box comparison (PW12) for the affine part. With the tower's own boundary rows it is exact, and the box-versus-torus difference reduces to an exponentially small term.

**Lemma 4.** Work in level-j units at the flat reference. Let T be a first-rule box tower, T_0 ⊃ T_1 ⊃ … ⊃ T_j. Let K_T be the linearisation at 1 of U ↦ (1/i)log M_{𝐁_T}(U) in the chart U = e^{iηa}. Let 𝓗_T be its Landau map over 1 (Theorem 3), H_T := D𝓗_T(0), and P^T_in(B) := (1, 𝓗_T(B), J(e^{iη𝓗_T(B)})). Let ℓ^b be the bare axial affine field, ℓ^b_μ(x) := Σ_{κ<μ}(x − z)_κF_{κμ} on the bare bond from x in direction μ, and put ℓ^T := K_Tℓ^b. Then:

- (a) On a level-q row c of T (bond length ξ'_q = L^{q−j}), ℓ^T(c) = ξ'_q ℓ^b_μ(c_−). On level-j rows ℓ^T = ℓ_F of Lemma 3.
- (b) H_Tℓ^T = ℓ^b + dχ on T_0, for a site function χ vanishing at the nodes of T.
- (c) Let G_X be gauge invariant with DG_X(0) = 0, and let X and its read stencil lie in T_1. Then D²(G_X∘P^T_in)(0)[ℓ^T, ℓ^T] = D²G_X(0)[ℓ^b, ℓ^b], where ℓ^b carries zero linear current on that stencil.

*Proof.* (a) At U = e^{iηa} all factors in (R3) commute to first order, and the log of a contour mean is the mean of the logs to first order. So in units where the coarse bond has length 1,
\[
 \log\mathcal M(e^{i\eta a})(c)=i\big[Q^{\rm s}a(c)+N(a)(c_-)-N(a)(c_+)\big]+O(|a|^2),
\]
with Q^s a(c) := L^{−4}Σ_{x∈B(c_−)} ∫_{[x,x']}a and N(a)(y) := L^{−4}Σ_{x∈B(y)} mean_{orders} ∫_{y→x}a. Take a = ℓ (an axial affine field in these units). Its component ℓ_μ does not depend on x_μ, so ∫_{[x,x']}ℓ = ℓ_μ(x). With x = c_− + ηr and the block sum Σ_r r_κ = 0, this gives Q^sℓ(c) = ℓ_μ(c_−). In N(ℓ)(y), the direction-ν leg of an ordered path contributes ηr_ν[ℓ_ν(y) + Σ_{κ<ν}ε_κηr_κF_{κν}], with ε_κ ∈ {0,1} fixed by the order. Its block sum vanishes, since Σ_rr_ν = 0 and Σ_rr_νr_κ = (Σr_ν)(Σr_κ) = 0 for κ ≠ ν. So N(ℓ) = 0, and one averaging step maps the affine field to the affine field with the same F. M_{𝐁} uses iterates of 𝓜. At U = 1 every intermediate average is 1, so K_T is the composite of these one-step linearisations. Induction on q gives (a).

(b) The first variation a = H_TB of the box problem solves L_0a = K_T^Tλ, K_Ta = B. Here L_0 is the Hessian of A_{T_0} at 1 in the chart, the box curl-curl operator of (R1). By [T4] the solution set is {H_TB + dχ : χ = 0 at nodes}, the residual gauge directions. Now test a = ℓ^b. K_Tℓ^b = ℓ^T by definition. curl ℓ^b is constant, so at a bare bond whose six plaquettes lie in T_0 the plaquette contributions cancel in opposite pairs: (L_0ℓ^b)(b) = 0. A bond with a plaquette outside T_0 has both endpoints outside T_1, because the gap between T_0 and T_1 exceeds ρξ'_0 ≥ 2 bare steps. So it is a level-0 determining row, whose constraint row is the identity on that bond (𝓜^0 = id). Hence L_0ℓ^b = K_T^Tλ, with λ := L_0ℓ^b on those rows and 0 elsewhere. So ℓ^b is in the solution set, which is (b). The linear current J'(1)ℓ^b = d*dℓ^b vanishes wherever the plaquettes lie in T_0.

(c) By (PW14), D²(G_X∘P^T_in)(0)[B,B] = D²G_X(0)[DP^T_in(0)B, DP^T_in(0)B]. By (b), DP^T_in(0)ℓ^T = (1, ℓ^b + dχ, d*d(ℓ^b + dχ)), and the current is 0 on the stencil, because dd = 0. Gauge invariance: G_X(g_s·P(t)) = G_X(P(t)), with g_s = e^{isχ} and P(t) the pair of e^{iηtℓ^b}. BCH gives g_s·P(t) = e^{iη(tℓ^b + s dχ + st R_1 + s²R_2)} with bilinear R_1 and quadratic R_2. Take ∂_s∂_t and ∂_s² at 0 and use DG_X(0) = 0. This gives D²G_X(0)[dχ, ℓ^b] = 0 and D²G_X(0)[dχ, dχ] = 0. □

**Lemma 4' (comparison with the torus map).** Let P_j be the level-j critical map on the torus at the flat reference. Let ℓ̃ be the torus datum equal to ℓ_F at the representative of c − z in the fundamental domain centred at z. Let L := DP_j(0)ℓ̃ on X. The series Σ_cℓ̃(c)DP_j(0)e_c converges absolutely there, by [T4]'s decay on the torus. Let T' be an admitted box tower around z of radius R' ≤ (torus side)/4 with X ⊂ T'_1. If D := 2 + diam X ≤ R'/2, then
\[
 L=\ell^b+d\chi''+E',\qquad\|E'\|_X\le C|F|R'^se^{-cR'} .
\]
Hence for every G_X as in Lemma 4 (c), |D²(G_X∘P_j)(0)[ℓ̃,ℓ̃] − D²G_X(0)[ℓ^b,ℓ^b]| ≤ C‖D²G_X(0)‖ |F|²D^sR'^s e^{−cR'}.

*Proof.* Linearise [9.3] at B = 0: L|_{T'_0} = H_{T'}[K_{T'}L] + dχ', with χ' = 0 at the nodes of T'. On level-j rows of T', K_{T'}L = ℓ̃ = ℓ_F, the torus constraint. On the lower-level collar rows, K_{T'}L =: β. So K_{T'}L = ℓ^{T'} + δ, where δ := β − ℓ^{T'} is supported on the collar rows. By Lemma 4 (b), L = ℓ^b + dχ'' + H_{T'}δ on T'_0. On the collar |L| ≤ C|F|(R' + C) by the torus decay, and |ℓ^{T'}| ≤ |F|R'. So |δ(c)| ≤ C|F|R'. [T4]'s decay with the cell-weighted sum Σ_c e^{−(θ/2)d_𝐁(x,c)} ≤ S_{θ/2} then gives ‖H_{T'}δ‖_X ≤ C|F|R' S_{θ/2} e^{−(θ/2)d_𝐁(X,\text{collar})}, and d_𝐁(X, collar) ≥ c(R' − D). The quadratic form estimate follows from Lemma 4 (c) applied to the gauge part. □

## 7. Theorem BX': (BX) on the Hölder core

Let a_out := C_8a_*, with a_* from (4.1) and C_8 fixed below. Under `wf-c.md`'s radius convention (α_k ≤ C_αα_{0,k}, Mα_0 ≪ α_1, α_1 ≤ C'Mα_0), a_out ≤ C_Mα_k, where C_M depends on M and the fixed constants. Take C_w := M/4, so that the level-j window Q_z of Lemma 3 lies in T_j(R_z).

**Theorem BX' (implication; proved by Claude, not yet checked).** Assume the hypotheses of Lemma 2, [T4] for the Rule W box tower T of R_z, [9.3], and the old-age input condition C_axa_outσ ≤ r_B/2 of SA (PW5). Fix t, ν, s, B' in the ranges of Lemma 2. Let B̂ be the box datum in the complete axial gauge about z, extended to the lower-level nodes of T by comb transports. Then:

- **(BX'-1) datum.** B̂ = ℓ^T + r on the rows of T. On level-j rows in Q_z, |F| ≤ Ca_outσ² and |r(c)| ≤ Ca_outσ^{2+α_H}|c − z|^{1+α_H}. On all rows, |B̂|, |r| ≤ CMa_outσ.
- **(BX'-2) pair.** For X ∋ z with its read stencil in T_1 and D := 2 + diam X ≤ C_w/(2σ),
\[
 \big\|P^T_{\rm in}(\widehat B)-(\mathbf 1,\ \ell^b+d\chi,\ 0)\big\|_X\le CD^s\big[a_{\rm out}\sigma^{2+\alpha_H}+r_{\mathrm B}^{-1}a_{\rm out}^2\sigma^4\big]
\]
in the level-j pair norm (SA (PW2): potential, gradient, current), and in its Hölder member.
- **(BX'-3) Hessian.** For every gauge-invariant regular member G_X as in Lemma 4 (c), D²(G_X∘P^T_in)(0)[ℓ^T,ℓ^T] = D²G_X(0)[ℓ^b,ℓ^b]. Also |D²G_X(0)[ℓ^b,ℓ^b] − D²(G_X∘P_j)(0)[ℓ̃,ℓ̃]| ≤ C‖D²G_X(0)‖|F|²D^se^{−cM/σ}.
- **(BX'-4) node gauge.** G_X(P^T_in(B̂)) equals the window value at Lemma N's node-reduced datum.

*Proof.* (BX'-1). Lemma 2 gives Lemma 3's hypothesis with b_1 := C_Va_*, because σ' ≤ σ. Lemma 3 and Lemma 4 (a) give the level-j statement. Off Q_z, the unexpanded comb bound |B̂(x)| ≤ Cb_1σ²|x − z| holds with |x − z| ≤ CM/σ. A lower-level row carries the extra factor ξ'_q ≤ 1. |ℓ^T| obeys the same bound.

(BX'-2). P^T_in(0) = (1,0,0), so P^T_in(B̂) = DP^T_in(0)ℓ^T + DP^T_in(0)r + N_2. Here N_2 := ∫_0^1(1−τ)D²P^T_in(τB̂)[B̂,B̂]dτ, and τB̂ lies in the polydisc of radius r_B/2 by the old-age condition.
- By Lemma 4 (b), DP^T_in(0)ℓ^T = (1, ℓ^b + dχ, 0) on the stencil.
- By [T4] at 0, ‖DP^T_in(0)r‖_X ≤ C_1Σ_c e^{−θd(c,X)}|r(c)|. Inside Q_z use (BX'-1) and the weighted sum (SA (PW9)) Σ_c e^{−μ dist(c,X)}(1+|c−z|)^m ≤ C_{μ,m}D^{m+4}. That rebuild is elementary: |c − z| ≤ D + dist(c,X) + C, and the shells grow polynomially. Outside Q_z, dist(c,X) ≥ C_w/(2σ), and CMa_outσ·S_θe^{−θC_w/(4σ)} ≤ Ca_outσ^{2+α_H}. This gives CD^{5+α_H}a_outσ^{2+α_H}.
- SA (PW4), rebuilt: for B in the r_B/2-polydisc, s ↦ ∂_{B(c)}Z_y(B + se_{c'}) is holomorphic for |s| < c_colr_B/2 and bounded by C_1e^{−θd(y,c)} ([T4] on the whole polydisc). Cauchy gives |∂_{c'}∂_cZ_y| ≤ (2C_1/(c_colr_B))e^{−θd(y,c)}. By symmetry the same holds with c'. The geometric mean gives (C/r_B)e^{−(θ/2)(d(y,c)+d(y,c'))}. So ‖N_2‖_X ≤ (C/r_B)(Σ_ce^{−(θ/2)d(c,X)}|B̂(c)|)² ≤ CD^{10}r_B^{−1}a_out²σ⁴.
- [T4]'s Hölder member has the same kernel decay. So the same sums bound the Hölder member.

(BX'-3). Lemma 4 (c) with T, then Lemma 4' with T' := T and R' = C_w/σ. The torus side is at least the window box side.

(BX'-4). The box map is covariant under node gauge transformations v near G. Covariance holds for unitary v by Theorem 3, and extends to complex v by the identity theorem in v, exactly as in the proof of `wf-room-2.md` Lemma E, item 3. Members are gauge invariant. Along a path of node gauges from 1 to the composite of g_z with g and Lemma N's v, the data stay in the r_B/2-polydisc, because |v||v^{−1}| ≤ e^{CMα_1}. So the two values agree by analytic continuation from the unitary path. □

**How Proposition W reads it.** Replace (BX) by (BX'-1)–(BX'-4), the member's own datum ℓ_z by ℓ^T, its response by ℓ^b, and E_z by the error of (BX'-2).
- Step 2's cancellation is (BX'-3) followed by (P20): Σ_{X∋z}D²(G̃_X∘P^T_in)(0)[ℓ^T,ℓ^T] = D²(F̃_z∘P_j)(0)[ℓ̃,ℓ̃] + O(g_jα_j^{−2}|F|²e^{−cM/σ}) = O(g_jα_j^{−2}a_out²σ⁴e^{−cM/σ}).
- Steps 3–4 read (BX'-2) with α_k replaced by a_out ≤ C_Mα_k.
- The gauge part dχ drops out of every Hessian by Lemma 4 (c). It also drops out of the cubic Taylor remainder, because Taylor's formula is applied to the gauge-invariant composite G̃_X∘P^T_in in the datum variable.

So (WF8), and with it the regular part of (19), hold for inputs in U^H_{k+1}, with constants depending on M, given Proposition W's other inputs. The e^{−cM/σ} term is absorbed as in WF12.

## 8. Preservation under the step

**Lemma 5 (inner Landau triples satisfy (H)).** Use the setting of `o1-decoupled.md` 4.2: a Rule W box □_0, its tower cut at depth j, the Landau pair (𝓗, u) over 1, and X ⊂ T'_j(□_0). There is C_{𝓗H} = C(L, α_H, θ) such that for sup|B| < r_I,
\[
 [\nabla\mathcal H(B)]_{\alpha_H,X}\le C_{\mathcal H\mathrm H}\sup|B| .
\]
So P_in(B) satisfies (H) on X at radii (a_0, a_1) as soon as C_{𝓗H} sup|B| < a_1.

*Proof.* The real factor is 1, so take g = 1 and A_r = 0. The real clauses hold trivially, and A'' = 𝓗(B) = ∫_0^1Σ_cB(c)h_c dτ with h_c := D𝓗(τB)e_c.
- [T4] 7.4 gives the covariant Hölder bound of ∇h_c at separations s ≤ 1, with the factor e^{−θd(y,y_c)}. The comparison is along straight paths at the background U_τ = e^{iη𝓗(τB)}.
- The straight transport over length s differs from 1 by at most Cs·C_𝓗 sup|B|. The covariant and ordinary gradients differ by [𝓗(τB), h_c] terms, whose variation over length s is at most (|∇𝓗||h_c| + |𝓗||∇h_c|)s ≤ C sup|B| e^{−θd}s^α. So the ordinary Hölder seminorm of ∇h_c is at most Ce^{−θd(y,y_c)}.
- Summing over c with Σ_ce^{−θd} ≤ S_θ gives CS_θ sup|B|. Separations above 1 use 2 sup|∇𝓗(B)| ≤ 2C_𝓗 sup|B|. □

**(A2-H).** Use `o1-decoupled.md` 4.5's order of constants with C_𝓗 replaced by max(C_𝓗, C_{𝓗H}) in condition (ii). Then the inner triple P_in(B_{t,ν}) of `wf-c.md` Theorem A (A2) also satisfies every (H) clause at most at 1/2 of its radius. This holds at every point of the disc and at every age, m = 0 included. The real clauses hold trivially. The radius bookkeeping of the (R4)–(R6) clauses is that of Theorem A, unchanged.

**(ER8u)-H.** The same constant shows that P_in(B) satisfies (H) for every sup|B| < r_j, once r_j ≤ α_{1,j}/(2C_{𝓗H}). This is a fixed reduction of the constant c in r_j ≥ cα_j. So the Taylor expansion of Proposition W, step 1, stays in U^H_j on the whole ball it uses.

**Proposition I (the repaired core is preserved; implication).** Suppose (I_k): every regular member of level ℓ ≤ k is holomorphic and bounded, with its norms g_ℓ, d_ℓ, r_ℓ, on U^H_ℓ. Consider the box-first step k (`wf7-bf.md`, `cond-c.md` Rule W, `wf-c.md` Theorem A). Then:
1. Every member evaluation in the step is at an inner Landau triple, and these lie in U^H_ℓ by (A2) and (A2-H). This includes Proposition W's Taylor expansion along τB̂, by (ER8u)-H.
2. At every input P ∈ U^H_{k+1} at half radii, Theorem BX' holds, so Proposition W gives (19) there, given its other inputs.
3. So the new members of level k+1 are bounded on U^H_{k+1}, on the same radii as before. The next step evaluates them only at points of item 1, one level up.

Hence (I_{k+1}) holds. No member is ever evaluated at a pair that violates (H). Codex's input of `bx.md` is never an evaluation point.

**Rule (C) for Cauchy estimates in pair space.** A consumer may bound a member's change by Cauchy's inequality along a complex segment P_0 + λ(P_1 − P_0) in pair space, as `wf7-bf.md` does for WF11–WF12 on its (4). It must measure the segment in the Hölder-augmented norm ‖·‖^H_X := max(‖·‖_X, [·]_{H,X}). (H) is convex in A' at fixed U and gauge. So for two inner Landau triples (U = 1), the segment stays in (H) for |λ| ≤ cα_j/‖P_1 − P_0‖^H_X. For box pairs, `wf7-bf.md` (4) holds in this norm with the same exponent, because [T4]'s Hölder member has the same kernel decay e^{−2γd_T(x,c)} as its value member. Expansions in the datum variable of a box map need nothing new, by (ER8u)-H.

## 9. Consumers: what still reads the smaller domain

Each item below was checked against the cited text. "Kept" means that the statement holds verbatim on U^H, because it is quantified over all core inputs or it is a statement about datum maps.

| consumer | what it reads | verdict |
|---|---|---|
| `wf-c.md` Theorem 6c^C, Lemma C, Corollary CC, Lemma RC | collar data and restriction of box maps, for every core input | kept |
| `wf-c.md` Theorem A (A1) | (R4) of 𝐔_{t,ν}, used by Lemmas N and E | kept; (A1) is not asked to give (H) for 𝐔_{t,ν}, because Lemma 2 handles the datum directly |
| `wf-c.md` Theorem A (A2) | core membership of the inner triple | extended by (A2-H), Section 8 |
| `wf-c.md` Proposition N, (H-node) | node lifts of the same box pair | kept; members are gauge invariant, and the Landau representative is in U^H by Lemma 5 |
| `wf7-bf.md` Section 2, identity (2) | algebraic identity at complete physical pairs | kept |
| `wf7-bf.md` (3)–(6), WF11–WF12, OA7 | first-response bounds of box pairs; Cauchy in the member core | kept, with Rule (C): (4) and OA7's pair estimate also hold in the Hölder-augmented norm |
| `wf7-bf.md` grouped directions | (BX) | now Theorem BX' on U^H_{k+1} |
| `wf7-bf.md` Section 4, heredity | read sets and Lemma CR | kept |
| `cond-c.md` Theorem C2, Rule W | containment of windows | kept (geometry) |
| `cond-c.md` 6.2, layered position (W2) | "affine and Hölder sizes are those of a level-(p−1) pair" | kept **if** (H) is imposed in ambient local units, as Section 2.2 does. Lemma 2 was written for top-layer base points only. The (W2) case repeats it with ℓ(z) = p − 1 and [PW-H]'s layer factor e^{−θ_L(k−p−1)_+} from (LD); this repeat is not written here |
| `b2-extract.md` Proposition W | (P20), (ER8u), (BX), (UR), (YA) | (BX) → BX'; (ER8u) → (ER8u)-H; (UR), (YA) are bounds on members and are needed only at evaluation points, which lie in U^H |
| `b4-step.md` (19), B1 | "on every admitted complex core" | read as "on every admitted U^H core"; B1's coupling discs are parameter discs and do not leave U^H |
| `ti-2.md` Theorem TI | invariance of the domain under the level-j torus group | kept: (H) is invariant under translations and the hypercube group |
| large-field consumers (Package C, 2.8, 2.13, floor screening, (DOM)) | member evaluations outside the window | **not checked here.** They must evaluate regular members only on U^H. Evaluations at critical backgrounds pass by Lemma 5. Any evaluation at a raw non-critical pair would need its own check |
