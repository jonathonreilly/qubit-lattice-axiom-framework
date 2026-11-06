lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T12:38Z

# Check of library/ol.md round 4 (OL-transfer)

First failing step: none.

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout 58c890225, 2026-11-06. One line-by-line reading by one model. This is not an audit and grants no status. No numeric job was run, and no step below rests on a computation.

Moves: row 339. This is the Gaussian supplier of CA-I 4.2:lem-one-loop, which the account states with its proof incomplete at one step (CA-I 56361-56368). It feeds hypothesis (b) of 4.19:prop-clause-zero and the absolute interval bound read by CA-II 5.14:thm-one-loop-law. If OL-transfer stands, Lemma 4.2(b) no longer waits on OL-W0-CA, the bound for the account's own walk assignment. If it fails, it does.

Kind: a check of our own new text (Codex, round 4). It is not a check of their proof.

Scope. I read §§15-19 and the Result (ol.md 2204-2845) line by line. For the inputs that round 4 retains, I read the statements and checked only that round 4 quotes them correctly: §2.1-2.4 and §3 (lines 70-493), §7 through (7.10) and (7.15) (612-915), §8 (1139-1410), the round-2 endpoint (1463-1571), §§10-11 (1572-1853), and §14 with the round-3 endpoint (2069-2203). I did not recheck their proofs.

Sources. CA-I and CA-II at 31a47c543775 were fetched by URL into /tmp/olgate-src. Their SHA-256 values match ol.md §20. I read these passages:
- CA-I: 540-680, the Wilson action definition, 1380-1540, 3588-3615, 3722-3762, 3764-4115, 4869-4910, 5519-5580, 5910-5955, 6095-6135, 6215-6650, 6820-6970, 9630-9800, 56355-56485 and 58700-58995.
- CA-II: 27042-27130.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the cell-resolvent lemma, the logarithm rule and the polarisation-limit argument that round 4 reuses. Tadeusz Bałaban, for the RG step and the coefficient convention.

## Findings (one defect, repairable)

**D1. Lines 2716-2724 (§19, "Order of choice"), with line 1679 (§11.1, "These choices precede κ, M"). The order is wrong. Repairable, not fatal.**

What is wrong:
- Round 4 fixes, in order: §11's operator choices (these include M_1 and R_1, line 1677), then s, r', ℓ, then κ, then M.
- The account fixes κ at Stage 3. Its floors read only d, Stage-0 numbers and L, and none reads M_1 (CA-I 1473-1489).
- It then fixes κ_1 ≥ max{16κ+1, 4Lκ+1} at Stage 4. At Stage 5 it fixes M_1 with δ_1 M_1 ≥ c κ_1, then the kernel constants, r' and ℓ (CA-I 1490-1520). M comes at Stage 6.
- So in round 4's written order, the account's floor on M_1 reads κ before κ is chosen. This is a cycle in the order of choice.

Repair (unproved, but checked against every use of κ in §§17-19). Round 4 reads κ in only three places:
1. the entropy margin κ/2 ≥ κ(d) of CA-I (g1), line 3742, which reads only d;
2. the factor e^{4κC_h} in E^♮ (line 2450);
3. the M-floor 4κC_h/(LM) ≤ θ/2 (line 2443), which is a Stage-6 condition.

So the order can be fixed without changing any constant:
- Take κ at Stage 3, where the account puts it.
- Put §11's floors on M_1 and R_1 at Stage 5, after κ_1. They are free upward and read only L, N and the early operator data.
- Then fix §11's B_u, δ_u, ρ_u = O_L(M_1) and the radii r_A, r_J.
- Then fix s, r' (by (k1)) and ℓ (by (k2)). This is the account's own Stage-5 position for r' and ℓ.
- Fix M at Stage 6.

Line 1679 should read "precede M", not "precede κ, M". Under this order, E^♮ depends on M_1, r' and ℓ. That is allowed, since Lemma 4.2(a) lets E^♮ and κ depend on L, N and p. The constant c_2 is still fixed at Stage 2 and does not move.

**Remark (breaks nothing).** (18.2), line 2529, asserts that each N^u term is invariant under constant colour conjugation. The reason given is that "each unfolded local matrix transforms by the same conjugation". The note asserts this without deriving it from §11's construction. It is true there, because every operation in §11 is equivariant under a constant g: Ad(U(b)), commutators, group means, logarithms, inverses, Neumann series, scalar cutoffs and tents. Also, the claim is not load-bearing term by term. (18.7) needs only the total version, Σ_{X,z} DN^u(X;P_∘,z) = DF_k(P_∘) = 0, which follows from the colour covariance of A_k and J_c. This is also how the account argues at CA-I 58823-58836, using G^c-invariance.

## c_0 against the account's normalization

Verdict: CORRECT. The value c_0 = (11N^2/(12π^2)) log L in the Result is the account's c_0 (CA-I 634-636, 3897-3899, and 1416-1421 at Stage 2; CA-II 5.14 line 1). It agrees with the textbook coefficient as follows.

1. The bare density is exp[-g_0^{-2} Σ_p (1 - Re tr U(∂p))] with tr 1 = 1 (CA-I 1.1:eq-wilson-action-2, -4). The usual Wilson form is β_W Σ_p (1 - N^{-1} Re Tr U_p) with β_W = 2N/g_std^2, where Tr(T_a T_b) = δ_ab/2. Since tr = N^{-1} Tr, the account's x = g^{-2} is β_W. So g^{-2} = 2N g_std^{-2}.
2. Textbook: μ dg_std/dμ = -b_0 g_std^3 with b_0 = (11N/3)/(16π^2). So d(g_std^{-2})/d log μ = 2b_0 = 11N/(24π^2).
3. Hence d(g^{-2})/d log μ = 2N · 11N/(24π^2) = 11N^2/(12π^2). One step changes the scale by L, which gives c_0 = (11N^2/(12π^2)) log L. For N = 3 this is 33/(4π^2) per unit log, the known one-loop running of β_W = 6/g^2.
4. The account's own route gives the same value. The basis t_a = sqrt(2N) T_a is orthonormal for <X,Y> = tr(XY). In it the action is (1/(4g^2)) Σ_x Σ_{μν} F^a F^a, and d(g^{-2})/d log μ = 11C/(24π^2), where C is the Casimir in that basis. This expression does not change when the inner product is rescaled.
   - ol.md §2.1 derives C_g = 2N^2 from Σ_a (t_a)_ij (t_a)_kl = N δ_il δ_jk - δ_ij δ_kl. I rechecked that identity.
   - I also rechecked Σ_a t_a^2 = (N^2-1)1, Σ_a [t_a,[t_a,X]] = 2N^2 X, and (2.2), Σ_{i<j} λ_ij^2 = N^2 for t = sqrt(N/2) diag(1,-1,0,...).
5. The extractor gives b[g^{-2}A] = g^{-2}. For the unit-lattice Wilson action and μ ≠ ν, the bond Hessian Π_μν(u) is +1 at u = -e_μ and at u = e_ν, and -1 at u = 0 and at u = e_ν - e_μ. Only u = e_ν - e_μ has u_μ u_ν ≠ 0, so Σ_u u_μ u_ν Π_μν(u) = (-1)(-1) = 1. Thus β^0 is an increment of x = g^{-2} in the same units. With x_{k+1} = x_k - β_{k+1} (CA-I 1.2:eq-couplings-1), β ≈ c_0 > 0 has the asymptotic-freedom sign.
6. The colour factors in the §2.3 table are spin 4C_g, four orbital directions -2/3 C_g and ghost +1/3 C_g, for a total of 11/3 C_g. This matches the textbook split 4 - 4/6 + 1/3 = 11/3. Then I_2(z) = (16π^2)^{-1} log(1/z) + O(1) with z = η^2 gives 11C_g/(24π^2) per log(1/η), and log(1/η) = k log L.

The constant c_2 also agrees with the account's. CA-I 4002-4006 sets c_2 = C_det + C_cmp/2. ol.md (3.14) sets c_2 = C_E + C_R + C_M, with C_cmp = 2(C_E + C_M) and C_R in the role of C_det.

Notation only: row 339 writes "k c_0 log L" with c_0 = 11N^2/(12π^2), so there c_0 is the per-unit-log coefficient. In the account and in the Result, c_0 already contains log L. The Result's k (11N^2/(12π^2)) log L is the account's k c_0, so there is no factor error.

## Line-by-line record of round 4

**§15 (2204-2253).** Every consumer row matches its source.
- CA-I 3808-3828 sums the pointed Hessians over all domains and base points before taking the moment.
- CA-I 3867-3879 applies the construction to the functional alone.
- CA-I 4875-4907 defines a walk system by its sum.
- CA-I 56361-56368 and CA-II 27042-27130 read only the numbers β^0_l, including the absolute bound 2c_2.
- The scope statements are honest: there is no termwise identification and no replacement inside the non-Gaussian expansion.

**§16 (2254-2313).** (16.1) is (7.8). I rederived (16.2) from R_w = -R A_w R and Jacobi's formula, and it holds. The section correctly claims only equality of the finite-volume observable. It is not used later.

**§17 intro and §17.1 (2314-2412).**
- Collar (2326-2333). Enlarging step domains can only lower d(ω;b,b'), so (17.1) persists. The collar supplies the two properties of (W') that the CA proof uses beyond the bounds: the kernel lies at distance ≥ 1 inside |ω|, and footprints have connected interiors (CA-I 6575-6580, 6617-6619).
- (17.2). On the balanced polydisc, a radial Cauchy estimate gives |f(t) - f(0)| ≤ a_ω Σ_{n≥1} s^n = a_ω s/(1-s). Summing gives (8.1).
- Positivity. The flat bound is A_k(P_∘) ≥ c_L (7.15). The far part has norm ≤ c_L/8, so the near part is ≥ 7c_L/8. The local perturbation is ≤ c_L/8, so every cell matrix satisfies Re T_X ≥ 3c_L/4 ≥ 7γ_*/8 with γ_* = c_L/2. On global data, Re A_k ≥ 7c_L/8 ≥ γ_*, and γ_* ≤ B_u follows.
- (k1) and (k2) are as in CA-I 6119-6128. (k1) alone already gives ε(r') ≤ c_L/16.
- I checked the CA proof (6312-6650 and 6827-6963). It reads only the range r, the datum-free Schur majorants, the cell bound Re T_X ≥ 7γ_*/8 and (k1)-(k2). This is as §17.1 states.
- (17.3) is the CA's clause (ii), with c = γ_*/2.
- The proof bounds each factor P_q, B_q and far step by a datum-free majorant, so the "abs" form (sup inside the sums) also holds.
- Clause (i) gives Σ_ϖ R_ϖ = (λ + A^Y)^{-1} on global data.

**§17.2 (2413-2491).**
- (17.4) is CA-I 9707-9757 with λ_0 = c, and log a - log c = ∫_0^∞ (a-c)(λ+c)^{-1}(λ+a)^{-1} dλ.
- (17.5): the bound per root is (N^2-1)(B_u+c) · 4S ∫_0^∞ (λ+c)^{-2} dλ = 4(N^2-1)S(B_u+c)/c. The factor 1/2 cancels against the two vacuum evaluations.
- The pivot bound h_N/3 is (7.10).
- (8.5)-(8.7) convert e^{-θD/2} ≤ e^{4κC_h} e^{-κ d(X)} once 4κC_h/(LM) ≤ θ/2. This gives (17.6) with E^♮ free of l and of the volume.
- Raw radius: |a| < s r_A η^2/4 gives |A'| < s r_A and |∇^η A'| < s r_A/2, so a_l > 0. Only a_l > 0 is used, as CA-I 3909-3914 allows.
- Common lifts hold with compatible grids. The whole-lattice terms are absolutely convergent sums of local terms.
- (17.7): summing over roots and hulls gives -1/2 [log det A_k(P) - log det A_k(P_∘)] on the accretive branch. Adding the pivots gives (7.8).

**§18.1 (2492-2570).**
- (18.2): an Ad-invariant linear functional on sl_N vanishes, because sl_N = [sl_N, sl_N]. Per slot, the derivative at the fixed point P_∘ is Ad-invariant. See the Remark above.
- (18.4) is CA (4.38:eq-polarisation-limit-1).
- (18.5): with a = (1/4) min{μ_l, κ/M} and (g2), a(d(x,z)+d(y,z)) ≤ (μ_l/4)(d_x+d_y) + (κ/2) d_l(X) + 4ac_dM.
- (18.6): wrapping domains have d_l > s_T/(4M) - 2 by (g3). Dominated convergence applies.

**§18.2 (2571-2643).**
- (18.7) is a finite sum on the torus, together with (18.2).
- (18.8): the centered-lift tail bound is uniform in T, and (18.6) handles the finitely many remaining lifts. Pointed translation covariance is not needed, so this replaces CA-I 58969-58987 correctly.
- (18.9) uses d(x,z) + d(y,z) ≥ d(x,y). (18.10) holds.
- Dependence only on x - y, reality and hypercubic covariance pass from the finite-volume Φ_{l,T}, through (18.8), to the limit.
- The Hessian of the total does not depend on the gauge representative, so the pointed tensors may depend on it without affecting the result.
- (18.11) is CA (increment-1)-(increment-3) applied to N^u.

**§18.3 (2644-2668).** Any admissible localization of Φ_{l,T} gives the same limit of H_{l,T}, and hence the same coefficient. The section correctly declines to infer a value for an unjustified family.

**§19 (2669-2741).**
- (19.1)-(19.2) follow from (18.11) and (3.3).
- (19.4) follows by subtraction and gives exactly the two-sided form that CA-II 5.14 reads.
- The scope sentences are honest: lem-unmarked, the full increment and OL-W0-CA remain separate.
- Order of choice: see D1.

**Result (2813-2845).** It matches §§16-19. Its scope statement is accurate.

## Verdict

**OL-transfer: ADVANCE, as an implication.** For every l ≥ 1, N^u_l is an admissible localization of Φ_l = F_{l-1} ∘ U_l in the sense of CA-I 3907-3914 and 3935-3938. The coefficient that CA (increment-1)-(increment-3) produce from it equals the second moment of lim_T D²Φ_{l,T}(0). It is therefore independent of the assignment, and β^0_l = b[Φ_l]. With round 1's (3.3) and (3.14), this gives |Σ_{l≤k} β^0_l - k c_0| ≤ c_2(L,N) and the interval bound 2c_2. The coefficient consumers at CA-I 3808-3828, 3876-3879, 3603, 56361-56368 and CA-II 5.14 read only these numbers, so they can use N^u. This holds after repair D1.

What this does not show:
- Inputs not rechecked here. The verdict holds only given them:
  - §11's depth-uniform bound B_u for the unfolded family (round 3), and through it p82, pw, rows, hm and piv;
  - §7's identification (7.6)-(7.8) and the flat gap (7.15) (round 2);
  - §8.3's physical admission (mu) and the fixed-depth response (18.1) (prefactor-loc);
  - the bulk calculation of §§2-3 (round 1), including the identification of the magnetic jet with b in (3.13).
  Rounds 1-3 of ol.md and mu are, as far as I can tell, not yet refereed by the other model.
- It is not Lemma 4.2(a) for the account's own family. The full increment β_j, β^A_j and 4.2:lem-unmarked still read the account's localized family, so its bounds (W', OL-W0-CA at the trivial nest) stay open wherever the full increment needs them. The note says this itself.

Checked line by line by Claude (Mini worker).
