# geo5c-count: the profile count GEO5(c)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, pinned at `4d90efd10`. Written during the gate `gates/geo-gate.md` (queue row 127), which found that rows 118-124 leave GEO5(c) open. Same-model and **ungated**: an implication, not an audit, with no status. No numeric job was run.

Credit: the label, its action and determining sequences, drop-out marks and their windows, the step formulas and the frame are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. SA means `YM4_sketch_500.tex` at `31a47c543775`. The half-cell profile is `geo-prop23.md` (5.1). The padding fact (3.2) and the nest-face argument are from `geo-5.md` Sections 3.1-3.2. Both are Codex text, gated in `gates/geo-gate.md`. The large-field regions follow Balaban (CMP 119, 122).

## 1. Statement

**Setting.** Work in level-k units, with ξ_i = L^{i−k}, η = L^{−k}, m_i = Mξ_i and s_i = MŘ_iξ_i, the side of a level-i cell. Distances are periodic sup-distances; boxes are read on their allowed non-wrapping lifts (torus floor, SA 17583). The profile of a level-i region A is any rule with φ[A](p) = 1 whenever d(p, A^c) ≥ s_i. This covers the adopted half-cell rule (5.1) and the one-cell rule (4.1) of `geo-prop23.md`, which is also the plateau of the outline's (RF33), SA 21045. Profiles read the **action** sequence (ν = 0; SA 6110-6111, 17440), written Λ^act_i, Ω^act_i, with Z^act_i = (Λ^act_i)^c. Tops and pillars are those of the **determining** sequence (ν = n), written Ω^det. A bare plaquette is carried by the top of the finest pillar among its corners (`sa-2.8-terms.md` Section 4). Stage nests satisfy the local gap (3.1) of `geo-5.md`: boxes D_{l−1} ⊂ D_l with d_∞(D_{l−1}, D_l^c) ≥ m_l and D_{t_♭} = C. The frame obeys (R19), SA 6019-6025, with upper slope B̄, exponent r ≥ 2 and θ_i ≥ γ^{-2} > e. Take L ≥ 12.

**Lemma GC.** Put C_1 := L·2^{r−1}(1 + r^r B̄), C_4 := 12C_1(1 + C_1) and d_0 := 5 + log_L C_4. Take any admissible history, any level k ≥ 1, the label at level k (the healed label of an operation at level k included), and any bare plaquette p carried by a determining top y of level j. Then

  #{1 ≤ i ≤ k : φ[Λ^act_i](p) < 1} ≤ (1 + k − j) + w ≤ d_0(1 + Ř_k)(1 + k − j).

Here w = 0, except when j lies in the window (t_♭, t_♭+n] of a standing drop-out Y of level t that contains the corner x_0 of p in the pillar of y. In that case w = ⌈log_L(12Ř_{t_♭})⌉. This is GEO5(c) of `sa-2.8-terms.md` Section 3, with that d_0, which depends only on L, r and B̄.

## 2. Four facts

**(F1) Monotone cell side.** s_i ≤ s_{i+1}, because s_{i+1}/s_i = LŘ_{i+1}/Ř_i ≥ 1 by Ř_i ≤ LŘ_{i+1} (R19). Also s_i ≥ Mη ≥ η.

**(F2) Gap of the action label.** For 1 ≤ i < k: d_∞(Z^act_i, Ω^act_{i+1}) ≥ 2s_{i+1}.

*Proof.* (a) *At creation.* Step i+1 creates Ω_{i+1} with Ω_{i+1}^c ⊃ Ŷ^{∼8}, where Y = Z_i is the live region (SA 17320). The set Ŷ^{∼8} contains every point within 8s_{i+1} of Y. At that moment the action Z_i equals the live Z_i. The two sequences differ only inside standing drop-outs, at levels of their windows (R21, SA 6098-6105). A window of a mark of level t' lies in (t'_♭, t'], and a drop-out never replaces its top entry Λ_{t'} (SA 17423-17430: Λ_l is replaced for l < t only, and "Λ_t ∩ X = ∅"). So the gap is at least 8s_{i+1} when it is created.

(b) *Later.* Later steps only add higher members. An operation at level t ≥ i+1 can change the action entries at levels i and i+1 only by filling. Healing replaces Ω_l, Λ_l by Ω_l ∪ Q, Λ_l ∪ Q for l ≤ t. An island does the same, except at Λ_t (SA 17417-17419). A drop-out keeps its pre-operation action entries (R21 with ν = 0). A filling removes the holes of Q at levels below t. The only new pairs it creates are a new small-field point of Q at level i+1 ≤ t and an old action hole z ∈ Z^act_i∖Q. Such a z lies in Z^act_{t−1}, by nesting, and Z^act_{t−1} is the live Z_{t−1}, by (a) applied at level t−1. Step t put Z^act_{t−1} into Ω_t^c. Q is a component of the live Z_t and z ∉ Q. By the padding fact (`geo-5.md` (3.2), from Z_t ⊃ (Ω_t^c)^{∼2}, SA 17321), d(z, Q) ≥ 2s_t ≥ 2s_{i+1} by (F1). Several components operated on at once are treated pair by pair in the same way. ∎

**(F3) Action level against determining level.** Let x be a site in layer j of the determining sequence (x ∈ Ω^det_j∖Ω^det_{j+1}). Put j'(x) := max{l ≤ j : x ∈ Ω^act_l}, or 0 if there is none. Then j'(x) ≥ j − w, with w as in Lemma GC.

*Proof.* The sequences differ only inside standing drop-outs, at their window levels, and at one place and level at most one drop-out is active (SA 17440, "marks wait"). Moreover Ω^act_l ⊂ Ω^det_l, because Z''_l ⊂ Ω_l^{°c} (R21).

*Case 1: no standing drop-out containing x has a window containing j.* Let l ≤ j. If no window of a mark containing x contains l, the entries at x agree, and x ∈ Ω^det_j ⊂ Ω^det_l gives x ∈ Ω^act_l. Otherwise l ∈ (t'_♭, t'_♭+n'] for a standing drop-out Y' ∋ x of level t', and then j > t'_♭+n'. Y' stays live, and step t'+1 puts it into Ω_{t'+1}^c, so x ∈ Ω^det_j forces j ≤ t'. At such a j the entry of Y' is the unchanged Ω^°_j (R21), so x ∉ A'_j := Y' ∩ Ω_j^{°c}. The pre-operation holes increase with level, so x ∉ A'_l, that is, x ∈ Ω^act_l. Hence j'(x) = j.

*Case 2: j ∈ (t_♭, t_♭+n] for the standing drop-out Y ∋ x of level t.* Write D_l = Z''_l(Y), C = Y ∩ Z_{t_♭} = D_{t_♭}, B_l = Y ∩ Z^°_l and A_l = Y ∩ Ω_l^{°c} ⊂ B_l (pre-operation, t_♭ ≤ l ≤ t). By R21, x ∈ Y∖D_j. Older marks inside Y lie in C, and x ∉ C. Younger marks containing Y have windows above t. So at x and at levels l ≤ j, only Y's entries matter.
- *l ≤ t_♭.* Inside Y the action and determining entries agree at level t_♭, so Y∖C ⊂ Λ^act_{t_♭} ⊂ Ω^act_l (`geo-5.md` (4.1)). Hence x ∈ Ω^act_l.
- *t_♭ < l ≤ j − w.* Quietness gives B_u = H_u^{[10]} and A_u = H_u^{[8]}, with H_u = hull_u(B_{u−1}) (SA 17576-17583) and B_{t_♭} = C. A cell hull lies within one cell side of its set, so B_u ⊂ B_{u−1} + [−11s_u, 11s_u]^4. Hence A_l ⊂ C + [−τ_l, τ_l]^4, with τ_l := 11Σ_{u=t_♭+1}^{l} s_u < 12Ř_{t_♭}m_l, using s_u = Ř_u m_u ≤ Ř_{t_♭}m_u (Ř is non-increasing), Σ_{u≤l} m_u < m_l L/(L−1) and L ≥ 12. Every face of the nest boxes moves outward by at least m_u at stage u (the gap (3.1), read on carriers as in `geo-5.md` Section 3.1). So D_j ⊃ C + [−σ_j, σ_j]^4, with σ_j ≥ m_j = L^{j−l}m_l ≥ 12Ř_{t_♭}m_l > τ_l, by the choice of w. Thus A_l ⊂ D_j ∌ x, so x ∈ Y∖A_l = Y ∩ Ω^act_l. ∎

**(F4) Frame bound.** For 0 ≤ u ≤ k: Ř_u ≤ C_1(1 + Ř_k)(1 + k − u).

*Proof.* Put y_u = min_{i≤u} θ_i ≥ y_k. If y_k is attained at some v ≤ u, then y_u = y_k. Otherwise it is attained at some v ∈ (u, k], and y_u ≤ θ_u ≤ θ_v + B̄(v−u) ≤ y_k + B̄(k−u) by (R19). Since y_k > 1, log y_u ≤ log y_k + log(1 + B̄(k−u)). For v ≥ 0, log(1+v) ≤ r v^{1/r}: equality holds at 0, and the derivative of the right side, v^{1/r−1}, is at least 1/(1+v). So (log(1 + B̄(k−u)))^r ≤ r^r B̄(k−u). Convexity gives (a+b)^r ≤ 2^{r−1}(a^r + b^r). Since (log y_u)^r ≥ 1, the smallest power of L not below it is less than L(log y_u)^r, and (log y_k)^r ≤ Ř_k. So Ř_u < L·2^{r−1}(Ř_k + r^r B̄(k−u)) ≤ C_1(1+Ř_k)(1+k−u). ∎

## 3. Proof of Lemma GC

Let x_0 be the corner of p in the pillar of y. The pillar is a level-j block in layer j, because members are unions of aligned 𝔐ξ-cubes and nested grids refine them (SA 9599). So x_0 ∈ Ω^det_j∖Ω^det_{j+1}. For 1 ≤ i < j'(x_0), we have x_0 ∈ Ω^act_{i+1}. By (F2), d(p, Z^act_i) ≥ 2s_{i+1} − η ≥ s_{i+1} ≥ s_i, using (F1). So φ[Λ^act_i](p) = 1. The count is therefore at most #{i : j'(x_0) ≤ i ≤ k} ≤ 1 + k − j'(x_0) ≤ 1 + k − j + w, by (F3).

To bound w in Case 2, note that j ≤ t and t_♭ = t − Ř_t (SA 6035: N_t = Ř_t). By (F4), Ř_t ≤ C_1(1+Ř_k)(1+k−j). Hence 1 + k − t_♭ ≤ (1+C_1)(1+Ř_k)(1+k−j), and Ř_{t_♭} ≤ C_1(1+C_1)(1+Ř_k)^2(1+k−j). With log_L(1+v) ≤ v for v ≥ 0, this gives w ≤ 1 + log_L C_4 + 2Ř_k + (k−j). So the count is at most 2(1+k−j) + 2Ř_k + 1 + log_L C_4 ≤ d_0(1+Ř_k)(1+k−j). ∎

## 4. Consumer and scope

- `sa-2.8-terms.md` Lemma W(4) now holds with this d_0, so v(p) ≤ x + B_*d_0(1+Ř)(1+k−j(y)) at every plaquette, on the whole torus, for the healed label. Bound 5.5 (R_1) is unchanged. Outside drop-out windows the sharper count 1 + k − j holds.
- **Reads:** the step formula SA 17320-17322; the three fates, SA 17417-17430; (R21), SA 6098-6105; "marks wait", SA 17440; the quiet class geometry, SA 17576-17583; the frame (R19); the padding fact and the core containment (4.1) of `geo-5.md`; the local nest gap (3.1).
- **Does not read:** the upper face-movement rule, Definition A, or the half-cell width. Any profile that equals 1 at distance s_i from the complement is enough.
- **Status:** a written implication by the same provider as the gate that asked for it. It counts only after a cross-provider gate. The hardest steps to check are (F2)(b), which needs every later change of the action entries at levels i and i+1 to be a filling, and (F3) Case 2, which compares pre-operation holes with stage boxes.
