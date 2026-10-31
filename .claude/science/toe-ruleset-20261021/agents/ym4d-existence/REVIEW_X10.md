# REVIEW_X10: independent hostile review of session 10 of the YM4D existence lane (§19 and the [RX9-fix] changes)

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session10_snapshot.md (`cmp` empty).
  - `diff session9 session10` read in full (the fix hunks and all of §19).
  - §18.7 (l.3623-3716) and §19 (l.3774-4041) read in full by offset.
  - §17 Conventions and (O1)-(O3) (l.2978-3061), and Theorem CB with (RLF-3^dis) (l.1645-1668), re-read.
- LOG.md session 10 (l.597-659) and REVIEW_X9.md (all).
- checks: x9_criteria.md, x9_drop.py (read line by line), x9_out.txt, x9_time.txt.
- Read-only layer 1:
  - ../ym4d-proof/PROOF.md session-19/20 headers (l.21-62): RW, N5-sf0, NAH1, NAH-ind;
  - ../ym4d-proof/SF.md (CE-s) (l.190-213, l.442-475, l.528) and Theorem CE-exp / Corollary CE-exp^0 (l.618-640).
- No web access. Literature remarks are the reviewer's own knowledge, marked [reviewer knowledge], and are not load-bearing.

Line numbers are EXISTENCE.md lines unless marked. No file other than this one was edited.

**Bottom line.**
- **RX9 fixes 1-10 are applied, with one overclaim.** The re-quantification calls the family form (c = c'g⁴ for all g ≤ g_∞)
  "equivalent" to the one-g form (l.3656, l.3661). It is strictly stronger.
- **Lemma DIFF: CORRECT**, with one scope restriction.
  - The second difference is the finite-volume RP norm of D_h = F - τ_hF.
  - At limit points with T_0 → ∞ it equals ||(1 - e^{-hH})([F] - ω(F)Ω)||², which vanishes on ker H, so it is blind to
    vacuum degeneracy.
  - At a fixed finite torus, [τ_aG] = e^{-aH}[G] is false: the torus OS vectors live in H⊗H*, the thermal picture. So (ii)'s
    words "finite or infinite volume" must be narrowed.
- **Lemma LO-D: CORRECT at depth 0.**
  - x9 re-run is byte-identical: A(1,1) = 2.250e-3 = 94.9% of C(1), and box convergence holds at 8e-6.
- **§19.3 (the lead's step is not an estimate): CORRECT.** One rate claim (l.3867-3868) is unproven.
- **Theorem SPEC-red: CORRECT as an implication.**
  - Every inequality was re-derived; the constants close at a/2.
  - The absolute-value bound on the coarse-mediated term is valid and removes (WC^bg)'s obstacle.
  - It does reach joint limit points, through Lemma DIFF (iv) with K_0 independent of T.
  - **Four binding precision defects:**
    1. the quantifier order of g, n and g_c;
    2. j' ≤ K, i.e. m_* ≥ n, is unstated;
    3. "possible for R ≥ R_0" needs a decay rate for e(R);
    4. the conditions depend on K through a = g_j⁴A_*.
- **(CE-cond): genuinely UV-type in scale content (ARGUED, agreed).** It is not within reach of layer 1 as layer 1 stands.
  - The most serious failure point is (ii)+(iii) together: background-uniform control over n ≍ log(1/g) steps.
  - Layer 1's only multi-level background result (NAH-ind) loses ≈ 10⁻⁴⁰ per level. At n ≍ log(1/g) that pushes the
    controlled background domain far below the typical field size g, so (CE-cond) and (LF-loc) cannot both hold on the
    current constants.
  - A failure point that is not named: the conditional large-field control. Theorem CB, the lane's only bridge from
    extensive to local bounds, needs RP, and conditioning on U_{j'} destroys RP.
- **"What it gives": the free-gluon remark is CORRECT**, but "not the trivial theory" is a misleading phrase.
  - In constructive QFT, "trivial" means Gaussian. The result is consistent with a Gaussian (free) limit.
  - LOG's "connected four-point bound" as the non-Gaussianity test is wrong as worded: composite cumulants of Φ are
    non-zero for free fields.
- **x9: honest.**
  - The re-run under the lock is byte-identical.
  - The B exponent miss is confirmed to be a coarse-Riemann-sum artefact (reviewer check: -4.91, -4.40, -4.19 at T = 64,
    128, 256).
- **Tally.**
  - Claimed: 53 / 1 / 3 / 6 / 12, ARGUED 31.
  - **Corrected: 53 / 1 / 3 / 6 / 12, ARGUED 32** (+1 for the §19.3 item-1 rate, if it is kept).

---

## (1) RX9 fixes (priority 1)

| Fix | Where (session-10 lines) | Verdict |
|---|---|---|
| 1 (WC_∞)/(WC_∞^sp) re-quantified | l.3653-3666, l.3714-3715, §0 l.157-158, l.3688 | **CONFIRMED with one overclaim.** One g with c_∞(g), c_sp(g) > 0: correct, and it removes the anti-AF g-uniform constant. **But** l.3656 ("equivalently bounds ∝ g⁴") and l.3661-3662 ("Equivalent family form"): the family form ⇒ the one-g form trivially. The converse needs (a) uniqueness of the tuned limit up to scale (the text's own "if"), and (b) that the best constant scales exactly like u_+^{-2} at fixed m_*. Fix: "**stronger** family form (implies the one-g form)". The natural family normalisation at fixed resolution m_* is c'u_+^{-2} (u_+ = g^{-2} + β_+m_*log L + R), not c'g⁴; the two are ≍ only at fixed m_* (the text writes ≍; acceptable) |
| 2 iterated vs joint | l.3626-3628, l.3667-3668, l.3670-3671 | CONFIRMED. Precision: a bound for K ≥ K_0(T_0, T) covers only joint sequences with K_n ≥ K_0(T_{0,n}, T_n), not every joint limit point. Write "joint limit points along sequences with K_n ≥ K_0(·)". §19's Lemma DIFF (iv) (K_0 independent of T) covers all of them, correctly |
| 3 RP plane | l.3672-3674 | CONFIRMED (θ(τ_{s/2}F) = τ_{-s/2}θF; translation invariance; s_1/2 a block multiple) |
| 4 independence claim deleted; uniform gap | l.3680-3683 | CONFIRMED |
| 5 caveat wording; ASSEMBLY mechanism | l.153-154, l.2514-2515, l.3555-3564, l.3744-3745 | CONFIRMED |
| 6 g_+ := sup_K g^S_{m_*} | l.3574-3577 | CONFIRMED. Monotonicity re-checked: d/dx[x(log 1/x)^{p_*}] > 0 for log(1/x) > p_* |
| 7 floor-type convention; proper blocks | l.3429-3432, l.3444-3445 | CONFIRMED |
| 8 torus term set tag; 4u^{-1/2}; N_c = n_s⁴ | l.3523-3525, l.3534-3535, l.3555-3557; §19.8 item 2 | CONFIRMED |
| 9 SP (iii) states RP, θ- and τ-invariant | l.3646-3647 | CONFIRMED |
| 10 "K-free" → "depth-uniform"; "Re"; e^{u/(2β_0)} | l.3063, l.2534, l.3504-3505, l.3562-3563 | CONFIRMED. Cosmetic: REVIEW_X9 called β_1 a two-loop name, but the lane defines β_1 := 11N²/(12π²) as its one-loop rate (l.2805, PLD normalisation, the rate for the Wilson β = 2N/g²). e^{u/(2β_0)} is right for u = 1/g² (l.2979). Define β_0 numerically (11N/(48π²)) at l.3563 |

Tally after the fixes alone: 52 / 1 / 3 / 5 / 12, ARGUED 28. **Agreed.**

---

## (2) Lemma DIFF (l.3810-3835): CORRECT, one scope restriction (binding)

**(i), re-derived.**
- With θτ_h = τ_{-h}θ and τ-invariance:
  Cov(θD^*, D) = C(0) - C(h) - Cov(τ_{-h}θF^*, F) + Cov(τ_{-h}θF^*, τ_hF) = C(0) - 2C(h) + C(2h).
- The reality argument (θ-invariance, then τ) is correct. F = Φ(P) is real anyway.
- E D_h = 0. The sign is ≥ 0 by X-RP^S in Π_0, since D_h ∈ 𝔄^S_+ (τ_hF moves away from Π_0; T/2 > t + 2h is needed, and it
  holds for T ≥ T_1).
- **Is it an OS norm at every finite volume? YES, as the finite-volume RP norm ||[D_h]||²_{K,T}.**

**(ii) is ||(1 - e^{-hH})([F] - ω(F)Ω)||² only at limit points with T_0 → ∞.**
- On a finite periodic torus with transfer matrix 𝕋 (eigenvalues e^{-E_n}), write τ = T_0 - (d + a). Then
  E[θF^*τ_aF] = Z^{-1}Σ_{m,n}e^{-τE_m}e^{-(d+a)E_n}|⟨m|F|n⟩|².
- This is a positive combination of e^{-a(E_n - E_m)}, including growing exponentials. The OS vectors live in H⊗H*, and τ_a
  is not e^{-aH}.
- So (ii)'s "every limit point ω (finite or infinite volume)" (l.3815) is wrong for a K → ∞ limit at a **fixed** hypercubic
  torus.
- (Under §19's hypercubic convention a "finite-volume" limit point is exactly that. In §18.7's (I)_fix, T_0 → ∞ and (ii) is
  fine.)
- Fix: "(ii) at every limit point with T_0 → ∞ (X-OS limits: fixed or infinite spatial volume)".
- The conclusion used later (iv) concerns T → ∞ hypercubic limits, so **nothing downstream changes**.
- Remark: the finite-T_0 sum is still blind to Δ = E_n - E_m = 0 terms, because (1 - e^{-hΔ})² = 0 there.

**Does it vanish on the vacuum-degenerate subspace? YES.** (1 - e^{-hH}) annihilates ker H, so the degenerate vacuum of SP
(iii) gives exactly 0.

**(iii)** (1 - e^{-x})² ≤ 1 - e^{-x} ≤ 1_{x>0}, and (1 - y)² ≤ 1 - y² on [0, 1]. Correct.

**(iv) CORRECT.**
- The bound holds on the whole index set {K ≥ K_0, T ≥ T_1}, with K_0 independent of T. So every sequence, iterated or joint,
  eventually lies in it.
- θ(D)^*D is a bounded local function, so the bound passes to every weak-* limit.
- The limit is translation-invariant and RP, so (ii) applies. Then σ_F((0, ∞)) ≥ c, and liminf C_F(0) ≥ c.
- **A uniform lower bound on the second difference gives (WC_∞^sp) and (WC_∞), for joint limits too: confirmed.**

**Weight.** Elementary, but it is the right observation: it turns "C_F not constant" into a sign-definite, vacuum-blind,
finite-volume target (WC_∞^Δ).

---

## (3) Lemma LO-D (l.3837-3859): CORRECT at depth 0

- **Wick.** Cov(Y_a², Y_b²) = 2δ_{ab}(g²c)², so Cov_Gauss(θΦ, τ_aΦ) = 2c_N²(N² - 1)g⁴c(d + a)². Correct. The O(Y⁴) terms enter
  at O(g⁶).
- **Positivity.**
  - c(d + a)² = ∫∫e^{-a(λ+μ)}dρdρ, so the combination is ∫∫(1 - e^{-h(λ+μ)})² ≥ 0. Correct (it is Lemma DIFF for the
    Gaussian measure).
  - Equality iff ρ = ρ({0})δ_0.
  - c(d) > 0: e^{-tH} is injective and c(1) > 0. c → 0 by Riemann-Lebesgue (the integrand (k̂_1² + k̂_2²)/k̂² is bounded, so
    it is L¹).
  - So ρ({0}) = 0 and ρ ≠ 0: strict. Correct.
- **x9 A: the code is correct as read.**
  - G_T(d) = T^{-4}Σ_{k≠0}cos(k_0d)(k̂_1² + k̂_2²)/k̂² is the gauge-invariant curvature correlator (|F̂_12|² in Feynman gauge).
  - A = ½[G(d)² - 2G(d + h)² + G(d + 2h)²] for Φ = ½F_12².
  - The A3 dense curl^Tcurl pseudo-inverse is an independent check. G(0) = 0.498 → ½ (= 2/4 by symmetry).
  - **A(1,1) = 2.250036e-3, C(1) = ½G(1)² = 2.3719e-3, ratio 0.9486** (checked by hand from G_48(1) = 6.887465e-2).
  - **Box convergence:** A(1,1) changes by 2e-4 relative from T = 16 to 48. A2's 8.3e-6 (d = 1) and 2.1e-4 (d = 3) are
    reproduced. A(5,·) moves about 2% from T = 16 to 48: still converging, and not listed in A2.
- **Reading (cosmetic).** "Almost all of the order-g⁴ correlation is non-vacuum" (l.3982-3983) understates it.
  - In the infinite-volume Gaussian model σ_F({0}) = 0 exactly: all of it is non-vacuum.
  - The 95% is the factor (1 - e^{-hλ})² < 1, not a vacuum fraction.
  - "Finite-energy" means λ = O(1) in level-j units: energies at F's own (fixed physical) resolution scale, not glueball
    scale.
- **Depth k ≥ 1 and depth-uniform A_*: ARGUED, as labelled.** The theorem never uses A_*'s identification, only its
  positivity as a constant in (CE-cond). So LO-D is interpretation, not an input, for SPEC-red. Counting it inside the SPEC-red
  bundle is harmless but logically loose (cosmetic).

---

## (4) §19.3, "local, hence volume-uniform" is not an estimate (l.3861-3880): CORRECT

- **Item 1.** (O2) lives on the global event 𝒮_j. NT-LF pays 6p||F||² with p ≥ P(𝒮_j^c), and (O3)'s bound C|Λ_j|e^{-a/g²} is
  extensive. So nothing volume-uniform comes from them. Correct.
  - **The rate claim "P(𝒮_j) ≤ (1 - p_0)^{N/c}" is unproven.** A per-cube lower bound p_0 gives an exponential rate only
    under independence or mixing.
  - "→ 0" holds, for instance, by the ergodic theorem in any limit whose bad-cube density is a.s. ≥ p_0. It is not needed
    anyway: the argument needs only that layer 1's bound is extensive.
  - Fix: replace the rate by "layer 1's bound on P(𝒮_j^c) is extensive (and P(𝒮_j) → 0 in any limit with a positive density of
    bad cubes)", or label it ARGUED (+1).
- **Item 2.** On 𝒮_j the level-j law is a massless lattice gauge theory in the whole volume. Its Gaussian reference has power-law
  covariance, so there is no cluster expansion for the full measure. Correct.
- **Item 3.** The spectral weighting says where the weight sits given σ_F. It is not a bound on the measure. Correct.
- **Verdict: the finding is correct.** The lead's step is physically sound (short-distance OPE/AF intuition) [reviewer
  knowledge] but is not an estimate.
  - The correct localising tools are conditioning, as SPEC-red does, or a finite-range decomposition of the Gaussian part
    (Brydges-Guadagni-Mitter type) [reviewer knowledge].

---

## (5) Theorem SPEC-red (l.3882-3936): CORRECT as an implication; four binding precision defects

**Re-derivation.**
- **Total covariance:** Cov(X, Y) = E[Cov(X, Y | 𝔅)] + Cov(E[X|𝔅], E[Y|𝔅]). Regular conditional laws exist on compact
  metric spaces.
  - G_R ∈ 𝔅 (it is defined from U_{j'}).
  - D is real, so every conditional covariance is real; (a) needs no "Re".
- **First term.**
  - |Cov(·|𝔅)| ≤ ||θD||_∞||D||_∞ ≤ 4M² off G_R.
  - On G_R it is ≥ (1 - r)a - e (≥ 0 once e ≤ a/16).
  - (1 - δ)((1 - r)a - e) ≥ (3/4)a - δa - e. Correct.
- **Second term.**
  - 𝔅 = σ(U_{j'}) is θ-stable: Π_0 is a block boundary at every level, by the floor convention of [RX9-fix 7].
  - The joint law of (U_j, U_{j'}) is θ-invariant, by the kernels' reflection covariance (Lemma NT-0's proof).
  - Hence E[θD | 𝔅] = E[D | 𝔅]∘θ̂ and Var is preserved. Cauchy-Schwarz gives ≥ -Var(E[D|𝔅]).
  - Var ≤ E|f - m|² for any constant m. f is real, so the midpoint is well defined. On G_R, |f - m| ≤ (ω_b + e)/2; off it,
    |f - m| ≤ 4M.
  - Correct.
- **Sum:** (3/4)a - e - (ω_b + e)²/4 - δ_R(a + 20M²) ≥ a(12 - 1 - 1 - 2)/16 = a/2. Correct.
- **g_j⁴ ≥ u_+^{-2}:** from (O1), u_j ≤ u_+. Correct.

**The coarse-mediated term needs no sign: CORRECT and the key idea.**
- It is bounded in absolute value by Var(E[D|𝔅]). That needs θ-covariance (which holds), not θ-invariance (which fails).
- (WC^bg)'s named obstacle is genuinely removed, and the price is moved into (CE-cond)(b).

**Is the conclusion about infinite-volume limit points, joint included? YES, given (CE-cond) as written.**
- K_0 is independent of T, and T_1(R) is independent of K. So Lemma DIFF (iv) applies on the whole index set.
- Restricted to hypercubic tori, as stated.

**Binding precision defects.**
1. **Quantifier order of g, n and g_c (l.3893-3896 against l.3950-3951, §19.5 (iii)).**
   - (CE-cond) is stated "for the given F, h, n": g_c, A_*, r, ω_b and e(·) come after n.
   - But §19.5 chooses n from g (n ≍ log(1/g)). With g ≤ g_c(n) and n = n(g), the requirement is circular unless the constants
     are uniform in n.
   - Since one g suffices, state it at **one pair**: "for the chosen g there is n = n(g) such that (a), (b) hold at (g, n) with
     constants obeying the three compatibility inequalities". Otherwise state uniformity in n ≤ n_max(g) explicitly.
2. **j' ≤ K, i.e. m_* ≥ n, is unstated (l.3884-3885).**
   - Levels count from the bare lattice (k = 0) to the unit lattice (k = K) (l.2978). The chain (U_0, …, U_K) has no level
     beyond K.
   - j' = K - m_* + n therefore requires n ≤ m_*. So F's resolution must satisfy m_* ≥ n ≍ log(1/g)/(2 log L).
   - Then g_{j'} ≤ g_c follows from (O1): u_{j'} ≥ g^{-2} + β_-(m_* - n)log L - R. §19.5's "u_{j'} ≥ g^{-2} - O(log 1/g)"
     (l.3951) should be replaced by that.
   - It also confirms "scale ≪ Λ^{-1}": ℓ_{j'} ≤ the unit lattice.
3. **"possible for R ≥ R_0 and g small" (l.3904) needs a rate for e(R).**
   - The conditions e(R) ≤ a/16 ≍ g⁴ and |N_R|C_dg^{-p_d}e^{-a_d/g²}·20M² ≤ a/8 are compatible only if e reaches g⁴ at an
     R_0(g) with |N_{R_0}| ≪ e^{a_d/g²}g^{4+p_d}.
   - That fails for slowly decaying e (e.g. e(R) = 1/log log R).
   - Fix: put a rate in (CE-cond) (e(R) ≤ C_eR^{-α}, or C_ee^{-m_eR}), or state the compatibility as a hypothesis.
4. **K-dependence of a := g_j⁴A_* (l.3902-3904), and a notation clash.**
   - The three conditions must hold for every K ≥ K_0, but a varies with K through g_j. State them with
     a_- := u_+^{-2}A_* (for e and ω_b) and a_+ := u_-^{-2}A_* (in δ_R(a + 20M²)).
   - Rename Theorem CB's exponent constant a (in δ_R, l.3890) to a_d. It clashes with a = g_j⁴A_*.

**Cosmetic.**
- The header (l.3882) lists "| Lemma DIFF, (LF-loc), (CE-cond)". It also consumes (O1), the joint θ-covariance of the chain,
  and X-RP^S. They are named under "Consumed" (l.3931-3936); add them to the header.

---

## (6) (CE-cond) and §19.5 (priority 6)

**Precisely stated?** Not yet: defects 1-4 above. Apart from those, (a) and (b) are well-posed. P_K-a.e. V with an essential
sup in (b) is fine.

**Genuinely UV-type? YES, in scale content (ARGUED; agreed).**
- By the Markov property, the conditional law of U_j given U_{j'} involves only S_j (all finer levels) and the kernels K_j…K_{j'-1}.
- No level coarser than j' enters, and every coupling involved is ≤ g_{j'} ≤ g_c.
- The IR (scales ≫ the unit lattice, where the coupling is O(1)) enters only through which V occur. That is handled by
  (LF-loc) and the sup over V.
- (CE-cond)(a) is a lower bound on a two-point function of a **massive, background-pinned** conditional measure, not of the
  full measure. So it is not "(WC_∞) restated". T28's exclusion is respected.

**The three named failure points, and which is the most serious.**
- **(ii)+(iii) together are the most serious.** They ask for background-uniform control of the n-step conditional
  fluctuation problem with n ≍ log(1/g).
  - Layer 1 has (NA-H_loc) only at level 1 (Theorem NAH1). Levels ≥ 2 rest on Proposition NAH-ind, and there "the proven
    background threshold shrinks by ≈ 10⁻⁴⁰ per level" (P/PROOF l.38). Uniformity needs (BG-unif), which is OPEN.
  - With n ≍ log(1/g)/(2 log L), the controlled background domain is ≲ ε_*·10^{-40n} ≈ ε_*·g^{42} for L = 3. That is far
    below the typical coarse-field size ≍ g.
  - So the small-field event G_R that (CE-cond) needs, and the one on which (LF-loc) gives a small complement, cannot both be
    used on the current constants. P/PROOF [R20-fix 8] says this loss is not shown to be intrinsic, so this is not a no-go.
    It is the binding obstruction.
- **(i) e(R) decoupling.** It is a standard Balaban-type localisation through a massive small-field collar [reviewer
  knowledge]. Plausible, and it needs a rate (defect 3).
- **Unnamed failure point (add as (iv)): conditional large-field control near supp D.**
  - Conditionally on V ∈ G_R, the fine levels j…j'-1 near F must be small-field with conditional probability close to 1.
  - §19.5 cites "coercivity (CLS-cone ⇐ (AE))". But the lane's only extensive-to-local bridge is Theorem CB (§13.5: "a local
    probability bound cannot follow from extensive bounds alone in general"), and CB needs RP of the measure.
  - The conditional law given U_{j'} is not RP: V is not θ-invariant. So CB cannot be reused inside (CE-cond).
  - A direct local Peierls argument for the conditional problem is needed. Layer 1's cut complement (SF.md l.204-205,
    "priced separately" through (SG^fl)) is extensive.
- **Recommended reformulation (reviewer; ARGUED, uncounted). It attacks (iii) directly.** n ≍ log(1/g) comes only from
  bounding (b) by a **sup** over backgrounds of size ε_1 (fixed), so that ω_b ≍ ε_1²L^{-4n}.
  - Only Var(E[D|𝔅]) is used (l.3918-3920). With typical coarse curvature ≍ g, the mean-square oscillation is
    ≍ g⁴L^{-8n}, against a ≍ g⁴A_*. So L^{8n} ≫ 1/A_* suffices, i.e. **n = O(1)**: n = 1 at L = 3 already gives 6561 against
    1/A_* ≈ 450 for one colour.
  - x9 B supports this: the sharp-cutoff coarse-mediated part of the second difference is 2e-6 of A(1,1) already at ℓ = 4.
  - The cost is a volume-uniform small-field tail at a g-scaled threshold τ = g·p(g), P_K(||1 - V_p|| ≥ τ) ≤ g^{4+}. That is
    the Balaban threshold choice, and through Theorem CB it is (RLF-3^dis) at threshold τ.
  - H-Bal-3T^S's ≤ g² is not enough. This trade would pay NAH-ind's per-level loss O(1) times instead of log(1/g) times.
- **Could layer 1 deliver (CE-cond)? Not as it stands. The closest pieces:**
  - SF.md Theorem CE-exp + Corollary CE-exp^0: a cluster expansion of one fluctuation integral at a fixed small-field
    background with background-local activities. That is CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮), at stage 0 only. (CE-s) itself
    is ARGUED, not written.
  - N5-sf0: the level-0 fluctuation operator at curvature-small backgrounds (gap, decay, holomorphy, background-local walk
    terms). An existence theorem.
  - RW: all levels at the trivial background.
  - NAH1: level 1.
  - **Missing:**
    1. an observable source in CE-exp (a routine extension [reviewer knowledge]);
    2. the stage-k (level j = K - m_*, K → ∞) versions ((OP-loc)_k, SF V4);
    3. the n-step prescribed-endpoint composition ((BG-unif) for n > 1);
    4. a conditional local large-field bound (above).
  - With n = O(1) per the reformulation, items 1 and 4 plus stage-k versions of CE-exp/N5 would suffice. Send it to layer 1
    in that form (§19.8 item 5).
- **Revision of the T24 attribution (l.3964-3967): justified as ARGUED.**
  - Spectral non-triviality in the sense σ_F((0, ∞)) > 0 is UV-type, given (CE-cond).
  - It must be read with (7): it is the UV statement that AF theories look free at short distance. It says nothing about
    infrared structure, and the gap stays infrared.

---

## (7) "What it gives" (T30, l.4010-4015; §0 l.169-171; LOG finding 6)

- **Not vacuum-degeneracy-only: CORRECT** (Lemma DIFF (ii)).
- **Weight at finite energies: CORRECT.** σ_F is a finite measure. "Finite" means at F's resolution scale in physical units,
  since K → ∞ is taken first.
- **Free-gluon remark: CORRECT.**
  - For N² - 1 free (abelianised) gluons at coupling g_j, Cov(θD, D) = g_j⁴A_D **exactly**, which meets ≥ g_j⁴A_*/2 whenever
    A_* ≤ A_D.
  - The bound is the free value and cannot certify interaction.
- **"Not the trivial theory" is misleading (binding wording).**
  - In constructive QFT, "trivial" means Gaussian (as in φ⁴_4 triviality) [reviewer knowledge]. The SPEC-red conclusion is
    **consistent with a Gaussian (generalized-free) limit**.
  - Write "not the vacuum-only (dim H = 1) theory", and add "Gaussianity of the limit is not excluded" at l.4010, §0 l.170 and
    LOG finding 6.
- **What would distinguish the interacting theory.**
  - LOG Next's "a connected four-point bound" is wrong as worded. Φ is quadratic in the curvature, so the connected three- and
    four-point cumulants of Φ are non-zero for free fields too. A lower bound on them certifies nothing.
  - Candidates that do distinguish (reviewer, ARGUED):
    - (a) a cumulant that vanishes for **every** centred Gaussian gauge field, e.g. an odd-order connected curvature cumulant
      carrying f^{abc}, such as the C- and P-even cubic invariant tr(Y_12[Y_23, Y_31]) at a site or at separated points with
      gauge-invariant transports. It is zero by Wick parity in the abelianised theory and O(g⁴) through the three-gluon vertex
      in YM;
    - (b) the running: a **two-sided** O(g⁶) statement that g_j^{-4}·Cov at fixed physical separation changes with depth by
      the factor (u_j/u_{j+1})², of sign fixed by β_0 > 0. A free theory at fixed coupling has none.
  - Both go through the same conditional route. (a) needs only a lower bound on |·| of a quantity whose Gaussian value is 0,
    so it fits SPEC-red's architecture best.

---

## (8) Check x9 and the re-run (priority 8)

**Pre-registration order (mtimes, UTC).**
- §19.0 03:44 < criteria 03:45:30 < script 03:46:05 < out/time 03:52:30. Consistent.
- Cosmetic: l.3802 says the derivations were written "after checks/x9_criteria.md", but LOG l.608-610 dates them 03:45-03:50 and
  the criteria "~03:46" (the file says 03:45:30). Harmonise the times.

**Code, read line by line.** Correct (see (3)).
- B: low and high Fourier modes are independent for the Gaussian, and E Cov(Φ|𝔅) = ½G_h² + G_lG_h with
  Cov(E[Φ|𝔅]) = ½G_l². Correct.
- **The "identity error" is an algebraic tautology** (½(G_l + G_h)² expanded), not a test. Say so at l.3987.

**B honesty.** The exponent miss (-4.91 against [-4.5, -3.5]) is recorded as "not consistent", as registered, with the cause
labelled untested. Honest.
- **Reviewer check (under the lock): the cause is confirmed.**
  - The continuum V_l ∝ ℓ^{-4} is exact: the integrand is homogeneous of degree 0 over a cube of side 2π/ℓ.
  - Fitted exponent between ℓ = 8 and 16 at T = 64, 128, 256: **-4.907, -4.399, -4.189** (low modes per direction 7/3, 15/7,
    31/15). It converges to -4.
  - Script: scratchpad `rerun_x10/vl_check.py`. The T = 64 values reproduce x9's 7.1526e-05 and 2.3842e-06.

**Re-run of x9 (reviewer, under the mandatory lock).**
- Lock acquired 04:01:18 UTC, with no wait. `rmdir` once at 04:01:19, no trap.
- nice 10; OMP/OpenBLAS/MKL/vecLib threads 1; `python3` without -I; no `timeout`. Load 3.34 (< 8); 44% memory free.
- **Output is byte-identical to checks/x9_out.txt** (`diff` empty, including the wall/RSS line: 0.2 s, 129 MB).
- The V_l check ran under a separate acquisition: 04:04:14-04:04:15, rmdir once, load 3.37.
- Output: scratchpad `rerun_x10/x9_out_rerun.txt`.

**Load-bearing:** the A values only, as stated. Positivity is analytic.

---

## (9) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| RX9 fixes 1-10 | CONFIRMED; fix 1 "equivalent family form" overclaims (stronger, not equivalent); fix 2 joint-form scope precision |
| Lemma DIFF (i), (iii), (iv) | CORRECT; OS (RP) norm at every finite volume; joint limits covered |
| Lemma DIFF (ii) | CORRECT for T_0 → ∞ limit points; **wrong at a fixed finite torus** (thermal OS space); narrow the words |
| Lemma LO-D | CORRECT at depth 0; x9 values reproduced; depth-uniform A_* ARGUED; not logically used by SPEC-red |
| §19.3 | CORRECT; the (1 - p_0)^{N/c} rate unproven (reword or ARGUED +1) |
| Theorem SPEC-red | CORRECT as an implication (re-derived to a/2); joint limits reached; binding defects 1-4 (n/g quantifiers, m_* ≥ n, rate of e(R), K-uniform conditions + a-clash) |
| (CE-cond) | UV-type in scale content (ARGUED, agreed); not deliverable by layer 1 now; most serious failure (ii)+(iii) via NAH-ind's 10⁻⁴⁰/level; unnamed (iv) conditional large-field control (no RP after conditioning); n = O(1) reformulation recommended |
| T24 revision | justified as ARGUED, with the free-field reading |
| T30 | free-gluon remark CORRECT; "not the trivial theory" misleading (Gaussian limit not excluded); "four-point bound" is not a non-Gaussianity test |
| x9 | honest; re-run byte-identical; B miss confirmed as coarse-sum artefact; B identity is tautological |

**Tally.**
- **Claimed:** PROVEN-HERE 53 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 6 / OPEN 12;
  ARGUED 31.
- **Corrected: 53 / 1 / 3 / 6 / 12; ARGUED 32** (+1: the §19.3 item-1 rate, if kept; 31 if it is reworded as in (4)).
  - SPEC-red +1 stays. It is a complete proof from named hypotheses once defects 1-4 are written in. They are precision
    defects, not gaps.
  - (CE-cond) +1 HYPOTHESIS-NEW is correct.
  - OPEN 12 is unchanged. (H-sig^S_loc)'s infinite-volume part is reduced, not discharged.
  - The reviewer's own suggestions in (6)-(7) are not counted.

---

## Binding fixes for session 11

1. **(CE-cond) quantifiers (l.3893-3896, l.3950-3951).** State it at one pair (g, n(g)) satisfying the compatibility
   inequalities, or with constants uniform in n ≤ n_max(g). Remove the circular g ≤ g_c(n), n = n(g).
2. **m_* ≥ n (l.3884-3885).** State j' = K - m_* + n ≤ K, i.e. m_* ≥ n. Replace l.3951's u_{j'} bound by
   u_{j'} ≥ g^{-2} + β_-(m_* - n)log L - R from (O1).
3. **e(R) rate (l.3894, l.3904).** Add a decay rate for e(R) to (CE-cond), or turn "possible for R ≥ R_0" into a stated
   compatibility hypothesis (R_0(g) with |N_{R_0}|e^{-a_d/g_{j'}²} ≪ g⁴).
4. **K-uniform conditions; notation (l.3890, l.3902-3904).** Use a_- = u_+^{-2}A_* and a_+ = u_-^{-2}A_*. Rename CB's a → a_d
   in δ_R.
5. **Lemma DIFF (ii) (l.3815).** "at every limit point with T_0 → ∞" (not "finite or infinite volume"). Add one line: at a
   fixed finite torus, (i) is the RP norm in the thermal OS space.
6. **Unnamed failure point (§19.5, l.3968-3972).** Add (iv): conditional large-field control near supp D. Theorem CB is not
   available for the conditional law (no RP), and §19.5's "coercivity" sentence (l.3955) is an assertion, not a route.
   Rank (ii)+(iii) as the binding obstruction: NAH-ind's ≈ 10⁻⁴⁰/level (P/PROOF l.38) against n ≍ log(1/g).
7. **T30 wording (l.4010-4015; §0 l.169-171; LOG finding 6).** "not the trivial theory" → "not the vacuum-only (dim H = 1)
   theory; Gaussianity of the limit is not excluded".
8. **LOG Next (non-Gaussianity).** Replace "a connected four-point bound" with a quantity that vanishes for every Gaussian
   gauge field (an odd, f^{abc}-carrying curvature cumulant), or a two-sided O(g⁶) running statement.
9. **RX9 fix 1 wording (l.3656, l.3661-3662).** "equivalently" / "Equivalent family form" → "stronger family form (implies
   the one-g form)". Fix 2: the joint form covers sequences with K_n ≥ K_0(·) only.
10. **§19.3 item 1 (l.3867-3868).** Replace the (1 - p_0)^{N/c} rate by the extensivity statement, or label it ARGUED.
11. **Cosmetic.**
    - SPEC-red header: add (O1), the joint θ-covariance and X-RP^S.
    - l.3982-3983: "95%" is the (1 - e^{-hλ})² factor, not a vacuum fraction.
    - l.3987: the B identity is tautological.
    - §19.6: record the T = 128/256 confirmation (-4.40, -4.19), credited to REVIEW_X10.
    - l.3802 / LOG l.608-610: harmonise the times.
    - β_0 := 11N/(48π²) at l.3563.

---

## Strategic verdict

- **What session 10 established (correctly).**
  - A sign-definite, vacuum-blind finite-volume target (Lemma DIFF).
  - An explicit, box-converged leading coefficient (LO-D, x9).
  - A correct diagnosis that "local ⇒ volume-uniform" is not an estimate.
  - A clean conditional implication (SPEC-red) whose central device, bounding the coarse-mediated term by a variance,
    removes session 9's θ-invariance obstacle and reaches joint limit points.
  - This is the lane's best infinite-volume result to date. It moves an apparently infrared target onto a background-uniform
    conditional weak-coupling statement, whose scale content is UV.
- **What it is worth, honestly.**
  - (i) It is a reduction to a new hypothesis that nobody has proven, and that layer 1 cannot currently supply. The binding
    obstruction is multi-level background uniformity, against NAH-ind's per-level loss.
  - (ii) Even if (CE-cond) were proven, the conclusion is the free (Gaussian) value and is consistent with a Gaussian limit.
    It is the statement "the theory is not empty at short distance", which AF predicts for free.
  - Do not present it as non-triviality in the constructive-QFT sense.
- **Recommendation, in order.**
  1. Apply binding fixes 1-4. They make SPEC-red's statement exact.
  2. Reformulate (CE-cond)(b) as a mean-square oscillation at a g-scaled threshold, so that n = O(1) (see (6)). Send layer 1
     the n = 1 version: source-augmented CE-exp at stage k, plus a conditional local large-field bound.
  3. The next science target is non-Gaussianity via the same conditional route, on a quantity with Gaussian value 0 (an odd
     f^{abc} cumulant), not a four-point bound on Φ.
  4. Leave §12.1 unchanged: §19 is conditional on a new, unadopted hypothesis.
