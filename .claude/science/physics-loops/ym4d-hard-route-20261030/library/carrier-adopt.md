lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T03:36Z

# carrier-adopt: check of `inv-root.md`, and adoption of its expansion as the stored carrier series

Queue row 167. Pinned at branch head de1534ccd (claude/ym4d-hard-route).
Written by Claude (Opus 5.5, max), on the Mac mini. Research-stage working state; no status.

Moves: rank 6 (2.13's stored cut, (4.1) of `sa-2.13-2.md`) and C4 (the order of constants).

Status of this file: in progress. Sections are written in order.

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, branch head `de1534ccd`. One reading by the other model. Research text, not an audit, no status. The outline was fetched by URL into a private scratch folder; its SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` matches the pin `31a47c543775`. Balaban's CMP 99 (389-434) OCR was read in `~/ym4d-papers/`. No numeric job was run; every step below is a written inequality.

Credits. Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the operation of SA 17520-17564, the walk conventions of SA 10208-10338, the UM Gaussian of SA 14097-14205 and the witness of SA 18300-18330. OpenAI Codex for `library/inv-root.md`, `um-envelope.md`, `sa-2.13-2.md` and the h-walk gates. Claude for `h-walk.md` and `h-walk-fix.md`. Tadeusz Balaban for the random-walk expansion of propagators, CMP 99 (1985) 389-434, Theorem 3.7 and Corollary 3.8, (3.90)-(3.94), pp. 409-410: one factor O(M^{-1/2}) per walk step, decay in the walk distance (3.93). I confirmed these lines in the OCR. They are the model for the outline's statement 5.

## 1. Check of `library/inv-root.md` (Codex)

**Checked line by line by Claude, first failing step none.** Each section is a valid implication from its named inputs. The inputs stay premises: the repaired A2 bounds (`a2-full.md` Theorems I-II and Lemma 5.1, as repaired in `gates/a2-full-gate.md`) and h-walk Theorem H (H1)-(H2) with the repaired count, collar and full read hull (`gates/h-walk-gate.md` Sections 8-9; `gates/h-walk-fix-gate.md` items 1, 4, 5; `h-walk-fix.md` Lemma N(d)).

| Section | Verdict | What I redid |
|---|---|---|
| 1, check of um-envelope 4-5 | ADVANCE | Each bullet; details below. This is the first other-model reading of um-envelope Sections 4-5. |
| 2, (11)-(12) | ADVANCE | Every admitted tree of (H2) is within R_h of the read hull, so l_ω ≤ d_B(ω;x,y). With η ≤ δ_h/2, e^{η l_ω}\|A_ω(x,y)\| ≤ C_h (C_h M_1^{-1/3})^m e^{-δ_h\|x-y\|/2}. The (H1) count C_h^m and the bounded number of roots at x give W once C_h^2 M_1^{-1/3} ≤ 1/2. The column sum is the same. (12) is Tonelli over the labelled intermediate coordinate. |
| 3, (13)-(16) | ADVANCE | At λ = 2b_s²/a_s, ‖(I - A_</λ)v‖² ≤ (1 - 2a_s/λ + b_s²/λ²)\|v\|² = ρ²\|v\|². A row of N_t^j has at most c(1+jr)^4 entries, so Cauchy-Schwarz gives √c(1+jr)²ρ^j. The choice θ ≤ -log ρ/(2r) gives e^{θ jr} ≤ ρ^{-j/2}. Then \|K_t\|_θ ≤ 1/4 + 1/4. The order r, then θ, then n, is noncircular. D ≤ length + 2R_* holds because the chain tree is connected and the hull lies within R_* of it. |
| 4, (17) | ADVANCE | The scalar identity, its Jordan-block extension, and Tonelli with the majorant 2p_r/(λ+t). The integral of t^{-1/2}/(λ+t) over (0,∞) is π/√λ. The symmetrized family has the same sum because (A+t)^{-1} is symmetric. |
| 5, (18)-(20) | ADVANCE | (18): a piece of length M/4, thickened by R_*, has ℓ∞ diameter < M when M ≥ 8R_*, so it meets at most 16 cubes; #P ≤ 16(1 + 8l/M). (19): a varied product starts at a row of Z_0 and its hull meets a cube at distance ≥ w, so l_1 + l_2 ≥ w - R_*. (20): the Cauchy integral on \|z\| = h/ε gives \|f(1) - f(0)\| ≤ sup\|f\|/(h/ε - 1) ≤ 2ε sup\|f\|/h. The four terms sum to 2WU e^{32κ̄-dM} + 6WUε/h, which is (20) with T = 2WU + 6WU/h. |
| 6, (21) | ADVANCE | (16) at t = 0 gives W_C. (11) with κ ≤ θ ≤ η/2 gives W_A. The Schur chains have moment W_A + W_A² W_C. |

Inv-root Section 1, redone. Um-envelope (5): with w ≥ 2R_h, δ(w - R_h)/4 ≥ δ c_w M/8. The inverse comparison: gaps a/2 and a/4 give ‖C - C_ref‖ ≤ (4/a)(2/a)e. (6)-(7): add and subtract X_s r_0. (8): slope t_1/L < 1/(4C_h^WF) against 1/(2C_h^WF). κ̄ ≥ Θ + 1 gives e^{κ̄} - 1 ≥ e^Θ(e - 1) ≥ e^Θ. (9): e^{dM} ≥ (dM)^5/5!. I also matched um-envelope (1) with SA UM15: with D = A c_m L^4 the two are equal term by term, and UM18-UM19 read as um-envelope uses them. Not re-read here: c4-order rows 1-7 and 10-25, and the radius window of its row 16.

Notes that break nothing. They fix the precision of what Section 6 of inv-root claims.

- (a) Lemma 4.1 of `sa-2.13-2.md` uses two facts about carriers: each factor carrier contains its two end coordinates, so consecutive factors share the contracted coordinate; and the diameter. Its proof never uses connectivity. Inv-root's endpoint balls contain the ends. For a precision term, add the two end coordinates to the read hull; D ≤ l_ω + 2R_h is unchanged, because both ends lie on every admitted tree.
- (b) D must be measured in a metric that dominates ℓ∞, because the threshold argument of `sa-2.13-2.md` Section 4 is in ℓ∞. Physical unit-lattice distance dominates ℓ∞.
- (c) All of inv-root's bounds hold where the A2 bounds hold, that is, on the fixed complex neighbourhood of pairs regular for the step's sequence. Each term is holomorphic on the local class on its hull. This is the same domain as h-walk (H2) and as the outline's statement 5 (SA 10311-10338). It is not a defect.
- (d) The length-weighted bounds (15) and (17) are stronger than the diameter bounds (16) and (21). The polymer readers in Section 3 below need the length form. Inv-root supplies it.
