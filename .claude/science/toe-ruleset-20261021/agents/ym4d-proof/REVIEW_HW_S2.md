# REVIEW_HW_S2: hostile review of lane H session 2 (HW.md §0-§11 [RHW1-fix] edits, §12A-§17; checks/w2_*)

Reviewer: an independent agent that wrote none of HW.md, HW_LOG.md or checks/w2_*. I edited no other file. No commits, PRs
or pushes.

Inputs (read-only; md5 at review time): HW.md 7937a648… (868 lines), HW_LOG.md 672459250…, REVIEW_HW_S1.md 53c3115d…,
SQ.md 42ded0fa… (§0, l.45-233: INF, MSG-dec, SUP-price, FORCE, (REG-min), DESC, PRICE-iii), RLARGE.md 24a73553… (§1.0-§1.2
l.107-195, §3 l.287-378, §4 l.382-453, §5 l.457-488), HIST.md 468e9f03… (§7.1-§7.5 l.452-601: H-nest, H-geo, HIST-sum, n_H,
(P3), P4-div; §14.1 l.842-871; §20.3 l.1307-1376), checks/w2_criteria.md, w2_relseq_toy.py (02f9a7a8…), w2_out.txt
(0d33f8b8…), w2_time.txt, w2_stderr.txt, with mtimes. Scratch (the w2 re-run): scratchpad `rw2/`.

"Line" means a line of HW.md unless another file is named. Status words as in PROOF.md.

---

## Bottom line

- **[RHW1-fix] edits and the (AE) → (CLS-min) switch: CONFIRMED.** Every use (TE (ii), W-bad, W-cb, FV, SAT) consumes
  only the cone-local infimum. The min-form constants c_pr = c_♭/C'², t_pr = C'τ_♭ follow from DESC (a)+(b), and I re-derived
  them. Caveat: the primary source (REG-min) → DESC/SUP-price is SQ session 1, which is unreviewed. (CLS-min) remains a
  hypothesis of Theorem HW, so nothing in HW is weakened.
- **Lemma REL-seq: CONFIRMED-WITH-FIX (counted).** I re-derived the telescoping, the containment, DECL, the step price
  (H-geo (iv)), the depth absorption, and the count 82Σ|Ω^c_j|.
  - **One binding fix (RS-1):** restrict the family to the laws that actually occur, R_{S,E} with S ⊇ S(𝔥), and preferably
    level-first ascending. The claim "any order, (PRICE^ℛ) on all of ℛ" (l.660-661) makes the consumed hypothesis
    strictly stronger. It even contains the plain chain (S = ∅).
  - **One binding fix (NA-1):** (NA-∅) (l.673) as written omits the vacuum c-number 𝒱_K^{LF}. HW's own Remark GAS shows
    that 𝒱_K^{LF}/|T| is not O(e^{-a'/g_K²}), so the statement is false in kind unless e^{𝒱^{LF}} is put in.
- **Theorem HW^cap + H4-red': CONFIRMED-WITH-FIX (counted).** The proof is right. The rate claim "θ up to ≈ 1/6"
  (l.729, l.854) is an overclaim (fix CAP-1).
  - 6θ < 1 is the mismatch condition only.
  - The fine factor still carries TE (iii)'s overlap 24: Y^f = 24u_{k+1}F^col (l.693). (SF-cap) is therefore a moment at
    rate 24θ(1 + 2Rg_K²), which by W-1's own heuristic needs 24θ(1 + 2Rg_K²) < 1.
  - What is removed is Hölder's 2 and W-bad's 2 (96 → 24), and above all the depth degradation. That part stands.
  - (LI^F) should be stated only for the capped weights it consumes (fix LI-1).
- **CAP-dec: CONFIRMED, RECOUNTED as uncounted.** It is a pointwise two-term expansion plus a union over choice functions,
  i.e. elementary, like HÖ.
- **SAT, LOOP-div, LOOP-const: CONFIRMED as arithmetic about bounds.** SAT is a property of the upper split TE (i)/(iii)
  evaluated at the actual finer field. It is NOT a property of the measure: a returned finer defect does not make the coarse
  plaquette bad.
- **THE ARCHITECTURE VERDICT (Priority 5): (SDP) is the right inequality, but it is the wrong wall for this file, and HW's
  route to it is exactly the route the R-operation exists to avoid.**
  - LOOP-const is LF-count at n = 1, i.e. cross-level bookkeeping of the returned gas inside one column.
  - (SDP) at level k must be a per-level output of node A's R-operated representation, not something induced from level
    k - 1.
  - With (SDP) re-owned that way, there is no recursion and LOOP-const does not arise.
  - The unreturned condition (n_♯ + 1)aβ_- > 4 + c_B does NOT close LOOP-const. It closes only HIST-sum's multi-cube count.
    The chain LOOP-const describes consists only of returned cubes (by DJ), one per level.
  - Details and the restated (M-f) are in §5.
- **w2 re-run: every result line reproduced byte for byte. OVERALL PASS.** Two disclosure gaps:
  - B2 checks a strided subsample, but the criteria say "all".
  - The criteria (04:00:33 UTC) already contain §14-§15's lemma names and constants, although HW_LOG dates §13-§15 to
    04:01-04:02.
- **Corrected tally: 6 counted** (4 from session 1, plus HW-6 REL-seq and HW-7 H4-red' + HW^cap), not 7.

---

## Priority 1. [RHW1-fix] edits and the (AE) → (CLS-min) switch

### Fix-by-fix (l.17-19, 41-43, 86-98, 112-113, 150-157, 175-186, 199-208, 219-221, 235-238, 257-261, 265-278, 289-296, 298-316, 341, 360-365, 392-419, 430-445, 495-528)
- **W-1** (l.299-301): θ ∈ (0, 1/96), with the reason stated. Applied.
- **W-2** (l.175-186, 203, 598-600): C_cone of RH3-fix N-4. I checked a_bad's size via (AE):
  - ε_1²/(2N·C_cone) with C_cone = 1.1-2.3·10¹⁵ and N = 2 gives (1.1-2.3)·10⁻¹⁶ε_1².
  - Via (REG-min): c_♭τ_♭² ≤ (1/640)(10⁻⁸/(53C_D²))² ≈ 5.6·10⁻²³/C_D⁴.
  - Both CORRECT.
- **W-3** (l.313-315): θ < 1/(96·82) for collars. **W-4** (l.307): C_ℓe^{aR} in C_H. **K-1** (l.438-440). **H-1 … H-11**,
  **S-1**, **S-2**. FV recounted (l.265-266), tally 4 (l.511-514). All applied as the review asked.
  - H-11 is corrected in place, and as an appended HW_LOG line (HW_LOG l.33-36), not by rewriting the log. Correct
    procedure.
- **One residue (recommended, H-12).** §10 W2 (l.500-505) still says "(H-w) ⇐ (AE) + …" and "(REL) is OPEN [P]". The
  bracket at l.495-496 covers this, but the bullet itself is unmarked. Add "[superseded, §16-§17]" inline.

### The (AE) → (CLS-min) switch, use by use (§12A l.577-600): CONFIRMED
- **Definition.** ℰ_P(V) (l.162) is an infimum over the finer fields. E_𝒞(P) reads them only inside 𝒞(P) and reads V only on
  ∂P (top terms φ_{M̄_c(U_{m-1})}(V_c), c ∈ ∂P). So ℰ_P(V) = SQ's 𝓔^{𝒞(P)}(V) (SQ l.65), and TE (ii) is (CLS-min) verbatim.
- **TE (ii) min-form constants.**
  - DESC (a): θ ≥ C'τ ⇒ 𝓔 ≥ c_♭τ² = (c_♭/C'²)(C'τ)².
  - DESC (b): θ < C'τ ⇒ 𝓔 ≥ c_♭min{θ/C', τ}² = (c_♭/C'²)θ².
  - Together: 𝓔 ≥ (c_♭/C'²)min{θ², (C'τ_♭)²}. **c_pr = c_♭/C'², t_pr = C'τ_♭: CORRECT.**
  - The alternative via (AE) is c = 1/(2NC_cone), t = 2 (||1 - V||_op ≤ 2, and CLS-red's 2/η_E branch covers E ≥ η_E).
    CORRECT.
- **W-bad:** X_Q is a sum of infima, and some P has ||1 - V_P|| ≥ ε_1. Infimum only.
- **W-cb:**
  - (α)/non-quiet at level k ≥ 1 is CLS-min. At k = 0 it is s ≥ ||1 - U||²/(2N) ≥ c_pr·min{·} (c_pr ≤ 1/(2N) for both
    sources).
  - (β) is KQ/PM, with no (AE). CORRECT.
- **FV:** the lower bound is CLS-min at every top V. "Every U" comes from TE (i), which is unconditional. CORRECT.
- **SAT (l.736-738):** F^col_Q(U_k) ≥ ℰ_P(U_k), an infimum over a subset of nonnegative terms. Infimum only. CORRECT.
- **Scope notes:**
  - (a) PRICE-iii is for cone tops at level ≥ 1, and level 0 stays on (B). HW does this correctly at W-bad l.206 and W-cb
    l.221.
  - (b) DESC needs level-k side ≥ 3 and τ ≤ min{τ_F, τ_R, …}. HW carries "level-m torus side ≥ 3" (l.175). τ_R comes from
    (REG-min) itself.
  - (c) **Provenance.** "(SQ session 1, PROVEN-HERE there given (REG-min), not yet reviewed)" (l.181-182, 594) is honest.
    The verdict on HW does not depend on SQ's review, because (CLS-min) is a named hypothesis of every HW statement that
    uses it (l.299, 520-523).

---

## Priority 2. Lemma REL-seq, Lemma DECL, (NA-∅), Remark GAS

### Lemma DECL (l.615-625): CONFIRMED (elementary, uncounted)
- **The identity.** On {𝒟 ⊂ D_j}, D_j ∪ E = D_j ∪ E', so 1_{R_{S,E}}1{𝒟 ⊂ D_j} = 1_{R_{S,E'}}1{𝒟 ⊂ D_j}. Integrating against
  W and dividing by Z(R_{S,E}) ≥ Z(R_{S,E'}) (m1) gives the claim. CORRECT.
- **LI-a on declared cubes (bad-only).**
  - The level-j factor reads ζ_{Q'} only for Q' ∉ 𝒟, and those cubes' interior links are disjoint from int Q.
  - Other levels read other fields (ζ at level j' reads only U_{j'}). CORRECT.
  - This needs the bad-only, history-independent defect notion, and §13's preamble (l.604-605) restricts to it. With
    collar clauses, the neighbours' σ_{Q'} read N_1 data and the claim fails, which is K2's territory. Stated.

### Lemma REL-seq (l.634-661): CONFIRMED-WITH-FIX (CONDITIONAL, implication proven; counted [HW-6])
- **(1) Telescoping.**
  - S_N = all, because the relaxed pairs are exactly Σ(Ω^c_{j-1}) ∪ N_1(𝒰_j), the complement of S^{(j)}(𝔥).
  - The chain R_{S_{i+1}} ⊂ R_{S_i} holds by (m1).
  - The ratio is Π μ_{R_{S_i}}(R_{S_{i+1}}). CORRECT.
- **(2) Containment (S2-F1).**
  - x ∈ D_j: otherwise D_j ∩ S_{i+1} = D_j ∩ S_i.
  - x ∈ C: a component C of D_j ∩ S_{i+1} with x ∉ C lies in S_i, and it is a full component of D_j ∩ S_i. Any component of
    D_j ∩ S_i that meets C is *-connected inside D_j ∩ S_{i+1}, hence lies in C.
  - The BFS-truncation subanimal of exactly n_♯ + 1 cubes through x exists. CORRECT.
- **(3) Step price.**
  - Lemma H-geo (iv) (HIST l.491) gives Σ_{m=j}^{K-1}|sh_m(𝒟)| ≤ 38417(n_♯ + 1) + 38416(K - 1 - j). The (F_R) lower half
    gives e^{-au_j} ≤ e^{-au_K}e^{aR}L^{-aβ_-(K-j)}.
  - The bracket is ≥ 0 iff (n_♯ + 1)aβ_-log L ≥ 38416c. This is implied by n_♯ ≥ n_H(B_0) with B_0 ≥ c, since
    (n_H + 1)aβ_- > 4 + c_B ≥ 38416c/log L. CORRECT.
  - **Cosmetic:** e^{38416c(K-1-j)} = e^{-38416c}·L^{(K-j)·38416c/log L}. The text writes e^{+38416c} (l.636, l.653). That is
    a valid over-estimate by e^{76832c}, but it is not the identity the line suggests. Recommended: write e^{-38416c}, or say
    "≤".
- **(4)-(5).** -log(1 - p) ≤ 2p on [0, ½], and N ≤ Σ_j(|Ω^c_j| + 81|𝒰_j|) ≤ 82Σ_j|Ω^c_j|.
  - The first term uses H-nest (i): Σ(Ω^c_{j-1}) ⊂ Ω^c_j (HIST l.472).
  - Σ_j|Ω^c_j| ≤ the shadow sums by HIST-sum step (2).
  - **B = 164ε_♯ → 0 at fixed n_♯: CORRECT.**
- **Order of constants (l.659-661).** a, C_ℓ, c → B_0 := B_1 + c + 1 → n_H → n_♯ → g_0(n_♯). Non-circular. Note: at the
  recorded a ≈ 10⁻¹⁷, n_H ≈ 10²² (w2 C1 prints 9.45·10²¹), so g_0(n_♯) is astronomically small. This is legitimate (all
  constants are g-independent) and worth one sentence.
- **Fix RS-1 (binding): the family.**
  - l.628-632 assumes (PRICE^ℛ) on ALL of ℛ, and l.660-661 claims the order is arbitrary because of that.
  - ℛ contains S = ∅, i.e. the plain chain W/Z_K. For that law, (PRICE^ℛ) is a plain-chain multi-cube Peierls bound, which
    is the large-field problem itself.
  - The proof consumes only laws R_{S_i,𝒟} with S_i ⊇ S(𝔥).
  - Under level-first ascending order, every finer level is fully constrained when level j is relaxed. The fine columns
    priced in (PRICE^ℛ) then carry only small components. This is the regime in which any (M-f)-type input is plausible, and
    it is REVIEW_HW_S1's order.
  - Under arbitrary order, finer relaxed regions under 𝒟's column may carry unconstrained large clusters, and (PRICE^ℛ)
    would then have to price through them.
  - **Restate:** ℛ_𝔥^↑ := {R_{S,E} : S ⊇ S(𝔥), S reached by level-first ascending relaxation, E ∋ the step animal}.
    (PRICE^ℛ) is assumed only on ℛ_𝔥^↑, and l.660-661 is replaced by "the order is level-first ascending; other orders are
    valid as implications from the stronger family hypothesis". w2 B5 tests only the logic (toy), so it does not bear on this.
- **Remark (not a defect, but it bears on Priority 5).**
  - (SDP)_θ on ℛ_𝔥^↑ already implies (PRICE^ℛ) at one level, with a = θa_bad, C_ℓ = C_sd, c = 0: apply it with S = 𝒟.
  - So REL-seq ⇐ (SDP) directly, with no HW^cap. (SDP) is of (PRICE) strength at a single level, which confirms HW's own
    remark (l.821-822) that (SDP) is "not strictly smaller in kind" than (H-w).

### Corollary (l.663-666): CONFIRMED with RS-1
(REL) is no longer an independent residual. S-1 is adopted correctly after re-derivation.

### (NA-∅) (l.668-676): WRONG AS WRITTEN; fix NA-1 (binding)
- HIST-sum with Z^sf := Z(∅) gives Z(∅) ≤ Z_K ≤ Z(∅)e^{C_H|T|e^{-(n_♯+1)a/g_K²}}. CORRECT.
- RLARGE (RLF-1)/(RLF-4) (l.176-177, 186-189) compare Z_K^{ren} := e^{-𝒱_K^{LF}}Z_K with Z_K^{sf}, not Z_K.
- 𝒱_K^{LF} = Σ_kN_{k+1}c̄_0^{sea}(g_k). Per final cell, Σ_kL^{4(K-1-k)}c̄_0(g_k) diverges as K → ∞, which is LF-count and
  HW's own Remark GAS (l.677-683). So |log Z(∅) - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} uniformly in K cannot hold with Z_K^{sf}
  the shifted-coupling small-field partition function. The phrase "with the same normalisation conventions … as RLARGE §1A"
  does not repair the displayed formula.
- **Fix:** (NA-∅) := |log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²}, equivalently a two-sided comparison of Z(∅)
  with Z_K^{ref} = e^{𝒱_K^{LF}}Z_K^{sf,ref}. Remark GAS then reads correctly as the reason the 𝒱^{LF} term must be there.

### Remark GAS (l.677-683): CONFIRMED (arithmetic about the bound, uncounted)
It is the K3-b/P4-div computation with a_r. Correctly scoped ("about the bound").

---

## Priority 3. Lemma CAP, (LI^F), H4-red', (M-f^cap), Theorem HW^cap

### Lemma CAP (l.690-695): CONFIRMED (elementary)
- (i) is a case split.
- (ii) holds because X^cap = π on the event.
- (iii) is TE (i)+(iii) with the coupling u_{k+1} kept (Y^mis = 6κu_{k+1}Φ_{int Q}, Y^f = 24u_{k+1}F^col_Q), then (i). w2 A1/A2
  are consistent with this (re-run).

### Lemma H4-red' (l.703-712): CONFIRMED (SU(2), CONDITIONAL ⇐ (LI^F); counted with HW^cap [HW-7])
I re-did the peel.
- **Top level k_1.** Every spectator reads U_m with m ≤ k_1, because 𝒰_{m+1} = ∅ for m > k_1.
- **Level k < k_1.**
  - Spectators of Q ∈ 𝒰_{k+2} read U_{k+1} on Q's level-(k+1) descendants. Q ∉ Σ(Ω^c_{k+1}), so Q ≠ π(x) for every
    x ∈ 𝒰_{k+1}. Those descendants are not in 𝒰_{k+1}, and the links with both endpoints in them are disjoint from
    int(𝒰_{k+1}). So these spectators are functions of V_rest.
  - Spectators of 𝒰_{k+1} read U_k, which is fixed during the V-integral.
  - Higher spectators sit inside h^F_{k+1}.
- **The step.** (LI^F), LI-a, then KS (c) per link uniformly in M̄_c(U_k) (U_k fixed), then h̲^F ≤ h^F and ∫Πk_c = 1. CORRECT.
- **Fix LI-1 (binding for the hypothesis statement).**
  - (LI^F) (l.697-701) is stated for ANY bounded F_Q ≥ 0. A sup-ratio for all weights is a pointwise Radon-Nikodym bound on
    the conditional law of the far-future data (the later history columns together with R's factors), given V vs V'.
  - That is strictly stronger than (LI), and stronger than needed.
  - State it for the weights consumed: F_Q = e^{θmin{π_Q, Y^f_Q}} ∈ [1, e^{θπ_Q}], or more generally the monotone family
    generated by them.
  - The plausibility argument (same channel as LI-a, columns disjoint by DJ) is the right one and is [inference].

### (M-f^cap) (l.714-717) and Theorem HW^cap (l.719-730): CONFIRMED-WITH-FIX (CONDITIONAL; implication proven; counted [HW-7])
- **Chain.** CAP (ii) with π_Q = a_bad u_j, then CAP (iii) pointwise.
  - The mismatch rate λ_c = 6θu_{k+1}/u_k ≤ 6θ(1 + Rg_k²) ≤ λ_* uses (F_R): u_{k+1} ≤ u_k + R and g_k² ≤ 2g_K².
  - Then H4-red' with F_Q := e^{θmin{π, Y^f}}, which is a function of U_k on Q's column: F^col_Q is an infimum over
    U_{<k}, so it reads only U_k on the column links.
  - Then (M-f^cap). The result is Z(𝔥) ≤ Z(R)·e^{(c_LI + c_f)·shadow}·Π[e^{-θa_bad u_j}(1 - λ_*)^{-3n_int/2}C_fc]. CORRECT.
- **"No e^{aR} in the price"** is correct: the window is at its own coupling u_j.
- **Fix CAP-1 (binding): the θ range.**
  - l.729 ("θ ranges up to ≈ 1/6") and l.854 restate λ_* < 1 as the range. λ_* concerns only the mismatch.
  - The fine factor is e^{θmin{π_Q, 24u_{k+1}F^col_Q}}. On the small-field event G_Q (no level-k defect below Q) the cap
    does not bite: π_Q = a_bad u_{k+1} is huge against the typical u_kF^col = O(dof).
  - So (SF-cap)'s c_sf is the uncapped rate-24θ(1 + Rg²) moment of u_kF^col on defect-free columns. By W-1's own Gaussian
    heuristic ((1 - λ)^{-dof/2}), it is g-uniform only for 24θ(1 + 2Rg_K²) < 1.
  - For 24θ ≥ 1 the capped moment is ≈ e^{θπ_Q}·(probability), and that cancels the price.
  - HW states this itself at l.717: "weaker than (M-f)_{24θ(1+2Rg_K²)}". That is the small-field half.
  - **Restate:** θ ∈ (0, 1/24) in effect, more precisely max{6θ, 24θ}(1 + 2Rg_K²) < 1, unless Y^f is re-defined without the
    overlap constant. One option is the moment of u_{k+1}Σ_Pℰ^<_P directly, but its Gaussian count still carries the
    overlap [inference].
  - The structural gains stand: no Hölder (96 → 24), and no rate degradation in depth. a = θa_bad shrinks by a factor of 4
    against the claim, which is irrelevant next to a_bad ≈ 10⁻¹⁶.
- **Collars:** not covered (l.730). Correctly disclosed.

---

## Priority 4. SAT, CAP-dec, LOOP-div, LOOP-const, §15.2, the wall (SDP)

### Observation SAT (l.736-739): CONFIRMED (⇐ (CLS-min); level 0 by (B)); its reading needs one sentence (fix SAT-1, recommended)
- **The proof.** A bad descendant x has an interior P with ||1 - U_k(P)|| ≥ ε_1. 𝒞(P)'s terms are column terms of Q, all
  ≥ 0, so F^col_Q ≥ ℰ_P(U_k) ≥ a_bad. Then Y^f ≥ 24a_bad u_{k+1}. CORRECT.
- **The reading.**
  - SAT is a property of the upper split X_Q ≤ Y^mis + Y^f evaluated at the actual level-k field. The window X_Q itself is a
    function of V = U_{k+1} alone (l.202).
  - SAT does NOT say that a bad level-k descendant makes Q bad, and it is not true that it does. A single returned finer
    defect changes the coarse plaquette's holonomy only through the contours that cross it. That is dilution, of size
    ~ε_1/L² per level: Proposition INH, CF, and SQ's decay class (D1).
  - So "Q bad because of x below" in LOOP-const's mechanism note (l.785-790) is a property of the bound, not of the
    measure.
- **Fix SAT-1:** add "SAT is a statement about the upper split, not about the coarse event".

### Lemma CAP-dec (l.741-755): CONFIRMED; RECOUNTED as uncounted
- On G_Q, min ≤ Y; on G^c_Q, min ≤ π. The expansion is exact.
- The choice functions x_Q are distinct because the columns are disjoint.
- e^{θπ_Q}e^{-θa_bad u_k} = e^{-θa_bad(u_k - u_{k+1})} ≤ e^{θa_bad R}. Indeed it is ≤ L^{-θa_badβ_-}e^{θa_bad R}, a
  gain, which HW does not use.
- C_fc = c_sf + 81C_sde^{θa_bad R}. CORRECT.
- It is five lines of elementary algebra, of the same kind as HÖ and FV (which REVIEW_HW_S1 recounted). **Uncounted.**
- (SF-cap)'s phrase "uniformly under conditioning on finer defects in other columns" is the right content. Note that
  G_Q excludes only level-k defects, which is enough: F^col_Q depends on U_k only, so deeper defects enter only through
  U_k's law.

### Lemma LOOP-div (l.758-771): CONFIRMED (arithmetic about a scheme, uncounted)
- θ_{K-m} ≥ ρ_0^mθ_K·u_K/u_{K-m}, and u_{K-m} ≤ u_K + β_+m log L + R. The right side grows like ρ_0^m/m. CORRECT for every
  fixed g_K.
- w2 C3 is uninformative (θ_K = 1/(2ρ_0) gives m_* = 1), as HW discloses. The arithmetic is two lines, so no numeric check
  is needed.

### Lemma LOOP-const (l.773-790): CONFIRMED (arithmetic about the bound, uncounted); its READING is corrected in §5
- The recursion C_sd(k) = K_m(c_sf + 81C_sd(k-1)e^{θa_bad(u_k - u_{k-1})}) follows from CAP-dec at k - 1 fed into the
  single-level HW^cap at k.
- With u_{k-1} - u_k ≤ β_+log L + R, it gives C_sd(k) ≥ G·C_sd(k-1), G = 81L^{-θa_badβ_+}e^{-θa_bad R}. CORRECT.
  - Small addition: K_m = (1 - λ_*)^{-324}e^{c_LI'} ≫ 1, so even G < 1 would need K_mG < 1 for a bounded constant. This is
    irrelevant here.
- **Size:** θa_bad(β_+log L + R) ≲ 10⁻¹⁶·O(1) against 4log 3 = 4.39, i.e. short by ≈ 10¹⁶-10¹⁷ via (AE) and ≈ 10²³ via
  (REG-min). Correct to the order. With CAP-1 (θ < 1/24) it is short by a further factor of 4.
- **Its correct reading:** LOOP-const is exactly LF-count (and K3-b, GAS) at n = 1. The level-(k+1) cube's price is
  charged, through the 81 descendants, to returned level-k defects. Those are charged to level k - 1, and so on. That is
  bookkeeping of the returned gas across levels inside one column, and the running beats L⁴ per level only at a per-cube
  exponent ≥ 4/β_+. See §5.

### §15.2 global count (l.792-805): CONFIRMED as arithmetic
It relocates to the same divergence, correctly: one cube per level, no n-enhancement, and S3-5's dilution gives an exponent
that is constant in depth.

### The wall (SDP) (l.807-827): the inequality is right; the status line is wrong. See §5.
- **Sufficiency (l.810-811):** (SDP) + (SF-cap) + (LI^F) + (CLS-min) ⇒ (M-f^cap) ⇒ (PRICE) ⇒ (H-w') with REL-seq. CORRECT,
  with CAP-1's θ range.
- **"What fails" (l.812-814):** correct as arithmetic about the column-induction route.
- **"Owner: this file" (l.808, l.866), "the wall": WRONG.** See §5. Re-own it (fix SDP-1).
- **l.819-820:** "(SDP) is expected to hold with a large margin; the difficulty is depth-uniformity of the constant, not
  the rate". AGREED. It is the key correct sentence of §15.

---

## 5. THE ARCHITECTURE QUESTION: is (SDP) the wrong requirement?

### Verdict
**(SDP) is the right inequality but the wrong requirement for HW.** HW's only attempted proof of it, column induction
inside ∫W·1_𝔥, is precisely the cross-level pricing of small defects that LF-count rules out and that the R-operation
exists to avoid. Re-own (SDP) as a per-level output of node A's R-operated representation (fix SDP-1). Then LOOP-const does
not arise, because nothing is inducted across levels. The unreturned condition (n_♯ + 1)aβ_- > 4 + c_B is not what closes
it.

### 5.1 One correction to the question's premise
RLF does price each returned cluster. It does so once, in-step, at its own level:
- (RLF-2) (RLARGE l.178-182): the returned contribution's activity is ≤ C^{|Y|}e^{-a|Y|/g_k²}·𝔯.
- (W1-ret'^J)_k (c) (l.406): the same three-way price for returned and unreturned configurations.
- HIST §14.1 (b) (HIST l.862-864): the returned large-field terms enter (I_k^E)'s polymers at O(e^{-a_♯/g_k²}) per cube.

What LF-count, K3-b, P4-div and GAS forbid is BOOKKEEPING the SUM of those prices over levels, Σ_kL^{4(K-k)}e^{-au_k},
because aβ ≪ 4. The R-operation replaces that sum by extraction (c̄_0^{sea} into 𝒱^{LF}, δβ_k into the flow) plus remainders
that are irrelevant and are contracted by the small-field step. So "returned defects are renormalised, not priced" should
read: **"each returned cluster is priced in-step at its own level with level-uniform constants; their sum is renormalised,
never bookkept."** (SDP), a per-level single-defect bound with a depth-uniform constant, is exactly the in-step price RLF
itself needs. As an inequality it is consistent with RLF, not opposed to it.

### 5.2 What is wrong: where HW's depth-uniformity was supposed to come from
- In RLF, the level-uniform constant of the level-k returned price comes from the level-uniform representation (I_{k-1}^E)
  at stage k - 1. That consists of:
  - the main term u_{k-1}[𝓔_{k-1} + κΦ] on the cone, with branch (iii) via (CLS-min);
  - polymers per cube ≤ E_0, in which the returned (k-1)-clusters appear only as extracted c-numbers, a coupling shift and
    an irrelevant remainder.

  Node A keeps E_0 level-uniform by contraction, NOT by consulting the previous level's defect probability.
- In HW (LOOP-const), the level-k constant is computed FROM the level-(k-1) constant through the column window.
  - SAT makes every finer returned defect in the column saturate the coarse cap, so the scheme charges the coarse defect to
    "some finer defect below".
  - Unrolled, that is P(coarse defect) ≲ Σ_r81^re^{-θa_bad u_{k-r}} (l.787-788), which is the per-column returned-gas count
    of Remark GAS.
  - This is cross-level bookkeeping of returned clusters, i.e. LF-count at n = 1. **LOOP-const is therefore the proof that
    (SDP) cannot be obtained inside the unrenormalised representation by column induction.** It is not evidence that (SDP)
    is false, and not a new wall.
- Physically, the saturation is an artifact of the upper split. A returned finer cluster's influence on the coarse field
  is, in RLF's language, c_0(Y) (field-independent; it cancels in every ratio) + T_Y·(coarse curvature)² (marginal) + R(Y)𝔯
  (irrelevant). In HW's language it is the dilution ε_1/L² (SAT-1). Neither makes the coarse plaquette bad.
- (SDP) on the relaxed family is also of (PRICE) strength at one level (§2, Remark): it alone gives REL-seq. Owned by HW as
  "the wall", it is near-circular in kind with (H-w) (HW concedes this at l.821-822). That is a second reason it cannot be
  HW's residual.

### 5.3 Should (M-f)'s moment run only over unreturned defects? Not literally; here is the correct restatement
- **Literal restriction is not available.**
  - E_{μ_R}[·] integrates over every configuration the integrand allows. The returned level-k defects in a history cube's
    column are such configurations: they lie in Λ_k, and R allows them.
  - The c-number extraction is field- and history-independent up to B_0 terms (HIST (P3), l.586-588). It therefore cancels
    in Z(𝔥)/Z(∅) and cannot remove them.
  - The coupling shift δβ_k changes the law only marginally.
  - So "(M-f) over unreturned defects only" is not a statement about ∫W·1_𝔥.
- **The correct form keeps CAP-dec's split and moves both of its inputs to node A, level by level:**
  - **(SF-cap)^A_θ** [node A; the small-field half, unchanged in content]: c_sf at rate 24θ(1 + Rg²) < 1 on defect-free
    columns. Source: the main-term localisation F^col_Q ≤ Σ_{x under Q}𝓔_{k,x}, which is HW §6 with HIST's current (a')/§25
    form (H-9), plus node A's local coupling response.
  - **(SDP)^A_θ** [node A; RLF-2's in-step returned price, read as a probability]: for every law of ℛ_𝔥^↑ (RS-1), every level
    k ≥ 0 and every set S of level-k cubes in Λ_k,
      μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{|S|}·exp(c_A·shadow sums),  a_A ≥ θa_bad,  C_A independent of g, K, T, k and the law.
    It is proven at each level k separately from:
    - the stage-(k-1) R-operated representation, (I_{k-1}^E)' in its two-field form (d);
    - (CLS-min) for the in-step window;
    - (W1-ret'^J)_{k-1} (c);
    - (SC)_{k-1};
    - R1^J's gas convergence, which turns an activity bound into a probability;
    - the (LI)-type future tilt.

    **It is never proven from (SDP) at level k - 1.**
  - Then CAP-dec gives (M-f^cap)_θ at every level with C_fc = c_sf + 81C_Ae^{θa_bad R}, the SAME constant at every level.
  - HW^cap + REL-seq give (H-w'), a = θa_bad, θ < 1/24 (CAP-1).
  - If a_A < θa_bad (for example if RLF's a_♯ carries a greedy dilution), lower θ to a_A/a_bad. Nothing else changes.
- **Equivalent single statement for node A's hypothesis list** (to replace "(M-f) large-field-tail half: owned by this
  file"):
  **(M-f^A)_θ:** for every 𝔥 and R ∈ ℛ_𝔥^↑, every k and A ⊂ 𝒰_{k+1}, E_R[Π_{Q∈A}e^{θmin{π_Q,Y^f_Q}}] ≤ C_fc^{|A|}e^{c·shadow},
  with C_fc level-uniform, ⇐ (SF-cap)^A + (SDP)^A as above.

### 5.4 Does LOOP-const then close? And the (n_♯ + 1)aβ > 4 question
- **With (SDP)^A, LOOP-const does not arise.** There is no recursion C_sd(k) ← C_sd(k-1). The constant is level-uniform
  because node A's representation is. The ×81 per level was produced only by the column induction.
- **(n_♯ + 1)aβ_- > 4 + c_B does NOT close LOOP-const.** It closes HIST-sum's count of unreturned components: a component
  of n > n_♯ cubes multiplies the running gain by n.
  - LOOP-const's chain has one cube per level, and it consists ONLY of returned cubes.
  - By DJ and H-nest (iii), a history cube's column lies in the small-field regions of all finer levels, so no unreturned
    component sits in another history cube's column.
  - The weight (Ce^{-a/g²})^{n_♯+1} of an unreturned cluster therefore never multiplies a saturation chain.
  - Restricting HW's pricing to unreturned defects is already what Theorem HW^cap does: only 𝒰-cubes are priced. That was
    never the problem. The problem was where the returned-defect input to the fine moment comes from.
- **The honest residual (this is where the wall now is).**
  - (SDP)^A transfers the difficulty to node A. It does not dissolve it.
  - If node A's in-step price of returned level-k clusters were itself derived by the column-window Chernoff of §14-§15,
    LOOP-const would reappear there verbatim.
  - Node A must use the property its R-operation encodes: returned finer clusters affect the coarse problem only through
    c_0 + T_Y-term + irrelevant remainder, which is a non-saturating split.
  - This is HW's own option (i) at l.816-818 ("a returned finer defect raises the coarse window's fine part by less than
    π_Q"), now with an owner and a mechanism: (W1-ret'^J) (a)-(b) + I-tay^J (the two-field extraction) + (SF-irr).
  - Option (ii) at l.818-820, a direct one-threshold large-deviation bound on the level-k marginal, is the same statement
    read from the density side. RLARGE §4.2 lists (D1-b) as "not consumed; do not attack". Under SDP-1 it is not needed:
    what is consumed is the integrated in-step price, not a pointwise density bound.
- **Net for the wall line.**
  - "(SDP) [OPEN, P, this file: the wall]" (l.808, l.866) becomes "(SDP)^A [OPEN, P; owner node A: RLF-2's in-step returned
    price at each level, level-uniform, via (I^E)' + (W1-ret'^J)(c) + (SC) + I-tay^J + gas convergence; NOT derivable by
    column induction (LOOP-const)]".
  - HW's large-field-tail half of (M-f) is thereby re-owned to node A, and S-2's "unowned" becomes "node A (RLF-2)".
  - HW keeps (LI^F) and (CLS-min) [⇐ (REG-min)] as its own interfaces.

---

## Priority 6. Check w2

### Procedure
- **Order.** The criteria mtime is 00:00:33 EDT = 04:00:33 UTC. The script's is 04:04:36 UTC, and the output and time files
  are 04:04:45 UTC. Criteria came before the script. One run. CONFIRMED.
- **Disclosure gap 1 (fix W2-1).**
  - The criteria file names "Lemma CAP of §14", LOOP-const's G = 81L^{-θaβ_+}e^{-θaR}, LOOP-div's m_*, and the constants
    θ ∈ {1/6, 1/100}, a ∈ {2.3·10⁻¹⁶, 5·10⁻²³}.
  - HW_LOG (l.47-48) dates §13-§15 to 04:01-04:02 UTC, i.e. after the criteria.
  - Either the derivations predated the criteria in draft, or the criteria were written against a plan with numbers already
    computed. Disclose which.
  - It does not affect w2's informational status. C1 and C2 are tautological (C1 is (⌊y⌋ + 1) > y; C2 is
    81(1 - 10⁻¹⁶) > 1) and could not fail.
- **Disclosure gap 2 (fix W2-2).**
  - B2's criterion says "zero exceptions over all configs and steps".
  - The script (w2_relseq_toy.py l.120, `bad[:: max(1, len(bad) // 2000)]`) checks a strided subsample of about 2000
    configurations per step whenever more fail.
  - §16 (l.835-836) reports "B2 step containment PASS" without saying so. State it, or re-run B2 on all configurations.
    B2's content is proven in REL-seq (2) anyway.
- **Coverage.** B tests the logic of REL-seq and DECL on a 4×4 toy defect law, not the chain. C is arithmetic. Nothing bears
  on (SDP), (LI^F), (SF-cap) or CAP-1's θ range. HW's scope line (l.842-843) says this correctly.

### Re-run (MANDATORY NUMERIC LOCK; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; no timeout; python without -I)
- The lock was acquired at 04:19:55 UTC, at load 2.69 with 38% memory free. Exit 0 at 04:19:57. The lock was released once
  by a single rmdir, with no trap. Wall time 1.16 s, peak RSS 147 MB.
- **Output:** identical to checks/w2_out.txt in every line, after excluding the wall-time field (diff empty).
  **OVERALL: PASS**:
  - A1 and A2: 0 violations in 10⁶ samples. A3 fails as required (332415 violations).
  - B1, B2, B3 (28 cases, tightness 0.352-0.495) and DECL pass. B4 fails as required. B5 passes.
  - C1-C4 pass, with C3 uninformative.
  - D: 1, 80, 7320.
- **Verdict:** w2 is CONFIRMED as recorded and is informational. The two disclosure fixes are W2-1 and W2-2.

---

## Corrected tally

| item | HW claim | verdict |
|---|---|---|
| [RHW1-fix] edits §0-§11 | applied | **CONFIRMED** (H-12 residue in §10 W2, recommended) |
| §12A switch (AE) → (CLS-min) | every use is the infimum | **CONFIRMED** (c_pr, t_pr re-derived from DESC (a)+(b); source SQ unreviewed, disclosed) |
| DECL | uncounted elementary | **CONFIRMED** (bad-only scope) |
| [HW-6] REL-seq | CONDITIONAL, counted | **CONFIRMED-WITH-FIX** (RS-1: family ℛ_𝔥^↑, level-first; cosmetic e^{±38416c}), counted |
| (NA-∅) | node A owes only this | **WRONG AS WRITTEN** (NA-1: include 𝒱_K^{LF}); the single-comparison reading is right |
| Remark GAS | uncounted arithmetic | CONFIRMED |
| CAP | uncounted | CONFIRMED |
| [HW-7] H4-red' + HW^cap | CONDITIONAL ⇐ (LI^F), (M-f^cap), (CLS-min); θ up to ≈ 1/6 | **CONFIRMED-WITH-FIX** (CAP-1: max{6θ, 24θ}(1 + 2Rg_K²) < 1; LI-1: (LI^F) for the capped weights), counted |
| [HW-8] CAP-dec | counted | **CONFIRMED, RECOUNTED as uncounted** (elementary) |
| SAT | uncounted | CONFIRMED (SAT-1: a property of the upper split, not of the coarse event) |
| LOOP-div, LOOP-const, §15.2 | arithmetic about bounds | CONFIRMED as arithmetic; LOOP-const re-read as LF-count at n = 1 (§5) |
| (SDP) | OPEN [P], this file, "the wall" | **status WRONG**: re-owned to node A as (SDP)^A (SDP-1); not derivable by column induction |
| (LI^F) | OPEN, this file | OPEN (LI-1) |
| (SF-cap) | OPEN, node A | OPEN, node A; rate 24θ (CAP-1) |
| w2 | PASS | **CONFIRMED** (re-run identical; W2-1, W2-2 disclosure) |

**Counted: 6 in total = session 1's 4 + HW-6 + HW-7** (HW claimed 4 + 3). Targets: S1 MET; S2 MET with RS-1 and NA-1; S3
PARTIAL. The rate result (no depth degradation) stands with CAP-1. The "exact wall" is re-identified: it is node A's
level-uniform in-step returned price (SDP)^A, not an HW-owned single-defect Peierls bound.

## Binding fixes (next lane-H session)
1. **SDP-1** (l.808, 822, 857-859, 866; §6 l.392-394; §5.1 l.289-290). Re-own (SDP) as (SDP)^A (node A: RLF-2's in-step
   returned price per level, level-uniform, via (I^E)' (d) + (CLS-min) + (W1-ret'^J)(c) + (SC) + I-tay^J + R1^J gas
   convergence). State that LOOP-const proves it is NOT derivable by column induction (LF-count at n = 1). Replace (M-f)'s
   "large-field-tail half: this file" with (M-f^A) ⇐ (SF-cap)^A + (SDP)^A (§5.3).
2. **NA-1** (l.673): (NA-∅) := |log Z(∅) - 𝒱_K^{LF} - log Z_K^{sf}| ≤ C|T|e^{-a'/g_K²} (or the comparison with Z_K^{ref}).
3. **RS-1** (l.628-632, 660-661): (PRICE^ℛ) only on ℛ_𝔥^↑ (S ⊇ S(𝔥), level-first ascending). Drop "any order" as a
   feature, or mark it as needing the stronger family.
4. **CAP-1** (l.721, 729, 754, 811, 854): the θ range is max{6θ, 24θ}(1 + 2Rg_K²) < 1. The 24 is TE (iii)'s overlap inside
   Y^f, and (SF-cap) is a rate-24θ moment.
5. **LI-1** (l.697-701): (LI^F) for the capped weights F_Q = e^{θmin{π_Q,Y^f_Q}} only.
6. **Recount** HW-8 CAP-dec as uncounted; tally 6 (l.862-864).
7. **W2-1, W2-2**: disclose the criteria/derivation timing and B2's subsample (l.835-836; HW_LOG).

Recommended:
- H-12: mark §10 W2 inline as superseded.
- SAT-1.
- REL-seq: write e^{-38416c} (or "≤") at l.636 and l.653, and record n_H ≈ 10²² at the recorded a.
- CAP-dec: note the unused gain L^{-θa_badβ_-}.
- LOOP-const: note K_m ≫ 1.

## Strategic verdict
- **What session 2 achieved, and keeps.**
  - (REL) is gone as a residual (REL-seq, with RS-1).
  - Node A owes one torus-wide comparison (with NA-1).
  - The (AE) dependence is replaced by the cone-local (CLS-min).
  - The rate loss across depth is removed (HW^cap), which answers HW-F5 at the level of rates.
  - LOOP-div and LOOP-const are correct and useful negative arithmetic.
- **What it got wrong.** It promoted the last arithmetic to "the wall, owned by this file". LOOP-const is not a new
  obstruction. It is the LF-count obstruction re-derived for single returned defects in one column, i.e. the reason the
  R-operation exists. The correct conclusion is: (H-w') ⇐ (CLS-min) + (LI^F) + (M-f^A), where (M-f^A) is node A's
  level-uniform small-field moment together with its in-step returned price.
- **Next targets, in order:**
  1. Apply SDP-1/NA-1/RS-1/CAP-1.
  2. Write the precise (SDP)^A interface in node A's terms: which clause of (W1-ret'^J)(c)/(SC) gives a probability bound
     under μ_R ∈ ℛ_𝔥^↑, and with which a_A against θa_bad. Hand it to the RLARGE/HIST owners.
  3. Prove (LI^F) for the capped weights at one level (the channel is LI-a's).
  4. A non-saturating split lemma (dilution: a returned finer cluster raises Q's capped fine part by o(π_Q)). This would be
     an HW-internal proof of (SDP) and is worth a session only if node A's route stalls.
