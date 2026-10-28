# REVIEW_X1_X2: independent hostile review of sessions 1 and 2 of the YM4D existence lane

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session2_snapshot.md (`cmp` empty). All 809 lines were read by offset.
- LOG.md and NOTES.md (all).
- checks/x1_* and x2_*: criteria, scripts, outputs and time files.
- P/literature/NOTES.md §9.1-9.8 and §10 (the CMP 109 transcription and the OSTI abstracts), as the reference for what
  Balaban states.

Line numbers below are EXISTENCE.md lines.

Literature: one open web search, for prior art on X-WIL. No paywall, sign-in or bot check was crossed. Re-runs used
`nice -n 10` with OMP/OpenBLAS/MKL/vecLib threads set to 1, at load 2.7 and 50% free memory. Re-run outputs are in the
scratchpad `rerun_x/`. No other file was edited.

**Bottom line.**
- **The mathematics written here is almost all correct.**
  - Every PROVEN-HERE item survives. 17 survive as written, and 7 need local fixes. None is WRONG as an implication.
- **The hypothesis layer is mislabelled, and that is the main problem.**
  - Only H-Bal-1 (SU(2)) and the small-field *form* in H-Bal-3(3a) are things Balaban states.
  - H-Bal-3 as packaged (law of the *full* measure, the remainder |R| ≤ 1/2, the S4c map, and (3b)) is an extension.
  - H-Bal-3G, -3L, -3T and -loc are new hypotheses. They should not carry an "IMPORTED" status.
  - So no non-soft conclusion of this lane follows from anything Balaban published or claimed.
- **One WRONG statement.** The single-expectation form of H-cont (l.410-411) is vacuous: it is identically zero by
  translation invariance.
- **One overclaim, rated GAP.** The finding that "no single-step norm bound can give H-cont" (l.714-718) is too broad.
- **X-WIL.** The proof is correct. Its novelty is unverified, and the constant (≈10⁻³⁴ in d = 4) makes it a curiosity,
  not a headline.

---

## (1) The H-Bal hypotheses: faithfulness to Balaban

Reference: CMP 109 as transcribed in P NOTES §9, and the CMP 122 I-II OSTI abstracts (P NOTES §10). CMP 102, 116, 119
and 122 have not been read in their primary text by anyone in either lane.

### H-Bal-1 (l.78-84): Balaban states it (SU(2); proof deferred). Label confirmed, with two fixes
- **Matches the source.** The statement matches CMP 109 Theorem 2 / (0.31) exactly:
  - log(L^kε)^{-1} = (K - k) log L;
  - g_K = g, and g_k ∈ ]0, γ].
- **Fix 1a: say the proof was never seen.** Balaban says the proof "will be given in a separate paper" (P §9.4). No lane
  has seen it.
  - For SU(N) the label should be "**plausible extension**". Balaban calls the SU(2) restriction "superficial", which
    is not a proof.
  - The sentence at l.79 should say this.
- **Fix 1b: state volume uniformity.** The volume-uniform and infinite-volume uses (X-NTAF "uniformly in the volume",
  X-IV with (c)) need g_0(ε, g) to be **independent of the torus side M**.
  - This is plausible, since β_j is defined after T → Z^d (CMP 109 (1.22)), but H-Bal-1 does not state it.
  - Add it to H-Bal-1, marked [unverified].

### H-Bal-2 (l.86-93): Balaban claims a UV-stability theorem; its exact form is unverified. Unused
- **What the sources show.** The OSTI abstract of CMP 122 II says the paper completes "the proof of the ultraviolet
  stability". The two-sided e^{±E|T|} form is the standard reading, not a transcription. Label: "Balaban states it (in
  some form)".
- **Not using it is correct.** X-ND, X-MONTEL and X-NTAF are bounds on block laws, which Z bounds alone cannot supply.
- **But do not call it a "main finding" (l.21-24, §0).** What it actually means is stronger and less flattering:
  **the conditional theorem rests on no published Balaban theorem except the small-field form and the deferred flow**.
  Every non-soft conclusion rests on hypotheses that no paper states.

### H-Bal-3 (l.95-112): split. (3a)-form: Balaban states it, for the small-field RG. (3a) as written, (3b) and S4c: plausible extension or new
- **(3a) form: the effective action is right; the measure it describes is not.**
  - Balaban's (0.22)-(0.24) and (0.29) give the effective action of the **small-field-restricted** transformation
    (0.17)-(0.20). There the integrals and the gauge fixing are restricted by χ, and the abstract says "The analysis is
    restricted to small field approximation" (P §9.1).
  - H-Bal-3 asserts this form for the density of the **law of the block variables of the full Wilson measure**. That
    law also contains the large-field histories, absorbed into a multiplicative remainder (1 + R).
  - Balaban never states a representation of the full block law in any paper read by either lane. If it exists, it
    is in CMP 116/122, which are unread. → **plausible extension**.
- **Wrong citation (l.109).** "|E_{K,m}(X)| ≤ E_0 e^{-κd(X)} (CMP 109 (1.18))" cites the wrong bound.
  - (1.18) bounds the **single-step** terms E^{(j)}(X).
  - The cumulative E_k = Σ_j[-β_j A^η + E^{(j)}] (0.23) is controlled only after the β-subtraction, by (0.28)-(0.30):
    |V^{(j)}(X)| ≤ O(1)(L^jη)^{4+α} e^{-κd_j(X)}.
  - Summing k copies of (1.18) gives kE_0, which is not K-uniform.
  - Fix: cite (0.28)-(0.30). State the regrouping of fine-scale polymers into coarse polymers as part of the
    hypothesis, marked [unverified]. Note that (0.29) is given on the regular domain, and that its analytic extension
    with the same constant is [unverified].
- **|R| ≤ 1/2 (l.110-111) is stronger than anything plausible from the R-operation.**
  - The naive count of fine large-field cubes diverges in 4D. This is P's own Proposition LF-count (see P NOTES §10,
    the Dimock lectures).
  - So the large-field histories must be resummed into polymer activities. The natural output is
    |log(1 + R)| ≤ C_R|Λ_m|, not |R| ≤ 1/2.
  - X-ND and X-MONTEL need only K-uniform two-sided bounds. **Fix:** replace |R| ≤ 1/2 by
    e^{-C_R|Λ_m|} ≤ 1 + R ≤ e^{C_R|Λ_m|}, and redo the constants c', c'' in X-ND. The proof is unchanged.
  - This removes the only source of q ∈ [1/3, 3] in the ARGUED H-Bal-3 ⇒ H-Bal-3L remark (l.567-571); see H-Bal-3L.
- **For S4c rather than (0.4).** On small fields S4c equals S4', which is a **diagonal-pairing variant** of (0.4), not
  (0.4) itself. P §9.2 / c17(B): the two differ at second order.
  - Balaban says "we may use many other definitions" (p.254), so this is a plausible extension. It is not "Balaban's
    (0.4)" (l.55, l.138).
  - The large-field caveat at l.156-158 is correctly flagged.
- **(3b), large-field mass ≤ η_0, K-uniform: new hypothesis.**
  - No read source bounds probabilities of the full measure.
  - It is consistent only at fixed m and fixed volume: ν(R_m) decays exponentially in |Λ_m|, so η_0 must depend on m
    and ℓ. Say so; l.101 lists η_0 among the "constants independent of K", which is right but incomplete.

### H-Bal-3G (l.114-119): new hypothesis
- The lane itself says "no source states it". The status IMPORTED-NOT-YET-REVERIFIED is wrong: nothing is being
  imported.

### H-Bal-3L (l.559-571): new hypothesis. The ARGUED link to H-Bal-3 is weaker than stated
- **What it needs.** It needs volume-uniform one-link density ratios on a *local* event G_b with ν(G_b^c) ≤ 1/4.
- **Why H-Bal-3 does not give it.** H-Bal-3's regular set R_m is **global** (all coarse plaquettes regular). In large
  volume ν(R_m(ε_0/2)) → 0, so G_b = R_m(ε_0/2) fails the η_L ≤ 1/4 requirement. The remainder R is global too, so
  its one-link ratio q has no volume-uniform bound.
- The remark at l.570-571 concedes the localisation, but the label "the one-link content of H-Bal-3G" overstates the
  link to H-Bal-3. It is a new local hypothesis.
- **Minor domain fix.** With G_b = R(ε_0/2) and α ≤ ε_0/2, a shift e^{sX} with |s| close to α can push |V_p - 1| past
  ε_0, since e^α - 1 > α. Take α ≤ ε_0/3.

### H-Bal-3T (l.573-578): new hypothesis (Dimock-analogue plausibility only)
- CMP 109 uses the fixed threshold ε_0. The g p(g) thresholds come from Dimock's φ⁴_3 (P §2).
- A volume-uniform per-plaquette tail bound is a localised large-field estimate that is not in any read source.

### H-Bal-loc (l.764-770): new hypothesis
- Every part of it is unstated anywhere:
  - position-dependent complex coupling;
  - a multiscale polymer representation with O(1) activities at every scale;
  - non-vanishing of Z_K on a complex polydisc of coupling fields.
- It is "plausible extension" in spirit only. The non-vanishing of Z_K[1/g_0² + η] for complex η of size r_0, uniformly
  in K, is itself a Lee-Yang/Fisher-zero-type statement for a system with ε^{-4} degrees of freedom per unit volume.
  It should be named as part of the hypothesis.

**Label summary (binding).**

| Hypothesis | Label |
|---|---|
| H-Bal-1 (SU(2)) | Balaban states it (proof deferred, unseen) |
| H-Bal-1 (SU(N), M-uniform) | plausible extension |
| H-Bal-2 | Balaban states it (exact form unverified); unused |
| H-Bal-3(3a), small-field form of the effective action for the small-field RG | Balaban states it (CMP 109 Thm 1/3; induction completed in CMP 116, unread) |
| H-Bal-3(3a) as the density of the full block law, with (1 + R), for S4c | plausible extension |
| H-Bal-3(3b) | new hypothesis |
| H-Bal-3G, H-Bal-3L, H-Bal-3T, H-Bal-loc | new hypothesis |

---

## (2) Part (a): the limit state

### X-S4c (l.131-158): CONFIRMED-WITH-FIX (wording)
- (i) Continuity: if Z_n → C, an eigenphase tends to ±π > r_1 (since r_1 < 2π/N ≤ π).
- (ii) Tracelessness: |Σθ_j| < 2π.
- (iii)-(iv): oddness of ψ and conjugation equivariance, both checked. I also checked link reversal with reference
  S^{-1}: U'_rev = (S e^{avg λ})^{-1}.
- **Fix (l.55, l.138):** "equals S4' (a diagonal-pairing variant of Balaban's (0.4))", not "hence Balaban's (0.4)".
- The finding that the S4c map removes E8* from the consistency question is **real and useful to P**.

### X-ALG (l.160-173): CONFIRMED
- 𝔄 is separable: countable generators, each a bounded sequence, with rational polynomials dense.
- The state space is weak-* compact and metrizable, hence sequentially compact.
- The spectrum is compact metrizable. Standard.

### X-CONS (l.175-185): CONFIRMED-WITH-FIX. As written, the identity in 𝔄 is false
- **What fails.** "F_{f∘A} = F_f in 𝔄" and "f ↦ F_f is a *-homomorphism into 𝔄" both fail in 𝔄 itself.
  - With the convention "constant 1 below the level", F_{f+g} - F_f - F_g = (-1)_{K<m} ≠ 0.
  - F_{f∘A} - F_f is non-zero at K = m.
- **Fix.** Pass to the asymptotic quotient 𝔄_∞ := 𝔄/(𝔄 ∩ c_0(Π_K C(Ω_K))) and set 𝒳 := Spec 𝔄_∞. ω factors through
  𝔄_∞, because ω(F) = lim ω_{K_j}(F) kills c_0. There both identities, and A∘p_{m+1} = p_m, are exact.
- **Second fix.** F_f ∈ 𝔄 only for **coarse-gauge-invariant** f. So p_m maps to the orbit space C_m/𝒢_m.
  - ν_{*,m} on C_m must be defined by ν_*(f) := ω(F_{f̄}), with f̄ the coarse gauge average.
  - This is legitimate because each ν_{K,m} is coarse-gauge invariant: fine gauge transformations at the block centres
    act as arbitrary coarse ones (X-S4c (iii)).
  - X-ND, X-MONTEL and X-IVND silently use this lift; write it once here.
- The substance is proven: consistency across resolutions holds with no hypothesis, given S4c.

### X-SYM (l.187-194), X-FLOW (l.216-223): CONFIRMED.

### X-FLOW-NL (l.225-240): CONFIRMED-WITH-FIX
- **The linearisation is right.** Ȧ = -d*dA, Ḟ = -Δ_2F, Δ_2 acts componentwise as the scalar Laplacian (x1 A2, exact),
  and the heat kernel is a product of Bessel functions.
- **But "non-zero for links b at any distance" is false on a torus.** The periodised kernel is symmetric under
  x_μ ↦ n - x_μ, so K_τ(x) - K_τ(x - e_μ) vanishes at x_μ = (n+1)/2 for odd n.
  - Fix: say "on Z^4, and on the torus for all but the antipodal-symmetric offsets".
- The conclusion (non-locality) needs only some far link, so it stands.
- **Second fix (l.240).** Say "X-RP does not apply to flowed loops". The text says "exact RP is not available", but
  non-locality does not prove that RP fails.

---

## (3) Part (b): RP, OS, ker T, two grids, the Gaussian estimate

### X-PLANES (l.67-69), X-LRP (l.196-205): CONFIRMED
- **Plane arithmetic.** P_m ⊂ P_{m+1} for odd L.
- **Torus.** Antipodal planes lie in P_m, and two disjoint layers of crossing links can be gauge-fixed independently.
- **X-LRP.** This is the standard Osterwalder-Seiler argument, and it holds for bounded measurable F.

### X-RP (l.207-214): CONFIRMED
- Locality holds through the iterated map: the fine-link dependence stays inside the union of the coarse blocks and
  their crossing links.
- θ maps resolution-m tilings, m < m_0, to D-shifted tilings, so θ(F) is again a generator.

### X-OS (l.242-269): CONFIRMED, with one honesty remark
- **Positivity.** I re-derived it: θ'(τ_sF) = θF for θ' the reflection in Π_0 + s/2, and Π_0 + jL^{-m} ∈ P_m.
- **Contraction.** It follows by iterated Cauchy-Schwarz.
- **Positive roots and the spectral statements (iii)-(iv).** These are correct.
- **Remark to add.** Nothing excludes 𝒦^⊥ = CΩ, i.e. a state that decorrelates across Π, in which case H = 0. "A
  Hamiltonian H ≥ 0 exists for every limit point" (l.266) is true but possibly vacuous. A public text must not present
  it as a non-trivial OS reconstruction.
- The construction is the textbook dense-lattice-time OS argument. It is correct, but not new.

### X-KER (l.651-662): CONFIRMED-WITH-FIX
- **The gap in (i).** The proof shows only [𝔄_{++}] ⊂ 𝒦^⊥. The "iff" in (i) also needs the reverse inclusion, which
  is not written.
- **Fix: add the reverse inclusion.** T(s)[𝔄_+] ⊂ [𝔄_{++}(s)] (by (iii)), and T(s)[𝔄_+] is dense in
  closure(Ran T(s)) = 𝒦^⊥. Hence closure[𝔄_{++}] = 𝒦^⊥ exactly.
- (ii) and (iii) are correct: Cauchy-Schwarz in L²(ω) plus θ-invariance of ω.

### X-CONT (l.408-417): WRONG as stated (it is an OPEN item, so the tally is unaffected)
- **Why it is vacuous.** The statement bounds |E_K[F(V_{K,a})] - E_K[F(V_{K,0})]|. For a ∈ D and K ≥ level(a), μ_K is
  invariant under the translation by a. So this difference is **identically 0**.
- **What X-OS (iv) and X-KER (iii) actually need** is the joint, L² form:
  sup_K E_K|F(V^(m)_{K,a}) - F(V^(m)_{K,0})|² ≤ C|X|_m (L^m|a|)^γ.
  This is exactly what the X-2GRID reading (l.679-680) and X-CONT-G use. "Joint version for products" (l.411) gestures
  at it.
- **Fix:** replace the statement with the L² form, and delete the single-expectation form.

### X-2GRID (l.664-680): CONFIRMED (an identity of definitions)
- Tilings at resolutions r ≥ n coincide because s ∈ L^{-r}Z^4. The level-(n-1) tiling is shifted by j level-n sites,
  and A is translation covariant.
- The reading at l.679-680 is correct. |F_s - F_0|² ∈ 𝔄, so the K-uniform L² bound passes to ω, and s_n = 2L^{-n} ∈
  2D_+ suffices for X-KER (iii).

### X-CONT-G (l.682-706): CONFIRMED
- **Re-derived.** I re-derived (ii) line by line: slab size jℓ³; ||ψ_slab||_1 = ℓ²; the transverse/in-plane counts ℓ²
  and jℓ, giving 4w and 4w²; (iii) ≤ 1/β.
- **Two caveats for the record.**
  - The composite-flux formula (i) is taken from P's Lemma 2.2(i). **x2 B does not test (i).** It builds ψ from formula
    (i) and checks the norm bounds, so (i)'s check status is whatever P's check of Lemma 2.2(i) is.
  - x2 B1 tests only 4w for both orientations, so the in-plane 4w² claim is untested by x2. It is proven, so this is
    minor.
- The data show V ∝ w² for both orientations (factor ≈ 9 per level at j = 1), so the proven w is not sharp. That is
  harmless.

### "Finding" (l.714-718): GAP (overclaim)
- "No single-step norm bound can give H-cont" / "H-cont cannot be reduced to a single-step bound in a norm on
  single-step outputs" is argued from one Gaussian example. It is also only true for *local* norms.
- X-CONT-G's own proof is a single-resolution bound in a dual norm: ⟨τ_sψ - ψ, Π_ex(τ_sψ - ψ)⟩, an H^{-1}-type norm
  of the one-step difference.
- The O(1) one-step discrepancy (x2 B3(a)) just reflects that at one step the relative shift is w = j/L, which is not
  small.
- **Fix:** "the single-step discrepancy is O(w) = O(1) in every per-plaquette (local) norm; smallness is visible only in
  a dual norm of the composite test form". Label it ARGUED.

### H-corr + H-lin ⇒ H-cont (l.720-733): ARGUED, correctly labelled
- The remark that the small-field single step needs the fluctuation covariance (CMP 99, P's N5) is accurate, and
  important: **part (b)'s missing piece is blocked on layer 1**.

### X-ARP (l.399-406): CONFIRMED
- The expansion and the bounds −2δ||G|| − δ² are right.

---

## (4) Part (c): non-triviality

### X-ND (l.279-295): CONFIRMED-WITH-FIX
- **The proof is correct.**
  - Normalisation: 𝒵^{-1} ≤ 1/(c' Haar R) from ν(R) ≤ 1.
  - Lower bound: 𝒵^{-1} ≥ (1 - η_0)/(c'' Haar R) from (3b).
  - Then Riesz and Portmanteau.
- **Fixes.**
  - Use the gauge lift (X-CONS fix).
  - Re-do the constants with the weakened remainder (1 + R ∈ e^{±C_R|Λ_m|}).
  - Say "weak non-triviality": block laws at fixed resolution are neither flat nor Haar. With g fixed at the unit scale
    *by hypothesis* (g_K = g), this is close to built in. It is not non-Gaussianity.

### X-MONTEL (l.297-310), X-CAUCHY (l.312-320): CONFIRMED
- Montel in several variables applies on the fixed complex neighbourhood with finitely many polymers.
- The weak-* L^∞ subsequence for R and the compactness of 𝒵 are correct.
- The Cauchy estimate gives T_n(B) = f^{(n)}(0)||B||^n/n!, bounded by E_0e^{-κd}(g||B||/α)^n.
- **Caveat.** O(g^n) depends entirely on the analyticity radius α being g-independent in coarse units. Balaban's
  domains (α_0, α_1, ε_0 fixed constants; P §9.4) support this. Mark it [unverified for the full law].

### C2, LAP-1 (l.580-599): CONFIRMED
- **C2.** I re-derived it: 2Ax/(1 - x) ≤ (8/3)Ax for x ≤ 1/4.
- **LAP-1 pair inequality.** The linear term cancels between ±s. With s² ≤ g² and g ≤ γ, the product ratio is
  ≥ (1/9)e^{-2C_*}, and AM-GM gives c = e^{-C_*}/3.
- **The rest of LAP-1.**
  - The change of variables under T_u is correct.
  - Disjointness: |u - u'| = |V'_pV_p^{-1} - 1| ≤ |V'_p - V_p|.
  - Packing: (2/π)|σ| ≤ |e^{σX} - 1| for |σ| ≤ π, and J ≥ 1/(2πr) for r ≤ 1/(2π).
  - The lemma is neat and correct.

### X-NTAF, X-NTAF-AF (l.601-622): CONFIRMED-WITH-FIX
- **Constants re-derived.**
  - r_*: 3πr_*e^{C_*} = 1/4.
  - δ_* = r_*²/(2N) = e^{-2C_*}/(288π²N). It agrees with x2's printed 9.73e-16.
- **Monotonicity of φ.** φ is increasing on (0, e^{-p_*}], and G_m ≤ g ≤ γ ≤ e^{-p_*}.
- **The asymptotic forms of the corollary are correct.**
- **Fixes.**
  - "Uniformly in the volume" needs H-Bal-1's M-uniformity (Fix 1b).
  - The asymptotic-freedom behaviour is an **input** (H-Bal-1). The theorem converts it into a statement about the
    state. Write "given H-Bal-1, -3L, -3T" in §0's row (c) and in every place it is called "the asymptotic-freedom
    signature" (l.32, l.614-622).
  - "Excludes massless free fields … and any theory whose block plaquettes approach the free value with a power"
    (l.620-622) is a statement about this state under these hypotheses only.

### X-WIL (l.624-632): CONFIRMED; novelty unverified; do not headline
- **Proof re-derived.**
  - The density is exp(-(1/g²)Σ|U_p - 1|²) in the HS convention.
  - The holomorphic increment is -tr((e^{sX} - 1)U') - tr(U'^*(e^{-sX} - 1)).
  - Each term is ≤ √N|e^{±sX} - 1|_HS ≤ √N(e^{|s|} - 1), using |X^n|_HS ≤ 1.
  - There are 2(d - 1) plaquettes per link, so A_1 = 4(d - 1)√N(e - 1).
  - With E_1 = 0 and η_L = 0, the bound holds for d ≥ 2, any N, any finite periodic lattice and g ≤ 1/2.
- **Strength.** In d = 4, N = 2: C_W ≈ 38.9 and δ_W ≈ 2·10⁻³⁴, against the true ≈ 3/8 (x2 A3 in 2D).
- **The bound is not trivial.** A naive conditional-on-the-staple argument loses e^{O(1/g²)}. The ±s/AM-GM cancellation
  is what makes it work.
- **Novelty.** A brief open search found weak-coupling *series* for ⟨P⟩ (e.g. arXiv:1205.6076, 2502.14421) and
  bootstrap *numerical* bounds (arXiv:2404.17071). It found no rigorous 1/β lower bound. This does **not** establish
  novelty: the result is of the elementary type that is often folklore (one-link Laplace / Brascamp-Lieb-type).
- **Public status.** "An elementary rigorous lower bound; a literature search is required before calling it new."

### X-IVND (l.339-344): CONFIRMED-WITH-FIX
- f must be gauge invariant to lie in 𝔄. Either take O_Y gauge invariant, or state the bound for the gauge-averaged
  marginal.
- "Not Haar" needs η_0 below the Haar probability of an irregular plaquette, which is 1 - O(ε_0^{N²-1}). State this
  condition.

---

## (5) Part (d): infinite volume

### X-IV (l.271-277): CONFIRMED
- The soft structure passes to the limit: a bounded-support F lies in the positive slab for ℓ_j large.
- The bare coupling may depend on ℓ unless Fix 1b is added. The soft results do not care; their interpretation as one
  theory does.

### X-IR (l.430-441): OPEN, honestly recorded.

---

## (6) Sources: H-src reduction and counterterm cancellation

### X-MOM (l.357-379): CONFIRMED (implication)
- **The steps are right.**
  - Moment bound from E e^{±Φ(h)}.
  - Diagonal subsequence and multilinear extension.
  - Kernel theorem; Carleman/method of moments; Minlos.
  - The exponential bound passes only for N(f) ≤ c_0/2, which the text correctly limits.
- **Minor.** "OS0 in the Glimm-Jaffe form" overstates: Glimm-Jaffe's form holds for all f, this one for small f. Also,
  (iv) needs θΦ_K(f) = Φ_K(θf); state it.

### X-SRC-CT (l.752-762): CONFIRMED
- **(i)** A ball of radius < δ/2 meets at most one support, and inclusion-exclusion over n ≥ 2 variables kills
  functions independent of any z_i.
- **(ii)** κ = ∂^nΔΨ(0), with a polydisc Cauchy bound C_s r_0^{-n}.
- **The "exact cancellation of divergent counterterms" is correct but elementary.** All the content is in H-src' /
  H-Bal-loc. The one-point function, which diverges like ε^{-4}g_0², and the coincident-point terms are untouched
  (H-src'-diag, OPEN). This is honestly said.

### X-SRC-RED (l.772-786): CONFIRMED | H-Bal-loc
- **Distance bound.** d_r ≥ δL^r/M - 4: cube diameter 2·side, two cubes.
- **The rest of the bound.**
  - The cube count |T|L^{4r}/M^4 is right.
  - The anchored polymer sum is ≤ K_0, with 2^n terms, and the r-sum converges.
  - Non-connecting polymers cancel exactly.
- **Constants.** e^{4(κ-κ_0)} ≥ e^{605} with κ_0 ≈ 151: the bound is K-uniform, not small.
- **The weight is on H-Bal-loc.** It asks for O(1) polymer activities at *every* scale, analytic in a complex coupling
  field, and for Z_K ≠ 0 on the polydisc. Both are new (§1).

### X-SRC-GAP (l.381-397): ARGUED items correctly uncounted.

---

## (7) Checks x1, x2

- **Re-runs.** Both re-run at load 2.7 and 50% free, nice 10, threads 1. **Outputs are byte-identical** to x1_out.txt
  and x2_out.txt. Times 0.43 s and 0.38 s; peak 67 MB and 163 MB.
- **Pre-registration.** The mtime order is consistent with criteria first:
  - x1_criteria 16:41:42 < script 16:42:29 < out 16:42:37;
  - x2_criteria 17:04:32 < script 17:05:26 < out 17:05:43.
  This is consistent with, not proof of, pre-registration. No criterion was edited after its output.
- **x1 (X-FLOW-NL).** A1-A3 exact; B1, B2 as reported. Load-bearing for the lattice identity "Hodge = componentwise
  scalar Laplacian", which is standard.
  - B2 uses an offset (2,2,2,2) on side 5. That avoids the symmetric zero noted above, so it is valid but does not
    probe the torus caveat.
- **x2 A (LAP-1).**
  - **Model check.** Haar weight sin²θ; |U - 1|²_HS = 8 sin²(θ/2); 1 - P = 1 - cos θ; the quadrature for ν(T_uS) on S³
    is correct; relative error 2e-11.
  - **A1 and A2 are not discriminating.** The bound is 10⁻¹⁸ against a measured 10⁻³, so no plausible error in LAP-1
    could fail them.
  - **A4 is the real test,** and it passes with margin. Minor deviation: the script checks ν(T_uS) ≥ c_sν(S), while the
    criterion states the ± sum. They are equivalent here by the u ↔ u^{-1} symmetry, but the equivalence should have
    been stated.
- **x2 B (X-CONT-G).** The Fourier symbol of Π_ex is right ((λ_μ + λ_ν)/λ on the diagonal component), and the shift
  multiplier is right.
  - It checks (ii)/(iii) given (i), not (i) itself.
  - B1 does not test the 4w² in-plane claim.
- **Verdict.** Both PASS as reported. Neither check carries a load-bearing PROVEN claim that the written proofs do not
  already carry.

---

## (8) Overclaims and missing "given H-…"

1. **§0 l.21-24 "Main finding (structural)".** Rewrite as: "Every non-soft conclusion rests on hypotheses (H-Bal-3,
   -3G, -3L, -3T, -loc) that no published paper states. The published Z-stability theorem (H-Bal-2) is not sufficient
   and not used."
2. **§0 table row (b) l.29.** Add "H ≥ 0 on 𝒦^⊥, which may be CΩ: possibly trivial without (c)".
3. **§0 row (c) l.31-32.** Write "given H-Bal-1, -3 (new form)" and "given H-Bal-1, -3L, -3T (new hypotheses)" in the
   *Delivered* column, not only in *From*. "Asymptotic freedom" is an input; say "AF-type running of the block
   plaquette, given the flow hypothesis".
4. **Status legend / tally l.37-38, l.467.** Create the status **HYPOTHESIS (new; no source)** for H-Bal-3G, -3L, -3T,
   -loc and for H-Bal-3's full-law packaging. IMPORTED-NOT-YET-REVERIFIED is reserved for things a source states.
5. **§10.4 l.790 "rests on … nothing else".** Add the S4c-compatibility of the large-field bookkeeping (listed OPEN at
   l.468) and the M-uniformity of H-Bal-1.
6. **l.804-806 "Unconditional … part (a)".** Correct, but add that it is standard compactness and RP. Magnen-
   Rivasseau-Sénéor already describe this layer (NOTES §2). New in substance are only S4c, X-CONS and X-KER.
7. **LOG Session 2 finding 1.** "X-NTAF proven in two-sided form" needs "(conditional on three hypotheses no source
   states)".
8. **l.714-718.** Narrow as in §3 above.

---

## Verdict counts

| Item | Verdict |
|---|---|
| X-PLANES, X-ALG, X-SYM, X-RP, X-FLOW, X-OS, X-IV, X-ARP, X-MOM, X-MONTEL, X-CAUCHY, LAP-1 (+C2), X-WIL, X-2GRID, X-CONT-G, X-SRC-CT, X-SRC-RED | CONFIRMED (17) |
| X-S4c, X-CONS, X-FLOW-NL, X-ND, X-IVND, X-NTAF (+AF), X-KER | CONFIRMED-WITH-FIX (7) |
| X-CONT single-expectation H-cont statement (OPEN item) | WRONG (vacuous) |
| "No single-step norm bound" finding | GAP (overclaim; narrow to ARGUED) |
| H-Bal-3 citation of (1.18) | WRONG citation → (0.28)-(0.30) |
| Status of H-Bal-3G/3L/3T/loc as IMPORTED | WRONG label → HYPOTHESIS (new) |

**Corrected tally:**
- **Claimed:** 24 / 1 / 7 / 11.
- **Corrected:** **PROVEN-HERE 24 (17 clean + 7 after fixes) / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3
  (H-Bal-1, H-Bal-2, H-Bal-3 small-field form) / HYPOTHESIS-NEW 5 (H-Bal-3 full-law packaging (1+R, S4c, 3b), -3G,
  -3L, -3T, -loc) / OPEN 11** (H-cont restated in L² form).
- **Substance.** Of the 24, about six are standard soft facts or identities: X-PLANES, X-ALG, X-IV, X-2GRID, X-ARP,
  X-SRC-CT(i). The substantive new items are X-S4c, X-CONS, X-KER, LAP-1/X-NTAF, X-WIL, X-CONT-G and X-SRC-RED.

---

## Binding fixes for session 3

1. Re-label the hypotheses per the §1 table. Add the status HYPOTHESIS (new; no source).
2. H-Bal-1: add the SU(N) caveat and M-uniformity [unverified].
3. H-Bal-3: cite (0.28)-(0.30), not (1.18); add the fine→coarse polymer regrouping; replace |R| ≤ 1/2 by
   e^{±C_R|Λ_m|}; note η_0 = η_0(m, ℓ); say "diagonal-pairing variant of (0.4)".
4. X-ND: redo c', c'' under fix 3. Strike or re-derive the "q ∈ [1/3, 3] from |R| ≤ 1/2" remark in H-Bal-3L.
5. X-CONS: the quotient 𝔄_∞ and the gauge lift of ν_{*,m}.
6. X-KER (i): add the reverse inclusion.
7. X-CONT: replace the single-expectation H-cont with the L² two-grid form.
8. X-FLOW-NL: the torus symmetric-zero caveat; "X-RP does not apply", not "RP unavailable".
9. X-IVND: the gauge-invariance of O_Y and the η_0 condition for "not Haar". H-Bal-3L: α ≤ ε_0/3.
10. Narrow l.714-718. Add the 𝒦^⊥ = CΩ remark to X-OS and §0.
11. §0 and §10.4 wording per §8. LOG finding 1 "conditional on new hypotheses".
12. X-WIL: label "novelty unverified"; do a literature search (one-link Laplace / Brascamp-Lieb / plaquette lower
    bounds) before any public use.

---

## Public-claim audit

**The strongest statement that could honestly be made public today, word for word:**

> For four-dimensional SU(N) lattice Yang-Mills theory with the Wilson action, we give an unreviewed conditional
> argument with the following content. Unconditionally, by compactness and Osterwalder-Seiler reflection positivity,
> along subsequences of lattice spacings L^{-K} → 0 the lattice measures define limit states on a separable algebra of
> block-averaged variables (a continuous, gauge-covariant averaging map at every L-adic resolution and shift) and of
> gradient-flowed lattice Wilson loops. These states are consistent across resolutions, reflection positive for every
> L-adic block-boundary hyperplane, invariant under L-adic translations and the hypercubic group, and yield an
> Osterwalder-Schrader Hilbert space with a positive self-adjoint generator H on the orthogonal complement of the
> kernel of the transfer operator (possibly trivial). Under additional hypotheses on the laws of the block variables
> (a coupling flow 1/g_m² ≈ 1/g² + O(m log L), which Balaban states for SU(2) with proof deferred, and local,
> volume-uniform one-link density-ratio and tail bounds, which no published work states and which we formulate as
> what Balaban's renormalization-group bounds should imply), the limit block plaquette satisfies
> c/(1/g² + β' m log L) ≤ ⟨1 - P⟩_m ≤ C (log m)^{2p}/m at resolution L^{-m}, uniformly in the volume, so the limit
> is neither flat nor scale invariant. Time continuity (kernel of the transfer operator = 0), Euclidean invariance,
> the OS regularity axiom for local fields, uniqueness, clustering and a mass gap are not established. This is not a
> construction of Yang-Mills theory, and it does not rest on any published large-field theorem.

**What would have to be added to strengthen it, in order of value:**
1. **A derivation of H-Bal-3L/3T (and 3G) from a stated Balaban-type inductive representation.** At minimum: from
   H-Bal-3 plus one named localisation hypothesis on the R-operation, read against CMP 116/122 primary text. This turns
   the "new hypotheses" into "consequences of Balaban's claimed bounds", which is the claim a reader cares about.
2. **𝒦 = {0}** (H-corr + H-lin, or H-bl directly). Only then does the OS reconstruction become a genuine Hamiltonian
   on the full Hilbert space with translation continuity.
3. **Independent review** of §10 (this review covers sessions 1-2 only), and **a literature search for X-WIL**.
4. **SU(N) and M-uniformity** of the flow. The H-src'-diag and OS0 contact terms, and X-ROT, are further off.

---

## Strategic verdict: the next target

The session-2 plan (§8: H-corr for compact U(1)) is a reasonable test of the H-corr interface. It is **not** the
best next move, for three reasons:
- the U(1) weak-coupling continuum limit is a free photon, so the result would be modest;
- H-corr in the non-abelian case is blocked on P's N5, the fluctuation covariance;
- the lane's real public-claim weakness is the provenance of its hypotheses, not ker T.

**Recommended order for session 3:**
1. Apply binding fixes 1-12. They are cheap and change the public statement.
2. **Target: H-Bal-3L ⇐ H-Bal-3(3a) [Balaban form] + H-loc-LF.** H-loc-LF is a single, explicitly stated localisation
   of the large-field remainder: the remainder factorises into polymer activities with an e^{-κd} bound, as in
   Dimock II's large-field polymers.
   - This would turn three new hypotheses into one, closer to what CMP 122 is claimed to give.
   - It uses only the one-link increment analysis: CMP 102 Proposition 9 decay, which is in P's linear package as
     N2-exp.
3. Only then H-bl/H-corr, preferably first as H-bl from H-Bal-3L-type local bounds (§8 item 2). H-bl may not need the
   fluctuation covariance.

Do not spend a session on X-NTAF-sharp. W-AF1 is Balaban's unseen flow paper.

Sources consulted for X-WIL prior art (open access, search listing only):
[arXiv:1205.6076](https://arxiv.org/pdf/1205.6076), [arXiv:2502.14421](https://arxiv.org/pdf/2502.14421),
[arXiv:2404.17071](https://arxiv.com/abs/2404.17071).
