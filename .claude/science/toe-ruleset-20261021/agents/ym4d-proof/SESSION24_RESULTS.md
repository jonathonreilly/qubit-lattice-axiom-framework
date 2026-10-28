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
