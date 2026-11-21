lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T18:36Z

# mu-uses-check: the uses of their 4.13 that mu-radii does not cover (queue row 364)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout f8bb65831. One line-by-line check, not an audit. Kind: check of where our frozen `library/mu.md` (with `library/mu-radii.md` §1, refereed in `gates/mur-gate.md`) covers the uses listed in `library/mu-uses-sol.md`. Sources: CA-I, CA-II, CA-III at 31a47c543775, fetched by URL; SHA-256 match `mu.md` §1 (4cb5cb5e…6e93, 6a1f74b0…2b8f, 7e36523b…352d). Source authors: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The minimiser theory is Tadeusz Bałaban's (CMP 98, 102b, 109, 119). No numeric job was run; every step is by hand.

Status: complete. Summary and defects in §6.

## 1. What is already covered, and the two covering statements

`mu.md` proves their 4.13 for the CMP 109 Lemma 4 window: outer data in a ball of radius δ around the identity, inner domains Z ⊂ X ⊂ \tilde□^2, both tower rules. By `gates/mu-gate.md` that covers the 4.7 and 4.8 uses, including 4.8:prop-class-reproduction (CA-I 34254–34257), which only carries the near-case hypotheses. `mu-radii.md` covers the 4.26 and 4.28 stage composites (CA-I 121193–123129, 144933), §4.31 (N1)–(N3) with its corrections, and CA-II 35641–35655, 35714, 44422, 44454. This report treats every other row of `mu-uses-sol.md`, and one use that list missed (I-5').

Each use below needs one of two statements. I name them here once.

**(RR) Real restriction.** Let U* be a real configuration that is critical (for example, minimal) for Bałaban's constrained problem of an admissible sequence Ω = (Ω_0 ⊃ Ω_1 ⊃ …) at its own data, and regular with curvature parameter ε_W in its local units. Let D ⊂ Ω_0 and let B_in be an admissible sequence D = D_0 ⊃ D_1 ⊃ … on the same L-adic grids, with D_q ⊂ Ω_q for q ≥ 1 (so dist(D_1, D^c) ≥ 2η, by admissibility). Assume (5.2) of `mu.md` with this ε_W:

  ε_W < a_0/2,  C_7 ε_W < a_1/2,  B_3 C_7 ε_W < a_0/2.   (C)

Then U(B_in, M_{B_in} U*) = (U*|_D)^u for a gauge transformation u, the level-0 bonds of D_0 \ D_1 (including bonds that cross ∂D) being data.

*Proof (a reading of `mu.md` §5 with a general outer problem).* (i) The sequence Ω~ = (Ω_0, D_1, D_2, …) is admissible: its first separation is at least that of Ω because D_1 ⊂ Ω_1, and its later separations are those of B_in. It satisfies Ω~_q ⊆ Ω_q, so every Ω-average is a composite of Ω~-averages and the Ω~-fibre of U* lies in its Ω-fibre (first paragraph of their CA-III 9.3:lem-refinement, 36939–37000, proved there). Hence U* is critical for (Ω~, M_{Ω~} U*); if U* is minimal, 9.3 gives minimality too. (ii) Ω~ prescribes every fine bond of Ω_0 outside the level-≥1 region of D. A bond that can vary touches D_1, so every plaquette that contains it lies in D. The full action and the action A_D of B_in differ by a constant on the fibre. So U*|_D is critical for (B_in, M_{B_in} U*). (iii) Local scales of B_in are at most those of Ω, so U*|_D is in the regular class 𝔘 at parameter ε_W (as in the proof of 9.3), and by CMP 98 Proposition 2 its B_in-data have test parameter at most C_7 ε_W. Under (C), CMP 102b Theorem 1 applies to B_in at these data, and its unique critical orbit (radius a_0) contains both the minimal orbit and U*|_D. □

(RR) is the step that `mu-radii.md` §1 states in its last paragraph ("the same real restriction argument also applies to a real regular outer minimizer which is not in a base-one chart"). Their own CA-II 8.5:lem-background-regularity, hypothesis (b) (96010–96028), states the same thing with C_7 = 2 (CMP 98 Proposition 2) and the ceiling α ≤ c̄_2, 2α ≤ a_1, 2B_3α ≤ a_0. It gives equality up to gauge only. The literal axial representative needs the aligned-tree step of `mu.md` §5 in addition. No complex datum enters.

**(CN) Complex nesting.** This is `mu.md` §6, in the form of `mu-radii.md` (3): equality holds on a connected complex parameter domain when both sides are holomorphic there and agree on a real slice. It needs one more thing than (RR): an admission bound that puts the induced inner datum in the inner chart **on the whole complex domain**. A real-slice argument with no such bound does not cover a complex use.

**Order of choice (CA-I 1401–1700).** The constants a_1, B_3, B_5 and R_1 of CMP 102b are fixed at Stage 5; a_0 and C_7 depend on (d, L) only; M is fixed at Stage 6. The regularity parameters of the uses below (the radii α_{i,n}, ε^I, the running size ε^run, and γ_0 through \bar γ_0(t_γ)) are fixed at Stage 7 or later, or tend to zero with the coupling. So (C), with ε_W bounded by such a parameter, is a downward condition on a Stage-7 radius or a Stage-8 ceiling on γ of the allowed form sup_{x ≥ γ^{-2}} h(x) ≤ c. Its right side reads only Stage 0–6 letters, so it makes no cycle.

## 2. CA-I uses

Each entry gives (a) whether the passage uses their 4.13 or another Bałaban fact, and (b) whether our proof covers it, with the ceiling.

**I-1. 4.26:prf-nested-criticality, hypothesis (III), CA-I 128569–128576, used in (d) at 128733–128737.** Statement status PROVED (given (I)–(IV)).
(a) Not 4.13 itself. (III) is uniqueness modulo gauge for Bałaban's localised problem on X' (CMP 109, top level p, exterior fixed at U_*), at the real stage background U_*, with the identification U_p(X', M^𝔰U_*) = (U_*|X')^u off the boundary layer. The criticality transfer is proved inside the lemma, by feasible-set inclusion (clauses (a)–(d)); (3.38) is not used. What (III) adds is step (iii) of (RR): CMP 102b Theorem 1 on the localised problem, with U_*|X' in its uniqueness class.
(b) **Covered after ceiling.** (RR) with Ω = 𝔅_*, D = X', B_in = the localised structure of (II), read as the constrained problem with constraint family 𝒞(𝔰) and fixed exterior, as their proof of (d) reads it; steps (i)–(ii) are their (a)–(d). Ceiling: (C) with ε_W = (1.4/5)\bar γ_0(t_γ), their bound (IV) with 4.26:eq-nested-criticality-3 and the run-free majorant (116618–116626) on the direct sizes, read in the units of 𝔘 (φ_arrest = 0.098 < 1). I did not trace the fixed (d, L) unit factor between their direct sizes and 𝔘. This is one more lower bound on t_γ, of the same kind as their list at 116637–116648; no cycle. (RR) gives equality on all of X'; (III) asks only off the boundary layer.

**I-2. 4.29:lem-localisation-exact, hypotheses (1)–(2), CA-I 147454–147466, used in Step 2 (147533–147546).** PROVED given (1)–(4).
(a) Not 4.13 literally. Hypothesis (1) is the real restriction of a CMP 102b Theorem 1 minimiser U* to Bałaban's collared problem 𝐁' = 𝐁_j(Λ_j^∼) of CMP 119 (2.13); (2) is Theorem 1 uniqueness. This is the content of 4.13 (both halves, real data only) for a different outer problem (the global step backgrounds U^0 = U_{k+1}, U^1 = U_k(e^{iB'}V^{(k)}), B' real) and a different inner structure.
(b) **Covered after ceiling.** (RR) with Ω the global sequence of U^ι, D = Λ_j^∼, B_in = 𝐁'. Domination D_q ⊂ Ω_q is their Step 1 (Λ_j^∼ ⊂ Ω_j^♮ ⊂ Ω_j, levels of 𝐁' at most j). Ceiling: (C) with ε_W the curvature parameter of U^ι, which is B_3ε_1^g for U^0 by 4.29:prop-window-minimiser (3), and the same with the data of e^{iB'}V^{(k)} for U^1. Only real data are used; (c) of the lemma reads the interpolation through hypothesis (4) and Proposition 9, not through nesting.

**I-3. 4.29:prop-window-minimiser, hypotheses (1), (2), (6), CA-I 148801–148809, used at 148871–148880 and 148908–148913.** PROVED given (1)–(7).
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

## 3. CA-II uses

**II-1. 5.2:rem-own-box, CA-II 4115–4117 and 4151–4154** (the box representation (5.2:eq-own-box-a), 𝔟 = U_j(□_0, 𝖵) on X modulo gauge, for an admissible background 𝔟 at scale n ≥ j, on one-layer boxes □'^{∼a+1} (a = n−j or ν) and on any box with two π_j-layers of margin).
(a) Uses the content of 4.13 (restriction and nesting), at real backgrounds and at the "extensions … to pairs (𝐔, 𝐉) on Bałaban's complex tubes" of 5.2:prop-box-comb-gauge (3929–3940). The parent (c1) is filed CITED (3926; "proofs being Bałaban's", 4035–4037). **Gap in their text:** for the two-layer box the remark derives the identity from clause (iv) of CMP 109 (1.11)–(1.16), quoted at 4126–4140. That clause constructs U_n(M^·𝐔) and bounds it on X^{∼−2}; it does not assert 𝐔 = U_n(X, M^·𝐔). So the identity is not in the quoted source; (RR)/(CN) supply it. Checked against the printed page (CMP 109 p. 262, clause (iv), (1.15)–(1.16), local copy `~/ym4d-papers/cmp109.txt` 716–743): the clause builds U_n(M^·(𝐔)), J_n(M^·(𝐔)) on the maximal sequence of X and states the bounds (1.16) on X^{∼−2}, "and the same bounds hold for U"; Bałaban adds that (iv) is there because later constructions "substitute the functions (1.15) in place of the variables U, J". No equality U = U_n(X, M^·U) is asserted. The a = ν one-layer box is taken as a hypothesis there (4050–4053).
(b) **Real backgrounds: covered after ceiling.** (RR) with D = □_0, B_in = the box sequence of CMP 109, Ω = 𝔟's own sequence, ceiling (C) with ε_W the curvature parameter of 𝔟 in level-j units (≤ 𝔞_n t² for the data, by (c1)). (RR) needs □_0 inside the region where 𝔟's own sequence has level ≥ j. The remark does not state this; each consumer must have it.
**Complex continuations, boxes of side D ≤ 5M/t: covered after ceiling.** Their cited (c3) gives the comb datum |B^ax| ≤ 2d(1+D)𝔞_n t² ≤ 12dM𝔞_n t. Under 12dMC_𝔞 sup_n α_·(g_n) < δ (a downward condition on the Stage-7 radii, after M and the δ of `mu.md` §4), the box data lie in the base-one chart of `mu.md` §4.1 (radius r > 2δ by (4.5), uniform in the box and depth) on the whole tube, and (CN), with (RR) on the real slice, gives the identity, again given domination. Both one-layer boxes qualify, since (2ν+3)M ≤ 5ML^{ν−1}. This reads (CN) only for continuations of minimiser maps along a connected parameter domain with a real slice. For an arbitrary pair of the tube that is not such a continuation, (c1) is not a restriction statement and I do not claim it.
**Complex continuations on larger two-layer boxes.** The consumer is 5.2:lem-marginal-bound (4729–4790). It reads the own box at complex admissible backgrounds (its (i) and the holomorphic families of (iii)), but only for X ⊂ \tilde□^2, where D_X = diam_j X + 5M and D_X t is at most a fixed multiple of M. On these boxes the per-bond form of (c3), |B^ax(b)| ≤ 2d(1+|b−y|)𝔞_n t², gives |B^ax| ≤ 2d(1+D_X)𝔞_n t² ≤ c(d)M𝔞_n, and (CN) is **covered after the ceiling** c(d)MC_𝔞 sup_n α_·(g_n) < δ. Their (c3) is stated for D ≤ 5M/t (4017–4018), and D_X can exceed 5M/t by a fixed factor; the derivation they give (a product of at most d(1+|b−y|) conjugated plaquettes, conjugation factor e^{O(Mα_1)} ≤ 2, 4070–4072) gives the same per-bond bound there, with the factor 2 kept by their ceiling O(1)Mα_1 ≤ β_s at a larger O(1). **Not covered:** complex continuations on two-layer boxes with D t unbounded (own boxes of large X). There the comb datum grows with D and the base-one chart does not reach; a real-base chart admission of the kind of `mu-radii.md` (16)–(18) would be needed. I found no consumer on T0's chain that reads this case; 8.5's consumers of large boxes are real (II-6).

**II-2. 5.2:rem-chain-configurations, CA-II 4220–4227.**
(a) The preparatory backgrounds U_k^{(n')} (real; the remark works at z = 0 and real couplings, 4159–4163) use the own-box representation of II-1, hence the real restriction content. The configurations Φ(b) are taken by statement (hypothesis (e)), and the large-field chain of CMP 122b by Bałaban's statement (hypothesis (a)); neither is a use of 4.13.
(b) **Covered after ceiling** for U_k^{(n')}: (RR) with (C) at their curvature parameter (the running small-field size, a Stage-8 ceiling), and the domination condition of II-1. Real only, so no admission is needed. The clause "a box meeting Z is admissible" (4212–4213) is not a restriction statement; (RR) does not give it, and the account takes it from CMP 122b.

**II-3. 5.2:lem-animal-resummation, CA-II 13872** (mechanism paragraph).
(a) It restates clause (a3) of the data-weight lemma quoted at 13754–13770, which is 5.5:lem-weight (a3)–(a4): the window 𝕎 restricted to a box Q of at most nine π_p-cubes is the minimiser of Q.
(b) **Covered by `mu-radii.md` §3** (CA-II 35641–35655 and 35714), after its ceiling (11) with the constant C_Q repaired in `gates/mur-gate.md` (defect 1). No new radius.

**II-4. 5.5:thm-membership-remainder, CA-II 44066–44078** ("a minimiser is the box minimiser of its own data", CMP 109 (3.19)).
(a) The CMP 109 (3.18)–(3.19) restriction, from the twisted global field to the window □_0. Clause (c) states it "at the real point of the construction, with σ ≡ 1 and 𝗍 real and small" (43914–43916, 44034). Holomorphy in (b) is proved directly through Proposition 9, without nesting.
(b) **Covered after ceiling.** (RR) at real data, D = □_0 ⊂ D_j, with (C) at the regularity of the real twisted field. No complex nesting is read.

**II-5. 8.5:lem-background-regularity, hypothesis (b), CA-II 96010–96029, used in (iii) at 96119–96138.**
(a) Hypothesis (b), "the nesting statement of the correlation theorem", is (RR) itself, for real configurations critical for a determining set of level ≥ j over □_0^{+t}; its ceiling α ≤ c̄_2, 2α ≤ a_1, 2B_3α ≤ a_0 is (C) with C_7 = 2. The backgrounds of ℜ(S; ε') are real, SU(N)-valued (95947).
(b) **Covered, no new ceiling.** (RR) proves hypothesis (b). Their (8.5:eq-critical-backgrounds-a) (95986) already imposes the ceiling at α = B_3ε'. Domination: □_0 ⊂ □_0^{+t} ⊂ 𝖢^♯ ⊂ Ω'_n.

**II-6. 8.5:lem-vacuum-subtraction (96177–96185) and II-7. 8.5:lem-core-estimate (96290–96291, 96381–96391).**
(a) No new use. Both read (8.5:eq-background-regularity-c) of II-5 at a real 𝔟: on the box □_X (side at most 4M(d_j(X)+5)), and on Q_y at level n with j = n. In the core estimate the complex variable σ enters only through ext_n, an analytic box map (hypothesis (b)); the nesting is read at σ = 1, the real background.
(b) **Covered, as II-5.** Box size does not enter (RR). For Q_y, (RR) needs only Q_y ⊂ Q_y^+ ⊂ 𝖢^♯ ⊂ Ω'_n, which the lemma assumes (96295–96296).

**II-8. 8.5:lem-minimiser-regular, CA-II 99782–99788.**
(a) The same real restriction, for the whole-lattice minimiser U_n(V) at real data, on the boxes of 8.5:def-regular-configurations. It cites "property (iv) of the minimal configurations listed in [CMP 109]" for the identity; as in II-1, clause (iv) does not contain it.
(b) **Covered after a stronger ceiling.** (RR) applies (outer level n everywhere, so domination holds). But the lemma assumes only ε' ≤ a_1 (99754), and its consumer only C_ext ε^win ≤ a_1 (100495, 100567). The restriction it cites needs the smallness of II-5's hypothesis (b) at α = B_3ε't²: the box data have test up to 2B_3ε't_m² on a rim layer of order m (up to 2B_3ε'L^{−2} at j = n−1), and the restricted field and the box minimal orbit must lie inside radius a_0 (curvature up to B_3ε' and 2B_3²ε'L^{−2}). From ε' ≤ a_1 alone these hold only if L² ≥ 2B_3 and B_3a_1 ≤ a_0 roughly, which the account does not state. **Repair (proved by (RR) under it):** assume (8.5:eq-critical-backgrounds-a) at ε' = C_ext ε^win in place of ε' ≤ a_1. ε^win is of order of the coupling times a power of its logarithm (95992–95993), so this is a Stage-8 ceiling; no cycle.

**II-9. 8.5:lem-branch-comparison, CA-II 101228–101232.**
(a) No new use. It reads (c1) through its hypothesis (3), the definition of 𝔢-regular configurations, for two real backgrounds (101209). Its hypothesis (1), domain-uniform localisation with exponential decay, is a different Bałaban fact (CMP 102b Proposition 9, (190)), not 4.13.
(b) **Covered** to the extent (3) is supplied by II-5 or II-8, with their ceilings.

## 4. CA-III uses (off T0's chain)

`library/port-map.md` F3 puts every leaf of CA chapters 9 and 10 off T0's chain. By FINISH "How we work" item 6, no lane works on these unless our chain reads them. I classify them from one reading each and do not check the admission radii.

- **III-1. 9.1:lem-hull-exactness, 2994–3016.** (a) Complex nesting ("re-minimisation of minimisers", 9.1:eq-hull-exactness-5) for gauge-invariant holomorphic f, at the polydisc points (𝗍, 𝗌) of the hull read; their text says it is "proved by the identity theorem on the totally real slice over the unique critical orbit". (b) **Not checked:** (CN) applies once the hull data stay in the chart on the whole polydisc; that is their clause (c) under 9.1:eq-hull-exactness-3, which I did not read.
- **III-2. 9.1:prop-dilation-failure, 5926.** (a) Complex nesting at a seed, used inside the proof of a negative statement (failure of uniform dilation fractions). (b) **Not checked**; same requirement as III-1.
- **III-3. 9.1:lem-slice-displacement, 6245–6265, 6345–6358.** (a) Nesting of the Landau chart under refinement at every complex β (9.1:eq-slice-displacement-3), and the second clause for critical configurations. This is (CN) for a Landau-chart map, not the axial window of 4.13. (b) **Not checked.**
- **III-4. 10.3:lem-real-values-unchanged, 88580–88593, 88620–88630.** (a) The real box restriction (two-layer box Q_v) at the real chain configuration chain(0⃗). (b) **Covered by (RR) after (C) only where domination holds.** The lemma uses Q_v "whatever the position … in particular … when Q_v meets Z" (88600–88602, 88632–88634). Where Q_v meets a region in which the chain configuration's own sequence has level below p*, (RR) does not apply; there the account rests on its chain statement (c), not on 4.13.

## 5. Related uses in `mu-uses-sol.md` (attribution not established there)

Part (a) only; none needs a new radius.

| Location | Verdict |
|---|---|
| CA-I 34738–34743 (after 4.8:lem-layerwise-bound) | Uses 4.13's real half: "tower-locality … for an admissible determining set", real only (34743). Covered by (RR) (and `mu.md` §5 in the 4.8 setting). Their text itself says the complex form "is not proved". |
| CA-I 41830–41833, 4.11:lem-idempotence | Not 4.13: CMP 102b Theorem 1 uniqueness at fixed data, no sub-domain. |
| CA-II 9400–9407, 5.2:lem-almost-invariance | Not 4.13: same-domain refinement by feasible-set inclusion plus Theorem 1, proved in place (the argument of CA-III 9.3). |
| CA-II 40007–40009, 5.5:thm-own-level-membership | Not 4.13: same-domain refinement criticality at the real point. |
| CA-II 52110–52162, 5.7:prop-critical-layer-closeness | (A1) is refinement criticality; the conclusion "𝕎 coincides with 𝕌 modulo a gauge transformation on the base block □_0" at real β, b is a real restriction to □_0, so (RR) content. Covered by (RR) after (C), if □_0 is dominated as in II-1. |
| CA-II 75359–75376, 8.2:lem-curvature-contraction | Not 4.13: whole-lattice nesting across levels (CMP 109 (0.21), (2.3)) plus uniqueness; no sub-domain. |
| CA-III 9297–9357, 11230–11232, 18908–18914 (9.1) | Complex criticality/nesting under refinement; off T0's chain, not checked. |
| CA-III 36969–36998, 9.3:lem-refinement | Their proved refinement lemma; an input of `mu.md` and of (RR), not a use. |

## 6. Summary, defects, verdict

**Per use.** "(C)" is the ceiling of §1 at the use's regularity parameter; every such ceiling is placed in their order without a cycle (§1, last paragraph).

| Use | Uses 4.13? | Covered by our proof? |
|---|---|---|
| I-1 4.26:prf-nested-criticality (III) | uniqueness half only, on Bałaban's localised problem | covered after (C) at (1.4/5)\bar γ_0(t_γ) |
| I-2 4.29:lem-localisation-exact (1)–(2) | real restriction, global → collared | covered after (C) at B_3ε_1^g |
| I-3 4.29:prop-window-minimiser (2), (6) | real restriction, CMP 109 (3.18) | covered after (C) at B_3ε_1^g |
| I-4 4.29:rem-transfer-inputs (2) | real restriction, twice | covered after (C) |
| I-5 4.29:cor-cubewise-analysis | via I-2, I-4 | covered after (C) |
| I-5' 4.29:prop-near-field-scope (not in the list) | real restriction | covered after (C) |
| I-6 4.31 three consumers | no new use | covered by `mu-radii.md` §4, corrected form |
| II-1 5.2:rem-own-box | yes, real and complex | real: covered after (C), given domination. Complex, boxes of side ≤ c(d)M/t (all that the marginal bound and the one-layer boxes read): covered after c(d)MC_𝔞 sup_n α_·(g_n) < δ. Complex, unbounded two-layer boxes: **not covered** |
| II-2 5.2:rem-chain-configurations | real restriction (preparatory chain) | covered after (C), given domination; the "box meeting Z" clause is not a restriction statement |
| II-3 5.2:lem-animal-resummation | same as 5.5 (a3) | covered by `mu-radii.md` §3 |
| II-4 5.5:thm-membership-remainder (c) | real restriction | covered after (C) |
| II-5 8.5:lem-background-regularity (b) | is (RR) | covered; their 95986 is the ceiling |
| II-6, II-7 8.5 vacuum subtraction, core estimate | no new use | covered, as II-5 |
| II-8 8.5:lem-minimiser-regular | real restriction | covered after a ceiling stronger than their ε' ≤ a_1 |
| II-9 8.5:lem-branch-comparison | no new use | covered as II-5/II-8 |
| III-1–III-3 (CA-III 9.1) | complex nesting | off T0's chain, not checked |
| III-4 10.3:lem-real-values-unchanged | real restriction | covered after (C) where domination holds; not where Q_v meets a low-level region |

**Defects and limits, ranked by what they break.**

1. **Citation gap in their text (CA-II 4126–4154 and 99782–99786).** 5.2:rem-own-box (two-layer box) and 8.5:lem-minimiser-regular take the identity "a minimiser restricted to a box with margin is the box minimiser of its own data" from clause (iv) of CMP 109 (1.11)–(1.16). The printed clause (p. 262) states only the bounds (1.16) for U_n(M^·𝐔) and for 𝐔; no equality. *Failure:* the identity used in (c1) for the two-layer box is not in the cited source. *Effect:* none after repair. (RR) proves it at real backgrounds under (C) and domination, from their own 9.3 and CMP 102b Theorem 1; (CN) proves it at complex continuations on boxes of side ≤ c(d)M/t. This is a missing proof of a step they cite, not a false statement.
2. **Weak hypothesis in 8.5:lem-minimiser-regular (CA-II 99754; consumer 100495, 100567).** ε' ≤ a_1 does not give the second application of Theorem 1 that its cited restriction step needs (II-8). *Failure:* the step's hypothesis is met only if roughly L² ≥ 2B_3 and B_3a_1 ≤ a_0, which the account does not state. *Repair:* assume (8.5:eq-critical-backgrounds-a) at ε' = C_ext ε^win; a Stage-8 ceiling. Not refuted.
3. **Domination is needed and not stated.** (RR) needs the box inside the region where the background's own sequence has level ≥ j. (c1) is stated for any two-layer box, and 5.2 (4212–4213) and CA-III 10.3 (88600–88602) use boxes meeting the large-field region Z. There the identity is not a restriction statement; the account takes it from CMP 122b by statement. Neither `mu.md` nor (RR) covers that case. I did not try to refute it.
4. **Complex continuations on unbounded two-layer boxes: not covered** (II-1). The base-one chart does not reach; a real-base chart admission of the `mu-radii.md` (16)–(18) kind would be needed. I found no consumer on T0's chain that reads this case.
5. **Minor (their text):** (c3) is stated for boxes of side ≤ 5M/t (4017–4018); the marginal bound reads own boxes up to diam_j\tilde□^2 + 5M. Their per-bond derivation (4070–4072) gives the same bound there with a fixed constant.
6. **Not traced:** the fixed (d, L) unit factor between the direct sizes of 4.26 (IV) and the class 𝔘 of CMP 102b (I-1).
7. **Inventory:** `mu-uses-sol.md` missed 4.29:prop-near-field-scope's hypothesis (CA-I 150365–150371), the same restriction statement (I-5').

**What this changes.** Every use of 4.13's content on T0's chain that `mu-radii.md` left open is now covered by `mu.md` (through (RR) and (CN)), each after a stated ceiling of the kind their order already admits. There are two exceptions. The first is the domination clause (defect 3), which the account takes from CMP 122b. The second is complex continuations on unbounded two-layer boxes (defect 4), which no on-chain consumer reads. Most of the uses are real. For the real uses, the complex nesting of `mu.md` §6 is not needed; the real restriction (RR) is enough. The ceilings for 4.29 and 8.5 read the account's own regularity parameters (ε_1^g, ε', ε^win) and are of the same form as the ceilings it already imposes.

**Verdict.** ADVANCE for the coverage claims marked "covered" in the table, as implications from `mu.md`, `mu-radii.md` §1, their CA-III 9.3 and CMP 102b Theorem 1 and Proposition 9 (cited inputs), and the account's own regularity hypotheses at each use. Defects 1 and 2 are corrections of their text (a citation that does not contain the step; a hypothesis too weak for the step), each with a repair. Defects 3 and 4 are honest non-claims. CA-III 9.1 is not assessed (off T0's chain).

Checked line by line by Claude (Mini worker).
