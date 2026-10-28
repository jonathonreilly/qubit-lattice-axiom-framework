# REVIEW_SF_S2: hostile review of lane F session 2 (SF.md §0-§5 [RSF1-fix] edits; §6-§8: Theorem CE-exp, Lemmas LOC-s, HULL, CE-exp-𝒞, CE-exp^0/^k, (CE-Q), SF-J', SF-src, (SF-N♮), Lemma BS, Lemma G-pert, Proposition U-red, (a5-G♯), (G♯-patch), (MIN-reg))

Reviewer: an independent agent that wrote none of SF.md. I edited no file except this one. No commits, PRs or pushes.

Inputs (read 2026-10-28 ~03:58-04:20 UTC):
- SF.md l.1-919 in full (by offset); SF_LOG.md in full; REVIEW_SF_S1.md in full (the binding list).
- checks/s2_criteria.md, s2_sf.py (line by line), s2_out.txt, s2_time.txt; birth/mod times (`stat -f %SB/%Sm`).
- PROOF.md: Setting CE / Theorem CE l.1831-1912; Setting N5-0 l.5116-5124 (the distance d); Setting N5-bg l.5199-5240;
  Theorem N5-sf0 l.5382-5406; B-NA-red + BNA-F1-F3 l.3147-3195; (R♯_ω) l.3477-3491; [S21] NAH-unif l.6036-6075.
- RTARGET.md §33-§37 (l.572-666). REVIEW_HIST_S4.md S4-1, S4-2, M-1-M-3, binding fixes, strategic verdict (l.220-280,
  l.468-506). HIST.md l.1549-1553 (R_ε, P_r), §25.4 NORM-an (l.1628-1642), l.1669 ((a3-q)). RLARGE.md l.55-80, l.681.
- agents/ym4d-existence/EXISTENCE.md §19.4-§19.5 (l.3882-3972) (read-only).
- md5 now: SF ab0199f0…, PROOF **8d8f0fcd…** (SF read 490aaf34…: **PROOF changed after SF's 03:45 read**; the [R21-fix]
  annotations to NAH-unif are now in PROOF, item A-4 below), HIST 468e9f03… (= SF's), RTARGET 5b742808… (SF read e9af331a…;
  §33-§35 unchanged in substance), REVIEW_HIST_S4 bc0a9da0… (= SF's), REVIEW_SF_S1 319d65c3… (= SF's), EXISTENCE 351bdd9e….

Scratch (lock-guarded runner and outputs): scratchpad `revSF2/` (run.sh, rev_s2_out.txt, rev_time.txt).

---

## Bottom line

- **Theorem CE-exp is correct, and it is a real gain.** Every step re-derived (LOC-s, HULL, the Step-2 sum, the sufficient
  condition, the s2 C numbers). It uses Theorem CE strictly as a black box, and every hypothesis of Setting CE is met: fields
  on fine sites, M⁴ sites per cube, ν_∅ a product probability measure over sites (it is: SF-cut's ν_∅ = Π_x χ_xμ_x/μ_x(χ_x)),
  H'(Y) complex, measurable, reading Z on Y only, bounded on supp ν. There is no tree-graph/Penrose step of its own to check;
  the Mayer step is CE's. The κ' = 469.04, κ ≥ 1.2808·10⁵, M_min = 3.187·10¹³ numbers are right (re-run identical).
- **CE-exp^0 is correct as a CONDITIONAL**, and one of its caveats is void: PROOF's d is the ℓ¹ torus distance of base
  points (Setting N5-0, l.5122), which dominates ℓ^∞. Delete "[not checked in PROOF's text]" (SF l.760).
- **CE-exp^k does not retire (OP-loc)_k.** Two defects:
  1. **(L-hol)_k, as stated, is not a viable target.** It asks the level-k main-term densities to be holomorphic on weighted
     polydiscs whose radius grows like ρ_ke^{μ_kd}. Those densities come from critical chains (implicit functions). At a link
     at distance d the polydisc allows |A_b| ≍ e^{μd}. There no small-field chain exists, so the density is not even defined.
     Exponential locality of the *derivative* (HIST A5 (C)) is a different and weaker statement.
     - The operator half of (OP-loc)_k is legitimately retired: the operator enters only through N_μ(|𝒞_k|).
     - The activity half survives. It is REVIEW_SF_S1 OP-3: a localisation expansion of the main-term densities into strictly
       local pieces, each analytic on a uniform polydisc.
  2. **CE-exp^k omits the inherited level-k polymer activities, and the rate budget does not close.** CE-exp needs input rate
     κ ≥ 273κ' + 1296W ≈ 1.28·10⁵ (M-units). It returns rate κ_c - 3κ_0 - 3 (= 1 at κ_c = 3κ_0 + 4). SF-blk multiplies by
     ≈ L.
     - For any κ_c, L(κ_c - 3κ_0 - 3 - κ_0) - 1 < 273κ_c at L = 3. So CE-exp cannot be iterated on its own output.
     - The e^{272κ'} factor in H'_0 also exceeds any per-level norm gain.
     - The loss is entirely SF-geo's multiplicative d(X^+) ≤ 273d(X) + 272. HULL's far-site part is additive.
     - New OPEN name: **(CE-col)**, a collar-native Theorem CE: Mayer connectivity through X_i^+, with a constant loss per
       polymer and no rate factor.
- **Lemma SF-J' is correct for every N; Lemma SF-src is correct** (both CONFIRMED). SF-src's bound is the max of the two
  cases. Calling it a sum is harmless.
- **STEP 3.**
  - (a5-G♯) is a correct restatement of PROOF's (G♯) in the §33 pair, with two wording fixes.
  - Lemma BS is CONFIRMED. R_ε is an operator-norm plaquette class (HIST l.1549), so the proof is complete.
  - Lemma G-pert is a correct implication, but it does **not** reduce (a5-G♯) to trivial-chain items in any case that B-NA-red
    does not already cover:
    - it is NA-IFT's Neumann step, valid only for chains X_c-small in ONE global gauge (||B_k||_D ≲ ε_0);
    - it bounds the trivial-slice Hessian at x^r, not the Hessian in "a per-level covariant slice through ψ^r". That
      identification is missing.
    - The generic background (no globally small gauge, BNA-F4) is entirely **(G♯-patch)**, and (G♯-patch) is a description,
      not a statement.
  - Proposition U-red is CONFIRMED (implication). (MIN-reg) is precisely stated after the post-proof precision, but it is
    (a5-U)'s global content renamed, and it belongs to lane D.
- **Binding fixes (RSF1): 20 tags checked.**
  - 15 CONFIRMED.
  - 4 CONFIRMED-WITH-FIX:
    - BG-1: its new sentence overstates what NAH-unif gives;
    - SF-thr-k-1: stale after PROOF's [R21-fix S21-5], which marks NAH-unif "GAP as stated" and adds (H-G) and (H-ℂ);
    - SF-thr-1/2: ε^J_loc still unchecked;
    - OP-1/2/3: its "retires" sentence (defect 1 above).
  - 1 stale-text note (§4.2/§4.3 untagged remnants).
  - None WRONG.
- **s2: honest and reproduced.**
  - The criteria were born before the script (03:46:33 vs 03:47:49 UTC); the criteria md5 matches the log (366105b1…).
  - Re-run: output byte-identical (OVERALL PASS 14/14), lock 04:05:44-04:05:53 UTC.
  - Five of the 14 criteria are tautologies of the construction (A1, A2, B2, the count part of D3, E2). They carry no
    evidence, and the 14/14 should be read as 9 informative passes.
- **(CE-cond) verdict: NO.** CE-exp does not supply EXISTENCE §19.4 (CE-cond), and no easy extension does (Part F).
- **Corrected tally (SF.md after session 2): PROVEN-HERE 20 + 1 standard (counted 7, not counted 13), CONDITIONAL 4, ARGUED
  2, 0 GAP, 0 WRONG**: SF's numbers.
  - Withdrawn claims: "(OP-loc)_k retired" (activity half), "(a5-G♯) reduces to trivial-chain items via G-pert", BG-1's
    "(i)-(iii) follow from CURV1 + NAH-unif".
  - (L-hol)_k is re-labelled NOT VIABLE AS STATED. New OPEN names: (CE-col), (L-loc)_k.
  - No PROOF.md tally change.

---

# PART A: the 20 [RSF1-fix] tags (fix number = REVIEW_SF_S1 Part D)

| # | SF line | fix | verdict | note / fix |
|---|---|---|---|---|
| 1 | l.34-36 | SF-J-2 (Frobenius structure) | CONFIRMED | Constants N/9, N/270, √N are for −tr A² (SF-J proof uses Σ\|λ\|² ≤ \|\|A\|\|²_F). |
| 2 | l.65-72 | SF-thr-1/2 (field chain; interior plaquettes; ε_loc, ε^J_loc) | CONFIRMED-WITH-FIX | Chain right. ε_loc ≤ ε_1/4 checked (RLARGE l.681). ε^J_loc is "assumed, not checked" (l.72). Its definition is HIST §4-§5 (RLARGE l.62); check it next session. The CURV1 constant at l.69 is now C_θ^{ρ} for ρ ([R21-fix S21-6], PROOF l.6046). |
| 3 | l.76-79 | SF-thr-k-2 (withdraw the soft-clause sentence for the background) | CONFIRMED | Matches REVIEW_SF_S1 A1-2 verbatim in substance. |
| 4 | l.83-85 | BG-1 (level-(k+1) wording) | CONFIRMED-WITH-FIX | Restoring the wording by annotation is acceptable. **The added sentence is overstated.** "(i)-(iii) follow from CURV1 + NAH-unif under (H-K) + (H-C)". (i) (curvature, ρ) follows, but now also needs (H-G), (H-ℂ) ([R21-fix S21-5]). (ii) holomorphy IS (H-ℂ) ⊂ (BG-unif) (ii) (PROOF l.6064), so this is circular. (iii) is the exponential tower response \|∂U_j/∂V_k\|. It is not a conclusion of NAH-unif at all. **Fix:** "(i) ⇐ CURV1 + NAH-unif under (H-K), (H-C), (H-G), (H-ℂ); (ii) = (H-ℂ); (iii) not supplied." |
| 5 | l.95-100 | BG-loc-1 (drop; content = A5 (A)-(C)) | CONFIRMED | Implication, not identity: right. The hypothesis list matches REVIEW_HIST_S4 l.449. |
| 6 | l.126-132 | SF-N-1 (re-base on NORM-an) | CONFIRMED | K_𝔫 = 2C_N·18.4(2 + 2c_N) = 36.8C_N(2 + 2c_N), correct from HIST l.1634-1636. "Unreviewed by its own reviewer except REVIEW_HIST_S4" should read "reviewed by REVIEW_HIST_S4 (strategic verdict 2: real and reusable)". |
| 7 | l.147 | SF-A2-3 (status) | CONFIRMED | |
| 8 | l.170-177 | OP-1/2/3 | CONFIRMED-WITH-FIX | (1)-(3) are right. The appended "Session 2 retires (OP-loc)_k … its activity input is (L-hol)_k" must be narrowed: the **operator half** is retired; the **activity half** (OP-3) is not (Part B, B-5). |
| 9 | l.189-192 | V-1 | CONFIRMED | |
| 10 | l.197-198 | V3 session-2 note | CONFIRMED | |
| 11 | l.251-257 | SF-thr-k-1/2 (re-base on NAH-unif) | CONFIRMED-WITH-FIX (stale, not SF's error) | Correct against PROOF 490aaf34. **PROOF now marks NAH-unif "GAP as stated"** (l.6037): it is a correct implication only with (H-G) and (H-ℂ) added. [S22] proves (H-G) at level 1. "Margin ≈ 10" and "K_p^♯ = 0.062, 0.103" are withdrawn there: read "K_p^♯ ≈ 0.11-0.13 at level 0 (closed inputs), margin ≈ 8, two rows, not certified" (PROOF l.13, l.6066). **Fix:** SF-thr-k CONDITIONAL ⇐ (N5-unif) ⇐ (H-K) + (H-C) + (H-G) + (H-ℂ). §8.1 l.876 and §8.2 l.905 likewise. |
| 12 | l.277-282 | SF-J-1 (chart-specific) | CONFIRMED | |
| 13 | l.329-330 | SF-T0-1 (κ_ker) | CONFIRMED | Grep: no remaining κ_0 used for the kernel strength. |
| 14 | l.350 | SF-A2-2 (covariance Ng_0²C) | CONFIRMED | |
| 15 | l.358-363 | SF-A2-1 (source size) | CONFIRMED | Via Lemma SF-src (Part C). |
| 16 | l.459-463 | V-2 | CONFIRMED | |
| 17 | l.465-467 | V8 note | CONFIRMED | |
| 18 | l.476-478 | SF-A3^0 (session 2) | CONFIRMED | |
| 19 | l.503-504, l.539-542 | §4 header + §4.2 bullet 1 (SF-J-1) | CONFIRMED, with a stale-text note | **§4.2 bullet 2 (l.543-544)** still says the linear term is "NON-vanishing" with no size; add "O(y_bg); zero at flat backgrounds (SF-src)". **§4.3 (l.555)** still calls (OP-loc)_k "a new necessary item". The l.503 header covers both as "superseded", which is acceptable, but tag them. |
| 20 | l.685 | §6.3 header | CONFIRMED | |

Fix 14 ((F1) consumers) and the owner notes are carried in §8.3 (l.911-919), correctly addressed to their owners. Fix 15 (validate
RW at s ≡ 1) is not applicable to s2, as SF_LOG says.

---

# PART B: Theorem CE-exp and its corollaries

### B-1. Lemma LOC-s (l.616-619, proof l.703-714): CONFIRMED (counted)
- (1) Möbius inversion over subsets of F = Λ∖∪X^+: right.
- (2) Locality: at s_y = 0 the variable Z_y does not enter, so g(1_T) reads only ∪X^+ ∪ T. Right.
- (3) F_{X,S} = ∫_{[0,1]^S}∂^Sg(σ_S, 0)dσ, with the F∖S variables at 0 (inside 𝔻, since |0| < 1 + e^{μδ}). The mixed
  first-order Cauchy bound on the S-polydisc of radii r_y < e^{μδ(y,X)} (|σ_y| + r_y < 1 + e^{μδ}) gives Π r_y^{-1}. Right.
- (4) dist(q(y), X) = n + 1 when dist(q(y), X^+) = n ≥ 1 (ℓ^∞ cube index), so δ ≥ nM + 1. Right; s2 B3's min(δ - Mn) = 1
  attains it.

### B-2. Lemma HULL (l.620-621, l.716-726): CONFIRMED (not counted)
- σ_y has length |Δ|_2 ≤ √4|Δ|_∞ = 2n_y.
- γ_y ⊂ Q'_y ⊂ X^+ has length ≤ the half-diagonal 1.
- τ' ⊂ ∪Y (σ_y lies in the union of the closed cubes it meets) and meets every closed cube of Y. So it is admissible for
  Setting CE's d (contained in ∪Y, meets every closed cube: PROOF l.1836-1838).
- Additive in the far sites: right.

### B-3. Theorem CE-exp (l.622-627, l.728-750): CONFIRMED (counted)
- Step 1:
  - H'(Y) := Σ_{Y(X,S)=Y}F_{X,S} reads Z on ∪X^+ ∪ S ⊂ ∪Y;
  - it is 0 unless Y is a polymer (HULL);
  - finite torus, finite sums.
- Step 2, re-derived:
  - e^{κ'd(Y)} ≤ e^{κ'(273d(X)+272)}Π_y e^{κ'(2n_y+1)}, with |F_{X,S}| ≤ h_0e^{-κd(X)}Π_y e^{-μMn_y};
  - the count #{sites with n(y,X) = n} ≤ |X^+|(2n + 1)⁴M⁴;
  - |X^+| ≤ 81|X| ≤ 1296(1 + d(X));
  - 2^{|Y|} ≤ 2^{16(1+d(Y))} (CE-geo').

  The displayed H'_0 and κ_c = κ' - 16 log 2 follow.
- Step 3: Setting CE's hypotheses checked one by one (PROOF l.1843-1845): fields on sites, each site in exactly one cube, ≤ M⁴
  sites per cube; ν product probability; H' measurable, complex, Φ|_Y-local; the bound on supp ν; κ_c > 3κ_0 + 3;
  H'_0 ≤ c_0(κ_c). CE's conclusion transfers.
- Sufficient condition: μM - 2κ' ≥ κ' + 4 log M + 8 gives M⁴e^{κ'}e^{-(μM-2κ')n} ≤ e^{-8n} for n ≥ 1. Right.
- "Is the per-site cut measure genuinely a product measure in the variables expanded?" **Yes.**
  - The interpolated variables are the per-site scalings s_y of Z_y = Z(y) ∈ R^n.
  - ν_∅ factorises over exactly those sites.
  - The slice is not an obstruction: 𝒞 = Π_UÕ^{-1/2}Π_U acts on the full white noise, whose gauge-direction components are
    killed by 𝒞 (SF-WN). The measure stays the unconstrained product μ_wn, cut per site.
- **Remark (cost, l.745-746, and SF l.423-424): the e^{272κ'} factor and the rate loss 1/273 are not "only an existence
  matter".** They block iteration (B-5).

### B-4. Corollary CE-exp-𝒞 (l.628-633, l.752-756): CONFIRMED (not counted)
- |s_y| < 2e^{μδ(y,X)};
- δ(y, X) ≤ ℓ^∞(y, x(b)) + δ(x(b), X) ≤ d(b, y) + δ(x(b), X);
- |A_b| ≤ 2pN_μ(|𝒞|)e^{μδ(x(b),X)}.

All right. The strictly-local reading is the important case. A site in X sees the far scalings only through 𝒞's tail. That is
why the lemma works without finite range.

### B-5. Corollary CE-exp^0 (l.634-640, l.758-774): CONDITIONAL, CONFIRMED-WITH-FIX
- Re-derived:
  - the M ≥ 2L + 1 pattern placement (diameter < M ⇒ two consecutive indices per coordinate ⇒ common vertex ⇒ d = 0,
    |X| ≤ 16);
  - h_0's three entries (128S_T(2√NpN)³g_0/r_T³ = 2S_T(4ρ'/r_T)³/g_0², with ρ' = 2g_0√NpN);
  - SF-J (5) on complex A (|λ_a| ≤ ||A||_op; the Σ_{a,b}|λ_a - λ_b|² identity and Schur hold for complex matrices);
  - SF-src at ρ' ≤ r_𝔫/2;
  - the count 16M⁴n_*.

  The per-term linear parts Dτ·A are not zero individually, but their sum is zero identically (SF-T0 (5)), so dropping them is
  exact.
- **Fix CE0-1 (l.760):** the distance caveat is void. d = ℓ¹ torus distance of base points (PROOF l.5122) ≥ ℓ^∞, and
  N5-sf0 (b)'s ℓ¹ bound holds for every m'' ≤ m_1. Delete "[not checked …]". CE-exp^0's hypotheses are then exactly
  (FP-loc)_0 + (SF-N♮) + SF-A2^0's background clause.
- **Fix CE0-2 (scope sentence):** the cut-good term is the ν_∅ term of a decomposition of an integrand that contains the chart
  indicator 1_D(𝒞Z) (SF-A2^0 l.345: the chart identity holds only where every ||1 - U_0(b)U(V)_b⁻¹|| ≤ ε^thr_N).
  - On supp ν_∅, 1_D ≡ 1 (ρ' ≤ r_T/8). Correct.
  - On Q ≠ ∅ terms 1_D(𝒞Z) is a NON-LOCAL function of Z. Add this to (CE-Q)'s statement.

### B-6. Corollary CE-exp^k (l.641-645, l.776-787): CONDITIONAL, CONFIRMED-WITH-FIX (scope); "(OP-loc)_k retired" WITHDRAWN for the activity half
- What is right:
  - the one-variable Cauchy bound |R_x| ≤ 2S_k(ρ/ρ_k)³;
  - 𝒫_X(ρ, μ_k) ⊂ 𝒫_{{x}}(ρ, μ_k) (δ(x(b), X) ≤ ℓ^∞(x(b), x));
  - the reduction to CE-exp-𝒞's weighted form.

  As an implication it is valid.
- **Fix CEk-1 (the hypothesis is not viable as stated).** (L-hol)_k asks 𝓔_{k,x}(e^AU) to be holomorphic and bounded for
  |A_b| < ρ_ke^{μ_kℓ^∞(x(b),x)}, at ALL b.
  - 𝓔_{k,x} is an energy density of the critical chain of E^♭(·; U) (HIST A5). The chain exists only on small-field domains
    (R_δ, 𝔇_{ε,α}).
  - At distance d the polydisc contains link variables e^{A_b} with |A_b| ≍ ρ_ke^{μ_kd}. There no critical chain exists, and
    the density is undefined, let alone bounded by S_k.
  - A toy shows the obstruction: f(A) = Σ_y e^{-κ|y|}log(1 + A_y) is exponentially local with derivative decay, but it is not
    holomorphic on any growing polydisc.
  - SF's "[inference]" (l.785-787: A5 (B) "with growing data allowed") does not survive this: A5 (B)'s contraction is in
    level-k sup-norm polydiscs (REVIEW_HIST_S4 l.250-251).
  - **Replace (L-hol)_k by (L-loc)_k:** 𝓔_{k,x} = Σ_{R∋x}𝓔_{x,R}, with 𝓔_{x,R} depending on A on R only, holomorphic and ≤
    S_ke^{-κ_Ld(R)} on the UNIFORM polydisc max_{b∈R}|A_b| < ρ_k. That is REVIEW_SF_S1 OP-3's localisation of the main term.
  - Then each piece is strictly local, and CE-exp-𝒞's strictly-local branch applies with X ⊃ R. κ_L in M-units is ≈ κ_5M,
    huge, so the rate requirement is met.
  - (L-loc)_k is derivable in principle from multi-derivative decay of 𝓔 on a uniform polydisc. That needs A5 (C) for all
    mixed derivatives, not only the first, and it is inside the B-NA wall.
- **Fix CEk-2 (missing activities; the rate budget).** At stage k the integrand also carries the inherited level-k polymer
  activities of (I_k^E)', with finite rate κ_in in M-units. CE-exp needs κ_in ≥ 273κ' + 1296W.
  - CE-exp's output rate is κ_c - 3κ_0 - 3. SF-blk returns L(κ - κ_0) - 1.
  - For every κ_c and L = 3, L(κ_c - 3κ_0 - 3 - κ_0) - 1 < 273(κ_c + 16 log 2) + 1296W, so the rate does not reproduce.
  - The norm does not either: the output size is ≍ C_1H'_0 ≤ C_1c_0, while the input must be ≤ e^{-272κ'}c_0.
  - Only SF-geo's multiplicative collar bound causes this. HULL's far-site part is additive, and so is an O(1)-per-polymer loss.
  - **New OPEN name (CE-col):** Theorem CE re-proved with collar-native Mayer connectivity. Polymers X_i are linked when
    X_i^+ ∩ X_j^+ ≠ ∅, the counting constant becomes 5⁴, and the output rate is κ - const with no factor 1/273. This is SF's
    own Remark (cost) (l.423-424). It is **needed** for any level-k use, not optional.
  - State CE-exp^k with the inherited activities and (CE-col) as hypotheses, or restrict its statement to the three listed
    activity types (then it is not the stage-k expansion).

### B-7. (CE-Q) (l.646-648, l.789-793): OPEN, ACCEPTED as named; statement to be completed
The inference (excise a region of radius ≍ (log λ)/m_1 around a Q-site with |Z_y| = λp, pay with e^{-λ²p²/4}) is the right
shape. In M-units the radius is ≈ log λ/(m_1M) ≤ log λ/1539, so the polymer cost is cheap. **Add** (Fix CQ-1):
- the non-local chart indicator 1_D(𝒞Z) on Q ≠ ∅ terms (B-5);
- the fact that on Q ≠ ∅ terms the Gaussian–Haar identity holds only on the chart. Outside it the integrand is the original
  Haar integrand, not a Gaussian one, so the excised region must be priced in U-variables (RLARGE branch (ii)), not in Z.

---

# PART C: Lemma SF-J', Lemma SF-src, (SF-N♮)

### C-1. Lemma SF-J' (l.686-689, l.843-857): CONFIRMED (not counted)
- (1) e^A = U ⇒ [A, U] = 0. Distinct eigenvalues ⇒ A is diagonal in U's eigenbasis with θ_a ∈ φ_a + 2πZ, and the
  spread < 2π puts all θ_a in [min θ, min θ + 2π).
- S(c) is non-decreasing, with jumps of exactly 2π, S(c + 2π) = S(c) + 2πN, and S ∈ 2πZ (det U = 1). So 0 is taken on
  exactly one constancy interval. Existence and uniqueness are both right.
- (2) D''_N has a null complement in D'_N. exp: D''_N → U_dist is a bijective local diffeomorphism (j > 0 since
  |θ_a - θ_b| < 2π), hence a diffeomorphism. log j is holomorphic near D'_N (spectral radius of ad A = spread < 2π < SF-J (4)'s
  2π radius).
- Same c_N, as in SF-J (1).
- REVIEW_SF_S1's sketch is now a proof.

### C-2. Lemma SF-src (l.690-692, l.859-863): CONFIRMED (implication ⇐ NORM-an + (SF-N♮); not counted)
- φ is holomorphic on |ζ| < r_𝔫, and |φ| ≤ K_𝔫(y_bg + c_y|ζ|)².
- R := max{y_bg/c_y, 2ρ} ≤ r_𝔫, and |φ'| ≤ 2sup_{|ζ|≤R}|φ|/R on |ζ| ≤ R/2. The two cases give 8K_𝔫c_yy_bgρ and ≤ 9K_𝔫c_y²ρ².
- Two small fixes:
  - (Fix src-1) when R = r_𝔫 the sup is over a closed disc on the boundary of the holomorphy domain. Use R' < r_𝔫 and let
    R' ↑ r_𝔫, or require y_bg/c_y < r_𝔫 strictly;
  - (Fix src-2) the bound is the max of the two terms, not their sum. The displayed sum is valid but weaker.
- At y_bg = 0 the O(ρ) term vanishes. This is consistent with EXISTENCE NA-3 and REVIEW_SF_S1 R5.

### C-3. (SF-N♮) (l.693-695): OPEN, ACCEPTED; likely short
REVIEW_HIST_S4 M-3 already shows the contour spread is gauge invariant and ≤ 1.011√NA_dε_R by the lasso. The linear bound
y(e^AU) ≤ y_bg + c_y max|A_b| for complex A is then a BCH estimate on each contour product of ≤ p_L links (c_y ≈ 2p_L).
Recommend proving it in the next session. It is cheap, and it removes one of CE-exp^0's two hypotheses.

---

# PART D: STEP 3

### D-1. (a5-G♯) (l.653-658): CONFIRMED as the S4-1 restatement, two wording fixes
- **Fix G♯-1:** §33 defines d as "the ℓ¹ torus distance between coarse positions L^{l-k}·(base point)" (RTARGET l.583-584).
  "Level-k ancestor distance" is REVIEW_HIST_S4's phrase. The two agree to O(1), so use §33's.
- **Fix G♯-2:** the weights e^{-md} (growing data) are B-NA-red's (PROOF l.3152), not §33's; §33 defines only w = e^{+md}.
  Cite B-NA-red for the ± pair.
- Otherwise (a5-G♯) is what B-NA-red's (G♯) says at ψ^r (PROOF l.3153, l.3166-3169, X = X_c Hölder, Y = divergence-form
  with ω, D = ||·||_{D,m}).

### D-2. Lemma BS (l.663-665, l.802-807): CONFIRMED (not counted)
- R_ε(X) = {||1 - V_p|| ≤ ε} (HIST l.1549) and the real points of P_s are Ue^X, X ∈ su(N), ||X|| ≤ s (HIST l.1552-1553).
- The four-factor telescoping with unitary factors, e^s - 1 ≤ 1.01005s ≤ 1.0102s, and 4.05·(ε_1/5) = 0.81ε_1 are all right.
- This closes S4-2's arithmetic (REVIEW_HIST_S4 l.262: 2ε_1 + 4.04s_5).

### D-3. Lemma G-pert (l.666-671, l.809-821): CONFIRMED as an implication; its "Reading" is OVERSTATED
- The Neumann bound is right: ||𝓛^{-1}D_x𝔑|| ≤ 2GC_Rt ≤ ½ ⇒ ||𝓛(x^r)^{-1}|| ≤ 2G, and the data bound is 2(G_D + GC_Rt). The
  re-centred-remainder remark (radius ≥ 3, (8/3)C_R) is also right.
- **Fix GP-1 (identification).** G-pert inverts the Hessian of E_NA∘exp + ½||Γ_gf·||² **in the trivial slice at x^r**.
  (a5-G♯) is stated "in a per-level covariant slice THROUGH ψ^r" (l.655). These are different gauge-fixed operators:
  - the slice functional and the Feynman term are re-centred;
  - the residual groups move.

  An equivalence lemma is needed: the two slice Hessians at a critical chain are conjugate by a gauge-chart change, bounded in
  the §33 pair. Or state (a5-G♯) at X_c-small chains in the trivial slice. The second is the natural choice; NA-IFT works there.
- **Fix GP-2 (reach).** G-pert's hypothesis t ≤ min{…} with t ≥ ||B^r||_D requires the data to be small in ONE global gauge.
  That is exactly B-NA-red's class (||B_k||_D ≤ ε_0, PROOF l.3148), and G-pert is the Neumann step inside NA-IFT's proof. It
  adds no case beyond B-NA-red.
  - Withdraw l.817-818's "(a5-G♯) follows from the trivial-chain items … no new wall" and l.681-683's "by G-pert they reduce
    to the trivial-chain items … plus (G♯-patch) and (MIN-reg)".
  - Correct reading: "(a5-G♯) on B-NA-red's class ⇐ (G♯_0-field) + (R♯_ω) + (FP♯') [+ GP-1]. For every U ∈ R_{3ε_1}(Λ_k)
    without a globally small gauge (BNA-F4), (a5-G♯) is (G♯-patch), and that is the whole difficulty."

### D-4. Proposition U-red (l.679-680, l.823-833): CONFIRMED (implication; not counted)
- The minimiser is critical in every direction on the boundaryless manifold. With Γ_gf(x') = 0 the Feynman gradient vanishes.
- x' is a fixed point of Φ = -𝓛_r^{-1}𝔑_r(·; 0), and so is 0. Lip Φ ≤ 2GCr_U ≤ ½ ⇒ x' = 0.
- The post-proof precision (COMPLETE gauge h = 0 and Γ_gf = 0, via (FP♯')) is necessary, and it is disclosed.
- The remark that own-unit regularity does not give X_c-closeness (L^{2k} factor) is right and important.

### D-5. (G♯-patch) (l.672-675): NOT PRECISELY STATED (name kept)
- It is a description ("needs a patching … into a global inverse"), with no constants, quantifiers or conclusion form.
- **Fix GPa-1:** state it as "there are G', G'_D, G'_w, G'_{D,w}, m'_G, depth-uniform, depending only on the trivial-chain
  constants and (C_R, ρ_0), such that for every real U ∈ R_{3ε_1}(Λ_k) and every ε_R-regular critical chain ψ^r, (G♯) holds in
  the slice through ψ^r with these constants."
- Say what it then is: (a5-G♯) minus B-NA-red's small-gauge class, i.e. the non-abelian N5-sf0-type local-gauge patching in
  Schauder norms. That is the B-NA wall itself (REVIEW_HIST_S4 strategic 3), not a new sub-item of it.

### D-6. (MIN-reg) (l.676-678, with l.823-825's precision): PRECISELY STATED; owner lane D
It is precise once the gauge is the complete one: ∀ minimisers ψ, ψ', ∃ a chain gauge trivial at level k with ψ' = ψe^{x'},
x' in the complete gauge through ψ, ||x'||_{X_c} ≤ r_U. But it is the global part of (a5-U) renamed: U-red is "a priori
closeness + local uniqueness". REVIEW_HIST_S4 assigns (a5-U) to lane D. Record (MIN-reg) as lane D's, not lane F's. Merge the
"(Linear case … [inference])" sentence into lane D's (a3-q) linear-case target.

---

# PART E: s2 (MANDATORY NUMERIC LOCK) and check design

- **Provenance.**
  - s2_criteria.md: born 2026-10-28 03:46:33 UTC, never modified; md5 366105b1… = SF_LOG.
  - s2_sf.py: born 03:47:49 UTC, after the criteria.
  - Output and timing written 03:52:08-03:52:17 UTC.
  - No post-run edit (mod = birth for the criteria and the script).
- **Re-run (this review).**
  - Lock: `until mkdir …/locks/numeric 2>/dev/null; do sleep 20; done`; acquired 04:05:44 UTC after another holder released.
  - Load 5.46 (< 8, checked inside the lock before running); 40% free.
  - nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; `python3` without -I; no `timeout`; no trap.
  - Exactly one `rmdir`, released 04:05:53 UTC.
  - 8.78 s, peak RSS 61 MB, exit 0.
  - **Output byte-identical to checks/s2_out.txt** (the lock lines excluded): OVERALL PASS 14/14. Record:
    scratchpad revSF2/rev_time.txt.
- **Code review (line by line):** no bug.
  - The A3 bound h is a valid sup of |H| over the reached polydisc.
  - The C2 log-domain W is exactly the theorem's W.
  - The D reconstruction (expm(A) = U, tr A = 0, spread < 2π on 500 samples per N) is the informative part of D3.
- **Design weaknesses (informational; no criterion is false):** five criteria cannot fail for a correct implementation of the
  construction.
  - A1: Möbius inversion is an identity.
  - A2: the pieces never read the off-set Z by construction.
  - B2: |Δ|_2 ≤ 2|Δ|_∞ in d = 4.
  - D3's window count: K + j + Nm = 0 has exactly one solution with j ∈ {0, …, N-1} for every integer K, so the count never
    sees the eigenvalue structure.
  - E2 is arithmetic. E1 is the triangle inequality, nearly so.

  The evidential criteria are A3-A4, B1, B3, C1-C2, D1-D2, D3 (reconstruction) and E1. A future check should test LOC-s's bound
  at its edge, e.g. an H with a singularity just outside the reached polydisc, so that A3 could fail.

---

# PART F: does CE-exp (or an easy extension) supply EXISTENCE §19.4 (CE-cond)?

**Verdict: NO.** Not by CE-exp^0, not by CE-exp^k, and not by an easy extension. (CE-cond) (EXISTENCE l.3893-3900) asks for:
(a) a lower bound on Cov(θ(D)^*, D | U_{j'} = V) of (1 - r)g_j⁴A_* with r ≤ ¼; (b) a bounded oscillation of E[D | V]. Both are
for P_K-a.e. V ∈ G_R, with V arbitrary (large-field allowed) outside N_R, at level j = K - m_* (deep), over n ≍ log(1/g)
levels j → j', uniformly in K, T and n. Against that:
1. **Levels.** CE-exp^0 is stage 0. (CE-cond) lives at deep levels and needs CE-exp^k. CE-exp^k rests on (L-hol)_k, which is
   not viable as stated (B-6). It also omits the inherited polymers, and its rate budget does not close (B-6, CEk-2). That
   needs (CE-col).
2. **n steps with a prescribed endpoint.** (CE-cond) is about the chain conditioned on U_{j'}. It needs (SF^J)_i for n
   consecutive i (A1-A4, including (SF-irr) extraction), with constants uniform in n up to log(1/g). CE-exp is one stage of A3.
3. **Local background.** (CE-cond) allows large-field coarse regions outside N_R, with influence e(R) → 0. CE-exp^0 is stated
   for backgrounds in N5-sf0's global class 𝔑(α_*). The region form is (N5-reg)_k plus the large-field localisation. The cut
   complement is (CE-Q).
4. **Source.** The easy extension would be a bounded local complex source λD as one more strictly local activity. That works
   in CE-exp's framework for one stage: CE-exp-𝒞's strictly local branch, |λ| small. It gives a one-stage conditional
   covariance with a relative correction r = O(g_0)·(the extreme constants: e^{1.28·10⁵}-type, N_{m_1}(|𝒞|)³). That is ≤ ¼
   only for astronomically small g. That is allowed for existence, but it is still one stage at stage 0. So it supplies none of
   1-3.

**What CE-exp does contribute to (CE-cond):** the mechanism. A per-site-cut white-noise expansion with no finite-range or
s-walk input is the right engine for (CE-cond)(a)'s one-step leading-order analysis at small-field backgrounds. Once (CE-col),
(L-loc)_k, (N5-reg)_k and the n-step reproduction exist, it is what one would run, with the observable as a local activity.
Record (CE-cond) ⇐ [ARGUED] {CE-exp^k with (L-loc)_k + (CE-col), (SF^J)_i for n steps with prescribed endpoint, (N5-reg),
(CE-Q) + large-field localisation}. This refines EXISTENCE §19.5's item list (owner EXISTENCE). It does not change (CE-cond)'s
status (HYPOTHESIS-NEW).

---

# PART G: corrected tally and binding fixes

**Tally of SF.md after session 2 (all items reviewed here):**
- PROVEN-HERE 20 + 1 standard (SF's count stands):
  - counted 7: SF-J, SF-T0, SF-DC, CE^+, SF-blk, LOC-s, CE-exp. All CONFIRMED.
  - not counted 13: SF-thr, SF-cut, SF-N0, SF-WN, SF-geo, SF-V, SF-J', SF-src, HULL, CE-exp-𝒞, BS, G-pert, U-red.
    - CONFIRMED: all except G-pert.
    - G-pert is CONFIRMED as an implication, with Fixes GP-1, GP-2 and its reading withdrawn.
- CONDITIONAL 4:
  - SF-thr-k: ⇐ (H-K) + (H-C) + (H-G) + (H-ℂ) after the R21 fix.
  - SF-A2^0.
  - CE-exp^0: ⇐ (FP-loc)_0 + (SF-N♮); caveat removed.
  - CE-exp^k: ⇐ (L-hol)_k, NOT VIABLE AS STATED. Replace by (L-loc)_k + (CE-col) + the inherited activities.
- ARGUED 2: (CE-s) (alternative route), SF-A3^0 (Q ≠ ∅ part).
- OPEN names:
  - (SF-N♮) (short);
  - (FP-loc)_k;
  - (N5-reg)_k;
  - (CE-Q) (Fix CQ-1);
  - **(L-loc)_k** (new, replaces (L-hol)_k);
  - **(CE-col)** (new);
  - (a5-G♯) [B-NA];
  - (R♯) at ψ^r [B-NA];
  - (G♯-patch) (NOT PRECISELY STATED; Fix GPa-1);
  - (MIN-reg) [lane D];
  - (a5-U), (a3-q) on R_{3ε_1} [lane D].
- 0 GAP, 0 WRONG.
- **No change to PROOF.md's tally.** SF discharges no RLARGE §4.2 row. Row 3's stage-0 A3 cut-good part moves from ARGUED to
  CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮), as SF says.

**Binding fixes (next SF session):**
1. **CEk-1:** replace (L-hol)_k by (L-loc)_k (uniform-polydisc localisation of the main-term densities). Withdraw "(OP-loc)_k
   retired" for the activity half at l.175-177, l.645, l.783-787 and §8.1 l.884/l.891. Withdraw the l.785-787 inference.
2. **CEk-2:** add the inherited polymer activities to CE-exp^k and record the rate/norm non-closure at L = 3. Name and attack
   **(CE-col)** (collar-native Theorem CE). Rewrite Remark (cost) l.423-424 and l.745-746: the 1/273 loss blocks iteration.
3. **CE0-1:** delete the distance caveat (l.760): d is ℓ¹ (PROOF l.5122).
4. **CE0-2 / CQ-1:** add to (CE-Q) the non-local chart indicator and the U-variable pricing outside the chart.
5. **SF-thr-k (stale, R21):** re-base on PROOF's current NAH-unif: + (H-G), (H-ℂ); margin ≈ 8, closed-input K_p^♯ ≈
   0.11-0.13. Do this at l.251-257, l.876, l.905.
6. **BG-1:** correct the sentence at l.84-85: (i) under (H-K), (H-C), (H-G), (H-ℂ); (ii) = (H-ℂ); (iii) not supplied.
7. **GP-1, GP-2:** state (a5-G♯) on B-NA-red's class in the trivial slice, or prove the slice-change equivalence. Withdraw the
   "no new wall / reduce to trivial-chain items" readings (l.681-683, l.817-818). Say that the generic case is (G♯-patch).
8. **GPa-1:** state (G♯-patch) precisely, as in D-5.
9. **G♯-1, G♯-2:** §33's coarse-position ℓ¹ distance; cite B-NA-red for the e^{±md} weights.
10. **src-1, src-2:** strict inequality or a limit for R = r_𝔫; "max" in place of "sum" (optional).
11. **Stale text:** tag §4.2 bullet 2 and §4.3's "(OP-loc)_k necessary". l.127: "reviewed by REVIEW_HIST_S4".
12. **SF-thr-2:** check ε^J_loc (HIST §4-§5) or keep it explicitly as an assumption in the status line.
13. **(MIN-reg):** re-home to lane D (owner note in §8.3).
14. **Check design:** the next check must include at least one criterion that a wrong bound could fail at the edge of LOC-s
    (Part E). Label the tautological criteria as such in the outcome.

---

# PART H: strategic verdict: (CE-Q) vs (L-hol)_k vs (MIN-reg)

**Verdict: attack (CE-Q) next, together with the cheap (SF-N♮), and add (CE-col) as the first item of the k ≥ 1 programme.
Do not attack (L-hol)_k in its current form. Hand (MIN-reg) to lane D.**

1. **(CE-Q)** is the only remaining stage-0 A3 item fully inside lane F. With (SF-N♮) (a short BCH/lasso estimate, C-3) and
   (FP-loc)_0, it would make stage-0 A2 + A3 complete: the first complete small-field step of the programme. Its failure mode
   is concrete: excised regions of M-radius ≈ log λ/1539, priced by e^{-λ²p²/4}, with the chart indicator treated in
   U-variables. It is session-scale.
2. **(L-hol)_k** as stated is very likely false for implicit-function densities (B-6). Its corrected form (L-loc)_k needs
   mixed-derivative decay of the main term on a uniform polydisc, i.e. A5 (C) beyond first order. That sits behind (a5-G♯)
   and (G♯-patch), the B-NA wall. Attacking it now would duplicate the B-NA lane.
3. **(MIN-reg)** is the global half of (a5-U). REVIEW_HIST_S4 strategic 3 already routes (a5-U), (a3-q) to lane D, and U-red
   has done the lane-F part (local uniqueness from (G♯) + (R♯)). Lane F should not take it.
4. **(CE-col) before any k ≥ 1 use.** Without it, CE-exp cannot be composed across levels at L = 3: a rate factor 1/273 and a
   norm factor e^{272κ'} per pass. It is a modification of Theorem CE's Step 1 counting: linking through collars, constant 5⁴.
   It should be done as soon as stage 0 closes. It also sharpens CE-exp^0's H'_0 by removing e^{272κ'}.
