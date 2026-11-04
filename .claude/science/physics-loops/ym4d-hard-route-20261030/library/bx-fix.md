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
