lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T18:36Z

# mu-uses-check: the uses of their 4.13 that mu-radii does not cover (queue row 364)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout f8bb65831. One line-by-line check, not an audit. Kind: check of where our frozen `library/mu.md` (with `library/mu-radii.md` §1, refereed in `gates/mur-gate.md`) covers the uses listed in `library/mu-uses-sol.md`. Sources: CA-I, CA-II, CA-III at 31a47c543775, fetched by URL; SHA-256 match `mu.md` §1 (4cb5cb5e…6e93, 6a1f74b0…2b8f, 7e36523b…352d). Source authors: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The minimiser theory is Tadeusz Bałaban's (CMP 98, 102b, 109, 119). No numeric job was run; every step is by hand.

Status: in progress. Sections are written as they finish.

## 1. What is already covered, and the two covering statements

`mu.md` proves their 4.13 for the CMP 109 Lemma 4 window: outer data in a ball of radius δ around the identity, inner domains Z ⊂ X ⊂ \tilde□^2, both tower rules. `mu-radii.md` covers 4.7, 4.8, 4.26 and 4.28 stage composites (CA-I 121193–123129, 144933), §4.31 (N1)–(N3) with its corrections, and CA-II 35641–35655, 35714, 44422, 44454. This report treats every other row of `mu-uses-sol.md`.

Each use below needs one of two statements. I name them here once.

**(RR) Real restriction.** Let U* be a real minimiser of Bałaban's constrained problem for an admissible sequence Ω = (Ω_0 ⊃ Ω_1 ⊃ …) with data V, regular with curvature parameter ε_W in its local units. Let D ⊂ Ω_0 and let B_in be an admissible sequence D = D_0 ⊃ D_1 ⊃ … on the same L-adic grids, with D_q ⊂ Ω_q for q ≥ 1 (so dist(D_1, D^c) ≥ 2η, by admissibility). Assume (5.2) of `mu.md` with this ε_W:

  ε_W < a_0/2,  C_7 ε_W < a_1/2,  B_3 C_7 ε_W < a_0/2.   (C)

Then U(B_in, M_{B_in} U*) = (U*|_D)^u for a gauge transformation u, the level-0 bonds of D_0 \ D_1 (including bonds that cross ∂D) being data.

*Proof (a reading of `mu.md` §5 with a general outer problem).* (i) The sequence Ω~ = (Ω_0, D_1, D_2, …) is admissible: its first separation is at least that of Ω because D_1 ⊂ Ω_1, and its later separations are those of B_in. It satisfies Ω~_q ⊆ Ω_q. Their CA-III 9.3:lem-refinement (36939–37000, proved there) gives that U* is minimal for (Ω~, M_{Ω~} U*). (ii) Ω~ prescribes every fine bond of Ω_0 outside the level-≥1 region of D. A bond that can vary touches D_1, so every plaquette that contains it lies in D. The full action and the action A_D of B_in differ by a constant on the fibre. So U*|_D is minimal, hence critical, for (B_in, M_{B_in} U*). (iii) Local scales of B_in are at most those of Ω, so U*|_D is in the regular class 𝔘 at parameter ε_W (as in the proof of 9.3), and by CMP 98 Proposition 2 its B_in-data have test parameter at most C_7 ε_W. Under (C), CMP 102b Theorem 1 applies to B_in at these data, and its unique critical orbit (radius a_0) contains both the minimal orbit and U*|_D. □

(RR) is the step that `mu-radii.md` §1 states in its last paragraph ("the same real restriction argument also applies to a real regular outer minimizer which is not in a base-one chart"). It gives equality up to gauge only. The literal axial representative needs the aligned-tree step of `mu.md` §5 in addition. No complex datum enters.

**(CN) Complex nesting.** This is `mu.md` §6, in the form of `mu-radii.md` (3): equality holds on a connected complex parameter domain when both sides are holomorphic there and agree on a real slice. It needs one more thing than (RR): an admission bound that puts the induced inner datum in the inner chart **on the whole complex domain**. A real-slice argument with no such bound does not cover a complex use.

**Order of choice (CA-I 1401–1700).** The constants a_1, B_3, B_5 and R_1 of CMP 102b are fixed at Stage 5; a_0 and C_7 depend on (d, L) only; M is fixed at Stage 6. The regularity parameters of the uses below (the radii α_{i,n}, ε^I, the running size ε^run, and γ_0 through \bar γ_0(t_γ)) are fixed at Stage 7 or later, or tend to zero with the coupling. So (C), with ε_W bounded by such a parameter, is a downward condition on a Stage-7 radius or a Stage-8 ceiling on γ of the allowed form sup_{x ≥ γ^{-2}} h(x) ≤ c. Its right side reads only Stage 0–6 letters, so it makes no cycle.

## 2. CA-I uses

Each entry gives (a) whether the passage uses their 4.13 or another Bałaban fact, and (b) whether our proof covers it, with the ceiling.

**I-1. 4.26:prf-nested-criticality, hypothesis (III), CA-I 128569–128576, used in (d) at 128733–128737.** Statement status PROVED (given (I)–(IV)).
(a) Not 4.13 itself. (III) is uniqueness modulo gauge for Bałaban's localised problem on X' (CMP 109, top level p, exterior fixed at U_*), at the real stage background U_*, with the identification U_p(X', M^𝔰U_*) = (U_*|X')^u off the boundary layer. The criticality transfer is proved inside the lemma, by feasible-set inclusion (clauses (a)–(d)); (3.38) is not used. What (III) adds is step (iii) of (RR): CMP 102b Theorem 1 on the localised problem, with U_*|X' in its uniqueness class.
(b) **Covered after ceiling.** (RR) with Ω = 𝔅_*, D = X', B_in = the localised structure of (II); steps (i)–(ii) are their (a)–(d). Ceiling: (C) with ε_W = (1.4/5)\bar γ_0(t_γ), their bound (IV) with 4.26:eq-nested-criticality-3 and the run-free majorant (116618–116626) on the direct sizes, read in the units of 𝔘 (φ_arrest = 0.098 < 1). I did not trace the fixed (d, L) unit factor between their direct sizes and 𝔘. This is one more lower bound on t_γ, of the same kind as their list at 116637–116648; no cycle. (RR) gives equality on all of X'; (III) asks only off the boundary layer.

**I-2. 4.29:lem-localisation-exact, hypotheses (1)–(2), CA-I 147454–147466, used in Step 2 (147535–147549).** PROVED given (1)–(4).
(a) Not 4.13 literally. Hypothesis (1) is the real restriction of a CMP 102b Theorem 1 minimiser U* to Bałaban's collared problem 𝐁' = 𝐁_j(Λ_j^∼) of CMP 119 (2.13); (2) is Theorem 1 uniqueness. This is the content of 4.13 (both halves, real data only) for a different outer problem (the global step backgrounds U^0 = U_{k+1}, U^1 = U_k(e^{iB'}V^{(k)}), B' real) and a different inner structure.
(b) **Covered after ceiling.** (RR) with Ω the global sequence of U^ι, D = Λ_j^∼, B_in = 𝐁'. Domination D_q ⊂ Ω_q is their Step 1 (Λ_j^∼ ⊂ Ω_j^♮ ⊂ Ω_j, levels of 𝐁' at most j). Ceiling: (C) with ε_W the curvature parameter of U^ι, which is B_3ε_1^g for U^0 by 4.29:prop-window-minimiser (3), and the same with the data of e^{iB'}V^{(k)} for U^1. Only real data are used; (c) of the lemma reads the interpolation through hypothesis (4) and Proposition 9, not through nesting.

**I-3. 4.29:prop-window-minimiser, hypotheses (1), (2), (6), CA-I 148801–148809, used at 148872–148880 and 148906–148912.** PROVED given (1)–(7).
(a) Not 4.13. Hypothesis (2) and its local form (6) are the restriction lemma, giving (d1) U_{k+1}|□_0 = U_i(□_0, M^·U_{k+1}) up to gauge, for j ≤ i ≤ s: this is CMP 109 (3.18) and the CMP 119 representation, real. The first identity of (d1) is CA-III 9.3 with Theorem 1, which their (1) and (4) state.
(b) **Covered after ceiling.** (RR) with Ω = 𝐁̃_s (or 𝔹), D = □_0, B_in = 𝐁_i(□_0); domination: □_0 ⊂ Ω_s, so D_q ⊂ Ω_q for q ≤ i ≤ s. Ceiling: (C) with ε_W = B_3ε_1^g from their (3). The account already needs B_3ε_1^g inside radius a_0 for its own first identity; the new part is the inner data test C_7ε_W.

**I-4. 4.29:rem-transfer-inputs, hypothesis (2) "local reproduction lemma", CA-I 151282–151289, used at 151386–151392, 151406 and 151429–151438.**
(a) Not 4.13. It is the same real restriction lemma, used twice: at D = Λ_j^∼ from U^0, U^1 (as I-2); and at D = □_0, B_in = 𝐁_j(□_0), from U* = W[𝐚] = U(𝐁', M'(e^{iη𝐚}U^0)), a real minimiser of the collared problem, for small real 𝐚 = (t + t_□ζ̄_□)𝐇_k. This second use is CMP 109 (3.18). The derivative in t_□ is taken at t_□ = 0 along real values, so no complex nesting is needed.
(b) **Covered after ceiling.** (RR) twice. For the second use Ω = 𝐁', and □_0 ⊂ Λ_j ⊂ D_j(𝐁') gives domination. Ceiling: (C) with ε_W the regularity parameter of W[𝐚] that 4.29:prop-near-field-scope supplies. That parameter reads ε_1^g and the source size δ_k^♯ (150378–150386); both are Stage-7/8 smallness, so no cycle.

**I-5. 4.29:cor-cubewise-analysis, item 9 and Case (A), CA-I 151610–151611, 151631–151632, 151661–151662, 151688.** PROVED given 1–9.
(a) Not 4.13. Item 9 retains the restriction lemma of I-2; Case (A) reads CMP 109 (3.18) at D = □_0 as its instance, exactly as I-4.
(b) **Covered after ceiling**, by I-2 and I-4 with the same ceilings. The complex bounds of Case (A) are on the window function itself (CMP 109 Lemma 4, i.e. `mu.md`), not on the global minimiser.

**I-5'. Not listed in `mu-uses-sol.md`: 4.29:prop-near-field-scope, the hypothesis "Reproduction of minimal configurations on a domain", CA-I 150365–150371.** Same statement as I-4's hypothesis, with "regular at the levels of 𝓑_1" left unquantified. Covered by (RR) under (C) at the regularity of the minimiser it is applied to.

**I-6. 4.31:prop-fixed-depth-convergence (154697–154700), 4.31:rem-non-minimiser-data (155466–155511), 4.31:rem-marginal-uniformity (156154–156214).**
(a) No new use. The first lists (I9) = (N1)–(N3) as an input; its proof (154682–154945) does not read them, they enter through 4.31:lem-background-membership and 4.31:prf-marginal-minimiser-path. The second is a remark that points to the same route. The third reads only the n-uniformity of the gauge bound.
(b) **Covered by `mu-radii.md` §4**, in its corrected form: (N1)–(N3) with a block-constant ū are false (counterexample (21)–(22), confirmed in `gates/mur-gate.md`); the corrected identities (14), (19), (20) hold with ‖g^{±1}‖ ≤ 1 + 2C_tK_Wβ, uniform in n because levels are compared only through L^nξ ≤ 1. So rem-marginal-uniformity holds with the enlarged c_u of mu-radii, fixed at (d, L, M) before w_s, r_s.
