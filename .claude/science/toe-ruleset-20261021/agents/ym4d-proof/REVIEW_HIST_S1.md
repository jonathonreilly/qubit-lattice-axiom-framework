# REVIEW_HIST_S1: hostile review of lane D session 1 (HIST.md: (H-pos) at bad cubes, multi-scale history (HIST))

Reviewer: an independent agent that wrote none of HIST.md or its checks. I edited no other file. No commits, PRs or pushes.

Inputs:
- REVIEW_S16_S17.md (format; G1-G4, fix R-7b, the strategic verdict) and REVIEW_S18_S19.md l.1-140 (R1/TS verdicts, F1,
  F2, G5, the N5 interface remark). HIST.md did not read REVIEW_S18_S19 (it lists only REVIEW_S16_S17 l.350-550).
- HIST.md (all 650 lines), HIST_LOG.md (all 30 lines).
- RLARGE.md §0, §1, §1A, §3-§6, §7.1-§7.4, §8.1-§8.5 in full (l.40-697).
- PROOF.md by grep/offset: Lemma CE-geo' (g1') l.2183-2200, (g3) l.1815, Lemma D4-norm l.1547-1565.
- LINEAR_PACKAGE.md §1.3 (Setting SC, l.76-90) and Lemma 2.7 E-low (l.149-155); checks/c31E.out (the E2 ratios HIST
  cites).
- checks/h1-h4: criteria, scripts, stored outputs, time files; all four re-run (below).

Scratch work (wrapper, re-run outputs) is in the scratchpad directory `revhist/`.

---

## Bottom line

- **The one-step kernel analysis is right and sharper than RLARGE's.** Lemma PM, Lemma KQ and Lemma RS-lin: CONFIRMED.
  I re-derived every inequality and constant.
- **Proposition CL^J (the joint frozen activity) is right as stated.** It is a genuine advance on R-7b. At stage k the
  level-(k+1) badness is priced by the normalised kernel K_k with U_k frozen, so no effective action is ever evaluated at
  a bad level-(k+1) cube, and the non-locality of S_k (its polymers E_k(X; U_k)) is genuinely frozen.
- **But the sentence that carries it into the induction is wrong.** HIST §2 (l.112-114) and the §4 Remark (l.240-242)
  say that the stage-k integrand depends on U_{k+1} "only through factors produced at stage k-1 near returned level-k
  defects". That is false once stage k-1's gas is exponentiated, which R1^J does:
  - every remainder ℛ^J_x of stage k-1, at every cube x, reads U_{k+1} on C(Y) for the clusters Y of x's box;
  - so is every re-extracted polymer of (W1-ret'^J).
  So J_k is never "explicit near B", and (H-Mayer) is not removed. It is replaced by a Mayer expansion over the whole
  lattice of SMALL two-field activities (size ≲ e^{-a''_J/g²} per cube). That is weaker than RLARGE's (H-Mayer), whose
  polymers are O(E_0), but it is global, not local to returned defects (fix H-1).
- **The (D1-c) argument is right, and it proves more than HIST says.** The Laplace link plus the non-constant c31 E2
  ratios kill every per-cube-bounded representation whose main term is the coarse Wilson action, on any domain that
  contains fields of size t with g ≪ t. That domain includes RLARGE's ε_1-small-field region Λ_k.
  - So the same argument refutes (I_k) on Λ_k in RLARGE's form, which RLF-step^J still assumes.
  - It also refutes the per-cube E_0 bound that HIST itself consumes in (P4) and in item (b) of (H-w)'s B_0.
  - HIST files this as a bracketed "[inference … not acted on]" and treats only fields of size g (l.372-375). That
    bracket has to be promoted to a named requirement on (I_k) (fix H-2).
- **Proposition CF and the (CLS-NA) wall: CONFIRMED, with a scope narrowing.** CF is an exact configuration. It shows
  that any bound pricing a bad level-k plaquette through O(1) mismatches or plaquettes per level fails beyond depth
  ~log(1/g)/log L, whatever the constants. That is a method limit, as claimed. Bounds that aggregate ≳ L^{4(k-j)}
  plaquettes (ℓ²/action sums, many-plaquette Peierls counts) are not excluded, and CF's cost is visible to them (fix H-8).
- **HIST-sum: CONFIRMED (CONDITIONAL on (H-w) and the lower half of (F)).** I re-did the entropy-vs-weight arithmetic.
  - Persistence costs e^{38416B_0} per configuration per level.
  - The flow gives L^{-naβ_-} per level, against L⁴ placements per level.
  - That gives n_H = ⌊(4 + 38416B_0/log L)/(aβ_-)⌋ and γ_H > 0 exactly as written.
  - Lemma H-geo is CONFIRMED.
  - The correction to RLARGE (P1) is real: RLARGE never charged its own boundary factors across levels.
- **The checks re-run identically** (h1-h4, all PASS). The criteria predate the scripts by 55-138 s.
- **Corrected tally (this file): 5 PROVEN-HERE / 2 CONDITIONAL / 6 ARGUED / 3 OPEN.** The claim was 6 / 4 / 4 / 3. The
  changes:
  - TS_K becomes an uncounted corollary.
  - (P4) and RLF-step^J are demoted to ARGUED: (P4) consumes the per-cube E_0 that H-2 refutes in the coarse-Wilson
    form, and RLF-step^J has unnamed gaps H-1, H-3 and H-4.
  - 0 counted items are GAP or WRONG. One uncounted sentence (§2 l.112-114) is WRONG.

---

## §2 Lemma TD and the stage-k integrand (l.98-114)

### Lemma TD: CONFIRMED (elementary)
- The top-down integration uses ∫K_i dU_{i+1} = 1 (D4-norm). The conditional law of U_{k+1} given U_{≤k} is Π_ck^{(k)}_c
  under the PLAIN chain measure. The caveat about history indicators (l.103-104) is honest.

### "G_k depends on U_{k+1} only through factors … near returned level-k defects" (l.112-114): WRONG (sentence; uncounted)
- Stage k-1 rewrites the level-k bad cubes as Z = Z_∅⟨Ξ^J_{k-1}⟩_cut, with Ξ^J_{k-1}(D) = Σ_BΠr^J_{Y_i}(D).
- r^J_Y is a function of the sample for EVERY cluster Y, including clusters where the sample is good. It reads U_{k+1}
  on C(Y), the level-(k+1) links with an endpoint block in Y (CL^J setting, l.173).
- Every level-(k+1) link has an endpoint block, so Ξ^J_{k-1} depends on all of U_{k+1}.
- R1^J then writes log Ξ^J_{k-1} = c-number + δβ^J_{k-1}Σs(U_{k-1}) + Σ_xℛ^J_x (l.269). The δβ term reads only U_{k-1},
  but every ℛ^J_x reads U_{k+1}. The re-extracted polymers of (W1-ret'^J) (l.539-542) are "polymers in (U_{k+1}, U_{k+2})"
  at every cube.
- The statement is true only for an individual term Z_B of the unexponentiated sum: its factor r^J_B reads U_{k+1} only on
  C(B). The induction does not keep that form (R1^J exponentiates).
- **Consequence:** CL^J (a)'s hypothesis "J_k explicit near B" fails for every B after stage k-1. CL^J (a)-(b) apply only
  after a Mayer expansion of all the stage-(k-1) U_{k+1}-dependent activities, jointly with the stage-k clusters.
- **Fix H-1.** Rewrite l.112-114, l.240-242 and (H-Mayer^J) (l.532-538):
  - (H-Mayer^J)_k: e^{Σ_xρ_x} with ρ_x := (every stage-(k-1) remainder, after the (W1-ret'^J) sea average, that reads
    level-(k+1) links), Mayer-expanded over the whole lattice jointly with the level-(k+1) clusters;
  - activities ≤ (Ce^{-a''_J/g_{k-1}²})^{#cubes}e^{-κ'd}, κ' > 3κ_0 + 3.
  - It is still weaker than RLARGE's (H-Mayer) (small activities, versus O(E_0)), and [s given (W1-ret'^J)] is a fair
    weight. "Only one earlier stage's … remainders near returned defects" must go.

## §3 Kernel positivity

### Lemma PM (l.122-136): CONFIRMED
- (1) Re tr(W_0⁻¹S) ≥ Re tr(W_0⁻¹M) - Nδ ≥ Re tr(S⁻¹M) - Nδ ≥ N - 2Nδ. So s ≤ 2δ, and by (B) ||W_0 - S|| ≤ 2√(Nδ).
- (2) |θ| ≤ (π/2)|e^{iθ} - 1| on [-π, π]. |Σθ_j| ≤ πN^{3/2}√δ < 2π iff δ < 4/N³, and δ_0 ≤ 2/N³. ||Y|| ≤ 1/8 iff
  δ ≤ 1/(64π²N) ≈ 1/(631.7N), and δ_0 ≤ 1/(640N).
- (3) Stationarity: ⟨X, W_0⁻¹M⟩ = -Re tr(XW_0⁻¹M) = 0 for X ∈ su(N), so P(W_0⁻¹M) = 0.
  - P(1) = 0, P(Y) = Y, ||P|| ≤ 2.
  - ||e^{-Y} - 1 + Y|| ≤ ½||Y||²e^{||Y||} ≤ 0.567||Y||².
  - Then ||Y|| ≤ 0.142||Y|| + 2δ, so ||Y|| ≤ 2.33δ.
- (4) ||e^Y - 1|| ≤ max|θ_j|. Right.

### Lemma KQ (l.138-149): CONFIRMED
- **Lower bound.** With U := V⁻¹W_0 and A := W_0⁻¹M, φ = N⁻¹Re tr((1 - U)A) = s(U) + N⁻¹Re tr((1 - U)(A - 1)), and
  ||1 - U|| = x. Right.
- **Upper bound.** For x ≤ 1/(4N) the angles are ≤ π/(8N), so X ∈ su(N). Stationarity removes the linear term, so
  φ ≤ e^{||X||} - 1 - ||X|| ≤ ||X||² ≤ (π²/4)x².
- **Global bound and (3.1).** These are D4-norm (2) verbatim.

### Lemma RS-lin (l.151-165): CONFIRMED (one wording fix)
- (a) δ ≤ A_dη_q ≤ δ_0, then PM.
- (b) x ≥ ε_1/8 - 3ε_1/(256N) ≥ ε_1/16. ||M̄ - W_0|| ≤ 4A_dη_q ≤ ε_1/(64N) ≤ x/(4N). Then φ ≥ x²/(4N) ≥ ε_1²/(1024N).
- (c) is RS (R2) with L²η < ε_1/2.
- Constants: at N = 2, ε_1 = 0.5, η_q = 8.68·10⁻⁵ and η_1 = 2.71·10⁻⁵. The ratio 2/ε_1 holds as ε_1 → 0.
- **Fix H-9 (wording, l.135-136, l.163-165, §10).** "Linear threshold" holds only for ε_1 ≤ 256Nδ_0 (= 0.4 for N = 2 and
  for N = 3). At the quoted ε_1 = 0.5 the ε_1-independent cap δ_0/A_d binds. The gain over RLARGE there is the factor 3.2
  in η, not linearity.
  - The binding exponent of the joint route is the plaquette branch a_η/81 ∝ η_q² (h4). Most of h4's 80-fold reduction of
    n_♯ comes from c_RS = 81 against 625, and the rest from η_q² against η_1².

## §4 Proposition CL^J (l.167-242): CONFIRMED-WITH-FIX

- **(a) Fubini.** The factor bookkeeping is right:
  - k^{(k)}_c for c ∈ int B;
  - k^{(k+1)}_{c'} for c' ∈ C(B), whose contours lie in the two endpoint level-(k+1) cubes of c';
  - F_k is free of level-(k+1) links; the χ_Q, Q ∉ B, read only int(Q).
  - The identity is exact *under its stated hypothesis* "J_k explicit near B". See H-1 for why that hypothesis fails in
    the induction.
  - **Fix H-6 (l.203-204).** "Den^J_B > 0 … simply continuity at the maximisers" is not a proof. Without quietness the
    maximisers need not make Q good. Use instead: U_{k+1} ≡ 1 on int(B) makes every interior plaquette 1, and the integrand
    is positive, so Den^J_B > 0 always.
- **(b) Factorisation.** For cube distance ≥ 2, a level-(k+2) link's two endpoints are adjacent, so it cannot touch both Y
  and Y'. Its contours stay in its two endpoint cubes, and those are not in Y'. Right.
- **(c) Size.**
  - *Numerator.* There are n_ℓ = 4L³(L - 1) choices per cube. Every c ∈ int Q has both endpoint blocks in R_k(Q). The 8
    C(Y) factors are bounded by their sup, ec_N⁻¹(κ/g_{k+1}²)^{N²-1} ≤ ec_N⁻¹(κ/g_k²)^{N²-1}. With the one integrated m_c
    factor this gives (ec_N⁻¹)⁹ and g^{-18(N²-1)}.
  - *Denominator.*
    - Caps of radius rg_k with r ≤ min{ε_1/32, 1/(4N)}, around a maximiser completion.
    - (i) gives χ = 1, using L²η_q + 4rg + 12A_dη_q < ε_1, which needs 12/(256N) ≤ 3/128 (N ≥ 2).
    - (ii) KQ (upper) gives ≥ e^{-3κr²}.
    - (iii) the ribbon bound for Ũ and p_Lrg give the exponent (3κ/2)[…] per c'.
  - *Ratio.* 12(1 + A_d)²ε°² ≤ 12ε_1²/(157²N) = ε_1²/(2054N) ≤ ε_1²/(2048N), so the exponent is a_J. The powers give p_J.
    All re-derived.
- **(d) Derivatives.** Λ^J_1 = 8κ(2 + C_𝒩): the multiplicity 8 (CL-1), back-tracking at most twice, D4-norm (3). Right.
- **(e) Invariance.** The chain gauge action restricts to nested block centres, and B_4 about a level-(k+1) cube centre
  preserves all three lattices (L odd). Right.
- **Remark l.237-242.** "CL^J (b) is exact: RLARGE's gap G1 does not arise at the frozen stage" is true for the S_k
  polymers. Those are functions of the frozen U_k. It is false for the U_{k+1}-dependent part of G_k (H-1). Rewrite as:
  "G1 is reduced to the Mayer expansion of small two-field activities, (H-Mayer^J)."
- **Priority 1 answer.**
  - CL^J never evaluates S_{k+1}, and S_k enters only as the weight of the frozen U_k. U_k is level-k small-field under the
    stage-k cut measure: the bad level-k cubes were rewritten at stage k-1, and the unreturned ones are outside Λ_k (Lemma
    H-nest (ii) for the activity collar).
  - U_k and U_{k+2} are genuinely frozen (Fubini over int(B) level-(k+1) links only).
  - (H-Mayer) is *reduced*, not removed.

## §5 GT-lat'', Lemma 7.2-0^J, Theorem R1^J, Corollary R1_Λ (l.246-300): CONFIRMED-WITH-FIX

- **GT-lat''.** GT-lat' uses only "a closed loop in the box bounds ≤ A(R_0) plaquettes", Ad-equivariance and the fact
  that B_4 maps straight segments to straight segments. None of these depends on the coarse-link length. Right.
- **Lemma 7.2-0^J.** Re-derived:
  - for c ∈ int Y, ||W_0 - S_c|| ≤ 3A_dε_2 (RS-lin (a));
  - ||1 - Ũ_p|| ≤ L²ε_2 + 12A_d(ε_2 + ε_V);
  - the c' telescoping ≤ 3LA_d(ε_2 + ε_V). This uses nested centred blocks: the straight level-k transporter of c' is the
    product of the S_c along it.
  - C_♭ = L² + 1 + (12 + 3L)A_d. Right.
  - **Fix (F1 of REVIEW_S18_S19, carried over).** The bracket "constants only" (l.280-281) needs the same one line as R1's
    F1: ε^J_♭(·; Y) is Lipschitz in tree coordinates on the chart ball, with constant C'(R^J_*), so a finite C^J_♮ exists.
- **R1^J substitution table.**
  - Every use R1's proof makes of CL (b)-(e), Lemma 7.2-0, locality and GT-lat' is supplied by the joint column.
  - Locality bound: n_cL² + (L² - 1)/2 + L² < (n_c + 2)L².
  - Wilson identification: 6L⁸ level-k plaquettes per cube, L⁸ base points per plane.
  - Torus: W cubes per direction.
  - Checked.
- **Status label (l.509, l.627).** "R1 proof [S18-repair, unreviewed]" is now stale. REVIEW_S18_S19 gives R1 and TS
  CONFIRMED-WITH-FIX (F1, F2). Cite it, so that nothing propagates as unreviewed. *This is not an overclaim:* HIST disclosed
  the inheritance, and the inherited input has since been confirmed.
- **R1_Λ: CONFIRMED, and it is more useful than HIST says.**
  - It is exactly the local-hypothesis R1 that REVIEW_S18_S19 G5 asks for ("R1-loc"), in the joint form, provided Λ' := the
    cubes whose boxes satisfy (H-ch)^J.
  - A sample-dependent Λ' is harmless: for x ∈ Λ'^{in} the functions 𝓖_S with S ∋ x, |S| ≤ n_c do not depend on Λ', and the
    Taylor step acts on the smooth r^J_Y.
  - Say this, and cite G5.
- **Cost not stated.** R1_Λ's δβ extraction is missing on the extraction collar of every collar-bad cube *inside Λ_{k+1}*
  (scattered in the sea with density e^{-c/g²}), not only near Ω^c. The cost is ≤ (2w_* + 1)⁴·12L⁸|δβ^J_k| per collar-bad
  cube, with w_* ~ n_c, so of order 10⁵n_♯⁴·C^J_*g^{-6}e^{-a''_J/g²}. It is small for g ≤ g_0(n_♯). It belongs in
  (W1-ret'^J), and should be listed there next to the other costs (l.317-325).

## §6 Outcome D1

### Theorem H-pos^J (l.304-325): CONFIRMED-WITH-FIX (uncounted corollary)
- (i)-(ii) are corollaries of CL^J and R1^J, with stage-independent constants. "(D1-a) holds at every level, in the joint
  form, uniformly in k" is right (frozen, under quietness and the ε^J_♭ hypothesis).
- **(iii), wording.** "Integrating U_k produces e^{-S_{k+1}} ONLY on the level-(k+1) small-field domain." After stage k the
  integrand carries ℛ^J and re-extracted polymers in (U_k, U_{k+1}, U_{k+2}). Integrating U_k produces a joint density of
  (U_{k+1}, U_{k+2}) on Λ_{k+1}, not a function e^{-S_{k+1}(U_{k+1})}.
  - **Fix H-3.** Name the needed form of the small-field step, (SF^J)_k: it integrates U_k with polymers in three levels and
    outputs two-field polymers. Put it in RLF-step^J step 5 and in §8's hypothesis list. In Balaban/Dimock it is routine
    for fine-coarse polymers, but RLARGE's (SF)_k is stated for a level-k density only.
- **"(H-pos)_k can be deleted" (l.316, l.562).** This is correct for the R-operation's activities. But the large-field cost
  of level-(k+1) defects has *moved*, not vanished. It is now carried by:
  - the kernel (proven);
  - (PLD-q)_k [s given SF];
  - (W1-ret'^J)(c) [s to P];
  - (H-w) [P].
  - **Fix H-10.** Say "(H-pos) is not needed by CL/R1; its content is relocated to …". In §10 the pre-stated success item
    "a proof that RLF-step does not need (H-pos)" is ARGUED (a sketch with hypotheses and the unnamed gaps H-1, H-3 and
    H-4), not MET as a proof. "(D1-a) MET" stands.

### Proposition CF (l.327-352): CONFIRMED (uncounted; bounds a method), scope fix
- The constant-curvature symmetric-gauge field has plaquette e^{iFσ_3}, and for 2sin(θ/2) = ε ≤ 0.52, θ ≤ 1.012ε.
- **(1)** For e_3/e_4 links the two axial paths have equal (1,2)-projections traversed oppositely, so A_{12} = 0. For e_1
  links the reflection x_2 ↦ 2(c_X)_2 - x_2 maps the S4' family to itself with the same σ and A ↦ -A. So M̄ = mean(cos FA)·S.
  - For i ≤ k - 1, |F|·(3/2)L(L - 1) ≤ θL^{-2}·(3/2)L(L - 1) < 3θ/2 ≤ π/4, so m ∈ (0, 1] and W_0 = S uniquely.
  - The corrected ribbon-area constant is right (and generous: only e_2-steps contribute, ≤ L(L - 1)/2).
- **(2)** The straight transporters give curvature L²F plus per-direction constant phases, which cancel in closed abelian
  loops. **(3)** The bare action is right.
- **Reading, fix H-8 (l.349-352, l.593-596).** CF defeats every bound that prices a bad level-k plaquette by O(1) kernel
  mismatches or O(1) level-j plaquettes above sup-thresholds t_j: such a bound needs t_j ≤ 1.05εL^{-2(k-j)}, and
  t_j²/g_j² → 0 with depth. That is a method limit, not a constants problem. Correct.
  - It does not exclude bounds that aggregate the L^{4(k-j)} level-j plaquettes. A many-plaquette Peierls count or an
    action sum gives L^{4(k-j)}t_j²/g_j² ≈ θ²/g_j², which does not decay.
  - "Visible only to an ℓ² (action-sum) bound" should read "visible to bounds that aggregate ≳ L^{4(k-j)} plaquettes per
    level".
  - "Route (R-a) meets (HP-F1)" should be limited to the sup-threshold (iterated-dichotomy) form of (R-a). Dimock-style
    per-level extraction uses action sums and is not covered.

### (CLS-NA) wall (l.354-363): CONFIRMED as a precisely named OPEN wall, one definition missing
- The linear abelian case follows from E-low: E_k ≥ c_E||dB_k||² ≥ c_E·Σ_{P∈𝒫}(…).
- The obstruction (the polar part of an average of transporters far from S, outside PM's range) is the right one.
- **"Pairwise disjoint shadows" for level-k plaquettes is undefined.** §7.1 defines shadows upward (projections to coarser
  levels); here a downward footprint is meant. Define it (e.g. the level-0 region U_4^{(k)}(P) under P, with a
  1-neighbourhood).
- Correctly scoped: the target is (D1-b), and RLF-step^J does not consume it.

### (D1-c) "ARGUED false at tree level" (l.365-375): CONFIRMED as ARGUED, and broadened (fix H-2)
- **The argument is right.**
  - If (I_k) held for all U with a g-independent per-cube E_0, then g²E_k → 0.
  - The Laplace link holds: compact group; log ∫e^{-(κ/g²)φ} = O(log(1/g)) by (3.1); coupling ratios → 1 at fixed k.
  - Together these force E_k(U) - E_k(1) = λΣs(U_P) identically.
  - Linearising at e^{itB} contradicts c31 E2. The cited numbers are verbatim in checks/c31E.out l.6-9: 0.05741, 0.05850,
    0.05820 and 0.04080. The linear chain uses the normalised kernel (LINEAR_PACKAGE §1.3), so it is the same φ.
- **It proves more than §6 says.** The configurations e^{itB} with g ≪ t < ε_1 are *small-field* (every plaquette < ε_1).
  On them the mismatch between the coarse Wilson action and the chain energy is ≍ t²/g² per cube, which is unbounded on
  RLARGE's g-independent ε_1-domain. So:
  - (I_k) on Λ_k, in RLARGE §8.1's form (coarse Wilson main term + polymers with per-cube bound), is ARGUED false too.
    RLF-step^J step 5 and H-pos^J (iii) assume it.
  - The per-cube polymer bound Σ_{X∋x}|E_m(X)| ≤ E_0 that HIST consumes in (P4) (l.504-505) and in (H-w)'s B_0 item (b)
    (l.456) is the same object, and falls with it.
  - The bracket at l.372-375 treats only fields of size g ("bounded but not small"). Fields of size t ≫ g are the
    decisive case.
- **What replaces RLARGE's per-cube form.** There are two layers:
  - for the R-operation, CL^J/R1^J (no action at bad cubes is needed);
  - for the representation, (I_k^E): main term E_k(U_k)/g̃_k², the chain-energy (background-field) action, plus polymers
    small in a background-field norm, as in Balaban/Dimock [inference].
  - The coupling shift δβ^J_k multiplies the coarse Wilson action, which is then not the main term. δβ^J_k·(Σs - λ⁻¹E_k)
    is a small polymer (|δβ| ≲ e^{-a''/g²} times O(1) per cube), so (P2)'s arithmetic survives, but the "one coupling
    shift" reading of (RLF-0) has to be restated against E_k.
  - **Fix H-2:** promote the bracket to a named requirement (I_k^E) on (SF)/(I_k), and re-base (P4) and (H-w)(b) on it.

## §7 Target D2

### §7.1 definitions and Lemma H-nest (l.379-406): CONFIRMED
- (i) Σ(Ω^c_k) ⊂ Ω^c_{k+1} is immediate from Σ-distributivity.
- (ii) Y ⊂ Λ_{k+1} gives dist(Y, π(Ω^c_k)) ≥ 2, so the level-k data under N_1(Y) are in Λ_k.
- (iii) Columns: the contrapositive gives an initial interval.
- The Remark separating the width-1 activity collar from the R^J_*-wide extraction collar is the key structural point, and
  it is right. With the extraction collar in the shadow, the per-level size ~n_c⁴ ~ n_♯⁴ would force n_♯ ≳ n_♯⁴B_0/(aβ log L).
  That is (HI-F1).
- Small defect configurations touching Σ(Ω^c_k) read collar data that were never R-operated. If those data are bad,
  the configurations are collar-bad and go to (W1-ret'^J). That is consistent with RLARGE's two thresholds, but it is
  worth one sentence at l.389-390.

### Lemma H-geo (l.409-424): CONFIRMED
- (i) |⌊u/L⌋ - ⌊v/L⌋| ≤ ⌊|u - v|/L⌋ + 1 ≤ 2 for |u - v| ≤ 3 and L ≥ 3. The induction closes with N_1∘N_2 = N_3.
- (ii) Scaled closed boxes are unit cubes of a translate of Z⁴. τ passes through every centre and hence meets every
  ancestor box. CE-geo' (g1') (PROOF l.2187) gives N(τ) ≤ 16 + 16ℓ, with ℓ ≤ 2(n - 1)L^{-m}.
- (iii) 7⁴ = 2401. (iv) 2401·32/(L - 1) ≤ 38416 for L ≥ 3, and 2401·16 = 38416.
- On the torus every count only decreases.

### Lemma RS-joint (l.427-443): CONFIRMED as CONDITIONAL (plain chain measure); the in-history form is ARGUED
- The split ζ ≤ qζ + (1 - q), the conditional independence (TD), the n_ℓε_ker bound (RS-lin (b)), the 81-greedy choice
  (R_k(Q)'s of non-*-adjacent cubes are ≥ L² + 1 apart), m_k = 6L⁸ and (x + y)^{|A|}: all checked. c_RS = 81 replaces
  RLARGE's ARGUED 5⁴.
- **Fix H-4 (l.442-443).** "The lemma is then the same, conditionally on the history" is ARGUED, not proven. In the
  induction the conditional law of U_{k+1} given U_{≤k} is tilted by G_k's U_{k+1}-dependent factors (H-1). Under
  (H-Mayer^J) the tilt is bounded by e^{Σ|ρ|}, which is plausibly harmless, but it is not written.

### Hypothesis (H-w) (l.446-458): a precise OPEN hypothesis; its ARGUED decomposition needs H-2
- The form is clear: Z^{sf}, creation weights at the creation level, and B_0 per cube per level of persistence.
- "Weaker than the Dimock form" is right in the sense that it is easier to satisfy: B_0 ≥ 0 is charged on more cubes.
- **No circularity.** B_0 = B_0' + 1, with B_0' cutoff-independent; item (d) is ≤ 1 for g ≤ g_0(n_♯). So n_H, then n_♯,
  then g_0 is non-circular.
- Item (b) needs H-2.
- Item (c) assumes the per-cube, per-level normalisation mismatch with Z^{sf} is O(1). For the exact soft chain this is
  plausible, because ∫K = 1 makes per-step normalisations trivial. Still, it should be said that a log(1/g) per cube per
  level here would make c_B g-dependent and n_H infinite (HI-F2). That is the one place where the threshold's
  g-independence is fragile [inference].

### Theorem HIST-sum (l.460-484): CONFIRMED (CONDITIONAL ⇐ (H-w), (F)_-)
- Injectivity, then the product bound with Σ_k|Ω^c_k| ≤ Σ_{(j,𝒟)}[38417|𝒟| + 38416(K - 1 - j)], then Π(1 + v) ≤ e^{Σv} over
  ALL pairs (finite torus).
- (g3) 6400^{n-1} per root.
- Flow e^{-na/g_j²} ≤ e^{-na/g_K²}L^{-naβ_-(K-1-j)}. The m-sum ratio L^{-(naβ_- - 4 - c_B)} ≤ L^{-γ_H} for n ≥ n_H + 1.
- The n-tail gives (2/6400)(6400C'_ℓe^{-a/g_K²})^{n_♯+1}, and C_H follows.
- The upper bound on Z_K uses Z(∅) ≤ Z^{sf} ((H-w) at 𝔥 = ∅). No lower bound on Z_K/Z^{sf} is claimed, which is consistent
  with (RLF-3).
- **Priority 4 verdict: the entropy-vs-weight core is right.** The per-level persistence entropy e^{38416B_0} is
  n-independent, and the per-level resource naβ_- log L is linear in n. That is the only reason a finite n_H exists. It
  needs (a) the width-1 shadow and (b) β_- > 0, both stated.
- Corrections to RLARGE (threshold n_♯ ≥ n_H; (P1) superseded): CONFIRMED. RLARGE's own (I_k) already carries
  e^{B_0|∂Ω|} per level, so its (P1) was missing exactly this factor.

### (P1)-(P5) over K levels (l.486-507)
- (P1) = HIST-sum: CONFIRMED.
- (P2), (P3) arithmetic: CONFIRMED (the collar corrections are ≤ C(n_♯)e^{-a''/g²} per cube). Add H-2's remark on the
  "coupling shift" reading.
- **Lemma P4-div: CONFIRMED (arithmetic).** It is LF-count's divergence under one level-m cube. Its reading ("(P4) cannot
  come from bookkeeping") is right.
- **(P4) "CONDITIONAL ⇐ (SF)'s polymer bound + (W1-ret')(b)": demoted to ARGUED.** The consumed (SF) bound Σ_{X∋x}|E_m(X)| ≤
  E_0 is the per-cube coarse-Wilson form that §6's own argument refutes on the ε_1-domain (H-2). Re-state (P4)'s hypothesis
  against (I_k^E) before calling it CONDITIONAL.
- (P5) unchanged.

### Theorem TS_K (l.509-527): CONFIRMED-WITH-FIX; recount as an uncounted corollary
- Top-ancestor decomposition (H-nest (iii)), then TS (TS-b) per top cube, then R1_Λ for the restricted gas, then the
  ℛ^∂ count with w_*. Right.
- **Fix H-5.** The hypothesis "BG-b relative to level m on Δ_*" uses TS's Δ_{*,n}: all cubes within R_*/L + 1 of
  𝒬_n(Δ). Near Ω^c that region contains large-field cubes, where (b1) (ε_2 + ε_V ≤ M_2σ_n²) cannot hold, so the hypothesis
  is unsatisfiable exactly where TS_K is new. Restrict it to Δ^{in}_{*,n} := the cubes meeting B̂_*(x) for
  x ∈ 𝒬_n(Δ) ∩ Λ_i^{in}. TS's proof uses (b1)-(b2) only there, and the overlap count is unchanged.
- **Counting.** Its only new ingredients are H-nest (iii) (counted with H-geo) and R1_Λ (counted with R1^J). List it under
  "PROVEN-HERE, not counted", as H-pos^J is.
- "The same proof works with R1^J" (l.511) is ARGUED: BG-b would have to cover the level-(i+2) links. Keep TS_K in the bare
  form as stated.

## §8 RLF-step^J (l.529-564): CONDITIONAL with unnamed gaps → counted as ARGUED
- Step 1 needs (H-Mayer^J) in H-1's global form.
- Step 5 needs (SF^J) (H-3) and (I_k^E) (H-2).
- Step 4 uses RS-joint in its in-history form (H-4).
- As in REVIEW_S16_S17's treatment of RLF-step (G1-G4), "a proof sketch modulo the named hypotheses" becomes true once
  H-1 to H-4 are named.
- **"What it added: nothing new in kind" (l.563-564)** is not right. (SF^J) and (I_k^E) are new in kind: the effective
  densities become two-field, and the main term changes.

## Checks (re-run)
Setup: laptop. The machine-wide numeric lock was taken by `mkdir` (and released by `rmdir`, under a trap), with nice 10,
OPENBLAS/OMP/MKL/vecLib threads 1, PYTHONDONTWRITEBYTECODE = 1, sequential, no `timeout`.
- One false start: my first wrapper used `python3 -I`, which hides the user-site numpy. h1-h3 died at import (h4 needs no
  numpy and ran). The lock was released. Re-run without `-I` (as REVIEW_S16_S17 disclosed for c31/c32); the scripts read
  only their own constants.

Load during the runs was 2.2-3.5 (< 8), with 44% free memory.

| Check | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| h4 | I1 PASS (informational table) | 0.02 s | 15 MB | identical |
| h2 | C1-C6 PASS, F = 0.01, 0.03, 0.058 | 0.9 s | 37 MB | identical except timing |
| h3 | G1-G4, N1 PASS; persistent shadow 81, then 256 | 5.2 s | 44 MB | identical except timing |
| h1 | P1, G, K1-K3, R PASS (N = 2, 3) | 209.6 s | 34 MB | identical except timing |

(Each output was compared with `diff` after stripping the timing/RSS tail.)

Procedure:
- **Criteria predate the scripts (mtimes, local time EDT = UTC-4):**
  - all four criteria 19:19:40;
  - h1 script 19:20:35, h2 19:20:58, h3 19:21:41, h4 19:21:58;
  - outputs 19:22:10-19:25:58.
  - HIST.md and HIST_LOG.md were last written at 19:26:27, after the outputs (§9-§12).
  - The order *inside* HIST (§0-§1 at 23:08 UTC before §2) cannot be verified from mtimes. 11 minutes for §2-§8 is
    recorded, not checked.
- No criterion was edited and no tolerance added. The disclosed h1 restart-count edit was restored before any run; the
  script has 20 restarts, as the criteria say.
- Disclosed deviations are real and harmless: h3 has 63 random sets per L (60//7 + 1 = 9 per n), not 60; h1 has bisection
  depth 60.
- **Scope observations.**
  - h1 R tests the sphere ||V - S|| = ε_1/8, not the whole event {≥ ε_1/8}; the lemma's proof covers the rest.
  - h1's SU(3) maximiser is local, from S; G spot-checks globality.
  - h2 is one step, as disclosed.
  - No check touches CL^J (c), R1^J or HIST-sum. The H-1 error is structural and no instance check would catch it.
  - h3's 256 = 4⁴ persistent shadow (against the proven 38416) means c_B could be ≈ 150× smaller with a sharper count.
    This is optional.

## Overclaims in the headers, tallies and outcomes
1. **l.112-114, l.240-242, l.319-320, l.537-538:** "near returned defects" / "G1 does not arise": H-1.
2. **l.316, l.562 "(H-pos)_k can be deleted … removed entirely":** relocated, not removed (H-10).
3. **l.588-591 (§10) "the pre-stated success item 'a proof that RLF-step does not need (H-pos)' is met":** ARGUED (sketch
   with unnamed gaps).
4. **l.351, l.593-596 "route (R-a) meets (HP-F1)":** for the sup-threshold form only (H-8).
5. **l.135-136, l.163-165 "linear threshold":** for ε_1 ≤ 0.4 only (H-9).
6. **l.372-375:** the (D1-c) consequence is understated (H-2). It reaches (I_k) on Λ_k and HIST's own E_0 uses.
7. **l.505, l.630:** (P4) CONDITIONAL on a bound §6 argues false in that form.
8. **l.563-564 "nothing new in kind":** (SF^J), (I_k^E).
9. **l.509, l.627 "[S18-repair, unreviewed]":** stale. Cite REVIEW_S18_S19 (R1, TS CONFIRMED-WITH-FIX).

## Verdict counts and tally

**Counted items (claimed 6).**
- Lemma PM (with KQ): CONFIRMED.
- Lemma RS-lin: CONFIRMED (H-9 wording).
- Proposition CL^J: CONFIRMED-WITH-FIX (H-6; the proposition is right as stated, and its application is H-1).
- Theorem R1^J (with GT-lat'', 7.2-0^J, R1_Λ): CONFIRMED-WITH-FIX (F1 carried over; status label; R1_Λ = G5).
- Lemma H-geo (with H-nest): CONFIRMED.
- Theorem TS_K: CONFIRMED-WITH-FIX (H-5), **recounted as an uncounted corollary.**
- **0 GAP, 0 WRONG among counted items.**

**Uncounted items.**
- Lemma TD, Proposition CF (scope H-8), Theorem H-pos^J (H-3, H-10), Lemma P4-div, (P2), (P3): CONFIRMED.
- Lemma RS-joint: CONFIRMED as CONDITIONAL (plain chain measure; in-history form ARGUED, H-4).
- Theorem HIST-sum: CONFIRMED as CONDITIONAL.
- (P4): CONDITIONAL → ARGUED (H-2).
- RLF-step^J: CONDITIONAL-with-unnamed-gaps → ARGUED (H-1, H-3, H-4).
- (D1-c): CONFIRMED as ARGUED, broadened (H-2).
- (CLS-NA), (D1-b), (H-w): OPEN, precisely named (CLS-NA needs its "shadow" defined).
- The §2 sentence l.112-114: WRONG.

**Corrected tally of HIST.md: 5 PROVEN-HERE / 2 CONDITIONAL / 6 ARGUED / 3 OPEN** (claimed 6 / 4 / 4 / 3).
- PROVEN-HERE: PM, RS-lin, CL^J, R1^J, H-geo.
- CONDITIONAL: RS-joint, HIST-sum.
- ARGUED: (D1-c), the Laplace link, the (H-w) decomposition, (H-Mayer^J), (P4), RLF-step^J.
- OPEN: (CLS-NA), (D1-b), (H-w).
- If the lead places these in PROOF.md, the main-path count rises by 5, not 6, once fixes H-1 to H-12 are written.
  (HIST correctly makes no PROOF tally change itself.)

## Required fixes (binding for the next lane-D session)
1. **H-1.** Make G_k's U_{k+1}-dependence global (all stage-(k-1) remainders and re-extracted polymers). Restate
   (H-Mayer^J) as a whole-lattice Mayer expansion of small two-field activities. Rewrite l.112-114, l.240-242 and
   l.532-538.
2. **H-2.** Broaden (D1-c): per-cube-bounded coarse-Wilson (I_k) fails on the ε_1 small-field domain too.
   - Name (I_k^E) (chain-energy main term) as a requirement on (SF)/(I_k).
   - Re-base (P4) and (H-w)(b) on it, and demote (P4) to ARGUED until then.
   - Restate the "one coupling shift" reading of (RLF-0) against E_k.
3. **H-3.** Name (SF^J)_k (three-level polymers in, two-field polymers out). Fix H-pos^J (iii)'s wording.
4. **H-4.** Mark RS-joint's in-history form ARGUED, with the e^{Σ|ρ|} tilt as the missing step.
5. **H-5.** Restrict TS_K's BG-b region to Δ^{in}_*. Move TS_K to the uncounted corollaries.
6. **H-6.** Den^J_B > 0 via U_{k+1} ≡ 1 on int(B).
7. **H-7.** Lemma 7.2-0^J: add F1's Lipschitz line for C^J_♮.
   - Cite REVIEW_S18_S19 for R1/TS.
   - State that R1_Λ with Λ' := the (H-ch)^J-good cubes is G5's R1-loc.
   - List the missing-shift cost near in-sea collar-bad cubes under (W1-ret'^J).
8. **H-8.** CF scope: "O(1) plaquettes or mismatches per level". Aggregating bounds are not excluded.
9. **H-9.** "Linear threshold" holds only for ε_1 ≤ 256Nδ_0. Say where h4's n_♯ gain comes from.
10. **H-10.** "(H-pos) relocated, not removed". §10's success item → ARGUED.
11. **H-11.** Define the downward "shadow" in (CLS-NA). Add the collar-bad sentence at §7.1 l.389-390. Add the (H-w)(c)
    fragility note (a log(1/g) per cube per level would break n_H).
12. **H-12.** §10-§11 tally → 5 / 2 / 6 / 3; "nothing new in kind" → (SF^J), (I_k^E).

---

## Strategic verdict: (H-w) versus (CLS-NA)

- **(CLS-NA) in full (large fields): do not attack.**
  - It is off the main path. CL^J/R1^J never evaluate an effective action at a bad cube, so the joint route does not need
    large-field stability of the chain energy.
  - Only the (D1-b) form wants it, and (D1-b) is not consumed by anything.
  - Proposition CF already says what any proof must look like (aggregating, ℓ²-type). That is CMP 122-scale work, with
    the papers unread.
- **(H-w): do not attack yet.**
  - It is on the main path ((RLF-3) via HIST-sum), but it is [P], and its decomposition rests on (W1-ret'^J)(c), (SF^J)
    and (I_k^E). The first is blocked behind N5/(DF4), as REVIEW_S16_S17 said; the other two do not exist yet.
  - Its combinatorial half is done and confirmed (HIST-sum). Its analytic half is literally the subject of CMP 122 II.
- **Recommended instead, in order:**
  1. **The binding fixes H-1 to H-12.** About half a session; mostly restatements.
  2. **(I_k^E), stated precisely, with RLF-step^J re-checked against it.** This is the real consequence of this session,
     and it is session-scale:
     - write the representation with the chain-energy main term;
     - check that CL^J, R1^J and HIST-sum are untouched (they are: U_k is frozen and the main term never enters them);
     - identify what (PLD-q), (P4) and (H-w)(b) then need.
  3. **[inference] The small-field restriction of (CLS-NA), "CLS-sf":** E_k(U) ≥ c·Σ_Ps(U_P) for fields with every level-k
     plaquette < ε_1. With (I_k^E), this is what (PLD-q)_k needs for its Peierls exponent at threshold η_q. It is a
     non-abelian perturbation of E-low near S, in Lemma PM's regime. That is the one piece of (CLS-NA) that is on the
     main path, and it is plausibly session-scale. Its full large-field version is not on the path.
  - (H-w) waits for (SF^J) and the CMP 122 reading, as (HIST) did in REVIEW_S16_S17.
