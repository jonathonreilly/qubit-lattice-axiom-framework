# REVIEW_RLARGE_V3: hostile review of RLARGE.md v3 (integration after REVIEW_RLARGE_V2)

Reviewer: an independent agent. I wrote none of RLARGE.md, RLARGE_INTEGRATION_LOG.md or any lane file. This file is the
only file I wrote in the working tree. No commits, PRs or pushes. Date: 2026-10-28, about 09:47-10:05 UTC.

**Inputs (read-only).**
- REVIEW_RLARGE_V2 (all). RLARGE.md v3 l.1-842 in full; Appendix A not re-read (byte-identity is claimed by the log and
  not re-checked here). RLARGE_INTEGRATION_LOG v3 section (l.66-131).
- HW.md: §2-§5.3 (l.76-391), §13-§15.3 (l.607-872), §18-§19 (l.918-1018). REVIEW_HW_S2: bottom line, §5.3-§5.4, tally.
- SQ.md l.190-232 (SUP-price remarks, θ_0) and l.312-336 (Corollary DESC-ε). REVIEW_SQ_S2: bottom line, l.339, 395, 438.
  REVIEW_SQ_S1 tally lines 155, 178, 343-346 (SUP-price, DESC, PRICE-iii).
- PLD.md l.482-492 ((SC)_k, Proposition W1R), l.966-990 (the laws (M3), (M3^+), (SG^{fl})_k), l.1027-1102 (HS-net, PLD-SG,
  INH, PLD-desc). REVIEW_PLD_S3 verdict lines (l.42-43, 222-320, 509).
- SF.md l.2825-2845 (§22.7 ε_1-driven rows). REVIEW_SF_S7 l.195-205 (TB-1). REVIEW_SF_S5 l.335-350 (the ε_1 table).
- FLOW: REVIEW_FLOW_S10 bottom line, §5, §11 (written 09:38 UTC, after v3's 09:37 input freeze). FLOW.md not re-read.
- EXISTENCE.md l.3072-3092 (the consumer of (RLF-3), [RX8-fix 8]). REVIEW_BFT_A_S5 l.36-39.
- File times (local EDT, +4 h = UTC): BFT_A.md and BFT_B.md were modified 09:35-09:40 UTC (after v3's read; no review of
  those edits exists). No REVIEW_HW_S3, REVIEW_SQ_S3, REVIEW_PLD_S4, REVIEW_SF_S8 exists.

**Numerics.** One script, scratchpad `rlv3/arith.py` (mpmath, 40 digits, decimal inputs as quoted). One run under the numeric
lock (one mkdir, one rmdir; nice 10; BLAS threads 1; load 2.1; < 1 s; no process left). Output `rlv3/out.txt`.

"l.N" without a file name means a line of RLARGE.md v3. Status words as in PROOF.md.

---

## Bottom line

- **REVIEW_RLARGE_V2's soundness flaw is fixed.** The fixed-V branch (iii) and the e^{B_0} absorption are deleted
  (l.339-343, 428-430). The defect price is now HW's forward Chernoff under the one law μ_{R(𝔥)}:
  - Lemma CH with W-bad's window, the CAP split, the H4-red′ peel, CAP-dec and REL-seq.
  - Every step quoted is one that REVIEW_HW_S2 CONFIRMED or CONFIRMED-WITH-FIX, and I re-traced the chain.
  - **As an implication, §3 is sound end to end, for bad-only defects and SU(2).**
- **New binding gap (S-1). The node-A inputs are stated under a law that no node-A tool reaches.**
  - (SDP)^A and (SF-cap)^A are moments under μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}}. These laws contain the FUTURE constraint 1_{R,j}, j > k.
  - PLD's bounds are under μ_{𝔥,ω} / μ^+: frozen exterior, before the level-(k+1) indicators are inserted (PLD l.971-975).
    (I_k^E)″ is a representation of the past marginal.
  - The bridge is the future tilt H_k(U_k) := ∫K_k·1_{R,k+1}·h_{k+1}. HW lists it as an input of (SDP)^A ("the (LI)-type
    future tilt", HW l.938).
  - v3 omits it from row 10b. Check (a) (l.539-542) says it enters "only through (LI^F)". **(LI^F) cannot carry it**: (LI^F)
    bounds h's sensitivity to V on int(𝒰_{k+1}) only (HW l.720-730). It says nothing about U_k on an arbitrary defect set S,
    or on a history column.
- **Circularity: none through (SDP)^A's listed inputs; one structural risk (S-2).**
  - The tilt is the conditional probability of the coarser levels' large-field event, so bounding it locally is a
    statement about levels > k.
  - Check (a) forbids exactly that content unless the tilt bound gets its own top-down proof. No source writes one.
- **(RLF-3′) (l.213-220) has the right exponent and the right reference.** Exponent a = min{θa_bad, a_A}; reference Z(∅); the
  NA-1 form; HS′'s shadow form. Three fixes:
  - B_0 must include REL-seq's c (HW l.671);
  - the status should read rows 10-10e plus the new tilt row, not 10f;
  - the D_j convention must be stated, because it decides where K15 lives.
- **§4.2.** Most statuses are quoted correctly where I checked. The problems:
  - row 1 is stale against REVIEW_FLOW_S10 (which postdates the read);
  - row 8 contradicts row 1a;
  - row 12 is off-route;
  - row 2 / K12 hides a possible return of (BG)_k (= BFT-3) through a_ret.
  - **FI-1 option A is valid only with one more statement (FI-1A, a per-level implicit equation).** Options A and B coincide
    once FI-1A is written.
- **Arithmetic: the integrator's n_H ≳ 2·10⁸⁷ / 184 levels is right only in the limit B_0 → 0.**
  - With HW's own B_0 = B_1 + c + 1 ≥ 1, c_B ≥ 34968 and **n_H ≥ 1.81·10⁹¹, W ≈ 3.6·10⁹¹, ≈ 192 wrap levels**.
  - The coupling ceiling is g_K² ≲ 2.7·10⁻⁹¹, not 10⁻⁸⁸. It still does not bind against DX′.
- **K16 is resolved.** The counts 42/60 are log_{L⁴} n (compact-cluster extent n^{1/4}); 46/184 are log_L W (side). RLARGE's
  own W := 2n_♯ + 5 makes log_L W the right count: **≥ 184, ≈ 192**.
- **K13 is CONFIRMED:** the coefficient ratio is 2.4-5.1·10⁹ in (REG-min)'s favour at ε_1 ≲ 6.7·10⁻⁴⁰. **K8 is CORRECT, with two
  additions.** On **K15** I give a closure route (Part 5).
- **Top 3 (Part 6):**
  1. the future-insensitivity statement (LI^U);
  2. one node-A "in-step returned price" theorem, delivering (SDP)^A + (SF-cap)^A + a_ret;
  3. (CLS-min) ⇐ (REG-min) ⇐ (MIN-reg)_cone.

---

## Part 1. Soundness of §3 (priority 1)

### 1.1 The chain, re-traced
1. **Lemma CH** (HW l.242-248; counted; CONFIRMED). The proof is a pointwise inequality, 1_𝔥 ≤ 1_RΠ1{Q ∈ D_j} ≤
   1_RΠe^{θ(X_Q − π_Q)}. It needs only X_Q ≥ π_Q on {Q ∈ D_j}. No law, independence or disjointness enters. CORRECT.
2. **W-bad** (X_Q = u_{k+1}Σ_Pℰ_P(V) ≥ a_bad u_{k+1}, a function of V alone). It rests on TE (ii) = (CLS-min). (CLS-min) is
   satisfied at ε_1 ≪ t_pr by DESC (b), with no lower amplitude threshold (SQ l.312-336). CORRECT, CONDITIONAL ⇐ (CLS-min).
3. **CAP (iii)**, X^cap ≤ Y^mis + min{π, Y^f}, and **CAP (ii)**, CH with X^cap. Elementary. CORRECT.
4. **H4-red′.**
   - It peels the int(𝒰_{k+1}) links top-down with KS (c). The spectators F_Q = e^{θmin{π,Y^f}} read U_k on Q's column only,
     and DJ keeps those columns disjoint from every int(𝒰) set.
   - It consumes (LI^F) for exactly these weights (LI-1). CORRECT (CONFIRMED by REVIEW_HW_S2).
5. **CAP-dec.** Pointwise two-term expansion, then the choice functions x_Q (distinct across Q because the columns are
   disjoint), then (SF-cap) and (SDP) at rate θa_bad. Here e^{θπ_Q}e^{−θa_bad u_k} ≤ e^{θa_bad R}. CORRECT.
6. **REL-seq.**
   - Telescoping in level-first ascending order. DECL. The step price is (PRICE^ℛ), which by HW §18.1's Remark is (SDP)^A on
     ℛ_𝔥^↑ with S = 𝒟.
   - The depth term is beaten by (n_♯ + 1)aβ_- ≥ 38416c/log L. CORRECT, CONDITIONAL.
7. **Assembly.** HW^cap × REL-seq gives (H-w′) with a = θa_bad (θ lowered to a_A/a_bad if a_A < θa_bad: needed so that CAP-dec's
   e^{θπ}e^{−a_Au} stays bounded, CORRECT). Then HS′ and HIST-sum. CORRECT.

So the "single law" design is genuine. CH uses μ_{R(𝔥)} only; the relaxed family ℛ_𝔥^↑ enters only through REL-seq's step
price. FV's lesson (l.351-363) is stated correctly. K5 is resolved for bad cubes as claimed.

### 1.2 Issues

**S-1 (binding): the node-A moments are stated under a law no node-A statement uses; the future tilt is unowned and
mis-routed.**
- *Where.* l.394-404 ((SF-cap)^A, (SDP)^A "for every μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}}"); row 10b (l.494); check (a) (l.539-542); §7 DAG
  (l.684-686).
- *The fact.* Under μ_{R(𝔥)} (and under any R_{S,E}) the U_k-marginal is, up to normalisation,
    ρ_k^{past}(U_k)·H_k(U_k),  H_k(U_k) := ∫K_k(U_{k+1}, U_k)·1_{R,k+1}·h_{k+1}(U_{k+1})dU_{k+1},
  with h_{k+1} as in HW l.365.
  - ρ_k^{past} is what node A represents: (I_k^E)″, and PLD's μ_{𝔥,ω}, "before the level-(k+1) indicators are inserted",
    PLD l.971-975.
  - E_ρ[H_k] is a torus-wide probability (of size exp(−O(|T|e^{−(n+1)a/g²}))), so only a local ratio bound on H_k is usable.
- *What (LI^F) gives.* Only h^F_{k+1}(V) ≤ e^{c_k}h^F_{k+1}(V′) for V, V′ differing on int(𝒰_{k+1}) (HW l.720-730). Neither
  (SDP)^A nor (SF-cap)^A can use it:
  - (SDP)^A needs H_k's sensitivity to U_k on an arbitrary set S of level-k cubes;
  - (SF-cap)^A needs it on the columns of 𝒰_{k+1}, uniformly under conditioning on finer defects in other columns.
- HW itself lists "the (LI)-type future tilt" as a separate input of (SDP)^A (HW l.938; REVIEW_HW_S2 l.347).
- *Answer to the brief's question.* μ_{R(𝔥)} is the law of the HW moments (CH, H4-red′, (M-f^A)). It is **not** the law of the
  PLD/SF fluctuation bounds (HS-net, PLD-SG, PLD-desc are under μ_{𝔥,ω}/μ^+, no future), nor of (I_k^E)″. v3 is honest that
  (SDP)^A and (SF-cap)^A are OPEN node-A items, but it names no bridge, and the bridge it implies ((LI^F)) is the wrong
  statement.
- *Fix.* Add **row 10g, (LI^U) (future insensitivity, uniform).** For every μ in ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}}, every k, every finite set
  S of level-k cubes (incl. the descendants of 𝒰_{k+1}), and U, U′ differing only on the level-k links read by S's windows
  and collars:
    H_k(U) ≤ exp(c_U(|S| + Σ_{m>k}|sh_m(S)|))·H_k(U′).
  - Owner: HW (it subsumes (LI) and (LI^F): the same channel, LI-a).
  - Make it an input of 10a, 10b and 10c. Rewrite check (a) as "the tilt enters (SDP)^A and (SF-cap)^A only through (LI^U)".
- *Whose shadow sums (HW l.939-940 leaves it open).* This is load-bearing, not a detail.
  - In CAP-dec, S = {x_Q} lies under 𝒰_{k+1}, so sh_m(S) ⊂ the shadows of 𝔥's components up to a fixed multiplicity, and the
    allowance is absorbed by HS′.
  - In REL-seq, S = the step animal, |S| = n_♯ + 1, and the depth term is beaten as in HW l.664-667.
  - For any other use (e.g. EXISTENCE's union bound, K8), an S-shadow allowance e^{38416c(K−k)} per isolated cube is NOT
    beaten at a_A ~ 10⁻⁸⁶. State (SDP)^A with S's own shadow sums and these two absorption facts.

**S-2 (binding as a check; not a demonstrated circularity): (LI^U)/(LI) are statements about levels > k.**
- h_{k+1} is the conditional probability, given U_{k+1}, that no unreturned defect occurs at levels ≥ k + 2 outside 𝔥's
  regions. A local ratio bound on it is a decay-of-influence statement for the coarser chain.
- Proven by the obvious route (cluster-expanding the future large-field event), it is of (H-w′)/HIST-sum strength on levels
  > k with a boundary field. That is exactly what check (a) forbids node A to consume at levels ≥ k.
- The induction directions conflict: node A builds level k from level k − 1 (bottom-up), while h is built from h_K ≡ 1
  (top-down).
- Nothing in v3, HW or node A orders the two.
- *Fix.* Add **check (d)**: (LI^U) must be proven without (H-w′), HIST-sum or (RLF-3′) at levels > k. Two candidate routes:
  - top-down from h_K ≡ 1, using only kernel locality, DECL-type declaration and the product structure of K_i;
  - a written two-direction order of constants.
- Until then, record (LI^U) as the single place where coarser-level information enters a level-k statement.

**S-3 (medium; reduces hypothesis strength): the law family can be narrowed.**
- If REL-seq is fed by (SDP)^A directly (HW §18.1 Remark, l.965-967), then (M-i), (LI^F) and (M-f^A) are needed under
  μ_{R(𝔥)} only. Only (SDP)^A (and the tilt part of (LI^U) it uses) is needed on ℛ_𝔥^↑.
- Rows 10a and 10c (l.493, 495) and §3.2's "every moment hypothesis below is stated on ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}}" (l.367-368) ask
  for more than is consumed.

**S-4 (medium): node A's representation must be uniform over the relaxed constraint patterns R_{S,E}.**
- (I_k^E)″ is stated per history 𝔥 (§4.1). The laws of ℛ_𝔥^↑ are constraint patterns, not histories: a partially relaxed
  level j, declared sets E^{(j)}.
- Under level-first ascending order the finer levels are fully constrained (Z(∅)-type), which helps. But the relaxed level
  and the declared sets are not covered by any node-A statement.
- Add to row 10b: "(I_k^E)″ and R1^J's gas convergence for every R_{S,E} ∈ ℛ_𝔥^↑, with the same constants".

**S-5 (low): what is not circular.** I traced every listed input of (SDP)^A: (I_{k−1}^E)″(d″), (CLS-min) (a static
variational statement), (W1-ret′^J)_{k−1}(c) ⇐ (SC)_{k−1} + (SF-irr)_k, R1^J's gas, I-σ, I-tay^J.
- None consumes (H-w′), HIST-sum or (RLF-3′).
- (I_k^E)″ (c) no longer carries unreturned prices (l.455-456).
- (SDP)^A is not derived from (SDP)^A at k − 1 (LOOP-const respected).
- So, apart from S-2, the answer to "any circularity through (SDP)^A?" is **no**.

**S-6 (cosmetic).**
- l.346: FV's (CLS-min) form was confirmed by REVIEW_HW_S2 (the switch, use by use), not by REVIEW_HW_S1, which reviewed
  the (AE) form.
- l.377: "REVIEW_SQ_S2 tally" is right for DESC-ε. PRICE-iii's CONFIRMED-as-CONDITIONAL is REVIEW_SQ_S1 l.178/346 (K20 says so).

---

## Part 2. (RLF-3′), its exponent and reference (priority 2)

- **Exponent: CORRECT.**
  - a = min{θa_bad, a_A} with max{6θ, 24θ}(1 + 2Rg_K²) < 1 (CAP-1).
  - The defect factor carries no e^{aR}: the window is at its own level's coupling (HW l.306-307). C_H uses C_ℓe^{aR} (W-4).
  - Both are as in HW.
- **Reference: CORRECT.** Z(∅) under (ref-a). Proposition PF shows that a Z_K reference carries no information. The passage to
  Z_K^{sf} is (NA-∅) in the NA-1 form with 𝒱_K^{LF}.
  - (RLF-4)'s triangle inequality (l.227-228) is right: log Z^{ren} = log Z_K − 𝒱 and |log Z_K − log Z(∅)| ≤
    C_H|T|e^{−(n_♯+1)a/g²}.
  - Note: (n_♯ + 1)a ≥ (4 + c_B)/β_- ≥ 21.5 (Part 4). So the HIST-sum term is never the binding exponent, and "any a′ < a" can
    be dropped: a′ is limited by (NA-∅) alone.
- **HS′ form and C_ℓ = (1 − λ_*)^{−3n_int/2}C_fc, C_fc = c_sf + 81C_Ae^{θa_bad R}: CORRECT** (HW l.756, 947).
- **Fix R3-1 (binding, l.216).** "B_0 = c_LI + c_f + 164ε_♯" omits REL-seq's requirement that n_H be computed with
  B_0 ≥ c. Here c is (PRICE^ℛ)'s shadow constant, which contains c_A (HW l.646, 671: "B_0 := B_1 + c + 1"). Write
  B_0 := c_LI + c_f + c + 1 (with 164ε_♯ ≤ 1). This changes n_H by four orders (Part 4).
- **Fix R3-2 (l.219).** "CONDITIONAL on the §4.2 rows 10-10f" should read 10-10e plus 10g (S-1). 10f is a scope extension: even
  granting its items, W-cb's (REL) is not discharged (l.446).
- **Fix R3-3 (binding; ties to K15).** (RLF-3′) is "bad-only" (l.220), while §2.3 defines defects as bad or collar-bad, and
  (RLF-4)'s Z(∅) (l.227) is written with "every D_j". State which D_j (RLF-3′) and (RLF-4) use.
  - With D_j bad-only, every large collar-bad region lies inside Z(∅). K15 then moves into (NA-∅), where the small-field
    package (which needs σ ≡ 1 for CL (c)) cannot absorb it.
  - With D_j = bad ∪ collar-bad, (RLF-3′) is unproven for those components (K15).
  - Either way the gap exists. v3 currently leaves its location undetermined.
- **Fix R3-4 (l.198-202).** (RLF-δ)'s γ_0 sentence quotes REVIEW_RLARGE_V2's "g² ≲ 10⁻⁹⁵", computed from a_coh. The exponent
  there is now a_ret (unknown, K12). Mark the number as "illustrative, from a_coh".

---

## Part 3. §4: the hypothesis list, the checks, FI-1 (priority 3)

### 3.1 Status audit of the §4.2 rows
Re-read at source for rows 3, 3a, 4, 9, 9p, 10, 10a-10e, 11, 23 (REVIEW_HW_S2 tally l.424-447; REVIEW_SQ_S2 l.26-55, 339,
395, 438; REVIEW_SQ_S1 l.155-346; REVIEW_BFT_A_S5 l.36-39; REVIEW_SF_S5 l.343). These are **quoted correctly** except as
listed below.

| row | issue | fix |
|---|---|---|
| 1 (l.474) | Stale since 09:38 UTC. REVIEW_FLOW_S10 CONFIRMS FINE-IR, IR-id, UIR-S (scalar (UIR) PROVEN), V-bord, V-Jac, V-tel. §79's expansion is FALSE (S10-1). **(DEF) is "not the right wall"**: it is replaced by (GP) (constant-field ghost pair) or (DEF-F). (VFINE) is now (VFINE-K). The remaining list is REVIEW_FLOW_S10 §11: (L-loc2), (VFINE-K), (VC-V), (GP), plus FI-1 and HIST's CL^J restatement. | Re-quote from REVIEW_FLOW_S10 §11; tag "after v3 input freeze". |
| 1a vs 8 (l.475, 489) | Row 1a: "(SF-bg) is no longer used by UNIV (Lemma TOW, CONFIRMED)". Row 8: (BG)_k load-bearing "as FLOW's (SF-bg) (row 1a)". These contradict each other. | Row 8: drop the FLOW clause, or cite the node-A use explicitly. See also 3.4 (a_ret). |
| 7, 12 (l.488, 500) | Both off the HW route (row 7 says so; row 12 is "relevant for RS-joint", which l.514 lists as not a hypothesis). | Move to the "Not hypotheses of RLF-step v3" list (l.513-517), with the note that they are kept for RS-joint/PLD-desc consumers. |
| 2 (l.476) | "(RLF-δ)_k delivered by (W1-ret′^J)_k (a)'s bound": the exponent a_ret is unstated (K12). | Cross-reference K12/U1. |
| 10a, 10c (l.493, 495) | Law family too wide (S-3). | Narrow to μ_{R(𝔥)}. |
| 10b (l.494) | Owner list lacks the future tilt; the law uniformity over R_{S,E} is not required (S-1, S-4). | Add (LI^U) (new row 10g) and the R_{S,E} uniformity clause. |
| 10f (l.498) | "(M-i) for collar links as stated": correct quote (HW l.317-318). See K15 for a route. | — |
| 11 (l.499) | The quoted "≈ 60 final levels" was computed at ε_1 ≤ 4.3·10⁻⁵⁹ (the old τ_c) with v1's n_* (REVIEW_SF_S5 l.343). It is doubly stale, and it is a compact-shape count. | Replace by Part 4's ≥ 184 (≈ 192). |
| 23 (l.511) | It leads with PROOF's S4-based map. The current status is REVIEW_BFT_A_S5's narrowed one (quoted at the end of the cell). BFT_A/BFT_B edits after 09:35 UTC are unreviewed. | Lead with REVIEW_BFT_A_S5. |

### 3.2 The three non-circularity checks (l.538-544)
- **(a)** Correct as a requirement. Its mechanism sentence is wrong: the tilt cannot enter "only through (LI^F)" (S-1). Replace
  by (LI^U), and add check (d) (S-2).
- **(b)** See 3.3.
- **(c)** S4-5: correctly recorded. It is a decision, not a proof. It blocks steps 3 and 5 jointly, so it is cheap and
  high-leverage. The lead should take it next.

### 3.3 FI-1: is option A valid?
- **What A asserts (l.560-564).** Treat the kernel couplings as parameters satisfying the bracket
  1/g_{k+1}² ≤ 1/g_k² + R, g_{k+1}² ≤ 1/(2R). Then (RLF-δ)_k uses data on [0, k] plus this bracket, and A5 (effective = kernel)
  is a separate fixed point.
- **Where A is valid.** Every HW statement uses only the u_i of W, i.e. kernel parameters ((F_R) on W's own parameters).
  So the large-field side is indifferent to A5. The decoupling is legitimate there.
- **What A omits.** The stage-k effective output u_{k+1}^{eff} depends on the parameter u_{k+1}^{ker} (through CL^J
  (c)-(d), F-mono H1-H4). A5 is then the per-level implicit equation u_{k+1}^{ker} = u_{k+1}^{eff}(u_0, …, u_k; u_{k+1}^{ker}).
  It is solvable forward, level by level, only if:
  - **(FI-1A)** u_{k+1}^{eff} is continuous in u_{k+1}^{ker} and maps the bracket into itself (contractive, or IVT
    on the scalar shift).
  - The dependence is through exponentially small large-field terms, so FI-1A is plausible [inference], but it is not
    written anywhere.
  - Without FI-1A, A5 is a global fixed point on [0, K] whose existence is not shown.
- **A versus B.** B's "check that the bracket at (k, k + 1) is an output of the step at k" (l.565-567) is the invariance half
  of FI-1A. **So A and B are the same proof once FI-1A is stated.** Record one option: "A with FI-1A".
- **Open question for the lead [inference].** Does node A need exact equality kernel = effective, or only comparability
  κu^{ker} ≍ u^{eff}? If only comparability is needed, A5 is a bracket statement, not a fixed point, and FI-1A dissolves.
  (SF^J)'s uses decide this; no source states it.

### 3.4 K12 (a_ret): who must state it
- a_ret is the exponent "a" of (SC2) in PLD's hypothesis (SC)_k (PLD l.485-486). Proposition W1R propagates it into
  |c̄_0| + |δβ_k| ≤ C′g_k^{−6−p}e^{−a/g_k²} (PLD l.490-491). **Owner: PLD.md ((SC)_k), with the R1^J activity bound (HIST) as
  its source.**
- The finding [inference, to be decided by the owner]. A returned level-k cluster is priced at fixed good V (𝒱_{k+1}; FV does
  not apply to good V).
  - By INH/CF a cut-good V carries coherent fine curvature up to ≈ ε/L² at zero kernel cost. So the frozen activity of an
    ε_1-bad level-k cube needs a fixed-V energy gap above the background, of size ≈ (ε_1 − Cε/L²)².
  - That is a background-regularity statement of (BG)_k = BFT-3 type, together with a g-independent normalisation ratio
    (KS-type).
  - **So (BG)_k (row 8) may return to the critical path through a_ret, (SC)_k and (SDP)^A,** although it is off the
    unreturned-price route.
  - The requirement a_A ≥ θa_bad becomes a_ret − (tilt allowance) ≥ θa_bad. It is plausible, since both come from an ε_1²
    threshold, but it is unproven.

---

## Part 4. Arithmetic (priority 4), recomputed

Inputs:
- c_pr = c_♭/C′² = 1/(640·53²) = 5.5625·10⁻⁷;
- β_- = β_0′/2 = 11N²/(24π²) = 0.185756 (N = 2);
- θ < 1/24 (CAP-1), so a < a_max = a_bad/24;
- L = 3, n_int = 216.

| quantity | integrator (l.92-94, 612, 616-617) | recomputed | verdict |
|---|---|---|---|
| a_bad (REG-min), ε_1 = 6.7·10⁻⁴⁰ | ≈ 2.5·10⁻⁸⁵ | 2.497·10⁻⁸⁵ | CORRECT |
| a_bad at 8.95·10⁻⁴⁰ | "consistent with TB-1's 4.2·10⁻⁸⁵" | 4.456·10⁻⁸⁵ | SF/REVIEW_SF_S7 used c_pr ≈ 5.2·10⁻⁷ (8.4·10⁻⁸⁵ at 1.27·10⁻³⁹ ⇒ 5.21·10⁻⁷). A 7% discrepancy, harmless, for the SF owner. |
| a_bad (AE), C_cone 1.1-2.3·10¹⁵ | ≈ 10⁻⁹⁴ | 1.02·10⁻⁹⁴ - 4.9·10⁻⁹⁵ | CORRECT |
| a_max = a_bad/24 | ≲ 1.0·10⁻⁸⁶ | 1.0404·10⁻⁸⁶ | CORRECT |
| n_H, B_0 → 0 | ≳ 2·10⁸⁷ | 2.070·10⁸⁷ | correct only as the c_B = 0 limit |
| **n_H with B_0 ≥ 1** (HW l.671) | (not computed: "c_B ≥ 0 only increases it") | c_B = 38416/ln 3 = 34968; **n_H ≥ 1.810·10⁹¹** | **the dominant term is c_B, not 4** |
| W = 2n_♯ + 5 | ≳ 4·10⁸⁷ | ≥ 4.14·10⁸⁷ (B_0 → 0); **≥ 3.62·10⁹¹** (B_0 ≥ 1) | — |
| wrap levels log_3 W | ≈ 184 | 183.6 (B_0 → 0); **191.9 (B_0 ≥ 1)** | Write "**≥ 184; ≈ 192 with HW's B_0**". Both are lower bounds, since θ < 1/24 strictly and a_A may be smaller. |
| (n_♯ + 1)a | — | ≥ 21.5 (B_0 → 0); ≥ 1.88·10⁵ (B_0 ≥ 1) | the HIST-sum exponent is O(1)/g², not small |
| log C_ℓ (λ_* ≤ ¼) | ≈ 93 | 324·ln(4/3) = 93.21 | CORRECT |
| coupling ceiling from 6400C_ℓe^{aR}e^{38417B_0}e^{−a/g²} ≤ ½ | g_K² ≲ a/10² ≈ 10⁻⁸⁸ | a/g² ≥ 102.7 + 38417B_0 ⇒ **g_K² ≲ 2.70·10⁻⁹¹** (B_0 = 1); 1.01·10⁻⁸⁸ only at B_0 = 0 | the integrator dropped e^{38417B_0}. The conclusion "far above DX′'s 2.5·10⁻¹⁵²/C_Ω" stands. |
| (P5) g_K² < a/(8(3κ_0 + 3)), 3κ_0 + 3 ≈ 457 | — | < 2.85·10⁻⁹⁰ | not binding |
| (TC) sufficient condition | ε_loc ≥ (16N + 3)ε_1/(128N) ≈ 0.137ε_1 | 35/256 = 0.1367 (from η_q ≤ ε_1/(256NA_d), always true) | CORRECT; U3 stands |
| ε_1 < t_pr (REG-min) | "on both routes" | t_pr = C′τ_♭ ≤ θ_0 ≈ 7.6·10⁻⁹ (C_D = 2), so ε_1 < t_pr iff C_D ≲ 7·10¹⁵ | true at the recorded C_D; state the C_D condition |

**Fixes N3-1 … N3-3.**
- §0 l.94 and §5.4 l.612: n_H ≥ (4 + c_B)/(aβ_-) with c_B ≥ 34968, so n_H ≥ 1.8·10⁹¹ and ≈ 192 wrap levels.
- §5.4 l.616-617: g_K² ≲ a/(3.9·10⁴) ≈ 2.7·10⁻⁹¹.
- §7 l.691: "46-184" becomes "≥ 184 (≈ 192)".

---

## Part 5. Conflicts (priority 5)

- **K8: CORRECT, with two additions.**
  - P_K(𝔥 ≠ ∅) = Σ_{𝔥≠∅}Z(𝔥)/Z_K ≤ Σ_{𝔥≠∅}Z(𝔥)/Z(∅) ≤ e^{C_H|T|e^{−(n_♯+1)a/g²}} − 1. So EXISTENCE's provision
    "Z(∅) ≥ e^{−E_∅|T|}Z_K^{sf}" (EXISTENCE l.3080-3082) and its factor e^{E_∅|T|} are **not needed**. This answers the
    normalisation question for that use.
  - Addition 1: EXISTENCE's union bound also uses a per-cube returned-defect probability under the PLAIN law P_K (l.3072-3074).
    The plain law is excluded from ℛ_𝔥^↑ (RS-1). The route is P_K(Q ∈ D_j) ≤ P_K(𝔥 ≠ ∅) + μ_{R(∅)}(Q ∈ D_j), i.e. (SDP)^A at
    𝔥 = ∅ with S = {Q}. This needs S's own shadow allowance (S-1), which is not beaten at a_A ~ 10⁻⁸⁶ uniformly in K − j. It
    is harmless only because EXISTENCE works at fixed |T| and fixed depth. Say so in K8.
  - Addition 2: Z(𝔥) must be read as ∫W·1_𝔥 (unrenormalised). Its identification with HIST §7.4's R-operated weight is
    "not checked" (HW l.86-89). The 𝔥 is bad-only (R3-3).
  - Also: EXISTENCE's level-sum factor e^{(n_♯+1)a_♯R} becomes e^{(n_♯+1)aR} ≥ e^{21.5R} (≥ e^{1.9·10⁵R} at B_0 ≥ 1). It is a
    K-independent constant, still harmless at fixed |T|.
- **K12:** see 3.4. Owner PLD ((SC)_k) with HIST (R1^J). Possible return of (BG)_k/BFT-3 through it.
- **K13: CONFIRMED.**
  - c_pr·2NC_cone = 2.45·10⁹ (C_cone = 1.1·10¹⁵) to 5.12·10⁹ (2.3·10¹⁵). At ε_1 < t_pr the (REG-min) coefficient beats
    (AE)'s by 2.4-5.1·10⁹, which reverses SQ's ε_1 = 0.5 "net loss 6-9 orders".
  - Caveats: (i) it needs C_D ≲ 7·10¹⁵ (so that ε_1 < t_pr); (ii) it changes n_H by 9 orders (≈ 20 wrap levels) but not the
    wall count, which REVIEW_SQ_S2 calls UNDECIDED (l.339); (iii) both sources are OPEN at paper scale.
  - U7 can be decided now for the constants: (REG-min) is primary. The wall choice stays open.
- **K15 (the largest gap): a closure route [inference; for HW's owner].** W-cb fails at three places: (M-i) is not reduced on
  collar links; there is no capping; (REL) is not discharged. All three come from one fact: R(𝔥) relaxes only N_1(𝒰_j) (HW
  l.95), while collar windows read N_1(Q) and C(Q), which are read again by σ_{Q″} of constrained cubes at distance 2.
  - **(i) Relax N_2(𝒰_j) for the joint defect notion.** RX (i)-(iii) survive any larger relaxation, because {𝔥(c) = 𝔥} ⊂ R and
    {𝔥(c) = ∅} ⊂ R are monotone in the relaxed set. REL-seq's count becomes Σ_j(|Ω^c_j| + 625|𝒰_j|) (constant 82 → 626).
    Then LI-a's data-reading holds for C(Q) and N_1(Q), H4-red′ peels the collar links, DECL extends to collar-bad cubes, and
    a capped collar theorem follows with θ < 1/(24·82·(1 + 2Rg²)).
  - **(ii) Collar windows that meet Σ(Ω^c_{j−1}) (the E10 family)** are saturated by the history's own defects (SAT). Price
    them by entropy, not energy: they lie in N_1(Σ(Ω^c)), so the number of possible such configurations is ≤ 2^{|N_1(shadow)|}
    = e^{c·shadow sums}, absorbed by HS′ into B_0 (raising c_B). Components that are mostly boundary-hugging then need the
    remaining (far) cubes to carry > n_♯ priced cubes, or a B_0-absorbed exception. This step must be checked against
    HIST-sum's per-component count; it is the hard part of the route.
  - **(iii)** It needs K14's history-independent collar rule.
  - If (i)-(iii) hold, K15 and most of E10 become corollaries of the bad-only machinery (rows 10f and 13 shrink to (ii)'s count).
- **K16: RESOLVED.** The counts measure different things:
  - 42 (SF §22.7; REVIEW_SF_S7: log_81(1.19·10⁸⁰) = 41.96) and 60 (REVIEW_SF_S5: log_3((5·10¹¹⁸)^{1/4}) = 62.2) are
    log_{L⁴} n, the extent of a COMPACT cluster.
  - 46 (log_3(2·9.45·10²¹ + 5) = 46.7) and 184 are log_L W.
  - A *-connected cluster of ≤ n_♯ cubes can be a line of length n_♯, so "shapes up to translation" fails whenever
    T_{k+1} < W. RLARGE's own definition (W := 2n_♯ + 5, extraction at T_{k+1} ≥ W, l.190-191, 203) therefore fixes the count
    at log_L W: **≥ 184, ≈ 192 with B_0 ≥ 1** (Part 4).
  - The base-81 counts undercount by a factor ≈ 4. (On SF's own n_*, the side count is 168, not 42.) (SF-last) must be stated
    for ≈ 192 K-independent levels, and for every level when K < 192.
- **K19: CORRECT handling.** v3 carries both maps. REVIEW_BFT_A_S5 is the latest verdict, and nothing newer is reviewed (BFT_A/B
  edits at 09:35-09:40 UTC are unreviewed). Fix: row 23 should lead with REVIEW_BFT_A_S5 (3.1). The owner of PROOF's map is
  the lead.

---

## Part 6. The FINAL critical-path list (from v3, corrected), by owner

Target L6-soft ⇐ (RLF-1) + (RLF-3′) + (RLF-4) + node-A bulk + assembly C.

- **HW.md [HW].**
  - **(LI^U)** (new; subsumes (LI), (LI^F); with check (d)).
  - (KS-N) [s].
  - The collar route of K15 (i)-(iii), replacing W-cb's (TC)/(M-i)/(REL) items.
- **Node A, interface items (owner file still unassigned, U10).**
  - **(SDP)^A + (SF-cap)^A as ONE per-level theorem**: the in-step returned price under R_{S,E} ∈ ℛ_𝔥^↑ ∪ {R(𝔥)}, uniform
    over constraint patterns (S-4), with S's own shadow allowance (S-1).
  - (NA-∅) (NA-1).
  - The S4-5 decision.
- **PLD.md [A].** (SC)_k with **a_ret stated** (K12); (SF-irr)_{k+1}; I-tay^J (with HIST); decide whether (BG)_k enters a_ret (3.4).
- **HIST.md [A].**
  - (I_k^E)″: (a5-U), (a3-q), (a4), S4-1/S4-2;
  - the CL^J restatement (H1-H5);
  - (H-Mayer^J); I-σ^J with σ^J_Q (K2); R1^J gas convergence for R_{S,E};
  - the stale A5 line l.1683.
- **SQ.md [A].** (REG-min) ⇐ (MIN-reg)_cone. Parallel route: (MS-Sob)/(SQ-dev) with HIST.
- **SF.md / PROOF.md [A].**
  - A1.k/A1.loc, A3 composition, (GF-dec)_k, (GF-B^𝔥), (DX-loc-3/4), (CH-c)'s inputs;
  - (C_♭-eval), C_Δ;
  - (R♯), (a5-G♯), (CL-4), (MIN_1), small tori, FP_U's background dependence;
  - (SF-last) for ≈ 192 wrap levels;
  - KW-1/N-1 (PROOF).
- **BFT_A/BFT_B [BFT].**
  - (H-inv+) [(CO-0)/(G♯_0-lev0), (CO-up), (SB)], (Res-Hölder), LRL (b), (FP♯′), (N1) → BFT-0/1/2;
  - weighted (H-inv+)_m → BFT-3 (k ≥ 2);
  - (W-comm) GAP 1, (CovLift), (Mult-Y), (Pair-loc) → BFT-4 (k ≥ 2);
  - SQ's θ_w > 1 and cone-box clause;
  - BFT-5 (unowned).
- **FLOW.md [FLOW].** (L-loc2), (VFINE-K), (VC-V), **(GP)** (replacing (DEF), REVIEW_FLOW_S10); FI-1A (3.3).
- **RLARGE.md [R].**
  - Fixes S-1…S-4, R3-1…R3-4, N3-1…N3-3, the row updates of 3.1;
  - I-σ; E10 residue (K15 (ii)); (TC) vs ε_loc (U3); K14; U2/U4 records;
  - check (d).
- **Other.** Assembly C [P].

**The three items whose resolution most reduces the remaining work.**
1. **(LI^U): future insensitivity, uniform over the relaxed laws.**
   - One statement feeds H4-red′ (the mismatch moment), (SDP)^A, (SF-cap)^A and, via K15 (i), the collar extension.
   - It is the only point where coarser-level information enters a level-k statement, so proving it top-down also discharges
     check (d), the only open circularity question.
   - Today it is split across (LI), (LI^F) and an unnamed tilt, and partly unowned.
2. **One node-A "in-step returned price" theorem.** It yields (SDP)^A + (SF-cap)^A + a_ret from (W1-ret′^J)(a)-(c) + (SC)_k +
   I-tay^J + R1^J's gas, uniform over R_{S,E}.
   - It collapses rows 2, 5, 5a, 10b, 10c, 15, 17, 18 and K12/U1/U10 into one deliverable with one owner.
   - It decides whether (BG)_k/BFT-3 is on the path.
3. **(CLS-min) ⇐ (REG-min) ⇐ (MIN-reg)_cone.** This is the single static wall behind W-bad, W-cb, FV, SAT, (SDP)^A's
   window and the value of a_bad, hence of a, n_H and the wrap count. K13 makes this route the primary one for the
   constants. REVIEW_SQ_S2: "The wall did not move closer."

Runners-up:
- (H-inv+), shared by BFT-0/1/2/3/4, which gates the K-independence of every threshold;
- the S4-5 decision (cheap; unblocks steps 3 and 5).

---

## Required fixes for the RLARGE owner (v3 → v3.1)
1. **S-1/S-2.**
   - Add row 10g (LI^U) and check (d).
   - Rewrite check (a)'s mechanism sentence (l.540-542) and row 10b's inputs.
   - State (SDP)^A with S's own shadow sums and the two absorption facts.
2. **S-3/S-4.** Narrow rows 10a and 10c to μ_{R(𝔥)}. Add the R_{S,E}-uniformity clause to 10b.
3. **R3-1 … R3-4.**
   - B_0 includes c;
   - status rows 10-10e + 10g;
   - state the D_j convention of (RLF-3′)/(RLF-4);
   - (RLF-δ)'s γ_0 number marked as illustrative.
4. **N3-1 … N3-3.** n_H ≥ 1.8·10⁹¹, ≈ 192 wrap levels, g_K² ≲ 2.7·10⁻⁹¹. Fix the §7 DAG label.
5. **Rows 1, 7, 8, 11, 12, 23** per 3.1.
6. **FI-1.** Replace options A/B by "A with FI-1A" (3.3). Add the equality-versus-comparability question to U4.
7. **K8** additions; K12 owner = PLD ((SC)_k) and the (BG)_k question; K13 → U7 decided for the constants; K15 route recorded;
   K16 resolved (log_L W).
