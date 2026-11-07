lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T16:05Z

# Gate: line-by-line check of library/layer-thm.md and library/layer-r2.md

Queue row 418. Claude Opus 5.5, max effort, commit 9a6feac0c, Mac mini worker 2. One reading by one other model; not an audit.

(In progress. Sections are written as they are checked.)

Sources: the four pinned account files, fetched by URL from github.com/ethanwsussman/Yang--Mills-LLM-experiment at `31a47c543775` into a scratch folder; SHA-256 equal to the table in `library/layer-find.md`. I, II, III, SA as in those notes. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Balaban for the chart and propagator constructions.

## 1. layer-r2.md, the (S5)-(B4) incompatibility (checked first)

**Verdict: ADVANCE.** The calculation of layer-r2 sections 4-6 is correct. I redid every step against the account's definitions. First failing step: none.

What I checked, in order:

- **Admission.** I 12935-13035: (S3) makes J a 𝔤^c-valued bond function with only `|J|_(-3) < a_γ`, and "no relation between J and U is required". So complex currents of the bidisc in 6.5 are admitted bases, with no derivative condition.
- **Definitions.** I 13719-13738 (Lemma `4.5:lem-free-current-operators`): `Θ'_J = k_JΛ + Λ^T j_J + Λ^T m_J Λ`, `G^J_π = Σ G_0(Θ'_J G_0)^n`, `H^J = G^J_π Q* q_J ℓ^{-1}`, `⟨A,Θ_J A⟩ = 2⟨H^J C^(2)(ℓA), J⟩`, `G̃^J = (I - G̃_0 Θ_J)^{-1} G̃_0`; `m_J(λ) = m_3 + D*_U m_4` with m_4 pointwise in `[λ,J]` (proof, I 13811-13823). So Θ_J depends on J only through the weight `w(J) = H^{J,T}J`, linearly, as r2 (31) uses. (J8) gives analyticity in (𝔞,J) on the whole class, so `Q_J(a)` is holomorphic on the bidisc at each mesh.
- **(15)-(16).** From `(Δ_a - Θ'_J)H^J = Q* q_J ℓ^{-1}` (J4) and `P_0 G_0 Q* = 0`, `P_0 H^J = H^J - H_0`: exact. The Neumann coefficients (16) follow because A_J is linear in J.
- **(13)-(14).** With d(t) = (-ta,0), (S5) gives `A'(t) = tT_J a + O(t²)` (V' has degree ≥ 2), and the inner map `X ↦ C(ℓA' - ℓH^J X)` (I 13995, Lemma `4.5:lem-nonlinear-correction` (a)) gives `X(t) = t² C_2(ℓT_J a, ℓT_J a) + O(t³)`, since DC(0) = 0. The Cauchy step on |t| = ε/2 gives (14). This needs holomorphy on a datum disc of mesh-free radius, which is exactly what (G) supplies.
- **Flat sector (20)-(22).** Qa = ⟨a⟩ on period-one fields; `B = P_0 G_0 = Δ^{-1}(I - Π_0)`, `ΔB = I - Π_0`, `Λ = Δ^{-1}D*`, `H_0 b = b`. These hold for any positive mass constant and any G' that inverts the site Laplacian on mean-zero fields; only `D*(constant) = 0`, `D_curl* D_curl + DD* = Δ` (flat) and `QH_0 = 1` are used.
- **(23)-(26).** The coarse-bond transport of e^{iηua} is the ordered product P_n(u) for every contour and for the composed k-step average (rows in other coordinates are identical), so x_0 = q_2(a). BCH: `[a(r),a(s)] = 2i A_*^{-2} sin(2π(s-r)/n) τ_3`; `Σ_{m=1}^{n-1}(n-m)z^m = nz/(1-z)`, Im = (n/2)cot(π/n). So c_n = -cot(π/n)/(2nA_*²) and |c_n| ≥ 1/(4πA_*²) for n ≥ 3. Correct.
- **(27)-(33).** I re-derived j_J from `⟨λ, j_J(A)⟩ = ⟨c^(1)(A,λ), J⟩` (I 13700-13706) and m_4 from the polarised c^(2). Every term of the full mixed coefficient (17): x_1 = x_2 = x_12 = 0 by (30)-(31); `A_2 H_0 x_0 = 0` (`[τ_3,τ_3] = 0`, `Λ(const) = 0`); `B A_1 H_0 x_0 = Dλ_1`; in `A_2 Dλ_1`, m_3 = 0 (`D_1 λ_1 = 0`), j_{J_2}(Dλ_1) = 0 (components 2 vs 1), k_{J_2}λ_1 has only component 1. So component 2 of `∂_s∂_t Q|_0` is exactly `D_2 Δ^{-1} D_1* m_4` with `m_4 = 2c_n d_1^{-4} f_n φ τ_1`. Signs and factors agree with (32)-(33).
- **(34)-(36).** D_1* and D_2 on the half-shifted sine modes, the eigenvalue `d_k² + d_r²`, `β_r ≥ 1/(4r)` for `2 ≤ r ≤ M-1`, `4k ≤ d_k ≤ 2πk`, and the dyadic-square count are all correct. The sine-sum bound `|S_M| ≤ 1+π` is correct (Abel summation). So the coefficient is at least `c_* q_n` with q_n → ∞ like log n.
- **(37)-(39).** Cauchy on |s| = |t| = r with r = γ_*/8 independent of n. The contradiction is valid.

**Mechanism, for the lead.** `Λ^T m_J Λ` contains `D Δ^{-1} D* m_4`, an order-zero operator applied to a product with the bounded current. Order-zero operators are not bounded on sup-norm data; the account says so itself: I 13599-13617 bounds `∇G_0∇*` only on Hölder data, and (J2) at I 13763-13764 says "The Laplacian member is not asserted for G^J_π". At an own-current pair `RD*H^J = 0` kills this term (layer-thm Attack 1), so the failure is specific to independent currents.

**What it establishes.** On any datum domain where the (S5) layers exist with a mesh-free radius and are holomorphic in the admitted independent current, (B4) has no mesh-free constant, and therefore (S9) fails: by (B3), (S9) implies (B4). Since layer-r2 section 2 derives (G) from the chart's own operator hypotheses (3), (B4) is false under the hypotheses the chain needs anyway. The stopping lemma R_Δ should not be attacked again on the independent-current domain.

**What it does not establish.** It does not refute (N1), the A' member or the four entries; it does not refute the block-only chart; it uses the field slot. I expect a block-only version with a coarse-scale varying block datum (then `C_2(ℓH_0 b, ℓH_0 b) ≠ 0` at J = 0 and the same `DΔ^{-1}D*m_4` term appears at second order in J), but I have not computed it; label: gap, not used below.
