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
τ_R ≤ 2.75e-15 (**now the binding entry of τ_♭, displacing 1.43e-10**), η_♭ 1e-26 → 4.2e-36,
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
**>>> IT WAS WRITTEN CONCURRENTLY.** BFT_B session 9 §31's **Proposition NCR** is exactly that bound, in
product form, PROVEN-HERE and exact. The reviewer could not see it (the two ran in parallel). So (NC-Γ)'s
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
