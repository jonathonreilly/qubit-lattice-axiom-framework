First failing step: none.

# LG1 pass-3 referee report (`library/lg1.md`)

Provenance: Claude Opus 5.5 (claude-opus-5-5), fresh session, 2026-11-05. One reading by one other model of a Codex distillation. This is not an audit and grants no status.

Read for the comparison: `library/lg1.md` (whole); `library/am1-port.md` (whole); `library/d2-d4.md` §2; `parts/upper-chain.md` Text §0 and Lemma 1.1; `library/t0-skeleton.md` §2 (Lemma S); `gates/o4-check-1.md` and `gates/bridge-check.md` (whole); `library/ym4-assembly.md` §4 (LG1 line) and §5 (LG1 entry). Outline `sa/ym4.tex` (SHA-256 `d7f77d4d…`, SHA-1 `107abaef…`) and `sa/YM3_I.tex` (SHA-1 `ea67b3ce…`): these hashes match the pinned files named in the text and in the two gates. I read every cited SA and Y3 range at its section and statement headers, and in full at SA 236–294, 4486–4497 and 6905–6915 and Y3 78338–78372. Each range holds the content the text assigns to it.

## What I checked

Each numbered statement against its proof, and each against its source note and gate.

- **Lemma 1.** 0 ≤ a_p ≤ 2 and e^{-2βN_P} ≤ Z ≤ 1. Covariance a_p(r^*U) = a_{rp}(U) gives O_a(f)∘r^* = O_a(f∘r^{-1}). Support: at x_μ = k+1/2 both plaquette types strictly above have lowest vertex ≥ k+1. The open-side restriction is correct. SA 6913 states the side property without "open"; the text's narrowing is right, since a plaquette centred on the mirror crosses it.
- **Lemma 2.** 6 plaquettes per bond, 8 bonds per vertex, denominator ≥ e^{-12β|B|}. The ratio e^{±2δ} and the uniform kernel convergence as the strength tends to zero are correct. Gauge averaging and determination are correct.
- **Lemma 3.** ½tr(gh^{-1}) = s(g)·s(h); the coefficient sum is e^{-β}e^{4β} = e^{3β}. At n = e_1+e_2 the crossing plaquettes are exactly the (1,2) plaquettes with base height c−1. I checked that θ_c(x_1,x_2) = (c−x_2, c−x_1) swaps P_+ and P_- with the stated common orientation. At a bond cut, ∫k_S(u,w·u')dw equals the double average by Haar invariance, so (7) is a positive Gram form. No gauge invariance of F is used.
- **Lemma 4.** The run-doubling argument and the normalisation by (Z_j^dis+ε)^{1/(2s)} are correct. The wall-reflection group acts simply transitively on the 2s slabs, so copies are well defined. Triangle inequality, |z|-homogeneity (half the copies conjugated), p(F̄) = p(F), p(1) = 1: correct.
- **Lemma 5.** 3 plaquettes per site per plane meet its positive bonds, so ≤ 18|∂_1D| noninterior plaquettes; ≤ 6|∂_1D| torus classes lack an interior representative. Oscillation 2β·24|∂_1D| = 48β|∂_1D|, and a density comparison costs exactly the oscillation. The omitted-term cost 2|t|‖A‖(m−m_in) and |∂_rD| ≤ (2r−1)^4|∂_1D| are correct.
- **Lemma 6.** KP_r ⊂ P_r; strict positivity; trace one; trace on W_r ≤ T_r ≤ β^r/r!; Σ_j|e_rj|^2 = dim W_r ≤ C(r+4,4); the root kernel converges uniformly. The gauge commutation of Q_S by uniqueness of the positive root closes the omission recorded in `o4-check-1.md` §1. The density statement is correct.
- **Lemma 7.** The integrated kernels are EQX_tQP; cycling gives Tr(X_1M⋯X_sM). The trace-Hölder word argument (reflection continues the alternation in every case) and Tr C^s ≤ Tr D^s are correct. Applied to the 2s factors X_tM^{1/2}, M^{1/2} it gives ∏‖X_t‖. The exchange limit 0 ≥ i^4ν(φ_ε) − C_εi^3, both signs of ε, and the skew operator with ⟨q_u,Dq_{u'}⟩ = Φ are correct.
- **Lemma 8.** The temporal gauge sets vertical bonds to one. V_S ≤ 8|S|; Φ ≥ e^{-10β|S|}; N and the layer weight ≥ e^{-12β|S|}. The layer equation (17) and the test ψ = φχ/Φ (needs n−1 ≥ m) are correct. θU[ũ] = U[R_{2t_0+1}ũ]. θ_{3/2}θ_{1/2} = τ_2.
- **Lemma 9.** ι = N^3h; [Q:Γ_i] = 2i^4; Γ_i is adapted with H = 2ih; |D_i| = 2i^4N^3h; (20) is 2/(iN)+2/(ih)+2/(iN)+2/(iN). I checked w_{2k}^{-1}τ_{(2k-1)v_h} = ϑ and τ_{v_h}w_j = w_{j+1}ϑ for both parities. Jensen is in the folded measure, in the right direction. A bond lies in at most two closed slabs, so in at most 2|B_A| supports. The family is invariant under T⊕Z(2v_h), since τ_{2v_h}w_j = w_{j+2}. Limit order (i first, then t) is correct.
- **Theorem 10.** Separation, polarisation, the period v = 2kn ∈ 2Z^4, θτ_v = τ_{-v}θ, and the L^2 extension to Borel half tests are correct. 4 + 12 normal families; generation of Z^4 ⋊ W_4 is correct.
- **Lemma 11.** |∂_1D| ≤ 8n^3, so 48β·8n^3/N_b = 384βl^4a^{-3}ℓ^{-1}. This differs from the 72β of `ui-port.md` and the C of `d2-d4.md` (3); all three are valid upper bounds. log(1+x) ≥ x − x^2 on |x| ≤ ½; p(1+tG) ≤ 1+tp(G); the phase step; the coarse cell (odd power L^k, centred on a fine centre) and the coarse dissemination are correct.
- **Lemma 12.** All six steps are correct. The scope remark matches `o4-check-1.md` §4 item 3.
- **Theorem 13 against `ym4-assembly.md` §5 LG1(a).** Clauses 1–6 match. Clause 1 is narrowed to the open side, as above. Clause 3 adds the all-state domination (23), which reads Theorem 10 (the S1g dependency noted in `bridge-check.md` §1 item 2). Imports: none, as in the assembly.

Each import (Haar measure, compactness, Riesz, Stone–Weierstrass, finite-dimensional spectral theory and the positive root, Fubini, martingale L^2 convergence, Cauchy–Schwarz, Jensen) is used only within its stated hypotheses.

## Findings

1. **L63, Lemma 1 origin.** It cites `upper-chain.md` Text §0. That section uses a dyadic lattice and the corner field e_a(x), not barycentres. It supplies only the finite-measure bound. The covariance and support claims rest on SA 6913 and on the proof given here. Not fatal; wording. Repair: cite §0 for the probability bound only.
2. **L236, Lemma 7 proof.** "since P commutes with E,Q" is not needed for the cycling step: after cycling, each block is QPEQ = M as written. The commutation is needed one line later, for M = (E^{1/2}PQ)^*(E^{1/2}PQ). Not fatal; wording. Repair: move the clause to L238.
3. **L346, Lemma 9.** "Any coincident boundary copies can be shared with half weight" has no referent. Each term w_jA_T lies in one closed slab, so in one closed half at every wall. Wall-plane bonds lie in both closed halves, and Lemma 3 covers closed halves. No sharing is needed. Not fatal. Repair: delete the sentence.
4. **L47, board copies.** "The unique composition of board-face reflections" is unique as a group element, not as a word. The parity used for conjugation is the determinant, so it is well defined. Lemmas 4 and 11 use only this. Not fatal; wording. Repair: say "the unique element of the reflection group".

## Verdict

LG1 holds as written. Every numbered statement is proved exactly as stated, from the listed foundational tools only. Every d = 4 constant and index rechecked here is correct: 6, 8, 12β, 48β, (2r−1)^4, e^{3β}, e^{-10β|S|}, e^{-12β|S|}, N^3h, 2i^4, 6/(iN)+2/(ih), 384β. The two gate corrections (choice of r; gauge commutation of the root) are carried in. The bond-cut correction of `bridge-check.md` §4 is also carried in. The four findings are wording only.

Checked line by line by Claude (fresh session).
