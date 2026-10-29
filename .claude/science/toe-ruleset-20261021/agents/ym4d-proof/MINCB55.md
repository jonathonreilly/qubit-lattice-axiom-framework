Reviewer model: claude-opus-5-5

# MINCB55 — the minimizing-background consumers (Codex ASSEMBLY work-list item 8)

## 0. PRE-STATED (written 2026-10-29T05:02:17Z, before any derivation; statements only)

Worker: Opus 5.5 (exact ID above), task brief `scratchpad/queue/mincb.md`, shared rules REVIEW_BRIEF_55.md.
Deliverables: this file and `checks/mc55_*` only. No git.

Targets.
- (T1) Consumer census. For every consumer that reads the GLOBAL-MINIMUM background tower (HIST's 𝓔_k,
  FLOW's 𝒯_k "Def F-strip", PROOF's E_1^NA, the φ-tower) on k-, T-uniform local domains — at least FLOW's
  (SF-bg)/(SF-g), HIST's main term (I_k^E)″, PLD's 𝔟(V) (ASSEMBLY55 C5b) — decide, from the consumer's own
  text located by string, which property of the background it actually uses: (a) global minimality
  (a comparison against configurations OFF the small-field chart), (b) only criticality on the chart plus a
  lower bound off it, or (c) only criticality.
- (T2) Either (MIN-cb): for real small-field data every global minimiser of the chain energy lies, modulo
  composite gauge, in BFT-E's fixed slice ball, uniformly in k, T and locally; or the alternative: (i) the
  critical-value restatement of each consumer, (ii) the restricted small-field minimum (the critical value
  is the minimum over the small-field chart), (iii) the large-field comparison (energy off the chart exceeds
  the chart minimum by a definite amount), each k-, T-uniform with every input named with its status.
- (T3) The CODEX_REVIEW_BFT4B bridge: are the global critical-value polymers the localised-minimiser
  densities that (I_k^E)″ uses? Settle it, or say exactly what is missing.

What would count as a refutation (of a claim in the existing record, or of my own route).
- Of (MIN-cb): a real small-field datum, at some k or T, whose global minimiser is not gauge-equivalent to a
  point of the slice ball (or whose minimum is not attained there), or an argument that the infimum of the
  chain energy over configurations off the chart is at or below the chart value for some admissible datum
  (e.g. non-trivial flat/toron sectors, Gribov copies, or block-constraint-compatible large-field
  configurations with comparable energy).
- Of the alternative route: a consumer whose load-bearing step genuinely compares against configurations
  off the chart (then a critical value is not enough); a small-field datum where the chart critical point is
  not the chart minimum (Hessian/convexity failure on the chart); or a large-field comparison constant that
  is not k-, T-uniform or is evaluated at a stale constant.
- Of (T3): an explicit mismatch between the global critical-value polymer activity and the localised
  minimiser density on some admissible datum, or a dependence of one on data outside the other's support.
- Of any status claim I make: a cited input whose status is weaker than I state, or a symbol I compared
  against an object it does not denote (checked by file + locating string).

Verdict vocabulary: CONFIRMED / NOT-VERIFIED / REFUTED for claims I check; PROVEN-HERE (with every input
and its status named) / CONDITIONAL / OPEN for results I produce. Numeric checks: criteria file first,
exact rational arithmetic only.

---

## 1. Read record, provenance, symbols pinned (written 2026-10-29T05:51:26Z, after reading, before the derivations of §3-§6)

**Read (by grep + bounded ranges; locating strings, not line numbers, are authoritative).** ASSEMBLY55 §1 (C5a/C5b, "Positivity,
the one min-property used on that domain"), §8 ML6; CODEX_REVIEW_ASSEMBLY R6, R7, "Corrected ordered OPEN work list" item 8;
CODEX_REVIEW_BFT4B R4-R9, "Single most dangerous unverified bridge"; HIST §14.0-14.3, §20.3 (C), §25 (Theorem A5, (a5-G), (a5-U),
(a3-q), (I_k^E)″, (c5″)); FLOW "Def F-strip", "(SF-bg)", "(SF-g)_k", §5.1 "Laplace expansion at the tree minimiser", Lemma F-tel;
PLD §15.2 "(SG^{fl})_k" table row "fixes 𝔟(V) := the minimiser of E_k + the kernel term given V", §16.9; PROOF "Lemma BR1", "*Not
shown:* that U(V) is the global minimiser", "[R20-fix 13, optional] (MIN_1) weakened", "Lemma TOWER-VAR", "Lemma N5-coer",
"Setting N5-0", "**Slice.** H_0 := {A : h(A) = 0}", "Lemma NA-alg", [S26-BANKED] lines for K^(σ), GV-E, BFT-3, NSL/ID, BFT-4 (a)/(b);
NSL55 §2-§4 (Theorem NSL, Lemma A, Lemma B, Corollary K-U, Theorem ID); CODEX_REVIEW_NSL F3, F5, F6, F7, "Exactly what may be
banked"; GV55 §3.1 "Theorem BFT-E (assembly)"; KFACTOR_OFF55 §1.1-1.4, "3.4 Proposition CCP"; BFT34_55 §1.1-1.3 (Lemma WD,
Theorem BFT3-glob); BFT_B §16.1 "quintic tents", §16.14 "I_χλ_0 := Σ_Xχ^5_Xλ_0(c_X)", bb11 row B1a; BFT_A "Lemma BA-1",
"||B_k||_D := sup|B_k|"; SF §6.2 ((a5-G♯), (a5-U), (MIN-reg), Proposition U-red), §7.1 (Corollary CE-exp^0, CE-exp^k), §10.1
"(CE-Q^∞): OPEN (named; the exact wall)"; HW "(CLS-min)_{c,t}", "the global minimiser restricted to Q's column is a competitor";
SQ §0 "(REG-min)"; LARGE55 §5-§6 ((BFT-coer), Lemma PRICE, I1-I11); CODEX_REVIEW_LARGE (F1-F6); LCONV55 §A-§C (Lemma FOL,
Theorem NC); REVIEW_S22 "Statement (BFT)", "Who needs which part".

**Files that look unfinished on disk now.** CODEX_REVIEW_LARGE.md ends after "Finding F6" with no summary table, no "Exactly what
may be banked" and no route verdict, although its PRE-STATED promises all three: **read as unfinished.** CODEX_REVIEW_RLOC and
CODEX_REVIEW_OFFGLOB were not used.

**Symbols pinned (systemic defect 1).** Everything new in this file carries a subscript M or a name not used elsewhere in the lane.
- **E^cb_j** := NSL55 §4.0 "E^cb_j(w) := 𝔉_j(exp Z_j(w); e^w)", Z_j(w) the depth-j BFT-E point (GV55 "Theorem BFT-E (assembly)"),
  real w with ‖w‖_D ≤ ε_u; **E^cb_0 := S_W**. **F^cb_j(w, v) := E^cb_j(w) + κ_jΣ_cφ̂_c(M̄^{(j)}_c(e^w); e^v)** (NSL55 §4.0);
  **U^cb_j(v)** := the level-j component of Z_{j+1}(v). These are PROOF's normalisation: 𝔉_k := S_W(U_0) + Σ_jκ_jΣ_cφ̂_c
  (TOWER-VAR), S_W := Σ_pRe tr(1 − U_p), φ̂ := Nφ (Setting N5-bg).
- **The min-tower** (three names, one object up to normalisation and the k̃/φ difference): HIST 𝓔_k (φ-based, s = 1 − Re tr/N,
  uniform κ) ; FLOW 𝒯_k (k̃-based; 𝒯_k − 𝓔_k = κΣd(M̄) ≥ 0, sextic, HIST Lemma HF); PROOF E_1^NA := min_UF. Dictionary:
  with κ_j ≡ κ, 𝔉_k(chain; V) = N·(HIST's chain energy), so **E^cb_k = N·(the HIST-normalised critical value)**. I write
  **E^min_k(V) := inf over chains of 𝔉_k(·; V)** (= N𝓔_k).
- **𝒢^rt_j** := level-j gauges equal to 1 at every level-(j+1) root. Per CODEX_REVIEW_NSL F5 (agreed below) this is a SUBGROUP of
  the fixed-datum symmetry group, not all of it; I only ever use elements of it.
- **S_[j]** := Ker Λ^{(1)} on level-j fields: the depth-1 slice of NSL55 applied to the step j → j+1 (Λ^{(1)} is linear, reads the
  finer field only, Lemma A (a)). Not N5-coer's slice, which I call **S_N := ker h ∩ ker(P_res d*)** (PROOF "Setting N5-0").
- ‖·‖_D := own-unit sup of the HS norm of link logs in the global gauge (BFT_A "||B_k||_D := sup|B_k|"). ℓ² := (Σ_b|w_b|²_HS)^{1/2}
  in own units (N5-coer's "unit-weight ℓ² norms on links"). |·|_∞,comp := max over links and HS-orthonormal su(N) components.
- Collisions avoided: I do not use ε_1, ε_*, η_1, C_1, c_1, κ_p as my own symbols; where I quote them, the file is named. HIST's
  κ_5 (decay rate), RLARGE's ε_1 (small-field threshold) and N5-coer's c_1 (= 1/(3.5·10⁶), NA-lev (c)) are three different objects
  and only the last one enters a constant here (inside γ_M, through N5-coer).

**Codex verdicts used** (agree/disagree is stated in §9): CODEX_REVIEW_ASSEMBLY R6, R7, item 8; CODEX_REVIEW_BFT4B R4, R9, closing
bridge sentence; CODEX_REVIEW_NSL F3, F5, F6, F7 and its bankable items 2-4; CODEX_REVIEW_KOFF item 5 / bankable (through [S26-BANKED]);
CODEX_REVIEW_GSHARP F9 (on N5-coer); CODEX_REVIEW_LARGE F1, F2 (file unfinished).

---

## 2. T1 — Consumer census: what each min-tower reader actually uses

Legend for the last column. **(c)** only properties a critical value has (analyticity, locality, jets, criticality, positivity,
the telescoping identity); **(d)** a LOWER bound on the tower — these transfer from the infimum to the critical value for free,
because a critical value is the energy of one chain: **E^cb_k ≥ E^min_k** wherever both are defined; **(b)** a minimum over the
consumer's own integration/chart domain, with a quadratic margin (the restricted small-field minimum of §3); **(a)** global
minimality over all chains. A consumer is put in (a) only if its load-bearing step compares against configurations outside every
small-field chart.

| # | Consumer (file, locating string) | What its load-bearing step uses | Needs |
|---|---|---|---|
| M1 | FLOW "Def F-strip" + "(SF-bg)": "The tree tower Φ_{j←n} and the functionals 𝒯_k are real analytic on a complex neighbourhood of the trivial field (in normalised Lie coordinates, uniformly in k), with exponentially local derivatives of every order ≤ 4" | analyticity on a k-uniform polydisc; derivative locality; 𝒯_k ≥ 0 = 𝒯_k(1); invariances; Hessian at 1 by "envelope theorem at a minimum that is nondegenerate on the gauge slice" | **(c)**. As written (min-defined) the analyticity clause is *equivalent* to an identification min = critical on the polydisc (a minimum of analytic functions is not analytic in general), i.e. it secretly contains (MIN-cb) there. Restated with 𝒯_k := E^cb_k/N and Φ := the BFT-E point it is BFT-2 + BFT-3 on 𝒞_glob (both banked conditionally, [S26-BANKED]); the Hessian identity holds at any nondegenerate critical point (Schur complement); positivity holds for any real chain's energy; invariances: §3.9 (c). The k̃ → φ replacement (CODEX_REVIEW_FLOW55 item 2; HIST "[RH2-fix 10]") is automatic: E^cb uses φ̂. |
| M2 | FLOW "(SF-g)_k" and FLOW55 §7 "given **(SF-g)_k**": "Ẽ_k are the renormalised level-k polymers … evaluated at the tree background", polydiscs D_α(X) | the background MAP Φ, not its minimality | **(c)** (Φ := BFT-E point). |
| M3 | FLOW §5.1 "Laplace expansion at the tree minimiser U* = Φ_{k←k+1}(V) gives −log∫ = u𝒯_{k+1}(V) + Γ_k(V) + O(1/u)"; Lemma F-tel "Minimising over U_j, then U_{j+1}, … gives min f = 𝒯_n(V), attained at the tower" | (i) the telescoping of the tower; (ii) a positive Gaussian at the expansion point; (iii) as a rigorous asymptotic, that the integrand on the integration chart is dominated by its value at the expansion point | (i) **(c)** = Theorem ID (I4) (banked conditionally). (ii) **(c)**. (iii) **(b)**: the restricted minimum on the stage-k chart (Theorem RSM_j, §3.6). The formal one-loop coefficients only see jets at 1 (ASSEMBLY C5a; CODEX_REVIEW_ASSEMBLY R6). |
| M4 | HIST "(a″) Main term u_k𝓔^{an}_k(U) on Λ_k (Theorem A5 (C)); real points: 𝓔^{an}_k = 𝓔^♭_k (the localised infimum over full cones)"; densities "equal on real points to the assigned terms of THE minimiser" | definitional: an infimum, made analytic through A5 (A) [(a3-q) + AE-red ⇒ every minimiser is regular and critical] and A5 (B) [(a5-U) ⇒ critical value = infimum on real points] | **(c)** for the definition: once the main term is DEFINED as the critical value with critical-chain densities (§6, Proposition DENS), A5 (A)-(B) and hence (a5-U), (a3-q) and A5's use of (MS-Sob) are not needed — on 𝒞_glob. The free-boundary version on Λ_k with large-field holes stays OPEN (it was OPEN before too: (a5-G) etc. were OPEN there). |
| M5 | HIST "(c4) The coupling shift of R1^J against 𝓔_k (PROVEN, arithmetic, given (a)'s per-cube bound C_𝓔)" | a per-cube bound 0 ≤ 𝓔_{k,x} ≤ C_𝓔 | **(c)**: Proposition DENS (b) (§6). |
| M6 | HIST "(c5″) Self-reproduction in critical-value form": "The Laplace step of (SF^J) needs the critical point to be the global minimiser of the real exponent" | the stage-k Laplace/cluster step around the background | **(b)**, not (a): the step integrates U_k over the history's small-field region only; SF's own rigorous version ("Corollary CE-exp^k: CONDITIONAL ⇐ … the criticality of the level-k background") assumes criticality + N5, and the cut complement is a separate item ((CE-Q)). The word "global" is refuted in §4.4. |
| M7 | HIST "(PLD-q)_k: its Peierls exponent … needs a classical lower bound u_k𝓔_k(U) ≥ u_kc_sf·η_q²-type per bad plaquette"; HIST "Corollary CLS-cone"; HIST Theorem A5 (D) | a LOWER bound on the tower | **(d)**: transfers to E^cb (A5 (D) says exactly this). Whether the lower bound itself holds is CLS/BFT-coer, OPEN, and independent of (MIN-cb). |
| M8 | HW "(CLS-min)_{c,t}" (= SQ's consumed statement; "(CLS-min) ⟺ the same lower bound for EVERY chain on 𝒞(P)", SQ "[RSQ1-fix S1-1]") | a lower bound for every chain | **(d)**; (MIN-cb) neither needed nor helpful. v3-route wall; LARGE55 replaces it by (BFT-coer). |
| M9 | HW "(M-f) … Reduction to the main term": "the global minimiser restricted to Q's column is a competitor in F^col's infimum" | that the assigned terms are those of SOME chain with top U_k | **(c)**: the argument is a competitor argument; it holds verbatim for the critical chain's terms. |
| M10 | PLD §15.2 table: "(I_k^E) … fixes 𝔟(V) := the minimiser of E_k + the kernel term given V (background field)"; (SG^{fl})_k "centred at 𝔟(V)"; Õ_i(𝔟(V), V) | the conditional law of U given V concentrates at 𝔟(V) with Gaussian tails; N5 at 𝔟(V); (BG)_k regularity | **(b)** (restricted minimum with quadratic margin on the cut-good integration domain: §3.6 + §3.7), plus N5 and BFT-1/3 at the critical point. The domain 𝒱^{sf}(A) is only LOCALLY small: region version OPEN. |
| M11 | PROOF "*Not shown:* that U(V) is the global minimiser of F(·, V) (B-NA's uniqueness at one level; named **(MIN_1)**)"; "For E_1^NA := min_UF (rather than the branch) the same holds under (MIN_1)"; "[R20-fix 13, optional] (MIN_1) weakened" | no consumer reads E_1^NA rather than E_1^br; PROOF itself records the restricted form as sufficient | **(b)**: Corollary MIN_1-w (§3.10) proves the weakened form on 𝒞_glob, conditionally. |
| M12 | SF "(a5-U) [restated on R_{3ε_1}; OPEN]", "(MIN-reg) [named, OPEN]", "Proposition U-red"; REVIEW_S22 "SF: BFT-1 (θ_w > 0), 2 (complex ball for (R♯)) and 5, giving (a5-G♯), (a5-U) and (MIN-reg)" | global uniqueness/closeness of minimisers, used only to make A5's infimum analytic | leave the critical path with M4's restatement. REVIEW_S22's "giving (a5-U) and (MIN-reg)" does not follow from BFT as stated (§8, finding F-9). |
| M13 | SF "(CE-Q^∞): OPEN (named; the exact wall)": "A Z-local bound would need a local coercivity of the true action (S(e^AU) − S(U) ≥ δ·(Hessian quadratic) on the chart, localised), which is not available" | a ONE-STEP coercivity of the action on the fluctuation chart | **(b)**, genuinely: this is the one consumer that needs a quantitative margin away from the background. Theorem RSM_j supplies the chart part (§4.2); beyond the chart it is OPEN. |
| M14 | RLARGE row 4 "(I_k^E)″"; LARGE55 "6.1 The target representation (R_m)": "main term u_m𝓔_m (coupling shifted by δβ)"; "6.2 (BFT-coer)" | M4's main term; (BFT-coer) is a lower bound on the main term at chart fields | M4's verdict; (BFT-coer) is **(d)**-type (a coercivity of the critical value), OPEN, LARGE55's I2. |
| M15 | UIR55 "(TC-b)_𝔍", "Lemma SPLIT/ENV-𝒯"; NORMS "By TOWER-VAR (d), D³E_k^br(1)"; FLOW55 "trivial-point jets" | jets at 1 | **(c)** (germ level; CODEX_REVIEW_ASSEMBLY R6). |
| M16 | HIST "(c3) … (D1-c) … g²(S_k(U) − S_k(U')) → 𝓔_k(U) − 𝓔_k(U') (Laplace link)" [ARGUED] | the g → 0 limit of the exact, unrestricted effective action | an ARGUED motivation, not a consumer of any proven statement; in a small-field representation the relevant object is the restricted minimum. No change. |

**Answer to T1.** No consumer's load-bearing step needs global minimality over all chains **(a)**. Ten readers need only
critical-value properties or lower bounds that transfer (M1, M2, M4, M5, M7, M8, M9, M14, M15, M16); four need a
**restricted** minimum with a quadratic margin on their own small-field chart (M3 (iii), M6, M10, M11), and one of those
(M13) needs that margin quantitatively. The only reader whose literal text demands global minimality is HIST (c5″) (M6), and
its demand is stronger than its use (§4.4). This is consistent with CODEX_REVIEW_ASSEMBLY R7's remark that the restricted
small-field form "is an alternative already named in PROOF", and it sharpens it: the alternative is not optional repair
architecture, it is what the consumers use.

---

## 3. T2 — The restricted small-field minimum (the alternative route), proven as an implication

### 3.0 Setting and the inputs, each with its status
Setting R: d = 4, N ≥ 2, odd L ≥ 3, κ_j ∈ [κ_−, κ_+], 0 < α < σ ≤ 1, θ₀ as in GV55 "Theorem BFT-E (assembly)"; 𝒞_glob (real data in
one global gauge), trivial background, m = 0; tori with level-k side T ≥ 3; 0 ≤ j ≤ k − 1. Level j is "own units"; ‖·‖_D, ℓ²,
S_[j], 𝒢^rt_j, Λ_* (level-j functions vanishing at the level-(j+1) roots) as pinned in §1.
- **(In-A) BFT-E at every depth** — GV55 Theorem BFT-E; [S26-BANKED] "Theorem K^(σ) (corrected) — CONFIRMED conditionally" and
  "Proposition GV-E … CONFIRMED as scoped implications". Used: existence/uniqueness of Z_j(w) for ‖w‖_D ≤ ε_0; BFT-1 bounds
  (own |x_i| ≤ L^{−(j−i)}η, own plaquette logs ≤ L^{−2(j−i)}(2η + 9η²), own residuals ≤ L^{−(2+σ)(j−1−i)}η + CL^{−3(j−i)}η², η :=
  C_0‖w‖_D); BFT-2 (Z_j and E^cb_j holomorphic on the polydisc |w|_∞ ≤ r_ℂε_0 with BFT-1 there); CCP (d) (fixed point = full
  critical point). **CONDITIONAL** (Codex KOFF/GV scope).
- **(In-B) Theorem NSL at depth 1 and at depth j** — NSL55 §2; Codex NSL bankable item 2 **CONDITIONAL** ("real existence,
  small-gauge uniqueness, bound C_N = 4 + 3C_Λ"). Used only in its real form, in the scaled norms (Codex NSL F6's analyticity
  qualification is respected: at depth 1, n_0 ≤ 20L³‖w‖_D + ‖v‖_D, so an own-unit sup ball of fixed radius IS inside NSL's
  hypothesis; at depth j I apply it only to configurations small in the depth-j scaled norm).
- **(In-C) Corollary K-U and Theorem ID (I1)-(I3)** — NSL55 §4.1, §4.3; Codex NSL bankable item 3 **CONDITIONAL** (with F3's
  repaired upscaling and F5's subgroup wording).
- **(In-D) Lemma N5-coer** — PROOF "Lemma N5-coer (coercivity on the slice …)": **O_i ≥ γ_i on H_0 = ker h**, O_i := H_i +
  κ_iQ^TQ + dP_resd* (PROOF "Setting N5-0"), γ_i := ½min{2c_1L^{−2}min(c_E^−, κ_−/2), ν_N}, level-uniform. Status: CONFIRMED in
  REVIEW_S18_S19 ("re-derived all four steps"); CODEX_REVIEW_GSHARP F9: N5-coer and LINEAR_PACKAGE Prop. 6.4 "do establish the
  one-level effective-energy inequalities for each i". I re-read its proof (steps (1)-(4) and the [R1819-fix 9] sharpening) and
  agree with its structure; I did not re-derive NA-lev (c)'s constant c_1 (frozen package). Only γ_min := inf_iγ_i > 0 is used.
- **(In-E) Composite gauge invariance of 𝔉_j and BA-1** — NSL55 "(In-4)" (re-derived there; Codex NSL F6 item 5 re-derives the
  residual covariance "ρ(x^g) = Ad(g_Y)ρ(x) exactly"); BFT_A "Lemma BA-1 (restriction)" (REVIEW_BFT_A_S1 CONFIRMED). Elementary.
- **(In-F) Local analyticity of φ̂** near the identity (CODEX_REVIEW_ASSEMBLY R6 step 3: "the maximizer defining φ is analytic
  by the ordinary finite-dimensional IFT"; HIST "Lemma TERM-an" (ii)-(iii) for an explicit domain). **CONFIRMED** (Codex) /
  PROVEN-HERE in HIST.
- **(In-G) NA-alg (a)** — PROOF "Lemma NA-alg": for M = Σw_je^{Y_j}, |Y_j|_HS ≤ y ≤ 1/20, the SU(N) maximiser is W_0 = e^{X_0} with
  **|X_0 − Ȳ| ≤ 9.2y²**. Lane status CONFIRMED-WITH-FIX (as cited in NSL55 §3.0).
- **(In-H) Quintic tents** — BFT_B "quintic tents σ_5(t) := 1 − 10t³ + 15t⁴ − 6t⁵ … χ^5_X(z) := Π_νσ_5(|z_ν − c_{X,ν}|_T/n)",
  bb11 "B1a … Σ_Xχ^5_X = 1 and χ^5_X(c_Y) = δ_{XY} … PASS (exact)"; the facts I use are re-checked exactly in **mc55_2** (§7).
- **(In-I) NSL55 Lemma A (a)-(b)**: Λ^{(j)} is real-linear, reads the finest field only, and **Λ^{(j)}(dμ) = −μ for μ ∈ Λ_*^{(j)}**
  (EP-alg; Codex GSHARP banked item 1; Codex NSL F6 item 1 re-derived). **CONFIRMED** (Codex).
- **(In-J) NSL55 Lemma B** ((B0), (B1′)): the gauge action in coarse units. Codex NSL F4: "corrected arithmetic holds".
None of (H2)_m, (H3)_m, BFT-3 at orders ≥ 2, BFT-4, BFT-5, (R), (a5-G♯), (MIN-reg), (a5-U), (a3-q), (MS-Sob) is used anywhere in §3.

### 3.1 Lemma CV (critical value against infimum) — PROVEN-HERE (one line)
For real B with ‖B‖_D ≤ ε_u: **E^cb_k(B) = 𝔉_k(exp Z_k(B); e^B) ≥ E^min_k(e^B) ≥ 0.** Hence every lower bound proven for E^min
(or for every chain) holds for E^cb_k on its domain; upper bounds do not transfer. *Proof.* A critical value is the energy of one
chain; every term of 𝔉_k is ≥ 0 on real chains. ∎ (Positivity alone does not give minimality: CODEX_REVIEW_ASSEMBLY R7, agreed.)

### 3.2 Lemma HL (Hessian-Lipschitz from holomorphy plus a uniform gradient bound) — PROVEN-HERE (elementary)
Let I be a finite set, P_R := {z ∈ ℂ^I : |z_i| < R ∀i}, f holomorphic on P_R, real on real points, with **|∂_if| ≤ G on P_R** for
every i. Then for real w, w′ ∈ P_{R/4}: **‖D²f(w)‖_{ℓ²→ℓ²} ≤ 2G/R and ‖D²f(w) − D²f(w′)‖_{ℓ²→ℓ²} ≤ (8G/R²)|w − w′|_∞.**
*Proof.* (1) For z ∈ P_{R/2} (complex) and real h with |h|_∞ ≤ 1, ζ ↦ ∂_if(z + ζh) is holomorphic on |ζ| < R/2 with modulus ≤ G, so
|(D²f(z)h)_i| ≤ 2G/R (Cauchy). (2) For real w ∈ P_{R/4} and real z, h with |z|_∞, |h|_∞ ≤ 1, ζ ↦ (D²f(w + ζz)h)_i is holomorphic on
|ζ| < R/4 (w + ζz ∈ P_{R/2}) with modulus ≤ 2G/R by (1), so |(D³f(w)[z, h, ·])_i| ≤ 8G/R². (3) For real w, z the matrices D²f(w) and
A := D³f(w)[z, ·, ·] are real symmetric; choosing h_j := sgn of the i-th row gives max row sums ≤ 2G/R resp. 8G/R²; for a real
symmetric matrix ‖·‖_{ℓ²→ℓ²} ≤ (max row sum · max column sum)^{1/2} = max row sum (Schur test). Integrate A along the segment
from w′ to w, which stays in the convex set P_{R/4}. ∎
*Why this matters.* It converts BFT-2 (holomorphy on a sup-norm polydisc, where |E^cb_j| itself is extensive) plus a LOCAL first-
derivative bound into an ℓ²-operator bound on Hessian differences, with no locality estimate at orders 2 and 3.

### 3.3 Lemma GC (the gradient constants) — PROVEN-HERE as an implication of In-A, In-E, In-F
(E) Fix j ≥ 1, D := N² − 1, R_E := r_ℂε_0/√D (the real-component polydisc P_{R_E} lies in BFT-2's polydisc, since |w_b|_HS ≤
√D·max_a|w^a_b|). There is G_E < ∞, depending only on (N, L, κ_+) and BFT-E's constants, with **|∂E^cb_j/∂w^a_y| ≤ G_E on
P_{R_E}**. (K) There are R_K > 0, G_K < ∞ depending only on (N, L, d, κ_+) such that K_j(w, v) := κ_jΣ_cφ̂_c(M̄_c(e^w); e^v) is
holomorphic on the component polydisc P_{R_K} in the joint variable (w, v), with all first partials bounded by G_K there.
*Proof.* (E) For real w, Z_j(w) is a full critical point (CCP (d)), so ∇_x𝔉_j(Z_j(w); w) = 0; both sides are holomorphic in w on
BFT-2's polydisc, hence the identity holds there. Chain rule: ∂E^cb_j/∂w_y = (∂_{w_y}𝔉_j)(Z_j(w); w). By BA-1 / TOWER-VAR only the top
soft term at the level-j link y depends on w_y: Ψ_y := κ_{j−1}φ̂_y(M̄_y(e^{x_{j−1}}); e^{w_y}), a holomorphic function of boundedly many
level-(j−1) links (those on the S4′ contours of y) and of w_y on the local domain of In-F; BFT-1 on the complex polydisc keeps
those arguments inside a fixed sub-polydisc of it (shrinking ε_0 by a fixed factor if necessary); Cauchy in w_y gives G_E.
This is the n = 1 bound "|∂E_k^br/∂B_y| ≤ C_E′" of BFT34_55 Theorem BFT3-glob (E); its proof there uses (H1) only, not (H2)_m or
(H3)_m — I checked this in the proof text ("Only the top soft term κ_{k−1}φ̂_y(M̄_y(e^{x_{k−1}}); B_y) depends on B_y … this gives
C_E′ and the n = 1 bound"). (K) K_j is a finite sum of local holomorphic terms (In-F) on the polydisc where every contour spread
is ≤ 1/20; a link lies on the S4′ contours of at most m_T level-(j+1) links (m_T = m_T(L, d)), and v_c enters one term. ∎

### 3.4 Lemma ANG (trivial-point coercivity on the slice S_[j]) — PROVEN-HERE as an implication of In-D, In-I
For every j ≥ 0 and every real level-j 1-form h ∈ S_[j]:
  **Hess_wF^cb_j(0, 0)[h, h] ≥ γ_M‖h‖²_2,  γ_M := γ_min/(1 + C_dΛ)²,  C_dΛ := ‖d∘Λ^{(1)}‖_{ℓ²→ℓ²} < ∞,**
with γ_min, C_dΛ independent of (j, k, T).
*Proof.* (1) *The form.* Z_j(0) = 0 (the trivial chain is a slice critical point; K-U). By the implicit function theorem in the
slice at the nondegenerate trivial point, D²E^cb_j(0) is the Schur complement of D²𝔉_j(0; 0) with respect to the slice
variables; since TOWER-VAR (c) identifies the quadratic part of 𝔉_j with Setting SC's chain energy, which is invariant under the
finer composite gauge directions to which the slice is a complement, that Schur complement is the minimum over ALL finer
variables, i.e. the Hessian H_j of Setting SC's E_j. With φ̂ = ½|QA|² + O(A³) (Setting N5-bg): **Hess_wF^cb_j(0, 0) =
(H_j + κ_jQ^TQ) ⊗ 1_{su(N)} = O_j − dP_resd*** (j = 0: H_0 = d*d, E^cb_0 = S_W). (2) *Decomposition.* λ ↦ (h(dλ), P_resd*dλ) maps
Λ_* bijectively onto (one su(N)-value per block) ⊕ Λ_res: both sides have dimension n_s − n_b per colour (n_s level-j sites, n_b
blocks; Λ_res := {λ(c_X) = 0, Σ_{B(X)}λ = 0} has n_s − 2n_b); and it is injective, because h(dλ) = Q_0λ − λ(c) (PROOF "**Slice.**
H_0 := {A : h(A) = 0}") is the vector of block means of λ, so λ ∈ Λ_res, and then 0 = ⟨λ, P_resΔλ⟩ = ‖dλ‖² forces λ = const = 0.
So every h ∈ S_[j] is h = h_N + dλ with λ ∈ Λ_*, h_N ∈ S_N. (3) *Angle.* 0 = Λ^{(1)}(h) = Λ^{(1)}(h_N) − λ (In-I), so h = h_N +
dΛ^{(1)}(h_N) and ‖h‖_2 ≤ (1 + C_dΛ)‖h_N‖_2. (4) *Gauge invariance of the form.* (H_j + κ_jQ^TQ)dλ = 0 for λ ∈ Λ_* (E_j depends on
its argument only through d — PROOF "Lemma N2-a … (abelian) … E_k … depend on B_k only through dB_k" — and Qdλ = d(ev λ) = 0).
So Hess[h, h] = Hess[h_N, h_N] = ⟨h_N, O_jh_N⟩ − ‖P_resd*h_N‖² = ⟨h_N, O_jh_N⟩ ≥ γ_j‖h_N‖² ≥ γ_min(1 + C_dΛ)^{−2}‖h‖². (5) *C_dΛ.*
Λ^{(1)} = Σ_Xχ^5_Xλ^E_X (BFT_B "box-Coulomb normal form … glued by quintic tents"; Lemma A (a): linear at this order) is a
translation-covariant linear map of finite range with one local coefficient pattern; the Schur test bounds ‖Λ^{(1)}‖_{ℓ²→ℓ²} by a
constant depending on (N, L, d), and ‖d‖_{ℓ²→ℓ²} ≤ 2√d. ∎ [C_dΛ is not evaluated here. Colour: the trivial-point form is colour
diagonal, so N5-coer's one-colour statement applies componentwise in an HS-orthonormal basis of su(N).]

### 3.5 Lemma GI_j (small datum-gauge invariance of E^cb_j) — PROVEN-HERE as an implication of In-A, In-B, In-C, In-E, In-H, In-J
There are ε_GI, δ_GI > 0, independent of (j, k, T), such that for j ≥ 1, real w with ‖w‖_D ≤ ε_GI and real ξ ∈ Λ_* (level-j, zero at
the level-(j+1) roots) with |ξ|_{C¹} := ‖ξ‖_∞ + D_1(ξ) ≤ δ_GI (D_1 := max over level-j links of |ξ(y) − ξ(x)|), w′ := w^{e^ξ} has
‖w′‖_D ≤ ‖w‖_D + 3D_1(ξ) and **E^cb_j(w′) = E^cb_j(w)**. Hence **F^cb_j(w^{e^ξ}, v) = F^cb_j(w, v)** for every v (the soft term is
exactly invariant under gauges equal to 1 at the level-(j+1) roots: M̄_c(U^g) = g(c_X)M̄_c(U)g(c_Y)^{−1}). For j = 0 this is exact
(S_W is invariant under all level-0 gauges).
*Proof.* (1) *Lift.* ξ̃ := Σ_Yχ^5_Yξ(Y) (level-j sites Y; depth-j tents). χ^5_X(c_Y) = δ_XY (In-H) gives ξ̃(c_Y) = ξ(Y), so g :=
(e^{ev^{(i)}ξ̃})_{i≤j} is a composite gauge whose level-j component is e^ξ. On each depth-j coarse cell ξ̃ is the tensor smoothstep
blend of its 2^d corner values; with the smoothstep bounds of mc55_2 (sup|σ_5′| = 15/8, sup|σ_5″| < 5.78, sup|σ_5‴| = 60, C²
matching at both ends) its C^{2,1} norm in depth-j coarse units is ≤ C_χ|ξ|_{C¹}, C_χ = C_χ(d), so ‖ξ̃‖_♮ ≤ C_χ|ξ|_{C¹}.
(2) *Transport.* By In-E, y := (Z_j(w))^g is a full critical point of 𝔉_j(·; w′) and 𝔉_j(y; w′) = 𝔉_j(Z_j(w); w) = E^cb_j(w).
(3) *Size.* Lemma B (B0)-(B1′) is the algebra of the gauge action; its input bounds (‖u_i‖ ≤ 4‖ξ̃‖_♮, ‖(Ξξ̃)^c_i‖ ≤ ‖ξ̃‖_♮ by the
averaging argument of NSL55 Lemma A (d)) do not use vanishing at the level-j roots. So level by level ‖y^c_i − x^c_i‖_{1,α;i} ≤
‖ξ̃‖_♮ + 5K_G‖ξ̃‖_♮(5‖ξ̃‖_♮ + ‖x^c_i‖) (x := Z_j(w)), and the weighted residual part is unchanged (endpoint covariance). Hence
‖y‖_{(σ),j} ≤ (1 + 5K_G‖ξ̃‖_♮)C_0′‖w‖_D + ‖ξ̃‖_♮(1 + 25K_G‖ξ̃‖_♮) =: r_y. (4) *Identification.* For r_y ≤ min(r_N, r_u/C_N) and ‖w′‖_D ≤
ε_u, NSL at depth j gives g′ ∈ 𝒢^{(j)} (trivial at level j: the datum w′ is unchanged) with y^{g′} ∈ S_E^{(j)}, ‖y^{g′}‖ ≤ C_Nr_y ≤ r_u;
y^{g′} is a full critical point (In-E); Corollary K-U at depth j: y^{g′} = Z_j(w′). So E^cb_j(w′) = 𝔉_j(y^{g′}; w′) = 𝔉_j(y; w′) =
E^cb_j(w). (5) ‖w′_b‖ ≤ ‖w_b‖ + |log(e^{ξ(x)}e^{−ξ(y)})| + (BCH cross terms) ≤ ‖w‖_D + 3D_1(ξ) for small arguments. Fix ε_GI, δ_GI so
that ε_GI + 3δ_GI ≤ ε_u, r_y ≤ min(r_N, r_u/C_N) and Lemma B's R_0-conditions hold. ∎
*Relation to the banked text.* This is the mechanism of NSL55's (I3) converse ("(U^cb_j(v))^{ev^{(j)}e^ξ} is again a critical point of
F^cb_j(·, v), with the same value"), run at a general datum w and with an explicit interpolating lift; Codex NSL F7 checked the
(I3) converse. CODEX_REVIEW_NSL F5's warning is respected: only root-trivial gauges are used, and no uniqueness of the gauge is
inferred.

### 3.6 Theorem RSM_j (the per-level restricted small-field minimum) — PROVEN-HERE as an implication of In-A … In-J
*Constants* (all independent of j, k, T): C_HL := 8G_E/R_E² + 8G_K/R_K² (Lemma GC; at j = 0 the E-part is S_W's, explicit and
local, and is absorbed into the K-part); **ρ_c := min(R_E/4, R_K/4, γ_M/(4C_HL))** (convexity radius); c_♮ the constant with
|ξ|_{C¹} ≤ c_♮‖ξ‖_♮ for ξ ∈ Λ_* at depth 1 (c_♮ = c_♮(L, d); sup via vanishing at roots, NSL55 Lemma A (c)'s remark). Choose
**ρ_M** with 20L³ρ_M ≤ r_N/2, C_N·21L³ρ_M/L ≤ ρ_c, 2C_Λc_♮·21L³ρ_M ≤ δ_GI, ρ_M ≤ ε_GI; then **ε_M** ≤ min(ρ_M, γ_M/(4C_HL), ε_lev,
ε_ID, R_K/4, Lρ_c/(2C_NC_0′)) (ε_lev, ε_ID: Theorem ID's constants).

> **Theorem RSM_j.** For every 0 ≤ j ≤ k − 1, every real level-(j+1) 1-form v with ‖v‖_D ≤ ε_M and every real level-j 1-form
> w with ‖w‖_D ≤ ρ_M (all in the global gauge):
> - (i) there is ξ(w) ∈ Λ_* with w_S := w^{e^{ξ(w)}} ∈ S_[j], ‖w_S‖_D ≤ ρ_c, and F^cb_j(w, v) = F^cb_j(w_S, v);
> - (ii) there is w_* ∈ S_[j] ∩ {‖·‖_D ≤ ρ_c} in the small-gauge orbit of U^cb_j(v), with
>   **F^cb_j(w, v) ≥ E^cb_{j+1}(v) + (γ_M/4)‖w_S − w_*‖²_2;**
> - (iii) equality holds iff w_S = w_*, iff w = (U^cb_j(v))^{e^ζ} with ζ ∈ Λ_* small (|ζ|_{C¹} ≤ 2δ_GI).
> In words: on the own-unit sup ball of fixed radius ρ_M, **the per-level critical value E^cb_{j+1}(v) is the minimum of
> F^cb_j(·, v)**, attained exactly on the small root-trivial gauge orbit of U^cb_j(v), with a quadratic margin in slice coordinates.

*Proof.* **Step 1 (strict convexity on the slice ball).** For real w ∈ S_[j], ‖w‖_D ≤ ρ_c, and h ∈ S_[j]:
Hess_wF^cb_j(w, v)[h, h] ≥ Hess_wF^cb_j(0, 0)[h, h] − (‖Hess E^cb_j(w) − Hess E^cb_j(0)‖_{2→2} + ‖Hess_{ww}K_j(w, v) − Hess_{ww}K_j(0, 0)‖_{2→2})‖h‖²
≥ (γ_M − C_HL(ρ_c + ε_M))‖h‖² ≥ (γ_M/2)‖h‖², by Lemma ANG and Lemma HL applied to E^cb_j (Lemma GC (E)) and to K_j as a function of (w, v)
(Lemma GC (K); the ww-block of a Hessian difference is bounded by the whole difference). The component sup of w is ≤ ‖w‖_D ≤ ρ_c ≤
R/4 for both polydiscs. **Step 2 (a slice critical point).** By ID (I2) (‖v‖_D ≤ ε_lev), U^cb_j(v) is a critical point of F^cb_j(·, v)
and F^cb_j(U^cb_j(v), v) = E^cb_{j+1}(v); by ID (I3), ‖U^cb_j(v)‖_{T;v} ≤ C_0′‖v‖_D. NSL at depth 1 on the step j → j+1 (whose depth-1 norm
is ‖·‖_{T;v}) gives ξ_* ∈ Λ_* with w_* := (U^cb_j(v))^{e^{ξ_*}} ∈ S_[j], ‖w_*‖_D ≤ ‖w_*‖_{T;v}/L ≤ C_NC_0′ε_M/L ≤ ρ_c/2, ‖ξ_*‖_♮ ≤
2C_ΛC_0′ε_M. By Lemma GI_j with the fixed gauge e^{ξ_*} on a neighbourhood of U^cb_j(v), F^cb_j(·, v) is invariant under the local
diffeomorphism w ↦ w^{e^{ξ_*}}; so w_* is a critical point of F^cb_j(·, v) in every direction and F^cb_j(w_*, v) = E^cb_{j+1}(v).
**Step 3 (minimum on the slice ball).** For w_S ∈ S_[j], ‖w_S‖_D ≤ ρ_c, the segment w_* + t(w_S − w_*) stays in S_[j] ∩ {‖·‖_D ≤ ρ_c}
(both convex); f(t) := F^cb_j(w_* + t(w_S − w_*), v) has f′(0) = 0 (Step 2) and f″ ≥ (γ_M/2)‖w_S − w_*‖² (Step 1); so f(1) ≥ f(0) +
(γ_M/4)‖w_S − w_*‖². **Step 4 (gauge saturation).** For ‖w‖_D ≤ ρ_M: ‖w‖_{T;v} ≤ 20L³ρ_M + ε_M ≤ r_N (NSL55 Lemma SC (c)); NSL at
depth 1 gives ξ(w) with w_S ∈ S_[j], ‖w_S‖_{T;v} ≤ C_N·21L³ρ_M, so ‖w_S‖_D ≤ ρ_c, and |ξ(w)|_{C¹} ≤ c_♮·2C_Λ·21L³ρ_M ≤ δ_GI. Lemma GI_j:
F^cb_j(w, v) = F^cb_j(w_S, v). Step 3 gives (ii). **Step 5 (equality).** Equality forces w_S = w_* (strict convexity), i.e.
w = w_*^{e^{−ξ(w)}} = (U^cb_j(v))^{e^{ξ_*}e^{−ξ(w)}}, and e^{ξ_*}e^{−ξ(w)} = e^ζ with ζ ∈ Λ_*, |ζ|_{C¹} ≤ 2δ_GI (BCH, small); conversely
Lemma GI_j. ∎
*What it does not give.* Nothing off 𝒞_glob, on boxes/regions with holes, or for complex data; nothing about chains outside the
sup ball. The radius ρ_M is fixed but not evaluated (it inherits G_E, R_E from BFT-E's unevaluated constants, C_dΛ, and N5-coer's
γ_min ≈ 10⁻¹⁰ at κ ≡ 1, L = 3 — PROOF's table "proven trivial gap γ_i … 1.29·10⁻¹⁰").
*Why this does not contradict LCONV55 Theorem NC.* NC's negative curvature is along "following directions" (LCONV55 Lemma FOL:
U_{m+1} = W_0(M̄(U_m)), coarse levels free), on which the soft terms contribute no curvature. In RSM_j the coarse field v is
FIXED; the slow directions that NC exploits are then pinned by κ_jQ^TQ, which is inside γ_M (Lemma ANG). This is LCONV55 §G2's
"one-step conditional positivity", made rigorous on a chart whose radius is fixed by γ_M/C_HL. RSM_j makes no claim about the
multiscale measure conditioned on the defect-free event, which is NC's object.

### 3.7 Lemma LIFT_j (the per-level small-field class lies in the gauge orbit of a sup chart) — PROVEN-HERE (elementary)
Put **n_L := (2d(L−1) + L + 1)·((2L − 1) + (d − 1)(L − 1))** (= 220 at d = 4, L = 3). For a level-j configuration U and a real
level-(j+1) 1-form v (V := e^v), assume **(h1)** ‖1 − U(p)‖_op ≤ ε′ for every level-j plaquette p, **(h2)** ‖V_c − W_0(M̄_c(U))‖_op ≤ ε′
for every level-(j+1) link c, with ε′ ≤ 1/(30√N n_L). Let g(z) := T(a(c_X → z)) for z ∈ B(X) (a = the axial path in coordinate
order inside the level-(j+1) block B(X); T = transport of U), so g ∈ 𝒢^rt_j. Then
- (i) intra-block links: U^g_b = 1 on tree links and ‖U^g_b − 1‖_op ≤ ((d − 1)(L − 1)/2)ε′ on the others;
- (ii) a link b from B(X) to B(X + e_μ), c := (X, X + e_μ): **‖U^g_b − V_c‖_op ≤ (1 + 2√N n_L)ε′**;
- (iii) hence w := log U^g (principal logs) has **‖w‖_D ≤ 1.1√N(max_c‖V_c − 1‖_op + (1 + 2√N n_L)ε′)** when the bracket is ≤ 1/2.
*Proof.* (a) *Lasso bound.* For a closed lattice path γ of length ℓ in a box Q (a product of intervals), fix o ∈ Q and axial paths
a_Q(o → ·) inside Q. Telescoping, γ is conjugate to the product over its edges e = (x, x′) of the loops a_Q(o→x)·e·a_Q(o→x′)^{−1};
two axial paths to neighbours x, x′ = x ± e_μ agree on the legs before μ, differ by one step in leg μ and then run parallel at
distance one, so each such loop is a ladder of ≤ diam_1(Q) plaquettes, i.e. a product of ≤ diam_1(Q) conjugated plaquette
holonomies. For unitaries ‖AB − 1‖ ≤ ‖A − 1‖ + ‖B − 1‖ and conjugation preserves the norm, so **‖hol(γ) − 1‖_op ≤
ℓ·diam_1(Q)·max_{p⊂Q}‖1 − U(p)‖_op**. (b) For b = (x, x ± e_μ) inside B(X), U^g_b is the holonomy of the single ladder loop based
at c_X, with ≤ Σ_{ν>μ}|x_ν − (c_X)_ν| ≤ (d − 1)(L − 1)/2 rungs: (i). (c) For b from x ∈ B(X) to y ∈ B(Y), U^g_b = T(path_b), path_b :=
a(c_X→x)·b·a(c_Y→y)^{−1}, a path c_X → c_Y in Q := B(X) ∪ B(Y). Each S4′ contour T^σ_{y′} = P^σ(c_X→y′)·S_{y′}·P^σ(c_Y→y′+Le_μ)^{−1}
(PROOF's identity "∫_{T^σ_y} A = ∫_{P^σ(c_X→y)} A + ∫_{S_y} A − ∫_{P^σ(c_Y→y+Le_μ)} A") is also such a path. The loop path_b·(contour)^{−1}
has length ≤ 2d(L − 1) + L + 1 and diam_1(Q) = (2L − 1) + (d − 1)(L − 1), so (a) gives ‖T_b − T_σ‖_op ≤ n_Lε′ ≤ 1/30 for every
contour (T_b := T(path_b)). Put Y_σ := log(T_b^{−1}T_σ): |Y_σ|_HS ≤ √N·1.04n_Lε′ =: y ≤ 1/20. Left covariance of the maximiser
(W ↦ T_bW is a bijection of SU(N) and Re tr((T_bW)^{−1}T_bM) = Re tr(W^{−1}M)) gives W_0(M̄_c) = T_bW_0(Σw_σe^{Y_σ}) = T_be^{X_0} with
|X_0|_HS ≤ y + 9.2y² ≤ 1.46y (In-G), so ‖W_0(M̄_c) − T_b‖_op ≤ e^{1.46y} − 1 ≤ 1.7√N n_Lε′. With (h2): ‖T_b − V_c‖ ≤ (1 + 1.7√N n_L)ε′:
(ii). (d) For unitary U with ‖U − 1‖_op ≤ 1/2, |log U|_op ≤ 1.02‖U − 1‖_op (eigenvalue by eigenvalue: |θ| ≤ (θ/2)/sin(θ/2)·|e^{iθ} − 1|),
and |·|_HS ≤ √N|·|_op: (iii). ∎ The lasso bound (a)-(b) and the contour comparison of (c) are checked on exact SU(2) configurations
in **mc55_3** (§7).

### 3.8 Corollary RSM_j-class (the per-level small-field class) — PROVEN-HERE as an implication
Let 𝒮_j(v; ε′) := {U : (h1) and (h2) of Lemma LIFT_j}. Take **ε′_M := ρ_M/(3√N(1 + 2√N n_L))** and ε_M ≤ ρ_M/(3√N) (compatible with
§3.6's choice). For ‖v‖_D ≤ ε_M and every U ∈ 𝒮_j(v; ε′_M): there is g ∈ 𝒢^rt_j with U^g = e^w, ‖w‖_D ≤ ρ_M (LIFT_j); the number
**F^cb_j(U, v) := F^cb_j(w, v)** does not depend on the choice of (g, w); and **F^cb_j(U, v) ≥ E^cb_{j+1}(v)**, with equality iff
U ∈ 𝒢^rt_j·U^cb_j(v). *Proof.* Well-definedness: if e^{w_2} = (e^{w_1})^h with h ∈ 𝒢^rt_j and ‖w_i‖_D ≤ ρ_M, then for every link
‖h(x) − h(y)‖ ≤ ‖e^{w_1,b} − 1‖ + ‖e^{w_2,b} − 1‖ ≤ 2.2ρ_M, and h = 1 at the roots, which are ≤ d(L − 1)/2 steps away; so h = e^ζ with
ζ ∈ Λ_*, |ζ|_{C¹} ≤ δ_GI for ρ_M small, and Lemma GI_j gives F^cb_j(w_2, v) = F^cb_j(w_1, v). The rest is Theorem RSM_j. ∎
This is the form the stage-k Laplace step consumes (M3 (iii), M6, M10): **on the per-level small-field class relative to a fixed
coarse field in 𝒞_glob, the background U^cb_k(v) is the minimiser of the stage-k main term, uniquely modulo 𝒢^rt_k.**

### 3.9 Theorem RSM-tower (the composite restricted minimum, by telescoping) — PROVEN-HERE as an implication
Put **R_M := min(ρ_M, ε_M)** and 𝒦^{(k)}_R := {real chains u = (u_0, …, u_{k−1}) : ‖u_i‖_D ≤ R ∀i} (one global gauge, own units).
> (a) For every k ≥ 1, T ≥ 3, real B with ‖B‖_D ≤ R_M and every u ∈ 𝒦^{(k)}_{R_M}: **𝔉_k(exp u; e^B) ≥ E^cb_k(B)**, with equality
> iff u = (Z_k(B))^G for a composite gauge G trivial at level k.
> (b) If ‖B‖_D ≤ ε_att := LR_M/C_0, then Z_k(B) ∈ 𝒦^{(k)}_{R_M}, so **E^cb_k(B) = min{𝔉_k(exp u; e^B) : u ∈ 𝒦^{(k)}_{R_M}}**.
> (c) For every symmetry r of the hierarchical lattice (translations by level-k vectors; the B_4 group fixing a level-k root) and
> ‖B‖_D ≤ ε_att: **E^cb_k(rB) = E^cb_k(B)**.
*Proof.* (a) Induction on depth with the statement P′_j: "for ‖w‖_D ≤ R_M and u ∈ 𝒦^{(j)}_{R_M}, 𝔉_j(exp u; e^w) ≥ E^cb_j(w), equality
iff u = (Z_j(w))^G, G trivial at level j". P′_1 is RSM_0 (𝔉_1(·; v) = F^cb_0(·, v), U^cb_0(v) = Z_1(v)). P′_j ⇒ P′_{j+1}: by BA-1,
𝔉_{j+1}(exp u; e^w) = 𝔉_j(exp u_{<j}; e^{u_j}) + κ_jΣφ̂(M̄(e^{u_j}); e^w) ≥ E^cb_j(u_j) + κ_jΣφ̂ = F^cb_j(u_j, w) ≥ E^cb_{j+1}(w), the first
inequality by P′_j with datum u_j (‖u_j‖_D ≤ R_M ≤ ε_M), the second by RSM_j (‖u_j‖_D ≤ ρ_M, ‖w‖_D ≤ ε_M). **The radius does not
grow with the depth**: each step uses the same (ρ_M, ε_M). Equality forces equality in both: u_j = (U^cb_j(w))^{e^ζ} (RSM_j (iii)) and
u_{<j} = (Z_j(u_j))^{G_1}, G_1 trivial at level j (P′_j). Step (4) of Lemma GI_j's proof gives Z_j((U^cb_j(w))^{e^ζ}) =
((Z_j(U^cb_j(w)))^{g_ζ})^{g′} (g_ζ the tent lift of ζ, g′ ∈ 𝒢^{(j)}), and ID (I1) at depth j + 1 gives Z_j(U^cb_j(w)) =
((Z_{j+1}(w))_{<j})^{e^{ξ_j}} with e^{ξ_j} ∈ 𝒢^{(j)} (‖w‖_D ≤ ε_ID). Composing, u = (Z_{j+1}(w))^G with G trivial at level j + 1.
Conversely, composite gauge copies have the same energy (In-E). (b) BFT-1: own |x*_i| ≤ L^{−(k−i)}C_0‖B‖_D ≤ C_0‖B‖_D/L ≤ R_M.
(c) 𝔉_k(r·u; r·B) = 𝔉_k(u; B) (S_W is invariant and the S4′ family is B_4-symmetric: FLOW "D4-norm (1): the S4' family is
B_4-symmetric"), and 𝒦^{(k)}_{R_M} is r-invariant because ‖·‖_D is; apply (b) to B and to rB. ∎
*Remarks.* (1) The class 𝒦_{R_M} is much larger than BFT-E's slice ball (own |x_i| ≤ L^{−(k−i)}η there): it contains every chain that
is R_M-small in the global gauge at every level, including rough fine-level configurations such as LCONV55's stripe (links ≤ β in
the global gauge). (2) Part (a) is a lower bound for every chain of the class even when ‖B‖_D > ε_att. (3) Part (c) supplies, for
the critical value, the translation/B_4 invariance that FLOW's "Def F-strip" asserts for the minimum. (4) A version of (a) for
chains that are small only gauge-invariantly at every level (plaquettes and residuals) would need a depth-uniform global
multi-scale gauge: Lemma LIFT_j's axial gauge adds O(ε′) to the potential at each level going down, so iterating it is not
uniform; a smooth-lift version (HIST's MSG gives one on cones) is NOT proven here. No consumer in §2 needs that version: every
stage-k step is per-level (Corollary RSM_j-class).

### 3.10 Corollary MIN_1-w (PROOF's "(MIN_1) weakened", on 𝒞_glob) — PROVEN-HERE as an implication
(i) *Balaban's convention.* For real v with ‖v‖_D ≤ ε_M: **E^cb_1(v) = min{𝔉_1(U; e^v) : U ∈ 𝒮_0(v; ε′_M)}**, attained exactly on
𝒢^{(1)}·Z_1(v). (ii) *PROOF's convention.* For V = e^v with ‖v‖_D ≤ min(ε_M, ε_E1) (NSL55 §5.3's ε_E1): BR1's U(V) lies in
𝒮_0(v; ε′_M) once ε_E1 is also small enough that BR1 (iii)'s plaquette and residual bounds are ≤ ε′_M, and then **U(V) is the
minimiser of F(·, V) over the level-0 small-field class, uniquely modulo 𝒢^{(1)}, and E_1^br(V) = E_1^NA-restricted(V) = E_1^cb(v).**
*Proof.* (i) is Corollary RSM_j-class at j = 0 (at j = 0 only In-A, In-B, In-C at depth 1, In-D at i = 0, In-I and LIFT_0 are
used: no BFT-3 and no GI beyond the exact invariance of S_W). (ii) adds Proposition E1 (NSL55 §5.3; Codex NSL bankable item 4,
CONDITIONAL "E1 on its stated BR1 overlap"). ∎ This is exactly the target form recorded at PROOF "[R20-fix 13, optional] (MIN_1)
weakened … *U(V) is the unique minimiser of F(·, V) among the U with (U, V) in the level-0 small-field class* … Recorded as the
target form; not proven" — now proven on 𝒞_glob, conditionally. Two inherited flags stay: BR1's proof is L = 3-specialised
(CODEX_REVIEW_NSL; ASSEMBLY55 C4), and ε_E1 is not explicit.

---

## 4. T2 (continued) — The large-field comparison: what exists, what is needed, what is not

### 4.1 Corollary MARGIN (a definite excess away from the background, inside the chart) — PROVEN-HERE as an implication
In the setting of Corollary RSM_j-class, let w_S be the slice representative of U ∈ 𝒮_j(v; ε′_M) and w_* that of U^cb_j(v). If
max_b‖e^{w_S,b} − e^{w_*,b}‖_op ≥ τ, then **F^cb_j(U, v) − E^cb_{j+1}(v) ≥ γ_Mτ²/5**. In particular, if some level-j plaquette holonomy or
soft residual of U, read in the slice gauge, differs from that of the background by ≥ τ (operator norm), the excess is ≥ γ_Mτ²/97
(a plaquette moves by ≤ 4·max over its links, so some link moves by ≥ τ/4.4).
*Proof.* RSM_j (ii) and ‖w_S − w_*‖_2 ≥ max_b|w_S,b − w_*,b|_HS ≥ τ/1.1 (logs are 1.1-bi-Lipschitz near 1): γ_M/4·(τ/1.1)² ≥ γ_Mτ²/5. ∎
This is the only per-level "comparison against configurations away from the chart minimum" that is meaningful as a statement about
F^cb_j: off the gauge-saturated chart, F^cb_j(U, v) is not defined, because E^cb_j(U) needs U in (the 𝒢^rt_j-orbit of) 𝒞_glob(ε_u).

### 4.2 What SF's (CE-Q^∞) needs, and how much of it RSM supplies
SF "(CE-Q^∞)": "A Z-local bound would need a local coercivity of the true action (S(e^AU) − S(U) ≥ δ·(Hessian quadratic) on the chart,
localised), which is not available". **Supplied here (chart part, conditionally):** for the stage-k main term at the background
U := U^cb_k(v), Corollary MARGIN gives u_k[F^cb_k(e^AU, v) − F^cb_k(U, v)] ≥ u_k(γ_M/4)‖(e^AU)_S − w_*‖²_2 for every real A with e^AU in
the gauge-saturated chart — a product of per-link Gaussian factors, i.e. Z-local in the required sense. The u-free parts of the true
stage-k action (the U-dependent kernel normaliser log𝒩, which CODEX_REVIEW_LARGE F1 shows must be kept; the inherited polymers,
O(1) per cube by HIST (b)) change the Hessian by O(1) per link against u_kγ_M/4, so they do not spoil the bound for g_k small.
**Not supplied:** (1) the conversion from my slice S_[k] to SF's fluctuation coordinates (a slice-change constant: SF's slice at the
background must be quantitatively transversal to the gauge orbit, an FPq-type bound ‖λ‖ ≤ K_FP‖χ_UD_Uλ‖ at U) — NOT-VERIFIED here;
(2) the part of the deep set beyond the chart, which consists of Gribov copies of SF's slice (a matter for the gauge fixing) and of
configurations leaving 𝒮_k(v; ε′_M) (genuine large fields, priced by the kernel or by the level-k main term, not by RSM). (CE-Q^∞)
stays OPEN, reduced by its chart part.

### 4.3 Off the per-level class: the comparison is chain-level, and no consumer uses it
A comparison "energy off the chart exceeds the chart minimum by a definite amount" can only be stated for the chain energy with all
finer levels free, i.e. as (MIN-cb) with a margin. §2 found no consumer that uses it. What the RG uses instead for configurations off
the chart is absolute pricing:
- **LARGE55's route:** (BFT-coer) — "𝓔_{j+1}(V; Λ) ≥ c_co·Σ_{P⊂Λ}‖1 − V_P‖²_op" for chart fields V — a LOWER bound on the critical value
  (type (d) of §2), OPEN (LARGE55 I2); Lemma MIS for mismatches (CODEX_REVIEW_LARGE F2: CONFIRMED as a tail bound, GAP as the
  advertised interface); the frozen-region normalisation I5 (OPEN).
- **v3 route:** (CLS-min) (HW), a lower bound for every chain, OPEN.
Neither is implied by (MIN-cb), and neither implies it. So the "large-field comparison" of the task is not a missing piece of the
min-tower question: it is LARGE55's I2 (or v3's (CLS-min)), which this file does not prove.
**Remark (why RSM does not give (BFT-coer) for free).** RSM identifies E^cb_k with a minimum over a class; it gives no lower bound in
terms of the nonlinear curvature. The naive perturbative route "E^cb_k(B) ≥ (1 − Cη)E^lin_k(B), then E-low" fails exactly, not only in
its constants: for a small non-abelian pure gauge B_b := log(g(x)g(y)^{−1}), e^B is flat, so E^cb_k(B) = 0 (Proposition FLAT, §5.1),
while its linear curl dB is a non-zero sum of BCH commutators (dB = −½Σ[·,·] + …), so E^lin_k(B) ≥ c_E‖dB‖² > 0 (E-low). A coercivity in
terms of ‖1 − V_P‖ must therefore be proven with local gauge choices, i.e. for a local decomposition of E^cb; that is (BFT-coer)'s
content.

### 4.4 Finding: HIST (c5″)'s "global minimiser" requirement — REFUTED as a necessity claim
HIST "(c5″) Self-reproduction in critical-value form": "The Laplace step of (SF^J) needs the critical point to be the global minimiser
of the real exponent: that is where Theorem A5 (B)'s agreement is consumed". *Correct statement.* The stage-k step needs (α)
criticality of the background for the full stage-k action (SF "Corollary CE-exp^k: CONDITIONAL ⇐ … the criticality of the level-k
background for the full level-k action"), (β) positivity of the fluctuation operator there (N5), (γ) a quadratic lower bound of the
action on the integration chart (§4.1-4.2, consumed only by the deep part (CE-Q^∞)), and (δ) pricing of the cut complement ((CE-Q),
(CE-Q^∞)). *Derivation.* SF's Corollary CE-exp^0 integrates the fluctuation over the support of ν_∅ (the cut-good set) after the
Gaussian change of variables at the background, and states "*Not covered:* the cut-complement terms Q ≠ ∅ ((CE-Q))"; its stage-k
version replaces only the activities. The integration domain is the history's small-field region; its complement is priced, not
Laplace-expanded. No step compares the background with configurations outside every chart. So "global" must be replaced by
"minimiser over the stage-k integration domain, with a quadratic margin" — which Corollaries RSM_k-class and MARGIN supply on
𝒞_glob (conditionally).

### 4.5 Findings on ASSEMBLY55 C5b — two sentences REFUTED, the MISMATCH verdict CONFIRMED
- ASSEMBLY55 C5b: "Positivity, the one min-property used on that domain, survives (ii) for free". **REFUTED.** Positivity is used
  (M1), but it is not the one min-property used: M3 (iii), M6, M10, M11 and M13 use the minimising property over the consumer's own
  integration chart. Correct statement: under (ii) positivity and all lower bounds survive for free (Lemma CV); the restricted
  minimum does not, and is Theorem RSM_j / Corollary RSM_j-class. (Agrees with CODEX_REVIEW_ASSEMBLY R7, which refuted the same
  sentence from the other side: "positivity of a critical value is much weaker than its minimizing property".)
- ASSEMBLY55 C5b: "Where HIST compares with large fields ((CLS-NA)), the min definition is genuinely used and (i) is needed".
  **REFUTED** as to "(i) is needed". (CLS-NA)/(CLS-min) are lower bounds; a lower bound for an infimum is a lower bound for every
  chain (SQ "[RSQ1-fix S1-1] (CLS-min) ⟺ the same lower bound for EVERY chain on 𝒞(P)"), hence for every critical value (Lemma CV).
  (MIN-cb) neither implies nor is needed for them. What the v3 route does use at non-chart coarse fields is the infimum as a
  *definition* (it is defined everywhere), not its identification with a critical value.
- ASSEMBLY55 C5b's verdict "**MISMATCH (object + class)**": **CONFIRMED** — the consumers' texts read the min-tower on uniform/local
  domains and no banked statement identified it with E^cb there; this file supplies the identification in the restricted form on
  𝒞_glob (§3), and the critical-value restatement for the rest (§2).

---

## 5. (MIN-cb) itself: what holds, what does not follow, and the counterexample search

### 5.1 Proposition FLAT ((MIN-cb) holds exactly at flat data, for every k and T) — PROVEN-HERE
Let B be real with ‖B‖_D ≤ R_M and V := e^B flat (every level-k plaquette = 1). Then (i) **the zero set of 𝔉_k(·; V) is a single
composite-gauge orbit, by gauges trivial at level k**; (ii) **E^cb_k(B) = 0 = E^min_k(V)**, and Z_k(B) lies in that orbit. Hence every
global minimiser of the chain energy is a composite-gauge copy of the BFT-E point: (MIN-cb) holds at flat data, uniformly in k, T.
*Proof.* (i) Zero energy forces S_W(U_0) = 0, i.e. U_0 flat, and every soft term zero, i.e. U_{i+1}(c) = W_0(M̄_c(U_i)). If U_i is flat,
all S4′ contours of c run from c_X to c_Y inside the simply connected box B(X) ∪ B(Y), so they have one transport T_c ∈ SU(N); then
M̄_c = T_c and W_0(T_c) = T_c (Re tr(W^{−1}T) ≤ N with equality only at W = T), so U_{i+1}(c) is the root-to-root transport of U_i.
Inductively every level is flat and every level-i link is the transport of U_0 along a concatenation of root-to-root paths; so the
holonomies of U_0 based at a level-k root c equal those of V. Two flat connections with equal based holonomies are related by
g(z) := T^{(1)}(c → z)T^{(2)}(c → z)^{−1} (path-independent because the based holonomies agree), with g(c) = 1; since both chains carry
the same top V, their root-to-root transports to every level-k root agree, so g = 1 at all level-k roots; restricting g to the
level-i roots maps the whole second chain onto the first (transports are covariant). (ii) PROOF "Lemma TOWER-VAR (b)": at the
composite lift Z^lift "every soft fluctuation vanishes, every level-0 plaquette has holonomy 1 except the k-fold corner plaquettes
(holonomy V_{k,P})"; for flat V all of these are 1, so 𝔉_k(Z^lift; V) = 0. Its links are 1 or V_c in the global gauge (Lemma U0), so
Z^lift ∈ 𝒦^{(k)}_{R_M}. Theorem RSM-tower (a) gives 0 = 𝔉_k(Z^lift; V) ≥ E^cb_k(B) ≥ 0, and its equality case puts Z^lift in the
composite-gauge orbit of Z_k(B). ∎ [Inputs: TOWER-VAR (b) (REVIEW_S22: "ENV, H-fac, LOC_1, TOWER-VAR: CONFIRMED") and RSM-tower;
(i) is the R6 step-2 argument of CODEX_REVIEW_ASSEMBLY generalised from V = 1 to any flat V.]

### 5.2 Proposition MIN-fin ((MIN-cb) at fixed k and T) — PROVEN-HERE as an implication (Codex R6's mechanism + RSM-tower)
For every k ≥ 1 and T ≥ 3 there is ε_{k,T} > 0 such that, for real B with ‖B‖_D ≤ ε_{k,T}, **every global minimiser of 𝔉_k(·; e^B) is a
composite-gauge copy of Z_k(B), and E^min_k(e^B) = E^cb_k(B).** *Proof.* Let 𝒩 be the composite-gauge saturation of the open set
{u : max_i‖u_i‖_D < R_M}: open, gauge invariant, containing the zero orbit of 𝔉_k(·; 1) (Proposition FLAT (i) at V = 1). Its
complement in the compact chain space is compact and carries 𝔉_k(·; 1) ≥ δ_{k,T} > 0; by uniform continuity 𝔉_k(·; e^B) ≥ δ_{k,T}/2 there
for small B, while E^cb_k(B) → 0. So every global minimiser lies in 𝒩, and RSM-tower (a) (with its equality case) applies. ∎
**Non-uniformity is real, not a proof artefact of this route.** E^cb_k(B) is extensive: for B with curvature of size ε on every
plaquette, E-low gives E^cb_k(B) ≥ (1 − O(η))c_E‖dB‖² ≍ ε²|Λ_k| (in a regime where the linearisation applies), while δ_{k,T} is the
energy of a localised defect. The compactness condition E^cb_k(B) < δ/2 therefore fails once |Λ_k| ≳ δ/ε²: no argument of this
global type can be uniform in T. A uniform proof has to be local: a chain that leaves the gauge-saturated chart near x must be shown
to have local energy above the local critical energy by a definite amount. The local comparison I can see (cut and paste on a
collar) needs a priori local closeness of the minimiser to Z_k(B) on the collar (SF's (MIN-reg)), a localised version of Corollary
MARGIN, and an ε-regularity statement "small local energy ⇒ every level small in a local gauge" (HIST's (AE), reduced there to
(MS-Sob)/(SQ-dev), OPEN at P-scale). I do not claim this is the only route.

### 5.3 Counterexample search (a small-field datum whose global minimiser leaves the chart) — none found
- *Flat data with holonomy (torons, constant fields).* Excluded exactly by Proposition FLAT.
- *Twisted chains* (fine holonomies differing from the top's): excluded at flat data by FLAT (i); at small non-flat data a twist must
  be absorbed by soft residuals along every coarse cycle that carries it, a definite positive cost [argued, not proven].
- *Centre-vortex sheets at an intermediate level j.* The (j → j+1) kernel can vanish at a vortex (φ_M(V) = 0 iff V = W_0(M), even for
  non-unitary M̄), but a vortex at level j is incompatible with following a smooth level j − 1 unless it is pushed down to level 0,
  where each pierced plaquette costs Re tr(1 − e^{2πi/N}) = N(1 − cos(2π/N)) > 0: a definite cost per unit area against an O(ε²)
  energy density [argued].
- *Gribov copies.* Copies of Z_k(B) in other gauges are the same orbit, not other minima.
- *LCONV55's stripe.* It lies in 𝒦_{R_M} (links ≤ β in the global gauge) above trivial data, where E^cb_k = 0 < its energy; it is a
  non-convexity witness for the multiscale measure (Theorem NC), not a competitor for the minimum, and Theorem RSM-tower (a) already
  covers it.
Verdict on uniform (MIN-cb): **OPEN** (no proof, no counterexample), and — by §2-§4 — **not consumed** by any reader once the
critical-value restatement and the restricted minimum are used.

---

## 6. T3 — The CODEX_REVIEW_BFT4B bridge: global critical-value polymers vs the localised-minimiser densities of (I_k^E)″

**The question** (CODEX_REVIEW_BFT4B, "Single most dangerous unverified bridge: identifying the bounded localization of the global
composite critical value with the gauge-invariant, centered-norm-controlled polymer class and assigned localized-minimizer densities
of (I_k^E)'', on its whole domain"). The two objects: BFT4a-glob's connected polymers R_X of E^cb_k (a decomposition of the global
total on the torus; R_X signed; BFT4W55 "Theorem BFT4a-glob", conditional on (R)); and HIST's densities 𝓔^{an}_{k,x} := "the 𝒞^♭-terms
assigned to x by the lexicographic rule of (a′), evaluated on the branches" of the minimiser of a FREE-BOUNDARY localised energy on Λ_k.

### 6.1 Proposition DENS (the critical-chain densities) — (a), (b), (d) PROVEN-HERE as implications; (c) ARGUED
For real B with ‖B‖_D ≤ ε_0 and x* := Z_k(B) (In-A), and each level-k cube x, let 𝒯(x) be the chain terms (level-0 plaquette terms of
S_W and soft terms κ_iφ̂_c) assigned to x by HIST's rule ("each term goes to the level-k cube of the level-k ancestor of its
lexicographically first vertex"), and put **𝓔^cb_{k,x}(B) := Σ_{t∈𝒯(x)} t(exp x*(B); e^B).**
- (a) Σ_x𝓔^cb_{k,x} = E^cb_k; each 𝓔^cb_{k,x} ≥ 0 on real B (every term is); each is holomorphic on BFT-2's polydisc (finitely many local
  holomorphic terms, In-F, composed with the holomorphic x*(B)).
- (b) **0 ≤ 𝓔^cb_{k,x}(B) ≤ C_dens·η², η := C_0‖B‖_D,** with
  **C_dens := 3N(2 + 9η)² + 4κ_+(1 + 2δ_ρ)[1/(1 − L^{−2σ}) + C_ρ²η²L^{−6}/(1 − L^{−2})]**, uniform in k and T, for every σ ∈ (0, 1]
  (δ_ρ := 9.2y² + e^{|ρ|}|ρ|√N/3, small on the BFT-E ball; C_ρ BFT-1 (1b)'s second-order constant).
- (c) [ARGUED, given BFT34_55 Lemma WD, i.e. given (H1), (H2)_m, (H3)_m] |∂𝓔^cb_{k,x}/∂B_y| ≤ C_locη e^{−m′d(x, y)}, uniformly in k, T.
- (d) For ‖B‖_D ≤ ε_att, x* is the minimiser of 𝔉_k(·; e^B) over 𝒦^{(k)}_{R_M}, unique modulo composite gauges (RSM-tower), and every
  term is composite-gauge invariant (In-E); so **𝓔^cb_{k,x} are the assigned densities of THE restricted minimiser** — no measurable
  selection is needed (the property HIST A5 (C) obtains from (a5-U)).
*Proof of (b).* *Level 0:* the terms assigned to x have their first vertex among the L^{4k} level-0 sites of x, so there are ≤ 6L^{4k}
of them (six plaquette orientations per site at d = 4); Re tr(1 − e^X) = Σ_j(1 − cos θ_j) ≤ |X|²_HS/2 and BFT-1 (1a) gives |log U_p| ≤
L^{−2k}(2η + 9η²) (a factor N covers an operator-norm reading), so level 0 contributes ≤ 6L^{4k}(N/2)L^{−4k}(2η + 9η²)² =
3N(2 + 9η)²η². *Level i:* the soft terms with base root in x number ≤ 4L^{4m}, m := k − 1 − i; NA-alg (b) gives
κ_iφ̂ = κ_iNφ ≤ κ_+|ρ|²(1/2 + δ_ρ); BFT-1 (1b) gives |ρ_i| ≤ L^{−(2+σ)m}η + C_ρL^{−3(m+1)}η²; with (a + b)² ≤ 2a² + 2b² the level-i sum is
≤ 4κ_+(1 + 2δ_ρ)[L^{(4−2(2+σ))m}η² + C_ρ²L^{4m−6(m+1)}η⁴], and Σ_{m≥0} gives the bracket. ∎ **The transport weight σ > 0 is load-bearing:**
at σ = 0 the level-i contributions do not decay and the bound grows like k (mc55_1 checks the exponent bookkeeping and the σ = 0
growth exactly).
*Why (c) is only ARGUED.* Bounding ∂t/∂B_y through the potential response (own |∂x_j(b)/∂B_y| ≤ C_1L^{−(k−j)}e^{−m·dist}) loses: at level
0 it gives L^{4k}·L^{−2k}η·L^{−k} = L^kη. The uniform bound needs the chain rule through the gauge-invariant outputs (plaquette logs
and residuals, whose responses Lemma WD bounds by L^{−2(k−j)} resp. L^{−(2+σ)(k−1−j)} times e^{−m·dist} — its sentence "the same for
every gauge-invariant output carried by 𝔐^{(σ)} (f_j, r_j)"), which gives L^{4k}·L^{−2k}η·L^{−2k} = η at level 0 and L^{−2σm}η at level
i; I have written this term by term only for the leading (linear) parts, not for the BCH corrections of log U_p and of ρ − r.

### 6.2 Verdict on the bridge
1. **As an identity of objects: not supplied, not true by construction, and not needed.** R_X/|X| and 𝓔^{an}_{k,x} are two different
   localisations; even where their totals agree (on the torus, if the infimum equals the critical value), equality of totals says
   nothing about the pieces. I agree with CODEX_REVIEW_BFT4B R4 ("the input gives a bounded localization of the **global** critical
   value. The consumer transfer has status **GAP**") and R9 ("equality of the sum over x to the action does not identify each new
   sum_X R_X/|X| with the particular assigned critical-chain density E_{k,x}").
2. **What (I_k^E)″ needs from its main-term densities, and what DENS supplies on 𝒞_glob (torus, global smallness):** positivity and a
   uniform per-cube bound (for (c4)) — **supplied** ((a), (b)); holomorphy on a uniform domain — **supplied** ((a)); "THE minimiser" —
   **supplied in the restricted sense** ((d)); first-derivative exponential locality — **ARGUED** ((c)); β = 1 in the bulk — germ level
   (ASSEMBLY C5a; CODEX_REVIEW_ASSEMBLY R6), infinite volume (JET-∞) OPEN.
3. **What remains OPEN and is not touched here:** the free-boundary localisation on Λ_k with large-field holes and (a4)'s boundary
   locality (no BFT-E, NSL, K-U or ID on regions: the same leaf as REVIEW_S22's "non-wrapping box", OFFGLOB55 and LARGE55's I1);
   SF's (L-loc)_k for these densities (a strictly local decomposition with all mixed derivatives; BFT34_55 Proposition CX shows that
   analyticity plus n ≤ 4 locality do not give it, so a BFT-4-type construction applied to the densities is needed — this, and only
   this, is where BFT4a-glob's polymer machinery would enter).
4. **Restated bridge (the one that should replace "the most dangerous" one in the work list):** *(DENS-reg)*: the critical-chain
   densities of Proposition DENS, constructed for the free-boundary critical chain on a region Λ_k with holes, with (a)-(d) uniformly
   in k, T and the region. Its torus case is (a), (b), (d) PROVEN-HERE (conditional on the banked BFT-E/NSL/ID chain) and (c) ARGUED.

---

## 7. Check record (criteria written and hashed before every script; exact rational arithmetic; exit 0, empty stderr)
All three criteria files were written together at 2026-10-29T06:05:18Z (sha256 below), before any mc55 script existed.

**mc55_1 — level sums of Proposition DENS (b).** `checks/mc55_1_criteria.md` (6c3f3ed5…) → `checks/mc55_1_levelsum.py` (91348568…,
06:05:34Z) → `checks/mc55_1_out.txt`. **PASS.** G1: for L ∈ {3, 5}, σ ∈ {1, ½} and every k ≤ 200, A_k ≤ 4/(1 − L^{−2σ}) exactly and
strictly increasing (limits 9/2, 6, 25/6, 5); G2: L^{4m}L^{−2(2+σ)m} = L^{−2σm} exactly (m ≤ 60); G4: 6L^{4k}(L^{−2k})² = 6. Controls
fired: σ = 0 gives A_200 = 800 > 400 (C1); the d = 5 count mutant gives A_200 = 800 > 6 (C2). *Scope:* arithmetic of the level
sums only; BFT-1's bounds and NA-alg (b) are inputs, not checked.

**mc55_2 — quintic tents (Lemma GI_j's lift).** `checks/mc55_2_criteria.md` (5fd01321…) → `checks/mc55_2_tents.py` (d7f4bc1f…,
06:05:59Z) → `checks/mc55_2_out.txt`. **PASS.** σ_5(t) + σ_5(1 − t) ≡ 1; C² gluing at 0 and 1; σ_5′ ≡ −30t²(1 − t)²; sup|σ_5′| = 15/8
(identity 15/8 − |σ_5′| = 30(t − ½)²(¼ + t(1 − t))); σ_5‴ ≡ −60(6t² − 6t + 1) and (σ_5″)² ≡ 100/3 modulo that quadratic, so sup|σ_5″| =
√(100/3) < 289/50; sup|σ_5‴| = 60; interpolation χ(n) = δ_{n0}; blend constant C_blend = 2⁴·60·4 = 3840. Control fired: the cubic
smoothstep satisfies the partition identity but has σ_3″(1) = 6 ≠ 0, so the C² gate FAILS for it (the partition identity alone
could not have discriminated). *Scope:* the 1-D facts and the product-rule constant; the claim ‖ξ̃‖_♮ ≤ C_χ|ξ|_{C¹} also uses that
discrete difference quotients are bounded by continuous derivatives (mean value theorem), not checked.

**mc55_3 — Lemma LIFT_j's counting on exact SU(2) configurations.** `checks/mc55_3_criteria.md` (1ac2bd1f…) →
`checks/mc55_3_lift.py` (5d0a8e13…, 06:07:27Z) → `checks/mc55_3_out.txt` (5.3 s). **PASS.** d = 3, L = 3, 6³ torus; four random
gauged instances (ε′ ≈ 1.08-1.28·10⁻⁴) and one aligned instance (ε′ ≈ 2.0·10⁻⁵): L1 (axial gauge exact on tree links), L2 (ladder
bound |U^h_b − 1| ≤ r(b)ε′, r(b) ≤ 2), L3 (contour comparison ≤ n_Lε′, n_L = 144), L4 (|W_0(M̄_c) − T_b| ≤ 1.7√2 n_Lε′ with W_0 = M̄/|M̄|
for SU(2), |M̄| enclosed rigorously; NA-alg regime 1.04√2 n_Lε′ ≤ 1/20) hold on all five; controls fired on the aligned instance
(undersized ladder r − 1; n_L → 1), and in fact on all five. **Post-run diagnostic, disclosed, not pre-registered**
(`checks/mc55_3_diag.py` → `checks/mc55_3_diag_out.txt`): the ladder gate L2 is **attained** (max |U^h_b − 1|²/(r²ε′²) = 1.0000 on
both instances shown), so it is discriminating; the contour gate L3 is loose (max |T_b − T_contour|/ε′ = 2.38 random, 4.00 aligned,
against 144), so mc55_3 can only expose an n_L error by more than a factor ≈ 36; the bound itself rests on the cone proof of
Lemma LIFT_j (a). *Scope:* d = 3 rather than d = 4 and N = 2; finitely many instances.

---

## 8. Findings, claim by claim (verdict; file + locating string; reason)

### 8.1 Inherited claims touched by this file
- **F-1 ASSEMBLY55 C5b, verdict "MISMATCH (object + class)" — CONFIRMED.** The consumers' texts (FLOW "Def F-strip", "(SF-bg)";
  HIST "(a″) Main term"; PLD "fixes 𝔟(V) := the minimiser") read the min-tower on uniform/local domains, and no banked statement
  identified it with E^cb there (§2).
- **F-2 ASSEMBLY55 C5b, "Positivity, the one min-property used on that domain, survives (ii) for free" — REFUTED** (§4.5). Correct:
  positivity and every lower bound survive (Lemma CV); the restricted minimum over the consumer's chart is also used (M3 (iii), M6,
  M10, M11, M13) and is Theorem RSM_j / Corollary RSM_j-class.
- **F-3 ASSEMBLY55 C5b, "Where HIST compares with large fields ((CLS-NA)), the min definition is genuinely used and (i) is needed"
  — REFUTED as to "(i) is needed"** (§4.5): (CLS-NA)/(CLS-min) are lower bounds for every chain; (MIN-cb) neither implies nor is
  needed for them.
- **F-4 ASSEMBLY55 C5b/ML6, "(MIN-cb) [OPEN] … it contains (a5-U) and (MIN_1)" — CONFIRMED** (a global identification contains the
  restricted ones; still OPEN, §5) — with the new reading that it is **off the critical path**.
- **F-5 HIST "(c5″) … The Laplace step of (SF^J) needs the critical point to be the global minimiser of the real exponent" —
  REFUTED as a necessity claim** (§4.4); correct form: criticality + N5 + a quadratic lower bound on the integration chart + pricing
  of the cut complement.
- **F-6 HIST Theorem A5 (D) "every real critical value dominates the infimum" — CONFIRMED** (Lemma CV).
- **F-7 REVIEW_S22 "SF: BFT-1 (θ_w > 0), 2 (complex ball for (R♯)) and 5, giving (a5-G♯), (a5-U) and (MIN-reg)" — NOT-VERIFIED as to
  (a5-U) and (MIN-reg).** BFT-0..5 are uniqueness/estimate statements in a ball; (a5-U)/(MIN-reg) quantify over every global
  minimiser. A local statement does not imply a global one without an input that puts the minimisers in the ball; that input is
  (MIN-cb)-type. What does follow (with this file) is the restricted form (RSM-tower; Corollary RSM_j-class).
- **F-8 PROOF "[R20-fix 13, optional] (MIN_1) weakened … Recorded as the target form; not proven" — target MET on 𝒞_glob,
  conditionally** (Corollary MIN_1-w). PROOF "E_1^NA := min_UF = E_1^br on 𝔅_1(ε_br) iff (MIN_1) holds" — CONFIRMED (logic), and no
  consumer requires E_1^NA (M11).
- **F-9 BFT34_55 Theorem BFT3-glob (E), the n = 1 bound "|∂E_k^br/∂B_y| ≤ C_E′" — CONFIRMED, and it uses (H1) only** (its proof text:
  envelope at the slice critical point, then Cauchy on the single top soft term). This is what Lemma GC (E) consumes; (H2)_m and
  (H3)_m are not needed for it.
- **F-10 NSL55 §4.0, "These are exactly the gauges under which w ↦ F_j(w, v) is invariant at fixed v" — REFUTED** (agree with
  CODEX_REVIEW_NSL F5). Re-derived witness: j = 0, v = 0, N = 2, the constant gauge c = diag(i, −i) ∉ 𝒢^rt_0 conjugates every plaquette
  and every S4′ transport, fixes V = 1, and maps the maximiser covariantly, so F^cb_0(w^c, 0) = F^cb_0(w, 0); on w = t·iσ_1 it acts as
  w ↦ −w. Correct: 𝒢^rt_j is a subgroup of the invariance group. Nothing in §3 uses the false characterisation.
- **F-11 CODEX_REVIEW_ASSEMBLY R6 (finite-chain germ) — CONFIRMED (agree);** its step-2 zero-orbit argument is generalised to every
  flat V in Proposition FLAT (i), and its compactness step is reused in Proposition MIN-fin.
- **F-12 CODEX_REVIEW_ASSEMBLY R7 ("positivity … is much weaker"; "(MIN-cb) … genuine OPEN sufficient bridge"; "Do not make uniform
  global minimizer identification a mandatory leaf") — CONFIRMED (agree)**, and sharpened: the restricted form is what the consumers
  use (§2), and it is now proven on 𝒞_glob as an implication (§3).
- **F-13 CODEX_REVIEW_BFT4B R4 and R9 (GAP for the literal transfer of BFT4a-glob's localisation to the assigned densities) —
  CONFIRMED (agree)** (§6.2 item 1).
- **F-14 FLOW "Def F-strip": "its Hessian at the trivial field is … H_k … (envelope theorem at a minimum that is nondegenerate on the
  gauge slice, N5-coer)" — CONFIRMED**: the identity holds at any nondegenerate critical point (Schur complement), so it holds for
  E^cb without (MIN-cb); at fixed k, T the minimum near 1 is that point (R6).
- **F-15 SF "(CE-Q^∞) … would need a local coercivity of the true action … which is not available" — status changed, not refuted:**
  the chart part is supplied by Corollary MARGIN (conditionally); the conversion to SF's slice is NOT-VERIFIED; the beyond-chart part
  stays OPEN (§4.2).
- **F-16 LARGE55 "(BFT-coer) — the only new nonlinear input (OPEN, s …)" — CONFIRMED as OPEN,** with a new exact remark: the naive
  perturbative route E^cb ≥ (1 − Cη)E^lin fails for small non-abelian pure gauges (E^cb = 0 by Proposition FLAT, E^lin > 0 by E-low),
  so (BFT-coer) must be proven with local gauges (§4.3).
- **F-17 LCONV55 Theorem NC — spot-checked for compatibility only, not re-verified:** its negative directions are following
  directions with free coarse levels (Lemma FOL); RSM_j fixes the coarse field. No conflict.
- **F-18 Lemma N5-coer — used as an input; NOT-VERIFIED here as to NA-lev (c)'s constant c_1** (frozen package; structure re-read and
  agreed; REVIEW_S18_S19 CONFIRMED; CODEX_REVIEW_GSHARP F9 acknowledges it). Only γ_min > 0 and its level-uniformity are used.

### 8.2 Results of this file (statuses; all pending a Codex check, nothing banked)
- **N-1 Census M1-M16 (§2)** — readings with reasons; answer to T1: no consumer needs global minimality.
- **N-2 Lemma CV** — PROVEN-HERE. **N-3 Lemma HL** — PROVEN-HERE (elementary). **N-4 Lemma GC** — PROVEN-HERE ⇐ In-A, In-E, In-F.
- **N-5 Lemma ANG** — PROVEN-HERE ⇐ In-D, In-I (C_dΛ finite, not evaluated).
- **N-6 Lemma GI_j** — PROVEN-HERE ⇐ In-A, In-B, In-C, In-E, In-H, In-J (mc55_2 for the tent facts).
- **N-7 Theorem RSM_j** — PROVEN-HERE as an implication of In-A … In-J; uniform in j, k, T; 𝒞_glob, tori, real data.
- **N-8 Lemma LIFT_j** — PROVEN-HERE (elementary; mc55_3). **N-9 Corollary RSM_j-class** — PROVEN-HERE as an implication.
- **N-10 Theorem RSM-tower (a)-(c)** — PROVEN-HERE as an implication (radius does not grow with depth).
- **N-11 Corollary MIN_1-w** — PROVEN-HERE as an implication (+ E1 for PROOF's convention).
- **N-12 Corollary MARGIN** — PROVEN-HERE as an implication. **N-13 Proposition FLAT** — PROVEN-HERE ((i) elementary; (ii) via
  TOWER-VAR (b) and RSM-tower). **N-14 Proposition MIN-fin** — PROVEN-HERE as an implication (non-uniform in k, T by design).
- **N-15 Proposition DENS** — (a), (b), (d) PROVEN-HERE as implications; (c) ARGUED (given Lemma WD). mc55_1 for (b)'s level sums.
- **N-16 Remark §4.3** — PROVEN-HERE (exact counterexample to the naive perturbative coercivity).
- **N-17 (MIN-cb), uniform** — OPEN; no counterexample (§5.3); not consumed after the restatement.
- **N-18 Bridge verdict (§6.2)** and the new named item **(DENS-reg)** — OPEN (region case); torus case as in N-15.

### 8.3 Summary table
| # | Claim | Verdict / status | Where |
|---|---|---|---|
| F-1 | ASSEMBLY C5b MISMATCH | CONFIRMED | §2, §4.5 |
| F-2 | "Positivity, the one min-property used" | **REFUTED** | §4.5 |
| F-3 | "(CLS-NA) … (i) is needed" | **REFUTED** | §4.5 |
| F-4 | (MIN-cb) contains (a5-U), (MIN_1); OPEN | CONFIRMED (now off the critical path) | §5 |
| F-5 | HIST (c5″) "global minimiser" needed | **REFUTED** (necessity) | §4.4 |
| F-6 | HIST A5 (D) | CONFIRMED | §3.1 |
| F-7 | REVIEW_S22 "BFT … giving (a5-U) and (MIN-reg)" | NOT-VERIFIED (does not follow) | §8.1 |
| F-8 | PROOF (MIN_1) weakened (target) | target met on 𝒞_glob, conditional | §3.10 |
| F-9 | BFT3-glob (E) n = 1 from (H1) only | CONFIRMED | §3.3 |
| F-10 | NSL55 "exactly the gauges …" | **REFUTED** (agree Codex NSL F5) | §8.1 |
| F-11 | Codex ASSEMBLY R6 | CONFIRMED (agree) | §5.1, §5.2 |
| F-12 | Codex ASSEMBLY R7 | CONFIRMED (agree) | §2 |
| F-13 | Codex BFT4B R4, R9 | CONFIRMED (agree) | §6.2 |
| F-14 | FLOW Def F-strip Hessian identity | CONFIRMED | §8.1 |
| F-15 | SF (CE-Q^∞) "not available" | reduced: chart part supplied (cond.); slice change NOT-VERIFIED | §4.2 |
| F-16 | LARGE55 (BFT-coer) OPEN | CONFIRMED OPEN (+ naive route fails) | §4.3 |
| F-17 | LCONV55 Theorem NC | spot-checked: compatible | §3.6 |
| F-18 | N5-coer constant c_1 | NOT-VERIFIED (input; structure agreed) | §3.0 |
| N-2…N-6 | Lemmas CV, HL, GC, ANG, GI_j | PROVEN-HERE (implications) | §3.1-3.5 |
| N-7 | **Theorem RSM_j** | PROVEN-HERE as implication | §3.6 |
| N-8, N-9 | LIFT_j; RSM_j-class | PROVEN-HERE | §3.7-3.8 |
| N-10 | **Theorem RSM-tower** | PROVEN-HERE as implication | §3.9 |
| N-11 | **MIN_1-w** | PROVEN-HERE as implication | §3.10 |
| N-12…N-14 | MARGIN; FLAT; MIN-fin | PROVEN-HERE | §4.1, §5.1, §5.2 |
| N-15 | DENS (a), (b), (d) / (c) | PROVEN-HERE / ARGUED | §6.1 |
| N-16 | naive coercivity fails | PROVEN-HERE (counterexample) | §4.3 |
| N-17 | uniform (MIN-cb) | OPEN, not consumed | §5 |
| N-18 | (DENS-reg) | OPEN (region case) | §6.2 |
| checks | mc55_1, mc55_2, mc55_3 | PASS (controls fired; mc55_3 L3 loose, disclosed) | §7 |
Counts on inherited claims: **CONFIRMED 10** (F-1, F-4, F-6, F-9, F-11, F-12, F-13, F-14, F-16, plus F-8's logical part),
**REFUTED 4** (F-2, F-3, F-5, F-10), **NOT-VERIFIED 2** (F-7, F-18); F-15 status changed; F-17 spot-checked only.

---

## 9. Codex verdicts used — agree or disagree (files as on disk at 05:0x-06:1xZ)
- **CODEX_REVIEW_ASSEMBLY R6** (finite-chain germ CONFIRMED; uniform radius and infinite volume NOT-VERIFIED) — **agree.** I
  re-derived steps 1, 2 and 4 in the form used here (Proposition FLAT (i) generalises step 2 to every flat V; MIN-fin reuses step 4).
  The −3 exchange coefficient of its E″″ identity is not used and was not re-derived.
- **CODEX_REVIEW_ASSEMBLY R7** ("positivity of a critical value is much weaker than its minimizing property"; "(MIN-cb) … genuine OPEN
  sufficient bridge"; the restricted small-field form as an alternative) — **agree**, sharpened in §2 (the consumers use exactly the
  restricted form) and §3 (proved on 𝒞_glob as an implication).
- **CODEX_REVIEW_ASSEMBLY work-list item 8** — answered by this file: the second option ("consistently use critical values and prove
  the restricted-small-field minimum and large-field comparisons needed by the chosen alternative"), with the finding that the
  large-field comparison needed is not a chain-energy comparison but (BFT-coer)/MIS pricing (§4.3).
- **CODEX_REVIEW_BFT4B R4, R9** (GAP for identifying BFT4a-glob's localisation with the assigned densities) — **agree.** **R5**
  (bounded holomorphy gives no derivative bounds up to the boundary; use interior radii) — **agree**, and respected: Lemma HL works
  on P_{R/4}. Its closing "single most dangerous unverified bridge" — **agree that it is unverified**; §6 replaces it by (DENS-reg).
- **CODEX_REVIEW_NSL F3** (Lemma SC (b)'s scalar inequality false, bound repaired) — agree; I use only Lemma SC (c) directly.
  **F5** (𝒢^rt_j is not the whole invariance group) — **agree**, witness re-derived (F-10). **F6** (real NSL CONFIRMED; holomorphy only in
  the scaled norm) — **agree**, and respected (§3.0 In-B). **F7** (Theorem ID CONFIRMED as conditional) — agree; my Lemma GI_j runs F7's
  (I3)-converse mechanism at a general datum.
- **CODEX_REVIEW_GSHARP F9** (N5-coer establishes the one-level inequalities for each i) — **agree** (structure re-read).
- **CODEX_REVIEW_FLOW55 §1.2** ("the exact normalized-kernel exponent must be the φ-tower, not FLOW's literally defined k̃-tower";
  identification with the k̃-tower at arbitrary backgrounds NOT-VERIFIED) — **agree**; the critical-value restatement uses φ̂ and so
  removes the k̃ question for M1-M3.
- **CODEX_REVIEW_LARGE F1** (the U-dependent normaliser log𝒩 must be kept in the soft action) — **agree with the structural point**
  (its SU(2) witness not re-derived); §4.2 treats log𝒩 as a u-free perturbation of the u-carrying main term. **F2** (MIS a valid tail
  bound; its advertised interface GAP) — agree as far as used. **The file is unfinished on disk** (ends after F6; no summary table,
  no bankable section, no route verdict).
- **CODEX_REVIEW_KOFF item 5 / CODEX_REVIEW_GV** — not re-read; used only through PROOF's [S26-BANKED] lines for Theorem K^(σ) and
  Proposition GV-E (status CONDITIONAL there).

---

## 10. For the lead (nothing here is banked; Codex first)

**What should change (proposed; the lead edits):**
1. **ASSEMBLY55 ML6 / Codex work-list item 8 / HANDOFF:** (MIN-cb) leaves the critical path. Replace it by
   (a) the critical-value restatement of the min-tower readers — FLOW "Def F-strip"/"(SF-bg)"/"(SF-g)_k" with 𝒯_k := E^cb_k/N and Φ :=
   the BFT-E point (so (SF-bg) ⇐ BFT-2 + BFT-3 on 𝒞_glob), HIST (I_k^E)″ (a″) with main term E^cb and densities 𝓔^cb_{k,x}
   (Proposition DENS), PLD's 𝔟(V) := U^cb_k(V) — editorial, with the producers named;
   (b) Theorem RSM_j / Corollary RSM_j-class / Theorem RSM-tower / Corollary MIN_1-w (this file; PROVEN-HERE as implications of the
   banked-conditional BFT-E/NSL/ID chain plus N5-coer) — **needs a Codex check**;
   (c) the region (boxes, holes) versions of BFT-E, NSL, K-U, ID and (DENS-reg) — to be merged into the existing OPEN leaf "BFT off
   𝒞_glob + boxes" (ASSEMBLY55 OPEN-list item 5; LARGE55 I1; OFFGLOB55), not a new wall.
   Uniform (MIN-cb) stays OPEN as a statement, off the path.
2. **HIST (a5-U), (a3-q), SF (MIN-reg), Proposition U-red, and Theorem A5's use of (MS-Sob)** are not needed to define the main term
   once (a) is adopted (on 𝒞_glob). (a5-G♯) stays (SF's N5 needs Hessian bounds at the critical chain).
3. **PROOF (MIN_1):** the "[R20-fix 13] weakened" target is met on 𝒞_glob (conditional); E_1^NA has no consumer.
4. **CODEX_REVIEW_BFT4B's "most dangerous bridge":** replace by (DENS-reg) (§6.2 item 4); its torus case is DENS (a), (b), (d)
   (conditional) and (c) ARGUED. BFT4a-glob's polymers are needed for polymer-class statements (SF (L-loc)_k, N5 via Cauchy), not to
   define the main term.
5. **SF (CE-Q^∞):** record the chart part as supplied (Corollary MARGIN), the slice-change constant as NOT-VERIFIED, the beyond-chart
   part as OPEN.
6. **Text corrections** (findings F-2, F-3, F-5, F-10): ASSEMBLY55 C5b's two sentences; HIST (c5″)'s "global"; NSL55 §4.0's "exactly
   the gauges" (already flagged by Codex NSL F5).
**PROOF.md tally:** no change proposed (every new item is a lane-level implication pending Codex; none closes a tally item).
**Critical path after this file:** the min-tower item reduces to the region leaf that was already on the path; on 𝒞_glob it is closed
modulo Codex on §3. The large-field side is unchanged: (BFT-coer) (LARGE55 I2) remains the open nonlinear input, and §4.3 adds
that its naive perturbative proof fails.

---

## 11. Errata and one addendum (found on a full re-read at 2026-10-29T06:14:03Z; append-only — each item overrides the text it names)
- **E1 (§2, "Answer to T1").** Read: "… **five** need a **restricted** minimum with a quadratic margin on their own small-field chart
  (M3 (iii), M6, M10, M11, M13), and M13 needs that margin quantitatively." ("four … and one of those" was a miscount.)
- **E2 (§3.6, constants).** ε_M must also satisfy **ε_M ≤ min(r_N, 21L³ρ_M, Lε_GI)/C_0′**, so that NSL applies to U^cb_j(v) in Step 2
  (‖U^cb_j(v)‖_{T;v} ≤ C_0′ε_M ≤ r_N), its slice gauge obeys |ξ_*|_{C¹} ≤ c_♮2C_ΛC_0′ε_M ≤ δ_GI, and Lemma GI_j applies at U^cb_j(v)
  (‖U^cb_j(v)‖_D ≤ C_0′ε_M/L ≤ ε_GI). All are fixed-constant conditions; nothing else changes.
- **E3 (§5.2, "Non-uniformity is real").** The sentence "E-low gives E^cb_k(B) ≥ (1 − O(η))c_E‖dB‖²" contradicts §4.3's remark (that
  comparison with E^lin fails in general) and is withdrawn. The extensivity lower bound of E^cb_k is **ARGUED**, not proven (it is
  (BFT-coer)-type; for data in one abelian direction, where log V_P = dB(P) exactly, it is E-low up to perturbative corrections
  [argued]); so the claim that the compactness route cannot be uniform is **ARGUED**. The "local proof needed" reading is unchanged.
- **E4 (§3.10 (ii)).** The hypothesis "once ε_E1 is also small enough that BR1 (iii)'s plaquette and residual bounds are ≤ ε′_M" is
  unnecessary: Proposition E1 gives U(V) ∈ 𝒢^{(1)}·Z_1(v), Z_1(v) ∈ 𝒮_0(v; ε′_M) (it is small), and 𝒮_0(v; ε′) is 𝒢^{(1)}-invariant
  (plaquette norms are gauge invariant; M̄_c(U^g) = M̄_c(U) for g = 1 at the level-1 roots); so U(V) ∈ 𝒮_0(v; ε′_M) for ‖v‖_D ≤
  min(ε_M, ε_E1), and (ii) follows from (i).
- **E5 (§4.1, second sentence).** The constant /97 holds for plaquette holonomies only. For a soft residual the factor 4 becomes the
  residual's Lipschitz constant in the links, ≤ 2ℓ_c(1 + O(y)) with ℓ_c := d(L − 1) + L the contour length and Lip(W_0) ≤ 2 near 1
  (NA-alg (a) gives 1 + O(y)), so the excess is ≥ γ_Mτ²/(20ℓ_c²) — **ARGUED** (the Lipschitz constant of W_0 is not written out).
- **E6 (§4.2).** "a product of per-link Gaussian factors, i.e. Z-local in the required sense" holds in slice coordinates
  ((e^AU)_S − w_*); Z-locality in SF's fluctuation coordinates is only after the slice change listed under "Not supplied (1)".
- **E7 (§1, min-tower dictionary).** "𝒯_k − 𝓔_k = κΣd(M̄) ≥ 0" is imprecise; read **0 ≤ 𝒯_k − 𝓔_k ≤ κΣ_{i,c}d(M̄_c(U*_i)) at 𝓔_k's
  minimiser chain U*** (HIST Lemma HF's "Consequence").
- **E8 (§2, M1).** "CODEX_REVIEW_FLOW55 item 2" — the text on disk is its §1.2 ("Every-background normalization — REFUTED under the
  literal cited k̃ convention"); ASSEMBLY55 C5a calls it item 2.
- **E9 (§2, M12).** "(§8, finding F-9)" should read "(§8, finding F-7)".
- **E10 (§1, ‖·‖_D).** BFT_A writes ‖B_k‖_D := sup|B_k| without naming the matrix norm here; if it is the operator norm rather than HS,
  the √N factors in R_E (Lemma GC) and in LIFT_j (iii) shift by at most √N. No conclusion changes.
- **Addendum A1 — Corollary UB (exact upper bound) — PROVEN-HERE as an implication.** For real B with ‖B‖_D ≤ R_M:
  **E^cb_k(B) ≤ S_W^{(k)}(e^B) := Σ_{level-k plaquettes P}Re tr(1 − V_P).** *Proof.* TOWER-VAR (b): the composite lift Z^lift has all soft
  fluctuations zero and level-0 plaquettes equal to 1 except one corner plaquette per coarse plaquette, with holonomy V_P; so
  𝔉_k(Z^lift; e^B) = S_W^{(k)}(e^B). Its links are 1 or V_c in the global gauge (Lemma U0), so Z^lift ∈ 𝒦^{(k)}_{R_M}; Theorem
  RSM-tower (a). ∎ The analogous bound E^min_k ≤ S_W^{(k)} is trivial (Z^lift is a competitor); its transfer to the critical value is
  exactly what the restricted minimum buys. (It is an upper bound, so it does not touch (BFT-coer).)

- **E11 (2026-10-29T06:14:33Z) — Addendum A1 (Corollary UB) is WRONG as stated and is withdrawn.** Checked against PROOF "Lemma U0 (the exact lift)"
  (ii): "every fine plaquette of U^(0) has holonomy 1, except the block-corner plaquettes (x, μ, ν) with x_μ ≡ x_ν ≡ L − 1 (mod L),
  whose holonomy is the level-1 plaquette holonomy V_P". For each coarse plaquette there are **L^{d−2}** such fine plaquettes (the
  transverse coordinates are free inside the block), so one lift step multiplies the Wilson action by L^{d−2}, and the composite lift
  gives **𝔉_k(Z^lift; e^B) = L^{(d−2)k}·S_W^{(k)}(e^B)**, not S_W^{(k)}(e^B). The correct (and k-dependent, hence useless for uniformity)
  consequence of RSM-tower (a) is E^cb_k(B) ≤ L^{(d−2)k}S_W^{(k)}(e^B). My sentence "one corner plaquette per coarse plaquette" was an
  unchecked reading of TOWER-VAR (b)'s plural "k-fold corner plaquettes". **Proposition FLAT (ii) is unaffected**: it uses only that
  every corner plaquette has holonomy V_P = 1 when V is flat, so 𝔉_k(Z^lift; V) = 0 whatever their number.

---

## Closing provenance
Written by claude-opus-5-5 (worker), 2026-10-29T06:15:01Z. Files written: this file; checks/mc55_1_criteria.md, mc55_1_levelsum.py, mc55_1_out.txt,
mc55_1_err.txt; mc55_2_criteria.md, mc55_2_tents.py, mc55_2_out.txt, mc55_2_err.txt; mc55_3_criteria.md, mc55_3_lift.py,
mc55_3_out.txt, mc55_3_err.txt; mc55_3_diag.py, mc55_3_diag_out.txt (post-run diagnostic, disclosed). No git. Nothing here is banked;
every PROVEN-HERE item is an implication of the named inputs and awaits a Codex check. After the errata, the verdict counts of §8.3
stand unchanged (Addendum A1 was never counted and is withdrawn by E11).
- **E12 (§7 header, "empty stderr").** checks/mc55_3_err.txt is not empty: it holds only the three timing lines of `/usr/bin/time -p`
  ("real 5.32 / user 5.29 / sys 0.01"), which writes to stderr. No Python warning or error was emitted; mc55_1_err.txt and
  mc55_2_err.txt are empty.
