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

## 2. Does the outline fix a different carrier expansion for the cut?

**No.** The outline names statement-5 walk series for the cut. It constructs none for the covariance. SA 17557-17564 fix no expansion.

- **What SA 17550 names.** "A chain is either a walk term of Δ^(j) or a sequence of a walk, a resolvent walk and a walk." In free coordinates the form is the step's precision 𝖠: "one has 𝖠 = 𝖢^𝖳 Δ^(k) 𝖢" (SA 10208). Its covariance is C^(j)(Λ_{j+1}) = (χ_Λ 𝖠 χ_Λ)^{-1} (SA 10206, 17532). The walks are those of statement 5 (SA 10311-10338): walks of cells of side O(M_1), a factor (C M_1^{-1/2})^{|ω|} M_1^{-|ω|/2} per walk, hull [[ω]], carrier [ω] = [[ω]] ∩ Ω_0 (SA 10210). This is Balaban's form, CMP 99 (3.90)-(3.94).
- **Precision side: no change.** Statement 5 for χ_Y 𝖠 χ_Y is rebuilt as `h-walk.md` Theorem H, with power M_1^{-1/3} and the read sets of `h-walk-fix.md`. Inv-root (11) uses exactly this series and these hulls.
- **Covariance side: nothing to conflict with.** Statement 5 bounds C^(k)(Y) by "the kernel bound that 6 states" (SA 10329). Statement 6 comes from 1c.8 (SA 10477). The outline does not write it out (`h-walk.md` Section 10 item 3). `h-walk-fix.md` Section 5 item 5 records: "Statement 5 for C^(k)(Y) is not in h-walk.md, and it stays open." SA 10478 also treats a walk expansion "as a datum enjoying the short list of properties of 7". So the adoption specifies a series that the outline leaves unconstructed.
- **What the adoption changes against statement 5.** Two things. The index is a chain of grouped polynomial entries and long precision walks, not a walk of M_1-cells. The per-term bound is an absolute moment at a fixed rate θ, not a factor M_1^{-1/2} per step. Section 3 shows that no reader of the cut reads either one. The per-walk factor serves statement 7 (SA 10552-10558, the parameter count and the torus push-forward). The cut does not decouple its kept forms.
- **What SA 17557-17564 say.** A rejected chain is longer than a cell. The kept form is "not a Schur complement but a truncated series. Its lower bound is therefore not inherited and has to be proved", with a plan by IMS localisation (SA 17558). Then the carriage rule (SA 17558, 17561, 17564). None of this fixes a series. `sa-2.13-2.md` Lemma 4.1 replaces the IMS plan.
- **Carriers.** SA 10558 states that the uncut hull is connected and that the carrier [ω] "need not be connected when Ω_0 ≠ T_ℓ". SA 17550 asks for chains "with connected carriers". So the cut must read uncut hulls. Inv-root's rule ("use the uncut connected hulls, including the endpoints") is this reading, not a change. The threshold of Lemma 4.1 holds under either reading: rejected implies D([ω]) ≥ s, hence D(hull) ≥ s.
- **The operation changes by specification.** Kept form and rejected part depend on the series; their sum S does not. The completed square moved into 𝐓^(j) is exact (SA 17540). So no identity ties the cut's series to the covariance series of the cluster expansion of the integrated field (SA 17542-17548).

## 3. The readers of the stored precision

Every reader accepts the adopted series. The table gives each reader, what it reads, and where the adopted series supplies it. Lemmas L, P and C are in Section 4.

| Reader | Line | What it reads | Supplied by |
|---|---|---|---|
| Retention rule | SA 17550 | chains of terms; the level-(j+1) cells a carrier meets; invariance under reversal | chain carrier = union of factor carriers; transpose-closed families (inv-root Sections 4, 6) |
| Rejected part 𝖡^× | SA 17554, 17558 | \|𝖡^×(X)\| ≤ C p_0(g_j)² e^{-cMŘ_{j+1}} e^{-κ d_{j+1}(X)} for stored fields in range | Lemma P, from the length moments (11), (15) |
| Kept-form lower bound | SA 17555, 17558 ("has to be proved"), 17693 | ⟨A', Δ^loc_𝔨 A'⟩ ≥ c Σ_b \|A'(b)\|² | `sa-2.13-2.md` Lemma 4.1 with (4.1) from inv-root (21); Lemma C at complex pairs |
| Carriage | SA 17558 (forms "given as functions of a pair (U,J) near 𝔨 ... constructed once and for all"; oscillation ≤ C p_0² e^{-κ d^♮_{j+1}(R)} "measured in the hull length"), 17561-17564 (localised differences) | each kept chain a holomorphic function of the pair and regions on its carrier, the same for every label; a pinned bound decaying in hull length; uniform bounds on a complex neighbourhood, for Cauchy estimates | Lemma L; the length moment (15); note (c) of Section 1 |
| Carried term unchanged | SA 19523(e); SA 18133 (a drop-out keeps its "complete kept forms") | the defining function of a kept form does not change | the series is fixed once, as functions of the pair (Section 5) |
| Lemma 2.5(iii) | SA 17676-17682 | ⟨B, Δ^(k) B⟩ ≥ c‖B‖², "and the bound extends to the kept conditional forms (2b)" | A2 for Δ^(k); the kept-form row above |
| Fluctuation, collar and rim witness | SA 18300-18330 (stored-schur) | κ_pos below the complete-precision gap and below the kept-form lower bound, in stored scaled coordinates | κ_pos = a/2 at real pairs, by Theorem A below; one step stores one level, so scaling multiplies both sides by one factor |
| Piece majorants | SA 19002 | "The Gaussian integration uses the Schur minimum" | the same bound |
| Stored Gaussian blocks | SA 18757-18790 | coercivity of the complete kept forms, used as β in the triangular Gaussian | β = a/2 by Theorem A |
| Complex-pair envelope | SA 18040-18105 | stored Gaussian weights at real reads inside Φ°; background differences inside V_X | real reads: Theorem A; differences: the carriage row |
| `sa-2.13.md` | Theorem 8.1, hypothesis 2; Section 9 | the complete and cut precision bounds inside the 2.5 witnesses | through the witness rows above |
| `sa-2.13-2.md` Section 4 | Lemma 4.1 | (4.1); transposition closure; ends inside carriers; D in a metric dominating ℓ∞; chain carrier = union | inv-root (21); notes (a), (b) of Section 1 |
| Label locality | SA 17558 (Balaban's rule "fails to be local"); `h-walk-fix.md` Section 5 item 5 | a kept chain depends on the history only through traces near 𝔨 | Lemma L(a) |
| Tori with room | SA 7837, where a kept form enters a localised term | the same function on every torus with room | Lemma L(b) |

No reader reads the walk index or the factor M_1^{-1/2} per step. So no reader needs a different expansion.

## 4. The adopted series and the three lemmas its readers need

Proved by Claude, not yet checked by the other model.

Fix the step j+1. Work in the free level-j coordinates (after pivot elimination), with counting measure and physical unit-lattice distance, which dominates ℓ∞. I is the set of stored coordinates (bonds of Ω_{j+1} ∖ Λ_{j+1}). J is the set of integrated coordinates (bonds of Λ_{j+1}). 𝖠 is the step's precision, inv-root (10).

**Definition D (adopted stored carrier series).**

1. *Precision terms.* The terms A_ω(x,y) of `h-walk.md` Theorem H for 𝖠 at the pair, with the count (H1), the bound (H2) and the full read hulls of `h-walk-fix.md` Lemma N(d) (radius R_h = 16L³M_1 + C_L). Restrict them to the blocks II, IJ, JI. Carrier: the full read hull together with x and y. Length: l_ω(x,y) of inv-root Section 2.
2. *Covariance terms.* The chains R_α(0;x,y) of inv-root (15) at t = 0, for 𝖠_J = χ_J 𝖠 χ_J, with the fixed numbers r, λ, n and the grouping of (14). Carrier of a grouped entry: B(x,R_*) ∪ B(y,R_*), R_* = nr + R_h. Carrier of a chain: the union of its factor carriers. Length: the sum of the factor lengths.
3. *Symmetrization.* Replace each term τ by τ/2 and τ^𝖳/2, with the same carrier. The sums do not change, because 𝖠 and 𝖠_J^{-1} are symmetric.
4. *Chains of S.* A chain μ is either a precision term of the block II, or a product A_ω R_α A_ω' with blocks IJ, JJ and JI. Its carrier is the union, and its length l_μ is the sum.
5. *Retention.* Apply the rule of SA 17550 to the chain carriers of item 4.

Each term τ of Definition D has end coordinates in its carrier. Its carrier lies within R_* of a connected set T, which contains both ends and has length at most l(τ) + ε, for every ε > 0. Call this property (T). For a grouped entry, T is the segment [x,y]. For a precision term, T is an admitted tree of (H2). For a chain, T is the union of the factor sets; it is connected, because consecutive factors share a coordinate.

**Lemma L (locality).** Let τ be a term of Definition D.

- (a) Let two sets of step data agree on the carrier of τ: the region traces, the trace of J and the pair are the same there. Then τ belongs to both families and has the same value.
- (b) The same holds for two tori with room that a translation in M_1 ξ_{j+1} ℤ⁴, carrying Ω_{j+1} and J, relates on the carrier.
- (c) τ is real at real pairs. τ is covariant under each gauge transformation and each isometry under which all precision terms are covariant and which preserves the regions.

*Input.* `h-walk-fix.md` Lemma N and Theorems W', H' (checked in `gates/h-walk-fix-gate.md`, items 1, 5, 6): a precision term whose full read set lies where two sets of data agree is in both index families and is the same function, also across tori with room, for grid translations.

*Proof.* For precision terms, (a) and (b) are the input. Take a grouped entry P_0(x,y) = λ^{-1} Σ_{i<n} N^i(x,y), with N = I - λ^{-1} χ_J A_< χ_J. The entry N^i(x,y) is a sum over paths x = u_0, ..., u_i = y in J with steps of length at most r, so every u_m lies in B(x, ir). The entry A_<(u,v) sums the precision terms with l_ω(u,v) ≤ r. Each of them has its full read set within R_h of a tree of length at most r through u, hence inside B(u, r + R_h). So every read of P_0(x,y) lies in B(x, (n-1)r + r + R_h) = B(x, R_*). By the input, the precision terms with read set in that ball are the same for both data, with the same values. The condition l_ω(u,v) ≤ r depends only on the read set and on u, v. The numbers λ, r, n are fixed. So P_0(x,y) is the same. The argument for Q_0 is the same with i = n. The E-factors are precision terms. A chain is a product of its factors, and its carrier contains each factor carrier. This proves (a). The proof of (b) is the same with the translation input. For (c): a polynomial with real fixed coefficients in real terms is real. An isometry that preserves the regions preserves the lengths l_ω(u,v), so it maps the split A = A_< + E to itself. Products of covariant terms are covariant. Symmetrization commutes with these maps. ∎

What (c) does not give: gauge covariance beyond the block-constant subgroup (𝖠 itself has no more, `h-walk.md` test 2.1), and covariance of pointed totals under all isometries (B2, SA 3937-3950). Both stay open, as they are for the precision terms.

**Lemma P (rejected part).** Let s := LM Ř_{j+1}, the side of a level-(j+1) cell in level-j units. Polymers are connected unions X of the level-(j+1) cubes of side LM, connected through closed cubes. d_{j+1}(X) is (LM)^{-1} times the length of a shortest tree in X that meets each cube (SA 5866). Assign each rejected chain μ to X(μ): the first, in a fixed order of finite sets of cubes, among the connected unions of least cardinality that contain every cube meeting the carrier of μ. Put

  𝖡^×(X) := -(1/2) Σ_{μ rejected, X(μ) = X} ⟨A', μ A'⟩.

Assume LM ≥ 8R_*, s ≥ 4R_* and Ř_{j+1} ≥ 1. Let sup_b \|A'(b)\| ≤ H. Then for every cube Q,

  Σ_{X ∋ Q} \|𝖡^×(X)\| e^{κ_1 d_{j+1}(X)} ≤ C_B H² e^{-θ s/32},   κ_1 := θ LM/1024.   (P)

C_B depends only on θ, the coordinate multiplicity, W and 2p_r/λ. It does not depend on M, depth, volume or the label. With H = C p_0(g_j), (P) gives the bound of SA 17554 with c = θL/32, and with κ_1 in place of κ once M ≥ 1024κ/(θL).

*Proof.* Step 1. A rejected chain has D(μ) ≥ s (threshold of `sa-2.13-2.md` Section 4, with note (b) of Section 1). By (T), D(μ) ≤ l_μ + 2R_*. So l_μ ≥ s - 2R_* ≥ s/2.

Step 2. Take T as in (T), of length at most l_μ + ε. Traverse it as a closed walk of length at most 2(l_μ + ε). Cut the walk into at most 1 + 8(l_μ + ε)/(LM) pieces of length at most LM/4. Each piece, thickened by R_*, has ℓ∞ diameter at most LM/4 + 2R_* < LM, so it meets at most 16 cubes. The cubes that meet the R_*-neighbourhood of T form a connected union, because that neighbourhood is connected. This union contains every cube that meets the carrier. So |X(μ)| ≤ 16 + 128 l_μ/(LM), after ε → 0.

Step 3. Join the centres of adjacent cubes of X(μ) along a spanning tree of their adjacency graph. Each segment has length at most 2LM and lies in the union of its two closed cubes. So d_{j+1}(X(μ)) ≤ 2(|X(μ)| - 1) ≤ 32 + 256 l_μ/(LM).

Step 4. The start x of μ lies in its carrier, hence in a cube of X(μ). Each cube of X(μ) is within 2LM |X(μ)| of x. So Q ∈ X(μ) gives dist(x,Q) ≤ 32LM + 256 l_μ.

Step 5. Put β := θ/1024. Split θ l_μ into four quarters. Step 1 bounds the first quarter below by θs/8. Step 3 bounds the second below by κ_1 d_{j+1}(X(μ)) - θLM/32. The third quarter equals 256 β l_μ. The fourth is nonnegative. Also 1[dist(x,Q) ≤ 32LM + 256 l_μ] ≤ e^{β(32LM + 256 l_μ - dist(x,Q))}. Each rejected chain is counted once, and \|⟨A', μA'⟩\| ≤ H² \|μ(x,y)\|. So the left side of (P) is at most

  (H²/2) e^{-θs/8 + θLM/16} Σ_x e^{-β dist(x,Q)} Σ_{(y,μ) from x} e^{θ l_μ} \|μ(x,y)\|.

The inner sum is at most W + W²(2p_r/λ), by (11) with θ ≤ η, by (15) at t = 0, and by (12). The number of lattice points within distance t of Q is at most c(LM + 2t + 1)⁴, so Σ_x e^{-β dist(x,Q)} ≤ C_β (LM + 1)⁴. Since s ≥ LM, -θs/8 + θLM/16 ≤ -θs/16. Finally (LM + 1)⁴ e^{-θs/32} ≤ (LM + 1)⁴ e^{-θLM/32}, which is bounded by a constant C_θ, because e^t ≥ t⁴/4!. This proves (P). ∎

**Lemma C (complex pairs).** Let 𝖠 be a complex matrix on ℂ^{I∪J} with Re 𝖠 := (𝖠 + 𝖠^*)/2 ≥ γ > 0. Let S := 𝖠_II - 𝖠_IJ 𝖠_JJ^{-1} 𝖠_JI.

- (a) Re S ≥ γ.
- (b) Suppose the series of S has the moments (4.1), with W := W_A + W_A² W_C, and every rejected chain meeting I has D ≥ s. Then the kept matrix K satisfies Re K ≥ γ - W e^{-κs}.

No symmetry of 𝖠 is used.

*Proof.* (a) Re 𝖠_JJ ≥ γ, so 𝖠_JJ is invertible. For v ∈ ℂ^I put w := -𝖠_JJ^{-1} 𝖠_JI v. Then 𝖠_JI v + 𝖠_JJ w = 0, so w^*(𝖠_JI v + 𝖠_JJ w) = 0. Hence (v,w)^* 𝖠 (v,w) = v^* 𝖠_II v + v^* 𝖠_IJ w = v^* S v. Its real part is at least γ(\|v\|² + \|w\|²) ≥ γ\|v\|². (b) The matrix R := S - K has row and column sums of \|R_xy\| at most W e^{-κs}, as in the proof of Lemma 4.1. So \|v^* R v\| ≤ (1/2) Σ_{x,y} \|R_xy\| (\|v_x\|² + \|v_y\|²) ≤ W e^{-κs} \|v\|². Subtract this from (a). ∎

At complex pairs of the A2 neighbourhood, Re 𝖠 ≥ a with a = 3c_L/4, and ‖𝖠‖ ≤ b with b = C_A + c_L/4 (`a2-full.md` Theorem II and Lemma 5.1; `gates/a2-full-gate.md` Sections 4-5). Inv-root's moments hold uniformly there (note (c) of Section 1). So Lemma C applies with γ = a.
