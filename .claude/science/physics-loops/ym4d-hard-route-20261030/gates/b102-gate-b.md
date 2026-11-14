lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T13:39Z

First failing step: none.

# Gate: `library/b102.md`, second half (H15–H25 and the Result), row 355 `b102-gate-b`

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, pinned at commit 242d44119 on `claude/ym4d-hard-route`. `b102.md` is byte-identical to the version gate-a read at 799a4acd0. Text by Codex (round 3, lines 1992–3630). One line-by-line reading by the other model. It is not an audit and grants no status. I did not write the text. No numerical run was used.

Scope read: `b102.md` §1 target (T1)–(T7) (36–160), the H2–H8 statements that round 3 reads (321–897), Lemma O (906–937), H9–H14 (1247–1895) as inputs, and all of §8 and the Result (1992–3630). Every step of H15–H25 was redone by hand, except as noted under "Not redone". Imports were checked for use as stated: `a1-balaban.md` §§3.5, 3.8, 3.9, 6, 7.2, 8, 9.1 (gate: ADVANCE); `flat-port.md` §4.1 (4.1), §9.2; `a3-balaban.md` (7.16)–(7.21); CA-I 13680–13979 (`4.5:lem-free-current-operators`), 14803–14869, 24239–24330, 35144–35199; CA-II 85845–85900; CA-III 35577–35624. CA-I, CA-II and CA-III were fetched at `31a47c543775` into a scratch folder. Their SHA-256 hashes match b102 §1 and §5 (lines 1156–1157). Balaban's text was read on printed pages rendered locally from `~/ym4d-papers` (nothing copied into the repository): CMP 102 pp. 279, 297–300, 303–309; CMP 99b pp. 396–399, 425–426.

Credit: T. Balaban for every operator, equation and estimate compared here. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account arguments that H16, H18 and H24 port.

## Findings (none breaks a statement)

**W1 (H18, lines 2560–2570: the Y→X_β bound for the two-constraint inverse (H18.9)). Repairable; the repair uses only H17–H18.** The text says "the gauge subtraction uses scalar inverse bounds". Read literally, that does not suffice. By G₁DR = DG'R and RD*G₁ = RG'D* (both proved at 2549–2559), the term is G₁DRD*G₁f = DG'R G'D*f. Its gradient member is a covariant Hessian of the scalar G'R(G'D*f). H17 states no such bound: its members are G∇*, ∇G∇* on Hölder data, the Laplacian, and the gradient Hölder seminorm. Repair (unproved here as text, each step checked): write the same term as G₁Dφ with φ = RG'D*f. Scalar H17 (lines 1–2) and (H17.5) bound |φ|₍₋₂₎ and every subunit Hölder seminorm by C|f|₍₋₃₎. Then N_β(G₁Dφ) ≤ C(|φ| + ℓ^ε[φ]_ε), by H17's mixed member for G₀ and the series (H18.6)–(H18.7). This is the mechanism H18 already uses for G₀Dφ in (H18.5). The series needs the current smallness ε = |J|₍₋₃₎ that H18 assumes. This matches Balaban: CMP 99b Theorem 3.13 (p. 426) gives 𝔊 = G₁ − G₁DRD*G₁ − G₁Q*(QG₁Q*)⁻¹QG₁ its bounds under (3.35) and (3.36). Consumers of this bound: (H20.2), (H21.2), (H23.2). Add the two lines at 2568.

**S1 (§1 lines 132–137; Result lines 3592–3593). Comparison with the printed paper. Repairable wording.** Printed Theorem 1 (p. 279) legibly reads "for 0 ≤ β ≤ β₀ = 1" in (9). b102 attributes its subunit restriction to damage in the OCR. The scan is clear. It reads as a misprint for β₀ < 1, for two reasons. B₄(β₀) is said to depend on β₀. CMP 99b (3.43) (p. 398) has 0 ≤ β ≤ β₀ < 1, with B₀(β₀) → ∞ as β₀ → 1. b102 proves β ≤ β₀ < 1 only (H21 line 3039, H24.11), and §1 says so. Repair: §1 should say that the printed endpoint is read as a misprint and is not proved. The Result's "(7)–(10)" should read "(9)–(10), for Hölder exponents below 1". (7) is the datum hypothesis and (8) is the space.

**S2 (Result lines 3588–3596 against printed Proposition 9, p. 309). Missing clause, immediate.** Printed Proposition 9 also asserts that ℋ(B) satisfies (19)–(21) with ε₂ = B₅ε₁ (see (173)). This includes the two second-order members of (19). The Result does not state this clause. It follows directly. (20)–(21) hold by construction in (H23.2). Value and gradient follow from (H23.3). The two second-order members follow by integrating the last two lines of (H24.12) along tB, with the sum over y' done by H15.5. Add one line.

**S3 (H23 lines 3220–3227, with the paragraph after H18 at 2588–2595). Sketch, not an error.** Analytic dependence on the external background under CMP 99b (3.35)–(3.38) is a printed Proposition 9 clause. b102 argues it at sketch level ("absolute values and absorption"). I found no error. I did not redo the complex-background versions of H9–H17. The Result calls this "stated in H23", which is accurate. (189), (190) and CA-II 8.4 do not need it.

**W2 (H24 lines 3277–3289).** The "explicit accounting" lists the last two of the eight (H6.6) terms in swapped order. In (H6.6) the seventh term is −(∂_vJ_D)*H*V₀'(T), of size r². The eighth is T'*V₀''(T)[T'v], of size r. The sizes and the sum CrN^ρ(v) are right.

**W3 (H25 line 3445).** "g=u e^H,quad" lacks a backslash.

Not redone (read at the depth stated, no defect seen):
- H19 ports `a1-balaban.md` §3.8. I checked that (H19.2) is a1 (3.15) and that H11–H12 and H17 supply it. I re-derived (H19.5) and the uniqueness/coverage step. a1's own perturbation estimates were read at sketch depth in its gate; I did not re-derive them.
- H21's one-step seam construction (2884–2938) I checked as finite combinatorics: each pivot is read by one row, the row derivative is L⁻³Ad T_c, the inverse norm is 2L³, and the contraction ball holds. I did not draw every corner case with one to three outer blocks.

## Verdict

| Statement | Verdict | Checked |
|---|---|---|
| H15 Gram inverse, lift | ADVANCE | (H15.6) conversions B† = Q*ℓ⁻³, Γ₀ = ℓJ₀ℓ⁻³, H₀ = G₀Q*J₀⁻¹ℓ⁻¹. \|B†e_c\| ≤ Cℓ_c⁻³ from (H9.2): pillar multiplicity up to n. Middle-face pivot coefficient L⁻³ in the counting row. Saddle Schur complement −Γ₀ and Gram gap via the H12 parametrix. Kernel of J₀⁻¹ matches (3.132) as fixed in a1 §3.9. |
| H16 second averaging derivative | ADVANCE | Cauchy on one kernel entry. Transpose (H16.3) and weighted bound (H16.4). D''(0) = C''(0) and four-factor telescoping for D₃. Import (H16.1) is a1 §3.5's kernel bound C₃r s^{1−d}. |
| H17 differentiated sources | ADVANCE | All four members match CMP 99b (3.42)–(3.45) (pp. 397–398). flat-port (4.1) applied per component in a small local gauge. Absorption and product rule redone. (H17.5) equals (3.49) up to an absorbed scale ratio. |
| H18 invariant lift, corrected inverse | ADVANCE (W1) | Second-order gauge invariance gives ΔDλ = 𝔨_J(λ) and D*ΔD = −𝔪_J, so E_π = −Θ'_J and G_π = CA-I's G^J_π. Checked RD*S = 0, G_iDR = DG'R, RD*H_i = 0, both constraints of (H18.9), and the inverse characterization. (H18.10) = printed CMP 102 (137). Energy positivity on ker 𝓑 ∩ ker RD*. |
| H19 gauge chart | ADVANCE (port; see "Not redone") | |
| H20 critical chart | ADVANCE | (H20.2) from the tangent-space characterization; the quadratic part on the slice is Δ₁. (H20.4) from D*Δ = 𝔧_J. (H20.6) = printed (138)–(140). P₀*L₀ = L₀P₀. (H20.8) = printed (143) with G̃ = GP₀*. |
| H21 reset, induction, cubes | ADVANCE | (H21.1) = printed (160). (H21.3) = (161) with 18d³L³B₀. B₃ as in (162), R₁M₁ as in (163), (H21.5) = Proposition 8. At reference one H = H₀. The protected-collar class (E, e) persists, so there is no C↓ᵏ. Cap M(ε₁) = R₁M₁a₁/ε₁ as printed. |
| H22 minimum | ADVANCE | (H22.2) from (H16.2) with sign-aligned directions. The segment bound (H22.4) gives a minimum over the whole regular class. This is stronger than printed (142), which notes only a positive Hessian. |
| H23 analytic branch | ADVANCE (S3) | ker 𝓑 = T ⊕ D ker Q' and D*J = 0 give P₀*J = 𝒢₁J = 0. (H23.4) has the form of (176)–(177). |
| H24 (189), (190) | ADVANCE (W2) | (H24.2) = printed (189) at rate δ₀/4. (H24.4)–(H24.5) = (180), (182)–(184). (H24.7)–(H24.9) redone. (H24.12) matches the five members of printed (190) (p. 308): ℓ⁻¹, ℓ⁻², ℓ^{−2−β} with unit-scale cutoff, ℓ⁻³, ℓ⁻³, times ℓ_{y'}⁻⁴e^{−δ₀d/8}. |
| H25 orbit extension (181) | ADVANCE (W3) | Three-lines bound on 0 ≤ Re z ≤ 1. Polar decomposition in SL(2,ℂ). Well-definedness on G^c𝒟. |
| Result vs printed Theorem 1 | ADVANCE (S1) | For d = 4, the fixed group and Hölder exponents below 1: existence, uniqueness for B₃ε₁ ≤ ε₀ ≤ a₀, cube class, (9)–(10). |
| Result vs printed Proposition 9, (189)–(190) | ADVANCE (S2, S3) | |

H15–H25 hold as written, after the two-line addition W1. They are implications from H1–H14 (gate-a: first failing step none), FP1 Lemma 8, flat-port §§4, 5, 8, 9, P82 Lemma 5, a1-balaban §§3.5, 3.8, 6, 7.2, 8, 9.1, and a3-balaban (7.16)–(7.21). The Result proves Balaban CMP 102 Theorem 1 (without the printed endpoint β = 1, read as a misprint), Proposition 9, (189) and (190). This holds in four dimensions for the lane's group, uniformly in depth, fine spacing, volume and admissible nest, with constants chosen in the stated order. It covers what CA-I 4.9 and CA-II 8.4 quote. No fabricated step was found. Every cited printed equation, account line range and library location that I opened says what b102 says.

**Gate-a's scope note S1 answered.** From CMP 99b Theorems 3.1–3.3, H15–H25 read only members that H13 and H17 prove. These are: value and gradient (O2); G∇* and ∇G∇* on Hölder data and the gradient Hölder seminorm (H17 lines 1–3, used in H18.5–H18.6, H21 and H24.10); and the covariant Laplacian of G₀ on Y forces only (H17 line 4, used in H20.8 and H24.8). No Laplacian member is read for G_π, G₁ or 𝒢₁, which matches the exclusion in CMP 99b Theorems 3.12–3.13 (p. 426). The second-order members for H and for the response come from the Ward identity and the alternative Euler equation, as in printed CMP 102 (137)–(140). (3.46)–(3.47) are not read; H15.5 does the sums.

Checked line by line by Claude (Mini worker).
