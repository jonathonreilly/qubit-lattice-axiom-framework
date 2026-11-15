lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GB1-QL referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), under PR #10138's method. The lane was launched under the pass-1 lane template; its task is pass 3, the referee of `GB1QL.md`. This session wrote neither pass 1 (`GB1QL_DRAFT.md`, Claude) nor pass 2 (`GB1QL.md`, Codex `gpt-6.1-terra`). This is one check: one whole-part, line-by-line read. No review of this review was commissioned. It grants no status and adopts nothing.

**Text read.** `GB1QL.md` as of commit `022ea74a0` (the last commit that touches it; also the branch head `claude/toe-assembly` when read). SHA-256 of the file read: `a663c30f8d5843b5442ac7d749cb7bdd284f39703bc4fec16328776cae31cbf6`. Line numbers below refer to that file.

**Sources read, with commits.** All at `022ea74a0` in this checkout. Pass 1: `GB1QL_DRAFT.md` (last changed `72cf23128`), SHA-256 `4d06962b9bfc929079b504fe6458c10c16abd148394854f83f23085d8f5a6ac0`; this equals the hash `GB1QL.md` line 11 records. The prior-work digest `prior/GB1QL.md` (all, 86 lines). `LW1_REFEREE.md` lines 1-80 (format) and `Y2W_DRAFT.md` lines 1-30 (head format). Further lines read are listed in section 0.1 at the end of this report.

**Working-set entries used.** None is used as a premise. The referee reads `L5-U`, `L5-O`, PS-5 and PS-6r only where `GB1QL.md` quotes or cites them, and checks those quotations in the verdict table.

**Method.** Every proof was re-derived by hand. A `[check]` is a scratch computation in `/tmp/toe-GB1QLref/` (under a minute and under 1 GB; the one numerical check took 0.5 s and 200 MB, started at 54 percent free memory). It guides only and proves nothing. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A **referee closure** is a short complete argument for a missing step, written so that it can be formalized.

---

## 1. Verdict table

Line numbers are those of `GB1QL.md` at `022ea74a0`. "Draft" means `GB1QL_DRAFT.md`.

| # | Item (GB1QL line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 Status (5) | CORRECT | The scope sentence matches what sections 1-2 prove. |
| 2 | §0 GAP summary (7) | CORRECT | Both gaps are real: items 13 and 72. |
| 3 | §0 Open by name (9) | CORRECT | Edit E5 asks for one wording change ((H-GI) and (H-Haar) as properties of the missing measure). |
| 4 | §0 Provenance (11) | CORRECT | The recorded draft hash equals the hash of `GB1QL_DRAFT.md` at `72cf23128`. |
| 5 | §0 Prior work (13) | CORRECT | `GA2_Y2.md` line 39 is Theorem 2.1 (N), line 43 Corollary 2.2; `GB1.md` Theorems 5.2, 6.1, 5U exist as cited. The two Peter-Weyl notes and the MDTN note were not read by the referee; the file uses them as context only. |
| 6 | §1.1 `S³`, `g`, Haar (23) | CORRECT | |
| 7 | §1.1 `𝓗_k`, `H_k`, flux (25) | CORRECT | |
| 8 | §1.1 `L_{μν}`, `J`, `K`, `N^±` (26) | CORRECT | Referee computation: left multiplication by `e^{iεσ_3/2}` moves `x` along the field `−(ε/2)(D_{12}+D_{34}) = −iεN^+_3`; right multiplication gives `+iεN^-_3`. So `N^+` is left and `N^-` right, as stated. Not load-bearing. |
| 9 | §1.1 `E²`, link matrix `U`, density (27-30) | CORRECT | Density of `⊕_k H_k` is cited ("Peter-Weyl ... not rebuilt"). Referee closure R2 (section 2) rebuilds it from Lemma 4.1(a) and Stone-Weierstrass. |
| 10 | §1.2 `R_s`, `x^±_μ`, `y_k`, `P_μ`, `U_s` (34-40) | CORRECT | `Σ_{k≤s}(k+1)² = (s+1)(s+2)(2s+3)/6` checked. |
| 11 | §1.2 `so(5)` identification and credit (42) | CORRECT | The Chandrasekharan-Wiese identification is context; no proof uses it. |
| 12 | §1.3 tiling, `X_p`, `B_p`, `B_C` (46-48) | CORRECT | With `U_{(x,y)} ↦ h_yUh_x^{-1}`: `U_4^*U_3^*U_2U_1 ↦ h_{x_0}X_ph_{x_0}^{-1}`. For `SU(2)` links `tr X_p` is real, so on `𝒦` `B_p = 2 tr X_p`; this is used in R1. |
| 13 | GAP (draft plaquette ordering) (50) | CORRECT; gap real | Draft line 116: "`X_p = U_{ℓ_1} U_{ℓ_2} U_{ℓ_3}^* U_{ℓ_4}^*`". Draft line 320: "`U_ℓ ↦ h_y U_ℓ h_x^{−1}`". Under these the draft trace is not invariant. The counterexample was recomputed: `iσ_1·1·(−iσ_1)·1 = 1` (trace 2); after `h = iσ_2` at the shared vertex, `(iσ_3)(−iσ_2)(−iσ_1) = −1` (trace −2). The corrected order is gauge covariant (item 12). Lemma 4.7 uses only "four distinct links, each factor `U` or `U^*`", so every later bound survives unchanged. |
| 14 | §1.3 the two ticks (52) | CORRECT | The infinite products are defined on local operators by Lemma 4.5(b). |
| 15 | §1.4 `ι`, `ι_Λ`, framework observable (56) | CORRECT | |
| 16 | §1.4 `F_M(Λ)`, `Π^Λ_M` (58) | CORRECT | |
| 17 | §1.4 class `S_M(Λ)` (60) | CORRECT | |
| 18 | §1.4 class `E_e(Λ)` and remark (61-63) | CORRECT | `E_e` is a class of Kogut-Susskind states; Corollary 4.9(b) covers framework states with the same bound. |
| 19 | §1.5 `d`-flux-bounded, examples (68) | CORRECT | For products the `d`'s add. |
| 20 | Definition `L5[SU(2), s]` (70-75) | CORRECT | Item 3 checked: `x^±_μ` and `Y_s` commute with `SO(4)` up to the vector action, so `U_s` transforms like `U`. Tests: items 82-83. |
| 21 | Lemma 4.1(a) (85, 101) | CORRECT | `Δ(\|x\|²q) = (4d+8)q` for harmonic `q` of degree `d`. |
| 22 | Lemma 4.1(b) (87, 103) | CORRECT | `Σ x_μ∂_νx_ν∂_μ = 𝔈²+3𝔈` rechecked via `𝔈∂_μ = ∂_μ(𝔈−1)`. |
| 23 | Lemma 4.1(c) (89, 105) | CORRECT | |
| 24 | Lemma 4.1(d) (91, 107) | CORRECT | |
| 25 | Lemma 4.1(e) (93, 109) | CORRECT | `(k+4) − k/(k+1) = (k+2)²/(k+1)`; `a_k + b_k = 1` matches `Σx_μ² = 1`. |
| 26 | Lemma 4.1(f) (95, 111) | CORRECT | |
| 27 | Lemma 4.1(g) (97, 113) | CORRECT | |
| 28 | Lemma 4.1(h) (99, 115) | CORRECT | |
| 29 | Proposition 4.2(a) (123, 131) | CORRECT | |
| 30 | Proposition 4.2(b) (125, 133) | CORRECT | The `so(5)` relations of `−i(x_a∂_b − x_b∂_a)` rederived; the `H_k → H_{k−2}` part vanishes because partial derivatives commute. |
| 31 | Proposition 4.2(c) (127, 135) | CORRECT | Numerator identity `(k+2)(S−k²−3k) + k(S−k²−k+2) = (2k+2)(S−k(k+2))` checked, `S = s(s+3)`. |
| 32 | Proposition 4.2(d) (129, 137) | CORRECT | `T² = (N^-)² − T`; eigenvalues `k/2`, `−(k+2)/2`; top eigenvalue of `U_s^*U_s` on `C²⊗H_k` is `(S − k² − k + 2)/S ≤ 1`. |
| 33 | Paragraph after 4.2 (139) | CORRECT | "Lemma 4.1(b) on `R⁵`" means the same computation in five variables, `Σ D² = \|x\|²Δ − 𝔈(𝔈+3)`; not used. |
| 34 | Lemma 4.3 (145-155) | CORRECT | Step 2 silently uses `U^-Π_0 = 0` (`x^-_μ` kills `H_0`); without it the `H_0` part of `(Y'_s − 1)v` would enter with weight 1. Add the clause. |
| 35 | Remark 4.4(i) (157) | CORRECT | `P_μ = Π_{≤1}x_μΠ_{≤1}` at `s = 1` checked. The identifications with the Ludwig-Jakobs-Urbach link and the MDTN note are context and were not checked. |
| 36 | Remark 4.4(ii) (157) | CORRECT | For `Q_μ` the weights are `z_k = 1` (`k < s`), so the `H_1` part of `[Q_μ, Q_ν]` is `(z_1² − z_0²)(…) = 0`. |
| 37 | Remark 4.6 (159) | CORRECT | Proved at operator level. Referee closure R1 (section 2) adds the correlator-level statement: Theorem 4.8(b) fails at top flux by at least `0.9θ²`, for every `s`. |
| 38 | Lemma 4.5(a) (165) | CORRECT | A box of side `L` has `3L(L+1)²` links. |
| 39 | Lemma 4.5(b) (167) | CORRECT | |
| 40 | Lemma 4.5(c) and finite-depth paragraph (169-173) | CORRECT | A periodic box must also carry the cube tiling of `GB1.md` Definition 5. |
| 41 | Embedded framework gates (175) | CORRECT | |
| 42 | Lemma 4.7, plaquette step (185) | CORRECT | |
| 43 | Lemma 4.7(a) (179, 187) | CORRECT | |
| 44 | Lemma 4.7(b) (181, 189) | CORRECT | Matches `GB1.md` line 113: "Telescoping unitary-gate compressions gives `‖∏_Cg_CP_C−∏_CA_C‖≤N_Ct_K`". |
| 45 | Lemma 4.7(c) (183, 191) | CORRECT | |
| 46 | Theorem 4.8(a) (199, 213-217) | CORRECT | Leak induction and one-tick split checked; `Σ_i` gives exactly `ε_n`. |
| 47 | Theorem 4.8(b) (201-205, 219) | CORRECT | Matched on `Λ_T` implies matched on `Λ_n ⊆ Λ_T` (partial trace keeps `F_M`), so "for all `n ≤ T`" holds. |
| 48 | Theorem 4.8(c) (207-211, 221) | CORRECT | Stirling step and `δ_s(M') ≤ 2(M'+3)²/s²` checked. |
| 49 | Pass-1 check note (223) | CORRECT as a report | Not reproduced by pass 2 or by the referee; guides only. |
| 50 | What Theorem 4.8 does not say (225) | CORRECT | |
| 51 | Corollary 4.9(a) (231-233, 239) | CORRECT | Markov bound, union bound for commuting projections, `‖ρ − ΠρΠ‖_1 ≤ 2√η'` by Cauchy-Schwarz, normalization cost `η'`. |
| 52 | Corollary 4.9(b) (235) | CORRECT | |
| 53 | Corollary 4.9(c) (237) | CORRECT | `δ_s ~ M²/s²` and `√η ~ M^{-1}` balance at `M = s^{2/3}`. |
| 54 | Corollary 4.10, facts (R1), (R2) (253) | CORRECT | (R1) needs the split `φ = Π_{M'}φ + r` first and then Theorem 4.8(a) on `Π_{M'}φ`; running the telescope on `φ` itself gives `2n‖r‖`. Say so. |
| 55 | Corollary 4.10(a) (247-249) | CORRECT | The chain `ε̂`, `ε̂ + Gt_K`, `2ε̂ + 3Gt_K`, `3ε̂ + 7Gt_K` rechecked; every cutoff is at most `M̂`. |
| 56 | Corollary 4.10(b) (251) | CORRECT | The proof gives `4G_nt_K`, below the stated `6G_nt_K`; the hypothesis `M + nK + 1 ≤ s` can be `M + nK ≤ s`. |

| 57 | §2 4.11 lead-in (261) | ERROR | "its four tests are in section 6". In `GB1QL.md` the tests are in section 4; section 6 is the draft's numbering. Fix: "section 4". |
| 58 | Proposition 4.11(a) (265, 267) | CORRECT | The doublet action is the second quantization of `h_x`; the link action is the `S³` rotation. Both commute with every gate. |
| 59 | Proposition 4.11(b) | CORRECT | `JU_sJ^{-1} = P_4 − iP·σ = U_s^*` as an operator matrix, and `U^*` transforms as `h_xU^*h_y^{-1}`. |
| 60 | Proposition 4.11(c) | CORRECT | `GB1_REFEREE.md` line 171 proves Theorem 5M(1) from: hops even and in one edge triple; A2's signs "act on all flavours alike"; `GA1_5.md` Lemma U, "which holds for five-mode sites and any finite registers"; Proposition C. Each holds for `L5[SU(2), s]`, with (b) for reversed links. The quoted phrase is the words of 5M's proof, as "its citation" says, not of `GA1_5.md` line 236. |
| 61 | Proposition 4.11(d) | CORRECT | Every term of `h_ℓ` contains `d_x` or `d_y` on the right, so it kills the matter vacuum. |
| 62 | Paragraph after 4.11 (269) | CORRECT | |
| 63 | 4.12 (U1) (275) | CORRECT | `GB1.md` lines 121-123 checked. |
| 64 | 4.12 (U2) (276) | CORRECT | Quotes match `LW1_5_DRAFT.md` lines 316 and 318, `TOE_ASSEMBLY.md` line 252 (section 3.9), and `GB1.md` line 165 ("rung \(n\ge1\) supplies no \(\mathbb C^2\) or spin-\(S\) coarse register"). What is proved: no member of `L5-U` has an `SU(2)` block register of dimension above `C(4, 2) = 6`. |
| 65 | (U3a), (U3b) (278) | CORRECT | `Λ²(C²⊗C²)` has dimension `6 = 3·1 + 1·3`. Named, not attempted. |
| 66 | Proposition 4.12(i) (280-284) | CORRECT | |
| 67 | Proposition 4.12(ii) | CORRECT | `(N−1)² = 1 − [N=1]`, `E² = (3/4)[N=1]`. |
| 68 | Paragraph after 4.12 (286) | CORRECT | Coefficient `−(4/3)τ_E` checked. |
| 69 | `L5-O` paragraph (288) | CORRECT | `LW1_5_DRAFT.md` line 305, `GA2_Y2_DRAFT.md` line 144 ("one law has one register") and `GB1.md` Lemma O2 (line 157) checked. |
| 70 | §3 lead-in (292) | ERROR | "quoted in section 0". `GB1QL.md` section 0 quotes nothing; the quote is in the draft, line 38. Fix: insert the quote of `GA2_Y2_DRAFT.md` line 211 (its text is checked equal in section 3.2 below). |
| 71 | (H-G) row (296) | CORRECT | The distiller's change from the draft's "the exact gauge group" (draft line 355) is right: the spectator modes enter no gate, so every even unitary on their Fock factor at a site commutes with the tick. |
| 72 | (H-GI) row (297) and distiller GAP (7) | CORRECT; gap real | Draft line 356: "Delivered ... The Gauss action is exact on both sides, and `ι` intertwines it". That is a fact about the dynamics on slice Hilbert spaces, not about a measure `μ`. The label "Conditional only" names no condition. Fix in section 3.2. |
| 73 | (H-Haar) row (298) | ERROR | Decision "Delivered approximately". The hypothesis is on `μ` ("`G`-valued links ... with Haar reference measure"), and the row's own reason says "This is not ... a four-dimensional Haar-reference measure". Same conflation as item 72. Fix in section 3.2; the reason text stands. |
| 74 | (H-4D) row (299) | ERROR (one clause) | "This is the first missing structural input in the draft's hand-off order." In that order (H-GI), line 297, comes first and, after the distiller's own repair, is not delivered. The decision "Not delivered" and its reason are right (`GB1.md` Theorem 2.1, line 43: "A positive unitary is the identity"). Fix: (H-4D) is the first missing input in dependency order (section 3.2). |
| 75 | (H-RP) row (300) | CORRECT | `GB1.md` line 208 checked. |
| 76 | (H-class) row (301) | CORRECT | |
| 77 | Uniformity row (302) | CORRECT | |
| 78 | T0-rate row (303) | CORRECT | |
| 79 | "The answer, exactly" (305) | INCOMPLETE | "The draft names (H-4D) as the first missing structural input" reports the draft and does not decide. The decision is in section 3.2. |
| 80 | Relation to the other requests (307) | CORRECT | `GA2_Y2.md` line 178 contains "**T0-QLR[G]** and **T0-D[G]** ask respectively for a controlled joint quantum-link/register limit"; `GB1.md` line 206 (row H1b) checked. |
| 81 | §4 four-test quote (311) | CORRECT | `LW1_5_DRAFT.md` line 328 checked. |
| 82 | R-QL5 and its tests (315) | CORRECT | 1 C, 2 P, 3 P, 4 C agreed. |
| 83 | R-QLC and its tests (316) | CORRECT | Test 1 passes because the brief hands the state class to the lane: "in a class of states you state" (draft line 30). Add that reason; otherwise the matched classes could read as fixing the target. |
| 84 | R-FORM row (317) | CORRECT | `GB1.md` lines 221 and 227 checked. |
| 85 | Closing paragraph of §4 (319) | CORRECT | |
| 86 | §5 check record (324) | CORRECT as a report | `s(s+3) = 4, 10, 18` at `s = 1, 2, 3`. |
| 87 | §5 scope (326) | CORRECT | |

**Counts.** 87 items: 82 CORRECT, 4 ERROR (57, 70, 73, 74), 1 INCOMPLETE (79). No ERROR or INCOMPLETE item touches a theorem of section 2. All four ERRORs are a cross-reference or a decision label.

---

## 2. Referee closures

### R1. The correlator comparison fails at top flux, for every `s` (extends Remark 4.6)

Remark 4.6 proves its claim at operator level: "No bound of Lemma 4.3's form that tends to zero as `s → ∞` holds uniformly on `R_s`." The title says more, "the flux restriction cannot be removed". The following closes the gap at the level of Theorem 4.8(b), at one tick.

**Claim R1.** Fix `s ≥ 1`, any `τ_E`, and `0 < |θ| ≤ 1/300`. Let `ℓ` be a link, `C` its tiling cube, `X = {ℓ}`, and `A = 1 − Π^ℓ_{≤s}`, the projection onto flux above `s` on `ℓ`. `A` is a function of `E²_ℓ`, so it is gauge invariant, `0`-flux-bounded, and `‖A‖ = 1`. Let `ψ_s` be the product vector with a unit `h ∈ H_s` on `ℓ` and the constant `1 ∈ H_0` on every other link of `Λ_1`, and let `ω_s`, `ω` be the vector states of `ψ_s` and `ψ = ι_Λψ_s`. They are matched at flux `s`. Then

`ω_s(α_s(ι_X^*Aι_X)) = 0` and `ω(α(A)) ≥ 0.9 θ²`.

So the error of Theorem 4.8(b) at `n = 1`, `M = s` is at least `0.9θ²`, for every `s`.

*Proof.*
1. `A` vanishes on `ran ι`, so `ι_X^*Aι_X = 0`.
2. `ψ` is an eigenvector of every `E²_{ℓ'}`, so `W_E ψ` is a phase times `ψ`. Gates of cubes other than `C` are unitary and commute with `A`. So `ω(α(A)) = ‖A g_C ψ‖²`.
3. Write `g_C = 1 − iθB_C + R`. With `‖B_C‖ ≤ 24` and `x = 24|θ| ≤ 0.08`, `‖R‖ ≤ e^x − 1 − x ≤ (x²/2)e^x ≤ 312θ²`. Since `Aψ = 0`, `‖Ag_Cψ‖ ≥ |θ|‖AB_Cψ‖ − 312θ²`.
4. A face of `C` that misses `ℓ` does not change the flux on `ℓ`, so it contributes nothing to `AB_Cψ`. The link `ℓ` lies in exactly two faces `p, p'` of `C`, which share no other link.
5. For `SU(2)` links, `tr X_p` is multiplication by a real function, so `B_p = 2 tr X_p` on `𝒦`. Move the factor of `ℓ` to the right end by cyclicity of the trace. Then `A tr X_p ψ = F_p := tr(Â G)`, where `Â` is the product of the other three link matrices or their adjoints (each a function of one link, of flux exactly one there), and `G = Σ_μ x^+_μh ⊗ e_μ` or `Σ_μ x^+_μh ⊗ e_μ^*` by the orientation of `ℓ` in `p`.
6. Haar orthogonality, rebuilt: on `S³`, `∫x_μx_ν dσ = δ_{μν}/4` (reflection and permutation symmetry, `Σx_μ² = 1`). With `Σ_μ (e_μ)_{cd}\overline{(e_μ)_{ab}} = 2δ_{ac}δ_{bd}` (the `e_μ/√2` are an orthonormal basis of `M_2(C)` up to phases), `∫\overline{g_{ab}}g_{cd} dσ = δ_{ac}δ_{bd}/2`, and the same for `g^*`. Write `Â = B_1 g B_2` with `g` (or `g^*`) one of its three factors and `B_1, B_2` the unitary products of the others. Integrating over that one link gives `∫\overline{Â_{ba}}Â_{dc} = (B_1B_1^*)_{db}(B_2^*B_2)_{ac}/2 = δ_{bd}δ_{ac}/2` pointwise in the other two links; Fubini applies because all entries are bounded. This gives `‖F_p‖² = ½ Σ_{ab}‖G_{ab}‖² = ½ Σ_{μν}⟨x^+_μh, x^+_νh⟩ tr(e_μ^*e_ν) = Σ_μ‖x^+_μh‖² = a_s`, by Lemma 4.1(d), (e).
7. `F_p` has flux one on the links of `p` other than `ℓ` and flux zero on those of `p'`; `F_{p'}` the reverse. So they are orthogonal, and `‖AB_Cψ‖² = 4a_s + 4a_s = 8a_s > 4`.
8. Hence `‖Ag_Cψ‖ ≥ 2|θ| − 312θ² ≥ 0.96|θ|` for `|θ| ≤ 1/300`, and `ω(α(A)) ≥ 0.92θ²`. □

`[check]` (`/tmp/toe-GB1QLref/check_r1.py`, Monte Carlo, `2·10^5` samples, 0.5 s, 200 MB peak): `E|F_p|² / (a_s E|h|²) = 1.0013, 1.0009, 1.0001, 1.0039` at `s = 1, 2, 3, 5`, with `h = (x_4 + ix_3)^s`. It agrees with step 6 and proves nothing.

**What R1 changes.** Nothing in Theorem 4.8; its hypothesis `M + nK ≤ s` with `ε_n → 0` already forces `M ≪ s`. R1 shows that this is needed even at one tick and for a gauge-invariant `0`-flux-bounded observable. It also backs the (H-Haar) row's last sentence ("Remark 4.6 rules out this flux-uniform approximation") at correlator level.

### R2. Density of `⊕_k H_k`, rebuilt (replaces the Peter-Weyl citation at line 30)

**Claim R2.** The algebraic sum `𝒫 = Σ_k H_k` is dense in `𝒦 = L²(S³, σ)`. Hence `𝒦 = ⊕̂_k H_k` (orthogonal by Lemma 4.1(c)), and `E² = Σ_k (k(k+2)/4)Π_k` is self-adjoint on its natural domain.

*Proof.* `H_0` holds the constants. By Lemma 4.1(a), `x_μ H_k ⊆ H_{k+1} + H_{k−1}` on `S³`, so `𝒫` is closed under multiplication by each `x_μ`. By induction on degree, `𝒫` contains the restriction of every complex polynomial. These restrictions form a unital algebra that separates points of `S³` and is closed under complex conjugation, so by Stone-Weierstrass they are dense in `C(S³)` in the sup norm. Sup-norm convergence implies `L²(σ)` convergence for the probability measure `σ`, and `C(S³)` is dense in `L²(σ)` for a finite Borel measure on a compact metric space. □

This removes the only cited, non-rebuilt lemma in section 2 of `GB1QL.md`.

---

## 3. The distiller's GAPs

### 3.1 GAP (draft plaquette ordering), line 50: real; the repair is correct

The draft (line 116) writes "`X_p = U_{ℓ_1} U_{ℓ_2} U_{ℓ_3}^* U_{ℓ_4}^*`" and (line 320) "`U_ℓ ↦ h_y U_ℓ h_x^{−1}`". Take a face with corners `x_0 → x_1 = x_0+e_i → x_2 = x_0+e_i+e_j → x_3 = x_0+e_j → x_0`, so `ℓ_1, ℓ_2` are traversed forward and `ℓ_3 = (x_3, x_2)`, `ℓ_4 = (x_0, x_3)` backward. The draft product picks up `h_{x_0}^{-1}h_{x_2}` between its first two factors, and these do not cancel. The distiller's counterexample is right (item 13). The repaired product `U_4^*U_3^*U_2U_1` transforms by `h_{x_0}(·)h_{x_0}^{-1}`, so its trace is invariant.

What the error touched. The comparison bounds (Lemma 4.7 onward) use only that a face has four distinct links, each entering once as `U` or `U^*`. They hold for either order. Gauge invariance does depend on the order: Proposition 4.11(a) ("`tr X_p` is invariant by cyclicity", draft line 326) and the name "Kogut-Susskind" for the target tick. With the draft order, the target would not be gauge invariant, and "gauge-invariant correlators" would compare non-invariant dynamics. With the repaired order, every lemma, proposition, theorem, corollary and remark of `GB1QL.md` section 2 holds as written (items 21-69; item 57 is a cross-reference only).

### 3.2 GAP (T0 hand-off conflation), lines 7 and 297: real; repaired statement

The start class, quoted. `GA2_Y2_DRAFT.md` line 211: "every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4`, with Haar reference measure and density in `𝒜_{k_0}(g)` for some `g ≤ g_*`". The draft's line 38 quotes the same sentence `[check: string comparison, 387 characters, equal]`.

**Lemma H (dependency order).** In this sentence, (H-GI), (H-RP), (H-Haar) and (H-class) are properties of one object, the measure `μ` that (H-4D) asks for. (H-G) fixes the group. So a hand-off that supplies no `μ` supplies none of the four properties, and the first input it lacks, after (H-G), is (H-4D).

*Proof.* Read the quoted noun phrase. "gauge-invariant" and "reflection-positive" modify "probability measure `μ`"; "with Haar reference measure" and "density in `𝒜_{k_0}(g)`" are attached to `μ`; "on `G`-valued links of `a_{k_0}Z^4`" names its configuration space. A property of `μ` is decided only once `μ` is given. □

**Decision on the draft's claim.** (H-4D) is the first missing input, in dependency order. It is not first in the draft's table order once (H-GI) is corrected, because (H-GI) is listed before it. The draft's "This is the first hypothesis that fails" (draft line 358) was consistent only with its false (H-GI) row; Lemma H gives the conclusion a correct reason.

**Repaired hand-off table** (replaces `GB1QL.md` lines 294-303; reasons not shown are unchanged):

| Hypothesis of T0-start[SU(2)] | Decision | Reason |
|---|---|---|
| (H-G) `G = SU(2)`, acting locally | Delivered in the test law | Line 296 unchanged. |
| (H-4D) a probability measure `μ` on `G`-valued links of `a_{k_0}Z⁴` | **Not delivered. The first missing input (Lemma H).** | Line 299's reason unchanged. |
| (H-GI) `μ` gauge invariant | Not delivered; a property of the missing `μ` | Proved instead, at slice level: both ticks commute with the gauge action, `ι` intertwines it, and `ι^*Aι` is gauge invariant when `A` is. The classes `S_M`, `E_e` admit non-invariant states. |
| (H-Haar) `μ` has Haar reference measure | Not delivered; a property of the missing `μ` | Slice analogue proved: each target link space is `L²(SU(2), Haar)`, and over one time slice their tensor product is T0's `H_W = ⊗_b L²(SU(2))` (`GA2_Y2.md` line 63, Corollary Y2-0(ii)). Correlators approach it at `O((log s)⁴/s²)` on `S_M` and `O(s^{−2/3})` on `E_e`, at fixed support, ticks and bound. Remark 4.6 and R1 exclude a flux-uniform version. |
| (H-RP) | Not delivered; a property of the missing `μ` | Line 300 unchanged. |
| (H-class) | Not delivered; a property of the missing `μ` | Line 301 unchanged. |
| Uniformity in `a`, `L` | Not a hypothesis on `μ` | It sits in T0-start's conclusion (i). Line 302 correctly records GB1-QL's own uniformity: volume yes; `a`, ticks, flux no. |
| T0-rate | Not delivered | Line 303 unchanged. |

**Repaired "The answer, exactly"** (replaces line 305): "GB1-QL delivers (H-G) in the named test law. The hand-off fails first at (H-4D): no probability measure on links of a four-dimensional lattice is constructed. (H-GI), (H-Haar), (H-RP) and (H-class) are properties of that measure and are not delivered. GB1-QL delivers slice-level analogues of two of them: gauge-covariant ticks with an equivariant comparison map, and the approach of framework correlators to the Kogut-Susskind slice space `L²(SU(2), Haar)`, with rates, for local observables, uniformly in volume and in ticks up to a stated time, on states of bounded flux or bounded local electric energy. The `a`-uniformity and T0-rate are not delivered."

---

## 4. Required edits to `GB1QL.md`

Draft and distilled constants agree: `ε_n`, `δ_s`, `η`, `M̂`, `4ε̂ + 7Gt_K`, `2rδ_s(M+nK)`, `K + 1 ≥ 24e³|θ|` and `‖B̃_C‖ ≤ 24` each occur in both texts with the same wording `[check: string search]`.

- **E1** (line 261, item 57). "its four tests are in section 6" becomes "its four tests are in section 4".
- **E2** (line 292, item 70). Replace "quoted in section 0" with the quote itself: the sentence of `GA2_Y2_DRAFT.md` line 211 that the draft quotes at its line 38.
- **E3** (lines 294-303, items 72-74). Replace the hand-off table with the repaired table of section 3.2. Add Lemma H, marked "(referee closure, `GB1QL_REFEREE.md`)".
- **E4** (line 305, item 79). Replace "The answer, exactly" with the repaired text of section 3.2.
- **E5** (lines 7 and 9, item 3). In the GAP summary add: "(H-4D) is the first missing input in dependency order (Lemma H)". In "Open by name" write: "T0-start[SU(2)]: (H-4D) first; (H-GI), (H-Haar), (H-RP) and (H-class) as properties of the missing measure".
- **E6** (line 30, item 9). Replace "(Peter-Weyl for `SU(2)`; standard, not rebuilt)" with referee closure R2.
- **E7** (after line 159, item 37). Add referee closure R1 after Remark 4.6, marked "(referee closure, `GB1QL_REFEREE.md`)".
- **E8** (Lemma 4.3, Step 2, item 34). After "By Step 1 its norm is at most" insert "(using `U^-Π_0 = 0`)".
- **E9** (Corollary 4.10, fact (R1), item 54). State the proof: apply Theorem 4.8(a) to `Π_{M'}φ`, and bound `(W̃ − W)(1 − Π_{M'})φ` by `2‖(1 − Π_{M'})φ‖`.
- **E10** (line 316, item 83). In R-QLC's reason (1) add: "the brief hands the class of states to the lane ('in a class of states you state')".

Optional, no verdict depends on them: Corollary 4.10(b) may state `4G_nt_K` and the hypothesis `M + nK ≤ s` (item 56); Lemma 4.5 may say "every periodic box that carries the cube tiling" (item 40).

## 5. Open statements to carry by name

These are the open items of `GB1QL.md` line 9, with the T0-start item reordered by Lemma H. The referee adds none.

- **GB1-QL[`L5-O`]**: whether an `so(20)` register family realises `R_s` in an `SU(2)` block of `L5-O`, with a class on which that block evolves on its own.
- **GB1-QL[matter]**: the comparison with matter present.
- **GB1-QL[U(2)]**, with **U3a** (`U(2)` to `SU(2)`) and **U3b** (the electric layer), on any route that supplies a growing `U(2)` block register.
- **E-1, E-2, E-3** of `GB1.md`; **GB1-CF**; the time continuum; **GB1-SC**; **VC1**.
- **T0-start[SU(2)]**: (H-4D) first; then (H-GI), (H-Haar), (H-RP), (H-class).
- **T0-rate**; **T0-QLR[SU(2)]** beyond its finite-time Hamiltonian regulator part.
- **Y2-W** for the fixed register.

## 6. Freeze recommendation

**Freeze `GB1QL.md` after edits E1-E10.** No theorem of section 2 changes. Four items are ERRORs (two cross-references and two decision labels in the hand-off table), and one is INCOMPLETE (the summary of the hand-off). Each is fixed by a local edit above.

At freeze, record:
- Lemma 4.1, Proposition 4.2, Lemma 4.3, Lemmas 4.5 and 4.7, Theorem 4.8, Corollaries 4.9 and 4.10, and Propositions 4.11 and 4.12 are proved, on the definitions of section 1. Those definitions are the distiller's and are not adopted.
- Referee closures R1, R2 and Lemma H have had this one check only. Mark them so.
- `L5[SU(2), s]`, R-QL5 and R-QLC stay proposed. Only the owner adopts.

---

## 7. Prior work used

Each prior result below was used or checked against, at `022ea74a0`, in this folder.

- `GB1.md` Theorem 5.2 and its leak step, line 113 ("Telescoping unitary-gate compressions gives ..."), from `GB1_REFEREE.md`: compared with Lemma 4.7(b) (item 44).
- `GB1.md` Theorem 2.1 (F1-F2), line 43: the reason in the (H-4D) row (item 74).
- `GB1.md` Theorem 6.1 (lines 121-123), Lemma O2 (line 157), lines 165 and 182, §8 rows H1a, H1b, H3 (lines 205, 206, 208), and the readings rows (lines 221, 227): quotations checked (items 63-69, 71, 75, 80, 84).
- `GB1_REFEREE.md` line 171, the proof of Theorem 5M(1): the basis of Proposition 4.11(c) (item 60).
- `GA1_5.md` Lemma U (line 236) and Proposition C (line 264): named by that proof; read only to locate them.
- `GA2_Y2.md` Theorem 2.1 (N) and Corollary 2.2 (lines 39, 43), Corollary Y2-0(ii) (line 63), and lines 166 and 178.
- `GA2_Y2_DRAFT.md` line 144 ((a1), "one law has one register") and line 211 (T0-start[G]): Lemma H rests on the latter's wording.
- `LW1_5_DRAFT.md` lines 305, 316, 318, 328; `TOE_ASSEMBLY.md` line 252 (section 3.9, ZM1-INV); `LIT_QLM.md` line 23.

**Prior work the digest missed.** `prior/GB1QL.md` does not name three inputs that `GB1QL.md` relies on. (1) `GA2_Y2.md` Corollary Y2-0(ii), line 63: "Let \(H_W=\bigotimes_b L^2(SU(2))\) be T0's slice space"; this is the object of the (H-Haar) row. (2) The proof of `GB1.md` Theorem 5M(1) in `GB1_REFEREE.md` line 171, which Proposition 4.11(c) ports. (3) `GA1_5.md` Lemma U and Proposition C, on which that proof rests.

## 0.1 Sources read, by line

All at `022ea74a0` in this checkout; no other branch was fetched.
- `GB1QL.md`: lines 1-326 (all).
- `GB1QL_DRAFT.md`: lines 28-39 (its section 0), and the grep hits at lines 18, 42, 116, 315, 320, 326, 349, 355-358, 364, 368, 370, 380, 399, 416, 427, 432.
- `prior/GB1QL.md`: lines 1-86 (all). `LW1_REFEREE.md`: lines 1-80. `Y2W_DRAFT.md`: lines 1-30.
- `GB1.md`: lines 9, 11, 29, 43, 81, 97, 103, 105, 113, 115, 121, 123, 139, 157, 159, 165, 167-171, 182, 186, 193, 205-208, 221, 226-227.
- `GB1_REFEREE.md`: lines 165-171, 191, 212, 218, 226, 241.
- `GA1_5.md`: lines 236 and 264 (first 400 characters).
- `GA2_Y2.md`: lines 14, 18, 39, 43, 59, 63, 65, 166, 178.
- `GA2_Y2_DRAFT.md`: lines 144, 205-215.
- `LW1_5_DRAFT.md`: lines 305, 316, 318, 328.
- `TOE_ASSEMBLY.md`: lines 183, 214, 248, 252, 449, 610, 726.
- `LIT_QLM.md`: line 23.

Not read: the MDTN note, the two Peter-Weyl notes on `main`, and the literature that `GB1QL.md` cites. `GB1QL.md` uses them as context only. R2 removes the one place where a cited result entered a definition.

---

## FINISH

**Proved.**
- Every lemma, proposition, theorem, corollary and remark of `GB1QL.md` section 2 holds as written, with the repaired plaquette order that the file already uses. This covers the harmonic identities of Lemma 4.1 and the `so(5)` quantum link of Proposition 4.2 (relations, Casimir `s(s+3)`, `‖U_s‖ ≤ 1`). It also covers Lemmas 4.3, 4.5 and 4.7; Theorem 4.8, with rate `O((log s)⁴/s²)` for bounded flux; Corollary 4.9, with rate `O(s^{−2/3})` for bounded local electric energy; and Corollary 4.10 for two-time correlators and loops. All bounds are uniform in the volume, for a fixed number of ticks.
- Propositions 4.11 (a)-(d) and 4.12 hold. The `L5-U` route fails at (U2): no member of `L5-U` has an `SU(2)` block register of dimension above 6.
- Referee closure R1: at top flux the comparison misses by at least `0.9θ²` at one tick, for every `s` and `0 < |θ| ≤ 1/300`. So the flux bound cannot be removed at correlator level either.
- Referee closure R2: `⊕_k H_k` is dense in `L²(S³)`, by Lemma 4.1(a) and Stone-Weierstrass, without Peter-Weyl.
- Lemma H: (H-4D) is the first missing input of the T0-start hand-off, in dependency order. (H-GI), (H-Haar), (H-RP) and (H-class) are properties of the measure it asks for.

**Counterexamples.**
- The draft's plaquette order is not gauge invariant: one vertex rotation takes the trace from 2 to −2 (distiller's example, recomputed).
- R1 refutes Theorem 4.8(b) without the flux restriction (`M = s`).
- Line 299's clause "the first missing structural input in the draft's hand-off order" is false as worded: in that order (H-GI) comes first and is not delivered.

**Open by name.** GB1-QL[`L5-O`]; GB1-QL[matter]; GB1-QL[U(2)] with U3a and U3b; E-1, E-2, E-3; GB1-CF; the time continuum; GB1-SC; VC1; T0-start[SU(2)] ((H-4D) first, then (H-GI), (H-Haar), (H-RP), (H-class)); T0-rate; T0-QLR[SU(2)] beyond its finite-time Hamiltonian regulator part; Y2-W for the fixed register. All are carried from `GB1QL.md`; none is new here.

**What changes downstream.**
- GB1, `SU(2)` rung: after edits E1-E10 and freeze, the rung has a theorem for the named test law `L5[SU(2), s]` on states with empty matter. It answers GB1-QL only if the owner adopts R-QL5 and R-QLC. The `L5-U` route stops at (U2).
- GA2 Y2 and T0-start[SU(2)]: the hand-off fails first at (H-4D). The slice-level analogues of (H-GI) and (H-Haar) are available to a later measure construction.
- T0-QLR[SU(2)]: its TOE-side regulator-error part now exists in Hamiltonian, finite-time form, for bounded flux or bounded local electric energy. R1 shows it cannot be made uniform in flux.
- Y2-W: unchanged.
