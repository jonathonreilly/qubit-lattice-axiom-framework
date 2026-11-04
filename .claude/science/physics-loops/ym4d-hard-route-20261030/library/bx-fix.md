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

**One addition (not a defect).** The obstruction does not depend on the splitting or the gauge. The curvature itself is F_{12}(x) = −πεa sin(π(x_1 + η/2)/σ)T, so it changes sign over the distance σ. Section 2.3 shows that every gauge with small potential then has a gradient Hölder seminorm of order εaσ^{−α}. So the repaired domain excludes this input.
