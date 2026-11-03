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
