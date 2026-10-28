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
