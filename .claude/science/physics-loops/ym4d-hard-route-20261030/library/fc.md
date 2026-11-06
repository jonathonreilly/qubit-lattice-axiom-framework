lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T04:55Z

# FC: the current identification and the complex frame change for library/stage-claude.md

Row 392 (`fc`). Pinned at commit 7796b75f1. Work in progress; sections are written as they are finished.
Proved by Claude (Mini worker), not yet checked by the other model.

Moves: the two BLOCKs of `gates/stage-gate.md` on `library/stage-claude.md` Theorem S (FINISH row 388), that is, AD-ST(2) (registry row `AD-ST(2)`, owner `stage-claude`), inside H-STAGE, the first input of A10 on the T0 chain.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, checkout at 7796b75f1 (branch `claude/ym4d-hard-route`). Research text, not an audit; grants no status. Written arguments only. Sources: CA-I, CA-II (`theorem_0_complete_account_raw_{I,II}.tex`) and SA (`YM4_sketch_500.tex`) at `31a47c543775`, fetched into a scratch folder; Balaban CMP 109 pp. 272-273 read from the PDF page images in `~/ym4d-papers/`.

Credit: Tadeusz Balaban for the substitution CMP 109 (3.10)-(3.18) and the operators of CMP 99b, 102b. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account at `31a47c543775`: the response chart (CA-I 4.5), its diagonal exactness, nested criticality (CA-I 4.26), and 5.2:cor-response-dilation. Codex for `gates/stage-gate.md` and `library/prior/fc.md`.

## 0. Duplicate check (rule 0a)

Searched `library/open-core.md`, `library/l17c.md`, `library/open-registry.md` and the FINISH rows for: shift-map, stage-response-identification, AD-ST, PAIR, frame change, FC, nested criticality, second slot, partner current.

* **Match, named.** Registry row `stage-response-identification` ("Their identification and uniform bounds on the complete stage family remain unproved", `library/shift-map.md:1661`, owner `shift-map`, FINISH row 261, lane finished, open). The gate (`gates/stage-gate.md` §6, last paragraph) places the *partner-current match* inside this bridge. `library/shift-map.md` §18 Attack C (lines 1632-1640) already found that equality on the physical current graph does not fix the extension in the independent current. So this note does **not** attack the identity "actual current = chart current 𝔍(b) at independent J" as a proof target, and does not attack the layer match (M-chart).
* **Not covered elsewhere.** Row 392's second branch, the weakest replacement that every consumer of AD-ST(2) accepts, is not in shift-map's statement (shift-map's open lemma is Lemma R, the returned-pair velocity (67)). Section 1 takes that branch: it bounds the actual current increment directly, given the layer match that (M-chart) already assumes.
* The frame change (item 2) is listed only as the open lemma FC of `library/stage-claude.md:275` (owner `stage-claude`, this row's lineage). The open-core seven (CM, CR, CA, CW, CH, CO, CV) do not contain it. FC-test, FC-mean-match and FC6 (FCON, ST1) are different statements that share the letters.

## 1. Item (1): the current of the stage move

Kind: check of their text, plus a short new identity (Lemma C1) and its consequence. The gate's BLOCK at `gates/stage-gate.md` §6 (c) is closed by a replacement that every consumer of AD-ST(2) accepts, and that the account itself already uses in CA-I 4.5-4.7. No identification of two currents is needed.

### 1.1 Two second-slot rules, both in the account

Notation is the account's (CA-I 4.5). (U,J) ∈ 𝔖, so J is only bounded: (S3) |J|₍₋₃₎ < a_γ, "no relation between J and U is required" (CA-I 12968-12970). Balaban's space has the same freedom: CMP 109 (1.14) asks only |𝐉| < γ₀ (p. 262). Write 𝔒 := D*_U D_U + D_U R D*_U. By the definitions Δ_a := Δ + D_URD*_U + Q*aQ (CA-I 13587) and Δ' := Δ − D*_UD_U (CA-I 13617),

  𝔒 = Δ_a − Q*aQ − Δ'.   (1.1)

* **The literal CMP 109 rule.** Balaban, CMP 109 p. 272, (3.10)-(3.13): the new current is (L^{j−1}η)³𝐉 + Δ_U𝐀 − P₁𝐀 + 𝐅₁(U,𝐀). He obtains it from (3.11) by replacing D*D with D*D + DRD* = Δ_U − P₁ + (lower-order local operator), which is exact when RD*𝐀 = 0. In the account's normalization this is
  𝔏(U,h) := 𝔒h + F(U,h),  F(U,h) := 𝒥(e^{iηh}U) − 𝒥(U) − D*_UD_Uh  (CA-I 14083-14091, = CMP 109 (3.11)).
  CA-II uses this rule: 5.8:lem-local-slot writes 𝔏_s = (D*D + DR_sD*)ℍ_s + F(U_{s−1},ℍ_s) (CA-II 56853-56855); 5.8:rem-slot-rules, rule 1, "moves by the increment of [CMP 109 (3.13)]" (CA-II 58698-58700); the corollary's identification paragraph (CA-II 14119-14123) names the CMP 109 (3.10)-(3.12) increment.
* **The chart rule.** The chart's datum is the pair (e^{iηℋ^J(B)}U, J + 𝔍(B)) (CA-I 14419). CA-I uses this rule *in place of* CMP 109 (3.13) at free current: "Replace the functional of [CMP109 (3.13)] by Φ^𝕂 := 𝐄^{(j)}(X, e^{iξA(t_□)}𝐔, J + 𝔍(B(t),t_□))" (CA-I 19640-19647; again CA-I 29387-29394). The reason is stated: "The kernel slot 𝔍 takes the place of the member of [CMP109 (3.14)] involving the Laplacian, whose analogue at free current is not proved and is not used here" (CA-I 29392-29394). CA-I 5815-5819 records why: Balaban excludes the covariant-Laplacian bound for G_π and G₁ ("It does not hold for G, G₁", CMP 99b), and for H, H₁ "it is not proved at free 𝐉". The replacement is justified by far clause (F3): at the physical pair (U_{k+1}, J_{k+1}) the replaced functional "is the composite function of [CMP109 (3.7)]" (CA-I 19670-19673).

So the account contains both rules. CA-I's small-field step uses the chart rule; CA-II's stage corollary names the CMP 109 rule.

### 1.2 Lemma C1: the exact difference of the two rules

**Lemma C1.** Let (U,J) ∈ 𝔖 and |B| < c₉, at undecoupled operators (s ≡ 1). Put X_G := D^J(A_G) and λ := ΛH^JX_G, with Λ = G'RD*_U. Then

  𝔍(B) = 𝔏(U, ℋ^J(B)) + 𝔨_J(λ) + Λ^T𝔪_J(λ).   (1.2)

*Proof.* By CA-I (4.5:eq-response-chart-2) (CA-I 14444-14449, proved there from the representation identity) and (1.1),
  𝔍(B) = 𝔒A_G − 𝒦₁X_G + F(U, ℋ^J(B)),  𝒦₁X := Q*𝗄X + Λ^T𝔧_J(H^JX) − Δ'H^JX.
Since ℋ^J(B) = A_G − H^JX_G (CA-I 14398), 𝔏(U,ℋ^J) = 𝔒A_G − 𝔒H^JX_G + F(U,ℋ^J). The F terms are equal. Hence 𝔍 − 𝔏 = 𝔒H^JX_G − 𝒦₁X_G. By (J2) and (J4), (Δ_a − Θ'_J)H^J = Q*𝗊_Jℓ⁻¹ and ℓQH^J = 1 (CA-I 13765, 13768-13772, 13920). So, with (1.1),
  𝔒H^JX = Θ'_JH^JX + Q*𝗊_Jℓ⁻¹X − Q*aℓ⁻¹X − Δ'H^JX = Θ'_JH^JX + Q*𝗄X − Δ'H^JX,
because 𝗄 := (𝗊_J − a)ℓ⁻¹ (CA-I 14139) and a, ℓ are scalars on each layer. Subtracting 𝒦₁X gives 𝔒H^JX − 𝒦₁X = Θ'_JH^JX − Λ^T𝔧_J(H^JX). Finally Θ'_J = 𝔨_JΛ + Λ^T𝔧_J + Λ^T𝔪_JΛ (CA-I 13725), so the difference is 𝔨_J(ΛH^JX) + Λ^T𝔪_J(ΛH^JX). ∎

**Corollary C1'.** (a) The two rules agree wherever RD*_UH^JX_G = 0, since then λ = 0. This holds on the physical diagonal: at a true pair RD*_{U₀}H = 0 (CMP 99b (3.124); CA-I 15544-15548), and H^J = H there (CA-I 15552-15553). This recovers (K6)(b), CA-I 15691-15693. (b) Off the diagonal the account asserts neither RD*_UH^J = 0 (CA-I 13774) nor RD*_Uℋ^J = 0 (CA-I 14679-14681). So the identity "actual CMP 109 current = 𝔍(b) at independent J" is **exactly** the vanishing of 𝔨_J(λ) + Λ^T𝔪_J(λ). This term is linear in J and quadratic in b (X_G = O(|b|²), CA-I 13998). This note does not decide whether it vanishes (rule 0a: shift-map's bridge, §0). No consumer needs it (§1.3).

**Why the literal rule is the harder one.** The 𝔨_J term is bounded in |·|₍₋₃₎ (𝔨_J is pointwise, |𝔨_J(λ)|₍₋₃₎ ≤ 2|λ|₍₀₎|J|₍₋₃₎, CA-I 13715). The 𝔪_J term is not bounded by the account's inputs. Write 𝔪_J(λ) = m₃ + D*_Um₄, with m₄ a pointwise bracket of λ and J (CA-I 13717-13718). Then Λ^T𝔪_J(λ) contains D_UG'D*_Um₄ = ∇_UG'∇*_U m₄. This operator has order 0 and is bounded only "on Hölder data" (CA-I 13599-13609). The datum m₄ contains J, which is only bounded. So a uniform sup bound on 𝔏 at free J needs either a Hölder bound on J or the covariant-Laplacian member for H^J. The account withholds both (CA-I 13763, 5815-5819, 29392-29394). This is the same gap that made CA-I replace (3.13) by the chart rule. The account's CA-II stage corollary records the Laplacian layer bound N^Δ_y(ℍ) ≤ B_ℍ p(y) only as a cited input of the absent stage-layer theorem (CA-I 116658-116661).

### 1.3 What the consumers read: the replacement

AD-ST(2) has one reader, the Cauchy step of the stage argument (CA-I 54970-54984; `stage-claude.md` §2.3). Through 5.2:cor-response-dilation, that step reads the second slot 𝒦 = 𝒦(𝕌,𝕁,b,σ) only through four properties:

* (W1) **physical point.** At every physical point (U₀, J(U₀)) of the stage (real U₀ in the class of CA-I 15669-15680) and every real passing datum b: 𝕁 + 𝒦 = J(e^{iηℍ}U₀).
* (W2) **holomorphy and decoupling.** 𝒦 is holomorphic in (𝕌,𝕁,b,σ) and reads σ only through the decoupled primitive operators (CA-II 13286-13288, 14127-14129).
* (W3) **size.** ℓ³|𝒦(x)| ≤ 2K_χ p(y) at χ ≡ 1 (antecedent (c), used only at χ ≡ 1, CA-II 14076-14093).
* (W4) **zero datum.** 𝒦 = 0 at b = 0 (CA-II 14107-14109).

The corollary's other steps read 𝒦 only as the factor χ_t𝒦 (pointwise product, locality, CA-II 14100-14104).

**Lemma R (the physical density does not depend on the rule).** Let 𝒦 and 𝒦' both satisfy (W1) at every stage. Then the stage densities built with 𝒦 and with 𝒦' are equal at every physical point of every stage.

*Proof.* Induction on the stage. Stage 0 involves no rule. Assume the two stage-n effective actions agree at every physical point of stage n. Fix a physical point P₀ = (U₀, J(U₀)) of stage n+1 and real fluctuation variables (A_j,B_j) in the integration stratum of (S2) (CA-I 54287-54300), with real datum b. The first slot e^{iηℍ}U₀ is the same for both rules. By (W1) both second slots equal J(e^{iηℍ}U₀). This pair is the true pair of the shifted real background, a physical point of stage n. So the integrands of (S2) agree pointwise on the real integration domain, and so do the integrals. The localized pieces of the two expansions may differ off the diagonal; only their sum enters the density, and the sum is the integral. ∎

This is the stage form of CA-I far clause (F3) (CA-I 19670-19673). Credit: Sussman and Alpoge for the device.

**Proposition C2 (the chart rule supplies the replacement).** Assume (M-chart) of `stage-claude.md` §4 (the layer match ℍ = ℋ^J(b); the gate says it "need not be proved again", §6) and the chart's (K1), (K2), (K6), (K8), (K10) with their imports. Prescribe the stage second slot by the chart rule, 𝒦 := 𝔍(σ;b), exactly as CA-I 19640-19647 does for the small-field step. Then (W1)-(W4) hold, with K_χ := B_♯/2 at σ ≡ 1 and K_χ := e^{c_𝕂κ₁}B_♯/2 at |σ| ≤ e^{κ₁}.

*Proof.* (W1): (K6)(b) gives J + 𝔍(B) = J(e^{iηℋ^J(B)}U₀) at the physical point (CA-I 15691-15693, 15862). (W2): (K1) joint analyticity in (B,𝔞,J) (CA-I 14530-14540); (K10) items 1, 2, 4 for σ (CA-I 15322-15337). (W3): Lemma L of `stage-claude.md` §4, with the gate's repair of its summation (`gates/stage-gate.md` §4: B_♯ = n_bC^K₁₉₀c₁ from the kernel-algebra sum (4.5:eq-kernel-algebra-1)); at complex σ use (K10) item 2 as Lemma L's second bullet does. (W4): (K2), 𝔍(0) = 0 (CA-I 14669). ∎

**Theorem C (BLOCK (c) closed).** Under the premises of Proposition C2, step (c) of Theorem S holds for the stage move whose second slot is prescribed by the chart rule: ℓ³|𝒥^♯[1](x)| ≤ 2K_χ p(y) with 𝒥^♯[1] := 𝔍(σ;b). By Lemma R this prescription changes no physical density. So, with the gate's other repairs and its premises (SPACE) and (LOCAL), Theorem S gives AD-ST at radius R₀ ≍ ϑ⁻¹ for the chart-rule stage move. The current half of the gate's premise (PAIR) is no longer needed; its layer half is (M-chart).

*Proof.* Proposition C2 supplies (W1)-(W4). The corollary's proof reads the second slot only through (W2)-(W4) (§1.3). Its identification paragraph needs the move at χ ≡ 1 to be the stage's actual move. With the prescription, the actual move *is* the chart-rule move, and (W1) with Lemma R makes it the physical one. ∎

**What this changes, and what it does not.**
* It replaces the gate's demanded identity by a convention the account already uses (CA-I 19640-19673, 29387-29394). It is a port, not a new construction.
* Wording repair for the account (for the lead, not a contribution claim): CA-II 14119-14123 identifies 𝒥^♯[1] with the CMP 109 (3.10)-(3.12) increment. Read literally, antecedent (c) then needs the Laplacian member that CA-I 5815-5819 says is unproved at free current. Read with CA-I's replacement of (3.13), 𝒥^♯[1] = 𝔍 and (c) at χ ≡ 1 follows from (K8). Lemma C1 gives the exact difference between the two readings.
* Not checked here: the CA-II 5.8 machinery that names the literal rule (5.8:lem-local-slot, 5.8:rem-slot-rules, CA-II 56800-56870, 58687-58748). It is not a reader of AD-ST(2). It uses real children at σ ≡ 𝟏. If the chart rule is adopted on the T0 chain, those statements must be re-read with 𝔍; Lemma C1 is the conversion formula.

## 2. Item (2): the frame change at complex data

Kind: proof of the steps of Attack 9 that the account states only at a real background (CA-I 128485), then the reduction of FC to one constant lemma. The gate's three gaps before the constant condition (`gates/stage-gate.md` §5, steps 1, 3, 4: branch, common gauge, admission) are closed as implications from named imports.

### 2.1 Consumers first, and what the auxiliary configurations read

* FC has one consumer: (SRC) under the one-frame reading (R1) (`stage-claude.md` §5.1 and line 275). Under the birth-frame reading (R♭), Lemma F gives (SRC) with no frame change (gate §5, ADVANCE). The account works on Σ♭ spaces and assumes "the identification of the spaces written with Σ and with Σ♭" (CA-II 13982-13983; used at 14117-14119). Its quotation of CMP 122a p. 190 (CA-I 148155-148172) gives the seven bounds and U_{p,X} = U(𝔹_p(X) ∪ {Γ_i}_{i<p}, M·𝕌), but not which nest supplies the Γ_i at stage n. So item (2) is needed only by a T0 chain that imports Balaban's stage theorem on his spaces and reads them as (R1).
* **The auxiliary configurations read 𝐔 only.** CMP 109 p. 262, condition (iv), (1.15)-(1.16): the pair (U_n(M'(𝐔)), J_n(M'(𝐔))), "J_n(M'(𝐔)) is defined by the formula (1.8) with U_n(M'(𝐔))". CA-I 9843-9846 (= CMP 119 (2.34)-(2.39)): U_{p,X}(M·(𝐔)) = U(𝐁_p(X) ∪ {Γ_i}_{i<p}, M·(𝐔)), and Remark (c), CA-I 9902-9904. The independent current 𝐉 enters no composite entry. The gate's concern about "an independent-current complex pair" (§5, step 1) therefore reduces to complex 𝐔, and the real slice in 𝐔 is a full totally real slice. This is what makes analytic continuation available here, unlike in §1.

### 2.2 Setting and imports

Fix an ordinary stage n+1, j = h+n, and the collar R_n = Z_{j+1}∖Z''_{j+1} (CA-I 53809-53814). For a tower 𝔱 = 𝐁_p(X'') ∪ {Γ_i}_{i<p}, write M^𝔱 for its constraint map (its retained averages, CA-I 128525-128533) and U(𝔱,V) for Balaban's configuration with averaged data V. Let D be a tower of the stage-n frame with p ≥ j+1, and D' the tower of the stage-(n+1) frame with the same 𝐁_p(X'') (the Γ_i agree for i ≤ j−1; `stage-claude.md` §5.3). Let 𝒞⁺ be the set of D-constraints that are not D'-constraints. A point of the stage-(n+1) space has a representative 𝐔 = e^{iηA'}U with U real (conditions (i)-(iii), CA-I 9840-9886). Put

  Q(𝐔) := U(D', M^{D'}𝐔)  (new auxiliary configuration),  O(𝐔) := U(D, M^D𝐔)  (old one).

Imports, all named in the account and none proved here:
* (B1) *Analytic background maps.* U(𝔱,·) is holomorphic on a complex neighbourhood 𝒱_𝔱 of the regular real data, G-valued at real data, in the 𝔱-axial gauge, and M^𝔱U(𝔱,V) = V exactly. (CMP 102b Theorem 1, Proposition 6 and the polydisc (172); CMP 119 §2; analyticity of the averaging maps, Remark 4.5:rem-averaging-analyticity, stated in CMP 98 without proof.) We take 𝒱_𝔱 inside the set where (B2) holds at real points.
* (B2) *Real uniqueness.* At real regular exterior and data, the localized 𝔱-problem has exactly one critical configuration in the 𝔱-axial gauge in Balaban's analyticity domain (hypothesis (III) of CA-I 128485, CA-I 128569-128577, from CMP 109).
* (B3) *Nesting.* Every D'-constraint of the localized problem is a fixed function of finitely many D-constraints and of the exterior, so Feas_D(V) ⊂ Feas_{D'}(Φ(V)) with Φ fixed and holomorphic (CA-I 128485 clauses (b), (c) with hypothesis (I), CA-I 128538-128547 and 128596-128660; CMP 119 (2.11)-(2.12)). The two nests differ only at level j+1 on the collar (CA-I 53809-53814), so 𝒞⁺ consists of D-constraints read in R_n (the level-j collar rows 𝒞_j and their seams).
* (B4) *Covariance.* U(𝔱,V^ĝ) = U(𝔱,V)^g for gauge maps g with induced coarse map ĝ, and the stage spaces are unions of G^c-orbits, read representative-wise (CMP 109 (1.10); CA-I 13118, 29398-29399; chart covariance (K5) and (F4), CA-I 19673-19685).
* (B5) *Diagonal exactness of the chart at real true pairs* ((K6), CA-I 15669-15700).

### 2.3 Lemma N (the gate's "off-collar block-data agreement")

If M^{D'}𝐔 ∈ 𝒱_{D'}, then M^DQ(𝐔) = M^D𝐔 on every D-constraint outside 𝒞⁺, and Φ(M^DQ) = Φ(M^D𝐔).

*Proof.* By (B1), M^{D'}Q = M^{D'}𝐔. A D-constraint outside 𝒞⁺ is a D'-constraint, so it takes the same value at Q and at 𝐔. By (B3), Φ(M^DQ) = M^{D'}Q = M^{D'}𝐔 = Φ(M^D𝐔). ∎

### 2.4 Proposition NC^ℂ (the gate's "common, uniquely selected analytic branch")

For a representative 𝐔 = e^{iηA'}U put 𝐔_s := e^{isηA'}U. Let 𝒟 be the set of such 𝐔 with M^{D'}𝐔_s ∈ 𝒱_{D'} and M^DQ(𝐔_s) ∈ 𝒱_D for all s ∈ [0,1]. Then for 𝐔 ∈ 𝒟,

  U(D, M^DQ(𝐔)) = Q(𝐔)^{u(𝐔)},   (2.1)

where u(𝐔) is the gauge map, equal to 1 at D's coarse base points, that puts Q(𝐔) in the D-axial gauge. u is a product of link variables of Q(𝐔) along the D-axial trees, so it is holomorphic in 𝐔 and G-valued at real 𝐔. There is no boundary-layer proviso: both sides are solutions of localized problems with the same exterior.

*Proof.* *Step 1, real points.* Let 𝐔_ℝ ∈ 𝒟 be real. Then Q_ℝ := Q(𝐔_ℝ) is real and critical for the localized D'-problem with data M^{D'}𝐔_ℝ (B1, B2). By (B3) and Lemma N, Q_ℝ ∈ Feas_D(M^DQ_ℝ) ⊂ Feas_{D'}(M^{D'}𝐔_ℝ). By clause (a) of CA-I 128485 (CA-I 128589-128595; its proof is the inclusion of tangent spaces, CA-I 128622-128627), Q_ℝ is critical on Feas_D(M^DQ_ℝ). The map u is 1 at the coarse base points, so Q_ℝ^u has the same D-data (B4), lies in the D-axial gauge and is critical. By (B2), Q_ℝ^u = U(D, M^DQ_ℝ).
*Step 2, an open real set.* 𝒟 is open, since each 𝒱 is open and [0,1] is compact. Its real points form an open set of real configurations, on which F(𝐔) := U(D, M^DQ(𝐔)) − Q(𝐔)^{u(𝐔)} vanishes by Step 1.
*Step 3, continuation.* F is holomorphic on 𝒟 (compositions of holomorphic maps, (B1)). Fix 𝐔 ∈ 𝒟. For s ∈ [0,1] the point 𝐔_s lies in 𝒟, because (𝐔_s)_{s'} = 𝐔_{ss'}. So the connected component of 𝒟 containing 𝐔 contains the real point U and a real neighbourhood of U. The real points (G-valued bond variables) form a totally real submanifold of maximal dimension in the complexified group. A holomorphic function that vanishes on a nonempty open set of real points has all derivatives zero there, so it vanishes on the connected component. Hence F(𝐔) = 0. ∎

This closes gate §5, step 1, at complex data: the branch is the analytic continuation of the real one, and it is unique because both sides are single-valued holomorphic maps on 𝒟.

### 2.5 Lemma G (the gate's "common gauges"; the size of the collar datum)

Let κ bound, in level-j units, the level-j curvature of M^j𝐔 and of M^jQ on R_n. Then the orbit of 𝐔 has a representative 𝐔^g, with g = 1 at every D'-base point (so Q(𝐔^g) = Q(𝐔)), such that for every c ∈ 𝒞⁺,

  |δd(c)| ≤ ‖Ad_{h_Q}‖·(2C_axLκ + C_BCH(dLκ)²),  δd(c) := (iη)⁻¹ log(M^jQ(c)⁻¹ M^j(𝐔^g)(c)),   (2.2)

with C_ax := (d−1)/2. Moreover O(𝐔^g) = O(𝐔)^{g̃} by (B4), so the old composite entries of the orbit may be read at 𝐔^g, up to the factors ‖Ad_{g̃}^{±1}‖ (equal to 1 at real 𝐔).

*Proof.* On one level-(j+1) block of R_n (side L in level-j steps), let h_W be the level-j gauge map that is 1 at the block's coarse base point and puts a level-j field W in the comb axial gauge from that point. In this gauge a link off the tree is an ordered product of at most (d−1)L/2 plaquette holonomies, each transported along tree paths. Each holonomy has |log| ≤ κ (times ‖Ad‖ of the transport at complex data), so by the Baker-Campbell-Hausdorff bound |log W^{h_W}(c)| ≤ C_axLκ + C_BCH(dLκ)². Put h := h_Q⁻¹h_𝐔 with h_Q := h_{M^jQ}, h_𝐔 := h_{M^j𝐔}. It is 1 at the coarse base point. Let g be constant on each level-j block of R_n, equal there to h at that block's level-j site, and g = 1 off R_n. By the covariance of Balaban's averages, M^j(𝐔^g) = (M^j𝐔)^h on R_n, and g = 1 at every D'-base point, so M^{D'}𝐔^g = M^{D'}𝐔. In the frame h_Q both fields are axial: (M^jQ)^{h_Q} by definition, and (M^j𝐔^g)^{h_Q} = (M^j𝐔)^{h_Qh} = (M^j𝐔)^{h_𝐔}. So each link of each field has |log| ≤ C_axLκ + C_BCH(dLκ)². Finally (W^{h})(c)⁻¹W'^{h}(c) = h(c₊)W(c)⁻¹W'(c)h(c₊)⁻¹, which gives (2.2). ∎

The gate's objection is right as a statement about arbitrary representatives: "existence of a small axial representative separately for each field does not identify their representatives" (§5, step 3). Without the choice of g, δd can be of order one: a gauge map that is trivial at the coarse points leaves Q unchanged and moves M^j𝐔 arbitrarily. Lemma G removes this by choosing the representative, which (B4) permits.

### 2.6 Lemma S (the gate's "admission of the joining segment")

Assume the γ-ceilings under which (Q^u, J(Q^u)) lies in the chart class 𝔖 of CA-I 12936-12972 (for a D-background at data near regular real data, by (B1) and CMP 102b Theorem 1) and |δd| < c₉/2 (by (2.2), |δd| = O(Lκ), a γ-ceiling). Then, with the response chart of CA-I 4.5 taken in the frame D at the pair (Q^u, J(Q^u)),

  O(𝐔^g) = e^{iηℋ(δd)}Q^u,  J(O(𝐔^g)) = J(Q^u) + 𝔍(δd),   (2.3)

and the joining segment t ↦ tδd, t ∈ [0,1], lies in the chart's datum ball.

*Proof.* By (2.1) and Lemma N, O(𝐔^g) = U(D, V₁) and Q^u = U(D, V₀), where V₀ = M^DQ and V₁ = M^D𝐔^g differ only on 𝒞⁺, and V₁ = V₀e^{iηδd} there. At real 𝐔 and real t, (K6)(a)-(b) (CA-I 15688-15697) give U(D, V₀e^{iηtδd}) = e^{iηℋ(tδd)}Q^u and the current identity, since (Q^u, J(Q^u)) is then a real true pair. Both sides are holomorphic in (𝐔, t) ((K1) and (B1)). Here the current is J(Q^u), a function of 𝐔, not an independent variable, so the real points form a full totally real slice, connected to each point as in Step 3 above. So (2.3) holds at complex 𝐔. The ball |tδd| ≤ |δd| < c₉/2 is convex; this is the admission of the segment. ∎

### 2.7 Theorem FC': the frame change, reduced to one constant condition

**Theorem FC' (implication).** Assume (B1)-(B5); Lemma L of `stage-claude.md` §4 (with the gate's summation repair) in the frame D at the pairs (Q^u, J(Q^u)); the first-order curvature line of ST1 Lemma 7 (46) (curvature increment ≤ 4N_y, as in Theorem S (g)); and the γ-ceilings of Lemmas G and S. Let C_av bound the level-j curvature of a Balaban average by the fine curvature it averages (CMP 98), so that on R_n

  κ ≤ κ_{n+1} := C_av c_{n+1}(j+1) L₀^{2e_{j+1}} α_{0,j+1} L⁻²  (level-j units),

from entry 1 (for 𝐔) and entry 2 of the new frame (for Q) at level j+1; here c_{n+1}(·) is the stage-(n+1) schedule factor and e the exponent of the L₀ weight (CA-I 49604-49640). Then at every sited point y of level m, the old composite entries 2 and 4 of the orbit exceed the new ones at y by at most

  ε_Ad + 4B_♯ |δd| e^{−δ_L d(y,𝒞_j)} / (L₀^{2e_m}α_{0,m}),  |δd| ≤ 2C_axL κ_{n+1}(1 + O(dLκ_{n+1})),   (2.4)

in units of the clause, where ε_Ad collects the factors ‖Ad_u‖, ‖Ad_{h_Q}‖, ‖Ad_{g̃}‖ − 1 (zero at real 𝐔, a γ-ceiling otherwise). Hence FC holds if, at every m,

  (FC*) 8B_♯C_axC_av · (L₀^{2e_{j+1}}α_{0,j+1})/(L₀^{2e_m}α_{0,m}) · L⁻¹ · e^{−δ_L d_m} ≤ ½β2^{−|m−j−1|} − ε_Ad,

with d_m the least scaled distance from 𝒞_j to points of level m.

*Proof.* Lemma G gives the representative 𝐔^g and (2.2). Proposition NC^ℂ gives (2.1) and Lemma S gives (2.3): O(𝐔^g) = e^{iηℋ(δd)}Q^u. Lemma L bounds N_y(ℋ(δd)) and ℓ³|𝔍(δd)| by B_♯|δd|e^{−δ_Ld(y,𝒞_j)}. The curvature of e^{iηℋ}Q^u differs from that of Q^u by at most 4N_y(ℋ) in the units η²ℓ_m⁻² (ST1 Lemma 7 (46)); entry 4 moves by ℓ³|𝔍| ≤ B_♯|δd|e^{−δ_Ld}. The new clause bounds Q, and Q^u differs from Q by Ad_u. Dividing by the clause unit L₀^{2e_m}α_{0,m} gives (2.4); inserting (2.2) and κ_{n+1} gives (FC*). ∎

**Where (FC*) binds.** For m ≥ j+2 or m ≤ j−1 the factor e^{−δ_Ld_m} beats 2^{|m−j|}·(1+β₀)^{|m−j|}L₀^{2|m−j|} once the nest separation, measured in the scaled metric, is at least (log 2(1+β₀)L₀²)/δ_L: a floor on M, chosen after L (CA-I 1468-1649). The two layers that touch the collar remain:
* m = j (the persistent level-j layer): with α_{0,j+1} ≤ (1+β₀)α_{0,j} (CA-I 127217-127218) and e_{j+1} = e_j + 1 in the zone I_M, (FC*) reads
  **32 B_♯C_axC_av(1+β₀) L₀² ≤ β L**   (FC*_j)
  (that is, 2C_fcC_axC_av(1+β₀)L₀²/L ≤ β/4 with C_fc := 4B_♯). This is `stage-claude.md`'s (FC-num), now with the averaging constant C_av made explicit and with every premise before it proved.
* m = j+1 (inside Ω_{j+1}, next to the collar): (FC*) reads 16B_♯C_axC_av ≤ βL, which (FC*_j) implies since L₀ ≥ 1.
* On the collar itself (old level j, new level j+1), the new entry of Q is smaller than the old clause's unit by the factor (1+β₀)L₀²L⁻², so the old entry need only stay below the full stage-(n+1) bound, which (FC*_j) also implies.

So, under (R1), **FC ⟸ (FC*_j)** plus γ-ceilings and a floor on M. With β = 1/4, β₀ = 1/7, C_ax = 3/2 (d = 4): B_♯C_av L₀² ≤ 7L/1536.

### 2.8 The open lemma, attacked three ways

**Lemma CC (open).** There is an admissible L with 32 B_♯(L)C_axC_av(L)(1+β₀)L₀² ≤ βL, where B_♯ is Lemma L's collar-response constant for the frames of the stage nests (or, in the flux form below, its curvature-to-flux analogue).

* **Attack A1 (direct, fixed L).** (FC*_j) is a numerical condition on C^K₁₉₀, c₁, n_b and C_av. These are (d,L)-numbers that the account never computes and places right after L (CA-II 2277-2278). B_♯ = n_bC^K₁₉₀c₁ ≥ n_b ≥ 2d, so with L₀ ≥ 1 one needs at least L ≥ 1536·8/7 ≈ 1755 times C^K₁₉₀c₁C_av. No source supplies these numbers. *Fails: no supplier.*
* **Attack A2 (L large, L₀ fixed).** The account allows L₀ ≥ 1 with L₀² ≤ L/3 (CA-I 45849), so L₀²/L → 0 as L grows, and (FC*_j) becomes a floor on L iff B_♯C_av = o(L). But the account's own bound on B_♯ grows like a power of L. Lemma L's B_♯ contains C^K₁₉₀, obtained through the kernel algebra, whose clause (i) costs C L^{d+4} c₁ per application (CA-I 13433-13438). That factor pays the exchange of level factors between adjacent levels, which carries no decay ((|j−j'|−1)₊ = 0 for |j−j'| = 1, CA-I 13471-13485). So with the account's constants B_♯ ≳ L^{d+4} and (FC*_j) fails for every large L. *Fails: the account's constants grow faster than L.*
* **Attack A3 (flux form, `stage-claude.md` (FC-L)).** The response to a pure-gauge datum δd = D_jλ (λ = 1 at the coarse base points) is a gauge map of Q^u, so the curvature change depends only on the level-j flux of δd, which is at most 2κ_{n+1}(1 + O(|δd|)). With a curvature-to-flux constant C'_fc this removes the factor L: the condition becomes 8C'_fcC_av(1+β₀)L₀² ≤ βL². But (K8) bounds the response by sup|B| (CA-I 14842-14862), not by the flux of B, so C'_fc is not supplied; bounding it by (K8) returns to A1-A2. An L-uniform curvature-to-flux bound would be an L-uniform Schauder-type estimate for Balaban's block-constrained minimizers, which no source in reach states. *Fails: no supplier for C'_fc.*

None of the three attacks gives a counterexample. (FC*_j) is a sufficient condition from upper bounds; the true response constants may be far smaller. So FC under (R1) is **neither proved nor refuted**: it is reduced to Lemma CC.

**Consequence for the route.** The frame change is not on the T0 path if the chain reads the stage spaces as (R♭), as the account does (Lemma F, gate §5 ADVANCE). Lemma CC is needed only to import Balaban's stage theorem on (R1) spaces. The constant problem of A2 is also a hint, not a proof, that Balaban's own bookkeeping is of the (R♭) kind: with (d,L)-numbers fixed after L, the one-frame comparison cannot be paid from the stage gap.
