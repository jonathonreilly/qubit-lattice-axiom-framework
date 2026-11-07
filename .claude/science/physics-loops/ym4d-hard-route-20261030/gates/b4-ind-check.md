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
| §2 constant order | ADVANCE, conditional on um-envelope (6)–(7) as supplied by inv-root (17)–(20) and carrier-adopt §6. Three ceilings must be added (D3); no cycle |
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
- **Step 4.** Its estimate (3) is exactly SA 1a.2.8 (SA 7586–7590), including the term |1−x/t|. The factor M⁴ of Lemma R (iv) multiplies the rooted domain count. It enters the domain sum S_{σ_0} inside τ_k and the constant of (1), both fixed after M. The coupling floor makes τ_k small, so the tree bound c_adj·τ_k·B_* ≤ 1/2 holds. No decay exponent changes, as §2 item 4 says. The Lipschitz bound by a complex dial on the old list is correct: the list action and the extractor b[·] are linear in each family.
- **Step 5.** `id-step.md` line 187 needs absolute convergence of the full connected series at every W′ ∈ 𝒦_k. Step 4 supplies it on the class SA 1a.2.8 names: the real block fields at which every background of the step exists and yields pairs in the domains of the terms. (DOM) puts 𝒦_k there.
- **Step 6.** TI (ii) at line 167 reads (ID) at level j, here (ID)_k from Step 5, so TI^E_k comes after the gas. Lemma R (v) preserves the total only where TI^E_k holds. These are the pairs P_k(B) and their continuation in datum coordinates. The step reads totals only at complete physical pairs, so this suffices (`dom.md` §1 makes the same restriction).
- **§5.** The chain (ID)_{i<k}, (20)_{i<k} → (19)_{k−1} → gas_k → (ID)_k → TI^E_k → (20)_k has no same-level edge back. b_k is computed in Step 6, and θ_{k+1} is chosen after it (c4-order row 25). The cycle κ̄ → M → C_0^UM → Θ → κ̄ is cut by um-envelope §5, given (6)–(7). Carrier-adopt §6 supplies (6)–(7) with b_d = 32, d = θc_w/4 and R, B, T fixed before M and κ̄.
- **§2 arithmetic.** Θ = C_h^UM{3 + c_ℓ[(1+4β_s)κ + g_*]} is um-envelope's t_0 + t_1κ. The λ-window is nonempty once κ is large, by row 3's bound L > 4C_h^WF C_h^UM c_ℓ(1+4β_s). Next, κ̄ ≥ Θ+1 gives log(e^κ̄−1) ≥ Θ (UM19). Also M⁴e^{−dM} ≤ 5!/(d⁵M), since e^{dM} ≥ (dM)⁵/5!. The local-stencil floor 2r_loc ≤ (8L²−9)M_1/2 is `um1-fix.md` (F); r_loc depends on L alone. Finally s(t) = δ(t)/α_{0}(t) = (A_1/C_0)(log t)^{𝔭₀−q}.

## 3. Defects, ranked by what each breaks

### D1. The list budget is an output of the induction, not an input

This is a hidden loop. It breaks line 217 ("Thus H_{<k} extends to H_{≤k}") and the box's "uniformly in its length". The regular part of the induction is not affected.

- **Where.** §2 item 4 fixes "the uniform list budget" before the run (line 45). 𝒫 assumes "bounded input lists" (line 63). H_{<k} carries "admitted aged families and their defect budgets" (line 85). Line 147 says the age argument cannot bound this budget. Lines 190–192 file the bracket β_k := F(S_sym+D) − F(S_sym) as "the defect output". Its bound is ‖β_k‖ ≤ Cs_{k−1}N_{k−1}(D), with N_{k−1}(D) := Σ_{j<k} ρ_{j,k}² d_j.
- **Why it is a loop.** The list at level k+1 holds β_k and the defects D_H that (INS) files at step k. Both are made at level k. A budget fixed before the run and assumed in 𝒫 at every level is therefore a claim about outputs of the induction. Line 217 does not prove it at level k, and §5 does not list this edge.
- **Explicit failure of the available bound.** A defect has no counterterm. So it enters (19) with weight ρ² and no age factor (WF10, SA 16057–16067; `b2-extract.md` line 183). For the new defect the note gives only Step 4's bound, d_k ≤ Cs_{k−1}N_{k−1}(D) + e_k. Here e_k bounds the defects newly filed at step k. This system has no bound uniform in the run length K:
  1. Take the smallest weights ρ ≡ 1 and equality. Then d_k = Cs_{k−1}Σ_{j<k}d_j + e_k satisfies every inequality of the note.
  2. Its sums S_k := Σ_{j≤k}d_j obey S_k = (1+Cs_{k−1})S_{k−1} + e_k. If some e_{k_0} > 0 and Cs ≤ 1, then S_K ≥ e_{k_0} exp(½C Σ_{k_0≤i<K} s_i), because log(1+x) ≥ x/2 on [0, 1].
  3. The frame bound |θ_{i+1}−θ_i| ≤ D (`dom.md` §2) gives θ_i ≤ θ_K + DK for i ≤ K. So s_i ≥ (A_1/C_0)(log(θ_K+DK))^{−(q−𝔭₀)}, and Σ_{i<K}s_i grows like K(log K)^{−(q−𝔭₀)}, without bound.
  4. A defect of remainder size has at most the large-field factor e^{−c p_0(g)²}, with p_0(g) = A_0(log g^{−2})^{𝔭₀} (SA 6029). Its exponent is a power of log θ, and θ ≤ θ_K + DK along the run. So it loses to exp(cK(log K)^{−(q−𝔭₀)}).
  So these estimates give no budget N_* fixed before the run. This is a gap, not a counterexample: the true defects may be smaller.
- **When a defect is present.** (INS) files D_H := H − ℛ_{m+1}H. Its total vanishes only under (R-inv) (`ti-2.md` §2, §4), and (R-inv) needs (NAT) beyond the lead's list. Only then may D_H be dropped. Nonconstant sources also make defects (D2). So even the constant-source run has some e_{k_0} > 0 unless (R-inv) holds.
- **What still holds.** Fix one level k and take H_{<k} with its budget. Then the boxed conclusions hold: B4_k, (1.6)_k, (ID)_k, TI_k, (20)_k and (19)_{k−1}. Steps 1–6 never read the budget at level k.
- **Repair candidates (not proved here).**
  - (a) Prove (R-inv) through (NAT). Then D_H has total zero and is dropped, and the constant-source run has no defect sector. SA's "renormalised" list already asks for invariant totals of the H^(j) (SA 7581–7582).
  - (b) Carry the budget in H with a profile π_j that the bracket keeps: Cs_{k−1}Σ_{j<k}ρ_{j,k}²π_j ≤ π_k/2. The geometric profile π_j = L^{−(K−j)} passes: Σ_n(1+n)L^{−n} is finite and Cs is small at the floor. Source defects have this profile (SA (LB7)–(LB9), 16434–16492). A remainder-shaped profile π_j = e^{−c(log θ_j)^a} fails. By the frame bound, Σ_{j<k}(1+k−j)π_j/π_k ≥ cθ_k²(log θ_k)^{−2(a−1)} when θ falls along the run. So (b) does not cover D_H.
  - (c) Bound the bracket inside the large-field credit of the region that made D_H. Neither this note nor its inputs do this.

### D2. Nonconstant source arrays: Step 6 has no Euclidean output, so H_{≤k} is not reached

This limits the scope. The consumers D1 and TU10 read sources.

- **Input side: correct.** Lines 148–149 say each site-frozen source is a Euclidean family with its own extractor, and that no invariance of the array is used. Theorem P gives (20) for each Euclidean family. So Steps 3–4 hold on SA's product box (SA 4006–4012, 16000–16007).
- **Output side: fails as written.** TI^E_k and Lemma R (v) need an invariant total. At a nonconstant source array the total is not invariant. So Step 6 does not give a Euclidean member per base point plus a scale-small defect at level k. Then the hypothesis at level k+1 fails for that array. SA 4921 names this as the task that remains: "prove the asserted bounds for the full array, including its noncovariant defects".
- **Repair (not proved here).** Take as the level-k member at z the constant-source output, with the source frozen at its value at z. Bound the difference from the actual output by SA's derivative defect (LB7)–(LB9). This has the scale gain L^{−(m−j)}, so with D1 (b) the defect sector would close. Until then, the boxed TI_k, (20)_k and the closure hold for constant sources only.

### D3. Three ceilings are missing from §2's order (minor; no cycle)

- (2) and (3) contain |1−x/t|, as SA 1a.2.8 does. The tree bound needs τ_k small. So the Wilson-weight disc |x−t| ≤ c_x t needs c_x ≤ cW_0e^{−Θ}/(c_fL⁴S_{σ_0}).
- um-envelope §5 also needs H_0c_x ≤ ¼min(ε_0/2, 1/(6DM⁴)).
- `id-step.md` §4 needs C_Lδ < ε, that is, A_1/A_0 < 1/C_L. This is a second ceiling on the ratio that DOM also bounds.

§2 lists none of the three. The first two come after W_0 and M and before the floor; the third comes after L, with DOM's ratio. So they add no cycle. Cauchy estimates in x (SA 22942) then cost the fixed factor 1/(c_x t).

## 4. Inputs that changed after `99bf6836b`

None of these changes adds a same-level edge. Each reads only earlier members.

- **BX⁺.** `bx-fix.md` now has Theorem BX′ and Proposition I. `gamma-bx.md` replaces several of its parts by Theorem BX*, Proposition W* and Proposition I*. These are proved by Claude and not yet checked (row 234). Proposition I* is an induction of its own. Its hypothesis (I_k) concerns members of levels ℓ ≤ k at fluctuation index k, that is, levels below the output level. So it fits H_{<k}, and H should carry it.
- **ω_n.** Proposition W* gives ω_n = C_M(1+n)^{3/2}L^{−α_H(n−1)}. The constant enters only N_*, and N_* is chosen after M.
- **New constant conditions.** Lemma O adds L ≥ L_0 and the ceiling CC_αL^{1−α_H}(s_k+c_ν) ≤ 1/8. Put L_0 in §2 item 1 and the c_ν ceiling in item 4. The binding case of Lemma O's second bound is j = k, which needs 1+B̄ ≤ L^{4+2α_H}/16. Here the frame envelope B̄ is fixed with L (c4-order row 3a), so this is a growth condition on B̄(L). It is not checked here.
- **UR, YA.** These are now implications: `ur-gauge.md` Theorem UR and Corollaries 6–7, with `gamma-bx.md` Theorem Γ. They read (ER8u), the Landau bound (5), (FG) under (REL′), and (TI) of the old member. If they replace the inputs, H_{<k} must also carry (FG)_i (`gamma-bx.md` Proposition 3).
- **ER7.** `c1-repr.md` §8 was checked by Claude in row 179. The note uses it correctly.

## 5. Folded check of `dom.md` §§2–4 (Codex)

Row 213 folds this check into the next lane that reads `dom.md`. Step 1 of the note reads it.

**Checked line by line by Claude, first failing step none, as an implication.** Two inputs are cited and were not re-derived: (4)'s pivot contraction (`s210-fix.md` Lemma G, checked by Codex in `loc.md` §4.1) and (9)'s real tower step (`a3-close.md` Lemma T, real part).

- **(2).** For log y > 2s, the logarithmic derivative of y^{−1/2}(log y)^s lies in (−1/(2y), 0). An increment of size at most D from y ≥ Θ ≥ D therefore changes the logarithm by at most 1/2, so neighbour ratios lie in [1/2, 2]. The three bounds of (2) follow, including a_i ≥ (C_0/2A_0)(log Θ)^d ε_i.
- **(5).** The curl expansion of e^{iη_kh}U_* gives the three terms, as stated. They are at most C_Fδ_k in F_k units, since ‖h‖_1 ≤ C_HC_Pδ_k.
- **(5) ⇒ (R15).** This is redone in Section 2 above.
- **(6)–(8).** In level-i units the potential gains L^{−n} and its derivative gains L^{−2n}. Then F_i(U)/(ce_i) < L^{−2n}·2·2^n = 2(2/L²)^n.
- **(10).** Dividing (9) by a_iL^{−i−p} and by a_iL^{2v−i−p} gives the same quotient (C_Tε_s/a_i)L^{−2(s−i)}L^{p−i}. Then (2) bounds it by (2C_TA_0/C_0)(log Θ)^{−d}(2/L²)^n.
- **(11).** The real gauge gains only L^{−n}, which gives (2/L)^n.
- **Clauses (a)–(e).** Each maps to its displayed step as stated.

## Result

**Kind (FINISH item 9).** A check of our own text, `library/b4-induction.md` (Codex). Checked line by line by Claude.

- **The order at level k: ADVANCE.** Steps 1–6 read only 𝒫, H_{<k}, the named inputs and earlier steps of the same level. TI^f_k precedes (ID)_k, and TI^E_k, the re-pointing and (20)_k follow it.
- **The circularity check: correct for the displayed chain.** One loop is missed. The defect and remainder list budget is assumed before the run, but it contains level-k outputs: the bracket β_k and the (INS) defects D_H (D1).
- **The constant order: ADVANCE.** It is conditional on um-envelope (6)–(7), as supplied by inv-root and carrier-adopt. Add the three ceilings of D3 and, at the head, `gamma-bx.md` Lemma O's two conditions.
- **First failing step: line 217**, for the list budget. With the note's own bounds (Step 4's bracket bound and WF10's ρ² weights with no age factor), the defect sector has no bound uniform in the run length unless every defect vanishes. So the box holds at one level from H_{<k}, but "uniformly in its length" is not proved.
- **Nonconstant source arrays (D2).** The closure is not reached there. TI^E_k and Lemma R need an invariant total.
- **Folded check:** `dom.md` §§2–4, first failing step none.

**What would change.**
- If (R-inv) is proved through (NAT), D_H has total zero and is dropped. D1 then disappears for the constant-source run, and the joint induction closes there, given BX⁺, UR, YA and LOC. Full B4 also needs the typed tests.
- If (R-inv) is not proved, the (INS) route needs a defect-budget argument that the present bracket bound cannot supply. This bears on `ti-2.md`'s choice of (INS) in place of (NAT).
- For sources, SA's derivative defect (LB7)–(LB9) has the geometric profile of D1 (b). It is the natural repair of D2.

**Evidence for other owners (only this file was written).**
- `b4-induction.md` §3 and line 217: make the list budget a statement carried in H. Line 217 should say the budget is not yet carried.
- `ti-2.md` §2 (INS): D_H is "filed as a scale-small noncovariant defect". By D1, a remainder-sized defect lacks the profile that the budget needs.
- `t0-skeleton.md` row B4: add "defect budget across levels, or (R-inv)" to the open items.

**Still open.** BX⁺ (`gamma-bx.md`, check row 234), LOC (first failed input: (N1′)), the typed tests (SA 5066–5106), (R-inv) or a defect-budget argument, and the source-array closure. `id-step.md` is not yet checked by the other model. This lane used only its statements.
