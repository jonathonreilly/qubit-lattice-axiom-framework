# REVIEW_X8: independent hostile review of session 8 of the YM4D existence lane (§17 and the [RX7-fix] changes)

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session8_snapshot.md (`cmp` empty).
  - `diff session7 session8` read in full (570 lines).
  - §17 (l.2894-3236) read in full by offset; §15.3 (H-sig^S) (l.2295-2298) and Lemma SIG-0 (l.2564-2583) re-read.
- LOG.md session 8 (l.428-516); REVIEW_X7.md (all).
- checks: x7_criteria.md, x7_toron_wc.py (read line by line), x7_out.txt, x7_time.txt.
- Read-only layer 1:
  - ../ym4d-proof/RLARGE.md v2 §0-§5.3 (l.1-486);
  - FLOW.md §4 (l.186-229), §7-§10 (l.408-476: F-flow, F-ll, F-tune, F-ind);
  - HIST.md §14.0-§14.2 (l.832-946) and §20.3 (l.1280-1381, including (C), the repaired (I_k^E)');
  - PROOF.md Setting CE and Theorem CE (l.1813-1882).
- No web access. Literature remarks below are the reviewer's own knowledge, marked [reviewer knowledge], and are
  not load-bearing.

Line numbers are EXISTENCE.md lines unless marked. No file other than this one was edited.

**Re-run conditions.** See (7).

**Bottom line.**
- **All 12 RX7 fixes are applied correctly** (one wording note on fix 11, cosmetic).
- **Lemma NT-0 is CORRECT.** It is an exact identity of the forward Markov chain (marginal = e^{-S_j}/Z by construction),
  and it is close to tautological. The re-aiming it licenses ((H-sig^S) at level j directly, with no (TRACK)) is right.
  - **One sub-claim is WRONG as stated:** "the leading connected cross-plane correlation is O(g_j⁴)". It holds only
    for observables with **contractible** support. A spatial Polyakov loop at fixed time is in 𝔄^S_{+,j} as defined
    (l.2933-2934). Its connected cross-plane correlation is **O(1)**, carried by the toron moduli.
- **Theorem NT-red (i)-(iii): CORRECT, with one definitional fix** (ν_s is not a conditioning on a set of U_j).
  - **(iv) is WRONG as an equivalence.** "liminf = 0 for every F" does not give a common subsequence, so it does not
    give a product limit point. Only one direction holds.
  - **NT-red is a reduction by strengthening.** (WC) is a two-point lower bound uniform over a class that contains every
    ν_s. So T21 is "decided" only under its second branch (the missing step is named).
- **(WC) is finite-dimensional, but not K-free as written.**
  - The class 𝔇_sf ranges over every depth k ≥ k_0 of the tower 𝓔_k, so (WC) carries a depth-uniformity requirement.
  - The suppression of non-flat small fields uniformly in depth needs the depth-uniform coercivity of 𝓔_k (HIST
    Corollary CLS-cone ⇐ (AE), OPEN). (WC) must list it.
- **The toron Laplace route (WC-tor) is plausible.** The Theorem-CE objection is right. "Massless" is the wrong
  word on a fixed torus; the real obstruction is the zero-mode/moduli set.
- **(SF-bg^tor) is correctly identified for the §14.1 form of (I_k^E), but it is stale.** HIST §20.3 (C), the repaired
  (I_k^E)', appeared during session 8 (HIST.md mtime 01:23 UTC).
  - In (I_k^E)', (a') defines the main term by an infimum (no (SF-bg) is needed to define it).
  - (b')'s gauge-covariant domain contains every flat configuration.
  - The gap therefore narrows to (a4) and (SF-∞) at toron backgrounds on **wrapping** charts and polymers.
- **K8: the conclusion is RIGHT, and the argument is incomplete.** The sign of 𝒱^{LF} matters. HIST-sum's own upper
  bound Z_K ≤ Z^{sf}e^{…} settles it against the literal reading (see (6)). K9: CORRECT.
- **x7: honest.** A PASS. B INCONCLUSIVE, recorded as such (4.5 and 4.1 SE against the pre-registered 5). The code was
  checked line by line. Re-run: (7).
- **Tally.** 50 / 1 / 3 / 5 / 12 stands. ARGUED is **25** (+1: the O(g⁴) order claim, restricted to contractible
  supports).
- **Strategic.**
  - (WC-tor) is a sound finite-volume problem. What it would deliver is non-triviality of the **small-volume**,
    perturbative finite-torus theory.
  - On a fixed torus there is a cheaper O(1) route (Polyakov loops through the moduli variance).
  - That route also shows that fixed-torus non-triviality carries almost no information about the infinite-volume
    question, which is (WC_∞).

---

## (1) RX7 fixes

| Fix | Where (session-8 lines) | Verdict |
|---|---|---|
| 1 c_* → 0; full mode sum; fixed-torus | l.2674-2679 | CONFIRMED |
| 2 "(a) EXCLUDED only when g_0²/σ² → 0"; σ ∝ g_0 counter-case | §0 l.107-112; l.2617-2621; l.2703-2708; T17 l.2857-2862; LOG l.397 | CONFIRMED |
| 3 free-model-only qualifier | §0 l.107-109; l.2711-2712; T17; LOG l.395 | CONFIRMED |
| 4 "free model:" prefix; SU(N) AF | l.686-687; l.2826-2827 | CONFIRMED |
| 5 proposed reading withdrawn; (W-F3) credited; LOG Next struck | l.2745-2759; LOG l.400, 424-425 | CONFIRMED |
| 6 RC: global continuity of X-S4c (i) cited; non-uniqueness | l.2727-2730 | CONFIRMED |
| 7 two-halves = ARGUED (analogy); ARGUED 20 | table l.2479; item 2 l.2809-2813; T20 l.2876-2878; l.689-690, 2889-2891; LOG l.406 | CONFIRMED |
| 8 TRACK fails in the example; SIG-RED lossy | l.2722-2724; l.2782-2785; §0 l.118-119 | CONFIRMED |
| 9 (H-sig^♭_ren): g_m fixed by F-tune | l.2792-2795 | CONFIRMED |
| 10 SEP "model-independently"; product-measure remark | l.2690-2691; l.2696-2699; l.2823-2824; §0 l.115-116 | CONFIRMED |
| 11 scope tags | l.2571; l.2628; §0 l.110 | CONFIRMED. Wording note: "CΩ iff liminf_j g_0(K_j) = 0" is true as "some limit point has H^S_ω = CΩ iff liminf = 0" (SIG-FREE (i) along the subsequence, (ii) otherwise). Add "for some limit point" (cosmetic). |
| 12 cosmetic l.1376, header | l.1410; l.15-16 | CONFIRMED |

**One related pre-existing overclaim** (§15.3, l.2296, unchanged since session 7): "(H-sig^S) … equivalently (Lemma
SIG-0) dim H^S_ω > 1 for every limit point". SIG-0 (ii) proves only ⇒. The converse is the same quantifier gap as
NT-red (iv) (see (3)). Fix: "equivalently" → "which implies".

---

## (2) Lemma NT-0 and the re-aiming (priority 2)

### The identity (l.2939-2946): CONFIRMED
- **Re-derived.** The joint law is W(U_0, …, U_K)/Z_K with W = e^{-S_0(U_0)}Π_{i<K}K_i(U_{i+1}, U_i) (RLARGE v2 §0, l.51-54).
  - Integrate U_K, U_{K-1}, …, U_{j+1} in that order. Each appears only in its own kernel's first argument, and
    ∫K_i dU_{i+1} = 1.
  - Then integrate U_0, …, U_{j-1}. By the defining recursion e^{-S_{k+1}(V)} = ∫K_k(V, U)e^{-S_k(U)}dU this leaves
    e^{-S_j(U_j)}.
  - Z_K = ∫e^{-S_k} is the same for every k by the same normalisation.
  - So yes: **the marginal law at level j is exactly e^{-S_j}/Z_K by construction.** No estimate is involved.
- **Conditions.**
  - S_j must be layer 1's effective action literally, i.e. -log of the marginal density. Layer 1 extracts only
    field-independent c-numbers (𝒱_k, 𝒱^{LF}) and re-parametrises u_k → u_k - δβ_k inside the representation. Neither
    changes the measure, so the identification holds.
  - θ-invariance needs Π_0 to be a block boundary at every level ≤ j ("one class, unshifted grids", l.2932), which is
    stated.
  - Gauge invariance: the kernels are gauge covariant (D4-norm).
- **Wording.** "At a fixed level" (l.2947) should read "at a fixed resolution m_* (level j = K - m_*)".
- **The consequence (l.2947-2951): CONFIRMED.** For F a function of U_j, Cov_{P_K} = Cov_{ν_{K,j}}. (TRACK) compared
  soft variables with a function of U_0 and has no role here. The re-aiming ((H-sig^S) at level j, not (H-sig^♭)) is
  right and useful.
- **Weight.** NT-0 is a one-line Markov-chain identity. Counted inside NT-red, it adds no weight.

### "Gauge invariance fixes the order" (l.2952-2956): CORRECT for contractible supports, WRONG as stated
- **The linear term vanishes (re-derived).**
  - Positive-side gauge averaging is legitimate: θ(F)^* does not see positive-side sites.
  - A gauge-invariant function, written in near-identity Lie coordinates after a local gauge, has a linear part that is
    an Ad-invariant linear form on ⊕su(N). Averaging over global Ad gives 0.
- **But 𝔄^S_{+,j} contains wrapping observables** (l.2933-2934: bounded continuous functions of links in the open
  positive half at positive distance).
  - Example: a spatial Polyakov loop P(t) = N⁻¹Re tr Π_{x_1}U_1 at a fixed time t > 0 lies inside the slice {t} × T³.
    That slice is at positive distance from Π_0 and from its antipode.
  - At a flat (toron) configuration, P(t) = P(-t) = N⁻¹Re tr h_1 for every t. This is not constant on the flat set.
  - So Cov(θP, P) ≈ Var_ν(N⁻¹Re tr h_1) + O(g²). This is **O(1)** whenever the moduli distribution of h_1 is not
    degenerate. In SU(2), by the centre symmetry, E tr h_1 = 0.
  - The O(g⁴) statement needs F to be supported in a **contractible** region. There a flat configuration is
    gauge-trivial, so F is constant on the flat set and its fluctuation is O(g²).
- **Fix (binding).** At l.2952-2956, l.3104 and LOG finding 2, add "for F supported in a contractible region (no
  torus-wrapping loops); wrapping observables (spatial Polyakov loops) have O(1) connected correlation through the toron
  moduli". "The O(g²) term exists only for abelian models" is true for the *linear* term only; say so.
- **Status.** That vanishing of the linear term leaves an O(g⁴) connected correlation with a non-zero coefficient is
  a perturbative (Laplace) statement, i.e. (WC)'s content. As written at l.2956 it is asserted as fact.
  - Label it ARGUED. ARGUED +1 = 25.

---

## (3) Theorem NT-red (priority 3)

### The statement and its uses
- **(ii) NT-LF (l.3010-3011, 3018-3020): CONFIRMED.**
  - The mixture identity Cov_ν = (1 - p)Cov_s + pCov_l + p(1 - p)(E_sA - E_lA)(E_sB - E_lB) is re-derived.
  - The bound is 6p||F||²_∞ (|Cov| ≤ ||F||², |ΔE| ≤ 2||F||).
  - θ-invariance is not needed for (ii).
- **(iii) NT-sec (l.3012-3013, 3020-3022): CONFIRMED.**
  - b∘θ = b, so ψ(b) = ψ(b)∘θ.
  - θ-invariance then gives E[θ(F)^*ψ(b)] = E[F^*ψ(b)], i.e. E[θF^* | b] = h^*.
  - Law of total covariance, with Var h ≥ 0.
  - It uses no RP of the conditional law. That matters, because b (holonomies) crosses the plane.
- **(i): CONFIRMED-WITH-FIX (definitional).**
  - **The problem.** ν_s := ν_{K,j}(· | 𝒮_j) (l.3022) treats 𝒮_j as a set of level-j configurations. But 𝒮_j (l.2971)
    contains "no large-field history". That is an event of the joint chain (U_0, …, U_j) (RLARGE v2 §5.1:
    𝔥 = (𝒰_0, …, 𝒰_{K-1})), not of U_j.
  - **What is correct.** Put A := {U_j small-field on every level-j cube} ∩ {𝔥_{≤j} = ∅}, an event of the joint chain.
    - ν_{K,j} = P_K(A)·law(U_j | A) + P_K(A^c)·law(U_j | A^c) is a mixture decomposition, so NT-LF applies with
      p = P_K(A^c).
    - law(U_j | A) has Haar density ∝ 1_{small}(U)·e^{-S_j(U)}|_∅. That is the trivial-history term of (I_j^E) (v2
      §4.1, l.385-387; returned defects are already resummed into E_j). So it is in 𝔇_sf.
    - θ- and gauge-invariance of A need the history construction (indicators, *-clustering, the R-operation's choices)
      to be reflection- and gauge-covariant. It is, by construction (B_4-covariant cubes, gauge-invariant indicators),
      but say so.
  - **Fix (binding).** Replace "ν_s := ν_{K,j}(· | 𝒮_j)" by "ν_s := law(U_j | A), A the joint-chain event above; its
    density is (O2)'s trivial-history term". Correct (O2) (l.2971-2973) in the same way: the display is e^{-S_j}|_∅,
    the history-∅ part of the marginal density, not e^{-S_j}.
  - **The arithmetic is checked.** Cov_{P_K} ≥ c_Wu_+^{-2} - 6δ_LF||F||² ≥ ½c_Wu_+^{-2}, and u_+^{-2} ≍ g⁴, so the
    condition is met for small g by δ_LF = o(g⁴).
- **(iv) NT-cpt (l.3014-3017, 3025-3030): WRONG as an equivalence; one direction CONFIRMED.**
  - **The quantifier gap.** "liminf_K Cov(F) = 0 for every F" does not give one subsequence along which all
    covariances vanish: each F may vanish along its own subsequence. The proof's "if every such covariance vanishes in
    the limit" silently assumes a common subsequence.
  - **What is true on the compact 𝒞_j.**
    - liminf_K Cov_K(F) = min over limit points ν of Cov_ν(F), since F is continuous.
    - Hence (H-sig^S) [∃F: liminf > 0] ⟺ ∃F with Cov_ν(F) > 0 at **every** limit point.
    - Its negation is "∀F ∃ν_F with Cov_{ν_F}(F) = 0". That does not produce one ν that is a product.
    - "No limit point is a product" ⟺ "dim H_ω > 1 for every limit point ω". This is the weaker statement.
  - **Fix (binding).** "(iv) (H-sig^S) at level j ⇒ no weak-* limit point of (ν_{K,j}) is a product across Π_0. 'dim H_ω
    > 1 for every limit point' ⟺ no limit point is a product. The converse to (H-sig^S) holds if (ν_{K,j}) converges
    (one limit point)."
  - The same change goes into LOG finding 3 ("failure ⟺ a product limit law") and into §15.3 l.2296 (see (1)).
- **"For every K" on the fixed torus (the claim at l.3008, l.3031-3033): CONFIRMED, conditionally.**
  - K enters only through:
    - membership ν_s ∈ 𝔇_sf (O1-O2 with K-uniform constants: FLOW F-tune's bracket is K- and torus-independent,
      FLOW l.427, 442-443; (I_k^E)'s constants are independent of g, k, K, T, HIST l.846);
    - p ≤ δ_LF (O3).
  - **Caveat: the depth index.** "(WC) contains no K" is literally true, but 𝔇_sf contains every depth k ≥ k_0 (see
    (4)). The K-uniformity has been moved into the class, not removed.
- **The orders (l.3104-3105): CONFIRMED with the contractible-support restriction of (2).** Leading term O(g_j⁴) for
  local gauge-invariant observables; remainder order not established.
  - [reviewer knowledge] Small-volume perturbation theory on periodic tori is known to have non-analytic expansions from
    the constant modes (Lüscher's small-volume effective Hamiltonian, Nucl. Phys. B219 (1983), gives expansions in
    g^{2/3} for energies). So "remainder relative o(1), order unknown" is the right level of claim.

### Is NT-red a real reduction? (T21)
- The pre-stated "Decided" criterion (l.2908-2910) has two branches:
  1. a proven implication from hypotheses none of which "is a K-uniform two-point lower bound";
  2. a precise statement of the missing step.
- **(WC) is a two-point lower bound, uniform over a class that contains ν_s for every K.** So NT-red does not meet
  branch 1. T21 is DECIDED under branch 2: the missing step is (WC), and the reasons are stated (not a CE expansion;
  toron moduli).
- **The proven content of NT-red** is:
  - the exact identification NT-0;
  - the removal of large fields at cost 6p||F||²;
  - the observation that the K-dependence can be packaged as a finitely-parametrised class.
- **Fix (binding).** At l.3206-3212 and LOG finding 3, add "NT-red meets T21's second branch only; (WC) is itself a
  class-uniform two-point lower bound containing every ν_s". The PROVEN-HERE count +1 is admissible (an implication is
  proven), but it is light.

### Physical regime (missing reading; binding)
- g ≤ g_W(𝕋, m_*) with g the coupling at the unit lattice of a fixed torus 𝕋 of T unit cells. g_W and c_W depend on 𝕋
  through F, c_*(T_{m_*}, t_b) ∝ T^{-4}-type constants, and the Laplace analysis.
- **So NT-red is a statement about the small-coupling, hence physically small-volume, finite-torus continuum limit**
  (box size ≪ Λ^{-1} unless g_W(T) decays no faster than (2β_0 log T)^{-1/2}; nothing here controls that).
- Add this at l.3006 and in §17.5 T23. It is the regime where weak-coupling Laplace analysis is natural, and where
  non-triviality is expected on perturbative grounds.

---

## (4) (WC), (WC-tor), Theorem CE (priority 4)

### Precision of (WC) (l.2997-3004)
- **Finite-dimensional: YES.** 𝒞_j = SU(N)^{links(Λ_j)} with Λ_j = T_0L^{m_*} × (TL^{m_*})³ is fixed and compact.
- **K-independent: NOT as written.** 𝔇_sf contains u𝓔_k for every depth k ≥ k_0, with 𝓔_k the depth-k tower (HIST §14.0)
  as a function on the fixed 𝒞_j. So (WC) is uniform over an infinite, depth-indexed family. That is K-uniformity in
  another form.
  - The deterministic tower is the only K-carrier, which is progress: no measure-theoretic UV limit is left.
  - But (WC) needs, uniformly in k:
    - **(a) the Hessian at the flat set.** At the trivial field this is PROVEN: HIST (c2), c_E||dB||² ≤ E_k ≤
      C_E(1 + κ)||dB||² uniformly in k and T, plus FLOW Lemma F-depth for convergence. At toron backgrounds it is not
      stated anywhere.
    - **(b) coercivity away from the flat set inside 𝒮_j.** 𝒮_j has a g-independent threshold ε_1. Configurations at
      distance ≫ g from the flat set but < ε_1 must be suppressed by u𝓔_k ≥ u·c·(distance)², uniformly in k. That is
      CLS-sf in cone form (HIST §20.3 (B), Corollary CLS-cone: CONDITIONAL ⇐ (AE), OPEN; RLARGE v2 row 9, weight P).
    - **(c) C³/C⁴ bounds of 𝓔_k near the flat set**, uniformly in k. For the transverse Laplace step and for the
      quartic zero-mode directions this is (SF-bg)-type analyticity. Locally that is FLOW §4 (SF-bg) / HIST (a4) via MSG.
- **Fix (binding).** Restate (WC) as "(WC) for the class 𝔇_sf, whose depth-uniform inputs are (a)-(c); (b) is
  CLS-cone ⇐ (AE) (layer 1, OPEN)". Replace "refers to no K" (l.3000) and "contains no K" (l.3032) by "contains no
  measure-theoretic UV limit; depth enters only through the deterministic towers 𝓔_k, k ≥ k_0".
- **Smaller precision items.**
  - In 𝔇_sf, 1_{𝒮_j} must be the U_j-local small-field indicator (see (3)).
  - t_b is not defined in (WC); point to SIG-FREE (ii).
  - "E obeying (O2)'s bounds" should list θ- and gauge-invariance of E (stated for ν, not for E).
- **Is (WC) plausibly true for the class?** YES at the level of orders.
  - E is O(1) per cube (HIST l.862-864: "bounded but NOT small") on a g-independent domain. By Cauchy estimates its
    quadratic part is O(1)·B² against u·B². Its linear part vanishes by gauge invariance at the flat set.
  - So E perturbs the transverse Gaussian at relative order g².
  - The class cannot be adversarial at small g except through the moduli directions, where u𝓔 vanishes and E (wrapping
    polymers) acts at O(1). That only reweights the sectors by a bounded density. NT-sec's sector-uniform bound is the
    right tool for it.

### Theorem CE does not apply (T22, l.3089-3103): CONFIRMED, one word to fix
- **Theorem CE is quoted correctly** (PROOF l.1873-1882): a product μ, |H(X)| ≤ H_0e^{-κd(X)}, κ > 3κ_0 + 3 ≈ 457,
  H_0 ≤ c_0(κ) ∝ e^{-2κ}.
- **Relative to Haar (a product), e^{-u𝓔} at small g is not a small activity.** This is RLARGE's own (SF-last) statement.
- **Relative to the Gaussian:** CE needs a product reference, and the correlated Gaussian e^{-uH_j} is not one. Its
  curvature covariance has power-law decay, far from κ > 457 in cube units.
- **Wording.** On a fixed finite torus "massless" is not itself the obstruction: decay is irrelevant in a fixed finite
  volume, and the transverse spectrum has a gap ≍ (2π/(TL^{m_*}))². The obstructions are:
  1. CE's hypotheses (product reference, κ > 457) are not met;
  2. the zero-mode/moduli set (constant modes, torons), where the action is quartic or vanishes.
  - Reword l.3095-3098 and l.3213-3214 accordingly.
- **What replaces it (finite-dimensional Laplace on a singular critical set): CORRECT.** T22 DECIDED.

### Toron moduli (l.3060-3085)
- **Facts: CONFIRMED.**
  - Flat lattice fields on a periodic torus are, up to gauge, constant commuting holonomies.
  - For SU(N), commuting tuples are simultaneously diagonalisable, so the moduli space is (T_max)⁴/W, connected, of
    dimension 4(N - 1).
  - Constant modes at the trivial connection have quartic action ([B_μ, B_ν]²).
  - The zero set of 𝓔_k is the skeleton image of the flat fine configurations.
- **Wording.** "Reducible points (e.g. the trivial connection)": every flat SU(N) connection on T⁴ is reducible
  (abelian). The singular points are those where the stabiliser jumps above the maximal torus (coincident eigenvalues;
  the trivial and centre-valued connections are the extreme cases). Reword l.3063-3064 and l.3070.
- **ARGUED "leading coefficient positive in every sector" (l.3075-3083): CONFIRMED as ARGUED.**
  - In a commuting background the Cartan fluctuations decouple and are untwisted, so they have the background-free c.
  - Every Wick term 2Cov(X_a, Y_b)² is ≥ 0.
  - The Var term of NT-sec is ≥ 0.
  - Near the singular points the non-commuting constant modes have size (uV)^{-1/4}. They shift the covariant Laplacian
    by a relative amount ≍ (uV)^{-1/4}·TL^{m_*} → 0 at fixed torus. Plausible.
  - Missing from the argument: uniformity in the depth k of the transverse Hessian **at toron backgrounds** ((a) above).
- **Is a Laplace analysis on the moduli a plausible route? YES.**
  - For one integral, ∫e^{-uf}φ over a compact real-analytic manifold with f ≥ 0 real-analytic has an asymptotic
    expansion in u^{-α}(log u)^β (resolution of singularities) [reviewer knowledge, standard].
  - So ratios of such integrals (covariances) have asymptotic expansions, and the leading coefficient is the ARGUED
    sector mixture.
  - The hard part is not existence of an expansion. It is a **lower bound uniform over the class** (E and k ≥ k_0) near
    the singular strata. Sector-conditioning (NT-sec) plus a transverse Gaussian comparison with quartic zero-mode
    control is the natural method.
- **Two alternatives the lane should weigh** [reviewer suggestions, ARGUED, not checked here]:
  1. **The O(1) route via wrapping observables** ((2) above).
     - With F = spatial Polyakov loop, NT-sec gives Cov(θF, F) ≥ E[Cov(θF, F | b)] + Var(E[F | b]).
     - E[F | b] = N⁻¹Re tr h_1 + O(g²).
     - Var(E[F | b]) is O(1) as soon as the moduli density under the class is bounded above and below relative to a
       fixed reference. That is plausible: the one-loop density times a bounded e^{±O(E_0)} reweighting from wrapping
       polymers.
     - E[Cov(· | b)] is O(g²).
     - Cost: the moduli density near the singular strata, at O(1) instead of a positivity statement at O(g⁴).
     - Price: it shows that fixed-torus dim H > 1 is carried by the toron zero modes, a finite-volume degree of freedom.
  2. **'t Hooft twisted spatial boundary conditions.**
     - [reviewer knowledge] For SU(N) with a spatial twist m ≠ 0 (twist in one spatial plane), the flat connections
       are finitely many, have centre-valued stabiliser, and are isolated. The moduli space disappears and (WC-tor)
       becomes a non-degenerate Laplace problem modulo gauge.
     - Time-reflection RP survives for purely spatial twists.
     - Cost: every layer-1 statement (RLARGE v2, HIST, FLOW (SF-∞)) is written for periodic tori. The twist is locally
       invisible, so only wrapping polymers change, but someone must check that.

---

## (5) (SF-bg^tor) (priority 5)

- **As stated (l.3071-3074), relative to HIST §14.1: CORRECT.**
  - FLOW §4 (SF-bg) (l.188-191) is stated "on a complex neighbourhood of the trivial field". (I_k^E)(a) (HIST l.849-851)
    defines 𝓔_{k,x} through it.
  - A toron is small-field everywhere but not globally near 1.
- **Stale (binding).** HIST §20.3 (C), (I_k^E)' (HIST l.1343-1381, written ≈ 01:23 UTC, after the lane's 01:19 read of
  HIST §14), changes this.
  - **(a')** 𝓔^Λ_k is defined by an infimum for every U (elementary fact (1)), with no (SF-bg) needed for the
    definition. On the whole torus it is 𝓔_k.
  - **(b')** The polydisc is defined by plaquette conditions and a Hermitian thickening, with no gauge chosen. Its real
    points include the whole ε_1-domain on every polymer, so they include every flat configuration (all plaquettes = 1).
  - **What remains.**
    - (a3)/(a4) at toron backgrounds. (a4) is ARGUED via MSG + local (SF-bg) on **bounded charts**. A toron is
      gauge-trivial on every contractible chart, so the local form covers it there.
    - **Wrapping** charts and polymers at levels near j, whose T_j-scale is finite on the fixed torus. There (SF-∞)
      ("wrapping polymers are bounded in the same norm", FLOW l.223-224) must hold at non-trivial holonomy.
- **Fix (binding).**
  - Re-cite (O2) as (I_j^E)' (HIST §20.3 (C)) at l.2970-2976, and delete "not yet written" (l.2971-2972).
  - Restate (SF-bg^tor) as "(I_j^E)' items (a3)-(a4) and (SF-∞) at flat non-trivial backgrounds on wrapping
    charts/polymers of the fixed torus; contractible charts are covered by the local form of (a4)".
  - "The global form of HIST's GAP S2-1" (l.3074) is superseded: (a') repairs S2-1. Report the narrowed item to layer 1
    instead.
- **Is it the right gap for layer 1? YES, narrowed.**
  - It is the only place where the fixed-torus setting asks of layer 1 something its infinite-volume constructions
    (Def F-g, (SF-∞)) do not already need.
  - It is shared with (WC)'s input (a) (the Hessian at toron backgrounds).

---

## (6) K8 and K9 (priority 6)

### K8 (l.3145-3165): conclusion CONFIRMED; argument to be completed (binding)
- **The derivation of P_K(E_all(k)) is checked.**
  - E_all(k) has n = N_k > n_♯, so it is unreturned.
  - Numerator: by v2 (RLF-3) per history (v2 l.183-185), times the restricted-sum factor (ARGUED, not in v2: correctly
    labelled).
  - Nesting: Σ_{k'≥k}|Ω^c_{k'}| ≤ N_k/(1 - L^{-4}) = (81/80)N_k at L = 3.
  - Denominator ≥ Z(∅).
- **The lane's reason is incomplete.** "Read literally, Z(∅)/Z^{sf} contains e^{𝒱^{LF}}, K-divergent, so the literal
  reading does not give (RLF-3^dis)" depends on the **sign** of 𝒱^{LF}. If 𝒱^{LF} → +∞, a lower bound Z(∅) ≥
  e^{-E_∅|T|}Z^{sf} would be easier, not harder. v2 bounds only |c̄_0^{sea}| (l.170-171).
- **The complete argument from v2's own lines.**
  - HIST-sum as quoted by v2 (l.469): Z(∅) ≤ Z_K ≤ Z^{sf}_K exp(C_H|T|e^{-(n_♯+1)a/g_K²}).
  - (RLF-1): Z_K = e^{𝒱^{LF}}Z^{ren}.
  - (RLF-4): Z^{ren} ≥ Z^{sf}e^{-C|T|e^{-a'/g_K²}}.
  - Together these give **𝒱^{LF} ≤ O(|T|) uniformly in K.**
  - So, under the literal reading, a K-divergent 𝒱^{LF} must diverge to -∞. Then Z(∅) ≤ Z_K ≪ Z^{sf}, and the needed
    Z(∅) ≥ e^{-E_∅|T|}Z^{sf} fails. Otherwise (𝒱^{LF} → +∞) the three v2 statements are mutually inconsistent.
  - Either way the literal reading does not deliver (RLF-3^dis). Under the Z^{ren}-decomposition reading,
    Z(∅) ≥ Z^{sf}(e^{-C|T|e^{-a'}} - (e^{C_H|T|e^{…}} - 1)) ≥ ½Z^{sf}, and E_∅ = log 2/|T| suffices.
  - Probabilities are ratios, and dividing every Z(𝔥) by the history-independent e^{𝒱^{LF}} changes none of them. So
    the question to v2 is exactly the lane's: which of Z(𝔥), e^{-𝒱^{LF}}Z(𝔥) obeys the (H-w) bound.
- **Fix (binding).** Replace the reason at l.3156-3159 and LOG finding 8 with the three-line argument above.
- **The same correction in (O3) (l.2987-2988).**
  - P_K(𝔥 ≠ ∅) ≤ Σ_{𝔥≠∅}Z(𝔥)/Z(∅) ≤ e^{E_∅|T|}(e^{C_H|T|e^{…}} - 1). Not "≤ e^{…} - 1", which needs Z(∅) ≥ Z^{sf}
    exactly.
  - The level sum in (O3) acquires e^{(n_♯+1)a_♯R} under (F_R) (v2 §5.2 [v2-F]).
  - Both are harmless at fixed |T|, so still o(g⁴).

### K9 (l.3167-3183): CONFIRMED
- v2 §0 (l.57-60) requires hypercubic tori for one shift. The electric/magnetic split under the time-preserving
  subgroup of B_4 is v2's own.
- NT-red on hypercubic T_0 = T even is consistent:
  - L odd keeps T_k even;
  - RP for the periodic reflection holds;
  - v2 is stated for every hypercubic T ≥ 3.
- ASSEMBLY (I)'s anisotropic setting consumes no RLF.
- (K9-req) is a correct, minimal request. The alternative (counterterms are infinite-volume numbers, anisotropy only at
  wrap levels) is what v2 (RLF-0) literally says ("infinite-volume numbers", l.169-170). It is the more likely answer.
- **Precision.** "Theorem NT-red needs nothing beyond v2" (l.3168) is about RLARGE. NT-red's (O2) is HIST's (I_j^E)'
  on a fixed torus, which has the (5) item. Add "(beyond the (SF-bg^tor) item for HIST)".
- **Cosmetic.** x7 itself uses 8×4³, which is not hypercubic. Harmless (x7 is non-load-bearing and Wilson-only). §17's
  subsection order is 17.6, 17.8, 17.6a, 17.7.

---

## (7) Check x7 and the re-run

- **Pre-registration order (local EDT mtimes).** criteria 21:20 < script 21:21 < out 21:34 < time 21:35. §17.0 is stamped
  01:19:39 UTC = 21:19 EDT. **Consistent.** The smoke run is disclosed, and the criteria were unchanged after it.
- **Code read line by line.**
  - **A.**
    - The symbol of d is correct.
    - Π_k is the projector onto range(d) via the pseudo-inverse.
    - The twisted momenta are k_μ = (2πn_μ + φ_μ)/T_μ, with the boundary phase restored. A1 compares with a dense
      twisted operator, and the wrap-phase correction is applied.
    - Λ normalisation: (1/(9V_s))Σ_yΣ_{o,o'} = (1/|S|²)ΣΣ by translation invariance.
    - The factor (Λ_0 + 2Λ_ch)/32 is re-derived. s ≈ |X|²/8 and Wick give (1/64)·2·Σ_{a,b}Cov², and the charged doublet
      contributes 2g⁴|Π^φ|².
    - The UB variance term: E[Φ | φ] = (g²/8)h(φ), so Var ≤ g⁴(range h)²/256.
  - **B.**
    - Kennedy-Pendleton heatbath, correct.
    - The quaternion product uses -a×b, i.e. the opposite algebra. It is used consistently (it represents U^† in
      standard convention), and plaquette real parts are unchanged.
    - Checkerboard by site parity per direction is valid.
    - Overrelaxation is in the same algebra.
    - Re-unitarisation every 50 sweeps.
    - Jackknife over 40 bins of 200 sweeps.
    - C(1) pairs adjacent time slices: the link-reflection pair, RP ≥ 0.
    - B0's ⟨s⟩β ≈ 0.754 against 3/4 (finite-volume zero modes) is a working sanity check.
- **A: PASS, honest.** One reading point: "the neutral part's sector independence is used, not tested" (l.3192-3193) is
  correctly disclosed.
- **B: INCONCLUSIVE, honestly recorded.**
  - The pre-registered rule needs C(1) > 5 SE at β = 16 and 32. The run has 4.5 and 4.1 SE. No FAIL clause holds.
  - z = -0.16 (β = 16) and -1.0 (β = 32) against 3.53e-6 are recomputed and agree.
  - The under-power estimate is consistent: (5/4.1)² ≈ 1.49.
  - Remark (not a finding against the lane): R decreases with β (4.87, 3.41, 2.83). Within errors this is consistent
    with a constant, but if it persisted it would point to a negative correction at small g, i.e. the non-analytic
    zero-mode sector. A better-powered B should also report R at β = 64.
  - d = 2: C(2)/g⁴ = 1.5e-6 ± 0.78e-6 at β = 16 against the leading 1.08e-7 (1.9 SE). Correctly called unresolved.
- **Load-bearing: none.** Stated so at l.3201-3203.
- **Re-run (reviewer, under the mandatory lock).**
  - Lock acquired 01:56:41 UTC after waiting for another holder; `rmdir` exactly once at 02:08:17 UTC, no trap.
  - nice 10; OMP/OpenBLAS/MKL/vecLib threads 1; `python3` without -I; no `timeout`.
  - Load 3.36 before and 3.30 after (< 8); 38% of memory free.
  - Output: scratchpad `rerun_x8/`.
  - **Result:** `x7_out.txt` is **identical** except the per-β and total wall times. Every number agrees digit for digit
    (fixed seeds), including:
    - A1 2.50e-16;
    - A3 LB 1.1770e-06 and UB 3.8559e-06;
    - R = 4.8743e-06, 3.4055e-06, 2.8304e-06 at 5.3, 4.5 and 4.1 SE;
    - "B0 PASS; B INCONCLUSIVE".
  - 696 s wall, 245 MB peak.

---

## (8) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| RX7 fixes 1-12 | CONFIRMED (fix 11 wording: "for some limit point") |
| §15.3 l.2296 "equivalently" | overclaim (pre-existing); "which implies" |
| Lemma NT-0 | CONFIRMED (exact Markov-chain identity; near-tautological) |
| "Leading term O(g⁴)" (l.2952-2956) | WRONG as stated; CORRECT for contractible supports; wrapping loops O(1); ARGUED |
| NT-red (ii) NT-LF, (iii) NT-sec | CONFIRMED |
| NT-red (i) | CONFIRMED-WITH-FIX (ν_s = law(U_j | A), A a joint-chain event; (O2) is e^{-S_j}|_∅) |
| NT-red (iv) NT-cpt | WRONG as an equivalence (quantifier); one direction CONFIRMED |
| NT-red as a reduction (T21) | DECIDED under branch 2 only; (WC) is a class-uniform two-point bound |
| NT-red regime | missing reading: small coupling at a fixed torus = small physical volume |
| Lemma NT-G | CONFIRMED (Gaussian part = free chain at constant u, noise 1/(κu); Wick factor ½(N² - 1)c²) |
| (WC) | finite-dimensional YES; K-free NO as written (depth-uniform inputs (a)-(c), incl. CLS-cone ⇐ (AE)) |
| T22 (CE not applicable) | CONFIRMED; "massless" → "zero-mode/moduli set; CE hypotheses unmet" |
| Toron facts; ARGUED sector positivity | CONFIRMED; "reducible" wording |
| (WC-tor) route | plausible; uniform lower bound near singular strata is the hard part |
| (SF-bg^tor) | CORRECT against §14.1; STALE against (I_k^E)' (HIST §20.3 (C)); narrow to wrapping charts/polymers |
| T23 | CONFIRMED (fixed torus conditional; (WC_∞) infrared) |
| T24 | CONFIRMED as ARGUED attribution; add that (WC) consumes CLS-cone ⇐ (AE) (layer-1 wall), so step (2) is not layer-1-free |
| K8 | conclusion CONFIRMED; argument completed by the sign (HIST-sum upper bound) |
| (O3) constants | e^{E_∅|T|} and e^{(n_♯+1)a_♯R} factors missing; harmless |
| K9 | CONFIRMED; "nothing beyond v2" is RLARGE-only |
| x7 A PASS, B INCONCLUSIVE | honest; code correct as read; re-run see (7) |

**Tally.**
- **Claimed:** PROVEN-HERE 50 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 12;
  ARGUED 24.
- **Corrected: 50 / 1 / 3 / 5 / 12; ARGUED 25.**
  - NT-red stays counted. Its counted content (i)-(iii) is correct after the ν_s fix. (iv) is reduced to its true
    direction and was never used by (i).
  - ARGUED +1: the O(g⁴) order claim for contractible supports. It was asserted as fact; it is a Laplace statement.
  - No HYPOTHESIS-NEW change. (WC) and (SF-bg^tor) are named parts of OPEN (H-sig^S), and OPEN stays 12.
- **Weight note.** The session's counted gain is one reduction whose non-trivial steps are elementary (NT-0, NT-LF,
  NT-sec). The substance is the identification of (WC) and of its inputs.

---

## Binding fixes for session 9

1. **Contractible support (l.2952-2956, l.3104, LOG finding 2).** Restrict "leading term O(g_j⁴)" to F with contractible
   support; add the Polyakov-loop O(1) counter-case. Say the abelian-only statement concerns the linear term. Label
   ARGUED. ARGUED 25.
2. **ν_s (l.3022-3023) and (O2) (l.2971-2973).** ν_s := law(U_j | A), A := {U_j all small-field} ∩ {𝔥_{≤j} = ∅}, a
   joint-chain event; (O2)'s display is e^{-S_j}|_∅. State the reflection/gauge covariance of the history construction.
3. **NT-cpt (iv).** Reduce to "(H-sig^S) ⇒ no product limit point; dim H_ω > 1 ∀ω ⟺ no product limit point; converse
   to (H-sig^S) if (ν_{K,j}) converges". Same at LOG finding 3 and §15.3 l.2296 ("equivalently" → "which implies").
4. **T21 reading (l.3206-3212).** "Decided under branch 2: (WC) is itself a two-point lower bound, uniform over a class
   containing every ν_s."
5. **(WC)'s depth inputs (l.2997-3004, l.3000, l.3032).** List (a) the depth-uniform Hessian at flat backgrounds (proven
   at 1 by HIST (c2); not at torons), (b) CLS-cone ⇐ (AE), (c) depth-uniform C³-C⁴ bounds. Replace "refers to/contains
   no K" by "no measure-theoretic UV limit; depth enters only through 𝓔_k, k ≥ k_0". Define t_b; list θ-/gauge-
   invariance of E.
6. **(I_j^E)' (l.2970-2976, l.3071-3074).** Re-cite HIST §20.3 (C). Delete "not yet written". Narrow (SF-bg^tor) to
   (a3)-(a4) + (SF-∞) at flat non-trivial backgrounds on wrapping charts/polymers. Drop "global form of GAP S2-1".
7. **K8 argument (l.3156-3159, LOG finding 8).** Use the sign argument: HIST-sum's Z_K ≤ Z^{sf}e^{…} with (RLF-1),
   (RLF-4) forces 𝒱^{LF} ≤ O(|T|); a K-divergent 𝒱^{LF} must then go to -∞, which defeats the lower bound.
8. **(O3) constants (l.2984-2988).** P(𝔥 ≠ ∅) ≤ e^{E_∅|T|}(e^{…} - 1); level sum × e^{(n_♯+1)a_♯R}.
9. **Physical regime (l.3006, §17.5 T23).** g ≤ g_W(𝕋) at a fixed torus is the small-volume regime; say so.
10. **T22 wording (l.3095-3098, l.3213-3214).** "Massless" → "CE's product/decay hypotheses unmet; zero-mode/moduli set".
    "Reducible points" → "singular strata (stabiliser larger than the maximal torus)".
11. **T24 (l.3129-3131).** Add that (WC) consumes CLS-cone ⇐ (AE). So step (2) is finite-dimensional but not independent
    of a layer-1 wall.
12. **Cosmetic.** l.2947 "fixed level" → "fixed resolution"; K9 "nothing beyond v2 (RLARGE)"; subsection order 17.6a/17.8;
    fix 11 "for some limit point".

---

## Strategic verdict on (WC-tor)

- **What session 8 established (correctly).**
  - The soft variables at fixed resolution are the effective-action field (NT-0). So non-triviality is a statement
    about layer 1's output law, with no soft-variable tracking.
  - Given layer 1's representation, large fields cost o(g⁴).
  - What remains on a fixed torus is a finite-dimensional, weak-coupling, sector-uniform lower bound. That is a
    well-posed and plausible problem, and Theorem CE is the wrong tool for it.
- **What (WC-tor) would and would not deliver.**
  - It would give dim H^S_ω > 1 for the finite-torus continuum limit at small coupling, i.e. in a physically small box.
    That is the regime where non-triviality is expected from perturbation theory.
  - On a fixed torus non-triviality is also obtainable at O(1) from wrapping observables through the toron moduli
    ((4), alternative 1). That is a sign that fixed-torus dim H > 1 is a weak statement: the zero-mode sector of a finite
    box carries it.
  - Neither version bears on non-triviality in infinite volume or at time side → ∞. That is (WC_∞), the infrared
    problem shared with the mass gap.
- **The (WC) step is not layer-1-free.** Depth-uniform coercivity of 𝓔_k (CLS-cone ⇐ (AE), layer 1's own P-weight wall)
  is an input, and so is the toron-background Hessian.
- **Recommendation, in order.**
  1. Apply the binding fixes. They are all wording or quantifier repairs except 5-6, which re-state the inputs.
  2. **If** a fixed-torus non-triviality theorem is wanted as a milestone, choose deliberately among:
     - (WC-tor) with local observables (the lane's plan; hardest at the singular strata);
     - the Polyakov-loop O(1) route (cheapest; needs the moduli density two-sidedly);
     - 't Hooft-twisted spatial boundary conditions (no moduli; needs layer-1 statements on twisted tori).
     Record in each case that the result is small-volume.
  3. Do not count further fixed-torus results as progress toward the continuum non-triviality that ASSEMBLY (I) needs.
     The decisive open item for that is (WC_∞), which should be stated precisely next, in the X-OS setting of ASSEMBLY (I).
  4. A better-powered x7 B (≥ 2× samples, β up to 64, criteria re-registered) only if B is to count. It cannot test
     (WC)'s uniformity in any case.
