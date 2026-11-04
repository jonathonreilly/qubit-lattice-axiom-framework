lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T00:15Z

# Check of `library/b4-induction.md` (row 222)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Branch `claude/ym4d-hard-route` pinned at `497241b0d`; the note was written at `99bf6836b`. Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL into a private scratch folder (32992 lines), cited as SA nnnn. One reading by the other model. Not an audit; it grants no status. No subagent. No numeric job: none was needed, and every step below is a written argument.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the step construction, Proposition 1a.2.8 (SA 7569–7590), the window estimates WF8–WF10 (SA 16040–16092), Obligation B4 and its product box (SA 4006–4037, 4919–4921) and the constant scheme (SA 14526–14583, 19475–19477). OpenAI Codex for the note under check and for `dom.md`, `id-step.md`, `c4-order.md`, `um-envelope.md`, `c1-repr.md`. Claude for `ti-2.md`, `b2-extract.md`, `bx-fix.md`, `gamma-bx.md`, `um1-fix.md`.

Kind of result (FINISH item 9): a check of our own text. Read in full: the note; `ti-2.md` §3; `dom.md`; `id-step.md`; `b2-extract.md` §§2–7; `c4-order.md`; `um-envelope.md`; `b4-step.md` §§10–11; `c1-repr.md` §8; `bx-fix.md` §§7–9; `gamma-bx.md` §§3.4–4; the cited SA lines.

## 1. Verdicts

Checked line by line by Claude. **First failing step: line 217, "Thus H_{<k} extends to H_{≤k}", for the defect and remainder budget** (defect D1). Everything before it passes at one level k.

| Statement of the note | Verdict |
|---|---|
| §1 indices: level k has output E^(k) and fluctuation scale k−1, so old origins are i<k; TI split into TI^f and TI^E | ADVANCE |
| §2 constant order | ADVANCE, conditional on um-envelope (6)–(7) as supplied by inv-root (17)–(20) and carrier-adopt §6. Two ceilings must be added (D3); no cycle |
| §3 inputs and H_{<k} | CORRECT-NO-ADVANCE: the scope of BX⁺, UR, YA, LOC is stated correctly. But the list budget in 𝒫 contains outputs of the induction (D1) |
| §4 Step 1: (DOM)_k, ER7 ⇒ ER8u, the source map [ID] | ADVANCE |
| §4 Step 2: TI^f_k from (ID)_{i<k} | ADVANCE |
| §4 Step 3: (19)_{k−1} from (20)_{i<k} and Proposition W | ADVANCE for the regular part. The site-frozen sentence (lines 148–149) is right for the input side only (D2) |
| §4 Step 4: gas convergence, (3), the Lipschitz bound, the member bound E_0 | ADVANCE, except the defect filing at lines 190–192, which does not close across levels (D1) |
| §4 Step 5: (ID)_k | ADVANCE |
| §4 Step 6: TI^E_k, the re-pointed member, (R14)_k, (20)_k | ADVANCE |
| §5 circularity check | The displayed chain has no same-level cycle: confirmed. One loop is missed: the list budget (D1) |
| Result box | ADVANCE as an implication at one level k from H_{<k}. "H_{<k} extends to H_{≤k}" and "uniformly in its length" are not proved for the defect sector (D1), nor for nonconstant source arrays (D2) |

## 2. The order at level k: what was redone

Each item names the step of the note and the source line that supplies it.

- **Indices (§1).** `b4-step.md` (19) is stated at fluctuation index k with origins j ≤ k and weight ω_{k+1−j}. Replacing k by k−1 gives origins i<k and ω_{k−i}, with σ = L^{−(k−1−i)}. This is (1) of the note. Proposition W's ω_n = C(1+n)^{3/2}L^{−α_H(n−1)} matches, through ρ_i² ≤ C(1+k−i) (WF1) and ρ³σ² ≤ ρ³σ^{α_H}.
- **Step 1.** `dom.md` (5) with dom's k = our k−1 gives F_{k−1}(U_{k−1}(V)) ≤ cL^{−2}e_k + C_Fδ_{k−1}. I redid the bound below ce_{k−1}/2: e_k/e_{k−1} ≤ 2 (dom says 4), 4c/L² < c/4 for L ≥ 27, and C_Fδ_{k−1} ≤ C_F(A_1/A_0)·2e_{k−1} ≤ ce_{k−1}/4. The ratios (10)–(11) are at most C(log Θ)^{−(q−𝔭₀)}(2/L)^n, as the note says. ER7 (`c1-repr.md` §8) reads only A1, (AV) and Definition A; its remainder is 2C_0c_T^{−2}ε_1², a quadratic error, as the note says. The source map [ID] (`id-step.md` (1)–(4)) reads (DOM), A1/A3, [QC], [R9], [RED]. No gas enters Step 1.
- **Step 2.** `ti-2.md` line 157 reads (ID)_i with i<j only, and H(j−1) is TI(i) at levels i<j. Lemma 3(b) gives MŘ_j ≤ L^{m+1−j} at insertion; since MŘ_j ≥ M > 1, the origin j of every inserted family is below the insertion step k. So TI^f_k reads no level-k output.
- **Step 3.** Proposition W reads (P20) for old members only. At the head, UR and YA are implications (`ur-gauge.md` Theorem UR, Corollaries 6–7, with `gamma-bx.md` Theorem Γ). Corollary 6 reads (TI) for the old member G = E^(i), i<k, so it is in H_{<k}. The youngest age i = k−1 uses the coefficient bound |b_{k−1}| ≤ Cg_{k−1}α_{k−1}^{−2} (SA 16076–16085), also from H_{<k}.
- **Step 4.** Its estimate (3) is exactly SA 1a.2.8 (SA 7586–7590), including the term |1−x/t|. The tree bound needs c_adj·τ_k·B_*·M⁴ ≤ 1/2. The factor M⁴ comes from Lemma R (iv); it is paid by τ_k, which is small at the coupling floor. The Lipschitz bound by a complex dial on the old list is correct: the list action and the extractor b[·] are linear in each family.
- **Step 5.** `id-step.md` line 187 needs absolute convergence of the full connected series at every W′ ∈ 𝒦_k. Step 4 supplies it on the class SA 1a.2.8 names: the real block fields at which every background of the step exists and yields pairs in the domains of the terms. (DOM) puts 𝒦_k there.
- **Step 6.** TI (ii) at line 167 reads (ID) at level j, here (ID)_k from Step 5, so TI^E_k comes after the gas. Lemma R (v) preserves the total only where TI^E_k holds. These are the pairs P_k(B) and their continuation in datum coordinates. The step reads totals only at complete physical pairs, so this suffices (`dom.md` §1 makes the same restriction).
- **§5.** The chain (ID)_{i<k}, (20)_{i<k} → (19)_{k−1} → gas_k → (ID)_k → TI^E_k → (20)_k has no same-level edge back. b_k is computed in Step 6, and θ_{k+1} is chosen after it (c4-order row 25). The cycle κ̄ → M → C_0^UM → Θ → κ̄ is cut by um-envelope §5, given (6)–(7). Carrier-adopt §6 supplies (6)–(7) with b_d = 32, d = θc_w/4 and R, B, T fixed before M and κ̄.
- **§2 arithmetic.** Θ = C_h^UM{3 + c_ℓ[(1+4β_s)κ + g_*]} is um-envelope's t_0 + t_1κ. The λ-window is nonempty once κ is large, by row 3's bound L > 4C_h^WF C_h^UM c_ℓ(1+4β_s). Next, κ̄ ≥ Θ+1 gives log(e^κ̄−1) ≥ Θ (UM19). Also M⁴e^{−dM} ≤ 5!/(d⁵M), since e^{dM} ≥ (dM)⁵/5!. The local-stencil floor 2r_loc ≤ (8L²−9)M_1/2 is `um1-fix.md` (F); r_loc depends on L alone. Finally s(t) = δ(t)/α_{0}(t) = (A_1/C_0)(log t)^{𝔭₀−q}.
