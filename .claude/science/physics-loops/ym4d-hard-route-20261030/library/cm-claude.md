lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T11:38Z

# CM: Claude attack on prescribed-word continuation (2.4:prop-m-freeness)

Queue row 345 (`cm-claude`). Commit a34245012. Proved by Claude, not yet checked by the other model. Research-stage working state; no status.

Credit: the statement, its words and its constants are Ethan Sussman and Levent Alpoge's complete account (with Claude and Codex as authors of their text), commit 31a47c543775. The background estimates go back to Balaban (CMP 95-122). The three earlier rounds are Codex's (`library/mf.md`).

(Sections follow as they are written.)

Sources: CA-I/II/III = `theorem_0_complete_account_raw_{I,II,III}.tex` at 31a47c543775, fetched once into `/tmp/cmclaude-src/`. SHA-256 of I, II and the outline match those in `open-core.md` §2; III is `7e36523b…a352d`. Numbers are raw TeX lines. Read before writing: `mf.md` (three rounds, nine attacks, whole), `cwch.md` §4 (Codex's CM consumer check), `l17c.md` §§1, 6, 7 and Result, `open-core.md` §§1–4 and 6.2, `port-map.md` rows 6 and 105.

Kind of result: proof of the step they mark incomplete (CA-II 59607–59609), as an implication from an input they admit, with a rate correction that changes no condition; plus a proof from their proved operator theorem on a smaller class; plus one precise open lemma for rebuilding the cited input.

## 1. Verdict in brief

1. **Consumer check first** (the row asks for it). Every reader of the proposition and of the letter μ₀ is listed in §2, with what it reads.
2. **New finding.** The companion clause (∗) is already an implication from an input the account admits. Clause (II) of the random-walk input (b3), CA-II 2181–2264, covers the member C_{Λ*}^{1/2} of its list. It bounds that companion at local data, on Balaban's analyticity space over every union Z ⊇ Z₀′ of cubes, for |𝗌(Δ)| ≤ e^{κ₁} and every M above its floors, by B_W e^{−δ_W ρ}. The rate is δ_W, not μ₀. Codex's consumer table (`cwch.md` §4.1) does not use this clause.
3. **The rate change is free** (Lemma R, §3). Put μ̂₀ := min{μ₀, δ_W}. No floor on M changes, no rim constant changes, and no width changes. The only reader of μ₀ that is not at a true pair is the Stage-6 floor μ₀M ≥ 2κ₁, and μ̂₀M ≥ 2κ₁ is the conjunction of two floors already imposed.
4. **Own route** (Theorem 1, §4). For local complex data about a global real base (the local balls of clause (H) of the operator theorem at free current), the companion family is proved here from that theorem, which the account proves. The proof integrates the resolvent sheets of its clause (D) term by term in the spectral parameter. It gives rate δ₀ and amplitude B₀(m₁/2)^{1/2}, both (d,L)-numbers. This removes the citation for that class.
5. **Open** (§5–§6): (b3) is cited (Balaban CMP 99b Theorem 3.15, CMP 116 (1.7)–(1.11)); it is the leaf `5.2:lem-random-walk-bounds`. Rebuilding its companion clause at data whose real part is given only locally is the one precise open lemma. Three new attacks are recorded with the exact reason each stops.

## 2. Consumer check (the l17c strategy, done first)

**What the account states.** CA-I 2239–2251 and CA-II 59574–59586 (the same proposition; CA-II 59590–59592 says so). At "backgrounds given only as local data on the cells of the one family of cells", the kernel 𝒦 = G_W obeys |𝒦(x,y)| ≤ B_W e^{−δ_W|x−y|}, and "the companion kernel of the random-walk expansion of that operator satisfies its exponential bound with decay rate μ₀", with (B_W, δ_W), μ₀ "the M-free constants of the same two bounds for backgrounds in the global regularity class". The proof (CA-II 59594–59609) supplies the first bound at local data and marks the second as (∗).

**Search.** Both labels; the phrases "companion kernel", "random-walk input", "one family of cells", "decomposition of the density"; every literal `\mu_0` in I–III; every `\delta_1M` in II. The phrase "decomposition of the density" occurs only in the two statements of the proposition (CA-I 2241, CA-II 59576). Unrelated meanings of μ₀ (Gaussian measures at I 7308–8750 and II 3611; measures at II 84681–84846; local constants at II 35927–35937, II 90506, III 91964–93549, III 106558; walk majorants at I 100661–102187) are excluded.

| # | Consumer, lines | What it reads | Accepts the corrected (∗′) below? |
|---|---|---|---|
| 1 | Order of choice, Stage 5 and 6: CA-I 1500–1551, 2058–2084 | Kernel constants placed after M₁, M₁^♯, κ₁ and before Θ₁, ϖ_T, r′, ℓ, M; three floors μ₀M ≥ 2κ₁, δ_WM ≥ 2κ₁, δ_WM/4 ≥ 32κ₁ + 2log(LM) + C(d,L). "it is used for no placement and for no side" (I 1535–1536). | Yes. μ̂₀ is a (d,L)-number placed with μ₀ (Lemma R (a)); its floor is implied by the first two (Lemma R (c)); the third floor does not read μ₀. |
| 2 | Hypothesis (A2) of `2.4:prop-order-consistent`, CA-I 2325–2345; its one use, 2403–2409 | "The two kernel estimates hold at local data on the one family of cells, with the M-free constants (B_W,δ_W) and μ₀, for every cube size M." | Yes, with μ̂₀ for the companion: that is (b3)(II) for 𝓜 = C_{Λ*}^{1/2} (row 9). |
| 3 | Rim constants, CA-II 8521–8545; admitted-input order 2405–2420; M-floors 2840–2850 | μ₀ := the Combes–Thomas rate of (γ₀, B_𝒜, δ_𝒜) (II 8527–8528). K₀ := max{(2B_𝒜/γ₀)C_ρ(μ₀/2), B²C_ρ(δ_W/2)}, δ₁ := min{μ₀/2, δ_W/2}, Θ₁ := max{1, K₀C_ρ(δ₁)}; floors δ₁M/M₁ ≥ 2, δ₁M ≥ κ₁. The first member of K₀ bounds T = −C_Λ𝒜_{Λ𝔯} at true pairs (II 10465–10471); the second bounds T₀ by clause (a) of the random-walk bound (II 10494–10495). | Yes, unchanged. δ₁ is unchanged (Lemma R (b)); K₀ keeps μ₀ in its true-pair member. |
| 4 | Root lemma `5.2:lem-covariance-root`, CA-II 10104–10186 (proved) | C_Λ^{1/2} at σ = 𝟙 at a true pair: ‖C_Λ^{1/2}(b,b′)‖ ≤ 2γ₀^{−1/2}e^{−μ₀ρ(b,b′)}. Its last paragraph (10182–10185) leaves the σ-family to "the random-walk expansion of this section", that is (b3). | Not a local-data use. It keeps μ₀; any smaller rate is weaker. |
| 5 | Positivity scope, CA-II 10465–10495 | μ₀-readers are at true pairs. "Elsewhere in that proof, at complex pairs and at pairs that are not true pairs, only bounds on kernels and on differences of kernels are used, namely in clause (i) of the M-freeness …, in the conditional-mean lemma and in the tolerance lemma. In particular, the reference transfer operator T₀ … is bounded there by clause (a) of the random-walk kernel bound" (10491–10495). | Yes. No local-data use of a companion bound at rate μ₀ occurs in the correlation theorem. |
| 6 | ψ-free remnants, CA-II 12346–12357, 12370–12384 | Rate δ₁MŘ_{k+1}; "expanded in random walks by the random-walk input" (12378–12380). | Yes. δ₁ unchanged. |
| 7 | Old terms beside a new region, CA-II 59540–59568 | "The same step also uses the independence from M of the kernel constants and of the decay rate of the random walk. This is not a printed sentence; it is Proposition 5.10:prop-m-freeness" (59566–59568). The step itself is Balaban's sentence, cited as printed; the account takes its containment by statement (II 4168–4177, hypothesis (a); II 4321–4324, Case 3). Its demand on the companion is not displayed. | Yes, as far as anything is displayed. The M-free random-walk constants at Balaban's analyticity spaces are stated by (b3) at (B_W, δ_W). Any later proof of Balaban's sentence must name its class; see §5. |
| 8 | Assembly, CA-III 110846–110866, 111066–111079; open list 111410–111412 | Order-consistency and the proposition, by name. | Yes. |
| 9 | Random-walk input (b3), CA-II 2181–2264 (supplier, not consumer) | For 𝓜 ∈ {𝒜, C_{Λ*}, C_{Λ*}^{1/2}, C_I}: "For every union Z ⊇ Z₀′ of cubes, the operator 𝓜(𝗌;𝐔,𝐉) is holomorphic on {|𝗌(Δ)| ≤ e^{κ₁}} times Balaban's analyticity space over Z, under δ₁M ≥ κ₁"; "the kernel depends on (𝐔,𝐉) restricted to Z only"; (II) \|𝓜(𝗌)(b,b′)\| ≤ B_W e^{−δ_W ρ(b,b′)}, B_W := Be^{16κ₁}, "with B, δ_W numbers depending on (d,L)" (2207–2211). Same statement: `5.2:lem-random-walk-bounds`, CA-II 8922–8940, status CITED (CMP 99b Theorem 3.15). | It is the supplier of (∗′). |

**The corrected clause.** Put μ̂₀ := min{μ₀, δ_W}.

> (∗′) For every Z ⊇ Z₀′ as in (b3), every (𝐔,𝐉) in Balaban's analyticity space over Z, every 𝗌 with |𝗌(Δ)| ≤ e^{κ₁}, and every M above its floors: |C_{Λ*}^{1/2}(𝗌;𝐔,𝐉)(b,b′)| ≤ B_W e^{−μ̂₀ρ(b,b′)}.

**Proof that (b3) implies (∗′).** By (b3)(II) for 𝓜 = C_{Λ*}^{1/2}, the left side is at most B_W e^{−δ_Wρ(b,b′)}. Since ρ ≥ 0 and δ_W ≥ μ̂₀, e^{−δ_Wρ} ≤ e^{−μ̂₀ρ}. B_W = Be^{16κ₁} and δ_W read only (d,L) and κ₁, so the constants are M-free and are fixed before Θ₁, ϖ_T, r′, ℓ and M (Stage 5 lets the kernel constants read d, L, M₁, M₁^♯ and κ₁: CA-I 2064–2066). The holomorphy, the locality in Z and the range of 𝗌 are those of (b3). ∎

**Verdict of the check.** Every consumer in the table accepts (∗′). (∗′) is an implication from (b3), an input the account already admits and uses in its correlation theorem (II 12927–12928 lists it among the hypotheses). So, at the account's own citation standard, the step marked (∗) is not an independent gap: it is clause (II) of (b3) for one of its four members, read at a rate the floors already cover. For our chain, which must rebuild cited inputs, CM merges into the leaf `5.2:lem-random-walk-bounds`. The prescribed-word display of `open-core.md` (CM) is stronger than any consumer reads; `cwch.md` §4.1 already found that no consumer uses the binomial weights and that the consumers accept an aggregate bound.

**Why this was missed.** `mf.md` §1 identifies the companion with the root lemma, notes that its last paragraph "sends the decoupled family back to the assigned random-walk expansion", and then asks for that family at the fixed rate μ₀. (b3) is that assigned expansion, and it states the bound at δ_W. The fixed-rate demand is the whole difference, and Lemma R shows no consumer needs it.

## 3. Lemma R: the rate correction changes no condition

**Lemma R.** Let μ₀ > 0 and δ_W > 0 be the (d,L)-numbers of the order (5.1:eq-admitted-inputs-b), CA-II 2412–2420, and put μ̂₀ := min{μ₀, δ_W}. Then:

- (a) μ̂₀ > 0 is a (d,L)-number. It can be placed directly after μ₀ in that order, and in Stage 5 of CA-I with the other kernel constants.
- (b) min{μ̂₀/2, δ_W/2} = min{μ₀/2, δ_W/2}.
- (c) For every M > 0 and c ≥ 0: μ̂₀M ≥ c if and only if μ₀M ≥ c and δ_WM ≥ c.
- (d) For every ρ ≥ 0 and every rate r ≥ μ̂₀: e^{−rρ} ≤ e^{−μ̂₀ρ}.

**Proof.** (a) The minimum of two positive numbers is positive. μ̂₀ reads only μ₀ and δ_W, which stand before it; no condition in the group before it reads it. (b) Halving is increasing, so min{a,b}/2 = min{a/2, b/2}. Hence min{μ̂₀/2, δ_W/2} = min{μ₀/2, δ_W/2, δ_W/2} = min{μ₀/2, δ_W/2}. (c) If μ̂₀ = μ₀ ≤ δ_W, then μ₀M ≥ c gives δ_WM ≥ μ₀M ≥ c; the converse is immediate. The case μ̂₀ = δ_W ≤ μ₀ is the same with the roles exchanged. (d) t ↦ e^{−tρ} is non-increasing for ρ ≥ 0. ∎

**What changes in the account.** Replace μ₀ by μ̂₀ in two places only: the companion clause of the proposition (CA-I 2247–2248, CA-II 59582–59583, and its restatement in (A2), CA-I 2339–2341), and the first Stage-6 floor (CA-I 1548, 2082). Keep μ₀, the Combes–Thomas rate, in the root lemma (CA-II 10109–10120) and in the first member of K₀ (CA-II 8536), which are read at true pairs only (row 5 of §2). Then:

- the admissible set of M is unchanged, by (c), because δ_WM ≥ 2κ₁ is already imposed (CA-I 1548);
- δ₁ = min{μ₀/2, δ_W/2} is unchanged, by (b), and so are the floors δ₁M/M₁ ≥ 2 and δ₁M ≥ κ₁ (CA-II 2845), and K₀, Θ₁, ϖ (CA-II 8536–8545);
- no width, ceiling or radius reads μ̂₀ except through these;
- by (d), the original clause at μ₀ implies the corrected one. This is a weakening of their statement, not a refutation.

So the corrected proposition has the same order of choice, letter for letter. This is the l17c pattern in its simplest form: the weaker statement is proved (by (b3), §2), and every consumer reads it.

## 4. Theorem 1: the companion from the operator theorem, on local balls

§2 closes (∗) at the account's citation standard. Our chain must rebuild cited inputs, so this section proves the companion clause from a statement the account proves, `4.14:thm-operator-theorem` (CA-I 46035–46129, status PROVED; our port `port/p4-operator.md`, A9). The class is the local balls of its clause (H): complex data given only near the walk, about a real base given on the whole lattice.

**Inputs used, all from CA-I.** Notation 4.14 (45237–45330): m₁ = γ₀/4, δ₀ = μ₁/4, B₀ = 12·2^d/m₁, ε₁ = γ₀/(8γ₁), all (d,L)-numbers. Clause (B): Re 𝖰 ≥ m₁ on 𝒰(ε₁). Clause (D) with its proof (47864–47884): for every 𝔹 ⊂ 𝔹⁺ and every x ≥ 0, (x+𝖠)^{−1} ∈ 𝒮_u[M/4; B₀m₁/(m₁+2x), δ₀; ε₁], "with walks and domains independent of x". Clause (G) (48012–48017): "Each walk of n steps in the expansion of (x+𝖠)^{−1} carries the factor (1+2x/m₁)^{−(n+1)}", and the unit words are products of factors (48021–48022). Clause (I): the constants depend on d and L only. The decay property (Sh3) of a sheet, in the form displayed at 46616–46632: for each walk ν and blocks y, y′ of the unit frame, ‖χ_y T_ν χ_{y′}‖ ≤ a_ν(y) e^{−δ d(ν;y,y′)}, with Σ_ν a_ν(y) ≤ B (the frame has one level, so the scale factor is 1; 47889–47890). Lemma `4.14:lem-local-balls` (46800–46950, PROVED).

Two readings of the sheet calculus are used and are named here, because the account states that calculus only by name (our port keeps it as the named input P4-H-sheet):

- **(Inv-x)** Each term R_ν(x) of (x+𝖠)^{−1} is continuous in x ∈ [0,∞). Reason given in the account: the terms are products of factors (48021–48022), the x-dependent factors are one-box resolvents, and an accretive matrix B with Re B ≥ m₁ has (x+B)^{−1} analytic in x on Re x > −m₁ (Step 1 below).
- **(Sh3-u)** The coefficients a_ν(y;x) of (Sh3) hold at every point of the analytic ball 𝒰(ε₁), not only pointwise. This is the form displayed at 46629 (coefficients built from the norm bound, not from the datum) and the form of hypothesis (W′), item 5 (CA-I 5547–5552).

**Theorem 1.** Assume the hypotheses of `4.14:thm-operator-theorem`, fix 𝔹 ⊂ 𝔹⁺, and put 𝖠 = 𝖰_{𝔹𝔹}. For a walk ν of the sheet of (D) and a point 𝗎 of 𝒰(ε₁), put

  𝖬_ν(𝗎) := (1/π) ∫₀^∞ x^{−1/2} R_ν(x;𝗎) dx.

(a) The integral converges absolutely, entrywise. The series Σ_ν 𝖬_ν(𝗎) converges absolutely, entrywise, to 𝖲(𝗎) := (1/π)∫₀^∞ x^{−1/2}(x+𝖠(𝗎))^{−1}dx. This is the formula by which the account defines the root, `5.2:eq-covariance-root-1` (CA-II 10114–10116), and by which Balaban defines C^{1/2}(σ) (CMP 116 (2.7), as described at CA-II 8948: "At σ = 𝟙 the operator C_Λ^{1/2}(σ) of [(2.7) CMP 116] is the square root of C_Λ supplied by the square-root lemma").

(b) For every walk ν and blocks y, y′: ‖χ_y 𝖬_ν(𝗎) χ_{y′}‖ ≤ ã_ν(y) e^{−δ₀ d(ν;y,y′)}, with Σ_ν ã_ν(y) ≤ B₀ (m₁/2)^{1/2} = 12·2^d (2m₁)^{−1/2}. The coefficients ã_ν(y) do not depend on 𝗎. The same holds with the roles of y and y′ exchanged.

(c) Each 𝖬_ν is analytic on 𝒰(ε₁).

(d) **Local balls.** Let U ∈ 𝒰_ℝ be given on the whole lattice, and let (A′,J) be given only on [ν]^≈, with every member of ‖(A′,J)‖_⋆ smaller than ε₁/2 there. Then 𝖬_ν is defined on this local ball by its value at the point (e^{iηχA′}U, χJ) of `4.14:lem-local-balls` (β). The value does not depend on the extension of the data. So defined, 𝖬_ν is analytic on the local ball and obeys (b) with the same coefficients.

(e) The constants B₀(m₁/2)^{1/2} and δ₀ depend on d and L only. They do not depend on M, k, K, the nest, 𝔹, the volume or g. They can be fixed at Stage 5 of CA-I, and in the (d,L)-group of (5.1:eq-admitted-inputs-b), before Θ₁, ϖ_T, r′, ℓ and M.

**Proof.**

*Step 1 (one accretive matrix).* Let B be a finite complex matrix with Re⟨v,Bv⟩ ≥ m₁|v|² for all v, m₁ > 0. For complex x with Re x > −m₁ and every v: |v|·|(x+B)v| ≥ Re⟨v,(x+B)v⟩ ≥ (Re x + m₁)|v|². So x+B is injective, hence invertible (finite dimension), and ‖(x+B)^{−1}‖ ≤ (Re x + m₁)^{−1}. Its entries are rational functions of x with no pole in Re x > −m₁ (Cramer's rule; the determinant does not vanish there). In particular they are continuous on [0,∞). This is the reason recorded in (Inv-x).

*Step 2 (the scalar integral).* For a > 0: (1/π)∫₀^∞ x^{−1/2} a/(a+x) dx = a^{1/2}. Substitute x = at², dx = 2at dt: the integral becomes (1/π)∫₀^∞ (a^{1/2}t)^{−1}·(1+t²)^{−1}·2at dt = (2a^{1/2}/π)∫₀^∞ dt/(1+t²) = a^{1/2}. With a = m₁/2, the function B₀m₁/(m₁+2x) equals B₀ a/(a+x), so (1/π)∫₀^∞ x^{−1/2} B₀m₁/(m₁+2x) dx = B₀(m₁/2)^{1/2}.

*Step 3 (measurable majorants).* Fix ν and a block y. The torus is finite, so there are finitely many blocks y′. Put

  a*_ν(y;x) := sup_{𝗎∈𝒰(ε₁)} max_{y′} ‖χ_y R_ν(x;𝗎) χ_{y′}‖ e^{δ₀ d(ν;y,y′)}.

By (Inv-x) each function x ↦ ‖χ_y R_ν(x;𝗎)χ_{y′}‖ is continuous on [0,∞). A supremum of continuous functions is lower semicontinuous, hence Borel measurable; so a*_ν(y;·) is measurable. By (D) and (Sh3-u), a*_ν(y;x) ≤ a_ν(y;x) and Σ_ν a_ν(y;x) ≤ B₀m₁/(m₁+2x), for every x ≥ 0.

*Step 4 (proof of (a) and (b)).* Put ã_ν(y) := (1/π)∫₀^∞ x^{−1/2} a*_ν(y;x) dx ∈ [0,∞]. The walks form a countable set and the a*_ν are non-negative and measurable. By Tonelli's theorem for a countable sum, and Steps 2–3,

  Σ_ν ã_ν(y) = (1/π)∫₀^∞ x^{−1/2} Σ_ν a*_ν(y;x) dx ≤ (1/π)∫₀^∞ x^{−1/2} B₀m₁/(m₁+2x) dx = B₀(m₁/2)^{1/2}.

In particular every ã_ν(y) is finite. For each 𝗎, each ν and each pair y, y′, ‖χ_y R_ν(x;𝗎)χ_{y′}‖ ≤ a*_ν(y;x)e^{−δ₀d(ν;y,y′)}, and the right side is integrable against x^{−1/2}. So the integral defining 𝖬_ν converges absolutely, and taking norms inside the integral gives (b). The blocks χ_y·χ_{y′} cover every entry, so the convergence is entrywise. For the series: Σ_ν ∫ x^{−1/2}‖χ_y R_ν(x)χ_{y′}‖dx ≤ π B₀(m₁/2)^{1/2} < ∞. Fubini's theorem therefore exchanges Σ_ν and ∫. For each x, Σ_ν R_ν(x) = (x+𝖠)^{−1} by (D), and the series converges absolutely by (Sh3). Hence Σ_ν 𝖬_ν = 𝖲. The column form of (b) is the same computation with the column sums of (Sh3).

*Step 5 (proof of (c)).* For each x, R_ν(x;·) is analytic on 𝒰(ε₁): it is a term of a sheet whose analyticity radius is ε₁ (clause (D)). Its entries are bounded on 𝒰(ε₁) by a*_ν(y;x) times a constant, and x^{−1/2}a*_ν(y;x) is integrable (Step 4). Restrict to any complex line {𝗎₀ + z𝗏} meeting 𝒰(ε₁). Fubini's theorem and Cauchy's theorem for each fixed x give that the integral of 𝖬_ν over every closed triangle in the line vanishes; continuity of 𝖬_ν follows from dominated convergence. By Morera's theorem 𝖬_ν is analytic on each line. A function on a finite-dimensional complex domain that is continuous and analytic on each complex line is analytic (Hartogs' theorem in its elementary form for continuous functions, via the Cauchy integral in each variable). This proves (c).

*Step 6 (proof of (d)).* Fix ν. For every x ≥ 0, (x+𝖠)^{−1} is a sheet of 𝒮_u[M/4; B₀m₁/(m₁+2x), δ₀; ε₁], so `4.14:lem-local-balls` applies to it with r = ε₁. Its cut-off χ of (4.14:eq-local-balls-1) depends only on [ν], and [ν] does not depend on x ("walks and domains independent of x"). So one point 𝗎̂ := (e^{iηχA′}U, χJ) ∈ 𝒰(ε₁) serves every x. By part (γ) of that lemma, R_ν(x;·) takes the same value at every point of 𝒰(ε₁) whose data agree with the given data on [ν]. Hence 𝖬_ν takes the same value at all such points, because it is an integral of these values; this is the independence of the extension. The map (A′,J) ↦ (χA′,χJ) is linear and sends the local ball into 𝒰(ε₁) (part (β)). So 𝖬_ν on the local ball is 𝖬_ν composed with an affine map, hence analytic by (c), and (b) holds at 𝗎̂ with the same coefficients.

*Step 7 (proof of (e)).* B₀ = 12·2^d/m₁ and m₁ = γ₀/4, δ₀ = μ₁/4 are (d,L)-numbers by Notation 4.14 and clause (I). No step above introduced another constant. ∎

**What Theorem 1 gives, and what it does not.**

- It proves the companion clause of the proposition at rate δ₀ in place of μ₀, on the local balls of clause (H), from a proved theorem. With μ̂₀ replaced by min{μ₀, δ₀} in Lemma R, (c) of that lemma now adds one floor, δ₀M ≥ 2κ₁; it reads only Stage-5 constants and is imposed at Stage 6 with the others (the pattern of `cwch.md` (M7)).
- The bound is stated in the distance d(ν;y,y′) of the unit frame. That is the distance in which clause (E) states the kernel 𝖢, which the account's proof uses for the first clause at local data (CA-II 59602–59605). So the two clauses now have the same proof at local data.
- It covers 𝗌 ≡ 𝟙. The decoupled family of (b3) with |𝗌(Δ)| ≤ e^{κ₁} needs in addition a count of the cubes a walk meets, as in hypothesis (c) of `4.4:prop-local-real-base` (CA-I 8122–8127), which is itself outstanding.
- It needs the real base U on the whole lattice, in 𝒰_ℝ. Data whose real part is given only locally are the subject of §5.
- It does not use, and does not identify, the words of the account's assigned expansion (b3). It is an own-route family with the same σ = 𝟙 sum 𝖲.

