# REVIEW_X9: independent hostile review of session 9 of the YM4D existence lane (§18 and the [RX8-fix] changes)

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session9_snapshot.md (`cmp` empty).
  - `diff session8 session9` read in full (760 lines: the fix hunks and all of §18).
  - §18 (l.3365-3714) read in full by offset; §17.2-§17.3 (O1)-(O3), the class 𝔇_sf and (WC) (l.3000-3068) re-read;
    §15.3 (H-sig^S) (l.2323-2327), §15.6 ASSEMBLY (II)-(III) and "Not delivered" (l.2486-2497); Corollary H-Bal-3T^S
    (l.1762-1767); H-Bal-3T (l.848-851); §12.1 (l.1392-1440).
- LOG.md session 9 (l.529-593) and the RX8-fix lines of LOG session 8 (l.463-502); REVIEW_X8.md (all).
- checks: x8_criteria.md, x8_polyakov.py (read line by line), x8_out.txt, x8_time.txt.
- Read-only layer 1: ../ym4d-proof/PROOF.md S1-S4' (l.524-560); HIST.md l.41 and l.108-109 (the kernel k^{(i)}_c and the
  chain's conditional independence), §20.3 (B) Corollary CLS-cone (l.1370-1395), §25.5 term set and (a3-q) (l.1650-1675).
- No web access. Literature remarks are the reviewer's own knowledge, marked [reviewer knowledge], not load-bearing.

Line numbers are EXISTENCE.md lines unless marked. No file other than this one was edited.

**Bottom line.**
- **All 12 RX8 fixes are applied correctly.** Three residual "K-free" phrases remain (cosmetic).
- **Lemma CTR: CORRECT.** The soft kernel does commute with the spatial centre transformations on the torus. The S4'
  crossing count is right, and so are the Haar invariance, the bare action and the kernel normalisation 𝒩_i. Two
  conditions are inherited and should be stated: (a) the unshifted-grid convention, under which H_μ is a block boundary
  at every level; (b) proper blocks at levels ≤ j.
- **POL-det (i)-(iii): CORRECT.** I re-derived every step:
  - the SU(2) bound F ≥ 3/4 - ||1 - [W_1, W_2]||, including the constant (the commutator equals 2s exactly);
  - the SU(N) compactness argument (a Z_N³-invariant N-atom measure is impossible);
  - both lattice Stokes bounds.
- **Proposition NT-pol^abs and Theorem NT-pol: CORRECT as conditional statements.** The bound is a genuine OS inner
  product across Π_0, not a variance. It is E[f_n(θ(t))·f_n(t)], lower-bounded by a one-slice second moment minus the
  ribbon transport cost. Lemma SMALL is correct (convexity bound, density ratio e^{2E_0N_c}, CLS-cone and (a3-q)). One
  precision item: the "no outer layer on the torus" reading of (a3-q).
- **Corollary NT-pol^OS: CORRECT** given H-Bal-3T^S's inputs + (K9-req). One quantifier precision: sup over K of g^S_{m_*}.
- **Caveat: adequately stated** in §0, §18.4, §18.5, §18.9, LOG and ASSEMBLY. One overstatement: "the coupling **must**
  be exponentially small" describes the proof's sufficient condition, not a property of the model.
- **§18.7 has two binding defects. Proposition SP is correct and important.**
  1. **(WC_∞) and (WC_∞^sp) are false as quantified for local F.** c_∞ (and c_sp) are uniform in g ≤ g_∞. For a fixed
     local F at the unit-lattice scale, the connected correlation is expected to vanish as g → 0 (O(g⁴), §17.1, §17.5;
     (WC) itself has c_Wu_+^{-2}). So a g-uniform c_∞ asks for the opposite of asymptotic freedom.
  2. **The iterated liminf covers only iterated limit points**, while the setting allows joint limits.
  - "Mass gap not needed": CORRECT.
  - "none of the three is implied by the others" is an unproven independence claim.
  - The RP justification of C_F(s_1) ≥ 0 names the wrong plane.
- **x8: honest and correct as read.** A1-A3 PASS, A4 informational, B0/B1 PASS. The re-run under the lock is
  **identical** except wall times (see (6)).
- **§12.1: no change required.** Word-for-word verdict and an optional clause in (7). I recommend not adopting the
  clause yet.
- **Tally.**
  - Claimed: 52 / 1 / 3 / 5 / 12, ARGUED 28.
  - **Corrected: 52 / 1 / 3 / 5 / 12, ARGUED 29** (+1: the independence claim at l.3628-3629, if kept).
- **Strategic.**
  - The Polyakov route is a clean, correct, cheap theorem, and it is honestly labelled as a small-box zero-mode statement.
  - It closes the fixed-torus question that REVIEW_X8 asked the lane to settle deliberately. It is not progress on
    continuum non-triviality, and the lane says so.
  - The decisive item is now (WC_∞^sp), and it must first be re-quantified (binding fix 1).

---

## (1) RX8 fixes (priority 1)

| Fix | Where (session-9 lines) | Verdict |
|---|---|---|
| 1 contractible support; Polyakov O(1); linear-term reading; ARGUED 25 | l.2983-2995; l.3205-3208; §0 l.133-137; LOG l.463-466; l.720, l.3304-3306 | CONFIRMED |
| 2 ν_s = law(U_j given A), A a joint-chain event; (O2) display e^{-S_j}, history-∅ part; covariance of the history construction | l.3095-3103; l.3016-3019 | CONFIRMED. The covariance is stated "as a property of v2's construction that v2 does not list": correct and honest |
| 3 NT-cpt one direction; "dim H > 1 ∀ω ⟺ no product limit point"; converse under convergence; §15.3 "which implies" | l.3083-3090, l.3105-3114; l.2324-2325; LOG l.473 | CONFIRMED. The proof of each direction was re-read and is correct |
| 4 T21 second branch only | l.3271-3275; §0 l.130-131; LOG l.475 | CONFIRMED |
| 5 depth inputs (a)-(c); "no measure-theoretic UV limit"; t_b; θ-/gauge invariance of E | l.3048-3068; l.3116-3119; l.3203-3204; l.3280 | CONFIRMED. **Residuals (cosmetic):** the §17.3 title (l.3044) still reads "a K-free statement"; the table row l.2515 still says "the K-free (WC)" before its own [RX8-fix 5] correction; l.9 is history (leave it). Change the first two to "a depth-uniform finite-dimensional statement" |
| 6 (I_j^E)' re-cited; "not yet written" struck; (SF-bg^tor) narrowed; "global form of S2-1" dropped | l.3009-3015; l.3158-3170; §0 l.136-137; LOG l.487-489 | CONFIRMED. The added reading of (I_k^E)'' (HIST §25.6) is a correct extension (real-point values and bounds only) |
| 7 K8 sign argument | l.3330-3337; LOG l.502 | CONFIRMED (the three-line argument verbatim) |
| 8 (O3) constants | l.3033-3037 | CONFIRMED |
| 9 physical regime | l.3072-3076; T23 l.3212-3214; §0 l.131-132 | CONFIRMED |
| 10 "massless" → CE hypotheses + zero-mode set; "reducible" → singular strata | l.3149-3154, 3158, 3175, 3192-3198, 3282-3284; LOG l.485, 489 | CONFIRMED |
| 11 T24: (WC) consumes CLS-cone ⇐ (AE) | l.3234-3238; l.3290 | CONFIRMED |
| 12 "fixed resolution"; K9 "(RLARGE)"; subsection order; "for some limit point" | l.2978; l.3345-3346; headers l.3224/3250/3270/3311; §0 l.113-114 | CONFIRMED. §17.8 now follows §17.7. The 17.6a header says "text unchanged", which is true of the re-ordering; §17.8's K8 text did change, under fix 7 |

---

## (2) Theorem NT-pol and its lemmas (priority 2)

### Lemma CTR (l.3407-3432): CORRECT, with two inherited conditions to state
- **Does the soft kernel commute with centre transformations on a torus? YES.** Re-derived against PROOF S4'
  (l.541-545) and HIST l.41 (k^{(i)}_c(V, U) = exp(-(κ/g_i²)[1 - N⁻¹Re tr(V⁻¹M̄_c(U))])/𝒩_i(M̄_c(U))):
  - **Crossing coarse link c = (X, X + e_μ), X at x_μ-index -1.**
    - T^σ_y = P^σ(c_X → y)·S_y·P^σ(c_Y → y + Le_μ)^†.
    - The two axial legs stay in their blocks (S4' L0) and do not cross H_μ.
    - The straight leg S_y runs from y ∈ X to y + Le_μ ∈ Y and crosses once, positively.
    - So T^σ_y ↦ zT^σ_y for every σ and y. M̄_c ↦ zM̄_c whether M̄_c is the arithmetic mean or the S4' log-average
      S_c exp(avg log(S_c⁻¹T)): S_c⁻¹T is unchanged and S_c ↦ zS_c.
    - V_c ↦ zV_c, so V⁻¹M̄ is unchanged.
    - 𝒩_i(zM) = 𝒩_i(M) by Haar invariance V' ↦ zV'.
  - **Non-crossing c (direction ν ≠ μ, or direction μ elsewhere).** No leg crosses, and nothing changes.
  - **Bare action and Haar measure.** Each (μ, ν) plaquette straddling H_μ contains one crossing link as U and one as U⁻¹,
    so z cancels. Haar measure is invariant under multiplication by a central element. Correct.
  - **Commutation.** γ commutes with θ (θ is a time reflection and preserves H_μ). f_n∘γ_z = z^nf_n, because W_μ crosses
    H_μ once. E f_n = 0 for n ∉ NZ³. Correct.
- **Inherited conditions (state them; not defects).**
  - (a) **H_μ is a block boundary at every level only under the floor-type block convention.** Level-(i+1) block x
    contains level-i sites {Lx, …, Lx + L - 1}, with root at its centre, so π(-1) = -1 and π(0) = 0. With
    centred-index blocks ({Lx - (L-1)/2, …, Lx + (L-1)/2}), sites -1 and 0 share block 0, and H_μ is not a boundary.
    - It is the same convention that §17 already uses for Π_0 ("unshifted grids", l.2963-2964), so nothing new is
      assumed.
    - Fix: cite that convention once at l.3410.
  - (b) **"Blocks lie on one side of H_μ" needs proper blocks at every level ≤ j.** At levels where the torus side in
    direction μ is 1 block, a block contains both sides. The kernels used are K_i for i < j, which produce level ≤ j
    fields with n_s = TL^{m_*} ≥ 3 sites per side. So this never occurs. Fix: add "(levels ≤ j only; there every block
    is a proper sub-box, n_s ≥ 3)".
- **Weight.** It is the standard centre symmetry. The value added is the S4' check, which is correct.

### Lemma POL-det (l.3434-3470): CORRECT
- **(i) SU(2), re-derived.**
  - ½tr ↔ Re, and ||1 - W||_op = |1 - w| (eigenvalues e^{±iφ}, |1 - w|² = 2 - 2cos φ).
  - **The commuting minimum.** cos²x + cos²y + cos²(x + y) = 1 + 2cos x cos y cos(x + y) (checked at x = y = 0 and
    x = y = π/3). cos x cos y = ½(w + v'). So the triple product is ½(w² + wv') ≥ ½(w² - |w|) ≥ -1/8. Minimum 3/4, at
    (π/3, π/3) (and at (2π/3, 2π/3), which x8 A1 finds).
  - **The non-commuting correction.**
    - Re(pq) - Re(pq') = -sin a sin b(c - σ), of modulus sin a sin b(1 - |c|) ≤ sin a sin b(1 - c²)^{1/2} = s.
    - The squares differ by ≤ 2s, so F(p, q) ≥ 3/4 - 2s.
  - **The commutator.** pq - qp = 2P×Q. With 1 - pqp⁻¹q⁻¹ = (qp - pq)p⁻¹q⁻¹, |1 - [p, q]| = 2|P×Q| = 2s **exactly**, so the
    constant is sharp in the sense used.
  - Verdict: F ≥ 3/4 - ||1 - W_1W_2W_1⁻¹W_2⁻¹||_op holds for all of SU(2) × SU(2).
- **(ii) SU(N), re-derived.**
  - Commuting triples diagonalise simultaneously, and tr W^n = ρ̂(n) for the N-atom phase measure ρ (with multiplicities).
  - N-atom measures on the compact 𝕋³ are weak-* closed, and ρ̂(n) is continuous.
  - ρ̂_∞ = 0 off NZ³ ⇒ ρ_∞ is invariant under translations by (2π/N)Z³. That action of Z_N³ is free, so every orbit has N³
    points of equal mass, and the total mass is ≥ N³ > N. Contradiction.
  - The step from commuting to near-commuting is by compactness of C_δ ↓ commuting set. Correct, and non-explicit
    (stated).
  - The charged set n ∉ NZ³ is the right one: z^n = 1 ∀z ∈ Z_N³ iff every n_μ ≡ 0 mod N.
- **(iii) Lattice Stokes: CORRECT.**
  - ||1 - gh|| ≤ ||1 - g|| + ||1 - h|| follows from 1 - gh = (1 - g) + g(1 - h).
  - The holonomy of a mapped rectangle is a product of conjugated plaquettes (peeling). Non-injective maps are fine:
    |R_n| counts with multiplicity.
  - (a) The covering square of the 2-torus has boundary W_μW_νW_μ⁻¹W_ν⁻¹ up to orientation/order conventions, which do not
    change ||1 - ·||.
  - (b) The ribbon gives W^n(t') = H·GW^n(t)G⁻¹, and |N⁻¹tr((H - 1)A)| ≤ ||H - 1||_op for unitary A. Correct for n with
    negative components too (W^n is a closed path at x_0).

### Proposition NT-pol^abs (l.3474-3491): CORRECT. **Is it an OS inner product? YES.**
- **What it bounds.** Cov_ν(θ(F_2), F_2) = E[F_2(θ(t))F_2(t)] - E[F_2]², with F_2 at slice t ≥ 0 and θ(F_2) at slice -1 - t:
  the OS form ⟨[F_2] - ωF_2·Ω, [F_2] - ωF_2·Ω⟩ across Π_0.
- **How it bounds it.** E[conj(f_n∘θ)f_n] = E|f_n|² + E[conj(f_n∘θ - f_n)f_n]:
  - a one-slice second moment (a variance, because E f_n = 0 by CTR);
  - minus a transport cost controlled by the ribbon through Π_0.
  - The lower bound is therefore a variance minus a deterministic ribbon bound. The quantity bounded is the cross-plane
    correlation. This is the right structure: on flat configurations f_n(θ(t)) = f_n(t) exactly, and the ribbon measures
    the deviation from flatness.
- **Arithmetic, re-derived.**
  - E|Δ_n|² ≤ |R_n|²η by Cauchy-Schwarz, with |R_n| = |n|_1n_sd_t and Σ_{S_2}|n|_1 = 4.
  - The SU(2) cross terms vanish: e_1, e_2, e_1 + e_2 are distinct mod 2.
  - Σ_nE|f_n|² ≥ 3/4 - n_s²η^{1/2} (Jensen).
  - SU(N): P(max comm > δ_N) ≤ 3n_s⁴η/δ_N² (Chebyshev; three planes; (n_s²)² from Cauchy-Schwarz).
  - All correct.
- **Precision (cosmetic).** For SU(N), Cov(θ(f_n)^*, f_n) should be read as the (real, ≥ 0 by RP) OS norm, and the
  Cauchy-Schwarz step as a bound on the real part. Say "Re" once at l.3480.

### Lemma SMALL (l.3493-3513): CORRECT, with one reading to label
- **The convexity bound.** Z(v) ≤ 1, log Z is convex, (log Z)' = -E_{μ_v}𝓔. So E_{μ_u}𝓔 ≤ (2/u)(-log Z(u)). Correct.
- **The entropy lower bound on Z(u).**
  - On B, ||1 - U_p|| ≤ 4u^{-1/2} (||1 - e^X|| ≤ ||X||). The text's 8u^{-1/2} is conservative and harmless (it only sets
    u_0).
  - Haar(B) ≥ (b_Nu^{-(N²-1)/2})^{|ℒ_j|}. (H-up) then gives u𝓔 ≤ 64C_3|𝒫_j| on B.
  - Correct.
- **The density ratio.** (O2) (l.3020-3021) bounds Σ_{X∋x}sup|E(X) - E(X; 1)| ≤ E_0 per cube. So |W - W(1)| ≤ E_0N_c, the
  oscillation is ≤ 2E_0N_c, and dν/dμ_u ≤ e^{2E_0N_c}. Correct.
- **The (H-coer) quote.** It matches HIST l.1372-1395: CLS-cone holds for every chain and every level-k field, and gives
  𝓔^Λ_k ≥ (1/24)ΣE_𝒞(P) ≥ (1/(24C_cone))Σs. **CONDITIONAL ⇐ (AE)**, correctly labelled.
- **The (H-up) reading.**
  - (a3-q) (HIST l.1669-1673) is per full cone of 𝒞^♭(Λ_k). The step "on the torus every chain term lies in a full cone
    (no outer layer)" is the lane's own inference from HIST §25.5's term-set definition, and the text says so.
  - It is plausible: on the periodic torus every level-k plaquette has its four corners in Λ_k.
  - But 𝓔_k = 𝓔^♭_k on the whole torus needs layer 1 to confirm that its torus term set has no 𝒞 ∖ 𝒞^♭ part.
  - Fix: tag the inference "[reading of HIST §25.5, to be confirmed by layer 1]" in the (H-up) item, and list it with the
    (SF-bg^tor) report. It does not change the count, because (H-up) is a consumed hypothesis.
- **η_K ≤ 2N·display + 4δ_LF.** ||1 - U||²_op ≤ Σ_a|1 - e^{iφ_a}|² = 2Ns(U). Correct.
- **Constants (cosmetic).** l.3528 says N_c ≍ T⁴L^{4(m_*-1)}. With n_s = TL^{m_*} level-j sites per side, the count of
  level-j unit cubes is n_s⁴ = T⁴L^{4m_*}. L^{4(m_*-1)} counts level-(j+1) blocks. State which cube (O2) sums over. The
  conclusion (exponential in the box volume) is unchanged.

### Theorem NT-pol (l.3515-3534): CORRECT as a conditional theorem
- Lemma NT-0 + CTR + NT-pol^abs + SMALL give Cov_{P_K}(θF_2, F_2) ≥ 3/8 for K ≥ K_0, at g ≤ g_P.
- **No two-point input; T25's criterion is met. No moduli density.** This is a real improvement on REVIEW_X8's
  alternative 1. The exact centre symmetry plus the algebraic lemma replace the two-sided moduli density.
- Lemma SIG-0 with periodic-reflection RP gives dim H^S_ω > 1 for every finite-torus limit point. Correct.
- **Counting: PROVEN-HERE +2 (NT-pol bundle; SMALL) is admissible.** The non-trivial parts are elementary, but complete.
  Lemma SMALL is honest about consuming two OPEN layer-1 items.

---

## (3) Corollary NT-pol^OS (priority 3): CORRECT, with one quantifier

- **The bound, re-derived.** H-Bal-3T^S (l.1762-1764) gives ν^S(|V_p - 1|_HS ≥ gp(g)) ≤ g² uniformly in K and the volume.
  - On the good event ||1 - V||_op ≤ |·|_HS < gp; elsewhere ||1 - V||²_op ≤ 4 ≤ 4N.
  - So η ≤ g²p² + 4Ng². The condition (n_s² + 4n_sd_t)g(p² + 4N)^{1/2} ≤ 3/8 matches.
- **Inputs.** CTR is torus-shape independent. θ-invariance and X-RP^S need T_0 even. Chessboard (CB) works on even
  anisotropic tori. (RLF-3^dis) on anisotropic tori is exactly (K9-req). All named.
- **Precision (binding, small).** g := g^S_{m_*} = g_{K-m_*} depends on K through the chain's sequence. "For every K" needs
  the condition at every K, i.e. with sup_{K ≥ K_0} g^S_{m_*}(K), which (F) brackets.
  - Fix (l.3540-3541): "let g_+ := sup_K g^S_{m_*} (finite and small by (F)) and suppose (n_s² + 4n_sd_t)·g_+(p(g_+)² +
    4N)^{1/2} ≤ 3/8". p(x) = (log 1/x)^{p_*} is increasing as x ↓ 0 only through log, so monotonicity of x·p(x) on small x
    makes the sup the right quantity.
- **Physics reading: CORRECT and consistent with x8.**
  - At fixed spatial torus and T_0 → ∞, the finite-K transfer matrix has a unique ground state (positive kernel on a
    compact space). So the Polyakov signal is carried by positive-energy electric-flux states of small energy (≍ g²/n_s in
    level-j units), not by vacuum degeneracy [reviewer knowledge].
  - That matches SP's phrase "near-zero-energy sectors" (l.3611-3612). Nothing to change.
- **Re-scoping (H-sig^S) → (H-sig^S_loc) with OPEN unchanged (l.3546-3553): ACCEPTABLE.**
  - §15.3's (H-sig^S) quantifies over "every limit point", and that includes spatial side → ∞, which NT-pol^OS does not
    reach. So the literal entry is **not** fully discharged.
  - The text says so ("at a fixed spatial torus"; l.3554-3555). Keeping OPEN at 12 is the conservative choice.

---

## (4) The honesty caveat (priority 4): ADEQUATE, with one overstatement

| Place | Text | Verdict |
|---|---|---|
| §0 l.146-147 | "Physically a tiny box (coupling exponentially small in the box volume, or g p(g) ≲ 1/n_s²), carried by the holonomy zero modes; not progress on continuum non-triviality" | adequate |
| §18.4 l.3527-3534 | g_P tiny; double-exponential margin to Λ^{-1}; "carried by the toron/centre zero-mode sector"; nothing on contractible support or infinite volume | adequate; **one overstatement (below)** |
| §18.5 l.3548-3549, 3554-3555 | "weak … holonomy zero modes of a small spatial box"; nothing for spatial side → ∞ | adequate |
| §18.9 l.3689-3691, 3710-3711 | caveat; "not counted as progress on continuum non-triviality" | adequate |
| ASSEMBLY l.2494-2496; table l.2515 | "physically small spatial box only; not for local observables, not for spatial side → ∞"; "small-box only" | adequate. Recommended (cosmetic): add "(carried by the holonomy/electric-flux zero-mode sector)" at l.2496 so that ASSEMBLY carries the mechanism, not only the size |
| LOG findings 3-4 | caveat stated, binding | adequate |

- **Overstatement (binding wording).** l.3528-3529: "the coupling must be exponentially small in the box volume".
  - It is the proof's sufficient condition, and the factor e^{2E_0N_c} is an artefact of the crude density ratio. x8 B
    shows the signal at β = 8 on 4³ spatially.
  - What is intrinsic is only box ≪ confinement length. In a large spatial box the spatial Polyakov correlator at fixed
    time separation is suppressed like e^{-σn_sd} in the confined phase [reviewer knowledge].
  - Fix: "the theorem's sufficient condition requires the coupling to be exponentially small in the box volume (an
    artefact of the density bound e^{2E_0N_c}); what is intrinsic is that the box is ≪ the confinement length, since in a
    large box spatial Polyakov correlators are area/length-suppressed". Same at §0 l.146 ("coupling exponentially small"
    → "sufficient condition: coupling exponentially small").
- "Λ^{-1} ≍ e^{u/β_1}" (l.3530): β_1 conventionally names the two-loop coefficient. Write e^{u/(2β_0)}·(…) or define β_1
  (cosmetic).

---

## (5) §18.7: (WC_∞), (WC_∞^sp), Proposition SP (priority 5)

### Proposition SP (l.3600-3612): CORRECT, and the most important observation of the session
- **(i), (ii).**
  - lim C_F(s) = ⟨v, e^{-sH}v⟩ = ∫e^{-sλ}dσ_F, with v = [F] - ω(F)Ω. τ_sF ∈ 𝔄^S_+ for s ≥ 0 and s a multiple of the block
    side.
  - C(0) - C(s_1) → ∫(1 - e^{-s_1λ})dσ_F > 0 ⟺ σ_F((0, ∞)) > 0.
  - Monotone and log-convex (Laplace transform of a positive measure).
  - Correct.
- **(iii), the example.**
  - Cov = ¼|ω_1(F) - ω_2(F)|² for every s is correct **if each ω_i is reflection positive (hence θ-invariant) and
    τ-invariant with H^S_{ω_i} = CΩ**.
  - If θ instead swapped ω_1 ↔ ω_2, the computation changes.
  - Fix (cosmetic, l.3608): "of two distinct RP, θ- and τ-invariant states".
- **The importance is correctly drawn.** "dim H > 1" is met by vacuum degeneracy. The spectral form (ii) is the
  meaningful non-triviality notion in infinite volume. This retroactively qualifies every "dim H > 1" target in the
  lane, and §18.7 says so.

### (WC_∞) / (WC_∞^sp) (l.3614-3619): WRONG as quantified (binding)
- **The g-uniformity of c_∞ and c_sp.**
  - The text reads: ∃m_*, F, g_∞, c_∞ such that ∀g ≤ g_∞, liminf liminf C_F(0) ≥ c_∞.
  - F is a fixed local observable at the unit-lattice resolution m_*, and g is the coupling at the unit lattice.
  - As g → 0 the scale of F is ever deeper in the asymptotically free regime. Its connected cross-plane correlation is
    expected to be O(g⁴) (§17.1, ARGUED; §17.5; x7 A's leading term ∝ g⁴).
  - (WC) itself is stated with c_Wu_+^{-2} ≍ g⁴, and (FS) at l.3646 uses ½c_Wu_+^{-2}.
  - So (WC_∞) as written asks for a g-uniform O(1) lower bound. It is expected to be **false**, and it is inconsistent
    with the lane's own (WC).
- **Why one g suffices.** In the tuned continuum limit, different g at the unit lattice are different choices of the
  unit length relative to Λ: the same theory, rescaled. So **a single g** suffices for non-triviality. "For every
  g ≤ g_∞" is both unnecessary and the source of the problem.
- **Fix (binding).** Either:
  - "there are m_*, F and g > 0 (one coupling suffices: g fixes the unit length relative to Λ) and c_∞ = c_∞(g) > 0
    such that …"; or
  - keep ∀g ≤ g_∞ and write the bound as c_∞u_+^{-2} (equivalently c_∞g⁴), matching (WC).
  - The same for c_sp in (WC_∞^sp).
  - The "minimal IR statement" (l.3659-3661) should be the one-g form.
- **Iterated vs joint limits (binding, precision).**
  - The setting allows K, T_0 → ∞ "jointly or iterated" (l.3590). The bound is an iterated liminf_{T_0,T} liminf_K.
  - "(WC_∞) ⇒ dim H > 1 for every infinite-volume limit point (the liminf is over the full family)" (l.3620-3621) is
    correct for iterated limit points: first K → ∞ at a fixed box, then the box → ∞.
  - It does not cover a limit along a joint sequence (K_n, T_n), which the iterated liminf does not control.
  - Fix: "for every iterated limit point; for joint limits replace the iterated liminf by liminf over (K, T_0, T) with
    K ≥ K_0(T_0, T)".
- **(WC_∞^sp) ⇒ (WC_∞) (l.3622): CONCLUSION CORRECT, the reason names the wrong plane.**
  - C_F(s_1) = E[θ(τ_{s_1/2}F)^*·τ_{s_1/2}F] - |E F|² (use θτ_aθ = τ_{-a} and translation invariance). It is ≥ 0 by RP in
    **Π_0** applied to G = τ_{s_1/2}F.
  - RP in the plane τ_{s_1/2}Π_0 applied to τ_{s_1/2}F returns C_F(0), not C_F(s_1).
  - Fix: "C_F(s_1) = ⟨θ(G), G⟩_conn ≥ 0 with G := τ_{s_1/2}F (RP in Π_0; s_1 an even multiple of the block side)".
- **Clustering (l.3624-3626): CORRECT at ω.** ker H = CΩ gives σ_F({0}) = 0, and then the two forms are equivalent at
  that ω. s_1 and the constant depend on ω, so it is not an equivalence of the box-uniform statements. "at ω" is written,
  which is enough.

### "Mass gap not needed for either" (l.3627-3632): CORRECT
- A gap is an upper bound on (ker H)^⊥. (WC_∞) and (WC_∞^sp) are lower bounds at fixed separation. Existence of limit
  points uses compactness only (states on a separable algebra are weak-* compact).
- **One unproven claim (l.3628-3629).** "Gap + uniqueness + (WC_∞) give (WC_∞^sp); none of the three is implied by the
  others."
  - The first half is correct at a limit point: σ_F ⊂ [m, ∞) gives C(0) - C(s_1) ≥ (1 - e^{-ms_1})C(0). It needs the gap
    to be uniform over limit points for the box-uniform form.
  - The second half is a logical-independence claim with no counterexamples given.
  - Fix: delete "none of the three is implied by the others", or label it ARGUED. Kept: ARGUED +1.
- **(FS) obstruction (l.3645-3652) and (WC^bg) (l.3653-3658).** Correctly ARGUED. The (FS) triangle inequality is valid,
  and the incompatibility argument is a sound heuristic.
- **Items 1-4 of "what must be uniform" (l.3633-3644): CORRECT.** Item 2 is the sharpest: (O3) is a global, extensive
  event, so NT-LF's 6p||F||² fails in infinite volume, and a decoupling form is needed.

### §18.6 twisted route (ARGUED): plausible, as labelled
- With m_{12} = 1, (W_1, W_2) is clock-shift, unique up to conjugation: centre factors on W_1, W_2 are gauge (conjugation
  by Q or P). W_0, W_3 ∈ Z_N, which gives N² isolated points related by centre symmetry.
- Adjoint zero modes would commute with an irreducible pair, so there are none. The Hessian is non-degenerate mod gauge.
- RP is kept: the stack is θ-invariant.
- All consistent with [reviewer knowledge] (van Baal's twisted tori).

---

## (6) Check x8 and the re-run (priority 6)

- **Pre-registration order (local EDT mtimes).** criteria 22:25 (02:25 UTC) < script 22:27 < out 22:49 < time 22:50.
  §18.0 is stamped 02:24 UTC. **Consistent.** No smoke run is claimed.
- **Code read line by line.**
  - **Algebra.** qmul uses -a×b (the anti-isomorphic copy of x7, disclosed). Every check is group-theoretic (conjugation-
    and inversion-invariant norms), so the copy is irrelevant.
  - **A1.** The grid includes 2π/3. The refinement is correct.
  - **A2.** The near-commuting pairs perturb an element of W_1's one-parameter subgroup by exp(εX). The commutator is
    P_1P_2P_1^†P_2^†.
  - **A3.**
    - plaq = U_μ(x)U_ν(x+μ)U_μ(x+ν)^†U_ν(x)^†.
    - T²_{12} = sum over (x_1, x_2) at fixed (t, x_3).
    - Ribbons: R1 sums the (0,1) plaquettes over x_1 at fixed (t, x_2, x_3), and R2 the (0,2) plaquettes over x_2. The
      e_1 + e_2 loop's ribbon is R1 + R2 at the same base point. Correct.
    - The forward accumulation over d = 1..7 from every t covers both ways round for every unordered pair.
  - **A4.** The diagonal phase triples are parametrised with Σ_a α = 0 (det 1). Nelder-Mead minimum (informational).
  - **B.**
    - Kennedy-Pendleton heatbath with α = βk is correct for β·Σ(1 - ½tr U_p) in quaternion form.
    - OR: V̂^†U^†V̂^† preserves Re(UV̂).
    - The checkerboard by total-coordinate parity is valid on even sides.
    - X(d) pairs slices t and 7 - t (the link reflection in planes 7|0, 3|4), averaged over spatial base points.
    - Jackknife over 25 bins of 100 sweeps.
  - **Informational nuance.** The "theorem bound" column uses the mean of s over all six plaquette orientations as η.
    That is not the max over the relevant plaquettes (on 8 × 4³, temporal and spatial plaquettes differ slightly). It is
    informational only, and it is vacuous either way.
- **Verdicts.**
  - A1-A3 PASS and honest.
  - B1 PASS by a wide margin (X(1) - 5 SE ≥ 1.58 at β = 16).
  - "No visible decay with separation" (X(1) ≈ X(3) ≈ X(5) within ≈ 1 SE) matches the zero-mode reading.
  - The centre-sector sticking (E f_n ≈ ±0.7-0.9) is correctly called irrelevant for the γ-invariant X(d), given that the
    sectors are γ-images of one another.
  - Load-bearing: none (stated l.3679-3681).
- **Re-run (reviewer, under the mandatory lock).**
  - Waited from 02:57:05 UTC for another holder; lock acquired 03:28:46 UTC (mkdir); `rmdir` exactly once at 03:33:59 UTC,
    no trap.
  - nice 10; OMP/OpenBLAS/MKL/vecLib threads 1; `python3` without -I; no `timeout`.
  - Load 3.50 at start and 4.24 at end (< 8); 37% of memory free.
  - Output: scratchpad `rerun_x9/`.
  - **Result:** `x8_out.txt` is **identical** except the β = 32 per-β time (89 s vs 88 s) and the total wall/peak line.
    Every number agrees digit for digit (fixed seeds), including:
    - A1 0.750000000000;
    - A2 min slack 1.419e-05;
    - A3 0 violations (40 + 150 configurations);
    - A4 4.444444 and 0.458692;
    - X(1) = 1.3459 ± 0.0238, 1.8006 ± 0.0432, 2.1674 ± 0.0502;
    - "B0 PASS; B1 PASS".
  - 312 s wall, 584 MB peak.

---

## (7) §12.1 public statement (priority 7): NO CHANGE REQUIRED; word-for-word verdict

- **§12.1 is byte-identical to session 8.** md5 of the subsection agrees, and session 9 did not touch it. Correct
  conduct.
- **Is it still true? YES.** It lists "a Hilbert space of dimension greater than one" among the items "not established".
  - Session 9's result is conditional, at a fixed small spatial torus, through wrapping observables.
  - Its X-OS form also uses (K9-req), which layer 1 has not adopted.
  - The unconditional and infinite-volume content of the sentence is unchanged, and the statement makes no fixed-torus
    claim anywhere.
- **Optional clause (do not adopt before an independent review of §18 and layer 1's answer on (K9-req)).** If one is
  wanted, insert after "…the local bound is derived from the extensive one by chessboard estimates." the sentence:
  > Under the same soft-branch hypotheses, together with an anisotropic-torus form of the counterterm statement that our
  > sister lane has not adopted, the soft Hilbert space on a fixed spatial torus of side small compared with the
  > confinement length has dimension greater than one, through spatial Polyakov loops; this is a finite-volume effect of
  > the holonomy zero modes and says nothing about local observables or infinite volume.
  - Then change "a Hilbert space of dimension greater than one" in the "not established" list to "a Hilbert space of
    dimension greater than one for local observables or in infinite volume".
  - **Recommendation:** leave §12.1 as is. The clause adds a weak, easily over-read result to a public text. The present
    text is not falsified by it.

---

## (8) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| RX8 fixes 1-12 | CONFIRMED (residual "K-free" at the l.3044 title and the l.2515 table, cosmetic) |
| Lemma CTR | CORRECT (S4' crossing count, kernel, 𝒩_i, Haar, action); state the floor-type block convention and "levels ≤ j, proper blocks" |
| POL-det (i) SU(2) | CORRECT (re-derived; commutator = 2s exactly) |
| POL-det (ii) SU(N) | CORRECT (compactness; free Z_N³ action; non-explicit) |
| POL-det (iii) Stokes | CORRECT |
| NT-pol^abs | CORRECT; a genuine OS (cross-plane) inner product; "Re" for SU(N) |
| Lemma SMALL | CORRECT; tag the torus "no outer layer" reading of (a3-q); N_c count cosmetic |
| Theorem NT-pol | CORRECT (conditional); T25 DECIDED; no moduli density, no two-point input |
| Corollary NT-pol^OS | CORRECT; sup_K g^S_{m_*} in the condition |
| Re-scoping to (H-sig^S_loc) | ACCEPTABLE (literal entry not fully discharged: spatial side → ∞) |
| Caveat | ADEQUATE everywhere; "must be exponentially small" → sufficient condition; ASSEMBLY: add the mechanism |
| §18.6 twisted | plausible, ARGUED as labelled |
| Proposition SP | CORRECT and important; example needs each ω_i RP, θ- and τ-invariant |
| (WC_∞), (WC_∞^sp) | WRONG as quantified (g-uniform c_∞, c_sp; expected false, inconsistent with (WC)); iterated-only limit points |
| (WC_∞^sp) ⇒ (WC_∞) | conclusion CORRECT; RP plane misnamed |
| "Mass gap not needed" | CORRECT |
| "none of the three implied by the others" | unproven; delete or ARGUED |
| x8 | honest; code correct as read; re-run identical (see (6)) |
| §12.1 | unchanged; still true; no update required |

**Tally.**
- **Claimed:** PROVEN-HERE 52 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 12;
  ARGUED 28.
- **Corrected: 52 / 1 / 3 / 5 / 12; ARGUED 29** (+1: the independence claim at l.3628-3629, if kept; 28 if it is deleted).
  - NT-pol (bundle) and SMALL stay counted. Both are complete proofs from named hypotheses.
  - Proposition SP is correctly uncounted, and so are the implications (WC_∞^sp) ⇒ (WC_∞) ⇒ dim H > 1.
  - (WC_∞)/(WC_∞^sp) are named parts of OPEN (H-sig^S_loc). Re-quantifying them changes no count.
  - HYPOTHESIS-NEW unchanged: CLS-cone, (a3-q) and (K9-req) are layer-1 items.

---

## Binding fixes for session 10

1. **(WC_∞), (WC_∞^sp) quantifiers (l.3614-3619, l.3659-3661, §0 l.151, LOG finding 6).** Replace the g-uniform c_∞, c_sp.
   Either use one coupling ("there are m_*, F, g > 0 and c_∞(g) > 0 …; one g suffices, since g only fixes the unit length
   relative to Λ") or keep ∀g ≤ g_∞ with bound c_∞u_+^{-2} (≍ g⁴), matching (WC) and (FS). State the minimal IR statement
   in the one-g form.
2. **Limit points (l.3590, l.3620-3621).** "(WC_∞) ⇒ dim H > 1 for every **iterated** limit point; for joint limits use
   liminf over (K, T_0, T) with K ≥ K_0(T_0, T)."
3. **RP plane (l.3622).** C_F(s_1) = ⟨θ(G), G⟩_conn ≥ 0 with G := τ_{s_1/2}F, RP in Π_0.
4. **Independence claim (l.3628-3629).** Delete "none of the three is implied by the others", or label it ARGUED (then
   ARGUED 29). For "gap + uniqueness + (WC_∞) ⇒ (WC_∞^sp)" in the box-uniform form, add "with the gap uniform over limit
   points".
5. **Caveat wording (l.3528-3529; §0 l.146).** "must be exponentially small" → "the theorem's sufficient condition
   requires … (an artefact of e^{2E_0N_c}); intrinsically the box must be ≪ the confinement length". ASSEMBLY l.2496: add
   "(carried by the holonomy/electric-flux zero-mode sector)".
6. **Corollary NT-pol^OS (l.3540-3541).** State the coupling condition with g_+ := sup_{K ≥ K_0}g^S_{m_*}(K) (bracketed by
   (F)).
7. **Lemma CTR (l.3410, l.3421-3422).** Cite the floor-type (unshifted) block convention shared with Π_0, and "levels ≤ j,
   where every block is a proper sub-box (n_s ≥ 3)".
8. **Lemma SMALL (l.3497-3500).** Tag "on the torus every chain term lies in a full cone" as "[reading of HIST §25.5; to be
   confirmed by layer 1]" and add it to the layer-1 report with (SF-bg^tor). Cosmetic: 8u^{-1/2} → 4u^{-1/2} (or keep it,
   noting that it is conservative); clarify which cubes N_c counts (l.3528).
9. **Proposition SP (iii) (l.3608).** "two distinct reflection-positive, θ- and τ-invariant states".
10. **Cosmetic.** l.3044 title and l.2515 "K-free" → "depth-uniform"; NT-pol^abs SU(N) "Re" (l.3480); β_1 at l.3530.

---

## Strategic verdict

- **What session 9 established (correctly).**
  - A complete, conditional, K-uniform fixed-torus non-triviality theorem: Cov ≥ 3/8 for SU(2), and the SU(N) family
    version. Its inputs are an exact symmetry (CTR), an algebraic lemma (POL-det) and one-point smallness (SMALL).
  - It uses no moduli density and no two-point input. It is better than either route REVIEW_X8 sketched.
  - The X-OS version at a fixed spatial torus is consistent with x8 and with the expected electric-flux physics.
- **What it is worth.** Exactly what the lane says: a small-box, zero-mode statement. It settles the fixed-torus
  milestone question that REVIEW_X8 posed, cheaply. Further fixed-torus work should stop here, as LOG Next already says.
  - The (WC-tor)/(WC-tw) Laplace programme for local observables on a fixed torus would add a perturbative small-box fact.
    It would not bear on (WC_∞).
- **Proposition SP changes the target.** The meaningful infrared statement is the spectral one, (WC_∞^sp): a box-uniform
  lower bound on the drop C_F(0) - C_F(s_1) for a local F.
  - As written it is mis-quantified (binding fix 1). Fixed, it is the right minimal IR target. It is not a mass gap, and
    as §18.7 argues, it is plausibly not reachable by fixed-volume weak-coupling methods without control up to the
    confinement scale.
- **Recommendation, in order.**
  1. Apply binding fixes 1-4 (they define the lane's top open target).
  2. Report the two layer-1 readings, (SF-bg^tor) and the torus term set of (a3-q), together with K8/K9.
  3. Next work, if any, on (WC_∞^sp) or (WC^bg)'s θ-invariant-σ-algebra obstacle. Not further fixed-torus theorems.
  4. Leave §12.1 unchanged until §18 and (K9-req) are independently settled.
