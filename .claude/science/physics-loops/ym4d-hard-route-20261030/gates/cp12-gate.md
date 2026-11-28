First failing step: none

# Pass-3 referee of CP12 (library/cp12.md, 672 lines)

Scope. One line-by-line reading of `library/cp12.md`. The draft `cp12-draft.md` was consulted only at Proposition 8.6 (L275) and Lemma 10.7 (L570–580). Imports were read at the cited places: p82.md §§1–3; pr-lay.md (real bound L38–44, §2 order, G/B/Q L217–240, Lemmas 5–7); in1.md (frame (1)–(3), H-OL (10), H-SF (11), Lemma 4, constant rows 1–10, Amendment 1); st1-r4.md (§2 inputs L125–136, Lemma 5 L347, Lemma 8 L539–628); a3-derivative.md §§3, 4.1–4.2, 6, 6.1, 7.1–7.5, 8.1 and its gate; a2-full.md Theorems IV/V and a2-full-gate §§6–7; c1-repr.md §8; b4-step.md §11; bx-fix.md (H); geoh-draft.md §§2.2, 7.2, 11. Outline lines checked in `sa/ym4.tex`: 6108–6116, 6326–6336, 9598–9606, 9652–9669, 9767–9772, 11756–11776, 12750–12775, 13556–13566, 13663–13672, 17405–17444. CA-I 49495–49547 and YM3-I 10426–10431 were spot-checked; CA-II/CA-III are quoted nowhere. No computation is used as a proof step.

## Findings

**1. L27, L100, L105 (Theorem 3 imports).** Step: the use of a3-derivative §6.1 (local Landau identification) and §7.1 (local Hessian comparison for Delta'). What is wrong: a3-derivative is unfrozen; its gate passes these sections only **with repairs**. They are the Lemma 6.2 repair (the submersion inference does not follow from (35)), one rooted tree per connected component in Proposition 6.4, and the curl correction `d_frak = d + E` for the Delta' bound in 7.1. cp12 cites the sections without these repairs. Theorem 3 uses exactly the repaired statements: "P81's local Landau identification" at L100, and the C_2 epsilon term of (3) with the Delta' bound. Repairable, not fatal: cite "a3-derivative §§6.1, 7.1 with the repairs of gates/a3-derivative-gate.md §§6.1, 7". No estimate changes.

**2. L89–91, display (3).** Step: `||DN°|| <= C_N r + C_2 epsilon`. What is wrong: N_1° = N_1 + (Delta' − W_0)a. Its W_0 part is `(DK_0[.])^T lambda_0`. Its size is ||lambda_0||_Y <= C° ||F'(0)||_F <= C° C_J r_0 (Theorem 2(4) and L78). This bound counts the boundary bonds, where the force is not controlled by the local parameter epsilon (L78 keeps the two bounds separate). So the display should read `C_N r + C_2(epsilon + ||lambda_0||_Y)`. Equivalently it should read `C_N r + C_2' r_0`. The proof already imposes the needed smallness ("including force smallness", L91), so the contraction and the bound 4/3 stand. Repairable, notational.

**3. L76, L114 (P81 supply in actual admission).** Step: "provided their P81 charts are supplied". This is not a defect. Frozen ST1 Lemma 5 (st1-r4 L347) supplies P81 on `||B|| < r_B` with a fixed radius, under A1/F0/REG. Naming it there makes the residual of assembly-status item 1 explicit. With this citation, item 1 is closed conditionally on A1/F0/REG, P82 I1–I8, PR-lay G/B/Q and the repaired a3-derivative.

**4. L118, L143–147, with L135–139 (indices in Theorem 4 and its consumer).** Step: feeding H-prof into a2-full Theorem IV. What is wrong: n_d(p) is defined through the midpoint of p. Theorem IV groups plaquettes by pillar and reads n(y) for the pillar's layer of the determining sequence (a2-full L160). At a seam these differ by at most one level. The consumer therefore needs |w(p)| <= 2 omega_0 (1 + n(y)). This costs a factor 2 in (5). Repairable: absorb the factor into C_IV, or state H-prof with the pillar layer. The identification "Theorem IV's n is the determining-sequence layer" is right: the background and d_B are formed on the determining sequence, as SA 17440 states.

**5. L163–172 (Outstanding: proposed refutation of literal H-prof).** Correctly placed: it is a conditional obstruction, and (7) is correct. The increment estimate checks: IN1 (10) gives |b^0_l − c_0| <= 2c_2, and (11) with u <= c_0/2 gives Σ_{l>t−N_t} b_l >= (c_0/2)(m+N_t) − 2c_2 over m+N_t terms. The term at l = t−N_t costs at least −B_b. Also j_d = t and j_a = t−N_t under the displayed hypotheses, because Ω^a ⊂ Ω^d inside windows (D4: Z'' ⊂ X \ Ω°). See the verdict on geoh D3 below. If that unrefereed result survives, the hypothesis of this mark is false for actual histories above a floor. The mark would then read: "obstruction vacuous above N_t >= N_crit; literal H-prof neither proved nor refuted".

**6. L571, L597–605 (Lemma 11 via frozen ST1).** Step: "equivalently the value-ball portion of frozen ST1 Lemma 8". Confirmed. ST1 (51) and (52) are stated in Lemma 8's **proof**, on `||w||' < r_w` and on the B-ball. They do not use Lemma 8's stated hypothesis `sup n(w) <= a_T`; they use only AV, (15), Lemma 3 and P81. With `||w||' <= lambda ||w||_inf` and s = lambda^{-1} at a settled top, they give (28) with C_T = 3/2 + 3/2. The unit bookkeeping checks: G = lambda J_bare = lambda^{-2} J_n because J_n = lambda^3 J_bare. Not a defect. The citation could add "proof of Lemma 8, at a settled top", because the lemma's statement alone carries the smaller-ball hypothesis. So (28) does not depend on the unchecked c1-repr §8.

## What was checked and holds (by section)

- **Lemma 1, (1).** Solving Xa − K^T lambda = f, Ka = b with the added mass K^T a_r K gives exactly (Tf + Hb, −ΣKGf + (Σ − a_r)b). With a_r = I this is P82 (14). Ran R = ker(Q'G_s) = Δ ker Q' follows from the symmetric idempotent P = G_s Q'^♯ N Q' G_s. Independence from the top mass and pairing holds because both are positive diagonal.
- **Theorem 2 (M1).** The adjoint of ℓ^{-1}K_A in the μ-pairing is K_A^T μ ℓ^{-1}. Injectivity of K_A^T gives (2). With ℓ = 1 this is a3-derivative §3 L41 and §7.5 (μ^{-1}). Assertion 4 follows from S°(0, −λ_0) = (F'(0), 0). (15) consumes only the counting multiplier: none of its five members is a multiplier, and its proof reads ω̇ only through P82 (15) in counting normalization. The outline's convention is cell-weighted, as SA 11760–11774 states ("Its fine pairing and the datum pairing are the actual cell-weighted pairings"). Converting its multiplier value bound costs sup ℓ/μ, which need not be uniform, as L59 says. P82 (3) and a3-derivative (6) are the same recursion (P82's S_W removes the two endpoint factors; a3's F_W multiplies them in their stated order).
- **Theorem 3.** PR-lay's real bound r_0 gives Reg_{2r_0}. Its cubes have side up to c_g M_1 ξ_j >= c_reg M_P ξ_j, and the two bounds add. The ceiling 2r_0 <= α_* checks. The contraction constants (1/8 + 1/8), the half ball, r_B <= r/(4C°C_b) and the 4/3 bound check, and θ_4 <= δ_w/8 <= θ_0. Equation (4) is a3 7.1's identity. The current comes from J = (Ξ_a^T)^{-1}K_a^T ω. The top factor uses Σ_{n<j} L^n η <= Cξ_j. The Hölder member checks. Actual admission matches PR-lay (20)–(21) and Lemma 7: the derivative of t^{-1/2}(log t)^Q has the sign of Q − ½ log t. C_G depends on M_1, and only the late ceiling uses it.
- **Theorem 4.** B_b(1+n_a) bounds the sum. The window argument gives n_a <= n_d + N_t and k − t <= n_d. Rounding gives N_t <= L(log θ_t)^r. The frame bound gives log θ_t <= log θ_k + log(1 + B̄(k−t)). Also (u+v)^r <= 2^{r−1}(u^r+v^r), and log(1+y) <= r(1+y)^{1/r}. The constants C_x and C_x' come out exactly as displayed. For (5): |t| >= 3θ_k/8, with Theorem IV and C_IV(L, θ_4, r_B) as in a2-full-gate D2. The floor θ_4 ρ >= 64 log L is a genuinely additional early floor, since P82's ρ_P gives only θ_4 ρ >= 4 log L.
- **Lemma 5.** The heat-kernel identity, Parseval with the weight (1+|n|²/T)^M, the tail with M > N+2, and the physical scaling to (11) all check. The time splits for (9) check, as does the bound max x^{1−α}(1 + log 1/x) = e^{β}/(eβ) <= 1 + 1/(eβ). In (10) the bounds are R^{2−r} for r <= 3 with N > max(0, r−2). The commutator transfers by [Δ,χ]^T = −[Δ,χ], with output orders 1 and 2. Every constant is mesh-free.
- **Lemma 6.** Ψ_1(0) = I, and Ψ_2 = Ad e^{iu}. The remainder S and its Lipschitz bound (13) check; the η^{−2} factor cancels O(η²V²). The fixed point (14) gives div A_2 = −ξ^{−2}Ψ_1(λ)λ, with the sign verified. The ball and contraction choices hold with K > 2C_R C and a_* small. Reality is preserved.
- **Theorem 7.** The current normalization checks: d/dt of 1 − ½ Re Tr(e^{itηv}P) is η⟨v, π(P)⟩. Each negative plaquette is Ad(U^{−1}) applied to the inverse of a positive one, which gives (16) with the sign δF + J ≈ 0. Also (17), and Δ_η A = δdA + ∇ div A, and (18) check. In (19): R <= ξ/8, the direct bound 2/η < 128/R when R < 64η, the sums 12 and 2, and the vanishing terminal term all check. The Hölder step uses R = ξ/2 >= 64η, or the separation ξ/128. The cap a_FH <= (16C_2)^{−1} keeps η|A_2| in the log branch. Every constant is uniform in s, η/ξ and volume. Only the real clause is claimed.
- **PR1 application (L339–343).** Q on side S+16, with enlargement S+22 and a = 4L³B_*(S+18)w, matches PR-lay (18). The bx-fix (H) real part follows with C_pot M w. The unit conversion costs L^{2+α_H}. The complex part, seams and the current supply are correctly left as imports.
- **Lemma 8.** The Ward identity follows directly from F_z(B^g) = F_z(B) and DF_z(0) = 0; covariance of the background supplies h(dχ). The polynomial extension holds under (20). Linear χ gives zero row and column sums. Quadratic χ gives the two antisymmetries. Reflections and permutations give T = b(δ_{μν}δ_{ρτ} − δ_{μτ}δ_{ρν}). The bulk moment equals b, and contraction gives b Σ_{μ<ν}|F|². Both tent sums equal 1, for N odd or even.
- **Lemma 9.** The half-rate second response, the shell count D_X^{q+4}, the expansion terms ρ²σ^{4+α} and ρ³σ⁶ (using a_out <= ρ_j a_j and a_j <= C r_B), and the regime with t bounded below all check. The base count gives ω_n, which is summable.
- **Theorem 10.** The iterated calculus with s_v = 1 has no second root term; draft L580's "analogous term with ∂_{s_□}" double counts, as L552 says. C2 annihilates disconnected Y. Cauchy gives q_s^{−(|Y|−1)}. Relabeling by Z = Ŷ gives 2^{|Z|} with |Y| >= |Z|/81, and (25) gives e^{−κ|Z|}. κ̄ >= 1 + K(κ + log 2 + 1) implies (25), since e^{κ̄} − 1 >= e^{κ̄−1}. (26) follows from the factorial 2, the animal count A^N, CM⁴N coordinates and the fibre-graph term ε g_k²/r <= ε(g_k/r)² for r <= 1. The doubled domain gives the gate's v = ½.
- **Lemma 11 and (29).** The recursion with Σ t_{q+1}/λ over q < n is bounded. B(w) is at most C_A λ ||w||_inf. The identity (29) is exact. Cauchy with λ^{−2} against R^{−2} gives a fixed constant.

## Proposition D3 of geoh-draft.md (L431–443)

**Is it right? Yes, with one one-line gap in its Lemma D0. It is conditional on geoh's own inputs.** These are the class conditions (G6), the CA-I nest specification (G9), Lemma 7.2 and boxing reach (Lemma 2.2). The chain checks:

- A_l ⊂ B_l ⊂ {d(·,C) <= τ_l}. The hull adds s_l, ten layers add 10 s_l, and boxing adds b_bx s_l. Induction runs from B_{t♭} = C.
- τ_l < 2(11+b_bx) Ř_{t♭} m_l, since Ř is non-increasing and Σ m_u <= m_l L/(L−1).
- {x ∈ X : d(x,C) < m_j} ⊂ Z''_j, because C ⊂ Z''_{j−1} and D0's gap at level j. Only this weaker form is used. The written claim with σ_j would need an inductive path inside X, which is not given, but it is not needed.
- With j − l >= w, A_l ⊂ Z''_j. Hence p ∉ Z''_j gives p ∈ Ω°_l for l <= j − w, and also for l <= t♭.
- The frame step gives Ř_{t♭} <= L2^{r−1}[N_t + r^r(1 + B̄N_t)] <= C_1'(1+N_t).
- N − log_L(1+N) is increasing, so N_t >= N_crit gives N_t − 1 >= w. Then p ∈ Ω°_{t♭+1}, which contradicts the configuration of draft Proposition 8.6 (L275) and of cp12 L165.

**The gap in D0.** For t♭ < u <= k_0, Z''_u = (Ω_u^{~5})^c ∩ X uses the global Ω_u, but the proof checks distance only from Ω_u ∩ X. **Repair:** Lemma 7.2 gives N_10 H_u ⊂ X. So a point within m_u of H_u is at distance >= 10 s_u − m_u >= 9 m_u from X^c, hence from Ω_u ∩ X^c. Separately, the case u = k_0 + 1 reads (G9)'s "consecutive members separated by one layer" as including the pair (k_0, k_0+1). That is a reading of CA-I, to be confirmed when geoh is refereed.

**Does it settle literal H-prof? No.** D3 shows that the cp12 obstruction (7) cannot be realized above the floor N_t >= N_crit. That floor is an X_0 floor at IN1 row 9, after L, r, B̄ and b_bx. So the obstruction does not refute literal H-prof for actual histories. But D3 gives only n_a <= n_d + w with w <= 1 + log_L(2(11+b_bx)C_1') + log_L(1+N_t). Since N_t is up to L(log θ)^r, this leaves |x_k(p) − x_k| <= B_b(1+n_d) + B_b w. The additive term is O(r log_L log θ_k + log_L(1+n_d)), and it is unbounded as θ_k grows. A uniform C(1+n_d) bound would need n_a − n_d <= C(1+n_d), which D3 does not prove. Nothing excludes a site at distance between m_j and τ_l from the core, so literal H-prof stays **neither proved nor refuted**. D3 does sharpen cp12 Theorem 4: its (log θ_k)^r term can be replaced by O(log log θ_k + log(1+n_d)). That replacement is harmless for the consumer either way.

## Constants and order

- **Row 3, before κ, independent of M and κ̄.** These are θ_4 = min(δ_0, δ_w)/8, r_𝔠 and r_B, set from α_*, ε_*, C_car, C°, C_b, C_N and C_2. C_4 and C_IV(L, θ_4, r_B) are in the same row.
- **Rows 1–2.** C_x and C_x' depend on c_0, c_2, L, r and B̄.
- **Absolute constants, before κ.** These are a_FH, C_F and C_{F,α}. C_pot uses L, B_* and C_box.
- **Late constants, as the text states.** The ceiling C_G v <= r_𝔠 sits in the final γ (C_G depends on M_1). Lemma 9's W_win comes after κ and M. Theorem 10 places κ̄ at row 5, c_ct at row 6, and C_form before X_0. The consumer constant R_s carries κ̄.
- **Amendment 1.** Its floors (L > L_0♮ at row 2, κ >= κ_0♮(L) at row 4) only raise floors. They move none of these constants.
- No cycle was found.

## Unchecked or unfrozen notes and what depends on them

- **Theorems 2–3** depend on a3-derivative §§4, 6.1, 7.1. That note is unfrozen and gated ADVANCE with repairs (Finding 1). They also depend on the P81 chart (frozen ST1 Lemma 5, under A1/F0/REG).
- **Theorem 4's (5) and Theorem 10's (26)** depend on a2-full Theorems IV and V, which are unfrozen, with a2-full-gate D1–D3 and D1–D2. The bound H-prof itself (Theorem 4's first display) uses only D4 and frozen IN1.
- **Lemma 11** can rest on frozen ST1 alone (Finding 6). c1-repr §8 has been checked only by its author model, and it is not needed.
- **The b4-step Outstanding** quotes b4-step (19)–(20) exactly as stated (b4-step L580, L601). Lemma 8 itself uses no unfrozen note.
- **geoh-draft** is not used by cp12.
- **bx-fix (H)** is used only for the definition of its real clause.

## Verdict

cp12 proves what its Result paragraph (L656) says, and no more. M1 holds in the raw/counting convention, with the correct conversion (2) to cell weights. (15) holds on the admitted real layered class. The corrected H-prof and its repaired consumer hold. The fine-mesh real Hölder theorem FH holds with mesh-uniform constants. Lemmas 8–9 hold under D6–D7, and Theorem 10 under C1–C2. The DOM residual (L624–626) is stated correctly. Frozen ST1 (51)–(52) already supplies the value-ball continuation, so the draft's DOM-in-flat is not a new open input. Full DOM does not reduce to (28). The six findings are all repairable; none is fatal.

**The Outstanding marks are all correctly placed:**
- L163, literal H-prof: a conditional obstruction, not a counterexample. geoh D3 would make it vacuous above N_crit, but it would not prove literal H-prof.
- L412, b4-step (20) and the actual-family stop.
- L457, draft Lemmas 10.5–10.6 do not establish D7. All three listed failures are real. On the third: e^{−n} <= Cω_n fails when α log L > 1.
- L552, H-ct for the actual step: C2 on arbitrary subsets, the root double count and C3.
- L624, actual DOM.

**Against the assembly:**
- Item 1 (P82M) is closed conditionally on the stated imports.
- Item 2 (PRH, PR1(6)) stays open in actual form. Actual H-ct and literal H-prof are both not proved.
- Item 5 (DOM) stays open.
- PR1(4)'s clause (H) receives its real part only.

Checked line by line by Claude (fresh session).
