# REVIEW_X5_X6: independent hostile review of sessions 5 and 6 of the YM4D existence lane

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session6_snapshot.md (`cmp` empty).
  - `diff session4 session6` was read in full: 997 lines. Outside §14-§15 the changes are the RX34 fixes, the header, §0
    and §6, as the file says.
  - §4 (X-OS, X-CONT), §6, §10.2 (X-KER, X-CONT-G), §13.1-13.2 and §14-§15 were read by offset.
- LOG.md sessions 4-6 (l.161-344) and REVIEW_X3_X4.md (all).
- checks: x4_criteria.md, x4_soft_noise.py, x4_out.txt, x4_time.txt; x5_criteria.md, x5_su2_soft.py, x5_out.txt,
  x5_time.txt, x5_posthoc_kernel.py, x5_posthoc_out.txt.
- P (read-only): only `grep N5 PROOF.md`, to check the N5 status cited in §15.6. N5 at levels i ≥ 1 is still OPEN there
  (PROOF.md l.14, l.2137).

Line numbers below are EXISTENCE.md lines unless marked. No web access. No file was edited other than this one.

**Re-run conditions.**
- Under the numeric lock (`mkdir …/scratchpad/locks/numeric`, released by an EXIT trap). nice 10, with
  OMP/OpenBLAS/MKL/vecLib threads set to 1.
- `uptime` load was 2.3 before and 3.0 after, so below 8. 47% of memory was free.
- No `timeout` was used.
- Output: scratchpad `rerun_x45/`, plus a reviewer-side script `extra_review.py` there.

**Bottom line.**
- **All 12 RX34 fixes are applied correctly.** §12.1 is REVIEW_X3_X4's text word for word (`diff` empty). Three cosmetic
  leftovers are listed in (1).
- **Theorem X-KER^S (iv) is CORRECT.** Its framing needs fixes, and the result is vacuous in the one model that can be
  computed:
  - The proof is X-KER (i) applied to an algebra with 𝔄_{++} = 𝔄_+. Nothing new is proved about the Wilson measure.
  - **New finding (reviewer).** In the free Gaussian soft chain with an (F)-type sequence, the soft OS form has rank one
    in the limit, so H^S_ω = CΩ. The OS form sees only F̃ = E[F | U_0], and Var F̃ ≤ Λ²|X|g_0² → 0.
  - Kernel triviality is established, and so is time continuity in X-OS (iv)'s sense on D. Both are free consequences of
    choosing open supports. The real gap is dim H^S_ω > 1, and none of (I)-(IV) of §15.6 touches it.
- **Theorem GS, GS-1, GS-2 and Corollary PLD-G^S are CONFIRMED.**
  - Re-derived: the exact noise sum (4σ²/3)(2L^{-2n} + L^{-4n}), the symbol bound and the (F) comparison.
  - One arithmetic error, in GS (iv) (diagnostic): 0.0654 / 0.0042 should be 0.0453 / 0.0021. The conclusion survives.
  - The corollary is mislabelled as an "instance of (PLD^mod_dis)" in five places, which contradicts the lane's own T16
    verdict.
- **Session 6 survives.**
  - CONFIRMED: Lemmas NA-1 and NA-2, Proposition NA-3, Theorem NA-GS1 and Proposition H-cont^S-red. H-cont^S-red needs
    one class fix.
  - Scope leaks: NA-3 is flat-background only, and NA-GS1 is SU(2), U_0 = 1, at fixed K. Several headline lines drop
    these qualifiers.
  - (NA-R2) is correctly OPEN. "(H-lin^S) ≡ (NA-R2)" overclaims: NA-R2 is about a flat background and an expectation,
    while H-lin^S concerns a general background and an L¹ estimate.
- **ASSEMBLY §15.6 is mostly faithful.**
  - (I) claims OS structure on a "fixed torus", which X-OS does not cover (it needs time side ℓ_0 → ∞).
  - Three provenance cells overstate layer-1 status: "PROVEN in layer 1" for unreverified imports, A1 missing from the
    table, and N5 not marked OPEN.
- **Checks.** x4 and x5 re-run identically: x4 byte-identical; x5 identical except wall times. **Both PASSes are
  honest.**
  - x5 B: an adequate fit (R_∞ + b/t + c/t²) has χ²/dof = 0.16 and R_∞ = 0.46943 ± 0.00064, which is +0.47 SE from 38/81.
    The reported "b ≈ +5.6" is a model artefact; the true value is b ≈ 4.1.
  - A3's -3.8 SE: replayed at the *same* M with 2.03·10⁶ samples, it comes out at +1.33 SE. It was a fluctuation.
- **Public statement.** §15.5's narrower PLD clause is ACCEPTED word for word. The time-continuity clause is ACCEPTED with
  changes; the text is given in (7).

---

## (1) The 12 RX34 fixes

| Fix | Where (session-6 lines) | Verdict |
|---|---|---|
| 1 X-RP^S continuum supports; counterexample; 𝔄_+ | l.1410-1417, 1425-1431 | CONFIRMED. The nesting sentence is right (L odd: an ancestor's support lies inside its descendant's support). |
| 2 L² H-cont / H-bl false for soft | l.544-548, 1452-1455, 1712-1714 | CONFIRMED |
| 3 CBE relabel; tallies | l.1493-1496, §0 l.69-70, §6 l.614-617, LOG l.226 | CONFIRMED |
| 4 "not Haar \| (RLF-3^dis), (F)"; kernel-only "not flat"; merge table inputs | l.1540-1546, 1591-1602, LOG l.197 | CONFIRMED. LOG l.196 keeps the old sentence, followed by the correction; acceptable. |
| 5 (RLF-3^dis) wording; g_RLF | l.71-73, 1537, 1557-1561, 1584-1586, 1594, 1717-1721, §12.1 | CONFIRMED |
| 6 P_cut identification | l.1642-1645, 1654-1656 | CONFIRMED |
| 7 A2 is deterministic-averaging evidence | l.1673-1675, 1691-1693, LOG l.209-210 | CONFIRMED-WITH-FIX (cosmetic): in LOG the annotation is inserted *inside* a sentence (l.208 "…Gaussian in" / l.211 "any global chart"). Move it to after the sentence that ends at l.213. |
| 8 MIX "reduced" | l.1572, 1579-1582, 1717 | CONFIRMED. LOG l.200 still says "D3 is not needed" without annotation (cosmetic; RX34 did not list LOG). |
| 9 KN / RS qualification | l.1619-1622 | CONFIRMED |
| 10 E_1 = E_bg + 2H_0K_0; conditions on g | l.1140-1155, 1178 | CONFIRMED |
| 11 §0 labels; (F) plausible extension; X-IVND′ + H-Bal-1 | l.43-45, 56, 58, 64-65, 607, 618-619 | CONFIRMED |
| 12 §12.1 word for word | l.1305-1330 | CONFIRMED (`diff` against REVIEW_X3_X4 l.443-468 is empty) |

**Cosmetic: there is no §14.2 heading.** §14.1 (l.1791) runs into §14.3 (l.1904), but l.1656, 1675, 1692, 1786 and LOG
all cite "§14.2". Insert "### 14.2 Theorem GS and the soft (PLD) analogue" before l.1805.

---

## (2) Theorem X-KER^S (iv) (l.2174-2195), the highest priority: CONFIRMED (mathematics); CONFIRMED-WITH-FIX (framing)

### The proof is correct. Checked step by step:

1. **Supports.**
   - A soft generator has finitely many variables of K-independent resolutions, so its continuum support is a finite
     union of closed cubes. That is compact, so its distance d from Π_0 is positive.
   - For a product of generators the support is the union, and d is the minimum. This uses the continuum-support class of
     RX34-fix 1 (l.1410-1413). Under that class, **no plane-touching soft generator exists**: a resolution-n link whose
     cube union meets Π_0 is excluded by definition. That was the risk named at l.2309-2311, and it does not materialise.
2. **The translated generator.**
   - For s ∈ 2D_+ with s < d, τ_{-s}G is again a soft generator. Translation by an element of D maps the class tree to
     itself (X-SYM^S; take K ≥ level(s)).
   - Its support has distance d - s > 0 from Π_0, so it lies in 𝔄^S_+, and T(s)[τ_{-s}G] = [G].
3. **The kernel.**
   - ker T(s) = ker T(2) = 𝒦, by unique positive roots (X-OS (ii)-(iii)).
   - T(s) is bounded and self-adjoint, so Ran T(s) ⊂ 𝒦^⊥.
   - The *-algebra of finite combinations is norm-dense, and ||[F]||_OS ≤ ||F||_∞. A closed subspace that contains a dense
     set is everything, so 𝒦 = {0}.
4. **The semigroup.** T(s) = T(2)^{s/2} is injective. Hence H = -½ log T(2) ≥ 0 is self-adjoint on all of H^S_ω, and
   T(s) → 1 strongly as s → 0 in D.

### What is and is not established (requested verdict)

- **Kernel triviality: yes.**
- **Time continuity: yes, in the precise sense of X-OS (iv).** That means lim_{s→0, s∈2D} ω(θ(F)^*τ_sF) = ω(θ(F)^*F)
  for all F ∈ 𝔄^S_+. It is equivalent to 𝒦 = {0}, and it gives strong continuity of T on D.
- **"Strongly continuous for real s ≥ 0" is functional calculus, not physics.** No continuum time translation acts on the
  algebra. The real-s semigroup is the unique positive interpolation. That is legitimate, but it should be said.
- **Nothing here concerns separated correlations.** For F and G at positive separation, ⟨F, T(s)G⟩ was already the
  restriction to D of a function analytic in s > 0, by X-OS (iii), *without* 𝒦 = {0}. The only new content is the
  limit s → 0. For an open-support algebra that limit is automatic, because every generator is already in Ran T(s) for
  small s.
- **The result is the textbook fact that an OS space built from test objects with strictly positive time supports has
  no kernel.** It is correct and not new. It answers nothing about the deterministic branch's plane-touching algebra.
  l.2192-2193 says this correctly.

### Can H^S_ω be one-dimensional, making the claim vacuous?

- **Yes. It is one-dimensional in the free model with (F)-type couplings (new finding; a short exact argument):**
  - **The setting.** Take the free Gaussian soft chain of §14.1, with kernel couplings from an (F)-type sequence, so the
    finest coupling satisfies g_0² ≤ (1/g² + β_-K log L)^{-1} → 0.
  - **What the OS form sees.** By X-KER^S (i), ⟨F, G⟩_OS = lim E_μ[θ(F̃)^*G̃].
  - **The bound on F̃.** For F = f(block curvatures on X), with f Λ-Lipschitz, the proof of X-CONT-G^S (l.1941-1945)
    gives F̃ = f_η(D(B_0)) with f_η Λ-Lipschitz. Then Var_μ(F̃) ≤ Λ² Σ_{P∈X} Var D(P) ≤ Λ²|X|g_0², by X-CONT-G (iii).
  - **The conclusion.** By Cauchy-Schwarz, |⟨F, G⟩_OS - conj(ωF)·ωG| ≤ lim (Var F̃ · Var G̃)^{1/2} = 0. So on this class
    the OS form has rank one, and H^S_ω = CΩ.
  - **Contrast with the soft law itself.** ω is not trivial: it is pure kernel noise of size g'_m²/κ, which l.1891-1895
    already notes.
  - **Contrast with constant couplings.** With constant couplings (g_i ≡ g) the form is not degenerate.
- **This is not a counterexample to the interacting theorem.** The free model does not run, and the lane says so at
  l.1893. But it shows two things:
  - (i) Every unconditional and conditional conclusion of §15.6 (I)-(III) has a free analogue that holds while the OS
    space is CΩ. The "not Haar" and AF bounds constrain the *full* soft law, kernel noise included. The OS form sees only
    the fine-field signal F̃.
  - (ii) Corollary X-CONT-G^S is satisfied vacuously under (F)-type couplings, because its left side → 0 for every w.
- **What non-triviality needs.** A K-uniform lower bound on a connected correlation across the plane:
  - **(H-sig^S)** (proposed name): there exist F, G ∈ 𝔄^S_+ with liminf_K |Cov_{μ_K}(θ(F̃_K), G̃_K)| > 0.
  - This is a statement about the Wilson measure seen through kernel smoothing. No kernel-only fact can supply it.

### Fixes (binding)

- **(a)** l.2174 title and l.2176-2178: add "(this is X-KER (i) for the open-support algebra, in which every generator lies
  in 𝔄_{++}; time continuity in the sense of X-OS (iv) on D; the real-s semigroup is the functional-calculus
  interpolation)".
- **(b)** After l.2195, add the free-model remark above, labelled **PROVEN-HERE (short; reviewer's computation, to be
  re-checked by the lane)** or **ARGUED** if the lane prefers. Add (H-sig^S), or "dim H^S_ω > 1", as an explicit **OPEN**
  entry. At present it appears only under "Not delivered" (l.2343).
- **(c)** §0 l.85-86 and LOG finding 4: append "(may be vacuous: H^S_ω may be CΩ; in the free (F)-type soft chain it is)".

---

## (3) Session 5: Theorem GS and its corollaries

### Lemma GS-1 (l.1805-1810): CONFIRMED
- The recursion Q_root^{n+1} = Q_str^{n+1} - dhQ_str^n + d ev λ_n is re-derived from (R) and root covariance.
- d∘d = 0 gives dQ_root^n = dQ_str^n.
- The noise sum follows by linearity.

### Lemma GS-2 (l.1812-1828): CONFIRMED (all five parts re-derived)
- **(a)** The coefficient of ξ_μ(z) is s^{-4} times #{(y, j) : y_μ + j = z_μ, y ∈ sX + box_s, j < s}. That count is a
  triangle m_s along μ and the indicator of the box transversally.
- **(b)** Σ m_s² = Σ_{u≤s}u² + Σ_{u<s}u² = (2s³ + s)/3. So Var = σ²s^{-8}·s³·(2s³ + s)/3 = (σ²/3)(2s^{-2} + s^{-4}).
- **(c), (d)**
  - b_μ(X) and b_μ(X + e_ν) are independent, because their transverse ν-supports are disjoint.
  - b_μ and b_ν are independent, because they use different components.
  - So db(P) has four independent terms, and Var = (4σ²/3)(2s^{-2} + s^{-4}). This is the **exact noise sum**.
  - Its n = 0 value is 4σ².
- **(e)** Decimating the filter s·D_s(q_μ)²·Π_{α≠μ}D_s(q_α) gives σ²s^{-2}Σ_a|D_s|⁴. Parseval gives Σ_a|D_s|² = 1, so the
  supremum is σ²s^{-2}, attained at P = 0. The curvature bound uses ||d||² ≤ 16.
- **x4** confirms all of this. B1 (position space) is the independent route; B2 uses the symbol of (e) itself.

### Theorem GS (l.1830-1855): CONFIRMED-WITH-FIX
- **(i)-(iii) and the convergence statement are re-derived:**
  - the bounds 4σ²_{j-1} ≤ N_j ≤ 4.35σ̄² at L = 3;
  - the tail 4σ̄²L^{-2(K-m)}/(1 - L^{-2});
  - and that N_K(m) is nondecreasing in K.
- **What (ii) imports.** The first term of (ii) relies on A1 (the curvature map of Q is a contraction, LINEAR_PACKAGE Lemma
  2.2). This is **imported, not re-derived** here: X-CONT-G (iii) bounds single composite fluxes, not the operator norm.
  Name it in the hypothesis table (§5 below).
- **(iv) arithmetic (WRONG number; conclusion survives).**
  - 0.5342 - 0.3777 - 0.1111 = **0.0453**, not 0.0654. Its square is **0.00206**, not 0.0042. (E3 in
    `extra_review.py` checks this.)
  - The constant is also specific to L = 3: the 1/9 and the l-sum 1/(L - 1) both use L = 3.
  - **Fix:** l.1840 and l.1853, and LOG l.270: replace 0.0042 by 0.0020 and 0.0654 by 0.0453, and add "(L = 3)".
  - The divergence of the gauge-variant root-representative variance stands. It is diagnostic only.

### Corollary PLD-G^S (l.1862-1872): CONFIRMED (mathematics); WRONG label
- **The comparison is re-derived:** g_i² ≤ β̂g_j² for i ≤ j, from both halves of (F).
- **The Gaussian product bound is re-derived:** E exp(Σ|F|²/(4λ)) ≤ 2^{dim/2} with Cov ≤ λ, applied over N² - 1
  independent copies.
- **The label contradicts the lane's own T16 verdict.** §15.5 (l.2298-2303) rejects "holds for the free Gaussian soft
  chain", because (PLD^mod_dis) is a statement about the conditioned P_cut. Yet the following lines still call the
  corollary "the free Gaussian instance of (PLD^mod_dis)":
  - l.80 (§0);
  - l.1862 (the title);
  - l.1888-1889;
  - l.1969-1970;
  - LOG l.273.
- **Fix (binding):** "an unconditioned analogue of (PLD^mod_dis) in the free noncompact abelian soft chain (N² - 1
  independent copies)". Leave the pre-stated text (l.1765, 1778) as it is.

### X-KER^S (i)-(iii) (l.1911-1934): CONFIRMED
(i) is the X-RP^S computation with G in place of the second F. (ii) is Cauchy-Schwarz plus θ-invariance of μ_K. (iii) is
correct, and now superseded by (iv).

### Corollary X-CONT-G^S (l.1936-1952): CONFIRMED, but vacuous under (F)-type couplings
The noise law does not depend on t, because the shifted class tree is a translate. So the conditional expectation is
f_η∘D_t, which is Λ-Lipschitz. The bound holds. Under (F)-type couplings, g_0 → 0, so the bound is trivial (§2). Say so
at l.1946.

---

## (4) Session 6 items

### Lemma NA-1 (l.2016-2040): CONFIRMED
- **(a)** For Y ∈ su(N), tr(YH) is imaginary and tr(YS) is real, so S ∈ iR·1.
- **(b)** For Hermitian A, conj tr(AZ) = tr(Z^{-1}A).
- **(c)** The real span of SU(2) is the quaternions, so M̄ = rW and A = r1.
- **(d)**
  - I_2/I_1 follows by differentiating ∫e^{t cos θ}sin²θ dθ = πI_1(t)/t.
  - The bound 1 - a ≤ 3/(2t) holds. It uses the substitution u = 1 - cos θ (density ∝ u^{1/2}(2 - u)^{1/2}e^{-tu}),
    Chebyshev's inequality with h decreasing, and truncation of a Gamma(3/2, t) law.
  - The asymptotics 1 - a = 3/(2t) - 3/(8t²) + … confirm that the bound is sharp. x5 A2 gives 0.999975.

### Lemma NA-2 (l.2042-2068): CONFIRMED
- **The factorisation (i)-(iii)** holds:
  - V_c^{-1} = W_c^{-1}(W_cZ_c^{-1}W_c^{-1}), using conjugation and inversion invariance;
  - A_1Y_1⋯A_ℓY_ℓ = (ΠA)Π(B_i^{-1}Y_iB_i);
  - central measures commute under convolution;
  - for (iii), law(Ỹ^{-1}) = law(Ỹ).
- **(ii)** follows from Schur.
- **(iv)** follows from 1 - Πa ≤ Σ(1 - a_i) and a ≥ 0.
- **The "distinct links" hypothesis is necessary**, and is correctly stated.

### Proposition NA-3 (l.2070-2084): CONFIRMED (proof); CONFIRMED-WITH-FIX (scope in headlines)
- **The proof is checked:**
  - a constant gauge transformation fixes U_0 = 1;
  - complex conjugation commutes with contour products, fixes Re tr, and preserves Haar measure, so 𝒩(conj M̄) = 𝒩(M̄);
  - V̄ = (V^{-1})^T, and a central law is determined by its eigenvalue law;
  - Schur gives α real;
  - log V is bounded, so E log V = 0.
- **The result is weak.** It holds only at U_0 = 1, where symmetry alone forbids any su(N)-valued mean. The bias question
  that matters is the background-dependent one, and that remains ARGUED (l.2143-2164).
- **Scope leaks.** These lines drop "in a flat background":
  - l.3 ("compact SU(N) soft noise: no bias at O(σ²)"; that also blurs NA-GS1's SU(2) scope);
  - §0 l.85-86 ("no additive drift of any block holonomy at any depth (all N)");
  - l.2115-2116 (item 1);
  - l.2361 (T14);
  - LOG l.317 (in the heading).
- **Fix (binding):** write "in a flat background (U_0 pure gauge)" in each. Rewrite l.3 as "compact soft noise: SU(2),
  flat background, fixed K: the O(σ²) floor is GS-damped; every N, flat background: no additive drift".
- The parity count (l.2148-2156) also survives ε-tensor terms, because ε has an even number of slots. It is correctly
  ARGUED.

### Theorem NA-GS1 (l.2088-2112): CONFIRMED (SU(2), U_0 = 1, fixed K, kernel only)
- **(1) Concentration.** P(G^c) ≤ C_Ke^{-cε^{-1/3}}, with r ≥ 1/2 on G, by induction over levels.
- **(4) The cross term**, which is the step to check. The latest level i* in a cubic monomial gives three cases:
  - i* once or three times: the term vanishes by φ ↦ -φ symmetry;
  - i* twice: the term is εσ²E[φ_e/r(past)], with 1/r = 1 + (even quadratic) + O(φ³), so it is O(ε^{5/2});
  - off-diagonal pairs at i* vanish by independence;
  - so the cross term is O(ε²) or smaller, as claimed.
- **The coefficient** is (1/2)·3·N_j. In the x5 B setting it is 38/81.
- **Scope: kernel only.** The fine field is frozen, so the result carries no Yang-Mills content. ASSEMBLY (I) correctly
  lists it as kernel-only. But l.2333-2334 ("the O(σ²) part of the noise floor is GS-damped (NA-GS1)") must add
  "(SU(2), flat background, fixed K)".

### The σ⁴ claim (l.2121-2125, 2279-2283): ARGUED, honestly labelled; one number fix
- **Summability under (F) is correct.** Σ_r(1/g² + β_-r log L)^{-2} < ∞.
- **The x5 coefficient comes from an inadequate fit.** "b ≈ +5.6" uses the R_∞ + b/t fit, whose χ²/dof is 101.
  - An adequate fit gives b = 4.04 with c = 39 (free R_∞), or b = 4.08 ± 0.05 (R_∞ fixed at 38/81), with χ²/dof 0.16-0.18
    (E2).
  - Damped like the linear term, the σ⁴ coefficient would be ≈ -15·(R1/R0) = -1.2. The observed +4.1 has the opposite sign
    and is not small.
  - So the qualitative finding ("created undamped at the averaging step") stands.
- **Fix:** at l.2279 and LOG l.334, replace "+5.6" by "≈ +4.1 (from a fit R_∞ + b/t + c/t², χ²/dof 0.16; the two-parameter
  fit gives 5.6)".
- **The garbled clause at l.2130-2131** ("the left side is then …") repeats itself. Also define c_N for N ≥ 3: NA-GS1 is
  SU(2) only, and the SU(N) O(σ²) coefficient is not proven.

### (NA-R2) OPEN (l.2127-2138): CONFIRMED as correctly OPEN
- **"Two readings of one estimate" (l.2249-2250) and the DAG line "H-lin^S ≡ NA-R2" (l.633) overclaim. The two objects
  differ:**
  - NA-R2 bounds the *expectation* of the floor in a *flat* background;
  - H-lin^S needs an *L¹, pathwise* linearisation of a synchronous difference at *general* backgrounds drawn from the limit
    law.
- **What is true:** H-lin^S needs a background-uniform, pathwise version of NA-R2's remainder.
- **Fix:** write "H-lin^S ⇐ (NA-R2^bg), a background-uniform pathwise form of NA-R2 (ARGUED)" at l.633, l.2249,
  l.2355 and l.2371. ARGUED becomes 16.

### Proposition H-cont^S-red (l.2206-2236): CONFIRMED-WITH-FIX
- **What checks out:**
  - (i) the Markov property of the tree; the shared variables at resolutions ≥ n;
  - (ii) the tower property plus conditional Jensen; uniform convergence of F̂_K (jointly continuous kernels on compact
    spaces) together with weak convergence of ν_{K,n};
  - (iii) |x|² ≤ 2|x| for |x| ≤ 2;
  - (iv) characters determine unitary representations of π_1 up to equivalence, U(N) conjugation reduces to SU(N)
    conjugation up to scalars, and Stone-Weierstrass applies.
- **Fix (l.2207-2210).** F may use shifted classes [b] whose level exceeds n(a). Then "E[F | res ≥ n] is a function of
  the shared U^{(n)}" is false: it depends on resolution-n variables of class [b]_n.
  - Put n := max(n(a), levels of F's classes). Then [b + a]_n = [b]_n, and (i)-(ii) hold with F̂ a function of finitely
    many resolution-n variables of those classes.
- **The free instance (l.2235-2236) is right**: under synchronous coupling the noise cancels in the curvature.

---

## (5) ASSEMBLY §15.6 and its hypothesis table

### (I) "Unconditionally": CONFIRMED-WITH-FIX
- **The OS claims need ℓ_0 → ∞.**
  - The OS claims (H ≥ 0, the semigroup, 𝒦 = {0}) rest on X-OS, whose setting is "time side ℓ_0 → ∞ jointly with K"
    (l.348). On a fixed time-periodic torus, τ_s does not preserve the positive-half algebra, and X-OS says the
    finite-temperature version is "not written out" (l.377-378).
  - **Fix (l.2324):** "(limit states: fixed torus, or jointly with the torus side → ∞; the OS statements: with the time
    side → ∞, as in X-OS)".
- **Correctly unconditional:**
  - limit, projectivity, symmetries, RP on the open-support class;
  - the unitary L-adic spatial translations;
  - C-invariance. NA-3's proof shows the kernels and μ_K are C-invariant; cite it as "(proof of NA-3)".
- **Add to (I):** "H^S_ω may be CΩ (it is, in the free (F)-type soft chain)". Do not leave this only under "Not
  delivered".

### (II) and (III): CONFIRMED
- These are CB/X-IVND^S and CB-sg/H-Bal-3T^S/X-NTAF^S, with the RX34 hypothesis sets.
- The lower bound is correctly marked kernel-only.
- The upper bound C(log m)^{2p_*}/m uses (F) through g^S_m² ≤ (β_-m log L)^{-1}. Its constant depends on β_-. Fine.

### (IV): CONFIRMED (conditional on H-cont^S_sp), with the H-cont^S-red class fix.

### Hypothesis table

| Row | Verdict |
|---|---|
| X-LRP | CONFIRMED (matches §6) |
| (C), (L), D4-norm (2): "PROVEN in layer 1" | **GAP (provenance).** (L) is proven *here* (§13.1, definition plus nesting). (C)'s reflection identities are re-derived here (§13.1; RX34 (3)). L9a′ and D4-norm (2) are layer-1 results **imported, not re-verified by this lane**. Write "imported from layer 1 (PROVEN there per P's status; not re-verified here)". |
| missing | **A1** (LINEAR_PACKAGE Lemma 2.2; used by GS (ii), hence by PLD-G^S and NA-GS1), **(R)** (re-checked by x4 A) and **(IT)** (re-derived, §14.1). Add them, with those labels. |
| (F) | CONFIRMED-WITH-FIX. "Includes the kernel-noise contribution" (l.2351, l.2161-2164) turns (F) into a **self-consistency condition**: the kernel couplings must equal the effective couplings that the kernels themselves help produce. Say so, and mark it ARGUED. "By definition" hides it. |
| (RLF-3^dis) | CONFIRMED. The wording matches RX34-fix 5. HIST.md and FLOW.md are honestly marked "not read". |
| (PLD^mod_dis) | CONFIRMED ("only an unconditioned noncompact free analogue"). This is the correct wording; propagate it (§3). |
| smallness | CONFIRMED |
| (H-cont^S_sp) | CONFIRMED-WITH-FIX. "N5 covariance bounds (PROOF; …)" must add "**N5 OPEN in layer 1 at levels i ≥ 1**" (PROOF.md l.14, l.2137; the lane's own l.940 says OPEN). Also "(H-lin^S) = (NA-R2)" → "⇐ (NA-R2^bg)" (§4). |

**Is anything claimed unconditional that is not?**
- The fixed-torus OS claim, in (I). That is all.
- The provenance cells overstate the status of two layer-1 imports (L9a′, D4-norm (2)) and leave out A1. Neither changes
  a conclusion.

---

## (6) Checks x4, x5: re-run and audit

- **Re-run.** Same conditions as above.
  - `x4_out.txt` is **byte-identical** (`diff` empty): 12.2 s, 229 MB.
  - `x5_out.txt` is identical except the three wall-time fields: 287.8 s, 860 MB peak.
- **Pre-registration order** (local mtimes, EDT = UTC - 4):
  - x4: criteria 18:56:36 < script 18:58:29 < out 18:58:54. §14.0 is stamped 22:54 UTC. Consistent.
  - x5: criteria 19:21:17 < script 19:29:29 < run 19:30:24-19:35:13 < post-hoc 19:41:14. §15.0 is stamped 23:21 UTC, the
    same minute as the criteria, and the lane says the criteria came first. The post-hoc run is labelled. Consistent.
- **x4: PASS is honest.**
  - **A (literal S4′ code)** and **B1 (position space)** are the independent tests.
  - **B2 and C use the symbol of GS-2 (e).** So they confirm internal consistency rather than test (e) independently.
    B1 covers (b) and (d) independently.
  - **D is weak.** It cannot fail once the closed form holds: the formula is a convergent geometric series, and the
    "independent route" sums B2 values.
  - **So T11's decisive content is B1 + A, plus the written proof.** The RuntimeWarnings come from `np.where`, which
    evaluates both branches. They are harmless.
- **x5 A: PASS is honest.**
  - **A3(i) tests convolution algebra on samples built as W_cZ_c by construction.** It checks the algebra of NA-2, not the
    kernel.
  - **A3(ii) is the only test of the kernel.** Its comp-1 value of -3.8 SE was inside the pre-stated 4 SE.
  - **The post-hoc run did not test the same M.** It used new seeds, hence new M.
  - **Reviewer replay (E1).** I reproduced the exact rng stream and recovered the same M (r = 0.3245). Fresh sampling with
    2.03·10⁶ accepted samples gives vector components at **+1.33, -0.47, +1.46 SE**; comp 1 = +3.3e-4, against x5's
    -3.0e-3. No bias at the level ≥ 5·10⁻⁴.
  - **Verdict: a fluctuation.** It is about p ≈ 4·10⁻³ over x5's ~27 z-tests: unusual but not alarming. NA-1 (c) is exact
    algebra in any case.
- **x5 B: PASS is honest, and stronger than reported.**
  - **The criterion.** The pre-stated test passes on the 0.015 tolerance: |0.46111 - 0.46914| = 0.008. Also
    R(400) = 0.47962 is within 2.23% of 38/81.
  - **The two-parameter fit.** On its own statistics, the R_∞ + b/t fit puts R_∞ 19 SE from 38/81, which is why it is
    inadequate (χ²/dof 101).
  - **The adequate fit (E2).** With R_∞ + b/t + c/t²: χ²/dof = **0.16**, R_∞ = **0.46943 ± 0.00064**, (R_∞ - 38/81)/SE =
    **+0.47**.
  - **What the data show.** (R - 38/81)·t = 5.61, 4.82, 4.49, 4.31, 4.21: plain curvature in 1/t.
  - **Conclusion.** The pass is honest, and the lane's caveat (l.2276-2277) is accurate. Only b ≈ 5.6 needs correcting
    (§4).
  - **Discrimination.** BIAS would need R_∞ > 1, against a depth-0 value of 6.
- **x5 C (informational): CONFIRMED.**
  - It tests noise at the fine level only, followed by two deterministic steps.
  - The ratio 0.1062 vs 0.1059 supports "the excess is damped afterwards".
  - It used one t and 24 samples, so it is suggestive, not proof.

---

## (7) Public statement

- **§12.1 as it stands is not false.** It is incomplete in one respect: soft time continuity.
- **§15.5's narrower clause is ACCEPTED, word for word.** Replace, in §12.1, "(a moderate-deviation bound for the
  small-field measure, for which no instance is established for the soft chain, even for free fields)" with:
  > (a moderate-deviation bound for the small-field measure; for the soft chain only an analogue for the unconditioned law
  > of the free, noncompact abelian model is established, and the compact interacting case is open)
  - It is accurate: PLD-G^S is CONFIRMED, it concerns the unconditioned law of N² - 1 abelian copies, and it does not
    attach a conditioned hypothesis to it.
- **The time-continuity clause is ACCEPTED WITH CHANGES.** X-KER^S (iv) is confirmed, but the §15.5 candidate:
  - drops the deterministic branch's open item;
  - says "strongly continuous" without the L-adic qualifier;
  - leaves room for the reading "time continuity of the theory".
- **Word-for-word replacement.**
  - **After** "…that complement may be one-dimensional, in which case H is trivial." insert:
    > For the soft variables, whose positive-time observables are by definition supported at positive distance from the
    > reflection plane, that kernel is trivial, so the L-adic Euclidean time translations are the restriction of a
    > strongly continuous semigroup e^{-sH} on the whole Hilbert space; this is a Hilbert-space consequence of reflection
    > positivity and of that choice of observables, and it says nothing about whether the Hilbert space is more than
    > one-dimensional.
  - **Replace** "Time continuity (kernel of the transfer operator = 0), Euclidean invariance, …" with:
    > Time continuity for continuous-block-average observables that touch the reflection plane, continuity of spatial
    > translations, Euclidean invariance, the OS regularity axiom for local fields, a Hilbert space of dimension greater
    > than one, uniqueness, clustering and a mass gap are not established.
- **§12.1's PLD clause and §12.2.** Both edits above are licensed by this review. Apply them in session 7, tagged
  [RX56-fix].

---

## (8) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| RX34 fixes 1-6, 8-12 | CONFIRMED |
| RX34 fix 7 (LOG sentence split); §14.2 heading missing; LOG l.200 | CONFIRMED-WITH-FIX (cosmetic) |
| Lemma GS-1, Lemma GS-2, X-KER^S (i)-(iii), Lemma NA-1, Lemma NA-2, Theorem NA-GS1 | CONFIRMED |
| Theorem GS (A1 imported; (iv) constant 0.0453 / 0.0021, L = 3) | CONFIRMED-WITH-FIX (one WRONG number, diagnostic) |
| Corollary PLD-G^S (mathematics) | CONFIRMED; label "instance of (PLD^mod_dis)" WRONG in 5 places (fix to "unconditioned free analogue") |
| Corollary X-CONT-G^S | CONFIRMED (vacuous under (F)-type couplings; say so) |
| Proposition NA-3 | CONFIRMED; "flat background" missing from 5 headline lines (fix) |
| Theorem X-KER^S (iv) | CONFIRMED (mathematics); framing fix; possibly vacuous (free (F)-type model: H^S_ω = CΩ) |
| Proposition H-cont^S-red | CONFIRMED-WITH-FIX (class level n := max(n(a), class levels)) |
| (NA-R2) OPEN | CONFIRMED; "H-lin^S ≡ NA-R2" GAP (overclaim; ⇐ background-uniform pathwise form, ARGUED) |
| σ⁴ claim | ARGUED, honest; b = 4.1, not 5.6 |
| ASSEMBLY (I) fixed-torus OS | GAP (wording; needs ℓ_0 → ∞) |
| Hypothesis table provenance ((C)/(L)/D4-norm, A1, N5, (F) self-consistency) | CONFIRMED-WITH-FIX |
| §15.5 PLD clause | ACCEPTED word for word |
| §15.5 time-continuity clause | ACCEPTED with changes (text in (7)) |
| x4, x5 | PASS honest; re-run identical |

**Tally.**
- **Claimed:** PROVEN-HERE 46 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 11.
- **Corrected: PROVEN-HERE 46 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 12.**
  - No counted item is demoted.
  - OPEN +1 is the new explicit entry **(H-sig^S) / dim H^S_ω > 1** (binding fix 2). Until now it existed only as "Not
    delivered".
  - ARGUED becomes 16 (uncounted): H-lin^S ⇐ (NA-R2^bg).
- **Substance of the six new counted items:**
  - NA-1, NA-2 and NA-GS1 are kernel-only.
  - NA-3 is a flat-background symmetry fact.
  - X-KER^S (iv) is X-KER (i) for an open-support algebra.
  - H-cont^S-red is a genuine reduction.
  - **None of the six adds information about the Wilson measure.**
- **Session 5's Theorem GS** is the substantive positive result of the two sessions: the soft variables survive the noise
  test.

---

## Binding fixes for session 7

1. **X-KER^S (iv)** (l.2174-2195): add the framing in (2a): it is X-KER (i) for the open-support algebra; it establishes
   continuity on D; the real-s semigroup is interpolation. Add the free-model rank-one remark (2b).
2. **New OPEN entry (H-sig^S).** A K-uniform connected correlation across the plane, liminf_K |Cov_μ(θF̃, G̃)| > 0, for
   some F, G ∈ 𝔄^S_+. Add it to §6, to §15.6 (I) and to "Not delivered". Tally OPEN 12.
3. **"Instance of (PLD^mod_dis)"** → "unconditioned free noncompact analogue" at l.80, 1862, 1888-1889, 1969-1970 and LOG
   l.273.
4. **"In a flat background"** for NA-3 at l.3, l.85-86, l.2115, l.2361 and LOG l.317. For NA-GS1, "(SU(2), flat
   background, fixed K)" at l.3, l.2333-2334 and l.2363.
5. **Theorem GS (iv):** 0.0453 / 0.0021, with "(L = 3)", at l.1840, l.1853 and LOG l.270. In GS (ii), name A1 as
   imported.
6. **"H-lin^S ≡ NA-R2"** → "H-lin^S ⇐ (NA-R2^bg) (ARGUED)" at l.633, 2249-2250, 2355 and 2371. Fix the garbled
   l.2130-2131 and define c_N, or restrict NA-R2's normalisation to SU(2).
7. **H-cont^S-red (i):** n := max(n(a), the levels of F's classes).
8. **ASSEMBLY (I):** OS statements need time side → ∞. Add "H^S_ω may be CΩ". Cite C-invariance as "proof of NA-3".
9. **Hypothesis table:**
   - (C)/(L)/D4-norm provenance as in (5);
   - add A1, (R) and (IT);
   - mark N5 OPEN at levels i ≥ 1;
   - describe (F) as a self-consistency condition (ARGUED).
10. **x5:** b ≈ 4.1 (three-term fit) at l.2279 and LOG l.334. Record E1 (same-M replay, +1.33 SE) and the E2 refit as
    reviewer evidence.
11. **Cosmetic:**
    - insert the §14.2 heading;
    - move the LOG l.209-210 annotation out of the sentence;
    - annotate LOG l.200 "D3 is not needed" with [RX34-fix 8].
12. **§12.1:** apply the two replacements in (7) word for word, tagged [RX56-fix]. Retire §12.2 as superseded.

---

## Strategic verdict

- **What is real.**
  - **Theorem GS is the decisive positive result.** The soft variables do not drift to Haar from accumulated noise. The
    mechanism is exact and simple: white noise is rough, so its block curvature is damped by L^{-2n}.
  - **Session 6's compact extension** (NA-1/NA-2 exact convolution; NA-GS1 at O(σ²)) closes the free-level question as far
    as perturbation theory at fixed K can.
  - **Together these remove risk 1 of REVIEW_X3_X4.**
- **What is illusory progress.**
  - **The removal of the 𝒦 gap.** Correct, but a consequence of choosing open supports. The lane was honest about this in
    l.2194-2195. The gap that matters is non-triviality.
  - **The soft OS form sees only F̃ = E[F | U_0].** In the only computable model with the lane's coupling scheme, F̃ →
    constant, so H^S_ω = CΩ while every analogue of (I)-(III) holds.
  - **The kernel noise is invisible to the OS form.** It therefore cannot help non-triviality. So all kernel-only items
    (KB, LAP^S, NA-1/2/3, NA-GS1) are irrelevant to it.
- **Next target, in order:**
  1. **(H-sig^S) in the free model with constant couplings.** It should hold there, via the massless propagator across the
     plane; check it.
  2. **Identify the interacting input that gives (H-sig^S) uniformly in K.** It must say that the Wilson fine field
     carries an O(g_m) coarse signal that survives kernel smoothing. This is close to H-corr^S with a *lower* bound. None
     of (RLF-3^dis), (PLD^mod_dis) or (F) provides it.
  3. **Only then return to (NA-R2^bg) / H-cont^S_sp.** That gate (spatial continuity) matters only for a non-trivial
    H^S_ω.
- **Layer-1 alignment** (RLF-3 in ratio form) is still the cheapest outstanding request.
- **What not to do.** Do not count further kernel-only or flat-background symmetry facts as progress on existence.
