# REVIEW_PLD_S5: hostile review of lane E session 5 (PLD.md §17.0-§17.9: Lemmas GEO / FT^far / COL-DEC, DIL-L, MD, Theorem NA-PRICE^E (i), the wall (J-NS^cd), check p5)

Reviewer: an independent agent. I wrote none of PLD.md, ran no git command, and edited no file except this one. No commits,
PRs or pushes.

Inputs. PLD.md at md5 **35b33c8fb3702f9de47d0afbdb7edf9a**, 211079 bytes, 1966 lines — the state PLD_LOG l.93 records as the
end of session 5. Line numbers below are that file's. Session 6 had not been appended when I read; I reviewed l.1664-1966
only.
- PLD.md §17 in full (l.1664-1966), §16 in full (l.1291-1663) for the fixes, §9 and §0 for conventions.
- PLD_LOG.md session-5 block (l.72-93) and the session-3 [RPLD-fix B3] provenance note (l.29-45).
- REVIEW_PLD_S4.md in full (the eight binding fixes and the seven recommended ones).
- HW.md §13.1 (l.607-632), §15 CAP-dec (l.769-800), §22 Cor. LI-0 (l.1127-1144), §23 Prop. LI-pw (l.1146-1188),
  §24.1-§24.3 (l.1191-1330), §26 H1-H9 (l.1357-1381), §30.1-§30.7 (l.1473-1663), §31 (l.1665-1671).
- REVIEW_HW_S2.md §5 (l.280-385), in particular §5.3 l.326-357 and §5.4 l.358-385.
- checks/p5_criteria.md (md5 755218e72a7623a87573b6dceb3c70e2 — the quoted `755218e7…` is CORRECT), checks/p5_pld.py,
  checks/p5_out.txt, checks/p5_time.txt.
- I re-derived the p5 part-B geometry and the §17.3/§17.4/§17.6 constants from scratch in my own code (Part 7). My scratch
  files are in
  `/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-yang-mills-proof-df9972/a931aaa3-5369-4512-9e8d-b8590010706c/scratchpad/rev5/`
  (`indep_s4.py`, `indep_dil.py`, `indep_rinf.py`). Exact rational arithmetic in plain python; no BLAS, no scipy, no numeric
  lock taken.

---

## Bottom line

1. **"c_f = 0" is true, and it is not a trick — but the cost did move, and the file does not say where.**
   - Lemmas GEO, FT^far and COL-DEC are correct. I could not break them. The conversion really is exact: no (LI^U), no
     shadow allowance, no tilt factor. The geometric separation that makes it exact (X_k(S) ∩ L^far_k(𝔥) = ∅, and
     S ∩ 𝒰_k = ∅) is genuinely supplied by HW in the form used — Theorem LI^U-0 / Cor. LI-0 (b) and DJ + H-nest (iii).
   - The cost went into the **quantifier**. §17.4 l.1855 states the theorem "for **every law ν_G with L_G ∩ X_k(S) = ∅** (in
     particular HW's (E1) law ν^{(k),w}_k, **any w**)", and §17.6 l.1905 delivers it "for every far weight w (HW's (E1)
     form)". That is exactly HW's **(E1)**, which HW.md l.1286-1292 **[RHW4-fix E1-1]** now declares **EXPECTED FALSE in sup
     form**, with "**The route of record is (E2)**". So the conjunction (CLS-min) + (SF-cap)^𝔉 + (J-NS^cd), as quantified, is
     expected to be unsatisfiable, and the delivered interface is expected to be vacuous. (Finding S5-8.)
   - The tilt is not absent; it has become the weight w. HW says so itself in Cor. LI-0 (b) as amended: the tilt "still
     reweights the column through the column's correlation with the far field under the past law" (HW l.1134-1137). §17.6
     l.1906's "the tilt contributes nothing" is the one sentence of §17 I would call misleading.
2. **The implication NA-PRICE^E (i) is valid logic.** The four-branch partition is exhaustive, the constants assemble, and
   there is no hidden level dependence beyond what the hypotheses carry. Two repairs are needed: it must be stated in the
   F-conditioned form its own Proposition CD (b) consumes, and k = 0, 1 are not covered while HW's TEL-f needs every level.
3. **Lemma MD is the real gain of this session.** The mismatch half of the old wall is now genuinely proven, at the kernel
   rate, with no recursion and no 81^k. I checked the quantifiers, the thresholds and the two-level coupling shift; it holds.
   The "good" threshold does not move between levels — 𝒞_j is defined with level-independent constants (½, ε_1/2) and 𝒞° is a
   separate, never-conflated set.
4. **The allowance is in the wrong currency, and it is a regression.** §17.4 l.1856 and l.1848 state the allowance as
   e^{c·s_k(𝔥)}, the **per-level slice**. HW.md l.1261-1266 **[RHW4-fix SL-1]** struck the slice as mis-indexed and replaced it
   by the union form ‖S‖_sh; HW l.1373 repeats this in H6-H7. PLD's own §16.5 l.1415 used ‖S‖_sh. Session 5 moved away from
   the form HW consumes. This is not cosmetic: in the slice currency, Cor. LAW (c)'s "no allowance compounds" and Proposition
   CD (b)'s recursion do not type-check (the level-(k-1) bound carries s_{k-1}(𝔥), the level-k target wants s_k(𝔥)). In the
   union currency they do. (Findings S5-9, S5-10.)
5. **p5 is clean and I reproduced it.** F_c = **301/729** exactly (printed 0.41289437585733885 — exact agreement), B1-B4 exact
   and correct, R_2 = 0.151173 / 0.281095 reproduced to six digits by my own conjugate-gradient solve with no BLAS, κ_eg =
   154112/767910375 = 2.006901·10⁻⁴ exactly. The pre-registered B6 rule and the NP-F5 verdict survive an independent check:
   my own explicit feasible point already gives R_∞(U4) ≥ 3.33, far above the pre-registered 0.746 and above §17.0's 1/2.
   One misstatement: §17.3 l.1807's "max_e|W_e| = 2/81" is true only over links **interior to a corner block**; over supp W
   the maximum is **1/27**. Not load-bearing.
6. **(E2^𝔉) is NOT supplied.** Not in whole, and not in the half that matters. Three independent reasons, each sufficient
   (Part 8). What §17 does supply is the Γ-side shape on history columns with c_f = 0, i.e. the easy half, and only
   conditionally on (LCR). The far-defect factor of (E2^𝔉) is outside PLD's standing condition (C_S), and the geometry that
   makes c_f = 0 (GEO (ii), COL-DEC) **fails** there.
7. **No status inflation.** §17.8's labels are honest: (NP-F4) MET, (NP-F5) MET at linear order, "Not success, not the partial
   bar". The file says plainly that (J-NS^cd) is two-level and probabilistic, that (LCR) is uncertified, that level 1 is
   uncovered and that CD (c) is ARGUED. I found nothing claimed PROVEN that rests on c_lcr.

---

# PART 1: provenance and process (priority 5, but it gates everything)

## S5-1. §17.0 was the first edit of the session. **CONFIRMED.**
PLD_LOG l.75-79 records: PLD.md 171531 bytes / md5 def1982d… before the append (and `def1982d61cccacf3fb1d3df7e86d446` is
exactly the file REVIEW_PLD_S4 l.5 says it reviewed), 177156 bytes / md5 42151dd1… at 11:22:35 UTC after §17.0, then the
[RPLD4-fix] edits at 11:23-11:24:49 (md5 a332517d…), then p5_criteria.md at 11:30:24, the script at 11:32:11, the run at
11:32:22-27, the derivations from 11:37:53 (l.89), final md5 35b33c8f… (l.91). The end of that chain is independently verifiable and
matches: PLD.md is now 211079 bytes with md5 **35b33c8fb3702f9de47d0afbdb7edf9a**, and p5_criteria.md has md5 **755218e7**….
- The brief's rule 1 (PRE-STATED first) and rule 2 (criteria before script) are both satisfied by this ordering.
- **The task brief put to me the premise that §17.0 claims to have been written after p5 ran. It does not.** §17.0's header
  (l.1672-1673) says "before any session-5 derivation, before any [RPLD4-fix] edit and before checks/p5_criteria.md". The
  "after the check p5 ran" clause is on the **derivations** header at l.1721, which is a different section and is correct.
  There is no ordering violation here.
- §17.0 cites no p5 output. I checked every number in l.1672-1719: the only constants are 1/2 (the pre-stated NP-F5
  threshold) and the slice definition quoted from HW. Clean.
- Caveat I cannot remove: every file in this worktree has mtime 08:03:19 (the checkout), so the intra-session timestamps rest
  on PLD_LOG and p5_time.txt alone. They are mutually consistent and the md5 chain anchors both endpoints.

## S5-2. checks/p5_criteria.md contains two constants derived in the same session. **CONFIRMED-WITH-FIX (immaterial).**
Criterion A1 is "5/256 = (5/8)·(1/16)/2 (the threshold constant of the centre-moving criterion)". Both 5/8 (the reduced centre
set 𝒞°) and 5/256 are produced by Lemma DIL-L (iii) (l.1799-1806), i.e. in this session. The brief's rule 2 says criteria "may
contain no constant derived in the same session".
- The file discloses the cause honestly at its head ("the session-5 derivations exist only as an unwritten sketch when this
  file is written") and names all four sketched results.
- It is immaterial: A1 is a tautology (I verified it; it cannot fail), and A2/A3 are "reported", not PASS/FAIL. No verdict
  depends on it. c_pr = 1/1797760 is a session-4 constant, legitimately quoted.
- **Fix P5-1 (minor):** record the breach in §17.7 in one clause, as session 3 did for session 2 ([RPLD-fix B3], PLD_LOG
  l.29-45).

## S5-3. The B6 decision band is NOT the pre-stated NP-F5 threshold. **CONFIRMED (conservative; not a defect).**
§17.0 l.1704-1706 defines (NP-F5) as "the dilution constant … is not < 1/2". p5_criteria.md's B6 instead declares NP-F5 MET
only at R_∞(U4) ≥ 1 − 1/√24 − 0.05 ≈ 0.746, relabelling [1/2, 0.746) as "refined split only". The criteria file is written
after §17.0, so it may fix the rule; and the change makes NP-F5 **harder** to meet. The observed 6.716 clears both. No issue.

## S5-4. The [RPLD4-fix] edits. **CONFIRMED (all fifteen applied; none strengthens a session-4 claim).**
I grepped §16 for the tags and read each site. All eight binding fixes are present and correctly implemented:
ARCH-1 (l.1599), NA-3 (l.1441), CW-1 (l.1396), C-1/NA-2 (l.1417, with §16.7 at l.1490 and §16.11 at l.1618), W-1 (l.1451),
K-1 (five sites: l.1558, l.1630, l.1633, l.1642, l.1648), CC-2 (l.1532, l.1622), FT-1 (l.1625, l.1651, l.1655).
All seven recommended ones too: W-2 (l.1472), FV-1 (l.1369), NA-1 (l.1437), A-1 (l.1542), CC-1 (l.1537), C-2 (l.1658),
P-1 (l.1586).
- I checked the two that could be fudged. **CW-1**: the false sentence is struck in place and replaced verbatim with the
  review's replacement, plus a forward pointer to the p5 B computation — correct, and the pointer is honest (it says
  "computed … not assumed"). **C-1**: §16.7 l.1490 now reads c_sf = e^{2c_U(81+Δ_sh)}c_lcr, c_f = 2c_U, and §16.5 l.1417
  discloses c_A = 6c_U + c_ns ≠ the pre-stated 2c_U with the n_H factor ≥ 3. Exactly what was asked.
- §17.1 l.1732's "Every edit weakens or corrects a session-4 claim; none strengthens one" is accurate as far as I can check.

---

# PART 2: the law conversion — Lemmas GEO, FT^far, COL-DEC (priority 1; counted item [E5] (1))

## S5-5. Lemma GEO (l.1745-1755). **CONFIRMED.** I re-derived all four clauses.
- **(i)** A level-k link c reads U_{k-1} only on links whose endpoints lie in c's two endpoint blocks (HIST l.964 reading
  rule); a link of L^∂_{k-1}(S) has an endpoint in a block under some Q ∈ S, so that block is an endpoint block of c, i.e.
  c ∈ X_k(S). Correct, and note it needs X_k (crossing links), not ℓ(S).
- **(ii)** Both endpoint cubes of a link of X_k(S) project into N_1(𝒰_{k+1}) ⊂ A_{k+1}(𝔥) (the ⌊u/L⌋ argument is right at
  L ≥ 3), while a far link needs an endpoint cube projecting into S^{(k+1)}(𝔥) = complement of A_{k+1}(𝔥). This is exactly
  compatible with HW's own definition of L^far_k(𝔥) (HW l.1136-1137). Correct.
- **(iii)** DECL's second claim (HW l.624-627) gives it, and the "sites are partitioned among cubes, crossing links are
  interior to no cube" step is right.
- **(iv)** Needs S ∩ 𝒰_k = ∅, the first half of (C_S), and uses it correctly: Φ_{k-1} reads only links with both endpoints in
  the level-(k-1) column of some Q″ ∈ 𝒰_k, and columns of distinct level-k cubes are disjoint. **This is the clause that
  makes (C_S) load-bearing**, and the file says so.
- **(C_S) is genuinely supplied.** l.1741-1743 cites DJ + H-nest (iii) via REVIEW_HW_S2 §5.4; I read it (REVIEW_HW_S2 l.364:
  "a history cube's column lies in the small-field regions of all finer levels, so no unreturned component sits in another
  history cube's column"). That gives 𝒰_k ∩ col(𝒰_{k+1}) = ∅ and the same one level down. The citation is accurate.

## S5-6. Lemma FT^far (l.1757-1764). **CONFIRMED; its hypothesis is stronger than its proof needs.**
- Step 1 is DECL with F riding along, plus (m1). I checked the direction: Z_{ν′} ≤ Z_ν gives E_ν[1F] ≤ E_{ν′}[1F]. The
  "indicators agree on {S ⊂ D_k}" step is HW's R_{S,E} definition (D_j ∪ E^{(j)}, HW l.613), so it is an equality, not an
  inequality. Correct.
- Step 2: under ν′ the factors reading U_k on ℓ(S) are exactly Π_{c∈ℓ(S)}k_c. I enumerated them: K_{k-1} (yes), 1_{R′,j}
  j ≤ k (no, by GEO (iii)), Φ_{k′} k′ < k (no, they read levels < k), G (no, by hypothesis). ν^{(k)}_k contains no K_k and no
  Φ_k, so nothing coarser exists to read them. The conclusion "**No (LI^U), no shadow allowance: c_T = 0**" is right.
- **The hypothesis L_G ∩ X_k(S) = ∅ is stronger than the proof uses: only L_G ∩ ℓ(S) = ∅ is consumed.** This matters in
  Part 8 — the weaker hypothesis would reach far cubes, the stronger one is what COL-DEC needs. Worth stating, because the
  gap between the two is precisely where (E2^𝔉) lives.

## S5-7. Lemma COL-DEC (l.1766-1772). **CONFIRMED.**
H′ = ∫Πk_c·1_{R′,k}G dU_k; the X_k(S) links integrate to 1 because neither 1_{R′,k} (GEO (iii)) nor G reads them, and the
surviving k_c, c ∉ X_k(S), do not read L^∂(S) (GEO (i)). Φ_{k-1} is excluded by GEO (iv). The remaining U_{k-1}-readers are
K_{k-2} (a product over links) and 1_{R,k-1}. Correct, and the k ≥ 2 proviso is stated.
- **This is the clause that needs the full X_k(S), not ℓ(S)**, because GEO (i) routes the level-(k-1) reading through the
  crossing links.

## S5-8. **Where the cost went. NARROWED (binding).**
The headline "on HW's route the law conversion costs NOTHING (c_f = 0)" is literally true and I could not break it. But the
session presents this as a reduction of difficulty, and it is not: it is a change of where the difficulty is booked.
- Session 4 priced the coarse event under the **full** law μ ∈ ℛ^A_𝔥 and paid (LI^U) to strip the future. Session 5 starts
  from the **past** law ν^{(k)}_k times a weight w — i.e. the future has already been stripped, by HW's Theorem LI^U-0, and
  what remains of it is w. Nothing is free; the tilt has become a quantifier.
- The theorem is then asserted **for every** such w (l.1855, l.1905). By GEO (ii) every (E1) weight qualifies, so the
  conclusion **contains** HW's (E1) at level k for S under 𝒰_{k+1}.
- HW.md l.1286-1292 **[RHW4-fix E1-1]**: "(E1) is EXPECTED FALSE in sup form … at small g the conditional law concentrates
  near the minimiser of a g-independent variational problem, whose interpolation into the column has curvature
  c_0·dist^{-p} ≫ ε_1 at fixed distance … So no g-uniform (SDP)^{A,far} holds in sup form. **The route of record is (E2).**"
- Therefore, by modus tollens on PLD's own implication, at least one of (SF-cap)^𝔉_{k-1} and (J-NS^cd)_k is false as
  quantified. I traced which: in E1-1's mechanism the far conditioning drives the column's own curvature above ε_1, so
  Q ∈ 𝒞_k with probability → 1; if the column carries no finer defect the violated hypothesis is **(SF-cap)^𝔉 with a uniform
  c_sf** (CW forces Y^f_Q ≥ 6a_bad u_k, so E[e^{θY^f}1_{G_Q}] blows up); if it does, the violated hypothesis is
  **(J-NS^cd)**. The kernel branches (T via KD, S_md via MD) are unconditional and survive — they are not where it breaks.
- **This is not a defect of the three lemmas.** It is a defect of the interface claim: §17.6 l.1905 and §17.9 l.1958 deliver
  the (E1) form, and HW's session 5 (11:24-11:29 UTC) had already abandoned it. PLD's read window was 10:56-11:22 UTC
  (PLD_LOG l.73), so PLD could not have seen E1-1. **But it could have seen the pre-session-5 text**: HW l.1282-1285's
  unbracketed "[inference, not used] (E1) in its sup form is doubtful at the recorded thresholds" was already there, and
  PLD's own read list (l.1668) names "(E1)/(E2)". The session chose the doubtful branch and said nothing about the doubt.
- **Binding fix B1:** restate Theorem NA-PRICE^E (i), (SF-cap)^𝔉 and (J-NS^cd) for **buffered** far weights only (w = 0 unless
  Buf^R_ρ(col S) ∩ D_k = ∅, HW l.1293-1297, l.1521-1523), not for all w. The buffer indicator is a function of U_k on int y
  for y at level-(k+1) index distance ≥ 2 from A, hence disjoint from X_k(S): **FT^far and COL-DEC survive the restriction
  unchanged.** This costs the session nothing and turns an expected-vacuous interface into the one HW actually consumes.

## S5-9. Corollary LAW (c) "no allowance compounds" (l.1781-1785). **CONFIRMED-WITH-FIX.**
The claim is right about the thing it names — there is no c_U on this route, so Proposition WALL (b)'s specific
c(k) ≥ c(k-1) + 4c_U does not arise. But §17.8 (a) l.1937-1938 upgrades it to "recursions compound nothing … Proposition
WALL (b)'s obstruction is gone", and that is only true after two repairs:
- (a) **Currency.** In the slice form actually used (e^{c·s_k(𝔥)}, l.1848, l.1856) the recursion does not type-check: CD (b)
  feeds the level-(k-1) theorem, which carries e^{c·s_{k-1}(𝔥)}, into a level-k target that wants e^{c·s_k(𝔥)}, and there is
  no inequality between the two slices. Unwound, it gives e^{c·Σ_{j≤k}s_j(𝔥)} ≤ e^{c·s(𝔥)} per level, hence e^{Kc·s(𝔥)} after
  TEL-f — exactly the compounding HW's SL-1 note (HW l.1261-1263) warns against. In the union form ‖S‖_sh the recursion does
  close with c(k) = c(k-1), because the level-k step adds no allowance of its own.
- (b) **The union-form excess is asserted, not proven here.** §16.6 (b) l.1460 computed the per-cube excess
  sh(x_Q) − sh(Q) ≤ 3.07·10⁶ and explicitly said that per-cube sums are what REL-seq cannot afford. The union-form statement
  that is needed — ‖x(S)‖_sh ≤ ‖S‖_sh + c·|S| with c depth-free — is plausible (the deep shadows of x(S) and S coincide) but
  is nowhere written in §17. It should be, in one displayed line, since the whole of CD (b) rests on it.
- **Binding fix B2:** restate every allowance in §17.4 and §17.6 in the union form ‖S‖_sh (HW [RHW4-fix SL-1], HW l.1265-1266
  and l.1373), as PLD's own §16.5 l.1415 already did, and add the one-line union-form excess bound.

## S5-10. The interface currency is a regression against HW and against PLD §16. **WRONG as an interface claim.**
§17.0 l.1686 pre-states the cost "in the per-level slice s_k(𝔥) … (HW §24.3)"; §17.4 l.1848/l.1856 and §17.6 l.1905-1906
deliver it. HW §24.3 **struck** the slice before session 5 ended (HW l.1261-1266) with the reason "the slice is mis-indexed
(the level-k factor concerns 𝒰_{k+1}'s columns; for 𝔥 with components only at level k + 1, s_k(𝔥) = 0) and PLD §16.5
NA-PRICE does not deliver it". The timing excuses the author (PLD read HW at 10:56-11:22, SL-1 landed 11:24-11:29) but the
lead must reconcile it: **as written, PLD S5 does not deliver H7's allowance.** Note the perverse case SL-1 names: when
s_k(𝔥) = 0 PLD's statement claims the bound with **no allowance at all**, which makes (J-NS^cd) correspondingly stronger than
necessary. Subsumed in binding fix B2.

---

# PART 3: Lemma DIL-L and the lasso computation (priority 2; half of counted item [E5] (2))

## S5-11. DIL-L (i)-(iii) (l.1793-1806). **CONFIRMED.** I re-derived every step.
- **(i)** ‖T^σ_y(U) − T^σ_y(U°)‖ ≤ Σ_e (traversals)·‖U_e − U°_e‖ by telescoping a product of unitaries; averaging gives the
  f_c-weighted sum; Cauchy-Schwarz gives (F_c·Σδ²)^{1/2}. Note f_c has been **redefined** from §16.6 (c) (a fraction of
  contours) to a traversal-weighted mean. The redefinition is stated (l.1791) and is the correct one.
- **(ii)** The SU(2) identity: VŴ^{-1} = e^{iαn·σ} gives ‖V − Ŵ‖_op = 2|sin(α/2)|, so ‖V − Ŵ‖²/2 = 1 − cos α and
  φ = r(1 − cos α) = r‖V − Ŵ‖²/2, hence δ_e² = 2φ_e/r_e. Correct, and p5 C2 confirms it at 1.8·10⁻¹⁵. The chain-gauge
  covariance claim is correct: U_{k-1} and the kernel centres M̄_e(U_{k-2}) transform by the same h(x_e)h(y_e)^{-1} only for
  transformations induced from level k−2, and a level-(k-1)-only transformation is indeed not a symmetry of the chain
  (it changes the kernel factors). The bound ‖ΔM̄_c‖² ≤ (2F_c/r_*)Σ_{e∈E}φ_e follows.
- **(iii)** Case 1: r_c(U) < ½ and r_c(U°) ≥ 5/8 give |Δr| > 1/8 ≥ 5ε_1/256 (and 5·6.4/256 = 1/8 exactly, so the
  "ε_1 ≤ 6.4" proviso is sharp). Case 2: telescoping four unitaries gives Σ_{∂P}‖ΔŴ_c‖ > ε_1/2 − ε_1/4 = ε_1/4, so some
  c has ‖ΔŴ_c‖ > ε_1/16, and the polar bound with r° ≥ 5/8 gives ‖ΔM̄_c‖ > (5/8)(ε_1/16)/2 = 5ε_1/256. Correct.
- **The hypothesis "r_e ≥ r_* on E" in (ii) is not discharged anywhere.** It is stated as a hypothesis, and the one place a
  number is attached to it (§17.6 l.1917, r_* = ½) is explicitly "not needed by Theorem NA-PRICE^E". So this is a scope note,
  not a defect — but if (EG)'s mismatch half is ever built on l.1915-1919, r_e ≥ ½ will have to be earned.

## S5-12. The answer to [RPLD4-fix W-2] (l.1809-1813). **CONFIRMED.**
This is the best paragraph in the session. The S4 review's objection was that DIL-1's δ is gauge-variant (axial gauge spreads
a one-plaquette defect along a line). The reply — that with the kernel-centre completion δ_e is chain-gauge invariant and
equals √(2φ_e/r_e), so the "line" representation is a *different field with a different kernel energy, priced accordingly* —
is correct and is the right answer. The gauge-covariant currency is the kernel energy, not the link count. W-2 is discharged.

## S5-13. "max_e|W_e| = 2/81" (l.1808). **WRONG as stated; NARROWED to the true statement; not load-bearing.**
My exact computation: over the whole support of W (540 links) the maximum is **1/27**; over the links **interior to a corner
block** (the 216 on which the LP runs) it is **2/81**. The p5 script prints the latter inside its B5 line and the file lifted
it out of that scope. Nothing in §17 uses the number. **Fix P5-2 (minor):** write "max over the interior links of a corner
block".

## S5-14. "computed in exact rationals, printed to 6 digits" (l.1807). **NARROWED.**
F_c **is** exact — I get the rational **301/729** = 0.41289437585733885, in exact agreement, for each of the four links of
∂P, so F_* = 301/729. But the four numbers that the session actually reasons with — R_∞ = 2.037037 / 6.716049 and
R_2 = 0.1512 / 0.2811 (l.1818-1821) — are floating LP and least-squares outputs. checks/p5_time.txt says so plainly ("The LP
values are numerical …, not exact rationals; the rational identifications … are not used"); §17.3's header sentence does not.
**Fix P5-3 (minor):** move the "exact rationals" claim so it covers F_c and 2/81 only, and record F_c = 301/729.

## S5-15. (NP-F5) MET at linear order (l.1822-1828). **CONFIRMED, independently.**
- I reproduced R_2 = **0.151173** (one block) and **0.281095** (four blocks) to six digits with my own conjugate-gradient
  solve of the normal equations (residuals 1.4·10⁻¹⁶ and 2.9·10⁻¹⁸), in plain python, no BLAS and no scipy.
- I did not reproduce the LP optima exactly, but I do not need to: the load-bearing direction is the **primal** one. An
  explicit feasible A supported on the interior links of the corner blocks with max_p|φ_p(A)| = 1 gives W·A ≥ **1.667** for
  one block and ≥ **3.333** for four. That already clears the pre-registered B6 band (0.746) by 4.5× and §17.0's own NP-F5
  threshold (1/2) by 6.7×. The verdict does not depend on the LP being right.
- **The abelian/linear restriction is not a weakness here, and I want to say so plainly.** (NP-F5) is a negative claim, and a
  negative claim is settled by a counterexample family; abelian configurations embed in SU(2), so the primal lower bound
  transfers at leading order, and at ε_1 ≈ 6.7·10⁻⁴⁰ the nonlinear correction is O(ε_1²). The "[linear order]" caveat the
  file attaches is more conservative than it needs to be.
- The reasoning behind the verdict is also right: to move the centre plaquette by ε_1/4 you need max curvature
  ≥ (ε_1/4)/2.037 ≈ 0.123 ε_1 < ε_1, so a threshold defect suffices and there is no raised threshold. The S4 review's
  branch 1 ("thin cluster, γ < ½") is genuinely dead. This is a real negative result and the session earned it.
- Supporting exact checks I re-ran: B1 (divergence-free at every site), B2 (support confined to the corner-block pairs),
  B3 (F_P = 9 = L² exactly for the uniform field), B4 (zero on 20 random integer gauge functions), |supp W| = 540. All agree.

## S5-16. Negative control C1n is weak. **NOT-VERIFIED (as a discriminator).**
C1n fires in 6 of 300 samples. A control that fires 2% of the time when the constant is halved would not have caught a
modest overstatement of f_c. C1's max ratio 0.8637 is the more informative number. Not a defect (C1 is labelled evidential and
DIL-L (i) is proven), but §17.7 should not read C1n as strong evidence.

---

# PART 4: Lemma MD (priority 2; the other half of [E5] (2))

## S5-17. Lemma MD (l.1836-1844). **CONFIRMED-WITH-FIX.** This is the session's best result.
The architecture is right: a returned finer defect whose own kernel centre is good is priced by **its own kernel**, at rate
λκε_1²/256, by FT^far one level down plus KD one level down. No recursion, no 81^k, no level-(k-1) defect probability — the
81 is a union over choice functions, once per Q. I checked:
- the union over the 81^{|S_md|} choice functions is correct (a product of unions is a union of products);
- X_{k-1}(T) ⊂ L^∂_{k-1}(S_md) for T = {x_Q}, so neither G′ nor F reads it — this is what COL-DEC delivers;
- (C_S) holds for T one level down (same DJ + H-nest (iii) argument, m = k+1 > k−1);
- the event {x_Q ∉ 𝒞_{k-1}} is a function of U_{k-2} and so is admissible as part of FT^far's F;
- u_{k-2} ≥ u_k − 2R gives the e^{2λκε_1²R/256} prefactor, which is correctly carried into C_A (l.1857).
- **Fix P5-4 (statement):** "ν″ := ν with the chosen cubes declared" (l.1840) is written as a single law, but ν″ depends on
  the choice function. Harmless where MD is used (it is the last step of the theorem's proof, with F ≡ 1, so E_{ν″}[F] = 1),
  but the lemma as stated is not well-formed. Quantify ν″ inside the union, or state the lemma with sup over choices.

## S5-18. The "own kernel centre is good" threshold does not move between levels. **CONFIRMED.**
This was the sharpest question put to me and the answer is that there is nothing wrong here.
- 𝒞_j(U_{j-1}) (§16.3 l.1375-1377) is defined by r_c < ½ and ‖1 − V^0_P‖ ≥ ε_1/2. Both constants are global; ε_1 is a single
  constant of the whole construction, not a level-indexed threshold. Only u shifts with the level, and every shift is paid
  by (F_R) with an explicit e^{λκε_1²R/256} per level.
- 𝒞° (l.1799-1800) is a **different, strictly smaller** set (5/8 and ε_1/4), introduced only inside DIL-L (iii) and used only
  inside Proposition CD (c). §17.4's split (l.1832-1833) uses 𝒞_{k-1}, not 𝒞°. The two are never conflated, and the margin
  between them is exactly what DIL-L (iii) converts into the 5ε_1/256 centre-move. I looked for a slide between them and did
  not find one.
- Consequently MD's pricing is level-uniform in the only sense that matters: p′_mis's exponent and prefactor contain no k.

---

# PART 5: Theorem NA-PRICE^E (i) and Proposition CD (priority 1; counted item [E5] (3))

## S5-19. The implication (l.1851-1863). **CONFIRMED as logic.**
- The partition is exhaustive: for Q ∈ S (so Q bad) either Q ∉ 𝒞_k (→T), or Q ∈ 𝒞_k with G_Q (→S_0), or Q ∈ 𝒞_k with G^c_Q,
  and then every defect under Q is a mismatch or a centre defect, with "both ⇒ S_cd" stated. 4^{|S|} ordered partitions, and
  dropping 1{Q ∈ 𝒞_k} for S_md is an upper bound. Correct.
- The chain FT^far → KD → (J-NS^cd) → (SF-cap)^𝔉 + CW → MD stays under the one law ν′ throughout; each hypothesis is in the
  E[Π·F] ≤ (…)E[F] form, so the composition is legitimate; the measurability of each F (own columns) checks out.
- Constants: C_A = 4·max{…} with four branches and each per-cube factor ≤ (C_A/4)e^{-a_A u_k}. a_A = min{λκε_1²/256, 6θa_bad,
  a_cd}. All correct arithmetic.
- **Wording slip:** l.1858 defines E with "∩_T{Q bad, Q ∉ 𝒞_k}" and then l.1860 says "the indicator of E is a function of
  U_{≤k-1}". "Q bad" is a function of U_k. The repair is §16.5's: drop "Q bad" from E (it is implied by {S ⊂ D_k}) and keep
  only 1{Q ∉ 𝒞_k}. One word.

## S5-20. Does the deduction silently need more? **CONFIRMED (no hidden level-uniformity need) — with one real omission.**
I went looking for the three things the brief asked about.
- **Level-uniformity:** every constant in C_A and a_A is built from λ, κ, ε_1, R, n_int, θ, a_bad, c_sf, C_cd. None carries a
  level index, and no step recurses. The theorem inherits level-uniformity from its hypotheses and adds none of its own.
  Clean.
- **A level-(k+1) form of something proven at a fixed level:** I found none. The proof reads levels k−2, k−1, k only, plus
  the future through the weight w (which is HW's, not PLD's).
- **The real omission:** Proposition CD (b) l.1873-1877 invokes "the theorem at level k − 1" applied to
  E_ν[Π1{x_Q ∈ 𝒞_{k-1} ∩ D_{k-1}}·F] — i.e. the **F-conditioned** form. The theorem as stated (l.1856) is an unconditioned
  probability. Its own proof would carry an F (FT^far does, and both hypotheses are already in F-form), so this is
  repairable, but it is not stated. **Binding fix B3:** state Theorem NA-PRICE^E (i) in the form
  E_ν[1{S ⊂ D_k}·F] ≤ (C_Ae^{-a_Au_k})^{|S|}e^{c_A‖S‖_sh}E_ν[F] for F measurable on the other columns, which is also closer
  to what CAP-dec and (E2^𝔉) consume.

## S5-21. Does (SDP)^{A,far} as delivered MATCH what HW consumes? **NARROWED — three mismatches.**
The **shape** matches: S a set of level-k cubes in the columns of A ⊂ 𝒰_{k+1}, under the past law of levels ≤ k weighted by a
far weight, bound (C_Ae^{-a_Au_k})^{|S|} with a_A ≥ θa_bad. That is HW l.1256-1259 and it is a real achievement — the
re-ownership of (SDP) to node A (REVIEW_HW_S2 §5.3) is being honoured in the right law for the first time. But:
- **(i) Allowance currency** — slice vs union form (S5-9, S5-10). Binding.
- **(ii) Levels.** The theorem is k ≥ 2 (l.1854); §17.6 l.1907 discloses that k = 1 needs a level-0 analogue of MD and is not
  covered, and §16.5 l.1437 leaves level 0 as a sketch. HW's H7 (l.1370) asks for **every** level k ≥ 0, and TEL-f
  (HW l.1235-1237) applies the level-k bound once per level — it needs all of them. So the delivered interface has a
  two-level hole at the bottom. Honestly disclosed, but the lead should not read "(SDP)^{A,far} delivered".
- **(iii) Route.** (E1) vs (E2) — S5-8. Binding.

## S5-22. Proposition CD (a), (b), (c) (l.1869-1888). **CONFIRMED as stated.**
- **(a)** The trivial bound is LOOP-const: b(k) ≤ 81[c·e^{-6θa_bad u_{k-1}} + b(k-1)], η = 1. Correct, same arithmetic as
  Proposition WALL (a).
- **(b)** 324 = 4 branches × 81 choices (§16.6's 243 = 3 × 81) ✓; C_cd = 81ηe^{a_AR}C_A ≤ C_A/4 ⟺ 324ηe^{a_AR} ≤ 1 ✓. The
  disclosure "an induction on k whose base (level 1) is not covered" is correct and decisive: **CD (b) closes nothing
  today**, because the induction bottoms out at exactly the level the theorem does not reach. Add the two repairs of S5-9
  and S5-20 and it would still close nothing without η.
- **(c)** ARGUED, correctly labelled. The arithmetic is right: (ε_1/(4·0.2811))² = 0.791ε_1² and (ε_1/(4·0.1512))² =
  2.735ε_1² — I get 0.7910 and 2.7348. The depth bound log(2/ε_1)/log L² ≈ 41.6 at ε_1 = 6.7·10⁻⁴⁰ checks out
  (log(2/6.7·10⁻⁴⁰)/log 9 = 90.9/2.197 = 41.4). The conclusion — that η < 1/324 needs an energy-graded defect probability at
  level k−1, "a statement of the same kind as (SDP)^A one level down" — is the honest reading, and it is exactly what
  REVIEW_HW_S2 l.349 ("It is never proven from (SDP) at level k − 1") and l.372 ("LOOP-const would reappear there verbatim")
  forbid as a route.

## S5-23. The outcome labels (§17.8, l.1933-1955). **CONFIRMED.**
I tried to find inflation and could not. (NP-F4) MET for the centre-defect part, (NP-F5) MET at linear order, "Not success,
not the partial bar: the remaining hypothesis (J-NS^cd) is two-level and probabilistic" — all accurate against the
pre-stated bars at l.1695-1709. The one sentence I would strike is in (a): "recursions compound nothing (Cor. LAW (c)):
Proposition WALL (b)'s obstruction is gone" (l.1937-1938), for the reasons in S5-9. Replace with "WALL (b)'s *tilt*
compounding (c(k) ≥ c(k-1) + 4c_U) is gone; whether the residual's own allowance compounds depends on restating it in the
union form".

## S5-24. The newly-allowed R-operated representation was not used. **NARROWED (observation, not a defect).**
§17.0 l.1710-1712 adds the R-operated representation ((I_{k-1}^E)″, CL^J, R1^J, (SC), (SF-irr)) to the allowed inputs — the
single architectural change REVIEW_PLD_S4 Part 3 asked for. Nothing in §17.2-§17.6 uses any of them: no extracted activity
ρ_Y, no |ρ_Y| ≤ E_0^{|Y|}, no punctured completion with the R-operated field. §17.5 names (LCR^punct) "for the record" and
does not prove it; §17.5 l.1897-1901 explains honestly why the certified CE package does not contain it. What the session did
instead was **refute** the review's branch 1 by computation (S5-15) — a legitimate and valuable use of the round. But branch 2
((EG) from CL^J (c) with the kernel factors kept energy-graded) was neither attempted nor declared impossible. The route the
S4 review proposed is still untested on its own terms.

---

# PART 6: c_lcr (priority 4)

## S5-25. What is load-bearing on c_lcr, and is anything mislabelled? **CONFIRMED — no status error in PLD S5.**
I traced every occurrence.
- Inside PLD §17: c_lcr enters only through (SF-cap)^𝔉_{k-1} (= (LCR)_{k-1} in G-form, c_sf = c_lcr, Cor. LAW (b) l.1778-1780),
  which is a **named hypothesis** of Theorem NA-PRICE^E (i), and the theorem's status line says CONDITIONAL (l.1851).
  §17.5 l.1902 and §17.8 (b) l.1939-1940 both state "not certified" without hedging. §17.6 l.1911 the same.
- **None of the three counted items depends on it.** [E5] (1) GEO/FT^far/COL-DEC and [E5] (2) DIL-L/MD are c_lcr-free; I
  checked each proof. [E5] (3) is an implication whose hypothesis carries it. So the tally "+3 PROVEN-HERE" is not inflated
  by c_lcr.
- Downstream exposure (for the lead, not a PLD defect): c_lcr sits inside c_sf → C_fc = c_sf + 81C_Ae^{θa_badR} →
  C_ℓ = (1 − λ_*)^{-3n_int/2}C_fc → HW's b_n, ε_2, g²_CRC (HW §30.6 l.1636-1639) and B_0, n_H (REL-boot). HW already discloses
  this ("Node A's C_fc, C_A, c_A are NOT certified (PLD §16.7: c_lcr not certified), so they stay symbolic"). Nothing is
  claimed proven anywhere that rests on a *value* of c_lcr.
- **One word is doing too much work.** §17.8 (e) l.1947 says "a_A = …, C_A, c_A = c_cd explicit". C_A contains c_lcr and C_cd
  and c_A **is** C_cd's allowance constant. They are explicit *in terms of two uncertified symbols*. **Fix P5-5 (minor):** say
  "explicit in terms of c_lcr and (C_cd, a_cd, c_cd)".
- **A note to the lead on the handoff wording.** HANDOFF.md's PLD bullet reads "Also open: c_lcr is uncertified. The working
  value is θ ≈ 8e-7". These are two unrelated open items: c_lcr is the small-field moment constant, and θ ≈ 8·10⁻⁷ is the
  a_ret-driven planning value from §16.8 (p4 E), now re-expressed as θ ≤ a_cd/a_bad (l.1913). Nothing bounds θ by c_lcr.

---

# PART 7: check p5 — my own re-derivation (priority 5)

I did not re-run checks/p5_pld.py (it needs scipy and the numeric lock). I re-derived its part-B geometry and the §17.3-§17.6
constants from the criteria file's geometric specification, in my own code, with `fractions.Fraction`, no numpy, no BLAS.

| quantity | §17 / p5_out claims | my independent value | verdict |
|---|---|---|---|
| \|Γ_c\| (S4′ contours per coarse link) | 1944 (24 orders × 81 y) | 1944 | agrees |
| F_c, each link of ∂P | 0.412894 "exact rationals" | **301/729** = 0.41289437585733885 | **exact agreement**; the rational is new |
| F_* | 0.412894 | 301/729 | agrees |
| \|supp W\| | 540 | 540 | agrees |
| max_e\|W_e\| | 2/81 (l.1808) | **1/27** over supp W; 2/81 over int(corner block) | **misstated scope** (S5-13) |
| B1 divergence-free | exact PASS | 0 at every site, exact | agrees |
| B2 locality | exact PASS | every supported link lies in a corner-block pair | agrees |
| B3 F_P(uniform b=1) | 9 exact | **9** exact (= L²) | agrees |
| B4 gauge ⇒ 0 | exact PASS (10 χ) | 0 on 20 random integer χ, exact | agrees |
| R_2 (one corner block) | 0.151173 | **0.151173** (own CG, residual 1.4·10⁻¹⁶) | agrees to 6 dp |
| R_2 (four corner blocks) | 0.281095 | **0.281095** (own CG, residual 2.9·10⁻¹⁸) | agrees to 6 dp |
| R_∞ (one block) | 2.037037 (LP) | ≥ **1.667** by explicit feasible point | consistent; LP not re-run |
| R_∞ (U4) | 6.716049 (LP) | ≥ **3.333** by explicit feasible point | consistent; B6 verdict independent of the LP |
| B6 rule outcome | NP-F5 MET (≥ 0.746) | MET on my lower bound alone | **confirmed** |
| §17.3 coefficient (1/(2F_*))(5/256)² | 4.62·10⁻⁴ | **18225/39452672** = 4.6194590·10⁻⁴ | exact agreement |
| A2 κ_eg | 2.006901·10⁻⁴ | **154112/767910375** = 2.0069006·10⁻⁴ | exact agreement |
| CD (c) 0.79ε_1² / 2.73ε_1² | (1/(4·0.2811))², (1/(4·0.1512))² | 0.79100, 2.73484 | agrees |
| A1 | 5/256 = (5/8)(1/16)/2 | true (tautology) | agrees |

Process: one run under the lock, 11:32:22-27, 4.1 s, 257 MB, load 3.40, 36% free, nice 10, one BLAS thread, one `rmdir`, exit
0 (p5_time.txt). All within the brief's limits. The criteria-header timestamp discrepancy ("≈11:33" vs mtime 11:30:24) is
disclosed in p5_time.txt and the header is not edited — correct handling. §17.7's scope paragraph (l.1930-1931) is accurate:
nothing in p5 tests the measure, (CLS-min), (SF-cap), (LCR), (J-NS^cd) or the nonabelian centre map.

---

# PART 8: does PLD S5 supply HW's (E2^𝔉)? (the question the lead asked)

**(E2^𝔉)_{θ,ρ} as HW states it (HW.md l.1524-1537), for every R ∈ 𝔉_𝔥, every j ≥ k_0, every finite Γ ⊂ level j+1 and every
finite Y of level-j cubes outside col(Γ) with col(Γ) ∪ Y R-free, ν = ν^{R,F}_j, w = h^{R,1}_j:**

  E_{ν^w}[Π_{Q∈Γ}e^{θmin{π_Q,Y^f_Q}} · 1{Y ⊂ D_j} · 1{Buf^R_ρ(col Γ ∪ Y) ∩ D_j = ∅}]
    ≤ C_fc^{|Γ|}(C_Ae^{-a_Au_j})^{|Y|}e^{c_A‖col Γ ∪ Y‖_sh}.

## S5-26. **VERDICT: PLD S5 does NOT supply (E2^𝔉). It supplies a part of the Γ-factor and none of the Y-factor.**
Three independent reasons, each on its own sufficient.

1. **Wrong pattern family.** (E2^𝔉) is asked uniformly over 𝔉_𝔥 = all upward-closed **column relaxations** R^{-𝒞} of R(𝔥)
   (HW l.1477-1479), and HW l.1534 names this as one of its two defining features. PLD §17.2 l.1736 fixes the law at
   1_{R(𝔥),j} and extends only by **declarations** inside the proof; Cor. LAW (d) l.1786-1787 states the uniformity achieved
   as "uniformity over declarations at levels k and k−1 inside the columns of S (finitely many patterns, all inside the
   proof)". Declaration adds defects; relaxation removes constraints on whole columns. These are different families, and
   HW's own §30.7 l.1660-1662 says the question is open and is node A's: "whether node A's proof … is uniform over such
   patterns is a node-A question; nothing in HW decides it." §17 does not answer it, and does not mention 𝔉_𝔥 at all
   (zero occurrences of "column-relaxed", "upward", "R-free" in l.1664-1966).
2. **Wrong geometry for Y, and the c_f = 0 mechanism fails exactly there.** Y is a set of **far** level-j cubes, outside
   col(Γ), made R-free by relaxing their own columns (HW l.1573-1576, step (4) of CRC-2T). PLD's theorem is stated only under
   the standing condition (C_S) (l.1741), which requires S to lie in the level-k part of the columns of 𝒰_m for some m > k.
   Y does not. Worse, the two lemmas that give c_f = 0 break for Y:
   - **GEO (ii) fails.** Its proof uses π(Q) ∈ A ⊂ 𝒰_{k+1}. For a far y ∈ Y, the crossing links from y to a neighbouring
     cube b that is **not** R-free lie in X_j(Y) and have a non-free endpoint cube, so by Theorem LI^U-0′ (HW l.1486-1490)
     the weight w = h^{R,1}_j **may read them**. PLD's hypothesis L_G ∩ X_k(S) = ∅ therefore fails.
   - FT^far survives (it only consumes L_G ∩ ℓ(S) = ∅, S5-6, and the interior links of a free cube are not read), but
     **COL-DEC does not**: GEO (i) routes the level-(j-1) reading through the crossing links, so G′ can read
     L^∂_{j-1}(Y). Without COL-DEC there is no product-kernel law one level down, hence no Lemma MD and no (SF-cap) step for
     far cubes. The session's whole mechanism is tailored to history columns.
3. **No buffer anywhere.** (E2^𝔉)'s content is **screening by a good buffer** (HW l.1298-1305, l.1657-1659: "a buffer whose
   interior curvature is < ε_1 everywhere must screen the column from the far field … That is plausible but not shown").
   §17 contains zero occurrences of "buffer", "Buf", "screen" or "(E2)" as a route. The one place the far field appears,
   §17.4 l.1855, quantifies over **all** far weights — the (E1) form HW has abandoned.

**What §17 does supply towards (E2^𝔉), honestly stated:**
- The **Γ-factor with Y = ∅ and R = R(𝔥)**: the fine moment on history columns reduces to (LCR)_{k} in G-form with
  **c_sf = c_lcr and c_f = 0 exactly** (Cor. LAW (b) l.1778-1780, §17.6 l.1910-1911). This is real, it is the first exact
  version, and it is the half HW already believed was the easy one. It is conditional on (LCR), which is uncertified.
- The **law identification**: ν^{(k)}_k with the finer spectators Φ_{k′}, k′ < k, is exactly HW's finer-first TEL-f law
  (HW l.1242-1243, l.1626-1631). That identification is correct and useful.
- The **allowance** is delivered in the wrong currency (S5-10) — (E2^𝔉) wants ‖col Γ ∪ Y‖_sh.
- Nothing at all towards the Y-factor, the buffer, or 𝔉_𝔥-uniformity.

**Net:** HW's new wall (W-𝔉) = (E2^𝔉) is **untouched**. If the lead was hoping PLD session 5 would discharge it, it did not;
if the lead was hoping it would reduce it, it reduced only the Γ-side bookkeeping. Binding fix B1 (restrict to buffered
weights) is the cheapest way to make the two lanes talk, and it costs PLD nothing: FT^far, GEO and COL-DEC are all intact
under the buffer indicator, because buffer cubes sit at level-(k+1) index distance ≥ 2 from A and their interior links are
disjoint from X_k(S).

## S5-27. Notation collision between the lanes. **CONFIRMED (binding, cheap).**
PLD introduces **(SF-cap)^𝔉** with "𝔉 = the law family of COL-DEC" (l.1953). HW uses **𝔉_𝔥** for the column-relaxed pattern
family and names its new wall **(E2^𝔉)** after it (HW l.1477, l.1524). Two different objects, same superscript, in two files
that must interface, with (SF-cap)^𝔉 and (E2^𝔉) both being node-A small-field inputs at the same level. This is the GE-T name
clash of REVIEW_BFT_B_S8 repeating itself. **Binding fix B4:** rename PLD's to (SF-cap)^{COL} or (SF-cap)^{G}.

---

## (a) Binding fixes (for the PLD owner)

1. **B1 (route).** Restate Theorem NA-PRICE^E (i), (SF-cap)^𝔉_{k-1} and (J-NS^cd)_k for **buffered** far weights only
   (w = 0 unless Buf^R_ρ(col S) ∩ D_k = ∅, HW l.1293-1297), not "for every law ν_G" / "any w". As written the hypothesis set
   is expected unsatisfiable, because the conclusion contains HW's (E1), declared EXPECTED FALSE in sup form at HW l.1286-1292.
   Record HW's E1-1 and the (E2) route of record in §17.6 and §17.9. Verify (one line) that FT^far, GEO and COL-DEC are
   unaffected by the buffer indicator.
2. **B2 (currency).** Replace the per-level slice s_k(𝔥) by the union form ‖S‖_sh (and ‖col Γ ∪ Y‖_sh at the interface) in
   (J-NS^cd) (l.1848), Theorem NA-PRICE^E (i) (l.1856), §17.4 l.1865 and §17.6 l.1905-1906, per HW [RHW4-fix SL-1]
   (HW l.1261-1266, l.1373) and PLD's own §16.5 l.1415. Add the one-line union-form excess bound
   ‖x(S)‖_sh ≤ ‖S‖_sh + c|S| with c depth-free, on which Cor. LAW (c) and Proposition CD (b) rest.
3. **B3 (statement).** State Theorem NA-PRICE^E (i) in the F-conditioned form E_ν[1{S ⊂ D_k}F] ≤ (…)E_ν[F]; Proposition
   CD (b) already consumes it and the proof already supports it.
4. **B4 (naming).** Rename (SF-cap)^𝔉 — it collides with HW's 𝔉_𝔥 and (E2^𝔉).
5. **B5 (claim).** §17.8 (a) l.1937-1938: "Proposition WALL (b)'s obstruction is gone" → "WALL (b)'s *tilt* compounding
   (c(k) ≥ c(k-1) + 4c_U) is gone; the residual's own allowance compounds unless stated in the union form". §17.6 l.1906's
   "the tilt contributes nothing" → "the tilt is converted exactly into the far weight w; what it costs is the uniformity in
   w (HW Cor. LI-0 (b) as amended, HW l.1134-1137)".
6. **B6 (scope).** Say in §17.6 and in the tally that H7 is **not** delivered: k = 0 and k = 1 are uncovered and TEL-f needs
   every level.

## Recommended (non-binding)
- P5-1: record the rule-2 breach in p5_criteria.md (A1's 5/8, 5/256 are session-5 constants).
- P5-2: "max_e|W_e| = 2/81" → "max over the interior links of a corner block"; over supp W it is 1/27.
- P5-3: scope the "exact rationals" claim to F_c and 2/81; record F_c = **301/729**.
- P5-4: Lemma MD's ν″ must be quantified per choice function.
- P5-5: §17.8 (e) "explicit" → "explicit in terms of c_lcr and (C_cd, a_cd, c_cd)".
- P5-6: §17.7 should not cite C1n as a strong control (6/300).

## (b) Independent tally of what session 5 adds

Counted items, my verdicts:
- **[E5] (1) Lemmas GEO + FT^far + COL-DEC: CONFIRMED.** The exact law conversion on HW's route, c_T = 0. Genuinely new and
  genuinely proven. Its value is narrower than §17.8 states: it removes the tilt *allowance*, not the tilt's content.
- **[E5] (2) Lemma DIL-L with Lemma MD: CONFIRMED-WITH-FIX** (P5-4 only). DIL-L is the correct gauge-covariant replacement
  for DIL-1 and discharges W-2. MD is the session's strongest result: the mismatch half of (J-NS^dir) is now proven at the
  kernel rate, with no recursion.
- **[E5] (3) Theorem NA-PRICE^E (i) as an implication: CONFIRMED-WITH-FIX** (B1, B2, B3). Valid logic; the hypothesis set as
  quantified is expected unsatisfiable, and the allowance is in a currency HW has struck.

**0 WRONG and 0 GAP among the counted items.** One statement outside the counted set is wrong as written (S5-13,
max_e|W_e|) and one interface claim is wrong (S5-10, the slice).

Uncounted:
- Corollary LAW (a), (b), (d): CONFIRMED. (c): CONFIRMED-WITH-FIX (S5-9).
- Proposition CD (a), (b): CONFIRMED as arithmetic; (b) closes nothing (base level uncovered). (c): ARGUED, correctly
  labelled.
- The p5 B computation: CONFIRMED and independently re-derived (Part 7).
- §17.5: CONFIRMED as an honest negative ((LCR^punct) named, not proven; the certified CE package does not contain it).

**Net movement of the wall.** Session 4 left (J-NS^dir): "coarse centre bad + returned finer defect in the column". Session 5
splits it and proves one half. What is left, (J-NS^cd), is strictly smaller: "coarse centre bad + a finer defect whose **own**
centre is bad". That is a real narrowing and I would not have been able to obtain it myself from §16. Against that: the
interface moved onto a route HW abandoned mid-session, and the one architectural input the S4 review added (the R-operated
representation) went unused.

## (c) Explicit verdict on HW's (E2^𝔉)

**PLD session 5 does not supply (E2^𝔉), and does not supply its hard half.** It supplies (i) the Γ-factor with Y = ∅ and
R = R(𝔥), reduced exactly to (LCR) in G-form with c_sf = c_lcr, c_f = 0 (conditional, c_lcr uncertified), and (ii) the correct
identification of HW's consumed law. It supplies **nothing** towards the far-defect factor 1{Y ⊂ D_j}, nothing towards the
good-buffer screening indicator, and nothing towards uniformity over the column-relaxed family 𝔉_𝔥 — and for far Y the very
mechanism that makes c_f = 0 (GEO (ii), hence COL-DEC) **fails**. HW's (W-𝔉) is where it was. See S5-26 for the three reasons
and for the cheapest repair (binding fix B1), which does not cost PLD any of its session-5 results.

## (d) The biggest live wall in this lane

**(J-NS^cd) restricted to buffered far weights — and specifically its (EG) content: an energy-graded price, at level k−1, for
a defect cube whose own kernel centre is bad.** Everything else in the lane is now either proven or reduced to it:
- The mismatch half is gone (MD).
- The thin-cluster escape is gone, by computation: §17.3 shows a corner-block cluster moves the coarse centre plaquette by
  ≈ 2.04× its maximal curvature, so there is no sup-form dilution and no raised threshold ((NP-F5), which I confirmed
  independently). Branch 1 of REVIEW_PLD_S4 Part 3 is dead.
- What remains is branch 2, unchanged in substance since REVIEW_PLD_S4: a price for the cluster itself, graded by its energy
  above its completion. §17.3's ℓ²-curvature constants give the deterministic half of the grading (0.1512 / 0.2811, so a
  centre-moving cluster carries curvature energy ≥ 0.79ε_1², ≥ 2.73ε_1² in one block). The probabilistic half — that this
  energy is charged — is not in hand, and Proposition CD (c) is right that it is "a statement of the same kind as (SDP)^A one
  level down". Its only named source remains CL^J (c)'s proof with the kernel factors kept energy-graded (REVIEW_PLD_S4
  l.258-259); that has still not been attempted.
- Until it exists, θ ≤ a_cd/a_bad and the planning value stays θ ≈ a_ret/a_bad ≈ 8·10⁻⁷, i.e. n_H × ≈ 5·10⁴, exactly as the
  previous review said. Note the compounding with HW's own session-5 arithmetic: HW §30.6 l.1639-1643 already needs
  g_K² < 4.9·10⁻⁹⁷/c_+ and n_♯ larger by ≈ 10¹⁰. The constants are moving the wrong way faster than the walls are falling.
