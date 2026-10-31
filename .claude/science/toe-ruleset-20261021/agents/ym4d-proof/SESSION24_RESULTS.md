# Session 24: worker results as they land (lead's running ledger)

Scored against the pre-stated targets of RTARGET.md §51. Statuses are the reviewers'/workers' own labels.
Nothing here is counted in PROOF.md's tally until the consolidation.

## REVIEW_FLOW_S13 (T51-A, 1 of 5) — landed. 727 lines.

**Verdict: session 13 is complete and its provenance is clean.** The handoff's "stopped mid-run" worry does
not materialise: (X1)-(X6) all dispositioned, all six pre-stated failure modes adjudicated, verdict
arithmetic reconciles (21 pre-stated lines / 19 PASS; 31 lines / 28 PASS). All nine [RFL12-fix] fixes
applied and correct. Four f16 artifact sizes/md5s and FLOW.md's md5 re-verified; §103's first-edit byte
accounting reconciles to 3494 B of insertions.

**The expected damaging finding is NOT there.** "Pairing at U = 1 grows" does not degenerate SLICE-U at the
trivial field: at ε = 0 the decomposition reduces to the proven VC-T0, and f16's own c_0(i) = 1.1111e-1,
1.2346e-2 is the exact L^-2 ratio. The growth is an ε² bookkeeping artefact of the *frozen* U = 1 slice.
PROOF.md l.6633's "FLOW BFT-2, 3 at the trivial field" is what FLOW **consumes** from BFT, a different
object. **SLICE-U is stronger than claimed:** clause (a) holds at *every* U (FLOW l.3738), not only at Cartan.

**The Cartan restriction is a genuine upstream reduction, not a measure-zero dodge.** c^tot_n is *defined* at
constant Cartan flux (FLOW l.3835); Lemma F-Π (i) gives the exact colour reduction (l.1548); §99's (T-a) was
already a Cartan-plane-wave statement. The root-sector linearisation genuinely block-diagonalises. But
§103-§110 never says *why* Cartan suffices — binding fix.

**One real mathematical gap. §105 (c), chain half (l.4680-4681): CONFIRMED-WITH-FIX.** The step from the
pointwise identity to the covariance needs avg_T N_T = avg_T N̄_T, which the pointwise identity does not
supply. It does follow from the maximiser's Lagrange condition (Im r_k independent of k), already in FLOW at
l.3010. Reviewer's numerics: off the maximiser the two averages differ by 0.137; at it they agree. True
statement, incomplete proof, N ≥ 3 only.

**Label and normalisation defects.**
- "PROVEN given (Π-loc)" is labelled in only 2 of 4 places (§107's heading and §110's tally omit it). The
  *count* is right under this lane's convention (REVIEW_FLOW_S9 l.371), so the reviewer confirms 75 / strict
  70, but the label must be added before PROOF.md quotes it. (Π-loc)'s one-line argument covers only its
  colour clause; at Π_j = 1 it is not needed, so **VC-T1 at Π = 1 is unconditional**.
- **§107 (d) over-normalises: NARROWED.** (c) is sharp at λ̃-degree 2 (matching (T-a2)); (d) states the rate
  only after Ñ_r of degree 12 (r = 1) and 30 (r = 2) where ≤ 4 / ≤ 8 is needed, permitting |K|^-30 blow-up
  at small K.
- §106 misquotes 2.92 where f16_out.txt says 2.8916. §106's withdrawal note quotes 1.99e-2 → 2.46e-3 from a
  (3,3,2,1) smoke run that **exists in no committed artifact and is not in FLOW_LOG** — one orphaned output.
- The log's byte-reconstruction recipe needs `flow13/`, which is gone, so that claim is now unverifiable
  (session 12's was reconstructed by its reviewer).

**Process findings (these matter beyond this lane).**
- **B3/B4 are honest FAILs with a correct diagnosis but self-inconsistent criteria.** δ = 0.02 *was*
  pre-registered; both FAILs are reported and the post-hoc runs labelled (even add1-B4 is reported as a FAIL).
  B4's δ⁴ claim verified to 0.8% (reviewer recomputed the field amplification as 7.4598, step 0.1492). But the
  criteria's own stated O(δ⁴) already gives 1.6e-7 > the 1e-7 threshold at δ = 0.02: **the FAIL was fixed at
  pre-registration.** And **B3 has no scaling test** (its smaller-δ value is at the roundoff floor), so
  §109's δ⁴ attribution is demonstrated for B4 only.
- **Unlogged threshold relaxation:** §103 pre-stated B2 ≤ 0.5; f16_criteria.md says ≤ 0.6, unlogged. No
  verdict affected (0.418).
- **The 1.03 GB smoke run is a disclosed breach of the 1 GB cap, and it was consequential:** it forced the
  (3,3,2,2) → (3,3,1,1) substitution, the single largest weakening of the session's evidence.
- **0.107 shrink: NARROWED, nothing load-bearing on it.** One ratio per order, SU(2) only, on a torus whose
  two short directions are a single site → 6 momenta, **all with λ̃ ∈ {3,6}, i.e. no small K at all** — which
  is exactly the probe REVIEW_FLOW_S12 §10.3(ii) asked for. §107 (b) derives the L^-i bound analytically
  (reviewer re-derived it), so the numerics are corroboration only.

**What is in hand.** (T-a2): PROVEN, unconditional, orders 1-2, with the sharp λ̃(K)λ̃(K+P) normalisation.
(T-a1): about half, conditionally — the 𝒞-part at the Cartan plane wave, orders ≤ 2, given (Π-loc), with
heavier-than-specified normalisation. Open: (T-a1-M) (the M-part, carrying the |K|^-2 IR content, the harder
half) and (T-a3) (newly named). (T-a1) moved; it did not close, and §110 says so.

**LEAD NOTE (simplification, worth carrying into the consolidation): (T-a1-M) and (T-b) are ONE wall**, the
fine background-dependent inverse H_⊥(U)^-1. FLOW's open list is therefore shorter than it reads.
Runner-up, and the item that decides whether any of §107 reaches the target: **(T-c)**, the plane-wave ↔
constant-Cartan-flux exchange, since c^tot_n is defined at U_f while everything proven in §104-§107 lives at
a plane wave.

**Scoring against T51-A's pre-stated expectation** (at least two of five reviews narrow, demote or refute a
headline): this review NARROWS §107 (d) and the 0.107 reading, and finds one incomplete proof. It does not
refute a headline. 1 of 5 in; expectation not yet decided.

## REVIEW_PLD_S5 (T51-A, 2 of 5) — landed. 561 lines.

Reviewed PLD.md's 1966-line prefix, byte-identical to the cited md5 (35b33c8f…); session 6 is a pure append
from l.1967 and was ignored. Provenance clean (§17.0 genuinely first, md5 chain verifiable at both ends);
one minor rule-2 breach (p5 criterion A1 uses session-5 constants — a tautology, immaterial).

**Tally: [E5](1) CONFIRMED; [E5](2) and [E5](3) CONFIRMED-WITH-FIX. 0 WRONG and 0 GAP among counted items.**
One uncounted statement and one interface claim are wrong. 6 binding fixes, 6 recommended.

**Headline: "c_f = 0" is TRUE — and the cost moved into a quantifier that HW has just declared FALSE.**
Lemmas GEO, FT^far and COL-DEC are correct (the reviewer re-derived all four GEO clauses, enumerated the
factors FT^far must exclude, and could not break them). The geometric separation they need
(X_k(S) ∩ L^far_k(𝔥) = ∅, S ∩ 𝒰_k = ∅) **is** genuinely supplied by HW in the form used (Theorem LI^U-0 /
Corollary LI-0 (b); DJ + H-nest (iii) via REVIEW_HW_S2 l.364). **But** the theorem is asserted for *every*
far weight w (PLD l.1855, l.1905), which is exactly HW's **(E1)** — and HW.md l.1286-1292 [RHW4-fix E1-1]
now calls (E1) **EXPECTED FALSE in sup form**, with "the route of record is (E2)". So the hypothesis set is
expected unsatisfiable as stated. The reviewer traced which hypothesis breaks: (SF-cap)^𝔉 with uniform
c_sf, or (J-NS^cd); the kernel branches survive. Timing is exculpatory (PLD read HW at 10:56-11:22; E1-1
landed 11:24-11:29) but HW's pre-existing "(E1) in its sup form is doubtful" (l.1282-1285) was visible and
is unmentioned. **Binding fix: restrict to buffered weights.** FT^far / GEO / COL-DEC survive the buffer
indicator unchanged, so the restriction costs the session nothing.

**Second binding finding: the allowance is in a struck currency.** §17.4 l.1848/l.1856 state it as the
per-level slice s_k(𝔥); HW l.1261-1266 [RHW4-fix SL-1] struck the slice as mis-indexed, and PLD's own §16.5
l.1415 used the union form ‖S‖_sh. Not cosmetic: in the slice currency **Corollary LAW (c)'s "no allowance
compounds" and Proposition CD (b)'s recursion do not type-check** (level k-1 carries s_{k-1}, the target
wants s_k; unwound it gives e^{Kc·s(𝔥)} — exactly SL-1's objection). In the union form they close.

**(E2^𝔉): NOT supplied.** Three independent reasons: (i) wrong pattern family (declarations, not
upward-closed column relaxations 𝔉_𝔥); (ii) **(E2^𝔉)'s far set Y violates PLD's standing condition (C_S)
and GEO (ii) FAILS there**, so h^{R,1}_j can read the crossing links of X_j(Y) and COL-DEC breaks;
(iii) §17 contains zero occurrences of buffer/screening. What it does supply is the Γ-factor at Y = ∅,
R = R(𝔥), reduced exactly to (LCR) in G-form with c_f = 0 — the easy half, conditionally.
*This answers the handoff's open question "does PLD S5 supply HW's (E2^𝔉)?" with a clear no.*

**Confirmed and unbroken:** Lemma MD (the session's best result — the mismatch half of the wall genuinely
proven at the kernel rate, no recursion, no 81^k); the "good" threshold does **not** drift between levels
(𝒞_j uses level-independent ½ and ε_1/2; 𝒞° is a separate set, never conflated); DIL-L (i)-(iii) and its
answer to W-2; the NA-PRICE^E implication as logic; no hidden level-uniformity need.
**c_lcr: no status error** — all three counted items are c_lcr-free and every mention says "not certified".

**p5 independently re-derived** (exact rationals, plain python, no BLAS, no lock): F_c = **301/729** exactly
(new; exact agreement with 0.41289437585733885), B1-B4 exact, |supp W| = 540, R_2 = 0.151173 / 0.281095
reproduced to 6 dp by the reviewer's own CG, κ_eg = **154112/767910375**, the 4.62e-4 and 0.79 / 2.73
constants exact. NP-F5 confirmed independently of the session's LP: an explicit feasible point gives
R_∞(U4) ≥ 3.33 against the pre-registered 0.746. **One misstatement:** §17.3's "max_e|W_e| = 2/81" is true
only over interior links of a corner block; over supp W it is **1/27**.

**Biggest live wall: (J-NS^cd) restricted to buffered weights — specifically its (EG) content.** The
thin-cluster escape is now dead by computation, so **branch 2 of the REVIEW_PLD_S4 review is all that is
left, and it has still not been attempted.**

**LEAD NOTE (cross-lane, the most important thing in this review).** HW and PLD have drifted apart without
either lane noticing: **HW's route of record is (E2), PLD S5's theorem is stated for (E1), and (E1) is
expected false while (E2^𝔉) is not supplied.** Neither lane is wrong internally; the interface is broken.
Both binding fixes (buffered weights; the union allowance currency) are cheap and were forwarded to the
node-A worker mid-run.

**Scoring T51-A:** 2 of 5 in. This review narrows a headline (the quantifier) and finds a struck currency;
FLOW_S13 narrowed two items. The pre-stated expectation (≥ 2 of 5 narrow, demote or refute) is **met**.

## REVIEW_SQ_S4 (T51-A, 3 of 5) — landed.

**The decision the handoff asked for: (CLS-min) delivery is PARTIAL — yes in form, no in number.**

Clause by clause against HW.md l.178-180 and RLARGE.md l.88-90, route β's chain produces **exactly** what
RLARGE consumes: every m ≥ 1, level-m side ≥ 3, *every* top V, min-form in ‖1-V_P‖²_op, ℰ_P(V) as the
cone-local **free-boundary infimum**, depth-uniform, cone-local not global. **No level-uniformity, norm,
boundary or cone-locality mismatch.** c_pr = 5.56e-7 unchanged. This is a better result than expected: the
interface is clean.

**But the number is not there.** RLARGE uses a_bad = c_pr·min{ε_1², t_pr²} = c_pr ε_1², valid only while
ε_1 < t_pr, which REVIEW_RLARGE_V3 l.286/l.313 pins as C_D ≲ 7e15. Session 4 turns C_D from an O(1)
parameter into **C_D ≈ (0.5-0.9)e3 · C_T**, where C_T is EPS-T's **uncomputed** Moser constant (via
A_0 = c_N·C_T'·(…), C_T' = 22.6 C_T, G = 2(1.011 A_0 + B_0)). **So the condition reads C_T ≲ 1e13, and
nothing bounds C_T.** The reviewer's read of the written proof puts it in 1e9-1e15 — **straddling the
threshold.** C_err = 1.655e7·C_D² was re-derived and validated against all three recorded θ_0 values, so the
inequality is exact. **Answer to the brief's question: yes, a downstream consumer needs a number from EPS-T,
to one decade.** New OPEN item **(CONST-T)**; the lane tally is 14 / 1 / **2**, not 14 / 1 / 1.

**"Integrable, not bounded": no slippage. The reviewer could not break it.** The averaged → pointwise arrow
is *inside* EPS-T and is licensed by q > d = 4 (the source enters in divergence form through
⟨𝒮, D_1*(ψu)⟩; V_s sits in ℓ^{q/2} with q/2 > d/2, at exactly constant scale-invariant norm). The q = 8
bookkeeping was re-done: hypothesis and conclusion sides are identically scale-invariant. TPL, (N1), (N2),
LEV-E, LOC-T, CARL and GARSIA all re-derive correctly; CARL is the genuine mechanism and is depth-uniform
for the stated reason. S4-F1…F4 all correctly adjudicated as non-occurring.

**One real hole (S4-3, binding).** EPS-T's proof asserts "|u| ≤ ε … so every plaquette has η ≤ c_Nε ≤ ¼"
(l.1467). **Circular:** §15.0's comparison is itself conditional on ‖1-U‖ ≤ ¼, and small |𝒫| does not give
small ‖1-U‖ — in SU(2), U = -1 gives 𝒫 = 0 with ‖1-U‖ = 2. BIA, WB and the R_1 bound all need η small.
The fix is one added hypothesis, discharged in every application. The reviewer could not build a
counterexample, so **not WRONG** — but the proof does not cover the stated class.

**Label and arithmetic defects.** EPS-T's PROVEN label **overstates what is written** (the Moser bookkeeping
is asserted, not expanded) — relabel. R_0 = 64 should be **128** (at 64 ≤ R < 128 the iteration runs zero
steps). e^{100} should be 1.6e4.

**The two failed checks.**
- **q4b P0 is substantive about the check, not the mathematics, and it REVERSES REVIEW_SQ_S3 R1.** The
  reviewer reproduced the mechanism independently in pure python: the det-normalised polar factor of
  complex-perturbed M has residual 3.7e-9 against the quaternion-projection maximiser's 1.2e-16, with a
  value gap of 4.4e-16 — second order, so K3 still passes.
- **q5 T2: the error is in the pre-registered criterion itself**, not only in the script (q5_criteria.md
  defines the wrong Q_str). It falsifies d∘Q_str^{uniform} = Q_2∘d, leaves TPL untouched (T1 exact), but
  **exposes a real conflict between BFT_B l.2189 and LINEAR_PACKAGE l.71** that the session referred to lane
  B without citations. *LINEAR_PACKAGE is FROZEN v1.1 (errata only), so this is an erratum candidate and
  needs the lead.* Also q5's W1-W3/B1 run on a side-3 torus where WB's locality claim is untestable.

**Thresholds the session never states, though its own constants force them:** θ_0 ≤ 1.46e-13,
τ_R ≤ 2.75e-15 (**[CORRECTED by TAUFLAT §6.5: τ_R is NOT the binding entry. τ_♭ is a min with TWO
entries that BOTH bind (SQ.md l.317-319), and θ_0^SUP/C′ is the binding one at the current C_D; "τ_♭ = τ_R"
is an EVALUATION, not an identity. This entry also carried "C_D ≈ (0.5-0.9)e3·C_T" alongside it, which is
what makes the two inconsistent — the lead propagated both in one paragraph.]**), η_♭ 1e-26 → 4.2e-36,
t_pr 7.6e-9 → 1.5e-13. (CVX-K) really is unused, including inside LU-ex. LU-ex's replacement for the
continuity method is complete and the Łojasiewicz withdrawal is correct.

**>>> This revises INTEGRATION_AUDIT.md. REVIEW_SQ_S2's "BFT as stated is insufficient" is now MOOT for SQ:
θ_w = 2 is PROVEN, and EPS-T + NREFL supply the free-boundary cone-box clause.** §13.8 was not updated —
binding fix — and that makes **RLARGE row 9 and HW row A5 stale**.

**Biggest live wall: (CONST-T), EPS-T's Moser constant.** Not the mathematics of route β.
*Lead reading: this is the most tractable high-value item surfaced so far — a bounded, session-scale
computation that decides whether the whole (CLS-min) → RLARGE interface carries a number or not.*

## REVIEW_HW_S5 (T51-A, 4 of 5) — landed. 714 lines. The most consequential review of the five.

HW.md's md5 unchanged; no numeric lock taken (everything exact/Decimal in plain python). 11 binding fixes.

**The headline survives and could not be broken.** Theorem CRC-2T (HW.md l.1554-1604) is a correct
implication. The induction is on the finite integer N(R) = |S_R|, every inner application is at a strictly
smaller value, the telescoping is exact, and step (4)'s event algebra (three R-freeness / maximality clauses)
holds. **Both of the lead's primed suspicions fail to materialise:**
- it is **not** a nonlinear bootstrap — inducting on the *number of constrained pairs* instead of on the
  level is the session's real idea, and it is what closes the m = k+1 step REVIEW_HW_S4 said could not close;
- **no one-species criterion is applied to a two-species gas.** (S1) *is* the species-1 criterion in the
  standard Δ²z ≤ ½ form (step (6)); the far-defect → animal direction is paid by the induction's own c_U and
  closed by 2ε_2 ≤ c_U. Both cross terms are accounted for.

**But there is no cluster expansion.** §30.4's "two-type gas" is a **bestiary**: no partition function, no
compatibility relation, no Mayer identity, no Kotecký-Preiss criterion. §29's Target V2(a) ("bounded by the
gas's partition-function ratio or polymer sum") is **never delivered**. The induction is *better* than what
was asked and should be claimed as that, not as a cluster expansion.

**>>> THE KEY QUESTION IS ANSWERED FAVOURABLY: the smallness condition IS satisfiable.** The reviewer traced
the g-dependence of every constant: a = θc_prε_1² with ε_1 at its own **g-free** ceiling; H5 *relaxes* as
g → 0; c_att, b_n, b_D are pure geometry; a_A ≥ θa_bad. **g²_CRC is a fixed positive number, not a moving
target.** The self-defeating failure mode does not occur.

**Three reversals of session 5's own reported verdicts** (independent 120-digit Decimal arithmetic):
1. **(S2) and (T) impose nothing new.** (S2)'s ceiling = 4.89789e-97; REL-boot's r ≤ ½ ceiling at the
   session's own c_f = **4.89802e-97**; HIST-sum's own condition = **4.898e-97**; (T)'s threshold
   9.99104e96·c₊ against n_H(a, B_0) = **9.99102e96·c₊**. **The entire tightening is the ×6561 that SH-att's
   N_4 step puts into c_f.** One lever, not a chain.
2. **>>> THE BREACH DOES NOT BIND.** REVIEW_RLARGE_V3 l.61 and REVIEW_SF_S7 l.335 put the binding ceiling at
   **g_0² ≲ 2.5e-152/C_Ω — slack by ~55 orders** for c₊ ≲ 2e55. **HANDOFF's resume step 3, "lower g_0 and
   recheck the SF thresholds", is WITHDRAWN.** There is no constants crisis; session 5's text implies one
   that does not exist.
3. "n_♯ grows by ≈ 10¹⁰" uses a **stale n_H** (2e87); the reviewed value is **1.81e91**, and at HW's own B_0
   it is 1.0e97·c₊ ≈ n_T.

**The cheapest real gain, which session 5 dismisses as "not needed".** SH-att's **6561 → 2401 is free in one
line** (use sh(P) ⊇ N_1(π^r P)). And the session's own check B2, plus the reviewer's re-runs at M = 20/40/80
and an adversarial sampler (max excess 257 per Y-cube, depth-stable), **suggest the multiplicative factor is
removable altogether — which would put g²_CRC at 3.2e-93/c₊, ABOVE the recorded ceiling, and make session
5's headline "failure" vanish entirely.** Commissioned as HW session 6, Target 1.

**(E2^𝔉) has three undeclared deltas against node A's actual statements**, i.e. HW is asking node A for
strictly more than node A owes: (i) **allowance currency** — PLD gives the slice s_k(𝔥) (l.1856) or ‖S‖_sh
(l.1408), while (E2^𝔉) wants the **union form over the attached patch**, which is neither; (ii) PLD covers
**k ≥ 2 only** ((LCR)_0 OPEN, l.1905) while (E2^𝔉) carries a level-0 clause that is itself mis-levelled;
(iii) **F_< is a free unquantified symbol.** Also the route of record switches **TF-1 off**, reinstating the
node-A law mismatch TF-1 removed.

**A favourable narrowing of the session's own new pessimism.** §24.3's doubt that a good buffer cannot screen
(straddling plaquettes) **does not transfer**: LI-pw is *pointwise* while (E2^𝔉) is an *expectation*, and the
measure suppresses the offending configurations at cost e^{-c/g_j²}.

**Process.** §29's pre-statement is **VERIFIED byte-exact** (located by brute-force hash search: 3695 bytes
at offset 144433, md5 7830e9f0); all six [RHW4-fix] fixes really applied; **w5 fully reproduces — all 11
verdicts**, in the reviewer's own code on a different toolchain (Decimal-120, pure python, exact Fractions).
But **binding rule 2 is breached**: the w5 criteria contain b_n, b_D, c_att derived in the same session, and
A1/A4/A5's PASS bands are brackets drawn around §30.6's own hand values. Criteria-before-script is
NOT-VERIFIABLE (the worktree checkout normalised all mtimes). §29's promised check-(ii) negative control was
**never run** (max 2z² = 0.783). HW.md has **no "FOR OTHER FILES" section** despite raising demands on PLD
and RLARGE — a rule-8 breach.

**Verdict on (CRC-1): dissolved as a wall, NOT discharged.** It is CONDITIONAL on (E2^𝔉), which is strictly
stronger than what node A owes. **RLARGE's critical-path item 1 should be re-labelled from "(CRC-1), a
two-species cluster expansion" to "(E2^𝔉)".**

**Biggest live wall: the union-form allowance e^{c_A‖col Γ ∪ Y‖_sh} over the whole attached patch — a
differently-shaped statement nobody has written.**

**LEAD ACTIONS TAKEN.** (a) HW session 6 commissioned: apply the 11 fixes, take levers (a) and (b) on the
×6561, restate CRC-2T as an induction on constrained pairs, renegotiate (E2^𝔉) into a form node A can owe,
and open a FOR OTHER FILES section. (b) The (E2^𝔉) deltas and the real wall forwarded to the node-A worker
mid-run. (c) **Two reviews now converge on the allowance currency as the crux** — REVIEW_PLD_S5 found PLD
using a currency HW had struck, and REVIEW_HW_S5 finds HW demanding a third currency PLD never offered. That
is the HW/PLD interface defect, seen from both sides independently.

**Scoring T51-A:** 4 of 5 in. Three sessions' headlines narrowed or relabelled, one session's reported
verdicts reversed three times, zero headlines refuted outright. Pre-stated expectation **met**.

## BFT_B session 9 — the (H-inv+) attack (T51-E). LANDED, and it is the session's biggest advance.

Append-only discipline verified byte-for-byte: BFT_B.md l.1-3569 still exactly 409782 B (the session-8 final
size), BFT_B_LOG.md l.1-420 unchanged at 44498 B. §27 PRE-STATED was the first edit (12:27:05 UTC, growth
logged as 14775 B exactly, statements only). §28 records all nine [RBB8-fix] errata as dated entries naming
the lines they correct, including RS8-3's rename of lane B's GE-T to **Lemma ΓT-op** (the name clash with
lane A's refuted (GE-T) is gone).

**1. (Res-Hölder) = EP-F4 is CLOSED at m = 0 for the part that was open.** The gap left by [RBB6-fix RS6-1]
was the non-co-closed BCH₂ remainder V_l. The mechanism is the good kind — an identity, not an estimate:
when level-wise co-closedness is dropped, **d*ρ_l is not unknown**. It is *forced* to be the
level-(l+1)-root restriction of Σ_{l'≤l} d*j_{l'}, by root covariance (d*Q_l^T = ev^T d*) and the
injectivity of ev^T — and **composite co-closedness is exactly the consistency condition for that cascade**
(Lemma RT-cc, PROVEN-HERE). The resulting funnel source is then a plain level-l current with
‖h_l^T‖_{ℓ^∞→ℓ^∞} ≤ 1, supported on block-interior links (Lemma FT, PROVEN-HERE). Theorem RHT goes through
with funnel factor **K_f = 2d/(1 - L^{-(2+α)}) = 8.737** at d = 4, L = 3, α = ¼ (Theorem RHT-cc,
PROVEN-HERE). Corollary RHT-V is PROVEN as an implication of lane A's Lemma CD (i) + Proposition NC:
**N_res ≤ C_V η², k-, T- and level-uniform, for every gauge fixing**, since the residuals are exactly
composite-gauge invariant. Weighted: Theorem RHT_m-cc with c_w = 14 (crude), which **extends lane A's
LRL (b) at T ≥ 5 to composite-co-closed sources**. Scope stated plainly in §29.4: a critical-point
statement (as RHT already was), resting on Lemma CD (PROVEN in lane A *given (GI)*), with C_NC crude.

**2. (CO-0) and (CO-up) are usable by lane B verbatim — and the project's open list was STALE.**
(CO-0) = lane A's **Theorem W0**, CONFIRMED (REVIEW_BFT_A_S6 l.23, 151). (CO-up) = **Theorem GU**,
CONFIRMED (same review, l.24, 181). REVIEW_BFT_A_S4 l.37's "(CO-up) mostly bookkeeping … ARGUED" is
**superseded** — it predates Theorem GU. REVIEW_BFT_B_S5's "(CO-0), (CO-up) OPEN" is **stale**. And
**(SB) is no longer an input at all**: REVIEW_BFT_A_S5 l.373 records that Theorem CO-B removes it.
**Consequence: (H-inv+) at m = 0, trivial background, level-wise co-closed classes on 𝒞_glob is PROVEN as
an implication, with every input CONFIRMED by a lane review.** PROOF.md's BFT clause table (l.6695) is
**stale in three places** — lead to fix in the consolidation.
*Lead note: three items the project was carrying as open had already been discharged by lane reviews and
nobody had reconciled the lists. This is the cost of per-lane open lists with no cross-lane reconciliation,
and it is the same defect class as the HW/PLD currency mismatch.*

**3. The (NC-Γ) restatement under lead decision D1.** Two parts.
- **(NC-Γ)_cc:** for composite-co-closed sources, Lemma FG (iii) makes the response *be* the Setting-LIN
  critical point, so every gauge-invariant output is Γ-independent — **the spikes and tents cancel
  identically.** The **residual half** (both L^{k-1-j}‖r^c_j‖ and N_res) is **PROVEN unconditionally**; the
  **curvature half** is **CONDITIONAL** on one new named item, **(CO-fun)** = (CO-0) for the
  funnel-augmented J_0 (which §29.1 (d) proves is co-closed, with f_0 = n²dΔ_0^{-1}J_0). (CO-fun) is OPEN
  because the funnel pieces are co-closed only *collectively*, so Theorem W0 cannot take them one at a time.
- **The remainder: Proposition NCR, PROVEN-HERE and exact:**
  f_0^Γ(S)(p) = ⟨S, Y^p_*⟩ + ⟨D(S), λ^Γ_*(p)⟩. **The entire gauge-fixing dependence is the pairing of the
  source's composite divergence with the gauge transport function**, and lane A's Lemma RC root terms and
  Proposition TE tents are the root and tent parts of that one object. So the remainder bound factorises as
  ‖D(S)‖_1 · sup|λ^{Γ_E}_*| on supp D(S) — the first factor O(‖∇(𝔉_k∘exp)‖) by Lemma CD (zero at critical
  points, second order along the contraction), the second a new named OPEN item **(GT-sup)**.
  **(NC-Γ)_cc + (GT-sup) ⟹ lane A's original (NC-Γ) for Γ_E**, and the original fails *only* through
  (GT-sup). This is route (i)'s lemma in product form — the form in which it is checkable.

**4. BFT-5 now has a statement and a status.** **(BFT-5_E)** (§32.1) for composite-co-closed sources, with
clause (c) quarantining the slice dependence in Proposition NCR's exact bilinear term.
**Status: OPEN, inputs named** — (G♯_0-field) [OPEN, lane A], (R♯_ω) [stated, not proven, PROOF-owned],
(G♯-patch^Ω); clause (b) inherits (NC-Γ)_cc and **clause (c) is PROVEN**. The new content is a narrowing:
SF's Lemma G-pert needs the background X_c-small in one gauge, which BNA-F4 says no global gauge supplies —
but **Corollary CL-iv supplies exactly that on every frame, k- and T-uniformly**, so (G♯-patch) narrows to
gluing frame-local inverses with CL-iv's transition gauges. Lemma Rω-frame delivered as **ARGUED**
(explicitly not CONDITIONAL): the frame rewriting is not a new wall, costing P(C_1ε); the gap is that the
commutator-to-divergence-form step has no explicit constants.

**Not attempted:** (Mult-Y)/GAP 1 and the nonabelian (CovLift) items. Targets 1-4 used the session.

**Check bb9, with a disclosed FAIL — process handled correctly.** criteria 12:31:25 with an amendment adding
A7 at 12:34:06, both before any script. Exact Fraction arithmetic, no numpy/BLAS, no lock taken (rule 6
exempts exact arithmetic), nice 10, 1 thread, 6.1 s, 28 MB.
- **bb9.out: NOT ALL PASS — B3, B4 FAIL.** Cause found after the run: a **script bug** (the level-1 gradient
  applied Q_1^T twice), so Part B solved the wrong energy. **Output and script kept unaltered as the record.**
- **bb9b.out: ALL PASS** (A1-A7, B0-B7), same criteria, **no criterion retuned**, one expression changed.
  Verifies root covariance, d*Q^T = ev^T d*, the funnel split, |c(X,b)| ≤ 1 with max 1/3 and one block per
  link, the cascade support claim with its control, funnel non-vacuity, and at the exact 180×180 critical
  point ψ_0 = the root restriction of d*j_0, the funnel-corrected recursion, and d*J_0 = 0.
  Scope limits reported: d = 2, abelian, k = 2; at T = 1 the top charge vanishes so Part B does not exercise
  a nonzero funnel inside the ρ-recursion (pre-registered; A3/A7 at T = 2 carry that part).

**>>> THE BIGGEST OBSTRUCTION TO BFT-0/1/2 HAS MOVED.** It is no longer in the (H-inv+) + (Res-Hölder)
bundle — **that bundle is closed at m = 0 and the trivial background.** It is now **the nontrivial
background**: every lane-A input above (W0, GU, CO-0R, CO-upR, CO-B, LIN0) is proven *at the trivial
background only*, so BFT-0/1/2 turns on the background-covariant slice **(N1)** together with (CovLift)'s
non-residual g_Z components at θ > 0 (OPEN). Second: the off-critical-set curvature half, **(CO-fun)** +
**(GT-sup)**. Third: m > 0 via lane A's DX_m, DB_m (quoted OPEN), which BFT-3 at k ≥ 2 needs.

**Scoring T51-E:** the pre-stated failure mode **HI-F1 does NOT occur** — (Res-Hölder) did not fail in every
norm pair, and its closure was by an identity (the forced cascade) rather than by a better estimate, so it
is not the Π_ex tail of COMP-F1 in disguise. Target T51-E is PASS on (Res-Hölder), (CO-0), (CO-up), the
(NC-Γ) restatement and BFT-5's statement; FAIL on (Mult-Y) and (CovLift), not attempted.

## REVIEW_BFT_A_S8 (T51-A, 5 of 5 — T51-A COMPLETE). 586 lines, 18 findings, 9 binding fixes.

BFT_A.md still 351969 B; no git, no numeric lock, no floating-point job — the reviewer's new results are
exact rational arithmetic (scripts in the reviewer's scratch: revA8/rev8_exact.py, rev8_psi.py).

**>>> THE STAND-IN QUESTION, ANSWERED LOUDLY — AND THIS IS A CONSTRUCTIVE REVERSAL.**
**The refutation of (GE-T) does not need the stand-in at all, and the route §38.8 uses to it is WRONG.**
§38.8 l.3582-3585 routes the tent coefficient through "ψ_u(X) ≈ … is the level-0 spike a of §38.4
(measured a = -0.0022; ARGUED identification)". **That identification is not available:** ψ_u(X) =
(h^{0→k}u)(c_X) and sp_0 are different functionals, and ba8's own output separates them (at the non-level-k
root, S_C0 has sp_0 = 0 with φ_1 = -0.002619; CG has sp_0 = -0.0017 with φ_1 = -0.000713 — slope ≈ -1.1, a
factor-3.7 sensitivity **the session never reports**). Worse, *a* was measured at a level-k root in two
representatives that are **not S_E**, and lane B's **PROVEN** §16.2 Step 1 forces sp_0(Π_Ex; c_X) to be a
partition-of-unity remainder, O(n^-3), **not** *a*.

**But ψ_u carries no representative, so the reviewer computed it exactly.** For u := ⅛d*δ_p (p the
(0,1)-plaquette at c_X + (1,0,0,0)) — co-closed, admissible with R = 1 — lane B's §16.2 Step 0 gives
**λ^E_X(u) = 0 for every box containing supp u**, so Π_E u⃗ = u⃗ and **nothing can cancel the tent**.
Exactly: **φ₁ = -1/432, φ₂ = -17/104976, same sign, ratio 17/243, ψ_u = -65/26244 at k = 2.** Tent
ℓ¹ = (130/6561)·L^{3(k-l)} against (GE-T)'s C_GT·L^{-3l}: **(GE-T) is FALSE by ≍ L^{3k}**, modulo two
routine estimates. The same exact computation reproduces E3's zero-pattern exactly (0 at four symmetric
offsets, ±1/54 at the asymmetric ones) and the measured φ₂/φ₁ ≈ 6.9%.

**Verdict: lead decision D1 (one slice, S_E) is WELL FOUNDED — for the TENT reason, not the measured-spike
reason.** The spike half does rest on the stand-in; the transport is sound in substance but the file's
justification is one clause ("plus terms smooth at Z"). The reviewer **supplies the missing estimate**
(Σ_X dχ⁵_X = 0 plus d*a_X = 0 at interior sites ⇒ no point divergence in S_E), and REVIEW_BFT_B_S8 derived
the same thing independently. (PW-i) for Y^p itself stays ARGUED.
*Lead note: the reviewer found a better proof of the session's own refutation than the session had. This is
the second constructive reversal pattern in this project's history — the checker supplying the result rather
than only breaking it.*

**All three of the lead's primed checks came back clean.** No PROVEN item depends on TE's size or on FS;
PW-E is nowhere used as if it had content; nothing closes the factor k or (PW-ii).

**PW-cc CONFIRMED, and its uniformity in k and T holds.** m′ := m*′/3 is pinned *before* the estimate
(l.1471); S(m′) = coth⁴(m′/2) is a ℤ⁴ sum dominating every torus; G_D(m′) = e^{20m′}G_D♭ is k,T-uniform;
κ_± are standing parameters. Every exponent re-done. **This is the session's one unconditional theorem.**

**DF, RF, TE (identity), RC: CONFIRMED. PW-E: CONFIRMED as an implication**, with the correction that one of
its *other* inputs (EP-rec's c_r = 24) is itself ARGUED. **Proposition SR is now VACUOUS for S_E**, not
merely short of (PW-ii) — §40's PW-SR row misleads.

**Provenance CONFIRMED** (byte boundaries exact). But **the §36 disclosure pre-states the whole session-8
story, so F3/F4 carry no pre-registration weight** — the session says so, though §40 alone would not reveal
it. **ba8's verdicts match the pre-registered criteria exactly** (both re-derived: ρ = 8.0244 ≥ 4 and
0.2303 ≥ 0.1644 ⇒ F3; 0 > 0.11515 false ⇒ not F6). Three disclosure fixes: undisclosed "F6-test YES"
print-floor lines at three offsets; "ε = 0 exactly" unsupported by a 6-decimal print; E4 uninformative and
misplaced. One undisclosed plan deviation (E1b run at (3,1), pre-registered (2,2)).

**The biggest live wall, now sharpened into a DICHOTOMY by the exact ratio 17/243.** A representative map
top-anchored for Y^p *and* 𝔐^∇-compatible for configurations. The dichotomy: **the full σ correction costs
a forbidden L^{2l(Z)}η point gradient, while §38.8's cheap "move only φ₁" escape leaves ≈ 7.5% of the spike,
still level- and k-independent, so (PW-i) still fails. Every finite funnel truncation leaves a
level-independent remainder.** Good news and the lever: **the level-k tents CAN be removed by a gauge smooth
on scale n (cost ≍ η, allowed); the intermediate spikes cannot.**

**Highest-value missing object, per this review: "lead decision D1's remainder bound for composite-co-closed
(NC-Γ), which is written nowhere."**
**>>> IT WAS WRITTEN CONCURRENTLY — but it is NOT the bound the review asked for.** BFT_B session 9 §31's
**Proposition NCR** is an exact *identity* in product form. **[CORRECTED by REVIEW_BFT_B_S9_S10, which marks
§36.5 (v)'s "REVIEW_BFT_A_S8's request is already answered" WRONG: an identity is not a bound. The lead
repeated that claim; it is withdrawn.]** The reviewer could not see it (the two ran in parallel). So (NC-Γ)'s
remainder IS written, and what remains is only its two factors — **(CO-fun)** and **(GT-sup)** — which are
now BFT_B session 10's entire scope, commissioned with the review's exact spike data forwarded to it.

---

# T51-A SCORED: COMPLETE. All five outstanding hostile reviews written.

**Headline survival:** CRC-2T survives; EPS-T survives with one added hypothesis; FLOW S13 survives;
lane A's refutation survives on *better* grounds than it claimed; lane B S8 was already confirmed.
**No headline was refuted outright.** Three were narrowed, one session's reported verdicts were reversed
three times, one session's framing was relabelled (bestiary, not cluster expansion), and one review supplied
a proof the session lacked. The pre-stated expectation (≥ 2 of 5 narrow, demote or refute) is **met**.

**What the five reviews changed about the project's state, collectively:**
1. **The constants crisis was false.** The smallness condition is satisfiable; the binding ceiling has ~55
   orders of slack; HANDOFF's resume step 3 is withdrawn; the whole tightening is one ×6561 geometric factor
   that is probably removable.
2. **Three "open" items were already closed** by lane reviews nobody had reconciled ((CO-0), (CO-up), (SB)).
3. **Two reviews independently converged on the HW/PLD allowance currency** as the real interface defect.
4. **The target's adequacy problem largely dissolved** (SQ proved θ_w = 2 natively), and was replaced by two
   concrete constants: (CONST-T) and D3's compounding factor.
5. **Process debt found: three rule breaches** (HW's rule-2 criteria contamination and missing FOR OTHER
   FILES; FLOW's 1.03 GB cap breach and an unlogged threshold relaxation; PLD's immaterial rule-2
   tautology), plus two criteria files that were themselves wrong (SQ's q5, FLOW's B4 — the latter fixing a
   FAIL at pre-registration).

## PLD session 6 — the node-A walls (T51-D). LANDED.

PLD.md l.1-1966 verified byte-identical (md5 35b33c8f…); §18.0 PRE-STATED was the first edit (12:28:16 UTC,
7793 bytes). §18.0-§18.12. **Counted PROVEN-HERE (unreviewed): 2.** **0 OPEN items closed.**
Check p6: **SUMMARY "FAIL: F2"**, all else PASS including all three negative controls. F2 is a script defect
(a finite partial sum against the criterion's infinite series); reported as a FAIL, **nothing re-run or
edited**, hand arithmetic labelled post-hoc, F2 not counted as passed, and no §18 statement depends on it.
Lock deliberately not taken (exact `fractions`/`math` only, no BLAS); justified in checks/p6_time.txt.

**(J-NS^cd): still OPEN. Induction on levels does NOT close it** (Proposition CHAIN, §18.5). Three
independent reasons:
1. **No base case.** NA-PRICE^E is proven for k ≥ 2, so CD (b)'s induction bottoms out exactly where the
   theorem cannot reach.
2. **No contraction.** The two pointwise certificates the event gives — F^col_Q(U_{k-1}) ≥ a_bad/4 (CW at
   level k) and F^col_x(U_{k-2}) ≥ a_bad/4 (CW at k-1) — are **nested, not additive**: TE (i)/(iii) make the
   second a sub-sum of the tower the first already bounds. So they certify a_bad/4, not a_bad/2, and η = 1
   is what the certificates *give*, not a crude bound. The one genuinely additive currency, DIL-L (ii)'s
   kernel energy, is **identically zero on centre defects by definition**.
3. Even the coherent sub-case, which carries a huge certificate (F^col_Q ≥ L^{4m}a_bad, price exponent
   4.86e10 against 324/level), **cannot cash it**: cashing needs a moment on a defect-carrying column.

**>>> The lead's pre-stated failure mode NA-F1 is HALF REFUTED, and I record that against myself.** I
pre-stated "the level induction for (J-NS^cd) **compounds**, so the energy grading is not closed by
induction alone." The conclusion holds; **the mechanism I guessed is wrong.** Compounding is *not* a reason:
the worker **proved** the union-form excess line ‖x(S)‖_sh ≤ ‖S‖_sh + (1 + Δ_sh)|S| that REVIEW_PLD_S5's
B2(b) left open, so **Corollary LAW (c) is right in the union currency**. The real obstruction is the
*nesting* of the certificates, which is a different and more interesting failure.

**Branch 2 (the route REVIEW_PLD_S4 left unattempted) WAS attempted. Finding (EG-cur):** (EG) is **vacuous**
in the kernel-energy currency and **non-empty** in the curvature-energy currency. The single missing
ingredient is the identification of the S4′ kernel mode with a local curvature minimiser, named
**(EG-link)**, OPEN.

**(E2^𝔉): not supplied by session 5 (confirming REVIEW_PLD_S5 independently) — but its law-conversion
obstruction is now CLOSED.**
- **Sharpening of the review: (C_S) is NOT the obstruction.** Only its clause S ∩ 𝒰_k = ∅ is used by GEO
  (i),(iii),(iv), FT^far and COL-DEC, and **Proposition FAR** proves HW's far Y satisfies it automatically.
  **The obstruction is GEO (ii) alone — about the *weight*, not the *set*.**
- **Lemma BUF:** one extra R-free ring gives L_w ∩ X_j(𝒜) = ∅ via LI^U-0′, so **FT^far and COL-DEC both
  apply to HW's own weight on far sets.** CRC-2T can buy the ring; exact cost **×82 on b_n, b_D, n_♯ and
  ÷82.0000 on g²_CRC** (p6 B1/B2). The pre-stated (NP-F8) is MET with the minimal enlargement named *and
  priced*. *Lead: forwarded to HW session 6, since ÷82 lands on its lever — on the pre-ring figures, full
  removal of the ×6561 gives ~3.2e-93/c₊, and ÷82 gives ~3.9e-95/c₊, still ~2.5× below the recorded 1e-94
  ceiling. So "the headline failure vanishes" does not survive the ring purchase against that ceiling. It
  does not matter, because the binding ceiling has ~55 orders of slack, but it must be reported honestly.*

**One lemma for both — YES, with the honest qualifier.** **(CEM^{COL})_k:**
E_ν[Π_{Q∈A∖A′} e^{θY^f_Q}·F] ≤ c_cem^{|A∖A′|}E_ν[F] on the B1-compliant law class 𝔏^buf_k. It is
**(SF-cap) with the factor 1_{G_Q} deleted** — single-level, a moment not a probability, defect-tolerant,
allowance (P0). **Proposition ONE** (proven) derives from it + (CLS-min): (SF-cap)^{COL}, (J-NS^cd),
NA-PRICE^E (i), the new NA-PRICE^{E+}, and (E2^𝔉′) (Corollary E2-RED). **Qualifier recorded prominently by
the worker: it is strictly STRONGER than the pair it replaces, so this is a CONSOLIDATION, not a
discharge** — (J-NS^cd) and NA-PRICE^E stand as session 5 left them. *This is the right label and the
worker volunteered it.*

**Proposition PATCH (proven) — the statement REVIEW_HW_S5 called "a differently-shaped statement nobody has
written", now written, with a structural explanation of WHY nobody had.** Monotonicity of ‖·‖_sh means any
set node A prices is ⊂ the patch, so **HW's union form follows free**; the slice is **incomparable** to both
consumers; per-cube depth is the thing that must never appear; and the finding: **NA-PRICE generates no
allowance at all, it only TRANSMITS the hypothesis's — so the patch allowance is a CLAUSE OF THE
HYPOTHESIS.** That is why no §16-§17 statement has that shape. What it would take: the moment with a
per-cube constant and no shadow sum. *Lead: this is the root diagnosis of the HW/PLD interface defect that
two reviews found from opposite sides.*

**NA-PRICE^{E+} (proven implication ⇐ (CLS-min) + (CEM^{COL})) is a large simplification of the pricing:**
a_A = min{λκε_1²/256, 6θa_bad} ≥ θa_bad **unconditionally**, c_A = 0, F-conditioned, **k ≥ 1**, **no MD, no
81, no recursion, 2^{|S|} instead of 4^{|S|}**. K12 then reads θ ↑ 1/24 with a_A = a_bad/4 (p6 C2).
If (J-NS^cd) is discharged, NA-PRICE^E becomes (SDP)^{A,far} in HW §24.3's shape at k ≥ 2 — **but still not
(E2^𝔉)**: four further items are needed (far-set class, allowance form, joint CAP-dec combination, levels 1
and 0), of which §18 supplies three and a half.

**Seven interface mismatches M-1…M-7 reported** (allowance, set class, levels, weight class, RLARGE's stale
quantifiers, form, F_<). **And a correction to REVIEW_HW_S5: the TF-1 switch-off is NOT a node-A
regression** — PLD §17.2 is already written for the finer-first law. *Lead: two lanes now disagree on this;
recorded, not adjudicated here.*

**c_lcr verdict.** The **value** is not load-bearing (it enters only as log c_lcr against b_n ≈ 2.04e10·c₊;
log c_lcr = 1e9 shifts g²_CRC by 4.9%, 1e11 would bind — p6 B3/B3n). **Existence and uniformity are.** No
statement labelled PROVEN rests on the value (independent audit, agreeing with REVIEW_PLD_S5's S5-25). But
**no certificate for (LCR) as written is possible: the weight-class uniformity it asserts is expected
false.** A certificate target is stated in five clauses.
**>>> Flagged as bigger than any c_lcr effect, and it is PROOF-owned (mine):** §16.8's λ_min = 3.17e-3
against REVIEW_PLD_S3's binding L0-1 (6.6e-10). **If L0-1 governs, a_ret falls ×4.80e6** (p6 D2). A question
for SF/PROOF; route (ii) defuses it. *Carried into the consolidation.*

**Single biggest remaining obstruction: (CEM-2).** A decoupling estimate, under the past law of a pattern in
𝔉_𝔥, between HW's buffered far weight and F^col_Q(U_{k-1}), across one R-free ring. **It is not obtainable
from the buffer-good event alone** — the event bounds curvature by ε_1 while a g-independent constant needs
≈ g_K, and those differ by **4.489e15** (p6 A2, with negative control A3 showing it is the gap and not a
formula artefact). **The mechanism must be the weight's *typicality*, not the event** — the same direction
as REVIEW_HW_S5's narrowing (LI-pw is pointwise, (E2^𝔉) is an expectation). Everything else reduces to
**(CEM-1)** = (LCR) + the main-term reduction off G_Q + u-uniformity of the activity bounds on
[(1-λ_f)u, u] — three named single-level statements.

**Scoring T51-D:** PASS on reporting a status for both walls and on the one-lemma question (answered yes,
with the correct "consolidation not discharge" label). NA-F1 half-refuted as above. 0 OPEN items closed —
the worker says so plainly, which is the behaviour the anti-inflation clause asked for.

## NORMS.md — the attack on the constant-compounding wall (T51-C). LANDED. 918 lines.
## This is the session's biggest result, and it corrects the lead on two points.

### Part 1: the per-level route is PROVABLY dead, by a no-go, not a gap

In the field-strength norm, Z_col·Z_row² = 1266.87 is replaced by
**A_per = 𝔠_vol·𝔠_ax²·L^{d-4}·(L²K̄) ∈ [1.08, 1.38]·𝔠** — a gain of **920-1171 per level** (check n1-E).
**But A_per < 1 is a NO-GO, and not because of a bad norm:**
- **Z_col = 156 is the column mass of 𝒦 = L^d·K̄ ≈ 9.7 plus (2/(d-1))K_ρ ≈ 1.5** (Proposition N1-8, an exact
  mass-balance identity). **>>> PROOF.md's own diagnosis is WRONG:** "Z_col ≥ the L^{d-1} = 27 crossing
  links of one coarse link times the spread" (PROOF.md l.6211-6213) misidentifies the count. The right count
  is L^d·K̄, and **the crossing-link count vanishes once the leg is measured through d₁X.** Lead to correct
  in the consolidation.
- **Z_row = 2.849 → 𝔠_ax/L** (smooth value 1/L = 0.333, factor 8.55). **Z_row ≥ 1 is a slice artefact:**
  pure-gauge coarse directions map to the concentrated lift J. **Lemma N1-2 (proved here)** licenses a
  spread representative — E3 and TOWER-VAR (d) hold for *any* admissible gauge reparametrisation of the
  critical family.
- The residue is **L²K̄ ≥ 1**, with equality only in the smooth limit (K_p^♯ → 1/L² *from below*).
  **The d = 4 cubic vertex is marginal, so A ≥ 1 in EVERY scale-covariant norm** — and the
  weight-invariance half of that is **PROVEN** (check n1-D PASS at six (θ_w, θ_A) pairs): **any A < 1 bought
  with non-canonical weights is cancelled exactly by the initial-condition mismatch.**
  Pre-stated failure mode **N-F2 occurs for every per-level route.**

*Lead reading: this upgrades decision D2 from a judgement to a theorem. The per-level route was labelled GAP;
it is now a no-go. No future session should attempt to repair it in any norm.*

### Part 2: the composite route — A_soft = 1/3 < 1. THE DELIVERABLE.

By **TOWER-VAR (d)** the level-k third derivative is a **single pullback** by the chain-minimiser map, so
there is **no per-level recursion and no per-level covariance — the anti-circularity constraint is satisfied
by construction**, not by argument. Three exponents add up: (d-2)k, -k, -k → **(d-4)k = 0** for the level-0
Wilson vertex (marginal, incurred **once**), and (n+d-1), -n, -n → **(d-1)-n** for the level-j soft vertex.
So **A_soft = 1/L = 1/3 < 1**, and **N3(D³E_k^br(1)) ≤ 𝔚 + 13.5·𝔖 uniformly in k** (Theorem N1-15).
The contraction comes from the residual decaying by L^{-(d-1)} per level while the curvature decays by
L^{-2}: **margin exactly one power of L.**

**(H-C)'s C_♭ clause: DISCHARGED at the trivial background, CONDITIONAL on (N-Q) and (N-loc).**
PROVEN-HERE: Lemmas N1-1, N1-2, **N1-4 (intermediate-level curvature decay θ_w = 2 on the torus,
reproducing SQ's REG-lin (d) constant C_0 + 4κ̂L²/(L²-1) by an independent route — an independent
cross-lane confirmation)**, N1-5/6/7, N1-8/9, N1-13 (i).
**Scope, stated plainly by the worker:** the *other* (H-C) clauses (𝔠_∞, A_in, A_out, c_K, 1/m₁, Z-tails)
are untouched, and the Lipschitz-on-the-class statement that BR1 and δ_Sch actually consume needs
**(N-bg)**, OPEN.

**Pre-stated failure modes: NORM-F1 does NOT occur** (conversion cost is 2(d-1) = 6, no L^{d-1}).
**NORM-F2 does NOT occur in §N6** — every response used is the response to level-k *data*, i.e. to d_k X,
which is **exact, not merely closed**; the Bianchi defect, Z and its tails return only in (N-bg), which is
where NORM-F2 must be re-examined. Same reason COMP-F1 / Π_ex does not arise. **NORM-F3 (circularity) does
not occur, by construction.**

### Part 3: >>> TWO CORRECTIONS TO THE LEAD, both recorded against me

1. **My relaxation of θ_w was wrong, and backwards.** I told this worker (mid-run) that since SQ had proven
   θ_w = 2 natively, it need not chase large θ_w and that A < 1 on any (0, θ̄] would serve. The worker's
   answer: **A = L^{d - θ_w^r - 2θ_A} with θ_A = min(1, θ_w^c - 1), so A < 1 ⟺ θ_w^r + 2θ_A > d. This route
   needs the MAXIMAL θ_w^c = 2 and does not get easier at small θ_w.** My guidance would have pointed it away
   from the only working parameter choice. It ignored the relaxation and delivered (θ_w^c, θ_w^r, θ_A) =
   (2, 3, 1).
2. **My framing of D3 was wrong on magnitudes.** I wrote that the 1267-per-level factor "is the sole origin
   of every astronomical smallness condition". The worker: **"only partly right — it is the origin of the
   depth-dependence."** C_θ is dominated by 288·A_in·coth⁴(m₁/2)·ℓ_θ, with 288𝔠_∞³C_♭ ≈ 9.0e9·C_♭ some
   **10³² below it**. So **g_K² = 4.9e-97/c₊ is UNCHANGED and g_0 still has to be lowered.** What
   1267-per-level threatened was the *existence* of a k-independent ε_BG, not the magnitudes. Corollary
   SF-thr-k already makes ε₁ k-independent *given* (BG-unif).
   *Consequence for the project: the magnitude problem and the uniformity problem are DIFFERENT problems with
   different causes. D3 conflated them. The uniformity problem is now solved at the trivial background
   (Part 2); the magnitude problem is coth⁴(m₁/2)-dominated and untouched. The consolidation must separate
   them.*

### Part 4: BFT-1 must be stated as a PAIR of weights — a new target defect

**With a single common θ_w there is NO solution in (0, 2].** A < 1 requires θ_w^r + 2θ_A > d = 4, met by
(curvature 2, residual 3). So **BFT-1 as stated — one existential θ_w ∈ (0, 2] — cannot support this route,
and must be restated with a weight PAIR (curvature θ_w^c = 2, residual θ_w^r = d - 1 = 3)**, merging with
REVIEW_SQ_S2's item (2).
*This REVIVES a form of INTEGRATION_AUDIT's A1, which I had withdrawn. Withdrawn for SQ's reason
(SQ proved θ_w = 2 natively); reinstated for a different and stronger reason (one weight is not enough for
anybody). Audit to be updated.*

**BFT-4:** the worker's route is an **ALTERNATIVE** to BFT-4 for the C_♭ clause at third order, **avoiding
(CovLift), (Mult-Y), (Pair-loc) and (I-id) entirely**, and a **tool** (the n = 3 instance) inside it
otherwise. *That is a large simplification of the BFT-4 route if it holds.*

### Part 5: the single remaining obstruction, and the cheap check that decides it

**(N-Q): ‖Q^j‖_{∞→∞} ≤ 𝔮₀·L^j with 𝔮₀ bounded in j** — whether the S4′ funnel (axial) legs accumulate in
the *composite* transport. **It is immediate with 𝔮₀ = 1 if Setting SC's Q is the straight average**
(‖Q_str^j‖ = L^j exactly). **The files are ambiguous:** J-str writes Q^T = Q_str^T - h^T d*, while SQ's
SHIFT writes "Q^m is the straight average". Crude p_L^j is insufficient and costs (11/3)² ≈ 13.4 per level.
Three-case reading in [N1-corr 1]: **bounded 𝔮₀ → uniform; polynomial → C_♭ ≲ k²; crude → 13.4/level.**
The bypass is the **multi-scale axial gauge** already named OPEN under (CL-1), which would also give (N-loc).

**The worker names the cheapest decisive check in the project: compute max_c Σ_b |Q^j(c,b)| for j = 1, 2, 3
at L = 3, d = 4 for Setting SC's actual Q, against 3, 9, 27 (bounded) versus 11, 121, 1331 (crude). Exact
rational arithmetic, no lock, seconds.** *Lead: commissioned immediately as NQ_CHECK.md.*

**Disclosed labelling defect (the worker's own):** check n1-C's criterion and script hard-code the residual
exponent as 3, so their d-general formula (d-5)n+3 is wrong off d = 4; the correct exponent is (d-1)-n. The
d = 4 verdict the criterion covers is unaffected, and §N6/§N7 use the correct form.

**Spin-off, ARGUED only:** the same divergence-form cure should take CURV-F2′/F2″'s 4𝔠_∞ ≈ 1.26e3 step to
O(1), **making all three failure modes one artefact.**

**Scoring T51-C: PASS.** A stated, A derived in both routes, the θ_w-range delivered, three of four
pre-stated failure modes correctly adjudicated as non-occurring, and the fourth (N-F2) shown to occur for
*every* per-level route — a sharper outcome than the target asked for. The anti-inflation clause is honoured:
0 main-path OPEN items are claimed closed, and (H-C)'s C_♭ clause is labelled CONDITIONAL on two named
inputs, not PROVEN.

## HW session 6 — the ×6561 lever and the interface repair. LANDED.

Append-only verified: the first 178489 bytes of HW.md still hash to session 5's closing md5 (prefix md5
1f0a6b37… re-verified); 178489 → 254211 bytes. §34-§41. All 11 [RHW5-fix] fixes applied as errata in §38,
each naming the line it corrects. **Tally 9 → 10.**

### Target 1: the lever. Beaten on one side, REFUTED on the other.

- **Lever (a) verified and then beaten.** The reviewer's free gain was 6561 → 2401. **The real constant is
  81** (**Lemma COV**): a radius-3 neighbourhood is a *union of 3⁴ translates* of the radius-1 one, so the
  attached cluster's shadow is covered by 81 translates of a set already counted in ‖P‖_sh, instead of being
  charged a volume ratio 7⁴ or 9⁴. **×81 off 6561 — ×29.6 beyond what the review offered.**
- **A second, independent gain. Lemma SH-2:** Σ^m(X) ⊆ N_2(π^m(X)), sharpening HIST's H-geo (i) from radius
  3 to **radius 2**, and **radius 2 is optimal** (radius 1 fails, 9076 witnesses). Hence
  2401/38416/38417 → **625/10000/10001**, and c_att(8) 1229313 → **320001**. A further ×3.84.
- **>>> Lever (b) is REFUTED, not proven (Proposition SH-neg, PROVEN).** At the all-ones base-3 position,
  P = {z}, Y = {z + 8e₁}: the excess is **exactly 27M + 55 over M levels with |Y| = 1**, so **no
  depth-independent additive constant exists**; the minimum multiplicative constant is ≥ 4/3 (≥ 5.714 on
  samples). The lemma REVIEW_HW_S5 named as the missing ingredient —
  "π^r(Y) ⊂ N_1(π^r(P)) ⇒ Σ^{r+c}(P∪Y) = Σ^{r+c}(P)" — **is false there**: the projections stay at distance
  1 for ever. **The reviewer's empirical depth-stability was an artefact:** check B2 and the re-runs
  randomised *position* and were adversarial only in *direction*.
  *Lead note: this is the fourth reversal of the session and the first in which a LANE refutes a REVIEWER's
  constructive suggestion, with a proof and an explicit diagnosis of why the numerics misled. The review's
  "the multiplicative factor is probably removable" was the single most optimistic claim in the five
  reviews, and it is now dead.*
- **Net: ×311.1 on g²_CRC, ÷311.2 on n_♯, ÷81 on c_f**, at any ring value.
- **The ring, folded in and made CHEAPER than node A priced it. Lemma RING: ×17, not ×82** — sh_r(X) is
  *already* N₁-thickened, so N₁ of it is a union of 2⁴ translates, not 3⁴ (w6 G6: 0 violations, observed
  max 2.783). HW bought node A's extra R-free ring in step (4) and confirmed PLD §18.12 request 1 (nothing
  else in CRC-2T reads R″). *Lead: two lanes now give different prices for the same ring, ×17 against ×82.
  HW's has a proof and a check. Recorded for the next review, not adjudicated here.*
- **g²_CRC, reported honestly:** **1.52362e-94/c₊ without the ring (ABOVE 1e-94 by ×1.52)**;
  **8.96376e-96/c₊ with the ×17 ring (BELOW 1e-94 by ×11.16)**; 1.85835e-96 at PLD's ×82.
  n_♯: 9.99e96 → **5.46e95**. **"The headline failure vanishes" does NOT survive the ring purchase** —
  stated plainly in §35.7 (i); even the unattainable additive form would give ≈ 3.9e-95 post-ring, still
  below 1e-94. *The lead's forwarded arithmetic was right in direction and the lane confirmed it rather than
  quoting the flattering pre-ring number.*
- **Pre-stated failure mode (W-F3) materialised.** With HIST's 38417/38416 left alone, REL-boot's r ≤ ½ and
  HIST-sum's condition become binding at **2.33e-96** (gain only ×4.77); the full ×311 is **CONDITIONAL on
  HIST adopting Corollary H-geo′** (request in §41, proof supplied). REVIEW_HW_S5's S5-12 four-way
  coincidence survives only in that variant (spread 1.0001 against 3.8415).
- **Not a crisis.** Slack against DX′ is **×3.59e56**. **HANDOFF's "lower g_0 / recheck the SF thresholds"
  is WITHDRAWN** (§41 item 1) — now withdrawn independently by two lanes.

### Target 2: Theorem CRC-2T′ — restated, not weakened
An **induction on the finite integer N(R) = |S_R|**, with exact telescoping, proven step containment and
event algebra, (S1) the standard Δ²z ≤ ½ criterion, and the closing condition a fixed inequality (c_U := 1
on input). **Gas framing dropped; §29 Target V2 (a) recorded NOT DELIVERED.** Off-route consumers named
(RLARGE K8, EXISTENCE).

### Target 3: >>> THE HW/PLD INTERFACE IS NOW REPAIRED
**(E2^𝔉′)'s allowance is restated as PLD Proposition PATCH's requirement** — *the moment carries at most a
per-cube constant and no shadow sum* — with the union/patch form derived by monotonicity, **so it is no
longer a request**. Slice agreed incomparable; per-cube depth never asked. **F_< universally quantified**
over bounded functions of U_{<k₀}. The mis-levelled level-0 clause is replaced by **(0a)** Γ at level 0 with
Y = ∅ **or (0b)** Γ at level 1 with Y at level 0, **both OPEN on both sides** — the largest residual after
the moment, since TEL-f needs every level. Seven deltas tabulated (D1-D7); **M-1…M-7 answered by number**
in §41. **TF-2: both positions recorded and not propagated — node A is right** (PLD §17.2's law already
carries the finer spectators); flagged for the lead. §24.3's straddling-plaquette doubt narrowed per S5-17;
the real residual is the no-volume-cost conditioning = **node A's (CEM-2)**, a decoupling under the measure.
*Lead: the defect that two reviews found from opposite sides, and that node A diagnosed at root (the patch
allowance is a clause of the hypothesis, not a theorem), is closed in one session by the two lanes agreeing
on PATCH's form. This is the clearest win of the parallel setup.*

### Target 4: process debt discharged
Session 5's **rule-2 breach recorded** (b_n, b_D, c_att in the w5 criteria; A1/A4/A5 are reproduction
checks). **w6's criteria contain no session-6 constant**, every criterion is labelled PRE-REGISTERED or
CONFIRMATORY, and the criteria md5 is in HW_LOG as the reviewer asked. **§29's never-run check-(ii) control
was RUN** (w6 N, PASS: above threshold the bound is vacuous while the exact ratio stays finite — with the
limitation stated, that it tests the bound and not the model). Stale n_H corrected (1.81e91 reviewed; at
HW's own B_0 ≈ n_T; **on session-6 constants n_H > n_T, so (T) adds nothing to H8′**). **§41 FOR OTHER FILES
added — the rule-8 breach repaired.**
**Negative results reported as such:** lever (b) refuted; the 1e-94 breach persists (×11.2); w6 criterion G5
came out identically uninformative and is **reported as a defective criterion, not as evidence**.

**Biggest remaining obstruction in scope: none that is HW's.** The single live wall is one node-A statement
— the moment under the exactly-converted law, with a per-cube constant and no shadow sum — plus its level-0
case. *So lane H is now clear and the whole chain waits on node A's (CEM-1)/(CEM-2) and the level-0 clause.*

## NQ_CHECK.md — (N-Q) decided. PROVEN. Theorem N1-15 now waits on ONE input.

**The "conflict" in the files was not a conflict, and both statements are correct about different objects.**
Setting SC's Q is **Q_root, the full S4′ order-averaged root map** — *not* the straight average: PROOF.md
l.2060, RTARGET.md l.414 and SQ.md l.15 all say so in the definition. **J-str** (LINEAR_PACKAGE l.166-171,
PROOF.md l.2093) is about Q_root: Q = Q_str - d∘h exactly, so Q^T = Q_str^T **only on co-closed forms**.
**SQ's SHIFT** parenthesis is SQ's *declared convention*, not a claim about Q_root: SQ.md l.655 states
"Q := Q_str (§0.4)", and SQ §0.4 l.352-357 **proves** that substitution legitimate for what SQ measures.
And the quantity SHIFT bounds cannot see the difference: **d∘Q_root^{(m)} = d∘Q_str^{(L^m)} exactly**
(PROOF.md l.2545; SQ.md l.411). One object, no duplicated reading.
*Load-bearing nuance the worker flagged:* SQ §0.4's substitution is a **gauge shift**, so it moves the
*potentials* — which is exactly what Lemma N1-11 bounds, and why (N-Q) was a real question: 𝔮_0 > 1 measures
precisely the accumulated funnel gauge.

**Exact values (COMPUTED, exact; gates G1-G5 all PASS).** max_c Σ_b |Q^j(c,b)| at d = 4, L = 3 on ℤ⁴
(which dominates every torus):

| j | exact | decimal | L^j | p_L^j | ratio to L^j |
|---|---|---|---|---|---|
| 1 | **205/27** | 7.592593 | 3 | 11 | 2.530864 |
| 2 | **2021/81** | 24.950617 | 9 | 121 | 2.772291 |
| 3 | **6115/81** | 75.493827 | 27 | 1331 | 2.796068 |

Increments 0.241427 → 0.023777, shrinking ×10 per level. 25.7 s, 856 MB, single thread, exact integers over
1944^j, no lock. G1 made c8(f)'s 2e-16 slice identity **entrywise exact**; G4 confirmed ‖Q_str^j‖ = L^j
exactly with non-negative entries.

**Case 1 holds and it is PROVEN for all j. Theorem NQ-1 (PROVEN-HERE):**
‖Q^j‖_{∞→∞} ≤ L^j + (d(L²-1)/(2L))·(L^j-1)/(L-1) ≤ **𝔮_0 L^j with 𝔮_0 = 1 + d(L+1)/(2L)**, uniformly in j,
on ℤ^d and every torus. **At d = 4, L = 3: 𝔮_0 = 11/3.** It uses only two PROVEN imports (the slice identity
and root covariance Q∘d = d∘ev) via the exact telescoping
Q^{(j)} = Q_str^{(j)} - d_j Σ_{i<j} ev^{(j-1-i)} h Q_str^{(i)}, then ‖Q_str^{(i)}‖ = L^i exactly, ‖ev‖ = 1,
‖h‖ ≤ d(L²-1)/(4L) = 8/3, ‖d∘G‖ ≤ 2‖G‖. The proven bound dominates all three computed values
(8.33/30.33/96.33 against 7.59/24.95/75.49) — the analytic and exact routes cross-check. A post-hoc run
verified the telescoping identity entrywise, 0 differing entries.

**>>> It also refutes NORMS.md's own pessimistic sub-estimate.** NORMS.md's named hole ("h applied to a pure
gauge") and its polynomial estimate 𝔮_0 ≤ 1 + 2d‖h‖j/L are **artefacts of expanding with the block mean M**,
which is self-referential (h^{(m+1)} = Mh^{(m)} + hQ^{(m)}); **the ev form never applies h to a pure gauge
and is j-independent.**

**Scope, honestly:** abelian / linearised — exactly Setting SC's, (N-Q)'s and Lemma N1-11's scope and no
further. L3g(a)-slice says there is no nonlinear SU(N) analogue of the identity, so **this does nothing for
(N-bg)**.

**Consequences:** (N-Q) ARGUED → **PROVEN**. Lemma N1-11 **PROVEN-HERE** with 𝔮_0 = 11/3 in 𝔠_P.
**Theorem N1-15 is CONDITIONAL ON (N-loc) ALONE**, conclusion unchanged (A_soft = 1/3,
N3(D³E_k^br(1)) ≤ 𝔚 + 13.5·𝔖), now uniform in k with no depth-dependence entering through the transport.
No smallness condition, ε_1 or g_K² changes.
**(N-loc) — the exponential locality of the gauge-variant representative, i.e. the multi-scale axial gauge
already named as (CL-1)'s open half — is now the single named input of Theorem N1-15.**

## CONST_T.md — (CONST-T) decided. The answer is "not at q = 8, yes at q ≈ 30".

Everything after the energy inequality (★) is expanded with explicit constants, giving the closed formula
(§6.1): **C_T = √6·F·B(4a)·[ ½(36·C_1·C_V·486)^a + ½(A_cγ_c)² + 288·C_1·Q ], a = q/(q-4).**

- **At q = 8 — the value SQ.md fixes (l.1621) — C_T ≥ 1.27e14, i.e. OVER the 1e13 threshold, for every
  C_1·C_V ≥ 1**, and C_1, C_V ≥ 1 are *forced* (each multiplies a bracket of nonnegative terms). Best
  estimate **5e20**, honest interval **[1.3e14, 3.2e23]**. A **PROVEN conditional negative** about this
  route's output — explicitly *not* a lower bound on the optimal constant in EPS-T's conclusion.
- **At q ≈ 30-100: C_T ≈ 1.2e12, interval [6e10, 3.3e13] — UNDER 1e13** across all but the worst corner.

**>>> The fix is a free parameter nobody had looked at, and the worker's own prediction about it was
backwards.** q is a free parameter of EPS-T that the lane happened to fix at 8, and **q = 8 is the WORST
admissible choice**: the Moser absorption exponent is a = q/(q-4), so q = 8 gives a = 2 — a full squaring of
the one-step constant. Raising q drives a → 1. **Compatibility checked clause by clause:** q > 4 ✓;
scale-invariance exact for every q (the identity (-2 + 4/σ)·σ/(σ-2) = -2) ✓; EPS-0b-avg holds for every q
with θ_G ∝ 1/q, which has ~25 decades of headroom above ε_1 ✓; and **C_T′ falls from 22.63·C_T to 16·C_T, so
the ceiling itself rises to ~1.7e13** ✓. Two structural facts make it clean: **χ = 2 is forced** (lattice
d = 4 Sobolev) and **A_sγ_s = 36·C_1·C_V·|N_1| is exactly independent of q** (the neighbour-multiplicity
exponents cancel). So q touches only a and B(4a).
**q_min against C_1·C_V: 9 at 1, 16 at 100, 31 at 2000, 132 at 1e4, unreachable at 5e4.**

**Smaller levers, all priced and none sufficient at q = 8:** radius schedule 23× (the written r_i spends R/8
of an available R/2 - 4, though its geometric *shape* is already optimal — Lemma S), N_3/N_1 split 160×,
β⁴ → β² in (★) 44×, B(m) against 2^{2m} 34×.
**The step with the most slack: the Young absorption of the supercritical potential** (§2.4(e)) — it raises
the entire one-step constant to the power a, costing 3.5e7 at q = 8.

**Does the interface carry a number? Not as EPS-T is written. It does at q ≳ 30**, conditional on
C_1·C_V ≲ 1e4 and ε_* ≤ 1e-4. **The only remaining blocker is (★) itself** — steps (2)-(4), l.1471-1487,
where C_1 and C_V live. Expanding them to numbers converts §6.1 from CONDITIONAL to PROVEN **by
substitution, with no further derivation; one session, independent of every other lane.**
*Lead: commissioned immediately as STAR_CONST.md.*

**Corrections found.** l.1504's e^{100} should be **255**, not REVIEW_SQ_S4's 1.6e4 — the review applies the
crude p ≥ R/64 at the one worst R and **over-states by 64×**. S4-6's R_0 = 128 confirmed independently
(i_* = 0 on [64,128)), but its "C_T ≥ 128² = 16384" is **not the leading contribution**, swamped by ≥ 6
decades. S4-3's added hypothesis is necessary but changes no factor of C_T that matters (the dominant term
uses 𝒮 and k only, never η).

**Failed checks, reported as fails.** Three of six pre-registered verdicts FAILED (B1, B2, B3) — **all
errors in the worker's own criteria**, not in SQ.md or the review: F peaks at the *right* edge of each dyadic
block, so max F is 4080 at R = 255 (not 2048 at 128) and 175.8 at R = 79; and i_* = 0 on [64,128), which the
criterion mis-transcribed. A1, A2, B4 PASS. ct1_moser.py Block C is superseded by post-hoc ct1b/ct1c and
nothing rests on it. **Also recorded: three of the worker's four pre-stated structural expectations were
refuted, including E4 ("raising q will cost"), which was backwards — and that refutation is the finding that
decides the task.**

## BFT_B session 10 — (CO-fun) and (GT-sup). LANDED. Two diagnoses refuted, including the lead's.

§34 (PRE-STATED, first edit, 13:07:28 UTC, 13525 bytes), §35, §36, §37.1-§37.4, appended only — no line of
§1-§33 touched.

**(CO-fun): PROVEN under a strengthened hypothesis — and session 9's own diagnosis of it was WRONG.**
Session 9 said (CO-fun) was open because "the funnel pieces are co-closed only collectively, so Theorem W0
cannot take them one at a time." **The funnel is not the obstruction at all.** Two facts (§35.1-§35.3):
(a) **Theorem W0 uses d*j_0 = 0 in exactly one essential place** — step 2's representative freedom — and
that is a condition on the **total** object paired with Y^p_0, **never on individual pieces**;
(b) the funnel is produced by the ρ-recursion, so **it never enters the dual pairing
f_0(p) = n²⟨S, Y^p⟩ at all.**
What does enter is the level-0 dual push-down C(j) = Σ_l (Q^{(0→l)})^T j_l, whose funnel parts **regroup**
(the brief's route 2): ξ_i = R_{i+1}(D(S)) - ψ_i, so under **D(S) = 0 as a function — call it (CC-0) —**
C(j) = Σ_l (Q_str^{(0→l)})^T ĵ_l, which is co-closed and priced k,T-uniformly by Lemma FT.
**Theorem COF: (CO-fun) PROVEN as an implication under (CC-0)** (m = 0, trivial background, 0 < α < θ;
inputs YH, W0 steps 3-4, GU, LIN0 and PW-cc's residual estimates, all CONFIRMED in lane A).
**Lemma CD (i) gives (CC-0) at every critical point of 𝔉_k** (§35.6).
**(CO-fun) as stated in §31.2 is FALSE without (CC-0)** — pre-stated S10-F4 occurs; erratum [S10-fix 1], and
§31.2's stated reason is superseded. Also proven: the free dΔ_0^{-1} form of (CO-fun) **loses a factor T**
(massless kernel ℓ¹ ≍ torus side), so the dual pairing is the only route (§35.8).

**(GT-sup): CONDITIONAL, and expected TRUE, not false. >>> This refutes the lead's forwarded guidance.**
I forwarded REVIEW_BFT_A_S8's exact spike data and told this worker that "the decisive question is whether
the spikes of λ^{Γ_E}_* are supported where D(S) lives". **The question is moot.**
λ^{Γ_E}_*(p) = Λ(Y^p_{*,0}), so lane B's own **PROVEN Lemma ΓT-op (d)** applies:
**sup|λ| ≤ 20·max_X ‖(Y^p_*)^c_0‖_{∞,Ñ_X} with an ABSOLUTE constant** (§36.2). So **(GT-sup) is not a
question about spike support at all** — it is a local sup bound on the chosen representative's own level-0
field, named **(Y-sup^loc)**. Further: **the level-k root charges drop out of the remainder identically**
(Λ(x)(c_Y) = 0; §36.1), and lane A's own arithmetic in Lemma RC's *Reading* puts the L^{2k-3}η² in
|D(R)(Z)|·n² with σ ≈ 0.003 **k-independent** — so **§31.3's expectation that (GT-sup) is false rests on
attributing the growth to the wrong factor** (erratum [S10-fix 2], ARGUED). The alternative ℓ^∞×ℓ¹ route
(§36.4) is conditional instead on **(NEUT-box)**, box-local neutrality, whose obstruction is ΓT-op (e)'s
pinned compensation charge.

**(NC-Γ) for Γ_E: COMPLETE at critical points; one scalar left off them. Theorem NCE (§36.5):**
- **(i) PROVEN as an implication at every critical point of 𝔉_k**, m = 0, trivial background, **every gauge
  fixing**, ~~k,T-uniformly~~ **[CORRECTED by REVIEW_BFT_B_S9_S10: NOT k-uniform. Corollary COF-crit (§35.6)
  is WRONG — it substitutes a per-level row bound for Theorem COF's ‖j‖_Pc = max_l L^{θ(k-l)}π_l(j_l),
  which differ by L^{θ(k-1)}; the sharper route leaves ≈ 25(k-1). The lead banked the uniform form here and
  in HANDOFF.md; both are corrected.]** Curvature half = Corollary COF-crit; residual half = session 9's
  Corollary RHT-V; remainder vanishes by GT-split / FG (iii).
- **(ii) Off the critical set both routes of §31.3 land on the same object:**
  D(S^E_0(S)) = I_χ^T D(S), so **the whole obstruction is the compensation charge Q_X = ⟨χ^5_X D(S)⟩ — one
  scalar per level-k box** — appearing twice, as the (P0) size of Γ_E^T D(S) and as the root charge of
  Proposition COF-res paired against Φ_k(Y^p_0) = Proposition TE's tent coefficient. **(TENT-Q) and
  (NEUT-box) are two faces of it.**
- **Cross-lane:** D^root and D^⊥ **partition** the two targets, neither drives both; and **(CO-fun)'s
  residue is the SAME FUNCTIONAL as the (GE-T) refutation, so they must not be priced as two items.**
  *Lead: that last point removes a double-count from the project's open accounting.*

**Single remaining obstruction:** curvature half → **(TENT-Q)**, the compensation charge ⟨χ^5_X D(S)⟩;
(GT-sup) → **(Y-sup^loc)**, a local sup bound on a named representative's field — **a lane-A linear-package
item**, i.e. it leaves lane B entirely.

**Checks.** bb10 (d = 2, L = 3, k = 2, exact Fraction, no lock, 5.95 s): **ALL PASS** (A1-A8, B0, B1) — the
regrouping identity, the root-charge defect identity and J_0 = C(j) - (Q_str^{(0→k)})^T ρ_{k-1} all exact.
bb10c (k = 3, criteria written before the script, no bb10 criterion retuned): **NOT ALL PASS — C4(b)
FAILED**, disclosed, diagnosed and **kept with no rerun**: the test family inflates π_0(j_0) (solve_div is an
antiderivative), so the two available bounds did not separate on the data. **The FAIL is of a
*demonstration*, not a lemma** — C4(a), the inequality Proposition COF-size actually uses, passed everywhere,
and C1/C2/C3/C5 confirmed Lemma DF-cc at three levels with its hypothesis shown load-bearing.
**The worker also corrected its own §37.1 in §37.4:** under (CC-0) the two groupings are the *same vector* at
every k, differing only in the available bound.

§37's FOR OTHER FILES records that **REVIEW_BFT_A_S8's closing request — D1's remainder bound, "written
nowhere" — is Proposition NCR** (§31.1, written concurrently), and that this session supplies its two factors.

## STAR_CONST.md — (CONST-T) now carries a NUMBER. 606 lines, §1-§12.

**The two constants, COMPUTED exactly.**
| | value | status |
|---|---|---|
| **C_1** (the (★) prefactor) | **5.70e3** | COMPUTED, from the cut-off bookkeeping of steps (2)+(4) |
| **C_V^source** | **7.23e-2** | COMPUTED |
| **C_1·C_V^source** | **411.92 ≤ 412** (exact floor over all δ-budgets: **319.20**) | **COMPUTED (exact)** |
| C_1·C_V^{curv,lin} = 17.5·C_K′c_N | [68, 3.4e5] | CONDITIONAL — C_K′ not in SQ.md |
| C_1·C_V^{curv,quad} | ≈ 3.0e6 at (c_N, C_B) = (1, 3.6) | CONDITIONAL — C_B not in SQ.md |
| ‖V_s‖_∞ ≤ R^{-2+8/q} < 1 | — | **PROVEN** (answers CONST_T §8.1 ask (b)) |

**q_min = 11** (conservative β-power) or 10. **>>> YES: the (CLS-min) → RLARGE interface carries a number at
q ≈ 12 — C_T ≤ 5.3e12 against the 1e13 ceiling, so C_D ≈ 1e15 ≤ 6.7e15.**

**But the PASS rests on two restatements of SQ.md §15.1, both PROVED here, neither new mathematics. With (★)
exactly as written there is NO admissible q.** Two more wrong steps, in the session's established pattern:
1. **V must carry THREE coefficients, not one** (l.1480). With a single C_V the product is max{…} ≈ 3.0e6,
   because the **quadratic curvature** coefficient — harmless in itself, its potential has norm ∝ ε_*² — is
   **promoted into a multiplier of the SOURCE term, the one raised to the power a.** **This alone is a
   blocker, independent of every multiplicity.**
2. **The source term's neighbourhoods are 3 plaquettes and 3 links, not N_3 = 14406 or N_1 = 486**
   (Lemmas A1-A3, §2.2: D_1* and D_2 are each exactly **3** covariant differences, not "≤ 6"; the source
   pairs each plaquette with exactly **2**; each link is the far link of exactly **3** plaquettes).
   **Worth 162× in the one-step base: q_min 74 → 11.**
Six-row table (multiplicity × β-power) at A_cγ_c = 1: M-sharp 10/11; CONST_T's 486 → 20/74; **SQ literal →
62 / none ≤ 400.**

**Answers to the lead's specific asks.**
- **η does NOT enter C_1 or C_V^source.** Steps (2) and (4) are pure calculus on ζ, w; the source group never
  touches U. η enters only the curvature coefficients, through c_N, BIA and WB. **CONST_T §5.3 CONFIRMED**,
  its reason sharpened. No contradiction with REVIEW_SQ_S4's S4-3.
- **Not pinnable in (★):** (i) **C_B and C_K′** — SQ gives only C_K′ ≤ 200·96 = 1.92e4 from counts it calls
  crude, and nothing for C_B; the missing estimate is an entrywise bound on WB's kernel k(p,p′) and BIA's BCH
  remainder. Harmless for C_T, but it means **the single-C_V reading of (★) has no number at all**.
  (ii) **A_cγ_c / ε_*** — in step (5), outside steps (2)-(4): §8.3 gives the **condition A_cγ_c ≤ 3.4e3**
  rather than a value, and notes CONST_T's SUPPLIED 4.7e3 **just fails** it, so ε_* must drop a factor 2-10
  (free: ~30 decades of headroom). (iii) Sharpness of 412 — OPEN, worth ≈8×, immaterial.
- **A β-power correction to CONST_T (§6.4, §11.2):** the V_c branch has a_c = 2 with a β⁴ coefficient, so the
  telescope needs **B(4·max{a,2}) = B(8) = 1931.5 for every q ≥ 8**, not B(4a). Worth 28× at q = 32; it moves
  CONST_T's q_min at C_1C_V = 1 from 9 to ≈ 12.

**Checks — one pre-registered FAIL, handled exactly right.** SC1-1 PASS. **SC1-2 FAIL** — the pre-registered
reading "C_1 = 20 wherever C_1 appears alone" gave 10/16/30/56/none against CONST_T's 9/16/31/132/none; **the
error is in the worker's own criterion** (CONST_T §6.3 splits the product as C_1 = C_V = √(C_1C_V)). Failing
output kept unaltered; post-hoc SC1-2b (labelled) reproduces 4 of 5 (134 against 132, traced to CONST_T's
B(4a) column being ≈8% low at mid-range; no CONST_T conclusion changes). SC1-3 PASS (monotonicity;
independently confirms CONST_T §4.2's q-lever). SC1-5 PASS. 22 s, plain python `-I`, no numpy/BLAS, no lock.
**Disclosed in §12: sc1_criteria.md's header says 13:3x UTC; it was actually 13:43. The order is correct
(STAR_CONST §1 13:31 → criteria 13:43 → script 13:50) and the worker did NOT edit the criteria file to fix
the minute.** *That is the right call and worth noting as the standard.*

**Biggest remaining obstruction: ε_* / A_cγ_c**, in Stage 1 step (5) (l.1489-1494). §8.3's inequality
**A_cγ_c ≤ 3.4e3 is now the only thing between CONST_T §6.1's formula and a PROVEN number**, and it is one
bounded session, independent of everything else. *Lead: commissioned immediately as EPSSTAR.md.*

## REVIEW_NQ_S1 — (N-Q) CONFIRMED PROVEN. 636 lines, findings NQ-1…NQ-30.

**The reviewer REBUILT rather than checked**: re-derived the Step 1 telescoping by induction from the two
cited identities, and re-implemented the whole computation from primary definitions in deliberately
different code (tuple keys instead of bit packing, Fraction instead of integers over a common denominator,
its own composition recursion, and a streaming coordinate sweep for j = 3 so the 4.1M-entry row is never
resident). Peaks 52 / 482 / 914 MB; no lock (rule-6 exemption). **All three exact values reproduce,
including j = 3: 205/27, 2021/81, 6115/81, supports 459 / 47,385 / 4,113,747, all four directions.**

**>>> A CONSTRUCTIVE STRENGTHENING: the identification of Q is FORCED, not chosen — by an argument NQ_CHECK
did not make.** PROOF (s23) l.2060 defines Setting SC's Q as Q_root verbatim; RTARGET l.414 and NORMS l.102
agree; SQ's `Q := Q_str` is a declared local convention (l.655/§0.4) whose proof the reviewer re-derived and
found correct. **And the CONSUMER forces it:** Lemma N1-11 step (4) uses
B_j = Q^j B_0 − Σ Q^{j−1−i} r_i, **exact only for Q_root**, while NORMS's own Lemma N1-4 says the Q_str
version holds only "modulo a level-j pure gauge" — **exactly the quantity a potential bound measures.**
So the ambiguity could not have been resolved the other way.

**Both of the lead's primed suspicions about the proof are UNFOUNDED.** (a) The slice identity
Q = Q_str − d∘h is an **unrestricted operator identity**; co-closedness attaches only to J-str's *transpose*,
so the telescoping is not confined to a subspace. (b) **‖d∘G‖ ≤ 2‖G‖ is exactly right**, because h lands in
**0-forms**, where d has two terms in every dimension — the 2(p+1)-term worry would bite only if the
correction were d of a 1-form, which is precisely what the slice identity avoids. Also ‖h‖ = 8/3 is an
**equality**, ‖ev^m‖ = 1, ‖Q_str^{(i)}‖ = L^i exactly, and **𝔮_0 = 11/3 is the exact sup of the proven ratio.**

**>>> THE FORK GOES TO NQ_CHECK, settled entrywise.** The ev-form and M-form composite slice functionals are
**the same operator** (0 differing of 23,328 at j = 2), and **h∘d = M − ev exactly** (0 differing of 81). So
**NORMS's j-linear growth is a bookkeeping loss, not a different quantity**, and its "h applied to a pure
gauge" hole genuinely does not arise in the ev form, where every h acts on Q_str^{(i)}B_0.

**One factual error (F1, binding).** G1 does **NOT** "strengthen check c8(f)'s 2e-16 to an entrywise exact
identity". In nq1_qnorm.py, Q_root and d∘h are assembled **from the same two primitives by the same code
path**, so G1 is **near-tautological**; c8(f) tested that the *nonlinear* U(1) S4′ map linearises to Q_root,
which G1 **assumes**. **F2:** G4 and G5 cannot fail for this construction, G2 cannot detect a wrong far-end
offset, **only G3 has real power**, and **no gate compared Q_root against an independent construction** —
the reviewer's own re-implementation supplies that missing control, and agrees.
*Lead: so the clean FAIL-free sweep was honest but under-powered; the reviewer's rebuild is what actually
certifies it. Worth remembering: a gate assembled from the same primitives as the object cannot test it.*

**New finding (F5), not in NQ_CHECK and in NORMS's scope: NORMS §N1 l.103-104 MISDEFINES Q_str** —
L^{d−1} transverse paths instead of the **L^d block legs**, **81 against the correct 135 entries.** Benign
for NORMS's conclusions, but it should be a third withdrawn text item. **Also NORMS l.414-415 conflates M
with ev.** *Forwarded to the NORMS reviewer and to the (N-loc) worker.*

**Other binding fixes.** F3: the theorem's quantifier does not cover the intermediate composites its consumer
uses (no gap, one line). F4: the "Lemma N1-11 → PROVEN-HERE" instruction over-reaches NQ_CHECK's own scope.
F6: the PROOF.md line numbers resolve in the **session-23 snapshot**, undisclosed and mixed with live RTARGET
numbers. **F7: the j = 1 clause of the BOUNDED criterion was vacuous a priori** (𝔫₁ ≤ p_L = 11 forces
R₁ ≤ 11/3), **and 𝔮₀ = p_L/L only at L = 3.** F9: 𝔠_P still carries C_f, C_R, R_eff.

**Process hygiene passes.** Criteria precede the script by 2 min 03 s on the filesystem; the reviewer
**re-anchored p_L = 11 to PROOF's own pre-session p_L := 5L − 4 and re-derived it as L + d(L−1) at d = 4**,
so no criteria constant is session-derived — the rule three sister lanes breached. The FAIL-free sweep is
honest, not retuned; the staged run used the stored script.

**>>> Biggest live wall, and a sobering honest reading: "(N-Q) was the small one."** (N-loc) **cannot be
settled by an identity** — it needs a **multi-scale axial construction**, already OPEN under PROOF's
**(CL-1)** — and **NORMS's near/far trade is "stated, not carried out."** Behind it, **(N-bg) is the
structural wall, and Theorem NQ-1 provably does not cross it** (NQ-1 is abelian/linearised and the slice
identity has no nonlinear SU(N) analogue). *Forwarded to the (N-loc) worker, which is attacking exactly
this; route 3 of its brief is where the work is.*

## REVIEW_NORMS_S1 — 887 lines, 15 binding fixes, and one of them is addressed to the LEAD.
## Tally of NORMS's 23 items: 13 CONFIRMED (2 upgraded by NQ-1), 4 NARROWED, 2 WRONG, 4 unchanged OPEN.

**Theorem N1-15 (A_soft = 1/L = 1/3 uniformly in k): CONFIRMED — at narrower scope.** The reviewer
**rebuilt the load-bearing "single pullback"** rather than accept the TOWER-VAR citation, which was the
lead's primary primed attack vector (a hidden per-level recursion re-entering through chain-rule terms):
D³(𝔉∘Z) = D³𝔉[Z′,Z′,Z′] + 3D²𝔉[Z″,Z′] + D𝔉[Z‴], and **both dangerous terms vanish by *first*-order
criticality** (𝔉_A = 0 and 𝔉_{AA}a′ + 𝔉_{AB} = 0) — **they appear and are annihilated, not dropped.** The
exponents were re-derived from the definitions at d = 2…6.
**Scope corrections: d = 4 ONLY** (every imported input is d = 4; LINEAR_PACKAGE l.56, l.166-171), and the
constant **𝔚 + 13.5𝔖 is ≳ 10⁷** at the proven locality rate, **not O(1)**.

### >>> THE MAIN FINDING: the per-level NO-GO IS NOT ESTABLISHED
(a) **"scale-covariant norm family" is used three times and never defined** — and as used it **excludes
𝔐's own Hölder leg**, i.e. the very norm the project's target is stated in.
(b) Part (i) is true but **VACUOUS**: it is the l = k anchoring identity, which the file itself calls "the
same number organised differently" at l.178-182.
(c) **Check n1-D is a TAUTOLOGY.** Its code computes k·eA + k·((d-4) - eA) **after discarding the only
derived quantity** (`# placeholder, replaced below`), so it returns d - 4 whether eA is 10⁶ or 1/3.
**"The weight-invariance half is PROVEN" therefore has NO computational support.**
(d) Part (ii) bounds an **estimate** from above **with no lower-bound input** — the standard this project
already applies at PROOF.md l.6550.
(e) **Pre-registered outcome (O3) was never tested**, although c38 C ("the Wilson cubic times the quadratic
normalisation, both → 1, plus an O(K²) irrelevant remainder") is literally (O3)'s signature.

**>>> BINDING FIX 1 IS ADDRESSED TO THE LEAD: HANDOFF.md l.44-47 carried this unestablished no-go into a
"do not relitigate" list.** I wrote that instruction, and it is wrong. **Corrected in this session:**
HANDOFF.md item 2 is struck and replaced with the reviewer's diagnosis plus an explicit note that the
per-level route is **OPEN, not refuted**; PROOF.md's [S24-fix 1] has the no-go half **withdrawn** as
[S24-fix 1a], with Proposition N1-8's Z_col correction retained (it stands on its own).
*The lesson is the project's own standing rule, which I failed to apply: no-gos need the same scrutiny as
positive theorems. I upgraded decision D2 "from a judgement to a theorem" on the strength of a tautological
check.*

### The headline gain figure is WRONG as stated
"≈ 10³ gain per level" sets **𝔠_vol = 𝔠_ax = 1**. But **Proposition N1-10's own bracket (l.371) forces
𝔠_ax ≳ 5.46**, so 𝔠_ax² ≳ 30; and **𝔠_vol is Corollary N1-9's c_m = coth(m′/2)^d — 3.7 / 80 / 7.4e6** at
𝒦's far-measured, near-measured and proven rates. Carrying both: **A_per ≤ 32-49 (gain 26-39)** at
𝔠_vol = 1, and **no gain at all** at 𝒦's near-field rate. **The same coth^d object is treated as 10²⁰ in
§N9 and as 1 in §N1.**

### NQ_CHECK confirmed independently, and NORMS's slip located
The reviewer re-derived the telescoping induction and **brute-forced ‖h‖ = d(L²-1)/(4L)**; (N-Q) is PROVEN,
𝔮_0 = 11/3. It also located the **arithmetic** slip in NORMS — a spurious L^{j-1-i} on factors the file
simultaneously declares non-growing — the second half of the M/ev conflation story.
**The lead's forwarded items verified:** Q_str misdefinition confirmed **entrywise, 135 against 81 entries**,
NORMS's support a **strict subset with 54 missing**; benign (every norm it uses agrees for both) **but it
contradicts the file's own import (I8), which Lemma N1-4's proof uses.** M/ev conflation confirmed and
placed causally.

### The lead's sharpened L-question, answered favourably
**A_soft = 1/L < 1 at EVERY admissible odd L ≥ 3, not only L = 3.** 𝔮_0 = 1 + d(L+1)/(2L) **decreases** in
L (11/3, 17/5, 23/7 → 3); the 𝔮_0 = p_L/L coincidence carries nothing. What worsens with L is the prefactor
L^{d-1}/(L-1). *So the NQ review's F7 scope worry is resolved in NORMS's favour.*

### >>> A CONSTRUCTIVE DISAGREEMENT WITH THE NQ REVIEW (RN1-20): (N-loc) may be UNNECESSARY
Locality enters Theorem N1-15 in **exactly one place and for one purpose** — to replace a torus volume
T_k^d by c_m ≈ 52⁴. **For tori of bounded level-k side, which is what NAH-unif's hypothesis quantifies
over, that replacement is not needed**, so Theorem N1-15 would hold **without (N-loc)** on that class.
The one unproven step is a **torus Hodge bound |B^{coex}|_∞ ≤ c_d·R·|dB|_∞**. The reviewer's judgement:
**"one session, not a paper, and it should PRECEDE opening the multi-scale axial gauge."**
*Lead: forwarded immediately to the (N-loc) worker, superseding the steer toward the multi-scale axial
construction that I had relayed from the NQ review. Two reviewers disagreed about where the work is and the
cheaper route won.*

### Biggest live wall: (N-bg), NOT (N-loc)
Theorem N1-15 bounds **the third Taylor coefficient at V_k = 1**; **(H-C) names the Lipschitz constant on
the class.** And NQ-1's slice identity **has no nonabelian analogue** (PROOF.md l.1159-1161).
**The reviewer's honest ledger line, which the lead adopts: "Nothing this session discharges a clause any
consumer consumes; the C_♭ clause moved OFF (CovLift)/(Mult-Y) and ONTO (N-bg)."**

**The reviewer's summary judgement:** *"The file's real contribution is Lemma N1-1 + Theorem N1-15 + §N7's
exponent-pair requirement on BFT-1 — substantial. Its no-go and its headline numbers are not."*

## BFT_B session 11 — the nontrivial background. LANDED, and it CONSOLIDATES two of the project's
## biggest open items into one.

§38 (PRE-STATED, first edit, 13:58:33 UTC, 20,581 bytes, logged), §39-§43 + FOR OTHER FILES. §27-§37
verified byte-identical (first 4307 lines = 555,646 bytes).

### 1. The cheap audit paid off: Proposition SIX-RED (PROVEN-HERE)
The six lane-A inputs decompose into three tiers, line by line:
- **Tier A** (operator identities, hold at every background): duality/Hessian symmetry, adjointness, the
  Euler-Lagrange cascade, ev^T injectivity, BL-2(b)'s straight/funnel split, 𝒜's probability-average
  property, BL-C, telescoping, superposition.
- **Tier B** — exactly **four** exactness steps: (B1) d*d* = 0; (B2) root covariance; (B3) "a constant
  2-form is co-closed" (**inside Theorem YH** — S11-F1 occurred); (B4) "a closed 1-form is a gradient" /
  "**d of a constant is 0**".
- **Tier C** — exactly **four shared kernels**: (C-I) M, M_f of LINEAR_PACKAGE Thm 4.2′; (C-II) C_α of
  LES/LES-div; (C-III) C_K; (C-IV) Lemma LE.
**Corollary LIN0 is Tier A ONLY. Theorem CO-upR is Tier A + B only.** Neither carries an analytic kernel of
its own. W0, GU, CO-0R and CO-B rest on the **same** Tier-C list; only W0 needs 𝒩*.
**>>> So the nontrivial background is FOUR KERNELS + FOUR DEFECTS, not six hypotheses**, and (C-II),
(C-III), (C-IV) are all **local at O(1) coarse scales.** Session 9's framing corrected by [S11-fix 1].

### 2. (N1): stated, mostly closed, with a correct SELF-REFUTATION
**bb11 A5 FAILED and the FAIL is CORRECT**: the session's own pre-stated Theorem N1-alg claimed EP-alg's
gauge shift at every background, but it uses "d of a constant is 0", and **d_Z(const) = (Ad_Z - 1)c ≠ 0**.
Exact replacement (§40.1) verified in bb11b (ALL PASS).
- **(N1-a): PROVEN-HERE** in the narrowed form — the gauge shift on the **pinned** class, exactly what
  §16.1(d),(e) use; uniqueness from **Lemma CL-uniq** (CONFIRMED), and **stronger at Z ≠ 1 than at Z = 1**.
  S11-F4 occurred: covariance → **equivariance in (Z,x)**, the form Theorem GI-cov already consumes.
- Λ_0/const is **unavailable at Z ≠ 1**; read Λ_0^Z := {λ | roots = 0}. Costs nothing — GT-split already
  takes that representative.
- **(N1-d): PROVEN as an implication of (N1-nd)** = Lemma FG (i) at Z = **the linearisation of BFT-0's own
  uniqueness clause, hence consumed, not added.**
- **Minimal consumption (Proposition N1-CONS, PROVEN-HERE):** BFT-0/1/2 needs **(N1-a) + (N1-d)** for
  (CL-0)/(FP♯′) — **both algebraic** — plus (N1-c) for §16.9's fourth use; (N1-b)/(N1-e) only as the
  𝔐-bridge.

### 3. Conjugation transports, and a reframe of what was thought to block it
- **Lemma CONJ (PROVEN-HERE): at a FLAT background, Ad_G intertwines everything EXACTLY, pointwise.** So
  the deviation is governed by the background **CURVATURE**, not ‖log Z‖ — and f_j ≤ C_N f_k holds on all of
  𝒦(ε) **gauge-invariantly, with no global gauge**. **>>> SF's BNA-F4 is about log Z, not F_Z.** *That is
  the reframe: the quantity everyone took to be the obstruction was the wrong quantity.*
- **Theorem BGD:** (a) (d_Z d_Z λ)(p) = (U₁ - U₂)λ(far corner), ‖U₁ - U₂‖_F = ‖Ad_{W_p} - 1‖_F, size
  ≤ c_N C_N L^{-2(k-j)} f_k — PROVEN-HERE. (b) **root covariance is EXACT iff the background is a
  straight-row tower — which §25.5 PROVES for Z^off**; off the tower the defect is the background's own
  straight residual, CONDITIONAL on (C_g-θ). (c) **both defects cost a FACTOR (1 + C f_k) in 𝔐, with no
  weight penalty, no factor k, and no restriction on θ_w ∈ (0,2]** — S11-F2 did **not** occur.
- **Lemma FR-price (PROVEN as an implication of CL-iv):** the **box normal form** frame gives d_Z = d + δ
  with relative size ≤ 8c_N C_1 f_k on Ñ_X; (C-II), (C-III), (C-IV), (N1-b), (N1-c) transport at
  (1 - 8c_N C_1 f_k)^{-1}, **k- and T-uniformly**. **The complete axial frame cannot be used** (BNA-F4 on
  one box). T ≥ 17. **(B3) costs nothing** — 𝔐^∇_Z's transported Campanato oscillation was already doing
  that work.
- **Proposition NL-GLOB:** Thm 4.2′ is a **momentum-space** argument, so **(C-I) alone does not transport.**
  It splits into **(GAP-Z)** plus exponential locality (Combes-Thomas, scalar weight, Ad-blind — ARGUED).
- **Theorem TRANSP (PROVEN as an implication): (H-inv+)_Z follows from (GAP-Z) + (N1-nd) ALONE**, at price
  (1 + C f_k). **Anti-circularity checked explicitly**: (GAP-Z) is the composite ℓ²/symbol input, the same
  shape the trivial-background chain already has; no per-level C^{(j)} is used as a Newton inverse.

### 4. (CovLift)'s g_Z at θ > 0: Proposition GZ-FALSE (PROVEN-HERE) — the clause is FALSE
**False at every θ > 0, for every lift.** It demands coarse-curvature decay at rate θ, while BFT-1's
**maximal** θ_w^c = 2 gives f_l ≤ C f_k with **no decay**. **Not a nonlinearity and not a parametrisation
artefact — a CURRENCY MISMATCH.** And **θ > 0 is doing real work**, because **Theorem GU needs θ > α > 0 in
the same slot**. *This forecloses the search for a better lift, which is a real saving.*
**Theorem Cg-nr:** the (G)-slot representative is free modulo Ker d_Z*, and W0/GU take it as input, so the
clause reads with 𝔤_l = inf{‖(F_l - 𝒫)^c‖_∞ : d_Z*𝒫 = 0}; (N2-lip) gives the right size, weighted
≤ C(L,θ) f_k for every 0 ≤ θ < 1. S11-F5 occurred: the block-wise Z-parallel comparison form is co-closed
only **inside** blocks, so the residue is a **per-block neutrality condition** (Lemma BOG's no-wrap clause)
→ new named item **(CURV-dec)**. An OPEN item reduced to a sharper OPEN item.
*Lead: forwarded to the (TENT-Q) worker — (CURV-dec) and (NEUT-box) have the same shape and may be one item.*

### 5. >>> THE SINGLE REMAINING OBSTRUCTION, AND IT IS NOT NEW
**(GAP-Z)** is **BFT-5's input (1), (G♯_0-field), moved off the trivial chain** — i.e. LINEAR_PACKAGE §10's
paper-scale *"propagator bounds at a general background [cf. CMP 95, 96, 99]"*.
**>>> The nontrivial background and BFT-5 are ONE obstruction, not two, and PROOF must not count them
twice.** Behind it, two **session-scale** items: **(N1-nd)** (paid by BFT-0's own uniqueness) and
**(CURV-dec)**.

### 6. Check discipline, and a warning about the earlier checks
**bb11: NOT ALL PASS — A5 FAILED**, output and script kept unaltered, **no rerun of bb11**; the diagnosis
was written into new criteria **before bb11b existed**. **bb11b: ALL PASS** (5 new pre-registered tests).
**The first NONABELIAN lane-B check** (SU(2) adjoint, rational 3-4-5 rotations, exact ℚ) — and it records
that **the abelian model of bb9b/bb10 is VACUOUS for every §41 statement**, without editing them.
*Lead: forwarded to the BFT_B s9/s10 reviewer. This is the third independent finding today that a check
lacked the power to fail, after one tautology and one gate built from the object's own primitives.*
Six scope limitations recorded; **the material one: the reduced 5×5 box tests the algebra but NOTHING about
Lemma FR-price, whose whole content is the box's fixed coarse size.** (N1-e) at Z is ARGUED only, and
S11-F6 occurred (LES "on the periodic lift") with an ARGUED answer via Theorem W0-loc's box form.

## EPSSTAR.md — A_cγ_c closed, C_T is a number, and a 52-decade conflict found inside a banked review.
## 834 lines, §1-§11. 9/9 pre-registered verdicts PASS.

### The result is stronger than the task asked for
From (H3), σ_c = 4 ⟹ ϑ_c = ½, **a_c = 2**, σ′_c = 4/3:
**A_c = 36·C_1·|N_3|^{3/4} = 4.731e4·C_1**, **γ_c = R·‖V_c‖_{ℓ⁴(B_{3R/4-3})}** with
C_1·V_c = Φ := c_K·M_3u + c_RB·(M_1u)². Step (5) yields **two inequalities on the same norm of the same Φ** —
(ABS-ε), which is the **definition** of ε_*, and (5′) with C_S1(q,m) = 6964 (m = 1) → 5686 (m → ∞) at
q = 12, **96% of it from 4096·c_g**. Dividing one by the other **eliminates every SUPPLIED constant**:

> **Theorem ES-1 [PROVEN]: A_cγ_c ≤ (1 + √6)·C_S1(q,m)/m** — no c_K, c_RB, C_K′, C_B, c_N or ε_* in it.

At **m = 1** (Stage 1 exactly as written) A_cγ_c ≤ **2.40e4**, 7.2× over the 3.4e3 target. **m = 7 gives
2.87e3 and clears it**; m = 19615 gives A_cγ_c ≤ 1. **So STAR_CONST §6.3's ARGUED claim and its §8.4 item 1
("C_B, C_K′ harmless for C_T") are now PROVEN**: C_T's number is identical at all four C_K′×c_N corners and
at C_B ∈ {3.6, 1e2, 1e4}.

### >>> TWO ERRORS IN THE LEAD'S BRIEF, both the lead's to own
I briefed "ε_* must drop by a factor of 2-10" and gave ε_* ≤ 1e-4 as a working figure, taking both from
STAR_CONST §8.3. **Both are wrong.** The real drop factor is **2.4e4 to 6.8e11**, for two reasons the worker
disclosed:
1. **STAR_CONST §8.3 quoted A_cγ_c = 236.9·C_1 at CONST_T's SUPPLIED C_1 = 20, while itself computing
   C_1 = 5699.6.** At its own C_1 the figure is **1.35e6, not 4.7e3.**
2. **ε_* = 1e-4 is not admissible at all** — (ABS-ε) caps it at 1.93e-6/c_K ≤ **2.8e-8**.
*I relayed a figure computed at one value of a constant into a context using another value of the same
constant. That is the same class of error this session has been finding all day, committed by the lead.*

### >>> A NAMING HAZARD, and I walked the worker into it
**There are FOUR distinct symbols called ε_* in this lane:** EPS-T's; **N5-sf0's α_*/(10p_L(4R_*+5)L)**;
BG-b's (ε_1²/(4NB))^{1/2}; and BFT_B l.2719's local one. **My brief offered "PROOF's ε_* = 2.476e-13/C_Δ"
as a comparator — that is N5-sf0's, NOT EPS-T's, and the near-coincidence with the new value is a
coincidence.** A rename request is filed in the worker's FOR OTHER FILES. *Carried into PROOF.md as a flag:
four symbols sharing a name across lanes is a defect waiting to be a wrong conclusion.*

### Lowering ε_* is free, with 21-25 decades to spare — the important half of the task
- EPS-T's ε_* propagates through **exactly one channel**: θ_ε = ε_*/84 (l.1622). Every other use is
  **hypothesis-side**, where lowering helps. ε_U/ε_G are route (α), dead per S4-20.
- The **covering direction is discharged by construction**: FORCE defines τ_R with θ_0/C′ in its min.
- **No-change floor: ε_* ≥ 84·θ_0^SUP = 1.12e-37.** τ_♭'s binding entry is **θ_0^SUP = 1/(3.31e7·C_D²) =
  1.33e-39, not τ_R = 2.75e-15** — so **nothing downstream moves at all.** Slack **21.1 decades** at the
  crudest C_K′, **25.1** at the measured one. (REVIEW_SQ_S4's S4-16 "~30 orders" is right in order but
  5-9 decades optimistic: it compared θ_ε with ε_1, not with the binding entry.)
  **No consumer needs ε_* above the new value.**
- **ε_* needed: 1.44e-12** (measured C_K′ = 3.9) **to 1.46e-16** (WB's written C_K′ = 1.92e4, c_N = 2).

### C_T, with an honest status
**C_T(q = 12) = 5.288e12; q_min = 11** (9.774e12 at q = 11, 2.031e12 at q = 16, plateau 1.40e12), under
STAR_CONST's conservative B(8). The worker's independent harness **reproduces STAR_CONST §8.3's q-row to
three digits**. Breakdown: source **73.8%**, cut-off **26.2%**, **curvature branch 0.00% — A_cγ_c is out of
the problem.**
**Status: COMPUTED (exact); PROVEN given (H1)-(H4); CONDITIONAL on (H2)** — STAR_CONST's two restatements of
SQ §15.1, **which SQ.md does not state today** (without them C_T = 8.05e15 and **no q works**) — **and
CONDITIONAL on CONST_T.md and STAR_CONST.md, both UNREVIEWED. Not PROVEN unconditionally.** *The worker
labelled this itself, unprompted.*

### The interface: YES for RLARGE, but the margin is thin
**C_D = 4.76e15 ≤ 6.7e15, so a_bad = c_pr·ε_1² holds.** Margin **only ×1.41 in C_D and ×1.99 in t_pr
against ε_1.**

### >>> NEW OPEN (§6.6, ARGUED): a 52-decade conflict inside REVIEW_SQ_S4, which this session had banked
**REVIEW_SQ_S4 uses two different binding entries of τ_♭.** S4-16 correctly takes t_pr ≤ θ_0^SUP; but
**S4-14 item 2 computes η_♭ ≈ 4.2e-36 from τ_♭ = τ_R, which requires C_D ≤ 4.55e2** — at C_D ≈ 4.76e15,
**η_♭ = 3.5e-88, a 52-decade difference.** The **DESC-ε replacement for AE-red** needs η_♭ ≥ 4C_3ε_1², i.e.
ε_1 ≤ t_pr/(1.42e5√C_3), **5.15 decades stronger than the linear clause S4-16 passed. It fails by ≈ 9.7
decades**, and closing it would need **C_T ≲ 3.5e10 — below this route's own floor** (c_s ≥ 319.2 forces
C_T ≥ 4.4e12). The worker states it costs **the replacement**, not RLARGE and not A5-via-AE-red, and
recommends it as the next task because **it is a review decision, not a derivation.**
*Lead: commissioned immediately as TAUFLAT.md. Note what this means about my own process — I banked
REVIEW_SQ_S4 as a clean result nine commits ago, and a downstream worker found an internal 52-decade
inconsistency in it. A review is evidence, not a certificate.*

### Discipline
**9/9 pre-registered verdicts PASS** (ES1-1…ES1-7), exact Fraction/Decimal, python3 -I, no lock, 1.91 s;
40- and 60-digit runs differ in exactly two lines, both the stated precision. **No FAIL — and the worker
says so plainly rather than manufacturing one, while naming the limitation its criteria cannot catch (an
error in its own §3 derivation).** **Two provenance disclosures:** es1_criteria.md's header says 14:14
(actual 14:11) and §1's says 14:00:05 (actual 14:00:12); both **forward-dated**, orders correct, **neither
file edited to fix it.**
**Flagged for CONST_T's owner: §2.4(d)'s A := 36·C_1·|N|^{1/σ′} appears to be 18** — its own
Z = 144·C_1·Q·β⁴d⁻²Σ is consistent with 18, not 36. Not used, so **every number above is up to 2.83×
pessimistic.**

## PLD session 7 — (CEM-2) DISSOLVED, (LCR) restated past its own impossibility, ring price settled.
## §19.0-§19.11. Append-only verified by hash (head -2931 = 312681 bytes, md5 4a6a0f25…, pre-session stat).
## 13 criteria, 0 FAIL, four negative controls as designed. Tally: +3 PROVEN-HERE, 0 OPEN closed.

### (CEM-2): not closed — **DISSOLVED as an ingredient**
**Lemma DLR + Theorem W-FREE (PROVEN-HERE): across one R-free ring the chain's MARKOV PROPERTY eliminates
the far weight EXACTLY, at cost 1.** The factor audit shows the only density factors reading the
column-interior level-(k-1) links are the kernels of K_{k-2} and the per-cube badness indicators, while w
and F are measurable w.r.t. the complement — so E_ν[Z·F] = E_ν[ζ·F] with ζ an explicit **local product**
functional of U_{k-2} inside region(S). **Therefore §18.7.2's Proposition SPLIT is a LOSSY reduction** — it
estimates by comparison a ratio that is **computable exactly** — and **(CEM-2) is NOT an ingredient of
(CEM^COL).** §18.11's named obstruction is **superseded.** *Honest negative kept by the worker: ζ is not
bounded pointwise, so this relocates rather than closes.*
*Lead: I briefed this worker to attack (CEM-2) as the chain's binding obstruction. It was not an ingredient
of the thing it was supposed to gate. Third time today that the named wall dissolved on inspection.*

**Typicality was the right mechanism, and it is now PRICED:** 1/(1-λ_f) per cube in the exponential
currency, 1 + log⁺C in the first-moment currency. The event route gives u·ε_1² = 4.489e15, which in the
first-moment currency **misses §18.8's own ceiling by 2.2445e6 *in the log*** (p7 A2) — a sharper statement
than "they differ by 4.489e15". **The structural reason the thresholds cancel:** the event bounds the
*field* at a g-independent threshold (costing a factor u to convert to action), while the measure prices it
in *action* units where the suppression rate is the same u. Residual: **(BCH-1)**, strictly smaller than
(CEM-2) in four ways (first moment; one scalar per cube; outside field only; no comparison of two laws).

### (CEM-1): three parts → two, with a self-correction
- **(a) the main-term reduction off G_Q: unchanged, still OPEN, still first to write.** The worker claimed
  in §19.4 that it was unnecessary and **WITHDREW that in §19.5** (appended, not edited): the trade compares
  the *minimised* column action with the exponent of the level-(k-1) **marginal**, and the fluctuation terms
  between them are exactly the representation's content. **§18.7.2 was right.**
- **(b) + (c) are ONE statement. Theorem AT:** the moment is a local coupling-lowering ratio whose log is
  ∫₀^{λ_f} E_λ[𝔞^col] dλ — so the u-interval is the **integration variable of an exact identity**, not a
  separate hypothesis on CL^J/R1^J activity bounds.
- **Also withdrawn: (ACT) as first stated** (its functional is extensive, ≍ 81^{k+1}; refutation ARGUED),
  repaired by **Lemma DOM′** with the minimised action.
- λ_f = 24θ(1 + 2Rg_K²) **rebuilt** from (F_R); **the κ's cancel, so the side condition is λ_f < 1, not
  λ_f < κ** (negative check recorded).

### >>> (LCR) restated past its own impossibility: **(LCR^act′)**, a FIRST moment
E_{λ,wF}[𝔞^col_S] ≤ B|S| for λ ∈ [0, λ_f], uniform in g, m, K, T, 𝔥, R, 𝒜, 𝒜′, F, F_<. Against §18.8(ii):
clauses **1, 3, 5 kept**, clause 2 (law class) **demoted** (the weight never enters the column's conditional
law), clause 4 (allowance) **discharged**. **It escapes §18.8(i)'s impossibility because that argument
bounds a conditional EXPONENTIAL moment from below and says nothing about a FIRST moment.** Clause 5 becomes
B ≤ 2e9; the equipartition value is 52488 — **4.58 decades inside** (p7 B3).
**p7 B1: (dof/2)·ln(1/(1-λ_f)) = 18190.954606 against p6 D1's recorded 18190.95** — so §18.7.2's "Gaussian
heuristic" is the **equipartition value of an exact identity.**
*PLD §18 had recorded that "no certificate for (LCR) as written is possible". The restatement is the way
through: the impossibility was about the exponential moment, and the chain only needs the first.*

### Level 0: (0a) reduced, and HW's reading of it reversed
**(0a) is strictly weaker than (0b)** (PROVEN: (0b) needs a level-0 (SDP), and there is no U_{-1} to
integrate). **Theorem L0: (0a) ⟸ (W0-EQ) + (BCH-0)**, where (W0-EQ) is a Laplace statement on **one 3⁴
block, 648 dimensions, 645 transverse**, uniform in the boundary datum; equipartition gives
log C_fc⁽⁰⁾ = 13.7254756 (p7 C2). **Level 0 is the MOST TRACTABLE instance, not the largest residual** —
Lemma DOM′ is an *identity* there, and the bare Wilson measure's DLR replaces the kernel's Markov property.
**HW §37 should state the level-0 clause as (0a) only.** (NP-F13) refuted.

### Single remaining obstruction to (SDP)^A: (BCH-1)
The first moment, under the buffered-weighted past law, of the boundary-forced conditional free-energy
excess of a column. **It is the ONLY item in the chain whose statement still mentions the far weight.**
**Route (ρ2) removes it** (pointwise (m1) w ≤ w^{-𝒞}, ring relaxation bought from CRC-2T′'s own induction, a
colouring/Hölder step), leaving **(SDP)^A ⇐ (CLS-min) + (RING-cc) + one weight-free single-level statement
(EQ-bc)**. Three declared prices: ×82; **c_A = 0 given up** for the patch allowance HW already asks for; and
θ ≤ 1/(24·5⁴) = 6.67e-5, **still 80× above the feared fallback**. ARGUED, with the circularity condition
declared.
**Route (ρ1) (outward regress) is log-DIVERGENT at d = 4 and convergent at d = 5** (p7 D1/D2, INDICATIVE) —
**the same marginality as NORMS §N5**, raised by the worker as a question to those owners.
*Lead: d = 4 marginality now surfaces independently in two unrelated lanes. Worth treating as a structural
feature of the problem rather than a coincidence of two estimates.*

### Two cross-lane consequences
1. **Finding (BUF-CC): a gap in §18.7.0.** Lemma BUF at level k-1 needs the **closed** column of N_1(𝒜)
   unconstrained, not "N_1(𝒜) R-free". Repair: hypothesis **(RING-cc)**; implications unaffected.
2. **>>> THIS SETTLES HANDOFF's open cross-lane disagreement 1, AND REVERSES HW §41 item 4 — and my steer
   was wrong.** **×17 is right for the OPEN column** (level-k BUF); **×82 for the CLOSED column**
   (level-(k-1) BUF), **which is the application the proof actually makes.** p7 F1: 1 + 3⁴ = 82 against
   1 + 2⁴ = 17, **ratio exactly 81/16. §18.4's ×82 stands.**
   *I recorded in HANDOFF.md that "HW's is the better-supported figure" because Lemma RING had a proof and a
   check. Both lanes were right about different columns; the one the proof uses is PLD's. HANDOFF corrected.*

**Four downgrades recorded, one of them of the worker's own §19.4.**

## REVIEW_BFT_B_S9_S10 — 101 KB, 27 findings. It REFUTES a claim the lead had already banked.

### >>> THE REFUTATION: Corollary COF-crit (§35.6) is WRONG, so Theorem NCE (i) is NOT k-uniform
Theorem COF is correct, but its RHS carries **‖j‖_Pc = max_l L^{θ(k-l)}π_l(j_l)**, and §35.6 substitutes the
**per-level** row bound π_l(V_l) ≤ 2C_NC C_bch κ_+L²η² — which §29.4 l.3729/3735 and §19.4 l.2629 both call
"uniform in l" — **as if it were that norm. They differ by L^{θ(k-1)}.** The sharper in-proof route
(π_0(C(j)) ≤ Σ_l π_l(ĵ_l)) gives a factor (k-1); optimising θ ≈ 1/((k-1)lnL) gives **≈ 25(k-1)**.
**Three independent records already said this:** lane A's binding [RBA2-fix] B3 (l.819-824, "the entire
level-count loss sits in the level-0 image"); REVIEW_BFT_A_S8's S8-13 ("the level sum stops being geometric,
and the factor k returns"); and **§36.5 (iv) ITSELF** ("the factor k … untouched") — **which contradicts
§36.5 (i) two pages earlier.** The missing input has a name: lane A's **(SPD)/(W2)**, OPEN.
**>>> The reviewer notes that SESSION24_RESULTS.md and HANDOFF.md "have already banked the k,T-uniform
form." That is me, twice. Both corrected above and in HANDOFF §5, which now puts the factor k first.**
*Lead's failure mode: session 10 asserted k,T-uniformity; three files already contradicted it, one of them
the same section two pages later; I propagated it into the binding handoff without cross-checking the lane's
own neighbouring text.*

### What the reviewer could NOT break
- **Lemma RT-cc: CONFIRMED, rebuilt from scratch.** Both suspected failure points are **absent**:
  ev^{(0→l+1)T} is injective on the **whole** space (distinct roots → distinct level-0 sites), and the
  cascade's consistency condition is **genuinely EQUIVALENT** to composite co-closedness, because the
  total-zero half of D(S) ⟂ Λ_0 is automatic (Σ_z ev^T d*j_l = Σ_X d*j_l = 0). **The keystone holds.**
- **Lemma FT, RHT-cc (K_f = 8.7377 verified), W0-use (checked line-by-line against BFT_A l.2465-2494),
  SPLIT, DF-cc, COF-size, COF-res, MASSLESS, GT-split, GT-ell: CONFIRMED.** **ΓT-op (d)'s constant 20 is
  verified and it DOES apply to Y^p_{*,0}** (its hypothesis class is "any level-0 1-form"). **Corollary
  RHT-V's "for every gauge fixing" is exact and earned.**
- **Session 10 beats session 9 on (CO-fun), cleanly, and there is NO circularity** — the lead's primed
  attack vector comes back clean. **(CC-0) ⟺ ψ_{k-1} = 0 ⟺ r_{k-1} co-closed, which is exactly what W0's own
  step 3 uses**, so it is the **right** hypothesis, not a convenient one. Theorem COF quantifies over
  sources, is **non-vacuous without any critical point**, and assumes nothing BFT-0 must prove.
- **Both FAILs handled correctly.** bb9's diagnosis is real (one expression, verified by diff) and **the fix
  is *forced* by the criteria file's own pre-registered energy, not fitted**; bb9b tests the same thing; and
  bb10c's C4(a) really is the inequality COF-size uses.

### Other binding findings
- **§31.1 *Reading* 2** ("λ's level-k-root part is TE's tent data") is **WRONG**, refuted by the same lane's
  §36.1; **no erratum covers it.**
- **(BFT-5_E) clause (c) is CONDITIONAL, not PROVEN** — it is recorded PROVEN at the background Z(V_k) via a
  **trivial-background** lemma.
- **§36.5 (v)'s "REVIEW_BFT_A_S8's request is already answered" is WRONG: an identity is not the bound that
  review asked for.** *The lead repeated this claim in the ledger; withdrawn above.*
- **The n² omission is NOT harmless in §31.3 (R2)** — the implication needs a third, unnamed input
  n²‖D^⊥(S)‖_1.
- **§36.2's "(GT-sup) is not a spike question" is NOT-VERIFIED:** it reduces to **(Y-sup^loc)**, which
  demands max_own|Y^p_0| ≲ 1/n near p — **contradicted by the |z|^{-3} profile behind 𝒩(Y^p) ≍ n.**
  *So (GT-sup) may be a spike-support question after all; forwarded to the (TENT-Q) worker, reversing my
  earlier relay.*
- **Provenance verified to the byte** (l.1-3569 = 409782 B exactly; §28's block 5259+119+80 = 5458,
  confirming both in-place corrections). Two process issues: **bb10_criteria.md has birth = mod = 13:12:15**,
  so "born 13:09:13, amendment appended" is **unsupported and the pre-amendment text is unrecoverable**; and
  **bb10c is not labelled post-hoc.**

### Part P — the lead's "could this check have failed?" lens, and it found a great deal
Of **bb9b's 15 verdicts: 5 unforced, 4 tautological or forced.** **A3 is the literal transpose of the
script's own definition Q = Qstr − dfun∘h** and therefore **cannot carry Lemma RT-cc (b)** — so §33.1's
"A3 + A7 carry the funnel part" **fails**. **B0 has near-zero power** (any operator built from r_l is
annihilated by Ξ — shown empirically; **B0 passed on the buggy energy**). B4 is forced.
Of **bb10's 11: 3 unforced**, and **A4 — which the criteria file calls the "central test" — cannot fail if
A3 passes.** bb10c's C4/C5 are session 10's **only** gates with power *and* a non-vacuous hypothesis, and
**C4(b) failed.**
**The funnel inside the ρ-recursion is tested NOWHERE, and no check reaches §35.6** — the very step now
refuted. The reviewer explicitly does **not** hold session 11's abelian-vacuity finding against these checks
(at the trivial background the chain maps *are* abelian), **but notes that (CC-0) at critical points rests
entirely on Lemma CD (i), a nonabelian identity no lane-B check touches.**
*Lead: this is the fourth and most productive application of the lens. It is now the standing first question
for every check in this project.*

**Exact re-derivations:** funnel kernel rebuilt from the definition (max|c| = 1/3, ℓ¹ row sum 4/3 ≤ 2, all
links interior); K_f = 8.73768…; bb10c C4's B^ψ = (1792, 2116/3, 2440/9) and (916, 1240/3, 1564/9),
B^ξ = 648/108; bb10 A8's 332 and 108 — **all matching the stored outputs to the last digit.**

**Verdicts.** (Res-Hölder) at m = 0: **Theorem RHT-cc closed, unconditional, with no 𝔉_k-criticality**;
**Corollary RHT-V closed only as the (H-inv+) *increment*, not as N_res ≤ C_Vη².** **Theorem NCE has content
and is not circular, but not the claimed uniformity.**
**Biggest live wall: the level-count factor k in the level-0 image of the non-co-closed plain rows** —
**upstream of (TENT-Q), (NEUT-box) and (Y-sup^loc), all three of which could be granted and still leave
≈ 25(k-1).**

## NLOC.md — (N-loc) BYPASSED at fixed T. 793 lines, 71 KB. One disclosed FAIL with a designed-FAIL control.

### The statement was ambiguous in exactly the way that decided the question
NORMS.md §N4's version is restated (§L2) as **two** claims about **one** admissible representative (Lemma
N1-2: nested, trivial at the level-k roots), with constants independent of j, k, the link x **and the torus
side T**: **(N-loc-a)** |ζ^c_{sm,j}Y|_∞ ≤ 𝔠_P L^{-(k-j)}|Y|_∞ and **(N-loc-b)** the exponentially-local
kernel form. **§N4's second display is never used by N1-15 and is withdrawn.**
**>>> "Uniformly in T" is the ENTIRE content of the open half, and it had never been written down.**

### Route 2 confirmed — independently, before the lead's note arrived
Theorem N1-15 consumes (N-loc) **exactly twice** (steps (2) and (4)), **only** through the column-ℓ¹ masses
𝔏_j ≤ 𝔠_L L^{(d-1)(k-j)}, and **only to replace a torus cell count T^d by c_m.** It consumes **neither
exponential decay nor finite support** — so RN1-20 is **CONFIRMED**.
**But Lemma LOC is NOT the instrument:** it localises the *covariance's* background dependence, not a
*potential's* gauge representative. So the lead's route 2 **via Lemma LOC** fails, while route 2's
weaker-hypothesis half **succeeds**.

### PROVEN: the torus Hodge bound, and the bypass
**Lemma NL-1 (PROVEN):** ∃λ with |B - dλ - h^B|_∞ ≤ 4dR|dB|_∞ on (ℤ/R)^d, the holonomy carried by an
explicit constant 1-form that **Lemma NL-2** computes exactly (c_j = L^{-(k-j)}c_k). With Theorem NQ-1 this
gives **Theorem NL-3′: (N-loc-a) with 𝔠_P independent of j, k and T** — the sup half needs only the
*gauge-invariant* locality, which is already proven (N2-exp).
**>>> Corollary NL-4: Theorem N1-15 is UNCONDITIONAL at d = 4, trivial background, linearised, at fixed
coarse side T ≥ T₀, with NO (N-loc)** — at a price of T^d ≈ **2.8e28** against c_m ≈ 7.3e6.

**New tool, PROVEN: Lemma NL-11** — degree-2 analytic division (a closed 2-form symbol is ν∧b̂ with b̂
analytic, |b̂| ≤ κ(η,η′)|F̂|, one step, every d ≥ 3; F̂(0) = 0 automatic for d ≥ 3). It is the
exterior-complex companion of LINEAR_PACKAGE Lemma 4.4, **rebuilt not cited**, per the standing rule. It
yields **Theorem NL-12: the pure-gauge half of (N-loc-b) outright, exponentially local, no box, no string,
no T.**

### Negatives, PROVEN — including a refutation of the lead's route 1
- **Global axial gauge fails by a factor T** (a Dirac string — though the string is a transverse pure gauge,
  Φ = d_⊥g).
- **Within-cell axial gauge meets the ℓ¹ budget and FAILS the sup budget by L^k: NORMS's near/far trade,
  carried out, FAILS.**
- **>>> Route 1 does not transfer, and the lead asked the wrong question.** I briefed: "check first whether
  the representative's box compressions obey a Combes-Thomas bound — that is the single hypothesis Theorem
  RW needs, and if it holds, most of the work is already done in the repository." The worker's answer:
  N5-sf0's gluing works because **R_g is block-diagonal orthogonal and the object is an OPERATOR**; a
  **potential shifts affinely**, so **Theorem RW has nothing to conjugate** — "Combes-Thomas on box
  compressions is not the relevant question."

### ARGUED — and it is the cheapest remaining win in the lane
The **Coulomb representative** has a **|x|^{-d} tail** (= LINEAR_PACKAGE Proposition 3.7's **Π_ex**), giving
**log T instead of T^d**, i.e. **10²⁸ → ≈ 16**. Missing only **a classical lattice Green's-function bound.**
*Lead: commissioned immediately as GREENT.md.*

### OPEN, but reduced to scalar form
**(N-loc-cell):** the fine half reduces to **a finite list of cell-flux divisibility conditions on the
already-proven symbol**, via the twisted-Koszul form of the level-0 complex (the L^k gain is the telescoping
sum; **the leading condition is PROVEN** from Lemma 4.4's identity). **This is (CL-1)'s open half — now in
scalar form rather than a construction to be invented.**

### Scope, stated honestly by the worker
Rates in coarse distance: η′ < π/2 for the gauge half (**j-, k- and T-free**), m′ < m_*′ for the invariant
inputs. **No j- or k-degradation anywhere proven. Every statement holds at all odd L ≥ 3; nothing uses p_L
or 𝔮₀ = p_L/L** (so the NQ review's F7 scope worry does not touch this lane either). Lemma NL-11 needs
d ≥ 3; Corollary NL-4 is **d = 4 only**.
**>>> Theorem N1-15 is now unconditional at FIXED T — and NOT uniform in T, which layer 2 needs. And
(H-C)'s C_♭ clause is NOT discharged:** N1-15 bounds D³E_k^br(1), while (H-C) names the Lipschitz constant
**on the class**. **(N-bg) is untouched and is the larger wall; NQ-1 provably does not cross it.**

### Disclosed FAIL, handled well, with a DESIGNED-FAIL control
**nl1-D FAILED as pre-registered** (199/200 inexact divisions, verdict 0). Script, output and criteria
**unaltered**; re-run under new id nl1-b, all three clauses PASS. Post-hoc diagnosis (**labelled**): the
helper's synthetic-division remainder *is* E_α p, so the clause tested something **the lemma never claims** —
which is also, post-hoc, **confirmation that the Dirac-string term is generically non-zero.**
**nl1-A/B/C PASS with a DESIGNED-FAIL control.** *That control is the right answer to the check-power
problem four reviews surfaced today, and it is now the standard to brief.*
**Eight requests in FOR OTHER FILES**, including three corrections to NORMS.md (R_eff undischarged,
(N-loc) → (N-loc♯) with "uniformly in T", the near/far trade) and, **in item 8, the three of its own claims
a hostile reviewer should attack first.**

## TENTQ.md — the box charges are ELIMINATED and (NEUT-box) is FALSE and withdrawn. 60 KB, §1-§6.
## All checks PASS, no FAIL — with a per-check power grading, honestly LOW→HIGHEST.

### The answer to "does Q_X vanish, cancel, or is it obstructed?" is none of the three, and better
- **Proposition QN (PROVEN-HERE):** **Σ_X Q_X(S) = 0 for EVERY chain source, no hypothesis.** The root-charge
  field I_χ^T D(S) is neutral, so the tent coefficient's constant mode is annihilated identically.
- **Proposition QSBP (PROVEN-HERE): Q_X(S) = Σ_l ⟨d(ev^{(0→l)}χ⁵_X), S_l⟩** — **the charge is a COLLAR FLUX
  of the source, never a box average of D(S).** Extends §25.1 (f) from one slot to the composite divergence.
- **Q_X ≠ 0** (pre-stated TQ-F2 does not occur): the exact configuration
  S_l = c·sign(d(ev^{(0→l)}χ⁵_X)) gives Q_X = 8c·L^{3(k-l)}.
- **>>> But |Q_X(S)| ≤ 2d·Σ_l π_l(S_l) = 8Σ_l π_l(S_l), k- and T-uniform, ABSOLUTE constant, and ATTAINED.
  The tent's total variation L^{3(k-l)} cancels EXACTLY against the own→coarse conversion. The charge was
  never the problem; the CURRENCY was.** *The fifth currency finding of the session.*

### (NEUT-box): a boundary term that does not vanish — FALSE, and struck
**Proposition QFALSE (PROVEN-HERE): (NEUT-box) as derived in §36.4 is FALSE by exactly L^{2k}** (post-hoc
probe tq1b: ratio exactly 9 at k = 1, 81 at k = 2). **Not repairable** — the bound above is attained. A
currency mismatch, not a cancellation failure. **(NEUT-box) should be STRUCK from the open set, not
attempted.** *My brief conjectured it was a vanishing boundary term; it is a boundary term and it does not
vanish, so the conjecture was wrong in both directions.*

### The pin cannot be moved, and it does not matter
The pin is **constitutive** of S_E — it is what gives ev^{(k)}Λ = 0 and hence makes Π_E a projection along
𝒢_0 — so pre-stated TQ-F5 occurs. **But Proposition PINC (PROVEN-HERE given ΓT-op (a)): the pinned charge's
entire contribution to every pairing cancels identically**, with Γ_E^Tφ = -Σ_XΣ_w χ⁵_X(w)φ(w)(A^X_w -
A^X_{c_X}), one piece of box dipoles and **no pinned term**. Lemma ΓT-op (e)'s second term is a property of
the **ℓ^∞ norm** (bb8t C1 really attains n^d), **not of the slice**. **Route (ii)/GT-ell is DEAD** — and
independently so: its *leading* term n⁴‖D‖_∞ already loses a power of n in the (P0) class.

### (TENT-Q) restated: the per-box charges are gone
**Theorem TQ-INT (PROVEN-HERE): 𝒯_p(S) = n²Σ_l⟨d(ev^{(0→l)}I_χΦ), S_l⟩** — **one** pairing against the
gradient of the tent-interpolated tent coefficient. With **Lemma TENT-TV**:
|𝒯_p| ≤ **128**·n²·osc_𝔅(Φ_k(Y^p_{*,0}))·Σ_lπ_l(S_l), **constant absolute**. So
**(TENT-Q) ⟸ (TENT-osc)**: one scalar inequality on the response field alone.

### Route 1 settled negatively and sharply
**Proposition TQ-NOGAIN:** neutrality buys **max → osc and nothing more** — Φ_k(v) vanishes at every level-k
root whose block misses supp v, so **osc = max exactly** (tq1 A8: ratio **1 exactly**).
**Proposition TGAUGE (a new identity; the check that could most easily have failed):**
Φ_k(x₀+dμ)(X) - Φ_k(x₀)(X) = A^{(0→k)}μ(X) - μ(c_X), so **the tent coefficient is a REPRESENTATIVE
ARTEFACT** that can be gauged to a constant (the residue then vanishing by QN) — **at an equal cost in the
main pairing.** Deficit: **exactly one power of n = L^k relative to (Y-sup^loc)**; the bound reproduces
§35.7's L^{2k-3} at the core value, **so the two accounts agree, and every L-power in §35.7 is a unit
conversion on Y^p.**

### Both of the lead's course corrections were addressed BEFORE it closed
1. **It does not claim k-uniformity; it accepts RS10-1** — and gives a **sharper** version: stating the
   bound against Σ_lπ_l(S_l) rather than ‖·‖_Pc makes the row loss **exactly the level count k — no power of
   L, no θ to optimise**, instead of ≈ 25(k-1). **Offered to lane B as cheaper bookkeeping of the same
   refutation.**
2. **(GT-sup)'s reopening is independently supported by its own numbers.** §2.8 (iii) reaches the same place
   from the other side: **sup_own|Y^p_0| ≍ 1, not 1/n, at distance 1 from p.** So **(Y-sup^loc) and
   (TENT-osc) are BOTH expected FALSE in the sup norm at the core.**
   **>>> The live question, now sharp: Φ_k is a BLOCK-AVERAGED AXIAL LINE INTEGRAL, not a sup, and the core
   of a |z|^{-3} field is a vanishing fraction of a block — whether the averaging beats the core is
   UNDECIDED.** *Lead: commissioned immediately as YSUP.md.*
3. **New project-wide dependency named: (Φ-conv)**, the convergence of Σφ_{i+1}, **exact only at i = 1 and
   ARGUED above.** **Every quantitative tent statement in the project, including §35.7's L^{2k-3}, is
   conditional on it.** *Flagged in PROOF.md.*

### Check-design, answered properly — and a proof that abelian scope is COMPLETE here
Per-check "tested against what / could it have failed", graded **LOW→HIGHEST**. **A6** (the new identity, two
disjoint constructions, pseudo-random data) and **A7** (a from-scratch rebuild of S8-7's four exact
rationals) have real power; **A1/A4 are near-forced and the worker says so.**
**No check reaches nonabelian content — and §2.0 PROVES that is COMPLETE, not vacuous, here**: every
operator used is su(N)-componentwise at the trivial background (§24.0, §16.1 (f)). **And the one place where
abelian WOULD be vacuous, it explicitly does not claim:** §2.9 (c) shows **Σ_X Q_X^Z ≠ 0 at a background**,
by a holonomy defect, curvature-governed via Lemma CONJ. (CC-0) rests on Lemma CD (i), taken as a named
input, untouched.
*This is the right answer to the check-power problem: not "my checks are powerful" but a proof of the scope
in which the model is complete, plus an explicit refusal to claim the case where it is not.*

### The lead's (NEUT-box) ↔ (CURV-dec) question, answered: THREE objects of one shape
**The distinguishing variable is the REGULARITY OF THE CUT-OFF.** (CURV-dec)'s residue and Proposition OB
use **hard** cut-offs (block indicator, piece decomposition) where neutrality is genuinely needed;
**(NEUT-box) uses the smooth χ⁵, which is exactly why it is defused** — the hard condition becomes a collar
flux with weight ≤ (15/8)/n. §42.4's "a pattern, not an identification" is **confirmed, with the reason
added.** **Transferable proposal (offered, not claimed):** run (CURV-dec)'s per-block solve against a
**quintic-tent partition** instead of a block indicator, absorb the per-box total by a pinned root charge,
and let PINC dispose of it — the three-step device S_E already implements. Unchecked: whether Lemma BOG's
constant 4q survives the smoothing.

### New named item: (P0-sup) — the two faces separate
Pre-stated TQ-F6 occurs. **Face (a) is NOT (NEUT-box):** Theorem COF's **Hölder** half feeds LES-div a
**pointwise** bound, and ‖Γ_E^TD(S)‖_∞ ≍ n^d‖D‖_∞ **genuinely**. **No neutrality statement repairs it.**
Proposed repair: take [f_0]_α from **Proposition NCR's DIFFERENCE form**, turning the Hölder half into a
Hölder (GT-sup).

**Net on the open accounting: -1 ((NEUT-box), withdrawn), +2 ((P0-sup), (TENT-osc)); (TENT-Q) RE-STATED, not
closed.** **Biggest remaining in scope: the own-unit size of Y^p's level-0 field IN THE NORM THE FUNNEL
ACTUALLY USES** — one lane-A object serving both faces, expected false in sup at the core, undecided in the
block-averaged norm.

## TAUFLAT.md — EPSSTAR §6.6 adjudicated ARGUED → **CONFIRMED**. 645+ lines. And it flags the lead twice.

### 1. The conflict is REAL, and the dissolution gate fired without saving it
The symbol-identity gate (pre-registered as the likeliest dissolution) **did** fire: **θ_0 IS two symbols** —
θ_0^SUP := 1/(2C_err) (SQ.md l.188) and θ_0^{SQ4} := min{θ_G, θ_ε} (l.1622) — and **REVIEW_SQ_S4's S4-14
item 4 had already flagged the collision, saying "both constraints apply".** **That is what makes the
conflict real:** τ_R and θ_0^SUP/C′ are **two separate entries of the SAME min** defining τ_♭ (SQ.md
l.317-319), so **"τ_♭ = τ_R" is an EVALUATION, not an identity.** Verdict **DISTINCT-AND-BOTH-BIND**.
Exact arithmetic (Fraction, 0.04 s, no lock): joint-consistency window **C_D ≤ 455.283301** exactly, against
a current C_D = 4.76e15 — outside by **×1.045e13**; η_♭ = **4.20662e-36** (entry τ_R) against
**3.52310e-88** (entry θ_0^SUP/C′) = **52.077 decades**; DESC-ε (iii) **fails by 9.707 decades of energy /
4.854 of ε_1**, strengthening factor 142125 = 5.153 decades. **All of EPSSTAR's headline figures are exact.**
**The defect is a STALE MINIMUM, not an error:** S4-14 item 2 is correct at C_D ∈ {0.45, 2, 2.25}; **S4-16,
in the same file, turns C_D into an output (≈(0.5-0.9)e3·C_T) and nobody re-ran item 2.** S4-16 itself is
sound — its t_pr ≤ θ_0^SUP is an upper bound valid whichever entry binds.
**>>> Power check PASSED, explicitly:** with C_D set inside the window and nothing else changed, **both
verdicts flip** (CONFLICT-ABSENT, CLAUSE-HOLDS). **Not a tautology.** *This is the first worker to apply the
session's check-power lens to its own adjudication, and it is now the standard to brief.*

### 2. One pre-registered verdict FAILED — against the source, making the finding STRONGER
**TF1-E SOURCE-DISAGREES.** EPSSTAR's three repair figures are each off by **√10** (3.16359 against
3.16228) — a one-decade slip under a square root. Corrected: t_pr required **9.5224e-35√C_3** (not 3.01e-35);
C_D ≤ **1.7812e13/C_3^¼** (not 3.17e13); C_T ≲ **1.98e10-3.56e10** (not 3.5-6.3e10). **So the repair bar is
1.78× HARDER than reported, and the finding is marginally stronger than its own author stated.** Output kept
unaltered, criteria untouched.

### 3. Load-bearing — YES, and it is a STATUS REGRESSION, not a lost convenience
The fact the lead's framing lacked is in **SQ.md's own §16 tally**: *"PRICE-iii and DESC-ε have their
hypothesis (REG-min) discharged by §15.3"* (via Theorem EPS-0, CONFIRMED by REVIEW_SQ_S4). So:

| route to AE-red's size clause | hypothesis | status |
|---|---|---|
| Theorem AE-red | (MS-Sob) | **OPEN** (HIST l.1323; ⇐ ARGUED ⇐ two further OPEN) |
| Corollary DESC-ε | (REG-min) | **DISCHARGED** |

**DESC-ε was the ONLY route free of an OPEN hypothesis** → LOAD-BEARING. It is a **replacement offered and
not yet adopted**: SQ l.348 says consumers "may cite DESC-ε *instead*"; HIST still states A5 ⇐ … + (MS-Sob)
through AE-red; and **EXISTENCE.md contains ZERO occurrences of DESC-ε or (REG-min).**
**Dies:** SQ §0.5's "all five are discharged by DESC-ε" for **3 of 5** consumers (HIST A5 (A), HIST
(I_k^E)′ (a4), SF.md — all take the size clause); **and with it, (MS-Sob)/(SQ-dev) RETURN TO THE CRITICAL
PATH — which HANDOFF.md's seven-item list did not name.** *Fixed: HANDOFF item 8 added.*
**Survives:** (CLS-min) to HW TE (ii) and RLARGE branch (iii) (infimum form, linear clause, margin ×1.99);
RLARGE's a_bad; **A5 via AE-red, clearing by 63.00 decades** (62.70 at C_S = 1e4); DESC-ε (i)/(ii); RED-0
(uses only DESC-ε's *conventions*); EPS-T/EPS-0/(REG-min). **Layer 2 unchanged.**

### 4. Cheapest alternative: lower ε_1 — and nobody had priced it
- **(A) Sharpen C_T: DEAD.** Only **0.080 decades** above its own floor (4.4e12), buying 0.160 against
  **4.854** needed.
- **(B) Sharpen C_err's prefactor** — a second lever the lead's framing missed (SQ's own "C_e and K crude by
  orders of magnitude… unclaimed"). Priced post-hoc: deleting the whole 4C_e bracket (96.3% of C_err) gives
  only **1.433 decades**; the residue needs K/C_D from 78.3 to **1.525** (×51.3) against h6's measured
  ×18.9. Most optimistic package lands **≈1.7 decades short.** One session, not a repair.
- **>>> (C) Lower ε_1 by 4.854 decades, to ≤ 9.38e-45 — CHEAPEST, ZERO new mathematics.** ε_1 enters
  **quadratically with the helpful sign**, and **RLARGE records only a CEILING, never a floor** (SQ l.312 /
  HW l.603's "ε_1 ≥ C′τ_♭" is a *branch selector* that already fails today). ε_1 < t_pr improves from ×1.99
  to **×142125**. Declared price: a_bad 2.5e-85→5e-95, n_H 2e87→1e97, wrap levels 184→205,
  g_K² 1e-88→1e-98 — and **RLARGE l.617-618 says these do not bind** (DX′ ceiling 54 decades below).
  **OWNER-GATED:** the worker did not sweep every ε_1 consumer, and **lowering ε_1 enlarges the large-field
  region.** *Lead: commissioned the sweep (EPS1_SWEEP.md). The decision itself is the owner's, not mine.*
- **(D) Prove (MS-Sob)** — cheapest that restores **all three** consumers at once, paper-scale, and already
  the route of record. **(E)** REVIEW_HIST_S4's per-scale sup pricing (Balaban CMP 109) would retire the
  item entirely. **(F) A weaker DESC-ε: NOT available** — the quadratic τ_♭ dependence **is** the descent
  mechanism, not bookkeeping.

### 5. Disclosures, including two against the lead
- TF1-E failed as pre-registered; reported unaltered.
- tf1b_criteria.md and tf1b_posthoc.py **share an mtime second**, so **file order is not demonstrable for
  the post-hoc probe**; no pre-registered verdict rests on it, and its one check with force (reconstructing
  S4-16's C_err to ×1.00274) is stated.
- Scope deviation, declared: post-hoc files prefixed `tf1b_`, not `tf1_`; new files, nothing overwritten,
  not renamed because the mtimes would go stale.
- **>>> SESSION24_RESULTS.md PROPAGATED THE INCONSISTENCY.** Its REVIEW_SQ_S4 entry carries "τ_R… now the
  binding entry of τ_♭" **and** "C_D ≈ (0.5-0.9)e3·C_T" **in the same entry** — the two are inconsistent, and
  I wrote both in one paragraph without noticing. *Corrected at the source entry above.*

## EPS1_SWEEP.md — ε_1 is FIVE symbols, and something binds TODAY. Verdict: SAFE WITH NAMED CONDITIONS.
## §0-§7, checks e1_*, e1b_*, e1c_*. Three checks reported as failures, unaltered.

### >>> ε_1 is at least FIVE distinct symbols, and one of them is a trap
| # | symbol | where |
|---|---|---|
| 1 | the χ_Q plaquette cut — **the subject of option C** | RLARGE l.58; same symbol in HIST/HW/PLD/SF/PROOF/EXISTENCE |
| 2 | **BFT_B's Theorem N2 threshold on the coarse flatness f_k, defined BY A FORMULA in O(1) constants** | BFT_B l.3058, l.2870 |
| 3 | FLOW's analyticity disc radius | FLOW l.1927, l.2834 |
| 4 | FLOW's mode amplitude | FLOW l.771 |
| 5 | an exponent index on a loop word | EXISTENCE l.2205 |

**Symbol 2 is the dangerous one:** BFT_B states it in **the same words** as RLARGE ("There are ε_1 > 0 …
such that"), but it is **an O(1) formula, not a choice**. Written as "lower ε_1", **lane B would read the
proposal as addressed to them**, and carried into 𝒦(ε_1) it would **cascade into 𝒞_glob**. TAUFLAT's
identity check (HIST A5 ↔ RLARGE a_bad) was correct **but did not read BFT_B or FLOW**.
**And symbol 1 has FOUR live numerical values in force:** 1.27e-39 (SF l.2837, **quoted as current by NORMS
l.746**), 9.52e-40, 8.95e-40, 6.7e-40.
*Third naming hazard of the session, after four ε_* and two θ_0. This is now a systemic defect, not three
accidents.*

### The consumer list
**Ceiling-side: 19 found, all helped or neutral** — (TH-ch′), (TH-ch″), the five-entry ceiling min, N5
compatibility, ε_1 < 2sin(π/N), HIST A5's ½δ_a, SF STEP 3, PLD (G0-1)(a)/(c), PLD INH, PROOF's 2D window,
PROOF l.4306's divergence window (which **widens**), EXISTENCE's non-triviality clause, KN-step's A_dη ≤ 1,
HW l.826, PLD's C_A exponentials.
**Floor-side: exactly ONE — and TAUFLAT did not have it.** TAUFLAT wrote "nothing bounds ε_1 from below";
**true of the seven files it read, FALSE in the existence lane** (EXISTENCE l.4191 "ε only has to contain
the typical field ≍ g", l.3112 coercivity "at distance ≫ g but < ε_1", with a constant at PLD l.995, an ℓ¹
margin ∝ g/ε_1). **It is respected: the window ε_1/g is 10^36.63 today → 10^31.78 after**, at the
ε_1-*independent* DX′ coupling, and exactly invariant at the ε_1-driven ones.
**Ratios (9 evaluated):** ε_loc/ε_1, θa_bad/(ε_1²/2N), α_E/ε_1, a·u_k and the (CEM-2) gap at the ε-driven
ceiling are **exactly invariant**; the **(CEM-2) gap IMPROVES by 9.707 decades** at the DX′ coupling; PLD
l.995's ℓ¹ margin is the one with the unhelpful sign. **(TC)/U3 fails by ×19.53 at EVERY ε_1** — option C
neither helps nor hurts it. *A separate pre-existing failure, newly visible.*

### Large-field cost, quantified
Wrap levels **183.6 → 204.0**; torus-caveat levels 42.2 → 47.3; coherent-chain depth 41.4 → 46.5
(81^depth 10^78.9 → 10^88.7). **The suppression exponent ε_1²/(4Ng²) is EXACTLY INVARIANT** (2.90218e16) at
the ε-driven ceiling; at DX′ the affordable level count falls 1.197e72 → 2.349e62, leaving **60.06 decades**
over the ~205-level wrap requirement. **HW's b_n, b_D, c_f, c_att and the ×82 ring contain no ε_1 and are
unchanged. More expensive, nothing broken.**

### >>> The declared price is INCOMPLETE, and RLARGE l.618 is FALSE — a_RS BINDS TODAY
Four of five figures reproduce; **g_K² SOURCE-DISAGREES ×2.04** (TAUFLAT's 1-s.f. rounding, favourable
direction). **Two exponents are steeper than the declared ±2: a_RS ∝ ε_1⁴ (19.415 decades)** and the Cauchy
C³ constant on 𝔇_{α_E} ∝ ε_1^{-3} (14.561, ARGUED).
**RLARGE l.617-618 re-verified against HW s6's ×82 closed-column numbers — and it FAILS.** g²_CRC
1.934e-96 → 3.794e-106 (margin over DX′ **55.90 → 46.19** decades), HIST-side 55.31 → 45.60, g²_ret
54.18 → 44.47, RLARGE's a/10² 63.63 → 53.92 (**so TAUFLAT's "54 decades" is the POST-move figure**).
**>>> But a_RS/10² sits 15.62 decades BELOW DX′ ALREADY TODAY**, and 35.03 after. **l.617 is scoped and
correct; l.618's unscoped "RLF's own ceilings do not bind" is FALSE.**
**The fix is already proven and was already requested: adopt KN-step's linear η_1** (EXISTENCE l.1771,
PROVEN; requested as REVIEW_PLD_S3 **E9** and never carried out) → **+66.52 today, +56.82 after: a 92-decade
gain.** *Lead: commissioned as ARS_FIX.md. This is independent of option C and matters either way.*
**Also: TAUFLAT's quoted 9.38496e-45 is 9.46e-7 ABOVE its own bound, so the clause FAILS at it.** The exact
bound is **9.38495112638e-45**, 4.8536 decades below 6.7e-40.

### Verdict: SAFE WITH NAMED CONDITIONS. **ε_1 was changed nowhere.**
(C1) scope to RLARGE §0's χ_Q cut only; **(C2) adopt KN-step's linear η_1, or scope RLARGE l.618 — the only
non-bookkeeping condition**; (C3) record the floor as ε_1 ≫ g; (C4) use 9.38495e-45; (C5) price the ε⁴ and
ε^{-3} branches; (C6) **settle which of the four ε_1 values is in force first**; (C7) conditional on
c₊·C_Ω ≲ 1.5e46 and on DX′ remaining binding.

### Check discipline — and a worker catching its OWN check having no power
Three reported as failures, unaltered: **e1-3 SOURCE-DISAGREES**; **e1-4 FAIL (a_RS binds already)**; and
**e1-5 NO POWER on its first run** — the clause verdict could not flip **precisely because the quoted value
sits on the wrong side of its bound** — re-run under new id `e1b` with criteria untouched, it is
**HAS-POWER** (both counterfactuals flip: floor at ε_1 = 1e-80, clause at ε_1 = 6.7e-40).
Independent constructions named: the floor against EXISTENCE's own window statements; the price against HW
§35.7's table and **SF §16.3/§19.4's ε_1-scaling tables — which already carry the ε^{-4} row TAUFLAT
omitted, and price ε_1 at values 14-57 decades BELOW this proposal**, so the proposal is conservative
against the lane's existing tables.
*Sixth application of the check-power lens, and the first in which a worker caught its own gate being
powerless, said so, and fixed it under a new id. That is now the fully-formed practice.*

## YSUP.md — the averaging does NOT beat the core. (TENT-osc) is FALSE by exactly n² = L^{2k}.
## Two disclosed FAILs kept unaltered, TWO designed-FAIL controls that both FIRED, one kept abort.

### 1. Φ_k's exact form and normalisation (PROVEN)
**Φ_k(v)(c_X) = Σ_{i<k}⟨K_i, v⟩** with **K_i := (Q_str^{(0→i)})^T h_i^T δ_{Y_{i+1}}**. **supp K_i is EXACTLY
the level-(i+1) block of c_X** (both ends attained — the h-kernel's longitudinal range {-1,0} and the
Q_str^T overhang n_i - 1 cancel to the block edge); **sup|K_i| = (10/81)n_i^{-3}** exactly;
**‖K_i‖₁ ≤ (8/3)n_i** (exact asymptote 2n_i). Normalisation pinned against an outside formula with **no free
parameter**: Φ_k(dδ_{c_X}) = L^{-dk} - 1 exactly at k = 1, 2 (TENTQ's TGAUGE). **No spurious power of n, and
§35.7's L^{2k-3} = n²/27 is reproduced.**

### 2. The exact block average — and the lead's guess was right for the wrong operator
For |v| ≤ C₀(1+|b-p|_∞)^{-3} in d = 4: the **block-averaged axial line integral is Θ(n_i^{-2})** (measured
16.72·C₀·n_i^{-2} at i = 6; ρ = 1.796, 1.901, 1.955 → 2). A **FULL** block average of the same field over
the same block is **Θ(n_i^{-3})** (measured 30.68·C₀·n_i^{-3}, ρ → 3).
**>>> "The brief's O(n^{-3}) is the right answer for the wrong operator."** *I briefed the full-average
power; the object is an axial line integral.*

### 3. The dimension count, and a THIRD independent appearance of d = 4 marginality
An axial line integral averages **d - 1 = 3 transverse directions and SUMS along the fourth**: per-link
weight n_i^{-(d-1)}, not n_i^{-d}; kernel ℓ¹ mass n_i, not 1. Against the profile,
‖v‖_{ℓ¹(block)} ≍ 64n_i — **marginal and log-free, because d - 1 - 3 = 0 EXACTLY at d = 4.**
*Third independent appearance of d = 4 marginality today, after NORMS §N5's cubic vertex and PLD §19's
route (ρ1) (log-divergent at d = 4, convergent at d = 5). This is a structural feature of the problem.*
**>>> But the power of the averaging is NOT what decides it, and my framing was wrong about which block.**
Φ_k's level-i term reads only the **level-(i+1)** block, not the level-k block. **At i = 0 that block has
side L = 3: the core is not a vanishing fraction of a 3⁴ block — it IS the whole of it, and the gain is 1.**
Even a per-level gain of n_i^{-3} would leave Φ_k = Θ(1).

### 4. The verdict, with an exact and striking lower bound
**0.0024768·C₀ ≤ max_X|Φ_k| ≤ 3.89·C₀, uniform in k and T.** The lower bound is **exact**: for u = ⅛d*δ_p
**the series TERMINATES — φ₃ = φ₄ = φ₅ = 0 exactly — so Φ_k = -65/26244 for EVERY k ≥ 2.**
**(TENT-osc) needs ≲ n^{-2}: fails by exactly n². (Y-sup^loc) needs ≲ 1/n and the averaged currency also
gives Θ(C₀): fails by exactly n.** The rescue fails in **both** currencies. **The far field is |·|^{-2}
(PROVEN), so the failure is strictly a CORE phenomenon.**

### 5. What is delivered anyway — and a project-wide dependency discharged
**(TENT-Q) is k- and T-uniform OUTSIDE p's coarse cell:** |𝒯_p(S)| ≤ 128·C·C₀·R_c^{-3}·Σ_lπ_l(S_l)
(ARGUED) — **shrinking the open item by T^d to the single core cell.**
**>>> (Φ-conv) is PROVEN for this profile class** (ratio L^{-2} = 1/9; the prior exact 17/243 sits under
it). *So [S24-flag 4]'s project-wide dependency is discharged for this class, one flag after it was raised.*

### 6. The fallbacks
**Hölder fallback (ARGUED): sound for face (a)** — it **removes (P0-sup) entirely** and lands on an object
that is O(C₀) with one extra power of decay, so it is **not harder than (GT-sup)**. **No help at all for
face (b)**, which carries the explicit n² of 𝒯_p.
**Bonus (ARGUED, hole named): (GT-sup) may hold WITHOUT (Y-sup^loc)** — λ^E_X(x)(z) = ⟨A^X_{c_X} - A^X_z,
x_0⟩ is a **marginal convolution of two |·|^{-3} kernels in d = 4**, giving O(C₀), **which recovers exactly
the factor n that REVIEW_BFT_B_S9_S10's S10-14 measures GT-loc to lose.** Needs the **box Neumann
Green's-function gradient profile**; not proven, not checked. *Lead: this connects directly to GREENT.md,
running now on lattice Green's functions.*

### 7. Check discipline — the strongest of the session
**Two disclosed FAILs kept unaltered:** ys1 A2(c) (the worker had pre-registered ‖K_i‖₁ as an *equality*;
only ≤ is derivable — **no statement uses the equality**) and ys1 A4 (band test inconclusive on the
staircase field at i ≤ 3). Repaired under a new id with the **original criteria untouched**: ys1b B1-B5 all
PASS. **TWO designed-FAIL controls both FIRED** (ys1 A7: corrupting off(l) gives 0 instead of -1/54;
ys1b2 B5: flattening the longitudinal multiplicity changes every value — **and ys1b_power.py's own mass
assertion caught it and aborted, and that abort is KEPT**). ys1 A1 **rebuilt all four of
REVIEW_BFT_A_S8's S8-7 rationals exactly.**

### 8. The one finite computation that decides face (b)
**Proposition TGAUGE's price.** Φ_k is a representative artefact that can be **gauged to zero**; TENTQ
prices the gauge as an **EQUAL** cost in the main pairing — **ARGUED, with NO μ CONSTRUCTED.** **With the
|·|^{-2} profile now in hand the natural μ is explicit, so this is ONE FINITE EXACT COMPUTATION, and it
decides whether face (b) is an obstruction at all.** *Lead: commissioned as TGAUGE_PRICE.md.*

**Not claimed, stated by the worker:** no k-uniformity for (NC-Γ) (RS10-1's upstream factor k accepted and
untouched); nothing nonabelian, at m > 0, θ > 0, or at a background; **no response field computed anywhere —
every statement about Y^p_{*,0} is CONDITIONAL on its core being in the |z|^{-3} class** (BFT_A §38.7 /
Theorem YH), **and whether Z″₀'s funnel could cancel g₀'s is the one place the negative verdict could be
attacked** (flagged to lane A).

## ARS_FIX.md — a_RS confirmed binding and WORSE; the lemma rebuilt; and the reason it was never adopted.

**a_RS binds today: CONFIRMED independently from RLARGE's own definitions** (l.64 → l.981/l.1026 → l.1020),
not from EPS1_SWEEP's summary. (V1) η_1's quadratic entry is active for all ε_1 < 512 (N = 2) / 768 (N = 3),
and a_RS's a_η entry for ε_1 < **814.587** — so **a_RS ∝ ε_1⁴ at every admissible ε_1**. (V2) the margin
against DX′ = 2.456e-152/C_Ω is **negative at all four live ε_1** (-14.506, -15.007, -15.114, **-15.617**)
and under **both** ceiling conventions. **RLARGE l.618's unscoped claim is FALSE.**
**Unfavourable correction:** l.1023 prices n cubes as (Ce^{-a_RS/g²})^{n/c_RS} with **c_RS = 5⁴ = 625**, and
l.1024 forms a_♯ = min{a″, a_♭, **a_RS/c_RS**}. **The honest margin today is -15.62 to -18.41 decades, up to
2.80 WORSE than reported.** Scope caveat EPS1_SWEEP omitted: l.832 declares a_♯/c_RS/n_♯ "superseded" while
l.830 still corrects Lemma RS *in a_RS*; **either way l.618 needs editing.**

**KN-step's linear η_1: REBUILT and PROVEN, not cited.** EXISTENCE's constants come back **independently**:
**106 → 8·12·(π/3)² = 105.276** (ratio 1.00688), **5.5 → 4.75889**, and **(L² + 5.5A_d)c_1 = ½ exactly**,
which is what makes the dichotomy exhaustive (t/2 + 4·(t/8) = t). **The mechanism:** re-centring at
W′ = Se^{X̄} makes the kernel error **quadratic** in δ (‖R‖ ≤ 3δ²) where RLARGE (R4) had it **linear**
(-2δ_c) — **and that linear δ_c loss IS the quadratic entry of l.64, so the adoption replaces (R3) AND (R4);
it is not a constant swap.** Strong structural check: **the kernel-branch constant κε_1²/(256N) comes out
IDENTICAL by both routes**, so only a_η moves.
**Hypotheses: H2-H7 all available in RLARGE** at the point of consumption (D4-norm (2) and g² ≤ κ are the
*same* tools (R4) already uses; conditional independence is Lemma TD). **H1 is NOT: Lemma KN needs M̄_c to
be a mixture with nonnegative normalised weights, where RLARGE l.992 says only "a mean of the T^σ_y".**
Convexity is load-bearing, so **the repair is CONDITIONAL on that one sentence.** Also flagged: the
traceless-log step carries an **N-dependence** (ε_1 < 78/N), **unadvertised** by "g-independent constants".

### >>> Why it was never adopted — and it is not an omission
**REVIEW_PLD_S3's E9 was an EITHER/OR, and RLARGE v3 took the other horn at l.830** ("η_1 is v2/v3's η_1
(E9)") — **a decision taken without the price in front of it.** The cheaper horn (fixing PLD's text) is
**worth nothing on this ceiling.** *So this is an owner decision to revisit with the price attached, not a
bug to fix. Surfaced, not taken.*

### Margins (C_Ω = 1; ε_1 unchanged, both values reported)
| | today ε_1 = 6.7e-40 | proposed 9.38495112638e-45 |
|---|---|---|
| quadratic η_1, /10² | **-15.617** | **-35.032** |
| linear η_1, /10² | **+66.523** | **+56.816** |
| with the c_RS divisor | -18.413 → +63.728 | -37.828 → +54.020 |
| **gain** | **+82.141** | **+91.848** |

**SOURCE-DISAGREES on the headline: the gain at TODAY's ε_1 is 82.141 decades, not 92** — 91.85 is the gain
at the *proposed* ε_1, the difference being exactly 2 × 4.854. **Both of EPS1_SWEEP's margin figures
(+66.52, +56.82) reproduce to 0.01 decade; only their DIFFERENCE was attributed to the wrong ε_1. PROOF.md
l.63-66 carries the same slip.** *Corrected in my flag above.*
**Carried through:** n_♯ falls **82.14 decades** (2.27e169 → 1.64e87), its level count 355.6 → 183.4 —
**exposing a second defect in RLARGE §5.4**, since l.612 reports 184 levels from n_H while l.1024 says the
induction uses n_♯. **m_τ** goes from 66/90/122 to an **ε_1-independent 3/4/5**.

### η_1 is THREE symbols — and worse in kind than ε_1's five
η_1^RS (RLARGE's quadratic min); **η_1^KN (c_1ε_1 — which PLD already uses in EIGHT places, calling it
"RLARGE's η_1")**; η_1^gauge (SQ l.1679, a bound variable). **Unlike ε_1's five, TWO of these are different
VALUES of the SAME quantity in the SAME lemma.** REVIEW_PLD_S3 l.463 said so, and **it has survived two
review cycles.** *Fourth naming finding of the session; added to [S24-flag 2a].*

### What the adoption would break: nothing — one recorded fact dies
**RLARGE l.65's "η_1 ≤ η_q", endorsed "CORRECT" by REVIEW_RLARGE_V2 §2.3, REVERSES** to η_1/η_q = 39.38
(N = 2) / 59.08 (N = 3); HIST l.186's route comparison reverses with it, **in the favourable direction** (the
RS route becomes **1551× better**). **Three consumers that COULD have failed did not:** RS-compatibility
(REVIEW_PLD_S3 l.305) holds with ×12.99 to spare; PLD's LD-arith no-go for SU(2)/SU(3) stands under both
forms; INH is unaffected. **The repair does not change a_RS's STATUS** — CONDITIONAL on (PLD)_k (i) before
and after, and REVIEW_PLD_S3 l.309 shows no threshold choice restores in-step derivation.

### Discipline
§0 pre-stated 15:11Z → ar1_criteria.md (**zero constants**) 15:20Z → first script 15:23Z.
**One FAIL reported as a FAIL:** ar1_margins.py's power line printed "NO POWER" through a **reporting bug**
(it compared two aggregate verdict strings, both "CONFIRMED", instead of the per-row BINDS/NOT-BINDING).
Script and output kept **byte-unaltered**; re-run as ar1b_power.py with criteria untouched — all verdicts
and gains **diff-identical**, **HAS-POWER**.
**Power constructed and run: the margin crosses zero at exponent p* = 3.61975 today** (3.23718 at the
proposed ε_1), with the sign flipping ±0.411 across it; **the hypothesis checks fail at t = 2, 10, 1000;
RS-compatibility fails at the counterfactual c_1 = 1/6.** Graded strong/medium/weak per check.
Exact Fraction; Decimal for display only, verified at 50 and 100 digits (worst disagreement 4.6e-49 decades).

**Biggest remaining in scope: not the arithmetic — THE DECISION.** One lemma replacement worth **82 decades
today**, hypotheses available bar one word, nothing broken. What stands in the way is that **RLARGE v3
already decided it the other way, without the price.** Below it: a_RS stays CONDITIONAL on (PLD)_k (i).

## TGAUGE_PRICE.md — verdict **EQUAL, exactly**, and now PROVEN rather than ARGUED. Route (β) CLOSED.
## 68.6 KB. §1 PRE-STATED 15,495 bytes, first edit 15:23 UTC. Three disclosed FAILs. 

### The explicit μ (PROVEN + COMPUTED)
The condition is exactly **A^{(0→k)}μ(X) = -Φ_k(c_X)** with μ = 0 at the level-k roots. Two solutions, with
s := (1 - n^{-d})^{-1}: **μ_flat** = Σ_X(-sΦ_k(c_X))(1_{B_X} - δ_{c_X}) — constant on each block with a
**one-site hole at the centre** — and **μ_pt** = Σ_X(-n^dΦ_k(c_X))δ_{c_X+e_0}, **one fine site per box**.
Both verified exactly, through the forward funnel, to set **Φ_k ≡ 0** in d = 2 (k = 2,3) and d = 4 (k = 1,2).

### Theorem TG-PRICE (PROVEN-HERE): the gauge is a NULL OPERATION
With P := n²⟨C(j),Y^p_0⟩, M := n²⟨Σ_l(Q_str^{(0→l)})^Tĵ_l, Y^p_0⟩ and 𝒯 the COF-res residue: M = P + 𝒯, and
**ΔP = n²⟨C(j),dμ⟩ = n²⟨D(S),μ⟩ = 0 for EVERY μ ∈ Λ₀** — because **d*C(j) = D^root(S) sits on the level-k
roots, and every composite gauge function is constant there.** Hence ΔM = Δ𝒯 = -𝒯, i.e.
**ρ = |ΔM|/|𝒯| = 1 exactly**, measured in **12 cells** (3 models × 2 fields × 2 μ) plus 4 in tg1.
**The gauge sends (M, 𝒯) ↦ (P, 0): the residue is RELABELLED, not removed — a NULL OPERATION on the
quantity to be bounded** (Corollary TG-NULL). **TP-F3, the only route to "strictly less", does not occur:
COF step (c)'s main pairing carries the SAME explicit n² as the residue.**

Independently, on the estimator's own terms: **Lemma TG-TV (PROVEN)** gives
‖d(A^{(0→l)}μ)‖₁ ≥ (n/L^l)^{d-1}osc₁(Φ) = Lemma TENT-TV's bound ÷ 2d, so **no μ beats the tent**; and
**Proposition TG-OPT** gives exactly ρ_tv(l) = s(1 + L^{-l}n^{1-d}) → 1 (657/656 and 1641/1640 at d = 4,
k = 2 — 0.15%). **So TENTQ's "natural but not forced" choice was OPTIMAL**, and §2.2 makes it moot.

### Termination and finite support — neither is the mechanism
μ **is** finitely supported — one level-k block, even **one fine site** — but from the witness's **compact
support**, not the termination; and **it does not help**, since the price depends on μ only through
A^{(0→k)}μ. The cheapest-support μ makes the ℓ¹×sup *estimate* **worst by exactly L^{k-l}** at an identical
exact price. **The termination pins the MAGNITUDE** (Φ_k(u) = -65/26244 for all k ≥ 2), so the equal price is
a **k-independent constant × n² — it survives every level.** It is **not** what forces the equality.

### >>> Route (β) is CLOSED. Face (b) IS an obstruction. The n² is real.
New invariant form offered: **(Y-N*)** — Theorem YH's norm with the inf restricted to Λ₀ — one statement,
**no (CC-0), no charges, no tent**; OPEN, sharpness OPEN, **expected false by n².**

### Two findings beyond the brief
1. **SOURCE-DISAGREES with TENTQ §2.7:** its display Σ_l⟨ĵ_l, d(ev^{(0→l)}μ)⟩ is **wrong** —
   **Q_str∘d = d∘A, the BLOCK AVERAGE**, not ev; checked exactly, **the ev form fails at every l ≥ 1.**
   (Size conclusion unaffected; **erratum, not refutation**.)
2. **>>> Proposition TG-EXCL — from the DESIGNED-FAIL CONTROL, and constructive.** The **root-delta μ would
   be cheaper by exactly L^{dk}** (ρ_root = 1/(L^{dk} - 1); measured 1/80, 1/728, 1/6560) — **but ΔP ≠ 0, so
   it is NOT a gauge. What would free face (b) is PRECISELY what Λ₀'s definition excludes.** *That is the
   sharpest statement of an obstruction produced today: not "we could not find a μ", but "the only μ that
   would work is exactly the one the gauge group does not contain."*

### Checks — and the worker found its own gates VACUOUS
tg1: 2.06 s, 79 MB, **three disclosed FAILs** — **clause Z: the script failed to implement its own
non-vacuity criterion, making three models' generic-field clauses VACUOUS, not PASSes**; the consequential
F; and clause E(ii), whose **criterion was wrong** (it omitted the root hole μ ∈ Λ_* forces). Outputs and
criteria kept **unaltered**; repaired under **tg1b** with criteria untouched: 4.07 s, 205 MB, **ALL PASS**,
ledger closed on one source. **Both designed-FAIL controls fired in ALL models** (a corrupted root offset
breaks TGAUGE; a flat straight-average multiplicity is rejected by its own mass assertion and breaks B4).
Outside references **rebuilt exactly**: COF-res's identity, TGAUGE, and S8-7's four rationals.
*Eighth and final application of the check-power lens — and this one caught its own clauses passing
vacuously. The practice is now fully formed and should be the first paragraph of every future brief.*

### Scope, and a one-sided limitation the worker volunteered
m = 0, trivial background, d = 4, L = 3, abelian/linearised, k ≤ 3. **§2.2 is UNCONDITIONAL on the profile
input, so YSUP's flagged Z″₀-cancellation attack point does not touch this verdict either way.** No
k-uniformity for (NC-Γ) claimed (RS10-1 stands, upstream). **One-sided limitation: COF step (c)'s r_m(Y^p)
terms are not inert under the shift and are not computed — any change is ADDITIONAL cost, so the verdict can
only move towards WORSE.**

### Biggest obstruction left
**Face (b) has NO representative-theoretic escape at all**, so the n² must be met either as **(Y-N*)** on
the response (**expected fatal**) or — **the one route not already expected to fail, requested to lane A** —
as **Σ_X|Q_X| ≲ n^{-2} on the SOURCE**, since max|Φ_k| ≤ 3.89·C₀ is k-uniform and **its lower bound is
attained.**

## GREENT.md — the Green's-function bound PROVEN, and the "≈16" price CORRECTED by 1.6e7. 699 lines.
## Outcome (G-O1). Two clauses FAILED, including a new failure mode: a gate UNSATISFIABLE BY CONSTRUCTION.

### 1. The statement needed — derived, and NL-8 named only one of its three parts
NLOC's consumer is a single number, the **cell sum 𝒮** in 𝔏_j ≤ d·𝔠_P·𝒮·L^{(d-1)n}. **Proposition NL-8's
own phrasing names only ONE of the three things it needs.** The correct list, at d = 4 on (ℤ/R)^d with
R = T·L^k:
- **(GT-1)** |∇_μG(x)| ≤ C_1|x|^{-(d-1)}, uniformly in R — the kernel of d₀*Δ₀^{-1} is **one** difference of
  the scalar G (Lemma GT-0);
- **(GT-2)** |∇_μ∇_λG(x)| ≤ C_2|x|^{-d} — **this is the one that does the work; (GT-1) alone gives a cell
  sum ≈ T, not log T**;
- **(GT-3)** a **FIRST-MOMENT** bound Σ_z|z - z₀|·|F₀(z)| — **the vanishing mean alone buys nothing.**
  Needs a new constant c_m⁽¹⁾ = Σ_X(|X|₁ + d)e^{-m′|X|₁} = **108.1·c_m** at the proven rate.

### 2. PROVEN, with explicit R-uniform constants
Route: 1-D Fourier bounds + an **exponential-tilt** bound giving Gaussian decay **with** the right
t^{-1/2}/t^{-1}/t^{-3/2} prefactor — **plain Chernoff has no prefactor and yields only |x|^{-(d-2)}, which
is exactly where a naive assembly dies** — plus periodisation at cost Ω ≤ 3.
**C₁ = 54, C₂ = 1703** (Euclidean); **429 and 27250** in coarse ℓ¹. **R-uniform, no logarithmic creep** (the
profile converges to 1.096 and 6.557 as s → ∞). Status: **COMPUTED upper Riemann sums of explicit elementary
integrals**, not closed form — the worker flags this as reviewer-attack item (i). Loose by ≈3e2 and ≈1e3
against the exactly computed maxima.
**>>> The zero mode NEVER enters** — every kernel entry is a difference of G, and the source is exact hence
mean-zero. **So the log T is NOT from the zero mode** (as the lead's brief supposed): **it is the ℓ¹ sum of
a |X|^{-d} profile over a box of side T, and hence IRREDUCIBLE.**

### 3. >>> The improved price is NOT ≈16 — the lead repeated this error too
| | value |
|---|---|
| NLOC Corollary NL-4's cell sum T^d | 2.80e28 |
| **GREENT's 𝒮_T at T = T₀** | **2.51e8** |
| **gain** | **1.11e20** |
| ideal (N-loc) at the same proven rate, c_m | 7.36e6 → **only 34× better** |

**"log T ≈ 16" is the log FACTOR; the constant in front is ≈1.5e7.** NLOC §L9 item 13 and its FOR OTHER
FILES item 7 ("down to log T ≈ 16") are **wrong as a price statement**, and **I repeated "10²⁸ → ≈16" in
HANDOFF.md and to the owner.** Logarithmic *growth* is confirmed (𝒮_T/log 2T ≈ 1e7 over T = 1e3…1e12).
*Corrected in HANDOFF.md item 1.*

### 4. Corollary NL-4 becomes NL-4′
Substitution c_m ↦ 𝒮_T and 𝔠_P ↦ 𝔠_P^coul, i.e. the factor **T^d/c_m = 3.8e21 replaced by 34.**
**A_soft = 1/L and all four exponent counts untouched.** Critically, **both legs come from ONE admissible
representative** (the Coulomb field at level 0 plus NL-3 step (3)'s nested correction) — which §L2 (A3)
requires and **NL-9 shows is exactly where the naive trade dies.**

### 5. T-uniformity: NO
**A log T is not T-uniform.** N1-15 is unconditional at **fixed** T ≥ T₀ with a **(log T)-sized constant**;
**the sup leg is T-uniform, the ℓ¹ leg is not.** **(N-loc-b)/(N-loc-cell) is still open and still needed for
layer 2.** **(N-bg) and (H-C)'s C_♭ clause are untouched — nothing here bears on them.**

### 6. Checks — and a NEW failure mode of the check-power lens
**PASS:** gt1-B (solver validated exactly; **two independent computations of the kernel column gave
byte-identical output**), **gt1-C (proof ≥ exact measurement: 53.6 ≥ 0.1698 and 1702.7 ≥ 1.7165)**,
**gt2-E (R-uniformity: both maxima DECREASE from R = 8 to 24)**, gt1b-A.
**FAIL gt1-A** — gt1_green.py's d* is **minus the true adjoint**, so it tested -Δ; script and output kept
unaltered, re-run as **gt1b-A: PASS, 0/23328 discrepancies.**
**>>> FAIL gt1-D, its re-run gt1b-D, and gt2-F** — the monotonicity gate **quantified over shells up to the
torus half-period, where reflection symmetry suppresses the kernel, so NO true power law could pass it: the
gate was UNSATISFIABLE BY CONSTRUCTION.** Post-hoc (labelled), a fixed-direction probe at R = 24 and 32 is
decisive: s⁴|b_A| bounded and falling (0.268 → 0.158) while s⁴|b_B| grows (0.347 → 0.572), local exponents
4.1-4.7 against 3.4-4.0. **The designed-FAIL arm does fail the d-th-power claim, so the gate had power — but
this is a post-hoc reading, not a passed gate**, and the worker says so.
*Ninth check-power finding, and a NEW mode: not a gate that cannot fail, but a gate that cannot PASS. Both
ends of the same defect — a criterion written without checking it is satisfiable by the truth.*

### 7. Could not pin
Closed forms for the two constants (quadrature-based upper sums). **The ≈1e3 of looseness is all in Lemma
GT-A's four integral bounds and the single-coordinate reduction costing d^{d-1} = 256 — sharpening it would
push 𝒮_T to ≈1e5-1e6, BELOW c_m**, and the worker flags it as **the cheapest remaining factor.** The
far-region bookkeeping in GT-4(b) is crude but **verified immaterial** (𝔠_i × 100 moves 𝒮_T by 0.19%).
