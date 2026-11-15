# REVIEW_X11: independent hostile review of session 11 of the YM4D existence lane (§20 and the [RX10-fix] changes)

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session11_snapshot.md (`diff` empty).
  - `diff session10 session11` read in full (the 11 fix hunks and all of §20).
  - §20 (l.4111-4507) read in full by offset; §19.4-§19.5 fix hunks re-read in context.
- LOG.md session 10 tail and session 11 (l.640-724); REVIEW_X10.md (all).
- checks: x10_criteria.md, x10_corner.py (read line by line), x10_out.txt, x10_time.txt.
- Read-only layer 1: ../ym4d-proof/SF.md Setting CE-exp, (H-exp), LOC-s, HULL, Theorem CE-exp and its proof, Corollaries
  CE-exp-𝒞, CE-exp^0, CE-exp^k with the [RSF2-fix] block (l.620-680, l.767-862), and §9.1/§10.1 (Theorem CE-Q (band),
  (CE-Q^∞), l.1010-1056, l.1175-1183); SF_LOG.md session-3 timeline; RLARGE.md §3.2 header.
- No web access. Literature remarks are the reviewer's own knowledge, marked [reviewer knowledge], and are not load-bearing.

Line numbers are EXISTENCE.md lines unless marked. No file other than this one was edited.

**Bottom line.**
- **RX10 fixes 1-11: all applied, all correct.** One residual: fix 8's LOG wording is fine, but §20.4 l.4440 re-introduces a
  vacuum-only claim that a one-point function cannot carry (see (4)).
- **Theorem SPEC-red^ms: CORRECT** as an implication. Every inequality re-derived; the constants close to exactly a/2.
  Lemma MK, Lemma MIX-cond: CORRECT. {q ≤ η} is 𝔅-measurable; Theorem CB is used only on the RP law.
  Two precision defects: (RLF-3^dis)_ε for ε < ε_1 is a strengthened hypothesis, not "Theorem CB, not new"; and the tally
  keeps both (CE-cond) and (CE-cond^ms) standing while counting only one.
- **Lemma CE-cov: CORRECT** (Cauchy bounds, polymer sum, λ-interpolation re-derived). Lemma CE-par: CORRECT in outline.
- **Missing-input list: right in substance, stale in two places, mis-ranked.**
  - Stale: §20 was written against SF.md as it stood before lane F's session 3 (04:26-04:38 UTC, concurrent). Since then,
    (CE-Q) is split into Theorem CE-Q (band, PROVEN analytic part) and (CE-Q^∞) (deep set, OPEN), and (L-hol)_k is
    "NOT VIABLE AS STATED", replaced by (L-loc)_k (OPEN, inside the B-NA wall).
  - (CE-loc)'s reason survives the update, with a different global event: Theorem CE-Q expands ∫ over 𝔇^c, and
    P(𝔇) ≤ |Λ|2^{n/2}e^{-a_*/(4g_0²)} is extensive, so P(𝔇^c) → 0 in infinite volume. The deep set, not the cut-good event, is
    now the global restriction.
  - Ranking: (M1) is not "the" binding input. (M2) carries (L-loc)_k, which sits inside layer 1's B-NA wall, and (M2) is
    needed level-uniformly (j = K - m_* → ∞). (M1) and (M2) are co-binding.
  - Ownership: both are layer-1 items: SF.md (lane F) plus RLARGE §3.2 branch (ii) for (CE-Q^∞), and branch (iii) for coarse
    large-field regions of V.
- **Lemma PO: CORRECT.** c_4 = ¾N(N² - 1) is re-derived by hand (BCH) and re-computed by an independent exact method (below).
  The Feynman-gauge value 0.008268·N(N² - 1) is reproduced. Lemma NG-wit: CORRECT, and nearly vacuous (see (4)).
- **Theorem NG-red: CORRECT as an implication** (Lemma REC's arithmetic re-derived). Two binding defects:
  - l.4440 "not vacuum-only" is false for a one-point function;
  - the honest content is "the limit is not sign-symmetric". No SU(N) lattice gauge measure is sign-symmetric, since
    U → U^{-1} is not a symmetry of the Wilson action.
- **Conclusion "excludes abelianised limits, not Gaussian-connection limits": RIGHT.** What would certify non-Gaussianity is
  in (4c).
- **x10: honest; re-run byte-identical.** One unrecorded deviation from the criteria: the sample count. Control C is a
  symmetry tautology.
- **Corrected tally:** 57 / 1 / 3 / **9** / 12 (or 13; see (6)); **ARGUED 36**.

---

## (1) RX10 fixes (priority 1)

| Fix | Where (session-11 lines) | Verdict |
|---|---|---|
| 1 (CE-cond) at one pair (g, n(g)) | l.3925-3933, l.3992-3994 | CONFIRMED. The circular g ≤ g_c(n), n = n(g) is gone; the n-uniformity caveat is stated |
| 2 m_* ≥ n; u_{j'} lower bound | l.3913-3915, l.3992 | CONFIRMED (j' = K - m_* + n ≤ K ⇔ m_* ≥ n; (O1) at depth m_* - n) |
| 3 e(R) rate; R_0(g) | l.3927, l.3942-3945 | CONFIRMED. R_0 ≍ 4m_e^{-1}log(1/g), so |N_{R_0}| is polylog and the third condition holds for g small. The counterexample e(R) = 1/log log R is apt |
| 4 a_±; a_d, R_O | l.3916-3917, l.3939-3941, l.3962-3963 | CONFIRMED. a_- ≤ a ≤ a_+ makes the three conditions K-uniform |
| 5 Lemma DIFF (ii) scope | l.3836-3843 | CONFIRMED. The thermal formula is copied correctly from REVIEW_X10 |
| 6 failure point (iv); ranking | l.3997-4001, l.4019-4025 | CONFIRMED. ε_*·10^{-40n} ≈ ε_*g^{42} at n = log(1/g)/(2 log 3): 10^{-40n} = g^{40 log 10/(2 log 3)} = g^{41.9}. Correct |
| 7 T30 wording | §0 l.171-172, l.4069-4071, LOG l.644-646 | CONFIRMED |
| 8 LOG Next | LOG l.660-663, l.4075-4078 | CONFIRMED. The pointer to §20.4 is appropriate |
| 9 family form "stronger"; joint scope | l.3671-3672, l.3677-3681, l.3687-3689 | CONFIRMED |
| 10 §19.3 rate → extensivity | l.3893-3897 | CONFIRMED. The ergodic-theorem remark is correctly hedged ("not claimed") |
| 11 cosmetic | l.3577-3578, l.3823, l.3910, l.4036-4051 | CONFIRMED. β_0 = 11N/(48π²) is the standard b_0 of μdg/dμ = -b_0g³, consistent with Λ ∝ e^{-u/(2β_0)}, u = 1/g² [reviewer knowledge] |

Tally after the fixes alone: 53 / 1 / 3 / 6 / 12, ARGUED 31. **Agreed.** The §19.3 rate was reworded, not kept.

---

## (2) Restated (CE-cond), SPEC-red^ms, MIX-cond, MK (priority 2)

**Lemma MK (l.4157-4166): CORRECT.**
- With ∫K_k(V, U)dV = 1, the law is a forward Markov chain U_0 → U_1 → …, and e^{-S_{k+1}} = ∫K_ke^{-S_k} gives the marginal of
  U_j.
- The joint density of (U_j, …, U_K) factorises as [e^{-S_j}Π_{j≤k<j'}K_k]·[Π_{k≥j'}K_k]. (i) and (ii) follow by Bayes.
- For n = 1 the conditional law is ∝ e^{-S_j(U)}K_j(V, U). This is exactly the stage-j integrand, with S_j the **exact** level-j
  effective action. Layer 1 represents that action only on small-field domains, which is (M1)'s point.

**Lemma MIX-cond (l.4168-4178): CORRECT.**
- (i): |Cov_{μ^l}| ≤ (2M)² = 4M², and the mean-difference product is ≥ -(4M)²q(1 - q) ≥ -16M²q. Total -20M²q.
- (ii): use |(1 - q)E_sY| + q|E_lY| ≤ |E_sY| + 2Mq. (Writing E_sY + q(E_lY - E_sY) would give 4Mq; the stated 2Mq is right by
  the first route.)
- (iii): tower property, q² ≤ q, Markov.
- **{q ≤ η} is legitimately 𝔅-measurable**: q is a σ(U_{j'})-measurable version of P(B_N | 𝔅). Hypotheses quantified
  "P_K-a.e. V" are version-independent.
- On q ∈ {0, 1} the formulas hold with the undefined law dropped. In (b^q)/(a^s) the hypotheses are only asked for q < 1, and
  on G, q ≤ η < 1. Consistent.

**(LF-loc)^ε (l.4183-4187): CORRECT given its hypothesis; tally defect (binding, minor).**
- The union bounds and |N_R^{(i)}| ≤ 6L^{4(j'-i)}|N_R| are fine.
- But (RLF-3^dis)_ε with ε < ε_1 is **strictly stronger** than (RLF-3^dis): more cubes are bad, and a_d(ε) is smaller. It is
  not implied by the §13.4 hypothesis.
- Either fix ε := ε_1 in SPEC-red^ms and NG-red (nothing in §20 needs ε < ε_1; ε only has to contain the typical field ≍ g),
  or list (RLF-3^dis)_ε among the hypotheses.
- l.4484's "(LF-loc)^ε is Theorem CB at threshold ε, not new" is true of the proof, not of the hypothesis.

**SPEC-red^ms (l.4209-4239): CORRECT. Re-derivation.**
- *Law of total covariance*: exact.
- *First term, on G = G_R^ε ∩ {q ≤ η}*:
  - MIX-cond (i) + (a^s) give (1 - q)[(1 - r)a - β_ag_j²Q_w - e] - 20M²q.
  - With (1 - r) ≥ 3/4, (3/4)a - e ≥ 0 (true: e ≤ a_-/32) and q ≤ η, this is ≥ (3/4)a - e - ηa - β_ag_j²Q_w - 20M²η.
  - Off G the bound is ≥ -4M². The constant c := (3/4)a - e - ηa - 20M²η satisfies E[1_Gc] ≥ c - δ·max(c, 0) ≥ c - δa.
  - So E[Cov | 𝔅] ≥ c - δa - 4M²δ - β_ag_j²E Q_w. Matches l.4227.
- *Jensen/(MOM_4)*: E Q_w ≤ WC_4^{1/2}g_{j'}². Correct.
- *Second term*:
  - The -Var(E[D | 𝔅]) step needs Var E[θD | 𝔅] = Var E[D | 𝔅]. That follows from the joint law's θ-invariance with θ mapping
    σ(U_{j'}) to itself (the plane is a block boundary at every level on L^K-divisible tori). Inherited from §19.4, accepted
    in REVIEW_X10.
  - On G_R^ε, |E[D | 𝔅]| ≤ β_bQ_w + e + 2Mq. Off it, ≤ 2M.
  - (x + y + z)² ≤ 3Σ, Minkowski ||Q_w||_2 ≤ WC_4^{1/2}g_{j'}², and E q² ≤ δ'_R give E[E[D | 𝔅]²] ≤ 3β_b²W²C_4g_{j'}⁴ + 3e² +
    12M²δ'_R + 4M²δ_R. Correct.
- *Closing*:
  - e ≤ a_-/32 holds by R(g).
  - 3e² ≤ 3a_-²/1024 ≤ a/32 holds since a_- ≤ a ≤ 1.
  - β_a-term: (K) gives β_aWC_4^{1/2} ≤ A_*/(16ρ). With ρ = (u_+/u'_-)², the bound is A_*u'_-/(16u_+²u_-) ≤ a_-/16, using
    u'_- ≤ u_- (true: β_-(m_* - n) ≤ β_-m_*).
  - β_b-term: ≤ A_*/(16ρu'_-²) = a_-/16.
  - Bracket ≤ a_-/16 by (C3).
  - a(3/4 - 1/32 - 1/32 - 3/16) = a/2. **Exact.**
- *(C3) for g small*: η = (δ'_R)^{1/2} ≍ g^{-p_d/2}e^{-a_d/(2g_{j'}²)}·poly(R), against a_- ≍ g⁴. True.
- *Order of choices (l.4219-4221)*: non-circular. n enters (K) through β_a, β_b and **also A_*(n)**, the n-step conditional
  value. A_* depends on n, so n_0 is defined implicitly by a g-free inequality, not by the explicit formula of l.4247.
  - Write "A_* = A_*(n)" in l.4247. This is cosmetic: the argument is unaffected because the inequality is g-free.

**What is genuinely gained (agreed).** The mean-square form makes the classical part of E[D | V] cost β_b²W²C_4g⁴ against
a ≍ g⁴ at fixed n, instead of ε²L^{-4n} against g⁴. The NAH-ind per-level loss is removed **from the statement** (l.4251-4252
says so honestly).

**Two caveats for the text.**
- (a) (b^q) for V ∈ G_R^ε with ε fixed is a **pointwise** quadratic bound over a fixed-size background domain. Its
  constant β_b must cover the classical value c_bL^{-4n}Q_w at backgrounds of size ε, not ≍ g. That is fine (it is
  quadratic), but the relative O(g²) fluctuation part must also be uniformly quadratic there, not only near V = 1. Say so in
  the reading (l.4195-4199).
- (b) l.4326: x9 B's "conditional part within 2e-6 of A(1, 1)" is at h = 1. SPEC-red^ms requires h ∈ L^nZ_{≥1} (h ≥ 3 at
  L = 3), so x9 does not inform A_* at an admissible h. Mark this.

**(CE-cond^ms) and (MOM_4) as hypotheses.** Well formed. (MOM_4)'s scaling g⁴ is the natural one. The log²(1/g) remark for a
g^{-p_d} prefactor is right: ∫4t³min(1, Cg^{-p}e^{-at²/g²})dt ≍ t_0⁴ with t_0² ≍ g²p log(1/g)/a.

---

## (3) Lemma CE-cov and the missing-input list (priority 3)

**Lemma CE-par (l.4256-4266): CORRECT in outline.**
- Steps 1-2 are finite sums. Step 3 uses Morera with Fubini (bounded integrand). Steps 3-4 are a uniformly convergent power
  series composed with a holomorphic map into the closed polydisc, then Weierstrass.
- The uniform (H-exp) bound in ζ is what keeps K#(ζ) inside the convergence polydisc. Accepted.

**Lemma CE-cov (l.4268-4289): CORRECT. Re-derivation.**
- κ'' = 5κ_0 + 3 - 3κ_0 - 3 = 2κ_0, and h_* is exactly the H'_0 ≤ c_0 threshold.
- With |λ| < h_*/(2h_0) and |z_i| < h_*/(4s_i), |F_X(ζ)| < h_*e^{-κd(X)} (d(X_i) = 0; this also holds when X_1 = X_2).
  Source pieces have d = 0, so κ is free for them.
- ∂_{z_1}∂_{z_2}ℒ = Cov_{P_λ}, ∂_{z_1}ℒ = E_{P_λ}. ℒ is a holomorphic logarithm of 𝒵, and derivatives of any holomorphic log
  agree.
- F#(Y) ⊃-support: the z_i pieces have Y(X_i, S) ⊃ X_i^+ ⊃ X_i, and F#(Y) uses only pieces with Y(X, S) ⊂ Y. So the
  derivatives vanish unless Y ⊃ X_1 (∪ X_2). Correct.
- Cauchy for the (1,1) mixed derivative on the bidisc: sup/(z_{0,1}z_{0,2}). The sum over Y ∋ Q is Σe^{-2κ_0d} ≤ K_0.
  B_2 = 16K_0C_1c_0s_1s_2/h_*² and B_1 = 4K_0C_1c_0s_1/h_*. Correct.
- λ-step: |G'(t)| ≤ B/(Λ_0 - t), so ∫_0^1 = B log(Λ_0/(Λ_0 - 1)) ≤ B·x/(1 - x)|_{x=1/Λ_0} ≤ 2B/Λ_0 = 4Bh_0/h_*.
  This gives (i) 64K_0C_1c_0s_1s_2h_0/h_*³ and (ii) 16K_0C_1c_0s_1h_0/h_*². **Both exact.**
- The bound is not sharp: it ignores the e^{-κ_0 dist(X_1, X_2)} that Y ⊃ X_1 ∪ X_2 forces. That is harmless for (a^s), where
  the reference covariance is O(1)·s_1s_2 at an O(1) separation.
- **Update:** the e^{3·272κ'} ≈ e^{3.8·10⁵} constant (l.4293) is removable now that SF's Corollary CE-exp-col (§10.3,
  PROVEN-HERE, not counted) holds. Lemma CE-cov should be re-stated over CE-exp-col (rate κ_c - κ_0 - 2κ̃_0 - 3 in d^+; no
  e^{272κ'}). This is a recommendation, not a defect.
- "Application" (l.4294-4304) is correctly labelled conditional, with the identification ARGUED, not written. That
  ARGUED item is **not** among the +4 ARGUED in the tally (see (6)).

**The missing-input list (l.4306-4331).**
- **(M1) (CE-loc): correct in substance; its stated reason is stale (binding).**
  - SF.md's session 3 (SF_LOG l.75-92: §9 at 04:26:13, [RSF2-fix] 04:26-04:29, §10 at 04:34-04:38 UTC) ran concurrently with
    §20 (targets 04:27, §20.3 appended 04:34). It now contains **Theorem CE-Q (band)** (SF l.1030-1041; analytic part
    PROVEN-HERE, CONDITIONAL ⇐ (FP-loc)_0 after Lemma SF-N♮) and **(CE-Q^∞) OPEN** (the deep set 𝔇).
  - So "(CE-Q) OPEN" (l.4312, l.4470, LOG finding 3) is out of date, and "CE-exp^0 CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮)"
    (l.4319) is now ⇐ (FP-loc)_0 alone.
  - **The conclusion survives with a different global event.** Theorem CE-Q expands ∫_{𝔇^c}, and
    μ_wn(𝔇) ≤ |Λ|2^{n/2}e^{-a_*/(4g_0²)} (SF l.1043) is extensive, so P(𝔇^c) → 0 as |Λ| → ∞. MIX-cond still cannot absorb it.
  - Rewrite (M1)'s reason as "the band expansion (Theorem CE-Q) is still conditioned on the **global** event 𝔇^c". The
    missing piece is (CE-Q^∞) **localised** (deep sites far from Ω excised and priced in U-variables) plus coarse large-V
    regions (RLARGE branch (iii)).
- **Is (CE-loc) "the" binding input? No; co-binding with (M2) (binding fix).**
  - (M2) needs CE-exp^k level-uniformly at j = K - m_* → ∞. Per SF's [RSF2-fix CEk-1/2] (l.840-856), its activity input is
    **(L-loc)_k, OPEN, inside the B-NA wall**: mixed-derivative decay of the main-term densities on a uniform polydisc, behind
    (a5-G♯) and (G♯-patch). (L-hol)_k, which l.4321 cites, is "NOT VIABLE AS STATED". The inherited activities are added,
    and composition goes through CE-col (now proven in the rate sense).
  - The B-NA wall is layer 1's central open wall. (M1), by contrast, is the standard Balaban/GJS large-field/small-field
    localisation [reviewer knowledge] once the small-field step exists.
  - So, if anything, (M2) is the deeper input. Write "(M1) and (M2) co-binding; (M2) contains (L-loc)_k (B-NA wall)", and
    reword ARGUED item 3 of l.4490 accordingly.
- **Is it a layer-1 item? Yes.**
  - Owners: SF.md (lane F) for the localised band expansion and (N5-reg)_j.
  - RLARGE.md §3.2 branch (ii) for (CE-Q^∞) (SF_LOG l.110 already assigns it there).
  - RLARGE branch (iii) for coarse background large-field regions (V ∉ 𝒱^sf away from N_R). l.4308 omits branch (iii);
    add it.
- **(M1) sub-claim l.4316-4317 (binding, minor):** "cut sites inside Ω … put into B_N at probability ≤ |Ω|2^{n/2}e^{-p²/4}" is
  the **reference** (white-noise) probability.
  - Under P_K, Z is not white noise: it is ν tilted by exp(ΣH), and Theorem CB does not see Z-events.
  - Either bound the Z-event's P_K-probability (e.g. from the band expansion's polymer weights), or define B_N in U-variables
    only.
- (M3) (A-cond), (M4) (BG-reg), (M5) (MOM_4): correctly stated and owned.
  - (M3) should note that A_* is the conditional value at admissible h ∈ L^nZ (see (2)(b)).
  - (M4) BR1/NAH1: agreed.

---

## (4) Lemma PO, NG-wit, NG-red; what is excluded; what would certify non-Gaussianity (priority 4)

### (4a) Lemma PO: independent verification

**By hand (BCH), i.i.d. links.**
- P_12 = U_1(0)U_2(e_1)U_1(e_2)^{-1}U_2(0)^{-1}, X = (A_1(0), A_2(e_1), -A_1(e_2), -A_2(0)).
- L_23 = A_2(0) + A_3(e_2) - A_2(e_3) - A_3(0); L_31 = A_3(0) + A_1(e_3) - A_3(e_1) - A_1(0).
- Of P_12's links, only A_1(0) (in L_31 with sign -) and A_2(0) (in L_23 with sign +) are shared.
- A pair (X_i, X_j) contributes only if one member pairs with L_23 and the other with L_31, so only (X_1, X_4) contributes.
  Its BCH term is ½[X_1, X_4] = -½[A_1(0), A_2(0)].
- With E tr([X, X'][L_1, L_2]) = K(γ_{XL_1}γ_{X'L_2} - γ_{XL_2}γ_{X'L_1}) (pairings inside a commutator vanish by antisymmetry
  of f) and K = Σ_{ab}tr([T^a, T^b]²) = -½f^{abc}f^{abc} = -½N(N² - 1):
  - contribution -½·K·(0·0 - (-1)(+1)) = -½K = ¼N(N² - 1).
- Degree 4 is O^{(4)} = Σ_cyc tr(Y_P^{(2)}[L_Q, L_R]) by cyclicity of tr(A[B, C]). The corner's cyclic axis symmetry makes the
  three terms equal: **c_4 = ¾N(N² - 1)**.
- Odd degrees vanish by x ↦ -x. χ = 1 near 1. The tail is e^{-c/σ}. **Confirmed.**

**By computer, an independent method** (scratchpad `rerun_x11/po_exact.py`; it shares no code with x10).
- My own corner geometry, series exp/log for complex matrices.
- The exact degree-4 Gaussian mean, computed by discrete Cauchy-integral extraction of the a⁴ and a²b² Taylor coefficients of O
  on every coordinate 2-plane: E p = 3Σ_ic_{i,4} + Σ_{i<j}c_{ij,22}. This is deterministic, with no Monte Carlo and no use of
  the Wick formula.
- My own direct-sum lattice propagator for the Feynman case.
- Results:
  - i.i.d.: **c_4 = 4.500000000000 (SU(2)), 18.000000000000 (SU(3))**, imaginary parts ≤ 4e-15.
  - Feynman gauge: c_4 = 0.049608 / 0.198431 at T = 16 and 0.049607 / 0.198429 at T = 32, i.e. **0.008268·N(N² - 1)**.
    G(0) = 0.154387, 0.154796. This reproduces x10 B to all printed digits.
- **Lemma PO is confirmed exactly, by a method independent of the Wick formula it states.** (The x10 B0 line only checks the
  formula against itself at Γ = 1.)

### (4b) Lemma NG-wit, Theorem NG-red, and the reading

- **NG-wit (l.4348-4351): CORRECT.**
  - O is odd under Y ↦ -Y. χ is even because ||1 - e^{-Y}|| = ||e^{-Y}(e^Y - 1)|| = ||1 - e^Y|| for unitary e^Y.
  - C-evenness re-checked: Y ↦ -Y^T maps tr(Y_1[Y_2, Y_3]) to itself.
- **NG-wit is nearly vacuous: say so (binding wording).**
  - No SU(N) lattice gauge measure of Wilson type is sign-symmetric. The joint flip corresponds to U_b ↦ U_b^{-1} on every link.
  - Under that flip, log P ↦ -L + ½Σ[X_i, X_j] + …, not -log P. Re tr e^{Y} then changes at cubic order through the
    L·[X, X] cross term, i.e. the lattice three-gluon vertex.
  - So "the limit is not sign-symmetric" holds trivially at every finite K and volume. NG-red adds only its **uniformity**
    (a lower bound ≍ g_j⁴ surviving every limit point).
  - The only sign-symmetric competitor is an exactly abelianised / Lie-linear law, i.e. N² - 1 free photons with linear
    "holonomies". That is a strawman for an SU(N)-valued limit.
- **Lemma REC (l.4412-4417): CORRECT.**
  - Iteration: x_j = Σ_{i<I}Γ^i(g_{k_i}⁴c + η_i) + Γ^Ix_K.
  - g_{k_i}⁴ ≤ ρ_n^ig_j⁴, using AF (g grows towards coarse levels, so ρ_n ≥ 1).
  - Σ_{i≥1}(γρ_n)^i ≤ 2γρ_n and Σ_{i≥0} ≤ 2 for γρ_n ≤ ½.
  - 1/8 + 1/8 + 1/4 = 1/2. **Exact.**
- **Theorem NG-red (l.4419-4432): CORRECT as an implication**, with two cosmetic fixes:
  - off G the bound should use max_{t'}||O_{t'}||_∞ (it is written with ||O_t||_∞);
  - the "second r_1" absorbing e(R), δ_R, δ'_R needs a separate positive constant (if r_1 = 0 nothing is absorbed). R(g) must
    satisfy e ≤ (const)·g_j⁴ with g_j the **smallest** coupling in the recursion.
  - (N3) with g_j⁴ ≥ u_+^{-2} and X_top ≍ g³ needs γ^I ≲ g, so I ≍ log(1/g)/log(1/γ). Correct.
  - The witness resolution m_* = I(g)n therefore moves with g. Under the one-g form this is legitimate. State in the
    theorem that the witness is a g-dependent observable (l.4425 says "at resolution m_*"; adequate).
- **(CE-cond^3)'s Γ-term closure (l.4397-4405): plausible as a hypothesis; it needs one more clause.**
  - The classical cubic of tr(Y_1[Y_2, Y_3]) at an interpolated background is a trilinear form in coarse logs. For N ≥ 3,
    tr(Y_1Y_2Y_3) has both f^{abc} (real part) and d^{abc} (imaginary part) pieces.
  - The d-part is C-odd and drops out of a C-even real observable **only if** the conditional law is C-covariant. State that C
    is a symmetry of the chain kernels (it is, for Wilson-type actions and conjugation-equivariant block maps
    [reviewer knowledge]), or allow d-type members in 𝒯.
- **l.4440 "not vacuum-only": FALSE (binding).**
  - A one-point function ω(O) ≠ 0 is compatible with dim H = 1: the OS vacuum vector already carries ⟨Ω, [O]Ω⟩ = ω(O).
  - Example: links constant in x, U_μ(x) = e^{a_μ} with non-commuting a_μ. Every plaquette equals e^{a_1}e^{a_2}e^{-a_1}e^{-a_2}
    and its rotations. The configuration is translation invariant, the gauge-invariant O is deterministic and ≠ 0, and the
    point-mass state has a one-dimensional OS space.
  - "Not vacuum-only" comes from SPEC-red(^ms), not from NG-red. Delete it from l.4440 and from LOG finding 5's implicit
    reading.

### (4c) Is "excludes abelianised limits, not Gaussian-connection limits" right? What would certify non-Gaussianity?

**Yes, the conclusion is right**, and it corrects REVIEW_X10 (7)(a): that review's "vanishes for every centred Gaussian gauge
field" was wrong for holonomy-built observables.
- x10 B and the reviewer's B-recomputation give c_4 > 0 for both the i.i.d. and Feynman-gauge covariances, the same sign that
  NG-red's c(t_0) would carry through its path-ordering part.
- So NG-red cannot separate YM from "free Maxwell^{N²-1} with holonomies taken at charge g". That is the physically relevant
  trivial scenario for an AF theory.

**"Gaussian connection" is gauge-dependent, so (NG-conn) as worded (l.4443: a witness vanishing for every Gaussian connection)
is not well posed.**
- A law that is Gaussian in Feynman gauge is not Gaussian in axial gauge, and vice versa.
- Lemma PO shows that holonomy observables of a Feynman-Gaussian connection have non-zero odd f^{abc} cumulants. So no single
  gauge-invariant odd witness can vanish on "Gaussian in some gauge".
- Re-pose (NG-conn) with the gauge named.

**What would certify non-Gaussianity, in increasing strength (reviewer, ARGUED; not counted):**
1. **Against "Gaussian in a complete (maximal-tree / axial) gauge".**
   - The f^{abc}-odd third cumulant E[f^{abc}x_1^ax_2^bx_3^c] of the logs of three complete-gauge link variables (equivalently,
     lasso holonomies based at the tree root; gauge-invariant up to the global conjugation at the root, which the f-contraction
     ignores).
   - It is **exactly 0** for every centred measure that is Gaussian in that gauge (odd moment; no path-ordering contamination,
     since the gauge-fixed links *are* the variables).
   - In Wilson YM it is O(g⁴) from the lattice three-gluon vertex (the L·[X, X] term of ½|Y_P|²; the Haar Jacobian is even).
   - It fits NG-red's one-point architecture, at the price of a lasso-shaped (less local) observable. Its tree-level value must
     be computed and shown ≠ 0 (cf. (c3-nz)).
   - This is the closest provable certificate. It excludes a well-defined Gaussian class, not all of them.
2. **Against the free theory (fixed Feynman Γ): the one-loop running, not two loops.**
   - A **two-sided** statement that g_j^{-4}·Cov(θD, D) at fixed physical separation changes between resolutions m_* and m_* + n
     by the factor (u_j/u_{j+n})² to relative accuracy o(g²) excludes every fixed-Γ free theory. β_0 suffices; the two-loop
     β_1 is not needed.
   - But an arbitrary Γ can mimic any single two-point function, so the running alone does not exclude all Gaussian connections.
3. **Against every Gaussian connection in a fixed gauge with arbitrary Γ: a Gaussian-consistency defect.**
   - Take a connected four-point function of a gauge-invariant composite minus its value **computed by Wick from the
     model's own gauge-fixed connection two-point function** (path ordering included, as in Lemma PO).
   - This is what the brief's "connected 4-point beyond its Gaussian-connection value" should mean. It needs two-sided control
     at relative order g² (a g⁶ effect against g⁴ leading terms), the same difficulty as option (B).
4. **The constructive gold standard** [reviewer knowledge]: in the continuum limit at fixed physical scale, non-zero connected
   n ≥ 3 Schwinger functions of renormalised, smeared gauge-invariant fields (e.g. gradient-flowed E(t)), or a non-trivial
   scattering amplitude (Haag-Ruelle, needs a gap). Far beyond this lane.

Recommendation: re-pose (NG-conn) as item 1 (named gauge). Pursue it through NG-red's recursion, whose architecture transfers
unchanged with 𝒯 replaced by lasso logs. Count (NG-conn) as OPEN once re-posed.

---

## (5) Check x10 and the re-run (priority 5)

**Pre-registration order.**
- §20.0 04:27 < criteria 04:27:55 < script < run 04:31:03-04:33:17. §20.1-§20.3 appended at 04:34 after SU(2) A lines were read
  (04:32:48). Disclosed; no §20.1-§20.3 statement uses an x10 number (checked). Consistent.

**Code, read line by line. Correct.**
- Basis normalisation tr(T^aT^b) = -½δ.
- The PLAQ tables match the plaquette definition.
- eigh-based expm for anti-Hermitian A; eig-based principal log, with the anti-Hermitian projection only removing rounding.
- Antithetic pairs give an unbiased even part.
- wick_c4 implements the l.4355 formula.
- Feynman G is the 4D lattice T^{-4}Σ_{k≠0}e^{ikr}/k̂²; corner at x_0 = 0 in directions 1-3; same-direction link offsets equal
  midpoint offsets.

**Defects (cosmetic-binding).**
- **Unrecorded deviation from the criteria.**
  - x10_criteria.md: "n = 2·10⁶ samples per σ". The run used 4·10⁵ antithetic pairs (8·10⁵ evaluations) for SU(2) and 2·10⁵
    pairs for SU(3) (script l.113; out lines "n=400000/200000 antithetic pairs").
  - The pass criteria are SE-relative, so the verdicts stand. But §20.5 must record the deviation (pre-registration
    discipline).
- **Control C is a symmetry tautology.** O_lin is an odd cubic polynomial in x, so E[O_lin] = 0 identically. C tests only that
  the RNG is unbiased. Label it as such, as REVIEW_X10 did for x9's B identity. It is not a control of "path ordering is the
  cause". The real discriminator is A against the linearised zero, and B0 against A.

**Re-run of x10 (reviewer, under the mandatory lock).**
- Lock acquired 04:46:05 UTC, with no wait. A single `rmdir` at 04:48:36, no trap, no process left running. (A later
  `locks/numeric`, created 04:49:41, belongs to another holder.)
- nice 10; OMP/OpenBLAS/MKL/vecLib threads 1; `python3` without -I; no `timeout`. Load 2.87 (< 8); 42% memory free.
- **x10 output is byte-identical to checks/x10_out.txt** except the wall/RSS line (132.9 s / 250 MB against 134.3 s / 267 MB).
  The RNG is seeded, so every number reproduces.
- The reviewer's po_exact.py ran in the same acquisition (17 s).
- Files: scratchpad `rerun_x11/x10_out_rerun.txt`, `rerun_x11/po_exact_out.txt`, `rerun_x11/time.txt`.

**Load-bearing:** A1, A2 as stated. Lemma PO is now confirmed three ways: by hand, by x10's MC, and by the reviewer's exact
extraction.

---

## (6) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| RX10 fixes 1-11 | CONFIRMED, all |
| Lemma MK, Lemma MIX-cond | CORRECT; {q ≤ η} ∈ 𝔅 legitimately; CB only on the RP law |
| (LF-loc)^ε | CORRECT given (RLF-3^dis)_ε, which is a strengthened hypothesis for ε < ε_1 (take ε = ε_1 or list it) |
| Theorem SPEC-red^ms | CORRECT; every inequality re-derived to exactly a/2; A_* = A_*(n) to be written; x9's A(1,1) is at an inadmissible h |
| Lemma CE-par, Lemma CE-cov | CORRECT (constants exact); restate over CE-exp-col to remove e^{3·272κ'} |
| Missing inputs (M1)-(M5) | substance right; (M1)'s reason stale (CE-Q band now proven; global event is now 𝔇^c); (M2) cites the withdrawn (L-hol)_k → (L-loc)_k (B-NA wall); (M1), (M2) co-binding; owners: SF + RLARGE (ii) and (iii); B_N Z-event probability is a reference, not a P_K, bound |
| Lemma PO | CORRECT; c_4 = ¾N(N² - 1) by hand and by the reviewer's exact method; Feynman value reproduced |
| Lemma NG-wit | CORRECT; nearly vacuous (no Wilson-type SU(N) measure is sign-symmetric) |
| Lemma REC, Theorem NG-red | CORRECT as implications; l.4440 "not vacuum-only" FALSE; C-covariance (or d-type members) needed for the Γ-closure |
| "excludes abelianised, not Gaussian-connection limits" | RIGHT; (NG-conn) as worded is gauge-dependent, so re-pose with a named gauge |
| x10 | honest; re-run byte-identical; sample-count deviation unrecorded; C is a tautology |

**Tally.**
- **Claimed:** PROVEN-HERE 57 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 8 / OPEN 12;
  ARGUED 35.
- **Corrected: 57 / 1 / 3 / 9 / 12; ARGUED 36.**
  - PROVEN-HERE +4 is agreed: SPEC-red^ms, CE-cov, PO, NG-red. PO is a standard Wick computation, but it is a new, checked
    statement that decides T33's null-model question. NG-red counts as a reduction, like SPEC-red.
  - HYPOTHESIS-NEW 8 → **9**. l.4485-4486 says session 10's (CE-cond) and Theorem SPEC-red "stand as stated", and (CE-cond^ms)
    "replaces" it with "no count change". Both cannot hold. (CE-cond^ms) is a different statement (restricted law, pointwise
    quadratic (b^q), background-quadratic loss in (a^s)); it implies neither (CE-cond) nor is implied by it. Either count it
    (+1, my choice) or retire (CE-cond) and SPEC-red to "superseded" (then 8).
  - (RLF-3^dis)_ε: if ε = ε_1 is fixed (recommended), no count; otherwise +1 (10).
  - OPEN 12 is defensible. If (NG-conn) is re-posed with a named gauge (4c), count it: 13. (CE-loc) stays layer 1's and
    uncounted, correctly.
  - ARGUED 35 → **36**. Add the "Application" identification of the reference values with g_j⁴A_cond(V) + … (l.4302-4304,
    explicitly "ARGUED, not written"). Item 3 of l.4490 is to be reworded to "(M1), (M2) co-binding".
  - The reviewer's (4c) suggestions are not counted.

---

## Binding fixes for session 12

1. **l.4440 (and LOG finding 5's reading).** Delete "not vacuum-only" from NG-red's conclusion. A one-point function is
   compatible with dim H = 1 (the constant non-commuting-link example). Vacuum-only exclusion comes from SPEC-red(^ms).
2. **(M1) reason (l.4310-4315, l.4469-4470, LOG finding 3).** Update to SF session 3:
   - Theorem CE-Q (band) proven, analytic part, CONDITIONAL ⇐ (FP-loc)_0;
   - the remaining global restriction is the deep set 𝔇, with P(𝔇) ≤ |Λ|2^{n/2}e^{-a_*/(4g_0²)} extensive;
   - (CE-loc) = (CE-Q^∞) localised + coarse large-V regions.
   - Replace "(CE-Q) OPEN" by "(CE-Q^∞) OPEN"; l.4319: CE-exp^0 ⇐ (FP-loc)_0 alone (after SF-N♮).
3. **(M2) (l.4318-4322).** (L-hol)_k → **(L-loc)_k** (SF [RSF2-fix CEk-1], OPEN, B-NA wall), plus the inherited activities;
   composition via CE-exp-col. Rank (M1), (M2) **co-binding**. Reword ARGUED item 3 (l.4490).
4. **Owners (l.4308).** Add RLARGE §3.2 branch (iii) (coarse background large-field regions) next to branch (ii).
5. **B_N Z-event (l.4316-4317).** The |Ω|2^{n/2}e^{-p²/4} bound is under the reference ν, not P_K. Bound it under P_K, or keep
   B_N in U-variables only.
6. **(RLF-3^dis)_ε (l.4183-4185, l.4484).** Fix ε := ε_1, or list (RLF-3^dis)_ε as a hypothesis of SPEC-red^ms/NG-red (it is
   stronger for ε < ε_1).
7. **Tally (l.4479-4490, §0 l.173-174, LOG).** HYPOTHESIS-NEW 9 (count (CE-cond^ms), or mark (CE-cond)/SPEC-red superseded);
   ARGUED 36 (the CE-cov application identification).
8. **(NG-conn) (l.4443, l.4477, LOG Next).** Re-pose with a named gauge. "Every Gaussian connection" is gauge-dependent, and by
   Lemma PO no gauge-invariant odd witness vanishes on all of them. Proposed: the f^{abc}-odd third cumulant of complete-axial
   (lasso) link logs. State NG-wit's near-vacuity (no Wilson-type SU(N) measure is sign-symmetric).
9. **NG-red's Γ-closure (l.4397-4405).** Add C-covariance of the chain (so d^{abc} parts drop), or admit d-type members in 𝒯.
   Off-G bound: use max_{t'}||O_{t'}||_∞. Use a separate constant for the absorbed e(R), δ_R, δ'_R terms.
10. **SPEC-red^ms cosmetic.** A_* = A_*(n) in l.4247. l.4326: x9's A(1, 1) is at h = 1, inadmissible for h ∈ L^nZ. In the
    reading at l.4195-4199, note that (b^q) must be uniformly quadratic over the fixed-ε domain, including the fluctuation part.
11. **x10 record (§20.5).** Record the sample-count deviation (criteria 2·10⁶ per σ; run 8·10⁵ / 4·10⁵ evaluations). Mark
    control C as a symmetry tautology. Credit the reviewer's exact re-computation.
12. **Recommendation (not binding).** Restate Lemma CE-cov over Corollary CE-exp-col (no e^{272κ'} factor).

---

## Strategic verdict

- **What session 11 established (correctly).**
  - The n ≍ log(1/g) obstruction of session 10 is removed **from the statement**. A mean-square (CE-cond^ms) plus a local
    fourth moment gives SPEC-red's conclusion with n fixed before g.
  - The conditional large-field point is disposed of cleanly by the tower property (MIX-cond). That is a genuine and reusable
    device.
  - Lemma CE-cov is the correct, routine transfer from a polymer representation to source covariances.
  - Lemma PO is a real correction, to the lane's brief and to REVIEW_X10: odd f^{abc} holonomy cumulants do **not** vanish
    for Gaussian connections.
- **What it is worth, honestly.**
  - (i) SPEC-red^ms is a cleaner reduction to a hypothesis nobody has proven. Its obstruction has moved into layer 1's
    (CE-Q^∞)-localisation and (L-loc)_k. The second is inside the B-NA wall, which is layer 1's main wall, so the lane's
    infrared statement is now **exactly as hard as layer 1's small-field step plus standard large-field localisation**. That
    is the right place for it to sit.
  - (ii) NG-red is correct but its content is weak. "Not sign-symmetric" holds at every finite lattice for Wilson-type
    measures. The theorem's value is the volume- and K-uniform lower bound, and it does not touch non-Gaussianity.
  - (iii) Non-Gaussianity is not established even conditionally. (NG-conn) as worded is ill-posed.
- **Recommendation, in order.**
  1. Apply binding fixes 1-3 and 7. They correct a false claim, stale layer-1 status and the tally.
  2. Send layer 1 the n = 1 request with (M1) re-expressed as (CE-Q^∞)-localised and (M2) as (L-loc)_k.
     Do not frame (CE-loc) as the sole blocker.
  3. For non-Gaussianity: re-pose (NG-conn) in a named complete gauge (lasso logs), compute its tree-level value (it must be
     ≠ 0), and reuse NG-red's recursion. Do not pursue "every Gaussian connection" witnesses.
  4. Leave §12.1 unchanged. §20 is conditional on new, unadopted hypotheses.
