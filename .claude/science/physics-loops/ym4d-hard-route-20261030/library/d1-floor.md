lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T04:21Z

# d1-floor: the torus floor (SA L23481) and the upper stability bound OH4 (SA L23439)

Queue row 170. Pinned at commit b1388bfbd, branch `claude/ym4d-hard-route`. Written by Claude (Opus 5.5, max) on the Mac mini worker, in a fresh session. Research text, not an audit; it grants no status. Proved by Claude, not yet checked by the other model, unless a line says otherwise.

**Moves:** T0 skeleton item 6 (D1, rank 10; node OSF16), read by S2, S3, TU10 and UI.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the history representation (SA 1a.2.3, L7463), Theorem 2.1 (L17259), the criteria OH1-OH8 (L23385-23630), (OSF16) (L19782) and the floor argument of (4c) (L23175-23189). T. Balaban for the background theorem (CMP 102, 1985, Theorem 1) behind A1, and for CMP 119 (1988) Theorem 1 and Corollary 3, which the outline's Theorem 2.1 extends. OpenAI Codex for `library/sa-2.13.md` (Theorem 8.1) and `sa-2.13-2.md`. Claude for `library/pre-213.md` (Theorem P) and `library/carrier-adopt.md`.

**Sources.** Outline `YM4_sketch_500.tex` at `31a47c543775f3f74013d06dd5d85962358f3b9e`, fetched by URL into a private scratch folder. Read: L4088-4135 (D1), L6040-6075 (tests), L7463-7500 (exact identities, vacuum constants), L7569-7670 (one step), L17255-17345 (Theorem 2.1, tests), L17516-17560 (T on a label), L19380-19406, L19640-19812 (OSF9-OSF16), L22947-23240 ((4c)), L23385-23630 (OH1-OH8). No numeric job was run; every step below is a written inequality.

## 0. Result in brief

(Filled in at the end.)

## 1. The floor (SA L23481) as an implication

### 1a. Notation and the three clauses the floor reads

Work at the last level K, in level-K units. The bare spacing is η = L^{-K}. The final torus has N := N_K sites and 4N bonds; dV is normalized product Haar measure on them. The frame value is θ := θ_K, with g := θ^{-1/2}. The tests use ε_K = g p_0(g), p_0(g) = (log g^{-2})^p (SA L4068, L17257). The plaquette test of a test cube □ is χ_K(□) = 1{|∂U_{K,□}(V) − 1| < ε_K η² on the bare plaquettes of □^{~1}} (SA L6061; the cube-localised background U_{K,□} is posed on the second-rule tower of □^{~4}, `library/assign-adopt.md` 1 and 4.5). χ_K is the product of χ_K(□) over all test cubes. |·| is the operator norm; another fixed matrix norm changes only the constants below. For s > 0 put

  B_s := {V : |V_b − 1| < s for every final bond b}.

S_0 is the never-large label: Ω_j = Λ_j = T and S_j = ∅ for every j (SA L21888). For S_0 there are no standing operations, so T'_K(S_0) = 1. There is no boundary term, since Z_j = ∅. The profiles are φ_j ≡ 1, so x_K(·) ≡ x_K. At S_0 the label constant is −ℰ_{K,S_0} = E (SA L7499). E is the vacuum constant of D1 and OH1-OH6.

The floor reads three clauses of the outline's Theorem 2.1 (SA L17259) at S_0. They are taken as premises here; Section 2 gives their sources and state.

- **(P1) Positivity and exactness at w = 0.** Z(0) = ∫ρ_K dV, and ρ_K = Σ_S ρ_{K,S} with every ρ_{K,S} ≥ 0 (SA 1a.2.3, L7463; Theorem 2.1, "each term is a non-negative measure"; class clause (vii), L19420).
- **(P2) The form at S_0.** ρ_{K,S_0}(V) = e^E χ_K(V) exp[−x_K A(U_K(V)) + 𝐒_K(V)], with 𝐒_K := 𝐄_K + 𝐑_K real on {χ_K = 1}. Here U_K(V) is the never-large background (the regular critical orbit with M^K U = V), 𝐄_K = Σ_{j≤K}{Σ_X [E^{(j)}(X,U) − E^{(j)}(X,1)] − b_j A(U)}, and 𝐑_K is the analogous sum of R-terms (SA L7499, L7569-7620, L17262).
- **(P3) Regular action bound.** There is E_−, fixed before the coupling ceiling γ, with 𝐒_K(V) ≥ −E_− N at every V ∈ B_s with χ_K(V) = 1. This is the first inequality of Theorem 2.1 (SA L17284), read at S_0 and on B_s only.

**Input that is checked.** A1, as `library/a1-balaban.md` Section 8, (8.2): for real data whose test loops have error at most ε_1 ≤ a_1, the default constrained problem has one regular critical orbit U, with |∂U(p) − 1| ≤ B ε_1 η² 𝖫(p)^{-2} and |J(U)(b)| ≤ B ε_1 𝖫(b)^{-3}. B, a_1 are fixed before depth and volume. Checked line by line by Claude (`gates/a1-balaban-gate.md`, row 91), first failing step none, conditional on F0. F0-F5 are checked (`gates/flat-port-gate.md`). (10.2) of that note is not read here.

### 1b. Lemma H (Haar ball)

For 0 < s ≤ 1, normalized Haar measure on SU(2) gives {U : |U − 1| < s} mass at least 8s³/(3π³).

*Proof.* Write U = cos ϑ + i sin ϑ n·σ with ϑ ∈ [0, π], n ∈ S². Normalized Haar measure is (2π²)^{-1} sin²ϑ dϑ dΩ(n); its total mass is (2π²)^{-1}·4π·(π/2) = 1. The eigenvalues of U are e^{±iϑ}, so |U − 1| = 2 sin(ϑ/2) < ϑ for ϑ > 0. Hence {ϑ < s} lies in the ball. Its mass is (2/π)∫_0^s sin²ϑ dϑ. On [0, 1], sin ϑ ≥ 2ϑ/π, by concavity of sin on [0, π/2]. So the mass is at least (2/π)(4/π²)s³/3 = 8s³/(3π³). ∎

This is the outline's computation (SA L23509-23517); the open ball needs no change of constant, since {ϑ < s} has the same mass as {ϑ ≤ s}.

### 1c. Lemma L (the lift has small loops and is consistent)

Let V ∈ B_s. For q < K let V^{(q)} be the lift of V to T^{(q)} (SA L9784): V^{(q)}(b) = 1 if b lies inside a level-K block, and V^{(q)}(b) = V(c) if b leads from the block of c_− into the block of c_+. Put V^{(K)} = V. Suppose 4s < c_M L^{-2}, the radius of the main rule of the average M (SA L7068-7073). Then:

(i) every plaquette variable of V^{(q)} is 1 or the holonomy of a plaquette of V; so |∂V^{(q)}(p) − 1| ≤ 4s for every q ≤ K and every level-q plaquette p;

(ii) M(V^{(q)}) = V^{(q+1)} for q < K.

*Proof.* (i) Take a level-q plaquette p in the (μ, ν) plane with lowest corner x. If no bond of p crosses a block face, all four bonds are 1. If only the two μ-bonds cross a face, x and x + e_ν lie in one block, so both μ-bonds cross between the same two blocks. They carry the same value V(c), and the ν-bonds are 1. So ∂V^{(q)}(p) = V(c) V(c)^{-1} = 1. The same holds with μ and ν exchanged. If both pairs cross faces, the four corners lie in the four blocks y, y + e_μ, y + e_ν, y + e_μ + e_ν, which span a level-K plaquette P. The four bonds carry the four bond values of P, so ∂V^{(q)}(p) is the holonomy of P at y. For unitary W_i, W_1W_2 − 1 = (W_1 − 1)W_2 + (W_2 − 1) and |W^{-1} − 1| = |W − 1|. So |W_1W_2W_3^{-1}W_4^{-1} − 1| ≤ Σ_i|W_i − 1| < 4s.

(ii) Level-K blocks are unions of level-(q+1) blocks, since blocks are centred and L is odd. Take a level-(q+1) bond c. Every contour of the average stays in B(c_−) or B(c_+), and so inside one level-K block; it carries 1. So U(c_−, x) = U(x', c_+) = 1. The straight segment [x, x'] has L level-q bonds. Exactly one crosses the face between B(c_−) and B(c_+). If c crosses a level-K face, that face lies in the level-K face, so this bond carries V(c̄), where c̄ is the level-K bond of c; otherwise it carries 1. The straight transport U[c] has the same single crossing. Hence W_x = U(c_−,x)U([x,x'])U(x',c_+)U[c]^{-1} = 1 for every x. By (i), ϖ_c ≤ 4s < c_M L^{-2}, so the main rule applies, and M(V^{(q)})(c) = exp(0)·U[c] = V^{(q+1)}(c). ∎

So the lifted datum of the tower problem is consistent across levels. A substituted finer average at a tower seam equals the coarser lift value. Every test loop of that datum is a plaquette of some V^{(q)}, and its error is less than 4s. The same holds for the global problem of S_0, whose datum is V alone.

### 1d. Lemma B (backgrounds on B_s)

Let 4s ≤ a_1 and 4s < c_M L^{-2}, and let V ∈ B_s.

(i) The global background U_K(V) exists, and |∂U_K(V)(p) − 1| ≤ 4Bs η² at every bare plaquette p. Hence A(U_K(V)) ≤ 48B²s²N.

(ii) Each cube-localised background U_{K,□}(V) exists, and |∂U_{K,□}(V)(p) − 1| ≤ 4Bs η² at every bare plaquette of □^{~1}.

(iii) If 4Bs < ε_K, then χ_K(V) = 1. So B_s ⊂ {χ_K = 1}.

*Proof.* (i) For S_0 every region is T, so every plaquette has corner scale 𝖫 = 1. By Lemma L the datum error is less than 4s ≤ a_1. A1 (8.2) gives the bound. For SU(2), a_p = 1 − ½ Re tr U_p = 1 − cos ϑ_p = ½|U_p − 1|², with e^{±iϑ_p} the eigenvalues. So a_p ≤ 8B²s²η⁴. There are 6η^{-4}N bare plaquettes. Hence A(U_K(V)) ≤ 48B²s²N.

(ii) The tower of □^{~4} under the second rule is a separated sequence (SA Theorem 6(a), L9776). Its datum is the lift, with error less than 4s by Lemma L. A1 (8.2) applies. By `assign-adopt.md` 4.5 ((A3)), the top member contains □^{~2}. There 𝖫 = 1, so the bound is 4Bs η².

(iii) By (ii) every plaquette that χ_K(□) tests has |∂U_{K,□} − 1| ≤ 4Bs η² < ε_K η². ∎

### 1e. Theorem F (the floor)

Fix c ∈ (0, 1] and put s = c θ^{-1/2} = c g. Let the coupling ceiling γ satisfy, for g ≤ γ:

  4cγ ≤ a_1,  4cγ < c_M L^{-2},  p_0(γ) > 4Bc,  and x_K ≤ 2θ (the tube).

Assume (P1)-(P3). Then

  e^{−E} Z(0) ≥ exp[−(C_F + 6 log θ) N],  C_F := E_− + 96B²c² + 4 log(3π³/(8c³)).   (F)

*Proof.* The ceilings give Lemma B on B_s. Indeed 4Bs < ε_K is 4Bc < p_0(g), and p_0 increases as g decreases. By (P1), Z(0) ≥ ∫ρ_{K,S_0} dV ≥ ∫_{B_s} ρ_{K,S_0} dV. On B_s, χ_K = 1 by Lemma B(iii). So (P2) and (P3) give ρ_{K,S_0} ≥ e^E exp[−x_K A(U_K(V)) − E_−N]. By Lemma B(i) and x_K ≤ 2θ, x_K A(U_K(V)) ≤ 2θ·48B²c²θ^{-1}N = 96B²c²N. By Lemma H and independence of the 4N bonds, the Haar mass of B_s is at least (8c³θ^{-3/2}/(3π³))^{4N}. Multiplying, e^{−E}Z(0) ≥ exp[−(E_− + 96B²c²)N]·(8c³/(3π³))^{4N}·θ^{-6N}, which is (F). ∎

**Remarks.** (a) The exponent 6 = ½·d·dim SU(2) per site, as in SA L23185. (b) Every ceiling is on γ alone, after L, B, a_1, c_M, c. So the order of constants of SA L19476 is kept. (c) Under first passage, θ_K lies in a fixed window above g^{-2}, so C_F + 6 log θ is a constant C_g (SA L23573-23580). (d) Lemma B(i) is the "action bound which must be verified" of SA L23497-23500. Lemma B(iii) is its "inclusion in the characteristic set". Both are now implications from the checked A1 and the adopted Definition A. The outline's elementary bound C_A = 48 for the coarse Wilson action (SA L23527-23535) is not used.

## 2. What (P1)-(P3) read, and their state

| Premise | Outline source | What it reads | State here |
|---|---|---|---|
| (P1) positivity, exactness | 1a.2.3 (L7463); Theorem 2.1; clause (vii) (L19420) | C1: every operation is a total Borel positive kernel or change of variables (SA L4041) | open (`t0-skeleton.md` C1: map only; ledger: extreme) |
| (P2) the form at S_0 | Theorem 2.1 (L17262); 1a.2.7 (L7501); 1a.2.9 (L7598-7620) | the whole induction: the one-step map 1.6 (B4) at real data for S_0, and the healed sums of R, which enter S_0 through the label-free R^{(j)} (SA L17548: "what R leaves is added"), so 2.10; class preservation, Theorem 2.11 (C4) | open |
| (P3) volume bound at S_0 | 1a.2.7, "when the label has no large fields, abs(𝐄_k(U_k)) + abs(𝐑_k(U_k)) ≤ C abs(T^(k))" (L7514); Theorem 2.1, first inequality (L17283) | the age gain of the regular terms (SA L19426, L19502-19510), so B2 (pointed marginal extraction, L3937) at the never-large background; the norm clauses ‖E^(j)‖ ≤ E_0, ‖R^(j)‖ ≤ g_j^κ0 | open (B2: `t0-skeleton.md` cited; ledger: extreme) |

**Why (P2) is a label statement, not a history statement.** One could try to keep only the history with no large field at any step. Its term is at most ρ_{K,S_0}, by positivity. But its exponent does not carry the R^(j): those contain the healed sums. E contains Σ_X R^(j+1)(X, 1) at every level (SA L7499). So that history's density is not normalized by e^{−E} up to an error O(N). The floor must use the label S_0 with its healed sums.

**Why (P3) is not a consequence of the norm clauses.** Take ‖E^(j)‖_{j,κ} ≤ E_0 alone. A second-order Cauchy bound at U = U_K(V), V ∈ B_s, gives per level j about C E_0 B²c² (θ_j/θ_K)(log θ_j)^{-2q} N, with α_{0,j}^{-2} = cθ_j(log θ_j)^{-2q} (SA L19432). By the flow, θ_j ≈ θ_K + λ(K − j). So the sum over j diverges like K²/(θ_K(log K)^{2q}). Taking a smaller ball radius s does not repair this: it costs 12 log(1/s) per site, which then grows with the cutoff. The outline's tent example (SA L19426-19432) is an array that meets every norm clause and adds the same multiple of the action at every level. So (P3) needs the cancellation by each member's own counterterm b_j A. That cancellation is B2.

**The R-part of (P3) needs no cancellation.** Every level is carried: 𝐑_K = Σ_{j≤K} Σ_X [R^(j)(X,U) − R^(j)(X,1)] (SA L17541; a carried term is unchanged, SA L19523). At the never-large background a level-j R-term costs a second-order Cauchy factor, which is the weight w_{K,j} ≤ C(K + 2 − j) of SA L19505. With ‖R^(j)‖ ≤ g_j^{κ0} and κ0 > 4, Σ_j w_{K,j} g_j^{κ0} converges. Section 4 proves this part, given its path lemma. Only the E-part needs B2.

**First input not yet proved, for the floor.** In reading order it is (P1), the positivity clause C1. (P2) and (P3) are open as well. Of the three, (P3) is the one the floor adds to plain membership of the class. Its first open input is B2 at the never-large background. Section 4 reduces (P3) to one Hessian statement.

## 3. The upper stability bound OH4 (SA L23439)

### 3a. Theorem U (OH4 from OH1-OH3)

Let Z(w) = Σ_S τ_S(w)(𝒱) with finitely many labels (OH1). Put Z̃(w) = e^{−E−ℰ(w)}Z(w), where ℰ(w) = Σ_{j,X} e_j(X;w) and ℰ(0) = 0. Let ℰ_S(w) be the vacuum constant of the term of label S; it is a number, not a function of V. Assume (OH2) ‖e^{ℰ_S(w)}τ_S(w)‖_TV ≤ W_S and Re[−E − ℰ(w) − ℰ_S(w)] ≤ C_0N + q(S), and (OH3) Σ_S e^{q(S)}W_S ≤ e^{C_1N}. Then |Z̃(w)| ≤ e^{(C_0+C_1)N}.

*Proof.* Z̃(w) = Σ_S e^{−E−ℰ(w)−ℰ_S(w)}·[e^{ℰ_S(w)}τ_S(w)](𝒱). For a complex measure μ, |μ(𝒱)| ≤ ‖μ‖_TV, and |e^z| = e^{Re z}. So |Z̃(w)| ≤ Σ_S e^{C_0N+q(S)}W_S ≤ e^{(C_0+C_1)N}. ∎

The proof takes no logarithm of Z and uses no zero-free region, as SA L23440-23447 says. Checked here line by line against SA L23385-23447: correct. At w = 0, Z̃(0) = e^{−E}Z(0), with the same E as in Theorem F. So Theorems F and U together give e^{−(C_F+6 log θ)N} ≤ Z̃(0) ≤ e^{(C_0+C_1)N}.

### 3b. How the construction is to supply OH2 and OH3

This is the outline's own assignment (SA (4c), L23153-23172, and L19380-19404), with the library pieces placed in it.

- **Term comparison (OH2, first half).** Put W_S := e^{ℰ_K(S)} τ^abs_{S,c_L}(𝒱) e^{c_L Σ_l|Γ_l|}. Here τ^abs_{S,c} is the label's positive majorant with the reserve weight e^{c·v(ω)} on every local history and the complex suprema inside the integrals (SA L17270-17278). Γ_l are the determining bonds of level l; for S_0 the sum is 4N. The comparison |e^{ℰ_K(S;w)}τ^w_S|(𝒱) ≤ W_S reads three things. (i) (OSF10): if |Ψ_ω| ≤ fN_ω, V_ω ≥ AN_ω, A ≥ f and c_⋆ ≥ 1, then |e^{Ψ_ω}| ≤ e^{c_⋆V_ω}; this is elementary and correct. (ii) (OSF13): the size recursion gives |Ψ_ω| ≤ max{C_W c̄ + 2c_int(1+c̄), f}·N_ω by induction on the nesting, since N_ω = N^0_ω + Σ N_ω'; correct given (OSF12). (iii) (OSF12): the formation bounds for the actual formed source exponents (OSF11) on the whole complex data box, with the carrier oscillation bounds of SA L23104-23140. (iii) is open.
- **Exponent bound (OH2, second half).** q(S) is the label's missing vacuum share plus its missing source-energy share. The vacuum part is the exact slot algebra of `sa-2.13.md` Section 2: (N_j − abs(A_j))e_j plus redone-site terms. It is proved there and checked (`pre-213.md` 1a). The source part is at most Σ_j(C log θ_{j−1} + C)#_j Z_j^+ (SA L23163), given (OH7). (OH7) is elementary from the local bounds abs(ΔE_j), abs(ΔR_j) ≤ C e^{−κd_j(X)} (SA L23547-23565). Those local bounds are D1's localized source energies, which are open.
- **Weighted label sum (OH3 = OSF16).** Σ_S e^{q(S)}W_S ≤ e^{C_1N} is (8.2) of `sa-2.13.md` Theorem 8.1, at a weight c ≥ c_L and with a load 𝓛_c(S) ≥ c_LΣ_l abs(Γ_l) − 4c_LN + q(S). The load (6.4) of that note dominates the determining-bond and defect parts. Theorem 8.1 is checked by Claude as a conditional implication (`pre-213.md` 1a, ADVANCE).

### 3c. The inputs of Theorem 8.1, and their state

| Hypothesis of Theorem 8.1 | Pieces | State |
|---|---|---|
| 1. Geometry and code | Lemma 4.1, (4.2), (5.1)-(5.7), (6.4) | proved by Codex, checked by Claude (`pre-213.md` 1a); premises: the read-address ownership (SA 18449-18470, open) and GEO1-GEO6 (checked under three supplied rules) |
| 2. (8.1), unsummed certificate for the literal operations | stored cut (4.1) of `sa-2.13-2.md` | `carrier-adopt.md` Theorem A: proved by Claude, not yet checked by Codex |
| | complex-pair remainder V_X: (Pre) | `pre-213.md` Theorem P: proved by Claude, not yet checked by Codex (check in row 169) |
| | V_X: (Inn), the inner comparison | **open** (row 169) |
| | V_X: (Act), retained activities and the localisation of SA 17890-17910 | open |
| | V_X: (Ref), the reference denominator | Proposition Ref, log-ratio ≤ 4δ_*: checked (`ref-chart.md`; rows 140, 146) |
| | real denominator price at p_r | `sa-2.13.md` Lemma 3.1: checked (one-sided) |
| | the complex-pair envelope SA 18029-18105, 18719-18876 | open |
| 3. Exact normalized assembly | the healed-history summation and the vacuum identity on the actual exponent and measures | open |

**First input not yet proved, for OH4.** Reading OH4's proof in order: OH1 needs the sourced exact representation, which is C1 (open), as for the floor. Then OH2 needs (OSF12) and the local source energies (open). Then OH3 needs Theorem 8.1, whose first unproved input, in its own order, is hypothesis 2: (8.1) for the literal operations. Inside (8.1) the first open piece is (Inn), the inner comparison of V_X (row 169). (Pre) and the stored cut are proved by Claude and wait for Codex's check.
