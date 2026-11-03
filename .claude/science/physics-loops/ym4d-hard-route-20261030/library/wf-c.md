lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T05:15Z

# WF-c: complex box localisation, Landau node lift, pointed-core admission

Row 173. Pinned at commit b264f9a3c. In progress; sections are written as they close.

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Research text, not an audit; it grants no status. Outline: Sussman–Alpoge `YM4_sketch_500.tex` at `31a47c543775`; SA numbers are its lines. No numeric job was run.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the window maps, the pair class (R4)–(R6), Theorems 5 and 6 of (1b) and the box-map package. T. Balaban for background localisation (CMP 109, 116 as cited there) and the axial/Landau gauge constructions (CMP 95, 96, 102). OpenAI Codex for `ld-decoupled.md`, `b4-step.md`, `nl-r9.md`, `pw-bridge.md`.

## 1. Check of `ld-decoupled.md` (Codex)

Checked line by line by Claude, Sections 2–4 and the new arithmetic of Section 1. Section 1 is itself Codex's check of `cond-c.md`; it is not re-reviewed (FINISH, How we work 5), except its frame-factor display.

**Verdict: (LD) ADVANCE.** Checked line by line by Claude, first failing step none. It is an implication from [PW] (`pw-bridge.md` (6.6)–(6.7), Section 7), [NL] (`nl-r9.md` Section 6, `dec-field.md` (5.1)), AV, BC and the WF domains.

What was redone:

- *(1), floors.* θ_L = (τ_L/16)min(M,ρ) = τ_Lρ/16 ≥ τ_Lρ'/16 ≥ 16 log L. Correct.
- *(2), rates.* `pw-bridge.md` (6.4)–(6.6) already pay the tags: the column bound has rate τ_L/8 after the factor e^{16κ̄}e^{128κ̄t/ℓ_P} with ℓ_P ≥ 2048κ̄/τ_L. A weight of rate λ = τ_L/16 then leaves τ_L/16 for the column sum, as (6.7) states. The 16 + 128t/ℓ_P count is (6.4) verbatim (two traversals, arcs of length ℓ_P/4, sixteen cubes each by (P)).
- *(3), BC.* For the determining sequence Lemma G of `cond-c.md` gives d(Ω_i^c, Ω_{i+1}) ≥ Mξ_{i+1} ≥ c_gξ_i. The segment between the last exit from Ω_i^c and the next entry into Ω_{i+1} lies in layer i, where the weight is 1/ξ_i. There are k−p−1 such disjoint segments for a start in layer p. Correct; it is `geo-5.md` Section 3.6.
- *(4)–(5), weighted fixed point.* Contraction constants q = C_WB³R ≤ 1/8 and q_C = 2C_CBR ≤ 1/4 match `dec-field.md` Proposition 5.1. The weighted step needs W(0) = 0 and C(0) = 0 and the weighted Lipschitz bounds on unweighted balls; `nl-r9.md` Section 6 and its Result state both. The weighted norms are finite on a finite torus, so absorption is legitimate. B/((1−q)(1−q_C)) = 32B/21 ≤ 2B. Correct. The same bound also follows by integrating (5.2) of `dec-field.md` along tB', 0 ≤ t ≤ 1.
- *(6).* The X norm is sup_y w(y) max{ξ_y|a|, ξ_y²|∇a|} (`dec-field.md` Section 5), so the sum in (6) costs a factor 2, absorbed in C.
- *(7) and (LD).* On the path V(ν) = e^{iη_k(t+νζ)h}U_+ the tangent is exactly ζh, since h_b commutes with its multiples. AV with (6) gives |v'_c| ≤ C δ_k (ξ_c/ξ_p) e^{−θ_L(k−p−1)_+}, |ζ| ≤ 1. This is the form `cond-c.md` 6.4 reads.
- *Section 1, frame factor.* √(b+1) ≤ √2 e^{b−1} for b ≥ 1 (equality at b = 1, and the right side grows faster). So ρ_j e^{−θ_L(b−1)} ≤ C√(1+a) e^{−(θ_L−1)(b−1)}. Correct.

Clarifications, none a defect: (i) the fine-layer pointwise size of h is δ_k/ξ_p, larger than the top-layer δ_k/ξ_k by L^{k−p}; the factor e^{−θ_L(k−p−1)} pays it, which is why θ_L > log L matters. (ii) The proof reads the step's own sequence for both d_B and BC; that is the common determining sequence of `cond-c.md` Lemma E, so no second metric enters.
