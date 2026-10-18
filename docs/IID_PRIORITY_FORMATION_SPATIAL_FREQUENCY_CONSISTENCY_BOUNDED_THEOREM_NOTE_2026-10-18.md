---
claim_id: iid_priority_formation_spatial_frequency_consistency_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Formation reading of Definition 1 of the coding-radius note with an empty start slice and a translation-covariant rule of range one on Z^3. Supplied premises: iid atomless activation times, iid per-site marks, a measurable rule. For any local pattern E (a finite support S and a measurable set of Record configurations on S) with probability p, and any deterministic sequence of distinct sites: (A) the empirical frequency F_n has E F_n = p and Var F_n <= chi_E/n, where chi_E = sum_z |Cov(1_E, 1_{E+z})| is finite and explicitly bounded. Under pairwise l1-separation s the bound improves to (p(1-p)+tau_E(s))/n, with tau_E(s) decaying factorially. (B) P(|F_n - p| >= eps) <= 3 exp(-n eps^2/(8 k_m)) whenever |S| c_m/(m+1)! <= eps/4, where k_m = |B_1(0, 2m+diam S)|. (C) For a context C with P(C) = q > 0, the conditional frequency N_n(E and C)/N_n(C) tends to P(E|C) almost surely, in every L^r with r finite, with Chebyshev tail 16(chi_{E and C}+chi_C)/(n q^2 eps^2) and an exponential tail with constant 6 (m and k_m taken for S union S_c, with delta_m <= q eps/16). The limits are the formation law's own probabilities. For strictly positive order-blind rules they equal the rule weights r(a|eta) given Record neighbour contexts. For order-sensitive rules they do not in general (witness: ferro (20,1,1)). For own-mark race rules (marks independent of the clock at the same site) the rule weight is recovered given the formation-time context, a pattern of (X,T). This is a partial, conditional discharge of the 2026-09-02 frequency-consistency obligation: a spatial site-sampling notion within one realisation, not repeated trials of one experiment; the 2026-09-02 dependency row stays supplied. Nothing identifies these probabilities with Born weights, and nothing here covers repeated readout of one Record."
upstream_dependencies:
  - iid_priority_formation_is_a_finitary_factor_of_iid_noise_with_factorial_coding_radius_tail_bounded_theorem_note_2026-10-18
  - order_blind_positive_formation_is_a_one_dependent_gibbs_field_bounded_theorem_note_2026-10-16
  - finite_action_functional_typed_admissibility_record_identification_decision_bounded_theorem_note_2026-09-02
runner: scripts/iid_priority_formation_spatial_frequency_consistency_2026_10_18.py
---

# Spatial frequency consistency for iid-priority formation fields

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Complete proofs under the stated hypotheses, with Monte Carlo checks; independently checked by a same-model-family agent (corrections applied). Rests on the companion coding-radius note. Nothing is adopted.
**Provenance:** drafted by a worker agent of the same model family as the campaign.

## 0. Result up front

Take the formation class of the coding-radius note with an empty start and a translation-covariant rule. Choose any local Record pattern, optionally conditioned on a local context of positive probability. Its empirical frequency along **any** deterministic sequence of distinct sites converges to its probability under the formation law. The convergence holds almost surely and in L², with variance at most χ/n and an exponential tail bound with explicit constants. This is a **partial and conditional discharge** of the frequency-consistency obligation in the 2026-09-02 decision note. That note's missing premise concerns repeated trials of one conditional experiment. This theorem gives a different frequency notion: spatial site-sampling within one formation realisation. Its limits are the formation law's own probabilities, which equal the one-use weights given Record contexts only for order-blind positive rules. Independence is relocated to the supplied microscopic noise (iid clocks and marks, empty start, one fixed rule), not derived. The 2026-09-02 dependency row therefore stays "supplied".

It does **not** say that these probabilities are Born weights. It does not cover sequential readouts of one Record. For order-sensitive rules it does not say that frequencies conditioned on neighbouring Records equal the rule's weights; they demonstrably do not.

## 1. What the repo's obligation actually is

Source: `docs/FINITE_ACTION_FUNCTIONAL_TYPED_ADMISSIBILITY_RECORD_IDENTIFICATION_DECISION_BOUNDED_THEOREM_NOTE_2026-09-02.md`, "What can actually be observed" and §8.

- **Which frequencies.** The empirical frequency F_m = (1/m) Σ_i X_i, where X_i is the indicator of a fixed event (one Record content a) in trial i.
- **Same conditions.** Every trial has the same neighbouring condition η, preparation, registered instrument and cadence. The note says that probabilities "can be inferred from repeated Record contents only under a supplied protocol … with a joint sampling law that justifies consistency."
- **Sampling order.** This is the trial index i. Neither the note nor the six premises of §8 fix a temporal, spatial or other order.
- **Status.** The six premises do not imply consistent frequencies. The note gives two sufficient extra premises:
  - (a) an IID product protocol: fresh carrier or non-erasing reset, independent draws, Var F_m = p(1−p)/m;
  - (b) "a separately supplied stationary ergodic joint process … almost-sure consistency by the ergodic theorem; no physical ergodicity or reset implementation is derived here."

  The dependency table lists "frequency consistency | additional IID/reset or stated ergodic joint law".
- **"Stationarity insufficient".** Draw a single B ~ Bernoulli(1/4) and set X_i = B for all i. Every trial has the correct one-use marginal, yet F_m = B and Var F_m = 3/16 for every m. At m = 4 this is 3/16 against the IID value 3/64, and the runner reproduces those numbers.

  The law is stationary and exchangeable but **not ergodic**: the shift-invariant event {X_1 = 1} has probability 1/4. It is not mixing, since Cov(X_i, X_j) = 3/16 for all i ≠ j, and its covariances are not summable. It is a mixture of two ergodic laws, the point masses at all-0 and all-1. The repo already concedes that ergodicity would suffice for almost-sure convergence. So the counterexample defeats only stationarity, and **it is excluded by the hypotheses below**, which give summable covariances. Compare the repo's 2026-06-06 firewalls (RECORD_IID_TYPICALITY, POST_RECORD_EXPECTATION_CONCENTRATION): they make the same point with perfectly correlated laws.

## 2. Setting

The setting is Definition 1 of the coding-radius note with G = Z³ (nearest-neighbour, D = 6) and an empty start slice B = ∅. The supplied premises are:

- activation times T_y, iid and atomless;
- marks U_y, iid;
- a measurable rule F with F_{y+v}∘θ_v = F_y.

X = (X_y) is the Record field, with values in a standard Borel space 𝒜. Write c_n for the number of n-step self-avoiding walks (OEIS A001412), so that c_n ≤ 6·5^(n−1).

Further definitions:

- **Pattern.** A pattern E = (S, P) has finite support S ⊂ Z³ and measurable P ⊂ 𝒜^S. Write E_x = {X_{S+x} ∈ P}, I_x = 1_{E_x} and p = P(E_0). By covariance, P(E_x) = p for every x.
- **Covariance function.** C_E(z) = Cov(I_0, I_z). Then χ_E := Σ_z |C_E(z)| and τ_E(s) := Σ_{|z|₁ ≥ s} |C_E(z)|.
- **Sampling sequence.** x_1, x_2, … is a deterministic sequence of **distinct** sites, fixed without reference to ω. The frequency is F_n = (1/n) Σ_{i≤n} I_{x_i}.

Everything below also holds for patterns of the joint field (X_y, T_y), because T_y is part of the noise on K_y. This is used in §5(ii).

## 3. Theorems

**Lemma 0 (summable covariances).** χ_E < ∞. Explicitly,

  |C_E(z)| ≤ min{ p(1−p), ½ Σ_{y∈S, y′∈S+z} Γ(d(y,y′)), |S|·c_m/(m+1)! },   where m = ⌊(d(S, S+z) − 1)/2⌋ ≥ 1 (the ball term needs d(S, S+z) ≥ 3; below that only p(1−p) applies),

and the terms decay like exp(−d ln d + O(d)). For |S| = 1 this gives χ_E ≤ 4069 (runner X3). The bound is rigorous but loose: the measured χ̂ is 1.70 for ferro (20,1,1) and 0.29 for copy-unanimous.

*Proof.* Apply the coding-radius note's Theorems 2 and 2′ with osc 1_E = 1. Add Cauchy–Schwarz, |Cov| ≤ √(Var I_0 · Var I_z) = p(1−p). There are O(d²) sites z at each ℓ¹ distance (4d²+2 when |S| = 1). ∎

**Theorem A (L² law; arbitrary site sequences).** Under the hypotheses of §2, E F_n = p and

  Var F_n ≤ χ_E / n.

If moreover |x_i − x_j|₁ ≥ s for all i ≠ j, then

  Var F_n ≤ (p(1−p) + τ_E(s)) / n.

So well-separated sampling ("fresh carriers") reproduces the repo's IID variance p(1−p)/m, up to a factorially small τ_E(s). Consequently P(|F_n − p| ≥ ε) ≤ χ_E/(nε²), and F_n → p almost surely.

*Proof.* Expand Var(Σ_i I_{x_i}) = Σ_{i,j} C_E(x_j − x_i). The sites are distinct, so for each fixed i the map j ↦ x_j − x_i is injective, and Σ_j |C_E(x_j − x_i)| ≤ χ_E. Under separation, the j ≠ i terms use only |z| ≥ s.

For the almost-sure statement, Chebyshev along n = k² gives Σ_k χ_E/(k²ε²) < ∞, so Borel–Cantelli yields F_{k²} → p almost surely. For k² ≤ n < (k+1)², the indicators lie in [0,1], so |F_n − F_{k²}| ≤ 2(2k+1)/k² → 0. ∎

**Theorem B (exponential concentration).** Let ε ∈ (0,1] and choose m ≥ 1 with δ_m := |S|·c_m/(m+1)! ≤ ε/4. Put k_m := |B₁(0, 2m + diam₁ S)| = 1 + Σ_{d=1}^{2m+diam S} (4d²+2). Then, for every n and every sequence of distinct sites,

  P(|F_n − p| ≥ ε) ≤ 3 exp(−n ε² / (8 k_m)).

In particular Σ_n P(·) < ∞, which gives almost-sure convergence directly. The constant m(ε) is O(log(1/ε)/log log(1/ε)), so the rate is ε²/polylog(1/ε). With |S| = 1 and ε = 0.05, m = 14, k_m = 30913, and the bound is 3·exp(−n/9.9·10⁷) (runner X).

*Proof.*

1. **Local copies.** Put W_x := ∪_{y∈S+x} B(y, m). Take independent copies ω′^{(x)} of the noise and set ω̂^{(x)} := ω on W_x and ω′^{(x)} off it. By the coding-radius note's Lemma 3, with a deterministic set, ω̂^{(x)} has the law of ω. Hence I^{(m)}_x := 1{X_{S+x}(ω̂^{(x)}) ∈ P} satisfies E I^{(m)}_x = p.
2. **Bad sites.** Put bad_x := 1{∃ y ∈ S+x : L_y ≥ m}, where L_y is the longest decreasing path from y. A decreasing path of length m lies in B(y, m), so bad_x is a function of the times on W_x. By the coding-radius note's Lemma 1, E bad_x ≤ δ_m.
3. **Agreement off bad sites.** On {bad_x = 0}, K_y ⊂ B(y, L_y+1) ⊂ B(y, m) ⊂ W_x for every y ∈ S+x. the coding-radius note's Lemma 2(iii) then gives X_{S+x}(ω̂^{(x)}) = X_{S+x}(ω), so |I_x − I^{(m)}_x| ≤ bad_x.
4. **Decomposition.** Let F^{(m)}_n and B_n be the averages of I^{(m)}_{x_i} and bad_{x_i}. Then |F_n − p| ≤ |F^{(m)}_n − p| + (B_n − E B_n) + δ_m.
5. **Colouring.** Both families are functions of (ω|_{W_x}, ω′^{(x)}). Members whose sets W_x are pairwise disjoint are therefore independent. W_x ∩ W_{x′} ≠ ∅ forces x′ − x ∈ B₁(0, 2m + diam S). So the dependency graph has maximum degree below k_m, and a greedy colouring uses at most k_m classes, each consisting of independent [0,1]-valued variables.
6. **Hoeffding on each class.** Generalised Hölder over the k colour classes plus Hoeffding's lemma give E e^{λ(Σ − EΣ)} ≤ e^{kλ²n/8}. Hence P(Σ − EΣ ≥ nη) ≤ e^{−2nη²/k}. This is Janson's (2004) inequality with the chromatic number in place of the fractional one.
7. **Conclusion.** Apply step 6 with η = ε/2 to F^{(m)}, two-sided, and with η = ε/4 to B_n. Since δ_m ≤ ε/4, the total is 2e^{−nε²/(2k)} + e^{−nε²/(8k)} ≤ 3e^{−nε²/(8k)}. ∎

**Theorem C (conditional frequencies).** Let C = (S_c, Q) be a context with q := P(C_0) > 0, and E a target pattern. Write N_n(·) for counts along the sequence and set F_n(E|C) := N_n(E∩C)/N_n(C), with 0/0 := 0. Then F_n(E|C) → P(E|C) almost surely and in every L^r with r < ∞. For 0 < ε ≤ 2:

  P(|F_n(E|C) − P(E|C)| ≥ ε) ≤ 16(χ_{E∩C} + χ_C)/(n q² ε²),

and an exponential tail holds: apply Theorem B with ε replaced by qε/4 to both patterns E∩C and C, with m and k_m computed for |S ∪ S_c| and diam(S ∪ S_c) and m chosen so that δ_m ≤ qε/16. The combined constant is 6 (not 3). Any fixed q > 0 suffices; the constants degrade as q⁻².

*Proof.* Put a = N_n(E∩C)/n, b = N_n(C)/n, r = P(E∩C) ≤ q and η = qε/4 ≤ q/2. If |a − r| < η and |b − q| < η, then b > q/2 and

  |a/b − r/q| ≤ |a − r|/b + r|q − b|/(bq) < 2η/q + 2η/q = ε.

So the bad event is contained in {|a − r| ≥ η} ∪ {|b − q| ≥ η}. Apply Theorem A to each. Almost-sure convergence follows from Theorem A applied to the numerator and denominator. Since |F_n(E|C)| ≤ 1, L^r convergence follows by bounded convergence. ∎

**Remark (non-covariant rules or B ≠ ∅).** the coding-radius note's Theorem 2 does not use translation invariance. Theorem A's variance bound therefore holds with χ := sup_x Σ_z |Cov(I_x, I_{x+z})|, and gives F_n − E F_n → 0. The frequency then tracks the average probability instead of a constant.

**Remark (what mixing alone gives).** For any stationary mixing field, C(z) → 0 gives Var F_n ≤ |B(R)|/n + sup_{|z|>R} |C(z)| → 0 along any sequence of distinct sites. That is L² consistency without a rate. Ergodicity alone gives almost-sure convergence of Følner box averages. The coding-radius class gives more: rates, and almost-sure convergence along arbitrary sequences. Any non-ergodic stationary law has box frequencies converging to the random limit P(E | invariant σ-field). This is exactly the failure in the repo's counterexample, where the limit is B itself.

## 4. Which probabilities are the limits

(i) **Order-blind strictly positive rules (2026-10-16 class).** The empty-start formation law restricted to any window W has the induced-subgraph product law of 2026-10-16 Theorem 1, for the following reasons:

- Formation on a finite box Λ is formation of the window Λ, so its marginal on W is that product form for every order.
- On {K_W ⊂ Λ}, the box and infinite-volume formations agree, by the coding-radius note's Lemma 2 applied to the box graph.
- P(K_W ⊄ Λ_N) → 0.

The six neighbours of a site are pairwise non-adjacent. So for any partial neighbour context η, P(X_0 = a | X_{neighbours} = η) = r(a|η), by product-form normalisation. **Spatial conditional frequencies given Record contexts converge to the rule weights.** The runner checks this exactly for the soldered chiral-pair rule (O2).

(ii) **Order-sensitive rules.** The limit is P_form(a | final Record context), which is generally not r(a|η).

- **Witness.** For ferro (20,1,1), freq(X_0 = 0 | X_{+x} = 0) = 0.5125 ± 0.0009, against the rule weight 0.8 (runner F4, z ≈ −306).
- **Own-mark rules.** These are rules that read marks only at their own site, such as the race. For them, X_0 = F(η_form, U_0), where U_0 is independent of the formation-time context. This needs U_0 independent of the clock T_0 at the same site; the race satisfies it, while Definition 1 of the coding-radius note also allows dependence within a site. That context is the set of earlier-formed neighbours and their Records, which do not depend on U_0. So the rule weight **is** the limiting frequency given the formation-time context, a local pattern of (X, T): 0.8043 ± 0.0034 against 0.8 (runner F3).
- **Caveat.** This requires the formation order to be readable. The repo's observation clause reads Records only.

(iii) **Born weights.** None of these limits is identified with Tr(ρE). That needs the 2026-09-02 premises: a complete action/state package, a registered effect partition, the identification (10) of action weights with the Admissibility law, and a matching-output instrument. They remain supplied or open.

## 5. Relation to the obligation, and what is not given

**What it gives.** Inside the formation model, trials can be read as distinct sites sharing a local context. The "joint sampling law" is then the formation law itself, not an extra product or reset postulate. Consistency follows with rate 1/n in L², a Chebyshev bound and an exponential bound. Well-separated sites reproduce the IID variance p(1−p)/m up to τ(s). The "stationarity insufficient" counterexample is non-ergodic and has non-summable covariance, so it lies outside the hypotheses. The theorem addresses it fully for this class.

**What it does not give.**

1. **No Born identification** (§4(iii)). Frequency equals probability only for the formation law's own probabilities.
2. **No sequential readouts of one Record.** A permanent Record read m times gives X_i = X_0 for all i. This is *exactly* the repo's perfectly correlated counterexample, with F_m = X_0. Consistency needs distinct carriers (sites), not repetition. A temporal-trial reading (reset, cadence, a re-prepared carrier) is not modelled.
3. **The premises stay supplied.** The independence has moved, not disappeared: iid clocks, iid marks, an empty start slice, and one fixed, non-random, covariant rule are all supplied. A rule or parameter drawn once makes a stationary non-ergodic mixture. The runner's R1 check gives a bimodal frequency, with a between-torus SD of 0.135 against 0.003 within a rule. A random correlated start slice and global conditioning also leave the class (coding-radius note §7).
4. **Deterministic sequences only.** An adaptive selection that peeks at the target (for example "sample sites where X = 1") is not covered. Selection by a local context is covered, through Theorem C.
5. **Matching the context to the repo's "same condition" is a modelling choice.** The note's η also covers preparation, registration and cadence; only the neighbour-Record part is modelled here.
6. **The constants are loose.** χ ≤ 4069 against measured values of 0.14 to 1.7.

## 6. Runner evidence (finite Monte Carlo, not proof)

Command: `python3 scripts/iid_priority_formation_spatial_frequency_consistency_2026_10_18.py` (seed 20261018). Result: **TOTAL PASS=17 FAIL=0** in 62 s. The simulation code is adapted, read-only, from the coding-radius runner, and the formation loop is rewritten to pass neighbour directions and record formation-time masks.

- **X.**
  - Exact repo counterexample numbers: 3/16 against 3/64, and non-summable covariance.
  - Rigorous χ ≤ 4069.
  - Theorem B parameters.
- **O. Chiral-pair order-blind rule**, 300 tori with L = 24. The expected constants come from the 2026-10-16 product formula and are computed separately from the simulation.
  - Class frequencies equal 1/12 within |z| ≤ 1.3.
  - Conditional frequencies given one or two neighbour Records match r(a|η) ∈ {1/8, 1/24, 1/12} within |z| ≤ 1.3.
  - n·Var of box means of h = X_{+x} + X_{−x} equals the exact 1/3 + (l−1)/(36l) for l = 1, 2, 4, 8, 11, within |z| ≤ 1.4. The replicas are exactly independent by 1-dependence.
  - Along a fixed scrambled sequence of distinct sites, chosen before any field was drawn, n·Var F_n matches the exact set-dependent prediction 1/3 + 2·#bonds/(72n) at n = 50, 500, 5000 and 13824.
- **F. Ferro (20,1,1)**, order-sensitive, 120 tori with L = 32.
  - Label frequency 1/6 (z = 0.17).
  - n·Var(F_l) rises from 0.139 to 1.40 by l = 12 and stays at or below χ̂ = 1.70. It matches Σ_z C(z)·(overlap weight). This is a same-data identity, a consistency check rather than an independent one.
  - Checks F3 and F4 as in §4(ii).
- **C. Copy-unanimous** (has zeros, order-sensitive): frequency 1/6 and the same two variance checks.
- **R. Rule mixture:** non-concentration, as in §5.3.

**Disclosure.** A plateau check (n·Var at the two largest l agreeing within 4 SE) was in the first version. It was removed after the quick run, before the full run, because it is not a valid test of O(1/n) scaling: finite-size growth toward χ is expected. The check counts above exclude it. No threshold was changed after the full run.

## Independent check

A fresh-context agent of the same model family checked the draft; it is not an independent human reviewer. It re-derived every proof by hand and wrote a new simulation, which passed 10/10 on 400 tori of size 24³ with the ferro rule. Files: `.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_check/`.

- **Confirmed:** Lemma 0, Theorem A and Theorem B.
- **Confirmed with corrections, now applied:**
  - Theorem C's exponential constant and support.
  - The own-mark independence condition.
  - The headline reading of the 2026-09-02 obligation, which is now a partial and conditional discharge.
- **Monte Carlo agreement:** a Record-context frequency of 0.5115 against 0.5125, and a formation-time-context frequency of 0.8004 against 0.80.

## 7. Prior art and contribution

**Standard.** The following are textbook results:

- Chebyshev's bound and the strong law for bounded variables with summable covariances (the subsequence argument);
- Hoeffding's inequality for dependency-graph sums (Janson, Random Structures Algorithms 24, 2004; recalled, not re-checked);
- the ergodic decomposition and the multidimensional ergodic theorem;
- for a factor of an iid process on an amenable group, Bernoullicity (Ornstein–Weiss); this is recalled and not used.

**New here (packaging).**

- The exact frequency obligation of the 2026-09-02 note is located, and its counterexample classified as non-ergodic and non-summable.
- The obligation is discharged for the coding-radius formation class, along arbitrary distinct-site sequences and with explicit Z³ constants.
- Separated sampling is shown to reproduce the IID variance.
- The limits are identified: rule weights for the order-blind class; not rule weights for order-sensitive rules given Record contexts (a witness is given); rule weights given the formation-time context.
- One-Record repetition is shown to be precisely the repo's counterexample.

## 8. No-Go discipline

Only one negative statement is made: that one-Record repetition and non-ergodic mixtures fail. It is shown by exact example, not by an impossibility theorem. Nothing is claimed about the framework outside the stated class. All premises are named in §2 and §5.3.


## Verification

```bash
python3 scripts/iid_priority_formation_spatial_frequency_consistency_2026_10_18.py
```

Expected: `TOTAL PASS=17 FAIL=0` (about one minute).

## Load-bearing sources

- [Coding-radius note](IID_PRIORITY_FORMATION_IS_A_FINITARY_FACTOR_OF_IID_NOISE_WITH_FACTORIAL_CODING_RADIUS_TAIL_BOUNDED_THEOREM_NOTE_2026-10-18.md)
- [Record-identification decision note](FINITE_ACTION_FUNCTIONAL_TYPED_ADMISSIBILITY_RECORD_IDENTIFICATION_DECISION_BOUNDED_THEOREM_NOTE_2026-09-02.md)
