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
