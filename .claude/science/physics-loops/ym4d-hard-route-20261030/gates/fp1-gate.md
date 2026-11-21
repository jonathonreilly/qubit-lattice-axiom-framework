First failing step: none.

# FP1 pass-3 referee report (`library/fp1.md`)

Provenance: Claude Opus 5.5 (claude-opus-5-5), fresh session, 2026-11-05. One reading by one other model of a Codex distillation. This is not an audit and grants no status.

Read for the comparison: `library/fp1.md` (whole); `library/flat-port.md` §§2.1, 3 (displays), 6–7 and 10; `gates/flat-port-gate.md` (whole); `gates/share-check-199fac1cb.md` header, §(a) and §(c), which check `seam-quadratic-c.md` and `lattice-uhlenbeck.md` with `lattice_sobolev_box_gauge.md` §1; the defect lists of `gates/fan-ext-73b09692a.md` and `gates/fd-local-00f9df685.md`; `library/in1.md` row 2 and its F8 floor; `library/ym4-assembly.md` §4 (FP1 line) and §5 (FP1 entry). Outline `sa/ym4.tex`, whose SHA-256 `d7f77d4d…` matches the hash in the text's source record. I read SA 960–1050 (Combes–Thomas), 8866–8960 (WI7–WI14) and 9196–9365 (FX8–FX20) in full, and the tag lists of 605–1149 and 8396–9583.

## What I checked

Each numbered statement against its proof, and each against its source note, gate and outline passage.

- **Lemma 2.** Q^*u = u(B) under the stated pairings, so QQ^* = I. Neumann path eigenvalues 4sin^2(πj/(2m)); first physical gap 4m^2sin^2(π/(2m)) ≥ 4. φ_m has mean one (roots of unity), QT = I, endpoint factor ≤ π^2η^2/4. ‖u‖^2 = ⟨A_s^{-1}Q^*u, A_sTu⟩ gives c_s = C_s^{-2}. The plain-coordinate remark (entries η^2; Q̄Q̄^* = η^4I) is correct.
- **Lemma 3.** The edge identity; |a|,|b| ≤ e|t|η; |a+b| ≤ et^2η^2; four incoming bonds; block ℓ^1-diameter ≤ 4; Schur 4e^4|t|. C_s' = 8e+4e^4 and t_s = min(1,(4C_s')^{-1}) give inverse norm ≤ 2 and (7). This is SA 960–1050 step for step. The compression argument is correct.
- **Lemma 4.** S_nd = d_nq_n; σ(df) = q_Lf − r_Lf; P_Ld = d_Lr_L. The induction gives ψ_k = r_Lψ_{k-1} − σ(S_{n'}·). Both fibre directions are correct (W2 of the flat-port gate). C_n has row sum n^2 and column sum n^{-2}. I_2 has row and column sums n^{-2}, n^2. I recomputed a_0 = (3n^2+1)/(4n^2) and a_1 = (n^2−1)/(8n^2) from the overlap counts. The symbol lies in [½,1], so ‖𝒯_n^{-1}‖ ≤ 16 and E_k ≤ 256‖da‖^2. This matches SA WI7–WI14.
- **Lemma 5.** The pivot has coefficient L^{-3} in its own row (all L longitudinal positions on the central line) and in no other row or contour. So P_Lh_0 = I, ran J = ker P_L and ‖Ju‖ ≥ ‖u‖. The null-vector argument holds at every phase, p = 0 included. The upper bound holds: ‖d‖^2 ≤ 24, GJ = Gι, ‖G‖^2 ≤ CL^5.
- **Lemma 6.** s_{μ,n} is the Fourier filter of S_n. n^{-4}|s|^2/λ = f/s_{n,m}, so D_{μ,n} = Σ_m f/s. The curl minimum equals the scalar minimum over coarse gradients, both ways. (12) is the scalar completion of the square. I verified Σ_μt^+t^-/f_μ = s/Q_0, h = 1/f − sRh/f, (t^-)^TD^{-1}t^+ = s^2𝒥 and (13). The alias bounds are correct. This matches SA FX8–FX20.
- **Lemma 7.** Contour shift; image sums; simultaneous unitary diagonalisation of commuting adjoint holonomies; the conjugated Schur bound and inverse series for A_F. All correct.
- **Lemma 8.** Q_cDλ = s_c^{-1}(Av_{c+}λ − Av_{c-}λ). The inward-bond counterexample and the column bound (15) with (1−L^{-3})^{-1} are correct. For the single-scale part I checked: q_{μ,ℓ}; Σ|q_ℓ|^2 = 1; |q_0| ≥ (2/π)^4; I−R is the projection onto q̄/ω; the energy (16); ‖W^{-1/2}g‖^2 = B; Qz = (e^{iϑ}−1)B; the O(|ϑ|^6) high-alias bound; and the 2ab step giving −C|ϑ|^8|A_0|^2. For the two-scale part I checked: R = R_s+R_+ by orthogonality of the H' minimiser; the decomposition (qa = 0, R_sD^*a = 0); HD_1ω = DH'ω by uniqueness; ΔH'ω = R_+D^*(A−A''); pillar Poincaré. The B_ax counts (3L, 4d+2 = 18 segments, d(4d+2) = 72 rectangles, CL^5 and 2L^3, 4L bare bonds) agree with `flat-port.md` (7.1)–(7.2) at d = 4. This matches flat-port §§6.1–6.2, 7.
- **Lemma 9.** Mean of β on its block is 1. Means of Λ are 1−2g and g, and g < 1/8. ζ reproduces 1 and t. Δ Σ_{y≥y_0+B}ζ_y = η_{y_0}. hd = I−T^0R^0, dh = I−T^1R^1, R^0h = 0, and the circle case holds. Row and column sums: all ten values correct. I recomputed the six component norms: 24B^2(222+32√6+24√2) < 8024B^2, and ‖T_2‖^2 ≤ 324.
- **Lemma 10.** Reflection identity (19) with the boundary term. Sobolev: ‖w‖_{4/3} ≤ ∏‖d_iw‖_1^{1/4}; ‖u‖_4 ≤ (3/2)‖∇u‖_2. Every component a_μ is odd in its own direction, so it has mean zero. (20); the error bound ‖E‖ ≤ CX‖f‖; ⟨f,[w,f]⟩ = 0; no first crossing of X_0; X ≤ 2Θ in the limit. Unit-cube seed (32 links, ≤ 3 plaquettes); growth gives X_init^2 ≤ 3X_old^2 + CΘ^2. This is share-check §(c), seed repair included.
- **Lemma 11.** C_nG = 0 from equal parents. S_BZ = 0. P^{[k]}X_D = v by (9). (23) is the shifted product rule. The commutator constant 24 holds, since each bond appears in 3 commutator terms. ‖S_B(χH)‖^2 ≤ 4‖H‖^2/(r^2B^2). 48+2·324·24·4 = 62256, c_R < 5·10^8. The shell containment and its rounding margin hold. The Young optimisation gives (22). This is share-check §(a).
- **Theorem 1 against `ym4-assembly.md` §5 FP1(a).** Clauses 1–4 match: gap c(L) ≤ A ≤ CL^8, factor 256, kernels with periodisation and holonomies, level-0 seam, U and LC, scalar block estimate. Imports: none, as in the assembly. FP1 states the domains (U real and small-energy; LC on the unrestricted flat fibre; Hölder at current scale). These are the restrictions the gates impose, not new ones.

## Findings

1. **L148, Lemma 4 source.** "SA 8396–8664 and 8776–9060 (CF/WI and FX1–FX3)". FX1–FX3 ("The two constrained minima are equal") are at SA 9081–9128, outside both ranges. That range lies inside Lemma 6's 9060–9583. Not fatal; citation. Repair: "8776–9128".
2. **L183, Lemma 5 upper bound.** Schur with row bound CL^4 and column bound CL^3 gives ‖J‖^2 ≤ CL^7. The stated CL^8 is true, not sharp. The absolute row sums of P_L are in fact ≤ 3L (≤ L for S_L, ≤ 2L for d_Lσ). No effect on (10). No repair needed.
3. **L191–L196, Lemma 6 notation.** The letter s names the straight filter s_{μ,n}, the alias denominator s_{n,m} and s = s_{n,0}. h names the pivot offset in D3 and the fine spacing in Lemma 8. Not fatal; wording.
4. **L408, Lemma 10.** "A bondless point needs no gauge estimate" lies outside D7, which requires n_i ≥ 1. Not fatal. Repair: delete the sentence, or admit n_i = 0 in D7.
5. **L50 and L247, scope of the Hölder clause.** At current scale the denominator of a local Hölder quotient is at least one. The clause therefore follows from the kernel bound. This agrees with the assembly's "in scale units". It is not a fine-mesh Hölder estimate, and FP1 says so. A consumer that needs Hölder continuity of fine-mesh potentials (for example PR1's clause (H)) cannot cite FP1(2) for it. Not a defect; scope.
6. **Assembly bookkeeping.** `ym4-assembly.md` §5 FP1(d) lists the brick one-jump and several-jump checks (73b09692a, 00f9df685) as part of FP1's status. FP1's Theorem 1 does not use them. It marks the brick-chart identification (D3) and the lateral closure of consumer families **Outstanding**. These items should not count toward FP1's [C]. Not a defect in FP1.

## Verdict

FP1 holds as written. Every numbered statement is proved exactly as stated, with no import from another assembly part. Every constant and index rechecked here is correct: 1/4, 4, 2π^2, π^2η^2/4, 8e+4e^4, a_0, a_1, 16, 256, L^{-3}, 24, (2/π)^4, (2/π)^5, O(|ϑ|^6), (1−L^{-3})^{-1}, c_H, 324, 3/2, 62256, c_R. The gate corrections W1–W3, the LC restriction, the seed repair and the brick qualifications are carried in. Findings 1–4 are citation and wording only. Findings 5–6 are scope notes for consumers and for the assembly.

Checked line by line by Claude (fresh session).
