lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T11:38Z

# CM: Claude attack on prescribed-word continuation (2.4:prop-m-freeness)

Queue row 345 (`cm-claude`). Commit a34245012. Proved by Claude, not yet checked by the other model. Research-stage working state; no status.

Credit: the statement, its words and its constants are Ethan Sussman and Levent Alpoge's complete account (with Claude and Codex as authors of their text), commit 31a47c543775. The background estimates go back to Balaban (CMP 95-122). The three earlier rounds are Codex's (`library/mf.md`).

Sources: CA-I/II/III = `theorem_0_complete_account_raw_{I,II,III}.tex` at 31a47c543775, fetched once into `/tmp/cmclaude-src/`. SHA-256 of I, II and the outline match those in `open-core.md` §2; III is `7e36523b…a352d`. Numbers are raw TeX lines. Read before writing: `mf.md` (three rounds, nine attacks, whole), `cwch.md` §4 (Codex's CM consumer check), `l17c.md` §§1, 6, 7 and Result, `open-core.md` §§1–4 and 6.2, `port-map.md` rows 6 and 105.

Kind of result: proof of the step they mark incomplete (CA-II 59607–59609), as an implication from an input they admit, with a rate correction that changes no condition; plus own-route proofs from their proved lemmas on the two local classes the account itself uses. What stays open is listed in §6; none of it is CM as a separate statement.

## 1. Verdict in brief

1. **Consumer check first**, as the row asks (§2). Every reader of the proposition and of the letter μ₀ is listed with what it reads.
2. **The marked step is an implication from an input the account admits** (§2). Clause (II) of the random-walk input (b3), CA-II 2181–2264, covers the member C_{Λ*}^{1/2}. It bounds that companion at local data, on Balaban's analyticity space over every union Z ⊇ Z₀′ of cubes, for |𝗌(Δ)| ≤ e^{κ₁} and every M above its floors, by B_W e^{−δ_W ρ}. The rate is δ_W, not μ₀. Codex's consumer table (`cwch.md` §4.1) does not use this clause.
3. **The rate change costs nothing** (Lemma R, §3). With μ̂₀ := min{μ₀, δ_W}, no floor on M, no rim constant and no width changes; μ₀ is read elsewhere only at true pairs.
4. **Own route on local balls** (Theorem 1, §4). From the proved operator theorem at free current: term-by-term integration of its resolvent sheets gives the companion family at local complex data about a global real base, rate δ₀, amplitude B₀(m₁/2)^{1/2}, both (d,L)-numbers.
5. **Own route on the account's own local class** (Theorem 2, §5). The §4.4 cell family 𝖬^{Y,W′} and its decoupled form obey M-free bounds at rate λ = ν/4 (Codex's `mf.md` Lemma 1, checked here, first failing step none) in **every** admissible geometry for W′ ⊂ Ω_{k+1}. Two new pieces: cell coercivity transfers from 𝒮₀ by the account's locality rule (Theorem 2(a)), and the walk-counting bound that `4.4:prop-local-real-base` assumes is proved (Lemma W).
6. **Open** (§6): nothing that is CM as a separate statement. The cited leaf `5.2:lem-random-walk-bounds` (if the chain keeps Balaban's family), one class of data that no displayed consumer reads, the undisplayed class of Balaban's old-terms sentence, and Codex's check of this note.

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
| 7 | Old terms beside a new region, CA-II 59540–59568 | "The same step also uses the independence from M of the kernel constants and of the decay rate of the random walk. This is not a printed sentence; it is Proposition 5.10:prop-m-freeness" (59566–59568). The step itself is Balaban's sentence, cited as printed; the account takes its containment by statement (II 4168–4177, hypothesis (a); II 4321–4324, Case 3). Its demand on the companion is not displayed. | Yes, as far as anything is displayed. The M-free random-walk constants at Balaban's analyticity spaces are stated by (b3) at (B_W, δ_W). Any later proof of Balaban's sentence must name its class; see §6, O3. |
| 8 | Assembly, CA-III 110846–110866, 111066–111079; open list 111410–111412 | Order-consistency and the proposition, by name. | Yes. |
| 9 | Random-walk input (b3), CA-II 2181–2264 (supplier, not consumer) | For 𝓜 ∈ {𝒜, C_{Λ*}, C_{Λ*}^{1/2}, C_I}: "For every union Z ⊇ Z₀′ of cubes, the operator 𝓜(𝗌;𝐔,𝐉) is holomorphic on {|𝗌(Δ)| ≤ e^{κ₁}} times Balaban's analyticity space over Z, under δ₁M ≥ κ₁"; "the kernel depends on (𝐔,𝐉) restricted to Z only"; (II) \|𝓜(𝗌)(b,b′)\| ≤ B_W e^{−δ_W ρ(b,b′)}, B_W := Be^{16κ₁}, "with B, δ_W numbers depending on (d,L)" (2207–2211). Same statement: `5.2:lem-random-walk-bounds`, CA-II 8922–8940, status CITED (CMP 99b Theorem 3.15). | It is the supplier of (∗′). |

**The corrected clause.** Put μ̂₀ := min{μ₀, δ_W}.

> (∗′) For every Z ⊇ Z₀′ as in (b3), every (𝐔,𝐉) in Balaban's analyticity space over Z, every 𝗌 with |𝗌(Δ)| ≤ e^{κ₁}, and every M above its floors: |C_{Λ*}^{1/2}(𝗌;𝐔,𝐉)(b,b′)| ≤ B_W e^{−μ̂₀ρ(b,b′)}.

**Proof that (b3) implies (∗′).** By (b3)(II) for 𝓜 = C_{Λ*}^{1/2}, the left side is at most B_W e^{−δ_Wρ(b,b′)}. Since ρ ≥ 0 and δ_W ≥ μ̂₀, e^{−δ_Wρ} ≤ e^{−μ̂₀ρ}. B_W = Be^{16κ₁} and δ_W read only (d,L) and κ₁, so the constants are M-free and are fixed before Θ₁, ϖ_T, r′, ℓ and M (Stage 5 lets the kernel constants read d, L, M₁, M₁^♯ and κ₁: CA-I 2064–2066). The holomorphy, the locality in Z and the range of 𝗌 are those of (b3). ∎

*Remark (if (II) is read at the scaffold point only).* Display (II) writes 𝓜(𝗌) without (𝐔,𝐉). Clause (I) and the "at all pairs" form of (III) (CA-II 2264–2271) still give the bound on the whole space: |𝓜(𝗌;𝐔,𝐉)(b,b′)| ≤ |𝓜₀(b,b′)| + |[𝓜(𝗌;𝐔,𝐉)−𝓜₀](b,b′)| ≤ [B + B_W(1+α₀+α₁)]e^{−δ_Wρ(b,b′)} ≤ 3B_W e^{−δ_Wρ(b,b′)}, using e^{−δ_W[𝖽−M/2]₊} ≤ 1, α₀+α₁ ≤ 1 and B ≤ B_W = Be^{16κ₁}. The amplitude 3B_W is still M-free.

**Verdict of the check.** Every consumer in the table accepts (∗′). (∗′) is an implication from (b3), an input the account already admits and uses in its correlation theorem (II 12927–12928 lists it among the hypotheses). So, at the account's own citation standard, the step marked (∗) is not an independent gap: it is clause (II) of (b3) for one of its four members, read at a rate the floors already cover. For our chain, which must rebuild cited inputs, CM merges into the leaf `5.2:lem-random-walk-bounds`. The prescribed-word display of `open-core.md` (CM) is stronger than any consumer reads; `cwch.md` §4.1 already found that no consumer uses the binomial weights and that the consumers accept an aggregate bound.

**Why this was missed.** `mf.md` §1 identifies the companion with the root lemma, notes that its last paragraph "sends the decoupled family back to the assigned random-walk expansion", and then asks for that family at the fixed rate μ₀. (b3) is that assigned expansion, and it states the bound at δ_W. Round 2 of `mf.md` read `5.2:lem-random-walk-bounds` (CA-II 8922–8999; `mf.md` §6), whose clause (a) states the bound for C_Λ^{1/2}, but did not use it, because it required the fixed rate μ₀. The fixed-rate demand is the whole difference, and Lemma R shows no consumer needs it.

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

So the corrected proposition has the same order of choice, letter for letter.

**If the rate comes from §4 or §5 instead of (b3).** Use two letters. Keep μ₀, the Combes–Thomas rate, wherever the account reads it at true pairs (root lemma, K₀, and δ₁ = min{μ₀/2, δ_W/2}); these do not read the local companion. Put μ̂₀ := min{μ₀, r}, where r is the rate proved there (δ₀ in Theorem 1, λ/2 in Theorem 2), in the companion clause only. Then (c) turns the first Stage-6 floor into μ₀M ≥ 2κ₁ together with rM ≥ 2κ₁. The second is a new floor on M; it reads only Stage-5 constants and is imposed at Stage 6 with the others (`cwch.md` (M7)). Part (b) is not needed in this case, because δ₁ keeps μ₀. This is the l17c pattern in its simplest form: the weaker statement is proved (by (b3), §2), and every consumer reads it.

## 4. Theorem 1: the companion from the operator theorem, on local balls

§2 closes (∗) at the account's citation standard. Our chain must rebuild cited inputs, so this section proves the companion clause from a statement the account proves, `4.14:thm-operator-theorem` (CA-I 46035–46129, status PROVED; our port `port/p4-operator.md`, A9). The class is the local balls of its clause (H): complex data given only near the walk, about a real base given on the whole lattice.

**Inputs used, all from CA-I.** Notation 4.14 (45237–45330): m₁ = γ₀/4, δ₀ = μ₁/4, B₀ = 12·2^d/m₁, ε₁ = γ₀/(8γ₁), all (d,L)-numbers. Clause (B): Re 𝖰 ≥ m₁ on 𝒰(ε₁). Clause (D) with its proof (47864–47884): for every 𝔹 ⊂ 𝔹⁺ and every x ≥ 0, (x+𝖠)^{−1} ∈ 𝒮_u[M/4; B₀m₁/(m₁+2x), δ₀; ε₁], "with walks and domains independent of x". Clause (G) (48012–48017): "Each walk of n steps in the expansion of (x+𝖠)^{−1} carries the factor (1+2x/m₁)^{−(n+1)}", and the unit words are products of factors (48021–48022). Clause (I): the constants depend on d and L only. The decay property (Sh3) of a sheet, in the form displayed at 46616–46632: for each walk ν and blocks y, y′ of the unit frame, ‖χ_y T_ν χ_{y′}‖ ≤ a_ν(y) e^{−δ d(ν;y,y′)}, with Σ_ν a_ν(y) ≤ B (the frame has one level, so the scale factor is 1; 47889–47890). Lemma `4.14:lem-local-balls` (46800–46950, PROVED).

Two readings of the sheet calculus are used and are named here, because the account states that calculus only by name (our port keeps it as the named input P4-H-sheet):

- **(Inv-x)** Each term R_ν(x) of (x+𝖠)^{−1} is continuous in x ∈ [0,∞). Reason given in the account: the terms are products of factors (48021–48022), the x-dependent factors are one-box resolvents, and an accretive matrix B with Re B ≥ m₁ has (x+B)^{−1} analytic in x on Re x > −m₁ (Step 1 below).
- **(Sh3-u)** For the unit-frame sheets, (Sh3) has the form displayed at 46616–46632 for the operator-construction format, and its coefficients a_ν(y;x) hold at every point of the analytic ball 𝒰(ε₁), not only pointwise. The display at 46629 builds the coefficients from the norm bound, not from the datum; hypothesis (W′), item 5 (CA-I 5547–5552), has the same form.

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

*Step 5 (proof of (c)).* Fix U ∈ 𝒰_ℝ. The fibre {(A′,J): ‖(A′,J)‖_⋆ < ε₁} is an open set of a finite-dimensional complex vector space, and analyticity is meant in (A′,J). For each x, R_ν(x;·) is analytic there: it is a term of a sheet whose analyticity radius is ε₁ (clause (D)). Its entries are bounded by a*_ν(y;x), and x^{−1/2}a*_ν(y;x) is integrable (Step 4). Restrict to any complex line in the fibre. Fubini's theorem and Cauchy's theorem for each fixed x give that the integral of 𝖬_ν over every closed triangle in the line vanishes; continuity of 𝖬_ν follows from dominated convergence. By Morera's theorem 𝖬_ν is analytic on each line. A continuous function on an open set of ℂⁿ that is analytic in each variable separately is analytic (Osgood's lemma: write it as the iterated Cauchy integral over a polydisc). This proves (c).

*Step 6 (proof of (d)).* Fix ν. For every x ≥ 0, (x+𝖠)^{−1} is a sheet of 𝒮_u[M/4; B₀m₁/(m₁+2x), δ₀; ε₁], so `4.14:lem-local-balls` applies to it with r = ε₁. Its cut-off χ of (4.14:eq-local-balls-1) depends only on [ν], and [ν] does not depend on x ("walks and domains independent of x"). So one point 𝗎̂ := (e^{iηχA′}U, χJ) ∈ 𝒰(ε₁) serves every x. By part (γ) of that lemma, R_ν(x;·) takes the same value at every point of 𝒰(ε₁) whose data agree with the given data on [ν]. Hence 𝖬_ν takes the same value at all such points, because it is an integral of these values; this is the independence of the extension. The map (A′,J) ↦ (χA′,χJ) is linear and sends the local ball into 𝒰(ε₁) (part (β)). So 𝖬_ν on the local ball is 𝖬_ν composed with an affine map, hence analytic by (c), and (b) holds at 𝗎̂ with the same coefficients.

*Step 7 (proof of (e)).* B₀ = 12·2^d/m₁ and m₁ = γ₀/4, δ₀ = μ₁/4 are (d,L)-numbers by Notation 4.14 and clause (I). No step above introduced another constant. ∎

**What Theorem 1 gives, and what it does not.**

- It proves the companion clause of the proposition at rate δ₀ in place of μ₀, on the local balls of clause (H), from a proved theorem. With μ̂₀ replaced by min{μ₀, δ₀} in Lemma R, (c) of that lemma now adds one floor, δ₀M ≥ 2κ₁; it reads only Stage-5 constants and is imposed at Stage 6 with the others (the pattern of `cwch.md` (M7)).
- The bound is stated in the distance d(ν;y,y′) of the unit frame. That is the distance in which clause (E) states the kernel 𝖢, which the account's proof uses for the first clause at local data (CA-II 59602–59605). So the two clauses now have the same proof at local data.
- It covers 𝗌 ≡ 𝟙. A decoupled form with |𝗌(Δ)| ≤ e^{κ₁} needs in addition a count of the cubes a walk meets. Lemma W (§5.2) gives that count for walks measured by tree length, as in `4.4:def-walk-systems`; the sheet walks here are measured by d(ν;y,y′), and the count in that distance is not done.
- It needs the real base U on the whole lattice, in 𝒰_ℝ. Data whose real part is given only locally are treated in §5 for W′ ⊂ Ω_{k+1}; the rest is O2 in §6.
- It does not use, and does not identify, the words of the account's assigned expansion (b3). It is an own-route family with the same σ = 𝟙 sum 𝖲.

## 5. Theorem 2: the account's own local companion family, in every admissible geometry

This section treats the reading in which "the cells of the one family" are the cells 𝒬 of side ℓ of `4.4:def-auxiliary-parameters` (CA-I 6095–6150; "The numbers defined below are the same in every setting in which they are used"), and "the decomposition of the density" is the setting of CMP 116 (2.14) used by `4.4:prop-local-real-base` (CA-I 8110–8169). There the account's companion at local data is the family 𝖬^Y of `4.4:lem-cell-resolvent`(v), decoupled by the interpolation rule.

### 5.1 Check of `mf.md` Lemma 1 (Codex)

Checked line by line by Claude, first failing step none. Points verified against the source:

- (6): |F(b,b′)| ≤ ν|b−b′|e^{ν|b−b′|}|T_X(b,b′)| uses |e^s−1| ≤ |s|e^{|s|} and that f is 1-Lipschitz. Then ν t e^{νt} = νt e^{−(δ−ν)t}·e^{δt} ≤ ν[e(δ−ν)]^{−1}e^{δt}, so the Schur sums give ‖F‖ ≤ ν𝖡/[e(δ−ν)] ≤ 2ν𝖡/(eδ) ≤ γ/8, by ν ≤ δ/2 and ν ≤ eγδ/(16𝖡).
- (7): D(x+T_X)D^{−1} = x+T_X+F, Re(x+T_X+F) ≥ x+3γ/4, and an entry is at most the operator norm; with b₀ = b′ this gives (x+a)^{−1}e^{−ν|b−b′|}, a = γ/2.
- (9): the single-cell weight. The book's argument (CA-I 6466–6470) is that rows and columns of P_q, B_q lie in q^♯, so d(q;b,b′) ≤ |b−b′|: the segment path from b₋ to b′₋ meets the single domain q^♯. Then the row sum is at most (x+a)^{−1}Σ_{b′}[Σ_qκ_q(b′)]e^{−(3ν/4)|b−b′|} ≤ S_ν/(x+a), and the column sum the same.
- (10)–(11): |b″−b′| ≥ ℓ−2−r ≥ ℓ/2 (CA-I 6487–6499 and (k2)); λ = ν/4 gives e^{λ|b−b′|}e^{−ν|b″−b′|} ≤ e^{λ|b−b″|}e^{−(ν/2)|b″−b′|}e^{−νℓ/8}; λ ≤ δ_𝖠 so the 𝖠-row sum at rate λ is at most 𝖡; with (x+a)^{−1} ≤ 2/γ and floor (4) this is ≤ 1/2.
- Far steps: d(ω;b,b′) ≥ d(ω) > r′ (lemma (c) after `4.4:def-walk-systems`, CA-I 4922–4925) gives |||E|||_{δ/2} ≤ 𝖡e^{−δr′/2}; the rate is monotone, so |||E|||_λ ≤ ε.
- (12)–(13): submultiplicativity of |||·|||_λ for families (lemma (a) there), |||N|||_λ ≤ 2S_ν/(x+a) ≤ 4S_ν/γ, |||EN|||_λ ≤ 1/2 by floor (4), sum ≤ 4S_ν/(x+a); integration by Step 2 of §4.
- Order: ν, λ, S_ν, a read only 𝖡, δ_𝖠, γ_*; floor (4) is a lower bound on r′, then on ℓ. None reads M.

### 5.2 Lemma W (walk counting)

This proves hypothesis (c) of `4.4:prop-local-real-base` (CA-I 8122–8127), which the account assumes there.

**Lemma W.** Let ϖ be a walk in the sense of `4.4:def-walk-systems` (CA-I 4875–4900) whose step domains have sup-diameter at most LM/4. Let b, b′ be bonds and t := d(ϖ;b,b′). Let σ₀ be the cubes of side LM of a standard partition, and let m(ϖ) be the number of Δ ∈ σ₀ that meet |ϖ| in the sense of `4.4:def-interpolation-rule` (int Δ ∩ |ϖ| ≠ ∅; CA-I 5131–5133). Then m(ϖ) ≤ 3^d (2t/(LM) + 1). For d = 4 this is the account's bound 81(2t/(LM) + 1).

**Proof.** Let η > 0 and let 𝒯 be a tree (a finite connected acyclic union of segments) that contains b₋, b′₋, meets every domain of ϖ, and has ℓ¹-length t_η ≤ t + η; by the definition of d(ϖ;b,b′) as the length of a shortest such tree, one exists. Doubling every segment of 𝒯 gives a connected multigraph in which every vertex has even degree, hence a closed path that runs through every point of 𝒯 and has length 2t_η. Parametrise it by arc length s ∈ [0, 2t_η], and mark the points p_j at s_j = jLM, j = 0, …, J, J := ⌊2t_η/(LM)⌋. There are J+1 ≤ 2t_η/(LM)+1 marked points. Every s lies within arc length LM/2 of some s_j or of 2t_η, and the path returns to p₀ at s = 2t_η. Arc length bounds ℓ¹-distance, which bounds sup-distance. So every point of 𝒯 is within sup-distance LM/2 of some p_j. Each domain of ϖ meets 𝒯 and has sup-diameter at most LM/4, so |ϖ| ⊂ ∪_j Q_j, where Q_j is the closed sup-ball of radius 3LM/4 about p_j, a cube of side 3LM/2.

Count the cubes Δ ∈ σ₀ with int Δ ∩ Q_j ≠ ∅. Both are products of intervals. In one coordinate, an open cell (na,(n+1)a) of length a = LM meets a closed interval [x, x+3a/2] if and only if n lies in the open interval (x/a−1, x/a+3/2), of length 5/2; it contains at most 3 integers. So at most 3^d cubes per j, and m(ϖ) ≤ 3^d(2t_η/(LM)+1). Let η → 0; m(ϖ) is an integer and does not depend on η. ∎

**Check of the domain hypothesis for the cell walks.** The steps of the walks of `4.4:lem-cell-resolvent`(i) have domains q^♯ (side at most 4ℓ ≤ M/12) or domains of far walks of 𝖠 (ℓ¹-diameter at most ρ_w by (W′) item 2, and ρ_w ≤ r ≤ ℓ by (k2)). By (k3), ℓ ≤ M/48. So all step domains have sup-diameter at most M/12 ≤ LM/4.

### 5.3 Theorem 2

**Setting.** Level k; an admissible geometry 𝔤 = (𝛀, Y) of §4.4, with any nest; a closed union W′ of M₁-cubes with W′ ⊂ Ω_{k+1}; a local datum 𝗎 ∈ 𝐏_{ρ,W′}. The form 𝖠 = Σ_ω 𝖠_ω satisfies (W′) with 𝖡, δ_𝖠, ρ_w, γ_* (CA-I 5517–5578, 6095–6100). Put ν, λ = ν/4, a = γ_*/2, S_ν as in `mf.md` (3).

**Theorem 2.** Assume the hypotheses of `4.4:lem-cell-coercivity` (CA-I 6646–6660: (W′) with its local half; the positivity statement for the base setting 𝒮₀; (k1); the halved ceilings on the primed radii), the auxiliary parameters chosen under `mf.md` (4) and the book's (k2′), and M ≥ 48ℓ. Then, for every admissible geometry, every W′ ⊂ Ω_{k+1} and every 𝗎 ∈ 𝐏_{ρ,W′}:

- (a) **Cell coercivity at every cell with q^♯ ⊂ W′.** For X ⊂ c*_q, Re⟨v, T_X(𝗎)v⟩ ≥ (7/8)γ_*|v|² for all v ∈ ℓ²(X; 𝔤^c).
- (b) **Local families.** The families 𝖱^{Y,W′}(x), x ≥ 0, and 𝖬^{Y,W′} of `4.4:lem-cell-resolvent`(v), built from 𝗎 alone, are defined and analytic in 𝗎, and |||𝖱^{Y,W′}(x)|||_λ ≤ 4S_ν/(x+a), |||𝖬^{Y,W′}|||_λ ≤ 4S_ν/√a.
- (c) **Decoupled families.** Let σ(Δ) ∈ ℂ, |σ(Δ)| ≤ e^{κ₁}, for Δ ∈ σ₀ (side LM), and K(σ) := (K_ϖ(𝗎)∏_{Δ meets |ϖ|}σ(Δ))_ϖ for K ∈ {𝖱^{Y,W′}(x), 𝖬^{Y,W′}}. If λLM ≥ 324κ₁, then |||K(σ)|||_{λ/2} ≤ e^{81κ₁}|||K|||_λ. In particular |Σ_ϖ 𝖬_ϖ(σ;𝗎)(b,b′)| ≤ e^{81κ₁}(4S_ν/√a)e^{−(λ/2)|b−b′|}, and each sum is holomorphic in σ on the open polydisc.
- (d) **Order.** λ, a, S_ν read only 𝖡, δ_𝖠, γ_*, which depend on d, L and G only and are fixed before M (CA-I 6097–6100); the amplitude e^{81κ₁}4S_ν/√a reads κ₁ in addition. All are fixed at Stage 5, before Θ₁, ϖ_T, r′, ℓ and M. The new conditions λLM ≥ 324κ₁ and (for Lemma R) λM ≥ 4κ₁ are floors on M.

**Proof.**

(a) The rule of 𝖠 is local in the sense of `4.4:def-local-rules` ((W′) item 6, CA-I 5554–5556), and it does not read Y: rule (R1′) takes "the family of walks of the walk-expansion theorem for the quadratic form" (CA-I 8887–8890), and Y enters `4.4:lem-cell-resolvent` only through χ_Y and c*_q. Let 𝔤₀ be the trivial nest with the same Y. Then W′ ⊂ Ω_{k+1} ∩ T and Y ∩ W′ = Y ∩ W′, so W′ is uniform for (𝔤, 𝔤₀) (CA-I 5008–5016). By conditions (i) and (ii) of local rules (CA-I 5030–5037), the walks ω with |ω| ⊂ W′ are the same for 𝔤 and 𝔤₀, and their terms are the same functions on 𝐏′_{|ω|}. The walks entering T_X have d(ω) ≤ r′ and a row in X ⊂ q*, hence [ω] ⊂ (q*)^{+r} ⊂ q^♯ ⊂ W′ (Step (1) of the proof of `4.4:lem-cell-coercivity`, CA-I 6676–6684). So T_X[𝔤](𝗎) = T_X[𝔤₀](𝗎|_{q^♯}). The restriction is a local datum on q^♯ (`4.4:def-local-data-classes`(b), CA-I 4486–4487). `4.4:lem-cell-coercivity`, proved at 𝒮₀, gives the bound.

(b) Every primitive of the families — the cell matrices T_q and their inverses, the near blocks in B_q, the far steps — is built from terms 𝖠_ω with |ω| ⊂ W′. By (a) and locality they are the base-setting primitives evaluated at 𝗎. `mf.md` Lemma 1 (checked in 5.1) uses only: the datum-free majorants of (W′) on those primitives, the cell coercivity of (a) at every cell with q^♯ ⊂ W′, Σ_qκ_q ≤ 1 over those cells, and the geometry of cells. Its proof therefore applies verbatim and gives the two bounds. Analyticity: each term is analytic in 𝗎 (`4.4:lem-cell-resolvent`(v)) and the families converge normally on 𝐏_{ρ,W′}.

(c) Fix b. For a walk ϖ and a bond b′, |K_ϖ(σ)(b,b′)| ≤ |K_ϖ(b,b′)|e^{κ₁m(ϖ)}. Lemma W (its domain hypothesis is checked in 5.2) gives m(ϖ) ≤ 81(2d(ϖ;b,b′)/(LM)+1). The floor λLM ≥ 324κ₁ gives 162κ₁/(LM) ≤ λ/2. Hence e^{κ₁m(ϖ)} ≤ e^{81κ₁}e^{(λ/2)d(ϖ;b,b′)}. Multiply by e^{(λ/2)d(ϖ;b,b′)} and sum over (ϖ, b′):

  Σ_{ϖ,b′} |K_ϖ(σ)(b,b′)|e^{(λ/2)d(ϖ;b,b′)} ≤ e^{81κ₁} Σ_{ϖ,b′} |K_ϖ(b,b′)|e^{λd(ϖ;b,b′)} ≤ e^{81κ₁}|||K|||_λ.

Columns are the same. For the entry bound, keep only the terms with the given b′ and use d(ϖ;b,b′) ≥ |b−b′|. Each term is a polynomial in the finitely many σ(Δ) (finite torus), and the majorant is uniform on the polydisc, so the sum is holomorphic on its interior.

(d) Read off from `mf.md` (3) and CA-I 6097–6100. ∎

**Consequence for the proposition.** In this reading, the companion at local data is 𝖬^{Y,W′} and its decoupled form, at every admissible geometry for W′ ⊂ Ω_{k+1}. Theorem 2 bounds it with M-free constants placed at Stage 5. Lemma R with μ̂₀ := min{μ₀, λ/2} then closes (∗): the first Stage-6 floor becomes μ₀M ≥ 2κ₁ and λM ≥ 4κ₁, a floor on M reading Stage-5 constants. `cwch.md` §4.1 rejected (M2) as covering "every actual local density datum" because cell coercivity is proved at 𝒮₀ (CA-I 6681–6687); part (a) removes that objection for every W′ ⊂ Ω_{k+1}, which is the region the account itself uses for general geometries ("In the setting 𝒮₀ any Z is admitted", CA-I 8137).

## 6. Where each reading stands, and what stays open

The account never defines "the companion kernel" at local data; it names the object only in the proposition. Each reading found in the account is covered:

| Reading of "companion at local data" | Covered by | Standing |
|---|---|---|
| Chapter 5's assigned family C_{Λ*}^{1/2}(𝗌;𝐔,𝐉), on Balaban's analyticity space over Z ⊇ Z₀′, \|𝗌(Δ)\| ≤ e^{κ₁} | §2, clause (II) of (b3) | Implication from their admitted input, cited Balaban. In our chain: the leaf `5.2:lem-random-walk-bounds` (CITED). |
| The termwise integral of the resolvent sheets of the operator theorem, at local complex data about a global real base | Theorem 1 (§4) | Proved from `4.14:thm-operator-theorem` (PROVED) and `4.14:lem-local-balls` (PROVED), with the two readings (Inv-x), (Sh3-u) of the named sheet calculus. |
| §4.4's cell family 𝖬^{Y,W′} and its decoupled form, W′ ⊂ Ω_{k+1}, any admissible geometry | Theorem 2 (§5) | Proved from `4.4:lem-cell-resolvent` and `4.4:lem-cell-coercivity` (both PROVED) with their hypotheses ((W′), the 𝒮₀ positivity statement, (k1), (k2), (k2′), ceilings), `mf.md` Lemma 1 (checked in 5.1) and Lemma W. |

In each row the corrected clause (∗′), with μ̂₀ := min{μ₀, r} for the rate r of that row, holds with constants fixed at Stage 5, for every M above its floors. By §2 and Lemma R, every consumer accepts it.

**What stays open.** None of these is CM as a separate statement.

- **O1.** If our chain keeps Balaban's own family in Chapter 5, the cited leaf `5.2:lem-random-walk-bounds` (CMP 99b Theorem 3.15; CMP 116 (1.7)–(1.11)) must be rebuilt. The chain needs it there anyway, for more than M-freeness: clauses (I) and (III), the reference operator 𝓜₀ and the family C_I(𝗌).
- **O2.** No result here covers data whose real part is given only locally at cells whose hull is not inside Ω_{k+1} (non-trivial traces), outside the local balls of clause (H). No displayed consumer reads the companion there. Chapter 5 puts the covariance domains Λ*, Λ*∩Z₀ inside Ω^{∼−1}_{k+1} (CA-II 8956), and §4.4 restricts Z to Ω_{k+1} in a general geometry (CA-I 8137).
- **O3.** Balaban's sentence on old terms beside a new region (`5.10:rem-old-terms-beside`, printed without proof) does not say which class of local data it reads. When that leaf is rebuilt, its proof must name the class. If the class is one of the three rows, (∗′) supplies it. If it is the class of O2, O2 becomes a precise open lemma there.
- **O4.** Theorem 1 uses the readings (Inv-x) and (Sh3-u) of the sheet calculus, which the account states by name only (our port: P4-H-sheet). Theorem 2 does not use them.
- **O5.** This note is proved by Claude and not yet checked by Codex.

**For the lead (no other file is edited here).** In `open-core.md` §4, C_M can be replaced by (∗′) with the rate convention of Lemma R. The prescribed-word display (CM) is a sufficient condition that no consumer reads. In `port-map.md` row 105, the state could read: implication from `5.2:lem-random-walk-bounds` at their standard; own route by Theorems 1–2 of `library/cm-claude.md`.

**Possible value to Sussman and Alpoge** (for the lead only; nothing is posted, and FINISH item 6 requires the five checks first): (i) their step (∗), CA-II 59607–59609, follows from their own admitted input (b3) under a rate convention that changes no condition of their order (Lemma R); (ii) Lemma W proves hypothesis (c) of their `4.4:prop-local-real-base`, which they assume; (iii) Theorem 2(a) extends their `4.4:lem-cell-coercivity` from 𝒮₀ to every admissible geometry for cells inside Ω_{k+1}, by their own locality rule. Item (i) is a proof of a step they mark incomplete; it uses only their text.

## Result

**Proof**

Kind: proof of the step they mark incomplete (CA-II 59607–59609), as an implication from an input they admit, under a rate convention that changes no condition; plus own-route proofs from their proved lemmas on the two local classes the account itself uses. Proved by Claude, not yet checked by Codex.

1. **Consumer check (§2).** Every consumer of `2.4:prop-m-freeness` / `5.10:prop-m-freeness` and every reader of μ₀ accepts the corrected clause (∗′): the companion at local data obeys an exponential bound with M-free constants fixed at Stage 5, at the rate μ̂₀ := min{μ₀, r}. Local-data uses read only the random-walk input (b3) and the first clause; μ₀ itself is read only at true pairs and in floors.
2. **(b3) ⇒ (∗′)** (§2), with r = δ_W and amplitude B_W (3B_W if (II) is read at the scaffold point only). **Lemma R** (§3): this μ̂₀ changes no floor on M, no rim constant (δ₁, K₀, Θ₁, ϖ) and no width. So, at the account's citation standard, (∗) is not an independent gap: CM merges into the cited leaf `5.2:lem-random-walk-bounds`.
3. **Theorem 1** (§4): from `4.14:thm-operator-theorem` and `4.14:lem-local-balls` (both PROVED), the companion family 𝖬_ν = (1/π)∫x^{−1/2}R_ν(x)dx exists, is analytic and obeys (Sh3) with Σ_ν ã_ν(y) ≤ B₀(m₁/2)^{1/2} at rate δ₀, on the local balls of clause (H). Two named readings of the sheet calculus are used, (Inv-x) and (Sh3-u).
4. **Theorem 2** (§5): in every admissible geometry and for every W′ ⊂ Ω_{k+1}, the §4.4 cell families obey |||𝖬^{Y,W′}|||_λ ≤ 4S_ν/√a, and their decoupled forms with |σ(Δ)| ≤ e^{κ₁} obey |||·|||_{λ/2} ≤ e^{81κ₁}·4S_ν/√a under λLM ≥ 324κ₁. New: cell coercivity transfers from 𝒮₀ by the locality rule (Theorem 2(a)); Lemma W proves the walk-counting hypothesis (c) of `4.4:prop-local-real-base`, with the account's constant 81.
5. **Check.** `mf.md` Lemma 1 (Codex): checked line by line by Claude, first failing step none.

**What stays open** (§6), none of it CM as a separate statement: O1, the cited leaf `5.2:lem-random-walk-bounds`, if our chain keeps Balaban's own family in Chapter 5; O2, data with a merely local real part at cells not inside Ω_{k+1} and outside the local balls, which no displayed consumer reads; O3, the class read by Balaban's old-terms sentence (`5.10:rem-old-terms-beside`, printed without proof), to be named when that leaf is rebuilt; O4, the readings (Inv-x), (Sh3-u) for Theorem 1; O5, Codex's check of this note. The prescribed-word display CM of `open-core.md` §4 is a sufficient condition that no consumer reads; (∗′) can replace it.
