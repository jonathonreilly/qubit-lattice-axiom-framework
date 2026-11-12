# Check of library/gap-tomboulis-read.md (FINISH row 799), by Claude Opus 5.5

- Target: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-tomboulis-read.md`, 879 lines, read in full.
- Clone commit: `612d615f6` (`git -C /Users/jonreilly/ym4d-lead/clone rev-parse --short HEAD`).
- PDFs: fetched once with `curl -sSfL` into the new empty directory
  `.../scratchpad/tomb-pdfs.clx4MX/`. Nothing in them was executed. A local PDFKit
  tool (written in a separate directory) extracted text and rendered pages to PNG;
  equations were read from the rendered images.
- Pages read (printed = PDF page numbers for all five):
  - Tomboulis 0707.2179v1: pp. 5, 11, 12, 13, 14, 15, 19, 25, 26, 27, 28, 35, 36, 43, 44, 45 (images); other pages only by text search.
  - Kanazawa 0805.2742v3: pp. 4, 5, 9, 10, 11, 12, 13, 14, 15, 16 (images).
  - Ito–Seiler 0803.3019v1: pp. 6–8 and 12–18 (extracted text).
  - Tomboulis reply 0712.2620v1: pp. 1–6 (extracted text).
  - PoS Confinement8 020 (downloaded without sign-in): p. 1 (text), pp. 7, 8, 9 (images).
- Not read by me, so the note's claims about them are UNCHECKED here: 0711.4930, 0901.4246,
  0710.1894, Kanazawa v1/v2, Ogilvie, Cheng–Tomboulis, Grady, Schierholz, the MPLA article,
  and all repository cross-references in §§5–6 of the note.
- No numerical run was made. Every verdict below rests on the PDFs and on hand arguments.

## A. READ claims against the PDFs

**A1. Appendix C (C.1)–(C.12) and V.1 (5.17).** The note's transcription of (C.6) matches
p. 44: Ψ = h(α_h(t),t) + (1−λ)Φ⁺(α⁺_h(t_I)) + λΦ⁺(α_h(t)) − Φ⁺_{Λ(n−1)}, with Φ⁺ from (C.5).
(C.8) is t_λ = −Ψ_λ/Ψ_t (p. 45). (C.9) is printed as
Ψ_t = [−(h_α + λA⁺)/(h_α + A) + 1] h_t < 0 "by (5.15) and since h_t < 0". (C.10) is
Ψ_λ = Φ⁺(α_h(t)) − Φ⁺(α⁺_h(t_I)) > 0 "by (C.4) and IV.5". T then concludes that t(λ) increases
and "extends to the solution t(1) > t_0". The p. 45 text states the sufficiency claim: if
Ψ_t ≠ 0 along the branch, existence of t(1) is guaranteed by basic existence theorems. No
bound keeping t(λ) inside [t_a, t_b] (the finite interval of (3.18)) is given. V.1 (p. 27)
defines α* through t^{(n)} of (5.14), and p. 26 says the solution of (5.14) exists "as shown in
Appendix C". So (5.17) rests on Appendix C. The note's reading is accurate. **HOLDS.**

**A2. p. 19 and footnote 8.** p. 19 says MK flow for SU(2) reaches strong coupling "by explicit
evaluation" for all β and d ≤ 4. It then says the choice r = 1−ε is irrelevant for the flow
because, for SU(2), the point is "a structurally stable point of the iteration". Footnote 8
says this matters where the point is not structurally stable, "e.g. in U(1)". No proof is
given. Kanazawa v3 p. 13 makes the same complaint ("neither analytical nor numerical
evidence"). The note's label ASSERTED is right. **HOLDS.**

**A3. (2.13), (A.4)–(A.5), the plaquette count and the "more bonds" remark.** p. 5 prints
Z ≥ (1 + Σ_{j≠0} d_j² c_j⁶)^{|Λ(n)|}. p. 35: the reflection halvings give (A.4) with a
single hypercube h on the right; the halving argument produces one factor per elementary
hypercube, i.e. per site. After (A.5) the text says that, since the number of bonds exceeds
the number of plaquettes, |Λ(n)| in (A.4) may be replaced by the latter. p. 36 §3 then says
"Let |Λ(n)| denote the number of plaquettes". In d = 4 a periodic lattice with V sites has
4V bonds and 6V plaquettes, so the remark is false, and replacing V by 6V strengthens the
bound (base > 1). The note's reading is accurate. **HOLDS.**

**A4. (5.6) warning.** p. 25 states |α⁺ − α| ≤ O(1/|Λ(1)|) and then warns that a discrepancy
of that size makes the bulk factor in (5.2) contribute as much as the ratio factor. The
note's statement "T explicitly warns against discarding the factor" is accurate. **HOLDS.**

**A5. Kanazawa v3 Theorems 1, 3, 4 and Appendix A.1.**
- Theorem 1 (p. 4): H is "an arbitrary discrete subgroup of U(1)" for G = U(N), and H = Z_N for
  G = SU(N); A^g > 0 arbitrary; 0 < α < λ({c'}); |α − ᾱ_Λ| ≤ O(1/|Λ|); identity (5). The note's
  "a finite subgroup H of the center" is loose for SU(N), where the theorem fixes H = Z_N.
  The note writes C/|Λ_c|; for fixed n this is equivalent. Minor wording only.
- Theorem 3 (p. 9), (38): two parameters differing by O(1/|Λ(n)|); stated as a special case
  of Theorem 1. Matches the note.
- Theorem 4 (p. 15): compact connected Lie group, r = 1 − 1/b², b ∈ N large depending on
  the initial coefficients; c_j(n) → 0. Proof pp. 15–16, (40)–(48), via the Müller–Schiemann
  inequalities (42)–(43), quoted not proved. p. 16 says it holds "both for abelian and for
  nonabelian theories". Matches the note, including U(1) and the choice of r.
- Appendix A.1 (pp. 10–14) lists four points: continuation (with the counterexample family
  Ψ = λf + (1−λ)g, f and g both strictly increasing, f = 0 unsolvable, g = 0 solvable; p. 11),
  the modified flow, the abelian/nonabelian location, and whether r is needed at all (p. 14,
  labelled the author's "guess"). The note's summary of A.1 is accurate. The specific example
  e^{−t} − 1 + 2λ is not in Kanazawa v3; it is in Ito–Seiler p. 16, credited to Kanazawa by
  private communication. The note credits it that way. **HOLDS.**

**A6. Ito–Seiler 0803.3019 §§3.2–3.3 and Theorem 2.2.** p. 12 lists Problems 1–3: existence of
t_m in (5.9) (separate shifts), existence of t* (common matching), and extension of t(λ)
"even if Ψ_t ≠ 0". p. 12 demands contractivity. §3.3 starts at the foot of p. 12 (the note
says pp. 13–16; trivial). p. 13 gives f_n(θ) = exp[−βθ²/(2rⁿ)] for the Gaussian model. p. 14
shows the SU(2), r = 0.9 numerical flow with a split near β ≈ 4.8. p. 16 gives the
e^{−t} − 1 + 2λ example. Theorem 2.2 (p. 6): (1) U(1) or SU(2), small β, area decay;
(2) U(1), large β, lim F/(L₃L₄) ≥ const/(L₁L₂), attributed on p. 7 to [13], listed on p. 18 as
"preprint in preparation". All as the note states. **HOLDS.**

**A7. PoS (4.5)–(4.11).** (4.5)–(4.6): r_m = 1 − ε/(1 + β_eff(m−1)), ε ~ 10⁻⁶ (p. 7). The p. 7
bracket is "seen numerically to hold". (4.9) is printed with −F̃₀ (no logarithm), twisted
residual first, untwisted second. (4.10)–(4.11) and conditions (i) F(x₀) < 0, (ii)
[1 + λF_x]⁻¹ ≥ 0, bounded D with a component of F positive on ∂D are on p. 8, with
x = (t, α). p. 8 then asserts that "the above conditions are satisfied" for large n and a
suitable h, with no proof. p. 9 says U(1) "hits a fixed point" and gives (4.15)–(4.16) for
Wilson-line correlators. All as the note states, except that (4.9) is on p. 7, not p. 8.
**HOLDS** (page slip only).

**A8. Reply 0712.2620 (not a named item, checked because it was downloaded).** pp. 1–5 say
(5.15) is invoked only at strong coupling. pp. 5–6 call r "an integral part of the argument".
No flow proof appears, and p. 4 repeats that t* exists if (5.15) holds. The note's §2 summary is
accurate. **HOLDS.**

## B. The note's own arguments, checked by hand

**B1. Counterexample Ψ = e^{−t} − 1 + 2λ (note §2.1).** Ψ_t = −e^{−t} < 0 and Ψ_λ = 2 > 0
everywhere. Ψ(0,0) = 0. Solving gives e^{−t} = 1 − 2λ, so t(λ) = −log(1−2λ) for λ < 1/2,
which diverges as λ → 1/2. For λ ≥ 1/2, e^{−t} = 1 − 2λ ≤ 0 has no real solution. It meets
every hypothesis T actually states on p. 45 (smooth gradient, Ψ_t ≠ 0 throughout), so it
refutes the stated inference. The note correctly says it is not a counterexample to the
SU(2) equation itself. **HOLDS.**

**B2. Ψ(1,t) identity and Ψ_t formula.** Definitions checked on pp. 12–14 and 44: F̃₀ = (F₀^U)^{h(α,t)}
(3.16); Z̃ = F̃₀^{|Λ|} Z(c̃(α)) (3.19); A = (ln F₀^U · |Λ|)⁻¹ ∂_α ln Z(c̃(α)) (3.27); A⁺ the
twisted analogue (4.22); h_t < 0 assumed (p. 14). With B = N ln F₀^U, Φ = B⁻¹ ln Z_c,
k = B⁻¹ ln Z_f, the untwisted level equation (3.24) is h(α(t),t) + Φ(α(t)) = k, so
α_t = −h_t/(h_α + A), which is (3.25)–(3.26).
- Ψ(1,t) = h + Φ⁺(α(t)) − k⁺ = k − k⁺ + Φ⁺(α(t)) − Φ(α(t)). So Ψ(1,t) = 0 iff
  Z_c⁺(α(t))/Z_c(α(t)) = Z_f⁺/Z_f. Correct.
- Ψ_t = h_t + (h_α + λA⁺)α_t = h_t[1 − (h_α + λA⁺)/(h_α + A)] = h_t (A − λA⁺)/(h_α + A).
  This is algebraically identical to (C.9). Correct.
- Ψ(0,t) = h(α(t),t) − h(α⁺(t_I),t_I) by (C.2), so t₀ of (C.3) solves it. Correct.

A consequence worth stating outright: by continuity in t and the intermediate value theorem,
Ψ(1,·) has a zero iff the fine ratio Z_f⁺/Z_f lies in the range of α ↦ Z_c⁺(α)/Z_c(α) over the
α values the level curve reaches. Appendix C therefore needs an endpoint bracket of the fine
ratio by coarse ratios. That bracket is (5.23), which T derives from (5.17), and which the PoS
paper supports only numerically (p. 7). The note says this in words. **HOLDS.**

**B3. The c⁶ counterexample (note §2.4).** Take f = 1 + 2cχ_{1/2}, 0 < c < 1/4 (so f ≥ 0, since
|χ_{1/2}| ≤ 2). Expand Z = Σ_S (2c)^{|S|} ∫ ∏_{p∈S} χ_{1/2}(U_p) over plaquette subsets S. The
substitution U_ℓ → −U_ℓ on one link flips the sign of every factor containing ℓ, so a nonzero
term needs every link covered an even number of times: S is a nonzero mod-2 2-cycle.

Are there 2-cycles of size ≤ 6 other than elementary cube boundaries? I checked this by a
slicing argument, not by enumeration. Pick a direction μ used by some plaquette of S. For a slab
k < x_μ < k+1, the (μ,ν)-plaquettes of S in that slab project to a set γ_k of ν-links in the
3D slice. Evenness at each μ-link makes γ_k a mod-2 1-cycle. The non-μ plaquettes σ_k of S
in the hyperplane x_μ = k satisfy ∂σ_k = γ_{k−1} + γ_k, by evenness at non-μ links. A nonzero
1-cycle in the cubic lattice has at least 4 links, with equality only for the boundary of one
square. On the torus with sides ≥ 8, either all slabs carry nonzero γ (≥ 32 plaquettes) or one
can cut at an empty slab and order the rest linearly. Let k₀ and k₁ be the first and last slabs
with γ ≠ 0. Then σ_{k₀} and σ_{k₁+1} are nonempty. If k₀ < k₁, |S| ≥ 8 + 2 = 10. If k₀ = k₁,
|S| ≥ 4 + 1 + 1 = 6, and equality forces γ = ∂(square) and σ_{k₀} = σ_{k₀+1} = that square:
an elementary 3-cube boundary. So there are no terms below order c⁶, and at order c⁶ the only
terms are cube boundaries. The next terms are O(c¹⁰).

Weight per cube: link integration with ∫D_{ab}(U)D_{cd}(U)* dU = δδ/d gives d^{#V−#E} for
the closed surface. The cube has 8 vertices and 12 edges, so (dc)⁶ d^{8−12} = d²c⁶ = 4c⁶.
χ_{1/2} is real, so orientation does not matter. There are C(4,3)V = 4V elementary cubes.
So Z = 1 + 16Vc⁶ + O(c¹⁰). The printed bound with exponent 6V gives
(1 + 4c⁶)^{6V} = 1 + 24Vc⁶ + O(c¹²) > Z for small c > 0. The cross-check with Kanazawa (12)
(p. 5), a₄ = 2/3: (2/3)·4c⁶ per plaquette × 6V = 16Vc⁶. The counts a₃ = 1/3 and a₄ = 2/3 fit
a per-plaquette normalization (1 cube per 3 plaquettes in 3D, 4 per 6 in 4D). **HOLDS.**

Supplement, not a correction: the site-counted bound Z ≥ (1 + Σd²c⁶)^V, which is what
(A.1)–(A.4) actually produce, still yields III.2 with c^L = c⁶ and F₀^L = 1 for b ≥ 2 in
d = 4. The coarse lattice has 6V/b⁴ ≤ V plaquettes, and |1 + Σ d_j c_j⁶ χ_j| ≤ 1 + Σ d_j² c_j⁶
pointwise. Hence Z_{Λ(n−1)} ≥ (1 + Σd²c⁶)^V ≥ (1 + Σd²c⁶)^{6V/b⁴} ≥ Z_{Λ(n)}({c⁶}), taking
(A.5) as printed. The note keeps only the c^L = 0 endpoint. That is safe but more cautious
than needed. The defect is in (2.13) and its cited justification, not in III.2.

**B4. Z₂ recursion and finite-group flow (note §3.1).**
- Z₂: e^{βu} ∝ 1 + (tanh β)u, and (1 + cu)^q ∝ 1 + tanh(q atanh c)u. s-fold convolution raises
  the coefficient to the power s. With c = 1 − δ, e^{2 atanh c} = (2−δ)/δ, so
  1 − ĉ = 2/(((2−δ)/δ)^q + 1) = 2δ^q/((2−δ)^q + δ^q) ≤ 2δ^q, since (2−δ)^q ≥ 1 for δ ≤ 1.
  1 − ĉ^s ≤ s(1 − ĉ) for s ≥ 1 by the mean-value theorem on [0,1]. Choosing
  2sδ₀^{q−1} ≤ 1/2 gives 1 − c' ≤ δ/2 for δ ≤ δ₀, because q ≥ 2. So c_n → 1. Correct.
- Finite group: after f^q and normalization, off-identity mass ≤ Kε^q. The product of s independent
  draws is the identity whenever every draw is, so its off-identity probability is ≤ sKε^q (union
  bound). The new weight at g ≠ 1 is ≤ sKε^q, and at 1 it is ≥ 1 − sKε^q. That gives the stated ε'.
  The Wilson weight restricted to a finite subgroup peaks only at the identity, and
  exp(β(tr g − 2)/2) → 0 for g ≠ 1. Correct for integer q > 1 and integer s.
**HOLDS.**

**B5. Sign countercheck of the 2008 repair (note §4).** As printed, x = (t, α), and both residuals
have the form f_i = −ln F̃₀ − N⁻¹ ln Z_i(α) + const (logarithm restored). So
∂_t f_i = −(ln F₀^U) h_t =: u > 0. Here F₀^U ≥ 1 by Jensen, since F₀^U = (∫f^ζ)^{b²} with
∫f = 1 and ζ ≥ 1, and h_t < 0. Also ∂_α f_i = −ln F₀^U (h_α + A_i) =: −a_i < 0.
(I + λF_x)⁻¹ has (2,1) entry −λu/det < 0 for small λ > 0. Condition (ii) as printed
therefore fails at every interior point. Reading the bulk term literally as −F̃₀ gives the
same sign. The note's computation is right.

**Correction to the weight of this point.** The failure belongs to the printed sign and
coordinate conventions, not to the method. F_x = [[u, −a₁], [u, −a₂]] has off-diagonal entries
of opposite sign. Swapping rows, reordering coordinates, or negating F keeps them of opposite
sign. But the reparametrization s = −t gives F_x = [[−u, −a₁], [−u, −a₂]], whose off-diagonals
are both negative (a Z-matrix). Then (I + λF_x)⁻¹ = det⁻¹[[1 − λa₂, λa₁], [λu, 1 − λu]] ≥ 0
entrywise for 0 ≤ λ ≤ λ₀ with λ₀ small, given bounded derivatives on D. Negating one residual
has the same effect. So condition (ii) can be met by a coordinate reflection. The substantive
unproved hypotheses of the 2008 repair are (i) and the bounded invariant domain with a
boundary sign, which amount to the endpoint bracket of B2. The note's own hedge says a
different order cone "might permit another construction" and would need verification. That
verification is easy and positive for (ii). The note should say so, and the RESULT line should
not present the sign failure as a defect of the repair's mathematics.
**HOLDS AFTER CORRECTION.**

**B6. Mean-value mismatch (note §2.3).** log Z_c(α) − log Z_c(α_N) = N[p_N(α) − p_N(α_N)]
= N p_N'(ξ_N)(α − α_N) = −γ_N p_N'(ξ_N). The limit −γ p'(α) needs γ_N → γ, ξ_N → α, and
locally uniform convergence of p_N' (the note's "converge near α" should be read as locally
uniform). The conclusion, that an O(1/N) mismatch leaves an O(1) log-ratio error, is right. It
agrees with Kanazawa p. 5, (14)–(15). **HOLDS.**

**B7. Error budget (note §5.5).** R_fine ≥ R_coarse − ε_a ≥ 1 − x with x = δ_a + ε_a ≤ 1/2. Then
F_fine = −log R_fine ≤ −log(1−x) = ∫₀^x dy/(1−y) ≤ 2x. **HOLDS.**

**B8. Remaining hand claims spot-checked.**
- Kanazawa's Theorem 4 arithmetic: q = b², s = b²−1 ≥ 2, q/s = 1/r. ρ = (1 − e^{−W₀})/r < 1
  iff b² > e^{W₀}. W non-increasing gives W_n ≤ ρⁿW₀. osc(V) ≤ W/2 with V(1) = 0 gives
  f_n → 1 uniformly. Correct.
- Σ_{j>0} d_j² c_{j,n} = g_n(1) − 1 for g_n = f_n/∫f_n. Correct.
- The Gaussian map: f^{b²} has variance 1/(b²β), and b²r convolutions give r/β, so β' = β/r. This
  confirms Ito–Seiler p. 13. Correct.
- "α_t ≥ η > 0 cannot hold on an unbounded interval": trivial and correct.

## C. Is the RESULT line fair, and is the failure located correctly?

**Location.** Yes. V.1/(5.17) needs t^{(n)} from (5.14). p. 26 sends that existence to
Appendix C. The only global step in Appendix C is the claim on p. 45 that Ψ_t ≠ 0 lets t(λ)
reach λ = 1. B1 refutes that inference in general. By B2, closing it for SU(2) is equivalent
to bracketing the fine ratio between coarse ratios on the reachable α range. That is (5.23),
which T obtains only as a corollary of (5.17). The unproved modified-flow claim (p. 19,
footnote 8) is a separate, independent gap, and the note keeps it separate. Kanazawa's
Theorem 4 removes it for a different choice (b large, r = 1 − 1/b²), for SU(2) and U(1)
alike. The note's U(1) diagnosis follows: once a valid flow exists for U(1), V.1 is the first
step that cannot hold for both groups.

**RESULT line.** Fair, with one correction. "A failed sign condition in the 2008 attempted
repair" is true of the printed formulas only. The reflection t → −t (or negating one residual)
satisfies condition (ii) locally (B5). The 2008 repair's real gap is the asserted bounded
domain and boundary sign, i.e. the same endpoint bracket. Suggested wording: "... and an
unproved trapping-domain hypothesis in the 2008 attempted repair, whose printed sign condition
fails only as a convention and is restored by t → −t". The rest of the line (OPEN; Kanazawa's
mismatched-ratio representation as the main salvage; partition-function bounds and the
connected-group flow isolate rather than remove the twist-normalizer comparison) matches
what the sources and the hand checks support.

**Minor wording fixes (no effect on conclusions).**
1. §4: (4.9) is on PoS p. 7, not p. 8.
2. §2: Ito–Seiler §3.3 begins on p. 12.
3. §2.3: Kanazawa Theorem 1 takes H = Z_N for SU(N), and an arbitrary discrete subgroup of
   U(1) for U(N). The note's "a finite subgroup H of the center" blurs the SU(N) case.
4. §2.3: "pressure derivatives converge near α" should say "locally uniformly".
5. §2.4 (optional strengthening): III.2 with c^L = c⁶ survives under the correct site count for
   b ≥ 2 (B3 supplement). The defect is confined to (2.13)/(A.4)–(A.5) and their remark.

## Verdict table

| Item | Verdict |
|---|---|
| A1 Appendix C (C.1)–(C.12) and V.1 (5.17) | HOLDS |
| A2 p. 19 and footnote 8 | HOLDS |
| A3 (2.13), (A.4)–(A.5), bonds/plaquettes remark | HOLDS |
| A4 (5.6) warning | HOLDS |
| A5 Kanazawa v3 Theorems 1, 3, 4; Appendix A.1 | HOLDS (minor wording on H for SU(N)) |
| A6 Ito–Seiler §§3.2–3.3, Theorem 2.2 | HOLDS (page start of §3.3) |
| A7 PoS (4.5)–(4.11) | HOLDS ((4.9) is on p. 7) |
| A8 Reply 0712.2620 | HOLDS |
| B1 Counterexample e^{−t} − 1 + 2λ | HOLDS |
| B2 Ψ(1,t) identity; Ψ_t = h_t(A − λA⁺)/(h_α + A) | HOLDS |
| B3 c⁶ counterexample (Z = 1 + 16Vc⁶ + O(c¹⁰) vs 1 + 24Vc⁶) | HOLDS; uniqueness of order-c⁶ terms checked by a slicing proof |
| B4 Z₂ recursion and finite-group flow | HOLDS |
| B5 Sign countercheck of the 2008 repair | HOLDS AFTER CORRECTION: the failure is a convention artefact; t → −t restores (ii) |
| B6 Mean-value mismatch | HOLDS (read "converge" as locally uniform) |
| B7 Error budget | HOLDS |
| C Decisive-failure location | HOLDS |
| C RESULT line | HOLDS AFTER CORRECTION: reword the 2008 sign-failure clause |

No item FAILS. Not checked: sources not downloaded (see header) and the repository
cross-references in §§5–6.

RESULT: HOLDS AFTER CORRECTION — the note's readings of Tomboulis, Kanazawa v3, Ito–Seiler, the reply and the PoS paper match the PDFs, and its hand arguments (continuation counterexample, Ψ identities, c⁶ normalization counterexample, Z₂/finite-group flow, mean-value mismatch, error budget) are correct; the one correction is that the 2008 repair's printed sign condition fails only by convention (t → −t restores it), so the RESULT line should name the unproved trapping domain/endpoint bracket, not the sign, as that repair's gap.
